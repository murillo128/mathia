# MI-011 — Sequential elimination leaves two angle channels, and mean-square local leakage is enough for the direct endpoint

**Evidence level:** exact on every finite strictly positive canonical section through PF-318. Compatible infinite-section realization, the required Hilbert--Schmidt leakage estimate, and the independent conditional channel remain open.

PF-315--PF-316 reduce the physical low/high angle to the pair `(T_H,Z_LH)`. The residual map `V_H` is not a third endpoint regularizer: if it attenuates a conditional direction, the defect is quadratically controlled by the direct angle, and weak trace of the full angle is equivalent to weak trace of both channels.

PF-317 localizes `Z_LH`. In simultaneous seam-energy coordinates the positive precision is `I+K` with `K>=0`; diagonal completion factors are contractions, so `s_j(Z_LH)<=s_j(K_LH)`. Nearest-neighbor cuff topology leaves only the three offsets `r=-1,0,1`, each an orthogonal direct sum of local high-to-nonconstant-low pant blocks.

PF-318 lowers the actual endpoint burden. Because each retained low target has rank only `O(1+log P_n)`, no pointwise operator bound `||L_(n+r) K H_n||=O(P_n^(-1))` is required. It is enough that

`||L_(n+r) K H_n||_(S_2)^2 <= C (1+log P_n)/P_n^2`.

Threshold counting uses rank below `P_n<=sigma^(-1)` and Hilbert--Schmidt mass above it; Chebyshev prime density and the tail `sum_(p>X)(1+log p)/p^2=O(X^(-1))` then give the required `O(sigma^(-1))` singular count. Individual local singular values may be larger than `1/P_n` by a `sqrt(log P_n)` factor without spoiling weak trace.

By self-adjointness, the Hilbert--Schmidt quantity is exactly aggregate high-frequency leakage of an orthonormal basis of the retained low target. The direct channel has therefore become an **average-square local Fourier/DtN leakage problem**, not a worst-input operator-norm problem. PF-215 remains the negative control: the complete adjacent pant block diverges on constant modes, so the estimate must still exploit the physical frequency split.

**Boundary.** PF-318 does not prove the local Hilbert--Schmidt estimate, estimate `T_H`, construct the compatible infinite operator, close the symmetric side, or supply signed target composition. It only identifies a strictly weaker endpoint-complete local criterion for `Z_LH`.