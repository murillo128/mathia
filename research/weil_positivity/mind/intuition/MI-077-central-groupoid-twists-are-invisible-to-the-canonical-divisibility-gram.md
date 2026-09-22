# MI-077 — Central groupoid twists are invisible to the canonical divisibility Gram

**Evidence level:** exact synthesis from WP-409 and [WP-410](../../findings/WP-410-central-bost-connes-groupoid-twists-leave-critical-divisibility-gram-unchanged.md) for the canonical Bost--Connes projection/KMS readout.

WP-409 showed that a base-independent scalar multiplier on `Q_+^x` can change projective scale multiplication while leaving the canonical divisibility projection Gram unchanged. WP-410 removes the remaining hope that arbitrary **central** groupoid dependence repairs this while the readout is fixed. For a `U(1)` Fell-line twist over the Bost--Connes groupoid with the same source/range geometry and scale dynamics, the range projections still satisfy

`E_n=S_n S_n^*=1_(n Zhat)`, `E_m E_n=E_lcm(m,n)`.

The critical KMS weights therefore remain `phi(E_n)=n^(-1)`, and after normalization the Gram is exactly

`G_(m,n)=gcd(m,n)/sqrt(mn)`.

The twist may carry nontrivial upstream phase geometry, including base dependence, but the canonical projection/KMS observable has already discarded it. Enlarging the central twist class without changing the positive readout therefore adds representation structure but no destination-visible information.

This closes a useful category distinction. The live phase route must either interrogate off-diagonal/phase-sensitive observables **before** projection, use a genuinely noncentral or operator-valued bundle whose multiplication changes the retained carrier, alter source/range/category geometry, or couple finite and archimedean data before the final positive scalar readout is formed. Merely replacing one scalar central twist by a more general scalar central twist cannot change the critical divisibility Gram.

**Boundary.** WP-410 does not show that central twists are mathematically trivial, nor that every phase-sensitive observable is blind to them. The invariance is specific to the canonical divisibility range projections and their KMS-normalized Gram under unchanged source/range geometry and dynamics. A different readout can retain phase information, but must then re-prove positivity, arithmetic canonicity and connection to the Weil destination.