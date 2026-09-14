# MI-040 — Unitary zero incidence spends two algebraic codimensions

**Evidence level:** conditional exact consequence of [AF-333](../../findings/AF-333-schanuel-forces-prime-phase-algebraic-codimension-at-most-one.md), assuming Schanuel's conjecture. No unconditional zero-free theorem or RH consequence is claimed.

For multiplicatively independent positive algebraic bases `a_1,...,a_n` and nonzero real `t`, AF-333 shows under Schanuel that the common-time phase tuple

`z(t)=(a_1^(-it),...,a_n^(-it))`

has `trdeg_Q Q(z_1,...,z_n) >= n-1`. Equivalently, its `Q`-Zariski closure can lose at most one algebraic codimension from the ambient torus.

A unit-circle cancellation consumes more than the single displayed equation suggests. If `n>=3` and `e_1(z)=sum_j z_j=0`, then `|z_j|=1` turns conjugation into inversion, so the same point also satisfies `sum_j z_j^(-1)=0`, equivalently `e_(n-1)(z)=0`. These two polynomial equations are independent for `n>=3`, forcing algebraic codimension at least two. That contradicts the Schanuel budget. Thus Schanuel forbids every nonzero-real-time equal-weight cancellation of three or more multiplicatively independent algebraic phases.

For the current eight-prime incidence problem this is sharper than the previous exceptional-time and coordinate-sparsity gates: **under Schanuel, `e_1=0` alone is already impossible, so the second target equation `e_4=0` is not needed.** The decisive resource is joint algebraic dimension of the whole phase tuple, not algebraicity of individual coordinates.

The reusable source principle is that retained provenance can increase the effective codimension of a target event. Here unit modulus is not decorative geometry: it converts the conjugate of one complex zero into a second algebraic relation on the same coordinates. An ambient equation count that forgets this provenance understates how much algebraic dependence the event requires.

The unconditional frontier is therefore precise. Six Exponentials gives coordinatewise algebraic sparsity, and exponential-algebraic exceptionalness constrains the parameter, but neither controls the joint polynomial-dependence budget. An unconditional replacement for the Schanuel step must exclude two independent algebraic relations on the common prime-phase tuple, or prove a comparably strong joint transcendence statement. More genericity, local conditioning, or algebraic-point classification does not address that missing currency.

**Boundary.** Every zero-free conclusion above is conditional on Schanuel. The argument is pointwise and gives no positive lower bound for the exponential sum; AF-329 near-incidence remains compatible with it. The common nonzero real parameter and multiplicative independence are essential to the transcendence-degree count.