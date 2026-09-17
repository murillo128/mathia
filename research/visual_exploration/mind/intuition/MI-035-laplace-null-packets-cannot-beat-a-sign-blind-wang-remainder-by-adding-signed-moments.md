# MI-035 — Laplace-null packets cannot beat a sign-blind Wang remainder by adding signed moments

**Evidence level:** literature+derived synthesis from [VIS-274](../../findings/VIS-274-wang-fixed-q-rescaled-laplace-limit.md) and [VIS-275](../../findings/VIS-275-wang-laplace-null-source-bound-floor.md). The obstruction concerns the rate certified by the current pointwise remainder envelope; it is not a lower bound on the true Wang residual.

At fixed physical `q`, VIS-274 shows that Wang's concentrating main term should be retained and rescaled rather than Taylor-collapsed. The normalized statistic then has a finite leading Laplace functional and an `O_h(1/log T)` remainder. A natural next move is to choose a signed packet with

`int h(q)e^(-4pi q)dq = 0`

and add further weighted moment cancellations in the hope of pushing below that rate.

VIS-275 shows why the current theorem interface cannot certify such an improvement. After the same fixed-`q` rescaling, the dominant available error bound is

`O((1/log T) int |h(q)| e^(-4pi q)dq)`.

The leading main term is a signed Laplace functional, but the proof envelope has already discarded the sign of the remainder. For every fixed nonzero packet, the weighted absolute norm is strictly positive. No finite collection of signed polynomial-Laplace moment constraints can make that majorant `o(1/log T)`.

The reusable distinction is between **cancelling a structured term and improving the theorem that controls what remains**. Orthogonality can remove a signed main component only while its sign/phase structure is still present. Once the proof passes to an absolute envelope, further signed cancellation conditions have nothing to act on.

The next useful source-side result must therefore expose new signed information: a first-order expansion such as `log(T) R_T(q) -> A(q)` in an integrable mode, a direct cancellation identity for the dominant Wang error, or a stronger pointwise remainder whose fixed-`q` rescaling is already `o(1/log T)`. Only then is it meaningful to engineer packets that cancel the new residual kernel and ask whether an arithmetic coefficient survives.

**Boundary.** The true residual for a special signed packet may be much smaller than the current majorant; VIS-275 does not exclude that. It says only that moment engineering alone cannot prove it through a sign-blind error interface. `T`-dependent packets with shrinking weighted `L^1` norm are also a different scaling problem.