# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Match source-mixture complexity to target geometry before tracing downstream gain

**Linked intuitions:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-056-bounded-hilbert-marks-have-sharp-sqrt-k-sparse-mixture-tv-fidelity`, `MI-057-paired-sign-cubes-transfer-banach-type-to-source-relative-mixture-fidelity`.

AF-451--AF-452 identify the exact fixed-source stability carrier as completable source-law secants. AF-453 rules out uniform TV control when that carrier contains weakly collapsing secants of nonvanishing TV size. AF-454 shows that an infinite one-atom alphabet needs a uniformly discrete observed image, and AF-455 shows that compact downstream processing destroys such a bounded atomwise margin even in infinite dimension.

AF-456 adds the source-complexity gate. For the full probability simplex on a countably infinite alphabet and a bounded linear/barycentric observation `T:l1(A)->Y`, the TV modulus is the lower gain of `T` on `l1_0(A)`. Positive full-simplex TV fidelity exists exactly when the target contains an isomorphic copy of `l1`; reflexive targets, including Hilbert spaces, cannot provide it.

AF-457 makes the Hilbert sparse-mixture boundary sharp rather than model-dependent. If the atom marks are bounded by `M`, every Hilbert-valued barycentric observation has worst-case `k`-sparse TV modulus at most `M/sqrt(2k)`, and the orthogonal one-hot marking attains equality. Thus adding Hilbert dimension, changing bounded marks, or making the atoms mutually orthogonal cannot beat the square-root loss.

AF-458 transfers the same geometry to a restricted physical source whenever its normalized completed-secant carrier contains a full paired sign `k`-cube. AF-459 removes the artificial all-or-nothing gate. If `D_k(C)` is the least mean TV distance from an ideal paired `k`-cube to the normalized physical carrier, then every bounded affine marking into a type-`p` Banach target obeys

`kappa_C(F_phi) <= M [T_p(Y) k^(1/p-1) + D_k(C)]`.

For `p>1`, `D_k(C)->0` already forces the restricted lower gain to vanish. Exact completion of a `1-o(1)` fraction of cube orientations is sufficient, since then `D_k(C)->0`; sparse forbidden orientations therefore do not evade the type obstruction. Conversely a uniform gain `kappa_0` forces `D_k(C)` to stay asymptotically bounded below by `kappa_0/M` up to the decaying type term.

The live arithmetic question is now quantitative and source-side: what is the asymptotic paired-cube completion profile `D_k(C)` of the actual physical carrier? If it tends to zero, target type already forces fidelity collapse. If it stays positive, the mathematically useful resource is the arithmetic constraint that keeps every large paired cube a positive average normalized-secant distance away. Either outcome should be established on the physical source carrier itself rather than inferred from ambient mixture dimension.

## Keep identifiability, atom separation and mixture stability separate

Exact injectivity can hold with zero quantitative inverse margin. Uniform separation of individual atoms can also coexist with zero full-simplex TV gain, and AF-457--AF-459 show that even optimal bounded target geometry can lose sparse-mixture margin as source complexity grows. A fidelity theorem must therefore state the source metric, admissible mixture class, completed secants, target/operator category and positive restricted lower gain. Infinite dimension, positive essential norm, characteristic-kernel injectivity, atomwise separation, orthogonality, or large defect from one particular paired cube alone do not supply uniform recovery of growing-complexity mixtures.
