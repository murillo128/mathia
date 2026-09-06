# WI-186 — black-box signed form-factor postprocessing cannot beat the bow resolution scale

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE`. This finding strengthens the support-one bow barrier of WI-185. It does **not** say that the true errors in the unconditional Montgomery theorem fail to cancel under a specially designed signed transform. It says that such cancellation cannot be certified by treating the currently published pointwise theorem as a black box: every signed linear combination inherits an error budget proportional to the total variation of its coefficients, and the selected bow principal form scales by the same total variation. Therefore algebraically cancelling the displayed main terms does not improve the guaranteed signal-to-error ratio for a sparse Maynard--Pratt bow. Any successful signed-observable escape must reopen the arithmetic proof and prove correlated error cancellation, or use genuinely different information such as short-height localization, non-principal coupling, or wider support.

## 1. Corrected unconditional pointwise input

Write

\[
L:=\log T,
\qquad
x=T^\alpha.
\]

The corrected Montgomery theorem in Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh, *Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions of Simple Zeros and Critical Zeros*, arXiv:2501.14545v3 (revised 1 Sep 2026), states uniformly for `1<=x<=T`

\[
\mathcal F(x,T)
=
\frac{T}{2\pi x^2}L^2
\left(1+O(L^{-1/2})\right)
+
\frac{T}{2\pi}\log x
+
O(T\sqrt L).
\tag{1}
\]

Thus for `x=T^alpha`,

\[
\mathcal F(T^\alpha,T)=M_T(\alpha)+E_T(\alpha),
\tag{2}
\]

where

\[
M_T(\alpha)
:=
\frac{T}{2\pi}T^{-2\alpha}L^2
+
\frac{T}{2\pi}\alpha L
\tag{3}
\]

and, uniformly for `0<=alpha<=1`,

\[
|E_T(\alpha)|
\ll
T^{1-2\alpha}L^{3/2}+T\sqrt L.
\tag{4}
\]

In particular, for every fixed `a>0`,

\[
\boxed{
\sup_{a\le\alpha\le1}|E_T(\alpha)|
\ll_a T\sqrt L.
}
\tag{5}
\]

No hypothesis on RH is used in (1)--(5). The revised paper explicitly records that the `O(T sqrt(log T))` term corrects the earlier lower-order error bookkeeping and now holds over the whole range `1<=x<=T`.

## 2. Signed linear postprocessing inherits total-variation error

Let `mu_T` be an arbitrary finite real signed Borel measure supported in `[a,1]`, where `a>0` is fixed. The measure may depend on `T`; finite differences and finite signed portfolios are included as atomic special cases. Define

\[
\mathcal L_{\mu}(T)
:=
\int_a^1 \mathcal F(T^\alpha,T)\,d\mu_T(\alpha).
\tag{6}
\]

Integrating (2) and applying only the pointwise estimate (5) gives

\[
\boxed{
\left|
\mathcal L_{\mu}(T)
-
\int_a^1 M_T(\alpha)\,d\mu_T(\alpha)
\right|
\ll_a
T\sqrt L\,\|\mu_T\|_{\rm TV}.
}
\tag{7}
\]

This remains true if the coefficients of an atomic portfolio grow with `T`; their growth is already recorded in `||mu_T||_TV`.

The key point is that (7) does not improve when the signed coefficients cancel the known main terms. Even granting the strongest possible algebraic cancellation

\[
\int_a^1 M_T(\alpha)\,d\mu_T(\alpha)=0,
\tag{8}
\]

one obtains from the published theorem, as a black box, only

\[
\boxed{
|\mathcal L_{\mu}(T)|
\ll_a
T\sqrt L\,\|\mu_T\|_{\rm TV}.
}
\tag{9}
\]

This total-variation dependence is not an artifact of a loose manipulation that can be removed while keeping exactly the same input. Abstractly, if the only information retained about an error family is the pointwise envelope `|E_T(alpha)|<=C T sqrt(L)`, then for any prescribed signed measure the admissible error family can align its sign with the Radon--Nikodym sign of `mu_T`, giving a linear-functional error of order `T sqrt(L)||mu_T||_TV`. Therefore no correlated cancellation theorem for `E_T(alpha)` follows from the pointwise statement alone. Proving such cancellation would be **new arithmetic information about the joint error as alpha varies**, not a different choice of coefficients applied to (1).

If support reaches `alpha=0`, the additional first-term uncertainty in (4) is larger, not smaller. Hence restricting to a fixed positive lower endpoint is the most favorable regime for this black-box test and already contains the reciprocal frequencies relevant to a fixed-spacing bow.

## 3. The bow principal signal scales by the same total variation

WI-185 proves for a mirror-closed Maynard--Pratt bow with `m` ordinate sites, spacing `c/L` with fixed `c>0`, and selected real parts in `[1/4,3/4]` that

\[
0\le
\mathcal F_{\mathcal B}(T^\alpha)
\ll_c
mL T^{\alpha/2},
\qquad 0\le\alpha\le1.
\tag{10}
\]

Consequently every signed portfolio from Section 2 satisfies

\[
\boxed{
\left|
\int_a^1
\mathcal F_{\mathcal B}(T^\alpha)
\,d\mu_T(\alpha)
\right|
\ll_c
mL\sqrt T\,\|\mu_T\|_{\rm TV}.
}
\tag{11}
\]

Comparing (11) with the guaranteed black-box uncertainty (7) gives the scale ratio

\[
\boxed{
\frac{
\text{selected bow principal scale}
}{
\text{pointwise-theorem signed-error scale}
}
\ll_{a,c}
\frac{m\sqrt L}{\sqrt T}.
}
\tag{12}
\]

The total variation cancels completely. Making the coefficients larger, using a high-order finite difference, or tuning them to annihilate both displayed main terms cannot change this ratio while the proof uses only the pointwise theorem plus absolute error propagation.

Hence

\[
\boxed{
m=o\!\left(\sqrt{T/L}\right)
\quad\Longrightarrow\quad
\text{the bow principal signal is sub-resolution for every such black-box signed portfolio.}
}
\tag{13}
\]

For the Maynard--Pratt obstruction `m=T^epsilon`, every fixed `epsilon<1/2` satisfies (13) by a polynomial margin.

More generally, combining WI-185's horizontal-width bound

\[
\mathcal F_{\mathcal B}(T^\alpha)
\ll mL T^{2\delta\alpha}
\tag{14}
\]

for `|beta-1/2|<=delta` with a signed portfolio supported in `[a,A]`, `A<=1`, gives

\[
\frac{\text{principal signal}}{\text{black-box pointwise error}}
\ll
m\sqrt L\,T^{2\delta A-1}.
\tag{15}
\]

Thus signed reweighting does not alter the theorem-resolution threshold

\[
\boxed{
m\asymp \frac{T^{1-2\delta A}}{\sqrt{\log T}}}
\tag{16}
\]

that is forced by the published pointwise error scale.

## 4. Why exact cancellation of the bulk is not enough

A tempting response to WI-185 is to choose coefficients `c_j` and frequencies `alpha_j` so that the `Theta(TL)` background cancels, for example

\[
\sum_j c_j M_T(\alpha_j)=0,
\tag{17}
\]

while a reciprocal bow harmonic survives. Equation (12) isolates why this does not yet buy a theorem. The cancellation in (17) concerns the **known main term**. The current unconditional source theorem supplies separate uniform error envelopes at the chosen frequencies but no covariance, common expansion, differentiability estimate, or signed mean theorem for those errors. Triangle inequality therefore pays

\[
T\sqrt L\sum_j|c_j|,
\tag{18}
\]

while WI-185 bounds the selected bow principal response by

\[
mL\sqrt T\sum_j|c_j|.
\tag{19}
\]

The same coefficient norm multiplies both sides. Algebraic cancellation of (17) cannot turn a `T^epsilon`, `epsilon<1/2`, bow into a visible source unless the arithmetic analysis also proves cancellation or a smaller error for the particular transform.

This is a logical information barrier, not a claim about the unknown true errors. The actual errors at different frequencies may have strong correlations. What is ruled out is obtaining those correlations **for free** from the already-published pointwise asymptotic.

## 5. Stress tests and escape routes

**Positivity/extraction.** A signed `mu_T` also loses the pointwise positivity enjoyed by `F_B(T^alpha)`. The estimate here is deliberately generous: it assumes that the selected principal block can already be isolated and asks only whether signed frequency postprocessing improves its scale. It does not solve the extraction problem of WI-184--WI-185.

**Cross terms.** The complete BGSTB square contains bow--reservoir cross terms. They are not bounded by (11) and could in principle carry a larger source-compatible signal. Exploiting them would be a genuinely different non-principal coupling mechanism, not a counterexample to this finding.

**Correlated arithmetic errors.** Reopening the proof of the Montgomery theorem and deriving a signed transform directly on the prime side may produce cancellation substantially better than (18). Such a theorem would evade the black-box hypothesis and is one of the explicit remaining routes.

**Short-height localization.** A form factor normalized to the bow's own height window could change both the natural main scale and the arithmetic error. WI-185 already identifies local/short-height normalization as a high-value escape; nothing here obstructs it.

**Wider support.** Equation (16) changes with `A`. Unconditionally established support in this interface is `A<=1`; justified support extension is new arithmetic information and lies outside this no-go statement.

**Near zero frequency.** Allowing mass near `alpha=0` exposes the additional `T^{1-2alpha}L^{3/2}` uncertainty in (4). Without a new uniform refinement it worsens, rather than improves, the black-box resolution.

## 6. Prior-art audit and evidence boundary

The load-bearing arithmetic statement is the corrected Montgomery theorem in arXiv:2501.14545v3, equation (3.2), whose error is quoted above exactly at the scale used in this finding. Its Lemma 1 supplies the positive squared-modulus representation underlying WI-185's selected principal form.

Frequency averaging and Fourier optimization of Montgomery's form factor are classical and active prior art. In particular:

- Andrés Chirre, Felipe Gonçalves and David de Laat, **Pair correlation estimates for the zeros of the zeta function via semidefinite programming**, *Advances in Mathematics* 361 (2020), 106926, DOI `10.1016/j.aim.2019.106926`, optimizes pair-correlation test functions via semidefinite programming;
- Emanuel Carneiro, Vorrapan Chandee, Andrés Chirre and Micah B. Milinovich, **On Montgomery's pair correlation conjecture: a tale of three integrals**, *J. Reine Angew. Math.* 786 (2022), 205--243, DOI `10.1515/crelle-2021-0084`, studies bounded-interval averages of the form factor under RH;
- Emanuel Carneiro, Micah B. Milinovich and Antonio Pedro Ramos, **Fourier optimization and Montgomery's pair correlation conjecture**, *Mathematics of Computation* 94 (2025), 409--424, DOI `10.1090/mcom/3990`, develops discrete and continuous averaging mechanisms for long form-factor intervals under RH.

These works show that averaging itself is not new. They do not supply the missing unconditional **correlated error theorem for the corrected complex-zero support-one asymptotic** needed to beat (18) for a selected sparse bow. A targeted search in this pass found no source stating the specific total-variation bow-resolution consequence (12)--(16). Absence from that search is not evidence of priority, and no novelty claim is made.

The exact Mathia delta is narrower: WI-185 left signed transforms open because cancellation of the global background might conceivably expose a sparse principal block. Equations (7)--(13) close the subclass in which the signed transform is justified only by black-box linear postprocessing of the current pointwise BGSTB theorem. They do **not** close signed transforms proved directly from the arithmetic source.

## 7. Research consequence

After WI-185, coefficient optimization at the level of the published support-one asymptotic is no longer a useful RH-facing route. The source obstruction is twofold:

\[
\text{principal bow scale}
\ll mL\sqrt T,
\qquad
\text{black-box signed uncertainty}
\asymp T\sqrt L,
\tag{20}
\]

with the same coefficient total variation multiplying both. For `m=T^epsilon`, `epsilon<1/2`, the gap is polynomial.

The next signed-observable attempt must therefore prove something stronger than a cancellation identity among known main terms. It must establish a **joint arithmetic estimate for the chosen transform** whose error cancels before absolute values are taken, or replace the global principal form by a locally normalized or non-principal observable. This narrows the route without changing the established unconditional simple-critical-zero proportion and without claiming an RH conclusion.