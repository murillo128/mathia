# MI-018 — Finite sign complexity transfers once harmonic tail cost beats collision loss

**Evidence level:** supported by AF-217--AF-220 and sharpened quantitatively by [AF-338](../../findings/AF-338-harmonic-collision-count-reduces-euler-sign-depth-to-linear-order.md), with the source-side limitation made explicit by [AF-339](../../findings/AF-339-mangoldt-minus-uniform-zero-sensitive-source-has-growing-sign-complexity.md). The observation theorem is fixed-finite-order in the absolutely convergent half-plane; no uniform growing-order total positivity, critical-line transport or stable inverse bound is claimed.

The useful observation currency is not positivity of every minor. It is a **finite sign-variation budget matched to a finite observation order**. AF-217 shows that the Euler-log family is not globally totally positive, while AF-218--AF-220 recover strict sign regularity at fixed order under quantitative sampling geometry.

AF-337 made the full-Euler tail comparison explicit but paid a quadratic sufficient depth by comparing higher harmonics to the first-harmonic determinant after discarding their inherited source collisions. AF-338 keeps those collisions. For a `k x k` minor, let `m_j` be the column harmonic labels, `S(m)=sum_j(m_j-1)` their total excess order, and `X(m)` the number of column pairs carrying unequal labels. Then exactly at the exponent-budget level

`X(m) <= (k-1) S(m)`.

Equal harmonic labels preserve the first-harmonic Vandermonde zero; only unequal labels can spend an inverse source-gap factor. The generalized Schur row-shape factor creates no positive power of the source scale. Consequently, for fixed order `r`, row spacing `h`, and `q_j in [P,AP]`, the full Euler-log sampling matrix is eventually strictly sign-regular through order `r` whenever

`sigma > r-1`,

with every full-Euler minor differing relatively from its first-harmonic minor by `O(P^-(sigma-(r-1)))`.

AF-339 shows why solving this observation-side transport problem does not by itself produce an RH-facing source. The canonical zero-sensitive discrepancy

`d_n=Lambda(n)-1`

has Dirichlet transform `-zeta'/zeta-zeta+1`, whose meromorphic continuation retains every zeta zero, but on `[P,AP]` its ordered sign variation is

`V=(2(A-1)+o(1)) P/log P`.

Thus the raw source eventually requires order `r=Theta(P/log P)` merely to enter the AF-216 sign-variation certificate. AF-338 is not uniform in such growing order, so its sufficient half-plane depth cannot be extrapolated mechanically to this regime.

The reusable principle now has two independent sides. On the **observation side**, price how much leading collision geometry each tail component actually destroys; treating every tail determinant independently can invent a much larger transport cost than the nonlinear expansion really pays. On the **source side**, do not infer a bounded certificate from zero sensitivity: the natural source may spend an unbounded amount of the very complexity the observation theorem consumes.

The remaining arithmetic problem is therefore a preserve-versus-simplify problem. Either construct an intrinsic recoding/grouping that reduces effective ordered sign complexity while proving that the zero-divisor discriminator remains recoverable, prove a genuinely growing-order observation theorem with the required joint source-scale control, or replace sign variation by a different finite source-complexity certificate that survives toward a zero-sensitive destination.

**Boundary.** AF-338 is an exact fixed-order sign theorem, not a prime discriminator or uniform inverse theorem. AF-339 obstructs only the raw `Lambda-1` representation and does not rule out source recodings, cumulative transforms, blockings, or other complexity notions. Any such simplification must audit whether the zero-sensitive meromorphic information survives the transformation.