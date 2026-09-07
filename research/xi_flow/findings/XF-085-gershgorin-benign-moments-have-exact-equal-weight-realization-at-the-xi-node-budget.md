# XF-085 — Gershgorin-benign moments have exact equal-weight realization at the Xi node budget

**Status:** `EXACT-DERIVED` + `CLASSICAL-QUADRATURE-BRIDGE` + `CONDITIONAL-XI-BUDGET` + `STRUCTURAL/REPAIR`. XF-084 reduced the live real-divisor existence problem to an equal-weight trigonometric moment problem and left the equal-weight constraint open even in its Gershgorin-benign regime. In that same regime the constraint can in fact be closed exactly. If the prescribed source-visible raw moments `Q_m` obey a fixed normalized `ell^1` margin

\[
\boxed{
2\sum_{m\in S}|Q_m|\le (1-\kappa)N,
\qquad \kappa>0,
}
\tag{1}
\]

for some visible set `S subset {1,...,K}`, then there is a constant `C_kappa` depending only on `kappa` such that every integer

\[
N\ge C_\kappa K
\tag{2}
\]

admits **exactly `N` unit-circle nodes** whose normalized moments equal `Q_m/N` on `S` and vanish on the unconstrained modes in `{1,...,K}\setminus S`. Thus the corresponding degree-`N` periodic real-divisor carrier reproduces every XF-079 sideband in `S` exactly. At the XF-083 scaling

\[
N=2D,
\qquad
K=O(D^{1/2}\log\log T)=o(D),
\tag{3}
\]

condition `(1)` with fixed `kappa` therefore makes the equal-weight carrier gate automatically feasible for all sufficiently large `T`. The remaining issue is no longer root placement in this cone, but proving that the transported Xi moments actually retain such a fixed margin, together with the separate heat-compatibility and positive-transition obligations.

## 1. The XF-084 margin itself produces a regular positive density

Extend the visible target by setting

\[
\mu_m:=\frac{Q_m}{N}\quad(m\in S),
\qquad
\mu_m:=0\quad(1\le m\le K,\ m\notin S),
\qquad
\mu_{-m}:=\overline{\mu_m}.
\tag{4}
\]

Define the real trigonometric polynomial

\[
W(\theta)
:=
1+\sum_{m=1}^{K}
\left(\mu_m e^{im\theta}+\overline{\mu_m}e^{-im\theta}\right)
=
1+2\operatorname{Re}\sum_{m=1}^{K}\mu_m e^{im\theta}.
\tag{5}
\]

Then

\[
\frac1{2\pi}\int_{-\pi}^{\pi}W(\theta)\,d\theta=1,
\qquad
\frac1{2\pi}\int_{-\pi}^{\pi}e^{-im\theta}W(\theta)\,d\theta=\mu_m
\quad(1\le m\le K).
\tag{6}
\]

Condition `(1)` is exactly

\[
2\sum_{m=1}^{K}|\mu_m|\le1-\kappa.
\tag{7}
\]

Hence, pointwise on the circle,

\[
\boxed{
\kappa\le W(\theta)\le2-\kappa.
}
\tag{8}
\]

This is stronger than merely passing the Toeplitz PSD test of XF-084: it gives an explicit absolutely continuous representing measure with a uniform positive floor and ceiling. In particular `W` is a periodic doubling weight. A direct interval comparison gives a doubling constant bounded only in terms of `kappa`, for example

\[
L_\kappa\le \frac{2(2-\kappa)}{\kappa}.
\tag{9}
\]

The construction is deliberately compatible with XF-070's quotient logic: modes not seen by the source selector are set to zero rather than being treated as hidden constraints.

## 2. Doubling-weight quadrature converts the density into exactly `N` equal atoms

For a periodic weight `W`, Gilboa--Peled define

\[
R_W^{\rm trig}(K)
:=
\frac{\int_{-\pi}^{\pi}W(\theta)\,d\theta}
{\inf_x\int_{x-1/K}^{x+1/K}W(\theta)\,d\theta}.
\tag{10}
\]

From `(8)`,

\[
\inf_x\int_{x-1/K}^{x+1/K}W(\theta)\,d\theta
\ge \frac{2\kappa}{K},
\tag{11}
\]

and therefore

\[
\boxed{
R_W^{\rm trig}(K)\le\frac{\pi K}{\kappa}.
}
\tag{12}
\]

Theorem 1.2 of Gilboa--Peled gives, for a periodic doubling weight of doubling constant `L`, an upper bound

\[
\overline N_W^{\rm trig}(K)
\le C(L)R_W^{\rm trig}(K),
\tag{13}
\]

where `\overline N_W^{\rm trig}(K)` is the least threshold such that a Chebyshev-type trigonometric quadrature of degree `K` exists for **every** prescribed node count above that threshold. Combining `(9)`, `(12)`, and `(13)` yields a constant `C_kappa` such that every integer `N>=C_kappa K` admits nodes `theta_1,...,theta_N` with equal weights satisfying

\[
\frac1N\sum_{j=1}^{N}p(\theta_j)
=
\frac1{2\pi}\int_{-\pi}^{\pi}p(\theta)W(\theta)\,d\theta
\tag{14}
\]

for every trigonometric polynomial of degree at most `K`.

Taking `p(\theta)=e^{-im\theta}` in `(14)` and using `(6)` gives

\[
\boxed{
\frac1N\sum_{j=1}^{N}e^{-im\theta_j}
=\mu_m
=\frac{Q_m}{N}
\quad(m\in S),
}
\tag{15}
\]

and the same average is zero on the completed modes outside `S`. With `nu_j=e^{i\theta_j}`, `(15)` is exactly the equal-weight unit-circle moment condition isolated in XF-084. Multiplying by `N`, the carrier power sums are `P_m=Q_m` on every visible mode.

There is no circular dependence hidden here. The density `W` depends on the normalized targets `Q_m/N`, but the uniform bounds `(8)`--`(12)` depend only on the fixed margin `kappa`; consequently the node threshold `C_kappa K` is uniform in `N` and in the particular target vector satisfying `(1)`.

## 3. The Xi node budget is asymptotically more than sufficient

XF-083 works with

\[
N=2D,
\qquad
K=O(D^{1/2}\log\log T).
\tag{16}
\]

In particular `K/N -> 0`. For each fixed `kappa>0`, equation `(2)` therefore holds automatically for sufficiently large `T`. Consequently, throughout the fixed-margin cone `(1)`, the degree constraint left open in XF-084 disappears asymptotically:

\[
\boxed{
\text{fixed normalized }\ell^1\text{ margin}
\;\Longrightarrow\;
\text{exact degree-}N\text{ equal-weight real-divisor realization}.
}
\tag{17}
\]

This is stronger than the weighted-measure relaxation and much stronger than rounding arbitrary atomic weights. The moments seen by XF-079 are matched **exactly**, so the `O(K)` power-sum error from naive weight quantization in XF-084 never appears. In this regime one also does not need the exponentially accurate whole-function approximation of XF-083 merely to manufacture the selector prefix: the finite sideband data themselves have an exact real-divisor realization.

## 4. Stress tests and evidence boundary

The fixed floor `kappa>0` is load-bearing. If `kappa=kappa(T)` tends to zero, the doubling constant and the Gilboa--Peled threshold may deteriorate, and `N/K->infinity` alone does not imply that the exact-`N` quadrature remains available. Equation `(17)` is therefore a uniform-interior theorem, not a boundary theorem for the full Toeplitz cone.

Condition `(1)` is sufficient, not necessary. Many PSD moment vectors violate the coefficient `ell^1` bound while still admitting regular positive representing measures or even exact equal-weight realizations. The general XF-084 PSD-completion/equal-weight problem remains open outside this benign cone.

Repeated nodes are harmless for the present moment gate because XF-084's carrier measure counts multiplicity. This finding does not assert root simplicity. More importantly, an exact real-divisor carrier at one slice is not yet an Xi-flow bridge: it does not show that the selected moments arise from the transported Xi quotient, that the carrier evolves compatibly with the required heat interval, or that a hypothetical `Lambda>0` transition leaves nonzero mass in the guarded destination norm.

## 5. Prior art and novelty boundary

The load-bearing external theorem is Shoni Gilboa and Ron Peled, **Chebyshev-Type Quadratures for Doubling Weights**, *Constructive Approximation* 45:2 (2017), 193--216, DOI `10.1007/s00365-016-9360-4`, arXiv:1507.01505. Their Theorem 1.2 gives the exact-node-count Chebyshev-type trigonometric quadrature bound for periodic doubling weights used in `(13)`. Equal-weight trigonometric quadrature itself is classical, and no novelty is claimed for that theorem.

The line-specific step is the observation that XF-084's own Gershgorin margin `(1)` canonically manufactures the bounded positive density `(5)`, whose doubling and local-mass constants are uniform in the Xi scaling. This turns the previously open equal-weight degree constraint into the exact realization theorem `(17)`. `SOURCES.md` is updated because the Gilboa--Peled theorem is now load-bearing rather than merely neighboring prior art.

## 6. Consequence for the live bridge

The proposed clue `CLUE-relative-xi-source-to-guarded-selector-stability` should remain `proposed`: this finding closes only a conditional algebraic existence gate. But it gives that clue a sharper next test. Instead of solving a nonlinear `N`-root placement problem first, estimate the transported source-visible moments and ask whether, after leaving the XF-070 infrared coordinates free,

\[
\boxed{
\frac{2}{N}\sum_{m\in S}|Q_m|
\le1-\kappa
}
\tag{18}
\]

holds with a fixed positive margin. If it does, the equal-weight real-divisor carrier exists exactly at the available `N=2D` budget for all sufficiently large scales. If it does not, the broader Toeplitz PSD completion and regular-measure route from XF-084 remains the correct fallback.

Thus the current frontier is no longer simply “can equal weights realize the visible moments?” In the uniform interior of the moment cone the answer is yes. The decisive source-side question is now whether the actual Xi-derived visible moment vector stays in that interior with quantitative margin through the required positive-time transport.