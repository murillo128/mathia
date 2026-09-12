# FD-062 — short-interval Möbius cancellation carries growing CRT packets below the deterministic host scale

**Status:** `EXACT-DERIVED + LITERATURE-DERIVED + SOURCE-SPECIFIC + SHORT-INTERVAL-MOBIUS + CRT-NONSQUAREFREE-PACKET + BELOW-CRITICAL-HOST + DIVERGING-LOCAL-OCCUPATION + ROUTE-REFINEMENT`.

`FD-055` and `FD-060` leave complementary pieces of the same transfer problem. `FD-055` uses genuine short-interval Möbius cancellation to move **one** nonsquarefree twin a logarithmic factor below the deterministic host scale `X/|\mathcal H(X)|`. `FD-060` uses CRT to create a **growing** nonsquarefree packet, but pays for that packet by moving the host a growing factor above the deterministic scale.

Those two costs need not be paid separately. The same short-interval saving that lets one row cross below the one-Lipschitz threshold has enough logarithmic room to carry a slowly growing CRT packet there as well.

Let

\[
A_X:=|\mathcal H(X)|,
\qquad
L_X:=\log X.
\]

Fix constants

\[
\vartheta>0.55,
\qquad
B>0,
\qquad
\kappa>0,
\qquad
B+\kappa<\frac13.
\tag{1}
\]

Suppose along an unbounded sequence that

\[
\boxed{
A_XL_X^B\ge X^\vartheta.
}
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

and every one of

\[
q+1,q+2,\ldots,q+K_X
\]

is nonsquarefree. In particular,

\[
\frac{qA_X}{X}\longrightarrow0,
\tag{4}
\]

so the packet lives on the genuinely **below-deterministic** side of the host-scale boundary.

Put

\[
T_X:=qX,
\qquad
x_d:=\left\lfloor\frac{T_X}{q+d}\right\rfloor
\quad(1\le d\le K_X).
\tag{5}
\]

The packet may be chosen so that, uniformly for all `1<=d<=K_X`,

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
\left(\frac1{\zeta(2)}-o(1)\right)
K_XA_X^2,
}
\tag{7}
\]

and if

\[
J_q(T):=w(q)\mathcal H(\lfloor T/q\rfloor)^2,
\qquad
w(r):=\frac{J_2(r)}{r^2},
\]

then

\[
\boxed{
\frac{U_{T_X,D}}{J_q(T_X)}
\ge
\left(\frac1{\zeta(2)}-o(1)\right)K_X
\longrightarrow\infty.
}
\tag{8}
\]

Thus a growing local nonsquarefree occupation packet does **not** intrinsically require the supercritical host factor `qA_X/X -> infinity` used in `FD-060`. Known arithmetic short-interval cancellation already supports `K_X -> infinity` while `qA_X/X -> 0`.

## 1. A diagonal CRT packet fits inside the logarithmic cancellation budget

For every fixed integer `K>=1`, choose distinct primes

\[
p_1,\ldots,p_K>K
\]

and put

\[
M_K:=\prod_{d=1}^Kp_d^2.
\tag{9}
\]

Choose the system once and for all so that the systems are nested as `K` grows. By the Chinese remainder theorem there is a reduced residue class `a_K mod M_K` with

\[
a_K\equiv-d\pmod{p_d^2}
\qquad(1\le d\le K).
\tag{10}
\]

Because `p_d>K>=d`, one has `gcd(a_K,M_K)=1`, while every

\[
q\equiv a_K\pmod{M_K}
\]

satisfies

\[
p_d^2\mid q+d
\qquad(1\le d\le K).
\tag{11}
\]

Hence `q+1,...,q+K` are all nonsquarefree.

Set

\[
R_X:=A_XL_X^B,
\qquad
Y_X:=\frac{X}{8R_X}.
\tag{12}
\]

The Davenport bound already used in `FD-055` gives, for every fixed `C`,

\[
\mathcal H(X)
\ll_C
\frac{X}{(\log X)^C}+X^{1/2}.
\tag{13}
\]

Therefore

\[
A_XL_X^{B+\kappa}=o(X),
\qquad
Y_X/L_X^\kappa\to\infty.
\tag{14}
\]

Choose `K_X` to be the largest integer `K` satisfying

\[
K\le L_X^\kappa,
\qquad
M_K\le Y_X^{1/4}.
\tag{15}
\]

For every fixed `K`, both conditions eventually hold because `Y_X->infinity`; hence

\[
K_X\to\infty.
\tag{16}
\]

The squarefree progression count proved directly in `FD-060` is uniform enough for this diagonal choice: if `gcd(a,M)=1`, then

\[
\#\{Y<n\le2Y:n\equiv a\pmod M,\ \mu(n)^2=1\}
=
\frac{Y}{M}C_M+O(\sqrt Y),
\tag{17}
\]

where

\[
C_M
=
\frac1{\zeta(2)}
\prod_{p\mid M}(1-p^{-2})^{-1}
\ge\frac1{\zeta(2)}.
\tag{18}
\]

With `M=M_(K_X)` and (15), the main term in (17) is at least a constant multiple of `Y_X^(3/4)`, while the error is `O(Y_X^(1/2))`. Thus for all sufficiently large `X` there is a **squarefree** integer

\[
q\equiv a_{K_X}\pmod{M_{K_X}},
\qquad
Y_X\le q\le2Y_X.
\tag{19}
\]

Equations (11)--(12) give the nonsquarefree packet, while (19) gives exactly (3).

The role of the diagonal restriction `M_(K_X)<=Y_X^(1/4)` is only to preserve an elementary squarefree-host count. No uniform squarefree theorem for rapidly growing progressions is being imported.

## 2. Every packet row remains inside one admissible short interval

For `1<=d<=K_X`, define the quotient displacement

\[
h_d:=X-x_d.
\]

Since `X` is integral,

\[
\boxed{
h_d=\left\lceil\frac{dX}{q+d}\right\rceil.}
\tag{20}
\]

Equation (14) and `K_X<=L_X^kappa` imply `K_X=o(q)` and

\[
K_XR_X=o(X).
\tag{21}
\]

Using `Y_X<=q<=2Y_X`, for all sufficiently large `X` one therefore has uniformly in the packet

\[
\boxed{
2R_X
\le h_d
\le9K_XR_X.
}
\tag{22}
\]

The lower bound follows from `q+d<=2q` and `q<=X/(4R_X)`; the upper bound follows from `q>=X/(8R_X)`.

By (2),

\[
h_d\ge2X^\vartheta,
\tag{23}
\]

while (21) gives `h_d=o(X)` and hence `x_d~X`. Thus the transferred short-interval estimate from `FD-048` applies uniformly to every interval `(x_d,X]`: for every fixed `eta>0`,

\[
|\mathcal H(X)-\mathcal H(x_d)|
\ll_{\vartheta,\eta}
\frac{h_d}{(\log X)^{1/3-\eta}}.
\tag{24}
\]

Choose `eta>0` so small that

\[
B+\kappa+\eta<\frac13.
\tag{25}
\]

Then (22)--(24) give

\[
\begin{aligned}
\max_{1\le d\le K_X}
|\mathcal H(X)-\mathcal H(x_d)|
&\ll
K_XA_XL_X^{B-1/3+\eta}\\
&\le
A_XL_X^{B+\kappa-1/3+\eta}
=o(A_X).
\end{aligned}
\tag{26}
\]

This proves the simultaneous first-order transfer (6). The logarithmic saving is being spent in two independent ways: `L_X^B` moves the host below the deterministic scale, while at most `L_X^kappa` is reserved for packet width. The only budget condition is their sum in (1).

## 3. The packet produces divergent local nonsquarefree occupation below criticality

Every row `q+d`, `1<=d<=K_X`, is nonsquarefree by (11). Since `q->infinity`, the packet eventually lies above every fixed `D`. The Jordan weights obey

\[
w(r)\ge\frac1{\zeta(2)}.
\tag{27}
\]

Therefore (6) gives

\[
\begin{aligned}
U_{T_X,D}
&\ge
\sum_{d=1}^{K_X}
w(q+d)\mathcal H(x_d)^2\\
&\ge
\left(\frac1{\zeta(2)}-o(1)\right)K_XA_X^2,
\end{aligned}
\]

which is (7).

The host itself is squarefree and samples the spike exactly:

\[
\left\lfloor\frac{T_X}{q}\right\rfloor=X,
\qquad
J_q(T_X)=w(q)A_X^2\le A_X^2.
\tag{28}
\]

Dividing (7) by (28) proves (8).

This should be compared directly with `FD-060`. There the deterministic one-Lipschitz law forces

\[
q\asymp K_X\frac{X}{A_X},
\qquad
\frac{qA_X}{X}\asymp K_X\to\infty,
\]

because the worst quotient displacement is of order `K_XX/q`. Here short-interval cancellation permits the same quantity to satisfy

\[
\frac{qA_X}{X}\asymp L_X^{-B}\to0
\]

while `K_X->infinity`. The packet therefore crosses the deterministic boundary in the strong sense that both the host and its furthest retained endpoint lie in a regime where bare bounded increments alone could lose the entire spike.

## 4. On a false-RH frontier sequence the power exponent is unchanged, but the subpower geometry is strictly stronger

Assume

\[
\Theta
:=
\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}
>0.55.
\tag{29}
\]

Choose `vartheta` with

\[
0.55<\vartheta<\Theta.
\]

`FD-046` supplies a sequence on which

\[
A_X=X^{\Theta+o(1)}.
\tag{30}
\]

For every fixed `B>0`, condition (2) then holds eventually. Equations (3) and (30) give

\[
q
=
\frac{X^{1-\Theta+o(1)}}{(\log X)^B},
\qquad
T_X
=
\frac{X^{2-\Theta+o(1)}}{(\log X)^B}.
\tag{31}
\]

Consequently

\[
\frac{\log q}{\log T_X}
\longrightarrow
\alpha_\Theta
:=
\frac{1-\Theta}{2-\Theta},
\tag{32}
\]

exactly as in `FD-055`, but now the same horizon carries **a diverging nonsquarefree packet** with total local energy `K_XA_X^2`.

On these polynomial-scale frontier sequences the CRT diagonal can be made quantitative. Using the standard prime bound `p_n\ll n\log n`, choose the `K` CRT primes with size `O(K log K)`. Then

\[
\log M_K=O(K\log K).
\tag{33}
\]

For any fixed `kappa` satisfying (1), one may therefore take

\[
\boxed{K_X=\lfloor(\log X)^\kappa\rfloor}
\tag{34}
\]

for all sufficiently large members of the sequence: (33) gives `M_(K_X)=X^{o(1)}`, whereas (31) makes `Y_X=X^{1-Theta+o(1)}` up to logarithms. Hence the host count (17) remains positive and (26) still tends to zero relative to `A_X`.

The logarithmic short-interval budget can therefore be split explicitly:

\[
B+\kappa<\frac13.
\tag{35}
\]

`B` measures how far below `X/A_X` the host is placed, while `kappa` measures how fast the packet grows. This tradeoff is invisible at the power exponent `alpha_Theta` but is genuine source-specific structure.

## 5. Global occupation remains a separate denominator problem

The new packet does not by itself prove a positive lower bound for

\[
\nu_{T,D}=\frac{U_{T,D}}{E_{T,D}}.
\]

Using only the `FD-046` envelope `E_(T,D)<<_(D,sigma) T^(2sigma)` with fixed `sigma>Theta` gives

\[
\nu_{T_X,D}
\gg_{D,\sigma}
K_XA_X^2T_X^{-2\sigma}.
\tag{36}
\]

Relative to the critical-scale construction, the smaller horizon contributes a factor of roughly `(log X)^(2sigma B)` and the packet contributes `K_X`. But the zero-frontier spike statement (30) and the passage `sigma downarrow Theta` carry uncontrolled subpower losses, so (36) does **not** by itself justify a new sharp logarithmic exponent for `nu`. At the polynomial scale it recovers the same `beta_Theta` barrier isolated in `FD-061`.

This separation matters. `FD-062` genuinely improves the **row-count/host-scale transfer geometry**: diverging packet size and below-critical placement are compatible. What remains load-bearing for global occupation is now even more clearly the denominator on those same source-selected horizons. A sharper same-horizon energy estimate could exploit the extra factors in (36); the generic zero-frontier envelope cannot certify that gain at logarithmic resolution.

## 6. Prior-art and falsification boundary

The analytic input is exactly the Matomäki--Teräväinen all-short-interval Möbius theorem already anchored in `SOURCES.md` and transferred to `mathcal H` in `FD-048`. The CRT construction of consecutive nonsquarefree integers and the squarefree progression count are the classical/elementary ingredients already isolated in `FD-060`. The standard bound `p_n<<n log n` used only for the quantitative frontier corollary is covered by the existing prime-number-theorem anchor in `SOURCES.md`.

A targeted literature search around Farey discrepancy, Mertens short intervals, squarefree/nonsquarefree denominators, Jordan totients, and consecutive nonsquarefree runs found the expected separate literatures but no theorem coupling a short-interval Möbius saving to a growing CRT packet in the reciprocal-floor Jordan energy. No novelty is claimed for any of those ingredients separately, and no new external theorem is load-bearing, so `SOURCES.md` remains unchanged.

The main failure modes are explicit. The estimate requires `vartheta>0.55`; it gives no packet in the unresolved strip where the available all-short-interval theorem does not apply. The budget `B+kappa<1/3` comes directly from the present logarithmic saving and is not claimed optimal. The host is adaptively selected in a CRT class; no statement is made for arbitrary preassigned hosts. Finally, (8) is a local comparison with the selected squarefree row, not a proof that the packet dominates the full energy `E_(T,D)`.

The durable research delta is therefore precise: **known physical short-interval cancellation already lets a growing nonsquarefree packet cross to `qA_X/X -> 0`; the next obstruction is no longer packet existence at the deterministic threshold, but the global energy denominator and the `Theta<=0.55` localization range.**