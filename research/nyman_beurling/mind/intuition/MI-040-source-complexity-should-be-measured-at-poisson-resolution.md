# MI-040 — Source complexity should be measured at Poisson resolution

**Evidence level:** exact source-side synthesis from [NB-167](../../findings/NB-167-capped-poisson-transport-is-the-source-resolution.md), [NB-168](../../findings/NB-168-stationary-arithmetic-rescue-is-density-sparse.md), [NB-172](../../findings/NB-172-low-range-entropy-suppresses-arbitrary-height-adaptation.md), [NB-173](../../findings/NB-173-low-source-rank-suppresses-arbitrarily-adaptive-height-selection.md), and [NB-174](../../findings/NB-174-poisson-resolution-approximate-source-complexity-suppresses-adaptive-rescue.md).

Exact linear rank is too brittle for an arithmetic source that already identifies a finite resolution. Near `Re s=1`, NB-167 shows that compact signed templates differing by capped Poisson transport much smaller than `q_T log T/H_T` cannot change the Euler response at the logarithmic rescue scale. Source complexity should therefore quotient out motion below that resolution before exact rank or catalogue size is charged.

NB-174 implements this directly. Represent each height-dependent template as a combination of stationary normalized directions plus a residual whose normalized capped-Poisson size is at most `epsilon`. Minimize the dictionary rank times worst coefficient `ell^2` energy over all such representations; call the result `mathfrak L_T(epsilon)`. When `epsilon` is below a fixed fraction of `log T/H_T`, the residual can consume only a fixed fraction of the rescue margin and the stationary core obeys the same mean-square bound as in NB-173.

Hence positive-density logarithmic rescue requires `mathfrak L_T(epsilon_T)` of order at least `log^2 T` outside the inherited ultra-thin regime. The statement allows arbitrary height-dependent selection, including nonmeasurable choices; only the realized source geometry is charged.

The approximate currency unifies the previous unordered compressions without identifying them. At zero tolerance it is the exact linear complexity of NB-173. At positive tolerance it satisfies

`(X_T-epsilon)_+^2 <= mathfrak L_T(epsilon) <= N_T(epsilon) X_T^2`,

so a small source-resolution covering number guarantees small approximate linear complexity, while the converse can fail dramatically. A continuous, high-entropy family may remain near a low-dimensional stationary span.

The reusable lesson is that **representation complexity is meaningful only after quotienting directions invisible to the source at the destination scale**. Exact rank, exact catalogue size and microscopic parameter variation can all overcount. Conversely, description length can undercount: a concise nonlinear rule may generate large stable approximate source complexity.

The next useful theorem would characterize `mathfrak L_T(epsilon_T)` for an intrinsic nonlinear arithmetic family, or give a dual lower bound that proves large source-resolvable complexity rather than merely large syntactic complexity.

**Boundary.** NB-174 remains a density obstruction inherited from the stationary mean-square theorem. Large approximate complexity is necessary, not sufficient, for rescue; the stationary responses can still be correlated or arithmetically ineffective. The result does not close sparse exceptional heights or the ultra-thin exterior regime and does not itself solve the Nyman target approximation problem.