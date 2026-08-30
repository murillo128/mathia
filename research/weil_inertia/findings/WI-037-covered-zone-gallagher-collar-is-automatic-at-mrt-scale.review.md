---
type: adversarial-review
target: research/weil_inertia/findings/WI-037-covered-zone-gallagher-collar-is-automatic-at-mrt-scale.md
---

# Adversarial review

## Adversary

The mathematical collar argument is not the issue here; the canonical finding identity is. The current tree contains two independent findings carrying the same stable ID `WI-037`: this target and `research/weil_inertia/findings/WI-037-mrt-does-not-close-the-welding-glue-from-divisor-boundedness-alone.md`. They are materially different claims (covered-zone rational/collar transport versus a welding-weight/MRT citation obstruction), so a bare reference to `WI-037` no longer identifies one mathematical claim.

That violates the review protocol's identity invariant that one stable finding ID denotes one stable mathematical claim, and it is material because Git change-stream consumers and cross-finding references cannot distinguish which result `WI-037` means. The target therefore cannot survive canonically under this ID while the other independent `WI-037` remains under the same ID.

Resolution requires restoring one-to-one claim identity: decide which claim retains `WI-037`, and withdraw/re-publish the other independent claim under a distinct stable finding ID according to the owner protocol. No mathematical weakening is requested; the objection is to the current ambiguous canonical identity.
