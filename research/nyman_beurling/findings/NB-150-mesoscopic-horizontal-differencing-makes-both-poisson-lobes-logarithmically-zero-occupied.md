# NB-150 — Mesoscopic horizontal differencing makes both Poisson lobes logarithmically zero-occupied

**Status:** `LITERATURE+DERIVED + SOURCE-SPECIFIC + SIGNED-POISSON + RIEMANN-VON-MANGOLDT + MESOSCOPIC-OBSTRUCTION + NB-149-FRONTIER`.

`NB-148` showed that cancelling the universal Hadamard `\frac12\log G` budget with a zero-mass signed exterior sampler necessarily creates an equal-integrated-mass negative Poisson lobe. `NB-149` then showed that controlling this lobe by Jordan domination merely restores the positive `Theta(log G)` budget. A natural location-sensitive escape remains: push the sign change far away from the target packet by moving the exterior sample points far to the right, so that the positive lobe becomes mesoscopically wide and perhaps the negative lobe lands where actual zeta zeros are harmless.

For the simplest and most favorable two-point horizontal difference, that escape fails for a stronger reason. Once the horizontal scale tends to infinity but remains `o(G)`, the Riemann--von Mangoldt law itself forces **both** lobes to be sampled by actual zeta zeros with asymptotic mass of order `log G`. The effect is unconditional, uses no RH or spacing hypothesis, and is independent of the horizontal coordinates of the zeros to first order. In particular, moving the negative lobe outward on any growing mesoscopic scale also broadens the positive lobe so much that an `O(log G)` target packet contributes a vanishing fraction of the positive zero mass.

Fix `c>1`. Let

\[
1\ll L=L_G=o(G),
\tag{1}
\]

and take the zero-mass signed exterior sampler

\[
\nu_G
=
\delta_{\,1+L+iG}
-
\delta_{\,1+cL+iG}.
\tag{2}
\]

For a nontrivial zeta zero `rho=beta+i gamma`, counted with multiplicity, define its signed zero-side charge

\[
Q_G(\rho)
:=
\frac{1+L-\beta}
{(1+L-\beta)^2+(G-\gamma)^2}
-
\frac{1+cL-\beta}
{(1+cL-\beta)^2+(G-\gamma)^2}.
\tag{3}
\]

Write

\[
q_c(x)
:=
\frac1{1+x^2}
-
\frac{c}{c^2+x^2}
=
\frac{(c-1)(c-x^2)}{(1+x^2)(c^2+x^2)}.
\tag{4}
\]

Then uniformly for every nontrivial zero, since `0<beta<1`,

\[
\boxed{
Q_G(\rho)
=
\frac1L
q_c\!\left(\frac{\gamma-G}{L}\right)
+
O_c\!\left(
\frac1{L^2}\,
\frac1{1+((\gamma-G)/L)^2}
\right).
}
\tag{5}
\]

The limiting profile is positive precisely on

\[
|x|<\sqrt c
\tag{6}
\]

and negative outside. Its positive and negative Lebesgue masses are exactly equal, as required by `NB-148`, and each is

\[
\boxed{
A_c
:=
\int_{\mathbb R}(q_c)_+(x)\,dx
=
\int_{\mathbb R}(q_c)_-(x)\,dx
=
4\arctan\sqrt c-\pi
>0.
}
\tag{7}
\]

The new source-specific statement is that the actual zeta zero set samples these two lobes at their mean Riemann--von Mangoldt density:

\[
\boxed{
\sum_{\substack{\zeta(\rho)=0\\ \gamma>0}}
\bigl(Q_G(\rho)\bigr)_+
=
\left(\frac{A_c}{2\pi}+o(1)\right)\log G,
}
\tag{8}
\]

and

\[
\boxed{
\sum_{\substack{\zeta(\rho)=0\\ \gamma>0}}
\bigl(Q_G(\rho)\bigr)_-
=
\left(\frac{A_c}{2\pi}+o(1)\right)\log G.
}
\tag{9}
\]

Thus the sign debt in this mesoscopic regime is not merely a possible `Theta(log G)` cost introduced by Jordan domination. **The true discrete zero set itself realizes a `Theta(log G)` negative lobe**, with the same leading mass as the positive lobe.

Moreover, any packet `F_G` of zeros satisfying

\[
|\gamma-G|=o(L)
\qquad(\rho\in F_G)
\tag{10}
\]

receives asymptotically constant positive charge per zero,

\[
Q_G(\rho)
=
\left(\frac{c-1}{c}+o(1)\right)\frac1L,
\tag{11}
\]

uniformly in `beta`. If `d_G` denotes its multiplicity-weighted rank, then

\[
\sum_{\rho\in F_G}Q_G(\rho)
=
\left(\frac{c-1}{c}+o(1)\right)
\frac{d_G}{L}.
\tag{12}
\]

Consequently, for the logarithmic confluence scale relevant to `NB-140`--`NB-149`,

\[
d_G=O(\log G),
\tag{13}
\]

the packet contributes only

\[
O\!\left(\frac{\log G}{L}\right)
=o(\log G),
\tag{14}
\]

whereas the full positive and negative lobes each carry `Theta(log G)` actual-zero mass. Multiplying the sampler `(2)` by `L` to restore order-one charge per target zero does not improve the ratio: it multiplies both background lobes to `Theta(L log G)`.

This closes the simplest idea of hiding the exported negative lobe by sending the exterior samples mesoscopically far to the right. Any successful signed exterior route must remain genuinely microscopic/nonuniform in ordinate, exploit exceptional zero placement at a scale where the global zero-count remainder is still relevant, use a more structured signed prime-side cancellation, or couple the signed expression directly to the Nyman target before the positive and negative zero masses are separated.

## 1. A smoothed Riemann--von Mangoldt sampling lemma

The load-bearing source theorem is already anchored in this line. Write

\[
N(T)
=
M(T)+E(T),
\qquad
M(T)
=
\frac{T}{2\pi}\log\frac{T}{2\pi e},
\qquad
E(T)=O(\log T),
\tag{15}
\]

with zeros counted with multiplicity. The explicit Bellotti--Wong--Fiori estimate in `SOURCES.md` is stronger than the form needed here.

Let `g` be a fixed nonnegative absolutely continuous function such that

\[
g(x)\ll (1+x^2)^{-1},
\qquad
\int_{\mathbb R}|g'(x)|\,dx<\infty.
\tag{16}
\]

For `L` satisfying `(1)`, define

\[
f_{G,L}(t)
:=
\frac1L g\!\left(\frac{t-G}{L}\right).
\tag{17}
\]

Then Stieltjes integration against `(15)` gives

\[
\boxed{
\sum_{\substack{\zeta(\rho)=0\\ \gamma>0}}
f_{G,L}(\gamma)
=
\frac{\log G}{2\pi}
\int_{\mathbb R}g(x)\,dx
+
O_g\!\left(
1+
\frac{\log G}{L}
+
\frac{L\log G}{G}
\right).
}
\tag{18}
\]

In particular the error is `o(log G)` whenever `(1)` holds.

To see `(18)`, first restrict to `G/2<=t<=3G/2`. Since

\[
M'(t)=\frac1{2\pi}\log\frac{t}{2\pi},
\tag{19}
\]

the main Stieltjes integral equals

\[
\frac{\log G}{2\pi}\int g
+
O_g\!\left(
1+
\frac{L}{G}\log\frac{G}{L}
\right).
\tag{20}
\]

For the remainder, integration by parts and `(16)` give

\[
\int_{G/2}^{3G/2} f_{G,L}(t)\,dE(t)
=
O_g\!\left(\frac{\log G}{L}ight),
\tag{21}
\]

with negligible boundary terms. Outside the central interval, `(16)` gives

\[
f_{G,L}(t)
\ll_g
\frac{L}{(t-G)^2},
\tag{22}
\]

and dyadic use of `N(T)\ll T\log T` yields total tail contribution

\[
O_g\!\left(\frac{L\log G}{G}\right).
\tag{23}
\]

Equations `(20)`--`(23)` prove `(18)`. This is only a smooth weighted consequence of the classical Riemann--von Mangoldt law; no new zero-density theorem is being claimed.

## 2. The two-point horizontal profile is asymptotically beta-blind

Put

\[
\theta:=1-\beta\in(0,1).
\tag{24}
\]

For `x=(gamma-G)/L`, the first term in `(3)` is

\[
\frac1L
\frac{1+\theta/L}{(1+\theta/L)^2+x^2},
\tag{25}
\]

and the second is

\[
\frac1L
\frac{c+\theta/L}{(c+\theta/L)^2+x^2}.
\tag{26}
\]

For

\[
F_a(x):=\frac{a}{a^2+x^2},
\tag{27}
\]

one has

\[
\left|\frac{\partial F_a(x)}{\partial a}\right|
=
\frac{|x^2-a^2|}{(a^2+x^2)^2}
\ll_c
\frac1{1+x^2}
\tag{28}
\]

uniformly for `a` in fixed neighborhoods of `1` and `c`. The mean-value theorem applied to `(25)`--`(26)` therefore gives `(5)`.

Let

\[
r(x):=(1+x^2)^{-1}.
\tag{29}
\]

Applying `(18)` to `r` shows that the sum over zeros of the error term in `(5)` is

\[
O_c\!\left(\frac{\log G}{L}\right)
=o(\log G).
\tag{30}
\]

Since `u->u_+` and `u->u_-` are 1-Lipschitz, the same error controls the positive and negative parts separately. Thus the horizontal coordinates `beta` of the actual zeros disappear from the leading mesoscopic lobe masses.

## 3. Exact lobe geometry and actual-zero occupation

Equation `(4)` immediately gives the sign boundary `(6)`. Because each Cauchy/Poisson kernel has integral `pi`,

\[
\int_{\mathbb R}q_c(x)\,dx=0.
\tag{31}
\]

The positive mass is computed explicitly:

\[
\begin{aligned}
A_c
&=
\int_{-\sqrt c}^{\sqrt c}
\left(
\frac1{1+x^2}
-
\frac{c}{c^2+x^2}
\right)dx\\
&=
2\arctan\sqrt c
-
2\arctan\frac1{\sqrt c}\\
&=
4\arctan\sqrt c-\pi,
\end{aligned}
\tag{32}
\]

which proves `(7)`. Both `(q_c)_+` and `(q_c)_-` satisfy the hypotheses of `(18)`. Hence

\[
\sum_\rho
\frac1L
(q_c)_\pm\!\left(\frac{\gamma-G}{L}\right)
=
\left(\frac{A_c}{2\pi}+o(1)\right)\log G.
\tag{33}
\]

Combining `(30)` and `(33)` proves `(8)` and `(9)`.

For `(11)`, condition `(10)` gives `x=o(1)`, so

\[
q_c(x)
=
q_c(0)+o(1)
=
1-\frac1c+o(1).
\tag{34}
\]

The uniform `O(L^{-2})` correction in `(5)` then proves `(11)`--`(14)`.

## 4. The prime side is not what kills this escape

The sampler `(2)` has total mass zero and both points have the same ordinate, so the universal leading Hadamard `\frac12\log G` term cancels exactly at the level isolated by `NB-148`. Moreover both samples lie deep in the Euler-product half-plane. From

\[
-\frac{\zeta'}{\zeta}(s)
=
\sum_{n\ge2}\frac{\Lambda(n)}{n^s},
\qquad \Re s>1,
\tag{35}
\]

one gets

\[
\left|\frac{\zeta'}{\zeta}(1+L+iG)\right|
+
\left|\frac{\zeta'}{\zeta}(1+cL+iG)\right|
=
O(2^{-L}).
\tag{36}
\]

Thus horizontal spreading makes the absolute prime-side cost extremely small. The obstruction in `(8)`--`(14)` is instead the zero geometry itself: on a growing scale `L`, ordinary Riemann--von Mangoldt density fills both lobes. The signed total can remain small because the two `Theta(log G)` pieces cancel each other, but that does not produce a positive certificate for one narrow target packet.

This distinction is important. `NB-149` said that **bounding** the adverse lobe positively costs `Theta(log G)`. Here, in a concrete mesoscopic family, the adverse lobe actually **contains** `Theta(log G)` discrete zero mass. No improvement of the Jordan estimate can remove that leading occupation.

## 5. Stress tests and boundaries

- **Fixed scale is not covered.** The proof needs `L->infinity` to make the `O(log G/L)` Riemann--von Mangoldt remainder negligible relative to the main `log G` lobe mass. For `L=O(1)`, the zero-count remainder is of the same order as the main term, so exceptional local zero placement remains possible. This is exactly where the live signed-location problem survives.
- **The theorem is two-point and horizontal.** It does not classify arbitrary many-point signed samplers, vertical differencing, or kernels whose positive and negative lobes shrink on zero-spacing scales.
- **No RH, simplicity, pair correlation, or zero-density input is used.** Multiplicity is handled by `N(T)`.
- **The result does not say every signed kernel is badly sampled.** It kills the specific strategy of moving the sign boundary outward through a growing horizontal Poisson scale while retaining a narrow target packet.
- **Rescaling weights does not help.** Multiplying `(2)` by any scalar multiplies the target charge and both lobe occupations by the same scalar.
- **The `o(G)` hypothesis matters.** It keeps the mesoscopic profile in a region where the mean zero density is asymptotically `\frac1{2\pi}\log G`. Macroscopic horizontal scales require a different normalization and are not classified here.

A direct falsification test is available: choose any fixed `c>1` and any explicit `L_G` with `L_G->infinity` and `L_G=o(G)`. If either lobe sum in `(8)`--`(9)` fails to have leading coefficient `A_c/(2pi)`, then either the uniform beta-blind expansion `(5)` or the weighted Riemann--von Mangoldt lemma `(18)` must fail. Both are explicit and independently auditable.

## 6. Prior-art and novelty audit

The weighted sampling lemma `(18)` is a routine consequence of the classical Riemann--von Mangoldt zero count, and no novelty is claimed for smooth zero counting. This line already anchors the stronger explicit Bellotti--Wong--Fiori estimate and uses short-interval consequences in `NB-112`, `NB-132`, and `NB-142`.

A structure-based literature search also found substantial classical and modern use of Poisson kernels in explicit-formula arguments. Carneiro and Milinovich, *On Littlewood's estimate for the modulus of the zeta function on the critical line* (2024, arXiv:2403.17803), and Chirre and Molero, *Explicit conditional bounds for zeta(s) at the edge of the critical strip* (Portugaliae Mathematica, 2026, DOI `10.4171/PM/2167`), combine Guinand--Weil explicit formulas with Poisson-kernel extremal approximations. Rodgers, *Tail bounds for counts of zeros and eigenvalues, and an application to ratios* (Comment. Math. Helv. 92 (2017), 311--347, DOI `10.4171/CMH/413`), studies much finer local zero-count statistics under RH. These works delimit the general Poisson/zero-count landscape; none is load-bearing for `(5)`--`(14)`.

The Mathia-specific delta is narrower: apply the already classical mean zero density to the **zero-mass two-point exterior sampler forced by the `NB-148` signed escape**, keep the horizontal coordinates of all actual zeros rather than assuming RH, and show that making the sign change mesoscopic forces both lobes to acquire equal logarithmic discrete occupation while an `O(log G)` narrow confluence packet becomes negligible. This is a source-specific route obstruction, not a new general theorem on zeta zero statistics. No new `SOURCES.md` dependency is required.

## 7. Consequence for the Nyman--Beurling frontier

`NB-148`--`NB-149` left open whether location sensitivity could repay the signed-lobe debt without reverting to positive domination. `NB-150` separates one regime cleanly:

\[
\boxed{
L_G\to\infty,\quad L_G=o(G)
\quad\Longrightarrow\quad
\text{two-point horizontal signed localization is background-dominated.}
}
\tag{37}
\]

The negative lobe cannot be made harmless merely by pushing it farther away, because the Riemann--von Mangoldt background fills it at exactly the same leading logarithmic scale as the positive lobe. At the same time, a logarithmic-rank target packet contributes only `O(log G/L_G)` before normalization.

Therefore the surviving signed route is now more local than `NB-149` alone implied. It must exploit fixed or shrinking ordinate scales where the zero-count remainder can compete with the mean density, use a kernel whose adverse support is tied to genuinely exceptional source information, retain cancellation against the prime side, or connect the signed expression to target-bearing Nyman data before lobe separation. **Mesoscopic smoothing is not the missing location-sensitive resource.**