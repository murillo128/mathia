# RE-130 — algebraic finite-edge packet mass always contains an algebraically strong atom

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + NONISOLATED-EDGE + ABSOLUTE-PACKET-MASS + OFF-CRITICAL-ZERO-DENSITY + SHARPENED-MAX-ATOM-INTERPOLATION + DIFFUSE-BRANCH-ELIMINATION + CA-PHASE-TRANSFER + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

Assume the attained finite-edge branch and notation of `RE-121`--`RE-129`,

\[
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1,
\qquad
\frac12<\sigma_0<\Theta,
\]

and fix `K>=0`. For a positive-ordinate subedge zero

\[
\rho=\beta+i\gamma,
\qquad
\sigma_0\le\beta<\Theta,
\qquad
\gamma>0,
\]

write

\[
a_{\rho,K}(U)
:=e^{-(\Theta-\beta)U}
\left[
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^{K}\frac{(-1)^k k!}{U^k(1-\rho)^{k+1}}
\right].
\tag{1}
\]

Define the largest atom and the absolute packet mass by

\[
M_K(U)
:=
\max_{\substack{\zeta(\rho)=0\\
\sigma_0\le\Re\rho<\Theta\\
\Im\rho>0}}
|a_{\rho,K}(U)|,
\tag{2}
\]

and

\[
\mathfrak A_K(U)
:=
\sum_{\substack{\zeta(\rho)=0\\
\sigma_0\le\Re\rho<\Theta\\
\Im\rho>0}}
|a_{\rho,K}(U)|,
\tag{3}
\]

with zeros counted with multiplicity. The maximum exists by `RE-129`, and the sum converges absolutely.

The original version of this finding used the full Riemann--von Mangoldt count and obtained

\[
\mathfrak A_K(U)
\ll
\sqrt{M_K(U)}\log\frac e{M_K(U)}.
\]

That is sufficient to eliminate the diffuse branch, but it throws away a source-specific fact already available elsewhere in this line: every atom in (3) lies in the fixed off-critical half-strip `Re rho>=sigma_0`, whose zeros have sublinear density. Keeping that information gives a strictly stronger interpolation.

Let

\[
N_{\sigma_0}(T)
:=
\#\{\rho=\beta+i\gamma:\zeta(\rho)=0,\ \beta\ge\sigma_0,\ 0<\gamma\le T\},
\tag{4}
\]

counting multiplicity. More generally, suppose for some fixed `kappa<2` and `q>=0` that

\[
N_{\sigma_0}(T)
\ll
T^\kappa(\log T)^q.
\tag{5}
\]

Then, whenever `U` is sufficiently large and `0<M_K(U)<=e^-2`, one has

\[
\boxed{
\mathfrak A_K(U)
\ll
M_K(U)^{1-\kappa/2}
\left(\log\frac e{M_K(U)}\right)^q.
}
\tag{6}
\]

For the classical Ingham zero-density estimate,

\[
\kappa_I(\sigma_0)
:=
\frac{3(1-\sigma_0)}{2-\sigma_0}<1,
\qquad q=5,
\tag{7}
\]

so with

\[
\boxed{
\alpha_I(\sigma_0)
:=1-\frac{\kappa_I(\sigma_0)}2
=
\frac{1+\sigma_0}{2(2-\sigma_0)}
>
\frac12,
}
\tag{8}
\]

we obtain the strict power improvement

\[
\boxed{
\mathfrak A_K(U)
\ll
M_K(U)^{\alpha_I(\sigma_0)}
\left(\log\frac e{M_K(U)}\right)^5.
}
\tag{9}
\]

The current Guth--Maynard density theorem can improve the power further in the range where its headline exponent beats Ingham. Put

\[
\kappa_G(\sigma_0)
:=\frac{30(1-\sigma_0)}{13},
\qquad
\kappa_*(\sigma_0)
:=\min\{\kappa_I(\sigma_0),\kappa_G(\sigma_0)\},
\tag{10}
\]

and

\[
\alpha_*(\sigma_0)
:=1-\frac{\kappa_*(\sigma_0)}2.
\tag{11}
\]

Since Ingham already gives `kappa_I<1`, one always has `alpha_*>1/2`. Absorbing logarithms and the `o(1)` in Guth--Maynard into an arbitrarily small power, for every fixed `epsilon>0`,

\[
\boxed{
\mathfrak A_K(U)
\ll_\epsilon
M_K(U)^{\alpha_*(\sigma_0)-\epsilon}
}
\tag{12}
\]

for all sufficiently small `M_K(U)`.

Consequently the maximum atom and the full absolute packet mass still have the same algebraic-versus-superalgebraic dichotomy,

\[
\boxed{
M_K(U)=U^{-\omega(1)}
\quad\Longleftrightarrow\quad
\mathfrak A_K(U)=U^{-\omega(1)},
}
\tag{13}
\]

but the quantitative atom extracted from algebraic mass is stronger than in the original argument. If, for fixed `B>0` and `c>0`,

\[
\mathfrak A_K(U)\ge cU^{-B},
\tag{14}
\]

then the explicit Ingham form gives

\[
\boxed{
M_K(U)
\gg
U^{-B/\alpha_I(\sigma_0)}
(\log U)^{-5/\alpha_I(\sigma_0)},
}
\tag{15}
\]

while the current best power consequence is: for every fixed `eta>0`,

\[
\boxed{
M_K(U)
\gg_\eta
U^{-B/\alpha_*(\sigma_0)-\eta}.
}
\tag{16}
\]

Because `alpha_*>1/2`, the exponent `B/alpha_*` is strictly smaller than the previous `2B`. The strong atom is therefore forced at a quantitatively larger scale, not merely at some unspecified algebraic scale.

Finally,

\[
\mathcal S_K(U)
=
2\Re\sum_\rho a_{\rho,K}(U)e^{i\gamma U}
\tag{17}
\]

satisfies

\[
|\mathcal S_K(U)|\le2\mathfrak A_K(U),
\tag{18}
\]

so the same conclusions follow from an algebraic signed packet value. The diffuse algebraic cloud is still eliminated, now with a sharper atom exponent.

## 1. The coefficient envelope and the relevant zero count

The uniform coefficient asymptotic from `RE-124`--`RE-129` is

\[
a_{\rho,K}(U)
=
\frac{e^{-(\Theta-\beta)U}}{\rho(1-\rho)}
\left(1+O_K(U^{-1})\right),
\tag{19}
\]

uniformly on the fixed strip. Since `sigma_0<=beta<Theta<1`,

\[
|\rho(1-\rho)|
\asymp_{\sigma_0,\Theta}
1+\gamma^2,
\]

and the damping never exceeds one. Hence

\[
\boxed{
|a_{\rho,K}(U)|
\le
\frac{C_K}{1+\gamma^2}.
}
\tag{20}
\]

The original proof paired (20) with the count of all zeta zeros. For the packet in (3), however, the correct counting function is (4). Under (5), Stieltjes partial summation gives

\[
\sum_{\substack{\beta\ge\sigma_0\\ \gamma>T}}
\frac1{1+\gamma^2}
\ll
T^{\kappa-2}(\log T)^q
\qquad(T\ge2).
\tag{21}
\]

Indeed, replacing `1/(1+t^2)` by `O(t^-2)` on the tail,

\[
\int_{(T,\infty)}t^{-2}\,dN_{\sigma_0}(t)
\le
2\int_T^\infty N_{\sigma_0}(t)t^{-3}\,dt
\ll
T^{\kappa-2}(\log T)^q,
\tag{22}
\]

where `kappa<2` makes the integral converge. Edge zeros with `beta=Theta` may be included in `N_(sigma_0)` although they are absent from the subedge packet; this only enlarges the upper bound.

## 2. Density-aware maximum-versus-mass interpolation

Write

\[
M:=M_K(U)
\]

and set

\[
T:=M^{-1/2}.
\tag{23}
\]

For `0<gamma<=T`, maximality and (5) give

\[
\sum_{0<\gamma\le T}|a_{\rho,K}(U)|
\le
M N_{\sigma_0}(T)
\ll
M T^\kappa(\log T)^q.
\tag{24}
\]

For `gamma>T`, equations (20)--(21) give

\[
\sum_{\gamma>T}|a_{\rho,K}(U)|
\ll
T^{\kappa-2}(\log T)^q.
\tag{25}
\]

At the balancing scale (23), both right-hand sides are

\[
\asymp
M^{1-\kappa/2}
\left(\log\frac eM\right)^q,
\]

which proves (6).

Ingham's classical estimate

\[
N_{\sigma_0}(T)
\ll_{\sigma_0}
T^{3(1-\sigma_0)/(2-\sigma_0)}(\log T)^5
\tag{26}
\]

proves (9). Guth--Maynard give

\[
N_{\sigma_0}(T)
\le
T^{30(1-\sigma_0)/13+o(1)},
\tag{27}
\]

so taking the better exponent in (26)--(27) and absorbing the slowly varying factors into `M^-epsilon` proves (12).

The improvement has a simple structural origin. The `1/gamma^2` coefficient envelope still chooses the balancing height `T=M^-1/2`, but the number of available packet atoms below that height is only `T^(kappa+o(1))`, not `T^(1+o(1))`. The off-critical zero-density exponent therefore survives directly in the maximum-versus-mass power.

## 3. Algebraic mass forces a quantitatively stronger atom

Equation (13) follows immediately from (9), together with the trivial inequality `M_K(U)<=mathfrak A_K(U)`.

For (15), let `alpha=alpha_I(sigma_0)` and suppose (14). For a small fixed `D>0`, put

\[
M_0
:=
D
U^{-B/\alpha}
(\log U)^{-5/\alpha}.
\tag{28}
\]

For sufficiently large `U`, the function

\[
x\mapsto x^\alpha\left(\log\frac ex\right)^5
\]

is increasing on `(0,M_0]`, and

\[
M_0^\alpha
\left(\log\frac e{M_0}\right)^5
\le
C_{B,\alpha}D^\alpha U^{-B}.
\tag{29}
\]

If `M<=M_0`, (9) and (29) contradict (14) once `D` is chosen sufficiently small. This proves (15).

For (16), choose `epsilon>0` so small that

\[
\frac{B}{\alpha_*-\epsilon}
<
\frac{B}{\alpha_*}+\frac\eta2.
\]

Applying (12) and the same monotonicity argument yields

\[
M_K(U)
\gg
U^{-B/(\alpha_*-\epsilon)-\eta/2}
\gg
U^{-B/\alpha_*-\eta}.
\]

If instead

\[
|\mathcal S_K(U)|\ge cU^{-B},
\]

then (18) gives `mathfrak A_K(U)>=cU^-B/2`, so the same extraction applies.

## 4. Effect on the strong-atom branch

The qualitative conclusion of the original `RE-130` is unchanged: there is no independent algebraic many-weak-mode regime. What changes is the quantitative budget inherited by `RE-129` and `RE-131`.

Suppose the packet has algebraic absolute mass as in (14). From (16), for every fixed `eta>0`, a maximizing zero `rho_0=beta_0+i gamma_0` may be taken with

\[
|a_{\rho_0,K}(U)|
\gg
U^{-B/\alpha_*-\eta}.
\tag{30}
\]

Combining (30) with the universal height envelope (20) gives

\[
\boxed{
\gamma_0
\ll_\eta
U^{B/(2\alpha_*)+\eta}.
}
\tag{31}
\]

Thus the polynomial-height search range for the dominant atom is also sharpened. On a sublinear observation window, `RE-129` now applies with any atom exponent just above `B/alpha_*`, rather than just above `2B`. Under the stronger macroscopic hiding hypothesis of `RE-131`, the same improved atom enters the polylogarithmic reciprocal-scale, horizontally locked cancelling-doublet conclusion.

For the excursion branch, `RE-123` transfers an order-`U^-A` continuum excursion to regular CA states whenever `A<K+1`. The density-aware interpolation therefore reduces the sufficient order budget from the old condition `2B<K+1` to

\[
\boxed{
\frac{B}{\alpha_*(\sigma_0)}<K+1
}
\tag{32}
\]

up to an arbitrarily small exponent loss. This does not exclude the forced doublets, but it makes the strong-atom reduction materially tighter before zero-spacing geometry enters.

## 5. Adversarial audit

The strengthened argument was checked against the main failure modes.

First, the zero-density theorem is applied only to the fixed half-strip `beta>=sigma_0`; no shrinking-strip uniformity is assumed. The packet itself already lives in that strip. Second, the count includes multiplicity, and including the attained edge zeros only makes the upper bound larger. Third, the high-height contribution is controlled by Stieltjes partial summation of the same zero-density count, not by silently reusing the full `N(T)<<T log T` tail.

Fourth, `kappa_I(sigma_0)<1` for every fixed `sigma_0>1/2`, so the Ingham exponent gives a genuine improvement over the old square-root interpolation throughout the allowed strip. Guth--Maynard is used only through the minimum in (10); where its headline exponent is weaker, it is ignored. Fifth, none of these density estimates controls local zero spacing. Equations (6)--(16) strengthen the size of the atom that must participate in the `RE-129`--`RE-131` cancellation geometry; they do not claim that the required companion is impossible.

Finally, the inverse bounds do not promote algebraic packet mass `U^-B` to an atom of the same size. The unavoidable exponent is `B/alpha_*`, with `1/2<alpha_*<1` for the fixed strip. This quantitative loss remains explicit in every downstream use.

No material objection survives these checks, so no `.review.md` sidecar is opened.

## 6. Prior-art boundary

No new zero-density theorem is claimed. Equation (26) is Ingham's classical 1940 estimate, already anchored in `SOURCES.md`; equation (27) is the Guth--Maynard theorem published in *Annals of Mathematics* in 2026, also already anchored there. The literature audit additionally checked the modern explicit treatment of Ingham's bound and recent small-gap/vertical-distribution work. Those sources confirm the density and spacing boundaries but do not contain this Robin/CA packet interpolation.

The interpolation itself is elementary once the correct counting function is retained: split the packet at `T=M^-1/2`, use maximality below `T`, the `1/gamma^2` coefficient envelope above `T`, and the fixed-strip zero-density count on both pieces. No novelty is claimed for that general argument in isolation. The line-specific correction is that `RE-130` previously counted every zeta zero even though its packet is entirely off the critical line; retaining the actual arithmetic support strictly improves the atom scale inherited by the finite-edge Robin/CA analysis.

Recent results proving large proportions of simple critical-line zeros do not change this conclusion: they are density/proportion statements and do not exclude the sparse off-critical packet assumed in the false-RH finite-edge branch.

## 7. Research effect

`RE-130` still closes the diffuse-cloud escape, but now with the source-sensitive exponent that the branch actually provides. Algebraic packet mass cannot merely be reduced to some atom of exponent about `2B`; the fixed off-critical zero density forces an atom of exponent about `B/alpha_*<2B`, with correspondingly smaller polynomial ordinate height.

This strengthens every subsequent use of the dominant-atom branch without changing its logical frontier. `RE-131` still leaves the actual exclusion of phase-tuned, horizontally locked off-critical doublets open. The nonattained edge and `Theta=1` remain separate frontiers.