# MC-384 — Chang composite-character theorem retains the log-log source horizon

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-REFINEMENT` · `SOURCE-COST` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The factorization-sensitive character-sum escape left open by `MC-383` is not supplied by the strongest classical composite-modulus theorem of Chang in its squarefree specialization. The obstruction is different from the `2^{-k}` saving loss isolated in `MC-382`: **Chang's applicability condition itself forces the conductor exponent to stay on the `log log` scale.**

Chang's Theorem 5 in *Short character sums for composite moduli* gives, for a primitive character modulo `q`, an interval `I` of length `N`, and the core

\[
q'=\prod_{p\mid q}p,
\]

a bound

\[
\left|\sum_{n\in I}\chi(n)\right|
< N\exp(-\sqrt{\log N})
\tag{1}
\]

under, among other hypotheses,

\[
q>N>\max_{p\mid q}p^{1000}
\tag{2}
\]

and

\[
\log N>
(\log q)^{1-c}
+C\log\!\left(2\frac{\log q}{\log q'}\right)
\frac{\log q'}{\log\log q},
\tag{3}
\]

for absolute positive constants `c,C`.

For the squarefree primitive source conductors relevant to the current endpoint branch, `q'=q`. Therefore `(3)` contains the unavoidable term

\[
C(\log 2)\frac{\log q}{\log\log q}.
\tag{4}
\]

Put

\[
N=y^{1+o(1)},
\qquad
q=y^{a(y)+o(1)}.
\tag{5}
\]

If Chang's theorem applies, `(3)` and `(4)` force

\[
1+o(1)
>
C(\log 2)\frac{a(y)}{\log(a(y)\log y)},
\tag{6}
\]

and hence

\[
\boxed{a(y)=O(\log\log y).}
\tag{7}
\]

Thus even after granting the source package the very strong local-prime hypothesis `(2)`, the theorem cannot be used as a black box for squarefree source conductors

\[
q=y^{a(y)}
\quad\text{with}\quad
a(y)\gg\log\log y.
\tag{8}
\]

This matters because the saving in `(1)` is far stronger than the endpoint frame needs. The failure beyond `(7)` is not a shortage of cancellation after the theorem starts; it is a **uniformity/admission barrier before the estimate is available**.

Cochrane--Granville--Zheng explicitly compare their 2026 moving-smoothness range with Chang's and state that their current proof requires `delta >> 1/log log q`, “more-or-less the same range of uniformity” as Chang in the squarefree setting. With `delta=log y/log q=1/a+o(1)`, that is the same source-exponent horizon `(7)`.

Consequently the surviving factor-local/multilinear escape after `MC-383` must be narrower than “use a composite-modulus theorem that sees the factorization.” It needs a theorem whose **squarefree moving-conductor admission range** itself extends past `log q/log N=O(log log N)`, or a mechanism that avoids requiring uniform single-character cancellation at every large primitive source conductor.

No estimate for `M(x)` follows.

## 1. Squarefree specialization makes the global core term unavoidable

Chang's theorem is designed for general composite moduli and records the squarefree core `q'` separately from `q`. That distinction can matter when the powerful part of the modulus is large. It disappears for the present source characters: their primitive conductors are squarefree, so

\[
q'=q.
\tag{9}
\]

Substituting `(9)` into the second term of `(3)` gives exactly

\[
C\log(2)\frac{\log q}{\log\log q}.
\tag{10}
\]

Discarding the first positive term `(log q)^{1-c}` only weakens the hypothesis, so every squarefree application necessarily satisfies

\[
\log N>
C\log(2)\frac{\log q}{\log\log q}.
\tag{11}
\]

This is the only part needed for the source-horizon audit.

## 2. The admission condition converts directly to `a=O(log log y)`

Let `L=log y`. Under `(5)`,

\[
\log N=(1+o(1))L,
\qquad
\log q=(a+o(1))L,
\qquad
\log\log q=\log(aL)+o(1).
\tag{12}
\]

Equation `(11)` therefore yields `(6)`. Equivalently, for some absolute `K>0`, every sufficiently large admissible pair obeys

\[
a\le K\log(aL).
\tag{13}
\]

Since `log a=o(a)`, `(13)` implies

\[
a=O(\log L)=O(\log\log y).
\tag{14}
\]

For example, if `a/log L -> infinity`, then `log(aL)=log L+log a=o(a)` along any such sequence satisfying `(13)`, contradicting `(13)`. The exact constant in `(14)` is immaterial here; the point is the order of the moving-conductor range.

The first term of `(3)` does not open a hidden wider squarefree regime. It is another positive requirement. In the range `a=O(log log y)` its contribution is compatible with large `y` for fixed `c>0`; beyond that, removing it entirely still leaves `(11)` and therefore `(14)`.

## 3. The small-prime-factor hypothesis does not explain this horizon

Condition `(2)` is restrictive: at interval scale `N=y^{1+o(1)}` it asks every prime divisor of the conductor to be at most roughly `y^{1/1000}`. But for the purpose of testing whether Chang supplies the missing factor-local escape, we may grant this hypothesis for free.

Indeed the endpoint source-cost arguments already use fixed-power cutoffs. Under a trial bound `P<=y^A`, deleting source-incidence columns belonging to primes above `y^beta` costs only `O(A/beta)` dimensions. Choosing any fixed `beta<1/1000` would put every surviving source conductor inside the prime-factor range `(2)` while preserving the same **linear-in-`A`** codimension shape used in `MC-381`.

Even in that optimistic subspace, however, a surviving primitive conductor `q=y^a` with `a>>log log y` is outside Chang's squarefree admission range by `(14)`. Therefore the old small-prime-factor requirement is not the load-bearing reason this theorem fails to continue the source-cost proof beyond the current analytic horizon.

This is only an audit of a possible black-box continuation. It does not assert that the endpoint necessarily supplies conductors meeting all of Chang's remaining hypotheses, nor that every surviving mode has conductor comparable with the common radical `P`.

## 4. The theorem's saving would otherwise be more than sufficient

Once Chang's theorem applies, `(1)` gives normalized cancellation

\[
\frac1N\left|\sum_{n\in I}\chi(n)\right|
<\exp(-\sqrt{\log N}).
\tag{15}
\]

At `N=y^{1+o(1)}`, this decays faster than every fixed negative power of `log y`. Thus the issue identified here is not analogous to the fixed global-modulus power tariff in `MC-383`, where a family-cardinality gain could not pay a term `q^theta` with fixed `theta>0`.

Chang's estimate has excellent output once admitted. The bottleneck is the hypothesis `(11)`, which prevents that output from being invoked uniformly when the squarefree conductor occupies more than `O(log log y)` interval-length exponents.

This separates two analytically distinct failure modes now present in the frontier:

- `MC-382`: iterated single-character q-vdC loses saving exponentially with conductor-layer depth;
- `MC-383`: a collective small-doubling theorem pays a fixed positive power of one global modulus;
- the present finding: a factorization-sensitive composite-modulus theorem has strong terminal saving, but its **entry condition** already enforces the same log-log conductor horizon in the squarefree regime.

A future route must avoid all three shapes, not merely improve the numerical saving after admission.

## 5. Prior art and novelty boundary

The primary theorem is Mei-Chu Chang, *Short character sums for composite moduli*, Journal d'Analyse Mathématique 123 (2014), 1--33, DOI `10.1007/s11854-014-0012-y`, arXiv:`1201.0299v2`. Theorem 5 is the source of `(1)`--`(3)`. Its proof iterates a Graham--Ringrose/Postnikov-style factorization and is prior art in full.

Cochrane--Granville--Zheng, *Mixed incomplete character sums of rational functions with smooth moduli*, arXiv:`2601.10927v1` (`MC-S46`), explicitly state that their moving parameter currently requires `delta >> 1/log log q` and describe this as essentially the same uniformity range as Chang for the relevant squarefree setting. Their later proof records `delta asymp 1/k` together with an iterated-depth condition, supplying an independent consistency check on the translation `(5)`--`(14)`.

No novelty is claimed for Chang's theorem, its proof, the Graham--Ringrose lineage, or the `log log` uniformity range. The durable Mathia contribution is the source-resource audit: in the squarefree endpoint specialization, the core term in Chang's own theorem statement converts directly into `(7)`, so this established factorization-sensitive route does not realize the factor-local escape left open by `MC-383`.

## Boundaries and falsification tests

- **This does not rule out factor-local character methods.** It rules out using Chang Theorem 5 as a black box beyond its squarefree moving-conductor admission range.
- **The common radical and primitive conductor remain distinct.** The calculation concerns any individual squarefree primitive conductor `q`; it does not identify `q` with the common source radical `P` unless that equality is separately proved for the mode in question.
- **A stronger modern theorem could evade the barrier.** In particular, an estimate with an admission condition depending on local factors without a `log q/log log q` squarefree-core term would not be covered.
- **A collective theorem could avoid uniform single-character control.** The present argument says nothing about a genuinely multilinear/source-family estimate that never asks for `(1)` separately for each high-conductor mode.
- **No lower bound for actual character sums is proved.** Failure of a theorem hypothesis is not evidence that the corresponding sum is large.
- **No RH-scale Möbius estimate is inferred.** The result only narrows the analytic source-cost program inside this research line.

## Research consequence

The next analytic search should not treat “composite modulus” or “factorization-sensitive” as sufficient evidence of a route past `MC-382`--`MC-383`. For squarefree source conductors, a candidate theorem must be audited first for the scaling of its **admission condition** after `q=y^a`, `N=y^{1+o(1)}`. If that condition already implies `a=O(log log y)`, stronger cancellation inside the admitted range cannot improve the current source-cost order.
