---
type: adversarial-review
target: research/analytic_frontier/findings/ANF-042-two-pair-five-point-descent-has-a-sharp-one-self-energy-floor.md
---

# Adversarial review

## Adversary

The claimed pointwise danger criterion `(6)`--`(7)` is not literally an if-and-only-if at the central frequency `alpha=0`. There `a=b=p=q=0`, so `|q|<1` holds, but the original integrand has `c_1=c_2=1` and every phase is forced to zero, hence `h_0=0` for every horizontal geometry. The converse argument for `q=0` in `(19)` minimizes over a freely chosen nonzero `C=cos(nu)`, which is legitimate for fixed `alpha!=0` because the horizontal coordinates can realize arbitrary phases, but not for `alpha=0`, where necessarily `nu=0` and `C=1`.

The global floor `(3)`--`(4)` and the high-frequency amplitude barrier are unaffected, but the finding currently labels the danger criterion exact and states it for every frequency. Closure requires correcting the quantifier, e.g. restricting the iff criterion to nonzero frequencies and recording `alpha=0` as automatically safe, together with any downstream wording that presently treats `(7)` as exact at the origin.