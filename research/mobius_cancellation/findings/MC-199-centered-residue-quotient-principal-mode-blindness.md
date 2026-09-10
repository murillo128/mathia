# MC-199 — Centered residue data factor through a quotient that does not determine the rough principal mode

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `DECISIVE-NEGATIVE`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-196` shows that a nonlinear statistic built from centered primorial residue aggregates can lie in the trivial representation and can enter an exact source identity involving the rough Möbius principal sum. `MC-198` then repairs the fixed-degree centered-polynomial analysis: at primorial rank `phi>2`, a centered polynomial retains a nonzero same-class top interaction, together with genuine cross-residue interactions that may cancel arithmetically.

There is a distinct information boundary that must remain separate from those interaction calculations. **A statistic built only from centered residue aggregates may be invariant under the residue-class symmetry while still being exactly blind to the linear principal mode.** Landing in a trivial representation after nonlinear mixing is not the same as recovering the principal Fourier coefficient that was removed by centering.

Let `G` be any finite set of `phi>=1` residue classes and let

\[
A=(A_a)_{a\in G},\qquad B=(B_a)_{a\in G}
\tag{1}
\]

be signed and support aggregates. Put

\[
S=\sum_a A_a,\qquad Q=\sum_a B_a,
\tag{2}
\]

and

\[
u=A-\frac S\phi\mathbf 1,
\qquad
v=B-\frac Q\phi\mathbf 1.
\tag{3}
\]

The centering map

\[
\mathcal C(A,B)=(u,v)
\tag{4}
\]

has the exact gauge symmetry

\[
\boxed{
\mathcal C(A+c\mathbf 1,B+d\mathbf 1)=\mathcal C(A,B)
}
\tag{5}
\]

for all scalars `c,d`. Hence every observable of the form

\[
F(A,B)=\Phi(\mathcal C(A,B))
\tag{6}
\]

—polynomial or not, equivariant before scalarization or not—factors through the quotient by the two constant directions. In particular the signed principal coordinate `S` does not factor through `\mathcal C`, because

\[
S(A+c\mathbf 1)=S(A)+c\phi.
\tag{7}
\]

This is not only an ambient-vector-space obstruction. It survives a **matched ternary-source control with identical class capacities and identical support aggregates**. Suppose every class contains at least two source sites. In each class choose two distinguished sites and set all other sites to zero. Define two ternary sources by

\[
(x^{(0)}_{a,1},x^{(0)}_{a,2})=(+1,-1),
\qquad
(x^{(+)}_{a,1},x^{(+)}_{a,2})=(+1,+1).
\tag{8}
\]

Both sources have exactly the same support in every class:

\[
B_a^{(0)}=B_a^{(+)}=2.
\tag{9}
\]

But their signed aggregates are

\[
A_a^{(0)}=0,
\qquad
A_a^{(+)}=2.
\tag{10}
\]

Therefore

\[
\boxed{
u^{(0)}=u^{(+)}=0,\qquad v^{(0)}=v^{(+)}=0,\qquad B^{(0)}=B^{(+)} }
\tag{11}
\]

while

\[
\boxed{S^{(0)}=0,\qquad S^{(+)}=2\phi.}
\tag{12}
\]

Consequently **even the complete centered signed profile together with the complete uncentered class-by-class support profile does not universally determine the signed principal sum on ternary sources.** Any universal decoder or inequality that purports to recover `S` from only those data is impossible without an additional source restriction that excludes the matched pair `(8)`.

For the logarithmic primorial `q=\prod_{p\le c\log X}p` with `0<c<1/2`, every reduced residue class has many representatives below `X` for sufficiently large `X`, so the two-site control can be embedded on the same residue-cell geometry used by the rough Möbius decomposition. The control is intentionally not claimed to be multiplicative or to equal Möbius. Its role is sharper: it proves that **residue centering plus ternary support algebra alone cannot supply the missing zero-mode information.** Any successful arithmetic transfer must use a relation that is false for this matched control—multiplicativity, inter-site divisor structure, an uncentered correlation identity, a boundary condition, or another genuinely source-specific constraint.

## 1. The centering quotient is exact at every nonlinear degree

Write

\[
C=I-\frac1\phi\mathbf 1\mathbf 1^T.
\tag{13}
\]

Then `u=CA`, `v=CB`, `C\mathbf 1=0`, and

\[
\ker C=\operatorname{span}\{\mathbf 1\}.
\tag{14}
\]

Thus `(4)` is literally a quotient map in each coordinate. Equation `(5)` is independent of polynomial degree, Fourier representation, character multiplication, positivity, or a choice of norm. Applying a nonlinear function after the quotient cannot reconstruct which point on a constant-direction fiber was the original input.

This extends the architecture-level observation of `MC-190`, where a translation-invariant Hermitian quadratic energy with zero principal multiplier satisfies `Q(F+c\mathbf 1)=Q(F)`. The present statement no longer assumes linearity, Hermitian structure, quadratic degree, positivity, or unit-group equivariance of the post-processing: once the raw data have first been replaced by `CA`, **every** subsequent function of that centered data is constant on the same fibers.

The support coordinate does not repair the defect if it is held fixed. The control `(8)`--`(12)` has identical `B` itself, not merely identical centered support `v`. Therefore adding `B`, `Q`, class capacities, or any deterministic function of those support data to a centered-sign decoder still leaves the two sources indistinguishable.

## 2. Why a nonlinear trivial representation is not the lost linear principal coordinate

The distinction matters directly for `MC-196`--`MC-198`. If `u` is expanded in nonprincipal multiplicative characters, products such as

\[
\widehat u(\chi_1)\widehat u(\chi_2)\widehat u(\chi_3),
\qquad \chi_1\chi_2\chi_3=1,
\tag{15}
\]

can indeed transform according to the trivial representation. This is a genuine nonlinear representation-theoretic coupling: nontrivial sectors can tensor together to produce an invariant scalar.

But the invariant scalar in `(15)` remains a function of `u=CA`. Equation `(5)` therefore makes it insensitive to `A\mapsto A+c\mathbf 1`. By contrast the linear principal Fourier coefficient is proportional to `S` and changes under the same transformation. The two notions of “principal” must not be conflated:

- **trivial output representation:** a nonlinear scalar is invariant under the class action;
- **principal linear input mode:** the constant Fourier coordinate of the original residue vector.

The first can be generated from transverse modes. The second cannot be reconstructed from centered data without an extra source relation.

This explains why the exact identity in `MC-196` necessarily leaves the centered statistic and brings back uncentered source information. Its relation

\[
D_3-J_3
=
S\left(2+\frac{3P_2}{\phi}-2\frac{S^2}{\phi^2}\right)
\tag{16}
\]

uses the same-residue pair/triple terms `P_2,D_3`; these are not functions of the centered aggregate profile alone. They are precisely additional inter-site source information capable, in principle, of breaking the quotient ambiguity.

## 3. Consequence for the centered-polynomial frontier

`MC-198` correctly leaves open cancellation between its same-class and cross-residue top-interaction sectors. The present quotient theorem narrows what such a cancellation could accomplish.

A bound or exact cancellation for

\[
F_P=\sum_a P(u_a,v_a)
\tag{17}
\]

**by itself cannot be a decoder for `S`**, regardless of the degree of `P`, because `(17)` factors through `\mathcal C`. Even a complete determination of the entire centered profile `(u,v)` would not distinguish the matched ternary sources `(8)`.

Therefore the second analytic possibility identified in `MC-198`—coupled cancellation among same-class and cross-residue top sectors—becomes useful for Mertens cancellation only if it participates in an additional arithmetic identity or inequality that also contains information outside the centered quotient and whose conditioning is independently controlled. Purely improving the estimate for a centered invariant, however sophisticated its nonlinear sector mixing, does not close the principal-mode gap.

This does **not** invalidate `MC-196`. That finding already contains the required outside-the-quotient objects `D_3` and `P_2`; its bottleneck is estimating them on the growing primorial shift lattice without paying the fixed-power restriction loss. The present result instead prevents the line from trying to evade that source bill merely by replacing `J_3` with a cleverer centered polynomial or other centered-only nonlinear invariant.

## 4. Prior-art and novelty audit

The linear algebra behind `(5)` is elementary: centering is projection onto the codimension-one zero-sum subspace, and centered moments/statistics are classically translation-invariant because they discard location. `MC-190` already records the same quotient-by-constants phenomenon for translation-invariant quadratic energies and audits the finite-group Fourier language used there. A targeted external search over centered moments, translation invariance, projections, and quotient representations found only these standard underlying mechanisms; no novelty is claimed for centering or quotient factorization.

The durable Mathia contribution is the **line-specific composition result and matched control**: applying the quotient observation to the current primorial residue interface, preserving the full ternary support profile exactly, and separating nonlinear trivial-representation output from recovery of the deleted linear principal coordinate. This is a frontier restriction on the live `MC-196`--`MC-198` mechanism, not a claim of a new general theorem in invariant theory or statistics.

No zero-free region, estimate for `M(X)`, correlation bound, or RH consequence is derived here.

## 5. Boundaries and falsification tests

- The no-go applies to observables whose signed input enters only through the centered aggregate vector `u=CA`. It does not apply when an uncentered signed statistic, an inter-site correlation, divisor/factorization data, or another source-specific relation is retained independently.
- The matched controls are ternary and have identical support at every chosen site/class, but they are not multiplicative functions. They therefore rule out **source-free aggregate decoding**, not a theorem that exploits Möbius multiplicativity or another exact arithmetic restriction.
- The statement does not say that a centered statistic is useless. A centered observable can enter an exact identity together with additional data, as `J_3` does in `MC-196`; it can also diagnose transverse arithmetic structure independently of the Mertens target.
- “Trivial representation” and “principal Fourier coefficient” coincide for linear vectors but need not coincide after taking tensor products or nonlinear invariants. Any future argument using nonlinear character products must state explicitly which meaning is intended.
- The control requires at least two available source sites in each class. This holds eventually for the active `q=X^{c+o(1)}` with `c<1/2`; the claim is not intended as a finite-`X` statement for residue classes with fewer representatives.
- A counterexample to the core quotient claim would require two inputs with identical centered aggregates but different values of a function asserted to depend only on those centered aggregates, contradicting the factorization `(4)`--`(6)`. A counterexample to the stronger ternary matched-control statement would require `(8)`--`(12)` to fail, which is excluded by direct calculation.

## Consequence for the line

The fixed-degree interaction hierarchy is now separated from a more basic identifiability issue. `MC-198` shows that centering does not algebraically remove the highest same-residue interaction; `MC-199` shows that **even perfect control of a centered nonlinear invariant does not by itself recover the deleted rough zero mode**.

The remaining nonlinear route must therefore pay for a genuine source bridge. It may exploit the pair/triple terms already exposed by `MC-196`, discover an arithmetic cancellation relation among complete residue-pattern sectors that also couples to an uncentered quantity, or leave the centered aggregate quotient altogether. Merely producing ever richer invariant scalars from transverse modes cannot solve the principal-mode problem.