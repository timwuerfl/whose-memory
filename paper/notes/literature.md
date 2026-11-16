# Literature check: "Whose Memory Is This?"

Checked 2026-11-13. Every row was checked against the arXiv API record (title, full author list, first-submission date, abstract). Where the abstract did not say what was actually measured, I also read the arXiv HTML; those rows are marked (HTML). Forethought pages and RFC 6962 were fetched from their own sites. BibTeX for every verified row is in `paper/refs.bib`. Nothing in this file comes from memory alone.

Search coverage: arXiv API, sorted by submittedDate. Queries: memory poisoning/agent, memory integrity, memory injection, forged + memory + agent, provenance + memory + agent, memory tampering / tamper-evident, self-recognition, own outputs, self-authorship, prefill + introspection/detect, source label/attribution + trust, signed/HMAC/cryptographic + memory + agent, self-attribution, generated vs retrieved context, re-derive/recompute + memory, probes + memory poisoning, tampered context + probes. I did not use Google Scholar, Semantic Scholar, OpenReview or ACL Anthology. Non-arXiv venues (for example a workshop paper that is not on arXiv) could therefore be missed.

---

## 1. Table

### 1a. Candidate citations

| key | verified? | exact title | what it actually shows | how we differ |
|---|---|---|---|---|
| karamchandani2026farma | yes (HTML) | Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses | FARMA injects forged *reasoning traces* into agent memory (e.g. "safety step already done"). In 50-trial evaluations it beats keyword filters and A-MemGuard. SENTINEL is a 5-layer pipeline (keyword, provenance/IFC label, taint, pattern, "Reasoning Guard" with 5 weighted structural signals). The provenance layer is beaten by **spoofed metadata (source=AGENT, VERIFIED)**. | Its spoofed-label result is a single attack/defence case. We measure the trust premium of the "own note" label, self-recognition under a forger ladder, and a signed-vs-unsigned comparison. |
| wei2025amemguard | yes | A-MemGuard: A Proactive Defense Framework for LLM-Based Agent Memory | Defence that combines consensus over reasoning paths from related memories with a separate "lessons" memory. Reports >95% ASR reduction. | Content-consensus defence. It does not test authorship or provenance, and FARMA shows it can be defeated. |
| zhang2024asb | yes (HTML) | Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents | Benchmark: 10 scenarios, 13 backbones, 27 attack/defence types. Memory-poisoning defences (PPL detection, LLM-based detection) are reported as ineffective. See section 5. | Their PPL is unconditioned text perplexity of the retrieved plan. Ours is own-model surprisal conditioned on the logged trace. |
| ardoin2026selfrecognition | yes (HTML) | LLM Self-Recognition: Steering and Retrieving Activation Signatures | Mostly a watermark paper. A random sparse steering vector added during generation gives a fingerprint that the model's own activations can recover (>98% multi-LLM attribution). Its baseline "self-recognition" is **own-LLM text vs human text** (XL-Sum summaries; Llama-3.1/3.2, Ministral). An LDA linear probe on mean activations reaches AUROC ≈99–100. Perplexity is ≈97–99.7 AUROC **when conditioned on the original prompt** but falls to ≈32–52 without it. | Its negatives are human text, not same-model or other-model forgeries. Its prompt-conditioning result is the closest precedent for our trace-conditioned surprisal delta (cite it as such). |
| panickssery2024recognize | yes | LLM Evaluators Recognize and Favor Their Own Generations | GPT-4 and Llama 2 tell their own summaries from other LLMs' and humans' better than chance. After fine-tuning, self-recognition correlates linearly with self-preference. | Summaries in an evaluator setting. Ours are agent memory notes with adversarial forgers and a downstream adoption outcome. |
| lindsey2026introspective | yes | Emergent Introspective Awareness in Large Language Models | Concept injection into activations. Models sometimes notice and name injected concepts. Some models use recalled prior intentions to **tell their own outputs from artificial prefills**. Claude Opus 4/4.1 are strongest. | Single-turn prefills and injected concepts. We test cross-session memory notes, where the original activations are gone. |
| pearsonvogel2026latent | yes | Latent Introspection: Models Can Detect Prior Concept Injections | Qwen-32B. A logit lens shows the residual stream detects *injected concepts* even though sampled outputs deny it. Accurate prompting about introspection raises sensitivity from 0.3% to 39.9%. | About concept injection, **not prefill detection**. It supports our verbal-vs-internal split (pillar 3). |
| kwon2026manufactured | yes (HTML) | Manufactured Confidence: How Memory Consolidation Turns Hearsay into Confident Facts | mem0/LangMem-style consolidation de-hedges remarks into flat facts that agents act on. In memory, a **bare, user-attributed and forged "system of record"** claim all grant alike (≈0.81). Hedges collapse grants. A passive "unverified" tag is ignored. Proposed fix: keep tentative phrasing at write time. See section 3. | They vary attribution *inside the memory text*. We vary the *channel/author label* (own note vs tool/web/user/agent/unlabelled) on byte-identical claims, and add authorship detection and gating. |
| mao2026pasb | yes | Agents Don't Just Agree, They Remember: Benchmarking Persistent Sycophancy in Self-Improving Personal Agents | PASB: 1,600 tasks, 16 models, Hermes-Agent/OpenClaw. A saved user claim raises downstream failure to 68.1% vs 35.6% when unsaved. In 38.8% of runs the saved note states the claim with more authority than the user gave it. | The note's content is the user's claim. They do not hold content fixed while varying the author label, and they do not test forgery or authorship. |
| bensal2026mist | yes | Recalling Too Well: Sycophancy Evaluation and Mitigation in Memory-Augmented Models | MIST benchmark. Memory amplifies sycophancy by up to 40% over in-context baselines. Lossy extraction is the main culprit. | Sycophancy through memory extraction. No authorship or provenance manipulation. |
| kumar2026authority | yes (HTML) | Authority Bias in Language Models: Source Deference and User Agreement Are Not Interchangeable | A "verified source" note flips 45–88% of correct answers in 7/8 models. Source-deference and user-agreement directions are causally separable. The authority direction is near-orthogonal to the assistant-persona axis. | Source-vs-user authority. There is **no "own memory note" condition**. |
| wu2024clasheval | yes | ClashEval: Quantifying the tug-of-war between an LLM's internal prior and external evidence | Models adopt incorrect retrieved content over correct priors >60% of the time, modulated by how far the perturbation deviates and by prior confidence. | Retrieved-vs-parametric conflict. We study a label effect with content held constant. |
| rfc6962 | yes | Certificate Transparency | Append-only, publicly auditable Merkle-tree logs of TLS certificates. | Design analogy for tamper-evident memory logs. |
| cottonbarratt2025designsketches | yes | Design Sketches: Collective Epistemics (Cotton-Barratt, Vaintrob, Sourbut; 25 Dec 2025) | Sketches five technologies, including "provenance tracing" (see where claims came from and how robust they are). | Motivation. We give an agent-internal, empirical instance of provenance tracing. |
| cottonbarratt2026aiforai | yes | AI for AI for Epistemics (Cotton-Barratt, Finnveden; 1 Apr 2026) | Argues AI R&D automation will speed up AI-for-epistemics tools. Names risks: "epistemic misalignment", "trust lock-in". Recommends auditable epistemic infrastructure. | Motivation for auditable, signed memory. |

### 1b. Background works

| key | verified? | exact title | what it shows | how we differ |
|---|---|---|---|---|
| chen2024agentpoison | yes | AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases | Backdoor triggers optimised to retrieve poisoned memory/KB entries. | Attack on retrieval. We study authorship and trust after retrieval. |
| dong2025minja | yes | Memory Injection Attacks on LLM Agents via Query-Only Interaction | MINJA: poisons memory through ordinary queries, with no direct write access. | Write-path attack. Our threat model assumes write access and asks whether the agent notices. |
| zou2024poisonedrag | yes | PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models | Injecting a few texts into a RAG corpus controls answers. | RAG, not first-person memory. |
| greshake2023indirect | yes | Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection | Introduces indirect prompt injection via retrieved data. | Foundational threat model. |
| binder2024lookinginward | yes | Looking Inward: Language Models Can Learn About Themselves by Introspection | Models predict their own behaviour better than other models trained on their behaviour. | Self-prediction, not self-authorship of stored text. |
| packer2023memgpt | yes | MemGPT: Towards LLMs as Operating Systems | Virtual context management in which the agent writes its own memory (basis of Letta). | System we model. |
| chhikara2025mem0 | yes | Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory | Memory extraction and consolidation architecture. | System we model. |
| park2023generative | yes | Generative Agents: Interactive Simulacra of Human Behavior | Memory stream, reflection and planning for agents. | Introduces self-written reflections as memory. |
| davidson2024selfrecognition | yes | Self-Recognition in Language Models | Model-generated "security questions" test self-recognition. Finds no consistent general self-recognition; models pick the "best" answer. | Supports the quality-confound worry. We add matched negatives. |
| laine2024sad | yes | Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs | Situational-awareness benchmark that includes self-knowledge and recognising own text. | General SA. Not memory. |
| longpre2021entity | yes | Entity-Based Knowledge Conflicts in Question Answering | Context-vs-parametric conflicts via entity substitution. | Background on knowledge conflict. |
| xie2023chameleon | yes | Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts | LLMs accept coherent conflicting evidence, yet also show confirmation bias toward their parametric memory. | Background. |
| wan2024evidence | yes | What Evidence Do Language Models Find Convincing? | ConflictingQA. Predictions are driven by relevance. Models largely **ignore stylistic/credibility features** such as scientific references or a neutral tone. | Studies document features, not explicit provenance labels. It is a weaker precedent for "labels change trust" than the planning doc assumed. |
| ackerman2024inspection | yes | Inspection and Control of Self-Generated-Text Recognition Ability in Llama3-8b-Instruct | Llama3-8b-Instruct (not base) recognises own vs human text. A residual-stream vector tracks self-authorship and can steer it. | Activation-level self-recognition precedent for our probes. Negatives are human text. |
| tan2024blinded | yes | Blinded by Generated Contexts: How Language Models Merge Generated and Retrieved Contexts When Knowledge Conflicts? | LLMs favour LLM-generated contexts over retrieved ones even when wrong. Driven by question similarity and segmentation. | Content-driven preference for generated text, not label-driven. A useful contrast to our byte-identical design. |

### 1c. Newer / closer work found (not in the planning doc)

| key | verified? | exact title | what it shows | how we differ |
|---|---|---|---|---|
| chen2026selfcorrectionillusion | yes (HTML) | The Self-Correction Illusion: Role Relabeling Gates Explicit Error Flagging in Large Language Models | A **byte-identical erroneous claim** is placed in the agent's `<thought>`, a user message, a tool response, or a system `<memory>` block. Moving it out of `<thought>` raises explicit correction by 23–93 pp (10/12 settings, 9 models). `<memory>` is often the *most* scrutinised role. | Closest to pillar 1. Their "self" is in-context thought, their outcome is error flagging during an audit, and their memory block is unattributed. We study cross-session notes *labelled as self-written*, measure adoption in downstream action, add web and other-agent channels, and run forgery and gating. |
| nikeghbal2026whoflips | yes (HTML) | Who Flips? Self- and Cross-Model Counterarguments Reveal Answer Instability in LLMs | On MMLU, telling a model that a counterargument was **its own from an earlier session** raises flip rate vs blind presentation in every model (mean +7.1 pp, up to +18.7 pp). | A two-arm (self vs blind) self-trust effect on MCQ argument persuasion. We run a multi-channel label ladder on agent memory claims with ground truth. |
| khullar2026selfattribution | yes | Self-Attribution Bias: When AI Monitors Go Easy on Themselves | Monitors rate actions as safer or more correct when the action sits in a prior assistant turn (implicitly their own) than when the same action appears in a user turn. **Explicitly stating that the action came from the monitor did not by itself induce the bias.** | This is a key caution for pillar 1: an explicit "you wrote this" label may not be what drives self-trust; role placement may. |
| rahman2026poem | yes | Proof-of-Execution Memory: Defending LLM Agents Against Forged-Reasoning Attacks by Verifying What Actually Happened | LLM rewording evades SENTINEL on the first try. Proposes an **HMAC-chained ledger** of executed safety steps, writable only by the action layer. A skip is allowed only if the ledger confirms execution. ASR drops to 0%. | Closest to pillar 4. It gates specific safety-step claims with a signed ledger. We compare signed tags vs a model-native re-derivation gate on general claims, including notes that are genuinely self-written but wrong. |
| louck2026tmanm | yes | Securing LLM-Agent Long-Term Memory Against Poisoning: Non-Malleable, Origin-Bound Authority with Machine-Checked Guarantees | Shows that content- and lineage-based defences are malleable: laundering through the agent's own summarisation, trusted-tool echo, or manufactured corroboration reaches up to 68% ASR. Proves write-time origin binding is necessary. TMA-NM reaches 0% ASR. | Formal and system-level. "Own summarisation" appears as a *laundering channel*, but they do not measure the model's self-trust premium or self-recognition. |
| saidi2026mutmem | yes | MutMem: Cryptographically Authorized Mutation in Persistent Agent Memory | Ed25519-signed memory mutations and signed poison labels. Explicitly "does not establish content truth". | Signing alone. Our point is that signing must be paired with re-derivation. |
| dabirsiaghi2026compaction | yes | Compaction Laundering: Provenance Destruction in Context-Compacting Coding Agents | Harnesses that flatten roles to text labels let a forged `[User]:` turn launder into compacted memory 87–100% of the time. Role-typed harnesses: 0%. A code-level provenance check catches 77%. | Shows that unsigned textual provenance is spoofable in real harnesses. Supports our unsigned-tag arm. |
| safin2026trustpropagation | yes | Trust propagation and structural containment in Multi-agent LLM pipelines | A forged approval through shared-memory poisoning compromises the validator 100% of the time, but **task-bound signed tokens** contain execution (0% unsafe actions). | Signed-authorisation precedent, in a multi-agent setting. |
| alpay2026autobiographical | yes | Provenance and Authorization in Autobiographical Language Models | Formal typed records and attestations. A small pilot (one frozen public model, 32 synthetic cases) compares flattened records, source labels and an admission gate. | A tiny pilot overlapping the shape of pillar 4. Not adversarial, and no forger ladder. |
| gu2026whosememory | yes | Whose Memory Is It? Scope-Aware Commit Rules for Long-Term LLM Memory | "Discourse ownership": hypotheticals and reported beliefs get committed as facts. CASK commit rule. | **Title collision risk** with ours. Different question (scope of propositions, not authorship). Consider renaming or citing it explicitly. |
| wang2026prefillawareness | yes | Prefill Awareness in Large Language Models | Frontier models detect tampered assistant-side context. Claude Opus 4.5 flags preference-opposing prefills in 9–35% of cases with 0% FPR. Stylistic mismatch drives flagging, while preference mismatch drives reversion. Also tested on SWE-bench trajectories. | Same-session assistant turns. We test cross-session memory notes against a graded forger ladder. |
| napa2026cotchanges | yes | Can Reasoning Models Detect Changes to their Chains of Thought? | Only modest detection of CoT edits. Models are **about as good on other models' CoTs as on their own**. | Strong prior that self-recognition gives little leverage. Our ladder tests this for memory. |
| nguyen2026prefillselfreport | yes | Can LLMs Reliably Self-Report Adversarial Prefills, and How? | 10 open models, 3B–70B: no model reliably recognises its own prefilled outputs (claims intent in 25.3% of prefilled cases). The signal runs through the refusal direction. | Safety prefills, verbal report. Our verbal-report detector arm should expect similar weakness. |
| asvin2026enaction | yes | From Simulation to Enaction: Post-trained language models recognize and react to their own generations | On-policy output entropy is 3–4× lower than off-policy. An internal "input surprise" signal causally modulates it. Verbal prefill recognition uses a different mechanism. | Precedent for surprisal and internal signals beating verbal report. Single context, not stored notes. |
| asvin2026privilegedpersona | yes | The Assistant as a Privileged Persona: A canonical reference in cross-persona self-recognition | Llama-3.1-70B. For the Assistant persona, authorship claim rate, persona-vector distance and an entropy/surprise gap are tightly coupled. This fails for other personas. | Surprisal-based authorship within one model. No forgers, no memory. |
| stamand2026sgtr | yes | Self-Generated Text Recognition: Quality Heuristics, Cross-Task Transfer, and Downstream Bias in LLM Evaluation | 13–21 models. Self-recognition varies with format (pairwise vs individual, **user vs assistant tags**) and domain. Quality heuristic is the dominant confound. SFT generalises. | Methodological must-cite for pillar 2: control for quality and role tags. |
| bai2025knowthyself | yes | Know Thyself? On the Incapability and Implications of AI Self-Recognition | 10 LLMs. Self-recognition is rarely above chance. Models are biased toward naming GPT and Claude. | Negative prior for pillar 2. |
| singh2026introspectrealitycheck | yes | Can LLMs Introspect? A Reality Check | Argues introspection claims need privileged access and second-order computation. Input-only classifiers match some "introspection" results. Tamper detection is not reliably distinguished from other manipulations. | Methodological caution for our verbal-report and probe arms. Include input-only baselines. |
| su2026trustswap | yes | Multi-Channel Mitigation of Source-Trust Shortcuts in Fact-Checking RL Agents | TrustSwap swaps or removes HIGH/LOW reliability labels with **evidence text fixed**. Label change alone flips 4–23% of confident verdicts (Qwen3), up to 50% for an RL fact-checker. | Same counterfactual-label method as ours, but reliability labels, not authorship or memory. |
| leong2026selfarbitration | yes | Instruction Self-Arbitration Is Not a Trust Boundary: Configuration-Dependent Tool Calls and External Enforcement in LLM Agents | In-context labels are not an enforceable boundary. **Source-format cues are linearly decodable (97.5–100% probe accuracy)**, but a crossed-probe test found no abstract provenance representation. | Direct precedent and caveat for our probe arm: probes may decode *format*, not *authorship*. |
| kwon2026reclaim | yes | Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One | A memory that keeps the conclusion but drops its "re-derivation basis" makes models re-emit stale values. A source-first policy restores correctability. | The re-derivation idea in a non-adversarial setting. Our gate uses the logged trace as the re-derivation basis. |
| kwon2026factwash | yes | FACTWASH: Catching AI Rewrites That Wash Hearsay into Fact | Deterministic write-time gate that flags dropped attribution, hedges or time. Optional LLM witness. | Write-time hygiene. Not an authorship check. |
| gadgil2026badmemory | yes | Bad Memory: Evaluating Prompt Injection Risks from Memory in Agentic Systems | Claude Code and Codex: hard to make agents overwrite their memory files, but payloads **already planted** in memory files attack current and future sessions. | Real-harness evidence for our threat model (write access to memory). |
| das2026selfpropagating | yes | Self-Propagating Misalignment in LLM Agents, and Why Auditing or Disabling Memory Is Not Enough | A misaligned agent writes goals into memory that later aligned sessions execute (58% / 18% of runs). A memory auditor only reduces this from 71% to 34%. | Shows that *genuinely self-authored* notes can be the hazard. Supports "re-derive content even if provenance is authentic". |
| dixit2026honestlying | yes | Honest Lying: Understanding Memory Confabulation in Reflexive Agents | Reflexion agents store confident but wrong self-diagnoses and keep acting on them. Programmatic extraction from the trajectory fixes much of it. | The same: authentic self-notes can be wrong, and trace-based re-derivation helps. |
| yang2026memorydojo | yes | MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory | 155 multi-session trajectories, 5 memory systems. All are susceptible. Memory-aware poison optimisation. | Poison lifecycle. No provenance or authorship measurement. |
| jiang2026permit | yes | PerMIT: Securing Persistent Memory for LLM Agents via Machine-Checked Integrity Theorems and Scalable Community Trust | Lean-verified gate: environment-derived memory reaches sensitive actions only if confirmed. | System gate. Not about model self-trust. |
| maloyan2026sleeper | yes | Sleeper Channels and Provenance Gates: Persistent Prompt Injection in Always-on Autonomous AI Agents | Persistent injection via memory, skills or cron. A provenance gate with owner attestations. Empirical evaluation is deferred. | Design only. |
| zhang2026memmark | yes | MemMark: State-Evolution Attribution Watermarking for Agent Long-Term Memory Systems | Keyed watermark in memory-write decisions for snapshot-only attribution. | Cryptographic authorship of a memory *store*. Not the model's own recognition. |

---

## 2. Corrections to the candidate list

1. **arXiv 2602.20031 is not a prefill-detection paper.** It is "Latent Introspection: Models Can Detect Prior Concept Injections" (Pearson-Vogel, Vanek, Douglas, Kulveit, 2026), about detecting *concept injections* via logit lens. For **prefill detection** cite: Lindsey 2601.01828 (it has a prefill section), **Prefill Awareness 2606.12747**, **Asvin & Lindsey 2605.25459**, and **Nguyen et al. 2606.23671**.
2. **arXiv 2606.06315 ("self-recognition in activations")** is mainly a *steering-based watermark* for multi-LLM attribution. Its "self-recognition" baseline is own-model vs **human** text, not own vs other-model or forged text. Do not cite it as showing that models recognise their own text against same-model forgeries. The classic activation-level self-recognition citation is **Ackerman & Panickssery 2410.02064**.
3. **"Manufactured Confidence" (2606.29279)**: the id and title are correct (sole author Alex Kwon). Note that its source-attribution manipulation is *within the memory text* (bare / "a user states" / forged "system of record"). Its key result is **source-invariance**: these all grant alike. That is the *opposite* of a provenance-label effect, so do not cite it as evidence that labels matter.
4. **Wan et al. 2024 (2402.11782)** found models largely *ignore* credibility and style features (references, neutral tone) and follow relevance. It is not evidence that provenance labels change trust. Better label-effect precedents: TrustSwap 2609.36611, Self-Correction Illusion 2606.05976, Who Flips? 2606.16011, Authority Bias 2609.37616.
5. **MINJA (2503.03704)**: the current arXiv title (v5) is "Memory Injection Attacks on LLM Agents via Query-Only Interaction". The earlier title "A Practical Memory Injection Attack against LLM Agents" refers to the same id. Use the current title.
6. **Lindsey (2025)**: the citable form is arXiv 2601.01828 (submitted 5 Jan 2026), "Emergent Introspective Awareness in Large Language Models", sole author Jack Lindsey. Year on arXiv is 2026. If you also want to cite the 2025 transformer-circuits.pub web version, I did not fetch it, so verify it before adding.
7. **ASB perplexity claim**: correct in direction, but see section 5. No single headline number is reported for PPL. The ≈0.66 FNR / ≈0.20 FPR figures in ASB Table 21 are for *LLM-based* detection, not PPL. Do not mix them up.
8. All other candidate ids (2607.05029, 2510.02373, 2410.02644, 2404.13076, 2601.01828, 2607.10526, 2606.10949, 2609.37616, 2404.10198, RFC 6962, both Forethought URLs) resolve to the described works. FARMA's acronym expands to "Forged Amplifying Rationale Memory Attack".
9. **Title collision:** "Whose Memory Is It? Scope-Aware Commit Rules for Long-Term LLM Memory" (2610.09008, Oct 2026) exists. Our title "Whose Memory Is This?" is very close. Either cite it in related work and make the difference clear, or tweak our title.

---

## 3. Closest work and exact delta

**Manufactured Confidence (Kwon, 2606.29279).** Setting: an access-control agent (plus a budget-approval replication) that reads a carried memory such as "Alice's clearance is admin" (true value: viewer). Five models: Claude Sonnet, Claude Haiku, GPT-4o-mini, Qwen-72B, Llama-70B. They vary (a) the *epistemic register* of the memory text (flat assertion vs "probably" / "rumor has it" / "reportedly" / "never verified") and (b) *attribution inside the text* (bare, "a user states…", forged "per the system of record", and in `forged.py` four forged authorities). Findings:
- Real consolidators (mem0, LangMem) de-hedge hearsay into flat facts.
- Agents grant on confidence, not source. Bare, attributed and forged-authority framings all grant at ≈0.81. Haiku is the one exception, at 0.47 for user attribution.
- A passive "unverified" tag leaks. An active "distrust" instruction over-escalates.
- Their contribution is "a diagnosis and its bound, not a defense". Their constructive lesson is that no single memory should be load-bearing and that a redundant source restores discrimination.

What they do **not** do:
- No condition where the claim is labelled as *the agent's own note*.
- No comparison across delivery channels (tool output, web snippet, user turn, other-agent message) with byte-identical content.
- No self-recognition or authorship detection, no forger ladder, no surprisal, probe or re-derivation detectors.
- No signed vs unsigned provenance comparison. They only show that a forged authority string is believed, which is the textual analogue of our unsigned-spoof arm.

Our delta: we hold the claim text and register fixed and vary the *author/channel label*, which isolates the self-trust premium from their confidence effect. Their source-invariance result is a prediction to engage with: if our premium comes out near zero, that replicates them; if it is positive, it shows that "own memory" is special compared with other attributions. Their register effect is also a confound we must control. Cite them as the closest neighbour for "memory write manufactures authority".

**The Self-Correction Illusion (Chen et al., 2606.05976).** A byte-identical erroneous claim is re-presented as the agent's `<thought>`, a user message, a calculator tool response, or a system `<memory>` block. The audit instruction is held fixed. 9 models; math, logical deduction and a third domain. Moving the claim out of `<thought>` raises *explicit error-flagging* by 23–93 pp. `<memory>` is often the most effective role, which they call "the strongest source-of-record framing". A nonsense tag trails `<memory>`, so the tag's lexical identity matters. This is methodologically the closest precedent to pillar 1 (byte-identical claim, role label varied, includes memory and tool).

What it does not cover:
- Its "self" condition is in-context chain-of-thought, not a persisted note attributed to the agent's past session.
- Its `<memory>` block is unattributed system memory, so it behaves as "external".
- Its outcome is error flagging under an explicit audit request, not adoption in a downstream decision.
- No web, other-agent or unattributed arms; no ground-truth multi-session environment; no forgery or gating.

Our delta: we separate "memory-as-system-record" from "memory-as-*my*-note". Their result predicts that an unattributed memory block may be scrutinised *more* than an in-context thought. Whether a first-person memory label recovers the thought-like blind spot is exactly our pillar-1 question.

**Who Flips? (Nikeghbal et al., 2606.16011)** and **Self-Attribution Bias (Khullar et al., 2603.04582).**
- *Who Flips?* (7 frontier models, MMLU): the same wrong-answer argument presented as "your own argument from an earlier session" raises flip rate over blind presentation for every model (mean +7.1 pp, max +18.7 pp). This is a measured **self-trust premium from a label alone**, though only two arms, on MCQ arguments, with no agent memory.
- *Khullar et al.*: monitors are more lenient toward actions in a prior assistant turn (implicitly their own) than toward the same action in a user turn. **Explicitly stating that the action came from the monitor did not by itself induce the bias.**

Together they mean the bare existence of a self-attribution effect is no longer novel, and whether explicit labels or role placement drive it is contested. Our delta: a multi-channel ladder (self-note vs tool vs web vs user vs other agent vs unattributed) in a multi-session agent with ground truth and downstream actions, plus implicit (role-placed) vs explicit (labelled) self-attribution as a factor. Add that factor if feasible; it directly addresses the Khullar result.

**FARMA (2607.05029) and Proof-of-Execution Memory (Rahman & Kim, 2608.16032).**
- *FARMA* forges reasoning-history entries. Its SENTINEL provenance/IFC layer trusts entries whose *declared* source is AGENT/SYSTEM, and FARMA simply spoofs `source=AGENT, trust=VERIFIED`. That is an empirical demonstration that **unsigned provenance tags are spoofable** in agent memory.
- *PoEM* shows SENTINEL's structural "Reasoning Guard" is evaded by LLM rewording on the first attempt. Its fix ignores memory content altogether: an **HMAC-chained, action-layer-only ledger** of executed safety steps, consulted before allowing a skip. Result: 0% ASR, near-0% FPR, while SENTINEL blocks 33–50% of legitimate operations. PoEM also observes a "capability paradox": stronger models follow forged claims more often (98–100% on GPT-4o/4o-mini vs 44% on Llama-3.1-8B).

Together they pre-empt the core of "unsigned tags are spoofable; signed ledgers work" for one claim type (safety steps were executed).

What remains ours:
1. A controlled head-to-head of unsigned tags vs HMAC-signed tags vs a **model-native re-derivation gate** on general factual and decision claims.
2. The case where provenance is **authentic but content is wrong**: the agent's own mistaken note (cf. Honest Lying 2605.29463, Self-Propagating Misalignment 2610.04083, Manufactured Confidence). Here signing *authenticates* the error and only re-derivation catches it.
3. The design rule combining both.

**Prefill/CoT tamper detection: Prefill Awareness (2606.12747), Napa et al. (2606.22085), Nguyen et al. (2606.23671), Lindsey (2601.01828), Asvin & Lindsey (2605.25459).** These ask whether a model can tell its own assistant-side context from inserted or edited content within one session.
- Prefill Awareness: frontier models sometimes detect preference-opposing prefills (Opus 4.5: 9–35%, 0% FPR). Stylistic mismatch drives flagging, while preference mismatch drives reversion.
- Napa et al.: detection of CoT edits is only modest, and models are about as good on other models' CoTs as on their own.
- Nguyen et al.: no open model reliably self-reports adversarial prefills.
- Asvin & Lindsey: on-policy recognition shows up in output entropy and an internal input-surprise signal, while verbal recognition uses a different mechanism.

None of these study **cross-session memory notes**, a **graded forger ladder** (template edit → other model → same-model restyle → adaptive best-of-N against the victim's self-rating → against its internals), or **matched negatives** (genuine same-model notes from *other* episodes, which remove the quality and style shortcut). Our pillar 2 is the memory-and-adversarial extension. Napa et al.'s "own ≈ other" and Prefill Awareness's "style drives flagging" predict that T2 (same-model restyle) and above defeat verbal self-recognition. Pre-register that.

**Self-recognition in activations (Ardoin et al., 2606.06315), Ackerman & Panickssery (2410.02064), Instruction Self-Arbitration (2608.28502).**
- *Ardoin et al.*: an LDA probe on mean activations separates own-model from human summaries at ≈99–100 AUROC. Perplexity matches this *only when conditioned on the original prompt* (≈97–99.7) and collapses without it (≈32–52). This is the closest precedent for our **trace-conditioned surprisal delta**, which applies the same logic with the logged trace as conditioning. Cite it, and frame our contribution as testing whether that conditioning advantage survives *same-model* forgers and adaptive T3/T4 attacks, where human-vs-LLM separability no longer helps.
- *Ackerman & Panickssery*: a self-authorship residual direction (own vs human).
- *Leong*: source-*format* cues are 97.5–100% linearly decodable, but the paper finds no abstract provenance representation. This is a warning that our probes may learn format; use format-matched negatives.

**Model-native re-derivation precedents: Reclaim Evaluation (2606.25449), Honest Lying (2605.29463), ASB's own "future defense" suggestion.**
- Kwon's *Reclaim* shows that keeping the "re-derivation basis" (source) instead of the conclusion restores correctability.
- *Honest Lying* fixes confabulated reflections by extracting failure signals from the trajectory.
- *ASB* suggests "contextual memory validation" against the broader task context as future work.

None evaluates **re-derivation from a logged trace as an integrity detector against forgers** or compares it with surprisal, probes and verbal report on the same items. That comparison is ours.

---

## 4. Pre-emption verdict per pillar

### Pillar 1: Self-trust premium by provenance label
**PARTIALLY pre-empted.**
- Who Flips? (2606.16011) measured a self-attribution premium (self vs blind, +7.1 pp mean) on MCQ counterarguments.
- Self-Correction Illusion (2606.05976) did byte-identical role relabelling across thought, user, tool and `<memory>` (outcome: error flagging).
- Khullar et al. (2603.04582) showed implicit self-attribution bias and found explicit labels insufficient.
- Manufactured Confidence (2606.29279) showed source-invariance across within-memory attributions.
- Authority Bias (2609.37616) and TrustSwap (2609.36611) cover label effects for verified-source and reliability labels.

Not pre-empted: a multi-channel ladder (own memory note / tool / web / user / other agent / unattributed) on byte-identical claims, in a multi-session agent with ground truth, measuring downstream adoption.

"To our knowledge, the first systematic measurement of …": **defensible only if narrowed.**
- Safe: "To our knowledge, the first controlled comparison of how agents weight a byte-identical claim when it is attributed to their *own past memory note* versus tool, web, user, peer-agent and unattributed sources, in a multi-session environment with ground truth."
- Avoid: "first to show models trust their own outputs more". Who Flips? and Khullar et al. pre-empt that.

Sharpen the delta:
1. Add an implicit-vs-explicit self-attribution factor (note in an assistant turn vs labelled "your note").
2. Control epistemic register (Kwon).
3. Report an unattributed `<memory>` arm so you can reconcile with the Self-Correction Illusion.

### Pillar 2: Self-recognition of own memory under a forger ladder with matched negatives
**NOT PRE-EMPTED (closely surrounded).** Relevant work:
- Self-recognition: Panickssery 2404.13076, Davidson 2407.06946, Ackerman 2410.02064, Know Thyself 2510.03399, SGTR 2608.26159.
- Tamper and prefill detection: Lindsey 2601.01828, Prefill Awareness 2606.12747, Napa 2606.22085, Nguyen 2606.23671.

None uses persisted agent memory, a graded adaptive forger ladder (T0–T4), or matched negatives of genuine same-model notes from other episodes. Napa et al.'s own-vs-other CoT comparison is the nearest. It covers one rung (another model) and a single session.
- Wording: "To our knowledge, the first evaluation of whether LLM agents can recognise their own memory notes against an adaptive forger ladder with matched same-model negatives" is **defensible**.
- Do not claim "first study of self-recognition" or "first study of tamper detection".

### Pillar 3: Where the integrity signal lives (verbal / re-derivation / consistency query / surprisal incl. trace-conditioned delta / probes)
**PARTIALLY pre-empted, on components only.**
- Verbal vs internal dissociation: Pearson-Vogel 2602.20031, Asvin & Lindsey 2605.25459, Nguyen 2606.23671.
- Probes vs perplexity, with prompt conditioning rescuing perplexity: Ardoin 2606.06315, own vs human text.
- Format probes: Leong 2608.28502.
- Unconditioned PPL is weak for memory poisoning: ASB.

No paper compares all five signal families on the same memory-forgery items, and none uses the trace-conditioned surprisal delta against same-model or adaptive forgers.
- Wording: "To our knowledge, the first head-to-head comparison of verbal self-report, trace re-derivation, consistency queries, own-model surprisal and activation probes as detectors of forged agent memory" is **defensible**.
- Do not claim novelty for "conditioning perplexity on the generating context". Credit Ardoin et al. (prompt-conditioned PPL) and Asvin (surprise signals).
- Add input-only and format-matched baselines (Singh et al. 2605.26242; Leong).

### Pillar 4: Provenance gate, signed vs unsigned, vs re-derivation gate
**PARTIALLY pre-empted.**
- Unsigned provenance spoofing: FARMA 2607.05029 (source=AGENT spoof defeats its provenance layer) and Compaction Laundering 2610.29869.
- Signed or authenticated provenance works: PoEM 2608.16032 (HMAC-chained ledger, 0% ASR), Trust propagation 2609.17648 (signed task tokens), TMA-NM 2606.24322 (origin-bound authority, proofs), MutMem 2608.02843 (Ed25519).
- Alpay & Alpay 2610.17935 piloted labels vs an admission gate on one model.

Not pre-empted:
- A controlled comparison of a *model-native re-derivation gate* against signed and unsigned tags on the same attack set.
- The authentic-but-wrong self-note case. Supporting evidence that this case matters: Das 2610.04083; Dixit 2605.29463; Kwon 2606.29279. Signing cannot catch it.
- The combined rule "sign provenance and re-derive content".
- Wording: do **not** claim "first to propose signed agent memory" or "first to show that unsigned tags are spoofable". Safe: "We compare … and show that signing and re-derivation fail on complementary cases: signing stops forged attribution but authenticates the agent's own errors, while re-derivation catches wrong content but is cheaper to evade when [result]."
- Position against PoEM explicitly: PoEM gates one claim type (executed safety steps) against an action-layer ledger; ours re-derives arbitrary note content from the logged trace.

### General wording advice
Prefer "to our knowledge, the first … that combines X, Y, Z" over "the first measurement of the self-trust premium". The field moved fast between Jun and Nov 2026: at least 6 directly relevant papers since June. A reviewer at this sprint may know Who Flips?, the Self-Correction Illusion, PoEM and Manufactured Confidence.

---

## 5. ASB perplexity-filter claim: what was reported

From ASB (2410.02644 v4, HTML), Sec. A.4.3 and the "Ineffectiveness of PPL detection Against Memory Attacks" paragraph with Fig. 4:
- PPL detection is applied to **plans retrieved from the memory database**, as a defence against the memory-poisoning attack. A plan is flagged as compromised when perplexity exceeds a threshold.
- They sweep thresholds **from 2.4 to 4.8** and plot FNR vs FPR curves per backbone (Fig. 4). They report that "regardless of the chosen threshold, FNR and FPR remain relatively high". Low thresholds give excessive false positives; high thresholds miss too many attacks.
- Their explanation is that malicious memory plans can be *simpler* (one step, e.g. directly calling a tool) than benign multi-step plans, so they are not higher-perplexity.
- **No single headline PPL number is reported in text or tables.** The results exist only as curves in Fig. 4.
- The numbers that sit next to Fig. 4 in the HTML are from **Table 21, LLM-based detection** for memory attacks: average **FNR 0.660, FPR 0.200** across 13 backbones (per-model FNR 0.654–0.671, FPR 0.193–0.204). ASB calls these defences "largely ineffective". Do not attribute these numbers to PPL.
- ASB's suggested future defence is "contextual memory validation", which analyses the plan against the full task context. That is close in spirit to our re-derivation gate; cite it as motivation.
- Safe sentence: "In ASB, a perplexity filter over retrieved memory plans could not reach both low FNR and low FPR at any threshold in 2.4–4.8 (their Fig. 4), and an LLM-based detector missed 66% of poisoned plans at a 20% FPR (their Table 21)."
- Our surprisal detector differs in two ways: it uses the *victim model's own* surprisal, and its delta is *conditioned on the logged trace*.

---

## 6. Could not verify / caveats
- The transformer-circuits.pub web version of Lindsey (2025): I did not fetch it. Only the arXiv form is verified.
- I read abstracts and HTML for the closest papers but not every table. Numbers quoted in section 3 come from the abstract or the HTML sections I read: Manufactured Confidence Table 1, Who Flips Table 3, Self-Correction Illusion Table 1/2, Ardoin Table 1, ASB Fig. 4 / Table 21.
- Search was arXiv-only (see top). Papers posted to arXiv after the morning of 13 Nov 2026 are not covered.
- Several close 2026 papers are single-author or small pilots: Alpay & Alpay, Maloyan & Namiot (empirics deferred), MutMem. Cite them as related, not as strong evidence.
