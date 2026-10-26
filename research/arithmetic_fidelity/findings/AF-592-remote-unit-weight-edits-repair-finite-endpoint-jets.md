# AF-592 — Remote unit-weight edits repair finite endpoint jets

## Status and claim

EXACT-DERIVED · LITERATURE+DERIVED · NEGATIVE/OBSTRUCTION · GENERALIZED-PRIME-MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

A fixed finite regular jet at the prime singular endpoint does not constrain
the interior turning complexity of the inverse-source crossover. The new
ingredient is an exact **remote jet repair** with arbitrarily small error on
the entire positive real axis, implemented by moving generators rather than
changing their unit coefficients.

Write
\[
 P(s)=\sum_{p\ {\rm prime}}p^{-s},\qquad
 c=e^{B_1},\qquad
 a_Q(z)=E_1^{-1}(Q(1+z)),\qquad
 F_Q(\tau)=\frac{c\,a_Q(2\tau)}{2\tau},
 \tag{1}
\]
where `B_1` is the reciprocal-prime Mertens constant and
`E_1(a)=integral_a^infinity exp(-t)dt/t`. The inverse is the positive real
decreasing inverse. A simple generalized-prime source has distinct real
generators greater than one, each with coefficient one; its formal products
retain generator provenance.

**Remote repair theorem.** Fix an integer `m>=1`, real numbers
`d_1,...,d_m`, a cutoff `Y>1`, and `epsilon>0`. There are a finite set `S`
of rational primes above `Y` and a same-cardinality set `G` of distinct
nonintegral real generators above `Y` such that the entire function
\[
 J(z)=\sum_{g\in G}g^{-1-z}-\sum_{p\in S}p^{-1-z}
 \tag{2}
\]
satisfies
\[
 \boxed{J(0)=0,\quad J^{(j)}(0)=d_j\ (1\le j\le m),
       \qquad \sup_{z\ge0}|J(z)|<\epsilon.}
 \tag{3}
\]
The edits can avoid every previously fixed finite set of generators by
moving the whole correction beyond it. The source obtained by removing `S`
and adding `G` remains positive and unit-weight. The signed expression (2)
is a difference of two admissible blocks, not a signed source.

**Crossover consequence.** Given additionally `N>=1`, `tau_*>0`, and
`0<eta<3/4`, there is a simple unit-weight source
`Q(s)=sum_(q in Q) q^(-s)` differing from the rational primes only in a finite
set above `Y`, for which
\[
 \boxed{Q(1+z)-P(1+z)=O(z^{m+1})\quad(z\longrightarrow0),}
 \tag{4}
\]
but `F_Q` has at least `N` distinct strict local minima in `(0,tau_*)`,
each below `eta`, separated by values above `3/4`. Thus the constant term
and every regular Taylor coefficient through degree `m` agree exactly with
the prime source. Moreover
\[
 F_Q(0+)=1,\qquad F_Q(\infty)=c\log2,
 \tag{5}
\]
and `F_Q` has the same initial derivative as `F_P`, is strictly increasing
for `tau >= (1+2e)/(2 log2)`, and has only finitely many stationary points
for each fixed constructed source. Its generalized Euler product has exactly
the zeta zeros, with multiplicity, in `0<Re s<1`.

The consequence uses the separated depressions of
[[research/arithmetic_fidelity/findings/AF-591-matched-prime-endpoints-admit-arbitrarily-many-crossover-minima|AF-591]].
That construction alone does not match higher regular coefficients. The
present correction supplies that missing constraint, but permits **real**
replacement generators; it does not preserve AF-591's rational-generator
guarantee. Neither result decides uniqueness for the ordinary prime source,
and the differing shape is not an RH discriminator.

## Prime blocks supply a uniformly invertible scaled moment map

Fix `m+2` compact intervals, ordered with positive gaps,
\[
 1<\alpha_1<\beta_1<\alpha_2<\beta_2<\cdots
   <\alpha_{m+2}<\beta_{m+2}.
\]
For large `T`, let
\[
 S_i(T)=\{p\ {\rm prime}:\alpha_iT<\log p\le\beta_iT\},
 \qquad
 \mu_{i,T}=\sum_{p\in S_i(T)}\frac1p\delta_{\log p/T}.
 \tag{6}
\]
The classical Mertens limit
`sum_(p<=x) 1/p = log log x+B_1+o(1)` gives, on each fixed interval,
\[
 \mu_{i,T}\ \Longrightarrow\ \frac{dv}{v}\bigg|_{[\alpha_i,\beta_i]}.
 \tag{7}
\]
Indeed the mass of every subinterval `(a,b]` tends to `log(b/a)` by
subtracting the two Mertens asymptotics at `exp(Tb)` and `exp(Ta)`.
Step-function approximation then gives convergence against continuous
functions. Endpoint prime atoms have mass tending to zero. In particular,
for `0<=j<=m`,
\[
 M_{ji}(T):=\int v^j\,d\mu_{i,T}(v)
 \longrightarrow M_{ji}:=\int_{\alpha_i}^{\beta_i}v^{j-1}\,dv.
 \tag{8}
\]
For `j=0`, the last integral is `log(beta_i/alpha_i)`. All masses and
moments in this fixed finite array are uniformly bounded.

Every `(m+1)`-column minor of `M` is strictly positive when the columns are
in increasing interval order. Multilinearity of the determinant gives
\[
 \det[M_{j,i_\ell}]_{0\le j\le m,\ 1\le\ell\le m+1}
 =\int_{\prod_{\ell=1}^{m+1}[\alpha_{i_\ell},\beta_{i_\ell}]}
       \prod_{a<b}(v_b-v_a)\prod_{\ell=1}^{m+1}\frac{dv_\ell}{v_\ell}>0.
 \tag{9}
\]
The gaps make every Vandermonde factor positive throughout the product.
This proves the precise rank property needed below without a small-prime
determinant computation or an assumption about individual prime gaps.

Move every prime in block `i` by the same logarithmic shift `theta_i`:
`p -> exp(theta_i)p`. For `0<=j<=m`, define the scaled moment change
\[
 A_{T,j}(\theta)=
 \sum_{i=1}^{m+2}\int
 \left[e^{-\theta_i}(v+\theta_i/T)^j-v^j\right]d\mu_{i,T}(v).
 \tag{10}
\]
This is not a change of source weights. It is the exact formula for the
reciprocal log moments after moving each unit-weight generator. If `J_theta`
is (2) for these shifts, then
\[
 A_{T,j}(\theta)=\frac{(-1)^j}{T^j}J_\theta^{(j)}(0).
 \tag{11}
\]
On a fixed small ball about zero, (8) shows convergence of (10), with its
first two derivatives in `theta`, to
\[
 A_{\infty,j}(\theta)
    =\sum_i M_{ji}(e^{-\theta_i}-1).
 \tag{12}
\]
Alternatively, uniform second-derivative bounds follow directly from (10)
and bounded support in (6). The exact Jacobian at zero is
\[
 \partial_{\theta_i}A_{T,j}(0)
   =-M_{ji}(T)+\frac jT M_{j-1,i}(T),
 \tag{13}
\]
with the second term absent for `j=0`. It tends to `-M`, so every maximal
minor stays nonzero for all sufficiently large `T` and all sufficiently
small `theta`.

Set
\[
 b_T=(0,-d_1/T,d_2/T^2,\ldots,(-1)^md_m/T^m).
 \tag{14}
\]
First fix the last shift to zero. The first `m+1` columns in (13) have
uniformly bounded inverse; the second derivatives are uniformly bounded.
The local inverse theorem therefore solves
\[
 A_T(\theta)=b_T,\qquad \|\theta\|=O_d(T^{-1}).
 \tag{15}
\]
Here is the uniformity explicitly: write the restricted map as
`A_T(x)=L_T x+R_T(x)`, with `||L_T^(-1)||<=C` and
`||D R_T(x)||<=C' ||x||`. For sufficiently small `b`,
`x -> L_T^(-1)(b-R_T(x))` is a contraction on the ball
`||x||<=2C||b||`, with constants independent of large `T`.
If `b=0`, use `x=0`. This prevents a shrinking, unquantified inverse-function
neighborhood from being used to solve (14).

## Keeping the correction simple, nonintegral and uniformly small

There is one extra block in (10). In a neighborhood of the solution (15),
the exact level set `A_T=b_T` is a one-dimensional smooth curve. Every
coordinate of its tangent is nonzero: otherwise a dependence among only
`m+1` columns of the Jacobian would contradict the maximal-minor property.
Thus every `theta_i` is strictly monotone on a sufficiently short local arc.
Choose that arc inside a ball `||theta||<=C_d/T`, increasing `C_d` if
necessary; this also works when all `d_j=0`.

For each fixed finite block and bounded shift interval there are only finitely
many forbidden values `theta_i=log(n/p)`, with `n` an integer and
`p in S_i(T)`. Each coordinate takes any one of those values at most once
on the arc. Avoiding finitely many points makes every shifted generator
nonintegral, including avoidance of zero shifts. Within a block the common
dilation preserves distinctness. Across blocks, the original logarithmic
gaps have size proportional to `T`, whereas all shifts are `O_d(1/T)`;
the shifted blocks therefore stay disjoint. All new generators can be put
beyond any earlier finite edits and beyond `Y` by choosing `T` large.
They also cannot collide with any unmodified rational prime, because they
are nonintegral. This proves the simplicity and admissibility assertions.

For `t=log p`, `z>=0`, and `|u|<=C_d/T`, take `T` large enough that
`t+u>=1`. Then
\[
 (1+z)e^{-(1+z)(t+u)}
   =p^{-1}e^{-u}(1+z)e^{-z(t+u)}
   \le e^{C_d/T}p^{-1}.
 \tag{16}
\]
The last inequality uses that `(1+z)exp(-az)<=1` for `a>=1`, by
differentiation in `z`. Integrating in the shift and summing yields
\[
 \sup_{z\ge0}|J_\theta(z)|
 \le e^{C_d/T}\sum_i|\theta_i|\mu_{i,T}([\alpha_i,\beta_i])
 =O_d(T^{-1}).
 \tag{17}
\]
Equations (11), (14) and (15) give the desired derivatives exactly;
(17) makes the norm less than any supplied `epsilon`. This proves (3).
The constants can depend on the supplied derivative vector and on `m`;
no uniform growing-order claim is made.

The zeroth constraint matters. If `J(0)=d_0!=0`, its positive-axis sup norm
is at least `|d_0|`; arbitrary smallness would be impossible. For derivatives
of positive order, the factors `(log p)^j` are unbounded on remote blocks,
which is precisely what allows (3). No claim of small total variation of the
two source measures follows from (17): moving a discrete atom can keep the
source measures mutually singular even when their Laplace transforms are close.

## Applying the repair without destroying the separated minima

Use AF-591 with parameters `N,max(Y,2),tau_*` and `eta/2` to obtain a finite edit
`Q_0(1+z)=P(1+z)+H(z)` and coordinates
\[
 0<u_N<v_N<u_{N-1}<\cdots<u_1<v_1<u_0<2\tau_*
\]
such that
\[
 F_{Q_0}(u_i/2)>3/4,\qquad F_{Q_0}(v_j/2)<\eta/2,
 \qquad H(0)=0.
 \tag{18}
\]
Here `H` is a finite exponential sum, so all derivatives at zero exist.
Apply (3), beyond every generator changed in forming `Q_0`, with
`d_j=-H^(j)(0)` for `1<=j<=m`. The resulting `Q=Q_0+J` is a positive
source: the primes removed by the new correction were still present in
`Q_0`, and the added generators are distinct from its whole source.
Its finite difference from `P` has zero derivatives through order `m`,
which proves the complex analytic statement (4).

It remains to transport the small correction through the inverse; a small
source error is not automatically a small error in every downstream norm.
Here only the **fixed finite** set of values in (18) needs to survive.
Write `a=E_1^(-1)(w)`. The exact differential identity is
\[
 \frac{d\log a}{dw}=-e^a.
 \tag{19}
\]
At the finitely many positive source values `w=Q_0(1+u_i)` and
`w=Q_0(1+v_j)`, choose `epsilon` small enough to keep all intervening
`w+J` positive. On these finitely many closed neighborhoods, the inverse
values have a finite upper bound `A`. Then
\[
 |\log F_Q(z/2)-\log F_{Q_0}(z/2)|
       \le e^A\epsilon
 \tag{20}
\]
at each selected coordinate. The strict margins in (18) allow `epsilon`
small enough to retain the high values above `3/4` and low values below
`eta`. This choice is made before selecting the remote correction scale.

Every interval `[u_j/2,u_(j-1)/2]` now has an interior minimizer below
`eta`. Positivity of the source makes `Q'` strictly negative on `(1,infinity)`;
the real analytic inverse gives real analyticity of `F_Q`. Its separated
high and low values make it nonconstant, so each interior minimizer is
isolated and strict. The disjoint interiors give at least `N` minima and
the intervening high values give at least `N-1` local maxima.

## Endpoint and zero-divisor audits

The analytic regular part of `P(1+z)+log z`, and the inverse calculation in
[[research/arithmetic_fidelity/findings/AF-589-prime-window-crossover-is-set-by-the-exact-source-coordinate|AF-589]],
give the endpoint assertions without assuming anything about prime gaps.
Since `m>=1`, (4) retains both the constant and linear regular coefficients.
In particular
\[
 F_Q'(0+)=F_P'(0+)=2(c^{-1}-C_1)<0,
 \qquad C_1=\gamma+\sum_p\frac{\log p}{p(p-1)}.
 \tag{21}
\]
More generally, `F_Q-F_P=O(tau^(m+1))` at zero. To see the order rather
than merely the limit, set `a=z b(z)` in
`E_1(a)=-gamma-log a+R(a)`, where `R` is analytic and `R(0)=0`.
The equation for `b` has a nonzero derivative in `b` at `z=0`.
Changing its regular input by `O(z^(m+1))` changes `b` by that same order.

All edits occur beyond `2`, which remains the unique smallest generator with
coefficient one. Thus `Q(1+z)~2^(-1-z)` and the classical
`E_1(a)~exp(-a)/a` gives (5)'s second endpoint. For reference, with
`b=z log2`, `a=a_Q(z)` and `M_1^Q=sum (log q)q^(-1-z)`,
\[
 \operatorname{sgn}F_Q'(z/2)
 =\operatorname{sgn}\{ze^a M_1^Q(z)-1\}.
\]
If `b>=1+2e`, then
`E_1(b-1)<e exp(-b)/(b-1)<=exp(-b)/2<Q(1+z)`, so `a<b-1`.
Also `M_1^Q>=log2 Q` and `exp(a)E_1(a)>1/(a+1)` by strict Jensen
applied to the exponential density. Therefore
`ze^a M_1^Q>b/(a+1)>1`. Together with (21), this confines all stationary
points to a compact subinterval of `(0,infinity)`. Analyticity makes their
number finite for each fixed source. There is no uniform initial sign interval
over the constructed class.

For the combined finite sets of removed and added generators, the formal
Euler product satisfies
\[
 Z_Q(s)=\zeta(s)
   \frac{\prod_{p\ {m removed}}(1-p^{-s})}
        {\prod_{g\ {m added}}(1-g^{-s})}
       \qquad(\Re s>1).
 \tag{22}
\]
Every finite-factor term is analytic and nonzero on `Re s>0`, since all
generators exceed one. This continues the identity and preserves every zero
in the open critical strip with its multiplicity. Thus the theorem does not
exhibit an RH-relevant distinction erased by finite jets; it exhibits a
crossover-shape distinction even inside one fixed nontrivial zero divisor.

## Prior art, mathematical delta and limits

Mertens' reciprocal-prime asymptotic is classical: F. Mertens,
[*Ein Beitrag zur analytischen Zahlentheorie*](https://doi.org/10.1515/crll.1874.78.46),
*J. reine angew. Math.* 78 (1874), 46–62. Pollack's
[published discussion, p. 14](https://ems.press/content/serial-article-files/45523)
states precisely the finite-limit form used in (7). Divergence alone, which
was enough for AF-591's large-mass relocations, would not justify (7).

Finite-moment matching is classical. Bayer–Teichmann,
[*The proof of Tchakaloff's theorem*](https://arxiv.org/abs/math/0502473),
*Proc. Amer. Math. Soc.* 134 (2006), 3035–3040, Theorem 2, gives positive
atomic cubature with adjustable positive weights. Peled,
[*Simple Universal Bounds for Chebyshev-Type Quadratures*](https://arxiv.org/abs/0903.4625),
studies equal-weight matching of finitely many polynomial moments. These
provide the close positive-moment and fixed-weight comparisons. Neither is
invoked as a theorem allowing the linked moments `exp(-t)t^j` to be repaired
by remote ordinary-prime blocks with (17). Equations (6)–(17) prove that
specific claim directly. The integrated Vandermonde determinant, uniform
inverse-function argument and avoidance of finitely many exceptional values
are classical methods; no general moment-problem novelty is claimed.

The exponential-integral identities are
[DLMF (6.6.2)](https://dlmf.nist.gov/6.6.E2) and
[(6.12.1)](https://dlmf.nist.gov/6.12.E1). The local comparison with
[[research/arithmetic_fidelity/findings/AF-182-euler-cluster-finite-difference-flatness|AF-182]]
and
[[research/arithmetic_fidelity/findings/AF-276-finite-right-half-plane-jets-leave-exact-far-prime-euler-fibers|AF-276]]
also limits the claim: finite-jet nonuniqueness is already present in this
line. AF-182 uses clustered moment cancellation and multiplicities;
AF-276 varies Euler coefficients at fixed prime locations. The distinct
result here is exact arbitrary boundary-jet correction by remote **simple
unit-weight** generator moves, with arbitrarily small whole-axis source error.
That norm control lets the fixed-amplitude interior minima survive while
all supplied regular endpoint coefficients are restored to the prime values.

The complete analytic proof is (6)–(22). No numerical minimum search,
finite-prime simulation, formal proof-assistant validation, or independent
adversarial approval is claimed. The load-bearing checks are uniform inverse
radius, nonzero maximal minors, exact coefficient/location coupling,
collision avoidance, and transport in the finite set of downstream values.

Only a fixed finite jet is repaired; its order and size may make the required
blocks arbitrarily remote and large. An infinite regular germ would identify
the analytic finite difference and would force it to vanish, so it is outside
the obstruction. A fixed edit budget, bounded generator range, rational-only
or integer-only replacement rule, or a uniform derivative-control norm is
also outside the theorem. It supplies no ordinary-prime uniqueness result,
no general recovery theorem for the modified sources, and no RH conclusion.
