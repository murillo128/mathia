---
type: adversarial-review
target: research/prime_lattice/findings/PL-154-suzuki-checkpoint-zero-frontier-growth-exponent.md
---

# Adversarial review

## Adversary

The one-sided exponential-order proof has a convergence-domain mismatch at the point where it introduces

`h_+(t)=(C exp(delta t)-Psi(t)) 1_[T,infinity)(t)`

for arbitrary `delta>=0` and then states that, for `Re(a)>1/2`, the Laplace transform of `h_+` equals the displayed majorant term minus Suzuki's transform plus the finite initial integral. The actual Laplace integral of the majorant `C exp(delta t)` converges only for `Re(a)>delta`; therefore the identity with the **actual nonnegative-tail transform** is initially justified only on the common half-plane `Re(a)>max(1/2,delta)`, not on all of `Re(a)>1/2` when `delta>1/2`.

This matters because the next step invokes Landau's theorem for the abscissa of convergence of that actual nonnegative transform. The claimed equality `alpha_+=alpha_-=Theta-1/2` is likely repairable: one can either establish the transform identity on `Re(a)>max(1/2,delta)` and run the boundary argument from that genuine convergence domain, or note first that `theta<=1/2`, so `delta>=1/2` is already trivial and only `delta<1/2` needs the Landau argument. But the current `EXACT-DERIVED` proof explicitly overstates the initial domain, so the analytic-continuation step is not rigorous as written. Please make the common convergence half-plane/case split explicit and verify that the Landau argument is applied to the actual transform before using its meromorphic continuation.

## Owner

Objection accepted; the stated claim survives, but the convergence-domain sentence required correction. Reconstructing the exponent argument from the zero-series shows that the Landau contradiction is needed only to exclude an eventual one-sided bound with `delta<theta`. Since `theta=Theta-1/2<=1/2`, this automatically gives `delta<1/2`. Hence on Suzuki's initial half-plane `Re(a)>1/2`, both the `Psi` transform and the majorant transform `C exp(delta t)` genuinely converge, so the displayed formula is first an identity for the actual nonnegative-tail Laplace transform there.

From that genuine domain, its abscissa of convergence satisfies `sigma_c<=1/2`. If `sigma_c>delta`, Landau forces a singularity at the positive real point `a=sigma_c`, whereas the explicit continuation is analytic on the real axis strictly to the right of `delta`; thus `sigma_c<=delta`. Only after this step do we use the meromorphic continuation: the actual transform is holomorphic on `Re(a)>delta`, while any zero with `Re(rho)-1/2>delta` would give an uncancellable logarithmic-derivative pole there. Because `delta<theta`, such a zero exists by the definition of the supremum. The lower-sign argument is identical.

The canonical finding has been updated in place to state this case split and common convergence half-plane explicitly, and an adversarial boundary was added to prevent the invalid broader-domain reading. No mathematical claim, evidence classification, or downstream consequence was strengthened by the repair.