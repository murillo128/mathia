# FD-062 — short-interval Möbius cancellation carries growing CRT packets below the deterministic host scale

**Status:** `EXACT-DERIVED + LITERATURE-DERIVED + SOURCE-SPECIFIC + SHORT-INTERVAL-MOBIUS + CRT-NONSQUAREFREE-PACKET + BELOW-CRITICAL-HOST + DIVERGING-LOCAL-OCCUPATION + ROUTE-REFINEMENT`.

`FD-055` and `FD-060` leave complementary pieces of the same transfer problem. `FD-055` uses genuine short-interval Möbius cancellation to move **one** nonsquarefree twin a logarithmic factor below the deterministic host scale `X/|\mathcal H(X)|`. `FD-060` creates a **growing** nonsquarefree CRT packet, but pays for it by moving the host a growing factor above that scale.

The two costs need not be paid separately. The logarithmic saving used in `FD-055` has enough room to carry a slowly growing CRT packet while the host remains below the deterministic threshold.

Let

\[
A_X:=|\mathcal H(X)|,
\qquad
L_X:=\log X.
\]

Fix

\[
\vartheta>0.55,
\qquad B>0,
\qquad \kappa>0,
\qquad B+\kappa<\frac13.
\tag{1}
\]

Suppose along an unbounded sequence that

\[
\boxed{A_XL_X^B\ge X^\vartheta.}
\tag{2}
\]

Then there are integers `K_X -> infinity` and squarefree hosts `q=q_X` such that

\[
K_X\le L_X^\kappa,
\qquad
\boxed{
\frac{1}{8L_X^B}
\le
\frac{qA_X}{X}
\le
\frac{1}{4L_X^B},
}
\tag{3}
\]

and every row

\[
q+1,q+2,\ldots,q+K_X
\]

is nonsquarefree. Thus

\[
\frac{qA_X}{X}\longrightarrow0.
\tag{4}
\]

Put

\[
T_X:=qX,
\qquad
x_d:=\left\lfloor\frac{T_X}{q+d}\right\rfloor
\quad(1\le d\le K_X).
\tag{5}
\]

The packet can be chosen so that, uniformly in `d`,

\[
\boxed{
\mathcal H(x_d)=\mathcal H(X)+o(A_X).
}
\tag{6}
\]

Consequently, for every fixed Schur-head dimension `D`,

\[
\boxed{
U_{T_X,D}
\ge
\left(\frac1{\zeta(2)}-o(1)\right)K_XA_X^2.
}
\tag{7}
\]

If

\[
J_q(T):=w(q)\mathcal H(\lfloor T/q\rfloor)^2,
\qquad
w(r):=\frac{J_2(r)}{r^2},
\]

then the squarefree host row satisfies `J_q(T_X)<=A_X^2`, so

\[
\boxed{
\frac{U_{T_X,D}}{J_q(T_X)}
\ge
\left(\frac1{\zeta(2)}-o(1)\right)K_X
\longrightarrow\infty.
}
\tag{8}
\]

Thus growing local nonsquarefree occupation does **not** intrinsically require the supercritical factor `qA_X/X -> infinity` of `FD-060`: known arithmetic short-interval cancellation supports `K_X -> infinity` while `qA_X/X -> 0`.

## 1. A nested CRT family fits inside the logarithmic cancellation budget

Choose once and for all distinct primes

\[
p_d>d
\qquad(d\ge1)
\]

and define the nested moduli

\[
M_K:=\prod_{d=1}^Kp_d^2.
\tag{9}
\]

For each `K`, the Chinese remainder theorem gives a class `a_K mod M_K` satisfying

\[
a_K\equiv-d\pmod{p_d^2}
\qquad(1\le d\le K).
\tag{10}
\]

Because `p_d>d`, no `p_d` divides `d`, hence

\[
\gcd(a_K,M_K)=1.
\tag{11}
\]

Every `q congruent a_K mod M_K` then obeys

\[
p_d^2\mid q+d
\qquad(1\le d\le K),
\tag{12}
\]

so `q+1,...,q+K` are all nonsquarefree.

Set

\[
R_X:=A_XL_X^B,
\qquad
Y_X:=\frac{X}{8R_X}.
\tag{13}
\]

The Davenport bound already used in `FD-055`,

\[
\mathcal H(X)
\ll_C
\frac{X}{(\log X)^C}+X^{1/2}
\qquad(C>0\text{ fixed}),
\tag{14}
\]

implies

\[
A_XL_X^{B+\kappa}=o(X),
\qquad
Y_X/L_X^\kappa\to\infty.
\tag{15}
\]

Choose `K_X` as the largest `K` satisfying

\[
K\le L_X^\kappa,
\qquad
M_K\le Y_X^{1/4}.
\tag{16}
\]

For every fixed `K`, both conditions eventually hold, so

\[
K_X\to\infty.
\tag{17}
\]

The squarefree progression count proved directly in `FD-060` gives, uniformly at the strength needed here,

\[
\#\{Y<n\le2Y:n\equiv a\pmod M,\ \mu(n)^2=1\}
=
\frac{Y}{M}C_M+O(\sqrt Y),
\tag{18}
\]

for `gcd(a,M)=1`, where

\[
C_M
=
\frac1{\zeta(2)}
\prod_{p\mid M}(1-p^{-2})^{-1}
\ge\frac1{\zeta(2)}.
\tag{19}
\]

With `M=M_(K_X)` and (16), the main term is `gg Y_X^(3/4)` while the error is `O(Y_X^(1/2))`. Hence for all sufficiently large `X` there is a **squarefree** host

\[
q\equiv a_{K_X}\pmod{M_{K_X}},
\qquad
Y_X\le q\le2Y_X.
\tag{20}
\]

Equations (12)--(13) give the packet, while (20) gives exactly (3). The diagonal restriction in (16) is used only to keep the elementary squarefree-host count positive; no uniform squarefree-distribution theorem for fast-growing moduli is imported.

## 2. The whole packet lies inside the available short-interval range

For `1<=d<=K_X`, let

\[
h_d:=X-x_d.
\]

Since `X` is integral,

\[
\boxed{
h_d=\left\lceil\frac{dX}{q+d}\right\rceil.}
\tag{21}
\]

Equation (15) and `K_X<=L_X^kappa` imply

\[
K_X=o(q),
\qquad
K_XR_X=o(X).
\tag{22}
\]

Using `Y_X<=q<=2Y_X`, for all sufficiently large `X` one has uniformly over the packet

\[
\boxed{
2R_X\le h_d\le9K_XR_X.
}
\tag{23}
\]

Indeed, `q+d<=2q` gives the lower bound from `q<=X/(4R_X)`, while `q>=X/(8R_X)` gives the upper bound.

By (2), `h_d>=2X^vartheta`; by (22), `h_d=o(X)` and hence `x_d~X`. Therefore the `FD-048` transfer of the Matomäki--Teräväinen all-short-interval estimate applies to every interval `(x_d,X]`:

\[
|\mathcal H(X)-\mathcal H(x_d)|
\ll_{\vartheta,\eta}
\frac{h_d}{(\log X)^{1/3-\eta}}
\tag{24}
\]

for every fixed `eta>0`.

Choose `eta` so that

\[
B+\kappa+\eta<\frac13.
\tag{25}
\]

Then

\[
\begin{aligned}
\max_{1\le d\le K_X}
|\mathcal H(X)-\mathcal H(x_d)|
&\ll
K_XA_XL_X^{B-1/3+\eta}\\
&\le
A_XL_X^{B+\kappa-1/3+\eta}
=o(A_X),
\end{aligned}
\tag{26}
\]

which proves (6). The logarithmic saving is split into two currencies: `L_X^B` moves the host below `X/A_X`, while up to `L_X^kappa` is reserved for packet width. The budget is precisely `B+kappa<1/3` at the strength of the present short-interval theorem.

## 3. The packet forces divergent local occupation on the subcritical side

Every `q+d` in the packet is nonsquarefree, and `q->infinity`, so all packet rows eventually lie above fixed `D`. Since

\[
w(r)\ge\frac1{\zeta(2)},
\tag{27}
\]

(6) gives

\[
\begin{aligned}
U_{T_X,D}
&\ge
\sum_{d=1}^{K_X}w(q+d)\mathcal H(x_d)^2\\
&\ge
\left(\frac1{\zeta(2)}-o(1)\right)K_XA_X^2,
\end{aligned}
\]

which is (7). The host itself is squarefree and samples the spike exactly because `floor(T_X/q)=X`, proving (8).

The contrast with `FD-060` is structural. There the deterministic one-Lipschitz mechanism needs

\[
q\asymp K_X\frac{X}{A_X},
\qquad
\frac{qA_X}{X}\asymp K_X\to\infty,
\]

because its worst quotient displacement is of order `K_XX/q`. Here instead

\[
\frac{qA_X}{X}\asymp L_X^{-B}\to0
\]

while `K_X->infinity`. Both the host and the furthest retained packet endpoint therefore lie beyond what bounded increments alone can protect.

## 4. On a false-RH frontier sequence the packet can grow by a fixed log power

Assume

\[
\Theta
:=
\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}
>0.55.
\tag{28}
\]

Choose `vartheta` with `0.55<vartheta<Theta`. `FD-046` supplies a sequence with

\[
A_X=X^{\Theta+o(1)}.
\tag{29}
\]

Then (2) holds eventually for every fixed `B>0`, and (3) gives

\[
q\asymp\frac{X}{A_XL_X^B},
\qquad
T_X=qX,
\tag{30}
\]

so

\[
\frac{\log q}{\log T_X}
\longrightarrow
\alpha_\Theta
:=
\frac{1-\Theta}{2-\Theta}.
\tag{31}
\]

Thus the power exponent is the same frontier exponent as in `FD-055`, but the same horizon now carries a diverging packet.

This can be made quantitative on the frontier sequence. Choose the fixed prime sequence above with the standard bound

\[
p_d\ll d\log d.
\]

Then

\[
\log M_K=O(K\log K).
\tag{32}
\]

For any fixed `kappa` satisfying (1), taking

\[
\boxed{K_X=\lfloor(\log X)^\kappa\rfloor}
\tag{33}
\]

still gives `M_(K_X)=X^{o(1)}`, while `Y_X=X^{1-Theta+o(1)}` up to logarithms. Hence (18) remains positive and (26) remains `o(A_X)`. On false-RH frontier spikes the short-interval budget therefore has the explicit tradeoff

\[
\boxed{B+\kappa<\frac13.}
\tag{34}
\]

`B` measures logarithmic penetration below the deterministic host scale and `kappa` measures logarithmic packet growth.

## 5. The remaining obstruction is the same-horizon denominator

The theorem still does not prove a positive lower bound for

\[
\nu_{T,D}:=\frac{U_{T,D}}{E_{T,D}}.
\]

Using only the `FD-046` envelope `E_(T,D)<<_(D,sigma)T^(2sigma)` for fixed `sigma>Theta` yields

\[
\nu_{T_X,D}
\gg_{D,\sigma}
K_XA_X^2T_X^{-2\sigma}.
\tag{35}
\]

Compared with the critical-scale host, the smaller horizon contributes a factor of roughly `(log X)^(2sigma B)` and the packet contributes `K_X`. However, the frontier spike relation `A_X=X^(Theta+o(1))` and the limiting passage `sigma downarrow Theta` contain uncontrolled subpower losses. Therefore (35) does **not** by itself justify a new sharp logarithmic exponent for `nu`; at polynomial resolution it returns the same `beta_Theta` barrier isolated in `FD-061`.

The research consequence is nevertheless stronger than `FD-060`: **row-count amplification and below-critical placement are compatible**. To convert that geometry into a stronger global occupation theorem, one now needs a denominator estimate on these same source-selected horizons, rather than a better CRT packet at the deterministic scale.

## 6. Prior-art and falsification boundary

The analytic input is exactly the Matomäki--Teräväinen all-short-interval Möbius theorem already anchored in `SOURCES.md` and transferred to `mathcal H` in `FD-048`. The CRT construction of consecutive nonsquarefree integers and the elementary squarefree progression count are the ingredients already isolated in `FD-060`. The prime-size estimate used only in the quantitative frontier corollary is covered by the existing prime-number-theorem anchor in `SOURCES.md`.

A targeted literature search around Farey discrepancy, Mertens short intervals, squarefree/nonsquarefree denominators, Jordan totients, and consecutive nonsquarefree runs found the expected separate literatures but no theorem coupling the short-interval Möbius saving to a growing CRT packet in the reciprocal-floor Jordan energy. No novelty is claimed for the separate ingredients, and no new external theorem is load-bearing, so `SOURCES.md` remains unchanged.

The failure modes are explicit. The argument requires `vartheta>0.55`; it does not cover the unresolved strip where the current all-short-interval theorem is unavailable. The budget `B+kappa<1/3` comes from the known logarithmic saving and is not claimed optimal. The host is selected adaptively in a CRT class, so nothing is asserted for arbitrary preassigned hosts. Finally, (8) is a local comparison with the selected squarefree host row, not a proof that the packet dominates the full energy `E_(T,D)`.

The durable delta is therefore precise: **known physical short-interval cancellation already lets a growing nonsquarefree packet cross to `qA_X/X -> 0`; the next obstruction is not packet existence at the deterministic threshold, but the global energy denominator and the `Theta<=0.55` localization range.**