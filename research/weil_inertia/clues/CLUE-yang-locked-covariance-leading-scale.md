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
  - research/weil_inertia/findings/WI-052-barban-davenport-halberstam-suppresses-pure-quotient-prime-modes.md
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

WI-052 now removes the strongest **pure quotient** version of that witness from the prime-specific
bulk. Proper prime powers carry only `o(1)` of the source Mertens base measure, so the dominant
large coefficients are actual distinct prime moduli. Classical Barban--Davenport--Halberstam
variance then implies that, on every fixed power-separated interior
`alpha+beta <= 1-delta`, the Mertens-averaged `L^2` projection of the centered von Mangoldt
function onto residue-class-constant modes modulo `b1` or `b2` is `o(1)`. Thus actual primes
cannot imitate the order-one quadratic `mod r` witness of WI-051 throughout a positive-mass
interior region. The unresolved aliasing is narrower: it must live in the **nonzero
shift-frequency fibers inside residue classes**, concentrate toward the short-shift boundary, or
arise from the separately booked collision/analytic interface. BDH alone does not control those
nonzero fibers or the locked pair--pair covariance.

## Research question

For the exact Yang cells and normalization **outside every fixed polylogarithmic reduced-coefficient
range**, after replacing the factorized twin model by the genuine full four-form local
singular-series model, does the remaining WI-043 locked pair--pair covariance have a nonzero
negative leading term proportional to the full admissible strip geometry, or must it become
lower order through arithmetic cancellation? WI-050 settles the corresponding question in the
polylogarithmic coefficient regime in favor of lower order. WI-051 identifies the large-index
aliasing mechanism, while WI-052 shows that its residue-class-constant quotient component is
arithmetically suppressed for actual primes on every fixed power-separated interior. The live
prime-specific question is therefore whether **nonzero aliasing / within-residue pair-correlation
fibers** can carry leading mass in the power-sized coefficient regime, especially near or beyond
the interface where the available shift count becomes short.

## Why it may matter

A nonzero leading **post-local-main** covariance term in those nonzero fibers would identify the
genuinely surviving arithmetic obstruction and show that the welding step needs coefficient-uniform
joint four-prime information beyond ordinary AP variance and deterministic local-series centering.
Conversely, a proof that those fibers are negligible would remove the principal prime-specific
escape left after WI-049--WI-052 and could supply the missing arithmetic mechanism needed to
finish the one-sided fourth-moment route. WI-052 is important here because it prevents the search
from spending effort on arbitrary quotient witnesses that classical prime-distribution variance
already rules out in the bulk.

## Research disposition

**Accepted, narrowed by WI-049--WI-052.** The exact monomial witness establishes that the source
covariance is not an algebraic zero, and the finite-scale run shows a stable enough signal to
justify a targeted asymptotic audit. WI-049 proves that the genuine full four-form deterministic
local main is centered with `o(1)` normalized source bias after the long-cell/short-boundary
split. WI-050 (`research/weil_inertia/findings/WI-050-polylog-locked-four-prime-cells-fall-to-higher-dimensional-siegel-walfisz.md`)
then proves, using Bienvenu's established theorem, that the genuine post-local-main four-prime
residual is itself `o(1)` on every fixed polylogarithmic coprime base range. WI-051
(`research/weil_inertia/findings/WI-051-complexity-one-fourier-control-does-not-remove-coefficient-wall.md`)
shows that source-faithful localization creates coherent large-index fibers and that ordinary
one-variable `U^2` control cannot bound them for arbitrary functions. WI-052
(`research/weil_inertia/findings/WI-052-barban-davenport-halberstam-suppresses-pure-quotient-prime-modes.md`)
then uses classical AP variance to suppress the residue-class-constant part of those fibers for
actual primes on every fixed power-separated interior. The accepted target is now specifically
the **nonzero aliasing / within-residue pair-correlation contribution to the post-four-form-local-main
prime residual for power-sized coefficients**, with the short-shift boundary and separately
booked collision/analytic interface kept distinct.

## Decisive test

Decompose the exact source-weighted locked covariance by reduced coefficient size, retaining the
source diagonal/collision and deterministic `S1/S2/S3` bookings and subtracting the genuine full
four-form Hardy--Littlewood local model cellwise. The polylogarithmic part is already controlled
by WI-050, and the pure residue-class quotient projection on every fixed power-separated interior
is controlled by WI-052. On the remaining family, resolve the localized Fourier fibers
`A_r(t), A_q(-t)` with **nonzero** fiber parameter `t`, or derive a direct joint estimate that
bypasses this decomposition. A viable suppression proof must show that their post-local-main
source-weighted contribution is `o(1)` uniformly through the power-sized coefficient region, with
a separate estimate for the shrinking short-shift boundary. A nonzero limiting coefficient on a
positive proportion of that mass, or a matching coefficient-uniform four-prime lower bound,
would support the leading-term mechanism. A proof that the complementary nonzero-fiber residual
is `o(1)` would refute it and close the clue. Any claimed suppression must still explain the exact
finite monomial witness rather than rely on identity cancellation.

## Evidence boundary

The monomial witness is an exact finite/source certificate that cancellation is not an algebraic
identity. The six normalized values are bounded numerical evidence only: they do not prove a
limit, its sign, a four-prime asymptotic, or the Yang--Yang one-sided fourth-moment theorem.
WI-049 rigorously removes the deterministic full-Euler local-main bias at the source scale.
WI-050 rigorously controls the **aggregated** post-local-main residual only when the reduced
coefficients are bounded by a fixed power of `log X`; it neither proves that this subfamily carries
a positive fraction of the source ledger nor supplies any theorem for the power-sized coefficient
range. WI-051 is an exact finite Fourier/localization obstruction for generic bounded functions,
not a counterexample built from primes. WI-052 is prime-specific but controls only the
residue-class-constant `L^2` quotient projection, and only uniformly on fixed power-separated
interiors; it does not control nonzero aliasing fibers, twin-prime residuals, the shrinking
`alpha+beta=1` boundary, or the coupled four-prime covariance. The original computation used the
pinned source's finite `Lambda`, intervals, `J=19`, base family, and stored twin-constant value; it
has not yet been rerun after subtracting the genuine full four-form local model. This clue makes
no novelty claim and is not a canonical finding.
