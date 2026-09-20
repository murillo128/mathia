# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Match source-mixture complexity to target geometry before tracing downstream gain

**Linked intuitions:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-056-bounded-hilbert-marks-have-sharp-sqrt-k-sparse-mixture-tv-fidelity`, `MI-057-paired-sign-cubes-transfer-banach-type-to-source-relative-mixture-fidelity`.

AF-451--AF-452 identify the exact fixed-source stability carrier as completable source-law secants. AF-453 rules out uniform TV control when that carrier contains weakly collapsing secants of nonvanishing TV size. AF-454 shows that an infinite one-atom alphabet needs a uniformly discrete observed image, and AF-455 shows that compact downstream processing destroys such a bounded atomwise margin even in infinite dimension.

AF-456 adds the source-complexity gate. For the full probability simplex on a countably infinite alphabet and a bounded linear/barycentric observation `T:l1(A)->Y`, the TV modulus is the lower gain of `T` on `l1_0(A)`. Positive full-simplex TV fidelity exists exactly when the target contains an isomorphic copy of `l1`; reflexive targets, including Hilbert spaces, cannot provide it.

AF-457 makes the Hilbert sparse-mixture boundary sharp rather than model-dependent. If the atom marks are bounded by `M`, every Hilbert-valued barycentric observation has worst-case `k`-sparse TV modulus at most `M/sqrt(2k)`, and the orthogonal one-hot marking attains equality. Thus adding Hilbert dimension, changing bounded marks, or making the atoms mutually orthogonal cannot beat the square-root loss.

AF-458 identifies the source-side certificate that transfers this geometry beyond the unrestricted simplex. In any Banach target of type `p in [1,2]`, bounded marks have worst-case `k`-sparse TV modulus at most `T_p(Y) M k^(1/p-1)`. More importantly, the same ceiling applies to a restricted physical source law whenever its completed secant carrier contains a complete paired `k`-cube: `2k` atoms whose balanced disjoint sign orientations are all completable. The exponent is sharp for the ambient type category, while failure of the cube condition is only an escape from this particular obstruction, not a fidelity theorem.

The live arithmetic question is therefore exact enough to test on the source itself: for growing `k`, does the completed physical source-law carrier contain paired sign cubes, approximate substitutes with controlled distortion, or some stricter geometry that excludes them? If such cubes survive, the target's Banach type already bounds the attainable TV gain; if they do not, the mathematically useful resource is the arithmetic constraint that removes those secants.

## Keep identifiability, atom separation and mixture stability separate

Exact injectivity can hold with zero quantitative inverse margin. Uniform separation of individual atoms can also coexist with zero full-simplex TV gain, and AF-457--AF-458 show that even optimal bounded target geometry can lose sparse-mixture margin as source complexity grows. A fidelity theorem must therefore state the source metric, admissible mixture class, completed secants, target/operator category and positive restricted lower gain. Infinite dimension, positive essential norm, characteristic-kernel injectivity, atomwise separation, orthogonality, or absence of one particular paired cube alone do not supply uniform recovery of growing-complexity mixtures.
