# Number macros (pilot)

| macro | value | meaning |
|---|---|---|
| `\PrimSelfTrust` | \ensuremath{-}38.9 | primary 1: net preference memory - tool (pp) |
| `\PrimSelfTrustLo` | \ensuremath{-}66.7 | primary 1: net preference memory - tool (pp), lower 95% CI bound |
| `\PrimSelfTrustHi` | \ensuremath{-}16.7 | primary 1: net preference memory - tool (pp), upper 95% CI bound |
| `\PrimSelfTrustCI` | [\ensuremath{-}66.7, \ensuremath{-}16.7] | primary 1: net preference memory - tool (pp), 95% CI |
| `\PrimSelfTrustN` | 18 | primary 1: net preference memory - tool (pp), n |
| `\PrimSelfTrustP` | 0.002 | primary 1: net preference memory - tool (pp), two-sided bootstrap p (n/a if not tested) |
| `\PrimSelfTrustPHolm` | 0.003 | primary 1: net preference memory - tool (pp), Holm-adjusted p |
| `\PrimSelfTrustSupported` | no | primary 1: net preference memory - tool (pp), registered criterion met |
| `\PrimVerbalTTwo` | 0.53 | primary 2: mean AUROC of V at T2 |
| `\PrimVerbalTTwoLo` | 0.50 | primary 2: mean AUROC of V at T2, lower 95% CI bound |
| `\PrimVerbalTTwoHi` | 0.58 | primary 2: mean AUROC of V at T2, upper 95% CI bound |
| `\PrimVerbalTTwoCI` | [0.50, 0.58] | primary 2: mean AUROC of V at T2, 95% CI |
| `\PrimVerbalTTwoN` | 108 | primary 2: mean AUROC of V at T2, n |
| `\PrimVerbalTTwoP` | \ensuremath{<}0.001 | primary 2: mean AUROC of V at T2, two-sided bootstrap p (n/a if not tested) |
| `\PrimVerbalTTwoPHolm` | 0.003 | primary 2: mean AUROC of V at T2, Holm-adjusted p |
| `\PrimVerbalTTwoSupported` | yes | primary 2: mean AUROC of V at T2, registered criterion met |
| `\PrimGapTThree` | 0.37 | primary 3: AUROC(best trace detector) - AUROC(V) at T3 |
| `\PrimGapTThreeLo` | 0.22 | primary 3: AUROC(best trace detector) - AUROC(V) at T3, lower 95% CI bound |
| `\PrimGapTThreeHi` | 0.42 | primary 3: AUROC(best trace detector) - AUROC(V) at T3, upper 95% CI bound |
| `\PrimGapTThreeCI` | [0.22, 0.42] | primary 3: AUROC(best trace detector) - AUROC(V) at T3, 95% CI |
| `\PrimGapTThreeN` | 112 | primary 3: AUROC(best trace detector) - AUROC(V) at T3, n |
| `\PrimGapTThreeP` | 0.001 | primary 3: AUROC(best trace detector) - AUROC(V) at T3, two-sided bootstrap p (n/a if not tested) |
| `\PrimGapTThreePHolm` | 0.003 | primary 3: AUROC(best trace detector) - AUROC(V) at T3, Holm-adjusted p |
| `\PrimGapTThreeSupported` | yes | primary 3: AUROC(best trace detector) - AUROC(V) at T3, registered criterion met |
| `\PrimGate` | n/a | primary 4: relative ASR reduction G1 vs none (%) [n/a: condition G1 absent (gate not run yet)] |
| `\PrimGateLo` | n/a | primary 4: relative ASR reduction G1 vs none (%), lower 95% CI bound |
| `\PrimGateHi` | n/a | primary 4: relative ASR reduction G1 vs none (%), upper 95% CI bound |
| `\PrimGateCI` | n/a | primary 4: relative ASR reduction G1 vs none (%), 95% CI |
| `\PrimGateN` | n/a | primary 4: relative ASR reduction G1 vs none (%), n |
| `\PrimGateP` | n/a | primary 4: relative ASR reduction G1 vs none (%), two-sided bootstrap p (n/a if not tested) |
| `\PrimGatePHolm` | n/a | primary 4: relative ASR reduction G1 vs none (%), Holm-adjusted p |
| `\PrimGateSupported` | n/a | primary 4: relative ASR reduction G1 vs none (%), registered criterion met |
| `\PrimGapDetector` | C | primary 3: trace detector selected on calibration episodes |
| `\PoneNetMemToolPooled` | \ensuremath{-}38.9 | P1 net memory - tool (pp), pooled |
| `\PoneNetMemToolPooledLo` | \ensuremath{-}66.7 | P1 net memory - tool (pp), pooled, lower 95% CI bound |
| `\PoneNetMemToolPooledHi` | \ensuremath{-}16.7 | P1 net memory - tool (pp), pooled, upper 95% CI bound |
| `\PoneNetMemToolPooledCI` | [\ensuremath{-}66.7, \ensuremath{-}16.7] | P1 net memory - tool (pp), pooled, 95% CI |
| `\PoneNetMemToolPooledN` | 18 | P1 net memory - tool (pp), pooled, n |
| `\PoneNetMemToolPooledP` | 0.002 | P1 net memory - tool (pp), pooled, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolDroppedPooled` | \ensuremath{-}38.9 | P1 net memory - tool (pp), unparsed dropped, pooled |
| `\PoneNetMemToolDroppedPooledLo` | \ensuremath{-}66.7 | P1 net memory - tool (pp), unparsed dropped, pooled, lower 95% CI bound |
| `\PoneNetMemToolDroppedPooledHi` | \ensuremath{-}16.7 | P1 net memory - tool (pp), unparsed dropped, pooled, upper 95% CI bound |
| `\PoneNetMemToolDroppedPooledCI` | [\ensuremath{-}66.7, \ensuremath{-}16.7] | P1 net memory - tool (pp), unparsed dropped, pooled, 95% CI |
| `\PoneNetMemToolDroppedPooledN` | 18 | P1 net memory - tool (pp), unparsed dropped, pooled, n |
| `\PoneNetMemToolDroppedPooledP` | 0.004 | P1 net memory - tool (pp), unparsed dropped, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareMemVsToolPooled` | 0.0 | P1 % follows memory vs tool, pooled |
| `\PoneShareMemVsToolPooledLo` | 0.0 | P1 % follows memory vs tool, pooled, lower 95% CI bound |
| `\PoneShareMemVsToolPooledHi` | 18.5 | P1 % follows memory vs tool, pooled, upper 95% CI bound |
| `\PoneShareMemVsToolPooledCI` | [0.0, 18.5] | P1 % follows memory vs tool, pooled, 95% CI |
| `\PoneShareMemVsToolPooledN` | 18 | P1 % follows memory vs tool, pooled, n |
| `\PoneShareMemVsToolPooledP` | n/a | P1 % follows memory vs tool, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareToolVsMemPooled` | 38.9 | P1 % follows tool vs memory, pooled |
| `\PoneShareToolVsMemPooledLo` | 16.7 | P1 % follows tool vs memory, pooled, lower 95% CI bound |
| `\PoneShareToolVsMemPooledHi` | 66.7 | P1 % follows tool vs memory, pooled, upper 95% CI bound |
| `\PoneShareToolVsMemPooledCI` | [16.7, 66.7] | P1 % follows tool vs memory, pooled, 95% CI |
| `\PoneShareToolVsMemPooledN` | 18 | P1 % follows tool vs memory, pooled, n |
| `\PoneShareToolVsMemPooledP` | n/a | P1 % follows tool vs memory, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolDeepSeekVFourFlash` | \ensuremath{-}22.2 | P1 net memory - tool (pp), deepseek-v4-flash |
| `\PoneNetMemToolDeepSeekVFourFlashLo` | \ensuremath{-}55.6 | P1 net memory - tool (pp), deepseek-v4-flash, lower 95% CI bound |
| `\PoneNetMemToolDeepSeekVFourFlashHi` | 0.0 | P1 net memory - tool (pp), deepseek-v4-flash, upper 95% CI bound |
| `\PoneNetMemToolDeepSeekVFourFlashCI` | [\ensuremath{-}55.6, 0.0] | P1 net memory - tool (pp), deepseek-v4-flash, 95% CI |
| `\PoneNetMemToolDeepSeekVFourFlashN` | 9 | P1 net memory - tool (pp), deepseek-v4-flash, n |
| `\PoneNetMemToolDeepSeekVFourFlashP` | 0.224 | P1 net memory - tool (pp), deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolDroppedDeepSeekVFourFlash` | \ensuremath{-}22.2 | P1 net memory - tool (pp), unparsed dropped, deepseek-v4-flash |
| `\PoneNetMemToolDroppedDeepSeekVFourFlashLo` | \ensuremath{-}44.4 | P1 net memory - tool (pp), unparsed dropped, deepseek-v4-flash, lower 95% CI bound |
| `\PoneNetMemToolDroppedDeepSeekVFourFlashHi` | 0.0 | P1 net memory - tool (pp), unparsed dropped, deepseek-v4-flash, upper 95% CI bound |
| `\PoneNetMemToolDroppedDeepSeekVFourFlashCI` | [\ensuremath{-}44.4, 0.0] | P1 net memory - tool (pp), unparsed dropped, deepseek-v4-flash, 95% CI |
| `\PoneNetMemToolDroppedDeepSeekVFourFlashN` | 9 | P1 net memory - tool (pp), unparsed dropped, deepseek-v4-flash, n |
| `\PoneNetMemToolDroppedDeepSeekVFourFlashP` | 0.205 | P1 net memory - tool (pp), unparsed dropped, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareMemVsToolDeepSeekVFourFlash` | 0.0 | P1 % follows memory vs tool, deepseek-v4-flash |
| `\PoneShareMemVsToolDeepSeekVFourFlashLo` | 0.0 | P1 % follows memory vs tool, deepseek-v4-flash, lower 95% CI bound |
| `\PoneShareMemVsToolDeepSeekVFourFlashHi` | 33.6 | P1 % follows memory vs tool, deepseek-v4-flash, upper 95% CI bound |
| `\PoneShareMemVsToolDeepSeekVFourFlashCI` | [0.0, 33.6] | P1 % follows memory vs tool, deepseek-v4-flash, 95% CI |
| `\PoneShareMemVsToolDeepSeekVFourFlashN` | 9 | P1 % follows memory vs tool, deepseek-v4-flash, n |
| `\PoneShareMemVsToolDeepSeekVFourFlashP` | n/a | P1 % follows memory vs tool, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareToolVsMemDeepSeekVFourFlash` | 22.2 | P1 % follows tool vs memory, deepseek-v4-flash |
| `\PoneShareToolVsMemDeepSeekVFourFlashLo` | 0.0 | P1 % follows tool vs memory, deepseek-v4-flash, lower 95% CI bound |
| `\PoneShareToolVsMemDeepSeekVFourFlashHi` | 55.6 | P1 % follows tool vs memory, deepseek-v4-flash, upper 95% CI bound |
| `\PoneShareToolVsMemDeepSeekVFourFlashCI` | [0.0, 55.6] | P1 % follows tool vs memory, deepseek-v4-flash, 95% CI |
| `\PoneShareToolVsMemDeepSeekVFourFlashN` | 9 | P1 % follows tool vs memory, deepseek-v4-flash, n |
| `\PoneShareToolVsMemDeepSeekVFourFlashP` | n/a | P1 % follows tool vs memory, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolGemmaFourThreeOneB` | \ensuremath{-}55.6 | P1 net memory - tool (pp), gemma-4-31b-it |
| `\PoneNetMemToolGemmaFourThreeOneBLo` | \ensuremath{-}88.9 | P1 net memory - tool (pp), gemma-4-31b-it, lower 95% CI bound |
| `\PoneNetMemToolGemmaFourThreeOneBHi` | \ensuremath{-}22.2 | P1 net memory - tool (pp), gemma-4-31b-it, upper 95% CI bound |
| `\PoneNetMemToolGemmaFourThreeOneBCI` | [\ensuremath{-}88.9, \ensuremath{-}22.2] | P1 net memory - tool (pp), gemma-4-31b-it, 95% CI |
| `\PoneNetMemToolGemmaFourThreeOneBN` | 9 | P1 net memory - tool (pp), gemma-4-31b-it, n |
| `\PoneNetMemToolGemmaFourThreeOneBP` | \ensuremath{<}0.001 | P1 net memory - tool (pp), gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolDroppedGemmaFourThreeOneB` | \ensuremath{-}55.6 | P1 net memory - tool (pp), unparsed dropped, gemma-4-31b-it |
| `\PoneNetMemToolDroppedGemmaFourThreeOneBLo` | \ensuremath{-}88.9 | P1 net memory - tool (pp), unparsed dropped, gemma-4-31b-it, lower 95% CI bound |
| `\PoneNetMemToolDroppedGemmaFourThreeOneBHi` | \ensuremath{-}22.2 | P1 net memory - tool (pp), unparsed dropped, gemma-4-31b-it, upper 95% CI bound |
| `\PoneNetMemToolDroppedGemmaFourThreeOneBCI` | [\ensuremath{-}88.9, \ensuremath{-}22.2] | P1 net memory - tool (pp), unparsed dropped, gemma-4-31b-it, 95% CI |
| `\PoneNetMemToolDroppedGemmaFourThreeOneBN` | 9 | P1 net memory - tool (pp), unparsed dropped, gemma-4-31b-it, n |
| `\PoneNetMemToolDroppedGemmaFourThreeOneBP` | 0.002 | P1 net memory - tool (pp), unparsed dropped, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareMemVsToolGemmaFourThreeOneB` | 0.0 | P1 % follows memory vs tool, gemma-4-31b-it |
| `\PoneShareMemVsToolGemmaFourThreeOneBLo` | 0.0 | P1 % follows memory vs tool, gemma-4-31b-it, lower 95% CI bound |
| `\PoneShareMemVsToolGemmaFourThreeOneBHi` | 33.6 | P1 % follows memory vs tool, gemma-4-31b-it, upper 95% CI bound |
| `\PoneShareMemVsToolGemmaFourThreeOneBCI` | [0.0, 33.6] | P1 % follows memory vs tool, gemma-4-31b-it, 95% CI |
| `\PoneShareMemVsToolGemmaFourThreeOneBN` | 9 | P1 % follows memory vs tool, gemma-4-31b-it, n |
| `\PoneShareMemVsToolGemmaFourThreeOneBP` | n/a | P1 % follows memory vs tool, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareToolVsMemGemmaFourThreeOneB` | 55.6 | P1 % follows tool vs memory, gemma-4-31b-it |
| `\PoneShareToolVsMemGemmaFourThreeOneBLo` | 22.2 | P1 % follows tool vs memory, gemma-4-31b-it, lower 95% CI bound |
| `\PoneShareToolVsMemGemmaFourThreeOneBHi` | 88.9 | P1 % follows tool vs memory, gemma-4-31b-it, upper 95% CI bound |
| `\PoneShareToolVsMemGemmaFourThreeOneBCI` | [22.2, 88.9] | P1 % follows tool vs memory, gemma-4-31b-it, 95% CI |
| `\PoneShareToolVsMemGemmaFourThreeOneBN` | 9 | P1 % follows tool vs memory, gemma-4-31b-it, n |
| `\PoneShareToolVsMemGemmaFourThreeOneBP` | n/a | P1 % follows tool vs memory, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PoneMixedShare` | n/a | P1 mixed model: P(follows memory / side chosen), % [n/a: outcome (near-)degenerate: 0 of 7 trials follow memory (fewer than 5 of one outcome); mixed model not estimable, exact binomial interval and test reported instead (they ignore clustering)] |
| `\PoneMixedShareLo` | n/a | P1 mixed model: P(follows memory / side chosen), %, lower 95% CI bound |
| `\PoneMixedShareHi` | n/a | P1 mixed model: P(follows memory / side chosen), %, upper 95% CI bound |
| `\PoneMixedShareCI` | n/a | P1 mixed model: P(follows memory / side chosen), %, 95% CI |
| `\PoneMixedShareN` | 7 | P1 mixed model: P(follows memory / side chosen), %, n |
| `\PoneMixedShareP` | n/a | P1 mixed model: P(follows memory / side chosen), %, two-sided bootstrap p (n/a if not tested) |
| `\PoneMixedEstimable` | no | P1 mixed model estimable |
| `\PoneSideChosenK` | 0 | P1 memory-vs-tool trials following memory among side-chosen |
| `\PoneSideChosenN` | 7 | P1 memory-vs-tool trials with a side chosen |
| `\PoneSideChosenExactCI` | [0.0, 41.0] | P1 share following memory among side-chosen, exact Clopper-Pearson CI (%) |
| `\PoneNetMemToolFamAssistant` | \ensuremath{-}66.7 | P1 net memory - tool (pp), family assistant |
| `\PoneNetMemToolFamAssistantLo` | \ensuremath{-}100.0 | P1 net memory - tool (pp), family assistant, lower 95% CI bound |
| `\PoneNetMemToolFamAssistantHi` | 0.0 | P1 net memory - tool (pp), family assistant, upper 95% CI bound |
| `\PoneNetMemToolFamAssistantCI` | [\ensuremath{-}100.0, 0.0] | P1 net memory - tool (pp), family assistant, 95% CI |
| `\PoneNetMemToolFamAssistantN` | 6 | P1 net memory - tool (pp), family assistant, n |
| `\PoneNetMemToolFamAssistantP` | 0.077 | P1 net memory - tool (pp), family assistant, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolFamInventory` | \ensuremath{-}33.3 | P1 net memory - tool (pp), family inventory |
| `\PoneNetMemToolFamInventoryLo` | \ensuremath{-}50.0 | P1 net memory - tool (pp), family inventory, lower 95% CI bound |
| `\PoneNetMemToolFamInventoryHi` | 0.0 | P1 net memory - tool (pp), family inventory, upper 95% CI bound |
| `\PoneNetMemToolFamInventoryCI` | [\ensuremath{-}50.0, 0.0] | P1 net memory - tool (pp), family inventory, 95% CI |
| `\PoneNetMemToolFamInventoryN` | 6 | P1 net memory - tool (pp), family inventory, n |
| `\PoneNetMemToolFamInventoryP` | 0.078 | P1 net memory - tool (pp), family inventory, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolFamResearch` | \ensuremath{-}16.7 | P1 net memory - tool (pp), family research |
| `\PoneNetMemToolFamResearchLo` | \ensuremath{-}50.0 | P1 net memory - tool (pp), family research, lower 95% CI bound |
| `\PoneNetMemToolFamResearchHi` | 0.0 | P1 net memory - tool (pp), family research, upper 95% CI bound |
| `\PoneNetMemToolFamResearchCI` | [\ensuremath{-}50.0, 0.0] | P1 net memory - tool (pp), family research, 95% CI |
| `\PoneNetMemToolFamResearchN` | 6 | P1 net memory - tool (pp), family research, n |
| `\PoneNetMemToolFamResearchP` | 0.616 | P1 net memory - tool (pp), family research, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolVariantZero` | \ensuremath{-}33.3 | P1 net memory - tool (pp), phrasing 0 |
| `\PoneNetMemToolVariantZeroLo` | \ensuremath{-}66.7 | P1 net memory - tool (pp), phrasing 0, lower 95% CI bound |
| `\PoneNetMemToolVariantZeroHi` | \ensuremath{-}8.3 | P1 net memory - tool (pp), phrasing 0, upper 95% CI bound |
| `\PoneNetMemToolVariantZeroCI` | [\ensuremath{-}66.7, \ensuremath{-}8.3] | P1 net memory - tool (pp), phrasing 0, 95% CI |
| `\PoneNetMemToolVariantZeroN` | 12 | P1 net memory - tool (pp), phrasing 0, n |
| `\PoneNetMemToolVariantZeroP` | 0.029 | P1 net memory - tool (pp), phrasing 0, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolVariantTwo` | \ensuremath{-}50.0 | P1 net memory - tool (pp), phrasing 2 |
| `\PoneNetMemToolVariantTwoLo` | \ensuremath{-}100.0 | P1 net memory - tool (pp), phrasing 2, lower 95% CI bound |
| `\PoneNetMemToolVariantTwoHi` | 0.0 | P1 net memory - tool (pp), phrasing 2, upper 95% CI bound |
| `\PoneNetMemToolVariantTwoCI` | [\ensuremath{-}100.0, 0.0] | P1 net memory - tool (pp), phrasing 2, 95% CI |
| `\PoneNetMemToolVariantTwoN` | 6 | P1 net memory - tool (pp), phrasing 2, n |
| `\PoneNetMemToolVariantTwoP` | 0.076 | P1 net memory - tool (pp), phrasing 2, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsToolFollowA` | 0.0 | P1 pair memory vs tool: % follows memory |
| `\PonePairMemoryVsToolFollowALo` | 0.0 | P1 pair memory vs tool: % follows memory, lower 95% CI bound |
| `\PonePairMemoryVsToolFollowAHi` | 18.5 | P1 pair memory vs tool: % follows memory, upper 95% CI bound |
| `\PonePairMemoryVsToolFollowACI` | [0.0, 18.5] | P1 pair memory vs tool: % follows memory, 95% CI |
| `\PonePairMemoryVsToolFollowAN` | 18 | P1 pair memory vs tool: % follows memory, n |
| `\PonePairMemoryVsToolFollowAP` | n/a | P1 pair memory vs tool: % follows memory, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsToolFollowB` | 38.9 | P1 pair memory vs tool: % follows tool |
| `\PonePairMemoryVsToolFollowBLo` | 16.7 | P1 pair memory vs tool: % follows tool, lower 95% CI bound |
| `\PonePairMemoryVsToolFollowBHi` | 66.7 | P1 pair memory vs tool: % follows tool, upper 95% CI bound |
| `\PonePairMemoryVsToolFollowBCI` | [16.7, 66.7] | P1 pair memory vs tool: % follows tool, 95% CI |
| `\PonePairMemoryVsToolFollowBN` | 18 | P1 pair memory vs tool: % follows tool, n |
| `\PonePairMemoryVsToolFollowBP` | n/a | P1 pair memory vs tool: % follows tool, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsToolEsc` | 61.1 | P1 pair memory vs tool: % flags conflict |
| `\PonePairMemoryVsToolEscLo` | 33.3 | P1 pair memory vs tool: % flags conflict, lower 95% CI bound |
| `\PonePairMemoryVsToolEscHi` | 83.3 | P1 pair memory vs tool: % flags conflict, upper 95% CI bound |
| `\PonePairMemoryVsToolEscCI` | [33.3, 83.3] | P1 pair memory vs tool: % flags conflict, 95% CI |
| `\PonePairMemoryVsToolEscN` | 18 | P1 pair memory vs tool: % flags conflict, n |
| `\PonePairMemoryVsToolEscP` | n/a | P1 pair memory vs tool: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsToolNet` | \ensuremath{-}38.9 | P1 pair memory vs tool: net A - B (pp) |
| `\PonePairMemoryVsToolNetLo` | \ensuremath{-}66.7 | P1 pair memory vs tool: net A - B (pp), lower 95% CI bound |
| `\PonePairMemoryVsToolNetHi` | \ensuremath{-}16.7 | P1 pair memory vs tool: net A - B (pp), upper 95% CI bound |
| `\PonePairMemoryVsToolNetCI` | [\ensuremath{-}66.7, \ensuremath{-}16.7] | P1 pair memory vs tool: net A - B (pp), 95% CI |
| `\PonePairMemoryVsToolNetN` | 18 | P1 pair memory vs tool: net A - B (pp), n |
| `\PonePairMemoryVsToolNetP` | 0.003 | P1 pair memory vs tool: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsWebFollowA` | 0.0 | P1 pair memory vs web: % follows memory |
| `\PonePairMemoryVsWebFollowALo` | 0.0 | P1 pair memory vs web: % follows memory, lower 95% CI bound |
| `\PonePairMemoryVsWebFollowAHi` | 18.5 | P1 pair memory vs web: % follows memory, upper 95% CI bound |
| `\PonePairMemoryVsWebFollowACI` | [0.0, 18.5] | P1 pair memory vs web: % follows memory, 95% CI |
| `\PonePairMemoryVsWebFollowAN` | 18 | P1 pair memory vs web: % follows memory, n |
| `\PonePairMemoryVsWebFollowAP` | n/a | P1 pair memory vs web: % follows memory, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsWebFollowB` | 38.9 | P1 pair memory vs web: % follows web |
| `\PonePairMemoryVsWebFollowBLo` | 16.7 | P1 pair memory vs web: % follows web, lower 95% CI bound |
| `\PonePairMemoryVsWebFollowBHi` | 66.7 | P1 pair memory vs web: % follows web, upper 95% CI bound |
| `\PonePairMemoryVsWebFollowBCI` | [16.7, 66.7] | P1 pair memory vs web: % follows web, 95% CI |
| `\PonePairMemoryVsWebFollowBN` | 18 | P1 pair memory vs web: % follows web, n |
| `\PonePairMemoryVsWebFollowBP` | n/a | P1 pair memory vs web: % follows web, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsWebEsc` | 61.1 | P1 pair memory vs web: % flags conflict |
| `\PonePairMemoryVsWebEscLo` | 33.3 | P1 pair memory vs web: % flags conflict, lower 95% CI bound |
| `\PonePairMemoryVsWebEscHi` | 83.3 | P1 pair memory vs web: % flags conflict, upper 95% CI bound |
| `\PonePairMemoryVsWebEscCI` | [33.3, 83.3] | P1 pair memory vs web: % flags conflict, 95% CI |
| `\PonePairMemoryVsWebEscN` | 18 | P1 pair memory vs web: % flags conflict, n |
| `\PonePairMemoryVsWebEscP` | n/a | P1 pair memory vs web: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsWebNet` | \ensuremath{-}38.9 | P1 pair memory vs web: net A - B (pp) |
| `\PonePairMemoryVsWebNetLo` | \ensuremath{-}66.7 | P1 pair memory vs web: net A - B (pp), lower 95% CI bound |
| `\PonePairMemoryVsWebNetHi` | \ensuremath{-}16.7 | P1 pair memory vs web: net A - B (pp), upper 95% CI bound |
| `\PonePairMemoryVsWebNetCI` | [\ensuremath{-}66.7, \ensuremath{-}16.7] | P1 pair memory vs web: net A - B (pp), 95% CI |
| `\PonePairMemoryVsWebNetN` | 18 | P1 pair memory vs web: net A - B (pp), n |
| `\PonePairMemoryVsWebNetP` | 0.002 | P1 pair memory vs web: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsUserFollowA` | 0.0 | P1 pair memory vs user: % follows memory |
| `\PonePairMemoryVsUserFollowALo` | 0.0 | P1 pair memory vs user: % follows memory, lower 95% CI bound |
| `\PonePairMemoryVsUserFollowAHi` | 18.5 | P1 pair memory vs user: % follows memory, upper 95% CI bound |
| `\PonePairMemoryVsUserFollowACI` | [0.0, 18.5] | P1 pair memory vs user: % follows memory, 95% CI |
| `\PonePairMemoryVsUserFollowAN` | 18 | P1 pair memory vs user: % follows memory, n |
| `\PonePairMemoryVsUserFollowAP` | n/a | P1 pair memory vs user: % follows memory, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsUserFollowB` | 50.0 | P1 pair memory vs user: % follows user |
| `\PonePairMemoryVsUserFollowBLo` | 22.2 | P1 pair memory vs user: % follows user, lower 95% CI bound |
| `\PonePairMemoryVsUserFollowBHi` | 77.8 | P1 pair memory vs user: % follows user, upper 95% CI bound |
| `\PonePairMemoryVsUserFollowBCI` | [22.2, 77.8] | P1 pair memory vs user: % follows user, 95% CI |
| `\PonePairMemoryVsUserFollowBN` | 18 | P1 pair memory vs user: % follows user, n |
| `\PonePairMemoryVsUserFollowBP` | n/a | P1 pair memory vs user: % follows user, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsUserEsc` | 50.0 | P1 pair memory vs user: % flags conflict |
| `\PonePairMemoryVsUserEscLo` | 22.2 | P1 pair memory vs user: % flags conflict, lower 95% CI bound |
| `\PonePairMemoryVsUserEscHi` | 77.8 | P1 pair memory vs user: % flags conflict, upper 95% CI bound |
| `\PonePairMemoryVsUserEscCI` | [22.2, 77.8] | P1 pair memory vs user: % flags conflict, 95% CI |
| `\PonePairMemoryVsUserEscN` | 18 | P1 pair memory vs user: % flags conflict, n |
| `\PonePairMemoryVsUserEscP` | n/a | P1 pair memory vs user: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsUserNet` | \ensuremath{-}50.0 | P1 pair memory vs user: net A - B (pp) |
| `\PonePairMemoryVsUserNetLo` | \ensuremath{-}77.8 | P1 pair memory vs user: net A - B (pp), lower 95% CI bound |
| `\PonePairMemoryVsUserNetHi` | \ensuremath{-}22.2 | P1 pair memory vs user: net A - B (pp), upper 95% CI bound |
| `\PonePairMemoryVsUserNetCI` | [\ensuremath{-}77.8, \ensuremath{-}22.2] | P1 pair memory vs user: net A - B (pp), 95% CI |
| `\PonePairMemoryVsUserNetN` | 18 | P1 pair memory vs user: net A - B (pp), n |
| `\PonePairMemoryVsUserNetP` | \ensuremath{<}0.001 | P1 pair memory vs user: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsAgentFollowA` | 0.0 | P1 pair memory vs agent: % follows memory |
| `\PonePairMemoryVsAgentFollowALo` | 0.0 | P1 pair memory vs agent: % follows memory, lower 95% CI bound |
| `\PonePairMemoryVsAgentFollowAHi` | 18.5 | P1 pair memory vs agent: % follows memory, upper 95% CI bound |
| `\PonePairMemoryVsAgentFollowACI` | [0.0, 18.5] | P1 pair memory vs agent: % follows memory, 95% CI |
| `\PonePairMemoryVsAgentFollowAN` | 18 | P1 pair memory vs agent: % follows memory, n |
| `\PonePairMemoryVsAgentFollowAP` | n/a | P1 pair memory vs agent: % follows memory, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsAgentFollowB` | 44.4 | P1 pair memory vs agent: % follows agent |
| `\PonePairMemoryVsAgentFollowBLo` | 27.8 | P1 pair memory vs agent: % follows agent, lower 95% CI bound |
| `\PonePairMemoryVsAgentFollowBHi` | 61.2 | P1 pair memory vs agent: % follows agent, upper 95% CI bound |
| `\PonePairMemoryVsAgentFollowBCI` | [27.8, 61.2] | P1 pair memory vs agent: % follows agent, 95% CI |
| `\PonePairMemoryVsAgentFollowBN` | 18 | P1 pair memory vs agent: % follows agent, n |
| `\PonePairMemoryVsAgentFollowBP` | n/a | P1 pair memory vs agent: % follows agent, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsAgentEsc` | 55.6 | P1 pair memory vs agent: % flags conflict |
| `\PonePairMemoryVsAgentEscLo` | 38.9 | P1 pair memory vs agent: % flags conflict, lower 95% CI bound |
| `\PonePairMemoryVsAgentEscHi` | 72.2 | P1 pair memory vs agent: % flags conflict, upper 95% CI bound |
| `\PonePairMemoryVsAgentEscCI` | [38.9, 72.2] | P1 pair memory vs agent: % flags conflict, 95% CI |
| `\PonePairMemoryVsAgentEscN` | 18 | P1 pair memory vs agent: % flags conflict, n |
| `\PonePairMemoryVsAgentEscP` | n/a | P1 pair memory vs agent: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsAgentNet` | \ensuremath{-}44.4 | P1 pair memory vs agent: net A - B (pp) |
| `\PonePairMemoryVsAgentNetLo` | \ensuremath{-}61.1 | P1 pair memory vs agent: net A - B (pp), lower 95% CI bound |
| `\PonePairMemoryVsAgentNetHi` | \ensuremath{-}27.8 | P1 pair memory vs agent: net A - B (pp), upper 95% CI bound |
| `\PonePairMemoryVsAgentNetCI` | [\ensuremath{-}61.1, \ensuremath{-}27.8] | P1 pair memory vs agent: net A - B (pp), 95% CI |
| `\PonePairMemoryVsAgentNetN` | 18 | P1 pair memory vs agent: net A - B (pp), n |
| `\PonePairMemoryVsAgentNetP` | \ensuremath{<}0.001 | P1 pair memory vs agent: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsUnattributedFollowA` | 0.0 | P1 pair memory vs unattributed: % follows memory |
| `\PonePairMemoryVsUnattributedFollowALo` | 0.0 | P1 pair memory vs unattributed: % follows memory, lower 95% CI bound |
| `\PonePairMemoryVsUnattributedFollowAHi` | 18.5 | P1 pair memory vs unattributed: % follows memory, upper 95% CI bound |
| `\PonePairMemoryVsUnattributedFollowACI` | [0.0, 18.5] | P1 pair memory vs unattributed: % follows memory, 95% CI |
| `\PonePairMemoryVsUnattributedFollowAN` | 18 | P1 pair memory vs unattributed: % follows memory, n |
| `\PonePairMemoryVsUnattributedFollowAP` | n/a | P1 pair memory vs unattributed: % follows memory, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsUnattributedFollowB` | 44.4 | P1 pair memory vs unattributed: % follows unattributed |
| `\PonePairMemoryVsUnattributedFollowBLo` | 22.2 | P1 pair memory vs unattributed: % follows unattributed, lower 95% CI bound |
| `\PonePairMemoryVsUnattributedFollowBHi` | 66.8 | P1 pair memory vs unattributed: % follows unattributed, upper 95% CI bound |
| `\PonePairMemoryVsUnattributedFollowBCI` | [22.2, 66.8] | P1 pair memory vs unattributed: % follows unattributed, 95% CI |
| `\PonePairMemoryVsUnattributedFollowBN` | 18 | P1 pair memory vs unattributed: % follows unattributed, n |
| `\PonePairMemoryVsUnattributedFollowBP` | n/a | P1 pair memory vs unattributed: % follows unattributed, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsUnattributedEsc` | 55.6 | P1 pair memory vs unattributed: % flags conflict |
| `\PonePairMemoryVsUnattributedEscLo` | 33.3 | P1 pair memory vs unattributed: % flags conflict, lower 95% CI bound |
| `\PonePairMemoryVsUnattributedEscHi` | 77.8 | P1 pair memory vs unattributed: % flags conflict, upper 95% CI bound |
| `\PonePairMemoryVsUnattributedEscCI` | [33.3, 77.8] | P1 pair memory vs unattributed: % flags conflict, 95% CI |
| `\PonePairMemoryVsUnattributedEscN` | 18 | P1 pair memory vs unattributed: % flags conflict, n |
| `\PonePairMemoryVsUnattributedEscP` | n/a | P1 pair memory vs unattributed: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsUnattributedNet` | \ensuremath{-}44.4 | P1 pair memory vs unattributed: net A - B (pp) |
| `\PonePairMemoryVsUnattributedNetLo` | \ensuremath{-}66.7 | P1 pair memory vs unattributed: net A - B (pp), lower 95% CI bound |
| `\PonePairMemoryVsUnattributedNetHi` | \ensuremath{-}22.2 | P1 pair memory vs unattributed: net A - B (pp), upper 95% CI bound |
| `\PonePairMemoryVsUnattributedNetCI` | [\ensuremath{-}66.7, \ensuremath{-}22.2] | P1 pair memory vs unattributed: net A - B (pp), 95% CI |
| `\PonePairMemoryVsUnattributedNetN` | 18 | P1 pair memory vs unattributed: net A - B (pp), n |
| `\PonePairMemoryVsUnattributedNetP` | 0.002 | P1 pair memory vs unattributed: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsDocumentFollowA` | 0.0 | P1 pair memory vs document: % follows memory |
| `\PonePairMemoryVsDocumentFollowALo` | 0.0 | P1 pair memory vs document: % follows memory, lower 95% CI bound |
| `\PonePairMemoryVsDocumentFollowAHi` | 18.5 | P1 pair memory vs document: % follows memory, upper 95% CI bound |
| `\PonePairMemoryVsDocumentFollowACI` | [0.0, 18.5] | P1 pair memory vs document: % follows memory, 95% CI |
| `\PonePairMemoryVsDocumentFollowAN` | 18 | P1 pair memory vs document: % follows memory, n |
| `\PonePairMemoryVsDocumentFollowAP` | n/a | P1 pair memory vs document: % follows memory, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsDocumentFollowB` | 44.4 | P1 pair memory vs document: % follows document |
| `\PonePairMemoryVsDocumentFollowBLo` | 22.2 | P1 pair memory vs document: % follows document, lower 95% CI bound |
| `\PonePairMemoryVsDocumentFollowBHi` | 66.7 | P1 pair memory vs document: % follows document, upper 95% CI bound |
| `\PonePairMemoryVsDocumentFollowBCI` | [22.2, 66.7] | P1 pair memory vs document: % follows document, 95% CI |
| `\PonePairMemoryVsDocumentFollowBN` | 18 | P1 pair memory vs document: % follows document, n |
| `\PonePairMemoryVsDocumentFollowBP` | n/a | P1 pair memory vs document: % follows document, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsDocumentEsc` | 55.6 | P1 pair memory vs document: % flags conflict |
| `\PonePairMemoryVsDocumentEscLo` | 33.3 | P1 pair memory vs document: % flags conflict, lower 95% CI bound |
| `\PonePairMemoryVsDocumentEscHi` | 77.8 | P1 pair memory vs document: % flags conflict, upper 95% CI bound |
| `\PonePairMemoryVsDocumentEscCI` | [33.3, 77.8] | P1 pair memory vs document: % flags conflict, 95% CI |
| `\PonePairMemoryVsDocumentEscN` | 18 | P1 pair memory vs document: % flags conflict, n |
| `\PonePairMemoryVsDocumentEscP` | n/a | P1 pair memory vs document: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsDocumentNet` | \ensuremath{-}44.4 | P1 pair memory vs document: net A - B (pp) |
| `\PonePairMemoryVsDocumentNetLo` | \ensuremath{-}66.7 | P1 pair memory vs document: net A - B (pp), lower 95% CI bound |
| `\PonePairMemoryVsDocumentNetHi` | \ensuremath{-}22.2 | P1 pair memory vs document: net A - B (pp), upper 95% CI bound |
| `\PonePairMemoryVsDocumentNetCI` | [\ensuremath{-}66.7, \ensuremath{-}22.2] | P1 pair memory vs document: net A - B (pp), 95% CI |
| `\PonePairMemoryVsDocumentNetN` | 18 | P1 pair memory vs document: net A - B (pp), n |
| `\PonePairMemoryVsDocumentNetP` | \ensuremath{<}0.001 | P1 pair memory vs document: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsWebFollowA` | 16.7 | P1 pair tool vs web: % follows tool |
| `\PonePairToolVsWebFollowALo` | 0.0 | P1 pair tool vs web: % follows tool, lower 95% CI bound |
| `\PonePairToolVsWebFollowAHi` | 50.0 | P1 pair tool vs web: % follows tool, upper 95% CI bound |
| `\PonePairToolVsWebFollowACI` | [0.0, 50.0] | P1 pair tool vs web: % follows tool, 95% CI |
| `\PonePairToolVsWebFollowAN` | 6 | P1 pair tool vs web: % follows tool, n |
| `\PonePairToolVsWebFollowAP` | n/a | P1 pair tool vs web: % follows tool, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsWebFollowB` | 0.0 | P1 pair tool vs web: % follows web |
| `\PonePairToolVsWebFollowBLo` | 0.0 | P1 pair tool vs web: % follows web, lower 95% CI bound |
| `\PonePairToolVsWebFollowBHi` | 45.9 | P1 pair tool vs web: % follows web, upper 95% CI bound |
| `\PonePairToolVsWebFollowBCI` | [0.0, 45.9] | P1 pair tool vs web: % follows web, 95% CI |
| `\PonePairToolVsWebFollowBN` | 6 | P1 pair tool vs web: % follows web, n |
| `\PonePairToolVsWebFollowBP` | n/a | P1 pair tool vs web: % follows web, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsWebEsc` | 83.3 | P1 pair tool vs web: % flags conflict |
| `\PonePairToolVsWebEscLo` | 50.0 | P1 pair tool vs web: % flags conflict, lower 95% CI bound |
| `\PonePairToolVsWebEscHi` | 100.0 | P1 pair tool vs web: % flags conflict, upper 95% CI bound |
| `\PonePairToolVsWebEscCI` | [50.0, 100.0] | P1 pair tool vs web: % flags conflict, 95% CI |
| `\PonePairToolVsWebEscN` | 6 | P1 pair tool vs web: % flags conflict, n |
| `\PonePairToolVsWebEscP` | n/a | P1 pair tool vs web: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsWebNet` | 16.7 | P1 pair tool vs web: net A - B (pp) |
| `\PonePairToolVsWebNetLo` | 0.0 | P1 pair tool vs web: net A - B (pp), lower 95% CI bound |
| `\PonePairToolVsWebNetHi` | 50.0 | P1 pair tool vs web: net A - B (pp), upper 95% CI bound |
| `\PonePairToolVsWebNetCI` | [0.0, 50.0] | P1 pair tool vs web: net A - B (pp), 95% CI |
| `\PonePairToolVsWebNetN` | 6 | P1 pair tool vs web: net A - B (pp), n |
| `\PonePairToolVsWebNetP` | 0.593 | P1 pair tool vs web: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsUserFollowA` | 0.0 | P1 pair tool vs user: % follows tool |
| `\PonePairToolVsUserFollowALo` | 0.0 | P1 pair tool vs user: % follows tool, lower 95% CI bound |
| `\PonePairToolVsUserFollowAHi` | 18.5 | P1 pair tool vs user: % follows tool, upper 95% CI bound |
| `\PonePairToolVsUserFollowACI` | [0.0, 18.5] | P1 pair tool vs user: % follows tool, 95% CI |
| `\PonePairToolVsUserFollowAN` | 18 | P1 pair tool vs user: % follows tool, n |
| `\PonePairToolVsUserFollowAP` | n/a | P1 pair tool vs user: % follows tool, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsUserFollowB` | 22.2 | P1 pair tool vs user: % follows user |
| `\PonePairToolVsUserFollowBLo` | 5.6 | P1 pair tool vs user: % follows user, lower 95% CI bound |
| `\PonePairToolVsUserFollowBHi` | 38.9 | P1 pair tool vs user: % follows user, upper 95% CI bound |
| `\PonePairToolVsUserFollowBCI` | [5.6, 38.9] | P1 pair tool vs user: % follows user, 95% CI |
| `\PonePairToolVsUserFollowBN` | 18 | P1 pair tool vs user: % follows user, n |
| `\PonePairToolVsUserFollowBP` | n/a | P1 pair tool vs user: % follows user, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsUserEsc` | 72.2 | P1 pair tool vs user: % flags conflict |
| `\PonePairToolVsUserEscLo` | 50.0 | P1 pair tool vs user: % flags conflict, lower 95% CI bound |
| `\PonePairToolVsUserEscHi` | 94.4 | P1 pair tool vs user: % flags conflict, upper 95% CI bound |
| `\PonePairToolVsUserEscCI` | [50.0, 94.4] | P1 pair tool vs user: % flags conflict, 95% CI |
| `\PonePairToolVsUserEscN` | 18 | P1 pair tool vs user: % flags conflict, n |
| `\PonePairToolVsUserEscP` | n/a | P1 pair tool vs user: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsUserNet` | \ensuremath{-}22.2 | P1 pair tool vs user: net A - B (pp) |
| `\PonePairToolVsUserNetLo` | \ensuremath{-}38.9 | P1 pair tool vs user: net A - B (pp), lower 95% CI bound |
| `\PonePairToolVsUserNetHi` | \ensuremath{-}5.6 | P1 pair tool vs user: net A - B (pp), upper 95% CI bound |
| `\PonePairToolVsUserNetCI` | [\ensuremath{-}38.9, \ensuremath{-}5.6] | P1 pair tool vs user: net A - B (pp), 95% CI |
| `\PonePairToolVsUserNetN` | 18 | P1 pair tool vs user: net A - B (pp), n |
| `\PonePairToolVsUserNetP` | 0.009 | P1 pair tool vs user: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsAgentFollowA` | 0.0 | P1 pair tool vs agent: % follows tool |
| `\PonePairToolVsAgentFollowALo` | 0.0 | P1 pair tool vs agent: % follows tool, lower 95% CI bound |
| `\PonePairToolVsAgentFollowAHi` | 45.9 | P1 pair tool vs agent: % follows tool, upper 95% CI bound |
| `\PonePairToolVsAgentFollowACI` | [0.0, 45.9] | P1 pair tool vs agent: % follows tool, 95% CI |
| `\PonePairToolVsAgentFollowAN` | 6 | P1 pair tool vs agent: % follows tool, n |
| `\PonePairToolVsAgentFollowAP` | n/a | P1 pair tool vs agent: % follows tool, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsAgentFollowB` | 0.0 | P1 pair tool vs agent: % follows agent |
| `\PonePairToolVsAgentFollowBLo` | 0.0 | P1 pair tool vs agent: % follows agent, lower 95% CI bound |
| `\PonePairToolVsAgentFollowBHi` | 45.9 | P1 pair tool vs agent: % follows agent, upper 95% CI bound |
| `\PonePairToolVsAgentFollowBCI` | [0.0, 45.9] | P1 pair tool vs agent: % follows agent, 95% CI |
| `\PonePairToolVsAgentFollowBN` | 6 | P1 pair tool vs agent: % follows agent, n |
| `\PonePairToolVsAgentFollowBP` | n/a | P1 pair tool vs agent: % follows agent, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsAgentEsc` | 100.0 | P1 pair tool vs agent: % flags conflict |
| `\PonePairToolVsAgentEscLo` | 54.1 | P1 pair tool vs agent: % flags conflict, lower 95% CI bound |
| `\PonePairToolVsAgentEscHi` | 100.0 | P1 pair tool vs agent: % flags conflict, upper 95% CI bound |
| `\PonePairToolVsAgentEscCI` | [54.1, 100.0] | P1 pair tool vs agent: % flags conflict, 95% CI |
| `\PonePairToolVsAgentEscN` | 6 | P1 pair tool vs agent: % flags conflict, n |
| `\PonePairToolVsAgentEscP` | n/a | P1 pair tool vs agent: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsAgentNet` | 0.0 | P1 pair tool vs agent: net A - B (pp) |
| `\PonePairToolVsAgentNetLo` | 0.0 | P1 pair tool vs agent: net A - B (pp), lower 95% CI bound |
| `\PonePairToolVsAgentNetHi` | 0.0 | P1 pair tool vs agent: net A - B (pp), upper 95% CI bound |
| `\PonePairToolVsAgentNetCI` | [0.0, 0.0] | P1 pair tool vs agent: net A - B (pp), 95% CI |
| `\PonePairToolVsAgentNetN` | 6 | P1 pair tool vs agent: net A - B (pp), n |
| `\PonePairToolVsAgentNetP` | 1.000 | P1 pair tool vs agent: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsAgentFollowA` | 0.0 | P1 pair web vs agent: % follows web |
| `\PonePairWebVsAgentFollowALo` | 0.0 | P1 pair web vs agent: % follows web, lower 95% CI bound |
| `\PonePairWebVsAgentFollowAHi` | 60.2 | P1 pair web vs agent: % follows web, upper 95% CI bound |
| `\PonePairWebVsAgentFollowACI` | [0.0, 60.2] | P1 pair web vs agent: % follows web, 95% CI |
| `\PonePairWebVsAgentFollowAN` | 4 | P1 pair web vs agent: % follows web, n |
| `\PonePairWebVsAgentFollowAP` | n/a | P1 pair web vs agent: % follows web, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsAgentFollowB` | 0.0 | P1 pair web vs agent: % follows agent |
| `\PonePairWebVsAgentFollowBLo` | 0.0 | P1 pair web vs agent: % follows agent, lower 95% CI bound |
| `\PonePairWebVsAgentFollowBHi` | 60.2 | P1 pair web vs agent: % follows agent, upper 95% CI bound |
| `\PonePairWebVsAgentFollowBCI` | [0.0, 60.2] | P1 pair web vs agent: % follows agent, 95% CI |
| `\PonePairWebVsAgentFollowBN` | 4 | P1 pair web vs agent: % follows agent, n |
| `\PonePairWebVsAgentFollowBP` | n/a | P1 pair web vs agent: % follows agent, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsAgentEsc` | 100.0 | P1 pair web vs agent: % flags conflict |
| `\PonePairWebVsAgentEscLo` | 39.8 | P1 pair web vs agent: % flags conflict, lower 95% CI bound |
| `\PonePairWebVsAgentEscHi` | 100.0 | P1 pair web vs agent: % flags conflict, upper 95% CI bound |
| `\PonePairWebVsAgentEscCI` | [39.8, 100.0] | P1 pair web vs agent: % flags conflict, 95% CI |
| `\PonePairWebVsAgentEscN` | 4 | P1 pair web vs agent: % flags conflict, n |
| `\PonePairWebVsAgentEscP` | n/a | P1 pair web vs agent: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsAgentNet` | 0.0 | P1 pair web vs agent: net A - B (pp) |
| `\PonePairWebVsAgentNetLo` | 0.0 | P1 pair web vs agent: net A - B (pp), lower 95% CI bound |
| `\PonePairWebVsAgentNetHi` | 0.0 | P1 pair web vs agent: net A - B (pp), upper 95% CI bound |
| `\PonePairWebVsAgentNetCI` | [0.0, 0.0] | P1 pair web vs agent: net A - B (pp), 95% CI |
| `\PonePairWebVsAgentNetN` | 4 | P1 pair web vs agent: net A - B (pp), n |
| `\PonePairWebVsAgentNetP` | 1.000 | P1 pair web vs agent: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsUnattributedFollowA` | 0.0 | P1 pair web vs unattributed: % follows web |
| `\PonePairWebVsUnattributedFollowALo` | 0.0 | P1 pair web vs unattributed: % follows web, lower 95% CI bound |
| `\PonePairWebVsUnattributedFollowAHi` | 45.9 | P1 pair web vs unattributed: % follows web, upper 95% CI bound |
| `\PonePairWebVsUnattributedFollowACI` | [0.0, 45.9] | P1 pair web vs unattributed: % follows web, 95% CI |
| `\PonePairWebVsUnattributedFollowAN` | 6 | P1 pair web vs unattributed: % follows web, n |
| `\PonePairWebVsUnattributedFollowAP` | n/a | P1 pair web vs unattributed: % follows web, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsUnattributedFollowB` | 16.7 | P1 pair web vs unattributed: % follows unattributed |
| `\PonePairWebVsUnattributedFollowBLo` | 0.0 | P1 pair web vs unattributed: % follows unattributed, lower 95% CI bound |
| `\PonePairWebVsUnattributedFollowBHi` | 50.0 | P1 pair web vs unattributed: % follows unattributed, upper 95% CI bound |
| `\PonePairWebVsUnattributedFollowBCI` | [0.0, 50.0] | P1 pair web vs unattributed: % follows unattributed, 95% CI |
| `\PonePairWebVsUnattributedFollowBN` | 6 | P1 pair web vs unattributed: % follows unattributed, n |
| `\PonePairWebVsUnattributedFollowBP` | n/a | P1 pair web vs unattributed: % follows unattributed, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsUnattributedEsc` | 83.3 | P1 pair web vs unattributed: % flags conflict |
| `\PonePairWebVsUnattributedEscLo` | 50.0 | P1 pair web vs unattributed: % flags conflict, lower 95% CI bound |
| `\PonePairWebVsUnattributedEscHi` | 100.0 | P1 pair web vs unattributed: % flags conflict, upper 95% CI bound |
| `\PonePairWebVsUnattributedEscCI` | [50.0, 100.0] | P1 pair web vs unattributed: % flags conflict, 95% CI |
| `\PonePairWebVsUnattributedEscN` | 6 | P1 pair web vs unattributed: % flags conflict, n |
| `\PonePairWebVsUnattributedEscP` | n/a | P1 pair web vs unattributed: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsUnattributedNet` | \ensuremath{-}16.7 | P1 pair web vs unattributed: net A - B (pp) |
| `\PonePairWebVsUnattributedNetLo` | \ensuremath{-}50.0 | P1 pair web vs unattributed: net A - B (pp), lower 95% CI bound |
| `\PonePairWebVsUnattributedNetHi` | 0.0 | P1 pair web vs unattributed: net A - B (pp), upper 95% CI bound |
| `\PonePairWebVsUnattributedNetCI` | [\ensuremath{-}50.0, 0.0] | P1 pair web vs unattributed: net A - B (pp), 95% CI |
| `\PonePairWebVsUnattributedNetN` | 6 | P1 pair web vs unattributed: net A - B (pp), n |
| `\PonePairWebVsUnattributedNetP` | 0.605 | P1 pair web vs unattributed: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsDocumentFollowA` | 0.0 | P1 pair web vs document: % follows web |
| `\PonePairWebVsDocumentFollowALo` | 0.0 | P1 pair web vs document: % follows web, lower 95% CI bound |
| `\PonePairWebVsDocumentFollowAHi` | 45.9 | P1 pair web vs document: % follows web, upper 95% CI bound |
| `\PonePairWebVsDocumentFollowACI` | [0.0, 45.9] | P1 pair web vs document: % follows web, 95% CI |
| `\PonePairWebVsDocumentFollowAN` | 6 | P1 pair web vs document: % follows web, n |
| `\PonePairWebVsDocumentFollowAP` | n/a | P1 pair web vs document: % follows web, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsDocumentFollowB` | 50.0 | P1 pair web vs document: % follows document |
| `\PonePairWebVsDocumentFollowBLo` | 0.0 | P1 pair web vs document: % follows document, lower 95% CI bound |
| `\PonePairWebVsDocumentFollowBHi` | 100.0 | P1 pair web vs document: % follows document, upper 95% CI bound |
| `\PonePairWebVsDocumentFollowBCI` | [0.0, 100.0] | P1 pair web vs document: % follows document, 95% CI |
| `\PonePairWebVsDocumentFollowBN` | 6 | P1 pair web vs document: % follows document, n |
| `\PonePairWebVsDocumentFollowBP` | n/a | P1 pair web vs document: % follows document, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsDocumentEsc` | 50.0 | P1 pair web vs document: % flags conflict |
| `\PonePairWebVsDocumentEscLo` | 0.0 | P1 pair web vs document: % flags conflict, lower 95% CI bound |
| `\PonePairWebVsDocumentEscHi` | 100.0 | P1 pair web vs document: % flags conflict, upper 95% CI bound |
| `\PonePairWebVsDocumentEscCI` | [0.0, 100.0] | P1 pair web vs document: % flags conflict, 95% CI |
| `\PonePairWebVsDocumentEscN` | 6 | P1 pair web vs document: % flags conflict, n |
| `\PonePairWebVsDocumentEscP` | n/a | P1 pair web vs document: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsDocumentNet` | \ensuremath{-}50.0 | P1 pair web vs document: net A - B (pp) |
| `\PonePairWebVsDocumentNetLo` | \ensuremath{-}100.0 | P1 pair web vs document: net A - B (pp), lower 95% CI bound |
| `\PonePairWebVsDocumentNetHi` | 0.0 | P1 pair web vs document: net A - B (pp), upper 95% CI bound |
| `\PonePairWebVsDocumentNetCI` | [\ensuremath{-}100.0, 0.0] | P1 pair web vs document: net A - B (pp), 95% CI |
| `\PonePairWebVsDocumentNetN` | 6 | P1 pair web vs document: net A - B (pp), n |
| `\PonePairWebVsDocumentNetP` | 0.085 | P1 pair web vs document: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsAgentFollowA` | 50.0 | P1 pair user vs agent: % follows user |
| `\PonePairUserVsAgentFollowALo` | 50.0 | P1 pair user vs agent: % follows user, lower 95% CI bound |
| `\PonePairUserVsAgentFollowAHi` | 50.0 | P1 pair user vs agent: % follows user, upper 95% CI bound |
| `\PonePairUserVsAgentFollowACI` | [50.0, 50.0] | P1 pair user vs agent: % follows user, 95% CI |
| `\PonePairUserVsAgentFollowAN` | 2 | P1 pair user vs agent: % follows user, n |
| `\PonePairUserVsAgentFollowAP` | n/a | P1 pair user vs agent: % follows user, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsAgentFollowB` | 0.0 | P1 pair user vs agent: % follows agent |
| `\PonePairUserVsAgentFollowBLo` | 0.0 | P1 pair user vs agent: % follows agent, lower 95% CI bound |
| `\PonePairUserVsAgentFollowBHi` | 84.2 | P1 pair user vs agent: % follows agent, upper 95% CI bound |
| `\PonePairUserVsAgentFollowBCI` | [0.0, 84.2] | P1 pair user vs agent: % follows agent, 95% CI |
| `\PonePairUserVsAgentFollowBN` | 2 | P1 pair user vs agent: % follows agent, n |
| `\PonePairUserVsAgentFollowBP` | n/a | P1 pair user vs agent: % follows agent, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsAgentEsc` | 50.0 | P1 pair user vs agent: % flags conflict |
| `\PonePairUserVsAgentEscLo` | 50.0 | P1 pair user vs agent: % flags conflict, lower 95% CI bound |
| `\PonePairUserVsAgentEscHi` | 50.0 | P1 pair user vs agent: % flags conflict, upper 95% CI bound |
| `\PonePairUserVsAgentEscCI` | [50.0, 50.0] | P1 pair user vs agent: % flags conflict, 95% CI |
| `\PonePairUserVsAgentEscN` | 2 | P1 pair user vs agent: % flags conflict, n |
| `\PonePairUserVsAgentEscP` | n/a | P1 pair user vs agent: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsAgentNet` | 50.0 | P1 pair user vs agent: net A - B (pp) |
| `\PonePairUserVsAgentNetLo` | 50.0 | P1 pair user vs agent: net A - B (pp), lower 95% CI bound |
| `\PonePairUserVsAgentNetHi` | 50.0 | P1 pair user vs agent: net A - B (pp), upper 95% CI bound |
| `\PonePairUserVsAgentNetCI` | [50.0, 50.0] | P1 pair user vs agent: net A - B (pp), 95% CI |
| `\PonePairUserVsAgentNetN` | 2 | P1 pair user vs agent: net A - B (pp), n |
| `\PonePairUserVsAgentNetP` | \ensuremath{<}0.001 | P1 pair user vs agent: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsDocumentFollowA` | 16.7 | P1 pair user vs document: % follows user |
| `\PonePairUserVsDocumentFollowALo` | 0.0 | P1 pair user vs document: % follows user, lower 95% CI bound |
| `\PonePairUserVsDocumentFollowAHi` | 38.9 | P1 pair user vs document: % follows user, upper 95% CI bound |
| `\PonePairUserVsDocumentFollowACI` | [0.0, 38.9] | P1 pair user vs document: % follows user, 95% CI |
| `\PonePairUserVsDocumentFollowAN` | 18 | P1 pair user vs document: % follows user, n |
| `\PonePairUserVsDocumentFollowAP` | n/a | P1 pair user vs document: % follows user, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsDocumentFollowB` | 11.1 | P1 pair user vs document: % follows document |
| `\PonePairUserVsDocumentFollowBLo` | 0.0 | P1 pair user vs document: % follows document, lower 95% CI bound |
| `\PonePairUserVsDocumentFollowBHi` | 33.3 | P1 pair user vs document: % follows document, upper 95% CI bound |
| `\PonePairUserVsDocumentFollowBCI` | [0.0, 33.3] | P1 pair user vs document: % follows document, 95% CI |
| `\PonePairUserVsDocumentFollowBN` | 18 | P1 pair user vs document: % follows document, n |
| `\PonePairUserVsDocumentFollowBP` | n/a | P1 pair user vs document: % follows document, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsDocumentEsc` | 72.2 | P1 pair user vs document: % flags conflict |
| `\PonePairUserVsDocumentEscLo` | 44.4 | P1 pair user vs document: % flags conflict, lower 95% CI bound |
| `\PonePairUserVsDocumentEscHi` | 100.0 | P1 pair user vs document: % flags conflict, upper 95% CI bound |
| `\PonePairUserVsDocumentEscCI` | [44.4, 100.0] | P1 pair user vs document: % flags conflict, 95% CI |
| `\PonePairUserVsDocumentEscN` | 18 | P1 pair user vs document: % flags conflict, n |
| `\PonePairUserVsDocumentEscP` | n/a | P1 pair user vs document: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsDocumentNet` | 5.6 | P1 pair user vs document: net A - B (pp) |
| `\PonePairUserVsDocumentNetLo` | \ensuremath{-}22.2 | P1 pair user vs document: net A - B (pp), lower 95% CI bound |
| `\PonePairUserVsDocumentNetHi` | 38.9 | P1 pair user vs document: net A - B (pp), upper 95% CI bound |
| `\PonePairUserVsDocumentNetCI` | [\ensuremath{-}22.2, 38.9] | P1 pair user vs document: net A - B (pp), 95% CI |
| `\PonePairUserVsDocumentNetN` | 18 | P1 pair user vs document: net A - B (pp), n |
| `\PonePairUserVsDocumentNetP` | 0.834 | P1 pair user vs document: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairUnattributedVsDocumentFollowA` | 0.0 | P1 pair unattributed vs document: % follows unattributed |
| `\PonePairUnattributedVsDocumentFollowALo` | 0.0 | P1 pair unattributed vs document: % follows unattributed, lower 95% CI bound |
| `\PonePairUnattributedVsDocumentFollowAHi` | 45.9 | P1 pair unattributed vs document: % follows unattributed, upper 95% CI bound |
| `\PonePairUnattributedVsDocumentFollowACI` | [0.0, 45.9] | P1 pair unattributed vs document: % follows unattributed, 95% CI |
| `\PonePairUnattributedVsDocumentFollowAN` | 6 | P1 pair unattributed vs document: % follows unattributed, n |
| `\PonePairUnattributedVsDocumentFollowAP` | n/a | P1 pair unattributed vs document: % follows unattributed, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUnattributedVsDocumentFollowB` | 16.7 | P1 pair unattributed vs document: % follows document |
| `\PonePairUnattributedVsDocumentFollowBLo` | 0.0 | P1 pair unattributed vs document: % follows document, lower 95% CI bound |
| `\PonePairUnattributedVsDocumentFollowBHi` | 50.0 | P1 pair unattributed vs document: % follows document, upper 95% CI bound |
| `\PonePairUnattributedVsDocumentFollowBCI` | [0.0, 50.0] | P1 pair unattributed vs document: % follows document, 95% CI |
| `\PonePairUnattributedVsDocumentFollowBN` | 6 | P1 pair unattributed vs document: % follows document, n |
| `\PonePairUnattributedVsDocumentFollowBP` | n/a | P1 pair unattributed vs document: % follows document, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUnattributedVsDocumentEsc` | 83.3 | P1 pair unattributed vs document: % flags conflict |
| `\PonePairUnattributedVsDocumentEscLo` | 50.0 | P1 pair unattributed vs document: % flags conflict, lower 95% CI bound |
| `\PonePairUnattributedVsDocumentEscHi` | 100.0 | P1 pair unattributed vs document: % flags conflict, upper 95% CI bound |
| `\PonePairUnattributedVsDocumentEscCI` | [50.0, 100.0] | P1 pair unattributed vs document: % flags conflict, 95% CI |
| `\PonePairUnattributedVsDocumentEscN` | 6 | P1 pair unattributed vs document: % flags conflict, n |
| `\PonePairUnattributedVsDocumentEscP` | n/a | P1 pair unattributed vs document: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUnattributedVsDocumentNet` | \ensuremath{-}16.7 | P1 pair unattributed vs document: net A - B (pp) |
| `\PonePairUnattributedVsDocumentNetLo` | \ensuremath{-}50.0 | P1 pair unattributed vs document: net A - B (pp), lower 95% CI bound |
| `\PonePairUnattributedVsDocumentNetHi` | 0.0 | P1 pair unattributed vs document: net A - B (pp), upper 95% CI bound |
| `\PonePairUnattributedVsDocumentNetCI` | [\ensuremath{-}50.0, 0.0] | P1 pair unattributed vs document: net A - B (pp), 95% CI |
| `\PonePairUnattributedVsDocumentNetN` | 6 | P1 pair unattributed vs document: net A - B (pp), n |
| `\PonePairUnattributedVsDocumentNetP` | 0.575 | P1 pair unattributed vs document: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsToolFollowA` | 5.6 | P1 forced memory vs tool: % follows memory |
| `\PoneForcedMemoryVsToolFollowALo` | 0.0 | P1 forced memory vs tool: % follows memory, lower 95% CI bound |
| `\PoneForcedMemoryVsToolFollowAHi` | 16.7 | P1 forced memory vs tool: % follows memory, upper 95% CI bound |
| `\PoneForcedMemoryVsToolFollowACI` | [0.0, 16.7] | P1 forced memory vs tool: % follows memory, 95% CI |
| `\PoneForcedMemoryVsToolFollowAN` | 18 | P1 forced memory vs tool: % follows memory, n |
| `\PoneForcedMemoryVsToolFollowAP` | n/a | P1 forced memory vs tool: % follows memory, two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsToolFollowB` | 94.4 | P1 forced memory vs tool: % follows tool |
| `\PoneForcedMemoryVsToolFollowBLo` | 83.3 | P1 forced memory vs tool: % follows tool, lower 95% CI bound |
| `\PoneForcedMemoryVsToolFollowBHi` | 100.0 | P1 forced memory vs tool: % follows tool, upper 95% CI bound |
| `\PoneForcedMemoryVsToolFollowBCI` | [83.3, 100.0] | P1 forced memory vs tool: % follows tool, 95% CI |
| `\PoneForcedMemoryVsToolFollowBN` | 18 | P1 forced memory vs tool: % follows tool, n |
| `\PoneForcedMemoryVsToolFollowBP` | n/a | P1 forced memory vs tool: % follows tool, two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsToolEsc` | 0.0 | P1 forced memory vs tool: % flags conflict |
| `\PoneForcedMemoryVsToolEscLo` | 0.0 | P1 forced memory vs tool: % flags conflict, lower 95% CI bound |
| `\PoneForcedMemoryVsToolEscHi` | 18.5 | P1 forced memory vs tool: % flags conflict, upper 95% CI bound |
| `\PoneForcedMemoryVsToolEscCI` | [0.0, 18.5] | P1 forced memory vs tool: % flags conflict, 95% CI |
| `\PoneForcedMemoryVsToolEscN` | 18 | P1 forced memory vs tool: % flags conflict, n |
| `\PoneForcedMemoryVsToolEscP` | n/a | P1 forced memory vs tool: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsToolNet` | \ensuremath{-}88.9 | P1 forced memory vs tool: net A - B (pp) |
| `\PoneForcedMemoryVsToolNetLo` | \ensuremath{-}100.0 | P1 forced memory vs tool: net A - B (pp), lower 95% CI bound |
| `\PoneForcedMemoryVsToolNetHi` | \ensuremath{-}66.7 | P1 forced memory vs tool: net A - B (pp), upper 95% CI bound |
| `\PoneForcedMemoryVsToolNetCI` | [\ensuremath{-}100.0, \ensuremath{-}66.7] | P1 forced memory vs tool: net A - B (pp), 95% CI |
| `\PoneForcedMemoryVsToolNetN` | 18 | P1 forced memory vs tool: net A - B (pp), n |
| `\PoneForcedMemoryVsToolNetP` | \ensuremath{<}0.001 | P1 forced memory vs tool: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsUserFollowA` | 0.0 | P1 forced memory vs user: % follows memory |
| `\PoneForcedMemoryVsUserFollowALo` | 0.0 | P1 forced memory vs user: % follows memory, lower 95% CI bound |
| `\PoneForcedMemoryVsUserFollowAHi` | 18.5 | P1 forced memory vs user: % follows memory, upper 95% CI bound |
| `\PoneForcedMemoryVsUserFollowACI` | [0.0, 18.5] | P1 forced memory vs user: % follows memory, 95% CI |
| `\PoneForcedMemoryVsUserFollowAN` | 18 | P1 forced memory vs user: % follows memory, n |
| `\PoneForcedMemoryVsUserFollowAP` | n/a | P1 forced memory vs user: % follows memory, two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsUserFollowB` | 100.0 | P1 forced memory vs user: % follows user |
| `\PoneForcedMemoryVsUserFollowBLo` | 81.5 | P1 forced memory vs user: % follows user, lower 95% CI bound |
| `\PoneForcedMemoryVsUserFollowBHi` | 100.0 | P1 forced memory vs user: % follows user, upper 95% CI bound |
| `\PoneForcedMemoryVsUserFollowBCI` | [81.5, 100.0] | P1 forced memory vs user: % follows user, 95% CI |
| `\PoneForcedMemoryVsUserFollowBN` | 18 | P1 forced memory vs user: % follows user, n |
| `\PoneForcedMemoryVsUserFollowBP` | n/a | P1 forced memory vs user: % follows user, two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsUserEsc` | 0.0 | P1 forced memory vs user: % flags conflict |
| `\PoneForcedMemoryVsUserEscLo` | 0.0 | P1 forced memory vs user: % flags conflict, lower 95% CI bound |
| `\PoneForcedMemoryVsUserEscHi` | 18.5 | P1 forced memory vs user: % flags conflict, upper 95% CI bound |
| `\PoneForcedMemoryVsUserEscCI` | [0.0, 18.5] | P1 forced memory vs user: % flags conflict, 95% CI |
| `\PoneForcedMemoryVsUserEscN` | 18 | P1 forced memory vs user: % flags conflict, n |
| `\PoneForcedMemoryVsUserEscP` | n/a | P1 forced memory vs user: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsUserNet` | \ensuremath{-}100.0 | P1 forced memory vs user: net A - B (pp) |
| `\PoneForcedMemoryVsUserNetLo` | \ensuremath{-}100.0 | P1 forced memory vs user: net A - B (pp), lower 95% CI bound |
| `\PoneForcedMemoryVsUserNetHi` | \ensuremath{-}100.0 | P1 forced memory vs user: net A - B (pp), upper 95% CI bound |
| `\PoneForcedMemoryVsUserNetCI` | [\ensuremath{-}100.0, \ensuremath{-}100.0] | P1 forced memory vs user: net A - B (pp), 95% CI |
| `\PoneForcedMemoryVsUserNetN` | 18 | P1 forced memory vs user: net A - B (pp), n |
| `\PoneForcedMemoryVsUserNetP` | \ensuremath{<}0.001 | P1 forced memory vs user: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsDocumentFollowA` | 5.6 | P1 forced memory vs document: % follows memory |
| `\PoneForcedMemoryVsDocumentFollowALo` | 0.0 | P1 forced memory vs document: % follows memory, lower 95% CI bound |
| `\PoneForcedMemoryVsDocumentFollowAHi` | 16.7 | P1 forced memory vs document: % follows memory, upper 95% CI bound |
| `\PoneForcedMemoryVsDocumentFollowACI` | [0.0, 16.7] | P1 forced memory vs document: % follows memory, 95% CI |
| `\PoneForcedMemoryVsDocumentFollowAN` | 18 | P1 forced memory vs document: % follows memory, n |
| `\PoneForcedMemoryVsDocumentFollowAP` | n/a | P1 forced memory vs document: % follows memory, two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsDocumentFollowB` | 94.4 | P1 forced memory vs document: % follows document |
| `\PoneForcedMemoryVsDocumentFollowBLo` | 83.3 | P1 forced memory vs document: % follows document, lower 95% CI bound |
| `\PoneForcedMemoryVsDocumentFollowBHi` | 100.0 | P1 forced memory vs document: % follows document, upper 95% CI bound |
| `\PoneForcedMemoryVsDocumentFollowBCI` | [83.3, 100.0] | P1 forced memory vs document: % follows document, 95% CI |
| `\PoneForcedMemoryVsDocumentFollowBN` | 18 | P1 forced memory vs document: % follows document, n |
| `\PoneForcedMemoryVsDocumentFollowBP` | n/a | P1 forced memory vs document: % follows document, two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsDocumentEsc` | 0.0 | P1 forced memory vs document: % flags conflict |
| `\PoneForcedMemoryVsDocumentEscLo` | 0.0 | P1 forced memory vs document: % flags conflict, lower 95% CI bound |
| `\PoneForcedMemoryVsDocumentEscHi` | 18.5 | P1 forced memory vs document: % flags conflict, upper 95% CI bound |
| `\PoneForcedMemoryVsDocumentEscCI` | [0.0, 18.5] | P1 forced memory vs document: % flags conflict, 95% CI |
| `\PoneForcedMemoryVsDocumentEscN` | 18 | P1 forced memory vs document: % flags conflict, n |
| `\PoneForcedMemoryVsDocumentEscP` | n/a | P1 forced memory vs document: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsDocumentNet` | \ensuremath{-}88.9 | P1 forced memory vs document: net A - B (pp) |
| `\PoneForcedMemoryVsDocumentNetLo` | \ensuremath{-}100.0 | P1 forced memory vs document: net A - B (pp), lower 95% CI bound |
| `\PoneForcedMemoryVsDocumentNetHi` | \ensuremath{-}66.7 | P1 forced memory vs document: net A - B (pp), upper 95% CI bound |
| `\PoneForcedMemoryVsDocumentNetCI` | [\ensuremath{-}100.0, \ensuremath{-}66.7] | P1 forced memory vs document: net A - B (pp), 95% CI |
| `\PoneForcedMemoryVsDocumentNetN` | 18 | P1 forced memory vs document: net A - B (pp), n |
| `\PoneForcedMemoryVsDocumentNetP` | \ensuremath{<}0.001 | P1 forced memory vs document: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneBTMemory` | \ensuremath{-}4.59 | P1 Bradley-Terry ability of memory (log-odds, centred) |
| `\PoneBTMemoryLo` | \ensuremath{-}4.98 | P1 Bradley-Terry ability of memory (log-odds, centred), lower 95% CI bound |
| `\PoneBTMemoryHi` | \ensuremath{-}4.06 | P1 Bradley-Terry ability of memory (log-odds, centred), upper 95% CI bound |
| `\PoneBTMemoryCI` | [\ensuremath{-}4.98, \ensuremath{-}4.06] | P1 Bradley-Terry ability of memory (log-odds, centred), 95% CI |
| `\PoneBTMemoryN` | 47 | P1 Bradley-Terry ability of memory (log-odds, centred), n |
| `\PoneBTMemoryP` | n/a | P1 Bradley-Terry ability of memory (log-odds, centred), two-sided bootstrap p (n/a if not tested) |
| `\PoneBTTool` | 0.10 | P1 Bradley-Terry ability of tool (log-odds, centred) |
| `\PoneBTToolLo` | \ensuremath{-}0.98 | P1 Bradley-Terry ability of tool (log-odds, centred), lower 95% CI bound |
| `\PoneBTToolHi` | 0.89 | P1 Bradley-Terry ability of tool (log-odds, centred), upper 95% CI bound |
| `\PoneBTToolCI` | [\ensuremath{-}0.98, 0.89] | P1 Bradley-Terry ability of tool (log-odds, centred), 95% CI |
| `\PoneBTToolN` | 12 | P1 Bradley-Terry ability of tool (log-odds, centred), n |
| `\PoneBTToolP` | n/a | P1 Bradley-Terry ability of tool (log-odds, centred), two-sided bootstrap p (n/a if not tested) |
| `\PoneBTWeb` | \ensuremath{-}1.34 | P1 Bradley-Terry ability of web (log-odds, centred) |
| `\PoneBTWebLo` | \ensuremath{-}1.87 | P1 Bradley-Terry ability of web (log-odds, centred), lower 95% CI bound |
| `\PoneBTWebHi` | \ensuremath{-}0.22 | P1 Bradley-Terry ability of web (log-odds, centred), upper 95% CI bound |
| `\PoneBTWebCI` | [\ensuremath{-}1.87, \ensuremath{-}0.22] | P1 Bradley-Terry ability of web (log-odds, centred), 95% CI |
| `\PoneBTWebN` | 12 | P1 Bradley-Terry ability of web (log-odds, centred), n |
| `\PoneBTWebP` | n/a | P1 Bradley-Terry ability of web (log-odds, centred), two-sided bootstrap p (n/a if not tested) |
| `\PoneBTUser` | 2.83 | P1 Bradley-Terry ability of user (log-odds, centred) |
| `\PoneBTUserLo` | 1.38 | P1 Bradley-Terry ability of user (log-odds, centred), lower 95% CI bound |
| `\PoneBTUserHi` | 4.30 | P1 Bradley-Terry ability of user (log-odds, centred), upper 95% CI bound |
| `\PoneBTUserCI` | [1.38, 4.30] | P1 Bradley-Terry ability of user (log-odds, centred), 95% CI |
| `\PoneBTUserN` | 19 | P1 Bradley-Terry ability of user (log-odds, centred), n |
| `\PoneBTUserP` | n/a | P1 Bradley-Terry ability of user (log-odds, centred), two-sided bootstrap p (n/a if not tested) |
| `\PoneBTAgent` | 0.11 | P1 Bradley-Terry ability of agent (log-odds, centred) |
| `\PoneBTAgentLo` | \ensuremath{-}0.55 | P1 Bradley-Terry ability of agent (log-odds, centred), lower 95% CI bound |
| `\PoneBTAgentHi` | 0.56 | P1 Bradley-Terry ability of agent (log-odds, centred), upper 95% CI bound |
| `\PoneBTAgentCI` | [\ensuremath{-}0.55, 0.56] | P1 Bradley-Terry ability of agent (log-odds, centred), 95% CI |
| `\PoneBTAgentN` | 9 | P1 Bradley-Terry ability of agent (log-odds, centred), n |
| `\PoneBTAgentP` | n/a | P1 Bradley-Terry ability of agent (log-odds, centred), two-sided bootstrap p (n/a if not tested) |
| `\PoneBTUnattributed` | 0.51 | P1 Bradley-Terry ability of unattributed (log-odds, centred) |
| `\PoneBTUnattributedLo` | \ensuremath{-}0.61 | P1 Bradley-Terry ability of unattributed (log-odds, centred), lower 95% CI bound |
| `\PoneBTUnattributedHi` | 1.60 | P1 Bradley-Terry ability of unattributed (log-odds, centred), upper 95% CI bound |
| `\PoneBTUnattributedCI` | [\ensuremath{-}0.61, 1.60] | P1 Bradley-Terry ability of unattributed (log-odds, centred), 95% CI |
| `\PoneBTUnattributedN` | 10 | P1 Bradley-Terry ability of unattributed (log-odds, centred), n |
| `\PoneBTUnattributedP` | n/a | P1 Bradley-Terry ability of unattributed (log-odds, centred), two-sided bootstrap p (n/a if not tested) |
| `\PoneBTDocument` | 2.39 | P1 Bradley-Terry ability of document (log-odds, centred) |
| `\PoneBTDocumentLo` | 0.71 | P1 Bradley-Terry ability of document (log-odds, centred), lower 95% CI bound |
| `\PoneBTDocumentHi` | 3.82 | P1 Bradley-Terry ability of document (log-odds, centred), upper 95% CI bound |
| `\PoneBTDocumentCI` | [0.71, 3.82] | P1 Bradley-Terry ability of document (log-odds, centred), 95% CI |
| `\PoneBTDocumentN` | 17 | P1 Bradley-Terry ability of document (log-odds, centred), n |
| `\PoneBTDocumentP` | n/a | P1 Bradley-Terry ability of document (log-odds, centred), two-sided bootstrap p (n/a if not tested) |
| `\PoneFramingMemoryVsTool` | 11.1 | P1 framing: change in % following memory when framed first-person, vs tool (pp) |
| `\PoneFramingMemoryVsToolLo` | 0.0 | P1 framing: change in % following memory when framed first-person, vs tool (pp), lower 95% CI bound |
| `\PoneFramingMemoryVsToolHi` | 33.3 | P1 framing: change in % following memory when framed first-person, vs tool (pp), upper 95% CI bound |
| `\PoneFramingMemoryVsToolCI` | [0.0, 33.3] | P1 framing: change in % following memory when framed first-person, vs tool (pp), 95% CI |
| `\PoneFramingMemoryVsToolN` | 18 | P1 framing: change in % following memory when framed first-person, vs tool (pp), n |
| `\PoneFramingMemoryVsToolP` | 0.659 | P1 framing: change in % following memory when framed first-person, vs tool (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneFramingMemoryVsDocument` | 5.6 | P1 framing: change in % following memory when framed first-person, vs document (pp) |
| `\PoneFramingMemoryVsDocumentLo` | 0.0 | P1 framing: change in % following memory when framed first-person, vs document (pp), lower 95% CI bound |
| `\PoneFramingMemoryVsDocumentHi` | 16.7 | P1 framing: change in % following memory when framed first-person, vs document (pp), upper 95% CI bound |
| `\PoneFramingMemoryVsDocumentCI` | [0.0, 16.7] | P1 framing: change in % following memory when framed first-person, vs document (pp), 95% CI |
| `\PoneFramingMemoryVsDocumentN` | 18 | P1 framing: change in % following memory when framed first-person, vs document (pp), n |
| `\PoneFramingMemoryVsDocumentP` | 0.675 | P1 framing: change in % following memory when framed first-person, vs document (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneFramingUserVsTool` | 16.7 | P1 framing: change in % following user when framed first-person, vs tool (pp) |
| `\PoneFramingUserVsToolLo` | 5.6 | P1 framing: change in % following user when framed first-person, vs tool (pp), lower 95% CI bound |
| `\PoneFramingUserVsToolHi` | 33.3 | P1 framing: change in % following user when framed first-person, vs tool (pp), upper 95% CI bound |
| `\PoneFramingUserVsToolCI` | [5.6, 33.3] | P1 framing: change in % following user when framed first-person, vs tool (pp), 95% CI |
| `\PoneFramingUserVsToolN` | 18 | P1 framing: change in % following user when framed first-person, vs tool (pp), n |
| `\PoneFramingUserVsToolP` | 0.045 | P1 framing: change in % following user when framed first-person, vs tool (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneFramingUserVsDocument` | 16.7 | P1 framing: change in % following user when framed first-person, vs document (pp) |
| `\PoneFramingUserVsDocumentLo` | 0.0 | P1 framing: change in % following user when framed first-person, vs document (pp), lower 95% CI bound |
| `\PoneFramingUserVsDocumentHi` | 38.9 | P1 framing: change in % following user when framed first-person, vs document (pp), upper 95% CI bound |
| `\PoneFramingUserVsDocumentCI` | [0.0, 38.9] | P1 framing: change in % following user when framed first-person, vs document (pp), 95% CI |
| `\PoneFramingUserVsDocumentN` | 18 | P1 framing: change in % following user when framed first-person, vs document (pp), n |
| `\PoneFramingUserVsDocumentP` | 0.195 | P1 framing: change in % following user when framed first-person, vs document (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneFramingMemoryBoth` | 8.3 | P1 framing effect for memory, both trials pooled (pp) |
| `\PoneFramingMemoryBothLo` | 0.0 | P1 framing effect for memory, both trials pooled (pp), lower 95% CI bound |
| `\PoneFramingMemoryBothHi` | 25.0 | P1 framing effect for memory, both trials pooled (pp), upper 95% CI bound |
| `\PoneFramingMemoryBothCI` | [0.0, 25.0] | P1 framing effect for memory, both trials pooled (pp), 95% CI |
| `\PoneFramingMemoryBothN` | 36 | P1 framing effect for memory, both trials pooled (pp), n |
| `\PoneFramingMemoryBothP` | 0.693 | P1 framing effect for memory, both trials pooled (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneFramingUserBoth` | 16.7 | P1 framing effect for user, both trials pooled (pp) |
| `\PoneFramingUserBothLo` | 2.8 | P1 framing effect for user, both trials pooled (pp), lower 95% CI bound |
| `\PoneFramingUserBothHi` | 33.4 | P1 framing effect for user, both trials pooled (pp), upper 95% CI bound |
| `\PoneFramingUserBothCI` | [2.8, 33.4] | P1 framing effect for user, both trials pooled (pp), 95% CI |
| `\PoneFramingUserBothN` | 36 | P1 framing effect for user, both trials pooled (pp), n |
| `\PoneFramingUserBothP` | 0.015 | P1 framing effect for user, both trials pooled (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneTurnVsTool` | 0.0 | P1 turn - labelled memory: change in % following memory vs tool (pp) |
| `\PoneTurnVsToolLo` | 0.0 | P1 turn - labelled memory: change in % following memory vs tool (pp), lower 95% CI bound |
| `\PoneTurnVsToolHi` | 0.0 | P1 turn - labelled memory: change in % following memory vs tool (pp), upper 95% CI bound |
| `\PoneTurnVsToolCI` | [0.0, 0.0] | P1 turn - labelled memory: change in % following memory vs tool (pp), 95% CI |
| `\PoneTurnVsToolN` | 18 | P1 turn - labelled memory: change in % following memory vs tool (pp), n |
| `\PoneTurnVsToolP` | 1.000 | P1 turn - labelled memory: change in % following memory vs tool (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneTurnVsDocument` | 0.0 | P1 turn - labelled memory: change in % following memory vs document (pp) |
| `\PoneTurnVsDocumentLo` | 0.0 | P1 turn - labelled memory: change in % following memory vs document (pp), lower 95% CI bound |
| `\PoneTurnVsDocumentHi` | 0.0 | P1 turn - labelled memory: change in % following memory vs document (pp), upper 95% CI bound |
| `\PoneTurnVsDocumentCI` | [0.0, 0.0] | P1 turn - labelled memory: change in % following memory vs document (pp), 95% CI |
| `\PoneTurnVsDocumentN` | 18 | P1 turn - labelled memory: change in % following memory vs document (pp), n |
| `\PoneTurnVsDocumentP` | 1.000 | P1 turn - labelled memory: change in % following memory vs document (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemoryAdopt` | 100.0 | P1 single claim (no conflict) in memory: % adopted, pooled |
| `\PoneSingleMemoryAdoptLo` | 63.1 | P1 single claim (no conflict) in memory: % adopted, pooled, lower 95% CI bound |
| `\PoneSingleMemoryAdoptHi` | 100.0 | P1 single claim (no conflict) in memory: % adopted, pooled, upper 95% CI bound |
| `\PoneSingleMemoryAdoptCI` | [63.1, 100.0] | P1 single claim (no conflict) in memory: % adopted, pooled, 95% CI |
| `\PoneSingleMemoryAdoptN` | 8 | P1 single claim (no conflict) in memory: % adopted, pooled, n |
| `\PoneSingleMemoryAdoptP` | n/a | P1 single claim (no conflict) in memory: % adopted, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemoryAdoptDeepSeekVFourFlash` | 100.0 | P1 single claim (no conflict) in memory: % adopted, deepseek-v4-flash |
| `\PoneSingleMemoryAdoptDeepSeekVFourFlashLo` | 39.8 | P1 single claim (no conflict) in memory: % adopted, deepseek-v4-flash, lower 95% CI bound |
| `\PoneSingleMemoryAdoptDeepSeekVFourFlashHi` | 100.0 | P1 single claim (no conflict) in memory: % adopted, deepseek-v4-flash, upper 95% CI bound |
| `\PoneSingleMemoryAdoptDeepSeekVFourFlashCI` | [39.8, 100.0] | P1 single claim (no conflict) in memory: % adopted, deepseek-v4-flash, 95% CI |
| `\PoneSingleMemoryAdoptDeepSeekVFourFlashN` | 4 | P1 single claim (no conflict) in memory: % adopted, deepseek-v4-flash, n |
| `\PoneSingleMemoryAdoptDeepSeekVFourFlashP` | n/a | P1 single claim (no conflict) in memory: % adopted, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemoryAdoptGemmaFourThreeOneB` | 100.0 | P1 single claim (no conflict) in memory: % adopted, gemma-4-31b-it |
| `\PoneSingleMemoryAdoptGemmaFourThreeOneBLo` | 39.8 | P1 single claim (no conflict) in memory: % adopted, gemma-4-31b-it, lower 95% CI bound |
| `\PoneSingleMemoryAdoptGemmaFourThreeOneBHi` | 100.0 | P1 single claim (no conflict) in memory: % adopted, gemma-4-31b-it, upper 95% CI bound |
| `\PoneSingleMemoryAdoptGemmaFourThreeOneBCI` | [39.8, 100.0] | P1 single claim (no conflict) in memory: % adopted, gemma-4-31b-it, 95% CI |
| `\PoneSingleMemoryAdoptGemmaFourThreeOneBN` | 4 | P1 single claim (no conflict) in memory: % adopted, gemma-4-31b-it, n |
| `\PoneSingleMemoryAdoptGemmaFourThreeOneBP` | n/a | P1 single claim (no conflict) in memory: % adopted, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleToolAdopt` | 100.0 | P1 single claim (no conflict) in tool: % adopted, pooled |
| `\PoneSingleToolAdoptLo` | 63.1 | P1 single claim (no conflict) in tool: % adopted, pooled, lower 95% CI bound |
| `\PoneSingleToolAdoptHi` | 100.0 | P1 single claim (no conflict) in tool: % adopted, pooled, upper 95% CI bound |
| `\PoneSingleToolAdoptCI` | [63.1, 100.0] | P1 single claim (no conflict) in tool: % adopted, pooled, 95% CI |
| `\PoneSingleToolAdoptN` | 8 | P1 single claim (no conflict) in tool: % adopted, pooled, n |
| `\PoneSingleToolAdoptP` | n/a | P1 single claim (no conflict) in tool: % adopted, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleToolAdoptDeepSeekVFourFlash` | 100.0 | P1 single claim (no conflict) in tool: % adopted, deepseek-v4-flash |
| `\PoneSingleToolAdoptDeepSeekVFourFlashLo` | 39.8 | P1 single claim (no conflict) in tool: % adopted, deepseek-v4-flash, lower 95% CI bound |
| `\PoneSingleToolAdoptDeepSeekVFourFlashHi` | 100.0 | P1 single claim (no conflict) in tool: % adopted, deepseek-v4-flash, upper 95% CI bound |
| `\PoneSingleToolAdoptDeepSeekVFourFlashCI` | [39.8, 100.0] | P1 single claim (no conflict) in tool: % adopted, deepseek-v4-flash, 95% CI |
| `\PoneSingleToolAdoptDeepSeekVFourFlashN` | 4 | P1 single claim (no conflict) in tool: % adopted, deepseek-v4-flash, n |
| `\PoneSingleToolAdoptDeepSeekVFourFlashP` | n/a | P1 single claim (no conflict) in tool: % adopted, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleToolAdoptGemmaFourThreeOneB` | 100.0 | P1 single claim (no conflict) in tool: % adopted, gemma-4-31b-it |
| `\PoneSingleToolAdoptGemmaFourThreeOneBLo` | 39.8 | P1 single claim (no conflict) in tool: % adopted, gemma-4-31b-it, lower 95% CI bound |
| `\PoneSingleToolAdoptGemmaFourThreeOneBHi` | 100.0 | P1 single claim (no conflict) in tool: % adopted, gemma-4-31b-it, upper 95% CI bound |
| `\PoneSingleToolAdoptGemmaFourThreeOneBCI` | [39.8, 100.0] | P1 single claim (no conflict) in tool: % adopted, gemma-4-31b-it, 95% CI |
| `\PoneSingleToolAdoptGemmaFourThreeOneBN` | 4 | P1 single claim (no conflict) in tool: % adopted, gemma-4-31b-it, n |
| `\PoneSingleToolAdoptGemmaFourThreeOneBP` | n/a | P1 single claim (no conflict) in tool: % adopted, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemMinusTool` | 0.0 | P1 single claim: adoption memory - tool (pp), pooled |
| `\PoneSingleMemMinusToolLo` | 0.0 | P1 single claim: adoption memory - tool (pp), pooled, lower 95% CI bound |
| `\PoneSingleMemMinusToolHi` | 0.0 | P1 single claim: adoption memory - tool (pp), pooled, upper 95% CI bound |
| `\PoneSingleMemMinusToolCI` | [0.0, 0.0] | P1 single claim: adoption memory - tool (pp), pooled, 95% CI |
| `\PoneSingleMemMinusToolN` | 8 | P1 single claim: adoption memory - tool (pp), pooled, n |
| `\PoneSingleMemMinusToolP` | 1.000 | P1 single claim: adoption memory - tool (pp), pooled, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemMinusToolDeepSeekVFourFlash` | 0.0 | P1 single claim: adoption memory - tool (pp), deepseek-v4-flash |
| `\PoneSingleMemMinusToolDeepSeekVFourFlashLo` | 0.0 | P1 single claim: adoption memory - tool (pp), deepseek-v4-flash, lower 95% CI bound |
| `\PoneSingleMemMinusToolDeepSeekVFourFlashHi` | 0.0 | P1 single claim: adoption memory - tool (pp), deepseek-v4-flash, upper 95% CI bound |
| `\PoneSingleMemMinusToolDeepSeekVFourFlashCI` | [0.0, 0.0] | P1 single claim: adoption memory - tool (pp), deepseek-v4-flash, 95% CI |
| `\PoneSingleMemMinusToolDeepSeekVFourFlashN` | 4 | P1 single claim: adoption memory - tool (pp), deepseek-v4-flash, n |
| `\PoneSingleMemMinusToolDeepSeekVFourFlashP` | 1.000 | P1 single claim: adoption memory - tool (pp), deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemMinusToolGemmaFourThreeOneB` | 0.0 | P1 single claim: adoption memory - tool (pp), gemma-4-31b-it |
| `\PoneSingleMemMinusToolGemmaFourThreeOneBLo` | 0.0 | P1 single claim: adoption memory - tool (pp), gemma-4-31b-it, lower 95% CI bound |
| `\PoneSingleMemMinusToolGemmaFourThreeOneBHi` | 0.0 | P1 single claim: adoption memory - tool (pp), gemma-4-31b-it, upper 95% CI bound |
| `\PoneSingleMemMinusToolGemmaFourThreeOneBCI` | [0.0, 0.0] | P1 single claim: adoption memory - tool (pp), gemma-4-31b-it, 95% CI |
| `\PoneSingleMemMinusToolGemmaFourThreeOneBN` | 4 | P1 single claim: adoption memory - tool (pp), gemma-4-31b-it, n |
| `\PoneSingleMemMinusToolGemmaFourThreeOneBP` | 1.000 | P1 single claim: adoption memory - tool (pp), gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PonePositionFirst` | 57.8 | P1 % following the first-shown claim (side chosen) |
| `\PonePositionFirstLo` | 47.2 | P1 % following the first-shown claim (side chosen), lower 95% CI bound |
| `\PonePositionFirstHi` | 66.7 | P1 % following the first-shown claim (side chosen), upper 95% CI bound |
| `\PonePositionFirstCI` | [47.2, 66.7] | P1 % following the first-shown claim (side chosen), 95% CI |
| `\PonePositionFirstN` | 147 | P1 % following the first-shown claim (side chosen), n |
| `\PonePositionFirstP` | 0.169 | P1 % following the first-shown claim (side chosen), two-sided bootstrap p (n/a if not tested) |
| `\PoneEscPair` | 64.4 | P1 % flags conflict, design pair |
| `\PoneEscPairLo` | 47.2 | P1 % flags conflict, design pair, lower 95% CI bound |
| `\PoneEscPairHi` | 78.9 | P1 % flags conflict, design pair, upper 95% CI bound |
| `\PoneEscPairCI` | [47.2, 78.9] | P1 % flags conflict, design pair, 95% CI |
| `\PoneEscPairN` | 180 | P1 % flags conflict, design pair, n |
| `\PoneEscPairP` | n/a | P1 % flags conflict, design pair, two-sided bootstrap p (n/a if not tested) |
| `\PoneConfPair` | 95.1 | P1 mean stated confidence, design pair |
| `\PoneConfPairLo` | 94.7 | P1 mean stated confidence, design pair, lower 95% CI bound |
| `\PoneConfPairHi` | 95.5 | P1 mean stated confidence, design pair, upper 95% CI bound |
| `\PoneConfPairCI` | [94.7, 95.5] | P1 mean stated confidence, design pair, 95% CI |
| `\PoneConfPairN` | 179 | P1 mean stated confidence, design pair, n |
| `\PoneConfPairP` | n/a | P1 mean stated confidence, design pair, two-sided bootstrap p (n/a if not tested) |
| `\PoneEscFraming` | 56.9 | P1 % flags conflict, design framing |
| `\PoneEscFramingLo` | 36.1 | P1 % flags conflict, design framing, lower 95% CI bound |
| `\PoneEscFramingHi` | 77.8 | P1 % flags conflict, design framing, upper 95% CI bound |
| `\PoneEscFramingCI` | [36.1, 77.8] | P1 % flags conflict, design framing, 95% CI |
| `\PoneEscFramingN` | 72 | P1 % flags conflict, design framing, n |
| `\PoneEscFramingP` | n/a | P1 % flags conflict, design framing, two-sided bootstrap p (n/a if not tested) |
| `\PoneConfFraming` | 94.3 | P1 mean stated confidence, design framing |
| `\PoneConfFramingLo` | 93.5 | P1 mean stated confidence, design framing, lower 95% CI bound |
| `\PoneConfFramingHi` | 95.1 | P1 mean stated confidence, design framing, upper 95% CI bound |
| `\PoneConfFramingCI` | [93.5, 95.1] | P1 mean stated confidence, design framing, 95% CI |
| `\PoneConfFramingN` | 71 | P1 mean stated confidence, design framing, n |
| `\PoneConfFramingP` | n/a | P1 mean stated confidence, design framing, two-sided bootstrap p (n/a if not tested) |
| `\PoneEscTurn` | 36.1 | P1 % flags conflict, design turn |
| `\PoneEscTurnLo` | 19.4 | P1 % flags conflict, design turn, lower 95% CI bound |
| `\PoneEscTurnHi` | 50.0 | P1 % flags conflict, design turn, upper 95% CI bound |
| `\PoneEscTurnCI` | [19.4, 50.0] | P1 % flags conflict, design turn, 95% CI |
| `\PoneEscTurnN` | 36 | P1 % flags conflict, design turn, n |
| `\PoneEscTurnP` | n/a | P1 % flags conflict, design turn, two-sided bootstrap p (n/a if not tested) |
| `\PoneConfTurn` | 97.7 | P1 mean stated confidence, design turn |
| `\PoneConfTurnLo` | 97.2 | P1 mean stated confidence, design turn, lower 95% CI bound |
| `\PoneConfTurnHi` | 98.1 | P1 mean stated confidence, design turn, upper 95% CI bound |
| `\PoneConfTurnCI` | [97.2, 98.1] | P1 mean stated confidence, design turn, 95% CI |
| `\PoneConfTurnN` | 35 | P1 mean stated confidence, design turn, n |
| `\PoneConfTurnP` | n/a | P1 mean stated confidence, design turn, two-sided bootstrap p (n/a if not tested) |
| `\PoneEscForced` | 0.0 | P1 % flags conflict, design forced |
| `\PoneEscForcedLo` | 0.0 | P1 % flags conflict, design forced, lower 95% CI bound |
| `\PoneEscForcedHi` | 6.6 | P1 % flags conflict, design forced, upper 95% CI bound |
| `\PoneEscForcedCI` | [0.0, 6.6] | P1 % flags conflict, design forced, 95% CI |
| `\PoneEscForcedN` | 54 | P1 % flags conflict, design forced, n |
| `\PoneEscForcedP` | n/a | P1 % flags conflict, design forced, two-sided bootstrap p (n/a if not tested) |
| `\PoneConfForced` | 96.7 | P1 mean stated confidence, design forced |
| `\PoneConfForcedLo` | 96.1 | P1 mean stated confidence, design forced, lower 95% CI bound |
| `\PoneConfForcedHi` | 97.1 | P1 mean stated confidence, design forced, upper 95% CI bound |
| `\PoneConfForcedCI` | [96.1, 97.1] | P1 mean stated confidence, design forced, 95% CI |
| `\PoneConfForcedN` | 54 | P1 mean stated confidence, design forced, n |
| `\PoneConfForcedP` | n/a | P1 mean stated confidence, design forced, two-sided bootstrap p (n/a if not tested) |
| `\PoneEscSingle` | 0.0 | P1 % flags conflict, design single |
| `\PoneEscSingleLo` | 0.0 | P1 % flags conflict, design single, lower 95% CI bound |
| `\PoneEscSingleHi` | 20.6 | P1 % flags conflict, design single, upper 95% CI bound |
| `\PoneEscSingleCI` | [0.0, 20.6] | P1 % flags conflict, design single, 95% CI |
| `\PoneEscSingleN` | 16 | P1 % flags conflict, design single, n |
| `\PoneEscSingleP` | n/a | P1 % flags conflict, design single, two-sided bootstrap p (n/a if not tested) |
| `\PoneConfSingle` | 98.4 | P1 mean stated confidence, design single |
| `\PoneConfSingleLo` | 97.8 | P1 mean stated confidence, design single, lower 95% CI bound |
| `\PoneConfSingleHi` | 98.8 | P1 mean stated confidence, design single, upper 95% CI bound |
| `\PoneConfSingleCI` | [97.8, 98.8] | P1 mean stated confidence, design single, 95% CI |
| `\PoneConfSingleN` | 16 | P1 mean stated confidence, design single, n |
| `\PoneConfSingleP` | n/a | P1 mean stated confidence, design single, two-sided bootstrap p (n/a if not tested) |
| `\LaundConfidence` | \ensuremath{-}1.7 | confidence laundering, stated confidence (0-100 points) |
| `\LaundConfidenceLo` | \ensuremath{-}6.4 | confidence laundering, stated confidence (0-100 points), lower 95% CI bound |
| `\LaundConfidenceHi` | 2.2 | confidence laundering, stated confidence (0-100 points), upper 95% CI bound |
| `\LaundConfidenceCI` | [\ensuremath{-}6.4, 2.2] | confidence laundering, stated confidence (0-100 points), 95% CI |
| `\LaundConfidenceN` | 143 | confidence laundering, stated confidence (0-100 points), n |
| `\LaundConfidenceP` | 0.421 | confidence laundering, stated confidence (0-100 points), two-sided bootstrap p (n/a if not tested) |
| `\LaundConfidenceEffectMemory` | 66.5 | certain - hedged, memory, stated confidence (0-100 points) |
| `\LaundConfidenceEffectMemoryLo` | 59.0 | certain - hedged, memory, stated confidence (0-100 points), lower 95% CI bound |
| `\LaundConfidenceEffectMemoryHi` | 73.3 | certain - hedged, memory, stated confidence (0-100 points), upper 95% CI bound |
| `\LaundConfidenceEffectMemoryCI` | [59.0, 73.3] | certain - hedged, memory, stated confidence (0-100 points), 95% CI |
| `\LaundConfidenceEffectMemoryN` | 143 | certain - hedged, memory, stated confidence (0-100 points), n |
| `\LaundConfidenceEffectMemoryP` | \ensuremath{<}0.001 | certain - hedged, memory, stated confidence (0-100 points), two-sided bootstrap p (n/a if not tested) |
| `\LaundConfidenceEffectTool` | 68.2 | certain - hedged, tool, stated confidence (0-100 points) |
| `\LaundConfidenceEffectToolLo` | 61.5 | certain - hedged, tool, stated confidence (0-100 points), lower 95% CI bound |
| `\LaundConfidenceEffectToolHi` | 74.1 | certain - hedged, tool, stated confidence (0-100 points), upper 95% CI bound |
| `\LaundConfidenceEffectToolCI` | [61.5, 74.1] | certain - hedged, tool, stated confidence (0-100 points), 95% CI |
| `\LaundConfidenceEffectToolN` | 143 | certain - hedged, tool, stated confidence (0-100 points), n |
| `\LaundConfidenceEffectToolP` | \ensuremath{<}0.001 | certain - hedged, tool, stated confidence (0-100 points), two-sided bootstrap p (n/a if not tested) |
| `\LaundConfidenceMemoryHedged` | 31.4 | confidence mean, memory_hedged |
| `\LaundConfidenceMemoryHedgedLo` | 24.6 | confidence mean, memory_hedged, lower 95% CI bound |
| `\LaundConfidenceMemoryHedgedHi` | 39.0 | confidence mean, memory_hedged, upper 95% CI bound |
| `\LaundConfidenceMemoryHedgedCI` | [24.6, 39.0] | confidence mean, memory_hedged, 95% CI |
| `\LaundConfidenceMemoryHedgedN` | 36 | confidence mean, memory_hedged, n |
| `\LaundConfidenceMemoryHedgedP` | n/a | confidence mean, memory_hedged, two-sided bootstrap p (n/a if not tested) |
| `\LaundConfidenceMemoryCertain` | 97.9 | confidence mean, memory_certain |
| `\LaundConfidenceMemoryCertainLo` | 97.5 | confidence mean, memory_certain, lower 95% CI bound |
| `\LaundConfidenceMemoryCertainHi` | 98.3 | confidence mean, memory_certain, upper 95% CI bound |
| `\LaundConfidenceMemoryCertainCI` | [97.5, 98.3] | confidence mean, memory_certain, 95% CI |
| `\LaundConfidenceMemoryCertainN` | 36 | confidence mean, memory_certain, n |
| `\LaundConfidenceMemoryCertainP` | n/a | confidence mean, memory_certain, two-sided bootstrap p (n/a if not tested) |
| `\LaundConfidenceToolHedged` | 30.0 | confidence mean, tool_hedged |
| `\LaundConfidenceToolHedgedLo` | 23.9 | confidence mean, tool_hedged, lower 95% CI bound |
| `\LaundConfidenceToolHedgedHi` | 36.9 | confidence mean, tool_hedged, upper 95% CI bound |
| `\LaundConfidenceToolHedgedCI` | [23.9, 36.9] | confidence mean, tool_hedged, 95% CI |
| `\LaundConfidenceToolHedgedN` | 35 | confidence mean, tool_hedged, n |
| `\LaundConfidenceToolHedgedP` | n/a | confidence mean, tool_hedged, two-sided bootstrap p (n/a if not tested) |
| `\LaundConfidenceToolCertain` | 98.2 | confidence mean, tool_certain |
| `\LaundConfidenceToolCertainLo` | 97.8 | confidence mean, tool_certain, lower 95% CI bound |
| `\LaundConfidenceToolCertainHi` | 98.7 | confidence mean, tool_certain, upper 95% CI bound |
| `\LaundConfidenceToolCertainCI` | [97.8, 98.7] | confidence mean, tool_certain, 95% CI |
| `\LaundConfidenceToolCertainN` | 36 | confidence mean, tool_certain, n |
| `\LaundConfidenceToolCertainP` | n/a | confidence mean, tool_certain, two-sided bootstrap p (n/a if not tested) |
| `\LaundAct` | \ensuremath{-}2.8 | confidence laundering, act rate (pp) |
| `\LaundActLo` | \ensuremath{-}13.9 | confidence laundering, act rate (pp), lower 95% CI bound |
| `\LaundActHi` | 5.6 | confidence laundering, act rate (pp), upper 95% CI bound |
| `\LaundActCI` | [\ensuremath{-}13.9, 5.6] | confidence laundering, act rate (pp), 95% CI |
| `\LaundActN` | 143 | confidence laundering, act rate (pp), n |
| `\LaundActP` | 0.788 | confidence laundering, act rate (pp), two-sided bootstrap p (n/a if not tested) |
| `\LaundActEffectMemory` | 94.4 | certain - hedged, memory, act rate (pp) |
| `\LaundActEffectMemoryLo` | 86.1 | certain - hedged, memory, act rate (pp), lower 95% CI bound |
| `\LaundActEffectMemoryHi` | 100.0 | certain - hedged, memory, act rate (pp), upper 95% CI bound |
| `\LaundActEffectMemoryCI` | [86.1, 100.0] | certain - hedged, memory, act rate (pp), 95% CI |
| `\LaundActEffectMemoryN` | 143 | certain - hedged, memory, act rate (pp), n |
| `\LaundActEffectMemoryP` | \ensuremath{<}0.001 | certain - hedged, memory, act rate (pp), two-sided bootstrap p (n/a if not tested) |
| `\LaundActEffectTool` | 97.2 | certain - hedged, tool, act rate (pp) |
| `\LaundActEffectToolLo` | 91.7 | certain - hedged, tool, act rate (pp), lower 95% CI bound |
| `\LaundActEffectToolHi` | 100.0 | certain - hedged, tool, act rate (pp), upper 95% CI bound |
| `\LaundActEffectToolCI` | [91.7, 100.0] | certain - hedged, tool, act rate (pp), 95% CI |
| `\LaundActEffectToolN` | 143 | certain - hedged, tool, act rate (pp), n |
| `\LaundActEffectToolP` | \ensuremath{<}0.001 | certain - hedged, tool, act rate (pp), two-sided bootstrap p (n/a if not tested) |
| `\LaundActMemoryHedged` | 0.0 | act mean, memory_hedged |
| `\LaundActMemoryHedgedLo` | 0.0 | act mean, memory_hedged, lower 95% CI bound |
| `\LaundActMemoryHedgedHi` | 0.0 | act mean, memory_hedged, upper 95% CI bound |
| `\LaundActMemoryHedgedCI` | [0.0, 0.0] | act mean, memory_hedged, 95% CI |
| `\LaundActMemoryHedgedN` | 36 | act mean, memory_hedged, n |
| `\LaundActMemoryHedgedP` | n/a | act mean, memory_hedged, two-sided bootstrap p (n/a if not tested) |
| `\LaundActMemoryCertain` | 94.4 | act mean, memory_certain |
| `\LaundActMemoryCertainLo` | 86.1 | act mean, memory_certain, lower 95% CI bound |
| `\LaundActMemoryCertainHi` | 100.0 | act mean, memory_certain, upper 95% CI bound |
| `\LaundActMemoryCertainCI` | [86.1, 100.0] | act mean, memory_certain, 95% CI |
| `\LaundActMemoryCertainN` | 36 | act mean, memory_certain, n |
| `\LaundActMemoryCertainP` | n/a | act mean, memory_certain, two-sided bootstrap p (n/a if not tested) |
| `\LaundActToolHedged` | 0.0 | act mean, tool_hedged |
| `\LaundActToolHedgedLo` | 0.0 | act mean, tool_hedged, lower 95% CI bound |
| `\LaundActToolHedgedHi` | 0.0 | act mean, tool_hedged, upper 95% CI bound |
| `\LaundActToolHedgedCI` | [0.0, 0.0] | act mean, tool_hedged, 95% CI |
| `\LaundActToolHedgedN` | 35 | act mean, tool_hedged, n |
| `\LaundActToolHedgedP` | n/a | act mean, tool_hedged, two-sided bootstrap p (n/a if not tested) |
| `\LaundActToolCertain` | 97.2 | act mean, tool_certain |
| `\LaundActToolCertainLo` | 91.7 | act mean, tool_certain, lower 95% CI bound |
| `\LaundActToolCertainHi` | 100.0 | act mean, tool_certain, upper 95% CI bound |
| `\LaundActToolCertainCI` | [91.7, 100.0] | act mean, tool_certain, 95% CI |
| `\LaundActToolCertainN` | 36 | act mean, tool_certain, n |
| `\LaundActToolCertainP` | n/a | act mean, tool_certain, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTZeroNegAll` | 0.93 | mean AUROC over hosted victims, C T0, negatives all_clean |
| `\DetMeanCTZeroNegAllLo` | 0.89 | mean AUROC over hosted victims, C T0, negatives all_clean, lower 95% CI bound |
| `\DetMeanCTZeroNegAllHi` | 0.97 | mean AUROC over hosted victims, C T0, negatives all_clean, upper 95% CI bound |
| `\DetMeanCTZeroNegAllCI` | [0.89, 0.97] | mean AUROC over hosted victims, C T0, negatives all_clean, 95% CI |
| `\DetMeanCTZeroNegAllN` | 132 | mean AUROC over hosted victims, C T0, negatives all_clean, n |
| `\DetMeanCTZeroNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T0, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTZeroNegAttacked` | 0.92 | mean AUROC over hosted victims, C T0, negatives in_attacked |
| `\DetMeanCTZeroNegAttackedLo` | 0.88 | mean AUROC over hosted victims, C T0, negatives in_attacked, lower 95% CI bound |
| `\DetMeanCTZeroNegAttackedHi` | 0.96 | mean AUROC over hosted victims, C T0, negatives in_attacked, upper 95% CI bound |
| `\DetMeanCTZeroNegAttackedCI` | [0.88, 0.96] | mean AUROC over hosted victims, C T0, negatives in_attacked, 95% CI |
| `\DetMeanCTZeroNegAttackedN` | 385 | mean AUROC over hosted victims, C T0, negatives in_attacked, n |
| `\DetMeanCTZeroNegAttackedP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T0, negatives in_attacked, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTZero` | 0.93 | mean AUROC over hosted victims, C T0, negatives same_slot |
| `\DetMeanCTZeroLo` | 0.89 | mean AUROC over hosted victims, C T0, negatives same_slot, lower 95% CI bound |
| `\DetMeanCTZeroHi` | 0.97 | mean AUROC over hosted victims, C T0, negatives same_slot, upper 95% CI bound |
| `\DetMeanCTZeroCI` | [0.89, 0.97] | mean AUROC over hosted victims, C T0, negatives same_slot, 95% CI |
| `\DetMeanCTZeroN` | 110 | mean AUROC over hosted victims, C T0, negatives same_slot, n |
| `\DetMeanCTZeroP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T0, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTOneNegAll` | 0.94 | mean AUROC over hosted victims, C T1, negatives all_clean |
| `\DetMeanCTOneNegAllLo` | 0.88 | mean AUROC over hosted victims, C T1, negatives all_clean, lower 95% CI bound |
| `\DetMeanCTOneNegAllHi` | 1.00 | mean AUROC over hosted victims, C T1, negatives all_clean, upper 95% CI bound |
| `\DetMeanCTOneNegAllCI` | [0.88, 1.00] | mean AUROC over hosted victims, C T1, negatives all_clean, 95% CI |
| `\DetMeanCTOneNegAllN` | 127 | mean AUROC over hosted victims, C T1, negatives all_clean, n |
| `\DetMeanCTOneNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T1, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTOneNegAttacked` | 0.94 | mean AUROC over hosted victims, C T1, negatives in_attacked |
| `\DetMeanCTOneNegAttackedLo` | 0.88 | mean AUROC over hosted victims, C T1, negatives in_attacked, lower 95% CI bound |
| `\DetMeanCTOneNegAttackedHi` | 1.00 | mean AUROC over hosted victims, C T1, negatives in_attacked, upper 95% CI bound |
| `\DetMeanCTOneNegAttackedCI` | [0.88, 1.00] | mean AUROC over hosted victims, C T1, negatives in_attacked, 95% CI |
| `\DetMeanCTOneNegAttackedN` | 350 | mean AUROC over hosted victims, C T1, negatives in_attacked, n |
| `\DetMeanCTOneNegAttackedP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T1, negatives in_attacked, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTOne` | 0.94 | mean AUROC over hosted victims, C T1, negatives same_slot |
| `\DetMeanCTOneLo` | 0.88 | mean AUROC over hosted victims, C T1, negatives same_slot, lower 95% CI bound |
| `\DetMeanCTOneHi` | 1.00 | mean AUROC over hosted victims, C T1, negatives same_slot, upper 95% CI bound |
| `\DetMeanCTOneCI` | [0.88, 1.00] | mean AUROC over hosted victims, C T1, negatives same_slot, 95% CI |
| `\DetMeanCTOneN` | 100 | mean AUROC over hosted victims, C T1, negatives same_slot, n |
| `\DetMeanCTOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T1, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTTwoNegAll` | 0.96 | mean AUROC over hosted victims, C T2, negatives all_clean |
| `\DetMeanCTTwoNegAllLo` | 0.90 | mean AUROC over hosted victims, C T2, negatives all_clean, lower 95% CI bound |
| `\DetMeanCTTwoNegAllHi` | 1.00 | mean AUROC over hosted victims, C T2, negatives all_clean, upper 95% CI bound |
| `\DetMeanCTTwoNegAllCI` | [0.90, 1.00] | mean AUROC over hosted victims, C T2, negatives all_clean, 95% CI |
| `\DetMeanCTTwoNegAllN` | 131 | mean AUROC over hosted victims, C T2, negatives all_clean, n |
| `\DetMeanCTTwoNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T2, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTTwoNegAttacked` | 0.95 | mean AUROC over hosted victims, C T2, negatives in_attacked |
| `\DetMeanCTTwoNegAttackedLo` | 0.90 | mean AUROC over hosted victims, C T2, negatives in_attacked, lower 95% CI bound |
| `\DetMeanCTTwoNegAttackedHi` | 0.99 | mean AUROC over hosted victims, C T2, negatives in_attacked, upper 95% CI bound |
| `\DetMeanCTTwoNegAttackedCI` | [0.90, 0.99] | mean AUROC over hosted victims, C T2, negatives in_attacked, 95% CI |
| `\DetMeanCTTwoNegAttackedN` | 378 | mean AUROC over hosted victims, C T2, negatives in_attacked, n |
| `\DetMeanCTTwoNegAttackedP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T2, negatives in_attacked, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTTwo` | 0.96 | mean AUROC over hosted victims, C T2, negatives same_slot |
| `\DetMeanCTTwoLo` | 0.90 | mean AUROC over hosted victims, C T2, negatives same_slot, lower 95% CI bound |
| `\DetMeanCTTwoHi` | 1.00 | mean AUROC over hosted victims, C T2, negatives same_slot, upper 95% CI bound |
| `\DetMeanCTTwoCI` | [0.90, 1.00] | mean AUROC over hosted victims, C T2, negatives same_slot, 95% CI |
| `\DetMeanCTTwoN` | 108 | mean AUROC over hosted victims, C T2, negatives same_slot, n |
| `\DetMeanCTTwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T2, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTThreeNegAll` | 0.94 | mean AUROC over hosted victims, C T3, negatives all_clean |
| `\DetMeanCTThreeNegAllLo` | 0.89 | mean AUROC over hosted victims, C T3, negatives all_clean, lower 95% CI bound |
| `\DetMeanCTThreeNegAllHi` | 0.99 | mean AUROC over hosted victims, C T3, negatives all_clean, upper 95% CI bound |
| `\DetMeanCTThreeNegAllCI` | [0.89, 0.99] | mean AUROC over hosted victims, C T3, negatives all_clean, 95% CI |
| `\DetMeanCTThreeNegAllN` | 129 | mean AUROC over hosted victims, C T3, negatives all_clean, n |
| `\DetMeanCTThreeNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T3, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTThreeNegAttacked` | 0.94 | mean AUROC over hosted victims, C T3, negatives in_attacked |
| `\DetMeanCTThreeNegAttackedLo` | 0.88 | mean AUROC over hosted victims, C T3, negatives in_attacked, lower 95% CI bound |
| `\DetMeanCTThreeNegAttackedHi` | 0.99 | mean AUROC over hosted victims, C T3, negatives in_attacked, upper 95% CI bound |
| `\DetMeanCTThreeNegAttackedCI` | [0.88, 0.99] | mean AUROC over hosted victims, C T3, negatives in_attacked, 95% CI |
| `\DetMeanCTThreeNegAttackedN` | 364 | mean AUROC over hosted victims, C T3, negatives in_attacked, n |
| `\DetMeanCTThreeNegAttackedP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T3, negatives in_attacked, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTThree` | 0.94 | mean AUROC over hosted victims, C T3, negatives same_slot |
| `\DetMeanCTThreeLo` | 0.89 | mean AUROC over hosted victims, C T3, negatives same_slot, lower 95% CI bound |
| `\DetMeanCTThreeHi` | 0.99 | mean AUROC over hosted victims, C T3, negatives same_slot, upper 95% CI bound |
| `\DetMeanCTThreeCI` | [0.89, 0.99] | mean AUROC over hosted victims, C T3, negatives same_slot, 95% CI |
| `\DetMeanCTThreeN` | 104 | mean AUROC over hosted victims, C T3, negatives same_slot, n |
| `\DetMeanCTThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T3, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRTZeroNegAll` | 0.87 | mean AUROC over hosted victims, R T0, negatives all_clean |
| `\DetMeanRTZeroNegAllLo` | 0.83 | mean AUROC over hosted victims, R T0, negatives all_clean, lower 95% CI bound |
| `\DetMeanRTZeroNegAllHi` | 0.90 | mean AUROC over hosted victims, R T0, negatives all_clean, upper 95% CI bound |
| `\DetMeanRTZeroNegAllCI` | [0.83, 0.90] | mean AUROC over hosted victims, R T0, negatives all_clean, 95% CI |
| `\DetMeanRTZeroNegAllN` | 142 | mean AUROC over hosted victims, R T0, negatives all_clean, n |
| `\DetMeanRTZeroNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T0, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRTZero` | 0.86 | mean AUROC over hosted victims, R T0, negatives same_slot |
| `\DetMeanRTZeroLo` | 0.83 | mean AUROC over hosted victims, R T0, negatives same_slot, lower 95% CI bound |
| `\DetMeanRTZeroHi` | 0.88 | mean AUROC over hosted victims, R T0, negatives same_slot, upper 95% CI bound |
| `\DetMeanRTZeroCI` | [0.83, 0.88] | mean AUROC over hosted victims, R T0, negatives same_slot, 95% CI |
| `\DetMeanRTZeroN` | 118 | mean AUROC over hosted victims, R T0, negatives same_slot, n |
| `\DetMeanRTZeroP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T0, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRTOneNegAll` | 0.87 | mean AUROC over hosted victims, R T1, negatives all_clean |
| `\DetMeanRTOneNegAllLo` | 0.83 | mean AUROC over hosted victims, R T1, negatives all_clean, lower 95% CI bound |
| `\DetMeanRTOneNegAllHi` | 0.90 | mean AUROC over hosted victims, R T1, negatives all_clean, upper 95% CI bound |
| `\DetMeanRTOneNegAllCI` | [0.83, 0.90] | mean AUROC over hosted victims, R T1, negatives all_clean, 95% CI |
| `\DetMeanRTOneNegAllN` | 137 | mean AUROC over hosted victims, R T1, negatives all_clean, n |
| `\DetMeanRTOneNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T1, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRTOne` | 0.86 | mean AUROC over hosted victims, R T1, negatives same_slot |
| `\DetMeanRTOneLo` | 0.82 | mean AUROC over hosted victims, R T1, negatives same_slot, lower 95% CI bound |
| `\DetMeanRTOneHi` | 0.89 | mean AUROC over hosted victims, R T1, negatives same_slot, upper 95% CI bound |
| `\DetMeanRTOneCI` | [0.82, 0.89] | mean AUROC over hosted victims, R T1, negatives same_slot, 95% CI |
| `\DetMeanRTOneN` | 108 | mean AUROC over hosted victims, R T1, negatives same_slot, n |
| `\DetMeanRTOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T1, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRTTwoNegAll` | 0.87 | mean AUROC over hosted victims, R T2, negatives all_clean |
| `\DetMeanRTTwoNegAllLo` | 0.83 | mean AUROC over hosted victims, R T2, negatives all_clean, lower 95% CI bound |
| `\DetMeanRTTwoNegAllHi` | 0.90 | mean AUROC over hosted victims, R T2, negatives all_clean, upper 95% CI bound |
| `\DetMeanRTTwoNegAllCI` | [0.83, 0.90] | mean AUROC over hosted victims, R T2, negatives all_clean, 95% CI |
| `\DetMeanRTTwoNegAllN` | 141 | mean AUROC over hosted victims, R T2, negatives all_clean, n |
| `\DetMeanRTTwoNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T2, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRTTwo` | 0.86 | mean AUROC over hosted victims, R T2, negatives same_slot |
| `\DetMeanRTTwoLo` | 0.83 | mean AUROC over hosted victims, R T2, negatives same_slot, lower 95% CI bound |
| `\DetMeanRTTwoHi` | 0.88 | mean AUROC over hosted victims, R T2, negatives same_slot, upper 95% CI bound |
| `\DetMeanRTTwoCI` | [0.83, 0.88] | mean AUROC over hosted victims, R T2, negatives same_slot, 95% CI |
| `\DetMeanRTTwoN` | 116 | mean AUROC over hosted victims, R T2, negatives same_slot, n |
| `\DetMeanRTTwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T2, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRTThreeNegAll` | 0.87 | mean AUROC over hosted victims, R T3, negatives all_clean |
| `\DetMeanRTThreeNegAllLo` | 0.83 | mean AUROC over hosted victims, R T3, negatives all_clean, lower 95% CI bound |
| `\DetMeanRTThreeNegAllHi` | 0.90 | mean AUROC over hosted victims, R T3, negatives all_clean, upper 95% CI bound |
| `\DetMeanRTThreeNegAllCI` | [0.83, 0.90] | mean AUROC over hosted victims, R T3, negatives all_clean, 95% CI |
| `\DetMeanRTThreeNegAllN` | 139 | mean AUROC over hosted victims, R T3, negatives all_clean, n |
| `\DetMeanRTThreeNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T3, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRTThree` | 0.85 | mean AUROC over hosted victims, R T3, negatives same_slot |
| `\DetMeanRTThreeLo` | 0.82 | mean AUROC over hosted victims, R T3, negatives same_slot, lower 95% CI bound |
| `\DetMeanRTThreeHi` | 0.88 | mean AUROC over hosted victims, R T3, negatives same_slot, upper 95% CI bound |
| `\DetMeanRTThreeCI` | [0.82, 0.88] | mean AUROC over hosted victims, R T3, negatives same_slot, 95% CI |
| `\DetMeanRTThreeN` | 112 | mean AUROC over hosted victims, R T3, negatives same_slot, n |
| `\DetMeanRTThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T3, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTZeroNegAll` | 0.60 | mean AUROC over hosted victims, V T0, negatives all_clean |
| `\DetMeanVTZeroNegAllLo` | 0.54 | mean AUROC over hosted victims, V T0, negatives all_clean, lower 95% CI bound |
| `\DetMeanVTZeroNegAllHi` | 0.70 | mean AUROC over hosted victims, V T0, negatives all_clean, upper 95% CI bound |
| `\DetMeanVTZeroNegAllCI` | [0.54, 0.70] | mean AUROC over hosted victims, V T0, negatives all_clean, 95% CI |
| `\DetMeanVTZeroNegAllN` | 132 | mean AUROC over hosted victims, V T0, negatives all_clean, n |
| `\DetMeanVTZeroNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T0, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTZeroNegAttacked` | 0.60 | mean AUROC over hosted victims, V T0, negatives in_attacked |
| `\DetMeanVTZeroNegAttackedLo` | 0.54 | mean AUROC over hosted victims, V T0, negatives in_attacked, lower 95% CI bound |
| `\DetMeanVTZeroNegAttackedHi` | 0.70 | mean AUROC over hosted victims, V T0, negatives in_attacked, upper 95% CI bound |
| `\DetMeanVTZeroNegAttackedCI` | [0.54, 0.70] | mean AUROC over hosted victims, V T0, negatives in_attacked, 95% CI |
| `\DetMeanVTZeroNegAttackedN` | 385 | mean AUROC over hosted victims, V T0, negatives in_attacked, n |
| `\DetMeanVTZeroNegAttackedP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T0, negatives in_attacked, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTZero` | 0.60 | mean AUROC over hosted victims, V T0, negatives same_slot |
| `\DetMeanVTZeroLo` | 0.54 | mean AUROC over hosted victims, V T0, negatives same_slot, lower 95% CI bound |
| `\DetMeanVTZeroHi` | 0.70 | mean AUROC over hosted victims, V T0, negatives same_slot, upper 95% CI bound |
| `\DetMeanVTZeroCI` | [0.54, 0.70] | mean AUROC over hosted victims, V T0, negatives same_slot, 95% CI |
| `\DetMeanVTZeroN` | 110 | mean AUROC over hosted victims, V T0, negatives same_slot, n |
| `\DetMeanVTZeroP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T0, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTOneNegAll` | 0.53 | mean AUROC over hosted victims, V T1, negatives all_clean |
| `\DetMeanVTOneNegAllLo` | 0.50 | mean AUROC over hosted victims, V T1, negatives all_clean, lower 95% CI bound |
| `\DetMeanVTOneNegAllHi` | 0.62 | mean AUROC over hosted victims, V T1, negatives all_clean, upper 95% CI bound |
| `\DetMeanVTOneNegAllCI` | [0.50, 0.62] | mean AUROC over hosted victims, V T1, negatives all_clean, 95% CI |
| `\DetMeanVTOneNegAllN` | 127 | mean AUROC over hosted victims, V T1, negatives all_clean, n |
| `\DetMeanVTOneNegAllP` | 0.167 | mean AUROC over hosted victims, V T1, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTOneNegAttacked` | 0.51 | mean AUROC over hosted victims, V T1, negatives in_attacked |
| `\DetMeanVTOneNegAttackedLo` | 0.50 | mean AUROC over hosted victims, V T1, negatives in_attacked, lower 95% CI bound |
| `\DetMeanVTOneNegAttackedHi` | 0.56 | mean AUROC over hosted victims, V T1, negatives in_attacked, upper 95% CI bound |
| `\DetMeanVTOneNegAttackedCI` | [0.50, 0.56] | mean AUROC over hosted victims, V T1, negatives in_attacked, 95% CI |
| `\DetMeanVTOneNegAttackedN` | 350 | mean AUROC over hosted victims, V T1, negatives in_attacked, n |
| `\DetMeanVTOneNegAttackedP` | 0.167 | mean AUROC over hosted victims, V T1, negatives in_attacked, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTOne` | 0.52 | mean AUROC over hosted victims, V T1, negatives same_slot |
| `\DetMeanVTOneLo` | 0.50 | mean AUROC over hosted victims, V T1, negatives same_slot, lower 95% CI bound |
| `\DetMeanVTOneHi` | 0.62 | mean AUROC over hosted victims, V T1, negatives same_slot, upper 95% CI bound |
| `\DetMeanVTOneCI` | [0.50, 0.62] | mean AUROC over hosted victims, V T1, negatives same_slot, 95% CI |
| `\DetMeanVTOneN` | 100 | mean AUROC over hosted victims, V T1, negatives same_slot, n |
| `\DetMeanVTOneP` | 0.167 | mean AUROC over hosted victims, V T1, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTTwoNegAll` | 0.52 | mean AUROC over hosted victims, V T2, negatives all_clean |
| `\DetMeanVTTwoNegAllLo` | 0.50 | mean AUROC over hosted victims, V T2, negatives all_clean, lower 95% CI bound |
| `\DetMeanVTTwoNegAllHi` | 0.57 | mean AUROC over hosted victims, V T2, negatives all_clean, upper 95% CI bound |
| `\DetMeanVTTwoNegAllCI` | [0.50, 0.57] | mean AUROC over hosted victims, V T2, negatives all_clean, 95% CI |
| `\DetMeanVTTwoNegAllN` | 131 | mean AUROC over hosted victims, V T2, negatives all_clean, n |
| `\DetMeanVTTwoNegAllP` | 0.047 | mean AUROC over hosted victims, V T2, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTTwoNegAttacked` | 0.53 | mean AUROC over hosted victims, V T2, negatives in_attacked |
| `\DetMeanVTTwoNegAttackedLo` | 0.51 | mean AUROC over hosted victims, V T2, negatives in_attacked, lower 95% CI bound |
| `\DetMeanVTTwoNegAttackedHi` | 0.57 | mean AUROC over hosted victims, V T2, negatives in_attacked, upper 95% CI bound |
| `\DetMeanVTTwoNegAttackedCI` | [0.51, 0.57] | mean AUROC over hosted victims, V T2, negatives in_attacked, 95% CI |
| `\DetMeanVTTwoNegAttackedN` | 378 | mean AUROC over hosted victims, V T2, negatives in_attacked, n |
| `\DetMeanVTTwoNegAttackedP` | 0.016 | mean AUROC over hosted victims, V T2, negatives in_attacked, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTTwo` | 0.53 | mean AUROC over hosted victims, V T2, negatives same_slot |
| `\DetMeanVTTwoLo` | 0.50 | mean AUROC over hosted victims, V T2, negatives same_slot, lower 95% CI bound |
| `\DetMeanVTTwoHi` | 0.58 | mean AUROC over hosted victims, V T2, negatives same_slot, upper 95% CI bound |
| `\DetMeanVTTwoCI` | [0.50, 0.58] | mean AUROC over hosted victims, V T2, negatives same_slot, 95% CI |
| `\DetMeanVTTwoN` | 108 | mean AUROC over hosted victims, V T2, negatives same_slot, n |
| `\DetMeanVTTwoP` | 0.047 | mean AUROC over hosted victims, V T2, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTThreeNegAll` | 0.54 | mean AUROC over hosted victims, V T3, negatives all_clean |
| `\DetMeanVTThreeNegAllLo` | 0.51 | mean AUROC over hosted victims, V T3, negatives all_clean, lower 95% CI bound |
| `\DetMeanVTThreeNegAllHi` | 0.61 | mean AUROC over hosted victims, V T3, negatives all_clean, upper 95% CI bound |
| `\DetMeanVTThreeNegAllCI` | [0.51, 0.61] | mean AUROC over hosted victims, V T3, negatives all_clean, 95% CI |
| `\DetMeanVTThreeNegAllN` | 129 | mean AUROC over hosted victims, V T3, negatives all_clean, n |
| `\DetMeanVTThreeNegAllP` | 0.016 | mean AUROC over hosted victims, V T3, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTThreeNegAttacked` | 0.53 | mean AUROC over hosted victims, V T3, negatives in_attacked |
| `\DetMeanVTThreeNegAttackedLo` | 0.51 | mean AUROC over hosted victims, V T3, negatives in_attacked, lower 95% CI bound |
| `\DetMeanVTThreeNegAttackedHi` | 0.58 | mean AUROC over hosted victims, V T3, negatives in_attacked, upper 95% CI bound |
| `\DetMeanVTThreeNegAttackedCI` | [0.51, 0.58] | mean AUROC over hosted victims, V T3, negatives in_attacked, 95% CI |
| `\DetMeanVTThreeNegAttackedN` | 364 | mean AUROC over hosted victims, V T3, negatives in_attacked, n |
| `\DetMeanVTThreeNegAttackedP` | 0.016 | mean AUROC over hosted victims, V T3, negatives in_attacked, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTThree` | 0.54 | mean AUROC over hosted victims, V T3, negatives same_slot |
| `\DetMeanVTThreeLo` | 0.51 | mean AUROC over hosted victims, V T3, negatives same_slot, lower 95% CI bound |
| `\DetMeanVTThreeHi` | 0.62 | mean AUROC over hosted victims, V T3, negatives same_slot, upper 95% CI bound |
| `\DetMeanVTThreeCI` | [0.51, 0.62] | mean AUROC over hosted victims, V T3, negatives same_slot, 95% CI |
| `\DetMeanVTThreeN` | 104 | mean AUROC over hosted victims, V T3, negatives same_slot, n |
| `\DetMeanVTThreeP` | 0.016 | mean AUROC over hosted victims, V T3, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanFTraceTZeroNegAll` | 0.62 | mean AUROC over hosted victims, f_trace T0, negatives all_clean |
| `\DetMeanFTraceTZeroNegAllLo` | 0.59 | mean AUROC over hosted victims, f_trace T0, negatives all_clean, lower 95% CI bound |
| `\DetMeanFTraceTZeroNegAllHi` | 0.66 | mean AUROC over hosted victims, f_trace T0, negatives all_clean, upper 95% CI bound |
| `\DetMeanFTraceTZeroNegAllCI` | [0.59, 0.66] | mean AUROC over hosted victims, f_trace T0, negatives all_clean, 95% CI |
| `\DetMeanFTraceTZeroNegAllN` | 142 | mean AUROC over hosted victims, f_trace T0, negatives all_clean, n |
| `\DetMeanFTraceTZeroNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T0, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanFTraceTZero` | 0.65 | mean AUROC over hosted victims, f_trace T0, negatives same_slot |
| `\DetMeanFTraceTZeroLo` | 0.62 | mean AUROC over hosted victims, f_trace T0, negatives same_slot, lower 95% CI bound |
| `\DetMeanFTraceTZeroHi` | 0.68 | mean AUROC over hosted victims, f_trace T0, negatives same_slot, upper 95% CI bound |
| `\DetMeanFTraceTZeroCI` | [0.62, 0.68] | mean AUROC over hosted victims, f_trace T0, negatives same_slot, 95% CI |
| `\DetMeanFTraceTZeroN` | 118 | mean AUROC over hosted victims, f_trace T0, negatives same_slot, n |
| `\DetMeanFTraceTZeroP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T0, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanFTraceTOneNegAll` | 0.64 | mean AUROC over hosted victims, f_trace T1, negatives all_clean |
| `\DetMeanFTraceTOneNegAllLo` | 0.61 | mean AUROC over hosted victims, f_trace T1, negatives all_clean, lower 95% CI bound |
| `\DetMeanFTraceTOneNegAllHi` | 0.69 | mean AUROC over hosted victims, f_trace T1, negatives all_clean, upper 95% CI bound |
| `\DetMeanFTraceTOneNegAllCI` | [0.61, 0.69] | mean AUROC over hosted victims, f_trace T1, negatives all_clean, 95% CI |
| `\DetMeanFTraceTOneNegAllN` | 137 | mean AUROC over hosted victims, f_trace T1, negatives all_clean, n |
| `\DetMeanFTraceTOneNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T1, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanFTraceTOne` | 0.66 | mean AUROC over hosted victims, f_trace T1, negatives same_slot |
| `\DetMeanFTraceTOneLo` | 0.62 | mean AUROC over hosted victims, f_trace T1, negatives same_slot, lower 95% CI bound |
| `\DetMeanFTraceTOneHi` | 0.69 | mean AUROC over hosted victims, f_trace T1, negatives same_slot, upper 95% CI bound |
| `\DetMeanFTraceTOneCI` | [0.62, 0.69] | mean AUROC over hosted victims, f_trace T1, negatives same_slot, 95% CI |
| `\DetMeanFTraceTOneN` | 108 | mean AUROC over hosted victims, f_trace T1, negatives same_slot, n |
| `\DetMeanFTraceTOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T1, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanFTraceTTwoNegAll` | 0.64 | mean AUROC over hosted victims, f_trace T2, negatives all_clean |
| `\DetMeanFTraceTTwoNegAllLo` | 0.61 | mean AUROC over hosted victims, f_trace T2, negatives all_clean, lower 95% CI bound |
| `\DetMeanFTraceTTwoNegAllHi` | 0.68 | mean AUROC over hosted victims, f_trace T2, negatives all_clean, upper 95% CI bound |
| `\DetMeanFTraceTTwoNegAllCI` | [0.61, 0.68] | mean AUROC over hosted victims, f_trace T2, negatives all_clean, 95% CI |
| `\DetMeanFTraceTTwoNegAllN` | 141 | mean AUROC over hosted victims, f_trace T2, negatives all_clean, n |
| `\DetMeanFTraceTTwoNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T2, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanFTraceTTwo` | 0.66 | mean AUROC over hosted victims, f_trace T2, negatives same_slot |
| `\DetMeanFTraceTTwoLo` | 0.64 | mean AUROC over hosted victims, f_trace T2, negatives same_slot, lower 95% CI bound |
| `\DetMeanFTraceTTwoHi` | 0.69 | mean AUROC over hosted victims, f_trace T2, negatives same_slot, upper 95% CI bound |
| `\DetMeanFTraceTTwoCI` | [0.64, 0.69] | mean AUROC over hosted victims, f_trace T2, negatives same_slot, 95% CI |
| `\DetMeanFTraceTTwoN` | 116 | mean AUROC over hosted victims, f_trace T2, negatives same_slot, n |
| `\DetMeanFTraceTTwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T2, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanFTraceTThreeNegAll` | 0.62 | mean AUROC over hosted victims, f_trace T3, negatives all_clean |
| `\DetMeanFTraceTThreeNegAllLo` | 0.58 | mean AUROC over hosted victims, f_trace T3, negatives all_clean, lower 95% CI bound |
| `\DetMeanFTraceTThreeNegAllHi` | 0.66 | mean AUROC over hosted victims, f_trace T3, negatives all_clean, upper 95% CI bound |
| `\DetMeanFTraceTThreeNegAllCI` | [0.58, 0.66] | mean AUROC over hosted victims, f_trace T3, negatives all_clean, 95% CI |
| `\DetMeanFTraceTThreeNegAllN` | 139 | mean AUROC over hosted victims, f_trace T3, negatives all_clean, n |
| `\DetMeanFTraceTThreeNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T3, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanFTraceTThree` | 0.65 | mean AUROC over hosted victims, f_trace T3, negatives same_slot |
| `\DetMeanFTraceTThreeLo` | 0.60 | mean AUROC over hosted victims, f_trace T3, negatives same_slot, lower 95% CI bound |
| `\DetMeanFTraceTThreeHi` | 0.70 | mean AUROC over hosted victims, f_trace T3, negatives same_slot, upper 95% CI bound |
| `\DetMeanFTraceTThreeCI` | [0.60, 0.70] | mean AUROC over hosted victims, f_trace T3, negatives same_slot, 95% CI |
| `\DetMeanFTraceTThreeN` | 112 | mean AUROC over hosted victims, f_trace T3, negatives same_slot, n |
| `\DetMeanFTraceTThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T3, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRFieldTZeroNegAll` | 0.65 | mean AUROC over hosted victims, r_field T0, negatives all_clean |
| `\DetMeanRFieldTZeroNegAllLo` | 0.61 | mean AUROC over hosted victims, r_field T0, negatives all_clean, lower 95% CI bound |
| `\DetMeanRFieldTZeroNegAllHi` | 0.69 | mean AUROC over hosted victims, r_field T0, negatives all_clean, upper 95% CI bound |
| `\DetMeanRFieldTZeroNegAllCI` | [0.61, 0.69] | mean AUROC over hosted victims, r_field T0, negatives all_clean, 95% CI |
| `\DetMeanRFieldTZeroNegAllN` | 142 | mean AUROC over hosted victims, r_field T0, negatives all_clean, n |
| `\DetMeanRFieldTZeroNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T0, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRFieldTZero` | 0.65 | mean AUROC over hosted victims, r_field T0, negatives same_slot |
| `\DetMeanRFieldTZeroLo` | 0.59 | mean AUROC over hosted victims, r_field T0, negatives same_slot, lower 95% CI bound |
| `\DetMeanRFieldTZeroHi` | 0.70 | mean AUROC over hosted victims, r_field T0, negatives same_slot, upper 95% CI bound |
| `\DetMeanRFieldTZeroCI` | [0.59, 0.70] | mean AUROC over hosted victims, r_field T0, negatives same_slot, 95% CI |
| `\DetMeanRFieldTZeroN` | 118 | mean AUROC over hosted victims, r_field T0, negatives same_slot, n |
| `\DetMeanRFieldTZeroP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T0, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRFieldTOneNegAll` | 0.66 | mean AUROC over hosted victims, r_field T1, negatives all_clean |
| `\DetMeanRFieldTOneNegAllLo` | 0.62 | mean AUROC over hosted victims, r_field T1, negatives all_clean, lower 95% CI bound |
| `\DetMeanRFieldTOneNegAllHi` | 0.72 | mean AUROC over hosted victims, r_field T1, negatives all_clean, upper 95% CI bound |
| `\DetMeanRFieldTOneNegAllCI` | [0.62, 0.72] | mean AUROC over hosted victims, r_field T1, negatives all_clean, 95% CI |
| `\DetMeanRFieldTOneNegAllN` | 137 | mean AUROC over hosted victims, r_field T1, negatives all_clean, n |
| `\DetMeanRFieldTOneNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T1, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRFieldTOne` | 0.65 | mean AUROC over hosted victims, r_field T1, negatives same_slot |
| `\DetMeanRFieldTOneLo` | 0.60 | mean AUROC over hosted victims, r_field T1, negatives same_slot, lower 95% CI bound |
| `\DetMeanRFieldTOneHi` | 0.70 | mean AUROC over hosted victims, r_field T1, negatives same_slot, upper 95% CI bound |
| `\DetMeanRFieldTOneCI` | [0.60, 0.70] | mean AUROC over hosted victims, r_field T1, negatives same_slot, 95% CI |
| `\DetMeanRFieldTOneN` | 108 | mean AUROC over hosted victims, r_field T1, negatives same_slot, n |
| `\DetMeanRFieldTOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T1, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRFieldTTwoNegAll` | 0.65 | mean AUROC over hosted victims, r_field T2, negatives all_clean |
| `\DetMeanRFieldTTwoNegAllLo` | 0.62 | mean AUROC over hosted victims, r_field T2, negatives all_clean, lower 95% CI bound |
| `\DetMeanRFieldTTwoNegAllHi` | 0.70 | mean AUROC over hosted victims, r_field T2, negatives all_clean, upper 95% CI bound |
| `\DetMeanRFieldTTwoNegAllCI` | [0.62, 0.70] | mean AUROC over hosted victims, r_field T2, negatives all_clean, 95% CI |
| `\DetMeanRFieldTTwoNegAllN` | 141 | mean AUROC over hosted victims, r_field T2, negatives all_clean, n |
| `\DetMeanRFieldTTwoNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T2, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRFieldTTwo` | 0.65 | mean AUROC over hosted victims, r_field T2, negatives same_slot |
| `\DetMeanRFieldTTwoLo` | 0.60 | mean AUROC over hosted victims, r_field T2, negatives same_slot, lower 95% CI bound |
| `\DetMeanRFieldTTwoHi` | 0.71 | mean AUROC over hosted victims, r_field T2, negatives same_slot, upper 95% CI bound |
| `\DetMeanRFieldTTwoCI` | [0.60, 0.71] | mean AUROC over hosted victims, r_field T2, negatives same_slot, 95% CI |
| `\DetMeanRFieldTTwoN` | 116 | mean AUROC over hosted victims, r_field T2, negatives same_slot, n |
| `\DetMeanRFieldTTwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T2, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRFieldTThreeNegAll` | 0.65 | mean AUROC over hosted victims, r_field T3, negatives all_clean |
| `\DetMeanRFieldTThreeNegAllLo` | 0.59 | mean AUROC over hosted victims, r_field T3, negatives all_clean, lower 95% CI bound |
| `\DetMeanRFieldTThreeNegAllHi` | 0.70 | mean AUROC over hosted victims, r_field T3, negatives all_clean, upper 95% CI bound |
| `\DetMeanRFieldTThreeNegAllCI` | [0.59, 0.70] | mean AUROC over hosted victims, r_field T3, negatives all_clean, 95% CI |
| `\DetMeanRFieldTThreeNegAllN` | 139 | mean AUROC over hosted victims, r_field T3, negatives all_clean, n |
| `\DetMeanRFieldTThreeNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T3, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRFieldTThree` | 0.65 | mean AUROC over hosted victims, r_field T3, negatives same_slot |
| `\DetMeanRFieldTThreeLo` | 0.57 | mean AUROC over hosted victims, r_field T3, negatives same_slot, lower 95% CI bound |
| `\DetMeanRFieldTThreeHi` | 0.73 | mean AUROC over hosted victims, r_field T3, negatives same_slot, upper 95% CI bound |
| `\DetMeanRFieldTThreeCI` | [0.57, 0.73] | mean AUROC over hosted victims, r_field T3, negatives same_slot, 95% CI |
| `\DetMeanRFieldTThreeN` | 112 | mean AUROC over hosted victims, r_field T3, negatives same_slot, n |
| `\DetMeanRFieldTThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T3, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTZero` | 0.59 | AUROC V T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTZeroLo` | 0.53 | AUROC V T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTZeroHi` | 0.74 | AUROC V T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTZeroCI` | [0.53, 0.74] | AUROC V T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTZeroN` | 60 | AUROC V T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTZeroP` | n/a | AUROC V T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTZeroTprOne` | 30.0 | TPR at 1% FPR (%), V T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTZeroTprOneLo` | 10.0 | TPR at 1% FPR (%), V T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTZeroTprOneHi` | 56.7 | TPR at 1% FPR (%), V T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTZeroTprOneCI` | [10.0, 56.7] | TPR at 1% FPR (%), V T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTZeroTprOneN` | 60 | TPR at 1% FPR (%), V T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTZeroTprOneP` | n/a | TPR at 1% FPR (%), V T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTZeroTprFive` | 30.0 | TPR at 5% FPR (%), V T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTZeroTprFiveLo` | 10.0 | TPR at 5% FPR (%), V T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTZeroTprFiveHi` | 56.7 | TPR at 5% FPR (%), V T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTZeroTprFiveCI` | [10.0, 56.7] | TPR at 5% FPR (%), V T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTZeroTprFiveN` | 60 | TPR at 5% FPR (%), V T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTZeroTprFiveP` | n/a | TPR at 5% FPR (%), V T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTOne` | 0.54 | AUROC V T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTOneLo` | 0.50 | AUROC V T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTOneHi` | 0.74 | AUROC V T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTOneCI` | [0.50, 0.74] | AUROC V T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTOneN` | 50 | AUROC V T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTOneP` | n/a | AUROC V T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTOneTprOne` | 16.0 | TPR at 1% FPR (%), V T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTOneTprOneLo` | 0.0 | TPR at 1% FPR (%), V T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTOneTprOneHi` | 48.0 | TPR at 1% FPR (%), V T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTOneTprOneCI` | [0.0, 48.0] | TPR at 1% FPR (%), V T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTOneTprOneN` | 50 | TPR at 1% FPR (%), V T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTOneTprOneP` | n/a | TPR at 1% FPR (%), V T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTOneTprFive` | 24.0 | TPR at 5% FPR (%), V T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTOneTprFiveLo` | 0.0 | TPR at 5% FPR (%), V T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTOneTprFiveHi` | 53.3 | TPR at 5% FPR (%), V T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTOneTprFiveCI` | [0.0, 53.3] | TPR at 5% FPR (%), V T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTOneTprFiveN` | 50 | TPR at 5% FPR (%), V T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTOneTprFiveP` | n/a | TPR at 5% FPR (%), V T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTTwo` | 0.51 | AUROC V T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTTwoLo` | 0.49 | AUROC V T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTTwoHi` | 0.57 | AUROC V T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTTwoCI` | [0.49, 0.57] | AUROC V T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTTwoN` | 60 | AUROC V T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTTwoP` | n/a | AUROC V T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTTwoTprOne` | 10.0 | TPR at 1% FPR (%), V T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTTwoTprOneLo` | 0.0 | TPR at 1% FPR (%), V T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTTwoTprOneHi` | 23.3 | TPR at 1% FPR (%), V T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTTwoTprOneCI` | [0.0, 23.3] | TPR at 1% FPR (%), V T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTTwoTprOneN` | 60 | TPR at 1% FPR (%), V T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTTwoTprOneP` | n/a | TPR at 1% FPR (%), V T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTTwoTprFive` | 13.3 | TPR at 5% FPR (%), V T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTTwoTprFiveLo` | 0.0 | TPR at 5% FPR (%), V T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTTwoTprFiveHi` | 26.7 | TPR at 5% FPR (%), V T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTTwoTprFiveCI` | [0.0, 26.7] | TPR at 5% FPR (%), V T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTTwoTprFiveN` | 60 | TPR at 5% FPR (%), V T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTTwoTprFiveP` | n/a | TPR at 5% FPR (%), V T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTThree` | 0.54 | AUROC V T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTThreeLo` | 0.50 | AUROC V T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTThreeHi` | 0.69 | AUROC V T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTThreeCI` | [0.50, 0.69] | AUROC V T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTThreeN` | 58 | AUROC V T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTThreeP` | n/a | AUROC V T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTThreeTprOne` | 13.8 | TPR at 1% FPR (%), V T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTThreeTprOneLo` | 0.0 | TPR at 1% FPR (%), V T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTThreeTprOneHi` | 41.4 | TPR at 1% FPR (%), V T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTThreeTprOneCI` | [0.0, 41.4] | TPR at 1% FPR (%), V T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTThreeTprOneN` | 58 | TPR at 1% FPR (%), V T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTThreeTprOneP` | n/a | TPR at 1% FPR (%), V T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTThreeTprFive` | 17.2 | TPR at 5% FPR (%), V T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTThreeTprFiveLo` | 0.0 | TPR at 5% FPR (%), V T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTThreeTprFiveHi` | 43.3 | TPR at 5% FPR (%), V T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTThreeTprFiveCI` | [0.0, 43.3] | TPR at 5% FPR (%), V T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTThreeTprFiveN` | 58 | TPR at 5% FPR (%), V T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTThreeTprFiveP` | n/a | TPR at 5% FPR (%), V T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTZero` | 0.88 | AUROC C T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTZeroLo` | 0.80 | AUROC C T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTZeroHi` | 0.95 | AUROC C T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTZeroCI` | [0.80, 0.95] | AUROC C T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTZeroN` | 60 | AUROC C T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTZeroP` | n/a | AUROC C T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTZeroTprOne` | 76.7 | TPR at 1% FPR (%), C T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTZeroTprOneLo` | 60.0 | TPR at 1% FPR (%), C T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTZeroTprOneHi` | 90.0 | TPR at 1% FPR (%), C T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTZeroTprOneCI` | [60.0, 90.0] | TPR at 1% FPR (%), C T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTZeroTprOneN` | 60 | TPR at 1% FPR (%), C T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTZeroTprOneP` | n/a | TPR at 1% FPR (%), C T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTZeroTprFive` | 76.7 | TPR at 5% FPR (%), C T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTZeroTprFiveLo` | 60.0 | TPR at 5% FPR (%), C T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTZeroTprFiveHi` | 90.0 | TPR at 5% FPR (%), C T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTZeroTprFiveCI` | [60.0, 90.0] | TPR at 5% FPR (%), C T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTZeroTprFiveN` | 60 | TPR at 5% FPR (%), C T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTZeroTprFiveP` | n/a | TPR at 5% FPR (%), C T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTOne` | 0.90 | AUROC C T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTOneLo` | 0.78 | AUROC C T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTOneHi` | 1.00 | AUROC C T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTOneCI` | [0.78, 1.00] | AUROC C T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTOneN` | 50 | AUROC C T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTOneP` | n/a | AUROC C T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTOneTprOne` | 80.0 | TPR at 1% FPR (%), C T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTOneTprOneLo` | 56.0 | TPR at 1% FPR (%), C T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTOneTprOneHi` | 100.0 | TPR at 1% FPR (%), C T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTOneTprOneCI` | [56.0, 100.0] | TPR at 1% FPR (%), C T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTOneTprOneN` | 50 | TPR at 1% FPR (%), C T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTOneTprOneP` | n/a | TPR at 1% FPR (%), C T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTOneTprFive` | 80.0 | TPR at 5% FPR (%), C T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTOneTprFiveLo` | 56.0 | TPR at 5% FPR (%), C T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTOneTprFiveHi` | 100.0 | TPR at 5% FPR (%), C T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTOneTprFiveCI` | [56.0, 100.0] | TPR at 5% FPR (%), C T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTOneTprFiveN` | 50 | TPR at 5% FPR (%), C T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTOneTprFiveP` | n/a | TPR at 5% FPR (%), C T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTTwo` | 0.93 | AUROC C T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTTwoLo` | 0.83 | AUROC C T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTTwoHi` | 1.00 | AUROC C T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTTwoCI` | [0.83, 1.00] | AUROC C T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTTwoN` | 60 | AUROC C T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTTwoP` | n/a | AUROC C T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTTwoTprOne` | 86.7 | TPR at 1% FPR (%), C T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTTwoTprOneLo` | 66.7 | TPR at 1% FPR (%), C T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTTwoTprOneHi` | 100.0 | TPR at 1% FPR (%), C T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTTwoTprOneCI` | [66.7, 100.0] | TPR at 1% FPR (%), C T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTTwoTprOneN` | 60 | TPR at 1% FPR (%), C T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTTwoTprOneP` | n/a | TPR at 1% FPR (%), C T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTTwoTprFive` | 86.7 | TPR at 5% FPR (%), C T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTTwoTprFiveLo` | 66.7 | TPR at 5% FPR (%), C T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTTwoTprFiveHi` | 100.0 | TPR at 5% FPR (%), C T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTTwoTprFiveCI` | [66.7, 100.0] | TPR at 5% FPR (%), C T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTTwoTprFiveN` | 60 | TPR at 5% FPR (%), C T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTTwoTprFiveP` | n/a | TPR at 5% FPR (%), C T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTThree` | 0.93 | AUROC C T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTThreeLo` | 0.85 | AUROC C T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTThreeHi` | 0.98 | AUROC C T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTThreeCI` | [0.85, 0.98] | AUROC C T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTThreeN` | 58 | AUROC C T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTThreeP` | n/a | AUROC C T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTThreeTprOne` | 86.2 | TPR at 1% FPR (%), C T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTThreeTprOneLo` | 70.4 | TPR at 1% FPR (%), C T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTThreeTprOneHi` | 96.7 | TPR at 1% FPR (%), C T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTThreeTprOneCI` | [70.4, 96.7] | TPR at 1% FPR (%), C T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTThreeTprOneN` | 58 | TPR at 1% FPR (%), C T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTThreeTprOneP` | n/a | TPR at 1% FPR (%), C T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTThreeTprFive` | 86.2 | TPR at 5% FPR (%), C T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTThreeTprFiveLo` | 70.4 | TPR at 5% FPR (%), C T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTThreeTprFiveHi` | 96.7 | TPR at 5% FPR (%), C T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTThreeTprFiveCI` | [70.4, 96.7] | TPR at 5% FPR (%), C T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTThreeTprFiveN` | 58 | TPR at 5% FPR (%), C T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTThreeTprFiveP` | n/a | TPR at 5% FPR (%), C T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTZero` | 0.72 | AUROC R T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTZeroLo` | 0.67 | AUROC R T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTZeroHi` | 0.77 | AUROC R T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTZeroCI` | [0.67, 0.77] | AUROC R T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTZeroN` | 60 | AUROC R T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTZeroP` | n/a | AUROC R T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTZeroTprOne` | 0.0 | TPR at 1% FPR (%), R T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTZeroTprOneLo` | 0.0 | TPR at 1% FPR (%), R T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTZeroTprOneHi` | 0.0 | TPR at 1% FPR (%), R T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTZeroTprOneCI` | [0.0, 0.0] | TPR at 1% FPR (%), R T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTZeroTprOneN` | 60 | TPR at 1% FPR (%), R T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTZeroTprOneP` | n/a | TPR at 1% FPR (%), R T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTZeroTprFive` | 0.0 | TPR at 5% FPR (%), R T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTZeroTprFiveLo` | 0.0 | TPR at 5% FPR (%), R T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTZeroTprFiveHi` | 0.0 | TPR at 5% FPR (%), R T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTZeroTprFiveCI` | [0.0, 0.0] | TPR at 5% FPR (%), R T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTZeroTprFiveN` | 60 | TPR at 5% FPR (%), R T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTZeroTprFiveP` | n/a | TPR at 5% FPR (%), R T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTOne` | 0.72 | AUROC R T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTOneLo` | 0.65 | AUROC R T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTOneHi` | 0.78 | AUROC R T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTOneCI` | [0.65, 0.78] | AUROC R T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTOneN` | 50 | AUROC R T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTOneP` | n/a | AUROC R T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTOneTprOne` | 0.0 | TPR at 1% FPR (%), R T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTOneTprOneLo` | 0.0 | TPR at 1% FPR (%), R T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTOneTprOneHi` | 0.0 | TPR at 1% FPR (%), R T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTOneTprOneCI` | [0.0, 0.0] | TPR at 1% FPR (%), R T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTOneTprOneN` | 50 | TPR at 1% FPR (%), R T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTOneTprOneP` | n/a | TPR at 1% FPR (%), R T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTOneTprFive` | 0.0 | TPR at 5% FPR (%), R T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTOneTprFiveLo` | 0.0 | TPR at 5% FPR (%), R T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTOneTprFiveHi` | 0.0 | TPR at 5% FPR (%), R T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTOneTprFiveCI` | [0.0, 0.0] | TPR at 5% FPR (%), R T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTOneTprFiveN` | 50 | TPR at 5% FPR (%), R T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTOneTprFiveP` | n/a | TPR at 5% FPR (%), R T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTTwo` | 0.72 | AUROC R T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTTwoLo` | 0.67 | AUROC R T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTTwoHi` | 0.77 | AUROC R T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTTwoCI` | [0.67, 0.77] | AUROC R T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTTwoN` | 60 | AUROC R T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTTwoP` | n/a | AUROC R T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTTwoTprOne` | 0.0 | TPR at 1% FPR (%), R T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTTwoTprOneLo` | 0.0 | TPR at 1% FPR (%), R T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTTwoTprOneHi` | 0.0 | TPR at 1% FPR (%), R T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTTwoTprOneCI` | [0.0, 0.0] | TPR at 1% FPR (%), R T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTTwoTprOneN` | 60 | TPR at 1% FPR (%), R T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTTwoTprOneP` | n/a | TPR at 1% FPR (%), R T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTTwoTprFive` | 0.0 | TPR at 5% FPR (%), R T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTTwoTprFiveLo` | 0.0 | TPR at 5% FPR (%), R T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTTwoTprFiveHi` | 0.0 | TPR at 5% FPR (%), R T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTTwoTprFiveCI` | [0.0, 0.0] | TPR at 5% FPR (%), R T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTTwoTprFiveN` | 60 | TPR at 5% FPR (%), R T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTTwoTprFiveP` | n/a | TPR at 5% FPR (%), R T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTThree` | 0.71 | AUROC R T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTThreeLo` | 0.64 | AUROC R T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTThreeHi` | 0.77 | AUROC R T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTThreeCI` | [0.64, 0.77] | AUROC R T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTThreeN` | 58 | AUROC R T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTThreeP` | n/a | AUROC R T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTThreeTprOne` | 0.0 | TPR at 1% FPR (%), R T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTThreeTprOneLo` | 0.0 | TPR at 1% FPR (%), R T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTThreeTprOneHi` | 0.0 | TPR at 1% FPR (%), R T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTThreeTprOneCI` | [0.0, 0.0] | TPR at 1% FPR (%), R T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTThreeTprOneN` | 58 | TPR at 1% FPR (%), R T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTThreeTprOneP` | n/a | TPR at 1% FPR (%), R T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTThreeTprFive` | 0.0 | TPR at 5% FPR (%), R T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTThreeTprFiveLo` | 0.0 | TPR at 5% FPR (%), R T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTThreeTprFiveHi` | 0.0 | TPR at 5% FPR (%), R T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTThreeTprFiveCI` | [0.0, 0.0] | TPR at 5% FPR (%), R T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTThreeTprFiveN` | 58 | TPR at 5% FPR (%), R T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTThreeTprFiveP` | n/a | TPR at 5% FPR (%), R T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTZero` | 0.62 | AUROC r_field T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTZeroLo` | 0.54 | AUROC r_field T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTZeroHi` | 0.71 | AUROC r_field T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTZeroCI` | [0.54, 0.71] | AUROC r_field T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTZeroN` | 60 | AUROC r_field T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTZeroP` | n/a | AUROC r_field T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTZeroTprOne` | 0.0 | TPR at 1% FPR (%), r_field T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTZeroTprOneLo` | 0.0 | TPR at 1% FPR (%), r_field T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTZeroTprOneHi` | 26.7 | TPR at 1% FPR (%), r_field T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTZeroTprOneCI` | [0.0, 26.7] | TPR at 1% FPR (%), r_field T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTZeroTprOneN` | 60 | TPR at 1% FPR (%), r_field T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTZeroTprOneP` | n/a | TPR at 1% FPR (%), r_field T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTZeroTprFive` | 3.3 | TPR at 5% FPR (%), r_field T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTZeroTprFiveLo` | 0.0 | TPR at 5% FPR (%), r_field T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTZeroTprFiveHi` | 36.7 | TPR at 5% FPR (%), r_field T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTZeroTprFiveCI` | [0.0, 36.7] | TPR at 5% FPR (%), r_field T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTZeroTprFiveN` | 60 | TPR at 5% FPR (%), r_field T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTZeroTprFiveP` | n/a | TPR at 5% FPR (%), r_field T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTOne` | 0.63 | AUROC r_field T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTOneLo` | 0.55 | AUROC r_field T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTOneHi` | 0.69 | AUROC r_field T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTOneCI` | [0.55, 0.69] | AUROC r_field T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTOneN` | 50 | AUROC r_field T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTOneP` | n/a | AUROC r_field T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTOneTprOne` | 0.0 | TPR at 1% FPR (%), r_field T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTOneTprOneLo` | 0.0 | TPR at 1% FPR (%), r_field T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTOneTprOneHi` | 36.7 | TPR at 1% FPR (%), r_field T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTOneTprOneCI` | [0.0, 36.7] | TPR at 1% FPR (%), r_field T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTOneTprOneN` | 50 | TPR at 1% FPR (%), r_field T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTOneTprOneP` | n/a | TPR at 1% FPR (%), r_field T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTOneTprFive` | 4.0 | TPR at 5% FPR (%), r_field T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTOneTprFiveLo` | 0.0 | TPR at 5% FPR (%), r_field T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTOneTprFiveHi` | 40.0 | TPR at 5% FPR (%), r_field T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTOneTprFiveCI` | [0.0, 40.0] | TPR at 5% FPR (%), r_field T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTOneTprFiveN` | 50 | TPR at 5% FPR (%), r_field T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTOneTprFiveP` | n/a | TPR at 5% FPR (%), r_field T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTTwo` | 0.62 | AUROC r_field T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTTwoLo` | 0.55 | AUROC r_field T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTTwoHi` | 0.71 | AUROC r_field T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTTwoCI` | [0.55, 0.71] | AUROC r_field T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTTwoN` | 60 | AUROC r_field T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTTwoP` | n/a | AUROC r_field T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTTwoTprOne` | 0.0 | TPR at 1% FPR (%), r_field T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTTwoTprOneLo` | 0.0 | TPR at 1% FPR (%), r_field T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTTwoTprOneHi` | 30.0 | TPR at 1% FPR (%), r_field T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTTwoTprOneCI` | [0.0, 30.0] | TPR at 1% FPR (%), r_field T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTTwoTprOneN` | 60 | TPR at 1% FPR (%), r_field T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTTwoTprOneP` | n/a | TPR at 1% FPR (%), r_field T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTTwoTprFive` | 3.3 | TPR at 5% FPR (%), r_field T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTTwoTprFiveLo` | 0.0 | TPR at 5% FPR (%), r_field T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTTwoTprFiveHi` | 36.7 | TPR at 5% FPR (%), r_field T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTTwoTprFiveCI` | [0.0, 36.7] | TPR at 5% FPR (%), r_field T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTTwoTprFiveN` | 60 | TPR at 5% FPR (%), r_field T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTTwoTprFiveP` | n/a | TPR at 5% FPR (%), r_field T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTThree` | 0.61 | AUROC r_field T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTThreeLo` | 0.50 | AUROC r_field T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTThreeHi` | 0.74 | AUROC r_field T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTThreeCI` | [0.50, 0.74] | AUROC r_field T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTThreeN` | 58 | AUROC r_field T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTThreeP` | n/a | AUROC r_field T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTThreeTprOne` | 0.0 | TPR at 1% FPR (%), r_field T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTThreeTprOneLo` | 0.0 | TPR at 1% FPR (%), r_field T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTThreeTprOneHi` | 29.6 | TPR at 1% FPR (%), r_field T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTThreeTprOneCI` | [0.0, 29.6] | TPR at 1% FPR (%), r_field T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTThreeTprOneN` | 58 | TPR at 1% FPR (%), r_field T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTThreeTprOneP` | n/a | TPR at 1% FPR (%), r_field T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTThreeTprFive` | 0.0 | TPR at 5% FPR (%), r_field T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTThreeTprFiveLo` | 0.0 | TPR at 5% FPR (%), r_field T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTThreeTprFiveHi` | 42.9 | TPR at 5% FPR (%), r_field T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTThreeTprFiveCI` | [0.0, 42.9] | TPR at 5% FPR (%), r_field T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTThreeTprFiveN` | 58 | TPR at 5% FPR (%), r_field T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTThreeTprFiveP` | n/a | TPR at 5% FPR (%), r_field T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTZero` | 0.62 | AUROC f_trace T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTZeroLo` | 0.57 | AUROC f_trace T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTZeroHi` | 0.67 | AUROC f_trace T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTZeroCI` | [0.57, 0.67] | AUROC f_trace T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTZeroN` | 60 | AUROC f_trace T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTZeroP` | n/a | AUROC f_trace T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTZeroTprOne` | 0.0 | TPR at 1% FPR (%), f_trace T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTZeroTprOneLo` | 0.0 | TPR at 1% FPR (%), f_trace T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTZeroTprOneHi` | 30.0 | TPR at 1% FPR (%), f_trace T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTZeroTprOneCI` | [0.0, 30.0] | TPR at 1% FPR (%), f_trace T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTZeroTprOneN` | 60 | TPR at 1% FPR (%), f_trace T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTZeroTprOneP` | n/a | TPR at 1% FPR (%), f_trace T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTZeroTprFive` | 3.3 | TPR at 5% FPR (%), f_trace T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTZeroTprFiveLo` | 0.0 | TPR at 5% FPR (%), f_trace T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTZeroTprFiveHi` | 40.0 | TPR at 5% FPR (%), f_trace T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTZeroTprFiveCI` | [0.0, 40.0] | TPR at 5% FPR (%), f_trace T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTZeroTprFiveN` | 60 | TPR at 5% FPR (%), f_trace T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTZeroTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTOne` | 0.64 | AUROC f_trace T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTOneLo` | 0.57 | AUROC f_trace T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTOneHi` | 0.70 | AUROC f_trace T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTOneCI` | [0.57, 0.70] | AUROC f_trace T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTOneN` | 50 | AUROC f_trace T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTOneP` | n/a | AUROC f_trace T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTOneTprOne` | 4.0 | TPR at 1% FPR (%), f_trace T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTOneTprOneLo` | 0.0 | TPR at 1% FPR (%), f_trace T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTOneTprOneHi` | 40.0 | TPR at 1% FPR (%), f_trace T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTOneTprOneCI` | [0.0, 40.0] | TPR at 1% FPR (%), f_trace T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTOneTprOneN` | 50 | TPR at 1% FPR (%), f_trace T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTOneTprOneP` | n/a | TPR at 1% FPR (%), f_trace T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTOneTprFive` | 8.0 | TPR at 5% FPR (%), f_trace T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTOneTprFiveLo` | 0.0 | TPR at 5% FPR (%), f_trace T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTOneTprFiveHi` | 48.0 | TPR at 5% FPR (%), f_trace T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTOneTprFiveCI` | [0.0, 48.0] | TPR at 5% FPR (%), f_trace T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTOneTprFiveN` | 50 | TPR at 5% FPR (%), f_trace T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTOneTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTTwo` | 0.64 | AUROC f_trace T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTTwoLo` | 0.61 | AUROC f_trace T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTTwoHi` | 0.68 | AUROC f_trace T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTTwoCI` | [0.61, 0.68] | AUROC f_trace T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTTwoN` | 60 | AUROC f_trace T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTTwoP` | n/a | AUROC f_trace T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTTwoTprOne` | 6.7 | TPR at 1% FPR (%), f_trace T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTTwoTprOneLo` | 0.0 | TPR at 1% FPR (%), f_trace T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTTwoTprOneHi` | 30.0 | TPR at 1% FPR (%), f_trace T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTTwoTprOneCI` | [0.0, 30.0] | TPR at 1% FPR (%), f_trace T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTTwoTprOneN` | 60 | TPR at 1% FPR (%), f_trace T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTTwoTprOneP` | n/a | TPR at 1% FPR (%), f_trace T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTTwoTprFive` | 6.7 | TPR at 5% FPR (%), f_trace T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTTwoTprFiveLo` | 0.0 | TPR at 5% FPR (%), f_trace T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTTwoTprFiveHi` | 40.0 | TPR at 5% FPR (%), f_trace T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTTwoTprFiveCI` | [0.0, 40.0] | TPR at 5% FPR (%), f_trace T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTTwoTprFiveN` | 60 | TPR at 5% FPR (%), f_trace T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTTwoTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTThree` | 0.61 | AUROC f_trace T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTThreeLo` | 0.52 | AUROC f_trace T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTThreeHi` | 0.69 | AUROC f_trace T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTThreeCI` | [0.52, 0.69] | AUROC f_trace T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTThreeN` | 58 | AUROC f_trace T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTThreeP` | n/a | AUROC f_trace T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTThreeTprOne` | 3.4 | TPR at 1% FPR (%), f_trace T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTThreeTprOneLo` | 0.0 | TPR at 1% FPR (%), f_trace T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTThreeTprOneHi` | 35.7 | TPR at 1% FPR (%), f_trace T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTThreeTprOneCI` | [0.0, 35.7] | TPR at 1% FPR (%), f_trace T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTThreeTprOneN` | 58 | TPR at 1% FPR (%), f_trace T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTThreeTprOneP` | n/a | TPR at 1% FPR (%), f_trace T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTThreeTprFive` | 10.3 | TPR at 5% FPR (%), f_trace T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTThreeTprFiveLo` | 0.0 | TPR at 5% FPR (%), f_trace T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTThreeTprFiveHi` | 44.4 | TPR at 5% FPR (%), f_trace T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTThreeTprFiveCI` | [0.0, 44.4] | TPR at 5% FPR (%), f_trace T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTThreeTprFiveN` | 58 | TPR at 5% FPR (%), f_trace T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTThreeTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTZero` | 0.62 | AUROC V T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTZeroLo` | 0.52 | AUROC V T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTZeroHi` | 0.73 | AUROC V T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTZeroCI` | [0.52, 0.73] | AUROC V T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTZeroN` | 50 | AUROC V T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTZeroP` | n/a | AUROC V T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTZeroTprOne` | 24.0 | TPR at 1% FPR (%), V T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTZeroTprOneLo` | 4.0 | TPR at 1% FPR (%), V T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTZeroTprOneHi` | 46.7 | TPR at 1% FPR (%), V T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTZeroTprOneCI` | [4.0, 46.7] | TPR at 1% FPR (%), V T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTZeroTprOneN` | 50 | TPR at 1% FPR (%), V T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTZeroTprOneP` | n/a | TPR at 1% FPR (%), V T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTZeroTprFive` | 24.0 | TPR at 5% FPR (%), V T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTZeroTprFiveLo` | 4.0 | TPR at 5% FPR (%), V T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTZeroTprFiveHi` | 46.7 | TPR at 5% FPR (%), V T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTZeroTprFiveCI` | [4.0, 46.7] | TPR at 5% FPR (%), V T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTZeroTprFiveN` | 50 | TPR at 5% FPR (%), V T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTZeroTprFiveP` | n/a | TPR at 5% FPR (%), V T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTOne` | 0.50 | AUROC V T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTOneLo` | 0.50 | AUROC V T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTOneHi` | 0.50 | AUROC V T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTOneCI` | [0.50, 0.50] | AUROC V T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTOneN` | 50 | AUROC V T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTOneP` | n/a | AUROC V T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTOneTprOne` | 0.0 | TPR at 1% FPR (%), V T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTOneTprOneLo` | 0.0 | TPR at 1% FPR (%), V T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTOneTprOneHi` | 0.0 | TPR at 1% FPR (%), V T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTOneTprOneCI` | [0.0, 0.0] | TPR at 1% FPR (%), V T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTOneTprOneN` | 50 | TPR at 1% FPR (%), V T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTOneTprOneP` | n/a | TPR at 1% FPR (%), V T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTOneTprFive` | 0.0 | TPR at 5% FPR (%), V T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTOneTprFiveLo` | 0.0 | TPR at 5% FPR (%), V T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTOneTprFiveHi` | 0.0 | TPR at 5% FPR (%), V T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTOneTprFiveCI` | [0.0, 0.0] | TPR at 5% FPR (%), V T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTOneTprFiveN` | 50 | TPR at 5% FPR (%), V T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTOneTprFiveP` | n/a | TPR at 5% FPR (%), V T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTTwo` | 0.54 | AUROC V T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTTwoLo` | 0.50 | AUROC V T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTTwoHi` | 0.58 | AUROC V T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTTwoCI` | [0.50, 0.58] | AUROC V T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTTwoN` | 48 | AUROC V T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTTwoP` | n/a | AUROC V T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTTwoTprOne` | 8.3 | TPR at 1% FPR (%), V T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTTwoTprOneLo` | 0.0 | TPR at 1% FPR (%), V T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTTwoTprOneHi` | 16.7 | TPR at 1% FPR (%), V T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTTwoTprOneCI` | [0.0, 16.7] | TPR at 1% FPR (%), V T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTTwoTprOneN` | 48 | TPR at 1% FPR (%), V T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTTwoTprOneP` | n/a | TPR at 1% FPR (%), V T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTTwoTprFive` | 8.3 | TPR at 5% FPR (%), V T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTTwoTprFiveLo` | 0.0 | TPR at 5% FPR (%), V T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTTwoTprFiveHi` | 16.7 | TPR at 5% FPR (%), V T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTTwoTprFiveCI` | [0.0, 16.7] | TPR at 5% FPR (%), V T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTTwoTprFiveN` | 48 | TPR at 5% FPR (%), V T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTTwoTprFiveP` | n/a | TPR at 5% FPR (%), V T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTThree` | 0.54 | AUROC V T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTThreeLo` | 0.50 | AUROC V T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTThreeHi` | 0.59 | AUROC V T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTThreeCI` | [0.50, 0.59] | AUROC V T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTThreeN` | 46 | AUROC V T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTThreeP` | n/a | AUROC V T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTThreeTprOne` | 8.7 | TPR at 1% FPR (%), V T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTThreeTprOneLo` | 0.0 | TPR at 1% FPR (%), V T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTThreeTprOneHi` | 17.2 | TPR at 1% FPR (%), V T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTThreeTprOneCI` | [0.0, 17.2] | TPR at 1% FPR (%), V T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTThreeTprOneN` | 46 | TPR at 1% FPR (%), V T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTThreeTprOneP` | n/a | TPR at 1% FPR (%), V T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTThreeTprFive` | 8.7 | TPR at 5% FPR (%), V T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTThreeTprFiveLo` | 0.0 | TPR at 5% FPR (%), V T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTThreeTprFiveHi` | 17.2 | TPR at 5% FPR (%), V T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTThreeTprFiveCI` | [0.0, 17.2] | TPR at 5% FPR (%), V T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTThreeTprFiveN` | 46 | TPR at 5% FPR (%), V T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTThreeTprFiveP` | n/a | TPR at 5% FPR (%), V T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTZero` | 0.98 | AUROC C T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTZeroLo` | 0.94 | AUROC C T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTZeroHi` | 1.00 | AUROC C T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTZeroCI` | [0.94, 1.00] | AUROC C T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTZeroN` | 50 | AUROC C T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTZeroP` | n/a | AUROC C T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTZeroTprOne` | 96.0 | TPR at 1% FPR (%), C T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTZeroTprOneLo` | 88.0 | TPR at 1% FPR (%), C T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTZeroTprOneHi` | 100.0 | TPR at 1% FPR (%), C T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTZeroTprOneCI` | [88.0, 100.0] | TPR at 1% FPR (%), C T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTZeroTprOneN` | 50 | TPR at 1% FPR (%), C T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTZeroTprOneP` | n/a | TPR at 1% FPR (%), C T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTZeroTprFive` | 96.0 | TPR at 5% FPR (%), C T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTZeroTprFiveLo` | 88.0 | TPR at 5% FPR (%), C T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTZeroTprFiveHi` | 100.0 | TPR at 5% FPR (%), C T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTZeroTprFiveCI` | [88.0, 100.0] | TPR at 5% FPR (%), C T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTZeroTprFiveN` | 50 | TPR at 5% FPR (%), C T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTZeroTprFiveP` | n/a | TPR at 5% FPR (%), C T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTOne` | 0.98 | AUROC C T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTOneLo` | 0.94 | AUROC C T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTOneHi` | 1.00 | AUROC C T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTOneCI` | [0.94, 1.00] | AUROC C T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTOneN` | 50 | AUROC C T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTOneP` | n/a | AUROC C T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTOneTprOne` | 96.0 | TPR at 1% FPR (%), C T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTOneTprOneLo` | 88.0 | TPR at 1% FPR (%), C T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTOneTprOneHi` | 100.0 | TPR at 1% FPR (%), C T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTOneTprOneCI` | [88.0, 100.0] | TPR at 1% FPR (%), C T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTOneTprOneN` | 50 | TPR at 1% FPR (%), C T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTOneTprOneP` | n/a | TPR at 1% FPR (%), C T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTOneTprFive` | 96.0 | TPR at 5% FPR (%), C T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTOneTprFiveLo` | 88.0 | TPR at 5% FPR (%), C T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTOneTprFiveHi` | 100.0 | TPR at 5% FPR (%), C T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTOneTprFiveCI` | [88.0, 100.0] | TPR at 5% FPR (%), C T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTOneTprFiveN` | 50 | TPR at 5% FPR (%), C T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTOneTprFiveP` | n/a | TPR at 5% FPR (%), C T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTTwo` | 0.98 | AUROC C T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTTwoLo` | 0.94 | AUROC C T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTTwoHi` | 1.00 | AUROC C T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTTwoCI` | [0.94, 1.00] | AUROC C T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTTwoN` | 48 | AUROC C T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTTwoP` | n/a | AUROC C T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTTwoTprOne` | 95.8 | TPR at 1% FPR (%), C T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTTwoTprOneLo` | 87.5 | TPR at 1% FPR (%), C T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTTwoTprOneHi` | 100.0 | TPR at 1% FPR (%), C T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTTwoTprOneCI` | [87.5, 100.0] | TPR at 1% FPR (%), C T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTTwoTprOneN` | 48 | TPR at 1% FPR (%), C T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTTwoTprOneP` | n/a | TPR at 1% FPR (%), C T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTTwoTprFive` | 95.8 | TPR at 5% FPR (%), C T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTTwoTprFiveLo` | 87.5 | TPR at 5% FPR (%), C T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTTwoTprFiveHi` | 100.0 | TPR at 5% FPR (%), C T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTTwoTprFiveCI` | [87.5, 100.0] | TPR at 5% FPR (%), C T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTTwoTprFiveN` | 48 | TPR at 5% FPR (%), C T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTTwoTprFiveP` | n/a | TPR at 5% FPR (%), C T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTThree` | 0.96 | AUROC C T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTThreeLo` | 0.87 | AUROC C T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTThreeHi` | 1.00 | AUROC C T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTThreeCI` | [0.87, 1.00] | AUROC C T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTThreeN` | 46 | AUROC C T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTThreeP` | n/a | AUROC C T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTThreeTprOne` | 91.3 | TPR at 1% FPR (%), C T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTThreeTprOneLo` | 73.9 | TPR at 1% FPR (%), C T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTThreeTprOneHi` | 100.0 | TPR at 1% FPR (%), C T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTThreeTprOneCI` | [73.9, 100.0] | TPR at 1% FPR (%), C T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTThreeTprOneN` | 46 | TPR at 1% FPR (%), C T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTThreeTprOneP` | n/a | TPR at 1% FPR (%), C T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTThreeTprFive` | 91.3 | TPR at 5% FPR (%), C T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTThreeTprFiveLo` | 73.9 | TPR at 5% FPR (%), C T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTThreeTprFiveHi` | 100.0 | TPR at 5% FPR (%), C T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTThreeTprFiveCI` | [73.9, 100.0] | TPR at 5% FPR (%), C T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTThreeTprFiveN` | 46 | TPR at 5% FPR (%), C T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTThreeTprFiveP` | n/a | TPR at 5% FPR (%), C T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTZero` | 1.00 | AUROC R T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTZeroLo` | 0.99 | AUROC R T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTZeroHi` | 1.00 | AUROC R T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTZeroCI` | [0.99, 1.00] | AUROC R T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTZeroN` | 58 | AUROC R T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTZeroP` | n/a | AUROC R T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTZeroTprOne` | 96.6 | TPR at 1% FPR (%), R T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTZeroTprOneLo` | 89.7 | TPR at 1% FPR (%), R T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTZeroTprOneHi` | 100.0 | TPR at 1% FPR (%), R T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTZeroTprOneCI` | [89.7, 100.0] | TPR at 1% FPR (%), R T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTZeroTprOneN` | 58 | TPR at 1% FPR (%), R T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTZeroTprOneP` | n/a | TPR at 1% FPR (%), R T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTZeroTprFive` | 96.6 | TPR at 5% FPR (%), R T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTZeroTprFiveLo` | 89.7 | TPR at 5% FPR (%), R T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTZeroTprFiveHi` | 100.0 | TPR at 5% FPR (%), R T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTZeroTprFiveCI` | [89.7, 100.0] | TPR at 5% FPR (%), R T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTZeroTprFiveN` | 58 | TPR at 5% FPR (%), R T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTZeroTprFiveP` | n/a | TPR at 5% FPR (%), R T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTOne` | 1.00 | AUROC R T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTOneLo` | 1.00 | AUROC R T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTOneHi` | 1.00 | AUROC R T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTOneCI` | [1.00, 1.00] | AUROC R T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTOneN` | 58 | AUROC R T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTOneP` | n/a | AUROC R T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTOneTprOne` | 100.0 | TPR at 1% FPR (%), R T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTOneTprOneLo` | 100.0 | TPR at 1% FPR (%), R T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTOneTprOneHi` | 100.0 | TPR at 1% FPR (%), R T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTOneTprOneCI` | [100.0, 100.0] | TPR at 1% FPR (%), R T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTOneTprOneN` | 58 | TPR at 1% FPR (%), R T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTOneTprOneP` | n/a | TPR at 1% FPR (%), R T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTOneTprFive` | 100.0 | TPR at 5% FPR (%), R T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTOneTprFiveLo` | 100.0 | TPR at 5% FPR (%), R T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTOneTprFiveHi` | 100.0 | TPR at 5% FPR (%), R T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTOneTprFiveCI` | [100.0, 100.0] | TPR at 5% FPR (%), R T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTOneTprFiveN` | 58 | TPR at 5% FPR (%), R T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTOneTprFiveP` | n/a | TPR at 5% FPR (%), R T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTTwo` | 1.00 | AUROC R T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTTwoLo` | 0.99 | AUROC R T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTTwoHi` | 1.00 | AUROC R T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTTwoCI` | [0.99, 1.00] | AUROC R T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTTwoN` | 56 | AUROC R T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTTwoP` | n/a | AUROC R T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTTwoTprOne` | 96.4 | TPR at 1% FPR (%), R T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTTwoTprOneLo` | 89.3 | TPR at 1% FPR (%), R T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTTwoTprOneHi` | 100.0 | TPR at 1% FPR (%), R T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTTwoTprOneCI` | [89.3, 100.0] | TPR at 1% FPR (%), R T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTTwoTprOneN` | 56 | TPR at 1% FPR (%), R T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTTwoTprOneP` | n/a | TPR at 1% FPR (%), R T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTTwoTprFive` | 96.4 | TPR at 5% FPR (%), R T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTTwoTprFiveLo` | 89.3 | TPR at 5% FPR (%), R T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTTwoTprFiveHi` | 100.0 | TPR at 5% FPR (%), R T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTTwoTprFiveCI` | [89.3, 100.0] | TPR at 5% FPR (%), R T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTTwoTprFiveN` | 56 | TPR at 5% FPR (%), R T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTTwoTprFiveP` | n/a | TPR at 5% FPR (%), R T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTThree` | 1.00 | AUROC R T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTThreeLo` | 1.00 | AUROC R T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTThreeHi` | 1.00 | AUROC R T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTThreeCI` | [1.00, 1.00] | AUROC R T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTThreeN` | 54 | AUROC R T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTThreeP` | n/a | AUROC R T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTThreeTprOne` | 96.3 | TPR at 1% FPR (%), R T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTThreeTprOneLo` | 89.3 | TPR at 1% FPR (%), R T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTThreeTprOneHi` | 100.0 | TPR at 1% FPR (%), R T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTThreeTprOneCI` | [89.3, 100.0] | TPR at 1% FPR (%), R T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTThreeTprOneN` | 54 | TPR at 1% FPR (%), R T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTThreeTprOneP` | n/a | TPR at 1% FPR (%), R T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTThreeTprFive` | 96.3 | TPR at 5% FPR (%), R T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTThreeTprFiveLo` | 92.9 | TPR at 5% FPR (%), R T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTThreeTprFiveHi` | 100.0 | TPR at 5% FPR (%), R T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTThreeTprFiveCI` | [92.9, 100.0] | TPR at 5% FPR (%), R T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTThreeTprFiveN` | 54 | TPR at 5% FPR (%), R T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTThreeTprFiveP` | n/a | TPR at 5% FPR (%), R T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTZero` | 0.67 | AUROC r_field T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTZeroLo` | 0.59 | AUROC r_field T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTZeroHi` | 0.74 | AUROC r_field T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTZeroCI` | [0.59, 0.74] | AUROC r_field T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTZeroN` | 58 | AUROC r_field T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTZeroP` | n/a | AUROC r_field T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTZeroTprOne` | 13.8 | TPR at 1% FPR (%), r_field T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTZeroTprOneLo` | 3.4 | TPR at 1% FPR (%), r_field T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTZeroTprOneHi` | 26.7 | TPR at 1% FPR (%), r_field T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTZeroTprOneCI` | [3.4, 26.7] | TPR at 1% FPR (%), r_field T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTZeroTprOneN` | 58 | TPR at 1% FPR (%), r_field T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTZeroTprOneP` | n/a | TPR at 1% FPR (%), r_field T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTZeroTprFive` | 13.8 | TPR at 5% FPR (%), r_field T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTZeroTprFiveLo` | 3.4 | TPR at 5% FPR (%), r_field T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTZeroTprFiveHi` | 34.5 | TPR at 5% FPR (%), r_field T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTZeroTprFiveCI` | [3.4, 34.5] | TPR at 5% FPR (%), r_field T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTZeroTprFiveN` | 58 | TPR at 5% FPR (%), r_field T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTZeroTprFiveP` | n/a | TPR at 5% FPR (%), r_field T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTOne` | 0.67 | AUROC r_field T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTOneLo` | 0.59 | AUROC r_field T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTOneHi` | 0.75 | AUROC r_field T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTOneCI` | [0.59, 0.75] | AUROC r_field T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTOneN` | 58 | AUROC r_field T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTOneP` | n/a | AUROC r_field T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTOneTprOne` | 17.2 | TPR at 1% FPR (%), r_field T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTOneTprOneLo` | 7.1 | TPR at 1% FPR (%), r_field T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTOneTprOneHi` | 30.0 | TPR at 1% FPR (%), r_field T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTOneTprOneCI` | [7.1, 30.0] | TPR at 1% FPR (%), r_field T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTOneTprOneN` | 58 | TPR at 1% FPR (%), r_field T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTOneTprOneP` | n/a | TPR at 1% FPR (%), r_field T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTOneTprFive` | 17.2 | TPR at 5% FPR (%), r_field T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTOneTprFiveLo` | 7.4 | TPR at 5% FPR (%), r_field T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTOneTprFiveHi` | 44.8 | TPR at 5% FPR (%), r_field T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTOneTprFiveCI` | [7.4, 44.8] | TPR at 5% FPR (%), r_field T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTOneTprFiveN` | 58 | TPR at 5% FPR (%), r_field T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTOneTprFiveP` | n/a | TPR at 5% FPR (%), r_field T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTTwo` | 0.68 | AUROC r_field T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTTwoLo` | 0.60 | AUROC r_field T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTTwoHi` | 0.77 | AUROC r_field T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTTwoCI` | [0.60, 0.77] | AUROC r_field T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTTwoN` | 56 | AUROC r_field T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTTwoP` | n/a | AUROC r_field T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTTwoTprOne` | 17.9 | TPR at 1% FPR (%), r_field T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTTwoTprOneLo` | 7.7 | TPR at 1% FPR (%), r_field T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTTwoTprOneHi` | 30.0 | TPR at 1% FPR (%), r_field T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTTwoTprOneCI` | [7.7, 30.0] | TPR at 1% FPR (%), r_field T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTTwoTprOneN` | 56 | TPR at 1% FPR (%), r_field T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTTwoTprOneP` | n/a | TPR at 1% FPR (%), r_field T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTTwoTprFive` | 17.9 | TPR at 5% FPR (%), r_field T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTTwoTprFiveLo` | 11.1 | TPR at 5% FPR (%), r_field T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTTwoTprFiveHi` | 48.2 | TPR at 5% FPR (%), r_field T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTTwoTprFiveCI` | [11.1, 48.2] | TPR at 5% FPR (%), r_field T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTTwoTprFiveN` | 56 | TPR at 5% FPR (%), r_field T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTTwoTprFiveP` | n/a | TPR at 5% FPR (%), r_field T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTThree` | 0.69 | AUROC r_field T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTThreeLo` | 0.60 | AUROC r_field T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTThreeHi` | 0.78 | AUROC r_field T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTThreeCI` | [0.60, 0.78] | AUROC r_field T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTThreeN` | 54 | AUROC r_field T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTThreeP` | n/a | AUROC r_field T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTThreeTprOne` | 18.5 | TPR at 1% FPR (%), r_field T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTThreeTprOneLo` | 8.0 | TPR at 1% FPR (%), r_field T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTThreeTprOneHi` | 31.0 | TPR at 1% FPR (%), r_field T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTThreeTprOneCI` | [8.0, 31.0] | TPR at 1% FPR (%), r_field T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTThreeTprOneN` | 54 | TPR at 1% FPR (%), r_field T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTThreeTprOneP` | n/a | TPR at 1% FPR (%), r_field T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTThreeTprFive` | 18.5 | TPR at 5% FPR (%), r_field T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTThreeTprFiveLo` | 8.0 | TPR at 5% FPR (%), r_field T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTThreeTprFiveHi` | 52.0 | TPR at 5% FPR (%), r_field T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTThreeTprFiveCI` | [8.0, 52.0] | TPR at 5% FPR (%), r_field T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTThreeTprFiveN` | 54 | TPR at 5% FPR (%), r_field T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTThreeTprFiveP` | n/a | TPR at 5% FPR (%), r_field T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTZero` | 0.68 | AUROC f_trace T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTZeroLo` | 0.64 | AUROC f_trace T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTZeroHi` | 0.71 | AUROC f_trace T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTZeroCI` | [0.64, 0.71] | AUROC f_trace T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTZeroN` | 58 | AUROC f_trace T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTZeroP` | n/a | AUROC f_trace T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTZeroTprOne` | 13.8 | TPR at 1% FPR (%), f_trace T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTZeroTprOneLo` | 7.4 | TPR at 1% FPR (%), f_trace T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTZeroTprOneHi` | 37.9 | TPR at 1% FPR (%), f_trace T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTZeroTprOneCI` | [7.4, 37.9] | TPR at 1% FPR (%), f_trace T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTZeroTprOneN` | 58 | TPR at 1% FPR (%), f_trace T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTZeroTprOneP` | n/a | TPR at 1% FPR (%), f_trace T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTZeroTprFive` | 31.0 | TPR at 5% FPR (%), f_trace T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTZeroTprFiveLo` | 14.8 | TPR at 5% FPR (%), f_trace T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTZeroTprFiveHi` | 40.0 | TPR at 5% FPR (%), f_trace T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTZeroTprFiveCI` | [14.8, 40.0] | TPR at 5% FPR (%), f_trace T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTZeroTprFiveN` | 58 | TPR at 5% FPR (%), f_trace T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTZeroTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTOne` | 0.68 | AUROC f_trace T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTOneLo` | 0.64 | AUROC f_trace T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTOneHi` | 0.72 | AUROC f_trace T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTOneCI` | [0.64, 0.72] | AUROC f_trace T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTOneN` | 58 | AUROC f_trace T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTOneP` | n/a | AUROC f_trace T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTOneTprOne` | 20.7 | TPR at 1% FPR (%), f_trace T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTOneTprOneLo` | 17.9 | TPR at 1% FPR (%), f_trace T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTOneTprOneHi` | 37.9 | TPR at 1% FPR (%), f_trace T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTOneTprOneCI` | [17.9, 37.9] | TPR at 1% FPR (%), f_trace T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTOneTprOneN` | 58 | TPR at 1% FPR (%), f_trace T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTOneTprOneP` | n/a | TPR at 1% FPR (%), f_trace T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTOneTprFive` | 31.0 | TPR at 5% FPR (%), f_trace T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTOneTprFiveLo` | 21.4 | TPR at 5% FPR (%), f_trace T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTOneTprFiveHi` | 40.0 | TPR at 5% FPR (%), f_trace T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTOneTprFiveCI` | [21.4, 40.0] | TPR at 5% FPR (%), f_trace T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTOneTprFiveN` | 58 | TPR at 5% FPR (%), f_trace T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTOneTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTTwo` | 0.68 | AUROC f_trace T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTTwoLo` | 0.64 | AUROC f_trace T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTTwoHi` | 0.73 | AUROC f_trace T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTTwoCI` | [0.64, 0.73] | AUROC f_trace T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTTwoN` | 56 | AUROC f_trace T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTTwoP` | n/a | AUROC f_trace T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTTwoTprOne` | 21.4 | TPR at 1% FPR (%), f_trace T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTTwoTprOneLo` | 17.9 | TPR at 1% FPR (%), f_trace T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTTwoTprOneHi` | 41.4 | TPR at 1% FPR (%), f_trace T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTTwoTprOneCI` | [17.9, 41.4] | TPR at 1% FPR (%), f_trace T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTTwoTprOneN` | 56 | TPR at 1% FPR (%), f_trace T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTTwoTprOneP` | n/a | TPR at 1% FPR (%), f_trace T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTTwoTprFive` | 32.1 | TPR at 5% FPR (%), f_trace T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTTwoTprFiveLo` | 21.4 | TPR at 5% FPR (%), f_trace T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTTwoTprFiveHi` | 41.4 | TPR at 5% FPR (%), f_trace T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTTwoTprFiveCI` | [21.4, 41.4] | TPR at 5% FPR (%), f_trace T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTTwoTprFiveN` | 56 | TPR at 5% FPR (%), f_trace T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTTwoTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTThree` | 0.69 | AUROC f_trace T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTThreeLo` | 0.64 | AUROC f_trace T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTThreeHi` | 0.74 | AUROC f_trace T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTThreeCI` | [0.64, 0.74] | AUROC f_trace T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTThreeN` | 54 | AUROC f_trace T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTThreeP` | n/a | AUROC f_trace T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTThreeTprOne` | 22.2 | TPR at 1% FPR (%), f_trace T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTThreeTprOneLo` | 17.9 | TPR at 1% FPR (%), f_trace T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTThreeTprOneHi` | 44.0 | TPR at 1% FPR (%), f_trace T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTThreeTprOneCI` | [17.9, 44.0] | TPR at 1% FPR (%), f_trace T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTThreeTprOneN` | 54 | TPR at 1% FPR (%), f_trace T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTThreeTprOneP` | n/a | TPR at 1% FPR (%), f_trace T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTThreeTprFive` | 33.3 | TPR at 5% FPR (%), f_trace T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTThreeTprFiveLo` | 22.2 | TPR at 5% FPR (%), f_trace T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTThreeTprFiveHi` | 44.4 | TPR at 5% FPR (%), f_trace T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTThreeTprFiveCI` | [22.2, 44.4] | TPR at 5% FPR (%), f_trace T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTThreeTprFiveN` | 54 | TPR at 5% FPR (%), f_trace T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTThreeTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatPooledCTZero` | 14.5 | flat-audit rate (%): all 7 entries same score, C, T0 stores, pooled |
| `\DetFlatPooledCTZeroLo` | 5.5 | flat-audit rate (%): all 7 entries same score, C, T0 stores, pooled, lower 95% CI bound |
| `\DetFlatPooledCTZeroHi` | 27.3 | flat-audit rate (%): all 7 entries same score, C, T0 stores, pooled, upper 95% CI bound |
| `\DetFlatPooledCTZeroCI` | [5.5, 27.3] | flat-audit rate (%): all 7 entries same score, C, T0 stores, pooled, 95% CI |
| `\DetFlatPooledCTZeroN` | 55 | flat-audit rate (%): all 7 entries same score, C, T0 stores, pooled, n |
| `\DetFlatPooledCTZeroP` | n/a | flat-audit rate (%): all 7 entries same score, C, T0 stores, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatDeepSeekVFourFlashCTZero` | 23.3 | flat-audit rate (%): all 7 entries same score, C, T0 stores, deepseek-v4-flash |
| `\DetFlatDeepSeekVFourFlashCTZeroLo` | 10.0 | flat-audit rate (%): all 7 entries same score, C, T0 stores, deepseek-v4-flash, lower 95% CI bound |
| `\DetFlatDeepSeekVFourFlashCTZeroHi` | 40.0 | flat-audit rate (%): all 7 entries same score, C, T0 stores, deepseek-v4-flash, upper 95% CI bound |
| `\DetFlatDeepSeekVFourFlashCTZeroCI` | [10.0, 40.0] | flat-audit rate (%): all 7 entries same score, C, T0 stores, deepseek-v4-flash, 95% CI |
| `\DetFlatDeepSeekVFourFlashCTZeroN` | 30 | flat-audit rate (%): all 7 entries same score, C, T0 stores, deepseek-v4-flash, n |
| `\DetFlatDeepSeekVFourFlashCTZeroP` | n/a | flat-audit rate (%): all 7 entries same score, C, T0 stores, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGemmaFourThreeOneBCTZero` | 4.0 | flat-audit rate (%): all 7 entries same score, C, T0 stores, gemma-4-31b-it |
| `\DetFlatGemmaFourThreeOneBCTZeroLo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T0 stores, gemma-4-31b-it, lower 95% CI bound |
| `\DetFlatGemmaFourThreeOneBCTZeroHi` | 12.0 | flat-audit rate (%): all 7 entries same score, C, T0 stores, gemma-4-31b-it, upper 95% CI bound |
| `\DetFlatGemmaFourThreeOneBCTZeroCI` | [0.0, 12.0] | flat-audit rate (%): all 7 entries same score, C, T0 stores, gemma-4-31b-it, 95% CI |
| `\DetFlatGemmaFourThreeOneBCTZeroN` | 25 | flat-audit rate (%): all 7 entries same score, C, T0 stores, gemma-4-31b-it, n |
| `\DetFlatGemmaFourThreeOneBCTZeroP` | n/a | flat-audit rate (%): all 7 entries same score, C, T0 stores, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatPooledCTOne` | 12.0 | flat-audit rate (%): all 7 entries same score, C, T1 stores, pooled |
| `\DetFlatPooledCTOneLo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T1 stores, pooled, lower 95% CI bound |
| `\DetFlatPooledCTOneHi` | 28.0 | flat-audit rate (%): all 7 entries same score, C, T1 stores, pooled, upper 95% CI bound |
| `\DetFlatPooledCTOneCI` | [0.0, 28.0] | flat-audit rate (%): all 7 entries same score, C, T1 stores, pooled, 95% CI |
| `\DetFlatPooledCTOneN` | 50 | flat-audit rate (%): all 7 entries same score, C, T1 stores, pooled, n |
| `\DetFlatPooledCTOneP` | n/a | flat-audit rate (%): all 7 entries same score, C, T1 stores, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatDeepSeekVFourFlashCTOne` | 20.0 | flat-audit rate (%): all 7 entries same score, C, T1 stores, deepseek-v4-flash |
| `\DetFlatDeepSeekVFourFlashCTOneLo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T1 stores, deepseek-v4-flash, lower 95% CI bound |
| `\DetFlatDeepSeekVFourFlashCTOneHi` | 44.0 | flat-audit rate (%): all 7 entries same score, C, T1 stores, deepseek-v4-flash, upper 95% CI bound |
| `\DetFlatDeepSeekVFourFlashCTOneCI` | [0.0, 44.0] | flat-audit rate (%): all 7 entries same score, C, T1 stores, deepseek-v4-flash, 95% CI |
| `\DetFlatDeepSeekVFourFlashCTOneN` | 25 | flat-audit rate (%): all 7 entries same score, C, T1 stores, deepseek-v4-flash, n |
| `\DetFlatDeepSeekVFourFlashCTOneP` | n/a | flat-audit rate (%): all 7 entries same score, C, T1 stores, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGemmaFourThreeOneBCTOne` | 4.0 | flat-audit rate (%): all 7 entries same score, C, T1 stores, gemma-4-31b-it |
| `\DetFlatGemmaFourThreeOneBCTOneLo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T1 stores, gemma-4-31b-it, lower 95% CI bound |
| `\DetFlatGemmaFourThreeOneBCTOneHi` | 12.0 | flat-audit rate (%): all 7 entries same score, C, T1 stores, gemma-4-31b-it, upper 95% CI bound |
| `\DetFlatGemmaFourThreeOneBCTOneCI` | [0.0, 12.0] | flat-audit rate (%): all 7 entries same score, C, T1 stores, gemma-4-31b-it, 95% CI |
| `\DetFlatGemmaFourThreeOneBCTOneN` | 25 | flat-audit rate (%): all 7 entries same score, C, T1 stores, gemma-4-31b-it, n |
| `\DetFlatGemmaFourThreeOneBCTOneP` | n/a | flat-audit rate (%): all 7 entries same score, C, T1 stores, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatPooledCTTwo` | 9.3 | flat-audit rate (%): all 7 entries same score, C, T2 stores, pooled |
| `\DetFlatPooledCTTwoLo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T2 stores, pooled, lower 95% CI bound |
| `\DetFlatPooledCTTwoHi` | 24.1 | flat-audit rate (%): all 7 entries same score, C, T2 stores, pooled, upper 95% CI bound |
| `\DetFlatPooledCTTwoCI` | [0.0, 24.1] | flat-audit rate (%): all 7 entries same score, C, T2 stores, pooled, 95% CI |
| `\DetFlatPooledCTTwoN` | 54 | flat-audit rate (%): all 7 entries same score, C, T2 stores, pooled, n |
| `\DetFlatPooledCTTwoP` | n/a | flat-audit rate (%): all 7 entries same score, C, T2 stores, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatDeepSeekVFourFlashCTTwo` | 13.3 | flat-audit rate (%): all 7 entries same score, C, T2 stores, deepseek-v4-flash |
| `\DetFlatDeepSeekVFourFlashCTTwoLo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T2 stores, deepseek-v4-flash, lower 95% CI bound |
| `\DetFlatDeepSeekVFourFlashCTTwoHi` | 33.3 | flat-audit rate (%): all 7 entries same score, C, T2 stores, deepseek-v4-flash, upper 95% CI bound |
| `\DetFlatDeepSeekVFourFlashCTTwoCI` | [0.0, 33.3] | flat-audit rate (%): all 7 entries same score, C, T2 stores, deepseek-v4-flash, 95% CI |
| `\DetFlatDeepSeekVFourFlashCTTwoN` | 30 | flat-audit rate (%): all 7 entries same score, C, T2 stores, deepseek-v4-flash, n |
| `\DetFlatDeepSeekVFourFlashCTTwoP` | n/a | flat-audit rate (%): all 7 entries same score, C, T2 stores, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGemmaFourThreeOneBCTTwo` | 4.2 | flat-audit rate (%): all 7 entries same score, C, T2 stores, gemma-4-31b-it |
| `\DetFlatGemmaFourThreeOneBCTTwoLo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T2 stores, gemma-4-31b-it, lower 95% CI bound |
| `\DetFlatGemmaFourThreeOneBCTTwoHi` | 12.5 | flat-audit rate (%): all 7 entries same score, C, T2 stores, gemma-4-31b-it, upper 95% CI bound |
| `\DetFlatGemmaFourThreeOneBCTTwoCI` | [0.0, 12.5] | flat-audit rate (%): all 7 entries same score, C, T2 stores, gemma-4-31b-it, 95% CI |
| `\DetFlatGemmaFourThreeOneBCTTwoN` | 24 | flat-audit rate (%): all 7 entries same score, C, T2 stores, gemma-4-31b-it, n |
| `\DetFlatGemmaFourThreeOneBCTTwoP` | n/a | flat-audit rate (%): all 7 entries same score, C, T2 stores, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatPooledCTThree` | 11.5 | flat-audit rate (%): all 7 entries same score, C, T3 stores, pooled |
| `\DetFlatPooledCTThreeLo` | 1.7 | flat-audit rate (%): all 7 entries same score, C, T3 stores, pooled, lower 95% CI bound |
| `\DetFlatPooledCTThreeHi` | 26.2 | flat-audit rate (%): all 7 entries same score, C, T3 stores, pooled, upper 95% CI bound |
| `\DetFlatPooledCTThreeCI` | [1.7, 26.2] | flat-audit rate (%): all 7 entries same score, C, T3 stores, pooled, 95% CI |
| `\DetFlatPooledCTThreeN` | 52 | flat-audit rate (%): all 7 entries same score, C, T3 stores, pooled, n |
| `\DetFlatPooledCTThreeP` | n/a | flat-audit rate (%): all 7 entries same score, C, T3 stores, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatDeepSeekVFourFlashCTThree` | 13.8 | flat-audit rate (%): all 7 entries same score, C, T3 stores, deepseek-v4-flash |
| `\DetFlatDeepSeekVFourFlashCTThreeLo` | 3.3 | flat-audit rate (%): all 7 entries same score, C, T3 stores, deepseek-v4-flash, lower 95% CI bound |
| `\DetFlatDeepSeekVFourFlashCTThreeHi` | 29.6 | flat-audit rate (%): all 7 entries same score, C, T3 stores, deepseek-v4-flash, upper 95% CI bound |
| `\DetFlatDeepSeekVFourFlashCTThreeCI` | [3.3, 29.6] | flat-audit rate (%): all 7 entries same score, C, T3 stores, deepseek-v4-flash, 95% CI |
| `\DetFlatDeepSeekVFourFlashCTThreeN` | 29 | flat-audit rate (%): all 7 entries same score, C, T3 stores, deepseek-v4-flash, n |
| `\DetFlatDeepSeekVFourFlashCTThreeP` | n/a | flat-audit rate (%): all 7 entries same score, C, T3 stores, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGemmaFourThreeOneBCTThree` | 8.7 | flat-audit rate (%): all 7 entries same score, C, T3 stores, gemma-4-31b-it |
| `\DetFlatGemmaFourThreeOneBCTThreeLo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T3 stores, gemma-4-31b-it, lower 95% CI bound |
| `\DetFlatGemmaFourThreeOneBCTThreeHi` | 25.0 | flat-audit rate (%): all 7 entries same score, C, T3 stores, gemma-4-31b-it, upper 95% CI bound |
| `\DetFlatGemmaFourThreeOneBCTThreeCI` | [0.0, 25.0] | flat-audit rate (%): all 7 entries same score, C, T3 stores, gemma-4-31b-it, 95% CI |
| `\DetFlatGemmaFourThreeOneBCTThreeN` | 23 | flat-audit rate (%): all 7 entries same score, C, T3 stores, gemma-4-31b-it, n |
| `\DetFlatGemmaFourThreeOneBCTThreeP` | n/a | flat-audit rate (%): all 7 entries same score, C, T3 stores, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatPooledCClean` | 100.0 | flat-audit rate (%): all 7 entries same score, C, clean stores, pooled |
| `\DetFlatPooledCCleanLo` | 71.5 | flat-audit rate (%): all 7 entries same score, C, clean stores, pooled, lower 95% CI bound |
| `\DetFlatPooledCCleanHi` | 100.0 | flat-audit rate (%): all 7 entries same score, C, clean stores, pooled, upper 95% CI bound |
| `\DetFlatPooledCCleanCI` | [71.5, 100.0] | flat-audit rate (%): all 7 entries same score, C, clean stores, pooled, 95% CI |
| `\DetFlatPooledCCleanN` | 11 | flat-audit rate (%): all 7 entries same score, C, clean stores, pooled, n |
| `\DetFlatPooledCCleanP` | n/a | flat-audit rate (%): all 7 entries same score, C, clean stores, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatDeepSeekVFourFlashCClean` | 100.0 | flat-audit rate (%): all 7 entries same score, C, clean stores, deepseek-v4-flash |
| `\DetFlatDeepSeekVFourFlashCCleanLo` | 54.1 | flat-audit rate (%): all 7 entries same score, C, clean stores, deepseek-v4-flash, lower 95% CI bound |
| `\DetFlatDeepSeekVFourFlashCCleanHi` | 100.0 | flat-audit rate (%): all 7 entries same score, C, clean stores, deepseek-v4-flash, upper 95% CI bound |
| `\DetFlatDeepSeekVFourFlashCCleanCI` | [54.1, 100.0] | flat-audit rate (%): all 7 entries same score, C, clean stores, deepseek-v4-flash, 95% CI |
| `\DetFlatDeepSeekVFourFlashCCleanN` | 6 | flat-audit rate (%): all 7 entries same score, C, clean stores, deepseek-v4-flash, n |
| `\DetFlatDeepSeekVFourFlashCCleanP` | n/a | flat-audit rate (%): all 7 entries same score, C, clean stores, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGemmaFourThreeOneBCClean` | 100.0 | flat-audit rate (%): all 7 entries same score, C, clean stores, gemma-4-31b-it |
| `\DetFlatGemmaFourThreeOneBCCleanLo` | 47.8 | flat-audit rate (%): all 7 entries same score, C, clean stores, gemma-4-31b-it, lower 95% CI bound |
| `\DetFlatGemmaFourThreeOneBCCleanHi` | 100.0 | flat-audit rate (%): all 7 entries same score, C, clean stores, gemma-4-31b-it, upper 95% CI bound |
| `\DetFlatGemmaFourThreeOneBCCleanCI` | [47.8, 100.0] | flat-audit rate (%): all 7 entries same score, C, clean stores, gemma-4-31b-it, 95% CI |
| `\DetFlatGemmaFourThreeOneBCCleanN` | 5 | flat-audit rate (%): all 7 entries same score, C, clean stores, gemma-4-31b-it, n |
| `\DetFlatGemmaFourThreeOneBCCleanP` | n/a | flat-audit rate (%): all 7 entries same score, C, clean stores, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatPooledVTZero` | 67.3 | flat-audit rate (%): all 7 entries same score, V, T0 stores, pooled |
| `\DetFlatPooledVTZeroLo` | 41.7 | flat-audit rate (%): all 7 entries same score, V, T0 stores, pooled, lower 95% CI bound |
| `\DetFlatPooledVTZeroHi` | 94.0 | flat-audit rate (%): all 7 entries same score, V, T0 stores, pooled, upper 95% CI bound |
| `\DetFlatPooledVTZeroCI` | [41.7, 94.0] | flat-audit rate (%): all 7 entries same score, V, T0 stores, pooled, 95% CI |
| `\DetFlatPooledVTZeroN` | 55 | flat-audit rate (%): all 7 entries same score, V, T0 stores, pooled, n |
| `\DetFlatPooledVTZeroP` | n/a | flat-audit rate (%): all 7 entries same score, V, T0 stores, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatDeepSeekVFourFlashVTZero` | 60.0 | flat-audit rate (%): all 7 entries same score, V, T0 stores, deepseek-v4-flash |
| `\DetFlatDeepSeekVFourFlashVTZeroLo` | 26.7 | flat-audit rate (%): all 7 entries same score, V, T0 stores, deepseek-v4-flash, lower 95% CI bound |
| `\DetFlatDeepSeekVFourFlashVTZeroHi` | 93.3 | flat-audit rate (%): all 7 entries same score, V, T0 stores, deepseek-v4-flash, upper 95% CI bound |
| `\DetFlatDeepSeekVFourFlashVTZeroCI` | [26.7, 93.3] | flat-audit rate (%): all 7 entries same score, V, T0 stores, deepseek-v4-flash, 95% CI |
| `\DetFlatDeepSeekVFourFlashVTZeroN` | 30 | flat-audit rate (%): all 7 entries same score, V, T0 stores, deepseek-v4-flash, n |
| `\DetFlatDeepSeekVFourFlashVTZeroP` | n/a | flat-audit rate (%): all 7 entries same score, V, T0 stores, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGemmaFourThreeOneBVTZero` | 76.0 | flat-audit rate (%): all 7 entries same score, V, T0 stores, gemma-4-31b-it |
| `\DetFlatGemmaFourThreeOneBVTZeroLo` | 56.0 | flat-audit rate (%): all 7 entries same score, V, T0 stores, gemma-4-31b-it, lower 95% CI bound |
| `\DetFlatGemmaFourThreeOneBVTZeroHi` | 96.0 | flat-audit rate (%): all 7 entries same score, V, T0 stores, gemma-4-31b-it, upper 95% CI bound |
| `\DetFlatGemmaFourThreeOneBVTZeroCI` | [56.0, 96.0] | flat-audit rate (%): all 7 entries same score, V, T0 stores, gemma-4-31b-it, 95% CI |
| `\DetFlatGemmaFourThreeOneBVTZeroN` | 25 | flat-audit rate (%): all 7 entries same score, V, T0 stores, gemma-4-31b-it, n |
| `\DetFlatGemmaFourThreeOneBVTZeroP` | n/a | flat-audit rate (%): all 7 entries same score, V, T0 stores, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatPooledVTOne` | 80.0 | flat-audit rate (%): all 7 entries same score, V, T1 stores, pooled |
| `\DetFlatPooledVTOneLo` | 60.0 | flat-audit rate (%): all 7 entries same score, V, T1 stores, pooled, lower 95% CI bound |
| `\DetFlatPooledVTOneHi` | 100.0 | flat-audit rate (%): all 7 entries same score, V, T1 stores, pooled, upper 95% CI bound |
| `\DetFlatPooledVTOneCI` | [60.0, 100.0] | flat-audit rate (%): all 7 entries same score, V, T1 stores, pooled, 95% CI |
| `\DetFlatPooledVTOneN` | 50 | flat-audit rate (%): all 7 entries same score, V, T1 stores, pooled, n |
| `\DetFlatPooledVTOneP` | n/a | flat-audit rate (%): all 7 entries same score, V, T1 stores, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatDeepSeekVFourFlashVTOne` | 60.0 | flat-audit rate (%): all 7 entries same score, V, T1 stores, deepseek-v4-flash |
| `\DetFlatDeepSeekVFourFlashVTOneLo` | 20.0 | flat-audit rate (%): all 7 entries same score, V, T1 stores, deepseek-v4-flash, lower 95% CI bound |
| `\DetFlatDeepSeekVFourFlashVTOneHi` | 100.0 | flat-audit rate (%): all 7 entries same score, V, T1 stores, deepseek-v4-flash, upper 95% CI bound |
| `\DetFlatDeepSeekVFourFlashVTOneCI` | [20.0, 100.0] | flat-audit rate (%): all 7 entries same score, V, T1 stores, deepseek-v4-flash, 95% CI |
| `\DetFlatDeepSeekVFourFlashVTOneN` | 25 | flat-audit rate (%): all 7 entries same score, V, T1 stores, deepseek-v4-flash, n |
| `\DetFlatDeepSeekVFourFlashVTOneP` | n/a | flat-audit rate (%): all 7 entries same score, V, T1 stores, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGemmaFourThreeOneBVTOne` | 100.0 | flat-audit rate (%): all 7 entries same score, V, T1 stores, gemma-4-31b-it |
| `\DetFlatGemmaFourThreeOneBVTOneLo` | 86.3 | flat-audit rate (%): all 7 entries same score, V, T1 stores, gemma-4-31b-it, lower 95% CI bound |
| `\DetFlatGemmaFourThreeOneBVTOneHi` | 100.0 | flat-audit rate (%): all 7 entries same score, V, T1 stores, gemma-4-31b-it, upper 95% CI bound |
| `\DetFlatGemmaFourThreeOneBVTOneCI` | [86.3, 100.0] | flat-audit rate (%): all 7 entries same score, V, T1 stores, gemma-4-31b-it, 95% CI |
| `\DetFlatGemmaFourThreeOneBVTOneN` | 25 | flat-audit rate (%): all 7 entries same score, V, T1 stores, gemma-4-31b-it, n |
| `\DetFlatGemmaFourThreeOneBVTOneP` | n/a | flat-audit rate (%): all 7 entries same score, V, T1 stores, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatPooledVTTwo` | 79.6 | flat-audit rate (%): all 7 entries same score, V, T2 stores, pooled |
| `\DetFlatPooledVTTwoLo` | 58.2 | flat-audit rate (%): all 7 entries same score, V, T2 stores, pooled, lower 95% CI bound |
| `\DetFlatPooledVTTwoHi` | 100.0 | flat-audit rate (%): all 7 entries same score, V, T2 stores, pooled, upper 95% CI bound |
| `\DetFlatPooledVTTwoCI` | [58.2, 100.0] | flat-audit rate (%): all 7 entries same score, V, T2 stores, pooled, 95% CI |
| `\DetFlatPooledVTTwoN` | 54 | flat-audit rate (%): all 7 entries same score, V, T2 stores, pooled, n |
| `\DetFlatPooledVTTwoP` | n/a | flat-audit rate (%): all 7 entries same score, V, T2 stores, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatDeepSeekVFourFlashVTTwo` | 70.0 | flat-audit rate (%): all 7 entries same score, V, T2 stores, deepseek-v4-flash |
| `\DetFlatDeepSeekVFourFlashVTTwoLo` | 36.6 | flat-audit rate (%): all 7 entries same score, V, T2 stores, deepseek-v4-flash, lower 95% CI bound |
| `\DetFlatDeepSeekVFourFlashVTTwoHi` | 100.0 | flat-audit rate (%): all 7 entries same score, V, T2 stores, deepseek-v4-flash, upper 95% CI bound |
| `\DetFlatDeepSeekVFourFlashVTTwoCI` | [36.6, 100.0] | flat-audit rate (%): all 7 entries same score, V, T2 stores, deepseek-v4-flash, 95% CI |
| `\DetFlatDeepSeekVFourFlashVTTwoN` | 30 | flat-audit rate (%): all 7 entries same score, V, T2 stores, deepseek-v4-flash, n |
| `\DetFlatDeepSeekVFourFlashVTTwoP` | n/a | flat-audit rate (%): all 7 entries same score, V, T2 stores, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGemmaFourThreeOneBVTTwo` | 91.7 | flat-audit rate (%): all 7 entries same score, V, T2 stores, gemma-4-31b-it |
| `\DetFlatGemmaFourThreeOneBVTTwoLo` | 83.3 | flat-audit rate (%): all 7 entries same score, V, T2 stores, gemma-4-31b-it, lower 95% CI bound |
| `\DetFlatGemmaFourThreeOneBVTTwoHi` | 100.0 | flat-audit rate (%): all 7 entries same score, V, T2 stores, gemma-4-31b-it, upper 95% CI bound |
| `\DetFlatGemmaFourThreeOneBVTTwoCI` | [83.3, 100.0] | flat-audit rate (%): all 7 entries same score, V, T2 stores, gemma-4-31b-it, 95% CI |
| `\DetFlatGemmaFourThreeOneBVTTwoN` | 24 | flat-audit rate (%): all 7 entries same score, V, T2 stores, gemma-4-31b-it, n |
| `\DetFlatGemmaFourThreeOneBVTTwoP` | n/a | flat-audit rate (%): all 7 entries same score, V, T2 stores, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatPooledVTThree` | 76.9 | flat-audit rate (%): all 7 entries same score, V, T3 stores, pooled |
| `\DetFlatPooledVTThreeLo` | 52.0 | flat-audit rate (%): all 7 entries same score, V, T3 stores, pooled, lower 95% CI bound |
| `\DetFlatPooledVTThreeHi` | 100.0 | flat-audit rate (%): all 7 entries same score, V, T3 stores, pooled, upper 95% CI bound |
| `\DetFlatPooledVTThreeCI` | [52.0, 100.0] | flat-audit rate (%): all 7 entries same score, V, T3 stores, pooled, 95% CI |
| `\DetFlatPooledVTThreeN` | 52 | flat-audit rate (%): all 7 entries same score, V, T3 stores, pooled, n |
| `\DetFlatPooledVTThreeP` | n/a | flat-audit rate (%): all 7 entries same score, V, T3 stores, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatDeepSeekVFourFlashVTThree` | 65.5 | flat-audit rate (%): all 7 entries same score, V, T3 stores, deepseek-v4-flash |
| `\DetFlatDeepSeekVFourFlashVTThreeLo` | 31.0 | flat-audit rate (%): all 7 entries same score, V, T3 stores, deepseek-v4-flash, lower 95% CI bound |
| `\DetFlatDeepSeekVFourFlashVTThreeHi` | 100.0 | flat-audit rate (%): all 7 entries same score, V, T3 stores, deepseek-v4-flash, upper 95% CI bound |
| `\DetFlatDeepSeekVFourFlashVTThreeCI` | [31.0, 100.0] | flat-audit rate (%): all 7 entries same score, V, T3 stores, deepseek-v4-flash, 95% CI |
| `\DetFlatDeepSeekVFourFlashVTThreeN` | 29 | flat-audit rate (%): all 7 entries same score, V, T3 stores, deepseek-v4-flash, n |
| `\DetFlatDeepSeekVFourFlashVTThreeP` | n/a | flat-audit rate (%): all 7 entries same score, V, T3 stores, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGemmaFourThreeOneBVTThree` | 91.3 | flat-audit rate (%): all 7 entries same score, V, T3 stores, gemma-4-31b-it |
| `\DetFlatGemmaFourThreeOneBVTThreeLo` | 83.3 | flat-audit rate (%): all 7 entries same score, V, T3 stores, gemma-4-31b-it, lower 95% CI bound |
| `\DetFlatGemmaFourThreeOneBVTThreeHi` | 100.0 | flat-audit rate (%): all 7 entries same score, V, T3 stores, gemma-4-31b-it, upper 95% CI bound |
| `\DetFlatGemmaFourThreeOneBVTThreeCI` | [83.3, 100.0] | flat-audit rate (%): all 7 entries same score, V, T3 stores, gemma-4-31b-it, 95% CI |
| `\DetFlatGemmaFourThreeOneBVTThreeN` | 23 | flat-audit rate (%): all 7 entries same score, V, T3 stores, gemma-4-31b-it, n |
| `\DetFlatGemmaFourThreeOneBVTThreeP` | n/a | flat-audit rate (%): all 7 entries same score, V, T3 stores, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatPooledVClean` | 81.8 | flat-audit rate (%): all 7 entries same score, V, clean stores, pooled |
| `\DetFlatPooledVCleanLo` | 60.0 | flat-audit rate (%): all 7 entries same score, V, clean stores, pooled, lower 95% CI bound |
| `\DetFlatPooledVCleanHi` | 100.0 | flat-audit rate (%): all 7 entries same score, V, clean stores, pooled, upper 95% CI bound |
| `\DetFlatPooledVCleanCI` | [60.0, 100.0] | flat-audit rate (%): all 7 entries same score, V, clean stores, pooled, 95% CI |
| `\DetFlatPooledVCleanN` | 11 | flat-audit rate (%): all 7 entries same score, V, clean stores, pooled, n |
| `\DetFlatPooledVCleanP` | n/a | flat-audit rate (%): all 7 entries same score, V, clean stores, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatDeepSeekVFourFlashVClean` | 66.7 | flat-audit rate (%): all 7 entries same score, V, clean stores, deepseek-v4-flash |
| `\DetFlatDeepSeekVFourFlashVCleanLo` | 33.3 | flat-audit rate (%): all 7 entries same score, V, clean stores, deepseek-v4-flash, lower 95% CI bound |
| `\DetFlatDeepSeekVFourFlashVCleanHi` | 100.0 | flat-audit rate (%): all 7 entries same score, V, clean stores, deepseek-v4-flash, upper 95% CI bound |
| `\DetFlatDeepSeekVFourFlashVCleanCI` | [33.3, 100.0] | flat-audit rate (%): all 7 entries same score, V, clean stores, deepseek-v4-flash, 95% CI |
| `\DetFlatDeepSeekVFourFlashVCleanN` | 6 | flat-audit rate (%): all 7 entries same score, V, clean stores, deepseek-v4-flash, n |
| `\DetFlatDeepSeekVFourFlashVCleanP` | n/a | flat-audit rate (%): all 7 entries same score, V, clean stores, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGemmaFourThreeOneBVClean` | 100.0 | flat-audit rate (%): all 7 entries same score, V, clean stores, gemma-4-31b-it |
| `\DetFlatGemmaFourThreeOneBVCleanLo` | 47.8 | flat-audit rate (%): all 7 entries same score, V, clean stores, gemma-4-31b-it, lower 95% CI bound |
| `\DetFlatGemmaFourThreeOneBVCleanHi` | 100.0 | flat-audit rate (%): all 7 entries same score, V, clean stores, gemma-4-31b-it, upper 95% CI bound |
| `\DetFlatGemmaFourThreeOneBVCleanCI` | [47.8, 100.0] | flat-audit rate (%): all 7 entries same score, V, clean stores, gemma-4-31b-it, 95% CI |
| `\DetFlatGemmaFourThreeOneBVCleanN` | 5 | flat-audit rate (%): all 7 entries same score, V, clean stores, gemma-4-31b-it, n |
| `\DetFlatGemmaFourThreeOneBVCleanP` | n/a | flat-audit rate (%): all 7 entries same score, V, clean stores, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledCTZeroStrict` | 83.6 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, pooled |
| `\DetRankPooledCTZeroStrictLo` | 72.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, pooled, lower 95% CI bound |
| `\DetRankPooledCTZeroStrictHi` | 93.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, pooled, upper 95% CI bound |
| `\DetRankPooledCTZeroStrictCI` | [72.0, 93.3] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, pooled, 95% CI |
| `\DetRankPooledCTZeroStrictN` | 55 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, pooled, n |
| `\DetRankPooledCTZeroStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledCTZeroTiesIncl` | 98.2 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, pooled |
| `\DetRankPooledCTZeroTiesInclLo` | 94.5 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, pooled, lower 95% CI bound |
| `\DetRankPooledCTZeroTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, pooled, upper 95% CI bound |
| `\DetRankPooledCTZeroTiesInclCI` | [94.5, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T0, pooled, 95% CI |
| `\DetRankPooledCTZeroTiesInclN` | 55 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, pooled, n |
| `\DetRankPooledCTZeroTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T0, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashCTZeroStrict` | 73.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashCTZeroStrictLo` | 56.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTZeroStrictHi` | 86.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTZeroStrictCI` | [56.7, 86.7] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashCTZeroStrictN` | 30 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashCTZeroStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashCTZeroTiesIncl` | 96.7 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashCTZeroTiesInclLo` | 90.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTZeroTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTZeroTiesInclCI` | [90.0, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T0, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashCTZeroTiesInclN` | 30 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashCTZeroTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBCTZeroStrict` | 96.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBCTZeroStrictLo` | 88.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTZeroStrictHi` | 100.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTZeroStrictCI` | [88.0, 100.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBCTZeroStrictN` | 25 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBCTZeroStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBCTZeroTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBCTZeroTiesInclLo` | 86.3 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTZeroTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTZeroTiesInclCI` | [86.3, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T0, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBCTZeroTiesInclN` | 25 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBCTZeroTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledCTOneStrict` | 88.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, pooled |
| `\DetRankPooledCTOneStrictLo` | 72.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, pooled, lower 95% CI bound |
| `\DetRankPooledCTOneStrictHi` | 100.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, pooled, upper 95% CI bound |
| `\DetRankPooledCTOneStrictCI` | [72.0, 100.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, pooled, 95% CI |
| `\DetRankPooledCTOneStrictN` | 50 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, pooled, n |
| `\DetRankPooledCTOneStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledCTOneTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, pooled |
| `\DetRankPooledCTOneTiesInclLo` | 92.9 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, pooled, lower 95% CI bound |
| `\DetRankPooledCTOneTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, pooled, upper 95% CI bound |
| `\DetRankPooledCTOneTiesInclCI` | [92.9, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T1, pooled, 95% CI |
| `\DetRankPooledCTOneTiesInclN` | 50 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, pooled, n |
| `\DetRankPooledCTOneTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashCTOneStrict` | 80.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashCTOneStrictLo` | 56.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTOneStrictHi` | 100.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTOneStrictCI` | [56.0, 100.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashCTOneStrictN` | 25 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashCTOneStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashCTOneTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashCTOneTiesInclLo` | 86.3 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTOneTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTOneTiesInclCI` | [86.3, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T1, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashCTOneTiesInclN` | 25 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashCTOneTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBCTOneStrict` | 96.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBCTOneStrictLo` | 88.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTOneStrictHi` | 100.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTOneStrictCI` | [88.0, 100.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBCTOneStrictN` | 25 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBCTOneStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBCTOneTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBCTOneTiesInclLo` | 86.3 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTOneTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTOneTiesInclCI` | [86.3, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T1, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBCTOneTiesInclN` | 25 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBCTOneTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledCTTwoStrict` | 87.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, pooled |
| `\DetRankPooledCTTwoStrictLo` | 72.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, pooled, lower 95% CI bound |
| `\DetRankPooledCTTwoStrictHi` | 98.2 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, pooled, upper 95% CI bound |
| `\DetRankPooledCTTwoStrictCI` | [72.7, 98.2] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, pooled, 95% CI |
| `\DetRankPooledCTTwoStrictN` | 54 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, pooled, n |
| `\DetRankPooledCTTwoStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledCTTwoTiesIncl` | 98.1 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, pooled |
| `\DetRankPooledCTTwoTiesInclLo` | 94.4 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, pooled, lower 95% CI bound |
| `\DetRankPooledCTTwoTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, pooled, upper 95% CI bound |
| `\DetRankPooledCTTwoTiesInclCI` | [94.4, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T2, pooled, 95% CI |
| `\DetRankPooledCTTwoTiesInclN` | 54 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, pooled, n |
| `\DetRankPooledCTTwoTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashCTTwoStrict` | 80.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashCTTwoStrictLo` | 60.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTTwoStrictHi` | 96.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTTwoStrictCI` | [60.0, 96.7] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashCTTwoStrictN` | 30 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashCTTwoStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashCTTwoTiesIncl` | 96.7 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashCTTwoTiesInclLo` | 90.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTTwoTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTTwoTiesInclCI` | [90.0, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T2, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashCTTwoTiesInclN` | 30 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashCTTwoTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBCTTwoStrict` | 95.8 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBCTTwoStrictLo` | 87.5 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTTwoStrictHi` | 100.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTTwoStrictCI` | [87.5, 100.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBCTTwoStrictN` | 24 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBCTTwoStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBCTTwoTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBCTTwoTiesInclLo` | 85.8 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTTwoTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTTwoTiesInclCI` | [85.8, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T2, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBCTTwoTiesInclN` | 24 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBCTTwoTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledCTThreeStrict` | 88.5 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, pooled |
| `\DetRankPooledCTThreeStrictLo` | 73.9 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, pooled, lower 95% CI bound |
| `\DetRankPooledCTThreeStrictHi` | 98.2 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, pooled, upper 95% CI bound |
| `\DetRankPooledCTThreeStrictCI` | [73.9, 98.2] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, pooled, 95% CI |
| `\DetRankPooledCTThreeStrictN` | 52 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, pooled, n |
| `\DetRankPooledCTThreeStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledCTThreeTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, pooled |
| `\DetRankPooledCTThreeTiesInclLo` | 93.2 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, pooled, lower 95% CI bound |
| `\DetRankPooledCTThreeTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, pooled, upper 95% CI bound |
| `\DetRankPooledCTThreeTiesInclCI` | [93.2, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T3, pooled, 95% CI |
| `\DetRankPooledCTThreeTiesInclN` | 52 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, pooled, n |
| `\DetRankPooledCTThreeTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashCTThreeStrict` | 86.2 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashCTThreeStrictLo` | 70.4 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTThreeStrictHi` | 96.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTThreeStrictCI` | [70.4, 96.7] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashCTThreeStrictN` | 29 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashCTThreeStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashCTThreeTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashCTThreeTiesInclLo` | 88.1 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTThreeTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTThreeTiesInclCI` | [88.1, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T3, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashCTThreeTiesInclN` | 29 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashCTThreeTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBCTThreeStrict` | 91.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBCTThreeStrictLo` | 75.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTThreeStrictHi` | 100.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTThreeStrictCI` | [75.0, 100.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBCTThreeStrictN` | 23 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBCTThreeStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBCTThreeTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBCTThreeTiesInclLo` | 85.2 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTThreeTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTThreeTiesInclCI` | [85.2, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T3, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBCTThreeTiesInclN` | 23 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBCTThreeTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledVTZeroStrict` | 27.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, pooled |
| `\DetRankPooledVTZeroStrictLo` | 6.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, pooled, lower 95% CI bound |
| `\DetRankPooledVTZeroStrictHi` | 48.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, pooled, upper 95% CI bound |
| `\DetRankPooledVTZeroStrictCI` | [6.0, 48.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, pooled, 95% CI |
| `\DetRankPooledVTZeroStrictN` | 55 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, pooled, n |
| `\DetRankPooledVTZeroStrictP` | 0.200 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledVTZeroTiesIncl` | 96.4 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, pooled |
| `\DetRankPooledVTZeroTiesInclLo` | 92.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, pooled, lower 95% CI bound |
| `\DetRankPooledVTZeroTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, pooled, upper 95% CI bound |
| `\DetRankPooledVTZeroTiesInclCI` | [92.0, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, V T0, pooled, 95% CI |
| `\DetRankPooledVTZeroTiesInclN` | 55 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, pooled, n |
| `\DetRankPooledVTZeroTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T0, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashVTZeroStrict` | 30.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashVTZeroStrictLo` | 6.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTZeroStrictHi` | 53.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTZeroStrictCI` | [6.7, 53.3] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashVTZeroStrictN` | 30 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashVTZeroStrictP` | 0.206 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashVTZeroTiesIncl` | 93.3 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashVTZeroTiesInclLo` | 86.7 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTZeroTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTZeroTiesInclCI` | [86.7, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, V T0, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashVTZeroTiesInclN` | 30 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashVTZeroTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBVTZeroStrict` | 24.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBVTZeroStrictLo` | 4.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTZeroStrictHi` | 44.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTZeroStrictCI` | [4.0, 44.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBVTZeroStrictN` | 25 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBVTZeroStrictP` | 0.328 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBVTZeroTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBVTZeroTiesInclLo` | 86.3 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTZeroTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTZeroTiesInclCI` | [86.3, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, V T0, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBVTZeroTiesInclN` | 25 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBVTZeroTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledVTOneStrict` | 8.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, pooled |
| `\DetRankPooledVTOneStrictLo` | 0.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, pooled, lower 95% CI bound |
| `\DetRankPooledVTOneStrictHi` | 20.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, pooled, upper 95% CI bound |
| `\DetRankPooledVTOneStrictCI` | [0.0, 20.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, pooled, 95% CI |
| `\DetRankPooledVTOneStrictN` | 50 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, pooled, n |
| `\DetRankPooledVTOneStrictP` | 0.187 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledVTOneTiesIncl` | 88.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, pooled |
| `\DetRankPooledVTOneTiesInclLo` | 72.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, pooled, lower 95% CI bound |
| `\DetRankPooledVTOneTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, pooled, upper 95% CI bound |
| `\DetRankPooledVTOneTiesInclCI` | [72.0, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, V T1, pooled, 95% CI |
| `\DetRankPooledVTOneTiesInclN` | 50 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, pooled, n |
| `\DetRankPooledVTOneTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashVTOneStrict` | 16.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashVTOneStrictLo` | 0.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTOneStrictHi` | 40.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTOneStrictCI` | [0.0, 40.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashVTOneStrictN` | 25 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashVTOneStrictP` | 0.880 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashVTOneTiesIncl` | 76.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashVTOneTiesInclLo` | 44.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTOneTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTOneTiesInclCI` | [44.0, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, V T1, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashVTOneTiesInclN` | 25 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashVTOneTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBVTOneStrict` | 0.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBVTOneStrictLo` | 0.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTOneStrictHi` | 13.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTOneStrictCI` | [0.0, 13.7] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBVTOneStrictN` | 25 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBVTOneStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBVTOneTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBVTOneTiesInclLo` | 86.3 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTOneTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTOneTiesInclCI` | [86.3, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, V T1, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBVTOneTiesInclN` | 25 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBVTOneTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledVTTwoStrict` | 9.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, pooled |
| `\DetRankPooledVTTwoStrictLo` | 0.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, pooled, lower 95% CI bound |
| `\DetRankPooledVTTwoStrictHi` | 20.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, pooled, upper 95% CI bound |
| `\DetRankPooledVTTwoStrictCI` | [0.0, 20.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, pooled, 95% CI |
| `\DetRankPooledVTTwoStrictN` | 54 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, pooled, n |
| `\DetRankPooledVTTwoStrictP` | 0.388 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledVTTwoTiesIncl` | 88.9 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, pooled |
| `\DetRankPooledVTTwoTiesInclLo` | 74.5 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, pooled, lower 95% CI bound |
| `\DetRankPooledVTTwoTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, pooled, upper 95% CI bound |
| `\DetRankPooledVTTwoTiesInclCI` | [74.5, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, V T2, pooled, 95% CI |
| `\DetRankPooledVTTwoTiesInclN` | 54 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, pooled, n |
| `\DetRankPooledVTTwoTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashVTTwoStrict` | 10.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashVTTwoStrictLo` | 0.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTTwoStrictHi` | 23.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTTwoStrictCI` | [0.0, 23.3] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashVTTwoStrictN` | 30 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashVTTwoStrictP` | 0.396 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashVTTwoTiesIncl` | 80.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashVTTwoTiesInclLo` | 53.3 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTTwoTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTTwoTiesInclCI` | [53.3, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, V T2, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashVTTwoTiesInclN` | 30 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashVTTwoTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBVTTwoStrict` | 8.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBVTTwoStrictLo` | 0.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTTwoStrictHi` | 16.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTTwoStrictCI` | [0.0, 16.7] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBVTTwoStrictN` | 24 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBVTTwoStrictP` | 0.167 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBVTTwoTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBVTTwoTiesInclLo` | 85.8 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTTwoTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTTwoTiesInclCI` | [85.8, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, V T2, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBVTTwoTiesInclN` | 24 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBVTTwoTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledVTThreeStrict` | 11.5 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, pooled |
| `\DetRankPooledVTThreeStrictLo` | 0.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, pooled, lower 95% CI bound |
| `\DetRankPooledVTThreeStrictHi` | 25.9 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, pooled, upper 95% CI bound |
| `\DetRankPooledVTThreeStrictCI` | [0.0, 25.9] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, pooled, 95% CI |
| `\DetRankPooledVTThreeStrictN` | 52 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, pooled, n |
| `\DetRankPooledVTThreeStrictP` | 0.687 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledVTThreeTiesIncl` | 88.5 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, pooled |
| `\DetRankPooledVTThreeTiesInclLo` | 74.1 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, pooled, lower 95% CI bound |
| `\DetRankPooledVTThreeTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, pooled, upper 95% CI bound |
| `\DetRankPooledVTThreeTiesInclCI` | [74.1, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, V T3, pooled, 95% CI |
| `\DetRankPooledVTThreeTiesInclN` | 52 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, pooled, n |
| `\DetRankPooledVTThreeTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashVTThreeStrict` | 13.8 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashVTThreeStrictLo` | 0.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTThreeStrictHi` | 33.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTThreeStrictCI` | [0.0, 33.3] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashVTThreeStrictN` | 29 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashVTThreeStrictP` | 0.825 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashVTThreeTiesIncl` | 79.3 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashVTThreeTiesInclLo` | 51.7 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTThreeTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTThreeTiesInclCI` | [51.7, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, V T3, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashVTThreeTiesInclN` | 29 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashVTThreeTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBVTThreeStrict` | 8.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBVTThreeStrictLo` | 0.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTThreeStrictHi` | 16.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTThreeStrictCI` | [0.0, 16.7] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBVTThreeStrictN` | 23 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBVTThreeStrictP` | 0.179 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBVTThreeTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBVTThreeTiesInclLo` | 85.2 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTThreeTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTThreeTiesInclCI` | [85.2, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, V T3, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBVTThreeTiesInclN` | 23 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBVTThreeTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRederivDisagreePooled` | 42.2 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), pooled |
| `\DetRederivDisagreePooledLo` | 30.5 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), pooled, lower 95% CI bound |
| `\DetRederivDisagreePooledHi` | 56.6 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), pooled, upper 95% CI bound |
| `\DetRederivDisagreePooledCI` | [30.5, 56.6] | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), pooled, 95% CI |
| `\DetRederivDisagreePooledN` | 83 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), pooled, n |
| `\DetRederivDisagreePooledP` | n/a | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRederivDisagreeDeepSeekVFourFlash` | 52.4 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), deepseek-v4-flash |
| `\DetRederivDisagreeDeepSeekVFourFlashLo` | 38.1 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), deepseek-v4-flash, lower 95% CI bound |
| `\DetRederivDisagreeDeepSeekVFourFlashHi` | 69.0 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), deepseek-v4-flash, upper 95% CI bound |
| `\DetRederivDisagreeDeepSeekVFourFlashCI` | [38.1, 69.0] | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), deepseek-v4-flash, 95% CI |
| `\DetRederivDisagreeDeepSeekVFourFlashN` | 42 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), deepseek-v4-flash, n |
| `\DetRederivDisagreeDeepSeekVFourFlashP` | n/a | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRederivDisagreeGemmaFourThreeOneB` | 31.7 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), gemma-4-31b-it |
| `\DetRederivDisagreeGemmaFourThreeOneBLo` | 14.6 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), gemma-4-31b-it, lower 95% CI bound |
| `\DetRederivDisagreeGemmaFourThreeOneBHi` | 50.0 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), gemma-4-31b-it, upper 95% CI bound |
| `\DetRederivDisagreeGemmaFourThreeOneBCI` | [14.6, 50.0] | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), gemma-4-31b-it, 95% CI |
| `\DetRederivDisagreeGemmaFourThreeOneBN` | 41 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), gemma-4-31b-it, n |
| `\DetRederivDisagreeGemmaFourThreeOneBP` | n/a | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetVerbalTThree` | 0.54 | mean AUROC of V at T3 (reported with primary 2) |
| `\DetVerbalTThreeLo` | 0.51 | mean AUROC of V at T3 (reported with primary 2), lower 95% CI bound |
| `\DetVerbalTThreeHi` | 0.62 | mean AUROC of V at T3 (reported with primary 2), upper 95% CI bound |
| `\DetVerbalTThreeCI` | [0.51, 0.62] | mean AUROC of V at T3 (reported with primary 2), 95% CI |
| `\DetVerbalTThreeN` | 104 | mean AUROC of V at T3 (reported with primary 2), n |
| `\DetVerbalTThreeP` | 0.014 | mean AUROC of V at T3 (reported with primary 2), two-sided bootstrap p (n/a if not tested) |
| `\DetCalibR` | 0.82 | pooled calibration AUROC of R (selection for primary 3) |
| `\DetCalibRLo` | 0.70 | pooled calibration AUROC of R (selection for primary 3), lower 95% CI bound |
| `\DetCalibRHi` | 0.96 | pooled calibration AUROC of R (selection for primary 3), upper 95% CI bound |
| `\DetCalibRCI` | [0.70, 0.96] | pooled calibration AUROC of R (selection for primary 3), 95% CI |
| `\DetCalibRN` | 138 | pooled calibration AUROC of R (selection for primary 3), n |
| `\DetCalibRP` | n/a | pooled calibration AUROC of R (selection for primary 3), two-sided bootstrap p (n/a if not tested) |
| `\DetCalibC` | 0.98 | pooled calibration AUROC of C (selection for primary 3) |
| `\DetCalibCLo` | 0.94 | pooled calibration AUROC of C (selection for primary 3), lower 95% CI bound |
| `\DetCalibCHi` | 1.00 | pooled calibration AUROC of C (selection for primary 3), upper 95% CI bound |
| `\DetCalibCCI` | [0.94, 1.00] | pooled calibration AUROC of C (selection for primary 3), 95% CI |
| `\DetCalibCN` | 118 | pooled calibration AUROC of C (selection for primary 3), n |
| `\DetCalibCP` | n/a | pooled calibration AUROC of C (selection for primary 3), two-sided bootstrap p (n/a if not tested) |
| `\NegsDeepSeekVFourFlashOtherEpisode` | 0.49 | matched negatives: AUROC of V, other_episode vs genuine, deepseek-v4-flash |
| `\NegsDeepSeekVFourFlashOtherEpisodeLo` | 0.40 | matched negatives: AUROC of V, other_episode vs genuine, deepseek-v4-flash, lower 95% CI bound |
| `\NegsDeepSeekVFourFlashOtherEpisodeHi` | 0.56 | matched negatives: AUROC of V, other_episode vs genuine, deepseek-v4-flash, upper 95% CI bound |
| `\NegsDeepSeekVFourFlashOtherEpisodeCI` | [0.40, 0.56] | matched negatives: AUROC of V, other_episode vs genuine, deepseek-v4-flash, 95% CI |
| `\NegsDeepSeekVFourFlashOtherEpisodeN` | 24 | matched negatives: AUROC of V, other_episode vs genuine, deepseek-v4-flash, n |
| `\NegsDeepSeekVFourFlashOtherEpisodeP` | n/a | matched negatives: AUROC of V, other_episode vs genuine, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\NegsDeepSeekVFourFlashOtherModel` | 0.53 | matched negatives: AUROC of V, other_model vs genuine, deepseek-v4-flash |
| `\NegsDeepSeekVFourFlashOtherModelLo` | 0.50 | matched negatives: AUROC of V, other_model vs genuine, deepseek-v4-flash, lower 95% CI bound |
| `\NegsDeepSeekVFourFlashOtherModelHi` | 0.66 | matched negatives: AUROC of V, other_model vs genuine, deepseek-v4-flash, upper 95% CI bound |
| `\NegsDeepSeekVFourFlashOtherModelCI` | [0.50, 0.66] | matched negatives: AUROC of V, other_model vs genuine, deepseek-v4-flash, 95% CI |
| `\NegsDeepSeekVFourFlashOtherModelN` | 22 | matched negatives: AUROC of V, other_model vs genuine, deepseek-v4-flash, n |
| `\NegsDeepSeekVFourFlashOtherModelP` | n/a | matched negatives: AUROC of V, other_model vs genuine, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\NegsGemmaFourThreeOneBOtherEpisode` | 0.50 | matched negatives: AUROC of V, other_episode vs genuine, gemma-4-31b-it |
| `\NegsGemmaFourThreeOneBOtherEpisodeLo` | 0.50 | matched negatives: AUROC of V, other_episode vs genuine, gemma-4-31b-it, lower 95% CI bound |
| `\NegsGemmaFourThreeOneBOtherEpisodeHi` | 0.50 | matched negatives: AUROC of V, other_episode vs genuine, gemma-4-31b-it, upper 95% CI bound |
| `\NegsGemmaFourThreeOneBOtherEpisodeCI` | [0.50, 0.50] | matched negatives: AUROC of V, other_episode vs genuine, gemma-4-31b-it, 95% CI |
| `\NegsGemmaFourThreeOneBOtherEpisodeN` | 20 | matched negatives: AUROC of V, other_episode vs genuine, gemma-4-31b-it, n |
| `\NegsGemmaFourThreeOneBOtherEpisodeP` | n/a | matched negatives: AUROC of V, other_episode vs genuine, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\NegsGemmaFourThreeOneBOtherModel` | 0.50 | matched negatives: AUROC of V, other_model vs genuine, gemma-4-31b-it |
| `\NegsGemmaFourThreeOneBOtherModelLo` | 0.50 | matched negatives: AUROC of V, other_model vs genuine, gemma-4-31b-it, lower 95% CI bound |
| `\NegsGemmaFourThreeOneBOtherModelHi` | 0.50 | matched negatives: AUROC of V, other_model vs genuine, gemma-4-31b-it, upper 95% CI bound |
| `\NegsGemmaFourThreeOneBOtherModelCI` | [0.50, 0.50] | matched negatives: AUROC of V, other_model vs genuine, gemma-4-31b-it, 95% CI |
| `\NegsGemmaFourThreeOneBOtherModelN` | 20 | matched negatives: AUROC of V, other_model vs genuine, gemma-4-31b-it, n |
| `\NegsGemmaFourThreeOneBOtherModelP` | n/a | matched negatives: AUROC of V, other_model vs genuine, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTZero` | 85.0 | 2AFC accuracy (%), T0, pooled |
| `\AfcPooledTZeroLo` | 70.0 | 2AFC accuracy (%), T0, pooled, lower 95% CI bound |
| `\AfcPooledTZeroHi` | 100.0 | 2AFC accuracy (%), T0, pooled, upper 95% CI bound |
| `\AfcPooledTZeroCI` | [70.0, 100.0] | 2AFC accuracy (%), T0, pooled, 95% CI |
| `\AfcPooledTZeroN` | 20 | 2AFC accuracy (%), T0, pooled, n |
| `\AfcPooledTZeroP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T0, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTOne` | 88.0 | 2AFC accuracy (%), T1, pooled |
| `\AfcPooledTOneLo` | 80.0 | 2AFC accuracy (%), T1, pooled, lower 95% CI bound |
| `\AfcPooledTOneHi` | 96.0 | 2AFC accuracy (%), T1, pooled, upper 95% CI bound |
| `\AfcPooledTOneCI` | [80.0, 96.0] | 2AFC accuracy (%), T1, pooled, 95% CI |
| `\AfcPooledTOneN` | 25 | 2AFC accuracy (%), T1, pooled, n |
| `\AfcPooledTOneP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTTwo` | 87.5 | 2AFC accuracy (%), T2, pooled |
| `\AfcPooledTTwoLo` | 80.0 | 2AFC accuracy (%), T2, pooled, lower 95% CI bound |
| `\AfcPooledTTwoHi` | 95.8 | 2AFC accuracy (%), T2, pooled, upper 95% CI bound |
| `\AfcPooledTTwoCI` | [80.0, 95.8] | 2AFC accuracy (%), T2, pooled, 95% CI |
| `\AfcPooledTTwoN` | 24 | 2AFC accuracy (%), T2, pooled, n |
| `\AfcPooledTTwoP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTThree` | 73.9 | 2AFC accuracy (%), T3, pooled |
| `\AfcPooledTThreeLo` | 62.5 | 2AFC accuracy (%), T3, pooled, lower 95% CI bound |
| `\AfcPooledTThreeHi` | 86.4 | 2AFC accuracy (%), T3, pooled, upper 95% CI bound |
| `\AfcPooledTThreeCI` | [62.5, 86.4] | 2AFC accuracy (%), T3, pooled, 95% CI |
| `\AfcPooledTThreeN` | 23 | 2AFC accuracy (%), T3, pooled, n |
| `\AfcPooledTThreeP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcGemmaFourThreeOneBTZero` | 85.0 | 2AFC accuracy (%), T0, gemma-4-31b-it |
| `\AfcGemmaFourThreeOneBTZeroLo` | 70.0 | 2AFC accuracy (%), T0, gemma-4-31b-it, lower 95% CI bound |
| `\AfcGemmaFourThreeOneBTZeroHi` | 100.0 | 2AFC accuracy (%), T0, gemma-4-31b-it, upper 95% CI bound |
| `\AfcGemmaFourThreeOneBTZeroCI` | [70.0, 100.0] | 2AFC accuracy (%), T0, gemma-4-31b-it, 95% CI |
| `\AfcGemmaFourThreeOneBTZeroN` | 20 | 2AFC accuracy (%), T0, gemma-4-31b-it, n |
| `\AfcGemmaFourThreeOneBTZeroP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\AfcGemmaFourThreeOneBTOne` | 88.0 | 2AFC accuracy (%), T1, gemma-4-31b-it |
| `\AfcGemmaFourThreeOneBTOneLo` | 80.0 | 2AFC accuracy (%), T1, gemma-4-31b-it, lower 95% CI bound |
| `\AfcGemmaFourThreeOneBTOneHi` | 96.0 | 2AFC accuracy (%), T1, gemma-4-31b-it, upper 95% CI bound |
| `\AfcGemmaFourThreeOneBTOneCI` | [80.0, 96.0] | 2AFC accuracy (%), T1, gemma-4-31b-it, 95% CI |
| `\AfcGemmaFourThreeOneBTOneN` | 25 | 2AFC accuracy (%), T1, gemma-4-31b-it, n |
| `\AfcGemmaFourThreeOneBTOneP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\AfcGemmaFourThreeOneBTTwo` | 87.5 | 2AFC accuracy (%), T2, gemma-4-31b-it |
| `\AfcGemmaFourThreeOneBTTwoLo` | 80.0 | 2AFC accuracy (%), T2, gemma-4-31b-it, lower 95% CI bound |
| `\AfcGemmaFourThreeOneBTTwoHi` | 95.8 | 2AFC accuracy (%), T2, gemma-4-31b-it, upper 95% CI bound |
| `\AfcGemmaFourThreeOneBTTwoCI` | [80.0, 95.8] | 2AFC accuracy (%), T2, gemma-4-31b-it, 95% CI |
| `\AfcGemmaFourThreeOneBTTwoN` | 24 | 2AFC accuracy (%), T2, gemma-4-31b-it, n |
| `\AfcGemmaFourThreeOneBTTwoP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\AfcGemmaFourThreeOneBTThree` | 73.9 | 2AFC accuracy (%), T3, gemma-4-31b-it |
| `\AfcGemmaFourThreeOneBTThreeLo` | 62.5 | 2AFC accuracy (%), T3, gemma-4-31b-it, lower 95% CI bound |
| `\AfcGemmaFourThreeOneBTThreeHi` | 86.4 | 2AFC accuracy (%), T3, gemma-4-31b-it, upper 95% CI bound |
| `\AfcGemmaFourThreeOneBTThreeCI` | [62.5, 86.4] | 2AFC accuracy (%), T3, gemma-4-31b-it, 95% CI |
| `\AfcGemmaFourThreeOneBTThreeN` | 23 | 2AFC accuracy (%), T3, gemma-4-31b-it, n |
| `\AfcGemmaFourThreeOneBTThreeP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\JudgeAccuracyIdentical` | 100.0 | judge gold set: accuracy_identical |
| `\JudgeAccuracyIdenticalLo` | 95.3 | judge gold set: accuracy_identical, lower 95% CI bound |
| `\JudgeAccuracyIdenticalHi` | 100.0 | judge gold set: accuracy_identical, upper 95% CI bound |
| `\JudgeAccuracyIdenticalCI` | [95.3, 100.0] | judge gold set: accuracy_identical, 95% CI |
| `\JudgeAccuracyIdenticalN` | 76 | judge gold set: accuracy_identical, n |
| `\JudgeAccuracyIdenticalP` | n/a | judge gold set: accuracy_identical, two-sided bootstrap p (n/a if not tested) |
| `\JudgeAnyFlagIdentical` | 0.0 | judge gold set: any_flag_identical |
| `\JudgeAnyFlagIdenticalLo` | 0.0 | judge gold set: any_flag_identical, lower 95% CI bound |
| `\JudgeAnyFlagIdenticalHi` | 4.7 | judge gold set: any_flag_identical, upper 95% CI bound |
| `\JudgeAnyFlagIdenticalCI` | [0.0, 4.7] | judge gold set: any_flag_identical, 95% CI |
| `\JudgeAnyFlagIdenticalN` | 76 | judge gold set: any_flag_identical, n |
| `\JudgeAnyFlagIdenticalP` | n/a | judge gold set: any_flag_identical, two-sided bootstrap p (n/a if not tested) |
| `\JudgeAccuracyResampled` | 57.8 | judge gold set: accuracy_resampled |
| `\JudgeAccuracyResampledLo` | 45.1 | judge gold set: accuracy_resampled, lower 95% CI bound |
| `\JudgeAccuracyResampledHi` | 69.5 | judge gold set: accuracy_resampled, upper 95% CI bound |
| `\JudgeAccuracyResampledCI` | [45.1, 69.5] | judge gold set: accuracy_resampled, 95% CI |
| `\JudgeAccuracyResampledN` | 83 | judge gold set: accuracy_resampled, n |
| `\JudgeAccuracyResampledP` | n/a | judge gold set: accuracy_resampled, two-sided bootstrap p (n/a if not tested) |
| `\JudgeAnyFlagResampled` | 42.2 | judge gold set: any_flag_resampled |
| `\JudgeAnyFlagResampledLo` | 30.1 | judge gold set: any_flag_resampled, lower 95% CI bound |
| `\JudgeAnyFlagResampledHi` | 54.8 | judge gold set: any_flag_resampled, upper 95% CI bound |
| `\JudgeAnyFlagResampledCI` | [30.1, 54.8] | judge gold set: any_flag_resampled, 95% CI |
| `\JudgeAnyFlagResampledN` | 83 | judge gold set: any_flag_resampled, n |
| `\JudgeAnyFlagResampledP` | n/a | judge gold set: any_flag_resampled, two-sided bootstrap p (n/a if not tested) |
| `\JudgeAccuracyTZero` | 100.0 | judge gold set: accuracy_T0 |
| `\JudgeAccuracyTZeroLo` | 93.9 | judge gold set: accuracy_T0, lower 95% CI bound |
| `\JudgeAccuracyTZeroHi` | 100.0 | judge gold set: accuracy_T0, upper 95% CI bound |
| `\JudgeAccuracyTZeroCI` | [93.9, 100.0] | judge gold set: accuracy_T0, 95% CI |
| `\JudgeAccuracyTZeroN` | 59 | judge gold set: accuracy_T0, n |
| `\JudgeAccuracyTZeroP` | n/a | judge gold set: accuracy_T0, two-sided bootstrap p (n/a if not tested) |
| `\JudgeAnyFlagTZero` | 100.0 | judge gold set: any_flag_T0 |
| `\JudgeAnyFlagTZeroLo` | 93.9 | judge gold set: any_flag_T0, lower 95% CI bound |
| `\JudgeAnyFlagTZeroHi` | 100.0 | judge gold set: any_flag_T0, upper 95% CI bound |
| `\JudgeAnyFlagTZeroCI` | [93.9, 100.0] | judge gold set: any_flag_T0, 95% CI |
| `\JudgeAnyFlagTZeroN` | 59 | judge gold set: any_flag_T0, n |
| `\JudgeAnyFlagTZeroP` | n/a | judge gold set: any_flag_T0, two-sided bootstrap p (n/a if not tested) |
| `\JudgeAurocTZeroVsResampled` | 0.85 | judge gold set: auroc_T0_vs_resampled |
| `\JudgeAurocTZeroVsResampledLo` | 0.80 | judge gold set: auroc_T0_vs_resampled, lower 95% CI bound |
| `\JudgeAurocTZeroVsResampledHi` | 0.90 | judge gold set: auroc_T0_vs_resampled, upper 95% CI bound |
| `\JudgeAurocTZeroVsResampledCI` | [0.80, 0.90] | judge gold set: auroc_T0_vs_resampled, 95% CI |
| `\JudgeAurocTZeroVsResampledN` | 142 | judge gold set: auroc_T0_vs_resampled, n |
| `\JudgeAurocTZeroVsResampledP` | \ensuremath{<}0.001 | judge gold set: auroc_T0_vs_resampled, two-sided bootstrap p (n/a if not tested) |
| `\JudgeAurocTZeroVsIdentical` | 1.00 | judge gold set: auroc_T0_vs_identical |
| `\JudgeAurocTZeroVsIdenticalLo` | 1.00 | judge gold set: auroc_T0_vs_identical, lower 95% CI bound |
| `\JudgeAurocTZeroVsIdenticalHi` | 1.00 | judge gold set: auroc_T0_vs_identical, upper 95% CI bound |
| `\JudgeAurocTZeroVsIdenticalCI` | [1.00, 1.00] | judge gold set: auroc_T0_vs_identical, 95% CI |
| `\JudgeAurocTZeroVsIdenticalN` | 135 | judge gold set: auroc_T0_vs_identical, n |
| `\JudgeAurocTZeroVsIdenticalP` | \ensuremath{<}0.001 | judge gold set: auroc_T0_vs_identical, two-sided bootstrap p (n/a if not tested) |
| `\JudgeFlagHitEOne` | 100.0 | judge gold set: flag_hit_E1 |
| `\JudgeFlagHitEOneLo` | 73.5 | judge gold set: flag_hit_E1, lower 95% CI bound |
| `\JudgeFlagHitEOneHi` | 100.0 | judge gold set: flag_hit_E1, upper 95% CI bound |
| `\JudgeFlagHitEOneCI` | [73.5, 100.0] | judge gold set: flag_hit_E1, 95% CI |
| `\JudgeFlagHitEOneN` | 12 | judge gold set: flag_hit_E1, n |
| `\JudgeFlagHitEOneP` | n/a | judge gold set: flag_hit_E1, two-sided bootstrap p (n/a if not tested) |
| `\JudgeFlagHitETwo` | 100.0 | judge gold set: flag_hit_E2 |
| `\JudgeFlagHitETwoLo` | 71.5 | judge gold set: flag_hit_E2, lower 95% CI bound |
| `\JudgeFlagHitETwoHi` | 100.0 | judge gold set: flag_hit_E2, upper 95% CI bound |
| `\JudgeFlagHitETwoCI` | [71.5, 100.0] | judge gold set: flag_hit_E2, 95% CI |
| `\JudgeFlagHitETwoN` | 11 | judge gold set: flag_hit_E2, n |
| `\JudgeFlagHitETwoP` | n/a | judge gold set: flag_hit_E2, two-sided bootstrap p (n/a if not tested) |
| `\JudgeFlagHitEThree` | 100.0 | judge gold set: flag_hit_E3 |
| `\JudgeFlagHitEThreeLo` | 73.5 | judge gold set: flag_hit_E3, lower 95% CI bound |
| `\JudgeFlagHitEThreeHi` | 100.0 | judge gold set: flag_hit_E3, upper 95% CI bound |
| `\JudgeFlagHitEThreeCI` | [73.5, 100.0] | judge gold set: flag_hit_E3, 95% CI |
| `\JudgeFlagHitEThreeN` | 12 | judge gold set: flag_hit_E3, n |
| `\JudgeFlagHitEThreeP` | n/a | judge gold set: flag_hit_E3, two-sided bootstrap p (n/a if not tested) |
| `\JudgeFlagHitEFour` | 100.0 | judge gold set: flag_hit_E4 |
| `\JudgeFlagHitEFourLo` | 73.5 | judge gold set: flag_hit_E4, lower 95% CI bound |
| `\JudgeFlagHitEFourHi` | 100.0 | judge gold set: flag_hit_E4, upper 95% CI bound |
| `\JudgeFlagHitEFourCI` | [73.5, 100.0] | judge gold set: flag_hit_E4, 95% CI |
| `\JudgeFlagHitEFourN` | 12 | judge gold set: flag_hit_E4, n |
| `\JudgeFlagHitEFourP` | n/a | judge gold set: flag_hit_E4, two-sided bootstrap p (n/a if not tested) |
| `\JudgeFlagHitEFive` | 100.0 | judge gold set: flag_hit_E5 |
| `\JudgeFlagHitEFiveLo` | 73.5 | judge gold set: flag_hit_E5, lower 95% CI bound |
| `\JudgeFlagHitEFiveHi` | 100.0 | judge gold set: flag_hit_E5, upper 95% CI bound |
| `\JudgeFlagHitEFiveCI` | [73.5, 100.0] | judge gold set: flag_hit_E5, 95% CI |
| `\JudgeFlagHitEFiveN` | 12 | judge gold set: flag_hit_E5, n |
| `\JudgeFlagHitEFiveP` | n/a | judge gold set: flag_hit_E5, two-sided bootstrap p (n/a if not tested) |
| `\ValidDeepSeekVFourFlashTZero` | 100.0 | % valid forgeries, T0, deepseek-v4-flash |
| `\ValidDeepSeekVFourFlashTZeroLo` | 94.0 | % valid forgeries, T0, deepseek-v4-flash, lower 95% CI bound |
| `\ValidDeepSeekVFourFlashTZeroHi` | 100.0 | % valid forgeries, T0, deepseek-v4-flash, upper 95% CI bound |
| `\ValidDeepSeekVFourFlashTZeroCI` | [94.0, 100.0] | % valid forgeries, T0, deepseek-v4-flash, 95% CI |
| `\ValidDeepSeekVFourFlashTZeroN` | 60 | % valid forgeries, T0, deepseek-v4-flash, n |
| `\ValidDeepSeekVFourFlashTZeroP` | n/a | % valid forgeries, T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\ValidDeepSeekVFourFlashTOne` | 83.3 | % valid forgeries, T1, deepseek-v4-flash |
| `\ValidDeepSeekVFourFlashTOneLo` | 58.3 | % valid forgeries, T1, deepseek-v4-flash, lower 95% CI bound |
| `\ValidDeepSeekVFourFlashTOneHi` | 100.0 | % valid forgeries, T1, deepseek-v4-flash, upper 95% CI bound |
| `\ValidDeepSeekVFourFlashTOneCI` | [58.3, 100.0] | % valid forgeries, T1, deepseek-v4-flash, 95% CI |
| `\ValidDeepSeekVFourFlashTOneN` | 60 | % valid forgeries, T1, deepseek-v4-flash, n |
| `\ValidDeepSeekVFourFlashTOneP` | n/a | % valid forgeries, T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\ValidDeepSeekVFourFlashTTwo` | 100.0 | % valid forgeries, T2, deepseek-v4-flash |
| `\ValidDeepSeekVFourFlashTTwoLo` | 94.0 | % valid forgeries, T2, deepseek-v4-flash, lower 95% CI bound |
| `\ValidDeepSeekVFourFlashTTwoHi` | 100.0 | % valid forgeries, T2, deepseek-v4-flash, upper 95% CI bound |
| `\ValidDeepSeekVFourFlashTTwoCI` | [94.0, 100.0] | % valid forgeries, T2, deepseek-v4-flash, 95% CI |
| `\ValidDeepSeekVFourFlashTTwoN` | 60 | % valid forgeries, T2, deepseek-v4-flash, n |
| `\ValidDeepSeekVFourFlashTTwoP` | n/a | % valid forgeries, T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\ValidDeepSeekVFourFlashTThree` | 98.3 | % valid forgeries, T3, deepseek-v4-flash |
| `\ValidDeepSeekVFourFlashTThreeLo` | 95.0 | % valid forgeries, T3, deepseek-v4-flash, lower 95% CI bound |
| `\ValidDeepSeekVFourFlashTThreeHi` | 100.0 | % valid forgeries, T3, deepseek-v4-flash, upper 95% CI bound |
| `\ValidDeepSeekVFourFlashTThreeCI` | [95.0, 100.0] | % valid forgeries, T3, deepseek-v4-flash, 95% CI |
| `\ValidDeepSeekVFourFlashTThreeN` | 60 | % valid forgeries, T3, deepseek-v4-flash, n |
| `\ValidDeepSeekVFourFlashTThreeP` | n/a | % valid forgeries, T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\ValidGemmaFourThreeOneBTZero` | 100.0 | % valid forgeries, T0, gemma-4-31b-it |
| `\ValidGemmaFourThreeOneBTZeroLo` | 93.9 | % valid forgeries, T0, gemma-4-31b-it, lower 95% CI bound |
| `\ValidGemmaFourThreeOneBTZeroHi` | 100.0 | % valid forgeries, T0, gemma-4-31b-it, upper 95% CI bound |
| `\ValidGemmaFourThreeOneBTZeroCI` | [93.9, 100.0] | % valid forgeries, T0, gemma-4-31b-it, 95% CI |
| `\ValidGemmaFourThreeOneBTZeroN` | 59 | % valid forgeries, T0, gemma-4-31b-it, n |
| `\ValidGemmaFourThreeOneBTZeroP` | n/a | % valid forgeries, T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\ValidGemmaFourThreeOneBTOne` | 100.0 | % valid forgeries, T1, gemma-4-31b-it |
| `\ValidGemmaFourThreeOneBTOneLo` | 93.9 | % valid forgeries, T1, gemma-4-31b-it, lower 95% CI bound |
| `\ValidGemmaFourThreeOneBTOneHi` | 100.0 | % valid forgeries, T1, gemma-4-31b-it, upper 95% CI bound |
| `\ValidGemmaFourThreeOneBTOneCI` | [93.9, 100.0] | % valid forgeries, T1, gemma-4-31b-it, 95% CI |
| `\ValidGemmaFourThreeOneBTOneN` | 59 | % valid forgeries, T1, gemma-4-31b-it, n |
| `\ValidGemmaFourThreeOneBTOneP` | n/a | % valid forgeries, T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\ValidGemmaFourThreeOneBTTwo` | 98.3 | % valid forgeries, T2, gemma-4-31b-it |
| `\ValidGemmaFourThreeOneBTTwoLo` | 94.9 | % valid forgeries, T2, gemma-4-31b-it, lower 95% CI bound |
| `\ValidGemmaFourThreeOneBTTwoHi` | 100.0 | % valid forgeries, T2, gemma-4-31b-it, upper 95% CI bound |
| `\ValidGemmaFourThreeOneBTTwoCI` | [94.9, 100.0] | % valid forgeries, T2, gemma-4-31b-it, 95% CI |
| `\ValidGemmaFourThreeOneBTTwoN` | 59 | % valid forgeries, T2, gemma-4-31b-it, n |
| `\ValidGemmaFourThreeOneBTTwoP` | n/a | % valid forgeries, T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\ValidGemmaFourThreeOneBTThree` | 98.3 | % valid forgeries, T3, gemma-4-31b-it |
| `\ValidGemmaFourThreeOneBTThreeLo` | 94.8 | % valid forgeries, T3, gemma-4-31b-it, lower 95% CI bound |
| `\ValidGemmaFourThreeOneBTThreeHi` | 100.0 | % valid forgeries, T3, gemma-4-31b-it, upper 95% CI bound |
| `\ValidGemmaFourThreeOneBTThreeCI` | [94.8, 100.0] | % valid forgeries, T3, gemma-4-31b-it, 95% CI |
| `\ValidGemmaFourThreeOneBTThreeN` | 59 | % valid forgeries, T3, gemma-4-31b-it, n |
| `\ValidGemmaFourThreeOneBTThreeP` | n/a | % valid forgeries, T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\TthreeDeepSeekVFourFlashFirstSelected` | 49.0 | T3: % first-shown candidate selected, deepseek-v4-flash |
| `\TthreeDeepSeekVFourFlashFirstSelectedLo` | 35.4 | T3: % first-shown candidate selected, deepseek-v4-flash, lower 95% CI bound |
| `\TthreeDeepSeekVFourFlashFirstSelectedHi` | 63.0 | T3: % first-shown candidate selected, deepseek-v4-flash, upper 95% CI bound |
| `\TthreeDeepSeekVFourFlashFirstSelectedCI` | [35.4, 63.0] | T3: % first-shown candidate selected, deepseek-v4-flash, 95% CI |
| `\TthreeDeepSeekVFourFlashFirstSelectedN` | 51 | T3: % first-shown candidate selected, deepseek-v4-flash, n |
| `\TthreeDeepSeekVFourFlashFirstSelectedP` | n/a | T3: % first-shown candidate selected, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\TthreeDeepSeekVFourFlashFirstTop` | 52.9 | T3: % first-shown candidate top-rated, deepseek-v4-flash |
| `\TthreeDeepSeekVFourFlashFirstTopLo` | 40.7 | T3: % first-shown candidate top-rated, deepseek-v4-flash, lower 95% CI bound |
| `\TthreeDeepSeekVFourFlashFirstTopHi` | 65.5 | T3: % first-shown candidate top-rated, deepseek-v4-flash, upper 95% CI bound |
| `\TthreeDeepSeekVFourFlashFirstTopCI` | [40.7, 65.5] | T3: % first-shown candidate top-rated, deepseek-v4-flash, 95% CI |
| `\TthreeDeepSeekVFourFlashFirstTopN` | 51 | T3: % first-shown candidate top-rated, deepseek-v4-flash, n |
| `\TthreeDeepSeekVFourFlashFirstTopP` | n/a | T3: % first-shown candidate top-rated, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\TthreeDeepSeekVFourFlashChance` | 16.7 | T3: chance level of first-shown selection (%), deepseek-v4-flash |
| `\TthreeGemmaFourThreeOneBFirstSelected` | 31.5 | T3: % first-shown candidate selected, gemma-4-31b-it |
| `\TthreeGemmaFourThreeOneBFirstSelectedLo` | 20.8 | T3: % first-shown candidate selected, gemma-4-31b-it, lower 95% CI bound |
| `\TthreeGemmaFourThreeOneBFirstSelectedHi` | 42.6 | T3: % first-shown candidate selected, gemma-4-31b-it, upper 95% CI bound |
| `\TthreeGemmaFourThreeOneBFirstSelectedCI` | [20.8, 42.6] | T3: % first-shown candidate selected, gemma-4-31b-it, 95% CI |
| `\TthreeGemmaFourThreeOneBFirstSelectedN` | 54 | T3: % first-shown candidate selected, gemma-4-31b-it, n |
| `\TthreeGemmaFourThreeOneBFirstSelectedP` | n/a | T3: % first-shown candidate selected, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\TthreeGemmaFourThreeOneBFirstTop` | 42.6 | T3: % first-shown candidate top-rated, gemma-4-31b-it |
| `\TthreeGemmaFourThreeOneBFirstTopLo` | 32.7 | T3: % first-shown candidate top-rated, gemma-4-31b-it, lower 95% CI bound |
| `\TthreeGemmaFourThreeOneBFirstTopHi` | 51.8 | T3: % first-shown candidate top-rated, gemma-4-31b-it, upper 95% CI bound |
| `\TthreeGemmaFourThreeOneBFirstTopCI` | [32.7, 51.8] | T3: % first-shown candidate top-rated, gemma-4-31b-it, 95% CI |
| `\TthreeGemmaFourThreeOneBFirstTopN` | 54 | T3: % first-shown candidate top-rated, gemma-4-31b-it, n |
| `\TthreeGemmaFourThreeOneBFirstTopP` | n/a | T3: % first-shown candidate top-rated, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\TthreeGemmaFourThreeOneBChance` | 13.9 | T3: chance level of first-shown selection (%), gemma-4-31b-it |
| `\PfourNoneTZeroPooledAsr` | 61.0 | ASR (%), none T0, pooled |
| `\PfourNoneTZeroPooledAsrLo` | 46.7 | ASR (%), none T0, pooled, lower 95% CI bound |
| `\PfourNoneTZeroPooledAsrHi` | 75.0 | ASR (%), none T0, pooled, upper 95% CI bound |
| `\PfourNoneTZeroPooledAsrCI` | [46.7, 75.0] | ASR (%), none T0, pooled, 95% CI |
| `\PfourNoneTZeroPooledAsrN` | 59 | ASR (%), none T0, pooled, n |
| `\PfourNoneTZeroPooledAsrP` | n/a | ASR (%), none T0, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroPooledAsrDropped` | 61.0 | ASR (%) unparsed dropped, none T0, pooled |
| `\PfourNoneTZeroPooledAsrDroppedLo` | 45.8 | ASR (%) unparsed dropped, none T0, pooled, lower 95% CI bound |
| `\PfourNoneTZeroPooledAsrDroppedHi` | 75.0 | ASR (%) unparsed dropped, none T0, pooled, upper 95% CI bound |
| `\PfourNoneTZeroPooledAsrDroppedCI` | [45.8, 75.0] | ASR (%) unparsed dropped, none T0, pooled, 95% CI |
| `\PfourNoneTZeroPooledAsrDroppedN` | 59 | ASR (%) unparsed dropped, none T0, pooled, n |
| `\PfourNoneTZeroPooledAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T0, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroPooledAsrCleanOk` | 60.3 | ASR / clean correct (%), none T0, pooled |
| `\PfourNoneTZeroPooledAsrCleanOkLo` | 46.7 | ASR / clean correct (%), none T0, pooled, lower 95% CI bound |
| `\PfourNoneTZeroPooledAsrCleanOkHi` | 73.7 | ASR / clean correct (%), none T0, pooled, upper 95% CI bound |
| `\PfourNoneTZeroPooledAsrCleanOkCI` | [46.7, 73.7] | ASR / clean correct (%), none T0, pooled, 95% CI |
| `\PfourNoneTZeroPooledAsrCleanOkN` | 58 | ASR / clean correct (%), none T0, pooled, n |
| `\PfourNoneTZeroPooledAsrCleanOkP` | n/a | ASR / clean correct (%), none T0, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroPooledNonTargetAcc` | 97.9 | non-target accuracy (%), none T0, pooled |
| `\PfourNoneTZeroPooledNonTargetAccLo` | 94.3 | non-target accuracy (%), none T0, pooled, lower 95% CI bound |
| `\PfourNoneTZeroPooledNonTargetAccHi` | 100.0 | non-target accuracy (%), none T0, pooled, upper 95% CI bound |
| `\PfourNoneTZeroPooledNonTargetAccCI` | [94.3, 100.0] | non-target accuracy (%), none T0, pooled, 95% CI |
| `\PfourNoneTZeroPooledNonTargetAccN` | 236 | non-target accuracy (%), none T0, pooled, n |
| `\PfourNoneTZeroPooledNonTargetAccP` | n/a | non-target accuracy (%), none T0, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroDeepSeekVFourFlashAsr` | 43.3 | ASR (%), none T0, deepseek-v4-flash |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrLo` | 30.0 | ASR (%), none T0, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrHi` | 60.0 | ASR (%), none T0, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrCI` | [30.0, 60.0] | ASR (%), none T0, deepseek-v4-flash, 95% CI |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrN` | 30 | ASR (%), none T0, deepseek-v4-flash, n |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrP` | n/a | ASR (%), none T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrDropped` | 43.3 | ASR (%) unparsed dropped, none T0, deepseek-v4-flash |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrDroppedLo` | 30.0 | ASR (%) unparsed dropped, none T0, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrDroppedHi` | 60.0 | ASR (%) unparsed dropped, none T0, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrDroppedCI` | [30.0, 60.0] | ASR (%) unparsed dropped, none T0, deepseek-v4-flash, 95% CI |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrDroppedN` | 30 | ASR (%) unparsed dropped, none T0, deepseek-v4-flash, n |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrCleanOk` | 43.3 | ASR / clean correct (%), none T0, deepseek-v4-flash |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrCleanOkLo` | 30.0 | ASR / clean correct (%), none T0, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrCleanOkHi` | 60.0 | ASR / clean correct (%), none T0, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrCleanOkCI` | [30.0, 60.0] | ASR / clean correct (%), none T0, deepseek-v4-flash, 95% CI |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrCleanOkN` | 30 | ASR / clean correct (%), none T0, deepseek-v4-flash, n |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrCleanOkP` | n/a | ASR / clean correct (%), none T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroDeepSeekVFourFlashNonTargetAcc` | 100.0 | non-target accuracy (%), none T0, deepseek-v4-flash |
| `\PfourNoneTZeroDeepSeekVFourFlashNonTargetAccLo` | 97.0 | non-target accuracy (%), none T0, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTZeroDeepSeekVFourFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), none T0, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTZeroDeepSeekVFourFlashNonTargetAccCI` | [97.0, 100.0] | non-target accuracy (%), none T0, deepseek-v4-flash, 95% CI |
| `\PfourNoneTZeroDeepSeekVFourFlashNonTargetAccN` | 120 | non-target accuracy (%), none T0, deepseek-v4-flash, n |
| `\PfourNoneTZeroDeepSeekVFourFlashNonTargetAccP` | n/a | non-target accuracy (%), none T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGemmaFourThreeOneBAsr` | 79.3 | ASR (%), none T0, gemma-4-31b-it |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrLo` | 62.0 | ASR (%), none T0, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrHi` | 93.3 | ASR (%), none T0, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrCI` | [62.0, 93.3] | ASR (%), none T0, gemma-4-31b-it, 95% CI |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrN` | 29 | ASR (%), none T0, gemma-4-31b-it, n |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrP` | n/a | ASR (%), none T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrDropped` | 79.3 | ASR (%) unparsed dropped, none T0, gemma-4-31b-it |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrDroppedLo` | 62.1 | ASR (%) unparsed dropped, none T0, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrDroppedHi` | 93.3 | ASR (%) unparsed dropped, none T0, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrDroppedCI` | [62.1, 93.3] | ASR (%) unparsed dropped, none T0, gemma-4-31b-it, 95% CI |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrDroppedN` | 29 | ASR (%) unparsed dropped, none T0, gemma-4-31b-it, n |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrCleanOk` | 78.6 | ASR / clean correct (%), none T0, gemma-4-31b-it |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrCleanOkLo` | 60.7 | ASR / clean correct (%), none T0, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrCleanOkHi` | 92.9 | ASR / clean correct (%), none T0, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrCleanOkCI` | [60.7, 92.9] | ASR / clean correct (%), none T0, gemma-4-31b-it, 95% CI |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrCleanOkN` | 28 | ASR / clean correct (%), none T0, gemma-4-31b-it, n |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrCleanOkP` | n/a | ASR / clean correct (%), none T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGemmaFourThreeOneBNonTargetAcc` | 95.7 | non-target accuracy (%), none T0, gemma-4-31b-it |
| `\PfourNoneTZeroGemmaFourThreeOneBNonTargetAccLo` | 88.0 | non-target accuracy (%), none T0, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTZeroGemmaFourThreeOneBNonTargetAccHi` | 100.0 | non-target accuracy (%), none T0, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTZeroGemmaFourThreeOneBNonTargetAccCI` | [88.0, 100.0] | non-target accuracy (%), none T0, gemma-4-31b-it, 95% CI |
| `\PfourNoneTZeroGemmaFourThreeOneBNonTargetAccN` | 116 | non-target accuracy (%), none T0, gemma-4-31b-it, n |
| `\PfourNoneTZeroGemmaFourThreeOneBNonTargetAccP` | n/a | non-target accuracy (%), none T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoPooledAsr` | 74.1 | ASR (%), none T2, pooled |
| `\PfourNoneTTwoPooledAsrLo` | 63.8 | ASR (%), none T2, pooled, lower 95% CI bound |
| `\PfourNoneTTwoPooledAsrHi` | 86.4 | ASR (%), none T2, pooled, upper 95% CI bound |
| `\PfourNoneTTwoPooledAsrCI` | [63.8, 86.4] | ASR (%), none T2, pooled, 95% CI |
| `\PfourNoneTTwoPooledAsrN` | 58 | ASR (%), none T2, pooled, n |
| `\PfourNoneTTwoPooledAsrP` | n/a | ASR (%), none T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoPooledAsrDropped` | 74.1 | ASR (%) unparsed dropped, none T2, pooled |
| `\PfourNoneTTwoPooledAsrDroppedLo` | 63.8 | ASR (%) unparsed dropped, none T2, pooled, lower 95% CI bound |
| `\PfourNoneTTwoPooledAsrDroppedHi` | 86.4 | ASR (%) unparsed dropped, none T2, pooled, upper 95% CI bound |
| `\PfourNoneTTwoPooledAsrDroppedCI` | [63.8, 86.4] | ASR (%) unparsed dropped, none T2, pooled, 95% CI |
| `\PfourNoneTTwoPooledAsrDroppedN` | 58 | ASR (%) unparsed dropped, none T2, pooled, n |
| `\PfourNoneTTwoPooledAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoPooledAsrCleanOk` | 73.7 | ASR / clean correct (%), none T2, pooled |
| `\PfourNoneTTwoPooledAsrCleanOkLo` | 63.8 | ASR / clean correct (%), none T2, pooled, lower 95% CI bound |
| `\PfourNoneTTwoPooledAsrCleanOkHi` | 85.7 | ASR / clean correct (%), none T2, pooled, upper 95% CI bound |
| `\PfourNoneTTwoPooledAsrCleanOkCI` | [63.8, 85.7] | ASR / clean correct (%), none T2, pooled, 95% CI |
| `\PfourNoneTTwoPooledAsrCleanOkN` | 57 | ASR / clean correct (%), none T2, pooled, n |
| `\PfourNoneTTwoPooledAsrCleanOkP` | n/a | ASR / clean correct (%), none T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoPooledNonTargetAcc` | 97.8 | non-target accuracy (%), none T2, pooled |
| `\PfourNoneTTwoPooledNonTargetAccLo` | 94.3 | non-target accuracy (%), none T2, pooled, lower 95% CI bound |
| `\PfourNoneTTwoPooledNonTargetAccHi` | 100.0 | non-target accuracy (%), none T2, pooled, upper 95% CI bound |
| `\PfourNoneTTwoPooledNonTargetAccCI` | [94.3, 100.0] | non-target accuracy (%), none T2, pooled, 95% CI |
| `\PfourNoneTTwoPooledNonTargetAccN` | 232 | non-target accuracy (%), none T2, pooled, n |
| `\PfourNoneTTwoPooledNonTargetAccP` | n/a | non-target accuracy (%), none T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoDeepSeekVFourFlashAsr` | 66.7 | ASR (%), none T2, deepseek-v4-flash |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrLo` | 60.0 | ASR (%), none T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrHi` | 80.0 | ASR (%), none T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrCI` | [60.0, 80.0] | ASR (%), none T2, deepseek-v4-flash, 95% CI |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrN` | 30 | ASR (%), none T2, deepseek-v4-flash, n |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrP` | n/a | ASR (%), none T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrDropped` | 66.7 | ASR (%) unparsed dropped, none T2, deepseek-v4-flash |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrDroppedLo` | 60.0 | ASR (%) unparsed dropped, none T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrDroppedHi` | 80.0 | ASR (%) unparsed dropped, none T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrDroppedCI` | [60.0, 80.0] | ASR (%) unparsed dropped, none T2, deepseek-v4-flash, 95% CI |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrDroppedN` | 30 | ASR (%) unparsed dropped, none T2, deepseek-v4-flash, n |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrCleanOk` | 66.7 | ASR / clean correct (%), none T2, deepseek-v4-flash |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrCleanOkLo` | 60.0 | ASR / clean correct (%), none T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrCleanOkHi` | 80.0 | ASR / clean correct (%), none T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrCleanOkCI` | [60.0, 80.0] | ASR / clean correct (%), none T2, deepseek-v4-flash, 95% CI |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrCleanOkN` | 30 | ASR / clean correct (%), none T2, deepseek-v4-flash, n |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrCleanOkP` | n/a | ASR / clean correct (%), none T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoDeepSeekVFourFlashNonTargetAcc` | 100.0 | non-target accuracy (%), none T2, deepseek-v4-flash |
| `\PfourNoneTTwoDeepSeekVFourFlashNonTargetAccLo` | 97.0 | non-target accuracy (%), none T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTTwoDeepSeekVFourFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), none T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTTwoDeepSeekVFourFlashNonTargetAccCI` | [97.0, 100.0] | non-target accuracy (%), none T2, deepseek-v4-flash, 95% CI |
| `\PfourNoneTTwoDeepSeekVFourFlashNonTargetAccN` | 120 | non-target accuracy (%), none T2, deepseek-v4-flash, n |
| `\PfourNoneTTwoDeepSeekVFourFlashNonTargetAccP` | n/a | non-target accuracy (%), none T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGemmaFourThreeOneBAsr` | 82.1 | ASR (%), none T2, gemma-4-31b-it |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrLo` | 66.7 | ASR (%), none T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrHi` | 96.4 | ASR (%), none T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrCI` | [66.7, 96.4] | ASR (%), none T2, gemma-4-31b-it, 95% CI |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrN` | 28 | ASR (%), none T2, gemma-4-31b-it, n |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrP` | n/a | ASR (%), none T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrDropped` | 82.1 | ASR (%) unparsed dropped, none T2, gemma-4-31b-it |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrDroppedLo` | 67.8 | ASR (%) unparsed dropped, none T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrDroppedHi` | 96.4 | ASR (%) unparsed dropped, none T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrDroppedCI` | [67.8, 96.4] | ASR (%) unparsed dropped, none T2, gemma-4-31b-it, 95% CI |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrDroppedN` | 28 | ASR (%) unparsed dropped, none T2, gemma-4-31b-it, n |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrCleanOk` | 81.5 | ASR / clean correct (%), none T2, gemma-4-31b-it |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrCleanOkLo` | 66.7 | ASR / clean correct (%), none T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrCleanOkHi` | 96.2 | ASR / clean correct (%), none T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrCleanOkCI` | [66.7, 96.2] | ASR / clean correct (%), none T2, gemma-4-31b-it, 95% CI |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrCleanOkN` | 27 | ASR / clean correct (%), none T2, gemma-4-31b-it, n |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrCleanOkP` | n/a | ASR / clean correct (%), none T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGemmaFourThreeOneBNonTargetAcc` | 95.5 | non-target accuracy (%), none T2, gemma-4-31b-it |
| `\PfourNoneTTwoGemmaFourThreeOneBNonTargetAccLo` | 88.0 | non-target accuracy (%), none T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTTwoGemmaFourThreeOneBNonTargetAccHi` | 100.0 | non-target accuracy (%), none T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTTwoGemmaFourThreeOneBNonTargetAccCI` | [88.0, 100.0] | non-target accuracy (%), none T2, gemma-4-31b-it, 95% CI |
| `\PfourNoneTTwoGemmaFourThreeOneBNonTargetAccN` | 112 | non-target accuracy (%), none T2, gemma-4-31b-it, n |
| `\PfourNoneTTwoGemmaFourThreeOneBNonTargetAccP` | n/a | non-target accuracy (%), none T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreePooledAsr` | 69.6 | ASR (%), none T3, pooled |
| `\PfourNoneTThreePooledAsrLo` | 56.9 | ASR (%), none T3, pooled, lower 95% CI bound |
| `\PfourNoneTThreePooledAsrHi` | 85.2 | ASR (%), none T3, pooled, upper 95% CI bound |
| `\PfourNoneTThreePooledAsrCI` | [56.9, 85.2] | ASR (%), none T3, pooled, 95% CI |
| `\PfourNoneTThreePooledAsrN` | 56 | ASR (%), none T3, pooled, n |
| `\PfourNoneTThreePooledAsrP` | n/a | ASR (%), none T3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreePooledAsrDropped` | 69.6 | ASR (%) unparsed dropped, none T3, pooled |
| `\PfourNoneTThreePooledAsrDroppedLo` | 56.9 | ASR (%) unparsed dropped, none T3, pooled, lower 95% CI bound |
| `\PfourNoneTThreePooledAsrDroppedHi` | 83.6 | ASR (%) unparsed dropped, none T3, pooled, upper 95% CI bound |
| `\PfourNoneTThreePooledAsrDroppedCI` | [56.9, 83.6] | ASR (%) unparsed dropped, none T3, pooled, 95% CI |
| `\PfourNoneTThreePooledAsrDroppedN` | 56 | ASR (%) unparsed dropped, none T3, pooled, n |
| `\PfourNoneTThreePooledAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreePooledAsrCleanOk` | 69.6 | ASR / clean correct (%), none T3, pooled |
| `\PfourNoneTThreePooledAsrCleanOkLo` | 56.9 | ASR / clean correct (%), none T3, pooled, lower 95% CI bound |
| `\PfourNoneTThreePooledAsrCleanOkHi` | 83.6 | ASR / clean correct (%), none T3, pooled, upper 95% CI bound |
| `\PfourNoneTThreePooledAsrCleanOkCI` | [56.9, 83.6] | ASR / clean correct (%), none T3, pooled, 95% CI |
| `\PfourNoneTThreePooledAsrCleanOkN` | 56 | ASR / clean correct (%), none T3, pooled, n |
| `\PfourNoneTThreePooledAsrCleanOkP` | n/a | ASR / clean correct (%), none T3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreePooledNonTargetAcc` | 97.3 | non-target accuracy (%), none T3, pooled |
| `\PfourNoneTThreePooledNonTargetAccLo` | 93.6 | non-target accuracy (%), none T3, pooled, lower 95% CI bound |
| `\PfourNoneTThreePooledNonTargetAccHi` | 100.0 | non-target accuracy (%), none T3, pooled, upper 95% CI bound |
| `\PfourNoneTThreePooledNonTargetAccCI` | [93.6, 100.0] | non-target accuracy (%), none T3, pooled, 95% CI |
| `\PfourNoneTThreePooledNonTargetAccN` | 224 | non-target accuracy (%), none T3, pooled, n |
| `\PfourNoneTThreePooledNonTargetAccP` | n/a | non-target accuracy (%), none T3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeDeepSeekVFourFlashAsr` | 62.1 | ASR (%), none T3, deepseek-v4-flash |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrLo` | 48.3 | ASR (%), none T3, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrHi` | 79.3 | ASR (%), none T3, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrCI` | [48.3, 79.3] | ASR (%), none T3, deepseek-v4-flash, 95% CI |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrN` | 29 | ASR (%), none T3, deepseek-v4-flash, n |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrP` | n/a | ASR (%), none T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrDropped` | 62.1 | ASR (%) unparsed dropped, none T3, deepseek-v4-flash |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrDroppedLo` | 50.0 | ASR (%) unparsed dropped, none T3, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrDroppedHi` | 79.3 | ASR (%) unparsed dropped, none T3, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrDroppedCI` | [50.0, 79.3] | ASR (%) unparsed dropped, none T3, deepseek-v4-flash, 95% CI |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrDroppedN` | 29 | ASR (%) unparsed dropped, none T3, deepseek-v4-flash, n |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrCleanOk` | 62.1 | ASR / clean correct (%), none T3, deepseek-v4-flash |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrCleanOkLo` | 48.3 | ASR / clean correct (%), none T3, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrCleanOkHi` | 79.3 | ASR / clean correct (%), none T3, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrCleanOkCI` | [48.3, 79.3] | ASR / clean correct (%), none T3, deepseek-v4-flash, 95% CI |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrCleanOkN` | 29 | ASR / clean correct (%), none T3, deepseek-v4-flash, n |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrCleanOkP` | n/a | ASR / clean correct (%), none T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeDeepSeekVFourFlashNonTargetAcc` | 100.0 | non-target accuracy (%), none T3, deepseek-v4-flash |
| `\PfourNoneTThreeDeepSeekVFourFlashNonTargetAccLo` | 96.9 | non-target accuracy (%), none T3, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTThreeDeepSeekVFourFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), none T3, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTThreeDeepSeekVFourFlashNonTargetAccCI` | [96.9, 100.0] | non-target accuracy (%), none T3, deepseek-v4-flash, 95% CI |
| `\PfourNoneTThreeDeepSeekVFourFlashNonTargetAccN` | 116 | non-target accuracy (%), none T3, deepseek-v4-flash, n |
| `\PfourNoneTThreeDeepSeekVFourFlashNonTargetAccP` | n/a | non-target accuracy (%), none T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGemmaFourThreeOneBAsr` | 77.8 | ASR (%), none T3, gemma-4-31b-it |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrLo` | 58.6 | ASR (%), none T3, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrHi` | 96.2 | ASR (%), none T3, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrCI` | [58.6, 96.2] | ASR (%), none T3, gemma-4-31b-it, 95% CI |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrN` | 27 | ASR (%), none T3, gemma-4-31b-it, n |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrP` | n/a | ASR (%), none T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrDropped` | 77.8 | ASR (%) unparsed dropped, none T3, gemma-4-31b-it |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrDroppedLo` | 57.1 | ASR (%) unparsed dropped, none T3, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrDroppedHi` | 96.3 | ASR (%) unparsed dropped, none T3, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrDroppedCI` | [57.1, 96.3] | ASR (%) unparsed dropped, none T3, gemma-4-31b-it, 95% CI |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrDroppedN` | 27 | ASR (%) unparsed dropped, none T3, gemma-4-31b-it, n |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrCleanOk` | 77.8 | ASR / clean correct (%), none T3, gemma-4-31b-it |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrCleanOkLo` | 58.6 | ASR / clean correct (%), none T3, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrCleanOkHi` | 96.2 | ASR / clean correct (%), none T3, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrCleanOkCI` | [58.6, 96.2] | ASR / clean correct (%), none T3, gemma-4-31b-it, 95% CI |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrCleanOkN` | 27 | ASR / clean correct (%), none T3, gemma-4-31b-it, n |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrCleanOkP` | n/a | ASR / clean correct (%), none T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGemmaFourThreeOneBNonTargetAcc` | 94.4 | non-target accuracy (%), none T3, gemma-4-31b-it |
| `\PfourNoneTThreeGemmaFourThreeOneBNonTargetAccLo` | 86.0 | non-target accuracy (%), none T3, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTThreeGemmaFourThreeOneBNonTargetAccHi` | 100.0 | non-target accuracy (%), none T3, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTThreeGemmaFourThreeOneBNonTargetAccCI` | [86.0, 100.0] | non-target accuracy (%), none T3, gemma-4-31b-it, 95% CI |
| `\PfourNoneTThreeGemmaFourThreeOneBNonTargetAccN` | 108 | non-target accuracy (%), none T3, gemma-4-31b-it, n |
| `\PfourNoneTThreeGemmaFourThreeOneBNonTargetAccP` | n/a | non-target accuracy (%), none T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryPooledAsr` | 16.9 | ASR (%), no_memory -, pooled |
| `\PfourNoMemoryPooledAsrLo` | 8.5 | ASR (%), no_memory -, pooled, lower 95% CI bound |
| `\PfourNoMemoryPooledAsrHi` | 25.4 | ASR (%), no_memory -, pooled, upper 95% CI bound |
| `\PfourNoMemoryPooledAsrCI` | [8.5, 25.4] | ASR (%), no_memory -, pooled, 95% CI |
| `\PfourNoMemoryPooledAsrN` | 59 | ASR (%), no_memory -, pooled, n |
| `\PfourNoMemoryPooledAsrP` | n/a | ASR (%), no_memory -, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryPooledAsrDropped` | 16.9 | ASR (%) unparsed dropped, no_memory -, pooled |
| `\PfourNoMemoryPooledAsrDroppedLo` | 8.3 | ASR (%) unparsed dropped, no_memory -, pooled, lower 95% CI bound |
| `\PfourNoMemoryPooledAsrDroppedHi` | 26.7 | ASR (%) unparsed dropped, no_memory -, pooled, upper 95% CI bound |
| `\PfourNoMemoryPooledAsrDroppedCI` | [8.3, 26.7] | ASR (%) unparsed dropped, no_memory -, pooled, 95% CI |
| `\PfourNoMemoryPooledAsrDroppedN` | 59 | ASR (%) unparsed dropped, no_memory -, pooled, n |
| `\PfourNoMemoryPooledAsrDroppedP` | n/a | ASR (%) unparsed dropped, no_memory -, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryPooledAsrCleanOk` | 15.5 | ASR / clean correct (%), no_memory -, pooled |
| `\PfourNoMemoryPooledAsrCleanOkLo` | 6.7 | ASR / clean correct (%), no_memory -, pooled, lower 95% CI bound |
| `\PfourNoMemoryPooledAsrCleanOkHi` | 25.4 | ASR / clean correct (%), no_memory -, pooled, upper 95% CI bound |
| `\PfourNoMemoryPooledAsrCleanOkCI` | [6.7, 25.4] | ASR / clean correct (%), no_memory -, pooled, 95% CI |
| `\PfourNoMemoryPooledAsrCleanOkN` | 58 | ASR / clean correct (%), no_memory -, pooled, n |
| `\PfourNoMemoryPooledAsrCleanOkP` | n/a | ASR / clean correct (%), no_memory -, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryPooledNonTargetAcc` | 96.6 | non-target accuracy (%), no_memory -, pooled |
| `\PfourNoMemoryPooledNonTargetAccLo` | 93.1 | non-target accuracy (%), no_memory -, pooled, lower 95% CI bound |
| `\PfourNoMemoryPooledNonTargetAccHi` | 99.2 | non-target accuracy (%), no_memory -, pooled, upper 95% CI bound |
| `\PfourNoMemoryPooledNonTargetAccCI` | [93.1, 99.2] | non-target accuracy (%), no_memory -, pooled, 95% CI |
| `\PfourNoMemoryPooledNonTargetAccN` | 236 | non-target accuracy (%), no_memory -, pooled, n |
| `\PfourNoMemoryPooledNonTargetAccP` | n/a | non-target accuracy (%), no_memory -, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryDeepSeekVFourFlashAsr` | 20.0 | ASR (%), no_memory -, deepseek-v4-flash |
| `\PfourNoMemoryDeepSeekVFourFlashAsrLo` | 6.7 | ASR (%), no_memory -, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoMemoryDeepSeekVFourFlashAsrHi` | 33.3 | ASR (%), no_memory -, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoMemoryDeepSeekVFourFlashAsrCI` | [6.7, 33.3] | ASR (%), no_memory -, deepseek-v4-flash, 95% CI |
| `\PfourNoMemoryDeepSeekVFourFlashAsrN` | 30 | ASR (%), no_memory -, deepseek-v4-flash, n |
| `\PfourNoMemoryDeepSeekVFourFlashAsrP` | n/a | ASR (%), no_memory -, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryDeepSeekVFourFlashAsrDropped` | 20.0 | ASR (%) unparsed dropped, no_memory -, deepseek-v4-flash |
| `\PfourNoMemoryDeepSeekVFourFlashAsrDroppedLo` | 6.7 | ASR (%) unparsed dropped, no_memory -, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoMemoryDeepSeekVFourFlashAsrDroppedHi` | 33.3 | ASR (%) unparsed dropped, no_memory -, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoMemoryDeepSeekVFourFlashAsrDroppedCI` | [6.7, 33.3] | ASR (%) unparsed dropped, no_memory -, deepseek-v4-flash, 95% CI |
| `\PfourNoMemoryDeepSeekVFourFlashAsrDroppedN` | 30 | ASR (%) unparsed dropped, no_memory -, deepseek-v4-flash, n |
| `\PfourNoMemoryDeepSeekVFourFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, no_memory -, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryDeepSeekVFourFlashAsrCleanOk` | 20.0 | ASR / clean correct (%), no_memory -, deepseek-v4-flash |
| `\PfourNoMemoryDeepSeekVFourFlashAsrCleanOkLo` | 6.7 | ASR / clean correct (%), no_memory -, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoMemoryDeepSeekVFourFlashAsrCleanOkHi` | 33.3 | ASR / clean correct (%), no_memory -, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoMemoryDeepSeekVFourFlashAsrCleanOkCI` | [6.7, 33.3] | ASR / clean correct (%), no_memory -, deepseek-v4-flash, 95% CI |
| `\PfourNoMemoryDeepSeekVFourFlashAsrCleanOkN` | 30 | ASR / clean correct (%), no_memory -, deepseek-v4-flash, n |
| `\PfourNoMemoryDeepSeekVFourFlashAsrCleanOkP` | n/a | ASR / clean correct (%), no_memory -, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryDeepSeekVFourFlashNonTargetAcc` | 100.0 | non-target accuracy (%), no_memory -, deepseek-v4-flash |
| `\PfourNoMemoryDeepSeekVFourFlashNonTargetAccLo` | 97.0 | non-target accuracy (%), no_memory -, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoMemoryDeepSeekVFourFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), no_memory -, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoMemoryDeepSeekVFourFlashNonTargetAccCI` | [97.0, 100.0] | non-target accuracy (%), no_memory -, deepseek-v4-flash, 95% CI |
| `\PfourNoMemoryDeepSeekVFourFlashNonTargetAccN` | 120 | non-target accuracy (%), no_memory -, deepseek-v4-flash, n |
| `\PfourNoMemoryDeepSeekVFourFlashNonTargetAccP` | n/a | non-target accuracy (%), no_memory -, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGemmaFourThreeOneBAsr` | 13.8 | ASR (%), no_memory -, gemma-4-31b-it |
| `\PfourNoMemoryGemmaFourThreeOneBAsrLo` | 3.3 | ASR (%), no_memory -, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoMemoryGemmaFourThreeOneBAsrHi` | 26.7 | ASR (%), no_memory -, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoMemoryGemmaFourThreeOneBAsrCI` | [3.3, 26.7] | ASR (%), no_memory -, gemma-4-31b-it, 95% CI |
| `\PfourNoMemoryGemmaFourThreeOneBAsrN` | 29 | ASR (%), no_memory -, gemma-4-31b-it, n |
| `\PfourNoMemoryGemmaFourThreeOneBAsrP` | n/a | ASR (%), no_memory -, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGemmaFourThreeOneBAsrDropped` | 13.8 | ASR (%) unparsed dropped, no_memory -, gemma-4-31b-it |
| `\PfourNoMemoryGemmaFourThreeOneBAsrDroppedLo` | 3.4 | ASR (%) unparsed dropped, no_memory -, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoMemoryGemmaFourThreeOneBAsrDroppedHi` | 26.7 | ASR (%) unparsed dropped, no_memory -, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoMemoryGemmaFourThreeOneBAsrDroppedCI` | [3.4, 26.7] | ASR (%) unparsed dropped, no_memory -, gemma-4-31b-it, 95% CI |
| `\PfourNoMemoryGemmaFourThreeOneBAsrDroppedN` | 29 | ASR (%) unparsed dropped, no_memory -, gemma-4-31b-it, n |
| `\PfourNoMemoryGemmaFourThreeOneBAsrDroppedP` | n/a | ASR (%) unparsed dropped, no_memory -, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGemmaFourThreeOneBAsrCleanOk` | 10.7 | ASR / clean correct (%), no_memory -, gemma-4-31b-it |
| `\PfourNoMemoryGemmaFourThreeOneBAsrCleanOkLo` | 0.0 | ASR / clean correct (%), no_memory -, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoMemoryGemmaFourThreeOneBAsrCleanOkHi` | 24.1 | ASR / clean correct (%), no_memory -, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoMemoryGemmaFourThreeOneBAsrCleanOkCI` | [0.0, 24.1] | ASR / clean correct (%), no_memory -, gemma-4-31b-it, 95% CI |
| `\PfourNoMemoryGemmaFourThreeOneBAsrCleanOkN` | 28 | ASR / clean correct (%), no_memory -, gemma-4-31b-it, n |
| `\PfourNoMemoryGemmaFourThreeOneBAsrCleanOkP` | n/a | ASR / clean correct (%), no_memory -, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGemmaFourThreeOneBNonTargetAcc` | 93.1 | non-target accuracy (%), no_memory -, gemma-4-31b-it |
| `\PfourNoMemoryGemmaFourThreeOneBNonTargetAccLo` | 85.2 | non-target accuracy (%), no_memory -, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoMemoryGemmaFourThreeOneBNonTargetAccHi` | 98.3 | non-target accuracy (%), no_memory -, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoMemoryGemmaFourThreeOneBNonTargetAccCI` | [85.2, 98.3] | non-target accuracy (%), no_memory -, gemma-4-31b-it, 95% CI |
| `\PfourNoMemoryGemmaFourThreeOneBNonTargetAccN` | 116 | non-target accuracy (%), no_memory -, gemma-4-31b-it, n |
| `\PfourNoMemoryGemmaFourThreeOneBNonTargetAccP` | n/a | non-target accuracy (%), no_memory -, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoPooledAsr` | 75.9 | ASR (%), G2u T2, pooled |
| `\PfourGTwoUTTwoPooledAsrLo` | 66.7 | ASR (%), G2u T2, pooled, lower 95% CI bound |
| `\PfourGTwoUTTwoPooledAsrHi` | 86.4 | ASR (%), G2u T2, pooled, upper 95% CI bound |
| `\PfourGTwoUTTwoPooledAsrCI` | [66.7, 86.4] | ASR (%), G2u T2, pooled, 95% CI |
| `\PfourGTwoUTTwoPooledAsrN` | 58 | ASR (%), G2u T2, pooled, n |
| `\PfourGTwoUTTwoPooledAsrP` | n/a | ASR (%), G2u T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoPooledAsrDropped` | 75.9 | ASR (%) unparsed dropped, G2u T2, pooled |
| `\PfourGTwoUTTwoPooledAsrDroppedLo` | 66.7 | ASR (%) unparsed dropped, G2u T2, pooled, lower 95% CI bound |
| `\PfourGTwoUTTwoPooledAsrDroppedHi` | 86.7 | ASR (%) unparsed dropped, G2u T2, pooled, upper 95% CI bound |
| `\PfourGTwoUTTwoPooledAsrDroppedCI` | [66.7, 86.7] | ASR (%) unparsed dropped, G2u T2, pooled, 95% CI |
| `\PfourGTwoUTTwoPooledAsrDroppedN` | 58 | ASR (%) unparsed dropped, G2u T2, pooled, n |
| `\PfourGTwoUTTwoPooledAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2u T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoPooledAsrCleanOk` | 75.0 | ASR / clean correct (%), G2u T2, pooled |
| `\PfourGTwoUTTwoPooledAsrCleanOkLo` | 66.1 | ASR / clean correct (%), G2u T2, pooled, lower 95% CI bound |
| `\PfourGTwoUTTwoPooledAsrCleanOkHi` | 85.7 | ASR / clean correct (%), G2u T2, pooled, upper 95% CI bound |
| `\PfourGTwoUTTwoPooledAsrCleanOkCI` | [66.1, 85.7] | ASR / clean correct (%), G2u T2, pooled, 95% CI |
| `\PfourGTwoUTTwoPooledAsrCleanOkN` | 56 | ASR / clean correct (%), G2u T2, pooled, n |
| `\PfourGTwoUTTwoPooledAsrCleanOkP` | n/a | ASR / clean correct (%), G2u T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoPooledNonTargetAcc` | 97.0 | non-target accuracy (%), G2u T2, pooled |
| `\PfourGTwoUTTwoPooledNonTargetAccLo` | 93.3 | non-target accuracy (%), G2u T2, pooled, lower 95% CI bound |
| `\PfourGTwoUTTwoPooledNonTargetAccHi` | 100.0 | non-target accuracy (%), G2u T2, pooled, upper 95% CI bound |
| `\PfourGTwoUTTwoPooledNonTargetAccCI` | [93.3, 100.0] | non-target accuracy (%), G2u T2, pooled, 95% CI |
| `\PfourGTwoUTTwoPooledNonTargetAccN` | 232 | non-target accuracy (%), G2u T2, pooled, n |
| `\PfourGTwoUTTwoPooledNonTargetAccP` | n/a | non-target accuracy (%), G2u T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsr` | 70.0 | ASR (%), G2u T2, deepseek-v4-flash |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrLo` | 60.0 | ASR (%), G2u T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrHi` | 83.3 | ASR (%), G2u T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrCI` | [60.0, 83.3] | ASR (%), G2u T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrN` | 30 | ASR (%), G2u T2, deepseek-v4-flash, n |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrP` | n/a | ASR (%), G2u T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrDropped` | 70.0 | ASR (%) unparsed dropped, G2u T2, deepseek-v4-flash |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrDroppedLo` | 60.0 | ASR (%) unparsed dropped, G2u T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrDroppedHi` | 83.3 | ASR (%) unparsed dropped, G2u T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrDroppedCI` | [60.0, 83.3] | ASR (%) unparsed dropped, G2u T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrDroppedN` | 30 | ASR (%) unparsed dropped, G2u T2, deepseek-v4-flash, n |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2u T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrCleanOk` | 70.0 | ASR / clean correct (%), G2u T2, deepseek-v4-flash |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrCleanOkLo` | 60.0 | ASR / clean correct (%), G2u T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrCleanOkHi` | 83.3 | ASR / clean correct (%), G2u T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrCleanOkCI` | [60.0, 83.3] | ASR / clean correct (%), G2u T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrCleanOkN` | 30 | ASR / clean correct (%), G2u T2, deepseek-v4-flash, n |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrCleanOkP` | n/a | ASR / clean correct (%), G2u T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoDeepSeekVFourFlashNonTargetAcc` | 100.0 | non-target accuracy (%), G2u T2, deepseek-v4-flash |
| `\PfourGTwoUTTwoDeepSeekVFourFlashNonTargetAccLo` | 97.0 | non-target accuracy (%), G2u T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoUTTwoDeepSeekVFourFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), G2u T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoUTTwoDeepSeekVFourFlashNonTargetAccCI` | [97.0, 100.0] | non-target accuracy (%), G2u T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoUTTwoDeepSeekVFourFlashNonTargetAccN` | 120 | non-target accuracy (%), G2u T2, deepseek-v4-flash, n |
| `\PfourGTwoUTTwoDeepSeekVFourFlashNonTargetAccP` | n/a | non-target accuracy (%), G2u T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsr` | 82.1 | ASR (%), G2u T2, gemma-4-31b-it |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrLo` | 67.9 | ASR (%), G2u T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrHi` | 96.4 | ASR (%), G2u T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrCI` | [67.9, 96.4] | ASR (%), G2u T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrN` | 28 | ASR (%), G2u T2, gemma-4-31b-it, n |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrP` | n/a | ASR (%), G2u T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrDropped` | 82.1 | ASR (%) unparsed dropped, G2u T2, gemma-4-31b-it |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrDroppedLo` | 66.7 | ASR (%) unparsed dropped, G2u T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrDroppedHi` | 96.4 | ASR (%) unparsed dropped, G2u T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrDroppedCI` | [66.7, 96.4] | ASR (%) unparsed dropped, G2u T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrDroppedN` | 28 | ASR (%) unparsed dropped, G2u T2, gemma-4-31b-it, n |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2u T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrCleanOk` | 80.8 | ASR / clean correct (%), G2u T2, gemma-4-31b-it |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrCleanOkLo` | 66.7 | ASR / clean correct (%), G2u T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrCleanOkHi` | 96.0 | ASR / clean correct (%), G2u T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrCleanOkCI` | [66.7, 96.0] | ASR / clean correct (%), G2u T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrCleanOkN` | 26 | ASR / clean correct (%), G2u T2, gemma-4-31b-it, n |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrCleanOkP` | n/a | ASR / clean correct (%), G2u T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGemmaFourThreeOneBNonTargetAcc` | 93.8 | non-target accuracy (%), G2u T2, gemma-4-31b-it |
| `\PfourGTwoUTTwoGemmaFourThreeOneBNonTargetAccLo` | 85.6 | non-target accuracy (%), G2u T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoUTTwoGemmaFourThreeOneBNonTargetAccHi` | 100.0 | non-target accuracy (%), G2u T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoUTTwoGemmaFourThreeOneBNonTargetAccCI` | [85.6, 100.0] | non-target accuracy (%), G2u T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoUTTwoGemmaFourThreeOneBNonTargetAccN` | 112 | non-target accuracy (%), G2u T2, gemma-4-31b-it, n |
| `\PfourGTwoUTTwoGemmaFourThreeOneBNonTargetAccP` | n/a | non-target accuracy (%), G2u T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoPooledAsr` | 29.3 | ASR (%), G2s T2, pooled |
| `\PfourGTwoSTTwoPooledAsrLo` | 22.8 | ASR (%), G2s T2, pooled, lower 95% CI bound |
| `\PfourGTwoSTTwoPooledAsrHi` | 35.6 | ASR (%), G2s T2, pooled, upper 95% CI bound |
| `\PfourGTwoSTTwoPooledAsrCI` | [22.8, 35.6] | ASR (%), G2s T2, pooled, 95% CI |
| `\PfourGTwoSTTwoPooledAsrN` | 58 | ASR (%), G2s T2, pooled, n |
| `\PfourGTwoSTTwoPooledAsrP` | n/a | ASR (%), G2s T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoPooledAsrDropped` | 30.4 | ASR (%) unparsed dropped, G2s T2, pooled |
| `\PfourGTwoSTTwoPooledAsrDroppedLo` | 22.8 | ASR (%) unparsed dropped, G2s T2, pooled, lower 95% CI bound |
| `\PfourGTwoSTTwoPooledAsrDroppedHi` | 38.2 | ASR (%) unparsed dropped, G2s T2, pooled, upper 95% CI bound |
| `\PfourGTwoSTTwoPooledAsrDroppedCI` | [22.8, 38.2] | ASR (%) unparsed dropped, G2s T2, pooled, 95% CI |
| `\PfourGTwoSTTwoPooledAsrDroppedN` | 56 | ASR (%) unparsed dropped, G2s T2, pooled, n |
| `\PfourGTwoSTTwoPooledAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2s T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoPooledAsrCleanOk` | 30.9 | ASR / clean correct (%), G2s T2, pooled |
| `\PfourGTwoSTTwoPooledAsrCleanOkLo` | 23.2 | ASR / clean correct (%), G2s T2, pooled, lower 95% CI bound |
| `\PfourGTwoSTTwoPooledAsrCleanOkHi` | 40.0 | ASR / clean correct (%), G2s T2, pooled, upper 95% CI bound |
| `\PfourGTwoSTTwoPooledAsrCleanOkCI` | [23.2, 40.0] | ASR / clean correct (%), G2s T2, pooled, 95% CI |
| `\PfourGTwoSTTwoPooledAsrCleanOkN` | 55 | ASR / clean correct (%), G2s T2, pooled, n |
| `\PfourGTwoSTTwoPooledAsrCleanOkP` | n/a | ASR / clean correct (%), G2s T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoPooledNonTargetAcc` | 96.4 | non-target accuracy (%), G2s T2, pooled |
| `\PfourGTwoSTTwoPooledNonTargetAccLo` | 92.7 | non-target accuracy (%), G2s T2, pooled, lower 95% CI bound |
| `\PfourGTwoSTTwoPooledNonTargetAccHi` | 99.6 | non-target accuracy (%), G2s T2, pooled, upper 95% CI bound |
| `\PfourGTwoSTTwoPooledNonTargetAccCI` | [92.7, 99.6] | non-target accuracy (%), G2s T2, pooled, 95% CI |
| `\PfourGTwoSTTwoPooledNonTargetAccN` | 224 | non-target accuracy (%), G2s T2, pooled, n |
| `\PfourGTwoSTTwoPooledNonTargetAccP` | n/a | non-target accuracy (%), G2s T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsr` | 50.0 | ASR (%), G2s T2, deepseek-v4-flash |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrLo` | 40.0 | ASR (%), G2s T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrHi` | 63.3 | ASR (%), G2s T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrCI` | [40.0, 63.3] | ASR (%), G2s T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrN` | 30 | ASR (%), G2s T2, deepseek-v4-flash, n |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrP` | n/a | ASR (%), G2s T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrDropped` | 50.0 | ASR (%) unparsed dropped, G2s T2, deepseek-v4-flash |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrDroppedLo` | 40.0 | ASR (%) unparsed dropped, G2s T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrDroppedHi` | 63.3 | ASR (%) unparsed dropped, G2s T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrDroppedCI` | [40.0, 63.3] | ASR (%) unparsed dropped, G2s T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrDroppedN` | 30 | ASR (%) unparsed dropped, G2s T2, deepseek-v4-flash, n |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2s T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrCleanOk` | 50.0 | ASR / clean correct (%), G2s T2, deepseek-v4-flash |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrCleanOkLo` | 40.0 | ASR / clean correct (%), G2s T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrCleanOkHi` | 63.3 | ASR / clean correct (%), G2s T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrCleanOkCI` | [40.0, 63.3] | ASR / clean correct (%), G2s T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrCleanOkN` | 30 | ASR / clean correct (%), G2s T2, deepseek-v4-flash, n |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrCleanOkP` | n/a | ASR / clean correct (%), G2s T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoDeepSeekVFourFlashNonTargetAcc` | 100.0 | non-target accuracy (%), G2s T2, deepseek-v4-flash |
| `\PfourGTwoSTTwoDeepSeekVFourFlashNonTargetAccLo` | 97.0 | non-target accuracy (%), G2s T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoSTTwoDeepSeekVFourFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), G2s T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoSTTwoDeepSeekVFourFlashNonTargetAccCI` | [97.0, 100.0] | non-target accuracy (%), G2s T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoSTTwoDeepSeekVFourFlashNonTargetAccN` | 120 | non-target accuracy (%), G2s T2, deepseek-v4-flash, n |
| `\PfourGTwoSTTwoDeepSeekVFourFlashNonTargetAccP` | n/a | non-target accuracy (%), G2s T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsr` | 7.1 | ASR (%), G2s T2, gemma-4-31b-it |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrLo` | 0.0 | ASR (%), G2s T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrHi` | 14.3 | ASR (%), G2s T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrCI` | [0.0, 14.3] | ASR (%), G2s T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrN` | 28 | ASR (%), G2s T2, gemma-4-31b-it, n |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrP` | n/a | ASR (%), G2s T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrDropped` | 7.7 | ASR (%) unparsed dropped, G2s T2, gemma-4-31b-it |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrDroppedLo` | 0.0 | ASR (%) unparsed dropped, G2s T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrDroppedHi` | 16.0 | ASR (%) unparsed dropped, G2s T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrDroppedCI` | [0.0, 16.0] | ASR (%) unparsed dropped, G2s T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrDroppedN` | 26 | ASR (%) unparsed dropped, G2s T2, gemma-4-31b-it, n |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2s T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrCleanOk` | 8.0 | ASR / clean correct (%), G2s T2, gemma-4-31b-it |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrCleanOkLo` | 0.0 | ASR / clean correct (%), G2s T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrCleanOkHi` | 16.7 | ASR / clean correct (%), G2s T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrCleanOkCI` | [0.0, 16.7] | ASR / clean correct (%), G2s T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrCleanOkN` | 25 | ASR / clean correct (%), G2s T2, gemma-4-31b-it, n |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrCleanOkP` | n/a | ASR / clean correct (%), G2s T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGemmaFourThreeOneBNonTargetAcc` | 92.3 | non-target accuracy (%), G2s T2, gemma-4-31b-it |
| `\PfourGTwoSTTwoGemmaFourThreeOneBNonTargetAccLo` | 84.0 | non-target accuracy (%), G2s T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoSTTwoGemmaFourThreeOneBNonTargetAccHi` | 99.1 | non-target accuracy (%), G2s T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoSTTwoGemmaFourThreeOneBNonTargetAccCI` | [84.0, 99.1] | non-target accuracy (%), G2s T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoSTTwoGemmaFourThreeOneBNonTargetAccN` | 104 | non-target accuracy (%), G2s T2, gemma-4-31b-it, n |
| `\PfourGTwoSTTwoGemmaFourThreeOneBNonTargetAccP` | n/a | non-target accuracy (%), G2s T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoPooledAsr` | 74.1 | ASR (%), G2s_insider T2, pooled |
| `\PfourGTwoSInsiderTTwoPooledAsrLo` | 63.8 | ASR (%), G2s_insider T2, pooled, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoPooledAsrHi` | 86.7 | ASR (%), G2s_insider T2, pooled, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoPooledAsrCI` | [63.8, 86.7] | ASR (%), G2s_insider T2, pooled, 95% CI |
| `\PfourGTwoSInsiderTTwoPooledAsrN` | 58 | ASR (%), G2s_insider T2, pooled, n |
| `\PfourGTwoSInsiderTTwoPooledAsrP` | n/a | ASR (%), G2s_insider T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoPooledAsrDropped` | 75.4 | ASR (%) unparsed dropped, G2s_insider T2, pooled |
| `\PfourGTwoSInsiderTTwoPooledAsrDroppedLo` | 65.5 | ASR (%) unparsed dropped, G2s_insider T2, pooled, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoPooledAsrDroppedHi` | 86.4 | ASR (%) unparsed dropped, G2s_insider T2, pooled, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoPooledAsrDroppedCI` | [65.5, 86.4] | ASR (%) unparsed dropped, G2s_insider T2, pooled, 95% CI |
| `\PfourGTwoSInsiderTTwoPooledAsrDroppedN` | 57 | ASR (%) unparsed dropped, G2s_insider T2, pooled, n |
| `\PfourGTwoSInsiderTTwoPooledAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2s_insider T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoPooledAsrCleanOk` | 75.0 | ASR / clean correct (%), G2s_insider T2, pooled |
| `\PfourGTwoSInsiderTTwoPooledAsrCleanOkLo` | 66.1 | ASR / clean correct (%), G2s_insider T2, pooled, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoPooledAsrCleanOkHi` | 86.0 | ASR / clean correct (%), G2s_insider T2, pooled, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoPooledAsrCleanOkCI` | [66.1, 86.0] | ASR / clean correct (%), G2s_insider T2, pooled, 95% CI |
| `\PfourGTwoSInsiderTTwoPooledAsrCleanOkN` | 56 | ASR / clean correct (%), G2s_insider T2, pooled, n |
| `\PfourGTwoSInsiderTTwoPooledAsrCleanOkP` | n/a | ASR / clean correct (%), G2s_insider T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoPooledNonTargetAcc` | 96.9 | non-target accuracy (%), G2s_insider T2, pooled |
| `\PfourGTwoSInsiderTTwoPooledNonTargetAccLo` | 93.6 | non-target accuracy (%), G2s_insider T2, pooled, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoPooledNonTargetAccHi` | 99.2 | non-target accuracy (%), G2s_insider T2, pooled, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoPooledNonTargetAccCI` | [93.6, 99.2] | non-target accuracy (%), G2s_insider T2, pooled, 95% CI |
| `\PfourGTwoSInsiderTTwoPooledNonTargetAccN` | 228 | non-target accuracy (%), G2s_insider T2, pooled, n |
| `\PfourGTwoSInsiderTTwoPooledNonTargetAccP` | n/a | non-target accuracy (%), G2s_insider T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsr` | 66.7 | ASR (%), G2s_insider T2, deepseek-v4-flash |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrLo` | 60.0 | ASR (%), G2s_insider T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrHi` | 80.0 | ASR (%), G2s_insider T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrCI` | [60.0, 80.0] | ASR (%), G2s_insider T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrN` | 30 | ASR (%), G2s_insider T2, deepseek-v4-flash, n |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrP` | n/a | ASR (%), G2s_insider T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrDropped` | 66.7 | ASR (%) unparsed dropped, G2s_insider T2, deepseek-v4-flash |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrDroppedLo` | 60.0 | ASR (%) unparsed dropped, G2s_insider T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrDroppedHi` | 80.0 | ASR (%) unparsed dropped, G2s_insider T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrDroppedCI` | [60.0, 80.0] | ASR (%) unparsed dropped, G2s_insider T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrDroppedN` | 30 | ASR (%) unparsed dropped, G2s_insider T2, deepseek-v4-flash, n |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2s_insider T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrCleanOk` | 66.7 | ASR / clean correct (%), G2s_insider T2, deepseek-v4-flash |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrCleanOkLo` | 60.0 | ASR / clean correct (%), G2s_insider T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrCleanOkHi` | 80.0 | ASR / clean correct (%), G2s_insider T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrCleanOkCI` | [60.0, 80.0] | ASR / clean correct (%), G2s_insider T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrCleanOkN` | 30 | ASR / clean correct (%), G2s_insider T2, deepseek-v4-flash, n |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrCleanOkP` | n/a | ASR / clean correct (%), G2s_insider T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashNonTargetAcc` | 99.2 | non-target accuracy (%), G2s_insider T2, deepseek-v4-flash |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashNonTargetAccLo` | 97.5 | non-target accuracy (%), G2s_insider T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), G2s_insider T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashNonTargetAccCI` | [97.5, 100.0] | non-target accuracy (%), G2s_insider T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashNonTargetAccN` | 120 | non-target accuracy (%), G2s_insider T2, deepseek-v4-flash, n |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashNonTargetAccP` | n/a | non-target accuracy (%), G2s_insider T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsr` | 82.1 | ASR (%), G2s_insider T2, gemma-4-31b-it |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrLo` | 67.9 | ASR (%), G2s_insider T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrHi` | 96.4 | ASR (%), G2s_insider T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrCI` | [67.9, 96.4] | ASR (%), G2s_insider T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrN` | 28 | ASR (%), G2s_insider T2, gemma-4-31b-it, n |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrP` | n/a | ASR (%), G2s_insider T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrDropped` | 85.2 | ASR (%) unparsed dropped, G2s_insider T2, gemma-4-31b-it |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrDroppedLo` | 70.4 | ASR (%) unparsed dropped, G2s_insider T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrDroppedHi` | 96.6 | ASR (%) unparsed dropped, G2s_insider T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrDroppedCI` | [70.4, 96.6] | ASR (%) unparsed dropped, G2s_insider T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrDroppedN` | 27 | ASR (%) unparsed dropped, G2s_insider T2, gemma-4-31b-it, n |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2s_insider T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrCleanOk` | 84.6 | ASR / clean correct (%), G2s_insider T2, gemma-4-31b-it |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrCleanOkLo` | 70.4 | ASR / clean correct (%), G2s_insider T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrCleanOkHi` | 96.3 | ASR / clean correct (%), G2s_insider T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrCleanOkCI` | [70.4, 96.3] | ASR / clean correct (%), G2s_insider T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrCleanOkN` | 26 | ASR / clean correct (%), G2s_insider T2, gemma-4-31b-it, n |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrCleanOkP` | n/a | ASR / clean correct (%), G2s_insider T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBNonTargetAcc` | 94.4 | non-target accuracy (%), G2s_insider T2, gemma-4-31b-it |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBNonTargetAccLo` | 86.5 | non-target accuracy (%), G2s_insider T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBNonTargetAccHi` | 99.1 | non-target accuracy (%), G2s_insider T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBNonTargetAccCI` | [86.5, 99.1] | non-target accuracy (%), G2s_insider T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBNonTargetAccN` | 108 | non-target accuracy (%), G2s_insider T2, gemma-4-31b-it, n |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBNonTargetAccP` | n/a | non-target accuracy (%), G2s_insider T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSPooledAsr` | 1.7 | ASR (%), G1+G2s -, pooled |
| `\PfourGOnePlusGTwoSPooledAsrLo` | 0.0 | ASR (%), G1+G2s -, pooled, lower 95% CI bound |
| `\PfourGOnePlusGTwoSPooledAsrHi` | 5.1 | ASR (%), G1+G2s -, pooled, upper 95% CI bound |
| `\PfourGOnePlusGTwoSPooledAsrCI` | [0.0, 5.1] | ASR (%), G1+G2s -, pooled, 95% CI |
| `\PfourGOnePlusGTwoSPooledAsrN` | 59 | ASR (%), G1+G2s -, pooled, n |
| `\PfourGOnePlusGTwoSPooledAsrP` | n/a | ASR (%), G1+G2s -, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSPooledAsrDropped` | 1.7 | ASR (%) unparsed dropped, G1+G2s -, pooled |
| `\PfourGOnePlusGTwoSPooledAsrDroppedLo` | 0.0 | ASR (%) unparsed dropped, G1+G2s -, pooled, lower 95% CI bound |
| `\PfourGOnePlusGTwoSPooledAsrDroppedHi` | 5.4 | ASR (%) unparsed dropped, G1+G2s -, pooled, upper 95% CI bound |
| `\PfourGOnePlusGTwoSPooledAsrDroppedCI` | [0.0, 5.4] | ASR (%) unparsed dropped, G1+G2s -, pooled, 95% CI |
| `\PfourGOnePlusGTwoSPooledAsrDroppedN` | 58 | ASR (%) unparsed dropped, G1+G2s -, pooled, n |
| `\PfourGOnePlusGTwoSPooledAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1+G2s -, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSPooledAsrCleanOk` | 1.8 | ASR / clean correct (%), G1+G2s -, pooled |
| `\PfourGOnePlusGTwoSPooledAsrCleanOkLo` | 0.0 | ASR / clean correct (%), G1+G2s -, pooled, lower 95% CI bound |
| `\PfourGOnePlusGTwoSPooledAsrCleanOkHi` | 5.5 | ASR / clean correct (%), G1+G2s -, pooled, upper 95% CI bound |
| `\PfourGOnePlusGTwoSPooledAsrCleanOkCI` | [0.0, 5.5] | ASR / clean correct (%), G1+G2s -, pooled, 95% CI |
| `\PfourGOnePlusGTwoSPooledAsrCleanOkN` | 57 | ASR / clean correct (%), G1+G2s -, pooled, n |
| `\PfourGOnePlusGTwoSPooledAsrCleanOkP` | n/a | ASR / clean correct (%), G1+G2s -, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSPooledNonTargetAcc` | 97.0 | non-target accuracy (%), G1+G2s -, pooled |
| `\PfourGOnePlusGTwoSPooledNonTargetAccLo` | 93.3 | non-target accuracy (%), G1+G2s -, pooled, lower 95% CI bound |
| `\PfourGOnePlusGTwoSPooledNonTargetAccHi` | 99.6 | non-target accuracy (%), G1+G2s -, pooled, upper 95% CI bound |
| `\PfourGOnePlusGTwoSPooledNonTargetAccCI` | [93.3, 99.6] | non-target accuracy (%), G1+G2s -, pooled, 95% CI |
| `\PfourGOnePlusGTwoSPooledNonTargetAccN` | 232 | non-target accuracy (%), G1+G2s -, pooled, n |
| `\PfourGOnePlusGTwoSPooledNonTargetAccP` | n/a | non-target accuracy (%), G1+G2s -, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsr` | 0.0 | ASR (%), G1+G2s -, deepseek-v4-flash |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrLo` | 0.0 | ASR (%), G1+G2s -, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrHi` | 11.6 | ASR (%), G1+G2s -, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrCI` | [0.0, 11.6] | ASR (%), G1+G2s -, deepseek-v4-flash, 95% CI |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrN` | 30 | ASR (%), G1+G2s -, deepseek-v4-flash, n |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrP` | n/a | ASR (%), G1+G2s -, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrDropped` | 0.0 | ASR (%) unparsed dropped, G1+G2s -, deepseek-v4-flash |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrDroppedLo` | 0.0 | ASR (%) unparsed dropped, G1+G2s -, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrDroppedHi` | 11.6 | ASR (%) unparsed dropped, G1+G2s -, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrDroppedCI` | [0.0, 11.6] | ASR (%) unparsed dropped, G1+G2s -, deepseek-v4-flash, 95% CI |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrDroppedN` | 30 | ASR (%) unparsed dropped, G1+G2s -, deepseek-v4-flash, n |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1+G2s -, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrCleanOk` | 0.0 | ASR / clean correct (%), G1+G2s -, deepseek-v4-flash |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrCleanOkLo` | 0.0 | ASR / clean correct (%), G1+G2s -, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrCleanOkHi` | 11.6 | ASR / clean correct (%), G1+G2s -, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrCleanOkCI` | [0.0, 11.6] | ASR / clean correct (%), G1+G2s -, deepseek-v4-flash, 95% CI |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrCleanOkN` | 30 | ASR / clean correct (%), G1+G2s -, deepseek-v4-flash, n |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrCleanOkP` | n/a | ASR / clean correct (%), G1+G2s -, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashNonTargetAcc` | 100.0 | non-target accuracy (%), G1+G2s -, deepseek-v4-flash |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashNonTargetAccLo` | 97.0 | non-target accuracy (%), G1+G2s -, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), G1+G2s -, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashNonTargetAccCI` | [97.0, 100.0] | non-target accuracy (%), G1+G2s -, deepseek-v4-flash, 95% CI |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashNonTargetAccN` | 120 | non-target accuracy (%), G1+G2s -, deepseek-v4-flash, n |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashNonTargetAccP` | n/a | non-target accuracy (%), G1+G2s -, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsr` | 3.4 | ASR (%), G1+G2s -, gemma-4-31b-it |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrLo` | 0.0 | ASR (%), G1+G2s -, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrHi` | 10.3 | ASR (%), G1+G2s -, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrCI` | [0.0, 10.3] | ASR (%), G1+G2s -, gemma-4-31b-it, 95% CI |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrN` | 29 | ASR (%), G1+G2s -, gemma-4-31b-it, n |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrP` | n/a | ASR (%), G1+G2s -, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrDropped` | 3.6 | ASR (%) unparsed dropped, G1+G2s -, gemma-4-31b-it |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrDroppedLo` | 0.0 | ASR (%) unparsed dropped, G1+G2s -, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrDroppedHi` | 11.5 | ASR (%) unparsed dropped, G1+G2s -, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrDroppedCI` | [0.0, 11.5] | ASR (%) unparsed dropped, G1+G2s -, gemma-4-31b-it, 95% CI |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrDroppedN` | 28 | ASR (%) unparsed dropped, G1+G2s -, gemma-4-31b-it, n |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1+G2s -, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrCleanOk` | 3.7 | ASR / clean correct (%), G1+G2s -, gemma-4-31b-it |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrCleanOkLo` | 0.0 | ASR / clean correct (%), G1+G2s -, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrCleanOkHi` | 12.0 | ASR / clean correct (%), G1+G2s -, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrCleanOkCI` | [0.0, 12.0] | ASR / clean correct (%), G1+G2s -, gemma-4-31b-it, 95% CI |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrCleanOkN` | 27 | ASR / clean correct (%), G1+G2s -, gemma-4-31b-it, n |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrCleanOkP` | n/a | ASR / clean correct (%), G1+G2s -, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBNonTargetAcc` | 93.8 | non-target accuracy (%), G1+G2s -, gemma-4-31b-it |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBNonTargetAccLo` | 86.0 | non-target accuracy (%), G1+G2s -, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBNonTargetAccHi` | 99.1 | non-target accuracy (%), G1+G2s -, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBNonTargetAccCI` | [86.0, 99.1] | non-target accuracy (%), G1+G2s -, gemma-4-31b-it, 95% CI |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBNonTargetAccN` | 112 | non-target accuracy (%), G1+G2s -, gemma-4-31b-it, n |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBNonTargetAccP` | n/a | non-target accuracy (%), G1+G2s -, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSPooledCleanAcc` | 95.0 | clean-store accuracy (%), G2s, pooled |
| `\PfourGTwoSPooledCleanAccLo` | 91.7 | clean-store accuracy (%), G2s, pooled, lower 95% CI bound |
| `\PfourGTwoSPooledCleanAccHi` | 98.3 | clean-store accuracy (%), G2s, pooled, upper 95% CI bound |
| `\PfourGTwoSPooledCleanAccCI` | [91.7, 98.3] | clean-store accuracy (%), G2s, pooled, 95% CI |
| `\PfourGTwoSPooledCleanAccN` | 60 | clean-store accuracy (%), G2s, pooled, n |
| `\PfourGTwoSPooledCleanAccP` | n/a | clean-store accuracy (%), G2s, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSPooledFpCost` | \ensuremath{-}1.7 | clean accuracy change vs none (pp), G2s, pooled |
| `\PfourGTwoSPooledFpCostLo` | \ensuremath{-}5.0 | clean accuracy change vs none (pp), G2s, pooled, lower 95% CI bound |
| `\PfourGTwoSPooledFpCostHi` | 0.0 | clean accuracy change vs none (pp), G2s, pooled, upper 95% CI bound |
| `\PfourGTwoSPooledFpCostCI` | [\ensuremath{-}5.0, 0.0] | clean accuracy change vs none (pp), G2s, pooled, 95% CI |
| `\PfourGTwoSPooledFpCostN` | 60 | clean accuracy change vs none (pp), G2s, pooled, n |
| `\PfourGTwoSPooledFpCostP` | 0.667 | clean accuracy change vs none (pp), G2s, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSDeepSeekVFourFlashCleanAcc` | 100.0 | clean-store accuracy (%), G2s, deepseek-v4-flash |
| `\PfourGTwoSDeepSeekVFourFlashCleanAccLo` | 88.4 | clean-store accuracy (%), G2s, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoSDeepSeekVFourFlashCleanAccHi` | 100.0 | clean-store accuracy (%), G2s, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoSDeepSeekVFourFlashCleanAccCI` | [88.4, 100.0] | clean-store accuracy (%), G2s, deepseek-v4-flash, 95% CI |
| `\PfourGTwoSDeepSeekVFourFlashCleanAccN` | 30 | clean-store accuracy (%), G2s, deepseek-v4-flash, n |
| `\PfourGTwoSDeepSeekVFourFlashCleanAccP` | n/a | clean-store accuracy (%), G2s, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSDeepSeekVFourFlashFpCost` | 0.0 | clean accuracy change vs none (pp), G2s, deepseek-v4-flash |
| `\PfourGTwoSDeepSeekVFourFlashFpCostLo` | 0.0 | clean accuracy change vs none (pp), G2s, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoSDeepSeekVFourFlashFpCostHi` | 0.0 | clean accuracy change vs none (pp), G2s, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoSDeepSeekVFourFlashFpCostCI` | [0.0, 0.0] | clean accuracy change vs none (pp), G2s, deepseek-v4-flash, 95% CI |
| `\PfourGTwoSDeepSeekVFourFlashFpCostN` | 30 | clean accuracy change vs none (pp), G2s, deepseek-v4-flash, n |
| `\PfourGTwoSDeepSeekVFourFlashFpCostP` | 1.000 | clean accuracy change vs none (pp), G2s, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSGemmaFourThreeOneBCleanAcc` | 90.0 | clean-store accuracy (%), G2s, gemma-4-31b-it |
| `\PfourGTwoSGemmaFourThreeOneBCleanAccLo` | 83.3 | clean-store accuracy (%), G2s, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoSGemmaFourThreeOneBCleanAccHi` | 96.7 | clean-store accuracy (%), G2s, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoSGemmaFourThreeOneBCleanAccCI` | [83.3, 96.7] | clean-store accuracy (%), G2s, gemma-4-31b-it, 95% CI |
| `\PfourGTwoSGemmaFourThreeOneBCleanAccN` | 30 | clean-store accuracy (%), G2s, gemma-4-31b-it, n |
| `\PfourGTwoSGemmaFourThreeOneBCleanAccP` | n/a | clean-store accuracy (%), G2s, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSGemmaFourThreeOneBFpCost` | \ensuremath{-}3.3 | clean accuracy change vs none (pp), G2s, gemma-4-31b-it |
| `\PfourGTwoSGemmaFourThreeOneBFpCostLo` | \ensuremath{-}10.0 | clean accuracy change vs none (pp), G2s, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoSGemmaFourThreeOneBFpCostHi` | 0.0 | clean accuracy change vs none (pp), G2s, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoSGemmaFourThreeOneBFpCostCI` | [\ensuremath{-}10.0, 0.0] | clean accuracy change vs none (pp), G2s, gemma-4-31b-it, 95% CI |
| `\PfourGTwoSGemmaFourThreeOneBFpCostN` | 30 | clean accuracy change vs none (pp), G2s, gemma-4-31b-it, n |
| `\PfourGTwoSGemmaFourThreeOneBFpCostP` | 0.698 | clean accuracy change vs none (pp), G2s, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUPooledCleanAcc` | 95.0 | clean-store accuracy (%), G2u, pooled |
| `\PfourGTwoUPooledCleanAccLo` | 91.7 | clean-store accuracy (%), G2u, pooled, lower 95% CI bound |
| `\PfourGTwoUPooledCleanAccHi` | 98.3 | clean-store accuracy (%), G2u, pooled, upper 95% CI bound |
| `\PfourGTwoUPooledCleanAccCI` | [91.7, 98.3] | clean-store accuracy (%), G2u, pooled, 95% CI |
| `\PfourGTwoUPooledCleanAccN` | 60 | clean-store accuracy (%), G2u, pooled, n |
| `\PfourGTwoUPooledCleanAccP` | n/a | clean-store accuracy (%), G2u, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUPooledFpCost` | \ensuremath{-}1.7 | clean accuracy change vs none (pp), G2u, pooled |
| `\PfourGTwoUPooledFpCostLo` | \ensuremath{-}5.0 | clean accuracy change vs none (pp), G2u, pooled, lower 95% CI bound |
| `\PfourGTwoUPooledFpCostHi` | 0.0 | clean accuracy change vs none (pp), G2u, pooled, upper 95% CI bound |
| `\PfourGTwoUPooledFpCostCI` | [\ensuremath{-}5.0, 0.0] | clean accuracy change vs none (pp), G2u, pooled, 95% CI |
| `\PfourGTwoUPooledFpCostN` | 60 | clean accuracy change vs none (pp), G2u, pooled, n |
| `\PfourGTwoUPooledFpCostP` | 0.684 | clean accuracy change vs none (pp), G2u, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUDeepSeekVFourFlashCleanAcc` | 100.0 | clean-store accuracy (%), G2u, deepseek-v4-flash |
| `\PfourGTwoUDeepSeekVFourFlashCleanAccLo` | 88.4 | clean-store accuracy (%), G2u, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoUDeepSeekVFourFlashCleanAccHi` | 100.0 | clean-store accuracy (%), G2u, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoUDeepSeekVFourFlashCleanAccCI` | [88.4, 100.0] | clean-store accuracy (%), G2u, deepseek-v4-flash, 95% CI |
| `\PfourGTwoUDeepSeekVFourFlashCleanAccN` | 30 | clean-store accuracy (%), G2u, deepseek-v4-flash, n |
| `\PfourGTwoUDeepSeekVFourFlashCleanAccP` | n/a | clean-store accuracy (%), G2u, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUDeepSeekVFourFlashFpCost` | 0.0 | clean accuracy change vs none (pp), G2u, deepseek-v4-flash |
| `\PfourGTwoUDeepSeekVFourFlashFpCostLo` | 0.0 | clean accuracy change vs none (pp), G2u, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoUDeepSeekVFourFlashFpCostHi` | 0.0 | clean accuracy change vs none (pp), G2u, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoUDeepSeekVFourFlashFpCostCI` | [0.0, 0.0] | clean accuracy change vs none (pp), G2u, deepseek-v4-flash, 95% CI |
| `\PfourGTwoUDeepSeekVFourFlashFpCostN` | 30 | clean accuracy change vs none (pp), G2u, deepseek-v4-flash, n |
| `\PfourGTwoUDeepSeekVFourFlashFpCostP` | 1.000 | clean accuracy change vs none (pp), G2u, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUGemmaFourThreeOneBCleanAcc` | 90.0 | clean-store accuracy (%), G2u, gemma-4-31b-it |
| `\PfourGTwoUGemmaFourThreeOneBCleanAccLo` | 83.3 | clean-store accuracy (%), G2u, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoUGemmaFourThreeOneBCleanAccHi` | 96.7 | clean-store accuracy (%), G2u, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoUGemmaFourThreeOneBCleanAccCI` | [83.3, 96.7] | clean-store accuracy (%), G2u, gemma-4-31b-it, 95% CI |
| `\PfourGTwoUGemmaFourThreeOneBCleanAccN` | 30 | clean-store accuracy (%), G2u, gemma-4-31b-it, n |
| `\PfourGTwoUGemmaFourThreeOneBCleanAccP` | n/a | clean-store accuracy (%), G2u, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUGemmaFourThreeOneBFpCost` | \ensuremath{-}3.3 | clean accuracy change vs none (pp), G2u, gemma-4-31b-it |
| `\PfourGTwoUGemmaFourThreeOneBFpCostLo` | \ensuremath{-}10.0 | clean accuracy change vs none (pp), G2u, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoUGemmaFourThreeOneBFpCostHi` | 0.0 | clean accuracy change vs none (pp), G2u, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoUGemmaFourThreeOneBFpCostCI` | [\ensuremath{-}10.0, 0.0] | clean accuracy change vs none (pp), G2u, gemma-4-31b-it, 95% CI |
| `\PfourGTwoUGemmaFourThreeOneBFpCostN` | 30 | clean accuracy change vs none (pp), G2u, gemma-4-31b-it, n |
| `\PfourGTwoUGemmaFourThreeOneBFpCostP` | 0.692 | clean accuracy change vs none (pp), G2u, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNonePooledCleanAcc` | 96.7 | clean-store accuracy (%), none, pooled |
| `\PfourNonePooledCleanAccLo` | 93.3 | clean-store accuracy (%), none, pooled, lower 95% CI bound |
| `\PfourNonePooledCleanAccHi` | 100.0 | clean-store accuracy (%), none, pooled, upper 95% CI bound |
| `\PfourNonePooledCleanAccCI` | [93.3, 100.0] | clean-store accuracy (%), none, pooled, 95% CI |
| `\PfourNonePooledCleanAccN` | 60 | clean-store accuracy (%), none, pooled, n |
| `\PfourNonePooledCleanAccP` | n/a | clean-store accuracy (%), none, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneDeepSeekVFourFlashCleanAcc` | 100.0 | clean-store accuracy (%), none, deepseek-v4-flash |
| `\PfourNoneDeepSeekVFourFlashCleanAccLo` | 88.4 | clean-store accuracy (%), none, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneDeepSeekVFourFlashCleanAccHi` | 100.0 | clean-store accuracy (%), none, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneDeepSeekVFourFlashCleanAccCI` | [88.4, 100.0] | clean-store accuracy (%), none, deepseek-v4-flash, 95% CI |
| `\PfourNoneDeepSeekVFourFlashCleanAccN` | 30 | clean-store accuracy (%), none, deepseek-v4-flash, n |
| `\PfourNoneDeepSeekVFourFlashCleanAccP` | n/a | clean-store accuracy (%), none, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneGemmaFourThreeOneBCleanAcc` | 93.3 | clean-store accuracy (%), none, gemma-4-31b-it |
| `\PfourNoneGemmaFourThreeOneBCleanAccLo` | 86.7 | clean-store accuracy (%), none, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneGemmaFourThreeOneBCleanAccHi` | 100.0 | clean-store accuracy (%), none, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneGemmaFourThreeOneBCleanAccCI` | [86.7, 100.0] | clean-store accuracy (%), none, gemma-4-31b-it, 95% CI |
| `\PfourNoneGemmaFourThreeOneBCleanAccN` | 30 | clean-store accuracy (%), none, gemma-4-31b-it, n |
| `\PfourNoneGemmaFourThreeOneBCleanAccP` | n/a | clean-store accuracy (%), none, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoURelRed` | \ensuremath{-}2.3 | relative ASR reduction (%) of G2u vs none T2 |
| `\PfourGTwoURelRedLo` | \ensuremath{-}7.7 | relative ASR reduction (%) of G2u vs none T2, lower 95% CI bound |
| `\PfourGTwoURelRedHi` | 0.0 | relative ASR reduction (%) of G2u vs none T2, upper 95% CI bound |
| `\PfourGTwoURelRedCI` | [\ensuremath{-}7.7, 0.0] | relative ASR reduction (%) of G2u vs none T2, 95% CI |
| `\PfourGTwoURelRedN` | 116 | relative ASR reduction (%) of G2u vs none T2, n |
| `\PfourGTwoURelRedP` | 0.641 | relative ASR reduction (%) of G2u vs none T2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUAbsDiff` | 1.7 | ASR difference (pp) G2u - none T2 |
| `\PfourGTwoUAbsDiffLo` | 0.0 | ASR difference (pp) G2u - none T2, lower 95% CI bound |
| `\PfourGTwoUAbsDiffHi` | 5.2 | ASR difference (pp) G2u - none T2, upper 95% CI bound |
| `\PfourGTwoUAbsDiffCI` | [0.0, 5.2] | ASR difference (pp) G2u - none T2, 95% CI |
| `\PfourGTwoUAbsDiffN` | 116 | ASR difference (pp) G2u - none T2, n |
| `\PfourGTwoUAbsDiffP` | 0.672 | ASR difference (pp) G2u - none T2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSRelRed` | 60.5 | relative ASR reduction (%) of G2s vs none T2 |
| `\PfourGTwoSRelRedLo` | 50.0 | relative ASR reduction (%) of G2s vs none T2, lower 95% CI bound |
| `\PfourGTwoSRelRedHi` | 67.5 | relative ASR reduction (%) of G2s vs none T2, upper 95% CI bound |
| `\PfourGTwoSRelRedCI` | [50.0, 67.5] | relative ASR reduction (%) of G2s vs none T2, 95% CI |
| `\PfourGTwoSRelRedN` | 116 | relative ASR reduction (%) of G2s vs none T2, n |
| `\PfourGTwoSRelRedP` | \ensuremath{<}0.001 | relative ASR reduction (%) of G2s vs none T2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSAbsDiff` | \ensuremath{-}44.8 | ASR difference (pp) G2s - none T2 |
| `\PfourGTwoSAbsDiffLo` | \ensuremath{-}54.4 | ASR difference (pp) G2s - none T2, lower 95% CI bound |
| `\PfourGTwoSAbsDiffHi` | \ensuremath{-}32.8 | ASR difference (pp) G2s - none T2, upper 95% CI bound |
| `\PfourGTwoSAbsDiffCI` | [\ensuremath{-}54.4, \ensuremath{-}32.8] | ASR difference (pp) G2s - none T2, 95% CI |
| `\PfourGTwoSAbsDiffN` | 116 | ASR difference (pp) G2s - none T2, n |
| `\PfourGTwoSAbsDiffP` | \ensuremath{<}0.001 | ASR difference (pp) G2s - none T2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderRelRed` | 0.0 | relative ASR reduction (%) of G2s_insider vs none T2 |
| `\PfourGTwoSInsiderRelRedLo` | 0.0 | relative ASR reduction (%) of G2s_insider vs none T2, lower 95% CI bound |
| `\PfourGTwoSInsiderRelRedHi` | 0.0 | relative ASR reduction (%) of G2s_insider vs none T2, upper 95% CI bound |
| `\PfourGTwoSInsiderRelRedCI` | [0.0, 0.0] | relative ASR reduction (%) of G2s_insider vs none T2, 95% CI |
| `\PfourGTwoSInsiderRelRedN` | 116 | relative ASR reduction (%) of G2s_insider vs none T2, n |
| `\PfourGTwoSInsiderRelRedP` | 1.000 | relative ASR reduction (%) of G2s_insider vs none T2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderAbsDiff` | 0.0 | ASR difference (pp) G2s_insider - none T2 |
| `\PfourGTwoSInsiderAbsDiffLo` | 0.0 | ASR difference (pp) G2s_insider - none T2, lower 95% CI bound |
| `\PfourGTwoSInsiderAbsDiffHi` | 0.0 | ASR difference (pp) G2s_insider - none T2, upper 95% CI bound |
| `\PfourGTwoSInsiderAbsDiffCI` | [0.0, 0.0] | ASR difference (pp) G2s_insider - none T2, 95% CI |
| `\PfourGTwoSInsiderAbsDiffN` | 116 | ASR difference (pp) G2s_insider - none T2, n |
| `\PfourGTwoSInsiderAbsDiffP` | 1.000 | ASR difference (pp) G2s_insider - none T2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSRelRed` | 97.7 | relative ASR reduction (%) of G1+G2s vs none T2 |
| `\PfourGOnePlusGTwoSRelRedLo` | 93.1 | relative ASR reduction (%) of G1+G2s vs none T2, lower 95% CI bound |
| `\PfourGOnePlusGTwoSRelRedHi` | 100.0 | relative ASR reduction (%) of G1+G2s vs none T2, upper 95% CI bound |
| `\PfourGOnePlusGTwoSRelRedCI` | [93.1, 100.0] | relative ASR reduction (%) of G1+G2s vs none T2, 95% CI |
| `\PfourGOnePlusGTwoSRelRedN` | 117 | relative ASR reduction (%) of G1+G2s vs none T2, n |
| `\PfourGOnePlusGTwoSRelRedP` | \ensuremath{<}0.001 | relative ASR reduction (%) of G1+G2s vs none T2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSAbsDiff` | \ensuremath{-}72.4 | ASR difference (pp) G1+G2s - none T2 |
| `\PfourGOnePlusGTwoSAbsDiffLo` | \ensuremath{-}84.8 | ASR difference (pp) G1+G2s - none T2, lower 95% CI bound |
| `\PfourGOnePlusGTwoSAbsDiffHi` | \ensuremath{-}62.1 | ASR difference (pp) G1+G2s - none T2, upper 95% CI bound |
| `\PfourGOnePlusGTwoSAbsDiffCI` | [\ensuremath{-}84.8, \ensuremath{-}62.1] | ASR difference (pp) G1+G2s - none T2, 95% CI |
| `\PfourGOnePlusGTwoSAbsDiffN` | 117 | ASR difference (pp) G1+G2s - none T2, n |
| `\PfourGOnePlusGTwoSAbsDiffP` | \ensuremath{<}0.001 | ASR difference (pp) G1+G2s - none T2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeRelRed` | n/a | relative ASR reduction (%) of G1 vs none at T3 [n/a: condition G1 at T3 absent] |
| `\PfourGOneTThreeRelRedLo` | n/a | relative ASR reduction (%) of G1 vs none at T3, lower 95% CI bound |
| `\PfourGOneTThreeRelRedHi` | n/a | relative ASR reduction (%) of G1 vs none at T3, upper 95% CI bound |
| `\PfourGOneTThreeRelRedCI` | n/a | relative ASR reduction (%) of G1 vs none at T3, 95% CI |
| `\PfourGOneTThreeRelRedN` | n/a | relative ASR reduction (%) of G1 vs none at T3, n |
| `\PfourGOneTThreeRelRedP` | n/a | relative ASR reduction (%) of G1 vs none at T3, two-sided bootstrap p (n/a if not tested) |
| `\PfourPrimarySensitivity` | n/a | primary 4 with unparsed answers dropped (%) |
| `\PfourPrimarySensitivityLo` | n/a | primary 4 with unparsed answers dropped (%), lower 95% CI bound |
| `\PfourPrimarySensitivityHi` | n/a | primary 4 with unparsed answers dropped (%), upper 95% CI bound |
| `\PfourPrimarySensitivityCI` | n/a | primary 4 with unparsed answers dropped (%), 95% CI |
| `\PfourPrimarySensitivityN` | n/a | primary 4 with unparsed answers dropped (%), n |
| `\PfourPrimarySensitivityP` | n/a | primary 4 with unparsed answers dropped (%), two-sided bootstrap p (n/a if not tested) |
| `\GateDeepSeekVFourFlashDetector` | n/a | gate detector, deepseek-v4-flash |
| `\GateDeepSeekVFourFlashFprCalib` | n/a | gate FPR on calibration genuine entries (%), deepseek-v4-flash |
| `\GateDeepSeekVFourFlashCallsPerRead` | n/a | extra model calls per memory read for G1, deepseek-v4-flash |
| `\GateGemmaFourThreeOneBDetector` | n/a | gate detector, gemma-4-31b-it |
| `\GateGemmaFourThreeOneBFprCalib` | n/a | gate FPR on calibration genuine entries (%), gemma-4-31b-it |
| `\GateGemmaFourThreeOneBCallsPerRead` | n/a | extra model calls per memory read for G1, gemma-4-31b-it |
| `\CostPilotHostedDetect` | 0.31 | spend (credits), pilot hosted_detect |
| `\CostPilotHostedGen` | 0.40 | spend (credits), pilot hosted_gen |
| `\CostPilotPOnePairs` | 0.08 | spend (credits), pilot p1_pairs |
| `\CostPilotPOneSelfTrust` | 0.19 | spend (credits), pilot p1_self_trust |
| `\CostPilotPFourGate` | 0.41 | spend (credits), pilot p4_gate |
| `\CostTotal` | 8.63 | total spend in the ledger (credits) |
| `\CostCallsTotal` | 21{,}900 | total model calls in the ledger |
| `\PoneNetMemToolQwenThreeEightTwoSevenB` | n/a | P1 PoneNetMemTool QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PoneNetMemToolQwenThreeEightTwoSevenBLo` | n/a | P1 PoneNetMemTool QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PoneNetMemToolQwenThreeEightTwoSevenBHi` | n/a | P1 PoneNetMemTool QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PoneNetMemToolQwenThreeEightTwoSevenBCI` | n/a | P1 PoneNetMemTool QwenThreeEightTwoSevenB, 95% CI |
| `\PoneNetMemToolQwenThreeEightTwoSevenBN` | n/a | P1 PoneNetMemTool QwenThreeEightTwoSevenB, n |
| `\PoneNetMemToolQwenThreeEightTwoSevenBP` | n/a | P1 PoneNetMemTool QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolDroppedQwenThreeEightTwoSevenB` | n/a | P1 PoneNetMemToolDropped QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PoneNetMemToolDroppedQwenThreeEightTwoSevenBLo` | n/a | P1 PoneNetMemToolDropped QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PoneNetMemToolDroppedQwenThreeEightTwoSevenBHi` | n/a | P1 PoneNetMemToolDropped QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PoneNetMemToolDroppedQwenThreeEightTwoSevenBCI` | n/a | P1 PoneNetMemToolDropped QwenThreeEightTwoSevenB, 95% CI |
| `\PoneNetMemToolDroppedQwenThreeEightTwoSevenBN` | n/a | P1 PoneNetMemToolDropped QwenThreeEightTwoSevenB, n |
| `\PoneNetMemToolDroppedQwenThreeEightTwoSevenBP` | n/a | P1 PoneNetMemToolDropped QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareMemVsToolQwenThreeEightTwoSevenB` | n/a | P1 PoneShareMemVsTool QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PoneShareMemVsToolQwenThreeEightTwoSevenBLo` | n/a | P1 PoneShareMemVsTool QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PoneShareMemVsToolQwenThreeEightTwoSevenBHi` | n/a | P1 PoneShareMemVsTool QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PoneShareMemVsToolQwenThreeEightTwoSevenBCI` | n/a | P1 PoneShareMemVsTool QwenThreeEightTwoSevenB, 95% CI |
| `\PoneShareMemVsToolQwenThreeEightTwoSevenBN` | n/a | P1 PoneShareMemVsTool QwenThreeEightTwoSevenB, n |
| `\PoneShareMemVsToolQwenThreeEightTwoSevenBP` | n/a | P1 PoneShareMemVsTool QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareToolVsMemQwenThreeEightTwoSevenB` | n/a | P1 PoneShareToolVsMem QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PoneShareToolVsMemQwenThreeEightTwoSevenBLo` | n/a | P1 PoneShareToolVsMem QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PoneShareToolVsMemQwenThreeEightTwoSevenBHi` | n/a | P1 PoneShareToolVsMem QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PoneShareToolVsMemQwenThreeEightTwoSevenBCI` | n/a | P1 PoneShareToolVsMem QwenThreeEightTwoSevenB, 95% CI |
| `\PoneShareToolVsMemQwenThreeEightTwoSevenBN` | n/a | P1 PoneShareToolVsMem QwenThreeEightTwoSevenB, n |
| `\PoneShareToolVsMemQwenThreeEightTwoSevenBP` | n/a | P1 PoneShareToolVsMem QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolGLMFiveThreeFlash` | n/a | P1 PoneNetMemTool GLMFiveThreeFlash [n/a: no data yet] |
| `\PoneNetMemToolGLMFiveThreeFlashLo` | n/a | P1 PoneNetMemTool GLMFiveThreeFlash, lower 95% CI bound |
| `\PoneNetMemToolGLMFiveThreeFlashHi` | n/a | P1 PoneNetMemTool GLMFiveThreeFlash, upper 95% CI bound |
| `\PoneNetMemToolGLMFiveThreeFlashCI` | n/a | P1 PoneNetMemTool GLMFiveThreeFlash, 95% CI |
| `\PoneNetMemToolGLMFiveThreeFlashN` | n/a | P1 PoneNetMemTool GLMFiveThreeFlash, n |
| `\PoneNetMemToolGLMFiveThreeFlashP` | n/a | P1 PoneNetMemTool GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolDroppedGLMFiveThreeFlash` | n/a | P1 PoneNetMemToolDropped GLMFiveThreeFlash [n/a: no data yet] |
| `\PoneNetMemToolDroppedGLMFiveThreeFlashLo` | n/a | P1 PoneNetMemToolDropped GLMFiveThreeFlash, lower 95% CI bound |
| `\PoneNetMemToolDroppedGLMFiveThreeFlashHi` | n/a | P1 PoneNetMemToolDropped GLMFiveThreeFlash, upper 95% CI bound |
| `\PoneNetMemToolDroppedGLMFiveThreeFlashCI` | n/a | P1 PoneNetMemToolDropped GLMFiveThreeFlash, 95% CI |
| `\PoneNetMemToolDroppedGLMFiveThreeFlashN` | n/a | P1 PoneNetMemToolDropped GLMFiveThreeFlash, n |
| `\PoneNetMemToolDroppedGLMFiveThreeFlashP` | n/a | P1 PoneNetMemToolDropped GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareMemVsToolGLMFiveThreeFlash` | n/a | P1 PoneShareMemVsTool GLMFiveThreeFlash [n/a: no data yet] |
| `\PoneShareMemVsToolGLMFiveThreeFlashLo` | n/a | P1 PoneShareMemVsTool GLMFiveThreeFlash, lower 95% CI bound |
| `\PoneShareMemVsToolGLMFiveThreeFlashHi` | n/a | P1 PoneShareMemVsTool GLMFiveThreeFlash, upper 95% CI bound |
| `\PoneShareMemVsToolGLMFiveThreeFlashCI` | n/a | P1 PoneShareMemVsTool GLMFiveThreeFlash, 95% CI |
| `\PoneShareMemVsToolGLMFiveThreeFlashN` | n/a | P1 PoneShareMemVsTool GLMFiveThreeFlash, n |
| `\PoneShareMemVsToolGLMFiveThreeFlashP` | n/a | P1 PoneShareMemVsTool GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareToolVsMemGLMFiveThreeFlash` | n/a | P1 PoneShareToolVsMem GLMFiveThreeFlash [n/a: no data yet] |
| `\PoneShareToolVsMemGLMFiveThreeFlashLo` | n/a | P1 PoneShareToolVsMem GLMFiveThreeFlash, lower 95% CI bound |
| `\PoneShareToolVsMemGLMFiveThreeFlashHi` | n/a | P1 PoneShareToolVsMem GLMFiveThreeFlash, upper 95% CI bound |
| `\PoneShareToolVsMemGLMFiveThreeFlashCI` | n/a | P1 PoneShareToolVsMem GLMFiveThreeFlash, 95% CI |
| `\PoneShareToolVsMemGLMFiveThreeFlashN` | n/a | P1 PoneShareToolVsMem GLMFiveThreeFlash, n |
| `\PoneShareToolVsMemGLMFiveThreeFlashP` | n/a | P1 PoneShareToolVsMem GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolGLMFiveTwo` | n/a | P1 PoneNetMemTool GLMFiveTwo [n/a: no data yet] |
| `\PoneNetMemToolGLMFiveTwoLo` | n/a | P1 PoneNetMemTool GLMFiveTwo, lower 95% CI bound |
| `\PoneNetMemToolGLMFiveTwoHi` | n/a | P1 PoneNetMemTool GLMFiveTwo, upper 95% CI bound |
| `\PoneNetMemToolGLMFiveTwoCI` | n/a | P1 PoneNetMemTool GLMFiveTwo, 95% CI |
| `\PoneNetMemToolGLMFiveTwoN` | n/a | P1 PoneNetMemTool GLMFiveTwo, n |
| `\PoneNetMemToolGLMFiveTwoP` | n/a | P1 PoneNetMemTool GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolDroppedGLMFiveTwo` | n/a | P1 PoneNetMemToolDropped GLMFiveTwo [n/a: no data yet] |
| `\PoneNetMemToolDroppedGLMFiveTwoLo` | n/a | P1 PoneNetMemToolDropped GLMFiveTwo, lower 95% CI bound |
| `\PoneNetMemToolDroppedGLMFiveTwoHi` | n/a | P1 PoneNetMemToolDropped GLMFiveTwo, upper 95% CI bound |
| `\PoneNetMemToolDroppedGLMFiveTwoCI` | n/a | P1 PoneNetMemToolDropped GLMFiveTwo, 95% CI |
| `\PoneNetMemToolDroppedGLMFiveTwoN` | n/a | P1 PoneNetMemToolDropped GLMFiveTwo, n |
| `\PoneNetMemToolDroppedGLMFiveTwoP` | n/a | P1 PoneNetMemToolDropped GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareMemVsToolGLMFiveTwo` | n/a | P1 PoneShareMemVsTool GLMFiveTwo [n/a: no data yet] |
| `\PoneShareMemVsToolGLMFiveTwoLo` | n/a | P1 PoneShareMemVsTool GLMFiveTwo, lower 95% CI bound |
| `\PoneShareMemVsToolGLMFiveTwoHi` | n/a | P1 PoneShareMemVsTool GLMFiveTwo, upper 95% CI bound |
| `\PoneShareMemVsToolGLMFiveTwoCI` | n/a | P1 PoneShareMemVsTool GLMFiveTwo, 95% CI |
| `\PoneShareMemVsToolGLMFiveTwoN` | n/a | P1 PoneShareMemVsTool GLMFiveTwo, n |
| `\PoneShareMemVsToolGLMFiveTwoP` | n/a | P1 PoneShareMemVsTool GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareToolVsMemGLMFiveTwo` | n/a | P1 PoneShareToolVsMem GLMFiveTwo [n/a: no data yet] |
| `\PoneShareToolVsMemGLMFiveTwoLo` | n/a | P1 PoneShareToolVsMem GLMFiveTwo, lower 95% CI bound |
| `\PoneShareToolVsMemGLMFiveTwoHi` | n/a | P1 PoneShareToolVsMem GLMFiveTwo, upper 95% CI bound |
| `\PoneShareToolVsMemGLMFiveTwoCI` | n/a | P1 PoneShareToolVsMem GLMFiveTwo, 95% CI |
| `\PoneShareToolVsMemGLMFiveTwoN` | n/a | P1 PoneShareToolVsMem GLMFiveTwo, n |
| `\PoneShareToolVsMemGLMFiveTwoP` | n/a | P1 PoneShareToolVsMem GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolQwenThreeFiveThreeNineSevenB` | n/a | P1 PoneNetMemTool QwenThreeFiveThreeNineSevenB [n/a: no data yet] |
| `\PoneNetMemToolQwenThreeFiveThreeNineSevenBLo` | n/a | P1 PoneNetMemTool QwenThreeFiveThreeNineSevenB, lower 95% CI bound |
| `\PoneNetMemToolQwenThreeFiveThreeNineSevenBHi` | n/a | P1 PoneNetMemTool QwenThreeFiveThreeNineSevenB, upper 95% CI bound |
| `\PoneNetMemToolQwenThreeFiveThreeNineSevenBCI` | n/a | P1 PoneNetMemTool QwenThreeFiveThreeNineSevenB, 95% CI |
| `\PoneNetMemToolQwenThreeFiveThreeNineSevenBN` | n/a | P1 PoneNetMemTool QwenThreeFiveThreeNineSevenB, n |
| `\PoneNetMemToolQwenThreeFiveThreeNineSevenBP` | n/a | P1 PoneNetMemTool QwenThreeFiveThreeNineSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolDroppedQwenThreeFiveThreeNineSevenB` | n/a | P1 PoneNetMemToolDropped QwenThreeFiveThreeNineSevenB [n/a: no data yet] |
| `\PoneNetMemToolDroppedQwenThreeFiveThreeNineSevenBLo` | n/a | P1 PoneNetMemToolDropped QwenThreeFiveThreeNineSevenB, lower 95% CI bound |
| `\PoneNetMemToolDroppedQwenThreeFiveThreeNineSevenBHi` | n/a | P1 PoneNetMemToolDropped QwenThreeFiveThreeNineSevenB, upper 95% CI bound |
| `\PoneNetMemToolDroppedQwenThreeFiveThreeNineSevenBCI` | n/a | P1 PoneNetMemToolDropped QwenThreeFiveThreeNineSevenB, 95% CI |
| `\PoneNetMemToolDroppedQwenThreeFiveThreeNineSevenBN` | n/a | P1 PoneNetMemToolDropped QwenThreeFiveThreeNineSevenB, n |
| `\PoneNetMemToolDroppedQwenThreeFiveThreeNineSevenBP` | n/a | P1 PoneNetMemToolDropped QwenThreeFiveThreeNineSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareMemVsToolQwenThreeFiveThreeNineSevenB` | n/a | P1 PoneShareMemVsTool QwenThreeFiveThreeNineSevenB [n/a: no data yet] |
| `\PoneShareMemVsToolQwenThreeFiveThreeNineSevenBLo` | n/a | P1 PoneShareMemVsTool QwenThreeFiveThreeNineSevenB, lower 95% CI bound |
| `\PoneShareMemVsToolQwenThreeFiveThreeNineSevenBHi` | n/a | P1 PoneShareMemVsTool QwenThreeFiveThreeNineSevenB, upper 95% CI bound |
| `\PoneShareMemVsToolQwenThreeFiveThreeNineSevenBCI` | n/a | P1 PoneShareMemVsTool QwenThreeFiveThreeNineSevenB, 95% CI |
| `\PoneShareMemVsToolQwenThreeFiveThreeNineSevenBN` | n/a | P1 PoneShareMemVsTool QwenThreeFiveThreeNineSevenB, n |
| `\PoneShareMemVsToolQwenThreeFiveThreeNineSevenBP` | n/a | P1 PoneShareMemVsTool QwenThreeFiveThreeNineSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareToolVsMemQwenThreeFiveThreeNineSevenB` | n/a | P1 PoneShareToolVsMem QwenThreeFiveThreeNineSevenB [n/a: no data yet] |
| `\PoneShareToolVsMemQwenThreeFiveThreeNineSevenBLo` | n/a | P1 PoneShareToolVsMem QwenThreeFiveThreeNineSevenB, lower 95% CI bound |
| `\PoneShareToolVsMemQwenThreeFiveThreeNineSevenBHi` | n/a | P1 PoneShareToolVsMem QwenThreeFiveThreeNineSevenB, upper 95% CI bound |
| `\PoneShareToolVsMemQwenThreeFiveThreeNineSevenBCI` | n/a | P1 PoneShareToolVsMem QwenThreeFiveThreeNineSevenB, 95% CI |
| `\PoneShareToolVsMemQwenThreeFiveThreeNineSevenBN` | n/a | P1 PoneShareToolVsMem QwenThreeFiveThreeNineSevenB, n |
| `\PoneShareToolVsMemQwenThreeFiveThreeNineSevenBP` | n/a | P1 PoneShareToolVsMem QwenThreeFiveThreeNineSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolVariantOne` | n/a | P1 net memory - tool, phrasing 1 [n/a: no data yet] |
| `\PoneNetMemToolVariantOneLo` | n/a | P1 net memory - tool, phrasing 1, lower 95% CI bound |
| `\PoneNetMemToolVariantOneHi` | n/a | P1 net memory - tool, phrasing 1, upper 95% CI bound |
| `\PoneNetMemToolVariantOneCI` | n/a | P1 net memory - tool, phrasing 1, 95% CI |
| `\PoneNetMemToolVariantOneN` | n/a | P1 net memory - tool, phrasing 1, n |
| `\PoneNetMemToolVariantOneP` | n/a | P1 net memory - tool, phrasing 1, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsUnattributedFollowA` | n/a | P1 pair tool vs unattributed FollowA [n/a: no data yet] |
| `\PonePairToolVsUnattributedFollowALo` | n/a | P1 pair tool vs unattributed FollowA, lower 95% CI bound |
| `\PonePairToolVsUnattributedFollowAHi` | n/a | P1 pair tool vs unattributed FollowA, upper 95% CI bound |
| `\PonePairToolVsUnattributedFollowACI` | n/a | P1 pair tool vs unattributed FollowA, 95% CI |
| `\PonePairToolVsUnattributedFollowAN` | n/a | P1 pair tool vs unattributed FollowA, n |
| `\PonePairToolVsUnattributedFollowAP` | n/a | P1 pair tool vs unattributed FollowA, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsUnattributedFollowB` | n/a | P1 pair tool vs unattributed FollowB [n/a: no data yet] |
| `\PonePairToolVsUnattributedFollowBLo` | n/a | P1 pair tool vs unattributed FollowB, lower 95% CI bound |
| `\PonePairToolVsUnattributedFollowBHi` | n/a | P1 pair tool vs unattributed FollowB, upper 95% CI bound |
| `\PonePairToolVsUnattributedFollowBCI` | n/a | P1 pair tool vs unattributed FollowB, 95% CI |
| `\PonePairToolVsUnattributedFollowBN` | n/a | P1 pair tool vs unattributed FollowB, n |
| `\PonePairToolVsUnattributedFollowBP` | n/a | P1 pair tool vs unattributed FollowB, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsUnattributedEsc` | n/a | P1 pair tool vs unattributed Esc [n/a: no data yet] |
| `\PonePairToolVsUnattributedEscLo` | n/a | P1 pair tool vs unattributed Esc, lower 95% CI bound |
| `\PonePairToolVsUnattributedEscHi` | n/a | P1 pair tool vs unattributed Esc, upper 95% CI bound |
| `\PonePairToolVsUnattributedEscCI` | n/a | P1 pair tool vs unattributed Esc, 95% CI |
| `\PonePairToolVsUnattributedEscN` | n/a | P1 pair tool vs unattributed Esc, n |
| `\PonePairToolVsUnattributedEscP` | n/a | P1 pair tool vs unattributed Esc, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsUnattributedNet` | n/a | P1 pair tool vs unattributed Net [n/a: no data yet] |
| `\PonePairToolVsUnattributedNetLo` | n/a | P1 pair tool vs unattributed Net, lower 95% CI bound |
| `\PonePairToolVsUnattributedNetHi` | n/a | P1 pair tool vs unattributed Net, upper 95% CI bound |
| `\PonePairToolVsUnattributedNetCI` | n/a | P1 pair tool vs unattributed Net, 95% CI |
| `\PonePairToolVsUnattributedNetN` | n/a | P1 pair tool vs unattributed Net, n |
| `\PonePairToolVsUnattributedNetP` | n/a | P1 pair tool vs unattributed Net, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsDocumentFollowA` | n/a | P1 pair tool vs document FollowA [n/a: no data yet] |
| `\PonePairToolVsDocumentFollowALo` | n/a | P1 pair tool vs document FollowA, lower 95% CI bound |
| `\PonePairToolVsDocumentFollowAHi` | n/a | P1 pair tool vs document FollowA, upper 95% CI bound |
| `\PonePairToolVsDocumentFollowACI` | n/a | P1 pair tool vs document FollowA, 95% CI |
| `\PonePairToolVsDocumentFollowAN` | n/a | P1 pair tool vs document FollowA, n |
| `\PonePairToolVsDocumentFollowAP` | n/a | P1 pair tool vs document FollowA, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsDocumentFollowB` | n/a | P1 pair tool vs document FollowB [n/a: no data yet] |
| `\PonePairToolVsDocumentFollowBLo` | n/a | P1 pair tool vs document FollowB, lower 95% CI bound |
| `\PonePairToolVsDocumentFollowBHi` | n/a | P1 pair tool vs document FollowB, upper 95% CI bound |
| `\PonePairToolVsDocumentFollowBCI` | n/a | P1 pair tool vs document FollowB, 95% CI |
| `\PonePairToolVsDocumentFollowBN` | n/a | P1 pair tool vs document FollowB, n |
| `\PonePairToolVsDocumentFollowBP` | n/a | P1 pair tool vs document FollowB, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsDocumentEsc` | n/a | P1 pair tool vs document Esc [n/a: no data yet] |
| `\PonePairToolVsDocumentEscLo` | n/a | P1 pair tool vs document Esc, lower 95% CI bound |
| `\PonePairToolVsDocumentEscHi` | n/a | P1 pair tool vs document Esc, upper 95% CI bound |
| `\PonePairToolVsDocumentEscCI` | n/a | P1 pair tool vs document Esc, 95% CI |
| `\PonePairToolVsDocumentEscN` | n/a | P1 pair tool vs document Esc, n |
| `\PonePairToolVsDocumentEscP` | n/a | P1 pair tool vs document Esc, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsDocumentNet` | n/a | P1 pair tool vs document Net [n/a: no data yet] |
| `\PonePairToolVsDocumentNetLo` | n/a | P1 pair tool vs document Net, lower 95% CI bound |
| `\PonePairToolVsDocumentNetHi` | n/a | P1 pair tool vs document Net, upper 95% CI bound |
| `\PonePairToolVsDocumentNetCI` | n/a | P1 pair tool vs document Net, 95% CI |
| `\PonePairToolVsDocumentNetN` | n/a | P1 pair tool vs document Net, n |
| `\PonePairToolVsDocumentNetP` | n/a | P1 pair tool vs document Net, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsUserFollowA` | n/a | P1 pair web vs user FollowA [n/a: no data yet] |
| `\PonePairWebVsUserFollowALo` | n/a | P1 pair web vs user FollowA, lower 95% CI bound |
| `\PonePairWebVsUserFollowAHi` | n/a | P1 pair web vs user FollowA, upper 95% CI bound |
| `\PonePairWebVsUserFollowACI` | n/a | P1 pair web vs user FollowA, 95% CI |
| `\PonePairWebVsUserFollowAN` | n/a | P1 pair web vs user FollowA, n |
| `\PonePairWebVsUserFollowAP` | n/a | P1 pair web vs user FollowA, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsUserFollowB` | n/a | P1 pair web vs user FollowB [n/a: no data yet] |
| `\PonePairWebVsUserFollowBLo` | n/a | P1 pair web vs user FollowB, lower 95% CI bound |
| `\PonePairWebVsUserFollowBHi` | n/a | P1 pair web vs user FollowB, upper 95% CI bound |
| `\PonePairWebVsUserFollowBCI` | n/a | P1 pair web vs user FollowB, 95% CI |
| `\PonePairWebVsUserFollowBN` | n/a | P1 pair web vs user FollowB, n |
| `\PonePairWebVsUserFollowBP` | n/a | P1 pair web vs user FollowB, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsUserEsc` | n/a | P1 pair web vs user Esc [n/a: no data yet] |
| `\PonePairWebVsUserEscLo` | n/a | P1 pair web vs user Esc, lower 95% CI bound |
| `\PonePairWebVsUserEscHi` | n/a | P1 pair web vs user Esc, upper 95% CI bound |
| `\PonePairWebVsUserEscCI` | n/a | P1 pair web vs user Esc, 95% CI |
| `\PonePairWebVsUserEscN` | n/a | P1 pair web vs user Esc, n |
| `\PonePairWebVsUserEscP` | n/a | P1 pair web vs user Esc, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsUserNet` | n/a | P1 pair web vs user Net [n/a: no data yet] |
| `\PonePairWebVsUserNetLo` | n/a | P1 pair web vs user Net, lower 95% CI bound |
| `\PonePairWebVsUserNetHi` | n/a | P1 pair web vs user Net, upper 95% CI bound |
| `\PonePairWebVsUserNetCI` | n/a | P1 pair web vs user Net, 95% CI |
| `\PonePairWebVsUserNetN` | n/a | P1 pair web vs user Net, n |
| `\PonePairWebVsUserNetP` | n/a | P1 pair web vs user Net, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsUnattributedFollowA` | n/a | P1 pair user vs unattributed FollowA [n/a: no data yet] |
| `\PonePairUserVsUnattributedFollowALo` | n/a | P1 pair user vs unattributed FollowA, lower 95% CI bound |
| `\PonePairUserVsUnattributedFollowAHi` | n/a | P1 pair user vs unattributed FollowA, upper 95% CI bound |
| `\PonePairUserVsUnattributedFollowACI` | n/a | P1 pair user vs unattributed FollowA, 95% CI |
| `\PonePairUserVsUnattributedFollowAN` | n/a | P1 pair user vs unattributed FollowA, n |
| `\PonePairUserVsUnattributedFollowAP` | n/a | P1 pair user vs unattributed FollowA, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsUnattributedFollowB` | n/a | P1 pair user vs unattributed FollowB [n/a: no data yet] |
| `\PonePairUserVsUnattributedFollowBLo` | n/a | P1 pair user vs unattributed FollowB, lower 95% CI bound |
| `\PonePairUserVsUnattributedFollowBHi` | n/a | P1 pair user vs unattributed FollowB, upper 95% CI bound |
| `\PonePairUserVsUnattributedFollowBCI` | n/a | P1 pair user vs unattributed FollowB, 95% CI |
| `\PonePairUserVsUnattributedFollowBN` | n/a | P1 pair user vs unattributed FollowB, n |
| `\PonePairUserVsUnattributedFollowBP` | n/a | P1 pair user vs unattributed FollowB, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsUnattributedEsc` | n/a | P1 pair user vs unattributed Esc [n/a: no data yet] |
| `\PonePairUserVsUnattributedEscLo` | n/a | P1 pair user vs unattributed Esc, lower 95% CI bound |
| `\PonePairUserVsUnattributedEscHi` | n/a | P1 pair user vs unattributed Esc, upper 95% CI bound |
| `\PonePairUserVsUnattributedEscCI` | n/a | P1 pair user vs unattributed Esc, 95% CI |
| `\PonePairUserVsUnattributedEscN` | n/a | P1 pair user vs unattributed Esc, n |
| `\PonePairUserVsUnattributedEscP` | n/a | P1 pair user vs unattributed Esc, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsUnattributedNet` | n/a | P1 pair user vs unattributed Net [n/a: no data yet] |
| `\PonePairUserVsUnattributedNetLo` | n/a | P1 pair user vs unattributed Net, lower 95% CI bound |
| `\PonePairUserVsUnattributedNetHi` | n/a | P1 pair user vs unattributed Net, upper 95% CI bound |
| `\PonePairUserVsUnattributedNetCI` | n/a | P1 pair user vs unattributed Net, 95% CI |
| `\PonePairUserVsUnattributedNetN` | n/a | P1 pair user vs unattributed Net, n |
| `\PonePairUserVsUnattributedNetP` | n/a | P1 pair user vs unattributed Net, two-sided bootstrap p (n/a if not tested) |
| `\PonePairAgentVsUnattributedFollowA` | n/a | P1 pair agent vs unattributed FollowA [n/a: no data yet] |
| `\PonePairAgentVsUnattributedFollowALo` | n/a | P1 pair agent vs unattributed FollowA, lower 95% CI bound |
| `\PonePairAgentVsUnattributedFollowAHi` | n/a | P1 pair agent vs unattributed FollowA, upper 95% CI bound |
| `\PonePairAgentVsUnattributedFollowACI` | n/a | P1 pair agent vs unattributed FollowA, 95% CI |
| `\PonePairAgentVsUnattributedFollowAN` | n/a | P1 pair agent vs unattributed FollowA, n |
| `\PonePairAgentVsUnattributedFollowAP` | n/a | P1 pair agent vs unattributed FollowA, two-sided bootstrap p (n/a if not tested) |
| `\PonePairAgentVsUnattributedFollowB` | n/a | P1 pair agent vs unattributed FollowB [n/a: no data yet] |
| `\PonePairAgentVsUnattributedFollowBLo` | n/a | P1 pair agent vs unattributed FollowB, lower 95% CI bound |
| `\PonePairAgentVsUnattributedFollowBHi` | n/a | P1 pair agent vs unattributed FollowB, upper 95% CI bound |
| `\PonePairAgentVsUnattributedFollowBCI` | n/a | P1 pair agent vs unattributed FollowB, 95% CI |
| `\PonePairAgentVsUnattributedFollowBN` | n/a | P1 pair agent vs unattributed FollowB, n |
| `\PonePairAgentVsUnattributedFollowBP` | n/a | P1 pair agent vs unattributed FollowB, two-sided bootstrap p (n/a if not tested) |
| `\PonePairAgentVsUnattributedEsc` | n/a | P1 pair agent vs unattributed Esc [n/a: no data yet] |
| `\PonePairAgentVsUnattributedEscLo` | n/a | P1 pair agent vs unattributed Esc, lower 95% CI bound |
| `\PonePairAgentVsUnattributedEscHi` | n/a | P1 pair agent vs unattributed Esc, upper 95% CI bound |
| `\PonePairAgentVsUnattributedEscCI` | n/a | P1 pair agent vs unattributed Esc, 95% CI |
| `\PonePairAgentVsUnattributedEscN` | n/a | P1 pair agent vs unattributed Esc, n |
| `\PonePairAgentVsUnattributedEscP` | n/a | P1 pair agent vs unattributed Esc, two-sided bootstrap p (n/a if not tested) |
| `\PonePairAgentVsUnattributedNet` | n/a | P1 pair agent vs unattributed Net [n/a: no data yet] |
| `\PonePairAgentVsUnattributedNetLo` | n/a | P1 pair agent vs unattributed Net, lower 95% CI bound |
| `\PonePairAgentVsUnattributedNetHi` | n/a | P1 pair agent vs unattributed Net, upper 95% CI bound |
| `\PonePairAgentVsUnattributedNetCI` | n/a | P1 pair agent vs unattributed Net, 95% CI |
| `\PonePairAgentVsUnattributedNetN` | n/a | P1 pair agent vs unattributed Net, n |
| `\PonePairAgentVsUnattributedNetP` | n/a | P1 pair agent vs unattributed Net, two-sided bootstrap p (n/a if not tested) |
| `\PonePairAgentVsDocumentFollowA` | n/a | P1 pair agent vs document FollowA [n/a: no data yet] |
| `\PonePairAgentVsDocumentFollowALo` | n/a | P1 pair agent vs document FollowA, lower 95% CI bound |
| `\PonePairAgentVsDocumentFollowAHi` | n/a | P1 pair agent vs document FollowA, upper 95% CI bound |
| `\PonePairAgentVsDocumentFollowACI` | n/a | P1 pair agent vs document FollowA, 95% CI |
| `\PonePairAgentVsDocumentFollowAN` | n/a | P1 pair agent vs document FollowA, n |
| `\PonePairAgentVsDocumentFollowAP` | n/a | P1 pair agent vs document FollowA, two-sided bootstrap p (n/a if not tested) |
| `\PonePairAgentVsDocumentFollowB` | n/a | P1 pair agent vs document FollowB [n/a: no data yet] |
| `\PonePairAgentVsDocumentFollowBLo` | n/a | P1 pair agent vs document FollowB, lower 95% CI bound |
| `\PonePairAgentVsDocumentFollowBHi` | n/a | P1 pair agent vs document FollowB, upper 95% CI bound |
| `\PonePairAgentVsDocumentFollowBCI` | n/a | P1 pair agent vs document FollowB, 95% CI |
| `\PonePairAgentVsDocumentFollowBN` | n/a | P1 pair agent vs document FollowB, n |
| `\PonePairAgentVsDocumentFollowBP` | n/a | P1 pair agent vs document FollowB, two-sided bootstrap p (n/a if not tested) |
| `\PonePairAgentVsDocumentEsc` | n/a | P1 pair agent vs document Esc [n/a: no data yet] |
| `\PonePairAgentVsDocumentEscLo` | n/a | P1 pair agent vs document Esc, lower 95% CI bound |
| `\PonePairAgentVsDocumentEscHi` | n/a | P1 pair agent vs document Esc, upper 95% CI bound |
| `\PonePairAgentVsDocumentEscCI` | n/a | P1 pair agent vs document Esc, 95% CI |
| `\PonePairAgentVsDocumentEscN` | n/a | P1 pair agent vs document Esc, n |
| `\PonePairAgentVsDocumentEscP` | n/a | P1 pair agent vs document Esc, two-sided bootstrap p (n/a if not tested) |
| `\PonePairAgentVsDocumentNet` | n/a | P1 pair agent vs document Net [n/a: no data yet] |
| `\PonePairAgentVsDocumentNetLo` | n/a | P1 pair agent vs document Net, lower 95% CI bound |
| `\PonePairAgentVsDocumentNetHi` | n/a | P1 pair agent vs document Net, upper 95% CI bound |
| `\PonePairAgentVsDocumentNetCI` | n/a | P1 pair agent vs document Net, 95% CI |
| `\PonePairAgentVsDocumentNetN` | n/a | P1 pair agent vs document Net, n |
| `\PonePairAgentVsDocumentNetP` | n/a | P1 pair agent vs document Net, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsToolFollowA` | n/a | P1 stale memory vs tool FollowA [n/a: no data yet] |
| `\PoneStaleMemoryVsToolFollowALo` | n/a | P1 stale memory vs tool FollowA, lower 95% CI bound |
| `\PoneStaleMemoryVsToolFollowAHi` | n/a | P1 stale memory vs tool FollowA, upper 95% CI bound |
| `\PoneStaleMemoryVsToolFollowACI` | n/a | P1 stale memory vs tool FollowA, 95% CI |
| `\PoneStaleMemoryVsToolFollowAN` | n/a | P1 stale memory vs tool FollowA, n |
| `\PoneStaleMemoryVsToolFollowAP` | n/a | P1 stale memory vs tool FollowA, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsToolFollowB` | n/a | P1 stale memory vs tool FollowB [n/a: no data yet] |
| `\PoneStaleMemoryVsToolFollowBLo` | n/a | P1 stale memory vs tool FollowB, lower 95% CI bound |
| `\PoneStaleMemoryVsToolFollowBHi` | n/a | P1 stale memory vs tool FollowB, upper 95% CI bound |
| `\PoneStaleMemoryVsToolFollowBCI` | n/a | P1 stale memory vs tool FollowB, 95% CI |
| `\PoneStaleMemoryVsToolFollowBN` | n/a | P1 stale memory vs tool FollowB, n |
| `\PoneStaleMemoryVsToolFollowBP` | n/a | P1 stale memory vs tool FollowB, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsToolEsc` | n/a | P1 stale memory vs tool Esc [n/a: no data yet] |
| `\PoneStaleMemoryVsToolEscLo` | n/a | P1 stale memory vs tool Esc, lower 95% CI bound |
| `\PoneStaleMemoryVsToolEscHi` | n/a | P1 stale memory vs tool Esc, upper 95% CI bound |
| `\PoneStaleMemoryVsToolEscCI` | n/a | P1 stale memory vs tool Esc, 95% CI |
| `\PoneStaleMemoryVsToolEscN` | n/a | P1 stale memory vs tool Esc, n |
| `\PoneStaleMemoryVsToolEscP` | n/a | P1 stale memory vs tool Esc, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsToolNet` | n/a | P1 stale memory vs tool Net [n/a: no data yet] |
| `\PoneStaleMemoryVsToolNetLo` | n/a | P1 stale memory vs tool Net, lower 95% CI bound |
| `\PoneStaleMemoryVsToolNetHi` | n/a | P1 stale memory vs tool Net, upper 95% CI bound |
| `\PoneStaleMemoryVsToolNetCI` | n/a | P1 stale memory vs tool Net, 95% CI |
| `\PoneStaleMemoryVsToolNetN` | n/a | P1 stale memory vs tool Net, n |
| `\PoneStaleMemoryVsToolNetP` | n/a | P1 stale memory vs tool Net, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsDocumentFollowA` | n/a | P1 stale memory vs document FollowA [n/a: no data yet] |
| `\PoneStaleMemoryVsDocumentFollowALo` | n/a | P1 stale memory vs document FollowA, lower 95% CI bound |
| `\PoneStaleMemoryVsDocumentFollowAHi` | n/a | P1 stale memory vs document FollowA, upper 95% CI bound |
| `\PoneStaleMemoryVsDocumentFollowACI` | n/a | P1 stale memory vs document FollowA, 95% CI |
| `\PoneStaleMemoryVsDocumentFollowAN` | n/a | P1 stale memory vs document FollowA, n |
| `\PoneStaleMemoryVsDocumentFollowAP` | n/a | P1 stale memory vs document FollowA, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsDocumentFollowB` | n/a | P1 stale memory vs document FollowB [n/a: no data yet] |
| `\PoneStaleMemoryVsDocumentFollowBLo` | n/a | P1 stale memory vs document FollowB, lower 95% CI bound |
| `\PoneStaleMemoryVsDocumentFollowBHi` | n/a | P1 stale memory vs document FollowB, upper 95% CI bound |
| `\PoneStaleMemoryVsDocumentFollowBCI` | n/a | P1 stale memory vs document FollowB, 95% CI |
| `\PoneStaleMemoryVsDocumentFollowBN` | n/a | P1 stale memory vs document FollowB, n |
| `\PoneStaleMemoryVsDocumentFollowBP` | n/a | P1 stale memory vs document FollowB, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsDocumentEsc` | n/a | P1 stale memory vs document Esc [n/a: no data yet] |
| `\PoneStaleMemoryVsDocumentEscLo` | n/a | P1 stale memory vs document Esc, lower 95% CI bound |
| `\PoneStaleMemoryVsDocumentEscHi` | n/a | P1 stale memory vs document Esc, upper 95% CI bound |
| `\PoneStaleMemoryVsDocumentEscCI` | n/a | P1 stale memory vs document Esc, 95% CI |
| `\PoneStaleMemoryVsDocumentEscN` | n/a | P1 stale memory vs document Esc, n |
| `\PoneStaleMemoryVsDocumentEscP` | n/a | P1 stale memory vs document Esc, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsDocumentNet` | n/a | P1 stale memory vs document Net [n/a: no data yet] |
| `\PoneStaleMemoryVsDocumentNetLo` | n/a | P1 stale memory vs document Net, lower 95% CI bound |
| `\PoneStaleMemoryVsDocumentNetHi` | n/a | P1 stale memory vs document Net, upper 95% CI bound |
| `\PoneStaleMemoryVsDocumentNetCI` | n/a | P1 stale memory vs document Net, 95% CI |
| `\PoneStaleMemoryVsDocumentNetN` | n/a | P1 stale memory vs document Net, n |
| `\PoneStaleMemoryVsDocumentNetP` | n/a | P1 stale memory vs document Net, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsUserFollowA` | n/a | P1 stale memory vs user FollowA [n/a: no data yet] |
| `\PoneStaleMemoryVsUserFollowALo` | n/a | P1 stale memory vs user FollowA, lower 95% CI bound |
| `\PoneStaleMemoryVsUserFollowAHi` | n/a | P1 stale memory vs user FollowA, upper 95% CI bound |
| `\PoneStaleMemoryVsUserFollowACI` | n/a | P1 stale memory vs user FollowA, 95% CI |
| `\PoneStaleMemoryVsUserFollowAN` | n/a | P1 stale memory vs user FollowA, n |
| `\PoneStaleMemoryVsUserFollowAP` | n/a | P1 stale memory vs user FollowA, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsUserFollowB` | n/a | P1 stale memory vs user FollowB [n/a: no data yet] |
| `\PoneStaleMemoryVsUserFollowBLo` | n/a | P1 stale memory vs user FollowB, lower 95% CI bound |
| `\PoneStaleMemoryVsUserFollowBHi` | n/a | P1 stale memory vs user FollowB, upper 95% CI bound |
| `\PoneStaleMemoryVsUserFollowBCI` | n/a | P1 stale memory vs user FollowB, 95% CI |
| `\PoneStaleMemoryVsUserFollowBN` | n/a | P1 stale memory vs user FollowB, n |
| `\PoneStaleMemoryVsUserFollowBP` | n/a | P1 stale memory vs user FollowB, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsUserEsc` | n/a | P1 stale memory vs user Esc [n/a: no data yet] |
| `\PoneStaleMemoryVsUserEscLo` | n/a | P1 stale memory vs user Esc, lower 95% CI bound |
| `\PoneStaleMemoryVsUserEscHi` | n/a | P1 stale memory vs user Esc, upper 95% CI bound |
| `\PoneStaleMemoryVsUserEscCI` | n/a | P1 stale memory vs user Esc, 95% CI |
| `\PoneStaleMemoryVsUserEscN` | n/a | P1 stale memory vs user Esc, n |
| `\PoneStaleMemoryVsUserEscP` | n/a | P1 stale memory vs user Esc, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsUserNet` | n/a | P1 stale memory vs user Net [n/a: no data yet] |
| `\PoneStaleMemoryVsUserNetLo` | n/a | P1 stale memory vs user Net, lower 95% CI bound |
| `\PoneStaleMemoryVsUserNetHi` | n/a | P1 stale memory vs user Net, upper 95% CI bound |
| `\PoneStaleMemoryVsUserNetCI` | n/a | P1 stale memory vs user Net, 95% CI |
| `\PoneStaleMemoryVsUserNetN` | n/a | P1 stale memory vs user Net, n |
| `\PoneStaleMemoryVsUserNetP` | n/a | P1 stale memory vs user Net, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsToolDiffMem` | n/a | P1 staleness control vs tool DiffMem [n/a: no data yet] |
| `\PoneStaleVsToolDiffMemLo` | n/a | P1 staleness control vs tool DiffMem, lower 95% CI bound |
| `\PoneStaleVsToolDiffMemHi` | n/a | P1 staleness control vs tool DiffMem, upper 95% CI bound |
| `\PoneStaleVsToolDiffMemCI` | n/a | P1 staleness control vs tool DiffMem, 95% CI |
| `\PoneStaleVsToolDiffMemN` | n/a | P1 staleness control vs tool DiffMem, n |
| `\PoneStaleVsToolDiffMemP` | n/a | P1 staleness control vs tool DiffMem, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsToolDiffOther` | n/a | P1 staleness control vs tool DiffOther [n/a: no data yet] |
| `\PoneStaleVsToolDiffOtherLo` | n/a | P1 staleness control vs tool DiffOther, lower 95% CI bound |
| `\PoneStaleVsToolDiffOtherHi` | n/a | P1 staleness control vs tool DiffOther, upper 95% CI bound |
| `\PoneStaleVsToolDiffOtherCI` | n/a | P1 staleness control vs tool DiffOther, 95% CI |
| `\PoneStaleVsToolDiffOtherN` | n/a | P1 staleness control vs tool DiffOther, n |
| `\PoneStaleVsToolDiffOtherP` | n/a | P1 staleness control vs tool DiffOther, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsToolNet` | n/a | P1 staleness control vs tool Net [n/a: no data yet] |
| `\PoneStaleVsToolNetLo` | n/a | P1 staleness control vs tool Net, lower 95% CI bound |
| `\PoneStaleVsToolNetHi` | n/a | P1 staleness control vs tool Net, upper 95% CI bound |
| `\PoneStaleVsToolNetCI` | n/a | P1 staleness control vs tool Net, 95% CI |
| `\PoneStaleVsToolNetN` | n/a | P1 staleness control vs tool Net, n |
| `\PoneStaleVsToolNetP` | n/a | P1 staleness control vs tool Net, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsDocumentDiffMem` | n/a | P1 staleness control vs document DiffMem [n/a: no data yet] |
| `\PoneStaleVsDocumentDiffMemLo` | n/a | P1 staleness control vs document DiffMem, lower 95% CI bound |
| `\PoneStaleVsDocumentDiffMemHi` | n/a | P1 staleness control vs document DiffMem, upper 95% CI bound |
| `\PoneStaleVsDocumentDiffMemCI` | n/a | P1 staleness control vs document DiffMem, 95% CI |
| `\PoneStaleVsDocumentDiffMemN` | n/a | P1 staleness control vs document DiffMem, n |
| `\PoneStaleVsDocumentDiffMemP` | n/a | P1 staleness control vs document DiffMem, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsDocumentDiffOther` | n/a | P1 staleness control vs document DiffOther [n/a: no data yet] |
| `\PoneStaleVsDocumentDiffOtherLo` | n/a | P1 staleness control vs document DiffOther, lower 95% CI bound |
| `\PoneStaleVsDocumentDiffOtherHi` | n/a | P1 staleness control vs document DiffOther, upper 95% CI bound |
| `\PoneStaleVsDocumentDiffOtherCI` | n/a | P1 staleness control vs document DiffOther, 95% CI |
| `\PoneStaleVsDocumentDiffOtherN` | n/a | P1 staleness control vs document DiffOther, n |
| `\PoneStaleVsDocumentDiffOtherP` | n/a | P1 staleness control vs document DiffOther, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsDocumentNet` | n/a | P1 staleness control vs document Net [n/a: no data yet] |
| `\PoneStaleVsDocumentNetLo` | n/a | P1 staleness control vs document Net, lower 95% CI bound |
| `\PoneStaleVsDocumentNetHi` | n/a | P1 staleness control vs document Net, upper 95% CI bound |
| `\PoneStaleVsDocumentNetCI` | n/a | P1 staleness control vs document Net, 95% CI |
| `\PoneStaleVsDocumentNetN` | n/a | P1 staleness control vs document Net, n |
| `\PoneStaleVsDocumentNetP` | n/a | P1 staleness control vs document Net, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsUserDiffMem` | n/a | P1 staleness control vs user DiffMem [n/a: no data yet] |
| `\PoneStaleVsUserDiffMemLo` | n/a | P1 staleness control vs user DiffMem, lower 95% CI bound |
| `\PoneStaleVsUserDiffMemHi` | n/a | P1 staleness control vs user DiffMem, upper 95% CI bound |
| `\PoneStaleVsUserDiffMemCI` | n/a | P1 staleness control vs user DiffMem, 95% CI |
| `\PoneStaleVsUserDiffMemN` | n/a | P1 staleness control vs user DiffMem, n |
| `\PoneStaleVsUserDiffMemP` | n/a | P1 staleness control vs user DiffMem, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsUserDiffOther` | n/a | P1 staleness control vs user DiffOther [n/a: no data yet] |
| `\PoneStaleVsUserDiffOtherLo` | n/a | P1 staleness control vs user DiffOther, lower 95% CI bound |
| `\PoneStaleVsUserDiffOtherHi` | n/a | P1 staleness control vs user DiffOther, upper 95% CI bound |
| `\PoneStaleVsUserDiffOtherCI` | n/a | P1 staleness control vs user DiffOther, 95% CI |
| `\PoneStaleVsUserDiffOtherN` | n/a | P1 staleness control vs user DiffOther, n |
| `\PoneStaleVsUserDiffOtherP` | n/a | P1 staleness control vs user DiffOther, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsUserNet` | n/a | P1 staleness control vs user Net [n/a: no data yet] |
| `\PoneStaleVsUserNetLo` | n/a | P1 staleness control vs user Net, lower 95% CI bound |
| `\PoneStaleVsUserNetHi` | n/a | P1 staleness control vs user Net, upper 95% CI bound |
| `\PoneStaleVsUserNetCI` | n/a | P1 staleness control vs user Net, 95% CI |
| `\PoneStaleVsUserNetN` | n/a | P1 staleness control vs user Net, n |
| `\PoneStaleVsUserNetP` | n/a | P1 staleness control vs user Net, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemoryAdoptQwenThreeEightTwoSevenB` | n/a | P1 single claim in memory: % adopted QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PoneSingleMemoryAdoptQwenThreeEightTwoSevenBLo` | n/a | P1 single claim in memory: % adopted QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PoneSingleMemoryAdoptQwenThreeEightTwoSevenBHi` | n/a | P1 single claim in memory: % adopted QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PoneSingleMemoryAdoptQwenThreeEightTwoSevenBCI` | n/a | P1 single claim in memory: % adopted QwenThreeEightTwoSevenB, 95% CI |
| `\PoneSingleMemoryAdoptQwenThreeEightTwoSevenBN` | n/a | P1 single claim in memory: % adopted QwenThreeEightTwoSevenB, n |
| `\PoneSingleMemoryAdoptQwenThreeEightTwoSevenBP` | n/a | P1 single claim in memory: % adopted QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleToolAdoptQwenThreeEightTwoSevenB` | n/a | P1 single claim in tool: % adopted QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PoneSingleToolAdoptQwenThreeEightTwoSevenBLo` | n/a | P1 single claim in tool: % adopted QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PoneSingleToolAdoptQwenThreeEightTwoSevenBHi` | n/a | P1 single claim in tool: % adopted QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PoneSingleToolAdoptQwenThreeEightTwoSevenBCI` | n/a | P1 single claim in tool: % adopted QwenThreeEightTwoSevenB, 95% CI |
| `\PoneSingleToolAdoptQwenThreeEightTwoSevenBN` | n/a | P1 single claim in tool: % adopted QwenThreeEightTwoSevenB, n |
| `\PoneSingleToolAdoptQwenThreeEightTwoSevenBP` | n/a | P1 single claim in tool: % adopted QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemMinusToolQwenThreeEightTwoSevenB` | n/a | P1 single claim: adoption memory - tool QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PoneSingleMemMinusToolQwenThreeEightTwoSevenBLo` | n/a | P1 single claim: adoption memory - tool QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PoneSingleMemMinusToolQwenThreeEightTwoSevenBHi` | n/a | P1 single claim: adoption memory - tool QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PoneSingleMemMinusToolQwenThreeEightTwoSevenBCI` | n/a | P1 single claim: adoption memory - tool QwenThreeEightTwoSevenB, 95% CI |
| `\PoneSingleMemMinusToolQwenThreeEightTwoSevenBN` | n/a | P1 single claim: adoption memory - tool QwenThreeEightTwoSevenB, n |
| `\PoneSingleMemMinusToolQwenThreeEightTwoSevenBP` | n/a | P1 single claim: adoption memory - tool QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemoryAdoptGLMFiveThreeFlash` | n/a | P1 single claim in memory: % adopted GLMFiveThreeFlash [n/a: no data yet] |
| `\PoneSingleMemoryAdoptGLMFiveThreeFlashLo` | n/a | P1 single claim in memory: % adopted GLMFiveThreeFlash, lower 95% CI bound |
| `\PoneSingleMemoryAdoptGLMFiveThreeFlashHi` | n/a | P1 single claim in memory: % adopted GLMFiveThreeFlash, upper 95% CI bound |
| `\PoneSingleMemoryAdoptGLMFiveThreeFlashCI` | n/a | P1 single claim in memory: % adopted GLMFiveThreeFlash, 95% CI |
| `\PoneSingleMemoryAdoptGLMFiveThreeFlashN` | n/a | P1 single claim in memory: % adopted GLMFiveThreeFlash, n |
| `\PoneSingleMemoryAdoptGLMFiveThreeFlashP` | n/a | P1 single claim in memory: % adopted GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleToolAdoptGLMFiveThreeFlash` | n/a | P1 single claim in tool: % adopted GLMFiveThreeFlash [n/a: no data yet] |
| `\PoneSingleToolAdoptGLMFiveThreeFlashLo` | n/a | P1 single claim in tool: % adopted GLMFiveThreeFlash, lower 95% CI bound |
| `\PoneSingleToolAdoptGLMFiveThreeFlashHi` | n/a | P1 single claim in tool: % adopted GLMFiveThreeFlash, upper 95% CI bound |
| `\PoneSingleToolAdoptGLMFiveThreeFlashCI` | n/a | P1 single claim in tool: % adopted GLMFiveThreeFlash, 95% CI |
| `\PoneSingleToolAdoptGLMFiveThreeFlashN` | n/a | P1 single claim in tool: % adopted GLMFiveThreeFlash, n |
| `\PoneSingleToolAdoptGLMFiveThreeFlashP` | n/a | P1 single claim in tool: % adopted GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemMinusToolGLMFiveThreeFlash` | n/a | P1 single claim: adoption memory - tool GLMFiveThreeFlash [n/a: no data yet] |
| `\PoneSingleMemMinusToolGLMFiveThreeFlashLo` | n/a | P1 single claim: adoption memory - tool GLMFiveThreeFlash, lower 95% CI bound |
| `\PoneSingleMemMinusToolGLMFiveThreeFlashHi` | n/a | P1 single claim: adoption memory - tool GLMFiveThreeFlash, upper 95% CI bound |
| `\PoneSingleMemMinusToolGLMFiveThreeFlashCI` | n/a | P1 single claim: adoption memory - tool GLMFiveThreeFlash, 95% CI |
| `\PoneSingleMemMinusToolGLMFiveThreeFlashN` | n/a | P1 single claim: adoption memory - tool GLMFiveThreeFlash, n |
| `\PoneSingleMemMinusToolGLMFiveThreeFlashP` | n/a | P1 single claim: adoption memory - tool GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemoryAdoptGLMFiveTwo` | n/a | P1 single claim in memory: % adopted GLMFiveTwo [n/a: no data yet] |
| `\PoneSingleMemoryAdoptGLMFiveTwoLo` | n/a | P1 single claim in memory: % adopted GLMFiveTwo, lower 95% CI bound |
| `\PoneSingleMemoryAdoptGLMFiveTwoHi` | n/a | P1 single claim in memory: % adopted GLMFiveTwo, upper 95% CI bound |
| `\PoneSingleMemoryAdoptGLMFiveTwoCI` | n/a | P1 single claim in memory: % adopted GLMFiveTwo, 95% CI |
| `\PoneSingleMemoryAdoptGLMFiveTwoN` | n/a | P1 single claim in memory: % adopted GLMFiveTwo, n |
| `\PoneSingleMemoryAdoptGLMFiveTwoP` | n/a | P1 single claim in memory: % adopted GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleToolAdoptGLMFiveTwo` | n/a | P1 single claim in tool: % adopted GLMFiveTwo [n/a: no data yet] |
| `\PoneSingleToolAdoptGLMFiveTwoLo` | n/a | P1 single claim in tool: % adopted GLMFiveTwo, lower 95% CI bound |
| `\PoneSingleToolAdoptGLMFiveTwoHi` | n/a | P1 single claim in tool: % adopted GLMFiveTwo, upper 95% CI bound |
| `\PoneSingleToolAdoptGLMFiveTwoCI` | n/a | P1 single claim in tool: % adopted GLMFiveTwo, 95% CI |
| `\PoneSingleToolAdoptGLMFiveTwoN` | n/a | P1 single claim in tool: % adopted GLMFiveTwo, n |
| `\PoneSingleToolAdoptGLMFiveTwoP` | n/a | P1 single claim in tool: % adopted GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemMinusToolGLMFiveTwo` | n/a | P1 single claim: adoption memory - tool GLMFiveTwo [n/a: no data yet] |
| `\PoneSingleMemMinusToolGLMFiveTwoLo` | n/a | P1 single claim: adoption memory - tool GLMFiveTwo, lower 95% CI bound |
| `\PoneSingleMemMinusToolGLMFiveTwoHi` | n/a | P1 single claim: adoption memory - tool GLMFiveTwo, upper 95% CI bound |
| `\PoneSingleMemMinusToolGLMFiveTwoCI` | n/a | P1 single claim: adoption memory - tool GLMFiveTwo, 95% CI |
| `\PoneSingleMemMinusToolGLMFiveTwoN` | n/a | P1 single claim: adoption memory - tool GLMFiveTwo, n |
| `\PoneSingleMemMinusToolGLMFiveTwoP` | n/a | P1 single claim: adoption memory - tool GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemoryAdoptQwenThreeFiveThreeNineSevenB` | n/a | P1 single claim in memory: % adopted QwenThreeFiveThreeNineSevenB [n/a: no data yet] |
| `\PoneSingleMemoryAdoptQwenThreeFiveThreeNineSevenBLo` | n/a | P1 single claim in memory: % adopted QwenThreeFiveThreeNineSevenB, lower 95% CI bound |
| `\PoneSingleMemoryAdoptQwenThreeFiveThreeNineSevenBHi` | n/a | P1 single claim in memory: % adopted QwenThreeFiveThreeNineSevenB, upper 95% CI bound |
| `\PoneSingleMemoryAdoptQwenThreeFiveThreeNineSevenBCI` | n/a | P1 single claim in memory: % adopted QwenThreeFiveThreeNineSevenB, 95% CI |
| `\PoneSingleMemoryAdoptQwenThreeFiveThreeNineSevenBN` | n/a | P1 single claim in memory: % adopted QwenThreeFiveThreeNineSevenB, n |
| `\PoneSingleMemoryAdoptQwenThreeFiveThreeNineSevenBP` | n/a | P1 single claim in memory: % adopted QwenThreeFiveThreeNineSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleToolAdoptQwenThreeFiveThreeNineSevenB` | n/a | P1 single claim in tool: % adopted QwenThreeFiveThreeNineSevenB [n/a: no data yet] |
| `\PoneSingleToolAdoptQwenThreeFiveThreeNineSevenBLo` | n/a | P1 single claim in tool: % adopted QwenThreeFiveThreeNineSevenB, lower 95% CI bound |
| `\PoneSingleToolAdoptQwenThreeFiveThreeNineSevenBHi` | n/a | P1 single claim in tool: % adopted QwenThreeFiveThreeNineSevenB, upper 95% CI bound |
| `\PoneSingleToolAdoptQwenThreeFiveThreeNineSevenBCI` | n/a | P1 single claim in tool: % adopted QwenThreeFiveThreeNineSevenB, 95% CI |
| `\PoneSingleToolAdoptQwenThreeFiveThreeNineSevenBN` | n/a | P1 single claim in tool: % adopted QwenThreeFiveThreeNineSevenB, n |
| `\PoneSingleToolAdoptQwenThreeFiveThreeNineSevenBP` | n/a | P1 single claim in tool: % adopted QwenThreeFiveThreeNineSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemMinusToolQwenThreeFiveThreeNineSevenB` | n/a | P1 single claim: adoption memory - tool QwenThreeFiveThreeNineSevenB [n/a: no data yet] |
| `\PoneSingleMemMinusToolQwenThreeFiveThreeNineSevenBLo` | n/a | P1 single claim: adoption memory - tool QwenThreeFiveThreeNineSevenB, lower 95% CI bound |
| `\PoneSingleMemMinusToolQwenThreeFiveThreeNineSevenBHi` | n/a | P1 single claim: adoption memory - tool QwenThreeFiveThreeNineSevenB, upper 95% CI bound |
| `\PoneSingleMemMinusToolQwenThreeFiveThreeNineSevenBCI` | n/a | P1 single claim: adoption memory - tool QwenThreeFiveThreeNineSevenB, 95% CI |
| `\PoneSingleMemMinusToolQwenThreeFiveThreeNineSevenBN` | n/a | P1 single claim: adoption memory - tool QwenThreeFiveThreeNineSevenB, n |
| `\PoneSingleMemMinusToolQwenThreeFiveThreeNineSevenBP` | n/a | P1 single claim: adoption memory - tool QwenThreeFiveThreeNineSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetRederivDisagreeQwenThreeEightTwoSevenB` | n/a | re-derivation disagreement rate for untouched notes, QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetRederivDisagreeQwenThreeEightTwoSevenBLo` | n/a | re-derivation disagreement rate for untouched notes, QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetRederivDisagreeQwenThreeEightTwoSevenBHi` | n/a | re-derivation disagreement rate for untouched notes, QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetRederivDisagreeQwenThreeEightTwoSevenBCI` | n/a | re-derivation disagreement rate for untouched notes, QwenThreeEightTwoSevenB, 95% CI |
| `\DetRederivDisagreeQwenThreeEightTwoSevenBN` | n/a | re-derivation disagreement rate for untouched notes, QwenThreeEightTwoSevenB, n |
| `\DetRederivDisagreeQwenThreeEightTwoSevenBP` | n/a | re-derivation disagreement rate for untouched notes, QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatQwenThreeEightTwoSevenBVClean` | n/a | flat-audit rate V clean QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetFlatQwenThreeEightTwoSevenBVCleanLo` | n/a | flat-audit rate V clean QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBVCleanHi` | n/a | flat-audit rate V clean QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBVCleanCI` | n/a | flat-audit rate V clean QwenThreeEightTwoSevenB, 95% CI |
| `\DetFlatQwenThreeEightTwoSevenBVCleanN` | n/a | flat-audit rate V clean QwenThreeEightTwoSevenB, n |
| `\DetFlatQwenThreeEightTwoSevenBVCleanP` | n/a | flat-audit rate V clean QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatQwenThreeEightTwoSevenBVTZero` | n/a | flat-audit rate V T0 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetFlatQwenThreeEightTwoSevenBVTZeroLo` | n/a | flat-audit rate V T0 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBVTZeroHi` | n/a | flat-audit rate V T0 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBVTZeroCI` | n/a | flat-audit rate V T0 QwenThreeEightTwoSevenB, 95% CI |
| `\DetFlatQwenThreeEightTwoSevenBVTZeroN` | n/a | flat-audit rate V T0 QwenThreeEightTwoSevenB, n |
| `\DetFlatQwenThreeEightTwoSevenBVTZeroP` | n/a | flat-audit rate V T0 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatQwenThreeEightTwoSevenBVTOne` | n/a | flat-audit rate V T1 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetFlatQwenThreeEightTwoSevenBVTOneLo` | n/a | flat-audit rate V T1 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBVTOneHi` | n/a | flat-audit rate V T1 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBVTOneCI` | n/a | flat-audit rate V T1 QwenThreeEightTwoSevenB, 95% CI |
| `\DetFlatQwenThreeEightTwoSevenBVTOneN` | n/a | flat-audit rate V T1 QwenThreeEightTwoSevenB, n |
| `\DetFlatQwenThreeEightTwoSevenBVTOneP` | n/a | flat-audit rate V T1 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatQwenThreeEightTwoSevenBVTTwo` | n/a | flat-audit rate V T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetFlatQwenThreeEightTwoSevenBVTTwoLo` | n/a | flat-audit rate V T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBVTTwoHi` | n/a | flat-audit rate V T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBVTTwoCI` | n/a | flat-audit rate V T2 QwenThreeEightTwoSevenB, 95% CI |
| `\DetFlatQwenThreeEightTwoSevenBVTTwoN` | n/a | flat-audit rate V T2 QwenThreeEightTwoSevenB, n |
| `\DetFlatQwenThreeEightTwoSevenBVTTwoP` | n/a | flat-audit rate V T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatQwenThreeEightTwoSevenBVTThree` | n/a | flat-audit rate V T3 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetFlatQwenThreeEightTwoSevenBVTThreeLo` | n/a | flat-audit rate V T3 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBVTThreeHi` | n/a | flat-audit rate V T3 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBVTThreeCI` | n/a | flat-audit rate V T3 QwenThreeEightTwoSevenB, 95% CI |
| `\DetFlatQwenThreeEightTwoSevenBVTThreeN` | n/a | flat-audit rate V T3 QwenThreeEightTwoSevenB, n |
| `\DetFlatQwenThreeEightTwoSevenBVTThreeP` | n/a | flat-audit rate V T3 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBVTZeroStrict` | n/a | within-store rank V T0 Strict QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetRankQwenThreeEightTwoSevenBVTZeroStrictLo` | n/a | within-store rank V T0 Strict QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTZeroStrictHi` | n/a | within-store rank V T0 Strict QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTZeroStrictCI` | n/a | within-store rank V T0 Strict QwenThreeEightTwoSevenB, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBVTZeroStrictN` | n/a | within-store rank V T0 Strict QwenThreeEightTwoSevenB, n |
| `\DetRankQwenThreeEightTwoSevenBVTZeroStrictP` | n/a | within-store rank V T0 Strict QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBVTZeroTiesIncl` | n/a | within-store rank V T0 TiesIncl QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetRankQwenThreeEightTwoSevenBVTZeroTiesInclLo` | n/a | within-store rank V T0 TiesIncl QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTZeroTiesInclHi` | n/a | within-store rank V T0 TiesIncl QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTZeroTiesInclCI` | n/a | within-store rank V T0 TiesIncl QwenThreeEightTwoSevenB, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBVTZeroTiesInclN` | n/a | within-store rank V T0 TiesIncl QwenThreeEightTwoSevenB, n |
| `\DetRankQwenThreeEightTwoSevenBVTZeroTiesInclP` | n/a | within-store rank V T0 TiesIncl QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBVTOneStrict` | n/a | within-store rank V T1 Strict QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetRankQwenThreeEightTwoSevenBVTOneStrictLo` | n/a | within-store rank V T1 Strict QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTOneStrictHi` | n/a | within-store rank V T1 Strict QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTOneStrictCI` | n/a | within-store rank V T1 Strict QwenThreeEightTwoSevenB, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBVTOneStrictN` | n/a | within-store rank V T1 Strict QwenThreeEightTwoSevenB, n |
| `\DetRankQwenThreeEightTwoSevenBVTOneStrictP` | n/a | within-store rank V T1 Strict QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBVTOneTiesIncl` | n/a | within-store rank V T1 TiesIncl QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetRankQwenThreeEightTwoSevenBVTOneTiesInclLo` | n/a | within-store rank V T1 TiesIncl QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTOneTiesInclHi` | n/a | within-store rank V T1 TiesIncl QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTOneTiesInclCI` | n/a | within-store rank V T1 TiesIncl QwenThreeEightTwoSevenB, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBVTOneTiesInclN` | n/a | within-store rank V T1 TiesIncl QwenThreeEightTwoSevenB, n |
| `\DetRankQwenThreeEightTwoSevenBVTOneTiesInclP` | n/a | within-store rank V T1 TiesIncl QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBVTTwoStrict` | n/a | within-store rank V T2 Strict QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetRankQwenThreeEightTwoSevenBVTTwoStrictLo` | n/a | within-store rank V T2 Strict QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTTwoStrictHi` | n/a | within-store rank V T2 Strict QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTTwoStrictCI` | n/a | within-store rank V T2 Strict QwenThreeEightTwoSevenB, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBVTTwoStrictN` | n/a | within-store rank V T2 Strict QwenThreeEightTwoSevenB, n |
| `\DetRankQwenThreeEightTwoSevenBVTTwoStrictP` | n/a | within-store rank V T2 Strict QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBVTTwoTiesIncl` | n/a | within-store rank V T2 TiesIncl QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetRankQwenThreeEightTwoSevenBVTTwoTiesInclLo` | n/a | within-store rank V T2 TiesIncl QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTTwoTiesInclHi` | n/a | within-store rank V T2 TiesIncl QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTTwoTiesInclCI` | n/a | within-store rank V T2 TiesIncl QwenThreeEightTwoSevenB, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBVTTwoTiesInclN` | n/a | within-store rank V T2 TiesIncl QwenThreeEightTwoSevenB, n |
| `\DetRankQwenThreeEightTwoSevenBVTTwoTiesInclP` | n/a | within-store rank V T2 TiesIncl QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBVTThreeStrict` | n/a | within-store rank V T3 Strict QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetRankQwenThreeEightTwoSevenBVTThreeStrictLo` | n/a | within-store rank V T3 Strict QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTThreeStrictHi` | n/a | within-store rank V T3 Strict QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTThreeStrictCI` | n/a | within-store rank V T3 Strict QwenThreeEightTwoSevenB, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBVTThreeStrictN` | n/a | within-store rank V T3 Strict QwenThreeEightTwoSevenB, n |
| `\DetRankQwenThreeEightTwoSevenBVTThreeStrictP` | n/a | within-store rank V T3 Strict QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBVTThreeTiesIncl` | n/a | within-store rank V T3 TiesIncl QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetRankQwenThreeEightTwoSevenBVTThreeTiesInclLo` | n/a | within-store rank V T3 TiesIncl QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTThreeTiesInclHi` | n/a | within-store rank V T3 TiesIncl QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTThreeTiesInclCI` | n/a | within-store rank V T3 TiesIncl QwenThreeEightTwoSevenB, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBVTThreeTiesInclN` | n/a | within-store rank V T3 TiesIncl QwenThreeEightTwoSevenB, n |
| `\DetRankQwenThreeEightTwoSevenBVTThreeTiesInclP` | n/a | within-store rank V T3 TiesIncl QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatQwenThreeEightTwoSevenBCClean` | n/a | flat-audit rate C clean QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetFlatQwenThreeEightTwoSevenBCCleanLo` | n/a | flat-audit rate C clean QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBCCleanHi` | n/a | flat-audit rate C clean QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBCCleanCI` | n/a | flat-audit rate C clean QwenThreeEightTwoSevenB, 95% CI |
| `\DetFlatQwenThreeEightTwoSevenBCCleanN` | n/a | flat-audit rate C clean QwenThreeEightTwoSevenB, n |
| `\DetFlatQwenThreeEightTwoSevenBCCleanP` | n/a | flat-audit rate C clean QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatQwenThreeEightTwoSevenBCTZero` | n/a | flat-audit rate C T0 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetFlatQwenThreeEightTwoSevenBCTZeroLo` | n/a | flat-audit rate C T0 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBCTZeroHi` | n/a | flat-audit rate C T0 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBCTZeroCI` | n/a | flat-audit rate C T0 QwenThreeEightTwoSevenB, 95% CI |
| `\DetFlatQwenThreeEightTwoSevenBCTZeroN` | n/a | flat-audit rate C T0 QwenThreeEightTwoSevenB, n |
| `\DetFlatQwenThreeEightTwoSevenBCTZeroP` | n/a | flat-audit rate C T0 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatQwenThreeEightTwoSevenBCTOne` | n/a | flat-audit rate C T1 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetFlatQwenThreeEightTwoSevenBCTOneLo` | n/a | flat-audit rate C T1 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBCTOneHi` | n/a | flat-audit rate C T1 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBCTOneCI` | n/a | flat-audit rate C T1 QwenThreeEightTwoSevenB, 95% CI |
| `\DetFlatQwenThreeEightTwoSevenBCTOneN` | n/a | flat-audit rate C T1 QwenThreeEightTwoSevenB, n |
| `\DetFlatQwenThreeEightTwoSevenBCTOneP` | n/a | flat-audit rate C T1 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatQwenThreeEightTwoSevenBCTTwo` | n/a | flat-audit rate C T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetFlatQwenThreeEightTwoSevenBCTTwoLo` | n/a | flat-audit rate C T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBCTTwoHi` | n/a | flat-audit rate C T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBCTTwoCI` | n/a | flat-audit rate C T2 QwenThreeEightTwoSevenB, 95% CI |
| `\DetFlatQwenThreeEightTwoSevenBCTTwoN` | n/a | flat-audit rate C T2 QwenThreeEightTwoSevenB, n |
| `\DetFlatQwenThreeEightTwoSevenBCTTwoP` | n/a | flat-audit rate C T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatQwenThreeEightTwoSevenBCTThree` | n/a | flat-audit rate C T3 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetFlatQwenThreeEightTwoSevenBCTThreeLo` | n/a | flat-audit rate C T3 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBCTThreeHi` | n/a | flat-audit rate C T3 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBCTThreeCI` | n/a | flat-audit rate C T3 QwenThreeEightTwoSevenB, 95% CI |
| `\DetFlatQwenThreeEightTwoSevenBCTThreeN` | n/a | flat-audit rate C T3 QwenThreeEightTwoSevenB, n |
| `\DetFlatQwenThreeEightTwoSevenBCTThreeP` | n/a | flat-audit rate C T3 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBCTZeroStrict` | n/a | within-store rank C T0 Strict QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetRankQwenThreeEightTwoSevenBCTZeroStrictLo` | n/a | within-store rank C T0 Strict QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTZeroStrictHi` | n/a | within-store rank C T0 Strict QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTZeroStrictCI` | n/a | within-store rank C T0 Strict QwenThreeEightTwoSevenB, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBCTZeroStrictN` | n/a | within-store rank C T0 Strict QwenThreeEightTwoSevenB, n |
| `\DetRankQwenThreeEightTwoSevenBCTZeroStrictP` | n/a | within-store rank C T0 Strict QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBCTZeroTiesIncl` | n/a | within-store rank C T0 TiesIncl QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetRankQwenThreeEightTwoSevenBCTZeroTiesInclLo` | n/a | within-store rank C T0 TiesIncl QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTZeroTiesInclHi` | n/a | within-store rank C T0 TiesIncl QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTZeroTiesInclCI` | n/a | within-store rank C T0 TiesIncl QwenThreeEightTwoSevenB, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBCTZeroTiesInclN` | n/a | within-store rank C T0 TiesIncl QwenThreeEightTwoSevenB, n |
| `\DetRankQwenThreeEightTwoSevenBCTZeroTiesInclP` | n/a | within-store rank C T0 TiesIncl QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBCTOneStrict` | n/a | within-store rank C T1 Strict QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetRankQwenThreeEightTwoSevenBCTOneStrictLo` | n/a | within-store rank C T1 Strict QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTOneStrictHi` | n/a | within-store rank C T1 Strict QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTOneStrictCI` | n/a | within-store rank C T1 Strict QwenThreeEightTwoSevenB, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBCTOneStrictN` | n/a | within-store rank C T1 Strict QwenThreeEightTwoSevenB, n |
| `\DetRankQwenThreeEightTwoSevenBCTOneStrictP` | n/a | within-store rank C T1 Strict QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBCTOneTiesIncl` | n/a | within-store rank C T1 TiesIncl QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetRankQwenThreeEightTwoSevenBCTOneTiesInclLo` | n/a | within-store rank C T1 TiesIncl QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTOneTiesInclHi` | n/a | within-store rank C T1 TiesIncl QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTOneTiesInclCI` | n/a | within-store rank C T1 TiesIncl QwenThreeEightTwoSevenB, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBCTOneTiesInclN` | n/a | within-store rank C T1 TiesIncl QwenThreeEightTwoSevenB, n |
| `\DetRankQwenThreeEightTwoSevenBCTOneTiesInclP` | n/a | within-store rank C T1 TiesIncl QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBCTTwoStrict` | n/a | within-store rank C T2 Strict QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetRankQwenThreeEightTwoSevenBCTTwoStrictLo` | n/a | within-store rank C T2 Strict QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTTwoStrictHi` | n/a | within-store rank C T2 Strict QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTTwoStrictCI` | n/a | within-store rank C T2 Strict QwenThreeEightTwoSevenB, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBCTTwoStrictN` | n/a | within-store rank C T2 Strict QwenThreeEightTwoSevenB, n |
| `\DetRankQwenThreeEightTwoSevenBCTTwoStrictP` | n/a | within-store rank C T2 Strict QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBCTTwoTiesIncl` | n/a | within-store rank C T2 TiesIncl QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetRankQwenThreeEightTwoSevenBCTTwoTiesInclLo` | n/a | within-store rank C T2 TiesIncl QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTTwoTiesInclHi` | n/a | within-store rank C T2 TiesIncl QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTTwoTiesInclCI` | n/a | within-store rank C T2 TiesIncl QwenThreeEightTwoSevenB, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBCTTwoTiesInclN` | n/a | within-store rank C T2 TiesIncl QwenThreeEightTwoSevenB, n |
| `\DetRankQwenThreeEightTwoSevenBCTTwoTiesInclP` | n/a | within-store rank C T2 TiesIncl QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBCTThreeStrict` | n/a | within-store rank C T3 Strict QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetRankQwenThreeEightTwoSevenBCTThreeStrictLo` | n/a | within-store rank C T3 Strict QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTThreeStrictHi` | n/a | within-store rank C T3 Strict QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTThreeStrictCI` | n/a | within-store rank C T3 Strict QwenThreeEightTwoSevenB, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBCTThreeStrictN` | n/a | within-store rank C T3 Strict QwenThreeEightTwoSevenB, n |
| `\DetRankQwenThreeEightTwoSevenBCTThreeStrictP` | n/a | within-store rank C T3 Strict QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBCTThreeTiesIncl` | n/a | within-store rank C T3 TiesIncl QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\DetRankQwenThreeEightTwoSevenBCTThreeTiesInclLo` | n/a | within-store rank C T3 TiesIncl QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTThreeTiesInclHi` | n/a | within-store rank C T3 TiesIncl QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTThreeTiesInclCI` | n/a | within-store rank C T3 TiesIncl QwenThreeEightTwoSevenB, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBCTThreeTiesInclN` | n/a | within-store rank C T3 TiesIncl QwenThreeEightTwoSevenB, n |
| `\DetRankQwenThreeEightTwoSevenBCTThreeTiesInclP` | n/a | within-store rank C T3 TiesIncl QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\DetRederivDisagreeGLMFiveThreeFlash` | n/a | re-derivation disagreement rate for untouched notes, GLMFiveThreeFlash [n/a: no data yet] |
| `\DetRederivDisagreeGLMFiveThreeFlashLo` | n/a | re-derivation disagreement rate for untouched notes, GLMFiveThreeFlash, lower 95% CI bound |
| `\DetRederivDisagreeGLMFiveThreeFlashHi` | n/a | re-derivation disagreement rate for untouched notes, GLMFiveThreeFlash, upper 95% CI bound |
| `\DetRederivDisagreeGLMFiveThreeFlashCI` | n/a | re-derivation disagreement rate for untouched notes, GLMFiveThreeFlash, 95% CI |
| `\DetRederivDisagreeGLMFiveThreeFlashN` | n/a | re-derivation disagreement rate for untouched notes, GLMFiveThreeFlash, n |
| `\DetRederivDisagreeGLMFiveThreeFlashP` | n/a | re-derivation disagreement rate for untouched notes, GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveThreeFlashVClean` | n/a | flat-audit rate V clean GLMFiveThreeFlash [n/a: no data yet] |
| `\DetFlatGLMFiveThreeFlashVCleanLo` | n/a | flat-audit rate V clean GLMFiveThreeFlash, lower 95% CI bound |
| `\DetFlatGLMFiveThreeFlashVCleanHi` | n/a | flat-audit rate V clean GLMFiveThreeFlash, upper 95% CI bound |
| `\DetFlatGLMFiveThreeFlashVCleanCI` | n/a | flat-audit rate V clean GLMFiveThreeFlash, 95% CI |
| `\DetFlatGLMFiveThreeFlashVCleanN` | n/a | flat-audit rate V clean GLMFiveThreeFlash, n |
| `\DetFlatGLMFiveThreeFlashVCleanP` | n/a | flat-audit rate V clean GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveThreeFlashVTZero` | n/a | flat-audit rate V T0 GLMFiveThreeFlash [n/a: no data yet] |
| `\DetFlatGLMFiveThreeFlashVTZeroLo` | n/a | flat-audit rate V T0 GLMFiveThreeFlash, lower 95% CI bound |
| `\DetFlatGLMFiveThreeFlashVTZeroHi` | n/a | flat-audit rate V T0 GLMFiveThreeFlash, upper 95% CI bound |
| `\DetFlatGLMFiveThreeFlashVTZeroCI` | n/a | flat-audit rate V T0 GLMFiveThreeFlash, 95% CI |
| `\DetFlatGLMFiveThreeFlashVTZeroN` | n/a | flat-audit rate V T0 GLMFiveThreeFlash, n |
| `\DetFlatGLMFiveThreeFlashVTZeroP` | n/a | flat-audit rate V T0 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveThreeFlashVTOne` | n/a | flat-audit rate V T1 GLMFiveThreeFlash [n/a: no data yet] |
| `\DetFlatGLMFiveThreeFlashVTOneLo` | n/a | flat-audit rate V T1 GLMFiveThreeFlash, lower 95% CI bound |
| `\DetFlatGLMFiveThreeFlashVTOneHi` | n/a | flat-audit rate V T1 GLMFiveThreeFlash, upper 95% CI bound |
| `\DetFlatGLMFiveThreeFlashVTOneCI` | n/a | flat-audit rate V T1 GLMFiveThreeFlash, 95% CI |
| `\DetFlatGLMFiveThreeFlashVTOneN` | n/a | flat-audit rate V T1 GLMFiveThreeFlash, n |
| `\DetFlatGLMFiveThreeFlashVTOneP` | n/a | flat-audit rate V T1 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveThreeFlashVTTwo` | n/a | flat-audit rate V T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\DetFlatGLMFiveThreeFlashVTTwoLo` | n/a | flat-audit rate V T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\DetFlatGLMFiveThreeFlashVTTwoHi` | n/a | flat-audit rate V T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\DetFlatGLMFiveThreeFlashVTTwoCI` | n/a | flat-audit rate V T2 GLMFiveThreeFlash, 95% CI |
| `\DetFlatGLMFiveThreeFlashVTTwoN` | n/a | flat-audit rate V T2 GLMFiveThreeFlash, n |
| `\DetFlatGLMFiveThreeFlashVTTwoP` | n/a | flat-audit rate V T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveThreeFlashVTThree` | n/a | flat-audit rate V T3 GLMFiveThreeFlash [n/a: no data yet] |
| `\DetFlatGLMFiveThreeFlashVTThreeLo` | n/a | flat-audit rate V T3 GLMFiveThreeFlash, lower 95% CI bound |
| `\DetFlatGLMFiveThreeFlashVTThreeHi` | n/a | flat-audit rate V T3 GLMFiveThreeFlash, upper 95% CI bound |
| `\DetFlatGLMFiveThreeFlashVTThreeCI` | n/a | flat-audit rate V T3 GLMFiveThreeFlash, 95% CI |
| `\DetFlatGLMFiveThreeFlashVTThreeN` | n/a | flat-audit rate V T3 GLMFiveThreeFlash, n |
| `\DetFlatGLMFiveThreeFlashVTThreeP` | n/a | flat-audit rate V T3 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashVTZeroStrict` | n/a | within-store rank V T0 Strict GLMFiveThreeFlash [n/a: no data yet] |
| `\DetRankGLMFiveThreeFlashVTZeroStrictLo` | n/a | within-store rank V T0 Strict GLMFiveThreeFlash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTZeroStrictHi` | n/a | within-store rank V T0 Strict GLMFiveThreeFlash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTZeroStrictCI` | n/a | within-store rank V T0 Strict GLMFiveThreeFlash, 95% CI |
| `\DetRankGLMFiveThreeFlashVTZeroStrictN` | n/a | within-store rank V T0 Strict GLMFiveThreeFlash, n |
| `\DetRankGLMFiveThreeFlashVTZeroStrictP` | n/a | within-store rank V T0 Strict GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashVTZeroTiesIncl` | n/a | within-store rank V T0 TiesIncl GLMFiveThreeFlash [n/a: no data yet] |
| `\DetRankGLMFiveThreeFlashVTZeroTiesInclLo` | n/a | within-store rank V T0 TiesIncl GLMFiveThreeFlash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTZeroTiesInclHi` | n/a | within-store rank V T0 TiesIncl GLMFiveThreeFlash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTZeroTiesInclCI` | n/a | within-store rank V T0 TiesIncl GLMFiveThreeFlash, 95% CI |
| `\DetRankGLMFiveThreeFlashVTZeroTiesInclN` | n/a | within-store rank V T0 TiesIncl GLMFiveThreeFlash, n |
| `\DetRankGLMFiveThreeFlashVTZeroTiesInclP` | n/a | within-store rank V T0 TiesIncl GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashVTOneStrict` | n/a | within-store rank V T1 Strict GLMFiveThreeFlash [n/a: no data yet] |
| `\DetRankGLMFiveThreeFlashVTOneStrictLo` | n/a | within-store rank V T1 Strict GLMFiveThreeFlash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTOneStrictHi` | n/a | within-store rank V T1 Strict GLMFiveThreeFlash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTOneStrictCI` | n/a | within-store rank V T1 Strict GLMFiveThreeFlash, 95% CI |
| `\DetRankGLMFiveThreeFlashVTOneStrictN` | n/a | within-store rank V T1 Strict GLMFiveThreeFlash, n |
| `\DetRankGLMFiveThreeFlashVTOneStrictP` | n/a | within-store rank V T1 Strict GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashVTOneTiesIncl` | n/a | within-store rank V T1 TiesIncl GLMFiveThreeFlash [n/a: no data yet] |
| `\DetRankGLMFiveThreeFlashVTOneTiesInclLo` | n/a | within-store rank V T1 TiesIncl GLMFiveThreeFlash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTOneTiesInclHi` | n/a | within-store rank V T1 TiesIncl GLMFiveThreeFlash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTOneTiesInclCI` | n/a | within-store rank V T1 TiesIncl GLMFiveThreeFlash, 95% CI |
| `\DetRankGLMFiveThreeFlashVTOneTiesInclN` | n/a | within-store rank V T1 TiesIncl GLMFiveThreeFlash, n |
| `\DetRankGLMFiveThreeFlashVTOneTiesInclP` | n/a | within-store rank V T1 TiesIncl GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashVTTwoStrict` | n/a | within-store rank V T2 Strict GLMFiveThreeFlash [n/a: no data yet] |
| `\DetRankGLMFiveThreeFlashVTTwoStrictLo` | n/a | within-store rank V T2 Strict GLMFiveThreeFlash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTTwoStrictHi` | n/a | within-store rank V T2 Strict GLMFiveThreeFlash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTTwoStrictCI` | n/a | within-store rank V T2 Strict GLMFiveThreeFlash, 95% CI |
| `\DetRankGLMFiveThreeFlashVTTwoStrictN` | n/a | within-store rank V T2 Strict GLMFiveThreeFlash, n |
| `\DetRankGLMFiveThreeFlashVTTwoStrictP` | n/a | within-store rank V T2 Strict GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashVTTwoTiesIncl` | n/a | within-store rank V T2 TiesIncl GLMFiveThreeFlash [n/a: no data yet] |
| `\DetRankGLMFiveThreeFlashVTTwoTiesInclLo` | n/a | within-store rank V T2 TiesIncl GLMFiveThreeFlash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTTwoTiesInclHi` | n/a | within-store rank V T2 TiesIncl GLMFiveThreeFlash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTTwoTiesInclCI` | n/a | within-store rank V T2 TiesIncl GLMFiveThreeFlash, 95% CI |
| `\DetRankGLMFiveThreeFlashVTTwoTiesInclN` | n/a | within-store rank V T2 TiesIncl GLMFiveThreeFlash, n |
| `\DetRankGLMFiveThreeFlashVTTwoTiesInclP` | n/a | within-store rank V T2 TiesIncl GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashVTThreeStrict` | n/a | within-store rank V T3 Strict GLMFiveThreeFlash [n/a: no data yet] |
| `\DetRankGLMFiveThreeFlashVTThreeStrictLo` | n/a | within-store rank V T3 Strict GLMFiveThreeFlash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTThreeStrictHi` | n/a | within-store rank V T3 Strict GLMFiveThreeFlash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTThreeStrictCI` | n/a | within-store rank V T3 Strict GLMFiveThreeFlash, 95% CI |
| `\DetRankGLMFiveThreeFlashVTThreeStrictN` | n/a | within-store rank V T3 Strict GLMFiveThreeFlash, n |
| `\DetRankGLMFiveThreeFlashVTThreeStrictP` | n/a | within-store rank V T3 Strict GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashVTThreeTiesIncl` | n/a | within-store rank V T3 TiesIncl GLMFiveThreeFlash [n/a: no data yet] |
| `\DetRankGLMFiveThreeFlashVTThreeTiesInclLo` | n/a | within-store rank V T3 TiesIncl GLMFiveThreeFlash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTThreeTiesInclHi` | n/a | within-store rank V T3 TiesIncl GLMFiveThreeFlash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTThreeTiesInclCI` | n/a | within-store rank V T3 TiesIncl GLMFiveThreeFlash, 95% CI |
| `\DetRankGLMFiveThreeFlashVTThreeTiesInclN` | n/a | within-store rank V T3 TiesIncl GLMFiveThreeFlash, n |
| `\DetRankGLMFiveThreeFlashVTThreeTiesInclP` | n/a | within-store rank V T3 TiesIncl GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveThreeFlashCClean` | n/a | flat-audit rate C clean GLMFiveThreeFlash [n/a: no data yet] |
| `\DetFlatGLMFiveThreeFlashCCleanLo` | n/a | flat-audit rate C clean GLMFiveThreeFlash, lower 95% CI bound |
| `\DetFlatGLMFiveThreeFlashCCleanHi` | n/a | flat-audit rate C clean GLMFiveThreeFlash, upper 95% CI bound |
| `\DetFlatGLMFiveThreeFlashCCleanCI` | n/a | flat-audit rate C clean GLMFiveThreeFlash, 95% CI |
| `\DetFlatGLMFiveThreeFlashCCleanN` | n/a | flat-audit rate C clean GLMFiveThreeFlash, n |
| `\DetFlatGLMFiveThreeFlashCCleanP` | n/a | flat-audit rate C clean GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveThreeFlashCTZero` | n/a | flat-audit rate C T0 GLMFiveThreeFlash [n/a: no data yet] |
| `\DetFlatGLMFiveThreeFlashCTZeroLo` | n/a | flat-audit rate C T0 GLMFiveThreeFlash, lower 95% CI bound |
| `\DetFlatGLMFiveThreeFlashCTZeroHi` | n/a | flat-audit rate C T0 GLMFiveThreeFlash, upper 95% CI bound |
| `\DetFlatGLMFiveThreeFlashCTZeroCI` | n/a | flat-audit rate C T0 GLMFiveThreeFlash, 95% CI |
| `\DetFlatGLMFiveThreeFlashCTZeroN` | n/a | flat-audit rate C T0 GLMFiveThreeFlash, n |
| `\DetFlatGLMFiveThreeFlashCTZeroP` | n/a | flat-audit rate C T0 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveThreeFlashCTOne` | n/a | flat-audit rate C T1 GLMFiveThreeFlash [n/a: no data yet] |
| `\DetFlatGLMFiveThreeFlashCTOneLo` | n/a | flat-audit rate C T1 GLMFiveThreeFlash, lower 95% CI bound |
| `\DetFlatGLMFiveThreeFlashCTOneHi` | n/a | flat-audit rate C T1 GLMFiveThreeFlash, upper 95% CI bound |
| `\DetFlatGLMFiveThreeFlashCTOneCI` | n/a | flat-audit rate C T1 GLMFiveThreeFlash, 95% CI |
| `\DetFlatGLMFiveThreeFlashCTOneN` | n/a | flat-audit rate C T1 GLMFiveThreeFlash, n |
| `\DetFlatGLMFiveThreeFlashCTOneP` | n/a | flat-audit rate C T1 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveThreeFlashCTTwo` | n/a | flat-audit rate C T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\DetFlatGLMFiveThreeFlashCTTwoLo` | n/a | flat-audit rate C T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\DetFlatGLMFiveThreeFlashCTTwoHi` | n/a | flat-audit rate C T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\DetFlatGLMFiveThreeFlashCTTwoCI` | n/a | flat-audit rate C T2 GLMFiveThreeFlash, 95% CI |
| `\DetFlatGLMFiveThreeFlashCTTwoN` | n/a | flat-audit rate C T2 GLMFiveThreeFlash, n |
| `\DetFlatGLMFiveThreeFlashCTTwoP` | n/a | flat-audit rate C T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveThreeFlashCTThree` | n/a | flat-audit rate C T3 GLMFiveThreeFlash [n/a: no data yet] |
| `\DetFlatGLMFiveThreeFlashCTThreeLo` | n/a | flat-audit rate C T3 GLMFiveThreeFlash, lower 95% CI bound |
| `\DetFlatGLMFiveThreeFlashCTThreeHi` | n/a | flat-audit rate C T3 GLMFiveThreeFlash, upper 95% CI bound |
| `\DetFlatGLMFiveThreeFlashCTThreeCI` | n/a | flat-audit rate C T3 GLMFiveThreeFlash, 95% CI |
| `\DetFlatGLMFiveThreeFlashCTThreeN` | n/a | flat-audit rate C T3 GLMFiveThreeFlash, n |
| `\DetFlatGLMFiveThreeFlashCTThreeP` | n/a | flat-audit rate C T3 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashCTZeroStrict` | n/a | within-store rank C T0 Strict GLMFiveThreeFlash [n/a: no data yet] |
| `\DetRankGLMFiveThreeFlashCTZeroStrictLo` | n/a | within-store rank C T0 Strict GLMFiveThreeFlash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTZeroStrictHi` | n/a | within-store rank C T0 Strict GLMFiveThreeFlash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTZeroStrictCI` | n/a | within-store rank C T0 Strict GLMFiveThreeFlash, 95% CI |
| `\DetRankGLMFiveThreeFlashCTZeroStrictN` | n/a | within-store rank C T0 Strict GLMFiveThreeFlash, n |
| `\DetRankGLMFiveThreeFlashCTZeroStrictP` | n/a | within-store rank C T0 Strict GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashCTZeroTiesIncl` | n/a | within-store rank C T0 TiesIncl GLMFiveThreeFlash [n/a: no data yet] |
| `\DetRankGLMFiveThreeFlashCTZeroTiesInclLo` | n/a | within-store rank C T0 TiesIncl GLMFiveThreeFlash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTZeroTiesInclHi` | n/a | within-store rank C T0 TiesIncl GLMFiveThreeFlash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTZeroTiesInclCI` | n/a | within-store rank C T0 TiesIncl GLMFiveThreeFlash, 95% CI |
| `\DetRankGLMFiveThreeFlashCTZeroTiesInclN` | n/a | within-store rank C T0 TiesIncl GLMFiveThreeFlash, n |
| `\DetRankGLMFiveThreeFlashCTZeroTiesInclP` | n/a | within-store rank C T0 TiesIncl GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashCTOneStrict` | n/a | within-store rank C T1 Strict GLMFiveThreeFlash [n/a: no data yet] |
| `\DetRankGLMFiveThreeFlashCTOneStrictLo` | n/a | within-store rank C T1 Strict GLMFiveThreeFlash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTOneStrictHi` | n/a | within-store rank C T1 Strict GLMFiveThreeFlash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTOneStrictCI` | n/a | within-store rank C T1 Strict GLMFiveThreeFlash, 95% CI |
| `\DetRankGLMFiveThreeFlashCTOneStrictN` | n/a | within-store rank C T1 Strict GLMFiveThreeFlash, n |
| `\DetRankGLMFiveThreeFlashCTOneStrictP` | n/a | within-store rank C T1 Strict GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashCTOneTiesIncl` | n/a | within-store rank C T1 TiesIncl GLMFiveThreeFlash [n/a: no data yet] |
| `\DetRankGLMFiveThreeFlashCTOneTiesInclLo` | n/a | within-store rank C T1 TiesIncl GLMFiveThreeFlash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTOneTiesInclHi` | n/a | within-store rank C T1 TiesIncl GLMFiveThreeFlash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTOneTiesInclCI` | n/a | within-store rank C T1 TiesIncl GLMFiveThreeFlash, 95% CI |
| `\DetRankGLMFiveThreeFlashCTOneTiesInclN` | n/a | within-store rank C T1 TiesIncl GLMFiveThreeFlash, n |
| `\DetRankGLMFiveThreeFlashCTOneTiesInclP` | n/a | within-store rank C T1 TiesIncl GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashCTTwoStrict` | n/a | within-store rank C T2 Strict GLMFiveThreeFlash [n/a: no data yet] |
| `\DetRankGLMFiveThreeFlashCTTwoStrictLo` | n/a | within-store rank C T2 Strict GLMFiveThreeFlash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTTwoStrictHi` | n/a | within-store rank C T2 Strict GLMFiveThreeFlash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTTwoStrictCI` | n/a | within-store rank C T2 Strict GLMFiveThreeFlash, 95% CI |
| `\DetRankGLMFiveThreeFlashCTTwoStrictN` | n/a | within-store rank C T2 Strict GLMFiveThreeFlash, n |
| `\DetRankGLMFiveThreeFlashCTTwoStrictP` | n/a | within-store rank C T2 Strict GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashCTTwoTiesIncl` | n/a | within-store rank C T2 TiesIncl GLMFiveThreeFlash [n/a: no data yet] |
| `\DetRankGLMFiveThreeFlashCTTwoTiesInclLo` | n/a | within-store rank C T2 TiesIncl GLMFiveThreeFlash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTTwoTiesInclHi` | n/a | within-store rank C T2 TiesIncl GLMFiveThreeFlash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTTwoTiesInclCI` | n/a | within-store rank C T2 TiesIncl GLMFiveThreeFlash, 95% CI |
| `\DetRankGLMFiveThreeFlashCTTwoTiesInclN` | n/a | within-store rank C T2 TiesIncl GLMFiveThreeFlash, n |
| `\DetRankGLMFiveThreeFlashCTTwoTiesInclP` | n/a | within-store rank C T2 TiesIncl GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashCTThreeStrict` | n/a | within-store rank C T3 Strict GLMFiveThreeFlash [n/a: no data yet] |
| `\DetRankGLMFiveThreeFlashCTThreeStrictLo` | n/a | within-store rank C T3 Strict GLMFiveThreeFlash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTThreeStrictHi` | n/a | within-store rank C T3 Strict GLMFiveThreeFlash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTThreeStrictCI` | n/a | within-store rank C T3 Strict GLMFiveThreeFlash, 95% CI |
| `\DetRankGLMFiveThreeFlashCTThreeStrictN` | n/a | within-store rank C T3 Strict GLMFiveThreeFlash, n |
| `\DetRankGLMFiveThreeFlashCTThreeStrictP` | n/a | within-store rank C T3 Strict GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashCTThreeTiesIncl` | n/a | within-store rank C T3 TiesIncl GLMFiveThreeFlash [n/a: no data yet] |
| `\DetRankGLMFiveThreeFlashCTThreeTiesInclLo` | n/a | within-store rank C T3 TiesIncl GLMFiveThreeFlash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTThreeTiesInclHi` | n/a | within-store rank C T3 TiesIncl GLMFiveThreeFlash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTThreeTiesInclCI` | n/a | within-store rank C T3 TiesIncl GLMFiveThreeFlash, 95% CI |
| `\DetRankGLMFiveThreeFlashCTThreeTiesInclN` | n/a | within-store rank C T3 TiesIncl GLMFiveThreeFlash, n |
| `\DetRankGLMFiveThreeFlashCTThreeTiesInclP` | n/a | within-store rank C T3 TiesIncl GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\DetRederivDisagreeGLMFiveTwo` | n/a | re-derivation disagreement rate for untouched notes, GLMFiveTwo [n/a: no data yet] |
| `\DetRederivDisagreeGLMFiveTwoLo` | n/a | re-derivation disagreement rate for untouched notes, GLMFiveTwo, lower 95% CI bound |
| `\DetRederivDisagreeGLMFiveTwoHi` | n/a | re-derivation disagreement rate for untouched notes, GLMFiveTwo, upper 95% CI bound |
| `\DetRederivDisagreeGLMFiveTwoCI` | n/a | re-derivation disagreement rate for untouched notes, GLMFiveTwo, 95% CI |
| `\DetRederivDisagreeGLMFiveTwoN` | n/a | re-derivation disagreement rate for untouched notes, GLMFiveTwo, n |
| `\DetRederivDisagreeGLMFiveTwoP` | n/a | re-derivation disagreement rate for untouched notes, GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveTwoVClean` | n/a | flat-audit rate V clean GLMFiveTwo [n/a: no data yet] |
| `\DetFlatGLMFiveTwoVCleanLo` | n/a | flat-audit rate V clean GLMFiveTwo, lower 95% CI bound |
| `\DetFlatGLMFiveTwoVCleanHi` | n/a | flat-audit rate V clean GLMFiveTwo, upper 95% CI bound |
| `\DetFlatGLMFiveTwoVCleanCI` | n/a | flat-audit rate V clean GLMFiveTwo, 95% CI |
| `\DetFlatGLMFiveTwoVCleanN` | n/a | flat-audit rate V clean GLMFiveTwo, n |
| `\DetFlatGLMFiveTwoVCleanP` | n/a | flat-audit rate V clean GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveTwoVTZero` | n/a | flat-audit rate V T0 GLMFiveTwo [n/a: no data yet] |
| `\DetFlatGLMFiveTwoVTZeroLo` | n/a | flat-audit rate V T0 GLMFiveTwo, lower 95% CI bound |
| `\DetFlatGLMFiveTwoVTZeroHi` | n/a | flat-audit rate V T0 GLMFiveTwo, upper 95% CI bound |
| `\DetFlatGLMFiveTwoVTZeroCI` | n/a | flat-audit rate V T0 GLMFiveTwo, 95% CI |
| `\DetFlatGLMFiveTwoVTZeroN` | n/a | flat-audit rate V T0 GLMFiveTwo, n |
| `\DetFlatGLMFiveTwoVTZeroP` | n/a | flat-audit rate V T0 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveTwoVTOne` | n/a | flat-audit rate V T1 GLMFiveTwo [n/a: no data yet] |
| `\DetFlatGLMFiveTwoVTOneLo` | n/a | flat-audit rate V T1 GLMFiveTwo, lower 95% CI bound |
| `\DetFlatGLMFiveTwoVTOneHi` | n/a | flat-audit rate V T1 GLMFiveTwo, upper 95% CI bound |
| `\DetFlatGLMFiveTwoVTOneCI` | n/a | flat-audit rate V T1 GLMFiveTwo, 95% CI |
| `\DetFlatGLMFiveTwoVTOneN` | n/a | flat-audit rate V T1 GLMFiveTwo, n |
| `\DetFlatGLMFiveTwoVTOneP` | n/a | flat-audit rate V T1 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveTwoVTTwo` | n/a | flat-audit rate V T2 GLMFiveTwo [n/a: no data yet] |
| `\DetFlatGLMFiveTwoVTTwoLo` | n/a | flat-audit rate V T2 GLMFiveTwo, lower 95% CI bound |
| `\DetFlatGLMFiveTwoVTTwoHi` | n/a | flat-audit rate V T2 GLMFiveTwo, upper 95% CI bound |
| `\DetFlatGLMFiveTwoVTTwoCI` | n/a | flat-audit rate V T2 GLMFiveTwo, 95% CI |
| `\DetFlatGLMFiveTwoVTTwoN` | n/a | flat-audit rate V T2 GLMFiveTwo, n |
| `\DetFlatGLMFiveTwoVTTwoP` | n/a | flat-audit rate V T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveTwoVTThree` | n/a | flat-audit rate V T3 GLMFiveTwo [n/a: no data yet] |
| `\DetFlatGLMFiveTwoVTThreeLo` | n/a | flat-audit rate V T3 GLMFiveTwo, lower 95% CI bound |
| `\DetFlatGLMFiveTwoVTThreeHi` | n/a | flat-audit rate V T3 GLMFiveTwo, upper 95% CI bound |
| `\DetFlatGLMFiveTwoVTThreeCI` | n/a | flat-audit rate V T3 GLMFiveTwo, 95% CI |
| `\DetFlatGLMFiveTwoVTThreeN` | n/a | flat-audit rate V T3 GLMFiveTwo, n |
| `\DetFlatGLMFiveTwoVTThreeP` | n/a | flat-audit rate V T3 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoVTZeroStrict` | n/a | within-store rank V T0 Strict GLMFiveTwo [n/a: no data yet] |
| `\DetRankGLMFiveTwoVTZeroStrictLo` | n/a | within-store rank V T0 Strict GLMFiveTwo, lower 95% CI bound |
| `\DetRankGLMFiveTwoVTZeroStrictHi` | n/a | within-store rank V T0 Strict GLMFiveTwo, upper 95% CI bound |
| `\DetRankGLMFiveTwoVTZeroStrictCI` | n/a | within-store rank V T0 Strict GLMFiveTwo, 95% CI |
| `\DetRankGLMFiveTwoVTZeroStrictN` | n/a | within-store rank V T0 Strict GLMFiveTwo, n |
| `\DetRankGLMFiveTwoVTZeroStrictP` | n/a | within-store rank V T0 Strict GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoVTZeroTiesIncl` | n/a | within-store rank V T0 TiesIncl GLMFiveTwo [n/a: no data yet] |
| `\DetRankGLMFiveTwoVTZeroTiesInclLo` | n/a | within-store rank V T0 TiesIncl GLMFiveTwo, lower 95% CI bound |
| `\DetRankGLMFiveTwoVTZeroTiesInclHi` | n/a | within-store rank V T0 TiesIncl GLMFiveTwo, upper 95% CI bound |
| `\DetRankGLMFiveTwoVTZeroTiesInclCI` | n/a | within-store rank V T0 TiesIncl GLMFiveTwo, 95% CI |
| `\DetRankGLMFiveTwoVTZeroTiesInclN` | n/a | within-store rank V T0 TiesIncl GLMFiveTwo, n |
| `\DetRankGLMFiveTwoVTZeroTiesInclP` | n/a | within-store rank V T0 TiesIncl GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoVTOneStrict` | n/a | within-store rank V T1 Strict GLMFiveTwo [n/a: no data yet] |
| `\DetRankGLMFiveTwoVTOneStrictLo` | n/a | within-store rank V T1 Strict GLMFiveTwo, lower 95% CI bound |
| `\DetRankGLMFiveTwoVTOneStrictHi` | n/a | within-store rank V T1 Strict GLMFiveTwo, upper 95% CI bound |
| `\DetRankGLMFiveTwoVTOneStrictCI` | n/a | within-store rank V T1 Strict GLMFiveTwo, 95% CI |
| `\DetRankGLMFiveTwoVTOneStrictN` | n/a | within-store rank V T1 Strict GLMFiveTwo, n |
| `\DetRankGLMFiveTwoVTOneStrictP` | n/a | within-store rank V T1 Strict GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoVTOneTiesIncl` | n/a | within-store rank V T1 TiesIncl GLMFiveTwo [n/a: no data yet] |
| `\DetRankGLMFiveTwoVTOneTiesInclLo` | n/a | within-store rank V T1 TiesIncl GLMFiveTwo, lower 95% CI bound |
| `\DetRankGLMFiveTwoVTOneTiesInclHi` | n/a | within-store rank V T1 TiesIncl GLMFiveTwo, upper 95% CI bound |
| `\DetRankGLMFiveTwoVTOneTiesInclCI` | n/a | within-store rank V T1 TiesIncl GLMFiveTwo, 95% CI |
| `\DetRankGLMFiveTwoVTOneTiesInclN` | n/a | within-store rank V T1 TiesIncl GLMFiveTwo, n |
| `\DetRankGLMFiveTwoVTOneTiesInclP` | n/a | within-store rank V T1 TiesIncl GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoVTTwoStrict` | n/a | within-store rank V T2 Strict GLMFiveTwo [n/a: no data yet] |
| `\DetRankGLMFiveTwoVTTwoStrictLo` | n/a | within-store rank V T2 Strict GLMFiveTwo, lower 95% CI bound |
| `\DetRankGLMFiveTwoVTTwoStrictHi` | n/a | within-store rank V T2 Strict GLMFiveTwo, upper 95% CI bound |
| `\DetRankGLMFiveTwoVTTwoStrictCI` | n/a | within-store rank V T2 Strict GLMFiveTwo, 95% CI |
| `\DetRankGLMFiveTwoVTTwoStrictN` | n/a | within-store rank V T2 Strict GLMFiveTwo, n |
| `\DetRankGLMFiveTwoVTTwoStrictP` | n/a | within-store rank V T2 Strict GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoVTTwoTiesIncl` | n/a | within-store rank V T2 TiesIncl GLMFiveTwo [n/a: no data yet] |
| `\DetRankGLMFiveTwoVTTwoTiesInclLo` | n/a | within-store rank V T2 TiesIncl GLMFiveTwo, lower 95% CI bound |
| `\DetRankGLMFiveTwoVTTwoTiesInclHi` | n/a | within-store rank V T2 TiesIncl GLMFiveTwo, upper 95% CI bound |
| `\DetRankGLMFiveTwoVTTwoTiesInclCI` | n/a | within-store rank V T2 TiesIncl GLMFiveTwo, 95% CI |
| `\DetRankGLMFiveTwoVTTwoTiesInclN` | n/a | within-store rank V T2 TiesIncl GLMFiveTwo, n |
| `\DetRankGLMFiveTwoVTTwoTiesInclP` | n/a | within-store rank V T2 TiesIncl GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoVTThreeStrict` | n/a | within-store rank V T3 Strict GLMFiveTwo [n/a: no data yet] |
| `\DetRankGLMFiveTwoVTThreeStrictLo` | n/a | within-store rank V T3 Strict GLMFiveTwo, lower 95% CI bound |
| `\DetRankGLMFiveTwoVTThreeStrictHi` | n/a | within-store rank V T3 Strict GLMFiveTwo, upper 95% CI bound |
| `\DetRankGLMFiveTwoVTThreeStrictCI` | n/a | within-store rank V T3 Strict GLMFiveTwo, 95% CI |
| `\DetRankGLMFiveTwoVTThreeStrictN` | n/a | within-store rank V T3 Strict GLMFiveTwo, n |
| `\DetRankGLMFiveTwoVTThreeStrictP` | n/a | within-store rank V T3 Strict GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoVTThreeTiesIncl` | n/a | within-store rank V T3 TiesIncl GLMFiveTwo [n/a: no data yet] |
| `\DetRankGLMFiveTwoVTThreeTiesInclLo` | n/a | within-store rank V T3 TiesIncl GLMFiveTwo, lower 95% CI bound |
| `\DetRankGLMFiveTwoVTThreeTiesInclHi` | n/a | within-store rank V T3 TiesIncl GLMFiveTwo, upper 95% CI bound |
| `\DetRankGLMFiveTwoVTThreeTiesInclCI` | n/a | within-store rank V T3 TiesIncl GLMFiveTwo, 95% CI |
| `\DetRankGLMFiveTwoVTThreeTiesInclN` | n/a | within-store rank V T3 TiesIncl GLMFiveTwo, n |
| `\DetRankGLMFiveTwoVTThreeTiesInclP` | n/a | within-store rank V T3 TiesIncl GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveTwoCClean` | n/a | flat-audit rate C clean GLMFiveTwo [n/a: no data yet] |
| `\DetFlatGLMFiveTwoCCleanLo` | n/a | flat-audit rate C clean GLMFiveTwo, lower 95% CI bound |
| `\DetFlatGLMFiveTwoCCleanHi` | n/a | flat-audit rate C clean GLMFiveTwo, upper 95% CI bound |
| `\DetFlatGLMFiveTwoCCleanCI` | n/a | flat-audit rate C clean GLMFiveTwo, 95% CI |
| `\DetFlatGLMFiveTwoCCleanN` | n/a | flat-audit rate C clean GLMFiveTwo, n |
| `\DetFlatGLMFiveTwoCCleanP` | n/a | flat-audit rate C clean GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveTwoCTZero` | n/a | flat-audit rate C T0 GLMFiveTwo [n/a: no data yet] |
| `\DetFlatGLMFiveTwoCTZeroLo` | n/a | flat-audit rate C T0 GLMFiveTwo, lower 95% CI bound |
| `\DetFlatGLMFiveTwoCTZeroHi` | n/a | flat-audit rate C T0 GLMFiveTwo, upper 95% CI bound |
| `\DetFlatGLMFiveTwoCTZeroCI` | n/a | flat-audit rate C T0 GLMFiveTwo, 95% CI |
| `\DetFlatGLMFiveTwoCTZeroN` | n/a | flat-audit rate C T0 GLMFiveTwo, n |
| `\DetFlatGLMFiveTwoCTZeroP` | n/a | flat-audit rate C T0 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveTwoCTOne` | n/a | flat-audit rate C T1 GLMFiveTwo [n/a: no data yet] |
| `\DetFlatGLMFiveTwoCTOneLo` | n/a | flat-audit rate C T1 GLMFiveTwo, lower 95% CI bound |
| `\DetFlatGLMFiveTwoCTOneHi` | n/a | flat-audit rate C T1 GLMFiveTwo, upper 95% CI bound |
| `\DetFlatGLMFiveTwoCTOneCI` | n/a | flat-audit rate C T1 GLMFiveTwo, 95% CI |
| `\DetFlatGLMFiveTwoCTOneN` | n/a | flat-audit rate C T1 GLMFiveTwo, n |
| `\DetFlatGLMFiveTwoCTOneP` | n/a | flat-audit rate C T1 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveTwoCTTwo` | n/a | flat-audit rate C T2 GLMFiveTwo [n/a: no data yet] |
| `\DetFlatGLMFiveTwoCTTwoLo` | n/a | flat-audit rate C T2 GLMFiveTwo, lower 95% CI bound |
| `\DetFlatGLMFiveTwoCTTwoHi` | n/a | flat-audit rate C T2 GLMFiveTwo, upper 95% CI bound |
| `\DetFlatGLMFiveTwoCTTwoCI` | n/a | flat-audit rate C T2 GLMFiveTwo, 95% CI |
| `\DetFlatGLMFiveTwoCTTwoN` | n/a | flat-audit rate C T2 GLMFiveTwo, n |
| `\DetFlatGLMFiveTwoCTTwoP` | n/a | flat-audit rate C T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveTwoCTThree` | n/a | flat-audit rate C T3 GLMFiveTwo [n/a: no data yet] |
| `\DetFlatGLMFiveTwoCTThreeLo` | n/a | flat-audit rate C T3 GLMFiveTwo, lower 95% CI bound |
| `\DetFlatGLMFiveTwoCTThreeHi` | n/a | flat-audit rate C T3 GLMFiveTwo, upper 95% CI bound |
| `\DetFlatGLMFiveTwoCTThreeCI` | n/a | flat-audit rate C T3 GLMFiveTwo, 95% CI |
| `\DetFlatGLMFiveTwoCTThreeN` | n/a | flat-audit rate C T3 GLMFiveTwo, n |
| `\DetFlatGLMFiveTwoCTThreeP` | n/a | flat-audit rate C T3 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoCTZeroStrict` | n/a | within-store rank C T0 Strict GLMFiveTwo [n/a: no data yet] |
| `\DetRankGLMFiveTwoCTZeroStrictLo` | n/a | within-store rank C T0 Strict GLMFiveTwo, lower 95% CI bound |
| `\DetRankGLMFiveTwoCTZeroStrictHi` | n/a | within-store rank C T0 Strict GLMFiveTwo, upper 95% CI bound |
| `\DetRankGLMFiveTwoCTZeroStrictCI` | n/a | within-store rank C T0 Strict GLMFiveTwo, 95% CI |
| `\DetRankGLMFiveTwoCTZeroStrictN` | n/a | within-store rank C T0 Strict GLMFiveTwo, n |
| `\DetRankGLMFiveTwoCTZeroStrictP` | n/a | within-store rank C T0 Strict GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoCTZeroTiesIncl` | n/a | within-store rank C T0 TiesIncl GLMFiveTwo [n/a: no data yet] |
| `\DetRankGLMFiveTwoCTZeroTiesInclLo` | n/a | within-store rank C T0 TiesIncl GLMFiveTwo, lower 95% CI bound |
| `\DetRankGLMFiveTwoCTZeroTiesInclHi` | n/a | within-store rank C T0 TiesIncl GLMFiveTwo, upper 95% CI bound |
| `\DetRankGLMFiveTwoCTZeroTiesInclCI` | n/a | within-store rank C T0 TiesIncl GLMFiveTwo, 95% CI |
| `\DetRankGLMFiveTwoCTZeroTiesInclN` | n/a | within-store rank C T0 TiesIncl GLMFiveTwo, n |
| `\DetRankGLMFiveTwoCTZeroTiesInclP` | n/a | within-store rank C T0 TiesIncl GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoCTOneStrict` | n/a | within-store rank C T1 Strict GLMFiveTwo [n/a: no data yet] |
| `\DetRankGLMFiveTwoCTOneStrictLo` | n/a | within-store rank C T1 Strict GLMFiveTwo, lower 95% CI bound |
| `\DetRankGLMFiveTwoCTOneStrictHi` | n/a | within-store rank C T1 Strict GLMFiveTwo, upper 95% CI bound |
| `\DetRankGLMFiveTwoCTOneStrictCI` | n/a | within-store rank C T1 Strict GLMFiveTwo, 95% CI |
| `\DetRankGLMFiveTwoCTOneStrictN` | n/a | within-store rank C T1 Strict GLMFiveTwo, n |
| `\DetRankGLMFiveTwoCTOneStrictP` | n/a | within-store rank C T1 Strict GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoCTOneTiesIncl` | n/a | within-store rank C T1 TiesIncl GLMFiveTwo [n/a: no data yet] |
| `\DetRankGLMFiveTwoCTOneTiesInclLo` | n/a | within-store rank C T1 TiesIncl GLMFiveTwo, lower 95% CI bound |
| `\DetRankGLMFiveTwoCTOneTiesInclHi` | n/a | within-store rank C T1 TiesIncl GLMFiveTwo, upper 95% CI bound |
| `\DetRankGLMFiveTwoCTOneTiesInclCI` | n/a | within-store rank C T1 TiesIncl GLMFiveTwo, 95% CI |
| `\DetRankGLMFiveTwoCTOneTiesInclN` | n/a | within-store rank C T1 TiesIncl GLMFiveTwo, n |
| `\DetRankGLMFiveTwoCTOneTiesInclP` | n/a | within-store rank C T1 TiesIncl GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoCTTwoStrict` | n/a | within-store rank C T2 Strict GLMFiveTwo [n/a: no data yet] |
| `\DetRankGLMFiveTwoCTTwoStrictLo` | n/a | within-store rank C T2 Strict GLMFiveTwo, lower 95% CI bound |
| `\DetRankGLMFiveTwoCTTwoStrictHi` | n/a | within-store rank C T2 Strict GLMFiveTwo, upper 95% CI bound |
| `\DetRankGLMFiveTwoCTTwoStrictCI` | n/a | within-store rank C T2 Strict GLMFiveTwo, 95% CI |
| `\DetRankGLMFiveTwoCTTwoStrictN` | n/a | within-store rank C T2 Strict GLMFiveTwo, n |
| `\DetRankGLMFiveTwoCTTwoStrictP` | n/a | within-store rank C T2 Strict GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoCTTwoTiesIncl` | n/a | within-store rank C T2 TiesIncl GLMFiveTwo [n/a: no data yet] |
| `\DetRankGLMFiveTwoCTTwoTiesInclLo` | n/a | within-store rank C T2 TiesIncl GLMFiveTwo, lower 95% CI bound |
| `\DetRankGLMFiveTwoCTTwoTiesInclHi` | n/a | within-store rank C T2 TiesIncl GLMFiveTwo, upper 95% CI bound |
| `\DetRankGLMFiveTwoCTTwoTiesInclCI` | n/a | within-store rank C T2 TiesIncl GLMFiveTwo, 95% CI |
| `\DetRankGLMFiveTwoCTTwoTiesInclN` | n/a | within-store rank C T2 TiesIncl GLMFiveTwo, n |
| `\DetRankGLMFiveTwoCTTwoTiesInclP` | n/a | within-store rank C T2 TiesIncl GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoCTThreeStrict` | n/a | within-store rank C T3 Strict GLMFiveTwo [n/a: no data yet] |
| `\DetRankGLMFiveTwoCTThreeStrictLo` | n/a | within-store rank C T3 Strict GLMFiveTwo, lower 95% CI bound |
| `\DetRankGLMFiveTwoCTThreeStrictHi` | n/a | within-store rank C T3 Strict GLMFiveTwo, upper 95% CI bound |
| `\DetRankGLMFiveTwoCTThreeStrictCI` | n/a | within-store rank C T3 Strict GLMFiveTwo, 95% CI |
| `\DetRankGLMFiveTwoCTThreeStrictN` | n/a | within-store rank C T3 Strict GLMFiveTwo, n |
| `\DetRankGLMFiveTwoCTThreeStrictP` | n/a | within-store rank C T3 Strict GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoCTThreeTiesIncl` | n/a | within-store rank C T3 TiesIncl GLMFiveTwo [n/a: no data yet] |
| `\DetRankGLMFiveTwoCTThreeTiesInclLo` | n/a | within-store rank C T3 TiesIncl GLMFiveTwo, lower 95% CI bound |
| `\DetRankGLMFiveTwoCTThreeTiesInclHi` | n/a | within-store rank C T3 TiesIncl GLMFiveTwo, upper 95% CI bound |
| `\DetRankGLMFiveTwoCTThreeTiesInclCI` | n/a | within-store rank C T3 TiesIncl GLMFiveTwo, 95% CI |
| `\DetRankGLMFiveTwoCTThreeTiesInclN` | n/a | within-store rank C T3 TiesIncl GLMFiveTwo, n |
| `\DetRankGLMFiveTwoCTThreeTiesInclP` | n/a | within-store rank C T3 TiesIncl GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PoneEscStale` | n/a | P1 % flags conflict, design stale [n/a: no data yet] |
| `\PoneEscStaleLo` | n/a | P1 % flags conflict, design stale, lower 95% CI bound |
| `\PoneEscStaleHi` | n/a | P1 % flags conflict, design stale, upper 95% CI bound |
| `\PoneEscStaleCI` | n/a | P1 % flags conflict, design stale, 95% CI |
| `\PoneEscStaleN` | n/a | P1 % flags conflict, design stale, n |
| `\PoneEscStaleP` | n/a | P1 % flags conflict, design stale, two-sided bootstrap p (n/a if not tested) |
| `\PoneConfStale` | n/a | P1 mean stated confidence, design stale [n/a: no data yet] |
| `\PoneConfStaleLo` | n/a | P1 mean stated confidence, design stale, lower 95% CI bound |
| `\PoneConfStaleHi` | n/a | P1 mean stated confidence, design stale, upper 95% CI bound |
| `\PoneConfStaleCI` | n/a | P1 mean stated confidence, design stale, 95% CI |
| `\PoneConfStaleN` | n/a | P1 mean stated confidence, design stale, n |
| `\PoneConfStaleP` | n/a | P1 mean stated confidence, design stale, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTZero` | n/a | detection V T0 qwen3.8-27b AUROC [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBVTZeroLo` | n/a | detection V T0 qwen3.8-27b AUROC, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTZeroHi` | n/a | detection V T0 qwen3.8-27b AUROC, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTZeroCI` | n/a | detection V T0 qwen3.8-27b AUROC, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTZeroN` | n/a | detection V T0 qwen3.8-27b AUROC, n |
| `\DetQwenThreeEightTwoSevenBVTZeroP` | n/a | detection V T0 qwen3.8-27b AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTZeroTprOne` | n/a | detection V T0 qwen3.8-27b TprOne [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBVTZeroTprOneLo` | n/a | detection V T0 qwen3.8-27b TprOne, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTZeroTprOneHi` | n/a | detection V T0 qwen3.8-27b TprOne, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTZeroTprOneCI` | n/a | detection V T0 qwen3.8-27b TprOne, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTZeroTprOneN` | n/a | detection V T0 qwen3.8-27b TprOne, n |
| `\DetQwenThreeEightTwoSevenBVTZeroTprOneP` | n/a | detection V T0 qwen3.8-27b TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTZeroTprFive` | n/a | detection V T0 qwen3.8-27b TprFive [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBVTZeroTprFiveLo` | n/a | detection V T0 qwen3.8-27b TprFive, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTZeroTprFiveHi` | n/a | detection V T0 qwen3.8-27b TprFive, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTZeroTprFiveCI` | n/a | detection V T0 qwen3.8-27b TprFive, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTZeroTprFiveN` | n/a | detection V T0 qwen3.8-27b TprFive, n |
| `\DetQwenThreeEightTwoSevenBVTZeroTprFiveP` | n/a | detection V T0 qwen3.8-27b TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTZero` | n/a | detection V T0 glm-5.3-flash AUROC [n/a: no data yet] |
| `\DetGLMFiveThreeFlashVTZeroLo` | n/a | detection V T0 glm-5.3-flash AUROC, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTZeroHi` | n/a | detection V T0 glm-5.3-flash AUROC, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTZeroCI` | n/a | detection V T0 glm-5.3-flash AUROC, 95% CI |
| `\DetGLMFiveThreeFlashVTZeroN` | n/a | detection V T0 glm-5.3-flash AUROC, n |
| `\DetGLMFiveThreeFlashVTZeroP` | n/a | detection V T0 glm-5.3-flash AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTZeroTprOne` | n/a | detection V T0 glm-5.3-flash TprOne [n/a: no data yet] |
| `\DetGLMFiveThreeFlashVTZeroTprOneLo` | n/a | detection V T0 glm-5.3-flash TprOne, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTZeroTprOneHi` | n/a | detection V T0 glm-5.3-flash TprOne, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTZeroTprOneCI` | n/a | detection V T0 glm-5.3-flash TprOne, 95% CI |
| `\DetGLMFiveThreeFlashVTZeroTprOneN` | n/a | detection V T0 glm-5.3-flash TprOne, n |
| `\DetGLMFiveThreeFlashVTZeroTprOneP` | n/a | detection V T0 glm-5.3-flash TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTZeroTprFive` | n/a | detection V T0 glm-5.3-flash TprFive [n/a: no data yet] |
| `\DetGLMFiveThreeFlashVTZeroTprFiveLo` | n/a | detection V T0 glm-5.3-flash TprFive, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTZeroTprFiveHi` | n/a | detection V T0 glm-5.3-flash TprFive, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTZeroTprFiveCI` | n/a | detection V T0 glm-5.3-flash TprFive, 95% CI |
| `\DetGLMFiveThreeFlashVTZeroTprFiveN` | n/a | detection V T0 glm-5.3-flash TprFive, n |
| `\DetGLMFiveThreeFlashVTZeroTprFiveP` | n/a | detection V T0 glm-5.3-flash TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTZero` | n/a | detection V T0 glm-5.2 AUROC [n/a: no data yet] |
| `\DetGLMFiveTwoVTZeroLo` | n/a | detection V T0 glm-5.2 AUROC, lower 95% CI bound |
| `\DetGLMFiveTwoVTZeroHi` | n/a | detection V T0 glm-5.2 AUROC, upper 95% CI bound |
| `\DetGLMFiveTwoVTZeroCI` | n/a | detection V T0 glm-5.2 AUROC, 95% CI |
| `\DetGLMFiveTwoVTZeroN` | n/a | detection V T0 glm-5.2 AUROC, n |
| `\DetGLMFiveTwoVTZeroP` | n/a | detection V T0 glm-5.2 AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTZeroTprOne` | n/a | detection V T0 glm-5.2 TprOne [n/a: no data yet] |
| `\DetGLMFiveTwoVTZeroTprOneLo` | n/a | detection V T0 glm-5.2 TprOne, lower 95% CI bound |
| `\DetGLMFiveTwoVTZeroTprOneHi` | n/a | detection V T0 glm-5.2 TprOne, upper 95% CI bound |
| `\DetGLMFiveTwoVTZeroTprOneCI` | n/a | detection V T0 glm-5.2 TprOne, 95% CI |
| `\DetGLMFiveTwoVTZeroTprOneN` | n/a | detection V T0 glm-5.2 TprOne, n |
| `\DetGLMFiveTwoVTZeroTprOneP` | n/a | detection V T0 glm-5.2 TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTZeroTprFive` | n/a | detection V T0 glm-5.2 TprFive [n/a: no data yet] |
| `\DetGLMFiveTwoVTZeroTprFiveLo` | n/a | detection V T0 glm-5.2 TprFive, lower 95% CI bound |
| `\DetGLMFiveTwoVTZeroTprFiveHi` | n/a | detection V T0 glm-5.2 TprFive, upper 95% CI bound |
| `\DetGLMFiveTwoVTZeroTprFiveCI` | n/a | detection V T0 glm-5.2 TprFive, 95% CI |
| `\DetGLMFiveTwoVTZeroTprFiveN` | n/a | detection V T0 glm-5.2 TprFive, n |
| `\DetGLMFiveTwoVTZeroTprFiveP` | n/a | detection V T0 glm-5.2 TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTOne` | n/a | detection V T1 qwen3.8-27b AUROC [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBVTOneLo` | n/a | detection V T1 qwen3.8-27b AUROC, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTOneHi` | n/a | detection V T1 qwen3.8-27b AUROC, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTOneCI` | n/a | detection V T1 qwen3.8-27b AUROC, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTOneN` | n/a | detection V T1 qwen3.8-27b AUROC, n |
| `\DetQwenThreeEightTwoSevenBVTOneP` | n/a | detection V T1 qwen3.8-27b AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTOneTprOne` | n/a | detection V T1 qwen3.8-27b TprOne [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBVTOneTprOneLo` | n/a | detection V T1 qwen3.8-27b TprOne, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTOneTprOneHi` | n/a | detection V T1 qwen3.8-27b TprOne, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTOneTprOneCI` | n/a | detection V T1 qwen3.8-27b TprOne, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTOneTprOneN` | n/a | detection V T1 qwen3.8-27b TprOne, n |
| `\DetQwenThreeEightTwoSevenBVTOneTprOneP` | n/a | detection V T1 qwen3.8-27b TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTOneTprFive` | n/a | detection V T1 qwen3.8-27b TprFive [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBVTOneTprFiveLo` | n/a | detection V T1 qwen3.8-27b TprFive, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTOneTprFiveHi` | n/a | detection V T1 qwen3.8-27b TprFive, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTOneTprFiveCI` | n/a | detection V T1 qwen3.8-27b TprFive, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTOneTprFiveN` | n/a | detection V T1 qwen3.8-27b TprFive, n |
| `\DetQwenThreeEightTwoSevenBVTOneTprFiveP` | n/a | detection V T1 qwen3.8-27b TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTOne` | n/a | detection V T1 glm-5.3-flash AUROC [n/a: no data yet] |
| `\DetGLMFiveThreeFlashVTOneLo` | n/a | detection V T1 glm-5.3-flash AUROC, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTOneHi` | n/a | detection V T1 glm-5.3-flash AUROC, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTOneCI` | n/a | detection V T1 glm-5.3-flash AUROC, 95% CI |
| `\DetGLMFiveThreeFlashVTOneN` | n/a | detection V T1 glm-5.3-flash AUROC, n |
| `\DetGLMFiveThreeFlashVTOneP` | n/a | detection V T1 glm-5.3-flash AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTOneTprOne` | n/a | detection V T1 glm-5.3-flash TprOne [n/a: no data yet] |
| `\DetGLMFiveThreeFlashVTOneTprOneLo` | n/a | detection V T1 glm-5.3-flash TprOne, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTOneTprOneHi` | n/a | detection V T1 glm-5.3-flash TprOne, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTOneTprOneCI` | n/a | detection V T1 glm-5.3-flash TprOne, 95% CI |
| `\DetGLMFiveThreeFlashVTOneTprOneN` | n/a | detection V T1 glm-5.3-flash TprOne, n |
| `\DetGLMFiveThreeFlashVTOneTprOneP` | n/a | detection V T1 glm-5.3-flash TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTOneTprFive` | n/a | detection V T1 glm-5.3-flash TprFive [n/a: no data yet] |
| `\DetGLMFiveThreeFlashVTOneTprFiveLo` | n/a | detection V T1 glm-5.3-flash TprFive, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTOneTprFiveHi` | n/a | detection V T1 glm-5.3-flash TprFive, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTOneTprFiveCI` | n/a | detection V T1 glm-5.3-flash TprFive, 95% CI |
| `\DetGLMFiveThreeFlashVTOneTprFiveN` | n/a | detection V T1 glm-5.3-flash TprFive, n |
| `\DetGLMFiveThreeFlashVTOneTprFiveP` | n/a | detection V T1 glm-5.3-flash TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTOne` | n/a | detection V T1 glm-5.2 AUROC [n/a: no data yet] |
| `\DetGLMFiveTwoVTOneLo` | n/a | detection V T1 glm-5.2 AUROC, lower 95% CI bound |
| `\DetGLMFiveTwoVTOneHi` | n/a | detection V T1 glm-5.2 AUROC, upper 95% CI bound |
| `\DetGLMFiveTwoVTOneCI` | n/a | detection V T1 glm-5.2 AUROC, 95% CI |
| `\DetGLMFiveTwoVTOneN` | n/a | detection V T1 glm-5.2 AUROC, n |
| `\DetGLMFiveTwoVTOneP` | n/a | detection V T1 glm-5.2 AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTOneTprOne` | n/a | detection V T1 glm-5.2 TprOne [n/a: no data yet] |
| `\DetGLMFiveTwoVTOneTprOneLo` | n/a | detection V T1 glm-5.2 TprOne, lower 95% CI bound |
| `\DetGLMFiveTwoVTOneTprOneHi` | n/a | detection V T1 glm-5.2 TprOne, upper 95% CI bound |
| `\DetGLMFiveTwoVTOneTprOneCI` | n/a | detection V T1 glm-5.2 TprOne, 95% CI |
| `\DetGLMFiveTwoVTOneTprOneN` | n/a | detection V T1 glm-5.2 TprOne, n |
| `\DetGLMFiveTwoVTOneTprOneP` | n/a | detection V T1 glm-5.2 TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTOneTprFive` | n/a | detection V T1 glm-5.2 TprFive [n/a: no data yet] |
| `\DetGLMFiveTwoVTOneTprFiveLo` | n/a | detection V T1 glm-5.2 TprFive, lower 95% CI bound |
| `\DetGLMFiveTwoVTOneTprFiveHi` | n/a | detection V T1 glm-5.2 TprFive, upper 95% CI bound |
| `\DetGLMFiveTwoVTOneTprFiveCI` | n/a | detection V T1 glm-5.2 TprFive, 95% CI |
| `\DetGLMFiveTwoVTOneTprFiveN` | n/a | detection V T1 glm-5.2 TprFive, n |
| `\DetGLMFiveTwoVTOneTprFiveP` | n/a | detection V T1 glm-5.2 TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTTwo` | n/a | detection V T2 qwen3.8-27b AUROC [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBVTTwoLo` | n/a | detection V T2 qwen3.8-27b AUROC, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTTwoHi` | n/a | detection V T2 qwen3.8-27b AUROC, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTTwoCI` | n/a | detection V T2 qwen3.8-27b AUROC, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTTwoN` | n/a | detection V T2 qwen3.8-27b AUROC, n |
| `\DetQwenThreeEightTwoSevenBVTTwoP` | n/a | detection V T2 qwen3.8-27b AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTTwoTprOne` | n/a | detection V T2 qwen3.8-27b TprOne [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBVTTwoTprOneLo` | n/a | detection V T2 qwen3.8-27b TprOne, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTTwoTprOneHi` | n/a | detection V T2 qwen3.8-27b TprOne, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTTwoTprOneCI` | n/a | detection V T2 qwen3.8-27b TprOne, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTTwoTprOneN` | n/a | detection V T2 qwen3.8-27b TprOne, n |
| `\DetQwenThreeEightTwoSevenBVTTwoTprOneP` | n/a | detection V T2 qwen3.8-27b TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTTwoTprFive` | n/a | detection V T2 qwen3.8-27b TprFive [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBVTTwoTprFiveLo` | n/a | detection V T2 qwen3.8-27b TprFive, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTTwoTprFiveHi` | n/a | detection V T2 qwen3.8-27b TprFive, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTTwoTprFiveCI` | n/a | detection V T2 qwen3.8-27b TprFive, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTTwoTprFiveN` | n/a | detection V T2 qwen3.8-27b TprFive, n |
| `\DetQwenThreeEightTwoSevenBVTTwoTprFiveP` | n/a | detection V T2 qwen3.8-27b TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTTwo` | n/a | detection V T2 glm-5.3-flash AUROC [n/a: no data yet] |
| `\DetGLMFiveThreeFlashVTTwoLo` | n/a | detection V T2 glm-5.3-flash AUROC, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTTwoHi` | n/a | detection V T2 glm-5.3-flash AUROC, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTTwoCI` | n/a | detection V T2 glm-5.3-flash AUROC, 95% CI |
| `\DetGLMFiveThreeFlashVTTwoN` | n/a | detection V T2 glm-5.3-flash AUROC, n |
| `\DetGLMFiveThreeFlashVTTwoP` | n/a | detection V T2 glm-5.3-flash AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTTwoTprOne` | n/a | detection V T2 glm-5.3-flash TprOne [n/a: no data yet] |
| `\DetGLMFiveThreeFlashVTTwoTprOneLo` | n/a | detection V T2 glm-5.3-flash TprOne, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTTwoTprOneHi` | n/a | detection V T2 glm-5.3-flash TprOne, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTTwoTprOneCI` | n/a | detection V T2 glm-5.3-flash TprOne, 95% CI |
| `\DetGLMFiveThreeFlashVTTwoTprOneN` | n/a | detection V T2 glm-5.3-flash TprOne, n |
| `\DetGLMFiveThreeFlashVTTwoTprOneP` | n/a | detection V T2 glm-5.3-flash TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTTwoTprFive` | n/a | detection V T2 glm-5.3-flash TprFive [n/a: no data yet] |
| `\DetGLMFiveThreeFlashVTTwoTprFiveLo` | n/a | detection V T2 glm-5.3-flash TprFive, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTTwoTprFiveHi` | n/a | detection V T2 glm-5.3-flash TprFive, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTTwoTprFiveCI` | n/a | detection V T2 glm-5.3-flash TprFive, 95% CI |
| `\DetGLMFiveThreeFlashVTTwoTprFiveN` | n/a | detection V T2 glm-5.3-flash TprFive, n |
| `\DetGLMFiveThreeFlashVTTwoTprFiveP` | n/a | detection V T2 glm-5.3-flash TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTTwo` | n/a | detection V T2 glm-5.2 AUROC [n/a: no data yet] |
| `\DetGLMFiveTwoVTTwoLo` | n/a | detection V T2 glm-5.2 AUROC, lower 95% CI bound |
| `\DetGLMFiveTwoVTTwoHi` | n/a | detection V T2 glm-5.2 AUROC, upper 95% CI bound |
| `\DetGLMFiveTwoVTTwoCI` | n/a | detection V T2 glm-5.2 AUROC, 95% CI |
| `\DetGLMFiveTwoVTTwoN` | n/a | detection V T2 glm-5.2 AUROC, n |
| `\DetGLMFiveTwoVTTwoP` | n/a | detection V T2 glm-5.2 AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTTwoTprOne` | n/a | detection V T2 glm-5.2 TprOne [n/a: no data yet] |
| `\DetGLMFiveTwoVTTwoTprOneLo` | n/a | detection V T2 glm-5.2 TprOne, lower 95% CI bound |
| `\DetGLMFiveTwoVTTwoTprOneHi` | n/a | detection V T2 glm-5.2 TprOne, upper 95% CI bound |
| `\DetGLMFiveTwoVTTwoTprOneCI` | n/a | detection V T2 glm-5.2 TprOne, 95% CI |
| `\DetGLMFiveTwoVTTwoTprOneN` | n/a | detection V T2 glm-5.2 TprOne, n |
| `\DetGLMFiveTwoVTTwoTprOneP` | n/a | detection V T2 glm-5.2 TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTTwoTprFive` | n/a | detection V T2 glm-5.2 TprFive [n/a: no data yet] |
| `\DetGLMFiveTwoVTTwoTprFiveLo` | n/a | detection V T2 glm-5.2 TprFive, lower 95% CI bound |
| `\DetGLMFiveTwoVTTwoTprFiveHi` | n/a | detection V T2 glm-5.2 TprFive, upper 95% CI bound |
| `\DetGLMFiveTwoVTTwoTprFiveCI` | n/a | detection V T2 glm-5.2 TprFive, 95% CI |
| `\DetGLMFiveTwoVTTwoTprFiveN` | n/a | detection V T2 glm-5.2 TprFive, n |
| `\DetGLMFiveTwoVTTwoTprFiveP` | n/a | detection V T2 glm-5.2 TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTThree` | n/a | detection V T3 qwen3.8-27b AUROC [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBVTThreeLo` | n/a | detection V T3 qwen3.8-27b AUROC, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTThreeHi` | n/a | detection V T3 qwen3.8-27b AUROC, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTThreeCI` | n/a | detection V T3 qwen3.8-27b AUROC, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTThreeN` | n/a | detection V T3 qwen3.8-27b AUROC, n |
| `\DetQwenThreeEightTwoSevenBVTThreeP` | n/a | detection V T3 qwen3.8-27b AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTThreeTprOne` | n/a | detection V T3 qwen3.8-27b TprOne [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBVTThreeTprOneLo` | n/a | detection V T3 qwen3.8-27b TprOne, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTThreeTprOneHi` | n/a | detection V T3 qwen3.8-27b TprOne, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTThreeTprOneCI` | n/a | detection V T3 qwen3.8-27b TprOne, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTThreeTprOneN` | n/a | detection V T3 qwen3.8-27b TprOne, n |
| `\DetQwenThreeEightTwoSevenBVTThreeTprOneP` | n/a | detection V T3 qwen3.8-27b TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTThreeTprFive` | n/a | detection V T3 qwen3.8-27b TprFive [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBVTThreeTprFiveLo` | n/a | detection V T3 qwen3.8-27b TprFive, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTThreeTprFiveHi` | n/a | detection V T3 qwen3.8-27b TprFive, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTThreeTprFiveCI` | n/a | detection V T3 qwen3.8-27b TprFive, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTThreeTprFiveN` | n/a | detection V T3 qwen3.8-27b TprFive, n |
| `\DetQwenThreeEightTwoSevenBVTThreeTprFiveP` | n/a | detection V T3 qwen3.8-27b TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTThree` | n/a | detection V T3 glm-5.3-flash AUROC [n/a: no data yet] |
| `\DetGLMFiveThreeFlashVTThreeLo` | n/a | detection V T3 glm-5.3-flash AUROC, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTThreeHi` | n/a | detection V T3 glm-5.3-flash AUROC, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTThreeCI` | n/a | detection V T3 glm-5.3-flash AUROC, 95% CI |
| `\DetGLMFiveThreeFlashVTThreeN` | n/a | detection V T3 glm-5.3-flash AUROC, n |
| `\DetGLMFiveThreeFlashVTThreeP` | n/a | detection V T3 glm-5.3-flash AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTThreeTprOne` | n/a | detection V T3 glm-5.3-flash TprOne [n/a: no data yet] |
| `\DetGLMFiveThreeFlashVTThreeTprOneLo` | n/a | detection V T3 glm-5.3-flash TprOne, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTThreeTprOneHi` | n/a | detection V T3 glm-5.3-flash TprOne, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTThreeTprOneCI` | n/a | detection V T3 glm-5.3-flash TprOne, 95% CI |
| `\DetGLMFiveThreeFlashVTThreeTprOneN` | n/a | detection V T3 glm-5.3-flash TprOne, n |
| `\DetGLMFiveThreeFlashVTThreeTprOneP` | n/a | detection V T3 glm-5.3-flash TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTThreeTprFive` | n/a | detection V T3 glm-5.3-flash TprFive [n/a: no data yet] |
| `\DetGLMFiveThreeFlashVTThreeTprFiveLo` | n/a | detection V T3 glm-5.3-flash TprFive, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTThreeTprFiveHi` | n/a | detection V T3 glm-5.3-flash TprFive, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTThreeTprFiveCI` | n/a | detection V T3 glm-5.3-flash TprFive, 95% CI |
| `\DetGLMFiveThreeFlashVTThreeTprFiveN` | n/a | detection V T3 glm-5.3-flash TprFive, n |
| `\DetGLMFiveThreeFlashVTThreeTprFiveP` | n/a | detection V T3 glm-5.3-flash TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTThree` | n/a | detection V T3 glm-5.2 AUROC [n/a: no data yet] |
| `\DetGLMFiveTwoVTThreeLo` | n/a | detection V T3 glm-5.2 AUROC, lower 95% CI bound |
| `\DetGLMFiveTwoVTThreeHi` | n/a | detection V T3 glm-5.2 AUROC, upper 95% CI bound |
| `\DetGLMFiveTwoVTThreeCI` | n/a | detection V T3 glm-5.2 AUROC, 95% CI |
| `\DetGLMFiveTwoVTThreeN` | n/a | detection V T3 glm-5.2 AUROC, n |
| `\DetGLMFiveTwoVTThreeP` | n/a | detection V T3 glm-5.2 AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTThreeTprOne` | n/a | detection V T3 glm-5.2 TprOne [n/a: no data yet] |
| `\DetGLMFiveTwoVTThreeTprOneLo` | n/a | detection V T3 glm-5.2 TprOne, lower 95% CI bound |
| `\DetGLMFiveTwoVTThreeTprOneHi` | n/a | detection V T3 glm-5.2 TprOne, upper 95% CI bound |
| `\DetGLMFiveTwoVTThreeTprOneCI` | n/a | detection V T3 glm-5.2 TprOne, 95% CI |
| `\DetGLMFiveTwoVTThreeTprOneN` | n/a | detection V T3 glm-5.2 TprOne, n |
| `\DetGLMFiveTwoVTThreeTprOneP` | n/a | detection V T3 glm-5.2 TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTThreeTprFive` | n/a | detection V T3 glm-5.2 TprFive [n/a: no data yet] |
| `\DetGLMFiveTwoVTThreeTprFiveLo` | n/a | detection V T3 glm-5.2 TprFive, lower 95% CI bound |
| `\DetGLMFiveTwoVTThreeTprFiveHi` | n/a | detection V T3 glm-5.2 TprFive, upper 95% CI bound |
| `\DetGLMFiveTwoVTThreeTprFiveCI` | n/a | detection V T3 glm-5.2 TprFive, 95% CI |
| `\DetGLMFiveTwoVTThreeTprFiveN` | n/a | detection V T3 glm-5.2 TprFive, n |
| `\DetGLMFiveTwoVTThreeTprFiveP` | n/a | detection V T3 glm-5.2 TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTZero` | n/a | detection C T0 qwen3.8-27b AUROC [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBCTZeroLo` | n/a | detection C T0 qwen3.8-27b AUROC, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTZeroHi` | n/a | detection C T0 qwen3.8-27b AUROC, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTZeroCI` | n/a | detection C T0 qwen3.8-27b AUROC, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTZeroN` | n/a | detection C T0 qwen3.8-27b AUROC, n |
| `\DetQwenThreeEightTwoSevenBCTZeroP` | n/a | detection C T0 qwen3.8-27b AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTZeroTprOne` | n/a | detection C T0 qwen3.8-27b TprOne [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBCTZeroTprOneLo` | n/a | detection C T0 qwen3.8-27b TprOne, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTZeroTprOneHi` | n/a | detection C T0 qwen3.8-27b TprOne, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTZeroTprOneCI` | n/a | detection C T0 qwen3.8-27b TprOne, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTZeroTprOneN` | n/a | detection C T0 qwen3.8-27b TprOne, n |
| `\DetQwenThreeEightTwoSevenBCTZeroTprOneP` | n/a | detection C T0 qwen3.8-27b TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTZeroTprFive` | n/a | detection C T0 qwen3.8-27b TprFive [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBCTZeroTprFiveLo` | n/a | detection C T0 qwen3.8-27b TprFive, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTZeroTprFiveHi` | n/a | detection C T0 qwen3.8-27b TprFive, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTZeroTprFiveCI` | n/a | detection C T0 qwen3.8-27b TprFive, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTZeroTprFiveN` | n/a | detection C T0 qwen3.8-27b TprFive, n |
| `\DetQwenThreeEightTwoSevenBCTZeroTprFiveP` | n/a | detection C T0 qwen3.8-27b TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTZero` | n/a | detection C T0 glm-5.3-flash AUROC [n/a: no data yet] |
| `\DetGLMFiveThreeFlashCTZeroLo` | n/a | detection C T0 glm-5.3-flash AUROC, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTZeroHi` | n/a | detection C T0 glm-5.3-flash AUROC, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTZeroCI` | n/a | detection C T0 glm-5.3-flash AUROC, 95% CI |
| `\DetGLMFiveThreeFlashCTZeroN` | n/a | detection C T0 glm-5.3-flash AUROC, n |
| `\DetGLMFiveThreeFlashCTZeroP` | n/a | detection C T0 glm-5.3-flash AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTZeroTprOne` | n/a | detection C T0 glm-5.3-flash TprOne [n/a: no data yet] |
| `\DetGLMFiveThreeFlashCTZeroTprOneLo` | n/a | detection C T0 glm-5.3-flash TprOne, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTZeroTprOneHi` | n/a | detection C T0 glm-5.3-flash TprOne, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTZeroTprOneCI` | n/a | detection C T0 glm-5.3-flash TprOne, 95% CI |
| `\DetGLMFiveThreeFlashCTZeroTprOneN` | n/a | detection C T0 glm-5.3-flash TprOne, n |
| `\DetGLMFiveThreeFlashCTZeroTprOneP` | n/a | detection C T0 glm-5.3-flash TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTZeroTprFive` | n/a | detection C T0 glm-5.3-flash TprFive [n/a: no data yet] |
| `\DetGLMFiveThreeFlashCTZeroTprFiveLo` | n/a | detection C T0 glm-5.3-flash TprFive, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTZeroTprFiveHi` | n/a | detection C T0 glm-5.3-flash TprFive, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTZeroTprFiveCI` | n/a | detection C T0 glm-5.3-flash TprFive, 95% CI |
| `\DetGLMFiveThreeFlashCTZeroTprFiveN` | n/a | detection C T0 glm-5.3-flash TprFive, n |
| `\DetGLMFiveThreeFlashCTZeroTprFiveP` | n/a | detection C T0 glm-5.3-flash TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTZero` | n/a | detection C T0 glm-5.2 AUROC [n/a: no data yet] |
| `\DetGLMFiveTwoCTZeroLo` | n/a | detection C T0 glm-5.2 AUROC, lower 95% CI bound |
| `\DetGLMFiveTwoCTZeroHi` | n/a | detection C T0 glm-5.2 AUROC, upper 95% CI bound |
| `\DetGLMFiveTwoCTZeroCI` | n/a | detection C T0 glm-5.2 AUROC, 95% CI |
| `\DetGLMFiveTwoCTZeroN` | n/a | detection C T0 glm-5.2 AUROC, n |
| `\DetGLMFiveTwoCTZeroP` | n/a | detection C T0 glm-5.2 AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTZeroTprOne` | n/a | detection C T0 glm-5.2 TprOne [n/a: no data yet] |
| `\DetGLMFiveTwoCTZeroTprOneLo` | n/a | detection C T0 glm-5.2 TprOne, lower 95% CI bound |
| `\DetGLMFiveTwoCTZeroTprOneHi` | n/a | detection C T0 glm-5.2 TprOne, upper 95% CI bound |
| `\DetGLMFiveTwoCTZeroTprOneCI` | n/a | detection C T0 glm-5.2 TprOne, 95% CI |
| `\DetGLMFiveTwoCTZeroTprOneN` | n/a | detection C T0 glm-5.2 TprOne, n |
| `\DetGLMFiveTwoCTZeroTprOneP` | n/a | detection C T0 glm-5.2 TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTZeroTprFive` | n/a | detection C T0 glm-5.2 TprFive [n/a: no data yet] |
| `\DetGLMFiveTwoCTZeroTprFiveLo` | n/a | detection C T0 glm-5.2 TprFive, lower 95% CI bound |
| `\DetGLMFiveTwoCTZeroTprFiveHi` | n/a | detection C T0 glm-5.2 TprFive, upper 95% CI bound |
| `\DetGLMFiveTwoCTZeroTprFiveCI` | n/a | detection C T0 glm-5.2 TprFive, 95% CI |
| `\DetGLMFiveTwoCTZeroTprFiveN` | n/a | detection C T0 glm-5.2 TprFive, n |
| `\DetGLMFiveTwoCTZeroTprFiveP` | n/a | detection C T0 glm-5.2 TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTOne` | n/a | detection C T1 qwen3.8-27b AUROC [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBCTOneLo` | n/a | detection C T1 qwen3.8-27b AUROC, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTOneHi` | n/a | detection C T1 qwen3.8-27b AUROC, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTOneCI` | n/a | detection C T1 qwen3.8-27b AUROC, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTOneN` | n/a | detection C T1 qwen3.8-27b AUROC, n |
| `\DetQwenThreeEightTwoSevenBCTOneP` | n/a | detection C T1 qwen3.8-27b AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTOneTprOne` | n/a | detection C T1 qwen3.8-27b TprOne [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBCTOneTprOneLo` | n/a | detection C T1 qwen3.8-27b TprOne, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTOneTprOneHi` | n/a | detection C T1 qwen3.8-27b TprOne, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTOneTprOneCI` | n/a | detection C T1 qwen3.8-27b TprOne, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTOneTprOneN` | n/a | detection C T1 qwen3.8-27b TprOne, n |
| `\DetQwenThreeEightTwoSevenBCTOneTprOneP` | n/a | detection C T1 qwen3.8-27b TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTOneTprFive` | n/a | detection C T1 qwen3.8-27b TprFive [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBCTOneTprFiveLo` | n/a | detection C T1 qwen3.8-27b TprFive, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTOneTprFiveHi` | n/a | detection C T1 qwen3.8-27b TprFive, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTOneTprFiveCI` | n/a | detection C T1 qwen3.8-27b TprFive, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTOneTprFiveN` | n/a | detection C T1 qwen3.8-27b TprFive, n |
| `\DetQwenThreeEightTwoSevenBCTOneTprFiveP` | n/a | detection C T1 qwen3.8-27b TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTOne` | n/a | detection C T1 glm-5.3-flash AUROC [n/a: no data yet] |
| `\DetGLMFiveThreeFlashCTOneLo` | n/a | detection C T1 glm-5.3-flash AUROC, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTOneHi` | n/a | detection C T1 glm-5.3-flash AUROC, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTOneCI` | n/a | detection C T1 glm-5.3-flash AUROC, 95% CI |
| `\DetGLMFiveThreeFlashCTOneN` | n/a | detection C T1 glm-5.3-flash AUROC, n |
| `\DetGLMFiveThreeFlashCTOneP` | n/a | detection C T1 glm-5.3-flash AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTOneTprOne` | n/a | detection C T1 glm-5.3-flash TprOne [n/a: no data yet] |
| `\DetGLMFiveThreeFlashCTOneTprOneLo` | n/a | detection C T1 glm-5.3-flash TprOne, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTOneTprOneHi` | n/a | detection C T1 glm-5.3-flash TprOne, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTOneTprOneCI` | n/a | detection C T1 glm-5.3-flash TprOne, 95% CI |
| `\DetGLMFiveThreeFlashCTOneTprOneN` | n/a | detection C T1 glm-5.3-flash TprOne, n |
| `\DetGLMFiveThreeFlashCTOneTprOneP` | n/a | detection C T1 glm-5.3-flash TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTOneTprFive` | n/a | detection C T1 glm-5.3-flash TprFive [n/a: no data yet] |
| `\DetGLMFiveThreeFlashCTOneTprFiveLo` | n/a | detection C T1 glm-5.3-flash TprFive, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTOneTprFiveHi` | n/a | detection C T1 glm-5.3-flash TprFive, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTOneTprFiveCI` | n/a | detection C T1 glm-5.3-flash TprFive, 95% CI |
| `\DetGLMFiveThreeFlashCTOneTprFiveN` | n/a | detection C T1 glm-5.3-flash TprFive, n |
| `\DetGLMFiveThreeFlashCTOneTprFiveP` | n/a | detection C T1 glm-5.3-flash TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTOne` | n/a | detection C T1 glm-5.2 AUROC [n/a: no data yet] |
| `\DetGLMFiveTwoCTOneLo` | n/a | detection C T1 glm-5.2 AUROC, lower 95% CI bound |
| `\DetGLMFiveTwoCTOneHi` | n/a | detection C T1 glm-5.2 AUROC, upper 95% CI bound |
| `\DetGLMFiveTwoCTOneCI` | n/a | detection C T1 glm-5.2 AUROC, 95% CI |
| `\DetGLMFiveTwoCTOneN` | n/a | detection C T1 glm-5.2 AUROC, n |
| `\DetGLMFiveTwoCTOneP` | n/a | detection C T1 glm-5.2 AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTOneTprOne` | n/a | detection C T1 glm-5.2 TprOne [n/a: no data yet] |
| `\DetGLMFiveTwoCTOneTprOneLo` | n/a | detection C T1 glm-5.2 TprOne, lower 95% CI bound |
| `\DetGLMFiveTwoCTOneTprOneHi` | n/a | detection C T1 glm-5.2 TprOne, upper 95% CI bound |
| `\DetGLMFiveTwoCTOneTprOneCI` | n/a | detection C T1 glm-5.2 TprOne, 95% CI |
| `\DetGLMFiveTwoCTOneTprOneN` | n/a | detection C T1 glm-5.2 TprOne, n |
| `\DetGLMFiveTwoCTOneTprOneP` | n/a | detection C T1 glm-5.2 TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTOneTprFive` | n/a | detection C T1 glm-5.2 TprFive [n/a: no data yet] |
| `\DetGLMFiveTwoCTOneTprFiveLo` | n/a | detection C T1 glm-5.2 TprFive, lower 95% CI bound |
| `\DetGLMFiveTwoCTOneTprFiveHi` | n/a | detection C T1 glm-5.2 TprFive, upper 95% CI bound |
| `\DetGLMFiveTwoCTOneTprFiveCI` | n/a | detection C T1 glm-5.2 TprFive, 95% CI |
| `\DetGLMFiveTwoCTOneTprFiveN` | n/a | detection C T1 glm-5.2 TprFive, n |
| `\DetGLMFiveTwoCTOneTprFiveP` | n/a | detection C T1 glm-5.2 TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTTwo` | n/a | detection C T2 qwen3.8-27b AUROC [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBCTTwoLo` | n/a | detection C T2 qwen3.8-27b AUROC, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTTwoHi` | n/a | detection C T2 qwen3.8-27b AUROC, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTTwoCI` | n/a | detection C T2 qwen3.8-27b AUROC, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTTwoN` | n/a | detection C T2 qwen3.8-27b AUROC, n |
| `\DetQwenThreeEightTwoSevenBCTTwoP` | n/a | detection C T2 qwen3.8-27b AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTTwoTprOne` | n/a | detection C T2 qwen3.8-27b TprOne [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBCTTwoTprOneLo` | n/a | detection C T2 qwen3.8-27b TprOne, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTTwoTprOneHi` | n/a | detection C T2 qwen3.8-27b TprOne, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTTwoTprOneCI` | n/a | detection C T2 qwen3.8-27b TprOne, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTTwoTprOneN` | n/a | detection C T2 qwen3.8-27b TprOne, n |
| `\DetQwenThreeEightTwoSevenBCTTwoTprOneP` | n/a | detection C T2 qwen3.8-27b TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTTwoTprFive` | n/a | detection C T2 qwen3.8-27b TprFive [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBCTTwoTprFiveLo` | n/a | detection C T2 qwen3.8-27b TprFive, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTTwoTprFiveHi` | n/a | detection C T2 qwen3.8-27b TprFive, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTTwoTprFiveCI` | n/a | detection C T2 qwen3.8-27b TprFive, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTTwoTprFiveN` | n/a | detection C T2 qwen3.8-27b TprFive, n |
| `\DetQwenThreeEightTwoSevenBCTTwoTprFiveP` | n/a | detection C T2 qwen3.8-27b TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTTwo` | n/a | detection C T2 glm-5.3-flash AUROC [n/a: no data yet] |
| `\DetGLMFiveThreeFlashCTTwoLo` | n/a | detection C T2 glm-5.3-flash AUROC, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTTwoHi` | n/a | detection C T2 glm-5.3-flash AUROC, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTTwoCI` | n/a | detection C T2 glm-5.3-flash AUROC, 95% CI |
| `\DetGLMFiveThreeFlashCTTwoN` | n/a | detection C T2 glm-5.3-flash AUROC, n |
| `\DetGLMFiveThreeFlashCTTwoP` | n/a | detection C T2 glm-5.3-flash AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTTwoTprOne` | n/a | detection C T2 glm-5.3-flash TprOne [n/a: no data yet] |
| `\DetGLMFiveThreeFlashCTTwoTprOneLo` | n/a | detection C T2 glm-5.3-flash TprOne, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTTwoTprOneHi` | n/a | detection C T2 glm-5.3-flash TprOne, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTTwoTprOneCI` | n/a | detection C T2 glm-5.3-flash TprOne, 95% CI |
| `\DetGLMFiveThreeFlashCTTwoTprOneN` | n/a | detection C T2 glm-5.3-flash TprOne, n |
| `\DetGLMFiveThreeFlashCTTwoTprOneP` | n/a | detection C T2 glm-5.3-flash TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTTwoTprFive` | n/a | detection C T2 glm-5.3-flash TprFive [n/a: no data yet] |
| `\DetGLMFiveThreeFlashCTTwoTprFiveLo` | n/a | detection C T2 glm-5.3-flash TprFive, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTTwoTprFiveHi` | n/a | detection C T2 glm-5.3-flash TprFive, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTTwoTprFiveCI` | n/a | detection C T2 glm-5.3-flash TprFive, 95% CI |
| `\DetGLMFiveThreeFlashCTTwoTprFiveN` | n/a | detection C T2 glm-5.3-flash TprFive, n |
| `\DetGLMFiveThreeFlashCTTwoTprFiveP` | n/a | detection C T2 glm-5.3-flash TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTTwo` | n/a | detection C T2 glm-5.2 AUROC [n/a: no data yet] |
| `\DetGLMFiveTwoCTTwoLo` | n/a | detection C T2 glm-5.2 AUROC, lower 95% CI bound |
| `\DetGLMFiveTwoCTTwoHi` | n/a | detection C T2 glm-5.2 AUROC, upper 95% CI bound |
| `\DetGLMFiveTwoCTTwoCI` | n/a | detection C T2 glm-5.2 AUROC, 95% CI |
| `\DetGLMFiveTwoCTTwoN` | n/a | detection C T2 glm-5.2 AUROC, n |
| `\DetGLMFiveTwoCTTwoP` | n/a | detection C T2 glm-5.2 AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTTwoTprOne` | n/a | detection C T2 glm-5.2 TprOne [n/a: no data yet] |
| `\DetGLMFiveTwoCTTwoTprOneLo` | n/a | detection C T2 glm-5.2 TprOne, lower 95% CI bound |
| `\DetGLMFiveTwoCTTwoTprOneHi` | n/a | detection C T2 glm-5.2 TprOne, upper 95% CI bound |
| `\DetGLMFiveTwoCTTwoTprOneCI` | n/a | detection C T2 glm-5.2 TprOne, 95% CI |
| `\DetGLMFiveTwoCTTwoTprOneN` | n/a | detection C T2 glm-5.2 TprOne, n |
| `\DetGLMFiveTwoCTTwoTprOneP` | n/a | detection C T2 glm-5.2 TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTTwoTprFive` | n/a | detection C T2 glm-5.2 TprFive [n/a: no data yet] |
| `\DetGLMFiveTwoCTTwoTprFiveLo` | n/a | detection C T2 glm-5.2 TprFive, lower 95% CI bound |
| `\DetGLMFiveTwoCTTwoTprFiveHi` | n/a | detection C T2 glm-5.2 TprFive, upper 95% CI bound |
| `\DetGLMFiveTwoCTTwoTprFiveCI` | n/a | detection C T2 glm-5.2 TprFive, 95% CI |
| `\DetGLMFiveTwoCTTwoTprFiveN` | n/a | detection C T2 glm-5.2 TprFive, n |
| `\DetGLMFiveTwoCTTwoTprFiveP` | n/a | detection C T2 glm-5.2 TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTThree` | n/a | detection C T3 qwen3.8-27b AUROC [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBCTThreeLo` | n/a | detection C T3 qwen3.8-27b AUROC, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTThreeHi` | n/a | detection C T3 qwen3.8-27b AUROC, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTThreeCI` | n/a | detection C T3 qwen3.8-27b AUROC, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTThreeN` | n/a | detection C T3 qwen3.8-27b AUROC, n |
| `\DetQwenThreeEightTwoSevenBCTThreeP` | n/a | detection C T3 qwen3.8-27b AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTThreeTprOne` | n/a | detection C T3 qwen3.8-27b TprOne [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBCTThreeTprOneLo` | n/a | detection C T3 qwen3.8-27b TprOne, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTThreeTprOneHi` | n/a | detection C T3 qwen3.8-27b TprOne, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTThreeTprOneCI` | n/a | detection C T3 qwen3.8-27b TprOne, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTThreeTprOneN` | n/a | detection C T3 qwen3.8-27b TprOne, n |
| `\DetQwenThreeEightTwoSevenBCTThreeTprOneP` | n/a | detection C T3 qwen3.8-27b TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTThreeTprFive` | n/a | detection C T3 qwen3.8-27b TprFive [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBCTThreeTprFiveLo` | n/a | detection C T3 qwen3.8-27b TprFive, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTThreeTprFiveHi` | n/a | detection C T3 qwen3.8-27b TprFive, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTThreeTprFiveCI` | n/a | detection C T3 qwen3.8-27b TprFive, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTThreeTprFiveN` | n/a | detection C T3 qwen3.8-27b TprFive, n |
| `\DetQwenThreeEightTwoSevenBCTThreeTprFiveP` | n/a | detection C T3 qwen3.8-27b TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTThree` | n/a | detection C T3 glm-5.3-flash AUROC [n/a: no data yet] |
| `\DetGLMFiveThreeFlashCTThreeLo` | n/a | detection C T3 glm-5.3-flash AUROC, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTThreeHi` | n/a | detection C T3 glm-5.3-flash AUROC, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTThreeCI` | n/a | detection C T3 glm-5.3-flash AUROC, 95% CI |
| `\DetGLMFiveThreeFlashCTThreeN` | n/a | detection C T3 glm-5.3-flash AUROC, n |
| `\DetGLMFiveThreeFlashCTThreeP` | n/a | detection C T3 glm-5.3-flash AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTThreeTprOne` | n/a | detection C T3 glm-5.3-flash TprOne [n/a: no data yet] |
| `\DetGLMFiveThreeFlashCTThreeTprOneLo` | n/a | detection C T3 glm-5.3-flash TprOne, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTThreeTprOneHi` | n/a | detection C T3 glm-5.3-flash TprOne, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTThreeTprOneCI` | n/a | detection C T3 glm-5.3-flash TprOne, 95% CI |
| `\DetGLMFiveThreeFlashCTThreeTprOneN` | n/a | detection C T3 glm-5.3-flash TprOne, n |
| `\DetGLMFiveThreeFlashCTThreeTprOneP` | n/a | detection C T3 glm-5.3-flash TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTThreeTprFive` | n/a | detection C T3 glm-5.3-flash TprFive [n/a: no data yet] |
| `\DetGLMFiveThreeFlashCTThreeTprFiveLo` | n/a | detection C T3 glm-5.3-flash TprFive, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTThreeTprFiveHi` | n/a | detection C T3 glm-5.3-flash TprFive, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTThreeTprFiveCI` | n/a | detection C T3 glm-5.3-flash TprFive, 95% CI |
| `\DetGLMFiveThreeFlashCTThreeTprFiveN` | n/a | detection C T3 glm-5.3-flash TprFive, n |
| `\DetGLMFiveThreeFlashCTThreeTprFiveP` | n/a | detection C T3 glm-5.3-flash TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTThree` | n/a | detection C T3 glm-5.2 AUROC [n/a: no data yet] |
| `\DetGLMFiveTwoCTThreeLo` | n/a | detection C T3 glm-5.2 AUROC, lower 95% CI bound |
| `\DetGLMFiveTwoCTThreeHi` | n/a | detection C T3 glm-5.2 AUROC, upper 95% CI bound |
| `\DetGLMFiveTwoCTThreeCI` | n/a | detection C T3 glm-5.2 AUROC, 95% CI |
| `\DetGLMFiveTwoCTThreeN` | n/a | detection C T3 glm-5.2 AUROC, n |
| `\DetGLMFiveTwoCTThreeP` | n/a | detection C T3 glm-5.2 AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTThreeTprOne` | n/a | detection C T3 glm-5.2 TprOne [n/a: no data yet] |
| `\DetGLMFiveTwoCTThreeTprOneLo` | n/a | detection C T3 glm-5.2 TprOne, lower 95% CI bound |
| `\DetGLMFiveTwoCTThreeTprOneHi` | n/a | detection C T3 glm-5.2 TprOne, upper 95% CI bound |
| `\DetGLMFiveTwoCTThreeTprOneCI` | n/a | detection C T3 glm-5.2 TprOne, 95% CI |
| `\DetGLMFiveTwoCTThreeTprOneN` | n/a | detection C T3 glm-5.2 TprOne, n |
| `\DetGLMFiveTwoCTThreeTprOneP` | n/a | detection C T3 glm-5.2 TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTThreeTprFive` | n/a | detection C T3 glm-5.2 TprFive [n/a: no data yet] |
| `\DetGLMFiveTwoCTThreeTprFiveLo` | n/a | detection C T3 glm-5.2 TprFive, lower 95% CI bound |
| `\DetGLMFiveTwoCTThreeTprFiveHi` | n/a | detection C T3 glm-5.2 TprFive, upper 95% CI bound |
| `\DetGLMFiveTwoCTThreeTprFiveCI` | n/a | detection C T3 glm-5.2 TprFive, 95% CI |
| `\DetGLMFiveTwoCTThreeTprFiveN` | n/a | detection C T3 glm-5.2 TprFive, n |
| `\DetGLMFiveTwoCTThreeTprFiveP` | n/a | detection C T3 glm-5.2 TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTZero` | n/a | detection R T0 qwen3.8-27b AUROC [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRTZeroLo` | n/a | detection R T0 qwen3.8-27b AUROC, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTZeroHi` | n/a | detection R T0 qwen3.8-27b AUROC, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTZeroCI` | n/a | detection R T0 qwen3.8-27b AUROC, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTZeroN` | n/a | detection R T0 qwen3.8-27b AUROC, n |
| `\DetQwenThreeEightTwoSevenBRTZeroP` | n/a | detection R T0 qwen3.8-27b AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTZeroTprOne` | n/a | detection R T0 qwen3.8-27b TprOne [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRTZeroTprOneLo` | n/a | detection R T0 qwen3.8-27b TprOne, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTZeroTprOneHi` | n/a | detection R T0 qwen3.8-27b TprOne, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTZeroTprOneCI` | n/a | detection R T0 qwen3.8-27b TprOne, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTZeroTprOneN` | n/a | detection R T0 qwen3.8-27b TprOne, n |
| `\DetQwenThreeEightTwoSevenBRTZeroTprOneP` | n/a | detection R T0 qwen3.8-27b TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTZeroTprFive` | n/a | detection R T0 qwen3.8-27b TprFive [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRTZeroTprFiveLo` | n/a | detection R T0 qwen3.8-27b TprFive, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTZeroTprFiveHi` | n/a | detection R T0 qwen3.8-27b TprFive, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTZeroTprFiveCI` | n/a | detection R T0 qwen3.8-27b TprFive, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTZeroTprFiveN` | n/a | detection R T0 qwen3.8-27b TprFive, n |
| `\DetQwenThreeEightTwoSevenBRTZeroTprFiveP` | n/a | detection R T0 qwen3.8-27b TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTZero` | n/a | detection R T0 glm-5.3-flash AUROC [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRTZeroLo` | n/a | detection R T0 glm-5.3-flash AUROC, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTZeroHi` | n/a | detection R T0 glm-5.3-flash AUROC, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTZeroCI` | n/a | detection R T0 glm-5.3-flash AUROC, 95% CI |
| `\DetGLMFiveThreeFlashRTZeroN` | n/a | detection R T0 glm-5.3-flash AUROC, n |
| `\DetGLMFiveThreeFlashRTZeroP` | n/a | detection R T0 glm-5.3-flash AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTZeroTprOne` | n/a | detection R T0 glm-5.3-flash TprOne [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRTZeroTprOneLo` | n/a | detection R T0 glm-5.3-flash TprOne, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTZeroTprOneHi` | n/a | detection R T0 glm-5.3-flash TprOne, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTZeroTprOneCI` | n/a | detection R T0 glm-5.3-flash TprOne, 95% CI |
| `\DetGLMFiveThreeFlashRTZeroTprOneN` | n/a | detection R T0 glm-5.3-flash TprOne, n |
| `\DetGLMFiveThreeFlashRTZeroTprOneP` | n/a | detection R T0 glm-5.3-flash TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTZeroTprFive` | n/a | detection R T0 glm-5.3-flash TprFive [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRTZeroTprFiveLo` | n/a | detection R T0 glm-5.3-flash TprFive, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTZeroTprFiveHi` | n/a | detection R T0 glm-5.3-flash TprFive, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTZeroTprFiveCI` | n/a | detection R T0 glm-5.3-flash TprFive, 95% CI |
| `\DetGLMFiveThreeFlashRTZeroTprFiveN` | n/a | detection R T0 glm-5.3-flash TprFive, n |
| `\DetGLMFiveThreeFlashRTZeroTprFiveP` | n/a | detection R T0 glm-5.3-flash TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTZero` | n/a | detection R T0 glm-5.2 AUROC [n/a: no data yet] |
| `\DetGLMFiveTwoRTZeroLo` | n/a | detection R T0 glm-5.2 AUROC, lower 95% CI bound |
| `\DetGLMFiveTwoRTZeroHi` | n/a | detection R T0 glm-5.2 AUROC, upper 95% CI bound |
| `\DetGLMFiveTwoRTZeroCI` | n/a | detection R T0 glm-5.2 AUROC, 95% CI |
| `\DetGLMFiveTwoRTZeroN` | n/a | detection R T0 glm-5.2 AUROC, n |
| `\DetGLMFiveTwoRTZeroP` | n/a | detection R T0 glm-5.2 AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTZeroTprOne` | n/a | detection R T0 glm-5.2 TprOne [n/a: no data yet] |
| `\DetGLMFiveTwoRTZeroTprOneLo` | n/a | detection R T0 glm-5.2 TprOne, lower 95% CI bound |
| `\DetGLMFiveTwoRTZeroTprOneHi` | n/a | detection R T0 glm-5.2 TprOne, upper 95% CI bound |
| `\DetGLMFiveTwoRTZeroTprOneCI` | n/a | detection R T0 glm-5.2 TprOne, 95% CI |
| `\DetGLMFiveTwoRTZeroTprOneN` | n/a | detection R T0 glm-5.2 TprOne, n |
| `\DetGLMFiveTwoRTZeroTprOneP` | n/a | detection R T0 glm-5.2 TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTZeroTprFive` | n/a | detection R T0 glm-5.2 TprFive [n/a: no data yet] |
| `\DetGLMFiveTwoRTZeroTprFiveLo` | n/a | detection R T0 glm-5.2 TprFive, lower 95% CI bound |
| `\DetGLMFiveTwoRTZeroTprFiveHi` | n/a | detection R T0 glm-5.2 TprFive, upper 95% CI bound |
| `\DetGLMFiveTwoRTZeroTprFiveCI` | n/a | detection R T0 glm-5.2 TprFive, 95% CI |
| `\DetGLMFiveTwoRTZeroTprFiveN` | n/a | detection R T0 glm-5.2 TprFive, n |
| `\DetGLMFiveTwoRTZeroTprFiveP` | n/a | detection R T0 glm-5.2 TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTOne` | n/a | detection R T1 qwen3.8-27b AUROC [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRTOneLo` | n/a | detection R T1 qwen3.8-27b AUROC, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTOneHi` | n/a | detection R T1 qwen3.8-27b AUROC, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTOneCI` | n/a | detection R T1 qwen3.8-27b AUROC, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTOneN` | n/a | detection R T1 qwen3.8-27b AUROC, n |
| `\DetQwenThreeEightTwoSevenBRTOneP` | n/a | detection R T1 qwen3.8-27b AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTOneTprOne` | n/a | detection R T1 qwen3.8-27b TprOne [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRTOneTprOneLo` | n/a | detection R T1 qwen3.8-27b TprOne, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTOneTprOneHi` | n/a | detection R T1 qwen3.8-27b TprOne, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTOneTprOneCI` | n/a | detection R T1 qwen3.8-27b TprOne, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTOneTprOneN` | n/a | detection R T1 qwen3.8-27b TprOne, n |
| `\DetQwenThreeEightTwoSevenBRTOneTprOneP` | n/a | detection R T1 qwen3.8-27b TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTOneTprFive` | n/a | detection R T1 qwen3.8-27b TprFive [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRTOneTprFiveLo` | n/a | detection R T1 qwen3.8-27b TprFive, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTOneTprFiveHi` | n/a | detection R T1 qwen3.8-27b TprFive, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTOneTprFiveCI` | n/a | detection R T1 qwen3.8-27b TprFive, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTOneTprFiveN` | n/a | detection R T1 qwen3.8-27b TprFive, n |
| `\DetQwenThreeEightTwoSevenBRTOneTprFiveP` | n/a | detection R T1 qwen3.8-27b TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTOne` | n/a | detection R T1 glm-5.3-flash AUROC [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRTOneLo` | n/a | detection R T1 glm-5.3-flash AUROC, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTOneHi` | n/a | detection R T1 glm-5.3-flash AUROC, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTOneCI` | n/a | detection R T1 glm-5.3-flash AUROC, 95% CI |
| `\DetGLMFiveThreeFlashRTOneN` | n/a | detection R T1 glm-5.3-flash AUROC, n |
| `\DetGLMFiveThreeFlashRTOneP` | n/a | detection R T1 glm-5.3-flash AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTOneTprOne` | n/a | detection R T1 glm-5.3-flash TprOne [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRTOneTprOneLo` | n/a | detection R T1 glm-5.3-flash TprOne, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTOneTprOneHi` | n/a | detection R T1 glm-5.3-flash TprOne, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTOneTprOneCI` | n/a | detection R T1 glm-5.3-flash TprOne, 95% CI |
| `\DetGLMFiveThreeFlashRTOneTprOneN` | n/a | detection R T1 glm-5.3-flash TprOne, n |
| `\DetGLMFiveThreeFlashRTOneTprOneP` | n/a | detection R T1 glm-5.3-flash TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTOneTprFive` | n/a | detection R T1 glm-5.3-flash TprFive [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRTOneTprFiveLo` | n/a | detection R T1 glm-5.3-flash TprFive, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTOneTprFiveHi` | n/a | detection R T1 glm-5.3-flash TprFive, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTOneTprFiveCI` | n/a | detection R T1 glm-5.3-flash TprFive, 95% CI |
| `\DetGLMFiveThreeFlashRTOneTprFiveN` | n/a | detection R T1 glm-5.3-flash TprFive, n |
| `\DetGLMFiveThreeFlashRTOneTprFiveP` | n/a | detection R T1 glm-5.3-flash TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTOne` | n/a | detection R T1 glm-5.2 AUROC [n/a: no data yet] |
| `\DetGLMFiveTwoRTOneLo` | n/a | detection R T1 glm-5.2 AUROC, lower 95% CI bound |
| `\DetGLMFiveTwoRTOneHi` | n/a | detection R T1 glm-5.2 AUROC, upper 95% CI bound |
| `\DetGLMFiveTwoRTOneCI` | n/a | detection R T1 glm-5.2 AUROC, 95% CI |
| `\DetGLMFiveTwoRTOneN` | n/a | detection R T1 glm-5.2 AUROC, n |
| `\DetGLMFiveTwoRTOneP` | n/a | detection R T1 glm-5.2 AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTOneTprOne` | n/a | detection R T1 glm-5.2 TprOne [n/a: no data yet] |
| `\DetGLMFiveTwoRTOneTprOneLo` | n/a | detection R T1 glm-5.2 TprOne, lower 95% CI bound |
| `\DetGLMFiveTwoRTOneTprOneHi` | n/a | detection R T1 glm-5.2 TprOne, upper 95% CI bound |
| `\DetGLMFiveTwoRTOneTprOneCI` | n/a | detection R T1 glm-5.2 TprOne, 95% CI |
| `\DetGLMFiveTwoRTOneTprOneN` | n/a | detection R T1 glm-5.2 TprOne, n |
| `\DetGLMFiveTwoRTOneTprOneP` | n/a | detection R T1 glm-5.2 TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTOneTprFive` | n/a | detection R T1 glm-5.2 TprFive [n/a: no data yet] |
| `\DetGLMFiveTwoRTOneTprFiveLo` | n/a | detection R T1 glm-5.2 TprFive, lower 95% CI bound |
| `\DetGLMFiveTwoRTOneTprFiveHi` | n/a | detection R T1 glm-5.2 TprFive, upper 95% CI bound |
| `\DetGLMFiveTwoRTOneTprFiveCI` | n/a | detection R T1 glm-5.2 TprFive, 95% CI |
| `\DetGLMFiveTwoRTOneTprFiveN` | n/a | detection R T1 glm-5.2 TprFive, n |
| `\DetGLMFiveTwoRTOneTprFiveP` | n/a | detection R T1 glm-5.2 TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTTwo` | n/a | detection R T2 qwen3.8-27b AUROC [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRTTwoLo` | n/a | detection R T2 qwen3.8-27b AUROC, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTTwoHi` | n/a | detection R T2 qwen3.8-27b AUROC, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTTwoCI` | n/a | detection R T2 qwen3.8-27b AUROC, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTTwoN` | n/a | detection R T2 qwen3.8-27b AUROC, n |
| `\DetQwenThreeEightTwoSevenBRTTwoP` | n/a | detection R T2 qwen3.8-27b AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTTwoTprOne` | n/a | detection R T2 qwen3.8-27b TprOne [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRTTwoTprOneLo` | n/a | detection R T2 qwen3.8-27b TprOne, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTTwoTprOneHi` | n/a | detection R T2 qwen3.8-27b TprOne, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTTwoTprOneCI` | n/a | detection R T2 qwen3.8-27b TprOne, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTTwoTprOneN` | n/a | detection R T2 qwen3.8-27b TprOne, n |
| `\DetQwenThreeEightTwoSevenBRTTwoTprOneP` | n/a | detection R T2 qwen3.8-27b TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTTwoTprFive` | n/a | detection R T2 qwen3.8-27b TprFive [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRTTwoTprFiveLo` | n/a | detection R T2 qwen3.8-27b TprFive, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTTwoTprFiveHi` | n/a | detection R T2 qwen3.8-27b TprFive, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTTwoTprFiveCI` | n/a | detection R T2 qwen3.8-27b TprFive, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTTwoTprFiveN` | n/a | detection R T2 qwen3.8-27b TprFive, n |
| `\DetQwenThreeEightTwoSevenBRTTwoTprFiveP` | n/a | detection R T2 qwen3.8-27b TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTTwo` | n/a | detection R T2 glm-5.3-flash AUROC [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRTTwoLo` | n/a | detection R T2 glm-5.3-flash AUROC, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTTwoHi` | n/a | detection R T2 glm-5.3-flash AUROC, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTTwoCI` | n/a | detection R T2 glm-5.3-flash AUROC, 95% CI |
| `\DetGLMFiveThreeFlashRTTwoN` | n/a | detection R T2 glm-5.3-flash AUROC, n |
| `\DetGLMFiveThreeFlashRTTwoP` | n/a | detection R T2 glm-5.3-flash AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTTwoTprOne` | n/a | detection R T2 glm-5.3-flash TprOne [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRTTwoTprOneLo` | n/a | detection R T2 glm-5.3-flash TprOne, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTTwoTprOneHi` | n/a | detection R T2 glm-5.3-flash TprOne, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTTwoTprOneCI` | n/a | detection R T2 glm-5.3-flash TprOne, 95% CI |
| `\DetGLMFiveThreeFlashRTTwoTprOneN` | n/a | detection R T2 glm-5.3-flash TprOne, n |
| `\DetGLMFiveThreeFlashRTTwoTprOneP` | n/a | detection R T2 glm-5.3-flash TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTTwoTprFive` | n/a | detection R T2 glm-5.3-flash TprFive [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRTTwoTprFiveLo` | n/a | detection R T2 glm-5.3-flash TprFive, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTTwoTprFiveHi` | n/a | detection R T2 glm-5.3-flash TprFive, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTTwoTprFiveCI` | n/a | detection R T2 glm-5.3-flash TprFive, 95% CI |
| `\DetGLMFiveThreeFlashRTTwoTprFiveN` | n/a | detection R T2 glm-5.3-flash TprFive, n |
| `\DetGLMFiveThreeFlashRTTwoTprFiveP` | n/a | detection R T2 glm-5.3-flash TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTTwo` | n/a | detection R T2 glm-5.2 AUROC [n/a: no data yet] |
| `\DetGLMFiveTwoRTTwoLo` | n/a | detection R T2 glm-5.2 AUROC, lower 95% CI bound |
| `\DetGLMFiveTwoRTTwoHi` | n/a | detection R T2 glm-5.2 AUROC, upper 95% CI bound |
| `\DetGLMFiveTwoRTTwoCI` | n/a | detection R T2 glm-5.2 AUROC, 95% CI |
| `\DetGLMFiveTwoRTTwoN` | n/a | detection R T2 glm-5.2 AUROC, n |
| `\DetGLMFiveTwoRTTwoP` | n/a | detection R T2 glm-5.2 AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTTwoTprOne` | n/a | detection R T2 glm-5.2 TprOne [n/a: no data yet] |
| `\DetGLMFiveTwoRTTwoTprOneLo` | n/a | detection R T2 glm-5.2 TprOne, lower 95% CI bound |
| `\DetGLMFiveTwoRTTwoTprOneHi` | n/a | detection R T2 glm-5.2 TprOne, upper 95% CI bound |
| `\DetGLMFiveTwoRTTwoTprOneCI` | n/a | detection R T2 glm-5.2 TprOne, 95% CI |
| `\DetGLMFiveTwoRTTwoTprOneN` | n/a | detection R T2 glm-5.2 TprOne, n |
| `\DetGLMFiveTwoRTTwoTprOneP` | n/a | detection R T2 glm-5.2 TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTTwoTprFive` | n/a | detection R T2 glm-5.2 TprFive [n/a: no data yet] |
| `\DetGLMFiveTwoRTTwoTprFiveLo` | n/a | detection R T2 glm-5.2 TprFive, lower 95% CI bound |
| `\DetGLMFiveTwoRTTwoTprFiveHi` | n/a | detection R T2 glm-5.2 TprFive, upper 95% CI bound |
| `\DetGLMFiveTwoRTTwoTprFiveCI` | n/a | detection R T2 glm-5.2 TprFive, 95% CI |
| `\DetGLMFiveTwoRTTwoTprFiveN` | n/a | detection R T2 glm-5.2 TprFive, n |
| `\DetGLMFiveTwoRTTwoTprFiveP` | n/a | detection R T2 glm-5.2 TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTThree` | n/a | detection R T3 qwen3.8-27b AUROC [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRTThreeLo` | n/a | detection R T3 qwen3.8-27b AUROC, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTThreeHi` | n/a | detection R T3 qwen3.8-27b AUROC, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTThreeCI` | n/a | detection R T3 qwen3.8-27b AUROC, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTThreeN` | n/a | detection R T3 qwen3.8-27b AUROC, n |
| `\DetQwenThreeEightTwoSevenBRTThreeP` | n/a | detection R T3 qwen3.8-27b AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTThreeTprOne` | n/a | detection R T3 qwen3.8-27b TprOne [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRTThreeTprOneLo` | n/a | detection R T3 qwen3.8-27b TprOne, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTThreeTprOneHi` | n/a | detection R T3 qwen3.8-27b TprOne, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTThreeTprOneCI` | n/a | detection R T3 qwen3.8-27b TprOne, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTThreeTprOneN` | n/a | detection R T3 qwen3.8-27b TprOne, n |
| `\DetQwenThreeEightTwoSevenBRTThreeTprOneP` | n/a | detection R T3 qwen3.8-27b TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTThreeTprFive` | n/a | detection R T3 qwen3.8-27b TprFive [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRTThreeTprFiveLo` | n/a | detection R T3 qwen3.8-27b TprFive, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTThreeTprFiveHi` | n/a | detection R T3 qwen3.8-27b TprFive, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTThreeTprFiveCI` | n/a | detection R T3 qwen3.8-27b TprFive, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTThreeTprFiveN` | n/a | detection R T3 qwen3.8-27b TprFive, n |
| `\DetQwenThreeEightTwoSevenBRTThreeTprFiveP` | n/a | detection R T3 qwen3.8-27b TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTThree` | n/a | detection R T3 glm-5.3-flash AUROC [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRTThreeLo` | n/a | detection R T3 glm-5.3-flash AUROC, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTThreeHi` | n/a | detection R T3 glm-5.3-flash AUROC, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTThreeCI` | n/a | detection R T3 glm-5.3-flash AUROC, 95% CI |
| `\DetGLMFiveThreeFlashRTThreeN` | n/a | detection R T3 glm-5.3-flash AUROC, n |
| `\DetGLMFiveThreeFlashRTThreeP` | n/a | detection R T3 glm-5.3-flash AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTThreeTprOne` | n/a | detection R T3 glm-5.3-flash TprOne [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRTThreeTprOneLo` | n/a | detection R T3 glm-5.3-flash TprOne, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTThreeTprOneHi` | n/a | detection R T3 glm-5.3-flash TprOne, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTThreeTprOneCI` | n/a | detection R T3 glm-5.3-flash TprOne, 95% CI |
| `\DetGLMFiveThreeFlashRTThreeTprOneN` | n/a | detection R T3 glm-5.3-flash TprOne, n |
| `\DetGLMFiveThreeFlashRTThreeTprOneP` | n/a | detection R T3 glm-5.3-flash TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTThreeTprFive` | n/a | detection R T3 glm-5.3-flash TprFive [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRTThreeTprFiveLo` | n/a | detection R T3 glm-5.3-flash TprFive, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTThreeTprFiveHi` | n/a | detection R T3 glm-5.3-flash TprFive, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTThreeTprFiveCI` | n/a | detection R T3 glm-5.3-flash TprFive, 95% CI |
| `\DetGLMFiveThreeFlashRTThreeTprFiveN` | n/a | detection R T3 glm-5.3-flash TprFive, n |
| `\DetGLMFiveThreeFlashRTThreeTprFiveP` | n/a | detection R T3 glm-5.3-flash TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTThree` | n/a | detection R T3 glm-5.2 AUROC [n/a: no data yet] |
| `\DetGLMFiveTwoRTThreeLo` | n/a | detection R T3 glm-5.2 AUROC, lower 95% CI bound |
| `\DetGLMFiveTwoRTThreeHi` | n/a | detection R T3 glm-5.2 AUROC, upper 95% CI bound |
| `\DetGLMFiveTwoRTThreeCI` | n/a | detection R T3 glm-5.2 AUROC, 95% CI |
| `\DetGLMFiveTwoRTThreeN` | n/a | detection R T3 glm-5.2 AUROC, n |
| `\DetGLMFiveTwoRTThreeP` | n/a | detection R T3 glm-5.2 AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTThreeTprOne` | n/a | detection R T3 glm-5.2 TprOne [n/a: no data yet] |
| `\DetGLMFiveTwoRTThreeTprOneLo` | n/a | detection R T3 glm-5.2 TprOne, lower 95% CI bound |
| `\DetGLMFiveTwoRTThreeTprOneHi` | n/a | detection R T3 glm-5.2 TprOne, upper 95% CI bound |
| `\DetGLMFiveTwoRTThreeTprOneCI` | n/a | detection R T3 glm-5.2 TprOne, 95% CI |
| `\DetGLMFiveTwoRTThreeTprOneN` | n/a | detection R T3 glm-5.2 TprOne, n |
| `\DetGLMFiveTwoRTThreeTprOneP` | n/a | detection R T3 glm-5.2 TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTThreeTprFive` | n/a | detection R T3 glm-5.2 TprFive [n/a: no data yet] |
| `\DetGLMFiveTwoRTThreeTprFiveLo` | n/a | detection R T3 glm-5.2 TprFive, lower 95% CI bound |
| `\DetGLMFiveTwoRTThreeTprFiveHi` | n/a | detection R T3 glm-5.2 TprFive, upper 95% CI bound |
| `\DetGLMFiveTwoRTThreeTprFiveCI` | n/a | detection R T3 glm-5.2 TprFive, 95% CI |
| `\DetGLMFiveTwoRTThreeTprFiveN` | n/a | detection R T3 glm-5.2 TprFive, n |
| `\DetGLMFiveTwoRTThreeTprFiveP` | n/a | detection R T3 glm-5.2 TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTZero` | n/a | detection r_field T0 qwen3.8-27b AUROC [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroLo` | n/a | detection r_field T0 qwen3.8-27b AUROC, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroHi` | n/a | detection r_field T0 qwen3.8-27b AUROC, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroCI` | n/a | detection r_field T0 qwen3.8-27b AUROC, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroN` | n/a | detection r_field T0 qwen3.8-27b AUROC, n |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroP` | n/a | detection r_field T0 qwen3.8-27b AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprOne` | n/a | detection r_field T0 qwen3.8-27b TprOne [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprOneLo` | n/a | detection r_field T0 qwen3.8-27b TprOne, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprOneHi` | n/a | detection r_field T0 qwen3.8-27b TprOne, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprOneCI` | n/a | detection r_field T0 qwen3.8-27b TprOne, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprOneN` | n/a | detection r_field T0 qwen3.8-27b TprOne, n |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprOneP` | n/a | detection r_field T0 qwen3.8-27b TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprFive` | n/a | detection r_field T0 qwen3.8-27b TprFive [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprFiveLo` | n/a | detection r_field T0 qwen3.8-27b TprFive, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprFiveHi` | n/a | detection r_field T0 qwen3.8-27b TprFive, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprFiveCI` | n/a | detection r_field T0 qwen3.8-27b TprFive, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprFiveN` | n/a | detection r_field T0 qwen3.8-27b TprFive, n |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprFiveP` | n/a | detection r_field T0 qwen3.8-27b TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTZero` | n/a | detection r_field T0 glm-5.3-flash AUROC [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRFieldTZeroLo` | n/a | detection r_field T0 glm-5.3-flash AUROC, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTZeroHi` | n/a | detection r_field T0 glm-5.3-flash AUROC, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTZeroCI` | n/a | detection r_field T0 glm-5.3-flash AUROC, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTZeroN` | n/a | detection r_field T0 glm-5.3-flash AUROC, n |
| `\DetGLMFiveThreeFlashRFieldTZeroP` | n/a | detection r_field T0 glm-5.3-flash AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTZeroTprOne` | n/a | detection r_field T0 glm-5.3-flash TprOne [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRFieldTZeroTprOneLo` | n/a | detection r_field T0 glm-5.3-flash TprOne, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTZeroTprOneHi` | n/a | detection r_field T0 glm-5.3-flash TprOne, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTZeroTprOneCI` | n/a | detection r_field T0 glm-5.3-flash TprOne, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTZeroTprOneN` | n/a | detection r_field T0 glm-5.3-flash TprOne, n |
| `\DetGLMFiveThreeFlashRFieldTZeroTprOneP` | n/a | detection r_field T0 glm-5.3-flash TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTZeroTprFive` | n/a | detection r_field T0 glm-5.3-flash TprFive [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRFieldTZeroTprFiveLo` | n/a | detection r_field T0 glm-5.3-flash TprFive, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTZeroTprFiveHi` | n/a | detection r_field T0 glm-5.3-flash TprFive, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTZeroTprFiveCI` | n/a | detection r_field T0 glm-5.3-flash TprFive, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTZeroTprFiveN` | n/a | detection r_field T0 glm-5.3-flash TprFive, n |
| `\DetGLMFiveThreeFlashRFieldTZeroTprFiveP` | n/a | detection r_field T0 glm-5.3-flash TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTZero` | n/a | detection r_field T0 glm-5.2 AUROC [n/a: no data yet] |
| `\DetGLMFiveTwoRFieldTZeroLo` | n/a | detection r_field T0 glm-5.2 AUROC, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTZeroHi` | n/a | detection r_field T0 glm-5.2 AUROC, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTZeroCI` | n/a | detection r_field T0 glm-5.2 AUROC, 95% CI |
| `\DetGLMFiveTwoRFieldTZeroN` | n/a | detection r_field T0 glm-5.2 AUROC, n |
| `\DetGLMFiveTwoRFieldTZeroP` | n/a | detection r_field T0 glm-5.2 AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTZeroTprOne` | n/a | detection r_field T0 glm-5.2 TprOne [n/a: no data yet] |
| `\DetGLMFiveTwoRFieldTZeroTprOneLo` | n/a | detection r_field T0 glm-5.2 TprOne, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTZeroTprOneHi` | n/a | detection r_field T0 glm-5.2 TprOne, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTZeroTprOneCI` | n/a | detection r_field T0 glm-5.2 TprOne, 95% CI |
| `\DetGLMFiveTwoRFieldTZeroTprOneN` | n/a | detection r_field T0 glm-5.2 TprOne, n |
| `\DetGLMFiveTwoRFieldTZeroTprOneP` | n/a | detection r_field T0 glm-5.2 TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTZeroTprFive` | n/a | detection r_field T0 glm-5.2 TprFive [n/a: no data yet] |
| `\DetGLMFiveTwoRFieldTZeroTprFiveLo` | n/a | detection r_field T0 glm-5.2 TprFive, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTZeroTprFiveHi` | n/a | detection r_field T0 glm-5.2 TprFive, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTZeroTprFiveCI` | n/a | detection r_field T0 glm-5.2 TprFive, 95% CI |
| `\DetGLMFiveTwoRFieldTZeroTprFiveN` | n/a | detection r_field T0 glm-5.2 TprFive, n |
| `\DetGLMFiveTwoRFieldTZeroTprFiveP` | n/a | detection r_field T0 glm-5.2 TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTOne` | n/a | detection r_field T1 qwen3.8-27b AUROC [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRFieldTOneLo` | n/a | detection r_field T1 qwen3.8-27b AUROC, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTOneHi` | n/a | detection r_field T1 qwen3.8-27b AUROC, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTOneCI` | n/a | detection r_field T1 qwen3.8-27b AUROC, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTOneN` | n/a | detection r_field T1 qwen3.8-27b AUROC, n |
| `\DetQwenThreeEightTwoSevenBRFieldTOneP` | n/a | detection r_field T1 qwen3.8-27b AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprOne` | n/a | detection r_field T1 qwen3.8-27b TprOne [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprOneLo` | n/a | detection r_field T1 qwen3.8-27b TprOne, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprOneHi` | n/a | detection r_field T1 qwen3.8-27b TprOne, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprOneCI` | n/a | detection r_field T1 qwen3.8-27b TprOne, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprOneN` | n/a | detection r_field T1 qwen3.8-27b TprOne, n |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprOneP` | n/a | detection r_field T1 qwen3.8-27b TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprFive` | n/a | detection r_field T1 qwen3.8-27b TprFive [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprFiveLo` | n/a | detection r_field T1 qwen3.8-27b TprFive, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprFiveHi` | n/a | detection r_field T1 qwen3.8-27b TprFive, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprFiveCI` | n/a | detection r_field T1 qwen3.8-27b TprFive, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprFiveN` | n/a | detection r_field T1 qwen3.8-27b TprFive, n |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprFiveP` | n/a | detection r_field T1 qwen3.8-27b TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTOne` | n/a | detection r_field T1 glm-5.3-flash AUROC [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRFieldTOneLo` | n/a | detection r_field T1 glm-5.3-flash AUROC, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTOneHi` | n/a | detection r_field T1 glm-5.3-flash AUROC, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTOneCI` | n/a | detection r_field T1 glm-5.3-flash AUROC, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTOneN` | n/a | detection r_field T1 glm-5.3-flash AUROC, n |
| `\DetGLMFiveThreeFlashRFieldTOneP` | n/a | detection r_field T1 glm-5.3-flash AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTOneTprOne` | n/a | detection r_field T1 glm-5.3-flash TprOne [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRFieldTOneTprOneLo` | n/a | detection r_field T1 glm-5.3-flash TprOne, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTOneTprOneHi` | n/a | detection r_field T1 glm-5.3-flash TprOne, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTOneTprOneCI` | n/a | detection r_field T1 glm-5.3-flash TprOne, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTOneTprOneN` | n/a | detection r_field T1 glm-5.3-flash TprOne, n |
| `\DetGLMFiveThreeFlashRFieldTOneTprOneP` | n/a | detection r_field T1 glm-5.3-flash TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTOneTprFive` | n/a | detection r_field T1 glm-5.3-flash TprFive [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRFieldTOneTprFiveLo` | n/a | detection r_field T1 glm-5.3-flash TprFive, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTOneTprFiveHi` | n/a | detection r_field T1 glm-5.3-flash TprFive, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTOneTprFiveCI` | n/a | detection r_field T1 glm-5.3-flash TprFive, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTOneTprFiveN` | n/a | detection r_field T1 glm-5.3-flash TprFive, n |
| `\DetGLMFiveThreeFlashRFieldTOneTprFiveP` | n/a | detection r_field T1 glm-5.3-flash TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTOne` | n/a | detection r_field T1 glm-5.2 AUROC [n/a: no data yet] |
| `\DetGLMFiveTwoRFieldTOneLo` | n/a | detection r_field T1 glm-5.2 AUROC, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTOneHi` | n/a | detection r_field T1 glm-5.2 AUROC, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTOneCI` | n/a | detection r_field T1 glm-5.2 AUROC, 95% CI |
| `\DetGLMFiveTwoRFieldTOneN` | n/a | detection r_field T1 glm-5.2 AUROC, n |
| `\DetGLMFiveTwoRFieldTOneP` | n/a | detection r_field T1 glm-5.2 AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTOneTprOne` | n/a | detection r_field T1 glm-5.2 TprOne [n/a: no data yet] |
| `\DetGLMFiveTwoRFieldTOneTprOneLo` | n/a | detection r_field T1 glm-5.2 TprOne, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTOneTprOneHi` | n/a | detection r_field T1 glm-5.2 TprOne, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTOneTprOneCI` | n/a | detection r_field T1 glm-5.2 TprOne, 95% CI |
| `\DetGLMFiveTwoRFieldTOneTprOneN` | n/a | detection r_field T1 glm-5.2 TprOne, n |
| `\DetGLMFiveTwoRFieldTOneTprOneP` | n/a | detection r_field T1 glm-5.2 TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTOneTprFive` | n/a | detection r_field T1 glm-5.2 TprFive [n/a: no data yet] |
| `\DetGLMFiveTwoRFieldTOneTprFiveLo` | n/a | detection r_field T1 glm-5.2 TprFive, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTOneTprFiveHi` | n/a | detection r_field T1 glm-5.2 TprFive, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTOneTprFiveCI` | n/a | detection r_field T1 glm-5.2 TprFive, 95% CI |
| `\DetGLMFiveTwoRFieldTOneTprFiveN` | n/a | detection r_field T1 glm-5.2 TprFive, n |
| `\DetGLMFiveTwoRFieldTOneTprFiveP` | n/a | detection r_field T1 glm-5.2 TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTTwo` | n/a | detection r_field T2 qwen3.8-27b AUROC [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoLo` | n/a | detection r_field T2 qwen3.8-27b AUROC, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoHi` | n/a | detection r_field T2 qwen3.8-27b AUROC, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoCI` | n/a | detection r_field T2 qwen3.8-27b AUROC, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoN` | n/a | detection r_field T2 qwen3.8-27b AUROC, n |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoP` | n/a | detection r_field T2 qwen3.8-27b AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprOne` | n/a | detection r_field T2 qwen3.8-27b TprOne [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprOneLo` | n/a | detection r_field T2 qwen3.8-27b TprOne, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprOneHi` | n/a | detection r_field T2 qwen3.8-27b TprOne, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprOneCI` | n/a | detection r_field T2 qwen3.8-27b TprOne, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprOneN` | n/a | detection r_field T2 qwen3.8-27b TprOne, n |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprOneP` | n/a | detection r_field T2 qwen3.8-27b TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprFive` | n/a | detection r_field T2 qwen3.8-27b TprFive [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprFiveLo` | n/a | detection r_field T2 qwen3.8-27b TprFive, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprFiveHi` | n/a | detection r_field T2 qwen3.8-27b TprFive, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprFiveCI` | n/a | detection r_field T2 qwen3.8-27b TprFive, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprFiveN` | n/a | detection r_field T2 qwen3.8-27b TprFive, n |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprFiveP` | n/a | detection r_field T2 qwen3.8-27b TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTTwo` | n/a | detection r_field T2 glm-5.3-flash AUROC [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRFieldTTwoLo` | n/a | detection r_field T2 glm-5.3-flash AUROC, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTTwoHi` | n/a | detection r_field T2 glm-5.3-flash AUROC, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTTwoCI` | n/a | detection r_field T2 glm-5.3-flash AUROC, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTTwoN` | n/a | detection r_field T2 glm-5.3-flash AUROC, n |
| `\DetGLMFiveThreeFlashRFieldTTwoP` | n/a | detection r_field T2 glm-5.3-flash AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTTwoTprOne` | n/a | detection r_field T2 glm-5.3-flash TprOne [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRFieldTTwoTprOneLo` | n/a | detection r_field T2 glm-5.3-flash TprOne, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTTwoTprOneHi` | n/a | detection r_field T2 glm-5.3-flash TprOne, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTTwoTprOneCI` | n/a | detection r_field T2 glm-5.3-flash TprOne, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTTwoTprOneN` | n/a | detection r_field T2 glm-5.3-flash TprOne, n |
| `\DetGLMFiveThreeFlashRFieldTTwoTprOneP` | n/a | detection r_field T2 glm-5.3-flash TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTTwoTprFive` | n/a | detection r_field T2 glm-5.3-flash TprFive [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRFieldTTwoTprFiveLo` | n/a | detection r_field T2 glm-5.3-flash TprFive, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTTwoTprFiveHi` | n/a | detection r_field T2 glm-5.3-flash TprFive, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTTwoTprFiveCI` | n/a | detection r_field T2 glm-5.3-flash TprFive, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTTwoTprFiveN` | n/a | detection r_field T2 glm-5.3-flash TprFive, n |
| `\DetGLMFiveThreeFlashRFieldTTwoTprFiveP` | n/a | detection r_field T2 glm-5.3-flash TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTTwo` | n/a | detection r_field T2 glm-5.2 AUROC [n/a: no data yet] |
| `\DetGLMFiveTwoRFieldTTwoLo` | n/a | detection r_field T2 glm-5.2 AUROC, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTTwoHi` | n/a | detection r_field T2 glm-5.2 AUROC, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTTwoCI` | n/a | detection r_field T2 glm-5.2 AUROC, 95% CI |
| `\DetGLMFiveTwoRFieldTTwoN` | n/a | detection r_field T2 glm-5.2 AUROC, n |
| `\DetGLMFiveTwoRFieldTTwoP` | n/a | detection r_field T2 glm-5.2 AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTTwoTprOne` | n/a | detection r_field T2 glm-5.2 TprOne [n/a: no data yet] |
| `\DetGLMFiveTwoRFieldTTwoTprOneLo` | n/a | detection r_field T2 glm-5.2 TprOne, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTTwoTprOneHi` | n/a | detection r_field T2 glm-5.2 TprOne, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTTwoTprOneCI` | n/a | detection r_field T2 glm-5.2 TprOne, 95% CI |
| `\DetGLMFiveTwoRFieldTTwoTprOneN` | n/a | detection r_field T2 glm-5.2 TprOne, n |
| `\DetGLMFiveTwoRFieldTTwoTprOneP` | n/a | detection r_field T2 glm-5.2 TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTTwoTprFive` | n/a | detection r_field T2 glm-5.2 TprFive [n/a: no data yet] |
| `\DetGLMFiveTwoRFieldTTwoTprFiveLo` | n/a | detection r_field T2 glm-5.2 TprFive, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTTwoTprFiveHi` | n/a | detection r_field T2 glm-5.2 TprFive, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTTwoTprFiveCI` | n/a | detection r_field T2 glm-5.2 TprFive, 95% CI |
| `\DetGLMFiveTwoRFieldTTwoTprFiveN` | n/a | detection r_field T2 glm-5.2 TprFive, n |
| `\DetGLMFiveTwoRFieldTTwoTprFiveP` | n/a | detection r_field T2 glm-5.2 TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTThree` | n/a | detection r_field T3 qwen3.8-27b AUROC [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeLo` | n/a | detection r_field T3 qwen3.8-27b AUROC, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeHi` | n/a | detection r_field T3 qwen3.8-27b AUROC, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeCI` | n/a | detection r_field T3 qwen3.8-27b AUROC, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeN` | n/a | detection r_field T3 qwen3.8-27b AUROC, n |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeP` | n/a | detection r_field T3 qwen3.8-27b AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprOne` | n/a | detection r_field T3 qwen3.8-27b TprOne [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprOneLo` | n/a | detection r_field T3 qwen3.8-27b TprOne, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprOneHi` | n/a | detection r_field T3 qwen3.8-27b TprOne, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprOneCI` | n/a | detection r_field T3 qwen3.8-27b TprOne, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprOneN` | n/a | detection r_field T3 qwen3.8-27b TprOne, n |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprOneP` | n/a | detection r_field T3 qwen3.8-27b TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprFive` | n/a | detection r_field T3 qwen3.8-27b TprFive [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprFiveLo` | n/a | detection r_field T3 qwen3.8-27b TprFive, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprFiveHi` | n/a | detection r_field T3 qwen3.8-27b TprFive, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprFiveCI` | n/a | detection r_field T3 qwen3.8-27b TprFive, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprFiveN` | n/a | detection r_field T3 qwen3.8-27b TprFive, n |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprFiveP` | n/a | detection r_field T3 qwen3.8-27b TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTThree` | n/a | detection r_field T3 glm-5.3-flash AUROC [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRFieldTThreeLo` | n/a | detection r_field T3 glm-5.3-flash AUROC, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTThreeHi` | n/a | detection r_field T3 glm-5.3-flash AUROC, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTThreeCI` | n/a | detection r_field T3 glm-5.3-flash AUROC, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTThreeN` | n/a | detection r_field T3 glm-5.3-flash AUROC, n |
| `\DetGLMFiveThreeFlashRFieldTThreeP` | n/a | detection r_field T3 glm-5.3-flash AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTThreeTprOne` | n/a | detection r_field T3 glm-5.3-flash TprOne [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRFieldTThreeTprOneLo` | n/a | detection r_field T3 glm-5.3-flash TprOne, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTThreeTprOneHi` | n/a | detection r_field T3 glm-5.3-flash TprOne, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTThreeTprOneCI` | n/a | detection r_field T3 glm-5.3-flash TprOne, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTThreeTprOneN` | n/a | detection r_field T3 glm-5.3-flash TprOne, n |
| `\DetGLMFiveThreeFlashRFieldTThreeTprOneP` | n/a | detection r_field T3 glm-5.3-flash TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTThreeTprFive` | n/a | detection r_field T3 glm-5.3-flash TprFive [n/a: no data yet] |
| `\DetGLMFiveThreeFlashRFieldTThreeTprFiveLo` | n/a | detection r_field T3 glm-5.3-flash TprFive, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTThreeTprFiveHi` | n/a | detection r_field T3 glm-5.3-flash TprFive, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTThreeTprFiveCI` | n/a | detection r_field T3 glm-5.3-flash TprFive, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTThreeTprFiveN` | n/a | detection r_field T3 glm-5.3-flash TprFive, n |
| `\DetGLMFiveThreeFlashRFieldTThreeTprFiveP` | n/a | detection r_field T3 glm-5.3-flash TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTThree` | n/a | detection r_field T3 glm-5.2 AUROC [n/a: no data yet] |
| `\DetGLMFiveTwoRFieldTThreeLo` | n/a | detection r_field T3 glm-5.2 AUROC, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTThreeHi` | n/a | detection r_field T3 glm-5.2 AUROC, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTThreeCI` | n/a | detection r_field T3 glm-5.2 AUROC, 95% CI |
| `\DetGLMFiveTwoRFieldTThreeN` | n/a | detection r_field T3 glm-5.2 AUROC, n |
| `\DetGLMFiveTwoRFieldTThreeP` | n/a | detection r_field T3 glm-5.2 AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTThreeTprOne` | n/a | detection r_field T3 glm-5.2 TprOne [n/a: no data yet] |
| `\DetGLMFiveTwoRFieldTThreeTprOneLo` | n/a | detection r_field T3 glm-5.2 TprOne, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTThreeTprOneHi` | n/a | detection r_field T3 glm-5.2 TprOne, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTThreeTprOneCI` | n/a | detection r_field T3 glm-5.2 TprOne, 95% CI |
| `\DetGLMFiveTwoRFieldTThreeTprOneN` | n/a | detection r_field T3 glm-5.2 TprOne, n |
| `\DetGLMFiveTwoRFieldTThreeTprOneP` | n/a | detection r_field T3 glm-5.2 TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTThreeTprFive` | n/a | detection r_field T3 glm-5.2 TprFive [n/a: no data yet] |
| `\DetGLMFiveTwoRFieldTThreeTprFiveLo` | n/a | detection r_field T3 glm-5.2 TprFive, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTThreeTprFiveHi` | n/a | detection r_field T3 glm-5.2 TprFive, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTThreeTprFiveCI` | n/a | detection r_field T3 glm-5.2 TprFive, 95% CI |
| `\DetGLMFiveTwoRFieldTThreeTprFiveN` | n/a | detection r_field T3 glm-5.2 TprFive, n |
| `\DetGLMFiveTwoRFieldTThreeTprFiveP` | n/a | detection r_field T3 glm-5.2 TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTZero` | n/a | detection f_trace T0 qwen3.8-27b AUROC [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroLo` | n/a | detection f_trace T0 qwen3.8-27b AUROC, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroHi` | n/a | detection f_trace T0 qwen3.8-27b AUROC, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroCI` | n/a | detection f_trace T0 qwen3.8-27b AUROC, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroN` | n/a | detection f_trace T0 qwen3.8-27b AUROC, n |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroP` | n/a | detection f_trace T0 qwen3.8-27b AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprOne` | n/a | detection f_trace T0 qwen3.8-27b TprOne [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprOneLo` | n/a | detection f_trace T0 qwen3.8-27b TprOne, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprOneHi` | n/a | detection f_trace T0 qwen3.8-27b TprOne, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprOneCI` | n/a | detection f_trace T0 qwen3.8-27b TprOne, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprOneN` | n/a | detection f_trace T0 qwen3.8-27b TprOne, n |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprOneP` | n/a | detection f_trace T0 qwen3.8-27b TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprFive` | n/a | detection f_trace T0 qwen3.8-27b TprFive [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprFiveLo` | n/a | detection f_trace T0 qwen3.8-27b TprFive, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprFiveHi` | n/a | detection f_trace T0 qwen3.8-27b TprFive, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprFiveCI` | n/a | detection f_trace T0 qwen3.8-27b TprFive, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprFiveN` | n/a | detection f_trace T0 qwen3.8-27b TprFive, n |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprFiveP` | n/a | detection f_trace T0 qwen3.8-27b TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTZero` | n/a | detection f_trace T0 glm-5.3-flash AUROC [n/a: no data yet] |
| `\DetGLMFiveThreeFlashFTraceTZeroLo` | n/a | detection f_trace T0 glm-5.3-flash AUROC, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTZeroHi` | n/a | detection f_trace T0 glm-5.3-flash AUROC, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTZeroCI` | n/a | detection f_trace T0 glm-5.3-flash AUROC, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTZeroN` | n/a | detection f_trace T0 glm-5.3-flash AUROC, n |
| `\DetGLMFiveThreeFlashFTraceTZeroP` | n/a | detection f_trace T0 glm-5.3-flash AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTZeroTprOne` | n/a | detection f_trace T0 glm-5.3-flash TprOne [n/a: no data yet] |
| `\DetGLMFiveThreeFlashFTraceTZeroTprOneLo` | n/a | detection f_trace T0 glm-5.3-flash TprOne, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTZeroTprOneHi` | n/a | detection f_trace T0 glm-5.3-flash TprOne, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTZeroTprOneCI` | n/a | detection f_trace T0 glm-5.3-flash TprOne, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTZeroTprOneN` | n/a | detection f_trace T0 glm-5.3-flash TprOne, n |
| `\DetGLMFiveThreeFlashFTraceTZeroTprOneP` | n/a | detection f_trace T0 glm-5.3-flash TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTZeroTprFive` | n/a | detection f_trace T0 glm-5.3-flash TprFive [n/a: no data yet] |
| `\DetGLMFiveThreeFlashFTraceTZeroTprFiveLo` | n/a | detection f_trace T0 glm-5.3-flash TprFive, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTZeroTprFiveHi` | n/a | detection f_trace T0 glm-5.3-flash TprFive, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTZeroTprFiveCI` | n/a | detection f_trace T0 glm-5.3-flash TprFive, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTZeroTprFiveN` | n/a | detection f_trace T0 glm-5.3-flash TprFive, n |
| `\DetGLMFiveThreeFlashFTraceTZeroTprFiveP` | n/a | detection f_trace T0 glm-5.3-flash TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTZero` | n/a | detection f_trace T0 glm-5.2 AUROC [n/a: no data yet] |
| `\DetGLMFiveTwoFTraceTZeroLo` | n/a | detection f_trace T0 glm-5.2 AUROC, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTZeroHi` | n/a | detection f_trace T0 glm-5.2 AUROC, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTZeroCI` | n/a | detection f_trace T0 glm-5.2 AUROC, 95% CI |
| `\DetGLMFiveTwoFTraceTZeroN` | n/a | detection f_trace T0 glm-5.2 AUROC, n |
| `\DetGLMFiveTwoFTraceTZeroP` | n/a | detection f_trace T0 glm-5.2 AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTZeroTprOne` | n/a | detection f_trace T0 glm-5.2 TprOne [n/a: no data yet] |
| `\DetGLMFiveTwoFTraceTZeroTprOneLo` | n/a | detection f_trace T0 glm-5.2 TprOne, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTZeroTprOneHi` | n/a | detection f_trace T0 glm-5.2 TprOne, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTZeroTprOneCI` | n/a | detection f_trace T0 glm-5.2 TprOne, 95% CI |
| `\DetGLMFiveTwoFTraceTZeroTprOneN` | n/a | detection f_trace T0 glm-5.2 TprOne, n |
| `\DetGLMFiveTwoFTraceTZeroTprOneP` | n/a | detection f_trace T0 glm-5.2 TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTZeroTprFive` | n/a | detection f_trace T0 glm-5.2 TprFive [n/a: no data yet] |
| `\DetGLMFiveTwoFTraceTZeroTprFiveLo` | n/a | detection f_trace T0 glm-5.2 TprFive, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTZeroTprFiveHi` | n/a | detection f_trace T0 glm-5.2 TprFive, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTZeroTprFiveCI` | n/a | detection f_trace T0 glm-5.2 TprFive, 95% CI |
| `\DetGLMFiveTwoFTraceTZeroTprFiveN` | n/a | detection f_trace T0 glm-5.2 TprFive, n |
| `\DetGLMFiveTwoFTraceTZeroTprFiveP` | n/a | detection f_trace T0 glm-5.2 TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTOne` | n/a | detection f_trace T1 qwen3.8-27b AUROC [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBFTraceTOneLo` | n/a | detection f_trace T1 qwen3.8-27b AUROC, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTOneHi` | n/a | detection f_trace T1 qwen3.8-27b AUROC, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTOneCI` | n/a | detection f_trace T1 qwen3.8-27b AUROC, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTOneN` | n/a | detection f_trace T1 qwen3.8-27b AUROC, n |
| `\DetQwenThreeEightTwoSevenBFTraceTOneP` | n/a | detection f_trace T1 qwen3.8-27b AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprOne` | n/a | detection f_trace T1 qwen3.8-27b TprOne [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprOneLo` | n/a | detection f_trace T1 qwen3.8-27b TprOne, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprOneHi` | n/a | detection f_trace T1 qwen3.8-27b TprOne, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprOneCI` | n/a | detection f_trace T1 qwen3.8-27b TprOne, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprOneN` | n/a | detection f_trace T1 qwen3.8-27b TprOne, n |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprOneP` | n/a | detection f_trace T1 qwen3.8-27b TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprFive` | n/a | detection f_trace T1 qwen3.8-27b TprFive [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprFiveLo` | n/a | detection f_trace T1 qwen3.8-27b TprFive, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprFiveHi` | n/a | detection f_trace T1 qwen3.8-27b TprFive, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprFiveCI` | n/a | detection f_trace T1 qwen3.8-27b TprFive, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprFiveN` | n/a | detection f_trace T1 qwen3.8-27b TprFive, n |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprFiveP` | n/a | detection f_trace T1 qwen3.8-27b TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTOne` | n/a | detection f_trace T1 glm-5.3-flash AUROC [n/a: no data yet] |
| `\DetGLMFiveThreeFlashFTraceTOneLo` | n/a | detection f_trace T1 glm-5.3-flash AUROC, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTOneHi` | n/a | detection f_trace T1 glm-5.3-flash AUROC, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTOneCI` | n/a | detection f_trace T1 glm-5.3-flash AUROC, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTOneN` | n/a | detection f_trace T1 glm-5.3-flash AUROC, n |
| `\DetGLMFiveThreeFlashFTraceTOneP` | n/a | detection f_trace T1 glm-5.3-flash AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTOneTprOne` | n/a | detection f_trace T1 glm-5.3-flash TprOne [n/a: no data yet] |
| `\DetGLMFiveThreeFlashFTraceTOneTprOneLo` | n/a | detection f_trace T1 glm-5.3-flash TprOne, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTOneTprOneHi` | n/a | detection f_trace T1 glm-5.3-flash TprOne, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTOneTprOneCI` | n/a | detection f_trace T1 glm-5.3-flash TprOne, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTOneTprOneN` | n/a | detection f_trace T1 glm-5.3-flash TprOne, n |
| `\DetGLMFiveThreeFlashFTraceTOneTprOneP` | n/a | detection f_trace T1 glm-5.3-flash TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTOneTprFive` | n/a | detection f_trace T1 glm-5.3-flash TprFive [n/a: no data yet] |
| `\DetGLMFiveThreeFlashFTraceTOneTprFiveLo` | n/a | detection f_trace T1 glm-5.3-flash TprFive, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTOneTprFiveHi` | n/a | detection f_trace T1 glm-5.3-flash TprFive, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTOneTprFiveCI` | n/a | detection f_trace T1 glm-5.3-flash TprFive, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTOneTprFiveN` | n/a | detection f_trace T1 glm-5.3-flash TprFive, n |
| `\DetGLMFiveThreeFlashFTraceTOneTprFiveP` | n/a | detection f_trace T1 glm-5.3-flash TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTOne` | n/a | detection f_trace T1 glm-5.2 AUROC [n/a: no data yet] |
| `\DetGLMFiveTwoFTraceTOneLo` | n/a | detection f_trace T1 glm-5.2 AUROC, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTOneHi` | n/a | detection f_trace T1 glm-5.2 AUROC, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTOneCI` | n/a | detection f_trace T1 glm-5.2 AUROC, 95% CI |
| `\DetGLMFiveTwoFTraceTOneN` | n/a | detection f_trace T1 glm-5.2 AUROC, n |
| `\DetGLMFiveTwoFTraceTOneP` | n/a | detection f_trace T1 glm-5.2 AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTOneTprOne` | n/a | detection f_trace T1 glm-5.2 TprOne [n/a: no data yet] |
| `\DetGLMFiveTwoFTraceTOneTprOneLo` | n/a | detection f_trace T1 glm-5.2 TprOne, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTOneTprOneHi` | n/a | detection f_trace T1 glm-5.2 TprOne, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTOneTprOneCI` | n/a | detection f_trace T1 glm-5.2 TprOne, 95% CI |
| `\DetGLMFiveTwoFTraceTOneTprOneN` | n/a | detection f_trace T1 glm-5.2 TprOne, n |
| `\DetGLMFiveTwoFTraceTOneTprOneP` | n/a | detection f_trace T1 glm-5.2 TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTOneTprFive` | n/a | detection f_trace T1 glm-5.2 TprFive [n/a: no data yet] |
| `\DetGLMFiveTwoFTraceTOneTprFiveLo` | n/a | detection f_trace T1 glm-5.2 TprFive, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTOneTprFiveHi` | n/a | detection f_trace T1 glm-5.2 TprFive, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTOneTprFiveCI` | n/a | detection f_trace T1 glm-5.2 TprFive, 95% CI |
| `\DetGLMFiveTwoFTraceTOneTprFiveN` | n/a | detection f_trace T1 glm-5.2 TprFive, n |
| `\DetGLMFiveTwoFTraceTOneTprFiveP` | n/a | detection f_trace T1 glm-5.2 TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTTwo` | n/a | detection f_trace T2 qwen3.8-27b AUROC [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoLo` | n/a | detection f_trace T2 qwen3.8-27b AUROC, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoHi` | n/a | detection f_trace T2 qwen3.8-27b AUROC, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoCI` | n/a | detection f_trace T2 qwen3.8-27b AUROC, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoN` | n/a | detection f_trace T2 qwen3.8-27b AUROC, n |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoP` | n/a | detection f_trace T2 qwen3.8-27b AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprOne` | n/a | detection f_trace T2 qwen3.8-27b TprOne [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprOneLo` | n/a | detection f_trace T2 qwen3.8-27b TprOne, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprOneHi` | n/a | detection f_trace T2 qwen3.8-27b TprOne, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprOneCI` | n/a | detection f_trace T2 qwen3.8-27b TprOne, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprOneN` | n/a | detection f_trace T2 qwen3.8-27b TprOne, n |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprOneP` | n/a | detection f_trace T2 qwen3.8-27b TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprFive` | n/a | detection f_trace T2 qwen3.8-27b TprFive [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprFiveLo` | n/a | detection f_trace T2 qwen3.8-27b TprFive, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprFiveHi` | n/a | detection f_trace T2 qwen3.8-27b TprFive, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprFiveCI` | n/a | detection f_trace T2 qwen3.8-27b TprFive, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprFiveN` | n/a | detection f_trace T2 qwen3.8-27b TprFive, n |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprFiveP` | n/a | detection f_trace T2 qwen3.8-27b TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTTwo` | n/a | detection f_trace T2 glm-5.3-flash AUROC [n/a: no data yet] |
| `\DetGLMFiveThreeFlashFTraceTTwoLo` | n/a | detection f_trace T2 glm-5.3-flash AUROC, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTTwoHi` | n/a | detection f_trace T2 glm-5.3-flash AUROC, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTTwoCI` | n/a | detection f_trace T2 glm-5.3-flash AUROC, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTTwoN` | n/a | detection f_trace T2 glm-5.3-flash AUROC, n |
| `\DetGLMFiveThreeFlashFTraceTTwoP` | n/a | detection f_trace T2 glm-5.3-flash AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTTwoTprOne` | n/a | detection f_trace T2 glm-5.3-flash TprOne [n/a: no data yet] |
| `\DetGLMFiveThreeFlashFTraceTTwoTprOneLo` | n/a | detection f_trace T2 glm-5.3-flash TprOne, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTTwoTprOneHi` | n/a | detection f_trace T2 glm-5.3-flash TprOne, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTTwoTprOneCI` | n/a | detection f_trace T2 glm-5.3-flash TprOne, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTTwoTprOneN` | n/a | detection f_trace T2 glm-5.3-flash TprOne, n |
| `\DetGLMFiveThreeFlashFTraceTTwoTprOneP` | n/a | detection f_trace T2 glm-5.3-flash TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTTwoTprFive` | n/a | detection f_trace T2 glm-5.3-flash TprFive [n/a: no data yet] |
| `\DetGLMFiveThreeFlashFTraceTTwoTprFiveLo` | n/a | detection f_trace T2 glm-5.3-flash TprFive, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTTwoTprFiveHi` | n/a | detection f_trace T2 glm-5.3-flash TprFive, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTTwoTprFiveCI` | n/a | detection f_trace T2 glm-5.3-flash TprFive, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTTwoTprFiveN` | n/a | detection f_trace T2 glm-5.3-flash TprFive, n |
| `\DetGLMFiveThreeFlashFTraceTTwoTprFiveP` | n/a | detection f_trace T2 glm-5.3-flash TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTTwo` | n/a | detection f_trace T2 glm-5.2 AUROC [n/a: no data yet] |
| `\DetGLMFiveTwoFTraceTTwoLo` | n/a | detection f_trace T2 glm-5.2 AUROC, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTTwoHi` | n/a | detection f_trace T2 glm-5.2 AUROC, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTTwoCI` | n/a | detection f_trace T2 glm-5.2 AUROC, 95% CI |
| `\DetGLMFiveTwoFTraceTTwoN` | n/a | detection f_trace T2 glm-5.2 AUROC, n |
| `\DetGLMFiveTwoFTraceTTwoP` | n/a | detection f_trace T2 glm-5.2 AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTTwoTprOne` | n/a | detection f_trace T2 glm-5.2 TprOne [n/a: no data yet] |
| `\DetGLMFiveTwoFTraceTTwoTprOneLo` | n/a | detection f_trace T2 glm-5.2 TprOne, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTTwoTprOneHi` | n/a | detection f_trace T2 glm-5.2 TprOne, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTTwoTprOneCI` | n/a | detection f_trace T2 glm-5.2 TprOne, 95% CI |
| `\DetGLMFiveTwoFTraceTTwoTprOneN` | n/a | detection f_trace T2 glm-5.2 TprOne, n |
| `\DetGLMFiveTwoFTraceTTwoTprOneP` | n/a | detection f_trace T2 glm-5.2 TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTTwoTprFive` | n/a | detection f_trace T2 glm-5.2 TprFive [n/a: no data yet] |
| `\DetGLMFiveTwoFTraceTTwoTprFiveLo` | n/a | detection f_trace T2 glm-5.2 TprFive, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTTwoTprFiveHi` | n/a | detection f_trace T2 glm-5.2 TprFive, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTTwoTprFiveCI` | n/a | detection f_trace T2 glm-5.2 TprFive, 95% CI |
| `\DetGLMFiveTwoFTraceTTwoTprFiveN` | n/a | detection f_trace T2 glm-5.2 TprFive, n |
| `\DetGLMFiveTwoFTraceTTwoTprFiveP` | n/a | detection f_trace T2 glm-5.2 TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTThree` | n/a | detection f_trace T3 qwen3.8-27b AUROC [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeLo` | n/a | detection f_trace T3 qwen3.8-27b AUROC, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeHi` | n/a | detection f_trace T3 qwen3.8-27b AUROC, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeCI` | n/a | detection f_trace T3 qwen3.8-27b AUROC, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeN` | n/a | detection f_trace T3 qwen3.8-27b AUROC, n |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeP` | n/a | detection f_trace T3 qwen3.8-27b AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprOne` | n/a | detection f_trace T3 qwen3.8-27b TprOne [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprOneLo` | n/a | detection f_trace T3 qwen3.8-27b TprOne, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprOneHi` | n/a | detection f_trace T3 qwen3.8-27b TprOne, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprOneCI` | n/a | detection f_trace T3 qwen3.8-27b TprOne, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprOneN` | n/a | detection f_trace T3 qwen3.8-27b TprOne, n |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprOneP` | n/a | detection f_trace T3 qwen3.8-27b TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprFive` | n/a | detection f_trace T3 qwen3.8-27b TprFive [n/a: no data yet] |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprFiveLo` | n/a | detection f_trace T3 qwen3.8-27b TprFive, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprFiveHi` | n/a | detection f_trace T3 qwen3.8-27b TprFive, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprFiveCI` | n/a | detection f_trace T3 qwen3.8-27b TprFive, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprFiveN` | n/a | detection f_trace T3 qwen3.8-27b TprFive, n |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprFiveP` | n/a | detection f_trace T3 qwen3.8-27b TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTThree` | n/a | detection f_trace T3 glm-5.3-flash AUROC [n/a: no data yet] |
| `\DetGLMFiveThreeFlashFTraceTThreeLo` | n/a | detection f_trace T3 glm-5.3-flash AUROC, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTThreeHi` | n/a | detection f_trace T3 glm-5.3-flash AUROC, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTThreeCI` | n/a | detection f_trace T3 glm-5.3-flash AUROC, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTThreeN` | n/a | detection f_trace T3 glm-5.3-flash AUROC, n |
| `\DetGLMFiveThreeFlashFTraceTThreeP` | n/a | detection f_trace T3 glm-5.3-flash AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTThreeTprOne` | n/a | detection f_trace T3 glm-5.3-flash TprOne [n/a: no data yet] |
| `\DetGLMFiveThreeFlashFTraceTThreeTprOneLo` | n/a | detection f_trace T3 glm-5.3-flash TprOne, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTThreeTprOneHi` | n/a | detection f_trace T3 glm-5.3-flash TprOne, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTThreeTprOneCI` | n/a | detection f_trace T3 glm-5.3-flash TprOne, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTThreeTprOneN` | n/a | detection f_trace T3 glm-5.3-flash TprOne, n |
| `\DetGLMFiveThreeFlashFTraceTThreeTprOneP` | n/a | detection f_trace T3 glm-5.3-flash TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTThreeTprFive` | n/a | detection f_trace T3 glm-5.3-flash TprFive [n/a: no data yet] |
| `\DetGLMFiveThreeFlashFTraceTThreeTprFiveLo` | n/a | detection f_trace T3 glm-5.3-flash TprFive, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTThreeTprFiveHi` | n/a | detection f_trace T3 glm-5.3-flash TprFive, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTThreeTprFiveCI` | n/a | detection f_trace T3 glm-5.3-flash TprFive, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTThreeTprFiveN` | n/a | detection f_trace T3 glm-5.3-flash TprFive, n |
| `\DetGLMFiveThreeFlashFTraceTThreeTprFiveP` | n/a | detection f_trace T3 glm-5.3-flash TprFive, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTThree` | n/a | detection f_trace T3 glm-5.2 AUROC [n/a: no data yet] |
| `\DetGLMFiveTwoFTraceTThreeLo` | n/a | detection f_trace T3 glm-5.2 AUROC, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTThreeHi` | n/a | detection f_trace T3 glm-5.2 AUROC, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTThreeCI` | n/a | detection f_trace T3 glm-5.2 AUROC, 95% CI |
| `\DetGLMFiveTwoFTraceTThreeN` | n/a | detection f_trace T3 glm-5.2 AUROC, n |
| `\DetGLMFiveTwoFTraceTThreeP` | n/a | detection f_trace T3 glm-5.2 AUROC, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTThreeTprOne` | n/a | detection f_trace T3 glm-5.2 TprOne [n/a: no data yet] |
| `\DetGLMFiveTwoFTraceTThreeTprOneLo` | n/a | detection f_trace T3 glm-5.2 TprOne, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTThreeTprOneHi` | n/a | detection f_trace T3 glm-5.2 TprOne, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTThreeTprOneCI` | n/a | detection f_trace T3 glm-5.2 TprOne, 95% CI |
| `\DetGLMFiveTwoFTraceTThreeTprOneN` | n/a | detection f_trace T3 glm-5.2 TprOne, n |
| `\DetGLMFiveTwoFTraceTThreeTprOneP` | n/a | detection f_trace T3 glm-5.2 TprOne, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTThreeTprFive` | n/a | detection f_trace T3 glm-5.2 TprFive [n/a: no data yet] |
| `\DetGLMFiveTwoFTraceTThreeTprFiveLo` | n/a | detection f_trace T3 glm-5.2 TprFive, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTThreeTprFiveHi` | n/a | detection f_trace T3 glm-5.2 TprFive, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTThreeTprFiveCI` | n/a | detection f_trace T3 glm-5.2 TprFive, 95% CI |
| `\DetGLMFiveTwoFTraceTThreeTprFiveN` | n/a | detection f_trace T3 glm-5.2 TprFive, n |
| `\DetGLMFiveTwoFTraceTThreeTprFiveP` | n/a | detection f_trace T3 glm-5.2 TprFive, two-sided bootstrap p (n/a if not tested) |
| `\GateDeepSeekVFourFlashCleanFlag` | n/a | gate CleanFlag deepseek-v4-flash [n/a: no data yet] |
| `\GateDeepSeekVFourFlashCleanFlagLo` | n/a | gate CleanFlag deepseek-v4-flash, lower 95% CI bound |
| `\GateDeepSeekVFourFlashCleanFlagHi` | n/a | gate CleanFlag deepseek-v4-flash, upper 95% CI bound |
| `\GateDeepSeekVFourFlashCleanFlagCI` | n/a | gate CleanFlag deepseek-v4-flash, 95% CI |
| `\GateDeepSeekVFourFlashCleanFlagN` | n/a | gate CleanFlag deepseek-v4-flash, n |
| `\GateDeepSeekVFourFlashCleanFlagP` | n/a | gate CleanFlag deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\GateDeepSeekVFourFlashTargetFlag` | n/a | gate TargetFlag deepseek-v4-flash [n/a: no data yet] |
| `\GateDeepSeekVFourFlashTargetFlagLo` | n/a | gate TargetFlag deepseek-v4-flash, lower 95% CI bound |
| `\GateDeepSeekVFourFlashTargetFlagHi` | n/a | gate TargetFlag deepseek-v4-flash, upper 95% CI bound |
| `\GateDeepSeekVFourFlashTargetFlagCI` | n/a | gate TargetFlag deepseek-v4-flash, 95% CI |
| `\GateDeepSeekVFourFlashTargetFlagN` | n/a | gate TargetFlag deepseek-v4-flash, n |
| `\GateDeepSeekVFourFlashTargetFlagP` | n/a | gate TargetFlag deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\NegsQwenThreeEightTwoSevenBOtherEpisode` | n/a | matched negatives other_episode qwen3.8-27b [n/a: no data yet] |
| `\NegsQwenThreeEightTwoSevenBOtherEpisodeLo` | n/a | matched negatives other_episode qwen3.8-27b, lower 95% CI bound |
| `\NegsQwenThreeEightTwoSevenBOtherEpisodeHi` | n/a | matched negatives other_episode qwen3.8-27b, upper 95% CI bound |
| `\NegsQwenThreeEightTwoSevenBOtherEpisodeCI` | n/a | matched negatives other_episode qwen3.8-27b, 95% CI |
| `\NegsQwenThreeEightTwoSevenBOtherEpisodeN` | n/a | matched negatives other_episode qwen3.8-27b, n |
| `\NegsQwenThreeEightTwoSevenBOtherEpisodeP` | n/a | matched negatives other_episode qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\NegsQwenThreeEightTwoSevenBOtherModel` | n/a | matched negatives other_model qwen3.8-27b [n/a: no data yet] |
| `\NegsQwenThreeEightTwoSevenBOtherModelLo` | n/a | matched negatives other_model qwen3.8-27b, lower 95% CI bound |
| `\NegsQwenThreeEightTwoSevenBOtherModelHi` | n/a | matched negatives other_model qwen3.8-27b, upper 95% CI bound |
| `\NegsQwenThreeEightTwoSevenBOtherModelCI` | n/a | matched negatives other_model qwen3.8-27b, 95% CI |
| `\NegsQwenThreeEightTwoSevenBOtherModelN` | n/a | matched negatives other_model qwen3.8-27b, n |
| `\NegsQwenThreeEightTwoSevenBOtherModelP` | n/a | matched negatives other_model qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\ValidQwenThreeEightTwoSevenBTZero` | n/a | % valid forgeries T0 qwen3.8-27b [n/a: no data yet] |
| `\ValidQwenThreeEightTwoSevenBTZeroLo` | n/a | % valid forgeries T0 qwen3.8-27b, lower 95% CI bound |
| `\ValidQwenThreeEightTwoSevenBTZeroHi` | n/a | % valid forgeries T0 qwen3.8-27b, upper 95% CI bound |
| `\ValidQwenThreeEightTwoSevenBTZeroCI` | n/a | % valid forgeries T0 qwen3.8-27b, 95% CI |
| `\ValidQwenThreeEightTwoSevenBTZeroN` | n/a | % valid forgeries T0 qwen3.8-27b, n |
| `\ValidQwenThreeEightTwoSevenBTZeroP` | n/a | % valid forgeries T0 qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\ValidQwenThreeEightTwoSevenBTOne` | n/a | % valid forgeries T1 qwen3.8-27b [n/a: no data yet] |
| `\ValidQwenThreeEightTwoSevenBTOneLo` | n/a | % valid forgeries T1 qwen3.8-27b, lower 95% CI bound |
| `\ValidQwenThreeEightTwoSevenBTOneHi` | n/a | % valid forgeries T1 qwen3.8-27b, upper 95% CI bound |
| `\ValidQwenThreeEightTwoSevenBTOneCI` | n/a | % valid forgeries T1 qwen3.8-27b, 95% CI |
| `\ValidQwenThreeEightTwoSevenBTOneN` | n/a | % valid forgeries T1 qwen3.8-27b, n |
| `\ValidQwenThreeEightTwoSevenBTOneP` | n/a | % valid forgeries T1 qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\ValidQwenThreeEightTwoSevenBTTwo` | n/a | % valid forgeries T2 qwen3.8-27b [n/a: no data yet] |
| `\ValidQwenThreeEightTwoSevenBTTwoLo` | n/a | % valid forgeries T2 qwen3.8-27b, lower 95% CI bound |
| `\ValidQwenThreeEightTwoSevenBTTwoHi` | n/a | % valid forgeries T2 qwen3.8-27b, upper 95% CI bound |
| `\ValidQwenThreeEightTwoSevenBTTwoCI` | n/a | % valid forgeries T2 qwen3.8-27b, 95% CI |
| `\ValidQwenThreeEightTwoSevenBTTwoN` | n/a | % valid forgeries T2 qwen3.8-27b, n |
| `\ValidQwenThreeEightTwoSevenBTTwoP` | n/a | % valid forgeries T2 qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\ValidQwenThreeEightTwoSevenBTThree` | n/a | % valid forgeries T3 qwen3.8-27b [n/a: no data yet] |
| `\ValidQwenThreeEightTwoSevenBTThreeLo` | n/a | % valid forgeries T3 qwen3.8-27b, lower 95% CI bound |
| `\ValidQwenThreeEightTwoSevenBTThreeHi` | n/a | % valid forgeries T3 qwen3.8-27b, upper 95% CI bound |
| `\ValidQwenThreeEightTwoSevenBTThreeCI` | n/a | % valid forgeries T3 qwen3.8-27b, 95% CI |
| `\ValidQwenThreeEightTwoSevenBTThreeN` | n/a | % valid forgeries T3 qwen3.8-27b, n |
| `\ValidQwenThreeEightTwoSevenBTThreeP` | n/a | % valid forgeries T3 qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\TthreeQwenThreeEightTwoSevenBFirstSelected` | n/a | T3 first-shown selected qwen3.8-27b [n/a: no data yet] |
| `\TthreeQwenThreeEightTwoSevenBFirstSelectedLo` | n/a | T3 first-shown selected qwen3.8-27b, lower 95% CI bound |
| `\TthreeQwenThreeEightTwoSevenBFirstSelectedHi` | n/a | T3 first-shown selected qwen3.8-27b, upper 95% CI bound |
| `\TthreeQwenThreeEightTwoSevenBFirstSelectedCI` | n/a | T3 first-shown selected qwen3.8-27b, 95% CI |
| `\TthreeQwenThreeEightTwoSevenBFirstSelectedN` | n/a | T3 first-shown selected qwen3.8-27b, n |
| `\TthreeQwenThreeEightTwoSevenBFirstSelectedP` | n/a | T3 first-shown selected qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\TthreeQwenThreeEightTwoSevenBFirstTop` | n/a | T3 first-shown top-rated qwen3.8-27b [n/a: no data yet] |
| `\TthreeQwenThreeEightTwoSevenBFirstTopLo` | n/a | T3 first-shown top-rated qwen3.8-27b, lower 95% CI bound |
| `\TthreeQwenThreeEightTwoSevenBFirstTopHi` | n/a | T3 first-shown top-rated qwen3.8-27b, upper 95% CI bound |
| `\TthreeQwenThreeEightTwoSevenBFirstTopCI` | n/a | T3 first-shown top-rated qwen3.8-27b, 95% CI |
| `\TthreeQwenThreeEightTwoSevenBFirstTopN` | n/a | T3 first-shown top-rated qwen3.8-27b, n |
| `\TthreeQwenThreeEightTwoSevenBFirstTopP` | n/a | T3 first-shown top-rated qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\TthreeQwenThreeEightTwoSevenBChance` | n/a | T3 chance level qwen3.8-27b [n/a: no data yet] |
| `\GateQwenThreeEightTwoSevenBDetector` | n/a | gate Detector qwen3.8-27b [n/a: no data yet] |
| `\GateQwenThreeEightTwoSevenBFprCalib` | n/a | gate FprCalib qwen3.8-27b [n/a: no data yet] |
| `\GateQwenThreeEightTwoSevenBCallsPerRead` | n/a | gate CallsPerRead qwen3.8-27b [n/a: no data yet] |
| `\GateQwenThreeEightTwoSevenBCleanFlag` | n/a | gate CleanFlag qwen3.8-27b [n/a: no data yet] |
| `\GateQwenThreeEightTwoSevenBCleanFlagLo` | n/a | gate CleanFlag qwen3.8-27b, lower 95% CI bound |
| `\GateQwenThreeEightTwoSevenBCleanFlagHi` | n/a | gate CleanFlag qwen3.8-27b, upper 95% CI bound |
| `\GateQwenThreeEightTwoSevenBCleanFlagCI` | n/a | gate CleanFlag qwen3.8-27b, 95% CI |
| `\GateQwenThreeEightTwoSevenBCleanFlagN` | n/a | gate CleanFlag qwen3.8-27b, n |
| `\GateQwenThreeEightTwoSevenBCleanFlagP` | n/a | gate CleanFlag qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\GateQwenThreeEightTwoSevenBTargetFlag` | n/a | gate TargetFlag qwen3.8-27b [n/a: no data yet] |
| `\GateQwenThreeEightTwoSevenBTargetFlagLo` | n/a | gate TargetFlag qwen3.8-27b, lower 95% CI bound |
| `\GateQwenThreeEightTwoSevenBTargetFlagHi` | n/a | gate TargetFlag qwen3.8-27b, upper 95% CI bound |
| `\GateQwenThreeEightTwoSevenBTargetFlagCI` | n/a | gate TargetFlag qwen3.8-27b, 95% CI |
| `\GateQwenThreeEightTwoSevenBTargetFlagN` | n/a | gate TargetFlag qwen3.8-27b, n |
| `\GateQwenThreeEightTwoSevenBTargetFlagP` | n/a | gate TargetFlag qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\GateGemmaFourThreeOneBCleanFlag` | n/a | gate CleanFlag gemma-4-31b-it [n/a: no data yet] |
| `\GateGemmaFourThreeOneBCleanFlagLo` | n/a | gate CleanFlag gemma-4-31b-it, lower 95% CI bound |
| `\GateGemmaFourThreeOneBCleanFlagHi` | n/a | gate CleanFlag gemma-4-31b-it, upper 95% CI bound |
| `\GateGemmaFourThreeOneBCleanFlagCI` | n/a | gate CleanFlag gemma-4-31b-it, 95% CI |
| `\GateGemmaFourThreeOneBCleanFlagN` | n/a | gate CleanFlag gemma-4-31b-it, n |
| `\GateGemmaFourThreeOneBCleanFlagP` | n/a | gate CleanFlag gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\GateGemmaFourThreeOneBTargetFlag` | n/a | gate TargetFlag gemma-4-31b-it [n/a: no data yet] |
| `\GateGemmaFourThreeOneBTargetFlagLo` | n/a | gate TargetFlag gemma-4-31b-it, lower 95% CI bound |
| `\GateGemmaFourThreeOneBTargetFlagHi` | n/a | gate TargetFlag gemma-4-31b-it, upper 95% CI bound |
| `\GateGemmaFourThreeOneBTargetFlagCI` | n/a | gate TargetFlag gemma-4-31b-it, 95% CI |
| `\GateGemmaFourThreeOneBTargetFlagN` | n/a | gate TargetFlag gemma-4-31b-it, n |
| `\GateGemmaFourThreeOneBTargetFlagP` | n/a | gate TargetFlag gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\NegsGLMFiveThreeFlashOtherEpisode` | n/a | matched negatives other_episode glm-5.3-flash [n/a: no data yet] |
| `\NegsGLMFiveThreeFlashOtherEpisodeLo` | n/a | matched negatives other_episode glm-5.3-flash, lower 95% CI bound |
| `\NegsGLMFiveThreeFlashOtherEpisodeHi` | n/a | matched negatives other_episode glm-5.3-flash, upper 95% CI bound |
| `\NegsGLMFiveThreeFlashOtherEpisodeCI` | n/a | matched negatives other_episode glm-5.3-flash, 95% CI |
| `\NegsGLMFiveThreeFlashOtherEpisodeN` | n/a | matched negatives other_episode glm-5.3-flash, n |
| `\NegsGLMFiveThreeFlashOtherEpisodeP` | n/a | matched negatives other_episode glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\NegsGLMFiveThreeFlashOtherModel` | n/a | matched negatives other_model glm-5.3-flash [n/a: no data yet] |
| `\NegsGLMFiveThreeFlashOtherModelLo` | n/a | matched negatives other_model glm-5.3-flash, lower 95% CI bound |
| `\NegsGLMFiveThreeFlashOtherModelHi` | n/a | matched negatives other_model glm-5.3-flash, upper 95% CI bound |
| `\NegsGLMFiveThreeFlashOtherModelCI` | n/a | matched negatives other_model glm-5.3-flash, 95% CI |
| `\NegsGLMFiveThreeFlashOtherModelN` | n/a | matched negatives other_model glm-5.3-flash, n |
| `\NegsGLMFiveThreeFlashOtherModelP` | n/a | matched negatives other_model glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\ValidGLMFiveThreeFlashTZero` | n/a | % valid forgeries T0 glm-5.3-flash [n/a: no data yet] |
| `\ValidGLMFiveThreeFlashTZeroLo` | n/a | % valid forgeries T0 glm-5.3-flash, lower 95% CI bound |
| `\ValidGLMFiveThreeFlashTZeroHi` | n/a | % valid forgeries T0 glm-5.3-flash, upper 95% CI bound |
| `\ValidGLMFiveThreeFlashTZeroCI` | n/a | % valid forgeries T0 glm-5.3-flash, 95% CI |
| `\ValidGLMFiveThreeFlashTZeroN` | n/a | % valid forgeries T0 glm-5.3-flash, n |
| `\ValidGLMFiveThreeFlashTZeroP` | n/a | % valid forgeries T0 glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\ValidGLMFiveThreeFlashTOne` | n/a | % valid forgeries T1 glm-5.3-flash [n/a: no data yet] |
| `\ValidGLMFiveThreeFlashTOneLo` | n/a | % valid forgeries T1 glm-5.3-flash, lower 95% CI bound |
| `\ValidGLMFiveThreeFlashTOneHi` | n/a | % valid forgeries T1 glm-5.3-flash, upper 95% CI bound |
| `\ValidGLMFiveThreeFlashTOneCI` | n/a | % valid forgeries T1 glm-5.3-flash, 95% CI |
| `\ValidGLMFiveThreeFlashTOneN` | n/a | % valid forgeries T1 glm-5.3-flash, n |
| `\ValidGLMFiveThreeFlashTOneP` | n/a | % valid forgeries T1 glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\ValidGLMFiveThreeFlashTTwo` | n/a | % valid forgeries T2 glm-5.3-flash [n/a: no data yet] |
| `\ValidGLMFiveThreeFlashTTwoLo` | n/a | % valid forgeries T2 glm-5.3-flash, lower 95% CI bound |
| `\ValidGLMFiveThreeFlashTTwoHi` | n/a | % valid forgeries T2 glm-5.3-flash, upper 95% CI bound |
| `\ValidGLMFiveThreeFlashTTwoCI` | n/a | % valid forgeries T2 glm-5.3-flash, 95% CI |
| `\ValidGLMFiveThreeFlashTTwoN` | n/a | % valid forgeries T2 glm-5.3-flash, n |
| `\ValidGLMFiveThreeFlashTTwoP` | n/a | % valid forgeries T2 glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\ValidGLMFiveThreeFlashTThree` | n/a | % valid forgeries T3 glm-5.3-flash [n/a: no data yet] |
| `\ValidGLMFiveThreeFlashTThreeLo` | n/a | % valid forgeries T3 glm-5.3-flash, lower 95% CI bound |
| `\ValidGLMFiveThreeFlashTThreeHi` | n/a | % valid forgeries T3 glm-5.3-flash, upper 95% CI bound |
| `\ValidGLMFiveThreeFlashTThreeCI` | n/a | % valid forgeries T3 glm-5.3-flash, 95% CI |
| `\ValidGLMFiveThreeFlashTThreeN` | n/a | % valid forgeries T3 glm-5.3-flash, n |
| `\ValidGLMFiveThreeFlashTThreeP` | n/a | % valid forgeries T3 glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\TthreeGLMFiveThreeFlashFirstSelected` | n/a | T3 first-shown selected glm-5.3-flash [n/a: no data yet] |
| `\TthreeGLMFiveThreeFlashFirstSelectedLo` | n/a | T3 first-shown selected glm-5.3-flash, lower 95% CI bound |
| `\TthreeGLMFiveThreeFlashFirstSelectedHi` | n/a | T3 first-shown selected glm-5.3-flash, upper 95% CI bound |
| `\TthreeGLMFiveThreeFlashFirstSelectedCI` | n/a | T3 first-shown selected glm-5.3-flash, 95% CI |
| `\TthreeGLMFiveThreeFlashFirstSelectedN` | n/a | T3 first-shown selected glm-5.3-flash, n |
| `\TthreeGLMFiveThreeFlashFirstSelectedP` | n/a | T3 first-shown selected glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\TthreeGLMFiveThreeFlashFirstTop` | n/a | T3 first-shown top-rated glm-5.3-flash [n/a: no data yet] |
| `\TthreeGLMFiveThreeFlashFirstTopLo` | n/a | T3 first-shown top-rated glm-5.3-flash, lower 95% CI bound |
| `\TthreeGLMFiveThreeFlashFirstTopHi` | n/a | T3 first-shown top-rated glm-5.3-flash, upper 95% CI bound |
| `\TthreeGLMFiveThreeFlashFirstTopCI` | n/a | T3 first-shown top-rated glm-5.3-flash, 95% CI |
| `\TthreeGLMFiveThreeFlashFirstTopN` | n/a | T3 first-shown top-rated glm-5.3-flash, n |
| `\TthreeGLMFiveThreeFlashFirstTopP` | n/a | T3 first-shown top-rated glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\TthreeGLMFiveThreeFlashChance` | n/a | T3 chance level glm-5.3-flash [n/a: no data yet] |
| `\GateGLMFiveThreeFlashDetector` | n/a | gate Detector glm-5.3-flash [n/a: no data yet] |
| `\GateGLMFiveThreeFlashFprCalib` | n/a | gate FprCalib glm-5.3-flash [n/a: no data yet] |
| `\GateGLMFiveThreeFlashCallsPerRead` | n/a | gate CallsPerRead glm-5.3-flash [n/a: no data yet] |
| `\GateGLMFiveThreeFlashCleanFlag` | n/a | gate CleanFlag glm-5.3-flash [n/a: no data yet] |
| `\GateGLMFiveThreeFlashCleanFlagLo` | n/a | gate CleanFlag glm-5.3-flash, lower 95% CI bound |
| `\GateGLMFiveThreeFlashCleanFlagHi` | n/a | gate CleanFlag glm-5.3-flash, upper 95% CI bound |
| `\GateGLMFiveThreeFlashCleanFlagCI` | n/a | gate CleanFlag glm-5.3-flash, 95% CI |
| `\GateGLMFiveThreeFlashCleanFlagN` | n/a | gate CleanFlag glm-5.3-flash, n |
| `\GateGLMFiveThreeFlashCleanFlagP` | n/a | gate CleanFlag glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\GateGLMFiveThreeFlashTargetFlag` | n/a | gate TargetFlag glm-5.3-flash [n/a: no data yet] |
| `\GateGLMFiveThreeFlashTargetFlagLo` | n/a | gate TargetFlag glm-5.3-flash, lower 95% CI bound |
| `\GateGLMFiveThreeFlashTargetFlagHi` | n/a | gate TargetFlag glm-5.3-flash, upper 95% CI bound |
| `\GateGLMFiveThreeFlashTargetFlagCI` | n/a | gate TargetFlag glm-5.3-flash, 95% CI |
| `\GateGLMFiveThreeFlashTargetFlagN` | n/a | gate TargetFlag glm-5.3-flash, n |
| `\GateGLMFiveThreeFlashTargetFlagP` | n/a | gate TargetFlag glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\NegsGLMFiveTwoOtherEpisode` | n/a | matched negatives other_episode glm-5.2 [n/a: no data yet] |
| `\NegsGLMFiveTwoOtherEpisodeLo` | n/a | matched negatives other_episode glm-5.2, lower 95% CI bound |
| `\NegsGLMFiveTwoOtherEpisodeHi` | n/a | matched negatives other_episode glm-5.2, upper 95% CI bound |
| `\NegsGLMFiveTwoOtherEpisodeCI` | n/a | matched negatives other_episode glm-5.2, 95% CI |
| `\NegsGLMFiveTwoOtherEpisodeN` | n/a | matched negatives other_episode glm-5.2, n |
| `\NegsGLMFiveTwoOtherEpisodeP` | n/a | matched negatives other_episode glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\NegsGLMFiveTwoOtherModel` | n/a | matched negatives other_model glm-5.2 [n/a: no data yet] |
| `\NegsGLMFiveTwoOtherModelLo` | n/a | matched negatives other_model glm-5.2, lower 95% CI bound |
| `\NegsGLMFiveTwoOtherModelHi` | n/a | matched negatives other_model glm-5.2, upper 95% CI bound |
| `\NegsGLMFiveTwoOtherModelCI` | n/a | matched negatives other_model glm-5.2, 95% CI |
| `\NegsGLMFiveTwoOtherModelN` | n/a | matched negatives other_model glm-5.2, n |
| `\NegsGLMFiveTwoOtherModelP` | n/a | matched negatives other_model glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\ValidGLMFiveTwoTZero` | n/a | % valid forgeries T0 glm-5.2 [n/a: no data yet] |
| `\ValidGLMFiveTwoTZeroLo` | n/a | % valid forgeries T0 glm-5.2, lower 95% CI bound |
| `\ValidGLMFiveTwoTZeroHi` | n/a | % valid forgeries T0 glm-5.2, upper 95% CI bound |
| `\ValidGLMFiveTwoTZeroCI` | n/a | % valid forgeries T0 glm-5.2, 95% CI |
| `\ValidGLMFiveTwoTZeroN` | n/a | % valid forgeries T0 glm-5.2, n |
| `\ValidGLMFiveTwoTZeroP` | n/a | % valid forgeries T0 glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\ValidGLMFiveTwoTOne` | n/a | % valid forgeries T1 glm-5.2 [n/a: no data yet] |
| `\ValidGLMFiveTwoTOneLo` | n/a | % valid forgeries T1 glm-5.2, lower 95% CI bound |
| `\ValidGLMFiveTwoTOneHi` | n/a | % valid forgeries T1 glm-5.2, upper 95% CI bound |
| `\ValidGLMFiveTwoTOneCI` | n/a | % valid forgeries T1 glm-5.2, 95% CI |
| `\ValidGLMFiveTwoTOneN` | n/a | % valid forgeries T1 glm-5.2, n |
| `\ValidGLMFiveTwoTOneP` | n/a | % valid forgeries T1 glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\ValidGLMFiveTwoTTwo` | n/a | % valid forgeries T2 glm-5.2 [n/a: no data yet] |
| `\ValidGLMFiveTwoTTwoLo` | n/a | % valid forgeries T2 glm-5.2, lower 95% CI bound |
| `\ValidGLMFiveTwoTTwoHi` | n/a | % valid forgeries T2 glm-5.2, upper 95% CI bound |
| `\ValidGLMFiveTwoTTwoCI` | n/a | % valid forgeries T2 glm-5.2, 95% CI |
| `\ValidGLMFiveTwoTTwoN` | n/a | % valid forgeries T2 glm-5.2, n |
| `\ValidGLMFiveTwoTTwoP` | n/a | % valid forgeries T2 glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\ValidGLMFiveTwoTThree` | n/a | % valid forgeries T3 glm-5.2 [n/a: no data yet] |
| `\ValidGLMFiveTwoTThreeLo` | n/a | % valid forgeries T3 glm-5.2, lower 95% CI bound |
| `\ValidGLMFiveTwoTThreeHi` | n/a | % valid forgeries T3 glm-5.2, upper 95% CI bound |
| `\ValidGLMFiveTwoTThreeCI` | n/a | % valid forgeries T3 glm-5.2, 95% CI |
| `\ValidGLMFiveTwoTThreeN` | n/a | % valid forgeries T3 glm-5.2, n |
| `\ValidGLMFiveTwoTThreeP` | n/a | % valid forgeries T3 glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\TthreeGLMFiveTwoFirstSelected` | n/a | T3 first-shown selected glm-5.2 [n/a: no data yet] |
| `\TthreeGLMFiveTwoFirstSelectedLo` | n/a | T3 first-shown selected glm-5.2, lower 95% CI bound |
| `\TthreeGLMFiveTwoFirstSelectedHi` | n/a | T3 first-shown selected glm-5.2, upper 95% CI bound |
| `\TthreeGLMFiveTwoFirstSelectedCI` | n/a | T3 first-shown selected glm-5.2, 95% CI |
| `\TthreeGLMFiveTwoFirstSelectedN` | n/a | T3 first-shown selected glm-5.2, n |
| `\TthreeGLMFiveTwoFirstSelectedP` | n/a | T3 first-shown selected glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\TthreeGLMFiveTwoFirstTop` | n/a | T3 first-shown top-rated glm-5.2 [n/a: no data yet] |
| `\TthreeGLMFiveTwoFirstTopLo` | n/a | T3 first-shown top-rated glm-5.2, lower 95% CI bound |
| `\TthreeGLMFiveTwoFirstTopHi` | n/a | T3 first-shown top-rated glm-5.2, upper 95% CI bound |
| `\TthreeGLMFiveTwoFirstTopCI` | n/a | T3 first-shown top-rated glm-5.2, 95% CI |
| `\TthreeGLMFiveTwoFirstTopN` | n/a | T3 first-shown top-rated glm-5.2, n |
| `\TthreeGLMFiveTwoFirstTopP` | n/a | T3 first-shown top-rated glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\TthreeGLMFiveTwoChance` | n/a | T3 chance level glm-5.2 [n/a: no data yet] |
| `\GateGLMFiveTwoDetector` | n/a | gate Detector glm-5.2 [n/a: no data yet] |
| `\GateGLMFiveTwoFprCalib` | n/a | gate FprCalib glm-5.2 [n/a: no data yet] |
| `\GateGLMFiveTwoCallsPerRead` | n/a | gate CallsPerRead glm-5.2 [n/a: no data yet] |
| `\GateGLMFiveTwoCleanFlag` | n/a | gate CleanFlag glm-5.2 [n/a: no data yet] |
| `\GateGLMFiveTwoCleanFlagLo` | n/a | gate CleanFlag glm-5.2, lower 95% CI bound |
| `\GateGLMFiveTwoCleanFlagHi` | n/a | gate CleanFlag glm-5.2, upper 95% CI bound |
| `\GateGLMFiveTwoCleanFlagCI` | n/a | gate CleanFlag glm-5.2, 95% CI |
| `\GateGLMFiveTwoCleanFlagN` | n/a | gate CleanFlag glm-5.2, n |
| `\GateGLMFiveTwoCleanFlagP` | n/a | gate CleanFlag glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\GateGLMFiveTwoTargetFlag` | n/a | gate TargetFlag glm-5.2 [n/a: no data yet] |
| `\GateGLMFiveTwoTargetFlagLo` | n/a | gate TargetFlag glm-5.2, lower 95% CI bound |
| `\GateGLMFiveTwoTargetFlagHi` | n/a | gate TargetFlag glm-5.2, upper 95% CI bound |
| `\GateGLMFiveTwoTargetFlagCI` | n/a | gate TargetFlag glm-5.2, 95% CI |
| `\GateGLMFiveTwoTargetFlagN` | n/a | gate TargetFlag glm-5.2, n |
| `\GateGLMFiveTwoTargetFlagP` | n/a | gate TargetFlag glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\AfcDeepSeekVFourFlashTZero` | n/a | 2AFC accuracy T0 DeepSeekVFourFlash [n/a: no data yet] |
| `\AfcDeepSeekVFourFlashTZeroLo` | n/a | 2AFC accuracy T0 DeepSeekVFourFlash, lower 95% CI bound |
| `\AfcDeepSeekVFourFlashTZeroHi` | n/a | 2AFC accuracy T0 DeepSeekVFourFlash, upper 95% CI bound |
| `\AfcDeepSeekVFourFlashTZeroCI` | n/a | 2AFC accuracy T0 DeepSeekVFourFlash, 95% CI |
| `\AfcDeepSeekVFourFlashTZeroN` | n/a | 2AFC accuracy T0 DeepSeekVFourFlash, n |
| `\AfcDeepSeekVFourFlashTZeroP` | n/a | 2AFC accuracy T0 DeepSeekVFourFlash, two-sided bootstrap p (n/a if not tested) |
| `\AfcDeepSeekVFourFlashTOne` | n/a | 2AFC accuracy T1 DeepSeekVFourFlash [n/a: no data yet] |
| `\AfcDeepSeekVFourFlashTOneLo` | n/a | 2AFC accuracy T1 DeepSeekVFourFlash, lower 95% CI bound |
| `\AfcDeepSeekVFourFlashTOneHi` | n/a | 2AFC accuracy T1 DeepSeekVFourFlash, upper 95% CI bound |
| `\AfcDeepSeekVFourFlashTOneCI` | n/a | 2AFC accuracy T1 DeepSeekVFourFlash, 95% CI |
| `\AfcDeepSeekVFourFlashTOneN` | n/a | 2AFC accuracy T1 DeepSeekVFourFlash, n |
| `\AfcDeepSeekVFourFlashTOneP` | n/a | 2AFC accuracy T1 DeepSeekVFourFlash, two-sided bootstrap p (n/a if not tested) |
| `\AfcDeepSeekVFourFlashTTwo` | n/a | 2AFC accuracy T2 DeepSeekVFourFlash [n/a: no data yet] |
| `\AfcDeepSeekVFourFlashTTwoLo` | n/a | 2AFC accuracy T2 DeepSeekVFourFlash, lower 95% CI bound |
| `\AfcDeepSeekVFourFlashTTwoHi` | n/a | 2AFC accuracy T2 DeepSeekVFourFlash, upper 95% CI bound |
| `\AfcDeepSeekVFourFlashTTwoCI` | n/a | 2AFC accuracy T2 DeepSeekVFourFlash, 95% CI |
| `\AfcDeepSeekVFourFlashTTwoN` | n/a | 2AFC accuracy T2 DeepSeekVFourFlash, n |
| `\AfcDeepSeekVFourFlashTTwoP` | n/a | 2AFC accuracy T2 DeepSeekVFourFlash, two-sided bootstrap p (n/a if not tested) |
| `\AfcDeepSeekVFourFlashTThree` | n/a | 2AFC accuracy T3 DeepSeekVFourFlash [n/a: no data yet] |
| `\AfcDeepSeekVFourFlashTThreeLo` | n/a | 2AFC accuracy T3 DeepSeekVFourFlash, lower 95% CI bound |
| `\AfcDeepSeekVFourFlashTThreeHi` | n/a | 2AFC accuracy T3 DeepSeekVFourFlash, upper 95% CI bound |
| `\AfcDeepSeekVFourFlashTThreeCI` | n/a | 2AFC accuracy T3 DeepSeekVFourFlash, 95% CI |
| `\AfcDeepSeekVFourFlashTThreeN` | n/a | 2AFC accuracy T3 DeepSeekVFourFlash, n |
| `\AfcDeepSeekVFourFlashTThreeP` | n/a | 2AFC accuracy T3 DeepSeekVFourFlash, two-sided bootstrap p (n/a if not tested) |
| `\AfcQwenThreeEightTwoSevenBTZero` | n/a | 2AFC accuracy T0 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\AfcQwenThreeEightTwoSevenBTZeroLo` | n/a | 2AFC accuracy T0 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\AfcQwenThreeEightTwoSevenBTZeroHi` | n/a | 2AFC accuracy T0 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\AfcQwenThreeEightTwoSevenBTZeroCI` | n/a | 2AFC accuracy T0 QwenThreeEightTwoSevenB, 95% CI |
| `\AfcQwenThreeEightTwoSevenBTZeroN` | n/a | 2AFC accuracy T0 QwenThreeEightTwoSevenB, n |
| `\AfcQwenThreeEightTwoSevenBTZeroP` | n/a | 2AFC accuracy T0 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\AfcQwenThreeEightTwoSevenBTOne` | n/a | 2AFC accuracy T1 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\AfcQwenThreeEightTwoSevenBTOneLo` | n/a | 2AFC accuracy T1 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\AfcQwenThreeEightTwoSevenBTOneHi` | n/a | 2AFC accuracy T1 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\AfcQwenThreeEightTwoSevenBTOneCI` | n/a | 2AFC accuracy T1 QwenThreeEightTwoSevenB, 95% CI |
| `\AfcQwenThreeEightTwoSevenBTOneN` | n/a | 2AFC accuracy T1 QwenThreeEightTwoSevenB, n |
| `\AfcQwenThreeEightTwoSevenBTOneP` | n/a | 2AFC accuracy T1 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\AfcQwenThreeEightTwoSevenBTTwo` | n/a | 2AFC accuracy T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\AfcQwenThreeEightTwoSevenBTTwoLo` | n/a | 2AFC accuracy T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\AfcQwenThreeEightTwoSevenBTTwoHi` | n/a | 2AFC accuracy T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\AfcQwenThreeEightTwoSevenBTTwoCI` | n/a | 2AFC accuracy T2 QwenThreeEightTwoSevenB, 95% CI |
| `\AfcQwenThreeEightTwoSevenBTTwoN` | n/a | 2AFC accuracy T2 QwenThreeEightTwoSevenB, n |
| `\AfcQwenThreeEightTwoSevenBTTwoP` | n/a | 2AFC accuracy T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\AfcQwenThreeEightTwoSevenBTThree` | n/a | 2AFC accuracy T3 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\AfcQwenThreeEightTwoSevenBTThreeLo` | n/a | 2AFC accuracy T3 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\AfcQwenThreeEightTwoSevenBTThreeHi` | n/a | 2AFC accuracy T3 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\AfcQwenThreeEightTwoSevenBTThreeCI` | n/a | 2AFC accuracy T3 QwenThreeEightTwoSevenB, 95% CI |
| `\AfcQwenThreeEightTwoSevenBTThreeN` | n/a | 2AFC accuracy T3 QwenThreeEightTwoSevenB, n |
| `\AfcQwenThreeEightTwoSevenBTThreeP` | n/a | 2AFC accuracy T3 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\AfcGLMFiveThreeFlashTZero` | n/a | 2AFC accuracy T0 GLMFiveThreeFlash [n/a: no data yet] |
| `\AfcGLMFiveThreeFlashTZeroLo` | n/a | 2AFC accuracy T0 GLMFiveThreeFlash, lower 95% CI bound |
| `\AfcGLMFiveThreeFlashTZeroHi` | n/a | 2AFC accuracy T0 GLMFiveThreeFlash, upper 95% CI bound |
| `\AfcGLMFiveThreeFlashTZeroCI` | n/a | 2AFC accuracy T0 GLMFiveThreeFlash, 95% CI |
| `\AfcGLMFiveThreeFlashTZeroN` | n/a | 2AFC accuracy T0 GLMFiveThreeFlash, n |
| `\AfcGLMFiveThreeFlashTZeroP` | n/a | 2AFC accuracy T0 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\AfcGLMFiveThreeFlashTOne` | n/a | 2AFC accuracy T1 GLMFiveThreeFlash [n/a: no data yet] |
| `\AfcGLMFiveThreeFlashTOneLo` | n/a | 2AFC accuracy T1 GLMFiveThreeFlash, lower 95% CI bound |
| `\AfcGLMFiveThreeFlashTOneHi` | n/a | 2AFC accuracy T1 GLMFiveThreeFlash, upper 95% CI bound |
| `\AfcGLMFiveThreeFlashTOneCI` | n/a | 2AFC accuracy T1 GLMFiveThreeFlash, 95% CI |
| `\AfcGLMFiveThreeFlashTOneN` | n/a | 2AFC accuracy T1 GLMFiveThreeFlash, n |
| `\AfcGLMFiveThreeFlashTOneP` | n/a | 2AFC accuracy T1 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\AfcGLMFiveThreeFlashTTwo` | n/a | 2AFC accuracy T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\AfcGLMFiveThreeFlashTTwoLo` | n/a | 2AFC accuracy T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\AfcGLMFiveThreeFlashTTwoHi` | n/a | 2AFC accuracy T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\AfcGLMFiveThreeFlashTTwoCI` | n/a | 2AFC accuracy T2 GLMFiveThreeFlash, 95% CI |
| `\AfcGLMFiveThreeFlashTTwoN` | n/a | 2AFC accuracy T2 GLMFiveThreeFlash, n |
| `\AfcGLMFiveThreeFlashTTwoP` | n/a | 2AFC accuracy T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\AfcGLMFiveThreeFlashTThree` | n/a | 2AFC accuracy T3 GLMFiveThreeFlash [n/a: no data yet] |
| `\AfcGLMFiveThreeFlashTThreeLo` | n/a | 2AFC accuracy T3 GLMFiveThreeFlash, lower 95% CI bound |
| `\AfcGLMFiveThreeFlashTThreeHi` | n/a | 2AFC accuracy T3 GLMFiveThreeFlash, upper 95% CI bound |
| `\AfcGLMFiveThreeFlashTThreeCI` | n/a | 2AFC accuracy T3 GLMFiveThreeFlash, 95% CI |
| `\AfcGLMFiveThreeFlashTThreeN` | n/a | 2AFC accuracy T3 GLMFiveThreeFlash, n |
| `\AfcGLMFiveThreeFlashTThreeP` | n/a | 2AFC accuracy T3 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\AfcGLMFiveTwoTZero` | n/a | 2AFC accuracy T0 GLMFiveTwo [n/a: no data yet] |
| `\AfcGLMFiveTwoTZeroLo` | n/a | 2AFC accuracy T0 GLMFiveTwo, lower 95% CI bound |
| `\AfcGLMFiveTwoTZeroHi` | n/a | 2AFC accuracy T0 GLMFiveTwo, upper 95% CI bound |
| `\AfcGLMFiveTwoTZeroCI` | n/a | 2AFC accuracy T0 GLMFiveTwo, 95% CI |
| `\AfcGLMFiveTwoTZeroN` | n/a | 2AFC accuracy T0 GLMFiveTwo, n |
| `\AfcGLMFiveTwoTZeroP` | n/a | 2AFC accuracy T0 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\AfcGLMFiveTwoTOne` | n/a | 2AFC accuracy T1 GLMFiveTwo [n/a: no data yet] |
| `\AfcGLMFiveTwoTOneLo` | n/a | 2AFC accuracy T1 GLMFiveTwo, lower 95% CI bound |
| `\AfcGLMFiveTwoTOneHi` | n/a | 2AFC accuracy T1 GLMFiveTwo, upper 95% CI bound |
| `\AfcGLMFiveTwoTOneCI` | n/a | 2AFC accuracy T1 GLMFiveTwo, 95% CI |
| `\AfcGLMFiveTwoTOneN` | n/a | 2AFC accuracy T1 GLMFiveTwo, n |
| `\AfcGLMFiveTwoTOneP` | n/a | 2AFC accuracy T1 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\AfcGLMFiveTwoTTwo` | n/a | 2AFC accuracy T2 GLMFiveTwo [n/a: no data yet] |
| `\AfcGLMFiveTwoTTwoLo` | n/a | 2AFC accuracy T2 GLMFiveTwo, lower 95% CI bound |
| `\AfcGLMFiveTwoTTwoHi` | n/a | 2AFC accuracy T2 GLMFiveTwo, upper 95% CI bound |
| `\AfcGLMFiveTwoTTwoCI` | n/a | 2AFC accuracy T2 GLMFiveTwo, 95% CI |
| `\AfcGLMFiveTwoTTwoN` | n/a | 2AFC accuracy T2 GLMFiveTwo, n |
| `\AfcGLMFiveTwoTTwoP` | n/a | 2AFC accuracy T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\AfcGLMFiveTwoTThree` | n/a | 2AFC accuracy T3 GLMFiveTwo [n/a: no data yet] |
| `\AfcGLMFiveTwoTThreeLo` | n/a | 2AFC accuracy T3 GLMFiveTwo, lower 95% CI bound |
| `\AfcGLMFiveTwoTThreeHi` | n/a | 2AFC accuracy T3 GLMFiveTwo, upper 95% CI bound |
| `\AfcGLMFiveTwoTThreeCI` | n/a | 2AFC accuracy T3 GLMFiveTwo, 95% CI |
| `\AfcGLMFiveTwoTThreeN` | n/a | 2AFC accuracy T3 GLMFiveTwo, n |
| `\AfcGLMFiveTwoTThreeP` | n/a | 2AFC accuracy T3 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsr` | n/a | P4 Asr none T0 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrLo` | n/a | P4 Asr none T0 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrHi` | n/a | P4 Asr none T0 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrCI` | n/a | P4 Asr none T0 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrN` | n/a | P4 Asr none T0 QwenThreeEightTwoSevenB, n |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrP` | n/a | P4 Asr none T0 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrDropped` | n/a | P4 AsrDropped none T0 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrDroppedLo` | n/a | P4 AsrDropped none T0 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrDroppedHi` | n/a | P4 AsrDropped none T0 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrDroppedCI` | n/a | P4 AsrDropped none T0 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrDroppedN` | n/a | P4 AsrDropped none T0 QwenThreeEightTwoSevenB, n |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrDroppedP` | n/a | P4 AsrDropped none T0 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrCleanOk` | n/a | P4 AsrCleanOk none T0 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrCleanOkLo` | n/a | P4 AsrCleanOk none T0 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrCleanOkHi` | n/a | P4 AsrCleanOk none T0 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrCleanOkCI` | n/a | P4 AsrCleanOk none T0 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrCleanOkN` | n/a | P4 AsrCleanOk none T0 QwenThreeEightTwoSevenB, n |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrCleanOkP` | n/a | P4 AsrCleanOk none T0 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBNonTargetAcc` | n/a | P4 NonTargetAcc none T0 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBNonTargetAccLo` | n/a | P4 NonTargetAcc none T0 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBNonTargetAccHi` | n/a | P4 NonTargetAcc none T0 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBNonTargetAccCI` | n/a | P4 NonTargetAcc none T0 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBNonTargetAccN` | n/a | P4 NonTargetAcc none T0 QwenThreeEightTwoSevenB, n |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBNonTargetAccP` | n/a | P4 NonTargetAcc none T0 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGLMFiveThreeFlashAsr` | n/a | P4 Asr none T0 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrLo` | n/a | P4 Asr none T0 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrHi` | n/a | P4 Asr none T0 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrCI` | n/a | P4 Asr none T0 GLMFiveThreeFlash, 95% CI |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrN` | n/a | P4 Asr none T0 GLMFiveThreeFlash, n |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrP` | n/a | P4 Asr none T0 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrDropped` | n/a | P4 AsrDropped none T0 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrDroppedLo` | n/a | P4 AsrDropped none T0 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrDroppedHi` | n/a | P4 AsrDropped none T0 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrDroppedCI` | n/a | P4 AsrDropped none T0 GLMFiveThreeFlash, 95% CI |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrDroppedN` | n/a | P4 AsrDropped none T0 GLMFiveThreeFlash, n |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrDroppedP` | n/a | P4 AsrDropped none T0 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrCleanOk` | n/a | P4 AsrCleanOk none T0 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrCleanOkLo` | n/a | P4 AsrCleanOk none T0 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrCleanOkHi` | n/a | P4 AsrCleanOk none T0 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrCleanOkCI` | n/a | P4 AsrCleanOk none T0 GLMFiveThreeFlash, 95% CI |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrCleanOkN` | n/a | P4 AsrCleanOk none T0 GLMFiveThreeFlash, n |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrCleanOkP` | n/a | P4 AsrCleanOk none T0 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGLMFiveThreeFlashNonTargetAcc` | n/a | P4 NonTargetAcc none T0 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourNoneTZeroGLMFiveThreeFlashNonTargetAccLo` | n/a | P4 NonTargetAcc none T0 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourNoneTZeroGLMFiveThreeFlashNonTargetAccHi` | n/a | P4 NonTargetAcc none T0 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourNoneTZeroGLMFiveThreeFlashNonTargetAccCI` | n/a | P4 NonTargetAcc none T0 GLMFiveThreeFlash, 95% CI |
| `\PfourNoneTZeroGLMFiveThreeFlashNonTargetAccN` | n/a | P4 NonTargetAcc none T0 GLMFiveThreeFlash, n |
| `\PfourNoneTZeroGLMFiveThreeFlashNonTargetAccP` | n/a | P4 NonTargetAcc none T0 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGLMFiveTwoAsr` | n/a | P4 Asr none T0 GLMFiveTwo [n/a: no data yet] |
| `\PfourNoneTZeroGLMFiveTwoAsrLo` | n/a | P4 Asr none T0 GLMFiveTwo, lower 95% CI bound |
| `\PfourNoneTZeroGLMFiveTwoAsrHi` | n/a | P4 Asr none T0 GLMFiveTwo, upper 95% CI bound |
| `\PfourNoneTZeroGLMFiveTwoAsrCI` | n/a | P4 Asr none T0 GLMFiveTwo, 95% CI |
| `\PfourNoneTZeroGLMFiveTwoAsrN` | n/a | P4 Asr none T0 GLMFiveTwo, n |
| `\PfourNoneTZeroGLMFiveTwoAsrP` | n/a | P4 Asr none T0 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGLMFiveTwoAsrDropped` | n/a | P4 AsrDropped none T0 GLMFiveTwo [n/a: no data yet] |
| `\PfourNoneTZeroGLMFiveTwoAsrDroppedLo` | n/a | P4 AsrDropped none T0 GLMFiveTwo, lower 95% CI bound |
| `\PfourNoneTZeroGLMFiveTwoAsrDroppedHi` | n/a | P4 AsrDropped none T0 GLMFiveTwo, upper 95% CI bound |
| `\PfourNoneTZeroGLMFiveTwoAsrDroppedCI` | n/a | P4 AsrDropped none T0 GLMFiveTwo, 95% CI |
| `\PfourNoneTZeroGLMFiveTwoAsrDroppedN` | n/a | P4 AsrDropped none T0 GLMFiveTwo, n |
| `\PfourNoneTZeroGLMFiveTwoAsrDroppedP` | n/a | P4 AsrDropped none T0 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGLMFiveTwoAsrCleanOk` | n/a | P4 AsrCleanOk none T0 GLMFiveTwo [n/a: no data yet] |
| `\PfourNoneTZeroGLMFiveTwoAsrCleanOkLo` | n/a | P4 AsrCleanOk none T0 GLMFiveTwo, lower 95% CI bound |
| `\PfourNoneTZeroGLMFiveTwoAsrCleanOkHi` | n/a | P4 AsrCleanOk none T0 GLMFiveTwo, upper 95% CI bound |
| `\PfourNoneTZeroGLMFiveTwoAsrCleanOkCI` | n/a | P4 AsrCleanOk none T0 GLMFiveTwo, 95% CI |
| `\PfourNoneTZeroGLMFiveTwoAsrCleanOkN` | n/a | P4 AsrCleanOk none T0 GLMFiveTwo, n |
| `\PfourNoneTZeroGLMFiveTwoAsrCleanOkP` | n/a | P4 AsrCleanOk none T0 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGLMFiveTwoNonTargetAcc` | n/a | P4 NonTargetAcc none T0 GLMFiveTwo [n/a: no data yet] |
| `\PfourNoneTZeroGLMFiveTwoNonTargetAccLo` | n/a | P4 NonTargetAcc none T0 GLMFiveTwo, lower 95% CI bound |
| `\PfourNoneTZeroGLMFiveTwoNonTargetAccHi` | n/a | P4 NonTargetAcc none T0 GLMFiveTwo, upper 95% CI bound |
| `\PfourNoneTZeroGLMFiveTwoNonTargetAccCI` | n/a | P4 NonTargetAcc none T0 GLMFiveTwo, 95% CI |
| `\PfourNoneTZeroGLMFiveTwoNonTargetAccN` | n/a | P4 NonTargetAcc none T0 GLMFiveTwo, n |
| `\PfourNoneTZeroGLMFiveTwoNonTargetAccP` | n/a | P4 NonTargetAcc none T0 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsr` | n/a | P4 Asr none T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrLo` | n/a | P4 Asr none T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrHi` | n/a | P4 Asr none T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrCI` | n/a | P4 Asr none T2 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrN` | n/a | P4 Asr none T2 QwenThreeEightTwoSevenB, n |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrP` | n/a | P4 Asr none T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrDropped` | n/a | P4 AsrDropped none T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrDroppedLo` | n/a | P4 AsrDropped none T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrDroppedHi` | n/a | P4 AsrDropped none T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrDroppedCI` | n/a | P4 AsrDropped none T2 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrDroppedN` | n/a | P4 AsrDropped none T2 QwenThreeEightTwoSevenB, n |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrDroppedP` | n/a | P4 AsrDropped none T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrCleanOk` | n/a | P4 AsrCleanOk none T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrCleanOkLo` | n/a | P4 AsrCleanOk none T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrCleanOkHi` | n/a | P4 AsrCleanOk none T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrCleanOkCI` | n/a | P4 AsrCleanOk none T2 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrCleanOkN` | n/a | P4 AsrCleanOk none T2 QwenThreeEightTwoSevenB, n |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrCleanOkP` | n/a | P4 AsrCleanOk none T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBNonTargetAcc` | n/a | P4 NonTargetAcc none T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBNonTargetAccLo` | n/a | P4 NonTargetAcc none T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBNonTargetAccHi` | n/a | P4 NonTargetAcc none T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBNonTargetAccCI` | n/a | P4 NonTargetAcc none T2 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBNonTargetAccN` | n/a | P4 NonTargetAcc none T2 QwenThreeEightTwoSevenB, n |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBNonTargetAccP` | n/a | P4 NonTargetAcc none T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGLMFiveThreeFlashAsr` | n/a | P4 Asr none T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrLo` | n/a | P4 Asr none T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrHi` | n/a | P4 Asr none T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrCI` | n/a | P4 Asr none T2 GLMFiveThreeFlash, 95% CI |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrN` | n/a | P4 Asr none T2 GLMFiveThreeFlash, n |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrP` | n/a | P4 Asr none T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrDropped` | n/a | P4 AsrDropped none T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrDroppedLo` | n/a | P4 AsrDropped none T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrDroppedHi` | n/a | P4 AsrDropped none T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrDroppedCI` | n/a | P4 AsrDropped none T2 GLMFiveThreeFlash, 95% CI |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrDroppedN` | n/a | P4 AsrDropped none T2 GLMFiveThreeFlash, n |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrDroppedP` | n/a | P4 AsrDropped none T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrCleanOk` | n/a | P4 AsrCleanOk none T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrCleanOkLo` | n/a | P4 AsrCleanOk none T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrCleanOkHi` | n/a | P4 AsrCleanOk none T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrCleanOkCI` | n/a | P4 AsrCleanOk none T2 GLMFiveThreeFlash, 95% CI |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrCleanOkN` | n/a | P4 AsrCleanOk none T2 GLMFiveThreeFlash, n |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrCleanOkP` | n/a | P4 AsrCleanOk none T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGLMFiveThreeFlashNonTargetAcc` | n/a | P4 NonTargetAcc none T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourNoneTTwoGLMFiveThreeFlashNonTargetAccLo` | n/a | P4 NonTargetAcc none T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourNoneTTwoGLMFiveThreeFlashNonTargetAccHi` | n/a | P4 NonTargetAcc none T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourNoneTTwoGLMFiveThreeFlashNonTargetAccCI` | n/a | P4 NonTargetAcc none T2 GLMFiveThreeFlash, 95% CI |
| `\PfourNoneTTwoGLMFiveThreeFlashNonTargetAccN` | n/a | P4 NonTargetAcc none T2 GLMFiveThreeFlash, n |
| `\PfourNoneTTwoGLMFiveThreeFlashNonTargetAccP` | n/a | P4 NonTargetAcc none T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGLMFiveTwoAsr` | n/a | P4 Asr none T2 GLMFiveTwo [n/a: no data yet] |
| `\PfourNoneTTwoGLMFiveTwoAsrLo` | n/a | P4 Asr none T2 GLMFiveTwo, lower 95% CI bound |
| `\PfourNoneTTwoGLMFiveTwoAsrHi` | n/a | P4 Asr none T2 GLMFiveTwo, upper 95% CI bound |
| `\PfourNoneTTwoGLMFiveTwoAsrCI` | n/a | P4 Asr none T2 GLMFiveTwo, 95% CI |
| `\PfourNoneTTwoGLMFiveTwoAsrN` | n/a | P4 Asr none T2 GLMFiveTwo, n |
| `\PfourNoneTTwoGLMFiveTwoAsrP` | n/a | P4 Asr none T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGLMFiveTwoAsrDropped` | n/a | P4 AsrDropped none T2 GLMFiveTwo [n/a: no data yet] |
| `\PfourNoneTTwoGLMFiveTwoAsrDroppedLo` | n/a | P4 AsrDropped none T2 GLMFiveTwo, lower 95% CI bound |
| `\PfourNoneTTwoGLMFiveTwoAsrDroppedHi` | n/a | P4 AsrDropped none T2 GLMFiveTwo, upper 95% CI bound |
| `\PfourNoneTTwoGLMFiveTwoAsrDroppedCI` | n/a | P4 AsrDropped none T2 GLMFiveTwo, 95% CI |
| `\PfourNoneTTwoGLMFiveTwoAsrDroppedN` | n/a | P4 AsrDropped none T2 GLMFiveTwo, n |
| `\PfourNoneTTwoGLMFiveTwoAsrDroppedP` | n/a | P4 AsrDropped none T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGLMFiveTwoAsrCleanOk` | n/a | P4 AsrCleanOk none T2 GLMFiveTwo [n/a: no data yet] |
| `\PfourNoneTTwoGLMFiveTwoAsrCleanOkLo` | n/a | P4 AsrCleanOk none T2 GLMFiveTwo, lower 95% CI bound |
| `\PfourNoneTTwoGLMFiveTwoAsrCleanOkHi` | n/a | P4 AsrCleanOk none T2 GLMFiveTwo, upper 95% CI bound |
| `\PfourNoneTTwoGLMFiveTwoAsrCleanOkCI` | n/a | P4 AsrCleanOk none T2 GLMFiveTwo, 95% CI |
| `\PfourNoneTTwoGLMFiveTwoAsrCleanOkN` | n/a | P4 AsrCleanOk none T2 GLMFiveTwo, n |
| `\PfourNoneTTwoGLMFiveTwoAsrCleanOkP` | n/a | P4 AsrCleanOk none T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGLMFiveTwoNonTargetAcc` | n/a | P4 NonTargetAcc none T2 GLMFiveTwo [n/a: no data yet] |
| `\PfourNoneTTwoGLMFiveTwoNonTargetAccLo` | n/a | P4 NonTargetAcc none T2 GLMFiveTwo, lower 95% CI bound |
| `\PfourNoneTTwoGLMFiveTwoNonTargetAccHi` | n/a | P4 NonTargetAcc none T2 GLMFiveTwo, upper 95% CI bound |
| `\PfourNoneTTwoGLMFiveTwoNonTargetAccCI` | n/a | P4 NonTargetAcc none T2 GLMFiveTwo, 95% CI |
| `\PfourNoneTTwoGLMFiveTwoNonTargetAccN` | n/a | P4 NonTargetAcc none T2 GLMFiveTwo, n |
| `\PfourNoneTTwoGLMFiveTwoNonTargetAccP` | n/a | P4 NonTargetAcc none T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsr` | n/a | P4 Asr none T3 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrLo` | n/a | P4 Asr none T3 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrHi` | n/a | P4 Asr none T3 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrCI` | n/a | P4 Asr none T3 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrN` | n/a | P4 Asr none T3 QwenThreeEightTwoSevenB, n |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrP` | n/a | P4 Asr none T3 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrDropped` | n/a | P4 AsrDropped none T3 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrDroppedLo` | n/a | P4 AsrDropped none T3 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrDroppedHi` | n/a | P4 AsrDropped none T3 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrDroppedCI` | n/a | P4 AsrDropped none T3 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrDroppedN` | n/a | P4 AsrDropped none T3 QwenThreeEightTwoSevenB, n |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrDroppedP` | n/a | P4 AsrDropped none T3 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrCleanOk` | n/a | P4 AsrCleanOk none T3 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrCleanOkLo` | n/a | P4 AsrCleanOk none T3 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrCleanOkHi` | n/a | P4 AsrCleanOk none T3 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrCleanOkCI` | n/a | P4 AsrCleanOk none T3 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrCleanOkN` | n/a | P4 AsrCleanOk none T3 QwenThreeEightTwoSevenB, n |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrCleanOkP` | n/a | P4 AsrCleanOk none T3 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBNonTargetAcc` | n/a | P4 NonTargetAcc none T3 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBNonTargetAccLo` | n/a | P4 NonTargetAcc none T3 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBNonTargetAccHi` | n/a | P4 NonTargetAcc none T3 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBNonTargetAccCI` | n/a | P4 NonTargetAcc none T3 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBNonTargetAccN` | n/a | P4 NonTargetAcc none T3 QwenThreeEightTwoSevenB, n |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBNonTargetAccP` | n/a | P4 NonTargetAcc none T3 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGLMFiveThreeFlashAsr` | n/a | P4 Asr none T3 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrLo` | n/a | P4 Asr none T3 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrHi` | n/a | P4 Asr none T3 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrCI` | n/a | P4 Asr none T3 GLMFiveThreeFlash, 95% CI |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrN` | n/a | P4 Asr none T3 GLMFiveThreeFlash, n |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrP` | n/a | P4 Asr none T3 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrDropped` | n/a | P4 AsrDropped none T3 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrDroppedLo` | n/a | P4 AsrDropped none T3 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrDroppedHi` | n/a | P4 AsrDropped none T3 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrDroppedCI` | n/a | P4 AsrDropped none T3 GLMFiveThreeFlash, 95% CI |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrDroppedN` | n/a | P4 AsrDropped none T3 GLMFiveThreeFlash, n |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrDroppedP` | n/a | P4 AsrDropped none T3 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrCleanOk` | n/a | P4 AsrCleanOk none T3 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrCleanOkLo` | n/a | P4 AsrCleanOk none T3 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrCleanOkHi` | n/a | P4 AsrCleanOk none T3 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrCleanOkCI` | n/a | P4 AsrCleanOk none T3 GLMFiveThreeFlash, 95% CI |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrCleanOkN` | n/a | P4 AsrCleanOk none T3 GLMFiveThreeFlash, n |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrCleanOkP` | n/a | P4 AsrCleanOk none T3 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGLMFiveThreeFlashNonTargetAcc` | n/a | P4 NonTargetAcc none T3 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourNoneTThreeGLMFiveThreeFlashNonTargetAccLo` | n/a | P4 NonTargetAcc none T3 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourNoneTThreeGLMFiveThreeFlashNonTargetAccHi` | n/a | P4 NonTargetAcc none T3 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourNoneTThreeGLMFiveThreeFlashNonTargetAccCI` | n/a | P4 NonTargetAcc none T3 GLMFiveThreeFlash, 95% CI |
| `\PfourNoneTThreeGLMFiveThreeFlashNonTargetAccN` | n/a | P4 NonTargetAcc none T3 GLMFiveThreeFlash, n |
| `\PfourNoneTThreeGLMFiveThreeFlashNonTargetAccP` | n/a | P4 NonTargetAcc none T3 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGLMFiveTwoAsr` | n/a | P4 Asr none T3 GLMFiveTwo [n/a: no data yet] |
| `\PfourNoneTThreeGLMFiveTwoAsrLo` | n/a | P4 Asr none T3 GLMFiveTwo, lower 95% CI bound |
| `\PfourNoneTThreeGLMFiveTwoAsrHi` | n/a | P4 Asr none T3 GLMFiveTwo, upper 95% CI bound |
| `\PfourNoneTThreeGLMFiveTwoAsrCI` | n/a | P4 Asr none T3 GLMFiveTwo, 95% CI |
| `\PfourNoneTThreeGLMFiveTwoAsrN` | n/a | P4 Asr none T3 GLMFiveTwo, n |
| `\PfourNoneTThreeGLMFiveTwoAsrP` | n/a | P4 Asr none T3 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGLMFiveTwoAsrDropped` | n/a | P4 AsrDropped none T3 GLMFiveTwo [n/a: no data yet] |
| `\PfourNoneTThreeGLMFiveTwoAsrDroppedLo` | n/a | P4 AsrDropped none T3 GLMFiveTwo, lower 95% CI bound |
| `\PfourNoneTThreeGLMFiveTwoAsrDroppedHi` | n/a | P4 AsrDropped none T3 GLMFiveTwo, upper 95% CI bound |
| `\PfourNoneTThreeGLMFiveTwoAsrDroppedCI` | n/a | P4 AsrDropped none T3 GLMFiveTwo, 95% CI |
| `\PfourNoneTThreeGLMFiveTwoAsrDroppedN` | n/a | P4 AsrDropped none T3 GLMFiveTwo, n |
| `\PfourNoneTThreeGLMFiveTwoAsrDroppedP` | n/a | P4 AsrDropped none T3 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGLMFiveTwoAsrCleanOk` | n/a | P4 AsrCleanOk none T3 GLMFiveTwo [n/a: no data yet] |
| `\PfourNoneTThreeGLMFiveTwoAsrCleanOkLo` | n/a | P4 AsrCleanOk none T3 GLMFiveTwo, lower 95% CI bound |
| `\PfourNoneTThreeGLMFiveTwoAsrCleanOkHi` | n/a | P4 AsrCleanOk none T3 GLMFiveTwo, upper 95% CI bound |
| `\PfourNoneTThreeGLMFiveTwoAsrCleanOkCI` | n/a | P4 AsrCleanOk none T3 GLMFiveTwo, 95% CI |
| `\PfourNoneTThreeGLMFiveTwoAsrCleanOkN` | n/a | P4 AsrCleanOk none T3 GLMFiveTwo, n |
| `\PfourNoneTThreeGLMFiveTwoAsrCleanOkP` | n/a | P4 AsrCleanOk none T3 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGLMFiveTwoNonTargetAcc` | n/a | P4 NonTargetAcc none T3 GLMFiveTwo [n/a: no data yet] |
| `\PfourNoneTThreeGLMFiveTwoNonTargetAccLo` | n/a | P4 NonTargetAcc none T3 GLMFiveTwo, lower 95% CI bound |
| `\PfourNoneTThreeGLMFiveTwoNonTargetAccHi` | n/a | P4 NonTargetAcc none T3 GLMFiveTwo, upper 95% CI bound |
| `\PfourNoneTThreeGLMFiveTwoNonTargetAccCI` | n/a | P4 NonTargetAcc none T3 GLMFiveTwo, 95% CI |
| `\PfourNoneTThreeGLMFiveTwoNonTargetAccN` | n/a | P4 NonTargetAcc none T3 GLMFiveTwo, n |
| `\PfourNoneTThreeGLMFiveTwoNonTargetAccP` | n/a | P4 NonTargetAcc none T3 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsr` | n/a | P4 Asr no_memory - QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrLo` | n/a | P4 Asr no_memory - QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrHi` | n/a | P4 Asr no_memory - QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrCI` | n/a | P4 Asr no_memory - QwenThreeEightTwoSevenB, 95% CI |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrN` | n/a | P4 Asr no_memory - QwenThreeEightTwoSevenB, n |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrP` | n/a | P4 Asr no_memory - QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrDropped` | n/a | P4 AsrDropped no_memory - QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrDroppedLo` | n/a | P4 AsrDropped no_memory - QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrDroppedHi` | n/a | P4 AsrDropped no_memory - QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrDroppedCI` | n/a | P4 AsrDropped no_memory - QwenThreeEightTwoSevenB, 95% CI |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrDroppedN` | n/a | P4 AsrDropped no_memory - QwenThreeEightTwoSevenB, n |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrDroppedP` | n/a | P4 AsrDropped no_memory - QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrCleanOk` | n/a | P4 AsrCleanOk no_memory - QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrCleanOkLo` | n/a | P4 AsrCleanOk no_memory - QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrCleanOkHi` | n/a | P4 AsrCleanOk no_memory - QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrCleanOkCI` | n/a | P4 AsrCleanOk no_memory - QwenThreeEightTwoSevenB, 95% CI |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrCleanOkN` | n/a | P4 AsrCleanOk no_memory - QwenThreeEightTwoSevenB, n |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrCleanOkP` | n/a | P4 AsrCleanOk no_memory - QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryQwenThreeEightTwoSevenBNonTargetAcc` | n/a | P4 NonTargetAcc no_memory - QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourNoMemoryQwenThreeEightTwoSevenBNonTargetAccLo` | n/a | P4 NonTargetAcc no_memory - QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourNoMemoryQwenThreeEightTwoSevenBNonTargetAccHi` | n/a | P4 NonTargetAcc no_memory - QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourNoMemoryQwenThreeEightTwoSevenBNonTargetAccCI` | n/a | P4 NonTargetAcc no_memory - QwenThreeEightTwoSevenB, 95% CI |
| `\PfourNoMemoryQwenThreeEightTwoSevenBNonTargetAccN` | n/a | P4 NonTargetAcc no_memory - QwenThreeEightTwoSevenB, n |
| `\PfourNoMemoryQwenThreeEightTwoSevenBNonTargetAccP` | n/a | P4 NonTargetAcc no_memory - QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGLMFiveThreeFlashAsr` | n/a | P4 Asr no_memory - GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourNoMemoryGLMFiveThreeFlashAsrLo` | n/a | P4 Asr no_memory - GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourNoMemoryGLMFiveThreeFlashAsrHi` | n/a | P4 Asr no_memory - GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourNoMemoryGLMFiveThreeFlashAsrCI` | n/a | P4 Asr no_memory - GLMFiveThreeFlash, 95% CI |
| `\PfourNoMemoryGLMFiveThreeFlashAsrN` | n/a | P4 Asr no_memory - GLMFiveThreeFlash, n |
| `\PfourNoMemoryGLMFiveThreeFlashAsrP` | n/a | P4 Asr no_memory - GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGLMFiveThreeFlashAsrDropped` | n/a | P4 AsrDropped no_memory - GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourNoMemoryGLMFiveThreeFlashAsrDroppedLo` | n/a | P4 AsrDropped no_memory - GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourNoMemoryGLMFiveThreeFlashAsrDroppedHi` | n/a | P4 AsrDropped no_memory - GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourNoMemoryGLMFiveThreeFlashAsrDroppedCI` | n/a | P4 AsrDropped no_memory - GLMFiveThreeFlash, 95% CI |
| `\PfourNoMemoryGLMFiveThreeFlashAsrDroppedN` | n/a | P4 AsrDropped no_memory - GLMFiveThreeFlash, n |
| `\PfourNoMemoryGLMFiveThreeFlashAsrDroppedP` | n/a | P4 AsrDropped no_memory - GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGLMFiveThreeFlashAsrCleanOk` | n/a | P4 AsrCleanOk no_memory - GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourNoMemoryGLMFiveThreeFlashAsrCleanOkLo` | n/a | P4 AsrCleanOk no_memory - GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourNoMemoryGLMFiveThreeFlashAsrCleanOkHi` | n/a | P4 AsrCleanOk no_memory - GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourNoMemoryGLMFiveThreeFlashAsrCleanOkCI` | n/a | P4 AsrCleanOk no_memory - GLMFiveThreeFlash, 95% CI |
| `\PfourNoMemoryGLMFiveThreeFlashAsrCleanOkN` | n/a | P4 AsrCleanOk no_memory - GLMFiveThreeFlash, n |
| `\PfourNoMemoryGLMFiveThreeFlashAsrCleanOkP` | n/a | P4 AsrCleanOk no_memory - GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGLMFiveThreeFlashNonTargetAcc` | n/a | P4 NonTargetAcc no_memory - GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourNoMemoryGLMFiveThreeFlashNonTargetAccLo` | n/a | P4 NonTargetAcc no_memory - GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourNoMemoryGLMFiveThreeFlashNonTargetAccHi` | n/a | P4 NonTargetAcc no_memory - GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourNoMemoryGLMFiveThreeFlashNonTargetAccCI` | n/a | P4 NonTargetAcc no_memory - GLMFiveThreeFlash, 95% CI |
| `\PfourNoMemoryGLMFiveThreeFlashNonTargetAccN` | n/a | P4 NonTargetAcc no_memory - GLMFiveThreeFlash, n |
| `\PfourNoMemoryGLMFiveThreeFlashNonTargetAccP` | n/a | P4 NonTargetAcc no_memory - GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGLMFiveTwoAsr` | n/a | P4 Asr no_memory - GLMFiveTwo [n/a: no data yet] |
| `\PfourNoMemoryGLMFiveTwoAsrLo` | n/a | P4 Asr no_memory - GLMFiveTwo, lower 95% CI bound |
| `\PfourNoMemoryGLMFiveTwoAsrHi` | n/a | P4 Asr no_memory - GLMFiveTwo, upper 95% CI bound |
| `\PfourNoMemoryGLMFiveTwoAsrCI` | n/a | P4 Asr no_memory - GLMFiveTwo, 95% CI |
| `\PfourNoMemoryGLMFiveTwoAsrN` | n/a | P4 Asr no_memory - GLMFiveTwo, n |
| `\PfourNoMemoryGLMFiveTwoAsrP` | n/a | P4 Asr no_memory - GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGLMFiveTwoAsrDropped` | n/a | P4 AsrDropped no_memory - GLMFiveTwo [n/a: no data yet] |
| `\PfourNoMemoryGLMFiveTwoAsrDroppedLo` | n/a | P4 AsrDropped no_memory - GLMFiveTwo, lower 95% CI bound |
| `\PfourNoMemoryGLMFiveTwoAsrDroppedHi` | n/a | P4 AsrDropped no_memory - GLMFiveTwo, upper 95% CI bound |
| `\PfourNoMemoryGLMFiveTwoAsrDroppedCI` | n/a | P4 AsrDropped no_memory - GLMFiveTwo, 95% CI |
| `\PfourNoMemoryGLMFiveTwoAsrDroppedN` | n/a | P4 AsrDropped no_memory - GLMFiveTwo, n |
| `\PfourNoMemoryGLMFiveTwoAsrDroppedP` | n/a | P4 AsrDropped no_memory - GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGLMFiveTwoAsrCleanOk` | n/a | P4 AsrCleanOk no_memory - GLMFiveTwo [n/a: no data yet] |
| `\PfourNoMemoryGLMFiveTwoAsrCleanOkLo` | n/a | P4 AsrCleanOk no_memory - GLMFiveTwo, lower 95% CI bound |
| `\PfourNoMemoryGLMFiveTwoAsrCleanOkHi` | n/a | P4 AsrCleanOk no_memory - GLMFiveTwo, upper 95% CI bound |
| `\PfourNoMemoryGLMFiveTwoAsrCleanOkCI` | n/a | P4 AsrCleanOk no_memory - GLMFiveTwo, 95% CI |
| `\PfourNoMemoryGLMFiveTwoAsrCleanOkN` | n/a | P4 AsrCleanOk no_memory - GLMFiveTwo, n |
| `\PfourNoMemoryGLMFiveTwoAsrCleanOkP` | n/a | P4 AsrCleanOk no_memory - GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGLMFiveTwoNonTargetAcc` | n/a | P4 NonTargetAcc no_memory - GLMFiveTwo [n/a: no data yet] |
| `\PfourNoMemoryGLMFiveTwoNonTargetAccLo` | n/a | P4 NonTargetAcc no_memory - GLMFiveTwo, lower 95% CI bound |
| `\PfourNoMemoryGLMFiveTwoNonTargetAccHi` | n/a | P4 NonTargetAcc no_memory - GLMFiveTwo, upper 95% CI bound |
| `\PfourNoMemoryGLMFiveTwoNonTargetAccCI` | n/a | P4 NonTargetAcc no_memory - GLMFiveTwo, 95% CI |
| `\PfourNoMemoryGLMFiveTwoNonTargetAccN` | n/a | P4 NonTargetAcc no_memory - GLMFiveTwo, n |
| `\PfourNoMemoryGLMFiveTwoNonTargetAccP` | n/a | P4 NonTargetAcc no_memory - GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroPooledAsr` | n/a | P4 Asr G1 T0 Pooled [n/a: no data yet] |
| `\PfourGOneTZeroPooledAsrLo` | n/a | P4 Asr G1 T0 Pooled, lower 95% CI bound |
| `\PfourGOneTZeroPooledAsrHi` | n/a | P4 Asr G1 T0 Pooled, upper 95% CI bound |
| `\PfourGOneTZeroPooledAsrCI` | n/a | P4 Asr G1 T0 Pooled, 95% CI |
| `\PfourGOneTZeroPooledAsrN` | n/a | P4 Asr G1 T0 Pooled, n |
| `\PfourGOneTZeroPooledAsrP` | n/a | P4 Asr G1 T0 Pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroPooledAsrDropped` | n/a | P4 AsrDropped G1 T0 Pooled [n/a: no data yet] |
| `\PfourGOneTZeroPooledAsrDroppedLo` | n/a | P4 AsrDropped G1 T0 Pooled, lower 95% CI bound |
| `\PfourGOneTZeroPooledAsrDroppedHi` | n/a | P4 AsrDropped G1 T0 Pooled, upper 95% CI bound |
| `\PfourGOneTZeroPooledAsrDroppedCI` | n/a | P4 AsrDropped G1 T0 Pooled, 95% CI |
| `\PfourGOneTZeroPooledAsrDroppedN` | n/a | P4 AsrDropped G1 T0 Pooled, n |
| `\PfourGOneTZeroPooledAsrDroppedP` | n/a | P4 AsrDropped G1 T0 Pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroPooledAsrCleanOk` | n/a | P4 AsrCleanOk G1 T0 Pooled [n/a: no data yet] |
| `\PfourGOneTZeroPooledAsrCleanOkLo` | n/a | P4 AsrCleanOk G1 T0 Pooled, lower 95% CI bound |
| `\PfourGOneTZeroPooledAsrCleanOkHi` | n/a | P4 AsrCleanOk G1 T0 Pooled, upper 95% CI bound |
| `\PfourGOneTZeroPooledAsrCleanOkCI` | n/a | P4 AsrCleanOk G1 T0 Pooled, 95% CI |
| `\PfourGOneTZeroPooledAsrCleanOkN` | n/a | P4 AsrCleanOk G1 T0 Pooled, n |
| `\PfourGOneTZeroPooledAsrCleanOkP` | n/a | P4 AsrCleanOk G1 T0 Pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroPooledNonTargetAcc` | n/a | P4 NonTargetAcc G1 T0 Pooled [n/a: no data yet] |
| `\PfourGOneTZeroPooledNonTargetAccLo` | n/a | P4 NonTargetAcc G1 T0 Pooled, lower 95% CI bound |
| `\PfourGOneTZeroPooledNonTargetAccHi` | n/a | P4 NonTargetAcc G1 T0 Pooled, upper 95% CI bound |
| `\PfourGOneTZeroPooledNonTargetAccCI` | n/a | P4 NonTargetAcc G1 T0 Pooled, 95% CI |
| `\PfourGOneTZeroPooledNonTargetAccN` | n/a | P4 NonTargetAcc G1 T0 Pooled, n |
| `\PfourGOneTZeroPooledNonTargetAccP` | n/a | P4 NonTargetAcc G1 T0 Pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroDeepSeekVFourFlashAsr` | n/a | P4 Asr G1 T0 DeepSeekVFourFlash [n/a: no data yet] |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrLo` | n/a | P4 Asr G1 T0 DeepSeekVFourFlash, lower 95% CI bound |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrHi` | n/a | P4 Asr G1 T0 DeepSeekVFourFlash, upper 95% CI bound |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrCI` | n/a | P4 Asr G1 T0 DeepSeekVFourFlash, 95% CI |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrN` | n/a | P4 Asr G1 T0 DeepSeekVFourFlash, n |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrP` | n/a | P4 Asr G1 T0 DeepSeekVFourFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrDropped` | n/a | P4 AsrDropped G1 T0 DeepSeekVFourFlash [n/a: no data yet] |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrDroppedLo` | n/a | P4 AsrDropped G1 T0 DeepSeekVFourFlash, lower 95% CI bound |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrDroppedHi` | n/a | P4 AsrDropped G1 T0 DeepSeekVFourFlash, upper 95% CI bound |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrDroppedCI` | n/a | P4 AsrDropped G1 T0 DeepSeekVFourFlash, 95% CI |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrDroppedN` | n/a | P4 AsrDropped G1 T0 DeepSeekVFourFlash, n |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrDroppedP` | n/a | P4 AsrDropped G1 T0 DeepSeekVFourFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrCleanOk` | n/a | P4 AsrCleanOk G1 T0 DeepSeekVFourFlash [n/a: no data yet] |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrCleanOkLo` | n/a | P4 AsrCleanOk G1 T0 DeepSeekVFourFlash, lower 95% CI bound |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrCleanOkHi` | n/a | P4 AsrCleanOk G1 T0 DeepSeekVFourFlash, upper 95% CI bound |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrCleanOkCI` | n/a | P4 AsrCleanOk G1 T0 DeepSeekVFourFlash, 95% CI |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrCleanOkN` | n/a | P4 AsrCleanOk G1 T0 DeepSeekVFourFlash, n |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrCleanOkP` | n/a | P4 AsrCleanOk G1 T0 DeepSeekVFourFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroDeepSeekVFourFlashNonTargetAcc` | n/a | P4 NonTargetAcc G1 T0 DeepSeekVFourFlash [n/a: no data yet] |
| `\PfourGOneTZeroDeepSeekVFourFlashNonTargetAccLo` | n/a | P4 NonTargetAcc G1 T0 DeepSeekVFourFlash, lower 95% CI bound |
| `\PfourGOneTZeroDeepSeekVFourFlashNonTargetAccHi` | n/a | P4 NonTargetAcc G1 T0 DeepSeekVFourFlash, upper 95% CI bound |
| `\PfourGOneTZeroDeepSeekVFourFlashNonTargetAccCI` | n/a | P4 NonTargetAcc G1 T0 DeepSeekVFourFlash, 95% CI |
| `\PfourGOneTZeroDeepSeekVFourFlashNonTargetAccN` | n/a | P4 NonTargetAcc G1 T0 DeepSeekVFourFlash, n |
| `\PfourGOneTZeroDeepSeekVFourFlashNonTargetAccP` | n/a | P4 NonTargetAcc G1 T0 DeepSeekVFourFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsr` | n/a | P4 Asr G1 T0 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrLo` | n/a | P4 Asr G1 T0 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrHi` | n/a | P4 Asr G1 T0 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrCI` | n/a | P4 Asr G1 T0 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrN` | n/a | P4 Asr G1 T0 QwenThreeEightTwoSevenB, n |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrP` | n/a | P4 Asr G1 T0 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrDropped` | n/a | P4 AsrDropped G1 T0 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrDroppedLo` | n/a | P4 AsrDropped G1 T0 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrDroppedHi` | n/a | P4 AsrDropped G1 T0 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrDroppedCI` | n/a | P4 AsrDropped G1 T0 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrDroppedN` | n/a | P4 AsrDropped G1 T0 QwenThreeEightTwoSevenB, n |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrDroppedP` | n/a | P4 AsrDropped G1 T0 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrCleanOk` | n/a | P4 AsrCleanOk G1 T0 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrCleanOkLo` | n/a | P4 AsrCleanOk G1 T0 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrCleanOkHi` | n/a | P4 AsrCleanOk G1 T0 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrCleanOkCI` | n/a | P4 AsrCleanOk G1 T0 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrCleanOkN` | n/a | P4 AsrCleanOk G1 T0 QwenThreeEightTwoSevenB, n |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrCleanOkP` | n/a | P4 AsrCleanOk G1 T0 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBNonTargetAcc` | n/a | P4 NonTargetAcc G1 T0 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBNonTargetAccLo` | n/a | P4 NonTargetAcc G1 T0 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBNonTargetAccHi` | n/a | P4 NonTargetAcc G1 T0 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBNonTargetAccCI` | n/a | P4 NonTargetAcc G1 T0 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBNonTargetAccN` | n/a | P4 NonTargetAcc G1 T0 QwenThreeEightTwoSevenB, n |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBNonTargetAccP` | n/a | P4 NonTargetAcc G1 T0 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGemmaFourThreeOneBAsr` | n/a | P4 Asr G1 T0 GemmaFourThreeOneB [n/a: no data yet] |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrLo` | n/a | P4 Asr G1 T0 GemmaFourThreeOneB, lower 95% CI bound |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrHi` | n/a | P4 Asr G1 T0 GemmaFourThreeOneB, upper 95% CI bound |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrCI` | n/a | P4 Asr G1 T0 GemmaFourThreeOneB, 95% CI |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrN` | n/a | P4 Asr G1 T0 GemmaFourThreeOneB, n |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrP` | n/a | P4 Asr G1 T0 GemmaFourThreeOneB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrDropped` | n/a | P4 AsrDropped G1 T0 GemmaFourThreeOneB [n/a: no data yet] |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrDroppedLo` | n/a | P4 AsrDropped G1 T0 GemmaFourThreeOneB, lower 95% CI bound |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrDroppedHi` | n/a | P4 AsrDropped G1 T0 GemmaFourThreeOneB, upper 95% CI bound |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrDroppedCI` | n/a | P4 AsrDropped G1 T0 GemmaFourThreeOneB, 95% CI |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrDroppedN` | n/a | P4 AsrDropped G1 T0 GemmaFourThreeOneB, n |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrDroppedP` | n/a | P4 AsrDropped G1 T0 GemmaFourThreeOneB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrCleanOk` | n/a | P4 AsrCleanOk G1 T0 GemmaFourThreeOneB [n/a: no data yet] |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrCleanOkLo` | n/a | P4 AsrCleanOk G1 T0 GemmaFourThreeOneB, lower 95% CI bound |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrCleanOkHi` | n/a | P4 AsrCleanOk G1 T0 GemmaFourThreeOneB, upper 95% CI bound |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrCleanOkCI` | n/a | P4 AsrCleanOk G1 T0 GemmaFourThreeOneB, 95% CI |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrCleanOkN` | n/a | P4 AsrCleanOk G1 T0 GemmaFourThreeOneB, n |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrCleanOkP` | n/a | P4 AsrCleanOk G1 T0 GemmaFourThreeOneB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGemmaFourThreeOneBNonTargetAcc` | n/a | P4 NonTargetAcc G1 T0 GemmaFourThreeOneB [n/a: no data yet] |
| `\PfourGOneTZeroGemmaFourThreeOneBNonTargetAccLo` | n/a | P4 NonTargetAcc G1 T0 GemmaFourThreeOneB, lower 95% CI bound |
| `\PfourGOneTZeroGemmaFourThreeOneBNonTargetAccHi` | n/a | P4 NonTargetAcc G1 T0 GemmaFourThreeOneB, upper 95% CI bound |
| `\PfourGOneTZeroGemmaFourThreeOneBNonTargetAccCI` | n/a | P4 NonTargetAcc G1 T0 GemmaFourThreeOneB, 95% CI |
| `\PfourGOneTZeroGemmaFourThreeOneBNonTargetAccN` | n/a | P4 NonTargetAcc G1 T0 GemmaFourThreeOneB, n |
| `\PfourGOneTZeroGemmaFourThreeOneBNonTargetAccP` | n/a | P4 NonTargetAcc G1 T0 GemmaFourThreeOneB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGLMFiveThreeFlashAsr` | n/a | P4 Asr G1 T0 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrLo` | n/a | P4 Asr G1 T0 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrHi` | n/a | P4 Asr G1 T0 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrCI` | n/a | P4 Asr G1 T0 GLMFiveThreeFlash, 95% CI |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrN` | n/a | P4 Asr G1 T0 GLMFiveThreeFlash, n |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrP` | n/a | P4 Asr G1 T0 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrDropped` | n/a | P4 AsrDropped G1 T0 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrDroppedLo` | n/a | P4 AsrDropped G1 T0 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrDroppedHi` | n/a | P4 AsrDropped G1 T0 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrDroppedCI` | n/a | P4 AsrDropped G1 T0 GLMFiveThreeFlash, 95% CI |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrDroppedN` | n/a | P4 AsrDropped G1 T0 GLMFiveThreeFlash, n |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrDroppedP` | n/a | P4 AsrDropped G1 T0 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrCleanOk` | n/a | P4 AsrCleanOk G1 T0 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrCleanOkLo` | n/a | P4 AsrCleanOk G1 T0 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrCleanOkHi` | n/a | P4 AsrCleanOk G1 T0 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrCleanOkCI` | n/a | P4 AsrCleanOk G1 T0 GLMFiveThreeFlash, 95% CI |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrCleanOkN` | n/a | P4 AsrCleanOk G1 T0 GLMFiveThreeFlash, n |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrCleanOkP` | n/a | P4 AsrCleanOk G1 T0 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGLMFiveThreeFlashNonTargetAcc` | n/a | P4 NonTargetAcc G1 T0 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGOneTZeroGLMFiveThreeFlashNonTargetAccLo` | n/a | P4 NonTargetAcc G1 T0 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGOneTZeroGLMFiveThreeFlashNonTargetAccHi` | n/a | P4 NonTargetAcc G1 T0 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGOneTZeroGLMFiveThreeFlashNonTargetAccCI` | n/a | P4 NonTargetAcc G1 T0 GLMFiveThreeFlash, 95% CI |
| `\PfourGOneTZeroGLMFiveThreeFlashNonTargetAccN` | n/a | P4 NonTargetAcc G1 T0 GLMFiveThreeFlash, n |
| `\PfourGOneTZeroGLMFiveThreeFlashNonTargetAccP` | n/a | P4 NonTargetAcc G1 T0 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGLMFiveTwoAsr` | n/a | P4 Asr G1 T0 GLMFiveTwo [n/a: no data yet] |
| `\PfourGOneTZeroGLMFiveTwoAsrLo` | n/a | P4 Asr G1 T0 GLMFiveTwo, lower 95% CI bound |
| `\PfourGOneTZeroGLMFiveTwoAsrHi` | n/a | P4 Asr G1 T0 GLMFiveTwo, upper 95% CI bound |
| `\PfourGOneTZeroGLMFiveTwoAsrCI` | n/a | P4 Asr G1 T0 GLMFiveTwo, 95% CI |
| `\PfourGOneTZeroGLMFiveTwoAsrN` | n/a | P4 Asr G1 T0 GLMFiveTwo, n |
| `\PfourGOneTZeroGLMFiveTwoAsrP` | n/a | P4 Asr G1 T0 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGLMFiveTwoAsrDropped` | n/a | P4 AsrDropped G1 T0 GLMFiveTwo [n/a: no data yet] |
| `\PfourGOneTZeroGLMFiveTwoAsrDroppedLo` | n/a | P4 AsrDropped G1 T0 GLMFiveTwo, lower 95% CI bound |
| `\PfourGOneTZeroGLMFiveTwoAsrDroppedHi` | n/a | P4 AsrDropped G1 T0 GLMFiveTwo, upper 95% CI bound |
| `\PfourGOneTZeroGLMFiveTwoAsrDroppedCI` | n/a | P4 AsrDropped G1 T0 GLMFiveTwo, 95% CI |
| `\PfourGOneTZeroGLMFiveTwoAsrDroppedN` | n/a | P4 AsrDropped G1 T0 GLMFiveTwo, n |
| `\PfourGOneTZeroGLMFiveTwoAsrDroppedP` | n/a | P4 AsrDropped G1 T0 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGLMFiveTwoAsrCleanOk` | n/a | P4 AsrCleanOk G1 T0 GLMFiveTwo [n/a: no data yet] |
| `\PfourGOneTZeroGLMFiveTwoAsrCleanOkLo` | n/a | P4 AsrCleanOk G1 T0 GLMFiveTwo, lower 95% CI bound |
| `\PfourGOneTZeroGLMFiveTwoAsrCleanOkHi` | n/a | P4 AsrCleanOk G1 T0 GLMFiveTwo, upper 95% CI bound |
| `\PfourGOneTZeroGLMFiveTwoAsrCleanOkCI` | n/a | P4 AsrCleanOk G1 T0 GLMFiveTwo, 95% CI |
| `\PfourGOneTZeroGLMFiveTwoAsrCleanOkN` | n/a | P4 AsrCleanOk G1 T0 GLMFiveTwo, n |
| `\PfourGOneTZeroGLMFiveTwoAsrCleanOkP` | n/a | P4 AsrCleanOk G1 T0 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGLMFiveTwoNonTargetAcc` | n/a | P4 NonTargetAcc G1 T0 GLMFiveTwo [n/a: no data yet] |
| `\PfourGOneTZeroGLMFiveTwoNonTargetAccLo` | n/a | P4 NonTargetAcc G1 T0 GLMFiveTwo, lower 95% CI bound |
| `\PfourGOneTZeroGLMFiveTwoNonTargetAccHi` | n/a | P4 NonTargetAcc G1 T0 GLMFiveTwo, upper 95% CI bound |
| `\PfourGOneTZeroGLMFiveTwoNonTargetAccCI` | n/a | P4 NonTargetAcc G1 T0 GLMFiveTwo, 95% CI |
| `\PfourGOneTZeroGLMFiveTwoNonTargetAccN` | n/a | P4 NonTargetAcc G1 T0 GLMFiveTwo, n |
| `\PfourGOneTZeroGLMFiveTwoNonTargetAccP` | n/a | P4 NonTargetAcc G1 T0 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoPooledAsr` | n/a | P4 Asr G1 T2 Pooled [n/a: no data yet] |
| `\PfourGOneTTwoPooledAsrLo` | n/a | P4 Asr G1 T2 Pooled, lower 95% CI bound |
| `\PfourGOneTTwoPooledAsrHi` | n/a | P4 Asr G1 T2 Pooled, upper 95% CI bound |
| `\PfourGOneTTwoPooledAsrCI` | n/a | P4 Asr G1 T2 Pooled, 95% CI |
| `\PfourGOneTTwoPooledAsrN` | n/a | P4 Asr G1 T2 Pooled, n |
| `\PfourGOneTTwoPooledAsrP` | n/a | P4 Asr G1 T2 Pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoPooledAsrDropped` | n/a | P4 AsrDropped G1 T2 Pooled [n/a: no data yet] |
| `\PfourGOneTTwoPooledAsrDroppedLo` | n/a | P4 AsrDropped G1 T2 Pooled, lower 95% CI bound |
| `\PfourGOneTTwoPooledAsrDroppedHi` | n/a | P4 AsrDropped G1 T2 Pooled, upper 95% CI bound |
| `\PfourGOneTTwoPooledAsrDroppedCI` | n/a | P4 AsrDropped G1 T2 Pooled, 95% CI |
| `\PfourGOneTTwoPooledAsrDroppedN` | n/a | P4 AsrDropped G1 T2 Pooled, n |
| `\PfourGOneTTwoPooledAsrDroppedP` | n/a | P4 AsrDropped G1 T2 Pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoPooledAsrCleanOk` | n/a | P4 AsrCleanOk G1 T2 Pooled [n/a: no data yet] |
| `\PfourGOneTTwoPooledAsrCleanOkLo` | n/a | P4 AsrCleanOk G1 T2 Pooled, lower 95% CI bound |
| `\PfourGOneTTwoPooledAsrCleanOkHi` | n/a | P4 AsrCleanOk G1 T2 Pooled, upper 95% CI bound |
| `\PfourGOneTTwoPooledAsrCleanOkCI` | n/a | P4 AsrCleanOk G1 T2 Pooled, 95% CI |
| `\PfourGOneTTwoPooledAsrCleanOkN` | n/a | P4 AsrCleanOk G1 T2 Pooled, n |
| `\PfourGOneTTwoPooledAsrCleanOkP` | n/a | P4 AsrCleanOk G1 T2 Pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoPooledNonTargetAcc` | n/a | P4 NonTargetAcc G1 T2 Pooled [n/a: no data yet] |
| `\PfourGOneTTwoPooledNonTargetAccLo` | n/a | P4 NonTargetAcc G1 T2 Pooled, lower 95% CI bound |
| `\PfourGOneTTwoPooledNonTargetAccHi` | n/a | P4 NonTargetAcc G1 T2 Pooled, upper 95% CI bound |
| `\PfourGOneTTwoPooledNonTargetAccCI` | n/a | P4 NonTargetAcc G1 T2 Pooled, 95% CI |
| `\PfourGOneTTwoPooledNonTargetAccN` | n/a | P4 NonTargetAcc G1 T2 Pooled, n |
| `\PfourGOneTTwoPooledNonTargetAccP` | n/a | P4 NonTargetAcc G1 T2 Pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoDeepSeekVFourFlashAsr` | n/a | P4 Asr G1 T2 DeepSeekVFourFlash [n/a: no data yet] |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrLo` | n/a | P4 Asr G1 T2 DeepSeekVFourFlash, lower 95% CI bound |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrHi` | n/a | P4 Asr G1 T2 DeepSeekVFourFlash, upper 95% CI bound |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrCI` | n/a | P4 Asr G1 T2 DeepSeekVFourFlash, 95% CI |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrN` | n/a | P4 Asr G1 T2 DeepSeekVFourFlash, n |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrP` | n/a | P4 Asr G1 T2 DeepSeekVFourFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrDropped` | n/a | P4 AsrDropped G1 T2 DeepSeekVFourFlash [n/a: no data yet] |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrDroppedLo` | n/a | P4 AsrDropped G1 T2 DeepSeekVFourFlash, lower 95% CI bound |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrDroppedHi` | n/a | P4 AsrDropped G1 T2 DeepSeekVFourFlash, upper 95% CI bound |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrDroppedCI` | n/a | P4 AsrDropped G1 T2 DeepSeekVFourFlash, 95% CI |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrDroppedN` | n/a | P4 AsrDropped G1 T2 DeepSeekVFourFlash, n |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrDroppedP` | n/a | P4 AsrDropped G1 T2 DeepSeekVFourFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrCleanOk` | n/a | P4 AsrCleanOk G1 T2 DeepSeekVFourFlash [n/a: no data yet] |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrCleanOkLo` | n/a | P4 AsrCleanOk G1 T2 DeepSeekVFourFlash, lower 95% CI bound |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrCleanOkHi` | n/a | P4 AsrCleanOk G1 T2 DeepSeekVFourFlash, upper 95% CI bound |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrCleanOkCI` | n/a | P4 AsrCleanOk G1 T2 DeepSeekVFourFlash, 95% CI |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrCleanOkN` | n/a | P4 AsrCleanOk G1 T2 DeepSeekVFourFlash, n |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrCleanOkP` | n/a | P4 AsrCleanOk G1 T2 DeepSeekVFourFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoDeepSeekVFourFlashNonTargetAcc` | n/a | P4 NonTargetAcc G1 T2 DeepSeekVFourFlash [n/a: no data yet] |
| `\PfourGOneTTwoDeepSeekVFourFlashNonTargetAccLo` | n/a | P4 NonTargetAcc G1 T2 DeepSeekVFourFlash, lower 95% CI bound |
| `\PfourGOneTTwoDeepSeekVFourFlashNonTargetAccHi` | n/a | P4 NonTargetAcc G1 T2 DeepSeekVFourFlash, upper 95% CI bound |
| `\PfourGOneTTwoDeepSeekVFourFlashNonTargetAccCI` | n/a | P4 NonTargetAcc G1 T2 DeepSeekVFourFlash, 95% CI |
| `\PfourGOneTTwoDeepSeekVFourFlashNonTargetAccN` | n/a | P4 NonTargetAcc G1 T2 DeepSeekVFourFlash, n |
| `\PfourGOneTTwoDeepSeekVFourFlashNonTargetAccP` | n/a | P4 NonTargetAcc G1 T2 DeepSeekVFourFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsr` | n/a | P4 Asr G1 T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrLo` | n/a | P4 Asr G1 T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrHi` | n/a | P4 Asr G1 T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrCI` | n/a | P4 Asr G1 T2 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrN` | n/a | P4 Asr G1 T2 QwenThreeEightTwoSevenB, n |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrP` | n/a | P4 Asr G1 T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrDropped` | n/a | P4 AsrDropped G1 T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrDroppedLo` | n/a | P4 AsrDropped G1 T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrDroppedHi` | n/a | P4 AsrDropped G1 T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrDroppedCI` | n/a | P4 AsrDropped G1 T2 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrDroppedN` | n/a | P4 AsrDropped G1 T2 QwenThreeEightTwoSevenB, n |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrDroppedP` | n/a | P4 AsrDropped G1 T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrCleanOk` | n/a | P4 AsrCleanOk G1 T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrCleanOkLo` | n/a | P4 AsrCleanOk G1 T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrCleanOkHi` | n/a | P4 AsrCleanOk G1 T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrCleanOkCI` | n/a | P4 AsrCleanOk G1 T2 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrCleanOkN` | n/a | P4 AsrCleanOk G1 T2 QwenThreeEightTwoSevenB, n |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrCleanOkP` | n/a | P4 AsrCleanOk G1 T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBNonTargetAcc` | n/a | P4 NonTargetAcc G1 T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBNonTargetAccLo` | n/a | P4 NonTargetAcc G1 T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBNonTargetAccHi` | n/a | P4 NonTargetAcc G1 T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBNonTargetAccCI` | n/a | P4 NonTargetAcc G1 T2 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBNonTargetAccN` | n/a | P4 NonTargetAcc G1 T2 QwenThreeEightTwoSevenB, n |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBNonTargetAccP` | n/a | P4 NonTargetAcc G1 T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGemmaFourThreeOneBAsr` | n/a | P4 Asr G1 T2 GemmaFourThreeOneB [n/a: no data yet] |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrLo` | n/a | P4 Asr G1 T2 GemmaFourThreeOneB, lower 95% CI bound |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrHi` | n/a | P4 Asr G1 T2 GemmaFourThreeOneB, upper 95% CI bound |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrCI` | n/a | P4 Asr G1 T2 GemmaFourThreeOneB, 95% CI |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrN` | n/a | P4 Asr G1 T2 GemmaFourThreeOneB, n |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrP` | n/a | P4 Asr G1 T2 GemmaFourThreeOneB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrDropped` | n/a | P4 AsrDropped G1 T2 GemmaFourThreeOneB [n/a: no data yet] |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrDroppedLo` | n/a | P4 AsrDropped G1 T2 GemmaFourThreeOneB, lower 95% CI bound |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrDroppedHi` | n/a | P4 AsrDropped G1 T2 GemmaFourThreeOneB, upper 95% CI bound |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrDroppedCI` | n/a | P4 AsrDropped G1 T2 GemmaFourThreeOneB, 95% CI |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrDroppedN` | n/a | P4 AsrDropped G1 T2 GemmaFourThreeOneB, n |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrDroppedP` | n/a | P4 AsrDropped G1 T2 GemmaFourThreeOneB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrCleanOk` | n/a | P4 AsrCleanOk G1 T2 GemmaFourThreeOneB [n/a: no data yet] |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrCleanOkLo` | n/a | P4 AsrCleanOk G1 T2 GemmaFourThreeOneB, lower 95% CI bound |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrCleanOkHi` | n/a | P4 AsrCleanOk G1 T2 GemmaFourThreeOneB, upper 95% CI bound |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrCleanOkCI` | n/a | P4 AsrCleanOk G1 T2 GemmaFourThreeOneB, 95% CI |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrCleanOkN` | n/a | P4 AsrCleanOk G1 T2 GemmaFourThreeOneB, n |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrCleanOkP` | n/a | P4 AsrCleanOk G1 T2 GemmaFourThreeOneB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGemmaFourThreeOneBNonTargetAcc` | n/a | P4 NonTargetAcc G1 T2 GemmaFourThreeOneB [n/a: no data yet] |
| `\PfourGOneTTwoGemmaFourThreeOneBNonTargetAccLo` | n/a | P4 NonTargetAcc G1 T2 GemmaFourThreeOneB, lower 95% CI bound |
| `\PfourGOneTTwoGemmaFourThreeOneBNonTargetAccHi` | n/a | P4 NonTargetAcc G1 T2 GemmaFourThreeOneB, upper 95% CI bound |
| `\PfourGOneTTwoGemmaFourThreeOneBNonTargetAccCI` | n/a | P4 NonTargetAcc G1 T2 GemmaFourThreeOneB, 95% CI |
| `\PfourGOneTTwoGemmaFourThreeOneBNonTargetAccN` | n/a | P4 NonTargetAcc G1 T2 GemmaFourThreeOneB, n |
| `\PfourGOneTTwoGemmaFourThreeOneBNonTargetAccP` | n/a | P4 NonTargetAcc G1 T2 GemmaFourThreeOneB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGLMFiveThreeFlashAsr` | n/a | P4 Asr G1 T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrLo` | n/a | P4 Asr G1 T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrHi` | n/a | P4 Asr G1 T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrCI` | n/a | P4 Asr G1 T2 GLMFiveThreeFlash, 95% CI |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrN` | n/a | P4 Asr G1 T2 GLMFiveThreeFlash, n |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrP` | n/a | P4 Asr G1 T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrDropped` | n/a | P4 AsrDropped G1 T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrDroppedLo` | n/a | P4 AsrDropped G1 T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrDroppedHi` | n/a | P4 AsrDropped G1 T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrDroppedCI` | n/a | P4 AsrDropped G1 T2 GLMFiveThreeFlash, 95% CI |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrDroppedN` | n/a | P4 AsrDropped G1 T2 GLMFiveThreeFlash, n |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrDroppedP` | n/a | P4 AsrDropped G1 T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrCleanOk` | n/a | P4 AsrCleanOk G1 T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrCleanOkLo` | n/a | P4 AsrCleanOk G1 T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrCleanOkHi` | n/a | P4 AsrCleanOk G1 T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrCleanOkCI` | n/a | P4 AsrCleanOk G1 T2 GLMFiveThreeFlash, 95% CI |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrCleanOkN` | n/a | P4 AsrCleanOk G1 T2 GLMFiveThreeFlash, n |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrCleanOkP` | n/a | P4 AsrCleanOk G1 T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGLMFiveThreeFlashNonTargetAcc` | n/a | P4 NonTargetAcc G1 T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGOneTTwoGLMFiveThreeFlashNonTargetAccLo` | n/a | P4 NonTargetAcc G1 T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGOneTTwoGLMFiveThreeFlashNonTargetAccHi` | n/a | P4 NonTargetAcc G1 T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGOneTTwoGLMFiveThreeFlashNonTargetAccCI` | n/a | P4 NonTargetAcc G1 T2 GLMFiveThreeFlash, 95% CI |
| `\PfourGOneTTwoGLMFiveThreeFlashNonTargetAccN` | n/a | P4 NonTargetAcc G1 T2 GLMFiveThreeFlash, n |
| `\PfourGOneTTwoGLMFiveThreeFlashNonTargetAccP` | n/a | P4 NonTargetAcc G1 T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGLMFiveTwoAsr` | n/a | P4 Asr G1 T2 GLMFiveTwo [n/a: no data yet] |
| `\PfourGOneTTwoGLMFiveTwoAsrLo` | n/a | P4 Asr G1 T2 GLMFiveTwo, lower 95% CI bound |
| `\PfourGOneTTwoGLMFiveTwoAsrHi` | n/a | P4 Asr G1 T2 GLMFiveTwo, upper 95% CI bound |
| `\PfourGOneTTwoGLMFiveTwoAsrCI` | n/a | P4 Asr G1 T2 GLMFiveTwo, 95% CI |
| `\PfourGOneTTwoGLMFiveTwoAsrN` | n/a | P4 Asr G1 T2 GLMFiveTwo, n |
| `\PfourGOneTTwoGLMFiveTwoAsrP` | n/a | P4 Asr G1 T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGLMFiveTwoAsrDropped` | n/a | P4 AsrDropped G1 T2 GLMFiveTwo [n/a: no data yet] |
| `\PfourGOneTTwoGLMFiveTwoAsrDroppedLo` | n/a | P4 AsrDropped G1 T2 GLMFiveTwo, lower 95% CI bound |
| `\PfourGOneTTwoGLMFiveTwoAsrDroppedHi` | n/a | P4 AsrDropped G1 T2 GLMFiveTwo, upper 95% CI bound |
| `\PfourGOneTTwoGLMFiveTwoAsrDroppedCI` | n/a | P4 AsrDropped G1 T2 GLMFiveTwo, 95% CI |
| `\PfourGOneTTwoGLMFiveTwoAsrDroppedN` | n/a | P4 AsrDropped G1 T2 GLMFiveTwo, n |
| `\PfourGOneTTwoGLMFiveTwoAsrDroppedP` | n/a | P4 AsrDropped G1 T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGLMFiveTwoAsrCleanOk` | n/a | P4 AsrCleanOk G1 T2 GLMFiveTwo [n/a: no data yet] |
| `\PfourGOneTTwoGLMFiveTwoAsrCleanOkLo` | n/a | P4 AsrCleanOk G1 T2 GLMFiveTwo, lower 95% CI bound |
| `\PfourGOneTTwoGLMFiveTwoAsrCleanOkHi` | n/a | P4 AsrCleanOk G1 T2 GLMFiveTwo, upper 95% CI bound |
| `\PfourGOneTTwoGLMFiveTwoAsrCleanOkCI` | n/a | P4 AsrCleanOk G1 T2 GLMFiveTwo, 95% CI |
| `\PfourGOneTTwoGLMFiveTwoAsrCleanOkN` | n/a | P4 AsrCleanOk G1 T2 GLMFiveTwo, n |
| `\PfourGOneTTwoGLMFiveTwoAsrCleanOkP` | n/a | P4 AsrCleanOk G1 T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGLMFiveTwoNonTargetAcc` | n/a | P4 NonTargetAcc G1 T2 GLMFiveTwo [n/a: no data yet] |
| `\PfourGOneTTwoGLMFiveTwoNonTargetAccLo` | n/a | P4 NonTargetAcc G1 T2 GLMFiveTwo, lower 95% CI bound |
| `\PfourGOneTTwoGLMFiveTwoNonTargetAccHi` | n/a | P4 NonTargetAcc G1 T2 GLMFiveTwo, upper 95% CI bound |
| `\PfourGOneTTwoGLMFiveTwoNonTargetAccCI` | n/a | P4 NonTargetAcc G1 T2 GLMFiveTwo, 95% CI |
| `\PfourGOneTTwoGLMFiveTwoNonTargetAccN` | n/a | P4 NonTargetAcc G1 T2 GLMFiveTwo, n |
| `\PfourGOneTTwoGLMFiveTwoNonTargetAccP` | n/a | P4 NonTargetAcc G1 T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreePooledAsr` | n/a | P4 Asr G1 T3 Pooled [n/a: no data yet] |
| `\PfourGOneTThreePooledAsrLo` | n/a | P4 Asr G1 T3 Pooled, lower 95% CI bound |
| `\PfourGOneTThreePooledAsrHi` | n/a | P4 Asr G1 T3 Pooled, upper 95% CI bound |
| `\PfourGOneTThreePooledAsrCI` | n/a | P4 Asr G1 T3 Pooled, 95% CI |
| `\PfourGOneTThreePooledAsrN` | n/a | P4 Asr G1 T3 Pooled, n |
| `\PfourGOneTThreePooledAsrP` | n/a | P4 Asr G1 T3 Pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreePooledAsrDropped` | n/a | P4 AsrDropped G1 T3 Pooled [n/a: no data yet] |
| `\PfourGOneTThreePooledAsrDroppedLo` | n/a | P4 AsrDropped G1 T3 Pooled, lower 95% CI bound |
| `\PfourGOneTThreePooledAsrDroppedHi` | n/a | P4 AsrDropped G1 T3 Pooled, upper 95% CI bound |
| `\PfourGOneTThreePooledAsrDroppedCI` | n/a | P4 AsrDropped G1 T3 Pooled, 95% CI |
| `\PfourGOneTThreePooledAsrDroppedN` | n/a | P4 AsrDropped G1 T3 Pooled, n |
| `\PfourGOneTThreePooledAsrDroppedP` | n/a | P4 AsrDropped G1 T3 Pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreePooledAsrCleanOk` | n/a | P4 AsrCleanOk G1 T3 Pooled [n/a: no data yet] |
| `\PfourGOneTThreePooledAsrCleanOkLo` | n/a | P4 AsrCleanOk G1 T3 Pooled, lower 95% CI bound |
| `\PfourGOneTThreePooledAsrCleanOkHi` | n/a | P4 AsrCleanOk G1 T3 Pooled, upper 95% CI bound |
| `\PfourGOneTThreePooledAsrCleanOkCI` | n/a | P4 AsrCleanOk G1 T3 Pooled, 95% CI |
| `\PfourGOneTThreePooledAsrCleanOkN` | n/a | P4 AsrCleanOk G1 T3 Pooled, n |
| `\PfourGOneTThreePooledAsrCleanOkP` | n/a | P4 AsrCleanOk G1 T3 Pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreePooledNonTargetAcc` | n/a | P4 NonTargetAcc G1 T3 Pooled [n/a: no data yet] |
| `\PfourGOneTThreePooledNonTargetAccLo` | n/a | P4 NonTargetAcc G1 T3 Pooled, lower 95% CI bound |
| `\PfourGOneTThreePooledNonTargetAccHi` | n/a | P4 NonTargetAcc G1 T3 Pooled, upper 95% CI bound |
| `\PfourGOneTThreePooledNonTargetAccCI` | n/a | P4 NonTargetAcc G1 T3 Pooled, 95% CI |
| `\PfourGOneTThreePooledNonTargetAccN` | n/a | P4 NonTargetAcc G1 T3 Pooled, n |
| `\PfourGOneTThreePooledNonTargetAccP` | n/a | P4 NonTargetAcc G1 T3 Pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeDeepSeekVFourFlashAsr` | n/a | P4 Asr G1 T3 DeepSeekVFourFlash [n/a: no data yet] |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrLo` | n/a | P4 Asr G1 T3 DeepSeekVFourFlash, lower 95% CI bound |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrHi` | n/a | P4 Asr G1 T3 DeepSeekVFourFlash, upper 95% CI bound |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrCI` | n/a | P4 Asr G1 T3 DeepSeekVFourFlash, 95% CI |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrN` | n/a | P4 Asr G1 T3 DeepSeekVFourFlash, n |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrP` | n/a | P4 Asr G1 T3 DeepSeekVFourFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrDropped` | n/a | P4 AsrDropped G1 T3 DeepSeekVFourFlash [n/a: no data yet] |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrDroppedLo` | n/a | P4 AsrDropped G1 T3 DeepSeekVFourFlash, lower 95% CI bound |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrDroppedHi` | n/a | P4 AsrDropped G1 T3 DeepSeekVFourFlash, upper 95% CI bound |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrDroppedCI` | n/a | P4 AsrDropped G1 T3 DeepSeekVFourFlash, 95% CI |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrDroppedN` | n/a | P4 AsrDropped G1 T3 DeepSeekVFourFlash, n |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrDroppedP` | n/a | P4 AsrDropped G1 T3 DeepSeekVFourFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrCleanOk` | n/a | P4 AsrCleanOk G1 T3 DeepSeekVFourFlash [n/a: no data yet] |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrCleanOkLo` | n/a | P4 AsrCleanOk G1 T3 DeepSeekVFourFlash, lower 95% CI bound |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrCleanOkHi` | n/a | P4 AsrCleanOk G1 T3 DeepSeekVFourFlash, upper 95% CI bound |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrCleanOkCI` | n/a | P4 AsrCleanOk G1 T3 DeepSeekVFourFlash, 95% CI |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrCleanOkN` | n/a | P4 AsrCleanOk G1 T3 DeepSeekVFourFlash, n |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrCleanOkP` | n/a | P4 AsrCleanOk G1 T3 DeepSeekVFourFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeDeepSeekVFourFlashNonTargetAcc` | n/a | P4 NonTargetAcc G1 T3 DeepSeekVFourFlash [n/a: no data yet] |
| `\PfourGOneTThreeDeepSeekVFourFlashNonTargetAccLo` | n/a | P4 NonTargetAcc G1 T3 DeepSeekVFourFlash, lower 95% CI bound |
| `\PfourGOneTThreeDeepSeekVFourFlashNonTargetAccHi` | n/a | P4 NonTargetAcc G1 T3 DeepSeekVFourFlash, upper 95% CI bound |
| `\PfourGOneTThreeDeepSeekVFourFlashNonTargetAccCI` | n/a | P4 NonTargetAcc G1 T3 DeepSeekVFourFlash, 95% CI |
| `\PfourGOneTThreeDeepSeekVFourFlashNonTargetAccN` | n/a | P4 NonTargetAcc G1 T3 DeepSeekVFourFlash, n |
| `\PfourGOneTThreeDeepSeekVFourFlashNonTargetAccP` | n/a | P4 NonTargetAcc G1 T3 DeepSeekVFourFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsr` | n/a | P4 Asr G1 T3 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrLo` | n/a | P4 Asr G1 T3 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrHi` | n/a | P4 Asr G1 T3 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrCI` | n/a | P4 Asr G1 T3 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrN` | n/a | P4 Asr G1 T3 QwenThreeEightTwoSevenB, n |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrP` | n/a | P4 Asr G1 T3 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrDropped` | n/a | P4 AsrDropped G1 T3 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrDroppedLo` | n/a | P4 AsrDropped G1 T3 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrDroppedHi` | n/a | P4 AsrDropped G1 T3 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrDroppedCI` | n/a | P4 AsrDropped G1 T3 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrDroppedN` | n/a | P4 AsrDropped G1 T3 QwenThreeEightTwoSevenB, n |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrDroppedP` | n/a | P4 AsrDropped G1 T3 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrCleanOk` | n/a | P4 AsrCleanOk G1 T3 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrCleanOkLo` | n/a | P4 AsrCleanOk G1 T3 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrCleanOkHi` | n/a | P4 AsrCleanOk G1 T3 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrCleanOkCI` | n/a | P4 AsrCleanOk G1 T3 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrCleanOkN` | n/a | P4 AsrCleanOk G1 T3 QwenThreeEightTwoSevenB, n |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrCleanOkP` | n/a | P4 AsrCleanOk G1 T3 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBNonTargetAcc` | n/a | P4 NonTargetAcc G1 T3 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBNonTargetAccLo` | n/a | P4 NonTargetAcc G1 T3 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBNonTargetAccHi` | n/a | P4 NonTargetAcc G1 T3 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBNonTargetAccCI` | n/a | P4 NonTargetAcc G1 T3 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBNonTargetAccN` | n/a | P4 NonTargetAcc G1 T3 QwenThreeEightTwoSevenB, n |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBNonTargetAccP` | n/a | P4 NonTargetAcc G1 T3 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGemmaFourThreeOneBAsr` | n/a | P4 Asr G1 T3 GemmaFourThreeOneB [n/a: no data yet] |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrLo` | n/a | P4 Asr G1 T3 GemmaFourThreeOneB, lower 95% CI bound |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrHi` | n/a | P4 Asr G1 T3 GemmaFourThreeOneB, upper 95% CI bound |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrCI` | n/a | P4 Asr G1 T3 GemmaFourThreeOneB, 95% CI |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrN` | n/a | P4 Asr G1 T3 GemmaFourThreeOneB, n |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrP` | n/a | P4 Asr G1 T3 GemmaFourThreeOneB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrDropped` | n/a | P4 AsrDropped G1 T3 GemmaFourThreeOneB [n/a: no data yet] |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrDroppedLo` | n/a | P4 AsrDropped G1 T3 GemmaFourThreeOneB, lower 95% CI bound |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrDroppedHi` | n/a | P4 AsrDropped G1 T3 GemmaFourThreeOneB, upper 95% CI bound |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrDroppedCI` | n/a | P4 AsrDropped G1 T3 GemmaFourThreeOneB, 95% CI |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrDroppedN` | n/a | P4 AsrDropped G1 T3 GemmaFourThreeOneB, n |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrDroppedP` | n/a | P4 AsrDropped G1 T3 GemmaFourThreeOneB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrCleanOk` | n/a | P4 AsrCleanOk G1 T3 GemmaFourThreeOneB [n/a: no data yet] |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrCleanOkLo` | n/a | P4 AsrCleanOk G1 T3 GemmaFourThreeOneB, lower 95% CI bound |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrCleanOkHi` | n/a | P4 AsrCleanOk G1 T3 GemmaFourThreeOneB, upper 95% CI bound |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrCleanOkCI` | n/a | P4 AsrCleanOk G1 T3 GemmaFourThreeOneB, 95% CI |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrCleanOkN` | n/a | P4 AsrCleanOk G1 T3 GemmaFourThreeOneB, n |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrCleanOkP` | n/a | P4 AsrCleanOk G1 T3 GemmaFourThreeOneB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGemmaFourThreeOneBNonTargetAcc` | n/a | P4 NonTargetAcc G1 T3 GemmaFourThreeOneB [n/a: no data yet] |
| `\PfourGOneTThreeGemmaFourThreeOneBNonTargetAccLo` | n/a | P4 NonTargetAcc G1 T3 GemmaFourThreeOneB, lower 95% CI bound |
| `\PfourGOneTThreeGemmaFourThreeOneBNonTargetAccHi` | n/a | P4 NonTargetAcc G1 T3 GemmaFourThreeOneB, upper 95% CI bound |
| `\PfourGOneTThreeGemmaFourThreeOneBNonTargetAccCI` | n/a | P4 NonTargetAcc G1 T3 GemmaFourThreeOneB, 95% CI |
| `\PfourGOneTThreeGemmaFourThreeOneBNonTargetAccN` | n/a | P4 NonTargetAcc G1 T3 GemmaFourThreeOneB, n |
| `\PfourGOneTThreeGemmaFourThreeOneBNonTargetAccP` | n/a | P4 NonTargetAcc G1 T3 GemmaFourThreeOneB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGLMFiveThreeFlashAsr` | n/a | P4 Asr G1 T3 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrLo` | n/a | P4 Asr G1 T3 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrHi` | n/a | P4 Asr G1 T3 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrCI` | n/a | P4 Asr G1 T3 GLMFiveThreeFlash, 95% CI |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrN` | n/a | P4 Asr G1 T3 GLMFiveThreeFlash, n |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrP` | n/a | P4 Asr G1 T3 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrDropped` | n/a | P4 AsrDropped G1 T3 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrDroppedLo` | n/a | P4 AsrDropped G1 T3 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrDroppedHi` | n/a | P4 AsrDropped G1 T3 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrDroppedCI` | n/a | P4 AsrDropped G1 T3 GLMFiveThreeFlash, 95% CI |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrDroppedN` | n/a | P4 AsrDropped G1 T3 GLMFiveThreeFlash, n |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrDroppedP` | n/a | P4 AsrDropped G1 T3 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrCleanOk` | n/a | P4 AsrCleanOk G1 T3 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrCleanOkLo` | n/a | P4 AsrCleanOk G1 T3 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrCleanOkHi` | n/a | P4 AsrCleanOk G1 T3 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrCleanOkCI` | n/a | P4 AsrCleanOk G1 T3 GLMFiveThreeFlash, 95% CI |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrCleanOkN` | n/a | P4 AsrCleanOk G1 T3 GLMFiveThreeFlash, n |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrCleanOkP` | n/a | P4 AsrCleanOk G1 T3 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGLMFiveThreeFlashNonTargetAcc` | n/a | P4 NonTargetAcc G1 T3 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGOneTThreeGLMFiveThreeFlashNonTargetAccLo` | n/a | P4 NonTargetAcc G1 T3 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGOneTThreeGLMFiveThreeFlashNonTargetAccHi` | n/a | P4 NonTargetAcc G1 T3 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGOneTThreeGLMFiveThreeFlashNonTargetAccCI` | n/a | P4 NonTargetAcc G1 T3 GLMFiveThreeFlash, 95% CI |
| `\PfourGOneTThreeGLMFiveThreeFlashNonTargetAccN` | n/a | P4 NonTargetAcc G1 T3 GLMFiveThreeFlash, n |
| `\PfourGOneTThreeGLMFiveThreeFlashNonTargetAccP` | n/a | P4 NonTargetAcc G1 T3 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGLMFiveTwoAsr` | n/a | P4 Asr G1 T3 GLMFiveTwo [n/a: no data yet] |
| `\PfourGOneTThreeGLMFiveTwoAsrLo` | n/a | P4 Asr G1 T3 GLMFiveTwo, lower 95% CI bound |
| `\PfourGOneTThreeGLMFiveTwoAsrHi` | n/a | P4 Asr G1 T3 GLMFiveTwo, upper 95% CI bound |
| `\PfourGOneTThreeGLMFiveTwoAsrCI` | n/a | P4 Asr G1 T3 GLMFiveTwo, 95% CI |
| `\PfourGOneTThreeGLMFiveTwoAsrN` | n/a | P4 Asr G1 T3 GLMFiveTwo, n |
| `\PfourGOneTThreeGLMFiveTwoAsrP` | n/a | P4 Asr G1 T3 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGLMFiveTwoAsrDropped` | n/a | P4 AsrDropped G1 T3 GLMFiveTwo [n/a: no data yet] |
| `\PfourGOneTThreeGLMFiveTwoAsrDroppedLo` | n/a | P4 AsrDropped G1 T3 GLMFiveTwo, lower 95% CI bound |
| `\PfourGOneTThreeGLMFiveTwoAsrDroppedHi` | n/a | P4 AsrDropped G1 T3 GLMFiveTwo, upper 95% CI bound |
| `\PfourGOneTThreeGLMFiveTwoAsrDroppedCI` | n/a | P4 AsrDropped G1 T3 GLMFiveTwo, 95% CI |
| `\PfourGOneTThreeGLMFiveTwoAsrDroppedN` | n/a | P4 AsrDropped G1 T3 GLMFiveTwo, n |
| `\PfourGOneTThreeGLMFiveTwoAsrDroppedP` | n/a | P4 AsrDropped G1 T3 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGLMFiveTwoAsrCleanOk` | n/a | P4 AsrCleanOk G1 T3 GLMFiveTwo [n/a: no data yet] |
| `\PfourGOneTThreeGLMFiveTwoAsrCleanOkLo` | n/a | P4 AsrCleanOk G1 T3 GLMFiveTwo, lower 95% CI bound |
| `\PfourGOneTThreeGLMFiveTwoAsrCleanOkHi` | n/a | P4 AsrCleanOk G1 T3 GLMFiveTwo, upper 95% CI bound |
| `\PfourGOneTThreeGLMFiveTwoAsrCleanOkCI` | n/a | P4 AsrCleanOk G1 T3 GLMFiveTwo, 95% CI |
| `\PfourGOneTThreeGLMFiveTwoAsrCleanOkN` | n/a | P4 AsrCleanOk G1 T3 GLMFiveTwo, n |
| `\PfourGOneTThreeGLMFiveTwoAsrCleanOkP` | n/a | P4 AsrCleanOk G1 T3 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGLMFiveTwoNonTargetAcc` | n/a | P4 NonTargetAcc G1 T3 GLMFiveTwo [n/a: no data yet] |
| `\PfourGOneTThreeGLMFiveTwoNonTargetAccLo` | n/a | P4 NonTargetAcc G1 T3 GLMFiveTwo, lower 95% CI bound |
| `\PfourGOneTThreeGLMFiveTwoNonTargetAccHi` | n/a | P4 NonTargetAcc G1 T3 GLMFiveTwo, upper 95% CI bound |
| `\PfourGOneTThreeGLMFiveTwoNonTargetAccCI` | n/a | P4 NonTargetAcc G1 T3 GLMFiveTwo, 95% CI |
| `\PfourGOneTThreeGLMFiveTwoNonTargetAccN` | n/a | P4 NonTargetAcc G1 T3 GLMFiveTwo, n |
| `\PfourGOneTThreeGLMFiveTwoNonTargetAccP` | n/a | P4 NonTargetAcc G1 T3 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsr` | n/a | P4 Asr G2u T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrLo` | n/a | P4 Asr G2u T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrHi` | n/a | P4 Asr G2u T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrCI` | n/a | P4 Asr G2u T2 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrN` | n/a | P4 Asr G2u T2 QwenThreeEightTwoSevenB, n |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrP` | n/a | P4 Asr G2u T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrDropped` | n/a | P4 AsrDropped G2u T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrDroppedLo` | n/a | P4 AsrDropped G2u T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrDroppedHi` | n/a | P4 AsrDropped G2u T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrDroppedCI` | n/a | P4 AsrDropped G2u T2 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrDroppedN` | n/a | P4 AsrDropped G2u T2 QwenThreeEightTwoSevenB, n |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrDroppedP` | n/a | P4 AsrDropped G2u T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrCleanOk` | n/a | P4 AsrCleanOk G2u T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrCleanOkLo` | n/a | P4 AsrCleanOk G2u T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrCleanOkHi` | n/a | P4 AsrCleanOk G2u T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrCleanOkCI` | n/a | P4 AsrCleanOk G2u T2 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrCleanOkN` | n/a | P4 AsrCleanOk G2u T2 QwenThreeEightTwoSevenB, n |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrCleanOkP` | n/a | P4 AsrCleanOk G2u T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBNonTargetAcc` | n/a | P4 NonTargetAcc G2u T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBNonTargetAccLo` | n/a | P4 NonTargetAcc G2u T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBNonTargetAccHi` | n/a | P4 NonTargetAcc G2u T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBNonTargetAccCI` | n/a | P4 NonTargetAcc G2u T2 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBNonTargetAccN` | n/a | P4 NonTargetAcc G2u T2 QwenThreeEightTwoSevenB, n |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBNonTargetAccP` | n/a | P4 NonTargetAcc G2u T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsr` | n/a | P4 Asr G2u T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrLo` | n/a | P4 Asr G2u T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrHi` | n/a | P4 Asr G2u T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrCI` | n/a | P4 Asr G2u T2 GLMFiveThreeFlash, 95% CI |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrN` | n/a | P4 Asr G2u T2 GLMFiveThreeFlash, n |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrP` | n/a | P4 Asr G2u T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrDropped` | n/a | P4 AsrDropped G2u T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrDroppedLo` | n/a | P4 AsrDropped G2u T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrDroppedHi` | n/a | P4 AsrDropped G2u T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrDroppedCI` | n/a | P4 AsrDropped G2u T2 GLMFiveThreeFlash, 95% CI |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrDroppedN` | n/a | P4 AsrDropped G2u T2 GLMFiveThreeFlash, n |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrDroppedP` | n/a | P4 AsrDropped G2u T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrCleanOk` | n/a | P4 AsrCleanOk G2u T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrCleanOkLo` | n/a | P4 AsrCleanOk G2u T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrCleanOkHi` | n/a | P4 AsrCleanOk G2u T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrCleanOkCI` | n/a | P4 AsrCleanOk G2u T2 GLMFiveThreeFlash, 95% CI |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrCleanOkN` | n/a | P4 AsrCleanOk G2u T2 GLMFiveThreeFlash, n |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrCleanOkP` | n/a | P4 AsrCleanOk G2u T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGLMFiveThreeFlashNonTargetAcc` | n/a | P4 NonTargetAcc G2u T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGTwoUTTwoGLMFiveThreeFlashNonTargetAccLo` | n/a | P4 NonTargetAcc G2u T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveThreeFlashNonTargetAccHi` | n/a | P4 NonTargetAcc G2u T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveThreeFlashNonTargetAccCI` | n/a | P4 NonTargetAcc G2u T2 GLMFiveThreeFlash, 95% CI |
| `\PfourGTwoUTTwoGLMFiveThreeFlashNonTargetAccN` | n/a | P4 NonTargetAcc G2u T2 GLMFiveThreeFlash, n |
| `\PfourGTwoUTTwoGLMFiveThreeFlashNonTargetAccP` | n/a | P4 NonTargetAcc G2u T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGLMFiveTwoAsr` | n/a | P4 Asr G2u T2 GLMFiveTwo [n/a: no data yet] |
| `\PfourGTwoUTTwoGLMFiveTwoAsrLo` | n/a | P4 Asr G2u T2 GLMFiveTwo, lower 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveTwoAsrHi` | n/a | P4 Asr G2u T2 GLMFiveTwo, upper 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveTwoAsrCI` | n/a | P4 Asr G2u T2 GLMFiveTwo, 95% CI |
| `\PfourGTwoUTTwoGLMFiveTwoAsrN` | n/a | P4 Asr G2u T2 GLMFiveTwo, n |
| `\PfourGTwoUTTwoGLMFiveTwoAsrP` | n/a | P4 Asr G2u T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGLMFiveTwoAsrDropped` | n/a | P4 AsrDropped G2u T2 GLMFiveTwo [n/a: no data yet] |
| `\PfourGTwoUTTwoGLMFiveTwoAsrDroppedLo` | n/a | P4 AsrDropped G2u T2 GLMFiveTwo, lower 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveTwoAsrDroppedHi` | n/a | P4 AsrDropped G2u T2 GLMFiveTwo, upper 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveTwoAsrDroppedCI` | n/a | P4 AsrDropped G2u T2 GLMFiveTwo, 95% CI |
| `\PfourGTwoUTTwoGLMFiveTwoAsrDroppedN` | n/a | P4 AsrDropped G2u T2 GLMFiveTwo, n |
| `\PfourGTwoUTTwoGLMFiveTwoAsrDroppedP` | n/a | P4 AsrDropped G2u T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGLMFiveTwoAsrCleanOk` | n/a | P4 AsrCleanOk G2u T2 GLMFiveTwo [n/a: no data yet] |
| `\PfourGTwoUTTwoGLMFiveTwoAsrCleanOkLo` | n/a | P4 AsrCleanOk G2u T2 GLMFiveTwo, lower 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveTwoAsrCleanOkHi` | n/a | P4 AsrCleanOk G2u T2 GLMFiveTwo, upper 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveTwoAsrCleanOkCI` | n/a | P4 AsrCleanOk G2u T2 GLMFiveTwo, 95% CI |
| `\PfourGTwoUTTwoGLMFiveTwoAsrCleanOkN` | n/a | P4 AsrCleanOk G2u T2 GLMFiveTwo, n |
| `\PfourGTwoUTTwoGLMFiveTwoAsrCleanOkP` | n/a | P4 AsrCleanOk G2u T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGLMFiveTwoNonTargetAcc` | n/a | P4 NonTargetAcc G2u T2 GLMFiveTwo [n/a: no data yet] |
| `\PfourGTwoUTTwoGLMFiveTwoNonTargetAccLo` | n/a | P4 NonTargetAcc G2u T2 GLMFiveTwo, lower 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveTwoNonTargetAccHi` | n/a | P4 NonTargetAcc G2u T2 GLMFiveTwo, upper 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveTwoNonTargetAccCI` | n/a | P4 NonTargetAcc G2u T2 GLMFiveTwo, 95% CI |
| `\PfourGTwoUTTwoGLMFiveTwoNonTargetAccN` | n/a | P4 NonTargetAcc G2u T2 GLMFiveTwo, n |
| `\PfourGTwoUTTwoGLMFiveTwoNonTargetAccP` | n/a | P4 NonTargetAcc G2u T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsr` | n/a | P4 Asr G2s T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrLo` | n/a | P4 Asr G2s T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrHi` | n/a | P4 Asr G2s T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrCI` | n/a | P4 Asr G2s T2 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrN` | n/a | P4 Asr G2s T2 QwenThreeEightTwoSevenB, n |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrP` | n/a | P4 Asr G2s T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrDropped` | n/a | P4 AsrDropped G2s T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrDroppedLo` | n/a | P4 AsrDropped G2s T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrDroppedHi` | n/a | P4 AsrDropped G2s T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrDroppedCI` | n/a | P4 AsrDropped G2s T2 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrDroppedN` | n/a | P4 AsrDropped G2s T2 QwenThreeEightTwoSevenB, n |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrDroppedP` | n/a | P4 AsrDropped G2s T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrCleanOk` | n/a | P4 AsrCleanOk G2s T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrCleanOkLo` | n/a | P4 AsrCleanOk G2s T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrCleanOkHi` | n/a | P4 AsrCleanOk G2s T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrCleanOkCI` | n/a | P4 AsrCleanOk G2s T2 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrCleanOkN` | n/a | P4 AsrCleanOk G2s T2 QwenThreeEightTwoSevenB, n |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrCleanOkP` | n/a | P4 AsrCleanOk G2s T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBNonTargetAcc` | n/a | P4 NonTargetAcc G2s T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBNonTargetAccLo` | n/a | P4 NonTargetAcc G2s T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBNonTargetAccHi` | n/a | P4 NonTargetAcc G2s T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBNonTargetAccCI` | n/a | P4 NonTargetAcc G2s T2 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBNonTargetAccN` | n/a | P4 NonTargetAcc G2s T2 QwenThreeEightTwoSevenB, n |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBNonTargetAccP` | n/a | P4 NonTargetAcc G2s T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsr` | n/a | P4 Asr G2s T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrLo` | n/a | P4 Asr G2s T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrHi` | n/a | P4 Asr G2s T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrCI` | n/a | P4 Asr G2s T2 GLMFiveThreeFlash, 95% CI |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrN` | n/a | P4 Asr G2s T2 GLMFiveThreeFlash, n |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrP` | n/a | P4 Asr G2s T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrDropped` | n/a | P4 AsrDropped G2s T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrDroppedLo` | n/a | P4 AsrDropped G2s T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrDroppedHi` | n/a | P4 AsrDropped G2s T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrDroppedCI` | n/a | P4 AsrDropped G2s T2 GLMFiveThreeFlash, 95% CI |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrDroppedN` | n/a | P4 AsrDropped G2s T2 GLMFiveThreeFlash, n |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrDroppedP` | n/a | P4 AsrDropped G2s T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrCleanOk` | n/a | P4 AsrCleanOk G2s T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrCleanOkLo` | n/a | P4 AsrCleanOk G2s T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrCleanOkHi` | n/a | P4 AsrCleanOk G2s T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrCleanOkCI` | n/a | P4 AsrCleanOk G2s T2 GLMFiveThreeFlash, 95% CI |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrCleanOkN` | n/a | P4 AsrCleanOk G2s T2 GLMFiveThreeFlash, n |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrCleanOkP` | n/a | P4 AsrCleanOk G2s T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGLMFiveThreeFlashNonTargetAcc` | n/a | P4 NonTargetAcc G2s T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGTwoSTTwoGLMFiveThreeFlashNonTargetAccLo` | n/a | P4 NonTargetAcc G2s T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveThreeFlashNonTargetAccHi` | n/a | P4 NonTargetAcc G2s T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveThreeFlashNonTargetAccCI` | n/a | P4 NonTargetAcc G2s T2 GLMFiveThreeFlash, 95% CI |
| `\PfourGTwoSTTwoGLMFiveThreeFlashNonTargetAccN` | n/a | P4 NonTargetAcc G2s T2 GLMFiveThreeFlash, n |
| `\PfourGTwoSTTwoGLMFiveThreeFlashNonTargetAccP` | n/a | P4 NonTargetAcc G2s T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGLMFiveTwoAsr` | n/a | P4 Asr G2s T2 GLMFiveTwo [n/a: no data yet] |
| `\PfourGTwoSTTwoGLMFiveTwoAsrLo` | n/a | P4 Asr G2s T2 GLMFiveTwo, lower 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveTwoAsrHi` | n/a | P4 Asr G2s T2 GLMFiveTwo, upper 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveTwoAsrCI` | n/a | P4 Asr G2s T2 GLMFiveTwo, 95% CI |
| `\PfourGTwoSTTwoGLMFiveTwoAsrN` | n/a | P4 Asr G2s T2 GLMFiveTwo, n |
| `\PfourGTwoSTTwoGLMFiveTwoAsrP` | n/a | P4 Asr G2s T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGLMFiveTwoAsrDropped` | n/a | P4 AsrDropped G2s T2 GLMFiveTwo [n/a: no data yet] |
| `\PfourGTwoSTTwoGLMFiveTwoAsrDroppedLo` | n/a | P4 AsrDropped G2s T2 GLMFiveTwo, lower 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveTwoAsrDroppedHi` | n/a | P4 AsrDropped G2s T2 GLMFiveTwo, upper 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveTwoAsrDroppedCI` | n/a | P4 AsrDropped G2s T2 GLMFiveTwo, 95% CI |
| `\PfourGTwoSTTwoGLMFiveTwoAsrDroppedN` | n/a | P4 AsrDropped G2s T2 GLMFiveTwo, n |
| `\PfourGTwoSTTwoGLMFiveTwoAsrDroppedP` | n/a | P4 AsrDropped G2s T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGLMFiveTwoAsrCleanOk` | n/a | P4 AsrCleanOk G2s T2 GLMFiveTwo [n/a: no data yet] |
| `\PfourGTwoSTTwoGLMFiveTwoAsrCleanOkLo` | n/a | P4 AsrCleanOk G2s T2 GLMFiveTwo, lower 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveTwoAsrCleanOkHi` | n/a | P4 AsrCleanOk G2s T2 GLMFiveTwo, upper 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveTwoAsrCleanOkCI` | n/a | P4 AsrCleanOk G2s T2 GLMFiveTwo, 95% CI |
| `\PfourGTwoSTTwoGLMFiveTwoAsrCleanOkN` | n/a | P4 AsrCleanOk G2s T2 GLMFiveTwo, n |
| `\PfourGTwoSTTwoGLMFiveTwoAsrCleanOkP` | n/a | P4 AsrCleanOk G2s T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGLMFiveTwoNonTargetAcc` | n/a | P4 NonTargetAcc G2s T2 GLMFiveTwo [n/a: no data yet] |
| `\PfourGTwoSTTwoGLMFiveTwoNonTargetAccLo` | n/a | P4 NonTargetAcc G2s T2 GLMFiveTwo, lower 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveTwoNonTargetAccHi` | n/a | P4 NonTargetAcc G2s T2 GLMFiveTwo, upper 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveTwoNonTargetAccCI` | n/a | P4 NonTargetAcc G2s T2 GLMFiveTwo, 95% CI |
| `\PfourGTwoSTTwoGLMFiveTwoNonTargetAccN` | n/a | P4 NonTargetAcc G2s T2 GLMFiveTwo, n |
| `\PfourGTwoSTTwoGLMFiveTwoNonTargetAccP` | n/a | P4 NonTargetAcc G2s T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsr` | n/a | P4 Asr G2s_insider T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrLo` | n/a | P4 Asr G2s_insider T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrHi` | n/a | P4 Asr G2s_insider T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrCI` | n/a | P4 Asr G2s_insider T2 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrN` | n/a | P4 Asr G2s_insider T2 QwenThreeEightTwoSevenB, n |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrP` | n/a | P4 Asr G2s_insider T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrDropped` | n/a | P4 AsrDropped G2s_insider T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrDroppedLo` | n/a | P4 AsrDropped G2s_insider T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrDroppedHi` | n/a | P4 AsrDropped G2s_insider T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrDroppedCI` | n/a | P4 AsrDropped G2s_insider T2 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrDroppedN` | n/a | P4 AsrDropped G2s_insider T2 QwenThreeEightTwoSevenB, n |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrDroppedP` | n/a | P4 AsrDropped G2s_insider T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrCleanOk` | n/a | P4 AsrCleanOk G2s_insider T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrCleanOkLo` | n/a | P4 AsrCleanOk G2s_insider T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrCleanOkHi` | n/a | P4 AsrCleanOk G2s_insider T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrCleanOkCI` | n/a | P4 AsrCleanOk G2s_insider T2 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrCleanOkN` | n/a | P4 AsrCleanOk G2s_insider T2 QwenThreeEightTwoSevenB, n |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrCleanOkP` | n/a | P4 AsrCleanOk G2s_insider T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBNonTargetAcc` | n/a | P4 NonTargetAcc G2s_insider T2 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBNonTargetAccLo` | n/a | P4 NonTargetAcc G2s_insider T2 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBNonTargetAccHi` | n/a | P4 NonTargetAcc G2s_insider T2 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBNonTargetAccCI` | n/a | P4 NonTargetAcc G2s_insider T2 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBNonTargetAccN` | n/a | P4 NonTargetAcc G2s_insider T2 QwenThreeEightTwoSevenB, n |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBNonTargetAccP` | n/a | P4 NonTargetAcc G2s_insider T2 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsr` | n/a | P4 Asr G2s_insider T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrLo` | n/a | P4 Asr G2s_insider T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrHi` | n/a | P4 Asr G2s_insider T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrCI` | n/a | P4 Asr G2s_insider T2 GLMFiveThreeFlash, 95% CI |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrN` | n/a | P4 Asr G2s_insider T2 GLMFiveThreeFlash, n |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrP` | n/a | P4 Asr G2s_insider T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrDropped` | n/a | P4 AsrDropped G2s_insider T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrDroppedLo` | n/a | P4 AsrDropped G2s_insider T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrDroppedHi` | n/a | P4 AsrDropped G2s_insider T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrDroppedCI` | n/a | P4 AsrDropped G2s_insider T2 GLMFiveThreeFlash, 95% CI |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrDroppedN` | n/a | P4 AsrDropped G2s_insider T2 GLMFiveThreeFlash, n |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrDroppedP` | n/a | P4 AsrDropped G2s_insider T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrCleanOk` | n/a | P4 AsrCleanOk G2s_insider T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrCleanOkLo` | n/a | P4 AsrCleanOk G2s_insider T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrCleanOkHi` | n/a | P4 AsrCleanOk G2s_insider T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrCleanOkCI` | n/a | P4 AsrCleanOk G2s_insider T2 GLMFiveThreeFlash, 95% CI |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrCleanOkN` | n/a | P4 AsrCleanOk G2s_insider T2 GLMFiveThreeFlash, n |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrCleanOkP` | n/a | P4 AsrCleanOk G2s_insider T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashNonTargetAcc` | n/a | P4 NonTargetAcc G2s_insider T2 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashNonTargetAccLo` | n/a | P4 NonTargetAcc G2s_insider T2 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashNonTargetAccHi` | n/a | P4 NonTargetAcc G2s_insider T2 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashNonTargetAccCI` | n/a | P4 NonTargetAcc G2s_insider T2 GLMFiveThreeFlash, 95% CI |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashNonTargetAccN` | n/a | P4 NonTargetAcc G2s_insider T2 GLMFiveThreeFlash, n |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashNonTargetAccP` | n/a | P4 NonTargetAcc G2s_insider T2 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsr` | n/a | P4 Asr G2s_insider T2 GLMFiveTwo [n/a: no data yet] |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrLo` | n/a | P4 Asr G2s_insider T2 GLMFiveTwo, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrHi` | n/a | P4 Asr G2s_insider T2 GLMFiveTwo, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrCI` | n/a | P4 Asr G2s_insider T2 GLMFiveTwo, 95% CI |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrN` | n/a | P4 Asr G2s_insider T2 GLMFiveTwo, n |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrP` | n/a | P4 Asr G2s_insider T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrDropped` | n/a | P4 AsrDropped G2s_insider T2 GLMFiveTwo [n/a: no data yet] |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrDroppedLo` | n/a | P4 AsrDropped G2s_insider T2 GLMFiveTwo, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrDroppedHi` | n/a | P4 AsrDropped G2s_insider T2 GLMFiveTwo, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrDroppedCI` | n/a | P4 AsrDropped G2s_insider T2 GLMFiveTwo, 95% CI |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrDroppedN` | n/a | P4 AsrDropped G2s_insider T2 GLMFiveTwo, n |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrDroppedP` | n/a | P4 AsrDropped G2s_insider T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrCleanOk` | n/a | P4 AsrCleanOk G2s_insider T2 GLMFiveTwo [n/a: no data yet] |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrCleanOkLo` | n/a | P4 AsrCleanOk G2s_insider T2 GLMFiveTwo, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrCleanOkHi` | n/a | P4 AsrCleanOk G2s_insider T2 GLMFiveTwo, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrCleanOkCI` | n/a | P4 AsrCleanOk G2s_insider T2 GLMFiveTwo, 95% CI |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrCleanOkN` | n/a | P4 AsrCleanOk G2s_insider T2 GLMFiveTwo, n |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrCleanOkP` | n/a | P4 AsrCleanOk G2s_insider T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoNonTargetAcc` | n/a | P4 NonTargetAcc G2s_insider T2 GLMFiveTwo [n/a: no data yet] |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoNonTargetAccLo` | n/a | P4 NonTargetAcc G2s_insider T2 GLMFiveTwo, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoNonTargetAccHi` | n/a | P4 NonTargetAcc G2s_insider T2 GLMFiveTwo, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoNonTargetAccCI` | n/a | P4 NonTargetAcc G2s_insider T2 GLMFiveTwo, 95% CI |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoNonTargetAccN` | n/a | P4 NonTargetAcc G2s_insider T2 GLMFiveTwo, n |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoNonTargetAccP` | n/a | P4 NonTargetAcc G2s_insider T2 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsr` | n/a | P4 Asr G1+G2s - QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrLo` | n/a | P4 Asr G1+G2s - QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrHi` | n/a | P4 Asr G1+G2s - QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrCI` | n/a | P4 Asr G1+G2s - QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrN` | n/a | P4 Asr G1+G2s - QwenThreeEightTwoSevenB, n |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrP` | n/a | P4 Asr G1+G2s - QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrDropped` | n/a | P4 AsrDropped G1+G2s - QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrDroppedLo` | n/a | P4 AsrDropped G1+G2s - QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrDroppedHi` | n/a | P4 AsrDropped G1+G2s - QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrDroppedCI` | n/a | P4 AsrDropped G1+G2s - QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrDroppedN` | n/a | P4 AsrDropped G1+G2s - QwenThreeEightTwoSevenB, n |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrDroppedP` | n/a | P4 AsrDropped G1+G2s - QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrCleanOk` | n/a | P4 AsrCleanOk G1+G2s - QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrCleanOkLo` | n/a | P4 AsrCleanOk G1+G2s - QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrCleanOkHi` | n/a | P4 AsrCleanOk G1+G2s - QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrCleanOkCI` | n/a | P4 AsrCleanOk G1+G2s - QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrCleanOkN` | n/a | P4 AsrCleanOk G1+G2s - QwenThreeEightTwoSevenB, n |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrCleanOkP` | n/a | P4 AsrCleanOk G1+G2s - QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBNonTargetAcc` | n/a | P4 NonTargetAcc G1+G2s - QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBNonTargetAccLo` | n/a | P4 NonTargetAcc G1+G2s - QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBNonTargetAccHi` | n/a | P4 NonTargetAcc G1+G2s - QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBNonTargetAccCI` | n/a | P4 NonTargetAcc G1+G2s - QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBNonTargetAccN` | n/a | P4 NonTargetAcc G1+G2s - QwenThreeEightTwoSevenB, n |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBNonTargetAccP` | n/a | P4 NonTargetAcc G1+G2s - QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsr` | n/a | P4 Asr G1+G2s - GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrLo` | n/a | P4 Asr G1+G2s - GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrHi` | n/a | P4 Asr G1+G2s - GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrCI` | n/a | P4 Asr G1+G2s - GLMFiveThreeFlash, 95% CI |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrN` | n/a | P4 Asr G1+G2s - GLMFiveThreeFlash, n |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrP` | n/a | P4 Asr G1+G2s - GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrDropped` | n/a | P4 AsrDropped G1+G2s - GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrDroppedLo` | n/a | P4 AsrDropped G1+G2s - GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrDroppedHi` | n/a | P4 AsrDropped G1+G2s - GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrDroppedCI` | n/a | P4 AsrDropped G1+G2s - GLMFiveThreeFlash, 95% CI |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrDroppedN` | n/a | P4 AsrDropped G1+G2s - GLMFiveThreeFlash, n |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrDroppedP` | n/a | P4 AsrDropped G1+G2s - GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrCleanOk` | n/a | P4 AsrCleanOk G1+G2s - GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrCleanOkLo` | n/a | P4 AsrCleanOk G1+G2s - GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrCleanOkHi` | n/a | P4 AsrCleanOk G1+G2s - GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrCleanOkCI` | n/a | P4 AsrCleanOk G1+G2s - GLMFiveThreeFlash, 95% CI |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrCleanOkN` | n/a | P4 AsrCleanOk G1+G2s - GLMFiveThreeFlash, n |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrCleanOkP` | n/a | P4 AsrCleanOk G1+G2s - GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashNonTargetAcc` | n/a | P4 NonTargetAcc G1+G2s - GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashNonTargetAccLo` | n/a | P4 NonTargetAcc G1+G2s - GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashNonTargetAccHi` | n/a | P4 NonTargetAcc G1+G2s - GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashNonTargetAccCI` | n/a | P4 NonTargetAcc G1+G2s - GLMFiveThreeFlash, 95% CI |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashNonTargetAccN` | n/a | P4 NonTargetAcc G1+G2s - GLMFiveThreeFlash, n |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashNonTargetAccP` | n/a | P4 NonTargetAcc G1+G2s - GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsr` | n/a | P4 Asr G1+G2s - GLMFiveTwo [n/a: no data yet] |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrLo` | n/a | P4 Asr G1+G2s - GLMFiveTwo, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrHi` | n/a | P4 Asr G1+G2s - GLMFiveTwo, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrCI` | n/a | P4 Asr G1+G2s - GLMFiveTwo, 95% CI |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrN` | n/a | P4 Asr G1+G2s - GLMFiveTwo, n |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrP` | n/a | P4 Asr G1+G2s - GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrDropped` | n/a | P4 AsrDropped G1+G2s - GLMFiveTwo [n/a: no data yet] |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrDroppedLo` | n/a | P4 AsrDropped G1+G2s - GLMFiveTwo, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrDroppedHi` | n/a | P4 AsrDropped G1+G2s - GLMFiveTwo, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrDroppedCI` | n/a | P4 AsrDropped G1+G2s - GLMFiveTwo, 95% CI |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrDroppedN` | n/a | P4 AsrDropped G1+G2s - GLMFiveTwo, n |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrDroppedP` | n/a | P4 AsrDropped G1+G2s - GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrCleanOk` | n/a | P4 AsrCleanOk G1+G2s - GLMFiveTwo [n/a: no data yet] |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrCleanOkLo` | n/a | P4 AsrCleanOk G1+G2s - GLMFiveTwo, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrCleanOkHi` | n/a | P4 AsrCleanOk G1+G2s - GLMFiveTwo, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrCleanOkCI` | n/a | P4 AsrCleanOk G1+G2s - GLMFiveTwo, 95% CI |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrCleanOkN` | n/a | P4 AsrCleanOk G1+G2s - GLMFiveTwo, n |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrCleanOkP` | n/a | P4 AsrCleanOk G1+G2s - GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGLMFiveTwoNonTargetAcc` | n/a | P4 NonTargetAcc G1+G2s - GLMFiveTwo [n/a: no data yet] |
| `\PfourGOnePlusGTwoSGLMFiveTwoNonTargetAccLo` | n/a | P4 NonTargetAcc G1+G2s - GLMFiveTwo, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveTwoNonTargetAccHi` | n/a | P4 NonTargetAcc G1+G2s - GLMFiveTwo, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveTwoNonTargetAccCI` | n/a | P4 NonTargetAcc G1+G2s - GLMFiveTwo, 95% CI |
| `\PfourGOnePlusGTwoSGLMFiveTwoNonTargetAccN` | n/a | P4 NonTargetAcc G1+G2s - GLMFiveTwo, n |
| `\PfourGOnePlusGTwoSGLMFiveTwoNonTargetAccP` | n/a | P4 NonTargetAcc G1+G2s - GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneQwenThreeEightTwoSevenBCleanAcc` | n/a | P4 clean accuracy none QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourNoneQwenThreeEightTwoSevenBCleanAccLo` | n/a | P4 clean accuracy none QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourNoneQwenThreeEightTwoSevenBCleanAccHi` | n/a | P4 clean accuracy none QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourNoneQwenThreeEightTwoSevenBCleanAccCI` | n/a | P4 clean accuracy none QwenThreeEightTwoSevenB, 95% CI |
| `\PfourNoneQwenThreeEightTwoSevenBCleanAccN` | n/a | P4 clean accuracy none QwenThreeEightTwoSevenB, n |
| `\PfourNoneQwenThreeEightTwoSevenBCleanAccP` | n/a | P4 clean accuracy none QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneGLMFiveThreeFlashCleanAcc` | n/a | P4 clean accuracy none GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourNoneGLMFiveThreeFlashCleanAccLo` | n/a | P4 clean accuracy none GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourNoneGLMFiveThreeFlashCleanAccHi` | n/a | P4 clean accuracy none GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourNoneGLMFiveThreeFlashCleanAccCI` | n/a | P4 clean accuracy none GLMFiveThreeFlash, 95% CI |
| `\PfourNoneGLMFiveThreeFlashCleanAccN` | n/a | P4 clean accuracy none GLMFiveThreeFlash, n |
| `\PfourNoneGLMFiveThreeFlashCleanAccP` | n/a | P4 clean accuracy none GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneGLMFiveTwoCleanAcc` | n/a | P4 clean accuracy none GLMFiveTwo [n/a: no data yet] |
| `\PfourNoneGLMFiveTwoCleanAccLo` | n/a | P4 clean accuracy none GLMFiveTwo, lower 95% CI bound |
| `\PfourNoneGLMFiveTwoCleanAccHi` | n/a | P4 clean accuracy none GLMFiveTwo, upper 95% CI bound |
| `\PfourNoneGLMFiveTwoCleanAccCI` | n/a | P4 clean accuracy none GLMFiveTwo, 95% CI |
| `\PfourNoneGLMFiveTwoCleanAccN` | n/a | P4 clean accuracy none GLMFiveTwo, n |
| `\PfourNoneGLMFiveTwoCleanAccP` | n/a | P4 clean accuracy none GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePooledCleanAcc` | n/a | P4 clean accuracy G1 Pooled [n/a: no data yet] |
| `\PfourGOnePooledCleanAccLo` | n/a | P4 clean accuracy G1 Pooled, lower 95% CI bound |
| `\PfourGOnePooledCleanAccHi` | n/a | P4 clean accuracy G1 Pooled, upper 95% CI bound |
| `\PfourGOnePooledCleanAccCI` | n/a | P4 clean accuracy G1 Pooled, 95% CI |
| `\PfourGOnePooledCleanAccN` | n/a | P4 clean accuracy G1 Pooled, n |
| `\PfourGOnePooledCleanAccP` | n/a | P4 clean accuracy G1 Pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePooledFpCost` | n/a | P4 clean accuracy change vs none G1 Pooled [n/a: no data yet] |
| `\PfourGOnePooledFpCostLo` | n/a | P4 clean accuracy change vs none G1 Pooled, lower 95% CI bound |
| `\PfourGOnePooledFpCostHi` | n/a | P4 clean accuracy change vs none G1 Pooled, upper 95% CI bound |
| `\PfourGOnePooledFpCostCI` | n/a | P4 clean accuracy change vs none G1 Pooled, 95% CI |
| `\PfourGOnePooledFpCostN` | n/a | P4 clean accuracy change vs none G1 Pooled, n |
| `\PfourGOnePooledFpCostP` | n/a | P4 clean accuracy change vs none G1 Pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneDeepSeekVFourFlashCleanAcc` | n/a | P4 clean accuracy G1 DeepSeekVFourFlash [n/a: no data yet] |
| `\PfourGOneDeepSeekVFourFlashCleanAccLo` | n/a | P4 clean accuracy G1 DeepSeekVFourFlash, lower 95% CI bound |
| `\PfourGOneDeepSeekVFourFlashCleanAccHi` | n/a | P4 clean accuracy G1 DeepSeekVFourFlash, upper 95% CI bound |
| `\PfourGOneDeepSeekVFourFlashCleanAccCI` | n/a | P4 clean accuracy G1 DeepSeekVFourFlash, 95% CI |
| `\PfourGOneDeepSeekVFourFlashCleanAccN` | n/a | P4 clean accuracy G1 DeepSeekVFourFlash, n |
| `\PfourGOneDeepSeekVFourFlashCleanAccP` | n/a | P4 clean accuracy G1 DeepSeekVFourFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneDeepSeekVFourFlashFpCost` | n/a | P4 clean accuracy change vs none G1 DeepSeekVFourFlash [n/a: no data yet] |
| `\PfourGOneDeepSeekVFourFlashFpCostLo` | n/a | P4 clean accuracy change vs none G1 DeepSeekVFourFlash, lower 95% CI bound |
| `\PfourGOneDeepSeekVFourFlashFpCostHi` | n/a | P4 clean accuracy change vs none G1 DeepSeekVFourFlash, upper 95% CI bound |
| `\PfourGOneDeepSeekVFourFlashFpCostCI` | n/a | P4 clean accuracy change vs none G1 DeepSeekVFourFlash, 95% CI |
| `\PfourGOneDeepSeekVFourFlashFpCostN` | n/a | P4 clean accuracy change vs none G1 DeepSeekVFourFlash, n |
| `\PfourGOneDeepSeekVFourFlashFpCostP` | n/a | P4 clean accuracy change vs none G1 DeepSeekVFourFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneQwenThreeEightTwoSevenBCleanAcc` | n/a | P4 clean accuracy G1 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGOneQwenThreeEightTwoSevenBCleanAccLo` | n/a | P4 clean accuracy G1 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGOneQwenThreeEightTwoSevenBCleanAccHi` | n/a | P4 clean accuracy G1 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGOneQwenThreeEightTwoSevenBCleanAccCI` | n/a | P4 clean accuracy G1 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGOneQwenThreeEightTwoSevenBCleanAccN` | n/a | P4 clean accuracy G1 QwenThreeEightTwoSevenB, n |
| `\PfourGOneQwenThreeEightTwoSevenBCleanAccP` | n/a | P4 clean accuracy G1 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneQwenThreeEightTwoSevenBFpCost` | n/a | P4 clean accuracy change vs none G1 QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGOneQwenThreeEightTwoSevenBFpCostLo` | n/a | P4 clean accuracy change vs none G1 QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGOneQwenThreeEightTwoSevenBFpCostHi` | n/a | P4 clean accuracy change vs none G1 QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGOneQwenThreeEightTwoSevenBFpCostCI` | n/a | P4 clean accuracy change vs none G1 QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGOneQwenThreeEightTwoSevenBFpCostN` | n/a | P4 clean accuracy change vs none G1 QwenThreeEightTwoSevenB, n |
| `\PfourGOneQwenThreeEightTwoSevenBFpCostP` | n/a | P4 clean accuracy change vs none G1 QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneGemmaFourThreeOneBCleanAcc` | n/a | P4 clean accuracy G1 GemmaFourThreeOneB [n/a: no data yet] |
| `\PfourGOneGemmaFourThreeOneBCleanAccLo` | n/a | P4 clean accuracy G1 GemmaFourThreeOneB, lower 95% CI bound |
| `\PfourGOneGemmaFourThreeOneBCleanAccHi` | n/a | P4 clean accuracy G1 GemmaFourThreeOneB, upper 95% CI bound |
| `\PfourGOneGemmaFourThreeOneBCleanAccCI` | n/a | P4 clean accuracy G1 GemmaFourThreeOneB, 95% CI |
| `\PfourGOneGemmaFourThreeOneBCleanAccN` | n/a | P4 clean accuracy G1 GemmaFourThreeOneB, n |
| `\PfourGOneGemmaFourThreeOneBCleanAccP` | n/a | P4 clean accuracy G1 GemmaFourThreeOneB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneGemmaFourThreeOneBFpCost` | n/a | P4 clean accuracy change vs none G1 GemmaFourThreeOneB [n/a: no data yet] |
| `\PfourGOneGemmaFourThreeOneBFpCostLo` | n/a | P4 clean accuracy change vs none G1 GemmaFourThreeOneB, lower 95% CI bound |
| `\PfourGOneGemmaFourThreeOneBFpCostHi` | n/a | P4 clean accuracy change vs none G1 GemmaFourThreeOneB, upper 95% CI bound |
| `\PfourGOneGemmaFourThreeOneBFpCostCI` | n/a | P4 clean accuracy change vs none G1 GemmaFourThreeOneB, 95% CI |
| `\PfourGOneGemmaFourThreeOneBFpCostN` | n/a | P4 clean accuracy change vs none G1 GemmaFourThreeOneB, n |
| `\PfourGOneGemmaFourThreeOneBFpCostP` | n/a | P4 clean accuracy change vs none G1 GemmaFourThreeOneB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneGLMFiveThreeFlashCleanAcc` | n/a | P4 clean accuracy G1 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGOneGLMFiveThreeFlashCleanAccLo` | n/a | P4 clean accuracy G1 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGOneGLMFiveThreeFlashCleanAccHi` | n/a | P4 clean accuracy G1 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGOneGLMFiveThreeFlashCleanAccCI` | n/a | P4 clean accuracy G1 GLMFiveThreeFlash, 95% CI |
| `\PfourGOneGLMFiveThreeFlashCleanAccN` | n/a | P4 clean accuracy G1 GLMFiveThreeFlash, n |
| `\PfourGOneGLMFiveThreeFlashCleanAccP` | n/a | P4 clean accuracy G1 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneGLMFiveThreeFlashFpCost` | n/a | P4 clean accuracy change vs none G1 GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGOneGLMFiveThreeFlashFpCostLo` | n/a | P4 clean accuracy change vs none G1 GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGOneGLMFiveThreeFlashFpCostHi` | n/a | P4 clean accuracy change vs none G1 GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGOneGLMFiveThreeFlashFpCostCI` | n/a | P4 clean accuracy change vs none G1 GLMFiveThreeFlash, 95% CI |
| `\PfourGOneGLMFiveThreeFlashFpCostN` | n/a | P4 clean accuracy change vs none G1 GLMFiveThreeFlash, n |
| `\PfourGOneGLMFiveThreeFlashFpCostP` | n/a | P4 clean accuracy change vs none G1 GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneGLMFiveTwoCleanAcc` | n/a | P4 clean accuracy G1 GLMFiveTwo [n/a: no data yet] |
| `\PfourGOneGLMFiveTwoCleanAccLo` | n/a | P4 clean accuracy G1 GLMFiveTwo, lower 95% CI bound |
| `\PfourGOneGLMFiveTwoCleanAccHi` | n/a | P4 clean accuracy G1 GLMFiveTwo, upper 95% CI bound |
| `\PfourGOneGLMFiveTwoCleanAccCI` | n/a | P4 clean accuracy G1 GLMFiveTwo, 95% CI |
| `\PfourGOneGLMFiveTwoCleanAccN` | n/a | P4 clean accuracy G1 GLMFiveTwo, n |
| `\PfourGOneGLMFiveTwoCleanAccP` | n/a | P4 clean accuracy G1 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneGLMFiveTwoFpCost` | n/a | P4 clean accuracy change vs none G1 GLMFiveTwo [n/a: no data yet] |
| `\PfourGOneGLMFiveTwoFpCostLo` | n/a | P4 clean accuracy change vs none G1 GLMFiveTwo, lower 95% CI bound |
| `\PfourGOneGLMFiveTwoFpCostHi` | n/a | P4 clean accuracy change vs none G1 GLMFiveTwo, upper 95% CI bound |
| `\PfourGOneGLMFiveTwoFpCostCI` | n/a | P4 clean accuracy change vs none G1 GLMFiveTwo, 95% CI |
| `\PfourGOneGLMFiveTwoFpCostN` | n/a | P4 clean accuracy change vs none G1 GLMFiveTwo, n |
| `\PfourGOneGLMFiveTwoFpCostP` | n/a | P4 clean accuracy change vs none G1 GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUQwenThreeEightTwoSevenBCleanAcc` | n/a | P4 clean accuracy G2u QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGTwoUQwenThreeEightTwoSevenBCleanAccLo` | n/a | P4 clean accuracy G2u QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGTwoUQwenThreeEightTwoSevenBCleanAccHi` | n/a | P4 clean accuracy G2u QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGTwoUQwenThreeEightTwoSevenBCleanAccCI` | n/a | P4 clean accuracy G2u QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGTwoUQwenThreeEightTwoSevenBCleanAccN` | n/a | P4 clean accuracy G2u QwenThreeEightTwoSevenB, n |
| `\PfourGTwoUQwenThreeEightTwoSevenBCleanAccP` | n/a | P4 clean accuracy G2u QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUQwenThreeEightTwoSevenBFpCost` | n/a | P4 clean accuracy change vs none G2u QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGTwoUQwenThreeEightTwoSevenBFpCostLo` | n/a | P4 clean accuracy change vs none G2u QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGTwoUQwenThreeEightTwoSevenBFpCostHi` | n/a | P4 clean accuracy change vs none G2u QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGTwoUQwenThreeEightTwoSevenBFpCostCI` | n/a | P4 clean accuracy change vs none G2u QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGTwoUQwenThreeEightTwoSevenBFpCostN` | n/a | P4 clean accuracy change vs none G2u QwenThreeEightTwoSevenB, n |
| `\PfourGTwoUQwenThreeEightTwoSevenBFpCostP` | n/a | P4 clean accuracy change vs none G2u QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUGLMFiveThreeFlashCleanAcc` | n/a | P4 clean accuracy G2u GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGTwoUGLMFiveThreeFlashCleanAccLo` | n/a | P4 clean accuracy G2u GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGTwoUGLMFiveThreeFlashCleanAccHi` | n/a | P4 clean accuracy G2u GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGTwoUGLMFiveThreeFlashCleanAccCI` | n/a | P4 clean accuracy G2u GLMFiveThreeFlash, 95% CI |
| `\PfourGTwoUGLMFiveThreeFlashCleanAccN` | n/a | P4 clean accuracy G2u GLMFiveThreeFlash, n |
| `\PfourGTwoUGLMFiveThreeFlashCleanAccP` | n/a | P4 clean accuracy G2u GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUGLMFiveThreeFlashFpCost` | n/a | P4 clean accuracy change vs none G2u GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGTwoUGLMFiveThreeFlashFpCostLo` | n/a | P4 clean accuracy change vs none G2u GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGTwoUGLMFiveThreeFlashFpCostHi` | n/a | P4 clean accuracy change vs none G2u GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGTwoUGLMFiveThreeFlashFpCostCI` | n/a | P4 clean accuracy change vs none G2u GLMFiveThreeFlash, 95% CI |
| `\PfourGTwoUGLMFiveThreeFlashFpCostN` | n/a | P4 clean accuracy change vs none G2u GLMFiveThreeFlash, n |
| `\PfourGTwoUGLMFiveThreeFlashFpCostP` | n/a | P4 clean accuracy change vs none G2u GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUGLMFiveTwoCleanAcc` | n/a | P4 clean accuracy G2u GLMFiveTwo [n/a: no data yet] |
| `\PfourGTwoUGLMFiveTwoCleanAccLo` | n/a | P4 clean accuracy G2u GLMFiveTwo, lower 95% CI bound |
| `\PfourGTwoUGLMFiveTwoCleanAccHi` | n/a | P4 clean accuracy G2u GLMFiveTwo, upper 95% CI bound |
| `\PfourGTwoUGLMFiveTwoCleanAccCI` | n/a | P4 clean accuracy G2u GLMFiveTwo, 95% CI |
| `\PfourGTwoUGLMFiveTwoCleanAccN` | n/a | P4 clean accuracy G2u GLMFiveTwo, n |
| `\PfourGTwoUGLMFiveTwoCleanAccP` | n/a | P4 clean accuracy G2u GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUGLMFiveTwoFpCost` | n/a | P4 clean accuracy change vs none G2u GLMFiveTwo [n/a: no data yet] |
| `\PfourGTwoUGLMFiveTwoFpCostLo` | n/a | P4 clean accuracy change vs none G2u GLMFiveTwo, lower 95% CI bound |
| `\PfourGTwoUGLMFiveTwoFpCostHi` | n/a | P4 clean accuracy change vs none G2u GLMFiveTwo, upper 95% CI bound |
| `\PfourGTwoUGLMFiveTwoFpCostCI` | n/a | P4 clean accuracy change vs none G2u GLMFiveTwo, 95% CI |
| `\PfourGTwoUGLMFiveTwoFpCostN` | n/a | P4 clean accuracy change vs none G2u GLMFiveTwo, n |
| `\PfourGTwoUGLMFiveTwoFpCostP` | n/a | P4 clean accuracy change vs none G2u GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSQwenThreeEightTwoSevenBCleanAcc` | n/a | P4 clean accuracy G2s QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGTwoSQwenThreeEightTwoSevenBCleanAccLo` | n/a | P4 clean accuracy G2s QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGTwoSQwenThreeEightTwoSevenBCleanAccHi` | n/a | P4 clean accuracy G2s QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGTwoSQwenThreeEightTwoSevenBCleanAccCI` | n/a | P4 clean accuracy G2s QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGTwoSQwenThreeEightTwoSevenBCleanAccN` | n/a | P4 clean accuracy G2s QwenThreeEightTwoSevenB, n |
| `\PfourGTwoSQwenThreeEightTwoSevenBCleanAccP` | n/a | P4 clean accuracy G2s QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSQwenThreeEightTwoSevenBFpCost` | n/a | P4 clean accuracy change vs none G2s QwenThreeEightTwoSevenB [n/a: no data yet] |
| `\PfourGTwoSQwenThreeEightTwoSevenBFpCostLo` | n/a | P4 clean accuracy change vs none G2s QwenThreeEightTwoSevenB, lower 95% CI bound |
| `\PfourGTwoSQwenThreeEightTwoSevenBFpCostHi` | n/a | P4 clean accuracy change vs none G2s QwenThreeEightTwoSevenB, upper 95% CI bound |
| `\PfourGTwoSQwenThreeEightTwoSevenBFpCostCI` | n/a | P4 clean accuracy change vs none G2s QwenThreeEightTwoSevenB, 95% CI |
| `\PfourGTwoSQwenThreeEightTwoSevenBFpCostN` | n/a | P4 clean accuracy change vs none G2s QwenThreeEightTwoSevenB, n |
| `\PfourGTwoSQwenThreeEightTwoSevenBFpCostP` | n/a | P4 clean accuracy change vs none G2s QwenThreeEightTwoSevenB, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSGLMFiveThreeFlashCleanAcc` | n/a | P4 clean accuracy G2s GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGTwoSGLMFiveThreeFlashCleanAccLo` | n/a | P4 clean accuracy G2s GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGTwoSGLMFiveThreeFlashCleanAccHi` | n/a | P4 clean accuracy G2s GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGTwoSGLMFiveThreeFlashCleanAccCI` | n/a | P4 clean accuracy G2s GLMFiveThreeFlash, 95% CI |
| `\PfourGTwoSGLMFiveThreeFlashCleanAccN` | n/a | P4 clean accuracy G2s GLMFiveThreeFlash, n |
| `\PfourGTwoSGLMFiveThreeFlashCleanAccP` | n/a | P4 clean accuracy G2s GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSGLMFiveThreeFlashFpCost` | n/a | P4 clean accuracy change vs none G2s GLMFiveThreeFlash [n/a: no data yet] |
| `\PfourGTwoSGLMFiveThreeFlashFpCostLo` | n/a | P4 clean accuracy change vs none G2s GLMFiveThreeFlash, lower 95% CI bound |
| `\PfourGTwoSGLMFiveThreeFlashFpCostHi` | n/a | P4 clean accuracy change vs none G2s GLMFiveThreeFlash, upper 95% CI bound |
| `\PfourGTwoSGLMFiveThreeFlashFpCostCI` | n/a | P4 clean accuracy change vs none G2s GLMFiveThreeFlash, 95% CI |
| `\PfourGTwoSGLMFiveThreeFlashFpCostN` | n/a | P4 clean accuracy change vs none G2s GLMFiveThreeFlash, n |
| `\PfourGTwoSGLMFiveThreeFlashFpCostP` | n/a | P4 clean accuracy change vs none G2s GLMFiveThreeFlash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSGLMFiveTwoCleanAcc` | n/a | P4 clean accuracy G2s GLMFiveTwo [n/a: no data yet] |
| `\PfourGTwoSGLMFiveTwoCleanAccLo` | n/a | P4 clean accuracy G2s GLMFiveTwo, lower 95% CI bound |
| `\PfourGTwoSGLMFiveTwoCleanAccHi` | n/a | P4 clean accuracy G2s GLMFiveTwo, upper 95% CI bound |
| `\PfourGTwoSGLMFiveTwoCleanAccCI` | n/a | P4 clean accuracy G2s GLMFiveTwo, 95% CI |
| `\PfourGTwoSGLMFiveTwoCleanAccN` | n/a | P4 clean accuracy G2s GLMFiveTwo, n |
| `\PfourGTwoSGLMFiveTwoCleanAccP` | n/a | P4 clean accuracy G2s GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSGLMFiveTwoFpCost` | n/a | P4 clean accuracy change vs none G2s GLMFiveTwo [n/a: no data yet] |
| `\PfourGTwoSGLMFiveTwoFpCostLo` | n/a | P4 clean accuracy change vs none G2s GLMFiveTwo, lower 95% CI bound |
| `\PfourGTwoSGLMFiveTwoFpCostHi` | n/a | P4 clean accuracy change vs none G2s GLMFiveTwo, upper 95% CI bound |
| `\PfourGTwoSGLMFiveTwoFpCostCI` | n/a | P4 clean accuracy change vs none G2s GLMFiveTwo, 95% CI |
| `\PfourGTwoSGLMFiveTwoFpCostN` | n/a | P4 clean accuracy change vs none G2s GLMFiveTwo, n |
| `\PfourGTwoSGLMFiveTwoFpCostP` | n/a | P4 clean accuracy change vs none G2s GLMFiveTwo, two-sided bootstrap p (n/a if not tested) |
