# MI-018 — Concentration of each cuff trace does not control their difference

**Evidence level:** supported by the scalar estimates and explicit
composite-label construction in
[PF-368](../../findings/PF-368-fixed-single-cuff-bands-concentrate-in-actual-windows-in-density.md)
and [PF-369](../../findings/PF-369-nearly-equal-cuff-lattices-hide-broad-band-residual-mass-beyond-actual-windows.md),
with the positive-shift cost of this explicit pair established in
[PF-370](../../findings/PF-370-positive-shift-trace-cost-dominates-the-two-cuff-escape-construction.md).
Prime realization and a uniform broad-band actual-energy comparison remain open.

Let `H[f]=int_R |f(t)|^2 sech(t)dt`. A trace on one exact period-`L`
Fourier lattice with fixed frequency span `W` satisfies

\[
\frac{H_{|t|>T}[f]}{H[f]}
\le\frac{4N^2}{\pi}e^{c(W)L-T},\qquad
c(W)=\frac4{\pi^2}\int_0^{\pi W/4}\log\coth u\,du<\frac12,
\quad N\le\lfloor WL/(2\pi)\rfloor+1.
\]

Thus `T/L->1/2` concentrates each fixed-band trace uniformly in its
coefficients. Two distinct periods can violate the corresponding bound
for their **difference**, even when they are exponentially close.

Fix `alpha>1/log(16)`, `n=ceil(alpha L)`, and
`L'=L+delta_L`, where `0<|delta_L|=o(L^2 e^(-L/2))`. PF-369 supplies
exact-lattice traces `f_L,f_(L')`, each on indices `n,...,3n`, whose
difference `g_L` obeys

\[
\frac{\int_{-L/2}^{L/2}|g_L(t)|^2\operatorname{sech}t\,dt}{H[g_L]}
\le C_\alpha\left(\frac{e^L}{n^2 16^n}
+\frac{\delta_L^2e^L}{L^4}\right)\longrightarrow0.
\]

The mechanism retains the small denominator. Set
`q(t)=cos^(2n)(pi t/L)` and take the Fourier partial sum `P_n` of the
periodic extension of `tq(t)` on `[-L/2,L/2]`. The exact discarded tail
gives `||tq-P_n||_infinity<=L/(2pi n4^n)` there. Modulate:
`Q=e^(4pi int/L)q=sum_(j=n)^(3n)c_j e^(2pi ijt/L)`,
`c_j=4^(-n) binom(2n,j-n)`, and `A=e^(4pi int/L)P_n`.
Then `R=tQ-A` is tiny centrally, but `R(L+s)=LQ(s)+R(s)` is of size `L`
for `|s|<=1`.

With `d_j=2pi j(1/L'-1/L)`, replace `tQ` by genuine divided differences:

\[
g_L(t)=\sum_{j=n}^{3n}\frac{c_j}{id_j}
\left(e^{2\pi ijt/L'}-e^{2\pi ijt/L}\right)-A(t),\qquad
|g_L-R|\le C_\alpha |\delta_L|t^2/L.
\]

The escaping-mass lower bound is `H[g_L]>=cL^2 e^(-L)`, so the error must
be compared with that scale; fixed-`L` divided-difference convergence would
not suffice. In this normalization individual coefficient absolute sums
can grow as `L/|delta_L|`. Scaling both traces leaves the mass ratio and
their relative energy costs unchanged. At `delta_L=0` this construction is unavailable and the
two lattices collapse to one: uniformity is singular at equal periods.

The exact cotangent flute from composite labels `6m+3`, `m>=1`, has
neighboring cuff periods satisfying
`delta_L=(8+o(1))e^(-L/2)>0`. Its prescribed corridor window has
`L/2-T=1+log(2/vartheta)+o(1)>0`, for the fixed small geometric
`vartheta>0`. With `alpha=1/2`, the central fraction is `O(L^(-4))`.
Each trace concentrates in this actual window while their difference
escapes it. A real or imaginary component gives the same obstruction
with real zero-mean traces.

Separate concentration estimates bound residual tails by
`H[f_L]+H[f_(L')]`, which may dwarf `H[f_(L')-f_L]`. They cannot supply
a broad-band scalar window/full-norm comparison from period agreement
and cotangent geometry alone. But this loss does not make the explicit
pair an inexpensive escape from actual energy.

Let `E_pant` minimize `int (|du|_g^2+|u|^2) dvol_g` with both traces
fixed. In [PF-363](../../findings/PF-363-trace-preserving-corridor-charts-give-a-coupled-pant-energy-lower-bound.md)'s
embedded trace-preserving chart, assume
`rho_1+rho_2<=eta_0 s`, fixed `eta_0<1`, and
`s=(h+h')/2~4e^(-L/2)`, where `h=4 artanh(e^(-L/2))` and similarly
for `h'`. At each inherited coordinate `t`, put `w=s cosh t`. The
transverse-plus-mass interval minimum with endpoints `a,b` is

\[
\frac12\tanh(w/2)|a+b|^2+
\frac12\coth(w/2)|a-b|^2.
\]

Thus the full energy pays for the common amplitude even where the
difference cancels. The uniform chart comparison gives, for arbitrary
finite-energy traces,

\[
E_{\rm pant}[f_L,f_{L'}]\ge c_*\int_{-T}^{T}
\tanh(s\cosh t/2)(|f_L(t)|^2+|f_{L'}(t)|^2)\,dt.
\]

For the specified divided-difference pair, all `d_j` have the same sign.
The positive exponential coefficients therefore give
`|f_(L')|\gtrsim L/|delta_L|` on a fixed central interval. PF-370 also
bounds the full residual by `H[g_L]<=C L^2 e^(-L/2)`. Consequently

\[
E_{\rm pant}\ge c\,sL^2/\delta_L^2,\qquad
\frac{s^{-1}H[g_L]}{E_{\rm pant}}
\le C\delta_L^2e^{L/2}
=o(L^4e^{-L/2})\longrightarrow0.
\]

The constants depend on fixed `alpha` and chart bounds, not on `L,delta_L`.
For the composite realization this ratio is `O(e^(-L/2))`. The same
conclusion holds for each real component; at least one retains scalar
escape. Common rescaling cannot change the ratio, and adding nonnegative
seam energy with the traces fixed only decreases it. Even a prime
realization of these periods would therefore not turn this pair into a
counterexample to an actual-energy lower certificate.

The positive shift is essential to this argument: removing the mass term
leaves the interval minimum `|a-b|^2/w`, with no common-amplitude penalty.
The estimate for this pair does not prove
`E_pant>=c s^(-1)H[f_(L')-f_L]` uniformly over arbitrary fixed-band traces,
identify global transition minimizers, or give a completed-angle,
compactness or RH conclusion. The sufficiently narrow combined-band
result remains compatible with both the scalar escape and its energy cost.
