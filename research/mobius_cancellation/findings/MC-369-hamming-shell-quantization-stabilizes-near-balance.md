# MC-369 — Hamming-shell quantization stabilizes near-balanced shell bias

**Status:** `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `RESOLUTION-TARIFF` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-368` showed that the exact-real prime-shell bias

\[
T=\sum_{i=1}^R d_iX_i
\]

can encode the entire punctured-cube source even when the shell masses `d_i` are arbitrarily close to `1/R`. The instability is entirely below the balanced Hamming-shell spacing. There is an exact finite-resolution quotient that removes that side channel, and its stability margin can be priced sharply.

Keep the even-rank source and endpoint notation of `MC-368`:

\[
X\sim\operatorname{Unif}\!\left(\{\pm1\}^R\setminus\{(+1,\ldots,+1)\}\right),
\qquad
T=\sum_{i=1}^R d_iX_i,
\qquad
\sum_i d_i=1.
\tag{1}
\]

Write

\[
d_i=\frac1R+\varepsilon_i,
\qquad
\sum_i\varepsilon_i=0,
\tag{2}
\]

and let

\[
J=\{i:X_i=-1\},
\qquad
K=|J|.
\tag{3}
\]

The balanced shell levels are

\[
b_k:=1-\frac{2k}{R},
\qquad 0\le k\le R,
\tag{4}
\]

with adjacent spacing `2/R`. Define the **Hamming-shell quantizer** `Q_R` by rounding a real input to its nearest level in `{b_0,...,b_R}` whenever that nearest level is unique.

Then

\[
\boxed{
T=b_K-2\varepsilon(J),
\qquad
\varepsilon(J):=\sum_{i\in J}\varepsilon_i.
}
\tag{5}
\]

Because `sum_i epsilon_i=0`,

\[
\boxed{
\max_{J\subseteq[R]}|\varepsilon(J)|
=\frac12\|\varepsilon\|_1.
}
\tag{6}
\]

Therefore the sharp strict margin

\[
\boxed{
\|\varepsilon\|_1<\frac1R
}
\tag{7}
\]

implies, simultaneously for every admissible source state,

\[
\boxed{
Q_R(T)=b_K.
}
\tag{8}
\]

Thus the quantized transcript forgets all subset identity and retains only Hamming weight. In count form, with `d_i=n_i/N`, condition `(7)` is exactly

\[
\boxed{
\sum_{i=1}^R\left|n_i-\frac NR\right|<\frac NR.
}
\tag{9}
\]

Under `(7)`, every coordinate has the same squared posterior predictability as at exact balance:

\[
\boxed{
\left\|\mathbf E[X_i\mid Q_R(T)]\right\|_2^2
=
\frac{2^R-R}{R(2^R-1)}
=\frac1R+O(2^{-R}).
}
\tag{10}
\]

Any further measurable coarsening of `Q_R(T)` has no larger own-phase leakage. Consequently the `MC-338` leakage-energy inequality gives

\[
\boxed{
\delta(W)
\ge
\left(
1-\sqrt{\mathcal E(W)}
\sqrt{\frac{2^R-R}{R(2^R-1)}}
\right)_+,
}
\tag{11}
\]

and exact dephasing through this finite-resolution scalar channel requires

\[
\boxed{
\mathcal E(W)
\ge
\frac{R(2^R-1)}{2^R-R}
=R+o(1).
}
\tag{12}
\]

This does **not** prove that the arithmetic mechanism naturally observes `Q_R(T)` rather than the exact scalar `T`. It does identify the missing resolution hypothesis precisely: the near-balanced shell is stable once the allowed scalar resolution cannot resolve perturbations across the half-gap `1/R` between balanced Hamming levels.

No estimate for `M(x)` and no zero-free result follows.

## 1. Exact perturbation identity

From `MC-368`,

\[
T=1-2d(J).
\]

Using `(2)` and `K=|J|`,

\[
d(J)=\frac KR+\varepsilon(J),
\]

so

\[
T
=1-\frac{2K}{R}-2\varepsilon(J)
=b_K-2\varepsilon(J),
\]

which proves `(5)`.

For a zero-sum real vector `epsilon`, let `P={i:epsilon_i>0}` and `N={i:epsilon_i<0}`. Then

\[
\sum_{i\in P}\varepsilon_i
=-\sum_{i\in N}\varepsilon_i
=\frac12\sum_i|\varepsilon_i|.
\]

Every subset sum lies between those two extrema, and both extrema are attained by `P` and `N`. This proves `(6)` exactly.

The distance from `T` to its balanced reference level `b_K` is therefore at most

\[
2\max_J|\varepsilon(J)|=\|\varepsilon\|_1.
\tag{13}
\]

Since adjacent balanced levels are `2/R` apart, the open Voronoi cell around `b_K` has radius `1/R`. Condition `(7)` puts every source state strictly inside its original cell, proving `(8)`.

The strict threshold is sharp as a **uniform nearest-shell decoding margin**. If `||epsilon||_1>1/R`, a subset attaining the positive or negative extremum in `(6)` moves by more than the half-gap, so its nearest balanced level is no longer `b_K`. At equality, a boundary tie can occur. Thus `1/R` is not an arbitrary safety constant introduced by the proof; it is the exact worst-case perturbation radius for this quotient.

## 2. The posterior collapses to Hamming weight

Under `(7)`, equation `(8)` makes `Q_R(T)` and `K` equivalent random variables because the levels `b_k` are distinct. Conditioned on `K=k>0`, the punctured-cube law is uniform over the `k`-subsets `J` of `[R]`. Hence

\[
\mathbf P(i\in J\mid K=k)=\frac{k}{R}
\]

and therefore

\[
\mathbf E[X_i\mid K=k]
=1-\frac{2k}{R}
=b_k.
\tag{14}
\]

It follows that

\[
\mathbf E[X_i\mid Q_R(T)]
=Q_R(T).
\tag{15}
\]

On the full sign cube,

\[
\mathbf E\left[\left(\frac1R\sum_iX_i\right)^2\right]=\frac1R.
\]

Removing the all-`+1` state and renormalizing gives

\[
\mathbf E[b_K^2]
=
\frac{2^R/R-1}{2^R-1}
=
\frac{2^R-R}{R(2^R-1)},
\]

which proves `(10)`. Conditional-expectation contraction proves the same upper bound for every downstream coarsening.

The important distinction from `MC-368` is representational, not asymptotic. The exact scalar can have up to `2^R-1` different source-dependent values and can be injective. The Hamming-shell quotient has only `R+1` possible levels and is permutation-invariant. Under `(7)`, the exponentially fine subset-sum code is removed exactly rather than merely estimated to be small.

## 3. The near-balanced counterexample of MC-368 is neutralized after this quotient

`MC-368` used the integer family

\[
n_i=B+2^{i-1},
\qquad
N=RB+2^R-1,
\tag{16}
\]

whose exact subset sums are all distinct for `B>2^R-1`. Hence exact access to `T` recovers the full source even as `B->infinity`.

For each fixed `R`, however,

\[
\left\|d-\frac1R\mathbf 1\right\|_1\longrightarrow0
\qquad(B\to\infty).
\tag{17}
\]

Therefore `(7)` eventually holds. At that point the same exact-real injective scalar, after the fixed symmetric quotient `Q_R`, carries only `K` and has the leakage `(10)`.

This separates two facts that `MC-368` deliberately left unresolved:

- approximate balance alone does not control information under exact-real observation;
- approximate balance **plus a specified finite-resolution quotient** can control it, and the required tolerance is exactly comparable with the balanced-shell half-gap.

The resolution condition is therefore not cosmetic. It is the mathematical operation that destroys the fine subset-sum address bits responsible for the discontinuity in `MC-368`.

## 4. Prior art and novelty boundary

The surrounding additive-combinatorial mechanisms are classical. Chapter 7 of Terence Tao and Van H. Vu, *Additive Combinatorics* (Cambridge University Press, 2006; DOI `10.1017/CBO9780511755149.008`), treats Littlewood--Offord concentration of weighted sign sums and the inverse question of what additive structure is forced by unusually concentrated sums. Equal coefficients are the canonical high-concentration/Hamming-weight case. At the opposite extreme, Tom Bohman, *A construction for sets of integers with distinct subset sums*, Electronic Journal of Combinatorics **5** (1998), R3, DOI `10.37236/1341`, studies coefficient sets whose subset sums are all distinct, the exact-real mechanism already used in `MC-368`.

A targeted search also checked weighted-Hamming, Boolean-slice, Littlewood--Offord, inverse Littlewood--Offord, and finite-precision subset-sum formulations. No novelty is claimed for nearest-neighbor quantization, exchangeability on a Hamming slice, the identity `max_J |sum_(i in J) epsilon_i|=||epsilon||_1/2` for zero-sum coefficients, or the general principle that finite precision can collapse subset-sum encodings.

The durable Mathia delta is narrower: for the **specific arithmetic shell-bias provenance of `MC-368`**, the natural permutation-symmetric Hamming-shell quotient has an exact and sharp `L^1` stability tariff `(7)`, after which the previous `Theta(1/R)` leakage-energy obstruction is restored verbatim. This is a concrete answer to the finite-resolution branch left open in the prior finding, not a new theorem about Littlewood--Offord theory.

## Boundaries and falsification tests

- **The quotient is an additional observation model.** Nothing here proves that the actual analytic coefficient architecture is forced to see only `Q_R(T)`. If it has exact or finer access to `T`, the `MC-368` subset-sum side channel remains live.
- **The metric is aggregate `L^1`, not coordinatewise closeness.** Tiny `L^infinity` error alone is insufficient for growing `R`; the exact stability margin is controlled by `||d-R^{-1}1||_1` because a subset can collect coherent same-sign perturbations.
- **Strict half-gap.** Condition `(7)` avoids ties. At `1/R` the nearest-shell map can be ambiguous; beyond it some source state crosses a shell boundary.
- **Even rank and the punctured source law.** Formula `(10)` uses the same even-rank punctured-cube model as `MC-368`. The quantization identity `(5)` itself does not require even rank, but no broader endpoint-source claim is made here.
- **Exact endpoint provenance.** The shell scalar must first be derived from the actual arithmetic partition as in `MC-296`/`MC-368`. This theorem does not license assigning the same tariff to unrelated weighted observables.
- **Multiple side channels remain outside the claim.** Individual prime data, several shell statistics, log-weighted sums, adaptive observations, or a finer quantizer can reveal more than `K`.
- **No arithmetic equidistribution theorem is supplied.** Condition `(9)` is a deterministic admission condition. This finding does not prove that rational-prime defect counts satisfy it at the endpoint scale.
- **No Mertens consequence.** The result prices one concrete observation channel; it does not bound `M(x)` or exclude zeros.

## Consequence for the research line

The resolution branch left open by `MC-368` is now exact. The prime-shell bias has two sharply different information regimes:

1. with exact-real access, arbitrarily small imbalance can encode every source coordinate through distinct subset sums;
2. after the permutation-symmetric Hamming-shell quotient, every mass vector satisfying `||d-R^{-1}1||_1<1/R` collapses to the same Hamming-weight transcript as exact balance, restoring own-phase leakage `Theta(1/R)` and an `R+o(1)` exact-dephasing energy cost.

This narrows the surviving arithmetic problem again. A future endpoint argument need not force **exact** equal defect-cell counts, but it must prove both pieces of a concrete resolution bridge: an arithmetic `L^1` imbalance bound strong enough for the observation scale, and a canonical reason the coefficient architecture cannot resolve below the corresponding shell spacing. Without the second piece `MC-368` applies; with it, `(7)`--`(12)` give the exact tariff.