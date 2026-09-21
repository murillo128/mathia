# MI-060 — Mesh-scale inverse-chord regularization is Poisson renormalization, not prime spectral data

**Evidence level:** exact operator synthesis from [PC-383](../../findings/PC-383-mesh-scale-inverse-chord-regularization-is-exact-poisson-renormalization.md), closing the canonical shrinking inverse-chord scalar escape left by PC-382. The Poisson kernel and root-averaging semigroup are classical; the line-specific content is their exact realization in the normalized Prime-Circle weighted refinement.

For the regularized inverse chord

`q_epsilon(z)=(|1-z|^2+epsilon^2)^(-1/2)`,

after intrinsic `L^2` normalization the squared modulus is exactly the circle Poisson kernel `P_rho`, where `rho=exp(-2 asinh(epsilon/2))`. For the degree-`m` power map, root-fiber averaging obeys the exact semigroup law

`E_m P_rho = P_(rho^m)`.

Hence the normalized positive operator is

`T_(m,epsilon)^* T_(m,epsilon) = M_(P_(exp(-tau)))`,

with the single dimensionless parameter

`tau=2m asinh(epsilon/2)`.

At exact mesh matching `epsilon_(m,tau)=2 sinh(tau/(2m))`, this positive operator is identical for every refinement degree `m`, prime or composite. The order-one defect at `epsilon~1/m` is therefore not a recovered prime-sensitive spectral carrier; it is the same classical Poisson profile transported by an exact renormalization law.

This sharpens the fixed-continuous collapse of MI-059. Merely allowing a canonical singular regularization to shrink at the inverse-image mesh does not create arithmetic discrimination if the normalized modulus closes under the universal Poisson semigroup. A surviving scalar singular mechanism must break that closure through a different singular profile, phase/non-normal data not determined by `T^*T`, source-dependent structure, or genuinely cross-level/nonseparable coupling.

**Boundary.** PC-383 classifies the normalized modulus of this inverse-chord family and its singular values; it does not classify every singular weight or the full nonnormal spectrum. Other conductor-dependent profiles may have different root-fiber renormalization. Their arithmetic value must be demonstrated rather than inferred from mesh-scale variation alone.