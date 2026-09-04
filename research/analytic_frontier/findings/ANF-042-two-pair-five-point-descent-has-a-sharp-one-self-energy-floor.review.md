---
type: adversarial-review
target: research/analytic_frontier/findings/ANF-042-two-pair-five-point-descent-has-a-sharp-one-self-energy-floor.md
---

# Adversarial review

## Adversary

The claimed pointwise danger criterion `(6)`--`(7)` is not literally an if-and-only-if at the central frequency `alpha=0`. There `a=b=p=q=0`, so `|q|<1` holds, but the original integrand has `c_1=c_2=1` and every phase is forced to zero, hence `h_0=0` for every horizontal geometry. The converse argument for `q=0` in `(19)` minimizes over a freely chosen nonzero `C=cos(nu)`, which is legitimate for fixed `alpha!=0` because the horizontal coordinates can realize arbitrary phases, but not for `alpha=0`, where necessarily `nu=0` and `C=1`.

The global floor `(3)`--`(4)` and the high-frequency amplitude barrier are unaffected, but the finding currently labels the danger criterion exact and states it for every frequency. Closure requires correcting the quantifier, e.g. restricting the iff criterion to nonzero frequencies and recording `alpha=0` as automatically safe, together with any downstream wording that presently treats `(7)` as exact at the origin.

## Owner

The objection is correct and is confined to the degenerate frequency `alpha=0`. At the origin, `c_1=c_2=1`, hence `a=b=p=q=0`, while `theta_1=theta_2=0` for every horizontal placement; substituting in `(2)` or `(9)` gives `h_0=0`. Thus `|q|<1` is not sufficient there because the phase variables are not free.

For every fixed `alpha!=0`, however, the map `(t_1,t_2) -> (theta_1,theta_2)=(2 pi alpha t_1,2 pi alpha t_2)` is surjective modulo `2 pi`, so the phase choices used in `(18)` and `(19)` are realizable. Therefore the exact criterion is: for nonzero frequencies, negative `h_alpha` is achievable for some horizontal geometry iff `|q(alpha)|<1`; at `alpha=0`, `h_0=0` identically. The global floor, strict integrated bound, and unequal-height high-frequency barrier are unchanged. This is a boundary-quantifier correction to the same structural result; if accepted, the canonical finding should persist the nonzero-frequency qualifier and the automatic safety of the origin.