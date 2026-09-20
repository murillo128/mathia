# NB-244 — Ramachandra–Révész clustering turns on beyond the Ford window

**Date:** 2026-09-20  
**Status:** `LITERATURE+DERIVED + FRESH-PRIOR-ART-AUDIT + ZETA-SPECIFIC-SCALE-AUDIT + NEGATIVE/METHOD-BOUNDARY + NB-243-FRONTIER`.

`NB-243` reduces the surviving source problem to a deterministic, Ford-depth-marked pair energy inside a height window of width

\[
W_F:=\frac1H=\frac JR,
\qquad
R:=Q^{2/3}(\log Q)^{1/3},
\qquad
Q:=\log(10+|t|),
\]

with `1 << J <= log Q`, carrier scale `1/X asymp 1/R`, and critical horizontal depth

\[
1-\beta=\frac{\log J+O(1)}X,
\qquad X\asymp R.
\]

A natural zeta-specific tool to test next is the classical near-one **zero-clustering** mechanism of Ramachandra, in the clean quantitative form proved by Révész. It is unusually relevant because, unlike ordinary zero-density estimates, it starts from one actual zero close to the one-line and forces weighted companion-zero mass near the same height and its double.

The exact Ford substitution shows a sharp limitation. The theorem's lower bound becomes non-vacuous only when its disk radius satisfies

\[
\boxed{
\lambda\gtrsim
\frac{(\log Q)(\log J)}R.
}
\]

But the whole Ford window has radius only `J/R`. Hence in the conservative transition regime

\[
\boxed{
\frac{\lambda_{\rm useful}}{W_F}
\gtrsim
\frac{(\log Q)(\log J)}J
\ge \log J
\longrightarrow\infty.
}
\]

At the Ford-window radius itself, Révész's forcing term is only `O(1/log J)` and the theorem's fixed subtractive constant makes the conclusion vacuous. At one carrier cell it is smaller still, `O(1/(log Q log J))`.

So this old near-one theorem is substantially finer than the unit-scale clustering methods audited earlier, but it still cannot see the current deterministic block. More strongly, every radius at which it yields positive information already contains a diverging number of complete Ford windows. The additional `2 gamma_0` alternative means that even this coarse companion mass need not occur in the selected block at all.

## 1. Ford variables and the critical zero

Use the notation stabilized in `NB-230`--`NB-243`:

\[
Q:=\log(10+|t|),
\qquad
L:=\log Q,
\qquad
R:=Q^{2/3}L^{1/3},
\tag{1}
\]

\[
X:=YR,
\qquad
J:=\frac RH,
\qquad
Y\asymp1,
\qquad
1\ll J\le L.
\tag{2}
\]

A zero in the critical Ford layer has

\[
\rho_0=\beta_0+i\gamma_0,
\qquad
|\gamma_0-t|\lesssim \frac JR,
\tag{3}
\]

and bounded Ford depth

\[
d_0:=X(1-\beta_0)-\log J=O(1).
\tag{4}
\]

Thus, writing

\[
\delta_0:=1-\beta_0,
\]

we have

\[
\boxed{
\delta_0
=
\frac{\log J+d_0}{X}
\asymp
\frac{\log J}{R}.
}
\tag{5}
\]

Because `J<=L`,

\[
\delta_0\log\log\gamma_0
\asymp
\frac{L\log J}{R}
\longrightarrow0.
\tag{6}
\]

In particular the critical Ford layer lies well inside the near-one range required by the clustering theorem below.

The two relevant vertical scales are

\[
\boxed{
W_F:=\frac1H=\frac JR
}
\tag{7}
\]

for the full selected Ford window and

\[
\boxed{
\Delta_F:=\frac1X\asymp\frac1R
}
\tag{8}
\]

for one carrier phase cell.

## 2. The Ramachandra–Révész clustering theorem

Révész's 2022 clustering theorem extends a result of Ramachandra and applies, in particular, to the ordinary Riemann zeta function. In the natural-integer specialization of his Theorem 3, suppose

\[
\zeta(\rho_0)=0,
\qquad
\beta_0>0.999,
\qquad
\gamma_0\ge100,
\tag{9}
\]

and

\[
1-\beta_0
<
\frac1{40\log\log\gamma_0}.
\tag{10}
\]

For `0<lambda<=2/3`, and for every auxiliary parameter `U` satisfying

\[
U>\max(A_{10},4\log\log\gamma_0),
\tag{11}
\]

his theorem gives, with absolute/effective constants,

\[
\begin{aligned}
&\sum_{\rho\in D(1+i\gamma_0,\lambda)\setminus\{\rho_0\}}
 e^{-U(1-\beta)}
\\
&\qquad+
\sum_{\rho\in D(1+2i\gamma_0,\lambda)}
 e^{-U(1-\beta)}
\\
&\hspace{35mm}
\gg
\frac{\lambda}{U(1-\beta_0)}-c_0.
\end{aligned}
\tag{12}
\]

The disks are Euclidean. Thus the conclusion is genuinely two-dimensional near-one information, not merely a global zero count.

For Ford zeros, conditions (9)--(10) are automatic for all sufficiently large `Q`: equation (6) is much stronger than (10), and `beta_0 -> 1`. Also `gamma_0 asymp t`, hence

\[
\log\log\gamma_0=L+o(1).
\tag{13}
\]

To maximize the strength of (12), take the smallest admissible scale

\[
U\asymp L.
\tag{14}
\]

Increasing `U` only decreases the forcing ratio in (12).

## 3. At the Ford-window radius the theorem is vacuous

Insert the full Ford-window radius

\[
\lambda=W_F=\frac JR.
\tag{15}
\]

Using (5) and (14),

\[
\begin{aligned}
\frac{\lambda}{U\delta_0}
&\asymp
\frac{J/R}{L(\log J)/X}
\\
&=
\frac{YJ}{L\log J}.
\end{aligned}
\tag{16}
\]

Since `J<=L` and `Y asymp 1`,

\[
\boxed{
\frac{W_F}{U\delta_0}
\ll
\frac1{\log J}
\longrightarrow0.
}
\tag{17}
\]

Therefore the right side of (12), at exactly the height window where `NB-243` needs pair information, is

\[
-c_0+o(1).
\tag{18}
\]

It gives no positive lower bound at all.

At one carrier cell the mismatch is even larger. Taking `lambda asymp Delta_F=1/X`,

\[
\boxed{
\frac{\Delta_F}{U\delta_0}
\asymp
\frac1{L\log J}
\longrightarrow0.
}
\tag{19}
\]

Thus the clustering theorem cannot resolve either of the two scales that survive `NB-243`: not the selected `J/R` block, and certainly not the `1/R` carrier lattice inside it.

This failure is not caused by an unnecessarily large fixed disk in the theorem. The parameter `lambda` is tunable all the way down to zero. What prevents the tuning is the theorem's own quantitative lower bound: shrinking `lambda` also shrinks the only positive term in (12).

## 4. The first non-vacuous radius lies beyond the whole Ford block

For (12) to force even a fixed positive amount of weighted companion mass, its positive term must dominate the fixed subtraction `c_0`. Up to theorem constants this requires

\[
\lambda\gtrsim U\delta_0.
\tag{20}
\]

Equations (5) and (14) therefore give the effective turn-on scale

\[
\boxed{
\lambda_{\rm useful}
\gtrsim
\frac{L\log J}{X}
\asymp
\frac{(\log Q)(\log J)}R.
}
\tag{21}
\]

Compare this first with the **entire Ford window**. From (7),

\[
\frac{\lambda_{\rm useful}}{W_F}
\gtrsim
\frac{L\log J}{YJ}.
\tag{22}
\]

Because `J<=L`,

\[
\boxed{
\frac{\lambda_{\rm useful}}{W_F}
\gtrsim
\log J
\longrightarrow\infty.
}
\tag{23}
\]

So the theorem does not merely miss individual carrier cells. It becomes informative only after its disk is wider than the **complete deterministic block selected by the Nyman source**, by a factor that still diverges in the most favorable endpoint `J=L`.

Relative to one carrier cell,

\[
\boxed{
\frac{\lambda_{\rm useful}}{\Delta_F}
\gtrsim
L\log J,
}
\tag{24}
\]

so a useful clustering disk spans a polylogarithmically growing number of carrier periods.

This is much closer to the desired scale than the half-isolated-zero clumps in `NB-238` or the large-zeta-sum inverse theorem in `NB-239`, but it remains on the wrong side of the exact localization threshold.

## 5. Asking the theorem for `Theta(J)` companion mass is even farther away

One might hope that the Ford packet needs `Theta(J)` points, so a clustering theorem could compensate for poor resolution by forcing a large population.

To make the right side of (12) of order `J`, however, one needs

\[
\frac{\lambda}{U\delta_0}\gtrsim J,
\]

hence

\[
\lambda
\gtrsim
J U\delta_0
\asymp
\frac{J L\log J}{R}.
\tag{25}
\]

Relative to the Ford window,

\[
\boxed{
\frac{\lambda}{W_F}
\gtrsim
L\log J.
}
\tag{26}
\]

Thus using the theorem as a population amplifier does not recover carrier geometry. The radius grows in direct proportion to the amount of companion mass demanded.

There is also no same-height guarantee in (12). The forced weighted mass is the **sum** of a disk around `1+i gamma_0` and another around `1+2i gamma_0`. In the worst case all of the theorem's positive output may be supplied by the doubled-height disk. Such output gives no pair information inside the selected Ford window around `t`.

## 6. Summing the theorem over a dangerous packet does not restore resolution

The matched packet left alive in `NB-231` and detected by the energy formulation of `NB-243` has `M=Theta(J)` points with spacing `Theta(1/R)` and total diameter

\[
\operatorname{diam}_\gamma \mathcal P
=O\!\left(\frac JR\right)
=O(W_F).
\tag{27}
\]

At every radius where (12) is non-vacuous, (23) gives

\[
\lambda_{\rm useful}
\gg
\operatorname{diam}_\gamma\mathcal P.
\tag{28}
\]

Consequently the disks `D(1+i gamma_j,lambda)` attached to all zeros of the packet overlap almost completely. The same is true of the disks centered near `1+2i gamma_j`.

This blocks the most obvious amplification attempt. Summing (12) over the `Theta(J)` packet zeros multiplies the right side by `J`, but it also allows the same companion zero to be counted in `Theta(J)` different clustering disks. There is no resulting lower bound of `Theta(J)` times as many **distinct** zeros, and no new constraint on the carrier pair energy.

At radii small enough to avoid this heavy overlap — `lambda=O(W_F)` or below — equation (17) says the individual clustering inequalities have already become vacuous. The two requirements cannot be satisfied simultaneously in the current regime.

## 7. Prior-art audit and representation boundary

The load-bearing external result for this scale audit is:

- Szilárd Gy. Révész, *Density estimates for the zeros of the Beurling ζ function in the critical strip*, Mathematika **68** (2022), 1045--1072, DOI `10.1112/mtk.12156`, arXiv:2012.09045. Section 5 / Theorem 3 of the current arXiv version gives the weighted clustering inequality (12), extending a classical theorem of Ramachandra to Beurling zeta functions and hence containing the ordinary Riemann-zeta specialization used here.

Révész explicitly identifies the classical antecedent as K. Ramachandra, *On the zeroes of the Riemann zeta function and L-series*, Acta Arith. **34** (1977/78), 211--218. He also notes that the later Balasubramanian--Ramachandra claim of localization solely in the disk around the original height contains a fatal missing main term. The fresh search for this pass did not locate a later repaired theorem providing same-height clustering at the Ford scale.

No novelty is claimed for the clustering theorem. The line-local content is the substitution of the exact Ford critical depth (5) and the two required vertical resolutions (7)--(8). That substitution exposes the quantitative turn-on radius (21), which is not visible from the qualitative statement that the theorem permits arbitrary `lambda>0`.

The argument is partly representation-generic: any theorem of the shape

\[
\text{forced mass}\gtrsim
\frac{\lambda}{U(1-\beta_0)}-O(1)
\tag{29}
\]

has the same minimum useful radius `lambda asymp U(1-beta_0)`. What is Nyman/zeta-specific is the Ford dictionary

\[
1-\beta_0\asymp\frac{\log J}{R},
\qquad
U_{\min}\asymp\log Q,
\qquad
W_F=\frac JR,
\tag{30}
\]

which yields the diverging ratio (23).

This finding is therefore a **method boundary**, not a theorem about a new zero configuration. It does not say that the actual zeros realize the matched packet, and it does not say that the Ramachandra--Révész argument cannot be sharpened. It says that the published clustering conclusion, even though it is pointwise and near-one, is quantitatively silent at the exact deterministic window required by `NB-243`.

## 8. Falsification boundary and route consequence

Several possible objections do not change the conclusion.

First, choosing `U` larger does not help: the forcing ratio is inversely proportional to `U`, so the optimal choice is already the minimum `U asymp log Q`. Second, choosing a smaller `lambda` is formally allowed but makes the theorem weaker; equations (17)--(19) quantify exactly when it becomes vacuous. Third, taking `J` at its largest allowed value is the most favorable comparison with the Ford window, yet even at `J=L` the scale ratio is at least `asymp log J`.

Fourth, the theorem can be very strong at macroscopic `lambda`. For fixed `lambda`, a critical Ford zero forces weighted companion mass on the scale roughly

\[
\frac{R}{L\log J},
\]

which diverges. That does not contradict the present boundary: the mass may lie across a disk vastly larger than the source window, may occur near `2t`, and is not resolved into the carrier phases needed by (23) of `NB-243`.

A decisive falsification would be a valid strengthening of the near-one clustering theorem whose positive term remains non-vacuous for

\[
\lambda\lesssim\frac JR
\]

uniformly for `1<<J<=log Q`, while keeping the companion mass at the original height and retaining enough horizontal information to preserve Ford depth marks. The currently published Ramachandra--Révész inequality does not have that property.

The source frontier after `NB-244` is therefore narrower. Classical near-one clustering is not merely missing one carrier period; **its first informative radius already lies outside the whole Ford block**. Any useful replacement must either improve the clustering tradeoff by at least the factor

\[
\frac{(\log Q)(\log J)}J,
\]

or bypass companion-zero forcing and attack the microlocal depth-marked carrier energy of `NB-243` directly.