# MI-066 — Relative frames transfer frontiers but admit common off-critical poles

**Evidence level:** supported conditional/negative synthesis of [PL-465](../../findings/PL-465-relative-frame-transfers-dirichlet-zero-bounds.md) and [PL-467](../../findings/PL-467-relative-frame-admits-sparse-common-off-critical-poles.md). The actual-prime frame is unproved; the control is a bounded positive integer-supported source, not von Mangoldt coefficients or a Dirichlet Euler product. No external novelty or formal verification is claimed.

For fixed `0<theta<1` and actual mod-5 prime-power windows `P_a(y)=sum_(y<n<=y+H,n=a mod 5)Lambda(n)`, `H=floor X^theta`, take either `R_a=P_a-H/4` or `R_a=P_a-bar P_a`, where `bar P_a=X^(-1)int_X^(2X)P_a`. Set `S_X=int_X^(2X)R R^Tdy`. If

`S_X >= c_theta Diag(S_X)`, `c_theta>0`,

at all sufficiently large real `X`, every unit-modulus character probe satisfies

`E_chi:=int_X^(2X)|sum_a chi(a)R_a|^2dy >= c_theta tr(S_X)`.

Thus one independently bounded character energy controls every residue variance. For `Theta_chi=sup{Re rho:L(rho,chi)=0, 0<Re rho<1}`, PL-465 proves

`Theta_max-Theta_min <= 1-theta`.

A family of fixed exponents approaching `1` therefore forces equality of the four suprema; it does not fix their common value. Under a separately assumed zeta RH, Selberg's principal-channel bound supplies `E_chi0<<XH(log X)^2`, and the frame then excludes all four characters' zeros in `Re s>1-theta/2`. This use of the frame transfers an **absolute** upper bound supplied elsewhere.

PL-467 realizes the common-frontier escape in one fixed source. For every `1/2<beta<1`, it builds bounded positive weights `b_n` on `5 ∤ n` with correct leading density `sum_(n<=x,n=a mod 5)b_n=x/4+O(x^beta)`. For each fixed `1-beta<theta<1`, both centers give, eventually at every real `X`,

`S_X >= (1/4)Diag(S_X)`,

`lambda_min(S_X) asymp lambda_max(S_X) asymp H^2 X^(2beta-1)`.

Each character Dirichlet series has rightmost critical-strip poles at `Re s=beta`. Their combined pole set is finite, conjugation/reflection symmetric, with residues `-1` in the character channels and `-1/4` in the identity-residue series. Hence these poles cannot cancel in the identity average. These are divisor symmetries, not a functional equation.

The construction adds sine/cosine modes at log frequencies `kM`, with amplitudes `x^(beta-1)` and their reflected `x^(-beta)` companions, to the residue densities `1/4`, with `k=1,2,3` and fixed large `M`. A finite initial adjustment makes the integer weights positive. Character orthogonality places the poles in the chosen channels. After division by `HX^(beta-1)`, the window vector approaches four separated sine/cosine modes on `u=y/X in [1,2]`; their Gram matrix has a uniform positive margin. The approximation errors are

`O(H/X + X^(1-2beta) + X^(1-beta)/H)=o(1)`.

These respectively price window variation, reflected modes and integer sampling. Empirical centering subtracts the modes' mean outer product, which is `O(M^(-2))`, so it does not destroy the frame.

The missing absolute scale is explicit. Whenever `theta>2(1-beta)`, for every fixed finite `A`,

`V_1/[XH(log X)^A] asymp X^(theta+2beta-2)/(log X)^A -> infinity`.

This is exactly the regime `beta>1-theta/2` where [MI-065](MI-065-seam-filtering-recovers-sparse-arithmetic-poles-from-dyadic-variance.md) would exclude a pole if its absolute variance premise held. Sparse poles, positive weights, residue signs and the relative frame can coexist; they do not manufacture that upper bound. The control omits prime support, prime-pair laws, Euler products and a completed functional equation, so it does not settle what an additional actual-prime input could force.
