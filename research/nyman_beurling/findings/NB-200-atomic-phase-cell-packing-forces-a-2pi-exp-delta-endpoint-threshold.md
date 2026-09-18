# NB-200 — Atomic phase-cell packing forces a `2πe^Δ` endpoint threshold

**Date:** 2026-09-18  
**Status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + SOURCE-ACQUISITION + POSITIVE-EULER + ENDPOINT-GRANULARITY + NB-199-EXTENSION`.

`NB-199` pushes the positive Euler-shell return obstruction to the logarithmic Mellin layer, but its Brun--Titchmarsh gain vanishes when the favorable phase windows become physically bounded. At that point the source is still not continuous: it is supported on the integer lattice. Once every favorable component has length below one, each component can carry at most one von-Mangoldt atom. Combining that atomic capacity with the fixed positive source mass in a thin logarithmic slab yields a further endpoint obstruction that needs no short-interval prime theorem.

Keep the notation of `NB-199`:

\[
x_a=e^{r_0/a},\qquad X_a=\log x_a=\frac{r_0}{a},\qquad y_a=e^\Delta x_a,
\]

\[
D_a:=\sum_{x_a\le n<y_a}\Lambda(n)n^{-1-a},
\qquad
w_{n,a}:=\frac{\Lambda(n)n^{-1-a}}{D_a}\mathbf 1_{[x_a,y_a)}(n),
\]

and

\[
\mathcal A_a(t):=\sum_n w_{n,a}|e^{-it\log n}-1|.
\]

Then for every fixed

\[
0<K<2\pi e^\Delta
\tag{1}
\]

there exist constants `c_K>0` and `a_K>0`, depending on `r_0`, `Delta`, and `K`, such that for `0<a<a_K`,

\[
\boxed{
\inf_{X_a^2\le |t|\le Kx_a/X_a}\mathcal A_a(t)
\ge \frac{c_K}{X_a}.
}
\tag{2}
\]

Thus the order-`a` positive-return gap does not stop at an unspecified small multiple of `x_a/log x_a`. It persists through every fixed endpoint constant strictly below `2πe^Delta`. Equivalently, if `a_j->0`, `|t_j|>=X_{a_j}^2`, and

\[
X_{a_j}\mathcal A_{a_j}(t_j)\to0,
\qquad
\frac{|t_j|X_{a_j}}{x_{a_j}}=O(1),
\]

then necessarily

\[
\boxed{
\liminf_{j\to\infty}
\frac{|t_j|X_{a_j}}{x_{a_j}}
\ge 2\pi e^\Delta.
}
\tag{3}
\]

The constant in (3) is a **one-sided capacity threshold**, not an existence or sharpness theorem: this finding does not construct returns at or above `2πe^Delta x_a/X_a`.

## Derivation

### 1. Split off the corridor already controlled by `NB-199`

Let `U_0>1` and `c_0>0` be constants from `NB-199`, and put

\[
\kappa_0:=U_0^{-1}.
\]

For

\[
X_a^2\le |t|\le \kappa_0\frac{x_a}{X_a},
\]

`NB-199` gives

\[
\mathcal A_a(t)
\ge
c_0\frac{\log U_0}{X_a}.
\tag{4}
\]

It therefore remains only to control the endpoint strip

\[
\kappa_0\frac{x_a}{X_a}
\le |t|\le
K\frac{x_a}{X_a}.
\tag{5}
\]

Write

\[
\kappa:=\frac{|t|X_a}{x_a}\in[\kappa_0,K].
\tag{6}
\]

By symmetry take `t>0` below.

### 2. A fixed logarithmic top slab carries a fixed fraction of the source

Choose `h` with `0<h<Delta` so small that

\[
K<2\pi e^{\Delta-h}.
\tag{7}
\]

Consider the top logarithmic slab

\[
J_{a,h}:=[x_ae^{\Delta-h},x_ae^\Delta).
\tag{8}
\]

The prime number theorem and Stieltjes partial summation give, exactly as in the shell normalization already used in `NB-198`--`NB-199`,

\[
D_a
=
\int_{x_a}^{e^\Delta x_a}u^{-1-a}\,du+o(1)
=e^{-r_0}\Delta+o(1),
\tag{9}
\]

while

\[
\sum_{n\in J_{a,h}}\Lambda(n)n^{-1-a}
=
\int_{x_ae^{\Delta-h}}^{x_ae^\Delta}u^{-1-a}\,du+o(1)
=e^{-r_0}h+o(1).
\tag{10}
\]

Hence the normalized source mass in the slab satisfies

\[
\boxed{
\sum_{n\in J_{a,h}}w_{n,a}
=\frac{h}{\Delta}+o(1).
}
\tag{11}
\]

No short-interval asymptotic appears here: `h` is fixed, so (10) is a macroscopic multiplicative interval.

### 3. At endpoint height every sufficiently narrow favorable phase cell contains at most one integer

Fix a constant `q>0`, to be chosen below, and set

\[
\delta_a:=\frac q{X_a}.
\tag{12}
\]

Define the favorable phase set

\[
W_{t,a}
:=
\left\{
 u\in[x_a,y_a):
 \operatorname{dist}(t\log u,2\pi\mathbb Z)\le\delta_a
\right\}.
\tag{13}
\]

Its components are centered at

\[
u_m=e^{2\pi m/t}
\]

and have physical length

\[
H_m=2u_m\sinh(\delta_a/t).
\tag{14}
\]

In the endpoint strip (5),

\[
\frac{\delta_a}{t}
=
\frac{q}{\kappa x_a},
\]

so uniformly for components meeting the shell,

\[
H_m
\le
2e^\Delta x_a\sinh\!\left(\frac{q}{\kappa_0x_a}\right)
=
\frac{2e^\Delta q}{\kappa_0}+o(1).
\tag{15}
\]

Choose, for example,

\[
0<q<\frac{\kappa_0}{4e^\Delta}.
\tag{16}
\]

Then for all sufficiently small `a`, every favorable component has length strictly below one. Consequently **each component contains at most one integer**, hence at most one point of the von-Mangoldt source.

The logarithmic length of `J_(a,h)` is `h`. Therefore the number of favorable components intersecting that slab is at most

\[
N_{a,h}(t)
\le
\frac{th}{2\pi}+O(1).
\tag{17}
\]

This is the source of the endpoint constant `2π`: one phase cell is available per logarithmic period `2π/t`.

### 4. Atomic capacity leaves a positive fraction of the top slab outside the favorable cells

For every integer `n` in `J_(a,h)`, the elementary bound `Lambda(n)<=log n` gives

\[
w_{n,a}
\le
\frac{(X_a+\Delta)(x_ae^{\Delta-h})^{-1-a}}{D_a}
=
\left(1+o(1)\right)
\frac{X_a}{x_a\Delta}e^{-(\Delta-h)}.
\tag{18}
\]

Since each favorable component carries at most one integer, (17)--(18) imply

\[
\sum_{\substack{n\in J_{a,h}\\n\in W_{t,a}}}w_{n,a}
\le
\left(1+o(1)\right)
\frac{\kappa h}{2\pi\Delta}e^{-(\Delta-h)}.
\tag{19}
\]

Using `kappa<=K`, define

\[
\theta:=\frac{K}{2\pi e^{\Delta-h}}<1.
\tag{20}
\]

Then (11) and (19) show that, uniformly throughout (5),

\[
\sum_{\substack{n\in J_{a,h}\\n\notin W_{t,a}}}w_{n,a}
\ge
\frac{h}{\Delta}(1-\theta)+o(1).
\tag{21}
\]

After shrinking `a_K` if necessary, the right side is bounded below by the fixed positive constant

\[
m_K:=\frac{h}{2\Delta}(1-\theta)>0.
\tag{22}
\]

Thus the favorable phase cells simply do not have enough **atomic carrying capacity** to hold all of the positive source mass in the top logarithmic slab.

### 5. The missing mass produces an order-`1/X_a` chord gap

For `n` outside `W_(t,a)`,

\[
|e^{-it\log n}-1|
\ge
2\sin(\delta_a/2).
\tag{23}
\]

Since `delta_a=q/X_a->0`, for small `a`,

\[
2\sin(\delta_a/2)\ge \frac q{2X_a}.
\tag{24}
\]

Positivity of the weights and (22) therefore give

\[
\mathcal A_a(t)
\ge
m_K\frac q{2X_a}
\tag{25}
\]

uniformly in the endpoint strip (5). Combining (25) with the lower corridor (4) proves (2), with

\[
c_K:=\min\left\{c_0\log U_0,\frac{m_Kq}{2}\right\}>0.
\]

Finally, if (3) failed, some fixed `K<2πe^Delta` would contain infinitely many `t_j` with `X_(a_j) A_(a_j)(t_j)->0`, contradicting (2). This proves the one-sided endpoint threshold.

## Stress tests and limits

The threshold is **not** a statement that `2πe^Delta` is the first actual return constant. The proof only shows that a positive source with `o(1/X_a)` chord error cannot fit below that capacity. Arithmetic dephasing, prime gaps, or destination constraints may push the first possible return much farther out.

The integer lattice is load-bearing but primality at unit scale is not. Once the phase components have length below one, the proof uses only one atom per component and `Lambda(n)<=log n`; it does not require a theorem about primes in bounded intervals. Prime-number-theorem input enters only through the macroscopic slab mass (9)--(11). The same argument would apply to other positive lattice-supported sources with comparable atom sizes and logarithmic slab density.

Positivity remains essential. The conclusion uses actual source **mass** left outside the favorable cells. A signed or complex synthesis can place large positive and negative coefficients in different phase cells and cancel at the aggregate level; the atomic occupancy estimate does not control such a mechanism.

The lower cutoff `X_a^2` is inherited from the convenient high-ordinate formulation of `NB-199`, not presented as a natural barrier. Earlier positive-source findings already exclude sufficiently accurate returns much lower down. The new content is the constant-scale extension through the logarithmic endpoint layer.

The argument is an acquisition theorem, not a bound for the optimal Nyman--Beurling distance. It still does not prove that an approximant capable of resolving the destination must realize a positive Euler-shell return with `o(a)` accuracy. Establishing that destination bridge remains a separate requirement.

## Prior-art and representation boundary

The load-bearing external input is only the prime number theorem already anchored in `SOURCES.md`; `NB-199` supplies the lower part of the high-ordinate corridor. No new literature dependency is required.

The phase-cell packing step is elementary and should not be treated as a novelty claim in isolation. Classical large-value theory for Dirichlet polynomials and Bohr almost-periodicity are neighboring literatures for rare phase alignment, but this finding imports no theorem from them. The line-local derived content is the combination of the actual positive von-Mangoldt shell normalization with the transition to sub-unit physical phase cells, producing the explicit endpoint capacity constant in (2)--(3).

The representation audit is correspondingly narrow. `2π` comes from phase periodicity, while `e^Delta` comes from the physical size of the upper edge of the fixed log-width source shell. Changing the shell geometry changes the capacity constant. What survives representation changes is the mechanism: once favorable cells are shorter than the source lattice spacing, total capturable positive mass is bounded by `number of cells × maximal atom mass`.

## Consequence for the research frontier

`NB-199` identified `x_a/log x_a` as the point where the Brun--Titchmarsh logarithmic reserve disappears. `NB-200` shows that disappearance is not the end of positive coercivity: **lattice granularity takes over exactly when interval-density technology stops resolving the cells**. An `o(a)` positive return at endpoint scale must lie at or beyond

\[
(2\pi e^\Delta-o(1))\frac{x_a}{\log x_a}.
\]

The positive-source frontier is therefore no longer merely “inside the final logarithmic layer.” The remaining problem is to understand the region at and beyond this atomic-capacity threshold, where there are enough phase cells in principle but their occupation by the actual von-Mangoldt source is still arithmetically constrained. Independently, the signed/complex synthesis route remains outside this monotone-mass argument.