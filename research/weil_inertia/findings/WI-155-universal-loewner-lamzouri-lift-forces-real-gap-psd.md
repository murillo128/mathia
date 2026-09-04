# WI-155 — a universal Loewner Lamzouri lift forces real-gap PSD and falls under the scalar one-delta barrier

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY`.

WI-154 proved that a support-one Hermitian matrix kernel cannot improve the sharp Montgomery--Taylor/CCLM one-delta constant if its real-gap values are pointwise positive semidefinite: every scalar compression is already in the sharp scalar extremal class. That finding deliberately left open whether a genuinely matrix-valued zero-side certificate could avoid pointwise PSD on real gaps.

For the most direct operator analogue of Lamzouri's universal finite-multiset inequality, it cannot. Let

\[
R:\mathbb C\to M_d(\mathbb C)
\]

be even, satisfy `R(0)=I_d`, and obey the conjugation symmetry

\[
R(\overline z)=R(z)^*.
\tag{1}
\]

Assume that for every nonempty finite multiset `Z` invariant under complex conjugation, with `N=|Z|` counted with multiplicity and `s(Z)` the number of simple real elements, one has the **universal Loewner Lamzouri-form census**

\[
\boxed{
 s(\mathcal Z)I_d
 \succeq
 2NI_d-\sum_{z,w\in\mathcal Z}R(z-w).
}
\tag{2}
\]

Then the complete two-element tests already force

\[
\boxed{R(x)\succeq0\quad(x\in\mathbb R),}
\tag{3}
\]

and

\[
\boxed{R(iy)\succeq I_d\quad(y\in\mathbb R).}
\tag{4}
\]

Consequently, if the real-axis restriction of `R` is continuous, even, entrywise integrable, and has entrywise Fourier transform supported in `[-1,1]`, WI-154 applies automatically:

\[
\boxed{
\int_{\mathbb R}R(x)
\left[1-\left(\frac{\sin \pi x}{\pi x}\right)^2\right]dx
\succeq
m_{\rm MT}I_d,
}
\tag{5}
\]

where

\[
m_{\rm MT}
=\frac1{\sqrt2}\cot\frac1{\sqrt2}-\frac12.
\]

Thus the natural strategy "replace Lamzouri's scalar pair kernel by one matrix kernel and ask for the same finite census in Loewner order" does **not** escape the scalar support-one one-delta extremal barrier. The pointwise-PSD hypothesis of WI-154 is not optional inside this direct architecture; the real two-point census forces it.

This is not an impossibility theorem for every matrix or joint-profile argument. A viable matrix escape must weaken or replace at least one load-bearing feature of (2): use a sign-indefinite matrix statistic whose positivity emerges only after a larger global combination, retain nonlinear coupled observables rather than one pair-sum kernel, restrict the configuration class using zeta-specific input, use higher correlations, or justify wider Fourier support.

## 1. Exact real two-point test

Fix `x in R`, `x != 0`, and take the two-point multiset

\[
\mathcal Z_x=\{0,x\}.
\]

Both elements are simple and real, so `N=2` and `s(Z_x)=2`. By evenness and the normalization `R(0)=I_d`,

\[
\sum_{z,w\in\mathcal Z_x}R(z-w)
=2I_d+R(x)+R(-x)
=2I_d+2R(x).
\tag{6}
\]

Substituting (6) into (2) gives

\[
2I_d
\succeq
4I_d-(2I_d+2R(x))
=2I_d-2R(x),
\]

hence

\[
R(x)\succeq0.
\tag{7}
\]

Since `R(0)=I_d`, (7) also holds at `x=0`. The conjugation symmetry (1) makes `R(x)` Hermitian on the real axis, so (7) is an ordinary Loewner statement rather than merely a condition on its Hermitian part.

This is the matrix analogue of the scalar real two-point necessary condition isolated in WI-146, but it is stronger in exactly the way relevant to WI-154: **every channel direction is nonnegative on every real gap**. For each `v in C^d`,

\[
r_v(x):=v^*R(x)v\ge0.
\tag{8}
\]

No positive-Hilbert representation, positive spectral density, Gram factorization, or arithmetic input is used.

## 2. The conjugate-pair test also lifts to Loewner order

Now fix `y in R`, `y != 0`, and take one non-real conjugate pair

\[
\mathcal Z_y=\{iy/2,-iy/2\}.
\]

There are no simple real elements, so `N=2` and `s(Z_y)=0`. Evenness gives

\[
\sum_{z,w\in\mathcal Z_y}R(z-w)
=2I_d+R(iy)+R(-iy)
=2I_d+2R(iy).
\tag{9}
\]

By (1) and evenness, `R(iy)` is Hermitian. Equation (2) therefore implies

\[
0
\succeq
4I_d-(2I_d+2R(iy)),
\]

or

\[
R(iy)\succeq I_d.
\tag{10}
\]

Every positive scalar compression inherits WI-145's hyperbolic condition:

\[
v^*R(iy)v\ge\|v\|^2.
\tag{11}
\]

This does not force the matrix Fourier profile to be pointwise PSD. WI-146 already shows in the scalar case that two-point real/imaginary tests can be compatible with signed spectral mass protected by farther-out positive repair. The new point here is different: for support-one one-delta optimization, Fourier-side positivity is unnecessary. Real-gap Loewner positivity alone is enough for WI-154.

## 3. Automatic reduction to the sharp scalar extremal problem

Assume now that `R|_R` is continuous, even, entrywise integrable, and

\[
\operatorname{supp}\widehat R\subset[-1,1]
\tag{12}
\]

entrywise. By Section 1, `R(x)\succeq0` for every real `x`. Therefore all hypotheses of WI-154 hold, and for

\[
\mathcal M(R)
:=\int_{\mathbb R}R(x)
\left[1-\left(\frac{\sin \pi x}{\pi x}\right)^2\right]dx
\tag{13}
\]

we obtain the exact Loewner lower bound (5).

Equivalently, if `Phi=widehat R`, then

\[
\Phi(0)+\int_{-1}^{1}|t|\Phi(t)\,dt
\succeq
C_{\rm MT}I_d,
\qquad
C_{\rm MT}
=\frac12+\frac1{\sqrt2}\cot\frac1{\sqrt2}.
\tag{14}
\]

The implication is purely structural:

\[
\text{universal Loewner census (2)}
\Longrightarrow
R(x)\succeq0\text{ on real gaps}
\Longrightarrow
\text{sharp scalar-compression constant (5).}
\tag{15}
\]

Hence adding matrix channels cannot lower the support-one one-delta cost if the matrix zero-side theorem has the direct universal form (2). Applying any positive linear functional to (5) preserves the same constant.

WI-154 also gives equality rigidity. If equality holds in (5), then the real-axis restriction must satisfy

\[
R(x)=R_{\rm MT}(x)I_d,
\tag{16}
\]

where `R_MT` is the unique normalized scalar CCLM extremizer. Equation (16) is only a **necessary real-axis condition** for equality inside the direct census class; it is not asserted here that the scalar CCLM extremizer itself satisfies the full complex-multiset inequality (2).

## 4. Why this is distinct from WI-144--WI-146

WI-144 treated matrix channels arising from a positive Hilbert feature or PSD spectral density and showed that coherent scalar collapse/Frobenius energy remains Fourier-positive. The present argument assumes none of that structure. The matrix Fourier transform may be indefinite and the kernel need not come from a positive operator-valued spectral measure.

WI-145 then showed that a universal **scalar** Lamzouri-form pair-sum kernel must obey `H(iy)>=1`, excluding a genuine uncompensated CGdL negative outer tail. WI-146 showed that the complete scalar two-point tests do not force Fourier positivity: remote positive spectral repair can hide a negative intermediate band.

WI-154 moved in a different direction: if a matrix real-gap kernel happens to be pointwise PSD, scalar compression already forces the sharp one-delta constant. The missing logical link for the most direct matrix census was whether that real-gap PSD property could be avoided. Equations (6)--(7) show it cannot: **the universal Loewner version of Lamzouri's own two-real-point census forces precisely the hypothesis that WI-154 needs.**

Thus remote signed spectral repair of the WI-146 type does not rescue this direct support-one matrix route. It may keep the Fourier profile sign-indefinite, but it cannot make any real-gap quadratic compression negative while (2) remains valid.

## 5. Scope boundary and surviving matrix routes

The Loewner placement of the count in (2) is load-bearing. A more complicated theorem may produce only a scalar inequality after an indefinite channel contraction, or may combine several matrices before any positivity statement is available. Such a construction need not imply (3).

Likewise, (2) uses **one translation-invariant pair-sum matrix kernel** for every finite conjugation-invariant multiset. A zeta-specific theorem could exploit relations unavailable to arbitrary multisets. A nonlinear joint constraint can couple several profile statistics without asking each channel direction to satisfy a Lamzouri census separately. A block-inertia certificate may be sign-indefinite locally and become useful only after a global rank/signature argument. None of those architectures is covered.

The support-one hypothesis enters only when passing from (3) to the sharp CCLM constant (5). Wider support changes the extremal problem and requires independently justified arithmetic information. Higher-order zero correlations also lie outside the pair-sum interface (2), so this finding does not resolve `CLUE-higher-zero-correlations-horizontal-rigidity`.

Finally, (5) is not a ceiling on the stronger certified bounds in this research line obtained from local Gram defect and nonlinear spectral geometry. It closes a proposed **replacement of the scalar one-delta pair kernel by a direct Loewner matrix kernel**, not every use of matrices inside the full Weil/inertia method.

## 6. Prior-art and novelty audit

The primary finite zero-side source is Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1 (2 September 2026), Proposition 2.1. Lamzouri proves for a scalar kernel `K=widehat(eta^2)` the universal inequality

\[
s(\mathcal Z)\ge2|\mathcal Z|-\sum_{z,w\in\mathcal Z}K(z-w)^2
\]

for every finite conjugation-invariant multiset. The operator statement (2) is **not** attributed to Lamzouri; it is the natural hypothetical Loewner lift tested here.

The sharp support-one scalar extremal input is Emanuel Carneiro, Vorrapan Chandee, Friedrich Littmann and Micah B. Milinovich, *Hilbert spaces and the pair correlation of zeros of the Riemann zeta-function*, J. Reine Angew. Math. 725 (2017), 143--182, arXiv:1406.5462, especially the one-delta extremal problem used in WI-153 and WI-154. No new scalar extremal theorem is claimed.

General matrix/operator-valued positive-definite kernels, matrix moment problems, and operator-valued Bochner theory are classical and were audited in WI-144/WI-154. A targeted literature search around matrix-valued Delsarte/Loewner finite-configuration inequalities and operator-valued extremal kernels located general matrix interpolation and positive-kernel theory, but no zeta-specific source supplying a direct matrix Lamzouri census or an escape from the two-point implication (7). No priority claim is made for the elementary Loewner two-point observation.

The Mathia contribution recorded here is the **closure of the exact gap left by WI-154 for the direct universal matrix lift**: if the scalar counting theorem is promoted to Loewner order without changing its Lamzouri pair-sum architecture, the two-real-point configuration itself forces the matrix kernel into the pointwise-PSD cone where the scalar CCLM extremizer is already sharp.

## Research consequence

The direct route

\[
\text{Lamzouri universal pair census}
\to
\text{one matrix kernel in Loewner order}
\to
\text{better support-one one-delta constant}
\]

should be treated as closed. Matrix dimension, noncommuting values, and an indefinite Fourier-side matrix do not help because the universal two-real-point test enforces `R(x)\succeq0` before the arithmetic optimization begins.

A credible matrix escape now has to be genuinely more than a Loewner-valued rewrite of the scalar census: sign-indefinite local blocks with global signature control, nonlinear multi-profile coupling, configuration-dependent/zeta-specific constraints, higher correlations, or wider support backed by new arithmetic information.