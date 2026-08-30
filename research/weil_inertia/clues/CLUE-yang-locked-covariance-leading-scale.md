---
id: CLUE-weil-inertia-yang-locked-covariance-leading-scale
type: research-clue
status: proposed
origin: research-watch
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-043-maximal-pair-discrepancy-does-not-control-locked-four-point-covariance.md
  - research/weil_inertia/findings/WI-048-full-local-welding-main-has-subpolynomial-prefix-discrepancy.md
---

# Does the exact Yang locked covariance have a nonzero leading-scale term?

## Observation

Independent compute execution of GitHub issue `#91` replayed the unmodified pinned source
`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`
and all registered `t2_swaps.py` falsifiers before instrumenting the same finite cells.  For
every nonzero structured shift, the execution enumerated the full integer strip geometry and
applied the WI-043 centered identity with the source twin singular-series means.

Exact integer/rational bookkeeping gives a finite algebraic witness that the locked covariance
does not cancel identically in the source combination.  At `T=2400`, block `[2X,2.3X]`,
`b1=5`, `b2=2`, and `k=-6`, the admissible ordered tuple

```text
(m,m',n,n') = (389,419,157,169),   169 = 13^2,
```

has common strip offset `j=7`.  Together with its ordered reversal it gives coefficient `2`
to the positive `C2^0 log(13) log(157) log(389) log(419)` monomial in the formal locked
covariance.  The other centered summands have positive `C2`-degree, so the covariance is not
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
to relative error at most `1.7e-15`.  Runtime was 65 seconds and peak resident memory was
41 MiB, well within the issue boundary.  Thus the bounded source computation selects the
“residual of comparable scale” branch, not exact cancellation or visible stronger suppression.

## Research question

For the exact Yang cells and normalization, does the sum of WI-043 locked pair--pair
covariances have a nonzero negative leading term proportional to the full admissible strip
geometry, or must it eventually become lower order through arithmetic cancellation not visible
at these six finite scales?

## Why it may matter

A nonzero leading covariance term would eliminate the remaining source-specific projection
escape and show that the welding step genuinely needs joint four-prime information rather than
better marginal discrepancy or deterministic local-series centering.  Conversely, a proof of
eventual suppression would identify an arithmetic mechanism absent from both WI-043's abstract
obstruction and the present finite source scales.

## Decisive test

Derive an asymptotic or a rigorous upper/lower bound for the exact source-weighted locked
covariance across the structured `(b1,b2,k)` family, with the diagonal and deterministic
`S1/S2/S3` bookings retained.  A nonzero limiting normalized coefficient, or a matching
four-prime lower bound on a positive proportion of source mass, would support the leading-term
mechanism.  A proof that the covariance divided by its exact geometry/pair-main scale tends to
zero would refute it.  Any claimed suppression must also explain the exact finite monomial
witness rather than rely on an identity cancellation.

## Evidence boundary

The monomial witness is an exact finite/source certificate that cancellation is not an algebraic
identity.  The six normalized values are bounded numerical evidence only: they do not prove a
limit, its sign, a four-prime asymptotic, or the Yang--Yang one-sided fourth-moment theorem.
The computation used the pinned source's finite `Lambda`, intervals, `J=19`, base family, and
stored twin-constant value; it did not test transfer to different truncations or establish that
the observed finite scaling persists asymptotically.  This clue makes no novelty claim and is
not a canonical finding.
