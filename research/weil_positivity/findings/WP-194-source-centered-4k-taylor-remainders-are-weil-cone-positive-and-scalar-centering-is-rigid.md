# WP-194 — Source-centered `4k` Taylor remainders are Weil-cone positive, and scalar centering is rigid

**Status:** `DERIVED + EXACT + HIGHER-ORDER-SPECTRAL-SHIFT + FULL-WEIL-AUTOCORRELATION-CONE + ZERO-BACKGROUND-POSITIVITY + SCALAR-CENTERING-RIGIDITY + MATCHED-NONARITHMETIC-CONTROL + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-193` leaves orders `n=4k` as the first higher-order spectral-shift category not excluded by derivative parity. Its exact gate is stronger than pointwise nonnegativity of the spectral-shift density: the even part of the density must be positive definite, equivalently have nonnegative Fourier transform.

That gate is not merely nonempty. There is a large exact class that satisfies it automatically. If the unperturbed operator is the **source-centered zero background** `H=0`, then every self-adjoint Schatten perturbation `0!=V in S^{4k}` gives a Taylor remainder that is strictly positive on every nonzero real smooth compactly supported autocorrelation. In the scalar model the converse centering statement is rigid: for a nonzero perturbation, translating the unperturbed scalar background from `0` to any `c!=0` makes the even spectral-shift density change Fourier sign, so full autocorrelation positivity fails.

Thus the `WP-193` positive-definiteness gate is an exact analytic survivor but is **not arithmetically selective**. Zero-background positivity holds for arbitrary nonarithmetic spectra as well. A Mathia route therefore cannot count `4k` Weil-cone positivity alone as evidence of arithmetic geometry: it must source-force the centering and independently derive the finite-prime, Gamma, and polar/global terms from the same construction.

## 1. Exact scalar spectral-shift density

Work first on a one-dimensional Hilbert space. Let

\[
H=c,\qquad V=v,\qquad v\ne0,
\tag{1}
\]

and let `n>=2`, with `r=n-1`. For `v>0`, Taylor's integral remainder gives

\[
\begin{aligned}
&f(c+v)-\sum_{j=0}^{n-1}\frac{f^{(j)}(c)}{j!}v^j\\
&\qquad=\frac1{r!}\int_c^{c+v}f^{(n)}(\lambda)(c+v-\lambda)^r\,d\lambda.
\end{aligned}
\tag{2}
\]

Hence the scalar higher-order spectral-shift density is exactly

\[
\boxed{
\eta_{n,c,v}(\lambda)
=\frac{(c+v-\lambda)^r}{r!}\,
\mathbf 1_{[c,c+v]}(\lambda)
}
\qquad(v>0).
\tag{3}
\]

For `v=-a<0`, reversing the integration limits gives the exact reflected density

\[
\eta_{n,c,-a}(\lambda)
=(-1)^n\frac{(\lambda-(c-a))^r}{r!}
\mathbf 1_{[c-a,c]}(\lambda).
\]

Thus negative scalar shifts carry an additional factor `(-1)^n`; this distinction is immaterial at the even orders used below but reverses the centered density at odd order. No zeta data, zero divisor, or arithmetic coefficient enters this calculation.

The question from `WP-193` is what happens to the even part

\[
\eta^{\rm ev}(x)=\frac12\bigl(\eta(x)+\eta(-x)\bigr)
\tag{4}
\]

under Fourier transform.

## 2. At `H=0` the even density has an explicit signed triangle mixture

Set `c=0` and write `a=|v|`. After changing the value at the single point `x=0`, which is immaterial in `L^1`, the continuous representative of the even density is

\[
\boxed{
\phi_{n,a,v}(x)
=\eta_{n,0,v}^{\rm ev}(x)
=\operatorname{sgn}(v)^n\frac{(a-|x|)_+^r}{2r!}.
}
\tag{5}
\]

For `r>=2`, the truncated power has the exact triangular-mixture identity

\[
(a-|x|)_+^r
=r(r-1)\int_0^a
(t-|x|)_+(a-t)^{r-2}\,dt.
\tag{6}
\]

Indeed, for `|x|<a`, putting `y=|x|` and integrating over `t in [y,a]` gives

\[
r(r-1)\int_y^a(t-y)(a-t)^{r-2}\,dt=(a-y)^r,
\tag{7}
\]

while both sides vanish for `|x|>=a`.

With the Fourier convention of `WP-193`,

\[
\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-i\xi x}\,dx,
\tag{8}
\]

the triangular kernel satisfies

\[
\boxed{
\widehat{(t-|x|)_+}(\xi)
=\frac{2(1-\cos(t\xi))}{\xi^2}\ge0.
}
\tag{9}
\]

Combining (5)--(9), for `n>=3` and `\xi!=0`,

\[
\boxed{
\widehat{\phi_{n,a,v}}(\xi)
=\frac{\operatorname{sgn}(v)^n}{(n-3)!\,\xi^2}
\int_0^a
(1-\cos(t\xi))(a-t)^{n-3}\,dt.
}
\tag{10}
\]

At `\xi=0`, continuity gives the same overall factor `\operatorname{sgn}(v)^n` times a strictly positive integral.

Therefore every centered scalar density of **even** order `n>=4` has a strictly positive Fourier transform after evenization for either sign of `v`. At odd order the sign is `\operatorname{sgn}(v)`, so a negative scalar perturbation reverses the Fourier sign. This is a direct compact-support Pólya-type phenomenon; no novelty is claimed for positive definiteness of such truncated powers. The branch-specific point is what it does to the exact Weil autocorrelation gate in `WP-193`.

## 3. Exact sign on the full autocorrelation cone

Let `0!=g in C_c^infty(R)` be real and

\[
h=g*\widetilde g,
\qquad
\widetilde g(x)=g(-x).
\tag{12}
\]

For even `n=2m`, `WP-193` gives the exact identity

\[
\mathcal R_{2m}(h;H,V)
=
\frac{(-1)^m}{2\pi}
\int_{\mathbb R}
\xi^{2m}|\widehat g(\xi)|^2
\widehat{\eta_{2m}^{\rm ev}}(\xi)\,d\xi.
\tag{13}
\]

At `H=0`, equation (10) makes the Fourier factor strictly positive. Consequently, for every scalar `v!=0`,

\[
\boxed{
\mathcal R_{4k}(g*\widetilde g;0,v)>0
\quad\text{for every }0!=g in C_c^infty(R).
}
\tag{14}
\]

The neighboring parity is an exact matched control:

\[
\boxed{
\mathcal R_{4k+2}(g*\widetilde g;0,v)<0
\quad\text{for every }0!=g in C_c^infty(R).
}
\tag{15}
\]

The inequalities are strict because `\widehat{\phi}` is strictly positive and the Fourier transform of a nonzero compactly supported smooth `g` cannot be supported only at `\xi=0`.

Thus `WP-193`'s `4k` survivor is realized by the most elementary source-centered spectral pair. There is no need to engineer a special positive-definite density once the background is exactly zero.

## 4. Zero-background positivity extends to arbitrary Schatten spectra

Now let `H=0` on a separable Hilbert space and let

\[
0\ne V=V^*\in\mathcal S^n.
\tag{16}
\]

Because `V` is compact and self-adjoint, choose an orthonormal eigenbasis with real eigenvalues `(v_j)`. For a smooth compactly supported `h`, functional calculus diagonalizes the Taylor remainder at zero. The scalar remainder for eigenvalue `v_j` is `O(|v_j|^n)` near zero, while

\[
\sum_j|v_j|^n<\infty.
\tag{17}
\]

Hence the trace remainder is the absolutely convergent sum of scalar remainders,

\[
\mathcal R_n(h;0,V)
=\sum_j\mathcal R_n(h;0,v_j).
\tag{18}
\]

Applying (14) term by term yields the operator theorem

\[
\boxed{
0\ne V=V^*\in\mathcal S^{4k}
\quad\Longrightarrow\quad
\mathcal R_{4k}(g*\widetilde g;0,V)>0
}
\tag{19}
\]

for every nonzero real `g in C_c^infty(R)`. Equivalently, the even part of the order-`4k` spectral-shift density is a positive-definite `L^1` function. At order `4k+2`, the same direct-sum argument gives strict negativity instead.

This makes the matched-control issue decisive. The theorem holds for **every** self-adjoint Schatten spectrum: deterministic, random, integer-spaced, perturbed, or otherwise nonarithmetic. Full Weil-autocorrelation-cone positivity at zero background therefore has no arithmetic specificity by itself.

## 5. Scalar centering is rigid

The zero in (19) is not a harmless scalar gauge. Return to `v>0` and arbitrary scalar background `c`. From (3), the Fourier transform of the even density is

\[
\widehat{\eta_{n,c,v}^{\rm ev}}(\xi)
=
\operatorname{Re}\!\left[
\frac{e^{-i(c+v)\xi}}{r!}
\int_0^v u^r e^{i\xi u}\,du
\right].
\tag{20}
\]

One integration by parts gives, as `\xi to +infty`,

\[
\boxed{
\widehat{\eta_{n,c,v}^{\rm ev}}(\xi)
=-\frac{v^r}{r!\,\xi}\sin(c\xi)
+O(\xi^{-2}).
}
\tag{21}
\]

If `c!=0`, choose sequences of frequencies tending to infinity on which `sin(c\xi)=1` and `sin(c\xi)=-1`. The `1/xi` term dominates the remainder, so the Fourier transform has infinitely many positive and negative values. The reflected `v<0` formula has the opposite leading sign but the same sign-change conclusion.

For `n=4k`, `WP-193` says full positivity on real compactly supported smooth autocorrelations is equivalent to nonnegativity of this Fourier transform. Equations (10) and (21) therefore give the exact scalar classification

\[
\boxed{
V=v\ne0,\ n=4k:
\qquad
\mathcal R_{4k}(g*\widetilde g;c,v)\ge0
\text{ for every real }g
\iff c=0.
}
\tag{22}
\]

For `c!=0`, continuity supplies an interval on which the multiplier is negative; a broad compactly supported envelope modulated to that interval gives a concrete negative autocorrelation by the concentration argument already used in `WP-193`.

So a translation of both endpoints of the scalar spectral segment changes the full-cone order even though its length `|v|` is unchanged. In this category, the spectral origin participates in the positivity theorem.

## 6. Aggressive falsification and exact scope

**This does not derive Weil positivity.** Equation (19) proves positivity on the same abstract autocorrelation cone that appears in the Weil criterion, but it does not identify `\mathcal R_{4k}` with the arithmetic explicit-formula functional. There is no Mangoldt term, Gamma term, or polar/global completion in the construction above.

**The positivity is too universal to be arithmetic evidence.** Replacing `V` by an arbitrary nonarithmetic compact self-adjoint operator preserves (19). Therefore any proposed bridge whose evidence is only `H=0` plus `4k` Taylor-remainder positivity fails the matched-control requirement of this branch.

**Centering cannot be tuned after the fact.** The scalar classification (22) shows that shifting a candidate pair to make its background zero is mathematically substantive for the Weil cone. A viable Mathia construction must make `H=0` canonical from its source geometry. Choosing the origin after inspecting arithmetic or spectral data would be an inserted gauge, explicitly excluded by the research mandate.

**The result does not prove operator-level centering uniqueness.** Equation (22) is a scalar rigidity theorem. For noncommuting or non-scalar backgrounds there may be other positive-definite even densities. This finding does not classify them. It says only that zero background supplies a universal survivor and that even the scalar sector loses the property under every nonzero background translation.

**Higher order still does not create mixed-prime incidence.** The zero-background theorem factorizes spectrally and works eigenvalue by eigenvalue. It therefore supplies no intrinsic cross-prime relation, no finite--archimedean coupling, and no reason for the local Euler data of `Q` to be distinguished from matched generalized-prime or random controls.

## 7. Prior-art and novelty boundary

The ingredients on the operator-theory side are not claimed as new. `WP-193` records the higher-order spectral-shift/Taylor-remainder framework and its external literature. Compactly supported truncated powers and triangle mixtures are classical positive-definite constructions, and the scalar formula (3) is the elementary Taylor integral remainder. The proof above is kept self-contained and does not require an additional external theorem beyond the framework already audited in `WP-193`.

A targeted prior-art search around higher-order spectral shift, Taylor remainders, Pólya-type positive-definite truncated powers, Fourier positivity, and autocorrelation criteria did not expose the specific branch-level combination asserted here: the exact zero-background `4k` full-cone theorem, its arbitrary-Schatten matched control, and the scalar `c=0` iff classification arising from the `WP-193` Weil-cone gate. The durable Mathia contribution is that **classification and falsification boundary**, not a claim of a new positive-definite kernel or a new spectral-shift theorem.

## 8. Consequence for `weil_positivity`

`WP-193` ended with the live possibility that a source-specific `4k` pair might force the extra positive-definiteness needed by the Weil cone. This finding sharpens that possibility in both directions.

First, the analytic gate is easier to satisfy than it looked:

\[
\boxed{
H=0,\quad V=V^*\in\mathcal S^{4k}
\quad\Longrightarrow\quad
\text{full autocorrelation-cone positivity}.
}
\tag{23}
\]

Second, that ease is itself a falsifier. Since (23) is universal over the perturbation spectrum, it cannot explain arithmetic specificity. The surviving Mathia question is no longer merely whether one can find a positive-definite `4k` density. It is whether an intrinsic finite--archimedean construction **forces the source-centered zero (or some genuinely nontrivial operator analogue), produces its perturbation without fitting arithmetic output, and makes the same canonical Taylor remainder equal the completed Weil functional**.

Until such an identification exists, the source-centered higher-order route is a broad analytic carrier, not a geometric proof of global Weil positivity. Its useful output is an exact constraint: centering must be part of the source structure, and positivity must survive after the finite-prime and archimedean/global pieces are derived rather than before they are attached.

## Dependencies

- `research/weil_positivity/findings/WP-193-higher-order-spectral-shift-positivity-has-a-mod-four-weil-autocorrelation-gate.md`

## Bottom line

The `4k` spectral-shift gate from `WP-193` has an exact universal survivor. At zero background, every nonzero self-adjoint Schatten perturbation is strictly positive on the full real Weil autocorrelation cone; neighboring `4k+2` orders are strictly negative. In the scalar `4k` model this positivity is rigidly centered: it holds for every autocorrelation exactly when the unperturbed scalar is `0`.

That is progress mainly because it prevents the next false positive. A source-centered `4k` remainder can provide independent analytic positivity, but that property survives arbitrary nonarithmetic matched controls. It bears on the Weil problem only if Mathia can force the centering and, from the same geometry, derive the finite Mangoldt, Gamma, and polar/global completion without fitting or importing the explicit formula.