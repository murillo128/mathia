# WI-017 — convex lattice-gas optimality nearly closes the integer-lattice countermodel search

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-IDENTITY + DECISIVE-NEGATIVE` for the integer-lattice subclass of the collapsed single-profile Montgomery--Taylor Gram-defect interface isolated in WI-015--WI-016. The generalized-Wigner / most-homogeneous ground-state theorem is classical (Hubbard; Pokrovsky--Uimin; restated explicitly as Theorem 0 by Jędrzejewski--Miękisz). The new durable point for this line is that the exact integer Montgomery--Taylor defect potential satisfies those hypotheses, so the entire arbitrary-word search collapses to a one-variable mechanical-ground-state problem. An exact bracket then shows that WI-016's `450/667` witness is already within `2.69e-7` in density of the best possible countermodel on the unit lattice.

## 1. Scope

Retain the collapsed stability interface from WI-015--WI-016,

\[
S\ge HN+\mathcal D(M)-o(N),
\qquad
H=H_{\rm MT}
=\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2},
\tag{1}
\]

where `M` is the limiting Montgomery--Taylor Gram matrix of the retained simple critical-line atoms and

\[
\mathcal D(M)=\operatorname{tr}\Psi(M),
\qquad
\Psi(t)=
\begin{cases}
(t-1)^2,&0\le t\le2,\\
2t-3,&t\ge2.
\end{cases}
\tag{2}
\]

Restrict only for this finding to configurations whose normalized atom positions are a subset of the unit lattice `Z`. WI-015 proved that every finite Gram section of **any** such subset has spectrum strictly inside `(0,2)`: at integer displacement `j`,

\[
k(j)=\frac{(-1)^{j+1}}{2\pi^2j^2-1},
\qquad
w_j:=|k(j)|^2=\frac1{(2\pi^2j^2-1)^2},
\tag{3}
\]

and the off-diagonal row sum is less than `4/17`. Hence on the whole integer-lattice class the kink of `Psi` is never reached and

\[
\boxed{\mathcal D(M)=\operatorname{tr}(M-I)^2.}
\tag{4}
\]

Thus, if an occupied subset has asymptotic density `r`, its defect per retained atom is exactly twice the one-dimensional pair-interaction energy per particle for the potential `w_j`.

## 2. The Montgomery--Taylor integer potential is a strictly convex repulsive lattice-gas potential

Extend (3) to real `x>=1` by

\[
V(x):=\frac1{(Ax^2-1)^2},
\qquad A:=2\pi^2.
\tag{5}
\]

Then

\[
V'(x)=-\frac{4Ax}{(Ax^2-1)^3}<0,
\]

and

\[
\boxed{
V''(x)=\frac{4A(5Ax^2+1)}{(Ax^2-1)^4}>0
}
\qquad(x\ge1).
\tag{6}
\]

Also `V(j)>0` and `V(j)=O(j^{-4})`, so the interaction is positive, summable, decreasing and strictly convex on the lattice.

This is exactly the classical one-dimensional lattice-gas regime in which the canonical ground states at fixed particle density are the generalized Wigner lattices / most homogeneous configurations. Jędrzejewski--Miękisz state this explicitly as their Theorem 0 and attribute the original result to Hubbard and to Pokrovsky--Uimin. Their characterization is that, for every neighbor order `n`, the separations of `n`-th-nearest particles take only the two consecutive integer values allowed by the density.

Therefore **the mechanical configurations used in WI-016 are not merely good integer-lattice witnesses: they minimize the complete exact Gram defect among all unit-lattice configurations of the same density.**

## 3. Closed formula for the minimum full Gram defect at fixed lattice density

Let `0<r<1`. For the most-homogeneous ground state define

\[
q_n:=\left\lfloor\frac nr\right\rfloor,
\qquad
\theta_n:=\frac nr-q_n\in[0,1).
\tag{7}
\]

For a rational density `r=m/L`, extend the ordered occupied sites periodically by `x_{i+m}=x_i+L`. Most homogeneity gives

\[
x_{i+n}-x_i\in\{q_n,q_n+1\}.
\]

Averaging over one period,

\[
\frac1m\sum_{i=1}^m(x_{i+n}-x_i)=\frac{nL}{m}=\frac nr,
\]

so the fraction of `n`-th-neighbor separations equal to `q_n+1` is exactly `theta_n`. Consequently the minimum defect per retained atom is

\[
\boxed{
d_{\min}(r)
=2\sum_{n\ge1}
\Bigl((1-\theta_n)w_{q_n}+\theta_n w_{q_n+1}\Bigr).
}
\tag{8}
\]

The same formula is the energy of the unique most-homogeneous invariant measure at irrational density. The series converges absolutely.

If `e(r)` denotes the minimum pair energy **per lattice site**, then

\[
\boxed{r\,d_{\min}(r)=2e(r).}
\tag{9}
\]

Thus the existence of an integer-lattice countermodel to the collapsed interface (1) at density `r` is equivalent to the scalar condition

\[
\boxed{
G(r):=r\bigl(1-d_{\min}(r)\bigr)\ge H.
}
\tag{10}
\]

There is no remaining combinatorial optimization over periodic words.

## 4. The scalar feasibility function is strictly increasing

The threshold in (10) is well behaved. Let

\[
W:=\sum_{j\ge1}w_j.
\]

In a large finite periodic lattice, inserting one particle into any empty site increases the pair energy by at most `2W`, because there are at most two occupied sites at each absolute displacement `j`. Passing to canonical ground-state energy densities gives, for `r_2>r_1`,

\[
e(r_2)-e(r_1)\le 2W(r_2-r_1).
\tag{11}
\]

Moreover, from `pi>3`,

\[
w_j<\frac1{17^2j^4},
\qquad
W<\frac2{289}.
\tag{12}
\]

Using (9),

\[
\begin{aligned}
G(r_2)-G(r_1)
&=(r_2-r_1)-2\bigl(e(r_2)-e(r_1)\bigr)\\
&>\left(1-\frac8{289}\right)(r_2-r_1)\\
&=\boxed{\frac{281}{289}(r_2-r_1)>0.}
\end{aligned}
\tag{13}
\]

The same estimate gives Lipschitz continuity. Hence there is at most one lattice-density threshold `r_*` at which (10) changes from impossible to possible.

## 5. Exact lower side of the threshold: `r_* > 0.6746624`

Set

\[
r_0:=\frac{52708}{78125}=0.6746624.
\tag{14}
\]

First obtain a rational lower bound for the baseline. Put `x=1/sqrt(2)`. Alternating Taylor bounds give

\[
\cos x
\le \sum_{k=0}^{6}\frac{(-1)^kx^{2k}}{(2k)!}
=\frac{3329448031}{4379443200},
\]

and

\[
\frac{\sin x}{x}
\ge \sum_{k=0}^{5}\frac{(-1)^kx^{2k}}{(2k+1)!}
=\frac{391174153}{425779200}.
\]

Therefore

\[
x\cot x
<\frac{8274993}{10^7},
\]

because

\[
\frac{8274993}{10^7}
-
\frac{23306136217}{28164539016}
=
\frac{129453361}{35205673770000000}>0.
\]

Hence

\[
\boxed{H>\frac{6725007}{10^7}=0.6725007.}
\tag{15}
\]

For the defect use the classical upper enclosure `pi<355/113`, which gives the termwise lower bound

\[
\underline w_j
:=\frac1{\left(2(355/113)^2j^2-1\right)^2}
<w_j.
\tag{16}
\]

At `r_0`, write

\[
q_n=\left\lfloor\frac{78125n}{52708}\right\rfloor,
\qquad
\theta_n=\frac{78125n-52708q_n}{52708}.
\]

Keeping only the first twenty positive terms of (8), exact rational arithmetic gives

\[
2\sum_{n=1}^{20}
\Bigl((1-\theta_n)\underline w_{q_n}
+\theta_n\underline w_{q_n+1}\Bigr)
>
\boxed{\frac{10013}{3125000}=0.00320416.}
\tag{17}
\]

Thus

\[
\begin{aligned}
G(r_0)
&<\frac{52708}{78125}
\left(1-\frac{10013}{3125000}\right)\\
&<\frac{6725007}{10^7}<H,
\end{aligned}
\]

with the exact middle margin

\[
\frac{52708}{78125}
\left(1-\frac{10013}{3125000}\right)
-
\frac{6725007}{10^7}
=
\boxed{-\frac{102639}{3906250000000}<0.}
\tag{18}
\]

So no unit-lattice configuration of density at most `0.6746624` can satisfy the collapsed stability inequality.

## 6. WI-016 supplies the upper side: `r_* < 450/667`

WI-016 gives the period-667 mechanical word of density

\[
r_1:=\frac{450}{667}=0.674662668665667\ldots
\tag{19}
\]

and proves by rational estimates that its exact full defect satisfies

\[
G(r_1)>H.
\tag{20}
\]

Combining (13), (18) and (20) yields the exact bracket

\[
\boxed{
0.6746624
<r_*
<\frac{450}{667}
=0.674662668665667\ldots
}
\tag{21}
\]

whose width is

\[
\boxed{
\frac{450}{667}-\frac{52708}{78125}
=\frac{14}{52109375}
=2.68665667\ldots\times10^{-7}.
}
\tag{22}
\]

Therefore WI-016 is already within `0.00002687` percentage points of the strongest obstruction obtainable from **any** unit-lattice subset under this collapsed interface.

## 7. Prior art and novelty audit

The load-bearing optimization theorem is classical, not new.

- Hubbard (1978) and Pokrovsky--Uimin (1978) determined the one-dimensional repulsive strictly-convex lattice-gas ground states, the generalized Wigner lattices.
- Jędrzejewski--Miękisz (2000), Theorem 0, explicitly states that at fixed density the ground-state configurations for a positive strictly convex interaction are the most homogeneous configurations, and characterizes them by the two-consecutive-values property for every `n`-th-neighbor separation.
- Mechanical / balanced descriptions of these configurations are classical. WI-016 already recorded this surrounding prior art and used one explicit rational mechanical word.
- `trmdy/zeta-simple-zeros-673137`, `docs/campaign-2.md`, is direct zeta-side prior art for phase-locked balanced integer-gap adversaries, but reports a looser numerical pair-energy ceiling and does not supply the reduction (8)--(10) for the **full** collapsed `tr Psi` interface.

No novelty is claimed for generalized Wigner lattices, convex lattice-gas ground states, mechanical words, or the MT integer kernel. The line-specific deduction is the exact fit of the MT defect potential to the classical theorem, together with the scalar reduction and rational bracket (21).

## 8. Consequence and falsification boundary

This closes a weak route cleanly. Searching larger periods, different balanced words, simulated annealing over `1/2` gap patterns, or arbitrary binary periodic words on the **same unit lattice** cannot materially strengthen WI-016: the classical ground-state theorem already identifies the optimizer at every density, and the best possible density threshold is trapped in an interval of width `2.69e-7`.

It does **not** prove that `r_*` is a ceiling for the entire collapsed support-one interface. A stronger countermodel may use noninteger atom locations, and a stronger zeta theorem may escape the collapsed interface altogether through the uncollapsed exceptional block, zeta-specific spacing/correlation information, multiple genuinely independent profiles, or support greater than one.

The useful research consequence is therefore directional:

\[
\boxed{
\text{stop optimizing unit-lattice words;}
\quad
\text{look for non-lattice adversaries or genuinely new zeta information.}
}
\]

For the countermodel programme itself, (8) is also a reusable exact benchmark: any proposed numerical search over integer configurations should reproduce `d_min(r)` rather than treating the word optimization as an open computational problem.
