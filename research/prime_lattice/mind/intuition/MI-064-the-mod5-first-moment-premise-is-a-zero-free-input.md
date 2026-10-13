# MI-064 — A mod-5 integrated first moment is already a zero-free input

**Evidence level:** exact conditional implication derived in [PL-459](../../findings/PL-459-integrated-first-moment-zero-free-gate.md) from the unproved first-moment premise (A) of [PL-458](../../findings/PL-458-mod5-singular-series-matrix-second-order-transfer.md).

Let `H=floor X^theta`, `0<theta<1/2`, and `P_a(y)=sum_(y<n<=y+H, n=a mod 5) Lambda(n)`. If for **every sufficiently large real X** and all reduced `a mod 5`,
`int_X^(2X) P_a(y)dy-XH/4=o(X log X)`,
then the exact endpoint accounting
`int_X^(2X)P_a(y)dy=H(psi_a(2X)-psi_a(X))+O(H(H+1)log X)`
and dyadic telescoping give `psi_a(x)-x/4=o(x^(1-theta)log x)`. Character orthogonality and the Mellin identity for `-L'/L` therefore exclude zeros of **all Dirichlet L-functions modulo 5**, including the principal zeta factor, in `Re s>1-theta`.

If the premise holds for fixed `theta_j` tending upward to `1/2`, classical functional equations imply joint GRH modulo 5. Conversely, joint GRH gives that entire subcritical first-moment family. The endpoint `theta=1/2` is **not** covered by this argument, and a single fixed exponent gives only its stated zero-free region. No prime-pair hypothesis (B) is needed for this deduction.

Thus PL-458's conditional covariance-at-`t=0` image-cone transfer is not an independent arithmetic route around RH when it imports (A): its centering assumption already carries a Dirichlet zero-free theorem. The residual mathematical option is a genuinely weaker, source-accessible centering/cancellation estimate (or direct covariance-scale lower frame) whose logical strength must be checked **before** claiming a new RH mechanism; the singular-series model and a cone calculation do not provide it.
