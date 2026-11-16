# Submission notes

For the Apart Research AI x Epistemics sprint (13–15 Nov 2026). Nothing has been submitted; this file collects
what the submission form asks for.

## Title

Whose Memory Is This? AI Agents Follow an Unchallenged Note and Cannot Spot a Swapped Fact Without the Session Log

## Authors

Tim Würfl, with Claude Code (Anthropic).

## Abstract (249 words)

AI agents that work across sessions keep notes, and anyone with write access to the memory store can replace one. We ask how agents weigh a note labelled as their own and whether they can tell it from a forgery. In MemLab, a synthetic environment, a graded forger replaces one of seven notes; we test five hosted open-weight models and one local model, without extended reasoning, under a pre-registered design. We hypothesised that agents over-trust their notes. They do not when a conflict is visible: against a contradicting tool output they flag the conflict in 61.3%, follow the tool in 37.9% and the note in 0.6%. Unchallenged, the note is taken as given: a forged note with a swapped fact steers the decision in 93.2% of cases. Inspection does not protect. Asked which entries they wrote, models reach an AUROC of 0.62 against a forger writing in their style and 0.50 for swapped facts; imitating their style adds nothing beyond fluency. Given the session log, the same audit reaches 0.99, and a gate built on it cuts attack success by 97.6%, an upper bound: the log is assumed intact and no forger targeted the auditor. A signature shown to the model as invalid still leaves 26.5% attack success. In the local model, surprisal of a note given the log carries the signal and an authorship probe does not. An agent's confidence in a note is no evidence for it. What helps is keeping the evidence it was written from.

## Track

Track 2, Trust Infrastructure (primary), with Track 1 as secondary.

## Files

- Paper: `paper/main.pdf` (Apart template style; core text to page 8, then references and appendix;
  "Dual-Use and Ethical Considerations" is Section 6 of the main text).
- Repository (private): https://github.com/timwuerfl/whose-memory
  The repository is private. Judges need access, or the repository has to be made public before submission;
  that decision is the submitter's.

## Pre-existing work to declare

None. Environment, experiments, analysis and paper were written during the sprint. The models used are
third-party open-weight models (hosted through Adaption Labs; one run locally).

## Use of AI assistance

Design decisions, code, experiments, analysis and text were produced with Claude Code under the author's
direction, as stated on the title page. Three reviewer passes (methodology, sprint judging criteria, AI-safety
domain) were run by sub-agents and their findings were incorporated (see `DECISIONS.md`, entry of 16 Nov 05:00).

## Things a judge may ask about

- **Pre-registration.** `PREREGISTRATION.md`, with two amendments recorded in the file. Of the four primary hypotheses, H1 (agents over-trust their own notes) was refuted with an effect
  in the opposite direction; the other three registered criteria are met.
- **Deviations.** A 40-hour outage of the machine (the laptop slept) forced a cut from 102 to 60 episodes per
  hosted model and the loss of the reasoning-on robustness arm. All deviations and the analysis conventions
  added afterwards are listed in the paper's Appendix B and in `DECISIONS.md`.
- **Scope.** Synthetic environment; single calls without extended reasoning; open-weight models from four
  families; the gate result assumes an intact session log and a forger that does not write for the auditor.
- **Cost.** $27.06 for 65,379 billed calls at Adaption Labs, the only paid service used (limit $1,500); ledger in `results/spend_ledger.csv`.

## Checklist before submitting

- [ ] Read `paper/main.pdf` once.
- [ ] Decide whether to make the repository public or to invite the judges.
- [ ] Submission closes Sun 15 Nov 23:59 AoE, which is Mon 16 Nov 12:59 CET.
