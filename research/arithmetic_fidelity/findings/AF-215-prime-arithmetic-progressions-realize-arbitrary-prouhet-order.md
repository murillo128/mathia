# AF-215 — Prime arithmetic progressions realize arbitrary Prouhet order

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-CONTROL`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-214 left open a specific source-side escape: its arbitrary-order Prouhet cancellation used distinct integers with unit multiplicity, but those integers were not required to be rational primes. One might therefore hope that **actual primality itself** imposes a finite ceiling on the order of exact polynomial-moment cancellation available to a simple source.

It does not.

For every integer

\[
m\ge 1,
\tag{1}
\]

there exist two disjoint finite sets of distinct rational primes

\[
P_m^+,\;P_m^-
\tag{2}
\]

with

\[
|P_m^+|=|P_m^-|=2^{m-1}
\tag{3}
\]

such that

\[
\boxed{
\sum_{p\in P_m^+}p^k
=
\sum_{p\in P_m^-}p^k,
\qquad k=0,1,\ldots,m-1.
}
\tag{4}
\]

Moreover the union `P_m^+\sqcup P_m^-` can be chosen to be a single arithmetic progression of rational primes.

Consequently,

\[
\boxed{
\text{primality + distinct support + unit multiplicity do not bound Prouhet cancellation order.}
}
\tag{5}
\]

Any Arithmetic Fidelity rescue that relies only on the source atoms being distinct rational primes cannot exclude arbitrary finite-order polynomial moment annihilation. A successful prime-specific restriction must use additional global or relational structure that is not inherited by arbitrary finite prime subsets.

## Derivation

### 1. Start from the Prouhet–Thue–Morse signs

For fixed `m`, let

\[
\varepsilon_j:=(-1)^{s_2(j)},
\qquad 0\le j<2^m,
\tag{6}
\]

where `s_2(j)` is the binary digit sum. As proved and sourced in AF-214, the classical Prouhet identity gives

\[
\sum_{j=0}^{2^m-1}\varepsilon_j j^r=0,
\qquad r=0,1,\ldots,m-1.
\tag{7}
\]

The case `r=0` says that exactly `2^{m-1}` signs are positive and exactly `2^{m-1}` are negative.

### 2. Put the same sign pattern on a prime arithmetic progression

Green and Tao proved that the rational primes contain arithmetic progressions of every finite length. Choose one of length `2^m`:

\[
p_j=a+d j,
\qquad 0\le j<2^m,
\qquad d>0,
\tag{8}
\]

with every `p_j` prime. Define

\[
P_m^+:=\{p_j:\varepsilon_j=+1\},
\qquad
P_m^-:=\{p_j:\varepsilon_j=-1\}.
\tag{9}
\]

Because `d>0`, all `p_j` are distinct, so `(9)` consists of two disjoint simple prime sets with unit multiplicity.

### 3. Prouhet cancellation is affine-invariant

For every integer `k<m`, the binomial theorem gives

\[
\begin{aligned}
\sum_{j=0}^{2^m-1}\varepsilon_j p_j^k
&=
\sum_j\varepsilon_j(a+d j)^k\\
&=
\sum_{r=0}^k {k\choose r}a^{k-r}d^r
\sum_j\varepsilon_j j^r.
\end{aligned}
\tag{10}
\]

Every inner signed moment in `(10)` vanishes by `(7)`, since `r\le k<m`. Therefore

\[
\sum_j\varepsilon_j p_j^k=0,
\qquad 0\le k<m,
\tag{11}
\]

which is exactly `(4)` after splitting the positive and negative signs.

No distributional estimate for primes is needed beyond existence of arbitrarily long prime arithmetic progressions. The argument is an exact composition of Green–Tao with the affine invariance of the Prouhet partition.

## Arithmetic Fidelity consequence

AF-214 showed that integrality, distinctness, and unit generator multiplicity do not prevent arbitrary-order Prouhet cancellation. The remaining obvious local support condition was actual rational primality. Equation `(4)` closes that escape at the same polynomial-moment information layer: **finite sets of genuine primes themselves realize arbitrary cancellation order**.

This rules out any proposed recovery theorem whose decisive source prior is merely hereditary membership in the rational primes — for example, a theorem intended to become coercive once every atom is known to be a distinct prime with coefficient `\pm1`. For every fixed order requested by such a theorem, a finite prime-supported counterconfiguration exists.

The result also sharpens the interpretation of “arithmetic provenance.” Primality is a pointwise property of each support atom, but the compression obstruction is relational. Preventing the Prouhet mechanism therefore requires constraints on how prime atoms occur **together**: canonical/global weighting, natural ordering or density, multiplicative relations, quantitative dispersion/correlation conditions, bounded source complexity, or another non-hereditary structure strong enough to exclude the prime arithmetic-progression subconfigurations used here.

## Prior art and novelty assessment

The two ingredients are established mathematics and no novelty is claimed for either one.

- Ben Green and Terence Tao, **“The primes contain arbitrarily long arithmetic progressions,”** *Annals of Mathematics* 167(2) (2008), 481–547, DOI `10.4007/annals.2008.167.481`. Their theorem supplies `(8)` for every finite length. Primary source: `https://annals.math.princeton.edu/2008/167-2/p03`.
- The Prouhet–Thue–Morse equal-power partition used in `(7)` is classical and was audited in AF-214, including Prouhet (1851), Wright (1959), and modern Thue–Morse references.
- Ernie Croot, Junzhe Mao, and Chi Hoi Yip, **“The Prouhet--Tarry--Escott problem for subsets with small doubling in integral domains,”** arXiv:`2609.05061` (2026). This very recent adjacent work proves broad Prouhet–Tarry–Escott existence results inside finite sets with small additive doubling. It reinforces that additive structure is a natural source of Prouhet configurations, but the present prime corollary needs only the older Green–Tao theorem plus the classical affine Prouhet identity.

A targeted prior-art search found the ingredients and broader Prouhet–Tarry–Escott literature but did not locate a source needed for this exact Arithmetic Fidelity use. The recorded contribution should therefore be treated conservatively as a **literature-derived obstruction/corollary**, not as a novelty claim.

## Boundaries and failure modes

1. The theorem is existential over finite prime subsets. It does **not** say that the canonical full prime sequence, the von Mangoldt measure, or a natural density-weighted prime ensemble globally matches these moments.
2. Green–Tao alone gives no quantitative control here on the ratio `d/a` of the progression in `(8)`. Therefore AF-214's sharp local Euler-flatness estimate `Theta(N^{-\sigma-m})` cannot simply be transferred to these prime configurations. The present result closes the exact moment-cancellation gate, not the stronger localized Euler-conditioning gate.
3. The construction uses exponentially many primes, `2^{m-1}` per side. A source class with a genuine cardinality or complexity budget can still bound the available cancellation order.
4. A non-hereditary source prior may exclude these finite subconfigurations even though every atom is prime. In particular, a theorem tied to canonical global weights, consecutive-prime order, multiplicative structure, or prescribed density/correlation data is not refuted by `(4)` without an additional argument.
5. No statement about zeta zeros, the critical strip, or RH follows from this result.

## Consequence for the next research step

Do not pursue “actual primality” as a pointwise cure for the AF-214 cancellation mechanism. The next useful source-side gate must be relational or global: identify a property genuinely obeyed by the canonical rational-prime source but **not** by arbitrary finite prime subsets, then prove that this property quantitatively limits Prouhet/Hobby–Rice-type near-null directions or show that it too admits matched controls. The strongest next candidates are constraints tied to natural prime density/order, canonical von Mangoldt weighting, multiplicative compatibility, or a bounded-complexity condition that is mathematically forced rather than imposed ad hoc.