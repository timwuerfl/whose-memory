# Number macros (main)

| macro | value | meaning |
|---|---|---|
| `\PrimSelfTrust` | \ensuremath{-}37.4 | primary 1: net preference memory - tool (pp) |
| `\PrimSelfTrustLo` | \ensuremath{-}43.3 | primary 1: net preference memory - tool (pp), lower 95% CI bound |
| `\PrimSelfTrustHi` | \ensuremath{-}31.7 | primary 1: net preference memory - tool (pp), upper 95% CI bound |
| `\PrimSelfTrustCI` | [\ensuremath{-}43.3, \ensuremath{-}31.7] | primary 1: net preference memory - tool (pp), 95% CI |
| `\PrimSelfTrustN` | 720 | primary 1: net preference memory - tool (pp), n |
| `\PrimSelfTrustP` | \ensuremath{<}0.001 | primary 1: net preference memory - tool (pp), two-sided bootstrap p (n/a if not tested) |
| `\PrimSelfTrustPHolm` | 0.004 | primary 1: net preference memory - tool (pp), Holm-adjusted p |
| `\PrimSelfTrustSupported` | no | primary 1: net preference memory - tool (pp), registered criterion met |
| `\PrimVerbalTTwo` | 0.62 | primary 2: mean AUROC of V at T2 |
| `\PrimVerbalTTwoLo` | 0.61 | primary 2: mean AUROC of V at T2, lower 95% CI bound |
| `\PrimVerbalTTwoHi` | 0.64 | primary 2: mean AUROC of V at T2, upper 95% CI bound |
| `\PrimVerbalTTwoCI` | [0.61, 0.64] | primary 2: mean AUROC of V at T2, 95% CI |
| `\PrimVerbalTTwoN` | 2{,}911 | primary 2: mean AUROC of V at T2, n |
| `\PrimVerbalTTwoP` | 0.002 | primary 2: mean AUROC of V at T2, two-sided bootstrap p (n/a if not tested) |
| `\PrimVerbalTTwoPHolm` | 0.004 | primary 2: mean AUROC of V at T2, Holm-adjusted p |
| `\PrimVerbalTTwoSupported` | yes | primary 2: mean AUROC of V at T2, registered criterion met |
| `\PrimGapTThree` | 0.39 | primary 3: AUROC(best trace detector) - AUROC(V) at T3 |
| `\PrimGapTThreeLo` | 0.37 | primary 3: AUROC(best trace detector) - AUROC(V) at T3, lower 95% CI bound |
| `\PrimGapTThreeHi` | 0.41 | primary 3: AUROC(best trace detector) - AUROC(V) at T3, upper 95% CI bound |
| `\PrimGapTThreeCI` | [0.37, 0.41] | primary 3: AUROC(best trace detector) - AUROC(V) at T3, 95% CI |
| `\PrimGapTThreeN` | 4{,}585 | primary 3: AUROC(best trace detector) - AUROC(V) at T3, n |
| `\PrimGapTThreeP` | \ensuremath{<}0.001 | primary 3: AUROC(best trace detector) - AUROC(V) at T3, two-sided bootstrap p (n/a if not tested) |
| `\PrimGapTThreePHolm` | 0.004 | primary 3: AUROC(best trace detector) - AUROC(V) at T3, Holm-adjusted p |
| `\PrimGapTThreeSupported` | yes | primary 3: AUROC(best trace detector) - AUROC(V) at T3, registered criterion met |
| `\PrimGate` | 97.6 | primary 4: relative ASR reduction G1 vs none (%) |
| `\PrimGateLo` | 96.3 | primary 4: relative ASR reduction G1 vs none (%), lower 95% CI bound |
| `\PrimGateHi` | 98.7 | primary 4: relative ASR reduction G1 vs none (%), upper 95% CI bound |
| `\PrimGateCI` | [96.3, 98.7] | primary 4: relative ASR reduction G1 vs none (%), 95% CI |
| `\PrimGateN` | 4{,}582 | primary 4: relative ASR reduction G1 vs none (%), n |
| `\PrimGateP` | \ensuremath{<}0.001 | primary 4: relative ASR reduction G1 vs none (%), two-sided bootstrap p (n/a if not tested) |
| `\PrimGatePHolm` | 0.004 | primary 4: relative ASR reduction G1 vs none (%), Holm-adjusted p |
| `\PrimGateSupported` | yes | primary 4: relative ASR reduction G1 vs none (%), registered criterion met |
| `\PrimGapDetector` | C | primary 3: trace detector selected on calibration episodes |
| `\PoneNetMemToolPooled` | \ensuremath{-}37.4 | P1 net memory - tool (pp), pooled |
| `\PoneNetMemToolPooledLo` | \ensuremath{-}43.3 | P1 net memory - tool (pp), pooled, lower 95% CI bound |
| `\PoneNetMemToolPooledHi` | \ensuremath{-}31.7 | P1 net memory - tool (pp), pooled, upper 95% CI bound |
| `\PoneNetMemToolPooledCI` | [\ensuremath{-}43.3, \ensuremath{-}31.7] | P1 net memory - tool (pp), pooled, 95% CI |
| `\PoneNetMemToolPooledN` | 720 | P1 net memory - tool (pp), pooled, n |
| `\PoneNetMemToolPooledP` | \ensuremath{<}0.001 | P1 net memory - tool (pp), pooled, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolDroppedPooled` | \ensuremath{-}37.5 | P1 net memory - tool (pp), unparsed dropped, pooled |
| `\PoneNetMemToolDroppedPooledLo` | \ensuremath{-}43.7 | P1 net memory - tool (pp), unparsed dropped, pooled, lower 95% CI bound |
| `\PoneNetMemToolDroppedPooledHi` | \ensuremath{-}31.4 | P1 net memory - tool (pp), unparsed dropped, pooled, upper 95% CI bound |
| `\PoneNetMemToolDroppedPooledCI` | [\ensuremath{-}43.7, \ensuremath{-}31.4] | P1 net memory - tool (pp), unparsed dropped, pooled, 95% CI |
| `\PoneNetMemToolDroppedPooledN` | 718 | P1 net memory - tool (pp), unparsed dropped, pooled, n |
| `\PoneNetMemToolDroppedPooledP` | \ensuremath{<}0.001 | P1 net memory - tool (pp), unparsed dropped, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareMemVsToolPooled` | 0.6 | P1 % follows memory vs tool, pooled |
| `\PoneShareMemVsToolPooledLo` | 0.1 | P1 % follows memory vs tool, pooled, lower 95% CI bound |
| `\PoneShareMemVsToolPooledHi` | 1.1 | P1 % follows memory vs tool, pooled, upper 95% CI bound |
| `\PoneShareMemVsToolPooledCI` | [0.1, 1.1] | P1 % follows memory vs tool, pooled, 95% CI |
| `\PoneShareMemVsToolPooledN` | 720 | P1 % follows memory vs tool, pooled, n |
| `\PoneShareMemVsToolPooledP` | n/a | P1 % follows memory vs tool, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareToolVsMemPooled` | 37.9 | P1 % follows tool vs memory, pooled |
| `\PoneShareToolVsMemPooledLo` | 32.2 | P1 % follows tool vs memory, pooled, lower 95% CI bound |
| `\PoneShareToolVsMemPooledHi` | 43.8 | P1 % follows tool vs memory, pooled, upper 95% CI bound |
| `\PoneShareToolVsMemPooledCI` | [32.2, 43.8] | P1 % follows tool vs memory, pooled, 95% CI |
| `\PoneShareToolVsMemPooledN` | 720 | P1 % follows tool vs memory, pooled, n |
| `\PoneShareToolVsMemPooledP` | n/a | P1 % follows tool vs memory, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolDeepSeekVFourFlash` | \ensuremath{-}15.8 | P1 net memory - tool (pp), deepseek-v4-flash |
| `\PoneNetMemToolDeepSeekVFourFlashLo` | \ensuremath{-}23.3 | P1 net memory - tool (pp), deepseek-v4-flash, lower 95% CI bound |
| `\PoneNetMemToolDeepSeekVFourFlashHi` | \ensuremath{-}9.2 | P1 net memory - tool (pp), deepseek-v4-flash, upper 95% CI bound |
| `\PoneNetMemToolDeepSeekVFourFlashCI` | [\ensuremath{-}23.3, \ensuremath{-}9.2] | P1 net memory - tool (pp), deepseek-v4-flash, 95% CI |
| `\PoneNetMemToolDeepSeekVFourFlashN` | 120 | P1 net memory - tool (pp), deepseek-v4-flash, n |
| `\PoneNetMemToolDeepSeekVFourFlashP` | \ensuremath{<}0.001 | P1 net memory - tool (pp), deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolDroppedDeepSeekVFourFlash` | \ensuremath{-}15.8 | P1 net memory - tool (pp), unparsed dropped, deepseek-v4-flash |
| `\PoneNetMemToolDroppedDeepSeekVFourFlashLo` | \ensuremath{-}23.3 | P1 net memory - tool (pp), unparsed dropped, deepseek-v4-flash, lower 95% CI bound |
| `\PoneNetMemToolDroppedDeepSeekVFourFlashHi` | \ensuremath{-}9.2 | P1 net memory - tool (pp), unparsed dropped, deepseek-v4-flash, upper 95% CI bound |
| `\PoneNetMemToolDroppedDeepSeekVFourFlashCI` | [\ensuremath{-}23.3, \ensuremath{-}9.2] | P1 net memory - tool (pp), unparsed dropped, deepseek-v4-flash, 95% CI |
| `\PoneNetMemToolDroppedDeepSeekVFourFlashN` | 120 | P1 net memory - tool (pp), unparsed dropped, deepseek-v4-flash, n |
| `\PoneNetMemToolDroppedDeepSeekVFourFlashP` | \ensuremath{<}0.001 | P1 net memory - tool (pp), unparsed dropped, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareMemVsToolDeepSeekVFourFlash` | 1.7 | P1 % follows memory vs tool, deepseek-v4-flash |
| `\PoneShareMemVsToolDeepSeekVFourFlashLo` | 0.0 | P1 % follows memory vs tool, deepseek-v4-flash, lower 95% CI bound |
| `\PoneShareMemVsToolDeepSeekVFourFlashHi` | 4.2 | P1 % follows memory vs tool, deepseek-v4-flash, upper 95% CI bound |
| `\PoneShareMemVsToolDeepSeekVFourFlashCI` | [0.0, 4.2] | P1 % follows memory vs tool, deepseek-v4-flash, 95% CI |
| `\PoneShareMemVsToolDeepSeekVFourFlashN` | 120 | P1 % follows memory vs tool, deepseek-v4-flash, n |
| `\PoneShareMemVsToolDeepSeekVFourFlashP` | n/a | P1 % follows memory vs tool, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareToolVsMemDeepSeekVFourFlash` | 17.5 | P1 % follows tool vs memory, deepseek-v4-flash |
| `\PoneShareToolVsMemDeepSeekVFourFlashLo` | 10.8 | P1 % follows tool vs memory, deepseek-v4-flash, lower 95% CI bound |
| `\PoneShareToolVsMemDeepSeekVFourFlashHi` | 25.0 | P1 % follows tool vs memory, deepseek-v4-flash, upper 95% CI bound |
| `\PoneShareToolVsMemDeepSeekVFourFlashCI` | [10.8, 25.0] | P1 % follows tool vs memory, deepseek-v4-flash, 95% CI |
| `\PoneShareToolVsMemDeepSeekVFourFlashN` | 120 | P1 % follows tool vs memory, deepseek-v4-flash, n |
| `\PoneShareToolVsMemDeepSeekVFourFlashP` | n/a | P1 % follows tool vs memory, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolQwenThreeEightTwoSevenB` | \ensuremath{-}35.8 | P1 net memory - tool (pp), qwen3.8-27b |
| `\PoneNetMemToolQwenThreeEightTwoSevenBLo` | \ensuremath{-}44.2 | P1 net memory - tool (pp), qwen3.8-27b, lower 95% CI bound |
| `\PoneNetMemToolQwenThreeEightTwoSevenBHi` | \ensuremath{-}27.5 | P1 net memory - tool (pp), qwen3.8-27b, upper 95% CI bound |
| `\PoneNetMemToolQwenThreeEightTwoSevenBCI` | [\ensuremath{-}44.2, \ensuremath{-}27.5] | P1 net memory - tool (pp), qwen3.8-27b, 95% CI |
| `\PoneNetMemToolQwenThreeEightTwoSevenBN` | 120 | P1 net memory - tool (pp), qwen3.8-27b, n |
| `\PoneNetMemToolQwenThreeEightTwoSevenBP` | \ensuremath{<}0.001 | P1 net memory - tool (pp), qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolDroppedQwenThreeEightTwoSevenB` | \ensuremath{-}35.8 | P1 net memory - tool (pp), unparsed dropped, qwen3.8-27b |
| `\PoneNetMemToolDroppedQwenThreeEightTwoSevenBLo` | \ensuremath{-}44.2 | P1 net memory - tool (pp), unparsed dropped, qwen3.8-27b, lower 95% CI bound |
| `\PoneNetMemToolDroppedQwenThreeEightTwoSevenBHi` | \ensuremath{-}27.5 | P1 net memory - tool (pp), unparsed dropped, qwen3.8-27b, upper 95% CI bound |
| `\PoneNetMemToolDroppedQwenThreeEightTwoSevenBCI` | [\ensuremath{-}44.2, \ensuremath{-}27.5] | P1 net memory - tool (pp), unparsed dropped, qwen3.8-27b, 95% CI |
| `\PoneNetMemToolDroppedQwenThreeEightTwoSevenBN` | 120 | P1 net memory - tool (pp), unparsed dropped, qwen3.8-27b, n |
| `\PoneNetMemToolDroppedQwenThreeEightTwoSevenBP` | \ensuremath{<}0.001 | P1 net memory - tool (pp), unparsed dropped, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareMemVsToolQwenThreeEightTwoSevenB` | 0.0 | P1 % follows memory vs tool, qwen3.8-27b |
| `\PoneShareMemVsToolQwenThreeEightTwoSevenBLo` | 0.0 | P1 % follows memory vs tool, qwen3.8-27b, lower 95% CI bound |
| `\PoneShareMemVsToolQwenThreeEightTwoSevenBHi` | 3.0 | P1 % follows memory vs tool, qwen3.8-27b, upper 95% CI bound |
| `\PoneShareMemVsToolQwenThreeEightTwoSevenBCI` | [0.0, 3.0] | P1 % follows memory vs tool, qwen3.8-27b, 95% CI |
| `\PoneShareMemVsToolQwenThreeEightTwoSevenBN` | 120 | P1 % follows memory vs tool, qwen3.8-27b, n |
| `\PoneShareMemVsToolQwenThreeEightTwoSevenBP` | n/a | P1 % follows memory vs tool, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareToolVsMemQwenThreeEightTwoSevenB` | 35.8 | P1 % follows tool vs memory, qwen3.8-27b |
| `\PoneShareToolVsMemQwenThreeEightTwoSevenBLo` | 27.5 | P1 % follows tool vs memory, qwen3.8-27b, lower 95% CI bound |
| `\PoneShareToolVsMemQwenThreeEightTwoSevenBHi` | 44.2 | P1 % follows tool vs memory, qwen3.8-27b, upper 95% CI bound |
| `\PoneShareToolVsMemQwenThreeEightTwoSevenBCI` | [27.5, 44.2] | P1 % follows tool vs memory, qwen3.8-27b, 95% CI |
| `\PoneShareToolVsMemQwenThreeEightTwoSevenBN` | 120 | P1 % follows tool vs memory, qwen3.8-27b, n |
| `\PoneShareToolVsMemQwenThreeEightTwoSevenBP` | n/a | P1 % follows tool vs memory, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolGemmaFourThreeOneB` | \ensuremath{-}65.0 | P1 net memory - tool (pp), gemma-4-31b-it |
| `\PoneNetMemToolGemmaFourThreeOneBLo` | \ensuremath{-}73.4 | P1 net memory - tool (pp), gemma-4-31b-it, lower 95% CI bound |
| `\PoneNetMemToolGemmaFourThreeOneBHi` | \ensuremath{-}55.8 | P1 net memory - tool (pp), gemma-4-31b-it, upper 95% CI bound |
| `\PoneNetMemToolGemmaFourThreeOneBCI` | [\ensuremath{-}73.4, \ensuremath{-}55.8] | P1 net memory - tool (pp), gemma-4-31b-it, 95% CI |
| `\PoneNetMemToolGemmaFourThreeOneBN` | 120 | P1 net memory - tool (pp), gemma-4-31b-it, n |
| `\PoneNetMemToolGemmaFourThreeOneBP` | \ensuremath{<}0.001 | P1 net memory - tool (pp), gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolDroppedGemmaFourThreeOneB` | \ensuremath{-}66.1 | P1 net memory - tool (pp), unparsed dropped, gemma-4-31b-it |
| `\PoneNetMemToolDroppedGemmaFourThreeOneBLo` | \ensuremath{-}74.6 | P1 net memory - tool (pp), unparsed dropped, gemma-4-31b-it, lower 95% CI bound |
| `\PoneNetMemToolDroppedGemmaFourThreeOneBHi` | \ensuremath{-}57.6 | P1 net memory - tool (pp), unparsed dropped, gemma-4-31b-it, upper 95% CI bound |
| `\PoneNetMemToolDroppedGemmaFourThreeOneBCI` | [\ensuremath{-}74.6, \ensuremath{-}57.6] | P1 net memory - tool (pp), unparsed dropped, gemma-4-31b-it, 95% CI |
| `\PoneNetMemToolDroppedGemmaFourThreeOneBN` | 118 | P1 net memory - tool (pp), unparsed dropped, gemma-4-31b-it, n |
| `\PoneNetMemToolDroppedGemmaFourThreeOneBP` | \ensuremath{<}0.001 | P1 net memory - tool (pp), unparsed dropped, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareMemVsToolGemmaFourThreeOneB` | 0.8 | P1 % follows memory vs tool, gemma-4-31b-it |
| `\PoneShareMemVsToolGemmaFourThreeOneBLo` | 0.0 | P1 % follows memory vs tool, gemma-4-31b-it, lower 95% CI bound |
| `\PoneShareMemVsToolGemmaFourThreeOneBHi` | 2.5 | P1 % follows memory vs tool, gemma-4-31b-it, upper 95% CI bound |
| `\PoneShareMemVsToolGemmaFourThreeOneBCI` | [0.0, 2.5] | P1 % follows memory vs tool, gemma-4-31b-it, 95% CI |
| `\PoneShareMemVsToolGemmaFourThreeOneBN` | 120 | P1 % follows memory vs tool, gemma-4-31b-it, n |
| `\PoneShareMemVsToolGemmaFourThreeOneBP` | n/a | P1 % follows memory vs tool, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareToolVsMemGemmaFourThreeOneB` | 65.8 | P1 % follows tool vs memory, gemma-4-31b-it |
| `\PoneShareToolVsMemGemmaFourThreeOneBLo` | 57.5 | P1 % follows tool vs memory, gemma-4-31b-it, lower 95% CI bound |
| `\PoneShareToolVsMemGemmaFourThreeOneBHi` | 74.2 | P1 % follows tool vs memory, gemma-4-31b-it, upper 95% CI bound |
| `\PoneShareToolVsMemGemmaFourThreeOneBCI` | [57.5, 74.2] | P1 % follows tool vs memory, gemma-4-31b-it, 95% CI |
| `\PoneShareToolVsMemGemmaFourThreeOneBN` | 120 | P1 % follows tool vs memory, gemma-4-31b-it, n |
| `\PoneShareToolVsMemGemmaFourThreeOneBP` | n/a | P1 % follows tool vs memory, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolGLMFiveThreeFlash` | \ensuremath{-}44.2 | P1 net memory - tool (pp), glm-5.3-flash |
| `\PoneNetMemToolGLMFiveThreeFlashLo` | \ensuremath{-}53.4 | P1 net memory - tool (pp), glm-5.3-flash, lower 95% CI bound |
| `\PoneNetMemToolGLMFiveThreeFlashHi` | \ensuremath{-}35.8 | P1 net memory - tool (pp), glm-5.3-flash, upper 95% CI bound |
| `\PoneNetMemToolGLMFiveThreeFlashCI` | [\ensuremath{-}53.4, \ensuremath{-}35.8] | P1 net memory - tool (pp), glm-5.3-flash, 95% CI |
| `\PoneNetMemToolGLMFiveThreeFlashN` | 120 | P1 net memory - tool (pp), glm-5.3-flash, n |
| `\PoneNetMemToolGLMFiveThreeFlashP` | \ensuremath{<}0.001 | P1 net memory - tool (pp), glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolDroppedGLMFiveThreeFlash` | \ensuremath{-}44.2 | P1 net memory - tool (pp), unparsed dropped, glm-5.3-flash |
| `\PoneNetMemToolDroppedGLMFiveThreeFlashLo` | \ensuremath{-}53.3 | P1 net memory - tool (pp), unparsed dropped, glm-5.3-flash, lower 95% CI bound |
| `\PoneNetMemToolDroppedGLMFiveThreeFlashHi` | \ensuremath{-}35.0 | P1 net memory - tool (pp), unparsed dropped, glm-5.3-flash, upper 95% CI bound |
| `\PoneNetMemToolDroppedGLMFiveThreeFlashCI` | [\ensuremath{-}53.3, \ensuremath{-}35.0] | P1 net memory - tool (pp), unparsed dropped, glm-5.3-flash, 95% CI |
| `\PoneNetMemToolDroppedGLMFiveThreeFlashN` | 120 | P1 net memory - tool (pp), unparsed dropped, glm-5.3-flash, n |
| `\PoneNetMemToolDroppedGLMFiveThreeFlashP` | \ensuremath{<}0.001 | P1 net memory - tool (pp), unparsed dropped, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareMemVsToolGLMFiveThreeFlash` | 0.0 | P1 % follows memory vs tool, glm-5.3-flash |
| `\PoneShareMemVsToolGLMFiveThreeFlashLo` | 0.0 | P1 % follows memory vs tool, glm-5.3-flash, lower 95% CI bound |
| `\PoneShareMemVsToolGLMFiveThreeFlashHi` | 3.0 | P1 % follows memory vs tool, glm-5.3-flash, upper 95% CI bound |
| `\PoneShareMemVsToolGLMFiveThreeFlashCI` | [0.0, 3.0] | P1 % follows memory vs tool, glm-5.3-flash, 95% CI |
| `\PoneShareMemVsToolGLMFiveThreeFlashN` | 120 | P1 % follows memory vs tool, glm-5.3-flash, n |
| `\PoneShareMemVsToolGLMFiveThreeFlashP` | n/a | P1 % follows memory vs tool, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareToolVsMemGLMFiveThreeFlash` | 44.2 | P1 % follows tool vs memory, glm-5.3-flash |
| `\PoneShareToolVsMemGLMFiveThreeFlashLo` | 35.8 | P1 % follows tool vs memory, glm-5.3-flash, lower 95% CI bound |
| `\PoneShareToolVsMemGLMFiveThreeFlashHi` | 53.3 | P1 % follows tool vs memory, glm-5.3-flash, upper 95% CI bound |
| `\PoneShareToolVsMemGLMFiveThreeFlashCI` | [35.8, 53.3] | P1 % follows tool vs memory, glm-5.3-flash, 95% CI |
| `\PoneShareToolVsMemGLMFiveThreeFlashN` | 120 | P1 % follows tool vs memory, glm-5.3-flash, n |
| `\PoneShareToolVsMemGLMFiveThreeFlashP` | n/a | P1 % follows tool vs memory, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolGLMFiveTwo` | \ensuremath{-}11.7 | P1 net memory - tool (pp), glm-5.2 |
| `\PoneNetMemToolGLMFiveTwoLo` | \ensuremath{-}17.5 | P1 net memory - tool (pp), glm-5.2, lower 95% CI bound |
| `\PoneNetMemToolGLMFiveTwoHi` | \ensuremath{-}5.8 | P1 net memory - tool (pp), glm-5.2, upper 95% CI bound |
| `\PoneNetMemToolGLMFiveTwoCI` | [\ensuremath{-}17.5, \ensuremath{-}5.8] | P1 net memory - tool (pp), glm-5.2, 95% CI |
| `\PoneNetMemToolGLMFiveTwoN` | 120 | P1 net memory - tool (pp), glm-5.2, n |
| `\PoneNetMemToolGLMFiveTwoP` | \ensuremath{<}0.001 | P1 net memory - tool (pp), glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolDroppedGLMFiveTwo` | \ensuremath{-}11.7 | P1 net memory - tool (pp), unparsed dropped, glm-5.2 |
| `\PoneNetMemToolDroppedGLMFiveTwoLo` | \ensuremath{-}17.5 | P1 net memory - tool (pp), unparsed dropped, glm-5.2, lower 95% CI bound |
| `\PoneNetMemToolDroppedGLMFiveTwoHi` | \ensuremath{-}5.8 | P1 net memory - tool (pp), unparsed dropped, glm-5.2, upper 95% CI bound |
| `\PoneNetMemToolDroppedGLMFiveTwoCI` | [\ensuremath{-}17.5, \ensuremath{-}5.8] | P1 net memory - tool (pp), unparsed dropped, glm-5.2, 95% CI |
| `\PoneNetMemToolDroppedGLMFiveTwoN` | 120 | P1 net memory - tool (pp), unparsed dropped, glm-5.2, n |
| `\PoneNetMemToolDroppedGLMFiveTwoP` | \ensuremath{<}0.001 | P1 net memory - tool (pp), unparsed dropped, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareMemVsToolGLMFiveTwo` | 0.0 | P1 % follows memory vs tool, glm-5.2 |
| `\PoneShareMemVsToolGLMFiveTwoLo` | 0.0 | P1 % follows memory vs tool, glm-5.2, lower 95% CI bound |
| `\PoneShareMemVsToolGLMFiveTwoHi` | 3.0 | P1 % follows memory vs tool, glm-5.2, upper 95% CI bound |
| `\PoneShareMemVsToolGLMFiveTwoCI` | [0.0, 3.0] | P1 % follows memory vs tool, glm-5.2, 95% CI |
| `\PoneShareMemVsToolGLMFiveTwoN` | 120 | P1 % follows memory vs tool, glm-5.2, n |
| `\PoneShareMemVsToolGLMFiveTwoP` | n/a | P1 % follows memory vs tool, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareToolVsMemGLMFiveTwo` | 11.7 | P1 % follows tool vs memory, glm-5.2 |
| `\PoneShareToolVsMemGLMFiveTwoLo` | 6.7 | P1 % follows tool vs memory, glm-5.2, lower 95% CI bound |
| `\PoneShareToolVsMemGLMFiveTwoHi` | 17.5 | P1 % follows tool vs memory, glm-5.2, upper 95% CI bound |
| `\PoneShareToolVsMemGLMFiveTwoCI` | [6.7, 17.5] | P1 % follows tool vs memory, glm-5.2, 95% CI |
| `\PoneShareToolVsMemGLMFiveTwoN` | 120 | P1 % follows tool vs memory, glm-5.2, n |
| `\PoneShareToolVsMemGLMFiveTwoP` | n/a | P1 % follows tool vs memory, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolQwenThreeFiveThreeNineSevenB` | \ensuremath{-}51.7 | P1 net memory - tool (pp), qwen3.5-397b |
| `\PoneNetMemToolQwenThreeFiveThreeNineSevenBLo` | \ensuremath{-}60.8 | P1 net memory - tool (pp), qwen3.5-397b, lower 95% CI bound |
| `\PoneNetMemToolQwenThreeFiveThreeNineSevenBHi` | \ensuremath{-}42.5 | P1 net memory - tool (pp), qwen3.5-397b, upper 95% CI bound |
| `\PoneNetMemToolQwenThreeFiveThreeNineSevenBCI` | [\ensuremath{-}60.8, \ensuremath{-}42.5] | P1 net memory - tool (pp), qwen3.5-397b, 95% CI |
| `\PoneNetMemToolQwenThreeFiveThreeNineSevenBN` | 120 | P1 net memory - tool (pp), qwen3.5-397b, n |
| `\PoneNetMemToolQwenThreeFiveThreeNineSevenBP` | \ensuremath{<}0.001 | P1 net memory - tool (pp), qwen3.5-397b, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolDroppedQwenThreeFiveThreeNineSevenB` | \ensuremath{-}51.7 | P1 net memory - tool (pp), unparsed dropped, qwen3.5-397b |
| `\PoneNetMemToolDroppedQwenThreeFiveThreeNineSevenBLo` | \ensuremath{-}60.8 | P1 net memory - tool (pp), unparsed dropped, qwen3.5-397b, lower 95% CI bound |
| `\PoneNetMemToolDroppedQwenThreeFiveThreeNineSevenBHi` | \ensuremath{-}42.5 | P1 net memory - tool (pp), unparsed dropped, qwen3.5-397b, upper 95% CI bound |
| `\PoneNetMemToolDroppedQwenThreeFiveThreeNineSevenBCI` | [\ensuremath{-}60.8, \ensuremath{-}42.5] | P1 net memory - tool (pp), unparsed dropped, qwen3.5-397b, 95% CI |
| `\PoneNetMemToolDroppedQwenThreeFiveThreeNineSevenBN` | 120 | P1 net memory - tool (pp), unparsed dropped, qwen3.5-397b, n |
| `\PoneNetMemToolDroppedQwenThreeFiveThreeNineSevenBP` | \ensuremath{<}0.001 | P1 net memory - tool (pp), unparsed dropped, qwen3.5-397b, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareMemVsToolQwenThreeFiveThreeNineSevenB` | 0.8 | P1 % follows memory vs tool, qwen3.5-397b |
| `\PoneShareMemVsToolQwenThreeFiveThreeNineSevenBLo` | 0.0 | P1 % follows memory vs tool, qwen3.5-397b, lower 95% CI bound |
| `\PoneShareMemVsToolQwenThreeFiveThreeNineSevenBHi` | 2.5 | P1 % follows memory vs tool, qwen3.5-397b, upper 95% CI bound |
| `\PoneShareMemVsToolQwenThreeFiveThreeNineSevenBCI` | [0.0, 2.5] | P1 % follows memory vs tool, qwen3.5-397b, 95% CI |
| `\PoneShareMemVsToolQwenThreeFiveThreeNineSevenBN` | 120 | P1 % follows memory vs tool, qwen3.5-397b, n |
| `\PoneShareMemVsToolQwenThreeFiveThreeNineSevenBP` | n/a | P1 % follows memory vs tool, qwen3.5-397b, two-sided bootstrap p (n/a if not tested) |
| `\PoneShareToolVsMemQwenThreeFiveThreeNineSevenB` | 52.5 | P1 % follows tool vs memory, qwen3.5-397b |
| `\PoneShareToolVsMemQwenThreeFiveThreeNineSevenBLo` | 44.2 | P1 % follows tool vs memory, qwen3.5-397b, lower 95% CI bound |
| `\PoneShareToolVsMemQwenThreeFiveThreeNineSevenBHi` | 60.8 | P1 % follows tool vs memory, qwen3.5-397b, upper 95% CI bound |
| `\PoneShareToolVsMemQwenThreeFiveThreeNineSevenBCI` | [44.2, 60.8] | P1 % follows tool vs memory, qwen3.5-397b, 95% CI |
| `\PoneShareToolVsMemQwenThreeFiveThreeNineSevenBN` | 120 | P1 % follows tool vs memory, qwen3.5-397b, n |
| `\PoneShareToolVsMemQwenThreeFiveThreeNineSevenBP` | n/a | P1 % follows tool vs memory, qwen3.5-397b, two-sided bootstrap p (n/a if not tested) |
| `\PoneMixedShare` | n/a | P1 mixed model: P(follows memory / side chosen), % [n/a: outcome (near-)degenerate: 4 of 277 trials follow memory (fewer than 5 of one outcome); mixed model not estimable, exact binomial interval and test reported instead (they ignore clustering)] |
| `\PoneMixedShareLo` | n/a | P1 mixed model: P(follows memory / side chosen), %, lower 95% CI bound |
| `\PoneMixedShareHi` | n/a | P1 mixed model: P(follows memory / side chosen), %, upper 95% CI bound |
| `\PoneMixedShareCI` | n/a | P1 mixed model: P(follows memory / side chosen), %, 95% CI |
| `\PoneMixedShareN` | 277 | P1 mixed model: P(follows memory / side chosen), %, n |
| `\PoneMixedShareP` | n/a | P1 mixed model: P(follows memory / side chosen), %, two-sided bootstrap p (n/a if not tested) |
| `\PoneMixedEstimable` | no | P1 mixed model estimable |
| `\PoneSideChosenK` | 4 | P1 memory-vs-tool trials following memory among side-chosen |
| `\PoneSideChosenN` | 277 | P1 memory-vs-tool trials with a side chosen |
| `\PoneSideChosenExactCI` | [0.4, 3.7] | P1 share following memory among side-chosen, exact Clopper-Pearson CI (%) |
| `\PoneNetMemToolFamAssistant` | \ensuremath{-}64.2 | P1 net memory - tool (pp), family assistant |
| `\PoneNetMemToolFamAssistantLo` | \ensuremath{-}73.3 | P1 net memory - tool (pp), family assistant, lower 95% CI bound |
| `\PoneNetMemToolFamAssistantHi` | \ensuremath{-}55.0 | P1 net memory - tool (pp), family assistant, upper 95% CI bound |
| `\PoneNetMemToolFamAssistantCI` | [\ensuremath{-}73.3, \ensuremath{-}55.0] | P1 net memory - tool (pp), family assistant, 95% CI |
| `\PoneNetMemToolFamAssistantN` | 240 | P1 net memory - tool (pp), family assistant, n |
| `\PoneNetMemToolFamAssistantP` | \ensuremath{<}0.001 | P1 net memory - tool (pp), family assistant, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolFamInventory` | \ensuremath{-}42.1 | P1 net memory - tool (pp), family inventory |
| `\PoneNetMemToolFamInventoryLo` | \ensuremath{-}48.3 | P1 net memory - tool (pp), family inventory, lower 95% CI bound |
| `\PoneNetMemToolFamInventoryHi` | \ensuremath{-}35.4 | P1 net memory - tool (pp), family inventory, upper 95% CI bound |
| `\PoneNetMemToolFamInventoryCI` | [\ensuremath{-}48.3, \ensuremath{-}35.4] | P1 net memory - tool (pp), family inventory, 95% CI |
| `\PoneNetMemToolFamInventoryN` | 240 | P1 net memory - tool (pp), family inventory, n |
| `\PoneNetMemToolFamInventoryP` | \ensuremath{<}0.001 | P1 net memory - tool (pp), family inventory, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolFamResearch` | \ensuremath{-}5.8 | P1 net memory - tool (pp), family research |
| `\PoneNetMemToolFamResearchLo` | \ensuremath{-}10.4 | P1 net memory - tool (pp), family research, lower 95% CI bound |
| `\PoneNetMemToolFamResearchHi` | \ensuremath{-}2.1 | P1 net memory - tool (pp), family research, upper 95% CI bound |
| `\PoneNetMemToolFamResearchCI` | [\ensuremath{-}10.4, \ensuremath{-}2.1] | P1 net memory - tool (pp), family research, 95% CI |
| `\PoneNetMemToolFamResearchN` | 240 | P1 net memory - tool (pp), family research, n |
| `\PoneNetMemToolFamResearchP` | \ensuremath{<}0.001 | P1 net memory - tool (pp), family research, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolVariantZero` | \ensuremath{-}36.5 | P1 net memory - tool (pp), phrasing 0 |
| `\PoneNetMemToolVariantZeroLo` | \ensuremath{-}47.4 | P1 net memory - tool (pp), phrasing 0, lower 95% CI bound |
| `\PoneNetMemToolVariantZeroHi` | \ensuremath{-}26.0 | P1 net memory - tool (pp), phrasing 0, upper 95% CI bound |
| `\PoneNetMemToolVariantZeroCI` | [\ensuremath{-}47.4, \ensuremath{-}26.0] | P1 net memory - tool (pp), phrasing 0, 95% CI |
| `\PoneNetMemToolVariantZeroN` | 192 | P1 net memory - tool (pp), phrasing 0, n |
| `\PoneNetMemToolVariantZeroP` | \ensuremath{<}0.001 | P1 net memory - tool (pp), phrasing 0, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolVariantOne` | \ensuremath{-}43.2 | P1 net memory - tool (pp), phrasing 1 |
| `\PoneNetMemToolVariantOneLo` | \ensuremath{-}52.3 | P1 net memory - tool (pp), phrasing 1, lower 95% CI bound |
| `\PoneNetMemToolVariantOneHi` | \ensuremath{-}34.1 | P1 net memory - tool (pp), phrasing 1, upper 95% CI bound |
| `\PoneNetMemToolVariantOneCI` | [\ensuremath{-}52.3, \ensuremath{-}34.1] | P1 net memory - tool (pp), phrasing 1, 95% CI |
| `\PoneNetMemToolVariantOneN` | 264 | P1 net memory - tool (pp), phrasing 1, n |
| `\PoneNetMemToolVariantOneP` | \ensuremath{<}0.001 | P1 net memory - tool (pp), phrasing 1, two-sided bootstrap p (n/a if not tested) |
| `\PoneNetMemToolVariantTwo` | \ensuremath{-}32.2 | P1 net memory - tool (pp), phrasing 2 |
| `\PoneNetMemToolVariantTwoLo` | \ensuremath{-}41.7 | P1 net memory - tool (pp), phrasing 2, lower 95% CI bound |
| `\PoneNetMemToolVariantTwoHi` | \ensuremath{-}22.7 | P1 net memory - tool (pp), phrasing 2, upper 95% CI bound |
| `\PoneNetMemToolVariantTwoCI` | [\ensuremath{-}41.7, \ensuremath{-}22.7] | P1 net memory - tool (pp), phrasing 2, 95% CI |
| `\PoneNetMemToolVariantTwoN` | 264 | P1 net memory - tool (pp), phrasing 2, n |
| `\PoneNetMemToolVariantTwoP` | \ensuremath{<}0.001 | P1 net memory - tool (pp), phrasing 2, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsToolFollowA` | 0.6 | P1 pair memory vs tool: % follows memory |
| `\PonePairMemoryVsToolFollowALo` | 0.1 | P1 pair memory vs tool: % follows memory, lower 95% CI bound |
| `\PonePairMemoryVsToolFollowAHi` | 1.1 | P1 pair memory vs tool: % follows memory, upper 95% CI bound |
| `\PonePairMemoryVsToolFollowACI` | [0.1, 1.1] | P1 pair memory vs tool: % follows memory, 95% CI |
| `\PonePairMemoryVsToolFollowAN` | 720 | P1 pair memory vs tool: % follows memory, n |
| `\PonePairMemoryVsToolFollowAP` | n/a | P1 pair memory vs tool: % follows memory, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsToolFollowB` | 37.9 | P1 pair memory vs tool: % follows tool |
| `\PonePairMemoryVsToolFollowBLo` | 32.1 | P1 pair memory vs tool: % follows tool, lower 95% CI bound |
| `\PonePairMemoryVsToolFollowBHi` | 43.6 | P1 pair memory vs tool: % follows tool, upper 95% CI bound |
| `\PonePairMemoryVsToolFollowBCI` | [32.1, 43.6] | P1 pair memory vs tool: % follows tool, 95% CI |
| `\PonePairMemoryVsToolFollowBN` | 720 | P1 pair memory vs tool: % follows tool, n |
| `\PonePairMemoryVsToolFollowBP` | n/a | P1 pair memory vs tool: % follows tool, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsToolEsc` | 61.3 | P1 pair memory vs tool: % flags conflict |
| `\PonePairMemoryVsToolEscLo` | 55.3 | P1 pair memory vs tool: % flags conflict, lower 95% CI bound |
| `\PonePairMemoryVsToolEscHi` | 66.8 | P1 pair memory vs tool: % flags conflict, upper 95% CI bound |
| `\PonePairMemoryVsToolEscCI` | [55.3, 66.8] | P1 pair memory vs tool: % flags conflict, 95% CI |
| `\PonePairMemoryVsToolEscN` | 720 | P1 pair memory vs tool: % flags conflict, n |
| `\PonePairMemoryVsToolEscP` | n/a | P1 pair memory vs tool: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsToolNet` | \ensuremath{-}37.4 | P1 pair memory vs tool: net A - B (pp) |
| `\PonePairMemoryVsToolNetLo` | \ensuremath{-}43.2 | P1 pair memory vs tool: net A - B (pp), lower 95% CI bound |
| `\PonePairMemoryVsToolNetHi` | \ensuremath{-}31.8 | P1 pair memory vs tool: net A - B (pp), upper 95% CI bound |
| `\PonePairMemoryVsToolNetCI` | [\ensuremath{-}43.2, \ensuremath{-}31.8] | P1 pair memory vs tool: net A - B (pp), 95% CI |
| `\PonePairMemoryVsToolNetN` | 720 | P1 pair memory vs tool: net A - B (pp), n |
| `\PonePairMemoryVsToolNetP` | \ensuremath{<}0.001 | P1 pair memory vs tool: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsWebFollowA` | 6.8 | P1 pair memory vs web: % follows memory |
| `\PonePairMemoryVsWebFollowALo` | 4.0 | P1 pair memory vs web: % follows memory, lower 95% CI bound |
| `\PonePairMemoryVsWebFollowAHi` | 10.0 | P1 pair memory vs web: % follows memory, upper 95% CI bound |
| `\PonePairMemoryVsWebFollowACI` | [4.0, 10.0] | P1 pair memory vs web: % follows memory, 95% CI |
| `\PonePairMemoryVsWebFollowAN` | 720 | P1 pair memory vs web: % follows memory, n |
| `\PonePairMemoryVsWebFollowAP` | n/a | P1 pair memory vs web: % follows memory, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsWebFollowB` | 11.1 | P1 pair memory vs web: % follows web |
| `\PonePairMemoryVsWebFollowBLo` | 7.6 | P1 pair memory vs web: % follows web, lower 95% CI bound |
| `\PonePairMemoryVsWebFollowBHi` | 15.0 | P1 pair memory vs web: % follows web, upper 95% CI bound |
| `\PonePairMemoryVsWebFollowBCI` | [7.6, 15.0] | P1 pair memory vs web: % follows web, 95% CI |
| `\PonePairMemoryVsWebFollowBN` | 720 | P1 pair memory vs web: % follows web, n |
| `\PonePairMemoryVsWebFollowBP` | n/a | P1 pair memory vs web: % follows web, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsWebEsc` | 81.5 | P1 pair memory vs web: % flags conflict |
| `\PonePairMemoryVsWebEscLo` | 76.7 | P1 pair memory vs web: % flags conflict, lower 95% CI bound |
| `\PonePairMemoryVsWebEscHi` | 86.5 | P1 pair memory vs web: % flags conflict, upper 95% CI bound |
| `\PonePairMemoryVsWebEscCI` | [76.7, 86.5] | P1 pair memory vs web: % flags conflict, 95% CI |
| `\PonePairMemoryVsWebEscN` | 720 | P1 pair memory vs web: % flags conflict, n |
| `\PonePairMemoryVsWebEscP` | n/a | P1 pair memory vs web: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsWebNet` | \ensuremath{-}4.3 | P1 pair memory vs web: net A - B (pp) |
| `\PonePairMemoryVsWebNetLo` | \ensuremath{-}8.6 | P1 pair memory vs web: net A - B (pp), lower 95% CI bound |
| `\PonePairMemoryVsWebNetHi` | 0.0 | P1 pair memory vs web: net A - B (pp), upper 95% CI bound |
| `\PonePairMemoryVsWebNetCI` | [\ensuremath{-}8.6, 0.0] | P1 pair memory vs web: net A - B (pp), 95% CI |
| `\PonePairMemoryVsWebNetN` | 720 | P1 pair memory vs web: net A - B (pp), n |
| `\PonePairMemoryVsWebNetP` | 0.052 | P1 pair memory vs web: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsUserFollowA` | 0.4 | P1 pair memory vs user: % follows memory |
| `\PonePairMemoryVsUserFollowALo` | 0.0 | P1 pair memory vs user: % follows memory, lower 95% CI bound |
| `\PonePairMemoryVsUserFollowAHi` | 1.0 | P1 pair memory vs user: % follows memory, upper 95% CI bound |
| `\PonePairMemoryVsUserFollowACI` | [0.0, 1.0] | P1 pair memory vs user: % follows memory, 95% CI |
| `\PonePairMemoryVsUserFollowAN` | 720 | P1 pair memory vs user: % follows memory, n |
| `\PonePairMemoryVsUserFollowAP` | n/a | P1 pair memory vs user: % follows memory, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsUserFollowB` | 42.4 | P1 pair memory vs user: % follows user |
| `\PonePairMemoryVsUserFollowBLo` | 36.4 | P1 pair memory vs user: % follows user, lower 95% CI bound |
| `\PonePairMemoryVsUserFollowBHi` | 47.9 | P1 pair memory vs user: % follows user, upper 95% CI bound |
| `\PonePairMemoryVsUserFollowBCI` | [36.4, 47.9] | P1 pair memory vs user: % follows user, 95% CI |
| `\PonePairMemoryVsUserFollowBN` | 720 | P1 pair memory vs user: % follows user, n |
| `\PonePairMemoryVsUserFollowBP` | n/a | P1 pair memory vs user: % follows user, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsUserEsc` | 56.5 | P1 pair memory vs user: % flags conflict |
| `\PonePairMemoryVsUserEscLo` | 50.7 | P1 pair memory vs user: % flags conflict, lower 95% CI bound |
| `\PonePairMemoryVsUserEscHi` | 62.4 | P1 pair memory vs user: % flags conflict, upper 95% CI bound |
| `\PonePairMemoryVsUserEscCI` | [50.7, 62.4] | P1 pair memory vs user: % flags conflict, 95% CI |
| `\PonePairMemoryVsUserEscN` | 720 | P1 pair memory vs user: % flags conflict, n |
| `\PonePairMemoryVsUserEscP` | n/a | P1 pair memory vs user: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsUserNet` | \ensuremath{-}41.9 | P1 pair memory vs user: net A - B (pp) |
| `\PonePairMemoryVsUserNetLo` | \ensuremath{-}47.9 | P1 pair memory vs user: net A - B (pp), lower 95% CI bound |
| `\PonePairMemoryVsUserNetHi` | \ensuremath{-}36.1 | P1 pair memory vs user: net A - B (pp), upper 95% CI bound |
| `\PonePairMemoryVsUserNetCI` | [\ensuremath{-}47.9, \ensuremath{-}36.1] | P1 pair memory vs user: net A - B (pp), 95% CI |
| `\PonePairMemoryVsUserNetN` | 720 | P1 pair memory vs user: net A - B (pp), n |
| `\PonePairMemoryVsUserNetP` | \ensuremath{<}0.001 | P1 pair memory vs user: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsAgentFollowA` | 2.8 | P1 pair memory vs agent: % follows memory |
| `\PonePairMemoryVsAgentFollowALo` | 1.1 | P1 pair memory vs agent: % follows memory, lower 95% CI bound |
| `\PonePairMemoryVsAgentFollowAHi` | 4.7 | P1 pair memory vs agent: % follows memory, upper 95% CI bound |
| `\PonePairMemoryVsAgentFollowACI` | [1.1, 4.7] | P1 pair memory vs agent: % follows memory, 95% CI |
| `\PonePairMemoryVsAgentFollowAN` | 720 | P1 pair memory vs agent: % follows memory, n |
| `\PonePairMemoryVsAgentFollowAP` | n/a | P1 pair memory vs agent: % follows memory, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsAgentFollowB` | 22.1 | P1 pair memory vs agent: % follows agent |
| `\PonePairMemoryVsAgentFollowBLo` | 17.1 | P1 pair memory vs agent: % follows agent, lower 95% CI bound |
| `\PonePairMemoryVsAgentFollowBHi` | 26.9 | P1 pair memory vs agent: % follows agent, upper 95% CI bound |
| `\PonePairMemoryVsAgentFollowBCI` | [17.1, 26.9] | P1 pair memory vs agent: % follows agent, 95% CI |
| `\PonePairMemoryVsAgentFollowBN` | 720 | P1 pair memory vs agent: % follows agent, n |
| `\PonePairMemoryVsAgentFollowBP` | n/a | P1 pair memory vs agent: % follows agent, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsAgentEsc` | 75.1 | P1 pair memory vs agent: % flags conflict |
| `\PonePairMemoryVsAgentEscLo` | 69.4 | P1 pair memory vs agent: % flags conflict, lower 95% CI bound |
| `\PonePairMemoryVsAgentEscHi` | 80.6 | P1 pair memory vs agent: % flags conflict, upper 95% CI bound |
| `\PonePairMemoryVsAgentEscCI` | [69.4, 80.6] | P1 pair memory vs agent: % flags conflict, 95% CI |
| `\PonePairMemoryVsAgentEscN` | 720 | P1 pair memory vs agent: % flags conflict, n |
| `\PonePairMemoryVsAgentEscP` | n/a | P1 pair memory vs agent: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsAgentNet` | \ensuremath{-}19.3 | P1 pair memory vs agent: net A - B (pp) |
| `\PonePairMemoryVsAgentNetLo` | \ensuremath{-}24.4 | P1 pair memory vs agent: net A - B (pp), lower 95% CI bound |
| `\PonePairMemoryVsAgentNetHi` | \ensuremath{-}14.0 | P1 pair memory vs agent: net A - B (pp), upper 95% CI bound |
| `\PonePairMemoryVsAgentNetCI` | [\ensuremath{-}24.4, \ensuremath{-}14.0] | P1 pair memory vs agent: net A - B (pp), 95% CI |
| `\PonePairMemoryVsAgentNetN` | 720 | P1 pair memory vs agent: net A - B (pp), n |
| `\PonePairMemoryVsAgentNetP` | \ensuremath{<}0.001 | P1 pair memory vs agent: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsUnattributedFollowA` | 1.2 | P1 pair memory vs unattributed: % follows memory |
| `\PonePairMemoryVsUnattributedFollowALo` | 0.6 | P1 pair memory vs unattributed: % follows memory, lower 95% CI bound |
| `\PonePairMemoryVsUnattributedFollowAHi` | 2.1 | P1 pair memory vs unattributed: % follows memory, upper 95% CI bound |
| `\PonePairMemoryVsUnattributedFollowACI` | [0.6, 2.1] | P1 pair memory vs unattributed: % follows memory, 95% CI |
| `\PonePairMemoryVsUnattributedFollowAN` | 720 | P1 pair memory vs unattributed: % follows memory, n |
| `\PonePairMemoryVsUnattributedFollowAP` | n/a | P1 pair memory vs unattributed: % follows memory, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsUnattributedFollowB` | 32.4 | P1 pair memory vs unattributed: % follows unattributed |
| `\PonePairMemoryVsUnattributedFollowBLo` | 26.8 | P1 pair memory vs unattributed: % follows unattributed, lower 95% CI bound |
| `\PonePairMemoryVsUnattributedFollowBHi` | 38.2 | P1 pair memory vs unattributed: % follows unattributed, upper 95% CI bound |
| `\PonePairMemoryVsUnattributedFollowBCI` | [26.8, 38.2] | P1 pair memory vs unattributed: % follows unattributed, 95% CI |
| `\PonePairMemoryVsUnattributedFollowBN` | 720 | P1 pair memory vs unattributed: % follows unattributed, n |
| `\PonePairMemoryVsUnattributedFollowBP` | n/a | P1 pair memory vs unattributed: % follows unattributed, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsUnattributedEsc` | 66.2 | P1 pair memory vs unattributed: % flags conflict |
| `\PonePairMemoryVsUnattributedEscLo` | 60.0 | P1 pair memory vs unattributed: % flags conflict, lower 95% CI bound |
| `\PonePairMemoryVsUnattributedEscHi` | 72.2 | P1 pair memory vs unattributed: % flags conflict, upper 95% CI bound |
| `\PonePairMemoryVsUnattributedEscCI` | [60.0, 72.2] | P1 pair memory vs unattributed: % flags conflict, 95% CI |
| `\PonePairMemoryVsUnattributedEscN` | 720 | P1 pair memory vs unattributed: % flags conflict, n |
| `\PonePairMemoryVsUnattributedEscP` | n/a | P1 pair memory vs unattributed: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsUnattributedNet` | \ensuremath{-}31.1 | P1 pair memory vs unattributed: net A - B (pp) |
| `\PonePairMemoryVsUnattributedNetLo` | \ensuremath{-}36.9 | P1 pair memory vs unattributed: net A - B (pp), lower 95% CI bound |
| `\PonePairMemoryVsUnattributedNetHi` | \ensuremath{-}25.6 | P1 pair memory vs unattributed: net A - B (pp), upper 95% CI bound |
| `\PonePairMemoryVsUnattributedNetCI` | [\ensuremath{-}36.9, \ensuremath{-}25.6] | P1 pair memory vs unattributed: net A - B (pp), 95% CI |
| `\PonePairMemoryVsUnattributedNetN` | 720 | P1 pair memory vs unattributed: net A - B (pp), n |
| `\PonePairMemoryVsUnattributedNetP` | \ensuremath{<}0.001 | P1 pair memory vs unattributed: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsDocumentFollowA` | 1.4 | P1 pair memory vs document: % follows memory |
| `\PonePairMemoryVsDocumentFollowALo` | 0.4 | P1 pair memory vs document: % follows memory, lower 95% CI bound |
| `\PonePairMemoryVsDocumentFollowAHi` | 2.6 | P1 pair memory vs document: % follows memory, upper 95% CI bound |
| `\PonePairMemoryVsDocumentFollowACI` | [0.4, 2.6] | P1 pair memory vs document: % follows memory, 95% CI |
| `\PonePairMemoryVsDocumentFollowAN` | 720 | P1 pair memory vs document: % follows memory, n |
| `\PonePairMemoryVsDocumentFollowAP` | n/a | P1 pair memory vs document: % follows memory, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsDocumentFollowB` | 31.7 | P1 pair memory vs document: % follows document |
| `\PonePairMemoryVsDocumentFollowBLo` | 26.2 | P1 pair memory vs document: % follows document, lower 95% CI bound |
| `\PonePairMemoryVsDocumentFollowBHi` | 37.5 | P1 pair memory vs document: % follows document, upper 95% CI bound |
| `\PonePairMemoryVsDocumentFollowBCI` | [26.2, 37.5] | P1 pair memory vs document: % follows document, 95% CI |
| `\PonePairMemoryVsDocumentFollowBN` | 720 | P1 pair memory vs document: % follows document, n |
| `\PonePairMemoryVsDocumentFollowBP` | n/a | P1 pair memory vs document: % follows document, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsDocumentEsc` | 66.8 | P1 pair memory vs document: % flags conflict |
| `\PonePairMemoryVsDocumentEscLo` | 60.8 | P1 pair memory vs document: % flags conflict, lower 95% CI bound |
| `\PonePairMemoryVsDocumentEscHi` | 72.4 | P1 pair memory vs document: % flags conflict, upper 95% CI bound |
| `\PonePairMemoryVsDocumentEscCI` | [60.8, 72.4] | P1 pair memory vs document: % flags conflict, 95% CI |
| `\PonePairMemoryVsDocumentEscN` | 720 | P1 pair memory vs document: % flags conflict, n |
| `\PonePairMemoryVsDocumentEscP` | n/a | P1 pair memory vs document: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairMemoryVsDocumentNet` | \ensuremath{-}30.3 | P1 pair memory vs document: net A - B (pp) |
| `\PonePairMemoryVsDocumentNetLo` | \ensuremath{-}36.0 | P1 pair memory vs document: net A - B (pp), lower 95% CI bound |
| `\PonePairMemoryVsDocumentNetHi` | \ensuremath{-}25.1 | P1 pair memory vs document: net A - B (pp), upper 95% CI bound |
| `\PonePairMemoryVsDocumentNetCI` | [\ensuremath{-}36.0, \ensuremath{-}25.1] | P1 pair memory vs document: net A - B (pp), 95% CI |
| `\PonePairMemoryVsDocumentNetN` | 720 | P1 pair memory vs document: net A - B (pp), n |
| `\PonePairMemoryVsDocumentNetP` | \ensuremath{<}0.001 | P1 pair memory vs document: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsWebFollowA` | 30.6 | P1 pair tool vs web: % follows tool |
| `\PonePairToolVsWebFollowALo` | 16.7 | P1 pair tool vs web: % follows tool, lower 95% CI bound |
| `\PonePairToolVsWebFollowAHi` | 45.4 | P1 pair tool vs web: % follows tool, upper 95% CI bound |
| `\PonePairToolVsWebFollowACI` | [16.7, 45.4] | P1 pair tool vs web: % follows tool, 95% CI |
| `\PonePairToolVsWebFollowAN` | 108 | P1 pair tool vs web: % follows tool, n |
| `\PonePairToolVsWebFollowAP` | n/a | P1 pair tool vs web: % follows tool, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsWebFollowB` | 0.0 | P1 pair tool vs web: % follows web |
| `\PonePairToolVsWebFollowBLo` | 0.0 | P1 pair tool vs web: % follows web, lower 95% CI bound |
| `\PonePairToolVsWebFollowBHi` | 3.4 | P1 pair tool vs web: % follows web, upper 95% CI bound |
| `\PonePairToolVsWebFollowBCI` | [0.0, 3.4] | P1 pair tool vs web: % follows web, 95% CI |
| `\PonePairToolVsWebFollowBN` | 108 | P1 pair tool vs web: % follows web, n |
| `\PonePairToolVsWebFollowBP` | n/a | P1 pair tool vs web: % follows web, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsWebEsc` | 69.4 | P1 pair tool vs web: % flags conflict |
| `\PonePairToolVsWebEscLo` | 54.6 | P1 pair tool vs web: % flags conflict, lower 95% CI bound |
| `\PonePairToolVsWebEscHi` | 83.3 | P1 pair tool vs web: % flags conflict, upper 95% CI bound |
| `\PonePairToolVsWebEscCI` | [54.6, 83.3] | P1 pair tool vs web: % flags conflict, 95% CI |
| `\PonePairToolVsWebEscN` | 108 | P1 pair tool vs web: % flags conflict, n |
| `\PonePairToolVsWebEscP` | n/a | P1 pair tool vs web: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsWebNet` | 30.6 | P1 pair tool vs web: net A - B (pp) |
| `\PonePairToolVsWebNetLo` | 16.7 | P1 pair tool vs web: net A - B (pp), lower 95% CI bound |
| `\PonePairToolVsWebNetHi` | 45.4 | P1 pair tool vs web: net A - B (pp), upper 95% CI bound |
| `\PonePairToolVsWebNetCI` | [16.7, 45.4] | P1 pair tool vs web: net A - B (pp), 95% CI |
| `\PonePairToolVsWebNetN` | 108 | P1 pair tool vs web: net A - B (pp), n |
| `\PonePairToolVsWebNetP` | \ensuremath{<}0.001 | P1 pair tool vs web: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsUserFollowA` | 11.0 | P1 pair tool vs user: % follows tool |
| `\PonePairToolVsUserFollowALo` | 7.6 | P1 pair tool vs user: % follows tool, lower 95% CI bound |
| `\PonePairToolVsUserFollowAHi` | 14.9 | P1 pair tool vs user: % follows tool, upper 95% CI bound |
| `\PonePairToolVsUserFollowACI` | [7.6, 14.9] | P1 pair tool vs user: % follows tool, 95% CI |
| `\PonePairToolVsUserFollowAN` | 720 | P1 pair tool vs user: % follows tool, n |
| `\PonePairToolVsUserFollowAP` | n/a | P1 pair tool vs user: % follows tool, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsUserFollowB` | 14.9 | P1 pair tool vs user: % follows user |
| `\PonePairToolVsUserFollowBLo` | 11.0 | P1 pair tool vs user: % follows user, lower 95% CI bound |
| `\PonePairToolVsUserFollowBHi` | 19.2 | P1 pair tool vs user: % follows user, upper 95% CI bound |
| `\PonePairToolVsUserFollowBCI` | [11.0, 19.2] | P1 pair tool vs user: % follows user, 95% CI |
| `\PonePairToolVsUserFollowBN` | 720 | P1 pair tool vs user: % follows user, n |
| `\PonePairToolVsUserFollowBP` | n/a | P1 pair tool vs user: % follows user, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsUserEsc` | 73.5 | P1 pair tool vs user: % flags conflict |
| `\PonePairToolVsUserEscLo` | 68.1 | P1 pair tool vs user: % flags conflict, lower 95% CI bound |
| `\PonePairToolVsUserEscHi` | 78.8 | P1 pair tool vs user: % flags conflict, upper 95% CI bound |
| `\PonePairToolVsUserEscCI` | [68.1, 78.8] | P1 pair tool vs user: % flags conflict, 95% CI |
| `\PonePairToolVsUserEscN` | 720 | P1 pair tool vs user: % flags conflict, n |
| `\PonePairToolVsUserEscP` | n/a | P1 pair tool vs user: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsUserNet` | \ensuremath{-}3.9 | P1 pair tool vs user: net A - B (pp) |
| `\PonePairToolVsUserNetLo` | \ensuremath{-}9.0 | P1 pair tool vs user: net A - B (pp), lower 95% CI bound |
| `\PonePairToolVsUserNetHi` | 1.8 | P1 pair tool vs user: net A - B (pp), upper 95% CI bound |
| `\PonePairToolVsUserNetCI` | [\ensuremath{-}9.0, 1.8] | P1 pair tool vs user: net A - B (pp), 95% CI |
| `\PonePairToolVsUserNetN` | 720 | P1 pair tool vs user: net A - B (pp), n |
| `\PonePairToolVsUserNetP` | 0.196 | P1 pair tool vs user: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsAgentFollowA` | 18.5 | P1 pair tool vs agent: % follows tool |
| `\PonePairToolVsAgentFollowALo` | 6.5 | P1 pair tool vs agent: % follows tool, lower 95% CI bound |
| `\PonePairToolVsAgentFollowAHi` | 31.5 | P1 pair tool vs agent: % follows tool, upper 95% CI bound |
| `\PonePairToolVsAgentFollowACI` | [6.5, 31.5] | P1 pair tool vs agent: % follows tool, 95% CI |
| `\PonePairToolVsAgentFollowAN` | 108 | P1 pair tool vs agent: % follows tool, n |
| `\PonePairToolVsAgentFollowAP` | n/a | P1 pair tool vs agent: % follows tool, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsAgentFollowB` | 2.8 | P1 pair tool vs agent: % follows agent |
| `\PonePairToolVsAgentFollowBLo` | 0.0 | P1 pair tool vs agent: % follows agent, lower 95% CI bound |
| `\PonePairToolVsAgentFollowBHi` | 7.4 | P1 pair tool vs agent: % follows agent, upper 95% CI bound |
| `\PonePairToolVsAgentFollowBCI` | [0.0, 7.4] | P1 pair tool vs agent: % follows agent, 95% CI |
| `\PonePairToolVsAgentFollowBN` | 108 | P1 pair tool vs agent: % follows agent, n |
| `\PonePairToolVsAgentFollowBP` | n/a | P1 pair tool vs agent: % follows agent, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsAgentEsc` | 78.7 | P1 pair tool vs agent: % flags conflict |
| `\PonePairToolVsAgentEscLo` | 63.0 | P1 pair tool vs agent: % flags conflict, lower 95% CI bound |
| `\PonePairToolVsAgentEscHi` | 91.7 | P1 pair tool vs agent: % flags conflict, upper 95% CI bound |
| `\PonePairToolVsAgentEscCI` | [63.0, 91.7] | P1 pair tool vs agent: % flags conflict, 95% CI |
| `\PonePairToolVsAgentEscN` | 108 | P1 pair tool vs agent: % flags conflict, n |
| `\PonePairToolVsAgentEscP` | n/a | P1 pair tool vs agent: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsAgentNet` | 15.7 | P1 pair tool vs agent: net A - B (pp) |
| `\PonePairToolVsAgentNetLo` | 3.7 | P1 pair tool vs agent: net A - B (pp), lower 95% CI bound |
| `\PonePairToolVsAgentNetHi` | 29.6 | P1 pair tool vs agent: net A - B (pp), upper 95% CI bound |
| `\PonePairToolVsAgentNetCI` | [3.7, 29.6] | P1 pair tool vs agent: net A - B (pp), 95% CI |
| `\PonePairToolVsAgentNetN` | 108 | P1 pair tool vs agent: net A - B (pp), n |
| `\PonePairToolVsAgentNetP` | 0.006 | P1 pair tool vs agent: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsUnattributedFollowA` | 14.8 | P1 pair tool vs unattributed: % follows tool |
| `\PonePairToolVsUnattributedFollowALo` | 6.5 | P1 pair tool vs unattributed: % follows tool, lower 95% CI bound |
| `\PonePairToolVsUnattributedFollowAHi` | 25.0 | P1 pair tool vs unattributed: % follows tool, upper 95% CI bound |
| `\PonePairToolVsUnattributedFollowACI` | [6.5, 25.0] | P1 pair tool vs unattributed: % follows tool, 95% CI |
| `\PonePairToolVsUnattributedFollowAN` | 108 | P1 pair tool vs unattributed: % follows tool, n |
| `\PonePairToolVsUnattributedFollowAP` | n/a | P1 pair tool vs unattributed: % follows tool, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsUnattributedFollowB` | 9.3 | P1 pair tool vs unattributed: % follows unattributed |
| `\PonePairToolVsUnattributedFollowBLo` | 3.7 | P1 pair tool vs unattributed: % follows unattributed, lower 95% CI bound |
| `\PonePairToolVsUnattributedFollowBHi` | 15.7 | P1 pair tool vs unattributed: % follows unattributed, upper 95% CI bound |
| `\PonePairToolVsUnattributedFollowBCI` | [3.7, 15.7] | P1 pair tool vs unattributed: % follows unattributed, 95% CI |
| `\PonePairToolVsUnattributedFollowBN` | 108 | P1 pair tool vs unattributed: % follows unattributed, n |
| `\PonePairToolVsUnattributedFollowBP` | n/a | P1 pair tool vs unattributed: % follows unattributed, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsUnattributedEsc` | 75.9 | P1 pair tool vs unattributed: % flags conflict |
| `\PonePairToolVsUnattributedEscLo` | 59.3 | P1 pair tool vs unattributed: % flags conflict, lower 95% CI bound |
| `\PonePairToolVsUnattributedEscHi` | 88.9 | P1 pair tool vs unattributed: % flags conflict, upper 95% CI bound |
| `\PonePairToolVsUnattributedEscCI` | [59.3, 88.9] | P1 pair tool vs unattributed: % flags conflict, 95% CI |
| `\PonePairToolVsUnattributedEscN` | 108 | P1 pair tool vs unattributed: % flags conflict, n |
| `\PonePairToolVsUnattributedEscP` | n/a | P1 pair tool vs unattributed: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsUnattributedNet` | 5.6 | P1 pair tool vs unattributed: net A - B (pp) |
| `\PonePairToolVsUnattributedNetLo` | \ensuremath{-}1.9 | P1 pair tool vs unattributed: net A - B (pp), lower 95% CI bound |
| `\PonePairToolVsUnattributedNetHi` | 13.0 | P1 pair tool vs unattributed: net A - B (pp), upper 95% CI bound |
| `\PonePairToolVsUnattributedNetCI` | [\ensuremath{-}1.9, 13.0] | P1 pair tool vs unattributed: net A - B (pp), 95% CI |
| `\PonePairToolVsUnattributedNetN` | 108 | P1 pair tool vs unattributed: net A - B (pp), n |
| `\PonePairToolVsUnattributedNetP` | 0.144 | P1 pair tool vs unattributed: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsDocumentFollowA` | 6.7 | P1 pair tool vs document: % follows tool |
| `\PonePairToolVsDocumentFollowALo` | 0.0 | P1 pair tool vs document: % follows tool, lower 95% CI bound |
| `\PonePairToolVsDocumentFollowAHi` | 15.8 | P1 pair tool vs document: % follows tool, upper 95% CI bound |
| `\PonePairToolVsDocumentFollowACI` | [0.0, 15.8] | P1 pair tool vs document: % follows tool, 95% CI |
| `\PonePairToolVsDocumentFollowAN` | 120 | P1 pair tool vs document: % follows tool, n |
| `\PonePairToolVsDocumentFollowAP` | n/a | P1 pair tool vs document: % follows tool, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsDocumentFollowB` | 6.7 | P1 pair tool vs document: % follows document |
| `\PonePairToolVsDocumentFollowBLo` | 1.7 | P1 pair tool vs document: % follows document, lower 95% CI bound |
| `\PonePairToolVsDocumentFollowBHi` | 13.3 | P1 pair tool vs document: % follows document, upper 95% CI bound |
| `\PonePairToolVsDocumentFollowBCI` | [1.7, 13.3] | P1 pair tool vs document: % follows document, 95% CI |
| `\PonePairToolVsDocumentFollowBN` | 120 | P1 pair tool vs document: % follows document, n |
| `\PonePairToolVsDocumentFollowBP` | n/a | P1 pair tool vs document: % follows document, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsDocumentEsc` | 85.8 | P1 pair tool vs document: % flags conflict |
| `\PonePairToolVsDocumentEscLo` | 75.0 | P1 pair tool vs document: % flags conflict, lower 95% CI bound |
| `\PonePairToolVsDocumentEscHi` | 94.2 | P1 pair tool vs document: % flags conflict, upper 95% CI bound |
| `\PonePairToolVsDocumentEscCI` | [75.0, 94.2] | P1 pair tool vs document: % flags conflict, 95% CI |
| `\PonePairToolVsDocumentEscN` | 120 | P1 pair tool vs document: % flags conflict, n |
| `\PonePairToolVsDocumentEscP` | n/a | P1 pair tool vs document: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairToolVsDocumentNet` | 0.0 | P1 pair tool vs document: net A - B (pp) |
| `\PonePairToolVsDocumentNetLo` | \ensuremath{-}9.2 | P1 pair tool vs document: net A - B (pp), lower 95% CI bound |
| `\PonePairToolVsDocumentNetHi` | 10.8 | P1 pair tool vs document: net A - B (pp), upper 95% CI bound |
| `\PonePairToolVsDocumentNetCI` | [\ensuremath{-}9.2, 10.8] | P1 pair tool vs document: net A - B (pp), 95% CI |
| `\PonePairToolVsDocumentNetN` | 120 | P1 pair tool vs document: net A - B (pp), n |
| `\PonePairToolVsDocumentNetP` | 1.000 | P1 pair tool vs document: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsUserFollowA` | 0.9 | P1 pair web vs user: % follows web |
| `\PonePairWebVsUserFollowALo` | 0.0 | P1 pair web vs user: % follows web, lower 95% CI bound |
| `\PonePairWebVsUserFollowAHi` | 2.6 | P1 pair web vs user: % follows web, upper 95% CI bound |
| `\PonePairWebVsUserFollowACI` | [0.0, 2.6] | P1 pair web vs user: % follows web, 95% CI |
| `\PonePairWebVsUserFollowAN` | 114 | P1 pair web vs user: % follows web, n |
| `\PonePairWebVsUserFollowAP` | n/a | P1 pair web vs user: % follows web, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsUserFollowB` | 22.8 | P1 pair web vs user: % follows user |
| `\PonePairWebVsUserFollowBLo` | 11.4 | P1 pair web vs user: % follows user, lower 95% CI bound |
| `\PonePairWebVsUserFollowBHi` | 35.1 | P1 pair web vs user: % follows user, upper 95% CI bound |
| `\PonePairWebVsUserFollowBCI` | [11.4, 35.1] | P1 pair web vs user: % follows user, 95% CI |
| `\PonePairWebVsUserFollowBN` | 114 | P1 pair web vs user: % follows user, n |
| `\PonePairWebVsUserFollowBP` | n/a | P1 pair web vs user: % follows user, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsUserEsc` | 76.3 | P1 pair web vs user: % flags conflict |
| `\PonePairWebVsUserEscLo` | 63.2 | P1 pair web vs user: % flags conflict, lower 95% CI bound |
| `\PonePairWebVsUserEscHi` | 87.7 | P1 pair web vs user: % flags conflict, upper 95% CI bound |
| `\PonePairWebVsUserEscCI` | [63.2, 87.7] | P1 pair web vs user: % flags conflict, 95% CI |
| `\PonePairWebVsUserEscN` | 114 | P1 pair web vs user: % flags conflict, n |
| `\PonePairWebVsUserEscP` | n/a | P1 pair web vs user: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsUserNet` | \ensuremath{-}21.9 | P1 pair web vs user: net A - B (pp) |
| `\PonePairWebVsUserNetLo` | \ensuremath{-}36.0 | P1 pair web vs user: net A - B (pp), lower 95% CI bound |
| `\PonePairWebVsUserNetHi` | \ensuremath{-}9.6 | P1 pair web vs user: net A - B (pp), upper 95% CI bound |
| `\PonePairWebVsUserNetCI` | [\ensuremath{-}36.0, \ensuremath{-}9.6] | P1 pair web vs user: net A - B (pp), 95% CI |
| `\PonePairWebVsUserNetN` | 114 | P1 pair web vs user: net A - B (pp), n |
| `\PonePairWebVsUserNetP` | \ensuremath{<}0.001 | P1 pair web vs user: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsAgentFollowA` | 1.9 | P1 pair web vs agent: % follows web |
| `\PonePairWebVsAgentFollowALo` | 0.0 | P1 pair web vs agent: % follows web, lower 95% CI bound |
| `\PonePairWebVsAgentFollowAHi` | 5.6 | P1 pair web vs agent: % follows web, upper 95% CI bound |
| `\PonePairWebVsAgentFollowACI` | [0.0, 5.6] | P1 pair web vs agent: % follows web, 95% CI |
| `\PonePairWebVsAgentFollowAN` | 108 | P1 pair web vs agent: % follows web, n |
| `\PonePairWebVsAgentFollowAP` | n/a | P1 pair web vs agent: % follows web, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsAgentFollowB` | 2.8 | P1 pair web vs agent: % follows agent |
| `\PonePairWebVsAgentFollowBLo` | 0.0 | P1 pair web vs agent: % follows agent, lower 95% CI bound |
| `\PonePairWebVsAgentFollowBHi` | 7.4 | P1 pair web vs agent: % follows agent, upper 95% CI bound |
| `\PonePairWebVsAgentFollowBCI` | [0.0, 7.4] | P1 pair web vs agent: % follows agent, 95% CI |
| `\PonePairWebVsAgentFollowBN` | 108 | P1 pair web vs agent: % follows agent, n |
| `\PonePairWebVsAgentFollowBP` | n/a | P1 pair web vs agent: % follows agent, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsAgentEsc` | 95.4 | P1 pair web vs agent: % flags conflict |
| `\PonePairWebVsAgentEscLo` | 89.8 | P1 pair web vs agent: % flags conflict, lower 95% CI bound |
| `\PonePairWebVsAgentEscHi` | 100.0 | P1 pair web vs agent: % flags conflict, upper 95% CI bound |
| `\PonePairWebVsAgentEscCI` | [89.8, 100.0] | P1 pair web vs agent: % flags conflict, 95% CI |
| `\PonePairWebVsAgentEscN` | 108 | P1 pair web vs agent: % flags conflict, n |
| `\PonePairWebVsAgentEscP` | n/a | P1 pair web vs agent: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsAgentNet` | \ensuremath{-}0.9 | P1 pair web vs agent: net A - B (pp) |
| `\PonePairWebVsAgentNetLo` | \ensuremath{-}6.5 | P1 pair web vs agent: net A - B (pp), lower 95% CI bound |
| `\PonePairWebVsAgentNetHi` | 4.6 | P1 pair web vs agent: net A - B (pp), upper 95% CI bound |
| `\PonePairWebVsAgentNetCI` | [\ensuremath{-}6.5, 4.6] | P1 pair web vs agent: net A - B (pp), 95% CI |
| `\PonePairWebVsAgentNetN` | 108 | P1 pair web vs agent: net A - B (pp), n |
| `\PonePairWebVsAgentNetP` | 0.903 | P1 pair web vs agent: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsUnattributedFollowA` | 0.9 | P1 pair web vs unattributed: % follows web |
| `\PonePairWebVsUnattributedFollowALo` | 0.0 | P1 pair web vs unattributed: % follows web, lower 95% CI bound |
| `\PonePairWebVsUnattributedFollowAHi` | 2.8 | P1 pair web vs unattributed: % follows web, upper 95% CI bound |
| `\PonePairWebVsUnattributedFollowACI` | [0.0, 2.8] | P1 pair web vs unattributed: % follows web, 95% CI |
| `\PonePairWebVsUnattributedFollowAN` | 108 | P1 pair web vs unattributed: % follows web, n |
| `\PonePairWebVsUnattributedFollowAP` | n/a | P1 pair web vs unattributed: % follows web, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsUnattributedFollowB` | 20.4 | P1 pair web vs unattributed: % follows unattributed |
| `\PonePairWebVsUnattributedFollowBLo` | 7.4 | P1 pair web vs unattributed: % follows unattributed, lower 95% CI bound |
| `\PonePairWebVsUnattributedFollowBHi` | 37.0 | P1 pair web vs unattributed: % follows unattributed, upper 95% CI bound |
| `\PonePairWebVsUnattributedFollowBCI` | [7.4, 37.0] | P1 pair web vs unattributed: % follows unattributed, 95% CI |
| `\PonePairWebVsUnattributedFollowBN` | 108 | P1 pair web vs unattributed: % follows unattributed, n |
| `\PonePairWebVsUnattributedFollowBP` | n/a | P1 pair web vs unattributed: % follows unattributed, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsUnattributedEsc` | 77.8 | P1 pair web vs unattributed: % flags conflict |
| `\PonePairWebVsUnattributedEscLo` | 61.1 | P1 pair web vs unattributed: % flags conflict, lower 95% CI bound |
| `\PonePairWebVsUnattributedEscHi` | 92.6 | P1 pair web vs unattributed: % flags conflict, upper 95% CI bound |
| `\PonePairWebVsUnattributedEscCI` | [61.1, 92.6] | P1 pair web vs unattributed: % flags conflict, 95% CI |
| `\PonePairWebVsUnattributedEscN` | 108 | P1 pair web vs unattributed: % flags conflict, n |
| `\PonePairWebVsUnattributedEscP` | n/a | P1 pair web vs unattributed: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsUnattributedNet` | \ensuremath{-}19.4 | P1 pair web vs unattributed: net A - B (pp) |
| `\PonePairWebVsUnattributedNetLo` | \ensuremath{-}34.3 | P1 pair web vs unattributed: net A - B (pp), lower 95% CI bound |
| `\PonePairWebVsUnattributedNetHi` | \ensuremath{-}6.5 | P1 pair web vs unattributed: net A - B (pp), upper 95% CI bound |
| `\PonePairWebVsUnattributedNetCI` | [\ensuremath{-}34.3, \ensuremath{-}6.5] | P1 pair web vs unattributed: net A - B (pp), 95% CI |
| `\PonePairWebVsUnattributedNetN` | 108 | P1 pair web vs unattributed: net A - B (pp), n |
| `\PonePairWebVsUnattributedNetP` | \ensuremath{<}0.001 | P1 pair web vs unattributed: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsDocumentFollowA` | 0.9 | P1 pair web vs document: % follows web |
| `\PonePairWebVsDocumentFollowALo` | 0.0 | P1 pair web vs document: % follows web, lower 95% CI bound |
| `\PonePairWebVsDocumentFollowAHi` | 2.8 | P1 pair web vs document: % follows web, upper 95% CI bound |
| `\PonePairWebVsDocumentFollowACI` | [0.0, 2.8] | P1 pair web vs document: % follows web, 95% CI |
| `\PonePairWebVsDocumentFollowAN` | 108 | P1 pair web vs document: % follows web, n |
| `\PonePairWebVsDocumentFollowAP` | n/a | P1 pair web vs document: % follows web, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsDocumentFollowB` | 22.2 | P1 pair web vs document: % follows document |
| `\PonePairWebVsDocumentFollowBLo` | 10.2 | P1 pair web vs document: % follows document, lower 95% CI bound |
| `\PonePairWebVsDocumentFollowBHi` | 35.2 | P1 pair web vs document: % follows document, upper 95% CI bound |
| `\PonePairWebVsDocumentFollowBCI` | [10.2, 35.2] | P1 pair web vs document: % follows document, 95% CI |
| `\PonePairWebVsDocumentFollowBN` | 108 | P1 pair web vs document: % follows document, n |
| `\PonePairWebVsDocumentFollowBP` | n/a | P1 pair web vs document: % follows document, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsDocumentEsc` | 76.9 | P1 pair web vs document: % flags conflict |
| `\PonePairWebVsDocumentEscLo` | 63.0 | P1 pair web vs document: % flags conflict, lower 95% CI bound |
| `\PonePairWebVsDocumentEscHi` | 89.8 | P1 pair web vs document: % flags conflict, upper 95% CI bound |
| `\PonePairWebVsDocumentEscCI` | [63.0, 89.8] | P1 pair web vs document: % flags conflict, 95% CI |
| `\PonePairWebVsDocumentEscN` | 108 | P1 pair web vs document: % flags conflict, n |
| `\PonePairWebVsDocumentEscP` | n/a | P1 pair web vs document: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairWebVsDocumentNet` | \ensuremath{-}21.3 | P1 pair web vs document: net A - B (pp) |
| `\PonePairWebVsDocumentNetLo` | \ensuremath{-}34.3 | P1 pair web vs document: net A - B (pp), lower 95% CI bound |
| `\PonePairWebVsDocumentNetHi` | \ensuremath{-}9.3 | P1 pair web vs document: net A - B (pp), upper 95% CI bound |
| `\PonePairWebVsDocumentNetCI` | [\ensuremath{-}34.3, \ensuremath{-}9.3] | P1 pair web vs document: net A - B (pp), 95% CI |
| `\PonePairWebVsDocumentNetN` | 108 | P1 pair web vs document: net A - B (pp), n |
| `\PonePairWebVsDocumentNetP` | \ensuremath{<}0.001 | P1 pair web vs document: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsAgentFollowA` | 25.0 | P1 pair user vs agent: % follows user |
| `\PonePairUserVsAgentFollowALo` | 11.1 | P1 pair user vs agent: % follows user, lower 95% CI bound |
| `\PonePairUserVsAgentFollowAHi` | 42.6 | P1 pair user vs agent: % follows user, upper 95% CI bound |
| `\PonePairUserVsAgentFollowACI` | [11.1, 42.6] | P1 pair user vs agent: % follows user, 95% CI |
| `\PonePairUserVsAgentFollowAN` | 108 | P1 pair user vs agent: % follows user, n |
| `\PonePairUserVsAgentFollowAP` | n/a | P1 pair user vs agent: % follows user, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsAgentFollowB` | 4.6 | P1 pair user vs agent: % follows agent |
| `\PonePairUserVsAgentFollowBLo` | 0.0 | P1 pair user vs agent: % follows agent, lower 95% CI bound |
| `\PonePairUserVsAgentFollowBHi` | 11.1 | P1 pair user vs agent: % follows agent, upper 95% CI bound |
| `\PonePairUserVsAgentFollowBCI` | [0.0, 11.1] | P1 pair user vs agent: % follows agent, 95% CI |
| `\PonePairUserVsAgentFollowBN` | 108 | P1 pair user vs agent: % follows agent, n |
| `\PonePairUserVsAgentFollowBP` | n/a | P1 pair user vs agent: % follows agent, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsAgentEsc` | 70.4 | P1 pair user vs agent: % flags conflict |
| `\PonePairUserVsAgentEscLo` | 51.8 | P1 pair user vs agent: % flags conflict, lower 95% CI bound |
| `\PonePairUserVsAgentEscHi` | 88.0 | P1 pair user vs agent: % flags conflict, upper 95% CI bound |
| `\PonePairUserVsAgentEscCI` | [51.8, 88.0] | P1 pair user vs agent: % flags conflict, 95% CI |
| `\PonePairUserVsAgentEscN` | 108 | P1 pair user vs agent: % flags conflict, n |
| `\PonePairUserVsAgentEscP` | n/a | P1 pair user vs agent: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsAgentNet` | 20.4 | P1 pair user vs agent: net A - B (pp) |
| `\PonePairUserVsAgentNetLo` | 8.3 | P1 pair user vs agent: net A - B (pp), lower 95% CI bound |
| `\PonePairUserVsAgentNetHi` | 35.2 | P1 pair user vs agent: net A - B (pp), upper 95% CI bound |
| `\PonePairUserVsAgentNetCI` | [8.3, 35.2] | P1 pair user vs agent: net A - B (pp), 95% CI |
| `\PonePairUserVsAgentNetN` | 108 | P1 pair user vs agent: net A - B (pp), n |
| `\PonePairUserVsAgentNetP` | \ensuremath{<}0.001 | P1 pair user vs agent: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsUnattributedFollowA` | 17.6 | P1 pair user vs unattributed: % follows user |
| `\PonePairUserVsUnattributedFollowALo` | 3.7 | P1 pair user vs unattributed: % follows user, lower 95% CI bound |
| `\PonePairUserVsUnattributedFollowAHi` | 33.3 | P1 pair user vs unattributed: % follows user, upper 95% CI bound |
| `\PonePairUserVsUnattributedFollowACI` | [3.7, 33.3] | P1 pair user vs unattributed: % follows user, 95% CI |
| `\PonePairUserVsUnattributedFollowAN` | 108 | P1 pair user vs unattributed: % follows user, n |
| `\PonePairUserVsUnattributedFollowAP` | n/a | P1 pair user vs unattributed: % follows user, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsUnattributedFollowB` | 1.9 | P1 pair user vs unattributed: % follows unattributed |
| `\PonePairUserVsUnattributedFollowBLo` | 0.0 | P1 pair user vs unattributed: % follows unattributed, lower 95% CI bound |
| `\PonePairUserVsUnattributedFollowBHi` | 4.6 | P1 pair user vs unattributed: % follows unattributed, upper 95% CI bound |
| `\PonePairUserVsUnattributedFollowBCI` | [0.0, 4.6] | P1 pair user vs unattributed: % follows unattributed, 95% CI |
| `\PonePairUserVsUnattributedFollowBN` | 108 | P1 pair user vs unattributed: % follows unattributed, n |
| `\PonePairUserVsUnattributedFollowBP` | n/a | P1 pair user vs unattributed: % follows unattributed, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsUnattributedEsc` | 80.6 | P1 pair user vs unattributed: % flags conflict |
| `\PonePairUserVsUnattributedEscLo` | 63.0 | P1 pair user vs unattributed: % flags conflict, lower 95% CI bound |
| `\PonePairUserVsUnattributedEscHi` | 94.4 | P1 pair user vs unattributed: % flags conflict, upper 95% CI bound |
| `\PonePairUserVsUnattributedEscCI` | [63.0, 94.4] | P1 pair user vs unattributed: % flags conflict, 95% CI |
| `\PonePairUserVsUnattributedEscN` | 108 | P1 pair user vs unattributed: % flags conflict, n |
| `\PonePairUserVsUnattributedEscP` | n/a | P1 pair user vs unattributed: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsUnattributedNet` | 15.7 | P1 pair user vs unattributed: net A - B (pp) |
| `\PonePairUserVsUnattributedNetLo` | 1.9 | P1 pair user vs unattributed: net A - B (pp), lower 95% CI bound |
| `\PonePairUserVsUnattributedNetHi` | 32.4 | P1 pair user vs unattributed: net A - B (pp), upper 95% CI bound |
| `\PonePairUserVsUnattributedNetCI` | [1.9, 32.4] | P1 pair user vs unattributed: net A - B (pp), 95% CI |
| `\PonePairUserVsUnattributedNetN` | 108 | P1 pair user vs unattributed: net A - B (pp), n |
| `\PonePairUserVsUnattributedNetP` | 0.032 | P1 pair user vs unattributed: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsDocumentFollowA` | 14.4 | P1 pair user vs document: % follows user |
| `\PonePairUserVsDocumentFollowALo` | 9.9 | P1 pair user vs document: % follows user, lower 95% CI bound |
| `\PonePairUserVsDocumentFollowAHi` | 19.4 | P1 pair user vs document: % follows user, upper 95% CI bound |
| `\PonePairUserVsDocumentFollowACI` | [9.9, 19.4] | P1 pair user vs document: % follows user, 95% CI |
| `\PonePairUserVsDocumentFollowAN` | 720 | P1 pair user vs document: % follows user, n |
| `\PonePairUserVsDocumentFollowAP` | n/a | P1 pair user vs document: % follows user, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsDocumentFollowB` | 7.6 | P1 pair user vs document: % follows document |
| `\PonePairUserVsDocumentFollowBLo` | 5.0 | P1 pair user vs document: % follows document, lower 95% CI bound |
| `\PonePairUserVsDocumentFollowBHi` | 10.7 | P1 pair user vs document: % follows document, upper 95% CI bound |
| `\PonePairUserVsDocumentFollowBCI` | [5.0, 10.7] | P1 pair user vs document: % follows document, 95% CI |
| `\PonePairUserVsDocumentFollowBN` | 720 | P1 pair user vs document: % follows document, n |
| `\PonePairUserVsDocumentFollowBP` | n/a | P1 pair user vs document: % follows document, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsDocumentEsc` | 77.6 | P1 pair user vs document: % flags conflict |
| `\PonePairUserVsDocumentEscLo` | 71.8 | P1 pair user vs document: % flags conflict, lower 95% CI bound |
| `\PonePairUserVsDocumentEscHi` | 83.1 | P1 pair user vs document: % flags conflict, upper 95% CI bound |
| `\PonePairUserVsDocumentEscCI` | [71.8, 83.1] | P1 pair user vs document: % flags conflict, 95% CI |
| `\PonePairUserVsDocumentEscN` | 720 | P1 pair user vs document: % flags conflict, n |
| `\PonePairUserVsDocumentEscP` | n/a | P1 pair user vs document: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUserVsDocumentNet` | 6.8 | P1 pair user vs document: net A - B (pp) |
| `\PonePairUserVsDocumentNetLo` | 2.1 | P1 pair user vs document: net A - B (pp), lower 95% CI bound |
| `\PonePairUserVsDocumentNetHi` | 12.2 | P1 pair user vs document: net A - B (pp), upper 95% CI bound |
| `\PonePairUserVsDocumentNetCI` | [2.1, 12.2] | P1 pair user vs document: net A - B (pp), 95% CI |
| `\PonePairUserVsDocumentNetN` | 720 | P1 pair user vs document: net A - B (pp), n |
| `\PonePairUserVsDocumentNetP` | 0.003 | P1 pair user vs document: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairAgentVsUnattributedFollowA` | 4.8 | P1 pair agent vs unattributed: % follows agent |
| `\PonePairAgentVsUnattributedFollowALo` | 1.6 | P1 pair agent vs unattributed: % follows agent, lower 95% CI bound |
| `\PonePairAgentVsUnattributedFollowAHi` | 8.7 | P1 pair agent vs unattributed: % follows agent, upper 95% CI bound |
| `\PonePairAgentVsUnattributedFollowACI` | [1.6, 8.7] | P1 pair agent vs unattributed: % follows agent, 95% CI |
| `\PonePairAgentVsUnattributedFollowAN` | 126 | P1 pair agent vs unattributed: % follows agent, n |
| `\PonePairAgentVsUnattributedFollowAP` | n/a | P1 pair agent vs unattributed: % follows agent, two-sided bootstrap p (n/a if not tested) |
| `\PonePairAgentVsUnattributedFollowB` | 13.5 | P1 pair agent vs unattributed: % follows unattributed |
| `\PonePairAgentVsUnattributedFollowBLo` | 4.8 | P1 pair agent vs unattributed: % follows unattributed, lower 95% CI bound |
| `\PonePairAgentVsUnattributedFollowBHi` | 23.8 | P1 pair agent vs unattributed: % follows unattributed, upper 95% CI bound |
| `\PonePairAgentVsUnattributedFollowBCI` | [4.8, 23.8] | P1 pair agent vs unattributed: % follows unattributed, 95% CI |
| `\PonePairAgentVsUnattributedFollowBN` | 126 | P1 pair agent vs unattributed: % follows unattributed, n |
| `\PonePairAgentVsUnattributedFollowBP` | n/a | P1 pair agent vs unattributed: % follows unattributed, two-sided bootstrap p (n/a if not tested) |
| `\PonePairAgentVsUnattributedEsc` | 81.7 | P1 pair agent vs unattributed: % flags conflict |
| `\PonePairAgentVsUnattributedEscLo` | 68.3 | P1 pair agent vs unattributed: % flags conflict, lower 95% CI bound |
| `\PonePairAgentVsUnattributedEscHi` | 92.9 | P1 pair agent vs unattributed: % flags conflict, upper 95% CI bound |
| `\PonePairAgentVsUnattributedEscCI` | [68.3, 92.9] | P1 pair agent vs unattributed: % flags conflict, 95% CI |
| `\PonePairAgentVsUnattributedEscN` | 126 | P1 pair agent vs unattributed: % flags conflict, n |
| `\PonePairAgentVsUnattributedEscP` | n/a | P1 pair agent vs unattributed: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairAgentVsUnattributedNet` | \ensuremath{-}8.7 | P1 pair agent vs unattributed: net A - B (pp) |
| `\PonePairAgentVsUnattributedNetLo` | \ensuremath{-}19.0 | P1 pair agent vs unattributed: net A - B (pp), lower 95% CI bound |
| `\PonePairAgentVsUnattributedNetHi` | \ensuremath{-}0.8 | P1 pair agent vs unattributed: net A - B (pp), upper 95% CI bound |
| `\PonePairAgentVsUnattributedNetCI` | [\ensuremath{-}19.0, \ensuremath{-}0.8] | P1 pair agent vs unattributed: net A - B (pp), 95% CI |
| `\PonePairAgentVsUnattributedNetN` | 126 | P1 pair agent vs unattributed: net A - B (pp), n |
| `\PonePairAgentVsUnattributedNetP` | 0.047 | P1 pair agent vs unattributed: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairAgentVsDocumentFollowA` | 3.7 | P1 pair agent vs document: % follows agent |
| `\PonePairAgentVsDocumentFollowALo` | 0.0 | P1 pair agent vs document: % follows agent, lower 95% CI bound |
| `\PonePairAgentVsDocumentFollowAHi` | 8.3 | P1 pair agent vs document: % follows agent, upper 95% CI bound |
| `\PonePairAgentVsDocumentFollowACI` | [0.0, 8.3] | P1 pair agent vs document: % follows agent, 95% CI |
| `\PonePairAgentVsDocumentFollowAN` | 108 | P1 pair agent vs document: % follows agent, n |
| `\PonePairAgentVsDocumentFollowAP` | n/a | P1 pair agent vs document: % follows agent, two-sided bootstrap p (n/a if not tested) |
| `\PonePairAgentVsDocumentFollowB` | 6.5 | P1 pair agent vs document: % follows document |
| `\PonePairAgentVsDocumentFollowBLo` | 0.9 | P1 pair agent vs document: % follows document, lower 95% CI bound |
| `\PonePairAgentVsDocumentFollowBHi` | 15.7 | P1 pair agent vs document: % follows document, upper 95% CI bound |
| `\PonePairAgentVsDocumentFollowBCI` | [0.9, 15.7] | P1 pair agent vs document: % follows document, 95% CI |
| `\PonePairAgentVsDocumentFollowBN` | 108 | P1 pair agent vs document: % follows document, n |
| `\PonePairAgentVsDocumentFollowBP` | n/a | P1 pair agent vs document: % follows document, two-sided bootstrap p (n/a if not tested) |
| `\PonePairAgentVsDocumentEsc` | 88.9 | P1 pair agent vs document: % flags conflict |
| `\PonePairAgentVsDocumentEscLo` | 78.7 | P1 pair agent vs document: % flags conflict, lower 95% CI bound |
| `\PonePairAgentVsDocumentEscHi` | 96.3 | P1 pair agent vs document: % flags conflict, upper 95% CI bound |
| `\PonePairAgentVsDocumentEscCI` | [78.7, 96.3] | P1 pair agent vs document: % flags conflict, 95% CI |
| `\PonePairAgentVsDocumentEscN` | 108 | P1 pair agent vs document: % flags conflict, n |
| `\PonePairAgentVsDocumentEscP` | n/a | P1 pair agent vs document: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairAgentVsDocumentNet` | \ensuremath{-}2.8 | P1 pair agent vs document: net A - B (pp) |
| `\PonePairAgentVsDocumentNetLo` | \ensuremath{-}12.0 | P1 pair agent vs document: net A - B (pp), lower 95% CI bound |
| `\PonePairAgentVsDocumentNetHi` | 3.7 | P1 pair agent vs document: net A - B (pp), upper 95% CI bound |
| `\PonePairAgentVsDocumentNetCI` | [\ensuremath{-}12.0, 3.7] | P1 pair agent vs document: net A - B (pp), 95% CI |
| `\PonePairAgentVsDocumentNetN` | 108 | P1 pair agent vs document: net A - B (pp), n |
| `\PonePairAgentVsDocumentNetP` | 0.638 | P1 pair agent vs document: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PonePairUnattributedVsDocumentFollowA` | 6.5 | P1 pair unattributed vs document: % follows unattributed |
| `\PonePairUnattributedVsDocumentFollowALo` | 1.9 | P1 pair unattributed vs document: % follows unattributed, lower 95% CI bound |
| `\PonePairUnattributedVsDocumentFollowAHi` | 12.0 | P1 pair unattributed vs document: % follows unattributed, upper 95% CI bound |
| `\PonePairUnattributedVsDocumentFollowACI` | [1.9, 12.0] | P1 pair unattributed vs document: % follows unattributed, 95% CI |
| `\PonePairUnattributedVsDocumentFollowAN` | 108 | P1 pair unattributed vs document: % follows unattributed, n |
| `\PonePairUnattributedVsDocumentFollowAP` | n/a | P1 pair unattributed vs document: % follows unattributed, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUnattributedVsDocumentFollowB` | 20.4 | P1 pair unattributed vs document: % follows document |
| `\PonePairUnattributedVsDocumentFollowBLo` | 9.3 | P1 pair unattributed vs document: % follows document, lower 95% CI bound |
| `\PonePairUnattributedVsDocumentFollowBHi` | 33.3 | P1 pair unattributed vs document: % follows document, upper 95% CI bound |
| `\PonePairUnattributedVsDocumentFollowBCI` | [9.3, 33.3] | P1 pair unattributed vs document: % follows document, 95% CI |
| `\PonePairUnattributedVsDocumentFollowBN` | 108 | P1 pair unattributed vs document: % follows document, n |
| `\PonePairUnattributedVsDocumentFollowBP` | n/a | P1 pair unattributed vs document: % follows document, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUnattributedVsDocumentEsc` | 73.1 | P1 pair unattributed vs document: % flags conflict |
| `\PonePairUnattributedVsDocumentEscLo` | 57.4 | P1 pair unattributed vs document: % flags conflict, lower 95% CI bound |
| `\PonePairUnattributedVsDocumentEscHi` | 88.9 | P1 pair unattributed vs document: % flags conflict, upper 95% CI bound |
| `\PonePairUnattributedVsDocumentEscCI` | [57.4, 88.9] | P1 pair unattributed vs document: % flags conflict, 95% CI |
| `\PonePairUnattributedVsDocumentEscN` | 108 | P1 pair unattributed vs document: % flags conflict, n |
| `\PonePairUnattributedVsDocumentEscP` | n/a | P1 pair unattributed vs document: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PonePairUnattributedVsDocumentNet` | \ensuremath{-}13.9 | P1 pair unattributed vs document: net A - B (pp) |
| `\PonePairUnattributedVsDocumentNetLo` | \ensuremath{-}24.1 | P1 pair unattributed vs document: net A - B (pp), lower 95% CI bound |
| `\PonePairUnattributedVsDocumentNetHi` | \ensuremath{-}4.6 | P1 pair unattributed vs document: net A - B (pp), upper 95% CI bound |
| `\PonePairUnattributedVsDocumentNetCI` | [\ensuremath{-}24.1, \ensuremath{-}4.6] | P1 pair unattributed vs document: net A - B (pp), 95% CI |
| `\PonePairUnattributedVsDocumentNetN` | 108 | P1 pair unattributed vs document: net A - B (pp), n |
| `\PonePairUnattributedVsDocumentNetP` | 0.005 | P1 pair unattributed vs document: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsToolFollowA` | 5.6 | P1 forced memory vs tool: % follows memory |
| `\PoneForcedMemoryVsToolFollowALo` | 2.5 | P1 forced memory vs tool: % follows memory, lower 95% CI bound |
| `\PoneForcedMemoryVsToolFollowAHi` | 9.2 | P1 forced memory vs tool: % follows memory, upper 95% CI bound |
| `\PoneForcedMemoryVsToolFollowACI` | [2.5, 9.2] | P1 forced memory vs tool: % follows memory, 95% CI |
| `\PoneForcedMemoryVsToolFollowAN` | 360 | P1 forced memory vs tool: % follows memory, n |
| `\PoneForcedMemoryVsToolFollowAP` | n/a | P1 forced memory vs tool: % follows memory, two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsToolFollowB` | 94.4 | P1 forced memory vs tool: % follows tool |
| `\PoneForcedMemoryVsToolFollowBLo` | 91.1 | P1 forced memory vs tool: % follows tool, lower 95% CI bound |
| `\PoneForcedMemoryVsToolFollowBHi` | 97.5 | P1 forced memory vs tool: % follows tool, upper 95% CI bound |
| `\PoneForcedMemoryVsToolFollowBCI` | [91.1, 97.5] | P1 forced memory vs tool: % follows tool, 95% CI |
| `\PoneForcedMemoryVsToolFollowBN` | 360 | P1 forced memory vs tool: % follows tool, n |
| `\PoneForcedMemoryVsToolFollowBP` | n/a | P1 forced memory vs tool: % follows tool, two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsToolEsc` | 0.0 | P1 forced memory vs tool: % flags conflict |
| `\PoneForcedMemoryVsToolEscLo` | 0.0 | P1 forced memory vs tool: % flags conflict, lower 95% CI bound |
| `\PoneForcedMemoryVsToolEscHi` | 1.0 | P1 forced memory vs tool: % flags conflict, upper 95% CI bound |
| `\PoneForcedMemoryVsToolEscCI` | [0.0, 1.0] | P1 forced memory vs tool: % flags conflict, 95% CI |
| `\PoneForcedMemoryVsToolEscN` | 360 | P1 forced memory vs tool: % flags conflict, n |
| `\PoneForcedMemoryVsToolEscP` | n/a | P1 forced memory vs tool: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsToolNet` | \ensuremath{-}88.9 | P1 forced memory vs tool: net A - B (pp) |
| `\PoneForcedMemoryVsToolNetLo` | \ensuremath{-}94.4 | P1 forced memory vs tool: net A - B (pp), lower 95% CI bound |
| `\PoneForcedMemoryVsToolNetHi` | \ensuremath{-}82.2 | P1 forced memory vs tool: net A - B (pp), upper 95% CI bound |
| `\PoneForcedMemoryVsToolNetCI` | [\ensuremath{-}94.4, \ensuremath{-}82.2] | P1 forced memory vs tool: net A - B (pp), 95% CI |
| `\PoneForcedMemoryVsToolNetN` | 360 | P1 forced memory vs tool: net A - B (pp), n |
| `\PoneForcedMemoryVsToolNetP` | \ensuremath{<}0.001 | P1 forced memory vs tool: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsUserFollowA` | 7.5 | P1 forced memory vs user: % follows memory |
| `\PoneForcedMemoryVsUserFollowALo` | 4.4 | P1 forced memory vs user: % follows memory, lower 95% CI bound |
| `\PoneForcedMemoryVsUserFollowAHi` | 10.8 | P1 forced memory vs user: % follows memory, upper 95% CI bound |
| `\PoneForcedMemoryVsUserFollowACI` | [4.4, 10.8] | P1 forced memory vs user: % follows memory, 95% CI |
| `\PoneForcedMemoryVsUserFollowAN` | 360 | P1 forced memory vs user: % follows memory, n |
| `\PoneForcedMemoryVsUserFollowAP` | n/a | P1 forced memory vs user: % follows memory, two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsUserFollowB` | 92.5 | P1 forced memory vs user: % follows user |
| `\PoneForcedMemoryVsUserFollowBLo` | 89.2 | P1 forced memory vs user: % follows user, lower 95% CI bound |
| `\PoneForcedMemoryVsUserFollowBHi` | 95.8 | P1 forced memory vs user: % follows user, upper 95% CI bound |
| `\PoneForcedMemoryVsUserFollowBCI` | [89.2, 95.8] | P1 forced memory vs user: % follows user, 95% CI |
| `\PoneForcedMemoryVsUserFollowBN` | 360 | P1 forced memory vs user: % follows user, n |
| `\PoneForcedMemoryVsUserFollowBP` | n/a | P1 forced memory vs user: % follows user, two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsUserEsc` | 0.0 | P1 forced memory vs user: % flags conflict |
| `\PoneForcedMemoryVsUserEscLo` | 0.0 | P1 forced memory vs user: % flags conflict, lower 95% CI bound |
| `\PoneForcedMemoryVsUserEscHi` | 1.0 | P1 forced memory vs user: % flags conflict, upper 95% CI bound |
| `\PoneForcedMemoryVsUserEscCI` | [0.0, 1.0] | P1 forced memory vs user: % flags conflict, 95% CI |
| `\PoneForcedMemoryVsUserEscN` | 360 | P1 forced memory vs user: % flags conflict, n |
| `\PoneForcedMemoryVsUserEscP` | n/a | P1 forced memory vs user: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsUserNet` | \ensuremath{-}85.0 | P1 forced memory vs user: net A - B (pp) |
| `\PoneForcedMemoryVsUserNetLo` | \ensuremath{-}91.1 | P1 forced memory vs user: net A - B (pp), lower 95% CI bound |
| `\PoneForcedMemoryVsUserNetHi` | \ensuremath{-}78.3 | P1 forced memory vs user: net A - B (pp), upper 95% CI bound |
| `\PoneForcedMemoryVsUserNetCI` | [\ensuremath{-}91.1, \ensuremath{-}78.3] | P1 forced memory vs user: net A - B (pp), 95% CI |
| `\PoneForcedMemoryVsUserNetN` | 360 | P1 forced memory vs user: net A - B (pp), n |
| `\PoneForcedMemoryVsUserNetP` | \ensuremath{<}0.001 | P1 forced memory vs user: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsDocumentFollowA` | 3.1 | P1 forced memory vs document: % follows memory |
| `\PoneForcedMemoryVsDocumentFollowALo` | 0.8 | P1 forced memory vs document: % follows memory, lower 95% CI bound |
| `\PoneForcedMemoryVsDocumentFollowAHi` | 6.1 | P1 forced memory vs document: % follows memory, upper 95% CI bound |
| `\PoneForcedMemoryVsDocumentFollowACI` | [0.8, 6.1] | P1 forced memory vs document: % follows memory, 95% CI |
| `\PoneForcedMemoryVsDocumentFollowAN` | 360 | P1 forced memory vs document: % follows memory, n |
| `\PoneForcedMemoryVsDocumentFollowAP` | n/a | P1 forced memory vs document: % follows memory, two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsDocumentFollowB` | 96.7 | P1 forced memory vs document: % follows document |
| `\PoneForcedMemoryVsDocumentFollowBLo` | 93.6 | P1 forced memory vs document: % follows document, lower 95% CI bound |
| `\PoneForcedMemoryVsDocumentFollowBHi` | 98.9 | P1 forced memory vs document: % follows document, upper 95% CI bound |
| `\PoneForcedMemoryVsDocumentFollowBCI` | [93.6, 98.9] | P1 forced memory vs document: % follows document, 95% CI |
| `\PoneForcedMemoryVsDocumentFollowBN` | 360 | P1 forced memory vs document: % follows document, n |
| `\PoneForcedMemoryVsDocumentFollowBP` | n/a | P1 forced memory vs document: % follows document, two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsDocumentEsc` | 0.0 | P1 forced memory vs document: % flags conflict |
| `\PoneForcedMemoryVsDocumentEscLo` | 0.0 | P1 forced memory vs document: % flags conflict, lower 95% CI bound |
| `\PoneForcedMemoryVsDocumentEscHi` | 1.0 | P1 forced memory vs document: % flags conflict, upper 95% CI bound |
| `\PoneForcedMemoryVsDocumentEscCI` | [0.0, 1.0] | P1 forced memory vs document: % flags conflict, 95% CI |
| `\PoneForcedMemoryVsDocumentEscN` | 360 | P1 forced memory vs document: % flags conflict, n |
| `\PoneForcedMemoryVsDocumentEscP` | n/a | P1 forced memory vs document: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PoneForcedMemoryVsDocumentNet` | \ensuremath{-}93.6 | P1 forced memory vs document: net A - B (pp) |
| `\PoneForcedMemoryVsDocumentNetLo` | \ensuremath{-}98.1 | P1 forced memory vs document: net A - B (pp), lower 95% CI bound |
| `\PoneForcedMemoryVsDocumentNetHi` | \ensuremath{-}87.8 | P1 forced memory vs document: net A - B (pp), upper 95% CI bound |
| `\PoneForcedMemoryVsDocumentNetCI` | [\ensuremath{-}98.1, \ensuremath{-}87.8] | P1 forced memory vs document: net A - B (pp), 95% CI |
| `\PoneForcedMemoryVsDocumentNetN` | 360 | P1 forced memory vs document: net A - B (pp), n |
| `\PoneForcedMemoryVsDocumentNetP` | \ensuremath{<}0.001 | P1 forced memory vs document: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsToolFollowA` | 6.1 | P1 stale memory vs tool: % follows memory |
| `\PoneStaleMemoryVsToolFollowALo` | 3.3 | P1 stale memory vs tool: % follows memory, lower 95% CI bound |
| `\PoneStaleMemoryVsToolFollowAHi` | 9.4 | P1 stale memory vs tool: % follows memory, upper 95% CI bound |
| `\PoneStaleMemoryVsToolFollowACI` | [3.3, 9.4] | P1 stale memory vs tool: % follows memory, 95% CI |
| `\PoneStaleMemoryVsToolFollowAN` | 360 | P1 stale memory vs tool: % follows memory, n |
| `\PoneStaleMemoryVsToolFollowAP` | n/a | P1 stale memory vs tool: % follows memory, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsToolFollowB` | 20.3 | P1 stale memory vs tool: % follows tool |
| `\PoneStaleMemoryVsToolFollowBLo` | 13.3 | P1 stale memory vs tool: % follows tool, lower 95% CI bound |
| `\PoneStaleMemoryVsToolFollowBHi` | 27.5 | P1 stale memory vs tool: % follows tool, upper 95% CI bound |
| `\PoneStaleMemoryVsToolFollowBCI` | [13.3, 27.5] | P1 stale memory vs tool: % follows tool, 95% CI |
| `\PoneStaleMemoryVsToolFollowBN` | 360 | P1 stale memory vs tool: % follows tool, n |
| `\PoneStaleMemoryVsToolFollowBP` | n/a | P1 stale memory vs tool: % follows tool, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsToolEsc` | 72.8 | P1 stale memory vs tool: % flags conflict |
| `\PoneStaleMemoryVsToolEscLo` | 65.3 | P1 stale memory vs tool: % flags conflict, lower 95% CI bound |
| `\PoneStaleMemoryVsToolEscHi` | 79.4 | P1 stale memory vs tool: % flags conflict, upper 95% CI bound |
| `\PoneStaleMemoryVsToolEscCI` | [65.3, 79.4] | P1 stale memory vs tool: % flags conflict, 95% CI |
| `\PoneStaleMemoryVsToolEscN` | 360 | P1 stale memory vs tool: % flags conflict, n |
| `\PoneStaleMemoryVsToolEscP` | n/a | P1 stale memory vs tool: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsToolNet` | \ensuremath{-}14.2 | P1 stale memory vs tool: net A - B (pp) |
| `\PoneStaleMemoryVsToolNetLo` | \ensuremath{-}22.8 | P1 stale memory vs tool: net A - B (pp), lower 95% CI bound |
| `\PoneStaleMemoryVsToolNetHi` | \ensuremath{-}5.8 | P1 stale memory vs tool: net A - B (pp), upper 95% CI bound |
| `\PoneStaleMemoryVsToolNetCI` | [\ensuremath{-}22.8, \ensuremath{-}5.8] | P1 stale memory vs tool: net A - B (pp), 95% CI |
| `\PoneStaleMemoryVsToolNetN` | 360 | P1 stale memory vs tool: net A - B (pp), n |
| `\PoneStaleMemoryVsToolNetP` | 0.002 | P1 stale memory vs tool: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsUserFollowA` | 11.1 | P1 stale memory vs user: % follows memory |
| `\PoneStaleMemoryVsUserFollowALo` | 7.2 | P1 stale memory vs user: % follows memory, lower 95% CI bound |
| `\PoneStaleMemoryVsUserFollowAHi` | 15.3 | P1 stale memory vs user: % follows memory, upper 95% CI bound |
| `\PoneStaleMemoryVsUserFollowACI` | [7.2, 15.3] | P1 stale memory vs user: % follows memory, 95% CI |
| `\PoneStaleMemoryVsUserFollowAN` | 360 | P1 stale memory vs user: % follows memory, n |
| `\PoneStaleMemoryVsUserFollowAP` | n/a | P1 stale memory vs user: % follows memory, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsUserFollowB` | 15.8 | P1 stale memory vs user: % follows user |
| `\PoneStaleMemoryVsUserFollowBLo` | 10.0 | P1 stale memory vs user: % follows user, lower 95% CI bound |
| `\PoneStaleMemoryVsUserFollowBHi` | 21.9 | P1 stale memory vs user: % follows user, upper 95% CI bound |
| `\PoneStaleMemoryVsUserFollowBCI` | [10.0, 21.9] | P1 stale memory vs user: % follows user, 95% CI |
| `\PoneStaleMemoryVsUserFollowBN` | 360 | P1 stale memory vs user: % follows user, n |
| `\PoneStaleMemoryVsUserFollowBP` | n/a | P1 stale memory vs user: % follows user, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsUserEsc` | 73.1 | P1 stale memory vs user: % flags conflict |
| `\PoneStaleMemoryVsUserEscLo` | 65.8 | P1 stale memory vs user: % flags conflict, lower 95% CI bound |
| `\PoneStaleMemoryVsUserEscHi` | 79.7 | P1 stale memory vs user: % flags conflict, upper 95% CI bound |
| `\PoneStaleMemoryVsUserEscCI` | [65.8, 79.7] | P1 stale memory vs user: % flags conflict, 95% CI |
| `\PoneStaleMemoryVsUserEscN` | 360 | P1 stale memory vs user: % flags conflict, n |
| `\PoneStaleMemoryVsUserEscP` | n/a | P1 stale memory vs user: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsUserNet` | \ensuremath{-}4.7 | P1 stale memory vs user: net A - B (pp) |
| `\PoneStaleMemoryVsUserNetLo` | \ensuremath{-}12.2 | P1 stale memory vs user: net A - B (pp), lower 95% CI bound |
| `\PoneStaleMemoryVsUserNetHi` | 2.2 | P1 stale memory vs user: net A - B (pp), upper 95% CI bound |
| `\PoneStaleMemoryVsUserNetCI` | [\ensuremath{-}12.2, 2.2] | P1 stale memory vs user: net A - B (pp), 95% CI |
| `\PoneStaleMemoryVsUserNetN` | 360 | P1 stale memory vs user: net A - B (pp), n |
| `\PoneStaleMemoryVsUserNetP` | 0.218 | P1 stale memory vs user: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsDocumentFollowA` | 2.2 | P1 stale memory vs document: % follows memory |
| `\PoneStaleMemoryVsDocumentFollowALo` | 0.6 | P1 stale memory vs document: % follows memory, lower 95% CI bound |
| `\PoneStaleMemoryVsDocumentFollowAHi` | 4.4 | P1 stale memory vs document: % follows memory, upper 95% CI bound |
| `\PoneStaleMemoryVsDocumentFollowACI` | [0.6, 4.4] | P1 stale memory vs document: % follows memory, 95% CI |
| `\PoneStaleMemoryVsDocumentFollowAN` | 360 | P1 stale memory vs document: % follows memory, n |
| `\PoneStaleMemoryVsDocumentFollowAP` | n/a | P1 stale memory vs document: % follows memory, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsDocumentFollowB` | 20.3 | P1 stale memory vs document: % follows document |
| `\PoneStaleMemoryVsDocumentFollowBLo` | 14.2 | P1 stale memory vs document: % follows document, lower 95% CI bound |
| `\PoneStaleMemoryVsDocumentFollowBHi` | 26.4 | P1 stale memory vs document: % follows document, upper 95% CI bound |
| `\PoneStaleMemoryVsDocumentFollowBCI` | [14.2, 26.4] | P1 stale memory vs document: % follows document, 95% CI |
| `\PoneStaleMemoryVsDocumentFollowBN` | 360 | P1 stale memory vs document: % follows document, n |
| `\PoneStaleMemoryVsDocumentFollowBP` | n/a | P1 stale memory vs document: % follows document, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsDocumentEsc` | 77.5 | P1 stale memory vs document: % flags conflict |
| `\PoneStaleMemoryVsDocumentEscLo` | 70.3 | P1 stale memory vs document: % flags conflict, lower 95% CI bound |
| `\PoneStaleMemoryVsDocumentEscHi` | 84.7 | P1 stale memory vs document: % flags conflict, upper 95% CI bound |
| `\PoneStaleMemoryVsDocumentEscCI` | [70.3, 84.7] | P1 stale memory vs document: % flags conflict, 95% CI |
| `\PoneStaleMemoryVsDocumentEscN` | 360 | P1 stale memory vs document: % flags conflict, n |
| `\PoneStaleMemoryVsDocumentEscP` | n/a | P1 stale memory vs document: % flags conflict, two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleMemoryVsDocumentNet` | \ensuremath{-}18.1 | P1 stale memory vs document: net A - B (pp) |
| `\PoneStaleMemoryVsDocumentNetLo` | \ensuremath{-}24.2 | P1 stale memory vs document: net A - B (pp), lower 95% CI bound |
| `\PoneStaleMemoryVsDocumentNetHi` | \ensuremath{-}12.5 | P1 stale memory vs document: net A - B (pp), upper 95% CI bound |
| `\PoneStaleMemoryVsDocumentNetCI` | [\ensuremath{-}24.2, \ensuremath{-}12.5] | P1 stale memory vs document: net A - B (pp), 95% CI |
| `\PoneStaleMemoryVsDocumentNetN` | 360 | P1 stale memory vs document: net A - B (pp), n |
| `\PoneStaleMemoryVsDocumentNetP` | \ensuremath{<}0.001 | P1 stale memory vs document: net A - B (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneBTMemory` | \ensuremath{-}2.49 | P1 Bradley-Terry ability of memory (log-odds, centred) |
| `\PoneBTMemoryLo` | \ensuremath{-}2.94 | P1 Bradley-Terry ability of memory (log-odds, centred), lower 95% CI bound |
| `\PoneBTMemoryHi` | \ensuremath{-}2.20 | P1 Bradley-Terry ability of memory (log-odds, centred), upper 95% CI bound |
| `\PoneBTMemoryCI` | [\ensuremath{-}2.94, \ensuremath{-}2.20] | P1 Bradley-Terry ability of memory (log-odds, centred), 95% CI |
| `\PoneBTMemoryN` | 1{,}373 | P1 Bradley-Terry ability of memory (log-odds, centred), n |
| `\PoneBTMemoryP` | n/a | P1 Bradley-Terry ability of memory (log-odds, centred), two-sided bootstrap p (n/a if not tested) |
| `\PoneBTTool` | 1.43 | P1 Bradley-Terry ability of tool (log-odds, centred) |
| `\PoneBTToolLo` | 1.14 | P1 Bradley-Terry ability of tool (log-odds, centred), lower 95% CI bound |
| `\PoneBTToolHi` | 1.74 | P1 Bradley-Terry ability of tool (log-odds, centred), upper 95% CI bound |
| `\PoneBTToolCI` | [1.14, 1.74] | P1 Bradley-Terry ability of tool (log-odds, centred), 95% CI |
| `\PoneBTToolN` | 561 | P1 Bradley-Terry ability of tool (log-odds, centred), n |
| `\PoneBTToolP` | n/a | P1 Bradley-Terry ability of tool (log-odds, centred), two-sided bootstrap p (n/a if not tested) |
| `\PoneBTWeb` | \ensuremath{-}2.00 | P1 Bradley-Terry ability of web (log-odds, centred) |
| `\PoneBTWebLo` | \ensuremath{-}2.51 | P1 Bradley-Terry ability of web (log-odds, centred), lower 95% CI bound |
| `\PoneBTWebHi` | \ensuremath{-}1.62 | P1 Bradley-Terry ability of web (log-odds, centred), upper 95% CI bound |
| `\PoneBTWebCI` | [\ensuremath{-}2.51, \ensuremath{-}1.62] | P1 Bradley-Terry ability of web (log-odds, centred), 95% CI |
| `\PoneBTWebN` | 242 | P1 Bradley-Terry ability of web (log-odds, centred), n |
| `\PoneBTWebP` | n/a | P1 Bradley-Terry ability of web (log-odds, centred), two-sided bootstrap p (n/a if not tested) |
| `\PoneBTUser` | 1.76 | P1 Bradley-Terry ability of user (log-odds, centred) |
| `\PoneBTUserLo` | 1.51 | P1 Bradley-Terry ability of user (log-odds, centred), lower 95% CI bound |
| `\PoneBTUserHi` | 2.12 | P1 Bradley-Terry ability of user (log-odds, centred), upper 95% CI bound |
| `\PoneBTUserCI` | [1.51, 2.12] | P1 Bradley-Terry ability of user (log-odds, centred), 95% CI |
| `\PoneBTUserN` | 733 | P1 Bradley-Terry ability of user (log-odds, centred), n |
| `\PoneBTUserP` | n/a | P1 Bradley-Terry ability of user (log-odds, centred), two-sided bootstrap p (n/a if not tested) |
| `\PoneBTAgent` | \ensuremath{-}0.34 | P1 Bradley-Terry ability of agent (log-odds, centred) |
| `\PoneBTAgentLo` | \ensuremath{-}0.85 | P1 Bradley-Terry ability of agent (log-odds, centred), lower 95% CI bound |
| `\PoneBTAgentHi` | 0.16 | P1 Bradley-Terry ability of agent (log-odds, centred), upper 95% CI bound |
| `\PoneBTAgentCI` | [\ensuremath{-}0.85, 0.16] | P1 Bradley-Terry ability of agent (log-odds, centred), 95% CI |
| `\PoneBTAgentN` | 273 | P1 Bradley-Terry ability of agent (log-odds, centred), n |
| `\PoneBTAgentP` | n/a | P1 Bradley-Terry ability of agent (log-odds, centred), two-sided bootstrap p (n/a if not tested) |
| `\PoneBTUnattributed` | 0.53 | P1 Bradley-Terry ability of unattributed (log-odds, centred) |
| `\PoneBTUnattributedLo` | 0.31 | P1 Bradley-Terry ability of unattributed (log-odds, centred), lower 95% CI bound |
| `\PoneBTUnattributedHi` | 0.79 | P1 Bradley-Terry ability of unattributed (log-odds, centred), upper 95% CI bound |
| `\PoneBTUnattributedCI` | [0.31, 0.79] | P1 Bradley-Terry ability of unattributed (log-odds, centred), 95% CI |
| `\PoneBTUnattributedN` | 364 | P1 Bradley-Terry ability of unattributed (log-odds, centred), n |
| `\PoneBTUnattributedP` | n/a | P1 Bradley-Terry ability of unattributed (log-odds, centred), two-sided bootstrap p (n/a if not tested) |
| `\PoneBTDocument` | 1.10 | P1 Bradley-Terry ability of document (log-odds, centred) |
| `\PoneBTDocumentLo` | 0.69 | P1 Bradley-Terry ability of document (log-odds, centred), lower 95% CI bound |
| `\PoneBTDocumentHi` | 1.64 | P1 Bradley-Terry ability of document (log-odds, centred), upper 95% CI bound |
| `\PoneBTDocumentCI` | [0.69, 1.64] | P1 Bradley-Terry ability of document (log-odds, centred), 95% CI |
| `\PoneBTDocumentN` | 478 | P1 Bradley-Terry ability of document (log-odds, centred), n |
| `\PoneBTDocumentP` | n/a | P1 Bradley-Terry ability of document (log-odds, centred), two-sided bootstrap p (n/a if not tested) |
| `\PoneFramingMemoryVsTool` | 3.9 | P1 framing: change in % following memory when framed first-person, vs tool (pp) |
| `\PoneFramingMemoryVsToolLo` | 1.9 | P1 framing: change in % following memory when framed first-person, vs tool (pp), lower 95% CI bound |
| `\PoneFramingMemoryVsToolHi` | 6.1 | P1 framing: change in % following memory when framed first-person, vs tool (pp), upper 95% CI bound |
| `\PoneFramingMemoryVsToolCI` | [1.9, 6.1] | P1 framing: change in % following memory when framed first-person, vs tool (pp), 95% CI |
| `\PoneFramingMemoryVsToolN` | 720 | P1 framing: change in % following memory when framed first-person, vs tool (pp), n |
| `\PoneFramingMemoryVsToolP` | \ensuremath{<}0.001 | P1 framing: change in % following memory when framed first-person, vs tool (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneFramingEscMemoryVsTool` | 8.2 | P1 framing: change in % flagging the conflict when memory is framed first-person, vs tool (pp) |
| `\PoneFramingEscMemoryVsToolLo` | 5.3 | P1 framing: change in % flagging the conflict when memory is framed first-person, vs tool (pp), lower 95% CI bound |
| `\PoneFramingEscMemoryVsToolHi` | 11.1 | P1 framing: change in % flagging the conflict when memory is framed first-person, vs tool (pp), upper 95% CI bound |
| `\PoneFramingEscMemoryVsToolCI` | [5.3, 11.1] | P1 framing: change in % flagging the conflict when memory is framed first-person, vs tool (pp), 95% CI |
| `\PoneFramingEscMemoryVsToolN` | 720 | P1 framing: change in % flagging the conflict when memory is framed first-person, vs tool (pp), n |
| `\PoneFramingEscMemoryVsToolP` | \ensuremath{<}0.001 | P1 framing: change in % flagging the conflict when memory is framed first-person, vs tool (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneFramingMemoryVsDocument` | 4.6 | P1 framing: change in % following memory when framed first-person, vs document (pp) |
| `\PoneFramingMemoryVsDocumentLo` | 2.5 | P1 framing: change in % following memory when framed first-person, vs document (pp), lower 95% CI bound |
| `\PoneFramingMemoryVsDocumentHi` | 6.9 | P1 framing: change in % following memory when framed first-person, vs document (pp), upper 95% CI bound |
| `\PoneFramingMemoryVsDocumentCI` | [2.5, 6.9] | P1 framing: change in % following memory when framed first-person, vs document (pp), 95% CI |
| `\PoneFramingMemoryVsDocumentN` | 720 | P1 framing: change in % following memory when framed first-person, vs document (pp), n |
| `\PoneFramingMemoryVsDocumentP` | \ensuremath{<}0.001 | P1 framing: change in % following memory when framed first-person, vs document (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneFramingEscMemoryVsDocument` | 6.7 | P1 framing: change in % flagging the conflict when memory is framed first-person, vs document (pp) |
| `\PoneFramingEscMemoryVsDocumentLo` | 3.8 | P1 framing: change in % flagging the conflict when memory is framed first-person, vs document (pp), lower 95% CI bound |
| `\PoneFramingEscMemoryVsDocumentHi` | 9.7 | P1 framing: change in % flagging the conflict when memory is framed first-person, vs document (pp), upper 95% CI bound |
| `\PoneFramingEscMemoryVsDocumentCI` | [3.8, 9.7] | P1 framing: change in % flagging the conflict when memory is framed first-person, vs document (pp), 95% CI |
| `\PoneFramingEscMemoryVsDocumentN` | 720 | P1 framing: change in % flagging the conflict when memory is framed first-person, vs document (pp), n |
| `\PoneFramingEscMemoryVsDocumentP` | \ensuremath{<}0.001 | P1 framing: change in % flagging the conflict when memory is framed first-person, vs document (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneFramingUserVsTool` | 10.6 | P1 framing: change in % following user when framed first-person, vs tool (pp) |
| `\PoneFramingUserVsToolLo` | 6.7 | P1 framing: change in % following user when framed first-person, vs tool (pp), lower 95% CI bound |
| `\PoneFramingUserVsToolHi` | 14.3 | P1 framing: change in % following user when framed first-person, vs tool (pp), upper 95% CI bound |
| `\PoneFramingUserVsToolCI` | [6.7, 14.3] | P1 framing: change in % following user when framed first-person, vs tool (pp), 95% CI |
| `\PoneFramingUserVsToolN` | 720 | P1 framing: change in % following user when framed first-person, vs tool (pp), n |
| `\PoneFramingUserVsToolP` | \ensuremath{<}0.001 | P1 framing: change in % following user when framed first-person, vs tool (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneFramingEscUserVsTool` | \ensuremath{-}4.3 | P1 framing: change in % flagging the conflict when user is framed first-person, vs tool (pp) |
| `\PoneFramingEscUserVsToolLo` | \ensuremath{-}7.4 | P1 framing: change in % flagging the conflict when user is framed first-person, vs tool (pp), lower 95% CI bound |
| `\PoneFramingEscUserVsToolHi` | \ensuremath{-}1.2 | P1 framing: change in % flagging the conflict when user is framed first-person, vs tool (pp), upper 95% CI bound |
| `\PoneFramingEscUserVsToolCI` | [\ensuremath{-}7.4, \ensuremath{-}1.2] | P1 framing: change in % flagging the conflict when user is framed first-person, vs tool (pp), 95% CI |
| `\PoneFramingEscUserVsToolN` | 720 | P1 framing: change in % flagging the conflict when user is framed first-person, vs tool (pp), n |
| `\PoneFramingEscUserVsToolP` | 0.007 | P1 framing: change in % flagging the conflict when user is framed first-person, vs tool (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneFramingUserVsDocument` | 10.3 | P1 framing: change in % following user when framed first-person, vs document (pp) |
| `\PoneFramingUserVsDocumentLo` | 7.2 | P1 framing: change in % following user when framed first-person, vs document (pp), lower 95% CI bound |
| `\PoneFramingUserVsDocumentHi` | 13.5 | P1 framing: change in % following user when framed first-person, vs document (pp), upper 95% CI bound |
| `\PoneFramingUserVsDocumentCI` | [7.2, 13.5] | P1 framing: change in % following user when framed first-person, vs document (pp), 95% CI |
| `\PoneFramingUserVsDocumentN` | 720 | P1 framing: change in % following user when framed first-person, vs document (pp), n |
| `\PoneFramingUserVsDocumentP` | \ensuremath{<}0.001 | P1 framing: change in % following user when framed first-person, vs document (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneFramingEscUserVsDocument` | \ensuremath{-}7.1 | P1 framing: change in % flagging the conflict when user is framed first-person, vs document (pp) |
| `\PoneFramingEscUserVsDocumentLo` | \ensuremath{-}10.0 | P1 framing: change in % flagging the conflict when user is framed first-person, vs document (pp), lower 95% CI bound |
| `\PoneFramingEscUserVsDocumentHi` | \ensuremath{-}4.3 | P1 framing: change in % flagging the conflict when user is framed first-person, vs document (pp), upper 95% CI bound |
| `\PoneFramingEscUserVsDocumentCI` | [\ensuremath{-}10.0, \ensuremath{-}4.3] | P1 framing: change in % flagging the conflict when user is framed first-person, vs document (pp), 95% CI |
| `\PoneFramingEscUserVsDocumentN` | 720 | P1 framing: change in % flagging the conflict when user is framed first-person, vs document (pp), n |
| `\PoneFramingEscUserVsDocumentP` | \ensuremath{<}0.001 | P1 framing: change in % flagging the conflict when user is framed first-person, vs document (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneFramingMemoryBoth` | 4.2 | P1 framing effect for memory, both trials pooled (pp) |
| `\PoneFramingMemoryBothLo` | 2.5 | P1 framing effect for memory, both trials pooled (pp), lower 95% CI bound |
| `\PoneFramingMemoryBothHi` | 6.3 | P1 framing effect for memory, both trials pooled (pp), upper 95% CI bound |
| `\PoneFramingMemoryBothCI` | [2.5, 6.3] | P1 framing effect for memory, both trials pooled (pp), 95% CI |
| `\PoneFramingMemoryBothN` | 1{,}440 | P1 framing effect for memory, both trials pooled (pp), n |
| `\PoneFramingMemoryBothP` | \ensuremath{<}0.001 | P1 framing effect for memory, both trials pooled (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneFramingUserBoth` | 10.4 | P1 framing effect for user, both trials pooled (pp) |
| `\PoneFramingUserBothLo` | 7.5 | P1 framing effect for user, both trials pooled (pp), lower 95% CI bound |
| `\PoneFramingUserBothHi` | 13.5 | P1 framing effect for user, both trials pooled (pp), upper 95% CI bound |
| `\PoneFramingUserBothCI` | [7.5, 13.5] | P1 framing effect for user, both trials pooled (pp), 95% CI |
| `\PoneFramingUserBothN` | 1{,}440 | P1 framing effect for user, both trials pooled (pp), n |
| `\PoneFramingUserBothP` | \ensuremath{<}0.001 | P1 framing effect for user, both trials pooled (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneTurnVsTool` | \ensuremath{-}0.3 | P1 turn - labelled memory: change in % following memory vs tool (pp) |
| `\PoneTurnVsToolLo` | \ensuremath{-}0.8 | P1 turn - labelled memory: change in % following memory vs tool (pp), lower 95% CI bound |
| `\PoneTurnVsToolHi` | 0.0 | P1 turn - labelled memory: change in % following memory vs tool (pp), upper 95% CI bound |
| `\PoneTurnVsToolCI` | [\ensuremath{-}0.8, 0.0] | P1 turn - labelled memory: change in % following memory vs tool (pp), 95% CI |
| `\PoneTurnVsToolN` | 360 | P1 turn - labelled memory: change in % following memory vs tool (pp), n |
| `\PoneTurnVsToolP` | 0.768 | P1 turn - labelled memory: change in % following memory vs tool (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneTurnVsDocument` | \ensuremath{-}0.6 | P1 turn - labelled memory: change in % following memory vs document (pp) |
| `\PoneTurnVsDocumentLo` | \ensuremath{-}1.4 | P1 turn - labelled memory: change in % following memory vs document (pp), lower 95% CI bound |
| `\PoneTurnVsDocumentHi` | 0.0 | P1 turn - labelled memory: change in % following memory vs document (pp), upper 95% CI bound |
| `\PoneTurnVsDocumentCI` | [\ensuremath{-}1.4, 0.0] | P1 turn - labelled memory: change in % following memory vs document (pp), 95% CI |
| `\PoneTurnVsDocumentN` | 360 | P1 turn - labelled memory: change in % following memory vs document (pp), n |
| `\PoneTurnVsDocumentP` | 0.253 | P1 turn - labelled memory: change in % following memory vs document (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsToolDiffMem` | 5.8 | P1 stale - unmarked: change in % following memory vs tool (pp) |
| `\PoneStaleVsToolDiffMemLo` | 3.3 | P1 stale - unmarked: change in % following memory vs tool (pp), lower 95% CI bound |
| `\PoneStaleVsToolDiffMemHi` | 8.9 | P1 stale - unmarked: change in % following memory vs tool (pp), upper 95% CI bound |
| `\PoneStaleVsToolDiffMemCI` | [3.3, 8.9] | P1 stale - unmarked: change in % following memory vs tool (pp), 95% CI |
| `\PoneStaleVsToolDiffMemN` | 360 | P1 stale - unmarked: change in % following memory vs tool (pp), n |
| `\PoneStaleVsToolDiffMemP` | \ensuremath{<}0.001 | P1 stale - unmarked: change in % following memory vs tool (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsToolDiffOther` | \ensuremath{-}15.6 | P1 stale - unmarked: change in % following tool (pp) |
| `\PoneStaleVsToolDiffOtherLo` | \ensuremath{-}20.0 | P1 stale - unmarked: change in % following tool (pp), lower 95% CI bound |
| `\PoneStaleVsToolDiffOtherHi` | \ensuremath{-}11.4 | P1 stale - unmarked: change in % following tool (pp), upper 95% CI bound |
| `\PoneStaleVsToolDiffOtherCI` | [\ensuremath{-}20.0, \ensuremath{-}11.4] | P1 stale - unmarked: change in % following tool (pp), 95% CI |
| `\PoneStaleVsToolDiffOtherN` | 360 | P1 stale - unmarked: change in % following tool (pp), n |
| `\PoneStaleVsToolDiffOtherP` | \ensuremath{<}0.001 | P1 stale - unmarked: change in % following tool (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsToolDiffEsc` | 9.2 | P1 stale - unmarked: change in % flagging the conflict vs tool (pp) |
| `\PoneStaleVsToolDiffEscLo` | 4.7 | P1 stale - unmarked: change in % flagging the conflict vs tool (pp), lower 95% CI bound |
| `\PoneStaleVsToolDiffEscHi` | 13.9 | P1 stale - unmarked: change in % flagging the conflict vs tool (pp), upper 95% CI bound |
| `\PoneStaleVsToolDiffEscCI` | [4.7, 13.9] | P1 stale - unmarked: change in % flagging the conflict vs tool (pp), 95% CI |
| `\PoneStaleVsToolDiffEscN` | 360 | P1 stale - unmarked: change in % flagging the conflict vs tool (pp), n |
| `\PoneStaleVsToolDiffEscP` | 0.002 | P1 stale - unmarked: change in % flagging the conflict vs tool (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsToolNetUnmarked` | \ensuremath{-}35.6 | P1 unmarked trials on the same items: net memory - tool (pp) |
| `\PoneStaleVsToolNetUnmarkedLo` | \ensuremath{-}42.8 | P1 unmarked trials on the same items: net memory - tool (pp), lower 95% CI bound |
| `\PoneStaleVsToolNetUnmarkedHi` | \ensuremath{-}28.3 | P1 unmarked trials on the same items: net memory - tool (pp), upper 95% CI bound |
| `\PoneStaleVsToolNetUnmarkedCI` | [\ensuremath{-}42.8, \ensuremath{-}28.3] | P1 unmarked trials on the same items: net memory - tool (pp), 95% CI |
| `\PoneStaleVsToolNetUnmarkedN` | 360 | P1 unmarked trials on the same items: net memory - tool (pp), n |
| `\PoneStaleVsToolNetUnmarkedP` | \ensuremath{<}0.001 | P1 unmarked trials on the same items: net memory - tool (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsToolNet` | \ensuremath{-}14.2 | P1 stale: net memory - tool (pp) |
| `\PoneStaleVsToolNetLo` | \ensuremath{-}23.1 | P1 stale: net memory - tool (pp), lower 95% CI bound |
| `\PoneStaleVsToolNetHi` | \ensuremath{-}5.8 | P1 stale: net memory - tool (pp), upper 95% CI bound |
| `\PoneStaleVsToolNetCI` | [\ensuremath{-}23.1, \ensuremath{-}5.8] | P1 stale: net memory - tool (pp), 95% CI |
| `\PoneStaleVsToolNetN` | 360 | P1 stale: net memory - tool (pp), n |
| `\PoneStaleVsToolNetP` | \ensuremath{<}0.001 | P1 stale: net memory - tool (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsDocumentDiffMem` | 1.7 | P1 stale - unmarked: change in % following memory vs document (pp) |
| `\PoneStaleVsDocumentDiffMemLo` | 0.0 | P1 stale - unmarked: change in % following memory vs document (pp), lower 95% CI bound |
| `\PoneStaleVsDocumentDiffMemHi` | 3.6 | P1 stale - unmarked: change in % following memory vs document (pp), upper 95% CI bound |
| `\PoneStaleVsDocumentDiffMemCI` | [0.0, 3.6] | P1 stale - unmarked: change in % following memory vs document (pp), 95% CI |
| `\PoneStaleVsDocumentDiffMemN` | 360 | P1 stale - unmarked: change in % following memory vs document (pp), n |
| `\PoneStaleVsDocumentDiffMemP` | 0.056 | P1 stale - unmarked: change in % following memory vs document (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsDocumentDiffOther` | \ensuremath{-}10.8 | P1 stale - unmarked: change in % following document (pp) |
| `\PoneStaleVsDocumentDiffOtherLo` | \ensuremath{-}15.3 | P1 stale - unmarked: change in % following document (pp), lower 95% CI bound |
| `\PoneStaleVsDocumentDiffOtherHi` | \ensuremath{-}6.9 | P1 stale - unmarked: change in % following document (pp), upper 95% CI bound |
| `\PoneStaleVsDocumentDiffOtherCI` | [\ensuremath{-}15.3, \ensuremath{-}6.9] | P1 stale - unmarked: change in % following document (pp), 95% CI |
| `\PoneStaleVsDocumentDiffOtherN` | 360 | P1 stale - unmarked: change in % following document (pp), n |
| `\PoneStaleVsDocumentDiffOtherP` | \ensuremath{<}0.001 | P1 stale - unmarked: change in % following document (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsDocumentDiffEsc` | 9.4 | P1 stale - unmarked: change in % flagging the conflict vs document (pp) |
| `\PoneStaleVsDocumentDiffEscLo` | 5.6 | P1 stale - unmarked: change in % flagging the conflict vs document (pp), lower 95% CI bound |
| `\PoneStaleVsDocumentDiffEscHi` | 13.3 | P1 stale - unmarked: change in % flagging the conflict vs document (pp), upper 95% CI bound |
| `\PoneStaleVsDocumentDiffEscCI` | [5.6, 13.3] | P1 stale - unmarked: change in % flagging the conflict vs document (pp), 95% CI |
| `\PoneStaleVsDocumentDiffEscN` | 360 | P1 stale - unmarked: change in % flagging the conflict vs document (pp), n |
| `\PoneStaleVsDocumentDiffEscP` | \ensuremath{<}0.001 | P1 stale - unmarked: change in % flagging the conflict vs document (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsDocumentNetUnmarked` | \ensuremath{-}30.6 | P1 unmarked trials on the same items: net memory - document (pp) |
| `\PoneStaleVsDocumentNetUnmarkedLo` | \ensuremath{-}38.6 | P1 unmarked trials on the same items: net memory - document (pp), lower 95% CI bound |
| `\PoneStaleVsDocumentNetUnmarkedHi` | \ensuremath{-}22.8 | P1 unmarked trials on the same items: net memory - document (pp), upper 95% CI bound |
| `\PoneStaleVsDocumentNetUnmarkedCI` | [\ensuremath{-}38.6, \ensuremath{-}22.8] | P1 unmarked trials on the same items: net memory - document (pp), 95% CI |
| `\PoneStaleVsDocumentNetUnmarkedN` | 360 | P1 unmarked trials on the same items: net memory - document (pp), n |
| `\PoneStaleVsDocumentNetUnmarkedP` | \ensuremath{<}0.001 | P1 unmarked trials on the same items: net memory - document (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsDocumentNet` | \ensuremath{-}18.1 | P1 stale: net memory - document (pp) |
| `\PoneStaleVsDocumentNetLo` | \ensuremath{-}24.2 | P1 stale: net memory - document (pp), lower 95% CI bound |
| `\PoneStaleVsDocumentNetHi` | \ensuremath{-}11.9 | P1 stale: net memory - document (pp), upper 95% CI bound |
| `\PoneStaleVsDocumentNetCI` | [\ensuremath{-}24.2, \ensuremath{-}11.9] | P1 stale: net memory - document (pp), 95% CI |
| `\PoneStaleVsDocumentNetN` | 360 | P1 stale: net memory - document (pp), n |
| `\PoneStaleVsDocumentNetP` | \ensuremath{<}0.001 | P1 stale: net memory - document (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsUserDiffMem` | 10.8 | P1 stale - unmarked: change in % following memory vs user (pp) |
| `\PoneStaleVsUserDiffMemLo` | 7.2 | P1 stale - unmarked: change in % following memory vs user (pp), lower 95% CI bound |
| `\PoneStaleVsUserDiffMemHi` | 15.0 | P1 stale - unmarked: change in % following memory vs user (pp), upper 95% CI bound |
| `\PoneStaleVsUserDiffMemCI` | [7.2, 15.0] | P1 stale - unmarked: change in % following memory vs user (pp), 95% CI |
| `\PoneStaleVsUserDiffMemN` | 360 | P1 stale - unmarked: change in % following memory vs user (pp), n |
| `\PoneStaleVsUserDiffMemP` | \ensuremath{<}0.001 | P1 stale - unmarked: change in % following memory vs user (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsUserDiffOther` | \ensuremath{-}24.7 | P1 stale - unmarked: change in % following user (pp) |
| `\PoneStaleVsUserDiffOtherLo` | \ensuremath{-}31.4 | P1 stale - unmarked: change in % following user (pp), lower 95% CI bound |
| `\PoneStaleVsUserDiffOtherHi` | \ensuremath{-}18.6 | P1 stale - unmarked: change in % following user (pp), upper 95% CI bound |
| `\PoneStaleVsUserDiffOtherCI` | [\ensuremath{-}31.4, \ensuremath{-}18.6] | P1 stale - unmarked: change in % following user (pp), 95% CI |
| `\PoneStaleVsUserDiffOtherN` | 360 | P1 stale - unmarked: change in % following user (pp), n |
| `\PoneStaleVsUserDiffOtherP` | \ensuremath{<}0.001 | P1 stale - unmarked: change in % following user (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsUserDiffEsc` | 14.4 | P1 stale - unmarked: change in % flagging the conflict vs user (pp) |
| `\PoneStaleVsUserDiffEscLo` | 10.0 | P1 stale - unmarked: change in % flagging the conflict vs user (pp), lower 95% CI bound |
| `\PoneStaleVsUserDiffEscHi` | 18.9 | P1 stale - unmarked: change in % flagging the conflict vs user (pp), upper 95% CI bound |
| `\PoneStaleVsUserDiffEscCI` | [10.0, 18.9] | P1 stale - unmarked: change in % flagging the conflict vs user (pp), 95% CI |
| `\PoneStaleVsUserDiffEscN` | 360 | P1 stale - unmarked: change in % flagging the conflict vs user (pp), n |
| `\PoneStaleVsUserDiffEscP` | \ensuremath{<}0.001 | P1 stale - unmarked: change in % flagging the conflict vs user (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsUserNetUnmarked` | \ensuremath{-}40.3 | P1 unmarked trials on the same items: net memory - user (pp) |
| `\PoneStaleVsUserNetUnmarkedLo` | \ensuremath{-}47.8 | P1 unmarked trials on the same items: net memory - user (pp), lower 95% CI bound |
| `\PoneStaleVsUserNetUnmarkedHi` | \ensuremath{-}32.2 | P1 unmarked trials on the same items: net memory - user (pp), upper 95% CI bound |
| `\PoneStaleVsUserNetUnmarkedCI` | [\ensuremath{-}47.8, \ensuremath{-}32.2] | P1 unmarked trials on the same items: net memory - user (pp), 95% CI |
| `\PoneStaleVsUserNetUnmarkedN` | 360 | P1 unmarked trials on the same items: net memory - user (pp), n |
| `\PoneStaleVsUserNetUnmarkedP` | \ensuremath{<}0.001 | P1 unmarked trials on the same items: net memory - user (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneStaleVsUserNet` | \ensuremath{-}4.7 | P1 stale: net memory - user (pp) |
| `\PoneStaleVsUserNetLo` | \ensuremath{-}12.2 | P1 stale: net memory - user (pp), lower 95% CI bound |
| `\PoneStaleVsUserNetHi` | 2.5 | P1 stale: net memory - user (pp), upper 95% CI bound |
| `\PoneStaleVsUserNetCI` | [\ensuremath{-}12.2, 2.5] | P1 stale: net memory - user (pp), 95% CI |
| `\PoneStaleVsUserNetN` | 360 | P1 stale: net memory - user (pp), n |
| `\PoneStaleVsUserNetP` | 0.234 | P1 stale: net memory - user (pp), two-sided bootstrap p (n/a if not tested) |
| `\PoneScopeTurnItems` | 60 | P1 design turn: number of items analysed |
| `\PoneScopeTurnBalanced` | yes | P1 design turn: analysed on seeds 50-69 of every family (balanced) rather than all collected items |
| `\PoneScopeTurnFamilies` | assistant 20, inventory 20, research 20 | P1 design turn: items per task family |
| `\PoneScopeForcedItems` | 60 | P1 design forced: number of items analysed |
| `\PoneScopeForcedBalanced` | yes | P1 design forced: analysed on seeds 50-69 of every family (balanced) rather than all collected items |
| `\PoneScopeForcedFamilies` | assistant 20, inventory 20, research 20 | P1 design forced: items per task family |
| `\PoneScopeSingleItems` | 34 | P1 design single: number of items analysed |
| `\PoneScopeSingleBalanced` | no | P1 design single: analysed on seeds 50-69 of every family (balanced) rather than all collected items |
| `\PoneScopeSingleFamilies` | assistant 9, inventory 13, research 12 | P1 design single: items per task family |
| `\PoneScopeStaleItems` | 60 | P1 design stale: number of items analysed |
| `\PoneScopeStaleBalanced` | yes | P1 design stale: analysed on seeds 50-69 of every family (balanced) rather than all collected items |
| `\PoneScopeStaleFamilies` | assistant 20, inventory 20, research 20 | P1 design stale: items per task family |
| `\PoneSingleMemoryAdopt` | 98.2 | P1 single claim (no conflict) in memory: % adopted, pooled |
| `\PoneSingleMemoryAdoptLo` | 95.8 | P1 single claim (no conflict) in memory: % adopted, pooled, lower 95% CI bound |
| `\PoneSingleMemoryAdoptHi` | 100.0 | P1 single claim (no conflict) in memory: % adopted, pooled, upper 95% CI bound |
| `\PoneSingleMemoryAdoptCI` | [95.8, 100.0] | P1 single claim (no conflict) in memory: % adopted, pooled, 95% CI |
| `\PoneSingleMemoryAdoptN` | 169 | P1 single claim (no conflict) in memory: % adopted, pooled, n |
| `\PoneSingleMemoryAdoptP` | n/a | P1 single claim (no conflict) in memory: % adopted, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemoryAdoptDeepSeekVFourFlash` | 96.3 | P1 single claim (no conflict) in memory: % adopted, deepseek-v4-flash |
| `\PoneSingleMemoryAdoptDeepSeekVFourFlashLo` | 88.9 | P1 single claim (no conflict) in memory: % adopted, deepseek-v4-flash, lower 95% CI bound |
| `\PoneSingleMemoryAdoptDeepSeekVFourFlashHi` | 100.0 | P1 single claim (no conflict) in memory: % adopted, deepseek-v4-flash, upper 95% CI bound |
| `\PoneSingleMemoryAdoptDeepSeekVFourFlashCI` | [88.9, 100.0] | P1 single claim (no conflict) in memory: % adopted, deepseek-v4-flash, 95% CI |
| `\PoneSingleMemoryAdoptDeepSeekVFourFlashN` | 27 | P1 single claim (no conflict) in memory: % adopted, deepseek-v4-flash, n |
| `\PoneSingleMemoryAdoptDeepSeekVFourFlashP` | n/a | P1 single claim (no conflict) in memory: % adopted, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemoryAdoptQwenThreeEightTwoSevenB` | 100.0 | P1 single claim (no conflict) in memory: % adopted, qwen3.8-27b |
| `\PoneSingleMemoryAdoptQwenThreeEightTwoSevenBLo` | 87.7 | P1 single claim (no conflict) in memory: % adopted, qwen3.8-27b, lower 95% CI bound |
| `\PoneSingleMemoryAdoptQwenThreeEightTwoSevenBHi` | 100.0 | P1 single claim (no conflict) in memory: % adopted, qwen3.8-27b, upper 95% CI bound |
| `\PoneSingleMemoryAdoptQwenThreeEightTwoSevenBCI` | [87.7, 100.0] | P1 single claim (no conflict) in memory: % adopted, qwen3.8-27b, 95% CI |
| `\PoneSingleMemoryAdoptQwenThreeEightTwoSevenBN` | 28 | P1 single claim (no conflict) in memory: % adopted, qwen3.8-27b, n |
| `\PoneSingleMemoryAdoptQwenThreeEightTwoSevenBP` | n/a | P1 single claim (no conflict) in memory: % adopted, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemoryAdoptGemmaFourThreeOneB` | 100.0 | P1 single claim (no conflict) in memory: % adopted, gemma-4-31b-it |
| `\PoneSingleMemoryAdoptGemmaFourThreeOneBLo` | 86.8 | P1 single claim (no conflict) in memory: % adopted, gemma-4-31b-it, lower 95% CI bound |
| `\PoneSingleMemoryAdoptGemmaFourThreeOneBHi` | 100.0 | P1 single claim (no conflict) in memory: % adopted, gemma-4-31b-it, upper 95% CI bound |
| `\PoneSingleMemoryAdoptGemmaFourThreeOneBCI` | [86.8, 100.0] | P1 single claim (no conflict) in memory: % adopted, gemma-4-31b-it, 95% CI |
| `\PoneSingleMemoryAdoptGemmaFourThreeOneBN` | 26 | P1 single claim (no conflict) in memory: % adopted, gemma-4-31b-it, n |
| `\PoneSingleMemoryAdoptGemmaFourThreeOneBP` | n/a | P1 single claim (no conflict) in memory: % adopted, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemoryAdoptGLMFiveThreeFlash` | 100.0 | P1 single claim (no conflict) in memory: % adopted, glm-5.3-flash |
| `\PoneSingleMemoryAdoptGLMFiveThreeFlashLo` | 86.8 | P1 single claim (no conflict) in memory: % adopted, glm-5.3-flash, lower 95% CI bound |
| `\PoneSingleMemoryAdoptGLMFiveThreeFlashHi` | 100.0 | P1 single claim (no conflict) in memory: % adopted, glm-5.3-flash, upper 95% CI bound |
| `\PoneSingleMemoryAdoptGLMFiveThreeFlashCI` | [86.8, 100.0] | P1 single claim (no conflict) in memory: % adopted, glm-5.3-flash, 95% CI |
| `\PoneSingleMemoryAdoptGLMFiveThreeFlashN` | 26 | P1 single claim (no conflict) in memory: % adopted, glm-5.3-flash, n |
| `\PoneSingleMemoryAdoptGLMFiveThreeFlashP` | n/a | P1 single claim (no conflict) in memory: % adopted, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemoryAdoptGLMFiveTwo` | 100.0 | P1 single claim (no conflict) in memory: % adopted, glm-5.2 |
| `\PoneSingleMemoryAdoptGLMFiveTwoLo` | 87.7 | P1 single claim (no conflict) in memory: % adopted, glm-5.2, lower 95% CI bound |
| `\PoneSingleMemoryAdoptGLMFiveTwoHi` | 100.0 | P1 single claim (no conflict) in memory: % adopted, glm-5.2, upper 95% CI bound |
| `\PoneSingleMemoryAdoptGLMFiveTwoCI` | [87.7, 100.0] | P1 single claim (no conflict) in memory: % adopted, glm-5.2, 95% CI |
| `\PoneSingleMemoryAdoptGLMFiveTwoN` | 28 | P1 single claim (no conflict) in memory: % adopted, glm-5.2, n |
| `\PoneSingleMemoryAdoptGLMFiveTwoP` | n/a | P1 single claim (no conflict) in memory: % adopted, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemoryAdoptQwenThreeFiveThreeNineSevenB` | 94.1 | P1 single claim (no conflict) in memory: % adopted, qwen3.5-397b |
| `\PoneSingleMemoryAdoptQwenThreeFiveThreeNineSevenBLo` | 85.3 | P1 single claim (no conflict) in memory: % adopted, qwen3.5-397b, lower 95% CI bound |
| `\PoneSingleMemoryAdoptQwenThreeFiveThreeNineSevenBHi` | 100.0 | P1 single claim (no conflict) in memory: % adopted, qwen3.5-397b, upper 95% CI bound |
| `\PoneSingleMemoryAdoptQwenThreeFiveThreeNineSevenBCI` | [85.3, 100.0] | P1 single claim (no conflict) in memory: % adopted, qwen3.5-397b, 95% CI |
| `\PoneSingleMemoryAdoptQwenThreeFiveThreeNineSevenBN` | 34 | P1 single claim (no conflict) in memory: % adopted, qwen3.5-397b, n |
| `\PoneSingleMemoryAdoptQwenThreeFiveThreeNineSevenBP` | n/a | P1 single claim (no conflict) in memory: % adopted, qwen3.5-397b, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleToolAdopt` | 97.6 | P1 single claim (no conflict) in tool: % adopted, pooled |
| `\PoneSingleToolAdoptLo` | 94.8 | P1 single claim (no conflict) in tool: % adopted, pooled, lower 95% CI bound |
| `\PoneSingleToolAdoptHi` | 99.5 | P1 single claim (no conflict) in tool: % adopted, pooled, upper 95% CI bound |
| `\PoneSingleToolAdoptCI` | [94.8, 99.5] | P1 single claim (no conflict) in tool: % adopted, pooled, 95% CI |
| `\PoneSingleToolAdoptN` | 169 | P1 single claim (no conflict) in tool: % adopted, pooled, n |
| `\PoneSingleToolAdoptP` | n/a | P1 single claim (no conflict) in tool: % adopted, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleToolAdoptDeepSeekVFourFlash` | 92.6 | P1 single claim (no conflict) in tool: % adopted, deepseek-v4-flash |
| `\PoneSingleToolAdoptDeepSeekVFourFlashLo` | 81.5 | P1 single claim (no conflict) in tool: % adopted, deepseek-v4-flash, lower 95% CI bound |
| `\PoneSingleToolAdoptDeepSeekVFourFlashHi` | 100.0 | P1 single claim (no conflict) in tool: % adopted, deepseek-v4-flash, upper 95% CI bound |
| `\PoneSingleToolAdoptDeepSeekVFourFlashCI` | [81.5, 100.0] | P1 single claim (no conflict) in tool: % adopted, deepseek-v4-flash, 95% CI |
| `\PoneSingleToolAdoptDeepSeekVFourFlashN` | 27 | P1 single claim (no conflict) in tool: % adopted, deepseek-v4-flash, n |
| `\PoneSingleToolAdoptDeepSeekVFourFlashP` | n/a | P1 single claim (no conflict) in tool: % adopted, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleToolAdoptQwenThreeEightTwoSevenB` | 100.0 | P1 single claim (no conflict) in tool: % adopted, qwen3.8-27b |
| `\PoneSingleToolAdoptQwenThreeEightTwoSevenBLo` | 87.7 | P1 single claim (no conflict) in tool: % adopted, qwen3.8-27b, lower 95% CI bound |
| `\PoneSingleToolAdoptQwenThreeEightTwoSevenBHi` | 100.0 | P1 single claim (no conflict) in tool: % adopted, qwen3.8-27b, upper 95% CI bound |
| `\PoneSingleToolAdoptQwenThreeEightTwoSevenBCI` | [87.7, 100.0] | P1 single claim (no conflict) in tool: % adopted, qwen3.8-27b, 95% CI |
| `\PoneSingleToolAdoptQwenThreeEightTwoSevenBN` | 28 | P1 single claim (no conflict) in tool: % adopted, qwen3.8-27b, n |
| `\PoneSingleToolAdoptQwenThreeEightTwoSevenBP` | n/a | P1 single claim (no conflict) in tool: % adopted, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleToolAdoptGemmaFourThreeOneB` | 100.0 | P1 single claim (no conflict) in tool: % adopted, gemma-4-31b-it |
| `\PoneSingleToolAdoptGemmaFourThreeOneBLo` | 86.8 | P1 single claim (no conflict) in tool: % adopted, gemma-4-31b-it, lower 95% CI bound |
| `\PoneSingleToolAdoptGemmaFourThreeOneBHi` | 100.0 | P1 single claim (no conflict) in tool: % adopted, gemma-4-31b-it, upper 95% CI bound |
| `\PoneSingleToolAdoptGemmaFourThreeOneBCI` | [86.8, 100.0] | P1 single claim (no conflict) in tool: % adopted, gemma-4-31b-it, 95% CI |
| `\PoneSingleToolAdoptGemmaFourThreeOneBN` | 26 | P1 single claim (no conflict) in tool: % adopted, gemma-4-31b-it, n |
| `\PoneSingleToolAdoptGemmaFourThreeOneBP` | n/a | P1 single claim (no conflict) in tool: % adopted, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleToolAdoptGLMFiveThreeFlash` | 100.0 | P1 single claim (no conflict) in tool: % adopted, glm-5.3-flash |
| `\PoneSingleToolAdoptGLMFiveThreeFlashLo` | 86.8 | P1 single claim (no conflict) in tool: % adopted, glm-5.3-flash, lower 95% CI bound |
| `\PoneSingleToolAdoptGLMFiveThreeFlashHi` | 100.0 | P1 single claim (no conflict) in tool: % adopted, glm-5.3-flash, upper 95% CI bound |
| `\PoneSingleToolAdoptGLMFiveThreeFlashCI` | [86.8, 100.0] | P1 single claim (no conflict) in tool: % adopted, glm-5.3-flash, 95% CI |
| `\PoneSingleToolAdoptGLMFiveThreeFlashN` | 26 | P1 single claim (no conflict) in tool: % adopted, glm-5.3-flash, n |
| `\PoneSingleToolAdoptGLMFiveThreeFlashP` | n/a | P1 single claim (no conflict) in tool: % adopted, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleToolAdoptGLMFiveTwo` | 100.0 | P1 single claim (no conflict) in tool: % adopted, glm-5.2 |
| `\PoneSingleToolAdoptGLMFiveTwoLo` | 87.7 | P1 single claim (no conflict) in tool: % adopted, glm-5.2, lower 95% CI bound |
| `\PoneSingleToolAdoptGLMFiveTwoHi` | 100.0 | P1 single claim (no conflict) in tool: % adopted, glm-5.2, upper 95% CI bound |
| `\PoneSingleToolAdoptGLMFiveTwoCI` | [87.7, 100.0] | P1 single claim (no conflict) in tool: % adopted, glm-5.2, 95% CI |
| `\PoneSingleToolAdoptGLMFiveTwoN` | 28 | P1 single claim (no conflict) in tool: % adopted, glm-5.2, n |
| `\PoneSingleToolAdoptGLMFiveTwoP` | n/a | P1 single claim (no conflict) in tool: % adopted, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleToolAdoptQwenThreeFiveThreeNineSevenB` | 94.1 | P1 single claim (no conflict) in tool: % adopted, qwen3.5-397b |
| `\PoneSingleToolAdoptQwenThreeFiveThreeNineSevenBLo` | 85.3 | P1 single claim (no conflict) in tool: % adopted, qwen3.5-397b, lower 95% CI bound |
| `\PoneSingleToolAdoptQwenThreeFiveThreeNineSevenBHi` | 100.0 | P1 single claim (no conflict) in tool: % adopted, qwen3.5-397b, upper 95% CI bound |
| `\PoneSingleToolAdoptQwenThreeFiveThreeNineSevenBCI` | [85.3, 100.0] | P1 single claim (no conflict) in tool: % adopted, qwen3.5-397b, 95% CI |
| `\PoneSingleToolAdoptQwenThreeFiveThreeNineSevenBN` | 34 | P1 single claim (no conflict) in tool: % adopted, qwen3.5-397b, n |
| `\PoneSingleToolAdoptQwenThreeFiveThreeNineSevenBP` | n/a | P1 single claim (no conflict) in tool: % adopted, qwen3.5-397b, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemMinusTool` | 0.6 | P1 single claim: adoption memory - tool (pp), pooled |
| `\PoneSingleMemMinusToolLo` | 0.0 | P1 single claim: adoption memory - tool (pp), pooled, lower 95% CI bound |
| `\PoneSingleMemMinusToolHi` | 1.8 | P1 single claim: adoption memory - tool (pp), pooled, upper 95% CI bound |
| `\PoneSingleMemMinusToolCI` | [0.0, 1.8] | P1 single claim: adoption memory - tool (pp), pooled, 95% CI |
| `\PoneSingleMemMinusToolN` | 169 | P1 single claim: adoption memory - tool (pp), pooled, n |
| `\PoneSingleMemMinusToolP` | 0.747 | P1 single claim: adoption memory - tool (pp), pooled, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemMinusToolDeepSeekVFourFlash` | 3.7 | P1 single claim: adoption memory - tool (pp), deepseek-v4-flash |
| `\PoneSingleMemMinusToolDeepSeekVFourFlashLo` | 0.0 | P1 single claim: adoption memory - tool (pp), deepseek-v4-flash, lower 95% CI bound |
| `\PoneSingleMemMinusToolDeepSeekVFourFlashHi` | 11.1 | P1 single claim: adoption memory - tool (pp), deepseek-v4-flash, upper 95% CI bound |
| `\PoneSingleMemMinusToolDeepSeekVFourFlashCI` | [0.0, 11.1] | P1 single claim: adoption memory - tool (pp), deepseek-v4-flash, 95% CI |
| `\PoneSingleMemMinusToolDeepSeekVFourFlashN` | 27 | P1 single claim: adoption memory - tool (pp), deepseek-v4-flash, n |
| `\PoneSingleMemMinusToolDeepSeekVFourFlashP` | 0.731 | P1 single claim: adoption memory - tool (pp), deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemMinusToolQwenThreeEightTwoSevenB` | 0.0 | P1 single claim: adoption memory - tool (pp), qwen3.8-27b |
| `\PoneSingleMemMinusToolQwenThreeEightTwoSevenBLo` | 0.0 | P1 single claim: adoption memory - tool (pp), qwen3.8-27b, lower 95% CI bound |
| `\PoneSingleMemMinusToolQwenThreeEightTwoSevenBHi` | 0.0 | P1 single claim: adoption memory - tool (pp), qwen3.8-27b, upper 95% CI bound |
| `\PoneSingleMemMinusToolQwenThreeEightTwoSevenBCI` | [0.0, 0.0] | P1 single claim: adoption memory - tool (pp), qwen3.8-27b, 95% CI |
| `\PoneSingleMemMinusToolQwenThreeEightTwoSevenBN` | 28 | P1 single claim: adoption memory - tool (pp), qwen3.8-27b, n |
| `\PoneSingleMemMinusToolQwenThreeEightTwoSevenBP` | 1.000 | P1 single claim: adoption memory - tool (pp), qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemMinusToolGemmaFourThreeOneB` | 0.0 | P1 single claim: adoption memory - tool (pp), gemma-4-31b-it |
| `\PoneSingleMemMinusToolGemmaFourThreeOneBLo` | 0.0 | P1 single claim: adoption memory - tool (pp), gemma-4-31b-it, lower 95% CI bound |
| `\PoneSingleMemMinusToolGemmaFourThreeOneBHi` | 0.0 | P1 single claim: adoption memory - tool (pp), gemma-4-31b-it, upper 95% CI bound |
| `\PoneSingleMemMinusToolGemmaFourThreeOneBCI` | [0.0, 0.0] | P1 single claim: adoption memory - tool (pp), gemma-4-31b-it, 95% CI |
| `\PoneSingleMemMinusToolGemmaFourThreeOneBN` | 26 | P1 single claim: adoption memory - tool (pp), gemma-4-31b-it, n |
| `\PoneSingleMemMinusToolGemmaFourThreeOneBP` | 1.000 | P1 single claim: adoption memory - tool (pp), gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemMinusToolGLMFiveThreeFlash` | 0.0 | P1 single claim: adoption memory - tool (pp), glm-5.3-flash |
| `\PoneSingleMemMinusToolGLMFiveThreeFlashLo` | 0.0 | P1 single claim: adoption memory - tool (pp), glm-5.3-flash, lower 95% CI bound |
| `\PoneSingleMemMinusToolGLMFiveThreeFlashHi` | 0.0 | P1 single claim: adoption memory - tool (pp), glm-5.3-flash, upper 95% CI bound |
| `\PoneSingleMemMinusToolGLMFiveThreeFlashCI` | [0.0, 0.0] | P1 single claim: adoption memory - tool (pp), glm-5.3-flash, 95% CI |
| `\PoneSingleMemMinusToolGLMFiveThreeFlashN` | 26 | P1 single claim: adoption memory - tool (pp), glm-5.3-flash, n |
| `\PoneSingleMemMinusToolGLMFiveThreeFlashP` | 1.000 | P1 single claim: adoption memory - tool (pp), glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemMinusToolGLMFiveTwo` | 0.0 | P1 single claim: adoption memory - tool (pp), glm-5.2 |
| `\PoneSingleMemMinusToolGLMFiveTwoLo` | 0.0 | P1 single claim: adoption memory - tool (pp), glm-5.2, lower 95% CI bound |
| `\PoneSingleMemMinusToolGLMFiveTwoHi` | 0.0 | P1 single claim: adoption memory - tool (pp), glm-5.2, upper 95% CI bound |
| `\PoneSingleMemMinusToolGLMFiveTwoCI` | [0.0, 0.0] | P1 single claim: adoption memory - tool (pp), glm-5.2, 95% CI |
| `\PoneSingleMemMinusToolGLMFiveTwoN` | 28 | P1 single claim: adoption memory - tool (pp), glm-5.2, n |
| `\PoneSingleMemMinusToolGLMFiveTwoP` | 1.000 | P1 single claim: adoption memory - tool (pp), glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PoneSingleMemMinusToolQwenThreeFiveThreeNineSevenB` | 0.0 | P1 single claim: adoption memory - tool (pp), qwen3.5-397b |
| `\PoneSingleMemMinusToolQwenThreeFiveThreeNineSevenBLo` | 0.0 | P1 single claim: adoption memory - tool (pp), qwen3.5-397b, lower 95% CI bound |
| `\PoneSingleMemMinusToolQwenThreeFiveThreeNineSevenBHi` | 0.0 | P1 single claim: adoption memory - tool (pp), qwen3.5-397b, upper 95% CI bound |
| `\PoneSingleMemMinusToolQwenThreeFiveThreeNineSevenBCI` | [0.0, 0.0] | P1 single claim: adoption memory - tool (pp), qwen3.5-397b, 95% CI |
| `\PoneSingleMemMinusToolQwenThreeFiveThreeNineSevenBN` | 34 | P1 single claim: adoption memory - tool (pp), qwen3.5-397b, n |
| `\PoneSingleMemMinusToolQwenThreeFiveThreeNineSevenBP` | 1.000 | P1 single claim: adoption memory - tool (pp), qwen3.5-397b, two-sided bootstrap p (n/a if not tested) |
| `\PonePositionFirst` | 52.5 | P1 % following the first-shown claim (side chosen) |
| `\PonePositionFirstLo` | 48.7 | P1 % following the first-shown claim (side chosen), lower 95% CI bound |
| `\PonePositionFirstHi` | 55.8 | P1 % following the first-shown claim (side chosen), upper 95% CI bound |
| `\PonePositionFirstCI` | [48.7, 55.8] | P1 % following the first-shown claim (side chosen), 95% CI |
| `\PonePositionFirstN` | 4{,}200 | P1 % following the first-shown claim (side chosen), n |
| `\PonePositionFirstP` | 0.196 | P1 % following the first-shown claim (side chosen), two-sided bootstrap p (n/a if not tested) |
| `\PoneEscPair` | 71.7 | P1 % flags conflict, design pair |
| `\PoneEscPairLo` | 66.5 | P1 % flags conflict, design pair, lower 95% CI bound |
| `\PoneEscPairHi` | 76.5 | P1 % flags conflict, design pair, upper 95% CI bound |
| `\PoneEscPairCI` | [66.5, 76.5] | P1 % flags conflict, design pair, 95% CI |
| `\PoneEscPairN` | 7{,}200 | P1 % flags conflict, design pair, n |
| `\PoneEscPairP` | n/a | P1 % flags conflict, design pair, two-sided bootstrap p (n/a if not tested) |
| `\PoneConfPair` | 94.4 | P1 mean stated confidence, design pair |
| `\PoneConfPairLo` | 94.1 | P1 mean stated confidence, design pair, lower 95% CI bound |
| `\PoneConfPairHi` | 94.6 | P1 mean stated confidence, design pair, upper 95% CI bound |
| `\PoneConfPairCI` | [94.1, 94.6] | P1 mean stated confidence, design pair, 95% CI |
| `\PoneConfPairN` | 7{,}177 | P1 mean stated confidence, design pair, n |
| `\PoneConfPairP` | n/a | P1 mean stated confidence, design pair, two-sided bootstrap p (n/a if not tested) |
| `\PoneEscFraming` | 70.7 | P1 % flags conflict, design framing |
| `\PoneEscFramingLo` | 64.9 | P1 % flags conflict, design framing, lower 95% CI bound |
| `\PoneEscFramingHi` | 76.4 | P1 % flags conflict, design framing, upper 95% CI bound |
| `\PoneEscFramingCI` | [64.9, 76.4] | P1 % flags conflict, design framing, 95% CI |
| `\PoneEscFramingN` | 2{,}880 | P1 % flags conflict, design framing, n |
| `\PoneEscFramingP` | n/a | P1 % flags conflict, design framing, two-sided bootstrap p (n/a if not tested) |
| `\PoneConfFraming` | 94.3 | P1 mean stated confidence, design framing |
| `\PoneConfFramingLo` | 94.1 | P1 mean stated confidence, design framing, lower 95% CI bound |
| `\PoneConfFramingHi` | 94.5 | P1 mean stated confidence, design framing, upper 95% CI bound |
| `\PoneConfFramingCI` | [94.1, 94.5] | P1 mean stated confidence, design framing, 95% CI |
| `\PoneConfFramingN` | 2{,}871 | P1 mean stated confidence, design framing, n |
| `\PoneConfFramingP` | n/a | P1 mean stated confidence, design framing, two-sided bootstrap p (n/a if not tested) |
| `\PoneEscTurn` | 47.8 | P1 % flags conflict, design turn |
| `\PoneEscTurnLo` | 38.6 | P1 % flags conflict, design turn, lower 95% CI bound |
| `\PoneEscTurnHi` | 56.8 | P1 % flags conflict, design turn, upper 95% CI bound |
| `\PoneEscTurnCI` | [38.6, 56.8] | P1 % flags conflict, design turn, 95% CI |
| `\PoneEscTurnN` | 720 | P1 % flags conflict, design turn, n |
| `\PoneEscTurnP` | n/a | P1 % flags conflict, design turn, two-sided bootstrap p (n/a if not tested) |
| `\PoneConfTurn` | 95.9 | P1 mean stated confidence, design turn |
| `\PoneConfTurnLo` | 95.6 | P1 mean stated confidence, design turn, lower 95% CI bound |
| `\PoneConfTurnHi` | 96.2 | P1 mean stated confidence, design turn, upper 95% CI bound |
| `\PoneConfTurnCI` | [95.6, 96.2] | P1 mean stated confidence, design turn, 95% CI |
| `\PoneConfTurnN` | 720 | P1 mean stated confidence, design turn, n |
| `\PoneConfTurnP` | n/a | P1 mean stated confidence, design turn, two-sided bootstrap p (n/a if not tested) |
| `\PoneEscForced` | 0.0 | P1 % flags conflict, design forced |
| `\PoneEscForcedLo` | 0.0 | P1 % flags conflict, design forced, lower 95% CI bound |
| `\PoneEscForcedHi` | 0.3 | P1 % flags conflict, design forced, upper 95% CI bound |
| `\PoneEscForcedCI` | [0.0, 0.3] | P1 % flags conflict, design forced, 95% CI |
| `\PoneEscForcedN` | 1{,}080 | P1 % flags conflict, design forced, n |
| `\PoneEscForcedP` | n/a | P1 % flags conflict, design forced, two-sided bootstrap p (n/a if not tested) |
| `\PoneConfForced` | 95.0 | P1 mean stated confidence, design forced |
| `\PoneConfForcedLo` | 94.7 | P1 mean stated confidence, design forced, lower 95% CI bound |
| `\PoneConfForcedHi` | 95.2 | P1 mean stated confidence, design forced, upper 95% CI bound |
| `\PoneConfForcedCI` | [94.7, 95.2] | P1 mean stated confidence, design forced, 95% CI |
| `\PoneConfForcedN` | 1{,}079 | P1 mean stated confidence, design forced, n |
| `\PoneConfForcedP` | n/a | P1 mean stated confidence, design forced, two-sided bootstrap p (n/a if not tested) |
| `\PoneEscStale` | 74.4 | P1 % flags conflict, design stale |
| `\PoneEscStaleLo` | 67.3 | P1 % flags conflict, design stale, lower 95% CI bound |
| `\PoneEscStaleHi` | 80.7 | P1 % flags conflict, design stale, upper 95% CI bound |
| `\PoneEscStaleCI` | [67.3, 80.7] | P1 % flags conflict, design stale, 95% CI |
| `\PoneEscStaleN` | 1{,}080 | P1 % flags conflict, design stale, n |
| `\PoneEscStaleP` | n/a | P1 % flags conflict, design stale, two-sided bootstrap p (n/a if not tested) |
| `\PoneConfStale` | 94.1 | P1 mean stated confidence, design stale |
| `\PoneConfStaleLo` | 93.6 | P1 mean stated confidence, design stale, lower 95% CI bound |
| `\PoneConfStaleHi` | 94.5 | P1 mean stated confidence, design stale, upper 95% CI bound |
| `\PoneConfStaleCI` | [93.6, 94.5] | P1 mean stated confidence, design stale, 95% CI |
| `\PoneConfStaleN` | 1{,}077 | P1 mean stated confidence, design stale, n |
| `\PoneConfStaleP` | n/a | P1 mean stated confidence, design stale, two-sided bootstrap p (n/a if not tested) |
| `\PoneEscSingle` | 0.9 | P1 % flags conflict, design single |
| `\PoneEscSingleLo` | 0.0 | P1 % flags conflict, design single, lower 95% CI bound |
| `\PoneEscSingleHi` | 2.3 | P1 % flags conflict, design single, upper 95% CI bound |
| `\PoneEscSingleCI` | [0.0, 2.3] | P1 % flags conflict, design single, 95% CI |
| `\PoneEscSingleN` | 338 | P1 % flags conflict, design single, n |
| `\PoneEscSingleP` | n/a | P1 % flags conflict, design single, two-sided bootstrap p (n/a if not tested) |
| `\PoneConfSingle` | 97.6 | P1 mean stated confidence, design single |
| `\PoneConfSingleLo` | 97.2 | P1 mean stated confidence, design single, lower 95% CI bound |
| `\PoneConfSingleHi` | 98.0 | P1 mean stated confidence, design single, upper 95% CI bound |
| `\PoneConfSingleCI` | [97.2, 98.0] | P1 mean stated confidence, design single, 95% CI |
| `\PoneConfSingleN` | 334 | P1 mean stated confidence, design single, n |
| `\PoneConfSingleP` | n/a | P1 mean stated confidence, design single, two-sided bootstrap p (n/a if not tested) |
| `\LaundConfidence` | \ensuremath{-}2.2 | confidence laundering, stated confidence (0-100 points) |
| `\LaundConfidenceLo` | \ensuremath{-}3.1 | confidence laundering, stated confidence (0-100 points), lower 95% CI bound |
| `\LaundConfidenceHi` | \ensuremath{-}1.2 | confidence laundering, stated confidence (0-100 points), upper 95% CI bound |
| `\LaundConfidenceCI` | [\ensuremath{-}3.1, \ensuremath{-}1.2] | confidence laundering, stated confidence (0-100 points), 95% CI |
| `\LaundConfidenceN` | 1{,}432 | confidence laundering, stated confidence (0-100 points), n |
| `\LaundConfidenceP` | \ensuremath{<}0.001 | confidence laundering, stated confidence (0-100 points), two-sided bootstrap p (n/a if not tested) |
| `\LaundConfidenceEffectMemory` | 70.3 | certain - hedged, memory, stated confidence (0-100 points) |
| `\LaundConfidenceEffectMemoryLo` | 68.0 | certain - hedged, memory, stated confidence (0-100 points), lower 95% CI bound |
| `\LaundConfidenceEffectMemoryHi` | 72.5 | certain - hedged, memory, stated confidence (0-100 points), upper 95% CI bound |
| `\LaundConfidenceEffectMemoryCI` | [68.0, 72.5] | certain - hedged, memory, stated confidence (0-100 points), 95% CI |
| `\LaundConfidenceEffectMemoryN` | 1{,}432 | certain - hedged, memory, stated confidence (0-100 points), n |
| `\LaundConfidenceEffectMemoryP` | \ensuremath{<}0.001 | certain - hedged, memory, stated confidence (0-100 points), two-sided bootstrap p (n/a if not tested) |
| `\LaundConfidenceEffectTool` | 72.5 | certain - hedged, tool, stated confidence (0-100 points) |
| `\LaundConfidenceEffectToolLo` | 70.2 | certain - hedged, tool, stated confidence (0-100 points), lower 95% CI bound |
| `\LaundConfidenceEffectToolHi` | 74.7 | certain - hedged, tool, stated confidence (0-100 points), upper 95% CI bound |
| `\LaundConfidenceEffectToolCI` | [70.2, 74.7] | certain - hedged, tool, stated confidence (0-100 points), 95% CI |
| `\LaundConfidenceEffectToolN` | 1{,}432 | certain - hedged, tool, stated confidence (0-100 points), n |
| `\LaundConfidenceEffectToolP` | \ensuremath{<}0.001 | certain - hedged, tool, stated confidence (0-100 points), two-sided bootstrap p (n/a if not tested) |
| `\LaundConfidenceMemoryHedged` | 26.5 | confidence mean, memory_hedged |
| `\LaundConfidenceMemoryHedgedLo` | 24.2 | confidence mean, memory_hedged, lower 95% CI bound |
| `\LaundConfidenceMemoryHedgedHi` | 28.9 | confidence mean, memory_hedged, upper 95% CI bound |
| `\LaundConfidenceMemoryHedgedCI` | [24.2, 28.9] | confidence mean, memory_hedged, 95% CI |
| `\LaundConfidenceMemoryHedgedN` | 357 | confidence mean, memory_hedged, n |
| `\LaundConfidenceMemoryHedgedP` | n/a | confidence mean, memory_hedged, two-sided bootstrap p (n/a if not tested) |
| `\LaundConfidenceMemoryCertain` | 96.8 | confidence mean, memory_certain |
| `\LaundConfidenceMemoryCertainLo` | 96.4 | confidence mean, memory_certain, lower 95% CI bound |
| `\LaundConfidenceMemoryCertainHi` | 97.1 | confidence mean, memory_certain, upper 95% CI bound |
| `\LaundConfidenceMemoryCertainCI` | [96.4, 97.1] | confidence mean, memory_certain, 95% CI |
| `\LaundConfidenceMemoryCertainN` | 359 | confidence mean, memory_certain, n |
| `\LaundConfidenceMemoryCertainP` | n/a | confidence mean, memory_certain, two-sided bootstrap p (n/a if not tested) |
| `\LaundConfidenceToolHedged` | 25.1 | confidence mean, tool_hedged |
| `\LaundConfidenceToolHedgedLo` | 22.8 | confidence mean, tool_hedged, lower 95% CI bound |
| `\LaundConfidenceToolHedgedHi` | 27.5 | confidence mean, tool_hedged, upper 95% CI bound |
| `\LaundConfidenceToolHedgedCI` | [22.8, 27.5] | confidence mean, tool_hedged, 95% CI |
| `\LaundConfidenceToolHedgedN` | 357 | confidence mean, tool_hedged, n |
| `\LaundConfidenceToolHedgedP` | n/a | confidence mean, tool_hedged, two-sided bootstrap p (n/a if not tested) |
| `\LaundConfidenceToolCertain` | 97.6 | confidence mean, tool_certain |
| `\LaundConfidenceToolCertainLo` | 97.2 | confidence mean, tool_certain, lower 95% CI bound |
| `\LaundConfidenceToolCertainHi` | 97.9 | confidence mean, tool_certain, upper 95% CI bound |
| `\LaundConfidenceToolCertainCI` | [97.2, 97.9] | confidence mean, tool_certain, 95% CI |
| `\LaundConfidenceToolCertainN` | 359 | confidence mean, tool_certain, n |
| `\LaundConfidenceToolCertainP` | n/a | confidence mean, tool_certain, two-sided bootstrap p (n/a if not tested) |
| `\LaundAct` | \ensuremath{-}2.2 | confidence laundering, act rate (pp) |
| `\LaundActLo` | \ensuremath{-}6.5 | confidence laundering, act rate (pp), lower 95% CI bound |
| `\LaundActHi` | 1.5 | confidence laundering, act rate (pp), upper 95% CI bound |
| `\LaundActCI` | [\ensuremath{-}6.5, 1.5] | confidence laundering, act rate (pp), 95% CI |
| `\LaundActN` | 1{,}432 | confidence laundering, act rate (pp), n |
| `\LaundActP` | 0.245 | confidence laundering, act rate (pp), two-sided bootstrap p (n/a if not tested) |
| `\LaundActEffectMemory` | 66.0 | certain - hedged, memory, act rate (pp) |
| `\LaundActEffectMemoryLo` | 59.4 | certain - hedged, memory, act rate (pp), lower 95% CI bound |
| `\LaundActEffectMemoryHi` | 72.2 | certain - hedged, memory, act rate (pp), upper 95% CI bound |
| `\LaundActEffectMemoryCI` | [59.4, 72.2] | certain - hedged, memory, act rate (pp), 95% CI |
| `\LaundActEffectMemoryN` | 1{,}432 | certain - hedged, memory, act rate (pp), n |
| `\LaundActEffectMemoryP` | \ensuremath{<}0.001 | certain - hedged, memory, act rate (pp), two-sided bootstrap p (n/a if not tested) |
| `\LaundActEffectTool` | 68.2 | certain - hedged, tool, act rate (pp) |
| `\LaundActEffectToolLo` | 61.5 | certain - hedged, tool, act rate (pp), lower 95% CI bound |
| `\LaundActEffectToolHi` | 74.7 | certain - hedged, tool, act rate (pp), upper 95% CI bound |
| `\LaundActEffectToolCI` | [61.5, 74.7] | certain - hedged, tool, act rate (pp), 95% CI |
| `\LaundActEffectToolN` | 1{,}432 | certain - hedged, tool, act rate (pp), n |
| `\LaundActEffectToolP` | \ensuremath{<}0.001 | certain - hedged, tool, act rate (pp), two-sided bootstrap p (n/a if not tested) |
| `\LaundActMemoryHedged` | 0.0 | act mean, memory_hedged |
| `\LaundActMemoryHedgedLo` | 0.0 | act mean, memory_hedged, lower 95% CI bound |
| `\LaundActMemoryHedgedHi` | 0.0 | act mean, memory_hedged, upper 95% CI bound |
| `\LaundActMemoryHedgedCI` | [0.0, 0.0] | act mean, memory_hedged, 95% CI |
| `\LaundActMemoryHedgedN` | 357 | act mean, memory_hedged, n |
| `\LaundActMemoryHedgedP` | n/a | act mean, memory_hedged, two-sided bootstrap p (n/a if not tested) |
| `\LaundActMemoryCertain` | 66.0 | act mean, memory_certain |
| `\LaundActMemoryCertainLo` | 59.4 | act mean, memory_certain, lower 95% CI bound |
| `\LaundActMemoryCertainHi` | 72.2 | act mean, memory_certain, upper 95% CI bound |
| `\LaundActMemoryCertainCI` | [59.4, 72.2] | act mean, memory_certain, 95% CI |
| `\LaundActMemoryCertainN` | 359 | act mean, memory_certain, n |
| `\LaundActMemoryCertainP` | n/a | act mean, memory_certain, two-sided bootstrap p (n/a if not tested) |
| `\LaundActToolHedged` | 0.0 | act mean, tool_hedged |
| `\LaundActToolHedgedLo` | 0.0 | act mean, tool_hedged, lower 95% CI bound |
| `\LaundActToolHedgedHi` | 0.0 | act mean, tool_hedged, upper 95% CI bound |
| `\LaundActToolHedgedCI` | [0.0, 0.0] | act mean, tool_hedged, 95% CI |
| `\LaundActToolHedgedN` | 357 | act mean, tool_hedged, n |
| `\LaundActToolHedgedP` | n/a | act mean, tool_hedged, two-sided bootstrap p (n/a if not tested) |
| `\LaundActToolCertain` | 68.2 | act mean, tool_certain |
| `\LaundActToolCertainLo` | 61.5 | act mean, tool_certain, lower 95% CI bound |
| `\LaundActToolCertainHi` | 74.7 | act mean, tool_certain, upper 95% CI bound |
| `\LaundActToolCertainCI` | [61.5, 74.7] | act mean, tool_certain, 95% CI |
| `\LaundActToolCertainN` | 359 | act mean, tool_certain, n |
| `\LaundActToolCertainP` | n/a | act mean, tool_certain, two-sided bootstrap p (n/a if not tested) |
| `\DetEditCTZeroEOne` | 0.98 | mean AUROC over hosted victims, C T0, edit type E1 |
| `\DetEditCTZeroEOneLo` | 0.97 | mean AUROC over hosted victims, C T0, edit type E1, lower 95% CI bound |
| `\DetEditCTZeroEOneHi` | 0.99 | mean AUROC over hosted victims, C T0, edit type E1, upper 95% CI bound |
| `\DetEditCTZeroEOneCI` | [0.97, 0.99] | mean AUROC over hosted victims, C T0, edit type E1, 95% CI |
| `\DetEditCTZeroEOneN` | 591 | mean AUROC over hosted victims, C T0, edit type E1, n |
| `\DetEditCTZeroEOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T0, edit type E1, two-sided bootstrap p (n/a if not tested) |
| `\DetEditCTZeroETwo` | 0.99 | mean AUROC over hosted victims, C T0, edit type E2 |
| `\DetEditCTZeroETwoLo` | 0.99 | mean AUROC over hosted victims, C T0, edit type E2, lower 95% CI bound |
| `\DetEditCTZeroETwoHi` | 1.00 | mean AUROC over hosted victims, C T0, edit type E2, upper 95% CI bound |
| `\DetEditCTZeroETwoCI` | [0.99, 1.00] | mean AUROC over hosted victims, C T0, edit type E2, 95% CI |
| `\DetEditCTZeroETwoN` | 591 | mean AUROC over hosted victims, C T0, edit type E2, n |
| `\DetEditCTZeroETwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T0, edit type E2, two-sided bootstrap p (n/a if not tested) |
| `\DetEditCTZeroEThree` | 1.00 | mean AUROC over hosted victims, C T0, edit type E3 |
| `\DetEditCTZeroEThreeLo` | 1.00 | mean AUROC over hosted victims, C T0, edit type E3, lower 95% CI bound |
| `\DetEditCTZeroEThreeHi` | 1.00 | mean AUROC over hosted victims, C T0, edit type E3, upper 95% CI bound |
| `\DetEditCTZeroEThreeCI` | [1.00, 1.00] | mean AUROC over hosted victims, C T0, edit type E3, 95% CI |
| `\DetEditCTZeroEThreeN` | 590 | mean AUROC over hosted victims, C T0, edit type E3, n |
| `\DetEditCTZeroEThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T0, edit type E3, two-sided bootstrap p (n/a if not tested) |
| `\DetEditCTZeroEFour` | 0.99 | mean AUROC over hosted victims, C T0, edit type E4 |
| `\DetEditCTZeroEFourLo` | 0.99 | mean AUROC over hosted victims, C T0, edit type E4, lower 95% CI bound |
| `\DetEditCTZeroEFourHi` | 1.00 | mean AUROC over hosted victims, C T0, edit type E4, upper 95% CI bound |
| `\DetEditCTZeroEFourCI` | [0.99, 1.00] | mean AUROC over hosted victims, C T0, edit type E4, 95% CI |
| `\DetEditCTZeroEFourN` | 591 | mean AUROC over hosted victims, C T0, edit type E4, n |
| `\DetEditCTZeroEFourP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T0, edit type E4, two-sided bootstrap p (n/a if not tested) |
| `\DetEditCTZeroEFive` | 0.99 | mean AUROC over hosted victims, C T0, edit type E5 |
| `\DetEditCTZeroEFiveLo` | 0.98 | mean AUROC over hosted victims, C T0, edit type E5, lower 95% CI bound |
| `\DetEditCTZeroEFiveHi` | 0.99 | mean AUROC over hosted victims, C T0, edit type E5, upper 95% CI bound |
| `\DetEditCTZeroEFiveCI` | [0.98, 0.99] | mean AUROC over hosted victims, C T0, edit type E5, 95% CI |
| `\DetEditCTZeroEFiveN` | 590 | mean AUROC over hosted victims, C T0, edit type E5, n |
| `\DetEditCTZeroEFiveP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T0, edit type E5, two-sided bootstrap p (n/a if not tested) |
| `\DetEditCTOneEOne` | 0.98 | mean AUROC over hosted victims, C T1, edit type E1 |
| `\DetEditCTOneEOneLo` | 0.97 | mean AUROC over hosted victims, C T1, edit type E1, lower 95% CI bound |
| `\DetEditCTOneEOneHi` | 0.99 | mean AUROC over hosted victims, C T1, edit type E1, upper 95% CI bound |
| `\DetEditCTOneEOneCI` | [0.97, 0.99] | mean AUROC over hosted victims, C T1, edit type E1, 95% CI |
| `\DetEditCTOneEOneN` | 589 | mean AUROC over hosted victims, C T1, edit type E1, n |
| `\DetEditCTOneEOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T1, edit type E1, two-sided bootstrap p (n/a if not tested) |
| `\DetEditCTOneETwo` | 0.99 | mean AUROC over hosted victims, C T1, edit type E2 |
| `\DetEditCTOneETwoLo` | 0.98 | mean AUROC over hosted victims, C T1, edit type E2, lower 95% CI bound |
| `\DetEditCTOneETwoHi` | 1.00 | mean AUROC over hosted victims, C T1, edit type E2, upper 95% CI bound |
| `\DetEditCTOneETwoCI` | [0.98, 1.00] | mean AUROC over hosted victims, C T1, edit type E2, 95% CI |
| `\DetEditCTOneETwoN` | 590 | mean AUROC over hosted victims, C T1, edit type E2, n |
| `\DetEditCTOneETwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T1, edit type E2, two-sided bootstrap p (n/a if not tested) |
| `\DetEditCTOneEThree` | 1.00 | mean AUROC over hosted victims, C T1, edit type E3 |
| `\DetEditCTOneEThreeLo` | 1.00 | mean AUROC over hosted victims, C T1, edit type E3, lower 95% CI bound |
| `\DetEditCTOneEThreeHi` | 1.00 | mean AUROC over hosted victims, C T1, edit type E3, upper 95% CI bound |
| `\DetEditCTOneEThreeCI` | [1.00, 1.00] | mean AUROC over hosted victims, C T1, edit type E3, 95% CI |
| `\DetEditCTOneEThreeN` | 591 | mean AUROC over hosted victims, C T1, edit type E3, n |
| `\DetEditCTOneEThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T1, edit type E3, two-sided bootstrap p (n/a if not tested) |
| `\DetEditCTOneEFour` | 1.00 | mean AUROC over hosted victims, C T1, edit type E4 |
| `\DetEditCTOneEFourLo` | 0.99 | mean AUROC over hosted victims, C T1, edit type E4, lower 95% CI bound |
| `\DetEditCTOneEFourHi` | 1.00 | mean AUROC over hosted victims, C T1, edit type E4, upper 95% CI bound |
| `\DetEditCTOneEFourCI` | [0.99, 1.00] | mean AUROC over hosted victims, C T1, edit type E4, 95% CI |
| `\DetEditCTOneEFourN` | 590 | mean AUROC over hosted victims, C T1, edit type E4, n |
| `\DetEditCTOneEFourP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T1, edit type E4, two-sided bootstrap p (n/a if not tested) |
| `\DetEditCTOneEFive` | 0.97 | mean AUROC over hosted victims, C T1, edit type E5 |
| `\DetEditCTOneEFiveLo` | 0.96 | mean AUROC over hosted victims, C T1, edit type E5, lower 95% CI bound |
| `\DetEditCTOneEFiveHi` | 0.99 | mean AUROC over hosted victims, C T1, edit type E5, upper 95% CI bound |
| `\DetEditCTOneEFiveCI` | [0.96, 0.99] | mean AUROC over hosted victims, C T1, edit type E5, 95% CI |
| `\DetEditCTOneEFiveN` | 549 | mean AUROC over hosted victims, C T1, edit type E5, n |
| `\DetEditCTOneEFiveP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T1, edit type E5, two-sided bootstrap p (n/a if not tested) |
| `\DetEditCTTwoEOne` | 0.98 | mean AUROC over hosted victims, C T2, edit type E1 |
| `\DetEditCTTwoEOneLo` | 0.97 | mean AUROC over hosted victims, C T2, edit type E1, lower 95% CI bound |
| `\DetEditCTTwoEOneHi` | 0.99 | mean AUROC over hosted victims, C T2, edit type E1, upper 95% CI bound |
| `\DetEditCTTwoEOneCI` | [0.97, 0.99] | mean AUROC over hosted victims, C T2, edit type E1, 95% CI |
| `\DetEditCTTwoEOneN` | 589 | mean AUROC over hosted victims, C T2, edit type E1, n |
| `\DetEditCTTwoEOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T2, edit type E1, two-sided bootstrap p (n/a if not tested) |
| `\DetEditCTTwoETwo` | 0.99 | mean AUROC over hosted victims, C T2, edit type E2 |
| `\DetEditCTTwoETwoLo` | 0.98 | mean AUROC over hosted victims, C T2, edit type E2, lower 95% CI bound |
| `\DetEditCTTwoETwoHi` | 1.00 | mean AUROC over hosted victims, C T2, edit type E2, upper 95% CI bound |
| `\DetEditCTTwoETwoCI` | [0.98, 1.00] | mean AUROC over hosted victims, C T2, edit type E2, 95% CI |
| `\DetEditCTTwoETwoN` | 569 | mean AUROC over hosted victims, C T2, edit type E2, n |
| `\DetEditCTTwoETwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T2, edit type E2, two-sided bootstrap p (n/a if not tested) |
| `\DetEditCTTwoEThree` | 1.00 | mean AUROC over hosted victims, C T2, edit type E3 |
| `\DetEditCTTwoEThreeLo` | 1.00 | mean AUROC over hosted victims, C T2, edit type E3, lower 95% CI bound |
| `\DetEditCTTwoEThreeHi` | 1.00 | mean AUROC over hosted victims, C T2, edit type E3, upper 95% CI bound |
| `\DetEditCTTwoEThreeCI` | [1.00, 1.00] | mean AUROC over hosted victims, C T2, edit type E3, 95% CI |
| `\DetEditCTTwoEThreeN` | 591 | mean AUROC over hosted victims, C T2, edit type E3, n |
| `\DetEditCTTwoEThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T2, edit type E3, two-sided bootstrap p (n/a if not tested) |
| `\DetEditCTTwoEFour` | 1.00 | mean AUROC over hosted victims, C T2, edit type E4 |
| `\DetEditCTTwoEFourLo` | 0.99 | mean AUROC over hosted victims, C T2, edit type E4, lower 95% CI bound |
| `\DetEditCTTwoEFourHi` | 1.00 | mean AUROC over hosted victims, C T2, edit type E4, upper 95% CI bound |
| `\DetEditCTTwoEFourCI` | [0.99, 1.00] | mean AUROC over hosted victims, C T2, edit type E4, 95% CI |
| `\DetEditCTTwoEFourN` | 591 | mean AUROC over hosted victims, C T2, edit type E4, n |
| `\DetEditCTTwoEFourP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T2, edit type E4, two-sided bootstrap p (n/a if not tested) |
| `\DetEditCTTwoEFive` | 0.98 | mean AUROC over hosted victims, C T2, edit type E5 |
| `\DetEditCTTwoEFiveLo` | 0.96 | mean AUROC over hosted victims, C T2, edit type E5, lower 95% CI bound |
| `\DetEditCTTwoEFiveHi` | 0.99 | mean AUROC over hosted victims, C T2, edit type E5, upper 95% CI bound |
| `\DetEditCTTwoEFiveCI` | [0.96, 0.99] | mean AUROC over hosted victims, C T2, edit type E5, 95% CI |
| `\DetEditCTTwoEFiveN` | 571 | mean AUROC over hosted victims, C T2, edit type E5, n |
| `\DetEditCTTwoEFiveP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T2, edit type E5, two-sided bootstrap p (n/a if not tested) |
| `\DetEditCTThreeEOne` | 0.98 | mean AUROC over hosted victims, C T3, edit type E1 |
| `\DetEditCTThreeEOneLo` | 0.97 | mean AUROC over hosted victims, C T3, edit type E1, lower 95% CI bound |
| `\DetEditCTThreeEOneHi` | 0.99 | mean AUROC over hosted victims, C T3, edit type E1, upper 95% CI bound |
| `\DetEditCTThreeEOneCI` | [0.97, 0.99] | mean AUROC over hosted victims, C T3, edit type E1, 95% CI |
| `\DetEditCTThreeEOneN` | 591 | mean AUROC over hosted victims, C T3, edit type E1, n |
| `\DetEditCTThreeEOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T3, edit type E1, two-sided bootstrap p (n/a if not tested) |
| `\DetEditCTThreeETwo` | 0.99 | mean AUROC over hosted victims, C T3, edit type E2 |
| `\DetEditCTThreeETwoLo` | 0.99 | mean AUROC over hosted victims, C T3, edit type E2, lower 95% CI bound |
| `\DetEditCTThreeETwoHi` | 1.00 | mean AUROC over hosted victims, C T3, edit type E2, upper 95% CI bound |
| `\DetEditCTThreeETwoCI` | [0.99, 1.00] | mean AUROC over hosted victims, C T3, edit type E2, 95% CI |
| `\DetEditCTThreeETwoN` | 583 | mean AUROC over hosted victims, C T3, edit type E2, n |
| `\DetEditCTThreeETwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T3, edit type E2, two-sided bootstrap p (n/a if not tested) |
| `\DetEditCTThreeEThree` | 1.00 | mean AUROC over hosted victims, C T3, edit type E3 |
| `\DetEditCTThreeEThreeLo` | 1.00 | mean AUROC over hosted victims, C T3, edit type E3, lower 95% CI bound |
| `\DetEditCTThreeEThreeHi` | 1.00 | mean AUROC over hosted victims, C T3, edit type E3, upper 95% CI bound |
| `\DetEditCTThreeEThreeCI` | [1.00, 1.00] | mean AUROC over hosted victims, C T3, edit type E3, 95% CI |
| `\DetEditCTThreeEThreeN` | 590 | mean AUROC over hosted victims, C T3, edit type E3, n |
| `\DetEditCTThreeEThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T3, edit type E3, two-sided bootstrap p (n/a if not tested) |
| `\DetEditCTThreeEFour` | 0.99 | mean AUROC over hosted victims, C T3, edit type E4 |
| `\DetEditCTThreeEFourLo` | 0.99 | mean AUROC over hosted victims, C T3, edit type E4, lower 95% CI bound |
| `\DetEditCTThreeEFourHi` | 1.00 | mean AUROC over hosted victims, C T3, edit type E4, upper 95% CI bound |
| `\DetEditCTThreeEFourCI` | [0.99, 1.00] | mean AUROC over hosted victims, C T3, edit type E4, 95% CI |
| `\DetEditCTThreeEFourN` | 590 | mean AUROC over hosted victims, C T3, edit type E4, n |
| `\DetEditCTThreeEFourP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T3, edit type E4, two-sided bootstrap p (n/a if not tested) |
| `\DetEditCTThreeEFive` | 0.98 | mean AUROC over hosted victims, C T3, edit type E5 |
| `\DetEditCTThreeEFiveLo` | 0.97 | mean AUROC over hosted victims, C T3, edit type E5, lower 95% CI bound |
| `\DetEditCTThreeEFiveHi` | 0.99 | mean AUROC over hosted victims, C T3, edit type E5, upper 95% CI bound |
| `\DetEditCTThreeEFiveCI` | [0.97, 0.99] | mean AUROC over hosted victims, C T3, edit type E5, 95% CI |
| `\DetEditCTThreeEFiveN` | 589 | mean AUROC over hosted victims, C T3, edit type E5, n |
| `\DetEditCTThreeEFiveP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T3, edit type E5, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRTZeroEOne` | 0.93 | mean AUROC over hosted victims, R T0, edit type E1 |
| `\DetEditRTZeroEOneLo` | 0.92 | mean AUROC over hosted victims, R T0, edit type E1, lower 95% CI bound |
| `\DetEditRTZeroEOneHi` | 0.95 | mean AUROC over hosted victims, R T0, edit type E1, upper 95% CI bound |
| `\DetEditRTZeroEOneCI` | [0.92, 0.95] | mean AUROC over hosted victims, R T0, edit type E1, 95% CI |
| `\DetEditRTZeroEOneN` | 595 | mean AUROC over hosted victims, R T0, edit type E1, n |
| `\DetEditRTZeroEOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T0, edit type E1, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRTZeroETwo` | 0.96 | mean AUROC over hosted victims, R T0, edit type E2 |
| `\DetEditRTZeroETwoLo` | 0.94 | mean AUROC over hosted victims, R T0, edit type E2, lower 95% CI bound |
| `\DetEditRTZeroETwoHi` | 0.97 | mean AUROC over hosted victims, R T0, edit type E2, upper 95% CI bound |
| `\DetEditRTZeroETwoCI` | [0.94, 0.97] | mean AUROC over hosted victims, R T0, edit type E2, 95% CI |
| `\DetEditRTZeroETwoN` | 593 | mean AUROC over hosted victims, R T0, edit type E2, n |
| `\DetEditRTZeroETwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T0, edit type E2, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRTZeroEThree` | 0.95 | mean AUROC over hosted victims, R T0, edit type E3 |
| `\DetEditRTZeroEThreeLo` | 0.94 | mean AUROC over hosted victims, R T0, edit type E3, lower 95% CI bound |
| `\DetEditRTZeroEThreeHi` | 0.96 | mean AUROC over hosted victims, R T0, edit type E3, upper 95% CI bound |
| `\DetEditRTZeroEThreeCI` | [0.94, 0.96] | mean AUROC over hosted victims, R T0, edit type E3, 95% CI |
| `\DetEditRTZeroEThreeN` | 597 | mean AUROC over hosted victims, R T0, edit type E3, n |
| `\DetEditRTZeroEThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T0, edit type E3, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRTZeroEFour` | 0.96 | mean AUROC over hosted victims, R T0, edit type E4 |
| `\DetEditRTZeroEFourLo` | 0.94 | mean AUROC over hosted victims, R T0, edit type E4, lower 95% CI bound |
| `\DetEditRTZeroEFourHi` | 0.97 | mean AUROC over hosted victims, R T0, edit type E4, upper 95% CI bound |
| `\DetEditRTZeroEFourCI` | [0.94, 0.97] | mean AUROC over hosted victims, R T0, edit type E4, 95% CI |
| `\DetEditRTZeroEFourN` | 595 | mean AUROC over hosted victims, R T0, edit type E4, n |
| `\DetEditRTZeroEFourP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T0, edit type E4, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRTZeroEFive` | 0.96 | mean AUROC over hosted victims, R T0, edit type E5 |
| `\DetEditRTZeroEFiveLo` | 0.95 | mean AUROC over hosted victims, R T0, edit type E5, lower 95% CI bound |
| `\DetEditRTZeroEFiveHi` | 0.98 | mean AUROC over hosted victims, R T0, edit type E5, upper 95% CI bound |
| `\DetEditRTZeroEFiveCI` | [0.95, 0.98] | mean AUROC over hosted victims, R T0, edit type E5, 95% CI |
| `\DetEditRTZeroEFiveN` | 597 | mean AUROC over hosted victims, R T0, edit type E5, n |
| `\DetEditRTZeroEFiveP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T0, edit type E5, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRTOneEOne` | 0.94 | mean AUROC over hosted victims, R T1, edit type E1 |
| `\DetEditRTOneEOneLo` | 0.92 | mean AUROC over hosted victims, R T1, edit type E1, lower 95% CI bound |
| `\DetEditRTOneEOneHi` | 0.95 | mean AUROC over hosted victims, R T1, edit type E1, upper 95% CI bound |
| `\DetEditRTOneEOneCI` | [0.92, 0.95] | mean AUROC over hosted victims, R T1, edit type E1, 95% CI |
| `\DetEditRTOneEOneN` | 595 | mean AUROC over hosted victims, R T1, edit type E1, n |
| `\DetEditRTOneEOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T1, edit type E1, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRTOneETwo` | 0.95 | mean AUROC over hosted victims, R T1, edit type E2 |
| `\DetEditRTOneETwoLo` | 0.94 | mean AUROC over hosted victims, R T1, edit type E2, lower 95% CI bound |
| `\DetEditRTOneETwoHi` | 0.97 | mean AUROC over hosted victims, R T1, edit type E2, upper 95% CI bound |
| `\DetEditRTOneETwoCI` | [0.94, 0.97] | mean AUROC over hosted victims, R T1, edit type E2, 95% CI |
| `\DetEditRTOneETwoN` | 595 | mean AUROC over hosted victims, R T1, edit type E2, n |
| `\DetEditRTOneETwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T1, edit type E2, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRTOneEThree` | 0.95 | mean AUROC over hosted victims, R T1, edit type E3 |
| `\DetEditRTOneEThreeLo` | 0.94 | mean AUROC over hosted victims, R T1, edit type E3, lower 95% CI bound |
| `\DetEditRTOneEThreeHi` | 0.96 | mean AUROC over hosted victims, R T1, edit type E3, upper 95% CI bound |
| `\DetEditRTOneEThreeCI` | [0.94, 0.96] | mean AUROC over hosted victims, R T1, edit type E3, 95% CI |
| `\DetEditRTOneEThreeN` | 599 | mean AUROC over hosted victims, R T1, edit type E3, n |
| `\DetEditRTOneEThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T1, edit type E3, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRTOneEFour` | 0.96 | mean AUROC over hosted victims, R T1, edit type E4 |
| `\DetEditRTOneEFourLo` | 0.94 | mean AUROC over hosted victims, R T1, edit type E4, lower 95% CI bound |
| `\DetEditRTOneEFourHi` | 0.97 | mean AUROC over hosted victims, R T1, edit type E4, upper 95% CI bound |
| `\DetEditRTOneEFourCI` | [0.94, 0.97] | mean AUROC over hosted victims, R T1, edit type E4, 95% CI |
| `\DetEditRTOneEFourN` | 597 | mean AUROC over hosted victims, R T1, edit type E4, n |
| `\DetEditRTOneEFourP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T1, edit type E4, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRTOneEFive` | 0.96 | mean AUROC over hosted victims, R T1, edit type E5 |
| `\DetEditRTOneEFiveLo` | 0.95 | mean AUROC over hosted victims, R T1, edit type E5, lower 95% CI bound |
| `\DetEditRTOneEFiveHi` | 0.97 | mean AUROC over hosted victims, R T1, edit type E5, upper 95% CI bound |
| `\DetEditRTOneEFiveCI` | [0.95, 0.97] | mean AUROC over hosted victims, R T1, edit type E5, 95% CI |
| `\DetEditRTOneEFiveN` | 557 | mean AUROC over hosted victims, R T1, edit type E5, n |
| `\DetEditRTOneEFiveP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T1, edit type E5, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRTTwoEOne` | 0.94 | mean AUROC over hosted victims, R T2, edit type E1 |
| `\DetEditRTTwoEOneLo` | 0.92 | mean AUROC over hosted victims, R T2, edit type E1, lower 95% CI bound |
| `\DetEditRTTwoEOneHi` | 0.95 | mean AUROC over hosted victims, R T2, edit type E1, upper 95% CI bound |
| `\DetEditRTTwoEOneCI` | [0.92, 0.95] | mean AUROC over hosted victims, R T2, edit type E1, 95% CI |
| `\DetEditRTTwoEOneN` | 594 | mean AUROC over hosted victims, R T2, edit type E1, n |
| `\DetEditRTTwoEOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T2, edit type E1, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRTTwoETwo` | 0.95 | mean AUROC over hosted victims, R T2, edit type E2 |
| `\DetEditRTTwoETwoLo` | 0.94 | mean AUROC over hosted victims, R T2, edit type E2, lower 95% CI bound |
| `\DetEditRTTwoETwoHi` | 0.97 | mean AUROC over hosted victims, R T2, edit type E2, upper 95% CI bound |
| `\DetEditRTTwoETwoCI` | [0.94, 0.97] | mean AUROC over hosted victims, R T2, edit type E2, 95% CI |
| `\DetEditRTTwoETwoN` | 572 | mean AUROC over hosted victims, R T2, edit type E2, n |
| `\DetEditRTTwoETwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T2, edit type E2, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRTTwoEThree` | 0.95 | mean AUROC over hosted victims, R T2, edit type E3 |
| `\DetEditRTTwoEThreeLo` | 0.94 | mean AUROC over hosted victims, R T2, edit type E3, lower 95% CI bound |
| `\DetEditRTTwoEThreeHi` | 0.96 | mean AUROC over hosted victims, R T2, edit type E3, upper 95% CI bound |
| `\DetEditRTTwoEThreeCI` | [0.94, 0.96] | mean AUROC over hosted victims, R T2, edit type E3, 95% CI |
| `\DetEditRTTwoEThreeN` | 598 | mean AUROC over hosted victims, R T2, edit type E3, n |
| `\DetEditRTTwoEThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T2, edit type E3, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRTTwoEFour` | 0.96 | mean AUROC over hosted victims, R T2, edit type E4 |
| `\DetEditRTTwoEFourLo` | 0.94 | mean AUROC over hosted victims, R T2, edit type E4, lower 95% CI bound |
| `\DetEditRTTwoEFourHi` | 0.97 | mean AUROC over hosted victims, R T2, edit type E4, upper 95% CI bound |
| `\DetEditRTTwoEFourCI` | [0.94, 0.97] | mean AUROC over hosted victims, R T2, edit type E4, 95% CI |
| `\DetEditRTTwoEFourN` | 596 | mean AUROC over hosted victims, R T2, edit type E4, n |
| `\DetEditRTTwoEFourP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T2, edit type E4, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRTTwoEFive` | 0.96 | mean AUROC over hosted victims, R T2, edit type E5 |
| `\DetEditRTTwoEFiveLo` | 0.95 | mean AUROC over hosted victims, R T2, edit type E5, lower 95% CI bound |
| `\DetEditRTTwoEFiveHi` | 0.98 | mean AUROC over hosted victims, R T2, edit type E5, upper 95% CI bound |
| `\DetEditRTTwoEFiveCI` | [0.95, 0.98] | mean AUROC over hosted victims, R T2, edit type E5, 95% CI |
| `\DetEditRTTwoEFiveN` | 578 | mean AUROC over hosted victims, R T2, edit type E5, n |
| `\DetEditRTTwoEFiveP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T2, edit type E5, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRTThreeEOne` | 0.93 | mean AUROC over hosted victims, R T3, edit type E1 |
| `\DetEditRTThreeEOneLo` | 0.92 | mean AUROC over hosted victims, R T3, edit type E1, lower 95% CI bound |
| `\DetEditRTThreeEOneHi` | 0.95 | mean AUROC over hosted victims, R T3, edit type E1, upper 95% CI bound |
| `\DetEditRTThreeEOneCI` | [0.92, 0.95] | mean AUROC over hosted victims, R T3, edit type E1, 95% CI |
| `\DetEditRTThreeEOneN` | 597 | mean AUROC over hosted victims, R T3, edit type E1, n |
| `\DetEditRTThreeEOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T3, edit type E1, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRTThreeETwo` | 0.96 | mean AUROC over hosted victims, R T3, edit type E2 |
| `\DetEditRTThreeETwoLo` | 0.94 | mean AUROC over hosted victims, R T3, edit type E2, lower 95% CI bound |
| `\DetEditRTThreeETwoHi` | 0.97 | mean AUROC over hosted victims, R T3, edit type E2, upper 95% CI bound |
| `\DetEditRTThreeETwoCI` | [0.94, 0.97] | mean AUROC over hosted victims, R T3, edit type E2, 95% CI |
| `\DetEditRTThreeETwoN` | 587 | mean AUROC over hosted victims, R T3, edit type E2, n |
| `\DetEditRTThreeETwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T3, edit type E2, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRTThreeEThree` | 0.95 | mean AUROC over hosted victims, R T3, edit type E3 |
| `\DetEditRTThreeEThreeLo` | 0.94 | mean AUROC over hosted victims, R T3, edit type E3, lower 95% CI bound |
| `\DetEditRTThreeEThreeHi` | 0.96 | mean AUROC over hosted victims, R T3, edit type E3, upper 95% CI bound |
| `\DetEditRTThreeEThreeCI` | [0.94, 0.96] | mean AUROC over hosted victims, R T3, edit type E3, 95% CI |
| `\DetEditRTThreeEThreeN` | 599 | mean AUROC over hosted victims, R T3, edit type E3, n |
| `\DetEditRTThreeEThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T3, edit type E3, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRTThreeEFour` | 0.96 | mean AUROC over hosted victims, R T3, edit type E4 |
| `\DetEditRTThreeEFourLo` | 0.94 | mean AUROC over hosted victims, R T3, edit type E4, lower 95% CI bound |
| `\DetEditRTThreeEFourHi` | 0.97 | mean AUROC over hosted victims, R T3, edit type E4, upper 95% CI bound |
| `\DetEditRTThreeEFourCI` | [0.94, 0.97] | mean AUROC over hosted victims, R T3, edit type E4, 95% CI |
| `\DetEditRTThreeEFourN` | 597 | mean AUROC over hosted victims, R T3, edit type E4, n |
| `\DetEditRTThreeEFourP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T3, edit type E4, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRTThreeEFive` | 0.96 | mean AUROC over hosted victims, R T3, edit type E5 |
| `\DetEditRTThreeEFiveLo` | 0.95 | mean AUROC over hosted victims, R T3, edit type E5, lower 95% CI bound |
| `\DetEditRTThreeEFiveHi` | 0.98 | mean AUROC over hosted victims, R T3, edit type E5, upper 95% CI bound |
| `\DetEditRTThreeEFiveCI` | [0.95, 0.98] | mean AUROC over hosted victims, R T3, edit type E5, 95% CI |
| `\DetEditRTThreeEFiveN` | 597 | mean AUROC over hosted victims, R T3, edit type E5, n |
| `\DetEditRTThreeEFiveP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T3, edit type E5, two-sided bootstrap p (n/a if not tested) |
| `\DetEditVTZeroEOne` | 0.49 | mean AUROC over hosted victims, V T0, edit type E1 |
| `\DetEditVTZeroEOneLo` | 0.47 | mean AUROC over hosted victims, V T0, edit type E1, lower 95% CI bound |
| `\DetEditVTZeroEOneHi` | 0.52 | mean AUROC over hosted victims, V T0, edit type E1, upper 95% CI bound |
| `\DetEditVTZeroEOneCI` | [0.47, 0.52] | mean AUROC over hosted victims, V T0, edit type E1, 95% CI |
| `\DetEditVTZeroEOneN` | 591 | mean AUROC over hosted victims, V T0, edit type E1, n |
| `\DetEditVTZeroEOneP` | 0.628 | mean AUROC over hosted victims, V T0, edit type E1, two-sided bootstrap p (n/a if not tested) |
| `\DetEditVTZeroETwo` | 0.88 | mean AUROC over hosted victims, V T0, edit type E2 |
| `\DetEditVTZeroETwoLo` | 0.86 | mean AUROC over hosted victims, V T0, edit type E2, lower 95% CI bound |
| `\DetEditVTZeroETwoHi` | 0.90 | mean AUROC over hosted victims, V T0, edit type E2, upper 95% CI bound |
| `\DetEditVTZeroETwoCI` | [0.86, 0.90] | mean AUROC over hosted victims, V T0, edit type E2, 95% CI |
| `\DetEditVTZeroETwoN` | 591 | mean AUROC over hosted victims, V T0, edit type E2, n |
| `\DetEditVTZeroETwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T0, edit type E2, two-sided bootstrap p (n/a if not tested) |
| `\DetEditVTZeroEThree` | 0.87 | mean AUROC over hosted victims, V T0, edit type E3 |
| `\DetEditVTZeroEThreeLo` | 0.85 | mean AUROC over hosted victims, V T0, edit type E3, lower 95% CI bound |
| `\DetEditVTZeroEThreeHi` | 0.90 | mean AUROC over hosted victims, V T0, edit type E3, upper 95% CI bound |
| `\DetEditVTZeroEThreeCI` | [0.85, 0.90] | mean AUROC over hosted victims, V T0, edit type E3, 95% CI |
| `\DetEditVTZeroEThreeN` | 591 | mean AUROC over hosted victims, V T0, edit type E3, n |
| `\DetEditVTZeroEThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T0, edit type E3, two-sided bootstrap p (n/a if not tested) |
| `\DetEditVTZeroEFour` | 0.93 | mean AUROC over hosted victims, V T0, edit type E4 |
| `\DetEditVTZeroEFourLo` | 0.91 | mean AUROC over hosted victims, V T0, edit type E4, lower 95% CI bound |
| `\DetEditVTZeroEFourHi` | 0.95 | mean AUROC over hosted victims, V T0, edit type E4, upper 95% CI bound |
| `\DetEditVTZeroEFourCI` | [0.91, 0.95] | mean AUROC over hosted victims, V T0, edit type E4, 95% CI |
| `\DetEditVTZeroEFourN` | 590 | mean AUROC over hosted victims, V T0, edit type E4, n |
| `\DetEditVTZeroEFourP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T0, edit type E4, two-sided bootstrap p (n/a if not tested) |
| `\DetEditVTZeroEFive` | 0.81 | mean AUROC over hosted victims, V T0, edit type E5 |
| `\DetEditVTZeroEFiveLo` | 0.78 | mean AUROC over hosted victims, V T0, edit type E5, lower 95% CI bound |
| `\DetEditVTZeroEFiveHi` | 0.84 | mean AUROC over hosted victims, V T0, edit type E5, upper 95% CI bound |
| `\DetEditVTZeroEFiveCI` | [0.78, 0.84] | mean AUROC over hosted victims, V T0, edit type E5, 95% CI |
| `\DetEditVTZeroEFiveN` | 590 | mean AUROC over hosted victims, V T0, edit type E5, n |
| `\DetEditVTZeroEFiveP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T0, edit type E5, two-sided bootstrap p (n/a if not tested) |
| `\DetEditVTOneEOne` | 0.51 | mean AUROC over hosted victims, V T1, edit type E1 |
| `\DetEditVTOneEOneLo` | 0.48 | mean AUROC over hosted victims, V T1, edit type E1, lower 95% CI bound |
| `\DetEditVTOneEOneHi` | 0.53 | mean AUROC over hosted victims, V T1, edit type E1, upper 95% CI bound |
| `\DetEditVTOneEOneCI` | [0.48, 0.53] | mean AUROC over hosted victims, V T1, edit type E1, 95% CI |
| `\DetEditVTOneEOneN` | 588 | mean AUROC over hosted victims, V T1, edit type E1, n |
| `\DetEditVTOneEOneP` | 0.605 | mean AUROC over hosted victims, V T1, edit type E1, two-sided bootstrap p (n/a if not tested) |
| `\DetEditVTOneETwo` | 0.79 | mean AUROC over hosted victims, V T1, edit type E2 |
| `\DetEditVTOneETwoLo` | 0.76 | mean AUROC over hosted victims, V T1, edit type E2, lower 95% CI bound |
| `\DetEditVTOneETwoHi` | 0.81 | mean AUROC over hosted victims, V T1, edit type E2, upper 95% CI bound |
| `\DetEditVTOneETwoCI` | [0.76, 0.81] | mean AUROC over hosted victims, V T1, edit type E2, 95% CI |
| `\DetEditVTOneETwoN` | 591 | mean AUROC over hosted victims, V T1, edit type E2, n |
| `\DetEditVTOneETwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T1, edit type E2, two-sided bootstrap p (n/a if not tested) |
| `\DetEditVTOneEThree` | 0.62 | mean AUROC over hosted victims, V T1, edit type E3 |
| `\DetEditVTOneEThreeLo` | 0.59 | mean AUROC over hosted victims, V T1, edit type E3, lower 95% CI bound |
| `\DetEditVTOneEThreeHi` | 0.65 | mean AUROC over hosted victims, V T1, edit type E3, upper 95% CI bound |
| `\DetEditVTOneEThreeCI` | [0.59, 0.65] | mean AUROC over hosted victims, V T1, edit type E3, 95% CI |
| `\DetEditVTOneEThreeN` | 591 | mean AUROC over hosted victims, V T1, edit type E3, n |
| `\DetEditVTOneEThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T1, edit type E3, two-sided bootstrap p (n/a if not tested) |
| `\DetEditVTOneEFour` | 0.66 | mean AUROC over hosted victims, V T1, edit type E4 |
| `\DetEditVTOneEFourLo` | 0.63 | mean AUROC over hosted victims, V T1, edit type E4, lower 95% CI bound |
| `\DetEditVTOneEFourHi` | 0.68 | mean AUROC over hosted victims, V T1, edit type E4, upper 95% CI bound |
| `\DetEditVTOneEFourCI` | [0.63, 0.68] | mean AUROC over hosted victims, V T1, edit type E4, 95% CI |
| `\DetEditVTOneEFourN` | 590 | mean AUROC over hosted victims, V T1, edit type E4, n |
| `\DetEditVTOneEFourP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T1, edit type E4, two-sided bootstrap p (n/a if not tested) |
| `\DetEditVTOneEFive` | 0.54 | mean AUROC over hosted victims, V T1, edit type E5 |
| `\DetEditVTOneEFiveLo` | 0.52 | mean AUROC over hosted victims, V T1, edit type E5, lower 95% CI bound |
| `\DetEditVTOneEFiveHi` | 0.57 | mean AUROC over hosted victims, V T1, edit type E5, upper 95% CI bound |
| `\DetEditVTOneEFiveCI` | [0.52, 0.57] | mean AUROC over hosted victims, V T1, edit type E5, 95% CI |
| `\DetEditVTOneEFiveN` | 548 | mean AUROC over hosted victims, V T1, edit type E5, n |
| `\DetEditVTOneEFiveP` | 0.002 | mean AUROC over hosted victims, V T1, edit type E5, two-sided bootstrap p (n/a if not tested) |
| `\DetEditVTTwoEOne` | 0.50 | mean AUROC over hosted victims, V T2, edit type E1 |
| `\DetEditVTTwoEOneLo` | 0.48 | mean AUROC over hosted victims, V T2, edit type E1, lower 95% CI bound |
| `\DetEditVTTwoEOneHi` | 0.53 | mean AUROC over hosted victims, V T2, edit type E1, upper 95% CI bound |
| `\DetEditVTTwoEOneCI` | [0.48, 0.53] | mean AUROC over hosted victims, V T2, edit type E1, 95% CI |
| `\DetEditVTTwoEOneN` | 589 | mean AUROC over hosted victims, V T2, edit type E1, n |
| `\DetEditVTTwoEOneP` | 0.933 | mean AUROC over hosted victims, V T2, edit type E1, two-sided bootstrap p (n/a if not tested) |
| `\DetEditVTTwoETwo` | 0.81 | mean AUROC over hosted victims, V T2, edit type E2 |
| `\DetEditVTTwoETwoLo` | 0.78 | mean AUROC over hosted victims, V T2, edit type E2, lower 95% CI bound |
| `\DetEditVTTwoETwoHi` | 0.84 | mean AUROC over hosted victims, V T2, edit type E2, upper 95% CI bound |
| `\DetEditVTTwoETwoCI` | [0.78, 0.84] | mean AUROC over hosted victims, V T2, edit type E2, 95% CI |
| `\DetEditVTTwoETwoN` | 569 | mean AUROC over hosted victims, V T2, edit type E2, n |
| `\DetEditVTTwoETwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T2, edit type E2, two-sided bootstrap p (n/a if not tested) |
| `\DetEditVTTwoEThree` | 0.63 | mean AUROC over hosted victims, V T2, edit type E3 |
| `\DetEditVTTwoEThreeLo` | 0.60 | mean AUROC over hosted victims, V T2, edit type E3, lower 95% CI bound |
| `\DetEditVTTwoEThreeHi` | 0.66 | mean AUROC over hosted victims, V T2, edit type E3, upper 95% CI bound |
| `\DetEditVTTwoEThreeCI` | [0.60, 0.66] | mean AUROC over hosted victims, V T2, edit type E3, 95% CI |
| `\DetEditVTTwoEThreeN` | 591 | mean AUROC over hosted victims, V T2, edit type E3, n |
| `\DetEditVTTwoEThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T2, edit type E3, two-sided bootstrap p (n/a if not tested) |
| `\DetEditVTTwoEFour` | 0.66 | mean AUROC over hosted victims, V T2, edit type E4 |
| `\DetEditVTTwoEFourLo` | 0.64 | mean AUROC over hosted victims, V T2, edit type E4, lower 95% CI bound |
| `\DetEditVTTwoEFourHi` | 0.69 | mean AUROC over hosted victims, V T2, edit type E4, upper 95% CI bound |
| `\DetEditVTTwoEFourCI` | [0.64, 0.69] | mean AUROC over hosted victims, V T2, edit type E4, 95% CI |
| `\DetEditVTTwoEFourN` | 591 | mean AUROC over hosted victims, V T2, edit type E4, n |
| `\DetEditVTTwoEFourP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T2, edit type E4, two-sided bootstrap p (n/a if not tested) |
| `\DetEditVTTwoEFive` | 0.53 | mean AUROC over hosted victims, V T2, edit type E5 |
| `\DetEditVTTwoEFiveLo` | 0.50 | mean AUROC over hosted victims, V T2, edit type E5, lower 95% CI bound |
| `\DetEditVTTwoEFiveHi` | 0.55 | mean AUROC over hosted victims, V T2, edit type E5, upper 95% CI bound |
| `\DetEditVTTwoEFiveCI` | [0.50, 0.55] | mean AUROC over hosted victims, V T2, edit type E5, 95% CI |
| `\DetEditVTTwoEFiveN` | 571 | mean AUROC over hosted victims, V T2, edit type E5, n |
| `\DetEditVTTwoEFiveP` | 0.076 | mean AUROC over hosted victims, V T2, edit type E5, two-sided bootstrap p (n/a if not tested) |
| `\DetEditVTThreeEOne` | 0.49 | mean AUROC over hosted victims, V T3, edit type E1 |
| `\DetEditVTThreeEOneLo` | 0.46 | mean AUROC over hosted victims, V T3, edit type E1, lower 95% CI bound |
| `\DetEditVTThreeEOneHi` | 0.51 | mean AUROC over hosted victims, V T3, edit type E1, upper 95% CI bound |
| `\DetEditVTThreeEOneCI` | [0.46, 0.51] | mean AUROC over hosted victims, V T3, edit type E1, 95% CI |
| `\DetEditVTThreeEOneN` | 590 | mean AUROC over hosted victims, V T3, edit type E1, n |
| `\DetEditVTThreeEOneP` | 0.305 | mean AUROC over hosted victims, V T3, edit type E1, two-sided bootstrap p (n/a if not tested) |
| `\DetEditVTThreeETwo` | 0.77 | mean AUROC over hosted victims, V T3, edit type E2 |
| `\DetEditVTThreeETwoLo` | 0.74 | mean AUROC over hosted victims, V T3, edit type E2, lower 95% CI bound |
| `\DetEditVTThreeETwoHi` | 0.80 | mean AUROC over hosted victims, V T3, edit type E2, upper 95% CI bound |
| `\DetEditVTThreeETwoCI` | [0.74, 0.80] | mean AUROC over hosted victims, V T3, edit type E2, 95% CI |
| `\DetEditVTThreeETwoN` | 582 | mean AUROC over hosted victims, V T3, edit type E2, n |
| `\DetEditVTThreeETwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T3, edit type E2, two-sided bootstrap p (n/a if not tested) |
| `\DetEditVTThreeEThree` | 0.62 | mean AUROC over hosted victims, V T3, edit type E3 |
| `\DetEditVTThreeEThreeLo` | 0.59 | mean AUROC over hosted victims, V T3, edit type E3, lower 95% CI bound |
| `\DetEditVTThreeEThreeHi` | 0.65 | mean AUROC over hosted victims, V T3, edit type E3, upper 95% CI bound |
| `\DetEditVTThreeEThreeCI` | [0.59, 0.65] | mean AUROC over hosted victims, V T3, edit type E3, 95% CI |
| `\DetEditVTThreeEThreeN` | 591 | mean AUROC over hosted victims, V T3, edit type E3, n |
| `\DetEditVTThreeEThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T3, edit type E3, two-sided bootstrap p (n/a if not tested) |
| `\DetEditVTThreeEFour` | 0.63 | mean AUROC over hosted victims, V T3, edit type E4 |
| `\DetEditVTThreeEFourLo` | 0.60 | mean AUROC over hosted victims, V T3, edit type E4, lower 95% CI bound |
| `\DetEditVTThreeEFourHi` | 0.66 | mean AUROC over hosted victims, V T3, edit type E4, upper 95% CI bound |
| `\DetEditVTThreeEFourCI` | [0.60, 0.66] | mean AUROC over hosted victims, V T3, edit type E4, 95% CI |
| `\DetEditVTThreeEFourN` | 591 | mean AUROC over hosted victims, V T3, edit type E4, n |
| `\DetEditVTThreeEFourP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T3, edit type E4, two-sided bootstrap p (n/a if not tested) |
| `\DetEditVTThreeEFive` | 0.51 | mean AUROC over hosted victims, V T3, edit type E5 |
| `\DetEditVTThreeEFiveLo` | 0.48 | mean AUROC over hosted victims, V T3, edit type E5, lower 95% CI bound |
| `\DetEditVTThreeEFiveHi` | 0.54 | mean AUROC over hosted victims, V T3, edit type E5, upper 95% CI bound |
| `\DetEditVTThreeEFiveCI` | [0.48, 0.54] | mean AUROC over hosted victims, V T3, edit type E5, 95% CI |
| `\DetEditVTThreeEFiveN` | 588 | mean AUROC over hosted victims, V T3, edit type E5, n |
| `\DetEditVTThreeEFiveP` | 0.575 | mean AUROC over hosted victims, V T3, edit type E5, two-sided bootstrap p (n/a if not tested) |
| `\DetEditFTraceTZeroEOne` | 0.92 | mean AUROC over hosted victims, f_trace T0, edit type E1 |
| `\DetEditFTraceTZeroEOneLo` | 0.90 | mean AUROC over hosted victims, f_trace T0, edit type E1, lower 95% CI bound |
| `\DetEditFTraceTZeroEOneHi` | 0.94 | mean AUROC over hosted victims, f_trace T0, edit type E1, upper 95% CI bound |
| `\DetEditFTraceTZeroEOneCI` | [0.90, 0.94] | mean AUROC over hosted victims, f_trace T0, edit type E1, 95% CI |
| `\DetEditFTraceTZeroEOneN` | 600 | mean AUROC over hosted victims, f_trace T0, edit type E1, n |
| `\DetEditFTraceTZeroEOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T0, edit type E1, two-sided bootstrap p (n/a if not tested) |
| `\DetEditFTraceTZeroETwo` | 0.71 | mean AUROC over hosted victims, f_trace T0, edit type E2 |
| `\DetEditFTraceTZeroETwoLo` | 0.69 | mean AUROC over hosted victims, f_trace T0, edit type E2, lower 95% CI bound |
| `\DetEditFTraceTZeroETwoHi` | 0.74 | mean AUROC over hosted victims, f_trace T0, edit type E2, upper 95% CI bound |
| `\DetEditFTraceTZeroETwoCI` | [0.69, 0.74] | mean AUROC over hosted victims, f_trace T0, edit type E2, 95% CI |
| `\DetEditFTraceTZeroETwoN` | 596 | mean AUROC over hosted victims, f_trace T0, edit type E2, n |
| `\DetEditFTraceTZeroETwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T0, edit type E2, two-sided bootstrap p (n/a if not tested) |
| `\DetEditFTraceTZeroEThree` | 0.60 | mean AUROC over hosted victims, f_trace T0, edit type E3 |
| `\DetEditFTraceTZeroEThreeLo` | 0.58 | mean AUROC over hosted victims, f_trace T0, edit type E3, lower 95% CI bound |
| `\DetEditFTraceTZeroEThreeHi` | 0.63 | mean AUROC over hosted victims, f_trace T0, edit type E3, upper 95% CI bound |
| `\DetEditFTraceTZeroEThreeCI` | [0.58, 0.63] | mean AUROC over hosted victims, f_trace T0, edit type E3, 95% CI |
| `\DetEditFTraceTZeroEThreeN` | 600 | mean AUROC over hosted victims, f_trace T0, edit type E3, n |
| `\DetEditFTraceTZeroEThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T0, edit type E3, two-sided bootstrap p (n/a if not tested) |
| `\DetEditFTraceTZeroEFour` | 0.56 | mean AUROC over hosted victims, f_trace T0, edit type E4 |
| `\DetEditFTraceTZeroEFourLo` | 0.54 | mean AUROC over hosted victims, f_trace T0, edit type E4, lower 95% CI bound |
| `\DetEditFTraceTZeroEFourHi` | 0.58 | mean AUROC over hosted victims, f_trace T0, edit type E4, upper 95% CI bound |
| `\DetEditFTraceTZeroEFourCI` | [0.54, 0.58] | mean AUROC over hosted victims, f_trace T0, edit type E4, 95% CI |
| `\DetEditFTraceTZeroEFourN` | 600 | mean AUROC over hosted victims, f_trace T0, edit type E4, n |
| `\DetEditFTraceTZeroEFourP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T0, edit type E4, two-sided bootstrap p (n/a if not tested) |
| `\DetEditFTraceTZeroEFive` | 0.50 | mean AUROC over hosted victims, f_trace T0, edit type E5 |
| `\DetEditFTraceTZeroEFiveLo` | 0.50 | mean AUROC over hosted victims, f_trace T0, edit type E5, lower 95% CI bound |
| `\DetEditFTraceTZeroEFiveHi` | 0.50 | mean AUROC over hosted victims, f_trace T0, edit type E5, upper 95% CI bound |
| `\DetEditFTraceTZeroEFiveCI` | [0.50, 0.50] | mean AUROC over hosted victims, f_trace T0, edit type E5, 95% CI |
| `\DetEditFTraceTZeroEFiveN` | 600 | mean AUROC over hosted victims, f_trace T0, edit type E5, n |
| `\DetEditFTraceTZeroEFiveP` | 0.922 | mean AUROC over hosted victims, f_trace T0, edit type E5, two-sided bootstrap p (n/a if not tested) |
| `\DetEditFTraceTOneEOne` | 0.92 | mean AUROC over hosted victims, f_trace T1, edit type E1 |
| `\DetEditFTraceTOneEOneLo` | 0.90 | mean AUROC over hosted victims, f_trace T1, edit type E1, lower 95% CI bound |
| `\DetEditFTraceTOneEOneHi` | 0.94 | mean AUROC over hosted victims, f_trace T1, edit type E1, upper 95% CI bound |
| `\DetEditFTraceTOneEOneCI` | [0.90, 0.94] | mean AUROC over hosted victims, f_trace T1, edit type E1, 95% CI |
| `\DetEditFTraceTOneEOneN` | 598 | mean AUROC over hosted victims, f_trace T1, edit type E1, n |
| `\DetEditFTraceTOneEOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T1, edit type E1, two-sided bootstrap p (n/a if not tested) |
| `\DetEditFTraceTOneETwo` | 0.73 | mean AUROC over hosted victims, f_trace T1, edit type E2 |
| `\DetEditFTraceTOneETwoLo` | 0.70 | mean AUROC over hosted victims, f_trace T1, edit type E2, lower 95% CI bound |
| `\DetEditFTraceTOneETwoHi` | 0.76 | mean AUROC over hosted victims, f_trace T1, edit type E2, upper 95% CI bound |
| `\DetEditFTraceTOneETwoCI` | [0.70, 0.76] | mean AUROC over hosted victims, f_trace T1, edit type E2, 95% CI |
| `\DetEditFTraceTOneETwoN` | 596 | mean AUROC over hosted victims, f_trace T1, edit type E2, n |
| `\DetEditFTraceTOneETwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T1, edit type E2, two-sided bootstrap p (n/a if not tested) |
| `\DetEditFTraceTOneEThree` | 0.60 | mean AUROC over hosted victims, f_trace T1, edit type E3 |
| `\DetEditFTraceTOneEThreeLo` | 0.58 | mean AUROC over hosted victims, f_trace T1, edit type E3, lower 95% CI bound |
| `\DetEditFTraceTOneEThreeHi` | 0.63 | mean AUROC over hosted victims, f_trace T1, edit type E3, upper 95% CI bound |
| `\DetEditFTraceTOneEThreeCI` | [0.58, 0.63] | mean AUROC over hosted victims, f_trace T1, edit type E3, 95% CI |
| `\DetEditFTraceTOneEThreeN` | 600 | mean AUROC over hosted victims, f_trace T1, edit type E3, n |
| `\DetEditFTraceTOneEThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T1, edit type E3, two-sided bootstrap p (n/a if not tested) |
| `\DetEditFTraceTOneEFour` | 0.54 | mean AUROC over hosted victims, f_trace T1, edit type E4 |
| `\DetEditFTraceTOneEFourLo` | 0.52 | mean AUROC over hosted victims, f_trace T1, edit type E4, lower 95% CI bound |
| `\DetEditFTraceTOneEFourHi` | 0.57 | mean AUROC over hosted victims, f_trace T1, edit type E4, upper 95% CI bound |
| `\DetEditFTraceTOneEFourCI` | [0.52, 0.57] | mean AUROC over hosted victims, f_trace T1, edit type E4, 95% CI |
| `\DetEditFTraceTOneEFourN` | 600 | mean AUROC over hosted victims, f_trace T1, edit type E4, n |
| `\DetEditFTraceTOneEFourP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T1, edit type E4, two-sided bootstrap p (n/a if not tested) |
| `\DetEditFTraceTOneEFive` | 0.50 | mean AUROC over hosted victims, f_trace T1, edit type E5 |
| `\DetEditFTraceTOneEFiveLo` | 0.49 | mean AUROC over hosted victims, f_trace T1, edit type E5, lower 95% CI bound |
| `\DetEditFTraceTOneEFiveHi` | 0.51 | mean AUROC over hosted victims, f_trace T1, edit type E5, upper 95% CI bound |
| `\DetEditFTraceTOneEFiveCI` | [0.49, 0.51] | mean AUROC over hosted victims, f_trace T1, edit type E5, 95% CI |
| `\DetEditFTraceTOneEFiveN` | 558 | mean AUROC over hosted victims, f_trace T1, edit type E5, n |
| `\DetEditFTraceTOneEFiveP` | 0.853 | mean AUROC over hosted victims, f_trace T1, edit type E5, two-sided bootstrap p (n/a if not tested) |
| `\DetEditFTraceTTwoEOne` | 0.92 | mean AUROC over hosted victims, f_trace T2, edit type E1 |
| `\DetEditFTraceTTwoEOneLo` | 0.90 | mean AUROC over hosted victims, f_trace T2, edit type E1, lower 95% CI bound |
| `\DetEditFTraceTTwoEOneHi` | 0.94 | mean AUROC over hosted victims, f_trace T2, edit type E1, upper 95% CI bound |
| `\DetEditFTraceTTwoEOneCI` | [0.90, 0.94] | mean AUROC over hosted victims, f_trace T2, edit type E1, 95% CI |
| `\DetEditFTraceTTwoEOneN` | 598 | mean AUROC over hosted victims, f_trace T2, edit type E1, n |
| `\DetEditFTraceTTwoEOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T2, edit type E1, two-sided bootstrap p (n/a if not tested) |
| `\DetEditFTraceTTwoETwo` | 0.77 | mean AUROC over hosted victims, f_trace T2, edit type E2 |
| `\DetEditFTraceTTwoETwoLo` | 0.75 | mean AUROC over hosted victims, f_trace T2, edit type E2, lower 95% CI bound |
| `\DetEditFTraceTTwoETwoHi` | 0.80 | mean AUROC over hosted victims, f_trace T2, edit type E2, upper 95% CI bound |
| `\DetEditFTraceTTwoETwoCI` | [0.75, 0.80] | mean AUROC over hosted victims, f_trace T2, edit type E2, 95% CI |
| `\DetEditFTraceTTwoETwoN` | 574 | mean AUROC over hosted victims, f_trace T2, edit type E2, n |
| `\DetEditFTraceTTwoETwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T2, edit type E2, two-sided bootstrap p (n/a if not tested) |
| `\DetEditFTraceTTwoEThree` | 0.59 | mean AUROC over hosted victims, f_trace T2, edit type E3 |
| `\DetEditFTraceTTwoEThreeLo` | 0.57 | mean AUROC over hosted victims, f_trace T2, edit type E3, lower 95% CI bound |
| `\DetEditFTraceTTwoEThreeHi` | 0.62 | mean AUROC over hosted victims, f_trace T2, edit type E3, upper 95% CI bound |
| `\DetEditFTraceTTwoEThreeCI` | [0.57, 0.62] | mean AUROC over hosted victims, f_trace T2, edit type E3, 95% CI |
| `\DetEditFTraceTTwoEThreeN` | 600 | mean AUROC over hosted victims, f_trace T2, edit type E3, n |
| `\DetEditFTraceTTwoEThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T2, edit type E3, two-sided bootstrap p (n/a if not tested) |
| `\DetEditFTraceTTwoEFour` | 0.55 | mean AUROC over hosted victims, f_trace T2, edit type E4 |
| `\DetEditFTraceTTwoEFourLo` | 0.53 | mean AUROC over hosted victims, f_trace T2, edit type E4, lower 95% CI bound |
| `\DetEditFTraceTTwoEFourHi` | 0.57 | mean AUROC over hosted victims, f_trace T2, edit type E4, upper 95% CI bound |
| `\DetEditFTraceTTwoEFourCI` | [0.53, 0.57] | mean AUROC over hosted victims, f_trace T2, edit type E4, 95% CI |
| `\DetEditFTraceTTwoEFourN` | 600 | mean AUROC over hosted victims, f_trace T2, edit type E4, n |
| `\DetEditFTraceTTwoEFourP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T2, edit type E4, two-sided bootstrap p (n/a if not tested) |
| `\DetEditFTraceTTwoEFive` | 0.50 | mean AUROC over hosted victims, f_trace T2, edit type E5 |
| `\DetEditFTraceTTwoEFiveLo` | 0.49 | mean AUROC over hosted victims, f_trace T2, edit type E5, lower 95% CI bound |
| `\DetEditFTraceTTwoEFiveHi` | 0.51 | mean AUROC over hosted victims, f_trace T2, edit type E5, upper 95% CI bound |
| `\DetEditFTraceTTwoEFiveCI` | [0.49, 0.51] | mean AUROC over hosted victims, f_trace T2, edit type E5, 95% CI |
| `\DetEditFTraceTTwoEFiveN` | 580 | mean AUROC over hosted victims, f_trace T2, edit type E5, n |
| `\DetEditFTraceTTwoEFiveP` | 0.546 | mean AUROC over hosted victims, f_trace T2, edit type E5, two-sided bootstrap p (n/a if not tested) |
| `\DetEditFTraceTThreeEOne` | 0.92 | mean AUROC over hosted victims, f_trace T3, edit type E1 |
| `\DetEditFTraceTThreeEOneLo` | 0.90 | mean AUROC over hosted victims, f_trace T3, edit type E1, lower 95% CI bound |
| `\DetEditFTraceTThreeEOneHi` | 0.94 | mean AUROC over hosted victims, f_trace T3, edit type E1, upper 95% CI bound |
| `\DetEditFTraceTThreeEOneCI` | [0.90, 0.94] | mean AUROC over hosted victims, f_trace T3, edit type E1, 95% CI |
| `\DetEditFTraceTThreeEOneN` | 600 | mean AUROC over hosted victims, f_trace T3, edit type E1, n |
| `\DetEditFTraceTThreeEOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T3, edit type E1, two-sided bootstrap p (n/a if not tested) |
| `\DetEditFTraceTThreeETwo` | 0.78 | mean AUROC over hosted victims, f_trace T3, edit type E2 |
| `\DetEditFTraceTThreeETwoLo` | 0.75 | mean AUROC over hosted victims, f_trace T3, edit type E2, lower 95% CI bound |
| `\DetEditFTraceTThreeETwoHi` | 0.80 | mean AUROC over hosted victims, f_trace T3, edit type E2, upper 95% CI bound |
| `\DetEditFTraceTThreeETwoCI` | [0.75, 0.80] | mean AUROC over hosted victims, f_trace T3, edit type E2, 95% CI |
| `\DetEditFTraceTThreeETwoN` | 588 | mean AUROC over hosted victims, f_trace T3, edit type E2, n |
| `\DetEditFTraceTThreeETwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T3, edit type E2, two-sided bootstrap p (n/a if not tested) |
| `\DetEditFTraceTThreeEThree` | 0.60 | mean AUROC over hosted victims, f_trace T3, edit type E3 |
| `\DetEditFTraceTThreeEThreeLo` | 0.57 | mean AUROC over hosted victims, f_trace T3, edit type E3, lower 95% CI bound |
| `\DetEditFTraceTThreeEThreeHi` | 0.63 | mean AUROC over hosted victims, f_trace T3, edit type E3, upper 95% CI bound |
| `\DetEditFTraceTThreeEThreeCI` | [0.57, 0.63] | mean AUROC over hosted victims, f_trace T3, edit type E3, 95% CI |
| `\DetEditFTraceTThreeEThreeN` | 600 | mean AUROC over hosted victims, f_trace T3, edit type E3, n |
| `\DetEditFTraceTThreeEThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T3, edit type E3, two-sided bootstrap p (n/a if not tested) |
| `\DetEditFTraceTThreeEFour` | 0.57 | mean AUROC over hosted victims, f_trace T3, edit type E4 |
| `\DetEditFTraceTThreeEFourLo` | 0.55 | mean AUROC over hosted victims, f_trace T3, edit type E4, lower 95% CI bound |
| `\DetEditFTraceTThreeEFourHi` | 0.59 | mean AUROC over hosted victims, f_trace T3, edit type E4, upper 95% CI bound |
| `\DetEditFTraceTThreeEFourCI` | [0.55, 0.59] | mean AUROC over hosted victims, f_trace T3, edit type E4, 95% CI |
| `\DetEditFTraceTThreeEFourN` | 600 | mean AUROC over hosted victims, f_trace T3, edit type E4, n |
| `\DetEditFTraceTThreeEFourP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T3, edit type E4, two-sided bootstrap p (n/a if not tested) |
| `\DetEditFTraceTThreeEFive` | 0.50 | mean AUROC over hosted victims, f_trace T3, edit type E5 |
| `\DetEditFTraceTThreeEFiveLo` | 0.49 | mean AUROC over hosted victims, f_trace T3, edit type E5, lower 95% CI bound |
| `\DetEditFTraceTThreeEFiveHi` | 0.51 | mean AUROC over hosted victims, f_trace T3, edit type E5, upper 95% CI bound |
| `\DetEditFTraceTThreeEFiveCI` | [0.49, 0.51] | mean AUROC over hosted victims, f_trace T3, edit type E5, 95% CI |
| `\DetEditFTraceTThreeEFiveN` | 598 | mean AUROC over hosted victims, f_trace T3, edit type E5, n |
| `\DetEditFTraceTThreeEFiveP` | 0.999 | mean AUROC over hosted victims, f_trace T3, edit type E5, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRFieldTZeroEOne` | 0.85 | mean AUROC over hosted victims, r_field T0, edit type E1 |
| `\DetEditRFieldTZeroEOneLo` | 0.83 | mean AUROC over hosted victims, r_field T0, edit type E1, lower 95% CI bound |
| `\DetEditRFieldTZeroEOneHi` | 0.87 | mean AUROC over hosted victims, r_field T0, edit type E1, upper 95% CI bound |
| `\DetEditRFieldTZeroEOneCI` | [0.83, 0.87] | mean AUROC over hosted victims, r_field T0, edit type E1, 95% CI |
| `\DetEditRFieldTZeroEOneN` | 598 | mean AUROC over hosted victims, r_field T0, edit type E1, n |
| `\DetEditRFieldTZeroEOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T0, edit type E1, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRFieldTZeroETwo` | 0.69 | mean AUROC over hosted victims, r_field T0, edit type E2 |
| `\DetEditRFieldTZeroETwoLo` | 0.67 | mean AUROC over hosted victims, r_field T0, edit type E2, lower 95% CI bound |
| `\DetEditRFieldTZeroETwoHi` | 0.72 | mean AUROC over hosted victims, r_field T0, edit type E2, upper 95% CI bound |
| `\DetEditRFieldTZeroETwoCI` | [0.67, 0.72] | mean AUROC over hosted victims, r_field T0, edit type E2, 95% CI |
| `\DetEditRFieldTZeroETwoN` | 596 | mean AUROC over hosted victims, r_field T0, edit type E2, n |
| `\DetEditRFieldTZeroETwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T0, edit type E2, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRFieldTZeroEThree` | 0.60 | mean AUROC over hosted victims, r_field T0, edit type E3 |
| `\DetEditRFieldTZeroEThreeLo` | 0.58 | mean AUROC over hosted victims, r_field T0, edit type E3, lower 95% CI bound |
| `\DetEditRFieldTZeroEThreeHi` | 0.62 | mean AUROC over hosted victims, r_field T0, edit type E3, upper 95% CI bound |
| `\DetEditRFieldTZeroEThreeCI` | [0.58, 0.62] | mean AUROC over hosted victims, r_field T0, edit type E3, 95% CI |
| `\DetEditRFieldTZeroEThreeN` | 600 | mean AUROC over hosted victims, r_field T0, edit type E3, n |
| `\DetEditRFieldTZeroEThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T0, edit type E3, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRFieldTZeroEFour` | 0.55 | mean AUROC over hosted victims, r_field T0, edit type E4 |
| `\DetEditRFieldTZeroEFourLo` | 0.54 | mean AUROC over hosted victims, r_field T0, edit type E4, lower 95% CI bound |
| `\DetEditRFieldTZeroEFourHi` | 0.57 | mean AUROC over hosted victims, r_field T0, edit type E4, upper 95% CI bound |
| `\DetEditRFieldTZeroEFourCI` | [0.54, 0.57] | mean AUROC over hosted victims, r_field T0, edit type E4, 95% CI |
| `\DetEditRFieldTZeroEFourN` | 598 | mean AUROC over hosted victims, r_field T0, edit type E4, n |
| `\DetEditRFieldTZeroEFourP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T0, edit type E4, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRFieldTZeroEFive` | 0.50 | mean AUROC over hosted victims, r_field T0, edit type E5 |
| `\DetEditRFieldTZeroEFiveLo` | 0.50 | mean AUROC over hosted victims, r_field T0, edit type E5, lower 95% CI bound |
| `\DetEditRFieldTZeroEFiveHi` | 0.51 | mean AUROC over hosted victims, r_field T0, edit type E5, upper 95% CI bound |
| `\DetEditRFieldTZeroEFiveCI` | [0.50, 0.51] | mean AUROC over hosted victims, r_field T0, edit type E5, 95% CI |
| `\DetEditRFieldTZeroEFiveN` | 600 | mean AUROC over hosted victims, r_field T0, edit type E5, n |
| `\DetEditRFieldTZeroEFiveP` | 0.553 | mean AUROC over hosted victims, r_field T0, edit type E5, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRFieldTOneEOne` | 0.86 | mean AUROC over hosted victims, r_field T1, edit type E1 |
| `\DetEditRFieldTOneEOneLo` | 0.84 | mean AUROC over hosted victims, r_field T1, edit type E1, lower 95% CI bound |
| `\DetEditRFieldTOneEOneHi` | 0.89 | mean AUROC over hosted victims, r_field T1, edit type E1, upper 95% CI bound |
| `\DetEditRFieldTOneEOneCI` | [0.84, 0.89] | mean AUROC over hosted victims, r_field T1, edit type E1, 95% CI |
| `\DetEditRFieldTOneEOneN` | 596 | mean AUROC over hosted victims, r_field T1, edit type E1, n |
| `\DetEditRFieldTOneEOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T1, edit type E1, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRFieldTOneETwo` | 0.70 | mean AUROC over hosted victims, r_field T1, edit type E2 |
| `\DetEditRFieldTOneETwoLo` | 0.67 | mean AUROC over hosted victims, r_field T1, edit type E2, lower 95% CI bound |
| `\DetEditRFieldTOneETwoHi` | 0.72 | mean AUROC over hosted victims, r_field T1, edit type E2, upper 95% CI bound |
| `\DetEditRFieldTOneETwoCI` | [0.67, 0.72] | mean AUROC over hosted victims, r_field T1, edit type E2, 95% CI |
| `\DetEditRFieldTOneETwoN` | 596 | mean AUROC over hosted victims, r_field T1, edit type E2, n |
| `\DetEditRFieldTOneETwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T1, edit type E2, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRFieldTOneEThree` | 0.60 | mean AUROC over hosted victims, r_field T1, edit type E3 |
| `\DetEditRFieldTOneEThreeLo` | 0.57 | mean AUROC over hosted victims, r_field T1, edit type E3, lower 95% CI bound |
| `\DetEditRFieldTOneEThreeHi` | 0.63 | mean AUROC over hosted victims, r_field T1, edit type E3, upper 95% CI bound |
| `\DetEditRFieldTOneEThreeCI` | [0.57, 0.63] | mean AUROC over hosted victims, r_field T1, edit type E3, 95% CI |
| `\DetEditRFieldTOneEThreeN` | 600 | mean AUROC over hosted victims, r_field T1, edit type E3, n |
| `\DetEditRFieldTOneEThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T1, edit type E3, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRFieldTOneEFour` | 0.54 | mean AUROC over hosted victims, r_field T1, edit type E4 |
| `\DetEditRFieldTOneEFourLo` | 0.52 | mean AUROC over hosted victims, r_field T1, edit type E4, lower 95% CI bound |
| `\DetEditRFieldTOneEFourHi` | 0.56 | mean AUROC over hosted victims, r_field T1, edit type E4, upper 95% CI bound |
| `\DetEditRFieldTOneEFourCI` | [0.52, 0.56] | mean AUROC over hosted victims, r_field T1, edit type E4, 95% CI |
| `\DetEditRFieldTOneEFourN` | 598 | mean AUROC over hosted victims, r_field T1, edit type E4, n |
| `\DetEditRFieldTOneEFourP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T1, edit type E4, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRFieldTOneEFive` | 0.49 | mean AUROC over hosted victims, r_field T1, edit type E5 |
| `\DetEditRFieldTOneEFiveLo` | 0.47 | mean AUROC over hosted victims, r_field T1, edit type E5, lower 95% CI bound |
| `\DetEditRFieldTOneEFiveHi` | 0.50 | mean AUROC over hosted victims, r_field T1, edit type E5, upper 95% CI bound |
| `\DetEditRFieldTOneEFiveCI` | [0.47, 0.50] | mean AUROC over hosted victims, r_field T1, edit type E5, 95% CI |
| `\DetEditRFieldTOneEFiveN` | 558 | mean AUROC over hosted victims, r_field T1, edit type E5, n |
| `\DetEditRFieldTOneEFiveP` | 0.057 | mean AUROC over hosted victims, r_field T1, edit type E5, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRFieldTTwoEOne` | 0.86 | mean AUROC over hosted victims, r_field T2, edit type E1 |
| `\DetEditRFieldTTwoEOneLo` | 0.84 | mean AUROC over hosted victims, r_field T2, edit type E1, lower 95% CI bound |
| `\DetEditRFieldTTwoEOneHi` | 0.88 | mean AUROC over hosted victims, r_field T2, edit type E1, upper 95% CI bound |
| `\DetEditRFieldTTwoEOneCI` | [0.84, 0.88] | mean AUROC over hosted victims, r_field T2, edit type E1, 95% CI |
| `\DetEditRFieldTTwoEOneN` | 596 | mean AUROC over hosted victims, r_field T2, edit type E1, n |
| `\DetEditRFieldTTwoEOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T2, edit type E1, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRFieldTTwoETwo` | 0.73 | mean AUROC over hosted victims, r_field T2, edit type E2 |
| `\DetEditRFieldTTwoETwoLo` | 0.71 | mean AUROC over hosted victims, r_field T2, edit type E2, lower 95% CI bound |
| `\DetEditRFieldTTwoETwoHi` | 0.76 | mean AUROC over hosted victims, r_field T2, edit type E2, upper 95% CI bound |
| `\DetEditRFieldTTwoETwoCI` | [0.71, 0.76] | mean AUROC over hosted victims, r_field T2, edit type E2, 95% CI |
| `\DetEditRFieldTTwoETwoN` | 574 | mean AUROC over hosted victims, r_field T2, edit type E2, n |
| `\DetEditRFieldTTwoETwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T2, edit type E2, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRFieldTTwoEThree` | 0.60 | mean AUROC over hosted victims, r_field T2, edit type E3 |
| `\DetEditRFieldTTwoEThreeLo` | 0.58 | mean AUROC over hosted victims, r_field T2, edit type E3, lower 95% CI bound |
| `\DetEditRFieldTTwoEThreeHi` | 0.63 | mean AUROC over hosted victims, r_field T2, edit type E3, upper 95% CI bound |
| `\DetEditRFieldTTwoEThreeCI` | [0.58, 0.63] | mean AUROC over hosted victims, r_field T2, edit type E3, 95% CI |
| `\DetEditRFieldTTwoEThreeN` | 600 | mean AUROC over hosted victims, r_field T2, edit type E3, n |
| `\DetEditRFieldTTwoEThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T2, edit type E3, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRFieldTTwoEFour` | 0.54 | mean AUROC over hosted victims, r_field T2, edit type E4 |
| `\DetEditRFieldTTwoEFourLo` | 0.52 | mean AUROC over hosted victims, r_field T2, edit type E4, lower 95% CI bound |
| `\DetEditRFieldTTwoEFourHi` | 0.56 | mean AUROC over hosted victims, r_field T2, edit type E4, upper 95% CI bound |
| `\DetEditRFieldTTwoEFourCI` | [0.52, 0.56] | mean AUROC over hosted victims, r_field T2, edit type E4, 95% CI |
| `\DetEditRFieldTTwoEFourN` | 598 | mean AUROC over hosted victims, r_field T2, edit type E4, n |
| `\DetEditRFieldTTwoEFourP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T2, edit type E4, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRFieldTTwoEFive` | 0.50 | mean AUROC over hosted victims, r_field T2, edit type E5 |
| `\DetEditRFieldTTwoEFiveLo` | 0.49 | mean AUROC over hosted victims, r_field T2, edit type E5, lower 95% CI bound |
| `\DetEditRFieldTTwoEFiveHi` | 0.50 | mean AUROC over hosted victims, r_field T2, edit type E5, upper 95% CI bound |
| `\DetEditRFieldTTwoEFiveCI` | [0.49, 0.50] | mean AUROC over hosted victims, r_field T2, edit type E5, 95% CI |
| `\DetEditRFieldTTwoEFiveN` | 580 | mean AUROC over hosted victims, r_field T2, edit type E5, n |
| `\DetEditRFieldTTwoEFiveP` | 0.344 | mean AUROC over hosted victims, r_field T2, edit type E5, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRFieldTThreeEOne` | 0.86 | mean AUROC over hosted victims, r_field T3, edit type E1 |
| `\DetEditRFieldTThreeEOneLo` | 0.84 | mean AUROC over hosted victims, r_field T3, edit type E1, lower 95% CI bound |
| `\DetEditRFieldTThreeEOneHi` | 0.88 | mean AUROC over hosted victims, r_field T3, edit type E1, upper 95% CI bound |
| `\DetEditRFieldTThreeEOneCI` | [0.84, 0.88] | mean AUROC over hosted victims, r_field T3, edit type E1, 95% CI |
| `\DetEditRFieldTThreeEOneN` | 598 | mean AUROC over hosted victims, r_field T3, edit type E1, n |
| `\DetEditRFieldTThreeEOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T3, edit type E1, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRFieldTThreeETwo` | 0.74 | mean AUROC over hosted victims, r_field T3, edit type E2 |
| `\DetEditRFieldTThreeETwoLo` | 0.71 | mean AUROC over hosted victims, r_field T3, edit type E2, lower 95% CI bound |
| `\DetEditRFieldTThreeETwoHi` | 0.77 | mean AUROC over hosted victims, r_field T3, edit type E2, upper 95% CI bound |
| `\DetEditRFieldTThreeETwoCI` | [0.71, 0.77] | mean AUROC over hosted victims, r_field T3, edit type E2, 95% CI |
| `\DetEditRFieldTThreeETwoN` | 588 | mean AUROC over hosted victims, r_field T3, edit type E2, n |
| `\DetEditRFieldTThreeETwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T3, edit type E2, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRFieldTThreeEThree` | 0.61 | mean AUROC over hosted victims, r_field T3, edit type E3 |
| `\DetEditRFieldTThreeEThreeLo` | 0.59 | mean AUROC over hosted victims, r_field T3, edit type E3, lower 95% CI bound |
| `\DetEditRFieldTThreeEThreeHi` | 0.64 | mean AUROC over hosted victims, r_field T3, edit type E3, upper 95% CI bound |
| `\DetEditRFieldTThreeEThreeCI` | [0.59, 0.64] | mean AUROC over hosted victims, r_field T3, edit type E3, 95% CI |
| `\DetEditRFieldTThreeEThreeN` | 600 | mean AUROC over hosted victims, r_field T3, edit type E3, n |
| `\DetEditRFieldTThreeEThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T3, edit type E3, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRFieldTThreeEFour` | 0.55 | mean AUROC over hosted victims, r_field T3, edit type E4 |
| `\DetEditRFieldTThreeEFourLo` | 0.53 | mean AUROC over hosted victims, r_field T3, edit type E4, lower 95% CI bound |
| `\DetEditRFieldTThreeEFourHi` | 0.58 | mean AUROC over hosted victims, r_field T3, edit type E4, upper 95% CI bound |
| `\DetEditRFieldTThreeEFourCI` | [0.53, 0.58] | mean AUROC over hosted victims, r_field T3, edit type E4, 95% CI |
| `\DetEditRFieldTThreeEFourN` | 598 | mean AUROC over hosted victims, r_field T3, edit type E4, n |
| `\DetEditRFieldTThreeEFourP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T3, edit type E4, two-sided bootstrap p (n/a if not tested) |
| `\DetEditRFieldTThreeEFive` | 0.49 | mean AUROC over hosted victims, r_field T3, edit type E5 |
| `\DetEditRFieldTThreeEFiveLo` | 0.48 | mean AUROC over hosted victims, r_field T3, edit type E5, lower 95% CI bound |
| `\DetEditRFieldTThreeEFiveHi` | 0.50 | mean AUROC over hosted victims, r_field T3, edit type E5, upper 95% CI bound |
| `\DetEditRFieldTThreeEFiveCI` | [0.48, 0.50] | mean AUROC over hosted victims, r_field T3, edit type E5, 95% CI |
| `\DetEditRFieldTThreeEFiveN` | 598 | mean AUROC over hosted victims, r_field T3, edit type E5, n |
| `\DetEditRFieldTThreeEFiveP` | 0.166 | mean AUROC over hosted victims, r_field T3, edit type E5, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanTprFiveVTZero` | 63.9 | mean over hosted victims of TPR at 5% FPR (%), V T0 (5 victims) |
| `\DetMeanTprFiveVTOne` | 25.7 | mean over hosted victims of TPR at 5% FPR (%), V T1 (5 victims) |
| `\DetMeanTprFiveVTTwo` | 27.0 | mean over hosted victims of TPR at 5% FPR (%), V T2 (5 victims) |
| `\DetMeanTprFiveVTThree` | 22.3 | mean over hosted victims of TPR at 5% FPR (%), V T3 (5 victims) |
| `\DetMeanTprFiveCTZero` | 98.5 | mean over hosted victims of TPR at 5% FPR (%), C T0 (5 victims) |
| `\DetMeanTprFiveCTOne` | 97.9 | mean over hosted victims of TPR at 5% FPR (%), C T1 (5 victims) |
| `\DetMeanTprFiveCTTwo` | 98.1 | mean over hosted victims of TPR at 5% FPR (%), C T2 (5 victims) |
| `\DetMeanTprFiveCTThree` | 98.2 | mean over hosted victims of TPR at 5% FPR (%), C T3 (5 victims) |
| `\DetMeanTprFiveRTZero` | 76.8 | mean over hosted victims of TPR at 5% FPR (%), R T0 (5 victims) |
| `\DetMeanTprFiveRTOne` | 76.6 | mean over hosted victims of TPR at 5% FPR (%), R T1 (5 victims) |
| `\DetMeanTprFiveRTTwo` | 76.1 | mean over hosted victims of TPR at 5% FPR (%), R T2 (5 victims) |
| `\DetMeanTprFiveRTThree` | 76.9 | mean over hosted victims of TPR at 5% FPR (%), R T3 (5 victims) |
| `\DetMeanTprFiveRFieldTZero` | 11.1 | mean over hosted victims of TPR at 5% FPR (%), r_field T0 (5 victims) |
| `\DetMeanTprFiveRFieldTOne` | 12.1 | mean over hosted victims of TPR at 5% FPR (%), r_field T1 (5 victims) |
| `\DetMeanTprFiveRFieldTTwo` | 12.3 | mean over hosted victims of TPR at 5% FPR (%), r_field T2 (5 victims) |
| `\DetMeanTprFiveRFieldTThree` | 13.5 | mean over hosted victims of TPR at 5% FPR (%), r_field T3 (5 victims) |
| `\DetMeanTprFiveFTraceTZero` | 19.2 | mean over hosted victims of TPR at 5% FPR (%), f_trace T0 (5 victims) |
| `\DetMeanTprFiveFTraceTOne` | 20.2 | mean over hosted victims of TPR at 5% FPR (%), f_trace T1 (5 victims) |
| `\DetMeanTprFiveFTraceTTwo` | 21.3 | mean over hosted victims of TPR at 5% FPR (%), f_trace T2 (5 victims) |
| `\DetMeanTprFiveFTraceTThree` | 22.3 | mean over hosted victims of TPR at 5% FPR (%), f_trace T3 (5 victims) |
| `\DetMeanCTZeroNegAll` | 0.99 | mean AUROC over hosted victims, C T0, negatives all_clean |
| `\DetMeanCTZeroNegAllLo` | 0.99 | mean AUROC over hosted victims, C T0, negatives all_clean, lower 95% CI bound |
| `\DetMeanCTZeroNegAllHi` | 0.99 | mean AUROC over hosted victims, C T0, negatives all_clean, upper 95% CI bound |
| `\DetMeanCTZeroNegAllCI` | [0.99, 0.99] | mean AUROC over hosted victims, C T0, negatives all_clean, 95% CI |
| `\DetMeanCTZeroNegAllN` | 3{,}543 | mean AUROC over hosted victims, C T0, negatives all_clean, n |
| `\DetMeanCTZeroNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T0, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTZeroNegAttacked` | 0.99 | mean AUROC over hosted victims, C T0, negatives in_attacked |
| `\DetMeanCTZeroNegAttackedLo` | 0.99 | mean AUROC over hosted victims, C T0, negatives in_attacked, lower 95% CI bound |
| `\DetMeanCTZeroNegAttackedHi` | 0.99 | mean AUROC over hosted victims, C T0, negatives in_attacked, upper 95% CI bound |
| `\DetMeanCTZeroNegAttackedCI` | [0.99, 0.99] | mean AUROC over hosted victims, C T0, negatives in_attacked, 95% CI |
| `\DetMeanCTZeroNegAttackedN` | 10{,}346 | mean AUROC over hosted victims, C T0, negatives in_attacked, n |
| `\DetMeanCTZeroNegAttackedP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T0, negatives in_attacked, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTZero` | 0.99 | mean AUROC over hosted victims, C T0, negatives same_slot |
| `\DetMeanCTZeroLo` | 0.99 | mean AUROC over hosted victims, C T0, negatives same_slot, lower 95% CI bound |
| `\DetMeanCTZeroHi` | 0.99 | mean AUROC over hosted victims, C T0, negatives same_slot, upper 95% CI bound |
| `\DetMeanCTZeroCI` | [0.99, 0.99] | mean AUROC over hosted victims, C T0, negatives same_slot, 95% CI |
| `\DetMeanCTZeroN` | 2{,}953 | mean AUROC over hosted victims, C T0, negatives same_slot, n |
| `\DetMeanCTZeroP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T0, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTOneNegAll` | 0.99 | mean AUROC over hosted victims, C T1, negatives all_clean |
| `\DetMeanCTOneNegAllLo` | 0.98 | mean AUROC over hosted victims, C T1, negatives all_clean, lower 95% CI bound |
| `\DetMeanCTOneNegAllHi` | 0.99 | mean AUROC over hosted victims, C T1, negatives all_clean, upper 95% CI bound |
| `\DetMeanCTOneNegAllCI` | [0.98, 0.99] | mean AUROC over hosted victims, C T1, negatives all_clean, 95% CI |
| `\DetMeanCTOneNegAllN` | 3{,}521 | mean AUROC over hosted victims, C T1, negatives all_clean, n |
| `\DetMeanCTOneNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T1, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTOneNegAttacked` | 0.99 | mean AUROC over hosted victims, C T1, negatives in_attacked |
| `\DetMeanCTOneNegAttackedLo` | 0.98 | mean AUROC over hosted victims, C T1, negatives in_attacked, lower 95% CI bound |
| `\DetMeanCTOneNegAttackedHi` | 0.99 | mean AUROC over hosted victims, C T1, negatives in_attacked, upper 95% CI bound |
| `\DetMeanCTOneNegAttackedCI` | [0.98, 0.99] | mean AUROC over hosted victims, C T1, negatives in_attacked, 95% CI |
| `\DetMeanCTOneNegAttackedN` | 10{,}192 | mean AUROC over hosted victims, C T1, negatives in_attacked, n |
| `\DetMeanCTOneNegAttackedP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T1, negatives in_attacked, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTOne` | 0.99 | mean AUROC over hosted victims, C T1, negatives same_slot |
| `\DetMeanCTOneLo` | 0.98 | mean AUROC over hosted victims, C T1, negatives same_slot, lower 95% CI bound |
| `\DetMeanCTOneHi` | 0.99 | mean AUROC over hosted victims, C T1, negatives same_slot, upper 95% CI bound |
| `\DetMeanCTOneCI` | [0.98, 0.99] | mean AUROC over hosted victims, C T1, negatives same_slot, 95% CI |
| `\DetMeanCTOneN` | 2{,}909 | mean AUROC over hosted victims, C T1, negatives same_slot, n |
| `\DetMeanCTOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T1, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTTwoNegAll` | 0.99 | mean AUROC over hosted victims, C T2, negatives all_clean |
| `\DetMeanCTTwoNegAllLo` | 0.99 | mean AUROC over hosted victims, C T2, negatives all_clean, lower 95% CI bound |
| `\DetMeanCTTwoNegAllHi` | 0.99 | mean AUROC over hosted victims, C T2, negatives all_clean, upper 95% CI bound |
| `\DetMeanCTTwoNegAllCI` | [0.99, 0.99] | mean AUROC over hosted victims, C T2, negatives all_clean, 95% CI |
| `\DetMeanCTTwoNegAllN` | 3{,}523 | mean AUROC over hosted victims, C T2, negatives all_clean, n |
| `\DetMeanCTTwoNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T2, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTTwoNegAttacked` | 0.99 | mean AUROC over hosted victims, C T2, negatives in_attacked |
| `\DetMeanCTTwoNegAttackedLo` | 0.98 | mean AUROC over hosted victims, C T2, negatives in_attacked, lower 95% CI bound |
| `\DetMeanCTTwoNegAttackedHi` | 0.99 | mean AUROC over hosted victims, C T2, negatives in_attacked, upper 95% CI bound |
| `\DetMeanCTTwoNegAttackedCI` | [0.98, 0.99] | mean AUROC over hosted victims, C T2, negatives in_attacked, 95% CI |
| `\DetMeanCTTwoNegAttackedN` | 10{,}206 | mean AUROC over hosted victims, C T2, negatives in_attacked, n |
| `\DetMeanCTTwoNegAttackedP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T2, negatives in_attacked, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTTwo` | 0.99 | mean AUROC over hosted victims, C T2, negatives same_slot |
| `\DetMeanCTTwoLo` | 0.99 | mean AUROC over hosted victims, C T2, negatives same_slot, lower 95% CI bound |
| `\DetMeanCTTwoHi` | 0.99 | mean AUROC over hosted victims, C T2, negatives same_slot, upper 95% CI bound |
| `\DetMeanCTTwoCI` | [0.99, 0.99] | mean AUROC over hosted victims, C T2, negatives same_slot, 95% CI |
| `\DetMeanCTTwoN` | 2{,}911 | mean AUROC over hosted victims, C T2, negatives same_slot, n |
| `\DetMeanCTTwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T2, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTThreeNegAll` | 0.99 | mean AUROC over hosted victims, C T3, negatives all_clean |
| `\DetMeanCTThreeNegAllLo` | 0.99 | mean AUROC over hosted victims, C T3, negatives all_clean, lower 95% CI bound |
| `\DetMeanCTThreeNegAllHi` | 0.99 | mean AUROC over hosted victims, C T3, negatives all_clean, upper 95% CI bound |
| `\DetMeanCTThreeNegAllCI` | [0.99, 0.99] | mean AUROC over hosted victims, C T3, negatives all_clean, 95% CI |
| `\DetMeanCTThreeNegAllN` | 3{,}538 | mean AUROC over hosted victims, C T3, negatives all_clean, n |
| `\DetMeanCTThreeNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T3, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTThreeNegAttacked` | 0.99 | mean AUROC over hosted victims, C T3, negatives in_attacked |
| `\DetMeanCTThreeNegAttackedLo` | 0.98 | mean AUROC over hosted victims, C T3, negatives in_attacked, lower 95% CI bound |
| `\DetMeanCTThreeNegAttackedHi` | 0.99 | mean AUROC over hosted victims, C T3, negatives in_attacked, upper 95% CI bound |
| `\DetMeanCTThreeNegAttackedCI` | [0.98, 0.99] | mean AUROC over hosted victims, C T3, negatives in_attacked, 95% CI |
| `\DetMeanCTThreeNegAttackedN` | 10{,}311 | mean AUROC over hosted victims, C T3, negatives in_attacked, n |
| `\DetMeanCTThreeNegAttackedP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T3, negatives in_attacked, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanCTThree` | 0.99 | mean AUROC over hosted victims, C T3, negatives same_slot |
| `\DetMeanCTThreeLo` | 0.99 | mean AUROC over hosted victims, C T3, negatives same_slot, lower 95% CI bound |
| `\DetMeanCTThreeHi` | 0.99 | mean AUROC over hosted victims, C T3, negatives same_slot, upper 95% CI bound |
| `\DetMeanCTThreeCI` | [0.99, 0.99] | mean AUROC over hosted victims, C T3, negatives same_slot, 95% CI |
| `\DetMeanCTThreeN` | 2{,}943 | mean AUROC over hosted victims, C T3, negatives same_slot, n |
| `\DetMeanCTThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, C T3, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRTZeroNegAll` | 0.95 | mean AUROC over hosted victims, R T0, negatives all_clean |
| `\DetMeanRTZeroNegAllLo` | 0.94 | mean AUROC over hosted victims, R T0, negatives all_clean, lower 95% CI bound |
| `\DetMeanRTZeroNegAllHi` | 0.95 | mean AUROC over hosted victims, R T0, negatives all_clean, upper 95% CI bound |
| `\DetMeanRTZeroNegAllCI` | [0.94, 0.95] | mean AUROC over hosted victims, R T0, negatives all_clean, 95% CI |
| `\DetMeanRTZeroNegAllN` | 3{,}573 | mean AUROC over hosted victims, R T0, negatives all_clean, n |
| `\DetMeanRTZeroNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T0, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRTZero` | 0.95 | mean AUROC over hosted victims, R T0, negatives same_slot |
| `\DetMeanRTZeroLo` | 0.94 | mean AUROC over hosted victims, R T0, negatives same_slot, lower 95% CI bound |
| `\DetMeanRTZeroHi` | 0.96 | mean AUROC over hosted victims, R T0, negatives same_slot, upper 95% CI bound |
| `\DetMeanRTZeroCI` | [0.94, 0.96] | mean AUROC over hosted victims, R T0, negatives same_slot, 95% CI |
| `\DetMeanRTZeroN` | 2{,}977 | mean AUROC over hosted victims, R T0, negatives same_slot, n |
| `\DetMeanRTZeroP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T0, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRTOneNegAll` | 0.95 | mean AUROC over hosted victims, R T1, negatives all_clean |
| `\DetMeanRTOneNegAllLo` | 0.94 | mean AUROC over hosted victims, R T1, negatives all_clean, lower 95% CI bound |
| `\DetMeanRTOneNegAllHi` | 0.95 | mean AUROC over hosted victims, R T1, negatives all_clean, upper 95% CI bound |
| `\DetMeanRTOneNegAllCI` | [0.94, 0.95] | mean AUROC over hosted victims, R T1, negatives all_clean, 95% CI |
| `\DetMeanRTOneNegAllN` | 3{,}561 | mean AUROC over hosted victims, R T1, negatives all_clean, n |
| `\DetMeanRTOneNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T1, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRTOne` | 0.95 | mean AUROC over hosted victims, R T1, negatives same_slot |
| `\DetMeanRTOneLo` | 0.94 | mean AUROC over hosted victims, R T1, negatives same_slot, lower 95% CI bound |
| `\DetMeanRTOneHi` | 0.96 | mean AUROC over hosted victims, R T1, negatives same_slot, upper 95% CI bound |
| `\DetMeanRTOneCI` | [0.94, 0.96] | mean AUROC over hosted victims, R T1, negatives same_slot, 95% CI |
| `\DetMeanRTOneN` | 2{,}943 | mean AUROC over hosted victims, R T1, negatives same_slot, n |
| `\DetMeanRTOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T1, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRTTwoNegAll` | 0.95 | mean AUROC over hosted victims, R T2, negatives all_clean |
| `\DetMeanRTTwoNegAllLo` | 0.94 | mean AUROC over hosted victims, R T2, negatives all_clean, lower 95% CI bound |
| `\DetMeanRTTwoNegAllHi` | 0.95 | mean AUROC over hosted victims, R T2, negatives all_clean, upper 95% CI bound |
| `\DetMeanRTTwoNegAllCI` | [0.94, 0.95] | mean AUROC over hosted victims, R T2, negatives all_clean, 95% CI |
| `\DetMeanRTTwoNegAllN` | 3{,}556 | mean AUROC over hosted victims, R T2, negatives all_clean, n |
| `\DetMeanRTTwoNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T2, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRTTwo` | 0.95 | mean AUROC over hosted victims, R T2, negatives same_slot |
| `\DetMeanRTTwoLo` | 0.94 | mean AUROC over hosted victims, R T2, negatives same_slot, lower 95% CI bound |
| `\DetMeanRTTwoHi` | 0.96 | mean AUROC over hosted victims, R T2, negatives same_slot, upper 95% CI bound |
| `\DetMeanRTTwoCI` | [0.94, 0.96] | mean AUROC over hosted victims, R T2, negatives same_slot, 95% CI |
| `\DetMeanRTTwoN` | 2{,}938 | mean AUROC over hosted victims, R T2, negatives same_slot, n |
| `\DetMeanRTTwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T2, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRTThreeNegAll` | 0.95 | mean AUROC over hosted victims, R T3, negatives all_clean |
| `\DetMeanRTThreeNegAllLo` | 0.94 | mean AUROC over hosted victims, R T3, negatives all_clean, lower 95% CI bound |
| `\DetMeanRTThreeNegAllHi` | 0.95 | mean AUROC over hosted victims, R T3, negatives all_clean, upper 95% CI bound |
| `\DetMeanRTThreeNegAllCI` | [0.94, 0.95] | mean AUROC over hosted victims, R T3, negatives all_clean, 95% CI |
| `\DetMeanRTThreeNegAllN` | 3{,}578 | mean AUROC over hosted victims, R T3, negatives all_clean, n |
| `\DetMeanRTThreeNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T3, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRTThree` | 0.95 | mean AUROC over hosted victims, R T3, negatives same_slot |
| `\DetMeanRTThreeLo` | 0.94 | mean AUROC over hosted victims, R T3, negatives same_slot, lower 95% CI bound |
| `\DetMeanRTThreeHi` | 0.96 | mean AUROC over hosted victims, R T3, negatives same_slot, upper 95% CI bound |
| `\DetMeanRTThreeCI` | [0.94, 0.96] | mean AUROC over hosted victims, R T3, negatives same_slot, 95% CI |
| `\DetMeanRTThreeN` | 2{,}977 | mean AUROC over hosted victims, R T3, negatives same_slot, n |
| `\DetMeanRTThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, R T3, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTZeroNegAll` | 0.79 | mean AUROC over hosted victims, V T0, negatives all_clean |
| `\DetMeanVTZeroNegAllLo` | 0.78 | mean AUROC over hosted victims, V T0, negatives all_clean, lower 95% CI bound |
| `\DetMeanVTZeroNegAllHi` | 0.81 | mean AUROC over hosted victims, V T0, negatives all_clean, upper 95% CI bound |
| `\DetMeanVTZeroNegAllCI` | [0.78, 0.81] | mean AUROC over hosted victims, V T0, negatives all_clean, 95% CI |
| `\DetMeanVTZeroNegAllN` | 3{,}543 | mean AUROC over hosted victims, V T0, negatives all_clean, n |
| `\DetMeanVTZeroNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T0, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTZeroNegAttacked` | 0.80 | mean AUROC over hosted victims, V T0, negatives in_attacked |
| `\DetMeanVTZeroNegAttackedLo` | 0.78 | mean AUROC over hosted victims, V T0, negatives in_attacked, lower 95% CI bound |
| `\DetMeanVTZeroNegAttackedHi` | 0.81 | mean AUROC over hosted victims, V T0, negatives in_attacked, upper 95% CI bound |
| `\DetMeanVTZeroNegAttackedCI` | [0.78, 0.81] | mean AUROC over hosted victims, V T0, negatives in_attacked, 95% CI |
| `\DetMeanVTZeroNegAttackedN` | 10{,}346 | mean AUROC over hosted victims, V T0, negatives in_attacked, n |
| `\DetMeanVTZeroNegAttackedP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T0, negatives in_attacked, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTZero` | 0.79 | mean AUROC over hosted victims, V T0, negatives same_slot |
| `\DetMeanVTZeroLo` | 0.78 | mean AUROC over hosted victims, V T0, negatives same_slot, lower 95% CI bound |
| `\DetMeanVTZeroHi` | 0.81 | mean AUROC over hosted victims, V T0, negatives same_slot, upper 95% CI bound |
| `\DetMeanVTZeroCI` | [0.78, 0.81] | mean AUROC over hosted victims, V T0, negatives same_slot, 95% CI |
| `\DetMeanVTZeroN` | 2{,}953 | mean AUROC over hosted victims, V T0, negatives same_slot, n |
| `\DetMeanVTZeroP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T0, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTOneNegAll` | 0.62 | mean AUROC over hosted victims, V T1, negatives all_clean |
| `\DetMeanVTOneNegAllLo` | 0.61 | mean AUROC over hosted victims, V T1, negatives all_clean, lower 95% CI bound |
| `\DetMeanVTOneNegAllHi` | 0.64 | mean AUROC over hosted victims, V T1, negatives all_clean, upper 95% CI bound |
| `\DetMeanVTOneNegAllCI` | [0.61, 0.64] | mean AUROC over hosted victims, V T1, negatives all_clean, 95% CI |
| `\DetMeanVTOneNegAllN` | 3{,}520 | mean AUROC over hosted victims, V T1, negatives all_clean, n |
| `\DetMeanVTOneNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T1, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTOneNegAttacked` | 0.62 | mean AUROC over hosted victims, V T1, negatives in_attacked |
| `\DetMeanVTOneNegAttackedLo` | 0.61 | mean AUROC over hosted victims, V T1, negatives in_attacked, lower 95% CI bound |
| `\DetMeanVTOneNegAttackedHi` | 0.63 | mean AUROC over hosted victims, V T1, negatives in_attacked, upper 95% CI bound |
| `\DetMeanVTOneNegAttackedCI` | [0.61, 0.63] | mean AUROC over hosted victims, V T1, negatives in_attacked, 95% CI |
| `\DetMeanVTOneNegAttackedN` | 10{,}185 | mean AUROC over hosted victims, V T1, negatives in_attacked, n |
| `\DetMeanVTOneNegAttackedP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T1, negatives in_attacked, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTOne` | 0.62 | mean AUROC over hosted victims, V T1, negatives same_slot |
| `\DetMeanVTOneLo` | 0.61 | mean AUROC over hosted victims, V T1, negatives same_slot, lower 95% CI bound |
| `\DetMeanVTOneHi` | 0.64 | mean AUROC over hosted victims, V T1, negatives same_slot, upper 95% CI bound |
| `\DetMeanVTOneCI` | [0.61, 0.64] | mean AUROC over hosted victims, V T1, negatives same_slot, 95% CI |
| `\DetMeanVTOneN` | 2{,}908 | mean AUROC over hosted victims, V T1, negatives same_slot, n |
| `\DetMeanVTOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T1, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTTwoNegAll` | 0.62 | mean AUROC over hosted victims, V T2, negatives all_clean |
| `\DetMeanVTTwoNegAllLo` | 0.61 | mean AUROC over hosted victims, V T2, negatives all_clean, lower 95% CI bound |
| `\DetMeanVTTwoNegAllHi` | 0.64 | mean AUROC over hosted victims, V T2, negatives all_clean, upper 95% CI bound |
| `\DetMeanVTTwoNegAllCI` | [0.61, 0.64] | mean AUROC over hosted victims, V T2, negatives all_clean, 95% CI |
| `\DetMeanVTTwoNegAllN` | 3{,}523 | mean AUROC over hosted victims, V T2, negatives all_clean, n |
| `\DetMeanVTTwoNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T2, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTTwoNegAttacked` | 0.62 | mean AUROC over hosted victims, V T2, negatives in_attacked |
| `\DetMeanVTTwoNegAttackedLo` | 0.61 | mean AUROC over hosted victims, V T2, negatives in_attacked, lower 95% CI bound |
| `\DetMeanVTTwoNegAttackedHi` | 0.63 | mean AUROC over hosted victims, V T2, negatives in_attacked, upper 95% CI bound |
| `\DetMeanVTTwoNegAttackedCI` | [0.61, 0.63] | mean AUROC over hosted victims, V T2, negatives in_attacked, 95% CI |
| `\DetMeanVTTwoNegAttackedN` | 10{,}206 | mean AUROC over hosted victims, V T2, negatives in_attacked, n |
| `\DetMeanVTTwoNegAttackedP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T2, negatives in_attacked, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTTwo` | 0.62 | mean AUROC over hosted victims, V T2, negatives same_slot |
| `\DetMeanVTTwoLo` | 0.61 | mean AUROC over hosted victims, V T2, negatives same_slot, lower 95% CI bound |
| `\DetMeanVTTwoHi` | 0.64 | mean AUROC over hosted victims, V T2, negatives same_slot, upper 95% CI bound |
| `\DetMeanVTTwoCI` | [0.61, 0.64] | mean AUROC over hosted victims, V T2, negatives same_slot, 95% CI |
| `\DetMeanVTTwoN` | 2{,}911 | mean AUROC over hosted victims, V T2, negatives same_slot, n |
| `\DetMeanVTTwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T2, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTThreeNegAll` | 0.60 | mean AUROC over hosted victims, V T3, negatives all_clean |
| `\DetMeanVTThreeNegAllLo` | 0.58 | mean AUROC over hosted victims, V T3, negatives all_clean, lower 95% CI bound |
| `\DetMeanVTThreeNegAllHi` | 0.62 | mean AUROC over hosted victims, V T3, negatives all_clean, upper 95% CI bound |
| `\DetMeanVTThreeNegAllCI` | [0.58, 0.62] | mean AUROC over hosted victims, V T3, negatives all_clean, 95% CI |
| `\DetMeanVTThreeNegAllN` | 3{,}537 | mean AUROC over hosted victims, V T3, negatives all_clean, n |
| `\DetMeanVTThreeNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T3, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTThreeNegAttacked` | 0.60 | mean AUROC over hosted victims, V T3, negatives in_attacked |
| `\DetMeanVTThreeNegAttackedLo` | 0.59 | mean AUROC over hosted victims, V T3, negatives in_attacked, lower 95% CI bound |
| `\DetMeanVTThreeNegAttackedHi` | 0.61 | mean AUROC over hosted victims, V T3, negatives in_attacked, upper 95% CI bound |
| `\DetMeanVTThreeNegAttackedCI` | [0.59, 0.61] | mean AUROC over hosted victims, V T3, negatives in_attacked, 95% CI |
| `\DetMeanVTThreeNegAttackedN` | 10{,}304 | mean AUROC over hosted victims, V T3, negatives in_attacked, n |
| `\DetMeanVTThreeNegAttackedP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T3, negatives in_attacked, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanVTThree` | 0.60 | mean AUROC over hosted victims, V T3, negatives same_slot |
| `\DetMeanVTThreeLo` | 0.59 | mean AUROC over hosted victims, V T3, negatives same_slot, lower 95% CI bound |
| `\DetMeanVTThreeHi` | 0.62 | mean AUROC over hosted victims, V T3, negatives same_slot, upper 95% CI bound |
| `\DetMeanVTThreeCI` | [0.59, 0.62] | mean AUROC over hosted victims, V T3, negatives same_slot, 95% CI |
| `\DetMeanVTThreeN` | 2{,}942 | mean AUROC over hosted victims, V T3, negatives same_slot, n |
| `\DetMeanVTThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, V T3, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanFTraceTZeroNegAll` | 0.62 | mean AUROC over hosted victims, f_trace T0, negatives all_clean |
| `\DetMeanFTraceTZeroNegAllLo` | 0.61 | mean AUROC over hosted victims, f_trace T0, negatives all_clean, lower 95% CI bound |
| `\DetMeanFTraceTZeroNegAllHi` | 0.63 | mean AUROC over hosted victims, f_trace T0, negatives all_clean, upper 95% CI bound |
| `\DetMeanFTraceTZeroNegAllCI` | [0.61, 0.63] | mean AUROC over hosted victims, f_trace T0, negatives all_clean, 95% CI |
| `\DetMeanFTraceTZeroNegAllN` | 3{,}594 | mean AUROC over hosted victims, f_trace T0, negatives all_clean, n |
| `\DetMeanFTraceTZeroNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T0, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanFTraceTZero` | 0.65 | mean AUROC over hosted victims, f_trace T0, negatives same_slot |
| `\DetMeanFTraceTZeroLo` | 0.65 | mean AUROC over hosted victims, f_trace T0, negatives same_slot, lower 95% CI bound |
| `\DetMeanFTraceTZeroHi` | 0.66 | mean AUROC over hosted victims, f_trace T0, negatives same_slot, upper 95% CI bound |
| `\DetMeanFTraceTZeroCI` | [0.65, 0.66] | mean AUROC over hosted victims, f_trace T0, negatives same_slot, 95% CI |
| `\DetMeanFTraceTZeroN` | 2{,}996 | mean AUROC over hosted victims, f_trace T0, negatives same_slot, n |
| `\DetMeanFTraceTZeroP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T0, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanFTraceTOneNegAll` | 0.62 | mean AUROC over hosted victims, f_trace T1, negatives all_clean |
| `\DetMeanFTraceTOneNegAllLo` | 0.61 | mean AUROC over hosted victims, f_trace T1, negatives all_clean, lower 95% CI bound |
| `\DetMeanFTraceTOneNegAllHi` | 0.63 | mean AUROC over hosted victims, f_trace T1, negatives all_clean, upper 95% CI bound |
| `\DetMeanFTraceTOneNegAllCI` | [0.61, 0.63] | mean AUROC over hosted victims, f_trace T1, negatives all_clean, 95% CI |
| `\DetMeanFTraceTOneNegAllN` | 3{,}572 | mean AUROC over hosted victims, f_trace T1, negatives all_clean, n |
| `\DetMeanFTraceTOneNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T1, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanFTraceTOne` | 0.66 | mean AUROC over hosted victims, f_trace T1, negatives same_slot |
| `\DetMeanFTraceTOneLo` | 0.65 | mean AUROC over hosted victims, f_trace T1, negatives same_slot, lower 95% CI bound |
| `\DetMeanFTraceTOneHi` | 0.67 | mean AUROC over hosted victims, f_trace T1, negatives same_slot, upper 95% CI bound |
| `\DetMeanFTraceTOneCI` | [0.65, 0.67] | mean AUROC over hosted victims, f_trace T1, negatives same_slot, 95% CI |
| `\DetMeanFTraceTOneN` | 2{,}952 | mean AUROC over hosted victims, f_trace T1, negatives same_slot, n |
| `\DetMeanFTraceTOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T1, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanFTraceTTwoNegAll` | 0.63 | mean AUROC over hosted victims, f_trace T2, negatives all_clean |
| `\DetMeanFTraceTTwoNegAllLo` | 0.62 | mean AUROC over hosted victims, f_trace T2, negatives all_clean, lower 95% CI bound |
| `\DetMeanFTraceTTwoNegAllHi` | 0.63 | mean AUROC over hosted victims, f_trace T2, negatives all_clean, upper 95% CI bound |
| `\DetMeanFTraceTTwoNegAllCI` | [0.62, 0.63] | mean AUROC over hosted victims, f_trace T2, negatives all_clean, 95% CI |
| `\DetMeanFTraceTTwoNegAllN` | 3{,}572 | mean AUROC over hosted victims, f_trace T2, negatives all_clean, n |
| `\DetMeanFTraceTTwoNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T2, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanFTraceTTwo` | 0.66 | mean AUROC over hosted victims, f_trace T2, negatives same_slot |
| `\DetMeanFTraceTTwoLo` | 0.65 | mean AUROC over hosted victims, f_trace T2, negatives same_slot, lower 95% CI bound |
| `\DetMeanFTraceTTwoHi` | 0.67 | mean AUROC over hosted victims, f_trace T2, negatives same_slot, upper 95% CI bound |
| `\DetMeanFTraceTTwoCI` | [0.65, 0.67] | mean AUROC over hosted victims, f_trace T2, negatives same_slot, 95% CI |
| `\DetMeanFTraceTTwoN` | 2{,}952 | mean AUROC over hosted victims, f_trace T2, negatives same_slot, n |
| `\DetMeanFTraceTTwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T2, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanFTraceTThreeNegAll` | 0.63 | mean AUROC over hosted victims, f_trace T3, negatives all_clean |
| `\DetMeanFTraceTThreeNegAllLo` | 0.62 | mean AUROC over hosted victims, f_trace T3, negatives all_clean, lower 95% CI bound |
| `\DetMeanFTraceTThreeNegAllHi` | 0.64 | mean AUROC over hosted victims, f_trace T3, negatives all_clean, upper 95% CI bound |
| `\DetMeanFTraceTThreeNegAllCI` | [0.62, 0.64] | mean AUROC over hosted victims, f_trace T3, negatives all_clean, 95% CI |
| `\DetMeanFTraceTThreeNegAllN` | 3{,}589 | mean AUROC over hosted victims, f_trace T3, negatives all_clean, n |
| `\DetMeanFTraceTThreeNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T3, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanFTraceTThree` | 0.67 | mean AUROC over hosted victims, f_trace T3, negatives same_slot |
| `\DetMeanFTraceTThreeLo` | 0.66 | mean AUROC over hosted victims, f_trace T3, negatives same_slot, lower 95% CI bound |
| `\DetMeanFTraceTThreeHi` | 0.68 | mean AUROC over hosted victims, f_trace T3, negatives same_slot, upper 95% CI bound |
| `\DetMeanFTraceTThreeCI` | [0.66, 0.68] | mean AUROC over hosted victims, f_trace T3, negatives same_slot, 95% CI |
| `\DetMeanFTraceTThreeN` | 2{,}986 | mean AUROC over hosted victims, f_trace T3, negatives same_slot, n |
| `\DetMeanFTraceTThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, f_trace T3, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRFieldTZeroNegAll` | 0.64 | mean AUROC over hosted victims, r_field T0, negatives all_clean |
| `\DetMeanRFieldTZeroNegAllLo` | 0.63 | mean AUROC over hosted victims, r_field T0, negatives all_clean, lower 95% CI bound |
| `\DetMeanRFieldTZeroNegAllHi` | 0.65 | mean AUROC over hosted victims, r_field T0, negatives all_clean, upper 95% CI bound |
| `\DetMeanRFieldTZeroNegAllCI` | [0.63, 0.65] | mean AUROC over hosted victims, r_field T0, negatives all_clean, 95% CI |
| `\DetMeanRFieldTZeroNegAllN` | 3{,}590 | mean AUROC over hosted victims, r_field T0, negatives all_clean, n |
| `\DetMeanRFieldTZeroNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T0, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRFieldTZero` | 0.64 | mean AUROC over hosted victims, r_field T0, negatives same_slot |
| `\DetMeanRFieldTZeroLo` | 0.63 | mean AUROC over hosted victims, r_field T0, negatives same_slot, lower 95% CI bound |
| `\DetMeanRFieldTZeroHi` | 0.65 | mean AUROC over hosted victims, r_field T0, negatives same_slot, upper 95% CI bound |
| `\DetMeanRFieldTZeroCI` | [0.63, 0.65] | mean AUROC over hosted victims, r_field T0, negatives same_slot, 95% CI |
| `\DetMeanRFieldTZeroN` | 2{,}992 | mean AUROC over hosted victims, r_field T0, negatives same_slot, n |
| `\DetMeanRFieldTZeroP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T0, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRFieldTOneNegAll` | 0.64 | mean AUROC over hosted victims, r_field T1, negatives all_clean |
| `\DetMeanRFieldTOneNegAllLo` | 0.63 | mean AUROC over hosted victims, r_field T1, negatives all_clean, lower 95% CI bound |
| `\DetMeanRFieldTOneNegAllHi` | 0.65 | mean AUROC over hosted victims, r_field T1, negatives all_clean, upper 95% CI bound |
| `\DetMeanRFieldTOneNegAllCI` | [0.63, 0.65] | mean AUROC over hosted victims, r_field T1, negatives all_clean, 95% CI |
| `\DetMeanRFieldTOneNegAllN` | 3{,}568 | mean AUROC over hosted victims, r_field T1, negatives all_clean, n |
| `\DetMeanRFieldTOneNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T1, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRFieldTOne` | 0.64 | mean AUROC over hosted victims, r_field T1, negatives same_slot |
| `\DetMeanRFieldTOneLo` | 0.62 | mean AUROC over hosted victims, r_field T1, negatives same_slot, lower 95% CI bound |
| `\DetMeanRFieldTOneHi` | 0.65 | mean AUROC over hosted victims, r_field T1, negatives same_slot, upper 95% CI bound |
| `\DetMeanRFieldTOneCI` | [0.62, 0.65] | mean AUROC over hosted victims, r_field T1, negatives same_slot, 95% CI |
| `\DetMeanRFieldTOneN` | 2{,}948 | mean AUROC over hosted victims, r_field T1, negatives same_slot, n |
| `\DetMeanRFieldTOneP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T1, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRFieldTTwoNegAll` | 0.65 | mean AUROC over hosted victims, r_field T2, negatives all_clean |
| `\DetMeanRFieldTTwoNegAllLo` | 0.64 | mean AUROC over hosted victims, r_field T2, negatives all_clean, lower 95% CI bound |
| `\DetMeanRFieldTTwoNegAllHi` | 0.66 | mean AUROC over hosted victims, r_field T2, negatives all_clean, upper 95% CI bound |
| `\DetMeanRFieldTTwoNegAllCI` | [0.64, 0.66] | mean AUROC over hosted victims, r_field T2, negatives all_clean, 95% CI |
| `\DetMeanRFieldTTwoNegAllN` | 3{,}568 | mean AUROC over hosted victims, r_field T2, negatives all_clean, n |
| `\DetMeanRFieldTTwoNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T2, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRFieldTTwo` | 0.64 | mean AUROC over hosted victims, r_field T2, negatives same_slot |
| `\DetMeanRFieldTTwoLo` | 0.63 | mean AUROC over hosted victims, r_field T2, negatives same_slot, lower 95% CI bound |
| `\DetMeanRFieldTTwoHi` | 0.65 | mean AUROC over hosted victims, r_field T2, negatives same_slot, upper 95% CI bound |
| `\DetMeanRFieldTTwoCI` | [0.63, 0.65] | mean AUROC over hosted victims, r_field T2, negatives same_slot, 95% CI |
| `\DetMeanRFieldTTwoN` | 2{,}948 | mean AUROC over hosted victims, r_field T2, negatives same_slot, n |
| `\DetMeanRFieldTTwoP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T2, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRFieldTThreeNegAll` | 0.65 | mean AUROC over hosted victims, r_field T3, negatives all_clean |
| `\DetMeanRFieldTThreeNegAllLo` | 0.64 | mean AUROC over hosted victims, r_field T3, negatives all_clean, lower 95% CI bound |
| `\DetMeanRFieldTThreeNegAllHi` | 0.66 | mean AUROC over hosted victims, r_field T3, negatives all_clean, upper 95% CI bound |
| `\DetMeanRFieldTThreeNegAllCI` | [0.64, 0.66] | mean AUROC over hosted victims, r_field T3, negatives all_clean, 95% CI |
| `\DetMeanRFieldTThreeNegAllN` | 3{,}585 | mean AUROC over hosted victims, r_field T3, negatives all_clean, n |
| `\DetMeanRFieldTThreeNegAllP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T3, negatives all_clean, two-sided bootstrap p (n/a if not tested) |
| `\DetMeanRFieldTThree` | 0.65 | mean AUROC over hosted victims, r_field T3, negatives same_slot |
| `\DetMeanRFieldTThreeLo` | 0.64 | mean AUROC over hosted victims, r_field T3, negatives same_slot, lower 95% CI bound |
| `\DetMeanRFieldTThreeHi` | 0.66 | mean AUROC over hosted victims, r_field T3, negatives same_slot, upper 95% CI bound |
| `\DetMeanRFieldTThreeCI` | [0.64, 0.66] | mean AUROC over hosted victims, r_field T3, negatives same_slot, 95% CI |
| `\DetMeanRFieldTThreeN` | 2{,}982 | mean AUROC over hosted victims, r_field T3, negatives same_slot, n |
| `\DetMeanRFieldTThreeP` | \ensuremath{<}0.001 | mean AUROC over hosted victims, r_field T3, negatives same_slot, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTZero` | 0.70 | AUROC V T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTZeroLo` | 0.66 | AUROC V T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTZeroHi` | 0.75 | AUROC V T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTZeroCI` | [0.66, 0.75] | AUROC V T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTZeroN` | 600 | AUROC V T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTZeroP` | n/a | AUROC V T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTZeroTprOne` | 46.3 | TPR at 1% FPR (%), V T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTZeroTprOneLo` | 40.0 | TPR at 1% FPR (%), V T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTZeroTprOneHi` | 52.7 | TPR at 1% FPR (%), V T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTZeroTprOneCI` | [40.0, 52.7] | TPR at 1% FPR (%), V T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTZeroTprOneN` | 600 | TPR at 1% FPR (%), V T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTZeroTprOneP` | n/a | TPR at 1% FPR (%), V T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTZeroTprFive` | 52.3 | TPR at 5% FPR (%), V T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTZeroTprFiveLo` | 43.3 | TPR at 5% FPR (%), V T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTZeroTprFiveHi` | 57.7 | TPR at 5% FPR (%), V T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTZeroTprFiveCI` | [43.3, 57.7] | TPR at 5% FPR (%), V T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTZeroTprFiveN` | 600 | TPR at 5% FPR (%), V T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTZeroTprFiveP` | n/a | TPR at 5% FPR (%), V T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTOne` | 0.59 | AUROC V T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTOneLo` | 0.55 | AUROC V T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTOneHi` | 0.63 | AUROC V T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTOneCI` | [0.55, 0.63] | AUROC V T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTOneN` | 594 | AUROC V T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTOneP` | n/a | AUROC V T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTOneTprOne` | 11.4 | TPR at 1% FPR (%), V T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTOneTprOneLo` | 7.4 | TPR at 1% FPR (%), V T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTOneTprOneHi` | 14.8 | TPR at 1% FPR (%), V T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTOneTprOneCI` | [7.4, 14.8] | TPR at 1% FPR (%), V T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTOneTprOneN` | 594 | TPR at 1% FPR (%), V T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTOneTprOneP` | n/a | TPR at 1% FPR (%), V T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTOneTprFive` | 18.5 | TPR at 5% FPR (%), V T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTOneTprFiveLo` | 9.4 | TPR at 5% FPR (%), V T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTOneTprFiveHi` | 22.6 | TPR at 5% FPR (%), V T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTOneTprFiveCI` | [9.4, 22.6] | TPR at 5% FPR (%), V T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTOneTprFiveN` | 594 | TPR at 5% FPR (%), V T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTOneTprFiveP` | n/a | TPR at 5% FPR (%), V T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTTwo` | 0.57 | AUROC V T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTTwoLo` | 0.54 | AUROC V T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTTwoHi` | 0.61 | AUROC V T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTTwoCI` | [0.54, 0.61] | AUROC V T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTTwoN` | 596 | AUROC V T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTTwoP` | n/a | AUROC V T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTTwoTprOne` | 12.1 | TPR at 1% FPR (%), V T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTTwoTprOneLo` | 8.1 | TPR at 1% FPR (%), V T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTTwoTprOneHi` | 15.8 | TPR at 1% FPR (%), V T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTTwoTprOneCI` | [8.1, 15.8] | TPR at 1% FPR (%), V T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTTwoTprOneN` | 596 | TPR at 1% FPR (%), V T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTTwoTprOneP` | n/a | TPR at 1% FPR (%), V T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTTwoTprFive` | 22.5 | TPR at 5% FPR (%), V T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTTwoTprFiveLo` | 10.1 | TPR at 5% FPR (%), V T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTTwoTprFiveHi` | 26.5 | TPR at 5% FPR (%), V T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTTwoTprFiveCI` | [10.1, 26.5] | TPR at 5% FPR (%), V T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTTwoTprFiveN` | 596 | TPR at 5% FPR (%), V T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTTwoTprFiveP` | n/a | TPR at 5% FPR (%), V T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTThree` | 0.56 | AUROC V T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTThreeLo` | 0.53 | AUROC V T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTThreeHi` | 0.60 | AUROC V T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTThreeCI` | [0.53, 0.60] | AUROC V T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTThreeN` | 600 | AUROC V T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTThreeP` | n/a | AUROC V T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTThreeTprOne` | 9.7 | TPR at 1% FPR (%), V T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTThreeTprOneLo` | 6.3 | TPR at 1% FPR (%), V T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTThreeTprOneHi` | 13.3 | TPR at 1% FPR (%), V T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTThreeTprOneCI` | [6.3, 13.3] | TPR at 1% FPR (%), V T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTThreeTprOneN` | 600 | TPR at 1% FPR (%), V T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTThreeTprOneP` | n/a | TPR at 1% FPR (%), V T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashVTThreeTprFive` | 16.7 | TPR at 5% FPR (%), V T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashVTThreeTprFiveLo` | 7.7 | TPR at 5% FPR (%), V T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashVTThreeTprFiveHi` | 20.7 | TPR at 5% FPR (%), V T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashVTThreeTprFiveCI` | [7.7, 20.7] | TPR at 5% FPR (%), V T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashVTThreeTprFiveN` | 600 | TPR at 5% FPR (%), V T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashVTThreeTprFiveP` | n/a | TPR at 5% FPR (%), V T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTZero` | 0.97 | AUROC C T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTZeroLo` | 0.95 | AUROC C T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTZeroHi` | 0.98 | AUROC C T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTZeroCI` | [0.95, 0.98] | AUROC C T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTZeroN` | 600 | AUROC C T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTZeroP` | n/a | AUROC C T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTZeroTprOne` | 91.0 | TPR at 1% FPR (%), C T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTZeroTprOneLo` | 86.3 | TPR at 1% FPR (%), C T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTZeroTprOneHi` | 95.3 | TPR at 1% FPR (%), C T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTZeroTprOneCI` | [86.3, 95.3] | TPR at 1% FPR (%), C T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTZeroTprOneN` | 600 | TPR at 1% FPR (%), C T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTZeroTprOneP` | n/a | TPR at 1% FPR (%), C T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTZeroTprFive` | 93.3 | TPR at 5% FPR (%), C T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTZeroTprFiveLo` | 89.7 | TPR at 5% FPR (%), C T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTZeroTprFiveHi` | 96.0 | TPR at 5% FPR (%), C T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTZeroTprFiveCI` | [89.7, 96.0] | TPR at 5% FPR (%), C T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTZeroTprFiveN` | 600 | TPR at 5% FPR (%), C T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTZeroTprFiveP` | n/a | TPR at 5% FPR (%), C T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTOne` | 0.96 | AUROC C T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTOneLo` | 0.94 | AUROC C T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTOneHi` | 0.98 | AUROC C T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTOneCI` | [0.94, 0.98] | AUROC C T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTOneN` | 594 | AUROC C T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTOneP` | n/a | AUROC C T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTOneTprOne` | 90.6 | TPR at 1% FPR (%), C T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTOneTprOneLo` | 85.5 | TPR at 1% FPR (%), C T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTOneTprOneHi` | 94.6 | TPR at 1% FPR (%), C T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTOneTprOneCI` | [85.5, 94.6] | TPR at 1% FPR (%), C T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTOneTprOneN` | 594 | TPR at 1% FPR (%), C T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTOneTprOneP` | n/a | TPR at 1% FPR (%), C T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTOneTprFive` | 92.6 | TPR at 5% FPR (%), C T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTOneTprFiveLo` | 88.2 | TPR at 5% FPR (%), C T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTOneTprFiveHi` | 95.7 | TPR at 5% FPR (%), C T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTOneTprFiveCI` | [88.2, 95.7] | TPR at 5% FPR (%), C T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTOneTprFiveN` | 594 | TPR at 5% FPR (%), C T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTOneTprFiveP` | n/a | TPR at 5% FPR (%), C T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTTwo` | 0.97 | AUROC C T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTTwoLo` | 0.95 | AUROC C T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTTwoHi` | 0.98 | AUROC C T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTTwoCI` | [0.95, 0.98] | AUROC C T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTTwoN` | 596 | AUROC C T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTTwoP` | n/a | AUROC C T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTTwoTprOne` | 91.9 | TPR at 1% FPR (%), C T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTTwoTprOneLo` | 87.3 | TPR at 1% FPR (%), C T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTTwoTprOneHi` | 95.0 | TPR at 1% FPR (%), C T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTTwoTprOneCI` | [87.3, 95.0] | TPR at 1% FPR (%), C T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTTwoTprOneN` | 596 | TPR at 1% FPR (%), C T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTTwoTprOneP` | n/a | TPR at 1% FPR (%), C T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTTwoTprFive` | 93.3 | TPR at 5% FPR (%), C T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTTwoTprFiveLo` | 90.0 | TPR at 5% FPR (%), C T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTTwoTprFiveHi` | 96.0 | TPR at 5% FPR (%), C T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTTwoTprFiveCI` | [90.0, 96.0] | TPR at 5% FPR (%), C T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTTwoTprFiveN` | 596 | TPR at 5% FPR (%), C T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTTwoTprFiveP` | n/a | TPR at 5% FPR (%), C T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTThree` | 0.97 | AUROC C T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTThreeLo` | 0.95 | AUROC C T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTThreeHi` | 0.98 | AUROC C T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTThreeCI` | [0.95, 0.98] | AUROC C T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTThreeN` | 600 | AUROC C T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTThreeP` | n/a | AUROC C T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTThreeTprOne` | 92.3 | TPR at 1% FPR (%), C T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTThreeTprOneLo` | 88.7 | TPR at 1% FPR (%), C T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTThreeTprOneHi` | 96.0 | TPR at 1% FPR (%), C T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTThreeTprOneCI` | [88.7, 96.0] | TPR at 1% FPR (%), C T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTThreeTprOneN` | 600 | TPR at 1% FPR (%), C T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTThreeTprOneP` | n/a | TPR at 1% FPR (%), C T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashCTThreeTprFive` | 93.7 | TPR at 5% FPR (%), C T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashCTThreeTprFiveLo` | 90.3 | TPR at 5% FPR (%), C T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashCTThreeTprFiveHi` | 96.3 | TPR at 5% FPR (%), C T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashCTThreeTprFiveCI` | [90.3, 96.3] | TPR at 5% FPR (%), C T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashCTThreeTprFiveN` | 600 | TPR at 5% FPR (%), C T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashCTThreeTprFiveP` | n/a | TPR at 5% FPR (%), C T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTZero` | 0.79 | AUROC R T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTZeroLo` | 0.76 | AUROC R T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTZeroHi` | 0.83 | AUROC R T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTZeroCI` | [0.76, 0.83] | AUROC R T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTZeroN` | 585 | AUROC R T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTZeroP` | n/a | AUROC R T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTZeroTprOne` | 0.0 | TPR at 1% FPR (%), R T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTZeroTprOneLo` | 0.0 | TPR at 1% FPR (%), R T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTZeroTprOneHi` | 0.0 | TPR at 1% FPR (%), R T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTZeroTprOneCI` | [0.0, 0.0] | TPR at 1% FPR (%), R T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTZeroTprOneN` | 585 | TPR at 1% FPR (%), R T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTZeroTprOneP` | n/a | TPR at 1% FPR (%), R T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTZeroTprFive` | 0.0 | TPR at 5% FPR (%), R T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTZeroTprFiveLo` | 0.0 | TPR at 5% FPR (%), R T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTZeroTprFiveHi` | 0.0 | TPR at 5% FPR (%), R T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTZeroTprFiveCI` | [0.0, 0.0] | TPR at 5% FPR (%), R T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTZeroTprFiveN` | 585 | TPR at 5% FPR (%), R T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTZeroTprFiveP` | n/a | TPR at 5% FPR (%), R T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTOne` | 0.79 | AUROC R T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTOneLo` | 0.75 | AUROC R T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTOneHi` | 0.83 | AUROC R T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTOneCI` | [0.75, 0.83] | AUROC R T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTOneN` | 589 | AUROC R T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTOneP` | n/a | AUROC R T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTOneTprOne` | 0.0 | TPR at 1% FPR (%), R T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTOneTprOneLo` | 0.0 | TPR at 1% FPR (%), R T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTOneTprOneHi` | 0.0 | TPR at 1% FPR (%), R T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTOneTprOneCI` | [0.0, 0.0] | TPR at 1% FPR (%), R T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTOneTprOneN` | 589 | TPR at 1% FPR (%), R T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTOneTprOneP` | n/a | TPR at 1% FPR (%), R T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTOneTprFive` | 0.0 | TPR at 5% FPR (%), R T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTOneTprFiveLo` | 0.0 | TPR at 5% FPR (%), R T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTOneTprFiveHi` | 0.0 | TPR at 5% FPR (%), R T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTOneTprFiveCI` | [0.0, 0.0] | TPR at 5% FPR (%), R T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTOneTprFiveN` | 589 | TPR at 5% FPR (%), R T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTOneTprFiveP` | n/a | TPR at 5% FPR (%), R T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTTwo` | 0.79 | AUROC R T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTTwoLo` | 0.76 | AUROC R T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTTwoHi` | 0.83 | AUROC R T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTTwoCI` | [0.76, 0.83] | AUROC R T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTTwoN` | 586 | AUROC R T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTTwoP` | n/a | AUROC R T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTTwoTprOne` | 0.0 | TPR at 1% FPR (%), R T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTTwoTprOneLo` | 0.0 | TPR at 1% FPR (%), R T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTTwoTprOneHi` | 0.0 | TPR at 1% FPR (%), R T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTTwoTprOneCI` | [0.0, 0.0] | TPR at 1% FPR (%), R T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTTwoTprOneN` | 586 | TPR at 1% FPR (%), R T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTTwoTprOneP` | n/a | TPR at 1% FPR (%), R T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTTwoTprFive` | 0.0 | TPR at 5% FPR (%), R T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTTwoTprFiveLo` | 0.0 | TPR at 5% FPR (%), R T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTTwoTprFiveHi` | 0.0 | TPR at 5% FPR (%), R T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTTwoTprFiveCI` | [0.0, 0.0] | TPR at 5% FPR (%), R T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTTwoTprFiveN` | 586 | TPR at 5% FPR (%), R T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTTwoTprFiveP` | n/a | TPR at 5% FPR (%), R T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTThree` | 0.79 | AUROC R T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTThreeLo` | 0.76 | AUROC R T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTThreeHi` | 0.83 | AUROC R T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTThreeCI` | [0.76, 0.83] | AUROC R T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTThreeN` | 595 | AUROC R T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTThreeP` | n/a | AUROC R T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTThreeTprOne` | 0.0 | TPR at 1% FPR (%), R T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTThreeTprOneLo` | 0.0 | TPR at 1% FPR (%), R T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTThreeTprOneHi` | 0.0 | TPR at 1% FPR (%), R T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTThreeTprOneCI` | [0.0, 0.0] | TPR at 1% FPR (%), R T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTThreeTprOneN` | 595 | TPR at 1% FPR (%), R T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTThreeTprOneP` | n/a | TPR at 1% FPR (%), R T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRTThreeTprFive` | 0.0 | TPR at 5% FPR (%), R T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRTThreeTprFiveLo` | 0.0 | TPR at 5% FPR (%), R T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRTThreeTprFiveHi` | 0.0 | TPR at 5% FPR (%), R T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRTThreeTprFiveCI` | [0.0, 0.0] | TPR at 5% FPR (%), R T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRTThreeTprFiveN` | 595 | TPR at 5% FPR (%), R T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRTThreeTprFiveP` | n/a | TPR at 5% FPR (%), R T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTZero` | 0.62 | AUROC r_field T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTZeroLo` | 0.60 | AUROC r_field T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTZeroHi` | 0.64 | AUROC r_field T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTZeroCI` | [0.60, 0.64] | AUROC r_field T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTZeroN` | 600 | AUROC r_field T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTZeroP` | n/a | AUROC r_field T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTZeroTprOne` | 1.3 | TPR at 1% FPR (%), r_field T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTZeroTprOneLo` | 0.7 | TPR at 1% FPR (%), r_field T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTZeroTprOneHi` | 5.0 | TPR at 1% FPR (%), r_field T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTZeroTprOneCI` | [0.7, 5.0] | TPR at 1% FPR (%), r_field T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTZeroTprOneN` | 600 | TPR at 1% FPR (%), r_field T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTZeroTprOneP` | n/a | TPR at 1% FPR (%), r_field T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTZeroTprFive` | 10.0 | TPR at 5% FPR (%), r_field T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTZeroTprFiveLo` | 6.3 | TPR at 5% FPR (%), r_field T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTZeroTprFiveHi` | 13.3 | TPR at 5% FPR (%), r_field T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTZeroTprFiveCI` | [6.3, 13.3] | TPR at 5% FPR (%), r_field T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTZeroTprFiveN` | 600 | TPR at 5% FPR (%), r_field T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTZeroTprFiveP` | n/a | TPR at 5% FPR (%), r_field T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTOne` | 0.61 | AUROC r_field T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTOneLo` | 0.59 | AUROC r_field T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTOneHi` | 0.63 | AUROC r_field T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTOneCI` | [0.59, 0.63] | AUROC r_field T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTOneN` | 594 | AUROC r_field T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTOneP` | n/a | AUROC r_field T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTOneTprOne` | 2.7 | TPR at 1% FPR (%), r_field T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTOneTprOneLo` | 1.0 | TPR at 1% FPR (%), r_field T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTOneTprOneHi` | 6.3 | TPR at 1% FPR (%), r_field T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTOneTprOneCI` | [1.0, 6.3] | TPR at 1% FPR (%), r_field T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTOneTprOneN` | 594 | TPR at 1% FPR (%), r_field T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTOneTprOneP` | n/a | TPR at 1% FPR (%), r_field T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTOneTprFive` | 11.1 | TPR at 5% FPR (%), r_field T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTOneTprFiveLo` | 6.8 | TPR at 5% FPR (%), r_field T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTOneTprFiveHi` | 15.2 | TPR at 5% FPR (%), r_field T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTOneTprFiveCI` | [6.8, 15.2] | TPR at 5% FPR (%), r_field T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTOneTprFiveN` | 594 | TPR at 5% FPR (%), r_field T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTOneTprFiveP` | n/a | TPR at 5% FPR (%), r_field T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTTwo` | 0.62 | AUROC r_field T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTTwoLo` | 0.60 | AUROC r_field T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTTwoHi` | 0.65 | AUROC r_field T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTTwoCI` | [0.60, 0.65] | AUROC r_field T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTTwoN` | 596 | AUROC r_field T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTTwoP` | n/a | AUROC r_field T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTTwoTprOne` | 2.3 | TPR at 1% FPR (%), r_field T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTTwoTprOneLo` | 1.0 | TPR at 1% FPR (%), r_field T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTTwoTprOneHi` | 5.4 | TPR at 1% FPR (%), r_field T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTTwoTprOneCI` | [1.0, 5.4] | TPR at 1% FPR (%), r_field T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTTwoTprOneN` | 596 | TPR at 1% FPR (%), r_field T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTTwoTprOneP` | n/a | TPR at 1% FPR (%), r_field T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTTwoTprFive` | 11.7 | TPR at 5% FPR (%), r_field T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTTwoTprFiveLo` | 7.3 | TPR at 5% FPR (%), r_field T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTTwoTprFiveHi` | 15.5 | TPR at 5% FPR (%), r_field T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTTwoTprFiveCI` | [7.3, 15.5] | TPR at 5% FPR (%), r_field T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTTwoTprFiveN` | 596 | TPR at 5% FPR (%), r_field T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTTwoTprFiveP` | n/a | TPR at 5% FPR (%), r_field T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTThree` | 0.64 | AUROC r_field T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTThreeLo` | 0.61 | AUROC r_field T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTThreeHi` | 0.67 | AUROC r_field T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTThreeCI` | [0.61, 0.67] | AUROC r_field T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTThreeN` | 600 | AUROC r_field T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTThreeP` | n/a | AUROC r_field T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTThreeTprOne` | 2.7 | TPR at 1% FPR (%), r_field T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTThreeTprOneLo` | 1.0 | TPR at 1% FPR (%), r_field T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTThreeTprOneHi` | 7.0 | TPR at 1% FPR (%), r_field T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTThreeTprOneCI` | [1.0, 7.0] | TPR at 1% FPR (%), r_field T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTThreeTprOneN` | 600 | TPR at 1% FPR (%), r_field T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTThreeTprOneP` | n/a | TPR at 1% FPR (%), r_field T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashRFieldTThreeTprFive` | 12.7 | TPR at 5% FPR (%), r_field T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashRFieldTThreeTprFiveLo` | 8.0 | TPR at 5% FPR (%), r_field T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTThreeTprFiveHi` | 16.7 | TPR at 5% FPR (%), r_field T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashRFieldTThreeTprFiveCI` | [8.0, 16.7] | TPR at 5% FPR (%), r_field T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashRFieldTThreeTprFiveN` | 600 | TPR at 5% FPR (%), r_field T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashRFieldTThreeTprFiveP` | n/a | TPR at 5% FPR (%), r_field T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTZero` | 0.65 | AUROC f_trace T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTZeroLo` | 0.63 | AUROC f_trace T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTZeroHi` | 0.67 | AUROC f_trace T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTZeroCI` | [0.63, 0.67] | AUROC f_trace T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTZeroN` | 600 | AUROC f_trace T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTZeroP` | n/a | AUROC f_trace T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTZeroTprOne` | 2.7 | TPR at 1% FPR (%), f_trace T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTZeroTprOneLo` | 1.3 | TPR at 1% FPR (%), f_trace T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTZeroTprOneHi` | 6.0 | TPR at 1% FPR (%), f_trace T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTZeroTprOneCI` | [1.3, 6.0] | TPR at 1% FPR (%), f_trace T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTZeroTprOneN` | 600 | TPR at 1% FPR (%), f_trace T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTZeroTprOneP` | n/a | TPR at 1% FPR (%), f_trace T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTZeroTprFive` | 16.3 | TPR at 5% FPR (%), f_trace T0, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTZeroTprFiveLo` | 5.0 | TPR at 5% FPR (%), f_trace T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTZeroTprFiveHi` | 21.3 | TPR at 5% FPR (%), f_trace T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTZeroTprFiveCI` | [5.0, 21.3] | TPR at 5% FPR (%), f_trace T0, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTZeroTprFiveN` | 600 | TPR at 5% FPR (%), f_trace T0, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTZeroTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTOne` | 0.64 | AUROC f_trace T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTOneLo` | 0.61 | AUROC f_trace T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTOneHi` | 0.67 | AUROC f_trace T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTOneCI` | [0.61, 0.67] | AUROC f_trace T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTOneN` | 594 | AUROC f_trace T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTOneP` | n/a | AUROC f_trace T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTOneTprOne` | 4.7 | TPR at 1% FPR (%), f_trace T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTOneTprOneLo` | 2.3 | TPR at 1% FPR (%), f_trace T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTOneTprOneHi` | 8.9 | TPR at 1% FPR (%), f_trace T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTOneTprOneCI` | [2.3, 8.9] | TPR at 1% FPR (%), f_trace T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTOneTprOneN` | 594 | TPR at 1% FPR (%), f_trace T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTOneTprOneP` | n/a | TPR at 1% FPR (%), f_trace T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTOneTprFive` | 14.5 | TPR at 5% FPR (%), f_trace T1, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTOneTprFiveLo` | 6.8 | TPR at 5% FPR (%), f_trace T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTOneTprFiveHi` | 22.9 | TPR at 5% FPR (%), f_trace T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTOneTprFiveCI` | [6.8, 22.9] | TPR at 5% FPR (%), f_trace T1, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTOneTprFiveN` | 594 | TPR at 5% FPR (%), f_trace T1, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTOneTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTTwo` | 0.67 | AUROC f_trace T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTTwoLo` | 0.64 | AUROC f_trace T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTTwoHi` | 0.69 | AUROC f_trace T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTTwoCI` | [0.64, 0.69] | AUROC f_trace T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTTwoN` | 596 | AUROC f_trace T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTTwoP` | n/a | AUROC f_trace T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTTwoTprOne` | 6.4 | TPR at 1% FPR (%), f_trace T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTTwoTprOneLo` | 3.7 | TPR at 1% FPR (%), f_trace T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTTwoTprOneHi` | 10.4 | TPR at 1% FPR (%), f_trace T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTTwoTprOneCI` | [3.7, 10.4] | TPR at 1% FPR (%), f_trace T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTTwoTprOneN` | 596 | TPR at 1% FPR (%), f_trace T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTTwoTprOneP` | n/a | TPR at 1% FPR (%), f_trace T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTTwoTprFive` | 20.1 | TPR at 5% FPR (%), f_trace T2, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTTwoTprFiveLo` | 7.8 | TPR at 5% FPR (%), f_trace T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTTwoTprFiveHi` | 25.5 | TPR at 5% FPR (%), f_trace T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTTwoTprFiveCI` | [7.8, 25.5] | TPR at 5% FPR (%), f_trace T2, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTTwoTprFiveN` | 596 | TPR at 5% FPR (%), f_trace T2, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTTwoTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTThree` | 0.68 | AUROC f_trace T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTThreeLo` | 0.66 | AUROC f_trace T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTThreeHi` | 0.71 | AUROC f_trace T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTThreeCI` | [0.66, 0.71] | AUROC f_trace T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTThreeN` | 600 | AUROC f_trace T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTThreeP` | n/a | AUROC f_trace T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTThreeTprOne` | 5.0 | TPR at 1% FPR (%), f_trace T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTThreeTprOneLo` | 3.0 | TPR at 1% FPR (%), f_trace T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTThreeTprOneHi` | 11.0 | TPR at 1% FPR (%), f_trace T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTThreeTprOneCI` | [3.0, 11.0] | TPR at 1% FPR (%), f_trace T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTThreeTprOneN` | 600 | TPR at 1% FPR (%), f_trace T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTThreeTprOneP` | n/a | TPR at 1% FPR (%), f_trace T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetDeepSeekVFourFlashFTraceTThreeTprFive` | 22.7 | TPR at 5% FPR (%), f_trace T3, deepseek-v4-flash |
| `\DetDeepSeekVFourFlashFTraceTThreeTprFiveLo` | 8.3 | TPR at 5% FPR (%), f_trace T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTThreeTprFiveHi` | 29.3 | TPR at 5% FPR (%), f_trace T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetDeepSeekVFourFlashFTraceTThreeTprFiveCI` | [8.3, 29.3] | TPR at 5% FPR (%), f_trace T3, deepseek-v4-flash, 95% CI |
| `\DetDeepSeekVFourFlashFTraceTThreeTprFiveN` | 600 | TPR at 5% FPR (%), f_trace T3, deepseek-v4-flash, n |
| `\DetDeepSeekVFourFlashFTraceTThreeTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTZero` | 0.78 | AUROC V T0, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBVTZeroLo` | 0.74 | AUROC V T0, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTZeroHi` | 0.81 | AUROC V T0, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTZeroCI` | [0.74, 0.81] | AUROC V T0, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTZeroN` | 598 | AUROC V T0, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBVTZeroP` | n/a | AUROC V T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTZeroTprOne` | 61.4 | TPR at 1% FPR (%), V T0, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBVTZeroTprOneLo` | 56.9 | TPR at 1% FPR (%), V T0, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTZeroTprOneHi` | 66.3 | TPR at 1% FPR (%), V T0, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTZeroTprOneCI` | [56.9, 66.3] | TPR at 1% FPR (%), V T0, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTZeroTprOneN` | 598 | TPR at 1% FPR (%), V T0, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBVTZeroTprOneP` | n/a | TPR at 1% FPR (%), V T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTZeroTprFive` | 62.4 | TPR at 5% FPR (%), V T0, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBVTZeroTprFiveLo` | 57.4 | TPR at 5% FPR (%), V T0, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTZeroTprFiveHi` | 66.9 | TPR at 5% FPR (%), V T0, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTZeroTprFiveCI` | [57.4, 66.9] | TPR at 5% FPR (%), V T0, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTZeroTprFiveN` | 598 | TPR at 5% FPR (%), V T0, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBVTZeroTprFiveP` | n/a | TPR at 5% FPR (%), V T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTOne` | 0.56 | AUROC V T1, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBVTOneLo` | 0.51 | AUROC V T1, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTOneHi` | 0.61 | AUROC V T1, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTOneCI` | [0.51, 0.61] | AUROC V T1, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTOneN` | 586 | AUROC V T1, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBVTOneP` | n/a | AUROC V T1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTOneTprOne` | 15.4 | TPR at 1% FPR (%), V T1, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBVTOneTprOneLo` | 12.6 | TPR at 1% FPR (%), V T1, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTOneTprOneHi` | 19.7 | TPR at 1% FPR (%), V T1, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTOneTprOneCI` | [12.6, 19.7] | TPR at 1% FPR (%), V T1, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTOneTprOneN` | 586 | TPR at 1% FPR (%), V T1, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBVTOneTprOneP` | n/a | TPR at 1% FPR (%), V T1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTOneTprFive` | 17.4 | TPR at 5% FPR (%), V T1, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBVTOneTprFiveLo` | 13.9 | TPR at 5% FPR (%), V T1, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTOneTprFiveHi` | 20.9 | TPR at 5% FPR (%), V T1, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTOneTprFiveCI` | [13.9, 20.9] | TPR at 5% FPR (%), V T1, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTOneTprFiveN` | 586 | TPR at 5% FPR (%), V T1, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBVTOneTprFiveP` | n/a | TPR at 5% FPR (%), V T1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTTwo` | 0.55 | AUROC V T2, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBVTTwoLo` | 0.50 | AUROC V T2, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTTwoHi` | 0.60 | AUROC V T2, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTTwoCI` | [0.50, 0.60] | AUROC V T2, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTTwoN` | 586 | AUROC V T2, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBVTTwoP` | n/a | AUROC V T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTTwoTprOne` | 11.6 | TPR at 1% FPR (%), V T2, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBVTTwoTprOneLo` | 8.6 | TPR at 1% FPR (%), V T2, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTTwoTprOneHi` | 16.2 | TPR at 1% FPR (%), V T2, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTTwoTprOneCI` | [8.6, 16.2] | TPR at 1% FPR (%), V T2, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTTwoTprOneN` | 586 | TPR at 1% FPR (%), V T2, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBVTTwoTprOneP` | n/a | TPR at 1% FPR (%), V T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTTwoTprFive` | 14.3 | TPR at 5% FPR (%), V T2, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBVTTwoTprFiveLo` | 10.6 | TPR at 5% FPR (%), V T2, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTTwoTprFiveHi` | 17.7 | TPR at 5% FPR (%), V T2, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTTwoTprFiveCI` | [10.6, 17.7] | TPR at 5% FPR (%), V T2, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTTwoTprFiveN` | 586 | TPR at 5% FPR (%), V T2, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBVTTwoTprFiveP` | n/a | TPR at 5% FPR (%), V T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTThree` | 0.54 | AUROC V T3, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBVTThreeLo` | 0.49 | AUROC V T3, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTThreeHi` | 0.58 | AUROC V T3, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTThreeCI` | [0.49, 0.58] | AUROC V T3, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTThreeN` | 595 | AUROC V T3, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBVTThreeP` | n/a | AUROC V T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTThreeTprOne` | 8.4 | TPR at 1% FPR (%), V T3, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBVTThreeTprOneLo` | 5.7 | TPR at 1% FPR (%), V T3, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTThreeTprOneHi` | 14.6 | TPR at 1% FPR (%), V T3, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTThreeTprOneCI` | [5.7, 14.6] | TPR at 1% FPR (%), V T3, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTThreeTprOneN` | 595 | TPR at 1% FPR (%), V T3, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBVTThreeTprOneP` | n/a | TPR at 1% FPR (%), V T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBVTThreeTprFive` | 12.1 | TPR at 5% FPR (%), V T3, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBVTThreeTprFiveLo` | 8.2 | TPR at 5% FPR (%), V T3, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTThreeTprFiveHi` | 16.2 | TPR at 5% FPR (%), V T3, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBVTThreeTprFiveCI` | [8.2, 16.2] | TPR at 5% FPR (%), V T3, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBVTThreeTprFiveN` | 595 | TPR at 5% FPR (%), V T3, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBVTThreeTprFiveP` | n/a | TPR at 5% FPR (%), V T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTZero` | 1.00 | AUROC C T0, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBCTZeroLo` | 1.00 | AUROC C T0, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTZeroHi` | 1.00 | AUROC C T0, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTZeroCI` | [1.00, 1.00] | AUROC C T0, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTZeroN` | 595 | AUROC C T0, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBCTZeroP` | n/a | AUROC C T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTZeroTprOne` | 99.3 | TPR at 1% FPR (%), C T0, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBCTZeroTprOneLo` | 75.0 | TPR at 1% FPR (%), C T0, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTZeroTprOneHi` | 100.0 | TPR at 1% FPR (%), C T0, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTZeroTprOneCI` | [75.0, 100.0] | TPR at 1% FPR (%), C T0, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTZeroTprOneN` | 595 | TPR at 1% FPR (%), C T0, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBCTZeroTprOneP` | n/a | TPR at 1% FPR (%), C T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTZeroTprFive` | 100.0 | TPR at 5% FPR (%), C T0, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBCTZeroTprFiveLo` | 98.7 | TPR at 5% FPR (%), C T0, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTZeroTprFiveHi` | 100.0 | TPR at 5% FPR (%), C T0, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTZeroTprFiveCI` | [98.7, 100.0] | TPR at 5% FPR (%), C T0, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTZeroTprFiveN` | 595 | TPR at 5% FPR (%), C T0, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBCTZeroTprFiveP` | n/a | TPR at 5% FPR (%), C T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTOne` | 1.00 | AUROC C T1, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBCTOneLo` | 1.00 | AUROC C T1, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTOneHi` | 1.00 | AUROC C T1, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTOneCI` | [1.00, 1.00] | AUROC C T1, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTOneN` | 581 | AUROC C T1, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBCTOneP` | n/a | AUROC C T1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTOneTprOne` | 99.3 | TPR at 1% FPR (%), C T1, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBCTOneTprOneLo` | 72.9 | TPR at 1% FPR (%), C T1, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTOneTprOneHi` | 100.0 | TPR at 1% FPR (%), C T1, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTOneTprOneCI` | [72.9, 100.0] | TPR at 1% FPR (%), C T1, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTOneTprOneN` | 581 | TPR at 1% FPR (%), C T1, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBCTOneTprOneP` | n/a | TPR at 1% FPR (%), C T1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTOneTprFive` | 99.7 | TPR at 5% FPR (%), C T1, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBCTOneTprFiveLo` | 98.6 | TPR at 5% FPR (%), C T1, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTOneTprFiveHi` | 100.0 | TPR at 5% FPR (%), C T1, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTOneTprFiveCI` | [98.6, 100.0] | TPR at 5% FPR (%), C T1, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTOneTprFiveN` | 581 | TPR at 5% FPR (%), C T1, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBCTOneTprFiveP` | n/a | TPR at 5% FPR (%), C T1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTTwo` | 1.00 | AUROC C T2, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBCTTwoLo` | 1.00 | AUROC C T2, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTTwoHi` | 1.00 | AUROC C T2, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTTwoCI` | [1.00, 1.00] | AUROC C T2, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTTwoN` | 581 | AUROC C T2, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBCTTwoP` | n/a | AUROC C T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTTwoTprOne` | 99.0 | TPR at 1% FPR (%), C T2, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBCTTwoTprOneLo` | 72.1 | TPR at 1% FPR (%), C T2, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTTwoTprOneHi` | 99.7 | TPR at 1% FPR (%), C T2, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTTwoTprOneCI` | [72.1, 99.7] | TPR at 1% FPR (%), C T2, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTTwoTprOneN` | 581 | TPR at 1% FPR (%), C T2, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBCTTwoTprOneP` | n/a | TPR at 1% FPR (%), C T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTTwoTprFive` | 100.0 | TPR at 5% FPR (%), C T2, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBCTTwoTprFiveLo` | 98.0 | TPR at 5% FPR (%), C T2, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTTwoTprFiveHi` | 100.0 | TPR at 5% FPR (%), C T2, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTTwoTprFiveCI` | [98.0, 100.0] | TPR at 5% FPR (%), C T2, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTTwoTprFiveN` | 581 | TPR at 5% FPR (%), C T2, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBCTTwoTprFiveP` | n/a | TPR at 5% FPR (%), C T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTThree` | 1.00 | AUROC C T3, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBCTThreeLo` | 1.00 | AUROC C T3, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTThreeHi` | 1.00 | AUROC C T3, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTThreeCI` | [1.00, 1.00] | AUROC C T3, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTThreeN` | 590 | AUROC C T3, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBCTThreeP` | n/a | AUROC C T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTThreeTprOne` | 99.3 | TPR at 1% FPR (%), C T3, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBCTThreeTprOneLo` | 73.7 | TPR at 1% FPR (%), C T3, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTThreeTprOneHi` | 100.0 | TPR at 1% FPR (%), C T3, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTThreeTprOneCI` | [73.7, 100.0] | TPR at 1% FPR (%), C T3, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTThreeTprOneN` | 590 | TPR at 1% FPR (%), C T3, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBCTThreeTprOneP` | n/a | TPR at 1% FPR (%), C T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBCTThreeTprFive` | 100.0 | TPR at 5% FPR (%), C T3, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBCTThreeTprFiveLo` | 98.6 | TPR at 5% FPR (%), C T3, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTThreeTprFiveHi` | 100.0 | TPR at 5% FPR (%), C T3, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBCTThreeTprFiveCI` | [98.6, 100.0] | TPR at 5% FPR (%), C T3, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBCTThreeTprFiveN` | 590 | TPR at 5% FPR (%), C T3, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBCTThreeTprFiveP` | n/a | TPR at 5% FPR (%), C T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTZero` | 0.99 | AUROC R T0, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRTZeroLo` | 0.98 | AUROC R T0, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTZeroHi` | 1.00 | AUROC R T0, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTZeroCI` | [0.98, 1.00] | AUROC R T0, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTZeroN` | 600 | AUROC R T0, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRTZeroP` | n/a | AUROC R T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTZeroTprOne` | 86.7 | TPR at 1% FPR (%), R T0, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRTZeroTprOneLo` | 55.0 | TPR at 1% FPR (%), R T0, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTZeroTprOneHi` | 91.0 | TPR at 1% FPR (%), R T0, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTZeroTprOneCI` | [55.0, 91.0] | TPR at 1% FPR (%), R T0, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTZeroTprOneN` | 600 | TPR at 1% FPR (%), R T0, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRTZeroTprOneP` | n/a | TPR at 1% FPR (%), R T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTZeroTprFive` | 98.7 | TPR at 5% FPR (%), R T0, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRTZeroTprFiveLo` | 83.7 | TPR at 5% FPR (%), R T0, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTZeroTprFiveHi` | 99.7 | TPR at 5% FPR (%), R T0, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTZeroTprFiveCI` | [83.7, 99.7] | TPR at 5% FPR (%), R T0, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTZeroTprFiveN` | 600 | TPR at 5% FPR (%), R T0, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRTZeroTprFiveP` | n/a | TPR at 5% FPR (%), R T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTOne` | 0.99 | AUROC R T1, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRTOneLo` | 0.98 | AUROC R T1, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTOneHi` | 1.00 | AUROC R T1, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTOneCI` | [0.98, 1.00] | AUROC R T1, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTOneN` | 586 | AUROC R T1, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRTOneP` | n/a | AUROC R T1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTOneTprOne` | 84.0 | TPR at 1% FPR (%), R T1, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRTOneTprOneLo` | 0.0 | TPR at 1% FPR (%), R T1, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTOneTprOneHi` | 88.2 | TPR at 1% FPR (%), R T1, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTOneTprOneCI` | [0.0, 88.2] | TPR at 1% FPR (%), R T1, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTOneTprOneN` | 586 | TPR at 1% FPR (%), R T1, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRTOneTprOneP` | n/a | TPR at 1% FPR (%), R T1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTOneTprFive` | 98.0 | TPR at 5% FPR (%), R T1, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRTOneTprFiveLo` | 81.0 | TPR at 5% FPR (%), R T1, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTOneTprFiveHi` | 99.3 | TPR at 5% FPR (%), R T1, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTOneTprFiveCI` | [81.0, 99.3] | TPR at 5% FPR (%), R T1, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTOneTprFiveN` | 586 | TPR at 5% FPR (%), R T1, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRTOneTprFiveP` | n/a | TPR at 5% FPR (%), R T1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTTwo` | 0.99 | AUROC R T2, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRTTwoLo` | 0.98 | AUROC R T2, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTTwoHi` | 1.00 | AUROC R T2, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTTwoCI` | [0.98, 1.00] | AUROC R T2, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTTwoN` | 586 | AUROC R T2, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRTTwoP` | n/a | AUROC R T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTTwoTprOne` | 83.6 | TPR at 1% FPR (%), R T2, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRTTwoTprOneLo` | 0.0 | TPR at 1% FPR (%), R T2, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTTwoTprOneHi` | 88.4 | TPR at 1% FPR (%), R T2, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTTwoTprOneCI` | [0.0, 88.4] | TPR at 1% FPR (%), R T2, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTTwoTprOneN` | 586 | TPR at 1% FPR (%), R T2, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRTTwoTprOneP` | n/a | TPR at 1% FPR (%), R T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTTwoTprFive` | 98.0 | TPR at 5% FPR (%), R T2, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRTTwoTprFiveLo` | 80.0 | TPR at 5% FPR (%), R T2, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTTwoTprFiveHi` | 99.3 | TPR at 5% FPR (%), R T2, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTTwoTprFiveCI` | [80.0, 99.3] | TPR at 5% FPR (%), R T2, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTTwoTprFiveN` | 586 | TPR at 5% FPR (%), R T2, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRTTwoTprFiveP` | n/a | TPR at 5% FPR (%), R T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTThree` | 0.99 | AUROC R T3, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRTThreeLo` | 0.99 | AUROC R T3, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTThreeHi` | 1.00 | AUROC R T3, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTThreeCI` | [0.99, 1.00] | AUROC R T3, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTThreeN` | 596 | AUROC R T3, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRTThreeP` | n/a | AUROC R T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTThreeTprOne` | 87.6 | TPR at 1% FPR (%), R T3, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRTThreeTprOneLo` | 0.0 | TPR at 1% FPR (%), R T3, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTThreeTprOneHi` | 91.3 | TPR at 1% FPR (%), R T3, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTThreeTprOneCI` | [0.0, 91.3] | TPR at 1% FPR (%), R T3, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTThreeTprOneN` | 596 | TPR at 1% FPR (%), R T3, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRTThreeTprOneP` | n/a | TPR at 1% FPR (%), R T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRTThreeTprFive` | 99.7 | TPR at 5% FPR (%), R T3, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRTThreeTprFiveLo` | 84.9 | TPR at 5% FPR (%), R T3, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTThreeTprFiveHi` | 100.0 | TPR at 5% FPR (%), R T3, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRTThreeTprFiveCI` | [84.9, 100.0] | TPR at 5% FPR (%), R T3, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRTThreeTprFiveN` | 596 | TPR at 5% FPR (%), R T3, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRTThreeTprFiveP` | n/a | TPR at 5% FPR (%), R T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTZero` | 0.62 | AUROC r_field T0, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroLo` | 0.60 | AUROC r_field T0, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroHi` | 0.65 | AUROC r_field T0, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroCI` | [0.60, 0.65] | AUROC r_field T0, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroN` | 600 | AUROC r_field T0, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroP` | n/a | AUROC r_field T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprOne` | 0.7 | TPR at 1% FPR (%), r_field T0, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprOneLo` | 0.0 | TPR at 1% FPR (%), r_field T0, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprOneHi` | 3.7 | TPR at 1% FPR (%), r_field T0, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprOneCI` | [0.0, 3.7] | TPR at 1% FPR (%), r_field T0, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprOneN` | 600 | TPR at 1% FPR (%), r_field T0, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprOneP` | n/a | TPR at 1% FPR (%), r_field T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprFive` | 9.3 | TPR at 5% FPR (%), r_field T0, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprFiveLo` | 6.0 | TPR at 5% FPR (%), r_field T0, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprFiveHi` | 11.3 | TPR at 5% FPR (%), r_field T0, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprFiveCI` | [6.0, 11.3] | TPR at 5% FPR (%), r_field T0, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprFiveN` | 600 | TPR at 5% FPR (%), r_field T0, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRFieldTZeroTprFiveP` | n/a | TPR at 5% FPR (%), r_field T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTOne` | 0.62 | AUROC r_field T1, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRFieldTOneLo` | 0.60 | AUROC r_field T1, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTOneHi` | 0.65 | AUROC r_field T1, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTOneCI` | [0.60, 0.65] | AUROC r_field T1, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTOneN` | 586 | AUROC r_field T1, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRFieldTOneP` | n/a | AUROC r_field T1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprOne` | 1.7 | TPR at 1% FPR (%), r_field T1, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprOneLo` | 0.0 | TPR at 1% FPR (%), r_field T1, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprOneHi` | 3.4 | TPR at 1% FPR (%), r_field T1, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprOneCI` | [0.0, 3.4] | TPR at 1% FPR (%), r_field T1, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprOneN` | 586 | TPR at 1% FPR (%), r_field T1, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprOneP` | n/a | TPR at 1% FPR (%), r_field T1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprFive` | 9.2 | TPR at 5% FPR (%), r_field T1, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprFiveLo` | 6.5 | TPR at 5% FPR (%), r_field T1, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprFiveHi` | 13.2 | TPR at 5% FPR (%), r_field T1, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprFiveCI` | [6.5, 13.2] | TPR at 5% FPR (%), r_field T1, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprFiveN` | 586 | TPR at 5% FPR (%), r_field T1, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRFieldTOneTprFiveP` | n/a | TPR at 5% FPR (%), r_field T1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTTwo` | 0.62 | AUROC r_field T2, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoLo` | 0.60 | AUROC r_field T2, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoHi` | 0.65 | AUROC r_field T2, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoCI` | [0.60, 0.65] | AUROC r_field T2, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoN` | 586 | AUROC r_field T2, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoP` | n/a | AUROC r_field T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprOne` | 1.7 | TPR at 1% FPR (%), r_field T2, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprOneLo` | 0.0 | TPR at 1% FPR (%), r_field T2, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprOneHi` | 5.1 | TPR at 1% FPR (%), r_field T2, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprOneCI` | [0.0, 5.1] | TPR at 1% FPR (%), r_field T2, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprOneN` | 586 | TPR at 1% FPR (%), r_field T2, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprOneP` | n/a | TPR at 1% FPR (%), r_field T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprFive` | 9.2 | TPR at 5% FPR (%), r_field T2, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprFiveLo` | 6.5 | TPR at 5% FPR (%), r_field T2, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprFiveHi` | 14.1 | TPR at 5% FPR (%), r_field T2, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprFiveCI` | [6.5, 14.1] | TPR at 5% FPR (%), r_field T2, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprFiveN` | 586 | TPR at 5% FPR (%), r_field T2, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRFieldTTwoTprFiveP` | n/a | TPR at 5% FPR (%), r_field T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTThree` | 0.63 | AUROC r_field T3, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeLo` | 0.60 | AUROC r_field T3, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeHi` | 0.65 | AUROC r_field T3, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeCI` | [0.60, 0.65] | AUROC r_field T3, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeN` | 596 | AUROC r_field T3, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeP` | n/a | AUROC r_field T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprOne` | 2.0 | TPR at 1% FPR (%), r_field T3, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprOneLo` | 0.0 | TPR at 1% FPR (%), r_field T3, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprOneHi` | 6.0 | TPR at 1% FPR (%), r_field T3, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprOneCI` | [0.0, 6.0] | TPR at 1% FPR (%), r_field T3, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprOneN` | 596 | TPR at 1% FPR (%), r_field T3, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprOneP` | n/a | TPR at 1% FPR (%), r_field T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprFive` | 10.7 | TPR at 5% FPR (%), r_field T3, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprFiveLo` | 8.0 | TPR at 5% FPR (%), r_field T3, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprFiveHi` | 15.0 | TPR at 5% FPR (%), r_field T3, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprFiveCI` | [8.0, 15.0] | TPR at 5% FPR (%), r_field T3, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprFiveN` | 596 | TPR at 5% FPR (%), r_field T3, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBRFieldTThreeTprFiveP` | n/a | TPR at 5% FPR (%), r_field T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTZero` | 0.66 | AUROC f_trace T0, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroLo` | 0.64 | AUROC f_trace T0, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroHi` | 0.68 | AUROC f_trace T0, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroCI` | [0.64, 0.68] | AUROC f_trace T0, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroN` | 600 | AUROC f_trace T0, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroP` | n/a | AUROC f_trace T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprOne` | 15.3 | TPR at 1% FPR (%), f_trace T0, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprOneLo` | 5.7 | TPR at 1% FPR (%), f_trace T0, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprOneHi` | 21.3 | TPR at 1% FPR (%), f_trace T0, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprOneCI` | [5.7, 21.3] | TPR at 1% FPR (%), f_trace T0, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprOneN` | 600 | TPR at 1% FPR (%), f_trace T0, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprOneP` | n/a | TPR at 1% FPR (%), f_trace T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprFive` | 25.0 | TPR at 5% FPR (%), f_trace T0, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprFiveLo` | 16.7 | TPR at 5% FPR (%), f_trace T0, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprFiveHi` | 29.7 | TPR at 5% FPR (%), f_trace T0, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprFiveCI` | [16.7, 29.7] | TPR at 5% FPR (%), f_trace T0, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprFiveN` | 600 | TPR at 5% FPR (%), f_trace T0, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBFTraceTZeroTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTOne` | 0.66 | AUROC f_trace T1, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBFTraceTOneLo` | 0.64 | AUROC f_trace T1, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTOneHi` | 0.68 | AUROC f_trace T1, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTOneCI` | [0.64, 0.68] | AUROC f_trace T1, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTOneN` | 586 | AUROC f_trace T1, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBFTraceTOneP` | n/a | AUROC f_trace T1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprOne` | 12.6 | TPR at 1% FPR (%), f_trace T1, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprOneLo` | 5.2 | TPR at 1% FPR (%), f_trace T1, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprOneHi` | 24.7 | TPR at 1% FPR (%), f_trace T1, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprOneCI` | [5.2, 24.7] | TPR at 1% FPR (%), f_trace T1, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprOneN` | 586 | TPR at 1% FPR (%), f_trace T1, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprOneP` | n/a | TPR at 1% FPR (%), f_trace T1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprFive` | 23.2 | TPR at 5% FPR (%), f_trace T1, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprFiveLo` | 19.7 | TPR at 5% FPR (%), f_trace T1, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprFiveHi` | 31.3 | TPR at 5% FPR (%), f_trace T1, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprFiveCI` | [19.7, 31.3] | TPR at 5% FPR (%), f_trace T1, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprFiveN` | 586 | TPR at 5% FPR (%), f_trace T1, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBFTraceTOneTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTTwo` | 0.66 | AUROC f_trace T2, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoLo` | 0.64 | AUROC f_trace T2, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoHi` | 0.68 | AUROC f_trace T2, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoCI` | [0.64, 0.68] | AUROC f_trace T2, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoN` | 586 | AUROC f_trace T2, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoP` | n/a | AUROC f_trace T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprOne` | 16.7 | TPR at 1% FPR (%), f_trace T2, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprOneLo` | 5.5 | TPR at 1% FPR (%), f_trace T2, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprOneHi` | 25.2 | TPR at 1% FPR (%), f_trace T2, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprOneCI` | [5.5, 25.2] | TPR at 1% FPR (%), f_trace T2, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprOneN` | 586 | TPR at 1% FPR (%), f_trace T2, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprOneP` | n/a | TPR at 1% FPR (%), f_trace T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprFive` | 27.0 | TPR at 5% FPR (%), f_trace T2, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprFiveLo` | 19.1 | TPR at 5% FPR (%), f_trace T2, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprFiveHi` | 31.5 | TPR at 5% FPR (%), f_trace T2, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprFiveCI` | [19.1, 31.5] | TPR at 5% FPR (%), f_trace T2, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprFiveN` | 586 | TPR at 5% FPR (%), f_trace T2, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBFTraceTTwoTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTThree` | 0.66 | AUROC f_trace T3, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeLo` | 0.64 | AUROC f_trace T3, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeHi` | 0.68 | AUROC f_trace T3, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeCI` | [0.64, 0.68] | AUROC f_trace T3, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeN` | 596 | AUROC f_trace T3, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeP` | n/a | AUROC f_trace T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprOne` | 13.4 | TPR at 1% FPR (%), f_trace T3, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprOneLo` | 6.4 | TPR at 1% FPR (%), f_trace T3, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprOneHi` | 24.0 | TPR at 1% FPR (%), f_trace T3, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprOneCI` | [6.4, 24.0] | TPR at 1% FPR (%), f_trace T3, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprOneN` | 596 | TPR at 1% FPR (%), f_trace T3, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprOneP` | n/a | TPR at 1% FPR (%), f_trace T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprFive` | 22.1 | TPR at 5% FPR (%), f_trace T3, qwen3.8-27b |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprFiveLo` | 18.5 | TPR at 5% FPR (%), f_trace T3, qwen3.8-27b, lower 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprFiveHi` | 30.4 | TPR at 5% FPR (%), f_trace T3, qwen3.8-27b, upper 95% CI bound |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprFiveCI` | [18.5, 30.4] | TPR at 5% FPR (%), f_trace T3, qwen3.8-27b, 95% CI |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprFiveN` | 596 | TPR at 5% FPR (%), f_trace T3, qwen3.8-27b, n |
| `\DetQwenThreeEightTwoSevenBFTraceTThreeTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTZero` | 0.74 | AUROC V T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTZeroLo` | 0.70 | AUROC V T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTZeroHi` | 0.77 | AUROC V T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTZeroCI` | [0.70, 0.77] | AUROC V T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTZeroN` | 555 | AUROC V T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTZeroP` | n/a | AUROC V T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTZeroTprOne` | 47.5 | TPR at 1% FPR (%), V T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTZeroTprOneLo` | 40.3 | TPR at 1% FPR (%), V T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTZeroTprOneHi` | 53.8 | TPR at 1% FPR (%), V T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTZeroTprOneCI` | [40.3, 53.8] | TPR at 1% FPR (%), V T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTZeroTprOneN` | 555 | TPR at 1% FPR (%), V T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTZeroTprOneP` | n/a | TPR at 1% FPR (%), V T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTZeroTprFive` | 47.5 | TPR at 5% FPR (%), V T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTZeroTprFiveLo` | 41.0 | TPR at 5% FPR (%), V T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTZeroTprFiveHi` | 54.2 | TPR at 5% FPR (%), V T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTZeroTprFiveCI` | [41.0, 54.2] | TPR at 5% FPR (%), V T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTZeroTprFiveN` | 555 | TPR at 5% FPR (%), V T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTZeroTprFiveP` | n/a | TPR at 5% FPR (%), V T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTOne` | 0.55 | AUROC V T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTOneLo` | 0.53 | AUROC V T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTOneHi` | 0.56 | AUROC V T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTOneCI` | [0.53, 0.56] | AUROC V T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTOneN` | 550 | AUROC V T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTOneP` | n/a | AUROC V T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTOneTprOne` | 9.8 | TPR at 1% FPR (%), V T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTOneTprOneLo` | 6.4 | TPR at 1% FPR (%), V T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTOneTprOneHi` | 13.0 | TPR at 1% FPR (%), V T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTOneTprOneCI` | [6.4, 13.0] | TPR at 1% FPR (%), V T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTOneTprOneN` | 550 | TPR at 1% FPR (%), V T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTOneTprOneP` | n/a | TPR at 1% FPR (%), V T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTOneTprFive` | 9.8 | TPR at 5% FPR (%), V T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTOneTprFiveLo` | 6.4 | TPR at 5% FPR (%), V T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTOneTprFiveHi` | 13.4 | TPR at 5% FPR (%), V T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTOneTprFiveCI` | [6.4, 13.4] | TPR at 5% FPR (%), V T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTOneTprFiveN` | 550 | TPR at 5% FPR (%), V T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTOneTprFiveP` | n/a | TPR at 5% FPR (%), V T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTTwo` | 0.56 | AUROC V T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTTwoLo` | 0.55 | AUROC V T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTTwoHi` | 0.58 | AUROC V T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTTwoCI` | [0.55, 0.58] | AUROC V T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTTwoN` | 533 | AUROC V T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTTwoP` | n/a | AUROC V T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTTwoTprOne` | 13.0 | TPR at 1% FPR (%), V T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTTwoTprOneLo` | 9.6 | TPR at 1% FPR (%), V T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTTwoTprOneHi` | 16.1 | TPR at 1% FPR (%), V T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTTwoTprOneCI` | [9.6, 16.1] | TPR at 1% FPR (%), V T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTTwoTprOneN` | 533 | TPR at 1% FPR (%), V T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTTwoTprOneP` | n/a | TPR at 1% FPR (%), V T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTTwoTprFive` | 13.0 | TPR at 5% FPR (%), V T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTTwoTprFiveLo` | 9.6 | TPR at 5% FPR (%), V T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTTwoTprFiveHi` | 16.4 | TPR at 5% FPR (%), V T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTTwoTprFiveCI` | [9.6, 16.4] | TPR at 5% FPR (%), V T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTTwoTprFiveN` | 533 | TPR at 5% FPR (%), V T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTTwoTprFiveP` | n/a | TPR at 5% FPR (%), V T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTThree` | 0.55 | AUROC V T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTThreeLo` | 0.54 | AUROC V T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTThreeHi` | 0.57 | AUROC V T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTThreeCI` | [0.54, 0.57] | AUROC V T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTThreeN` | 547 | AUROC V T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTThreeP` | n/a | AUROC V T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTThreeTprOne` | 11.3 | TPR at 1% FPR (%), V T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTThreeTprOneLo` | 8.0 | TPR at 1% FPR (%), V T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTThreeTprOneHi` | 14.6 | TPR at 1% FPR (%), V T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTThreeTprOneCI` | [8.0, 14.6] | TPR at 1% FPR (%), V T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTThreeTprOneN` | 547 | TPR at 1% FPR (%), V T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTThreeTprOneP` | n/a | TPR at 1% FPR (%), V T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBVTThreeTprFive` | 11.3 | TPR at 5% FPR (%), V T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBVTThreeTprFiveLo` | 8.2 | TPR at 5% FPR (%), V T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBVTThreeTprFiveHi` | 14.6 | TPR at 5% FPR (%), V T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBVTThreeTprFiveCI` | [8.2, 14.6] | TPR at 5% FPR (%), V T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBVTThreeTprFiveN` | 547 | TPR at 5% FPR (%), V T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBVTThreeTprFiveP` | n/a | TPR at 5% FPR (%), V T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTZero` | 1.00 | AUROC C T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTZeroLo` | 0.99 | AUROC C T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTZeroHi` | 1.00 | AUROC C T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTZeroCI` | [0.99, 1.00] | AUROC C T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTZeroN` | 558 | AUROC C T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTZeroP` | n/a | AUROC C T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTZeroTprOne` | 99.3 | TPR at 1% FPR (%), C T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTZeroTprOneLo` | 96.2 | TPR at 1% FPR (%), C T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTZeroTprOneHi` | 100.0 | TPR at 1% FPR (%), C T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTZeroTprOneCI` | [96.2, 100.0] | TPR at 1% FPR (%), C T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTZeroTprOneN` | 558 | TPR at 1% FPR (%), C T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTZeroTprOneP` | n/a | TPR at 1% FPR (%), C T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTZeroTprFive` | 99.3 | TPR at 5% FPR (%), C T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTZeroTprFiveLo` | 98.2 | TPR at 5% FPR (%), C T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTZeroTprFiveHi` | 100.0 | TPR at 5% FPR (%), C T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTZeroTprFiveCI` | [98.2, 100.0] | TPR at 5% FPR (%), C T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTZeroTprFiveN` | 558 | TPR at 5% FPR (%), C T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTZeroTprFiveP` | n/a | TPR at 5% FPR (%), C T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTOne` | 0.99 | AUROC C T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTOneLo` | 0.99 | AUROC C T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTOneHi` | 1.00 | AUROC C T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTOneCI` | [0.99, 1.00] | AUROC C T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTOneN` | 556 | AUROC C T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTOneP` | n/a | AUROC C T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTOneTprOne` | 98.9 | TPR at 1% FPR (%), C T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTOneTprOneLo` | 94.8 | TPR at 1% FPR (%), C T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTOneTprOneHi` | 100.0 | TPR at 1% FPR (%), C T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTOneTprOneCI` | [94.8, 100.0] | TPR at 1% FPR (%), C T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTOneTprOneN` | 556 | TPR at 1% FPR (%), C T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTOneTprOneP` | n/a | TPR at 1% FPR (%), C T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTOneTprFive` | 98.9 | TPR at 5% FPR (%), C T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTOneTprFiveLo` | 97.5 | TPR at 5% FPR (%), C T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTOneTprFiveHi` | 100.0 | TPR at 5% FPR (%), C T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTOneTprFiveCI` | [97.5, 100.0] | TPR at 5% FPR (%), C T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTOneTprFiveN` | 556 | TPR at 5% FPR (%), C T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTOneTprFiveP` | n/a | TPR at 5% FPR (%), C T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTTwo` | 0.99 | AUROC C T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTTwoLo` | 0.99 | AUROC C T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTTwoHi` | 1.00 | AUROC C T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTTwoCI` | [0.99, 1.00] | AUROC C T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTTwoN` | 538 | AUROC C T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTTwoP` | n/a | AUROC C T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTTwoTprOne` | 98.9 | TPR at 1% FPR (%), C T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTTwoTprOneLo` | 95.9 | TPR at 1% FPR (%), C T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTTwoTprOneHi` | 100.0 | TPR at 1% FPR (%), C T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTTwoTprOneCI` | [95.9, 100.0] | TPR at 1% FPR (%), C T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTTwoTprOneN` | 538 | TPR at 1% FPR (%), C T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTTwoTprOneP` | n/a | TPR at 1% FPR (%), C T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTTwoTprFive` | 98.9 | TPR at 5% FPR (%), C T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTTwoTprFiveLo` | 97.5 | TPR at 5% FPR (%), C T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTTwoTprFiveHi` | 100.0 | TPR at 5% FPR (%), C T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTTwoTprFiveCI` | [97.5, 100.0] | TPR at 5% FPR (%), C T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTTwoTprFiveN` | 538 | TPR at 5% FPR (%), C T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTTwoTprFiveP` | n/a | TPR at 5% FPR (%), C T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTThree` | 1.00 | AUROC C T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTThreeLo` | 0.99 | AUROC C T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTThreeHi` | 1.00 | AUROC C T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTThreeCI` | [0.99, 1.00] | AUROC C T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTThreeN` | 553 | AUROC C T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTThreeP` | n/a | AUROC C T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTThreeTprOne` | 99.3 | TPR at 1% FPR (%), C T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTThreeTprOneLo` | 95.5 | TPR at 1% FPR (%), C T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTThreeTprOneHi` | 100.0 | TPR at 1% FPR (%), C T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTThreeTprOneCI` | [95.5, 100.0] | TPR at 1% FPR (%), C T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTThreeTprOneN` | 553 | TPR at 1% FPR (%), C T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTThreeTprOneP` | n/a | TPR at 1% FPR (%), C T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBCTThreeTprFive` | 99.3 | TPR at 5% FPR (%), C T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBCTThreeTprFiveLo` | 98.2 | TPR at 5% FPR (%), C T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBCTThreeTprFiveHi` | 100.0 | TPR at 5% FPR (%), C T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBCTThreeTprFiveCI` | [98.2, 100.0] | TPR at 5% FPR (%), C T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBCTThreeTprFiveN` | 553 | TPR at 5% FPR (%), C T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBCTThreeTprFiveP` | n/a | TPR at 5% FPR (%), C T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTZero` | 0.98 | AUROC R T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTZeroLo` | 0.97 | AUROC R T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTZeroHi` | 0.99 | AUROC R T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTZeroCI` | [0.97, 0.99] | AUROC R T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTZeroN` | 592 | AUROC R T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTZeroP` | n/a | AUROC R T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTZeroTprOne` | 0.0 | TPR at 1% FPR (%), R T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTZeroTprOneLo` | 0.0 | TPR at 1% FPR (%), R T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTZeroTprOneHi` | 90.6 | TPR at 1% FPR (%), R T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTZeroTprOneCI` | [0.0, 90.6] | TPR at 1% FPR (%), R T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTZeroTprOneN` | 592 | TPR at 1% FPR (%), R T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTZeroTprOneP` | n/a | TPR at 1% FPR (%), R T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTZeroTprFive` | 89.9 | TPR at 5% FPR (%), R T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTZeroTprFiveLo` | 83.4 | TPR at 5% FPR (%), R T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTZeroTprFiveHi` | 99.3 | TPR at 5% FPR (%), R T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTZeroTprFiveCI` | [83.4, 99.3] | TPR at 5% FPR (%), R T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTZeroTprFiveN` | 592 | TPR at 5% FPR (%), R T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTZeroTprFiveP` | n/a | TPR at 5% FPR (%), R T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTOne` | 0.98 | AUROC R T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTOneLo` | 0.97 | AUROC R T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTOneHi` | 1.00 | AUROC R T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTOneCI` | [0.97, 1.00] | AUROC R T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTOneN` | 590 | AUROC R T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTOneP` | n/a | AUROC R T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTOneTprOne` | 0.0 | TPR at 1% FPR (%), R T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTOneTprOneLo` | 0.0 | TPR at 1% FPR (%), R T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTOneTprOneHi` | 90.2 | TPR at 1% FPR (%), R T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTOneTprOneCI` | [0.0, 90.2] | TPR at 1% FPR (%), R T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTOneTprOneN` | 590 | TPR at 1% FPR (%), R T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTOneTprOneP` | n/a | TPR at 1% FPR (%), R T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTOneTprFive` | 89.2 | TPR at 5% FPR (%), R T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTOneTprFiveLo` | 83.0 | TPR at 5% FPR (%), R T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTOneTprFiveHi` | 99.3 | TPR at 5% FPR (%), R T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTOneTprFiveCI` | [83.0, 99.3] | TPR at 5% FPR (%), R T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTOneTprFiveN` | 590 | TPR at 5% FPR (%), R T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTOneTprFiveP` | n/a | TPR at 5% FPR (%), R T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTTwo` | 0.98 | AUROC R T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTTwoLo` | 0.96 | AUROC R T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTTwoHi` | 0.99 | AUROC R T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTTwoCI` | [0.96, 0.99] | AUROC R T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTTwoN` | 570 | AUROC R T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTTwoP` | n/a | AUROC R T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTTwoTprOne` | 0.0 | TPR at 1% FPR (%), R T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTTwoTprOneLo` | 0.0 | TPR at 1% FPR (%), R T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTTwoTprOneHi` | 88.9 | TPR at 1% FPR (%), R T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTTwoTprOneCI` | [0.0, 88.9] | TPR at 1% FPR (%), R T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTTwoTprOneN` | 570 | TPR at 1% FPR (%), R T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTTwoTprOneP` | n/a | TPR at 1% FPR (%), R T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTTwoTprFive` | 87.0 | TPR at 5% FPR (%), R T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTTwoTprFiveLo` | 76.2 | TPR at 5% FPR (%), R T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTTwoTprFiveHi` | 98.3 | TPR at 5% FPR (%), R T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTTwoTprFiveCI` | [76.2, 98.3] | TPR at 5% FPR (%), R T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTTwoTprFiveN` | 570 | TPR at 5% FPR (%), R T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTTwoTprFiveP` | n/a | TPR at 5% FPR (%), R T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTThree` | 0.98 | AUROC R T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTThreeLo` | 0.97 | AUROC R T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTThreeHi` | 0.99 | AUROC R T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTThreeCI` | [0.97, 0.99] | AUROC R T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTThreeN` | 586 | AUROC R T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTThreeP` | n/a | AUROC R T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTThreeTprOne` | 0.0 | TPR at 1% FPR (%), R T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTThreeTprOneLo` | 0.0 | TPR at 1% FPR (%), R T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTThreeTprOneHi` | 90.7 | TPR at 1% FPR (%), R T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTThreeTprOneCI` | [0.0, 90.7] | TPR at 1% FPR (%), R T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTThreeTprOneN` | 586 | TPR at 1% FPR (%), R T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTThreeTprOneP` | n/a | TPR at 1% FPR (%), R T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRTThreeTprFive` | 89.1 | TPR at 5% FPR (%), R T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRTThreeTprFiveLo` | 82.4 | TPR at 5% FPR (%), R T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRTThreeTprFiveHi` | 99.3 | TPR at 5% FPR (%), R T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRTThreeTprFiveCI` | [82.4, 99.3] | TPR at 5% FPR (%), R T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRTThreeTprFiveN` | 586 | TPR at 5% FPR (%), R T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRTThreeTprFiveP` | n/a | TPR at 5% FPR (%), R T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTZero` | 0.65 | AUROC r_field T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTZeroLo` | 0.62 | AUROC r_field T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTZeroHi` | 0.67 | AUROC r_field T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTZeroCI` | [0.62, 0.67] | AUROC r_field T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTZeroN` | 592 | AUROC r_field T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTZeroP` | n/a | AUROC r_field T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTZeroTprOne` | 0.7 | TPR at 1% FPR (%), r_field T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTZeroTprOneLo` | 0.0 | TPR at 1% FPR (%), r_field T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTZeroTprOneHi` | 6.5 | TPR at 1% FPR (%), r_field T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTZeroTprOneCI` | [0.0, 6.5] | TPR at 1% FPR (%), r_field T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTZeroTprOneN` | 592 | TPR at 1% FPR (%), r_field T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTZeroTprOneP` | n/a | TPR at 1% FPR (%), r_field T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTZeroTprFive` | 10.8 | TPR at 5% FPR (%), r_field T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTZeroTprFiveLo` | 5.4 | TPR at 5% FPR (%), r_field T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTZeroTprFiveHi` | 15.9 | TPR at 5% FPR (%), r_field T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTZeroTprFiveCI` | [5.4, 15.9] | TPR at 5% FPR (%), r_field T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTZeroTprFiveN` | 592 | TPR at 5% FPR (%), r_field T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTZeroTprFiveP` | n/a | TPR at 5% FPR (%), r_field T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTOne` | 0.65 | AUROC r_field T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTOneLo` | 0.63 | AUROC r_field T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTOneHi` | 0.68 | AUROC r_field T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTOneCI` | [0.63, 0.68] | AUROC r_field T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTOneN` | 590 | AUROC r_field T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTOneP` | n/a | AUROC r_field T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTOneTprOne` | 2.4 | TPR at 1% FPR (%), r_field T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTOneTprOneLo` | 1.3 | TPR at 1% FPR (%), r_field T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTOneTprOneHi` | 10.3 | TPR at 1% FPR (%), r_field T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTOneTprOneCI` | [1.3, 10.3] | TPR at 1% FPR (%), r_field T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTOneTprOneN` | 590 | TPR at 1% FPR (%), r_field T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTOneTprOneP` | n/a | TPR at 1% FPR (%), r_field T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTOneTprFive` | 14.9 | TPR at 5% FPR (%), r_field T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTOneTprFiveLo` | 8.4 | TPR at 5% FPR (%), r_field T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTOneTprFiveHi` | 19.2 | TPR at 5% FPR (%), r_field T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTOneTprFiveCI` | [8.4, 19.2] | TPR at 5% FPR (%), r_field T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTOneTprFiveN` | 590 | TPR at 5% FPR (%), r_field T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTOneTprFiveP` | n/a | TPR at 5% FPR (%), r_field T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTTwo` | 0.65 | AUROC r_field T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTTwoLo` | 0.63 | AUROC r_field T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTTwoHi` | 0.68 | AUROC r_field T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTTwoCI` | [0.63, 0.68] | AUROC r_field T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTTwoN` | 570 | AUROC r_field T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTTwoP` | n/a | AUROC r_field T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTTwoTprOne` | 2.8 | TPR at 1% FPR (%), r_field T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTTwoTprOneLo` | 0.7 | TPR at 1% FPR (%), r_field T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTTwoTprOneHi` | 10.1 | TPR at 1% FPR (%), r_field T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTTwoTprOneCI` | [0.7, 10.1] | TPR at 1% FPR (%), r_field T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTTwoTprOneN` | 570 | TPR at 1% FPR (%), r_field T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTTwoTprOneP` | n/a | TPR at 1% FPR (%), r_field T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTTwoTprFive` | 14.7 | TPR at 5% FPR (%), r_field T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTTwoTprFiveLo` | 8.5 | TPR at 5% FPR (%), r_field T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTTwoTprFiveHi` | 20.2 | TPR at 5% FPR (%), r_field T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTTwoTprFiveCI` | [8.5, 20.2] | TPR at 5% FPR (%), r_field T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTTwoTprFiveN` | 570 | TPR at 5% FPR (%), r_field T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTTwoTprFiveP` | n/a | TPR at 5% FPR (%), r_field T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTThree` | 0.65 | AUROC r_field T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTThreeLo` | 0.63 | AUROC r_field T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTThreeHi` | 0.68 | AUROC r_field T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTThreeCI` | [0.63, 0.68] | AUROC r_field T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTThreeN` | 586 | AUROC r_field T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTThreeP` | n/a | AUROC r_field T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTThreeTprOne` | 2.7 | TPR at 1% FPR (%), r_field T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTThreeTprOneLo` | 0.7 | TPR at 1% FPR (%), r_field T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTThreeTprOneHi` | 10.5 | TPR at 1% FPR (%), r_field T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTThreeTprOneCI` | [0.7, 10.5] | TPR at 1% FPR (%), r_field T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTThreeTprOneN` | 586 | TPR at 1% FPR (%), r_field T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTThreeTprOneP` | n/a | TPR at 1% FPR (%), r_field T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBRFieldTThreeTprFive` | 14.7 | TPR at 5% FPR (%), r_field T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBRFieldTThreeTprFiveLo` | 8.9 | TPR at 5% FPR (%), r_field T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTThreeTprFiveHi` | 19.9 | TPR at 5% FPR (%), r_field T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBRFieldTThreeTprFiveCI` | [8.9, 19.9] | TPR at 5% FPR (%), r_field T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBRFieldTThreeTprFiveN` | 586 | TPR at 5% FPR (%), r_field T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBRFieldTThreeTprFiveP` | n/a | TPR at 5% FPR (%), r_field T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTZero` | 0.67 | AUROC f_trace T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTZeroLo` | 0.65 | AUROC f_trace T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTZeroHi` | 0.69 | AUROC f_trace T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTZeroCI` | [0.65, 0.69] | AUROC f_trace T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTZeroN` | 596 | AUROC f_trace T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTZeroP` | n/a | AUROC f_trace T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTZeroTprOne` | 13.1 | TPR at 1% FPR (%), f_trace T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTZeroTprOneLo` | 4.0 | TPR at 1% FPR (%), f_trace T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTZeroTprOneHi` | 17.0 | TPR at 1% FPR (%), f_trace T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTZeroTprOneCI` | [4.0, 17.0] | TPR at 1% FPR (%), f_trace T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTZeroTprOneN` | 596 | TPR at 1% FPR (%), f_trace T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTZeroTprOneP` | n/a | TPR at 1% FPR (%), f_trace T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTZeroTprFive` | 23.2 | TPR at 5% FPR (%), f_trace T0, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTZeroTprFiveLo` | 12.4 | TPR at 5% FPR (%), f_trace T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTZeroTprFiveHi` | 31.5 | TPR at 5% FPR (%), f_trace T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTZeroTprFiveCI` | [12.4, 31.5] | TPR at 5% FPR (%), f_trace T0, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTZeroTprFiveN` | 596 | TPR at 5% FPR (%), f_trace T0, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTZeroTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTOne` | 0.68 | AUROC f_trace T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTOneLo` | 0.66 | AUROC f_trace T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTOneHi` | 0.69 | AUROC f_trace T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTOneCI` | [0.66, 0.69] | AUROC f_trace T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTOneN` | 594 | AUROC f_trace T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTOneP` | n/a | AUROC f_trace T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTOneTprOne` | 15.8 | TPR at 1% FPR (%), f_trace T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTOneTprOneLo` | 7.4 | TPR at 1% FPR (%), f_trace T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTOneTprOneHi` | 19.6 | TPR at 1% FPR (%), f_trace T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTOneTprOneCI` | [7.4, 19.6] | TPR at 1% FPR (%), f_trace T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTOneTprOneN` | 594 | TPR at 1% FPR (%), f_trace T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTOneTprOneP` | n/a | TPR at 1% FPR (%), f_trace T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTOneTprFive` | 27.6 | TPR at 5% FPR (%), f_trace T1, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTOneTprFiveLo` | 16.4 | TPR at 5% FPR (%), f_trace T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTOneTprFiveHi` | 34.0 | TPR at 5% FPR (%), f_trace T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTOneTprFiveCI` | [16.4, 34.0] | TPR at 5% FPR (%), f_trace T1, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTOneTprFiveN` | 594 | TPR at 5% FPR (%), f_trace T1, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTOneTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTTwo` | 0.67 | AUROC f_trace T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTTwoLo` | 0.65 | AUROC f_trace T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTTwoHi` | 0.69 | AUROC f_trace T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTTwoCI` | [0.65, 0.69] | AUROC f_trace T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTTwoN` | 574 | AUROC f_trace T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTTwoP` | n/a | AUROC f_trace T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTTwoTprOne` | 14.6 | TPR at 1% FPR (%), f_trace T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTTwoTprOneLo` | 6.4 | TPR at 1% FPR (%), f_trace T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTTwoTprOneHi` | 18.8 | TPR at 1% FPR (%), f_trace T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTTwoTprOneCI` | [6.4, 18.8] | TPR at 1% FPR (%), f_trace T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTTwoTprOneN` | 574 | TPR at 1% FPR (%), f_trace T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTTwoTprOneP` | n/a | TPR at 1% FPR (%), f_trace T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTTwoTprFive` | 26.1 | TPR at 5% FPR (%), f_trace T2, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTTwoTprFiveLo` | 14.4 | TPR at 5% FPR (%), f_trace T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTTwoTprFiveHi` | 33.9 | TPR at 5% FPR (%), f_trace T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTTwoTprFiveCI` | [14.4, 33.9] | TPR at 5% FPR (%), f_trace T2, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTTwoTprFiveN` | 574 | TPR at 5% FPR (%), f_trace T2, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTTwoTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTThree` | 0.66 | AUROC f_trace T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTThreeLo` | 0.65 | AUROC f_trace T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTThreeHi` | 0.68 | AUROC f_trace T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTThreeCI` | [0.65, 0.68] | AUROC f_trace T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTThreeN` | 590 | AUROC f_trace T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTThreeP` | n/a | AUROC f_trace T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTThreeTprOne` | 14.6 | TPR at 1% FPR (%), f_trace T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTThreeTprOneLo` | 6.4 | TPR at 1% FPR (%), f_trace T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTThreeTprOneHi` | 18.1 | TPR at 1% FPR (%), f_trace T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTThreeTprOneCI` | [6.4, 18.1] | TPR at 1% FPR (%), f_trace T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTThreeTprOneN` | 590 | TPR at 1% FPR (%), f_trace T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTThreeTprOneP` | n/a | TPR at 1% FPR (%), f_trace T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGemmaFourThreeOneBFTraceTThreeTprFive` | 26.1 | TPR at 5% FPR (%), f_trace T3, gemma-4-31b-it |
| `\DetGemmaFourThreeOneBFTraceTThreeTprFiveLo` | 14.9 | TPR at 5% FPR (%), f_trace T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTThreeTprFiveHi` | 33.2 | TPR at 5% FPR (%), f_trace T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetGemmaFourThreeOneBFTraceTThreeTprFiveCI` | [14.9, 33.2] | TPR at 5% FPR (%), f_trace T3, gemma-4-31b-it, 95% CI |
| `\DetGemmaFourThreeOneBFTraceTThreeTprFiveN` | 590 | TPR at 5% FPR (%), f_trace T3, gemma-4-31b-it, n |
| `\DetGemmaFourThreeOneBFTraceTThreeTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTZero` | 0.89 | AUROC V T0, glm-5.3-flash |
| `\DetGLMFiveThreeFlashVTZeroLo` | 0.87 | AUROC V T0, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTZeroHi` | 0.90 | AUROC V T0, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTZeroCI` | [0.87, 0.90] | AUROC V T0, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashVTZeroN` | 600 | AUROC V T0, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashVTZeroP` | n/a | AUROC V T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTZeroTprOne` | 76.7 | TPR at 1% FPR (%), V T0, glm-5.3-flash |
| `\DetGLMFiveThreeFlashVTZeroTprOneLo` | 70.0 | TPR at 1% FPR (%), V T0, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTZeroTprOneHi` | 80.0 | TPR at 1% FPR (%), V T0, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTZeroTprOneCI` | [70.0, 80.0] | TPR at 1% FPR (%), V T0, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashVTZeroTprOneN` | 600 | TPR at 1% FPR (%), V T0, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashVTZeroTprOneP` | n/a | TPR at 1% FPR (%), V T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTZeroTprFive` | 79.7 | TPR at 5% FPR (%), V T0, glm-5.3-flash |
| `\DetGLMFiveThreeFlashVTZeroTprFiveLo` | 77.3 | TPR at 5% FPR (%), V T0, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTZeroTprFiveHi` | 81.7 | TPR at 5% FPR (%), V T0, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTZeroTprFiveCI` | [77.3, 81.7] | TPR at 5% FPR (%), V T0, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashVTZeroTprFiveN` | 600 | TPR at 5% FPR (%), V T0, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashVTZeroTprFiveP` | n/a | TPR at 5% FPR (%), V T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTOne` | 0.71 | AUROC V T1, glm-5.3-flash |
| `\DetGLMFiveThreeFlashVTOneLo` | 0.68 | AUROC V T1, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTOneHi` | 0.75 | AUROC V T1, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTOneCI` | [0.68, 0.75] | AUROC V T1, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashVTOneN` | 592 | AUROC V T1, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashVTOneP` | n/a | AUROC V T1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTOneTprOne` | 32.1 | TPR at 1% FPR (%), V T1, glm-5.3-flash |
| `\DetGLMFiveThreeFlashVTOneTprOneLo` | 21.5 | TPR at 1% FPR (%), V T1, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTOneTprOneHi` | 39.7 | TPR at 1% FPR (%), V T1, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTOneTprOneCI` | [21.5, 39.7] | TPR at 1% FPR (%), V T1, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashVTOneTprOneN` | 592 | TPR at 1% FPR (%), V T1, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashVTOneTprOneP` | n/a | TPR at 1% FPR (%), V T1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTOneTprFive` | 43.2 | TPR at 5% FPR (%), V T1, glm-5.3-flash |
| `\DetGLMFiveThreeFlashVTOneTprFiveLo` | 36.1 | TPR at 5% FPR (%), V T1, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTOneTprFiveHi` | 50.0 | TPR at 5% FPR (%), V T1, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTOneTprFiveCI` | [36.1, 50.0] | TPR at 5% FPR (%), V T1, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashVTOneTprFiveN` | 592 | TPR at 5% FPR (%), V T1, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashVTOneTprFiveP` | n/a | TPR at 5% FPR (%), V T1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTTwo` | 0.73 | AUROC V T2, glm-5.3-flash |
| `\DetGLMFiveThreeFlashVTTwoLo` | 0.70 | AUROC V T2, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTTwoHi` | 0.76 | AUROC V T2, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTTwoCI` | [0.70, 0.76] | AUROC V T2, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashVTTwoN` | 598 | AUROC V T2, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashVTTwoP` | n/a | AUROC V T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTTwoTprOne` | 30.8 | TPR at 1% FPR (%), V T2, glm-5.3-flash |
| `\DetGLMFiveThreeFlashVTTwoTprOneLo` | 21.7 | TPR at 1% FPR (%), V T2, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTTwoTprOneHi` | 40.3 | TPR at 1% FPR (%), V T2, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTTwoTprOneCI` | [21.7, 40.3] | TPR at 1% FPR (%), V T2, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashVTTwoTprOneN` | 598 | TPR at 1% FPR (%), V T2, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashVTTwoTprOneP` | n/a | TPR at 1% FPR (%), V T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTTwoTprFive` | 42.8 | TPR at 5% FPR (%), V T2, glm-5.3-flash |
| `\DetGLMFiveThreeFlashVTTwoTprFiveLo` | 36.5 | TPR at 5% FPR (%), V T2, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTTwoTprFiveHi` | 49.5 | TPR at 5% FPR (%), V T2, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTTwoTprFiveCI` | [36.5, 49.5] | TPR at 5% FPR (%), V T2, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashVTTwoTprFiveN` | 598 | TPR at 5% FPR (%), V T2, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashVTTwoTprFiveP` | n/a | TPR at 5% FPR (%), V T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTThree` | 0.67 | AUROC V T3, glm-5.3-flash |
| `\DetGLMFiveThreeFlashVTThreeLo` | 0.63 | AUROC V T3, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTThreeHi` | 0.71 | AUROC V T3, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTThreeCI` | [0.63, 0.71] | AUROC V T3, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashVTThreeN` | 600 | AUROC V T3, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashVTThreeP` | n/a | AUROC V T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTThreeTprOne` | 27.3 | TPR at 1% FPR (%), V T3, glm-5.3-flash |
| `\DetGLMFiveThreeFlashVTThreeTprOneLo` | 20.3 | TPR at 1% FPR (%), V T3, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTThreeTprOneHi` | 34.3 | TPR at 1% FPR (%), V T3, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTThreeTprOneCI` | [20.3, 34.3] | TPR at 1% FPR (%), V T3, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashVTThreeTprOneN` | 600 | TPR at 1% FPR (%), V T3, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashVTThreeTprOneP` | n/a | TPR at 1% FPR (%), V T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashVTThreeTprFive` | 36.7 | TPR at 5% FPR (%), V T3, glm-5.3-flash |
| `\DetGLMFiveThreeFlashVTThreeTprFiveLo` | 31.3 | TPR at 5% FPR (%), V T3, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashVTThreeTprFiveHi` | 43.0 | TPR at 5% FPR (%), V T3, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashVTThreeTprFiveCI` | [31.3, 43.0] | TPR at 5% FPR (%), V T3, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashVTThreeTprFiveN` | 600 | TPR at 5% FPR (%), V T3, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashVTThreeTprFiveP` | n/a | TPR at 5% FPR (%), V T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTZero` | 1.00 | AUROC C T0, glm-5.3-flash |
| `\DetGLMFiveThreeFlashCTZeroLo` | 0.99 | AUROC C T0, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTZeroHi` | 1.00 | AUROC C T0, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTZeroCI` | [0.99, 1.00] | AUROC C T0, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashCTZeroN` | 600 | AUROC C T0, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashCTZeroP` | n/a | AUROC C T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTZeroTprOne` | 99.7 | TPR at 1% FPR (%), C T0, glm-5.3-flash |
| `\DetGLMFiveThreeFlashCTZeroTprOneLo` | 80.0 | TPR at 1% FPR (%), C T0, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTZeroTprOneHi` | 100.0 | TPR at 1% FPR (%), C T0, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTZeroTprOneCI` | [80.0, 100.0] | TPR at 1% FPR (%), C T0, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashCTZeroTprOneN` | 600 | TPR at 1% FPR (%), C T0, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashCTZeroTprOneP` | n/a | TPR at 1% FPR (%), C T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTZeroTprFive` | 100.0 | TPR at 5% FPR (%), C T0, glm-5.3-flash |
| `\DetGLMFiveThreeFlashCTZeroTprFiveLo` | 100.0 | TPR at 5% FPR (%), C T0, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTZeroTprFiveHi` | 100.0 | TPR at 5% FPR (%), C T0, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTZeroTprFiveCI` | [100.0, 100.0] | TPR at 5% FPR (%), C T0, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashCTZeroTprFiveN` | 600 | TPR at 5% FPR (%), C T0, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashCTZeroTprFiveP` | n/a | TPR at 5% FPR (%), C T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTOne` | 1.00 | AUROC C T1, glm-5.3-flash |
| `\DetGLMFiveThreeFlashCTOneLo` | 0.99 | AUROC C T1, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTOneHi` | 1.00 | AUROC C T1, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTOneCI` | [0.99, 1.00] | AUROC C T1, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashCTOneN` | 592 | AUROC C T1, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashCTOneP` | n/a | AUROC C T1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTOneTprOne` | 98.3 | TPR at 1% FPR (%), C T1, glm-5.3-flash |
| `\DetGLMFiveThreeFlashCTOneTprOneLo` | 64.4 | TPR at 1% FPR (%), C T1, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTOneTprOneHi` | 100.0 | TPR at 1% FPR (%), C T1, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTOneTprOneCI` | [64.4, 100.0] | TPR at 1% FPR (%), C T1, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashCTOneTprOneN` | 592 | TPR at 1% FPR (%), C T1, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashCTOneTprOneP` | n/a | TPR at 1% FPR (%), C T1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTOneTprFive` | 99.7 | TPR at 5% FPR (%), C T1, glm-5.3-flash |
| `\DetGLMFiveThreeFlashCTOneTprFiveLo` | 99.0 | TPR at 5% FPR (%), C T1, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTOneTprFiveHi` | 100.0 | TPR at 5% FPR (%), C T1, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTOneTprFiveCI` | [99.0, 100.0] | TPR at 5% FPR (%), C T1, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashCTOneTprFiveN` | 592 | TPR at 5% FPR (%), C T1, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashCTOneTprFiveP` | n/a | TPR at 5% FPR (%), C T1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTTwo` | 1.00 | AUROC C T2, glm-5.3-flash |
| `\DetGLMFiveThreeFlashCTTwoLo` | 0.99 | AUROC C T2, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTTwoHi` | 1.00 | AUROC C T2, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTTwoCI` | [0.99, 1.00] | AUROC C T2, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashCTTwoN` | 598 | AUROC C T2, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashCTTwoP` | n/a | AUROC C T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTTwoTprOne` | 96.0 | TPR at 1% FPR (%), C T2, glm-5.3-flash |
| `\DetGLMFiveThreeFlashCTTwoTprOneLo` | 57.9 | TPR at 1% FPR (%), C T2, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTTwoTprOneHi` | 100.0 | TPR at 1% FPR (%), C T2, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTTwoTprOneCI` | [57.9, 100.0] | TPR at 1% FPR (%), C T2, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashCTTwoTprOneN` | 598 | TPR at 1% FPR (%), C T2, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashCTTwoTprOneP` | n/a | TPR at 1% FPR (%), C T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTTwoTprFive` | 99.7 | TPR at 5% FPR (%), C T2, glm-5.3-flash |
| `\DetGLMFiveThreeFlashCTTwoTprFiveLo` | 99.0 | TPR at 5% FPR (%), C T2, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTTwoTprFiveHi` | 100.0 | TPR at 5% FPR (%), C T2, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTTwoTprFiveCI` | [99.0, 100.0] | TPR at 5% FPR (%), C T2, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashCTTwoTprFiveN` | 598 | TPR at 5% FPR (%), C T2, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashCTTwoTprFiveP` | n/a | TPR at 5% FPR (%), C T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTThree` | 1.00 | AUROC C T3, glm-5.3-flash |
| `\DetGLMFiveThreeFlashCTThreeLo` | 1.00 | AUROC C T3, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTThreeHi` | 1.00 | AUROC C T3, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTThreeCI` | [1.00, 1.00] | AUROC C T3, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashCTThreeN` | 600 | AUROC C T3, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashCTThreeP` | n/a | AUROC C T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTThreeTprOne` | 100.0 | TPR at 1% FPR (%), C T3, glm-5.3-flash |
| `\DetGLMFiveThreeFlashCTThreeTprOneLo` | 83.0 | TPR at 1% FPR (%), C T3, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTThreeTprOneHi` | 100.0 | TPR at 1% FPR (%), C T3, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTThreeTprOneCI` | [83.0, 100.0] | TPR at 1% FPR (%), C T3, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashCTThreeTprOneN` | 600 | TPR at 1% FPR (%), C T3, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashCTThreeTprOneP` | n/a | TPR at 1% FPR (%), C T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashCTThreeTprFive` | 100.0 | TPR at 5% FPR (%), C T3, glm-5.3-flash |
| `\DetGLMFiveThreeFlashCTThreeTprFiveLo` | 100.0 | TPR at 5% FPR (%), C T3, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashCTThreeTprFiveHi` | 100.0 | TPR at 5% FPR (%), C T3, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashCTThreeTprFiveCI` | [100.0, 100.0] | TPR at 5% FPR (%), C T3, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashCTThreeTprFiveN` | 600 | TPR at 5% FPR (%), C T3, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashCTThreeTprFiveP` | n/a | TPR at 5% FPR (%), C T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTZero` | 1.00 | AUROC R T0, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRTZeroLo` | 0.99 | AUROC R T0, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTZeroHi` | 1.00 | AUROC R T0, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTZeroCI` | [0.99, 1.00] | AUROC R T0, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRTZeroN` | 600 | AUROC R T0, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRTZeroP` | n/a | AUROC R T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTZeroTprOne` | 97.3 | TPR at 1% FPR (%), R T0, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRTZeroTprOneLo` | 64.7 | TPR at 1% FPR (%), R T0, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTZeroTprOneHi` | 99.7 | TPR at 1% FPR (%), R T0, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTZeroTprOneCI` | [64.7, 99.7] | TPR at 1% FPR (%), R T0, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRTZeroTprOneN` | 600 | TPR at 1% FPR (%), R T0, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRTZeroTprOneP` | n/a | TPR at 1% FPR (%), R T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTZeroTprFive` | 98.3 | TPR at 5% FPR (%), R T0, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRTZeroTprFiveLo` | 96.7 | TPR at 5% FPR (%), R T0, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTZeroTprFiveHi` | 100.0 | TPR at 5% FPR (%), R T0, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTZeroTprFiveCI` | [96.7, 100.0] | TPR at 5% FPR (%), R T0, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRTZeroTprFiveN` | 600 | TPR at 5% FPR (%), R T0, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRTZeroTprFiveP` | n/a | TPR at 5% FPR (%), R T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTOne` | 1.00 | AUROC R T1, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRTOneLo` | 0.99 | AUROC R T1, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTOneHi` | 1.00 | AUROC R T1, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTOneCI` | [0.99, 1.00] | AUROC R T1, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRTOneN` | 592 | AUROC R T1, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRTOneP` | n/a | AUROC R T1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTOneTprOne` | 86.5 | TPR at 1% FPR (%), R T1, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRTOneTprOneLo` | 61.4 | TPR at 1% FPR (%), R T1, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTOneTprOneHi` | 98.6 | TPR at 1% FPR (%), R T1, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTOneTprOneCI` | [61.4, 98.6] | TPR at 1% FPR (%), R T1, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRTOneTprOneN` | 592 | TPR at 1% FPR (%), R T1, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRTOneTprOneP` | n/a | TPR at 1% FPR (%), R T1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTOneTprFive` | 97.6 | TPR at 5% FPR (%), R T1, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRTOneTprFiveLo` | 95.9 | TPR at 5% FPR (%), R T1, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTOneTprFiveHi` | 100.0 | TPR at 5% FPR (%), R T1, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTOneTprFiveCI` | [95.9, 100.0] | TPR at 5% FPR (%), R T1, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRTOneTprFiveN` | 592 | TPR at 5% FPR (%), R T1, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRTOneTprFiveP` | n/a | TPR at 5% FPR (%), R T1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTTwo` | 1.00 | AUROC R T2, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRTTwoLo` | 1.00 | AUROC R T2, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTTwoHi` | 1.00 | AUROC R T2, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTTwoCI` | [1.00, 1.00] | AUROC R T2, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRTTwoN` | 598 | AUROC R T2, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRTTwoP` | n/a | AUROC R T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTTwoTprOne` | 88.0 | TPR at 1% FPR (%), R T2, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRTTwoTprOneLo` | 67.6 | TPR at 1% FPR (%), R T2, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTTwoTprOneHi` | 99.3 | TPR at 1% FPR (%), R T2, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTTwoTprOneCI` | [67.6, 99.3] | TPR at 1% FPR (%), R T2, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRTTwoTprOneN` | 598 | TPR at 1% FPR (%), R T2, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRTTwoTprOneP` | n/a | TPR at 1% FPR (%), R T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTTwoTprFive` | 98.3 | TPR at 5% FPR (%), R T2, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRTTwoTprFiveLo` | 97.0 | TPR at 5% FPR (%), R T2, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTTwoTprFiveHi` | 100.0 | TPR at 5% FPR (%), R T2, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTTwoTprFiveCI` | [97.0, 100.0] | TPR at 5% FPR (%), R T2, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRTTwoTprFiveN` | 598 | TPR at 5% FPR (%), R T2, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRTTwoTprFiveP` | n/a | TPR at 5% FPR (%), R T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTThree` | 1.00 | AUROC R T3, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRTThreeLo` | 0.99 | AUROC R T3, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTThreeHi` | 1.00 | AUROC R T3, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTThreeCI` | [0.99, 1.00] | AUROC R T3, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRTThreeN` | 600 | AUROC R T3, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRTThreeP` | n/a | AUROC R T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTThreeTprOne` | 97.7 | TPR at 1% FPR (%), R T3, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRTThreeTprOneLo` | 71.3 | TPR at 1% FPR (%), R T3, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTThreeTprOneHi` | 99.3 | TPR at 1% FPR (%), R T3, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTThreeTprOneCI` | [71.3, 99.3] | TPR at 1% FPR (%), R T3, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRTThreeTprOneN` | 600 | TPR at 1% FPR (%), R T3, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRTThreeTprOneP` | n/a | TPR at 1% FPR (%), R T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRTThreeTprFive` | 98.0 | TPR at 5% FPR (%), R T3, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRTThreeTprFiveLo` | 96.3 | TPR at 5% FPR (%), R T3, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRTThreeTprFiveHi` | 100.0 | TPR at 5% FPR (%), R T3, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRTThreeTprFiveCI` | [96.3, 100.0] | TPR at 5% FPR (%), R T3, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRTThreeTprFiveN` | 600 | TPR at 5% FPR (%), R T3, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRTThreeTprFiveP` | n/a | TPR at 5% FPR (%), R T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTZero` | 0.64 | AUROC r_field T0, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRFieldTZeroLo` | 0.62 | AUROC r_field T0, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTZeroHi` | 0.66 | AUROC r_field T0, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTZeroCI` | [0.62, 0.66] | AUROC r_field T0, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTZeroN` | 600 | AUROC r_field T0, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRFieldTZeroP` | n/a | AUROC r_field T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTZeroTprOne` | 2.3 | TPR at 1% FPR (%), r_field T0, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRFieldTZeroTprOneLo` | 1.0 | TPR at 1% FPR (%), r_field T0, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTZeroTprOneHi` | 7.7 | TPR at 1% FPR (%), r_field T0, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTZeroTprOneCI` | [1.0, 7.7] | TPR at 1% FPR (%), r_field T0, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTZeroTprOneN` | 600 | TPR at 1% FPR (%), r_field T0, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRFieldTZeroTprOneP` | n/a | TPR at 1% FPR (%), r_field T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTZeroTprFive` | 11.7 | TPR at 5% FPR (%), r_field T0, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRFieldTZeroTprFiveLo` | 7.3 | TPR at 5% FPR (%), r_field T0, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTZeroTprFiveHi` | 18.0 | TPR at 5% FPR (%), r_field T0, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTZeroTprFiveCI` | [7.3, 18.0] | TPR at 5% FPR (%), r_field T0, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTZeroTprFiveN` | 600 | TPR at 5% FPR (%), r_field T0, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRFieldTZeroTprFiveP` | n/a | TPR at 5% FPR (%), r_field T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTOne` | 0.64 | AUROC r_field T1, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRFieldTOneLo` | 0.61 | AUROC r_field T1, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTOneHi` | 0.66 | AUROC r_field T1, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTOneCI` | [0.61, 0.66] | AUROC r_field T1, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTOneN` | 592 | AUROC r_field T1, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRFieldTOneP` | n/a | AUROC r_field T1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTOneTprOne` | 3.7 | TPR at 1% FPR (%), r_field T1, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRFieldTOneTprOneLo` | 1.7 | TPR at 1% FPR (%), r_field T1, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTOneTprOneHi` | 9.4 | TPR at 1% FPR (%), r_field T1, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTOneTprOneCI` | [1.7, 9.4] | TPR at 1% FPR (%), r_field T1, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTOneTprOneN` | 592 | TPR at 1% FPR (%), r_field T1, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRFieldTOneTprOneP` | n/a | TPR at 1% FPR (%), r_field T1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTOneTprFive` | 14.5 | TPR at 5% FPR (%), r_field T1, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRFieldTOneTprFiveLo` | 8.8 | TPR at 5% FPR (%), r_field T1, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTOneTprFiveHi` | 20.9 | TPR at 5% FPR (%), r_field T1, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTOneTprFiveCI` | [8.8, 20.9] | TPR at 5% FPR (%), r_field T1, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTOneTprFiveN` | 592 | TPR at 5% FPR (%), r_field T1, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRFieldTOneTprFiveP` | n/a | TPR at 5% FPR (%), r_field T1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTTwo` | 0.64 | AUROC r_field T2, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRFieldTTwoLo` | 0.62 | AUROC r_field T2, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTTwoHi` | 0.66 | AUROC r_field T2, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTTwoCI` | [0.62, 0.66] | AUROC r_field T2, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTTwoN` | 598 | AUROC r_field T2, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRFieldTTwoP` | n/a | AUROC r_field T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTTwoTprOne` | 3.3 | TPR at 1% FPR (%), r_field T2, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRFieldTTwoTprOneLo` | 1.0 | TPR at 1% FPR (%), r_field T2, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTTwoTprOneHi` | 10.7 | TPR at 1% FPR (%), r_field T2, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTTwoTprOneCI` | [1.0, 10.7] | TPR at 1% FPR (%), r_field T2, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTTwoTprOneN` | 598 | TPR at 1% FPR (%), r_field T2, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRFieldTTwoTprOneP` | n/a | TPR at 1% FPR (%), r_field T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTTwoTprFive` | 15.4 | TPR at 5% FPR (%), r_field T2, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRFieldTTwoTprFiveLo` | 9.4 | TPR at 5% FPR (%), r_field T2, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTTwoTprFiveHi` | 20.3 | TPR at 5% FPR (%), r_field T2, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTTwoTprFiveCI` | [9.4, 20.3] | TPR at 5% FPR (%), r_field T2, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTTwoTprFiveN` | 598 | TPR at 5% FPR (%), r_field T2, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRFieldTTwoTprFiveP` | n/a | TPR at 5% FPR (%), r_field T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTThree` | 0.65 | AUROC r_field T3, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRFieldTThreeLo` | 0.63 | AUROC r_field T3, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTThreeHi` | 0.67 | AUROC r_field T3, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTThreeCI` | [0.63, 0.67] | AUROC r_field T3, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTThreeN` | 600 | AUROC r_field T3, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRFieldTThreeP` | n/a | AUROC r_field T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTThreeTprOne` | 3.3 | TPR at 1% FPR (%), r_field T3, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRFieldTThreeTprOneLo` | 1.3 | TPR at 1% FPR (%), r_field T3, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTThreeTprOneHi` | 12.0 | TPR at 1% FPR (%), r_field T3, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTThreeTprOneCI` | [1.3, 12.0] | TPR at 1% FPR (%), r_field T3, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTThreeTprOneN` | 600 | TPR at 1% FPR (%), r_field T3, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRFieldTThreeTprOneP` | n/a | TPR at 1% FPR (%), r_field T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashRFieldTThreeTprFive` | 15.3 | TPR at 5% FPR (%), r_field T3, glm-5.3-flash |
| `\DetGLMFiveThreeFlashRFieldTThreeTprFiveLo` | 10.0 | TPR at 5% FPR (%), r_field T3, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTThreeTprFiveHi` | 21.0 | TPR at 5% FPR (%), r_field T3, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashRFieldTThreeTprFiveCI` | [10.0, 21.0] | TPR at 5% FPR (%), r_field T3, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashRFieldTThreeTprFiveN` | 600 | TPR at 5% FPR (%), r_field T3, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashRFieldTThreeTprFiveP` | n/a | TPR at 5% FPR (%), r_field T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTZero` | 0.63 | AUROC f_trace T0, glm-5.3-flash |
| `\DetGLMFiveThreeFlashFTraceTZeroLo` | 0.61 | AUROC f_trace T0, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTZeroHi` | 0.65 | AUROC f_trace T0, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTZeroCI` | [0.61, 0.65] | AUROC f_trace T0, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTZeroN` | 600 | AUROC f_trace T0, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashFTraceTZeroP` | n/a | AUROC f_trace T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTZeroTprOne` | 8.3 | TPR at 1% FPR (%), f_trace T0, glm-5.3-flash |
| `\DetGLMFiveThreeFlashFTraceTZeroTprOneLo` | 0.7 | TPR at 1% FPR (%), f_trace T0, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTZeroTprOneHi` | 11.3 | TPR at 1% FPR (%), f_trace T0, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTZeroTprOneCI` | [0.7, 11.3] | TPR at 1% FPR (%), f_trace T0, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTZeroTprOneN` | 600 | TPR at 1% FPR (%), f_trace T0, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashFTraceTZeroTprOneP` | n/a | TPR at 1% FPR (%), f_trace T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTZeroTprFive` | 12.0 | TPR at 5% FPR (%), f_trace T0, glm-5.3-flash |
| `\DetGLMFiveThreeFlashFTraceTZeroTprFiveLo` | 8.3 | TPR at 5% FPR (%), f_trace T0, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTZeroTprFiveHi` | 16.7 | TPR at 5% FPR (%), f_trace T0, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTZeroTprFiveCI` | [8.3, 16.7] | TPR at 5% FPR (%), f_trace T0, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTZeroTprFiveN` | 600 | TPR at 5% FPR (%), f_trace T0, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashFTraceTZeroTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTOne` | 0.63 | AUROC f_trace T1, glm-5.3-flash |
| `\DetGLMFiveThreeFlashFTraceTOneLo` | 0.61 | AUROC f_trace T1, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTOneHi` | 0.66 | AUROC f_trace T1, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTOneCI` | [0.61, 0.66] | AUROC f_trace T1, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTOneN` | 592 | AUROC f_trace T1, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashFTraceTOneP` | n/a | AUROC f_trace T1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTOneTprOne` | 4.7 | TPR at 1% FPR (%), f_trace T1, glm-5.3-flash |
| `\DetGLMFiveThreeFlashFTraceTOneTprOneLo` | 0.3 | TPR at 1% FPR (%), f_trace T1, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTOneTprOneHi` | 13.2 | TPR at 1% FPR (%), f_trace T1, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTOneTprOneCI` | [0.3, 13.2] | TPR at 1% FPR (%), f_trace T1, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTOneTprOneN` | 592 | TPR at 1% FPR (%), f_trace T1, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashFTraceTOneTprOneP` | n/a | TPR at 1% FPR (%), f_trace T1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTOneTprFive` | 14.5 | TPR at 5% FPR (%), f_trace T1, glm-5.3-flash |
| `\DetGLMFiveThreeFlashFTraceTOneTprFiveLo` | 9.5 | TPR at 5% FPR (%), f_trace T1, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTOneTprFiveHi` | 19.3 | TPR at 5% FPR (%), f_trace T1, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTOneTprFiveCI` | [9.5, 19.3] | TPR at 5% FPR (%), f_trace T1, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTOneTprFiveN` | 592 | TPR at 5% FPR (%), f_trace T1, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashFTraceTOneTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTTwo` | 0.63 | AUROC f_trace T2, glm-5.3-flash |
| `\DetGLMFiveThreeFlashFTraceTTwoLo` | 0.60 | AUROC f_trace T2, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTTwoHi` | 0.65 | AUROC f_trace T2, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTTwoCI` | [0.60, 0.65] | AUROC f_trace T2, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTTwoN` | 598 | AUROC f_trace T2, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashFTraceTTwoP` | n/a | AUROC f_trace T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTTwoTprOne` | 4.7 | TPR at 1% FPR (%), f_trace T2, glm-5.3-flash |
| `\DetGLMFiveThreeFlashFTraceTTwoTprOneLo` | 0.3 | TPR at 1% FPR (%), f_trace T2, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTTwoTprOneHi` | 13.1 | TPR at 1% FPR (%), f_trace T2, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTTwoTprOneCI` | [0.3, 13.1] | TPR at 1% FPR (%), f_trace T2, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTTwoTprOneN` | 598 | TPR at 1% FPR (%), f_trace T2, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashFTraceTTwoTprOneP` | n/a | TPR at 1% FPR (%), f_trace T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTTwoTprFive` | 13.4 | TPR at 5% FPR (%), f_trace T2, glm-5.3-flash |
| `\DetGLMFiveThreeFlashFTraceTTwoTprFiveLo` | 9.4 | TPR at 5% FPR (%), f_trace T2, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTTwoTprFiveHi` | 18.3 | TPR at 5% FPR (%), f_trace T2, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTTwoTprFiveCI` | [9.4, 18.3] | TPR at 5% FPR (%), f_trace T2, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTTwoTprFiveN` | 598 | TPR at 5% FPR (%), f_trace T2, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashFTraceTTwoTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTThree` | 0.63 | AUROC f_trace T3, glm-5.3-flash |
| `\DetGLMFiveThreeFlashFTraceTThreeLo` | 0.61 | AUROC f_trace T3, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTThreeHi` | 0.66 | AUROC f_trace T3, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTThreeCI` | [0.61, 0.66] | AUROC f_trace T3, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTThreeN` | 600 | AUROC f_trace T3, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashFTraceTThreeP` | n/a | AUROC f_trace T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTThreeTprOne` | 9.7 | TPR at 1% FPR (%), f_trace T3, glm-5.3-flash |
| `\DetGLMFiveThreeFlashFTraceTThreeTprOneLo` | 1.7 | TPR at 1% FPR (%), f_trace T3, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTThreeTprOneHi` | 14.3 | TPR at 1% FPR (%), f_trace T3, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTThreeTprOneCI` | [1.7, 14.3] | TPR at 1% FPR (%), f_trace T3, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTThreeTprOneN` | 600 | TPR at 1% FPR (%), f_trace T3, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashFTraceTThreeTprOneP` | n/a | TPR at 1% FPR (%), f_trace T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveThreeFlashFTraceTThreeTprFive` | 15.3 | TPR at 5% FPR (%), f_trace T3, glm-5.3-flash |
| `\DetGLMFiveThreeFlashFTraceTThreeTprFiveLo` | 10.7 | TPR at 5% FPR (%), f_trace T3, glm-5.3-flash, lower 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTThreeTprFiveHi` | 20.3 | TPR at 5% FPR (%), f_trace T3, glm-5.3-flash, upper 95% CI bound |
| `\DetGLMFiveThreeFlashFTraceTThreeTprFiveCI` | [10.7, 20.3] | TPR at 5% FPR (%), f_trace T3, glm-5.3-flash, 95% CI |
| `\DetGLMFiveThreeFlashFTraceTThreeTprFiveN` | 600 | TPR at 5% FPR (%), f_trace T3, glm-5.3-flash, n |
| `\DetGLMFiveThreeFlashFTraceTThreeTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTZero` | 0.88 | AUROC V T0, glm-5.2 |
| `\DetGLMFiveTwoVTZeroLo` | 0.86 | AUROC V T0, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoVTZeroHi` | 0.89 | AUROC V T0, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoVTZeroCI` | [0.86, 0.89] | AUROC V T0, glm-5.2, 95% CI |
| `\DetGLMFiveTwoVTZeroN` | 600 | AUROC V T0, glm-5.2, n |
| `\DetGLMFiveTwoVTZeroP` | n/a | AUROC V T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTZeroTprOne` | 49.0 | TPR at 1% FPR (%), V T0, glm-5.2 |
| `\DetGLMFiveTwoVTZeroTprOneLo` | 13.3 | TPR at 1% FPR (%), V T0, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoVTZeroTprOneHi` | 72.3 | TPR at 1% FPR (%), V T0, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoVTZeroTprOneCI` | [13.3, 72.3] | TPR at 1% FPR (%), V T0, glm-5.2, 95% CI |
| `\DetGLMFiveTwoVTZeroTprOneN` | 600 | TPR at 1% FPR (%), V T0, glm-5.2, n |
| `\DetGLMFiveTwoVTZeroTprOneP` | n/a | TPR at 1% FPR (%), V T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTZeroTprFive` | 77.7 | TPR at 5% FPR (%), V T0, glm-5.2 |
| `\DetGLMFiveTwoVTZeroTprFiveLo` | 67.7 | TPR at 5% FPR (%), V T0, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoVTZeroTprFiveHi` | 80.0 | TPR at 5% FPR (%), V T0, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoVTZeroTprFiveCI` | [67.7, 80.0] | TPR at 5% FPR (%), V T0, glm-5.2, 95% CI |
| `\DetGLMFiveTwoVTZeroTprFiveN` | 600 | TPR at 5% FPR (%), V T0, glm-5.2, n |
| `\DetGLMFiveTwoVTZeroTprFiveP` | n/a | TPR at 5% FPR (%), V T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTOne` | 0.70 | AUROC V T1, glm-5.2 |
| `\DetGLMFiveTwoVTOneLo` | 0.67 | AUROC V T1, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoVTOneHi` | 0.73 | AUROC V T1, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoVTOneCI` | [0.67, 0.73] | AUROC V T1, glm-5.2, 95% CI |
| `\DetGLMFiveTwoVTOneN` | 586 | AUROC V T1, glm-5.2, n |
| `\DetGLMFiveTwoVTOneP` | n/a | AUROC V T1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTOneTprOne` | 13.0 | TPR at 1% FPR (%), V T1, glm-5.2 |
| `\DetGLMFiveTwoVTOneTprOneLo` | 3.1 | TPR at 1% FPR (%), V T1, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoVTOneTprOneHi` | 31.0 | TPR at 1% FPR (%), V T1, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoVTOneTprOneCI` | [3.1, 31.0] | TPR at 1% FPR (%), V T1, glm-5.2, 95% CI |
| `\DetGLMFiveTwoVTOneTprOneN` | 586 | TPR at 1% FPR (%), V T1, glm-5.2, n |
| `\DetGLMFiveTwoVTOneTprOneP` | n/a | TPR at 1% FPR (%), V T1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTOneTprFive` | 39.6 | TPR at 5% FPR (%), V T1, glm-5.2 |
| `\DetGLMFiveTwoVTOneTprFiveLo` | 25.2 | TPR at 5% FPR (%), V T1, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoVTOneTprFiveHi` | 43.9 | TPR at 5% FPR (%), V T1, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoVTOneTprFiveCI` | [25.2, 43.9] | TPR at 5% FPR (%), V T1, glm-5.2, 95% CI |
| `\DetGLMFiveTwoVTOneTprFiveN` | 586 | TPR at 5% FPR (%), V T1, glm-5.2, n |
| `\DetGLMFiveTwoVTOneTprFiveP` | n/a | TPR at 5% FPR (%), V T1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTTwo` | 0.71 | AUROC V T2, glm-5.2 |
| `\DetGLMFiveTwoVTTwoLo` | 0.68 | AUROC V T2, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoVTTwoHi` | 0.75 | AUROC V T2, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoVTTwoCI` | [0.68, 0.75] | AUROC V T2, glm-5.2, 95% CI |
| `\DetGLMFiveTwoVTTwoN` | 598 | AUROC V T2, glm-5.2, n |
| `\DetGLMFiveTwoVTTwoP` | n/a | AUROC V T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTTwoTprOne` | 13.4 | TPR at 1% FPR (%), V T2, glm-5.2 |
| `\DetGLMFiveTwoVTTwoTprOneLo` | 3.0 | TPR at 1% FPR (%), V T2, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoVTTwoTprOneHi` | 33.4 | TPR at 1% FPR (%), V T2, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoVTTwoTprOneCI` | [3.0, 33.4] | TPR at 1% FPR (%), V T2, glm-5.2, 95% CI |
| `\DetGLMFiveTwoVTTwoTprOneN` | 598 | TPR at 1% FPR (%), V T2, glm-5.2, n |
| `\DetGLMFiveTwoVTTwoTprOneP` | n/a | TPR at 1% FPR (%), V T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTTwoTprFive` | 42.1 | TPR at 5% FPR (%), V T2, glm-5.2 |
| `\DetGLMFiveTwoVTTwoTprFiveLo` | 27.8 | TPR at 5% FPR (%), V T2, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoVTTwoTprFiveHi` | 46.7 | TPR at 5% FPR (%), V T2, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoVTTwoTprFiveCI` | [27.8, 46.7] | TPR at 5% FPR (%), V T2, glm-5.2, 95% CI |
| `\DetGLMFiveTwoVTTwoTprFiveN` | 598 | TPR at 5% FPR (%), V T2, glm-5.2, n |
| `\DetGLMFiveTwoVTTwoTprFiveP` | n/a | TPR at 5% FPR (%), V T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTThree` | 0.68 | AUROC V T3, glm-5.2 |
| `\DetGLMFiveTwoVTThreeLo` | 0.64 | AUROC V T3, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoVTThreeHi` | 0.72 | AUROC V T3, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoVTThreeCI` | [0.64, 0.72] | AUROC V T3, glm-5.2, 95% CI |
| `\DetGLMFiveTwoVTThreeN` | 600 | AUROC V T3, glm-5.2, n |
| `\DetGLMFiveTwoVTThreeP` | n/a | AUROC V T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTThreeTprOne` | 14.3 | TPR at 1% FPR (%), V T3, glm-5.2 |
| `\DetGLMFiveTwoVTThreeTprOneLo` | 2.7 | TPR at 1% FPR (%), V T3, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoVTThreeTprOneHi` | 31.7 | TPR at 1% FPR (%), V T3, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoVTThreeTprOneCI` | [2.7, 31.7] | TPR at 1% FPR (%), V T3, glm-5.2, 95% CI |
| `\DetGLMFiveTwoVTThreeTprOneN` | 600 | TPR at 1% FPR (%), V T3, glm-5.2, n |
| `\DetGLMFiveTwoVTThreeTprOneP` | n/a | TPR at 1% FPR (%), V T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoVTThreeTprFive` | 35.0 | TPR at 5% FPR (%), V T3, glm-5.2 |
| `\DetGLMFiveTwoVTThreeTprFiveLo` | 26.3 | TPR at 5% FPR (%), V T3, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoVTThreeTprFiveHi` | 39.3 | TPR at 5% FPR (%), V T3, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoVTThreeTprFiveCI` | [26.3, 39.3] | TPR at 5% FPR (%), V T3, glm-5.2, 95% CI |
| `\DetGLMFiveTwoVTThreeTprFiveN` | 600 | TPR at 5% FPR (%), V T3, glm-5.2, n |
| `\DetGLMFiveTwoVTThreeTprFiveP` | n/a | TPR at 5% FPR (%), V T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTZero` | 1.00 | AUROC C T0, glm-5.2 |
| `\DetGLMFiveTwoCTZeroLo` | 0.99 | AUROC C T0, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoCTZeroHi` | 1.00 | AUROC C T0, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoCTZeroCI` | [0.99, 1.00] | AUROC C T0, glm-5.2, 95% CI |
| `\DetGLMFiveTwoCTZeroN` | 600 | AUROC C T0, glm-5.2, n |
| `\DetGLMFiveTwoCTZeroP` | n/a | AUROC C T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTZeroTprOne` | 99.7 | TPR at 1% FPR (%), C T0, glm-5.2 |
| `\DetGLMFiveTwoCTZeroTprOneLo` | 96.0 | TPR at 1% FPR (%), C T0, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoCTZeroTprOneHi` | 100.0 | TPR at 1% FPR (%), C T0, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoCTZeroTprOneCI` | [96.0, 100.0] | TPR at 1% FPR (%), C T0, glm-5.2, 95% CI |
| `\DetGLMFiveTwoCTZeroTprOneN` | 600 | TPR at 1% FPR (%), C T0, glm-5.2, n |
| `\DetGLMFiveTwoCTZeroTprOneP` | n/a | TPR at 1% FPR (%), C T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTZeroTprFive` | 99.7 | TPR at 5% FPR (%), C T0, glm-5.2 |
| `\DetGLMFiveTwoCTZeroTprFiveLo` | 99.0 | TPR at 5% FPR (%), C T0, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoCTZeroTprFiveHi` | 100.0 | TPR at 5% FPR (%), C T0, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoCTZeroTprFiveCI` | [99.0, 100.0] | TPR at 5% FPR (%), C T0, glm-5.2, 95% CI |
| `\DetGLMFiveTwoCTZeroTprFiveN` | 600 | TPR at 5% FPR (%), C T0, glm-5.2, n |
| `\DetGLMFiveTwoCTZeroTprFiveP` | n/a | TPR at 5% FPR (%), C T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTOne` | 0.99 | AUROC C T1, glm-5.2 |
| `\DetGLMFiveTwoCTOneLo` | 0.99 | AUROC C T1, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoCTOneHi` | 1.00 | AUROC C T1, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoCTOneCI` | [0.99, 1.00] | AUROC C T1, glm-5.2, 95% CI |
| `\DetGLMFiveTwoCTOneN` | 586 | AUROC C T1, glm-5.2, n |
| `\DetGLMFiveTwoCTOneP` | n/a | AUROC C T1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTOneTprOne` | 98.3 | TPR at 1% FPR (%), C T1, glm-5.2 |
| `\DetGLMFiveTwoCTOneTprOneLo` | 90.2 | TPR at 1% FPR (%), C T1, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoCTOneTprOneHi` | 99.7 | TPR at 1% FPR (%), C T1, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoCTOneTprOneCI` | [90.2, 99.7] | TPR at 1% FPR (%), C T1, glm-5.2, 95% CI |
| `\DetGLMFiveTwoCTOneTprOneN` | 586 | TPR at 1% FPR (%), C T1, glm-5.2, n |
| `\DetGLMFiveTwoCTOneTprOneP` | n/a | TPR at 1% FPR (%), C T1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTOneTprFive` | 98.6 | TPR at 5% FPR (%), C T1, glm-5.2 |
| `\DetGLMFiveTwoCTOneTprFiveLo` | 97.6 | TPR at 5% FPR (%), C T1, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoCTOneTprFiveHi` | 100.0 | TPR at 5% FPR (%), C T1, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoCTOneTprFiveCI` | [97.6, 100.0] | TPR at 5% FPR (%), C T1, glm-5.2, 95% CI |
| `\DetGLMFiveTwoCTOneTprFiveN` | 586 | TPR at 5% FPR (%), C T1, glm-5.2, n |
| `\DetGLMFiveTwoCTOneTprFiveP` | n/a | TPR at 5% FPR (%), C T1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTTwo` | 0.99 | AUROC C T2, glm-5.2 |
| `\DetGLMFiveTwoCTTwoLo` | 0.98 | AUROC C T2, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoCTTwoHi` | 1.00 | AUROC C T2, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoCTTwoCI` | [0.98, 1.00] | AUROC C T2, glm-5.2, 95% CI |
| `\DetGLMFiveTwoCTTwoN` | 598 | AUROC C T2, glm-5.2, n |
| `\DetGLMFiveTwoCTTwoP` | n/a | AUROC C T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTTwoTprOne` | 97.7 | TPR at 1% FPR (%), C T2, glm-5.2 |
| `\DetGLMFiveTwoCTTwoTprOneLo` | 89.9 | TPR at 1% FPR (%), C T2, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoCTTwoTprOneHi` | 99.7 | TPR at 1% FPR (%), C T2, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoCTTwoTprOneCI` | [89.9, 99.7] | TPR at 1% FPR (%), C T2, glm-5.2, 95% CI |
| `\DetGLMFiveTwoCTTwoTprOneN` | 598 | TPR at 1% FPR (%), C T2, glm-5.2, n |
| `\DetGLMFiveTwoCTTwoTprOneP` | n/a | TPR at 1% FPR (%), C T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTTwoTprFive` | 98.7 | TPR at 5% FPR (%), C T2, glm-5.2 |
| `\DetGLMFiveTwoCTTwoTprFiveLo` | 97.3 | TPR at 5% FPR (%), C T2, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoCTTwoTprFiveHi` | 99.7 | TPR at 5% FPR (%), C T2, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoCTTwoTprFiveCI` | [97.3, 99.7] | TPR at 5% FPR (%), C T2, glm-5.2, 95% CI |
| `\DetGLMFiveTwoCTTwoTprFiveN` | 598 | TPR at 5% FPR (%), C T2, glm-5.2, n |
| `\DetGLMFiveTwoCTTwoTprFiveP` | n/a | TPR at 5% FPR (%), C T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTThree` | 0.99 | AUROC C T3, glm-5.2 |
| `\DetGLMFiveTwoCTThreeLo` | 0.98 | AUROC C T3, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoCTThreeHi` | 1.00 | AUROC C T3, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoCTThreeCI` | [0.98, 1.00] | AUROC C T3, glm-5.2, 95% CI |
| `\DetGLMFiveTwoCTThreeN` | 600 | AUROC C T3, glm-5.2, n |
| `\DetGLMFiveTwoCTThreeP` | n/a | AUROC C T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTThreeTprOne` | 97.7 | TPR at 1% FPR (%), C T3, glm-5.2 |
| `\DetGLMFiveTwoCTThreeTprOneLo` | 92.7 | TPR at 1% FPR (%), C T3, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoCTThreeTprOneHi` | 99.0 | TPR at 1% FPR (%), C T3, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoCTThreeTprOneCI` | [92.7, 99.0] | TPR at 1% FPR (%), C T3, glm-5.2, 95% CI |
| `\DetGLMFiveTwoCTThreeTprOneN` | 600 | TPR at 1% FPR (%), C T3, glm-5.2, n |
| `\DetGLMFiveTwoCTThreeTprOneP` | n/a | TPR at 1% FPR (%), C T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoCTThreeTprFive` | 98.0 | TPR at 5% FPR (%), C T3, glm-5.2 |
| `\DetGLMFiveTwoCTThreeTprFiveLo` | 96.3 | TPR at 5% FPR (%), C T3, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoCTThreeTprFiveHi` | 99.3 | TPR at 5% FPR (%), C T3, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoCTThreeTprFiveCI` | [96.3, 99.3] | TPR at 5% FPR (%), C T3, glm-5.2, 95% CI |
| `\DetGLMFiveTwoCTThreeTprFiveN` | 600 | TPR at 5% FPR (%), C T3, glm-5.2, n |
| `\DetGLMFiveTwoCTThreeTprFiveP` | n/a | TPR at 5% FPR (%), C T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTZero` | 1.00 | AUROC R T0, glm-5.2 |
| `\DetGLMFiveTwoRTZeroLo` | 0.99 | AUROC R T0, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRTZeroHi` | 1.00 | AUROC R T0, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRTZeroCI` | [0.99, 1.00] | AUROC R T0, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRTZeroN` | 600 | AUROC R T0, glm-5.2, n |
| `\DetGLMFiveTwoRTZeroP` | n/a | AUROC R T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTZeroTprOne` | 97.3 | TPR at 1% FPR (%), R T0, glm-5.2 |
| `\DetGLMFiveTwoRTZeroTprOneLo` | 81.3 | TPR at 1% FPR (%), R T0, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRTZeroTprOneHi` | 98.7 | TPR at 1% FPR (%), R T0, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRTZeroTprOneCI` | [81.3, 98.7] | TPR at 1% FPR (%), R T0, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRTZeroTprOneN` | 600 | TPR at 1% FPR (%), R T0, glm-5.2, n |
| `\DetGLMFiveTwoRTZeroTprOneP` | n/a | TPR at 1% FPR (%), R T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTZeroTprFive` | 97.3 | TPR at 5% FPR (%), R T0, glm-5.2 |
| `\DetGLMFiveTwoRTZeroTprFiveLo` | 95.7 | TPR at 5% FPR (%), R T0, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRTZeroTprFiveHi` | 99.0 | TPR at 5% FPR (%), R T0, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRTZeroTprFiveCI` | [95.7, 99.0] | TPR at 5% FPR (%), R T0, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRTZeroTprFiveN` | 600 | TPR at 5% FPR (%), R T0, glm-5.2, n |
| `\DetGLMFiveTwoRTZeroTprFiveP` | n/a | TPR at 5% FPR (%), R T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTOne` | 1.00 | AUROC R T1, glm-5.2 |
| `\DetGLMFiveTwoRTOneLo` | 1.00 | AUROC R T1, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRTOneHi` | 1.00 | AUROC R T1, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRTOneCI` | [1.00, 1.00] | AUROC R T1, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRTOneN` | 586 | AUROC R T1, glm-5.2, n |
| `\DetGLMFiveTwoRTOneP` | n/a | AUROC R T1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTOneTprOne` | 98.3 | TPR at 1% FPR (%), R T1, glm-5.2 |
| `\DetGLMFiveTwoRTOneTprOneLo` | 60.7 | TPR at 1% FPR (%), R T1, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRTOneTprOneHi` | 99.7 | TPR at 1% FPR (%), R T1, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRTOneTprOneCI` | [60.7, 99.7] | TPR at 1% FPR (%), R T1, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRTOneTprOneN` | 586 | TPR at 1% FPR (%), R T1, glm-5.2, n |
| `\DetGLMFiveTwoRTOneTprOneP` | n/a | TPR at 1% FPR (%), R T1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTOneTprFive` | 98.3 | TPR at 5% FPR (%), R T1, glm-5.2 |
| `\DetGLMFiveTwoRTOneTprFiveLo` | 96.9 | TPR at 5% FPR (%), R T1, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRTOneTprFiveHi` | 99.7 | TPR at 5% FPR (%), R T1, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRTOneTprFiveCI` | [96.9, 99.7] | TPR at 5% FPR (%), R T1, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRTOneTprFiveN` | 586 | TPR at 5% FPR (%), R T1, glm-5.2, n |
| `\DetGLMFiveTwoRTOneTprFiveP` | n/a | TPR at 5% FPR (%), R T1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTTwo` | 1.00 | AUROC R T2, glm-5.2 |
| `\DetGLMFiveTwoRTTwoLo` | 1.00 | AUROC R T2, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRTTwoHi` | 1.00 | AUROC R T2, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRTTwoCI` | [1.00, 1.00] | AUROC R T2, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRTTwoN` | 598 | AUROC R T2, glm-5.2, n |
| `\DetGLMFiveTwoRTTwoP` | n/a | AUROC R T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTTwoTprOne` | 97.3 | TPR at 1% FPR (%), R T2, glm-5.2 |
| `\DetGLMFiveTwoRTTwoTprOneLo` | 74.7 | TPR at 1% FPR (%), R T2, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRTTwoTprOneHi` | 99.0 | TPR at 1% FPR (%), R T2, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRTTwoTprOneCI` | [74.7, 99.0] | TPR at 1% FPR (%), R T2, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRTTwoTprOneN` | 598 | TPR at 1% FPR (%), R T2, glm-5.2, n |
| `\DetGLMFiveTwoRTTwoTprOneP` | n/a | TPR at 1% FPR (%), R T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTTwoTprFive` | 97.3 | TPR at 5% FPR (%), R T2, glm-5.2 |
| `\DetGLMFiveTwoRTTwoTprFiveLo` | 95.0 | TPR at 5% FPR (%), R T2, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRTTwoTprFiveHi` | 99.0 | TPR at 5% FPR (%), R T2, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRTTwoTprFiveCI` | [95.0, 99.0] | TPR at 5% FPR (%), R T2, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRTTwoTprFiveN` | 598 | TPR at 5% FPR (%), R T2, glm-5.2, n |
| `\DetGLMFiveTwoRTTwoTprFiveP` | n/a | TPR at 5% FPR (%), R T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTThree` | 1.00 | AUROC R T3, glm-5.2 |
| `\DetGLMFiveTwoRTThreeLo` | 0.99 | AUROC R T3, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRTThreeHi` | 1.00 | AUROC R T3, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRTThreeCI` | [0.99, 1.00] | AUROC R T3, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRTThreeN` | 600 | AUROC R T3, glm-5.2, n |
| `\DetGLMFiveTwoRTThreeP` | n/a | AUROC R T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTThreeTprOne` | 97.7 | TPR at 1% FPR (%), R T3, glm-5.2 |
| `\DetGLMFiveTwoRTThreeTprOneLo` | 80.3 | TPR at 1% FPR (%), R T3, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRTThreeTprOneHi` | 99.0 | TPR at 1% FPR (%), R T3, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRTThreeTprOneCI` | [80.3, 99.0] | TPR at 1% FPR (%), R T3, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRTThreeTprOneN` | 600 | TPR at 1% FPR (%), R T3, glm-5.2, n |
| `\DetGLMFiveTwoRTThreeTprOneP` | n/a | TPR at 1% FPR (%), R T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRTThreeTprFive` | 97.7 | TPR at 5% FPR (%), R T3, glm-5.2 |
| `\DetGLMFiveTwoRTThreeTprFiveLo` | 96.0 | TPR at 5% FPR (%), R T3, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRTThreeTprFiveHi` | 99.3 | TPR at 5% FPR (%), R T3, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRTThreeTprFiveCI` | [96.0, 99.3] | TPR at 5% FPR (%), R T3, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRTThreeTprFiveN` | 600 | TPR at 5% FPR (%), R T3, glm-5.2, n |
| `\DetGLMFiveTwoRTThreeTprFiveP` | n/a | TPR at 5% FPR (%), R T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTZero` | 0.66 | AUROC r_field T0, glm-5.2 |
| `\DetGLMFiveTwoRFieldTZeroLo` | 0.63 | AUROC r_field T0, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTZeroHi` | 0.68 | AUROC r_field T0, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTZeroCI` | [0.63, 0.68] | AUROC r_field T0, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRFieldTZeroN` | 600 | AUROC r_field T0, glm-5.2, n |
| `\DetGLMFiveTwoRFieldTZeroP` | n/a | AUROC r_field T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTZeroTprOne` | 3.0 | TPR at 1% FPR (%), r_field T0, glm-5.2 |
| `\DetGLMFiveTwoRFieldTZeroTprOneLo` | 0.7 | TPR at 1% FPR (%), r_field T0, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTZeroTprOneHi` | 4.7 | TPR at 1% FPR (%), r_field T0, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTZeroTprOneCI` | [0.7, 4.7] | TPR at 1% FPR (%), r_field T0, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRFieldTZeroTprOneN` | 600 | TPR at 1% FPR (%), r_field T0, glm-5.2, n |
| `\DetGLMFiveTwoRFieldTZeroTprOneP` | n/a | TPR at 1% FPR (%), r_field T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTZeroTprFive` | 13.7 | TPR at 5% FPR (%), r_field T0, glm-5.2 |
| `\DetGLMFiveTwoRFieldTZeroTprFiveLo` | 6.7 | TPR at 5% FPR (%), r_field T0, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTZeroTprFiveHi` | 20.7 | TPR at 5% FPR (%), r_field T0, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTZeroTprFiveCI` | [6.7, 20.7] | TPR at 5% FPR (%), r_field T0, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRFieldTZeroTprFiveN` | 600 | TPR at 5% FPR (%), r_field T0, glm-5.2, n |
| `\DetGLMFiveTwoRFieldTZeroTprFiveP` | n/a | TPR at 5% FPR (%), r_field T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTOne` | 0.66 | AUROC r_field T1, glm-5.2 |
| `\DetGLMFiveTwoRFieldTOneLo` | 0.64 | AUROC r_field T1, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTOneHi` | 0.69 | AUROC r_field T1, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTOneCI` | [0.64, 0.69] | AUROC r_field T1, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRFieldTOneN` | 586 | AUROC r_field T1, glm-5.2, n |
| `\DetGLMFiveTwoRFieldTOneP` | n/a | AUROC r_field T1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTOneTprOne` | 4.4 | TPR at 1% FPR (%), r_field T1, glm-5.2 |
| `\DetGLMFiveTwoRFieldTOneTprOneLo` | 2.7 | TPR at 1% FPR (%), r_field T1, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTOneTprOneHi` | 7.8 | TPR at 1% FPR (%), r_field T1, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTOneTprOneCI` | [2.7, 7.8] | TPR at 1% FPR (%), r_field T1, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRFieldTOneTprOneN` | 586 | TPR at 1% FPR (%), r_field T1, glm-5.2, n |
| `\DetGLMFiveTwoRFieldTOneTprOneP` | n/a | TPR at 1% FPR (%), r_field T1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTOneTprFive` | 10.9 | TPR at 5% FPR (%), r_field T1, glm-5.2 |
| `\DetGLMFiveTwoRFieldTOneTprFiveLo` | 7.5 | TPR at 5% FPR (%), r_field T1, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTOneTprFiveHi` | 24.5 | TPR at 5% FPR (%), r_field T1, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTOneTprFiveCI` | [7.5, 24.5] | TPR at 5% FPR (%), r_field T1, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRFieldTOneTprFiveN` | 586 | TPR at 5% FPR (%), r_field T1, glm-5.2, n |
| `\DetGLMFiveTwoRFieldTOneTprFiveP` | n/a | TPR at 5% FPR (%), r_field T1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTTwo` | 0.68 | AUROC r_field T2, glm-5.2 |
| `\DetGLMFiveTwoRFieldTTwoLo` | 0.66 | AUROC r_field T2, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTTwoHi` | 0.70 | AUROC r_field T2, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTTwoCI` | [0.66, 0.70] | AUROC r_field T2, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRFieldTTwoN` | 598 | AUROC r_field T2, glm-5.2, n |
| `\DetGLMFiveTwoRFieldTTwoP` | n/a | AUROC r_field T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTTwoTprOne` | 3.0 | TPR at 1% FPR (%), r_field T2, glm-5.2 |
| `\DetGLMFiveTwoRFieldTTwoTprOneLo` | 0.3 | TPR at 1% FPR (%), r_field T2, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTTwoTprOneHi` | 7.7 | TPR at 1% FPR (%), r_field T2, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTTwoTprOneCI` | [0.3, 7.7] | TPR at 1% FPR (%), r_field T2, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRFieldTTwoTprOneN` | 598 | TPR at 1% FPR (%), r_field T2, glm-5.2, n |
| `\DetGLMFiveTwoRFieldTTwoTprOneP` | n/a | TPR at 1% FPR (%), r_field T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTTwoTprFive` | 10.4 | TPR at 5% FPR (%), r_field T2, glm-5.2 |
| `\DetGLMFiveTwoRFieldTTwoTprFiveLo` | 7.3 | TPR at 5% FPR (%), r_field T2, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTTwoTprFiveHi` | 24.3 | TPR at 5% FPR (%), r_field T2, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTTwoTprFiveCI` | [7.3, 24.3] | TPR at 5% FPR (%), r_field T2, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRFieldTTwoTprFiveN` | 598 | TPR at 5% FPR (%), r_field T2, glm-5.2, n |
| `\DetGLMFiveTwoRFieldTTwoTprFiveP` | n/a | TPR at 5% FPR (%), r_field T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTThree` | 0.68 | AUROC r_field T3, glm-5.2 |
| `\DetGLMFiveTwoRFieldTThreeLo` | 0.66 | AUROC r_field T3, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTThreeHi` | 0.70 | AUROC r_field T3, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTThreeCI` | [0.66, 0.70] | AUROC r_field T3, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRFieldTThreeN` | 600 | AUROC r_field T3, glm-5.2, n |
| `\DetGLMFiveTwoRFieldTThreeP` | n/a | AUROC r_field T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTThreeTprOne` | 5.0 | TPR at 1% FPR (%), r_field T3, glm-5.2 |
| `\DetGLMFiveTwoRFieldTThreeTprOneLo` | 1.3 | TPR at 1% FPR (%), r_field T3, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTThreeTprOneHi` | 8.7 | TPR at 1% FPR (%), r_field T3, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTThreeTprOneCI` | [1.3, 8.7] | TPR at 1% FPR (%), r_field T3, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRFieldTThreeTprOneN` | 600 | TPR at 1% FPR (%), r_field T3, glm-5.2, n |
| `\DetGLMFiveTwoRFieldTThreeTprOneP` | n/a | TPR at 1% FPR (%), r_field T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoRFieldTThreeTprFive` | 14.0 | TPR at 5% FPR (%), r_field T3, glm-5.2 |
| `\DetGLMFiveTwoRFieldTThreeTprFiveLo` | 7.7 | TPR at 5% FPR (%), r_field T3, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoRFieldTThreeTprFiveHi` | 26.0 | TPR at 5% FPR (%), r_field T3, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoRFieldTThreeTprFiveCI` | [7.7, 26.0] | TPR at 5% FPR (%), r_field T3, glm-5.2, 95% CI |
| `\DetGLMFiveTwoRFieldTThreeTprFiveN` | 600 | TPR at 5% FPR (%), r_field T3, glm-5.2, n |
| `\DetGLMFiveTwoRFieldTThreeTprFiveP` | n/a | TPR at 5% FPR (%), r_field T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTZero` | 0.66 | AUROC f_trace T0, glm-5.2 |
| `\DetGLMFiveTwoFTraceTZeroLo` | 0.64 | AUROC f_trace T0, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTZeroHi` | 0.68 | AUROC f_trace T0, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTZeroCI` | [0.64, 0.68] | AUROC f_trace T0, glm-5.2, 95% CI |
| `\DetGLMFiveTwoFTraceTZeroN` | 600 | AUROC f_trace T0, glm-5.2, n |
| `\DetGLMFiveTwoFTraceTZeroP` | n/a | AUROC f_trace T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTZeroTprOne` | 2.7 | TPR at 1% FPR (%), f_trace T0, glm-5.2 |
| `\DetGLMFiveTwoFTraceTZeroTprOneLo` | 1.0 | TPR at 1% FPR (%), f_trace T0, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTZeroTprOneHi` | 9.0 | TPR at 1% FPR (%), f_trace T0, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTZeroTprOneCI` | [1.0, 9.0] | TPR at 1% FPR (%), f_trace T0, glm-5.2, 95% CI |
| `\DetGLMFiveTwoFTraceTZeroTprOneN` | 600 | TPR at 1% FPR (%), f_trace T0, glm-5.2, n |
| `\DetGLMFiveTwoFTraceTZeroTprOneP` | n/a | TPR at 1% FPR (%), f_trace T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTZeroTprFive` | 19.7 | TPR at 5% FPR (%), f_trace T0, glm-5.2 |
| `\DetGLMFiveTwoFTraceTZeroTprFiveLo` | 12.0 | TPR at 5% FPR (%), f_trace T0, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTZeroTprFiveHi` | 24.0 | TPR at 5% FPR (%), f_trace T0, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTZeroTprFiveCI` | [12.0, 24.0] | TPR at 5% FPR (%), f_trace T0, glm-5.2, 95% CI |
| `\DetGLMFiveTwoFTraceTZeroTprFiveN` | 600 | TPR at 5% FPR (%), f_trace T0, glm-5.2, n |
| `\DetGLMFiveTwoFTraceTZeroTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTOne` | 0.67 | AUROC f_trace T1, glm-5.2 |
| `\DetGLMFiveTwoFTraceTOneLo` | 0.64 | AUROC f_trace T1, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTOneHi` | 0.69 | AUROC f_trace T1, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTOneCI` | [0.64, 0.69] | AUROC f_trace T1, glm-5.2, 95% CI |
| `\DetGLMFiveTwoFTraceTOneN` | 586 | AUROC f_trace T1, glm-5.2, n |
| `\DetGLMFiveTwoFTraceTOneP` | n/a | AUROC f_trace T1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTOneTprOne` | 5.5 | TPR at 1% FPR (%), f_trace T1, glm-5.2 |
| `\DetGLMFiveTwoFTraceTOneTprOneLo` | 2.0 | TPR at 1% FPR (%), f_trace T1, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTOneTprOneHi` | 9.2 | TPR at 1% FPR (%), f_trace T1, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTOneTprOneCI` | [2.0, 9.2] | TPR at 1% FPR (%), f_trace T1, glm-5.2, 95% CI |
| `\DetGLMFiveTwoFTraceTOneTprOneN` | 586 | TPR at 1% FPR (%), f_trace T1, glm-5.2, n |
| `\DetGLMFiveTwoFTraceTOneTprOneP` | n/a | TPR at 1% FPR (%), f_trace T1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTOneTprFive` | 21.2 | TPR at 5% FPR (%), f_trace T1, glm-5.2 |
| `\DetGLMFiveTwoFTraceTOneTprFiveLo` | 14.4 | TPR at 5% FPR (%), f_trace T1, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTOneTprFiveHi` | 30.6 | TPR at 5% FPR (%), f_trace T1, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTOneTprFiveCI` | [14.4, 30.6] | TPR at 5% FPR (%), f_trace T1, glm-5.2, 95% CI |
| `\DetGLMFiveTwoFTraceTOneTprFiveN` | 586 | TPR at 5% FPR (%), f_trace T1, glm-5.2, n |
| `\DetGLMFiveTwoFTraceTOneTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTTwo` | 0.69 | AUROC f_trace T2, glm-5.2 |
| `\DetGLMFiveTwoFTraceTTwoLo` | 0.67 | AUROC f_trace T2, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTTwoHi` | 0.71 | AUROC f_trace T2, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTTwoCI` | [0.67, 0.71] | AUROC f_trace T2, glm-5.2, 95% CI |
| `\DetGLMFiveTwoFTraceTTwoN` | 598 | AUROC f_trace T2, glm-5.2, n |
| `\DetGLMFiveTwoFTraceTTwoP` | n/a | AUROC f_trace T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTTwoTprOne` | 6.4 | TPR at 1% FPR (%), f_trace T2, glm-5.2 |
| `\DetGLMFiveTwoFTraceTTwoTprOneLo` | 2.4 | TPR at 1% FPR (%), f_trace T2, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTTwoTprOneHi` | 11.0 | TPR at 1% FPR (%), f_trace T2, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTTwoTprOneCI` | [2.4, 11.0] | TPR at 1% FPR (%), f_trace T2, glm-5.2, 95% CI |
| `\DetGLMFiveTwoFTraceTTwoTprOneN` | 598 | TPR at 1% FPR (%), f_trace T2, glm-5.2, n |
| `\DetGLMFiveTwoFTraceTTwoTprOneP` | n/a | TPR at 1% FPR (%), f_trace T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTTwoTprFive` | 19.7 | TPR at 5% FPR (%), f_trace T2, glm-5.2 |
| `\DetGLMFiveTwoFTraceTTwoTprFiveLo` | 14.0 | TPR at 5% FPR (%), f_trace T2, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTTwoTprFiveHi` | 29.9 | TPR at 5% FPR (%), f_trace T2, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTTwoTprFiveCI` | [14.0, 29.9] | TPR at 5% FPR (%), f_trace T2, glm-5.2, 95% CI |
| `\DetGLMFiveTwoFTraceTTwoTprFiveN` | 598 | TPR at 5% FPR (%), f_trace T2, glm-5.2, n |
| `\DetGLMFiveTwoFTraceTTwoTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTThree` | 0.69 | AUROC f_trace T3, glm-5.2 |
| `\DetGLMFiveTwoFTraceTThreeLo` | 0.67 | AUROC f_trace T3, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTThreeHi` | 0.71 | AUROC f_trace T3, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTThreeCI` | [0.67, 0.71] | AUROC f_trace T3, glm-5.2, 95% CI |
| `\DetGLMFiveTwoFTraceTThreeN` | 600 | AUROC f_trace T3, glm-5.2, n |
| `\DetGLMFiveTwoFTraceTThreeP` | n/a | AUROC f_trace T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTThreeTprOne` | 6.7 | TPR at 1% FPR (%), f_trace T3, glm-5.2 |
| `\DetGLMFiveTwoFTraceTThreeTprOneLo` | 3.3 | TPR at 1% FPR (%), f_trace T3, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTThreeTprOneHi` | 12.3 | TPR at 1% FPR (%), f_trace T3, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTThreeTprOneCI` | [3.3, 12.3] | TPR at 1% FPR (%), f_trace T3, glm-5.2, 95% CI |
| `\DetGLMFiveTwoFTraceTThreeTprOneN` | 600 | TPR at 1% FPR (%), f_trace T3, glm-5.2, n |
| `\DetGLMFiveTwoFTraceTThreeTprOneP` | n/a | TPR at 1% FPR (%), f_trace T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetGLMFiveTwoFTraceTThreeTprFive` | 25.3 | TPR at 5% FPR (%), f_trace T3, glm-5.2 |
| `\DetGLMFiveTwoFTraceTThreeTprFiveLo` | 14.7 | TPR at 5% FPR (%), f_trace T3, glm-5.2, lower 95% CI bound |
| `\DetGLMFiveTwoFTraceTThreeTprFiveHi` | 30.3 | TPR at 5% FPR (%), f_trace T3, glm-5.2, upper 95% CI bound |
| `\DetGLMFiveTwoFTraceTThreeTprFiveCI` | [14.7, 30.3] | TPR at 5% FPR (%), f_trace T3, glm-5.2, 95% CI |
| `\DetGLMFiveTwoFTraceTThreeTprFiveN` | 600 | TPR at 5% FPR (%), f_trace T3, glm-5.2, n |
| `\DetGLMFiveTwoFTraceTThreeTprFiveP` | n/a | TPR at 5% FPR (%), f_trace T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatPooledCTZero` | 1.6 | flat-audit rate (%): all 7 entries same score, C, T0 stores, pooled |
| `\DetFlatPooledCTZeroLo` | 0.9 | flat-audit rate (%): all 7 entries same score, C, T0 stores, pooled, lower 95% CI bound |
| `\DetFlatPooledCTZeroHi` | 2.3 | flat-audit rate (%): all 7 entries same score, C, T0 stores, pooled, upper 95% CI bound |
| `\DetFlatPooledCTZeroCI` | [0.9, 2.3] | flat-audit rate (%): all 7 entries same score, C, T0 stores, pooled, 95% CI |
| `\DetFlatPooledCTZeroN` | 1{,}478 | flat-audit rate (%): all 7 entries same score, C, T0 stores, pooled, n |
| `\DetFlatPooledCTZeroP` | n/a | flat-audit rate (%): all 7 entries same score, C, T0 stores, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatDeepSeekVFourFlashCTZero` | 6.7 | flat-audit rate (%): all 7 entries same score, C, T0 stores, deepseek-v4-flash |
| `\DetFlatDeepSeekVFourFlashCTZeroLo` | 4.0 | flat-audit rate (%): all 7 entries same score, C, T0 stores, deepseek-v4-flash, lower 95% CI bound |
| `\DetFlatDeepSeekVFourFlashCTZeroHi` | 10.0 | flat-audit rate (%): all 7 entries same score, C, T0 stores, deepseek-v4-flash, upper 95% CI bound |
| `\DetFlatDeepSeekVFourFlashCTZeroCI` | [4.0, 10.0] | flat-audit rate (%): all 7 entries same score, C, T0 stores, deepseek-v4-flash, 95% CI |
| `\DetFlatDeepSeekVFourFlashCTZeroN` | 300 | flat-audit rate (%): all 7 entries same score, C, T0 stores, deepseek-v4-flash, n |
| `\DetFlatDeepSeekVFourFlashCTZeroP` | n/a | flat-audit rate (%): all 7 entries same score, C, T0 stores, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGemmaFourThreeOneBCTZero` | 0.7 | flat-audit rate (%): all 7 entries same score, C, T0 stores, gemma-4-31b-it |
| `\DetFlatGemmaFourThreeOneBCTZeroLo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T0 stores, gemma-4-31b-it, lower 95% CI bound |
| `\DetFlatGemmaFourThreeOneBCTZeroHi` | 1.8 | flat-audit rate (%): all 7 entries same score, C, T0 stores, gemma-4-31b-it, upper 95% CI bound |
| `\DetFlatGemmaFourThreeOneBCTZeroCI` | [0.0, 1.8] | flat-audit rate (%): all 7 entries same score, C, T0 stores, gemma-4-31b-it, 95% CI |
| `\DetFlatGemmaFourThreeOneBCTZeroN` | 278 | flat-audit rate (%): all 7 entries same score, C, T0 stores, gemma-4-31b-it, n |
| `\DetFlatGemmaFourThreeOneBCTZeroP` | n/a | flat-audit rate (%): all 7 entries same score, C, T0 stores, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveTwoCTZero` | 0.3 | flat-audit rate (%): all 7 entries same score, C, T0 stores, glm-5.2 |
| `\DetFlatGLMFiveTwoCTZeroLo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T0 stores, glm-5.2, lower 95% CI bound |
| `\DetFlatGLMFiveTwoCTZeroHi` | 1.0 | flat-audit rate (%): all 7 entries same score, C, T0 stores, glm-5.2, upper 95% CI bound |
| `\DetFlatGLMFiveTwoCTZeroCI` | [0.0, 1.0] | flat-audit rate (%): all 7 entries same score, C, T0 stores, glm-5.2, 95% CI |
| `\DetFlatGLMFiveTwoCTZeroN` | 300 | flat-audit rate (%): all 7 entries same score, C, T0 stores, glm-5.2, n |
| `\DetFlatGLMFiveTwoCTZeroP` | n/a | flat-audit rate (%): all 7 entries same score, C, T0 stores, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveThreeFlashCTZero` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T0 stores, glm-5.3-flash |
| `\DetFlatGLMFiveThreeFlashCTZeroLo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T0 stores, glm-5.3-flash, lower 95% CI bound |
| `\DetFlatGLMFiveThreeFlashCTZeroHi` | 1.2 | flat-audit rate (%): all 7 entries same score, C, T0 stores, glm-5.3-flash, upper 95% CI bound |
| `\DetFlatGLMFiveThreeFlashCTZeroCI` | [0.0, 1.2] | flat-audit rate (%): all 7 entries same score, C, T0 stores, glm-5.3-flash, 95% CI |
| `\DetFlatGLMFiveThreeFlashCTZeroN` | 300 | flat-audit rate (%): all 7 entries same score, C, T0 stores, glm-5.3-flash, n |
| `\DetFlatGLMFiveThreeFlashCTZeroP` | n/a | flat-audit rate (%): all 7 entries same score, C, T0 stores, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatQwenThreeEightTwoSevenBCTZero` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T0 stores, qwen3.8-27b |
| `\DetFlatQwenThreeEightTwoSevenBCTZeroLo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T0 stores, qwen3.8-27b, lower 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBCTZeroHi` | 1.2 | flat-audit rate (%): all 7 entries same score, C, T0 stores, qwen3.8-27b, upper 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBCTZeroCI` | [0.0, 1.2] | flat-audit rate (%): all 7 entries same score, C, T0 stores, qwen3.8-27b, 95% CI |
| `\DetFlatQwenThreeEightTwoSevenBCTZeroN` | 300 | flat-audit rate (%): all 7 entries same score, C, T0 stores, qwen3.8-27b, n |
| `\DetFlatQwenThreeEightTwoSevenBCTZeroP` | n/a | flat-audit rate (%): all 7 entries same score, C, T0 stores, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatPooledCTOne` | 1.9 | flat-audit rate (%): all 7 entries same score, C, T1 stores, pooled |
| `\DetFlatPooledCTOneLo` | 1.1 | flat-audit rate (%): all 7 entries same score, C, T1 stores, pooled, lower 95% CI bound |
| `\DetFlatPooledCTOneHi` | 2.9 | flat-audit rate (%): all 7 entries same score, C, T1 stores, pooled, upper 95% CI bound |
| `\DetFlatPooledCTOneCI` | [1.1, 2.9] | flat-audit rate (%): all 7 entries same score, C, T1 stores, pooled, 95% CI |
| `\DetFlatPooledCTOneN` | 1{,}456 | flat-audit rate (%): all 7 entries same score, C, T1 stores, pooled, n |
| `\DetFlatPooledCTOneP` | n/a | flat-audit rate (%): all 7 entries same score, C, T1 stores, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatDeepSeekVFourFlashCTOne` | 7.1 | flat-audit rate (%): all 7 entries same score, C, T1 stores, deepseek-v4-flash |
| `\DetFlatDeepSeekVFourFlashCTOneLo` | 4.0 | flat-audit rate (%): all 7 entries same score, C, T1 stores, deepseek-v4-flash, lower 95% CI bound |
| `\DetFlatDeepSeekVFourFlashCTOneHi` | 10.9 | flat-audit rate (%): all 7 entries same score, C, T1 stores, deepseek-v4-flash, upper 95% CI bound |
| `\DetFlatDeepSeekVFourFlashCTOneCI` | [4.0, 10.9] | flat-audit rate (%): all 7 entries same score, C, T1 stores, deepseek-v4-flash, 95% CI |
| `\DetFlatDeepSeekVFourFlashCTOneN` | 297 | flat-audit rate (%): all 7 entries same score, C, T1 stores, deepseek-v4-flash, n |
| `\DetFlatDeepSeekVFourFlashCTOneP` | n/a | flat-audit rate (%): all 7 entries same score, C, T1 stores, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGemmaFourThreeOneBCTOne` | 1.1 | flat-audit rate (%): all 7 entries same score, C, T1 stores, gemma-4-31b-it |
| `\DetFlatGemmaFourThreeOneBCTOneLo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T1 stores, gemma-4-31b-it, lower 95% CI bound |
| `\DetFlatGemmaFourThreeOneBCTOneHi` | 2.5 | flat-audit rate (%): all 7 entries same score, C, T1 stores, gemma-4-31b-it, upper 95% CI bound |
| `\DetFlatGemmaFourThreeOneBCTOneCI` | [0.0, 2.5] | flat-audit rate (%): all 7 entries same score, C, T1 stores, gemma-4-31b-it, 95% CI |
| `\DetFlatGemmaFourThreeOneBCTOneN` | 277 | flat-audit rate (%): all 7 entries same score, C, T1 stores, gemma-4-31b-it, n |
| `\DetFlatGemmaFourThreeOneBCTOneP` | n/a | flat-audit rate (%): all 7 entries same score, C, T1 stores, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveTwoCTOne` | 1.0 | flat-audit rate (%): all 7 entries same score, C, T1 stores, glm-5.2 |
| `\DetFlatGLMFiveTwoCTOneLo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T1 stores, glm-5.2, lower 95% CI bound |
| `\DetFlatGLMFiveTwoCTOneHi` | 2.4 | flat-audit rate (%): all 7 entries same score, C, T1 stores, glm-5.2, upper 95% CI bound |
| `\DetFlatGLMFiveTwoCTOneCI` | [0.0, 2.4] | flat-audit rate (%): all 7 entries same score, C, T1 stores, glm-5.2, 95% CI |
| `\DetFlatGLMFiveTwoCTOneN` | 293 | flat-audit rate (%): all 7 entries same score, C, T1 stores, glm-5.2, n |
| `\DetFlatGLMFiveTwoCTOneP` | n/a | flat-audit rate (%): all 7 entries same score, C, T1 stores, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveThreeFlashCTOne` | 0.3 | flat-audit rate (%): all 7 entries same score, C, T1 stores, glm-5.3-flash |
| `\DetFlatGLMFiveThreeFlashCTOneLo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T1 stores, glm-5.3-flash, lower 95% CI bound |
| `\DetFlatGLMFiveThreeFlashCTOneHi` | 1.0 | flat-audit rate (%): all 7 entries same score, C, T1 stores, glm-5.3-flash, upper 95% CI bound |
| `\DetFlatGLMFiveThreeFlashCTOneCI` | [0.0, 1.0] | flat-audit rate (%): all 7 entries same score, C, T1 stores, glm-5.3-flash, 95% CI |
| `\DetFlatGLMFiveThreeFlashCTOneN` | 296 | flat-audit rate (%): all 7 entries same score, C, T1 stores, glm-5.3-flash, n |
| `\DetFlatGLMFiveThreeFlashCTOneP` | n/a | flat-audit rate (%): all 7 entries same score, C, T1 stores, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatQwenThreeEightTwoSevenBCTOne` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T1 stores, qwen3.8-27b |
| `\DetFlatQwenThreeEightTwoSevenBCTOneLo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T1 stores, qwen3.8-27b, lower 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBCTOneHi` | 1.3 | flat-audit rate (%): all 7 entries same score, C, T1 stores, qwen3.8-27b, upper 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBCTOneCI` | [0.0, 1.3] | flat-audit rate (%): all 7 entries same score, C, T1 stores, qwen3.8-27b, 95% CI |
| `\DetFlatQwenThreeEightTwoSevenBCTOneN` | 293 | flat-audit rate (%): all 7 entries same score, C, T1 stores, qwen3.8-27b, n |
| `\DetFlatQwenThreeEightTwoSevenBCTOneP` | n/a | flat-audit rate (%): all 7 entries same score, C, T1 stores, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatPooledCTTwo` | 1.8 | flat-audit rate (%): all 7 entries same score, C, T2 stores, pooled |
| `\DetFlatPooledCTTwoLo` | 1.0 | flat-audit rate (%): all 7 entries same score, C, T2 stores, pooled, lower 95% CI bound |
| `\DetFlatPooledCTTwoHi` | 2.6 | flat-audit rate (%): all 7 entries same score, C, T2 stores, pooled, upper 95% CI bound |
| `\DetFlatPooledCTTwoCI` | [1.0, 2.6] | flat-audit rate (%): all 7 entries same score, C, T2 stores, pooled, 95% CI |
| `\DetFlatPooledCTTwoN` | 1{,}458 | flat-audit rate (%): all 7 entries same score, C, T2 stores, pooled, n |
| `\DetFlatPooledCTTwoP` | n/a | flat-audit rate (%): all 7 entries same score, C, T2 stores, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatDeepSeekVFourFlashCTTwo` | 6.0 | flat-audit rate (%): all 7 entries same score, C, T2 stores, deepseek-v4-flash |
| `\DetFlatDeepSeekVFourFlashCTTwoLo` | 3.7 | flat-audit rate (%): all 7 entries same score, C, T2 stores, deepseek-v4-flash, lower 95% CI bound |
| `\DetFlatDeepSeekVFourFlashCTTwoHi` | 8.4 | flat-audit rate (%): all 7 entries same score, C, T2 stores, deepseek-v4-flash, upper 95% CI bound |
| `\DetFlatDeepSeekVFourFlashCTTwoCI` | [3.7, 8.4] | flat-audit rate (%): all 7 entries same score, C, T2 stores, deepseek-v4-flash, 95% CI |
| `\DetFlatDeepSeekVFourFlashCTTwoN` | 298 | flat-audit rate (%): all 7 entries same score, C, T2 stores, deepseek-v4-flash, n |
| `\DetFlatDeepSeekVFourFlashCTTwoP` | n/a | flat-audit rate (%): all 7 entries same score, C, T2 stores, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGemmaFourThreeOneBCTTwo` | 1.1 | flat-audit rate (%): all 7 entries same score, C, T2 stores, gemma-4-31b-it |
| `\DetFlatGemmaFourThreeOneBCTTwoLo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T2 stores, gemma-4-31b-it, lower 95% CI bound |
| `\DetFlatGemmaFourThreeOneBCTTwoHi` | 2.6 | flat-audit rate (%): all 7 entries same score, C, T2 stores, gemma-4-31b-it, upper 95% CI bound |
| `\DetFlatGemmaFourThreeOneBCTTwoCI` | [0.0, 2.6] | flat-audit rate (%): all 7 entries same score, C, T2 stores, gemma-4-31b-it, 95% CI |
| `\DetFlatGemmaFourThreeOneBCTTwoN` | 269 | flat-audit rate (%): all 7 entries same score, C, T2 stores, gemma-4-31b-it, n |
| `\DetFlatGemmaFourThreeOneBCTTwoP` | n/a | flat-audit rate (%): all 7 entries same score, C, T2 stores, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveTwoCTTwo` | 1.3 | flat-audit rate (%): all 7 entries same score, C, T2 stores, glm-5.2 |
| `\DetFlatGLMFiveTwoCTTwoLo` | 0.3 | flat-audit rate (%): all 7 entries same score, C, T2 stores, glm-5.2, lower 95% CI bound |
| `\DetFlatGLMFiveTwoCTTwoHi` | 2.7 | flat-audit rate (%): all 7 entries same score, C, T2 stores, glm-5.2, upper 95% CI bound |
| `\DetFlatGLMFiveTwoCTTwoCI` | [0.3, 2.7] | flat-audit rate (%): all 7 entries same score, C, T2 stores, glm-5.2, 95% CI |
| `\DetFlatGLMFiveTwoCTTwoN` | 299 | flat-audit rate (%): all 7 entries same score, C, T2 stores, glm-5.2, n |
| `\DetFlatGLMFiveTwoCTTwoP` | n/a | flat-audit rate (%): all 7 entries same score, C, T2 stores, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveThreeFlashCTTwo` | 0.3 | flat-audit rate (%): all 7 entries same score, C, T2 stores, glm-5.3-flash |
| `\DetFlatGLMFiveThreeFlashCTTwoLo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T2 stores, glm-5.3-flash, lower 95% CI bound |
| `\DetFlatGLMFiveThreeFlashCTTwoHi` | 1.0 | flat-audit rate (%): all 7 entries same score, C, T2 stores, glm-5.3-flash, upper 95% CI bound |
| `\DetFlatGLMFiveThreeFlashCTTwoCI` | [0.0, 1.0] | flat-audit rate (%): all 7 entries same score, C, T2 stores, glm-5.3-flash, 95% CI |
| `\DetFlatGLMFiveThreeFlashCTTwoN` | 299 | flat-audit rate (%): all 7 entries same score, C, T2 stores, glm-5.3-flash, n |
| `\DetFlatGLMFiveThreeFlashCTTwoP` | n/a | flat-audit rate (%): all 7 entries same score, C, T2 stores, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatQwenThreeEightTwoSevenBCTTwo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T2 stores, qwen3.8-27b |
| `\DetFlatQwenThreeEightTwoSevenBCTTwoLo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T2 stores, qwen3.8-27b, lower 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBCTTwoHi` | 1.3 | flat-audit rate (%): all 7 entries same score, C, T2 stores, qwen3.8-27b, upper 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBCTTwoCI` | [0.0, 1.3] | flat-audit rate (%): all 7 entries same score, C, T2 stores, qwen3.8-27b, 95% CI |
| `\DetFlatQwenThreeEightTwoSevenBCTTwoN` | 293 | flat-audit rate (%): all 7 entries same score, C, T2 stores, qwen3.8-27b, n |
| `\DetFlatQwenThreeEightTwoSevenBCTTwoP` | n/a | flat-audit rate (%): all 7 entries same score, C, T2 stores, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatPooledCTThree` | 1.6 | flat-audit rate (%): all 7 entries same score, C, T3 stores, pooled |
| `\DetFlatPooledCTThreeLo` | 0.9 | flat-audit rate (%): all 7 entries same score, C, T3 stores, pooled, lower 95% CI bound |
| `\DetFlatPooledCTThreeHi` | 2.5 | flat-audit rate (%): all 7 entries same score, C, T3 stores, pooled, upper 95% CI bound |
| `\DetFlatPooledCTThreeCI` | [0.9, 2.5] | flat-audit rate (%): all 7 entries same score, C, T3 stores, pooled, 95% CI |
| `\DetFlatPooledCTThreeN` | 1{,}473 | flat-audit rate (%): all 7 entries same score, C, T3 stores, pooled, n |
| `\DetFlatPooledCTThreeP` | n/a | flat-audit rate (%): all 7 entries same score, C, T3 stores, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatDeepSeekVFourFlashCTThree` | 6.0 | flat-audit rate (%): all 7 entries same score, C, T3 stores, deepseek-v4-flash |
| `\DetFlatDeepSeekVFourFlashCTThreeLo` | 3.0 | flat-audit rate (%): all 7 entries same score, C, T3 stores, deepseek-v4-flash, lower 95% CI bound |
| `\DetFlatDeepSeekVFourFlashCTThreeHi` | 9.3 | flat-audit rate (%): all 7 entries same score, C, T3 stores, deepseek-v4-flash, upper 95% CI bound |
| `\DetFlatDeepSeekVFourFlashCTThreeCI` | [3.0, 9.3] | flat-audit rate (%): all 7 entries same score, C, T3 stores, deepseek-v4-flash, 95% CI |
| `\DetFlatDeepSeekVFourFlashCTThreeN` | 300 | flat-audit rate (%): all 7 entries same score, C, T3 stores, deepseek-v4-flash, n |
| `\DetFlatDeepSeekVFourFlashCTThreeP` | n/a | flat-audit rate (%): all 7 entries same score, C, T3 stores, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGemmaFourThreeOneBCTThree` | 0.7 | flat-audit rate (%): all 7 entries same score, C, T3 stores, gemma-4-31b-it |
| `\DetFlatGemmaFourThreeOneBCTThreeLo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T3 stores, gemma-4-31b-it, lower 95% CI bound |
| `\DetFlatGemmaFourThreeOneBCTThreeHi` | 1.8 | flat-audit rate (%): all 7 entries same score, C, T3 stores, gemma-4-31b-it, upper 95% CI bound |
| `\DetFlatGemmaFourThreeOneBCTThreeCI` | [0.0, 1.8] | flat-audit rate (%): all 7 entries same score, C, T3 stores, gemma-4-31b-it, 95% CI |
| `\DetFlatGemmaFourThreeOneBCTThreeN` | 276 | flat-audit rate (%): all 7 entries same score, C, T3 stores, gemma-4-31b-it, n |
| `\DetFlatGemmaFourThreeOneBCTThreeP` | n/a | flat-audit rate (%): all 7 entries same score, C, T3 stores, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveTwoCTThree` | 1.3 | flat-audit rate (%): all 7 entries same score, C, T3 stores, glm-5.2 |
| `\DetFlatGLMFiveTwoCTThreeLo` | 0.3 | flat-audit rate (%): all 7 entries same score, C, T3 stores, glm-5.2, lower 95% CI bound |
| `\DetFlatGLMFiveTwoCTThreeHi` | 2.7 | flat-audit rate (%): all 7 entries same score, C, T3 stores, glm-5.2, upper 95% CI bound |
| `\DetFlatGLMFiveTwoCTThreeCI` | [0.3, 2.7] | flat-audit rate (%): all 7 entries same score, C, T3 stores, glm-5.2, 95% CI |
| `\DetFlatGLMFiveTwoCTThreeN` | 300 | flat-audit rate (%): all 7 entries same score, C, T3 stores, glm-5.2, n |
| `\DetFlatGLMFiveTwoCTThreeP` | n/a | flat-audit rate (%): all 7 entries same score, C, T3 stores, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveThreeFlashCTThree` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T3 stores, glm-5.3-flash |
| `\DetFlatGLMFiveThreeFlashCTThreeLo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T3 stores, glm-5.3-flash, lower 95% CI bound |
| `\DetFlatGLMFiveThreeFlashCTThreeHi` | 1.2 | flat-audit rate (%): all 7 entries same score, C, T3 stores, glm-5.3-flash, upper 95% CI bound |
| `\DetFlatGLMFiveThreeFlashCTThreeCI` | [0.0, 1.2] | flat-audit rate (%): all 7 entries same score, C, T3 stores, glm-5.3-flash, 95% CI |
| `\DetFlatGLMFiveThreeFlashCTThreeN` | 300 | flat-audit rate (%): all 7 entries same score, C, T3 stores, glm-5.3-flash, n |
| `\DetFlatGLMFiveThreeFlashCTThreeP` | n/a | flat-audit rate (%): all 7 entries same score, C, T3 stores, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatQwenThreeEightTwoSevenBCTThree` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T3 stores, qwen3.8-27b |
| `\DetFlatQwenThreeEightTwoSevenBCTThreeLo` | 0.0 | flat-audit rate (%): all 7 entries same score, C, T3 stores, qwen3.8-27b, lower 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBCTThreeHi` | 1.2 | flat-audit rate (%): all 7 entries same score, C, T3 stores, qwen3.8-27b, upper 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBCTThreeCI` | [0.0, 1.2] | flat-audit rate (%): all 7 entries same score, C, T3 stores, qwen3.8-27b, 95% CI |
| `\DetFlatQwenThreeEightTwoSevenBCTThreeN` | 297 | flat-audit rate (%): all 7 entries same score, C, T3 stores, qwen3.8-27b, n |
| `\DetFlatQwenThreeEightTwoSevenBCTThreeP` | n/a | flat-audit rate (%): all 7 entries same score, C, T3 stores, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatPooledCClean` | 71.2 | flat-audit rate (%): all 7 entries same score, C, clean stores, pooled |
| `\DetFlatPooledCCleanLo` | 66.3 | flat-audit rate (%): all 7 entries same score, C, clean stores, pooled, lower 95% CI bound |
| `\DetFlatPooledCCleanHi` | 75.7 | flat-audit rate (%): all 7 entries same score, C, clean stores, pooled, upper 95% CI bound |
| `\DetFlatPooledCCleanCI` | [66.3, 75.7] | flat-audit rate (%): all 7 entries same score, C, clean stores, pooled, 95% CI |
| `\DetFlatPooledCCleanN` | 295 | flat-audit rate (%): all 7 entries same score, C, clean stores, pooled, n |
| `\DetFlatPooledCCleanP` | n/a | flat-audit rate (%): all 7 entries same score, C, clean stores, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatDeepSeekVFourFlashCClean` | 96.7 | flat-audit rate (%): all 7 entries same score, C, clean stores, deepseek-v4-flash |
| `\DetFlatDeepSeekVFourFlashCCleanLo` | 91.7 | flat-audit rate (%): all 7 entries same score, C, clean stores, deepseek-v4-flash, lower 95% CI bound |
| `\DetFlatDeepSeekVFourFlashCCleanHi` | 100.0 | flat-audit rate (%): all 7 entries same score, C, clean stores, deepseek-v4-flash, upper 95% CI bound |
| `\DetFlatDeepSeekVFourFlashCCleanCI` | [91.7, 100.0] | flat-audit rate (%): all 7 entries same score, C, clean stores, deepseek-v4-flash, 95% CI |
| `\DetFlatDeepSeekVFourFlashCCleanN` | 60 | flat-audit rate (%): all 7 entries same score, C, clean stores, deepseek-v4-flash, n |
| `\DetFlatDeepSeekVFourFlashCCleanP` | n/a | flat-audit rate (%): all 7 entries same score, C, clean stores, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGemmaFourThreeOneBCClean` | 98.2 | flat-audit rate (%): all 7 entries same score, C, clean stores, gemma-4-31b-it |
| `\DetFlatGemmaFourThreeOneBCCleanLo` | 94.6 | flat-audit rate (%): all 7 entries same score, C, clean stores, gemma-4-31b-it, lower 95% CI bound |
| `\DetFlatGemmaFourThreeOneBCCleanHi` | 100.0 | flat-audit rate (%): all 7 entries same score, C, clean stores, gemma-4-31b-it, upper 95% CI bound |
| `\DetFlatGemmaFourThreeOneBCCleanCI` | [94.6, 100.0] | flat-audit rate (%): all 7 entries same score, C, clean stores, gemma-4-31b-it, 95% CI |
| `\DetFlatGemmaFourThreeOneBCCleanN` | 56 | flat-audit rate (%): all 7 entries same score, C, clean stores, gemma-4-31b-it, n |
| `\DetFlatGemmaFourThreeOneBCCleanP` | n/a | flat-audit rate (%): all 7 entries same score, C, clean stores, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveTwoCClean` | 70.0 | flat-audit rate (%): all 7 entries same score, C, clean stores, glm-5.2 |
| `\DetFlatGLMFiveTwoCCleanLo` | 56.7 | flat-audit rate (%): all 7 entries same score, C, clean stores, glm-5.2, lower 95% CI bound |
| `\DetFlatGLMFiveTwoCCleanHi` | 81.7 | flat-audit rate (%): all 7 entries same score, C, clean stores, glm-5.2, upper 95% CI bound |
| `\DetFlatGLMFiveTwoCCleanCI` | [56.7, 81.7] | flat-audit rate (%): all 7 entries same score, C, clean stores, glm-5.2, 95% CI |
| `\DetFlatGLMFiveTwoCCleanN` | 60 | flat-audit rate (%): all 7 entries same score, C, clean stores, glm-5.2, n |
| `\DetFlatGLMFiveTwoCCleanP` | n/a | flat-audit rate (%): all 7 entries same score, C, clean stores, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveThreeFlashCClean` | 25.0 | flat-audit rate (%): all 7 entries same score, C, clean stores, glm-5.3-flash |
| `\DetFlatGLMFiveThreeFlashCCleanLo` | 15.0 | flat-audit rate (%): all 7 entries same score, C, clean stores, glm-5.3-flash, lower 95% CI bound |
| `\DetFlatGLMFiveThreeFlashCCleanHi` | 36.7 | flat-audit rate (%): all 7 entries same score, C, clean stores, glm-5.3-flash, upper 95% CI bound |
| `\DetFlatGLMFiveThreeFlashCCleanCI` | [15.0, 36.7] | flat-audit rate (%): all 7 entries same score, C, clean stores, glm-5.3-flash, 95% CI |
| `\DetFlatGLMFiveThreeFlashCCleanN` | 60 | flat-audit rate (%): all 7 entries same score, C, clean stores, glm-5.3-flash, n |
| `\DetFlatGLMFiveThreeFlashCCleanP` | n/a | flat-audit rate (%): all 7 entries same score, C, clean stores, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatQwenThreeEightTwoSevenBCClean` | 67.8 | flat-audit rate (%): all 7 entries same score, C, clean stores, qwen3.8-27b |
| `\DetFlatQwenThreeEightTwoSevenBCCleanLo` | 55.9 | flat-audit rate (%): all 7 entries same score, C, clean stores, qwen3.8-27b, lower 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBCCleanHi` | 79.7 | flat-audit rate (%): all 7 entries same score, C, clean stores, qwen3.8-27b, upper 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBCCleanCI` | [55.9, 79.7] | flat-audit rate (%): all 7 entries same score, C, clean stores, qwen3.8-27b, 95% CI |
| `\DetFlatQwenThreeEightTwoSevenBCCleanN` | 59 | flat-audit rate (%): all 7 entries same score, C, clean stores, qwen3.8-27b, n |
| `\DetFlatQwenThreeEightTwoSevenBCCleanP` | n/a | flat-audit rate (%): all 7 entries same score, C, clean stores, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatPooledVTZero` | 24.8 | flat-audit rate (%): all 7 entries same score, V, T0 stores, pooled |
| `\DetFlatPooledVTZeroLo` | 21.4 | flat-audit rate (%): all 7 entries same score, V, T0 stores, pooled, lower 95% CI bound |
| `\DetFlatPooledVTZeroHi` | 28.4 | flat-audit rate (%): all 7 entries same score, V, T0 stores, pooled, upper 95% CI bound |
| `\DetFlatPooledVTZeroCI` | [21.4, 28.4] | flat-audit rate (%): all 7 entries same score, V, T0 stores, pooled, 95% CI |
| `\DetFlatPooledVTZeroN` | 1{,}478 | flat-audit rate (%): all 7 entries same score, V, T0 stores, pooled, n |
| `\DetFlatPooledVTZeroP` | n/a | flat-audit rate (%): all 7 entries same score, V, T0 stores, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatDeepSeekVFourFlashVTZero` | 28.7 | flat-audit rate (%): all 7 entries same score, V, T0 stores, deepseek-v4-flash |
| `\DetFlatDeepSeekVFourFlashVTZeroLo` | 20.0 | flat-audit rate (%): all 7 entries same score, V, T0 stores, deepseek-v4-flash, lower 95% CI bound |
| `\DetFlatDeepSeekVFourFlashVTZeroHi` | 38.0 | flat-audit rate (%): all 7 entries same score, V, T0 stores, deepseek-v4-flash, upper 95% CI bound |
| `\DetFlatDeepSeekVFourFlashVTZeroCI` | [20.0, 38.0] | flat-audit rate (%): all 7 entries same score, V, T0 stores, deepseek-v4-flash, 95% CI |
| `\DetFlatDeepSeekVFourFlashVTZeroN` | 300 | flat-audit rate (%): all 7 entries same score, V, T0 stores, deepseek-v4-flash, n |
| `\DetFlatDeepSeekVFourFlashVTZeroP` | n/a | flat-audit rate (%): all 7 entries same score, V, T0 stores, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGemmaFourThreeOneBVTZero` | 52.1 | flat-audit rate (%): all 7 entries same score, V, T0 stores, gemma-4-31b-it |
| `\DetFlatGemmaFourThreeOneBVTZeroLo` | 45.4 | flat-audit rate (%): all 7 entries same score, V, T0 stores, gemma-4-31b-it, lower 95% CI bound |
| `\DetFlatGemmaFourThreeOneBVTZeroHi` | 58.9 | flat-audit rate (%): all 7 entries same score, V, T0 stores, gemma-4-31b-it, upper 95% CI bound |
| `\DetFlatGemmaFourThreeOneBVTZeroCI` | [45.4, 58.9] | flat-audit rate (%): all 7 entries same score, V, T0 stores, gemma-4-31b-it, 95% CI |
| `\DetFlatGemmaFourThreeOneBVTZeroN` | 280 | flat-audit rate (%): all 7 entries same score, V, T0 stores, gemma-4-31b-it, n |
| `\DetFlatGemmaFourThreeOneBVTZeroP` | n/a | flat-audit rate (%): all 7 entries same score, V, T0 stores, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveTwoVTZero` | 4.3 | flat-audit rate (%): all 7 entries same score, V, T0 stores, glm-5.2 |
| `\DetFlatGLMFiveTwoVTZeroLo` | 2.3 | flat-audit rate (%): all 7 entries same score, V, T0 stores, glm-5.2, lower 95% CI bound |
| `\DetFlatGLMFiveTwoVTZeroHi` | 6.7 | flat-audit rate (%): all 7 entries same score, V, T0 stores, glm-5.2, upper 95% CI bound |
| `\DetFlatGLMFiveTwoVTZeroCI` | [2.3, 6.7] | flat-audit rate (%): all 7 entries same score, V, T0 stores, glm-5.2, 95% CI |
| `\DetFlatGLMFiveTwoVTZeroN` | 300 | flat-audit rate (%): all 7 entries same score, V, T0 stores, glm-5.2, n |
| `\DetFlatGLMFiveTwoVTZeroP` | n/a | flat-audit rate (%): all 7 entries same score, V, T0 stores, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveThreeFlashVTZero` | 3.7 | flat-audit rate (%): all 7 entries same score, V, T0 stores, glm-5.3-flash |
| `\DetFlatGLMFiveThreeFlashVTZeroLo` | 1.7 | flat-audit rate (%): all 7 entries same score, V, T0 stores, glm-5.3-flash, lower 95% CI bound |
| `\DetFlatGLMFiveThreeFlashVTZeroHi` | 6.0 | flat-audit rate (%): all 7 entries same score, V, T0 stores, glm-5.3-flash, upper 95% CI bound |
| `\DetFlatGLMFiveThreeFlashVTZeroCI` | [1.7, 6.0] | flat-audit rate (%): all 7 entries same score, V, T0 stores, glm-5.3-flash, 95% CI |
| `\DetFlatGLMFiveThreeFlashVTZeroN` | 300 | flat-audit rate (%): all 7 entries same score, V, T0 stores, glm-5.3-flash, n |
| `\DetFlatGLMFiveThreeFlashVTZeroP` | n/a | flat-audit rate (%): all 7 entries same score, V, T0 stores, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatQwenThreeEightTwoSevenBVTZero` | 36.9 | flat-audit rate (%): all 7 entries same score, V, T0 stores, qwen3.8-27b |
| `\DetFlatQwenThreeEightTwoSevenBVTZeroLo` | 32.4 | flat-audit rate (%): all 7 entries same score, V, T0 stores, qwen3.8-27b, lower 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBVTZeroHi` | 42.0 | flat-audit rate (%): all 7 entries same score, V, T0 stores, qwen3.8-27b, upper 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBVTZeroCI` | [32.4, 42.0] | flat-audit rate (%): all 7 entries same score, V, T0 stores, qwen3.8-27b, 95% CI |
| `\DetFlatQwenThreeEightTwoSevenBVTZeroN` | 298 | flat-audit rate (%): all 7 entries same score, V, T0 stores, qwen3.8-27b, n |
| `\DetFlatQwenThreeEightTwoSevenBVTZeroP` | n/a | flat-audit rate (%): all 7 entries same score, V, T0 stores, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatPooledVTOne` | 43.2 | flat-audit rate (%): all 7 entries same score, V, T1 stores, pooled |
| `\DetFlatPooledVTOneLo` | 39.7 | flat-audit rate (%): all 7 entries same score, V, T1 stores, pooled, lower 95% CI bound |
| `\DetFlatPooledVTOneHi` | 47.0 | flat-audit rate (%): all 7 entries same score, V, T1 stores, pooled, upper 95% CI bound |
| `\DetFlatPooledVTOneCI` | [39.7, 47.0] | flat-audit rate (%): all 7 entries same score, V, T1 stores, pooled, 95% CI |
| `\DetFlatPooledVTOneN` | 1{,}455 | flat-audit rate (%): all 7 entries same score, V, T1 stores, pooled, n |
| `\DetFlatPooledVTOneP` | n/a | flat-audit rate (%): all 7 entries same score, V, T1 stores, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatDeepSeekVFourFlashVTOne` | 31.3 | flat-audit rate (%): all 7 entries same score, V, T1 stores, deepseek-v4-flash |
| `\DetFlatDeepSeekVFourFlashVTOneLo` | 20.5 | flat-audit rate (%): all 7 entries same score, V, T1 stores, deepseek-v4-flash, lower 95% CI bound |
| `\DetFlatDeepSeekVFourFlashVTOneHi` | 42.5 | flat-audit rate (%): all 7 entries same score, V, T1 stores, deepseek-v4-flash, upper 95% CI bound |
| `\DetFlatDeepSeekVFourFlashVTOneCI` | [20.5, 42.5] | flat-audit rate (%): all 7 entries same score, V, T1 stores, deepseek-v4-flash, 95% CI |
| `\DetFlatDeepSeekVFourFlashVTOneN` | 297 | flat-audit rate (%): all 7 entries same score, V, T1 stores, deepseek-v4-flash, n |
| `\DetFlatDeepSeekVFourFlashVTOneP` | n/a | flat-audit rate (%): all 7 entries same score, V, T1 stores, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGemmaFourThreeOneBVTOne` | 89.5 | flat-audit rate (%): all 7 entries same score, V, T1 stores, gemma-4-31b-it |
| `\DetFlatGemmaFourThreeOneBVTOneLo` | 85.6 | flat-audit rate (%): all 7 entries same score, V, T1 stores, gemma-4-31b-it, lower 95% CI bound |
| `\DetFlatGemmaFourThreeOneBVTOneHi` | 93.1 | flat-audit rate (%): all 7 entries same score, V, T1 stores, gemma-4-31b-it, upper 95% CI bound |
| `\DetFlatGemmaFourThreeOneBVTOneCI` | [85.6, 93.1] | flat-audit rate (%): all 7 entries same score, V, T1 stores, gemma-4-31b-it, 95% CI |
| `\DetFlatGemmaFourThreeOneBVTOneN` | 276 | flat-audit rate (%): all 7 entries same score, V, T1 stores, gemma-4-31b-it, n |
| `\DetFlatGemmaFourThreeOneBVTOneP` | n/a | flat-audit rate (%): all 7 entries same score, V, T1 stores, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveTwoVTOne` | 11.9 | flat-audit rate (%): all 7 entries same score, V, T1 stores, glm-5.2 |
| `\DetFlatGLMFiveTwoVTOneLo` | 7.4 | flat-audit rate (%): all 7 entries same score, V, T1 stores, glm-5.2, lower 95% CI bound |
| `\DetFlatGLMFiveTwoVTOneHi` | 16.7 | flat-audit rate (%): all 7 entries same score, V, T1 stores, glm-5.2, upper 95% CI bound |
| `\DetFlatGLMFiveTwoVTOneCI` | [7.4, 16.7] | flat-audit rate (%): all 7 entries same score, V, T1 stores, glm-5.2, 95% CI |
| `\DetFlatGLMFiveTwoVTOneN` | 293 | flat-audit rate (%): all 7 entries same score, V, T1 stores, glm-5.2, n |
| `\DetFlatGLMFiveTwoVTOneP` | n/a | flat-audit rate (%): all 7 entries same score, V, T1 stores, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveThreeFlashVTOne` | 7.1 | flat-audit rate (%): all 7 entries same score, V, T1 stores, glm-5.3-flash |
| `\DetFlatGLMFiveThreeFlashVTOneLo` | 3.7 | flat-audit rate (%): all 7 entries same score, V, T1 stores, glm-5.3-flash, lower 95% CI bound |
| `\DetFlatGLMFiveThreeFlashVTOneHi` | 11.2 | flat-audit rate (%): all 7 entries same score, V, T1 stores, glm-5.3-flash, upper 95% CI bound |
| `\DetFlatGLMFiveThreeFlashVTOneCI` | [3.7, 11.2] | flat-audit rate (%): all 7 entries same score, V, T1 stores, glm-5.3-flash, 95% CI |
| `\DetFlatGLMFiveThreeFlashVTOneN` | 296 | flat-audit rate (%): all 7 entries same score, V, T1 stores, glm-5.3-flash, n |
| `\DetFlatGLMFiveThreeFlashVTOneP` | n/a | flat-audit rate (%): all 7 entries same score, V, T1 stores, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatQwenThreeEightTwoSevenBVTOne` | 79.5 | flat-audit rate (%): all 7 entries same score, V, T1 stores, qwen3.8-27b |
| `\DetFlatQwenThreeEightTwoSevenBVTOneLo` | 75.3 | flat-audit rate (%): all 7 entries same score, V, T1 stores, qwen3.8-27b, lower 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBVTOneHi` | 83.7 | flat-audit rate (%): all 7 entries same score, V, T1 stores, qwen3.8-27b, upper 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBVTOneCI` | [75.3, 83.7] | flat-audit rate (%): all 7 entries same score, V, T1 stores, qwen3.8-27b, 95% CI |
| `\DetFlatQwenThreeEightTwoSevenBVTOneN` | 293 | flat-audit rate (%): all 7 entries same score, V, T1 stores, qwen3.8-27b, n |
| `\DetFlatQwenThreeEightTwoSevenBVTOneP` | n/a | flat-audit rate (%): all 7 entries same score, V, T1 stores, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatPooledVTTwo` | 43.3 | flat-audit rate (%): all 7 entries same score, V, T2 stores, pooled |
| `\DetFlatPooledVTTwoLo` | 39.9 | flat-audit rate (%): all 7 entries same score, V, T2 stores, pooled, lower 95% CI bound |
| `\DetFlatPooledVTTwoHi` | 47.0 | flat-audit rate (%): all 7 entries same score, V, T2 stores, pooled, upper 95% CI bound |
| `\DetFlatPooledVTTwoCI` | [39.9, 47.0] | flat-audit rate (%): all 7 entries same score, V, T2 stores, pooled, 95% CI |
| `\DetFlatPooledVTTwoN` | 1{,}458 | flat-audit rate (%): all 7 entries same score, V, T2 stores, pooled, n |
| `\DetFlatPooledVTTwoP` | n/a | flat-audit rate (%): all 7 entries same score, V, T2 stores, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatDeepSeekVFourFlashVTTwo` | 35.2 | flat-audit rate (%): all 7 entries same score, V, T2 stores, deepseek-v4-flash |
| `\DetFlatDeepSeekVFourFlashVTTwoLo` | 24.6 | flat-audit rate (%): all 7 entries same score, V, T2 stores, deepseek-v4-flash, lower 95% CI bound |
| `\DetFlatDeepSeekVFourFlashVTTwoHi` | 47.0 | flat-audit rate (%): all 7 entries same score, V, T2 stores, deepseek-v4-flash, upper 95% CI bound |
| `\DetFlatDeepSeekVFourFlashVTTwoCI` | [24.6, 47.0] | flat-audit rate (%): all 7 entries same score, V, T2 stores, deepseek-v4-flash, 95% CI |
| `\DetFlatDeepSeekVFourFlashVTTwoN` | 298 | flat-audit rate (%): all 7 entries same score, V, T2 stores, deepseek-v4-flash, n |
| `\DetFlatDeepSeekVFourFlashVTTwoP` | n/a | flat-audit rate (%): all 7 entries same score, V, T2 stores, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGemmaFourThreeOneBVTTwo` | 85.5 | flat-audit rate (%): all 7 entries same score, V, T2 stores, gemma-4-31b-it |
| `\DetFlatGemmaFourThreeOneBVTTwoLo` | 81.2 | flat-audit rate (%): all 7 entries same score, V, T2 stores, gemma-4-31b-it, lower 95% CI bound |
| `\DetFlatGemmaFourThreeOneBVTTwoHi` | 89.2 | flat-audit rate (%): all 7 entries same score, V, T2 stores, gemma-4-31b-it, upper 95% CI bound |
| `\DetFlatGemmaFourThreeOneBVTTwoCI` | [81.2, 89.2] | flat-audit rate (%): all 7 entries same score, V, T2 stores, gemma-4-31b-it, 95% CI |
| `\DetFlatGemmaFourThreeOneBVTTwoN` | 269 | flat-audit rate (%): all 7 entries same score, V, T2 stores, gemma-4-31b-it, n |
| `\DetFlatGemmaFourThreeOneBVTTwoP` | n/a | flat-audit rate (%): all 7 entries same score, V, T2 stores, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveTwoVTTwo` | 12.0 | flat-audit rate (%): all 7 entries same score, V, T2 stores, glm-5.2 |
| `\DetFlatGLMFiveTwoVTTwoLo` | 7.4 | flat-audit rate (%): all 7 entries same score, V, T2 stores, glm-5.2, lower 95% CI bound |
| `\DetFlatGLMFiveTwoVTTwoHi` | 17.4 | flat-audit rate (%): all 7 entries same score, V, T2 stores, glm-5.2, upper 95% CI bound |
| `\DetFlatGLMFiveTwoVTTwoCI` | [7.4, 17.4] | flat-audit rate (%): all 7 entries same score, V, T2 stores, glm-5.2, 95% CI |
| `\DetFlatGLMFiveTwoVTTwoN` | 299 | flat-audit rate (%): all 7 entries same score, V, T2 stores, glm-5.2, n |
| `\DetFlatGLMFiveTwoVTTwoP` | n/a | flat-audit rate (%): all 7 entries same score, V, T2 stores, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveThreeFlashVTTwo` | 7.4 | flat-audit rate (%): all 7 entries same score, V, T2 stores, glm-5.3-flash |
| `\DetFlatGLMFiveThreeFlashVTTwoLo` | 3.7 | flat-audit rate (%): all 7 entries same score, V, T2 stores, glm-5.3-flash, lower 95% CI bound |
| `\DetFlatGLMFiveThreeFlashVTTwoHi` | 11.7 | flat-audit rate (%): all 7 entries same score, V, T2 stores, glm-5.3-flash, upper 95% CI bound |
| `\DetFlatGLMFiveThreeFlashVTTwoCI` | [3.7, 11.7] | flat-audit rate (%): all 7 entries same score, V, T2 stores, glm-5.3-flash, 95% CI |
| `\DetFlatGLMFiveThreeFlashVTTwoN` | 299 | flat-audit rate (%): all 7 entries same score, V, T2 stores, glm-5.3-flash, n |
| `\DetFlatGLMFiveThreeFlashVTTwoP` | n/a | flat-audit rate (%): all 7 entries same score, V, T2 stores, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatQwenThreeEightTwoSevenBVTTwo` | 81.6 | flat-audit rate (%): all 7 entries same score, V, T2 stores, qwen3.8-27b |
| `\DetFlatQwenThreeEightTwoSevenBVTTwoLo` | 76.7 | flat-audit rate (%): all 7 entries same score, V, T2 stores, qwen3.8-27b, lower 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBVTTwoHi` | 86.3 | flat-audit rate (%): all 7 entries same score, V, T2 stores, qwen3.8-27b, upper 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBVTTwoCI` | [76.7, 86.3] | flat-audit rate (%): all 7 entries same score, V, T2 stores, qwen3.8-27b, 95% CI |
| `\DetFlatQwenThreeEightTwoSevenBVTTwoN` | 293 | flat-audit rate (%): all 7 entries same score, V, T2 stores, qwen3.8-27b, n |
| `\DetFlatQwenThreeEightTwoSevenBVTTwoP` | n/a | flat-audit rate (%): all 7 entries same score, V, T2 stores, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatPooledVTThree` | 44.4 | flat-audit rate (%): all 7 entries same score, V, T3 stores, pooled |
| `\DetFlatPooledVTThreeLo` | 40.8 | flat-audit rate (%): all 7 entries same score, V, T3 stores, pooled, lower 95% CI bound |
| `\DetFlatPooledVTThreeHi` | 48.4 | flat-audit rate (%): all 7 entries same score, V, T3 stores, pooled, upper 95% CI bound |
| `\DetFlatPooledVTThreeCI` | [40.8, 48.4] | flat-audit rate (%): all 7 entries same score, V, T3 stores, pooled, 95% CI |
| `\DetFlatPooledVTThreeN` | 1{,}472 | flat-audit rate (%): all 7 entries same score, V, T3 stores, pooled, n |
| `\DetFlatPooledVTThreeP` | n/a | flat-audit rate (%): all 7 entries same score, V, T3 stores, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatDeepSeekVFourFlashVTThree` | 33.3 | flat-audit rate (%): all 7 entries same score, V, T3 stores, deepseek-v4-flash |
| `\DetFlatDeepSeekVFourFlashVTThreeLo` | 22.7 | flat-audit rate (%): all 7 entries same score, V, T3 stores, deepseek-v4-flash, lower 95% CI bound |
| `\DetFlatDeepSeekVFourFlashVTThreeHi` | 44.0 | flat-audit rate (%): all 7 entries same score, V, T3 stores, deepseek-v4-flash, upper 95% CI bound |
| `\DetFlatDeepSeekVFourFlashVTThreeCI` | [22.7, 44.0] | flat-audit rate (%): all 7 entries same score, V, T3 stores, deepseek-v4-flash, 95% CI |
| `\DetFlatDeepSeekVFourFlashVTThreeN` | 300 | flat-audit rate (%): all 7 entries same score, V, T3 stores, deepseek-v4-flash, n |
| `\DetFlatDeepSeekVFourFlashVTThreeP` | n/a | flat-audit rate (%): all 7 entries same score, V, T3 stores, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGemmaFourThreeOneBVTThree` | 87.3 | flat-audit rate (%): all 7 entries same score, V, T3 stores, gemma-4-31b-it |
| `\DetFlatGemmaFourThreeOneBVTThreeLo` | 83.7 | flat-audit rate (%): all 7 entries same score, V, T3 stores, gemma-4-31b-it, lower 95% CI bound |
| `\DetFlatGemmaFourThreeOneBVTThreeHi` | 90.9 | flat-audit rate (%): all 7 entries same score, V, T3 stores, gemma-4-31b-it, upper 95% CI bound |
| `\DetFlatGemmaFourThreeOneBVTThreeCI` | [83.7, 90.9] | flat-audit rate (%): all 7 entries same score, V, T3 stores, gemma-4-31b-it, 95% CI |
| `\DetFlatGemmaFourThreeOneBVTThreeN` | 275 | flat-audit rate (%): all 7 entries same score, V, T3 stores, gemma-4-31b-it, n |
| `\DetFlatGemmaFourThreeOneBVTThreeP` | n/a | flat-audit rate (%): all 7 entries same score, V, T3 stores, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveTwoVTThree` | 12.0 | flat-audit rate (%): all 7 entries same score, V, T3 stores, glm-5.2 |
| `\DetFlatGLMFiveTwoVTThreeLo` | 7.3 | flat-audit rate (%): all 7 entries same score, V, T3 stores, glm-5.2, lower 95% CI bound |
| `\DetFlatGLMFiveTwoVTThreeHi` | 17.3 | flat-audit rate (%): all 7 entries same score, V, T3 stores, glm-5.2, upper 95% CI bound |
| `\DetFlatGLMFiveTwoVTThreeCI` | [7.3, 17.3] | flat-audit rate (%): all 7 entries same score, V, T3 stores, glm-5.2, 95% CI |
| `\DetFlatGLMFiveTwoVTThreeN` | 300 | flat-audit rate (%): all 7 entries same score, V, T3 stores, glm-5.2, n |
| `\DetFlatGLMFiveTwoVTThreeP` | n/a | flat-audit rate (%): all 7 entries same score, V, T3 stores, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveThreeFlashVTThree` | 8.7 | flat-audit rate (%): all 7 entries same score, V, T3 stores, glm-5.3-flash |
| `\DetFlatGLMFiveThreeFlashVTThreeLo` | 4.0 | flat-audit rate (%): all 7 entries same score, V, T3 stores, glm-5.3-flash, lower 95% CI bound |
| `\DetFlatGLMFiveThreeFlashVTThreeHi` | 13.7 | flat-audit rate (%): all 7 entries same score, V, T3 stores, glm-5.3-flash, upper 95% CI bound |
| `\DetFlatGLMFiveThreeFlashVTThreeCI` | [4.0, 13.7] | flat-audit rate (%): all 7 entries same score, V, T3 stores, glm-5.3-flash, 95% CI |
| `\DetFlatGLMFiveThreeFlashVTThreeN` | 300 | flat-audit rate (%): all 7 entries same score, V, T3 stores, glm-5.3-flash, n |
| `\DetFlatGLMFiveThreeFlashVTThreeP` | n/a | flat-audit rate (%): all 7 entries same score, V, T3 stores, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatQwenThreeEightTwoSevenBVTThree` | 84.8 | flat-audit rate (%): all 7 entries same score, V, T3 stores, qwen3.8-27b |
| `\DetFlatQwenThreeEightTwoSevenBVTThreeLo` | 79.7 | flat-audit rate (%): all 7 entries same score, V, T3 stores, qwen3.8-27b, lower 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBVTThreeHi` | 89.9 | flat-audit rate (%): all 7 entries same score, V, T3 stores, qwen3.8-27b, upper 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBVTThreeCI` | [79.7, 89.9] | flat-audit rate (%): all 7 entries same score, V, T3 stores, qwen3.8-27b, 95% CI |
| `\DetFlatQwenThreeEightTwoSevenBVTThreeN` | 297 | flat-audit rate (%): all 7 entries same score, V, T3 stores, qwen3.8-27b, n |
| `\DetFlatQwenThreeEightTwoSevenBVTThreeP` | n/a | flat-audit rate (%): all 7 entries same score, V, T3 stores, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatPooledVClean` | 51.9 | flat-audit rate (%): all 7 entries same score, V, clean stores, pooled |
| `\DetFlatPooledVCleanLo` | 46.7 | flat-audit rate (%): all 7 entries same score, V, clean stores, pooled, lower 95% CI bound |
| `\DetFlatPooledVCleanHi` | 57.1 | flat-audit rate (%): all 7 entries same score, V, clean stores, pooled, upper 95% CI bound |
| `\DetFlatPooledVCleanCI` | [46.7, 57.1] | flat-audit rate (%): all 7 entries same score, V, clean stores, pooled, 95% CI |
| `\DetFlatPooledVCleanN` | 295 | flat-audit rate (%): all 7 entries same score, V, clean stores, pooled, n |
| `\DetFlatPooledVCleanP` | n/a | flat-audit rate (%): all 7 entries same score, V, clean stores, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatDeepSeekVFourFlashVClean` | 36.7 | flat-audit rate (%): all 7 entries same score, V, clean stores, deepseek-v4-flash |
| `\DetFlatDeepSeekVFourFlashVCleanLo` | 25.0 | flat-audit rate (%): all 7 entries same score, V, clean stores, deepseek-v4-flash, lower 95% CI bound |
| `\DetFlatDeepSeekVFourFlashVCleanHi` | 48.3 | flat-audit rate (%): all 7 entries same score, V, clean stores, deepseek-v4-flash, upper 95% CI bound |
| `\DetFlatDeepSeekVFourFlashVCleanCI` | [25.0, 48.3] | flat-audit rate (%): all 7 entries same score, V, clean stores, deepseek-v4-flash, 95% CI |
| `\DetFlatDeepSeekVFourFlashVCleanN` | 60 | flat-audit rate (%): all 7 entries same score, V, clean stores, deepseek-v4-flash, n |
| `\DetFlatDeepSeekVFourFlashVCleanP` | n/a | flat-audit rate (%): all 7 entries same score, V, clean stores, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGemmaFourThreeOneBVClean` | 98.2 | flat-audit rate (%): all 7 entries same score, V, clean stores, gemma-4-31b-it |
| `\DetFlatGemmaFourThreeOneBVCleanLo` | 92.7 | flat-audit rate (%): all 7 entries same score, V, clean stores, gemma-4-31b-it, lower 95% CI bound |
| `\DetFlatGemmaFourThreeOneBVCleanHi` | 100.0 | flat-audit rate (%): all 7 entries same score, V, clean stores, gemma-4-31b-it, upper 95% CI bound |
| `\DetFlatGemmaFourThreeOneBVCleanCI` | [92.7, 100.0] | flat-audit rate (%): all 7 entries same score, V, clean stores, gemma-4-31b-it, 95% CI |
| `\DetFlatGemmaFourThreeOneBVCleanN` | 55 | flat-audit rate (%): all 7 entries same score, V, clean stores, gemma-4-31b-it, n |
| `\DetFlatGemmaFourThreeOneBVCleanP` | n/a | flat-audit rate (%): all 7 entries same score, V, clean stores, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveTwoVClean` | 20.0 | flat-audit rate (%): all 7 entries same score, V, clean stores, glm-5.2 |
| `\DetFlatGLMFiveTwoVCleanLo` | 10.0 | flat-audit rate (%): all 7 entries same score, V, clean stores, glm-5.2, lower 95% CI bound |
| `\DetFlatGLMFiveTwoVCleanHi` | 30.0 | flat-audit rate (%): all 7 entries same score, V, clean stores, glm-5.2, upper 95% CI bound |
| `\DetFlatGLMFiveTwoVCleanCI` | [10.0, 30.0] | flat-audit rate (%): all 7 entries same score, V, clean stores, glm-5.2, 95% CI |
| `\DetFlatGLMFiveTwoVCleanN` | 60 | flat-audit rate (%): all 7 entries same score, V, clean stores, glm-5.2, n |
| `\DetFlatGLMFiveTwoVCleanP` | n/a | flat-audit rate (%): all 7 entries same score, V, clean stores, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatGLMFiveThreeFlashVClean` | 13.3 | flat-audit rate (%): all 7 entries same score, V, clean stores, glm-5.3-flash |
| `\DetFlatGLMFiveThreeFlashVCleanLo` | 5.0 | flat-audit rate (%): all 7 entries same score, V, clean stores, glm-5.3-flash, lower 95% CI bound |
| `\DetFlatGLMFiveThreeFlashVCleanHi` | 21.7 | flat-audit rate (%): all 7 entries same score, V, clean stores, glm-5.3-flash, upper 95% CI bound |
| `\DetFlatGLMFiveThreeFlashVCleanCI` | [5.0, 21.7] | flat-audit rate (%): all 7 entries same score, V, clean stores, glm-5.3-flash, 95% CI |
| `\DetFlatGLMFiveThreeFlashVCleanN` | 60 | flat-audit rate (%): all 7 entries same score, V, clean stores, glm-5.3-flash, n |
| `\DetFlatGLMFiveThreeFlashVCleanP` | n/a | flat-audit rate (%): all 7 entries same score, V, clean stores, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetFlatQwenThreeEightTwoSevenBVClean` | 95.0 | flat-audit rate (%): all 7 entries same score, V, clean stores, qwen3.8-27b |
| `\DetFlatQwenThreeEightTwoSevenBVCleanLo` | 88.3 | flat-audit rate (%): all 7 entries same score, V, clean stores, qwen3.8-27b, lower 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBVCleanHi` | 100.0 | flat-audit rate (%): all 7 entries same score, V, clean stores, qwen3.8-27b, upper 95% CI bound |
| `\DetFlatQwenThreeEightTwoSevenBVCleanCI` | [88.3, 100.0] | flat-audit rate (%): all 7 entries same score, V, clean stores, qwen3.8-27b, 95% CI |
| `\DetFlatQwenThreeEightTwoSevenBVCleanN` | 60 | flat-audit rate (%): all 7 entries same score, V, clean stores, qwen3.8-27b, n |
| `\DetFlatQwenThreeEightTwoSevenBVCleanP` | n/a | flat-audit rate (%): all 7 entries same score, V, clean stores, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledCTZeroStrict` | 96.8 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, pooled |
| `\DetRankPooledCTZeroStrictLo` | 95.4 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, pooled, lower 95% CI bound |
| `\DetRankPooledCTZeroStrictHi` | 98.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, pooled, upper 95% CI bound |
| `\DetRankPooledCTZeroStrictCI` | [95.4, 98.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, pooled, 95% CI |
| `\DetRankPooledCTZeroStrictN` | 1{,}478 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, pooled, n |
| `\DetRankPooledCTZeroStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledCTZeroTiesIncl` | 99.8 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, pooled |
| `\DetRankPooledCTZeroTiesInclLo` | 99.6 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, pooled, lower 95% CI bound |
| `\DetRankPooledCTZeroTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, pooled, upper 95% CI bound |
| `\DetRankPooledCTZeroTiesInclCI` | [99.6, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T0, pooled, 95% CI |
| `\DetRankPooledCTZeroTiesInclN` | 1{,}478 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, pooled, n |
| `\DetRankPooledCTZeroTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T0, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashCTZeroStrict` | 92.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashCTZeroStrictLo` | 89.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTZeroStrictHi` | 95.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTZeroStrictCI` | [89.0, 95.3] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashCTZeroStrictN` | 300 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashCTZeroStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashCTZeroTiesIncl` | 99.3 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashCTZeroTiesInclLo` | 98.3 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTZeroTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTZeroTiesInclCI` | [98.3, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T0, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashCTZeroTiesInclN` | 300 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashCTZeroTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBCTZeroStrict` | 98.2 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBCTZeroStrictLo` | 96.1 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTZeroStrictHi` | 99.6 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTZeroStrictCI` | [96.1, 99.6] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBCTZeroStrictN` | 278 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBCTZeroStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBCTZeroTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBCTZeroTiesInclLo` | 98.7 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTZeroTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTZeroTiesInclCI` | [98.7, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T0, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBCTZeroTiesInclN` | 278 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBCTZeroTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoCTZeroStrict` | 99.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, glm-5.2 |
| `\DetRankGLMFiveTwoCTZeroStrictLo` | 99.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, glm-5.2, lower 95% CI bound |
| `\DetRankGLMFiveTwoCTZeroStrictHi` | 100.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, glm-5.2, upper 95% CI bound |
| `\DetRankGLMFiveTwoCTZeroStrictCI` | [99.0, 100.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, glm-5.2, 95% CI |
| `\DetRankGLMFiveTwoCTZeroStrictN` | 300 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, glm-5.2, n |
| `\DetRankGLMFiveTwoCTZeroStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoCTZeroTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, glm-5.2 |
| `\DetRankGLMFiveTwoCTZeroTiesInclLo` | 98.8 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, glm-5.2, lower 95% CI bound |
| `\DetRankGLMFiveTwoCTZeroTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, glm-5.2, upper 95% CI bound |
| `\DetRankGLMFiveTwoCTZeroTiesInclCI` | [98.8, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T0, glm-5.2, 95% CI |
| `\DetRankGLMFiveTwoCTZeroTiesInclN` | 300 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, glm-5.2, n |
| `\DetRankGLMFiveTwoCTZeroTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashCTZeroStrict` | 99.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, glm-5.3-flash |
| `\DetRankGLMFiveThreeFlashCTZeroStrictLo` | 98.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, glm-5.3-flash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTZeroStrictHi` | 100.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, glm-5.3-flash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTZeroStrictCI` | [98.3, 100.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, glm-5.3-flash, 95% CI |
| `\DetRankGLMFiveThreeFlashCTZeroStrictN` | 300 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, glm-5.3-flash, n |
| `\DetRankGLMFiveThreeFlashCTZeroStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashCTZeroTiesIncl` | 99.7 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, glm-5.3-flash |
| `\DetRankGLMFiveThreeFlashCTZeroTiesInclLo` | 99.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, glm-5.3-flash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTZeroTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, glm-5.3-flash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTZeroTiesInclCI` | [99.0, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T0, glm-5.3-flash, 95% CI |
| `\DetRankGLMFiveThreeFlashCTZeroTiesInclN` | 300 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, glm-5.3-flash, n |
| `\DetRankGLMFiveThreeFlashCTZeroTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBCTZeroStrict` | 94.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, qwen3.8-27b |
| `\DetRankQwenThreeEightTwoSevenBCTZeroStrictLo` | 90.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, qwen3.8-27b, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTZeroStrictHi` | 98.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, qwen3.8-27b, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTZeroStrictCI` | [90.3, 98.3] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, qwen3.8-27b, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBCTZeroStrictN` | 300 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, qwen3.8-27b, n |
| `\DetRankQwenThreeEightTwoSevenBCTZeroStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBCTZeroTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, qwen3.8-27b |
| `\DetRankQwenThreeEightTwoSevenBCTZeroTiesInclLo` | 98.8 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, qwen3.8-27b, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTZeroTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, qwen3.8-27b, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTZeroTiesInclCI` | [98.8, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T0, qwen3.8-27b, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBCTZeroTiesInclN` | 300 | % attacked stores where the forged entry is most suspicious incl. ties, C T0, qwen3.8-27b, n |
| `\DetRankQwenThreeEightTwoSevenBCTZeroTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledCTOneStrict` | 96.2 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, pooled |
| `\DetRankPooledCTOneStrictLo` | 94.8 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, pooled, lower 95% CI bound |
| `\DetRankPooledCTOneStrictHi` | 97.5 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, pooled, upper 95% CI bound |
| `\DetRankPooledCTOneStrictCI` | [94.8, 97.5] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, pooled, 95% CI |
| `\DetRankPooledCTOneStrictN` | 1{,}456 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, pooled, n |
| `\DetRankPooledCTOneStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledCTOneTiesIncl` | 99.5 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, pooled |
| `\DetRankPooledCTOneTiesInclLo` | 98.9 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, pooled, lower 95% CI bound |
| `\DetRankPooledCTOneTiesInclHi` | 99.9 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, pooled, upper 95% CI bound |
| `\DetRankPooledCTOneTiesInclCI` | [98.9, 99.9] | % attacked stores where the forged entry is most suspicious incl. ties, C T1, pooled, 95% CI |
| `\DetRankPooledCTOneTiesInclN` | 1{,}456 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, pooled, n |
| `\DetRankPooledCTOneTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashCTOneStrict` | 90.9 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashCTOneStrictLo` | 86.9 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTOneStrictHi` | 94.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTOneStrictCI` | [86.9, 94.3] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashCTOneStrictN` | 297 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashCTOneStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashCTOneTiesIncl` | 98.3 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashCTOneTiesInclLo` | 96.3 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTOneTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTOneTiesInclCI` | [96.3, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T1, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashCTOneTiesInclN` | 297 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashCTOneTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBCTOneStrict` | 98.2 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBCTOneStrictLo` | 96.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTOneStrictHi` | 99.6 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTOneStrictCI` | [96.7, 99.6] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBCTOneStrictN` | 277 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBCTOneStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBCTOneTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBCTOneTiesInclLo` | 98.7 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTOneTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTOneTiesInclCI` | [98.7, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T1, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBCTOneTiesInclN` | 277 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBCTOneTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoCTOneStrict` | 98.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, glm-5.2 |
| `\DetRankGLMFiveTwoCTOneStrictLo` | 96.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, glm-5.2, lower 95% CI bound |
| `\DetRankGLMFiveTwoCTOneStrictHi` | 99.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, glm-5.2, upper 95% CI bound |
| `\DetRankGLMFiveTwoCTOneStrictCI` | [96.3, 99.3] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, glm-5.2, 95% CI |
| `\DetRankGLMFiveTwoCTOneStrictN` | 293 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, glm-5.2, n |
| `\DetRankGLMFiveTwoCTOneStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoCTOneTiesIncl` | 99.3 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, glm-5.2 |
| `\DetRankGLMFiveTwoCTOneTiesInclLo` | 98.3 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, glm-5.2, lower 95% CI bound |
| `\DetRankGLMFiveTwoCTOneTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, glm-5.2, upper 95% CI bound |
| `\DetRankGLMFiveTwoCTOneTiesInclCI` | [98.3, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T1, glm-5.2, 95% CI |
| `\DetRankGLMFiveTwoCTOneTiesInclN` | 293 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, glm-5.2, n |
| `\DetRankGLMFiveTwoCTOneTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashCTOneStrict` | 99.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, glm-5.3-flash |
| `\DetRankGLMFiveThreeFlashCTOneStrictLo` | 99.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, glm-5.3-flash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTOneStrictHi` | 100.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, glm-5.3-flash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTOneStrictCI` | [99.0, 100.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, glm-5.3-flash, 95% CI |
| `\DetRankGLMFiveThreeFlashCTOneStrictN` | 296 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, glm-5.3-flash, n |
| `\DetRankGLMFiveThreeFlashCTOneStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashCTOneTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, glm-5.3-flash |
| `\DetRankGLMFiveThreeFlashCTOneTiesInclLo` | 98.8 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, glm-5.3-flash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTOneTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, glm-5.3-flash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTOneTiesInclCI` | [98.8, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T1, glm-5.3-flash, 95% CI |
| `\DetRankGLMFiveThreeFlashCTOneTiesInclN` | 296 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, glm-5.3-flash, n |
| `\DetRankGLMFiveThreeFlashCTOneTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBCTOneStrict` | 94.5 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, qwen3.8-27b |
| `\DetRankQwenThreeEightTwoSevenBCTOneStrictLo` | 89.9 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, qwen3.8-27b, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTOneStrictHi` | 98.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, qwen3.8-27b, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTOneStrictCI` | [89.9, 98.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, qwen3.8-27b, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBCTOneStrictN` | 293 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, qwen3.8-27b, n |
| `\DetRankQwenThreeEightTwoSevenBCTOneStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBCTOneTiesIncl` | 99.7 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, qwen3.8-27b |
| `\DetRankQwenThreeEightTwoSevenBCTOneTiesInclLo` | 99.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, qwen3.8-27b, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTOneTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, qwen3.8-27b, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTOneTiesInclCI` | [99.0, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T1, qwen3.8-27b, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBCTOneTiesInclN` | 293 | % attacked stores where the forged entry is most suspicious incl. ties, C T1, qwen3.8-27b, n |
| `\DetRankQwenThreeEightTwoSevenBCTOneTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledCTTwoStrict` | 96.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, pooled |
| `\DetRankPooledCTTwoStrictLo` | 95.5 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, pooled, lower 95% CI bound |
| `\DetRankPooledCTTwoStrictHi` | 97.8 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, pooled, upper 95% CI bound |
| `\DetRankPooledCTTwoStrictCI` | [95.5, 97.8] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, pooled, 95% CI |
| `\DetRankPooledCTTwoStrictN` | 1{,}458 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, pooled, n |
| `\DetRankPooledCTTwoStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledCTTwoTiesIncl` | 99.7 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, pooled |
| `\DetRankPooledCTTwoTiesInclLo` | 99.4 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, pooled, lower 95% CI bound |
| `\DetRankPooledCTTwoTiesInclHi` | 99.9 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, pooled, upper 95% CI bound |
| `\DetRankPooledCTTwoTiesInclCI` | [99.4, 99.9] | % attacked stores where the forged entry is most suspicious incl. ties, C T2, pooled, 95% CI |
| `\DetRankPooledCTTwoTiesInclN` | 1{,}458 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, pooled, n |
| `\DetRankPooledCTTwoTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashCTTwoStrict` | 91.9 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashCTTwoStrictLo` | 88.9 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTTwoStrictHi` | 95.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTTwoStrictCI` | [88.9, 95.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashCTTwoStrictN` | 298 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashCTTwoStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashCTTwoTiesIncl` | 98.7 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashCTTwoTiesInclLo` | 97.3 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTTwoTiesInclHi` | 99.7 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTTwoTiesInclCI` | [97.3, 99.7] | % attacked stores where the forged entry is most suspicious incl. ties, C T2, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashCTTwoTiesInclN` | 298 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashCTTwoTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBCTTwoStrict` | 97.8 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBCTTwoStrictLo` | 95.6 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTTwoStrictHi` | 99.6 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTTwoStrictCI` | [95.6, 99.6] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBCTTwoStrictN` | 269 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBCTTwoStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBCTTwoTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBCTTwoTiesInclLo` | 98.6 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTTwoTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTTwoTiesInclCI` | [98.6, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T2, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBCTTwoTiesInclN` | 269 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBCTTwoTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoCTTwoStrict` | 98.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, glm-5.2 |
| `\DetRankGLMFiveTwoCTTwoStrictLo` | 96.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, glm-5.2, lower 95% CI bound |
| `\DetRankGLMFiveTwoCTTwoStrictHi` | 99.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, glm-5.2, upper 95% CI bound |
| `\DetRankGLMFiveTwoCTTwoStrictCI` | [96.0, 99.7] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, glm-5.2, 95% CI |
| `\DetRankGLMFiveTwoCTTwoStrictN` | 299 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, glm-5.2, n |
| `\DetRankGLMFiveTwoCTTwoStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoCTTwoTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, glm-5.2 |
| `\DetRankGLMFiveTwoCTTwoTiesInclLo` | 98.8 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, glm-5.2, lower 95% CI bound |
| `\DetRankGLMFiveTwoCTTwoTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, glm-5.2, upper 95% CI bound |
| `\DetRankGLMFiveTwoCTTwoTiesInclCI` | [98.8, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T2, glm-5.2, 95% CI |
| `\DetRankGLMFiveTwoCTTwoTiesInclN` | 299 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, glm-5.2, n |
| `\DetRankGLMFiveTwoCTTwoTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashCTTwoStrict` | 99.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, glm-5.3-flash |
| `\DetRankGLMFiveThreeFlashCTTwoStrictLo` | 99.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, glm-5.3-flash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTTwoStrictHi` | 100.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, glm-5.3-flash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTTwoStrictCI` | [99.0, 100.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, glm-5.3-flash, 95% CI |
| `\DetRankGLMFiveThreeFlashCTTwoStrictN` | 299 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, glm-5.3-flash, n |
| `\DetRankGLMFiveThreeFlashCTTwoStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashCTTwoTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, glm-5.3-flash |
| `\DetRankGLMFiveThreeFlashCTTwoTiesInclLo` | 98.8 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, glm-5.3-flash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTTwoTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, glm-5.3-flash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTTwoTiesInclCI` | [98.8, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T2, glm-5.3-flash, 95% CI |
| `\DetRankGLMFiveThreeFlashCTTwoTiesInclN` | 299 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, glm-5.3-flash, n |
| `\DetRankGLMFiveThreeFlashCTTwoTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBCTTwoStrict` | 96.2 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, qwen3.8-27b |
| `\DetRankQwenThreeEightTwoSevenBCTTwoStrictLo` | 92.5 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, qwen3.8-27b, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTTwoStrictHi` | 99.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, qwen3.8-27b, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTTwoStrictCI` | [92.5, 99.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, qwen3.8-27b, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBCTTwoStrictN` | 293 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, qwen3.8-27b, n |
| `\DetRankQwenThreeEightTwoSevenBCTTwoStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBCTTwoTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, qwen3.8-27b |
| `\DetRankQwenThreeEightTwoSevenBCTTwoTiesInclLo` | 98.7 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, qwen3.8-27b, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTTwoTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, qwen3.8-27b, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTTwoTiesInclCI` | [98.7, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T2, qwen3.8-27b, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBCTTwoTiesInclN` | 293 | % attacked stores where the forged entry is most suspicious incl. ties, C T2, qwen3.8-27b, n |
| `\DetRankQwenThreeEightTwoSevenBCTTwoTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledCTThreeStrict` | 96.4 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, pooled |
| `\DetRankPooledCTThreeStrictLo` | 94.8 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, pooled, lower 95% CI bound |
| `\DetRankPooledCTThreeStrictHi` | 97.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, pooled, upper 95% CI bound |
| `\DetRankPooledCTThreeStrictCI` | [94.8, 97.7] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, pooled, 95% CI |
| `\DetRankPooledCTThreeStrictN` | 1{,}473 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, pooled, n |
| `\DetRankPooledCTThreeStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledCTThreeTiesIncl` | 99.7 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, pooled |
| `\DetRankPooledCTThreeTiesInclLo` | 99.3 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, pooled, lower 95% CI bound |
| `\DetRankPooledCTThreeTiesInclHi` | 99.9 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, pooled, upper 95% CI bound |
| `\DetRankPooledCTThreeTiesInclCI` | [99.3, 99.9] | % attacked stores where the forged entry is most suspicious incl. ties, C T3, pooled, 95% CI |
| `\DetRankPooledCTThreeTiesInclN` | 1{,}473 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, pooled, n |
| `\DetRankPooledCTThreeTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashCTThreeStrict` | 92.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashCTThreeStrictLo` | 88.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTThreeStrictHi` | 95.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTThreeStrictCI` | [88.0, 95.7] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashCTThreeStrictN` | 300 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashCTThreeStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashCTThreeTiesIncl` | 98.7 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashCTThreeTiesInclLo` | 97.3 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTThreeTiesInclHi` | 99.7 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashCTThreeTiesInclCI` | [97.3, 99.7] | % attacked stores where the forged entry is most suspicious incl. ties, C T3, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashCTThreeTiesInclN` | 300 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashCTThreeTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBCTThreeStrict` | 97.8 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBCTThreeStrictLo` | 95.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTThreeStrictHi` | 99.6 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTThreeStrictCI` | [95.3, 99.6] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBCTThreeStrictN` | 276 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBCTThreeStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBCTThreeTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBCTThreeTiesInclLo` | 98.7 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTThreeTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBCTThreeTiesInclCI` | [98.7, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T3, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBCTThreeTiesInclN` | 276 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBCTThreeTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoCTThreeStrict` | 98.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, glm-5.2 |
| `\DetRankGLMFiveTwoCTThreeStrictLo` | 96.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, glm-5.2, lower 95% CI bound |
| `\DetRankGLMFiveTwoCTThreeStrictHi` | 99.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, glm-5.2, upper 95% CI bound |
| `\DetRankGLMFiveTwoCTThreeStrictCI` | [96.3, 99.3] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, glm-5.2, 95% CI |
| `\DetRankGLMFiveTwoCTThreeStrictN` | 300 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, glm-5.2, n |
| `\DetRankGLMFiveTwoCTThreeStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoCTThreeTiesIncl` | 99.7 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, glm-5.2 |
| `\DetRankGLMFiveTwoCTThreeTiesInclLo` | 99.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, glm-5.2, lower 95% CI bound |
| `\DetRankGLMFiveTwoCTThreeTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, glm-5.2, upper 95% CI bound |
| `\DetRankGLMFiveTwoCTThreeTiesInclCI` | [99.0, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T3, glm-5.2, 95% CI |
| `\DetRankGLMFiveTwoCTThreeTiesInclN` | 300 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, glm-5.2, n |
| `\DetRankGLMFiveTwoCTThreeTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashCTThreeStrict` | 99.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, glm-5.3-flash |
| `\DetRankGLMFiveThreeFlashCTThreeStrictLo` | 99.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, glm-5.3-flash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTThreeStrictHi` | 100.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, glm-5.3-flash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTThreeStrictCI` | [99.0, 100.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, glm-5.3-flash, 95% CI |
| `\DetRankGLMFiveThreeFlashCTThreeStrictN` | 300 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, glm-5.3-flash, n |
| `\DetRankGLMFiveThreeFlashCTThreeStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashCTThreeTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, glm-5.3-flash |
| `\DetRankGLMFiveThreeFlashCTThreeTiesInclLo` | 98.8 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, glm-5.3-flash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTThreeTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, glm-5.3-flash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashCTThreeTiesInclCI` | [98.8, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T3, glm-5.3-flash, 95% CI |
| `\DetRankGLMFiveThreeFlashCTThreeTiesInclN` | 300 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, glm-5.3-flash, n |
| `\DetRankGLMFiveThreeFlashCTThreeTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBCTThreeStrict` | 94.6 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, qwen3.8-27b |
| `\DetRankQwenThreeEightTwoSevenBCTThreeStrictLo` | 89.9 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, qwen3.8-27b, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTThreeStrictHi` | 98.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, qwen3.8-27b, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTThreeStrictCI` | [89.9, 98.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, qwen3.8-27b, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBCTThreeStrictN` | 297 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, qwen3.8-27b, n |
| `\DetRankQwenThreeEightTwoSevenBCTThreeStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), C T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBCTThreeTiesIncl` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, qwen3.8-27b |
| `\DetRankQwenThreeEightTwoSevenBCTThreeTiesInclLo` | 98.8 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, qwen3.8-27b, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTThreeTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, qwen3.8-27b, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBCTThreeTiesInclCI` | [98.8, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, C T3, qwen3.8-27b, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBCTThreeTiesInclN` | 297 | % attacked stores where the forged entry is most suspicious incl. ties, C T3, qwen3.8-27b, n |
| `\DetRankQwenThreeEightTwoSevenBCTThreeTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, C T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledVTZeroStrict` | 63.8 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, pooled |
| `\DetRankPooledVTZeroStrictLo` | 60.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, pooled, lower 95% CI bound |
| `\DetRankPooledVTZeroStrictHi` | 66.9 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, pooled, upper 95% CI bound |
| `\DetRankPooledVTZeroStrictCI` | [60.7, 66.9] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, pooled, 95% CI |
| `\DetRankPooledVTZeroStrictN` | 1{,}478 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, pooled, n |
| `\DetRankPooledVTZeroStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledVTZeroTiesIncl` | 89.2 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, pooled |
| `\DetRankPooledVTZeroTiesInclLo` | 87.5 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, pooled, lower 95% CI bound |
| `\DetRankPooledVTZeroTiesInclHi` | 90.7 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, pooled, upper 95% CI bound |
| `\DetRankPooledVTZeroTiesInclCI` | [87.5, 90.7] | % attacked stores where the forged entry is most suspicious incl. ties, V T0, pooled, 95% CI |
| `\DetRankPooledVTZeroTiesInclN` | 1{,}478 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, pooled, n |
| `\DetRankPooledVTZeroTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T0, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashVTZeroStrict` | 53.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashVTZeroStrictLo` | 46.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTZeroStrictHi` | 60.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTZeroStrictCI` | [46.3, 60.3] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashVTZeroStrictN` | 300 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashVTZeroStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashVTZeroTiesIncl` | 82.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashVTZeroTiesInclLo` | 77.3 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTZeroTiesInclHi` | 86.3 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTZeroTiesInclCI` | [77.3, 86.3] | % attacked stores where the forged entry is most suspicious incl. ties, V T0, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashVTZeroTiesInclN` | 300 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashVTZeroTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBVTZeroStrict` | 44.6 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBVTZeroStrictLo` | 37.9 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTZeroStrictHi` | 50.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTZeroStrictCI` | [37.9, 50.7] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBVTZeroStrictN` | 280 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBVTZeroStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBVTZeroTiesIncl` | 98.6 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBVTZeroTiesInclLo` | 96.1 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTZeroTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTZeroTiesInclCI` | [96.1, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, V T0, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBVTZeroTiesInclN` | 280 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBVTZeroTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoVTZeroStrict` | 77.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, glm-5.2 |
| `\DetRankGLMFiveTwoVTZeroStrictLo` | 74.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, glm-5.2, lower 95% CI bound |
| `\DetRankGLMFiveTwoVTZeroStrictHi` | 80.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, glm-5.2, upper 95% CI bound |
| `\DetRankGLMFiveTwoVTZeroStrictCI` | [74.0, 80.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, glm-5.2, 95% CI |
| `\DetRankGLMFiveTwoVTZeroStrictN` | 300 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, glm-5.2, n |
| `\DetRankGLMFiveTwoVTZeroStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoVTZeroTiesIncl` | 82.3 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, glm-5.2 |
| `\DetRankGLMFiveTwoVTZeroTiesInclLo` | 79.7 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, glm-5.2, lower 95% CI bound |
| `\DetRankGLMFiveTwoVTZeroTiesInclHi` | 85.3 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, glm-5.2, upper 95% CI bound |
| `\DetRankGLMFiveTwoVTZeroTiesInclCI` | [79.7, 85.3] | % attacked stores where the forged entry is most suspicious incl. ties, V T0, glm-5.2, 95% CI |
| `\DetRankGLMFiveTwoVTZeroTiesInclN` | 300 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, glm-5.2, n |
| `\DetRankGLMFiveTwoVTZeroTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashVTZeroStrict` | 80.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, glm-5.3-flash |
| `\DetRankGLMFiveThreeFlashVTZeroStrictLo` | 78.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, glm-5.3-flash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTZeroStrictHi` | 82.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, glm-5.3-flash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTZeroStrictCI` | [78.3, 82.3] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, glm-5.3-flash, 95% CI |
| `\DetRankGLMFiveThreeFlashVTZeroStrictN` | 300 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, glm-5.3-flash, n |
| `\DetRankGLMFiveThreeFlashVTZeroStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashVTZeroTiesIncl` | 84.7 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, glm-5.3-flash |
| `\DetRankGLMFiveThreeFlashVTZeroTiesInclLo` | 82.3 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, glm-5.3-flash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTZeroTiesInclHi` | 87.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, glm-5.3-flash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTZeroTiesInclCI` | [82.3, 87.0] | % attacked stores where the forged entry is most suspicious incl. ties, V T0, glm-5.3-flash, 95% CI |
| `\DetRankGLMFiveThreeFlashVTZeroTiesInclN` | 300 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, glm-5.3-flash, n |
| `\DetRankGLMFiveThreeFlashVTZeroTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBVTZeroStrict` | 62.4 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, qwen3.8-27b |
| `\DetRankQwenThreeEightTwoSevenBVTZeroStrictLo` | 57.2 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, qwen3.8-27b, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTZeroStrictHi` | 67.1 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, qwen3.8-27b, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTZeroStrictCI` | [57.2, 67.1] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, qwen3.8-27b, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBVTZeroStrictN` | 298 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, qwen3.8-27b, n |
| `\DetRankQwenThreeEightTwoSevenBVTZeroStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBVTZeroTiesIncl` | 99.3 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, qwen3.8-27b |
| `\DetRankQwenThreeEightTwoSevenBVTZeroTiesInclLo` | 98.3 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, qwen3.8-27b, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTZeroTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, qwen3.8-27b, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTZeroTiesInclCI` | [98.3, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, V T0, qwen3.8-27b, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBVTZeroTiesInclN` | 298 | % attacked stores where the forged entry is most suspicious incl. ties, V T0, qwen3.8-27b, n |
| `\DetRankQwenThreeEightTwoSevenBVTZeroTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledVTOneStrict` | 29.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, pooled |
| `\DetRankPooledVTOneStrictLo` | 25.9 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, pooled, lower 95% CI bound |
| `\DetRankPooledVTOneStrictHi` | 32.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, pooled, upper 95% CI bound |
| `\DetRankPooledVTOneStrictCI` | [25.9, 32.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, pooled, 95% CI |
| `\DetRankPooledVTOneStrictN` | 1{,}455 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, pooled, n |
| `\DetRankPooledVTOneStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledVTOneTiesIncl` | 73.7 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, pooled |
| `\DetRankPooledVTOneTiesInclLo` | 70.8 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, pooled, lower 95% CI bound |
| `\DetRankPooledVTOneTiesInclHi` | 76.5 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, pooled, upper 95% CI bound |
| `\DetRankPooledVTOneTiesInclCI` | [70.8, 76.5] | % attacked stores where the forged entry is most suspicious incl. ties, V T1, pooled, 95% CI |
| `\DetRankPooledVTOneTiesInclN` | 1{,}455 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, pooled, n |
| `\DetRankPooledVTOneTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashVTOneStrict` | 27.6 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashVTOneStrictLo` | 21.5 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTOneStrictHi` | 33.6 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTOneStrictCI` | [21.5, 33.6] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashVTOneStrictN` | 297 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashVTOneStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashVTOneTiesIncl` | 59.6 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashVTOneTiesInclLo` | 51.5 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTOneTiesInclHi` | 67.2 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTOneTiesInclCI` | [51.5, 67.2] | % attacked stores where the forged entry is most suspicious incl. ties, V T1, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashVTOneTiesInclN` | 297 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashVTOneTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBVTOneStrict` | 9.1 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBVTOneStrictLo` | 5.8 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTOneStrictHi` | 12.4 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTOneStrictCI` | [5.8, 12.4] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBVTOneStrictN` | 276 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBVTOneStrictP` | 0.006 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBVTOneTiesIncl` | 98.6 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBVTOneTiesInclLo` | 96.4 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTOneTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTOneTiesInclCI` | [96.4, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, V T1, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBVTOneTiesInclN` | 276 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBVTOneTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoVTOneStrict` | 44.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, glm-5.2 |
| `\DetRankGLMFiveTwoVTOneStrictLo` | 38.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, glm-5.2, lower 95% CI bound |
| `\DetRankGLMFiveTwoVTOneStrictHi` | 49.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, glm-5.2, upper 95% CI bound |
| `\DetRankGLMFiveTwoVTOneStrictCI` | [38.3, 49.7] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, glm-5.2, 95% CI |
| `\DetRankGLMFiveTwoVTOneStrictN` | 293 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, glm-5.2, n |
| `\DetRankGLMFiveTwoVTOneStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoVTOneTiesIncl` | 59.4 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, glm-5.2 |
| `\DetRankGLMFiveTwoVTOneTiesInclLo` | 52.9 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, glm-5.2, lower 95% CI bound |
| `\DetRankGLMFiveTwoVTOneTiesInclHi` | 65.8 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, glm-5.2, upper 95% CI bound |
| `\DetRankGLMFiveTwoVTOneTiesInclCI` | [52.9, 65.8] | % attacked stores where the forged entry is most suspicious incl. ties, V T1, glm-5.2, 95% CI |
| `\DetRankGLMFiveTwoVTOneTiesInclN` | 293 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, glm-5.2, n |
| `\DetRankGLMFiveTwoVTOneTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashVTOneStrict` | 46.6 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, glm-5.3-flash |
| `\DetRankGLMFiveThreeFlashVTOneStrictLo` | 41.9 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, glm-5.3-flash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTOneStrictHi` | 51.5 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, glm-5.3-flash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTOneStrictCI` | [41.9, 51.5] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, glm-5.3-flash, 95% CI |
| `\DetRankGLMFiveThreeFlashVTOneStrictN` | 296 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, glm-5.3-flash, n |
| `\DetRankGLMFiveThreeFlashVTOneStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashVTOneTiesIncl` | 55.7 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, glm-5.3-flash |
| `\DetRankGLMFiveThreeFlashVTOneTiesInclLo` | 51.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, glm-5.3-flash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTOneTiesInclHi` | 60.8 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, glm-5.3-flash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTOneTiesInclCI` | [51.0, 60.8] | % attacked stores where the forged entry is most suspicious incl. ties, V T1, glm-5.3-flash, 95% CI |
| `\DetRankGLMFiveThreeFlashVTOneTiesInclN` | 296 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, glm-5.3-flash, n |
| `\DetRankGLMFiveThreeFlashVTOneTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBVTOneStrict` | 16.4 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, qwen3.8-27b |
| `\DetRankQwenThreeEightTwoSevenBVTOneStrictLo` | 13.2 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, qwen3.8-27b, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTOneStrictHi` | 19.6 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, qwen3.8-27b, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTOneStrictCI` | [13.2, 19.6] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, qwen3.8-27b, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBVTOneStrictN` | 293 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, qwen3.8-27b, n |
| `\DetRankQwenThreeEightTwoSevenBVTOneStrictP` | 0.236 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBVTOneTiesIncl` | 96.9 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, qwen3.8-27b |
| `\DetRankQwenThreeEightTwoSevenBVTOneTiesInclLo` | 94.2 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, qwen3.8-27b, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTOneTiesInclHi` | 99.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, qwen3.8-27b, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTOneTiesInclCI` | [94.2, 99.0] | % attacked stores where the forged entry is most suspicious incl. ties, V T1, qwen3.8-27b, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBVTOneTiesInclN` | 293 | % attacked stores where the forged entry is most suspicious incl. ties, V T1, qwen3.8-27b, n |
| `\DetRankQwenThreeEightTwoSevenBVTOneTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledVTTwoStrict` | 29.8 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, pooled |
| `\DetRankPooledVTTwoStrictLo` | 27.2 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, pooled, lower 95% CI bound |
| `\DetRankPooledVTTwoStrictHi` | 32.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, pooled, upper 95% CI bound |
| `\DetRankPooledVTTwoStrictCI` | [27.2, 32.3] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, pooled, 95% CI |
| `\DetRankPooledVTTwoStrictN` | 1{,}458 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, pooled, n |
| `\DetRankPooledVTTwoStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledVTTwoTiesIncl` | 74.1 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, pooled |
| `\DetRankPooledVTTwoTiesInclLo` | 71.2 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, pooled, lower 95% CI bound |
| `\DetRankPooledVTTwoTiesInclHi` | 76.7 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, pooled, upper 95% CI bound |
| `\DetRankPooledVTTwoTiesInclCI` | [71.2, 76.7] | % attacked stores where the forged entry is most suspicious incl. ties, V T2, pooled, 95% CI |
| `\DetRankPooledVTTwoTiesInclN` | 1{,}458 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, pooled, n |
| `\DetRankPooledVTTwoTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashVTTwoStrict` | 27.2 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashVTTwoStrictLo` | 21.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTTwoStrictHi` | 32.9 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTTwoStrictCI` | [21.7, 32.9] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashVTTwoStrictN` | 298 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashVTTwoStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashVTTwoTiesIncl` | 62.8 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashVTTwoTiesInclLo` | 55.7 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTTwoTiesInclHi` | 69.6 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTTwoTiesInclCI` | [55.7, 69.6] | % attacked stores where the forged entry is most suspicious incl. ties, V T2, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashVTTwoTiesInclN` | 298 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashVTTwoTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBVTTwoStrict` | 12.6 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBVTTwoStrictLo` | 9.6 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTTwoStrictHi` | 15.8 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTTwoStrictCI` | [9.6, 15.8] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBVTTwoStrictN` | 269 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBVTTwoStrictP` | 0.304 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBVTTwoTiesIncl` | 98.1 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBVTTwoTiesInclLo` | 95.2 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTTwoTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTTwoTiesInclCI` | [95.2, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, V T2, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBVTTwoTiesInclN` | 269 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBVTTwoTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoVTTwoStrict` | 44.1 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, glm-5.2 |
| `\DetRankGLMFiveTwoVTTwoStrictLo` | 39.2 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, glm-5.2, lower 95% CI bound |
| `\DetRankGLMFiveTwoVTTwoStrictHi` | 49.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, glm-5.2, upper 95% CI bound |
| `\DetRankGLMFiveTwoVTTwoStrictCI` | [39.2, 49.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, glm-5.2, 95% CI |
| `\DetRankGLMFiveTwoVTTwoStrictN` | 299 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, glm-5.2, n |
| `\DetRankGLMFiveTwoVTTwoStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoVTTwoTiesIncl` | 58.5 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, glm-5.2 |
| `\DetRankGLMFiveTwoVTTwoTiesInclLo` | 53.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, glm-5.2, lower 95% CI bound |
| `\DetRankGLMFiveTwoVTTwoTiesInclHi` | 64.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, glm-5.2, upper 95% CI bound |
| `\DetRankGLMFiveTwoVTTwoTiesInclCI` | [53.0, 64.0] | % attacked stores where the forged entry is most suspicious incl. ties, V T2, glm-5.2, 95% CI |
| `\DetRankGLMFiveTwoVTTwoTiesInclN` | 299 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, glm-5.2, n |
| `\DetRankGLMFiveTwoVTTwoTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashVTTwoStrict` | 49.2 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, glm-5.3-flash |
| `\DetRankGLMFiveThreeFlashVTTwoStrictLo` | 44.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, glm-5.3-flash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTTwoStrictHi` | 53.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, glm-5.3-flash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTTwoStrictCI` | [44.3, 53.7] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, glm-5.3-flash, 95% CI |
| `\DetRankGLMFiveThreeFlashVTTwoStrictN` | 299 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, glm-5.3-flash, n |
| `\DetRankGLMFiveThreeFlashVTTwoStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashVTTwoTiesIncl` | 57.9 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, glm-5.3-flash |
| `\DetRankGLMFiveThreeFlashVTTwoTiesInclLo` | 53.2 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, glm-5.3-flash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTTwoTiesInclHi` | 62.6 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, glm-5.3-flash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTTwoTiesInclCI` | [53.2, 62.6] | % attacked stores where the forged entry is most suspicious incl. ties, V T2, glm-5.3-flash, 95% CI |
| `\DetRankGLMFiveThreeFlashVTTwoTiesInclN` | 299 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, glm-5.3-flash, n |
| `\DetRankGLMFiveThreeFlashVTTwoTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBVTTwoStrict` | 13.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, qwen3.8-27b |
| `\DetRankQwenThreeEightTwoSevenBVTTwoStrictLo` | 10.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, qwen3.8-27b, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTTwoStrictHi` | 17.2 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, qwen3.8-27b, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTTwoStrictCI` | [10.3, 17.2] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, qwen3.8-27b, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBVTTwoStrictN` | 293 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, qwen3.8-27b, n |
| `\DetRankQwenThreeEightTwoSevenBVTTwoStrictP` | 0.695 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBVTTwoTiesIncl` | 95.9 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, qwen3.8-27b |
| `\DetRankQwenThreeEightTwoSevenBVTTwoTiesInclLo` | 92.8 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, qwen3.8-27b, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTTwoTiesInclHi` | 98.6 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, qwen3.8-27b, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTTwoTiesInclCI` | [92.8, 98.6] | % attacked stores where the forged entry is most suspicious incl. ties, V T2, qwen3.8-27b, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBVTTwoTiesInclN` | 293 | % attacked stores where the forged entry is most suspicious incl. ties, V T2, qwen3.8-27b, n |
| `\DetRankQwenThreeEightTwoSevenBVTTwoTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledVTThreeStrict` | 25.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, pooled |
| `\DetRankPooledVTThreeStrictLo` | 22.9 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, pooled, lower 95% CI bound |
| `\DetRankPooledVTThreeStrictHi` | 28.5 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, pooled, upper 95% CI bound |
| `\DetRankPooledVTThreeStrictCI` | [22.9, 28.5] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, pooled, 95% CI |
| `\DetRankPooledVTThreeStrictN` | 1{,}472 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, pooled, n |
| `\DetRankPooledVTThreeStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankPooledVTThreeTiesIncl` | 71.9 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, pooled |
| `\DetRankPooledVTThreeTiesInclLo` | 68.8 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, pooled, lower 95% CI bound |
| `\DetRankPooledVTThreeTiesInclHi` | 75.1 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, pooled, upper 95% CI bound |
| `\DetRankPooledVTThreeTiesInclCI` | [68.8, 75.1] | % attacked stores where the forged entry is most suspicious incl. ties, V T3, pooled, 95% CI |
| `\DetRankPooledVTThreeTiesInclN` | 1{,}472 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, pooled, n |
| `\DetRankPooledVTThreeTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashVTThreeStrict` | 23.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashVTThreeStrictLo` | 17.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTThreeStrictHi` | 30.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTThreeStrictCI` | [17.7, 30.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashVTThreeStrictN` | 300 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashVTThreeStrictP` | 0.002 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankDeepSeekVFourFlashVTThreeTiesIncl` | 57.7 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, deepseek-v4-flash |
| `\DetRankDeepSeekVFourFlashVTThreeTiesInclLo` | 49.3 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, deepseek-v4-flash, lower 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTThreeTiesInclHi` | 65.7 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, deepseek-v4-flash, upper 95% CI bound |
| `\DetRankDeepSeekVFourFlashVTThreeTiesInclCI` | [49.3, 65.7] | % attacked stores where the forged entry is most suspicious incl. ties, V T3, deepseek-v4-flash, 95% CI |
| `\DetRankDeepSeekVFourFlashVTThreeTiesInclN` | 300 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, deepseek-v4-flash, n |
| `\DetRankDeepSeekVFourFlashVTThreeTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBVTThreeStrict` | 11.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBVTThreeStrictLo` | 8.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTThreeStrictHi` | 14.9 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTThreeStrictCI` | [8.0, 14.9] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBVTThreeStrictN` | 275 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBVTThreeStrictP` | 0.098 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGemmaFourThreeOneBVTThreeTiesIncl` | 98.5 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, gemma-4-31b-it |
| `\DetRankGemmaFourThreeOneBVTThreeTiesInclLo` | 96.7 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, gemma-4-31b-it, lower 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTThreeTiesInclHi` | 100.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, gemma-4-31b-it, upper 95% CI bound |
| `\DetRankGemmaFourThreeOneBVTThreeTiesInclCI` | [96.7, 100.0] | % attacked stores where the forged entry is most suspicious incl. ties, V T3, gemma-4-31b-it, 95% CI |
| `\DetRankGemmaFourThreeOneBVTThreeTiesInclN` | 275 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, gemma-4-31b-it, n |
| `\DetRankGemmaFourThreeOneBVTThreeTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoVTThreeStrict` | 39.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, glm-5.2 |
| `\DetRankGLMFiveTwoVTThreeStrictLo` | 35.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, glm-5.2, lower 95% CI bound |
| `\DetRankGLMFiveTwoVTThreeStrictHi` | 44.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, glm-5.2, upper 95% CI bound |
| `\DetRankGLMFiveTwoVTThreeStrictCI` | [35.3, 44.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, glm-5.2, 95% CI |
| `\DetRankGLMFiveTwoVTThreeStrictN` | 300 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, glm-5.2, n |
| `\DetRankGLMFiveTwoVTThreeStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveTwoVTThreeTiesIncl` | 55.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, glm-5.2 |
| `\DetRankGLMFiveTwoVTThreeTiesInclLo` | 48.7 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, glm-5.2, lower 95% CI bound |
| `\DetRankGLMFiveTwoVTThreeTiesInclHi` | 60.7 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, glm-5.2, upper 95% CI bound |
| `\DetRankGLMFiveTwoVTThreeTiesInclCI` | [48.7, 60.7] | % attacked stores where the forged entry is most suspicious incl. ties, V T3, glm-5.2, 95% CI |
| `\DetRankGLMFiveTwoVTThreeTiesInclN` | 300 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, glm-5.2, n |
| `\DetRankGLMFiveTwoVTThreeTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashVTThreeStrict` | 42.7 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, glm-5.3-flash |
| `\DetRankGLMFiveThreeFlashVTThreeStrictLo` | 37.3 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, glm-5.3-flash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTThreeStrictHi` | 48.0 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, glm-5.3-flash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTThreeStrictCI` | [37.3, 48.0] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, glm-5.3-flash, 95% CI |
| `\DetRankGLMFiveThreeFlashVTThreeStrictN` | 300 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, glm-5.3-flash, n |
| `\DetRankGLMFiveThreeFlashVTThreeStrictP` | \ensuremath{<}0.001 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankGLMFiveThreeFlashVTThreeTiesIncl` | 54.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, glm-5.3-flash |
| `\DetRankGLMFiveThreeFlashVTThreeTiesInclLo` | 48.7 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, glm-5.3-flash, lower 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTThreeTiesInclHi` | 59.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, glm-5.3-flash, upper 95% CI bound |
| `\DetRankGLMFiveThreeFlashVTThreeTiesInclCI` | [48.7, 59.0] | % attacked stores where the forged entry is most suspicious incl. ties, V T3, glm-5.3-flash, 95% CI |
| `\DetRankGLMFiveThreeFlashVTThreeTiesInclN` | 300 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, glm-5.3-flash, n |
| `\DetRankGLMFiveThreeFlashVTThreeTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBVTThreeStrict` | 9.8 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, qwen3.8-27b |
| `\DetRankQwenThreeEightTwoSevenBVTThreeStrictLo` | 7.1 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, qwen3.8-27b, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTThreeStrictHi` | 12.8 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, qwen3.8-27b, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTThreeStrictCI` | [7.1, 12.8] | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, qwen3.8-27b, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBVTThreeStrictN` | 297 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, qwen3.8-27b, n |
| `\DetRankQwenThreeEightTwoSevenBVTThreeStrictP` | 0.007 | % attacked stores where the forged entry is strictly most suspicious (chance 14.3), V T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetRankQwenThreeEightTwoSevenBVTThreeTiesIncl` | 97.0 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, qwen3.8-27b |
| `\DetRankQwenThreeEightTwoSevenBVTThreeTiesInclLo` | 94.3 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, qwen3.8-27b, lower 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTThreeTiesInclHi` | 99.3 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, qwen3.8-27b, upper 95% CI bound |
| `\DetRankQwenThreeEightTwoSevenBVTThreeTiesInclCI` | [94.3, 99.3] | % attacked stores where the forged entry is most suspicious incl. ties, V T3, qwen3.8-27b, 95% CI |
| `\DetRankQwenThreeEightTwoSevenBVTThreeTiesInclN` | 297 | % attacked stores where the forged entry is most suspicious incl. ties, V T3, qwen3.8-27b, n |
| `\DetRankQwenThreeEightTwoSevenBVTThreeTiesInclP` | n/a | % attacked stores where the forged entry is most suspicious incl. ties, V T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetRederivDisagreePooled` | 43.2 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), pooled |
| `\DetRederivDisagreePooledLo` | 40.7 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), pooled, lower 95% CI bound |
| `\DetRederivDisagreePooledHi` | 45.6 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), pooled, upper 95% CI bound |
| `\DetRederivDisagreePooledCI` | [40.7, 45.6] | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), pooled, 95% CI |
| `\DetRederivDisagreePooledN` | 2{,}087 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), pooled, n |
| `\DetRederivDisagreePooledP` | n/a | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), pooled, two-sided bootstrap p (n/a if not tested) |
| `\DetRederivDisagreeDeepSeekVFourFlash` | 58.8 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), deepseek-v4-flash |
| `\DetRederivDisagreeDeepSeekVFourFlashLo` | 53.3 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), deepseek-v4-flash, lower 95% CI bound |
| `\DetRederivDisagreeDeepSeekVFourFlashHi` | 64.6 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), deepseek-v4-flash, upper 95% CI bound |
| `\DetRederivDisagreeDeepSeekVFourFlashCI` | [53.3, 64.6] | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), deepseek-v4-flash, 95% CI |
| `\DetRederivDisagreeDeepSeekVFourFlashN` | 413 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), deepseek-v4-flash, n |
| `\DetRederivDisagreeDeepSeekVFourFlashP` | n/a | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRederivDisagreeGemmaFourThreeOneB` | 37.0 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), gemma-4-31b-it |
| `\DetRederivDisagreeGemmaFourThreeOneBLo` | 31.7 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), gemma-4-31b-it, lower 95% CI bound |
| `\DetRederivDisagreeGemmaFourThreeOneBHi` | 42.3 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), gemma-4-31b-it, upper 95% CI bound |
| `\DetRederivDisagreeGemmaFourThreeOneBCI` | [31.7, 42.3] | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), gemma-4-31b-it, 95% CI |
| `\DetRederivDisagreeGemmaFourThreeOneBN` | 414 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), gemma-4-31b-it, n |
| `\DetRederivDisagreeGemmaFourThreeOneBP` | n/a | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\DetRederivDisagreeGLMFiveTwo` | 31.7 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), glm-5.2 |
| `\DetRederivDisagreeGLMFiveTwoLo` | 25.7 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), glm-5.2, lower 95% CI bound |
| `\DetRederivDisagreeGLMFiveTwoHi` | 37.6 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), glm-5.2, upper 95% CI bound |
| `\DetRederivDisagreeGLMFiveTwoCI` | [25.7, 37.6] | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), glm-5.2, 95% CI |
| `\DetRederivDisagreeGLMFiveTwoN` | 420 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), glm-5.2, n |
| `\DetRederivDisagreeGLMFiveTwoP` | n/a | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\DetRederivDisagreeGLMFiveThreeFlash` | 34.3 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), glm-5.3-flash |
| `\DetRederivDisagreeGLMFiveThreeFlashLo` | 28.1 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), glm-5.3-flash, lower 95% CI bound |
| `\DetRederivDisagreeGLMFiveThreeFlashHi` | 40.2 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), glm-5.3-flash, upper 95% CI bound |
| `\DetRederivDisagreeGLMFiveThreeFlashCI` | [28.1, 40.2] | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), glm-5.3-flash, 95% CI |
| `\DetRederivDisagreeGLMFiveThreeFlashN` | 420 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), glm-5.3-flash, n |
| `\DetRederivDisagreeGLMFiveThreeFlashP` | n/a | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\DetRederivDisagreeQwenThreeEightTwoSevenB` | 54.5 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), qwen3.8-27b |
| `\DetRederivDisagreeQwenThreeEightTwoSevenBLo` | 49.0 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), qwen3.8-27b, lower 95% CI bound |
| `\DetRederivDisagreeQwenThreeEightTwoSevenBHi` | 59.5 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), qwen3.8-27b, upper 95% CI bound |
| `\DetRederivDisagreeQwenThreeEightTwoSevenBCI` | [49.0, 59.5] | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), qwen3.8-27b, 95% CI |
| `\DetRederivDisagreeQwenThreeEightTwoSevenBN` | 420 | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), qwen3.8-27b, n |
| `\DetRederivDisagreeQwenThreeEightTwoSevenBP` | n/a | re-derivation disagreement rate for untouched genuine notes: % with p_altered >= 50 (R false positives), qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\DetVerbalTThree` | 0.60 | mean AUROC of V at T3 (reported with primary 2) |
| `\DetVerbalTThreeLo` | 0.59 | mean AUROC of V at T3 (reported with primary 2), lower 95% CI bound |
| `\DetVerbalTThreeHi` | 0.62 | mean AUROC of V at T3 (reported with primary 2), upper 95% CI bound |
| `\DetVerbalTThreeCI` | [0.59, 0.62] | mean AUROC of V at T3 (reported with primary 2), 95% CI |
| `\DetVerbalTThreeN` | 2{,}942 | mean AUROC of V at T3 (reported with primary 2), n |
| `\DetVerbalTThreeP` | \ensuremath{<}0.001 | mean AUROC of V at T3 (reported with primary 2), two-sided bootstrap p (n/a if not tested) |
| `\DetCalibR` | 0.94 | pooled calibration AUROC of R (selection for primary 3) |
| `\DetCalibRLo` | 0.91 | pooled calibration AUROC of R (selection for primary 3), lower 95% CI bound |
| `\DetCalibRHi` | 0.97 | pooled calibration AUROC of R (selection for primary 3), upper 95% CI bound |
| `\DetCalibRCI` | [0.91, 0.97] | pooled calibration AUROC of R (selection for primary 3), 95% CI |
| `\DetCalibRN` | 1{,}602 | pooled calibration AUROC of R (selection for primary 3), n |
| `\DetCalibRP` | n/a | pooled calibration AUROC of R (selection for primary 3), two-sided bootstrap p (n/a if not tested) |
| `\DetCalibC` | 0.99 | pooled calibration AUROC of C (selection for primary 3) |
| `\DetCalibCLo` | 0.98 | pooled calibration AUROC of C (selection for primary 3), lower 95% CI bound |
| `\DetCalibCHi` | 0.99 | pooled calibration AUROC of C (selection for primary 3), upper 95% CI bound |
| `\DetCalibCCI` | [0.98, 0.99] | pooled calibration AUROC of C (selection for primary 3), 95% CI |
| `\DetCalibCN` | 1{,}611 | pooled calibration AUROC of C (selection for primary 3), n |
| `\DetCalibCP` | n/a | pooled calibration AUROC of C (selection for primary 3), two-sided bootstrap p (n/a if not tested) |
| `\NegsDeepSeekVFourFlashOtherEpisode` | 0.53 | matched negatives: AUROC of V, other_episode vs genuine, deepseek-v4-flash |
| `\NegsDeepSeekVFourFlashOtherEpisodeLo` | 0.48 | matched negatives: AUROC of V, other_episode vs genuine, deepseek-v4-flash, lower 95% CI bound |
| `\NegsDeepSeekVFourFlashOtherEpisodeHi` | 0.59 | matched negatives: AUROC of V, other_episode vs genuine, deepseek-v4-flash, upper 95% CI bound |
| `\NegsDeepSeekVFourFlashOtherEpisodeCI` | [0.48, 0.59] | matched negatives: AUROC of V, other_episode vs genuine, deepseek-v4-flash, 95% CI |
| `\NegsDeepSeekVFourFlashOtherEpisodeN` | 240 | matched negatives: AUROC of V, other_episode vs genuine, deepseek-v4-flash, n |
| `\NegsDeepSeekVFourFlashOtherEpisodeP` | n/a | matched negatives: AUROC of V, other_episode vs genuine, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\NegsDeepSeekVFourFlashOtherModel` | 0.52 | matched negatives: AUROC of V, other_model vs genuine, deepseek-v4-flash |
| `\NegsDeepSeekVFourFlashOtherModelLo` | 0.48 | matched negatives: AUROC of V, other_model vs genuine, deepseek-v4-flash, lower 95% CI bound |
| `\NegsDeepSeekVFourFlashOtherModelHi` | 0.56 | matched negatives: AUROC of V, other_model vs genuine, deepseek-v4-flash, upper 95% CI bound |
| `\NegsDeepSeekVFourFlashOtherModelCI` | [0.48, 0.56] | matched negatives: AUROC of V, other_model vs genuine, deepseek-v4-flash, 95% CI |
| `\NegsDeepSeekVFourFlashOtherModelN` | 238 | matched negatives: AUROC of V, other_model vs genuine, deepseek-v4-flash, n |
| `\NegsDeepSeekVFourFlashOtherModelP` | n/a | matched negatives: AUROC of V, other_model vs genuine, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\NegsQwenThreeEightTwoSevenBOtherEpisode` | 0.52 | matched negatives: AUROC of V, other_episode vs genuine, qwen3.8-27b |
| `\NegsQwenThreeEightTwoSevenBOtherEpisodeLo` | 0.46 | matched negatives: AUROC of V, other_episode vs genuine, qwen3.8-27b, lower 95% CI bound |
| `\NegsQwenThreeEightTwoSevenBOtherEpisodeHi` | 0.58 | matched negatives: AUROC of V, other_episode vs genuine, qwen3.8-27b, upper 95% CI bound |
| `\NegsQwenThreeEightTwoSevenBOtherEpisodeCI` | [0.46, 0.58] | matched negatives: AUROC of V, other_episode vs genuine, qwen3.8-27b, 95% CI |
| `\NegsQwenThreeEightTwoSevenBOtherEpisodeN` | 240 | matched negatives: AUROC of V, other_episode vs genuine, qwen3.8-27b, n |
| `\NegsQwenThreeEightTwoSevenBOtherEpisodeP` | n/a | matched negatives: AUROC of V, other_episode vs genuine, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\NegsQwenThreeEightTwoSevenBOtherModel` | 0.46 | matched negatives: AUROC of V, other_model vs genuine, qwen3.8-27b |
| `\NegsQwenThreeEightTwoSevenBOtherModelLo` | 0.40 | matched negatives: AUROC of V, other_model vs genuine, qwen3.8-27b, lower 95% CI bound |
| `\NegsQwenThreeEightTwoSevenBOtherModelHi` | 0.52 | matched negatives: AUROC of V, other_model vs genuine, qwen3.8-27b, upper 95% CI bound |
| `\NegsQwenThreeEightTwoSevenBOtherModelCI` | [0.40, 0.52] | matched negatives: AUROC of V, other_model vs genuine, qwen3.8-27b, 95% CI |
| `\NegsQwenThreeEightTwoSevenBOtherModelN` | 234 | matched negatives: AUROC of V, other_model vs genuine, qwen3.8-27b, n |
| `\NegsQwenThreeEightTwoSevenBOtherModelP` | n/a | matched negatives: AUROC of V, other_model vs genuine, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\NegsGemmaFourThreeOneBOtherEpisode` | 0.52 | matched negatives: AUROC of V, other_episode vs genuine, gemma-4-31b-it |
| `\NegsGemmaFourThreeOneBOtherEpisodeLo` | 0.50 | matched negatives: AUROC of V, other_episode vs genuine, gemma-4-31b-it, lower 95% CI bound |
| `\NegsGemmaFourThreeOneBOtherEpisodeHi` | 0.54 | matched negatives: AUROC of V, other_episode vs genuine, gemma-4-31b-it, upper 95% CI bound |
| `\NegsGemmaFourThreeOneBOtherEpisodeCI` | [0.50, 0.54] | matched negatives: AUROC of V, other_episode vs genuine, gemma-4-31b-it, 95% CI |
| `\NegsGemmaFourThreeOneBOtherEpisodeN` | 222 | matched negatives: AUROC of V, other_episode vs genuine, gemma-4-31b-it, n |
| `\NegsGemmaFourThreeOneBOtherEpisodeP` | n/a | matched negatives: AUROC of V, other_episode vs genuine, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\NegsGemmaFourThreeOneBOtherModel` | 0.50 | matched negatives: AUROC of V, other_model vs genuine, gemma-4-31b-it |
| `\NegsGemmaFourThreeOneBOtherModelLo` | 0.50 | matched negatives: AUROC of V, other_model vs genuine, gemma-4-31b-it, lower 95% CI bound |
| `\NegsGemmaFourThreeOneBOtherModelHi` | 0.50 | matched negatives: AUROC of V, other_model vs genuine, gemma-4-31b-it, upper 95% CI bound |
| `\NegsGemmaFourThreeOneBOtherModelCI` | [0.50, 0.50] | matched negatives: AUROC of V, other_model vs genuine, gemma-4-31b-it, 95% CI |
| `\NegsGemmaFourThreeOneBOtherModelN` | 218 | matched negatives: AUROC of V, other_model vs genuine, gemma-4-31b-it, n |
| `\NegsGemmaFourThreeOneBOtherModelP` | n/a | matched negatives: AUROC of V, other_model vs genuine, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\NegsGLMFiveThreeFlashOtherEpisode` | 0.52 | matched negatives: AUROC of V, other_episode vs genuine, glm-5.3-flash |
| `\NegsGLMFiveThreeFlashOtherEpisodeLo` | 0.47 | matched negatives: AUROC of V, other_episode vs genuine, glm-5.3-flash, lower 95% CI bound |
| `\NegsGLMFiveThreeFlashOtherEpisodeHi` | 0.57 | matched negatives: AUROC of V, other_episode vs genuine, glm-5.3-flash, upper 95% CI bound |
| `\NegsGLMFiveThreeFlashOtherEpisodeCI` | [0.47, 0.57] | matched negatives: AUROC of V, other_episode vs genuine, glm-5.3-flash, 95% CI |
| `\NegsGLMFiveThreeFlashOtherEpisodeN` | 240 | matched negatives: AUROC of V, other_episode vs genuine, glm-5.3-flash, n |
| `\NegsGLMFiveThreeFlashOtherEpisodeP` | n/a | matched negatives: AUROC of V, other_episode vs genuine, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\NegsGLMFiveThreeFlashOtherModel` | 0.60 | matched negatives: AUROC of V, other_model vs genuine, glm-5.3-flash |
| `\NegsGLMFiveThreeFlashOtherModelLo` | 0.56 | matched negatives: AUROC of V, other_model vs genuine, glm-5.3-flash, lower 95% CI bound |
| `\NegsGLMFiveThreeFlashOtherModelHi` | 0.65 | matched negatives: AUROC of V, other_model vs genuine, glm-5.3-flash, upper 95% CI bound |
| `\NegsGLMFiveThreeFlashOtherModelCI` | [0.56, 0.65] | matched negatives: AUROC of V, other_model vs genuine, glm-5.3-flash, 95% CI |
| `\NegsGLMFiveThreeFlashOtherModelN` | 238 | matched negatives: AUROC of V, other_model vs genuine, glm-5.3-flash, n |
| `\NegsGLMFiveThreeFlashOtherModelP` | n/a | matched negatives: AUROC of V, other_model vs genuine, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\NegsGLMFiveTwoOtherEpisode` | 0.55 | matched negatives: AUROC of V, other_episode vs genuine, glm-5.2 |
| `\NegsGLMFiveTwoOtherEpisodeLo` | 0.50 | matched negatives: AUROC of V, other_episode vs genuine, glm-5.2, lower 95% CI bound |
| `\NegsGLMFiveTwoOtherEpisodeHi` | 0.61 | matched negatives: AUROC of V, other_episode vs genuine, glm-5.2, upper 95% CI bound |
| `\NegsGLMFiveTwoOtherEpisodeCI` | [0.50, 0.61] | matched negatives: AUROC of V, other_episode vs genuine, glm-5.2, 95% CI |
| `\NegsGLMFiveTwoOtherEpisodeN` | 240 | matched negatives: AUROC of V, other_episode vs genuine, glm-5.2, n |
| `\NegsGLMFiveTwoOtherEpisodeP` | n/a | matched negatives: AUROC of V, other_episode vs genuine, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\NegsGLMFiveTwoOtherModel` | 0.55 | matched negatives: AUROC of V, other_model vs genuine, glm-5.2 |
| `\NegsGLMFiveTwoOtherModelLo` | 0.50 | matched negatives: AUROC of V, other_model vs genuine, glm-5.2, lower 95% CI bound |
| `\NegsGLMFiveTwoOtherModelHi` | 0.61 | matched negatives: AUROC of V, other_model vs genuine, glm-5.2, upper 95% CI bound |
| `\NegsGLMFiveTwoOtherModelCI` | [0.50, 0.61] | matched negatives: AUROC of V, other_model vs genuine, glm-5.2, 95% CI |
| `\NegsGLMFiveTwoOtherModelN` | 238 | matched negatives: AUROC of V, other_model vs genuine, glm-5.2, n |
| `\NegsGLMFiveTwoOtherModelP` | n/a | matched negatives: AUROC of V, other_model vs genuine, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTZero` | 88.1 | 2AFC accuracy (%), T0, pooled |
| `\AfcPooledTZeroLo` | 85.7 | 2AFC accuracy (%), T0, pooled, lower 95% CI bound |
| `\AfcPooledTZeroHi` | 90.4 | 2AFC accuracy (%), T0, pooled, upper 95% CI bound |
| `\AfcPooledTZeroCI` | [85.7, 90.4] | 2AFC accuracy (%), T0, pooled, 95% CI |
| `\AfcPooledTZeroN` | 1{,}480 | 2AFC accuracy (%), T0, pooled, n |
| `\AfcPooledTZeroP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T0, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTZeroEOne` | 54.4 | 2AFC accuracy (%), T0, E1, pooled |
| `\AfcPooledTZeroEOneLo` | 41.4 | 2AFC accuracy (%), T0, E1, pooled, lower 95% CI bound |
| `\AfcPooledTZeroEOneHi` | 66.2 | 2AFC accuracy (%), T0, E1, pooled, upper 95% CI bound |
| `\AfcPooledTZeroEOneCI` | [41.4, 66.2] | 2AFC accuracy (%), T0, E1, pooled, 95% CI |
| `\AfcPooledTZeroEOneN` | 296 | 2AFC accuracy (%), T0, E1, pooled, n |
| `\AfcPooledTZeroEOneP` | 0.532 | 2AFC accuracy (%), T0, E1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTZeroETwo` | 96.6 | 2AFC accuracy (%), T0, E2, pooled |
| `\AfcPooledTZeroETwoLo` | 94.2 | 2AFC accuracy (%), T0, E2, pooled, lower 95% CI bound |
| `\AfcPooledTZeroETwoHi` | 98.6 | 2AFC accuracy (%), T0, E2, pooled, upper 95% CI bound |
| `\AfcPooledTZeroETwoCI` | [94.2, 98.6] | 2AFC accuracy (%), T0, E2, pooled, 95% CI |
| `\AfcPooledTZeroETwoN` | 296 | 2AFC accuracy (%), T0, E2, pooled, n |
| `\AfcPooledTZeroETwoP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T0, E2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTZeroEThree` | 95.3 | 2AFC accuracy (%), T0, E3, pooled |
| `\AfcPooledTZeroEThreeLo` | 92.9 | 2AFC accuracy (%), T0, E3, pooled, lower 95% CI bound |
| `\AfcPooledTZeroEThreeHi` | 97.3 | 2AFC accuracy (%), T0, E3, pooled, upper 95% CI bound |
| `\AfcPooledTZeroEThreeCI` | [92.9, 97.3] | 2AFC accuracy (%), T0, E3, pooled, 95% CI |
| `\AfcPooledTZeroEThreeN` | 296 | 2AFC accuracy (%), T0, E3, pooled, n |
| `\AfcPooledTZeroEThreeP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T0, E3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTZeroEFour` | 98.6 | 2AFC accuracy (%), T0, E4, pooled |
| `\AfcPooledTZeroEFourLo` | 97.3 | 2AFC accuracy (%), T0, E4, pooled, lower 95% CI bound |
| `\AfcPooledTZeroEFourHi` | 99.7 | 2AFC accuracy (%), T0, E4, pooled, upper 95% CI bound |
| `\AfcPooledTZeroEFourCI` | [97.3, 99.7] | 2AFC accuracy (%), T0, E4, pooled, 95% CI |
| `\AfcPooledTZeroEFourN` | 296 | 2AFC accuracy (%), T0, E4, pooled, n |
| `\AfcPooledTZeroEFourP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T0, E4, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTZeroEFive` | 95.6 | 2AFC accuracy (%), T0, E5, pooled |
| `\AfcPooledTZeroEFiveLo` | 92.9 | 2AFC accuracy (%), T0, E5, pooled, lower 95% CI bound |
| `\AfcPooledTZeroEFiveHi` | 98.0 | 2AFC accuracy (%), T0, E5, pooled, upper 95% CI bound |
| `\AfcPooledTZeroEFiveCI` | [92.9, 98.0] | 2AFC accuracy (%), T0, E5, pooled, 95% CI |
| `\AfcPooledTZeroEFiveN` | 296 | 2AFC accuracy (%), T0, E5, pooled, n |
| `\AfcPooledTZeroEFiveP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T0, E5, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTOne` | 78.6 | 2AFC accuracy (%), T1, pooled |
| `\AfcPooledTOneLo` | 76.2 | 2AFC accuracy (%), T1, pooled, lower 95% CI bound |
| `\AfcPooledTOneHi` | 80.9 | 2AFC accuracy (%), T1, pooled, upper 95% CI bound |
| `\AfcPooledTOneCI` | [76.2, 80.9] | 2AFC accuracy (%), T1, pooled, 95% CI |
| `\AfcPooledTOneN` | 1{,}439 | 2AFC accuracy (%), T1, pooled, n |
| `\AfcPooledTOneP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTOneEOne` | 40.2 | 2AFC accuracy (%), T1, E1, pooled |
| `\AfcPooledTOneEOneLo` | 29.0 | 2AFC accuracy (%), T1, E1, pooled, lower 95% CI bound |
| `\AfcPooledTOneEOneHi` | 51.4 | 2AFC accuracy (%), T1, E1, pooled, upper 95% CI bound |
| `\AfcPooledTOneEOneCI` | [29.0, 51.4] | 2AFC accuracy (%), T1, E1, pooled, 95% CI |
| `\AfcPooledTOneEOneN` | 291 | 2AFC accuracy (%), T1, E1, pooled, n |
| `\AfcPooledTOneEOneP` | 0.109 | 2AFC accuracy (%), T1, E1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTOneETwo` | 86.0 | 2AFC accuracy (%), T1, E2, pooled |
| `\AfcPooledTOneETwoLo` | 81.0 | 2AFC accuracy (%), T1, E2, pooled, lower 95% CI bound |
| `\AfcPooledTOneETwoHi` | 90.5 | 2AFC accuracy (%), T1, E2, pooled, upper 95% CI bound |
| `\AfcPooledTOneETwoCI` | [81.0, 90.5] | 2AFC accuracy (%), T1, E2, pooled, 95% CI |
| `\AfcPooledTOneETwoN` | 292 | 2AFC accuracy (%), T1, E2, pooled, n |
| `\AfcPooledTOneETwoP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T1, E2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTOneEThree` | 92.1 | 2AFC accuracy (%), T1, E3, pooled |
| `\AfcPooledTOneEThreeLo` | 88.4 | 2AFC accuracy (%), T1, E3, pooled, lower 95% CI bound |
| `\AfcPooledTOneEThreeHi` | 95.8 | 2AFC accuracy (%), T1, E3, pooled, upper 95% CI bound |
| `\AfcPooledTOneEThreeCI` | [88.4, 95.8] | 2AFC accuracy (%), T1, E3, pooled, 95% CI |
| `\AfcPooledTOneEThreeN` | 292 | 2AFC accuracy (%), T1, E3, pooled, n |
| `\AfcPooledTOneEThreeP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T1, E3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTOneEFour` | 94.5 | 2AFC accuracy (%), T1, E4, pooled |
| `\AfcPooledTOneEFourLo` | 91.2 | 2AFC accuracy (%), T1, E4, pooled, lower 95% CI bound |
| `\AfcPooledTOneEFourHi` | 97.3 | 2AFC accuracy (%), T1, E4, pooled, upper 95% CI bound |
| `\AfcPooledTOneEFourCI` | [91.2, 97.3] | 2AFC accuracy (%), T1, E4, pooled, 95% CI |
| `\AfcPooledTOneEFourN` | 292 | 2AFC accuracy (%), T1, E4, pooled, n |
| `\AfcPooledTOneEFourP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T1, E4, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTOneEFive` | 80.1 | 2AFC accuracy (%), T1, E5, pooled |
| `\AfcPooledTOneEFiveLo` | 73.4 | 2AFC accuracy (%), T1, E5, pooled, lower 95% CI bound |
| `\AfcPooledTOneEFiveHi` | 86.6 | 2AFC accuracy (%), T1, E5, pooled, upper 95% CI bound |
| `\AfcPooledTOneEFiveCI` | [73.4, 86.6] | 2AFC accuracy (%), T1, E5, pooled, 95% CI |
| `\AfcPooledTOneEFiveN` | 272 | 2AFC accuracy (%), T1, E5, pooled, n |
| `\AfcPooledTOneEFiveP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T1, E5, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTTwo` | 80.8 | 2AFC accuracy (%), T2, pooled |
| `\AfcPooledTTwoLo` | 78.3 | 2AFC accuracy (%), T2, pooled, lower 95% CI bound |
| `\AfcPooledTTwoHi` | 83.4 | 2AFC accuracy (%), T2, pooled, upper 95% CI bound |
| `\AfcPooledTTwoCI` | [78.3, 83.4] | 2AFC accuracy (%), T2, pooled, 95% CI |
| `\AfcPooledTTwoN` | 1{,}433 | 2AFC accuracy (%), T2, pooled, n |
| `\AfcPooledTTwoP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTTwoEOne` | 52.8 | 2AFC accuracy (%), T2, E1, pooled |
| `\AfcPooledTTwoEOneLo` | 41.5 | 2AFC accuracy (%), T2, E1, pooled, lower 95% CI bound |
| `\AfcPooledTTwoEOneHi` | 63.5 | 2AFC accuracy (%), T2, E1, pooled, upper 95% CI bound |
| `\AfcPooledTTwoEOneCI` | [41.5, 63.5] | 2AFC accuracy (%), T2, E1, pooled, 95% CI |
| `\AfcPooledTTwoEOneN` | 290 | 2AFC accuracy (%), T2, E1, pooled, n |
| `\AfcPooledTTwoEOneP` | 0.651 | 2AFC accuracy (%), T2, E1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTTwoETwo` | 86.4 | 2AFC accuracy (%), T2, E2, pooled |
| `\AfcPooledTTwoETwoLo` | 80.8 | 2AFC accuracy (%), T2, E2, pooled, lower 95% CI bound |
| `\AfcPooledTTwoETwoHi` | 91.4 | 2AFC accuracy (%), T2, E2, pooled, upper 95% CI bound |
| `\AfcPooledTTwoETwoCI` | [80.8, 91.4] | 2AFC accuracy (%), T2, E2, pooled, 95% CI |
| `\AfcPooledTTwoETwoN` | 280 | 2AFC accuracy (%), T2, E2, pooled, n |
| `\AfcPooledTTwoETwoP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T2, E2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTTwoEThree` | 85.9 | 2AFC accuracy (%), T2, E3, pooled |
| `\AfcPooledTTwoEThreeLo` | 80.8 | 2AFC accuracy (%), T2, E3, pooled, lower 95% CI bound |
| `\AfcPooledTTwoEThreeHi` | 90.6 | 2AFC accuracy (%), T2, E3, pooled, upper 95% CI bound |
| `\AfcPooledTTwoEThreeCI` | [80.8, 90.6] | 2AFC accuracy (%), T2, E3, pooled, 95% CI |
| `\AfcPooledTTwoEThreeN` | 291 | 2AFC accuracy (%), T2, E3, pooled, n |
| `\AfcPooledTTwoEThreeP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T2, E3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTTwoEFour` | 93.1 | 2AFC accuracy (%), T2, E4, pooled |
| `\AfcPooledTTwoEFourLo` | 89.4 | 2AFC accuracy (%), T2, E4, pooled, lower 95% CI bound |
| `\AfcPooledTTwoEFourHi` | 96.6 | 2AFC accuracy (%), T2, E4, pooled, upper 95% CI bound |
| `\AfcPooledTTwoEFourCI` | [89.4, 96.6] | 2AFC accuracy (%), T2, E4, pooled, 95% CI |
| `\AfcPooledTTwoEFourN` | 291 | 2AFC accuracy (%), T2, E4, pooled, n |
| `\AfcPooledTTwoEFourP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T2, E4, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTTwoEFive` | 86.1 | 2AFC accuracy (%), T2, E5, pooled |
| `\AfcPooledTTwoEFiveLo` | 80.1 | 2AFC accuracy (%), T2, E5, pooled, lower 95% CI bound |
| `\AfcPooledTTwoEFiveHi` | 91.8 | 2AFC accuracy (%), T2, E5, pooled, upper 95% CI bound |
| `\AfcPooledTTwoEFiveCI` | [80.1, 91.8] | 2AFC accuracy (%), T2, E5, pooled, 95% CI |
| `\AfcPooledTTwoEFiveN` | 281 | 2AFC accuracy (%), T2, E5, pooled, n |
| `\AfcPooledTTwoEFiveP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T2, E5, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTThree` | 79.7 | 2AFC accuracy (%), T3, pooled |
| `\AfcPooledTThreeLo` | 77.0 | 2AFC accuracy (%), T3, pooled, lower 95% CI bound |
| `\AfcPooledTThreeHi` | 82.8 | 2AFC accuracy (%), T3, pooled, upper 95% CI bound |
| `\AfcPooledTThreeCI` | [77.0, 82.8] | 2AFC accuracy (%), T3, pooled, 95% CI |
| `\AfcPooledTThreeN` | 1{,}440 | 2AFC accuracy (%), T3, pooled, n |
| `\AfcPooledTThreeP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTThreeEOne` | 49.1 | 2AFC accuracy (%), T3, E1, pooled |
| `\AfcPooledTThreeEOneLo` | 37.1 | 2AFC accuracy (%), T3, E1, pooled, lower 95% CI bound |
| `\AfcPooledTThreeEOneHi` | 61.2 | 2AFC accuracy (%), T3, E1, pooled, upper 95% CI bound |
| `\AfcPooledTThreeEOneCI` | [37.1, 61.2] | 2AFC accuracy (%), T3, E1, pooled, 95% CI |
| `\AfcPooledTThreeEOneN` | 289 | 2AFC accuracy (%), T3, E1, pooled, n |
| `\AfcPooledTThreeEOneP` | 0.914 | 2AFC accuracy (%), T3, E1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTThreeETwo` | 86.3 | 2AFC accuracy (%), T3, E2, pooled |
| `\AfcPooledTThreeETwoLo` | 80.8 | 2AFC accuracy (%), T3, E2, pooled, lower 95% CI bound |
| `\AfcPooledTThreeETwoHi` | 91.5 | 2AFC accuracy (%), T3, E2, pooled, upper 95% CI bound |
| `\AfcPooledTThreeETwoCI` | [80.8, 91.5] | 2AFC accuracy (%), T3, E2, pooled, 95% CI |
| `\AfcPooledTThreeETwoN` | 285 | 2AFC accuracy (%), T3, E2, pooled, n |
| `\AfcPooledTThreeETwoP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T3, E2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTThreeEThree` | 83.7 | 2AFC accuracy (%), T3, E3, pooled |
| `\AfcPooledTThreeEThreeLo` | 78.4 | 2AFC accuracy (%), T3, E3, pooled, lower 95% CI bound |
| `\AfcPooledTThreeEThreeHi` | 88.9 | 2AFC accuracy (%), T3, E3, pooled, upper 95% CI bound |
| `\AfcPooledTThreeEThreeCI` | [78.4, 88.9] | 2AFC accuracy (%), T3, E3, pooled, 95% CI |
| `\AfcPooledTThreeEThreeN` | 289 | 2AFC accuracy (%), T3, E3, pooled, n |
| `\AfcPooledTThreeEThreeP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T3, E3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTThreeEFour` | 91.7 | 2AFC accuracy (%), T3, E4, pooled |
| `\AfcPooledTThreeEFourLo` | 86.8 | 2AFC accuracy (%), T3, E4, pooled, lower 95% CI bound |
| `\AfcPooledTThreeEFourHi` | 95.9 | 2AFC accuracy (%), T3, E4, pooled, upper 95% CI bound |
| `\AfcPooledTThreeEFourCI` | [86.8, 95.9] | 2AFC accuracy (%), T3, E4, pooled, 95% CI |
| `\AfcPooledTThreeEFourN` | 289 | 2AFC accuracy (%), T3, E4, pooled, n |
| `\AfcPooledTThreeEFourP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T3, E4, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcPooledTThreeEFive` | 87.8 | 2AFC accuracy (%), T3, E5, pooled |
| `\AfcPooledTThreeEFiveLo` | 82.0 | 2AFC accuracy (%), T3, E5, pooled, lower 95% CI bound |
| `\AfcPooledTThreeEFiveHi` | 93.1 | 2AFC accuracy (%), T3, E5, pooled, upper 95% CI bound |
| `\AfcPooledTThreeEFiveCI` | [82.0, 93.1] | 2AFC accuracy (%), T3, E5, pooled, 95% CI |
| `\AfcPooledTThreeEFiveN` | 288 | 2AFC accuracy (%), T3, E5, pooled, n |
| `\AfcPooledTThreeEFiveP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T3, E5, pooled, two-sided bootstrap p (n/a if not tested) |
| `\AfcDeepSeekVFourFlashTZero` | 80.3 | 2AFC accuracy (%), T0, deepseek-v4-flash |
| `\AfcDeepSeekVFourFlashTZeroLo` | 75.7 | 2AFC accuracy (%), T0, deepseek-v4-flash, lower 95% CI bound |
| `\AfcDeepSeekVFourFlashTZeroHi` | 84.7 | 2AFC accuracy (%), T0, deepseek-v4-flash, upper 95% CI bound |
| `\AfcDeepSeekVFourFlashTZeroCI` | [75.7, 84.7] | 2AFC accuracy (%), T0, deepseek-v4-flash, 95% CI |
| `\AfcDeepSeekVFourFlashTZeroN` | 300 | 2AFC accuracy (%), T0, deepseek-v4-flash, n |
| `\AfcDeepSeekVFourFlashTZeroP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\AfcDeepSeekVFourFlashTOne` | 72.7 | 2AFC accuracy (%), T1, deepseek-v4-flash |
| `\AfcDeepSeekVFourFlashTOneLo` | 68.3 | 2AFC accuracy (%), T1, deepseek-v4-flash, lower 95% CI bound |
| `\AfcDeepSeekVFourFlashTOneHi` | 77.4 | 2AFC accuracy (%), T1, deepseek-v4-flash, upper 95% CI bound |
| `\AfcDeepSeekVFourFlashTOneCI` | [68.3, 77.4] | 2AFC accuracy (%), T1, deepseek-v4-flash, 95% CI |
| `\AfcDeepSeekVFourFlashTOneN` | 297 | 2AFC accuracy (%), T1, deepseek-v4-flash, n |
| `\AfcDeepSeekVFourFlashTOneP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\AfcDeepSeekVFourFlashTTwo` | 72.5 | 2AFC accuracy (%), T2, deepseek-v4-flash |
| `\AfcDeepSeekVFourFlashTTwoLo` | 67.6 | 2AFC accuracy (%), T2, deepseek-v4-flash, lower 95% CI bound |
| `\AfcDeepSeekVFourFlashTTwoHi` | 77.5 | 2AFC accuracy (%), T2, deepseek-v4-flash, upper 95% CI bound |
| `\AfcDeepSeekVFourFlashTTwoCI` | [67.6, 77.5] | 2AFC accuracy (%), T2, deepseek-v4-flash, 95% CI |
| `\AfcDeepSeekVFourFlashTTwoN` | 298 | 2AFC accuracy (%), T2, deepseek-v4-flash, n |
| `\AfcDeepSeekVFourFlashTTwoP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\AfcDeepSeekVFourFlashTThree` | 74.0 | 2AFC accuracy (%), T3, deepseek-v4-flash |
| `\AfcDeepSeekVFourFlashTThreeLo` | 69.3 | 2AFC accuracy (%), T3, deepseek-v4-flash, lower 95% CI bound |
| `\AfcDeepSeekVFourFlashTThreeHi` | 78.3 | 2AFC accuracy (%), T3, deepseek-v4-flash, upper 95% CI bound |
| `\AfcDeepSeekVFourFlashTThreeCI` | [69.3, 78.3] | 2AFC accuracy (%), T3, deepseek-v4-flash, 95% CI |
| `\AfcDeepSeekVFourFlashTThreeN` | 300 | 2AFC accuracy (%), T3, deepseek-v4-flash, n |
| `\AfcDeepSeekVFourFlashTThreeP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\AfcQwenThreeEightTwoSevenBTZero` | 90.3 | 2AFC accuracy (%), T0, qwen3.8-27b |
| `\AfcQwenThreeEightTwoSevenBTZeroLo` | 87.7 | 2AFC accuracy (%), T0, qwen3.8-27b, lower 95% CI bound |
| `\AfcQwenThreeEightTwoSevenBTZeroHi` | 93.0 | 2AFC accuracy (%), T0, qwen3.8-27b, upper 95% CI bound |
| `\AfcQwenThreeEightTwoSevenBTZeroCI` | [87.7, 93.0] | 2AFC accuracy (%), T0, qwen3.8-27b, 95% CI |
| `\AfcQwenThreeEightTwoSevenBTZeroN` | 300 | 2AFC accuracy (%), T0, qwen3.8-27b, n |
| `\AfcQwenThreeEightTwoSevenBTZeroP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\AfcQwenThreeEightTwoSevenBTOne` | 76.1 | 2AFC accuracy (%), T1, qwen3.8-27b |
| `\AfcQwenThreeEightTwoSevenBTOneLo` | 72.0 | 2AFC accuracy (%), T1, qwen3.8-27b, lower 95% CI bound |
| `\AfcQwenThreeEightTwoSevenBTOneHi` | 79.9 | 2AFC accuracy (%), T1, qwen3.8-27b, upper 95% CI bound |
| `\AfcQwenThreeEightTwoSevenBTOneCI` | [72.0, 79.9] | 2AFC accuracy (%), T1, qwen3.8-27b, 95% CI |
| `\AfcQwenThreeEightTwoSevenBTOneN` | 284 | 2AFC accuracy (%), T1, qwen3.8-27b, n |
| `\AfcQwenThreeEightTwoSevenBTOneP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\AfcQwenThreeEightTwoSevenBTTwo` | 81.6 | 2AFC accuracy (%), T2, qwen3.8-27b |
| `\AfcQwenThreeEightTwoSevenBTTwoLo` | 77.9 | 2AFC accuracy (%), T2, qwen3.8-27b, lower 95% CI bound |
| `\AfcQwenThreeEightTwoSevenBTTwoHi` | 85.4 | 2AFC accuracy (%), T2, qwen3.8-27b, upper 95% CI bound |
| `\AfcQwenThreeEightTwoSevenBTTwoCI` | [77.9, 85.4] | 2AFC accuracy (%), T2, qwen3.8-27b, 95% CI |
| `\AfcQwenThreeEightTwoSevenBTTwoN` | 293 | 2AFC accuracy (%), T2, qwen3.8-27b, n |
| `\AfcQwenThreeEightTwoSevenBTTwoP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\AfcQwenThreeEightTwoSevenBTThree` | 79.5 | 2AFC accuracy (%), T3, qwen3.8-27b |
| `\AfcQwenThreeEightTwoSevenBTThreeLo` | 75.8 | 2AFC accuracy (%), T3, qwen3.8-27b, lower 95% CI bound |
| `\AfcQwenThreeEightTwoSevenBTThreeHi` | 83.3 | 2AFC accuracy (%), T3, qwen3.8-27b, upper 95% CI bound |
| `\AfcQwenThreeEightTwoSevenBTThreeCI` | [75.8, 83.3] | 2AFC accuracy (%), T3, qwen3.8-27b, 95% CI |
| `\AfcQwenThreeEightTwoSevenBTThreeN` | 298 | 2AFC accuracy (%), T3, qwen3.8-27b, n |
| `\AfcQwenThreeEightTwoSevenBTThreeP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\AfcGemmaFourThreeOneBTZero` | 90.0 | 2AFC accuracy (%), T0, gemma-4-31b-it |
| `\AfcGemmaFourThreeOneBTZeroLo` | 86.8 | 2AFC accuracy (%), T0, gemma-4-31b-it, lower 95% CI bound |
| `\AfcGemmaFourThreeOneBTZeroHi` | 92.9 | 2AFC accuracy (%), T0, gemma-4-31b-it, upper 95% CI bound |
| `\AfcGemmaFourThreeOneBTZeroCI` | [86.8, 92.9] | 2AFC accuracy (%), T0, gemma-4-31b-it, 95% CI |
| `\AfcGemmaFourThreeOneBTZeroN` | 280 | 2AFC accuracy (%), T0, gemma-4-31b-it, n |
| `\AfcGemmaFourThreeOneBTZeroP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\AfcGemmaFourThreeOneBTOne` | 79.9 | 2AFC accuracy (%), T1, gemma-4-31b-it |
| `\AfcGemmaFourThreeOneBTOneLo` | 76.1 | 2AFC accuracy (%), T1, gemma-4-31b-it, lower 95% CI bound |
| `\AfcGemmaFourThreeOneBTOneHi` | 83.5 | 2AFC accuracy (%), T1, gemma-4-31b-it, upper 95% CI bound |
| `\AfcGemmaFourThreeOneBTOneCI` | [76.1, 83.5] | 2AFC accuracy (%), T1, gemma-4-31b-it, 95% CI |
| `\AfcGemmaFourThreeOneBTOneN` | 279 | 2AFC accuracy (%), T1, gemma-4-31b-it, n |
| `\AfcGemmaFourThreeOneBTOneP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\AfcGemmaFourThreeOneBTTwo` | 81.8 | 2AFC accuracy (%), T2, gemma-4-31b-it |
| `\AfcGemmaFourThreeOneBTTwoLo` | 78.4 | 2AFC accuracy (%), T2, gemma-4-31b-it, lower 95% CI bound |
| `\AfcGemmaFourThreeOneBTTwoHi` | 85.0 | 2AFC accuracy (%), T2, gemma-4-31b-it, upper 95% CI bound |
| `\AfcGemmaFourThreeOneBTTwoCI` | [78.4, 85.0] | 2AFC accuracy (%), T2, gemma-4-31b-it, 95% CI |
| `\AfcGemmaFourThreeOneBTTwoN` | 269 | 2AFC accuracy (%), T2, gemma-4-31b-it, n |
| `\AfcGemmaFourThreeOneBTTwoP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\AfcGemmaFourThreeOneBTThree` | 79.4 | 2AFC accuracy (%), T3, gemma-4-31b-it |
| `\AfcGemmaFourThreeOneBTThreeLo` | 74.7 | 2AFC accuracy (%), T3, gemma-4-31b-it, lower 95% CI bound |
| `\AfcGemmaFourThreeOneBTThreeHi` | 84.2 | 2AFC accuracy (%), T3, gemma-4-31b-it, upper 95% CI bound |
| `\AfcGemmaFourThreeOneBTThreeCI` | [74.7, 84.2] | 2AFC accuracy (%), T3, gemma-4-31b-it, 95% CI |
| `\AfcGemmaFourThreeOneBTThreeN` | 277 | 2AFC accuracy (%), T3, gemma-4-31b-it, n |
| `\AfcGemmaFourThreeOneBTThreeP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\AfcGLMFiveThreeFlashTZero` | 91.3 | 2AFC accuracy (%), T0, glm-5.3-flash |
| `\AfcGLMFiveThreeFlashTZeroLo` | 88.7 | 2AFC accuracy (%), T0, glm-5.3-flash, lower 95% CI bound |
| `\AfcGLMFiveThreeFlashTZeroHi` | 93.7 | 2AFC accuracy (%), T0, glm-5.3-flash, upper 95% CI bound |
| `\AfcGLMFiveThreeFlashTZeroCI` | [88.7, 93.7] | 2AFC accuracy (%), T0, glm-5.3-flash, 95% CI |
| `\AfcGLMFiveThreeFlashTZeroN` | 300 | 2AFC accuracy (%), T0, glm-5.3-flash, n |
| `\AfcGLMFiveThreeFlashTZeroP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\AfcGLMFiveThreeFlashTOne` | 86.0 | 2AFC accuracy (%), T1, glm-5.3-flash |
| `\AfcGLMFiveThreeFlashTOneLo` | 83.6 | 2AFC accuracy (%), T1, glm-5.3-flash, lower 95% CI bound |
| `\AfcGLMFiveThreeFlashTOneHi` | 88.5 | 2AFC accuracy (%), T1, glm-5.3-flash, upper 95% CI bound |
| `\AfcGLMFiveThreeFlashTOneCI` | [83.6, 88.5] | 2AFC accuracy (%), T1, glm-5.3-flash, 95% CI |
| `\AfcGLMFiveThreeFlashTOneN` | 286 | 2AFC accuracy (%), T1, glm-5.3-flash, n |
| `\AfcGLMFiveThreeFlashTOneP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\AfcGLMFiveThreeFlashTTwo` | 87.6 | 2AFC accuracy (%), T2, glm-5.3-flash |
| `\AfcGLMFiveThreeFlashTTwoLo` | 84.3 | 2AFC accuracy (%), T2, glm-5.3-flash, lower 95% CI bound |
| `\AfcGLMFiveThreeFlashTTwoHi` | 90.9 | 2AFC accuracy (%), T2, glm-5.3-flash, upper 95% CI bound |
| `\AfcGLMFiveThreeFlashTTwoCI` | [84.3, 90.9] | 2AFC accuracy (%), T2, glm-5.3-flash, 95% CI |
| `\AfcGLMFiveThreeFlashTTwoN` | 274 | 2AFC accuracy (%), T2, glm-5.3-flash, n |
| `\AfcGLMFiveThreeFlashTTwoP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\AfcGLMFiveThreeFlashTThree` | 88.3 | 2AFC accuracy (%), T3, glm-5.3-flash |
| `\AfcGLMFiveThreeFlashTThreeLo` | 85.3 | 2AFC accuracy (%), T3, glm-5.3-flash, lower 95% CI bound |
| `\AfcGLMFiveThreeFlashTThreeHi` | 91.3 | 2AFC accuracy (%), T3, glm-5.3-flash, upper 95% CI bound |
| `\AfcGLMFiveThreeFlashTThreeCI` | [85.3, 91.3] | 2AFC accuracy (%), T3, glm-5.3-flash, 95% CI |
| `\AfcGLMFiveThreeFlashTThreeN` | 265 | 2AFC accuracy (%), T3, glm-5.3-flash, n |
| `\AfcGLMFiveThreeFlashTThreeP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\AfcGLMFiveTwoTZero` | 88.7 | 2AFC accuracy (%), T0, glm-5.2 |
| `\AfcGLMFiveTwoTZeroLo` | 86.0 | 2AFC accuracy (%), T0, glm-5.2, lower 95% CI bound |
| `\AfcGLMFiveTwoTZeroHi` | 91.3 | 2AFC accuracy (%), T0, glm-5.2, upper 95% CI bound |
| `\AfcGLMFiveTwoTZeroCI` | [86.0, 91.3] | 2AFC accuracy (%), T0, glm-5.2, 95% CI |
| `\AfcGLMFiveTwoTZeroN` | 300 | 2AFC accuracy (%), T0, glm-5.2, n |
| `\AfcGLMFiveTwoTZeroP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\AfcGLMFiveTwoTOne` | 78.5 | 2AFC accuracy (%), T1, glm-5.2 |
| `\AfcGLMFiveTwoTOneLo` | 74.4 | 2AFC accuracy (%), T1, glm-5.2, lower 95% CI bound |
| `\AfcGLMFiveTwoTOneHi` | 82.4 | 2AFC accuracy (%), T1, glm-5.2, upper 95% CI bound |
| `\AfcGLMFiveTwoTOneCI` | [74.4, 82.4] | 2AFC accuracy (%), T1, glm-5.2, 95% CI |
| `\AfcGLMFiveTwoTOneN` | 293 | 2AFC accuracy (%), T1, glm-5.2, n |
| `\AfcGLMFiveTwoTOneP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\AfcGLMFiveTwoTTwo` | 81.3 | 2AFC accuracy (%), T2, glm-5.2 |
| `\AfcGLMFiveTwoTTwoLo` | 77.4 | 2AFC accuracy (%), T2, glm-5.2, lower 95% CI bound |
| `\AfcGLMFiveTwoTTwoHi` | 84.7 | 2AFC accuracy (%), T2, glm-5.2, upper 95% CI bound |
| `\AfcGLMFiveTwoTTwoCI` | [77.4, 84.7] | 2AFC accuracy (%), T2, glm-5.2, 95% CI |
| `\AfcGLMFiveTwoTTwoN` | 299 | 2AFC accuracy (%), T2, glm-5.2, n |
| `\AfcGLMFiveTwoTTwoP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\AfcGLMFiveTwoTThree` | 78.3 | 2AFC accuracy (%), T3, glm-5.2 |
| `\AfcGLMFiveTwoTThreeLo` | 74.3 | 2AFC accuracy (%), T3, glm-5.2, lower 95% CI bound |
| `\AfcGLMFiveTwoTThreeHi` | 82.0 | 2AFC accuracy (%), T3, glm-5.2, upper 95% CI bound |
| `\AfcGLMFiveTwoTThreeCI` | [74.3, 82.0] | 2AFC accuracy (%), T3, glm-5.2, 95% CI |
| `\AfcGLMFiveTwoTThreeN` | 300 | 2AFC accuracy (%), T3, glm-5.2, n |
| `\AfcGLMFiveTwoTThreeP` | \ensuremath{<}0.001 | 2AFC accuracy (%), T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\JudgeAccuracyIdentical` | 100.0 | judge gold set: accuracy_identical |
| `\JudgeAccuracyIdenticalLo` | 99.8 | judge gold set: accuracy_identical, lower 95% CI bound |
| `\JudgeAccuracyIdenticalHi` | 100.0 | judge gold set: accuracy_identical, upper 95% CI bound |
| `\JudgeAccuracyIdenticalCI` | [99.8, 100.0] | judge gold set: accuracy_identical, 95% CI |
| `\JudgeAccuracyIdenticalN` | 2{,}019 | judge gold set: accuracy_identical, n |
| `\JudgeAccuracyIdenticalP` | n/a | judge gold set: accuracy_identical, two-sided bootstrap p (n/a if not tested) |
| `\JudgeAnyFlagIdentical` | 0.0 | judge gold set: any_flag_identical |
| `\JudgeAnyFlagIdenticalLo` | 0.0 | judge gold set: any_flag_identical, lower 95% CI bound |
| `\JudgeAnyFlagIdenticalHi` | 0.2 | judge gold set: any_flag_identical, upper 95% CI bound |
| `\JudgeAnyFlagIdenticalCI` | [0.0, 0.2] | judge gold set: any_flag_identical, 95% CI |
| `\JudgeAnyFlagIdenticalN` | 2{,}019 | judge gold set: any_flag_identical, n |
| `\JudgeAnyFlagIdenticalP` | n/a | judge gold set: any_flag_identical, two-sided bootstrap p (n/a if not tested) |
| `\JudgeAccuracyResampled` | 56.8 | judge gold set: accuracy_resampled |
| `\JudgeAccuracyResampledLo` | 54.4 | judge gold set: accuracy_resampled, lower 95% CI bound |
| `\JudgeAccuracyResampledHi` | 59.3 | judge gold set: accuracy_resampled, upper 95% CI bound |
| `\JudgeAccuracyResampledCI` | [54.4, 59.3] | judge gold set: accuracy_resampled, 95% CI |
| `\JudgeAccuracyResampledN` | 2{,}087 | judge gold set: accuracy_resampled, n |
| `\JudgeAccuracyResampledP` | n/a | judge gold set: accuracy_resampled, two-sided bootstrap p (n/a if not tested) |
| `\JudgeAnyFlagResampled` | 43.9 | judge gold set: any_flag_resampled |
| `\JudgeAnyFlagResampledLo` | 41.3 | judge gold set: any_flag_resampled, lower 95% CI bound |
| `\JudgeAnyFlagResampledHi` | 46.4 | judge gold set: any_flag_resampled, upper 95% CI bound |
| `\JudgeAnyFlagResampledCI` | [41.3, 46.4] | judge gold set: any_flag_resampled, 95% CI |
| `\JudgeAnyFlagResampledN` | 2{,}087 | judge gold set: any_flag_resampled, n |
| `\JudgeAnyFlagResampledP` | n/a | judge gold set: any_flag_resampled, two-sided bootstrap p (n/a if not tested) |
| `\JudgeAccuracyTZero` | 99.8 | judge gold set: accuracy_T0 |
| `\JudgeAccuracyTZeroLo` | 99.5 | judge gold set: accuracy_T0, lower 95% CI bound |
| `\JudgeAccuracyTZeroHi` | 100.0 | judge gold set: accuracy_T0, upper 95% CI bound |
| `\JudgeAccuracyTZeroCI` | [99.5, 100.0] | judge gold set: accuracy_T0, 95% CI |
| `\JudgeAccuracyTZeroN` | 1{,}486 | judge gold set: accuracy_T0, n |
| `\JudgeAccuracyTZeroP` | n/a | judge gold set: accuracy_T0, two-sided bootstrap p (n/a if not tested) |
| `\JudgeAnyFlagTZero` | 99.8 | judge gold set: any_flag_T0 |
| `\JudgeAnyFlagTZeroLo` | 99.5 | judge gold set: any_flag_T0, lower 95% CI bound |
| `\JudgeAnyFlagTZeroHi` | 100.0 | judge gold set: any_flag_T0, upper 95% CI bound |
| `\JudgeAnyFlagTZeroCI` | [99.5, 100.0] | judge gold set: any_flag_T0, 95% CI |
| `\JudgeAnyFlagTZeroN` | 1{,}486 | judge gold set: any_flag_T0, n |
| `\JudgeAnyFlagTZeroP` | n/a | judge gold set: any_flag_T0, two-sided bootstrap p (n/a if not tested) |
| `\JudgeAurocTZeroVsResampled` | 0.94 | judge gold set: auroc_T0_vs_resampled |
| `\JudgeAurocTZeroVsResampledLo` | 0.93 | judge gold set: auroc_T0_vs_resampled, lower 95% CI bound |
| `\JudgeAurocTZeroVsResampledHi` | 0.95 | judge gold set: auroc_T0_vs_resampled, upper 95% CI bound |
| `\JudgeAurocTZeroVsResampledCI` | [0.93, 0.95] | judge gold set: auroc_T0_vs_resampled, 95% CI |
| `\JudgeAurocTZeroVsResampledN` | 3{,}573 | judge gold set: auroc_T0_vs_resampled, n |
| `\JudgeAurocTZeroVsResampledP` | \ensuremath{<}0.001 | judge gold set: auroc_T0_vs_resampled, two-sided bootstrap p (n/a if not tested) |
| `\JudgeAurocTZeroVsIdentical` | 1.00 | judge gold set: auroc_T0_vs_identical |
| `\JudgeAurocTZeroVsIdenticalLo` | 1.00 | judge gold set: auroc_T0_vs_identical, lower 95% CI bound |
| `\JudgeAurocTZeroVsIdenticalHi` | 1.00 | judge gold set: auroc_T0_vs_identical, upper 95% CI bound |
| `\JudgeAurocTZeroVsIdenticalCI` | [1.00, 1.00] | judge gold set: auroc_T0_vs_identical, 95% CI |
| `\JudgeAurocTZeroVsIdenticalN` | 3{,}505 | judge gold set: auroc_T0_vs_identical, n |
| `\JudgeAurocTZeroVsIdenticalP` | \ensuremath{<}0.001 | judge gold set: auroc_T0_vs_identical, two-sided bootstrap p (n/a if not tested) |
| `\JudgeFlagHitEOne` | 99.0 | judge gold set: flag_hit_E1 |
| `\JudgeFlagHitEOneLo` | 97.3 | judge gold set: flag_hit_E1, lower 95% CI bound |
| `\JudgeFlagHitEOneHi` | 100.0 | judge gold set: flag_hit_E1, upper 95% CI bound |
| `\JudgeFlagHitEOneCI` | [97.3, 100.0] | judge gold set: flag_hit_E1, 95% CI |
| `\JudgeFlagHitEOneN` | 297 | judge gold set: flag_hit_E1, n |
| `\JudgeFlagHitEOneP` | n/a | judge gold set: flag_hit_E1, two-sided bootstrap p (n/a if not tested) |
| `\JudgeFlagHitETwo` | 100.0 | judge gold set: flag_hit_E2 |
| `\JudgeFlagHitETwoLo` | 98.8 | judge gold set: flag_hit_E2, lower 95% CI bound |
| `\JudgeFlagHitETwoHi` | 100.0 | judge gold set: flag_hit_E2, upper 95% CI bound |
| `\JudgeFlagHitETwoCI` | [98.8, 100.0] | judge gold set: flag_hit_E2, 95% CI |
| `\JudgeFlagHitETwoN` | 296 | judge gold set: flag_hit_E2, n |
| `\JudgeFlagHitETwoP` | n/a | judge gold set: flag_hit_E2, two-sided bootstrap p (n/a if not tested) |
| `\JudgeFlagHitEThree` | 100.0 | judge gold set: flag_hit_E3 |
| `\JudgeFlagHitEThreeLo` | 98.8 | judge gold set: flag_hit_E3, lower 95% CI bound |
| `\JudgeFlagHitEThreeHi` | 100.0 | judge gold set: flag_hit_E3, upper 95% CI bound |
| `\JudgeFlagHitEThreeCI` | [98.8, 100.0] | judge gold set: flag_hit_E3, 95% CI |
| `\JudgeFlagHitEThreeN` | 298 | judge gold set: flag_hit_E3, n |
| `\JudgeFlagHitEThreeP` | n/a | judge gold set: flag_hit_E3, two-sided bootstrap p (n/a if not tested) |
| `\JudgeFlagHitEFour` | 100.0 | judge gold set: flag_hit_E4 |
| `\JudgeFlagHitEFourLo` | 98.8 | judge gold set: flag_hit_E4, lower 95% CI bound |
| `\JudgeFlagHitEFourHi` | 100.0 | judge gold set: flag_hit_E4, upper 95% CI bound |
| `\JudgeFlagHitEFourCI` | [98.8, 100.0] | judge gold set: flag_hit_E4, 95% CI |
| `\JudgeFlagHitEFourN` | 297 | judge gold set: flag_hit_E4, n |
| `\JudgeFlagHitEFourP` | n/a | judge gold set: flag_hit_E4, two-sided bootstrap p (n/a if not tested) |
| `\JudgeFlagHitEFive` | 100.0 | judge gold set: flag_hit_E5 |
| `\JudgeFlagHitEFiveLo` | 98.8 | judge gold set: flag_hit_E5, lower 95% CI bound |
| `\JudgeFlagHitEFiveHi` | 100.0 | judge gold set: flag_hit_E5, upper 95% CI bound |
| `\JudgeFlagHitEFiveCI` | [98.8, 100.0] | judge gold set: flag_hit_E5, 95% CI |
| `\JudgeFlagHitEFiveN` | 298 | judge gold set: flag_hit_E5, n |
| `\JudgeFlagHitEFiveP` | n/a | judge gold set: flag_hit_E5, two-sided bootstrap p (n/a if not tested) |
| `\ValidDeepSeekVFourFlashTZero` | 100.0 | % valid forgeries, T0, deepseek-v4-flash |
| `\ValidDeepSeekVFourFlashTZeroLo` | 98.8 | % valid forgeries, T0, deepseek-v4-flash, lower 95% CI bound |
| `\ValidDeepSeekVFourFlashTZeroHi` | 100.0 | % valid forgeries, T0, deepseek-v4-flash, upper 95% CI bound |
| `\ValidDeepSeekVFourFlashTZeroCI` | [98.8, 100.0] | % valid forgeries, T0, deepseek-v4-flash, 95% CI |
| `\ValidDeepSeekVFourFlashTZeroN` | 300 | % valid forgeries, T0, deepseek-v4-flash, n |
| `\ValidDeepSeekVFourFlashTZeroP` | n/a | % valid forgeries, T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\ValidDeepSeekVFourFlashTOne` | 99.0 | % valid forgeries, T1, deepseek-v4-flash |
| `\ValidDeepSeekVFourFlashTOneLo` | 97.7 | % valid forgeries, T1, deepseek-v4-flash, lower 95% CI bound |
| `\ValidDeepSeekVFourFlashTOneHi` | 100.0 | % valid forgeries, T1, deepseek-v4-flash, upper 95% CI bound |
| `\ValidDeepSeekVFourFlashTOneCI` | [97.7, 100.0] | % valid forgeries, T1, deepseek-v4-flash, 95% CI |
| `\ValidDeepSeekVFourFlashTOneN` | 300 | % valid forgeries, T1, deepseek-v4-flash, n |
| `\ValidDeepSeekVFourFlashTOneP` | n/a | % valid forgeries, T1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\ValidDeepSeekVFourFlashTTwo` | 99.3 | % valid forgeries, T2, deepseek-v4-flash |
| `\ValidDeepSeekVFourFlashTTwoLo` | 98.3 | % valid forgeries, T2, deepseek-v4-flash, lower 95% CI bound |
| `\ValidDeepSeekVFourFlashTTwoHi` | 100.0 | % valid forgeries, T2, deepseek-v4-flash, upper 95% CI bound |
| `\ValidDeepSeekVFourFlashTTwoCI` | [98.3, 100.0] | % valid forgeries, T2, deepseek-v4-flash, 95% CI |
| `\ValidDeepSeekVFourFlashTTwoN` | 300 | % valid forgeries, T2, deepseek-v4-flash, n |
| `\ValidDeepSeekVFourFlashTTwoP` | n/a | % valid forgeries, T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\ValidDeepSeekVFourFlashTThree` | 100.0 | % valid forgeries, T3, deepseek-v4-flash |
| `\ValidDeepSeekVFourFlashTThreeLo` | 98.8 | % valid forgeries, T3, deepseek-v4-flash, lower 95% CI bound |
| `\ValidDeepSeekVFourFlashTThreeHi` | 100.0 | % valid forgeries, T3, deepseek-v4-flash, upper 95% CI bound |
| `\ValidDeepSeekVFourFlashTThreeCI` | [98.8, 100.0] | % valid forgeries, T3, deepseek-v4-flash, 95% CI |
| `\ValidDeepSeekVFourFlashTThreeN` | 300 | % valid forgeries, T3, deepseek-v4-flash, n |
| `\ValidDeepSeekVFourFlashTThreeP` | n/a | % valid forgeries, T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\ValidQwenThreeEightTwoSevenBTZero` | 100.0 | % valid forgeries, T0, qwen3.8-27b |
| `\ValidQwenThreeEightTwoSevenBTZeroLo` | 98.8 | % valid forgeries, T0, qwen3.8-27b, lower 95% CI bound |
| `\ValidQwenThreeEightTwoSevenBTZeroHi` | 100.0 | % valid forgeries, T0, qwen3.8-27b, upper 95% CI bound |
| `\ValidQwenThreeEightTwoSevenBTZeroCI` | [98.8, 100.0] | % valid forgeries, T0, qwen3.8-27b, 95% CI |
| `\ValidQwenThreeEightTwoSevenBTZeroN` | 300 | % valid forgeries, T0, qwen3.8-27b, n |
| `\ValidQwenThreeEightTwoSevenBTZeroP` | n/a | % valid forgeries, T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\ValidQwenThreeEightTwoSevenBTOne` | 97.7 | % valid forgeries, T1, qwen3.8-27b |
| `\ValidQwenThreeEightTwoSevenBTOneLo` | 96.0 | % valid forgeries, T1, qwen3.8-27b, lower 95% CI bound |
| `\ValidQwenThreeEightTwoSevenBTOneHi` | 99.3 | % valid forgeries, T1, qwen3.8-27b, upper 95% CI bound |
| `\ValidQwenThreeEightTwoSevenBTOneCI` | [96.0, 99.3] | % valid forgeries, T1, qwen3.8-27b, 95% CI |
| `\ValidQwenThreeEightTwoSevenBTOneN` | 300 | % valid forgeries, T1, qwen3.8-27b, n |
| `\ValidQwenThreeEightTwoSevenBTOneP` | n/a | % valid forgeries, T1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\ValidQwenThreeEightTwoSevenBTTwo` | 97.7 | % valid forgeries, T2, qwen3.8-27b |
| `\ValidQwenThreeEightTwoSevenBTTwoLo` | 96.0 | % valid forgeries, T2, qwen3.8-27b, lower 95% CI bound |
| `\ValidQwenThreeEightTwoSevenBTTwoHi` | 99.3 | % valid forgeries, T2, qwen3.8-27b, upper 95% CI bound |
| `\ValidQwenThreeEightTwoSevenBTTwoCI` | [96.0, 99.3] | % valid forgeries, T2, qwen3.8-27b, 95% CI |
| `\ValidQwenThreeEightTwoSevenBTTwoN` | 300 | % valid forgeries, T2, qwen3.8-27b, n |
| `\ValidQwenThreeEightTwoSevenBTTwoP` | n/a | % valid forgeries, T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\ValidQwenThreeEightTwoSevenBTThree` | 99.3 | % valid forgeries, T3, qwen3.8-27b |
| `\ValidQwenThreeEightTwoSevenBTThreeLo` | 98.3 | % valid forgeries, T3, qwen3.8-27b, lower 95% CI bound |
| `\ValidQwenThreeEightTwoSevenBTThreeHi` | 100.0 | % valid forgeries, T3, qwen3.8-27b, upper 95% CI bound |
| `\ValidQwenThreeEightTwoSevenBTThreeCI` | [98.3, 100.0] | % valid forgeries, T3, qwen3.8-27b, 95% CI |
| `\ValidQwenThreeEightTwoSevenBTThreeN` | 300 | % valid forgeries, T3, qwen3.8-27b, n |
| `\ValidQwenThreeEightTwoSevenBTThreeP` | n/a | % valid forgeries, T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\ValidGemmaFourThreeOneBTZero` | 100.0 | % valid forgeries, T0, gemma-4-31b-it |
| `\ValidGemmaFourThreeOneBTZeroLo` | 98.8 | % valid forgeries, T0, gemma-4-31b-it, lower 95% CI bound |
| `\ValidGemmaFourThreeOneBTZeroHi` | 100.0 | % valid forgeries, T0, gemma-4-31b-it, upper 95% CI bound |
| `\ValidGemmaFourThreeOneBTZeroCI` | [98.8, 100.0] | % valid forgeries, T0, gemma-4-31b-it, 95% CI |
| `\ValidGemmaFourThreeOneBTZeroN` | 298 | % valid forgeries, T0, gemma-4-31b-it, n |
| `\ValidGemmaFourThreeOneBTZeroP` | n/a | % valid forgeries, T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\ValidGemmaFourThreeOneBTOne` | 99.7 | % valid forgeries, T1, gemma-4-31b-it |
| `\ValidGemmaFourThreeOneBTOneLo` | 99.0 | % valid forgeries, T1, gemma-4-31b-it, lower 95% CI bound |
| `\ValidGemmaFourThreeOneBTOneHi` | 100.0 | % valid forgeries, T1, gemma-4-31b-it, upper 95% CI bound |
| `\ValidGemmaFourThreeOneBTOneCI` | [99.0, 100.0] | % valid forgeries, T1, gemma-4-31b-it, 95% CI |
| `\ValidGemmaFourThreeOneBTOneN` | 298 | % valid forgeries, T1, gemma-4-31b-it, n |
| `\ValidGemmaFourThreeOneBTOneP` | n/a | % valid forgeries, T1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\ValidGemmaFourThreeOneBTTwo` | 96.3 | % valid forgeries, T2, gemma-4-31b-it |
| `\ValidGemmaFourThreeOneBTTwoLo` | 94.0 | % valid forgeries, T2, gemma-4-31b-it, lower 95% CI bound |
| `\ValidGemmaFourThreeOneBTTwoHi` | 98.3 | % valid forgeries, T2, gemma-4-31b-it, upper 95% CI bound |
| `\ValidGemmaFourThreeOneBTTwoCI` | [94.0, 98.3] | % valid forgeries, T2, gemma-4-31b-it, 95% CI |
| `\ValidGemmaFourThreeOneBTTwoN` | 298 | % valid forgeries, T2, gemma-4-31b-it, n |
| `\ValidGemmaFourThreeOneBTTwoP` | n/a | % valid forgeries, T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\ValidGemmaFourThreeOneBTThree` | 99.0 | % valid forgeries, T3, gemma-4-31b-it |
| `\ValidGemmaFourThreeOneBTThreeLo` | 97.7 | % valid forgeries, T3, gemma-4-31b-it, lower 95% CI bound |
| `\ValidGemmaFourThreeOneBTThreeHi` | 100.0 | % valid forgeries, T3, gemma-4-31b-it, upper 95% CI bound |
| `\ValidGemmaFourThreeOneBTThreeCI` | [97.7, 100.0] | % valid forgeries, T3, gemma-4-31b-it, 95% CI |
| `\ValidGemmaFourThreeOneBTThreeN` | 298 | % valid forgeries, T3, gemma-4-31b-it, n |
| `\ValidGemmaFourThreeOneBTThreeP` | n/a | % valid forgeries, T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\ValidGLMFiveThreeFlashTZero` | 100.0 | % valid forgeries, T0, glm-5.3-flash |
| `\ValidGLMFiveThreeFlashTZeroLo` | 98.8 | % valid forgeries, T0, glm-5.3-flash, lower 95% CI bound |
| `\ValidGLMFiveThreeFlashTZeroHi` | 100.0 | % valid forgeries, T0, glm-5.3-flash, upper 95% CI bound |
| `\ValidGLMFiveThreeFlashTZeroCI` | [98.8, 100.0] | % valid forgeries, T0, glm-5.3-flash, 95% CI |
| `\ValidGLMFiveThreeFlashTZeroN` | 300 | % valid forgeries, T0, glm-5.3-flash, n |
| `\ValidGLMFiveThreeFlashTZeroP` | n/a | % valid forgeries, T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\ValidGLMFiveThreeFlashTOne` | 98.7 | % valid forgeries, T1, glm-5.3-flash |
| `\ValidGLMFiveThreeFlashTOneLo` | 97.3 | % valid forgeries, T1, glm-5.3-flash, lower 95% CI bound |
| `\ValidGLMFiveThreeFlashTOneHi` | 99.7 | % valid forgeries, T1, glm-5.3-flash, upper 95% CI bound |
| `\ValidGLMFiveThreeFlashTOneCI` | [97.3, 99.7] | % valid forgeries, T1, glm-5.3-flash, 95% CI |
| `\ValidGLMFiveThreeFlashTOneN` | 300 | % valid forgeries, T1, glm-5.3-flash, n |
| `\ValidGLMFiveThreeFlashTOneP` | n/a | % valid forgeries, T1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\ValidGLMFiveThreeFlashTTwo` | 99.7 | % valid forgeries, T2, glm-5.3-flash |
| `\ValidGLMFiveThreeFlashTTwoLo` | 99.0 | % valid forgeries, T2, glm-5.3-flash, lower 95% CI bound |
| `\ValidGLMFiveThreeFlashTTwoHi` | 100.0 | % valid forgeries, T2, glm-5.3-flash, upper 95% CI bound |
| `\ValidGLMFiveThreeFlashTTwoCI` | [99.0, 100.0] | % valid forgeries, T2, glm-5.3-flash, 95% CI |
| `\ValidGLMFiveThreeFlashTTwoN` | 300 | % valid forgeries, T2, glm-5.3-flash, n |
| `\ValidGLMFiveThreeFlashTTwoP` | n/a | % valid forgeries, T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\ValidGLMFiveThreeFlashTThree` | 100.0 | % valid forgeries, T3, glm-5.3-flash |
| `\ValidGLMFiveThreeFlashTThreeLo` | 98.8 | % valid forgeries, T3, glm-5.3-flash, lower 95% CI bound |
| `\ValidGLMFiveThreeFlashTThreeHi` | 100.0 | % valid forgeries, T3, glm-5.3-flash, upper 95% CI bound |
| `\ValidGLMFiveThreeFlashTThreeCI` | [98.8, 100.0] | % valid forgeries, T3, glm-5.3-flash, 95% CI |
| `\ValidGLMFiveThreeFlashTThreeN` | 300 | % valid forgeries, T3, glm-5.3-flash, n |
| `\ValidGLMFiveThreeFlashTThreeP` | n/a | % valid forgeries, T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\ValidGLMFiveTwoTZero` | 100.0 | % valid forgeries, T0, glm-5.2 |
| `\ValidGLMFiveTwoTZeroLo` | 98.8 | % valid forgeries, T0, glm-5.2, lower 95% CI bound |
| `\ValidGLMFiveTwoTZeroHi` | 100.0 | % valid forgeries, T0, glm-5.2, upper 95% CI bound |
| `\ValidGLMFiveTwoTZeroCI` | [98.8, 100.0] | % valid forgeries, T0, glm-5.2, 95% CI |
| `\ValidGLMFiveTwoTZeroN` | 300 | % valid forgeries, T0, glm-5.2, n |
| `\ValidGLMFiveTwoTZeroP` | n/a | % valid forgeries, T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\ValidGLMFiveTwoTOne` | 97.7 | % valid forgeries, T1, glm-5.2 |
| `\ValidGLMFiveTwoTOneLo` | 96.0 | % valid forgeries, T1, glm-5.2, lower 95% CI bound |
| `\ValidGLMFiveTwoTOneHi` | 99.3 | % valid forgeries, T1, glm-5.2, upper 95% CI bound |
| `\ValidGLMFiveTwoTOneCI` | [96.0, 99.3] | % valid forgeries, T1, glm-5.2, 95% CI |
| `\ValidGLMFiveTwoTOneN` | 300 | % valid forgeries, T1, glm-5.2, n |
| `\ValidGLMFiveTwoTOneP` | n/a | % valid forgeries, T1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\ValidGLMFiveTwoTTwo` | 99.7 | % valid forgeries, T2, glm-5.2 |
| `\ValidGLMFiveTwoTTwoLo` | 99.0 | % valid forgeries, T2, glm-5.2, lower 95% CI bound |
| `\ValidGLMFiveTwoTTwoHi` | 100.0 | % valid forgeries, T2, glm-5.2, upper 95% CI bound |
| `\ValidGLMFiveTwoTTwoCI` | [99.0, 100.0] | % valid forgeries, T2, glm-5.2, 95% CI |
| `\ValidGLMFiveTwoTTwoN` | 300 | % valid forgeries, T2, glm-5.2, n |
| `\ValidGLMFiveTwoTTwoP` | n/a | % valid forgeries, T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\ValidGLMFiveTwoTThree` | 100.0 | % valid forgeries, T3, glm-5.2 |
| `\ValidGLMFiveTwoTThreeLo` | 98.8 | % valid forgeries, T3, glm-5.2, lower 95% CI bound |
| `\ValidGLMFiveTwoTThreeHi` | 100.0 | % valid forgeries, T3, glm-5.2, upper 95% CI bound |
| `\ValidGLMFiveTwoTThreeCI` | [98.8, 100.0] | % valid forgeries, T3, glm-5.2, 95% CI |
| `\ValidGLMFiveTwoTThreeN` | 300 | % valid forgeries, T3, glm-5.2, n |
| `\ValidGLMFiveTwoTThreeP` | n/a | % valid forgeries, T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\TthreeDeepSeekVFourFlashFirstSelected` | 15.3 | T3: % first-shown candidate selected, deepseek-v4-flash |
| `\TthreeDeepSeekVFourFlashFirstSelectedLo` | 12.3 | T3: % first-shown candidate selected, deepseek-v4-flash, lower 95% CI bound |
| `\TthreeDeepSeekVFourFlashFirstSelectedHi` | 18.3 | T3: % first-shown candidate selected, deepseek-v4-flash, upper 95% CI bound |
| `\TthreeDeepSeekVFourFlashFirstSelectedCI` | [12.3, 18.3] | T3: % first-shown candidate selected, deepseek-v4-flash, 95% CI |
| `\TthreeDeepSeekVFourFlashFirstSelectedN` | 300 | T3: % first-shown candidate selected, deepseek-v4-flash, n |
| `\TthreeDeepSeekVFourFlashFirstSelectedP` | n/a | T3: % first-shown candidate selected, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\TthreeDeepSeekVFourFlashFirstTop` | 21.7 | T3: % first-shown candidate top-rated, deepseek-v4-flash |
| `\TthreeDeepSeekVFourFlashFirstTopLo` | 18.0 | T3: % first-shown candidate top-rated, deepseek-v4-flash, lower 95% CI bound |
| `\TthreeDeepSeekVFourFlashFirstTopHi` | 25.7 | T3: % first-shown candidate top-rated, deepseek-v4-flash, upper 95% CI bound |
| `\TthreeDeepSeekVFourFlashFirstTopCI` | [18.0, 25.7] | T3: % first-shown candidate top-rated, deepseek-v4-flash, 95% CI |
| `\TthreeDeepSeekVFourFlashFirstTopN` | 300 | T3: % first-shown candidate top-rated, deepseek-v4-flash, n |
| `\TthreeDeepSeekVFourFlashFirstTopP` | n/a | T3: % first-shown candidate top-rated, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\TthreeDeepSeekVFourFlashChance` | 14.7 | T3: chance level of first-shown selection (%), deepseek-v4-flash |
| `\TthreeQwenThreeEightTwoSevenBFirstSelected` | 45.5 | T3: % first-shown candidate selected, qwen3.8-27b |
| `\TthreeQwenThreeEightTwoSevenBFirstSelectedLo` | 40.1 | T3: % first-shown candidate selected, qwen3.8-27b, lower 95% CI bound |
| `\TthreeQwenThreeEightTwoSevenBFirstSelectedHi` | 51.0 | T3: % first-shown candidate selected, qwen3.8-27b, upper 95% CI bound |
| `\TthreeQwenThreeEightTwoSevenBFirstSelectedCI` | [40.1, 51.0] | T3: % first-shown candidate selected, qwen3.8-27b, 95% CI |
| `\TthreeQwenThreeEightTwoSevenBFirstSelectedN` | 290 | T3: % first-shown candidate selected, qwen3.8-27b, n |
| `\TthreeQwenThreeEightTwoSevenBFirstSelectedP` | n/a | T3: % first-shown candidate selected, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\TthreeQwenThreeEightTwoSevenBFirstTop` | 69.3 | T3: % first-shown candidate top-rated, qwen3.8-27b |
| `\TthreeQwenThreeEightTwoSevenBFirstTopLo` | 64.5 | T3: % first-shown candidate top-rated, qwen3.8-27b, lower 95% CI bound |
| `\TthreeQwenThreeEightTwoSevenBFirstTopHi` | 74.0 | T3: % first-shown candidate top-rated, qwen3.8-27b, upper 95% CI bound |
| `\TthreeQwenThreeEightTwoSevenBFirstTopCI` | [64.5, 74.0] | T3: % first-shown candidate top-rated, qwen3.8-27b, 95% CI |
| `\TthreeQwenThreeEightTwoSevenBFirstTopN` | 290 | T3: % first-shown candidate top-rated, qwen3.8-27b, n |
| `\TthreeQwenThreeEightTwoSevenBFirstTopP` | n/a | T3: % first-shown candidate top-rated, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\TthreeQwenThreeEightTwoSevenBChance` | 14.2 | T3: chance level of first-shown selection (%), qwen3.8-27b |
| `\TthreeGemmaFourThreeOneBFirstSelected` | 31.7 | T3: % first-shown candidate selected, gemma-4-31b-it |
| `\TthreeGemmaFourThreeOneBFirstSelectedLo` | 26.0 | T3: % first-shown candidate selected, gemma-4-31b-it, lower 95% CI bound |
| `\TthreeGemmaFourThreeOneBFirstSelectedHi` | 37.4 | T3: % first-shown candidate selected, gemma-4-31b-it, upper 95% CI bound |
| `\TthreeGemmaFourThreeOneBFirstSelectedCI` | [26.0, 37.4] | T3: % first-shown candidate selected, gemma-4-31b-it, 95% CI |
| `\TthreeGemmaFourThreeOneBFirstSelectedN` | 290 | T3: % first-shown candidate selected, gemma-4-31b-it, n |
| `\TthreeGemmaFourThreeOneBFirstSelectedP` | n/a | T3: % first-shown candidate selected, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\TthreeGemmaFourThreeOneBFirstTop` | 61.7 | T3: % first-shown candidate top-rated, gemma-4-31b-it |
| `\TthreeGemmaFourThreeOneBFirstTopLo` | 55.9 | T3: % first-shown candidate top-rated, gemma-4-31b-it, lower 95% CI bound |
| `\TthreeGemmaFourThreeOneBFirstTopHi` | 67.6 | T3: % first-shown candidate top-rated, gemma-4-31b-it, upper 95% CI bound |
| `\TthreeGemmaFourThreeOneBFirstTopCI` | [55.9, 67.6] | T3: % first-shown candidate top-rated, gemma-4-31b-it, 95% CI |
| `\TthreeGemmaFourThreeOneBFirstTopN` | 290 | T3: % first-shown candidate top-rated, gemma-4-31b-it, n |
| `\TthreeGemmaFourThreeOneBFirstTopP` | n/a | T3: % first-shown candidate top-rated, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\TthreeGemmaFourThreeOneBChance` | 13.6 | T3: chance level of first-shown selection (%), gemma-4-31b-it |
| `\TthreeGLMFiveThreeFlashFirstSelected` | 11.4 | T3: % first-shown candidate selected, glm-5.3-flash |
| `\TthreeGLMFiveThreeFlashFirstSelectedLo` | 8.0 | T3: % first-shown candidate selected, glm-5.3-flash, lower 95% CI bound |
| `\TthreeGLMFiveThreeFlashFirstSelectedHi` | 15.1 | T3: % first-shown candidate selected, glm-5.3-flash, upper 95% CI bound |
| `\TthreeGLMFiveThreeFlashFirstSelectedCI` | [8.0, 15.1] | T3: % first-shown candidate selected, glm-5.3-flash, 95% CI |
| `\TthreeGLMFiveThreeFlashFirstSelectedN` | 299 | T3: % first-shown candidate selected, glm-5.3-flash, n |
| `\TthreeGLMFiveThreeFlashFirstSelectedP` | n/a | T3: % first-shown candidate selected, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\TthreeGLMFiveThreeFlashFirstTop` | 20.4 | T3: % first-shown candidate top-rated, glm-5.3-flash |
| `\TthreeGLMFiveThreeFlashFirstTopLo` | 16.7 | T3: % first-shown candidate top-rated, glm-5.3-flash, lower 95% CI bound |
| `\TthreeGLMFiveThreeFlashFirstTopHi` | 24.4 | T3: % first-shown candidate top-rated, glm-5.3-flash, upper 95% CI bound |
| `\TthreeGLMFiveThreeFlashFirstTopCI` | [16.7, 24.4] | T3: % first-shown candidate top-rated, glm-5.3-flash, 95% CI |
| `\TthreeGLMFiveThreeFlashFirstTopN` | 299 | T3: % first-shown candidate top-rated, glm-5.3-flash, n |
| `\TthreeGLMFiveThreeFlashFirstTopP` | n/a | T3: % first-shown candidate top-rated, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\TthreeGLMFiveThreeFlashChance` | 14.3 | T3: chance level of first-shown selection (%), glm-5.3-flash |
| `\TthreeGLMFiveTwoFirstSelected` | 5.0 | T3: % first-shown candidate selected, glm-5.2 |
| `\TthreeGLMFiveTwoFirstSelectedLo` | 3.0 | T3: % first-shown candidate selected, glm-5.2, lower 95% CI bound |
| `\TthreeGLMFiveTwoFirstSelectedHi` | 7.3 | T3: % first-shown candidate selected, glm-5.2, upper 95% CI bound |
| `\TthreeGLMFiveTwoFirstSelectedCI` | [3.0, 7.3] | T3: % first-shown candidate selected, glm-5.2, 95% CI |
| `\TthreeGLMFiveTwoFirstSelectedN` | 300 | T3: % first-shown candidate selected, glm-5.2, n |
| `\TthreeGLMFiveTwoFirstSelectedP` | n/a | T3: % first-shown candidate selected, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\TthreeGLMFiveTwoFirstTop` | 14.7 | T3: % first-shown candidate top-rated, glm-5.2 |
| `\TthreeGLMFiveTwoFirstTopLo` | 11.3 | T3: % first-shown candidate top-rated, glm-5.2, lower 95% CI bound |
| `\TthreeGLMFiveTwoFirstTopHi` | 18.3 | T3: % first-shown candidate top-rated, glm-5.2, upper 95% CI bound |
| `\TthreeGLMFiveTwoFirstTopCI` | [11.3, 18.3] | T3: % first-shown candidate top-rated, glm-5.2, 95% CI |
| `\TthreeGLMFiveTwoFirstTopN` | 300 | T3: % first-shown candidate top-rated, glm-5.2, n |
| `\TthreeGLMFiveTwoFirstTopP` | n/a | T3: % first-shown candidate top-rated, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\TthreeGLMFiveTwoChance` | 13.1 | T3: chance level of first-shown selection (%), glm-5.2 |
| `\PfourEditNoneTZeroEOneAsr` | 91.5 | ASR (%), none T0, edit type E1, pooled |
| `\PfourEditNoneTZeroEOneAsrLo` | 87.2 | ASR (%), none T0, edit type E1, pooled, lower 95% CI bound |
| `\PfourEditNoneTZeroEOneAsrHi` | 95.3 | ASR (%), none T0, edit type E1, pooled, upper 95% CI bound |
| `\PfourEditNoneTZeroEOneAsrCI` | [87.2, 95.3] | ASR (%), none T0, edit type E1, pooled, 95% CI |
| `\PfourEditNoneTZeroEOneAsrN` | 235 | ASR (%), none T0, edit type E1, pooled, n |
| `\PfourEditNoneTZeroEOneAsrP` | n/a | ASR (%), none T0, edit type E1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditNoneTZeroETwoAsr` | 39.9 | ASR (%), none T0, edit type E2, pooled |
| `\PfourEditNoneTZeroETwoAsrLo` | 30.9 | ASR (%), none T0, edit type E2, pooled, lower 95% CI bound |
| `\PfourEditNoneTZeroETwoAsrHi` | 49.4 | ASR (%), none T0, edit type E2, pooled, upper 95% CI bound |
| `\PfourEditNoneTZeroETwoAsrCI` | [30.9, 49.4] | ASR (%), none T0, edit type E2, pooled, 95% CI |
| `\PfourEditNoneTZeroETwoAsrN` | 233 | ASR (%), none T0, edit type E2, pooled, n |
| `\PfourEditNoneTZeroETwoAsrP` | n/a | ASR (%), none T0, edit type E2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditNoneTZeroEThreeAsr` | 67.2 | ASR (%), none T0, edit type E3, pooled |
| `\PfourEditNoneTZeroEThreeAsrLo` | 57.9 | ASR (%), none T0, edit type E3, pooled, lower 95% CI bound |
| `\PfourEditNoneTZeroEThreeAsrHi` | 76.6 | ASR (%), none T0, edit type E3, pooled, upper 95% CI bound |
| `\PfourEditNoneTZeroEThreeAsrCI` | [57.9, 76.6] | ASR (%), none T0, edit type E3, pooled, 95% CI |
| `\PfourEditNoneTZeroEThreeAsrN` | 235 | ASR (%), none T0, edit type E3, pooled, n |
| `\PfourEditNoneTZeroEThreeAsrP` | n/a | ASR (%), none T0, edit type E3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditNoneTZeroEFourAsr` | 26.0 | ASR (%), none T0, edit type E4, pooled |
| `\PfourEditNoneTZeroEFourAsrLo` | 18.3 | ASR (%), none T0, edit type E4, pooled, lower 95% CI bound |
| `\PfourEditNoneTZeroEFourAsrHi` | 34.9 | ASR (%), none T0, edit type E4, pooled, upper 95% CI bound |
| `\PfourEditNoneTZeroEFourAsrCI` | [18.3, 34.9] | ASR (%), none T0, edit type E4, pooled, 95% CI |
| `\PfourEditNoneTZeroEFourAsrN` | 235 | ASR (%), none T0, edit type E4, pooled, n |
| `\PfourEditNoneTZeroEFourAsrP` | n/a | ASR (%), none T0, edit type E4, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditNoneTZeroEFiveAsr` | 37.0 | ASR (%), none T0, edit type E5, pooled |
| `\PfourEditNoneTZeroEFiveAsrLo` | 27.2 | ASR (%), none T0, edit type E5, pooled, lower 95% CI bound |
| `\PfourEditNoneTZeroEFiveAsrHi` | 47.7 | ASR (%), none T0, edit type E5, pooled, upper 95% CI bound |
| `\PfourEditNoneTZeroEFiveAsrCI` | [27.2, 47.7] | ASR (%), none T0, edit type E5, pooled, 95% CI |
| `\PfourEditNoneTZeroEFiveAsrN` | 235 | ASR (%), none T0, edit type E5, pooled, n |
| `\PfourEditNoneTZeroEFiveAsrP` | n/a | ASR (%), none T0, edit type E5, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditNoneTTwoEOneAsr` | 93.2 | ASR (%), none T2, edit type E1, pooled |
| `\PfourEditNoneTTwoEOneAsrLo` | 89.4 | ASR (%), none T2, edit type E1, pooled, lower 95% CI bound |
| `\PfourEditNoneTTwoEOneAsrHi` | 96.2 | ASR (%), none T2, edit type E1, pooled, upper 95% CI bound |
| `\PfourEditNoneTTwoEOneAsrCI` | [89.4, 96.2] | ASR (%), none T2, edit type E1, pooled, 95% CI |
| `\PfourEditNoneTTwoEOneAsrN` | 235 | ASR (%), none T2, edit type E1, pooled, n |
| `\PfourEditNoneTTwoEOneAsrP` | n/a | ASR (%), none T2, edit type E1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditNoneTTwoETwoAsr` | 35.0 | ASR (%), none T2, edit type E2, pooled |
| `\PfourEditNoneTTwoETwoAsrLo` | 28.1 | ASR (%), none T2, edit type E2, pooled, lower 95% CI bound |
| `\PfourEditNoneTTwoETwoAsrHi` | 42.0 | ASR (%), none T2, edit type E2, pooled, upper 95% CI bound |
| `\PfourEditNoneTTwoETwoAsrCI` | [28.1, 42.0] | ASR (%), none T2, edit type E2, pooled, 95% CI |
| `\PfourEditNoneTTwoETwoAsrN` | 223 | ASR (%), none T2, edit type E2, pooled, n |
| `\PfourEditNoneTTwoETwoAsrP` | n/a | ASR (%), none T2, edit type E2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditNoneTTwoEThreeAsr` | 86.4 | ASR (%), none T2, edit type E3, pooled |
| `\PfourEditNoneTTwoEThreeAsrLo` | 81.7 | ASR (%), none T2, edit type E3, pooled, lower 95% CI bound |
| `\PfourEditNoneTTwoEThreeAsrHi` | 90.6 | ASR (%), none T2, edit type E3, pooled, upper 95% CI bound |
| `\PfourEditNoneTTwoEThreeAsrCI` | [81.7, 90.6] | ASR (%), none T2, edit type E3, pooled, 95% CI |
| `\PfourEditNoneTTwoEThreeAsrN` | 235 | ASR (%), none T2, edit type E3, pooled, n |
| `\PfourEditNoneTTwoEThreeAsrP` | n/a | ASR (%), none T2, edit type E3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditNoneTTwoEFourAsr` | 64.3 | ASR (%), none T2, edit type E4, pooled |
| `\PfourEditNoneTTwoEFourAsrLo` | 54.0 | ASR (%), none T2, edit type E4, pooled, lower 95% CI bound |
| `\PfourEditNoneTTwoEFourAsrHi` | 73.6 | ASR (%), none T2, edit type E4, pooled, upper 95% CI bound |
| `\PfourEditNoneTTwoEFourAsrCI` | [54.0, 73.6] | ASR (%), none T2, edit type E4, pooled, 95% CI |
| `\PfourEditNoneTTwoEFourAsrN` | 235 | ASR (%), none T2, edit type E4, pooled, n |
| `\PfourEditNoneTTwoEFourAsrP` | n/a | ASR (%), none T2, edit type E4, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditNoneTTwoEFiveAsr` | 22.0 | ASR (%), none T2, edit type E5, pooled |
| `\PfourEditNoneTTwoEFiveAsrLo` | 12.3 | ASR (%), none T2, edit type E5, pooled, lower 95% CI bound |
| `\PfourEditNoneTTwoEFiveAsrHi` | 31.8 | ASR (%), none T2, edit type E5, pooled, upper 95% CI bound |
| `\PfourEditNoneTTwoEFiveAsrCI` | [12.3, 31.8] | ASR (%), none T2, edit type E5, pooled, 95% CI |
| `\PfourEditNoneTTwoEFiveAsrN` | 227 | ASR (%), none T2, edit type E5, pooled, n |
| `\PfourEditNoneTTwoEFiveAsrP` | n/a | ASR (%), none T2, edit type E5, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditNoneTThreeEOneAsr` | 93.6 | ASR (%), none T3, edit type E1, pooled |
| `\PfourEditNoneTThreeEOneAsrLo` | 90.2 | ASR (%), none T3, edit type E1, pooled, lower 95% CI bound |
| `\PfourEditNoneTThreeEOneAsrHi` | 96.6 | ASR (%), none T3, edit type E1, pooled, upper 95% CI bound |
| `\PfourEditNoneTThreeEOneAsrCI` | [90.2, 96.6] | ASR (%), none T3, edit type E1, pooled, 95% CI |
| `\PfourEditNoneTThreeEOneAsrN` | 235 | ASR (%), none T3, edit type E1, pooled, n |
| `\PfourEditNoneTThreeEOneAsrP` | n/a | ASR (%), none T3, edit type E1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditNoneTThreeETwoAsr` | 41.0 | ASR (%), none T3, edit type E2, pooled |
| `\PfourEditNoneTThreeETwoAsrLo` | 34.8 | ASR (%), none T3, edit type E2, pooled, lower 95% CI bound |
| `\PfourEditNoneTThreeETwoAsrHi` | 47.4 | ASR (%), none T3, edit type E2, pooled, upper 95% CI bound |
| `\PfourEditNoneTThreeETwoAsrCI` | [34.8, 47.4] | ASR (%), none T3, edit type E2, pooled, 95% CI |
| `\PfourEditNoneTThreeETwoAsrN` | 229 | ASR (%), none T3, edit type E2, pooled, n |
| `\PfourEditNoneTThreeETwoAsrP` | n/a | ASR (%), none T3, edit type E2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditNoneTThreeEThreeAsr` | 88.1 | ASR (%), none T3, edit type E3, pooled |
| `\PfourEditNoneTThreeEThreeAsrLo` | 81.7 | ASR (%), none T3, edit type E3, pooled, lower 95% CI bound |
| `\PfourEditNoneTThreeEThreeAsrHi` | 93.6 | ASR (%), none T3, edit type E3, pooled, upper 95% CI bound |
| `\PfourEditNoneTThreeEThreeAsrCI` | [81.7, 93.6] | ASR (%), none T3, edit type E3, pooled, 95% CI |
| `\PfourEditNoneTThreeEThreeAsrN` | 235 | ASR (%), none T3, edit type E3, pooled, n |
| `\PfourEditNoneTThreeEThreeAsrP` | n/a | ASR (%), none T3, edit type E3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditNoneTThreeEFourAsr` | 66.8 | ASR (%), none T3, edit type E4, pooled |
| `\PfourEditNoneTThreeEFourAsrLo` | 56.6 | ASR (%), none T3, edit type E4, pooled, lower 95% CI bound |
| `\PfourEditNoneTThreeEFourAsrHi` | 76.2 | ASR (%), none T3, edit type E4, pooled, upper 95% CI bound |
| `\PfourEditNoneTThreeEFourAsrCI` | [56.6, 76.2] | ASR (%), none T3, edit type E4, pooled, 95% CI |
| `\PfourEditNoneTThreeEFourAsrN` | 235 | ASR (%), none T3, edit type E4, pooled, n |
| `\PfourEditNoneTThreeEFourAsrP` | n/a | ASR (%), none T3, edit type E4, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditNoneTThreeEFiveAsr` | 26.1 | ASR (%), none T3, edit type E5, pooled |
| `\PfourEditNoneTThreeEFiveAsrLo` | 16.2 | ASR (%), none T3, edit type E5, pooled, lower 95% CI bound |
| `\PfourEditNoneTThreeEFiveAsrHi` | 36.6 | ASR (%), none T3, edit type E5, pooled, upper 95% CI bound |
| `\PfourEditNoneTThreeEFiveAsrCI` | [16.2, 36.6] | ASR (%), none T3, edit type E5, pooled, 95% CI |
| `\PfourEditNoneTThreeEFiveAsrN` | 234 | ASR (%), none T3, edit type E5, pooled, n |
| `\PfourEditNoneTThreeEFiveAsrP` | n/a | ASR (%), none T3, edit type E5, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditNoMemoryEOneAsr` | 26.8 | ASR (%), no_memory -, edit type E1, pooled |
| `\PfourEditNoMemoryEOneAsrLo` | 20.0 | ASR (%), no_memory -, edit type E1, pooled, lower 95% CI bound |
| `\PfourEditNoMemoryEOneAsrHi` | 34.0 | ASR (%), no_memory -, edit type E1, pooled, upper 95% CI bound |
| `\PfourEditNoMemoryEOneAsrCI` | [20.0, 34.0] | ASR (%), no_memory -, edit type E1, pooled, 95% CI |
| `\PfourEditNoMemoryEOneAsrN` | 235 | ASR (%), no_memory -, edit type E1, pooled, n |
| `\PfourEditNoMemoryEOneAsrP` | n/a | ASR (%), no_memory -, edit type E1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditNoMemoryETwoAsr` | 19.7 | ASR (%), no_memory -, edit type E2, pooled |
| `\PfourEditNoMemoryETwoAsrLo` | 11.3 | ASR (%), no_memory -, edit type E2, pooled, lower 95% CI bound |
| `\PfourEditNoMemoryETwoAsrHi` | 29.6 | ASR (%), no_memory -, edit type E2, pooled, upper 95% CI bound |
| `\PfourEditNoMemoryETwoAsrCI` | [11.3, 29.6] | ASR (%), no_memory -, edit type E2, pooled, 95% CI |
| `\PfourEditNoMemoryETwoAsrN` | 233 | ASR (%), no_memory -, edit type E2, pooled, n |
| `\PfourEditNoMemoryETwoAsrP` | n/a | ASR (%), no_memory -, edit type E2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditNoMemoryEThreeAsr` | 6.8 | ASR (%), no_memory -, edit type E3, pooled |
| `\PfourEditNoMemoryEThreeAsrLo` | 3.0 | ASR (%), no_memory -, edit type E3, pooled, lower 95% CI bound |
| `\PfourEditNoMemoryEThreeAsrHi` | 11.9 | ASR (%), no_memory -, edit type E3, pooled, upper 95% CI bound |
| `\PfourEditNoMemoryEThreeAsrCI` | [3.0, 11.9] | ASR (%), no_memory -, edit type E3, pooled, 95% CI |
| `\PfourEditNoMemoryEThreeAsrN` | 235 | ASR (%), no_memory -, edit type E3, pooled, n |
| `\PfourEditNoMemoryEThreeAsrP` | n/a | ASR (%), no_memory -, edit type E3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditNoMemoryEFourAsr` | 5.5 | ASR (%), no_memory -, edit type E4, pooled |
| `\PfourEditNoMemoryEFourAsrLo` | 2.1 | ASR (%), no_memory -, edit type E4, pooled, lower 95% CI bound |
| `\PfourEditNoMemoryEFourAsrHi` | 9.4 | ASR (%), no_memory -, edit type E4, pooled, upper 95% CI bound |
| `\PfourEditNoMemoryEFourAsrCI` | [2.1, 9.4] | ASR (%), no_memory -, edit type E4, pooled, 95% CI |
| `\PfourEditNoMemoryEFourAsrN` | 235 | ASR (%), no_memory -, edit type E4, pooled, n |
| `\PfourEditNoMemoryEFourAsrP` | n/a | ASR (%), no_memory -, edit type E4, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditNoMemoryEFiveAsr` | 1.3 | ASR (%), no_memory -, edit type E5, pooled |
| `\PfourEditNoMemoryEFiveAsrLo` | 0.0 | ASR (%), no_memory -, edit type E5, pooled, lower 95% CI bound |
| `\PfourEditNoMemoryEFiveAsrHi` | 3.0 | ASR (%), no_memory -, edit type E5, pooled, upper 95% CI bound |
| `\PfourEditNoMemoryEFiveAsrCI` | [0.0, 3.0] | ASR (%), no_memory -, edit type E5, pooled, 95% CI |
| `\PfourEditNoMemoryEFiveAsrN` | 235 | ASR (%), no_memory -, edit type E5, pooled, n |
| `\PfourEditNoMemoryEFiveAsrP` | n/a | ASR (%), no_memory -, edit type E5, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGOneTZeroEOneAsr` | 6.1 | ASR (%), G1 T0, edit type E1, pooled |
| `\PfourEditGOneTZeroEOneAsrLo` | 3.0 | ASR (%), G1 T0, edit type E1, pooled, lower 95% CI bound |
| `\PfourEditGOneTZeroEOneAsrHi` | 9.7 | ASR (%), G1 T0, edit type E1, pooled, upper 95% CI bound |
| `\PfourEditGOneTZeroEOneAsrCI` | [3.0, 9.7] | ASR (%), G1 T0, edit type E1, pooled, 95% CI |
| `\PfourEditGOneTZeroEOneAsrN` | 231 | ASR (%), G1 T0, edit type E1, pooled, n |
| `\PfourEditGOneTZeroEOneAsrP` | n/a | ASR (%), G1 T0, edit type E1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGOneTZeroETwoAsr` | 0.4 | ASR (%), G1 T0, edit type E2, pooled |
| `\PfourEditGOneTZeroETwoAsrLo` | 0.0 | ASR (%), G1 T0, edit type E2, pooled, lower 95% CI bound |
| `\PfourEditGOneTZeroETwoAsrHi` | 1.3 | ASR (%), G1 T0, edit type E2, pooled, upper 95% CI bound |
| `\PfourEditGOneTZeroETwoAsrCI` | [0.0, 1.3] | ASR (%), G1 T0, edit type E2, pooled, 95% CI |
| `\PfourEditGOneTZeroETwoAsrN` | 231 | ASR (%), G1 T0, edit type E2, pooled, n |
| `\PfourEditGOneTZeroETwoAsrP` | n/a | ASR (%), G1 T0, edit type E2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGOneTZeroEThreeAsr` | 0.0 | ASR (%), G1 T0, edit type E3, pooled |
| `\PfourEditGOneTZeroEThreeAsrLo` | 0.0 | ASR (%), G1 T0, edit type E3, pooled, lower 95% CI bound |
| `\PfourEditGOneTZeroEThreeAsrHi` | 1.6 | ASR (%), G1 T0, edit type E3, pooled, upper 95% CI bound |
| `\PfourEditGOneTZeroEThreeAsrCI` | [0.0, 1.6] | ASR (%), G1 T0, edit type E3, pooled, 95% CI |
| `\PfourEditGOneTZeroEThreeAsrN` | 231 | ASR (%), G1 T0, edit type E3, pooled, n |
| `\PfourEditGOneTZeroEThreeAsrP` | n/a | ASR (%), G1 T0, edit type E3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGOneTZeroEFourAsr` | 0.0 | ASR (%), G1 T0, edit type E4, pooled |
| `\PfourEditGOneTZeroEFourAsrLo` | 0.0 | ASR (%), G1 T0, edit type E4, pooled, lower 95% CI bound |
| `\PfourEditGOneTZeroEFourAsrHi` | 1.6 | ASR (%), G1 T0, edit type E4, pooled, upper 95% CI bound |
| `\PfourEditGOneTZeroEFourAsrCI` | [0.0, 1.6] | ASR (%), G1 T0, edit type E4, pooled, 95% CI |
| `\PfourEditGOneTZeroEFourAsrN` | 231 | ASR (%), G1 T0, edit type E4, pooled, n |
| `\PfourEditGOneTZeroEFourAsrP` | n/a | ASR (%), G1 T0, edit type E4, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGOneTZeroEFiveAsr` | 1.3 | ASR (%), G1 T0, edit type E5, pooled |
| `\PfourEditGOneTZeroEFiveAsrLo` | 0.0 | ASR (%), G1 T0, edit type E5, pooled, lower 95% CI bound |
| `\PfourEditGOneTZeroEFiveAsrHi` | 3.0 | ASR (%), G1 T0, edit type E5, pooled, upper 95% CI bound |
| `\PfourEditGOneTZeroEFiveAsrCI` | [0.0, 3.0] | ASR (%), G1 T0, edit type E5, pooled, 95% CI |
| `\PfourEditGOneTZeroEFiveAsrN` | 230 | ASR (%), G1 T0, edit type E5, pooled, n |
| `\PfourEditGOneTZeroEFiveAsrP` | n/a | ASR (%), G1 T0, edit type E5, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGOneTTwoEOneAsr` | 5.2 | ASR (%), G1 T2, edit type E1, pooled |
| `\PfourEditGOneTTwoEOneAsrLo` | 2.2 | ASR (%), G1 T2, edit type E1, pooled, lower 95% CI bound |
| `\PfourEditGOneTTwoEOneAsrHi` | 8.6 | ASR (%), G1 T2, edit type E1, pooled, upper 95% CI bound |
| `\PfourEditGOneTTwoEOneAsrCI` | [2.2, 8.6] | ASR (%), G1 T2, edit type E1, pooled, 95% CI |
| `\PfourEditGOneTTwoEOneAsrN` | 231 | ASR (%), G1 T2, edit type E1, pooled, n |
| `\PfourEditGOneTTwoEOneAsrP` | n/a | ASR (%), G1 T2, edit type E1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGOneTTwoETwoAsr` | 0.0 | ASR (%), G1 T2, edit type E2, pooled |
| `\PfourEditGOneTTwoETwoAsrLo` | 0.0 | ASR (%), G1 T2, edit type E2, pooled, lower 95% CI bound |
| `\PfourEditGOneTTwoETwoAsrHi` | 1.7 | ASR (%), G1 T2, edit type E2, pooled, upper 95% CI bound |
| `\PfourEditGOneTTwoETwoAsrCI` | [0.0, 1.7] | ASR (%), G1 T2, edit type E2, pooled, 95% CI |
| `\PfourEditGOneTTwoETwoAsrN` | 221 | ASR (%), G1 T2, edit type E2, pooled, n |
| `\PfourEditGOneTTwoETwoAsrP` | n/a | ASR (%), G1 T2, edit type E2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGOneTTwoEThreeAsr` | 0.0 | ASR (%), G1 T2, edit type E3, pooled |
| `\PfourEditGOneTTwoEThreeAsrLo` | 0.0 | ASR (%), G1 T2, edit type E3, pooled, lower 95% CI bound |
| `\PfourEditGOneTTwoEThreeAsrHi` | 1.6 | ASR (%), G1 T2, edit type E3, pooled, upper 95% CI bound |
| `\PfourEditGOneTTwoEThreeAsrCI` | [0.0, 1.6] | ASR (%), G1 T2, edit type E3, pooled, 95% CI |
| `\PfourEditGOneTTwoEThreeAsrN` | 231 | ASR (%), G1 T2, edit type E3, pooled, n |
| `\PfourEditGOneTTwoEThreeAsrP` | n/a | ASR (%), G1 T2, edit type E3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGOneTTwoEFourAsr` | 0.0 | ASR (%), G1 T2, edit type E4, pooled |
| `\PfourEditGOneTTwoEFourAsrLo` | 0.0 | ASR (%), G1 T2, edit type E4, pooled, lower 95% CI bound |
| `\PfourEditGOneTTwoEFourAsrHi` | 1.6 | ASR (%), G1 T2, edit type E4, pooled, upper 95% CI bound |
| `\PfourEditGOneTTwoEFourAsrCI` | [0.0, 1.6] | ASR (%), G1 T2, edit type E4, pooled, 95% CI |
| `\PfourEditGOneTTwoEFourAsrN` | 231 | ASR (%), G1 T2, edit type E4, pooled, n |
| `\PfourEditGOneTTwoEFourAsrP` | n/a | ASR (%), G1 T2, edit type E4, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGOneTTwoEFiveAsr` | 0.4 | ASR (%), G1 T2, edit type E5, pooled |
| `\PfourEditGOneTTwoEFiveAsrLo` | 0.0 | ASR (%), G1 T2, edit type E5, pooled, lower 95% CI bound |
| `\PfourEditGOneTTwoEFiveAsrHi` | 1.4 | ASR (%), G1 T2, edit type E5, pooled, upper 95% CI bound |
| `\PfourEditGOneTTwoEFiveAsrCI` | [0.0, 1.4] | ASR (%), G1 T2, edit type E5, pooled, 95% CI |
| `\PfourEditGOneTTwoEFiveAsrN` | 223 | ASR (%), G1 T2, edit type E5, pooled, n |
| `\PfourEditGOneTTwoEFiveAsrP` | n/a | ASR (%), G1 T2, edit type E5, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGOneTThreeEOneAsr` | 6.9 | ASR (%), G1 T3, edit type E1, pooled |
| `\PfourEditGOneTThreeEOneAsrLo` | 3.5 | ASR (%), G1 T3, edit type E1, pooled, lower 95% CI bound |
| `\PfourEditGOneTThreeEOneAsrHi` | 10.8 | ASR (%), G1 T3, edit type E1, pooled, upper 95% CI bound |
| `\PfourEditGOneTThreeEOneAsrCI` | [3.5, 10.8] | ASR (%), G1 T3, edit type E1, pooled, 95% CI |
| `\PfourEditGOneTThreeEOneAsrN` | 231 | ASR (%), G1 T3, edit type E1, pooled, n |
| `\PfourEditGOneTThreeEOneAsrP` | n/a | ASR (%), G1 T3, edit type E1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGOneTThreeETwoAsr` | 0.9 | ASR (%), G1 T3, edit type E2, pooled |
| `\PfourEditGOneTThreeETwoAsrLo` | 0.0 | ASR (%), G1 T3, edit type E2, pooled, lower 95% CI bound |
| `\PfourEditGOneTThreeETwoAsrHi` | 2.7 | ASR (%), G1 T3, edit type E2, pooled, upper 95% CI bound |
| `\PfourEditGOneTThreeETwoAsrCI` | [0.0, 2.7] | ASR (%), G1 T3, edit type E2, pooled, 95% CI |
| `\PfourEditGOneTThreeETwoAsrN` | 227 | ASR (%), G1 T3, edit type E2, pooled, n |
| `\PfourEditGOneTThreeETwoAsrP` | n/a | ASR (%), G1 T3, edit type E2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGOneTThreeEThreeAsr` | 0.0 | ASR (%), G1 T3, edit type E3, pooled |
| `\PfourEditGOneTThreeEThreeAsrLo` | 0.0 | ASR (%), G1 T3, edit type E3, pooled, lower 95% CI bound |
| `\PfourEditGOneTThreeEThreeAsrHi` | 1.6 | ASR (%), G1 T3, edit type E3, pooled, upper 95% CI bound |
| `\PfourEditGOneTThreeEThreeAsrCI` | [0.0, 1.6] | ASR (%), G1 T3, edit type E3, pooled, 95% CI |
| `\PfourEditGOneTThreeEThreeAsrN` | 230 | ASR (%), G1 T3, edit type E3, pooled, n |
| `\PfourEditGOneTThreeEThreeAsrP` | n/a | ASR (%), G1 T3, edit type E3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGOneTThreeEFourAsr` | 0.0 | ASR (%), G1 T3, edit type E4, pooled |
| `\PfourEditGOneTThreeEFourAsrLo` | 0.0 | ASR (%), G1 T3, edit type E4, pooled, lower 95% CI bound |
| `\PfourEditGOneTThreeEFourAsrHi` | 1.6 | ASR (%), G1 T3, edit type E4, pooled, upper 95% CI bound |
| `\PfourEditGOneTThreeEFourAsrCI` | [0.0, 1.6] | ASR (%), G1 T3, edit type E4, pooled, 95% CI |
| `\PfourEditGOneTThreeEFourAsrN` | 230 | ASR (%), G1 T3, edit type E4, pooled, n |
| `\PfourEditGOneTThreeEFourAsrP` | n/a | ASR (%), G1 T3, edit type E4, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGOneTThreeEFiveAsr` | 0.4 | ASR (%), G1 T3, edit type E5, pooled |
| `\PfourEditGOneTThreeEFiveAsrLo` | 0.0 | ASR (%), G1 T3, edit type E5, pooled, lower 95% CI bound |
| `\PfourEditGOneTThreeEFiveAsrHi` | 1.3 | ASR (%), G1 T3, edit type E5, pooled, upper 95% CI bound |
| `\PfourEditGOneTThreeEFiveAsrCI` | [0.0, 1.3] | ASR (%), G1 T3, edit type E5, pooled, 95% CI |
| `\PfourEditGOneTThreeEFiveAsrN` | 230 | ASR (%), G1 T3, edit type E5, pooled, n |
| `\PfourEditGOneTThreeEFiveAsrP` | n/a | ASR (%), G1 T3, edit type E5, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGTwoUTTwoEOneAsr` | 92.8 | ASR (%), G2u T2, edit type E1, pooled |
| `\PfourEditGTwoUTTwoEOneAsrLo` | 89.4 | ASR (%), G2u T2, edit type E1, pooled, lower 95% CI bound |
| `\PfourEditGTwoUTTwoEOneAsrHi` | 95.7 | ASR (%), G2u T2, edit type E1, pooled, upper 95% CI bound |
| `\PfourEditGTwoUTTwoEOneAsrCI` | [89.4, 95.7] | ASR (%), G2u T2, edit type E1, pooled, 95% CI |
| `\PfourEditGTwoUTTwoEOneAsrN` | 235 | ASR (%), G2u T2, edit type E1, pooled, n |
| `\PfourEditGTwoUTTwoEOneAsrP` | n/a | ASR (%), G2u T2, edit type E1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGTwoUTTwoETwoAsr` | 31.4 | ASR (%), G2u T2, edit type E2, pooled |
| `\PfourEditGTwoUTTwoETwoAsrLo` | 24.3 | ASR (%), G2u T2, edit type E2, pooled, lower 95% CI bound |
| `\PfourEditGTwoUTTwoETwoAsrHi` | 38.9 | ASR (%), G2u T2, edit type E2, pooled, upper 95% CI bound |
| `\PfourEditGTwoUTTwoETwoAsrCI` | [24.3, 38.9] | ASR (%), G2u T2, edit type E2, pooled, 95% CI |
| `\PfourEditGTwoUTTwoETwoAsrN` | 223 | ASR (%), G2u T2, edit type E2, pooled, n |
| `\PfourEditGTwoUTTwoETwoAsrP` | n/a | ASR (%), G2u T2, edit type E2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGTwoUTTwoEThreeAsr` | 87.2 | ASR (%), G2u T2, edit type E3, pooled |
| `\PfourEditGTwoUTTwoEThreeAsrLo` | 82.1 | ASR (%), G2u T2, edit type E3, pooled, lower 95% CI bound |
| `\PfourEditGTwoUTTwoEThreeAsrHi` | 91.5 | ASR (%), G2u T2, edit type E3, pooled, upper 95% CI bound |
| `\PfourEditGTwoUTTwoEThreeAsrCI` | [82.1, 91.5] | ASR (%), G2u T2, edit type E3, pooled, 95% CI |
| `\PfourEditGTwoUTTwoEThreeAsrN` | 235 | ASR (%), G2u T2, edit type E3, pooled, n |
| `\PfourEditGTwoUTTwoEThreeAsrP` | n/a | ASR (%), G2u T2, edit type E3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGTwoUTTwoEFourAsr` | 63.4 | ASR (%), G2u T2, edit type E4, pooled |
| `\PfourEditGTwoUTTwoEFourAsrLo` | 53.6 | ASR (%), G2u T2, edit type E4, pooled, lower 95% CI bound |
| `\PfourEditGTwoUTTwoEFourAsrHi` | 72.8 | ASR (%), G2u T2, edit type E4, pooled, upper 95% CI bound |
| `\PfourEditGTwoUTTwoEFourAsrCI` | [53.6, 72.8] | ASR (%), G2u T2, edit type E4, pooled, 95% CI |
| `\PfourEditGTwoUTTwoEFourAsrN` | 235 | ASR (%), G2u T2, edit type E4, pooled, n |
| `\PfourEditGTwoUTTwoEFourAsrP` | n/a | ASR (%), G2u T2, edit type E4, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGTwoUTTwoEFiveAsr` | 22.0 | ASR (%), G2u T2, edit type E5, pooled |
| `\PfourEditGTwoUTTwoEFiveAsrLo` | 13.0 | ASR (%), G2u T2, edit type E5, pooled, lower 95% CI bound |
| `\PfourEditGTwoUTTwoEFiveAsrHi` | 32.2 | ASR (%), G2u T2, edit type E5, pooled, upper 95% CI bound |
| `\PfourEditGTwoUTTwoEFiveAsrCI` | [13.0, 32.2] | ASR (%), G2u T2, edit type E5, pooled, 95% CI |
| `\PfourEditGTwoUTTwoEFiveAsrN` | 227 | ASR (%), G2u T2, edit type E5, pooled, n |
| `\PfourEditGTwoUTTwoEFiveAsrP` | n/a | ASR (%), G2u T2, edit type E5, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGTwoSTTwoEOneAsr` | 81.7 | ASR (%), G2s T2, edit type E1, pooled |
| `\PfourEditGTwoSTTwoEOneAsrLo` | 77.9 | ASR (%), G2s T2, edit type E1, pooled, lower 95% CI bound |
| `\PfourEditGTwoSTTwoEOneAsrHi` | 85.5 | ASR (%), G2s T2, edit type E1, pooled, upper 95% CI bound |
| `\PfourEditGTwoSTTwoEOneAsrCI` | [77.9, 85.5] | ASR (%), G2s T2, edit type E1, pooled, 95% CI |
| `\PfourEditGTwoSTTwoEOneAsrN` | 235 | ASR (%), G2s T2, edit type E1, pooled, n |
| `\PfourEditGTwoSTTwoEOneAsrP` | n/a | ASR (%), G2s T2, edit type E1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGTwoSTTwoETwoAsr` | 12.6 | ASR (%), G2s T2, edit type E2, pooled |
| `\PfourEditGTwoSTTwoETwoAsrLo` | 8.4 | ASR (%), G2s T2, edit type E2, pooled, lower 95% CI bound |
| `\PfourEditGTwoSTTwoETwoAsrHi` | 16.7 | ASR (%), G2s T2, edit type E2, pooled, upper 95% CI bound |
| `\PfourEditGTwoSTTwoETwoAsrCI` | [8.4, 16.7] | ASR (%), G2s T2, edit type E2, pooled, 95% CI |
| `\PfourEditGTwoSTTwoETwoAsrN` | 223 | ASR (%), G2s T2, edit type E2, pooled, n |
| `\PfourEditGTwoSTTwoETwoAsrP` | n/a | ASR (%), G2s T2, edit type E2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGTwoSTTwoEThreeAsr` | 21.3 | ASR (%), G2s T2, edit type E3, pooled |
| `\PfourEditGTwoSTTwoEThreeAsrLo` | 17.0 | ASR (%), G2s T2, edit type E3, pooled, lower 95% CI bound |
| `\PfourEditGTwoSTTwoEThreeAsrHi` | 26.0 | ASR (%), G2s T2, edit type E3, pooled, upper 95% CI bound |
| `\PfourEditGTwoSTTwoEThreeAsrCI` | [17.0, 26.0] | ASR (%), G2s T2, edit type E3, pooled, 95% CI |
| `\PfourEditGTwoSTTwoEThreeAsrN` | 235 | ASR (%), G2s T2, edit type E3, pooled, n |
| `\PfourEditGTwoSTTwoEThreeAsrP` | n/a | ASR (%), G2s T2, edit type E3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGTwoSTTwoEFourAsr` | 6.0 | ASR (%), G2s T2, edit type E4, pooled |
| `\PfourEditGTwoSTTwoEFourAsrLo` | 2.6 | ASR (%), G2s T2, edit type E4, pooled, lower 95% CI bound |
| `\PfourEditGTwoSTTwoEFourAsrHi` | 9.8 | ASR (%), G2s T2, edit type E4, pooled, upper 95% CI bound |
| `\PfourEditGTwoSTTwoEFourAsrCI` | [2.6, 9.8] | ASR (%), G2s T2, edit type E4, pooled, 95% CI |
| `\PfourEditGTwoSTTwoEFourAsrN` | 235 | ASR (%), G2s T2, edit type E4, pooled, n |
| `\PfourEditGTwoSTTwoEFourAsrP` | n/a | ASR (%), G2s T2, edit type E4, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGTwoSTTwoEFiveAsr` | 9.7 | ASR (%), G2s T2, edit type E5, pooled |
| `\PfourEditGTwoSTTwoEFiveAsrLo` | 4.4 | ASR (%), G2s T2, edit type E5, pooled, lower 95% CI bound |
| `\PfourEditGTwoSTTwoEFiveAsrHi` | 16.2 | ASR (%), G2s T2, edit type E5, pooled, upper 95% CI bound |
| `\PfourEditGTwoSTTwoEFiveAsrCI` | [4.4, 16.2] | ASR (%), G2s T2, edit type E5, pooled, 95% CI |
| `\PfourEditGTwoSTTwoEFiveAsrN` | 227 | ASR (%), G2s T2, edit type E5, pooled, n |
| `\PfourEditGTwoSTTwoEFiveAsrP` | n/a | ASR (%), G2s T2, edit type E5, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGTwoSInsiderTTwoEOneAsr` | 94.0 | ASR (%), G2s_insider T2, edit type E1, pooled |
| `\PfourEditGTwoSInsiderTTwoEOneAsrLo` | 90.6 | ASR (%), G2s_insider T2, edit type E1, pooled, lower 95% CI bound |
| `\PfourEditGTwoSInsiderTTwoEOneAsrHi` | 97.0 | ASR (%), G2s_insider T2, edit type E1, pooled, upper 95% CI bound |
| `\PfourEditGTwoSInsiderTTwoEOneAsrCI` | [90.6, 97.0] | ASR (%), G2s_insider T2, edit type E1, pooled, 95% CI |
| `\PfourEditGTwoSInsiderTTwoEOneAsrN` | 235 | ASR (%), G2s_insider T2, edit type E1, pooled, n |
| `\PfourEditGTwoSInsiderTTwoEOneAsrP` | n/a | ASR (%), G2s_insider T2, edit type E1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGTwoSInsiderTTwoETwoAsr` | 31.4 | ASR (%), G2s_insider T2, edit type E2, pooled |
| `\PfourEditGTwoSInsiderTTwoETwoAsrLo` | 24.8 | ASR (%), G2s_insider T2, edit type E2, pooled, lower 95% CI bound |
| `\PfourEditGTwoSInsiderTTwoETwoAsrHi` | 38.9 | ASR (%), G2s_insider T2, edit type E2, pooled, upper 95% CI bound |
| `\PfourEditGTwoSInsiderTTwoETwoAsrCI` | [24.8, 38.9] | ASR (%), G2s_insider T2, edit type E2, pooled, 95% CI |
| `\PfourEditGTwoSInsiderTTwoETwoAsrN` | 223 | ASR (%), G2s_insider T2, edit type E2, pooled, n |
| `\PfourEditGTwoSInsiderTTwoETwoAsrP` | n/a | ASR (%), G2s_insider T2, edit type E2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGTwoSInsiderTTwoEThreeAsr` | 85.1 | ASR (%), G2s_insider T2, edit type E3, pooled |
| `\PfourEditGTwoSInsiderTTwoEThreeAsrLo` | 80.0 | ASR (%), G2s_insider T2, edit type E3, pooled, lower 95% CI bound |
| `\PfourEditGTwoSInsiderTTwoEThreeAsrHi` | 89.8 | ASR (%), G2s_insider T2, edit type E3, pooled, upper 95% CI bound |
| `\PfourEditGTwoSInsiderTTwoEThreeAsrCI` | [80.0, 89.8] | ASR (%), G2s_insider T2, edit type E3, pooled, 95% CI |
| `\PfourEditGTwoSInsiderTTwoEThreeAsrN` | 235 | ASR (%), G2s_insider T2, edit type E3, pooled, n |
| `\PfourEditGTwoSInsiderTTwoEThreeAsrP` | n/a | ASR (%), G2s_insider T2, edit type E3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGTwoSInsiderTTwoEFourAsr` | 64.7 | ASR (%), G2s_insider T2, edit type E4, pooled |
| `\PfourEditGTwoSInsiderTTwoEFourAsrLo` | 55.3 | ASR (%), G2s_insider T2, edit type E4, pooled, lower 95% CI bound |
| `\PfourEditGTwoSInsiderTTwoEFourAsrHi` | 74.0 | ASR (%), G2s_insider T2, edit type E4, pooled, upper 95% CI bound |
| `\PfourEditGTwoSInsiderTTwoEFourAsrCI` | [55.3, 74.0] | ASR (%), G2s_insider T2, edit type E4, pooled, 95% CI |
| `\PfourEditGTwoSInsiderTTwoEFourAsrN` | 235 | ASR (%), G2s_insider T2, edit type E4, pooled, n |
| `\PfourEditGTwoSInsiderTTwoEFourAsrP` | n/a | ASR (%), G2s_insider T2, edit type E4, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGTwoSInsiderTTwoEFiveAsr` | 22.5 | ASR (%), G2s_insider T2, edit type E5, pooled |
| `\PfourEditGTwoSInsiderTTwoEFiveAsrLo` | 12.6 | ASR (%), G2s_insider T2, edit type E5, pooled, lower 95% CI bound |
| `\PfourEditGTwoSInsiderTTwoEFiveAsrHi` | 32.2 | ASR (%), G2s_insider T2, edit type E5, pooled, upper 95% CI bound |
| `\PfourEditGTwoSInsiderTTwoEFiveAsrCI` | [12.6, 32.2] | ASR (%), G2s_insider T2, edit type E5, pooled, 95% CI |
| `\PfourEditGTwoSInsiderTTwoEFiveAsrN` | 227 | ASR (%), G2s_insider T2, edit type E5, pooled, n |
| `\PfourEditGTwoSInsiderTTwoEFiveAsrP` | n/a | ASR (%), G2s_insider T2, edit type E5, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGOnePlusGTwoSEOneAsr` | 1.3 | ASR (%), G1+G2s -, edit type E1, pooled |
| `\PfourEditGOnePlusGTwoSEOneAsrLo` | 0.0 | ASR (%), G1+G2s -, edit type E1, pooled, lower 95% CI bound |
| `\PfourEditGOnePlusGTwoSEOneAsrHi` | 3.0 | ASR (%), G1+G2s -, edit type E1, pooled, upper 95% CI bound |
| `\PfourEditGOnePlusGTwoSEOneAsrCI` | [0.0, 3.0] | ASR (%), G1+G2s -, edit type E1, pooled, 95% CI |
| `\PfourEditGOnePlusGTwoSEOneAsrN` | 235 | ASR (%), G1+G2s -, edit type E1, pooled, n |
| `\PfourEditGOnePlusGTwoSEOneAsrP` | n/a | ASR (%), G1+G2s -, edit type E1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGOnePlusGTwoSETwoAsr` | 0.0 | ASR (%), G1+G2s -, edit type E2, pooled |
| `\PfourEditGOnePlusGTwoSETwoAsrLo` | 0.0 | ASR (%), G1+G2s -, edit type E2, pooled, lower 95% CI bound |
| `\PfourEditGOnePlusGTwoSETwoAsrHi` | 1.6 | ASR (%), G1+G2s -, edit type E2, pooled, upper 95% CI bound |
| `\PfourEditGOnePlusGTwoSETwoAsrCI` | [0.0, 1.6] | ASR (%), G1+G2s -, edit type E2, pooled, 95% CI |
| `\PfourEditGOnePlusGTwoSETwoAsrN` | 233 | ASR (%), G1+G2s -, edit type E2, pooled, n |
| `\PfourEditGOnePlusGTwoSETwoAsrP` | n/a | ASR (%), G1+G2s -, edit type E2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGOnePlusGTwoSEThreeAsr` | 0.0 | ASR (%), G1+G2s -, edit type E3, pooled |
| `\PfourEditGOnePlusGTwoSEThreeAsrLo` | 0.0 | ASR (%), G1+G2s -, edit type E3, pooled, lower 95% CI bound |
| `\PfourEditGOnePlusGTwoSEThreeAsrHi` | 1.6 | ASR (%), G1+G2s -, edit type E3, pooled, upper 95% CI bound |
| `\PfourEditGOnePlusGTwoSEThreeAsrCI` | [0.0, 1.6] | ASR (%), G1+G2s -, edit type E3, pooled, 95% CI |
| `\PfourEditGOnePlusGTwoSEThreeAsrN` | 235 | ASR (%), G1+G2s -, edit type E3, pooled, n |
| `\PfourEditGOnePlusGTwoSEThreeAsrP` | n/a | ASR (%), G1+G2s -, edit type E3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGOnePlusGTwoSEFourAsr` | 0.0 | ASR (%), G1+G2s -, edit type E4, pooled |
| `\PfourEditGOnePlusGTwoSEFourAsrLo` | 0.0 | ASR (%), G1+G2s -, edit type E4, pooled, lower 95% CI bound |
| `\PfourEditGOnePlusGTwoSEFourAsrHi` | 1.6 | ASR (%), G1+G2s -, edit type E4, pooled, upper 95% CI bound |
| `\PfourEditGOnePlusGTwoSEFourAsrCI` | [0.0, 1.6] | ASR (%), G1+G2s -, edit type E4, pooled, 95% CI |
| `\PfourEditGOnePlusGTwoSEFourAsrN` | 235 | ASR (%), G1+G2s -, edit type E4, pooled, n |
| `\PfourEditGOnePlusGTwoSEFourAsrP` | n/a | ASR (%), G1+G2s -, edit type E4, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourEditGOnePlusGTwoSEFiveAsr` | 0.9 | ASR (%), G1+G2s -, edit type E5, pooled |
| `\PfourEditGOnePlusGTwoSEFiveAsrLo` | 0.0 | ASR (%), G1+G2s -, edit type E5, pooled, lower 95% CI bound |
| `\PfourEditGOnePlusGTwoSEFiveAsrHi` | 2.1 | ASR (%), G1+G2s -, edit type E5, pooled, upper 95% CI bound |
| `\PfourEditGOnePlusGTwoSEFiveAsrCI` | [0.0, 2.1] | ASR (%), G1+G2s -, edit type E5, pooled, 95% CI |
| `\PfourEditGOnePlusGTwoSEFiveAsrN` | 235 | ASR (%), G1+G2s -, edit type E5, pooled, n |
| `\PfourEditGOnePlusGTwoSEFiveAsrP` | n/a | ASR (%), G1+G2s -, edit type E5, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroPooledAsr` | 52.3 | ASR (%), none T0, pooled |
| `\PfourNoneTZeroPooledAsrLo` | 48.0 | ASR (%), none T0, pooled, lower 95% CI bound |
| `\PfourNoneTZeroPooledAsrHi` | 56.6 | ASR (%), none T0, pooled, upper 95% CI bound |
| `\PfourNoneTZeroPooledAsrCI` | [48.0, 56.6] | ASR (%), none T0, pooled, 95% CI |
| `\PfourNoneTZeroPooledAsrN` | 1{,}173 | ASR (%), none T0, pooled, n |
| `\PfourNoneTZeroPooledAsrP` | n/a | ASR (%), none T0, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroPooledAsrDropped` | 52.5 | ASR (%) unparsed dropped, none T0, pooled |
| `\PfourNoneTZeroPooledAsrDroppedLo` | 48.1 | ASR (%) unparsed dropped, none T0, pooled, lower 95% CI bound |
| `\PfourNoneTZeroPooledAsrDroppedHi` | 56.8 | ASR (%) unparsed dropped, none T0, pooled, upper 95% CI bound |
| `\PfourNoneTZeroPooledAsrDroppedCI` | [48.1, 56.8] | ASR (%) unparsed dropped, none T0, pooled, 95% CI |
| `\PfourNoneTZeroPooledAsrDroppedN` | 1{,}170 | ASR (%) unparsed dropped, none T0, pooled, n |
| `\PfourNoneTZeroPooledAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T0, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroPooledAsrCleanOk` | 52.0 | ASR / clean correct (%), none T0, pooled |
| `\PfourNoneTZeroPooledAsrCleanOkLo` | 47.6 | ASR / clean correct (%), none T0, pooled, lower 95% CI bound |
| `\PfourNoneTZeroPooledAsrCleanOkHi` | 56.1 | ASR / clean correct (%), none T0, pooled, upper 95% CI bound |
| `\PfourNoneTZeroPooledAsrCleanOkCI` | [47.6, 56.1] | ASR / clean correct (%), none T0, pooled, 95% CI |
| `\PfourNoneTZeroPooledAsrCleanOkN` | 1{,}146 | ASR / clean correct (%), none T0, pooled, n |
| `\PfourNoneTZeroPooledAsrCleanOkP` | n/a | ASR / clean correct (%), none T0, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroPooledNonTargetAcc` | 97.9 | non-target accuracy (%), none T0, pooled |
| `\PfourNoneTZeroPooledNonTargetAccLo` | 96.9 | non-target accuracy (%), none T0, pooled, lower 95% CI bound |
| `\PfourNoneTZeroPooledNonTargetAccHi` | 98.9 | non-target accuracy (%), none T0, pooled, upper 95% CI bound |
| `\PfourNoneTZeroPooledNonTargetAccCI` | [96.9, 98.9] | non-target accuracy (%), none T0, pooled, 95% CI |
| `\PfourNoneTZeroPooledNonTargetAccN` | 4{,}680 | non-target accuracy (%), none T0, pooled, n |
| `\PfourNoneTZeroPooledNonTargetAccP` | n/a | non-target accuracy (%), none T0, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroDeepSeekVFourFlashAsr` | 41.7 | ASR (%), none T0, deepseek-v4-flash |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrLo` | 36.6 | ASR (%), none T0, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrHi` | 46.8 | ASR (%), none T0, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrCI` | [36.6, 46.8] | ASR (%), none T0, deepseek-v4-flash, 95% CI |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrN` | 235 | ASR (%), none T0, deepseek-v4-flash, n |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrP` | n/a | ASR (%), none T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrDropped` | 41.7 | ASR (%) unparsed dropped, none T0, deepseek-v4-flash |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrDroppedLo` | 36.2 | ASR (%) unparsed dropped, none T0, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrDroppedHi` | 46.8 | ASR (%) unparsed dropped, none T0, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrDroppedCI` | [36.2, 46.8] | ASR (%) unparsed dropped, none T0, deepseek-v4-flash, 95% CI |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrDroppedN` | 235 | ASR (%) unparsed dropped, none T0, deepseek-v4-flash, n |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrCleanOk` | 41.5 | ASR / clean correct (%), none T0, deepseek-v4-flash |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrCleanOkLo` | 36.2 | ASR / clean correct (%), none T0, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrCleanOkHi` | 46.6 | ASR / clean correct (%), none T0, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrCleanOkCI` | [36.2, 46.6] | ASR / clean correct (%), none T0, deepseek-v4-flash, 95% CI |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrCleanOkN` | 234 | ASR / clean correct (%), none T0, deepseek-v4-flash, n |
| `\PfourNoneTZeroDeepSeekVFourFlashAsrCleanOkP` | n/a | ASR / clean correct (%), none T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroDeepSeekVFourFlashNonTargetAcc` | 99.6 | non-target accuracy (%), none T0, deepseek-v4-flash |
| `\PfourNoneTZeroDeepSeekVFourFlashNonTargetAccLo` | 98.7 | non-target accuracy (%), none T0, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTZeroDeepSeekVFourFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), none T0, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTZeroDeepSeekVFourFlashNonTargetAccCI` | [98.7, 100.0] | non-target accuracy (%), none T0, deepseek-v4-flash, 95% CI |
| `\PfourNoneTZeroDeepSeekVFourFlashNonTargetAccN` | 940 | non-target accuracy (%), none T0, deepseek-v4-flash, n |
| `\PfourNoneTZeroDeepSeekVFourFlashNonTargetAccP` | n/a | non-target accuracy (%), none T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsr` | 47.7 | ASR (%), none T0, qwen3.8-27b |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrLo` | 40.9 | ASR (%), none T0, qwen3.8-27b, lower 95% CI bound |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrHi` | 54.0 | ASR (%), none T0, qwen3.8-27b, upper 95% CI bound |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrCI` | [40.9, 54.0] | ASR (%), none T0, qwen3.8-27b, 95% CI |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrN` | 235 | ASR (%), none T0, qwen3.8-27b, n |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrP` | n/a | ASR (%), none T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrDropped` | 47.7 | ASR (%) unparsed dropped, none T0, qwen3.8-27b |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrDroppedLo` | 41.3 | ASR (%) unparsed dropped, none T0, qwen3.8-27b, lower 95% CI bound |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrDroppedHi` | 54.5 | ASR (%) unparsed dropped, none T0, qwen3.8-27b, upper 95% CI bound |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrDroppedCI` | [41.3, 54.5] | ASR (%) unparsed dropped, none T0, qwen3.8-27b, 95% CI |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrDroppedN` | 235 | ASR (%) unparsed dropped, none T0, qwen3.8-27b, n |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrCleanOk` | 46.6 | ASR / clean correct (%), none T0, qwen3.8-27b |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrCleanOkLo` | 39.6 | ASR / clean correct (%), none T0, qwen3.8-27b, lower 95% CI bound |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrCleanOkHi` | 53.7 | ASR / clean correct (%), none T0, qwen3.8-27b, upper 95% CI bound |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrCleanOkCI` | [39.6, 53.7] | ASR / clean correct (%), none T0, qwen3.8-27b, 95% CI |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrCleanOkN` | 223 | ASR / clean correct (%), none T0, qwen3.8-27b, n |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBAsrCleanOkP` | n/a | ASR / clean correct (%), none T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBNonTargetAcc` | 94.3 | non-target accuracy (%), none T0, qwen3.8-27b |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBNonTargetAccLo` | 91.6 | non-target accuracy (%), none T0, qwen3.8-27b, lower 95% CI bound |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBNonTargetAccHi` | 96.8 | non-target accuracy (%), none T0, qwen3.8-27b, upper 95% CI bound |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBNonTargetAccCI` | [91.6, 96.8] | non-target accuracy (%), none T0, qwen3.8-27b, 95% CI |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBNonTargetAccN` | 940 | non-target accuracy (%), none T0, qwen3.8-27b, n |
| `\PfourNoneTZeroQwenThreeEightTwoSevenBNonTargetAccP` | n/a | non-target accuracy (%), none T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGemmaFourThreeOneBAsr` | 73.4 | ASR (%), none T0, gemma-4-31b-it |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrLo` | 67.4 | ASR (%), none T0, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrHi` | 79.1 | ASR (%), none T0, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrCI` | [67.4, 79.1] | ASR (%), none T0, gemma-4-31b-it, 95% CI |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrN` | 233 | ASR (%), none T0, gemma-4-31b-it, n |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrP` | n/a | ASR (%), none T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrDropped` | 74.3 | ASR (%) unparsed dropped, none T0, gemma-4-31b-it |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrDroppedLo` | 68.3 | ASR (%) unparsed dropped, none T0, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrDroppedHi` | 80.3 | ASR (%) unparsed dropped, none T0, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrDroppedCI` | [68.3, 80.3] | ASR (%) unparsed dropped, none T0, gemma-4-31b-it, 95% CI |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrDroppedN` | 230 | ASR (%) unparsed dropped, none T0, gemma-4-31b-it, n |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrCleanOk` | 73.5 | ASR / clean correct (%), none T0, gemma-4-31b-it |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrCleanOkLo` | 67.7 | ASR / clean correct (%), none T0, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrCleanOkHi` | 79.5 | ASR / clean correct (%), none T0, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrCleanOkCI` | [67.7, 79.5] | ASR / clean correct (%), none T0, gemma-4-31b-it, 95% CI |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrCleanOkN` | 223 | ASR / clean correct (%), none T0, gemma-4-31b-it, n |
| `\PfourNoneTZeroGemmaFourThreeOneBAsrCleanOkP` | n/a | ASR / clean correct (%), none T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGemmaFourThreeOneBNonTargetAcc` | 98.2 | non-target accuracy (%), none T0, gemma-4-31b-it |
| `\PfourNoneTZeroGemmaFourThreeOneBNonTargetAccLo` | 96.0 | non-target accuracy (%), none T0, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTZeroGemmaFourThreeOneBNonTargetAccHi` | 99.8 | non-target accuracy (%), none T0, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTZeroGemmaFourThreeOneBNonTargetAccCI` | [96.0, 99.8] | non-target accuracy (%), none T0, gemma-4-31b-it, 95% CI |
| `\PfourNoneTZeroGemmaFourThreeOneBNonTargetAccN` | 920 | non-target accuracy (%), none T0, gemma-4-31b-it, n |
| `\PfourNoneTZeroGemmaFourThreeOneBNonTargetAccP` | n/a | non-target accuracy (%), none T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGLMFiveThreeFlashAsr` | 41.3 | ASR (%), none T0, glm-5.3-flash |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrLo` | 36.6 | ASR (%), none T0, glm-5.3-flash, lower 95% CI bound |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrHi` | 45.5 | ASR (%), none T0, glm-5.3-flash, upper 95% CI bound |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrCI` | [36.6, 45.5] | ASR (%), none T0, glm-5.3-flash, 95% CI |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrN` | 235 | ASR (%), none T0, glm-5.3-flash, n |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrP` | n/a | ASR (%), none T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrDropped` | 41.3 | ASR (%) unparsed dropped, none T0, glm-5.3-flash |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrDroppedLo` | 37.0 | ASR (%) unparsed dropped, none T0, glm-5.3-flash, lower 95% CI bound |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrDroppedHi` | 46.0 | ASR (%) unparsed dropped, none T0, glm-5.3-flash, upper 95% CI bound |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrDroppedCI` | [37.0, 46.0] | ASR (%) unparsed dropped, none T0, glm-5.3-flash, 95% CI |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrDroppedN` | 235 | ASR (%) unparsed dropped, none T0, glm-5.3-flash, n |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrCleanOk` | 41.3 | ASR / clean correct (%), none T0, glm-5.3-flash |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrCleanOkLo` | 37.0 | ASR / clean correct (%), none T0, glm-5.3-flash, lower 95% CI bound |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrCleanOkHi` | 46.0 | ASR / clean correct (%), none T0, glm-5.3-flash, upper 95% CI bound |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrCleanOkCI` | [37.0, 46.0] | ASR / clean correct (%), none T0, glm-5.3-flash, 95% CI |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrCleanOkN` | 235 | ASR / clean correct (%), none T0, glm-5.3-flash, n |
| `\PfourNoneTZeroGLMFiveThreeFlashAsrCleanOkP` | n/a | ASR / clean correct (%), none T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGLMFiveThreeFlashNonTargetAcc` | 99.8 | non-target accuracy (%), none T0, glm-5.3-flash |
| `\PfourNoneTZeroGLMFiveThreeFlashNonTargetAccLo` | 99.4 | non-target accuracy (%), none T0, glm-5.3-flash, lower 95% CI bound |
| `\PfourNoneTZeroGLMFiveThreeFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), none T0, glm-5.3-flash, upper 95% CI bound |
| `\PfourNoneTZeroGLMFiveThreeFlashNonTargetAccCI` | [99.4, 100.0] | non-target accuracy (%), none T0, glm-5.3-flash, 95% CI |
| `\PfourNoneTZeroGLMFiveThreeFlashNonTargetAccN` | 940 | non-target accuracy (%), none T0, glm-5.3-flash, n |
| `\PfourNoneTZeroGLMFiveThreeFlashNonTargetAccP` | n/a | non-target accuracy (%), none T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGLMFiveTwoAsr` | 57.9 | ASR (%), none T0, glm-5.2 |
| `\PfourNoneTZeroGLMFiveTwoAsrLo` | 52.8 | ASR (%), none T0, glm-5.2, lower 95% CI bound |
| `\PfourNoneTZeroGLMFiveTwoAsrHi` | 63.0 | ASR (%), none T0, glm-5.2, upper 95% CI bound |
| `\PfourNoneTZeroGLMFiveTwoAsrCI` | [52.8, 63.0] | ASR (%), none T0, glm-5.2, 95% CI |
| `\PfourNoneTZeroGLMFiveTwoAsrN` | 235 | ASR (%), none T0, glm-5.2, n |
| `\PfourNoneTZeroGLMFiveTwoAsrP` | n/a | ASR (%), none T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGLMFiveTwoAsrDropped` | 57.9 | ASR (%) unparsed dropped, none T0, glm-5.2 |
| `\PfourNoneTZeroGLMFiveTwoAsrDroppedLo` | 52.8 | ASR (%) unparsed dropped, none T0, glm-5.2, lower 95% CI bound |
| `\PfourNoneTZeroGLMFiveTwoAsrDroppedHi` | 63.0 | ASR (%) unparsed dropped, none T0, glm-5.2, upper 95% CI bound |
| `\PfourNoneTZeroGLMFiveTwoAsrDroppedCI` | [52.8, 63.0] | ASR (%) unparsed dropped, none T0, glm-5.2, 95% CI |
| `\PfourNoneTZeroGLMFiveTwoAsrDroppedN` | 235 | ASR (%) unparsed dropped, none T0, glm-5.2, n |
| `\PfourNoneTZeroGLMFiveTwoAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGLMFiveTwoAsrCleanOk` | 58.0 | ASR / clean correct (%), none T0, glm-5.2 |
| `\PfourNoneTZeroGLMFiveTwoAsrCleanOkLo` | 52.8 | ASR / clean correct (%), none T0, glm-5.2, lower 95% CI bound |
| `\PfourNoneTZeroGLMFiveTwoAsrCleanOkHi` | 62.9 | ASR / clean correct (%), none T0, glm-5.2, upper 95% CI bound |
| `\PfourNoneTZeroGLMFiveTwoAsrCleanOkCI` | [52.8, 62.9] | ASR / clean correct (%), none T0, glm-5.2, 95% CI |
| `\PfourNoneTZeroGLMFiveTwoAsrCleanOkN` | 231 | ASR / clean correct (%), none T0, glm-5.2, n |
| `\PfourNoneTZeroGLMFiveTwoAsrCleanOkP` | n/a | ASR / clean correct (%), none T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTZeroGLMFiveTwoNonTargetAcc` | 98.0 | non-target accuracy (%), none T0, glm-5.2 |
| `\PfourNoneTZeroGLMFiveTwoNonTargetAccLo` | 95.7 | non-target accuracy (%), none T0, glm-5.2, lower 95% CI bound |
| `\PfourNoneTZeroGLMFiveTwoNonTargetAccHi` | 99.6 | non-target accuracy (%), none T0, glm-5.2, upper 95% CI bound |
| `\PfourNoneTZeroGLMFiveTwoNonTargetAccCI` | [95.7, 99.6] | non-target accuracy (%), none T0, glm-5.2, 95% CI |
| `\PfourNoneTZeroGLMFiveTwoNonTargetAccN` | 940 | non-target accuracy (%), none T0, glm-5.2, n |
| `\PfourNoneTZeroGLMFiveTwoNonTargetAccP` | n/a | non-target accuracy (%), none T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoPooledAsr` | 60.7 | ASR (%), none T2, pooled |
| `\PfourNoneTTwoPooledAsrLo` | 56.5 | ASR (%), none T2, pooled, lower 95% CI bound |
| `\PfourNoneTTwoPooledAsrHi` | 64.7 | ASR (%), none T2, pooled, upper 95% CI bound |
| `\PfourNoneTTwoPooledAsrCI` | [56.5, 64.7] | ASR (%), none T2, pooled, 95% CI |
| `\PfourNoneTTwoPooledAsrN` | 1{,}155 | ASR (%), none T2, pooled, n |
| `\PfourNoneTTwoPooledAsrP` | n/a | ASR (%), none T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoPooledAsrDropped` | 60.9 | ASR (%) unparsed dropped, none T2, pooled |
| `\PfourNoneTTwoPooledAsrDroppedLo` | 56.7 | ASR (%) unparsed dropped, none T2, pooled, lower 95% CI bound |
| `\PfourNoneTTwoPooledAsrDroppedHi` | 64.9 | ASR (%) unparsed dropped, none T2, pooled, upper 95% CI bound |
| `\PfourNoneTTwoPooledAsrDroppedCI` | [56.7, 64.9] | ASR (%) unparsed dropped, none T2, pooled, 95% CI |
| `\PfourNoneTTwoPooledAsrDroppedN` | 1{,}151 | ASR (%) unparsed dropped, none T2, pooled, n |
| `\PfourNoneTTwoPooledAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoPooledAsrCleanOk` | 60.7 | ASR / clean correct (%), none T2, pooled |
| `\PfourNoneTTwoPooledAsrCleanOkLo` | 56.4 | ASR / clean correct (%), none T2, pooled, lower 95% CI bound |
| `\PfourNoneTTwoPooledAsrCleanOkHi` | 64.9 | ASR / clean correct (%), none T2, pooled, upper 95% CI bound |
| `\PfourNoneTTwoPooledAsrCleanOkCI` | [56.4, 64.9] | ASR / clean correct (%), none T2, pooled, 95% CI |
| `\PfourNoneTTwoPooledAsrCleanOkN` | 1{,}127 | ASR / clean correct (%), none T2, pooled, n |
| `\PfourNoneTTwoPooledAsrCleanOkP` | n/a | ASR / clean correct (%), none T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoPooledNonTargetAcc` | 98.0 | non-target accuracy (%), none T2, pooled |
| `\PfourNoneTTwoPooledNonTargetAccLo` | 96.9 | non-target accuracy (%), none T2, pooled, lower 95% CI bound |
| `\PfourNoneTTwoPooledNonTargetAccHi` | 99.0 | non-target accuracy (%), none T2, pooled, upper 95% CI bound |
| `\PfourNoneTTwoPooledNonTargetAccCI` | [96.9, 99.0] | non-target accuracy (%), none T2, pooled, 95% CI |
| `\PfourNoneTTwoPooledNonTargetAccN` | 4{,}604 | non-target accuracy (%), none T2, pooled, n |
| `\PfourNoneTTwoPooledNonTargetAccP` | n/a | non-target accuracy (%), none T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoDeepSeekVFourFlashAsr` | 53.8 | ASR (%), none T2, deepseek-v4-flash |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrLo` | 47.4 | ASR (%), none T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrHi` | 60.1 | ASR (%), none T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrCI` | [47.4, 60.1] | ASR (%), none T2, deepseek-v4-flash, 95% CI |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrN` | 234 | ASR (%), none T2, deepseek-v4-flash, n |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrP` | n/a | ASR (%), none T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrDropped` | 53.8 | ASR (%) unparsed dropped, none T2, deepseek-v4-flash |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrDroppedLo` | 47.2 | ASR (%) unparsed dropped, none T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrDroppedHi` | 60.3 | ASR (%) unparsed dropped, none T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrDroppedCI` | [47.2, 60.3] | ASR (%) unparsed dropped, none T2, deepseek-v4-flash, 95% CI |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrDroppedN` | 234 | ASR (%) unparsed dropped, none T2, deepseek-v4-flash, n |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrCleanOk` | 53.6 | ASR / clean correct (%), none T2, deepseek-v4-flash |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrCleanOkLo` | 47.2 | ASR / clean correct (%), none T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrCleanOkHi` | 60.4 | ASR / clean correct (%), none T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrCleanOkCI` | [47.2, 60.4] | ASR / clean correct (%), none T2, deepseek-v4-flash, 95% CI |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrCleanOkN` | 233 | ASR / clean correct (%), none T2, deepseek-v4-flash, n |
| `\PfourNoneTTwoDeepSeekVFourFlashAsrCleanOkP` | n/a | ASR / clean correct (%), none T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoDeepSeekVFourFlashNonTargetAcc` | 99.6 | non-target accuracy (%), none T2, deepseek-v4-flash |
| `\PfourNoneTTwoDeepSeekVFourFlashNonTargetAccLo` | 98.7 | non-target accuracy (%), none T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTTwoDeepSeekVFourFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), none T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTTwoDeepSeekVFourFlashNonTargetAccCI` | [98.7, 100.0] | non-target accuracy (%), none T2, deepseek-v4-flash, 95% CI |
| `\PfourNoneTTwoDeepSeekVFourFlashNonTargetAccN` | 936 | non-target accuracy (%), none T2, deepseek-v4-flash, n |
| `\PfourNoneTTwoDeepSeekVFourFlashNonTargetAccP` | n/a | non-target accuracy (%), none T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsr` | 55.7 | ASR (%), none T2, qwen3.8-27b |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrLo` | 48.5 | ASR (%), none T2, qwen3.8-27b, lower 95% CI bound |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrHi` | 62.7 | ASR (%), none T2, qwen3.8-27b, upper 95% CI bound |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrCI` | [48.5, 62.7] | ASR (%), none T2, qwen3.8-27b, 95% CI |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrN` | 230 | ASR (%), none T2, qwen3.8-27b, n |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrP` | n/a | ASR (%), none T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrDropped` | 55.7 | ASR (%) unparsed dropped, none T2, qwen3.8-27b |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrDroppedLo` | 48.9 | ASR (%) unparsed dropped, none T2, qwen3.8-27b, lower 95% CI bound |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrDroppedHi` | 62.4 | ASR (%) unparsed dropped, none T2, qwen3.8-27b, upper 95% CI bound |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrDroppedCI` | [48.9, 62.4] | ASR (%) unparsed dropped, none T2, qwen3.8-27b, 95% CI |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrDroppedN` | 230 | ASR (%) unparsed dropped, none T2, qwen3.8-27b, n |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrCleanOk` | 55.0 | ASR / clean correct (%), none T2, qwen3.8-27b |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrCleanOkLo` | 47.8 | ASR / clean correct (%), none T2, qwen3.8-27b, lower 95% CI bound |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrCleanOkHi` | 62.2 | ASR / clean correct (%), none T2, qwen3.8-27b, upper 95% CI bound |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrCleanOkCI` | [47.8, 62.2] | ASR / clean correct (%), none T2, qwen3.8-27b, 95% CI |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrCleanOkN` | 218 | ASR / clean correct (%), none T2, qwen3.8-27b, n |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBAsrCleanOkP` | n/a | ASR / clean correct (%), none T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBNonTargetAcc` | 94.6 | non-target accuracy (%), none T2, qwen3.8-27b |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBNonTargetAccLo` | 91.8 | non-target accuracy (%), none T2, qwen3.8-27b, lower 95% CI bound |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBNonTargetAccHi` | 97.0 | non-target accuracy (%), none T2, qwen3.8-27b, upper 95% CI bound |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBNonTargetAccCI` | [91.8, 97.0] | non-target accuracy (%), none T2, qwen3.8-27b, 95% CI |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBNonTargetAccN` | 920 | non-target accuracy (%), none T2, qwen3.8-27b, n |
| `\PfourNoneTTwoQwenThreeEightTwoSevenBNonTargetAccP` | n/a | non-target accuracy (%), none T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGemmaFourThreeOneBAsr` | 72.6 | ASR (%), none T2, gemma-4-31b-it |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrLo` | 67.3 | ASR (%), none T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrHi` | 77.6 | ASR (%), none T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrCI` | [67.3, 77.6] | ASR (%), none T2, gemma-4-31b-it, 95% CI |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrN` | 223 | ASR (%), none T2, gemma-4-31b-it, n |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrP` | n/a | ASR (%), none T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrDropped` | 73.6 | ASR (%) unparsed dropped, none T2, gemma-4-31b-it |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrDroppedLo` | 68.5 | ASR (%) unparsed dropped, none T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrDroppedHi` | 78.8 | ASR (%) unparsed dropped, none T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrDroppedCI` | [68.5, 78.8] | ASR (%) unparsed dropped, none T2, gemma-4-31b-it, 95% CI |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrDroppedN` | 220 | ASR (%) unparsed dropped, none T2, gemma-4-31b-it, n |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrCleanOk` | 73.2 | ASR / clean correct (%), none T2, gemma-4-31b-it |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrCleanOkLo` | 67.9 | ASR / clean correct (%), none T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrCleanOkHi` | 78.3 | ASR / clean correct (%), none T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrCleanOkCI` | [67.9, 78.3] | ASR / clean correct (%), none T2, gemma-4-31b-it, 95% CI |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrCleanOkN` | 213 | ASR / clean correct (%), none T2, gemma-4-31b-it, n |
| `\PfourNoneTTwoGemmaFourThreeOneBAsrCleanOkP` | n/a | ASR / clean correct (%), none T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGemmaFourThreeOneBNonTargetAcc` | 98.3 | non-target accuracy (%), none T2, gemma-4-31b-it |
| `\PfourNoneTTwoGemmaFourThreeOneBNonTargetAccLo` | 96.2 | non-target accuracy (%), none T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTTwoGemmaFourThreeOneBNonTargetAccHi` | 100.0 | non-target accuracy (%), none T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTTwoGemmaFourThreeOneBNonTargetAccCI` | [96.2, 100.0] | non-target accuracy (%), none T2, gemma-4-31b-it, 95% CI |
| `\PfourNoneTTwoGemmaFourThreeOneBNonTargetAccN` | 880 | non-target accuracy (%), none T2, gemma-4-31b-it, n |
| `\PfourNoneTTwoGemmaFourThreeOneBNonTargetAccP` | n/a | non-target accuracy (%), none T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGLMFiveThreeFlashAsr` | 59.8 | ASR (%), none T2, glm-5.3-flash |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrLo` | 54.5 | ASR (%), none T2, glm-5.3-flash, lower 95% CI bound |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrHi` | 65.2 | ASR (%), none T2, glm-5.3-flash, upper 95% CI bound |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrCI` | [54.5, 65.2] | ASR (%), none T2, glm-5.3-flash, 95% CI |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrN` | 234 | ASR (%), none T2, glm-5.3-flash, n |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrP` | n/a | ASR (%), none T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrDropped` | 60.1 | ASR (%) unparsed dropped, none T2, glm-5.3-flash |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrDroppedLo` | 55.1 | ASR (%) unparsed dropped, none T2, glm-5.3-flash, lower 95% CI bound |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrDroppedHi` | 65.1 | ASR (%) unparsed dropped, none T2, glm-5.3-flash, upper 95% CI bound |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrDroppedCI` | [55.1, 65.1] | ASR (%) unparsed dropped, none T2, glm-5.3-flash, 95% CI |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrDroppedN` | 233 | ASR (%) unparsed dropped, none T2, glm-5.3-flash, n |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrCleanOk` | 60.1 | ASR / clean correct (%), none T2, glm-5.3-flash |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrCleanOkLo` | 55.0 | ASR / clean correct (%), none T2, glm-5.3-flash, lower 95% CI bound |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrCleanOkHi` | 65.0 | ASR / clean correct (%), none T2, glm-5.3-flash, upper 95% CI bound |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrCleanOkCI` | [55.0, 65.0] | ASR / clean correct (%), none T2, glm-5.3-flash, 95% CI |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrCleanOkN` | 233 | ASR / clean correct (%), none T2, glm-5.3-flash, n |
| `\PfourNoneTTwoGLMFiveThreeFlashAsrCleanOkP` | n/a | ASR / clean correct (%), none T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGLMFiveThreeFlashNonTargetAcc` | 99.6 | non-target accuracy (%), none T2, glm-5.3-flash |
| `\PfourNoneTTwoGLMFiveThreeFlashNonTargetAccLo` | 99.0 | non-target accuracy (%), none T2, glm-5.3-flash, lower 95% CI bound |
| `\PfourNoneTTwoGLMFiveThreeFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), none T2, glm-5.3-flash, upper 95% CI bound |
| `\PfourNoneTTwoGLMFiveThreeFlashNonTargetAccCI` | [99.0, 100.0] | non-target accuracy (%), none T2, glm-5.3-flash, 95% CI |
| `\PfourNoneTTwoGLMFiveThreeFlashNonTargetAccN` | 932 | non-target accuracy (%), none T2, glm-5.3-flash, n |
| `\PfourNoneTTwoGLMFiveThreeFlashNonTargetAccP` | n/a | non-target accuracy (%), none T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGLMFiveTwoAsr` | 62.0 | ASR (%), none T2, glm-5.2 |
| `\PfourNoneTTwoGLMFiveTwoAsrLo` | 57.3 | ASR (%), none T2, glm-5.2, lower 95% CI bound |
| `\PfourNoneTTwoGLMFiveTwoAsrHi` | 66.4 | ASR (%), none T2, glm-5.2, upper 95% CI bound |
| `\PfourNoneTTwoGLMFiveTwoAsrCI` | [57.3, 66.4] | ASR (%), none T2, glm-5.2, 95% CI |
| `\PfourNoneTTwoGLMFiveTwoAsrN` | 234 | ASR (%), none T2, glm-5.2, n |
| `\PfourNoneTTwoGLMFiveTwoAsrP` | n/a | ASR (%), none T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGLMFiveTwoAsrDropped` | 62.0 | ASR (%) unparsed dropped, none T2, glm-5.2 |
| `\PfourNoneTTwoGLMFiveTwoAsrDroppedLo` | 57.3 | ASR (%) unparsed dropped, none T2, glm-5.2, lower 95% CI bound |
| `\PfourNoneTTwoGLMFiveTwoAsrDroppedHi` | 66.4 | ASR (%) unparsed dropped, none T2, glm-5.2, upper 95% CI bound |
| `\PfourNoneTTwoGLMFiveTwoAsrDroppedCI` | [57.3, 66.4] | ASR (%) unparsed dropped, none T2, glm-5.2, 95% CI |
| `\PfourNoneTTwoGLMFiveTwoAsrDroppedN` | 234 | ASR (%) unparsed dropped, none T2, glm-5.2, n |
| `\PfourNoneTTwoGLMFiveTwoAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGLMFiveTwoAsrCleanOk` | 62.2 | ASR / clean correct (%), none T2, glm-5.2 |
| `\PfourNoneTTwoGLMFiveTwoAsrCleanOkLo` | 57.4 | ASR / clean correct (%), none T2, glm-5.2, lower 95% CI bound |
| `\PfourNoneTTwoGLMFiveTwoAsrCleanOkHi` | 66.7 | ASR / clean correct (%), none T2, glm-5.2, upper 95% CI bound |
| `\PfourNoneTTwoGLMFiveTwoAsrCleanOkCI` | [57.4, 66.7] | ASR / clean correct (%), none T2, glm-5.2, 95% CI |
| `\PfourNoneTTwoGLMFiveTwoAsrCleanOkN` | 230 | ASR / clean correct (%), none T2, glm-5.2, n |
| `\PfourNoneTTwoGLMFiveTwoAsrCleanOkP` | n/a | ASR / clean correct (%), none T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTTwoGLMFiveTwoNonTargetAcc` | 98.0 | non-target accuracy (%), none T2, glm-5.2 |
| `\PfourNoneTTwoGLMFiveTwoNonTargetAccLo` | 96.0 | non-target accuracy (%), none T2, glm-5.2, lower 95% CI bound |
| `\PfourNoneTTwoGLMFiveTwoNonTargetAccHi` | 99.6 | non-target accuracy (%), none T2, glm-5.2, upper 95% CI bound |
| `\PfourNoneTTwoGLMFiveTwoNonTargetAccCI` | [96.0, 99.6] | non-target accuracy (%), none T2, glm-5.2, 95% CI |
| `\PfourNoneTTwoGLMFiveTwoNonTargetAccN` | 936 | non-target accuracy (%), none T2, glm-5.2, n |
| `\PfourNoneTTwoGLMFiveTwoNonTargetAccP` | n/a | non-target accuracy (%), none T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreePooledAsr` | 63.3 | ASR (%), none T3, pooled |
| `\PfourNoneTThreePooledAsrLo` | 59.1 | ASR (%), none T3, pooled, lower 95% CI bound |
| `\PfourNoneTThreePooledAsrHi` | 67.3 | ASR (%), none T3, pooled, upper 95% CI bound |
| `\PfourNoneTThreePooledAsrCI` | [59.1, 67.3] | ASR (%), none T3, pooled, 95% CI |
| `\PfourNoneTThreePooledAsrN` | 1{,}168 | ASR (%), none T3, pooled, n |
| `\PfourNoneTThreePooledAsrP` | n/a | ASR (%), none T3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreePooledAsrDropped` | 63.3 | ASR (%) unparsed dropped, none T3, pooled |
| `\PfourNoneTThreePooledAsrDroppedLo` | 59.1 | ASR (%) unparsed dropped, none T3, pooled, lower 95% CI bound |
| `\PfourNoneTThreePooledAsrDroppedHi` | 67.3 | ASR (%) unparsed dropped, none T3, pooled, upper 95% CI bound |
| `\PfourNoneTThreePooledAsrDroppedCI` | [59.1, 67.3] | ASR (%) unparsed dropped, none T3, pooled, 95% CI |
| `\PfourNoneTThreePooledAsrDroppedN` | 1{,}168 | ASR (%) unparsed dropped, none T3, pooled, n |
| `\PfourNoneTThreePooledAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreePooledAsrCleanOk` | 63.0 | ASR / clean correct (%), none T3, pooled |
| `\PfourNoneTThreePooledAsrCleanOkLo` | 58.8 | ASR / clean correct (%), none T3, pooled, lower 95% CI bound |
| `\PfourNoneTThreePooledAsrCleanOkHi` | 67.3 | ASR / clean correct (%), none T3, pooled, upper 95% CI bound |
| `\PfourNoneTThreePooledAsrCleanOkCI` | [58.8, 67.3] | ASR / clean correct (%), none T3, pooled, 95% CI |
| `\PfourNoneTThreePooledAsrCleanOkN` | 1{,}143 | ASR / clean correct (%), none T3, pooled, n |
| `\PfourNoneTThreePooledAsrCleanOkP` | n/a | ASR / clean correct (%), none T3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreePooledNonTargetAcc` | 98.0 | non-target accuracy (%), none T3, pooled |
| `\PfourNoneTThreePooledNonTargetAccLo` | 97.0 | non-target accuracy (%), none T3, pooled, lower 95% CI bound |
| `\PfourNoneTThreePooledNonTargetAccHi` | 98.9 | non-target accuracy (%), none T3, pooled, upper 95% CI bound |
| `\PfourNoneTThreePooledNonTargetAccCI` | [97.0, 98.9] | non-target accuracy (%), none T3, pooled, 95% CI |
| `\PfourNoneTThreePooledNonTargetAccN` | 4{,}672 | non-target accuracy (%), none T3, pooled, n |
| `\PfourNoneTThreePooledNonTargetAccP` | n/a | non-target accuracy (%), none T3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeDeepSeekVFourFlashAsr` | 63.4 | ASR (%), none T3, deepseek-v4-flash |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrLo` | 57.4 | ASR (%), none T3, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrHi` | 69.8 | ASR (%), none T3, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrCI` | [57.4, 69.8] | ASR (%), none T3, deepseek-v4-flash, 95% CI |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrN` | 235 | ASR (%), none T3, deepseek-v4-flash, n |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrP` | n/a | ASR (%), none T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrDropped` | 63.4 | ASR (%) unparsed dropped, none T3, deepseek-v4-flash |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrDroppedLo` | 57.4 | ASR (%) unparsed dropped, none T3, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrDroppedHi` | 69.4 | ASR (%) unparsed dropped, none T3, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrDroppedCI` | [57.4, 69.4] | ASR (%) unparsed dropped, none T3, deepseek-v4-flash, 95% CI |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrDroppedN` | 235 | ASR (%) unparsed dropped, none T3, deepseek-v4-flash, n |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrCleanOk` | 63.2 | ASR / clean correct (%), none T3, deepseek-v4-flash |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrCleanOkLo` | 57.3 | ASR / clean correct (%), none T3, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrCleanOkHi` | 69.2 | ASR / clean correct (%), none T3, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrCleanOkCI` | [57.3, 69.2] | ASR / clean correct (%), none T3, deepseek-v4-flash, 95% CI |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrCleanOkN` | 234 | ASR / clean correct (%), none T3, deepseek-v4-flash, n |
| `\PfourNoneTThreeDeepSeekVFourFlashAsrCleanOkP` | n/a | ASR / clean correct (%), none T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeDeepSeekVFourFlashNonTargetAcc` | 99.7 | non-target accuracy (%), none T3, deepseek-v4-flash |
| `\PfourNoneTThreeDeepSeekVFourFlashNonTargetAccLo` | 99.0 | non-target accuracy (%), none T3, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneTThreeDeepSeekVFourFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), none T3, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneTThreeDeepSeekVFourFlashNonTargetAccCI` | [99.0, 100.0] | non-target accuracy (%), none T3, deepseek-v4-flash, 95% CI |
| `\PfourNoneTThreeDeepSeekVFourFlashNonTargetAccN` | 940 | non-target accuracy (%), none T3, deepseek-v4-flash, n |
| `\PfourNoneTThreeDeepSeekVFourFlashNonTargetAccP` | n/a | non-target accuracy (%), none T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsr` | 62.2 | ASR (%), none T3, qwen3.8-27b |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrLo` | 56.2 | ASR (%), none T3, qwen3.8-27b, lower 95% CI bound |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrHi` | 68.4 | ASR (%), none T3, qwen3.8-27b, upper 95% CI bound |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrCI` | [56.2, 68.4] | ASR (%), none T3, qwen3.8-27b, 95% CI |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrN` | 233 | ASR (%), none T3, qwen3.8-27b, n |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrP` | n/a | ASR (%), none T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrDropped` | 62.2 | ASR (%) unparsed dropped, none T3, qwen3.8-27b |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrDroppedLo` | 56.0 | ASR (%) unparsed dropped, none T3, qwen3.8-27b, lower 95% CI bound |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrDroppedHi` | 68.2 | ASR (%) unparsed dropped, none T3, qwen3.8-27b, upper 95% CI bound |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrDroppedCI` | [56.0, 68.2] | ASR (%) unparsed dropped, none T3, qwen3.8-27b, 95% CI |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrDroppedN` | 233 | ASR (%) unparsed dropped, none T3, qwen3.8-27b, n |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrCleanOk` | 62.0 | ASR / clean correct (%), none T3, qwen3.8-27b |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrCleanOkLo` | 55.5 | ASR / clean correct (%), none T3, qwen3.8-27b, lower 95% CI bound |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrCleanOkHi` | 67.9 | ASR / clean correct (%), none T3, qwen3.8-27b, upper 95% CI bound |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrCleanOkCI` | [55.5, 67.9] | ASR / clean correct (%), none T3, qwen3.8-27b, 95% CI |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrCleanOkN` | 221 | ASR / clean correct (%), none T3, qwen3.8-27b, n |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBAsrCleanOkP` | n/a | ASR / clean correct (%), none T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBNonTargetAcc` | 94.1 | non-target accuracy (%), none T3, qwen3.8-27b |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBNonTargetAccLo` | 91.5 | non-target accuracy (%), none T3, qwen3.8-27b, lower 95% CI bound |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBNonTargetAccHi` | 96.5 | non-target accuracy (%), none T3, qwen3.8-27b, upper 95% CI bound |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBNonTargetAccCI` | [91.5, 96.5] | non-target accuracy (%), none T3, qwen3.8-27b, 95% CI |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBNonTargetAccN` | 932 | non-target accuracy (%), none T3, qwen3.8-27b, n |
| `\PfourNoneTThreeQwenThreeEightTwoSevenBNonTargetAccP` | n/a | non-target accuracy (%), none T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGemmaFourThreeOneBAsr` | 74.8 | ASR (%), none T3, gemma-4-31b-it |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrLo` | 70.0 | ASR (%), none T3, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrHi` | 79.6 | ASR (%), none T3, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrCI` | [70.0, 79.6] | ASR (%), none T3, gemma-4-31b-it, 95% CI |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrN` | 230 | ASR (%), none T3, gemma-4-31b-it, n |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrP` | n/a | ASR (%), none T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrDropped` | 74.8 | ASR (%) unparsed dropped, none T3, gemma-4-31b-it |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrDroppedLo` | 70.0 | ASR (%) unparsed dropped, none T3, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrDroppedHi` | 79.6 | ASR (%) unparsed dropped, none T3, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrDroppedCI` | [70.0, 79.6] | ASR (%) unparsed dropped, none T3, gemma-4-31b-it, 95% CI |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrDroppedN` | 230 | ASR (%) unparsed dropped, none T3, gemma-4-31b-it, n |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrCleanOk` | 73.9 | ASR / clean correct (%), none T3, gemma-4-31b-it |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrCleanOkLo` | 69.0 | ASR / clean correct (%), none T3, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrCleanOkHi` | 78.7 | ASR / clean correct (%), none T3, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrCleanOkCI` | [69.0, 78.7] | ASR / clean correct (%), none T3, gemma-4-31b-it, 95% CI |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrCleanOkN` | 222 | ASR / clean correct (%), none T3, gemma-4-31b-it, n |
| `\PfourNoneTThreeGemmaFourThreeOneBAsrCleanOkP` | n/a | ASR / clean correct (%), none T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGemmaFourThreeOneBNonTargetAcc` | 98.4 | non-target accuracy (%), none T3, gemma-4-31b-it |
| `\PfourNoneTThreeGemmaFourThreeOneBNonTargetAccLo` | 96.3 | non-target accuracy (%), none T3, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneTThreeGemmaFourThreeOneBNonTargetAccHi` | 99.9 | non-target accuracy (%), none T3, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneTThreeGemmaFourThreeOneBNonTargetAccCI` | [96.3, 99.9] | non-target accuracy (%), none T3, gemma-4-31b-it, 95% CI |
| `\PfourNoneTThreeGemmaFourThreeOneBNonTargetAccN` | 920 | non-target accuracy (%), none T3, gemma-4-31b-it, n |
| `\PfourNoneTThreeGemmaFourThreeOneBNonTargetAccP` | n/a | non-target accuracy (%), none T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGLMFiveThreeFlashAsr` | 57.0 | ASR (%), none T3, glm-5.3-flash |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrLo` | 52.3 | ASR (%), none T3, glm-5.3-flash, lower 95% CI bound |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrHi` | 61.3 | ASR (%), none T3, glm-5.3-flash, upper 95% CI bound |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrCI` | [52.3, 61.3] | ASR (%), none T3, glm-5.3-flash, 95% CI |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrN` | 235 | ASR (%), none T3, glm-5.3-flash, n |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrP` | n/a | ASR (%), none T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrDropped` | 57.0 | ASR (%) unparsed dropped, none T3, glm-5.3-flash |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrDroppedLo` | 52.3 | ASR (%) unparsed dropped, none T3, glm-5.3-flash, lower 95% CI bound |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrDroppedHi` | 61.7 | ASR (%) unparsed dropped, none T3, glm-5.3-flash, upper 95% CI bound |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrDroppedCI` | [52.3, 61.7] | ASR (%) unparsed dropped, none T3, glm-5.3-flash, 95% CI |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrDroppedN` | 235 | ASR (%) unparsed dropped, none T3, glm-5.3-flash, n |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrCleanOk` | 57.0 | ASR / clean correct (%), none T3, glm-5.3-flash |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrCleanOkLo` | 52.8 | ASR / clean correct (%), none T3, glm-5.3-flash, lower 95% CI bound |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrCleanOkHi` | 61.7 | ASR / clean correct (%), none T3, glm-5.3-flash, upper 95% CI bound |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrCleanOkCI` | [52.8, 61.7] | ASR / clean correct (%), none T3, glm-5.3-flash, 95% CI |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrCleanOkN` | 235 | ASR / clean correct (%), none T3, glm-5.3-flash, n |
| `\PfourNoneTThreeGLMFiveThreeFlashAsrCleanOkP` | n/a | ASR / clean correct (%), none T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGLMFiveThreeFlashNonTargetAcc` | 100.0 | non-target accuracy (%), none T3, glm-5.3-flash |
| `\PfourNoneTThreeGLMFiveThreeFlashNonTargetAccLo` | 99.6 | non-target accuracy (%), none T3, glm-5.3-flash, lower 95% CI bound |
| `\PfourNoneTThreeGLMFiveThreeFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), none T3, glm-5.3-flash, upper 95% CI bound |
| `\PfourNoneTThreeGLMFiveThreeFlashNonTargetAccCI` | [99.6, 100.0] | non-target accuracy (%), none T3, glm-5.3-flash, 95% CI |
| `\PfourNoneTThreeGLMFiveThreeFlashNonTargetAccN` | 940 | non-target accuracy (%), none T3, glm-5.3-flash, n |
| `\PfourNoneTThreeGLMFiveThreeFlashNonTargetAccP` | n/a | non-target accuracy (%), none T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGLMFiveTwoAsr` | 59.1 | ASR (%), none T3, glm-5.2 |
| `\PfourNoneTThreeGLMFiveTwoAsrLo` | 54.0 | ASR (%), none T3, glm-5.2, lower 95% CI bound |
| `\PfourNoneTThreeGLMFiveTwoAsrHi` | 64.3 | ASR (%), none T3, glm-5.2, upper 95% CI bound |
| `\PfourNoneTThreeGLMFiveTwoAsrCI` | [54.0, 64.3] | ASR (%), none T3, glm-5.2, 95% CI |
| `\PfourNoneTThreeGLMFiveTwoAsrN` | 235 | ASR (%), none T3, glm-5.2, n |
| `\PfourNoneTThreeGLMFiveTwoAsrP` | n/a | ASR (%), none T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGLMFiveTwoAsrDropped` | 59.1 | ASR (%) unparsed dropped, none T3, glm-5.2 |
| `\PfourNoneTThreeGLMFiveTwoAsrDroppedLo` | 54.5 | ASR (%) unparsed dropped, none T3, glm-5.2, lower 95% CI bound |
| `\PfourNoneTThreeGLMFiveTwoAsrDroppedHi` | 64.3 | ASR (%) unparsed dropped, none T3, glm-5.2, upper 95% CI bound |
| `\PfourNoneTThreeGLMFiveTwoAsrDroppedCI` | [54.5, 64.3] | ASR (%) unparsed dropped, none T3, glm-5.2, 95% CI |
| `\PfourNoneTThreeGLMFiveTwoAsrDroppedN` | 235 | ASR (%) unparsed dropped, none T3, glm-5.2, n |
| `\PfourNoneTThreeGLMFiveTwoAsrDroppedP` | n/a | ASR (%) unparsed dropped, none T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGLMFiveTwoAsrCleanOk` | 59.3 | ASR / clean correct (%), none T3, glm-5.2 |
| `\PfourNoneTThreeGLMFiveTwoAsrCleanOkLo` | 54.3 | ASR / clean correct (%), none T3, glm-5.2, lower 95% CI bound |
| `\PfourNoneTThreeGLMFiveTwoAsrCleanOkHi` | 64.8 | ASR / clean correct (%), none T3, glm-5.2, upper 95% CI bound |
| `\PfourNoneTThreeGLMFiveTwoAsrCleanOkCI` | [54.3, 64.8] | ASR / clean correct (%), none T3, glm-5.2, 95% CI |
| `\PfourNoneTThreeGLMFiveTwoAsrCleanOkN` | 231 | ASR / clean correct (%), none T3, glm-5.2, n |
| `\PfourNoneTThreeGLMFiveTwoAsrCleanOkP` | n/a | ASR / clean correct (%), none T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneTThreeGLMFiveTwoNonTargetAcc` | 97.9 | non-target accuracy (%), none T3, glm-5.2 |
| `\PfourNoneTThreeGLMFiveTwoNonTargetAccLo` | 95.6 | non-target accuracy (%), none T3, glm-5.2, lower 95% CI bound |
| `\PfourNoneTThreeGLMFiveTwoNonTargetAccHi` | 99.6 | non-target accuracy (%), none T3, glm-5.2, upper 95% CI bound |
| `\PfourNoneTThreeGLMFiveTwoNonTargetAccCI` | [95.6, 99.6] | non-target accuracy (%), none T3, glm-5.2, 95% CI |
| `\PfourNoneTThreeGLMFiveTwoNonTargetAccN` | 940 | non-target accuracy (%), none T3, glm-5.2, n |
| `\PfourNoneTThreeGLMFiveTwoNonTargetAccP` | n/a | non-target accuracy (%), none T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryPooledAsr` | 12.0 | ASR (%), no_memory -, pooled |
| `\PfourNoMemoryPooledAsrLo` | 9.6 | ASR (%), no_memory -, pooled, lower 95% CI bound |
| `\PfourNoMemoryPooledAsrHi` | 14.4 | ASR (%), no_memory -, pooled, upper 95% CI bound |
| `\PfourNoMemoryPooledAsrCI` | [9.6, 14.4] | ASR (%), no_memory -, pooled, 95% CI |
| `\PfourNoMemoryPooledAsrN` | 1{,}173 | ASR (%), no_memory -, pooled, n |
| `\PfourNoMemoryPooledAsrP` | n/a | ASR (%), no_memory -, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryPooledAsrDropped` | 12.1 | ASR (%) unparsed dropped, no_memory -, pooled |
| `\PfourNoMemoryPooledAsrDroppedLo` | 9.7 | ASR (%) unparsed dropped, no_memory -, pooled, lower 95% CI bound |
| `\PfourNoMemoryPooledAsrDroppedHi` | 14.4 | ASR (%) unparsed dropped, no_memory -, pooled, upper 95% CI bound |
| `\PfourNoMemoryPooledAsrDroppedCI` | [9.7, 14.4] | ASR (%) unparsed dropped, no_memory -, pooled, 95% CI |
| `\PfourNoMemoryPooledAsrDroppedN` | 1{,}168 | ASR (%) unparsed dropped, no_memory -, pooled, n |
| `\PfourNoMemoryPooledAsrDroppedP` | n/a | ASR (%) unparsed dropped, no_memory -, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryPooledAsrCleanOk` | 12.1 | ASR / clean correct (%), no_memory -, pooled |
| `\PfourNoMemoryPooledAsrCleanOkLo` | 9.7 | ASR / clean correct (%), no_memory -, pooled, lower 95% CI bound |
| `\PfourNoMemoryPooledAsrCleanOkHi` | 14.8 | ASR / clean correct (%), no_memory -, pooled, upper 95% CI bound |
| `\PfourNoMemoryPooledAsrCleanOkCI` | [9.7, 14.8] | ASR / clean correct (%), no_memory -, pooled, 95% CI |
| `\PfourNoMemoryPooledAsrCleanOkN` | 1{,}143 | ASR / clean correct (%), no_memory -, pooled, n |
| `\PfourNoMemoryPooledAsrCleanOkP` | n/a | ASR / clean correct (%), no_memory -, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryPooledNonTargetAcc` | 97.8 | non-target accuracy (%), no_memory -, pooled |
| `\PfourNoMemoryPooledNonTargetAccLo` | 96.7 | non-target accuracy (%), no_memory -, pooled, lower 95% CI bound |
| `\PfourNoMemoryPooledNonTargetAccHi` | 98.8 | non-target accuracy (%), no_memory -, pooled, upper 95% CI bound |
| `\PfourNoMemoryPooledNonTargetAccCI` | [96.7, 98.8] | non-target accuracy (%), no_memory -, pooled, 95% CI |
| `\PfourNoMemoryPooledNonTargetAccN` | 4{,}672 | non-target accuracy (%), no_memory -, pooled, n |
| `\PfourNoMemoryPooledNonTargetAccP` | n/a | non-target accuracy (%), no_memory -, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryDeepSeekVFourFlashAsr` | 16.2 | ASR (%), no_memory -, deepseek-v4-flash |
| `\PfourNoMemoryDeepSeekVFourFlashAsrLo` | 12.3 | ASR (%), no_memory -, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoMemoryDeepSeekVFourFlashAsrHi` | 20.0 | ASR (%), no_memory -, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoMemoryDeepSeekVFourFlashAsrCI` | [12.3, 20.0] | ASR (%), no_memory -, deepseek-v4-flash, 95% CI |
| `\PfourNoMemoryDeepSeekVFourFlashAsrN` | 235 | ASR (%), no_memory -, deepseek-v4-flash, n |
| `\PfourNoMemoryDeepSeekVFourFlashAsrP` | n/a | ASR (%), no_memory -, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryDeepSeekVFourFlashAsrDropped` | 16.2 | ASR (%) unparsed dropped, no_memory -, deepseek-v4-flash |
| `\PfourNoMemoryDeepSeekVFourFlashAsrDroppedLo` | 12.3 | ASR (%) unparsed dropped, no_memory -, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoMemoryDeepSeekVFourFlashAsrDroppedHi` | 20.0 | ASR (%) unparsed dropped, no_memory -, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoMemoryDeepSeekVFourFlashAsrDroppedCI` | [12.3, 20.0] | ASR (%) unparsed dropped, no_memory -, deepseek-v4-flash, 95% CI |
| `\PfourNoMemoryDeepSeekVFourFlashAsrDroppedN` | 235 | ASR (%) unparsed dropped, no_memory -, deepseek-v4-flash, n |
| `\PfourNoMemoryDeepSeekVFourFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, no_memory -, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryDeepSeekVFourFlashAsrCleanOk` | 16.2 | ASR / clean correct (%), no_memory -, deepseek-v4-flash |
| `\PfourNoMemoryDeepSeekVFourFlashAsrCleanOkLo` | 12.4 | ASR / clean correct (%), no_memory -, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoMemoryDeepSeekVFourFlashAsrCleanOkHi` | 20.1 | ASR / clean correct (%), no_memory -, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoMemoryDeepSeekVFourFlashAsrCleanOkCI` | [12.4, 20.1] | ASR / clean correct (%), no_memory -, deepseek-v4-flash, 95% CI |
| `\PfourNoMemoryDeepSeekVFourFlashAsrCleanOkN` | 234 | ASR / clean correct (%), no_memory -, deepseek-v4-flash, n |
| `\PfourNoMemoryDeepSeekVFourFlashAsrCleanOkP` | n/a | ASR / clean correct (%), no_memory -, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryDeepSeekVFourFlashNonTargetAcc` | 99.5 | non-target accuracy (%), no_memory -, deepseek-v4-flash |
| `\PfourNoMemoryDeepSeekVFourFlashNonTargetAccLo` | 98.7 | non-target accuracy (%), no_memory -, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoMemoryDeepSeekVFourFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), no_memory -, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoMemoryDeepSeekVFourFlashNonTargetAccCI` | [98.7, 100.0] | non-target accuracy (%), no_memory -, deepseek-v4-flash, 95% CI |
| `\PfourNoMemoryDeepSeekVFourFlashNonTargetAccN` | 940 | non-target accuracy (%), no_memory -, deepseek-v4-flash, n |
| `\PfourNoMemoryDeepSeekVFourFlashNonTargetAccP` | n/a | non-target accuracy (%), no_memory -, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsr` | 13.6 | ASR (%), no_memory -, qwen3.8-27b |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrLo` | 10.2 | ASR (%), no_memory -, qwen3.8-27b, lower 95% CI bound |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrHi` | 17.4 | ASR (%), no_memory -, qwen3.8-27b, upper 95% CI bound |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrCI` | [10.2, 17.4] | ASR (%), no_memory -, qwen3.8-27b, 95% CI |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrN` | 235 | ASR (%), no_memory -, qwen3.8-27b, n |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrP` | n/a | ASR (%), no_memory -, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrDropped` | 13.7 | ASR (%) unparsed dropped, no_memory -, qwen3.8-27b |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrDroppedLo` | 10.2 | ASR (%) unparsed dropped, no_memory -, qwen3.8-27b, lower 95% CI bound |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrDroppedHi` | 17.2 | ASR (%) unparsed dropped, no_memory -, qwen3.8-27b, upper 95% CI bound |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrDroppedCI` | [10.2, 17.2] | ASR (%) unparsed dropped, no_memory -, qwen3.8-27b, 95% CI |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrDroppedN` | 234 | ASR (%) unparsed dropped, no_memory -, qwen3.8-27b, n |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrDroppedP` | n/a | ASR (%) unparsed dropped, no_memory -, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrCleanOk` | 13.1 | ASR / clean correct (%), no_memory -, qwen3.8-27b |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrCleanOkLo` | 9.3 | ASR / clean correct (%), no_memory -, qwen3.8-27b, lower 95% CI bound |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrCleanOkHi` | 16.9 | ASR / clean correct (%), no_memory -, qwen3.8-27b, upper 95% CI bound |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrCleanOkCI` | [9.3, 16.9] | ASR / clean correct (%), no_memory -, qwen3.8-27b, 95% CI |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrCleanOkN` | 222 | ASR / clean correct (%), no_memory -, qwen3.8-27b, n |
| `\PfourNoMemoryQwenThreeEightTwoSevenBAsrCleanOkP` | n/a | ASR / clean correct (%), no_memory -, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryQwenThreeEightTwoSevenBNonTargetAcc` | 93.7 | non-target accuracy (%), no_memory -, qwen3.8-27b |
| `\PfourNoMemoryQwenThreeEightTwoSevenBNonTargetAccLo` | 91.1 | non-target accuracy (%), no_memory -, qwen3.8-27b, lower 95% CI bound |
| `\PfourNoMemoryQwenThreeEightTwoSevenBNonTargetAccHi` | 96.2 | non-target accuracy (%), no_memory -, qwen3.8-27b, upper 95% CI bound |
| `\PfourNoMemoryQwenThreeEightTwoSevenBNonTargetAccCI` | [91.1, 96.2] | non-target accuracy (%), no_memory -, qwen3.8-27b, 95% CI |
| `\PfourNoMemoryQwenThreeEightTwoSevenBNonTargetAccN` | 936 | non-target accuracy (%), no_memory -, qwen3.8-27b, n |
| `\PfourNoMemoryQwenThreeEightTwoSevenBNonTargetAccP` | n/a | non-target accuracy (%), no_memory -, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGemmaFourThreeOneBAsr` | 8.2 | ASR (%), no_memory -, gemma-4-31b-it |
| `\PfourNoMemoryGemmaFourThreeOneBAsrLo` | 4.8 | ASR (%), no_memory -, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoMemoryGemmaFourThreeOneBAsrHi` | 11.6 | ASR (%), no_memory -, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoMemoryGemmaFourThreeOneBAsrCI` | [4.8, 11.6] | ASR (%), no_memory -, gemma-4-31b-it, 95% CI |
| `\PfourNoMemoryGemmaFourThreeOneBAsrN` | 233 | ASR (%), no_memory -, gemma-4-31b-it, n |
| `\PfourNoMemoryGemmaFourThreeOneBAsrP` | n/a | ASR (%), no_memory -, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGemmaFourThreeOneBAsrDropped` | 8.3 | ASR (%) unparsed dropped, no_memory -, gemma-4-31b-it |
| `\PfourNoMemoryGemmaFourThreeOneBAsrDroppedLo` | 5.1 | ASR (%) unparsed dropped, no_memory -, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoMemoryGemmaFourThreeOneBAsrDroppedHi` | 11.8 | ASR (%) unparsed dropped, no_memory -, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoMemoryGemmaFourThreeOneBAsrDroppedCI` | [5.1, 11.8] | ASR (%) unparsed dropped, no_memory -, gemma-4-31b-it, 95% CI |
| `\PfourNoMemoryGemmaFourThreeOneBAsrDroppedN` | 230 | ASR (%) unparsed dropped, no_memory -, gemma-4-31b-it, n |
| `\PfourNoMemoryGemmaFourThreeOneBAsrDroppedP` | n/a | ASR (%) unparsed dropped, no_memory -, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGemmaFourThreeOneBAsrCleanOk` | 8.6 | ASR / clean correct (%), no_memory -, gemma-4-31b-it |
| `\PfourNoMemoryGemmaFourThreeOneBAsrCleanOkLo` | 5.4 | ASR / clean correct (%), no_memory -, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoMemoryGemmaFourThreeOneBAsrCleanOkHi` | 12.1 | ASR / clean correct (%), no_memory -, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoMemoryGemmaFourThreeOneBAsrCleanOkCI` | [5.4, 12.1] | ASR / clean correct (%), no_memory -, gemma-4-31b-it, 95% CI |
| `\PfourNoMemoryGemmaFourThreeOneBAsrCleanOkN` | 222 | ASR / clean correct (%), no_memory -, gemma-4-31b-it, n |
| `\PfourNoMemoryGemmaFourThreeOneBAsrCleanOkP` | n/a | ASR / clean correct (%), no_memory -, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGemmaFourThreeOneBNonTargetAcc` | 97.9 | non-target accuracy (%), no_memory -, gemma-4-31b-it |
| `\PfourNoMemoryGemmaFourThreeOneBNonTargetAccLo` | 95.7 | non-target accuracy (%), no_memory -, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoMemoryGemmaFourThreeOneBNonTargetAccHi` | 99.6 | non-target accuracy (%), no_memory -, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoMemoryGemmaFourThreeOneBNonTargetAccCI` | [95.7, 99.6] | non-target accuracy (%), no_memory -, gemma-4-31b-it, 95% CI |
| `\PfourNoMemoryGemmaFourThreeOneBNonTargetAccN` | 920 | non-target accuracy (%), no_memory -, gemma-4-31b-it, n |
| `\PfourNoMemoryGemmaFourThreeOneBNonTargetAccP` | n/a | non-target accuracy (%), no_memory -, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGLMFiveThreeFlashAsr` | 9.8 | ASR (%), no_memory -, glm-5.3-flash |
| `\PfourNoMemoryGLMFiveThreeFlashAsrLo` | 6.0 | ASR (%), no_memory -, glm-5.3-flash, lower 95% CI bound |
| `\PfourNoMemoryGLMFiveThreeFlashAsrHi` | 13.6 | ASR (%), no_memory -, glm-5.3-flash, upper 95% CI bound |
| `\PfourNoMemoryGLMFiveThreeFlashAsrCI` | [6.0, 13.6] | ASR (%), no_memory -, glm-5.3-flash, 95% CI |
| `\PfourNoMemoryGLMFiveThreeFlashAsrN` | 235 | ASR (%), no_memory -, glm-5.3-flash, n |
| `\PfourNoMemoryGLMFiveThreeFlashAsrP` | n/a | ASR (%), no_memory -, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGLMFiveThreeFlashAsrDropped` | 9.8 | ASR (%) unparsed dropped, no_memory -, glm-5.3-flash |
| `\PfourNoMemoryGLMFiveThreeFlashAsrDroppedLo` | 6.4 | ASR (%) unparsed dropped, no_memory -, glm-5.3-flash, lower 95% CI bound |
| `\PfourNoMemoryGLMFiveThreeFlashAsrDroppedHi` | 14.0 | ASR (%) unparsed dropped, no_memory -, glm-5.3-flash, upper 95% CI bound |
| `\PfourNoMemoryGLMFiveThreeFlashAsrDroppedCI` | [6.4, 14.0] | ASR (%) unparsed dropped, no_memory -, glm-5.3-flash, 95% CI |
| `\PfourNoMemoryGLMFiveThreeFlashAsrDroppedN` | 234 | ASR (%) unparsed dropped, no_memory -, glm-5.3-flash, n |
| `\PfourNoMemoryGLMFiveThreeFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, no_memory -, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGLMFiveThreeFlashAsrCleanOk` | 9.8 | ASR / clean correct (%), no_memory -, glm-5.3-flash |
| `\PfourNoMemoryGLMFiveThreeFlashAsrCleanOkLo` | 6.0 | ASR / clean correct (%), no_memory -, glm-5.3-flash, lower 95% CI bound |
| `\PfourNoMemoryGLMFiveThreeFlashAsrCleanOkHi` | 14.1 | ASR / clean correct (%), no_memory -, glm-5.3-flash, upper 95% CI bound |
| `\PfourNoMemoryGLMFiveThreeFlashAsrCleanOkCI` | [6.0, 14.1] | ASR / clean correct (%), no_memory -, glm-5.3-flash, 95% CI |
| `\PfourNoMemoryGLMFiveThreeFlashAsrCleanOkN` | 234 | ASR / clean correct (%), no_memory -, glm-5.3-flash, n |
| `\PfourNoMemoryGLMFiveThreeFlashAsrCleanOkP` | n/a | ASR / clean correct (%), no_memory -, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGLMFiveThreeFlashNonTargetAcc` | 99.6 | non-target accuracy (%), no_memory -, glm-5.3-flash |
| `\PfourNoMemoryGLMFiveThreeFlashNonTargetAccLo` | 98.7 | non-target accuracy (%), no_memory -, glm-5.3-flash, lower 95% CI bound |
| `\PfourNoMemoryGLMFiveThreeFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), no_memory -, glm-5.3-flash, upper 95% CI bound |
| `\PfourNoMemoryGLMFiveThreeFlashNonTargetAccCI` | [98.7, 100.0] | non-target accuracy (%), no_memory -, glm-5.3-flash, 95% CI |
| `\PfourNoMemoryGLMFiveThreeFlashNonTargetAccN` | 936 | non-target accuracy (%), no_memory -, glm-5.3-flash, n |
| `\PfourNoMemoryGLMFiveThreeFlashNonTargetAccP` | n/a | non-target accuracy (%), no_memory -, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGLMFiveTwoAsr` | 12.3 | ASR (%), no_memory -, glm-5.2 |
| `\PfourNoMemoryGLMFiveTwoAsrLo` | 8.5 | ASR (%), no_memory -, glm-5.2, lower 95% CI bound |
| `\PfourNoMemoryGLMFiveTwoAsrHi` | 16.6 | ASR (%), no_memory -, glm-5.2, upper 95% CI bound |
| `\PfourNoMemoryGLMFiveTwoAsrCI` | [8.5, 16.6] | ASR (%), no_memory -, glm-5.2, 95% CI |
| `\PfourNoMemoryGLMFiveTwoAsrN` | 235 | ASR (%), no_memory -, glm-5.2, n |
| `\PfourNoMemoryGLMFiveTwoAsrP` | n/a | ASR (%), no_memory -, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGLMFiveTwoAsrDropped` | 12.3 | ASR (%) unparsed dropped, no_memory -, glm-5.2 |
| `\PfourNoMemoryGLMFiveTwoAsrDroppedLo` | 8.5 | ASR (%) unparsed dropped, no_memory -, glm-5.2, lower 95% CI bound |
| `\PfourNoMemoryGLMFiveTwoAsrDroppedHi` | 16.2 | ASR (%) unparsed dropped, no_memory -, glm-5.2, upper 95% CI bound |
| `\PfourNoMemoryGLMFiveTwoAsrDroppedCI` | [8.5, 16.2] | ASR (%) unparsed dropped, no_memory -, glm-5.2, 95% CI |
| `\PfourNoMemoryGLMFiveTwoAsrDroppedN` | 235 | ASR (%) unparsed dropped, no_memory -, glm-5.2, n |
| `\PfourNoMemoryGLMFiveTwoAsrDroppedP` | n/a | ASR (%) unparsed dropped, no_memory -, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGLMFiveTwoAsrCleanOk` | 12.6 | ASR / clean correct (%), no_memory -, glm-5.2 |
| `\PfourNoMemoryGLMFiveTwoAsrCleanOkLo` | 8.8 | ASR / clean correct (%), no_memory -, glm-5.2, lower 95% CI bound |
| `\PfourNoMemoryGLMFiveTwoAsrCleanOkHi` | 16.5 | ASR / clean correct (%), no_memory -, glm-5.2, upper 95% CI bound |
| `\PfourNoMemoryGLMFiveTwoAsrCleanOkCI` | [8.8, 16.5] | ASR / clean correct (%), no_memory -, glm-5.2, 95% CI |
| `\PfourNoMemoryGLMFiveTwoAsrCleanOkN` | 231 | ASR / clean correct (%), no_memory -, glm-5.2, n |
| `\PfourNoMemoryGLMFiveTwoAsrCleanOkP` | n/a | ASR / clean correct (%), no_memory -, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoMemoryGLMFiveTwoNonTargetAcc` | 98.4 | non-target accuracy (%), no_memory -, glm-5.2 |
| `\PfourNoMemoryGLMFiveTwoNonTargetAccLo` | 96.9 | non-target accuracy (%), no_memory -, glm-5.2, lower 95% CI bound |
| `\PfourNoMemoryGLMFiveTwoNonTargetAccHi` | 99.7 | non-target accuracy (%), no_memory -, glm-5.2, upper 95% CI bound |
| `\PfourNoMemoryGLMFiveTwoNonTargetAccCI` | [96.9, 99.7] | non-target accuracy (%), no_memory -, glm-5.2, 95% CI |
| `\PfourNoMemoryGLMFiveTwoNonTargetAccN` | 940 | non-target accuracy (%), no_memory -, glm-5.2, n |
| `\PfourNoMemoryGLMFiveTwoNonTargetAccP` | n/a | non-target accuracy (%), no_memory -, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroPooledAsr` | 1.6 | ASR (%), G1 T0, pooled |
| `\PfourGOneTZeroPooledAsrLo` | 0.8 | ASR (%), G1 T0, pooled, lower 95% CI bound |
| `\PfourGOneTZeroPooledAsrHi` | 2.4 | ASR (%), G1 T0, pooled, upper 95% CI bound |
| `\PfourGOneTZeroPooledAsrCI` | [0.8, 2.4] | ASR (%), G1 T0, pooled, 95% CI |
| `\PfourGOneTZeroPooledAsrN` | 1{,}154 | ASR (%), G1 T0, pooled, n |
| `\PfourGOneTZeroPooledAsrP` | n/a | ASR (%), G1 T0, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroPooledAsrDropped` | 1.6 | ASR (%) unparsed dropped, G1 T0, pooled |
| `\PfourGOneTZeroPooledAsrDroppedLo` | 0.8 | ASR (%) unparsed dropped, G1 T0, pooled, lower 95% CI bound |
| `\PfourGOneTZeroPooledAsrDroppedHi` | 2.4 | ASR (%) unparsed dropped, G1 T0, pooled, upper 95% CI bound |
| `\PfourGOneTZeroPooledAsrDroppedCI` | [0.8, 2.4] | ASR (%) unparsed dropped, G1 T0, pooled, 95% CI |
| `\PfourGOneTZeroPooledAsrDroppedN` | 1{,}153 | ASR (%) unparsed dropped, G1 T0, pooled, n |
| `\PfourGOneTZeroPooledAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1 T0, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroPooledAsrCleanOk` | 1.2 | ASR / clean correct (%), G1 T0, pooled |
| `\PfourGOneTZeroPooledAsrCleanOkLo` | 0.5 | ASR / clean correct (%), G1 T0, pooled, lower 95% CI bound |
| `\PfourGOneTZeroPooledAsrCleanOkHi` | 2.1 | ASR / clean correct (%), G1 T0, pooled, upper 95% CI bound |
| `\PfourGOneTZeroPooledAsrCleanOkCI` | [0.5, 2.1] | ASR / clean correct (%), G1 T0, pooled, 95% CI |
| `\PfourGOneTZeroPooledAsrCleanOkN` | 1{,}127 | ASR / clean correct (%), G1 T0, pooled, n |
| `\PfourGOneTZeroPooledAsrCleanOkP` | n/a | ASR / clean correct (%), G1 T0, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroPooledNonTargetAcc` | 97.9 | non-target accuracy (%), G1 T0, pooled |
| `\PfourGOneTZeroPooledNonTargetAccLo` | 96.9 | non-target accuracy (%), G1 T0, pooled, lower 95% CI bound |
| `\PfourGOneTZeroPooledNonTargetAccHi` | 98.9 | non-target accuracy (%), G1 T0, pooled, upper 95% CI bound |
| `\PfourGOneTZeroPooledNonTargetAccCI` | [96.9, 98.9] | non-target accuracy (%), G1 T0, pooled, 95% CI |
| `\PfourGOneTZeroPooledNonTargetAccN` | 4{,}612 | non-target accuracy (%), G1 T0, pooled, n |
| `\PfourGOneTZeroPooledNonTargetAccP` | n/a | non-target accuracy (%), G1 T0, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroDeepSeekVFourFlashAsr` | 3.8 | ASR (%), G1 T0, deepseek-v4-flash |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrLo` | 1.3 | ASR (%), G1 T0, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrHi` | 6.4 | ASR (%), G1 T0, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrCI` | [1.3, 6.4] | ASR (%), G1 T0, deepseek-v4-flash, 95% CI |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrN` | 235 | ASR (%), G1 T0, deepseek-v4-flash, n |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrP` | n/a | ASR (%), G1 T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrDropped` | 3.8 | ASR (%) unparsed dropped, G1 T0, deepseek-v4-flash |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrDroppedLo` | 1.7 | ASR (%) unparsed dropped, G1 T0, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrDroppedHi` | 6.4 | ASR (%) unparsed dropped, G1 T0, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrDroppedCI` | [1.7, 6.4] | ASR (%) unparsed dropped, G1 T0, deepseek-v4-flash, 95% CI |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrDroppedN` | 235 | ASR (%) unparsed dropped, G1 T0, deepseek-v4-flash, n |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1 T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrCleanOk` | 3.8 | ASR / clean correct (%), G1 T0, deepseek-v4-flash |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrCleanOkLo` | 1.7 | ASR / clean correct (%), G1 T0, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrCleanOkHi` | 6.8 | ASR / clean correct (%), G1 T0, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrCleanOkCI` | [1.7, 6.8] | ASR / clean correct (%), G1 T0, deepseek-v4-flash, 95% CI |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrCleanOkN` | 234 | ASR / clean correct (%), G1 T0, deepseek-v4-flash, n |
| `\PfourGOneTZeroDeepSeekVFourFlashAsrCleanOkP` | n/a | ASR / clean correct (%), G1 T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroDeepSeekVFourFlashNonTargetAcc` | 99.6 | non-target accuracy (%), G1 T0, deepseek-v4-flash |
| `\PfourGOneTZeroDeepSeekVFourFlashNonTargetAccLo` | 98.8 | non-target accuracy (%), G1 T0, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGOneTZeroDeepSeekVFourFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), G1 T0, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGOneTZeroDeepSeekVFourFlashNonTargetAccCI` | [98.8, 100.0] | non-target accuracy (%), G1 T0, deepseek-v4-flash, 95% CI |
| `\PfourGOneTZeroDeepSeekVFourFlashNonTargetAccN` | 940 | non-target accuracy (%), G1 T0, deepseek-v4-flash, n |
| `\PfourGOneTZeroDeepSeekVFourFlashNonTargetAccP` | n/a | non-target accuracy (%), G1 T0, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsr` | 2.1 | ASR (%), G1 T0, qwen3.8-27b |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrLo` | 0.4 | ASR (%), G1 T0, qwen3.8-27b, lower 95% CI bound |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrHi` | 4.3 | ASR (%), G1 T0, qwen3.8-27b, upper 95% CI bound |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrCI` | [0.4, 4.3] | ASR (%), G1 T0, qwen3.8-27b, 95% CI |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrN` | 235 | ASR (%), G1 T0, qwen3.8-27b, n |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrP` | n/a | ASR (%), G1 T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrDropped` | 2.1 | ASR (%) unparsed dropped, G1 T0, qwen3.8-27b |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrDroppedLo` | 0.4 | ASR (%) unparsed dropped, G1 T0, qwen3.8-27b, lower 95% CI bound |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrDroppedHi` | 3.8 | ASR (%) unparsed dropped, G1 T0, qwen3.8-27b, upper 95% CI bound |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrDroppedCI` | [0.4, 3.8] | ASR (%) unparsed dropped, G1 T0, qwen3.8-27b, 95% CI |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrDroppedN` | 235 | ASR (%) unparsed dropped, G1 T0, qwen3.8-27b, n |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1 T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrCleanOk` | 0.9 | ASR / clean correct (%), G1 T0, qwen3.8-27b |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrCleanOkLo` | 0.0 | ASR / clean correct (%), G1 T0, qwen3.8-27b, lower 95% CI bound |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrCleanOkHi` | 2.3 | ASR / clean correct (%), G1 T0, qwen3.8-27b, upper 95% CI bound |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrCleanOkCI` | [0.0, 2.3] | ASR / clean correct (%), G1 T0, qwen3.8-27b, 95% CI |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrCleanOkN` | 217 | ASR / clean correct (%), G1 T0, qwen3.8-27b, n |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBAsrCleanOkP` | n/a | ASR / clean correct (%), G1 T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBNonTargetAcc` | 93.9 | non-target accuracy (%), G1 T0, qwen3.8-27b |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBNonTargetAccLo` | 91.2 | non-target accuracy (%), G1 T0, qwen3.8-27b, lower 95% CI bound |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBNonTargetAccHi` | 96.3 | non-target accuracy (%), G1 T0, qwen3.8-27b, upper 95% CI bound |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBNonTargetAccCI` | [91.2, 96.3] | non-target accuracy (%), G1 T0, qwen3.8-27b, 95% CI |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBNonTargetAccN` | 940 | non-target accuracy (%), G1 T0, qwen3.8-27b, n |
| `\PfourGOneTZeroQwenThreeEightTwoSevenBNonTargetAccP` | n/a | non-target accuracy (%), G1 T0, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGemmaFourThreeOneBAsr` | 1.4 | ASR (%), G1 T0, gemma-4-31b-it |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrLo` | 0.0 | ASR (%), G1 T0, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrHi` | 3.3 | ASR (%), G1 T0, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrCI` | [0.0, 3.3] | ASR (%), G1 T0, gemma-4-31b-it, 95% CI |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrN` | 214 | ASR (%), G1 T0, gemma-4-31b-it, n |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrP` | n/a | ASR (%), G1 T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrDropped` | 1.4 | ASR (%) unparsed dropped, G1 T0, gemma-4-31b-it |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrDroppedLo` | 0.0 | ASR (%) unparsed dropped, G1 T0, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrDroppedHi` | 3.3 | ASR (%) unparsed dropped, G1 T0, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrDroppedCI` | [0.0, 3.3] | ASR (%) unparsed dropped, G1 T0, gemma-4-31b-it, 95% CI |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrDroppedN` | 213 | ASR (%) unparsed dropped, G1 T0, gemma-4-31b-it, n |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1 T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrCleanOk` | 1.0 | ASR / clean correct (%), G1 T0, gemma-4-31b-it |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrCleanOkLo` | 0.0 | ASR / clean correct (%), G1 T0, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrCleanOkHi` | 2.4 | ASR / clean correct (%), G1 T0, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrCleanOkCI` | [0.0, 2.4] | ASR / clean correct (%), G1 T0, gemma-4-31b-it, 95% CI |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrCleanOkN` | 210 | ASR / clean correct (%), G1 T0, gemma-4-31b-it, n |
| `\PfourGOneTZeroGemmaFourThreeOneBAsrCleanOkP` | n/a | ASR / clean correct (%), G1 T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGemmaFourThreeOneBNonTargetAcc` | 98.6 | non-target accuracy (%), G1 T0, gemma-4-31b-it |
| `\PfourGOneTZeroGemmaFourThreeOneBNonTargetAccLo` | 96.2 | non-target accuracy (%), G1 T0, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGOneTZeroGemmaFourThreeOneBNonTargetAccHi` | 100.0 | non-target accuracy (%), G1 T0, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGOneTZeroGemmaFourThreeOneBNonTargetAccCI` | [96.2, 100.0] | non-target accuracy (%), G1 T0, gemma-4-31b-it, 95% CI |
| `\PfourGOneTZeroGemmaFourThreeOneBNonTargetAccN` | 852 | non-target accuracy (%), G1 T0, gemma-4-31b-it, n |
| `\PfourGOneTZeroGemmaFourThreeOneBNonTargetAccP` | n/a | non-target accuracy (%), G1 T0, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGLMFiveThreeFlashAsr` | 0.0 | ASR (%), G1 T0, glm-5.3-flash |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrLo` | 0.0 | ASR (%), G1 T0, glm-5.3-flash, lower 95% CI bound |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrHi` | 1.6 | ASR (%), G1 T0, glm-5.3-flash, upper 95% CI bound |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrCI` | [0.0, 1.6] | ASR (%), G1 T0, glm-5.3-flash, 95% CI |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrN` | 235 | ASR (%), G1 T0, glm-5.3-flash, n |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrP` | n/a | ASR (%), G1 T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrDropped` | 0.0 | ASR (%) unparsed dropped, G1 T0, glm-5.3-flash |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrDroppedLo` | 0.0 | ASR (%) unparsed dropped, G1 T0, glm-5.3-flash, lower 95% CI bound |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrDroppedHi` | 1.6 | ASR (%) unparsed dropped, G1 T0, glm-5.3-flash, upper 95% CI bound |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrDroppedCI` | [0.0, 1.6] | ASR (%) unparsed dropped, G1 T0, glm-5.3-flash, 95% CI |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrDroppedN` | 235 | ASR (%) unparsed dropped, G1 T0, glm-5.3-flash, n |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1 T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrCleanOk` | 0.0 | ASR / clean correct (%), G1 T0, glm-5.3-flash |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrCleanOkLo` | 0.0 | ASR / clean correct (%), G1 T0, glm-5.3-flash, lower 95% CI bound |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrCleanOkHi` | 1.6 | ASR / clean correct (%), G1 T0, glm-5.3-flash, upper 95% CI bound |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrCleanOkCI` | [0.0, 1.6] | ASR / clean correct (%), G1 T0, glm-5.3-flash, 95% CI |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrCleanOkN` | 235 | ASR / clean correct (%), G1 T0, glm-5.3-flash, n |
| `\PfourGOneTZeroGLMFiveThreeFlashAsrCleanOkP` | n/a | ASR / clean correct (%), G1 T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGLMFiveThreeFlashNonTargetAcc` | 99.8 | non-target accuracy (%), G1 T0, glm-5.3-flash |
| `\PfourGOneTZeroGLMFiveThreeFlashNonTargetAccLo` | 99.4 | non-target accuracy (%), G1 T0, glm-5.3-flash, lower 95% CI bound |
| `\PfourGOneTZeroGLMFiveThreeFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), G1 T0, glm-5.3-flash, upper 95% CI bound |
| `\PfourGOneTZeroGLMFiveThreeFlashNonTargetAccCI` | [99.4, 100.0] | non-target accuracy (%), G1 T0, glm-5.3-flash, 95% CI |
| `\PfourGOneTZeroGLMFiveThreeFlashNonTargetAccN` | 940 | non-target accuracy (%), G1 T0, glm-5.3-flash, n |
| `\PfourGOneTZeroGLMFiveThreeFlashNonTargetAccP` | n/a | non-target accuracy (%), G1 T0, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGLMFiveTwoAsr` | 0.4 | ASR (%), G1 T0, glm-5.2 |
| `\PfourGOneTZeroGLMFiveTwoAsrLo` | 0.0 | ASR (%), G1 T0, glm-5.2, lower 95% CI bound |
| `\PfourGOneTZeroGLMFiveTwoAsrHi` | 1.3 | ASR (%), G1 T0, glm-5.2, upper 95% CI bound |
| `\PfourGOneTZeroGLMFiveTwoAsrCI` | [0.0, 1.3] | ASR (%), G1 T0, glm-5.2, 95% CI |
| `\PfourGOneTZeroGLMFiveTwoAsrN` | 235 | ASR (%), G1 T0, glm-5.2, n |
| `\PfourGOneTZeroGLMFiveTwoAsrP` | n/a | ASR (%), G1 T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGLMFiveTwoAsrDropped` | 0.4 | ASR (%) unparsed dropped, G1 T0, glm-5.2 |
| `\PfourGOneTZeroGLMFiveTwoAsrDroppedLo` | 0.0 | ASR (%) unparsed dropped, G1 T0, glm-5.2, lower 95% CI bound |
| `\PfourGOneTZeroGLMFiveTwoAsrDroppedHi` | 1.3 | ASR (%) unparsed dropped, G1 T0, glm-5.2, upper 95% CI bound |
| `\PfourGOneTZeroGLMFiveTwoAsrDroppedCI` | [0.0, 1.3] | ASR (%) unparsed dropped, G1 T0, glm-5.2, 95% CI |
| `\PfourGOneTZeroGLMFiveTwoAsrDroppedN` | 235 | ASR (%) unparsed dropped, G1 T0, glm-5.2, n |
| `\PfourGOneTZeroGLMFiveTwoAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1 T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGLMFiveTwoAsrCleanOk` | 0.4 | ASR / clean correct (%), G1 T0, glm-5.2 |
| `\PfourGOneTZeroGLMFiveTwoAsrCleanOkLo` | 0.0 | ASR / clean correct (%), G1 T0, glm-5.2, lower 95% CI bound |
| `\PfourGOneTZeroGLMFiveTwoAsrCleanOkHi` | 1.3 | ASR / clean correct (%), G1 T0, glm-5.2, upper 95% CI bound |
| `\PfourGOneTZeroGLMFiveTwoAsrCleanOkCI` | [0.0, 1.3] | ASR / clean correct (%), G1 T0, glm-5.2, 95% CI |
| `\PfourGOneTZeroGLMFiveTwoAsrCleanOkN` | 231 | ASR / clean correct (%), G1 T0, glm-5.2, n |
| `\PfourGOneTZeroGLMFiveTwoAsrCleanOkP` | n/a | ASR / clean correct (%), G1 T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTZeroGLMFiveTwoNonTargetAcc` | 97.9 | non-target accuracy (%), G1 T0, glm-5.2 |
| `\PfourGOneTZeroGLMFiveTwoNonTargetAccLo` | 95.7 | non-target accuracy (%), G1 T0, glm-5.2, lower 95% CI bound |
| `\PfourGOneTZeroGLMFiveTwoNonTargetAccHi` | 99.6 | non-target accuracy (%), G1 T0, glm-5.2, upper 95% CI bound |
| `\PfourGOneTZeroGLMFiveTwoNonTargetAccCI` | [95.7, 99.6] | non-target accuracy (%), G1 T0, glm-5.2, 95% CI |
| `\PfourGOneTZeroGLMFiveTwoNonTargetAccN` | 940 | non-target accuracy (%), G1 T0, glm-5.2, n |
| `\PfourGOneTZeroGLMFiveTwoNonTargetAccP` | n/a | non-target accuracy (%), G1 T0, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoPooledAsr` | 1.1 | ASR (%), G1 T2, pooled |
| `\PfourGOneTTwoPooledAsrLo` | 0.5 | ASR (%), G1 T2, pooled, lower 95% CI bound |
| `\PfourGOneTTwoPooledAsrHi` | 1.8 | ASR (%), G1 T2, pooled, upper 95% CI bound |
| `\PfourGOneTTwoPooledAsrCI` | [0.5, 1.8] | ASR (%), G1 T2, pooled, 95% CI |
| `\PfourGOneTTwoPooledAsrN` | 1{,}137 | ASR (%), G1 T2, pooled, n |
| `\PfourGOneTTwoPooledAsrP` | n/a | ASR (%), G1 T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoPooledAsrDropped` | 1.1 | ASR (%) unparsed dropped, G1 T2, pooled |
| `\PfourGOneTTwoPooledAsrDroppedLo` | 0.5 | ASR (%) unparsed dropped, G1 T2, pooled, lower 95% CI bound |
| `\PfourGOneTTwoPooledAsrDroppedHi` | 1.8 | ASR (%) unparsed dropped, G1 T2, pooled, upper 95% CI bound |
| `\PfourGOneTTwoPooledAsrDroppedCI` | [0.5, 1.8] | ASR (%) unparsed dropped, G1 T2, pooled, 95% CI |
| `\PfourGOneTTwoPooledAsrDroppedN` | 1{,}137 | ASR (%) unparsed dropped, G1 T2, pooled, n |
| `\PfourGOneTTwoPooledAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1 T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoPooledAsrCleanOk` | 0.8 | ASR / clean correct (%), G1 T2, pooled |
| `\PfourGOneTTwoPooledAsrCleanOkLo` | 0.2 | ASR / clean correct (%), G1 T2, pooled, lower 95% CI bound |
| `\PfourGOneTTwoPooledAsrCleanOkHi` | 1.5 | ASR / clean correct (%), G1 T2, pooled, upper 95% CI bound |
| `\PfourGOneTTwoPooledAsrCleanOkCI` | [0.2, 1.5] | ASR / clean correct (%), G1 T2, pooled, 95% CI |
| `\PfourGOneTTwoPooledAsrCleanOkN` | 1{,}111 | ASR / clean correct (%), G1 T2, pooled, n |
| `\PfourGOneTTwoPooledAsrCleanOkP` | n/a | ASR / clean correct (%), G1 T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoPooledNonTargetAcc` | 97.9 | non-target accuracy (%), G1 T2, pooled |
| `\PfourGOneTTwoPooledNonTargetAccLo` | 96.7 | non-target accuracy (%), G1 T2, pooled, lower 95% CI bound |
| `\PfourGOneTTwoPooledNonTargetAccHi` | 98.9 | non-target accuracy (%), G1 T2, pooled, upper 95% CI bound |
| `\PfourGOneTTwoPooledNonTargetAccCI` | [96.7, 98.9] | non-target accuracy (%), G1 T2, pooled, 95% CI |
| `\PfourGOneTTwoPooledNonTargetAccN` | 4{,}548 | non-target accuracy (%), G1 T2, pooled, n |
| `\PfourGOneTTwoPooledNonTargetAccP` | n/a | non-target accuracy (%), G1 T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoDeepSeekVFourFlashAsr` | 2.1 | ASR (%), G1 T2, deepseek-v4-flash |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrLo` | 0.4 | ASR (%), G1 T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrHi` | 3.9 | ASR (%), G1 T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrCI` | [0.4, 3.9] | ASR (%), G1 T2, deepseek-v4-flash, 95% CI |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrN` | 234 | ASR (%), G1 T2, deepseek-v4-flash, n |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrP` | n/a | ASR (%), G1 T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrDropped` | 2.1 | ASR (%) unparsed dropped, G1 T2, deepseek-v4-flash |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrDroppedLo` | 0.4 | ASR (%) unparsed dropped, G1 T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrDroppedHi` | 3.9 | ASR (%) unparsed dropped, G1 T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrDroppedCI` | [0.4, 3.9] | ASR (%) unparsed dropped, G1 T2, deepseek-v4-flash, 95% CI |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrDroppedN` | 234 | ASR (%) unparsed dropped, G1 T2, deepseek-v4-flash, n |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1 T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrCleanOk` | 2.1 | ASR / clean correct (%), G1 T2, deepseek-v4-flash |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrCleanOkLo` | 0.4 | ASR / clean correct (%), G1 T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrCleanOkHi` | 3.9 | ASR / clean correct (%), G1 T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrCleanOkCI` | [0.4, 3.9] | ASR / clean correct (%), G1 T2, deepseek-v4-flash, 95% CI |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrCleanOkN` | 233 | ASR / clean correct (%), G1 T2, deepseek-v4-flash, n |
| `\PfourGOneTTwoDeepSeekVFourFlashAsrCleanOkP` | n/a | ASR / clean correct (%), G1 T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoDeepSeekVFourFlashNonTargetAcc` | 99.6 | non-target accuracy (%), G1 T2, deepseek-v4-flash |
| `\PfourGOneTTwoDeepSeekVFourFlashNonTargetAccLo` | 98.8 | non-target accuracy (%), G1 T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGOneTTwoDeepSeekVFourFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), G1 T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGOneTTwoDeepSeekVFourFlashNonTargetAccCI` | [98.8, 100.0] | non-target accuracy (%), G1 T2, deepseek-v4-flash, 95% CI |
| `\PfourGOneTTwoDeepSeekVFourFlashNonTargetAccN` | 936 | non-target accuracy (%), G1 T2, deepseek-v4-flash, n |
| `\PfourGOneTTwoDeepSeekVFourFlashNonTargetAccP` | n/a | non-target accuracy (%), G1 T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsr` | 1.7 | ASR (%), G1 T2, qwen3.8-27b |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrLo` | 0.4 | ASR (%), G1 T2, qwen3.8-27b, lower 95% CI bound |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrHi` | 3.5 | ASR (%), G1 T2, qwen3.8-27b, upper 95% CI bound |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrCI` | [0.4, 3.5] | ASR (%), G1 T2, qwen3.8-27b, 95% CI |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrN` | 230 | ASR (%), G1 T2, qwen3.8-27b, n |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrP` | n/a | ASR (%), G1 T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrDropped` | 1.7 | ASR (%) unparsed dropped, G1 T2, qwen3.8-27b |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrDroppedLo` | 0.4 | ASR (%) unparsed dropped, G1 T2, qwen3.8-27b, lower 95% CI bound |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrDroppedHi` | 3.5 | ASR (%) unparsed dropped, G1 T2, qwen3.8-27b, upper 95% CI bound |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrDroppedCI` | [0.4, 3.5] | ASR (%) unparsed dropped, G1 T2, qwen3.8-27b, 95% CI |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrDroppedN` | 230 | ASR (%) unparsed dropped, G1 T2, qwen3.8-27b, n |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1 T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrCleanOk` | 0.5 | ASR / clean correct (%), G1 T2, qwen3.8-27b |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrCleanOkLo` | 0.0 | ASR / clean correct (%), G1 T2, qwen3.8-27b, lower 95% CI bound |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrCleanOkHi` | 1.5 | ASR / clean correct (%), G1 T2, qwen3.8-27b, upper 95% CI bound |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrCleanOkCI` | [0.0, 1.5] | ASR / clean correct (%), G1 T2, qwen3.8-27b, 95% CI |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrCleanOkN` | 212 | ASR / clean correct (%), G1 T2, qwen3.8-27b, n |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBAsrCleanOkP` | n/a | ASR / clean correct (%), G1 T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBNonTargetAcc` | 93.8 | non-target accuracy (%), G1 T2, qwen3.8-27b |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBNonTargetAccLo` | 91.0 | non-target accuracy (%), G1 T2, qwen3.8-27b, lower 95% CI bound |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBNonTargetAccHi` | 96.4 | non-target accuracy (%), G1 T2, qwen3.8-27b, upper 95% CI bound |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBNonTargetAccCI` | [91.0, 96.4] | non-target accuracy (%), G1 T2, qwen3.8-27b, 95% CI |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBNonTargetAccN` | 920 | non-target accuracy (%), G1 T2, qwen3.8-27b, n |
| `\PfourGOneTTwoQwenThreeEightTwoSevenBNonTargetAccP` | n/a | non-target accuracy (%), G1 T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGemmaFourThreeOneBAsr` | 1.0 | ASR (%), G1 T2, gemma-4-31b-it |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrLo` | 0.0 | ASR (%), G1 T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrHi` | 2.4 | ASR (%), G1 T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrCI` | [0.0, 2.4] | ASR (%), G1 T2, gemma-4-31b-it, 95% CI |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrN` | 205 | ASR (%), G1 T2, gemma-4-31b-it, n |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrP` | n/a | ASR (%), G1 T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrDropped` | 1.0 | ASR (%) unparsed dropped, G1 T2, gemma-4-31b-it |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrDroppedLo` | 0.0 | ASR (%) unparsed dropped, G1 T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrDroppedHi` | 2.5 | ASR (%) unparsed dropped, G1 T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrDroppedCI` | [0.0, 2.5] | ASR (%) unparsed dropped, G1 T2, gemma-4-31b-it, 95% CI |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrDroppedN` | 205 | ASR (%) unparsed dropped, G1 T2, gemma-4-31b-it, n |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1 T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrCleanOk` | 0.5 | ASR / clean correct (%), G1 T2, gemma-4-31b-it |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrCleanOkLo` | 0.0 | ASR / clean correct (%), G1 T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrCleanOkHi` | 1.5 | ASR / clean correct (%), G1 T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrCleanOkCI` | [0.0, 1.5] | ASR / clean correct (%), G1 T2, gemma-4-31b-it, 95% CI |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrCleanOkN` | 202 | ASR / clean correct (%), G1 T2, gemma-4-31b-it, n |
| `\PfourGOneTTwoGemmaFourThreeOneBAsrCleanOkP` | n/a | ASR / clean correct (%), G1 T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGemmaFourThreeOneBNonTargetAcc` | 98.5 | non-target accuracy (%), G1 T2, gemma-4-31b-it |
| `\PfourGOneTTwoGemmaFourThreeOneBNonTargetAccLo` | 96.1 | non-target accuracy (%), G1 T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGOneTTwoGemmaFourThreeOneBNonTargetAccHi` | 100.0 | non-target accuracy (%), G1 T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGOneTTwoGemmaFourThreeOneBNonTargetAccCI` | [96.1, 100.0] | non-target accuracy (%), G1 T2, gemma-4-31b-it, 95% CI |
| `\PfourGOneTTwoGemmaFourThreeOneBNonTargetAccN` | 820 | non-target accuracy (%), G1 T2, gemma-4-31b-it, n |
| `\PfourGOneTTwoGemmaFourThreeOneBNonTargetAccP` | n/a | non-target accuracy (%), G1 T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGLMFiveThreeFlashAsr` | 0.0 | ASR (%), G1 T2, glm-5.3-flash |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrLo` | 0.0 | ASR (%), G1 T2, glm-5.3-flash, lower 95% CI bound |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrHi` | 1.6 | ASR (%), G1 T2, glm-5.3-flash, upper 95% CI bound |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrCI` | [0.0, 1.6] | ASR (%), G1 T2, glm-5.3-flash, 95% CI |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrN` | 234 | ASR (%), G1 T2, glm-5.3-flash, n |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrP` | n/a | ASR (%), G1 T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrDropped` | 0.0 | ASR (%) unparsed dropped, G1 T2, glm-5.3-flash |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrDroppedLo` | 0.0 | ASR (%) unparsed dropped, G1 T2, glm-5.3-flash, lower 95% CI bound |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrDroppedHi` | 1.6 | ASR (%) unparsed dropped, G1 T2, glm-5.3-flash, upper 95% CI bound |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrDroppedCI` | [0.0, 1.6] | ASR (%) unparsed dropped, G1 T2, glm-5.3-flash, 95% CI |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrDroppedN` | 234 | ASR (%) unparsed dropped, G1 T2, glm-5.3-flash, n |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1 T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrCleanOk` | 0.0 | ASR / clean correct (%), G1 T2, glm-5.3-flash |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrCleanOkLo` | 0.0 | ASR / clean correct (%), G1 T2, glm-5.3-flash, lower 95% CI bound |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrCleanOkHi` | 1.6 | ASR / clean correct (%), G1 T2, glm-5.3-flash, upper 95% CI bound |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrCleanOkCI` | [0.0, 1.6] | ASR / clean correct (%), G1 T2, glm-5.3-flash, 95% CI |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrCleanOkN` | 234 | ASR / clean correct (%), G1 T2, glm-5.3-flash, n |
| `\PfourGOneTTwoGLMFiveThreeFlashAsrCleanOkP` | n/a | ASR / clean correct (%), G1 T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGLMFiveThreeFlashNonTargetAcc` | 99.8 | non-target accuracy (%), G1 T2, glm-5.3-flash |
| `\PfourGOneTTwoGLMFiveThreeFlashNonTargetAccLo` | 99.4 | non-target accuracy (%), G1 T2, glm-5.3-flash, lower 95% CI bound |
| `\PfourGOneTTwoGLMFiveThreeFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), G1 T2, glm-5.3-flash, upper 95% CI bound |
| `\PfourGOneTTwoGLMFiveThreeFlashNonTargetAccCI` | [99.4, 100.0] | non-target accuracy (%), G1 T2, glm-5.3-flash, 95% CI |
| `\PfourGOneTTwoGLMFiveThreeFlashNonTargetAccN` | 936 | non-target accuracy (%), G1 T2, glm-5.3-flash, n |
| `\PfourGOneTTwoGLMFiveThreeFlashNonTargetAccP` | n/a | non-target accuracy (%), G1 T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGLMFiveTwoAsr` | 0.9 | ASR (%), G1 T2, glm-5.2 |
| `\PfourGOneTTwoGLMFiveTwoAsrLo` | 0.0 | ASR (%), G1 T2, glm-5.2, lower 95% CI bound |
| `\PfourGOneTTwoGLMFiveTwoAsrHi` | 2.1 | ASR (%), G1 T2, glm-5.2, upper 95% CI bound |
| `\PfourGOneTTwoGLMFiveTwoAsrCI` | [0.0, 2.1] | ASR (%), G1 T2, glm-5.2, 95% CI |
| `\PfourGOneTTwoGLMFiveTwoAsrN` | 234 | ASR (%), G1 T2, glm-5.2, n |
| `\PfourGOneTTwoGLMFiveTwoAsrP` | n/a | ASR (%), G1 T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGLMFiveTwoAsrDropped` | 0.9 | ASR (%) unparsed dropped, G1 T2, glm-5.2 |
| `\PfourGOneTTwoGLMFiveTwoAsrDroppedLo` | 0.0 | ASR (%) unparsed dropped, G1 T2, glm-5.2, lower 95% CI bound |
| `\PfourGOneTTwoGLMFiveTwoAsrDroppedHi` | 2.1 | ASR (%) unparsed dropped, G1 T2, glm-5.2, upper 95% CI bound |
| `\PfourGOneTTwoGLMFiveTwoAsrDroppedCI` | [0.0, 2.1] | ASR (%) unparsed dropped, G1 T2, glm-5.2, 95% CI |
| `\PfourGOneTTwoGLMFiveTwoAsrDroppedN` | 234 | ASR (%) unparsed dropped, G1 T2, glm-5.2, n |
| `\PfourGOneTTwoGLMFiveTwoAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1 T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGLMFiveTwoAsrCleanOk` | 0.9 | ASR / clean correct (%), G1 T2, glm-5.2 |
| `\PfourGOneTTwoGLMFiveTwoAsrCleanOkLo` | 0.0 | ASR / clean correct (%), G1 T2, glm-5.2, lower 95% CI bound |
| `\PfourGOneTTwoGLMFiveTwoAsrCleanOkHi` | 2.2 | ASR / clean correct (%), G1 T2, glm-5.2, upper 95% CI bound |
| `\PfourGOneTTwoGLMFiveTwoAsrCleanOkCI` | [0.0, 2.2] | ASR / clean correct (%), G1 T2, glm-5.2, 95% CI |
| `\PfourGOneTTwoGLMFiveTwoAsrCleanOkN` | 230 | ASR / clean correct (%), G1 T2, glm-5.2, n |
| `\PfourGOneTTwoGLMFiveTwoAsrCleanOkP` | n/a | ASR / clean correct (%), G1 T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTTwoGLMFiveTwoNonTargetAcc` | 97.9 | non-target accuracy (%), G1 T2, glm-5.2 |
| `\PfourGOneTTwoGLMFiveTwoNonTargetAccLo` | 95.6 | non-target accuracy (%), G1 T2, glm-5.2, lower 95% CI bound |
| `\PfourGOneTTwoGLMFiveTwoNonTargetAccHi` | 99.6 | non-target accuracy (%), G1 T2, glm-5.2, upper 95% CI bound |
| `\PfourGOneTTwoGLMFiveTwoNonTargetAccCI` | [95.6, 99.6] | non-target accuracy (%), G1 T2, glm-5.2, 95% CI |
| `\PfourGOneTTwoGLMFiveTwoNonTargetAccN` | 936 | non-target accuracy (%), G1 T2, glm-5.2, n |
| `\PfourGOneTTwoGLMFiveTwoNonTargetAccP` | n/a | non-target accuracy (%), G1 T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreePooledAsr` | 1.7 | ASR (%), G1 T3, pooled |
| `\PfourGOneTThreePooledAsrLo` | 0.9 | ASR (%), G1 T3, pooled, lower 95% CI bound |
| `\PfourGOneTThreePooledAsrHi` | 2.4 | ASR (%), G1 T3, pooled, upper 95% CI bound |
| `\PfourGOneTThreePooledAsrCI` | [0.9, 2.4] | ASR (%), G1 T3, pooled, 95% CI |
| `\PfourGOneTThreePooledAsrN` | 1{,}148 | ASR (%), G1 T3, pooled, n |
| `\PfourGOneTThreePooledAsrP` | n/a | ASR (%), G1 T3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreePooledAsrDropped` | 1.7 | ASR (%) unparsed dropped, G1 T3, pooled |
| `\PfourGOneTThreePooledAsrDroppedLo` | 0.9 | ASR (%) unparsed dropped, G1 T3, pooled, lower 95% CI bound |
| `\PfourGOneTThreePooledAsrDroppedHi` | 2.5 | ASR (%) unparsed dropped, G1 T3, pooled, upper 95% CI bound |
| `\PfourGOneTThreePooledAsrDroppedCI` | [0.9, 2.5] | ASR (%) unparsed dropped, G1 T3, pooled, 95% CI |
| `\PfourGOneTThreePooledAsrDroppedN` | 1{,}148 | ASR (%) unparsed dropped, G1 T3, pooled, n |
| `\PfourGOneTThreePooledAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1 T3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreePooledAsrCleanOk` | 1.3 | ASR / clean correct (%), G1 T3, pooled |
| `\PfourGOneTThreePooledAsrCleanOkLo` | 0.6 | ASR / clean correct (%), G1 T3, pooled, lower 95% CI bound |
| `\PfourGOneTThreePooledAsrCleanOkHi` | 2.2 | ASR / clean correct (%), G1 T3, pooled, upper 95% CI bound |
| `\PfourGOneTThreePooledAsrCleanOkCI` | [0.6, 2.2] | ASR / clean correct (%), G1 T3, pooled, 95% CI |
| `\PfourGOneTThreePooledAsrCleanOkN` | 1{,}122 | ASR / clean correct (%), G1 T3, pooled, n |
| `\PfourGOneTThreePooledAsrCleanOkP` | n/a | ASR / clean correct (%), G1 T3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreePooledNonTargetAcc` | 97.9 | non-target accuracy (%), G1 T3, pooled |
| `\PfourGOneTThreePooledNonTargetAccLo` | 96.8 | non-target accuracy (%), G1 T3, pooled, lower 95% CI bound |
| `\PfourGOneTThreePooledNonTargetAccHi` | 98.9 | non-target accuracy (%), G1 T3, pooled, upper 95% CI bound |
| `\PfourGOneTThreePooledNonTargetAccCI` | [96.8, 98.9] | non-target accuracy (%), G1 T3, pooled, 95% CI |
| `\PfourGOneTThreePooledNonTargetAccN` | 4{,}592 | non-target accuracy (%), G1 T3, pooled, n |
| `\PfourGOneTThreePooledNonTargetAccP` | n/a | non-target accuracy (%), G1 T3, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeDeepSeekVFourFlashAsr` | 3.8 | ASR (%), G1 T3, deepseek-v4-flash |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrLo` | 1.7 | ASR (%), G1 T3, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrHi` | 6.0 | ASR (%), G1 T3, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrCI` | [1.7, 6.0] | ASR (%), G1 T3, deepseek-v4-flash, 95% CI |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrN` | 235 | ASR (%), G1 T3, deepseek-v4-flash, n |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrP` | n/a | ASR (%), G1 T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrDropped` | 3.8 | ASR (%) unparsed dropped, G1 T3, deepseek-v4-flash |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrDroppedLo` | 1.7 | ASR (%) unparsed dropped, G1 T3, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrDroppedHi` | 6.4 | ASR (%) unparsed dropped, G1 T3, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrDroppedCI` | [1.7, 6.4] | ASR (%) unparsed dropped, G1 T3, deepseek-v4-flash, 95% CI |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrDroppedN` | 235 | ASR (%) unparsed dropped, G1 T3, deepseek-v4-flash, n |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1 T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrCleanOk` | 3.8 | ASR / clean correct (%), G1 T3, deepseek-v4-flash |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrCleanOkLo` | 1.7 | ASR / clean correct (%), G1 T3, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrCleanOkHi` | 6.4 | ASR / clean correct (%), G1 T3, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrCleanOkCI` | [1.7, 6.4] | ASR / clean correct (%), G1 T3, deepseek-v4-flash, 95% CI |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrCleanOkN` | 234 | ASR / clean correct (%), G1 T3, deepseek-v4-flash, n |
| `\PfourGOneTThreeDeepSeekVFourFlashAsrCleanOkP` | n/a | ASR / clean correct (%), G1 T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeDeepSeekVFourFlashNonTargetAcc` | 99.6 | non-target accuracy (%), G1 T3, deepseek-v4-flash |
| `\PfourGOneTThreeDeepSeekVFourFlashNonTargetAccLo` | 98.8 | non-target accuracy (%), G1 T3, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGOneTThreeDeepSeekVFourFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), G1 T3, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGOneTThreeDeepSeekVFourFlashNonTargetAccCI` | [98.8, 100.0] | non-target accuracy (%), G1 T3, deepseek-v4-flash, 95% CI |
| `\PfourGOneTThreeDeepSeekVFourFlashNonTargetAccN` | 940 | non-target accuracy (%), G1 T3, deepseek-v4-flash, n |
| `\PfourGOneTThreeDeepSeekVFourFlashNonTargetAccP` | n/a | non-target accuracy (%), G1 T3, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsr` | 2.2 | ASR (%), G1 T3, qwen3.8-27b |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrLo` | 0.4 | ASR (%), G1 T3, qwen3.8-27b, lower 95% CI bound |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrHi` | 3.9 | ASR (%), G1 T3, qwen3.8-27b, upper 95% CI bound |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrCI` | [0.4, 3.9] | ASR (%), G1 T3, qwen3.8-27b, 95% CI |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrN` | 232 | ASR (%), G1 T3, qwen3.8-27b, n |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrP` | n/a | ASR (%), G1 T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrDropped` | 2.2 | ASR (%) unparsed dropped, G1 T3, qwen3.8-27b |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrDroppedLo` | 0.4 | ASR (%) unparsed dropped, G1 T3, qwen3.8-27b, lower 95% CI bound |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrDroppedHi` | 3.9 | ASR (%) unparsed dropped, G1 T3, qwen3.8-27b, upper 95% CI bound |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrDroppedCI` | [0.4, 3.9] | ASR (%) unparsed dropped, G1 T3, qwen3.8-27b, 95% CI |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrDroppedN` | 232 | ASR (%) unparsed dropped, G1 T3, qwen3.8-27b, n |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1 T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrCleanOk` | 0.9 | ASR / clean correct (%), G1 T3, qwen3.8-27b |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrCleanOkLo` | 0.0 | ASR / clean correct (%), G1 T3, qwen3.8-27b, lower 95% CI bound |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrCleanOkHi` | 2.3 | ASR / clean correct (%), G1 T3, qwen3.8-27b, upper 95% CI bound |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrCleanOkCI` | [0.0, 2.3] | ASR / clean correct (%), G1 T3, qwen3.8-27b, 95% CI |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrCleanOkN` | 214 | ASR / clean correct (%), G1 T3, qwen3.8-27b, n |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBAsrCleanOkP` | n/a | ASR / clean correct (%), G1 T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBNonTargetAcc` | 93.9 | non-target accuracy (%), G1 T3, qwen3.8-27b |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBNonTargetAccLo` | 91.0 | non-target accuracy (%), G1 T3, qwen3.8-27b, lower 95% CI bound |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBNonTargetAccHi` | 96.5 | non-target accuracy (%), G1 T3, qwen3.8-27b, upper 95% CI bound |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBNonTargetAccCI` | [91.0, 96.5] | non-target accuracy (%), G1 T3, qwen3.8-27b, 95% CI |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBNonTargetAccN` | 928 | non-target accuracy (%), G1 T3, qwen3.8-27b, n |
| `\PfourGOneTThreeQwenThreeEightTwoSevenBNonTargetAccP` | n/a | non-target accuracy (%), G1 T3, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGemmaFourThreeOneBAsr` | 0.9 | ASR (%), G1 T3, gemma-4-31b-it |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrLo` | 0.0 | ASR (%), G1 T3, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrHi` | 2.4 | ASR (%), G1 T3, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrCI` | [0.0, 2.4] | ASR (%), G1 T3, gemma-4-31b-it, 95% CI |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrN` | 211 | ASR (%), G1 T3, gemma-4-31b-it, n |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrP` | n/a | ASR (%), G1 T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrDropped` | 0.9 | ASR (%) unparsed dropped, G1 T3, gemma-4-31b-it |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrDroppedLo` | 0.0 | ASR (%) unparsed dropped, G1 T3, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrDroppedHi` | 2.4 | ASR (%) unparsed dropped, G1 T3, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrDroppedCI` | [0.0, 2.4] | ASR (%) unparsed dropped, G1 T3, gemma-4-31b-it, 95% CI |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrDroppedN` | 211 | ASR (%) unparsed dropped, G1 T3, gemma-4-31b-it, n |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1 T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrCleanOk` | 0.5 | ASR / clean correct (%), G1 T3, gemma-4-31b-it |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrCleanOkLo` | 0.0 | ASR / clean correct (%), G1 T3, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrCleanOkHi` | 1.5 | ASR / clean correct (%), G1 T3, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrCleanOkCI` | [0.0, 1.5] | ASR / clean correct (%), G1 T3, gemma-4-31b-it, 95% CI |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrCleanOkN` | 208 | ASR / clean correct (%), G1 T3, gemma-4-31b-it, n |
| `\PfourGOneTThreeGemmaFourThreeOneBAsrCleanOkP` | n/a | ASR / clean correct (%), G1 T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGemmaFourThreeOneBNonTargetAcc` | 98.6 | non-target accuracy (%), G1 T3, gemma-4-31b-it |
| `\PfourGOneTThreeGemmaFourThreeOneBNonTargetAccLo` | 96.2 | non-target accuracy (%), G1 T3, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGOneTThreeGemmaFourThreeOneBNonTargetAccHi` | 100.0 | non-target accuracy (%), G1 T3, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGOneTThreeGemmaFourThreeOneBNonTargetAccCI` | [96.2, 100.0] | non-target accuracy (%), G1 T3, gemma-4-31b-it, 95% CI |
| `\PfourGOneTThreeGemmaFourThreeOneBNonTargetAccN` | 844 | non-target accuracy (%), G1 T3, gemma-4-31b-it, n |
| `\PfourGOneTThreeGemmaFourThreeOneBNonTargetAccP` | n/a | non-target accuracy (%), G1 T3, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGLMFiveThreeFlashAsr` | 0.4 | ASR (%), G1 T3, glm-5.3-flash |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrLo` | 0.0 | ASR (%), G1 T3, glm-5.3-flash, lower 95% CI bound |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrHi` | 1.3 | ASR (%), G1 T3, glm-5.3-flash, upper 95% CI bound |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrCI` | [0.0, 1.3] | ASR (%), G1 T3, glm-5.3-flash, 95% CI |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrN` | 235 | ASR (%), G1 T3, glm-5.3-flash, n |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrP` | n/a | ASR (%), G1 T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrDropped` | 0.4 | ASR (%) unparsed dropped, G1 T3, glm-5.3-flash |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrDroppedLo` | 0.0 | ASR (%) unparsed dropped, G1 T3, glm-5.3-flash, lower 95% CI bound |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrDroppedHi` | 1.3 | ASR (%) unparsed dropped, G1 T3, glm-5.3-flash, upper 95% CI bound |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrDroppedCI` | [0.0, 1.3] | ASR (%) unparsed dropped, G1 T3, glm-5.3-flash, 95% CI |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrDroppedN` | 235 | ASR (%) unparsed dropped, G1 T3, glm-5.3-flash, n |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1 T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrCleanOk` | 0.4 | ASR / clean correct (%), G1 T3, glm-5.3-flash |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrCleanOkLo` | 0.0 | ASR / clean correct (%), G1 T3, glm-5.3-flash, lower 95% CI bound |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrCleanOkHi` | 1.3 | ASR / clean correct (%), G1 T3, glm-5.3-flash, upper 95% CI bound |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrCleanOkCI` | [0.0, 1.3] | ASR / clean correct (%), G1 T3, glm-5.3-flash, 95% CI |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrCleanOkN` | 235 | ASR / clean correct (%), G1 T3, glm-5.3-flash, n |
| `\PfourGOneTThreeGLMFiveThreeFlashAsrCleanOkP` | n/a | ASR / clean correct (%), G1 T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGLMFiveThreeFlashNonTargetAcc` | 99.8 | non-target accuracy (%), G1 T3, glm-5.3-flash |
| `\PfourGOneTThreeGLMFiveThreeFlashNonTargetAccLo` | 99.4 | non-target accuracy (%), G1 T3, glm-5.3-flash, lower 95% CI bound |
| `\PfourGOneTThreeGLMFiveThreeFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), G1 T3, glm-5.3-flash, upper 95% CI bound |
| `\PfourGOneTThreeGLMFiveThreeFlashNonTargetAccCI` | [99.4, 100.0] | non-target accuracy (%), G1 T3, glm-5.3-flash, 95% CI |
| `\PfourGOneTThreeGLMFiveThreeFlashNonTargetAccN` | 940 | non-target accuracy (%), G1 T3, glm-5.3-flash, n |
| `\PfourGOneTThreeGLMFiveThreeFlashNonTargetAccP` | n/a | non-target accuracy (%), G1 T3, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGLMFiveTwoAsr` | 0.9 | ASR (%), G1 T3, glm-5.2 |
| `\PfourGOneTThreeGLMFiveTwoAsrLo` | 0.0 | ASR (%), G1 T3, glm-5.2, lower 95% CI bound |
| `\PfourGOneTThreeGLMFiveTwoAsrHi` | 2.1 | ASR (%), G1 T3, glm-5.2, upper 95% CI bound |
| `\PfourGOneTThreeGLMFiveTwoAsrCI` | [0.0, 2.1] | ASR (%), G1 T3, glm-5.2, 95% CI |
| `\PfourGOneTThreeGLMFiveTwoAsrN` | 235 | ASR (%), G1 T3, glm-5.2, n |
| `\PfourGOneTThreeGLMFiveTwoAsrP` | n/a | ASR (%), G1 T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGLMFiveTwoAsrDropped` | 0.9 | ASR (%) unparsed dropped, G1 T3, glm-5.2 |
| `\PfourGOneTThreeGLMFiveTwoAsrDroppedLo` | 0.0 | ASR (%) unparsed dropped, G1 T3, glm-5.2, lower 95% CI bound |
| `\PfourGOneTThreeGLMFiveTwoAsrDroppedHi` | 2.1 | ASR (%) unparsed dropped, G1 T3, glm-5.2, upper 95% CI bound |
| `\PfourGOneTThreeGLMFiveTwoAsrDroppedCI` | [0.0, 2.1] | ASR (%) unparsed dropped, G1 T3, glm-5.2, 95% CI |
| `\PfourGOneTThreeGLMFiveTwoAsrDroppedN` | 235 | ASR (%) unparsed dropped, G1 T3, glm-5.2, n |
| `\PfourGOneTThreeGLMFiveTwoAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1 T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGLMFiveTwoAsrCleanOk` | 0.9 | ASR / clean correct (%), G1 T3, glm-5.2 |
| `\PfourGOneTThreeGLMFiveTwoAsrCleanOkLo` | 0.0 | ASR / clean correct (%), G1 T3, glm-5.2, lower 95% CI bound |
| `\PfourGOneTThreeGLMFiveTwoAsrCleanOkHi` | 2.2 | ASR / clean correct (%), G1 T3, glm-5.2, upper 95% CI bound |
| `\PfourGOneTThreeGLMFiveTwoAsrCleanOkCI` | [0.0, 2.2] | ASR / clean correct (%), G1 T3, glm-5.2, 95% CI |
| `\PfourGOneTThreeGLMFiveTwoAsrCleanOkN` | 231 | ASR / clean correct (%), G1 T3, glm-5.2, n |
| `\PfourGOneTThreeGLMFiveTwoAsrCleanOkP` | n/a | ASR / clean correct (%), G1 T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeGLMFiveTwoNonTargetAcc` | 97.9 | non-target accuracy (%), G1 T3, glm-5.2 |
| `\PfourGOneTThreeGLMFiveTwoNonTargetAccLo` | 95.4 | non-target accuracy (%), G1 T3, glm-5.2, lower 95% CI bound |
| `\PfourGOneTThreeGLMFiveTwoNonTargetAccHi` | 99.6 | non-target accuracy (%), G1 T3, glm-5.2, upper 95% CI bound |
| `\PfourGOneTThreeGLMFiveTwoNonTargetAccCI` | [95.4, 99.6] | non-target accuracy (%), G1 T3, glm-5.2, 95% CI |
| `\PfourGOneTThreeGLMFiveTwoNonTargetAccN` | 940 | non-target accuracy (%), G1 T3, glm-5.2, n |
| `\PfourGOneTThreeGLMFiveTwoNonTargetAccP` | n/a | non-target accuracy (%), G1 T3, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoPooledAsr` | 59.9 | ASR (%), G2u T2, pooled |
| `\PfourGTwoUTTwoPooledAsrLo` | 56.0 | ASR (%), G2u T2, pooled, lower 95% CI bound |
| `\PfourGTwoUTTwoPooledAsrHi` | 63.9 | ASR (%), G2u T2, pooled, upper 95% CI bound |
| `\PfourGTwoUTTwoPooledAsrCI` | [56.0, 63.9] | ASR (%), G2u T2, pooled, 95% CI |
| `\PfourGTwoUTTwoPooledAsrN` | 1{,}155 | ASR (%), G2u T2, pooled, n |
| `\PfourGTwoUTTwoPooledAsrP` | n/a | ASR (%), G2u T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoPooledAsrDropped` | 60.1 | ASR (%) unparsed dropped, G2u T2, pooled |
| `\PfourGTwoUTTwoPooledAsrDroppedLo` | 56.2 | ASR (%) unparsed dropped, G2u T2, pooled, lower 95% CI bound |
| `\PfourGTwoUTTwoPooledAsrDroppedHi` | 64.1 | ASR (%) unparsed dropped, G2u T2, pooled, upper 95% CI bound |
| `\PfourGTwoUTTwoPooledAsrDroppedCI` | [56.2, 64.1] | ASR (%) unparsed dropped, G2u T2, pooled, 95% CI |
| `\PfourGTwoUTTwoPooledAsrDroppedN` | 1{,}152 | ASR (%) unparsed dropped, G2u T2, pooled, n |
| `\PfourGTwoUTTwoPooledAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2u T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoPooledAsrCleanOk` | 60.2 | ASR / clean correct (%), G2u T2, pooled |
| `\PfourGTwoUTTwoPooledAsrCleanOkLo` | 56.3 | ASR / clean correct (%), G2u T2, pooled, lower 95% CI bound |
| `\PfourGTwoUTTwoPooledAsrCleanOkHi` | 64.2 | ASR / clean correct (%), G2u T2, pooled, upper 95% CI bound |
| `\PfourGTwoUTTwoPooledAsrCleanOkCI` | [56.3, 64.2] | ASR / clean correct (%), G2u T2, pooled, 95% CI |
| `\PfourGTwoUTTwoPooledAsrCleanOkN` | 1{,}134 | ASR / clean correct (%), G2u T2, pooled, n |
| `\PfourGTwoUTTwoPooledAsrCleanOkP` | n/a | ASR / clean correct (%), G2u T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoPooledNonTargetAcc` | 98.2 | non-target accuracy (%), G2u T2, pooled |
| `\PfourGTwoUTTwoPooledNonTargetAccLo` | 97.1 | non-target accuracy (%), G2u T2, pooled, lower 95% CI bound |
| `\PfourGTwoUTTwoPooledNonTargetAccHi` | 99.1 | non-target accuracy (%), G2u T2, pooled, upper 95% CI bound |
| `\PfourGTwoUTTwoPooledNonTargetAccCI` | [97.1, 99.1] | non-target accuracy (%), G2u T2, pooled, 95% CI |
| `\PfourGTwoUTTwoPooledNonTargetAccN` | 4{,}608 | non-target accuracy (%), G2u T2, pooled, n |
| `\PfourGTwoUTTwoPooledNonTargetAccP` | n/a | non-target accuracy (%), G2u T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsr` | 52.6 | ASR (%), G2u T2, deepseek-v4-flash |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrLo` | 46.0 | ASR (%), G2u T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrHi` | 59.2 | ASR (%), G2u T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrCI` | [46.0, 59.2] | ASR (%), G2u T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrN` | 234 | ASR (%), G2u T2, deepseek-v4-flash, n |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrP` | n/a | ASR (%), G2u T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrDropped` | 52.6 | ASR (%) unparsed dropped, G2u T2, deepseek-v4-flash |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrDroppedLo` | 45.3 | ASR (%) unparsed dropped, G2u T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrDroppedHi` | 59.1 | ASR (%) unparsed dropped, G2u T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrDroppedCI` | [45.3, 59.1] | ASR (%) unparsed dropped, G2u T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrDroppedN` | 234 | ASR (%) unparsed dropped, G2u T2, deepseek-v4-flash, n |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2u T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrCleanOk` | 52.6 | ASR / clean correct (%), G2u T2, deepseek-v4-flash |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrCleanOkLo` | 46.2 | ASR / clean correct (%), G2u T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrCleanOkHi` | 59.6 | ASR / clean correct (%), G2u T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrCleanOkCI` | [46.2, 59.6] | ASR / clean correct (%), G2u T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrCleanOkN` | 234 | ASR / clean correct (%), G2u T2, deepseek-v4-flash, n |
| `\PfourGTwoUTTwoDeepSeekVFourFlashAsrCleanOkP` | n/a | ASR / clean correct (%), G2u T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoDeepSeekVFourFlashNonTargetAcc` | 99.6 | non-target accuracy (%), G2u T2, deepseek-v4-flash |
| `\PfourGTwoUTTwoDeepSeekVFourFlashNonTargetAccLo` | 98.7 | non-target accuracy (%), G2u T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoUTTwoDeepSeekVFourFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), G2u T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoUTTwoDeepSeekVFourFlashNonTargetAccCI` | [98.7, 100.0] | non-target accuracy (%), G2u T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoUTTwoDeepSeekVFourFlashNonTargetAccN` | 936 | non-target accuracy (%), G2u T2, deepseek-v4-flash, n |
| `\PfourGTwoUTTwoDeepSeekVFourFlashNonTargetAccP` | n/a | non-target accuracy (%), G2u T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsr` | 53.0 | ASR (%), G2u T2, qwen3.8-27b |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrLo` | 47.2 | ASR (%), G2u T2, qwen3.8-27b, lower 95% CI bound |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrHi` | 59.1 | ASR (%), G2u T2, qwen3.8-27b, upper 95% CI bound |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrCI` | [47.2, 59.1] | ASR (%), G2u T2, qwen3.8-27b, 95% CI |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrN` | 230 | ASR (%), G2u T2, qwen3.8-27b, n |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrP` | n/a | ASR (%), G2u T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrDropped` | 53.0 | ASR (%) unparsed dropped, G2u T2, qwen3.8-27b |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrDroppedLo` | 47.2 | ASR (%) unparsed dropped, G2u T2, qwen3.8-27b, lower 95% CI bound |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrDroppedHi` | 59.0 | ASR (%) unparsed dropped, G2u T2, qwen3.8-27b, upper 95% CI bound |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrDroppedCI` | [47.2, 59.0] | ASR (%) unparsed dropped, G2u T2, qwen3.8-27b, 95% CI |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrDroppedN` | 230 | ASR (%) unparsed dropped, G2u T2, qwen3.8-27b, n |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2u T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrCleanOk` | 52.8 | ASR / clean correct (%), G2u T2, qwen3.8-27b |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrCleanOkLo` | 46.5 | ASR / clean correct (%), G2u T2, qwen3.8-27b, lower 95% CI bound |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrCleanOkHi` | 58.7 | ASR / clean correct (%), G2u T2, qwen3.8-27b, upper 95% CI bound |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrCleanOkCI` | [46.5, 58.7] | ASR / clean correct (%), G2u T2, qwen3.8-27b, 95% CI |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrCleanOkN` | 218 | ASR / clean correct (%), G2u T2, qwen3.8-27b, n |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBAsrCleanOkP` | n/a | ASR / clean correct (%), G2u T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBNonTargetAcc` | 95.1 | non-target accuracy (%), G2u T2, qwen3.8-27b |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBNonTargetAccLo` | 92.7 | non-target accuracy (%), G2u T2, qwen3.8-27b, lower 95% CI bound |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBNonTargetAccHi` | 97.5 | non-target accuracy (%), G2u T2, qwen3.8-27b, upper 95% CI bound |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBNonTargetAccCI` | [92.7, 97.5] | non-target accuracy (%), G2u T2, qwen3.8-27b, 95% CI |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBNonTargetAccN` | 920 | non-target accuracy (%), G2u T2, qwen3.8-27b, n |
| `\PfourGTwoUTTwoQwenThreeEightTwoSevenBNonTargetAccP` | n/a | non-target accuracy (%), G2u T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsr` | 72.2 | ASR (%), G2u T2, gemma-4-31b-it |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrLo` | 67.1 | ASR (%), G2u T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrHi` | 77.6 | ASR (%), G2u T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrCI` | [67.1, 77.6] | ASR (%), G2u T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrN` | 223 | ASR (%), G2u T2, gemma-4-31b-it, n |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrP` | n/a | ASR (%), G2u T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrDropped` | 72.5 | ASR (%) unparsed dropped, G2u T2, gemma-4-31b-it |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrDroppedLo` | 66.8 | ASR (%) unparsed dropped, G2u T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrDroppedHi` | 77.7 | ASR (%) unparsed dropped, G2u T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrDroppedCI` | [66.8, 77.7] | ASR (%) unparsed dropped, G2u T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrDroppedN` | 222 | ASR (%) unparsed dropped, G2u T2, gemma-4-31b-it, n |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2u T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrCleanOk` | 72.7 | ASR / clean correct (%), G2u T2, gemma-4-31b-it |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrCleanOkLo` | 67.3 | ASR / clean correct (%), G2u T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrCleanOkHi` | 78.2 | ASR / clean correct (%), G2u T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrCleanOkCI` | [67.3, 78.2] | ASR / clean correct (%), G2u T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrCleanOkN` | 220 | ASR / clean correct (%), G2u T2, gemma-4-31b-it, n |
| `\PfourGTwoUTTwoGemmaFourThreeOneBAsrCleanOkP` | n/a | ASR / clean correct (%), G2u T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGemmaFourThreeOneBNonTargetAcc` | 98.5 | non-target accuracy (%), G2u T2, gemma-4-31b-it |
| `\PfourGTwoUTTwoGemmaFourThreeOneBNonTargetAccLo` | 96.6 | non-target accuracy (%), G2u T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoUTTwoGemmaFourThreeOneBNonTargetAccHi` | 100.0 | non-target accuracy (%), G2u T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoUTTwoGemmaFourThreeOneBNonTargetAccCI` | [96.6, 100.0] | non-target accuracy (%), G2u T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoUTTwoGemmaFourThreeOneBNonTargetAccN` | 888 | non-target accuracy (%), G2u T2, gemma-4-31b-it, n |
| `\PfourGTwoUTTwoGemmaFourThreeOneBNonTargetAccP` | n/a | non-target accuracy (%), G2u T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsr` | 60.3 | ASR (%), G2u T2, glm-5.3-flash |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrLo` | 55.7 | ASR (%), G2u T2, glm-5.3-flash, lower 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrHi` | 65.0 | ASR (%), G2u T2, glm-5.3-flash, upper 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrCI` | [55.7, 65.0] | ASR (%), G2u T2, glm-5.3-flash, 95% CI |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrN` | 234 | ASR (%), G2u T2, glm-5.3-flash, n |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrP` | n/a | ASR (%), G2u T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrDropped` | 60.8 | ASR (%) unparsed dropped, G2u T2, glm-5.3-flash |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrDroppedLo` | 56.0 | ASR (%) unparsed dropped, G2u T2, glm-5.3-flash, lower 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrDroppedHi` | 65.7 | ASR (%) unparsed dropped, G2u T2, glm-5.3-flash, upper 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrDroppedCI` | [56.0, 65.7] | ASR (%) unparsed dropped, G2u T2, glm-5.3-flash, 95% CI |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrDroppedN` | 232 | ASR (%) unparsed dropped, G2u T2, glm-5.3-flash, n |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2u T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrCleanOk` | 61.0 | ASR / clean correct (%), G2u T2, glm-5.3-flash |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrCleanOkLo` | 56.4 | ASR / clean correct (%), G2u T2, glm-5.3-flash, lower 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrCleanOkHi` | 65.9 | ASR / clean correct (%), G2u T2, glm-5.3-flash, upper 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrCleanOkCI` | [56.4, 65.9] | ASR / clean correct (%), G2u T2, glm-5.3-flash, 95% CI |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrCleanOkN` | 231 | ASR / clean correct (%), G2u T2, glm-5.3-flash, n |
| `\PfourGTwoUTTwoGLMFiveThreeFlashAsrCleanOkP` | n/a | ASR / clean correct (%), G2u T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGLMFiveThreeFlashNonTargetAcc` | 99.5 | non-target accuracy (%), G2u T2, glm-5.3-flash |
| `\PfourGTwoUTTwoGLMFiveThreeFlashNonTargetAccLo` | 98.5 | non-target accuracy (%), G2u T2, glm-5.3-flash, lower 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveThreeFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), G2u T2, glm-5.3-flash, upper 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveThreeFlashNonTargetAccCI` | [98.5, 100.0] | non-target accuracy (%), G2u T2, glm-5.3-flash, 95% CI |
| `\PfourGTwoUTTwoGLMFiveThreeFlashNonTargetAccN` | 928 | non-target accuracy (%), G2u T2, glm-5.3-flash, n |
| `\PfourGTwoUTTwoGLMFiveThreeFlashNonTargetAccP` | n/a | non-target accuracy (%), G2u T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGLMFiveTwoAsr` | 62.0 | ASR (%), G2u T2, glm-5.2 |
| `\PfourGTwoUTTwoGLMFiveTwoAsrLo` | 57.7 | ASR (%), G2u T2, glm-5.2, lower 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveTwoAsrHi` | 66.2 | ASR (%), G2u T2, glm-5.2, upper 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveTwoAsrCI` | [57.7, 66.2] | ASR (%), G2u T2, glm-5.2, 95% CI |
| `\PfourGTwoUTTwoGLMFiveTwoAsrN` | 234 | ASR (%), G2u T2, glm-5.2, n |
| `\PfourGTwoUTTwoGLMFiveTwoAsrP` | n/a | ASR (%), G2u T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGLMFiveTwoAsrDropped` | 62.0 | ASR (%) unparsed dropped, G2u T2, glm-5.2 |
| `\PfourGTwoUTTwoGLMFiveTwoAsrDroppedLo` | 57.9 | ASR (%) unparsed dropped, G2u T2, glm-5.2, lower 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveTwoAsrDroppedHi` | 66.0 | ASR (%) unparsed dropped, G2u T2, glm-5.2, upper 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveTwoAsrDroppedCI` | [57.9, 66.0] | ASR (%) unparsed dropped, G2u T2, glm-5.2, 95% CI |
| `\PfourGTwoUTTwoGLMFiveTwoAsrDroppedN` | 234 | ASR (%) unparsed dropped, G2u T2, glm-5.2, n |
| `\PfourGTwoUTTwoGLMFiveTwoAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2u T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGLMFiveTwoAsrCleanOk` | 62.3 | ASR / clean correct (%), G2u T2, glm-5.2 |
| `\PfourGTwoUTTwoGLMFiveTwoAsrCleanOkLo` | 57.9 | ASR / clean correct (%), G2u T2, glm-5.2, lower 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveTwoAsrCleanOkHi` | 66.8 | ASR / clean correct (%), G2u T2, glm-5.2, upper 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveTwoAsrCleanOkCI` | [57.9, 66.8] | ASR / clean correct (%), G2u T2, glm-5.2, 95% CI |
| `\PfourGTwoUTTwoGLMFiveTwoAsrCleanOkN` | 231 | ASR / clean correct (%), G2u T2, glm-5.2, n |
| `\PfourGTwoUTTwoGLMFiveTwoAsrCleanOkP` | n/a | ASR / clean correct (%), G2u T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUTTwoGLMFiveTwoNonTargetAcc` | 98.3 | non-target accuracy (%), G2u T2, glm-5.2 |
| `\PfourGTwoUTTwoGLMFiveTwoNonTargetAccLo` | 96.6 | non-target accuracy (%), G2u T2, glm-5.2, lower 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveTwoNonTargetAccHi` | 99.8 | non-target accuracy (%), G2u T2, glm-5.2, upper 95% CI bound |
| `\PfourGTwoUTTwoGLMFiveTwoNonTargetAccCI` | [96.6, 99.8] | non-target accuracy (%), G2u T2, glm-5.2, 95% CI |
| `\PfourGTwoUTTwoGLMFiveTwoNonTargetAccN` | 936 | non-target accuracy (%), G2u T2, glm-5.2, n |
| `\PfourGTwoUTTwoGLMFiveTwoNonTargetAccP` | n/a | non-target accuracy (%), G2u T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoPooledAsr` | 26.5 | ASR (%), G2s T2, pooled |
| `\PfourGTwoSTTwoPooledAsrLo` | 24.5 | ASR (%), G2s T2, pooled, lower 95% CI bound |
| `\PfourGTwoSTTwoPooledAsrHi` | 28.6 | ASR (%), G2s T2, pooled, upper 95% CI bound |
| `\PfourGTwoSTTwoPooledAsrCI` | [24.5, 28.6] | ASR (%), G2s T2, pooled, 95% CI |
| `\PfourGTwoSTTwoPooledAsrN` | 1{,}155 | ASR (%), G2s T2, pooled, n |
| `\PfourGTwoSTTwoPooledAsrP` | n/a | ASR (%), G2s T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoPooledAsrDropped` | 26.7 | ASR (%) unparsed dropped, G2s T2, pooled |
| `\PfourGTwoSTTwoPooledAsrDroppedLo` | 24.8 | ASR (%) unparsed dropped, G2s T2, pooled, lower 95% CI bound |
| `\PfourGTwoSTTwoPooledAsrDroppedHi` | 28.7 | ASR (%) unparsed dropped, G2s T2, pooled, upper 95% CI bound |
| `\PfourGTwoSTTwoPooledAsrDroppedCI` | [24.8, 28.7] | ASR (%) unparsed dropped, G2s T2, pooled, 95% CI |
| `\PfourGTwoSTTwoPooledAsrDroppedN` | 1{,}148 | ASR (%) unparsed dropped, G2s T2, pooled, n |
| `\PfourGTwoSTTwoPooledAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2s T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoPooledAsrCleanOk` | 26.7 | ASR / clean correct (%), G2s T2, pooled |
| `\PfourGTwoSTTwoPooledAsrCleanOkLo` | 24.6 | ASR / clean correct (%), G2s T2, pooled, lower 95% CI bound |
| `\PfourGTwoSTTwoPooledAsrCleanOkHi` | 29.0 | ASR / clean correct (%), G2s T2, pooled, upper 95% CI bound |
| `\PfourGTwoSTTwoPooledAsrCleanOkCI` | [24.6, 29.0] | ASR / clean correct (%), G2s T2, pooled, 95% CI |
| `\PfourGTwoSTTwoPooledAsrCleanOkN` | 1{,}123 | ASR / clean correct (%), G2s T2, pooled, n |
| `\PfourGTwoSTTwoPooledAsrCleanOkP` | n/a | ASR / clean correct (%), G2s T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoPooledNonTargetAcc` | 98.2 | non-target accuracy (%), G2s T2, pooled |
| `\PfourGTwoSTTwoPooledNonTargetAccLo` | 97.2 | non-target accuracy (%), G2s T2, pooled, lower 95% CI bound |
| `\PfourGTwoSTTwoPooledNonTargetAccHi` | 99.0 | non-target accuracy (%), G2s T2, pooled, upper 95% CI bound |
| `\PfourGTwoSTTwoPooledNonTargetAccCI` | [97.2, 99.0] | non-target accuracy (%), G2s T2, pooled, 95% CI |
| `\PfourGTwoSTTwoPooledNonTargetAccN` | 4{,}592 | non-target accuracy (%), G2s T2, pooled, n |
| `\PfourGTwoSTTwoPooledNonTargetAccP` | n/a | non-target accuracy (%), G2s T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsr` | 42.3 | ASR (%), G2s T2, deepseek-v4-flash |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrLo` | 37.0 | ASR (%), G2s T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrHi` | 47.6 | ASR (%), G2s T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrCI` | [37.0, 47.6] | ASR (%), G2s T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrN` | 234 | ASR (%), G2s T2, deepseek-v4-flash, n |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrP` | n/a | ASR (%), G2s T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrDropped` | 42.3 | ASR (%) unparsed dropped, G2s T2, deepseek-v4-flash |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrDroppedLo` | 37.0 | ASR (%) unparsed dropped, G2s T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrDroppedHi` | 47.6 | ASR (%) unparsed dropped, G2s T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrDroppedCI` | [37.0, 47.6] | ASR (%) unparsed dropped, G2s T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrDroppedN` | 234 | ASR (%) unparsed dropped, G2s T2, deepseek-v4-flash, n |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2s T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrCleanOk` | 42.7 | ASR / clean correct (%), G2s T2, deepseek-v4-flash |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrCleanOkLo` | 37.6 | ASR / clean correct (%), G2s T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrCleanOkHi` | 48.1 | ASR / clean correct (%), G2s T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrCleanOkCI` | [37.6, 48.1] | ASR / clean correct (%), G2s T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrCleanOkN` | 232 | ASR / clean correct (%), G2s T2, deepseek-v4-flash, n |
| `\PfourGTwoSTTwoDeepSeekVFourFlashAsrCleanOkP` | n/a | ASR / clean correct (%), G2s T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoDeepSeekVFourFlashNonTargetAcc` | 99.4 | non-target accuracy (%), G2s T2, deepseek-v4-flash |
| `\PfourGTwoSTTwoDeepSeekVFourFlashNonTargetAccLo` | 98.4 | non-target accuracy (%), G2s T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoSTTwoDeepSeekVFourFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), G2s T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoSTTwoDeepSeekVFourFlashNonTargetAccCI` | [98.4, 100.0] | non-target accuracy (%), G2s T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoSTTwoDeepSeekVFourFlashNonTargetAccN` | 936 | non-target accuracy (%), G2s T2, deepseek-v4-flash, n |
| `\PfourGTwoSTTwoDeepSeekVFourFlashNonTargetAccP` | n/a | non-target accuracy (%), G2s T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsr` | 16.5 | ASR (%), G2s T2, qwen3.8-27b |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrLo` | 13.1 | ASR (%), G2s T2, qwen3.8-27b, lower 95% CI bound |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrHi` | 19.8 | ASR (%), G2s T2, qwen3.8-27b, upper 95% CI bound |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrCI` | [13.1, 19.8] | ASR (%), G2s T2, qwen3.8-27b, 95% CI |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrN` | 230 | ASR (%), G2s T2, qwen3.8-27b, n |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrP` | n/a | ASR (%), G2s T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrDropped` | 16.5 | ASR (%) unparsed dropped, G2s T2, qwen3.8-27b |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrDroppedLo` | 13.1 | ASR (%) unparsed dropped, G2s T2, qwen3.8-27b, lower 95% CI bound |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrDroppedHi` | 19.8 | ASR (%) unparsed dropped, G2s T2, qwen3.8-27b, upper 95% CI bound |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrDroppedCI` | [13.1, 19.8] | ASR (%) unparsed dropped, G2s T2, qwen3.8-27b, 95% CI |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrDroppedN` | 230 | ASR (%) unparsed dropped, G2s T2, qwen3.8-27b, n |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2s T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrCleanOk` | 15.3 | ASR / clean correct (%), G2s T2, qwen3.8-27b |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrCleanOkLo` | 12.2 | ASR / clean correct (%), G2s T2, qwen3.8-27b, lower 95% CI bound |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrCleanOkHi` | 18.3 | ASR / clean correct (%), G2s T2, qwen3.8-27b, upper 95% CI bound |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrCleanOkCI` | [12.2, 18.3] | ASR / clean correct (%), G2s T2, qwen3.8-27b, 95% CI |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrCleanOkN` | 216 | ASR / clean correct (%), G2s T2, qwen3.8-27b, n |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBAsrCleanOkP` | n/a | ASR / clean correct (%), G2s T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBNonTargetAcc` | 94.6 | non-target accuracy (%), G2s T2, qwen3.8-27b |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBNonTargetAccLo` | 92.3 | non-target accuracy (%), G2s T2, qwen3.8-27b, lower 95% CI bound |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBNonTargetAccHi` | 96.8 | non-target accuracy (%), G2s T2, qwen3.8-27b, upper 95% CI bound |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBNonTargetAccCI` | [92.3, 96.8] | non-target accuracy (%), G2s T2, qwen3.8-27b, 95% CI |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBNonTargetAccN` | 920 | non-target accuracy (%), G2s T2, qwen3.8-27b, n |
| `\PfourGTwoSTTwoQwenThreeEightTwoSevenBNonTargetAccP` | n/a | non-target accuracy (%), G2s T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsr` | 13.5 | ASR (%), G2s T2, gemma-4-31b-it |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrLo` | 9.3 | ASR (%), G2s T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrHi` | 17.9 | ASR (%), G2s T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrCI` | [9.3, 17.9] | ASR (%), G2s T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrN` | 223 | ASR (%), G2s T2, gemma-4-31b-it, n |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrP` | n/a | ASR (%), G2s T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrDropped` | 13.9 | ASR (%) unparsed dropped, G2s T2, gemma-4-31b-it |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrDroppedLo` | 9.6 | ASR (%) unparsed dropped, G2s T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrDroppedHi` | 18.6 | ASR (%) unparsed dropped, G2s T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrDroppedCI` | [9.6, 18.6] | ASR (%) unparsed dropped, G2s T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrDroppedN` | 216 | ASR (%) unparsed dropped, G2s T2, gemma-4-31b-it, n |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2s T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrCleanOk` | 14.2 | ASR / clean correct (%), G2s T2, gemma-4-31b-it |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrCleanOkLo` | 9.9 | ASR / clean correct (%), G2s T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrCleanOkHi` | 19.1 | ASR / clean correct (%), G2s T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrCleanOkCI` | [9.9, 19.1] | ASR / clean correct (%), G2s T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrCleanOkN` | 211 | ASR / clean correct (%), G2s T2, gemma-4-31b-it, n |
| `\PfourGTwoSTTwoGemmaFourThreeOneBAsrCleanOkP` | n/a | ASR / clean correct (%), G2s T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGemmaFourThreeOneBNonTargetAcc` | 98.7 | non-target accuracy (%), G2s T2, gemma-4-31b-it |
| `\PfourGTwoSTTwoGemmaFourThreeOneBNonTargetAccLo` | 97.2 | non-target accuracy (%), G2s T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoSTTwoGemmaFourThreeOneBNonTargetAccHi` | 100.0 | non-target accuracy (%), G2s T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoSTTwoGemmaFourThreeOneBNonTargetAccCI` | [97.2, 100.0] | non-target accuracy (%), G2s T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoSTTwoGemmaFourThreeOneBNonTargetAccN` | 864 | non-target accuracy (%), G2s T2, gemma-4-31b-it, n |
| `\PfourGTwoSTTwoGemmaFourThreeOneBNonTargetAccP` | n/a | non-target accuracy (%), G2s T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsr` | 24.4 | ASR (%), G2s T2, glm-5.3-flash |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrLo` | 22.1 | ASR (%), G2s T2, glm-5.3-flash, lower 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrHi` | 26.8 | ASR (%), G2s T2, glm-5.3-flash, upper 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrCI` | [22.1, 26.8] | ASR (%), G2s T2, glm-5.3-flash, 95% CI |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrN` | 234 | ASR (%), G2s T2, glm-5.3-flash, n |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrP` | n/a | ASR (%), G2s T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrDropped` | 24.4 | ASR (%) unparsed dropped, G2s T2, glm-5.3-flash |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrDroppedLo` | 22.1 | ASR (%) unparsed dropped, G2s T2, glm-5.3-flash, lower 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrDroppedHi` | 26.6 | ASR (%) unparsed dropped, G2s T2, glm-5.3-flash, upper 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrDroppedCI` | [22.1, 26.6] | ASR (%) unparsed dropped, G2s T2, glm-5.3-flash, 95% CI |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrDroppedN` | 234 | ASR (%) unparsed dropped, G2s T2, glm-5.3-flash, n |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2s T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrCleanOk` | 24.5 | ASR / clean correct (%), G2s T2, glm-5.3-flash |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrCleanOkLo` | 22.2 | ASR / clean correct (%), G2s T2, glm-5.3-flash, lower 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrCleanOkHi` | 26.9 | ASR / clean correct (%), G2s T2, glm-5.3-flash, upper 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrCleanOkCI` | [22.2, 26.9] | ASR / clean correct (%), G2s T2, glm-5.3-flash, 95% CI |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrCleanOkN` | 233 | ASR / clean correct (%), G2s T2, glm-5.3-flash, n |
| `\PfourGTwoSTTwoGLMFiveThreeFlashAsrCleanOkP` | n/a | ASR / clean correct (%), G2s T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGLMFiveThreeFlashNonTargetAcc` | 99.6 | non-target accuracy (%), G2s T2, glm-5.3-flash |
| `\PfourGTwoSTTwoGLMFiveThreeFlashNonTargetAccLo` | 99.0 | non-target accuracy (%), G2s T2, glm-5.3-flash, lower 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveThreeFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), G2s T2, glm-5.3-flash, upper 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveThreeFlashNonTargetAccCI` | [99.0, 100.0] | non-target accuracy (%), G2s T2, glm-5.3-flash, 95% CI |
| `\PfourGTwoSTTwoGLMFiveThreeFlashNonTargetAccN` | 936 | non-target accuracy (%), G2s T2, glm-5.3-flash, n |
| `\PfourGTwoSTTwoGLMFiveThreeFlashNonTargetAccP` | n/a | non-target accuracy (%), G2s T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGLMFiveTwoAsr` | 35.0 | ASR (%), G2s T2, glm-5.2 |
| `\PfourGTwoSTTwoGLMFiveTwoAsrLo` | 30.9 | ASR (%), G2s T2, glm-5.2, lower 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveTwoAsrHi` | 38.9 | ASR (%), G2s T2, glm-5.2, upper 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveTwoAsrCI` | [30.9, 38.9] | ASR (%), G2s T2, glm-5.2, 95% CI |
| `\PfourGTwoSTTwoGLMFiveTwoAsrN` | 234 | ASR (%), G2s T2, glm-5.2, n |
| `\PfourGTwoSTTwoGLMFiveTwoAsrP` | n/a | ASR (%), G2s T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGLMFiveTwoAsrDropped` | 35.0 | ASR (%) unparsed dropped, G2s T2, glm-5.2 |
| `\PfourGTwoSTTwoGLMFiveTwoAsrDroppedLo` | 31.0 | ASR (%) unparsed dropped, G2s T2, glm-5.2, lower 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveTwoAsrDroppedHi` | 39.1 | ASR (%) unparsed dropped, G2s T2, glm-5.2, upper 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveTwoAsrDroppedCI` | [31.0, 39.1] | ASR (%) unparsed dropped, G2s T2, glm-5.2, 95% CI |
| `\PfourGTwoSTTwoGLMFiveTwoAsrDroppedN` | 234 | ASR (%) unparsed dropped, G2s T2, glm-5.2, n |
| `\PfourGTwoSTTwoGLMFiveTwoAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2s T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGLMFiveTwoAsrCleanOk` | 35.1 | ASR / clean correct (%), G2s T2, glm-5.2 |
| `\PfourGTwoSTTwoGLMFiveTwoAsrCleanOkLo` | 30.9 | ASR / clean correct (%), G2s T2, glm-5.2, lower 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveTwoAsrCleanOkHi` | 39.4 | ASR / clean correct (%), G2s T2, glm-5.2, upper 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveTwoAsrCleanOkCI` | [30.9, 39.4] | ASR / clean correct (%), G2s T2, glm-5.2, 95% CI |
| `\PfourGTwoSTTwoGLMFiveTwoAsrCleanOkN` | 231 | ASR / clean correct (%), G2s T2, glm-5.2, n |
| `\PfourGTwoSTTwoGLMFiveTwoAsrCleanOkP` | n/a | ASR / clean correct (%), G2s T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSTTwoGLMFiveTwoNonTargetAcc` | 98.6 | non-target accuracy (%), G2s T2, glm-5.2 |
| `\PfourGTwoSTTwoGLMFiveTwoNonTargetAccLo` | 96.8 | non-target accuracy (%), G2s T2, glm-5.2, lower 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveTwoNonTargetAccHi` | 100.0 | non-target accuracy (%), G2s T2, glm-5.2, upper 95% CI bound |
| `\PfourGTwoSTTwoGLMFiveTwoNonTargetAccCI` | [96.8, 100.0] | non-target accuracy (%), G2s T2, glm-5.2, 95% CI |
| `\PfourGTwoSTTwoGLMFiveTwoNonTargetAccN` | 936 | non-target accuracy (%), G2s T2, glm-5.2, n |
| `\PfourGTwoSTTwoGLMFiveTwoNonTargetAccP` | n/a | non-target accuracy (%), G2s T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoPooledAsr` | 60.1 | ASR (%), G2s_insider T2, pooled |
| `\PfourGTwoSInsiderTTwoPooledAsrLo` | 56.0 | ASR (%), G2s_insider T2, pooled, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoPooledAsrHi` | 64.1 | ASR (%), G2s_insider T2, pooled, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoPooledAsrCI` | [56.0, 64.1] | ASR (%), G2s_insider T2, pooled, 95% CI |
| `\PfourGTwoSInsiderTTwoPooledAsrN` | 1{,}155 | ASR (%), G2s_insider T2, pooled, n |
| `\PfourGTwoSInsiderTTwoPooledAsrP` | n/a | ASR (%), G2s_insider T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoPooledAsrDropped` | 60.1 | ASR (%) unparsed dropped, G2s_insider T2, pooled |
| `\PfourGTwoSInsiderTTwoPooledAsrDroppedLo` | 55.9 | ASR (%) unparsed dropped, G2s_insider T2, pooled, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoPooledAsrDroppedHi` | 64.0 | ASR (%) unparsed dropped, G2s_insider T2, pooled, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoPooledAsrDroppedCI` | [55.9, 64.0] | ASR (%) unparsed dropped, G2s_insider T2, pooled, 95% CI |
| `\PfourGTwoSInsiderTTwoPooledAsrDroppedN` | 1{,}154 | ASR (%) unparsed dropped, G2s_insider T2, pooled, n |
| `\PfourGTwoSInsiderTTwoPooledAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2s_insider T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoPooledAsrCleanOk` | 59.9 | ASR / clean correct (%), G2s_insider T2, pooled |
| `\PfourGTwoSInsiderTTwoPooledAsrCleanOkLo` | 55.5 | ASR / clean correct (%), G2s_insider T2, pooled, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoPooledAsrCleanOkHi` | 63.8 | ASR / clean correct (%), G2s_insider T2, pooled, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoPooledAsrCleanOkCI` | [55.5, 63.8] | ASR / clean correct (%), G2s_insider T2, pooled, 95% CI |
| `\PfourGTwoSInsiderTTwoPooledAsrCleanOkN` | 1{,}129 | ASR / clean correct (%), G2s_insider T2, pooled, n |
| `\PfourGTwoSInsiderTTwoPooledAsrCleanOkP` | n/a | ASR / clean correct (%), G2s_insider T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoPooledNonTargetAcc` | 98.1 | non-target accuracy (%), G2s_insider T2, pooled |
| `\PfourGTwoSInsiderTTwoPooledNonTargetAccLo` | 97.1 | non-target accuracy (%), G2s_insider T2, pooled, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoPooledNonTargetAccHi` | 98.9 | non-target accuracy (%), G2s_insider T2, pooled, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoPooledNonTargetAccCI` | [97.1, 98.9] | non-target accuracy (%), G2s_insider T2, pooled, 95% CI |
| `\PfourGTwoSInsiderTTwoPooledNonTargetAccN` | 4{,}616 | non-target accuracy (%), G2s_insider T2, pooled, n |
| `\PfourGTwoSInsiderTTwoPooledNonTargetAccP` | n/a | non-target accuracy (%), G2s_insider T2, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsr` | 52.1 | ASR (%), G2s_insider T2, deepseek-v4-flash |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrLo` | 46.4 | ASR (%), G2s_insider T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrHi` | 58.1 | ASR (%), G2s_insider T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrCI` | [46.4, 58.1] | ASR (%), G2s_insider T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrN` | 234 | ASR (%), G2s_insider T2, deepseek-v4-flash, n |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrP` | n/a | ASR (%), G2s_insider T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrDropped` | 52.1 | ASR (%) unparsed dropped, G2s_insider T2, deepseek-v4-flash |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrDroppedLo` | 46.4 | ASR (%) unparsed dropped, G2s_insider T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrDroppedHi` | 58.1 | ASR (%) unparsed dropped, G2s_insider T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrDroppedCI` | [46.4, 58.1] | ASR (%) unparsed dropped, G2s_insider T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrDroppedN` | 234 | ASR (%) unparsed dropped, G2s_insider T2, deepseek-v4-flash, n |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2s_insider T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrCleanOk` | 52.4 | ASR / clean correct (%), G2s_insider T2, deepseek-v4-flash |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrCleanOkLo` | 46.5 | ASR / clean correct (%), G2s_insider T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrCleanOkHi` | 58.4 | ASR / clean correct (%), G2s_insider T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrCleanOkCI` | [46.5, 58.4] | ASR / clean correct (%), G2s_insider T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrCleanOkN` | 233 | ASR / clean correct (%), G2s_insider T2, deepseek-v4-flash, n |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashAsrCleanOkP` | n/a | ASR / clean correct (%), G2s_insider T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashNonTargetAcc` | 99.6 | non-target accuracy (%), G2s_insider T2, deepseek-v4-flash |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashNonTargetAccLo` | 98.9 | non-target accuracy (%), G2s_insider T2, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), G2s_insider T2, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashNonTargetAccCI` | [98.9, 100.0] | non-target accuracy (%), G2s_insider T2, deepseek-v4-flash, 95% CI |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashNonTargetAccN` | 936 | non-target accuracy (%), G2s_insider T2, deepseek-v4-flash, n |
| `\PfourGTwoSInsiderTTwoDeepSeekVFourFlashNonTargetAccP` | n/a | non-target accuracy (%), G2s_insider T2, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsr` | 54.3 | ASR (%), G2s_insider T2, qwen3.8-27b |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrLo` | 47.9 | ASR (%), G2s_insider T2, qwen3.8-27b, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrHi` | 60.8 | ASR (%), G2s_insider T2, qwen3.8-27b, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrCI` | [47.9, 60.8] | ASR (%), G2s_insider T2, qwen3.8-27b, 95% CI |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrN` | 230 | ASR (%), G2s_insider T2, qwen3.8-27b, n |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrP` | n/a | ASR (%), G2s_insider T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrDropped` | 54.3 | ASR (%) unparsed dropped, G2s_insider T2, qwen3.8-27b |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrDroppedLo` | 47.7 | ASR (%) unparsed dropped, G2s_insider T2, qwen3.8-27b, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrDroppedHi` | 60.8 | ASR (%) unparsed dropped, G2s_insider T2, qwen3.8-27b, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrDroppedCI` | [47.7, 60.8] | ASR (%) unparsed dropped, G2s_insider T2, qwen3.8-27b, 95% CI |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrDroppedN` | 230 | ASR (%) unparsed dropped, G2s_insider T2, qwen3.8-27b, n |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2s_insider T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrCleanOk` | 53.2 | ASR / clean correct (%), G2s_insider T2, qwen3.8-27b |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrCleanOkLo` | 46.5 | ASR / clean correct (%), G2s_insider T2, qwen3.8-27b, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrCleanOkHi` | 59.9 | ASR / clean correct (%), G2s_insider T2, qwen3.8-27b, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrCleanOkCI` | [46.5, 59.9] | ASR / clean correct (%), G2s_insider T2, qwen3.8-27b, 95% CI |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrCleanOkN` | 218 | ASR / clean correct (%), G2s_insider T2, qwen3.8-27b, n |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBAsrCleanOkP` | n/a | ASR / clean correct (%), G2s_insider T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBNonTargetAcc` | 94.5 | non-target accuracy (%), G2s_insider T2, qwen3.8-27b |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBNonTargetAccLo` | 91.9 | non-target accuracy (%), G2s_insider T2, qwen3.8-27b, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBNonTargetAccHi` | 96.8 | non-target accuracy (%), G2s_insider T2, qwen3.8-27b, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBNonTargetAccCI` | [91.9, 96.8] | non-target accuracy (%), G2s_insider T2, qwen3.8-27b, 95% CI |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBNonTargetAccN` | 920 | non-target accuracy (%), G2s_insider T2, qwen3.8-27b, n |
| `\PfourGTwoSInsiderTTwoQwenThreeEightTwoSevenBNonTargetAccP` | n/a | non-target accuracy (%), G2s_insider T2, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsr` | 74.4 | ASR (%), G2s_insider T2, gemma-4-31b-it |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrLo` | 69.6 | ASR (%), G2s_insider T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrHi` | 79.2 | ASR (%), G2s_insider T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrCI` | [69.6, 79.2] | ASR (%), G2s_insider T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrN` | 223 | ASR (%), G2s_insider T2, gemma-4-31b-it, n |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrP` | n/a | ASR (%), G2s_insider T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrDropped` | 74.8 | ASR (%) unparsed dropped, G2s_insider T2, gemma-4-31b-it |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrDroppedLo` | 69.7 | ASR (%) unparsed dropped, G2s_insider T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrDroppedHi` | 79.7 | ASR (%) unparsed dropped, G2s_insider T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrDroppedCI` | [69.7, 79.7] | ASR (%) unparsed dropped, G2s_insider T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrDroppedN` | 222 | ASR (%) unparsed dropped, G2s_insider T2, gemma-4-31b-it, n |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2s_insider T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrCleanOk` | 74.3 | ASR / clean correct (%), G2s_insider T2, gemma-4-31b-it |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrCleanOkLo` | 69.4 | ASR / clean correct (%), G2s_insider T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrCleanOkHi` | 79.1 | ASR / clean correct (%), G2s_insider T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrCleanOkCI` | [69.4, 79.1] | ASR / clean correct (%), G2s_insider T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrCleanOkN` | 214 | ASR / clean correct (%), G2s_insider T2, gemma-4-31b-it, n |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBAsrCleanOkP` | n/a | ASR / clean correct (%), G2s_insider T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBNonTargetAcc` | 98.3 | non-target accuracy (%), G2s_insider T2, gemma-4-31b-it |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBNonTargetAccLo` | 96.3 | non-target accuracy (%), G2s_insider T2, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBNonTargetAccHi` | 99.9 | non-target accuracy (%), G2s_insider T2, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBNonTargetAccCI` | [96.3, 99.9] | non-target accuracy (%), G2s_insider T2, gemma-4-31b-it, 95% CI |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBNonTargetAccN` | 888 | non-target accuracy (%), G2s_insider T2, gemma-4-31b-it, n |
| `\PfourGTwoSInsiderTTwoGemmaFourThreeOneBNonTargetAccP` | n/a | non-target accuracy (%), G2s_insider T2, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsr` | 59.0 | ASR (%), G2s_insider T2, glm-5.3-flash |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrLo` | 53.8 | ASR (%), G2s_insider T2, glm-5.3-flash, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrHi` | 63.8 | ASR (%), G2s_insider T2, glm-5.3-flash, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrCI` | [53.8, 63.8] | ASR (%), G2s_insider T2, glm-5.3-flash, 95% CI |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrN` | 234 | ASR (%), G2s_insider T2, glm-5.3-flash, n |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrP` | n/a | ASR (%), G2s_insider T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrDropped` | 59.0 | ASR (%) unparsed dropped, G2s_insider T2, glm-5.3-flash |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrDroppedLo` | 54.3 | ASR (%) unparsed dropped, G2s_insider T2, glm-5.3-flash, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrDroppedHi` | 64.3 | ASR (%) unparsed dropped, G2s_insider T2, glm-5.3-flash, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrDroppedCI` | [54.3, 64.3] | ASR (%) unparsed dropped, G2s_insider T2, glm-5.3-flash, 95% CI |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrDroppedN` | 234 | ASR (%) unparsed dropped, G2s_insider T2, glm-5.3-flash, n |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2s_insider T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrCleanOk` | 59.0 | ASR / clean correct (%), G2s_insider T2, glm-5.3-flash |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrCleanOkLo` | 54.0 | ASR / clean correct (%), G2s_insider T2, glm-5.3-flash, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrCleanOkHi` | 63.8 | ASR / clean correct (%), G2s_insider T2, glm-5.3-flash, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrCleanOkCI` | [54.0, 63.8] | ASR / clean correct (%), G2s_insider T2, glm-5.3-flash, 95% CI |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrCleanOkN` | 234 | ASR / clean correct (%), G2s_insider T2, glm-5.3-flash, n |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashAsrCleanOkP` | n/a | ASR / clean correct (%), G2s_insider T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashNonTargetAcc` | 99.7 | non-target accuracy (%), G2s_insider T2, glm-5.3-flash |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashNonTargetAccLo` | 99.1 | non-target accuracy (%), G2s_insider T2, glm-5.3-flash, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), G2s_insider T2, glm-5.3-flash, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashNonTargetAccCI` | [99.1, 100.0] | non-target accuracy (%), G2s_insider T2, glm-5.3-flash, 95% CI |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashNonTargetAccN` | 936 | non-target accuracy (%), G2s_insider T2, glm-5.3-flash, n |
| `\PfourGTwoSInsiderTTwoGLMFiveThreeFlashNonTargetAccP` | n/a | non-target accuracy (%), G2s_insider T2, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsr` | 61.1 | ASR (%), G2s_insider T2, glm-5.2 |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrLo` | 56.8 | ASR (%), G2s_insider T2, glm-5.2, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrHi` | 65.7 | ASR (%), G2s_insider T2, glm-5.2, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrCI` | [56.8, 65.7] | ASR (%), G2s_insider T2, glm-5.2, 95% CI |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrN` | 234 | ASR (%), G2s_insider T2, glm-5.2, n |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrP` | n/a | ASR (%), G2s_insider T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrDropped` | 61.1 | ASR (%) unparsed dropped, G2s_insider T2, glm-5.2 |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrDroppedLo` | 56.2 | ASR (%) unparsed dropped, G2s_insider T2, glm-5.2, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrDroppedHi` | 65.8 | ASR (%) unparsed dropped, G2s_insider T2, glm-5.2, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrDroppedCI` | [56.2, 65.8] | ASR (%) unparsed dropped, G2s_insider T2, glm-5.2, 95% CI |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrDroppedN` | 234 | ASR (%) unparsed dropped, G2s_insider T2, glm-5.2, n |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrDroppedP` | n/a | ASR (%) unparsed dropped, G2s_insider T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrCleanOk` | 61.3 | ASR / clean correct (%), G2s_insider T2, glm-5.2 |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrCleanOkLo` | 56.5 | ASR / clean correct (%), G2s_insider T2, glm-5.2, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrCleanOkHi` | 65.9 | ASR / clean correct (%), G2s_insider T2, glm-5.2, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrCleanOkCI` | [56.5, 65.9] | ASR / clean correct (%), G2s_insider T2, glm-5.2, 95% CI |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrCleanOkN` | 230 | ASR / clean correct (%), G2s_insider T2, glm-5.2, n |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoAsrCleanOkP` | n/a | ASR / clean correct (%), G2s_insider T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoNonTargetAcc` | 98.4 | non-target accuracy (%), G2s_insider T2, glm-5.2 |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoNonTargetAccLo` | 96.7 | non-target accuracy (%), G2s_insider T2, glm-5.2, lower 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoNonTargetAccHi` | 99.8 | non-target accuracy (%), G2s_insider T2, glm-5.2, upper 95% CI bound |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoNonTargetAccCI` | [96.7, 99.8] | non-target accuracy (%), G2s_insider T2, glm-5.2, 95% CI |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoNonTargetAccN` | 936 | non-target accuracy (%), G2s_insider T2, glm-5.2, n |
| `\PfourGTwoSInsiderTTwoGLMFiveTwoNonTargetAccP` | n/a | non-target accuracy (%), G2s_insider T2, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSPooledAsr` | 0.4 | ASR (%), G1+G2s -, pooled |
| `\PfourGOnePlusGTwoSPooledAsrLo` | 0.1 | ASR (%), G1+G2s -, pooled, lower 95% CI bound |
| `\PfourGOnePlusGTwoSPooledAsrHi` | 0.8 | ASR (%), G1+G2s -, pooled, upper 95% CI bound |
| `\PfourGOnePlusGTwoSPooledAsrCI` | [0.1, 0.8] | ASR (%), G1+G2s -, pooled, 95% CI |
| `\PfourGOnePlusGTwoSPooledAsrN` | 1{,}173 | ASR (%), G1+G2s -, pooled, n |
| `\PfourGOnePlusGTwoSPooledAsrP` | n/a | ASR (%), G1+G2s -, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSPooledAsrDropped` | 0.4 | ASR (%) unparsed dropped, G1+G2s -, pooled |
| `\PfourGOnePlusGTwoSPooledAsrDroppedLo` | 0.1 | ASR (%) unparsed dropped, G1+G2s -, pooled, lower 95% CI bound |
| `\PfourGOnePlusGTwoSPooledAsrDroppedHi` | 0.9 | ASR (%) unparsed dropped, G1+G2s -, pooled, upper 95% CI bound |
| `\PfourGOnePlusGTwoSPooledAsrDroppedCI` | [0.1, 0.9] | ASR (%) unparsed dropped, G1+G2s -, pooled, 95% CI |
| `\PfourGOnePlusGTwoSPooledAsrDroppedN` | 1{,}171 | ASR (%) unparsed dropped, G1+G2s -, pooled, n |
| `\PfourGOnePlusGTwoSPooledAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1+G2s -, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSPooledAsrCleanOk` | 0.1 | ASR / clean correct (%), G1+G2s -, pooled |
| `\PfourGOnePlusGTwoSPooledAsrCleanOkLo` | 0.0 | ASR / clean correct (%), G1+G2s -, pooled, lower 95% CI bound |
| `\PfourGOnePlusGTwoSPooledAsrCleanOkHi` | 0.3 | ASR / clean correct (%), G1+G2s -, pooled, upper 95% CI bound |
| `\PfourGOnePlusGTwoSPooledAsrCleanOkCI` | [0.0, 0.3] | ASR / clean correct (%), G1+G2s -, pooled, 95% CI |
| `\PfourGOnePlusGTwoSPooledAsrCleanOkN` | 1{,}146 | ASR / clean correct (%), G1+G2s -, pooled, n |
| `\PfourGOnePlusGTwoSPooledAsrCleanOkP` | n/a | ASR / clean correct (%), G1+G2s -, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSPooledNonTargetAcc` | 98.1 | non-target accuracy (%), G1+G2s -, pooled |
| `\PfourGOnePlusGTwoSPooledNonTargetAccLo` | 97.2 | non-target accuracy (%), G1+G2s -, pooled, lower 95% CI bound |
| `\PfourGOnePlusGTwoSPooledNonTargetAccHi` | 98.9 | non-target accuracy (%), G1+G2s -, pooled, upper 95% CI bound |
| `\PfourGOnePlusGTwoSPooledNonTargetAccCI` | [97.2, 98.9] | non-target accuracy (%), G1+G2s -, pooled, 95% CI |
| `\PfourGOnePlusGTwoSPooledNonTargetAccN` | 4{,}684 | non-target accuracy (%), G1+G2s -, pooled, n |
| `\PfourGOnePlusGTwoSPooledNonTargetAccP` | n/a | non-target accuracy (%), G1+G2s -, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsr` | 0.0 | ASR (%), G1+G2s -, deepseek-v4-flash |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrLo` | 0.0 | ASR (%), G1+G2s -, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrHi` | 1.6 | ASR (%), G1+G2s -, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrCI` | [0.0, 1.6] | ASR (%), G1+G2s -, deepseek-v4-flash, 95% CI |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrN` | 235 | ASR (%), G1+G2s -, deepseek-v4-flash, n |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrP` | n/a | ASR (%), G1+G2s -, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrDropped` | 0.0 | ASR (%) unparsed dropped, G1+G2s -, deepseek-v4-flash |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrDroppedLo` | 0.0 | ASR (%) unparsed dropped, G1+G2s -, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrDroppedHi` | 1.6 | ASR (%) unparsed dropped, G1+G2s -, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrDroppedCI` | [0.0, 1.6] | ASR (%) unparsed dropped, G1+G2s -, deepseek-v4-flash, 95% CI |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrDroppedN` | 235 | ASR (%) unparsed dropped, G1+G2s -, deepseek-v4-flash, n |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1+G2s -, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrCleanOk` | 0.0 | ASR / clean correct (%), G1+G2s -, deepseek-v4-flash |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrCleanOkLo` | 0.0 | ASR / clean correct (%), G1+G2s -, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrCleanOkHi` | 1.6 | ASR / clean correct (%), G1+G2s -, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrCleanOkCI` | [0.0, 1.6] | ASR / clean correct (%), G1+G2s -, deepseek-v4-flash, 95% CI |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrCleanOkN` | 234 | ASR / clean correct (%), G1+G2s -, deepseek-v4-flash, n |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashAsrCleanOkP` | n/a | ASR / clean correct (%), G1+G2s -, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashNonTargetAcc` | 99.5 | non-target accuracy (%), G1+G2s -, deepseek-v4-flash |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashNonTargetAccLo` | 98.6 | non-target accuracy (%), G1+G2s -, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), G1+G2s -, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashNonTargetAccCI` | [98.6, 100.0] | non-target accuracy (%), G1+G2s -, deepseek-v4-flash, 95% CI |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashNonTargetAccN` | 940 | non-target accuracy (%), G1+G2s -, deepseek-v4-flash, n |
| `\PfourGOnePlusGTwoSDeepSeekVFourFlashNonTargetAccP` | n/a | non-target accuracy (%), G1+G2s -, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsr` | 1.3 | ASR (%), G1+G2s -, qwen3.8-27b |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrLo` | 0.0 | ASR (%), G1+G2s -, qwen3.8-27b, lower 95% CI bound |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrHi` | 2.6 | ASR (%), G1+G2s -, qwen3.8-27b, upper 95% CI bound |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrCI` | [0.0, 2.6] | ASR (%), G1+G2s -, qwen3.8-27b, 95% CI |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrN` | 235 | ASR (%), G1+G2s -, qwen3.8-27b, n |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrP` | n/a | ASR (%), G1+G2s -, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrDropped` | 1.3 | ASR (%) unparsed dropped, G1+G2s -, qwen3.8-27b |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrDroppedLo` | 0.0 | ASR (%) unparsed dropped, G1+G2s -, qwen3.8-27b, lower 95% CI bound |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrDroppedHi` | 3.0 | ASR (%) unparsed dropped, G1+G2s -, qwen3.8-27b, upper 95% CI bound |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrDroppedCI` | [0.0, 3.0] | ASR (%) unparsed dropped, G1+G2s -, qwen3.8-27b, 95% CI |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrDroppedN` | 235 | ASR (%) unparsed dropped, G1+G2s -, qwen3.8-27b, n |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1+G2s -, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrCleanOk` | 0.0 | ASR / clean correct (%), G1+G2s -, qwen3.8-27b |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrCleanOkLo` | 0.0 | ASR / clean correct (%), G1+G2s -, qwen3.8-27b, lower 95% CI bound |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrCleanOkHi` | 1.6 | ASR / clean correct (%), G1+G2s -, qwen3.8-27b, upper 95% CI bound |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrCleanOkCI` | [0.0, 1.6] | ASR / clean correct (%), G1+G2s -, qwen3.8-27b, 95% CI |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrCleanOkN` | 223 | ASR / clean correct (%), G1+G2s -, qwen3.8-27b, n |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBAsrCleanOkP` | n/a | ASR / clean correct (%), G1+G2s -, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBNonTargetAcc` | 94.0 | non-target accuracy (%), G1+G2s -, qwen3.8-27b |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBNonTargetAccLo` | 91.6 | non-target accuracy (%), G1+G2s -, qwen3.8-27b, lower 95% CI bound |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBNonTargetAccHi` | 96.4 | non-target accuracy (%), G1+G2s -, qwen3.8-27b, upper 95% CI bound |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBNonTargetAccCI` | [91.6, 96.4] | non-target accuracy (%), G1+G2s -, qwen3.8-27b, 95% CI |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBNonTargetAccN` | 940 | non-target accuracy (%), G1+G2s -, qwen3.8-27b, n |
| `\PfourGOnePlusGTwoSQwenThreeEightTwoSevenBNonTargetAccP` | n/a | non-target accuracy (%), G1+G2s -, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsr` | 0.9 | ASR (%), G1+G2s -, gemma-4-31b-it |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrLo` | 0.0 | ASR (%), G1+G2s -, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrHi` | 2.2 | ASR (%), G1+G2s -, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrCI` | [0.0, 2.2] | ASR (%), G1+G2s -, gemma-4-31b-it, 95% CI |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrN` | 233 | ASR (%), G1+G2s -, gemma-4-31b-it, n |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrP` | n/a | ASR (%), G1+G2s -, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrDropped` | 0.9 | ASR (%) unparsed dropped, G1+G2s -, gemma-4-31b-it |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrDroppedLo` | 0.0 | ASR (%) unparsed dropped, G1+G2s -, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrDroppedHi` | 2.2 | ASR (%) unparsed dropped, G1+G2s -, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrDroppedCI` | [0.0, 2.2] | ASR (%) unparsed dropped, G1+G2s -, gemma-4-31b-it, 95% CI |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrDroppedN` | 231 | ASR (%) unparsed dropped, G1+G2s -, gemma-4-31b-it, n |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1+G2s -, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrCleanOk` | 0.4 | ASR / clean correct (%), G1+G2s -, gemma-4-31b-it |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrCleanOkLo` | 0.0 | ASR / clean correct (%), G1+G2s -, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrCleanOkHi` | 1.4 | ASR / clean correct (%), G1+G2s -, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrCleanOkCI` | [0.0, 1.4] | ASR / clean correct (%), G1+G2s -, gemma-4-31b-it, 95% CI |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrCleanOkN` | 223 | ASR / clean correct (%), G1+G2s -, gemma-4-31b-it, n |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBAsrCleanOkP` | n/a | ASR / clean correct (%), G1+G2s -, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBNonTargetAcc` | 98.7 | non-target accuracy (%), G1+G2s -, gemma-4-31b-it |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBNonTargetAccLo` | 97.0 | non-target accuracy (%), G1+G2s -, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBNonTargetAccHi` | 100.0 | non-target accuracy (%), G1+G2s -, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBNonTargetAccCI` | [97.0, 100.0] | non-target accuracy (%), G1+G2s -, gemma-4-31b-it, 95% CI |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBNonTargetAccN` | 924 | non-target accuracy (%), G1+G2s -, gemma-4-31b-it, n |
| `\PfourGOnePlusGTwoSGemmaFourThreeOneBNonTargetAccP` | n/a | non-target accuracy (%), G1+G2s -, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsr` | 0.0 | ASR (%), G1+G2s -, glm-5.3-flash |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrLo` | 0.0 | ASR (%), G1+G2s -, glm-5.3-flash, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrHi` | 1.6 | ASR (%), G1+G2s -, glm-5.3-flash, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrCI` | [0.0, 1.6] | ASR (%), G1+G2s -, glm-5.3-flash, 95% CI |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrN` | 235 | ASR (%), G1+G2s -, glm-5.3-flash, n |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrP` | n/a | ASR (%), G1+G2s -, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrDropped` | 0.0 | ASR (%) unparsed dropped, G1+G2s -, glm-5.3-flash |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrDroppedLo` | 0.0 | ASR (%) unparsed dropped, G1+G2s -, glm-5.3-flash, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrDroppedHi` | 1.6 | ASR (%) unparsed dropped, G1+G2s -, glm-5.3-flash, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrDroppedCI` | [0.0, 1.6] | ASR (%) unparsed dropped, G1+G2s -, glm-5.3-flash, 95% CI |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrDroppedN` | 235 | ASR (%) unparsed dropped, G1+G2s -, glm-5.3-flash, n |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1+G2s -, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrCleanOk` | 0.0 | ASR / clean correct (%), G1+G2s -, glm-5.3-flash |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrCleanOkLo` | 0.0 | ASR / clean correct (%), G1+G2s -, glm-5.3-flash, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrCleanOkHi` | 1.6 | ASR / clean correct (%), G1+G2s -, glm-5.3-flash, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrCleanOkCI` | [0.0, 1.6] | ASR / clean correct (%), G1+G2s -, glm-5.3-flash, 95% CI |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrCleanOkN` | 235 | ASR / clean correct (%), G1+G2s -, glm-5.3-flash, n |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashAsrCleanOkP` | n/a | ASR / clean correct (%), G1+G2s -, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashNonTargetAcc` | 99.8 | non-target accuracy (%), G1+G2s -, glm-5.3-flash |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashNonTargetAccLo` | 99.4 | non-target accuracy (%), G1+G2s -, glm-5.3-flash, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashNonTargetAccHi` | 100.0 | non-target accuracy (%), G1+G2s -, glm-5.3-flash, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashNonTargetAccCI` | [99.4, 100.0] | non-target accuracy (%), G1+G2s -, glm-5.3-flash, 95% CI |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashNonTargetAccN` | 940 | non-target accuracy (%), G1+G2s -, glm-5.3-flash, n |
| `\PfourGOnePlusGTwoSGLMFiveThreeFlashNonTargetAccP` | n/a | non-target accuracy (%), G1+G2s -, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsr` | 0.0 | ASR (%), G1+G2s -, glm-5.2 |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrLo` | 0.0 | ASR (%), G1+G2s -, glm-5.2, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrHi` | 1.6 | ASR (%), G1+G2s -, glm-5.2, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrCI` | [0.0, 1.6] | ASR (%), G1+G2s -, glm-5.2, 95% CI |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrN` | 235 | ASR (%), G1+G2s -, glm-5.2, n |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrP` | n/a | ASR (%), G1+G2s -, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrDropped` | 0.0 | ASR (%) unparsed dropped, G1+G2s -, glm-5.2 |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrDroppedLo` | 0.0 | ASR (%) unparsed dropped, G1+G2s -, glm-5.2, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrDroppedHi` | 1.6 | ASR (%) unparsed dropped, G1+G2s -, glm-5.2, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrDroppedCI` | [0.0, 1.6] | ASR (%) unparsed dropped, G1+G2s -, glm-5.2, 95% CI |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrDroppedN` | 235 | ASR (%) unparsed dropped, G1+G2s -, glm-5.2, n |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrDroppedP` | n/a | ASR (%) unparsed dropped, G1+G2s -, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrCleanOk` | 0.0 | ASR / clean correct (%), G1+G2s -, glm-5.2 |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrCleanOkLo` | 0.0 | ASR / clean correct (%), G1+G2s -, glm-5.2, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrCleanOkHi` | 1.6 | ASR / clean correct (%), G1+G2s -, glm-5.2, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrCleanOkCI` | [0.0, 1.6] | ASR / clean correct (%), G1+G2s -, glm-5.2, 95% CI |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrCleanOkN` | 231 | ASR / clean correct (%), G1+G2s -, glm-5.2, n |
| `\PfourGOnePlusGTwoSGLMFiveTwoAsrCleanOkP` | n/a | ASR / clean correct (%), G1+G2s -, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSGLMFiveTwoNonTargetAcc` | 98.6 | non-target accuracy (%), G1+G2s -, glm-5.2 |
| `\PfourGOnePlusGTwoSGLMFiveTwoNonTargetAccLo` | 96.9 | non-target accuracy (%), G1+G2s -, glm-5.2, lower 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveTwoNonTargetAccHi` | 99.9 | non-target accuracy (%), G1+G2s -, glm-5.2, upper 95% CI bound |
| `\PfourGOnePlusGTwoSGLMFiveTwoNonTargetAccCI` | [96.9, 99.9] | non-target accuracy (%), G1+G2s -, glm-5.2, 95% CI |
| `\PfourGOnePlusGTwoSGLMFiveTwoNonTargetAccN` | 940 | non-target accuracy (%), G1+G2s -, glm-5.2, n |
| `\PfourGOnePlusGTwoSGLMFiveTwoNonTargetAccP` | n/a | non-target accuracy (%), G1+G2s -, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePooledCleanAcc` | 98.2 | clean-store accuracy (%), G1, pooled |
| `\PfourGOnePooledCleanAccLo` | 97.1 | clean-store accuracy (%), G1, pooled, lower 95% CI bound |
| `\PfourGOnePooledCleanAccHi` | 99.0 | clean-store accuracy (%), G1, pooled, upper 95% CI bound |
| `\PfourGOnePooledCleanAccCI` | [97.1, 99.0] | clean-store accuracy (%), G1, pooled, 95% CI |
| `\PfourGOnePooledCleanAccN` | 1{,}150 | clean-store accuracy (%), G1, pooled, n |
| `\PfourGOnePooledCleanAccP` | n/a | clean-store accuracy (%), G1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePooledFpCost` | \ensuremath{-}0.1 | clean accuracy change vs none (pp), G1, pooled |
| `\PfourGOnePooledFpCostLo` | \ensuremath{-}0.3 | clean accuracy change vs none (pp), G1, pooled, lower 95% CI bound |
| `\PfourGOnePooledFpCostHi` | 0.0 | clean accuracy change vs none (pp), G1, pooled, upper 95% CI bound |
| `\PfourGOnePooledFpCostCI` | [\ensuremath{-}0.3, 0.0] | clean accuracy change vs none (pp), G1, pooled, 95% CI |
| `\PfourGOnePooledFpCostN` | 1{,}145 | clean accuracy change vs none (pp), G1, pooled, n |
| `\PfourGOnePooledFpCostP` | 0.723 | clean accuracy change vs none (pp), G1, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneDeepSeekVFourFlashCleanAcc` | 99.6 | clean-store accuracy (%), G1, deepseek-v4-flash |
| `\PfourGOneDeepSeekVFourFlashCleanAccLo` | 98.7 | clean-store accuracy (%), G1, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGOneDeepSeekVFourFlashCleanAccHi` | 100.0 | clean-store accuracy (%), G1, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGOneDeepSeekVFourFlashCleanAccCI` | [98.7, 100.0] | clean-store accuracy (%), G1, deepseek-v4-flash, 95% CI |
| `\PfourGOneDeepSeekVFourFlashCleanAccN` | 235 | clean-store accuracy (%), G1, deepseek-v4-flash, n |
| `\PfourGOneDeepSeekVFourFlashCleanAccP` | n/a | clean-store accuracy (%), G1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneDeepSeekVFourFlashFpCost` | 0.0 | clean accuracy change vs none (pp), G1, deepseek-v4-flash |
| `\PfourGOneDeepSeekVFourFlashFpCostLo` | 0.0 | clean accuracy change vs none (pp), G1, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGOneDeepSeekVFourFlashFpCostHi` | 0.0 | clean accuracy change vs none (pp), G1, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGOneDeepSeekVFourFlashFpCostCI` | [0.0, 0.0] | clean accuracy change vs none (pp), G1, deepseek-v4-flash, 95% CI |
| `\PfourGOneDeepSeekVFourFlashFpCostN` | 235 | clean accuracy change vs none (pp), G1, deepseek-v4-flash, n |
| `\PfourGOneDeepSeekVFourFlashFpCostP` | 1.000 | clean accuracy change vs none (pp), G1, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneQwenThreeEightTwoSevenBCleanAcc` | 94.3 | clean-store accuracy (%), G1, qwen3.8-27b |
| `\PfourGOneQwenThreeEightTwoSevenBCleanAccLo` | 91.3 | clean-store accuracy (%), G1, qwen3.8-27b, lower 95% CI bound |
| `\PfourGOneQwenThreeEightTwoSevenBCleanAccHi` | 97.4 | clean-store accuracy (%), G1, qwen3.8-27b, upper 95% CI bound |
| `\PfourGOneQwenThreeEightTwoSevenBCleanAccCI` | [91.3, 97.4] | clean-store accuracy (%), G1, qwen3.8-27b, 95% CI |
| `\PfourGOneQwenThreeEightTwoSevenBCleanAccN` | 230 | clean-store accuracy (%), G1, qwen3.8-27b, n |
| `\PfourGOneQwenThreeEightTwoSevenBCleanAccP` | n/a | clean-store accuracy (%), G1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneQwenThreeEightTwoSevenBFpCost` | \ensuremath{-}0.4 | clean accuracy change vs none (pp), G1, qwen3.8-27b |
| `\PfourGOneQwenThreeEightTwoSevenBFpCostLo` | \ensuremath{-}1.3 | clean accuracy change vs none (pp), G1, qwen3.8-27b, lower 95% CI bound |
| `\PfourGOneQwenThreeEightTwoSevenBFpCostHi` | 0.0 | clean accuracy change vs none (pp), G1, qwen3.8-27b, upper 95% CI bound |
| `\PfourGOneQwenThreeEightTwoSevenBFpCostCI` | [\ensuremath{-}1.3, 0.0] | clean accuracy change vs none (pp), G1, qwen3.8-27b, 95% CI |
| `\PfourGOneQwenThreeEightTwoSevenBFpCostN` | 230 | clean accuracy change vs none (pp), G1, qwen3.8-27b, n |
| `\PfourGOneQwenThreeEightTwoSevenBFpCostP` | 0.702 | clean accuracy change vs none (pp), G1, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneGemmaFourThreeOneBCleanAcc` | 98.6 | clean-store accuracy (%), G1, gemma-4-31b-it |
| `\PfourGOneGemmaFourThreeOneBCleanAccLo` | 96.3 | clean-store accuracy (%), G1, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGOneGemmaFourThreeOneBCleanAccHi` | 100.0 | clean-store accuracy (%), G1, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGOneGemmaFourThreeOneBCleanAccCI` | [96.3, 100.0] | clean-store accuracy (%), G1, gemma-4-31b-it, 95% CI |
| `\PfourGOneGemmaFourThreeOneBCleanAccN` | 215 | clean-store accuracy (%), G1, gemma-4-31b-it, n |
| `\PfourGOneGemmaFourThreeOneBCleanAccP` | n/a | clean-store accuracy (%), G1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneGemmaFourThreeOneBFpCost` | 0.0 | clean accuracy change vs none (pp), G1, gemma-4-31b-it |
| `\PfourGOneGemmaFourThreeOneBFpCostLo` | 0.0 | clean accuracy change vs none (pp), G1, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGOneGemmaFourThreeOneBFpCostHi` | 0.0 | clean accuracy change vs none (pp), G1, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGOneGemmaFourThreeOneBFpCostCI` | [0.0, 0.0] | clean accuracy change vs none (pp), G1, gemma-4-31b-it, 95% CI |
| `\PfourGOneGemmaFourThreeOneBFpCostN` | 210 | clean accuracy change vs none (pp), G1, gemma-4-31b-it, n |
| `\PfourGOneGemmaFourThreeOneBFpCostP` | 1.000 | clean accuracy change vs none (pp), G1, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneGLMFiveThreeFlashCleanAcc` | 100.0 | clean-store accuracy (%), G1, glm-5.3-flash |
| `\PfourGOneGLMFiveThreeFlashCleanAccLo` | 98.4 | clean-store accuracy (%), G1, glm-5.3-flash, lower 95% CI bound |
| `\PfourGOneGLMFiveThreeFlashCleanAccHi` | 100.0 | clean-store accuracy (%), G1, glm-5.3-flash, upper 95% CI bound |
| `\PfourGOneGLMFiveThreeFlashCleanAccCI` | [98.4, 100.0] | clean-store accuracy (%), G1, glm-5.3-flash, 95% CI |
| `\PfourGOneGLMFiveThreeFlashCleanAccN` | 235 | clean-store accuracy (%), G1, glm-5.3-flash, n |
| `\PfourGOneGLMFiveThreeFlashCleanAccP` | n/a | clean-store accuracy (%), G1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneGLMFiveThreeFlashFpCost` | 0.0 | clean accuracy change vs none (pp), G1, glm-5.3-flash |
| `\PfourGOneGLMFiveThreeFlashFpCostLo` | 0.0 | clean accuracy change vs none (pp), G1, glm-5.3-flash, lower 95% CI bound |
| `\PfourGOneGLMFiveThreeFlashFpCostHi` | 0.0 | clean accuracy change vs none (pp), G1, glm-5.3-flash, upper 95% CI bound |
| `\PfourGOneGLMFiveThreeFlashFpCostCI` | [0.0, 0.0] | clean accuracy change vs none (pp), G1, glm-5.3-flash, 95% CI |
| `\PfourGOneGLMFiveThreeFlashFpCostN` | 235 | clean accuracy change vs none (pp), G1, glm-5.3-flash, n |
| `\PfourGOneGLMFiveThreeFlashFpCostP` | 1.000 | clean accuracy change vs none (pp), G1, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneGLMFiveTwoCleanAcc` | 98.3 | clean-store accuracy (%), G1, glm-5.2 |
| `\PfourGOneGLMFiveTwoCleanAccLo` | 96.6 | clean-store accuracy (%), G1, glm-5.2, lower 95% CI bound |
| `\PfourGOneGLMFiveTwoCleanAccHi` | 99.6 | clean-store accuracy (%), G1, glm-5.2, upper 95% CI bound |
| `\PfourGOneGLMFiveTwoCleanAccCI` | [96.6, 99.6] | clean-store accuracy (%), G1, glm-5.2, 95% CI |
| `\PfourGOneGLMFiveTwoCleanAccN` | 235 | clean-store accuracy (%), G1, glm-5.2, n |
| `\PfourGOneGLMFiveTwoCleanAccP` | n/a | clean-store accuracy (%), G1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneGLMFiveTwoFpCost` | 0.0 | clean accuracy change vs none (pp), G1, glm-5.2 |
| `\PfourGOneGLMFiveTwoFpCostLo` | 0.0 | clean accuracy change vs none (pp), G1, glm-5.2, lower 95% CI bound |
| `\PfourGOneGLMFiveTwoFpCostHi` | 0.0 | clean accuracy change vs none (pp), G1, glm-5.2, upper 95% CI bound |
| `\PfourGOneGLMFiveTwoFpCostCI` | [0.0, 0.0] | clean accuracy change vs none (pp), G1, glm-5.2, 95% CI |
| `\PfourGOneGLMFiveTwoFpCostN` | 235 | clean accuracy change vs none (pp), G1, glm-5.2, n |
| `\PfourGOneGLMFiveTwoFpCostP` | 1.000 | clean accuracy change vs none (pp), G1, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSPooledCleanAcc` | 98.0 | clean-store accuracy (%), G2s, pooled |
| `\PfourGTwoSPooledCleanAccLo` | 96.9 | clean-store accuracy (%), G2s, pooled, lower 95% CI bound |
| `\PfourGTwoSPooledCleanAccHi` | 98.9 | clean-store accuracy (%), G2s, pooled, upper 95% CI bound |
| `\PfourGTwoSPooledCleanAccCI` | [96.9, 98.9] | clean-store accuracy (%), G2s, pooled, 95% CI |
| `\PfourGTwoSPooledCleanAccN` | 1{,}170 | clean-store accuracy (%), G2s, pooled, n |
| `\PfourGTwoSPooledCleanAccP` | n/a | clean-store accuracy (%), G2s, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSPooledFpCost` | \ensuremath{-}0.2 | clean accuracy change vs none (pp), G2s, pooled |
| `\PfourGTwoSPooledFpCostLo` | \ensuremath{-}0.5 | clean accuracy change vs none (pp), G2s, pooled, lower 95% CI bound |
| `\PfourGTwoSPooledFpCostHi` | 0.2 | clean accuracy change vs none (pp), G2s, pooled, upper 95% CI bound |
| `\PfourGTwoSPooledFpCostCI` | [\ensuremath{-}0.5, 0.2] | clean accuracy change vs none (pp), G2s, pooled, 95% CI |
| `\PfourGTwoSPooledFpCostN` | 1{,}165 | clean accuracy change vs none (pp), G2s, pooled, n |
| `\PfourGTwoSPooledFpCostP` | 0.443 | clean accuracy change vs none (pp), G2s, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSDeepSeekVFourFlashCleanAcc` | 99.1 | clean-store accuracy (%), G2s, deepseek-v4-flash |
| `\PfourGTwoSDeepSeekVFourFlashCleanAccLo` | 97.9 | clean-store accuracy (%), G2s, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoSDeepSeekVFourFlashCleanAccHi` | 100.0 | clean-store accuracy (%), G2s, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoSDeepSeekVFourFlashCleanAccCI` | [97.9, 100.0] | clean-store accuracy (%), G2s, deepseek-v4-flash, 95% CI |
| `\PfourGTwoSDeepSeekVFourFlashCleanAccN` | 235 | clean-store accuracy (%), G2s, deepseek-v4-flash, n |
| `\PfourGTwoSDeepSeekVFourFlashCleanAccP` | n/a | clean-store accuracy (%), G2s, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSDeepSeekVFourFlashFpCost` | \ensuremath{-}0.4 | clean accuracy change vs none (pp), G2s, deepseek-v4-flash |
| `\PfourGTwoSDeepSeekVFourFlashFpCostLo` | \ensuremath{-}1.3 | clean accuracy change vs none (pp), G2s, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoSDeepSeekVFourFlashFpCostHi` | 0.0 | clean accuracy change vs none (pp), G2s, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoSDeepSeekVFourFlashFpCostCI` | [\ensuremath{-}1.3, 0.0] | clean accuracy change vs none (pp), G2s, deepseek-v4-flash, 95% CI |
| `\PfourGTwoSDeepSeekVFourFlashFpCostN` | 235 | clean accuracy change vs none (pp), G2s, deepseek-v4-flash, n |
| `\PfourGTwoSDeepSeekVFourFlashFpCostP` | 0.723 | clean accuracy change vs none (pp), G2s, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSQwenThreeEightTwoSevenBCleanAcc` | 94.0 | clean-store accuracy (%), G2s, qwen3.8-27b |
| `\PfourGTwoSQwenThreeEightTwoSevenBCleanAccLo` | 91.5 | clean-store accuracy (%), G2s, qwen3.8-27b, lower 95% CI bound |
| `\PfourGTwoSQwenThreeEightTwoSevenBCleanAccHi` | 96.6 | clean-store accuracy (%), G2s, qwen3.8-27b, upper 95% CI bound |
| `\PfourGTwoSQwenThreeEightTwoSevenBCleanAccCI` | [91.5, 96.6] | clean-store accuracy (%), G2s, qwen3.8-27b, 95% CI |
| `\PfourGTwoSQwenThreeEightTwoSevenBCleanAccN` | 235 | clean-store accuracy (%), G2s, qwen3.8-27b, n |
| `\PfourGTwoSQwenThreeEightTwoSevenBCleanAccP` | n/a | clean-store accuracy (%), G2s, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSQwenThreeEightTwoSevenBFpCost` | \ensuremath{-}0.9 | clean accuracy change vs none (pp), G2s, qwen3.8-27b |
| `\PfourGTwoSQwenThreeEightTwoSevenBFpCostLo` | \ensuremath{-}2.1 | clean accuracy change vs none (pp), G2s, qwen3.8-27b, lower 95% CI bound |
| `\PfourGTwoSQwenThreeEightTwoSevenBFpCostHi` | 0.0 | clean accuracy change vs none (pp), G2s, qwen3.8-27b, upper 95% CI bound |
| `\PfourGTwoSQwenThreeEightTwoSevenBFpCostCI` | [\ensuremath{-}2.1, 0.0] | clean accuracy change vs none (pp), G2s, qwen3.8-27b, 95% CI |
| `\PfourGTwoSQwenThreeEightTwoSevenBFpCostN` | 235 | clean accuracy change vs none (pp), G2s, qwen3.8-27b, n |
| `\PfourGTwoSQwenThreeEightTwoSevenBFpCostP` | 0.260 | clean accuracy change vs none (pp), G2s, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSGemmaFourThreeOneBCleanAcc` | 98.7 | clean-store accuracy (%), G2s, gemma-4-31b-it |
| `\PfourGTwoSGemmaFourThreeOneBCleanAccLo` | 97.4 | clean-store accuracy (%), G2s, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoSGemmaFourThreeOneBCleanAccHi` | 100.0 | clean-store accuracy (%), G2s, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoSGemmaFourThreeOneBCleanAccCI` | [97.4, 100.0] | clean-store accuracy (%), G2s, gemma-4-31b-it, 95% CI |
| `\PfourGTwoSGemmaFourThreeOneBCleanAccN` | 230 | clean-store accuracy (%), G2s, gemma-4-31b-it, n |
| `\PfourGTwoSGemmaFourThreeOneBCleanAccP` | n/a | clean-store accuracy (%), G2s, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSGemmaFourThreeOneBFpCost` | 0.4 | clean accuracy change vs none (pp), G2s, gemma-4-31b-it |
| `\PfourGTwoSGemmaFourThreeOneBFpCostLo` | 0.0 | clean accuracy change vs none (pp), G2s, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoSGemmaFourThreeOneBFpCostHi` | 1.3 | clean accuracy change vs none (pp), G2s, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoSGemmaFourThreeOneBFpCostCI` | [0.0, 1.3] | clean accuracy change vs none (pp), G2s, gemma-4-31b-it, 95% CI |
| `\PfourGTwoSGemmaFourThreeOneBFpCostN` | 225 | clean accuracy change vs none (pp), G2s, gemma-4-31b-it, n |
| `\PfourGTwoSGemmaFourThreeOneBFpCostP` | 0.728 | clean accuracy change vs none (pp), G2s, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSGLMFiveThreeFlashCleanAcc` | 99.6 | clean-store accuracy (%), G2s, glm-5.3-flash |
| `\PfourGTwoSGLMFiveThreeFlashCleanAccLo` | 98.7 | clean-store accuracy (%), G2s, glm-5.3-flash, lower 95% CI bound |
| `\PfourGTwoSGLMFiveThreeFlashCleanAccHi` | 100.0 | clean-store accuracy (%), G2s, glm-5.3-flash, upper 95% CI bound |
| `\PfourGTwoSGLMFiveThreeFlashCleanAccCI` | [98.7, 100.0] | clean-store accuracy (%), G2s, glm-5.3-flash, 95% CI |
| `\PfourGTwoSGLMFiveThreeFlashCleanAccN` | 235 | clean-store accuracy (%), G2s, glm-5.3-flash, n |
| `\PfourGTwoSGLMFiveThreeFlashCleanAccP` | n/a | clean-store accuracy (%), G2s, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSGLMFiveThreeFlashFpCost` | \ensuremath{-}0.4 | clean accuracy change vs none (pp), G2s, glm-5.3-flash |
| `\PfourGTwoSGLMFiveThreeFlashFpCostLo` | \ensuremath{-}1.3 | clean accuracy change vs none (pp), G2s, glm-5.3-flash, lower 95% CI bound |
| `\PfourGTwoSGLMFiveThreeFlashFpCostHi` | 0.0 | clean accuracy change vs none (pp), G2s, glm-5.3-flash, upper 95% CI bound |
| `\PfourGTwoSGLMFiveThreeFlashFpCostCI` | [\ensuremath{-}1.3, 0.0] | clean accuracy change vs none (pp), G2s, glm-5.3-flash, 95% CI |
| `\PfourGTwoSGLMFiveThreeFlashFpCostN` | 235 | clean accuracy change vs none (pp), G2s, glm-5.3-flash, n |
| `\PfourGTwoSGLMFiveThreeFlashFpCostP` | 0.720 | clean accuracy change vs none (pp), G2s, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSGLMFiveTwoCleanAcc` | 98.7 | clean-store accuracy (%), G2s, glm-5.2 |
| `\PfourGTwoSGLMFiveTwoCleanAccLo` | 97.0 | clean-store accuracy (%), G2s, glm-5.2, lower 95% CI bound |
| `\PfourGTwoSGLMFiveTwoCleanAccHi` | 100.0 | clean-store accuracy (%), G2s, glm-5.2, upper 95% CI bound |
| `\PfourGTwoSGLMFiveTwoCleanAccCI` | [97.0, 100.0] | clean-store accuracy (%), G2s, glm-5.2, 95% CI |
| `\PfourGTwoSGLMFiveTwoCleanAccN` | 235 | clean-store accuracy (%), G2s, glm-5.2, n |
| `\PfourGTwoSGLMFiveTwoCleanAccP` | n/a | clean-store accuracy (%), G2s, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSGLMFiveTwoFpCost` | 0.4 | clean accuracy change vs none (pp), G2s, glm-5.2 |
| `\PfourGTwoSGLMFiveTwoFpCostLo` | 0.0 | clean accuracy change vs none (pp), G2s, glm-5.2, lower 95% CI bound |
| `\PfourGTwoSGLMFiveTwoFpCostHi` | 1.3 | clean accuracy change vs none (pp), G2s, glm-5.2, upper 95% CI bound |
| `\PfourGTwoSGLMFiveTwoFpCostCI` | [0.0, 1.3] | clean accuracy change vs none (pp), G2s, glm-5.2, 95% CI |
| `\PfourGTwoSGLMFiveTwoFpCostN` | 235 | clean accuracy change vs none (pp), G2s, glm-5.2, n |
| `\PfourGTwoSGLMFiveTwoFpCostP` | 0.732 | clean accuracy change vs none (pp), G2s, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUPooledCleanAcc` | 98.4 | clean-store accuracy (%), G2u, pooled |
| `\PfourGTwoUPooledCleanAccLo` | 97.6 | clean-store accuracy (%), G2u, pooled, lower 95% CI bound |
| `\PfourGTwoUPooledCleanAccHi` | 99.1 | clean-store accuracy (%), G2u, pooled, upper 95% CI bound |
| `\PfourGTwoUPooledCleanAccCI` | [97.6, 99.1] | clean-store accuracy (%), G2u, pooled, 95% CI |
| `\PfourGTwoUPooledCleanAccN` | 1{,}175 | clean-store accuracy (%), G2u, pooled, n |
| `\PfourGTwoUPooledCleanAccP` | n/a | clean-store accuracy (%), G2u, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUPooledFpCost` | 0.2 | clean accuracy change vs none (pp), G2u, pooled |
| `\PfourGTwoUPooledFpCostLo` | \ensuremath{-}0.2 | clean accuracy change vs none (pp), G2u, pooled, lower 95% CI bound |
| `\PfourGTwoUPooledFpCostHi` | 0.6 | clean accuracy change vs none (pp), G2u, pooled, upper 95% CI bound |
| `\PfourGTwoUPooledFpCostCI` | [\ensuremath{-}0.2, 0.6] | clean accuracy change vs none (pp), G2u, pooled, 95% CI |
| `\PfourGTwoUPooledFpCostN` | 1{,}170 | clean accuracy change vs none (pp), G2u, pooled, n |
| `\PfourGTwoUPooledFpCostP` | 0.566 | clean accuracy change vs none (pp), G2u, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUDeepSeekVFourFlashCleanAcc` | 100.0 | clean-store accuracy (%), G2u, deepseek-v4-flash |
| `\PfourGTwoUDeepSeekVFourFlashCleanAccLo` | 98.4 | clean-store accuracy (%), G2u, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoUDeepSeekVFourFlashCleanAccHi` | 100.0 | clean-store accuracy (%), G2u, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoUDeepSeekVFourFlashCleanAccCI` | [98.4, 100.0] | clean-store accuracy (%), G2u, deepseek-v4-flash, 95% CI |
| `\PfourGTwoUDeepSeekVFourFlashCleanAccN` | 235 | clean-store accuracy (%), G2u, deepseek-v4-flash, n |
| `\PfourGTwoUDeepSeekVFourFlashCleanAccP` | n/a | clean-store accuracy (%), G2u, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUDeepSeekVFourFlashFpCost` | 0.4 | clean accuracy change vs none (pp), G2u, deepseek-v4-flash |
| `\PfourGTwoUDeepSeekVFourFlashFpCostLo` | 0.0 | clean accuracy change vs none (pp), G2u, deepseek-v4-flash, lower 95% CI bound |
| `\PfourGTwoUDeepSeekVFourFlashFpCostHi` | 1.3 | clean accuracy change vs none (pp), G2u, deepseek-v4-flash, upper 95% CI bound |
| `\PfourGTwoUDeepSeekVFourFlashFpCostCI` | [0.0, 1.3] | clean accuracy change vs none (pp), G2u, deepseek-v4-flash, 95% CI |
| `\PfourGTwoUDeepSeekVFourFlashFpCostN` | 235 | clean accuracy change vs none (pp), G2u, deepseek-v4-flash, n |
| `\PfourGTwoUDeepSeekVFourFlashFpCostP` | 0.721 | clean accuracy change vs none (pp), G2u, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUQwenThreeEightTwoSevenBCleanAcc` | 94.9 | clean-store accuracy (%), G2u, qwen3.8-27b |
| `\PfourGTwoUQwenThreeEightTwoSevenBCleanAccLo` | 92.3 | clean-store accuracy (%), G2u, qwen3.8-27b, lower 95% CI bound |
| `\PfourGTwoUQwenThreeEightTwoSevenBCleanAccHi` | 97.0 | clean-store accuracy (%), G2u, qwen3.8-27b, upper 95% CI bound |
| `\PfourGTwoUQwenThreeEightTwoSevenBCleanAccCI` | [92.3, 97.0] | clean-store accuracy (%), G2u, qwen3.8-27b, 95% CI |
| `\PfourGTwoUQwenThreeEightTwoSevenBCleanAccN` | 235 | clean-store accuracy (%), G2u, qwen3.8-27b, n |
| `\PfourGTwoUQwenThreeEightTwoSevenBCleanAccP` | n/a | clean-store accuracy (%), G2u, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUQwenThreeEightTwoSevenBFpCost` | 0.0 | clean accuracy change vs none (pp), G2u, qwen3.8-27b |
| `\PfourGTwoUQwenThreeEightTwoSevenBFpCostLo` | \ensuremath{-}1.3 | clean accuracy change vs none (pp), G2u, qwen3.8-27b, lower 95% CI bound |
| `\PfourGTwoUQwenThreeEightTwoSevenBFpCostHi` | 1.3 | clean accuracy change vs none (pp), G2u, qwen3.8-27b, upper 95% CI bound |
| `\PfourGTwoUQwenThreeEightTwoSevenBFpCostCI` | [\ensuremath{-}1.3, 1.3] | clean accuracy change vs none (pp), G2u, qwen3.8-27b, 95% CI |
| `\PfourGTwoUQwenThreeEightTwoSevenBFpCostN` | 235 | clean accuracy change vs none (pp), G2u, qwen3.8-27b, n |
| `\PfourGTwoUQwenThreeEightTwoSevenBFpCostP` | 1.000 | clean accuracy change vs none (pp), G2u, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUGemmaFourThreeOneBCleanAcc` | 98.7 | clean-store accuracy (%), G2u, gemma-4-31b-it |
| `\PfourGTwoUGemmaFourThreeOneBCleanAccLo` | 97.4 | clean-store accuracy (%), G2u, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoUGemmaFourThreeOneBCleanAccHi` | 100.0 | clean-store accuracy (%), G2u, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoUGemmaFourThreeOneBCleanAccCI` | [97.4, 100.0] | clean-store accuracy (%), G2u, gemma-4-31b-it, 95% CI |
| `\PfourGTwoUGemmaFourThreeOneBCleanAccN` | 235 | clean-store accuracy (%), G2u, gemma-4-31b-it, n |
| `\PfourGTwoUGemmaFourThreeOneBCleanAccP` | n/a | clean-store accuracy (%), G2u, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUGemmaFourThreeOneBFpCost` | 0.4 | clean accuracy change vs none (pp), G2u, gemma-4-31b-it |
| `\PfourGTwoUGemmaFourThreeOneBFpCostLo` | 0.0 | clean accuracy change vs none (pp), G2u, gemma-4-31b-it, lower 95% CI bound |
| `\PfourGTwoUGemmaFourThreeOneBFpCostHi` | 1.3 | clean accuracy change vs none (pp), G2u, gemma-4-31b-it, upper 95% CI bound |
| `\PfourGTwoUGemmaFourThreeOneBFpCostCI` | [0.0, 1.3] | clean accuracy change vs none (pp), G2u, gemma-4-31b-it, 95% CI |
| `\PfourGTwoUGemmaFourThreeOneBFpCostN` | 230 | clean accuracy change vs none (pp), G2u, gemma-4-31b-it, n |
| `\PfourGTwoUGemmaFourThreeOneBFpCostP` | 0.752 | clean accuracy change vs none (pp), G2u, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUGLMFiveThreeFlashCleanAcc` | 99.6 | clean-store accuracy (%), G2u, glm-5.3-flash |
| `\PfourGTwoUGLMFiveThreeFlashCleanAccLo` | 98.7 | clean-store accuracy (%), G2u, glm-5.3-flash, lower 95% CI bound |
| `\PfourGTwoUGLMFiveThreeFlashCleanAccHi` | 100.0 | clean-store accuracy (%), G2u, glm-5.3-flash, upper 95% CI bound |
| `\PfourGTwoUGLMFiveThreeFlashCleanAccCI` | [98.7, 100.0] | clean-store accuracy (%), G2u, glm-5.3-flash, 95% CI |
| `\PfourGTwoUGLMFiveThreeFlashCleanAccN` | 235 | clean-store accuracy (%), G2u, glm-5.3-flash, n |
| `\PfourGTwoUGLMFiveThreeFlashCleanAccP` | n/a | clean-store accuracy (%), G2u, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUGLMFiveThreeFlashFpCost` | \ensuremath{-}0.4 | clean accuracy change vs none (pp), G2u, glm-5.3-flash |
| `\PfourGTwoUGLMFiveThreeFlashFpCostLo` | \ensuremath{-}1.3 | clean accuracy change vs none (pp), G2u, glm-5.3-flash, lower 95% CI bound |
| `\PfourGTwoUGLMFiveThreeFlashFpCostHi` | 0.0 | clean accuracy change vs none (pp), G2u, glm-5.3-flash, upper 95% CI bound |
| `\PfourGTwoUGLMFiveThreeFlashFpCostCI` | [\ensuremath{-}1.3, 0.0] | clean accuracy change vs none (pp), G2u, glm-5.3-flash, 95% CI |
| `\PfourGTwoUGLMFiveThreeFlashFpCostN` | 235 | clean accuracy change vs none (pp), G2u, glm-5.3-flash, n |
| `\PfourGTwoUGLMFiveThreeFlashFpCostP` | 0.700 | clean accuracy change vs none (pp), G2u, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUGLMFiveTwoCleanAcc` | 98.7 | clean-store accuracy (%), G2u, glm-5.2 |
| `\PfourGTwoUGLMFiveTwoCleanAccLo` | 97.0 | clean-store accuracy (%), G2u, glm-5.2, lower 95% CI bound |
| `\PfourGTwoUGLMFiveTwoCleanAccHi` | 100.0 | clean-store accuracy (%), G2u, glm-5.2, upper 95% CI bound |
| `\PfourGTwoUGLMFiveTwoCleanAccCI` | [97.0, 100.0] | clean-store accuracy (%), G2u, glm-5.2, 95% CI |
| `\PfourGTwoUGLMFiveTwoCleanAccN` | 235 | clean-store accuracy (%), G2u, glm-5.2, n |
| `\PfourGTwoUGLMFiveTwoCleanAccP` | n/a | clean-store accuracy (%), G2u, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUGLMFiveTwoFpCost` | 0.4 | clean accuracy change vs none (pp), G2u, glm-5.2 |
| `\PfourGTwoUGLMFiveTwoFpCostLo` | 0.0 | clean accuracy change vs none (pp), G2u, glm-5.2, lower 95% CI bound |
| `\PfourGTwoUGLMFiveTwoFpCostHi` | 1.3 | clean accuracy change vs none (pp), G2u, glm-5.2, upper 95% CI bound |
| `\PfourGTwoUGLMFiveTwoFpCostCI` | [0.0, 1.3] | clean accuracy change vs none (pp), G2u, glm-5.2, 95% CI |
| `\PfourGTwoUGLMFiveTwoFpCostN` | 235 | clean accuracy change vs none (pp), G2u, glm-5.2, n |
| `\PfourGTwoUGLMFiveTwoFpCostP` | 0.704 | clean accuracy change vs none (pp), G2u, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourNonePooledCleanAcc` | 98.2 | clean-store accuracy (%), none, pooled |
| `\PfourNonePooledCleanAccLo` | 97.2 | clean-store accuracy (%), none, pooled, lower 95% CI bound |
| `\PfourNonePooledCleanAccHi` | 99.1 | clean-store accuracy (%), none, pooled, upper 95% CI bound |
| `\PfourNonePooledCleanAccCI` | [97.2, 99.1] | clean-store accuracy (%), none, pooled, 95% CI |
| `\PfourNonePooledCleanAccN` | 1{,}170 | clean-store accuracy (%), none, pooled, n |
| `\PfourNonePooledCleanAccP` | n/a | clean-store accuracy (%), none, pooled, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneDeepSeekVFourFlashCleanAcc` | 99.6 | clean-store accuracy (%), none, deepseek-v4-flash |
| `\PfourNoneDeepSeekVFourFlashCleanAccLo` | 98.7 | clean-store accuracy (%), none, deepseek-v4-flash, lower 95% CI bound |
| `\PfourNoneDeepSeekVFourFlashCleanAccHi` | 100.0 | clean-store accuracy (%), none, deepseek-v4-flash, upper 95% CI bound |
| `\PfourNoneDeepSeekVFourFlashCleanAccCI` | [98.7, 100.0] | clean-store accuracy (%), none, deepseek-v4-flash, 95% CI |
| `\PfourNoneDeepSeekVFourFlashCleanAccN` | 235 | clean-store accuracy (%), none, deepseek-v4-flash, n |
| `\PfourNoneDeepSeekVFourFlashCleanAccP` | n/a | clean-store accuracy (%), none, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneQwenThreeEightTwoSevenBCleanAcc` | 94.9 | clean-store accuracy (%), none, qwen3.8-27b |
| `\PfourNoneQwenThreeEightTwoSevenBCleanAccLo` | 92.3 | clean-store accuracy (%), none, qwen3.8-27b, lower 95% CI bound |
| `\PfourNoneQwenThreeEightTwoSevenBCleanAccHi` | 97.4 | clean-store accuracy (%), none, qwen3.8-27b, upper 95% CI bound |
| `\PfourNoneQwenThreeEightTwoSevenBCleanAccCI` | [92.3, 97.4] | clean-store accuracy (%), none, qwen3.8-27b, 95% CI |
| `\PfourNoneQwenThreeEightTwoSevenBCleanAccN` | 235 | clean-store accuracy (%), none, qwen3.8-27b, n |
| `\PfourNoneQwenThreeEightTwoSevenBCleanAccP` | n/a | clean-store accuracy (%), none, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneGemmaFourThreeOneBCleanAcc` | 98.3 | clean-store accuracy (%), none, gemma-4-31b-it |
| `\PfourNoneGemmaFourThreeOneBCleanAccLo` | 95.7 | clean-store accuracy (%), none, gemma-4-31b-it, lower 95% CI bound |
| `\PfourNoneGemmaFourThreeOneBCleanAccHi` | 100.0 | clean-store accuracy (%), none, gemma-4-31b-it, upper 95% CI bound |
| `\PfourNoneGemmaFourThreeOneBCleanAccCI` | [95.7, 100.0] | clean-store accuracy (%), none, gemma-4-31b-it, 95% CI |
| `\PfourNoneGemmaFourThreeOneBCleanAccN` | 230 | clean-store accuracy (%), none, gemma-4-31b-it, n |
| `\PfourNoneGemmaFourThreeOneBCleanAccP` | n/a | clean-store accuracy (%), none, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneGLMFiveThreeFlashCleanAcc` | 100.0 | clean-store accuracy (%), none, glm-5.3-flash |
| `\PfourNoneGLMFiveThreeFlashCleanAccLo` | 98.4 | clean-store accuracy (%), none, glm-5.3-flash, lower 95% CI bound |
| `\PfourNoneGLMFiveThreeFlashCleanAccHi` | 100.0 | clean-store accuracy (%), none, glm-5.3-flash, upper 95% CI bound |
| `\PfourNoneGLMFiveThreeFlashCleanAccCI` | [98.4, 100.0] | clean-store accuracy (%), none, glm-5.3-flash, 95% CI |
| `\PfourNoneGLMFiveThreeFlashCleanAccN` | 235 | clean-store accuracy (%), none, glm-5.3-flash, n |
| `\PfourNoneGLMFiveThreeFlashCleanAccP` | n/a | clean-store accuracy (%), none, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\PfourNoneGLMFiveTwoCleanAcc` | 98.3 | clean-store accuracy (%), none, glm-5.2 |
| `\PfourNoneGLMFiveTwoCleanAccLo` | 96.6 | clean-store accuracy (%), none, glm-5.2, lower 95% CI bound |
| `\PfourNoneGLMFiveTwoCleanAccHi` | 99.6 | clean-store accuracy (%), none, glm-5.2, upper 95% CI bound |
| `\PfourNoneGLMFiveTwoCleanAccCI` | [96.6, 99.6] | clean-store accuracy (%), none, glm-5.2, 95% CI |
| `\PfourNoneGLMFiveTwoCleanAccN` | 235 | clean-store accuracy (%), none, glm-5.2, n |
| `\PfourNoneGLMFiveTwoCleanAccP` | n/a | clean-store accuracy (%), none, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoURelRed` | 1.3 | relative ASR reduction (%) of G2u vs none T2 |
| `\PfourGTwoURelRedLo` | \ensuremath{-}0.1 | relative ASR reduction (%) of G2u vs none T2, lower 95% CI bound |
| `\PfourGTwoURelRedHi` | 2.6 | relative ASR reduction (%) of G2u vs none T2, upper 95% CI bound |
| `\PfourGTwoURelRedCI` | [\ensuremath{-}0.1, 2.6] | relative ASR reduction (%) of G2u vs none T2, 95% CI |
| `\PfourGTwoURelRedN` | 2{,}310 | relative ASR reduction (%) of G2u vs none T2, n |
| `\PfourGTwoURelRedP` | 0.086 | relative ASR reduction (%) of G2u vs none T2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoUAbsDiff` | \ensuremath{-}0.8 | ASR difference (pp) G2u - none T2 |
| `\PfourGTwoUAbsDiffLo` | \ensuremath{-}1.6 | ASR difference (pp) G2u - none T2, lower 95% CI bound |
| `\PfourGTwoUAbsDiffHi` | 0.1 | ASR difference (pp) G2u - none T2, upper 95% CI bound |
| `\PfourGTwoUAbsDiffCI` | [\ensuremath{-}1.6, 0.1] | ASR difference (pp) G2u - none T2, 95% CI |
| `\PfourGTwoUAbsDiffN` | 2{,}310 | ASR difference (pp) G2u - none T2, n |
| `\PfourGTwoUAbsDiffP` | 0.093 | ASR difference (pp) G2u - none T2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSRelRed` | 56.3 | relative ASR reduction (%) of G2s vs none T2 |
| `\PfourGTwoSRelRedLo` | 52.9 | relative ASR reduction (%) of G2s vs none T2, lower 95% CI bound |
| `\PfourGTwoSRelRedHi` | 59.2 | relative ASR reduction (%) of G2s vs none T2, upper 95% CI bound |
| `\PfourGTwoSRelRedCI` | [52.9, 59.2] | relative ASR reduction (%) of G2s vs none T2, 95% CI |
| `\PfourGTwoSRelRedN` | 2{,}310 | relative ASR reduction (%) of G2s vs none T2, n |
| `\PfourGTwoSRelRedP` | \ensuremath{<}0.001 | relative ASR reduction (%) of G2s vs none T2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSAbsDiff` | \ensuremath{-}34.2 | ASR difference (pp) G2s - none T2 |
| `\PfourGTwoSAbsDiffLo` | \ensuremath{-}37.8 | ASR difference (pp) G2s - none T2, lower 95% CI bound |
| `\PfourGTwoSAbsDiffHi` | \ensuremath{-}30.6 | ASR difference (pp) G2s - none T2, upper 95% CI bound |
| `\PfourGTwoSAbsDiffCI` | [\ensuremath{-}37.8, \ensuremath{-}30.6] | ASR difference (pp) G2s - none T2, 95% CI |
| `\PfourGTwoSAbsDiffN` | 2{,}310 | ASR difference (pp) G2s - none T2, n |
| `\PfourGTwoSAbsDiffP` | \ensuremath{<}0.001 | ASR difference (pp) G2s - none T2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderRelRed` | 1.0 | relative ASR reduction (%) of G2s_insider vs none T2 |
| `\PfourGTwoSInsiderRelRedLo` | \ensuremath{-}1.1 | relative ASR reduction (%) of G2s_insider vs none T2, lower 95% CI bound |
| `\PfourGTwoSInsiderRelRedHi` | 3.1 | relative ASR reduction (%) of G2s_insider vs none T2, upper 95% CI bound |
| `\PfourGTwoSInsiderRelRedCI` | [\ensuremath{-}1.1, 3.1] | relative ASR reduction (%) of G2s_insider vs none T2, 95% CI |
| `\PfourGTwoSInsiderRelRedN` | 2{,}310 | relative ASR reduction (%) of G2s_insider vs none T2, n |
| `\PfourGTwoSInsiderRelRedP` | 0.385 | relative ASR reduction (%) of G2s_insider vs none T2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGTwoSInsiderAbsDiff` | \ensuremath{-}0.6 | ASR difference (pp) G2s_insider - none T2 |
| `\PfourGTwoSInsiderAbsDiffLo` | \ensuremath{-}2.0 | ASR difference (pp) G2s_insider - none T2, lower 95% CI bound |
| `\PfourGTwoSInsiderAbsDiffHi` | 0.6 | ASR difference (pp) G2s_insider - none T2, upper 95% CI bound |
| `\PfourGTwoSInsiderAbsDiffCI` | [\ensuremath{-}2.0, 0.6] | ASR difference (pp) G2s_insider - none T2, 95% CI |
| `\PfourGTwoSInsiderAbsDiffN` | 2{,}310 | ASR difference (pp) G2s_insider - none T2, n |
| `\PfourGTwoSInsiderAbsDiffP` | 0.388 | ASR difference (pp) G2s_insider - none T2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSRelRed` | 99.3 | relative ASR reduction (%) of G1+G2s vs none T2 |
| `\PfourGOnePlusGTwoSRelRedLo` | 98.7 | relative ASR reduction (%) of G1+G2s vs none T2, lower 95% CI bound |
| `\PfourGOnePlusGTwoSRelRedHi` | 99.9 | relative ASR reduction (%) of G1+G2s vs none T2, upper 95% CI bound |
| `\PfourGOnePlusGTwoSRelRedCI` | [98.7, 99.9] | relative ASR reduction (%) of G1+G2s vs none T2, 95% CI |
| `\PfourGOnePlusGTwoSRelRedN` | 2{,}328 | relative ASR reduction (%) of G1+G2s vs none T2, n |
| `\PfourGOnePlusGTwoSRelRedP` | \ensuremath{<}0.001 | relative ASR reduction (%) of G1+G2s vs none T2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOnePlusGTwoSAbsDiff` | \ensuremath{-}60.3 | ASR difference (pp) G1+G2s - none T2 |
| `\PfourGOnePlusGTwoSAbsDiffLo` | \ensuremath{-}64.5 | ASR difference (pp) G1+G2s - none T2, lower 95% CI bound |
| `\PfourGOnePlusGTwoSAbsDiffHi` | \ensuremath{-}56.0 | ASR difference (pp) G1+G2s - none T2, upper 95% CI bound |
| `\PfourGOnePlusGTwoSAbsDiffCI` | [\ensuremath{-}64.5, \ensuremath{-}56.0] | ASR difference (pp) G1+G2s - none T2, 95% CI |
| `\PfourGOnePlusGTwoSAbsDiffN` | 2{,}328 | ASR difference (pp) G1+G2s - none T2, n |
| `\PfourGOnePlusGTwoSAbsDiffP` | \ensuremath{<}0.001 | ASR difference (pp) G1+G2s - none T2, two-sided bootstrap p (n/a if not tested) |
| `\PfourGOneTThreeRelRed` | 97.4 | relative ASR reduction (%) of G1 vs none at T3 |
| `\PfourGOneTThreeRelRedLo` | 96.2 | relative ASR reduction (%) of G1 vs none at T3, lower 95% CI bound |
| `\PfourGOneTThreeRelRedHi` | 98.5 | relative ASR reduction (%) of G1 vs none at T3, upper 95% CI bound |
| `\PfourGOneTThreeRelRedCI` | [96.2, 98.5] | relative ASR reduction (%) of G1 vs none at T3, 95% CI |
| `\PfourGOneTThreeRelRedN` | 2{,}296 | relative ASR reduction (%) of G1 vs none at T3, n |
| `\PfourGOneTThreeRelRedP` | \ensuremath{<}0.001 | relative ASR reduction (%) of G1 vs none at T3, two-sided bootstrap p (n/a if not tested) |
| `\PfourPrimarySensitivity` | 97.6 | primary 4 with unparsed answers dropped (%) |
| `\PfourPrimarySensitivityLo` | 96.4 | primary 4 with unparsed answers dropped (%), lower 95% CI bound |
| `\PfourPrimarySensitivityHi` | 98.7 | primary 4 with unparsed answers dropped (%), upper 95% CI bound |
| `\PfourPrimarySensitivityCI` | [96.4, 98.7] | primary 4 with unparsed answers dropped (%), 95% CI |
| `\PfourPrimarySensitivityN` | 4{,}574 | primary 4 with unparsed answers dropped (%), n |
| `\PfourPrimarySensitivityP` | \ensuremath{<}0.001 | primary 4 with unparsed answers dropped (%), two-sided bootstrap p (n/a if not tested) |
| `\GateDeepSeekVFourFlashDetector` | c | gate detector, deepseek-v4-flash |
| `\GateDeepSeekVFourFlashFprCalib` | 3.3 | gate FPR on calibration genuine entries (%), deepseek-v4-flash |
| `\GateDeepSeekVFourFlashCallsPerRead` | 1 | extra model calls per memory read for G1, deepseek-v4-flash |
| `\GateDeepSeekVFourFlashCleanFlag` | 0.3 | G1 % genuine entries replaced in clean stores, deepseek-v4-flash |
| `\GateDeepSeekVFourFlashCleanFlagLo` | 0.0 | G1 % genuine entries replaced in clean stores, deepseek-v4-flash, lower 95% CI bound |
| `\GateDeepSeekVFourFlashCleanFlagHi` | 0.9 | G1 % genuine entries replaced in clean stores, deepseek-v4-flash, upper 95% CI bound |
| `\GateDeepSeekVFourFlashCleanFlagCI` | [0.0, 0.9] | G1 % genuine entries replaced in clean stores, deepseek-v4-flash, 95% CI |
| `\GateDeepSeekVFourFlashCleanFlagN` | 47 | G1 % genuine entries replaced in clean stores, deepseek-v4-flash, n |
| `\GateDeepSeekVFourFlashCleanFlagP` | n/a | G1 % genuine entries replaced in clean stores, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\GateDeepSeekVFourFlashTargetFlag` | 92.5 | G1 % forged targets replaced, deepseek-v4-flash |
| `\GateDeepSeekVFourFlashTargetFlagLo` | 89.6 | G1 % forged targets replaced, deepseek-v4-flash, lower 95% CI bound |
| `\GateDeepSeekVFourFlashTargetFlagHi` | 95.0 | G1 % forged targets replaced, deepseek-v4-flash, upper 95% CI bound |
| `\GateDeepSeekVFourFlashTargetFlagCI` | [89.6, 95.0] | G1 % forged targets replaced, deepseek-v4-flash, 95% CI |
| `\GateDeepSeekVFourFlashTargetFlagN` | 704 | G1 % forged targets replaced, deepseek-v4-flash, n |
| `\GateDeepSeekVFourFlashTargetFlagP` | n/a | G1 % forged targets replaced, deepseek-v4-flash, two-sided bootstrap p (n/a if not tested) |
| `\GateQwenThreeEightTwoSevenBDetector` | c | gate detector, qwen3.8-27b |
| `\GateQwenThreeEightTwoSevenBFprCalib` | 3.3 | gate FPR on calibration genuine entries (%), qwen3.8-27b |
| `\GateQwenThreeEightTwoSevenBCallsPerRead` | 1 | extra model calls per memory read for G1, qwen3.8-27b |
| `\GateQwenThreeEightTwoSevenBCleanFlag` | 1.2 | G1 % genuine entries replaced in clean stores, qwen3.8-27b |
| `\GateQwenThreeEightTwoSevenBCleanFlagLo` | 0.0 | G1 % genuine entries replaced in clean stores, qwen3.8-27b, lower 95% CI bound |
| `\GateQwenThreeEightTwoSevenBCleanFlagHi` | 2.8 | G1 % genuine entries replaced in clean stores, qwen3.8-27b, upper 95% CI bound |
| `\GateQwenThreeEightTwoSevenBCleanFlagCI` | [0.0, 2.8] | G1 % genuine entries replaced in clean stores, qwen3.8-27b, 95% CI |
| `\GateQwenThreeEightTwoSevenBCleanFlagN` | 46 | G1 % genuine entries replaced in clean stores, qwen3.8-27b, n |
| `\GateQwenThreeEightTwoSevenBCleanFlagP` | n/a | G1 % genuine entries replaced in clean stores, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\GateQwenThreeEightTwoSevenBTargetFlag` | 99.1 | G1 % forged targets replaced, qwen3.8-27b |
| `\GateQwenThreeEightTwoSevenBTargetFlagLo` | 97.9 | G1 % forged targets replaced, qwen3.8-27b, lower 95% CI bound |
| `\GateQwenThreeEightTwoSevenBTargetFlagHi` | 100.0 | G1 % forged targets replaced, qwen3.8-27b, upper 95% CI bound |
| `\GateQwenThreeEightTwoSevenBTargetFlagCI` | [97.9, 100.0] | G1 % forged targets replaced, qwen3.8-27b, 95% CI |
| `\GateQwenThreeEightTwoSevenBTargetFlagN` | 697 | G1 % forged targets replaced, qwen3.8-27b, n |
| `\GateQwenThreeEightTwoSevenBTargetFlagP` | n/a | G1 % forged targets replaced, qwen3.8-27b, two-sided bootstrap p (n/a if not tested) |
| `\GateGemmaFourThreeOneBDetector` | c | gate detector, gemma-4-31b-it |
| `\GateGemmaFourThreeOneBFprCalib` | 1.1 | gate FPR on calibration genuine entries (%), gemma-4-31b-it |
| `\GateGemmaFourThreeOneBCallsPerRead` | 1 | extra model calls per memory read for G1, gemma-4-31b-it |
| `\GateGemmaFourThreeOneBCleanFlag` | 0.0 | G1 % genuine entries replaced in clean stores, gemma-4-31b-it |
| `\GateGemmaFourThreeOneBCleanFlagLo` | 0.0 | G1 % genuine entries replaced in clean stores, gemma-4-31b-it, lower 95% CI bound |
| `\GateGemmaFourThreeOneBCleanFlagHi` | 0.0 | G1 % genuine entries replaced in clean stores, gemma-4-31b-it, upper 95% CI bound |
| `\GateGemmaFourThreeOneBCleanFlagCI` | [0.0, 0.0] | G1 % genuine entries replaced in clean stores, gemma-4-31b-it, 95% CI |
| `\GateGemmaFourThreeOneBCleanFlagN` | 43 | G1 % genuine entries replaced in clean stores, gemma-4-31b-it, n |
| `\GateGemmaFourThreeOneBCleanFlagP` | n/a | G1 % genuine entries replaced in clean stores, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\GateGemmaFourThreeOneBTargetFlag` | 99.0 | G1 % forged targets replaced, gemma-4-31b-it |
| `\GateGemmaFourThreeOneBTargetFlagLo` | 97.8 | G1 % forged targets replaced, gemma-4-31b-it, lower 95% CI bound |
| `\GateGemmaFourThreeOneBTargetFlagHi` | 100.0 | G1 % forged targets replaced, gemma-4-31b-it, upper 95% CI bound |
| `\GateGemmaFourThreeOneBTargetFlagCI` | [97.8, 100.0] | G1 % forged targets replaced, gemma-4-31b-it, 95% CI |
| `\GateGemmaFourThreeOneBTargetFlagN` | 630 | G1 % forged targets replaced, gemma-4-31b-it, n |
| `\GateGemmaFourThreeOneBTargetFlagP` | n/a | G1 % forged targets replaced, gemma-4-31b-it, two-sided bootstrap p (n/a if not tested) |
| `\GateGLMFiveThreeFlashDetector` | r | gate detector, glm-5.3-flash |
| `\GateGLMFiveThreeFlashFprCalib` | 4.4 | gate FPR on calibration genuine entries (%), glm-5.3-flash |
| `\GateGLMFiveThreeFlashCallsPerRead` | 8 | extra model calls per memory read for G1, glm-5.3-flash |
| `\GateGLMFiveThreeFlashCleanFlag` | 10.3 | G1 % genuine entries replaced in clean stores, glm-5.3-flash |
| `\GateGLMFiveThreeFlashCleanFlagLo` | 7.0 | G1 % genuine entries replaced in clean stores, glm-5.3-flash, lower 95% CI bound |
| `\GateGLMFiveThreeFlashCleanFlagHi` | 14.0 | G1 % genuine entries replaced in clean stores, glm-5.3-flash, upper 95% CI bound |
| `\GateGLMFiveThreeFlashCleanFlagCI` | [7.0, 14.0] | G1 % genuine entries replaced in clean stores, glm-5.3-flash, 95% CI |
| `\GateGLMFiveThreeFlashCleanFlagN` | 47 | G1 % genuine entries replaced in clean stores, glm-5.3-flash, n |
| `\GateGLMFiveThreeFlashCleanFlagP` | n/a | G1 % genuine entries replaced in clean stores, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\GateGLMFiveThreeFlashTargetFlag` | 99.7 | G1 % forged targets replaced, glm-5.3-flash |
| `\GateGLMFiveThreeFlashTargetFlagLo` | 99.3 | G1 % forged targets replaced, glm-5.3-flash, lower 95% CI bound |
| `\GateGLMFiveThreeFlashTargetFlagHi` | 100.0 | G1 % forged targets replaced, glm-5.3-flash, upper 95% CI bound |
| `\GateGLMFiveThreeFlashTargetFlagCI` | [99.3, 100.0] | G1 % forged targets replaced, glm-5.3-flash, 95% CI |
| `\GateGLMFiveThreeFlashTargetFlagN` | 704 | G1 % forged targets replaced, glm-5.3-flash, n |
| `\GateGLMFiveThreeFlashTargetFlagP` | n/a | G1 % forged targets replaced, glm-5.3-flash, two-sided bootstrap p (n/a if not tested) |
| `\GateGLMFiveTwoDetector` | c | gate detector, glm-5.2 |
| `\GateGLMFiveTwoFprCalib` | 4.4 | gate FPR on calibration genuine entries (%), glm-5.2 |
| `\GateGLMFiveTwoCallsPerRead` | 1 | extra model calls per memory read for G1, glm-5.2 |
| `\GateGLMFiveTwoCleanFlag` | 2.4 | G1 % genuine entries replaced in clean stores, glm-5.2 |
| `\GateGLMFiveTwoCleanFlagLo` | 0.6 | G1 % genuine entries replaced in clean stores, glm-5.2, lower 95% CI bound |
| `\GateGLMFiveTwoCleanFlagHi` | 4.6 | G1 % genuine entries replaced in clean stores, glm-5.2, upper 95% CI bound |
| `\GateGLMFiveTwoCleanFlagCI` | [0.6, 4.6] | G1 % genuine entries replaced in clean stores, glm-5.2, 95% CI |
| `\GateGLMFiveTwoCleanFlagN` | 47 | G1 % genuine entries replaced in clean stores, glm-5.2, n |
| `\GateGLMFiveTwoCleanFlagP` | n/a | G1 % genuine entries replaced in clean stores, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\GateGLMFiveTwoTargetFlag` | 98.6 | G1 % forged targets replaced, glm-5.2 |
| `\GateGLMFiveTwoTargetFlagLo` | 97.4 | G1 % forged targets replaced, glm-5.2, lower 95% CI bound |
| `\GateGLMFiveTwoTargetFlagHi` | 99.6 | G1 % forged targets replaced, glm-5.2, upper 95% CI bound |
| `\GateGLMFiveTwoTargetFlagCI` | [97.4, 99.6] | G1 % forged targets replaced, glm-5.2, 95% CI |
| `\GateGLMFiveTwoTargetFlagN` | 704 | G1 % forged targets replaced, glm-5.2, n |
| `\GateGLMFiveTwoTargetFlagP` | n/a | G1 % forged targets replaced, glm-5.2, two-sided bootstrap p (n/a if not tested) |
| `\CostMainHostedDetect` | 7.59 | spend (credits), main hosted_detect |
| `\CostMainHostedGen` | 6.42 | spend (credits), main hosted_gen |
| `\CostMainPOnePairs` | 3.07 | spend (credits), main p1_pairs |
| `\CostMainPFourGate` | 8.41 | spend (credits), main p4_gate |
| `\CostTotal` | 27.06 | total spend in the ledger (credits) |
| `\CostCallsTotal` | 65{,}379 | total model calls in the ledger |
| `\DetTokensInV` | 1{,}013 | mean input tokens per store-level audit call, V (all hosted victims) |
| `\DetTokensInC` | 2{,}348 | mean input tokens per store-level audit call, C (all hosted victims) |
| `\DetTokensRatioCV` | 2.3 | input tokens of a C audit call relative to a V audit call |
| `\PfourNotSingledEOneAsr` | 92.6 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E1, tiers pooled, evaluation episodes |
| `\PfourNotSingledEOneAsrLo` | 89.1 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E1, tiers pooled, evaluation episodes, lower 95% CI bound |
| `\PfourNotSingledEOneAsrHi` | 95.7 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E1, tiers pooled, evaluation episodes, upper 95% CI bound |
| `\PfourNotSingledEOneAsrCI` | [89.1, 95.7] | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E1, tiers pooled, evaluation episodes, 95% CI |
| `\PfourNotSingledEOneAsrN` | 674 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E1, tiers pooled, evaluation episodes, n |
| `\PfourNotSingledEOneAsrP` | n/a | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E1, tiers pooled, evaluation episodes, two-sided bootstrap p (n/a if not tested) |
| `\PfourSingledEOneAsr` | 94.4 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E1, tiers pooled, evaluation episodes |
| `\PfourSingledEOneAsrLo` | 80.0 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E1, tiers pooled, evaluation episodes, lower 95% CI bound |
| `\PfourSingledEOneAsrHi` | 100.0 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E1, tiers pooled, evaluation episodes, upper 95% CI bound |
| `\PfourSingledEOneAsrCI` | [80.0, 100.0] | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E1, tiers pooled, evaluation episodes, 95% CI |
| `\PfourSingledEOneAsrN` | 18 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E1, tiers pooled, evaluation episodes, n |
| `\PfourSingledEOneAsrP` | n/a | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E1, tiers pooled, evaluation episodes, two-sided bootstrap p (n/a if not tested) |
| `\PfourNotSingledETwoAsr` | 60.4 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E2, tiers pooled, evaluation episodes |
| `\PfourNotSingledETwoAsrLo` | 51.8 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E2, tiers pooled, evaluation episodes, lower 95% CI bound |
| `\PfourNotSingledETwoAsrHi` | 68.3 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E2, tiers pooled, evaluation episodes, upper 95% CI bound |
| `\PfourNotSingledETwoAsrCI` | [51.8, 68.3] | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E2, tiers pooled, evaluation episodes, 95% CI |
| `\PfourNotSingledETwoAsrN` | 222 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E2, tiers pooled, evaluation episodes, n |
| `\PfourNotSingledETwoAsrP` | n/a | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E2, tiers pooled, evaluation episodes, two-sided bootstrap p (n/a if not tested) |
| `\PfourSingledETwoAsr` | 28.5 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E2, tiers pooled, evaluation episodes |
| `\PfourSingledETwoAsrLo` | 23.7 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E2, tiers pooled, evaluation episodes, lower 95% CI bound |
| `\PfourSingledETwoAsrHi` | 33.6 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E2, tiers pooled, evaluation episodes, upper 95% CI bound |
| `\PfourSingledETwoAsrCI` | [23.7, 33.6] | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E2, tiers pooled, evaluation episodes, 95% CI |
| `\PfourSingledETwoAsrN` | 456 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E2, tiers pooled, evaluation episodes, n |
| `\PfourSingledETwoAsrP` | n/a | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E2, tiers pooled, evaluation episodes, two-sided bootstrap p (n/a if not tested) |
| `\PfourNotSingledEThreeAsr` | 87.0 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E3, tiers pooled, evaluation episodes |
| `\PfourNotSingledEThreeAsrLo` | 82.6 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E3, tiers pooled, evaluation episodes, lower 95% CI bound |
| `\PfourNotSingledEThreeAsrHi` | 90.9 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E3, tiers pooled, evaluation episodes, upper 95% CI bound |
| `\PfourNotSingledEThreeAsrCI` | [82.6, 90.9] | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E3, tiers pooled, evaluation episodes, 95% CI |
| `\PfourNotSingledEThreeAsrN` | 384 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E3, tiers pooled, evaluation episodes, n |
| `\PfourNotSingledEThreeAsrP` | n/a | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E3, tiers pooled, evaluation episodes, two-sided bootstrap p (n/a if not tested) |
| `\PfourSingledEThreeAsr` | 71.8 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E3, tiers pooled, evaluation episodes |
| `\PfourSingledEThreeAsrLo` | 66.2 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E3, tiers pooled, evaluation episodes, lower 95% CI bound |
| `\PfourSingledEThreeAsrHi` | 77.2 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E3, tiers pooled, evaluation episodes, upper 95% CI bound |
| `\PfourSingledEThreeAsrCI` | [66.2, 77.2] | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E3, tiers pooled, evaluation episodes, 95% CI |
| `\PfourSingledEThreeAsrN` | 309 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E3, tiers pooled, evaluation episodes, n |
| `\PfourSingledEThreeAsrP` | n/a | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E3, tiers pooled, evaluation episodes, two-sided bootstrap p (n/a if not tested) |
| `\PfourNotSingledEFourAsr` | 67.6 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E4, tiers pooled, evaluation episodes |
| `\PfourNotSingledEFourAsrLo` | 60.9 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E4, tiers pooled, evaluation episodes, lower 95% CI bound |
| `\PfourNotSingledEFourAsrHi` | 74.1 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E4, tiers pooled, evaluation episodes, upper 95% CI bound |
| `\PfourNotSingledEFourAsrCI` | [60.9, 74.1] | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E4, tiers pooled, evaluation episodes, 95% CI |
| `\PfourNotSingledEFourAsrN` | 324 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E4, tiers pooled, evaluation episodes, n |
| `\PfourNotSingledEFourAsrP` | n/a | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E4, tiers pooled, evaluation episodes, two-sided bootstrap p (n/a if not tested) |
| `\PfourSingledEFourAsr` | 37.8 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E4, tiers pooled, evaluation episodes |
| `\PfourSingledEFourAsrLo` | 32.2 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E4, tiers pooled, evaluation episodes, lower 95% CI bound |
| `\PfourSingledEFourAsrHi` | 43.5 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E4, tiers pooled, evaluation episodes, upper 95% CI bound |
| `\PfourSingledEFourAsrCI` | [32.2, 43.5] | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E4, tiers pooled, evaluation episodes, 95% CI |
| `\PfourSingledEFourAsrN` | 368 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E4, tiers pooled, evaluation episodes, n |
| `\PfourSingledEFourAsrP` | n/a | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E4, tiers pooled, evaluation episodes, two-sided bootstrap p (n/a if not tested) |
| `\PfourNotSingledEFiveAsr` | 27.8 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E5, tiers pooled, evaluation episodes |
| `\PfourNotSingledEFiveAsrLo` | 22.4 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E5, tiers pooled, evaluation episodes, lower 95% CI bound |
| `\PfourNotSingledEFiveAsrHi` | 33.7 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E5, tiers pooled, evaluation episodes, upper 95% CI bound |
| `\PfourNotSingledEFiveAsrCI` | [22.4, 33.7] | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E5, tiers pooled, evaluation episodes, 95% CI |
| `\PfourNotSingledEFiveAsrN` | 478 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E5, tiers pooled, evaluation episodes, n |
| `\PfourNotSingledEFiveAsrP` | n/a | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit E5, tiers pooled, evaluation episodes, two-sided bootstrap p (n/a if not tested) |
| `\PfourSingledEFiveAsr` | 27.9 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E5, tiers pooled, evaluation episodes |
| `\PfourSingledEFiveAsrLo` | 21.2 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E5, tiers pooled, evaluation episodes, lower 95% CI bound |
| `\PfourSingledEFiveAsrHi` | 35.1 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E5, tiers pooled, evaluation episodes, upper 95% CI bound |
| `\PfourSingledEFiveAsrCI` | [21.2, 35.1] | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E5, tiers pooled, evaluation episodes, 95% CI |
| `\PfourSingledEFiveAsrN` | 204 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E5, tiers pooled, evaluation episodes, n |
| `\PfourSingledEFiveAsrP` | n/a | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit E5, tiers pooled, evaluation episodes, two-sided bootstrap p (n/a if not tested) |
| `\PfourNotSingledAsr` | 69.4 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit all, tiers pooled, evaluation episodes |
| `\PfourNotSingledAsrLo` | 66.7 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit all, tiers pooled, evaluation episodes, lower 95% CI bound |
| `\PfourNotSingledAsrHi` | 72.0 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit all, tiers pooled, evaluation episodes, upper 95% CI bound |
| `\PfourNotSingledAsrCI` | [66.7, 72.0] | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit all, tiers pooled, evaluation episodes, 95% CI |
| `\PfourNotSingledAsrN` | 2{,}082 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit all, tiers pooled, evaluation episodes, n |
| `\PfourNotSingledAsrP` | n/a | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: False, edit all, tiers pooled, evaluation episodes, two-sided bootstrap p (n/a if not tested) |
| `\PfourSingledAsr` | 41.7 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit all, tiers pooled, evaluation episodes |
| `\PfourSingledAsrLo` | 38.7 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit all, tiers pooled, evaluation episodes, lower 95% CI bound |
| `\PfourSingledAsrHi` | 44.6 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit all, tiers pooled, evaluation episodes, upper 95% CI bound |
| `\PfourSingledAsrCI` | [38.7, 44.6] | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit all, tiers pooled, evaluation episodes, 95% CI |
| `\PfourSingledAsrN` | 1{,}355 | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit all, tiers pooled, evaluation episodes, n |
| `\PfourSingledAsrP` | n/a | ASR (%) without defence where the verbal audit rated the forged entry strictly lowest: True, edit all, tiers pooled, evaluation episodes, two-sided bootstrap p (n/a if not tested) |
