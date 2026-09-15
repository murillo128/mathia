# NB-133 — zero-count visibility and Vinogradov–Korobov depth still permit superpolynomial annihilator collapse

**Status:** `EXACT-DERIVED + MATCHED-CONTROL + NB-132-ROUTE-BOUNDARY + ZERO-COUNT-RANK-CAP + VINOGRADOV-KOROBOV-COMPATIBLE + SUPERPOLYNOMIAL-ANNIHILATOR-COLLAPSE + PHASE-CLUSTERING-BOTTLENECK + REPRESENTATION-AUDIT`.

`NB-132` removes one representation-level escape left after `NB-131`: for genuine zeta zeros in a fixed-width polynomial-height band, explicit zero counting bounds the confluent rank strongly enough that a complete `q`-geometric recurrence window is already visible inside the natural cutoff. The remaining question is quantitative conditioning. `NB-124` measures that conditioning by the normalized missing-root margin

\[
\mathfrak s_{F,q}
=(1-r)
\frac{|A_{F,q}(r)|^2}
{\sum_{j=0}^{d}|a_j|^2r^j},
\qquad
r=q^{-1},
\]

while `NB-125` supplies a Vinogradov–Korobov lower bound on the radial distance of each genuine root from the missing target root.

The obvious next splice would be to combine the logarithmic rank cap of `NB-132` with the Vinogradov–Korobov depth of `NB-125` and hope that the visible annihilator is then polynomially conditioned. That implication is false at the level of those two coarse source laws. There are simple formal packets in the same narrow polynomial-height regime, obeying even the short-window numerical rank allowance coming from the same explicit zero-count error and lying safely on the allowed side of the Vinogradov–Korobov zero-free boundary, for which the **exact** normalized annihilator margin is smaller than every power of the cutoff.

The obstruction is angular. Zero counting controls how many roots may occur in the band, and the zero-free region controls their radii, but neither prevents `Theta(log R)` sampled roots from occupying an `o(1)` phase arc around the missing root. Such a phase cluster makes the annihilator itself superpolynomially ill-conditioned even though its full recurrence is visible.

This is a matched-control result. The constructed points are not asserted to be zeta zeros. Its conclusion is therefore precise: **the rank information extracted in `NB-132` plus Vinogradov–Korobov horizontal depth cannot by themselves yield a polynomial lower bound for the `NB-124` margin.** Any successful conditioning theorem must import additional source-specific geometry, such as anti-clustering, spacing, multibase phase information, or another statistic that excludes this packet.

## 1. A recurrence-visible narrow-band matched packet

Fix an integer `q>=2` and constants `A>0`, `W>0` in the `NB-132` visibility regime

\[
\kappa_{A,W}
:=A\left(\frac{W}{4\pi}+0.10076\right)
<\frac1{\log q}.
\tag{1}
\]

Choose once and for all

\[
\boxed{
0<c<0.10076\,A.
}
\tag{2}
\]

This is deliberately stronger than merely requiring `c<kappa_(A,W)`. Since

\[
0.10076\,A<\kappa_{A,W}<\frac1{\log q},
\tag{3}
\]

it leaves both the recurrence budget and the shrinking-window zero-count error with room to spare.

For large `R`, put

\[
d_R:=\lfloor c\log R\rfloor.
\tag{4}
\]

Then

\[
\boxed{
d_R+1\le \log_q R
}
\tag{5}
\]

for all sufficiently large `R`. Thus a packet of rank `d_R` lies strictly inside the recurrence-visibility budget of `NB-132`.

Let

\[
T_q:=\frac{2\pi}{\log q}
\]

be the exact one-base alias period from `NB-126`. Choose an integer `m_R` so that

\[
G_R:=m_RT_q
=\frac12R^A+O_q(1).
\tag{6}
\]

Hence

\[
G_R\asymp R^A,
\qquad
G_R\log q\in2\pi\mathbb Z.
\tag{7}
\]

Use the same explicit Vinogradov–Korobov scale as `NB-125`, with `K_VK=53.989`, but stay a fixed factor to the left of the forbidden boundary:

\[
\eta_R
:=
\frac{2}
{K_{\rm VK}
(\log G_R)^{2/3}
(\log\log G_R)^{1/3}}.
\tag{8}
\]

Set

\[
\beta_R:=1-\eta_R,
\qquad
\delta_R:=\frac{\eta_R}{d_R\log q},
\tag{9}
\]

and define `d_R` distinct simple formal right-half points

\[
\rho_{j,R}
:=
\beta_R+i(G_R+j\delta_R),
\qquad
0\le j<d_R.
\tag{10}
\]

Their total vertical diameter is

\[
(d_R-1)\delta_R
<\frac{\eta_R}{\log q}
=o(1).
\tag{11}
\]

Therefore, for all large `R`, the whole packet lies in some interval `(T_R,T_R+W]` with

\[
T_R+W\le R^A.
\tag{12}
\]

For example one may take `T_R=G_R-\delta_R/2`; then `(11)` and `G_R=R^A/2+O_q(1)` make `(12)` automatic eventually.

The stronger choice `(2)` also survives a more adversarial zero-count check than the fixed-width statement of `NB-132`. If the Bellotti–Wong–Fiori zero-count estimate is reapplied directly to an interval of width `O(eta_R)=o(1)` around `G_R`, the main term contributes only `o(log R)`, while the two endpoint errors permit at most

\[
(0.20152\,A+o(1))\log R
\]

total zeros counted with multiplicity. Functional-equation symmetry pairs every right-half off-critical point with a left-half point at the same positive ordinate, so the corresponding right-half numerical allowance is

\[
(0.10076\,A+o(1))\log R.
\tag{13}
\]

Thus `d_R=c log R+O(1)` with `(2)` remains below the rank allowance even at the packet's actual shrinking vertical diameter. This does **not** turn the formal points into zeta zeros; it closes the loophole that the fixed-width count might reject them once its scale is refined.

The packet is simple: no multiplicity is used. If one wants the formal control to respect the elementary functional-equation and conjugation symmetries, adjoin the reflected points `1-\overline{\rho_{j,R}}` and both conjugates. The right-half positive-frequency packet `(10)`, which is the packet entering the `NB-124` annihilator, is unchanged.

## 2. The packet lies on the permitted side of the zero-free law

Bellotti's explicit Vinogradov–Korobov region, already used in `NB-125`, excludes actual zeros with

\[
1-\beta
\le
\frac1{K_{\rm VK}
(\log|\gamma|)^{2/3}
(\log\log|\gamma|)^{1/3}}.
\tag{14}
\]

For the points `(10)`, `|gamma|=G_R+o(1)`. Consequently

\[
\frac1{K_{\rm VK}
(\log|\gamma|)^{2/3}
(\log\log|\gamma|)^{1/3}}
=
\left(\frac12+o(1)\right)\eta_R.
\tag{15}
\]

Since

\[
1-\beta_R=\eta_R,
\tag{16}
\]

the formal roots are a factor asymptotically `2` farther left than the explicit forbidden boundary. Thus the zero-free law itself does not reject their horizontal location. Again this is only compatibility with the one-sided numerical constraint, not an assertion of existence of zeta zeros there.

The two coarse pieces of genuine-zero information currently available in this route therefore allow the same scales as the matched packet:

\[
d_R\asymp\log R,
\qquad
|\gamma|\asymp R^A,
\qquad
1-\beta_R
\asymp
(\log R)^{-2/3}
(\log\log R)^{-1/3}.
\tag{17}
\]

What they do not control is the angular arrangement of the sampled roots.

## 3. All sampled roots fit inside a Vinogradov–Korobov-sized arc around the missing root

Write

\[
r=q^{-1},
\qquad
\lambda_{j,R}
:=q^{-\overline{\rho_{j,R}}}.
\tag{18}
\]

Because `G_R log q` is an integer multiple of `2pi`, equations `(9)`--`(10)` give

\[
\lambda_{j,R}
=q^{-\beta_R}
\exp\!\left(
 i\,j\frac{\eta_R}{d_R}
\right).
\tag{19}
\]

Thus every characteristic root has radius

\[
|\lambda_{j,R}|
=q^{-1+\eta_R}
=rq^{\eta_R}
\tag{20}
\]

and angular displacement at most `eta_R` from the positive real axis.

Normalize the distance to the missing root by the root radius. Since

\[
\frac r{|\lambda_{j,R}|}=q^{-\eta_R},
\]

we have

\[
\begin{aligned}
\frac{|r-\lambda_{j,R}|}{|\lambda_{j,R}|}
&=
\left|
q^{-\eta_R}
-
\exp\!\left(i j\eta_R/d_R\right)
\right|\\
&\le
|1-q^{-\eta_R}|
+
\left|1-
\exp\!\left(i j\eta_R/d_R\right)
\right|\\
&\le
(\log q+1)\eta_R
\end{aligned}
\tag{21}
\]

for all sufficiently large `R`. Put

\[
C_q:=1+\log q.
\tag{22}
\]

Then

\[
\boxed{
|r-\lambda_{j,R}|
\le C_q\eta_R|\lambda_{j,R}|
\quad(0\le j<d_R).
}
\tag{23}
\]

This is the missing geometry. Neither the count envelope nor the radial zero-free envelope provides a lower bound on the mutual phase spacing needed to prevent `(23)` from holding simultaneously for logarithmically many roots.

## 4. The exact normalized annihilator margin collapses faster than every power

Let

\[
A_R(z)
:=
\prod_{j=0}^{d_R-1}(z-\lambda_{j,R})
=
\sum_{k=0}^{d_R}a_{k,R}z^k.
\tag{24}
\]

The `NB-124` normalized margin is

\[
\mathfrak s_R
:=(1-r)
\frac{|A_R(r)|^2}
{\sum_{k=0}^{d_R}|a_{k,R}|^2r^k}.
\tag{25}
\]

The numerator factors exactly. By `(23)`,

\[
|A_R(r)|
\le
(C_q\eta_R)^{d_R}
\prod_{j=0}^{d_R-1}|\lambda_{j,R}|.
\tag{26}
\]

For the denominator it is enough to keep the constant coefficient. Since

\[
a_{0,R}=(-1)^{d_R}
\prod_{j=0}^{d_R-1}\lambda_{j,R},
\]

we have

\[
\sum_{k=0}^{d_R}|a_{k,R}|^2r^k
\ge
|a_{0,R}|^2
=
\prod_{j=0}^{d_R-1}|\lambda_{j,R}|^2.
\tag{27}
\]

Combining `(25)`--`(27)` yields the exact conditioning upper bound

\[
\boxed{
\mathfrak s_R
\le
(1-r)(C_q\eta_R)^{2d_R}.
}
\tag{28}
\]

Now `G_R asymp R^A`, so `(8)` gives

\[
\log\eta_R
=
-\frac23\log\log R
-\frac13\log\log\log R
+O_{A,q}(1).
\tag{29}
\]

Together with `d_R=c log R+O(1)`, equation `(28)` gives

\[
\boxed{
\log\mathfrak s_R
\le
-\left(\frac{4c}{3}+o(1)\right)
\log R\log\log R.
}
\tag{30}
\]

Equivalently,

\[
\boxed{
\mathfrak s_R
\le
R^{-(4c/3+o(1))\log\log R}.
}
\tag{31}
\]

In particular, for every fixed `M>0`,

\[
\boxed{
\mathfrak s_R=o(R^{-M}).
}
\tag{32}
\]

This is not merely a weak lower bound failing to prove enough. The **exact normalized annihilator margin itself** can be superpolynomially small in a matched packet satisfying the same rank scale, polynomial-height scale and Vinogradov–Korobov horizontal-depth scale used by `NB-132` and `NB-125`.

At the same time `(5)` guarantees

\[
q^{d_R+1}\le R,
\tag{33}
\]

so the entire annihilating recurrence is visible in the natural cutoff. The failure is therefore conditioning, not hidden recurrence order.

## 5. What this rules out after `NB-132`

`NB-132` correctly restores **visibility** for genuine narrow polynomial-height zero packets. `NB-133` shows that visibility plus the present radial source law does not automatically restore **coercivity**. A proof based only on the following summaries cannot yield a polynomial lower bound for `mathfrak s_(F,q)`: a logarithmic upper bound on right-half packet rank of the size supplied by explicit zero counting, polynomial-height localization in a fixed or shrinking vertical band, the Vinogradov–Korobov lower bound on `1-beta`, and functional-equation/conjugation symmetry with multiplicity bookkeeping. The matched packet `(10)` obeys the corresponding numerical constraints while `(32)` defeats every polynomial lower bound.

The conclusion is deliberately about the `NB-124` certificate. Small `mathfrak s_R` does **not** by itself prove that the formal packet achieves near-perfect Nyman target capture; `NB-124` is a one-sided upper bound on capture. What `(32)` proves is that the current annihilator route cannot obtain the required polynomial separation from those coarse source inputs alone.

This sharply identifies the missing information. The construction uses a phase cluster of `Theta(log R)` simple roots in an arc of width `Theta(eta_R)`. A source-specific theorem can defeat it by proving enough angular anti-concentration for the actual sampled roots `q^{-\bar rho}`, by coupling several multiplicatively independent bases before taking scalar margins, by exploiting the growing natural-grid phase resolution of `NB-128`--`NB-129`, or by finding a different target-bearing functional whose conditioning does not multiply all rootwise distances.

The point is not that one of these routes must work. It is that **another zero-free estimate or a sharper count carrying only population and radial-depth information cannot close the gap by itself**. The missing theorem has to control arrangement, not only population and radial depth.

## 6. Adversarial and prior-art audit

Several possible failure modes were checked directly. No multiplicity loophole is used: every point in `(10)` is simple because `delta_R>0`, and the superpolynomial collapse comes from a growing cluster of distinct characteristic roots. The construction does not put the formal points inside Bellotti's forbidden region; the factor `2` in `(8)` leaves a fixed asymptotic safety margin on the allowed side. The coefficient normalization cannot rescue the certificate: equation `(27)` is a lower bound on the exact weighted coefficient norm, so `(28)` is an upper bound on the exact normalized margin, with no hidden Prony condition number.

The strongest count objection was also tested. Because the packet diameter is `o(1)`, it is not enough merely to compare `d_R` with the fixed-width coefficient in `NB-132`. Reapplying the same explicit `N(T)` error at the actual shrinking scale gives `(13)`, and the stricter choice `(2)` keeps the symmetrized matched packet below that allowance as well. Thus the construction is not exploiting a mismatch between the theorem's fixed `W` and the packet's much smaller width.

The one-base alias alignment is intentional. `NB-126` showed that a fixed base is blind to exact vertical alias lifts, while `NB-127`--`NB-129` showed why multibase or growing natural-grid information can recover height/phase information that one base loses. `NB-133` does not repeat that alias result: the new point is that even **after `NB-132` makes the full recurrence visible for genuine polynomial-height packets**, the count and Vinogradov–Korobov laws still allow a recurrence-visible formal packet whose normalized margin collapses superpolynomially.

A targeted external audit found the expected neighboring zero-free-region and zeta-zero-spacing literature but no unconditional theorem supplying the off-critical, shrinking-scale angular anti-clustering needed to reject `(10)`. Critical-line small-gap results generally impose RH or control different gap statistics, and a recent inverse theorem forcing many zeros into thin regions from large zeta sums does not supply a minimum-spacing or annihilator-conditioning estimate. No new external theorem is load-bearing for `(28)`--`(32)`: Bellotti's zero-free region and the Bellotti–Wong–Fiori zero-count estimate are already anchored in `SOURCES.md` through `NB-125` and `NB-132`, so no source-file update is required.

## Consequence

The frontier after `NB-132` is now narrower. **Recurrence visibility is solved in the narrow polynomial-height regime, but conditioning is not a consequence of zero count plus zero-free depth.** The next useful source-facing result must control the phase geometry of actual zeta roots strongly enough to prevent logarithmically many sampled roots from accumulating around the missing target root, or replace the fixed-base product margin by a statistic that retains the non-aliased information before conditioning is taken. Until such structure enters, the `NB-124` annihilator certificate can be superpolynomially noncoercive even though every recurrence coefficient it uses is fully visible inside the cutoff.