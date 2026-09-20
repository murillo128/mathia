# MI-053 — Shell-2 radial order escapes reciprocal parity, but its canonical refinement is the real-cyclotomic Chebyshev tower

**Evidence level:** exact synthesis from [PC-371](../../findings/PC-371-shell2-centered-order-cone-is-universal-ramanujan-moment-data.md) and [PC-372](../../findings/PC-372-shell2-order-refinement-is-real-cyclotomic-chebyshev-tower.md), interpreted against PC-355 and PC-369--PC-370. No RH selector is claimed.

PC-371 gives the exact shell-2 order cone: `exp W_n(r)=prod_j(1-lambda_j y(r))`, with `y(r)=4r/(1+r)^2` and `lambda_j=cos^2(theta_j/2)`. This pointwise order genuinely defeats the sign-flipped reciprocal control, but the cone itself is universal for conjugation-stable unit-circle configurations and its moments are finite transforms of Ramanujan sums.

PC-372 shows that the complete polynomial carries no hidden extra layer. If `R_n` is the root polynomial of the `lambda_j`, then `R_n(lambda)=4^(-phi(n)/2) Psi_n(4lambda-2)`, so the full order polynomial is just the maximal-real cyclotomic polynomial in an affine reciprocal coordinate. The source-native power map `z -> z^p` descends exactly to `C_p(lambda)=(1+T_p(2lambda-1))/2`, and the parent/child preimage law is precisely the maximal-real form of ordinary cyclotomic refinement.

Thus the most canonical cross-shell repair left by PC-371 also classicalizes. It can reject generic irrational unit-circle controls only by detecting torsion/root-of-unity dynamics already present in the cyclotomic/Bost--Connes tower. Retaining the full order polynomial plus its natural power-map refinement is therefore not a new arithmetic selector; it is another exact coordinate system for classical cyclotomic data.

The durable boundary is now **order plus a cross-shell operation not reducible to Chebyshev pullback/cyclotomic refinement and not merely a decoder of the cyclotomic tower**. PC-372 explicitly leaves derivative-weighted transfer operators, source-forced interactions between different prime directions, and other genuinely nonlocal constructions outside its theorem, but none is established as useful merely by lying outside it.

**Boundary.** PC-372 closes the canonical power/refinement route, not every nonlinear or nonlocal order-sensitive construction. Any surviving operation still has to beat both the reciprocal control and the stronger classicalization test.