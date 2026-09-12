# FD-064 — power-gap short-interval transfer yields polynomial packets but preserves the two-thirds barrier

**Status:** `EXACT-DERIVED + LITERATURE-DERIVED + SOURCE-SPECIFIC + SHORT-INTERVAL-MOBIUS + POLYNOMIAL-PACKET + POWER-BUDGET-CLASSIFICATION + TWO-THIRDS-INVARIANCE + CUBE-ROOT-BARRIER + ROUTE-OBSTRUCTION`.

`FD-062`--`FD-063` use the Matomäki--Teräväinen all-short-interval Möbius estimate at a host scale logarithmically below the deterministic reciprocal-floor scale `X/|\mathcal H(X)|`. There the packet length is necessarily subpower because the first transferred interval already has length comparable with the source spike itself. A tempting escape is to move the host **above** that critical scale. Then the first transfer interval is polynomially shorter than the spike, so the spare power can be spent on a polynomially growing packet.

That escape is real locally but does not improve the current global occupation exponent. In fact the whole power-law family can be classified exactly. Let

\[
\Theta:=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\},
\qquad 0.55<\Theta<1,
\]

and choose a zero-frontier spike sequence

\[
A_X:=|\mathcal H(X)|=X^{\Theta+o(1)}.
\tag{1}
\]

Fix an all-short-interval exponent

\[
0.55<\vartheta<\Theta
\tag{2}
\]

and a host exponent `lambda` with

\[
\boxed{
1-\Theta<\lambda\le 1-\vartheta.
}
\tag{3}
\]

For every packet exponent

\[
\boxed{
0<\kappa<\Theta+\lambda-1,
}
\tag{4}
\]

put

\[
K_X:=\lfloor X^\kappa\rfloor,
\qquad
Y_X:=\frac18X^\lambda,
\tag{5}
\]

and consider every integer host

\[
Y_X\le q\le2Y_X.
\tag{6}
\]

With

\[
T_q:=qX,
\qquad
x_{q,d}:=\left\lfloor\frac{T_q}{q+d}\right\rfloor
\qquad(1\le d\le K_X),
\tag{7}
\]

one has uniformly over the whole host corridor and the whole polynomial packet

\[
\boxed{
\mathcal H(x_{q,d})=\mathcal H(X)+o(A_X).
}
\tag{8}
\]

Consequently, for every fixed Schur-head dimension `D`,

\[
\boxed{
U_{T_q,D}
\ge
\left(\frac1{4\zeta(2)}-o(1)\right)
K_XA_X^2
=
X^{2\Theta+\kappa+o(1)}
}
\tag{9}
\]

uniformly in `q`.

Thus the power gap between the zero frontier `Theta` and the short-interval scale available at the chosen host really can be converted into a polynomial packet. However, after normalization by the generic zero-frontier energy envelope, the best exponent obtainable anywhere in this family is already bounded by the combination of `FD-049` and `FD-061`. The apparent new power is exactly offset by the later evaluation horizon.

Moreover, every host reachable by a **direct uniform all-short-interval theorem with threshold above one half** remains strictly below the cube-root Jordan scale. The square-root short-interval threshold is exactly the phase boundary at which a transferred host packet first reaches `r\asymp T^(1/3)`.

## 1. The transfer budget is `kappa < Theta + lambda - 1`

For `q` in (6) and `1<=d<=K_X`, integrality of `X` gives

\[
h_{q,d}:=X-x_{q,d}
=
\left\lceil\frac{dX}{q+d}\right\rceil.
\tag{10}
\]

Because (4) and `Theta<1` imply `kappa<lambda`, one has `K_X=o(q)` uniformly. Hence eventually `q+d<=2q`, and the corridor constants in (5)--(6) give

\[
2dX^{1-\lambda}
\ll h_{q,d}
\ll dX^{1-\lambda},
\]

more precisely enough for the uniform power bounds

\[
\boxed{
X^{1-\lambda}\ll h_{q,d}
\ll X^{1-\lambda+\kappa}.
}
\tag{11}
\]

The lower constraint in (3) has two different meanings. First, the Matomäki--Teräväinen theorem used in `FD-048` applies to every interval of length at least `X^vartheta`. Since `lambda<=1-vartheta`, (11) gives

\[
h_{q,d}\gg X^{\vartheta}
\tag{12}
\]

for every packet row. Second, the upper endpoint in (11) stays below the zero-frontier spike scale because (4) is exactly

\[
1-\lambda+\kappa<\Theta.
\tag{13}
\]

In particular `h_(q,d)=o(X)`, so `x_(q,d)\sim X` uniformly.

The source transfer from `FD-048` therefore gives, for every fixed `0<eta<1/3`,

\[
|\mathcal H(X)-\mathcal H(x_{q,d})|
\ll_{\vartheta,\eta}
\frac{h_{q,d}}{(\log X)^{1/3-\eta}}
\ll
X^{1-\lambda+\kappa+o(1)}.
\tag{14}
\]

By (1) and (13), the final quantity is `o(A_X)`, proving (8). Unlike `FD-062`--`FD-063`, no logarithmic budget such as `B+kappa<1/3` is needed here: the strict power gap itself absorbs the logarithmic loss.

The condition `lambda>1-Theta` is exactly what makes a positive packet exponent possible. At the power-critical host

\[
\lambda=1-\Theta,
\tag{15}
\]

the right side of (4) collapses to zero, recovering the earlier fact that only subpower packet growth is available there from the present logarithmic-saving theorem. Moving the host outward by `X^delta` creates exactly `delta` powers of packet budget.

## 2. Four-adic density converts the whole power budget into nonsquarefree energy

For a fixed host let

\[
\mathcal D_q:=\{1\le d\le K_X:4\mid q+d\}.
\tag{16}
\]

As in `FD-063`,

\[
|\mathcal D_q|=\frac{K_X}{4}+O(1),
\tag{17}
\]

and every row `q+d` with `d\in\mathcal D_q` is nonsquarefree. Since `q\to\infty`, all these rows eventually exceed fixed `D`. The Jordan weight satisfies

\[
w(r)=\frac{J_2(r)}{r^2}\ge\frac1{\zeta(2)}.
\tag{18}
\]

Using (8),

\[
\begin{aligned}
U_{T_q,D}
&\ge
\sum_{d\in\mathcal D_q}
 w(q+d)\mathcal H(x_{q,d})^2\\
&\ge
\left(\frac1{4\zeta(2)}-o(1)\right)
K_XA_X^2,
\end{aligned}
\tag{19}
\]

uniformly throughout the corridor. This proves (9).

The packet is genuinely polynomial: `K_X=X^(kappa+o(1))`. Hence the subpower multiplicity in `FD-060`--`FD-063` was not an intrinsic limitation of reciprocal-floor transfer. It was a consequence of working at the critical host power `q=X^(1-Theta+o(1))`, where the first transferred interval already costs the full source amplitude at the power scale.

## 3. Global normalization has an exact two-parameter exponent

Let

\[
\nu_{T,D}:=\frac{U_{T,D}}{E_{T,D}}.
\]

`FD-046` gives for every fixed `sigma>Theta`

\[
E_{T,D}\ll_{D,\sigma}T^{2\sigma}.
\tag{20}
\]

For the present host family,

\[
T_q=qX=X^{1+\lambda+o(1)}.
\tag{21}
\]

Combining (1), (9), (20), and (21), then allowing `sigma` to approach `Theta` from the right, gives the power-scale loss exponent

\[
\boxed{
\beta(\Theta,\lambda,\kappa)
:=
\frac{2\Theta\lambda-\kappa}{1+\lambda}.
}
\tag{22}
\]

Precisely, for every `epsilon>0`, uniformly over all hosts in (6),

\[
\boxed{
T_q^{\,\beta(\Theta,\lambda,\kappa)+\epsilon}
\nu_{T_q,D}
\longrightarrow\infty.
}
\tag{23}
\]

along the spike sequence.

For fixed `lambda`, increasing the packet is always favorable, so the infimum allowed by the transfer budget (4) is obtained as `kappa` approaches `Theta+lambda-1` from below:

\[
\boxed{
 b_\Theta(\lambda)
:=
\inf_\kappa\beta(\Theta,\lambda,\kappa)
=
\frac{1-\Theta+(2\Theta-1)\lambda}{1+\lambda}.
}
\tag{24}
\]

The endpoint is an infimum rather than a claim at equality: the transfer proof needs the strict inequality (13). Arbitrarily small fixed losses recover exponents arbitrarily close to (24).

Now

\[
\boxed{
 b_\Theta'(\lambda)
=
\frac{3\Theta-2}{(1+\lambda)^2}.
}
\tag{25}
\]

This derivative explains the `Theta=2/3` crossover without any reference to the earlier CRT packet length.

If `Theta>2/3`, (25) is positive, so the best exponent is obtained by moving `lambda` **back toward** the critical host boundary `1-Theta`. There

\[
\lim_{\lambda\downarrow1-\Theta}b_\Theta(\lambda)
=
\frac{2\Theta(1-\Theta)}{2-\Theta}
=\beta_\Theta,
\tag{26}
\]

exactly the `FD-061` packet exponent. Polynomial packet growth farther out never improves it.

If `1/2<Theta<2/3`, (25) is negative, so one would instead push the host as far out as the short-interval theorem permits. At `lambda=1-vartheta`,

\[
 b_\Theta(1-\vartheta)
=
\frac{\Theta+\vartheta-2\Theta\vartheta}{2-\vartheta}.
\tag{27}
\]

But comparison with the all-horizon `FD-049` exponent gives the exact identity

\[
\boxed{
 b_\Theta(1-\vartheta)-(2\Theta-1)
=
\frac{2-3\Theta}{2-\vartheta}>0.
}
\tag{28}
\]

Thus `FD-049` remains strictly stronger. At `Theta=2/3`, equations (24)--(25) collapse to

\[
\boxed{
 b_{2/3}(\lambda)=\frac13
}
\tag{29}
\]

for every admissible host exponent. The crossover is therefore invariant across the entire direct power-gap packet family.

Combining the cases: **using only the current direct all-short-interval transfer plus the generic zero-frontier denominator envelope, no polynomial choice of host displacement and packet multiplicity improves the best power-scale occupation barrier already supplied by `FD-049` and `FD-061`.** The extra packet power is real, but its horizon cost exactly neutralizes it at the optimization level.

## 4. The same budget has a geometric phase boundary at the cube-root Jordan core

The packet rows satisfy `r=q+d=q(1+o(1))`, because `kappa<lambda`. Relative to their physical horizon `T_q=qX`,

\[
\boxed{
 r
=
T_q^{\,\alpha(\lambda)+o(1)},
\qquad
\alpha(\lambda):=\frac{\lambda}{1+\lambda}.
}
\tag{30}
\]

The all-short-interval applicability constraint `lambda<=1-vartheta` therefore gives

\[
\boxed{
\alpha(\lambda)
\le
\frac{1-\vartheta}{2-\vartheta}.
}
\tag{31}
\]

The right side is below `1/3` exactly when `vartheta>1/2`:

\[
\frac{1-\vartheta}{2-\vartheta}<\frac13
\quad\Longleftrightarrow\quad
\vartheta>\frac12.
\tag{32}
\]

Hence every packet accessible by the current Matomäki--Teräväinen direct all-interval theorem lies polynomially **inside** the `H^(1/3)` Jordan core isolated by `FD-037`. Since the published theorem requires every fixed `vartheta>0.55`, the largest row exponent reachable by this mechanism has supremum

\[
\boxed{
\frac{1-0.55}{2-0.55}
=
\frac9{29}
<\frac13.
}
\tag{33}
\]

This is not merely a numerical accident. To place the host row itself at the cube-root boundary one needs

\[
q\asymp T^{1/3},
\qquad T=qX,
\]

which is equivalent to

\[
q\asymp X^{1/2}.
\tag{34}
\]

The first reciprocal-floor displacement is then

\[
X-\left\lfloor\frac{qX}{q+1}\right\rfloor
\asymp\frac Xq
\asymp X^{1/2}.
\tag{35}
\]

Thus **square-root short-interval cancellation is exactly the direct-transfer threshold for reaching the cube-root Jordan boundary**. A theorem valid only for interval exponents strictly above one half can populate deeper parts of the core, possibly with polynomial packets, but cannot push this construction to or beyond the boundary where `FD-037` loses control.

This also explains the location of the `FD-063` packet on a false-RH frontier. There `q=X^(1-Theta+o(1))` and `T=X^(2-Theta+o(1))`, so

\[
q=T^{(1-\Theta)/(2-\Theta)+o(1)},
\tag{36}
\]

and

\[
\frac13-rac{1-\Theta}{2-\Theta}
=
\frac{2\Theta-1}{3(2-\Theta)}>0.
\tag{37}
\]

The logarithmic below-critical displacement in `FD-063` does not alter this power separation.

## 5. Prior-art boundary and what would actually change the frontier

The only external analytic theorem used here is the Matomäki--Teräväinen all-short-interval Möbius estimate already anchored in `SOURCES.md` and already transferred to `mathcal H` in `FD-048`. The zero-frontier denominator envelope is the existing `FD-046` consequence of the classical Mertens/zeta frontier. Four-adic row density is elementary and already used in `FD-063`. No new external theorem is load-bearing, so `SOURCES.md` requires no change.

A targeted literature search across Farey discrepancy, Möbius short intervals, Jordan-totient energies, and short-interval Farey/Mertens criteria located the expected classical and recent components but no statement matching the host/packet power-budget classification (22)--(29) or the exact square-root/cube-root phase relation (30)--(35). No novelty is claimed for any of the individual analytic ingredients.

The result is deliberately a **route classification**, not a proof that positive nonsquarefree occupation is impossible. It assumes the packet is transferred by direct endpoint cancellation on every required interval and normalizes only with the generic all-horizon energy envelope. It does not rule out a source-coupled same-horizon denominator theorem, a maximal/almost-all short-interval theorem whose exceptional set can be localized to the adaptive host corridor, a stronger arithmetic relation among different Jordan rows, or cancellation information below the square-root interval scale.

The practical frontier is therefore sharper in two independent senses. First, moving above the critical host to harvest polynomial packet multiplicity is not a missing power-scale optimization: the full two-parameter calculation already returns the existing `Theta=2/3` crossover. Second, the direct uniform short-interval route cannot confront the cube-root concentration escape of `FD-037` until its interval threshold reaches the square-root scale. Improvements that do neither of those things can still sharpen logarithms or local packet structure, but they cannot change these two power-level obstructions.