# RE-174 — Unbounded Euler-temperature samples restore infinite prime-source rigidity

**Status:** `CLASSICAL-DIRICHLET-UNIQUENESS + EXACT-DERIVED + PRIME-SUPPORT-INFINITE-RIGIDITY + EULER-PRODUCT-FINGERPRINT + RE-173-BOUNDARY + STABILITY-WARNING + PRIOR-ART-IDENTIFIED`.

**Parent findings:** RE-169, RE-172, RE-173.

`RE-173` shows that an infinite ordinary-prime control with multiplicities in `{0,1,2}` can preserve the ordinary Mertens normalization exactly, remain far inside every fixed Korobov--Vinogradov Chebyshev envelope, and still create an order-one transient post-selector Robin excursion. Thus one exact scalar Euler-factor charge at the Mertens boundary does not recover multiplicity-one occupancy.

There is, however, an exact rigidity boundary immediately to its right. Let `Q` be any ordinary-prime-supported source with multiplicities

\[
m_p\in\{0,1,2\},
\qquad
c_p:=m_p-1\in\{-1,0,1\}.
\tag{1}
\]

For real `sigma>1`, define the absolutely convergent Euler product

\[
Z_Q(\sigma)
:=\prod_p(1-p^{-\sigma})^{-m_p}
\tag{2}
\]

and its logarithmic discrepancy from the ordinary source

\[
D_Q(\sigma)
:=\log Z_Q(\sigma)-\log\zeta(\sigma)
=\sum_p c_p\log\frac1{1-p^{-\sigma}}.
\tag{3}
\]

Then:

1. if `D_Q(sigma_j)=0` on any unbounded sequence `sigma_j->infinity`, necessarily `c_p=0` for every prime `p`;
2. more sharply, if `P` is the smallest modified prime, then
   \[
   \boxed{
   D_Q(\sigma)
   =c_P P^{-\sigma}(1+o(1))
   \qquad(\sigma\to\infty);
   }
   \tag{4}
   \]
3. consequently the germ of `D_Q` at `+infinity` recovers the first multiplicity defect, and after subtracting its Euler factor the process can be iterated through the entire modified prime set.

So the noncompact null direction of `RE-173` is a **boundary phenomenon at the Mertens temperature**. It cannot preserve an unbounded family of exact Euler-product samples in `Re s>1`.

The cost is equally important. Once the first-defect regime in (4) is reached, the signal detecting a defect at prime `P` is only of size `P^{-sigma}`. Thus exact high-temperature Euler data are rigid but exponentially ill-conditioned as a selector-scale observable. This identifies a mathematically complete source fingerprint, not yet a robust mechanism for Robin.

## 1. The Euler discrepancy is an ordinary Dirichlet series

For `sigma>1`, absolute convergence permits

\[
\log\frac1{1-p^{-\sigma}}
=\sum_{k\ge1}\frac{p^{-k\sigma}}{k}.
\tag{5}
\]

Hence

\[
D_Q(\sigma)
=\sum_p\sum_{k\ge1}
\frac{c_p}{k}\,p^{-k\sigma}.
\tag{6}
\]

Because a positive integer cannot be a positive power of two distinct primes, the prime powers in (6) do not collide across different primes. Therefore (6) is the ordinary Dirichlet series

\[
\boxed{
D_Q(\sigma)=\sum_{n\ge2}\frac{a_Q(n)}{n^\sigma},
}
\tag{7}
\]

with

\[
a_Q(n)=
\begin{cases}
 c_p/k,&n=p^k,\\
 0,&\text{otherwise}.
\end{cases}
\tag{8}
\]

The coefficients satisfy `|a_Q(n)|<=1`, so (7) converges absolutely throughout `sigma>1`.

This already places the proposed source invariant inside the classical uniqueness theory of Dirichlet series rather than creating a new Robin-specific analytic theorem.

## 2. Sparse samples tending to infinity determine all multiplicities

Suppose

\[
D_Q(\sigma_j)=0,
\qquad
\sigma_j\to\infty.
\tag{9}
\]

The classical uniqueness theorem for absolutely convergent Dirichlet series states that equality on an infinite sequence whose real parts tend to `+infinity` determines every Dirichlet coefficient. Applying it to (7) and the zero series yields

\[
a_Q(n)=0
\qquad\text{for every }n.
\tag{10}
\]

In particular, at `n=p`,

\[
a_Q(p)=c_p=0
\qquad\text{for every prime }p.
\tag{11}
\]

Thus

\[
\boxed{
Z_Q(\sigma_j)=\zeta(\sigma_j)
\text{ for an unbounded sequence }\sigma_j
\Longrightarrow
m_p=1\text{ for every }p.
}
\tag{12}
\]

This remains true despite infinite modified support. The distinction from `RE-172` is structural: `RE-172` used a **largest** modified prime and its private valuation, so it stopped at infinite support. Here the limit `sigma->infinity` exposes the **smallest** modified prime, which always exists for any nonempty subset of the ordinary primes.

## 3. Direct first-defect asymptotics

The same conclusion has a line-specific proof that makes the conditioning visible. Assume the source is nontrivial and let

\[
P:=\min\{p:c_p\ne0\}.
\tag{13}
\]

Write

\[
L_\sigma(p):=\log\frac1{1-p^{-\sigma}}.
\tag{14}
\]

For fixed `P`,

\[
L_\sigma(P)
=P^{-\sigma}+O(P^{-2\sigma}).
\tag{15}
\]

For the later primes, using `|c_p|<=1` and `sigma>=2`,

\[
\begin{aligned}
\sum_{p>P}|c_p|L_\sigma(p)
&\le \frac1{1-2^{-\sigma}}
   \sum_{n>P}n^{-\sigma}\\
&\le \frac43\left(
(P+1)^{-\sigma}
+\frac{(P+1)^{1-\sigma}}{\sigma-1}
\right).
\end{aligned}
\tag{16}
\]

After division by `P^{-sigma}`, the right side tends to zero because

\[
\left(\frac{P}{P+1}\right)^\sigma
\left(1+\frac{P+1}{\sigma-1}\right)
\longrightarrow0.
\tag{17}
\]

Combining (15)--(17) proves (4). In particular, for every nontrivial `Q` there is `sigma_0(Q)` such that

\[
\operatorname{sgn}D_Q(\sigma)=\operatorname{sgn}c_P
\qquad(\sigma\ge\sigma_0(Q)).
\tag{18}
\]

So a nontrivial bounded-multiplicity prime control has no zeros arbitrarily far to the right.

The first defect is itself encoded by the asymptotic decay:

\[
\boxed{
\log P
=
\lim_{\sigma\to\infty}
-\frac1\sigma\log|D_Q(\sigma)|,
}
\tag{19}
\]

and then

\[
\boxed{
c_P
=
\lim_{\sigma\to\infty}P^\sigma D_Q(\sigma).
}
\tag{20}
\]

Subtracting `c_P L_sigma(P)` from `D_Q` exposes the next modified prime and repeats the procedure. Thus the full high-temperature germ is an exact multiplicity fingerprint.

## 4. What this says about the RE-173 control

In `RE-173`, the source `Q_p` first differs from the ordinary source by deleting primes in `[2p,3p]`. Let `P_p` be the smallest deleted prime. Then

\[
c_{P_p}=-1,
\qquad
2p\le P_p\le3p.
\tag{21}
\]

Although that construction achieves

\[
\Gamma(Q_p)=\gamma
\tag{22}
\]

exactly by an infinite compensating tail, (4) gives, for each fixed `p`,

\[
\boxed{
D_{Q_p}(\sigma)
=-P_p^{-\sigma}(1+o(1))
\qquad(\sigma\to\infty).
}
\tag{23}
\]

The delayed duplications near `[16p,17p]` and at geometrically increasing later primes become asymptotically invisible compared with the first deletion. Hence the exact Mertens cancellation in `RE-173` cannot be promoted to equality of the full Euler-temperature profile.

This is a genuine sharpening of the source-fidelity map, but not a closure of Robin. Equation (23) also shows why. At temperature `sigma`, the source signal of a selector-scale defect is only

\[
\asymp P_p^{-\sigma}.
\tag{24}
\]

Any approximate version of (12) that tries to use increasingly large `sigma` must therefore know the Euler discrepancy on the exponentially small scale `P_p^{-sigma}` once the first defect dominates. A fixed KV estimate, exact Mertens normalization, or another aggregate prime-count envelope contains nothing close to this precision.

The high-temperature fingerprint is therefore **rigid but badly conditioned**. It recovers multiplicity-one occupancy by resolving the earliest changed Euler factor almost coefficient by coefficient, rather than by controlling the Robin-scale signed mass.

## 5. Adversarial checks and scope

**Infinite support is allowed.** No terminal modified prime is used. The theorem directly covers the noncompact support mechanism that defeated `RE-172`.

**Bounded multiplicities are load-bearing for the simple absolute-convergence statement.** The `{0,1,2}` class of `RE-173` is fully covered. More general multiplicity growth can be allowed whenever (7) is absolutely convergent in a right half-plane, but no broader claim is needed here.

**One or finitely many fixed temperatures are not covered.** The theorem needs an unbounded sequence of exact samples. It does not show that a nontrivial infinite control cannot satisfy `Z_Q(s_j)=zeta(s_j)` at a prescribed finite collection of `s_j>1` while also matching Mertens and KV. That finite-temperature interpolation question remains open.

**Approximate equality is not rigid at useful precision.** The coefficient-extraction mechanism becomes exponentially sensitive as `sigma` grows. This finding supplies no polynomially conditioned selector invariant and no unconditional Robin estimate.

**This does not assume or derive RH.** Everything occurs in the absolutely convergent half-plane `Re s>1` and is a source-identification statement.

**The result does not make multiplicity-one a usable hypothesis by itself.** Requiring every ordinary prime to occur exactly once already specifies the actual source. The point is narrower: an analytic family of Euler samples detects that occupancy exactly, while the single Mertens boundary charge does not.

## 6. Prior-art and representation audit

The analytic core is classical. Tom M. Apostol, *Introduction to Analytic Number Theory* (Springer, 1976), Chapter 11, Theorem 11.3, states the relevant uniqueness theorem in precisely the sparse form used above: two absolutely convergent Dirichlet series agreeing on an infinite sequence with real parts tending to `+infinity` have identical coefficients. Modern lecture treatments reproduce the same coefficient-extraction proof. The Euler product for `zeta(s)` in `Re s>1` and its absolute convergence are standard classical facts.

Accordingly, **no novelty is claimed for the uniqueness theorem or for recovering a first nonzero Dirichlet coefficient from the limit at `+infinity`**. The line-specific contribution is the representation audit around `RE-173`: the logarithm of a prime-multiplicity Euler-product perturbation has prime-power coefficients `c_p/k`, so the noncompact exact-Mertens null direction becomes completely visible to any unbounded set of high-temperature samples. The same calculation quantifies why this otherwise perfect fingerprint is not automatically useful for the Robin selector: its first-defect signal is `P^{-sigma}`.

A targeted prior-art search checked classical Dirichlet-series uniqueness, Euler products, and modern uniqueness literature. The present claim is best classified as a classical theorem specialized to the exact source-fidelity boundary exposed by `RE-173`, not as a new theorem about Dirichlet series. No new external theorem is load-bearing because Sections 1 and 3 contain a complete direct derivation of the specialization, so `SOURCES.md` remains unchanged.

Representation-wise, `RE-172` and `RE-174` are dual triangularizations of the same ordinary-prime lattice. Finite Mertens support is read from the **largest** changed prime by valuation; arbitrary bounded infinite support is read from the **smallest** changed prime by high-temperature decay. `RE-173` lives exactly between them: its infinite tail destroys the former triangularization while exact matching at only `sigma=1` never invokes the latter.

## 7. Research consequence

The live source-fidelity question should not be reframed as merely finding more exact scalar normalizations. There is already a complete classical answer at the other extreme: an unbounded family of Euler temperatures determines the multiplicities exactly. But that answer pays for rigidity by probing exponentially tiny coefficient-scale signals.

The useful missing resource is therefore more specific:

\[
\boxed{
\text{find a selector-conditioned invariant that is robust at Robin scale,}
\\
\text{yet cannot be preserved by the RE-173 delete/duplicate tail.}
}
\tag{25}
\]

A finite set of fixed Euler temperatures is a natural next falsification target because it lies strictly between one Mertens charge and the complete high-temperature fingerprint. If such finitely many moments can still be matched by a KV-faithful infinite prime control, then the search should move away from finite-dimensional Euler summaries toward genuinely local occupancy, selector-conditioned prime counts, or another source relation with quantitative conditioning.

**Provenance:** derived against default-branch snapshot `65c5a545f8c70f357491f8936a71fb1e74fad277`; stable finding prefix `RE`; no adversarial sidecar was open; local clues were inspected; no clue-state, `mind/**`, README, graph, or source-registry mutation required.