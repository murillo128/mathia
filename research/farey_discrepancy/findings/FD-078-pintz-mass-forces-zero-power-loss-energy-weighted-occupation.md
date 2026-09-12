# FD-078 — Pintz mass forces zero-power-loss energy-weighted occupation

**Status:** `EXACT-DERIVED + LITERATURE-CALIBRATED + MOMENT-LIFT + POWER-ANNULUS-AGGREGATION + ENERGY-WEIGHTED-OCCUPATION + ZERO-POWER-LOSS + SCHUR-PROJECTIVE-TRANSFER`.

`FD-077` shows that the physical quotient-shell source

\[
\mathcal H(N)
=\sum_{s\le N}\frac{\mathbf M(\lfloor N/s\rfloor)}s
\]

has logarithmic `L^1` mass of full zeta-zero exponent in every fixed power annulus. It then obtains a full-counting-exponent family of causal horizons with only arbitrarily small polynomial occupation loss. That still leaves a different escape: the **physical energy itself** could, in principle, concentrate on a much thinner collection of badly occupied horizons, so an unweighted counting statement need not control the energy-weighted geometry.

The `L^1` theorem already rules out that escape at every fixed polynomial scale. Weighted Hölder lifts the source mass to full `L^p` logarithmic moment exponent `p Theta`. A single fixed nonsquarefree Jordan row then injects the `p=2` source moment into the nonsquarefree Schur energy. Consequently, in every fixed power annulus of horizons, the logarithmically aggregated total energy, nonsquarefree energy, and Schur projective residual all have the same full exponent `2 Theta`.

Thus the **energy-weighted** nonsquarefree occupation can still tend to zero, but it cannot lose any fixed positive power. This is orthogonal to `FD-050`: that finding gives a positive logarithmic average of the pointwise occupation ratios, whereas the present theorem allows the horizon weights themselves to be the physical energies and shows that even this adversarial reweighting cannot create polynomial-scale dilution.

Let

\[
\Theta
:=
\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.
\]

For fixed `0<alpha<1` and `p>=1`, define the logarithmic source moment in the terminal power annulus

\[
S_{p,\alpha}(X)
:=
\sum_{X^{1-\alpha}<n\le X}
\frac{|\mathcal H(n)|^p}{n}.
\]

Then

\[
\boxed{
\lim_{X\to\infty}
\frac{\log(1+S_{p,\alpha}(X))}{\log X}
=p\Theta.
}
\tag{1}
\]

Now fix a Schur head `D`. Write

\[
w(r):=\frac{J_2(r)}{r^2},
\]

\[
E_{H,D}
:=
\sum_{D<r\le H}w(r)
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right)^2,
\]

\[
U_{H,D}
:=
\sum_{\substack{D<r\le H\\\mu(r)=0}}w(r)
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right)^2,
\]

and let `rho_(H,D)^2` be the squared Schur residual from the distinguished equality ray, so that `FD-049` gives

\[
U_{H,D}\le \rho_{H,D}^2\le E_{H,D}.
\tag{2}
\]

Use the exact logarithmic horizon weight

\[
\lambda_H:=\log\frac{H+1}{H}.
\]

For fixed `0<alpha<1`, put

\[
\mathscr E_{D,\alpha}(X)
:=
\sum_{X^{1-\alpha}<H\le X}
\lambda_H E_{H,D},
\]

\[
\mathscr U_{D,\alpha}(X)
:=
\sum_{X^{1-\alpha}<H\le X}
\lambda_H U_{H,D},
\]

\[
\mathscr R_{D,\alpha}(X)
:=
\sum_{X^{1-\alpha}<H\le X}
\lambda_H \rho_{H,D}^2.
\]

Then all three annular aggregates have the full doubled zero-frontier exponent:

\[
\boxed{
\lim_{X\to\infty}
\frac{\log(1+\mathscr U_{D,\alpha}(X))}{\log X}
=
\lim_{X\to\infty}
\frac{\log(1+\mathscr R_{D,\alpha}(X))}{\log X}
=
\lim_{X\to\infty}
\frac{\log(1+\mathscr E_{D,\alpha}(X))}{\log X}
=2\Theta.
}
\tag{3}
\]

In particular, the annular **energy-weighted occupation**

\[
\Omega_{D,\alpha}(X)
:=
\frac{\mathscr U_{D,\alpha}(X)}{\mathscr E_{D,\alpha}(X)}
\]

and the corresponding energy-weighted projective defect

\[
\Pi_{D,\alpha}(X)
:=
\frac{\mathscr R_{D,\alpha}(X)}{\mathscr E_{D,\alpha}(X)}
\]

satisfy

\[
\boxed{
\frac{\log(1/\Omega_{D,\alpha}(X))}{\log X}
\longrightarrow0,
\qquad
\frac{\log(1/\Pi_{D,\alpha}(X))}{\log X}
\longrightarrow0.
}
\tag{4}
\]

Equivalently, for every fixed `eta>0`,

\[
\boxed{
\Omega_{D,\alpha}(X)\ge X^{-\eta},
\qquad
\Pi_{D,\alpha}(X)\ge X^{-\eta}
}
\tag{5}
\]

for all sufficiently large `X`. Since `Pi>=Omega`, only the first inequality is substantive.

The same conclusions hold for the cumulative aggregates obtained by summing over all sufficiently large `H<=X`; the power-annulus form is stronger and is the one proved below.

## 1. Pintz `L^1` mass lifts to every logarithmic source moment

`FD-077`, using Pintz's 2026 average-absolute-order theorem for the Mertens function through the exact inverse floor transform of `FD-046`, proves that for every fixed `0<alpha<1`,

\[
L_{\mathcal H}(X;\alpha)
:=
\sum_{X^{1-\alpha}<n\le X}
\frac{|\mathcal H(n)|}{n}
\]

satisfies

\[
\boxed{
\lim_{X\to\infty}
\frac{\log(1+L_{\mathcal H}(X;\alpha))}{\log X}
=\Theta.
}
\tag{6}
\]

For `p>=1`, weighted Hölder on the same annulus gives

\[
\left(
\sum\frac{|\mathcal H(n)|}{n}
\right)^p
\le
\left(
\sum\frac{|\mathcal H(n)|^p}{n}
\right)
\left(
\sum\frac1n
\right)^{p-1}.
\tag{7}
\]

The harmonic mass of the annulus is only logarithmic:

\[
\sum_{X^{1-\alpha}<n\le X}\frac1n
=\alpha\log X+O(1)
=X^{o(1)}.
\tag{8}
\]

Equations (6)--(8) therefore imply

\[
\liminf_{X\to\infty}
\frac{\log(1+S_{p,\alpha}(X))}{\log X}
\ge p\Theta.
\tag{9}
\]

For the opposite direction, `FD-046` gives for every fixed `sigma>Theta`

\[
|\mathcal H(n)|\ll_\sigma n^\sigma.
\tag{10}
\]

Hence

\[
S_{p,\alpha}(X)
\ll_{p,\sigma}
\sum_{n\le X}n^{p\sigma-1}
\ll_{p,\sigma}X^{p\sigma}.
\tag{11}
\]

Letting `sigma` decrease to `Theta` proves (1). For `p=2`, in particular,

\[
\boxed{
\lim_{X\to\infty}
\frac{\log(1+S_{2,\alpha}(X))}{\log X}
=2\Theta.
}
\tag{12}
\]

The point of (12) is not merely that large source values exist. It says that their **quadratic logarithmic mass** already fills the entire zero-frontier exponent in every fixed power annulus. Sparse isolated limsup spikes cannot account for this statement.

## 2. One fixed nonsquarefree row transfers the full quadratic moment into every horizon annulus

Fix once and for all a nonsquarefree integer `q>D`. At the causal horizon

\[
H=qn,
\]

the Jordan row `r=q` samples the source exactly at `n`, and because `q` is nonsquarefree it lies inside `U_(H,D)`. Thus, exactly as in `FD-077`,

\[
\boxed{
U_{qn,D}\ge w(q)\mathcal H(n)^2.
}
\tag{13}
\]

Fix the target horizon-annulus exponent `alpha`, and choose any fixed `0<beta<alpha`, for example `beta=alpha/2`. Put

\[
Y:=\frac Xq.
\]

For

\[
Y^{1-\beta}<n\le Y,
\]

we have `qn<=X`, while

\[
qn
>
qY^{1-\beta}
=q^\beta X^{1-\beta}
>X^{1-\alpha}
\tag{14}
\]

for all sufficiently large `X`, because `alpha-beta>0`. Therefore all such causal horizons lie inside the target annulus `(X^(1-alpha),X]`.

The logarithmic weight at a causal horizon obeys

\[
\lambda_{qn}
=\log\left(1+\frac1{qn}\right)
\ge\frac1{qn+1}
\ge\frac1{(q+1)n}.
\tag{15}
\]

Using only the horizons `H=qn` from (14), equations (13)--(15) yield

\[
\begin{aligned}
\mathscr U_{D,\alpha}(X)
&\ge
\sum_{Y^{1-\beta}<n\le Y}
\lambda_{qn}U_{qn,D}\\
&\ge
\frac{w(q)}{q+1}
\sum_{Y^{1-\beta}<n\le Y}
\frac{\mathcal H(n)^2}{n}.
\end{aligned}
\tag{16}
\]

By (12), applied at scale `Y=X/q`, the right side has power exponent `2Theta`. Hence

\[
\boxed{
\liminf_{X\to\infty}
\frac{\log(1+\mathscr U_{D,\alpha}(X))}{\log X}
\ge2\Theta.
}
\tag{17}
\]

This lower bound uses only one fixed causal row. The full nonsquarefree union can only add energy.

## 3. The zero-frontier envelope closes the aggregate exponent from above

For every `sigma>Theta`, `FD-046` gives the fixed-head physical energy envelope

\[
E_{H,D}\ll_{D,\sigma}H^{2\sigma}.
\tag{18}
\]

Also

\[
\lambda_H
=\log\left(1+\frac1H\right)
\le\frac1H.
\tag{19}
\]

Therefore

\[
\begin{aligned}
\mathscr E_{D,\alpha}(X)
&\le
\sum_{H\le X}\frac{E_{H,D}}H\\
&\ll_{D,\sigma}
\sum_{H\le X}H^{2\sigma-1}
\ll_{D,\sigma}X^{2\sigma}.
\end{aligned}
\tag{20}
\]

Since

\[
\mathscr U_{D,\alpha}(X)
\le
\mathscr R_{D,\alpha}(X)
\le
\mathscr E_{D,\alpha}(X),
\tag{21}
\]

equation (17), followed by `sigma downarrow Theta` in (20), proves all three limits in (3).

This is where the average-order input changes the conclusion relative to `FD-046`. `FD-046` shows that one fixed row has limsup pointwise exponent `2Theta`; arbitrarily separated spikes are compatible with that. Equations (12), (16), and (20) instead give a **full limit for the cumulative logarithmic energy in every fixed power annulus**. The energy exponent cannot disappear between sparse pointwise spikes.

## 4. Energy reweighting cannot create a polynomial occupation escape

Because both numerator and denominator of `Omega_(D,alpha)` have logarithmic exponent `2Theta`,

\[
\frac{\log\mathscr E_{D,\alpha}(X)
-\log\mathscr U_{D,\alpha}(X)}{\log X}
\longrightarrow0.
\tag{22}
\]

Since `0<Omega<=1` for all sufficiently large `X`, this is exactly the first limit in (4). Equation (21) gives `Pi>=Omega`, proving the projective statement as well.

The interpretation is different from the logarithmic-average theorem `FD-050`. There one averages the **pointwise ratio** `nu_(H,D)=U_(H,D)/E_(H,D)` against multiplicative horizon measure and obtains a positive lower logarithmic mean. That theorem permits a logarithmically negligible exceptional family to carry disproportionately large total energy. Here the weights are effectively `lambda_H E_(H,D)`: the aggregate ratio is

\[
\Omega_{D,\alpha}(X)
=
\frac{
\sum\lambda_H E_{H,D}\nu_{H,D}
}{
\sum\lambda_H E_{H,D}
}.
\tag{23}
\]

Equation (4) therefore says that even after the horizon measure is tilted by the physical energy itself, the nonsquarefree component cannot suffer a fixed polynomial loss on any fixed power annulus.

This also sharpens the abundance conclusion of `FD-077`. A full-counting-exponent set could still have zero natural and logarithmic density. The present statement no longer counts source samples: it aggregates their **actual quadratic contribution to the Schur geometry** and proves that this contribution retains the full polynomial exponent of the total physical energy.

## 5. Falsification boundary

The theorem deliberately stops at zero polynomial loss. It does **not** prove

\[
\Omega_{D,\alpha}(X)\ge c_D>0,
\]

nor does it rule out decay such as inverse powers of `log X` or stretched exponentials in `log X`. Equal power exponents alone cannot distinguish those possibilities. Thus `CLUE-joint-nonsquarefree-jordan-energy-occupation` remains unresolved: pointwise eventual positive occupation is much stronger than (4).

The fixed-head hypothesis is essential to the proof as written. The upper envelope (18) is the fixed-`D` estimate used in `FD-046`, and the lower injection selects one fixed nonsquarefree `q>D`. A head tending to infinity eventually excludes every fixed row; the head-covariant mechanism of `FD-068` is a different argument and cannot simply be substituted into (16).

The annulus exponent `alpha` is also fixed. Nothing here is uniform as `alpha=alpha(X)` tends to zero, because the source-mass input `FD-077` is itself a fixed-power-annulus theorem. Likewise, the argument makes no claim that the large `L^2` mass lies at strict source records; it does not recover the pointwise constant protection of `FD-072`.

At the critical boundary `Theta=1/2`, equations (1)--(5) remain valid with source square-moment exponent `1`. They still forbid a polynomial aggregate occupation loss, but they do not create an off-critical contradiction. Under false RH, `Theta>1/2`, the same theorem says that every fixed power annulus carries superlinear logarithmic Schur energy of exponent `2Theta`, with the nonsquarefree transverse component sharing that full exponent.

A matched synthetic profile with very deep occupation losses on supermultiplicatively sparse horizons, such as the control behind `FD-048`, is not contradicted: those individual bad horizons can remain present. What the present theorem excludes for the actual arithmetic source is that such exceptional horizons capture a polynomially larger share of the **annular aggregate energy** than the nonsquarefree sector.

## 6. Prior-art boundary

The only external arithmetic input is the Pintz 2026 average-absolute-order theorem already anchored in `SOURCES.md` and already transferred to `mathcal H` in `FD-077`. Equation (1) is then an elementary weighted-Hölder consequence of that canonical finding, while the passage from source square moment to nonsquarefree Schur energy uses only the exact fixed-row Jordan sampling identity already present in this line.

A directed search around Mertens average moments, Farey discrepancy, Jordan-totient/GCD energies, nonsquarefree restrictions, and logarithmic aggregation located Pintz's average-order paper and the recent Farey local-discrepancy literature, but no theorem matching the specific energy-weighted occupation statement (3)--(5). No priority claim is made. No new external theorem is load-bearing here, so `SOURCES.md` is unchanged.

The decisive distinction from nearby canonical results is:

- `FD-046`: pointwise **limsup** energy exponent on any fixed row;
- `FD-050`: positive global logarithmic average of the **unweighted pointwise occupation ratio**;
- `FD-077`: full polynomial counting exponent for frontier-near source samples and subpower pointwise occupation on those causal samples;
- the present result: a full `2Theta` exponent for the **energy-weighted aggregate nonsquarefree and projective mass in every fixed power annulus**.

The remaining target is correspondingly narrower: upgrade the subpower ratio in (4) to a nonvanishing aggregate constant, or find a source-specific mechanism that prevents the total Schur energy from concentrating by even a subpower factor on the residual low-occupation set.