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