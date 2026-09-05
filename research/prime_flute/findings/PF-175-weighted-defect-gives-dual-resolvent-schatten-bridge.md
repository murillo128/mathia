# PF-175 — weighted metric defect gives a dual-identified resolvent Schatten bridge

**Status:** `LITERATURE+DERIVED + EXACT-CONDITIONAL + BOUNDARY`. PF-174 converts Güneysu--Thalmaier inverse-unit-ball weighted metric control into Schatten bounds for **heat-smoothed** comparison factors, but deliberately stops before the first relative resolvent because the heat semigroup cannot be inverted by a bounded operation. The present finding closes a different, form-natural resolvent bridge. For two complete quasi-isometric hyperbolic metrics, weighted `L^r` metric deviation with `r>1` implies an `S_r` first-resolvent comparison for the dual-volume identification `J^\vee=(I^{-1})^*`. The proof uses the exact quadratic-form difference and factors each coefficient perturbation between **two resolvent-smoothed half-factors**, each lying in `S_{2r}` by the same heat/gradient estimates audited in PF-174. For the trivial and density-unitary identifications the same weighted input gives `S_r` at least for `r>=2`; the strip `1<r<2` remains an identification-transfer problem. No global weighted body/interface estimate for the prime/shift pair, no `S_1` statement for the dual identification, no wave/scattering equivalence, and no RH consequence is claimed.

## Claim

Let `(M,g)` and `(M,h)` be complete hyperbolic surfaces on the same smooth manifold, with `g` and `h` globally quasi-isometric. Put

\[
\mathcal H_g=L^2(M,d\mu_g),
\qquad
\mathcal H_h=L^2(M,d\mu_h),
\]

let `H_g,H_h` be the nonnegative self-adjoint Laplacians, and write

\[
R_g=(H_g+1)^{-1},
\qquad
R_h=(H_h+1)^{-1}.
\tag{1}
\]

Let

\[
I:\mathcal H_g\longrightarrow\mathcal H_h,
\qquad
If=f
\tag{2}
\]

be the trivial identification and put

\[
\rho:=\frac{d\mu_h}{d\mu_g}.
\tag{3}
\]

The Hilbert-space adjoint of `I^{-1}` is the bounded identification

\[
\boxed{
J^\vee:=(I^{-1})^*,
\qquad
J^\vee f=\rho^{-1}f.
}
\tag{4}
\]

Call this the **dual-volume identification**. It is characterized by the exact pairing identity

\[
\langle J^\vee f,v\rangle_h
=
\langle f,v\rangle_g.
\tag{5}
\]

Let `delta_{g,h}` be the Güneysu--Thalmaier multiplicative metric-deviation scalar and define

\[
W_j(x):=\mu_j(B_j(x,1))^{-1},
\qquad j\in\{g,h\}.
\tag{6}
\]

Fix `r>1`. Assume

\[
\boxed{
\int_M W_g\,\delta_{g,h}^{\,r}\,d\mu_g
+
\int_M W_h\,\delta_{g,h}^{\,r}\,d\mu_h
<\infty.
}
\tag{7}
\]

Then

\[
\boxed{
R_hJ^\vee-IR_g
\in
\mathcal S_r(\mathcal H_g,\mathcal H_h).
}
\tag{8}
\]

There is a second, weaker identification consequence. Let

\[
U:\mathcal H_g\longrightarrow\mathcal H_h,
\qquad
Uf=\rho^{-1/2}f
\tag{9}
\]

be the canonical density-unitary map. Under (7), for every `r>=2`,

\[
\boxed{
R_hI-IR_g\in\mathcal S_r,
\qquad
R_hU-UR_g\in\mathcal S_r.
}
\tag{10}
\]

Equivalently, after conjugating by `U`, the standard common-Hilbert-space first relative resolvent lies in `S_r` for `r>=2` whenever the corresponding weighted metric deviation (7) holds.

The distinction between (8) and (10) is essential. The proof of (8) reaches every `r>1` because the perturbation is split between two `S_{2r}` resolvent half-factors. Transferring from `J^\vee` to `I` or `U` introduces a **one-sided density multiplier**, and the Güneysu--Thalmaier `S_2`-to-operator interpolation used here controls that term only for exponents at least `2`. PF-175 therefore does not settle `1<r<2` for the density-unitary prime/shift relative resolvent.

## 1. The dual identification exposes an exact two-sided form factorization

Let `A=A_{g,h}` be the positive cotangent comparison endomorphism defined by

\[
h^*(\alpha,\beta)
=
g^*(A\alpha,\beta).
\tag{11}
\]

The target Dirichlet form, written with the source measure, is

\[
q_h(u,v)
=
\int_M
g^*(\rho A\,du,dv)\,d\mu_g.
\tag{12}
\]

Set

\[
C:=\rho A-I,
\qquad
b:=\rho-1.
\tag{13}
\]

Because the two metrics are uniformly quasi-isometric, their relative eigenvalues remain in one fixed compact subset of `(0,\infty)`. The Güneysu--Thalmaier deviation is a smooth monotone function of the logarithms of those eigenvalues. Hence there is a quasi-isometry-dependent constant such that pointwise

\[
\boxed{
|C|_g+|b|
\le C_0\,\delta_{g,h}.
}
\tag{14}
\]

Take `f in H_g`, `z in H_h`, and put

\[
u=R_gf,
\qquad
v=R_hz.
\tag{15}
\]

Quasi-isometry identifies the two form domains, so both variational equations may be tested against `u` and `v`. From (5),

\[
\langle R_hJ^\vee f,z\rangle_h
=
\langle f,R_hz\rangle_g.
\tag{16}
\]

The source resolvent equation gives

\[
\langle f,v\rangle_g
=
q_g(u,v)+\langle u,v\rangle_g,
\tag{17}
\]

while self-adjointness of the target resolvent gives

\[
\langle Iu,z\rangle_h
=
q_h(u,v)+\langle u,v\rangle_h.
\tag{18}
\]

Subtracting (18) from (17) yields the exact identity

\[
\boxed{
\begin{aligned}
\left\langle
(R_hJ^\vee-IR_g)f,z
\right\rangle_h
={}&
-\int_M g^*(C\,dR_gf,dR_hz)\,d\mu_g\\
&-\int_M b\,(R_gf)\,\overline{R_hz}\,d\mu_g.
\end{aligned}
}
\tag{19}
\]

No derivative of `rho`, no derivative of the metric coefficients, and no inverse heat operator appears. This is the analytic gain over trying to unsmooth PF-174 directly: the first resolvent already supplies one derivative of smoothing on **each side** of the principal coefficient defect.

## 2. Weighted heat estimates make each resolvent half-factor `S_{2r}`

PF-174 audited the Güneysu--Thalmaier heat and gradient kernel estimates on complete hyperbolic surfaces without an injectivity-radius lower bound. For `0<t<=1`, with `W_j` as in (6), they give the fixed-time Hilbert--Schmidt bounds

\[
\|M_a e^{-tH_j}\|_{\mathcal S_2}
\le
C t^{-1/2}
\|a\|_{L^2(W_jd\mu_j)},
\tag{20}
\]

and

\[
\|M_a d e^{-tH_j}\|_{\mathcal S_2}
\le
C t^{-1}
\|a\|_{L^2(W_jd\mu_j)}.
\tag{21}
\]

The corresponding operator bounds are

\[
\|M_a e^{-tH_j}\|
\le \|a\|_\infty,
\qquad
\|M_a d e^{-tH_j}\|
\le C t^{-1/2}\|a\|_\infty.
\tag{22}
\]

Complex interpolation between `S_2` and `S_\infty` therefore gives, for every `q>=2`,

\[
\boxed{
\|M_a e^{-tH_j}\|_{\mathcal S_q}
\le
C_q t^{-1/q}
\|a\|_{L^q(W_jd\mu_j)},
}
\tag{23}
\]

\[
\boxed{
\|M_a d e^{-tH_j}\|_{\mathcal S_q}
\le
C_q t^{-1/2-1/q}
\|a\|_{L^q(W_jd\mu_j)}.
}
\tag{24}
\]

Integrating the semigroup representation

\[
R_j=\int_0^\infty e^{-t}e^{-tH_j}\,dt
\tag{25}
\]

gives

\[
M_aR_j\in\mathcal S_q
\qquad(q>1),
\tag{26}
\]

whenever (23) is available, and

\[
\boxed{
M_a dR_j\in\mathcal S_q
\qquad(q>2),
}
\tag{27}
\]

from (24), because the small-time exponent

\[
\frac12+\frac1q<1
\quad\Longleftrightarrow\quad
q>2.
\tag{28}
\]

For the application to (19), set `q=2r`. Since `r>1`, equation (28) holds strictly.

Now factor the coefficient fields by polar decomposition,

\[
C=|C|^{1/2}\operatorname{sgn}(C)|C|^{1/2},
\qquad
b=|b|^{1/2}\operatorname{sgn}(b)|b|^{1/2}.
\tag{29}
\]

Equation (14) and hypothesis (7) imply

\[
|C|^{1/2},\,|b|^{1/2}
\in
L^{2r}(W_gd\mu_g)
\tag{30}
\]

on the source side and, after the bounded quasi-isometric conversion of cotangent norms and measures,

\[
|C|^{1/2},\,|b|^{1/2}
\in
L^{2r}(W_hd\mu_h)
\tag{31}
\]

on the target side. Consequently the four source/target resolvent half-factors appearing in (19) lie in `S_{2r}`.

## 3. Schatten Hölder proves the first-resolvent result

Use (29) in (19). Up to bounded quasi-isometric identifications of the two cotangent `L^2` spaces, the gradient term is a product of the form

\[
\bigl(M_{|C|^{1/2}}dR_h\bigr)^*
\,
\operatorname{sgn}(C)
\,
\bigl(M_{|C|^{1/2}}dR_g\bigr),
\tag{32}
\]

and the scalar term has the analogous factorization

\[
\bigl(M_{|b|^{1/2}}R_h\bigr)^*
\,
\operatorname{sgn}(b)
\,
\bigl(M_{|b|^{1/2}}R_g\bigr).
\tag{33}
\]

Each outer factor lies in `S_{2r}` by (26)--(31), and each middle factor is bounded. Schatten Hölder therefore gives

\[
\mathcal S_{2r}\,\mathcal B\,\mathcal S_{2r}
\subset
\mathcal S_r.
\tag{34}
\]

Equations (19), (32)--(34) prove (8).

The point is not merely that a heat-regularized perturbation is Schatten. The exact resolvent form identity itself supplies the two smoothing halves, so the heat estimates are used only to prove ideal membership of those halves. Nothing is subsequently unsmoothed.

The threshold `r>1` in this argument is also structurally transparent: at `r=1`, the required gradient half-factor would be `S_2`, and (21) produces the logarithmically nonintegrable small-time scale `t^{-1}` in (25). PF-175 makes **no claim** that the dual-identified operator in (8) fails to be trace class at that endpoint; the proof simply stops there.

## 4. Trivial and density-unitary identifications are reached for `r>=2`

The density-unitary map (9) and the dual map (4) differ from the trivial identification by bounded scalar multipliers. Algebraically,

\[
\begin{aligned}
(R_hU-UR_g)-(R_hJ^\vee-IR_g)
={}&
R_h(U-J^\vee)
-(U-I)R_g.
\end{aligned}
\tag{35}
\]

Similarly,

\[
(R_hI-IR_g)-(R_hJ^\vee-IR_g)
=
R_h(I-J^\vee).
\tag{36}
\]

Uniform quasi-isometry and the same eigenvalue comparison used in (14) give

\[
|\rho^{-1/2}-1|
+
|\rho^{-1/2}-\rho^{-1}|
+
|1-\rho^{-1}|
\le
C_1\delta_{g,h}.
\tag{37}
\]

For `r>=2`, (7), (23), and (25) imply the one-sided multiplier estimates

\[
M_cR_j\in\mathcal S_r
\tag{38}
\]

for every scalar `c` bounded by `C delta_{g,h}`; right-sided versions follow by taking adjoints and using the bounded density conversion. Equations (35)--(38) therefore prove (10).

For `1<r<2`, this particular interpolation argument does not provide (38), because (23) was obtained by interpolating only between `S_2` and operator norm. It would be incorrect to infer the missing range merely from the dual result. In particular, PF-149 proves asymptotic equivalence of the trivial and density-unitary identifications for **wave operators**, but asymptotic wave equivalence is much weaker than equality modulo `S_r`.

Thus the current analytic picture is

\[
\boxed{
\begin{array}{rcl}
\text{weighted }\delta^r,\ r>1
&\Longrightarrow&
R_hJ^\vee-IR_g\in S_r,\\[1mm]
\text{weighted }\delta^r,\ r\ge2
&\Longrightarrow&
R_hU-UR_g\in S_r,\\[1mm]
1<r<2\text{ for }U
&:&
\text{still open by this method.}
\end{array}}
\tag{39}
\]

## 5. Consequence for the exact prime/shift clone

Apply the theorem to the exact prime flute `g` and the transported all-composite shift-clone metric `h` under a future smooth globally boundary-coherent version of the PF-125/PF-139/PF-140 comparison.

PF-174 has already proved that the complete PF-138 family of collapsing Margulis-short collars satisfies the weighted `delta^r` input uniformly for every `r>=1`, with a summable family budget after the `t_eta=O(P^{-3})` matched core-length defect is inserted. PF-140 removes the standard-cusp handoff, and PF-145 identifies the exact local `L^1` currency of the remaining collar-interface trace.

What is **not** yet proved is the global hypothesis (7) for one coherent prime/shift marking. The unresolved input remains the actual outer collar/body interface, the body trace reaching the PF-145 fixed interior interfaces, and the total weighted body/interface assembly. PF-130 and PF-139 give strong unweighted `L^1` information on major body pieces, but they deliberately do not control the inverse-unit-ball-volume weight on every true thin interaction.

Accordingly PF-175 sharpens the accepted Schatten clue without resolving it:

\[
\boxed{
\text{weighted global geometry}
\Longrightarrow
\begin{cases}
S_r\text{ dual first resolvent},&r>1,\\
S_r\text{ natural unitary first resolvent},&r\ge2,
\end{cases}
}
\tag{40}
\]

while the desired standard density-unitary classification for every `r>1` still needs both the missing geometric input and the identification transfer in `1<r<2`.

One especially clean residual test is now visible. If a boundary-compatible prime/shift marking with the required weighted metric budget could additionally be chosen **area preserving**,

\[
\rho\equiv1,
\tag{41}
\]

then

\[
J^\vee=I=U
\tag{42}
\]

and (8) would immediately give the standard common-Hilbert-space `S_r` conclusion for every `r>1`. PF-175 does not assert that such a globally marked area-preserving comparison exists; (41) is a concrete geometric subproblem for the accepted clue.

## 6. Endpoint and gauge controls

Several tempting overclaims fail.

First, PF-112's non-`S_1` theorem applies to the **density-unitary common-Hilbert-space first resolvent** of two genuinely different metrics. It must not be transferred automatically to (8). The dual identification changes the order-`-2` principal symbol. In dimension two a conformal metric change already shows why this matters: if `h=e^{2\varphi}g`, then `rho=e^{2\varphi}` and the leading symbols of `rho^{-1}R_h` and `R_g` cancel. Thus `r=1` for `J^\vee` requires its own analysis.

Second, the weighted condition (7) is stronger than PF-126's unweighted `L^r` coefficient estimate. Zero injectivity radius is exactly why the inverse-unit-ball factor cannot be silently dropped.

Third, (8) is an ideal statement for a two-Hilbert-space resolvent comparison under one specific identification. It is not equality of spectra, scattering matrices, resonances, Selberg/Ruelle data, or determinants.

Fourth, even a positive unitary `S_r`, `r>1`, classification would be a **prime/composite comparison-class result**. The second metric is the exact all-composite shift clone itself. Such an ideal class cannot by itself certify primality or RH; it only tells us how much spectral information survives this matched control.

## 7. Prior art and novelty audit

The heat-kernel input is classical/literature-backed. Güneysu--Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow*, Ann. Inst. Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`, provide the heat and gradient estimates, inverse-unit-ball control, and geometric comparison framework used in PF-174 and in Section 2 above. Their published conclusion is a wave-operator/scattering criterion; PF-175 does not attribute the first-resolvent `S_r` statement (8) to them.

There is substantial classical precedent for coefficient perturbations producing Schatten resolvent differences. G. Barbatis, *Trace estimates and invariance of the essential spectrum*, Arch. Math. 87 (2006), 343--349, DOI `10.1007/s00013-006-1716-8`, arXiv:math/0601435, proves trace-ideal resolvent estimates for elliptic coefficient perturbations on `R^N` in terms of `L^p` coefficient differences. Behrndt--Langer--Lotoreichik and related extension-theory work give further Schatten estimates for resolvent differences produced by changes of elliptic boundary conditions. Those settings and hypotheses differ from the present two-Hilbert-space, inverse-unit-ball-weighted, zero-injectivity-radius geometry.

Directed searches by structure -- metric perturbation resolvent Schatten class, Laplace--Beltrami resolvent difference, weighted coefficient ideals, and geometric scattering without injectivity radius -- found these neighboring theories but no exact source for (8) in the form used here. **No general theorem novelty is claimed.** The durable Mathia content is the audited project-specific bridge

\[
\boxed{
\text{PF-174 weighted half-factor estimates}
+
\text{dual-volume quadratic-form identity}
\Longrightarrow
S_r\text{ first-resolvent comparison for }r>1,
}
\tag{43}
\]

together with the exact separation between the still-open geometric input, the solved dual-identification bridge, and the residual natural-identification strip.

## 8. Audit / falsification core

A later adversary can check PF-175 through a finite chain:

1. verify (4)--(5) directly from `dmu_h=rho dmu_g`;
2. write the target Dirichlet form with source measure and verify (12)--(14);
3. subtract the two resolvent variational equations to obtain (19), checking that the dual identification is essential to the exact source pairing;
4. import only PF-174/Güneysu--Thalmaier's fixed-time heat and gradient Hilbert--Schmidt estimates, interpolate to (23)--(24), and integrate in time;
5. check that `q=2r>2` is exactly what makes the gradient resolvent half-factor integrable at zero;
6. factor `C` and `b` as in (29) and apply Schatten Hölder to obtain (8);
7. verify (35)--(38) separately and retain the restriction `r>=2` for the one-sided density-identification correction;
8. do not use PF-112 to assert a dual-identification `S_1` obstruction;
9. in the prime/shift application, verify that PF-174 controls only the already-audited weighted sectors and do not promote PF-130/PF-139's unweighted body estimates to (7).

A refutation can therefore attack one of three precise places: the exact form identity, the weighted heat-to-resolvent half-factor estimate, or the global prime/shift weighted geometry. Failure of the last item would not refute the general conditional bridge; it would identify the remaining geometric obstruction that the accepted clue is supposed to test.

## Research consequence

PF-174 left the phrase “resolvent-level bridge” as a single unresolved analytic box. PF-175 splits that box. For the dual-volume comparison, the bridge is now closed for every `r>1`. For the standard density-unitary comparison, the same weighted input reaches `r>=2`, while `1<r<2` remains a genuine identification-sensitive problem.

The accepted `CLUE-shift-clone-sharp-schatten-threshold.md` should therefore concentrate on two residual tasks rather than redoing heat interpolation: prove or refute the **global weighted body/interface metric budget**, and then close the density-identification strip `1<r<2` (with an area-preserving marked comparison as one exact geometric route). The endpoint `S_1` for the standard identification remains excluded by PF-112.
