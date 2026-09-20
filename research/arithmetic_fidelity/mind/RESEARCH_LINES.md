# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Match source-mixture complexity to target geometry before tracing downstream gain

**Linked intuitions:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-056-bounded-hilbert-marks-have-sharp-sqrt-k-sparse-mixture-tv-fidelity`, `MI-057-paired-sign-cubes-transfer-banach-type-to-source-relative-mixture-fidelity`.

AF-451--AF-452 identify the exact fixed-source stability carrier as completable source-law secants. AF-453 rules out uniform TV control when that carrier contains weakly collapsing secants of nonvanishing TV size. AF-454 shows that an infinite one-atom alphabet needs a uniformly discrete observed image, and AF-455 shows that compact downstream processing destroys such a bounded atomwise margin even in infinite dimension.

AF-456 adds the source-complexity gate. For the full probability simplex on a countably infinite alphabet and a bounded linear/barycentric observation `T:l1(A)->Y`, positive full-simplex TV fidelity exists exactly when the target contains an isomorphic copy of `l1`; reflexive targets, including Hilbert spaces, cannot provide it. AF-457 makes the Hilbert sparse-mixture boundary sharp: bounded atom marks force worst-case `k`-sparse TV modulus at most `M/sqrt(2k)`, attained by orthogonal one-hot marks.

AF-458--AF-459 transfer the same obstruction to restricted physical sources through paired-cube completion. If `D_k(C)` is the least mean TV distance from an ideal paired `k`-cube to the normalized physical carrier, then every bounded affine marking into a type-`p` Banach target obeys `kappa_C(F_phi) <= M[T_p(Y)k^(1/p-1)+D_k(C)]`. Exact completion of almost all orientations already gives `D_k(C)->0`; sparse forbidden orientations do not evade the type obstruction.

AF-460 now settles one broad source-side model exactly. The normalized kernel carrier of any bounded finite-rank linear law on an infinite alphabet has `D_k=0` for every fixed `k`. Therefore finitely many bounded linear source constraints cannot by themselves protect bounded-affine TV fidelity once their full normalized kernel remains physically admissible. The load-bearing question is no longer whether such laws reduce dimension, but whether the **actual physical completion** removes the kernel cube geometry.

The live arithmetic question is consequently sharper: which source constraints keep the normalized physical carrier a positive average distance from every large paired cube after completion? Positivity, support/boundary restrictions, nonlinear or infinite-dimensional laws are plausible categories only insofar as one can prove that separation on the physical carrier. If the carrier still contains a normalized finite-rank kernel, target type already forces fidelity collapse.

## Keep identifiability, atom separation and mixture stability separate

Exact injectivity can hold with zero quantitative inverse margin. Uniform separation of individual atoms can coexist with zero full-simplex TV gain, and AF-457--AF-460 show that even optimal bounded target geometry loses growing-complexity margin whenever the physical source admits enough paired-cube completion. A fidelity theorem must state the source metric, admissible mixture class, completed secants, target/operator category and positive restricted lower gain. Infinite dimension, positive essential norm, characteristic-kernel injectivity, atomwise separation, orthogonality, or finitely many bounded conservation laws do not supply uniform recovery unless they exclude the relevant normalized kernel geometry.