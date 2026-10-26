# PF-367 — exact cuff-lattice packets obstruct broad-band corridor comparison

**Status:** EXACT-DERIVED + CLASSICAL-BINOMIAL-AND-LAPLACE-METHOD + WINDOW-COMPARISON-OBSTRUCTION.

The small-band condition in PF-361 cannot be removed merely by requiring the
frequencies to lie on an exact cuff Fourier lattice. A binomial packet in a
physical frequency interval of width `W` has its `sech`-weighted mass concentrated
at distance

\[
r_W L,\qquad r_W=\frac{\arctan W}{\pi},
\tag{1}
\]

from the coordinate origin, where `L` is the cuff period. If a symmetric corridor
window has half-length `T=theta L+O(1)` with `0<theta<r_W`, the fraction of mass
inside that window tends to zero exponentially. The packet exists on every
sufficiently large real period, uses consecutive exact Fourier modes, and has
coefficient absolute sum one. No free coalescing-frequency choice is used.

This gives a quantitative obstruction to extending the **uniform window/full
scalar-norm comparison** used in PF-363--PF-366. It does not refute their narrow
band results, prove that actual maximal prime corridors have short enough
windows to realize the obstruction, or determine a wide-band shorted angle.
For the actual embedded window, Section 4 derives a necessary power-sized
neighboring gap jump and an exceptional-count bound. That window captures
asymptotically all of this fixed-width packet's mass in prime-index density;
unbounded consecutive-gap ratios alone do not realize its escape regime.

## 1. An exact lattice packet and its mass ratio

Fix `W>0`. For `L` tending to infinity, choose any positive integers

\[
n_L=\frac{WL}{2\pi}+O(1)
\]

and any integers `k_L`. Define the `L`-periodic complex trigonometric polynomial

\[
p_L(t)=2^{-n_L}e^{2\pi i k_Lt/L}
              (e^{2\pi it/L}-1)^{n_L}.
\tag{2}
\]

Its frequencies are exactly `2pi(k_L+j)/L`, `0<=j<=n_L`, and

\[
|p_L(t)|^2=|\sin(\pi t/L)|^{2n_L},\qquad
\sum_{j=0}^{n_L}2^{-n_L}\binom{n_L}{j}=1.
\tag{3}
\]

To place the packet in any fixed open interval `(a,a+W)`, take
`k_L=floor(aL/(2pi))+1` and `n_L=floor(WL/(2pi))-2` on a sufficiently far tail.
Both endpoints then lie strictly inside the interval. In particular the packet
can lie wholly in a positive transition band; it need not contain a constant.

Write

\[
H[p]=\int_{\mathbb R}|p(t)|^2\operatorname{sech}t\,dt,\qquad
\mathcal R_L(T)=\frac{\int_{-T}^{T}|p_L(t)|^2\operatorname{sech}t\,dt}{H[p_L]},
\]
\[
\Phi_W(x)=\frac W\pi\log|\sin(\pi x)|-|x|.
\tag{4}
\]

For `0<theta<r_W` and `T_L=theta L+O(1)`,

\[
\boxed{\quad\lim_{L\to\infty}\frac1L\log\mathcal R_L(T_L)
       =-I_W(\theta)<0,\quad}
\tag{5}
\]
\[
I_W(\theta)=\Phi_W(r_W)-\Phi_W(\theta)
=\theta-r_W+\frac W\pi
  \log\frac{W}{\sqrt{1+W^2}\sin(\pi\theta)}.
\tag{6}
\]

The same family provides a control on the other side: if
`r_W<theta<1/2`, then `R_L(T_L)->1` and

\[
\lim_{L\to\infty}\frac1L\log(1-\mathcal R_L(T_L))
       =\Phi_W(\theta)-\Phi_W(r_W)<0.
\tag{7}
\]

At `T_L=r_W L+O(1)`, the fraction tends to `1/2`. These are thresholds for
this explicit packet, not an optimal concentration theorem over the whole band.

## 2. Derivation, including all periods

The bounds

\[
e^{-|t|}\le\operatorname{sech}t\le2e^{-|t|}
\tag{8}
\]

reduce the exponential rates to integrals with the exponential weight. Set
`W_L=2pi n_L/L=W+O(1/L)` and rescale `t=Lx`. On `0<x<1`, the resulting
integrand is exactly

\[
\exp\{L\Phi_{W_L}(x)\}.
\tag{9}
\]

The sine factor is periodic in absolute value. For the exponential weight,
the integral on `[jL,(j+1)L]` is `exp(-jL)` times the integral on `[0,L]`.
Thus the positive half-line contributes a geometric factor
`1/(1-exp(-L))`; reflection handles the negative half-line. Bounds (8) show
that these reductions preserve logarithmic rates for the original norm.

On `(0,1)`,

\[
\Phi_W'(x)=W\cot(\pi x)-1,\qquad
\Phi_W''(x)=-\pi W\csc^2(\pi x)<0.
\tag{10}
\]

The unique maximum is `r_W` from (1). The function tends to minus infinity
at both endpoints. Upper bounds by its supremum and lower bounds on a fixed
neighborhood of the maximum give

\[
\lim_{L\to\infty}L^{-1}\log H[p_L]=\Phi_W(r_W).
\tag{11}
\]

This elementary Laplace argument remains valid with `W_L` in (9): convergence
is uniform on compact subintervals, and `W_L>=W/2` eventually controls the
logarithmic singularities uniformly near the endpoints. The outside factor
`L` has zero logarithmic rate.

When `theta<r_W`, the maximum on `[0,theta]` is the endpoint `theta`.
The same upper/lower argument gives numerator rate `Phi_W(theta)` and proves
(5). An `O(1)` change of `T_L` changes the rescaled endpoint by `O(1/L)` and
does not affect that rate.

When `r_W<theta<1/2`, the maximum on `[theta,1]` is again `theta`.
Later periods have maximal rate at most `Phi_W(r_W)-1`. Since
`Phi_W(theta)>Phi_W(1/2)=-1/2` and `Phi_W(r_W)<=0`, later periods are
strictly smaller. This proves (7).

For the equality case, the actual maximizer is `r_(W_L)=r_W+O(1/L)`.
The second derivative in (10) is negative and nonzero there. Expansion on
the scale `x-r_(W_L)=y/sqrt(L)` gives a centered Gaussian profile, with
exponentially negligible mass outside any fixed neighborhood. The cutoff
is `O(1/sqrt(L))` from the maximum in this scaled variable, so it captures
half the mass of each of the two reflected peaks. Near those peaks,
`sech(Lx)/(2 exp(-L|x|))->1` uniformly. This proves the stated `1/2` limit.
It is not asserted for arbitrary `T_L/L->r_W` without control of the smaller
cutoff displacement.

## 3. Real seam traces and the exact failure of the comparison

Write `p_L=u_L+i v_L`. Both `H` and the window integral split into the sums
for these two real trigonometric polynomials. Their complex mass ratio is
therefore a weighted average of the real ratios. At least one nonzero choice
`f_L in {u_L,v_L}` satisfies

\[
\frac{H_{[-T_L,T_L]}[f_L]}{H[f_L]}
          \le\mathcal R_L(T_L).
\tag{12}
\]

For `a>0` in Section 1, these real traces use only sines and cosines with
positive physical frequencies in `(a,a+W)` and have zero cuff mean. Placing
`f_L` on one end of an edge and zero on the other makes it an allowed edge
difference regardless of the neighboring cuff period. Thus unequal or
rationally independent neighboring lattices cannot invalidate this control.

For any `0<theta<1/2`, whenever

\[
\boxed{W>\tan(\pi\theta),}
\tag{13}
\]

there is no constant `c>0`, independent of `L`, such that
`H_[-T_L,T_L][f]>=c H[f]` for every trace in that physical band. This is
an exact-lattice counterexample to a **uniform** comparison, not just poor
conditioning observed in a numerical Gram matrix.

More generally, a uniform positive comparison along a sequence of periods
and windows requires

\[
\liminf T_L/L\ge r_W;
\tag{14}
\]

otherwise use a subsequence whose ratios are bounded above by a fixed
`theta<r_W` and apply monotonicity in window size. Condition (14) is only
necessary. Neither its converse nor optimality of the packet is claimed.

## 4. Consequence and exact prime-flute boundary

PF-361/PF-363 certify an embedded edge window satisfying
`T_i>=b_0 max(L_i,L_(i+1))-C`, with `b_0=19/80`. In particular a shorter
window of half-length `b_0 L_i-C` is available for the trace on cuff `i`.
For this conservative choice, (13) becomes

\[
W>\tan(19\pi/80)\simeq0.92439049.
\tag{15}
\]

The comparison fails on these subwindows along the **actual** prime-cuff
periods, since the proof needs only `L_i->infinity` and uses their exact
Fourier spacing. A full eliminated low interval `[-lambda,lambda]` also
contains such a packet whenever `2lambda>tan(19pi/80)`: choose an interior
width between these two quantities. Realification preserves that symmetric
low interval.

Consequently exact lattice membership and the conservative lower window
bound alone do not extend the full-line Cauchy lower-certificate method to
arbitrary broad bands. One must use larger available corridors, a stronger
concentration estimate with its valid width/window relation, information
special to the actual minimizing residuals, or other positive energy terms.
PF-361's arbitrarily coalescing example had not settled this exact-lattice,
linearly growing-window regime.

The maximal embedded window can be larger than the subwindow just used.
For that window, the obstruction applies if an actual subsequence satisfies
`limsup T_i/L_i<r_W`; no such prime-gap subsequence is established here.
In particular the lower bound `T_i/L_i>=b_0-o(1)` is not an upper bound and
cannot be used to claim failure on every full corridor.

### Actual-window escape needs a power-sized neighboring gap

Use the full **prescribed embedded window** of PF-363, not an assertion about
the maximal possible embedded domain. Fix its sufficiently small geometric
constant `0<vartheta<1` and put

\[
P=p_{i-1},\quad a=p_i-p_{i-1},\quad b=p_{i+1}-p_i,
\qquad
T_i=\operatorname{arsinh}\frac{\vartheta}{\sinh s_i}-1,
\quad s_i=(h_i+h_{i+1})/2.
\tag{16}
\]

Here `a=g_(i-1)` and `b=g_i` in the README's indexing. PF-001's exact law is
`L_i=2 log coth(h_i/4)`. The uniform small-gap input from Baker--Harman--Pintz
(S6) and `F(x)=log cot(pi/x)=log(x/pi)+O(x^-2)` give

\[
h_i=\frac aP(1+o(1)),\qquad
h_{i+1}=\frac bP(1+o(1)),
\]
\[
L_i=2\log\frac{4P}{a}+o(1),\qquad
T_i=\log\frac{4\vartheta P}{a+b}-1+o(1),
\]
\[
\boxed{\frac{L_i}{2}-T_i
 =\log(1+b/a)-\log\vartheta+1+o(1).}
\tag{17}
\]

All errors tend to zero uniformly on the prime tail, including unbounded
`b/a`. For example `F'(x)=x^-1+O(x^-3)` gives each relative mesh error
`O((a+b)/P+P^-2)` by integration. The hyperbolic expansions add
`O(h_i^2+s_i^2)`. This is the same boundary-location mechanism as PF-324,
now compared with the entire cuff period rather than a fixed recentered
window. In particular `T_i<L_i/2` eventually.

For every fixed `0<theta<1/2`, there is `c_theta>0` such that, sufficiently
far out,

\[
\boxed{T_i\le\theta L_i
\quad\Longrightarrow\quad
b\ge c_\theta P^{1-2\theta}a^{2\theta}.}
\tag{18}
\]

The constants can depend on the fixed geometric choice `vartheta`.
Indeed the second line of (17) first gives the displayed lower bound for
`a+b`. Its ratio to `a` tends to infinity, since it is bounded below by a
positive constant times `(P/a)^(1-2theta)`. Thus `b` is eventually at least
half of this bound. For the packet's fixed-margin escape regime take
`theta<r_W`; the necessary jump has positive power `1-2theta` in `P`,
even when the preceding gap is bounded.

There is also an unconditional count. The gaps `b` indexed by a dyadic
block `X<=P<2X` occupy disjoint consecutive-prime intervals. They lie in
an interval of length `O(X)` and have total `O(X)`; the possible endpoint
overshoot is `O(X^(21/40))`. Since `a>=2`, (18) implies

\[
\boxed{\#\{i:X\le p_{i-1}<2X,\ T_i\le\theta L_i\}
       =O_\theta(X^{2\theta}).}
\tag{19}
\]

This is just a telescoping gap sum followed by the threshold bound, not a
new prime-distribution theorem. Summing dyadic blocks gives the same order
up to `P<=X`. The prime number theorem then makes the fraction among those
prime indices `O_theta(X^(2theta-1) log X)`, which tends to zero. Consequently
`T_i/L_i` converges to `1/2` in prime-index density: for every fixed positive
epsilon, the proportion with `|T_i/L_i-1/2|>epsilon` tends to zero.

For each **fixed finite** `W`, choose `r_W<theta<1/2`. Outside the exceptional
set in (19), monotonicity of the window integral and (7) give

\[
\mathcal R_{L_i}(T_i)\ge\mathcal R_{L_i}(\theta L_i)\longrightarrow1.
\tag{20}
\]

The limit is uniform on the remaining tail because `L_i->infinity`, and
modulation does not affect this complex packet's modulus. Thus its actual
window mass ratio tends to one **in density**, not necessarily on every
subsequence. Any larger available window only increases that ratio. Equation
(20) is about the explicit packet (2), not a uniform estimate over all
trigonometric polynomials, either real component separately, or minimizing
Schur residuals. No conclusion is asserted for a width growing with `i`.

Pintz's unbounded consecutive-gap-ratio theorem used in PF-324 does not
supply this power-scale jump on an infinite prime subsequence. Its quantitative
lower bound is of Erdős--Rankin logarithmic scale; a lower bound of that size is not a
positive power of `P`. Nor does it bound the constructed gaps from above
at that scale. There is no conflict: an unbounded absolute seam distance
in (17) can still be `o(L_i)`.

Two nonprime endpoint controls check the distinction without assuming a
conjectural prime pattern. Take `P=6m+3` as `m->infinity` and
use the endpoint triple `P,P+a,P+a+b`, with `a=6`. If
`b=6 ceil((log P)^2)`, all labels are composite and `b/a->infinity`, but
`T_i/L_i->1/2`; the packet stays inside the window. If instead
`b=6 ceil(P^(2/5)/6)`, the same exact cotangent and cuff construction gives
`T_i/L_i->3/10`. For `W=2`, this is below `r_W`, so (5), or monotonicity with
a fixed intermediate cutoff, gives exponentially vanishing window mass.
Both controls have `a,b=o(P)` and even satisfy a bound with exponent `21/40`.
They validate the scale distinction; neither is a prime realization theorem.

The exceptional count can still permit infinitely many escaping modules.
It does not imply compactness or any Schatten estimate: an operator may
retain nondecaying singular values on a zero-density subsequence. The
existence of actual prime pairs meeting the required power-scale jump,
and their behavior after full energy normalization, remain unproved here.

Nor does a failure of the uniform scalar comparison prove failure of an
optimized residual lower bound. These packets are arbitrary band fields,
not proved to be the transition minimizers for a retained low trace. The
actual pant retains tangential, mass and exterior energy, and its upper trial
contains a nonsingular coefficient cost. Those terms have not been compared
to this exponentially small `H[p_L]`. No actual shorted-angle, compactness,
relative-resolvent, scattering or RH conclusion follows.

## 5. Prior art, checks and novelty boundary

The polynomial `(z-1)^n`, modulation and binomial expansion are classical.
The concentration calculation is an elementary application of Laplace's
method; see the authoritative [NIST DLMF, Section 2.3(iii)](https://dlmf.nist.gov/2.3#iii).
Equations (8)--(11) give the logarithmic argument directly, including the
unbounded domain and the varying integer order.

The closest general concentration input remains Friedland--Yomdin,
*An observation on the Turán--Nazarov inequality*, Studia Math. 218 (2013),
27--39, [Theorem 1.1](https://www.impan.pl/shop/publication/transaction/download/product/89801)
(S34). Its dependence on term count is consistent with this obstruction.
Gaillac--Gautier's [weighted truncated-Fourier manuscript](https://publications.ut-capitole.fr/id/eprint/32479/1/wp_tse_1013.pdf),
Proposition 1 and Section 3, studies the `sech` kernel and spectral bounds
using related concentration methods. Neither theorem is needed for the
explicit packet calculation.

The audit covered exponential-polynomial concentration, weighted
trigonometric Remez inequalities and weighted Fourier restriction. No new
general uncertainty principle, extremal polynomial or asymptotic method is
claimed. The derived addition is the exact-cuff-lattice control, its explicit
width/window obstruction and the separation between a certified subwindow
and the full geometric window, including the arithmetic restriction (18)
and count (19). Absence of identical wording in a search is not novelty evidence.

For (17)--(20), the external inputs are the already-used sublinear gap
bound of Baker--Harman--Pintz, *The Difference Between Consecutive Primes,
II*, Proc. London Math. Soc. 83 (2001), 532--562,
[publisher record](https://doi.org/10.1112/plms/83.3.532), and the classical
prime number theorem as stated in [NIST DLMF 27.2.3](https://dlmf.nist.gov/27.2#E3).
Only the latter converts the elementary absolute exceptional count into
a proportion of prime indices. Pintz's [primary paper](https://arxiv.org/pdf/1406.2658),
Theorems 1, 1' and 2, equations (3.2)--(3.3), supplies the precise logarithmic
ratio guarantee compared with (18). Its theorem is used to audit the
proposed arithmetic bridge, not to assert existence or nonexistence of
power-sized prime gaps. Neither these classical sources nor (19) resolve
the exceptional prime subsequences needed by a full-window counterexample.

Supplementary standard-library checks verified the exact binomial absolute
mass and vanishing moments of orders below `n` for `n=1,...,64`. Scaled
Simpson quadrature checked 36 cases with `W in {1/2,1,2}`,
`L in {128,256,512,1024}`, and `theta=r_W-0.04,r_W,r_W+0.04`, using 16,384
panels on each side of the cutoff within the first positive period. Later
periods have relative mass at most `2 exp(-L)/(1-exp(-L))` by (8) and
periodicity. The observed localization, logarithmic rates and critical
half-mass limit were consistent with (5)--(7); quadrature is not a rigorous
error certificate or a prime-flute PDE calculation. Scratch is outside Git.

For the actual-window boundary, a separate standard-library Decimal check
used 200-digit working precision on 15 composite endpoint triples:
`P=6*10^k+3`, `k in {6,12,24,48,80}`, `a=6`, and `b` equal to `a` or either
control above. Direct trigonometric mesh, cuff and window evaluation with
`vartheta=0.1` agreed with (17); the absolute defect error divided by
`(a+b)/P+P^-2` stayed below `0.51`. These finite high-precision checks audit
the indexing, constants and contrasting regimes, not the prime exceptional
count or an infinite subsequence. They are not interval-certified; scratch
remains outside Git.

The proof, rather than those finite checks, establishes the result. A
standalone formalization of the binomial identity would not verify the
asymptotic or its missing exceptional-prime/actual-energy application; no compute
or Lean handoff is proposed for that peripheral step.
