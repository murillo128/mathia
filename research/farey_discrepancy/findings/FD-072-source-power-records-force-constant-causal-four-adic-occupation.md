# FD-072 — source power records force constant causal four-adic occupation

**Status:** `EXACT-DERIVED + SOURCE-POWER-RECORDS + EPISODE-ADAPTED-HORIZON + CAUSAL-DENOMINATOR + FIXED-FOUR-ADIC-WITNESS + CONSTANT-NONSQUAREFREE-OCCUPATION + SCHUR-GAP + ZERO-FRONTIER-CERTIFICATE`.

`FD-069`--`FD-070` show that an arbitrary physical spike eventually generates persistent nonsquarefree occupation, while `FD-071` shows why persistence at arbitrarily later horizons is not enough: a later zero-frontier spike can dominate the same-horizon denominator and dilute every fixed earlier packet. The surviving question is therefore episode-adapted. Can one choose a horizon tied to the source episode so that the denominator is forced to see only source values already controlled by that episode?

At **power-record points** the answer is yes, and no short-interval coherence or reciprocal onset delay is needed. Fix `sigma>1/2` and define

\[
R_\sigma(n):=\frac{|\mathcal H(n)|}{n^\sigma},
\qquad
A_X:=|\mathcal H(X)|.
\tag{1}
\]

Call `X` a `sigma`-record when

\[
R_\sigma(X)=\max_{1\le n\le X}R_\sigma(n).
\tag{2}
\]

Put

\[
\mathscr C_\sigma
:=
\sum_{r=4}^{\infty}\left(\frac4r\right)^{2\sigma}
=
4^{2\sigma}
\left(
\zeta(2\sigma)-1-2^{-2\sigma}-3^{-2\sigma}
\right),
\tag{3}
\]

which is finite exactly because `sigma>1/2`, and set

\[
\kappa_\sigma:=\frac{3}{4\mathscr C_\sigma}>0.
\tag{4}
\]

Then every `sigma`-record `X>=2`, at the fixed four-adic horizon

\[
T=4X,
\qquad
D=3,
\tag{5}
\]

satisfies

\[
\boxed{
\nu_{4X,3}
:=\frac{U_{4X,3}}{E_{4X,3}}
\ge \kappa_\sigma.
}
\tag{6}
\]

Moreover, if `epsilon_(T,D)` is the normalized Schur projective defect of `FD-049` and

\[
\mathfrak D_{T,D}
=\Delta_{T,D}\varepsilon_{T,D},
\qquad
\Delta_{T,D}:=C_T-C_D,
\tag{7}
\]

is the scalar GCD-duality saturation loss of `FD-032`/`FD-065`, then

\[
\boxed{
\varepsilon_{4X,3}\ge\kappa_\sigma,
\qquad
\mathfrak D_{4X,3}
\ge\frac{\kappa_\sigma}{24}
=\frac1{32\mathscr C_\sigma}.
}
\tag{8}
\]

Thus a source-selected power record cannot be squarefree-diluted at its own four-adic causal horizon. The whole denominator is bounded by the record amplitude itself, while the single nonsquarefree row `r=4` captures that amplitude exactly.

## 1. A power record controls every source value visible at `T=4X`

The record condition (2) gives, for every `1<=n<=X`,

\[
\boxed{
|\mathcal H(n)|
\le
A_X\left(\frac nX\right)^\sigma.
}
\tag{9}
\]

At `T=4X` and fixed head `D=3`, every surviving Jordan row satisfies `4<=r<=4X`, so its quotient argument is

\[
n_r:=\left\lfloor\frac{4X}{r}\right\rfloor
\le X.
\tag{10}
\]

This is the causal point missing from the arbitrary-later-horizon analysis: **no row in the denominator can sample the source after the record time `X`**. Combining (9) with

\[
\frac{n_r}{X}
\le\frac4r
\tag{11}
\]

gives

\[
|\mathcal H(n_r)|^2
\le
A_X^2\left(\frac4r\right)^{2\sigma}.
\tag{12}
\]

Write as usual

\[
w(r):=\frac{J_2(r)}{r^2},
\qquad 0<w(r)\le1,
\tag{13}
\]

and

\[
E_{T,D}
:=
\sum_{D<r\le T}
w(r)
\mathcal H\!\left(\left\lfloor\frac Tr\right\rfloor\right)^2.
\tag{14}
\]

Then (12)--(13) imply the complete same-horizon denominator bound

\[
\begin{aligned}
E_{4X,3}
&\le
A_X^2
\sum_{r=4}^{4X}
\left(\frac4r\right)^{2\sigma}\\
&\le
\boxed{\mathscr C_\sigma A_X^2}.
\end{aligned}
\tag{15}
\]

The convergence threshold `sigma>1/2` is exact for this argument. At `sigma=1/2`, the comparison series is harmonic and the record envelope alone no longer bounds the complete denominator by a constant multiple of `A_X^2`.

## 2. The row `r=4` captures the record exactly and is automatically transverse

The same horizon contains the row `r=4`, and

\[
\left\lfloor\frac{4X}{4}\right\rfloor=X.
\tag{16}
\]

Since `4` is nonsquarefree,

\[
w(4)=\frac{J_2(4)}{4^2}=\frac34,
\tag{17}
\]

and therefore the joint nonsquarefree energy obeys

\[
\boxed{
U_{4X,3}
\ge
\frac34 A_X^2.
}
\tag{18}
\]

Dividing (18) by (15) proves (6).

This is stronger at the selected record horizon than the fixed-dilation injection of `FD-047`. That injection compares `U_(4X,3)` with the **lower-horizon tail energy** `E_(X,3)`. Here the record envelope controls the **entire current denominator** `E_(4X,3)` directly, including all squarefree rows. The mechanism is not an average over a four-adic chain and does not rely on logarithmic density.

The equality ray has zero Jordan coordinate on every nonsquarefree row, so `FD-049` gives

\[
\varepsilon_{4X,3}
\ge
\nu_{4X,3}.
\tag{19}
\]

For the scalar loss, `FD-003` gives

\[
C_N=\sum_{n\le N}\frac{\mu(n)^2}{J_2(n)}.
\tag{20}
\]

Hence, for `X>=2`,

\[
\Delta_{4X,3}
=C_{4X}-C_3
\ge
\frac{\mu(5)^2}{J_2(5)}
=\frac1{24}.
\tag{21}
\]

Equations (7), (19), (21), and (6) prove (8). No asymptotic estimate for `Delta` is needed.

## 3. False RH forces infinitely many constant-occupation record horizons

Let

\[
\Theta
:=
\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.
\tag{22}
\]

`FD-046` proves that the physical shell source `mathcal H` has the same power-growth frontier as the Mertens function. In particular, whenever

\[
\frac12<\sigma<\Theta,
\tag{23}
\]

the normalized values `R_sigma(n)` are unbounded. Therefore there is an unbounded sequence of strict new `sigma`-records `X_j`, and (6)--(8) hold at every horizon `T_j=4X_j`. Consequently,

\[
\boxed{
\Theta>\sigma>\frac12
\quad\Longrightarrow\quad
\limsup_{T\to\infty}\nu_{T,3}
\ge\kappa_\sigma,
}
\tag{24}
\]

and

\[
\boxed{
\Theta>\sigma>\frac12
\quad\Longrightarrow\quad
\limsup_{T\to\infty}\mathfrak D_{T,3}
\ge\frac{\kappa_\sigma}{24}.
}
\tag{25}
\]

This yields a direct zero-frontier certificate by contraposition:

\[
\boxed{
\limsup_{T\to\infty}\nu_{T,3}<\kappa_\sigma
\quad\Longrightarrow\quad
\Theta\le\sigma,
}
\tag{26}
\]

with the analogous implication from `limsup mathfrak D_(T,3)<kappa_sigma/24`.

In particular,

\[
\boxed{
\nu_{T,3}\to0
\quad\Longrightarrow\quad
\mathrm{RH},
}
\tag{27}
\]

and likewise

\[
\boxed{
\mathfrak D_{T,3}\to0
\quad\Longrightarrow\quad
\mathrm{RH}.
}
\tag{28}
\]

These are one-way criteria, not proofs that either geometric quantity tends to zero. They isolate a precise consequence that any future vanishing theorem for the physical occupation or fixed-head scalar saturation channel would have.

## 4. The constant degenerates exactly at the critical exponent

The record theorem does not smuggle in a uniform RH gap. Indeed

\[
\mathscr C_\sigma
=
\sum_{r=4}^{\infty}\left(\frac4r\right)^{2\sigma}
\longrightarrow\infty
\qquad(\sigma\downarrow1/2),
\tag{29}
\]

so

\[
\boxed{
\kappa_\sigma\longrightarrow0
\qquad(\sigma\downarrow1/2).
}
\tag{30}
\]

Thus a frontier only infinitesimally to the right of the critical line forces only an correspondingly small positive occupation constant through this argument. The mechanism becomes quantitatively strong only when there is a fixed power gap above `1/2`.

Because each term `(4/r)^(2sigma)` decreases with `sigma`, `mathscr C_sigma` is decreasing and `kappa_sigma` increasing. Hence (24) can also be read as a monotone quantitative bridge: a measured or proved upper bound on the limsup occupation below `kappa_sigma` excludes every zeta zero to the right of `Re(s)=sigma`.

No converse is asserted. RH gives the usual subcritical power envelopes but does not imply `nu_(T,3)->0`; `FD-047`, `FD-050`, and `FD-068` in fact show substantial recurrent nonsquarefree occupation under broader averaging quantifiers.

## 5. Why this evades the `FD-071` dilution mechanism without contradicting it

`FD-071` fixes an earlier episode `X` and lets the physical horizon move far into the future. A later frontier spike `N` can then be sampled by a squarefree row and contribute `N^(2Theta-o(1))` to the denominator, while the old packet grows only linearly in the horizon. The old episode is therefore diluted.

Here the quantifiers are reversed. At a `sigma`-record `X`, choose the **episode's own** horizon `T=4X`. Every quotient sampled by every surviving row is at most `X`, so there is literally no later source value available to dilute the record. The record inequality (9) then prices all earlier values relative to `A_X`. This is exactly the source-specific same-horizon coupling that `FD-071` left open.

The result also explains the scope of the two-thirds barrier in `FD-064`--`FD-066` and `FD-070`. Those findings transport a generic spike through a local source window to many nonsquarefree rows under arbitrary or delayed host geometries; their normalization becomes competitive only above `Theta=2/3`. A power record needs no local packet transport at all: the fixed row `4` samples it exactly, and global control of all earlier quotients comes from the record envelope. Therefore the `2/3` threshold is not a universal obstruction to **source-adapted sparse horizons**.

This does not settle `CLUE-joint-nonsquarefree-jordan-energy-occupation`. That clue asks for a positive fraction at every sufficiently large horizon. Power records can be arbitrarily sparse, and the theorem gives no upper bound on the gaps between them, no positive ordinary/logarithmic density of record horizons, and no transfer of the constant gap to their neighborhoods. The remaining issue is now sharply separated: recurrence/density of source-selected record episodes, or a mechanism that propagates their causal denominator control to enough nearby horizons.

## 6. Prior-art boundary and falsification checks

The only non-elementary analytic input in the zero-frontier consequence is the classical Mertens/zeta power-growth theorem already anchored through Titchmarsh in `SOURCES.md` and transferred to `mathcal H` by `FD-046`. The power-record envelope (9), the exact four-adic sample (16), and the summable denominator comparison (15) are elementary. A targeted audit over Mertens record values, Farey discrepancy, GCD/Jordan energies, and normalized power records did not identify an external theorem supplying this particular causal occupation bridge. No new external dependency is load-bearing, so `SOURCES.md` requires no addition and no broad novelty claim is made.

The falsification boundary is explicit. The horizon must be tied to the record as `T=4X`; replacing it by an arbitrary much later horizon reopens the `FD-071` dilution mechanism. The head `D=3` is fixed so row `4` survives. The record must control the **same** physical source `mathcal H` used by the denominator; a record of an unrelated Mertens statistic would not imply (9). The exponent must satisfy `sigma>1/2`; at the endpoint the comparison series diverges. Finally, (27)--(28) are implications from a future vanishing theorem to RH, not evidence that such vanishing occurs. The durable gain is the exact source-adapted statement (6): every power record above the critical exponent forces a fixed positive same-horizon nonsquarefree fraction and a fixed positive Schur saturation loss.
