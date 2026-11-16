# Decision log

Newest at the bottom. Each entry: what was decided, and why.

## Fri 13 Nov

- **Repo root is the working directory**, pushed to the private repo `timwuerfl/whose-memory`.
- **Toolchain.** `/usr/bin/git` and `/usr/bin/make` fail because the Xcode licence is not accepted on this Mac;
  we set `DEVELOPER_DIR=/Library/Developer/CommandLineTools`, which works without it. Python 3.12 comes from `uv`
  into `.venv`; caches (uv, Hugging Face, LLM responses) live under `cache/` (git-ignored).
- **Commit author** uses the GitHub noreply address, so no personal e-mail enters the history.
- **Adaption model id.** The docs' `glm-53-flash` is `glm-5.3-flash` on the live API. All 7 hosted models are
  visible to both keys.
- **Spend ledger** uses `usage.cost` from each response (verified against the price table for
  `deepseek-v4-flash`: 102 in + 63 out tokens → 1.29e-5 credits).
- **Hosted models emit reasoning tokens** by default; `max_output_tokens` must leave room for them.
- **One note per session, written from that session's trace alone.** This makes re-derivation (R) well defined:
  the same call, on the same trace, with an independent sample. Genuine notes are sampled at temperature 0.7 so that
  a re-derived note is never a byte-identical replay.
- **Pillar 1 "true-claim control".** The world is fictional, so a "true" and a "false" claim are symmetric to the
  model. We therefore (i) counterbalance which of two values plays the claim, (ii) keep the contradicting evidence
  in one fixed channel (a document excerpt) at a counterbalanced position, and (iii) add two controls: no claim
  (floor) and claim without contradicting evidence (ceiling).
- **Primary self-trust premium is label-only**: adoption(memory) − adoption(tool) with byte-identical neutral
  claim text, so that only the provenance header differs. First-person "I verified earlier that …" framing is the
  separate H1b ablation.
- **Literature check (63 verified references, `paper/notes/literature.md`).** No pillar is fully pre-empted;
  pillars 1, 3 and 4 are partly anticipated, so the paper claims only the deltas:
  P1 = first controlled comparison of a byte-identical claim attributed to the agent's own past note vs five other
  sources with ground truth (closest: Self-Correction Illusion 2606.05976, Who Flips? 2606.16011, Self-Attribution
  Bias 2603.04582); P2 = first evaluation of memory self-recognition against an adaptive forger ladder with matched
  same-model negatives; P3 = the head-to-head of five detector types on forged memory; P4 = signing and
  re-derivation fail on complementary cases (FARMA 2607.05029 already shows unsigned tags are spoofable, PoEM
  2608.16032 already shows HMAC ledgers work). Corrections to the planning doc: 2602.20031 is concept-injection
  detection, not prefill detection; "Manufactured Confidence" finds that source attribution inside memory text
  does *not* change uptake, so it is not a label-effect precedent; ASB reports no headline number for perplexity.
- **Title.** "Whose Memory Is It? Scope-Aware Commit Rules…" (2610.09008) already exists. We keep the working title
  for now and decide at writing time whether to change it; if kept, that paper is cited explicitly.
- **P1 addition prompted by the literature.** Khullar et al. report that an explicit "you wrote this" label alone
  did not create self-attribution bias, while placement in the model's own turn did. If the API accepts multi-turn
  input, P1 gets a seventh, secondary condition: the note delivered structurally as a prior assistant turn.
- **Verbal recognition (V) is asked without the trace**, with the rest of the episode's memory store as context.
  That is the realistic situation (memory is consulted because the trace is no longer in context) and it keeps V
  distinct from the consistency query C, which does see the trace.

## Fri 13 Nov, late evening — redesign around the request limit

- **The API allows about 70 requests/min in total** (key 1: 50/min, key 2: 25/min, rolling 60 s window shared
  across models; no token limit found; details in `SPECS.md`). Until Sunday midday that is roughly 100–150k
  requests, against the ~600k the first plan implied. Dollars are not the constraint; requests are.
- **Unit of a hosted call = one memory store of one episode.** Verbal recognition (V) and the consistency
  query (C) audit all 7 entries of a store in one call; the judge compares up to 7 note pairs per call; the
  downstream task asks all 5 of an episode's questions in one call; forgers rewrite an episode's 5 target notes
  per call. An attacked store contains exactly one forged entry, as in the threat model. Full specification:
  `experiments/README.md`. Local experiments keep single-entry queries (the GPU, not the API, limits them).
- **Sample.** 34 episodes per family (102 episodes, 510 attack instances per tier) for four hosted victims and
  20 per family (60 episodes, 300 instances per tier) for the large model; Pillar 1 uses 150 items per victim.
  That still meets the target of ≥ 300 forged notes per (victim, tier). Planned total: about 79k requests.
- **T3 for all five edit types** on hosted victims (packing makes candidates cheap): 4 calls × 2 rewrites per
  note = 8 candidates, ranked by the victim in one separate call per instance under a held-out phrasing.
- **One re-derivation per session** instead of two. The re-derived note also serves as the repair in the gate.
- **Reasoning stays on at the lowest effort** for every study call (one uniform setting; exact per-model
  parameter in `STUDY_EXTRA`). Turning reasoning off cost accuracy in the probe, and reasoning costs tokens,
  not requests.
- **Pillar 4 scope.** `none` and `G1` at T0, T2, T3; tag conditions at T2; a `no_memory` baseline (target entry
  removed) because for E3–E5 the cautious option can be right without any note.
- **Local genuine notes are sampled at temperature 0.7**, like the hosted ones, not decoded greedily: with greedy
  notes own-model surprisal would separate genuine from forged by construction.
- **Local adaptive tiers are formed post hoc** from one scored pool of 8 candidates per instance: T3 (victim's
  self-rating, held-out phrasing), T4s (lowest surprisal), T4d (lowest surprisal delta), T4c (highest
  consistency score), T4p (probe from an attacker split), plus a random-candidate baseline T2r.
- **Large model changed to `glm-5.2`.** `qwen3.5-397b` accepts only 3 requests in flight per key and spends
  3–9k reasoning tokens (about 100 s) per call even at the lowest effort, i.e. about 4 requests/min; the full chain
  would take two days. It joins Pillar 1 only (short single calls). `glm-5.2` runs the full chain on the reduced
  sample (60 episodes).
- **Client changes found necessary by the probe:** streaming responses (long reasoning calls otherwise end in
  HTTP 504 after 60 s), a cross-process request window, `max_output_tokens` 16,384 so that reasoning cannot
  starve the answer.

## Sat 14 Nov, 00:20 — after the first pilot reports

- **Pillar 1 redesigned as head-to-head conflicts.** Pilot (18 items, 2 victims): against a contradicting
  document the claim was adopted in ~10% of trials, ~68% escalated, and the memory note was the *least* followed
  channel (0-6%); with no contradicting evidence the claim was followed 100% of the time. The fixed-document
  design cannot rank channels at that floor. Main design: two channels assert the same sentence with different
  values; 7 channels (document added), 120 items per victim. H1 is kept as stated although the pilot points
  against it.
- **Reasoning setting.** Notes, re-derivations and judgement calls: reasoning on, effort "low". Forger pipeline
  (T1/T2/T3 rewrites, T3 ranking): reasoning off, 8,192 output tokens. In the pilot, packed rewrite calls with
  reasoning ran out of output budget (17 of 27 T1 calls by `gemma-4-26b-a4b-it`, 12% of ranking calls by
  `deepseek-v4-flash`).
- **E5 validity check tightened** (`asserts_certainty` in `memlab/attacks/template.py`): 5 of 12 genuine hedged
  pilot notes passed the old check. The dataset is unchanged by this (verified by regeneration).
- **Known attacker-side weaknesses, left as they are and reported:** the exact-phrase validity check rejects some
  paraphrases that do carry the attack (they are regenerated or excluded); `deepseek-v4-flash` shows a primacy
  bias when ranking T3 candidates (first-shown candidate wins 27 of 51 times), so its T3 is a weaker adaptive
  attacker than intended.
- **Pre-registration made binding** at this commit; detector and gate stages may be amended before their own
  main runs (section 9 of the pre-registration).

## Sat 14 Nov, 01:30 — reasoning off (pre-registration amendment 2)

- **What happened.** The main run (notes + Pillar 1) started at 00:25 with reasoning on. Billed throughput fell
  from ~65 to ~18-35 calls/min while the shared limiter kept reacting to 429s on every model of a key. Capping
  requests in flight per key at 12 did not help: calls then took ~80 s each. Output tokens per minute never
  exceeded roughly 100k for the account. Conclusion: with reasoning on, the provider's token throughput is the
  binding limit, not the request window.
- **Decision.** All main-study calls run with extended reasoning off (effort "none"; `glm-5.3-flash` at "low",
  which yields ~0-60 reasoning tokens there, because "none" leaks reasoning into its answer). This restores the
  request window (~69 calls/min) as the limit and removes the reasoning loops and truncations seen in the pilot.
  A small reasoning-on arm checks whether the conclusions survive reasoning.
- **Cost of the decision.** Results describe agents answering without extended reasoning. That is a weaker test
  of "agents cannot tell" than reasoning-on would be, and is stated as a limitation; the robustness arm bounds it.
- **Data set aside.** `results/raw/main_reasoning_low_aborted/` (1,943 rows) is kept for the record and for a
  descriptive comparison only.
- **Client:** shared per-key in-flight pool (`KEY_INFLIGHT_CAP`, default 12), 429 trail in
  `cache/llm/http429.log`, `experiments/status.py` for monitoring.

## Sat 14 Nov, 03:30 — gate pilot under reasoning off; run order

- **Gate pilot (6 episodes, 2 victims, reasoning off).** Baseline attack success on the target question is
  0.43-0.82 depending on victim and tier; clean accuracy 0.93-1.00, so no question type is at floor. No design
  change to Pillar 4; its main run uses the registered conditions.
- **Known flaw in E1 questions, left as is and reported.** The three wrong options of a factual-swap question
  are each one transposition away from the correct value, so the correct value can be guessed above chance
  without any memory (pilot: 3 of 6 and 1 of 6). Notes and forgeries were already being generated when this was
  found, and the registered `no_memory` baseline measures exactly this, so the dataset stays frozen. Consequence
  for reading the results: for E1, accuracy after an entry is removed or marked invalid overstates what the
  agent knows; per-edit-type results are reported.
- **Signed tags are a compliance test as well as a mechanism test.** In the pilot one victim followed an entry
  shown as `signature=INVALID` in half the cases, mostly where the question offers no "unknown" option. This is
  kept as an outcome, not treated as a prompt bug.
- **Four degenerate answers** (`gemma-4-31b-it` repeating one token up to the limit, reproducibly at T=0) stay
  missing, as registered.
- **Run order in practice.** Pillar 1 runs alongside note generation at low concurrency to use the part of the
  request window that note generation leaves idle. Stages that depend on each other (notes → forgeries →
  detectors → gate) keep priority.
- **Analysis code is developed on pilot files** (same formats) while the main run collects; pilot numbers never
  enter the paper.

## Sat 14 Nov, 04:00 — analysis conventions fixed before any main-run result was computed

The analysis code (`analysis/`) was written and tested on pilot files only. Where the pre-registration left a
detail open, the choice below was fixed now, before main data existed for the stage concerned:

- **Estimand 2** is registered as a criterion (upper CI bound < 0.65), not a test. For the Holm family its
  p-value tests AUROC = 0.65 (two-sided bootstrap). "Supported" follows the registered criterion; we also report
  whether it survives Holm.
- **Estimands 1 and 3** are directional; they count as supported if the estimate has the hypothesised sign and
  the Holm-adjusted p is below .05.
- **Estimand 3, choice of detector:** one detector for all victims, chosen by AUROC pooled over hosted victims
  and tiers T0-T3 against same-slot negatives on calibration episodes (ties go to C). The gate (G1) makes its own
  choice per victim on calibration episodes, as a deployed gate would; if the two choices differ, both are named.
- **Clustering:** pooled shares and ratios resample item or episode ids jointly across victims (the same items
  are shown to every victim); victim-averaged AUROCs resample episodes within victim.
- **Proportions at 0% or 100%** get Clopper-Pearson intervals instead of a degenerate bootstrap interval. If the
  mixed model for estimand 1 is not estimable because one side is (almost) never chosen, an exact binomial
  interval is reported in its place and this is stated.
- **TPR at fixed FPR:** an entry is flagged if its score is strictly above the threshold; the realised FPR is
  reported next to the nominal one (scores are integers 0-100 with heavy ties).
- **Missing answers** count as "attack failed" / "not followed" (registered); for confidence and accuracy
  outcomes they are dropped and counted.
- **Local, T4p:** episodes are split in two halves by hash; the attacker's probe is trained on one half and
  selects candidates for the other, and the defender's probes used against T4p are trained within the other half
  only. Local integrity gap: best of surprisal delta, consistency score and consistency probe chosen on
  calibration episodes at T0-T2, reported per adaptive tier and pooled over the T4 tiers.
- **Local limits found while building:** "own notes from other episodes" are not part of the local item set, and
  the third negative set (genuine entries inside attacked stores) does not exist locally because local scoring
  is per entry.

## Sat 14 Nov, 06:30 — detector re-pilot, local chain restart, size of the reasoning-on arm

- **Detector re-pilot with reasoning off (pilot seeds, 2 victims): no design change.** Parse rates 95-100%.
  V is flat: in 77 of 120 (`deepseek-v4-flash`) and 92 of 102 (`gemma-4-31b-it`) audited stores all seven entries
  got the same self-authorship rating. C separates. The cross-family judge marks every T0 forgery but also 32%
  of independently re-derived genuine notes as different in substance, so R has a real false-positive rate; the
  registered rule (better detector on calibration episodes) decides which one the gate uses. The detector agent
  never delivered its report; this assessment is from `hosted_detect --run pilot --summary` and
  `analysis.hosted --run pilot`.
- **Local chain restarted at 06:10.** The local pipeline's hosted calls (T1 forgeries, other-model notes) ran
  with `--rpm-scale 0.3`. The scale is applied to the shared request window, so these processes only sent when the
  whole account was below 30% of the limit, which was almost never: 109 of 300 T1 calls in 83 minutes, GPU idle.
  Restarted with the full window and with GPU forging in parallel. No data was discarded (completed calls are
  cached).
- **Reasoning-on robustness arm, size fixed now (amendment 2 left it open).** Victims: `deepseek-v4-flash` and
  `gemma-4-31b-it` (the pilot victims, for which reasoning at the lowest effort is known to complete within the
  output limit). Episodes: the first 10 main seeds per family (30 episodes per victim). Calls, all on the
  reasoning-off notes and forgeries of the main run so that only the judgement call differs: V and C on clean
  stores and T0/T2/T3 stores, R, downstream answers under `none` (clean, T0, T2, T3), and the Pillar 1 `pair`
  design on the first 40 items. About 4,000 calls. It starts when the main hosted stages have finished. If it
  cannot complete by Sunday 08:00 CET, completed cells are reported in the order V, C, downstream, R, Pillar 1.
  It is secondary and descriptive: differences to the main arm with paired bootstrap intervals, no tests.

## Sun 15 Nov, 23:30 — Deviations from the pre-registration: the laptop slept for 40 hours; sample and stage cuts

**What happened.** The laptop went to sleep on Sat 14 Nov at about 07:05 CET and woke on Sun 15 Nov at about
23:15 CET. The spend ledger shows no completed request in between; the short wake-ups only produced connection
errors (502 from the proxy), which are retried. All runners survived and resumed. At 23:20 the main run stood at:
Pillar 1 27-36% per victim (57% for `qwen3.5-397b`), forgeries complete for `glm-5.2` only, detectors and gate
started for `glm-5.2` only (7% and 4%).

**Budget.** 11 hours of runtime are left for data collection (until about 10:30 CET on Mon 16 Nov). The request
window is the binding limit: 69 requests/min, about 4,100 per hour, 44,000 in 10.7 hours if the window is full
all the time; the planning figure is 36,000 completed calls (the hours before the sleep averaged 3,200). The
registered design still needs about 70,000: Pillar 1 13,700 (10,800 head-to-head trials, 2,900 confidence
trials), forgeries 2,300, detectors 26,200 (56 calls per episode), gate 23,700, local hosted calls 500,
reasoning-on arm 4,000.

**Rule used for the cut.** Decided from request counts alone. No main-run detector or gate response has been
inspected, and no Pillar 1 outcome was looked at for this decision (only job ids and error flags were counted).
All four primary estimands and all five hosted victims are kept; what is cut is sample size and secondary cells.

1. **Hosted chain on 60 episodes per victim.** Forgeries, detectors and gate run on seeds 50-69 of each family
   (60 episodes, 300 attack instances per tier) for all five hosted victims. This is the sample registered for
   `glm-5.2`; the other four were registered at 102 episodes. Calibration split unchanged (hash, 25%). Notes and
   re-derivations exist for all 102 episodes and stay in the repository; forgeries already generated for seeds
   70-83 are not used.
2. **Detectors: V, C and R first, on all tiers T0-T3.** Matched negatives and 2AFC move behind the gate (below).
3. **Gate: `none` and `G1` first (primary estimand 4), then `G2u`, `G2s`, `G1+G2s` (H5).** `no_memory` and
   `G2s_insider` move to the stretch list.
4. **Pillar 1: designs `pair` and `framing` are completed on all 120 items for all six victims** (primary
   estimand 1, Bradley-Terry ranking, H1b). The designs `turn`, `forced`, `single` and `stale` stop where they
   are (about a third of the items per victim, half for `qwen3.5-397b`; the runner works through items in a fixed
   order that does not depend on responses) and move to the stretch list. **Confidence trials (H1c) run on the
   first 20 seeds per family (60 of 120 items).**
5. **Reasoning-on robustness arm: not run.** It was secondary and descriptive, and its size (about 4,000 calls
   at reasoning-token throughput) does not fit.
6. **Stretch list, run only after every item above has finished, in this order, no new stage after 09:10 CET:**
   matched negatives for V; gate conditions `no_memory` and `G2s_insider`; 2AFC; the remaining Pillar 1 designs;
   the remaining confidence items. Whatever is incomplete at the end is reported as incomplete with its counts
   (pre-registration §5).

**Planned calls after the cut:** forgeries about 1,000, detectors 14,400, gate 12,300, Pillar 1 6,400,
confidence 1,440; together about 35,500. The run is driven by `experiments/run_remaining.sh`
(log: `results/logs/cut_driver.log`); every stage is resumable and uses the existing flags of the runners
(`--limit`, `--per-family`, `--parts`, `--conditions`, `--designs`), so no runner code changed.

**Other.** The local chain (GPU) is not request-limited and continues unchanged. A `caffeinate` guard keeps the
machine awake on AC power for the remaining runtime.

## Mon 16 Nov, 02:45 — P1 runs restarted with reserved request tickets; 16 minutes of P1 time lost

Not a design change: same commands, seeds, designs and outputs as in the 23:30 entry. Only the scheduling changes.

- **What I saw.** At 02:24 the five P1 runs (pair and framing trials) were at 58–69% and were getting 6 requests a
  minute between them, about 9% of the window. At that rate P1 would finish last, after 08:30.
- **Why that is wrong.** The pre-registration puts P1 first in the priority order, and the P1 tidy files are only
  written when a run ends, so the analysis would have no final P1 data for five of six victims until the end.
- **Cause.** The client lets 12 requests per key be in flight across all processes (lock-file tickets). A worker
  that finishes a call takes its next ticket at once, so the stages that hold tickets keep them. The detector
  stages held nearly all 24; a 70-second probe with four workers got none.
- **What I did.** Stopped the five P1 stages of `experiments/run_remaining.sh` (the driver's other stages were not
  touched) and restarted them from `experiments/run_p1_boost.sh` with `MEMLAB_KEY_INFLIGHT=18`. The P1 processes
  then see six extra tickets per key that the other stages do not use. In-process concurrency stays at 3 per key.
  Finished trials are read back from the raw files and the cache, so nothing is repeated.
- **My mistake on the way.** The first three restarts (02:25, 02:30, 02:37) were started without network permission
  for the API host, so their requests never left the machine. P1 made no progress from 02:25 to 02:41. The first
  of the three (24 threads per key) also took request-window slots for requests that were never sent, which
  roughly halved the other stages' throughput from 02:26 to 02:29 (about 150 calls lost). No data were affected:
  failed sends write no rows.
- **Risk.** Up to 18 tickets per key can now be held, against the cap of 12 that was set after 429 errors with
  long reasoning calls. Most ticket holders are waiting for the request window, not in flight; I watch the 429
  count and go back to 12 if it rises.
- **Effect on the budget.** None on the total (about 68 requests a minute). Remaining core work at 02:24 was
  about 25,400 calls against about 31,500 available before the 10:11 cutoff. No results were inspected.

## Mon 16 Nov, 05:00 — Analysis conventions added after the reviewer round (paper session)

Three reviewer sub-agents read the draft at 04:45. At that time the detector stage was complete for one victim
and partial for three, the gate (none, G1) was complete for `glm-5.2` only, and no tag, 2AFC, matched-negative
or local T1/T4p result existed. The following analysis choices were made then. None was chosen by looking at
which variant gives the larger effect; the effect of each on the numbers available at 05:00 is stated.

1. **Completeness guard for means over victims** (`analysis/common.py`, `MIN_CELL_SHARE = 0.5`). A victim whose
   cell holds less than half of the instances of the largest victim cell is left out of that mean. Reason:
   `gemma-4-31b-it` had entered estimand 2 with 6 forged and 2 genuine entries at full weight. Effect at 05:00:
   V at T2 0.629 [0.600, 0.669] → 0.640 [0.621, 0.660]; H2 is "not supported" either way.
2. **Integrity gap on common entries** (`analysis/detection.py`, `primary3`). The gap AUROC(best log-based
   audit) − AUROC(V) at T3 is computed on the forged entries that both audits have scored. Before, each audit
   used its own set (1,048 vs 1,195 stores while C was still running). Effect: 0.378 → 0.349; supported either way.
3. **All attack-success rates on evaluation episodes** (`analysis/p4.py`, `usable`). The gate must be evaluated
   on evaluation episodes because its threshold is fixed on the calibration split; the no-defence and tag
   conditions were computed on all episodes, so a figure showed two different sets of attack instances.
   Estimand 4 was already matched and does not change (98.9%). Descriptive no-defence rates move from
   55.3/61.2/58.3% to 57.9/62.0/59.1% (T0/T2/T3, `glm-5.2`).
4. **Staleness comparison on the same items** (`analysis/p1.py`). The unmarked net preference reported next to
   the stale trials is computed on the items that have stale trials (before: all items).
5. **Re-derivation judge left as run.** The detector sub-agent and the methodologist both pointed out that the
   judge sees only-genuine or only-forged batches and that the judge model differs for the DeepSeek victim
   (`memlab/config.py:judge_for`), which confounds judge and victim. Re-running was not possible in the time
   left. The paper reports R per victim, names both problems, and draws no conclusion that depends on R.
6. **Reporting.** H1b, H1c and the own-turn trials are now in the main text; the per-edit-type table
   (`paper/tables/edit_summary.tex`) and per-edit attack-success macros were added; token cost per audit call
   comes from `analysis/audit_tokens.py` (reads raw rows, writes `results/processed/main/audit_tokens.json`).

## Mon 16 Nov, 08:15 — Core finished at 08:05; how the stretch list is run

All core stages of the 23:30 entry ended with rc=0 by 08:05 (P1 pair, framing and confidence trials for six
victims; forgeries, detectors V, C, R and the gate conditions none, G1, G2u, G2s, G1+G2s for five victims on
seeds 50–69). The stretch list keeps its logged order. Three points differ from the 23:30 entry; all were decided
from job counts, with no results inspected.

1. **2AFC runs next to the extra gate conditions, not after them.** The driver would skip any stage that starts
   after 09:06, and the extra gate conditions (about 3,000 calls) end near that time. I pause the driver once it
   has started `no_memory` and `G2s_insider`, and start the 2AFC from `experiments/run_stretch2.sh`.
2. **Remaining P1 designs (turn, forced, single, stale) only on the items of seeds 50–69.** That is 60 of 120
   items, 520 trials per victim, of which about 310 per victim are still missing. The full set would need about
   4,150 calls and would not finish; what exists so far covers the families unevenly because the trials were
   run family by family. Seeds 50–69 are the seeds of the hosted chain. Trials already made for other seeds stay
   in the data; analyses of these four designs should restrict to seeds 50–69.
3. **Remaining confidence items are not run.** Confidence trials stay at the first 20 seeds per family (60 items).

No new API stage starts after 09:55 (first written as 09:40; moved at 08:27 because the last P1 designs take a few
minutes each). Everything still running is stopped at about 10:15.

## Mon 16 Nov, 08:20 — Scope of the secondary Pillar 1 designs (paper session)

Before the outage the stale, forced, single-source and own-turn trials had run on the items reached in
family-major order: all 40 inventory items and, for some models, up to 30 research items; no assistant item. The
run session now collects these designs on seeds 50-69 of every family (60 items, 20 per family). Rule, coded in
`analysis/p1.py:secondary_scope` before any of the new trials was analysed: per design, if every one of the six
models has at least 54 of those 60 items, the design is analysed on seeds 50-69 only, so that families and
models are balanced; otherwise on all items collected, and the paper states the family composition. Trials left
out by the rule stay in the processed files. Reason: the size of the channel effect differs strongly between
task families, so an inventory-heavy sample is not comparable with the 120-item main trials.

## Mon 16 Nov, 10:00 — Hosted runs closed at 09:55; what ran and what did not

All hosted stages ended with rc=0; no stage failed or was skipped, and nothing had to be stopped. No API calls
after 09:55. Since the restart at 23:31: 41,828 billed calls, $17.44; total spend $27.06 of the $1,500 cap.

**Ran in full (as cut in the 23:30 entry)**
- P1 pair and framing trials on 120 items and confidence trials on 60 items (first 20 seeds per family), for six
  victims.
- Forgeries T0–T3, detectors V, C, R, and gate conditions none, G1, G2u, G2s, G1+G2s, for five victims on seeds
  50–69 (60 episodes per victim).

**Stretch list, ran in full**
- Matched negatives for V (`v_negs.jsonl`), five victims.
- Gate conditions `no_memory` and `G2s_insider`, five victims, 60 episodes.
- 2AFC (`afc.jsonl`), five victims. For `glm-5.3-flash`, 14 of 240 calls ended at the output-token limit on every
  attempt and are unscored (70 of 1,195 rows); `qwen3.8-27b` has 9 unscored rows from answers that did not parse.
- Secondary P1 designs (stale, single, forced, turn) on the 60 items of seeds 50–69, six victims, complete. Trials
  from Saturday on other seeds (12 to 38 more items per victim, family coverage uneven) are also in the tidy
  files; analyses of these designs should restrict to seeds 50–69.

**Not run**
- Hosted chain on seeds 70–149 (the registered 140 episodes for the four small victims).
- Confidence trials on the other 60 items; secondary P1 designs on seeds 70–89.
- The reasoning-on robustness arm (`main_reasoning_low`).

**Known gaps inside what ran**
- `gemma-4-31b-it` has fewer detector and gate rows than the other victims (for example 8,127 V rows against
  8,785). Some of its genuine notes are missing from the notes stage, so V and C skipped 4 of its 60 episodes
  and 76 stores; 15 of its 1,192 forgery rows are marked not valid (8 for `glm-5.2`).
- P1 answers that did not parse: `gemma-4-31b-it` 30 of 1,680 pair and framing trials and 8 of 240 confidence
  trials; `qwen3.8-27b` 2 of 1,680.

## Mon 16 Nov, 10:10 — Final refresh on closed data (paper session)

After the run session's close-out (entry above) the analysis was rerun once on the final files. Outcome of the
08:20 scope rule: stale, forced-choice and own-turn trials are complete on the 60 balanced items for all six
models and are reported on those items alone; the single-source design covers 34 items and is reported on all
of them with its family composition. Added for the stretch data, with no change to any registered estimand:
per-edit 2AFC macros (`analysis/numbers.py`), two appendix tables (`controls_afc`, `controls_negs` in
`analysis/tables.py`), and the corresponding sentences in sections 3.1, 3.2 and 3.4 and in the appendix. The
confidence trials remain at 60 items and the reasoning-on arm was not run.
