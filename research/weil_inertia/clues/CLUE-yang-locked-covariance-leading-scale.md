---
id: CLUE-weil-inertia-yang-locked-covariance-leading-scale
type: research-clue
status: accepted
origin: research-watch
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-043-maximal-pair-discrepancy-does-not-control-locked-four-point-covariance.md
  - research/weil_inertia/findings/WI-048-full-local-welding-main-has-subpolynomial-prefix-discrepancy.md
  - research/weil_inertia/findings/WI-049-locked-four-prime-local-main-centers-cellwise.md
  - research/weil_inertia/findings/WI-050-polylog-locked-four-prime-cells-fall-to-higher-dimensional-siegel-walfisz.md
  - research/weil_inertia/findings/WI-051-complexity-one-fourier-control-does-not-remove-coefficient-wall.md
---

# Does the exact Yang locked covariance have a nonzero leading-scale term?

## Observation

Independent compute execution of GitHub issue `#91` replayed the unmodified pinned source
`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`
and all registered `t2_swaps.py` falsifiers before instrumenting the same finite cells. For
every nonzero structured shift, the execution enumerated the full integer strip geometry and
applied the WI-043 centered identity with the source twin singular-series means.

Exact integer/rational bookkeeping gives a finite algebraic witness that the locked covariance
does not cancel identically in the source combination. At `T=2400`, block `[2X,2.3X]`,
`b1=5`, `b2=2`, and `k=-6`, the admissible ordered tuple

```text
(m,m',n,n') = (389,419,157,169),   169 = 13^2,
```

has common strip offset `j=7`. Together with its ordered reversal it gives coefficient `2`
to the positive `C2^0 log(13) log(157) log(389) log(419)` monomial in the formal locked
covariance. The other centered summands have positive `C2`-degree, so the covariance is not
removed by an algebraic `S1-2*S2+S3` identity.

Using source double precision only for normalized diagnostics, six consecutive doubled scales
`T=2400,4800,9600,19200,38400,76800` gave respectively

```text
locked covariance / pair main:
-0.4425, -0.3485, -0.3026, -0.2278, -0.2659, -0.3186

locked covariance / exact geometry count:
-0.7267, -0.7073, -0.7027, -0.5766, -0.7106, -0.8803
```

The source swap, centered `S1` decomposition, and full `D` recomposition agreed at every scale
to relative error at most `1.7e-15`. Runtime was 65 seconds and peak resident memory was
41 MiB, well within the issue boundary. Thus the bounded source computation selects the
“residual of comparable scale” branch, not exact cancellation or visible stronger suppression.

WI-049 now removes the deterministic local-model escape at the actual source scale. For the
genuine four-form Hardy--Littlewood local factor of a fixed admissible cell, the exact local
autocorrelation law gives

```text
mean over k mod p of sigma_4,p(k;j) = kappa_p(j)^2
```

prime by prime, hence over every finite CRT conductor. Its finite-conductor interval discrepancy
is `O((log P)^4)` uniformly in the admissible lock and dominant coprime prime-power bases and
survives deterministic bounded-variation weighting. Taking `P=X^4` past every nonzero
source-scale collision determinant makes the remaining Euler tail generic; WI-049 proves that
the full four-form local main then has `o(1)` normalized deterministic bias in the Yang
off-diagonal aggregation. Therefore a persistent leading covariance cannot be explained by a
missing deterministic four-prime singular-series main or by the finite-to-full Euler passage.
It must survive after that true joint local main is subtracted, or come from the separately
booked analytic/collision interface.

WI-050 supplies an additional unconditional suppression mechanism on a large structural
subregime. After the lock and shift are unsliced, the coprime Yang `S1` square is the
finite-complexity three-variable system

```text
(m, m-b1*k, n, n-b2*k).
```

Bienvenu's higher-dimensional Siegel--Walfisz theorem therefore gives the expected four-prime
asymptotic uniformly whenever `b1,b2 <= (log X)^B` for any fixed `B`; WI-049 then identifies
that asymptotic with the genuine cellwise four-form local main after aggregation. Thus the
post-local-main residual is rigorously lower order throughout every fixed polylogarithmic
coefficient regime. Any leading residual must be carried by super-polylogarithmic reduced
coefficients or by the separately booked collision/analytic interface.

WI-051 sharpens the remaining analytic target. The same unsliced four-form system has
Cauchy--Schwarz complexity exactly one, and on one common prime cyclic group its multilinear
average has an exact coefficient-independent Fourier/`U^2` representation. But this does not
remove the power-coefficient wall: in a common ambient group the Yang cells have relative volume
`asymp 1/(b1^2*b2^2)`, while localizing to the natural matched scales turns `k -> b1*k` and
`k -> b2*k` into maps onto proper subgroups. WI-051 gives an explicit bounded mean-zero quadratic
quotient phase for which the localized correlation remains order one while the ordinary `U^2`
norm tends to zero like a negative fourth-root of the subgroup index. Thus a successful
complexity-one repair must be **quotient-aware** after the genuine local main is removed; ordinary
one-variable `U^2=o(1)` is information-theoretically insufficient at source-faithful scale.

## Research question

For the exact Yang cells and normalization **outside every fixed polylogarithmic reduced-coefficient
range**, after replacing the factorized twin model by the genuine full four-form local
singular-series model, does the remaining WI-043 locked pair--pair covariance have a nonzero
negative leading term proportional to the full admissible strip geometry, or must it become
lower order through arithmetic cancellation? WI-050 settles the corresponding question in the
polylogarithmic coefficient regime in favor of lower order. WI-051 further reduces the plausible
repair space: any lower-order proof in the power-sized regime must control the quotient/aliasing
modes created by the large-index dilations, or bypass them with a genuinely joint estimate.

## Why it may matter

A nonzero leading **post-local-main** covariance term in the super-polylogarithmic/power-sized
coefficient region would eliminate the remaining source-specific projection escape and show that
the welding step genuinely needs coefficient-uniform joint four-prime information rather than
better marginal discrepancy or deterministic local-series centering. Conversely, a proof of
eventual suppression there would identify the missing arithmetic mechanism needed to finish the
one-sided fourth-moment route. WI-049 rules out an omitted Hardy--Littlewood four-form main and a
leading Euler-tail bias; WI-050 additionally rules out the entire fixed-polylog coefficient
regime as the source of a leading prime residual; WI-051 rules out the cheap inference that
complexity one plus ordinary `U^2` uniformity automatically controls the remaining anisotropic
cells.

## Research disposition

**Accepted, narrowed by WI-049, WI-050 and WI-051.** The exact monomial witness establishes that
the source covariance is not an algebraic zero, and the finite-scale run shows a stable enough
signal to justify a targeted asymptotic audit. WI-049 proves that the genuine full four-form
deterministic local main is centered with `o(1)` normalized source bias after the
long-cell/short-boundary split. WI-050 (`research/weil_inertia/findings/WI-050-polylog-locked-four-prime-cells-fall-to-higher-dimensional-siegel-walfisz.md`)
then proves, using Bienvenu's established theorem, that the genuine post-local-main four-prime
residual is itself `o(1)` on every fixed polylogarithmic coprime base range. WI-051
(`research/weil_inertia/findings/WI-051-complexity-one-fourier-control-does-not-remove-coefficient-wall.md`)
shows that the remaining system is Fourier-complexity one but that source-faithful localization
creates coherent quotient modes and necessarily coefficient-sensitive `U^2` control. The
accepted target is therefore specifically the **super-polylogarithmic/power-sized coefficient
contribution to the post-four-form-local-main prime residual, with quotient/AP aliasing controlled
explicitly**, while the separately booked collision/analytic interface remains distinct.

## Decisive test

Decompose the exact source-weighted locked covariance by reduced coefficient size, retaining the
source diagonal/collision and deterministic `S1/S2/S3` bookings and subtracting the genuine full
four-form Hardy--Littlewood local model cellwise. The polylogarithmic part is already controlled
by WI-050. On the complementary family, derive an asymptotic or rigorous upper/lower bound after
normalization by its exact source mass. A viable suppression proof should in particular establish
that the post-local-main prime residual has negligible mass on the quotient/aliasing Fourier
fibers induced by `k -> r*k` and `k -> q*k`, uniformly over a positive proportion of the
power-sized coefficient region, or supply a direct joint estimate that makes those fibers
irrelevant. A nonzero limiting coefficient on a positive proportion of that mass, or a matching
coefficient-uniform four-prime lower bound, would support the leading-term mechanism. A proof
that this complementary residual is `o(1)` would refute it and close the clue. Any claimed
suppression must explain both the exact finite monomial witness and the WI-051 quotient-mode
obstruction rather than rely on identity cancellation or unlocalized `U^2` control.

## Evidence boundary

The monomial witness is an exact finite/source certificate that cancellation is not an algebraic
identity. The six normalized values are bounded numerical evidence only: they do not prove a
limit, its sign, a four-prime asymptotic, or the Yang--Yang one-sided fourth-moment theorem.
WI-049 rigorously removes the deterministic full-Euler local-main bias at the source scale.
WI-050 rigorously controls the **aggregated** post-local-main residual only when the reduced
coefficients are bounded by a fixed power of `log X`; it neither proves that this subfamily carries
a positive fraction of the source ledger nor supplies any theorem for the power-sized coefficient
range. WI-051 is an exact finite Fourier/localization obstruction for generic bounded functions,
not a counterexample built from primes: it proves that ordinary `U^2` information alone cannot
exclude coherent quotient modes, but it leaves open a prime-specific theorem showing that the
genuine locally centered von Mangoldt residual is orthogonal to those modes. The original
computation used the pinned source's finite `Lambda`, intervals, `J=19`, base family, and stored
twin-constant value; it has not yet been rerun after subtracting the genuine full four-form local
model. This clue makes no novelty claim and is not a canonical finding.
