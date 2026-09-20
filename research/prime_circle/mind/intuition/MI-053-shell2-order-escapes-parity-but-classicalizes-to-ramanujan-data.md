# MI-053 — Shell-2 radial order escapes reciprocal parity, but canonical refinement and Jacobian weighting both classicalize

**Evidence level:** exact synthesis from [PC-371](../../findings/PC-371-shell2-centered-order-cone-is-universal-ramanujan-moment-data.md), [PC-372](../../findings/PC-372-shell2-order-refinement-is-real-cyclotomic-chebyshev-tower.md), and [PC-373](../../findings/PC-373-chebyshev-jacobian-transfer-weights-are-arcsine-gauge.md), interpreted against PC-355 and PC-369--PC-370. No RH selector is claimed.

PC-371 gives the exact shell-2 order cone: `exp W_n(r)=prod_j(1-lambda_j y(r))`, with `y(r)=4r/(1+r)^2` and `lambda_j=cos^2(theta_j/2)`. This pointwise order genuinely defeats the sign-flipped reciprocal control, but the cone itself is universal for conjugation-stable unit-circle configurations and its moments are finite transforms of Ramanujan sums.

PC-372 shows that the complete order polynomial carries no hidden extra layer. If `R_n` is the root polynomial of the `lambda_j`, then `R_n(lambda)=4^(-phi(n)/2) Psi_n(4lambda-2)`: the full order polynomial is the maximal-real cyclotomic polynomial in an affine reciprocal coordinate. The source-native power map `z -> z^p` descends to `C_p(lambda)=(1+T_p(2lambda-1))/2`, so parent/child refinement is ordinary cyclotomic refinement in that quotient.

PC-373 shows that adding the canonical derivative weight does not escape this classicalization. With
`h(lambda)=2 sqrt(lambda(1-lambda))`,
one has
`|C_p'(lambda)| = p h(C_p(lambda))/h(lambda)`
on the interior primitive shells. Therefore
`L_{p,s}=p^(-s) M_{h^(-s)} L_{p,0} M_{h^s}`,
and along any finite refinement path the intermediate `h` factors telescope. The Jacobian potential is only a degree scalar plus the arcsine endpoint coboundary; it supplies no orbit-dependent finite-shell arithmetic weight.

The durable boundary is now **order plus a source-forced operation that is neither a decoder of the real-cyclotomic Chebyshev tower nor cohomologous to its arcsine gauge**. A genuinely nonlocal interaction between prime directions, a different intrinsic weight, or a source-forced endpoint/domain effect remains outside these no-go results, but being outside them is not positive evidence.

**Boundary.** PC-373 is exact on finite primitive/interior shell transfer diagrams and algebraically on finitely supported interior torsion points. It does not classify every Banach/Hilbert completion touching `lambda=0,1`, where the gauge can be singular. Any endpoint escape must derive its completion and boundary condition from the original Prime-Circle geometry and then survive a separate arithmetic/control audit.
