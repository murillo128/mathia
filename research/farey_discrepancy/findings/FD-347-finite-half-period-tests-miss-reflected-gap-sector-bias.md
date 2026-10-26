# FD-347 — Finite half-period tests miss reflected gap-sector bias

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + MATCHED-CONTROL-OBSTRUCTION.

For every fixed integer `R>=0`, there are increasing reflection-symmetric
rational grids that retain the genuine Farey normalized gap inventory
(with doubled multiplicities), all the leading fixed-lag correlation
limits used in FD-346, and its entire coarse high-band spectral limit,
while satisfying
\[
\widetilde S_{M/2+r}(Q)=O_R(Q^{-2})\qquad(|r|\le R).
\tag{1}
\]
Nevertheless, their upper-band sine energy has a limiting fraction on
indices divisible by four different from one half. Thus a fixed finite
window of half-period estimates, even at the stronger scale (1), cannot
certify sector equipartition from these retained data alone.

These are artificial grids, with `M=2N_Q` gaps. They do not retain a
Farey denominator cutoff or the labeled adjacency relations. The result
does **not** refute the genuine-source decorrelation conjecture in the
[half-period clue](../clues/CLUE-half-period-gap-decorrelation.md).
Its contribution beyond the clue's identical-copy control is that the
control now **passes any prescribed finite window of the proposed
decorrelation test**, yet still fails sector equipartition.

## 1. Reflected rotation of the genuine gap population

For genuine Farey order `Q>=3`, write `N=N_Q=sum_(q<=Q) phi(q)` and use
the periodic gaps `g_k=x_(k+1)-x_k`, with indices modulo `N`. They satisfy
\[
g_{N-1-k}=g_k,\qquad \sum_{k=0}^{N-1}g_k=1,\qquad
0<g_k\le Q^{-1}.
\tag{2}
\]
Fix an integer `t>=1`, independent of `Q`. Set `M=2N` and define
\[
\widetilde g_k=\tfrac12g_{k+t},\qquad
\widetilde g_{N+k}=\tfrac12g_{k-t}\quad(0\le k<N).
\tag{3}
\]
By (2), the second half is the reversal of the first. The cumulative
grid `z_0=0`, `z_k=sum_(i<k) tilde g_i` is rational, strictly increasing,
has `z_M=1`, `z_N=1/2`, and obeys `z_(M-k)=1-z_k`.
The multiset of `M tilde g_k` is exactly two copies of that of `N g_k`.

The doubled size has natural normalization
\[
W_Q=\frac{2Q^2}{\log Q}.
\tag{4}
\]
Equivalently, its effective scale is `sqrt(2) Q`: its rank count has the
same asymptotic size as at that scale, and (4) differs from
`(sqrt(2)Q)^2/log(sqrt(2)Q)` by a factor tending to one. This is a
normalization convention, not a second integer Farey order.

## 2. Ordinary and half-period correlations

Put `S_r=sum_k g_k g_(k+r)` and
`tilde S_r=sum_(k=0)^(M-1) tilde g_k tilde g_(k+r)`. For every fixed
integer `r`, comparison with the separately periodic halves gives
\[
\begin{split}
\widetilde S_r&=\tfrac12S_r+O_{|r|}(Q^{-2}),\\
\widetilde S_{N+r}
&=\tfrac14\bigl(S_{r-2t}+S_{r+2t}\bigr)+O_{|r|}(Q^{-2}).
\end{split}\tag{5}
\]
For `|r|<N`, each error in (5) has absolute value at most
`|r|/(2Q^2)`. Indeed, at most `2|r|` products cross a seam instead of the
corresponding periodic half; both possible products lie in
`[0,1/(4Q^2)]`. The second identity compares the two rotations with
relative shifts `r-2t` and `r+2t`. At `r=0` it is exact:
\[
\widetilde S_N=\tfrac12S_{2t}.
\tag{6}
\]

The classical input, with lag fixed before the limit, is
\[
\frac{Q^2S_r}{\log Q}\longrightarrow c_r,\qquad
c_0=\frac{12}{\pi^2},\quad c_{\pm1}=\frac6{\pi^2},\quad
c_r=0\ (|r|\ge2),
\tag{7}
\]
with the stronger `S_r=O_r(Q^-2)` for every fixed `|r|>=2`.
These are exactly the arithmetic inputs of
[FD-346](FD-346-classical-gap-correlations-separate-high-band-farey-transport.md),
checked in the primary formulation of Dong–Nguyen–Nguyen–Zaharescu,
[equation (2.2) and Theorem 2.3](https://arxiv.org/html/2606.12907v1).
No growing lag is inserted into that theorem.

Choose `t=ceil((R+2)/2)`, so `2t>=R+2`. Then `|r+/-2t|>=2` for
`|r|<=R`, so (5) proves (1). Meanwhile, for every fixed integer `r`,
(5) and (7) give
\[
W_Q\widetilde S_r\to c_r,\qquad
W_Q\widetilde S_{N+r}\to\tfrac12(c_{r-2t}+c_{r+2t}).
\tag{8}
\]
The full half-period correlation sequence does not vanish: its limit at
`r=2t` is `6/pi^2`. The hidden correlation has been moved outside the
prescribed finite test window, not eliminated.

## 3. Exact limiting sector densities

For the unitary transform of the new gaps, define
\[
\widetilde G_j=M^{-1/2}\sum_{k=0}^{M-1}\widetilde g_k
 e^{-2\pi ijk/M},\qquad \theta_j=2\pi j/M,
\]
\[
\mu_Q=W_Q\sum_j|\widetilde G_j|^2\delta_{\theta_j},\qquad
\nu_Q=W_Q\sum_j(-1)^j|\widetilde G_j|^2\delta_{\theta_j}.
\tag{9}
\]
Their `r`th Fourier moments are respectively the two quantities on the
left of (8). The masses of `mu_Q` are bounded, and `|nu_Q|=mu_Q`.
Trigonometric-polynomial approximation therefore proves
\[
\mu_Q\Rightarrow\mu,\qquad
\nu_Q\Rightarrow\cos(2t\theta)\mu,\qquad
d\mu(\theta)=\frac6{\pi^3}(1+\cos\theta)\,d\theta.
\tag{10}
\]
In particular the even- and odd-`j` positive measures converge to
`cos^2(t theta) mu` and `sin^2(t theta) mu`.

Let `tilde D_k=z_k-k/M`, and use orthonormal DST-I coefficients
\[
\widetilde d_m=\sqrt{2/M}\sum_{k=1}^{M-1}\widetilde D_k
 \sin(\pi mk/M),\qquad 1\le m<M.
\]
Let `tilde F_j` be the unitary periodic Fourier transform of `tilde D`.
Reflection kills odd `m`. Discrete integration and the periodic/DST
dictionary give `|tilde F_j|^2=|tilde G_j|^2/[4 sin^2(theta_j/2)]`
for `j!=0` and `tilde d_(2j)^2=2|tilde F_j|^2` for `0<j<M/2`.
On every fixed band `alpha<=m/M<1`, `0<alpha<1`, the multiplier is
bounded. All limiting boundaries are atom-free. Consequently
\[
\begin{split}
W_Q\!\sum_{\substack{m/M\ge\alpha\\m\equiv0\ (4)}}
 \widetilde d_m^2\delta_{m/M}
&\Rightarrow \frac6{\pi^2}\cos^2(t\pi x)\cot^2(\pi x/2)\,dx,\\
W_Q\!\sum_{\substack{m/M\ge\alpha\\m\equiv2\ (4)}}
 \widetilde d_m^2\delta_{m/M}
&\Rightarrow \frac6{\pi^2}\sin^2(t\pi x)\cot^2(\pi x/2)\,dx,
\end{split}\tag{11}
\]
on `[alpha,1]`. Their sum is the same coarse spectral limit as FD-346.
Thus preserving that limit does not merely leave an abstract moment
ambiguity: positive reflected rational grids realize the different
sector densities in (11).

## 4. Every fixed rotation produces a nonzero upper-band bias

Set `I=integral_(1/2)^1 cot^2(pi x/2) dx=2/pi-1/2>0`. The limiting
fraction of upper-band energy on `4|m` is
\[
P_t=\frac12+\frac{B_t}{2I},\qquad
B_t=\int_{1/2}^1\cot^2(\pi x/2)\cos(2t\pi x)\,dx.
\tag{12}
\]
It is not one half for any positive integer `t`. To see this without a
numerical sign test, put `f(u)=cot^2(pi/4+pi u/2)` on `[0,1/2]`.
Then `f'(1/2)=0` and
\[
f''(u)=\frac{\pi^2}{2}\left[
\csc^4(\pi/4+\pi u/2)
+2\cot^2(\pi/4+\pi u/2)\csc^2(\pi/4+\pi u/2)\right]>0.
\]
Twice integrating by parts, using the vanishing endpoint sines, yields
\[
(-1)^t B_t
=\frac1{(2t\pi)^2}\int_0^{1/2}f''(u)
 [1-\cos(2t\pi u)]\,du>0.
\tag{13}
\]
The two integrals in (11) over the upper band are positive, so their
conditional laws and the fraction (12) are defined for all sufficiently
large `Q`.

For `t=1`, the exact evaluation `B_1=6/pi-2` gives
\[
P_1=\frac12+\frac{6/\pi-2}{2(2/\pi-1/2)}
=0.1701038168\ldots.
\tag{14}
\]
This control already has `tilde S_(M/2)=O(Q^-2)`, yet only about 17% of
its upper-band energy lies on `4|m`. Larger fixed `t` hide the failure
from any chosen finite offset window. The bias depends on that window;
no lower bound uniform as `R->infinity` is asserted.

## 5. Prior art, audit, and consequence

The Farey gap-correlation input is classical Hall/Boca–Cobeli–Zaharescu
theory, with the explicit formulation cited above. Fourier correlation,
shift modulation, finite-moment nonuniqueness and weak convergence via
trigonometric polynomials are classical. Searches by Farey gap/rank
correlations, half-period lags, shifted gap spectra and truncated
trigonometric moments did not identify this particular positive-grid
certificate; that is not a claim of general novelty. No new arithmetic
estimate is used or proved.

Unlike FD-313's local-block controls for full cumulative energy, this
construction retains the actual Farey gap population up to scaling and
duplication, matches the entire classical high-band profile, and passes
specified **macroscopic-lag** tests. Unlike identical replication, it
passes those tests while leaving a quantitatively explicit sector bias.
The new conclusion is restricted to the insufficiency of that finite
testing mechanism in the stated control class.

A standard-library scratch audit generated exact Farey gaps for every
`3<=Q<=25` and `t=1,2,3,4`. It checked reflection, the midpoint, the
normalized multiset, (6), and 1,256 rational seam/correlation inequalities
from (5). Independent direct DFT and DST sums at `Q=7,11,19,31`,
`t=1,2,4`, checked the signed-correlation and inverse-difference
dictionaries with maximum absolute error below `1.5e-14`.
Numerical quadrature checked (14) and the signs in (13) for `1<=t<=8`.
These are finite identity and normalization audits; the limit proof is
(5)–(13), not an extrapolation of computed spectra. No Lean or independent
adversarial verification is claimed.

For the genuine Farey source, the all-fixed-offset conjecture remains
open. A proof for every fixed offset, or a sufficient band-weighted
estimate, still gives equipartition as explained in the clue. A theorem
using additional denominator/adjacency arithmetic could also make a
finite test sufficient; this control does not retain that information.
There is no conclusion about low-frequency Franel energy, an RH bound,
or the full total-variation limit for the original reassembly.
