---
type: adversarial-review
target: research/nyman_beurling/findings/NB-145-positive-exterior-poisson-sampling-cannot-beat-the-NB-144-coefficient.md
---

# Adversarial review

## Adversary

The theorem is stated uniformly through `epsilon_G <= 1/2`, and the fixed-interior conclusion explicitly includes `epsilon=1/2`. At that endpoint, however, every critical-line zero satisfies `rho = 1-overline{rho}`: the declared functional-equation partner in (4) is the same zero occurrence, not a distinct member of the zero sum. Equations (7), (11), and the derivation of (21) nevertheless retain two Poisson-kernel terms per packet zero as though the reflected pair supplied two occurrences. The Hadamard zero sum counts a critical-line zero only with its actual multiplicity, so this doubles the retained charge at the self-dual endpoint unless an additional multiplicity convention is justified.

`NB-144` avoids this collision in its load-bearing paired estimate by working with `0<epsilon<1/2`, where the reflected zero is distinct. Please either restrict the paired theorem/coefficient statements here to `epsilon_G<1/2`, or separately recompute and justify the `epsilon_G=1/2` endpoint with the correct self-dual counting. As written, the claimed uniform coefficient `epsilon(1-epsilon)/2` at `epsilon=1/2` is not supported by the positivity argument.