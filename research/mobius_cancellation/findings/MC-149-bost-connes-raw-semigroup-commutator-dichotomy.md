# MC-149 — Raw Bost–Connes semigroup commutators are either universal or exclude Möbius

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Work in the canonical number-state representation used in `MC-148`,

\[
\mathcal H=\ell^2(\mathbb N),
\qquad
S_m\varepsilon_k=\varepsilon_{mk},
\qquad
D_a\varepsilon_k=a_k\varepsilon_k
\]

for `m>=2` and an arbitrary bounded arithmetic sequence `a=(a_k)`.
`MC-148` left commutators with the semigroup isometries as a genuinely transverse direction because

\[
[D_a,S_m]\varepsilon_k=(a_{mk}-a_k)\varepsilon_{mk}.
\tag{1}
\]

The raw commutator has an exact regularity dichotomy.

First, boundedness gives no selectivity at all:

\[
\boxed{
\|[D_a,S_m]\|
=\sup_{k\ge1}|a_{mk}-a_k|
\le 2\|a\|_\infty,
}
\tag{2}
\]

so even the uniform condition

\[
\sup_{m\ge2}\|[D_a,S_m]\|<\infty
\tag{3}
\]

is automatic for **every** bounded diagonal target.

Second, the first natural decay strengthening goes in the opposite direction. The operator `[D_a,S_m]` is compact exactly when

\[
a_{mk}-a_k\longrightarrow0
\qquad(k\to\infty).
\tag{4}
\]

For the actual Möbius diagonal `D_\mu`, this never happens for any `m>=2`. More sharply,

\[
\boxed{
\|[D_\mu,S_m]\|_{\rm ess}
=\|[D_\mu,S_m]\|
=\begin{cases}
2,& \mu(m)=-1,\\
1,& \mu(m)\in\{0,1\},
\end{cases}
\qquad m\ge2.
}
\tag{5}
\]

Thus every raw semigroup commutator with Möbius is noncompact. In fact for every finite Schatten exponent `0<q<infty`,

\[
[D_\mu,S_m]\notin\mathcal S_q.
\tag{6}
\]

Consequently the most immediate transverse-regularity escape from `MC-148` closes sharply:

- requiring only bounded raw commutators with the canonical semigroup isometries accepts every bounded lookup table;
- requiring compact, `c_0`, or finite-Schatten decay of those same raw commutators rejects the Möbius target itself.

A surviving transverse Bost–Connes route therefore needs additional structure between these extremes — for example a source-forced weighted/twisted commutator, a nontrivial averaged family, or another nonlocal construction — and must still prove a cheaper transfer to anchored Mertens excursion. Raw semigroup commutator regularity by itself cannot be that selector.

## 1. The commutator is an orthogonal weighted injection

From `(1)`, put

\[
w_{a,m}(k)=a_{mk}-a_k.
\tag{7}
\]

The vectors `\varepsilon_{mk}` are orthonormal as `k` varies, hence

\[
[D_a,S_m]^*[D_a,S_m]\,\varepsilon_k
=|w_{a,m}(k)|^2\varepsilon_k.
\tag{8}
\]

Therefore the singular-value data of the commutator are exactly the absolute weights `|w_{a,m}(k)|`, counted with multiplicity. In particular,

\[
\|[D_a,S_m]\|=\sup_k|w_{a,m}(k)|,
\tag{9}
\]

which proves `(2)`.

The same diagonalization gives the standard compactness test directly, without invoking any arithmetic theorem. Let `P_N` project onto `span\{\varepsilon_1,\ldots,\varepsilon_N\}`. Then

\[
[D_a,S_m]P_N
\]

has finite rank, while

\[
\|[D_a,S_m](I-P_N)\|
=\sup_{k>N}|w_{a,m}(k)|.
\tag{10}
\]

Hence `w_{a,m}(k)->0` implies compactness. Conversely, if the commutator is compact, the orthonormal sequence `\varepsilon_k` converges weakly to zero, so its images must converge to zero in norm; by `(1)` those norms are `|w_{a,m}(k)|`. This proves `(4)`.

The same argument identifies the essential norm:

\[
\boxed{
\|[D_a,S_m]\|_{\rm ess}
=\limsup_{k\to\infty}|a_{mk}-a_k|.
}
\tag{11}
\]

Finally, from `(8)`, for every finite `q>0`,

\[
[D_a,S_m]\in\mathcal S_q
\quad\Longleftrightarrow\quad
\sum_{k\ge1}|a_{mk}-a_k|^q<\infty.
\tag{12}
\]

So boundedness, compactness, essential norm, and Schatten summability all reduce to exact multiplicative finite-difference conditions on the represented arithmetic sequence.

## 2. Möbius has a persistent multiplicative finite difference for every dilation

Set

\[
w_m(k)=\mu(mk)-\mu(k).
\tag{13}
\]

There are three exhaustive cases.

### Case A: `mu(m)=-1`

Then `m` is squarefree with an odd number of prime factors. For every squarefree `k` coprime to `m`, multiplicativity gives

\[
\mu(mk)=\mu(m)\mu(k)=-\mu(k),
\]

hence

\[
|w_m(k)|=2.
\tag{14}
\]

There are infinitely many such `k` — for example primes not dividing `m`. Since `|w_m(k)|<=2` always, `(14)` gives

\[
\sup_k|w_m(k)|=\limsup_k|w_m(k)|=2.
\tag{15}
\]

### Case B: `mu(m)=0`

Then `m` contains a squared prime divisor, so `mk` is never squarefree and

\[
\mu(mk)=0
\qquad(k\ge1).
\]

Thus

\[
w_m(k)=-\mu(k).
\tag{16}
\]

The weights have absolute value `1` on every squarefree `k`, an infinite set. Therefore

\[
\sup_k|w_m(k)|=\limsup_k|w_m(k)|=1.
\tag{17}
\]

### Case C: `mu(m)=1`, with `m>=2`

Now `m` is squarefree with an even positive number of prime factors. If `k` is squarefree and coprime to `m`, then

\[
\mu(mk)=\mu(m)\mu(k)=\mu(k),
\]

so `w_m(k)=0`. If `k` is squarefree and shares at least one prime factor with `m`, then `mk` contains a square, hence

\[
\mu(mk)=0,
\qquad
|w_m(k)|=1.
\tag{18}
\]

If `k` is not squarefree, both terms in `(13)` vanish. Hence `|w_m(k)|<=1` for all `k`, while `(18)` occurs infinitely often: fix a prime `p|m` and take `k=pq` with primes `q` outside the finite prime support of `m`. Therefore

\[
\sup_k|w_m(k)|=\limsup_k|w_m(k)|=1.
\tag{19}
\]

Equations `(15)`, `(17)`, and `(19)` prove `(5)`.

They also prove `(6)` immediately. In every case there are infinitely many `k` with `|w_m(k)|>=1`, so the series in `(12)` diverges for every finite Schatten exponent.

The obstruction is therefore not a delicate density statement. It is forced by elementary squarefree/multiplicative structure on explicit infinite subsequences.

## 3. Why raw bounded commutators cannot select an arithmetic diagonal

Equation `(2)` is stronger than saying that Möbius happens to have bounded transverse variation. For every bounded sequence `a`,

\[
\sup_{m\ge2}\sup_{k\ge1}|a_{mk}-a_k|
\le2\|a\|_\infty.
\tag{20}
\]

Thus any admissibility rule whose only transverse requirement is boundedness of `[D_a,S_m]` for each canonical semigroup isometry — even with a uniform unweighted bound over all `m` — admits the entire target-complete diagonal `\ell^\infty(\mathbb N)` exposed by `MC-147`.

This is the semigroup analogue of the energy-flow blindness in `MC-148`, but for a different reason. The Hamiltonian commutator vanishes on every diagonal. The semigroup commutator does see multiplicative variation, yet its raw operator norm can never exceed the trivial oscillation diameter of a bounded sequence. Without an additional scale, summability, averaging, twisting, or relative normalization, boundedness alone contains no arithmetic discriminator.

At the next obvious endpoint, demanding compactness means imposing the multiplicative slow-variation condition `(4)` for each selected `m`. Möbius violates that condition maximally enough to have essential norm at least `1` for every nontrivial dilation. Finite Schatten conditions are still stronger and therefore also impossible for the target.

So the raw family has a precise **too-weak / wrong-target** split rather than a hidden intermediate regularity theorem.

## 4. Relation to `MC-147` and `MC-148`

`MC-147` showed that the strong/weak closure of the represented Bost–Connes coefficient algebra is all bounded diagonals. That made unrestricted weak closure target-complete and left source-natural regularity as a possible way to restore selectivity.

`MC-148` then proved that canonical Hamiltonian/time-flow regularity is diagonal-blind: every bounded diagonal is fixed, infinitely smooth, and entire for that flow. It explicitly identified semigroup commutators

\[
[D_a,S_m]\varepsilon_k=(a_{mk}-a_k)\varepsilon_{mk}
\]

as a genuinely transverse first-kill surface not covered by the energy no-go.

The present finding performs that first kill for the **raw** commutator family. It does not say that all transverse noncommutative geometry fails. It says that the two immediate topology classes do not provide the missing selector:

\[
\text{bounded raw semigroup differences}
\Rightarrow
\text{all }\ell^\infty\text{ targets},
\tag{21}
\]

whereas

\[
\text{compact/Schatten raw semigroup differences}
\Rightarrow
\text{Möbius excluded}.
\tag{22}
\]

Any future proposal must therefore identify what extra structure changes this dichotomy and why that extra structure is intrinsic rather than a disguised encoding of `mu` or `M(x)`.

## 5. Prior-art and novelty audit

The Bost–Connes system, its canonical semigroup isometries, and the number-state representation are established prior art and were already audited in `MC-138`–`MC-148`. No novelty is claimed for those objects.

The operator-theoretic step is also standard in mechanism. An operator sending an orthonormal basis to orthogonal basis vectors with scalar weights is a weighted shift/injection; its norm is the supremum of the weights, and compactness is equivalent to the weights tending to zero. For example, modern weighted-shift references record the classical compactness criterion explicitly; the proof in Section 1 is included because this represented semigroup map is sparse rather than the usual nearest-neighbor unilateral shift and the direct argument is shorter than transporting notation.

A targeted literature search also located Greenfield, Marcolli and Teh, *Twisted Spectral Triples and Quantum Statistical Mechanical Systems*, P-Adic Numbers, Ultrametric Analysis, and Applications **6** (2014), 81–104, DOI `10.1134/S2070046614020010`, which develops twisted spectral-triple constructions related to the Bost–Connes quantum statistical mechanical system. That literature is a boundary, not support for a stronger no-go: the present calculation concerns only the raw commutators of arithmetic diagonals with the canonical semigroup isometries in the number-state representation. It does not collapse twisted commutators, alternative Dirac operators, or other spectral-triple data to `(1)`.

Targeted searches for Bost–Connes semigroup commutators together with Möbius arithmetic did not locate the exact norm/essential-norm classification `(5)`. No novelty inference is drawn from that absence. The classification is an elementary specialization of standard weighted-shift facts plus classical Möbius multiplicativity, so the result is recorded as `EXACT-DERIVED` with **no novelty claim**.

## Boundaries and falsification tests

- **Raw canonical semigroup family only.** The result concerns `[D_a,S_m]` with the standard number-state semigroup isometries. A twisted commutator, different correspondence, different representation, or different Dirac/derivation requires a separate theorem.
- **No claim that compact commutators are a spectral-triple axiom.** Ordinary spectral triples require bounded commutators with the Dirac operator; compactness typically belongs elsewhere in the definition. Compactness and Schatten decay are tested here only as the first natural way one might try to sharpen the universally bounded raw semigroup difference into a selective decay condition.
- **Weights can create intermediate classes.** Replacing `(20)` by a source-forced weighted family, an average over `m`, a scale-dependent normalization, or another summability budget can evade the literal dichotomy. Such a proposal must explain why the weights are intrinsic and must be audited for target reconstruction or circularity.
- **The result is representation-specific.** It does not identify arbitrary universal-algebra commutators with the sparse operators in `(1)` outside the canonical number-state representation.
- **Essential norm is the relevant no-decay certificate.** Finite numerical checks cannot establish `(5)`; the proof uses explicit infinite squarefree subsequences, so the noncompactness cannot disappear at larger `k`.
- **No Mertens estimate follows.** The calculation constrains a representation-level selector. It neither bounds `M(x)` nor supplies an RH-equivalent criterion.

## Consequence for the line

The simple transverse regularity route left open by `MC-148` is now classified. The canonical semigroup isometries do detect multiplicative finite differences, but **raw boundedness detects too little and raw compact/Schatten decay demands the wrong behavior from Möbius**.

Accordingly, further Bost–Connes work should not spend cycles testing unweighted boundedness or compactness of `[D_\mu,S_m]`. A surviving noncommutative route must introduce an independently justified intermediate structure — weighted, twisted, averaged, representation-dependent, or otherwise nonlocal — and then demonstrate that it retains Möbius orientation while connecting non-tautologically to anchored additive Mertens excursion.