# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Match source-mixture complexity to target geometry before tracing downstream gain

**Linked intuitions:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-056-bounded-hilbert-marks-have-sharp-sqrt-k-sparse-mixture-tv-fidelity`.

AF-451--AF-452 identify the exact fixed-source stability carrier as completable source-law secants. AF-453 rules out uniform TV control when that carrier contains weakly collapsing secants of nonvanishing TV size. AF-454 shows that an infinite one-atom alphabet needs a uniformly discrete observed image, and AF-455 shows that compact downstream processing destroys such a bounded atomwise margin even in infinite dimension.

AF-456 adds the source-complexity gate. For the full probability simplex on a countably infinite alphabet and a bounded linear/barycentric observation `T:l1(A)->Y`, the TV modulus is the lower gain of `T` on `l1_0(A)`. Positive full-simplex TV fidelity exists exactly when the target contains an isomorphic copy of `l1`; reflexive targets, including Hilbert spaces, cannot provide it.

AF-457 makes the Hilbert sparse-mixture boundary sharp rather than model-dependent. If the atom marks are bounded by `M`, every Hilbert-valued barycentric observation has worst-case `k`-sparse TV modulus at most `M/sqrt(2k)`, and the orthogonal one-hot marking attains equality. Thus adding Hilbert dimension, changing bounded marks, or making the atoms mutually orthogonal cannot beat the square-root loss. Any better sparse-mixture theorem must come from a smaller physical source-law secant class, a non-Hilbert target geometry, or a different source metric.

The live arithmetic question is therefore source-specific: which mixture complexities are actually admissible, which balanced disjoint sparse secants survive in the completed physical source law, and what restricted lower gain is possible on precisely those secants? If the arithmetic class contains the AF-457 extremizing geometry at growing `k`, Hilbert TV conditioning must decay like `k^{-1/2}`; if it excludes that geometry, the exclusion itself is the theorem that must be proved.

## Keep identifiability, atom separation and mixture stability separate

Exact injectivity can hold with zero quantitative inverse margin. Uniform separation of individual atoms can also coexist with zero full-simplex TV gain, and AF-457 shows that even the optimal bounded Hilbert marking necessarily loses sparse-mixture margin as `k` grows. A fidelity theorem must therefore state the source metric, admissible mixture class, completed secants, target/operator category and positive restricted lower gain. Infinite dimension, positive essential norm, characteristic-kernel injectivity, atomwise separation, or orthogonality alone do not supply uniform recovery of growing-complexity mixtures.
