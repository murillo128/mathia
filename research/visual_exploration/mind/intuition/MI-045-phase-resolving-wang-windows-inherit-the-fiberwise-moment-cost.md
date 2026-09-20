# MI-045 — Phase-resolving Wang windows inherit the fiberwise moment cost

**Evidence level:** exact harmonic-analysis synthesis from [VIS-343](../../findings/VIS-343-wang-dilate-mixture-cancellation-order.md), [VIS-344](../../findings/VIS-344-wang-translated-dilate-cancellation-fibers.md), and [VIS-345](../../findings/VIS-345-long-window-phase-resolution.md), using the explicit finite exponential-sum frame bound derived in VIS-345. This is a multiplier obstruction for fixed translated-dilate banks, not a source-specific estimate for the theta remainder.

For

`M(xi)=sum_j c_j exp(-i b_j xi)m(a_j xi)`,

let `b_1,...,b_B` be the distinct active translations, `Delta=min_(p!=q)|b_p-b_q|`, and

`S_(b,k)=sum_(j:b_j=b)c_j a_j^(-k)`.

After the lower moments in each translation fiber vanish through order `k-1`, Wang's large-frequency expansion reduces the next order to

`xi^k M(xi)=beta_k P_k(xi)+O(X^(-1))`,

on `xi in [X,2X]`, where

`P_k(xi)=sum_b S_(b,k) exp(-i b xi)`.

On any interval `I=[X,X+L] subset [X,2X]`, direct integration of this finite exponential polynomial gives

`RMS_I(P_k)^2 >= [1-2(B-1)/(L Delta)] sum_b |S_(b,k)|^2`.

Hence, when

`L Delta >= 4(B-1)`,

`RMS_I(xi^k M(xi)) >= (|beta_k|/sqrt(2)) (sum_b |S_(b,k)|^2)^(1/2) - C_k/X`.

The interval location does not enter the lower frame constant. Destructive interference can occur at selected frequencies, but once the window resolves the beat spacing of the translation phases it cannot keep the whole exponential polynomial small unless the coefficient vector itself is small.

Therefore a fixed separated bank cannot evade VIS-344 merely by using moving windows. If windows `I_X subset [X,2X]` satisfy the phase-resolution condition and `sup_(I_X)|M|=O(X^(-r))`, induction in `k` forces

`S_(b,k)=0` for every active `b` and `k=1,...,r-1`.

The within-fiber Vandermonde cost then returns: every active translation fiber that contributes order `r` needs at least `r` distinct scales. A moving-window construction is a genuinely different asymptotic resource only when its windows stay unresolved relative to the phase geometry or when the bank itself changes in a way that invalidates the fixed-frame estimate.

For a scale-dependent family, the explicit escape parameter is `L_X Delta_X/B_X`. Remaining possibilities include `L_X Delta_X` staying comparable to or below `B_X`, `Delta_X->0`, scale-dependent coefficients or scales whose conditioning/remainder constants deteriorate, frequency- or source-dependent coefficients, and signed estimates for `G` that do not require the multiplier to be uniformly small on the whole interval. Each route has a quantitative cost that cannot be hidden under the label “finite-window localization.”

**Boundary.** The frame bound is sufficient, not claimed sharp, and concerns finite fixed banks with distinct real translations. It does not rule out short unresolved windows, clustered translations, adaptive banks, infinite expansions or arithmetic cancellation coupled directly to `G`. No prime-number-theorem or RH consequence follows.