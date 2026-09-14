# RE-112 — finite zero edge forces power-scale Robin recovery corridors

**Status:** `LITERATURE+DERIVED + ZERO-EDGE-CONDITIONED + INTER-BLOCK-RECOVERY + EVENT-WORKLOAD + POWER-SCALE-CORRIDOR + FALSE-RH-CONSEQUENCE + KV-MINIMAL-BRANCH-ELIMINATION + PRIOR-ART-AUDITED`.

`RE-109`--`RE-111` bound Robin recovery by the unconditional Korobov--Vinogradov PNT envelope. That is the correct unconditional envelope, but it throws away information already present in the false-RH parameter

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho.
\]

If `Theta<1`, the classical explicit-formula bound is polynomially stronger: Montgomery--Vaughan record

\[
\psi(x)=x+O\!\left(x^\Theta(\log x)^2\right).
\]

Feeding that bound into the exact one-sided recovery budget of `RE-110` changes the corridor scale by a genuine power. For the adaptive false-RH witnesses of `RE-034`, recovery to the next nonpositive Robin state satisfies

\[
\boxed{
V-Y\gg_{\Theta,b}\frac{Y^{2-\Theta-b}}{\log Y}.
}
\]

Consequently, if `b=1-Theta+eta`, the quantitative blocks selected at that exponent are separated on the almost-linear scale

\[
Y^{1-\eta}/\log Y,
\]

and the corresponding fixed-`eta` family has at most `O_{Theta,eta}(T^eta log T)` selected blocks with logarithmic scale in `[T,2T]`. In particular, the `RE-111` branch in which recovery occurs at the *unconditional* Korobov--Vinogradov minimum is impossible for every fixed `Theta<1`; an unbounded sequence of such recoveries would force the extreme alternative `Theta=1`.

No novelty is claimed for the classical relation between `Theta` and the PNT error exponent. The new statement is its coupling to the exact CA event-workload recovery identity and the adaptive Robin amplitude floor.

## 1. The full CA event sweep inherits the `Theta`-power PNT envelope

Assume RH is false and

\[
\frac12<\Theta<1.
\tag{1}
\]

A classical explicit-formula consequence, recorded for example in Montgomery--Vaughan, is

\[
\boxed{
\psi(x)-x
=O_\Theta\!\left(x^\Theta(\log x)^2\right).
}
\tag{2}
\]

Since

\[
\psi(x)-\vartheta(x)
=O\!\left(x^{1/2}(\log x)^2\right),
\tag{3}
\]

and `Theta>1/2`, this gives

\[
\vartheta(x)-x
=O_\Theta\!\left(x^\Theta(\log x)^2\right).
\tag{4}
\]

For the full CA event sweep `Phi`, `RE-069` gives

\[
\Phi_1(x)=\vartheta(x)+O(\log x),
\tag{5}
\]

while the higher active layers contribute only

\[
\Phi_{\ge2}(x)
=O\!\left(x^{1/2}(\log x)^{3/2}\right).
\tag{6}
\]

Therefore, uniformly for large real `x`,

\[
\boxed{
\Phi(x)
=x+O_\Theta\!\left(x^\Theta(\log x)^2\right).
}
\tag{7}
\]

Taking `t\uparrow x` in this uniform estimate gives the same bound directly for the left limit,

\[
\Phi(x^-)
=x+O_\Theta\!\left(x^\Theta(\log x)^2\right).
\tag{8}
\]

Thus the one-sided event workload itself has the spectral envelope

\[
\boxed{
\bigl(x-\Phi(x^-)\bigr)_+
\ll_\Theta x^\Theta(\log x)^2.
}
\tag{9}
\]

No event-tie multiplicity estimate is needed for this passage to the left limit. Equation (2) is the only new literature input in the finding.

## 2. The `RE-110` recovery budget becomes a power-scale corridor

Let `C<D` be CA states with

\[
Y:=\log C,
\qquad
V:=\log D,
\qquad
L:=V-Y,
\tag{10}
\]

and suppose

\[
h(C)>0,
\qquad
h(D)\le0.
\tag{11}
\]

For the crossed event groups, `RE-110` defines

\[
M_+(C,D)
:=
\max_e(\eta_e-u_e)_+,
\qquad
u_e:=\Phi(\eta_e^-),
\tag{12}
\]

and proves the exact one-sided budget

\[
\boxed{
L M_+(C,D)
\ge
(1+o(1))h(C)Y^2\log Y.
}
\tag{13}
\]

First suppose `L<=Y`. Then every physical coordinate `u_e` lies in `[Y,2Y]`. If a crossed event has positive forward defect, (8) gives

\[
u_e
=\eta_e+O_\Theta\!\left(\eta_e^\Theta(\log\eta_e)^2\right).
\tag{14}
\]

Because `Theta<1`, the error is `o(eta_e)`. Hence `eta_e asymp Y` uniformly over every event contributing to `M_+`, and therefore

\[
\boxed{
M_+(C,D)
\ll_\Theta
Y^\Theta(\log Y)^2.
}
\tag{15}
\]

Substitution into (13) yields

\[
\boxed{
L
\gg_\Theta
\frac{h(C)Y^{2-\Theta}}{\log Y}.
}
\tag{16}
\]

If instead `L>Y`, that already supplies a larger corridor whenever the right side of (16) is `o(Y)`. Uniformly, without deciding which branch occurs, one may state

\[
\boxed{
L
\gg_\Theta
\min\!\left\{
Y,
\frac{h(C)Y^{2-\Theta}}{\log Y}
\right\}.
}
\tag{17}
\]

The role of the `Theta<1` hypothesis is now transparent: it converts the qualitative PNT localization of event coordinates into a power envelope for the workload that a fast recovery is allowed to use.

## 3. Quantitative false-RH witnesses are separated almost linearly

Now let `C=C_b` be a regular adaptive-amplitude witness from `RE-034`, for fixed

\[
1-\Theta<b<\frac12.
\tag{18}
\]

Its actual Robin height satisfies

\[
\boxed{
h(C)\gg_b Y^{-b}.}
\tag{19}
\]

Let `D` be the first later CA state with nonpositive Robin height. Since

\[
\alpha:=2-\Theta-b<1
\tag{20}
\]

by `b>1-Theta`, the scale `Y^alpha/log Y` is `o(Y)`. Thus (17)--(19) give, in either the short- or long-corridor branch,

\[
\boxed{
V-Y
\gg_{\Theta,b}
\frac{Y^{2-\Theta-b}}{\log Y}.
}
\tag{21}
\]

Order the adaptive selected states belonging to distinct quantitative counterexample blocks for this fixed `b` by their logarithmic scales `Y_k`. Before the next positive block can begin, the current block must pass through its first nonpositive state. Hence

\[
Y_{k+1}-Y_k
\ge V_k-Y_k
\gg_{\Theta,b}
\frac{Y_k^{2-\Theta-b}}{\log Y_k}.
\tag{22}
\]

Consequently the number `N_b(T)` of these selected quantitative blocks with

\[
T\le Y_k<2T
\]

obeys

\[
\boxed{
N_b(T)
\ll_{\Theta,b}
T^{\Theta+b-1}\log T.
}
\tag{23}
\]

For every fixed

\[
0<\eta<\Theta-\frac12,
\tag{24}
\]

we may choose

\[
b=1-\Theta+\eta,
\tag{25}
\]

which lies in the admissible interval. The quantitative family selected for that fixed exponent then satisfies

\[
\boxed{
V-Y
\gg_{\Theta,\eta}
\frac{Y^{1-\eta}}{\log Y},
\qquad
N_\eta(T)
\ll_{\Theta,\eta}
T^\eta\log T.
}
\tag{26}
\]

Thus choosing `b` arbitrarily close to the zero-edge threshold `1-Theta` produces corresponding quantitative block families with arbitrarily small **fixed** polynomial packing exponent. This does not assert a `T^{o(1)}` bound for one fixed family, because the selected family changes with `b`.

This is not a contradiction. Robin's quantitative theorem supplies infinitely many such blocks, not a positive density of them.

## 4. The `RE-111` Korobov--Vinogradov-minimal branch can occur only at `Theta=1`

Write the unconditional envelope used by `RE-109`--`RE-111` as

\[
\mathcal E(Y)
=
\exp\!\left[-a(\log Y)^{3/5}(\log\log Y)^{-1/5}\right].
\tag{27}
\]

Within its standing short-corridor hypothesis `L<=Y`, `RE-111` studies a near-minimal recovery satisfying

\[
L
\ll
\frac{h(C)Y\log Y}{\mathcal E(Y)}.
\tag{28}
\]

If `Theta<1`, the same hypothesis `L<=Y` makes (16) available. The ratio of that spectral lower scale to the right side of (28) is

\[
\frac{
 h(C)Y^{2-\Theta}/\log Y
}{
 h(C)Y\log Y/\mathcal E(Y)
}
=
\frac{Y^{1-\Theta}\mathcal E(Y)}{(\log Y)^2}
\longrightarrow\infty.
\tag{29}
\]

The convergence follows because `mathcal E(Y)=Y^{-o(1)}`. Therefore (28) is incompatible with (16) for all sufficiently large selected witnesses whenever `Theta<1`.

Hence

\[
\boxed{
\text{an unbounded family of `RE-111` KV-minimal recoveries}
\quad\Longrightarrow\quad
\Theta=1.
}
\tag{30}
\]

The first-layer PNT-saturation packet extracted in `RE-111` is therefore not the generic next obstruction in the finite-zero-edge branch. It is relevant only to the extreme possibility that nontrivial zeros approach the line `Re s=1` arbitrarily closely. For every fixed `Theta<1`, the correct recovery benchmark is instead the power scale (21).

## 5. Sharpness boundary and prior art

The PNT input (2) is classical. Montgomery and Vaughan explicitly record that if `Theta` is the supremum of the real parts of zeta zeros then

\[
\psi(x)=x+O\!\left(x^\Theta(\log x)^2\right),
\]

and the same classical Landau/explicit-formula mechanism gives errors of size `Omega(x^{Theta-epsilon})` for every `epsilon>0`. Thus the exponent `Theta` in the workload envelope cannot be replaced, from knowledge of the zero edge alone, by any fixed smaller exponent.

This also supplies the matched-control boundary for (21). A relaxed monotone event staircase allowed a forward defect of order `Y^Theta` over a corridor of length `L` can make the product `L M_+` saturate the exact budget (13) at exponent level. Therefore improving the exponent `2-Theta-b` requires more than the global location of zeta zeros; it needs source information conditioned on the CA-selected recovery interval.

A current prior-art search found the classical zero-edge/PNT relation and neighboring Robin/CA work using ordinary Chebyshev and Mertens bounds, but no result coupling the `Theta`-power PNT envelope to the exact CA recovery workload or deriving the block-packing law (23). The novelty claim is restricted to that coupling.

## Consequence for the research line

The inter-block frontier now splits cleanly by the zero edge.

- If `Theta<1`, do not spend further effort trying to exclude the unconditional-envelope saturation packets of `RE-111`; they cannot govern asymptotically minimal recovery. The available spectral information already forces the stronger power-scale corridor (21), and the fixed-`b` quantitative block families obey the packing law (23).
- If `Theta=1`, the power refinement disappears and `RE-109`--`RE-111` remain the relevant unconditional frontier. In that extreme branch, excluding one-sided Korobov--Vinogradov saturation on CA-selected recovery intervals is still a genuine source-specific target.

A useful next theorem in the finite-zero-edge branch would have to exploit more than the scalar zero edge `Theta`: for example, density or phase information capable of making the `Y^Theta` workload envelope non-saturable on the adaptively selected corridors.