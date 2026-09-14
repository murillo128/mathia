# RE-112 — finite zero edge forces power-scale Robin recovery corridors

**Status:** `LITERATURE+DERIVED + ZERO-EDGE-CONDITIONED + OFF-LINE-ZERO-DENSITY + LOG-FREE-FALSE-RH-PNT-EDGE + INTER-BLOCK-RECOVERY + EVENT-WORKLOAD + POWER-SCALE-CORRIDOR + FIRST-LAYER-SATURATION-PACKET + FALSE-RH-CONSEQUENCE + KV-MINIMAL-BRANCH-ELIMINATION + PRIOR-ART-AUDITED`.

`RE-109`--`RE-111` bound Robin recovery by the unconditional Korobov--Vinogradov PNT envelope. The first version of this finding replaced that envelope by the classical textbook consequence

\[
\psi(x)-x=O\!\left(x^\Theta(\log x)^2\right),
\qquad
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho,
\]

and obtained a power-scale inter-block corridor. In the false-RH finite-edge regime this still leaves two unnecessary logarithms. The reason is structural: once `Theta>1/2`, any fixed strip strictly to the right of the critical line contains only a sublinear number of zeros, so its reciprocal-ordinate mass is summable.

Combining the standard truncated Riemann--von Mangoldt formula with Ingham's classical zero-density estimate gives the sharper endpoint bound

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

For an adaptive false-RH witness of exponent `b`, this becomes

\[
\boxed{
V-Y\gg_{\Theta,b}Y^{2-\Theta-b}\log Y.
}
\]

Thus for `b=1-Theta+eta` the selected quantitative blocks are separated on the almost-linear scale `Y^(1-eta) log Y`, and their fixed-`eta` packing in `[T,2T]` is `O_{Theta,eta}(T^eta/log T)`.

There is also a source-level rigidity statement. If recovery is within a constant factor of this sharpened minimum, then a fixed positive fraction of the crossed physical mass must be carried by ordinary first-layer prime events satisfying

\[
p-\vartheta(p)\asymp Y^\Theta
\]

with the recovery-favorable sign. The packet contains at least `gg h(C)Y^(2-Theta)` distinct primes, hence `gg_b Y^(2-Theta-b)` for the adaptive witnesses. So the finite-edge frontier is no longer a logarithmic artifact of the textbook PNT bound: improving it requires ruling out **CA-selected one-sided saturation of the true `Theta`-scale source envelope**.

No novelty is claimed for the truncated explicit formula, zero-density estimates, or their standard PNT consequences separately. The line-specific content is the density-assisted endpoint sharpening and its coupling to the exact CA recovery workload, block packing, and first-layer packet extraction.

## 1. Off-line zero density removes the textbook `log^2 x` loss when `Theta>1/2`

Assume RH is false and

\[
\frac12<\Theta<1.
\tag{1}
\]

Choose once and for all

\[
\sigma_0
:=
\frac12+\min\!\left\{
\frac{\Theta-1/2}{2},\frac1{10}
\right\}.
\tag{2}
\]

Then

\[
\frac12<\sigma_0<\Theta,
\qquad
\sigma_0\le\frac35.
\]

Ingham's classical zero-density estimate, in the notation already used in `RE-100`, gives

\[
N(\sigma_0,T)
\ll_{\sigma_0}
T^{\kappa}(\log T)^A,
\qquad
\kappa
:=
\frac{3(1-\sigma_0)}{2-\sigma_0}
<1
\tag{3}
\]

for some fixed `A`. The strict inequality is exactly equivalent to `sigma_0>1/2`.

Dyadic summation now gives an elementary but decisive consequence:

\[
\begin{aligned}
\sum_{\substack{\zeta(\rho)=0\\ \Re\rho\ge\sigma_0}}
\frac1{1+|\Im\rho|}
&\ll_{
\sigma_0}
1+
\sum_{j\ge0}
2^{-j}N(\sigma_0,2^{j+1})\\
&\ll_{
\sigma_0}
1+
\sum_{j\ge0}
2^{-(1-\kappa)j}(1+j)^A
<\infty.
\end{aligned}
\tag{4}
\]

Thus the zero contribution from the fixed off-critical half-strip `Re rho>=sigma_0` is absolutely summable after the natural `1/rho` weight.

Use the standard truncated Riemann--von Mangoldt formula for the half-jump convention `psi_0`. Taking a truncation height `T\asymp x` away from zero ordinates gives uniformly for `x>=2`

\[
\psi_0(x)-x
=
-
\sum_{|\Im\rho|\le T}
\frac{x^\rho}{\rho}
+O((\log x)^2).
\tag{5}
\]

Split the zero sum at `sigma_0`. For the left part, the ordinary zero count gives

\[
\sum_{\substack{|\Im\rho|\le T\\ \Re\rho<\sigma_0}}
\left|\frac{x^\rho}{\rho}\right|
\ll
x^{\sigma_0}(\log T)^2
\ll
x^{\sigma_0}(\log x)^2
=o_\Theta(x^\Theta).
\tag{6}
\]

For the right part, (4) and `Re rho<=Theta` give the uniform absolute estimate

\[
\sum_{\substack{|\Im\rho|\le T\\ \Re\rho\ge\sigma_0}}
\left|\frac{x^\rho}{\rho}\right|
\ll_\Theta
x^\Theta.
\tag{7}
\]

Equations (5)--(7) therefore yield

\[
\boxed{
\psi_0(x)-x=O_\Theta(x^\Theta).
}
\tag{8}
\]

At a prime power, `psi-psi_0=O(log x)`, so the same estimate holds for the usual right-continuous Chebyshev function:

\[
\boxed{
\psi(x)-x=O_\Theta(x^\Theta).
}
\tag{9}
\]

This sharpening fails exactly at the RH edge `Theta=1/2`: there is then no fixed `sigma_0` between `1/2` and `Theta`, and the reciprocal-ordinate mass of the critical-line zeros has the familiar logarithmic divergence. That is why the standard RH bound retains logarithms while a genuinely off-critical finite edge does not.

Finally,

\[
\psi(x)-\vartheta(x)
=O\!\left(x^{1/2}(\log x)^2\right)
=o_\Theta(x^\Theta),
\tag{10}
\]

so

\[
\boxed{
\vartheta(x)-x=O_\Theta(x^\Theta).
}
\tag{11}
\]

The exponent `Theta` cannot be replaced by any fixed smaller exponent on the basis of the zero edge alone: the classical Landau/explicit-formula mechanism gives `Omega(x^(Theta-epsilon))` for every fixed `epsilon>0`.

## 2. The full CA event sweep inherits the log-free `Theta` envelope

For the full CA event sweep `Phi`, `RE-069` gives

\[
\Phi_1(x)=\vartheta(x)+O(\log x),
\tag{12}
\]

while all higher active layers together contribute only

\[
\Phi_{\ge2}(x)
=O\!\left(x^{1/2}(\log x)^{3/2}\right).
\tag{13}
\]

Since `Theta>1/2`, equations (11)--(13) give

\[
\boxed{
\Phi(x)=x+O_\Theta(x^\Theta).
}
\tag{14}
\]

Taking `t\uparrow x` in the uniform estimate gives the same bound for the left limit,

\[
\boxed{
\Phi(x^-)=x+O_\Theta(x^\Theta).
}
\tag{15}
\]

and hence the forward workload envelope

\[
\boxed{
\bigl(x-\Phi(x^-)\bigr)_+
\ll_\Theta x^\Theta.
}
\tag{16}
\]

This is the key correction to the first version of the finding. The two logarithms in the earlier workload height were not intrinsic to a finite false-RH zero edge; they came from using a textbook bound that does not exploit the unconditional sparsity of off-critical zeros.

## 3. The `RE-110` recovery budget gains two logarithms

Let `C<D` be CA states with

\[
Y:=\log C,
\qquad
V:=\log D,
\qquad
L:=V-Y,
\tag{17}
\]

and suppose

\[
h(C)>0,
\qquad
h(D)\le0.
\tag{18}
\]

For the crossed event groups, `RE-110` defines

\[
M_+(C,D)
:=
\max_e(\eta_e-u_e)_+,
\qquad
u_e:=\Phi(\eta_e^-),
\tag{19}
\]

and proves

\[
\boxed{
L M_+(C,D)
\ge
(1+o(1))h(C)Y^2\log Y.
}
\tag{20}
\]

First suppose `L<=Y`. Then every physical coordinate `u_e` lies in `[Y,2Y]`. If a crossed event has positive forward defect, (15) gives

\[
u_e
=\eta_e+O_\Theta(\eta_e^\Theta).
\tag{21}
\]

Because `Theta<1`, the error is `o(eta_e)`. Hence every event contributing to `M_+` has `eta_e\asymp Y`, and therefore

\[
\boxed{
M_+(C,D)\ll_\Theta Y^\Theta.
}
\tag{22}
\]

Substituting into (20),

\[
\boxed{
L
\gg_\Theta
h(C)Y^{2-\Theta}\log Y.
}
\tag{23}
\]

If `L>Y`, that already supplies a larger corridor whenever the right side of (23) is `o(Y)`. Uniformly one may write

\[
\boxed{
L
\gg_\Theta
\min\!\left\{
Y,
 h(C)Y^{2-\Theta}\log Y
\right\}.
}
\tag{24}
\]

The power exponent is the same as in the first version of `RE-112`, but the exact corridor scale is larger by `(log Y)^2`.

## 4. Adaptive false-RH blocks are almost linearly separated with improved packing

Let `C=C_b` be a regular adaptive-amplitude witness from `RE-034`, for fixed

\[
1-\Theta<b<\frac12.
\tag{25}
\]

Its actual Robin height satisfies

\[
\boxed{
h(C)\gg_b Y^{-b}.}
\tag{26}
\]

Put

\[
\alpha:=2-\Theta-b.
\tag{27}
\]

The lower condition `b>1-Theta` gives `alpha<1`, while `Theta<1` and `b<1/2` give

\[
\boxed{
\frac12<\alpha<1.
}
\tag{28}
\]

Thus `Y^alpha log Y=o(Y)`, so (24)--(26) imply in either the short- or long-corridor branch

\[
\boxed{
V-Y
\gg_{\Theta,b}
Y^{2-\Theta-b}\log Y.
}
\tag{29}
\]

Order the adaptive selected states belonging to distinct quantitative counterexample blocks for this fixed `b` by logarithmic scales `Y_k`. Before the next positive block can begin, the current block must pass through its first nonpositive state. Hence

\[
Y_{k+1}-Y_k
\gg_{\Theta,b}
Y_k^{2-\Theta-b}\log Y_k.
\tag{30}
\]

Consequently the number `N_b(T)` of these selected quantitative blocks with `T<=Y_k<2T` satisfies

\[
\boxed{
N_b(T)
\ll_{\Theta,b}
\frac{T^{\Theta+b-1}}{\log T}.
}
\tag{31}
\]

For every fixed

\[
0<\eta<\Theta-\frac12,
\tag{32}
\]

choose

\[
b=1-\Theta+\eta.
\tag{33}
\]

Then

\[
\boxed{
V-Y
\gg_{\Theta,\eta}
Y^{1-\eta}\log Y,
\qquad
N_\eta(T)
\ll_{\Theta,\eta}
\frac{T^\eta}{\log T}.
}
\tag{34}
\]

As before, this is a family-by-family statement for each fixed `eta`; varying `eta` changes the selected adaptive family and does not imply a single-family `T^{o(1)}` bound.

## 5. Near-minimal finite-edge recovery forces a positive-mass `Theta`-saturation packet

The log-free envelope also upgrades the packet mechanism of `RE-111`. Assume `C=C_b` is an adaptive witness as above and that its first recovery to `h(D)<=0` is within a fixed constant factor of the new minimum,

\[
L
\ll_{\Theta,b}
 h(C)Y^{2-\Theta}\log Y.
\tag{35}
\]

By (23), `L` is then comparable with that scale. Because `alpha<1`, this branch automatically has `L<=Y` for large `Y`.

Use the physical/event partition from `RE-110`. A crossed event group at coordinate `eta_e`, with logarithmic mass `m_e`, occupies

\[
I_e=(u_e,u_e+m_e],
\qquad
u_e=\Phi(\eta_e^-),
\tag{36}
\]

and the intervals `I_e` partition `(Y,V]`. On `I_e` put

\[
Q(s):=\eta_e,
\qquad
f(s):=(Q(s)-s)_+.
\tag{37}
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
\tag{38}
\]

Equation (16) gives the uniform height bound

\[
0\le f(s)\ll_\Theta Y^\Theta.
\tag{39}
\]

Set

\[
T_*:=\frac{A}{4L},
\qquad
S:=\{s\in(Y,V]:f(s)\ge T_*\}.
\tag{40}
\]

The same layer-cake estimate as in `RE-111` gives

\[
\boxed{
|S|
\gg_\Theta
\frac{A}{Y^\Theta}
=
 h(C)Y^{2-\Theta}\log Y.
}
\tag{41}
\]

Under (35), equations (23) and (41) show `|S|\gg L`: the marked workload occupies a fixed positive proportion of the recovery mass.

The total higher-layer atomic mass available at scale `Y` is only

\[
O\!\left(Y^{1/2}(\log Y)^{3/2}\right).
\tag{42}
\]

For the adaptive witnesses, (26), (28), and (41) give

\[
|S|
\gg_b
Y^{2-\Theta-b}\log Y
=
Y^{\alpha}\log Y,
\qquad
\alpha>\frac12.
\tag{43}
\]

Thus (42) is `o(|S|)`. After deleting all higher-layer atoms from the marked event groups, a fixed positive fraction of the marked mass remains on distinct ordinary first-layer prime events.

For every surviving marked first-layer prime `p`, the transfer argument of `RE-111` gives

\[
p-\vartheta(p)
\gg
T_*
\asymp
\frac{h(C)Y^2\log Y}{L}.
\tag{44}
\]

The near-minimal upper bound (35) therefore implies

\[
p-\vartheta(p)
\gg_\Theta
Y^\Theta.
\tag{45}
\]

On the other hand, (11) gives the matching global upper bound for `p\asymp Y`. Hence every marked first-layer prime satisfies

\[
\boxed{
p-\vartheta(p)\asymp_\Theta Y^\Theta}
\tag{46}
\]

with the same recovery-favorable sign.

Their total first-layer logarithmic mass is `gg L`, so, since `log p\asymp log Y`, the packet has cardinality

\[
\boxed{
\#P(C,D)
\gg_\Theta
\frac{L}{\log Y}
\gg_\Theta
h(C)Y^{2-\Theta}.
}
\tag{47}
\]

For the adaptive amplitude floor,

\[
\boxed{
\#P(C,D)
\gg_{\Theta,b}
Y^{2-\Theta-b}.
}
\tag{48}
\]

In particular, for `b=1-Theta+eta`, a near-minimal recovery forces at least `gg Y^(1-eta)` distinct first-layer primes at which the one-sided Chebyshev deficit is of full `Theta`-scale.

This is the finite-edge analogue of `RE-111`, but with the correct spectral envelope. A single extreme event, a sparse collection of higher-layer events, or the logarithmic slack in the textbook PNT bound cannot pay the bill.

## 6. The unconditional KV-minimal branch can occur only at `Theta=1`

Write the unconditional envelope used by `RE-109`--`RE-111` as

\[
\mathcal E(Y)
=
\exp\!\left[-a(\log Y)^{3/5}(\log\log Y)^{-1/5}\right].
\tag{49}
\]

Within its standing short-corridor hypothesis, `RE-111` studies recovery on the unconditional minimum scale

\[
L
\ll
\frac{h(C)Y\log Y}{\mathcal E(Y)}.
\tag{50}
\]

If `Theta<1`, the sharpened spectral lower scale (23) divided by the right side of (50) is

\[
\frac{
 h(C)Y^{2-\Theta}\log Y
}{
 h(C)Y\log Y/\mathcal E(Y)
}
=
Y^{1-\Theta}\mathcal E(Y)
\longrightarrow\infty,
\tag{51}
\]

because `mathcal E(Y)=Y^{-o(1)}`. Therefore the KV-minimal branch is asymptotically incompatible with every fixed finite edge `Theta<1`.

Hence

\[
\boxed{
\text{an unbounded family of `RE-111` KV-minimal recoveries}
\quad\Longrightarrow\quad
\Theta=1.
}
\tag{52}
\]

The first-layer KV-saturation packet of `RE-111` remains relevant only in that extreme branch. For every finite zero edge, the correct packet is instead the `Theta`-scale packet of Section 5.

## 7. Matched control, prior-art boundary, and the new source target

The improved corridor and packet scales are already sharp for the information used here. A relaxed monotone event staircase on an interval of length

\[
L_0
\asymp
hY^{2-\Theta}\log Y
\tag{53}
\]

with forward defect

\[
M\asymp Y^\Theta
\tag{54}
\]

has positive workload area

\[
L_0M
\asymp
hY^2\log Y,
\tag{55}
\]

exactly matching `RE-110`. Splitting the interval into logarithmic atoms gives `asymp hY^(2-Theta)` marked atoms, matching (47). This synthetic control is not asserted to arise from the ordinary primes; it shows that **recovery area + scalar zero edge + event atomicity** alone cannot improve the new scales.

The analytic sharpening in Section 1 uses only standard ingredients: the truncated Riemann--von Mangoldt explicit formula and a fixed off-critical zero-density estimate. Ingham's density theorem is already load-bearing elsewhere in the line (`RE-100`), and Montgomery--Vaughan is already the source anchor for the zero-edge PNT relation used by the first version of this finding. A current prior-art search also found modern work sharpening the explicit truncation error and work on large PNT-error sets, but no CA-selected recovery statement of the form above. No novelty is claimed for the analytic ingredients or for generic large-value questions; the novelty claim is restricted to their coupling with the CA recovery identity and adaptive Robin witnesses.

The finite-edge research target is now more precise than the first version of `RE-112` suggested. It is not enough to improve the global PNT bound by logarithms: those logarithms have disappeared. To beat (29), one must show that CA-selected recovery intervals cannot carry a positive-mass packet of ordinary first-layer primes with

\[
p-\vartheta(p)\asymp Y^\Theta
\]

and the recovery-favorable sign. That requires source information beyond the scalar zero edge, such as phase or density information conditioned on the selected interval. The `Theta=1` branch remains separate and continues to be governed by the unconditional `RE-109`--`RE-111` anti-saturation problem.