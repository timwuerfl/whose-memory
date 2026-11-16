"""Resumable bulk job runner on top of AdaptionClient.

Each finished job becomes one JSON line in ``out_path``::

    {job_id, model, meta, text, reasoning, usage, cost, cached, error, parsed, attempts}

Re-running with the same ``out_path`` skips jobs that already have a row without ``error``.
Rows whose parse failed (``parsed: null``, ``error: null``) count as finished.
"""
from __future__ import annotations

import asyncio
import json
import os
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Optional

from tqdm.auto import tqdm

from .adaption import AdaptionClient, BudgetExceeded


@dataclass
class Job:
    job_id: str
    model: str
    input: Any
    instructions: Optional[str] = None
    max_output_tokens: int = 1024
    temperature: float = 0.0
    sample_idx: int = 0
    tag: str = ""
    meta: dict = field(default_factory=dict)
    extra: Optional[dict] = None


def load_rows(out_path: str | Path) -> list[dict]:
    """All rows of a JSONL output file (tolerates a truncated last line)."""
    p = Path(out_path)
    if not p.exists():
        return []
    rows = []
    with open(p) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return rows


async def run_jobs(client: AdaptionClient, jobs: list[Job], out_path: str | Path, *,
                   parse: Optional[Callable[[str], Optional[dict]]] = None, desc: str = "",
                   max_parse_retries: int = 2, n_workers: Optional[int] = None,
                   fsync_every: int = 50) -> list[dict]:
    """Run ``jobs`` concurrently, appending one row per finished job to ``out_path``.

    Returns all rows (old + new), one per job, in job order (jobs that could not run, e.g.
    after ``BudgetExceeded``, are missing). Re-raises ``BudgetExceeded`` after flushing.
    """
    ids = [j.job_id for j in jobs]
    if len(set(ids)) != len(ids):
        raise ValueError("duplicate job_id in jobs")
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    latest: dict[str, dict] = {}
    for row in load_rows(out_path):
        jid = row.get("job_id")
        prev = latest.get(jid)
        # keep the latest successful row; an error row never replaces a success
        if prev is None or prev.get("error") or not row.get("error"):
            latest[jid] = row
    todo = [j for j in jobs if j.job_id not in latest or latest[j.job_id].get("error")]

    stats = {"cost": 0.0, "err": 0, "pfail": 0, "cached": 0}
    bar = tqdm(total=len(jobs), initial=len(jobs) - len(todo), desc=desc or "jobs",
               dynamic_ncols=True, smoothing=0.05)
    f = open(out_path, "a")
    n_written = 0
    last_sync = time.monotonic()
    budget_exc: list[BaseException] = []

    def write_row(row: dict) -> None:
        nonlocal n_written, last_sync
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
        n_written += 1
        if n_written % fsync_every == 0 or time.monotonic() - last_sync > 10:
            f.flush()
            os.fsync(f.fileno())
            last_sync = time.monotonic()

    async def do_job(job: Job) -> None:
        total_cost = 0.0
        attempts = 0
        parsed = None
        c = None
        for pa in range(max_parse_retries + 1):
            c = await client.complete(job.model, job.input, job.instructions,
                                      max_output_tokens=job.max_output_tokens,
                                      temperature=job.temperature,
                                      sample_idx=job.sample_idx + 1000 * pa, tag=job.tag,
                                      extra=job.extra)
            attempts += 1
            total_cost += 0.0 if c.cached else c.cost
            if c.error:
                break
            if parse is None:
                break
            try:
                parsed = parse(c.text)
            except Exception:
                parsed = None
            if parsed is not None:
                break
        row = {"job_id": job.job_id, "model": job.model, "meta": job.meta, "text": c.text,
               "reasoning": c.reasoning, "usage": c.usage, "cost": total_cost,
               "cached": c.cached, "error": c.error, "parsed": parsed, "attempts": attempts}
        write_row(row)
        latest[job.job_id] = row
        stats["cost"] += total_cost
        stats["cached"] += int(c.cached)
        if c.error:
            stats["err"] += 1
        elif parse is not None and parsed is None:
            stats["pfail"] += 1
        bar.update(1)
        bar.set_postfix(cost=f"{stats['cost']:.4f}", err=stats["err"], pfail=stats["pfail"],
                        cached=stats["cached"], refresh=False)

    queue: asyncio.Queue = asyncio.Queue()
    for j in todo:
        queue.put_nowait(j)
    n_workers = n_workers or max(1, client.total_concurrency * 2)

    async def worker() -> None:
        while not budget_exc:
            try:
                job = queue.get_nowait()
            except asyncio.QueueEmpty:
                return
            try:
                await do_job(job)
            except BudgetExceeded as e:
                budget_exc.append(e)
                return

    try:
        await asyncio.gather(*(worker() for _ in range(min(n_workers, max(1, len(todo))))))
    finally:
        f.flush()
        os.fsync(f.fileno())
        f.close()
        bar.close()
        client.flush_ledger()
    if budget_exc:
        raise budget_exc[0]
    return [latest[j.job_id] for j in jobs if j.job_id in latest]


def run(client: Optional[AdaptionClient], jobs: list[Job], out_path: str | Path, **kwargs) -> list[dict]:
    """Synchronous wrapper around :func:`run_jobs` (creates a client if ``client`` is None)."""
    own = client is None
    client = client or AdaptionClient()

    async def _go():
        try:
            return await run_jobs(client, jobs, out_path, **kwargs)
        finally:
            if own:
                await client.close()
            elif client._http is not None:  # http client is bound to this event loop
                await client._http.aclose()
                client._http = None
                client._loop = None

    return asyncio.run(_go())
