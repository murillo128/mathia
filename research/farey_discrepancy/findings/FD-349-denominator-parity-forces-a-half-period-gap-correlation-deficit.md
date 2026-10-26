# FD-349 — Denominator parity forces a half-period gap-correlation deficit

**Status:** LITERATURE+DERIVED + UNCONDITIONAL-ASYMPTOTIC-BOUND.

For genuine Farey gaps, every fixed offset from the half-period has a
correlation bounded strictly below the full gap energy:
\[
\boxed{\liminf_{Q\to\infty}\frac{Q^2}{\log Q}
 [S_0(Q)-S_{N_Q/2+r}(Q)]\ge\frac1{\pi^2},\qquad r\in\mathbb Z
 \text{ fixed}.}\tag{1}
\]
Consequently
\[
\limsup_{Q\to\infty}\frac{Q^2S_{N_Q/2+r}(Q)}{\log Q}
 \le\frac{11}{\pi^2},\qquad
\limsup_{Q\to\infty}\frac{S_{N_Q/2+r}(Q)}{S_0(Q)}\le\frac{11}{12}.
\tag{2}
\]
The limits run over all integer orders, hence also over primes.
The constant is not asserted sharp. This is a strict deficit at the
logarithmic scale, **not** the conjectured vanishing at that scale.

The mechanism uses FD-348's exact rational separation, but needs no
rank anti-concentration estimate. A small odd-denominator cusp can meet
only a cusp of twice its denominator or a much smaller gap; a cusp of
denominator twice an odd integer has the reverse size mismatch or also
meets a much smaller gap. Their harmonic gap energy forces (1).

## 1. Objects and a finite deficit certificate

Use the positive-point Farey convention
\[
0=x_0<\cdots<x_N=1,\quad N=\sum_{q\le Q}\varphi(q),\quad h=N/2,
\]
with `Q>=3`, periodic denominators, and `x_(k+N)=x_k+1`. Set
\[
g_k=x_{k+1}-x_k=\frac1{q_kq_{k+1}},\quad
s_k=\min(q_k,q_{k+1}),\quad S_j=\sum_{k=0}^{N-1}g_kg_{k+j}.
\]
The cyclic shift `P_l g` has entries `g_(k+l)`. Exactly,
\[
2(S_0-S_{h+r})=\|g-P_{h+r}g\|_2^2.\tag{3}
\]

Choose integers `t,L` with `1<=t`, `2t<=L<Q/2`, and
\[
2tL\epsilon<1,\qquad \epsilon=\frac2Q+\frac{|r|+1}{N}.
\tag{4}
\]
Define the two disjoint small-endpoint energies
\[
E_o(Q,t)=\sum_{\substack{s_k\le t\\s_k\ {m odd}}}g_k^2,
\qquad
E_2(Q,t)=\sum_{\substack{s_k\le t\\s_k\equiv2\ (4)}}g_k^2,
\]
and
\[
\eta=\frac{2t}{L},\qquad
\beta=\max\!\left\{\frac{Q}{2(Q-2t)},\eta\right\},\qquad
z_+=\max(0,z).
\]
Then the finite certificate is
\[
\boxed{\|g-P_{h+r}g\|_2^2
 \ge (1-\beta)_+^2 E_o(Q,t)+(1-\eta)_+^2 E_2(Q,t).}\tag{5}
\]

To prove it, take a gap with small endpoint denominator `q=s_k<=t`,
and put `d=s_(k+h+r)`. If `d<=L`,
[FD-348](FD-348-small-denominator-half-period-pairs-are-exact-rational-translates.md)
applies with thresholds `(t,L)`: the two small endpoints differ by
exactly one half. Thus `d=2q` for odd `q`, and `d=q/2` for `q=2 mod 4`.
For completeness, the rational-separation input compares the endpoint
displacement error `<=epsilon`, obtained from Dress's sample discrepancy
bound, with the minimum nonzero error `1/(2qd)`. Condition (4) makes
the comparison strict. This also fixes the cyclic lift and includes
the gap ending at `1`.

The other endpoint denominators of the source and target gaps, say
`b,b'`, lie respectively in `(Q-q,Q]` and `(Q-d,Q]`. Hence, if `d<=L`,
\[
\frac{g_{k+h+r}}{g_k}=\frac{qb}{db'}
\begin{cases}
\displaystyle\le\frac{Q}{2(Q-2t)},&q\text{ odd},\\[4pt]
\displaystyle\ge2(1-t/Q),&q\equiv2\pmod4.
\end{cases}\tag{6}
\]
If instead `d>L`, its other endpoint is greater than `Q/2`, so
\[
g_{k+h+r}<\frac2{QL},\qquad g_k\ge\frac1{qQ},\qquad
\frac{g_{k+h+r}}{g_k}\le\eta.\tag{7}
\]
For odd `q`, (6)–(7) give an absolute relative difference at least
`(1-beta)_+`. For `q=2 mod 4`, the close alternative gives at least
`1-2t/Q>=1-eta`, and the distant alternative gives `(1-eta)_+`.
Summing their squares over the disjoint index sets proves (5).
No involution property of `P_(h+r)` is used, so this works for nonzero
fixed offsets as well as for `r=0`.

## 2. The two parity classes carry enough logarithmic energy

When `2t<Q`, each reduced vertex with denominator at most `t` is the
unique small endpoint of both of its incident gaps. On the circle there
are exactly `phi(q)` such vertices of denominator `q`, including the
single vertex `0=1 mod 1` at `q=1`. Therefore for either parity class
`C` used above,
\[
\frac2{Q^2}\sum_{\substack{q\le t\\q\in C}}\frac{\varphi(q)}{q^2}
\le E_C(Q,t)\le
\frac2{(Q-t)^2}\sum_{\substack{q\le t\\q\in C}}\frac{\varphi(q)}{q^2}.
\tag{8}
\]
There is no double counting: no gap has two endpoints of denominator
at most `t`, because adjacent denominators sum to more than `Q`.

The necessary harmonic sums are elementary:
\[
H_o(t):=\sum_{\substack{q\le t\\q\text{ odd}}}\frac{\varphi(q)}{q^2}
=\frac4{\pi^2}\log t+O(1),\qquad
H_2(t)=\frac14H_o(t/2)=\frac1{\pi^2}\log t+O(1).
\tag{9}
\]
Indeed, `phi(n)/n=sum_(d|n) mu(d)/d` gives
\[
H_o(t)=\sum_{\substack{d\le t\\d\text{ odd}}}\frac{\mu(d)}{d^2}
 \sum_{\substack{m\le t/d\\m\text{ odd}}}\frac1m.
\]
The inner sum is `(log(t/d))/2+O(1)`, uniformly for `t/d>=1`.
Absolute convergence of the outer sums, including the `log d` weight,
and
\[
\sum_{d\ {m odd}}\frac{\mu(d)}{d^2}
=\prod_{p\ne2}(1-p^{-2})=\frac8{\pi^2}
\]
prove the first equality in (9); `phi(2m)=phi(m)` for odd `m` proves
the second. These are classical totient/Möbius identities, not a
cancellation estimate.

For all sufficiently large `Q`, take
\[
t=\left\lfloor\frac{\sqrt Q}{\log Q}\right\rfloor,
\qquad L=\left\lfloor\frac{Q}{16t}\right\rfloor.\tag{10}
\]
For each fixed `r`, `epsilon<=3/Q` eventually, so
`2tL epsilon<=3/8<1`. Also `2t<=L<Q/2`, `t/Q->0`, `eta->0`,
`beta->1/2`, and `log t/log Q->1/2`. Equations (8)–(9) yield
\[
\frac{Q^2 E_o(Q,t)}{\log Q}\to\frac4{\pi^2},\qquad
\frac{Q^2 E_2(Q,t)}{\log Q}\to\frac1{\pi^2}.
\tag{11}
\]
Thus (5) has limiting lower coefficient
`(1/4)(4/pi^2)+1/pi^2=2/pi^2`. Dividing (3) by two proves (1).
The classical gap-energy asymptotic
\[
S_0(Q)=\frac{12}{\pi^2}\frac{\log Q}{Q^2}+O(Q^{-2})\tag{12}
\]
then proves (2). No growing lag is substituted into a fixed-lag theorem.

## 3. A nonvanishing alternating gap sector

With unitary gap Fourier coefficients
`G_j=N^(-1/2) sum_k g_k exp(-2 pi i j k/N)`, Parseval gives exactly
\[
\sum_{j\ {m odd}}|G_j|^2=\frac{S_0-S_h}{2}.
\]
Consequently
\[
\liminf_{Q\to\infty}\frac{Q^2}{\log Q}
 \sum_{j\ {m odd}}|G_j|^2\ge\frac1{2\pi^2},\qquad
\liminf_{Q\to\infty}
 \frac{\sum_{j\ {m odd}}|G_j|^2}{\sum_j|G_j|^2}\ge\frac1{24}.
\tag{13}
\]
This rules out asymptotic concentration of the **full gap spectrum**
in even Fourier indices. The identical-copy control in the half-period
clue has exactly that concentration; its missing denominator cutoff and
adjacency hypotheses matter to (5).

One can retain some of (13) in a broad fixed band of the discrepancy
spectrum, without claiming the unresolved upper-half-band split.
[FD-346](FD-346-classical-gap-correlations-separate-high-band-farey-transport.md)
gives the weak gap-measure limit
`(6/pi^3)(1+cos theta) d theta`. For fixed `0<alpha<1`, its mass within angular distance
`pi alpha` of zero is
\[
L_\alpha=\frac{12}{\pi^3}(\pi\alpha+\sin(\pi\alpha)).
\]
Remove that entire mass, an upper bound on the removed odd-index mass.
Reflection kills the Nyquist coefficient and pairs the remaining
Fourier masses. The exact discrepancy dictionary is
`d_(2j)^2=|G_j|^2/[2 sin^2(pi j/N)]` for `0<j<N/2`, where `d_m`
are the orthonormal DST-I coefficients of `x_k-k/N`.
Since the multiplier is at least `1/2`, it follows that
\[
\liminf_{Q\to\infty}\frac{Q^2}{\log Q}
 \sum_{\substack{m/N\ge\alpha\\m\equiv2\ (4)}}d_m^2
\ge \frac1{8\pi^2}
 -\frac3{\pi^3}(\pi\alpha+\sin(\pi\alpha)).\tag{14}
\]
Restriction is legitimate because the limiting measure has no boundary
atoms. For example `alpha=1/100` makes the right side positive
(`0.0065863769...`). This is still at the small high-frequency energy
scale `log Q/Q^2`; it neither controls low-frequency Franel energy nor
settles the sector fraction in `[1/2,1]`.

## 4. Prior art, checks, and remaining boundary

The analytic inputs are François Dress, *Discrépance des suites de
Farey*, J. Théor. Nombres Bordeaux **11**(2) (1999), 345–367
([primary paper](https://www.numdam.org/article/JTNB_1999__11_2_345_0.pdf)),
for the absolute-discrepancy bound used in FD-348; and Anji Dong,
Huy Xuan Nguyen, Vi Anh Nguyen and Alexandru Zaharescu,
*Effective Estimates for a Class of Farey Fraction Sums and Bounds for
Mundici-Type Constants*, [arXiv:2606.12907v1](https://arxiv.org/html/2606.12907v1),
equation (2.2), for (12). FD-346 derives the weak measure used in (14)
from the classical fixed-lag correlations. Rational separation, the
totient harmonic sums, the shift-norm identity and Fourier sector
projection are classical. Searches by moving-lag Farey gap correlations,
half-translation and denominator parity did not supply (1); no general
novelty claim follows from that bounded search.

The local addition beyond FD-348 is the **summed size mismatch**:
its support restriction alone leaves a quadratic rank-resonance count,
whereas (5) converts two denominator classes into a positive fraction
of the logarithmic gap energy. This proves a genuine moving-lag bound
without estimating the number of rank coincidences. It does not prove
the joint-denominator count conjecture, its sublogarithmic variant,
`S_(h+r)=o(log Q/Q^2)`, or sector equipartition. Qualitative BCZ mixing
is not used, and no uniformity for offsets growing with `Q` is claimed.

An exact-rational scratch audit generated Farey grids for all
`3<=Q<=80` and for `Q=127,251,509,1021`. Across 925 admissible
`(Q,r,t,L)` panels with `-3<=r<=3`, it checked 3,182 local inequalities
(6)–(7), every resulting restricted-sum certificate (5), and the
finite energy bounds (8). A smaller panel checked 485 whole-norm
identities (3). Exact totient sums also checked the parity identity
in (9) through `t=10000`. A separate sorted-reduced-rational construction
for every `3<=Q<=31` checked the Fourier/DST identities, Nyquist
vanishing and 116 finite band inequalities underlying (14), with
maximum floating-point identity error below `5.6e-16`.
These checks test indexing, factors and finite algebra; the asymptotic
proof is (4)–(12), not extrapolation from the panel. No Lean verification
or independent adversarial approval is claimed.

The bound excludes near-perfect half-period alignment of the genuine
gap word. It remains compatible with a positive logarithmic correlation
coefficient, so the accepted decorrelation and denominator-count clues
remain open. There is no RH improvement.
