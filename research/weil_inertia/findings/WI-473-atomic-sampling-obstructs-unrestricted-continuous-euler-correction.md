# WI-473 — atomic sampling obstructs unrestricted continuous Euler correction

**Status:** LITERATURE+EXACT-DERIVED + CLASSICAL-UNIFORM-BOUNDEDNESS-SPECIALIZATION + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM + NON-RH.

**Local dependencies:** [WI-461](WI-461-fixed-scale-euler-peaks-have-positive-density-at-zeta-zero-ordinates.md), for the leading Haar law and its absolute continuity; [WI-470](WI-470-three-prime-curvature-gives-finite-euler-correction-at-every-safe-line.md), for the finite signed scalar correction. [WI-469](WI-469-gevrey-cutoffs-admit-the-full-first-euler-sampling-correction.md) and [WI-472](WI-472-log-distance-decay-enlarges-the-euler-sampling-test-class.md) establish the separate positive Gevrey-test results.

## Claim and boundary changed

Fix `sigma>1` and `r>0`. Let `Q` be the full, originally normalized
Euler response, `mu=Q_#m` its Haar probability law, and `nu` the finite
signed correction of WI-470. Set

\[
 D_T=N(2T)-N(T),\qquad
 P_T=\frac1{D_T}\sum_{T<\gamma\le2T}\delta_{Q(\gamma)},\qquad
 c_T=\frac{2\pi D_T}{T},\qquad R_T=c_T(P_T-\mu).
 \tag{1}
\]

Here `N(T)` counts nontrivial zeros with `0<Im(rho)<=T`, and (1) is
used for sufficiently large `T` that `D_T>0`. Zeros are counted with
multiplicity, without restricting real parts.
The total variation convention is the full variation mass, not half
that mass. Then

\[
 \boxed{\|R_T\|_{\rm TV}=2c_T=2\log T+O(1),\qquad
 \|R_T-\nu\|_{\rm TV}=2\log T+O_{\sigma,r}(1).}
 \tag{2}
\]

For every prescribed sequence `T_j -> infinity` there is a **fixed real
continuous** test `f` on `[0,q_*]`, with `0<=f<=1`, such that

\[
 \boxed{\limsup_j|R_{T_j}(f)|=\infty.}
 \tag{3}
\]

Thus the order-`T` sampling expansion

\[
 \sum_{T<\gamma\le2T}f(Q(\gamma))
 =D_T\int f\,d\mu+\frac{T}{2\pi}\int f\,d\nu+o_f(T)
 \tag{4}
\]

**cannot hold for every fixed continuous test.** The same failing test
defeats every fixed finite signed correction measure, since subtracting
its finite integral cannot remove (3). Failure can be localized to any
open interval of positive `mu` mass. Replacing Haar centering by the
continuous-height mean also does not give an all-continuous-test theorem.

Unlike WI-471, this is an obstruction to the arithmetic assertion itself,
not merely to absolute Fourier summability. It is a classical sampling
obstruction, not an arithmetic defect detector. It does not refute (4)
for every smooth test, any specified threshold, or any specified function
of bounded variation.

## The diffuse comparison law is justified for this object

On the product prime torus with probability Haar measure `m`, define

\[
 A=\sum_{n\ge2}\Lambda(n)n^{-\sigma},\quad
 a_n=\Lambda(n)n^{-\sigma}/A,\quad
 G_r(n,m)=e^{-r|\log(n/m)|}-(nm)^{-r},
\]
\[
 Q(z)=\sum_{n,m\ge2}a_na_mG_r(n,m)\chi_{n/m}(z),\qquad
 z_p(t)=e^{-it\log p},\qquad Q(t)=Q(z(t)).
 \tag{5}
\]

For a positive rational `u`, `chi_u(z)=product_p z_p^(nu_p(u))`, where
`nu_p(u)` is its signed prime exponent. Only prime powers have nonzero
`a_n`. The series converges absolutely and uniformly. The Gram representation
gives `0<=Q<=q_*:=Q(1)<=1`. The strict positivity of `G_r(p,q)` for
distinct primes is important below.

Here is the non-atomicity check, independently of any sampling error
estimate. Condition on every prime coordinate except two distinct primes
`p,q`. The remaining real function `F(theta,psi)` is analytic on the
two-dimensional torus: each prime-power series has geometrically decaying
coefficients, including every differentiated series. Its Fourier
coefficient at `(1,-1)` is exactly
`a_p a_q G_r(p,q)>0`, independently of the frozen tail. Terms involving
only one of these coordinates cannot cancel that coefficient. Therefore
`partial_theta F` is a nonzero real analytic function and has a
two-dimensional null zero set. Off that set, the local change of variables
`(theta,psi) -> (F(theta,psi),psi)` is nonsingular. A countable chart cover
shows that every scalar Lebesgue-null set has null preimage. Integrating
over the frozen coordinates proves

\[
 \mu\ll dx.
 \tag{6}
\]

This is the conditional analytic argument of WI-461; the three-anchor
curvature argument of WI-470 also gives (6) and additionally constructs
`nu=k(x)dx`, `k in L^1`, with `nu([0,q_*])=0`. In particular (6) is
not an assumption about where actual zeros occur. No RH input enters it.

## Exact residual norm and a single fixed bad test

Let `S_T` be the finite set of sampled response values. Repeated
ordinates or repeated response values merely combine positive atoms.
Then `P_T(S_T)=1` and `mu(S_T)=0`, so the two probability measures are
mutually singular. Their difference has positive and negative parts
`P_T` and `mu`. This proves `||R_T||_TV=2c_T` exactly.

The Riemann--von Mangoldt formula gives

\[
 c_T=\log T+2\log2-\log(2\pi)-1+O(\log T/T).
 \tag{7}
\]

For any fixed finite signed measure `eta`, the triangle inequalities give

\[
 2c_T-\|\eta\|_{\rm TV}
 \le\|R_T-\eta\|_{\rm TV}
 \le2c_T+\|\eta\|_{\rm TV}.
 \tag{8}
\]

Taking `eta=nu` proves the remaining assertion in (2). No sign or
absolute-continuity property of `eta` is needed for (8).

Each `R_(T_j)` is a bounded real linear functional on the Banach space
`C([0,q_*])` with the uniform norm. Its operator norm equals its
measure total variation. For this particular difference the equality
can also be seen directly: choose a continuous function equal to one at
all points of `S_T` and equal to minus one outside an open neighborhood
of arbitrarily small `mu` mass. Its `R_T` value tends to `2c_T`.

To make the fixed-test quantifier explicit, define the closed sets

\[
 E_K=\{f:\sup_j|R_{T_j}(f)|\le K\},\qquad K=1,2,\ldots.
 \tag{9}
\]

If any `E_K` contained a ball of radius `epsilon` around `f_0`,
subtracting the bounds at `f_0+h` and `f_0` would give
`||R_(T_j)||<=2K/epsilon` for every `j`, contrary to (2). Each `E_K`
therefore has empty interior. Baire's theorem shows that the tests with
unbounded residual form a dense `G_delta` set. Choose one real `g` from
that set. Since `R_T(1)=0`, replacing it by
`f=(1+g/||g||_infinity)/2` proves (3) with `0<=f<=1`.

The witness is fixed after the height sequence is prescribed; it is not
a different test chosen at each height. The existence proof gives no
formula, smoothness, monotonicity, variation bound, or independently
specified arithmetic construction of that witness.

For localization let `I=(a,b)` have closure in `(0,q_*)` and `mu(I)>0`.
Apply the same argument to the Banach space `C_0(I)`, extended by zero.
The restricted norm is

\[
 \|R_T|_{C_0(I)}\|=c_T\{P_T(I)+\mu(I)\}\ge c_T\mu(I)\longrightarrow\infty.
 \tag{10}
\]

Regularity of the measures allows continuous tests vanishing at the
endpoints to approximate the signs on compact subsets of `I`.
This proves the norm identity even if atoms approach an endpoint.
The resulting real witness is supported in `[a,b]`; at least one of
its positive and negative parts still has unbounded residual. Scaling
that part gives a nonnegative continuous witness bounded by one in the
same response window. Such windows exist by (6).

## Continuous-height centering does not repair the all-test claim

Put `mu_T^h=T^(-1) integral_T^(2T) delta_(Q(t)) dt` and
`R_T^h=c_T(P_T-mu_T^h)`. The scalar function `Q(t)` is real analytic:
in every strip `|Im t|<delta<sigma-1`, (5) is dominated by
`sum_(n,m) a_n a_m (nm)^delta<infinity`. It is nonconstant, since

\[
 Q''(0)=-\sum_{n,m\ge2}a_na_mG_r(n,m)(\log(n/m))^2<0.
 \tag{11}
\]

The differentiated sum converges; any two distinct primes supply a
strictly negative term. A nonconstant real analytic function has only
isolated critical points on each bounded real interval. One-dimensional
change of variables away from them proves `mu_T^h<<dx`. Hence

\[
 \|R_T^h\|_{\rm TV}=2c_T.
 \tag{12}
\]

The fixed-test argument applies again, including subtraction of any
fixed finite signed correction. The Haar and continuous-height centers
can be interchanged for the established Gevrey class using its arithmetic
estimate; their interchange at the correction scale is not asserted for
an arbitrary continuous test.

## Prior art, matched controls and consequence

Ford--Soundararajan--Zaharescu, *On the distribution of imaginary parts
of zeros of the Riemann zeta function, II*, **Math. Ann. 343** (2009),
487--505, [§1, immediately before and after (1.4)](https://arxiv.org/pdf/0805.2745),
already state that the leading fractional-part law can converge
arbitrarily slowly for continuous tests and that its first correction
cannot hold for all such tests. Their (1.2) supplies the zero-counting
normalization used in (7). This phenomenon is therefore established
prior art, not a new general zeta-sampling principle.

The functional-analytic step is the classical Banach--Steinhaus/Baire
argument, proved in (9). For an explicit quadrature comparison see
Alen Alexanderian, *A basic note on convergence of quadrature formulas*,
revised March 5, 2018, [Theorems 1.1 and 2.1](https://aalexan3.math.ncsu.edu/articles/quad_conv_note.pdf):
dense-class convergence needs a uniform functional norm before it
extends to all continuous tests. Here that norm diverges exactly.

The local mathematical delta is the verified nonlinear Euler pushforward
application: (6) and (11) make the empirical and both comparison laws
mutually singular, (2) fixes the exact residual scale, and (10) shows
that failure is not confined to a response endpoint. WI-470's finite
coefficient measure cannot supply the missing uniform bound. This
eliminates a general continuous-test extension even if a different
Fourier norm were to replace WI-471's failing certificate.

The controls are essential to interpreting the result:

- Any finite empirical probability law compared with a non-atomic law
  has the same norm obstruction under a diverging rescaling. Equally
  spaced quadrature points already provide a matched control. Thus no
  off-critical-zero information is present in this argument.
- Prime-only nonconstant responses remain subject to the obstruction
  even when their prime-axis correction is zero. A constant diagonal
  response, or `r=0`, has atomic Haar law and falls outside (6).
- Leading convergence `P_T(f)->mu(f)` for every continuous `f` remains
  valid. Dividing (3) by `c_T` can still give zero. There is no conflict
  with WI-461's uniform leading threshold law.
- Diverging total variation does not force failure on any specified
  threshold or bounded-variation class. For example, empirical uniform
  grids can have `O(1/n)` interval discrepancy while their difference
  from Lebesgue measure has variation two. Threshold discrepancy and
  all-continuous-test convergence at a finer scale are different gates.
- The witness need not be smooth. WI-469/WI-472 and WI-470's finite
  scalar coefficient remain intact. No numerical, formal, or independent
  adversarial certification is claimed.

The bounded question closes at this classical but strict arithmetic
boundary. Further threshold work must retain a test regularity or
discrepancy budget; coefficient existence and uniform approximation alone
cannot yield (4) for every continuous test. No separate formalization
handoff is selected: the general measure/Baire lemma is standard and no
additional structural fertility question is identified here.
