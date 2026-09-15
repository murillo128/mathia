# AF-367 — finite prime prefix plus square-root Beurling regularity does not determine zero geometry

**Status:** `LITERATURE+DERIVED`, `DECISIVE-NEGATIVE`, `ARITHMETIC-FIDELITY`, `MATCHED-CONTROL`, `FINITE-HORIZON`, `BEURLING-BOUNDARY`, `NO-NOVELTY-CLAIM`

## Claim

AF-366 showed that an arbitrary Dirichlet coefficient tail can be changed after every finite observation horizon while inserting a new pole, even when the ordinary coefficient amplitude of that tail tends to zero. Its main boundary was arithmetic: those pole-insertion tails were general Dirichlet sequences, not tails forced to arise from a positive generalized-prime system.

A classical construction of Wen-Bin Zhang closes a substantial part of that boundary. For every prescribed finite cutoff `X_0`, there are two Beurling generalized-prime systems `P_RH` and `P_DV` such that:

1. below `X_0`, the generalized primes of **both** systems are exactly the ordinary rational primes;
2. both generalized-integer counting functions satisfy the same strong regularity scale
   \[
   N_{P}(x)=x+O\!\left(x^{1/2}\exp\{c(\log x)^{2/3}\}\right)
   \tag{1}
   \]
   for a suitable constant `c`;
3. the first system realizes the Beurling analogue of the Riemann hypothesis;
4. the second realizes only the classical de la Vallée Poussin zero-free-region/error-term scale rather than RH.

Zhang's 2007 precursor makes the zero-geometry contrast explicit: the irregular member has infinitely many Beurling-zeta zeros on a curve of the form

\[
\sigma=1-\frac{1}{\log |t|}
\tag{2}
\]

(with no zeros to the right in that construction), while the RH member has its corresponding zero-free half-plane through `Re(s)>1/2`. The 2013 normalization result then forces an arbitrarily long initial generalized-prime segment to be exactly the rational-prime segment while retaining the contrasting global regimes.

Consequently, fix any finite `X_0` and consider the retained datum

\[
T_{X_0}(P)
:=
\Bigl(P\cap(1,X_0],\;[P\text{ satisfies the regularity class }(1)]\Bigr).
\tag{3}
\]

Let `D(P)` record the binary discriminator "the associated Beurling zeta satisfies RH". Zhang's pair gives

\[
T_{X_0}(P_{RH})=T_{X_0}(P_{DV}),
\qquad
D(P_{RH})\ne D(P_{DV}).
\tag{4}
\]

Therefore, by the fiberwise fidelity criterion of AF-001,

\[
\boxed{
D\text{ does not factor through any finite generalized-prime prefix plus the coarse source class }(1).
}
\tag{5}
\]

This remains true if the finite observation records the complete generalized-integer multiset up to `X_0`. Any generalized integer at most `X_0` uses only generalized-prime factors at most `X_0`; those factors are the ordinary rational primes in both normalized systems. Hence the two finite generalized-integer prefixes coincide with the ordinary integers as well.

The Arithmetic Fidelity consequence is sharper than AF-366's unrestricted-tail obstruction:

\[
\boxed{
\text{positive Euler-product structure}
+\text{ exact rational-prime prefix of arbitrary finite length}
+\text{ near-square-root global integer-counting regularity}
\not\Rightarrow
\text{ RH-level zero geometry}.
}
\tag{6}
\]

Thus any source-side condition intended to make a finite observation horizon pole/zero faithful must use information stricter than this Beurling package. In particular, merely requiring a genuine positive generalized-prime tail and a very regular generalized-integer count does not repair the finite-horizon loss.

## Derivation

### 1. Zhang's normalization gives matched finite-prefix controls inside the generalized-prime category

A Beurling prime system is an unbounded sequence

\[
1<p_1\le p_2\le\cdots
\]

whose free multiplicative semigroup, with multiplicities where appropriate, forms the generalized integers. The associated zeta function is represented in its initial convergence half-plane by the positive Euler product

\[
\zeta_P(s)=\prod_{p\in P}(1-p^{-s})^{-1}.
\tag{7}
\]

So this is a materially narrower source category than the arbitrary coefficient sequences used in AF-366.

Zhang's 2013 paper, *Normalization of Beurling generalized primes with Riemann Hypothesis*, states that two Beurling systems can be chosen so that, **up to any assigned large number**, the primes of both systems are exactly the rational primes not exceeding that number. The same paper states that both systems satisfy `(1)`, while the first realizes RH and the second realizes exactly the classical zero-free-region / de la Vallée Poussin error-term regime.

The cutoff is prescribed before the systems are constructed. Thus for every finite horizon `X_0`, not merely along one subsequence of horizons, there is a matched pair whose complete prime data below that horizon are identical.

This is the category-specific strengthening that AF-366 itself did not provide.

### 2. The generalized-integer prefix is also forced to agree

The prime-prefix statement automatically propagates to every generalized integer at most the same cutoff.

Suppose `n<=X_0` is a generalized integer in either system. Every generalized-prime factor of `n` is greater than one, so no factor can exceed `X_0`. All available factors at that scale are therefore ordinary rational primes. Their products are ordinary positive integers, and ordinary unique factorization fixes their multiplicity representation at this finite scale.

Conversely every ordinary integer `n<=X_0` factors into ordinary rational primes at most `n<=X_0`, all of which occur as generalized primes in both systems. Therefore

\[
N_{P_{RH}}\cap[1,X_0]
=
N_{P_{DV}}\cap[1,X_0]
=
\{1,2,\ldots,\lfloor X_0\rfloor\}
\tag{8}
\]

with the ordinary finite-scale multiplicities.

Hence replacing a finite prime-prefix observation by the complete finite multiplicative semigroup visible below the same horizon does not separate the controls.

### 3. A strong common asymptotic class still does not close the fiber

Equation `(1)` is much stronger than merely imposing the Beurling prime-number theorem or a linear generalized-integer density. Both controls have generalized-integer count within a sublinear error only slightly above square-root scale:

\[
N_P(x)-x
=O\!\left(x^{1/2+o(1)}\right).
\tag{9}
\]

Nevertheless their zeta zero geometry is qualitatively different. Zhang's earlier 2007 construction, *Beurling primes with RH and Beurling primes with large oscillation*, supplies the underlying contrast: one system satisfies RH, while another has infinitely many zeros as far right as the de la Vallée Poussin scale and corresponding large prime-counting oscillation. The 2013 normalization result preserves this contrast while forcing an arbitrary initial rational-prime segment and the normalization `N(x)~x`.

Therefore the regularity statement `(1)` is not a sufficient tail class for recovering RH status from a finite source prefix. It constrains the global density of generalized integers very strongly, but it leaves enough tail freedom to alter the analytic zero geometry decisively.

### 4. Fiberwise formulation

Let `B_{X_0}` be the class of Beurling systems whose generalized primes agree exactly with the rational primes through `X_0` and whose generalized-integer counting function belongs to the regularity class `(1)`. Let

\[
D_{RH}:B_{X_0}\to\{0,1\}
\]

be the RH discriminator.

The Zhang pair proves that `D_RH` is nonconstant on `B_{X_0}` for every finite `X_0`. Equivalently, if `T_{X_0}` forgets the tail while retaining the finite prime/integer prefix and only the stated asymptotic-class tag, then one fiber of `T_{X_0}` contains both an RH and a non-RH system.

This is exactly AF-001's no-decoder criterion:

\[
\exists P,Q:\ T_{X_0}(P)=T_{X_0}(Q),\ D_{RH}(P)\ne D_{RH}(Q)
\Longrightarrow
\nexists\,\widehat D\text{ with }D_{RH}=\widehat D\circ T_{X_0}.
\tag{10}
\]

No numerical conditioning issue is needed. The obstruction is exact non-identifiability at the declared information layer.

## Relation to AF-017 and AF-366

AF-017 and AF-367 witness different failures and should not be conflated.

AF-017 shows that compressing an **entire** generalized Euler-product function to its meromorphic zero/pole divisor can erase the generalized-prime norm multiset: Grosswald--Schnitzer controls change the prime norms while preserving the divisor. That is a destination-compression failure.

AF-366 instead shows that a **finite source horizon** cannot protect later Dirichlet poles against unrestricted coefficient completions. Its explicit tail insertions deliberately did not claim to belong to a generalized-prime category.

AF-367 upgrades the latter obstruction. The adversarial completions can remain inside a genuine positive Beurling generalized-prime framework, can agree with the rational primes for an arbitrarily long prescribed initial segment, and can share the strong global integer-counting class `(1)`, yet still have incompatible RH-level zero geometry.

So the surviving frontier after AF-366 becomes more precise:

\[
\text{finite exact arithmetic prefix}
+\text{ coarse global regularity}
\quad\text{is insufficient even under Beurling multiplicativity.}
\tag{11}
\]

A successful source gate must therefore exploit a genuinely stronger global property: for example an exact ordinary-integer lattice constraint, a sufficiently strong summatory/cancellation law, a rigid continuation/growth class, a global functional relation tied to ordinary arithmetic, or another nonlocal certificate that Zhang's matched controls cannot share.

Those possibilities are candidates, not consequences of the present result.

## Prior art and novelty assessment

No novelty is claimed for the existence of these Beurling systems.

The decisive primary source is:

- Wen-Bin Zhang (Chung Man Ping), **“Normalization of Beurling generalized primes with Riemann Hypothesis,”** *Annales Universitatis Scientiarum Budapestinensis de Rolando Eötvös Nominatae, Sectio Computatorica* **39** (2013), 459–469, DOI `10.71352/ac.39.459`. Its abstract states exactly the three facts used here: arbitrary prescribed agreement with the rational primes up to a finite level, the common generalized-integer estimate `(1)`, and the RH versus classical-zero-free-region split.

The underlying contrasting constructions are developed in:

- Wen-Bin Zhang, **“Beurling primes with RH and Beurling primes with large oscillation,”** *Mathematische Annalen* **337** (2007), 671–704, DOI `10.1007/s00208-006-0051-5`. This gives the explicit RH system and the large-oscillation system with infinitely many zeros on the classical `1-c/log|t|` scale.

Modern Beurling literature continues to use these examples as calibration for what generalized-prime regularity does and does not force; for example recent zero-density work stresses that strong Axiom-A-type integer counting alone does not force RH-level zero-free regions.

The only derived content here is the Arithmetic Fidelity interpretation: Zhang's normalization is an exact matched-control theorem for the finite-horizon fiber left open by AF-366. It identifies a concrete information package that is insufficient even after imposing positive generalized-prime structure and near-square-root generalized-integer regularity.

## Boundaries and failure modes

- This is a theorem about the **Beurling generalized-prime category**, not a counterexample for the ordinary rational primes. The controls cease to be the ordinary prime system after the prescribed finite cutoff.
- The two controls share the asymptotic **class** `(1)`, not the exact global function `N_P(x)`. A destination that retains the complete generalized-integer counting function, complete Euler product, or complete prime sequence has strictly more information and is not refuted by `(4)`.
- The estimate `(1)` is an integer-counting constraint. It is not the same as a pointwise bound on the difference of generalized von Mangoldt coefficients, nor does it assert the exact cancellation hypotheses used in classical RH-equivalent error criteria.
- The finite-prefix equality can be made arbitrarily long but remains finite. Nothing here says that two different Beurling systems can agree at every generalized prime.
- The 2013 theorem is used as literature evidence; this finding does not reproduce Zhang's probabilistic/analytic construction. Its exact role is to provide an already-established matched pair.
- The phrase "realizes RH" refers to the corresponding Beurling-zeta RH notion, not to proving the classical Riemann hypothesis for `zeta(s)`.
- The generalized-prime category permits global arithmetic behavior unavailable to the exact ordinary integers. Therefore the result identifies which retained properties are insufficient; it does not prove which extra ordinary-arithmetic property is necessary or sufficient.

## Decisive audit test

Any proposed finite-horizon route that claims its retained source data are enough to force RH-sensitive zero geometry should be tested against the Zhang pair.

If the route uses only:

1. all generalized-prime or generalized-integer data below some finite `X_0`;
2. positivity and multiplicative generation by generalized primes; and
3. the global regularity class `(1)` or a weaker consequence of it,

then the route cannot distinguish the RH and non-RH controls above and therefore cannot decode RH status in that category.

To escape this obstruction, the proposal must state a further retained property and prove that at least one member of Zhang's normalized pair violates it. Merely increasing the finite cutoff does not help, because the normalization theorem applies after every prescribed finite cutoff.