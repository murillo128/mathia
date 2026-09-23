# WI-417 — Bounded source density restores quadratic shallow-depth Blaschke coercivity

**Status:** `CLASSICAL-PRIOR-ART + EXACT-DERIVED + STRUCTURAL-CONSTRAINT`.

**Parents:** [WI-415](./WI-415-count-quantum-height-depth-budget-is-t-over-delta.md), [WI-416](./WI-416-oracle-blaschke-targeting-has-zero-tv-infimum.md).

## Claim

WI-416 showed that a finite discrete defect set has zero finite-TV cost if translated Blaschke probes may be placed atomically after seeing the targets: arbitrarily small coefficients can be compensated by moving a probe exponentially close to each logarithmic singularity. A uniform two-dimensional density cap removes that atomic escape, and in fact the resulting one-target capacity can be computed exactly.

For

\[
q_{a,b}(\gamma,d)
=\frac12\log
\frac{(\gamma-b)^2+(a+d)^2}
     {(\gamma-b)^2+(a-d)^2},
\qquad a,d>0,
\tag{1}
\]

fix a target `(\gamma,d)`, a required quantum `Q>0`, and a density cap `B>0`. Let `\nu` range over finite signed or complex measures on `(0,\infty)\times\mathbb R` that are absolutely continuous with respect to `da db` and satisfy

\[
\frac{d|\nu|}{da\,db}\le B
\quad\text{a.e.}
\tag{2}
\]

Define

\[
\mathcal M_B(d,Q)
=
\inf\left\{
\|\nu\|_{\rm TV}:
|Q_\nu(\gamma,d)|\ge Q
\right\},
\qquad
Q_\nu(\gamma,d)=\int q_{a,b}(\gamma,d)\,d\nu(a,b).
\tag{3}
\]

For `t>0` put

\[
R_{B,d}(t)
=
\pi B d^2
\left(
t\,\operatorname{csch}^2 t+\coth t-1
\right).
\tag{4}
\]

`R_{B,d}` is strictly decreasing from `+\infty` to `0`, so there is a unique `t_Q>0` with `R_{B,d}(t_Q)=Q`. Then the capacity is exactly

\[
\boxed{
\mathcal M_B(d,Q)
=
\pi B d^2\,\operatorname{csch}^2 t_Q.
}
\tag{5}
\]

Equivalently, if

\[
x=\sqrt{\frac{\mathcal M_B(d,Q)}{\pi B d^2}},
\qquad
\eta=\frac{Q}{\pi B d^2},
\tag{6}
\]

then `x` is the unique positive solution of

\[
\boxed{
\eta=H(x)
:=
x^2\operatorname{arsinh}(1/x)
+\sqrt{1+x^2}-1.
}
\tag{7}
\]

In particular,

\[
\boxed{
\frac{Q^2}{4\pi B d^2}
\le
\mathcal M_B(d,Q)
\le
\frac{(Q+\pi B d^2)^2}{4\pi B d^2}.
}
\tag{8}
\]

Hence, whenever `Q/(B d^2)\to\infty`,

\[
\boxed{
\mathcal M_B(d,Q)
\sim
\frac{Q^2}{4\pi B d^2}.
}
\tag{9}
\]

For fixed `B,Q`, this gives the sharp shallow-depth asymptotic

\[
\boxed{
\mathcal M_B(d,Q)
\sim
\frac{Q^2}{4\pi B}\,d^{-2}
\qquad(d\downarrow0).
}
\tag{10}
\]

The extremizer is positive: density `B` on one exact superlevel disk of the Blaschke kernel. Signed or complex coefficients cannot improve the optimum. Thus the `d^{-2}` exponent is not only order-sharp; the leading constant and full one-target capacity are fixed by the half-plane Green geometry.

No zero is excluded and no statement of RH follows. The missing zeta-specific step is still to derive an admissible source-side density bound such as (2) from arithmetic data, and then to control reuse of the same source budget across multiple exceptional zeros.

## 1. Exact superlevel geometry

Write `x=b-\gamma`. The inequality `q_{a,b}(\gamma,d)>t` is equivalent to

\[
x^2+a^2+d^2
<
2ad\,\coth t.
\tag{11}
\]

Completing the square in `a` gives

\[
\boxed{
\{q_{a,b}(\gamma,d)>t\}
=
\left\{
(a,b):
(a-d\coth t)^2+(b-\gamma)^2
<
d^2\operatorname{csch}^2 t
\right\}.
}
\tag{12}
\]

Thus every positive superlevel set is a Euclidean disk with center

\[
(d\coth t,\gamma)
\]

and radius

\[
d\,\operatorname{csch}t.
\]

The disk lies wholly inside the allowed source half-plane `a>0`, because its leftmost horizontal coordinate is

\[
d(\coth t-\operatorname{csch}t)
=
d\tanh(t/2)>0.
\tag{13}
\]

Therefore the distribution function of the exact Blaschke charge is

\[
\boxed{
A_d(t)
:=
\left|\{q_{a,b}(\gamma,d)>t\}\right|
=
\pi d^2\operatorname{csch}^2 t.
}
\tag{14}
\]

This is stronger than a radial majorant: it is the exact superlevel geometry of the original half-plane kernel.

## 2. Exact bathtub capacity

Let

\[
f(a,b)=\frac{d|\nu|}{da\,db},
\qquad
0\le f\le B,
\qquad
\int f=M:=\|\nu\|_{\rm TV}.
\tag{15}
\]

Positivity of the kernel gives

\[
|Q_\nu(\gamma,d)|
\le
\int q_{a,b}(\gamma,d)\,f(a,b)\,da\,db.
\tag{16}
\]

Layer cake and (14) imply

\[
\begin{aligned}
\int q f
&=
\int_0^\infty
\left(
\int_{\{q>t\}}f
\right)dt\\
&\le
\int_0^\infty
\min\{M,\,B A_d(t)\}\,dt.
\end{aligned}
\tag{17}
\]

There is a unique `t_M>0` with

\[
M
=
B A_d(t_M)
=
\pi B d^2\operatorname{csch}^2 t_M.
\tag{18}
\]

Because the superlevel sets of a function are nested, density

\[
f_M
=
B\,\mathbf 1_{\{q>t_M\}}
\tag{19}
\]

attains equality in (17) simultaneously at every layer. Hence the right side of (17) is the exact maximum response among all admissible signed or complex measures of TV mass `M`.

Using

\[
\int_{t_M}^{\infty}\operatorname{csch}^2 t\,dt
=
\coth t_M-1,
\]

the exact response envelope is

\[
\boxed{
\mathcal R_{B,d}(M)
=
M t_M
+
\pi B d^2(\coth t_M-1),
}
\tag{20}
\]

with `t_M` determined by (18). It is strictly increasing in `M`; equivalently, after setting

\[
x=\sqrt{\frac{M}{\pi B d^2}},
\qquad
t_M=\operatorname{arsinh}(1/x),
\tag{21}
\]

we obtain

\[
\boxed{
\mathcal R_{B,d}(M)
=
\pi B d^2 H(x),
}
\tag{22}
\]

where `H` is (7), and

\[
H'(x)
=
2x\,\operatorname{arsinh}(1/x)>0.
\tag{23}
\]

The unique mass for which the exact envelope equals `Q` is therefore precisely (5)--(7). The optimizing measure is the positive absolutely continuous measure with density (19), so the infimum in (3) is attained.

## 3. Sharp quadratic scale and constants

The implicit capacity yields simple global bounds. Since

\[
\operatorname{arsinh}(1/x)\le\frac1x,
\qquad
\sqrt{1+x^2}-1\le x,
\]

we have

\[
H(x)\le2x.
\tag{24}
\]

For the reverse estimate needed here, use

\[
\operatorname{arsinh}(1/x)
=
\int_0^{1/x}\frac{du}{\sqrt{1+u^2}}
\ge
\frac1{\sqrt{1+x^2}}.
\tag{25}
\]

Then

\[
\begin{aligned}
H(x)
&\ge
\frac{x^2}{\sqrt{1+x^2}}
+\sqrt{1+x^2}-1\\
&=
\frac{2x^2+1}{\sqrt{1+x^2}}-1\\
&\ge
2x-1,
\end{aligned}
\tag{26}
\]

because `(2x^2+1)^2-4x^2(1+x^2)=1`.

Applying `2x-1\le H(x)\le2x` to (7) gives

\[
\frac{\eta}{2}
\le x\le
\frac{\eta+1}{2}.
\tag{27}
\]

Multiplying by `\pi B d^2` after squaring proves (8). When `\eta\to\infty`, (27) gives `x\sim\eta/2`, proving (9). In particular the optimal shallow-depth leading constant is `1/(4\pi)`, not merely an unspecified constant hidden in `\Theta(d^{-2})`.

The exact formula also identifies the density-scale transition. For fixed `Q`, if

\[
B(d)d^2\to0,
\]

then (9) forces `\mathcal M_{B(d)}(d,Q)\to\infty`. A cap at the critical scale `B(d)\asymp d^{-2}` can leave a finite positive cost, while allowing `B(d)d^2\to\infty` drives the exact capacity back toward zero. Thus `d^{-2}` is the genuine source-density crossover between coercive and increasingly oracle-like concentration.

## 4. Stress tests and what this does not buy

The theorem remains a **one-target** statement. One source distribution can contribute to many exceptional zeros, so the exact capacity (5) cannot be summed over zeros without an additional packing, transport, separation, near-orthogonality, or source-allocation theorem. The sharpening of the one-target constant does not by itself produce a stronger simple-critical-zero proportion or an RH implication.

The density hypothesis is genuinely two-dimensional. Atomic measures, measures on curves, or source representations with no `L^\infty(da\,db)` control lie outside (2), and WI-416 remains the correct obstruction for unrestricted target-adaptive atoms. The exact superlevel disks make this boundary especially explicit: the optimum under a density cap is obtained by saturating a two-dimensional neighborhood of the logarithmic pole; collapsing that neighborhood to a singular source is exactly the escape that the cap forbids.

No current zeta-side theorem in this line supplies (2) with a useful `B(d)`. The arithmetic problem therefore remains upstream of the capacity calculation. Even if such a cap were proved, a global defect-to-zero bootstrap would still need a multiple-target theorem preventing the same admissible source mass from paying repeatedly for many defects.

Finally, (5) is specific to the linear translated-Blaschke response and an `L^\infty` density cap measured against Euclidean `da db`. Different source norms, singular measures, nonlinear observables, or renormalized infinite-budget constructions are not controlled by this extremal problem.

## 5. Prior-art and novelty audit

The ingredients are classical. The layer-cake/bathtub principle is standard rearrangement theory; a classical reference is H. J. Brascamp, E. H. Lieb, and J. M. Luttinger, *A general rearrangement inequality for multiple integrals*, Journal of Functional Analysis **17** (1974), 227--237, DOI `10.1016/0022-1236(74)90013-5`. The exact disks in (12) are the elementary Apollonius-circle level sets of a half-plane logarithmic Green/Blaschke kernel. The zeta/half-plane factorization itself is already anchored in WI-409--WI-416 through Kunik and the Balazard--Saias--Yor lineage.

A targeted search around half-plane Green/Blaschke level sets, Poisson-kernel translates, rearrangement/bathtub extremals, and bounded-density potential estimates found classical ingredients but no reason to make a priority claim for the general potential-theory mechanism. None is made. The line-specific result recorded here is the exact specialization relevant to the WI-416 regularity escape: the original translated-Blaschke kernel has an explicitly computable bounded-density one-target capacity, with positive extremizer and sharp leading constant `1/(4\pi)`.

The result is stronger than a generic Riesz-potential interpolation estimate because it uses the exact distribution function (14), not a radial majorant. Its mathematical role in `weil_inertia` is correspondingly narrow: it completely solves the one-target `L^\infty` source-capacity problem while leaving the zeta-specific source-regularity and multiple-target reuse questions untouched.

## Consequence

The Blaschke branch now has an exact third regime between WI-415 continuum coverage and WI-416 atomic oracle targeting:

\[
\boxed{
\text{one discrete target}
+\text{2D source-density cap }B
\Longrightarrow
\mathcal M_B(d,Q)
=
\pi B d^2\operatorname{csch}^2 t_Q,
}
\tag{28}
\]

where `t_Q` is determined by (4). In the shallow coercive regime this becomes

\[
\boxed{
\mathcal M_B(d,Q)
\sim
\frac{Q^2}{4\pi B d^2}.
}
\tag{29}
\]

So the one-target regularity gate itself is no longer a source of constant-factor slack. Any further progress on this branch must derive source regularity from arithmetic information, control budget reuse across multiple defects, or leave the linear translated-Blaschke architecture.
