# WI-368 — Desogus's printed gamma cancellation uses the kernel with the wrong quadratic-form sign

**Status:** `EXACT-DERIVED + PRIMARY-SOURCE-CRITICAL-AUDIT + DECISIVE-SECTION5-BARRIER + NON-ESTABLISHED-RH`.

## Claim

The scalar kernel identity printed as equation (59) in Marco Desogus's *The Three Gates: A Rooted-Operator Approach to Weil Positivity* (`arXiv:2609.20367v1`) is algebraically correct, but it does **not** give the claimed cancellation of the regular gamma term in the quadratic form. The Cauchy kernel enters a closed difference form with the opposite off-diagonal sign.

In the `(0,1)` normalization of WI-367, write

\[
K_C^{(A)}(u,v)=\frac{Ae^{-A|u-v|/2}}{1-e^{-A|u-v|}},
\qquad
K_H^{(A)}(u,v)=\frac{Ae^{-A|u-v|/2}}{1+e^{-A|u-v|}}.
\tag{1}
\]

The paper's Lemma 5.1, equivalently WI-367, gives

\[
\boxed{
\frac12\bigl(K_C^{(A)}+K_H^{(A)}\bigr)
=
\frac1{2|u-v|}+A\rho(A|u-v|).
}
\tag{2}
\]

Desogus then subtracts the explicit gamma kernel `A rho(A|u-v|)` at the **positive-kernel** level and concludes that only `1/(2|u-v|)` remains. But the singular term used in Proposition 5.3 is the closed difference form

\[
q_C[f]
=
\frac14\iint
\frac{|f(x)-f(y)|^2}{|x-y|}\,dx\,dy.
\tag{3}
\]

After polarization, its off-diagonal operator kernel is **minus one half** of the transported Cauchy kernel. For the exact Cauchy--Carleman source realization reconstructed in WI-367,

\[
q_C[f]-\frac12\langle f,K_{\rm Carl}f\rangle
+\text{diagonal multiplier},
\tag{4}
\]

the transported off-diagonal kernel is therefore

\[
\boxed{
-\frac12\bigl(K_C^{(A)}+K_H^{(A)}\bigr)
=
-\frac1{2|u-v|}-A\rho(A|u-v|).
}
\tag{5}
\]

Equation (5) is exactly the off-diagonal kernel of the normalized collar form

\[
\mathfrak b-K_{\gamma,A},
\tag{6}
\]

not of the gamma-free collar `mathfrak b`. Thus the regular gamma term is already part of the transported full archimedean form. Treating the `+A rho` on the right of (2) as a further positive operator contribution that cancels the explicit `-K_{gamma,A}` reverses the sign supplied by the quadratic difference form.

No scalar, endpoint potential, or diagonal/killing correction can repair this mismatch: on disjointly supported test functions all multiplication terms have zero cross-polarization, while the difference between (5) and the gamma-free cross-kernel is the genuinely nonlocal kernel `-A rho(A|u-v|)`, which is not identically zero.

Consequently, Lemma 5.2 and Proposition 5.3 do not establish the gamma-free one-cell collar used downstream. A repair must keep the true gamma-corrected channel and reprove the quantitative reserve, or introduce an additional **off-diagonal** source term and prove that the actual localized Weil form contains it. Pure diagonal bookkeeping cannot supply the missing cancellation.

This is a barrier to the printed Section 5 transport, not a proof that no repaired rooted-operator argument can work and not a proof or disproof of RH.

## 1. The sign carried by a closed difference form

For a symmetric kernel `K(u,v)`, define

\[
q_K[f,g]
=
\frac14\iint
(f(u)-f(v))\overline{(g(u)-g(v))}K(u,v)\,du\,dv.
\tag{7}
\]

Expanding and using symmetry gives

\[
q_K[f,g]
=
\frac12\int f(u)\overline{g(u)}
\left(\int K(u,v)\,dv\right)du
-
\frac12\iint f(u)\overline{g(v)}K(u,v)\,du\,dv.
\tag{8}
\]

Hence the off-diagonal operator kernel of `q_K` is `-K/2`. This minus sign is structural; it is not changed by closure, by a unitary change of variables, or by adding multiplication operators.

Under the half-density unitary

\[
(U_Af)(u)=\sqrt{Ae^{Au}}\,f(e^{Au}),
\tag{9}
\]

the source Cauchy and Carleman kernels become (1). The exact source completion found in WI-367 includes `-K_Carl/2`. Its off-diagonal operator kernel is therefore the left side of (5), and (2) immediately gives the right side of (5).

This is also a direct consistency check on WI-367's full identity

\[
\mathfrak c_A[U_A^{-1}g]
=
\mathfrak b[g]
-c_A\|g\|_2^2
-K_{\gamma,A}[g],
\tag{10}
\]

with the convention-dependent scalar `c_A=log A+log(2 pi)+gamma`. The exact diagonal multiplier derived there repairs the Jacobian/endpoint term, but it does not and cannot alter (5).

## 2. What equation (59) actually proves

Section 5 of `arXiv:2609.20367v1` states first the correct positive-kernel identity

\[
\frac12\bigl(K_C^{(A)}+K_H^{(A)}\bigr)
=
\frac1{2r}+A\rho(Ar),
\qquad r=|u-v|,
\tag{11}
\]

and then equation (59)

\[
\frac12\bigl(K_C^{(A)}+K_H^{(A)}\bigr)
-A\rho(Ar)
=
\frac1{2r}.
\tag{12}
\]

As a scalar identity, (12) is true. The issue is its interpretation. Proposition 5.3 immediately afterwards says that the singular part is represented by the closed difference form (3). In that form the kernel (11) contributes with the off-diagonal sign shown in (8), so the corresponding operator identity is

\[
-\frac12\bigl(K_C^{(A)}+K_H^{(A)}\bigr)
=
-\frac1{2r}-A\rho(Ar).
\tag{13}
\]

This is already the gamma-corrected target cross-kernel. There is no `+A rho` operator term available to cancel a separately subtracted `-K_{gamma,A}`.

Equivalently, there are only two consistent bookkeeping choices:

1. regard the Cauchy--Carleman source realization as the pullback of the full target `mathfrak b-K_gamma`; then (13) is the correct cross-kernel and the gamma term survives once;
2. build a source form whose transported cross-kernel is the gamma-free `-1/(2r)`; then that source form differs from the pullback of the full archimedean block by a nonlocal term, and its equality to the physical localized Weil form must be proved separately.

The printed argument combines the first description in Proposition 5.3 with the cancellation conclusion appropriate only to the second.

## 3. Diagonal completion cannot hide the discrepancy

The mismatch can be detected without assigning any value to the singular diagonal. Choose real smooth functions `phi, psi` with disjoint compact supports in `(0,1)` and with the two supports sufficiently close that `A|u-v|` lies in a region where `rho` does not vanish. Since

\[
\lim_{z\downarrow0}\rho(z)=\frac14,
\tag{14}
\]

such supports exist for every `A>0`.

For every multiplication operator `M`,

\[
\langle \phi,M\psi\rangle=0.
\tag{15}
\]

But the difference between the exact gamma-corrected cross-kernel (5) and the claimed gamma-free one is

\[
-A\rho(A|u-v|),
\tag{16}
\]

so for nonnegative `phi,psi` supported in a sufficiently small adjacent pair of intervals,

\[
-A\iint
\rho(A|u-v|)\phi(u)\psi(v)\,du\,dv\ne0.
\tag{17}
\]

Therefore no endpoint logarithm, scalar normalization, diagonal/killing term, or form closure can convert the exact full transport into a gamma-free collar. Any repair must modify the off-diagonal source content.

This disjoint-support test also separates the present issue cleanly from WI-363's original Jacobian multiplier. WI-367 repairs that multiplier exactly. Equation (17) survives after that repair.

## 4. Relation to WI-364--WI-367

WI-364 found that odd folding retains an image channel that the gamma-free bookkeeping did not display. WI-365 proved the corresponding exact image `J_A` is positive, so it may be dropped when only a lower bound is needed, but showed that doing so does not transport the numerical bare-Carleman OSPR reserve. WI-366 then ruled out the simplest uniform comparison `J_A >= c K` along the cofinal regime.

WI-367 solved the independent diagonal-transport problem and reconstructed the exact source multiplier needed for the full archimedean identity. The present finding strengthens its remaining caveat: the missing gamma-free step is not merely an omitted diagonal calculation. The printed cancellation in Lemma 5.2 uses the positive kernel (11) before the minus sign imposed by the difference form. Once Proposition 5.3 is interpreted as an equality of quadratic forms, the regular gamma term necessarily remains in the cross-kernel.

Thus the current source-to-cell gate is sharper:

\[
\boxed{
\text{the true gamma-corrected nonlocal channel must be retained or replaced by an exactly proved off-diagonal source identity.}
}
\tag{18}
\]

A diagonal repair is no longer a live escape route.

## 5. Consequence for the claimed OSPR reserve

The preprint's Section 4 computes the fixed normalized Carleman rebound

\[
d_*=0.493421929855680\ldots
\tag{19}
\]

for the bare kernel `K(u,v)=1/(u+v)`, and later combines it with the affine load in the strict reserve

\[
d_*-\delta_*\rho_{\rm aff}>0.005713\ldots.
\tag{20}
\]

Section 6 explicitly says that this reserve is to be used only after loss and rebound have been placed on the same transported fixed-target cut form. The sign mismatch above prevents Lemma 5.2--Proposition 5.3 from supplying that identification as written. The exact transported form carries the gamma-corrected channel instead.

This does **not** prove that no quantitative rebound exists for the true channel. It says that the printed value `d_*`, computed for the bare Carleman block, has not been transported to the exact full Weil form by the stated Section 5 argument. Any repaired proof must derive the reserve for the actual surviving operator or exhibit a separate exact bare-Carleman contribution with correct provenance.

## 6. Primary-source and novelty audit

The primary source is Marco Desogus, *The Three Gates: A Rooted-Operator Approach to Weil Positivity*, `arXiv:2609.20367v1`, submitted 17 September 2026. The load-bearing statements are Lemma 5.1 equations (56)--(58), Lemma 5.2 equation (59), equation (60)--(61), and Proposition 5.3. The source explicitly describes (59) as cancellation of the regular gamma kernel and Proposition 5.3 as transport of the complete quadratic form.

A fresh targeted web audit on 20 September 2026 searched for independent technical discussion or a correction of Desogus's Cauchy--Carleman/gamma cancellation. It located the primary arXiv submission and mirrors/summaries, but no independent source addressing this sign issue. Absence from that search is not evidence of priority, and no priority claim is made.

The algebra used here is elementary quadratic-form polarization plus the exact kernel transport already reconstructed in WI-367. The durable contribution is the source-specific audit conclusion: equation (59) is true only at the unsigned kernel level and cannot justify the gamma-free quadratic-form identity claimed downstream.

## 7. Falsification and scope

This finding can be falsified by exhibiting, from the actual localized Weil source form, an additional off-diagonal term whose transport contributes `+A rho(A|u-v|)` with the coefficient needed to remove (16), while preserving all other terms of equation (60). A multiplication correction is insufficient by (15)--(17).

Alternatively, a repaired proof may keep the gamma-corrected channel and establish the required cofinal reserve directly for that operator. WI-365--WI-366 leave that possibility open.

The finding does not audit the paper's finite interval certificates, common-cut Schur algebra, or final closure independently of this transport gate. It does not claim that every rooted-operator approach fails. It establishes only that the printed Section 5 cancellation does not follow as an equality of the complete quadratic form and therefore cannot presently support the later gamma-free Carleman reserve.

## Consequence for the research line

The diagonal/source normalization branch is now separated cleanly from the nonlocal gamma branch. WI-367 repairs the former. The latter has an exact sign obstruction inside the printed cancellation step: the regular gamma kernel is part of the correct transported cross-kernel rather than an extra positive term available for cancellation.

Future work should therefore stop searching for scalar or endpoint corrections to Lemma 5.2. The two mathematically live repair directions are source-explicit and testable: derive an additional off-diagonal term from the true explicit formula, or quantify the OSPR/Schur reserve of the actual gamma-corrected positive channel without replacing it by the bare Carleman operator.