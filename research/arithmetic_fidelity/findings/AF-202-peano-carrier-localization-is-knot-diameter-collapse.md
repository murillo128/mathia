# AF-202 — Peano-carrier localization is exactly anchored knot-diameter collapse

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-BRIDGE`, `SOURCE-LOCALIZATION`, `QUANTITATIVE-RECOVERY`, `NO-NOVELTY-CLAIM`

## Claim

AF-199 identifies the normalized Peano B-spline as the positive carrier of every minimal-support moment-flat divided-difference control, and AF-201 proves that weak concentration of that carrier at the anchored endpoint is exactly the localization topology seen by a fixed finite Euler band when the homogeneous source profile stays two-sided bounded. The remaining localization condition can be translated completely back into the source knots.

Fix an order `m>=1` and distinct ordered knots

\[
x=u_0<u_1<\cdots<u_m,
\qquad
D:=u_m-x>0.
\tag{1}
\]

Let

\[
\beta_u(dv)=B_u(v)\,dv
\tag{2}
\]

be the normalized Peano B-spline probability carrier from AF-199. Let

\[
\Theta=(\Theta_0,\ldots,\Theta_m)
\sim \operatorname{Dirichlet}(1,\ldots,1)
\tag{3}
\]

be uniform on the standard `m`-simplex and define the random convex combination

\[
V_u:=\sum_{j=0}^m\Theta_j u_j.
\tag{4}
\]

Then the classical Genocchi-Hermite formula and the AF-199 Peano representation give the exact identity in law

\[
\boxed{
\beta_u=\mathcal L(V_u).
}
\tag{5}
\]

Consequently the carrier cannot concentrate at `x` while even one extreme knot remains macroscopically separated from `x`. More quantitatively, for every `0<r<D`,

\[
\boxed{
\beta_u([x+r,\infty))
\ge
\left(1-\frac rD\right)^m.
}
\tag{6}
\]

Indeed `V_u-x>=Theta_m D`, and the uniform-simplex marginal satisfies

\[
\mathbb P(\Theta_m\ge a)=(1-a)^m,
\qquad 0\le a\le1.
\tag{7}
\]

Now specialize the AF-201 real Euler localization defect. For fixed `sigma>0`, write

\[
g_0(v)=F_\sigma^{(4)}(v)>0,
\qquad
c(r):=1-\frac{g_0(x+r)}{g_0(x)}>0
\quad(r>0),
\tag{8}
\]

and

\[
\Lambda_\sigma(\beta_u)
:=1-\frac1{g_0(x)}\int g_0(v)\,d\beta_u(v).
\tag{9}
\]

Since `g_0` is strictly decreasing on `[x,infinity)`, `(5)`--`(7)` imply the two-sided diameter estimate

\[
\boxed{
2^{-m}c(D/2)
\le
\Lambda_\sigma(\beta_u)
\le
c(D).
}
\tag{10}
\]

The upper bound uses only `supp(beta_u) subset [x,x+D]`; the lower bound is the nontrivial direction and follows because at least `2^{-m}` of the Dirichlet-simplex mass satisfies `Theta_m>=1/2` and therefore lands at or beyond `x+D/2`.

Hence for any sequence of fixed-order minimal-support controls with common anchored endpoint `x`, writing `D_n=u_{m,n}-x`,

\[
\boxed{
D_n\to0
\quad\Longleftrightarrow\quad
\Lambda_\sigma(\beta_n)\to0
\quad\Longleftrightarrow\quad
\beta_n\Rightarrow\delta_x.
}
\tag{11}
\]

Thus **weak Peano-carrier localization is not an additional hidden probability-space condition in the fixed-order minimal-support class: it is exactly contraction of the full knot diameter to the anchored endpoint.** Compact gap-ratio control and bounded `D_n/W_1` are sufficient ways to force this, but neither is the intrinsic localization topology.

For the quartic five-node source class of AF-195--AF-201, `(11)` combines with AF-201 immediately. If

\[
0<q_-\le Q_n\le q_+<\infty,
\tag{12}
\]

then uniform finite-band transfer of the normalized full Euler transform to its quartic endpoint model is equivalent to

\[
\boxed{D_n\to0.}
\tag{13}
\]

In particular, the source-side localization part of the accepted quartic clue is now exact. The remaining question is no longer which probability topology on the Peano carrier is required; it is whether a natural source class or full-Euler sublevel condition forces `(12)` and `(13)` simultaneously, or whether diameter contraction must be declared as an independent resource.

## Derivation

### 1. Genocchi-Hermite identifies the Peano B-spline as a Dirichlet barycentric law

For sufficiently smooth `f`, AF-199 gives

\[
f[u_0,\ldots,u_m]
=
\frac1{m!}
\int f^{(m)}(v)\,d\beta_u(v).
\tag{14}
\]

The classical Genocchi-Hermite formula expresses the same divided difference as an integral of `f^(m)` over the simplex of convex combinations of the knots. With normalized simplex probability measure this is

\[
f[u_0,\ldots,u_m]
=
\frac1{m!}
\mathbb E\!\left[
 f^{(m)}\!\left(\sum_{j=0}^m\Theta_j u_j\right)
\right].
\tag{15}
\]

Given any continuous test function `h` on `[u_0,u_m]`, choose an `m`-fold antiderivative `f` with `f^(m)=h`. Comparing `(14)` and `(15)` yields

\[
\int h(v)\,d\beta_u(v)
=
\mathbb E[h(V_u)],
\tag{16}
\]

for every continuous `h`, proving `(5)`.

This also recovers AF-200's barycenter formula without a separate polynomial calculation. Since `E Theta_j=1/(m+1)`,

\[
\int v\,d\beta_u(v)
=
\frac1{m+1}\sum_{j=0}^m u_j.
\tag{17}
\]

The full law, rather than only its first moment, is what makes the converse localization statement possible.

### 2. The extreme knot leaves a fixed amount of carrier mass at its own scale

Because every knot is at least `x`,

\[
V_u-x
=
\sum_{j=0}^m\Theta_j(u_j-x)
\ge
\Theta_m D.
\tag{18}
\]

Under uniform measure on the simplex, the slice `Theta_m>=a` is an affine copy of the full simplex scaled by `1-a` in `m` dimensions. Its relative volume is therefore

\[
(1-a)^m.
\tag{19}
\]

Taking `a=r/D` in `(18)` proves `(6)`. In particular,

\[
\beta_u([x+D/2,\infty))\ge2^{-m}.
\tag{20}
\]

This rules out a failure mode that is possible for arbitrary probability measures: an extreme support point cannot carry vanishingly small Peano probability independently of the other knots. In a fixed-order normalized B-spline, the simplex geometry gives a dimension-dependent positive amount of mass at a fixed fraction of the extreme-knot scale.

### 3. The AF-201 Euler defect is quantitatively equivalent to knot diameter

By `(9)`,

\[
\Lambda_\sigma(\beta_u)
=
\int
\left(1-\frac{g_0(v)}{g_0(x)}\right)
\,d\beta_u(v).
\tag{21}
\]

The integrand is nonnegative and increasing on `[x,infinity)`. Since the carrier is supported inside `[x,x+D]`,

\[
\Lambda_\sigma(\beta_u)
\le
1-\frac{g_0(x+D)}{g_0(x)}
=c(D),
\tag{22}
\]

which is the upper half of `(10)`.

On the event `V_u>=x+D/2`, the integrand in `(21)` is at least `c(D/2)`. Equation `(20)` therefore gives

\[
\Lambda_\sigma(\beta_u)
\ge
c(D/2)\,2^{-m},
\tag{23}
\]

proving the lower half.

If `D_n->0`, continuity of `g_0` at `x` makes `c(D_n)->0`, so `(22)` gives `Lambda_sigma(beta_n)->0`. Conversely, if `Lambda_sigma(beta_n)->0` but `D_n` fails to tend to zero, then along some subsequence `D_n>=epsilon>0`. Equation `(6)` with the fixed radius `r=epsilon/2` gives

\[
\beta_n([x+\epsilon/2,\infty))
\ge2^{-m},
\tag{24}
\]

and `(21)` then yields the fixed contradiction

\[
\Lambda_\sigma(\beta_n)
\ge
2^{-m}c(\epsilon/2)>0.
\tag{25}
\]

This proves the first equivalence in `(11)`. The second is AF-201's general characterization of the same defect, and also follows directly from `(6)` plus shrinking support.

## Consequence for the quartic localization frontier

AF-200 showed that source `W_1` alone permits a five-knot quartic control to keep fixed transport separation while sending most of its relevant Peano geometry out to a region where the fixed Euler band is exponentially insensitive. AF-201 then identified weak carrier concentration as the exact bounded-profile observation topology but deliberately left its source-side meaning open.

Equation `(11)` closes that translation: **for fixed cancellation order and minimal support, the source-localization variable is simply the anchored knot diameter.** One does not need a bounded carrier first moment, a compact projective gap-ratio class, or a bounded diameter-to-`W_1` ratio as the definition of localization. Those are stronger mechanisms that may imply the true condition `D->0`.

This also isolates the remaining difficulty cleanly. The homogeneous profile `Q` is dilation invariant, whereas `D` scales linearly with common knot dilation. Therefore profile control and localization are logically different resources. A bounded `Q_n` sequence does not, by this finding alone, imply `D_n->0` from `W_1->0`; proving such a projective properness theorem, or finding a counterexample, remains a separate source-geometry problem. Likewise, compactness of full-Euler minimizing sublevels has not been established.

For any future Gamma-convergence or minimizer-transfer argument in the quartic class, the localization assumption can now be audited at the source level: under `(12)`, AF-201's finite-band endpoint reduction holds exactly when the extreme knot contracts to `x`. Any stronger proposed condition must justify why its extra projective information is needed for something beyond localization itself.

## Prior art and novelty assessment

The Genocchi-Hermite simplex representation of divided differences is classical. Carl de Boor's survey **“Divided Differences,”** *Surveys in Approximation Theory* 1 (2005), 46--69, explicitly records the simplex integral representation and its historical Genocchi/Hermite provenance (e-print `arXiv:math/0502036`). AF-199 already audited the equivalent Peano-kernel/B-spline representation against classical divided-difference and spline theory.

The probabilistic/Dirichlet-average interpretation of B-splines is also established prior art. B. C. Carlson, **“B-splines, hypergeometric functions, and Dirichlet averages,”** *Journal of Approximation Theory* 67 (1991), 311--325, develops the B-spline/Dirichlet-average connection. Brigitte Forster and Peter Massopust, **“Statistical encounters with complex B-splines,”** *Constructive Approximation* 29 (2009), 325--344, DOI `10.1007/s00365-008-9019-x`, explicitly uses generalized Hermite-Genocchi formulas for stochastic/Dirichlet-mean interpretations.

No novelty is claimed for `(5)`, the simplex marginal `(7)`, or the general probabilistic interpretation. The durable Arithmetic Fidelity result is the exact specialization of those classical facts to the AF-199/AF-201 source-observation bridge: the quantitative defect sandwich `(10)` and the equivalence `(11)` identify the previously unresolved Peano localization topology with a concrete source-knot condition and remove several stronger candidate localization assumptions from the intrinsic gate.

## Boundaries

- The equivalence uses **fixed finite order `m`** and the normalized minimal-support Peano B-spline. It is not uniform when the cancellation order or number of knots grows; the lower mass constant `2^{-m}` then degenerates.
- The left endpoint is anchored and every knot lies to its right. A moving anchor requires the corresponding translated statement; a two-sided source would need a different extreme-knot audit.
- Knot diameter contraction settles carrier localization only. It does not prove boundedness or coercivity of the scale-free profile `Q`, global optimality of any knot shape, or compactness of full-Euler sublevels.
- AF-201's equivalence between carrier localization and uniform finite-band transfer still requires the declared two-sided profile bounds. This finding does not remove those hypotheses.
- The result concerns the matched moment-flat control class, not the rational primes themselves. It establishes no prime-specificity or RH consequence.
- No claim is made that `D->0` is necessary for arbitrary non-minimal-support probability carriers. The converse relies on the Dirichlet-simplex law forced by the fixed-order minimal-support B-spline geometry.
