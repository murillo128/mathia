# MI-011 — Exact local source consistency can hide forced nonlocal mass or preserve a pre-compression joint defect

**Evidence level:** supported by NB-066--NB-070 and RE-068--RE-072; no operator or estimate is transferred between the lines.

Nyman--Beurling and Robin Extremal expose different staged failures of “local matching implies global harmlessness.”

In Nyman, NB-066--NB-067 make the stable-tail obstruction a global continuation cost visible through finite Schur complements. NB-068 showed that zero one-cell memory and fixed finite Gram bandwidth do not prevent a hidden boundary mode. NB-069 then adds the exact source covariance: canonical innovations obey integer-dilation branching, and uniformly bounded fixed-band nonorthogonality is incompatible with that law.

NB-070 strengthens the source-matched restriction. Exact branching transports every nonzero coarse correlation into at least linear absolute Gram mass across every descendant block pair. Under uniform innovation bounds, vanishing uniform absolute row tails force orthogonality. Thus any surviving nonorthogonal matched obstruction must carry order-one aggregate absolute correlation arbitrarily far from the diagonal; rapidly decaying long-range repairs are not enough. The unresolved step is signed: the forced far mass may still cancel in the block averages and Schur complement.

In Robin, RE-068 fixes the prime multiset exactly and RE-069 suppresses direct timing through the final kernel. RE-070--RE-071 find a surviving selector geometry that drives `H_vartheta` upward and `E_l` downward across one matched packet. RE-072 shows that the same orientation persists through an entire consecutive matched first-layer fan: the intervening fixed-state cells have the same signs, so the run accumulates a one-sided Chebyshev--Mertens ledger with no internal cancellation. Positive threshold width itself has a quantitative Chebyshev excursion cost.

The common discipline is now sharper: **match the exact source covariance first, then ask what global quantity that covariance forces before the destination compression**. In Nyman the source law forbids localization by forcing far correlation mass; in Robin the adaptive selector forbids internal cancellation by forcing a monotone error ledger. Neither statement is yet the final target inequality, because signs/phases in the Nyman continuation and global prime-error capacity in Robin remain unresolved.

**Boundary.** No Nyman Schur theorem transfers to Robin prime errors, and no Chebyshev--Mertens drift theorem transfers to Nyman continuation. The synthesis concerns the staged source/destination test and the fact that locally harmless representations can be globally constrained by exact source covariance.