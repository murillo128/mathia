# FD-055 — short-interval Möbius cancellation penetrates the additive-transfer boundary logarithmically

**Status:** `EXACT-DERIVED + LITERATURE-DERIVED + SOURCE-SPECIFIC + SHORT-INTERVAL-MOBIUS + ADAPTIVE-NONSQUAREFREE-TWIN + LOGARITHMIC-THRESHOLD-PENETRATION + ZERO-FRONTIER-ENDPOINT + JOINT-NONSQUAREFREE-OCCUPATION`.

`FD-054` proves a local quadratic transfer from a squarefree Jordan host to a bounded-distance nonsquarefree row whenever the shell spike is large enough compared with the quotient displacement. With

\[
A=|\mathcal H(X)|,
\qquad
T=qX,
\]

its one-Lipschitz argument requires

\[
\frac{qA}{X}\longrightarrow\infty,
\]

so the host must lie asymptotically above the natural scale `q ~ X/A`. On zero-frontier spikes this gives the strict row-exponent threshold

\[
\alpha>\alpha_\Theta
:=\frac{1-\Theta}{2-\Theta}.
\]

The physical source has stronger local regularity than one-Lipschitz. `FD-048` transfers the Matomäki--Teräväinen all-short-interval estimate for Möbius to the exact shell source. Keeping that logarithmic cancellation instead of discarding it shows that the local transfer survives when the squarefree host is a logarithmic factor **below** `X/A`.

Fix

\[
\vartheta>0.55,
\qquad
0<B<\frac13.
\]

For every sufficiently large integer `X`, put

\[
A_X:=|\mathcal H(X)|,
\qquad
L_X:=\log X.
\]

Suppose

\[
\boxed{
A_XL_X^B\ge X^\vartheta.
}
\tag{1}
\]

Then there is a squarefree host `q_X` with

\[
\boxed{
q_X\asymp \frac{X}{A_XL_X^B},
\qquad
\frac{q_XA_X}{X}\asymp L_X^{-B}\longrightarrow0,
}
\tag{2}
\]

such that, at the physical horizon

\[
T_X:=q_XX,
\]

the nearest row

\[
q_X^*:=4\left\lceil\frac{q_X}{4}\right\rceil
\]

is nonsquarefree and satisfies

\[
\boxed{
\mathcal H\!\left(\left\lfloor\frac{T_X}{q_X^*}\right\rfloor\right)
=
\mathcal H(X)+o(A_X).
}
\tag{3}
\]

Consequently, for every fixed Schur-head dimension `D`, along any unbounded sequence satisfying (1),

\[
\boxed{
U_{T_X,D}
\ge
\left(\frac1{\zeta(2)}-o(1)\right)A_X^2
\ge
\left(\frac1{\zeta(2)}-o(1)\right)J_{q_X}(T_X),
}
\tag{4}
\]

where

\[
J_q(T):=w(q)\mathcal H(\lfloor T/q\rfloor)^2,
\qquad
w(q)=\frac{J_2(q)}{q^2}.
\]

Thus the sufficient condition in `FD-054` is not the physical transfer threshold. It is the threshold of the bare one-Lipschitz argument. The exact Möbius source penetrates it by every fixed factor `(log X)^B` with `B<1/3` on spikes large enough to enter the presently known all-short-interval range.

If

\[
\Theta
:=
\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}
>0.55,
\]

then `FD-046` supplies a sequence with shell power exponent tending to `Theta`. Applying the construction on that sequence gives

\[
\boxed{
\frac{\log q_X}{\log X}\longrightarrow1-\Theta,
\qquad
\frac{\log q_X}{\log T_X}
\longrightarrow
\alpha_\Theta
=
\frac{1-\Theta}{2-\Theta}.
}
\tag{5}
\]

Hence, whenever the zero frontier lies beyond the current short-interval exponent `0.55`, the strict power-scale inequality in `FD-054` can be closed at its endpoint: frontier-scale squarefree hosts at `alpha_Theta` still acquire a comparable nonsquarefree quadratic twin, even though their adaptive placement obeys `q_XA_X/X -> 0`.

## 1. The physical shell source has enough global room to choose the adaptive host

The source is

\[
\mathcal H(X)
=
\sum_{d\le X}\frac{\mathbf M(\lfloor X/d\rfloor)}d,
\]

and `FD-048` records the exact coefficient convolution behind it. Davenport's classical bound

\[
\mathbf M(y)\ll_K \frac{y}{(\log y)^K}
\]

for every fixed `K` also implies, by splitting the floor transform at `d=\sqrt X`, that for every fixed `K`

\[
\boxed{
\mathcal H(X)
\ll_K
\frac{X}{(\log X)^K}+X^{1/2}.
}
\tag{6}
\]

Indeed, for `d<=sqrt(X)` the Mertens estimate gives the first term after summing `X/d^2`, while for `d>sqrt(X)` the trivial bound `|M(y)|<=y` contributes `O(sqrt(X))`. In particular, for every fixed `B`,

\[
A_XL_X^B=o(X).
\tag{7}
\]

Set

\[
R_X:=A_XL_X^B,
\qquad
y_X:=\frac{X}{8R_X}.
\tag{8}
\]

Under (1), `R_X->infinity`; by (7), `y_X->infinity`. The classical positive density of squarefree integers, with the quantitative form already anchored through Walfisz in `SOURCES.md`, implies

\[
Q(2y)-Q(y)=\frac{y}{\zeta(2)}+o(y)>0.
\]

Hence for all sufficiently large `X` there is a squarefree integer `q_X` satisfying

\[
y_X\le q_X\le2y_X.
\tag{9}
\]

Equations (8)--(9) immediately give (2), including the important fact that

\[
\frac{q_XA_X}{X}\asymp \frac1{L_X^B}\to0.
\tag{10}
\]

So this host lies on the opposite side of the one-Lipschitz criterion used in `FD-054`.

## 2. The nearest multiple of four samples only a short interval away

Because `q_X` is squarefree, it is not divisible by four. Write

\[
q_X^*=q_X+\Delta_X,
\qquad
\Delta_X\in\{1,2,3\}.
\tag{11}
\]

Put

\[
X_X^*:=\left\lfloor\frac{q_XX}{q_X^*}\right\rfloor,
\qquad
h_X:=X-X_X^*.
\tag{12}
\]

The floor gives the two-sided deterministic estimate

\[
\frac{\Delta_XX}{q_X^*}
\le h_X
\le
\frac{\Delta_XX}{q_X^*}+1.
\tag{13}
\]

Using `Delta_X>=1`, `Delta_X<=3`, and (9), for all sufficiently large `X`,

\[
\boxed{
2R_X\le h_X\le25R_X.
}
\tag{14}
\]

The constants are deliberately inessential; what matters is the exact scale

\[
h_X\asymp A_X(\log X)^B.
\tag{15}
\]

Equation (7) implies `h_X=o(X)`, so `X_X^*~X`. Condition (1) and (14) also imply

\[
h_X\ge (X_X^*)^\vartheta
\tag{16}
\]

for all sufficiently large `X`. Thus the additive twin is now separated from the host by a quotient interval that is too long for the one-Lipschitz estimate to preserve a spike of height `A_X`, but is still inside the all-short-interval Möbius cancellation regime.

## 3. Matomäki--Teräväinen cancellation recovers the spike across that interval

Choose `eta>0` so that

\[
B<\frac13-\eta.
\tag{17}
\]

`FD-048`, using Matomäki--Teräväinen, proves the physical shell estimate

\[
\boxed{
|\mathcal H(x+h)-\mathcal H(x)|
\ll_{\vartheta,\eta}
\frac{h}{(\log x)^{1/3-\eta}}
}
\tag{18}
\]

uniformly for `x^vartheta<=h<=x`. Apply (18) with

\[
x=X_X^*,
\qquad
h=h_X.
\]

Equations (7), (14), and (16) verify its range. Since `X_X^*~X`,

\[
\begin{aligned}
|\mathcal H(X)-\mathcal H(X_X^*)|
&\ll
\frac{A_XL_X^B}{L_X^{1/3-\eta}}\\
&=
A_XL_X^{B-1/3+\eta}
=o(A_X).
\end{aligned}
\tag{19}
\]

This proves (3). The point is not merely a better constant: the interval has length `A_X(log X)^B`, which is larger than the spike height by a diverging logarithmic factor. Bare bounded-increment control would permit complete cancellation across such an interval; the arithmetic short-interval theorem forbids it for the physical source.

The row `q_X^*` is divisible by four, hence nonsquarefree. Since `q_X->infinity`, it eventually lies above every fixed `D`, and clearly `q_X^*<=T_X`. Therefore it is one positive summand in `U_(T_X,D)`. The uniform Jordan bound

\[
w(r)\ge\frac1{\zeta(2)}
\]

and (3) give the first inequality in (4). The original squarefree host contributes

\[
J_{q_X}(T_X)=w(q_X)A_X^2\le A_X^2,
\]

which gives the second.

## 4. The zero frontier reaches the endpoint when `Theta>0.55`

Assume `Theta>0.55`. Choose once and for all

\[
0.55<\vartheta<\Theta.
\tag{20}
\]

`FD-046` proves

\[
\limsup_{X\to\infty}
\frac{\log(1+|\mathcal H(X)|)}{\log X}
=\Theta.
\tag{21}
\]

Hence there is a sequence `X_j->infinity` on which, writing `A_j=|\mathcal H(X_j)|`,

\[
\lambda_j:=\frac{\log A_j}{\log X_j}\longrightarrow\Theta.
\tag{22}
\]

In particular `A_jL_j^B>=X_j^vartheta` eventually, so the preceding construction applies. From (2),

\[
\frac{\log q_j}{\log X_j}
=
1-\lambda_j
-B\frac{\log\log X_j}{\log X_j}
+o(1)
\longrightarrow1-\Theta.
\tag{23}
\]

With `T_j=q_jX_j`,

\[
\frac{\log T_j}{\log X_j}
\longrightarrow2-\Theta,
\tag{24}
\]

and division of (23) by (24) proves (5).

This is the exact power-scale endpoint left open by `FD-054` in the range `Theta>0.55`. The improvement is stronger than simply taking its strict exponent `c>1-Theta` closer to the boundary: on the adaptive hosts above,

\[
q_j\asymp
\frac{X_j}{A_j(\log X_j)^B},
\]

whereas the one-Lipschitz transfer would require `q_j A_j/X_j -> infinity`. Here the same quantity tends to zero as `(log X_j)^(-B)`.

## 5. What this does and does not close

The result advances the live low-row program in the `mind`, but it does not resolve `CLUE-joint-nonsquarefree-jordan-energy-occupation`. Equation (4) transports one frontier-scale squarefree row into a comparable nonsquarefree row. Other low rows can still make the total denominator `E_(T,D)` much larger, so no fixed positive lower bound for `U/E` follows.

Nor does the argument penetrate below `alpha_Theta` by a positive power. Its gain over the adaptive threshold is logarithmic, with exponent limited by the current `1/3-eta` saving in (18). The condition `vartheta>0.55` is also load-bearing. If false RH were realized only with

\[
\frac12<\Theta\le0.55,
\]

the presently available all-short-interval theorem does not reach the frontier-sized quotient displacement, and `FD-054` remains the relevant unconditional transfer result.

The useful frontier is therefore sharper. For `Theta>0.55`, a putative quadratic occupation escape cannot rely on isolating frontier-sized shell spikes on squarefree rows at the boundary `alpha_Theta`, even after moving those hosts a fixed logarithmic factor below the deterministic Lipschitz threshold. Any surviving mechanism must either make unrelated low-row energy overwhelm the transported pair, live at genuinely smaller power-scale rows, or exploit the unresolved `Theta<=0.55` short-interval range.

## 6. Prior art and falsification boundary

The external analytic inputs are exactly the Matomäki--Teräväinen short-interval Möbius estimate and the squarefree counting law already anchored in `SOURCES.md`; Davenport's Mertens bound is anchored there as well. No novelty is claimed for those theorems or for the elementary multiple-of-four pairing from `FD-037` and `FD-054`.

A targeted prior-art search around short-interval Möbius cancellation, squarefree or `k`-free Farey denominators, and RH-sensitive Farey discrepancy found the expected Matomäki--Teräväinen theorem and the neighboring work of Banks and of Chahal--Chatterjee--Chaubey on Farey fractions with squarefree/`k`-free denominators. Those works concern restricted Farey subsequences, discrepancy/equidistribution, and correlation statistics; no matching result was found for the present adaptive Jordan-row energy transfer or its logarithmic crossing of the `q~X/|mathcal H(X)|` boundary. No new theorem is load-bearing, so `SOURCES.md` needs no update.

The main falsification checks are explicit. The adaptive squarefree interval must tend to infinity; (6)--(8) guarantee this. The quotient displacement must satisfy both sides of the short-interval range; (14), (1), and `R_X=o(X)` do so. The logarithmic exponent must obey `B<1/3-eta`; otherwise (19) need not be `o(A_X)`. Finally, the zero-frontier endpoint conclusion uses `Theta>0.55`; it must not be cited for the unresolved strip `1/2<Theta<=0.55`, as proving a positive pointwise occupation fraction, or as excluding denominator domination by other low Jordan rows.