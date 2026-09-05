# PF-174 — weighted metric defect controls a smoothed Schatten scale, not the first resolvent

**Status:** `LITERATURE+DERIVED + EXACT-OPERATOR-IDEAL + NEGATIVE/BOUNDARY`. Güneysu--Thalmaier's heat/gradient factorization underlying their two-metric scattering criterion has a direct Schatten interpolation refinement: a deviation multiplier in weighted `L^{2r}` gives the corresponding heat or gradient factor in `S_{2r}`, so a product of the two factors lies in `S_r`. For the exact matched collapsing collars already analyzed in PF-128/PF-138, the inverse-unit-ball-volume weighted metric deviation is in `L^r` for every `r>=1`, uniformly in the shrinking cuff length and summably over the complete Margulis-short shift-clone tail. Thus the short-collar sector already reaches the trace-class endpoint for the **heat-smoothed comparison operator** used in scattering theory. This does **not** imply that the first relative resolvent is trace class, or even `S_r`: the heat regularization is load-bearing, and removing it is precisely the unresolved body/interface/resolvent gate. PF-112 supplies a hard endpoint falsifier for any argument that accidentally erases that distinction.

## Claim

Let `(M,g)` be a complete Riemannian manifold in the geometric regime used by S16, write

\[
P_s=e^{-sH},\qquad H=-\Delta_g,
\]

and put

\[
W(x):=\mu_g(B_g(x,1))^{-1}.
\]

The heat-kernel and gradient estimates used in S16 imply, for each fixed `s>0`, Hilbert--Schmidt estimates of the form

\[
\|M_aP_s\|_{\mathcal S_2}
\le C_s\|a\|_{L^2(W\,d\mu_g)},
\qquad
\|M_a dP_s\|_{\mathcal S_2}
\le C_s'\|a\|_{L^2(W\,d\mu_g)}.
\tag{1}
\]

The trivial operator endpoints are

\[
\|M_aP_s\|\le \|a\|_\infty,
\qquad
\|M_a dP_s\|\le C_s''\|a\|_\infty.
\tag{2}
\]

Interpolating the linear maps `a -> M_aP_s` and `a -> M_a dP_s` between `(1)` and `(2)` gives, for every `q in [2,infinity)`,

\[
\boxed{
\|M_aP_s\|_{\mathcal S_q}
+
\|M_a dP_s\|_{\mathcal S_q}
\le C_{s,q}\|a\|_{L^q(W\,d\mu_g)}.
}
\tag{3}
\]

Here one uses the standard interpolation identities

\[
[L^2(W\,d\mu_g),L^\infty]_{\theta}=L^q(W\,d\mu_g),
\qquad
[\mathcal S_2,\mathcal S_\infty]_{\theta}=\mathcal S_q,
\]

with `q=2/(1-theta)`.

In the Güneysu--Thalmaier two-metric comparison, the scalar and cotangent deviation terms are factored through square-root multipliers whose squares are bounded, up to the fixed quasi-isometry constants, by their metric deviation `delta_{g,h}`. Consequently, whenever the corresponding weighted condition holds in the metrics required by the factorization,

\[
\int_M W(x)\,\delta_{g,h}(x)^r\,d\mu_g(x)<\infty,
\tag{4}
\]

each square-root heat/gradient factor belongs to `S_{2r}` and Schatten Hölder places its product in `S_r`. For `r=1` this is the trace-class endpoint used in the scattering argument of S16. For `r>1`, equation `(3)` is the direct interpolation extension of the same **smoothed** mechanism.

The project-specific collar input is stronger than was recorded in PF-128. On the standard collapsing collar use its exact coordinate

\[
s=\sqrt{L^2+x^2},\qquad d\mu=dx\,d\theta,
\]

and let `L_+=e^tL`, with `t` uniformly bounded. PF-128 proves

\[
\delta_{L,t}(x)
\le C|t|\frac{L^2}{x^2+L^2},
\qquad
W_L(x)\le \frac{C}{\min(1,s)}.
\tag{5}
\]

Then for every `r>=1`, on the central region `s<=1`,

\[
\begin{aligned}
\int_{s\le1}W_L\,\delta_{L,t}^r\,d\mu
&\le
C_r|t|^rL^{2r}
\int_{\mathbb R}(x^2+L^2)^{-r-1/2}\,dx\\
&=
C_r|t|^r
\int_{\mathbb R}(1+u^2)^{-r-1/2}\,du\\
&\le C_r'|t|^r.
\end{aligned}
\tag{6}
\]

On the outer region `s>=1`, the weight is bounded and PF-128's unweighted `L^r` estimate gives

\[
\int_{s\ge1}W_L\,\delta_{L,t}^r\,d\mu
\le C_r|t|^rL
\le C_r|t|^r.
\tag{7}
\]

Therefore

\[
\boxed{
\int_{C_L}W_L\,\delta_{L,t}^r\,d\mu
\le C_r|t|^r
\qquad(r\ge1),
}
\tag{8}
\]

with a constant uniform as `L->0`.

PF-138 supplies the exact shift-clone tail input for every sufficiently short closed-geodesic collar: on a dyadic prime scale `P`, the relative collar parameter satisfies `|t_eta|=O(P^{-3})`, while the complete short-geodesic multiplicity is `O(P^{0.525})`. Hence

\[
\sum_{\eta\in\mathcal S}
\int_{C_\eta}W_\eta\,\delta_\eta^r\,d\mu
\ll
\sum_P P^{0.525-3r}<\infty
\qquad(r\ge1).
\tag{9}
\]

Thus the complete PF-138 Margulis-short collar sector satisfies the full weighted `L^r` scale, including the `r=1` endpoint.

## 1. Why the interpolation statement is exact

The first estimate in `(1)` follows directly from the semigroup kernel identity. If `p_s(x,y)` is the heat kernel,

\[
\|M_aP_s\|_2^2
=
\int_M |a(x)|^2
\left(\int_M |p_s(x,y)|^2\,d\mu(y)\right)d\mu(x)
=
\int_M |a(x)|^2p_{2s}(x,x)\,d\mu(x).
\tag{10}
\]

S16 controls the diagonal heat kernel by the inverse unit-ball volume at fixed time, producing the weighted `L^2` bound. Its Bismut-type gradient estimate gives the analogous Hilbert--Schmidt bound for the differentiated semigroup. The `L^infinity -> B(L^2)` endpoints are immediate from semigroup contraction and the fixed-time `L^2` gradient bound. Complex interpolation then gives `(3)` without changing the volume weight.

This step does not require a new pseudodifferential calculus on the zero-systole flute. It is an operator-ideal consequence of the same heat/gradient bounds already used by S16.

## 2. The square-root deviation fixes the Schatten exponent

The scattering factorization does not insert `delta` itself as one multiplier. It splits the metric/density error into square-root scalar and cotangent multipliers. Schematically, the relevant factors have the form

\[
M_{|S|^{1/2}}P_s,
\qquad
M_{|\widehat S|^{1/2}}dP_s,
\]

with

\[
|S|+|\widehat S|\le C\,\delta_{g,h}
\tag{11}
\]

under fixed quasi-isometry control. Therefore `(4)` at exponent `r` places each square-root multiplier in weighted `L^{2r}`. Equation `(3)` gives each analytic factor in `S_{2r}`, and the ideal inequality

\[
\|AB\|_{\mathcal S_r}
\le
\|A\|_{\mathcal S_{2r}}\|B\|_{\mathcal S_{2r}}
\tag{12}
\]

places the product in `S_r`.

This exponent bookkeeping matters for the accepted sharp-Schatten clue: the natural weighted metric input for a smoothed `S_r` conclusion is `delta in L^r(W dmu)`, not an unweighted `L^r` estimate and not `delta in L^{2r}`.

## 3. What the collar calculation does and does not buy

Equation `(8)` shows that collapse of the canonical short collar does not destroy the weighted scale. The apparently dangerous inverse-volume factor contributes `1/s` in the central part, but the metric deformation contributes the compensating `L^2/(x^2+L^2)` profile. After the rescaling `x=Lu`, the cuff length disappears exactly from the weighted integral.

PF-138 already established the `r=1` summability needed for the Güneysu--Thalmaier wave criterion on the complete Margulis-short sector. Equation `(9)` shows that interpolation above the endpoint is therefore **not the missing short-tail argument**: this sector is already at the strongest trace-class endpoint available to the heat-smoothed comparison factorization.

The still-useful content of `(3)` is a conditional global bridge. If the remaining boundary-coherent body/interface comparison can be shown to satisfy weighted `L^r` metric deviation for some `r>1` even when weighted `L^1` fails, then the same heat factorization gives an `S_r` **smoothed** comparison operator without requiring injectivity-radius lower bounds. PF-126's unweighted global `L^r` defect does not by itself verify this input, and PF-130's strong unweighted `L^1` Lambert-body budget likewise does not control the inverse-volume weight across the unresolved global interfaces.

## 4. Heat smoothing cannot be removed for free

The operator controlled above is the heat-regularized comparison object used in the Hempel--Post--Weder scattering criterion, after Güneysu--Thalmaier factorization. It is not

\[
(H_h+1)^{-1}I-I(H_g+1)^{-1}.
\tag{13}
\]

There is no bounded operation that simply cancels `e^{-sH}` from the Schatten estimate: the inverse heat multiplier grows exponentially at high spectral parameter. This is not a technical nuisance but the exact place where local pseudodifferential order re-enters.

PF-112 proves that for the genuinely non-isometric two-dimensional prime/shift pair the first relative resolvent is not trace class. By contrast, the smoothed comparison mechanism can be trace class under `(4)` with `r=1`. Therefore any proposed argument that turns the Güneysu--Thalmaier trace-class heat factorization directly into `S_1` membership of `(13)` is false for this problem. The heat factors have removed precisely the high-frequency obstruction detected by PF-112.

For `r>1`, a resolvent-level conclusion remains possible, but it needs an additional common-Hilbert-space quadratic-form/resolvent factorization or an explicit outer body/interface calculus that preserves the desired exponent without pretending to invert the heat semigroup.

## 5. Consequence for the current research frontier

The accepted clue `CLUE-shift-clone-sharp-schatten-threshold` no longer needs to ask whether the heat and gradient factors themselves admit Schatten interpolation. They do, with the exact exponent in `(3)`--`(4)`. Nor should another cycle be spent proving weighted `L^r` control on the already-exhausted Margulis-short collars: `(8)`--`(9)` reach even `r=1` there.

The heat route now has two explicit remaining gates:

1. obtain the correct **weighted** `L^r` control for the actual boundary-coherent body/interface part of the prime/shift comparison, rather than substituting PF-126's unweighted estimate;
2. bridge the resulting smoothed `S_r` comparison estimate to the **first relative resolvent** without erasing the PF-112 high-frequency obstruction.

The direct Krein/Dirichlet-to-Neumann route and the heat route are therefore complementary descriptions of the same body-loaded problem. PF-173 shows relative cancellation at the central transmission interface; PF-174 shows that heat smoothing handles the short thin geometry even more strongly, but neither contains the complementary-body response or repeated global interactions.

## 6. Prior-art and novelty audit

S16, Güneysu--Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow*, Annales de l'Institut Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`, is the authoritative source for the inverse-unit-ball-volume criterion, the heat/gradient Hilbert--Schmidt estimates, the square-root deviation factorization, and the trace-class endpoint used to prove wave-operator existence/completeness.

A targeted search also checked Güneysu--Marot, *A note on the scattering theory of Kato-Ricci manifolds*, arXiv:2411.03204 (2024), which gives a newer weighted `L^1` wave-operator criterion using Kato-Ricci heat/gradient estimates. It likewise states a scattering criterion, not a first-relative-resolvent Schatten theorem.

The interpolation identities and Schatten Hölder inequality used in `(3)` and `(12)` are standard operator-ideal facts. **No novelty is claimed for that abstract interpolation lemma.** Directed searches for metric-perturbation Schatten refinements of this heat factorization did not locate a theorem that converts weighted `L^r` metric deviation into `S_r` membership of the first relative resolvent on this zero-injectivity-radius geometry. Absence of such a result in the bounded audit is not a novelty claim.

The durable Mathia contribution is narrower and project-specific: PF-128's exact collapsing-collar coordinates imply the uniform weighted scale `(8)`; PF-138 makes it summable over the complete short tail; and combining that geometry with S16 separates a solved **smoothed ideal** subproblem from the still-open **first-resolvent/body-interface** subproblem.

## 7. Audit / falsification core

A later adversary can check PF-174 through the following finite chain:

1. from S16, verify the fixed-time diagonal heat-kernel and gradient estimates used to obtain the Hilbert--Schmidt multiplier bounds `(1)`;
2. verify the trivial `L^infinity` operator endpoints `(2)` and interpolate to `(3)` using `[S_2,S_infinity]=S_q`;
3. inspect S16's scalar/cotangent square-root factorization and verify the exponent passage `delta^r -> L^{2r}` for each square-root multiplier, then apply Schatten Hölder as in `(12)`;
4. import PF-128's exact collar coordinate, inverse-unit-ball-volume bound, and pointwise deviation estimate, and check the one-dimensional scaling integral `(6)`;
5. import PF-138's `O(P^{-3})` relative collar displacement and `O(P^{0.525})` complete short-geodesic count to verify `(9)`;
6. keep the conclusion attached to the heat-smoothed comparison operator; do not identify it with the first resolvent difference;
7. use PF-112 as an endpoint falsifier: any purported global argument that would deduce first-resolvent `S_1` solely from this smoothed trace-class mechanism has necessarily used an invalid unsmoothing step.

A refutation would need to break one of the S16 kernel estimates/factorizations, the interpolation exponent, PF-128's weighted collar scaling, or PF-138's complete short-tail count. Failure to control the unresolved body/interface comparison would not refute PF-174; it is exactly the boundary of the claim.