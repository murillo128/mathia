---
type: partial-positive
research_line: xi_flow
finding_id: XF-155
status: canonical
---

# XF-155 — vanishing positive heat exposes the outward edge mode beyond a universal log-2 depth

## Statement

For the maximal-contact matched pair used in XF-145--XF-154, positive heat has a second visibility mechanism outside the near-antipodal regime controlled by XF-153. A heat time that vanishes with degree can spectrally isolate the outward highest-frequency edge mode while costing only a polynomial factor.

Use the exact normalized finite-sum representation from XF-153. For even `N>=8`, write `n=N-2`,

\[
\delta_k=\frac n2-k,
\qquad 0\le k\le n,
\]

and, for outward complex depth `H>0`, real antipodal-distance coordinate `D in [0,pi/2]`, and normalized positive heat time `u>=0`,

\[
\mathcal A_N(u;H,D)
=
e^{NH-N^2u/4}
\left|
2^{-n}\sum_{k=0}^{n}\binom nk
 e^{2\delta_k(H+iD)+u\delta_k^2}
\right|.
\tag{1}
\]

Fix any `H>0` and any constant `c>2`, and set

\[
\boxed{
 u_N=c\frac{\log N}{N}.
}
\tag{2}
\]

Then `u_N->0`, and uniformly for every `D in [0,pi/2]`,

\[
\boxed{
\mathcal A_N(u_N;H,D)
=(1+o(1))
\exp\!\left(
(2N-2)H-(N-2)\log2-(N-1)u_N
\right).
}
\tag{3}
\]

Consequently,

\[
\boxed{
\lim_{N\to\infty}
\frac1N\log\mathcal A_N(u_N;H,D)
=2H-\log2
}
\tag{4}
\]

uniformly in `D`. Since the initial slice from XF-154 has exponential rate

\[
F_+(H,D)
=
H+\frac12\log\!\left(\cos^2D+\sinh^2H\right),
\tag{5}
\]

the complete positive-time history obeys the lower exponential bound

\[
\boxed{
\liminf_{N\to\infty}
\frac1N
\log\sup_{u\ge0}\mathcal A_N(u;H,D)
\ge
\max\{F_+(H,D),\,2H-\log2\}.
}
\tag{6}
\]

Thus this matched control cannot remain exponentially hidden throughout the full future once

\[
\boxed{
H>H_{\rm edge}:=\frac12\log2.
}
\tag{7}
\]

In physical complex height `h=(L/pi)H`, the corresponding universal upper cap on any exponentially hidden outward region certified by this control is

\[
\boxed{
h_{\rm edge}=\frac{L}{2\pi}\log2.}
\tag{8}
\]

This is an upper bound on the full-future blindness depth, not an exact full-future threshold.

## Exact edge-mode isolation

Factor the `k=0` term out of the finite sum in `(1)`. Its contribution to `mathcal A_N` is exactly

\[
E_N(u,H)
=
\exp\!\left(
(2N-2)H-(N-2)\log2-(N-1)u
\right).
\tag{9}
\]

Indeed, `delta_0=n/2` and

\[
\frac{N^2-n^2}{4}=N-1.
\]

After factoring this edge term, the `k`th summand has relative modulus

\[
R_{N,k}
=
\binom nk
\exp\!\left(-2kH-u\,k(n-k)\right),
\tag{10}
\]

and relative phase `e^{-2ikD}`. The crucial point is that the modulus estimate does not depend on `D`.

For `1<=k<=n/2`, use `k(n-k)>=kn/2` and `binom(n,k)<=n^k/k!` to obtain

\[
R_{N,k}
\le
\frac{B_N^k}{k!},
\qquad
B_N
:=n\exp\!\left(-2H-\frac{u_Nn}{2}\right).
\tag{11}
\]

Because `u_N=c log(N)/N` with `c>2`,

\[
B_N=N^{1-c/2+o(1)}\longrightarrow0,
\]

so

\[
\sum_{1\le k\le n/2}R_{N,k}
\le e^{B_N}-1=o(1).
\tag{12}
\]

For the opposite half write `k=n-j`, `0<=j<n/2`. Then

\[
R_{N,n-j}
=e^{-2nH}\binom nj
\exp\!\left(2jH-u_Nj(n-j)\right).
\tag{13}
\]

Using `j(n-j)>=jn/2` for `j>=1`, the whole upper half is bounded by

\[
e^{-2nH}
\exp(C_N),
\qquad
C_N
:=n\exp\!\left(2H-\frac{u_Nn}{2}\right)
=N^{1-c/2+o(1)},
\tag{14}
\]

which is again `o(1)` for fixed `H>0`. Therefore the sum of the moduli of every non-edge term is `o(1)` relative to the `k=0` term. No phase cancellation can remove the edge, uniformly in `D`, and `(3)` follows.

At the boundary `H=(log 2)/2`, `(9)` gives only polynomial loss,

\[
E_N(u_N,H_{\rm edge})
=2\exp(-(N-1)u_N)
=N^{-c+o(1)},
\tag{15}
\]

so even there the edge is no longer exponentially hidden.

## Where positive heat must beat the initial slice

XF-154 gives the exact initial-only threshold

\[
H_*(D)
=
\frac12\log\!\left(
\sqrt{3+\cos^2(2D)}-\cos(2D)
\right).
\tag{16}
\]

There is a unique physical crossover where this equals `H_edge`. Since the threshold equation can be written with `y=e^{2H}` as

\[
y^2+2\cos(2D)y-3=0,
\]

substituting `y=2` yields

\[
\boxed{
D_c
=\frac12\arccos\!\left(-\frac14\right)
\approx0.91173829
\quad(52.24\text{ degrees}).
}
\tag{17}
\]

For every fixed `D>D_c`,

\[
H_*(D)>\frac12\log2.
\]

Hence there is a nonempty interval

\[
\frac12\log2 < H < H_*(D)
\]

on which the initial slice is exponentially hidden but the vanishing positive heat time `(2)` is exponentially amplified. Positive heat therefore **strictly lowers the matched-control visibility obstruction** in this far-from-antipodal sector.

At the real-center endpoint `D=pi/2`, for example, the initial threshold is `(log 3)/2`, whereas the edge mechanism guarantees loss of exponential blindness above `(log 2)/2`.

This does not contradict XF-153. That finding proves exact exponential-threshold stability only for `0<=D<=pi/4`; there `H_*(D)` lies below `H_edge`, so the newly exposed edge mode becomes relevant only after the initial witness has already crossed its threshold.

## Evidence classification

**EXACT-DERIVED.** Equation `(3)` follows from the exact finite Fourier/Gaussian representation already established in XF-153 plus elementary binomial tail estimates. The crossover `(17)` is algebraic. A direct finite-`N` check was also used as a stress test of signs and normalization, but no numerical observation is needed by the proof.

The substantive delta is qualitative: XF-153 cannot be extended to the whole physical fundamental domain. In the outer sector `D>D_c`, positive heat reveals information that the initial trace still hides exponentially. The mechanism is spectral selection rather than longer-time accumulation: the chosen normalized heat time tends to zero while suppressing the interior binomial modes relative to the outward spectral edge.

## Prior-art audit

A directed audit searched structurally adjacent literature on backward heat flow of high-degree trigonometric polynomials, Curie--Weiss/Lee--Yang partition functions in complex field, and saddle-point/large-deviation descriptions of binomial sums. That literature contains closely related polynomial and heat-flow structures, but the present claim uses only the exact Mathia matched-packet formula `(1)` and the elementary tail comparison `(10)`--`(14)`. No external theorem is load-bearing, and no structurally matching statement for the `u_N~(log N)/N` edge isolation or the resulting `H_edge=(log 2)/2` cap was identified. No priority claim beyond this specific derived consequence is made, so `SOURCES.md` needs no new anchor.

## Falsification boundary

The edge-isolation asymptotic requires fixed `H>0`; it is not uniform in regimes where `H=H_N->0`. It concerns the canonical maximal-contact matched control and outward complex continuation only. It neither proves stable recovery of `Lambda_per` above `H_edge` nor shows that the actual Xi source realizes this matched direction.

Most importantly, `(6)` is a lower bound on the best full-future visibility rate. It does **not** prove that `max{F_+,2H-log2}` is the exact rate. Intermediate Fourier modes or different heat-time scalings may become visible earlier. In particular, the sector

\[
\frac\pi4<D\le D_c
\]

remains unresolved, and even for `D>D_c` the exact all-future threshold may lie below `(log 2)/2`.

## Consequences for the frontier

The near-antipodal conclusion of XF-153 remains sharp on its proved sector, but the target-side story is no longer globally static under positive heat. Away from the antipode, a vanishing amount of heat can act as a spectral projector: it kills the binomial bulk relative to the outward highest-frequency edge while charging only a polynomial loss to that edge.

The next target-side gate is therefore not to extend the one-Lipschitz argument mechanically. It is to determine the full large-`N` variational envelope of `(1)` across `pi/4<D<=pi/2`, including possible mesoscopic Fourier saddles and heat scalings between the initial slice and the edge-isolation regime. The source-side alternative remains unchanged: derive a Xi-specific restriction excluding the maximal-contact packet, or exhibit source-faithful information whose controlled observation crosses the resulting target-side barrier.