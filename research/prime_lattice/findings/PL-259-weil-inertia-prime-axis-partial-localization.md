# PL-259 — Weil second moments turn prime-axis data into unconditional partial critical-line localization

**Evidence:** `LITERATURE+DERIVED`

**Status:** `POSITIVE-MECHANISM + SHARP-BOUNDARY + PRIOR-ART-REDIRECT`

## Claim

Alpöge--Furman (2026) give an unconditional theorem in which a finite compression of Weil's Hermitian form converts the prime-power part of the explicit formula into genuine information about the **horizontal location** of Riemann zeros: at least

\[
\left(\frac23-o(1)\right)N(T,2T)
\]

zeros, counted with multiplicity, are simple and lie on `Re(s)=1/2`, and at least `(5/6-o(1))N(T,2T)` are distinct. With the Montgomery--Taylor window the constants improve to about `0.6725` and `0.8362`. Their zero-side mechanism uses rank and inertia of an indefinite Hermitian form rather than assuming Weil positivity/RH.

For the prime-exponent lattice this has a precise interpretation: the finite-prime input is supported only on the **prime-power axis rays**

\[
\alpha=r e_p,
\qquad
E(\alpha)=r\log p,
\]

because the von Mangoldt weight vanishes away from prime powers. Thus a source-determined Hermitian object fed only by the `log p` axis-ray spectrum can already force a nontrivial unconditional proportion of the Riemann divisor onto the self-dual line.

This is an important positive correction to the more pessimistic spectral redirects in `PL-013`, `PL-044`, `PL-254`, `PL-257`, and `PL-258`: **divisor-complete realization as the spectrum of one fixed self-adjoint operator is not necessary for obtaining rigorous zero-location information.** A source-forced indefinite Hermitian form together with an arithmetic second-moment estimate can already localize many zeros.

The result does **not** provide an RH mechanism. Alpöge--Furman's own audit states that the inputs are insensitive to `o(N)` off-line zeros. Lamzouri (2026) then reproves the same optimized localization by a direct Hilbert-space/pair-correlation inequality, without the finite-matrix framework. Consequently the durable mechanism is the **Weil/pair-correlation first-two-moment structure**, while finite-matrix inertia is a particularly transparent realization of it, not a uniquely load-bearing Hilbert--Pólya operator.

## 1. Prime-exponent reconstruction of the arithmetic side

Write

\[
n=\prod_p p^{v_p(n)},
\qquad
E(v(n))=\sum_p v_p(n)\log p=\log n.
\]

The prime term in the explicit-formula compression is a Dirichlet polynomial of the form

\[
P_X(\tau)
 =-\frac1\pi\sum_{n\le X}
   \frac{\Lambda(n)}{\sqrt n}\cos(\tau\log n),
\]

up to the paper's fixed Fourier normalization. Since

\[
\Lambda(n)\ne0
\quad\Longleftrightarrow\quad
n=p^r,
\]

this is exactly

\[
P_X(\tau)
 =-\frac1\pi
 \sum_{p^r\le X}
 (\log p)p^{-r/2}
 \cos(\tau r\log p)
\]

or, in lattice coordinates,

\[
P_X(\tau)
 =-\frac1\pi
 \sum_{r e_p:\ E(r e_p)\le\log X}
 (\log p)e^{-E(r e_p)/2}
 \cos\!\bigl(\tau E(r e_p)\bigr).
\tag{1}
\]

Equation (1) is the line-specific content: the full positive cone `N_0^(P)` does not enter directly. The completed explicit formula projects its rational-prime arithmetic onto the one-coordinate rays `r e_p`, with precisely the frequencies

\[
\langle r e_p,(\log q)_q\rangle=r\log p.
\]

Mixed-prime exponent vectors are absent from the finite-prime source term. Any claim that the Alpöge--Furman theorem exploits the whole exponent lattice would therefore be false.

The analytic continuation boundary is also clean. The zero/prime identity being used is Weil's **completed explicit formula**, whose archimedean term and zero divisor are already part of the continued object. Nothing here is obtained by formally extending the Euler product or a termwise identity from `Re(s)>1` into the critical strip.

## 2. Zero-side signature records horizontal displacement

For a nontrivial zero `rho`, use the centered coordinate

\[
z_\rho=\frac{\rho-1/2}{i}.
\]

Then

\[
\rho=\frac12+i\gamma
\quad\Longleftrightarrow\quad
z_\rho\in\mathbb R.
\]

The finite family of translated/modulated test functions produces vectors `v_rho` and a real symmetric/Hermitian compression `\widetilde G`. For an on-line zero, `v_rho` is real and its contribution is a positive rank-one atom

\[
m_\rho v_\rho v_\rho^{\mathsf T}\succeq0.
\]

For an off-line functional-equation pair, the centered parameters are conjugate. Write

\[
v_\rho=a+ib,
\qquad a,b\in\mathbb R^d.
\]

The paired contribution is

\[
m_\rho\left(
 v_\rho v_\rho^{\mathsf T}
 +\overline{v_\rho}\,\overline{v_\rho}^{\mathsf T}
 \right)
 =2m_\rho(aa^{\mathsf T}-bb^{\mathsf T}).
\tag{2}
\]

Thus one off-line pair contributes a pullback of a form of signature `(1,1)` and can add at most one positive and one negative direction. This is substantially more informative than ordinary self-adjoint spectral reality: **the sign geometry changes according to whether the zero parameter is real after centering, i.e. according to whether `Re(rho)=1/2`.**

Alpöge--Furman combine (2) with Sylvester-type inertia control to separate the positive-semidefinite part carried by simple critical zeros from the residual part carried by multiplicities and off-line pairs.

## 3. Arithmetic first and second moments force a positive critical-line proportion

The prime side of the explicit formula evaluates the relevant aggregate moments of the compression. In the basic window normalization,

\[
\operatorname{tr}\widetilde G=(1+o(1))N,
\qquad
\|\widetilde G\|_{\mathrm{HS}}^2
 =\left(\frac43+o(1)\right)N,
\tag{3}
\]

where `N=N(T,2T)` at the scale of the zero window. A rank--trace inequality for a decomposition into an on-line positive part and an inertia-controlled remainder then forces

\[
N_{0}^{\mathrm{simple}}(T,2T)
 \ge \left(\frac23-o(1)\right)N(T,2T).
\tag{4}
\]

Optimizing the test window through the Montgomery--Taylor extremal problem improves the constant to approximately `0.6725`.

The important structural point for this research line is that (3)--(4) are not an arbitrary operator encoding of zeta. The matrix is a finite compression of the classical Weil form; its entries are fixed by the completed explicit formula; the arithmetic moments are evaluated from the von-Mangoldt/prime-power source; and the zero-side sign structure follows from the functional-equation pairing. The mechanism therefore passes the line's source-determination and continuation controls.

## 4. Matched control: matrix inertia is not uniquely load-bearing

Lamzouri's September 2026 proof is a decisive novelty/adversarial control. It obtains the same Montgomery--Taylor constant by replacing the finite-dimensional matrix/rank--trace machinery with a Hilbert-space inequality for a conjugation-invariant multiset of complex zero parameters, followed directly by the unconditional pair-correlation theorem.

Lamzouri explicitly observes that both arguments reduce the needed information to a quadratic form/second-moment estimate over the zeros and therefore to the same Montgomery--Taylor extremal problem. Consequently it would be an overclaim to interpret `\widetilde G` itself as a newly discovered Hilbert--Pólya matrix or to treat its inertia packaging as the unique arithmetic rigidity.

The robust common mechanism is instead

\[
\text{completed explicit formula}
\ +\ 
\text{conjugation/functional-equation symmetry}
\ +\ 
\text{unconditional pair-correlation second moment}
\ \Longrightarrow\ 
\text{positive-proportion critical-line localization}.
\]

Alpöge--Furman's Hermitian compression remains especially useful for `prime_lattice` because it makes the signature contribution (2) geometrically explicit.

## 5. Why this does not approach RH by window optimization alone

The result is a **proportion theorem**, not an exclusion theorem. Alpöge--Furman emphasize that their inputs are insensitive to `o(N)` off-line zeros. Therefore even an asymptotic density-one conclusion from the same kind of aggregate data would still permit a finite or zero-density exceptional set and would not imply RH.

Their sharpness discussion also shows that the first-two-moment certificate has extremal configurations compatible with a residual population not individually localized. Pushing the test window can improve the constant, but it does not change the logical type of information: trace/second moment plus aggregate inertia cannot by itself certify the absence of every off-line pair.

At larger Fourier support/higher moments, the prime side stops being controlled by only the easy diagonal. One encounters prime-pair and higher additive/multiplicative correlations of Hardy--Littlewood/Rudnick--Sarnak type. Such stronger arithmetic input may improve density statements, but **density improvement is still not an RH proof unless it yields a uniform local certificate excluding each exceptional pair.**

A useful falsification test for any proposed extension of this route is therefore:

> Can the proposed observable distinguish two admissible zero configurations having the same asymptotic first/second moments but differing by one, finitely many, or `o(N)` off-line functional-equation pairs?

If not, it cannot close the RH gap, regardless of how close its asymptotic critical-line proportion is to `100%`.

## 6. Relation to existing `prime_lattice` evidence

This result does not supersede the earlier negative findings; it separates two notions that they had left too close together.

- `PL-013` records the classical Weil prime-power-axis spectral-triple route and the missing infinite spectral-convergence/positivity bridge. `PL-259` shows that a **finite, indefinite** Weil compression nevertheless yields unconditional horizontal-location information through inertia and moments.
- `PL-044` shows that ordinary localized self-adjoint spectral reality can persist in a prime-free regime and therefore is not itself arithmetic evidence. Here the useful readout is not mere reality of eigenvalues; it is the source-forced **signature decomposition** of zero contributions plus prime-side moments.
- `PL-254`, `PL-257`, and `PL-258` show that placing zeros in a spectral/transfer parameter set does not force them onto the self-dual line. `PL-259` demonstrates a different route: one need not realize every zero as a fixed operator eigenvalue in order to prove a quantitative localization theorem.
- `PL-109` already shows that prime-power axis data can be RH-complete in a Lindelöf-type criterion. `PL-259` gives a different, unconditional axis-ray mechanism, but only at aggregate density level.

The line should therefore not require a future mechanism to look like a single self-adjoint Hilbert--Pólya operator. A viable alternative is a **source-determined sign/inertia or local-defect certificate** whose arithmetic side is strong enough to detect an individual off-line pair.

## 7. Research consequence

The most useful next target is now sharper than "find positivity" or "find a spectrum containing the zeros":

\[
\boxed{
\text{construct a source-forced local certificate whose sign/inertia changes for every off-line pair,}
\\
\text{and control that certificate arithmetically without averaging away a sparse exceptional set.}
}
\]

The Alpöge--Furman/Lamzouri breakthrough proves that prime-axis explicit-formula data plus finite-dimensional/Hilbert geometry can genuinely cross from vertical pair statistics to horizontal zero localization. Its limitation identifies the missing scale: **individual or uniformly local zero exclusion**, not another optimization of an asymptotic second moment.

No formalization handoff is opened for this finding. Alpöge--Furman already provide a Lean 4 formalization of their main theorem and principal finite-dimensional ingredients against Mathlib's `riemannZeta`; the exponent-coordinate rewrite of von-Mangoldt support in (1) is immediate and does not expose a separate fertile theorem boundary.

## Prior art and novelty audit

1. **Levent Alpöge, Ralph Furman**, “More than two thirds of the zeta zeros are simple and on the critical line,” arXiv:2608.13637v2 [math.NT], submitted 13 August 2026, revised 19 August 2026. https://arxiv.org/abs/2608.13637
   - Primary theorem-level source for the unconditional `2/3`, `5/6`, and Montgomery--Taylor improvements; the finite Weil compression, rank--trace inequality, off-line `(1,1)` inertia blocks, sharpness discussion, and accompanying Lean formalization are all source results.

2. **Youness Lamzouri**, “A new proof that more than `2/3` of the zeros of the Riemann zeta function are simple and on the critical line,” arXiv:2609.02882 [math.NT], submitted 2 September 2026. https://arxiv.org/abs/2609.02882
   - Matched control. Replaces the finite matrix/rank--trace framework by a direct Hilbert-space inequality and unconditional pair correlation, while recovering the same optimized constant. This rules out treating the matrix formalism as uniquely responsible for the localization.

3. **André Weil**, “Sur les ‘formules explicites’ de la théorie des nombres premiers,” *Comm. Sém. Math. Univ. Lund* (1952), 252--265.
   - Classical source of the explicit-formula Hermitian form and positivity criterion lineage.

4. **Enrico Bombieri**, “Remarks on Weil’s quadratic functional in the theory of prime numbers, I,” *Atti Accad. Naz. Lincei Rend. Lincei Mat. Appl.* **11**(3) (2000), 183--233.
   - Classical prior art for the relationship between finite Weil forms, positivity/inertia, and off-line zero pairs. Alpöge--Furman explicitly credit Bombieri for the negative-index observation.

### Novelty classification

The theorem and finite Hermitian construction are **not Mathia discoveries**. The only derived line-specific step is the exact exponent-coordinate identification of the von-Mangoldt source with the axis-ray set `{r e_p}` and the resulting research redirect: an indefinite source-forced Hermitian form can carry authentic critical-line information even though ordinary spectral reality and divisor realization do not.

This is stored because it materially changes the viable mechanism class for `prime_lattice`, while its matched-control and sparse-exception boundary prevent overclaiming progress toward RH.