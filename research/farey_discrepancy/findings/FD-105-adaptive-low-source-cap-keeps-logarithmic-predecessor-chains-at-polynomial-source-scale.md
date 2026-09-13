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

Moreover those source-rich rows automatically lie in the intrinsic row core `r<=H/(L_H+1)`. Repeating the direct compression of `FD-104` only on this source-rich core has total shell error `o(U_H)` without using the global source envelope or an externally chosen row exponent `rho`.

Tracking the quotient labels through the exact odd, dyadic-eligible, dyadic-terminal, and head repairs shows more: for every fixed `1/2<sigma<Theta`, the same branch constant `b_sigma>0` of `FD-104` yields a predecessor `C<H` carrying a nonsquarefree mask supported on source arguments larger than `L_H/2`, with

\[
\boxed{
\frac{U_C^{>L_H/2}}{C^{2\sigma}}
\ge
b_\sigma\frac{U_H}{H^{2\sigma}}.
}
\tag{4}
\]

Thus the mass recurrence is automatically a **source-tagged** recurrence. In particular the selected lower horizon obeys

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

the predecessor chain exists for **every**

\[
0\le j\le \xi\log H_0
\]

once `H_0` is large, and throughout that chain

\[
\boxed{
H_j\ge H_0^{\gamma-o(1)},
\qquad
x_j\ge H_0^{\gamma-o(1)}
}
\tag{8}
\]

for the source quotient `x_j` carried by the selected predecessor mask (with the source statement starting after the first transport). Thus `FD-104`'s alternative “or the chain reaches a fixed bounded range first” is not real in the high-mass regime: the entire guaranteed logarithmic chain remains at polynomial physical **and source** scale relative to its entry.

This still does not prove RH. An adversarial comparison with the exact source budget of `FD-102` shows why. The worst-branch constant satisfies `b_sigma<=1/64`, so the source exponent guaranteed after `d log_2 H_0` steps is no better than

\[
\Gamma(d)=2(\Theta-\sigma)-d\log_2(1/b_\sigma).
\tag{9}
\]

A consecutive nonhead segment is geometrically compatible with `FD-102` whenever its final source is below `H_0^(1-d+o(1))`. But

\[
d+\Gamma(d)
=2(\Theta-\sigma)
-d\bigl(\log_2(1/b_\sigma)-1\bigr)
<1.
\tag{10}
\]

So the new polynomial source floor never exhausts the exact nonhead source budget under the current **global minimum** branch loss. The live obstruction has therefore moved again: not persistence of a large source tag, but an amortized branch-specific relation between normalized-mass loss, horizon contraction, and source descent. The global `b_sigma` discards precisely that branch information.

## 1. A deterministic cap for the low-source sector

Write, as before,

\[
V_H(r)
=\sqrt{w(r)}\,\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right),
\qquad
w(r)=\frac{J_2(r)}{r^2},
\tag{11}
\]

and

\[
E_H=\sum_{1<r\le H}|V_H(r)|^2,
\qquad
U_H=\sum_{\substack{1<r\le H\\\mu(r)=0}}|V_H(r)|^2.
\tag{12}
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
\tag{13}
\]

The physical source satisfies `mathcal H(0)=0` and the exact increment bound

\[
|\mathcal H(n+1)-\mathcal H(n)|\le1,
\]

so

\[
|\mathcal H(n)|\le n.
\tag{14}
\]

Also `w(r)<=1`. If `floor(H/r)<=L`, then

\[
r>\frac{H}{L+1}.
\tag{15}
\]

Therefore, whenever `H/(L+1)>=2`,

\[
\begin{aligned}
U_H^{\le L}
&\le E_H^{\le L}\\
&\le H^2
\sum_{r>H/(L+1)}\frac1{r^2}\\
&\le 2H(L+1).
\end{aligned}
\tag{16}
\]

This proves (1). No cancellation, zeta-zero estimate, density theorem, or squarefree-counting input enters.

There is also a useful global normalization check. From the same pointwise bound,

\[
U_H\le E_H
\le H^2\sum_{r=2}^{\infty}r^{-2}
<H^2.
\tag{17}
\]

Hence the adaptive cutoff (2) always satisfies `L_H=o(H)`. Under the high-mass hypothesis

\[
U_H\ge H^{1+\delta}
\tag{18}
\]

for fixed `delta>0`, one has `L_H->infinity`, and (16) gives

\[
U_H^{\le L_H}
\le
\frac{2U_H}{\log H}+2H
=o(U_H).
\tag{19}
\]

This is (3).

The scale `U_H/H` is intrinsic. At the exact linear floor `U_H=H^(1+o(1))`, equation (2) need not tend to infinity, matching the quotient-one rows isolated in `FD-104`. Thus the source localization degenerates exactly where the high-mass predecessor theorem itself loses its power margin.

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
\tag{20}
\]

Every row in this set satisfies

\[
r\le\frac{H}{L_H+1},
\tag{21}
\]

so

\[
\#\mathcal G_H^{\rm src}
\le\frac{H}{L_H+1}
\ll\frac{H^2\log H}{U_H}.
\tag{22}
\]

For each retained row choose, exactly as in `FD-104`, the smallest prime `p` with `p^2|r`, write `r=ps`, and set

\[
A_p=\left\lceil\frac Hp\right\rceil.
\tag{23}
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
\tag{24}
\]

Thus every retained source-rich row stays source-rich after first deflation:

\[
\boxed{y>L_H.}
\tag{25}
\]

The radical and Jordan weight are unchanged, and the source increment error is at most one per retained row. Hence the squared compression error is at most

\[
\#\mathcal G_H^{\rm src}
\ll\frac{H^2\log H}{U_H}.
\tag{26}
\]

Relative to the parent mass this is

\[
\frac{H^2\log H}{U_H^2}
\le H^{-2\delta}\log H
=o(1).
\tag{27}
\]

Combining (3) and (27), the source-rich compressed packets carry

\[
\boxed{
\sum_p
\|P_{S_{p,H}^{\rm src}}V_{A_p,1}\|_2^2
\ge(1-o(1))U_H.
}
\tag{28}
\]

This is stronger than merely choosing the `rho`-core of `FD-104`: the row cutoff is forced by the mass itself, all retained coordinates already have a quantitative source label, and the global envelope `|mathcal H(n)|<<n^tau` is not needed for the truncation.

## 3. Every exact repair preserves the adaptive source scale

Run the branch analysis of `FD-104` on the packets in (28).

For an odd repeated prime, `FD-091` writes `s=pt`, sends the row to `u=4t`, and uses

\[
C_p=4\left\lfloor\frac{A_p}{p}\right\rfloor.
\tag{29}
\]

Its exact quotient identity is

\[
\left\lfloor\frac{C_p}{u}\right\rfloor
=
\left\lfloor\frac{A_p}{s}\right\rfloor
=y>L_H.
\tag{30}
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
\tag{31}
\]

Only the dyadic head changes the source argument. There the first-deflated source is exactly `B=y>L_H`. With the `lambda=1/2` retreat used in `FD-104`,

\[
S=|\mathcal H(B)|,
\qquad
h=\left\lfloor\frac S2\right\rfloor,
\qquad
Y=B-h.
\tag{32}
\]

Since `S<=B`,

\[
Y\ge\frac B2>\frac{L_H}{2}.
\tag{33}
\]

The destination row `4` at horizon `4Y` therefore also lies above the source threshold `L_H/2`.

Consequently every branch used to prove `FD-104` can be run with its destination mask restricted to source arguments larger than `L_H/2`. Since (28) still carries `(1-o(1))U_H`, the same fixed slack in the definition

\[
b_\sigma
=
\frac12\min\left\{
 c_{\rm odd}(\sigma),
 2^{2\sigma-2},
 c_{\rm term}(\sigma),
 \frac1{32}
\right\}
\tag{34}
\]

absorbs the new vanishing errors. This proves (4).

The destination mask is nonsquarefree in every branch. Hence every one of its rows is at least `4`. If one such row samples a source argument larger than `L_H/2`, then

\[
C>2L_H.
\tag{35}
\]

Using (2), (18), and `L_H->infinity`,

\[
\boxed{
C\gg\frac{U_H}{H\log H}.
}
\tag{36}
\]

This is the mass-adaptive physical-scale floor asserted in (5).

As a finite floor-geometry stress test, the first-deflation identity and the odd/dyadic exact reembeddings were exhaustively checked for every source-rich nonsquarefree row for `20<=H<250`; no exception occurred. This computation is only a guard against indexing mistakes—the proof is the exact floor algebra above.

## 4. The `FD-104` logarithmic chain can no longer collapse early

Take a strict-record entry `H_0` supplied by `FD-096`, fix

\[
\frac12<\sigma<\Theta,
\]

and retain the normalized occupied mass

\[
\mathfrak U_\sigma(H)=\frac{U_H}{H^{2\sigma}}.
\tag{37}
\]

`FD-104` gives

\[
\mathfrak U_\sigma(H_j)
\ge
b_\sigma^j H_0^{2(\Theta-\sigma)-o(1)}
\tag{38}
\]

at every realized predecessor step. Fix `xi` as in (6), and write

\[
\Gamma
:=
2(\Theta-\sigma)-\xi|\log b_\sigma|>0.
\tag{39}
\]

Uniformly for every `j<=xi log H_0`, equation (38) gives

\[
\mathfrak U_\sigma(H_j)
\ge H_0^{\Gamma-o(1)}.
\tag{40}
\]

Therefore

\[
\frac{U_{H_j}}{H_j}
=
\mathfrak U_\sigma(H_j)H_j^{2\sigma-1}
\ge
H_0^{\Gamma-o(1)},
\tag{41}
\]

because `2sigma-1>0`. Applying (2) at the current state gives

\[
L_{H_j}
\ge H_0^{\Gamma-o(1)}.
\tag{42}
\]

Equations (4) and (35) now show that the next predecessor has both a source tag and a horizon satisfying

\[
x_{j+1}\ge H_0^{\Gamma-o(1)},
\qquad
H_{j+1}\ge H_0^{\Gamma-o(1)}.
\tag{43}
\]

Thus the lower state is automatically still in the asymptotic high-mass regime where the predecessor theorem applies. Induction removes the stopping alternative in `FD-104`: for every fixed `gamma<Gamma`, all sufficiently large entries admit the full chain through `floor(xi log H_0)` steps, and all its noninitial horizons and selected source tags exceed `H_0^gamma` up to subpower factors. This proves (8).

The conclusion is stronger than saying that the source argument is a positive power of the **current** horizon. It stays a positive power of the original entry scale throughout the entire guaranteed logarithmic depth.

## 5. Why the exact `FD-102` source budget still does not close

The new source floor is enough to remove bounded-scale collapse, but it is not enough to force a contradiction with the exact nonhead potential of `FD-102`.

Write a depth as

\[
m=d\log_2H_0.
\tag{44}
\]

Ignoring only subpower factors, (38) guarantees the source scale

\[
x_m
\gtrsim
H_0^{\Gamma(d)},
\qquad
\Gamma(d)
:=
2(\Theta-\sigma)
-d\log_2(1/b_\sigma),
\tag{45}
\]

as long as `Gamma(d)>0`. On the other hand the exact `FD-102` geometry for a consecutive nonhead segment gives

\[
8x_m-1
\le
\frac{H_0-1}{2^m},
\tag{46}
\]

whose exponent-level upper scale is `H_0^(1-d)`.

These two inequalities would conflict only if

\[
d+\Gamma(d)>1.
\tag{47}
\]

But the global branch constant of `FD-104` contains the head coefficient `1/32` and the outer factor `1/2`, so

\[
b_\sigma\le\frac1{64},
\qquad
\log_2(1/b_\sigma)\ge6.
\tag{48}
\]

Consequently

\[
\begin{aligned}
d+\Gamma(d)
&=
2(\Theta-\sigma)
-d\bigl(\log_2(1/b_\sigma)-1\bigr)\\
&\le
2(\Theta-\sigma)
<1.
\end{aligned}
\tag{49}
\]

So the present worst-branch recurrence leaves a strict exponent gap to the source-budget wall for every admissible depth. This is a useful negative result: simply inserting the now-available persistent source tag into `FD-102` cannot finish the descent argument.

The comparison also points to the correct next refinement. Equation (49) uses the **minimum** branch coefficient at every generation and forgets how much horizon contraction each branch actually buys. The dyadic eligible branch, odd `p`-branches, repaired terminal branches, and source-head retreats have very different pairs of mass loss and geometric progress. A successful continuation should therefore use a branch-additive or amortized potential that charges normalized-mass loss against the actual contraction/source movement of that same branch, rather than collapsing all channels to `b_sigma` before iterating.

## 6. Stress tests, prior art, and novelty boundary

The linear low-source sector from `FD-104` is the matched endpoint control. Rows `H/2<r<=H` divisible by `4` have source quotient `1` and already contribute `gg H` to `U_H`. At mass `U_H=H^(1+o(1))`, the adaptive threshold `L_H` need not grow, so neither (3) nor the polynomial source floor can be strengthened across the linear boundary by this argument. The high-mass hypothesis is therefore aligned with an actual physical carrier, not merely with the proof.

The exact quotient-preservation statements in (30)--(31) were already established in `FD-091` and `FD-093`; the only new ingredient is to start those repairs from the mass-adaptive source-rich core and to keep its source label throughout the branch split. The head loss by a factor at most two in (33) is also exact from the one-Lipschitz source law used in `FD-095`.

The literature audit rechecked the current Farey local-discrepancy formulas of García (2025), the July 2026 average-local-discrepancy/gap-order result already anchored in this line, the classical Franel--Landau/Mertens and Smith/GCD boundaries, and recent work on Farey fractions with `k`-free denominators. Those results concern discrepancy identities, denominator restrictions, gap statistics, or divisor algebra; no located source states the low-source Jordan-energy cap (16), the mass-adaptive source cutoff (2), or the source-tagged predecessor recurrence (4). No external theorem is load-bearing here, so `SOURCES.md` requires no change.

## 7. Updated frontier

`FD-104` left two possible reasons why its effective predecessor chain might fail to communicate with `FD-102`: the chain could collapse to bounded physical scale, or its intermediate states could lose every polynomially large source tag because they were no longer frontier-sharp. Both possibilities are removed here. High occupied mass itself forces a source-rich core at scale `U_H/(H log H)`, and the exact predecessor repairs carry that core into the next physical state. Along the whole `FD-104` logarithmic window, both the horizons and the selected source arguments remain polynomial in the original entry scale.

The remaining obstruction is therefore genuinely compositional. The current scalar recurrence pays the worst branch loss `b_sigma` at every generation before comparing with the exact source potential, and (49) proves that this coarse-graining leaves too much source budget. The next useful theorem should keep the branch labels and amortize **mass loss versus actual horizon/source progress** step by step; alternatively it must recover a stronger source-amplitude/record constraint after retagging. Merely proving that a large source quotient persists is no longer an open gate.