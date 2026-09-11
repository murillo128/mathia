# ANF-175 — Prime-scale marginals pin dangerous endpoint loading to the square-root scale below the all-interval barrier

**Status:** `DERIVED + PRIME-SCALE-MARGINAL-CONTROL + SHARP-LOADING-SCALE + LONG-RANGE-INVISIBILITY + ACTIVATION-SCALE-GATE`. `ANF-174` showed that sparse unit atoms can emulate a tiny coherent drift, but its power-sized grid spacing deliberately distorted the one-point scale of the physical prime contribution. The obstruction survives after removing that mismatch. Take atoms of magnitude `asymp log X` on a grid of spacing `asymp log X`, so the occupied-site scale is prime-sized, the candidate density is prime-sized, and the local total-variation envelope is only `O(H+log X)` on an interval of length `H`. By retaining the candidate sites whose **exact** logarithmic carrier lies in one angular sector, one can still build the critical charge `asymp sqrt(X log X)` and then hold it for the rest of the endpoint.

The new point is quantitative. Under the same `O(H+log X)` marginal envelope, triangle inequality forces any packet that stores critical charge to occupy physical length at least `Omega(sqrt(X log X))`, while the carrier-sector construction attains that scale. Thus `sqrt(X log X)` is the sharp loading scale for this natural marginal class. Moreover the whole packet has total `l^1` mass only `O(sqrt(X log X))`. Consequently, on every interval in the presently available all-interval range `H >= X^(5/8+eta)`, its correlation against **every bounded test** is `o(H log^{-A} X)` for every fixed `A`, even though it creates bow-scale endpoint completion and hence a target-sized Fejer scale-slope defect.

So the current obstruction is more localized than `ANF-174` suggested. Matching prime-scale atom size and density still does not determine placement, but it pins the dangerous placement problem to the near-square-root scale. The next theorem must either reach that loading scale with source-specific exact-carrier cancellation, obtain an absolute `o(sqrt(X log X))` discrepancy while remaining above `X^(5/8+eta)`, or control the signed dyadic/Fejer defect directly. More fixed-log saving above the present activation threshold cannot see this matched control.

## 1. Prime-scale one-point marginals give a square-root lower bound for charge loading

Retain the bow regime used in `ANF-173`--`ANF-174`,

\[
K=X^{1-2\varepsilon+o(1)},
\qquad
0<\varepsilon<\frac1{16},
\qquad
A_0X^2\le U\le B_0X^2,
\tag{1}
\]

with fixed `0<A_0<B_0<infinity`. Fix a small constant `delta>0` and write

\[
a_X:=\sqrt{\delta X\log X}.
\tag{2}
\]

This is the critical stored charge because holding a prefix sum of magnitude `a_X` for `Theta(K)` steps contributes `Theta(XK log X)` to endpoint completion.

Consider a real-amplitude packet

\[
b_j=c_j(X+j)^{-iU}
\tag{3}
\]

that satisfies the following prime-scale marginal envelope on every interval `J` of coefficient indices:

\[
\sum_{j\in J}|c_j|
\le
C\bigl(|J|+\log X\bigr)
\tag{4}
\]

for some fixed `C`. This is only a matched-control hypothesis, not a theorem asserted here for the actual residual `r_X=vartheta-Q_X`. It captures the elementary one-point scale `log X` at density `1/log X`: such atoms contribute `O(1)` total variation per physical site on average, with one atom-sized boundary allowance.

If a prefix of length `L` stores critical charge,

\[
\left|\sum_{j\le L}b_j\right|\ge a_X,
\tag{5}
\]

then by (3)--(4)

\[
a_X
\le
\sum_{j\le L}|c_j|
\le
C(L+\log X).
\tag{6}
\]

Since `a_X/log X -> infinity`, this forces

\[
\boxed{L\gg_C \sqrt{X\log X}.}
\tag{7}
\]

Thus within this natural marginal class the critical endpoint charge cannot be assembled on a substantially shorter physical scale. The next section shows that this lower bound is sharp up to constants even when the exact logarithmic carrier is retained.

## 2. A prime-sized carrier-sector packet attains the lower bound

Set

\[
A_X:=\log X,
\qquad
q_X:=\lceil\log X\rceil,
\tag{8}
\]

and choose

\[
N:=\left\lceil\frac{4\sqrt3\,a_X}{A_X}\right\rceil,
\qquad
j_m:=m q_X,
\qquad
1\le m\le N.
\tag{9}
\]

The candidate sites have spacing `asymp log X`, and an active atom will have magnitude `log X`. Their physical span is

\[
L:=Nq_X
=(4\sqrt3+o(1))a_X
=\Theta(\sqrt{X\log X})
=o(K).
\tag{10}
\]

Write the exact carrier directions

\[
v_j:=(X+j)^{-iU}.
\tag{11}
\]

Partition the unit circle into six sectors of angular width `pi/3`. At least one sector contains at least `N/6` of the candidate rays `v_{j_m}`. Let `theta_X` be its center and let `S` be the candidate indices in that sector. For every `j in S`,

\[
\operatorname{Re}(e^{-i\theta_X}v_j)
\ge
\cos(\pi/6)
=\frac{\sqrt3}{2}.
\tag{12}
\]

Define

\[
c_j:=A_X1_S(j),
\qquad
b_j:=c_j(X+j)^{-iU},
\tag{13}
\]

and set all other coefficients to zero. The amplitudes are nonnegative and take only the values `0` and `log X`. The accumulated charge at the end of the packet is

\[
Q_X:=\sum_{j\le L}b_j
=A_X\sum_{j\in S}v_j,
\tag{14}
\]

so (9) and (12) give

\[
\operatorname{Re}(e^{-i\theta_X}Q_X)
\ge
\frac{\sqrt3}{2}A_X|S|
\ge
\frac{\sqrt3}{12}A_XN
\ge a_X.
\tag{15}
\]

Hence

\[
\boxed{|Q_X|\ge a_X.}
\tag{16}
\]

The same construction satisfies the marginal envelope (4). Indeed any interval `J` of length `H` contains at most `H/q_X+1` candidate sites, hence

\[
\sum_{j\in J}|c_j|
\le
A_X\left(\frac H{q_X}+1\right)
\ll H+\log X.
\tag{17}
\]

Inside the loading packet the candidate density is `asymp 1/log X`, the active density is between a fixed fraction of that and the candidate density in aggregate, and each active atom has magnitude `log X`. Thus (7) and (10) show that the scale `sqrt(X log X)` is not merely sufficient for the matched control: it is the sharp charge-loading scale permitted by these prime-sized one-point marginals.

## 3. The packet is invisible to every bounded test on the current all-interval range

The whole packet has small absolute mass. From (9) and (13),

\[
\sum_{j<K}|b_j|
=A_X|S|
\le A_XN
\ll a_X.
\tag{18}
\]

Therefore for **every** interval `I`, every length `H`, and every complex test sequence `F` satisfying `|F(j)|<=1`, one has

\[
\left|\sum_{j\in I}b_jF(j)\right|
\le
\sum_{j<K}|b_j|
\ll a_X.
\tag{19}
\]

Now fix `eta>0` and suppose

\[
H\ge X^{5/8+\eta}.
\tag{20}
\]

For every fixed `A>0`,

\[
\frac{a_X}{H(\log X)^{-A}}
\ll
X^{-1/8-\eta}(\log X)^{A+1/2}
\longrightarrow0.
\tag{21}
\]

Consequently the matched packet obeys the much stronger all-bounded-test estimate

\[
\boxed{
\sup_{|F|\le1}
\left|\sum_{j\in I}b_jF(j)\right|
=o_A\!\left(H(\log X)^{-A}\right)
}
\tag{22}
\]

uniformly for every interval in the present all-interval activation range. In particular it automatically passes any fixed-complexity polynomial-phase or nilsequence test there. This is stronger than the control in `ANF-174`: no power-sparse support is needed to manufacture long-range pseudorandomness. The entire dangerous packet simply fits below the scale at which the theorem starts, and its total mass is already too small to be detected by an `H log^{-A} X` error once `H>=X^(5/8+eta)`.

Fixed-order Gowers uniformity on the same long intervals is also harmless. Let `M:=|S|<=N`. For the standard normalized short-interval `U^s` cube average, every nonzero cube has a zero corner at an active site and each product has magnitude at most `A_X^(2^s)`. Hence, for fixed `s>=2`,

\[
\|b\|_{U^s(I)}
\ll_s
A_X\left(\frac{M}{H}\right)^{1/2^s}
\ll_s
(\log X)
\left(\frac{a_X}{A_XH}\right)^{1/2^s}.
\tag{23}
\]

Under (20) this decays by a fixed power of `X` for every fixed `s`. Thus the prime-scale packet remains compatible with the qualitative higher-uniformity conclusions used earlier on exactly the range where those conclusions are presently available.

## 4. Despite long-range invisibility, endpoint completion and the Fejer defect are target-sized

All coefficients vanish after `L`, so every prefix `r>=L` retains the same charge `Q_X`. The left endpoint completion is therefore

\[
E_-(b)
:=
\sum_{r=1}^{K-1}
\left|\sum_{j\le r}b_j\right|^2
\ge
(K-L)|Q_X|^2.
\tag{24}
\]

Using (10) and (16),

\[
\boxed{
E_-(b)
\ge
(\delta-o(1))XK\log X.
}
\tag{25}
\]

The diagonal contribution remains negligible. Since `|b_j|` is either zero or `A_X`,

\[
\Delta_-(b)
\le
K\sum_{j<K}|b_j|^2
=K A_X^2|S|
\le K A_X^2N
\ll K A_Xa_X.
\tag{26}
\]

Therefore

\[
\frac{\Delta_-(b)}{XK\log X}
\ll
\frac{a_X}{X}
\asymp
\sqrt{\frac{\log X}{X}}
\longrightarrow0.
\tag{27}
\]

The completion is genuinely off-diagonal. The dyadic endpoint ledger of `ANF-169` and the exact Fejer scale-slope identity of `ANF-172` therefore force some dyadic scale `H` with

\[
\boxed{
D_{2H}-D_H
\gg_\delta
\frac{X\log X}{\log K},
}
\tag{28}
\]

up to the fixed constants recorded there. Thus matching the natural one-point magnitude/density scale does not protect the actual downstream decision statistic.

## 5. The remaining gap is now a scale gap, not another marginal-statistics gap

`ANF-174` isolated placement as the remaining artificial freedom but used unit atoms on a grid whose spacing could be a power of `X`. The present control removes that mismatch. The dangerous packet can have atom size `log X`, candidate spacing `log X`, local total variation `O(H+log X)`, and still satisfy every bounded-test estimate of the form `H log^{-A} X` on all intervals with `H>=X^(5/8+eta)`.

At the same time, the marginal envelope proves that the packet cannot be compressed significantly below

\[
H_*\asymp\sqrt{X\log X}.
\tag{29}
\]

So the currently relevant information gap is sharply localized between the critical loading scale `H_*` and the all-interval activation scale `X^(5/8+eta)`. Their ratio is

\[
\frac{X^{5/8+\eta}}{H_*}
=
X^{1/8+\eta}(\log X)^{-1/2},
\tag{30}
\]

a genuine power gap. Merely increasing the fixed logarithmic saving above `X^(5/8+eta)` cannot close it, because the entire matched packet contributes only `O(H_*)` absolute mass there.

This identifies three quantitatively different routes that would actually address the obstruction. An all-interval exact-carrier theorem could descend to `H` of order `sqrt(X log X)` (where even a genuine logarithmic relative saving would forbid the coherent packet); a theorem that remains above `X^(5/8+eta)` could instead give an **absolute** carrier-sector/prefix discrepancy `o(sqrt(X log X))`, which is a power improvement over `H log^{-A} X`; or one can bypass prefix loading and prove directly that the signed dyadic correlation / coupled Fejer scale-slope defect of `ANF-169`--`ANF-172` is `o(X log X/log K)` for the actual prime-minus-Ramanujan source.

This does not assert that the physical residual itself obeys (4) uniformly down to `H_*`, nor that prime locations realize the carrier-sector packet. The role of the construction is adversarial: even after matching the natural prime-sized one-point marginals, placement freedom alone realizes the forbidden endpoint behavior while remaining invisible to every long-range bounded test currently activated. Any closure must therefore inject source-specific placement information at the square-root loading scale or an absolute substitute of equivalent strength.

## 6. Prior-art audit

The all-interval higher-uniformity input already used in `ANF-173` gives `H log^{-A} X` nilsequence decorrelation for the von Mangoldt residual once `H>=X^(5/8+eta)`, for arbitrary fixed complexity/order; the companion almost-all theory reaches shorter scales but does not supply the distinguished-endpoint all-interval statement needed here. The present finding does not strengthen either theorem. Instead, equations (18)--(22) give a deterministic matched control whose **total absolute mass** is already below their error scale throughout the all-interval regime.

The square-root lower bound (7), the sector construction (8)--(17), and the invisibility calculation (18)--(30) are elementary and internal. No external result beyond the already-recorded frontier inputs is load-bearing, so no new source entry is required.

## Verdict

Prime-sized one-point marginals sharpen the endpoint obstruction rather than remove it. Under the natural envelope `sum |c_j|=O(H+log X)`, critical charge `sqrt(X log X)` requires physical loading length `Omega(sqrt(X log X))`; exact carrier-sector selection with atoms of size `log X` at spacing `log X` attains that scale. The resulting packet has only `O(sqrt(X log X))` total mass, so it satisfies **every bounded-test** `H log^{-A} X` estimate on the entire currently available all-interval range, yet it produces `E_-(b)asymp XK log X` and a target-sized Fejer scale-slope defect.

The active analytic gate is therefore quantitative and scale-specific: source placement must be controlled at the near-square-root loading scale, or with an absolute discrepancy strong enough to substitute for such control. Further fixed-log improvement that remains above the `5/8` activation barrier is not the missing ingredient.