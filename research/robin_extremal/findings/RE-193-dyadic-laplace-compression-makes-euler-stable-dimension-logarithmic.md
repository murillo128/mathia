# Finding

**ID:** RE-193

**Status:** `EXACT-DERIVED + EULER-SPECTRAL-CONDITIONING + DYADIC-LAPLACE-COMPRESSION + LOGARITHMIC-STABLE-RANK + SOURCE-INFORMATION-BOUND + PRIOR-ART-BOUNDED`

**Research line:** `robin_extremal`

## Claim

Keep the exact ordinary-prime Euler channel of `RE-192`. For a finite signed packet supported on

\[
Q_-\le q\le Q_+,
\qquad 2\le Q_-\le Q_+,
\]

write

\[
D(s):=\sum_q c_q\log(1-q^{-s})^{-1},
\qquad
V:=\sum_q\frac{|c_q|}{q},
\]

and observe

\[
(\mathcal E c)(u):=Q_-^uD(1+u),
\qquad 0\le u\le U.
\]

Let

\[
W:=\log\frac{Q_+}{Q_-},
\qquad
R:=UW.
\]

For every `0<epsilon<=1/2` there is a finite-rank operator `A_epsilon` such that

\[
\boxed{
\operatorname{rank}(A_\varepsilon)
\le
C\bigl(1+\log(1+R)\bigr)
 \bigl(1+\log(1/\varepsilon)\bigr)
}
\tag{1}
\]

and

\[
\boxed{
\|\mathcal E-A_\varepsilon\|_{\ell^1(q^{-1})\to L^\infty[0,U]}
\le
\varepsilon+\frac{2}{Q_-}.
}
\tag{2}
\]

Equivalently, if

\[
r\ge
C\bigl(1+\log(1+R)\bigr)
 \bigl(1+\log(1/\varepsilon)\bigr),
\]

then

\[
\boxed{
a_{r+1}(\mathcal E)
\le
\varepsilon+\frac{2}{Q_-}.}
\tag{3}
\]

Thus `RE-192`'s global Taylor rank `O(R)` is not the correct large-rectangle capacity scale. At fixed source-scale tolerance the stable scalar Euler dimension is at most **logarithmic** in the spectral-logwidth budget `R`, not linear in it.

In particular, if

\[
Q_-=p^A,
\qquad
Q_+=p^B,
\qquad
U=\Theta(1),
\]

with fixed `0<A<B`, then `R=Theta(log p)` and

\[
\boxed{
\operatorname{rank}_{\varepsilon}(\mathcal E)
=O_\varepsilon(\log\log p)
}
\tag{4}
\]

for every fixed `epsilon>0` above the `O(p^{-A})` prime-power floor. Polynomial source separation at constant spectral distance therefore supplies at most logarithmically many robust dyadic scale coordinates.

## Derivation

The prime-power reduction from `RE-192` is unchanged. Put

\[
x_q:=\log(q/Q_-)\in[0,W].
\]

Then

\[
Q_-^u\log(1-q^{-1-u})^{-1}
=
\frac1q e^{-ux_q}+\mathcal P_q(u),
\]

with

\[
\sup_{0\le u\le U}
\left|
\sum_q c_q\mathcal P_q(u)
\right|
\le
\frac{2V}{Q_-}.
\tag{5}
\]

So it is enough to compress the first-harmonic operator. For `U>0`, set

\[
t:=u/U\in[0,1],
\qquad
y_q:=Ux_q\in[0,R].
\]

Its kernel is simply

\[
K(t,y)=e^{-ty}.
\tag{6}
\]

The case `U=0` is a single scalar evaluation and is trivially rank one.

The global Taylor expansion used in `RE-192` treats the whole interval `0<=y<=R` at once and therefore pays for the largest product `ty=R`. Instead split the source coordinate dyadically. Let

\[
I_0=[0,1],
\qquad
I_j=(2^{j-1},2^j]\cap[0,R],
\]

for `1<=j<=J`, where

\[
J\le C\bigl(1+\log(1+R)\bigr).
\]

For `j>=1` write `a_j=2^{j-1}`, so `I_j subset (a_j,2a_j]`. Fix

\[
L:=\log(8/\varepsilon),
\qquad
m:=\lceil16eL\rceil.
\]

On blocks with `a_j<=2L`, use the ordinary degree-`m-1` Taylor polynomial

\[
P_m(z):=\sum_{n=0}^{m-1}\frac{(-z)^n}{n!}.
\]

Here `0<=ty<=4L`. On a block with `a_j>2L`, introduce a continuous cutoff `chi_j:[0,1]->[0,1]` satisfying

\[
\chi_j(t)=1\quad (0\le t\le L/a_j),
\]

\[
\chi_j(t)=0\quad (2L/a_j\le t\le1),
\]

and interpolate linearly in between. Approximate the block kernel by

\[
K_j^{(m)}(t,y):=\chi_j(t)P_m(ty).
\tag{7}
\]

Whenever `chi_j(t)` is nonzero one has `ty<=4L`, and Taylor's theorem gives

\[
|e^{-ty}-P_m(ty)|
\le
\frac{(4L)^m}{m!}
\le
\left(\frac{4eL}{m}\right)^m
\le4^{-m}
\le e^{-L}.
\tag{8}
\]

In the transition region, `t>=L/a_j` and `y>a_j`, hence `ty>=L` and the discarded part is at most `e^{-L}`. Once the cutoff is zero one even has `ty>=2L`. Therefore

\[
\sup_{t\in[0,1],\,y\in I_j}
|e^{-ty}-K_j^{(m)}(t,y)|
\le2e^{-L}
\le\varepsilon/4.
\tag{9}
\]

The same Taylor estimate handles `I_0`. The important point is that every block approximant has separated rank at most `m`: after expanding (7), its terms are

\[
\left[\chi_j(t)(-t)^n/n!\right]
\left[y^n\mathbf 1_{I_j}(y)\right].
\]

Because the `I_j` partition the source axis, summing the block approximants does **not** sum their pointwise errors: every source location belongs to only one block. Hence the resulting kernel approximation is uniformly `O(e^{-L})` on the entire rectangle, while its rank is at most

\[
(J+1)m
\le
C\bigl(1+\log(1+R)\bigr)
 \bigl(1+\log(1/\varepsilon)\bigr).
\tag{10}
\]

Uniform kernel error immediately gives the same operator error from the weighted source `ell^1` norm `V` to spectral `L^infinity`. Combining (10) with the exact prime-power remainder (5) proves (1)--(3).

The bound also gives a useful inverse reading. If a scalar Euler channel is claimed to carry `K` robust independent coordinates at tolerance `epsilon`, the present upper bound can fail to rule that out only if

\[
\boxed{
\log(1+R)
\gtrsim
\frac{K}{1+\log(1/\varepsilon)}.
}
\tag{11}
\]

At fixed tolerance this means `R` must be at least exponential in `K`. Shrinking the requested tolerance can buy additional effective rank, so (11) is a precision-aware necessary condition, not an absolute dimension law.

## Representation audit

The decisive representation is again the exact Euler discrepancy in logarithmic source coordinates, but `RE-193` changes how the finite-Laplace rectangle is resolved. A single global polynomial sees the largest product `R=UW`; a dyadic source decomposition instead follows the natural decay geometry of `e^{-ux}`. Large source coordinates matter only in a correspondingly thin boundary layer `u=O(1/x)`, so each multiplicative source scale costs only `O(log(1/epsilon))` separated directions. The number of relevant scales is `O(log(1+R))`.

The low-rank mechanism itself is generic positive finite-Laplace geometry. Nothing in the dyadic argument uses primality. The `robin_extremal` ownership is retained because the actual observable is still the exact ordinary-prime Euler-factor discrepancy, the source norm is the reciprocal prime-multiplicity variation used by the matched controls, and the `n>=2` Euler harmonics are uniformly below the explicit `O(Q_-^-1)` floor. No surrogate source or unsigned replacement is introduced.

The block indicators in the source variable do not assume that primes fill the intervals: they merely group whatever ordinary primes are present. The continuous spectral cutoff is deliberate. A hard cutoff would still give a pointwise separated approximation but would leave the natural `C([0,U])`/continuous-profile codomain; the continuous cutoff keeps the finite-rank approximant in the same spectral function space.

## Exact or empirical?

Exact and derived. The proof uses only the Euler expansion, a dyadic partition, a continuous cutoff and Taylor's theorem. No numerical singular-value experiment, zero statistic, asymptotic fit or probabilistic model is used.

## Source dependence

The source-specific content is the reduction of the exact ordinary-prime Euler packet to the positive Laplace kernel with the explicit prime-power floor (5). The logarithmic rank estimate for `e^{-ty}` is a generic approximation statement and would apply equally to signed measures on a positive source interval.

The finding does **not** construct a `{0,1,2}` matched control across polynomial source scales, does not prove a matching lower bound `Omega(log R)`, does not show that `R->infinity` creates Robin leverage, and does not convert finite-precision stable information into exact source identification. It only strengthens the information-capacity upper bound.

## Prior-art audit

A targeted search was run for truncated/finite Laplace transforms, low-rank exponential-kernel approximations and dyadic/hierarchical kernel compression. Lederman--Rokhlin analyze the singular system and severe conditioning of truncated Laplace transforms. Bourguiba--Karoui prove super-exponential spectral decay for a weighted finite bilateral Laplace operator. Hierarchical low-rank approximation of smooth kernel blocks is also standard numerical-analysis technology.

Those references make the generic compression phenomenon prior art territory; no novelty is claimed for the abstract idea that Laplace/exponential kernels admit efficient separated approximation. The search did not locate the exact elementary `ell^1(q^-1) -> L^infinity` dyadic bound (1)--(3), nor its ordinary-prime Euler-packet consequence (4). No external theorem is load-bearing because the needed estimate is proved directly above, so `SOURCES.md` requires no new durable dependency.

## Literature status

Generic finite-Laplace compactness, spectral decay and hierarchical low-rank kernel approximation are established themes. The line-specific contribution is an exact Mathia lemma that sharpens `RE-192` from a global `O(R)` Taylor budget to a precision-aware `O(log(1+R) log(1/epsilon))` budget for the ordinary-prime Euler channel, thereby showing that the first `R_p->infinity` regime identified by `RE-192` still has very small robust scalar capacity.

## Caveats

The estimate is one-sided on real `s>=1`; vertical imaginary sampling or analytic continuation can have different geometry. The rank bound is only an upper bound and may be far from sharp. It is a finite-precision statement: exact continuum data remain source-rigid by analyticity, and if `epsilon` shrinks rapidly with `p` the factor `log(1/epsilon)` can itself carry substantial dimension. The theorem controls the scalar Euler channel, not a joint source-native observable tied directly to the Robin destination.

For fixed `U` and polynomial source support, (4) is only a fixed-tolerance statement. At a source-native tolerance that decays polynomially or faster, the allowed rank can grow much more quickly. Any proposed rigidity argument must therefore state its actual residual scale before using the logarithmic fixed-precision corollary.

## Next experiment

Stop treating `R_p->infinity` alone as the next scalar threshold. Quantify the **actual source-native tolerance** required by a selector-scale Robin displacement, insert it into

\[
(1+\log(1+R_p))(1+\log(1/\varepsilon_p)),
\]

and compare that capacity with the number of independent source constraints a rigidity proof would need. In parallel, test whether honest ordinary-prime `{0,1,2}` matched controls can realize even the dyadic `O(log R_p)` scale degrees of freedom while preserving a fixed KV envelope and the transient Robin excursion. If they can, the scalar route must move to a genuinely joint/nonlocal invariant rather than merely enlarging the Euler rectangle.

## Sources

- `RE-190`, *Shrinking Euler sampling windows collapse to reciprocal-mass rank one*.
- `RE-191`, *Fixed Euler-temperature windows are factorially compressible*.
- `RE-192`, *Spectral span times log-source width controls Euler stable rank*.
- R. R. Lederman and V. Rokhlin, *On the Analytical and Numerical Properties of the Truncated Laplace Transform I*, SIAM Journal on Numerical Analysis **53** (2015), 1214--1235, DOI `10.1137/140990681`.
- N. Bourguiba and A. Karoui, *Weighted finite Laplace transform operator: spectral analysis and quality of approximation by its eigenfunctions*, Integral Transforms and Special Functions **29** (2018), 679--698, DOI `10.1080/10652469.2018.1489804`.
