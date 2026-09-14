# MI-018 — Finite sign complexity transfers once harmonic tail cost beats collision loss

**Evidence level:** supported by AF-217--AF-220 and sharpened quantitatively by [AF-338](../../findings/AF-338-harmonic-collision-count-reduces-euler-sign-depth-to-linear-order.md), with the source-side boundary sharpened by [AF-339](../../findings/AF-339-mangoldt-minus-uniform-zero-sensitive-source-has-growing-sign-complexity.md) and [AF-340](../../findings/AF-340-constant-background-zero-isolation-forces-growing-sign-complexity.md). The observation theorem is fixed-finite-order in the absolutely convergent half-plane; no uniform growing-order total positivity, critical-line transport or stable inverse bound is claimed.

The useful observation currency is not positivity of every minor. It is a **finite sign-variation budget matched to a finite observation order**. AF-217 shows that the Euler-log family is not globally totally positive, while AF-218--AF-220 recover strict sign regularity at fixed order under quantitative sampling geometry.

AF-337 made the full-Euler tail comparison explicit but paid a quadratic sufficient depth by comparing higher-harmonic determinants to the first-harmonic determinant after discarding inherited source collisions. AF-338 keeps those collisions. For a `k x k` minor, let `m_j` be the column harmonic labels, `S(m)=sum_j(m_j-1)` their total excess order, and `X(m)` the number of column pairs carrying unequal labels. Then

`X(m) <= (k-1) S(m)`.

Equal harmonic labels preserve the first-harmonic Vandermonde zero; only unequal labels can spend an inverse source-gap factor. Consequently, for fixed order `r`, row spacing `h`, and `q_j in [P,AP]`, the full Euler-log sampling matrix is eventually strictly sign-regular through order `r` whenever

`sigma > r-1`,

with every full-Euler minor differing relatively from its first-harmonic minor by `O(P^-(sigma-(r-1)))`.

AF-339 shows that the pole-cancelled zero-sensitive discrepancy

`d_n=Lambda(n)-1`

has Dirichlet transform `-zeta'/zeta-zeta+1`, retains the zeta zero divisor, and has ordered sign variation

`V=(2(A-1)+o(1)) P/log P`

on every fixed multiplicative window `[P,AP]`. Thus the raw centered source eventually lies outside every fixed-order AF-216/AF-338 sign budget.

AF-340 identifies the exact resource responsible for that cost inside the complete constant-background family `Lambda(n)-c`. Every `c` retains the zeta-zero poles with the same residues. For `c<=0` the nonzero coefficients are one-signed and the ordered variation is zero, but the pole at `s=1` survives. For every `c>0` the variation is again `Theta(P/log P)`, and `c=1` is the **unique** constant background that cancels the pole at `1`.

So zero-divisor sensitivity itself does **not** force a complicated signed source: `Lambda` is already zero-sensitive and sign-simple. What becomes expensive under constant centering is isolating the zero-sensitive fluctuation from the main zeta pole. Within `Lambda-c`, bounded sign complexity and exact pole cancellation cannot coexist.

The reusable principle has three independent currencies. On the **observation side**, price how much leading collision geometry each tail component actually destroys. On the **source side**, do not infer a bounded certificate from zero sensitivity. At the **centering/interface**, do not infer that subtracting a simple main term is free: the operation that removes a dominant analytic background can create exactly the source oscillation consumed by the downstream theorem.

The remaining arithmetic problem is therefore more specific than “compress a zero-sensitive source.” Either construct a nonconstant/multiscale recoding or grouping that quarantines the main term while preserving recoverable zero-divisor information and a cheap finite certificate, prove a genuinely growing-order observation theorem with the required joint source-scale control, or replace ordered sign variation by another finite source-complexity invariant that survives toward a zero-sensitive destination.

**Boundary.** AF-338 is an exact fixed-order sign theorem, not a prime discriminator or uniform inverse theorem. AF-340 classifies only constant backgrounds `Lambda-c`; it does not show that pole cancellation is logically necessary for every RH-facing representation and does not rule out cumulative transforms, blockings, varying baselines or other source-complexity notions. Any proposed simplification must audit which zero-sensitive information and which main-term cancellation survive.