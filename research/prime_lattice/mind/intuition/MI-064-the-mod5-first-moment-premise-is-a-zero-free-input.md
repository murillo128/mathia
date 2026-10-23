# MI-064 — Mod-5 window moments retain a zero-free prerequisite after empirical centering

**Evidence level:** supported; exact conditional implications in [PL-459](../../findings/PL-459-integrated-first-moment-zero-free-gate.md), [PL-461](../../findings/PL-461-single-identity-residue-moment-zero-free-gate.md), [PL-462](../../findings/PL-462-narrow-window-phase-coherence-zero-free-gate.md) and [PL-463](../../findings/PL-463-empirically-centered-window-variance-zero-free-gate.md). The actual-prime moment estimates are unproved premises, not conclusions.

Let `H=floor X^theta`, `P_a(y)=sum_(y<n<=y+H, n=a mod 5) Lambda(n)`, and `psi_a(x)=sum_(n<=x, n=a mod 5) Lambda(n)`. Every prime-moment premise below is required for **every sufficiently large real X**, with fixed `theta` and constants independent of `X`. The excluded zeros belong to all Dirichlet `L(s,chi)` modulo 5, including the primitive zeta component; the principal factor's extra Euler zeros on `Re s=0` are outside these half-planes.

For `0<theta<1/2`, combine the four-channel first-moment premise
`int_X^(2X) P_a(y)dy-XH/4=o(X log X)`
with the exact endpoint accounting
`int_X^(2X)P_a(y)dy=H(psi_a(2X)-psi_a(X))+O(H(H+1)log X)`
and dyadic telescoping to get `psi_a(x)-x/4=o(x^(1-theta)log x)`. Character orthogonality and the Mellin identity for `-L'/L` exclude zeros in `Re s>1-theta`.

For fixed `theta_j` tending upward to `1/2`, this first-moment family is equivalent to joint GRH modulo 5 by the classical explicit formula and functional equations. Its endpoint `theta=1/2` is **not** covered by the little-`o` argument. This diagnoses assumption (A) of [PL-458](../../findings/PL-458-mod5-singular-series-matrix-second-order-transfer.md), independently of its prime-pair assumption (B).

The raw second moment has a stronger one-channel obstruction. For `0<theta<=1/2`, it suffices that

`Q_11=int_X^(2X) P_1(y)^2 dy <= XH^2/16 + O(XH log X)`.

Cauchy--Schwarz and the same endpoint identity give only the **one-sided** error `psi_1(x)-x/4<=O(x^(1-theta)log x)`. PL-461 applies Landau positivity, using the explicitly checked absence of real mod-5 L-zeros, to continue its Mellin transform to `Re s>1-theta`. A single residue suffices because

`D_1(s)=sum_(n=1 mod 5) Lambda(n)n^(-s)=(1/4)sum_(chi mod 5)(-L'/L)(s,chi)` initially for `Re s>1`.

All character weights at the identity residue are `1`, so residues at coincident zeros add with the same sign instead of cancelling. The exact leading coefficient `1/16` matters. This raw ceiling at `theta=1/2` already implies joint GRH. In PL-458's strict range `1/6<theta<1/2`, just the `a=b=1` instance of (B) supplies it, without (A); the pair-to-moment endpoint error does **not** justify that transfer at `theta=1/2`. Dropping (A) while retaining (B) therefore does not evade the zero-free premise.

Nor does one selected narrow-window modulation per scale. Put `P_(1,t)=sum Lambda(n)n^(-it)` on the same window/residue and `Q_t=int|P_(1,t)|^2`. Nonnegative coefficients give

`cos^2(Delta/2) Q_0 <= Q_t <= Q_0`, `Delta=|t|log(1+H/X)<=pi`.

For `|t_X|=O(X sqrt(log X)/H^(3/2))`, the relative loss is `O(log X/H)`, hence costs only `O(XH log X)` against the raw main term. A raw ceiling at even one such `t_X` transfers to `Q_0` and the same zero-free region. This is positive-arc geometry, not a prime-specific cancellation law; it does not apply to signed or centered windows.

Empirical centering changes the exponent, not the presence of a zero-free prerequisite. For `0<theta<1`, set

`bar P_1=X^(-1)int_X^(2X)P_1(y)dy`,

`V_1=int_X^(2X)|P_1(y)-bar P_1|^2 dy`.

PL-463 proves that `V_1=O(XH(log X)^A)` for any fixed finite `A>=0` excludes zeros in **`Re s>1-theta/2`**, with no bound on `bar P_1-H/4`. For every real smooth `w` compactly supported in `(1,2)` with `int w=0`, Cauchy--Schwarz after removing the mean yields a probe bound of order `X/sqrt H` (up to `(log X)^(A/2)`). To recover the fixed test `w(n/X)` from the window average, write `tau=H/X` and

`B_tau f(u)=tau^(-1)int_0^tau f(u-v)dv`.

A finite inverse of its Taylor symbol, `(1-exp(-z))/z`, constructs a mean-zero `f_tau` of bounded `L^2` norm with `B_tau f_tau=w+O(tau^N)`. Choosing **`N(1-theta)>theta/2`** makes the resulting source error `O(X tau^N log X)` negligible. This removes the first-order approximation cutoff near `theta=2/3`; the required order and constants need not remain bounded as `theta` tends to `1`.

The resulting bound on `S_w(X)=sum_(n=1 mod 5)Lambda(n)w(n/X)` makes its scale Mellin transform holomorphic in `Re s>1-theta/2`. That transform equals `W(s)D_1(s)`, where `W(s)=int_1^2 w(u)u^(s-1)du`. Mean removal forces `W(1)=0`, eliminating the main pole. It does not force `W(rho)=0` for any `rho!=1`: a sufficiently localized real derivative bump detects each such mode. The **whole test family**, not one fixed probe, therefore retains every zero pole of `D_1`. Unlike the raw one-sided argument, this proof detects possible real zeros directly.

The positive-density control `dmu=(1/4+c x^(beta-1))dx`, `c>0`, `0<beta<1`, has empirically centered variance asymptotic to `c^2 C_beta H^2 X^(2beta-1)` with `C_beta>0`. Its ratio to `XH` is of order `X^(theta+2beta-2)`, so a pole at `beta=1-theta/2` is compatible with the ceiling. This explains the loss for general positive sources; it is not an optimality theorem for primes. At `theta=1/2`, the centered implication excludes zeros only to the right of `3/4`. Joint GRH follows from a family of fixed centered estimates with `theta_j` tending to **`1`**, not to `1/2`.

These operations are distinct from pointwise projection across the four residue coordinates, which creates the exact principal zero mode in [MI-062](MI-062-raw-and-exactly-centered-residue-grams-both-miss-the-dephasing-positivity-cone.md). Fitting a constant over `y in [X,2X]` does not impose that residue relation. Neither centered upper bounds nor raw moment ceilings are supplied by positivity of a Gram matrix, and a relative lower-frame inequality alone implies neither upper bound. The direct complex-polarized cone question of [MI-063](MI-063-the-live-prime-lattice-gate-is-a-complex-polarized-lower-frame-at-covariance-scale.md) remains distinct. Sparse scales, a center depending on `y`, or vertical-frequency averages are different hypotheses; none inherits these implications without another argument.
