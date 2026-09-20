# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Match source-mixture complexity to target geometry before tracing downstream gain

**Linked intuition:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`.

AF-451--AF-452 identify the exact fixed-source stability carrier as completable source-law secants. AF-453 rules out uniform TV control when that carrier contains weakly collapsing secants of nonvanishing TV size. AF-454 shows that an infinite one-atom alphabet needs a uniformly discrete observed image, and AF-455 shows that compact downstream processing destroys such a bounded atomwise margin even in infinite dimension.

AF-456 adds the source-complexity gate. For the full probability simplex on a countably infinite alphabet and a bounded linear/barycentric observation `T:l1(A)->Y`, the TV modulus is the lower gain of `T` on `l1_0(A)`. Positive full-simplex TV fidelity exists exactly when the target contains an isomorphic copy of `l1`; reflexive targets, including Hilbert spaces, cannot provide it. By contrast, the canonical `l2` one-hot carrier has the sharp `k`-sparse mixture modulus `1/sqrt(2k)`.

The live question is therefore not simply which noncompact operator survives downstream compression. For the physical arithmetic source class, what mixture complexity is actually admissible, what completed secants does it generate, and which target/operator category remains bounded below on those secants? If arbitrary mixtures are required in TV, a Hilbert target is categorically excluded; if only bounded-complexity mixtures matter, the dependence of the restricted lower gain on that complexity becomes part of the theorem.

## Keep identifiability, atom separation and mixture stability separate

Exact injectivity can hold with zero quantitative inverse margin. Uniform separation of individual atoms can also coexist with zero full-simplex TV gain: the one-hot Hilbert embedding is the canonical example. A fidelity theorem must therefore state the source metric, admissible mixture class, completed secants, target/operator category and positive restricted lower gain. Infinite dimension, positive essential norm, characteristic-kernel injectivity, or atomwise separation alone do not supply uniform recovery of arbitrary mixtures.
