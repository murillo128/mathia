---
type: theorem
research_line: xi_flow
finding_id: XF-178
status: canonical
---

# XF-178 — Moment-balanced atom packets defeat every fixed-power Jacobi norm

**Evidence classification:** `EXACT-DERIVED + DECISIVE-NEGATIVE + INVERSE-STABILITY-NO-GO`. XF-176 gives exact Jacobi rigidity, while XF-177 shows that a single remote atom displacement is invisible below the half-power weight `x^(-1/2)`. The present finding shows that the half-power threshold is not a global many-atom threshold. More strongly, for every fixed power weight `x^(-alpha)`, one can move a finite packet of unit-mass atoms by a fixed nonzero absolute amount, keep positivity, evenness, uniform separation, and eventual exact agreement with the Xi comb, and make the weighted Jacobi defect converge to zero together with every fixed logarithmic scale derivative. The mechanism is exact finite moment cancellation inside the packet. Thus **no single fixed power-weighted real-axis Jacobi `C^infinity` topology is coercive for uniform atom placement** on the full positive unit-mass finite-surgery class.

## Statement

Fix a real number

\[
\alpha\ge 0.
\tag{1}
\]

Choose an integer `R>=1` such that

\[
\boxed{R+1>2\alpha.}
\tag{2}
\]

Then there exist an integer `m=R+1`, the reference offsets

\[
a_j=j,\qquad 0\le j\le R,
\tag{3}
\]

and a distinct strictly increasing offset vector

\[
b_0<b_1<\cdots<b_R,
\qquad
|b_j-j|<\frac14,
\tag{4}
\]

such that

\[
\boxed{
\sum_{j=0}^{R}b_j^r
=
\sum_{j=0}^{R}j^r
\qquad (1\le r\le R).
}
\tag{5}
\]

Because the two packets are distinct, the fixed displacement

\[
\delta_*:=\max_{0\le j\le R}|b_j-j|
\tag{6}
\]

is strictly positive.

For every sufficiently large integer `N`, form an even positive unit-mass comb `rho_N` from the integer comb `delta_Z` by replacing exactly the atoms

\[
\pm(N+j),\qquad 0\le j\le R,
\tag{7}
\]

with

\[
\pm(N+b_j),\qquad 0\le j\le R.
\tag{8}
\]

All other atoms remain unchanged. Define

\[
\Theta_N(x):=\langle\rho_N,e^{-\pi x(\cdot)^2}\rangle,
\qquad x>0,
\tag{9}
\]

and the real-axis Jacobi residual

\[
\mathcal J_N(x)
:=
\Theta_N(x)-x^{-1/2}\Theta_N(1/x).
\tag{10}
\]

Let

\[
\mathcal D:=x\frac{d}{dx}.
\tag{11}
\]

Then for every fixed integer `k>=0`,

\[
\boxed{
\sup_{x>0}
 x^{-\alpha}|\mathcal D^k\mathcal J_N(x)|
=
O_{\alpha,R,k}(N^{2\alpha-R-1}).
}
\tag{12}
\]

By `(2)`, the right-hand side tends to zero. Nevertheless every `rho_N` satisfies

\[
\boxed{
\sup_n|r_n-n|=\delta_*>0,
}
\tag{13}
\]

when its positive support is enumerated increasingly as `r_1<r_2<...`.

Consequently, for **every fixed `alpha>=0`**, there is no modulus `omega(epsilon)->0` such that uniform absolute support displacement can be bounded by the complete fixed-`alpha` logarithmic smooth topology

\[
p_{\alpha,k}(\mathcal J)
:=
\sup_{x>0}x^{-\alpha}|\mathcal D^k\mathcal J(x)|,
\qquad k=0,1,2,\ldots,
\tag{14}
\]

on this positive unit-mass finite-surgery class. Along the sequence above, every seminorm in `(14)` tends to zero while `(13)` stays fixed.

The smallest case already defeats the XF-177 half-power candidate. Take `R=1`, so the reference packet is `{0,1}` and choose

\[
\{b_0,b_1\}=\{\delta,1-\delta\},
\qquad 0<\delta<\frac14.
\tag{15}
\]

The packet preserves its center exactly. Equation `(12)` gives, in particular,

\[
\boxed{
\sup_{x>0}x^{-1/2}|\mathcal J_N(x)|=O_\delta(N^{-1}),
}
\tag{16}
\]

although the two atoms move by the fixed amount `delta`. Thus `x^(-1/2)` is sharp for an **isolated** atom but already noncoercive for a centered two-atom packet.

## 1. Moment-balanced packets exist locally around any finite integer block

Set

\[
a=(0,1,\ldots,R)\in\mathbb R^{R+1}
\tag{17}
\]

and consider the moment map

\[
F:\mathbb R^{R+1}\to\mathbb R^R,
\qquad
F_r(c)=\sum_{j=0}^{R}c_j^r,
\quad 1\le r\le R.
\tag{18}
\]

Its Jacobian at `a` is

\[
\frac{\partial F_r}{\partial c_j}(a)
=
rj^{r-1}.
\tag{19}
\]

The `R` rows have rank `R`: after dividing row `r` by `r`, they are the evaluations at the distinct points `0,1,...,R` of the monomials `1,t,...,t^(R-1)`, hence form a Vandermonde-rank system. Therefore the implicit-function theorem makes

\[
F^{-1}(F(a))
\tag{20}
\]

a smooth one-dimensional manifold near `a`.

The permutation orbit of `a` is finite and discrete. Hence `(20)` contains points `b` arbitrarily close to `a` that are not permutations of `a`. Choose one so close that `(4)` holds. The coordinate intervals `(j-1/4,j+1/4)` are disjoint, so the coordinates remain strictly ordered. Equation `(5)` is exactly `F(b)=F(a)`.

This construction is deliberately local and real. The classical Prouhet--Tarry--Escott problem is a neighboring discrete problem asking for distinct integer multisets with matching initial power sums, but no Prouhet--Tarry--Escott existence theorem is needed here. The local level-set argument supplies the required packet for every finite order `R`.

## 2. Moment cancellation suppresses the remote Gaussian packet to order `N^(-R-1)`

Let the signed offset measure be

\[
\sigma
:=
\sum_{j=0}^{R}\delta_{b_j}
-
\sum_{j=0}^{R}\delta_j.
\tag{21}
\]

Equal cardinality gives the zeroth moment cancellation, and `(5)` gives the rest:

\[
\boxed{
\int s^r\,d\sigma(s)=0
\qquad (0\le r\le R).
}
\tag{22}
\]

Since the ordinary integer theta comb obeys Jacobi reciprocity exactly, only the packet contributes to `(10)`. Put

\[
D_N(x)
:=
2\int e^{-\pi(N+s)^2x}\,d\sigma(s).
\tag{23}
\]

Then

\[
\boxed{
\mathcal J_N(x)
=
D_N(x)-x^{-1/2}D_N(1/x).
}
\tag{24}
\]

Scale

\[
y=N^2x,
\qquad
f_{N,y}(s)
:=
e^{-\pi y(1+s/N)^2}.
\tag{25}
\]

The support of `sigma` lies in a fixed bounded interval depending only on `R` and the chosen packet. Taylor-expand `f_(N,y)` in `s` through degree `R`. Every polynomial term vanishes after integration by `(22)`. Thus only the order-`R+1` remainder survives.

For `N` larger than twice the packet radius, differentiation of the quadratic exponential gives the uniform bound

\[
\left|
\partial_s^{R+1} f_{N,y}(s)
\right|
\le
C_R
N^{-R-1}
 y^q(1+y)^{R+1-q}e^{-c_Ry},
\tag{26}
\]

where

\[
q:=\left\lceil\frac{R+1}{2}\right\rceil.
\tag{27}
\]

Indeed, every term in the derivative uses first derivatives of the exponent, of size `O(y/N)`, and second derivatives, of size `O(y/N^2)`. A term of total differential order `R+1` therefore carries exactly `N^(-R-1)` and at least `q` powers of `y`. The exponential remains bounded by `e^(-c_R y)` because `1+s/N` stays uniformly away from zero.

Taylor's theorem and `(22)` now give

\[
\boxed{
|D_N(y/N^2)|
\le
C_R
N^{-R-1}
 y^q(1+y)^{R+1-q}e^{-c_Ry}.
}
\tag{28}
\]

Applying `mathcal D=x d/dx=y d/dy` a fixed number of times only changes the polynomial factor. It does not change the `N^(-R-1)` factor or the order `y^q` at the origin. Hence for every fixed `k>=0`,

\[
|\mathcal D^kD_N(y/N^2)|
\le
C_{R,k}
N^{-R-1}
 y^q(1+y)^{C_{R,k}}e^{-c_Ry}.
\tag{29}
\]

## 3. Every fixed power weight can be beaten by choosing enough packet moments

For the direct term in `(24)`, `(29)` yields

\[
\begin{aligned}
 x^{-\alpha}|\mathcal D^kD_N(x)|
&=
N^{2\alpha}y^{-\alpha}
|\mathcal D^kD_N(y/N^2)|\\
&\le
C_{\alpha,R,k}
N^{2\alpha-R-1}
 y^{q-\alpha}(1+y)^{C_{R,k}}e^{-c_Ry}.
\end{aligned}
\tag{30}
\]

Condition `(2)` implies

\[
q>\alpha,
\tag{31}
\]

so the `y` factor in `(30)` is bounded both at zero and infinity. Therefore

\[
\boxed{
\sup_{x>0}
 x^{-\alpha}|\mathcal D^kD_N(x)|
=O_{\alpha,R,k}(N^{2\alpha-R-1}).
}
\tag{32}
\]

The reciprocal term is smaller. When `v=N^2/x`, one has `1/x=v/N^2` and `x=N^2/v`. Differentiating `x^(-1/2)D_N(1/x)` produces only a finite linear combination of terms of the form

\[
x^{-1/2}(\mathcal D^jD_N)(1/x),
\qquad 0\le j\le k.
\tag{33}
\]

Using `(29)` at `v` gives

\[
\sup_{x>0}
 x^{-\alpha-1/2}
 |(\mathcal D^jD_N)(1/x)|
=
O_{\alpha,R,j}(N^{-R-2\alpha-2}),
\tag{34}
\]

because the remaining `v`-factor is polynomial times `e^(-c_Rv)`. Combining `(32)` and `(34)` proves `(12)`.

The mechanism is worth separating from a mere derivative estimate. A remote atom at radius `N` is naturally scanned at heat scale `x~N^(-2)`. XF-177's isolated displacement leaves a first offset moment, so its packet defect begins at order `N^(-1)` on that scale. Here the first `R` offset moments cancel exactly, pushing the first possible packet signal to order `N^(-R-1)`. The factor `x^(-alpha)~N^(2alpha)` can compensate only finitely many of those cancellations.

## 4. The support geometry stays source-faithful while the modular signal disappears

Because `|b_j-j|<1/4`, the moved positive atoms satisfy

\[
N+j-\frac14
<
N+b_j
<
N+j+\frac14.
\tag{35}
\]

Hence neighboring moved atoms are separated by more than `1/2`, and the first and last moved atoms remain more than `3/4` from the untouched external integers. The full support is therefore uniformly separated independently of `N`.

Every mass remains exactly one. The comb is positive and even. Outside the finite block `(7)` it agrees exactly with `delta_Z`; in particular its increasingly enumerated positive support satisfies

\[
r_n-n\to0,
\qquad
w_n\equiv1.
\tag{36}
\]

Thus the counterexample does not exploit signed masses, vanishing weights, density defects, support accumulation, or failure of the asymptotic matching hypotheses used by XF-176. The only freedom is a coordinated finite packet motion.

For `R=1`, the exact center preservation in `(15)` already cancels the isolated-atom `N^(-1)` signal and leaves an `N^(-2)` packet signal. More generally, each additional matched offset moment removes another order in the remote-scale expansion.

## 5. Consequence for the XF-176 quantitative program

XF-177 correctly identifies `alpha=1/2` as the sharp threshold for a **single independently moved atom**. It is not a threshold for the full atomwise inverse problem. Equation `(16)` shows that the smallest centered packet defeats it, and `(12)` shows that coordinated packets defeat every other fixed exponent as well.

Therefore a quantitative continuation of XF-176 cannot be based on one norm

\[
\sup_{x>0}x^{-\alpha}|\mathcal J(x)|
\tag{37}
\]

for any fixed `alpha`, nor can adding any or all fixed logarithmic scale derivatives at that same exponent repair the inverse. A finite packet can be chosen with enough exact moment cancellation to make the entire resulting fixed-`alpha` logarithmic `C^infinity` topology blind to a fixed support error.

The remaining source-side possibilities are qualitatively different:

1. use a **scale hierarchy** whose effective small-`x` resolution strengthens without a fixed exponent cap;
2. recover packet moments or atom locations through a genuinely atom-resolving transform rather than a single weighted Jacobi supremum;
3. impose a source-specific cross-index law that forbids the moment-balanced packet motions admitted here;
4. target a weaker metric than uniform absolute placement, one aligned with the topology that the modular trace actually controls.

Only after such a source-side inverse is available does comparison with height-growing Xi contour margins become meaningful. Increasing the fixed Jacobi power from `1/2` to `1`, `3/2`, or any other predetermined value does not solve the full problem.

## Stress tests and boundary conditions

The packet depends on the chosen exponent `alpha`: to defeat a stronger fixed weight one uses more matched moments and therefore a larger finite packet. The theorem does **not** construct one universal packet sequence that is simultaneously invisible for every `alpha`.

Accordingly, this result does not rule out a topology involving all power weights simultaneously, a non-polynomial small-`x` amplification, a full Mellin family, or another atom-resolving observable. It rules out only any inverse theorem whose source norm is capped at one fixed power exponent, even if all logarithmic derivatives at that exponent are included.

The result also does not weaken XF-176. Exact Jacobi residual zero plus its asymptotic matching hypotheses remains rigid. The present sequence has a nonzero defect for every finite `N`; the point is that exact rigidity has no continuous inverse in any one fixed power-weighted logarithmic smooth topology.

Finally, the construction is a source-side obstruction, not a zero-location theorem. It says that the proposed modular defect cannot by itself certify uniform square-lattice placement. It does not assert that the corresponding deformed entire functions acquire or preserve any particular zero pattern.

## Prior-art and novelty audit

The classical Prouhet--Tarry--Escott problem is the closest recognizable moment-cancellation analogue: it asks for distinct finite multisets with equal sums of initial powers. That literature concerns arithmetic/integer solutions and is not needed here. The local real packet `(17)--(20)` follows directly from the implicit-function theorem and exists at every finite order.

A targeted audit of approximate Poisson summation, Fourier-quasicrystal stability, moment matching, and Gaussian/Laplace inversion found the expected general fact that finite moment matching suppresses smooth-transform differences, but no theorem that supplies or contradicts the specific Xi/Jacobi conclusion `(12)--(14)`. No specialized external result is load-bearing, so `SOURCES.md` does not require a new dependency.

No broad novelty claim is made for moment matching or Taylor cancellation. The durable line-specific result is their exact interaction with the Xi square-lattice Jacobi scan: coordinated positive unit-mass finite surgeries can push modular visibility beyond **any predetermined power resolution** while retaining a fixed absolute atom error.

## Consequence for `xi_flow`

The cross-index program now has a sharper boundary. XF-176 proves qualitative exact rigidity; XF-177 shows that weak modular topologies miss isolated remote errors; XF-178 shows that there is **no finite critical power exponent for arbitrary coordinated atom motion**. The missing ingredient is therefore not the correct single exponent. It is a source law or transform that resolves arbitrarily high finite packet moments, or a deliberate weakening of the placement metric.

Do not spend further passes searching for a universal many-atom coercivity theorem by merely increasing the fixed weight `x^(-alpha)` or adjoining more logarithmic derivatives at that same weight. Any such fixed exponent can be defeated by a sufficiently moment-balanced remote packet.