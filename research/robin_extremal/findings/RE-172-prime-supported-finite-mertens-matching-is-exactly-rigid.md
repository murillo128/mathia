# RE-172 — Prime-supported finite Mertens matching is exactly rigid

**Status:** `EXACT-DERIVED + PRIME-SUPPORT-RIGIDITY + FINITE-MERTENS-INJECTIVITY + GENERALIZED-CONTROL-BOUNDARY + SELECTOR-FIDELITY-NARROWING + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-057, RE-169, RE-171.

`RE-171` shows that exact equality of the asymptotic Mertens normalization does not determine a selected finite Robin prefix inside the generalized-prime control class. Its exact third-shell correction is deliberately continuous: ordinary primes are deleted, while replacement generalized labels move through real positions until the scalar equation `Gamma(Q_p)=gamma` is met.

That freedom disappears completely if the compensating source is required to remain on **ordinary prime labels with rational, hence in particular integer, multiplicities**.

Let `S` be a finite set of ordinary primes and let `c_p in Q` be signed multiplicity changes. Thus

\[
d\vartheta_Q-d\vartheta
=\sum_{p\in S} c_p\log p\,\delta_p.
\tag{1}
\]

For an actual prime multiset source the `c_p` are integers, with the obvious nonnegativity restriction on the final multiplicities; allowing rational `c_p` only strengthens the algebraic statement. Put

\[
H(p):=-\log(1-p^{-1})=\log\frac p{p-1}.
\tag{2}
\]

Because the perturbation is finite, the ordinary Mertens constant exists for `Q`, and the exact `RE-169` sum rule reduces to

\[
\boxed{
\Gamma(Q)-\gamma
=\sum_{p\in S} c_p H(p).
}
\tag{3}
\]

The finite family

\[
\left\{H(p):p\text{ prime}\right\}
\tag{4}
\]

is linearly independent over `Q`. Consequently

\[
\boxed{
\Gamma(Q)=\gamma
\quad\Longrightarrow\quad
c_p=0\ \text{for every }p\in S.
}
\tag{5}
\]

Thus **no nontrivial finite modification supported on ordinary prime labels can preserve the ordinary Mertens normalization exactly**, even if prime multiplicities are allowed to change. In particular, the finite three-shell exact compensation mechanism of `RE-171` cannot be made prime-supported merely by replacing its continuous generalized labels with a sufficiently fine selection of ordinary primes.

Equivalently, if a prime-supported integer-multiplicity control agrees with the ordinary source below a selector, changes a selected prefix nontrivially, and nevertheless has `Gamma(Q)=gamma`, then its compensating modifications cannot terminate in any finite later shell. They must continue through arbitrarily large primes. Exact Mertens matching therefore becomes a genuine **noncompactness constraint** once ordinary prime support is imposed.

This is a sharper source boundary than `RE-056`--`RE-057`. `RE-056` proved that the integer lattice by itself does not supply rigidity, while `RE-057` showed that exact ordinary divisor-sum first-layer behavior forces an integer label to be prime. The present result identifies what that primality gate buys at the global normalization level: the ordinary Euler factors carry a triangular private-prime valuation that makes the finite Mertens coordinate injective.

## 1. Exact Mertens matching becomes a finite injectivity theorem

For a finite perturbation (1), `RE-169` gives

\[
\Gamma(Q)-\gamma
=\int h(t)\,d(\vartheta_Q-\vartheta)(t),
\tag{6}
\]

where

\[
h(t)=\frac{-\log(1-t^{-1})}{\log t}.
\tag{7}
\]

Substituting the atoms in (1),

\[
\Gamma(Q)-\gamma
=\sum_{p\in S} c_p h(p)\log p
=\sum_{p\in S} c_p\log\frac p{p-1},
\tag{8}
\]

which proves (3).

Assume now that the right side of (8) vanishes. Clear denominators: choose `D>=1` with

\[
m_p:=Dc_p\in\mathbb Z
\qquad(p\in S).
\tag{9}
\]

Exponentiating `D` times (8) gives the exact rational identity

\[
\boxed{
\prod_{p\in S}\left(\frac p{p-1}\right)^{m_p}=1.
}
\tag{10}
\]

Suppose some `m_p` is nonzero and let `P` be the largest prime in its support. Take the ordinary `P`-adic valuation of (10). The factor indexed by `P` contributes exactly `m_P`. Every factor indexed by a smaller prime `q<P` contributes zero, because both

\[
q<P,
\qquad
q-1<P,
\tag{11}
\]

so neither its numerator nor its denominator is divisible by `P`. Hence

\[
v_P\!\left(
\prod_{p\in S}\left(\frac p{p-1}\right)^{m_p}
\right)=m_P.
\tag{12}
\]

The left side must be zero by (10), contradicting `m_P!=0`. Therefore no such `P` exists and every `m_p`, hence every `c_p`, vanishes. This proves (4)--(5).

The proof is triangular rather than transcendental. No lower bound for linear forms in logarithms is needed: the largest changed prime is a private prime divisor of its own numerator and cannot occur anywhere in the earlier Euler factors.

## 2. Why primality, not integrality, is load-bearing

The largest-prime argument fails immediately if arbitrary integer labels are allowed. Indeed the Mertens-type factors

\[
\frac n{n-1}
\tag{13}
\]

have exact telescoping relations. The smallest example is

\[
\boxed{
\left(\frac21\right)^{-1}
\left(\frac32\right)
\left(\frac43\right)=1,
}
\tag{14}
\]

or equivalently

\[
H(3)+H(4)-H(2)=0.
\tag{15}
\]

Thus an integer-label generalized source can possess a nontrivial finite exact-Mertens null direction. This is consistent with `RE-056`: the integer lattice alone does not recover ordinary-prime rigidity.

The obstruction in (12) appears only because every allowed label is itself prime. That is precisely the arithmetic distinction isolated locally by `RE-057`: if an integer label is required to reproduce the ordinary one-new-factor divisor-sum increment, it must be prime. The two findings therefore splice cleanly. `RE-057` makes primality unavoidable at the local `sigma` transition; `RE-172` shows that, once primality is imposed, exact finite Mertens compensation has no nontrivial kernel.

There is a parallel but even more elementary rigidity for exact Chebyshev-mass balance. If a finite prime-supported rational perturbation satisfies

\[
\sum_p c_p\log p=0,
\tag{16}
\]

then clearing denominators and unique factorization again force every `c_p=0`. Therefore the exact endpoint mass resets used inside the balanced generalized shells of `RE-167`--`RE-171` also rely on leaving the ordinary prime-support lattice. The Mertens statement is stronger for the present frontier because it needs no separate Chebyshev-balance hypothesis: exact `Gamma` alone already kills every finite prime-supported perturbation.

## 3. Consequence for the RE-171 control

The exact correction in `RE-171` deletes ordinary prime pairs `r_j<s_j` and inserts the continuously movable generalized labels

\[
r_j e^{-\tau},\qquad s_j e^{\tau}.
\tag{17}
\]

That construction has two useful properties: the product of each pair is fixed, giving exact Chebyshev-mass balance, while its Mertens contribution varies continuously through an interval of length `asymp 1/p`. With `O(log p)` pairs, the residual `O((log p)/p)` left by the first two shells can be tuned to zero by the intermediate value theorem.

Equation (5) shows that this continuous relocation is not cosmetic. If all inserted labels in the complete finite correction were required to be ordinary primes and all multiplicity changes rational, exact equality

\[
\Gamma(Q_p)=\gamma
\tag{18}
\]

would imply that the complete perturbation is identically zero. Hence there is no prime-supported analogue of the final compactly supported source in `RE-171` with the same exact normalization and a nontrivial earlier excursion.

The information boundary therefore changes from

\[
\text{exact Mertens scalar precision is insufficient}
\tag{19}
\]

inside the broad generalized-source class to the more precise statement

\[
\boxed{
\text{exact Mertens matching}
+
\text{ordinary-prime support}
+
\text{finite rational multiplicity change}
\Longrightarrow
\text{source rigidity}.
}
\tag{20}
\]

This does not prove selected-prefix rigidity for the actual primes. It says instead that any matched control which preserves the ordinary prime-support arithmetic must pay for a nontrivial prefix perturbation by becoming **genuinely noncompact**. A finite sequence of compensation shells can no longer close the source exactly.

## 4. Falsification checks and boundaries

**Real multiplicity weights are not covered.** If arbitrary real `c_p` are allowed, any two positive numbers `H(p)` admit a one-dimensional real linear relation after choosing the coefficients from the values themselves. Rationality/integrality of multiplicities is load-bearing.

**Arbitrary integer labels are not covered.** Equation (14) is an explicit finite counterexample. The theorem is about prime support, not about discretizing generalized labels onto `N`.

**Infinite prime-supported perturbations are not covered.** The proof selects a largest changed prime. For an infinite perturbation with a convergent Mertens difference there is no terminal valuation, and this argument gives no injectivity theorem. In particular, `RE-172` does not rule out an infinite prime-supported compensation whose weighted Mertens debt converges to zero.

**Approximate Mertens matching is not covered.** The proof is exact. It gives no useful lower bound for a nonzero finite linear form

\[
\sum_p c_pH(p)
\tag{21}
\]

in terms of its largest prime or support size. Therefore it does not supersede `RE-170`, whose final mismatch is merely `o((sqrt(p)log p)^(-1))`. A quantitative approximate analogue would require a genuinely new Diophantine estimate.

**This is not an ordinary-prime or CA counterexample exclusion.** Requiring an alternative source to use only the ordinary prime labels is a much stronger fidelity condition than PNT, KV, Mertens normalization, or generic integrality. The result identifies a source-specific rigidity mechanism and invalidates one finite matched-control escape under that mechanism; it does not yet show how the CA selector forces a usable bound on the actual ordinary-prime future.

## 5. Prior-art and representation audit

The identity `Gamma(Q)-gamma=sum c_p log(p/(p-1))` is the finite-source specialization of `RE-169`; the Euler factors themselves are classical Mertens-product objects. A targeted literature search checked standard Mertens-product references, including Jared Duker Lichtman's work on dissecting Mertens' prime product, together with searches for multiplicative or rational independence of the factors `p/(p-1)`. No located source stated the finite independence lemma in the present form or its consequence for matched Robin-source controls.

No independent number-theory novelty is claimed for the lemma. Its proof is a one-line largest-prime valuation argument from unique factorization and is best regarded as elementary arithmetic. The line-specific content is the splice with `RE-057`, `RE-169`, and `RE-171`: the scalar Mertens normalization that is nonrigid under continuous generalized labels becomes injective on finite ordinary-prime multiplicity perturbations, so the exact three-shell control cannot survive the primality gate.

Representation-wise, the phenomenon is not a generic property of positive kernels or finite atomic measures. It comes from a triangular arithmetic representation: the factor `p/(p-1)` contains the prime `p` in its numerator, while every earlier allowed factor is built entirely from integers below `p`. Passing to arbitrary generalized labels destroys that private valuation. This is precisely the kind of source information absent from the continuous controls.

No new external theorem is load-bearing, so `SOURCES.md` is unchanged.

## 6. Research consequence

The accepted selector-height coupling question remains open, but `RE-172` removes one ambiguity in how to interpret `RE-171`. The failure of exact scalar Mertens rigidity there is **not** source-faithful once the exact prime-support arithmetic is imposed. Any nontrivial exact-Mertens matched control on ordinary prime labels must have unbounded support, or else leave rational/integer multiplicity fidelity.

This gives a concrete next boundary. One may now ask whether the combination

\[
\text{prime-supported integer changes}
+
\text{KV-sized cumulative discrepancy}
+
\Gamma(Q)=\gamma
\tag{22}
\]

admits an **infinite** post-selector control carrying an order-one transient `RE-153` displacement, or whether the integer one-atom granularity plus the `RE-169` tail-capacity law forces that displacement to die before such an infinite compensation can be assembled. Either outcome would be materially sharper than adding another scalar normalization: it tests whether the actual prime Euler-factor lattice supplies the selector-sensitive spatial rigidity missing after `RE-171`.

**Provenance:** derived against default-branch snapshot `d16ece8d8bcfcf1afe48165791cb6ec3837e842a`; stable finding prefix `RE`; no adversarial sidecar was open; no clue-state, `mind/**`, README, graph, or source-registry mutation required.