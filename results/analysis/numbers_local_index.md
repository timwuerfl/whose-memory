# Local-analysis macros (`paper/numbers_local.tex`)

Generated from `results/analysis/local.json` by `analysis/local_tables.py`.

| macro | value | meaning |
|---|---|---|
| `\LocNEpisodes` | 150 | local main episodes with registry items |
| `\LocNInstances` | 300 | attack instances (genuine target notes) |
| `\LocNItems` | 4{,}199 | registry items (all kinds) |
| `\LocValidRateTZero` | 100.0\% | share of T0 forgeries that are valid (n=300) |
| `\LocValidRateTOne` | 84.7\% | share of T1 forgeries that are valid (n=300) |
| `\LocValidRateTTwo` | 96.7\% | share of T2 forgeries that are valid (n=300) |
| `\LocValidRateCand` | 81.1\% | share of pool candidates that are valid (n=2400) |
| `\LocInstWithValidCand` | 299 | instances with at least one valid candidate (of 300) |
| `\LocNPosTZero` | 300 | valid T0 forgeries (positives, all instances) |
| `\LocNNegTZero` | 300 | matched genuine notes for T0 |
| `\LocNPosTOne` | 254 | valid T1 forgeries (positives, all instances) |
| `\LocNNegTOne` | 254 | matched genuine notes for T1 |
| `\LocNPosTTwo` | 290 | valid T2 forgeries (positives, all instances) |
| `\LocNNegTTwo` | 290 | matched genuine notes for T2 |
| `\LocNPosTTwoR` | 299 | valid T2r forgeries (positives, all instances) |
| `\LocNNegTTwoR` | 299 | matched genuine notes for T2r |
| `\LocNPosTThree` | 299 | valid T3 forgeries (positives, all instances) |
| `\LocNNegTThree` | 299 | matched genuine notes for T3 |
| `\LocNPosTFourS` | 299 | valid T4s forgeries (positives, all instances) |
| `\LocNNegTFourS` | 299 | matched genuine notes for T4s |
| `\LocNPosTFourD` | 299 | valid T4d forgeries (positives, all instances) |
| `\LocNNegTFourD` | 299 | matched genuine notes for T4d |
| `\LocNPosTFourC` | 299 | valid T4c forgeries (positives, all instances) |
| `\LocNNegTFourC` | 299 | matched genuine notes for T4c |
| `\LocNPosTFourP` | 299 | valid T4p forgeries (positives, all instances) |
| `\LocNNegTFourP` | 299 | matched genuine notes for T4p |
| `\LocAucSurpTZero` | 0.97 | AUROC of s_trace_mean for T0 vs matched genuine notes (all instances); n+=300, n-=300 |
| `\LocAucSurpTZeroLo` | 0.96 | lower 95% CI bound of \LocAucSurpTZero |
| `\LocAucSurpTZeroHi` | 0.98 | upper 95% CI bound of \LocAucSurpTZero |
| `\LocAucSurpTOne` | 0.97 | AUROC of s_trace_mean for T1 vs matched genuine notes (all instances); n+=254, n-=254 |
| `\LocAucSurpTOneLo` | 0.95 | lower 95% CI bound of \LocAucSurpTOne |
| `\LocAucSurpTOneHi` | 0.98 | upper 95% CI bound of \LocAucSurpTOne |
| `\LocAucSurpTTwo` | 0.97 | AUROC of s_trace_mean for T2 vs matched genuine notes (all instances); n+=290, n-=290 |
| `\LocAucSurpTTwoLo` | 0.95 | lower 95% CI bound of \LocAucSurpTTwo |
| `\LocAucSurpTTwoHi` | 0.98 | upper 95% CI bound of \LocAucSurpTTwo |
| `\LocAucSurpTTwoR` | 0.98 | AUROC of s_trace_mean for T2r vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucSurpTTwoRLo` | 0.97 | lower 95% CI bound of \LocAucSurpTTwoR |
| `\LocAucSurpTTwoRHi` | 0.99 | upper 95% CI bound of \LocAucSurpTTwoR |
| `\LocAucSurpTThree` | 0.98 | AUROC of s_trace_mean for T3 vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucSurpTThreeLo` | 0.97 | lower 95% CI bound of \LocAucSurpTThree |
| `\LocAucSurpTThreeHi` | 0.99 | upper 95% CI bound of \LocAucSurpTThree |
| `\LocAucSurpTFourS` | 0.97 | AUROC of s_trace_mean for T4s vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucSurpTFourSLo` | 0.95 | lower 95% CI bound of \LocAucSurpTFourS |
| `\LocAucSurpTFourSHi` | 0.98 | upper 95% CI bound of \LocAucSurpTFourS |
| `\LocAucSurpTFourD` | 0.97 | AUROC of s_trace_mean for T4d vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucSurpTFourDLo` | 0.96 | lower 95% CI bound of \LocAucSurpTFourD |
| `\LocAucSurpTFourDHi` | 0.98 | upper 95% CI bound of \LocAucSurpTFourD |
| `\LocAucSurpTFourC` | 0.98 | AUROC of s_trace_mean for T4c vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucSurpTFourCLo` | 0.97 | lower 95% CI bound of \LocAucSurpTFourC |
| `\LocAucSurpTFourCHi` | 0.99 | upper 95% CI bound of \LocAucSurpTFourC |
| `\LocAucSurpTFourP` | 0.98 | AUROC of s_trace_mean for T4p vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucSurpTFourPLo` | 0.97 | lower 95% CI bound of \LocAucSurpTFourP |
| `\LocAucSurpTFourPHi` | 0.99 | upper 95% CI bound of \LocAucSurpTFourP |
| `\LocAucSurpBlindTZero` | 0.55 | AUROC of s_blind_mean for T0 vs matched genuine notes (all instances); n+=300, n-=300 |
| `\LocAucSurpBlindTZeroLo` | 0.54 | lower 95% CI bound of \LocAucSurpBlindTZero |
| `\LocAucSurpBlindTZeroHi` | 0.57 | upper 95% CI bound of \LocAucSurpBlindTZero |
| `\LocAucSurpBlindTOne` | 0.62 | AUROC of s_blind_mean for T1 vs matched genuine notes (all instances); n+=254, n-=254 |
| `\LocAucSurpBlindTOneLo` | 0.60 | lower 95% CI bound of \LocAucSurpBlindTOne |
| `\LocAucSurpBlindTOneHi` | 0.64 | upper 95% CI bound of \LocAucSurpBlindTOne |
| `\LocAucSurpBlindTTwo` | 0.64 | AUROC of s_blind_mean for T2 vs matched genuine notes (all instances); n+=290, n-=290 |
| `\LocAucSurpBlindTTwoLo` | 0.62 | lower 95% CI bound of \LocAucSurpBlindTTwo |
| `\LocAucSurpBlindTTwoHi` | 0.66 | upper 95% CI bound of \LocAucSurpBlindTTwo |
| `\LocAucSurpBlindTTwoR` | 0.71 | AUROC of s_blind_mean for T2r vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucSurpBlindTTwoRLo` | 0.68 | lower 95% CI bound of \LocAucSurpBlindTTwoR |
| `\LocAucSurpBlindTTwoRHi` | 0.73 | upper 95% CI bound of \LocAucSurpBlindTTwoR |
| `\LocAucSurpBlindTThree` | 0.71 | AUROC of s_blind_mean for T3 vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucSurpBlindTThreeLo` | 0.68 | lower 95% CI bound of \LocAucSurpBlindTThree |
| `\LocAucSurpBlindTThreeHi` | 0.73 | upper 95% CI bound of \LocAucSurpBlindTThree |
| `\LocAucSurpBlindTFourS` | 0.62 | AUROC of s_blind_mean for T4s vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucSurpBlindTFourSLo` | 0.60 | lower 95% CI bound of \LocAucSurpBlindTFourS |
| `\LocAucSurpBlindTFourSHi` | 0.64 | upper 95% CI bound of \LocAucSurpBlindTFourS |
| `\LocAucSurpBlindTFourD` | 0.73 | AUROC of s_blind_mean for T4d vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucSurpBlindTFourDLo` | 0.71 | lower 95% CI bound of \LocAucSurpBlindTFourD |
| `\LocAucSurpBlindTFourDHi` | 0.75 | upper 95% CI bound of \LocAucSurpBlindTFourD |
| `\LocAucSurpBlindTFourC` | 0.70 | AUROC of s_blind_mean for T4c vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucSurpBlindTFourCLo` | 0.68 | lower 95% CI bound of \LocAucSurpBlindTFourC |
| `\LocAucSurpBlindTFourCHi` | 0.72 | upper 95% CI bound of \LocAucSurpBlindTFourC |
| `\LocAucSurpBlindTFourP` | 0.71 | AUROC of s_blind_mean for T4p vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucSurpBlindTFourPLo` | 0.69 | lower 95% CI bound of \LocAucSurpBlindTFourP |
| `\LocAucSurpBlindTFourPHi` | 0.74 | upper 95% CI bound of \LocAucSurpBlindTFourP |
| `\LocAucSurpDeltaTZero` | 0.76 | AUROC of s_delta for T0 vs matched genuine notes (all instances); n+=300, n-=300 |
| `\LocAucSurpDeltaTZeroLo` | 0.74 | lower 95% CI bound of \LocAucSurpDeltaTZero |
| `\LocAucSurpDeltaTZeroHi` | 0.78 | upper 95% CI bound of \LocAucSurpDeltaTZero |
| `\LocAucSurpDeltaTOne` | 0.78 | AUROC of s_delta for T1 vs matched genuine notes (all instances); n+=254, n-=254 |
| `\LocAucSurpDeltaTOneLo` | 0.76 | lower 95% CI bound of \LocAucSurpDeltaTOne |
| `\LocAucSurpDeltaTOneHi` | 0.80 | upper 95% CI bound of \LocAucSurpDeltaTOne |
| `\LocAucSurpDeltaTTwo` | 0.78 | AUROC of s_delta for T2 vs matched genuine notes (all instances); n+=290, n-=290 |
| `\LocAucSurpDeltaTTwoLo` | 0.76 | lower 95% CI bound of \LocAucSurpDeltaTTwo |
| `\LocAucSurpDeltaTTwoHi` | 0.81 | upper 95% CI bound of \LocAucSurpDeltaTTwo |
| `\LocAucSurpDeltaTTwoR` | 0.82 | AUROC of s_delta for T2r vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucSurpDeltaTTwoRLo` | 0.80 | lower 95% CI bound of \LocAucSurpDeltaTTwoR |
| `\LocAucSurpDeltaTTwoRHi` | 0.84 | upper 95% CI bound of \LocAucSurpDeltaTTwoR |
| `\LocAucSurpDeltaTThree` | 0.83 | AUROC of s_delta for T3 vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucSurpDeltaTThreeLo` | 0.81 | lower 95% CI bound of \LocAucSurpDeltaTThree |
| `\LocAucSurpDeltaTThreeHi` | 0.85 | upper 95% CI bound of \LocAucSurpDeltaTThree |
| `\LocAucSurpDeltaTFourS` | 0.75 | AUROC of s_delta for T4s vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucSurpDeltaTFourSLo` | 0.73 | lower 95% CI bound of \LocAucSurpDeltaTFourS |
| `\LocAucSurpDeltaTFourSHi` | 0.78 | upper 95% CI bound of \LocAucSurpDeltaTFourS |
| `\LocAucSurpDeltaTFourD` | 0.72 | AUROC of s_delta for T4d vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucSurpDeltaTFourDLo` | 0.70 | lower 95% CI bound of \LocAucSurpDeltaTFourD |
| `\LocAucSurpDeltaTFourDHi` | 0.74 | upper 95% CI bound of \LocAucSurpDeltaTFourD |
| `\LocAucSurpDeltaTFourC` | 0.79 | AUROC of s_delta for T4c vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucSurpDeltaTFourCLo` | 0.77 | lower 95% CI bound of \LocAucSurpDeltaTFourC |
| `\LocAucSurpDeltaTFourCHi` | 0.81 | upper 95% CI bound of \LocAucSurpDeltaTFourC |
| `\LocAucSurpDeltaTFourP` | 0.86 | AUROC of s_delta for T4p vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucSurpDeltaTFourPLo` | 0.84 | lower 95% CI bound of \LocAucSurpDeltaTFourP |
| `\LocAucSurpDeltaTFourPHi` | 0.88 | upper 95% CI bound of \LocAucSurpDeltaTFourP |
| `\LocAucVerbalTZero` | 0.65 | AUROC of v for T0 vs matched genuine notes (all instances); n+=300, n-=300 |
| `\LocAucVerbalTZeroLo` | 0.62 | lower 95% CI bound of \LocAucVerbalTZero |
| `\LocAucVerbalTZeroHi` | 0.67 | upper 95% CI bound of \LocAucVerbalTZero |
| `\LocAucVerbalTOne` | 0.56 | AUROC of v for T1 vs matched genuine notes (all instances); n+=254, n-=254 |
| `\LocAucVerbalTOneLo` | 0.55 | lower 95% CI bound of \LocAucVerbalTOne |
| `\LocAucVerbalTOneHi` | 0.58 | upper 95% CI bound of \LocAucVerbalTOne |
| `\LocAucVerbalTTwo` | 0.57 | AUROC of v for T2 vs matched genuine notes (all instances); n+=290, n-=290 |
| `\LocAucVerbalTTwoLo` | 0.55 | lower 95% CI bound of \LocAucVerbalTTwo |
| `\LocAucVerbalTTwoHi` | 0.59 | upper 95% CI bound of \LocAucVerbalTTwo |
| `\LocAucVerbalTTwoR` | 0.60 | AUROC of v for T2r vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucVerbalTTwoRLo` | 0.58 | lower 95% CI bound of \LocAucVerbalTTwoR |
| `\LocAucVerbalTTwoRHi` | 0.62 | upper 95% CI bound of \LocAucVerbalTTwoR |
| `\LocAucVerbalTThree` | 0.54 | AUROC of v for T3 vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucVerbalTThreeLo` | 0.53 | lower 95% CI bound of \LocAucVerbalTThree |
| `\LocAucVerbalTThreeHi` | 0.56 | upper 95% CI bound of \LocAucVerbalTThree |
| `\LocAucVerbalTFourS` | 0.59 | AUROC of v for T4s vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucVerbalTFourSLo` | 0.57 | lower 95% CI bound of \LocAucVerbalTFourS |
| `\LocAucVerbalTFourSHi` | 0.61 | upper 95% CI bound of \LocAucVerbalTFourS |
| `\LocAucVerbalTFourD` | 0.59 | AUROC of v for T4d vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucVerbalTFourDLo` | 0.57 | lower 95% CI bound of \LocAucVerbalTFourD |
| `\LocAucVerbalTFourDHi` | 0.61 | upper 95% CI bound of \LocAucVerbalTFourD |
| `\LocAucVerbalTFourC` | 0.56 | AUROC of v for T4c vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucVerbalTFourCLo` | 0.54 | lower 95% CI bound of \LocAucVerbalTFourC |
| `\LocAucVerbalTFourCHi` | 0.58 | upper 95% CI bound of \LocAucVerbalTFourC |
| `\LocAucVerbalTFourP` | 0.59 | AUROC of v for T4p vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucVerbalTFourPLo` | 0.57 | lower 95% CI bound of \LocAucVerbalTFourP |
| `\LocAucVerbalTFourPHi` | 0.61 | upper 95% CI bound of \LocAucVerbalTFourP |
| `\LocAucConsistTZero` | 0.98 | AUROC of c for T0 vs matched genuine notes (all instances); n+=300, n-=300 |
| `\LocAucConsistTZeroLo` | 0.97 | lower 95% CI bound of \LocAucConsistTZero |
| `\LocAucConsistTZeroHi` | 0.98 | upper 95% CI bound of \LocAucConsistTZero |
| `\LocAucConsistTOne` | 0.95 | AUROC of c for T1 vs matched genuine notes (all instances); n+=254, n-=254 |
| `\LocAucConsistTOneLo` | 0.93 | lower 95% CI bound of \LocAucConsistTOne |
| `\LocAucConsistTOneHi` | 0.96 | upper 95% CI bound of \LocAucConsistTOne |
| `\LocAucConsistTTwo` | 0.95 | AUROC of c for T2 vs matched genuine notes (all instances); n+=290, n-=290 |
| `\LocAucConsistTTwoLo` | 0.94 | lower 95% CI bound of \LocAucConsistTTwo |
| `\LocAucConsistTTwoHi` | 0.96 | upper 95% CI bound of \LocAucConsistTTwo |
| `\LocAucConsistTTwoR` | 0.96 | AUROC of c for T2r vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucConsistTTwoRLo` | 0.95 | lower 95% CI bound of \LocAucConsistTTwoR |
| `\LocAucConsistTTwoRHi` | 0.97 | upper 95% CI bound of \LocAucConsistTTwoR |
| `\LocAucConsistTThree` | 0.95 | AUROC of c for T3 vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucConsistTThreeLo` | 0.94 | lower 95% CI bound of \LocAucConsistTThree |
| `\LocAucConsistTThreeHi` | 0.97 | upper 95% CI bound of \LocAucConsistTThree |
| `\LocAucConsistTFourS` | 0.95 | AUROC of c for T4s vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucConsistTFourSLo` | 0.93 | lower 95% CI bound of \LocAucConsistTFourS |
| `\LocAucConsistTFourSHi` | 0.97 | upper 95% CI bound of \LocAucConsistTFourS |
| `\LocAucConsistTFourD` | 0.95 | AUROC of c for T4d vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucConsistTFourDLo` | 0.93 | lower 95% CI bound of \LocAucConsistTFourD |
| `\LocAucConsistTFourDHi` | 0.96 | upper 95% CI bound of \LocAucConsistTFourD |
| `\LocAucConsistTFourC` | 0.90 | AUROC of c for T4c vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucConsistTFourCLo` | 0.88 | lower 95% CI bound of \LocAucConsistTFourC |
| `\LocAucConsistTFourCHi` | 0.92 | upper 95% CI bound of \LocAucConsistTFourC |
| `\LocAucConsistTFourP` | 0.97 | AUROC of c for T4p vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucConsistTFourPLo` | 0.96 | lower 95% CI bound of \LocAucConsistTFourP |
| `\LocAucConsistTFourPHi` | 0.98 | upper 95% CI bound of \LocAucConsistTFourP |
| `\LocAucProbeSelfTZero` | 0.50 | AUROC of P1 for T0 vs matched genuine notes (all instances); n+=300, n-=300 |
| `\LocAucProbeSelfTZeroLo` | 0.49 | lower 95% CI bound of \LocAucProbeSelfTZero |
| `\LocAucProbeSelfTZeroHi` | 0.51 | upper 95% CI bound of \LocAucProbeSelfTZero |
| `\LocAucProbeSelfTOne` | 0.54 | AUROC of P1 for T1 vs matched genuine notes (all instances); n+=254, n-=254 |
| `\LocAucProbeSelfTOneLo` | 0.52 | lower 95% CI bound of \LocAucProbeSelfTOne |
| `\LocAucProbeSelfTOneHi` | 0.56 | upper 95% CI bound of \LocAucProbeSelfTOne |
| `\LocAucProbeSelfTTwo` | 0.46 | AUROC of P1 for T2 vs matched genuine notes (all instances); n+=290, n-=290 |
| `\LocAucProbeSelfTTwoLo` | 0.44 | lower 95% CI bound of \LocAucProbeSelfTTwo |
| `\LocAucProbeSelfTTwoHi` | 0.48 | upper 95% CI bound of \LocAucProbeSelfTTwo |
| `\LocAucProbeSelfTTwoR` | 0.43 | AUROC of P1 for T2r vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucProbeSelfTTwoRLo` | 0.41 | lower 95% CI bound of \LocAucProbeSelfTTwoR |
| `\LocAucProbeSelfTTwoRHi` | 0.46 | upper 95% CI bound of \LocAucProbeSelfTTwoR |
| `\LocAucProbeSelfTThree` | 0.41 | AUROC of P1 for T3 vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucProbeSelfTThreeLo` | 0.38 | lower 95% CI bound of \LocAucProbeSelfTThree |
| `\LocAucProbeSelfTThreeHi` | 0.43 | upper 95% CI bound of \LocAucProbeSelfTThree |
| `\LocAucProbeSelfTFourS` | 0.50 | AUROC of P1 for T4s vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucProbeSelfTFourSLo` | 0.49 | lower 95% CI bound of \LocAucProbeSelfTFourS |
| `\LocAucProbeSelfTFourSHi` | 0.52 | upper 95% CI bound of \LocAucProbeSelfTFourS |
| `\LocAucProbeSelfTFourD` | 0.51 | AUROC of P1 for T4d vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucProbeSelfTFourDLo` | 0.49 | lower 95% CI bound of \LocAucProbeSelfTFourD |
| `\LocAucProbeSelfTFourDHi` | 0.53 | upper 95% CI bound of \LocAucProbeSelfTFourD |
| `\LocAucProbeSelfTFourC` | 0.46 | AUROC of P1 for T4c vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucProbeSelfTFourCLo` | 0.44 | lower 95% CI bound of \LocAucProbeSelfTFourC |
| `\LocAucProbeSelfTFourCHi` | 0.48 | upper 95% CI bound of \LocAucProbeSelfTFourC |
| `\LocAucProbeSelfTFourP` | \textit{n/a} | AUROC of P1 for T4p vs matched genuine notes (all instances); n+=None, n-=None (n/a: full-sample LOFO probe shares training episodes with the T4p attacker; use the split-half probe) |
| `\LocAucProbeSelfTFourPLo` | \textit{n/a} | lower 95% CI bound of \LocAucProbeSelfTFourP (n/a: full-sample LOFO probe shares training episodes with the T4p attacker; use the split-half probe) |
| `\LocAucProbeSelfTFourPHi` | \textit{n/a} | upper 95% CI bound of \LocAucProbeSelfTFourP (n/a: full-sample LOFO probe shares training episodes with the T4p attacker; use the split-half probe) |
| `\LocAucProbeConsTZero` | 0.97 | AUROC of P2 for T0 vs matched genuine notes (all instances); n+=300, n-=300 |
| `\LocAucProbeConsTZeroLo` | 0.96 | lower 95% CI bound of \LocAucProbeConsTZero |
| `\LocAucProbeConsTZeroHi` | 0.98 | upper 95% CI bound of \LocAucProbeConsTZero |
| `\LocAucProbeConsTOne` | 0.96 | AUROC of P2 for T1 vs matched genuine notes (all instances); n+=254, n-=254 |
| `\LocAucProbeConsTOneLo` | 0.95 | lower 95% CI bound of \LocAucProbeConsTOne |
| `\LocAucProbeConsTOneHi` | 0.97 | upper 95% CI bound of \LocAucProbeConsTOne |
| `\LocAucProbeConsTTwo` | 0.96 | AUROC of P2 for T2 vs matched genuine notes (all instances); n+=290, n-=290 |
| `\LocAucProbeConsTTwoLo` | 0.95 | lower 95% CI bound of \LocAucProbeConsTTwo |
| `\LocAucProbeConsTTwoHi` | 0.97 | upper 95% CI bound of \LocAucProbeConsTTwo |
| `\LocAucProbeConsTTwoR` | 0.97 | AUROC of P2 for T2r vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucProbeConsTTwoRLo` | 0.95 | lower 95% CI bound of \LocAucProbeConsTTwoR |
| `\LocAucProbeConsTTwoRHi` | 0.98 | upper 95% CI bound of \LocAucProbeConsTTwoR |
| `\LocAucProbeConsTThree` | 0.97 | AUROC of P2 for T3 vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucProbeConsTThreeLo` | 0.96 | lower 95% CI bound of \LocAucProbeConsTThree |
| `\LocAucProbeConsTThreeHi` | 0.98 | upper 95% CI bound of \LocAucProbeConsTThree |
| `\LocAucProbeConsTFourS` | 0.95 | AUROC of P2 for T4s vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucProbeConsTFourSLo` | 0.93 | lower 95% CI bound of \LocAucProbeConsTFourS |
| `\LocAucProbeConsTFourSHi` | 0.96 | upper 95% CI bound of \LocAucProbeConsTFourS |
| `\LocAucProbeConsTFourD` | 0.95 | AUROC of P2 for T4d vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucProbeConsTFourDLo` | 0.94 | lower 95% CI bound of \LocAucProbeConsTFourD |
| `\LocAucProbeConsTFourDHi` | 0.97 | upper 95% CI bound of \LocAucProbeConsTFourD |
| `\LocAucProbeConsTFourC` | 0.96 | AUROC of P2 for T4c vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucProbeConsTFourCLo` | 0.94 | lower 95% CI bound of \LocAucProbeConsTFourC |
| `\LocAucProbeConsTFourCHi` | 0.97 | upper 95% CI bound of \LocAucProbeConsTFourC |
| `\LocAucProbeConsTFourP` | \textit{n/a} | AUROC of P2 for T4p vs matched genuine notes (all instances); n+=None, n-=None (n/a: full-sample LOFO probe shares training episodes with the T4p attacker; use the split-half probe) |
| `\LocAucProbeConsTFourPLo` | \textit{n/a} | lower 95% CI bound of \LocAucProbeConsTFourP (n/a: full-sample LOFO probe shares training episodes with the T4p attacker; use the split-half probe) |
| `\LocAucProbeConsTFourPHi` | \textit{n/a} | upper 95% CI bound of \LocAucProbeConsTFourP (n/a: full-sample LOFO probe shares training episodes with the T4p attacker; use the split-half probe) |
| `\LocAucProbeSelfSplitTZero` | 0.48 | AUROC of P1h for T0 vs matched genuine notes (all instances); n+=300, n-=300 |
| `\LocAucProbeSelfSplitTZeroLo` | 0.48 | lower 95% CI bound of \LocAucProbeSelfSplitTZero |
| `\LocAucProbeSelfSplitTZeroHi` | 0.49 | upper 95% CI bound of \LocAucProbeSelfSplitTZero |
| `\LocAucProbeSelfSplitTOne` | 0.53 | AUROC of P1h for T1 vs matched genuine notes (all instances); n+=254, n-=254 |
| `\LocAucProbeSelfSplitTOneLo` | 0.51 | lower 95% CI bound of \LocAucProbeSelfSplitTOne |
| `\LocAucProbeSelfSplitTOneHi` | 0.54 | upper 95% CI bound of \LocAucProbeSelfSplitTOne |
| `\LocAucProbeSelfSplitTTwo` | 0.47 | AUROC of P1h for T2 vs matched genuine notes (all instances); n+=290, n-=290 |
| `\LocAucProbeSelfSplitTTwoLo` | 0.46 | lower 95% CI bound of \LocAucProbeSelfSplitTTwo |
| `\LocAucProbeSelfSplitTTwoHi` | 0.48 | upper 95% CI bound of \LocAucProbeSelfSplitTTwo |
| `\LocAucProbeSelfSplitTTwoR` | 0.45 | AUROC of P1h for T2r vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucProbeSelfSplitTTwoRLo` | 0.44 | lower 95% CI bound of \LocAucProbeSelfSplitTTwoR |
| `\LocAucProbeSelfSplitTTwoRHi` | 0.46 | upper 95% CI bound of \LocAucProbeSelfSplitTTwoR |
| `\LocAucProbeSelfSplitTThree` | 0.45 | AUROC of P1h for T3 vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucProbeSelfSplitTThreeLo` | 0.43 | lower 95% CI bound of \LocAucProbeSelfSplitTThree |
| `\LocAucProbeSelfSplitTThreeHi` | 0.46 | upper 95% CI bound of \LocAucProbeSelfSplitTThree |
| `\LocAucProbeSelfSplitTFourS` | 0.50 | AUROC of P1h for T4s vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucProbeSelfSplitTFourSLo` | 0.49 | lower 95% CI bound of \LocAucProbeSelfSplitTFourS |
| `\LocAucProbeSelfSplitTFourSHi` | 0.51 | upper 95% CI bound of \LocAucProbeSelfSplitTFourS |
| `\LocAucProbeSelfSplitTFourD` | 0.50 | AUROC of P1h for T4d vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucProbeSelfSplitTFourDLo` | 0.49 | lower 95% CI bound of \LocAucProbeSelfSplitTFourD |
| `\LocAucProbeSelfSplitTFourDHi` | 0.52 | upper 95% CI bound of \LocAucProbeSelfSplitTFourD |
| `\LocAucProbeSelfSplitTFourC` | 0.47 | AUROC of P1h for T4c vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucProbeSelfSplitTFourCLo` | 0.46 | lower 95% CI bound of \LocAucProbeSelfSplitTFourC |
| `\LocAucProbeSelfSplitTFourCHi` | 0.49 | upper 95% CI bound of \LocAucProbeSelfSplitTFourC |
| `\LocAucProbeSelfSplitTFourP` | 0.38 | AUROC of P1h for T4p vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucProbeSelfSplitTFourPLo` | 0.37 | lower 95% CI bound of \LocAucProbeSelfSplitTFourP |
| `\LocAucProbeSelfSplitTFourPHi` | 0.39 | upper 95% CI bound of \LocAucProbeSelfSplitTFourP |
| `\LocAucProbeConsSplitTZero` | 0.95 | AUROC of P2h for T0 vs matched genuine notes (all instances); n+=300, n-=300 |
| `\LocAucProbeConsSplitTZeroLo` | 0.94 | lower 95% CI bound of \LocAucProbeConsSplitTZero |
| `\LocAucProbeConsSplitTZeroHi` | 0.97 | upper 95% CI bound of \LocAucProbeConsSplitTZero |
| `\LocAucProbeConsSplitTOne` | 0.94 | AUROC of P2h for T1 vs matched genuine notes (all instances); n+=254, n-=254 |
| `\LocAucProbeConsSplitTOneLo` | 0.92 | lower 95% CI bound of \LocAucProbeConsSplitTOne |
| `\LocAucProbeConsSplitTOneHi` | 0.96 | upper 95% CI bound of \LocAucProbeConsSplitTOne |
| `\LocAucProbeConsSplitTTwo` | 0.94 | AUROC of P2h for T2 vs matched genuine notes (all instances); n+=290, n-=290 |
| `\LocAucProbeConsSplitTTwoLo` | 0.92 | lower 95% CI bound of \LocAucProbeConsSplitTTwo |
| `\LocAucProbeConsSplitTTwoHi` | 0.95 | upper 95% CI bound of \LocAucProbeConsSplitTTwo |
| `\LocAucProbeConsSplitTTwoR` | 0.95 | AUROC of P2h for T2r vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucProbeConsSplitTTwoRLo` | 0.94 | lower 95% CI bound of \LocAucProbeConsSplitTTwoR |
| `\LocAucProbeConsSplitTTwoRHi` | 0.96 | upper 95% CI bound of \LocAucProbeConsSplitTTwoR |
| `\LocAucProbeConsSplitTThree` | 0.95 | AUROC of P2h for T3 vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucProbeConsSplitTThreeLo` | 0.94 | lower 95% CI bound of \LocAucProbeConsSplitTThree |
| `\LocAucProbeConsSplitTThreeHi` | 0.97 | upper 95% CI bound of \LocAucProbeConsSplitTThree |
| `\LocAucProbeConsSplitTFourS` | 0.93 | AUROC of P2h for T4s vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucProbeConsSplitTFourSLo` | 0.91 | lower 95% CI bound of \LocAucProbeConsSplitTFourS |
| `\LocAucProbeConsSplitTFourSHi` | 0.95 | upper 95% CI bound of \LocAucProbeConsSplitTFourS |
| `\LocAucProbeConsSplitTFourD` | 0.93 | AUROC of P2h for T4d vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucProbeConsSplitTFourDLo` | 0.91 | lower 95% CI bound of \LocAucProbeConsSplitTFourD |
| `\LocAucProbeConsSplitTFourDHi` | 0.95 | upper 95% CI bound of \LocAucProbeConsSplitTFourD |
| `\LocAucProbeConsSplitTFourC` | 0.94 | AUROC of P2h for T4c vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucProbeConsSplitTFourCLo` | 0.92 | lower 95% CI bound of \LocAucProbeConsSplitTFourC |
| `\LocAucProbeConsSplitTFourCHi` | 0.96 | upper 95% CI bound of \LocAucProbeConsSplitTFourC |
| `\LocAucProbeConsSplitTFourP` | 0.96 | AUROC of P2h for T4p vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucProbeConsSplitTFourPLo` | 0.94 | lower 95% CI bound of \LocAucProbeConsSplitTFourP |
| `\LocAucProbeConsSplitTFourPHi` | 0.97 | upper 95% CI bound of \LocAucProbeConsSplitTFourP |
| `\LocAucPplGptTZero` | 0.39 | AUROC of ppl_gpt2 for T0 vs matched genuine notes (all instances); n+=300, n-=300 |
| `\LocAucPplGptTZeroLo` | 0.37 | lower 95% CI bound of \LocAucPplGptTZero |
| `\LocAucPplGptTZeroHi` | 0.40 | upper 95% CI bound of \LocAucPplGptTZero |
| `\LocAucPplGptTOne` | 0.48 | AUROC of ppl_gpt2 for T1 vs matched genuine notes (all instances); n+=254, n-=254 |
| `\LocAucPplGptTOneLo` | 0.46 | lower 95% CI bound of \LocAucPplGptTOne |
| `\LocAucPplGptTOneHi` | 0.51 | upper 95% CI bound of \LocAucPplGptTOne |
| `\LocAucPplGptTTwo` | 0.50 | AUROC of ppl_gpt2 for T2 vs matched genuine notes (all instances); n+=290, n-=290 |
| `\LocAucPplGptTTwoLo` | 0.48 | lower 95% CI bound of \LocAucPplGptTTwo |
| `\LocAucPplGptTTwoHi` | 0.52 | upper 95% CI bound of \LocAucPplGptTTwo |
| `\LocAucPplGptTTwoR` | 0.52 | AUROC of ppl_gpt2 for T2r vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucPplGptTTwoRLo` | 0.50 | lower 95% CI bound of \LocAucPplGptTTwoR |
| `\LocAucPplGptTTwoRHi` | 0.55 | upper 95% CI bound of \LocAucPplGptTTwoR |
| `\LocAucPplGptTThree` | 0.53 | AUROC of ppl_gpt2 for T3 vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucPplGptTThreeLo` | 0.51 | lower 95% CI bound of \LocAucPplGptTThree |
| `\LocAucPplGptTThreeHi` | 0.56 | upper 95% CI bound of \LocAucPplGptTThree |
| `\LocAucPplGptTFourS` | 0.49 | AUROC of ppl_gpt2 for T4s vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucPplGptTFourSLo` | 0.48 | lower 95% CI bound of \LocAucPplGptTFourS |
| `\LocAucPplGptTFourSHi` | 0.51 | upper 95% CI bound of \LocAucPplGptTFourS |
| `\LocAucPplGptTFourD` | 0.57 | AUROC of ppl_gpt2 for T4d vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucPplGptTFourDLo` | 0.55 | lower 95% CI bound of \LocAucPplGptTFourD |
| `\LocAucPplGptTFourDHi` | 0.59 | upper 95% CI bound of \LocAucPplGptTFourD |
| `\LocAucPplGptTFourC` | 0.54 | AUROC of ppl_gpt2 for T4c vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucPplGptTFourCLo` | 0.52 | lower 95% CI bound of \LocAucPplGptTFourC |
| `\LocAucPplGptTFourCHi` | 0.56 | upper 95% CI bound of \LocAucPplGptTFourC |
| `\LocAucPplGptTFourP` | 0.52 | AUROC of ppl_gpt2 for T4p vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucPplGptTFourPLo` | 0.49 | lower 95% CI bound of \LocAucPplGptTFourP |
| `\LocAucPplGptTFourPHi` | 0.54 | upper 95% CI bound of \LocAucPplGptTFourP |
| `\LocAucPplSmallTZero` | 0.42 | AUROC of ppl_small for T0 vs matched genuine notes (all instances); n+=300, n-=300 |
| `\LocAucPplSmallTZeroLo` | 0.41 | lower 95% CI bound of \LocAucPplSmallTZero |
| `\LocAucPplSmallTZeroHi` | 0.44 | upper 95% CI bound of \LocAucPplSmallTZero |
| `\LocAucPplSmallTOne` | 0.54 | AUROC of ppl_small for T1 vs matched genuine notes (all instances); n+=254, n-=254 |
| `\LocAucPplSmallTOneLo` | 0.52 | lower 95% CI bound of \LocAucPplSmallTOne |
| `\LocAucPplSmallTOneHi` | 0.56 | upper 95% CI bound of \LocAucPplSmallTOne |
| `\LocAucPplSmallTTwo` | 0.55 | AUROC of ppl_small for T2 vs matched genuine notes (all instances); n+=290, n-=290 |
| `\LocAucPplSmallTTwoLo` | 0.53 | lower 95% CI bound of \LocAucPplSmallTTwo |
| `\LocAucPplSmallTTwoHi` | 0.57 | upper 95% CI bound of \LocAucPplSmallTTwo |
| `\LocAucPplSmallTTwoR` | 0.58 | AUROC of ppl_small for T2r vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucPplSmallTTwoRLo` | 0.56 | lower 95% CI bound of \LocAucPplSmallTTwoR |
| `\LocAucPplSmallTTwoRHi` | 0.61 | upper 95% CI bound of \LocAucPplSmallTTwoR |
| `\LocAucPplSmallTThree` | 0.58 | AUROC of ppl_small for T3 vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucPplSmallTThreeLo` | 0.56 | lower 95% CI bound of \LocAucPplSmallTThree |
| `\LocAucPplSmallTThreeHi` | 0.61 | upper 95% CI bound of \LocAucPplSmallTThree |
| `\LocAucPplSmallTFourS` | 0.53 | AUROC of ppl_small for T4s vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucPplSmallTFourSLo` | 0.52 | lower 95% CI bound of \LocAucPplSmallTFourS |
| `\LocAucPplSmallTFourSHi` | 0.55 | upper 95% CI bound of \LocAucPplSmallTFourS |
| `\LocAucPplSmallTFourD` | 0.62 | AUROC of ppl_small for T4d vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucPplSmallTFourDLo` | 0.60 | lower 95% CI bound of \LocAucPplSmallTFourD |
| `\LocAucPplSmallTFourDHi` | 0.64 | upper 95% CI bound of \LocAucPplSmallTFourD |
| `\LocAucPplSmallTFourC` | 0.59 | AUROC of ppl_small for T4c vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucPplSmallTFourCLo` | 0.57 | lower 95% CI bound of \LocAucPplSmallTFourC |
| `\LocAucPplSmallTFourCHi` | 0.61 | upper 95% CI bound of \LocAucPplSmallTFourC |
| `\LocAucPplSmallTFourP` | 0.57 | AUROC of ppl_small for T4p vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucPplSmallTFourPLo` | 0.55 | lower 95% CI bound of \LocAucPplSmallTFourP |
| `\LocAucPplSmallTFourPHi` | 0.60 | upper 95% CI bound of \LocAucPplSmallTFourP |
| `\LocAucLenCharsTZero` | 0.73 | AUROC of len_chars for T0 vs matched genuine notes (all instances); n+=300, n-=300 |
| `\LocAucLenCharsTZeroLo` | 0.71 | lower 95% CI bound of \LocAucLenCharsTZero |
| `\LocAucLenCharsTZeroHi` | 0.75 | upper 95% CI bound of \LocAucLenCharsTZero |
| `\LocAucLenCharsTOne` | 0.43 | AUROC of len_chars for T1 vs matched genuine notes (all instances); n+=254, n-=254 |
| `\LocAucLenCharsTOneLo` | 0.41 | lower 95% CI bound of \LocAucLenCharsTOne |
| `\LocAucLenCharsTOneHi` | 0.46 | upper 95% CI bound of \LocAucLenCharsTOne |
| `\LocAucLenCharsTTwo` | 0.47 | AUROC of len_chars for T2 vs matched genuine notes (all instances); n+=290, n-=290 |
| `\LocAucLenCharsTTwoLo` | 0.44 | lower 95% CI bound of \LocAucLenCharsTTwo |
| `\LocAucLenCharsTTwoHi` | 0.50 | upper 95% CI bound of \LocAucLenCharsTTwo |
| `\LocAucLenCharsTTwoR` | 0.50 | AUROC of len_chars for T2r vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucLenCharsTTwoRLo` | 0.48 | lower 95% CI bound of \LocAucLenCharsTTwoR |
| `\LocAucLenCharsTTwoRHi` | 0.53 | upper 95% CI bound of \LocAucLenCharsTTwoR |
| `\LocAucLenCharsTThree` | 0.50 | AUROC of len_chars for T3 vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucLenCharsTThreeLo` | 0.47 | lower 95% CI bound of \LocAucLenCharsTThree |
| `\LocAucLenCharsTThreeHi` | 0.53 | upper 95% CI bound of \LocAucLenCharsTThree |
| `\LocAucLenCharsTFourS` | 0.51 | AUROC of len_chars for T4s vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucLenCharsTFourSLo` | 0.49 | lower 95% CI bound of \LocAucLenCharsTFourS |
| `\LocAucLenCharsTFourSHi` | 0.54 | upper 95% CI bound of \LocAucLenCharsTFourS |
| `\LocAucLenCharsTFourD` | 0.46 | AUROC of len_chars for T4d vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucLenCharsTFourDLo` | 0.44 | lower 95% CI bound of \LocAucLenCharsTFourD |
| `\LocAucLenCharsTFourDHi` | 0.48 | upper 95% CI bound of \LocAucLenCharsTFourD |
| `\LocAucLenCharsTFourC` | 0.49 | AUROC of len_chars for T4c vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucLenCharsTFourCLo` | 0.47 | lower 95% CI bound of \LocAucLenCharsTFourC |
| `\LocAucLenCharsTFourCHi` | 0.52 | upper 95% CI bound of \LocAucLenCharsTFourC |
| `\LocAucLenCharsTFourP` | 0.58 | AUROC of len_chars for T4p vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucLenCharsTFourPLo` | 0.55 | lower 95% CI bound of \LocAucLenCharsTFourP |
| `\LocAucLenCharsTFourPHi` | 0.61 | upper 95% CI bound of \LocAucLenCharsTFourP |
| `\LocAucBowConsTZero` | 0.83 | AUROC of bow_P2 for T0 vs matched genuine notes (all instances); n+=300, n-=300 |
| `\LocAucBowConsTZeroLo` | 0.80 | lower 95% CI bound of \LocAucBowConsTZero |
| `\LocAucBowConsTZeroHi` | 0.86 | upper 95% CI bound of \LocAucBowConsTZero |
| `\LocAucBowConsTOne` | 0.76 | AUROC of bow_P2 for T1 vs matched genuine notes (all instances); n+=254, n-=254 |
| `\LocAucBowConsTOneLo` | 0.73 | lower 95% CI bound of \LocAucBowConsTOne |
| `\LocAucBowConsTOneHi` | 0.78 | upper 95% CI bound of \LocAucBowConsTOne |
| `\LocAucBowConsTTwo` | 0.77 | AUROC of bow_P2 for T2 vs matched genuine notes (all instances); n+=290, n-=290 |
| `\LocAucBowConsTTwoLo` | 0.75 | lower 95% CI bound of \LocAucBowConsTTwo |
| `\LocAucBowConsTTwoHi` | 0.79 | upper 95% CI bound of \LocAucBowConsTTwo |
| `\LocAucBowConsTTwoR` | 0.78 | AUROC of bow_P2 for T2r vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucBowConsTTwoRLo` | 0.75 | lower 95% CI bound of \LocAucBowConsTTwoR |
| `\LocAucBowConsTTwoRHi` | 0.81 | upper 95% CI bound of \LocAucBowConsTTwoR |
| `\LocAucBowConsTThree` | 0.78 | AUROC of bow_P2 for T3 vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucBowConsTThreeLo` | 0.75 | lower 95% CI bound of \LocAucBowConsTThree |
| `\LocAucBowConsTThreeHi` | 0.80 | upper 95% CI bound of \LocAucBowConsTThree |
| `\LocAucBowConsTFourS` | 0.76 | AUROC of bow_P2 for T4s vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucBowConsTFourSLo` | 0.74 | lower 95% CI bound of \LocAucBowConsTFourS |
| `\LocAucBowConsTFourSHi` | 0.78 | upper 95% CI bound of \LocAucBowConsTFourS |
| `\LocAucBowConsTFourD` | 0.76 | AUROC of bow_P2 for T4d vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucBowConsTFourDLo` | 0.74 | lower 95% CI bound of \LocAucBowConsTFourD |
| `\LocAucBowConsTFourDHi` | 0.79 | upper 95% CI bound of \LocAucBowConsTFourD |
| `\LocAucBowConsTFourC` | 0.76 | AUROC of bow_P2 for T4c vs matched genuine notes (all instances); n+=299, n-=299 |
| `\LocAucBowConsTFourCLo` | 0.73 | lower 95% CI bound of \LocAucBowConsTFourC |
| `\LocAucBowConsTFourCHi` | 0.78 | upper 95% CI bound of \LocAucBowConsTFourC |
| `\LocAucBowConsTFourP` | \textit{n/a} | AUROC of bow_P2 for T4p vs matched genuine notes (all instances); n+=None, n-=None (n/a: full-sample LOFO probe shares training episodes with the T4p attacker; use the split-half probe) |
| `\LocAucBowConsTFourPLo` | \textit{n/a} | lower 95% CI bound of \LocAucBowConsTFourP (n/a: full-sample LOFO probe shares training episodes with the T4p attacker; use the split-half probe) |
| `\LocAucBowConsTFourPHi` | \textit{n/a} | upper 95% CI bound of \LocAucBowConsTFourP (n/a: full-sample LOFO probe shares training episodes with the T4p attacker; use the split-half probe) |
| `\LocSelfAuthSurp` | 0.96 | AUROC own genuine vs other-model notes, s_trace_mean; n+=599, n-=300 |
| `\LocSelfAuthSurpLo` | 0.95 | lower CI of \LocSelfAuthSurp |
| `\LocSelfAuthSurpHi` | 0.97 | upper CI of \LocSelfAuthSurp |
| `\LocSelfAuthSurpBlind` | 0.85 | AUROC own genuine vs other-model notes, s_blind_mean; n+=599, n-=300 |
| `\LocSelfAuthSurpBlindLo` | 0.82 | lower CI of \LocSelfAuthSurpBlind |
| `\LocSelfAuthSurpBlindHi` | 0.87 | upper CI of \LocSelfAuthSurpBlind |
| `\LocSelfAuthSurpDelta` | 0.44 | AUROC own genuine vs other-model notes, s_delta; n+=599, n-=300 |
| `\LocSelfAuthSurpDeltaLo` | 0.41 | lower CI of \LocSelfAuthSurpDelta |
| `\LocSelfAuthSurpDeltaHi` | 0.47 | upper CI of \LocSelfAuthSurpDelta |
| `\LocSelfAuthPplGpt` | 0.74 | AUROC own genuine vs other-model notes, ppl_gpt2; n+=599, n-=300 |
| `\LocSelfAuthPplGptLo` | 0.71 | lower CI of \LocSelfAuthPplGpt |
| `\LocSelfAuthPplGptHi` | 0.77 | upper CI of \LocSelfAuthPplGpt |
| `\LocSelfAuthProbeSelf` | 1.00 | AUROC own genuine vs other-model notes, P1; n+=599, n-=300 |
| `\LocSelfAuthProbeSelfLo` | 1.00 | lower CI of \LocSelfAuthProbeSelf |
| `\LocSelfAuthProbeSelfHi` | 1.00 | upper CI of \LocSelfAuthProbeSelf |
| `\LocSelfAuthProbeSelfBlind` | 1.00 | AUROC own genuine vs other-model notes, P1_blind; n+=599, n-=300 |
| `\LocSelfAuthProbeSelfBlindLo` | 0.99 | lower CI of \LocSelfAuthProbeSelfBlind |
| `\LocSelfAuthProbeSelfBlindHi` | 1.00 | upper CI of \LocSelfAuthProbeSelfBlind |
| `\LocSelfAuthBowSelf` | 0.99 | AUROC own genuine vs other-model notes, bow_P1; n+=599, n-=300 |
| `\LocSelfAuthBowSelfLo` | 0.99 | lower CI of \LocSelfAuthBowSelf |
| `\LocSelfAuthBowSelfHi` | 1.00 | upper CI of \LocSelfAuthBowSelf |
| `\LocSelfAuthLenChars` | 0.12 | AUROC own genuine vs other-model notes, len_chars; n+=599, n-=300 |
| `\LocSelfAuthLenCharsLo` | 0.11 | lower CI of \LocSelfAuthLenChars |
| `\LocSelfAuthLenCharsHi` | 0.14 | upper CI of \LocSelfAuthLenChars |
| `\LocProbeSelfTrace` | 1.00 | pooled out-of-fold AUROC of P1 (trace activations, mean-pooled, LOFO); n+=599, n-=300 |
| `\LocProbeSelfTraceLo` | 1.00 | lower CI of \LocProbeSelfTrace |
| `\LocProbeSelfTraceHi` | 1.00 | upper CI of \LocProbeSelfTrace |
| `\LocProbeSelfTraceShuf` | 0.50 | mean pooled AUROC of P1 (trace) over 5 shuffled-label refits |
| `\LocProbeSelfTraceLast` | 1.00 | pooled AUROC of P1 (trace) on last-token activations |
| `\LocProbeSelfTraceSplit` | 0.99 | pooled AUROC of the split-half P1 (trace) |
| `\LocProbeSelfBlind` | 1.00 | pooled out-of-fold AUROC of P1 (blind activations, mean-pooled, LOFO); n+=599, n-=300 |
| `\LocProbeSelfBlindLo` | 0.99 | lower CI of \LocProbeSelfBlind |
| `\LocProbeSelfBlindHi` | 1.00 | upper CI of \LocProbeSelfBlind |
| `\LocProbeSelfBlindShuf` | 0.48 | mean pooled AUROC of P1 (blind) over 5 shuffled-label refits |
| `\LocProbeSelfBlindLast` | 0.99 | pooled AUROC of P1 (blind) on last-token activations |
| `\LocProbeSelfBlindSplit` | 0.99 | pooled AUROC of the split-half P1 (blind) |
| `\LocBowSelf` | 0.99 | pooled AUROC of the bag-of-words + length baseline on the P1 task; n+=599, n-=300 |
| `\LocBowSelfLo` | 0.99 | lower CI of \LocBowSelf |
| `\LocBowSelfHi` | 1.00 | upper CI of \LocBowSelf |
| `\LocProbeConsTrace` | 0.97 | pooled out-of-fold AUROC of P2 (trace activations, mean-pooled, LOFO); n+=844, n-=300 |
| `\LocProbeConsTraceLo` | 0.96 | lower CI of \LocProbeConsTrace |
| `\LocProbeConsTraceHi` | 0.98 | upper CI of \LocProbeConsTrace |
| `\LocProbeConsTraceShuf` | 0.49 | mean pooled AUROC of P2 (trace) over 5 shuffled-label refits |
| `\LocProbeConsTraceLast` | 0.94 | pooled AUROC of P2 (trace) on last-token activations |
| `\LocProbeConsTraceSplit` | 0.95 | pooled AUROC of the split-half P2 (trace) |
| `\LocProbeConsBlind` | 0.86 | pooled out-of-fold AUROC of P2 (blind activations, mean-pooled, LOFO); n+=844, n-=300 |
| `\LocProbeConsBlindLo` | 0.84 | lower CI of \LocProbeConsBlind |
| `\LocProbeConsBlindHi` | 0.88 | upper CI of \LocProbeConsBlind |
| `\LocProbeConsBlindShuf` | 0.51 | mean pooled AUROC of P2 (blind) over 5 shuffled-label refits |
| `\LocProbeConsBlindLast` | 0.87 | pooled AUROC of P2 (blind) on last-token activations |
| `\LocProbeConsBlindSplit` | 0.83 | pooled AUROC of the split-half P2 (blind) |
| `\LocBowCons` | 0.79 | pooled AUROC of the bag-of-words + length baseline on the P2 task; n+=844, n-=300 |
| `\LocBowConsLo` | 0.77 | lower CI of \LocBowCons |
| `\LocBowConsHi` | 0.81 | upper CI of \LocBowCons |
| `\LocHFourSurpTFourS` | 0.96 | H4: AUROC of style signal s_trace_mean under its targeted tier T4s (common instances); n+=250, n-=250 |
| `\LocHFourSurpTFourSLo` | 0.95 | lower CI of \LocHFourSurpTFourS |
| `\LocHFourSurpTFourSHi` | 0.97 | upper CI of \LocHFourSurpTFourS |
| `\LocHFourProbeSelfSplitTFourP` | 0.38 | H4: AUROC of style signal P1h under its targeted tier T4p (common instances); n+=250, n-=250 |
| `\LocHFourProbeSelfSplitTFourPLo` | 0.36 | lower CI of \LocHFourProbeSelfSplitTFourP |
| `\LocHFourProbeSelfSplitTFourPHi` | 0.39 | upper CI of \LocHFourProbeSelfSplitTFourP |
| `\LocWorstSurpDelta` | 0.72 | worst-case AUROC of s_delta over the T4 tiers (at T4d) |
| `\LocWorstConsist` | 0.90 | worst-case AUROC of c over the T4 tiers (at T4c) |
| `\LocWorstProbeConsSplit` | 0.94 | worst-case AUROC of P2h over the T4 tiers (at T4s) |
| `\LocWorstSurp` | 0.96 | worst-case AUROC of s_trace_mean over the T4 tiers (at T4s) |
| `\LocWorstProbeSelfSplit` | 0.38 | worst-case AUROC of P1h over the T4 tiers (at T4p) |
| `\LocHFourBestTrace` | Probe P2 (split-half) | trace-based signal with the highest worst-case AUROC over T4 tiers |
| `\LocHFourTraceMinusStyle` | $-$0.03 | worst-case AUROC, best trace minus best style signal |
| `\LocHFourTraceMinusStyleLo` | $-$0.05 | lower CI of \LocHFourTraceMinusStyle |
| `\LocHFourTraceMinusStyleHi` | $-$0.00 | upper CI of \LocHFourTraceMinusStyle |
| `\LocGapBest` | Consistency $P(\text{yes})$ | trace-based detector chosen on calibration episodes for the local integrity gap |
| `\LocGapTThree` | $+$0.41 | integrity gap AUROC(c) - AUROC(verbal) at T3, evaluation episodes; n+=231, n-=231 |
| `\LocGapTThreeLo` | $+$0.39 | lower CI of \LocGapTThree |
| `\LocGapTThreeHi` | $+$0.43 | upper CI of \LocGapTThree |
| `\LocGapTFourS` | $+$0.36 | integrity gap AUROC(c) - AUROC(verbal) at T4s, evaluation episodes; n+=231, n-=231 |
| `\LocGapTFourSLo` | $+$0.33 | lower CI of \LocGapTFourS |
| `\LocGapTFourSHi` | $+$0.39 | upper CI of \LocGapTFourS |
| `\LocGapTFourD` | $+$0.35 | integrity gap AUROC(c) - AUROC(verbal) at T4d, evaluation episodes; n+=231, n-=231 |
| `\LocGapTFourDLo` | $+$0.33 | lower CI of \LocGapTFourD |
| `\LocGapTFourDHi` | $+$0.38 | upper CI of \LocGapTFourD |
| `\LocGapTFourC` | $+$0.34 | integrity gap AUROC(c) - AUROC(verbal) at T4c, evaluation episodes; n+=231, n-=231 |
| `\LocGapTFourCLo` | $+$0.31 | lower CI of \LocGapTFourC |
| `\LocGapTFourCHi` | $+$0.37 | upper CI of \LocGapTFourC |
| `\LocGapTFourP` | $+$0.38 | integrity gap AUROC(c) - AUROC(verbal) at T4p, evaluation episodes; n+=231, n-=231 |
| `\LocGapTFourPLo` | $+$0.36 | lower CI of \LocGapTFourP |
| `\LocGapTFourPHi` | $+$0.40 | upper CI of \LocGapTFourP |
| `\LocGapTFourPooled` | $+$0.36 | integrity gap AUROC(c) - AUROC(verbal) at T4_pooled, evaluation episodes; n+=924, n-=231 |
| `\LocGapTFourPooledLo` | $+$0.33 | lower CI of \LocGapTFourPooled |
| `\LocGapTFourPooledHi` | $+$0.38 | upper CI of \LocGapTFourPooled |
| `\LocShiftTThreeSurp` | $+$0.00 | AUROC change of s_trace_mean under rule T3 relative to T2r (n=299 instances) |
| `\LocShiftTThreeSurpSd` | $+$0.25 | mean oriented-score shift of s_trace_mean under T3 vs T2r, in genuine-SD units |
| `\LocShiftTThreeSurpBlind` | $+$0.00 | AUROC change of s_blind_mean under rule T3 relative to T2r (n=299 instances) |
| `\LocShiftTThreeSurpBlindSd` | $+$0.01 | mean oriented-score shift of s_blind_mean under T3 vs T2r, in genuine-SD units |
| `\LocShiftTThreeSurpDelta` | $+$0.01 | AUROC change of s_delta under rule T3 relative to T2r (n=299 instances) |
| `\LocShiftTThreeSurpDeltaSd` | $+$0.07 | mean oriented-score shift of s_delta under T3 vs T2r, in genuine-SD units |
| `\LocShiftTThreeConsist` | $-$0.01 | AUROC change of c under rule T3 relative to T2r (n=299 instances) |
| `\LocShiftTThreeConsistSd` | $-$0.05 | mean oriented-score shift of c under T3 vs T2r, in genuine-SD units |
| `\LocShiftTThreeVerbal` | $-$0.05 | AUROC change of v under rule T3 relative to T2r (n=299 instances) |
| `\LocShiftTThreeVerbalSd` | $-$0.21 | mean oriented-score shift of v under T3 vs T2r, in genuine-SD units |
| `\LocShiftTThreeProbeSelfSplit` | $-$0.01 | AUROC change of P1h under rule T3 relative to T2r (n=299 instances) |
| `\LocShiftTThreeProbeSelfSplitSd` | $-$0.03 | mean oriented-score shift of P1h under T3 vs T2r, in genuine-SD units |
| `\LocShiftTThreeProbeConsSplit` | $+$0.00 | AUROC change of P2h under rule T3 relative to T2r (n=299 instances) |
| `\LocShiftTThreeProbeConsSplitSd` | $+$0.11 | mean oriented-score shift of P2h under T3 vs T2r, in genuine-SD units |
| `\LocShiftTThreePplGpt` | $+$0.01 | AUROC change of ppl_gpt2 under rule T3 relative to T2r (n=299 instances) |
| `\LocShiftTThreePplGptSd` | $+$0.04 | mean oriented-score shift of ppl_gpt2 under T3 vs T2r, in genuine-SD units |
| `\LocShiftTThreePplSmall` | $+$0.00 | AUROC change of ppl_small under rule T3 relative to T2r (n=299 instances) |
| `\LocShiftTThreePplSmallSd` | $+$0.02 | mean oriented-score shift of ppl_small under T3 vs T2r, in genuine-SD units |
| `\LocShiftTThreeLenChars` | $-$0.00 | AUROC change of len_chars under rule T3 relative to T2r (n=299 instances) |
| `\LocShiftTThreeLenCharsSd` | $+$0.01 | mean oriented-score shift of len_chars under T3 vs T2r, in genuine-SD units |
| `\LocShiftTFourSSurp` | $-$0.01 | AUROC change of s_trace_mean under rule T4s relative to T2r (n=299 instances) |
| `\LocShiftTFourSSurpSd` | $-$2.51 | mean oriented-score shift of s_trace_mean under T4s vs T2r, in genuine-SD units |
| `\LocShiftTFourSSurpBlind` | $-$0.08 | AUROC change of s_blind_mean under rule T4s relative to T2r (n=299 instances) |
| `\LocShiftTFourSSurpBlindSd` | $-$0.34 | mean oriented-score shift of s_blind_mean under T4s vs T2r, in genuine-SD units |
| `\LocShiftTFourSSurpDelta` | $-$0.07 | AUROC change of s_delta under rule T4s relative to T2r (n=299 instances) |
| `\LocShiftTFourSSurpDeltaSd` | $-$0.48 | mean oriented-score shift of s_delta under T4s vs T2r, in genuine-SD units |
| `\LocShiftTFourSConsist` | $-$0.01 | AUROC change of c under rule T4s relative to T2r (n=299 instances) |
| `\LocShiftTFourSConsistSd` | $-$0.07 | mean oriented-score shift of c under T4s vs T2r, in genuine-SD units |
| `\LocShiftTFourSVerbal` | $-$0.01 | AUROC change of v under rule T4s relative to T2r (n=299 instances) |
| `\LocShiftTFourSVerbalSd` | $-$0.04 | mean oriented-score shift of v under T4s vs T2r, in genuine-SD units |
| `\LocShiftTFourSProbeSelfSplit` | $+$0.04 | AUROC change of P1h under rule T4s relative to T2r (n=299 instances) |
| `\LocShiftTFourSProbeSelfSplitSd` | $+$0.17 | mean oriented-score shift of P1h under T4s vs T2r, in genuine-SD units |
| `\LocShiftTFourSProbeConsSplit` | $-$0.02 | AUROC change of P2h under rule T4s relative to T2r (n=299 instances) |
| `\LocShiftTFourSProbeConsSplitSd` | $-$0.62 | mean oriented-score shift of P2h under T4s vs T2r, in genuine-SD units |
| `\LocShiftTFourSPplGpt` | $-$0.03 | AUROC change of ppl_gpt2 under rule T4s relative to T2r (n=299 instances) |
| `\LocShiftTFourSPplGptSd` | $-$0.09 | mean oriented-score shift of ppl_gpt2 under T4s vs T2r, in genuine-SD units |
| `\LocShiftTFourSPplSmall` | $-$0.05 | AUROC change of ppl_small under rule T4s relative to T2r (n=299 instances) |
| `\LocShiftTFourSPplSmallSd` | $-$0.17 | mean oriented-score shift of ppl_small under T4s vs T2r, in genuine-SD units |
| `\LocShiftTFourSLenChars` | $+$0.01 | AUROC change of len_chars under rule T4s relative to T2r (n=299 instances) |
| `\LocShiftTFourSLenCharsSd` | $-$0.00 | mean oriented-score shift of len_chars under T4s vs T2r, in genuine-SD units |
| `\LocShiftTFourDSurp` | $-$0.01 | AUROC change of s_trace_mean under rule T4d relative to T2r (n=299 instances) |
| `\LocShiftTFourDSurpSd` | $-$1.71 | mean oriented-score shift of s_trace_mean under T4d vs T2r, in genuine-SD units |
| `\LocShiftTFourDSurpBlind` | $+$0.02 | AUROC change of s_blind_mean under rule T4d relative to T2r (n=299 instances) |
| `\LocShiftTFourDSurpBlindSd` | $+$0.14 | mean oriented-score shift of s_blind_mean under T4d vs T2r, in genuine-SD units |
| `\LocShiftTFourDSurpDelta` | $-$0.11 | AUROC change of s_delta under rule T4d relative to T2r (n=299 instances) |
| `\LocShiftTFourDSurpDeltaSd` | $-$0.68 | mean oriented-score shift of s_delta under T4d vs T2r, in genuine-SD units |
| `\LocShiftTFourDConsist` | $-$0.01 | AUROC change of c under rule T4d relative to T2r (n=299 instances) |
| `\LocShiftTFourDConsistSd` | $-$0.12 | mean oriented-score shift of c under T4d vs T2r, in genuine-SD units |
| `\LocShiftTFourDVerbal` | $-$0.01 | AUROC change of v under rule T4d relative to T2r (n=299 instances) |
| `\LocShiftTFourDVerbalSd` | $-$0.03 | mean oriented-score shift of v under T4d vs T2r, in genuine-SD units |
| `\LocShiftTFourDProbeSelfSplit` | $+$0.05 | AUROC change of P1h under rule T4d relative to T2r (n=299 instances) |
| `\LocShiftTFourDProbeSelfSplitSd` | $+$0.20 | mean oriented-score shift of P1h under T4d vs T2r, in genuine-SD units |
| `\LocShiftTFourDProbeConsSplit` | $-$0.02 | AUROC change of P2h under rule T4d relative to T2r (n=299 instances) |
| `\LocShiftTFourDProbeConsSplitSd` | $-$0.51 | mean oriented-score shift of P2h under T4d vs T2r, in genuine-SD units |
| `\LocShiftTFourDPplGpt` | $+$0.05 | AUROC change of ppl_gpt2 under rule T4d relative to T2r (n=299 instances) |
| `\LocShiftTFourDPplGptSd` | $+$0.19 | mean oriented-score shift of ppl_gpt2 under T4d vs T2r, in genuine-SD units |
| `\LocShiftTFourDPplSmall` | $+$0.04 | AUROC change of ppl_small under rule T4d relative to T2r (n=299 instances) |
| `\LocShiftTFourDPplSmallSd` | $+$0.17 | mean oriented-score shift of ppl_small under T4d vs T2r, in genuine-SD units |
| `\LocShiftTFourDLenChars` | $-$0.04 | AUROC change of len_chars under rule T4d relative to T2r (n=299 instances) |
| `\LocShiftTFourDLenCharsSd` | $-$0.21 | mean oriented-score shift of len_chars under T4d vs T2r, in genuine-SD units |
| `\LocShiftTFourCSurp` | $-$0.00 | AUROC change of s_trace_mean under rule T4c relative to T2r (n=299 instances) |
| `\LocShiftTFourCSurpSd` | $-$0.64 | mean oriented-score shift of s_trace_mean under T4c vs T2r, in genuine-SD units |
| `\LocShiftTFourCSurpBlind` | $-$0.01 | AUROC change of s_blind_mean under rule T4c relative to T2r (n=299 instances) |
| `\LocShiftTFourCSurpBlindSd` | $-$0.00 | mean oriented-score shift of s_blind_mean under T4c vs T2r, in genuine-SD units |
| `\LocShiftTFourCSurpDelta` | $-$0.03 | AUROC change of s_delta under rule T4c relative to T2r (n=299 instances) |
| `\LocShiftTFourCSurpDeltaSd` | $-$0.21 | mean oriented-score shift of s_delta under T4c vs T2r, in genuine-SD units |
| `\LocShiftTFourCConsist` | $-$0.06 | AUROC change of c under rule T4c relative to T2r (n=299 instances) |
| `\LocShiftTFourCConsistSd` | $-$0.58 | mean oriented-score shift of c under T4c vs T2r, in genuine-SD units |
| `\LocShiftTFourCVerbal` | $-$0.04 | AUROC change of v under rule T4c relative to T2r (n=299 instances) |
| `\LocShiftTFourCVerbalSd` | $-$0.14 | mean oriented-score shift of v under T4c vs T2r, in genuine-SD units |
| `\LocShiftTFourCProbeSelfSplit` | $+$0.02 | AUROC change of P1h under rule T4c relative to T2r (n=299 instances) |
| `\LocShiftTFourCProbeSelfSplitSd` | $+$0.08 | mean oriented-score shift of P1h under T4c vs T2r, in genuine-SD units |
| `\LocShiftTFourCProbeConsSplit` | $-$0.01 | AUROC change of P2h under rule T4c relative to T2r (n=299 instances) |
| `\LocShiftTFourCProbeConsSplitSd` | $-$0.32 | mean oriented-score shift of P2h under T4c vs T2r, in genuine-SD units |
| `\LocShiftTFourCPplGpt` | $+$0.02 | AUROC change of ppl_gpt2 under rule T4c relative to T2r (n=299 instances) |
| `\LocShiftTFourCPplGptSd` | $+$0.07 | mean oriented-score shift of ppl_gpt2 under T4c vs T2r, in genuine-SD units |
| `\LocShiftTFourCPplSmall` | $+$0.01 | AUROC change of ppl_small under rule T4c relative to T2r (n=299 instances) |
| `\LocShiftTFourCPplSmallSd` | $+$0.04 | mean oriented-score shift of ppl_small under T4c vs T2r, in genuine-SD units |
| `\LocShiftTFourCLenChars` | $-$0.01 | AUROC change of len_chars under rule T4c relative to T2r (n=299 instances) |
| `\LocShiftTFourCLenCharsSd` | $-$0.06 | mean oriented-score shift of len_chars under T4c vs T2r, in genuine-SD units |
| `\LocShiftTFourPSurp` | $+$0.00 | AUROC change of s_trace_mean under rule T4p relative to T2r (n=299 instances) |
| `\LocShiftTFourPSurpSd` | $+$1.29 | mean oriented-score shift of s_trace_mean under T4p vs T2r, in genuine-SD units |
| `\LocShiftTFourPSurpBlind` | $+$0.01 | AUROC change of s_blind_mean under rule T4p relative to T2r (n=299 instances) |
| `\LocShiftTFourPSurpBlindSd` | $+$0.03 | mean oriented-score shift of s_blind_mean under T4p vs T2r, in genuine-SD units |
| `\LocShiftTFourPSurpDelta` | $+$0.04 | AUROC change of s_delta under rule T4p relative to T2r (n=299 instances) |
| `\LocShiftTFourPSurpDeltaSd` | $+$0.39 | mean oriented-score shift of s_delta under T4p vs T2r, in genuine-SD units |
| `\LocShiftTFourPConsist` | $+$0.01 | AUROC change of c under rule T4p relative to T2r (n=299 instances) |
| `\LocShiftTFourPConsistSd` | $+$0.09 | mean oriented-score shift of c under T4p vs T2r, in genuine-SD units |
| `\LocShiftTFourPVerbal` | $-$0.01 | AUROC change of v under rule T4p relative to T2r (n=299 instances) |
| `\LocShiftTFourPVerbalSd` | $-$0.04 | mean oriented-score shift of v under T4p vs T2r, in genuine-SD units |
| `\LocShiftTFourPProbeSelfSplit` | $-$0.07 | AUROC change of P1h under rule T4p relative to T2r (n=299 instances) |
| `\LocShiftTFourPProbeSelfSplitSd` | $-$0.30 | mean oriented-score shift of P1h under T4p vs T2r, in genuine-SD units |
| `\LocShiftTFourPProbeConsSplit` | $+$0.01 | AUROC change of P2h under rule T4p relative to T2r (n=299 instances) |
| `\LocShiftTFourPProbeConsSplitSd` | $+$0.38 | mean oriented-score shift of P2h under T4p vs T2r, in genuine-SD units |
| `\LocShiftTFourPPplGpt` | $-$0.01 | AUROC change of ppl_gpt2 under rule T4p relative to T2r (n=299 instances) |
| `\LocShiftTFourPPplGptSd` | $-$0.04 | mean oriented-score shift of ppl_gpt2 under T4p vs T2r, in genuine-SD units |
| `\LocShiftTFourPPplSmall` | $-$0.01 | AUROC change of ppl_small under rule T4p relative to T2r (n=299 instances) |
| `\LocShiftTFourPPplSmallSd` | $-$0.04 | mean oriented-score shift of ppl_small under T4p vs T2r, in genuine-SD units |
| `\LocShiftTFourPLenChars` | $+$0.07 | AUROC change of len_chars under rule T4p relative to T2r (n=299 instances) |
| `\LocShiftTFourPLenCharsSd` | $+$0.38 | mean oriented-score shift of len_chars under T4p vs T2r, in genuine-SD units |
