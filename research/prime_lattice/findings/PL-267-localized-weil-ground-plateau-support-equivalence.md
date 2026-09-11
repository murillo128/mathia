# PL-267 — Localized Weil ground-energy plateaus are exactly proper-support ground states

**Evidence:** `LITERATURE+DERIVED`

**Status:** `STRUCTURAL-REDUCTION + SHARP-BOUNDARY`

## Claim

Let `Q_W^a` be Suzuki's localized completed Weil form on `L^2(-a,a)` and let `A_a` be its associated lower-bounded self-adjoint operator. Write

\[
\lambda_a=\min \sigma(A_a)
=\inf_{0\ne u\in\mathfrak D(Q_W^a)}
\frac{Q_W^a(u)}{\|u\|_2^2}.
\]

For `0<a<b`, identify `L^2(-a,a)` with the subspace of `L^2(-b,b)` obtained by zero extension. Suzuki's construction uses exactly this zero-extension convention, and `Q_W^a` and `Q_W^b` are restrictions of the same global completed Weil form. Therefore

\[
\mathfrak D(Q_W^a)\subset \mathfrak D(Q_W^b),
\qquad
Q_W^b(u)=Q_W^a(u)
\]

for every zero-extended `u` in the smaller form domain.

The domain monotonicity of `PL-266` can then be sharpened to the exact equality criterion

\[
\boxed{
\lambda_a=\lambda_b
\iff
\ker(A_b-\lambda_b)
\text{ contains a nonzero vector supported in }[-a,a].
}
\]

In the forward direction, **every** ground vector of `A_a`, extended by zero, is a ground vector of `A_b`. In the reverse direction, any ground vector of `A_b` supported in the smaller interval is admissible for `Q_W^a` with the same Rayleigh quotient.

Hence a nontrivial plateau of the localized ground energy is not an abstract variational pathology: it is exactly a failure of support propagation for the ground eigenspace. In particular, strict domain monotonicity

\[
0<a<b\Longrightarrow \lambda_b<\lambda_a
\]

would follow from the much weaker statement that no ground vector of `A_b` can be supported in a proper centered subinterval of `(-b,b)`. A full unique-continuation theorem is stronger than necessary.

This sharpens the residual caveat in `PL-266`. It does **not** prove that zero plateaus are impossible, and it does not prove RH. It converts the plateau question into a precise operator-theoretic support problem for Suzuki's actual localized Weil operator.

## 1. Exact nesting of the localized form domains

Suzuki defines the global completed Weil quadratic form `Q_W` on `L^2(R)` and, for each `a>0`, the localized closed form by restriction to functions supported in `(-a,a)`. His convention explicitly identifies `L^2(-a,a)` with its zero extension to `L^2(R)`.

Consequently, if `0<a<b` and `u\in\mathfrak D(Q_W^a)`, then the same zero-extended function belongs to `L^2(-b,b)` and has finite global Weil form. Hence

\[
u\in\mathfrak D(Q_W^b),
\qquad
Q_W^b(u)=Q_W(u)=Q_W^a(u),
\qquad
\|u\|_{L^2(-b,b)}=\|u\|_{L^2(-a,a)}.
\]

Taking infima immediately gives the monotonicity already isolated in `PL-266`:

\[
\lambda_b\le \lambda_a.
\]

The present point is that equality carries much more information because Suzuki's localized operators have an actual lowest eigenvalue, not merely an unattained lower form bound.

## 2. Equality forces a zero-extended ground state

Assume `\lambda_a=\lambda_b`. Let `u_a` be a normalized ground eigenvector of `A_a`. Since the operator is associated with `Q_W^a`,

\[
Q_W^a(u_a)=\lambda_a.
\]

Extend `u_a` by zero from `(-a,a)` to `(-b,b)`. By the exact form nesting,

\[
Q_W^b(u_a)=Q_W^a(u_a)=\lambda_a=\lambda_b.
\]

Thus `u_a` attains the minimum of the Rayleigh quotient for the larger closed semibounded form. The standard Euler--Lagrange argument for closed quadratic forms now gives, for every `w\in\mathfrak D(Q_W^b)`,

\[
Q_W^b(u_a,w)=\lambda_b\langle u_a,w\rangle.
\]

By the representation theorem for the operator associated with a closed semibounded form, this means

\[
u_a\in\mathfrak D(A_b),
\qquad
A_bu_a=\lambda_bu_a.
\]

Therefore the larger-domain ground eigenspace contains a nonzero eigenvector whose support is contained in `[-a,a]`. The argument applies to every vector in the ground eigenspace of `A_a`, so equality of the endpoints embeds the entire smaller ground space into the larger one by zero extension.

## 3. A proper-support ground state forces equality

Conversely, suppose `u_b` is a nonzero ground eigenvector of `A_b` and

\[
\operatorname{supp}u_b\subset[-a,a]
\]

up to null sets. Since `u_b\in\mathfrak D(Q_W^b)` and `Q_W^b` is the restriction of the same global form, the support condition places `u_b` in `\mathfrak D(Q_W^a)` and preserves both its norm and form value. Hence

\[
\lambda_a
\le
\frac{Q_W^a(u_b)}{\|u_b\|_2^2}
=
\frac{Q_W^b(u_b)}{\|u_b\|_2^2}
=\lambda_b.
\]

Together with domain monotonicity `\lambda_b\le\lambda_a`, this gives `\lambda_a=\lambda_b`.

Because `a\mapsto\lambda_a` is nonincreasing, equality at two endpoints also implies constancy on the whole interval `[a,b]`. Thus the following statements are equivalent for `0<a<b`:

\[
\lambda_a=\lambda_b,
\]

\[
\lambda_c=\lambda_a\quad\text{for every }c\in[a,b],
\]

and

\[
\ker(A_b-\lambda_b)
\text{ contains a nonzero vector supported in }[-a,a].
\]

This equivalence is purely variational and does not use an Euler product, a zero expansion, or RH.

## 4. The remaining plateau problem is a support-unique-continuation problem

`PL-266` defines, under failure of RH,

\[
a_-:=\inf\{a>0:\lambda_a<0\}
\]

and proves that finite Galerkin first-negative thresholds converge to `a_-`. Its only caveat for identifying `a_-` with an earliest degeneracy radius is the possibility that `\lambda_a=0` on an interval before strict negativity begins.

The equivalence above makes that caveat concrete. A zero plateau `[a_0,a_-]` with `a_0<a_-` would force, for every `b` in its interior and in particular at the right endpoint, a zero-energy ground state of `A_b` supported in the strictly smaller interval `[-a_0,a_0]`. Conversely, any such proper-support zero ground state creates an equality interval by domain monotonicity.

Therefore a sufficient theorem for removing the plateau caveat is:

\[
\boxed{
A_bu=\lambda_bu,\ u\ne0
\quad\Longrightarrow\quad
\operatorname{supp}u\text{ is not contained in }[-a,a]
\text{ for any }a<b.
}
\]

A conventional weak unique-continuation property for `A_b` would imply this, because a properly supported ground vector vanishes on the nonempty boundary collar `(-b,-a)\cup(a,b)`. But full UCP is not required; one needs only this support statement for the bottom eigenspace.

## 5. Why standard logarithmic-Laplacian UCP cannot simply be imported

The localized Weil operator has a logarithmic-Laplacian-like singular component, so it is tempting to invoke existing unique-continuation results for the logarithmic Laplacian. That transfer is not automatic.

Suzuki's distributional kernel contains, in addition to the `Pf(1/|t|)` singularity and scalar delta term, a smooth completed contribution and the finite prime-power translation atoms that are active at the chosen aperture. Thus the equation for `A_b` is not merely

\[
L_\Delta u+q(x)u=\lambda u
\]

with a bounded local multiplication potential. On a boundary collar where a candidate eigenfunction vanishes, the nonlocal smooth-convolution and translated-copy terms need not vanish there. A UCP theorem for the bare logarithmic Laplacian or a logarithmic Schrödinger operator with local potential therefore does not by itself exclude a localized Weil ground state with proper support.

A successful plateau-exclusion theorem must handle the **actual completed nonlocal kernel**, including the prime-power translation terms, or exploit a more structural property of Suzuki's form. This is the precise remaining burden; merely citing generic nonlocal UCP is insufficient.

## 6. Prior-art and novelty audit

The load-bearing literature input is already registered as source 56 in `research/prime_lattice/SOURCES.md`:

- Masatoshi Suzuki, **“Weil's quadratic form via the screw function,”** arXiv:2606.09096v2. Suzuki supplies the global/localized form construction, zero-extension convention, self-adjoint operator with discrete lower-bounded spectrum, existence of the ground state, and the Rayleigh characterization used above.

Suzuki proves continuity of `a\mapsto\lambda_a` and the small-aperture/negativity criteria used in `PL-266`, but the inspected paper does not state the endpoint-equality/proper-support equivalence above as a theorem. A targeted literature search for strict domain monotonicity, localized-Weil unique continuation, and proper-support eigenfunctions found nearby unique-continuation theory for logarithmic Laplacians but no theorem directly covering Suzuki's completed operator. Search absence is not evidence of originality, and no priority claim is made for the elementary variational lemma.

The durable line-specific delta is instead the exact reduction of the remaining `PL-266` ambiguity: **zero-plateau exclusion is neither a moving-threshold approximation problem nor a generic continuity problem; it is a support-propagation problem for the localized Weil ground eigenspace.**

## 7. Adversarial boundaries and falsification

The reduction depends on four exact ingredients: the localized forms must be restrictions of one global form; smaller intervals must embed by zero extension; the bottom of each localized spectrum must be attained; and the operator/form representation theorem must identify a form minimizer with a ground eigenvector. These are the properties supplied by Suzuki's construction.

The statement would fail for a localization scheme in which enlarging the interval changes the quadratic form itself, introduces boundary counterterms, or lacks an attained ground state. It should therefore not be transferred automatically to arbitrary finite CvS matrices or to another truncation family merely because their lowest eigenvalues are monotone.

The result also does not establish strict monotonicity. The completed Weil kernel is nonlocal, and no proof is given that its ground states possess the required support-unique-continuation property. A plateau remains logically possible until that theorem is proved.

Finally, even strict decrease of `\lambda_a` would not prove its sign. Under RH the Weil form is nonnegative at every aperture; under RH failure strict decrease would organize how the lowest energy crosses zero. The difficult RH-facing task remains source-side control of the unshifted completed Weil form, as emphasized by `PL-264`--`PL-266`.

## Consequence for the research line

The localized-Weil branch now has a cleaner separation of gates. Finite negative detectability is already stable by `PL-266`; the ambiguity between earliest degeneracy and onset of strict negativity is equivalent to a ground-state support question; and the global RH burden is still the sign of the unshifted completed form.

Accordingly, a useful successor on the plateau issue should try to prove or disprove the no-proper-support property for Suzuki's ground eigenspaces using the completed nonlocal kernel. A successor that only proves more continuity or stronger fixed-radius Galerkin convergence does not address this remaining obstruction. The broader source-side program should still prioritize nonlocal coupling among prime events and the archimedean/pole completion rather than single-edge spectral geometry.