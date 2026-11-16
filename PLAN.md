# PLAN — "Whose Memory Is This?"

Apart AI x Epistemics sprint, 13–15 Nov 2026. This file describes the study as it was run. The reasons for
every change from the first plan are in `DECISIONS.md`; the binding design is `PREREGISTRATION.md`
(amendments in its section 9).

## The chain we test
1. **Trust (P1).** How does an agent weigh a claim in its own memory note against the same claim arriving
   through another channel (tool, web, user, other agent, unattributed context, document)?
2. **Recognition (P2).** Can an agent tell which notes it wrote, as forgers get stronger (T0→T4)?
3. **Signal (P3).** Where does an integrity signal live: verbal self-report (V), a consistency check against the
   session log (C), re-derivation from the log (R), own-model surprisal (S), activation probes (P)?
4. **Gate (P4).** Does a model-native gate (G1) or a provenance tag (G2, unsigned vs HMAC-signed) stop the attack?

## Setup
- Hardware: Apple M4 Pro, 24 GB, macOS. Local model on PyTorch MPS.
- Hosted API: Adaption Labs, two keys, about 69 requests/min in total. Requests, not dollars, are the constraint.
- Hosted victims (full chain): `deepseek-v4-flash`, `qwen3.8-27b`, `gemma-4-31b-it`, `glm-5.3-flash`, `glm-5.2`.
  `qwen3.5-397b` takes part in P1 only. Judges and T1 forgers come from another model family.
- Local victim: `Qwen/Qwen3.5-4B` (surprisal, logit read-outs, probes, T4 forgers).
- All main-study calls run with extended reasoning off (amendment 2).

## Environment (`memlab/`)
- 3 task families (inventory, research, assistant). An episode has 7 sessions; the agent writes one note per
  session from that session's log alone. Each episode carries one attack opportunity per edit type (E1 factual
  swap, E2 injected instruction, E3 forged conclusion, E4 forged commitment, E5 confidence inflation), each with
  a four-option downstream question whose answer flips if the edit is believed.
- One hosted call handles one memory store (7 notes) of one episode.

## Experiments as run
| | What varies | Outcome | Sample |
|---|---|---|---|
| P1 | two channels assert different values (7 channels); neutral, first-person, forced, single-source, stale | which source is followed, or conflict flagged | 120 items × 6 models (neutral and first-person on all items; other variants on a subset) |
| P2 | genuine vs forged (T0–T3), matched negatives, 2AFC | AUROC of V | 60 episodes × 5 models, 300 forged notes per tier and model |
| P3 | V vs C vs R (hosted); S, logit read-outs, probes, T4 (local) | AUROC, TPR at 5% FPR | same notes; local: 150 episodes |
| P4 | none, G1, G2u, G2s, G1+G2s (plus no-memory and insider if time) | attack success, clean accuracy, extra calls | evaluation episodes (75%) |

Registered sample for four hosted victims was 102 episodes. A 40-hour outage of the machine (Sat 14 – Sun 15 Nov)
forced the cut to 60; see `DECISIONS.md`, "Sun 15 Nov, 23:30". The reasoning-on robustness arm was dropped.

## Code map
- `memlab/`: environment, prompts, forgers, defences, API client with spend ledger.
- `experiments/`: runners (`hosted_gen`, `hosted_detect`, `p1_self_trust`, `p4_gate`, `local_pipeline`),
  `run_remaining.sh` (driver after the outage), `status.py`.
- `analysis/`: everything from processed rows to `paper/numbers.tex`, figures and tables
  (`python -m analysis.reproduce --run main`).
- `paper/`: LaTeX source; every number in the text is a macro from `paper/numbers.tex`.

## Gates
- Pilot on disjoint seeds before the registration became binding; parse rates of at least 95% per stage.
- Spend: hard stop at $1,500; ledger in `results/spend_ledger.csv`.
