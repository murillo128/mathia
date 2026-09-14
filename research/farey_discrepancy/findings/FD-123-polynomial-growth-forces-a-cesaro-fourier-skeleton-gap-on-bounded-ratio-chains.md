# FD-123 — polynomial growth forces a Cesàro Fourier-skeleton gap on bounded-ratio chains

**Status:** `EXACT-DERIVED + FLOOR-QUOTIENT-FOURIER-SKELETON + BOUNDED-RATIO-MULTIHORIZON + POLYNOMIAL-SOURCE-GROWTH + CESARO-SATURATION-GAP + ROUTE-NARROWING`.

`FD-121`--`FD-122` show that one common source cannot simultaneously track the separate Fourier-skeleton equality rays at two horizons joined by a fixed squarefree dilation. Their remaining escape is explicit: nonsquarefree dilation ratios are not covered by the repeated-prime collision used there, and even the squarefree pair gaps do not say which endpoint pays the cost.

For bounded integer-ratio chains, a very weak source hypothesis closes that escape **in Cesàro mean**. The key observation is that a later nonsquarefree transition remembers every earlier endpoint through one exact floor-quotient coordinate. The `FD-122` coordinate-stability inequality then turns high saturation at that later horizon into multiplicative growth of the source endpoint. A polynomial envelope permits such high-saturation nonsquarefree stages only below a fixed density, while squarefree stages already pay the `FD-122` pairwise gap. Combining the two alternatives yields a schedule-independent positive average deficit.

Let

\[
\mathcal Q_H
:=
\left\{\left\lfloor\frac Hm\right\rfloor:1\le m\le H\right\},
\qquad
A_H(k)
:=
\sum_{d\mid k}d\,Y\!\left(\left\lfloor\frac Hd\right\rfloor\right),
\tag{1}
\]

and retain the `FD-118`--`FD-122` skeleton energy

\[
\mathcal E_H^{\mathcal Q}(Y)
:=
\sum_{k\in\mathcal Q_H}\frac{|A_H(k)|^2}{k^2},
\qquad
\Delta_H(Y)
:=
\mathcal E_H^{\mathcal Q}(Y)-|Y(H)|^2
\ge0.
\tag{2}
\]

Define the normalized saturation ratio

\[
S_H(Y)
:=
\begin{cases}
\dfrac{|Y(H)|^2}{\mathcal E_H^{\mathcal Q}(Y)},&
\mathcal E_H^{\mathcal Q}(Y)>0,\\[1.2ex]
0,&\mathcal E_H^{\mathcal Q}(Y)=0.
\end{cases}
\tag{3}
\]

Thus `0<=S_H<=1`; when `Y(H) ne 0`,

\[
\frac{\Delta_H(Y)}{|Y(H)|^2}
=
\frac1{S_H(Y)}-1.
\tag{4}
\]

Consider any integer-ratio chain

\[
H_j=q_jH_{j-1},
\qquad
2\le q_j\le Q<\infty,
\tag{5}
\]

and suppose that for some fixed `C<infinity` and `alpha>=0`,

\[
|Y(n)|\le Cn^\alpha
\qquad(n\ge1).
\tag{6}
\]

Then there is an explicit constant

\[
\Gamma_{\alpha,Q}>0
\tag{7}
\]

depending only on `alpha` and `Q` such that

\[
\boxed{
\liminf_{n\to\infty}
\frac1{n+1}
\sum_{j=0}^{n}
\bigl(1-S_{H_j}(Y)\bigr)
\ge
\Gamma_{\alpha,Q}>0.
}
\tag{8}
\]

Equivalently,

\[
\boxed{
\limsup_{n\to\infty}
\frac1{n+1}
\sum_{j=0}^{n}S_{H_j}(Y)
\le
1-\Gamma_{\alpha,Q}<1.
}
\tag{9}
\]

So a polynomial-growth common source cannot Cesàro-saturate the minimal Fourier skeleton along **any** bounded integer-ratio schedule. For the physical source `Y=M`, the trivial bound `|M(n)|<=n` supplies (6) with `alpha=1`, so (8)--(9) hold unconditionally on every such chain.

## 1. Nonsquarefree stages remember every earlier endpoint

`FD-122` proves, for every `k in mathcal Q_H`,

\[
\left|
Y\!\left(\left\lfloor\frac Hk\right\rfloor\right)
-
\frac{\mu(k)}kY(H)
\right|^2
\le
C_k\,\Delta_H(Y),
\tag{10}
\]

where

\[
C_k
=
\sum_{\substack{e\mid k\\e<k}}
\frac{\mu(e)^2}{e^2}
\le
\sum_{e\ge1}\frac1{e^2}
=:\,Z
=\zeta(2).
\tag{11}
\]

Take any `i<j` on the chain and put

\[
k_{i,j}:=\frac{H_j}{H_i}
=\prod_{\ell=i+1}^{j}q_\ell.
\tag{12}
\]

This coordinate belongs to `mathcal Q_(H_j)` **exactly**, with no asymptotic membership condition: choosing `m=H_i` gives

\[
\left\lfloor\frac{H_j}{H_i}\right\rfloor=k_{i,j}.
\tag{13}
\]

Moreover

\[
Y\!\left(\left\lfloor\frac{H_j}{k_{i,j}}\right\rfloor\right)
=Y(H_i).
\tag{14}
\]

If the current transition `q_j` is nonsquarefree, then `k_(i,j)` is nonsquarefree as well, hence `mu(k_(i,j))=0`. Equations (10)--(11) therefore give

\[
|Y(H_i)|^2
\le
Z\,\Delta_{H_j}(Y).
\tag{15}
\]

Whenever `S_(H_j)>0`, substitution of (4) yields the long-range amplification inequality

\[
\boxed{
\left|
\frac{Y(H_i)}{Y(H_j)}
\right|
\le
\sqrt{
Z\left(\frac1{S_{H_j}}-1\right)
}
\qquad
(i<j,\ q_j\text{ nonsquarefree}).
}
\tag{16}
\]

The crucial point is that an intervening bad horizon does not reset the constraint. A single nonsquarefree factor in the **current** transition makes the whole quotient `H_j/H_i` nonsquarefree, and the later skeleton samples the earlier endpoint at a coordinate whose equality-ray value is exactly zero.

## 2. Polynomial growth bounds the density of highly saturated nonsquarefree stages

Fix `r in (0,1)` and set

\[
\theta(r)
:=
\sqrt{Z\left(\frac1r-1\right)}.
\tag{17}
\]

Assume `theta(r)<1`. Let

\[
G_r(n)
:=
\#\{1\le j\le n:
q_j\text{ nonsquarefree},\ S_{H_j}\ge r\}.
\tag{18}
\]

Enumerate these indices as

\[
g_1<g_2<\cdots.
\tag{19}
\]

Every listed endpoint is nonzero. Applying (16) at `j=g_m` with `i=g_(m-1)` gives

\[
|Y(H_{g_m})|
\ge
\theta(r)^{-1}|Y(H_{g_{m-1}})|.
\tag{20}
\]

Hence

\[
|Y(H_{g_m})|
\ge
|Y(H_{g_1})|\,\theta(r)^{-(m-1)}.
\tag{21}
\]

On the other hand, (5) implies `H_j<=H_0Q^j`, so the polynomial envelope (6) gives

\[
|Y(H_{g_m})|
\le
CH_0^\alpha Q^{\alpha g_m}.
\tag{22}
\]

Comparing logarithms in (21)--(22) yields

\[
\boxed{
\limsup_{n\to\infty}
\frac{G_r(n)}n
\le
\frac{\alpha\log Q}{\log(1/\theta(r))}.
}
\tag{23}
\]

For a concrete uniform choice, set

\[
\theta_{\alpha,Q}:=\frac1{2Q^\alpha},
\qquad
r_{\alpha,Q}
:=
\left(1+\frac1{4ZQ^{2\alpha}}\right)^{-1},
\tag{24}
\]

so that `theta(r_(alpha,Q))=theta_(alpha,Q)`. Put

\[
a_{\alpha,Q}
:=1-r_{\alpha,Q}
=
\frac1{4ZQ^{2\alpha}+1},
\qquad
\rho_{\alpha,Q}
:=
\frac{\alpha\log Q}{\log(2Q^\alpha)}<1.
\tag{25}
\]

Then

\[
\limsup_{n\to\infty}
\frac{G_{r_{\alpha,Q}}(n)}n
\le
\rho_{\alpha,Q}.
\tag{26}
\]

Thus a fixed positive fraction of nonsquarefree stages must have saturation below `r_(alpha,Q)` unless squarefree transitions themselves occupy most of the schedule.

## 3. Squarefree transitions supply the complementary deficit

For each fixed squarefree `q>1`, `FD-122` gives a constant `c_q>0` and, once the base horizon is large enough,

\[
\Delta_H(Y)+\Delta_{qH}(Y)
\ge
c_q\bigl(|Y(H)|^2+|Y(qH)|^2\bigr).
\tag{27}
\]

Because only the finite set `2<=q<=Q` occurs here, define

\[
c_Q^{\rm sf}
:=
\min_{\substack{2\le q\le Q\\q\text{ squarefree}}}c_q
>0,
\qquad
\delta_Q^{\rm sf}
:=
\frac{c_Q^{\rm sf}}{1+c_Q^{\rm sf}}
>0.
\tag{28}
\]

The finite-horizon thresholds in `FD-122` are uniformly absorbed after finitely many stages of (5). For every sufficiently late squarefree transition `q_j`, (27) implies

\[
\boxed{
\bigl(1-S_{H_{j-1}}\bigr)
+
\bigl(1-S_{H_j}\bigr)
\ge
\delta_Q^{\rm sf}.
}
\tag{29}
\]

Indeed, if both endpoint deficits were smaller than `delta_Q^(sf)`, then both saturations would exceed `1/(1+c_Q^(sf))`, so (4) would make each relative excess strictly smaller than `c_Q^(sf)`, contradicting (27). If an endpoint vanishes, its saturation is zero and (29) is automatic.

Let

\[
N_{\rm sf}(n)
:=
\#\{1\le j\le n:q_j\text{ squarefree}\},
\qquad
s_n:=\frac{N_{\rm sf}(n)}n.
\tag{30}
\]

Summing (29) over the squarefree transitions counts every horizon deficit at most twice. Therefore, with

\[
b_Q:=\frac{\delta_Q^{\rm sf}}2,
\tag{31}
\]

we have

\[
\frac1{n+1}
\sum_{j=0}^{n}(1-S_{H_j})
\ge
b_Qs_n-o(1).
\tag{32}
\]

The nonsquarefree stages give a second simultaneous lower bound. Among the first `n` transitions, `n-N_(sf)(n)` are nonsquarefree; by (26), at most `rho_(alpha,Q)n+o(n)` of those can have saturation at least `r_(alpha,Q)`. Every remaining one contributes deficit greater than `a_(alpha,Q)`. Hence

\[
\frac1{n+1}
\sum_{j=0}^{n}(1-S_{H_j})
\ge
 a_{\alpha,Q}
\bigl(1-\rho_{\alpha,Q}-s_n\bigr)-o(1).
\tag{33}
\]

Combining (32)--(33) and minimizing over the possible transition density `s_n` gives

\[
\min_{0\le s\le1}
\max\left\{
 b_Qs,
 a_{\alpha,Q}(1-\rho_{\alpha,Q}-s)
\right\}
=
\frac{a_{\alpha,Q}b_Q}{a_{\alpha,Q}+b_Q}
(1-\rho_{\alpha,Q}).
\tag{34}
\]

Consequently one may take

\[
\boxed{
\Gamma_{\alpha,Q}
:=
\frac{a_{\alpha,Q}b_Q}{a_{\alpha,Q}+b_Q}
(1-\rho_{\alpha,Q})
>0,
}
\tag{35}
\]

which proves (8)--(9).

The mechanism is exhaustive for bounded integer-ratio schedules. If squarefree transitions have noticeable density, their pairwise coherence gaps contribute a positive average deficit. If they do not, nonsquarefree transitions dominate, and high saturation at too many of those stages would force endpoint amplification faster than any allowed polynomial envelope.

## 4. Physical Mertens consequence and exact scope

For the physical source `Y=M`, no cancellation theorem is required. Since `mu(n) in {-1,0,1}`,

\[
|M(n)|\le n,
\tag{36}
\]

so (6) holds with `alpha=1`. Therefore every bounded integer-ratio chain satisfies

\[
\boxed{
\limsup_{n\to\infty}
\frac1{n+1}
\sum_{j=0}^{n}
S_{H_j}(M)
\le
1-\Gamma_{1,Q}<1.
}
\tag{37}
\]

This closes the simplest **nonsquarefree-transition / sparse-reset escape** left by `FD-122` at the level of bounded-ratio Cesàro saturation. The result is stronger than merely saying that one bad horizon recurs: the normalized equality-ray deficit has a fixed positive average depending only on the growth exponent and the ratio ceiling.

It is still not the pointwise theorem required by the Farey/RH target. Equation (37) permits sparse or even positive-pattern subsequences of horizons to lie very close to the equality ray; it does not force a designated horizon to pay the gap, does not bound `M(H)` separately from the skeleton energy, and does not improve the Franel--Landau critical exponent. The constants also deteriorate as `Q` grows, because the squarefree-dilation constants from `FD-122` are not uniform in the dilation.

Unbounded-ratio or supermultiplicatively sparse schedules are outside the theorem. This is not cosmetic: the earlier GCD-duality branch contains explicit sparse-saturation controls showing that large scale jumps can restore interpolation freedom under weak source envelopes. The present result therefore isolates a genuine bounded-scale coherence theorem rather than claiming a global pointwise obstruction.

## 5. Prior-art, internal precedent and adversarial audit

The mathematical pattern has an explicit **internal precedent**. `FD-021`--`FD-022` use polynomial endpoint growth and long-range quotient coordinates to turn squarefree/nonsquarefree transition alternatives into recurrent and Cesàro gaps for the older GCD-duality geometry. The present result does not claim that argument pattern as new. Its substantive delta is that `FD-122` supplies the two ingredients needed to transplant the mechanism to the current minimal Fourier skeleton: coordinate stability for every visible quotient and a positive squarefree-dilation pair gap. This removes one of the explicit current escape routes after `FD-117`--`FD-122` without adding a new source coordinate.

A targeted literature audit covered Farey--Mertens relations, Fourier treatments of Farey fractions, and the floor-quotient order/compression literature. Those subjects provide the established surrounding structures; no matching bounded-ratio Cesàro saturation theorem for the Fourier skeleton (1)--(2) was found. No external theorem is load-bearing in (8): the proof uses only the canonical `FD-122` inequalities, the elementary bound `C_k<=zeta(2)`, and the polynomial envelope. Accordingly no new source anchor is required in `SOURCES.md`.

The owner-side stress test checked the main failure modes explicitly. The quotient coordinate `H_j/H_i` is genuinely in `mathcal Q_(H_j)` rather than merely asymptotically visible; nonsquarefreeness of the current transition propagates to that whole quotient; zero endpoints are harmless because they have saturation zero; the density argument remains valid for `alpha=0`; bounded `Q` makes the squarefree thresholds uniform after finitely many stages; and the Cesàro conclusion is not silently upgraded to a pointwise endpoint bound.

The durable conclusion is therefore narrow but positive: **on the minimal Farey/Mertens Fourier skeleton, the repeated-prime/nonsquarefree transition escape cannot sustain Cesàro near-saturation along any bounded-ratio chain whose source has polynomial growth.** The remaining obstruction is genuinely pointwise or unbounded-scale: force the designated RH-relevant horizon to carry a positive relative excess, obtain constants stable as the dilation family grows, or introduce additional arithmetic structure beyond cumulative discrepancy.