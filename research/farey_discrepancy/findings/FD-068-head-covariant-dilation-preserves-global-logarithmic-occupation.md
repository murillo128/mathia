# FD-068 — head-covariant dilation preserves global logarithmic occupation

**Status:** `EXACT-DERIVED + HEAD-COVARIANT-DILATION + GROWING-SCHUR-HEAD + GLOBAL-LOGARITHMIC-AVERAGE + JOINT-NONSQUAREFREE-OCCUPATION + ZERO-FRONTIER-CALIBRATED + CROSS-RAY-OBSTRUCTION`.

`FD-050` converts the fixed-head nonsquarefree dilation inequality into a global logarithmic lower-tail bound by telescoping over all horizons, but explicitly leaves a moving Schur head outside that argument. `FD-067` supplies the missing exact covariance: dilation by a nonsquarefree integer rescales the physical head from `D` to `floor(D/q)`. If the head is chosen as one deterministic scale-covariant function of the horizon, the moving-head energy again becomes a single multiplicative cocycle, so the `FD-050` all-horizon telescope survives.

Fix a nonsquarefree integer `q>1`. Let `D_H` be an integer head schedule with `1<=D_H<H` for all sufficiently large `H`, and assume the eventual **q-subcovariance**

\[
\boxed{
\left\lfloor\frac{D_H}{q}\right\rfloor
\le
D_{\lfloor H/q\rfloor}.
}
\tag{1}
\]

Write

\[
E_H:=E_{H,D_H},
\qquad
U_H:=U_{H,D_H},
\qquad
\nu_H:=\frac{U_H}{E_H},
\qquad
w(q):=\frac{J_2(q)}{q^2}.
\tag{2}
\]

Then the exact moving-head dilation inequality is

\[
\boxed{
\nu_H
\ge
w(q)\frac{E_{\lfloor H/q\rfloor}}{E_H}.
}
\tag{3}
\]

Consequently, if for some `0<=delta<=1`

\[
D_H=H^{\delta+o(1)},
\tag{4}
\]

and

\[
\Theta:=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\},
\qquad
a_\delta(\Theta):=\delta+2\Theta(1-\delta),
\tag{5}
\]

then, with logarithmic weights

\[
\lambda_H:=\log\frac{H+1}{H},
\qquad
W_X:=\sum_{H=H_*}^{X-1}\lambda_H
=\log\frac{X}{H_*},
\tag{6}
\]

one has

\[
\boxed{
\limsup_{X\to\infty}
\frac1{W_X}
\sum_{H=H_*}^{X-1}
\lambda_H\log\frac1{\nu_H}
\le
L_{q,\delta}
:=a_\delta(\Theta)\log q-\log w(q).
}
\tag{7}
\]

Equivalently,

\[
\boxed{
\liminf_{X\to\infty}
\prod_{H=H_*}^{X-1}
\nu_H^{\lambda_H/W_X}
\ge
c_{q,\delta}
:=w(q)q^{-a_\delta(\Theta)}.
}
\tag{8}
\]

Thus extremely small occupation remains globally sparse even when the Schur head grows. For every fixed `0<eta<1`,

\[
\boxed{
\limsup_{X\to\infty}
\frac1{W_X}
\sum_{\substack{H_*\le H<X\\\nu_H\le\eta}}
\lambda_H
\le
\min\!\left\{1,
\frac{L_{q,\delta}}{\log(1/\eta)}
\right\}.
}
\tag{9}
\]

In particular, every `eta<c_(q,delta)` leaves a positive lower logarithmic density of horizons with `nu_H>eta`, while for any deterministic `eta_X->0` the horizons below `eta_X` have logarithmic density tending to zero.

For the canonical dilation `q=4`,

\[
\boxed{
c_{4,\delta}
=\frac34\,4^{-\{\delta+2\Theta(1-\delta)\}}.}
\tag{10}
\]

At a linear q-covariant head, `delta=1`, the zero-frontier exponent disappears completely:

\[
\boxed{c_{4,1}=\frac3{16}}
\tag{11}
\]

unconditionally. More generally, under RH `a_delta(1/2)=1` for every `delta`, so the same `3/16` constant holds throughout the whole head-growth range. The result does not produce a pointwise gap: a zero-frontier spike sequence may still hide inside a logarithmically negligible exceptional set. It does show that **growing the head does not restore a positive-logarithmic-density cross-ray escape**.

## 1. The head-covariant injection closes to one moving energy

Retain the physical quantities of `FD-065`--`FD-067`,

\[
E_{H,D}
:=
\sum_{D<r\le H}
\frac{J_2(r)}{r^2}
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right)^2,
\tag{12}
\]

\[
U_{H,D}
:=
\sum_{\substack{D<r\le H\\\mu(r)=0}}
\frac{J_2(r)}{r^2}
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right)^2.
\tag{13}
\]

For every nonsquarefree integer `q`, `FD-067` proves the exact injection

\[
U_{H,D}
\ge
w(q)
E_{\lfloor H/q\rfloor,\lfloor D/q\rfloor}.
\tag{14}
\]

Apply (14) with `D=D_H`. Since `E_(H,D)` is nonincreasing in the cutoff `D`, the covariance assumption (1) gives

\[
E_{\lfloor H/q\rfloor,\lfloor D_H/q\rfloor}
\ge
E_{\lfloor H/q\rfloor,D_{\lfloor H/q\rfloor}}
=E_{\lfloor H/q\rfloor}.
\tag{15}
\]

Hence

\[
U_H\ge w(q)E_{\lfloor H/q\rfloor},
\tag{16}
\]

which is (3). Taking logarithms gives the exact one-step entropy inequality

\[
\boxed{
\log\frac1{\nu_H}
\le
-\log w(q)
+\log E_H
-\log E_{\lfloor H/q\rfloor}.
}
\tag{17}
\]

This is the key distinction from an arbitrary moving head. The lower-horizon term in (17) is the value of the **same schedule-defined energy** at `floor(H/q)`, so there is again only one function to telescope.

The covariance condition is not restrictive at the power scales used in the current Schur analysis. For every fixed `0<delta<1` and `c>0`,

\[
D_H=\lfloor cH^\delta\rfloor
\tag{18}
\]

satisfies (1) for all sufficiently large `H`: if `H'=floor(H/q)`, then

\[
\frac{cH^\delta/q}{c(H')^\delta}
=q^{\delta-1}(1+o(1))<1.
\tag{19}
\]

Fixed heads recover `delta=0`. At the linear endpoint, the exact schedule

\[
D_H=\left\lfloor\frac Hm\right\rfloor,
\qquad m\ge3,
\tag{20}
\]

is q-covariant for every integer `q`, because

\[
\left\lfloor\frac{\lfloor H/m\rfloor}{q}\right\rfloor
=
\left\lfloor\frac{H}{mq}\right\rfloor
=
\left\lfloor\frac{\lfloor H/q\rfloor}{m}\right\rfloor.
\tag{21}
\]

Thus the linear-head case in (11) is a genuine all-horizon schedule, not an interpolation from one q-adic chain.

## 2. Logarithmic integration cancels every interior scale

Choose `H_0` so that (1), `D_H<H`, and the definitions above hold for every `H>=H_0`, and start the average at `H_*=qH_0`. Define the step function

\[
F(x):=\log E_{\lfloor x\rfloor}
\qquad(x\ge H_0).
\tag{22}
\]

For almost every `x` in a unit interval `[H,H+1)`,

\[
F(x/q)=\log E_{\lfloor H/q\rfloor}.
\tag{23}
\]

Integrating (17) against the multiplicative measure `dx/x` from `H_*` to an integer `X` therefore gives

\[
\begin{aligned}
\sum_{H=H_*}^{X-1}
\lambda_H\log\frac1{\nu_H}
&\le
-\log w(q)\log\frac{X}{H_*}\\
&\quad+
\int_{H_*}^{X}
\bigl(F(x)-F(x/q)\bigr)\frac{dx}{x}.
\end{aligned}
\tag{24}
\]

The moving head has disappeared inside the single function `F`. The scale difference telescopes exactly:

\[
\boxed{
\int_{H_*}^{X}
\bigl(F(x)-F(x/q)\bigr)\frac{dx}{x}
=
\int_{X/q}^{X}F(y)\frac{dy}{y}
-
\int_{H_*/q}^{H_*}F(y)\frac{dy}{y}.
}
\tag{25}
\]

All interior horizons cancel, just as in the fixed-head `FD-050` argument. The second integral is a fixed boundary constant; only the top multiplicative shell `[X/q,X]` needs an analytic bound.

This is the exact global counterpart of the discrete chain product in `FD-067`. There the denominator telescopes only along `H_j=q^jH_0`. Here the q-subcovariant schedule lets the same cancellation run simultaneously through the complete set of integer horizons under logarithmic measure.

## 3. The zero-frontier envelope prices the top boundary

For every fixed `sigma>Theta`, the source envelope used in `FD-065` and `FD-067` gives

\[
E_{H,D}
\ll_\sigma
H^{2\sigma}D^{1-2\sigma}.
\tag{26}
\]

Under (4),

\[
\log E_H
\le
\bigl(a_\delta(\sigma)+o(1)\bigr)\log H,
\qquad
 a_\delta(\sigma)
:=\delta+2\sigma(1-\delta).
\tag{27}
\]

The `o(1)` is uniform on each fixed-ratio terminal shell `[X/q,X]`. Hence

\[
\int_{X/q}^{X}F(y)\frac{dy}{y}
\le
 a_\delta(\sigma)(\log q)\log X
+o(\log X).
\tag{28}
\]

Insert this in (24), divide by `W_X=log(X/H_*)`, let `X->infinity`, and then let `sigma` decrease to `Theta`. This proves (7).

Exponentiating (7) gives (8). Weighted AM--GM also yields the arithmetic occupation consequence

\[
\boxed{
\liminf_{X\to\infty}
\frac1{W_X}
\sum_{H=H_*}^{X-1}
\lambda_H\nu_H
\ge c_{q,\delta}.
}
\tag{29}
\]

No lower regular-variation law for the physical energy is assumed. The energy may jump, plateau, or oscillate subpolynomially; only its zero-frontier upper envelope enters through the final boundary shell.

## 4. Lower-tail sparsity and the linear-head constant

Every entropy term in (7) is nonnegative because `0<nu_H<=1`. On the set `nu_H<=eta`,

\[
\log\frac1{\nu_H}\ge\log\frac1\eta.
\tag{30}
\]

Combining this with (7) proves (9). If `eta<c_(q,delta)`, then

\[
\frac{L_{q,\delta}}{\log(1/\eta)}<1,
\tag{31}
\]

so the complementary set `nu_H>eta` has positive lower logarithmic density. If instead `eta=eta_X->0`, the same estimate divided by `log(1/eta_X)` shows that the logarithmic weight of the low-occupation set tends to zero.

For `q=4`, `w(4)=3/4`. Since `Theta<=1`,

\[
a_\delta(\Theta)\le2-\delta,
\tag{32}
\]

and therefore the unconditional bound is

\[
\boxed{
c_{4,\delta}\ge\frac{3}{4^{3-\delta}}.}
\tag{33}
\]

At `delta=0`, this reduces to the fixed-head all-horizon constant of `FD-050`. At `delta=1`, equation (5) gives `a_1(Theta)=1` identically, so (11) follows. The same constant also holds for every `delta` under RH because `a_delta(1/2)=1`.

The important point is not the numerical value `3/16` by itself. `FD-067` already obtains it along one four-adic chain at a linear head. Equation (11) promotes the same zero-frontier-independent occupation scale to a **global logarithmic statement over all horizons**.

## 5. The Schur scalar loss recurs on positive logarithmic scale

Let

\[
\varepsilon_H:=\frac{\rho_{H,D_H}^2}{E_H},
\qquad
\mathfrak D_H
:=C_H-\widehat R_{H,D_H}
=\Delta_{H,D_H}\varepsilon_H.
\tag{34}
\]

As in `FD-065`--`FD-067`, nonsquarefree Jordan rows are transverse to the equality ray, so

\[
\varepsilon_H\ge\nu_H.
\tag{35}
\]

Whenever `D_H->infinity` and `2D_H<H`, `FD-065` gives

\[
\Delta_{H,D_H}\asymp D_H^{-1}.
\tag{36}
\]

Hence for every fixed `eta<c_(q,delta)`, a positive lower logarithmic density of horizons satisfies

\[
\boxed{
\mathfrak D_H
\gg_\eta\frac1{D_H}.
}
\tag{37}
\]

For `0<delta<1`, the hypotheses of (36) are automatic for the power schedules (18). For the linear schedule (20), `m>=3` gives `2D_H<H` eventually, and (37) becomes a recurrent all-horizon scalar loss of order `1/H` on a set of positive logarithmic density. For a genuinely fixed head, the leverage instead tends to a positive constant, recovering the fixed-head interpretation of `FD-050`.

Equation (37) should not be confused with a pointwise Franel estimate. It is a density statement for the Schur relaxation. In particular, it gives no lower bound at a prescribed adaptive spike horizon.

## 6. What this closes and what still escapes

`FD-050` showed that fixed-head occupation cannot be tiny on a positive amount of multiplicative scale, but its proof could not move the cutoff. `FD-067` showed that a moving head remains recurrently occupied on each fixed q-adic chain, but explicitly left cross-ray hopping open. Equations (3)--(9) combine the exact pieces and close the intermediate loophole: **for every q-subcovariant polynomial head, cross-ray hopping cannot make low occupation typical in global logarithmic scale.**

The surviving escape is thinner but still large enough to contain an RH countermechanism. A sequence of off-critical zero-frontier spikes can be arbitrarily sparse; nothing proved here forces those adaptively selected horizons to have positive logarithmic density or to intersect the good set in (9). Thus `FD-066`'s source-coherence threshold is untouched, and no new zero-free region follows.

A genuinely stronger next step would need one of three new inputs: a source theorem forcing zero-frontier spikes to occupy nonnegligible logarithmic scale, a pointwise coupling between spike size and the moving-head occupation at the same horizon, or a recurrence that controls the logarithmically sparse exceptional set rather than only its density. Repeating the present dilation telescope with more fixed `q` values does not by itself supply that localization.

## 7. Prior-art and falsification boundary

The load-bearing mathematics is internal: `FD-067` supplies the head-rescaled nonsquarefree injection, `FD-046`/`FD-065` supply the zero-frontier energy envelope, and `FD-065` supplies the Schur leverage estimate. The logarithmic scale telescope is elementary. A targeted audit across classical Smith/meet GCD-matrix and Jordan-totient factorization, Farey--Franel/Mertens discrepancy, recent Farey local-discrepancy work, and logarithmic-density formulations did not locate a statement matching the schedule-covariant inequality (3) together with the global growing-head bounds (7)--(9). No priority claim is made, and no new external theorem is load-bearing, so `SOURCES.md` requires no change.

The main falsification conditions are explicit. Nonsquarefreeness of `q` is essential to (14). The head covariance (1), not merely the power exponent (4), is what closes the lower-horizon energy to the same schedule; an arbitrarily oscillating head with the same exponent need not satisfy the telescope. The power law is used only to price the top boundary in (28). Logarithmic density is intrinsic to the multiplicative scale shift and must not be upgraded silently to natural density or a pointwise statement. Finally, the scalar conclusion (37) additionally requires the leverage regime `D_H->infinity` and `2D_H<H`; the occupation theorem (7)--(9) does not.