# ANF-135 — origin curvature prevents faster-than-factorial copy-rate saturation

**Status:** `EXACT-DERIVED + DEPTH-QUANTITATIVE-INVARIANT + POSITIVE-TRANSLATION-CASCADE + ORIGIN-CURVATURE-BUDGET + FACTORIAL-SLACK-LOWER-BOUND + DIAGONAL-DEPTH-WINDOW`. `ANF-134` reduces much of the arbitrary-depth problem for the `ANF-133` positive saddle cascade to two questions: whether the residual copy-rate slack

\[
\delta_d=f_\gamma-2R_d
\]

can be exhausted, and whether source prefactors remain controlled when the chamber count and depth grow. The first question admits a quantitative answer. For every fixed-`q` critical seed from `ANF-129`, the successive first-critical retunings of `ANF-133` cannot drive `\delta_d` to zero arbitrarily fast. There are constants `c,C>0`, depending only on the fixed seed parameters, such that once `\delta_d` enters a fixed small neighborhood of zero,

\[
\boxed{
\delta_{d+1}
\ge
c\,\frac{\delta_d}
{1+\log(\delta_0/\delta_d)}.
}
\tag{1}
\]

Consequently

\[
\boxed{
\log\frac{\delta_0}{\delta_d}
\le
C(d+1)\log(d+2),
\qquad
\delta_d
\ge
\delta_0\exp[-C(d+1)\log(d+2)].
}
\tag{2}
\]

Thus the scalar budget may still tend to zero, but no faster than a factorial-type scale `exp[-O(d log d)]`. The mechanism is the fixed positive slope at the origin. Every source-critical pressure satisfies

\[
G_d(0)=-\delta_d,
\qquad
G_d'(0)=1,
\qquad
G_d\le0,
\tag{3}
\]

so a tiny origin deficit requires enough negative curvature to bend the graph back below zero. The historical annihilator curvature cannot grow freely: `ANF-134` already bounds its accumulated translation span by `log(\delta_0/\delta_d)`, and on the zero-free origin interval this converts directly into the curvature bound that yields (1).

This is weaker than proving a positive residual slack. It does, however, rule out superfactorial or iterated-exponential budget saturation and opens a genuine pressure-level diagonal regime. If `D=D(A)` satisfies

\[
D(A)\log(D(A)+2)=o(\log A),
\tag{4}
\]

then

\[
\delta_{D(A)}=A^{-o(1)},
\tag{5}
\]

every annihilator shift is `A^{o(1)}`, and the accumulated annihilator translation span is `A^{1+o(1)}`. What still prevents this from being a complete diagonal construction is exactly the other gate isolated by `ANF-134`: chamber proliferation and finite-`A` floor/Laplace-prefactor errors are not controlled by (1)--(5).

## 1. The fixed-`q` seed has a uniform smooth origin chamber

Fix `gamma>0` and a sufficiently large fixed digit arity `q` from `ANF-129`. Keep

\[
F_\gamma(\alpha)
=\alpha+2\gamma\log\cos\frac{\pi\alpha}{2},
\qquad
f_\gamma=\max F_\gamma,
\]

and the critically tuned digit pressure

\[
B_q(\alpha)
=
F_\gamma(\alpha)-f_\gamma
+2r_q\log|D_q(d_q\alpha)|,
\tag{6}
\]

where

\[
D_q(x)=\sum_{v=0}^{q-1}e^{-2\pi i vx},
\qquad
d_q=\frac{q-1}{qa}.
\]

Its copy-rate slack is

\[
\delta_0
:=f_\gamma-2r_q\log q>0,
\tag{7}
\]

so

\[
B_q(0)=-\delta_0,
\qquad
B_q'(0)=1.
\tag{8}
\]

The first positive zero of the digit factor occurs at

\[
\zeta_q
=\frac{1}{qd_q}
=\frac{a}{q-1}>0.
\tag{9}
\]

Because `q` is fixed, `B_q` is smooth on `[0,\zeta_q)`. Hence there are fixed constants

\[
0<\bar\delta_q
<\min(\delta_0,\zeta_q,1),
\qquad
C_q<\infty,
\tag{10}
\]

such that

\[
B_q''(\alpha)\ge-C_q
\qquad
(0\le\alpha\le\bar\delta_q/2).
\tag{11}
\]

The small positive digit zeros closer to the origin than the original saddle therefore cause no difficulty in the saturation regime: if the slack never falls below `\bar\delta_q`, there is already a positive residual bound; if it does, all later local arguments take place strictly before the first digit zero.

## 2. Historical annihilator curvature is paid for by accumulated span

Write the stage-`d` limiting pressure from `ANF-133` as

\[
G_d(\alpha)
=
B_q(\alpha)
+2\sum_{k=1}^{d}
\theta_k
\sum_{j=1}^{J_{k-1}}
\log\left|
1+e^{-2\pi i\tau_{j,k-1}\alpha}
\right|,
\tag{12}
\]

where

\[
\tau_{j,k-1}=\frac1{2\xi_{j,k-1}}
\]

and `xi_{j,k-1}` ranges over the positive critical skeleton at stage `k-1`. The retuning law is

\[
\delta_k
=
\delta_{k-1}
-2\theta_kJ_{k-1}\log2.
\tag{13}
\]

Set

\[
L_d:=\log\frac{\delta_0}{\delta_d}.
\tag{14}
\]

`ANF-134` gives

\[
\xi_{j,k-1}\ge\delta_{k-1}.
\tag{15}
\]

Since the slack decreases with the depth, for every `k\le d`,

\[
\tau_{j,k-1}
\le\frac1{2\delta_{k-1}}
\le\frac1{2\delta_d}.
\tag{16}
\]

The normalized translation span spent by the historical annihilator layers is

\[
S_d
:=
\sum_{k=1}^{d}
\theta_k\sum_{j=1}^{J_{k-1}}\tau_{j,k-1}.
\tag{17}
\]

Using (13) and (15),

\[
\begin{aligned}
S_d
&\le
\sum_{k=1}^{d}
\frac{\theta_kJ_{k-1}}{2\delta_{k-1}}\\
&=
\frac1{4\log2}
\sum_{k=1}^{d}
\frac{\delta_{k-1}-\delta_k}{\delta_{k-1}}\\
&\le
\boxed{
\frac1{4\log2}L_d.
}
\end{aligned}
\tag{18}
\]

This is the limiting-density form of the span law in `ANF-134`.

Now suppose `\delta_d\le\bar\delta_q` and restrict to

\[
0\le\alpha\le\frac{\delta_d}{2}.
\tag{19}
\]

For every historical binomial factor, (15) implies

\[
\left|
\pi\tau_{j,k-1}\alpha
\right|
\le\frac\pi4.
\]

Writing

\[
\ell_\tau(\alpha)
:=
\log|1+e^{-2\pi i\tau\alpha}|
=
\log2+\log|\cos(\pi\tau\alpha)|,
\]

one has on this interval

\[
\ell_\tau''(\alpha)
=-\pi^2\tau^2\sec^2(\pi\tau\alpha)
\ge-2\pi^2\tau^2.
\tag{20}
\]

Hence the total historical annihilator curvature obeys

\[
\begin{aligned}
G_d''(\alpha)
&\ge
-C_q
-4\pi^2
\sum_{k=1}^{d}
\theta_k\sum_j\tau_{j,k-1}^2\\
&\ge
-C_q
-\frac{2\pi^2}{\delta_d}S_d\\
&\ge
\boxed{
-C_q
-\frac{\pi^2}{2\log2}
\frac{L_d}{\delta_d}.
}
\end{aligned}
\tag{21}
\]

The chamber count has disappeared. Many old saddles can create large curvature only by paying translation span, and that span was already paid out of the logarithmic slack budget.

## 3. The next retuning layer cannot bend the origin arbitrarily sharply

Let the stage-`d` critical skeleton have `J_d` points and annihilator

\[
Q_d(\alpha)
=
\prod_{j=1}^{J_d}
\left(1+e^{-2\pi i\alpha/(2\xi_{j,d})}
\right).
\tag{22}
\]

For a prospective density `0\le\theta\le\theta_{0,d}`, where the origin-saturation density from `ANF-133` is

\[
\theta_{0,d}
=
\frac{\delta_d}{2J_d\log2},
\tag{23}
\]

put

\[
H_{d,\theta}(\alpha)
=G_d(\alpha)+2\theta\log|Q_d(\alpha)|.
\tag{24}
\]

Again `xi_{j,d}>=delta_d`, so (20) applies on (19). Moreover,

\[
\theta\sum_j\tau_{j,d}
\le
\theta_{0,d}\frac{J_d}{2\delta_d}
=
\frac1{4\log2},
\tag{25}
\]

and therefore

\[
4\pi^2\theta\sum_j\tau_{j,d}^2
\le
\frac{\pi^2}{2\delta_d\log2}.
\tag{26}
\]

Combining (21) and (26), and shrinking `\bar\delta_q` if needed, there is a fixed `K_q>=1` such that for every stage with `\delta_d\le\bar\delta_q`, every `0\le\theta\le\theta_{0,d}`, and every `0\le\alpha\le\delta_d/2`,

\[
\boxed{
H_{d,\theta}''(\alpha)
\ge
-K_q\frac{1+L_d}{\delta_d}.
}
\tag{27}
\]

Let `theta_{d+1}` be the first positive critical density of `ANF-133`. Then

\[
H_{d,\theta_{d+1}}=G_{d+1},
\qquad
\sup G_{d+1}=0.
\]

At the origin,

\[
G_{d+1}(0)=-\delta_{d+1},
\qquad
G_{d+1}'(0)=1.
\tag{28}
\]

Choose

\[
x_d
=
\frac{\delta_d}
{2K_q(1+L_d)}.
\tag{29}
\]

Then `x_d<=delta_d/2`, and (27) gives the Taylor lower bound

\[
\begin{aligned}
G_{d+1}(x_d)
&\ge
-\delta_{d+1}
+x_d
-\frac12K_q\frac{1+L_d}{\delta_d}x_d^2\\
&\ge
-\delta_{d+1}+\frac34x_d.
\end{aligned}
\tag{30}
\]

But `G_{d+1}(x_d)<=0` by source criticality. Therefore

\[
\boxed{
\delta_{d+1}
\ge
\frac{3}{8K_q}
\frac{\delta_d}{1+L_d},
}
\tag{31}
\]

which is (1).

The fixed slope in (28) is load-bearing. If positive-translation symmetry did not force the logarithmic-modulus derivative of every factor to vanish at the origin, the pressure could flatten there and the argument would give no lower bound on the next slack.

## 4. Saturation is at worst factorial-scale

Taking logarithms of (31) gives, after absorbing the fixed constant,

\[
L_{d+1}
\le
L_d+\log(1+L_d)+C_q'.
\tag{32}
\]

If the sequence never reaches `\bar\delta_q`, it already has a positive residual slack. Otherwise the value of `L_d` at the first crossing is bounded by a fixed seed-dependent constant, and the elementary recursion (32) yields by induction

\[
\boxed{
L_d
\le
C_q''(d+1)\log(d+2).
}
\tag{33}
\]

Equation (2) follows. Thus the first-critical retuning sequence may in principle satisfy `delta_d->0`, but it cannot spend the remaining copy-rate budget in a geometrically accelerating or iterated-exponential cascade.

Combining (33) with `ANF-134` gives two unconditional depth estimates for this architecture:

\[
\boxed{
\max_{j}\tau_{j,d}
\le
\frac1{2\delta_d}
\le
\exp[O_q(d\log(d+2))],
}
\tag{34}
\]

and

\[
\boxed{
\frac{\operatorname{Span}_{\rm ann}(d,A)}A
\le
\frac{L_d}{4\log2}
=O_q(d\log(d+2)).
}
\tag{35}
\]

The second estimate is much milder than the worst individual-shift bound: even if late annihilators become long, their allowed densities shrink with the same budget.

For a diagonal depth satisfying (4), (33)--(35) imply

\[
\delta_{D(A)}=A^{-o(1)},
\qquad
\max\tau_{j,D(A)}=A^{o(1)},
\qquad
\operatorname{Span}_{\rm ann}(D(A),A)=A^{1+o(1)}.
\tag{36}
\]

At the limiting-pressure level, `ANF-134` also gives

\[
G_{D(A)}(\alpha)
\le-\frac{\delta_{D(A)}}2
\qquad
\left(0\le\alpha\le\frac{\delta_{D(A)}}2\right),
\tag{37}
\]

so the central gap itself decays only subpolynomially in `A` in this diagonal regime.

Equation (37) must **not** be promoted to a finite-`A` source estimate without additional work. A floor `floor(theta_d A)` can lose one entire copy of a degree-`J_d` annihilator, and the unweighted chamber counts `J_d` are not controlled by the weighted budget `theta_d J_d`. The same problem affects uniform Laplace prefactors when critical chambers proliferate. Those are exactly the remaining depth-sensitive quantities identified in `ANF-134`.

## 5. Adversarial controls and prior-art boundary

The result is specific to the positive same-profile cascade of `ANF-129`--`ANF-133`. Signed or complex translation coefficients can change the origin derivative and destroy the positive-span bookkeeping. A different positive architecture with extra translations not paid through the `ANF-133` retuning law need not satisfy (18). The fixed-`q` hypothesis is also used: it supplies the nonzero zero-free interval (9) on which the seed curvature is bounded. Letting `q=q_d` grow with depth would require adding the shrinking first digit zero to the budget.

The estimate does not prove `inf_d delta_d>0`; `exp[-C d log d]` still tends to zero. Nor does it establish a fatal Montgomery--Taylor near-extremizer at depth `D(A)->infinity`. Its durable content is narrower: **copy-rate saturation itself cannot be the source of an arbitrarily fast depth catastrophe**. Any failure inside the slow diagonal window (4) must come from the uncontrolled chamber/prefactor/floor sector, or from a different architecture outside the hypotheses.

A direct falsification test is to construct a valid fixed-`q` `ANF-133` first-critical sequence with

\[
\log(\delta_0/\delta_d)
\gg d\log d.
\]

Such a sequence would force a failure in one of the load-bearing inputs above: `xi>=delta`, the logarithmic span law, the zero-free origin interval, the explicit binomial curvature, or the fixed origin slope.

A directed prior-art audit against classical Riesz products, generalized positive trigonometric products, characteristic-function curvature, and standard trigonometric-polynomial derivative estimates found the ambient ingredients but not this retuning statement. The facts that positive trigonometric factors are bounded by their coefficient mass and that logarithmic Fourier curvature is controlled by translation variance/span are classical; no external theorem is imported in (18)--(33). The Mathia-specific step is to combine those local facts with the `ANF-133` first-critical density and the `ANF-134` slack/span identity to obtain the recursive lower bound (31). No novelty claim is made beyond that internal derived consequence, and no `SOURCES.md` change is required.

The theorem surface is elementary enough that a separate Lean handoff would mostly formalize one-variable calculus and a scalar recurrence rather than test the live analytic bottleneck. The higher-value next target remains the finite-`A` source-prefactor/chamber-count problem.

## Consequence for `analytic_frontier`

`ANF-134` left two tightly coupled arbitrary-depth gates. `ANF-135` partially closes the scalar one: even if the copy-rate ceiling is eventually saturated, it is approached no faster than `exp[-O(d log d)]`. This supplies a broad diagonal depth range in which slack, critical-skeleton location, shifts, and total translation geometry remain subpolynomially controlled on the `A` scale.

The next decisive question is therefore more focused. One should test whether the proliferating critical skeleton admits a depth-uniform or slowly growing bound strong enough to absorb the `floor(theta_d A)` errors and preserve a two-sided source estimate along some `D(A)` satisfying (4). A failure there would be a genuine prefactor/combinatorial obstruction rather than hidden collapse of the scalar copy-rate budget.