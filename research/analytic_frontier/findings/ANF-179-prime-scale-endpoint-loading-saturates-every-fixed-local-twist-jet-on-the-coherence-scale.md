# ANF-179 — Prime-scale endpoint loading saturates every fixed local twist jet on the coherence scale

**Status:** `DERIVED + MATCHED-CONTROL + LOCAL-TWIST-JET-BARRIER + FIXED-SOBOLEV-BARRIER`. `ANF-177` and `ANF-178` show that the prime-scale endpoint-loading packet from `ANF-175` is not a pointwise-in-twist pathology: after exact carrier selection it remains target-sized throughout a window of width `asymp X/a_X`, and every fixed local magnitude norm is already sharp there. A remaining generic escape is to use **twist derivatives** rather than magnitude alone. Derivatives probe the local frequency distribution, so in principle a carrier-aligned packet could be large while having an anomalous twist jet that a Sobolev- or derivative-sensitive estimate detects.

That escape also fails at fixed order. A harmless modification of the `ANF-175` control places all candidate atoms in the terminal half of its loading interval. It preserves prime-sized atoms, prime-scale spacing, the `O(H+log X)` local total-variation envelope, critical endpoint charge, long-range invisibility, and bow-scale completion. After removing the common base carrier `X^{-it}` and rescaling the twist variable by the natural coherence width, the modified packet becomes an exponential polynomial whose frequencies all lie in one fixed positive interval bounded away from both zero and infinity. The same angular-sector selection that creates endpoint charge then forces **every derivative of any fixed order** to remain comparable to the critical charge throughout a fixed rescaled twist window.

Concretely, for every fixed integer `r>=0` there is a matched control for which, with

\[
a_X:=\sqrt{\delta X\log X},
\qquad
W_X\asymp \frac{X}{a_X},
\]

and the demodulated profile

\[
G_X(t):=X^{it}P_X(t),
\]

one has simultaneously for `0<=k<=r`

\[
\boxed{
\left|W_X^k G_X^{(k)}(t)\right|\asymp_{r,\delta} a_X
}
\]

throughout a twist interval of width `asymp W_X` around the distinguished height `U`. Hence every fixed local Sobolev hierarchy built from these naturally normalized derivatives has the same critical scale as the zeroth-order magnitude statistic. Fixed-order twist smoothness, finite jets, and coefficient-generic derivative bounds therefore do not constrain the endpoint memory any more strongly than `ANF-178`'s magnitude hierarchy. A useful derivative-sensitive theorem must exploit arithmetic placement, a growing-order/nonlocal mechanism, or a source-specific differential filter rather than generic band-limited smoothness.

## 1. Move the prime-scale candidates into the terminal half of the loading interval

Work in the bow regime of `ANF-175`--`ANF-178`,

\[
K=X^{1-2\varepsilon+o(1)},
\qquad
0<\varepsilon<\frac1{16},
\qquad
A_0X^2\le U\le B_0X^2,
\tag{1}
\]

and fix `delta>0`. Put

\[
a_X:=\sqrt{\delta X\log X},
\qquad
A_X:=\log X,
\qquad
q_X:=\lceil\log X\rceil,
\tag{2}
\]

and choose

\[
N:=\left\lceil\frac{4\sqrt3\,a_X}{A_X}\right\rceil.
\tag{3}
\]

Instead of the candidate sites `m q_X` used in `ANF-175`, take

\[
j_m:=(N+m)q_X,
\qquad 1\le m\le N,
\tag{4}
\]

and define the full loading span

\[
L_X:=2Nq_X.
\tag{5}
\]

Thus every candidate lies in the terminal half

\[
\frac{L_X}{2}<j_m\le L_X.
\tag{6}
\]

As before, partition the exact carrier rays

\[
v_j:=(X+j)^{-iU}
\tag{7}
\]

into six sectors of angular width `pi/3`, retain a sector containing at least `N/6` candidates, and call its active set `S`. Let `theta_X` be the center of that sector. Define

\[
P_X(t):=A_X\sum_{j\in S}(X+j)^{-it}.
\tag{8}
\]

For every `j in S`,

\[
\operatorname{Re}(e^{-i\theta_X}v_j)\ge \cos(\pi/6)=\frac{\sqrt3}{2},
\]

so by (3)

\[
|P_X(U)|
\ge
\frac{\sqrt3}{2}A_X|S|
\ge
\frac{\sqrt3}{12}A_XN
\ge a_X.
\tag{9}
\]

Nothing essential in the prime-scale marginal control changes. Candidate spacing is still `q_Xasymp log X`; each active atom still has magnitude `log X`; every coefficient interval `J` of length `H` obeys

\[
\sum_{j\in J}|c_j|
\le
A_X\left(\frac{H}{q_X}+1\right)
\ll H+\log X;
\tag{10}
\]

and

\[
L_X=2Nq_X=\Theta_\delta(a_X)=o(K).
\tag{11}
\]

The total `l^1` mass is still `A_X|S|=O_\delta(a_X)`. Therefore the long-interval invisibility argument of `ANF-175` survives verbatim: above the current `X^(5/8+eta)` activation range, the entire packet lies below every fixed `H(log X)^(-A)` bounded-test allowance. The only new feature is (6), which prevents the rescaled local frequencies from collapsing toward zero.

## 2. Demodulation and coherence rescaling put every active frequency in one fixed positive band

The raw derivatives of `P_X(t)` contain the irrelevant common carrier frequency `log X`. Remove it by defining

\[
G_X(t):=X^{it}P_X(t)
=A_X\sum_{j\in S}\exp\!\left(-it\log\left(1+\frac jX\right)\right).
\tag{12}
\]

Set the natural twist scale

\[
W_X:=\frac{X}{L_X}
\asymp_\delta \frac{X}{a_X}
\asymp_\delta\sqrt{\frac{X}{\log X}},
\tag{13}
\]

and introduce the dimensionless local coordinate

\[
t=U+W_Xy.
\tag{14}
\]

Then

\[
F_X(y):=G_X(U+W_Xy)
=A_X\sum_{j\in S}\zeta_j e^{-iy\xi_j},
\tag{15}
\]

where

\[
\zeta_j:=\exp\!\left(-iU\log\left(1+\frac jX\right)\right),
\qquad
\xi_j:=\frac{X}{L_X}\log\left(1+\frac jX\right).
\tag{16}
\]

Multiplication by the common phase `X^{iU}` does not alter the sector geometry, so all `zeta_j` remain within angular distance `pi/6` of a common direction.

The terminal-half placement gives a uniform lower frequency bound. Since `L_X=o(X)` and `L_X/2<j<=L_X`, the elementary inequalities

\[
z-\frac{z^2}{2}\le \log(1+z)\le z
\qquad(z\ge0)
\tag{17}
\]

give, for all sufficiently large `X`,

\[
\frac12-\frac{L_X}{2X}
\le \xi_j\le1.
\tag{18}
\]

In particular,

\[
\boxed{\frac25\le\xi_j\le1}
\tag{19}
\]

uniformly over every active site. After coherence rescaling the packet is therefore genuinely band-limited in a **fixed annulus away from zero**, independently of `X`.

## 3. Every fixed derivative remains target-sized across a full coherence window

Differentiate (15). For every integer `k>=0`,

\[
F_X^{(k)}(y)
=A_X(-i)^k\sum_{j\in S}\xi_j^k\zeta_j e^{-iy\xi_j}.
\tag{20}
\]

Choose once and for all

\[
c:=\frac{\pi}{12}.
\tag{21}
\]

For `|y|<=c`, equation (19) shows that the extra rotation `y\xi_j` has magnitude at most `pi/12`. Since the original `zeta_j` lie in a sector of half-width `pi/6`, every summand in (20), after removing the common factor `(-i)^k`, lies in a sector of half-width at most

\[
\frac\pi6+\frac\pi{12}=\frac\pi4.
\tag{22}
\]

The weights `xi_j^k` are nonnegative. Projection onto the center of that sector therefore yields

\[
|F_X^{(k)}(y)|
\ge
\cos(\pi/4)A_X\sum_{j\in S}\xi_j^k
\ge
\frac1{\sqrt2}\left(\frac25\right)^k A_X|S|.
\tag{23}
\]

The opposite bound is immediate from `xi_j<=1`:

\[
|F_X^{(k)}(y)|
\le A_X|S|.
\tag{24}
\]

Since `N/6<=|S|<=N` and `A_XNasymp a_X`, equations (23)--(24) imply that for every fixed `r>=0` there are constants `0<c_{r,delta}<=C_{r,delta}<infinity` such that

\[
\boxed{
c_{r,\delta}a_X
\le
|F_X^{(k)}(y)|
\le
C_{r,\delta}a_X
}
\tag{25}
\]

simultaneously for

\[
0\le k\le r,
\qquad
|y|\le\frac\pi{12}.
\tag{26}
\]

Because `d/dy=W_X d/dt`, equation (25) is exactly

\[
\boxed{
\left|W_X^kG_X^{(k)}(t)\right|
\asymp_{r,\delta}a_X
}
\tag{27}
\]

for every `0<=k<=r` throughout

\[
|t-U|\le \frac\pi{12}W_X.
\tag{28}
\]

So the packet does not merely remain large under a twist perturbation. Its complete **fixed-order dimensionless jet** remains large at the same natural scale throughout a full `Theta(W_X)` coherence interval.

## 4. Fixed Sobolev and derivative-moment refinements inherit the ANF-178 barrier

Let `p>0`, `r>=0`, and `0<=k<=r` be fixed. Integrating (25) over the fixed `y` interval gives

\[
\int_{-\pi/12}^{\pi/12}|F_X^{(k)}(y)|^pdy
\asymp_{p,r,\delta}a_X^p.
\tag{29}
\]

Returning to `t`,

\[
\boxed{
\int_{U-cW_X}^{U+cW_X}
\left|W_X^kG_X^{(k)}(t)\right|^pdt
\asymp_{p,r,\delta}
W_Xa_X^p
\asymp_{p,r,\delta}
Xa_X^{p-1}.
}
\tag{30}
\]

Thus any fixed Sobolev-type magnitude statistic obtained by summing finitely many terms in (30) has exactly the same scale as the zeroth-order local moment in `ANF-178`. The derivatives do not create a new generic small parameter. This is the natural behavior of a bounded-band exponential polynomial: after scaling by its coherence length, differentiation costs only a constant per fixed order. The new point here is that the same packet simultaneously carries the critical endpoint memory and gives a matching lower bound for every member of the finite jet.

The modified packet also preserves the downstream obstruction. All coefficients vanish after `L_X`, so every later prefix retains the charge from (9), and

\[
E_-(b)
\ge
(K-L_X)|P_X(U)|^2
\ge
(\delta-o(1))XK\log X.
\tag{31}
\]

Its diagonal contribution is still lower order because

\[
K\sum_{j\in S}A_X^2
\ll
K a_X\log X
=o(XK\log X).
\tag{32}
\]

Hence `ANF-169` again forces a positive real dyadic shifted-correlation block, and `ANF-172` identifies that block with a target-sized Fejer scale-slope defect. The fixed-jet regularity in (27)--(30) therefore coexists with exactly the endpoint statistic the bow argument must eliminate.

## 5. Stress tests and evidence boundary

The demodulation in (12) is essential. Differentiating the raw `P_X(t)` mostly measures the common frequency `log X`, which is a coordinate artifact and supplies no additional information. Equation (27) instead measures derivatives after removing that carrier and normalizing by the actual coherence width, so it tests the strongest coefficient-generic finite-jet refinement that this packet naturally presents.

The conclusion is deliberately **fixed-order**. The lower constant in (23) deteriorates like `(2/5)^k`, so nothing here controls a derivative order `r=r(X)` tending to infinity. A growing-order jet, analytic-continuation argument, or genuinely nonlocal twist observable may therefore carry more information. Likewise, an arbitrary signed differential filter can have a symbol that vanishes or oscillates on the band `[2/5,1]`; the argument does not rule out a specially designed source-faithful filter of that kind.

Most importantly, the active sites are still selected after inspecting the distinguished carrier phase. The construction is a matched control, not a model for the actual residual `r_X=vartheta-Q_R`. It proves that prime-sized marginals, long-interval pseudorandomness, local twist magnitude statistics, and now every fixed naturally normalized twist jet remain insufficient **without arithmetic information about placement**. It does not prove that the physical prime/rough residual realizes the packet.

## 6. Prior-art boundary and research consequence

Classical Bernstein/Paley--Wiener theory already relates spectral width to derivative bounds for entire functions of exponential type, and Turan--Nazarov-type theory studies observability of exponential polynomials from sets or intervals. No novelty is claimed for those general harmonic-analysis principles. They are not load-bearing here: equations (17)--(30) are an elementary direct calculation for the explicit matched packet. The Mathia-specific content is the simultaneous compatibility of prime-scale endpoint loading, bow-scale completion, and saturation of the complete fixed local twist jet after the natural carrier/coherence normalization. No new external source dependency is therefore required for this finding.

The analytic frontier narrows accordingly. Replacing local `L^2` by higher fixed moments was already blocked by `ANF-178`; replacing magnitude-only statistics by finitely many generic twist derivatives does not help either. A viable local-twist theorem must use arithmetic placement to obtain a strict saving below this packet, use an operator whose symbol encodes source structure rather than only band-limited smoothness, or introduce complexity that grows with `X`. The alternative remains the direct route: control the signed dyadic correlation / Fejer scale-slope defect consumed by `ANF-169`--`ANF-172`.

## Falsification criterion

This finding is falsified if the terminal-half packet above fails any of the claimed prime-scale marginal, charge, or completion estimates, or if after the base-carrier demodulation and coherence rescaling one can find a fixed derivative order `k` for which (25) fails uniformly on the stated fixed `y` interval. It is also overclaimed if its fixed-jet conclusion is read as excluding growing-order, nonlocal, or source-specific differential observables; those remain explicit escape routes.