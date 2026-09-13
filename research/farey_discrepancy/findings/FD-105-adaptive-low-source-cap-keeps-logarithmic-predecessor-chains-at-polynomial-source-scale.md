# FD-105 — adaptive low-source cap keeps logarithmic predecessor chains at polynomial source scale

**Status:** `EXACT-DERIVED + LOW-SOURCE-ENERGY-CAP + MASS-ADAPTIVE-SOURCE-LOCALIZATION + SOURCE-TAGGED-PREDECESSOR + POLYNOMIAL-SCALE-LOGARITHMIC-CHAIN + FALSE-RH-COMPOSITION + AMORTIZED-BRANCH-FRONTIER`.

`FD-104` makes predecessor composition uniform above the linear nonsquarefree mass floor, but its effective logarithmic-depth theorem still has an explicit escape: the chain is guaranteed for `xi log H_0` steps only **unless** the physical horizon falls into a fixed bounded range first. Its updated frontier therefore asks for a persistent large source quotient/tag along the high-mass chain.

That source information is already forced by high mass. The exact one-Lipschitz source law implies a deterministic cap on all physical energy carried by rows whose quotient-shell source argument is at most `L`:

\[
\boxed{
E_H^{\le L}\le 2H(L+1)
}
\tag{1}
\]

for `L=o(H)`, once `H` is large. Hence a state with `U_H\gg H` cannot place most of its nonsquarefree mass on bounded or too-small source arguments. At the adaptive threshold

\[
L_H:=\left\lfloor\frac{U_H}{H\log H}\right\rfloor,
\tag{2}
\]

any fixed-power high-mass state `U_H>=H^(1+delta)` has

\[
\boxed{
U_H^{>L_H}=(1-o(1))U_H.
}
\tag{3}
\]

Moreover those source-rich rows automatically lie in the intrinsic row core `r<=H/(L_H+1)`. Repeating the direct compression of `FD-104` only on this core has total shell error `o(U_H)` without using the global source envelope or an externally chosen row exponent `rho`.

Tracking the quotient labels through the exact odd, dyadic-eligible, dyadic-terminal, and head repairs shows more. For every fixed `1/2<sigma<Theta`, the same branch constant `b_sigma>0` of `FD-104` yields a predecessor `C<H` carrying a nonsquarefree mask supported on source arguments larger than `L_H/2`, with

\[
\boxed{
\frac{U_C^{>L_H/2}}{C^{2\sigma}}
\ge
b_\sigma\frac{U_H}{H^{2\sigma}}.
}
\tag{4}
\]

Thus the mass recurrence is automatically a **source-tagged** recurrence. In particular,

\[
\boxed{
C\gg \frac{U_H}{H\log H}.
}
\tag{5}
\]

Combining (5) with the normalized-mass recurrence of `FD-104` removes its bounded-scale escape. Starting from a strict-record entry `H_0` of `FD-096`, for every

\[
\xi<\frac{2(\Theta-\sigma)}{|\log b_\sigma|}
\tag{6}
\]

and every fixed

\[
0<\gamma<2(\Theta-\sigma)-\xi|\log b_\sigma|,
\tag{7}
\]

the predecessor chain exists for every `0<=j<=xi log H_0` once `H_0` is large, and throughout that chain

\[
\boxed{
H_j\ge H_0^{\gamma-o(1)},
\qquad
x_j\ge H_0^{\gamma-o(1)}
}
\tag{8}
\]

for the source quotient `x_j` carried by the selected predecessor mask, with the source statement starting after the first transport. Thus the alternative “or the chain reaches a fixed bounded range first” in `FD-104` is not real in the high-mass regime: the entire guaranteed logarithmic chain remains at polynomial physical **and source** scale relative to its entry.

This still does not prove RH. Feeding the new source floor back into the worst-branch scalar recurrence remains compatible with the exact nonhead ceiling of `FD-102`. The next gate is therefore not persistence of a polynomial source tag, but a branch-sensitive relation between normalized-mass loss, actual horizon contraction, and source descent. The global minimum `b_sigma` discards precisely that information.

## 1. A deterministic cap for the low-source sector

Write, as before,

\[
V_H(r)
=\sqrt{w(r)}\,\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right),
\qquad
w(r)=\frac{J_2(r)}{r^2},
\tag{9}
\]

and

\[
E_H=\sum_{1<r\le H}|V_H(r)|^2,
\qquad
U_H=\sum_{\substack{1<r\le H\\\mu(r)=0}}|V_H(r)|^2.
\tag{10}
\]

For a real cutoff `L>=1`, define

\[
E_H^{\le L}
:=
\sum_{\substack{1<r\le H\\\lfloor H/r\rfloor\le L}}
|V_H(r)|^2,
\qquad
U_H^{\le L}
:=
\sum_{\substack{1<r\le H\\\mu(r)=0\\\lfloor H/r\rfloor\le L}}
|V_H(r)|^2.
\tag{11}
\]

The physical source satisfies `mathcal H(0)=0` and the exact increment bound

\[
|\mathcal H(n+1)-\mathcal H(n)|\le1,
\]

so

\[
|\mathcal H(n)|\le n.
\tag{12}
\]

Also `w(r)<=1`. If `floor(H/r)<=L`, then

\[
r>\frac{H}{L+1}.
\tag{13}
\]

Therefore, whenever `H/(L+1)>=2`,

\[
\begin{aligned}
U_H^{\le L}
&\le E_H^{\le L}\\
&\le H^2\sum_{r>H/(L+1)}\frac1{r^2}\\
&\le 2H(L+1).
\end{aligned}
\tag{14}
\]

This proves (1). No cancellation, zeta-zero estimate, density theorem, or squarefree-counting input enters.

The same pointwise estimate gives

\[
U_H\le E_H
\le H^2\sum_{r=2}^{\infty}r^{-2}
<H^2.
\tag{15}
\]

Hence `L_H=o(H)`. Under the high-mass hypothesis

\[
U_H\ge H^{1+\delta}
\tag{16}
\]

for fixed `delta>0`, one has `L_H->infinity`, and (14) gives

\[
U_H^{\le L_H}
\le
\frac{2U_H}{\log H}+2H
=o(U_H).
\tag{17}
\]

This proves (3).

The scale `U_H/H` is intrinsic. At the exact linear floor `U_H=H^(1+o(1))`, equation (2) need not tend to infinity, matching the quotient-one rows isolated in `FD-104`. Thus source localization degenerates exactly where the high-mass predecessor theorem itself loses its power margin.

## 2. Source-rich rows form their own compression core

Let

\[
\mathcal G_H^{\rm src}
:=
\left\{
2\le r\le H:
\mu(r)=0,
\left\lfloor\frac Hr\right\rfloor>L_H
\right\}.
\tag{18}
\]

Every row in this set satisfies

\[
r\le\frac{H}{L_H+1},
\]

so

\[
\#\mathcal G_H^{\rm src}
\le\frac{H}{L_H+1}
\ll\frac{H^2\log H}{U_H}.
\tag{19}
\]

For each retained row choose, exactly as in `FD-104`, the smallest prime `p` with `p^2|r`, write `r=ps`, and set

\[
A_p=\left\lceil\frac Hp\right\rceil.
\tag{20}
\]

If

\[
x:=\left\lfloor\frac H{ps}\right\rfloor,
\qquad
y:=\left\lfloor\frac{A_p}{s}\right\rfloor,
\]

then the exact floor comparison of `FD-104` gives

\[
y\in\{x,x+1\}.
\tag{21}
\]

Thus every retained source-rich row stays source-rich after first deflation:

\[
\boxed{y>L_H.}
\tag{22}
\]

The radical and Jordan weight are unchanged, and the source increment error is at most one per retained row. Hence the squared compression error is at most

\[
\#\mathcal G_H^{\rm src}
\ll\frac{H^2\log H}{U_H}.
\tag{23}
\]

Relative to the parent mass,

\[
\frac{H^2\log H}{U_H^2}
\le H^{-2\delta}\log H
=o(1).
\tag{24}
\]

Combining (3) and (24), the source-rich compressed packets carry

\[
\boxed{
\sum_p
\|P_{S_{p,H}^{\rm src}}V_{A_p,1}\|_2^2
\ge(1-o(1))U_H.
}
\tag{25}
\]

This is stronger than merely choosing the `rho`-core of `FD-104`: the row cutoff is forced by the mass itself, all retained coordinates already have a quantitative source label, and the global envelope `|mathcal H(n)|<<n^tau` is not needed for the truncation.

## 3. Every exact repair preserves the adaptive source scale

Run the branch analysis of `FD-104` on the packets in (25).

For an odd repeated prime, `FD-091` writes `s=pt`, sends the row to `u=4t`, and uses

\[
C_p=4\left\lfloor\frac{A_p}{p}\right\rfloor.
\tag{26}
\]

Its exact quotient identity is

\[
\left\lfloor\frac{C_p}{u}\right\rfloor
=
\left\lfloor\frac{A_p}{s}\right\rfloor
=y>L_H.
\tag{27}
\]

For the dyadic eligible branch, the half-scale state `A_2` retains the same first-deflated row and therefore the same `y>L_H`.

For the dyadic terminal nonhead branch, `FD-093` writes the first-deflated row as `s=2m`, then repairs `m=pt` to row `4t` at horizon `4 floor(B/p)`. Its exact identity gives

\[
\left\lfloor\frac{4\lfloor B/p\rfloor}{4t}\right\rfloor
=
\left\lfloor\frac Bm\right\rfloor
=
\left\lfloor\frac{A_2}{2m}\right\rfloor
=y>L_H.
\tag{28}
\]

Only the dyadic head changes the source argument. There the first-deflated source is exactly `B=y>L_H`. With the `lambda=1/2` retreat used in `FD-104`,

\[
S=|\mathcal H(B)|,
\qquad
h=\left\lfloor\frac S2\right\rfloor,
\qquad
Y=B-h.
\tag{29}
\]

Since `S<=B`,

\[
Y\ge\frac B2>\frac{L_H}{2}.
\tag{30}
\]

The destination row `4` at horizon `4Y` therefore also lies above the source threshold `L_H/2`.

Consequently every branch used to prove `FD-104` can be run with its destination mask restricted to source arguments larger than `L_H/2`. Since (25) still carries `(1-o(1))U_H`, the same fixed slack in

\[
b_\sigma
=
\frac12\min\left\{
 c_{\rm odd}(\sigma),
 2^{2\sigma-2},
 c_{\rm term}(\sigma),
 \frac1{32}
\right\}
\tag{31}
\]

absorbs the new vanishing errors. This proves (4).

The destination mask is nonsquarefree in every branch. Hence every one of its rows is at least `4`. If one such row samples a source argument larger than `L_H/2`, then

\[
C>2L_H.
\tag{32}
\]

Using (2), (16), and `L_H->infinity`,

\[
\boxed{
C\gg\frac{U_H}{H\log H}.
}
\tag{33}
\]

This proves (5).

As a finite floor-geometry stress test, the first-deflation identity and the odd/dyadic exact reembeddings were exhaustively checked for every source-rich nonsquarefree row for `20<=H<250`; no exception occurred. This computation is only a guard against indexing mistakes—the proof is the exact floor algebra above.

## 4. The `FD-104` logarithmic chain can no longer collapse early

Take a strict-record entry `H_0` supplied by `FD-096`, fix

\[
\frac12<\sigma<\Theta,
\]

and retain

\[
\mathfrak U_\sigma(H)=\frac{U_H}{H^{2\sigma}}.
\tag{34}
\]

`FD-104` gives

\[
\mathfrak U_\sigma(H_j)
\ge
b_\sigma^j H_0^{2(\Theta-\sigma)-o(1)}
\tag{35}
\]

at every realized predecessor step. Fix `xi` as in (6), and put

\[
\Gamma
:=
2(\Theta-\sigma)-\xi|\log b_\sigma|>0.
\tag{36}
\]

Uniformly for every `j<=xi log H_0`,

\[
\mathfrak U_\sigma(H_j)
\ge H_0^{\Gamma-o(1)}.
\tag{37}
\]

Therefore

\[
\frac{U_{H_j}}{H_j}
=
\mathfrak U_\sigma(H_j)H_j^{2\sigma-1}
\ge
H_0^{\Gamma-o(1)},
\tag{38}
\]

because `2sigma-1>0`. Applying (2) at the current state gives

\[
L_{H_j}
\ge H_0^{\Gamma-o(1)}.
\tag{39}
\]

Equations (4) and (32) now show that the next predecessor has both a source tag and a horizon satisfying

\[
x_{j+1}\ge H_0^{\Gamma-o(1)},
\qquad
H_{j+1}\ge H_0^{\Gamma-o(1)}.
\tag{40}
\]

Thus the lower state is automatically still asymptotic, while (37) also keeps it in the fixed-power high-mass regime required to repeat the construction. Induction removes the stopping alternative in `FD-104`: for every fixed `gamma<Gamma`, all sufficiently large entries admit the full chain through `floor(xi log H_0)` steps, and all noninitial horizons and selected source tags exceed `H_0^gamma` up to subpower factors.

The conclusion is stronger than saying that the source argument is a positive power of the **current** horizon. It stays a positive power of the original entry scale throughout the entire guaranteed logarithmic depth.

## 5. The worst-branch scalar bounds still fit below the `FD-102` ceiling

The result closes the bounded-scale and lost-tag escapes, but it does not by itself force source descent. The reason can be seen by feeding the adaptive floor back into the current worst-branch recurrence rather than using only the crude bound `H_j>=1`.

Write

\[
L_\sigma:=\log_2(1/b_\sigma),
\qquad
q:=2\sigma-1,
\qquad
A:=2(\Theta-\sigma).
\tag{41}
\]

At depth `m=d log_2 H_0`, equation (35) supplies the normalized-mass exponent

\[
A-L_\sigma d.
\tag{42}
\]

If the current horizon has exponent `h`, meaning `H_m=H_0^(h+o(1))`, then the adaptive source floor (2) has exponent at least

\[
A-L_\sigma d+qh.
\tag{43}
\]

The next horizon has at least the same exponent, up to the negligible logarithmic denominator in (2). After the finite initial transient, the natural lower-envelope fixed point of these **scalar** inequalities is therefore

\[
\boxed{
h_*(d)=s_*(d)
=
\frac{A-L_\sigma d}{1-q}
=
\frac{2(\Theta-\sigma)-L_\sigma d}
{2(1-\sigma)}
}
\tag{44}
\]

while the numerator is positive.

For a consecutive nonhead segment, `FD-102` gives exactly

\[
8x_m-1\le\frac{H_0-1}{2^m},
\tag{45}
\]

so its exponent-level source ceiling is `1-d`. The scalar lower envelope (44) stays strictly below that ceiling:

\[
\begin{aligned}
1-d-h_*(d)
&=
\frac{
2(1-\Theta)
+d\bigl(L_\sigma-2(1-\sigma)\bigr)
}
{2(1-\sigma)}\\
&>0.
\end{aligned}
\tag{46}
\]

Indeed `Theta<=1`, while (31) gives `b_sigma<=1/64`, hence `L_sigma>=6>2(1-sigma)`.

Equation (46) is an adversarial **scalar feasibility check**, not a construction of a physical predecessor genealogy. Its role is narrower and safer: even after the new source floor is fed back self-consistently, the worst-branch mass recurrence and the exact `FD-102` nonhead ceiling do not algebraically collide. Therefore comparing only those scalar bounds cannot close the argument.

This points to the next refinement. Equation (46) uses the minimum branch coefficient at every generation and forgets how much horizon contraction each branch actually buys. The dyadic eligible branch, odd `p`-branches, repaired terminal branches, and source-head retreats have very different pairs of mass loss and geometric progress. A useful continuation should use a branch-additive or amortized potential that charges normalized-mass loss against the actual contraction/source movement of the same branch, rather than collapsing all channels to `b_sigma` before iterating.

## 6. Stress tests, prior art, and updated frontier

The linear low-source sector from `FD-104` is the matched endpoint control. Rows `H/2<r<=H` divisible by `4` have source quotient `1` and already contribute `gg H` to `U_H`. At mass `U_H=H^(1+o(1))`, the adaptive threshold `L_H` need not grow, so neither (3) nor the polynomial source floor can be strengthened across the linear boundary by this argument. The high-mass hypothesis is therefore aligned with an actual physical carrier, not merely with the proof.

The exact quotient-preservation statements (27)--(28) were already established in `FD-091` and `FD-093`; the new ingredient is to start those repairs from the mass-adaptive source-rich core and keep its source label throughout the branch split. The head loss by a factor at most two in (30) is exact from the one-Lipschitz source law used in `FD-095`.

The literature audit rechecked the current Farey local-discrepancy formulas of García (2025), the July 2026 average-local-discrepancy/gap-order result already anchored in this line, the classical Franel--Landau/Mertens and Smith/GCD boundaries, and recent work on Farey fractions with `k`-free denominators. Those results concern discrepancy identities, denominator restrictions, gap statistics, or divisor algebra; no located source states the low-source Jordan-energy cap (14), the mass-adaptive source cutoff (2), or the source-tagged predecessor recurrence (4). No external theorem is load-bearing here, so `SOURCES.md` requires no change.

`FD-104` left two possible reasons why its effective predecessor chain might fail to communicate with `FD-102`: the chain could collapse to bounded physical scale, or its intermediate states could lose every polynomially large source tag because they were no longer frontier-sharp. Both possibilities are removed here. High occupied mass itself forces a source-rich core at scale `U_H/(H log H)`, and the exact predecessor repairs carry that core into the next physical state. Along the whole `FD-104` logarithmic window, both the horizons and the selected source arguments remain polynomial in the original entry scale.

The remaining obstruction is genuinely compositional. The current scalar recurrence pays the worst branch loss `b_sigma` at every generation before comparing with the exact source potential, and (46) shows that this coarse-graining still leaves room below the `FD-102` ceiling. The next useful theorem should keep branch labels and amortize **mass loss versus actual horizon/source progress** step by step; alternatively it must recover a stronger source-amplitude/record constraint after retagging. Merely proving that a large source quotient persists is no longer an open gate.
