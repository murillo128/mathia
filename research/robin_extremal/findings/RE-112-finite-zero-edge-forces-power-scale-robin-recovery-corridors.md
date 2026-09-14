# RE-112 — finite zero edge forces power-scale Robin recovery corridors

**Status:** `LITERATURE+DERIVED + ZERO-EDGE-CONDITIONED + OFF-LINE-ZERO-DENSITY + LOG-FREE-FALSE-RH-PNT-EDGE + INTER-BLOCK-RECOVERY + EVENT-WORKLOAD + POWER-SCALE-CORRIDOR + FIRST-LAYER-SATURATION-PACKET + FALSE-RH-CONSEQUENCE + KV-MINIMAL-BRANCH-ELIMINATION + PRIOR-ART-AUDITED`.

`RE-109`--`RE-111` bound Robin recovery by the unconditional Korobov--Vinogradov PNT envelope. The first version of this finding replaced that envelope by the classical textbook consequence

\[
\psi(x)-x=O\!\left(x^\Theta(\log x)^2\right),
\qquad
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho,
\]

and obtained a power-scale inter-block corridor. In the false-RH finite-edge regime the two logarithms are not intrinsic. Once `Theta>1/2`, any fixed strip strictly to the right of the critical line contains only a sublinear number of zeros, so its reciprocal-ordinate mass is summable. Combining the standard truncated Riemann--von Mangoldt formula with Ingham's classical zero-density estimate gives

\[
\boxed{
\psi(x)-x=O_\Theta(x^\Theta)
}
\qquad\left(\frac12<\Theta<1\right).
\]

Consequently the full CA event sweep satisfies

\[
\boxed{
\Phi(x)=x+O_\Theta(x^\Theta),
}
\]

and the exact one-sided recovery budget of `RE-110` improves to

\[
\boxed{
V-Y\gg_\Theta h(C)Y^{2-\Theta}\log Y.
}
\]

For an adaptive false-RH witness of exponent `b`, this yields

\[
\boxed{
V-Y\gg_{\Theta,b}Y^{2-\Theta-b}\log Y.
}
\]

Thus for `b=1-Theta+eta` the selected quantitative blocks are separated on the almost-linear scale `Y^(1-eta) log Y`, and their fixed-`eta` packing in `[T,2T]` is `O_{Theta,eta}(T^eta/log T)`.

There is also a source-level rigidity statement. If a **short** recovery is within a constant factor of this sharpened minimum, then a fixed positive fraction of its crossed physical mass must be carried by ordinary first-layer prime events satisfying

\[
p-\vartheta(p)\asymp Y^\Theta
\]

with the recovery-favorable sign. The packet contains at least `gg h(C)Y^(2-Theta)` distinct primes, hence `gg_b Y^(2-Theta-b)` for the adaptive witnesses. The finite-edge frontier is therefore no longer a logarithmic artifact of the textbook PNT bound: improving it requires ruling out **CA-selected one-sided saturation of the true `Theta`-scale source envelope**.

No novelty is claimed for the truncated explicit formula or zero-density estimates separately. The line-specific content is their endpoint sharpening in this false-RH regime and its coupling to the exact CA recovery workload, block packing, and first-layer packet extraction.

## 1. Off-line zero density removes the textbook `log^2 x` loss

Assume

\[
\frac12<\Theta<1.
\tag{1}
\]

Choose a fixed

\[
\sigma_0
:=
\frac12+\min\!\left\{
\frac{\Theta-1/2}{2},\frac1{10}
\right\}.
\tag{2}
\]

Then `1/2<sigma_0<Theta` and `sigma_0<=3/5`. Ingham's zero-density estimate, already anchored and used in `RE-100`, gives

\[
N(\sigma_0,T)
\ll_{\sigma_0}
T^\kappa(\log T)^A,
\qquad
\kappa:=\frac{3(1-\sigma_0)}{2-\sigma_0}<1
\tag{3}
\]

for some fixed `A`. Dyadic summation therefore yields

\[
\boxed{
\sum_{\substack{\zeta(\rho)=0\\ \Re\rho\ge\sigma_0}}
\frac1{1+|\Im\rho|}<\infty.
}
\tag{4}
\]

Indeed the `j`-th dyadic block is

\[
\ll_{\sigma_0}
2^{-j}N(\sigma_0,2^{j+1})
\ll
2^{-(1-\kappa)j}(1+j)^A,
\]

and this is summable. Thus the zero contribution from a fixed off-critical half-strip is absolutely summable after the natural `1/rho` weight.

Use the standard truncated Riemann--von Mangoldt formula for the half-jump convention `psi_0`. Taking `T\asymp x` away from zero ordinates gives uniformly for `x>=2`

\[
\psi_0(x)-x
=
-\sum_{|\Im\rho|\le T}\frac{x^\rho}{\rho}
+O((\log x)^2).
\tag{5}
\]

For zeros with `Re rho<sigma_0`, the ordinary zero count gives

\[
\sum_{\substack{|\Im\rho|\le T\\ \Re\rho<\sigma_0}}
\left|\frac{x^\rho}{\rho}\right|
\ll
x^{\sigma_0}(\log x)^2
=o_\Theta(x^\Theta).
\tag{6}
\]

For the complementary zeros, (4) and `Re rho<=Theta` give

\[
\sum_{\substack{|\Im\rho|\le T\\ \Re\rho\ge\sigma_0}}
\left|\frac{x^\rho}{\rho}\right|
\ll_\Theta x^\Theta.
\tag{7}
\]

Hence

\[
\boxed{
\psi_0(x)-x=O_\Theta(x^\Theta).
}
\tag{8}
\]

At a prime power, `psi-psi_0=O(log x)`, so

\[
\boxed{
\psi(x)-x=O_\Theta(x^\Theta).
}
\tag{9}
\]

This mechanism fails exactly at `Theta=1/2`: there is then no fixed `sigma_0` strictly between the critical line and the zero edge, and the reciprocal-ordinate mass of critical-line zeros has the familiar logarithmic divergence. Finally,

\[
\psi(x)-\vartheta(x)
=O\!\left(x^{1/2}(\log x)^2\right)
=o_\Theta(x^\Theta),
\]

so

\[
\boxed{
\vartheta(x)-x=O_\Theta(x^\Theta).
}
\tag{10}
\]

The exponent `Theta` cannot be replaced by any fixed smaller exponent using the zero edge alone: the classical Landau/explicit-formula mechanism gives errors of size `Omega(x^(Theta-epsilon))` for every fixed `epsilon>0`.

## 2. The CA event sweep and Robin recovery inherit the log-free envelope

For the full CA event sweep, `RE-069` gives

\[
\Phi_1(x)=\vartheta(x)+O(\log x),
\tag{11}
\]

while all higher active layers contribute only

\[
\Phi_{\ge2}(x)
=O\!\left(x^{1/2}(\log x)^{3/2}\right).
\tag{12}
\]

Since `Theta>1/2`, (10)--(12) imply

\[
\boxed{
\Phi(x)=x+O_\Theta(x^\Theta),
\qquad
\Phi(x^-)=x+O_\Theta(x^\Theta).
}
\tag{13}
\]

Let `C<D` be CA states and put

\[
Y:=\log C,
\qquad
V:=\log D,
\qquad
L:=V-Y,
\tag{14}
\]

with `h(C)>0` and `h(D)<=0`. For crossed event groups, `RE-110` defines

\[
M_+(C,D)
:=
\max_e(\eta_e-u_e)_+,
\qquad
u_e:=\Phi(\eta_e^-),
\tag{15}
\]

and proves

\[
\boxed{
L M_+(C,D)
\ge
(1+o(1))h(C)Y^2\log Y.
}
\tag{16}
\]

First suppose `L<=Y`. Every physical coordinate `u_e` then lies in `[Y,2Y]`. If a crossed event has positive forward defect, (13) gives

\[
u_e=\eta_e+O_\Theta(\eta_e^\Theta).
\]

Because `Theta<1`, any event contributing to `M_+` has `eta_e\asymp Y`, so

\[
\boxed{
M_+(C,D)\ll_\Theta Y^\Theta.
}
\tag{17}
\]

Substitution in (16) gives

\[
\boxed{
L\gg_\Theta h(C)Y^{2-\Theta}\log Y.
}
\tag{18}
\]

If `L>Y`, that branch already supplies a larger displacement whenever the right side of (18) is sublinear. Uniformly,

\[
\boxed{
L
\gg_\Theta
\min\!\left\{
Y,
 h(C)Y^{2-\Theta}\log Y
\right\}.
}
\tag{19}
\]

Relative to the first version of `RE-112`, the power exponent is unchanged but the exact corridor scale is larger by `(log Y)^2`.

## 3. Adaptive false-RH blocks are almost linearly separated

Let `C=C_b` be a regular adaptive-amplitude witness from `RE-034`, for fixed

\[
1-\Theta<b<\frac12.
\tag{20}
\]

Its actual Robin height satisfies

\[
h(C)\gg_bY^{-b}.
\tag{21}
\]

Set

\[
\alpha:=2-\Theta-b.
\]

Then

\[
\frac12<\alpha<1.
\tag{22}
\]

Since `Y^alpha log Y=o(Y)`, equations (19)--(21) give

\[
\boxed{
V-Y\gg_{\Theta,b}Y^{2-\Theta-b}\log Y.
}
\tag{23}
\]

Order the selected states belonging to distinct quantitative counterexample blocks for this fixed `b` by logarithmic scales `Y_k`. The next positive block cannot begin before the current one reaches its first nonpositive state, hence

\[
Y_{k+1}-Y_k
\gg_{\Theta,b}
Y_k^{2-\Theta-b}\log Y_k.
\tag{24}
\]

Therefore the number `N_b(T)` of selected quantitative blocks with `T<=Y_k<2T` obeys

\[
\boxed{
N_b(T)
\ll_{\Theta,b}
\frac{T^{\Theta+b-1}}{\log T}.
}
\tag{25}
\]

For every fixed `0<eta<Theta-1/2`, choose `b=1-Theta+eta`. Then

\[
\boxed{
V-Y\gg_{\Theta,\eta}Y^{1-\eta}\log Y,
\qquad
N_\eta(T)
\ll_{\Theta,\eta}
\frac{T^\eta}{\log T}.
}
\tag{26}
\]

This remains a family-by-family statement for each fixed `eta`; varying `eta` changes the selected adaptive family and does not imply a single-family `T^{o(1)}` bound.

## 4. Near-minimal short recovery forces a positive-mass `Theta`-saturation packet

The log-free envelope also upgrades the packet mechanism of `RE-111`. Assume `C=C_b` is an adaptive witness as above and that its first recovery satisfies both

\[
L\le Y
\tag{27}
\]

and the near-minimal upper bound

\[
L
\ll_{\Theta,b}
 h(C)Y^{2-\Theta}\log Y.
\tag{28}
\]

By (18), `L` is then comparable with the spectral minimum.

Use the physical/event partition from `RE-110`. A crossed event group at coordinate `eta_e`, with logarithmic mass `m_e`, occupies

\[
I_e=(u_e,u_e+m_e],
\qquad
u_e:=\Phi(\eta_e^-),
\tag{29}
\]

and these intervals partition `(Y,V]`. On `I_e` set

\[
Q(s):=\eta_e,
\qquad
f(s):=(Q(s)-s)_+.
\]

Then

\[
\mathcal W_+(C,D)
=
\int_Y^V f(s)\,ds
\ge
(1-o(1))A,
\qquad
A:=h(C)Y^2\log Y.
\tag{30}
\]

Equation (13) gives the uniform height bound

\[
0\le f(s)\ll_\Theta Y^\Theta.
\tag{31}
\]

Put

\[
T_*:=\frac{A}{4L},
\qquad
S:=\{s\in(Y,V]:f(s)\ge T_*\}.
\]

The layer-cake estimate used in `RE-111` gives

\[
\boxed{
|S|
\gg_\Theta
\frac{A}{Y^\Theta}
=
 h(C)Y^{2-\Theta}\log Y.
}
\tag{32}
\]

Together with (28), this shows `|S|\gg L`: a fixed positive fraction of the recovery mass lies in marked event groups.

The entire higher-layer atomic mass at scale `Y` is only

\[
O\!\left(Y^{1/2}(\log Y)^{3/2}\right).
\tag{33}
\]

Using (21) and `alpha>1/2`, the right side of (32) is

\[
\gg_bY^\alpha\log Y,
\]

so (33) is `o(|S|)`. After deleting every higher-layer atom from the marked groups, a fixed positive fraction of the marked mass remains on distinct ordinary first-layer prime events.

For each surviving marked first-layer prime `p`, the transfer argument of `RE-111` gives

\[
p-\vartheta(p)
\gg
T_*
\asymp
\frac{h(C)Y^2\log Y}{L}.
\tag{34}
\]

The near-minimal upper bound (28) yields

\[
p-\vartheta(p)\gg_\Theta Y^\Theta,
\]

while (10) supplies the matching global upper bound for `p\asymp Y`. Therefore

\[
\boxed{
p-\vartheta(p)\asymp_\Theta Y^\Theta}
\tag{35}
\]

with the recovery-favorable sign for every marked first-layer prime.

Their total first-layer logarithmic mass is `gg L`; since `log p\asymp log Y`,

\[
\boxed{
\#P(C,D)
\gg_\Theta
\frac{L}{\log Y}
\gg_\Theta
h(C)Y^{2-\Theta}.
}
\tag{36}
\]

For adaptive witnesses this becomes

\[
\boxed{
\#P(C,D)
\gg_{\Theta,b}
Y^{2-\Theta-b}.
}
\tag{37}
\]

In particular, choosing `b=1-Theta+eta`, a near-minimal short recovery forces at least `gg Y^(1-eta)` distinct first-layer primes with one-sided Chebyshev deficit of full `Theta`-scale. A single extreme event, sparse higher-layer activity, or the logarithmic slack in the textbook PNT bound cannot pay the recovery bill.

## 5. The unconditional KV-minimal branch survives only at `Theta=1`

Write the unconditional envelope used by `RE-109`--`RE-111` as

\[
\mathcal E(Y)
=
\exp\!\left[-a(\log Y)^{3/5}(\log\log Y)^{-1/5}\right].
\]

Within its standing short-corridor hypothesis, `RE-111` studies recovery on the scale

\[
L
\ll
\frac{h(C)Y\log Y}{\mathcal E(Y)}.
\tag{38}
\]

If `Theta<1`, the sharpened lower scale (18) divided by the right side of (38) is

\[
Y^{1-\Theta}\mathcal E(Y)
\longrightarrow\infty,
\tag{39}
\]

because `mathcal E(Y)=Y^{-o(1)}`. Hence

\[
\boxed{
\text{an unbounded family of `RE-111` KV-minimal recoveries}
\Longrightarrow
\Theta=1.
}
\tag{40}
\]

For every finite zero edge, the relevant saturation object is instead the `Theta`-scale first-layer packet of Section 4.

## 6. Matched control, prior-art boundary, and the new source target

The sharpened scales are already optimal for the information used here. A relaxed monotone event staircase on a physical interval of length

\[
L_0\asymp hY^{2-\Theta}\log Y
\]

with forward defect `M\asymp Y^Theta` has area

\[
L_0M\asymp hY^2\log Y,
\]

exactly matching the `RE-110` recovery budget. Splitting that interval into logarithmic atoms produces `asymp hY^(2-Theta)` marked atoms, matching (36). This synthetic control is not asserted to arise from the ordinary primes; it shows that **recovery area + scalar zero edge + event atomicity** cannot improve the new orders.

The analytic sharpening in Section 1 uses only standard ingredients already anchored in `SOURCES.md`: the truncated Riemann--von Mangoldt explicit formula and Ingham's fixed off-critical zero-density theorem. A current prior-art audit also found modern refinements of the explicit truncation error and work on large PNT-error sets, but no CA-selected recovery implication of the form above. No novelty is claimed for the analytic ingredients or for generic PNT large-value questions; the novelty claim is restricted to their coupling with the CA recovery identity and adaptive Robin witnesses.

The finite-edge target is now precise. Improving (23) cannot come from recovering the two textbook logarithms; they are already absent. One must show that CA-selected recovery intervals cannot carry a positive-mass packet of ordinary first-layer primes with

\[
p-\vartheta(p)\asymp Y^\Theta
\]

and the recovery-favorable sign. That requires source information beyond the scalar zero edge, such as phase or density information conditioned on the selected interval. The `Theta=1` branch remains separate and continues to be governed by the unconditional `RE-109`--`RE-111` anti-saturation problem.