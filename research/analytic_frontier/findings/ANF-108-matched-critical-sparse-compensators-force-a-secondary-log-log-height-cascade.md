# ANF-108 — matched-critical sparse compensators force a secondary log-log height cascade

**Status:** `EXACT-DERIVED + ENDPOINT-ANTI-CONCENTRATION + CRITICAL-TAIL-SOURCE-LOCALIZATION + COMPENSATOR-CASCADE + FIXED-RAY-NARROWING`. `ANF-107` isolates an intermediate sparse-tail chamber in which a tail is already Montgomery--Taylor source-heavy but remains invisible to every fixed proper central notch, so its only possible role in a global near-extremizer is to cancel source excess through the notch-complement channel. The minimal source-visible height from `ANF-103` is especially rigid. Combining the strip-occupancy estimate of `ANF-106` with the endpoint zero of the Montgomery--Taylor spectrum gives a uniform endpoint anti-concentration inequality for every bounded-height physical configuration. A tail sitting in the matched source-critical window concentrates its source norm into a shrinking neighborhood of `|alpha|=1`; the macroscopic negative core--tail interaction forced by `ANF-104` must therefore occur in that same shrinking neighborhood. A bounded-height core cannot supply it.

More sharply, let `W_n=A_n sqcup B_n` be a fiber-complete split of a Montgomery--Taylor near-extremizer, put

\[
L_n=L(W_n),\qquad m_n=|B_n|,\qquad R_n=\frac{L_n}{m_n^2}\to\infty,
\]

and suppose the sparse tail is source-heavy,

\[
\liminf_n\frac{\|S_{B_n}\|_0^2}{L_n}\ge\lambda>0,
\]

while its maximum height `H_{B,n}` obeys the matched-critical upper bound

\[
4\pi H_{B,n}\le \log R_n+2\log\log R_n+O(1).
\]

Then, writing `H_{A,n}=max_{a in A_n}|Im a|`, one necessarily has

\[
\boxed{
\liminf_{n\to\infty}
\frac{H_{A,n}}{\log\log R_n}
\ge \frac1{4\pi}.
}
\tag{1}
\]

Thus the source-critical sparse compensator cannot sit above a uniformly bounded, or even `o(log log R)`, core. It forces a **secondary vertical cascade** inside the retained component. No horizontal gap between `A_n` and `B_n` is assumed.

## 1. Bounded strips are uniformly anti-concentrated at the Montgomery--Taylor endpoints

Retain

\[
J_0=J_{\rm MT},\qquad
E_0(X)=\int_{-1}^{1}J_0(\alpha)|S_X(\alpha)|^2\,d\alpha,
\]

and the factorization of `ANF-103/106`,

\[
J_0=g*g,
\qquad
G:=\|g\|_\infty,
\qquad
0\le J_0(\alpha)\le G^2(1-|\alpha|).
\tag{2}
\]

For `0<delta<=1/2`, define the endpoint energy

\[
E_{\rm edge,\delta}(X)
:=
\int_{1-\delta\le|\alpha|\le1}
J_0(\alpha)|S_X(\alpha)|^2\,d\alpha.
\tag{3}
\]

Assume all points of `X` satisfy `|Im z|<=H`, and set `a=2H+2`. The occupancy argument of `ANF-106`, using the strip-positive bandlimited probe there, partitions the real axis into cells of width `a` with total multiplicities `n_j` satisfying

\[
\sum_j n_j^2\le C_H E_0(X),
\qquad
C_H=\frac{100\pi^2a}{j_*},
\tag{4}
\]

where `j_*>0` is the fixed Montgomery--Taylor central lower bound from that finding.

To exploit the linear endpoint zero in (2), majorize the positive endpoint by the triangular tent

\[
T_{\delta,+}(\alpha)
:=
\delta\left(1-
\frac{|\alpha-(1-\delta)|}{\delta}
\right)_+.
\tag{5}
\]

On `1-delta<=alpha<=1`, `T_{delta,+}(alpha)=1-alpha`, so the positive-edge contribution in (3) is at most

\[
G^2\int T_{\delta,+}(\alpha)|S_X(\alpha)|^2\,d\alpha.
\]

The Fourier--Laplace transform of the tent is exact:

\[
\widehat T_{\delta,+}(z)
=
\delta^2e^{-2\pi i(1-\delta)z}
\operatorname{sinc}(\delta z)^2,
\qquad
\operatorname{sinc}(u)=\frac{\sin(\pi u)}{\pi u}.
\tag{6}
\]

For `z=x+iy`, the integral representation of `sinc` together with the elementary large-`|x|` bound gives a universal constant `C` such that

\[
|\operatorname{sinc}(\delta z)|^2
\le
C\frac{e^{2\pi\delta|y|}}
       {1+\delta^2x^2}.
\]

Because the center of the tent is `1-delta`, the two exponential factors match exactly:

\[
\boxed{
|\widehat T_{\delta,+}(x+iy)|
\le
C\,
\frac{\delta^2e^{2\pi|y|}}
     {1+\delta^2x^2}.
}
\tag{7}
\]

For a pair `z,w in X`, the relevant argument is `z-bar w`, whose imaginary part has modulus at most `2H`; hence (7) costs only `e^{4pi H}`. If the real parts lie in cells `j,k`, then for `|j-k|>=2` their horizontal distance is at least `a(|j-k|-1)`. Expanding the quadratic form into pairs, taking absolute values only after inserting (7), grouping by cell distance, and using Cauchy--Schwarz,

\[
\sum_j n_jn_{j+d}\le\sum_jn_j^2,
\]

gives

\[
\begin{aligned}
E_{+,\delta}(X)
&\le
C G^2 e^{4\pi H}
\left(\sum_jn_j^2\right)
\sum_{d\in\mathbb Z}
\frac{\delta^2}{1+c\delta^2d^2}\\
&\le
C'G^2e^{4\pi H}\delta
\sum_jn_j^2.
\end{aligned}
\]

The negative endpoint is identical. Combining with (4) yields the finite, geometry-free bound

\[
\boxed{
E_{\rm edge,\delta}(X)
\le
C_*\,(1+H)e^{4\pi H}\,\delta\,E_0(X),
\qquad 0<\delta\le\frac12,
}
\tag{8}
\]

for one universal Montgomery--Taylor constant `C_*`. Multiplicities, collisions, arbitrary horizontal span, and absence of gaps are all allowed. The dependence `e^{4pi H}` is the natural Fourier--Laplace price of probing the spectral endpoints `|alpha|=1`; the additional factor `delta` comes from the linear endpoint zero of `J_0` plus the `l^2` cell occupancy supplied by `ANF-106`.

Equation (8) is stronger than the fixed-height statement needed below. It is explicit enough to let the strip height grow with the scale.

## 2. A matched-critical sparse tail puts all of its source interaction into a shrinking endpoint layer

Return to `W_n=A_n sqcup B_n`. Near-extremality means

\[
\frac{E_0(W_n)}{L_n}\to1.
\tag{9}
\]

Because the tail is source-heavy and `R_n->infinity`, `ANF-103` supplies the matching lower bound

\[
4\pi H_{B,n}
\ge
\log R_n+2\log\log R_n+O_\lambda(1).
\tag{10}
\]

Together with the assumed upper bound, this places `B_n` in the two-sided source-critical window. The exact tail estimate of `ANF-103`,

\[
E_0(B_n)
\ll
m_n^2\frac{e^{4\pi H_{B,n}}}{H_{B,n}^2},
\]

therefore gives

\[
\boxed{
\lambda\le
\liminf\frac{E_0(B_n)}{L_n}
\le
\limsup\frac{E_0(B_n)}{L_n}
<\infty.
}
\tag{11}
\]

Consequently the triangle inequality and (9) also give

\[
E_0(A_n)=O(L_n).
\tag{12}
\]

Now choose the shrinking endpoint width

\[
\delta_n
:=
4\frac{\log\log R_n}{\log R_n}.
\tag{13}
\]

For large `n`, `0<delta_n<1/2`. On the inner band `|alpha|<=1-delta_n`, the pointwise bound

\[
|S_{B_n}(\alpha)|
\le m_ne^{2\pi|\alpha|H_{B,n}}
\]

and `int J_0=1` give

\[
\begin{aligned}
\frac1{L_n}
\int_{|\alpha|\le1-\delta_n}
J_0|S_{B_n}|^2
&\le
R_n^{-1}
 e^{4\pi(1-\delta_n)H_{B,n}}\\
&\ll
R_n^{-\delta_n}
(\log R_n)^{2(1-\delta_n)}
=o(1).
\end{aligned}
\tag{14}
\]

Indeed `R_n^{-delta_n}=(log R_n)^{-4}`. Thus a source-heavy tail at the matched critical height has asymptotically all source-relevant mass available only in the shrinking endpoint layer

\[
1-\delta_n<|\alpha|\le1.
\tag{15}
\]

For every fixed proper notch `eta<1`, this is consistent with `ANF-107`: the layer (15) eventually lies outside the fixed central band, so the tail is notch-negligible and belongs precisely to the compensator chamber rather than the direct-notch-carriage chamber.

## 3. Near-extremality forces the core to carry macroscopic endpoint source energy

Since `m_n=o(sqrt{L_n})`, one has `L(B_n)/L_n->0`. The exact source polarization of `ANF-104`, applied to the source-heavy hypothesis, yields

\[
\limsup_n
\frac{\mathcal C_0(A_n,B_n)}{L_n}
\le-\frac\lambda2,
\tag{16}
\]

where

\[
\mathcal C_0(A,B)
:=
\operatorname{Re}
\int J_0S_A\overline{S_B}.
\]

Split this cross term into the inner band of (14) and the endpoint layer (15). By (12), (14), and Cauchy--Schwarz, the inner contribution is `o(L_n)`. Hence for all sufficiently large `n`,

\[
\left|
\operatorname{Re}
\int_{1-\delta_n<|\alpha|\le1}
J_0S_{A_n}\overline{S_{B_n}}
\right|
\ge\frac\lambda3L_n.
\tag{17}
\]

The tail endpoint energy is at most its full source energy, which is `O(L_n)` by (11). Another Cauchy--Schwarz inequality therefore forces

\[
\boxed{
E_{\rm edge,\delta_n}(A_n)
\ge c_\lambda L_n
}
\tag{18}
\]

for some `c_lambda>0` depending only on the source-heavy lower bound and the bounded constant in the critical window. This is the new rigidity statement behind the cascade: a source-critical sparse compensator can cancel its excess only if the retained core itself has macroscopic Montgomery--Taylor energy in an endpoint layer whose width tends to zero like `log log R/log R`.

No horizontal remoteness is used. `ANF-104` needed a gap only for its separate geometric upper bound on the cross term; the negative-polarization conclusion (16) is gap-free.

## 4. Endpoint anti-concentration converts that forced energy into a second height scale

Apply (8) to `A_n` at height `H_{A,n}` and width `delta_n`. From (12) and (18),

\[
c_\lambda L_n
\le
C_* (1+H_{A,n})e^{4\pi H_{A,n}}
\delta_n E_0(A_n)
\le
C' (1+H_{A,n})e^{4\pi H_{A,n}}
\delta_n L_n.
\]

After cancelling `L_n`,

\[
\boxed{
(1+H_{A,n})e^{4\pi H_{A,n}}
\frac{\log\log R_n}{\log R_n}
\gg 1.
}
\tag{19}
\]

Suppose for contradiction that along a subsequence

\[
H_{A,n}
\le
\left(\frac1{4\pi}-\varepsilon\right)
\log\log R_n
\]

for some fixed `epsilon>0`. Then the left side of (19) is at most a constant times

\[
(\log\log R_n)^2
(\log R_n)^{-4\pi\varepsilon}
\longrightarrow0,
\]

contradicting (19). This proves (1).

For the calibration of `ANF-095`, where `R_n asymp n`, a tail sitting at

\[
H_{B,n}
=
\frac{\log n+2\log\log n+O(1)}{4\pi}
\]

can therefore act as a notch-invisible source compensator only if the retained core already reaches

\[
\boxed{
H_{A,n}
\ge
\left(\frac1{4\pi}-o(1)\right)
\log\log n.
}
\tag{20}
\]

The primary logarithmic height has generated a secondary log--log height requirement. This does not yet iterate automatically, because (20) is a statement about the maximum core height, not about a source-heavy sparse subcomponent of the core. It nevertheless eliminates the most natural compensator geometry: a minimally source-visible high tail cancelling against an otherwise uniformly bounded physical core.

## 5. Prior-art boundary, adversarial checks, and remaining frontier

The nearest classical themes are large-sieve inequalities for exponential sums and concentration estimates for signals. Montgomery--Vaughan's large sieve (`Mathematika` 20 (1973), 119--134, DOI `10.1112/S0025579300004708`) controls exponential sums under spacing hypotheses, while Donoho--Logan's *Signal Recovery and the Large Sieve* (`SIAM J. Appl. Math.` 52 (1992), DOI `10.1137/0152031`) studies how much norm bandlimited functions can concentrate on small sets. Neither result is load-bearing here. The frequencies in the physical configuration may collide and have no uniform separation, the points may have bounded complex height, and the needed norm is weighted by a spectrum that itself vanishes linearly at its endpoint. Equation (8) follows directly from the exact tent transform plus the `ANF-106` occupancy estimate, so no new `SOURCES.md` anchor is required and no generic large-sieve novelty is claimed.

Several limits are essential. The cascade theorem uses an **upper** matched-critical height bound for the tail. If `H_B` exceeds `log R+2 log log R` by an unbounded amount, its normalized source norm need not stay `O(1)` and the shrinking layer in (13) is no longer the correct scale; this is a genuinely different high-tail chamber, eventually including the direct notch-visibility regime of `ANF-107`. If the tail is not source-heavy, `ANF-103` already removes it. The fiber-complete split remains necessary for the affine polarization in `ANF-104`, although the endpoint anti-concentration lemma (8) itself needs no split.

The positivity of physical multiplicities is also load-bearing through `ANF-106`: arbitrary signed coefficients would not satisfy the same strip-positive occupancy control. Conversely, (8) makes no assumption on horizontal span or gaps and remains valid when the strip height grows. Finally, (1) does **not** say that the high points forced inside `A_n` carry a macroscopic amount of source energy. A single very high but source-negligible point could witness the maximum. The next decisive gate is therefore to strengthen (18)--(20) into a height-truncation statement that extracts a **source-relevant secondary high component**, which would make the cascade iterable; the competing negative route is to construct a physical near-extremizer whose tail lies above the matched source-critical window and survives all the way to the stronger fixed-notch height threshold of `ANF-107`.

This finding does not prove `beta_eta<B_eta`, improve the simple-critical-zero proportion, or establish RH. It narrows the intermediate sparse-tail obstruction from “a high tail can compensate an exposed core” to a quantitatively cascading endpoint interaction: at the minimal source-visible height, compensation forces the core itself out of every bounded vertical strip and at least onto the secondary `log log R` scale.