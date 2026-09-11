# ANF-171 — phase-orthogonal moving-window packets saturate the square-function danger scale

**Status:** `EXACT-DERIVED + TARGET-SCALE-STRESS-CONTROL + PHASE-OBSTRUCTION + CAUCHY-SATURATION + NEGATIVE-ROUTE-RESULT`. `ANF-170` correctly proves that a dangerous signed dyadic endpoint shell forces a large positive moving-window square function `Q_H`, and therefore that sufficiently small `Q_H` is enough to rule out endpoint completion. The remaining question is whether this positive quantity is close enough to the actual endpoint obstruction to deserve priority as the next source theorem.

There is an exact target-scale stress control showing that it is not. A constant-modulus geometric endpoint packet can make `A Q_H` live exactly at the `ANF-170` danger scale and can asymptotically saturate Cauchy--Schwarz in **modulus**, while the signed quantity `Re S_H` is smaller by a vanishing factor because the moving window sits at a quarter-turn phase relative to the current coefficient. For the same packet the full endpoint prefix energy is `o(X K log X)` throughout the difficult bow regime `0<epsilon<1/4`. Thus the loss from `S_H` to `Q_H` is not merely a harmless constant or an edge effect: at the exact scale forced by `ANF-170`, the missing datum is angular alignment.

## 1. A geometric packet can put the full moving window at a quarter turn

Fix an endpoint sequence and retain the notation of `ANF-170`,

\[
B_H(m)=\sum_{\substack{H\le h<2H\\h<m}}b_{m-h},
\qquad
S_H=\sum_{m=H+1}^{K-1}w_m b_m\overline{B_H(m)},
\qquad
w_m=1-\frac mK,
\tag{1}
\]

with

\[
A=\sum_{m<K}w_m|b_m|^2,
\qquad
Q_H=\sum_{m=H+1}^{K-1}w_m|B_H(m)|^2.
\tag{2}
\]

Assume `2H<K` and define a constant-modulus geometric packet

\[
\boxed{
 b_j=a e^{ij\theta},
 \qquad
 \theta:=\frac{\pi}{3H-1},
 \qquad 1\le j<K,
}
\tag{3}
\]

where `a>0`. For every interior site `m>=2H`, the moving window is complete and therefore

\[
B_H(m)
=b_m D_H,
\qquad
D_H:=\sum_{h=H}^{2H-1}e^{-ih\theta}.
\tag{4}
\]

The finite geometric-sum identity gives

\[
D_H
=
\exp\!\left(-\frac{i(3H-1)\theta}{2}\right)
\frac{\sin(H\theta/2)}{\sin(\theta/2)}.
\tag{5}
\]

Our choice of `theta` makes the phase in (5) exactly `-pi/2`. Hence

\[
\boxed{
D_H=-i d_H,
\qquad
d_H:=
\frac{\sin\!\left(\frac{\pi H}{2(3H-1)}\right)}
     {\sin\!\left(\frac{\pi}{2(3H-1)}\right)}
=\left(\frac3\pi+o(1)\right)H.
}
\tag{6}
\]

Consequently, for every `m>=2H`,

\[
b_m\overline{B_H(m)}
=i a^2 d_H,
\tag{7}
\]

which is **purely imaginary**. The entire interior moving-window contribution therefore carries large modulus but contributes exactly zero to `Re S_H`.

Only the truncated boundary sites `H<m<2H` can contribute to the real part. There are `O(H)` such sites and each truncated window has modulus at most `aH`, so

\[
\boxed{
|\operatorname{Re}S_H|\ll a^2H^2.
}
\tag{8}
\]

This is the basic phase-orthogonality mechanism.

## 2. Cauchy is asymptotically saturated in modulus despite the lost real part

The packet has an exact weighted mass

\[
A
=a^2\sum_{m=1}^{K-1}\left(1-\frac mK\right)
=\frac{a^2(K-1)}2
\sim\frac{a^2K}{2}.
\tag{9}
\]

If `H=o(K)`, the interior weight satisfies

\[
\sum_{m=2H}^{K-1}w_m
=\frac K2+o(K).
\tag{10}
\]

Using (6), the positive square function is therefore

\[
Q_H
=
\left(\frac{9}{2\pi^2}+o(1)\right)a^2KH^2,
\tag{11}
\]

because the truncated boundary contributes only `O(a^2H^3)=o(a^2KH^2)`. Likewise (7) gives

\[
S_H
=
i\left(\frac{3}{2\pi}+o(1)\right)a^2KH
+O(a^2H^2).
\tag{12}
\]

Equations (9)--(12) imply

\[
\boxed{
\frac{|S_H|^2}{A Q_H}\longrightarrow1,
\qquad
\frac{\operatorname{Re}S_H}{\sqrt{A Q_H}}\longrightarrow0.
}
\tag{13}
\]

Thus the Cauchy bridge of `ANF-170`,

\[
|S_H|^2\le A Q_H,
\tag{14}
\]

can be essentially an equality while being useless for the quantity that actually enters the endpoint ledger, namely `Re S_H`. The loss is entirely angular: the large moving-window vector is almost perfectly aligned with the current coefficient after a quarter-turn, rather than with positive real alignment.

It is useful to name this distinction explicitly. Define the real alignment coefficient

\[
\alpha_H
:=
\frac{\operatorname{Re}S_H}{\sqrt{A Q_H}}
\qquad
(AQ_H>0).
\tag{15}
\]

Then `|alpha_H|<=1`, and endpoint danger on a dyadic shell is controlled by the product

\[
\operatorname{Re}S_H
=\alpha_H\sqrt{A Q_H}.
\tag{16}
\]

`ANF-170` retains the energy factor `sqrt(A Q_H)` but discards `alpha_H`. The packet (3) has maximal complex coherence and `alpha_H=o(1)`.

## 3. The phase loss occurs exactly at the ANF-170 forced scale

Now specialize to the bow regime

\[
K=X^{1-2\varepsilon+o(1)},
\qquad
0<\varepsilon<\frac14,
\tag{17}
\]

and put

\[
L:=\log_2(2K).
\tag{18}
\]

Choose the constant modulus at the natural logarithmic RMS normalization

\[
a^2:=\log X,
\tag{19}
\]

and choose a dyadic `H` satisfying

\[
\boxed{
H\asymp\frac{X}{KL}.
}
\tag{20}
\]

Such a dyadic scale exists for all sufficiently large `X`: indeed

\[
\frac{X}{KL}
=X^{2\varepsilon+o(1)}(\log X)^{-1}\to\infty,
\tag{21}
\]

while

\[
\frac{H}{K}
\asymp
\frac{X}{K^2L}
=X^{-1+4\varepsilon+o(1)}(\log X)^{-1}	o0.
\tag{22}
\]

Thus the assumptions `H->infinity` and `2H<K` used above hold throughout the difficult range.

At this scale, (9) and (11) give

\[
A\asymp K\log X,
\qquad
Q_H\asymp
\frac{X^2\log X}{K L^2},
\tag{23}
\]

and hence

\[
\boxed{
A Q_H
\asymp
\frac{X^2\log^2X}{L^2}.
}
\tag{24}
\]

This is exactly the self-normalized danger scale in `ANF-170`: a macroscopic completion there forces, up to the fixed `delta` constant,

\[
A Q_H
\gg_\delta
\frac{X^2\log^2X}{L^2}.
\tag{25}
\]

The modulus of the signed shell also sits at the `ANF-169` witness scale,

\[
|S_H|
\asymp
\frac{X\log X}{L}.
\tag{26}
\]

Nevertheless (8) and (20) give

\[
\frac{|\operatorname{Re}S_H|}{X\log X/L}
\ll
\frac{X}{K^2L}
=X^{-1+4\varepsilon+o(1)}(\log X)^{-1}
\longrightarrow0.
\tag{27}
\]

So the packet pays the full positive square-function bill and even produces a shell of the correct **complex magnitude**, yet it fails the positive-real shell condition required by `ANF-169` by a vanishing factor.

## 4. The same packet has negligible endpoint completion

The endpoint prefix sum is explicit:

\[
P_r
:=
\sum_{j=1}^r b_j
=
a e^{i(r+1)\theta/2}
\frac{\sin(r\theta/2)}{\sin(\theta/2)}.
\tag{28}
\]

Therefore

\[
|P_r|
\le
\frac{a}{\sin(\theta/2)}
\ll aH,
\tag{29}
\]

uniformly in `r<K`. The full one-endpoint completion obeys

\[
E
:=
\sum_{r=1}^{K-1}|P_r|^2
\ll
K a^2H^2.
\tag{30}
\]

With (19)--(20),

\[
E
\ll
\frac{X^2\log X}{K L^2},
\tag{31}
\]

and relative to the bow target `T_bow=XK log X`,

\[
\boxed{
\frac{E}{XK\log X}
\ll
\frac{X}{K^2L^2}
=X^{-1+4\varepsilon+o(1)}(\log X)^{-2}
\longrightarrow0.
}
\tag{32}
\]

Thus this is not merely a local shell whose imaginary phase would somehow reappear as large prefix energy elsewhere. The **entire endpoint completion is negligible at bow scale** even though `A Q_H` and `|S_H|` both sit at their respective danger scales.

The example is a deterministic stress control, not an arithmetic counterexample. Its coefficients are chosen directly after twisting; it does not assert that the actual residual `r_X(n)=vartheta(n)-Q_R(n)` realizes this phase pattern. Its role is narrower and exact: it tests how much information the positive representation in `ANF-170` retains before source arithmetic is used.

## 5. Consequence for the source-side theorem target

`ANF-170` remains fully correct. Uniformly proving

\[
A_\sigma Q_H^\sigma
=o\!\left(\frac{X^2\log^2X}{\log^2(2K)}\right)
\tag{33}
\]

for the actual prime-minus-Ramanujan residual would still close the endpoint witness. What `ANF-171` shows is that (33) is **strictly stronger than the phase-sensitive information needed at the exact target scale**. Small endpoint completion does not force the positive square function below that scale, even for a constant-modulus packet for which the Cauchy inequality is asymptotically sharp in magnitude.

The live gate therefore naturally splits into two source-specific possibilities. One may still prove that the actual arithmetic residual has genuinely subcritical `Q_H`; that would be sufficient and would bypass alignment. But if the real source naturally has `Q_H` at or above the scale (25), the missing theorem must retain the sign/phase information encoded by `alpha_H`, equivalently control `Re S_H` rather than only the positive moving-window energy. In particular, a Selberg-integral or large-sieve estimate that loses the angle between `b_m` and `B_H(m)` may be paying a theorem-strength cost that the endpoint problem itself does not require.

This sharpens the qualitative caveat already noted in `ANF-170`: large `Q_H` need not imply large positive `S_H`. The new point is that the caveat persists **at exactly the forced bow scale**, with asymptotic Cauchy saturation and negligible total completion. The next arithmetic audit should therefore compare the cost of proving subcritical `Q_H` against the cost of proving a directly phase-sensitive dyadic estimate for

\[
\operatorname{Re}
\sum_m
w_m r_X(n_m)n_m^{-iU}
\overline{
\sum_{h\sim H}r_X(n_{m-h})n_{m-h}^{-iU}
}.
\tag{34}
\]

A bounded prior-art audit found only the standard finite-geometric-sum/Dirichlet-kernel identity behind (5), together with generic Fourier/autocorrelation interpretations. No external theorem is load-bearing for the target-scale construction, and no source located in the audit supplies the endpoint-weighted phase obstruction (24)--(32) in this bow setting. `SOURCES.md` therefore requires no new anchor.

The structural conclusion is negative but useful: the positive square function from `ANF-170` is a valid sufficient interface, not a scale-sharp surrogate for endpoint danger. **Endpoint danger is a two-factor event: enough moving-window energy and enough positive-real alignment.** Any source theorem may kill either factor, and the arithmetic strategy should preserve that freedom rather than treating energy alone as the only remaining gate.
