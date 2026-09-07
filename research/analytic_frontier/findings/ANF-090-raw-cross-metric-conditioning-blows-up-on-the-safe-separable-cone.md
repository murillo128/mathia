# ANF-090 — raw cross-metric conditioning blows up on the safe separable cone

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CROSS-METRIC-GRAM-GATE + SEPARABLE-CONE + FIXED-SEPARATION + FIXED-HEIGHT + GROWING-CARDINALITY`. `ANF-089` turns Montgomery--Taylor near-equality into the cross-metric bound

\[
d_{\rm sep}(W)^2
\le
\frac{\chi_s(W)}{2q_s}\frac{\Delta(W)}{L(W)},
\qquad
\chi_s(W)=\frac{b_s(W)}{a(W)},
\tag{1}
\]

and leaves open whether useful geometric classes admit a uniform bound on `chi_s`. There is a sharp obstruction to treating that raw ratio as an intrinsic nonseparability condition: **`chi_s` is unbounded, in fact exponentially large, on configurations that are themselves exactly separable and globally safe by `ANF-085`.** Fixed pairwise separation, fixed nonzero height, multiplicity one, and exact product center--height structure do not prevent the source Gram factor `a(W)` from becoming exponentially small as cardinality grows.

Fix the central-notch spectrum `J_s` and constant `q_s>0` used in `ANF-085`--`ANF-089`. For any fixed

\[
0<\delta<1,
\qquad
y>0,
\tag{2}
\]

and integer `n>=1`, define

\[
X_n:=\{0,\delta,2\delta,\ldots,n\delta\},
\qquad
Y:=\{-y,+y\},
\tag{3}
\]

and the conjugation-invariant product multiset

\[
W_n:=X_n+iY
=\{j\delta-iy,j\delta+iy:0\le j\le n\}.
\tag{4}
\]

Every point has multiplicity one, all nonreal heights are exactly `y`, and the full complex support has the fixed minimum separation

\[
\operatorname{sep}(W_n)=\min\{\delta,2y\}>0.
\tag{5}
\]

Put

\[
r_\delta:=\sin\frac{\pi\delta}{2}\in(0,1),
\qquad
A_y:=\int_{-1/2}^{1/2}\eta_{\rm MT}(u)^2e^{4\pi uy}\,du,
\tag{6}
\]

and

\[
B_{s,y}:=
4\int_{-1}^{1}J_s(\alpha)
\bigl(\cosh(2\pi\alpha y)-1\bigr)^2\,d\alpha>0.
\tag{7}
\]

Then the two Gram factors of `ANF-089` satisfy the explicit bounds

\[
\boxed{
a(W_n)\le A_y(2n+1)r_\delta^{2n},
\qquad
b_s(W_n)\ge B_{s,y}.
}
\tag{8}
\]

Consequently

\[
\boxed{
\chi_s(W_n)
\ge
\frac{B_{s,y}}{A_y(2n+1)}
\,r_\delta^{-2n}
\longrightarrow\infty
}
\tag{9}
\]

exponentially in `n`. Yet `W_n` is itself a product/separable multiset covered by `ANF-085`, so

\[
\boxed{
d_{\rm sep}(W_n)=0}
\tag{10}
\]

for every `n`, and the central-notch certificate is globally valid on the entire family. Thus large raw `chi_s` can occur arbitrarily deep inside the safe class; it is a one-sided proof constant for the particular real-collapse comparison used in `ANF-089`, not a geometric measure of distance from the separable cone.

## 1. A binomial finite difference makes the source Gram exponentially singular

Recall from `ANF-089` that the source modes are

\[
f_z(u)=\eta_{\rm MT}(u)e^{-2\pi iuz},
\qquad -\tfrac12\le u\le\tfrac12,
\tag{11}
\]

and `a(W_n)` is the smallest eigenvalue of their Gram matrix over the distinct support of `W_n`.

Use a Rayleigh vector supported only on the upper row `z_j=j\delta+iy`. Let

\[
c_j:=(-1)^j\binom nj,
\qquad
C_n^2:=\sum_{j=0}^n|c_j|^2=\binom{2n}{n}.
\tag{12}
\]

The corresponding normalized synthesis is exactly

\[
\begin{aligned}
F_n(u)
&:=\frac1{C_n}\sum_{j=0}^nc_j f_{j\delta+iy}(u)\\
&=\frac{\eta_{\rm MT}(u)e^{2\pi uy}}{C_n}
\bigl(1-e^{-2\pi i\delta u}\bigr)^n.
\end{aligned}
\tag{13}
\]

Because `0<delta<1` and `|u|<=1/2`,

\[
\left|1-e^{-2\pi i\delta u}\right|
=2|\sin(\pi\delta u)|
\le2\sin\frac{\pi\delta}{2}
=2r_\delta.
\tag{14}
\]

Therefore the Rayleigh principle gives

\[
a(W_n)
\le\|F_n\|_2^2
\le
A_y\frac{(2r_\delta)^{2n}}{\binom{2n}{n}}.
\tag{15}
\]

The elementary identity `sum_{k=0}^{2n} binom(2n,k)=4^n`, together with maximality of the central binomial coefficient, implies

\[
\binom{2n}{n}\ge\frac{4^n}{2n+1}.
\tag{16}
\]

Substituting (16) into (15) proves the first half of (8):

\[
a(W_n)\le A_y(2n+1)r_\delta^{2n}.
\tag{17}
\]

No collision or vanishing frequency gap is involved. The null direction is the ordinary `n`th finite difference of one fixed-gap horizontal exponential row, observed only on the Montgomery--Taylor source interval.

## 2. The destination collapse defect retains fixed mass

Choose the upper representatives `z_j=j\delta+iy` for the nonreal conjugate pairs. The pair-to-real-center defect used in `ANF-089` is

\[
\begin{aligned}
d_j(\alpha)
&=e^{-2\pi i\alpha(j\delta+iy)}
 +e^{-2\pi i\alpha(j\delta-iy)}
 -2e^{-2\pi i\alpha j\delta}\\
&=2e^{-2\pi i\alpha j\delta}
\bigl(\cosh(2\pi\alpha y)-1\bigr).
\end{aligned}
\tag{18}
\]

Hence every diagonal entry of the destination defect Gram matrix `D_s(W_n)` is exactly `B_{s,y}`. Since `D_s(W_n)` is positive semidefinite,

\[
b_s(W_n)=\lambda_{\max}(D_s(W_n))
\ge \max_j(D_s)_{jj}
=B_{s,y}.
\tag{19}
\]

The constant is strictly positive: `J_s>=0` is not zero almost everywhere, while `cosh(2 pi alpha y)-1` vanishes only at `alpha=0` when `y>0`. This proves the second half of (8), and (9) follows immediately from (17) and (19).

The two sides of the ratio are therefore deteriorating for fundamentally different reasons. The source can synthesize a very small finite difference on its observation window, whereas each individual destination pair-collapse defect keeps the same nonzero central-notch norm independently of `n`.

## 3. The blow-up occurs on the exact safe cone

The family (4) has the product form of `ANF-085` with horizontal occupancies `a_j=1` and the common symmetric vertical profile `Y={-y,+y}`. It is therefore already a member of the comparison class `Sep(W_n)` from `ANF-086`. Taking `P=W_n` in the definition of the relative destination defect gives

\[
\delta_s(W_n\mid W_n)=0,
\qquad
d_{\rm sep}(W_n)=0,
\tag{20}
\]

which is (10). More strongly, `ANF-085` gives, with `N_n=2(n+1)`,

\[
E_{F_s}(W_n)\ge2q_sN_n,
\tag{21}
\]

so the fixed central-notch affine certificate is valid directly, at arbitrary cardinality and with the same fixed height `y`.

This is the decisive distinction. `ANF-089` correctly states that large `chi_s` is only a necessary escape channel and not evidence of a counterexample. The present family shows that the slack is not merely quantitative: **the raw ratio can diverge exponentially while the intrinsic separable-cone distance is identically zero.** Any strategy that attempts to close the all-cardinality complex gate by proving a cardinality-uniform bound on this unquotiented `chi_s` over a class containing the separable fibers is therefore impossible.

## 4. Stress tests and boundary conditions

The Rayleigh vector in Section 1 is allowed to live on only one conjugate branch. Conjugation invariance is a property of the zero multiset `W_n`; the minimum eigenvalue `a(W_n)` is taken over arbitrary complex coefficient vectors on its full distinct support, so setting the coefficients of the lower row to zero is a legitimate upper bound for `a(W_n)`.

The construction also keeps every obvious geometric regularity fixed. There are no repeated support points, no shrinking horizontal gaps, no vertical growth, and no multiplicity growth. Only the number and total horizontal span of the centers increase. The assumption `delta<1` is essential to the displayed exponential estimate because it gives `r_delta<1`; the finding makes no claim about the critical case `delta=1` or about a uniform source lower bound for `delta>1` in the full two-row complex system.

Most importantly, (9) does **not** imply that `Delta(W_n)/L(W_n)` is small, that the family is Montgomery--Taylor near-extremal, or that it can defeat the central-notch certificate. In fact (20)--(21) show the opposite target-side conclusion: it is exactly in the already controlled product class. The result therefore does not refute `ANF-089`; it identifies a structural limitation of using its particular real-collapse condition number as the next global invariant.

## 5. Prior art and novelty boundary

The source-side mechanism is classical nonharmonic-Fourier conditioning. Ingham-type inequalities already show that a fixed frequency gap by itself gives a uniform lower Riesz bound only when the observation interval is sufficiently long relative to that gap; in the present normalization the single-row threshold is naturally at the unit spacing scale. The binomial vector (12)--(17) is a self-contained finite-section witness of the complementary conditioning loss, so no external theorem is used in the proof.

A targeted check of classical Ingham/Riesz and divided-difference literature found no Mathia-specific statement coupling that source-window loss to the destination pair-collapse Gram of `ANF-089`, and no result is needed externally for (8)--(10). The new durable content is precisely that the **cross-metric ratio introduced by the current analytic-frontier reduction can diverge exponentially on the exact all-height separable cone that the same line has already proved safe**. No new external dependency is load-bearing, so `SOURCES.md` is unchanged.

## 6. Research consequence: quotient the conditioning before trying to bound it

`ANF-089` converted the phrase “conditioning-to-geometry” into a concrete finite Gram ratio. `ANF-090` now shows that the raw ratio is still too coarse to be the final all-cardinality gate: it penalizes a particular collapse to the real axis even when a configuration already has a zero-cost comparator elsewhere in the separable cone.

The next useful theorem must therefore incorporate the separable quotient before conditioning is measured. One option is a defect Gram formed only after minimizing or projecting away exact product-fiber directions; another is a direct estimate from the Montgomery--Taylor projection taxes to `d_sep` that never passes through the real-collapse comparator. In either formulation, a genuine obstruction must be **nonseparable after quotienting** and source-ill-conditioned in a direction that retains destination mass after the nearest safe product component has been removed.

Equivalently, a cardinality-uniform bound on raw `chi_s` is no longer a sensible target. The live quantitative question is whether the near-extremal condition itself controls a separable-quotiented condition number strongly enough that

\[
\frac{\Delta(W)}{L(W)}\times
\bigl(\text{quotiented cross-metric amplification}\bigr)
\longrightarrow0
\tag{22}
\]

on every putative fatal sequence, or whether a genuinely nonseparable growing family can violate that coupled estimate. Higher-order carriers remain unnecessary until such a quotient-aware family survives the existing central-notch and projection-tax controls.