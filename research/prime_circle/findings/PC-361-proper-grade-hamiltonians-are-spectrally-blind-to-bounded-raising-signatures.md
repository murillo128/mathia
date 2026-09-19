# PC-361 — proper grade Hamiltonians are spectrally blind to bounded raising signatures

- **Finding ID:** `PC-361`
- **Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE`
- **Workflow:** `DERIVED + PRIOR-ART AUDIT + ADVERSARIAL CONTROL`
- **Research line:** `prime_circle`
- **Result type:** exact unbounded-operator / compact-resolvent obstruction
- **Scope:** closes the most direct unbounded/closed-operator escape left by PC-358--PC-360: adding any bounded strictly degree-raising Prime-Circle signature multiplier to a proper diagonal grade Hamiltonian cannot move its ordinary eigenvalue spectrum, even when reciprocal parity is unbounded and no bounded source/control similarity is available
- **RH relevance:** high as a boundary result. The canonical tensor-degree Hamiltonian `N` produces a genuine unbounded compact-resolvent operator, but every bounded one-sided signature perturbation leaves its discrete spectrum exactly `N_0`; the Prime-Circle data survive only in eigenvectors, Riesz projections, Jordan geometry, resolvent norms, or other non-eigenvalue data. A spectral RH route must therefore use an intrinsically non-triangular domain/operator coupling, an unbounded signature term, or same-grade/backward/two-sided interactions.

## Claim

PC-355--PC-360 isolate an all-depth Prime-Circle signature tower in which the centered inversion defect acts by positive tensor degree. Finite truncations have only the eigenvalue `1`; fixed Hilbert metrics preserve reciprocal similarity; ratio-decaying completions make bounded positive-degree multipliers compact; and asymptotically geometric scalar grade weights reduce finite positive-degree polynomials to radial Fock multipliers modulo compacts. PC-360 deliberately leaves unbounded/closed spectralizations and genuinely infinite mixed-degree bounded multipliers outside its theorem.

The most canonical unbounded spectralization is to add the tensor-degree number operator. That does give compact resolvent, but it still cannot expose the Prime-Circle coefficients.

Let

\[
\mathcal H=\bigoplus_{m\ge0}\mathcal H_m,
\qquad 0<\dim \mathcal H_m<\infty,
\]

be any Hilbert completion of the graded Prime-Circle word space with finite-dimensional grades. Let a real grade energy `epsilon_m` satisfy

\[
\epsilon_m\to+\infty,
\]

and define the diagonal proper grade Hamiltonian

\[
H_0\vert_{\mathcal H_m}=\epsilon_m I,
\qquad
\mathcal D(H_0)=\left\{x:\sum_m |\epsilon_m|^2\|x_m\|^2<\infty\right\}.
\]

Let `Q` be **any bounded strictly grade-raising operator**,

\[
P_jQP_k=0\qquad\text{unless }j>k,
\tag{1}
\]

where `P_m` is the grade projection. No finite bandwidth, homogeneous norm summability, tensor-factorization, shell-diagonality, or arithmetic assumption is imposed on `Q`.

Set

\[
H=H_0+Q,\qquad \mathcal D(H)=\mathcal D(H_0).
\]

Then

\[
\boxed{\operatorname{Spec}(H)=\{\epsilon_m:m\ge0\}.}
\tag{2}
\]

Moreover, for every distinct energy value `lambda`, its algebraic multiplicity is exactly

\[
\boxed{
\operatorname{algmult}_H(\lambda)
=
\sum_{m:\,\epsilon_m=\lambda}\dim\mathcal H_m.
}
\tag{3}
\]

In particular, for the canonical number operator

\[
N\vert_{\mathcal H_m}=mI,
\]

one has

\[
\boxed{\operatorname{Spec}(N+Q)=\mathbb N_0,}
\qquad
\boxed{\operatorname{algmult}_{N+Q}(m)=\dim\mathcal H_m.}
\tag{4}
\]

Thus an arbitrary bounded all-depth Prime-Circle signature multiplier can be fully source-dependent and mix arbitrarily many higher degrees, yet the ordinary compact-resolvent spectrum of the natural grade Hamiltonian remains completely source-blind.

## 1. The perturbed grade Hamiltonian is closed with compact resolvent

Because `epsilon_m -> +infinity` and every grade is finite-dimensional, `H_0` is closed and has compact resolvent. Indeed, for a real `R` large enough that `epsilon_m+R>0` for every `m`,

\[
(H_0+R)^{-1}\vert_{\mathcal H_m}
=(\epsilon_m+R)^{-1}I,
\]

and these block eigenvalues tend to zero. Finite-dimensionality of each grade makes the resolvent compact even when `dim H_m` grows with `m`.

Since `Q` is bounded, `H=H_0+Q` is closed on the same domain. More explicitly, for `R` so large that

\[
\|Q\|\,\|(H_0+R)^{-1}\|<1,
\]

we have

\[
H+R
=\left(I+Q(H_0+R)^{-1}\right)(H_0+R),
\]

so `-R` lies in the resolvent and

\[
(H+R)^{-1}
=(H_0+R)^{-1}
\left(I+Q(H_0+R)^{-1}\right)^{-1}.
\tag{5}
\]

The first factor is compact and the second bounded. Hence `H` has compact resolvent. The same argument holds for the homotopy

\[
H_t=H_0+tQ,\qquad 0\le t\le1.
\tag{6}
\]

Therefore every finite spectral point of every `H_t` is an isolated eigenvalue of finite algebraic multiplicity.

## 2. Strict raising forces every eigenvalue onto the bare grade energies

Let `x != 0` satisfy

\[
H_t x=\lambda x.
\]

Because the grading starts at zero, there is a least `m` for which `x_m=P_mx` is nonzero. Condition (1) implies

\[
P_mQx=0:
\]

`Q` can reach grade `m` only from lower grades, and all lower components of `x` vanish. Projecting the eigenvalue equation onto grade `m` gives

\[
\epsilon_m x_m=\lambda x_m.
\]

Therefore

\[
\boxed{\lambda=\epsilon_m.}
\tag{7}
\]

Since `H_t` has compact resolvent, there is no additional continuous or residual spectrum at finite points. Thus, for every `t`,

\[
\operatorname{Spec}(H_t)\subseteq\{\epsilon_m:m\ge0\}.
\tag{8}
\]

This is the infinite-dimensional analogue of the elementary fact that adding a strictly triangular matrix does not change the diagonal eigenvalues, but here the diagonal part is unbounded and the conclusion applies to the full compact-resolvent operator.

## 3. No bare grade eigenvalue can disappear

Containment (8) does not by itself prove that every `epsilon_m` remains an eigenvalue, because a nonnormal infinite triangular perturbation could in principle create domain pathologies. Compact resolvent plus the bounded homotopy (6) removes that loophole.

Fix a distinct value `lambda` in the set `{epsilon_m}`. Since `epsilon_m -> +infinity`, the set of grade energies is discrete in every bounded interval and only finitely many grades have energy `lambda`. Choose a small positively oriented circle `Gamma_lambda` around `lambda` containing no other grade energy. Equation (8) implies

\[
\Gamma_\lambda\subset\rho(H_t)
\qquad\text{for every }t\in[0,1].
\]

The Riesz projection

\[
\Pi_\lambda(t)
=
\frac{1}{2\pi i}\int_{\Gamma_\lambda}(z-H_t)^{-1}\,dz
\tag{9}
\]

depends continuously on `t`; its finite rank is therefore constant on the connected interval `[0,1]`. At `t=0`,

\[
\operatorname{rank}\Pi_\lambda(0)
=
\sum_{m:\,\epsilon_m=\lambda}\dim\mathcal H_m.
\]

The same rank holds at `t=1`, proving (2) and (3). This also shows exactly what the raising perturbation may change: it can create nontrivial generalized eigenvectors and strongly nonnormal Riesz projections, but it cannot move, remove, or change the total algebraic multiplicity of any grade energy.

## 4. Prime-Circle consequence: unbounded parity is not enough

For the inversion-defect signature tower of PC-355--PC-360, a normalized all-depth left multiplier has the form

\[
L=I+Q,
\]

where its positive-degree part `Q` strictly raises tensor degree whenever it extends boundedly to the chosen completion. PC-358 showed that source and reciprocal control remain isospectral whenever the algebraic parity extends boundedly. PC-359 then noted that natural weighted completions can make that parity genuinely unbounded, so ordinary bounded-similarity arguments no longer apply.

The present result does **not** use parity at all. If the source positive-degree operator `Q_src` is bounded and strictly raising, then

\[
\operatorname{Spec}(N+Q_{src})=\mathbb N_0.
\]

If a matched reciprocal control also defines a bounded strictly raising `Q_ctl`, independently of whether the parity intertwiner between them is bounded, then separately

\[
\operatorname{Spec}(N+Q_{ctl})=\mathbb N_0.
\tag{10}
\]

So making reciprocal parity unbounded does not by itself create a spectral discriminator. The one-sided grading already freezes the eigenvalues before any source/control comparison is made.

This is stronger than the finite-truncation nilpotence in PC-355 and the finite triangular development of PC-351. Here the operator is genuinely unbounded, has compact resolvent, and may contain an arbitrary bounded infinite mixture of all positive tensor degrees. No finite-polynomial or norm-summable homogeneous decomposition is needed once the complete raising term is known to be bounded.

## 5. What survives outside the theorem

Equation (2) is only an ordinary-spectrum no-go. The Prime-Circle coefficients can remain visible in eigenvectors, generalized eigenspaces, Riesz-projection norms, resolvent growth, pseudospectra, semigroup behavior, or other nonnormal data. Those quantities require a fresh matched-control audit; this result does not declare them source-blind.

More importantly, several operator constructions remain genuinely outside the theorem. A self-adjoint-looking repair such as

\[
N+Q+Q^*
\]

contains a backward/lowering channel and is no longer triangular. Same-grade arithmetic blocks, two-sided interactions, source-dependent domains, or an unbounded signature perturbation also escape (1). PC-360's non-scalar grade coupling can escape as well if it changes the diagonal grade operator or destroys strict raising rather than merely changing the ambient Hilbert norm.

These are substantive boundaries, not invitations to add arbitrary wrappers. Any surviving construction still has to be forced by the roots-of-unity geometry and must pass the existing matched non-arithmetic control tests before a spectral coincidence can count as RH evidence.

## Prior-art and novelty audit

The abstract operator theory is classical. Bounded perturbations of closed compact-resolvent operators, Riesz projections under norm-resolvent-continuous perturbations, and the spectral rigidity of triangular operator matrices are standard. As a nearby explicit reference, John Sylvester, *Discreteness of Transmission Eigenvalues via Upper Triangular Compact Operators*, SIAM Journal on Mathematical Analysis **44** (2012), 341--354, DOI `10.1137/110836420`, uses upper-triangular compact-resolvent structure to obtain discreteness and finite-dimensional generalized eigenspaces. The broader triangular-operator-matrix literature likewise treats spectral information inherited from diagonal blocks.

No novelty is claimed for the general functional-analysis ingredients. The line-local contribution is the exact application to the Prime-Circle all-depth signature frontier: PC-359/PC-360 left unbounded/closed spectralizations and arbitrary bounded infinite mixed-degree raising multipliers unresolved, while PC-351 treated finite-dimensional triangular developments. Equations (2)--(10) show that the most canonical compact-resolvent repair, and in fact every proper scalar grade Hamiltonian plus a bounded strictly raising signature term, has eigenvalues fixed entirely by the chosen grade energies. That makes the construction a classical triangular spectral wrapper rather than a new zeta mechanism.

The proof is self-contained apart from standard compact-resolvent/Riesz-projection facts, so this finding does not introduce a new load-bearing `SOURCES.md` dependency.

## Falsification / disproof audit

- **Finite-grade control:** truncating at grade `M` makes `H_0+Q` block triangular with the same diagonal blocks `epsilon_m I`; (2) reduces to ordinary finite-dimensional triangularity.
- **Single-step shift control:** on `ell^2(N_0)`, `N+alpha S` with bounded unilateral raising shift `S` has exactly the integer spectrum by the theorem, even though its eigenvectors and resolvent differ from those of `N`.
- **Infinite mixed-degree control:** no decomposition `Q=sum_k Q_k` is used. The theorem needs only boundedness of the complete `Q` and the projection relation (1), so it covers bounded positive-degree mixtures outside PC-360's finite-polynomial argument.
- **Multiplicity control:** repeated grade energies are allowed. The Riesz rank at a repeated value is the sum of the dimensions of all grades carrying that value; raising couplings may create Jordan chains but cannot change that total algebraic multiplicity.
- **Domain control:** boundedness of `Q` is load-bearing. If the signature term is unbounded, `D(H_0)` need not be its natural domain and the compact-resolvent homotopy can fail.
- **Directionality control:** strict raising is load-bearing. Adding `Q^*`, a same-grade block, or any genuine lowering channel invalidates the least-grade argument and can move eigenvalues.
- **Control-class check:** no source/control similarity is assumed. Source and matched control are individually pinned to the same grade spectrum whenever each satisfies the theorem, so even an unbounded reciprocal parity does not rescue this ordinary-spectrum route.
- **RH-specific check:** neither the critical line, the gamma factor, nor Riemann zeros enter the grade energies. Choosing them into `epsilon_m` by hand would be an arbitrary spectral wrapper and is excluded by the research mandate.

## Boundary assessment

This is a decisive negative for the natural route

`Prime-Circle all-depth signature -> bounded one-sided raising multiplier -> canonical unbounded grade Hamiltonian -> discrete eigenvalue spectrum -> RH mechanism`.

The route fails for a structural reason: compact resolvent makes all finite spectral points eigenvalues, and the first occupied grade fixes every eigenvalue before the arithmetic off-diagonal data can act. The remaining operator frontier must therefore break at least one load-bearing hypothesis in a geometry-forced way: boundedness of the signature perturbation, scalar/proper grade diagonalization, strict one-sided raising, or a common source-independent domain. In particular, backward/two-sided or same-grade couplings are the next genuinely distinct spectral class; merely making the completion infinite or the reciprocal parity unbounded is not enough.

## Artifact status

Single durable finding. No clue disposition or `SOURCES.md` update is required.