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

## Research question

For the exact Yang cells and normalization, after replacing the factorized twin model by the
genuine full four-form local singular-series model, does the remaining WI-043 locked pair--pair
covariance have a nonzero negative leading term proportional to the full admissible strip
geometry, or must it become lower order through arithmetic cancellation?

## Why it may matter

A nonzero leading **post-local-main** covariance term would eliminate the remaining
source-specific projection escape and show that the welding step genuinely needs joint
four-prime information rather than better marginal discrepancy or deterministic local-series
centering. Conversely, a proof of eventual suppression would identify an arithmetic mechanism
absent from WI-043's abstract obstruction. WI-049 now rules out both an omitted Hardy--Littlewood
four-form main and a leading Euler-tail bias, so this is the shortest remaining analytic fork in
the one-sided fourth-moment route.

## Research disposition

**Accepted, narrowed by WI-049.** The exact monomial witness establishes that the source
covariance is not an algebraic zero, and the finite-scale run shows a stable enough signal to
justify a targeted asymptotic audit. WI-049 proves that the genuine full four-form deterministic
local main is centered with `o(1)` normalized source bias after the long-cell/short-boundary split.
The accepted target is therefore specifically the **post-four-form-local-main prime residual**,
with the separately booked collision/analytic interface kept distinct.

## Decisive test

Recompute the exact source-weighted locked covariance across the structured `(b1,b2,k)` family
with the genuine full four-form Hardy--Littlewood local model subtracted cellwise, retaining the
source diagonal/collision and deterministic `S1/S2/S3` bookings. Then derive an asymptotic or
rigorous upper/lower bound for that residual. A nonzero limiting normalized coefficient, or a
matching four-prime lower bound on a positive proportion of source mass, would support the
leading-term mechanism. A proof that the post-local-main covariance divided by its exact
geometry/pair-main scale tends to zero would refute it. Any claimed suppression must explain
the exact finite monomial witness rather than rely on an identity cancellation.

## Evidence boundary

The monomial witness is an exact finite/source certificate that cancellation is not an algebraic
identity. The six normalized values are bounded numerical evidence only: they do not prove a
limit, its sign, a four-prime asymptotic, or the Yang--Yang one-sided fourth-moment theorem.
WI-049 now rigorously removes the deterministic full-Euler local-main bias at the source scale,
but it is **not** a prime-correlation theorem and does not control the genuine post-local-main
four-prime residual or the separately booked analytic/collision interface. The computation used
the pinned source's finite `Lambda`, intervals, `J=19`, base family, and stored twin-constant
value; it has not yet been rerun after subtracting the genuine full four-form local model. This
clue makes no novelty claim and is not a canonical finding.
