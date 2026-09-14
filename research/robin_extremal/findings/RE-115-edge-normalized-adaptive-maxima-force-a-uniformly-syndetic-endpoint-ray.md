# RE-115 — edge-normalized adaptive maxima force a uniformly syndetic endpoint ray

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + EDGE-NORMALIZED-ADAPTIVE-SELECTOR + MOVING-THRESHOLD + ENDPOINT-MIXED-RACE-RAY + UNIFORM-ALMOST-PERIODICITY + NEGATIVE/OBSTRUCTION + PRIOR-ART-AUDITED`.

Assume RH is false with finite attained zero edge

\[
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1,
\qquad
c:=1-\Theta\in(0,1/2),
\tag{1}
\]

and retain the actual edge profiles from `RE-113`--`RE-114`,

\[
F_\Theta(u)
=
\sum_{\Re\rho=\Theta}\frac{e^{i\Im(\rho)u}}{\rho},
\qquad
G_\Theta(u)
=
\sum_{\Re\rho=\Theta}\frac{e^{i\Im(\rho)u}}{1-\rho}.
\tag{2}
\]

A tempting response to `RE-114` is to move the adaptive exponent toward the spectral endpoint `b=c=1-Theta`. Fixed `b>c` detects amplitudes `Y^{-b}`, whereas the actual edge scale isolated by `RE-113` is

\[
h(C)\asymp \frac{Y^{-c}}{\log Y},
\qquad Y=\log C.
\tag{3}
\]

The missing logarithm suggests replacing the fixed-power amplitude by the edge-normalized block functional

\[
\boxed{
B_\Theta(C)
:=Y^c\log Y\,\bigl(e^{h(C)}-1\bigr).
}
\tag{4}
\]

That retuning is exact, but it does **not** create a new spectral obstruction.

Let `C` be the rightmost maximizer of `B_Theta` on any sufficiently large finite positive CA block and put

\[
Y:=\log C,
\qquad
q:=B_\Theta(C),
\qquad
a(C):=1-e^{-h(C)}.
\tag{5}
\]

Then `C` is a regular CA tangent state for a unique event parameter `Z>Y`, with

\[
\boxed{
Y=\Phi(Z),
\qquad
\frac1{Z\log Z}
=
\frac1{Y\log Y}
-
\frac{b_Ya(C)}Y,
\qquad
b_Y:=c+\frac1{\log Y}.
}
\tag{6}
\]

Thus the logarithmic correction in (4) has a precise variational meaning: it generates a **moving adaptive exponent**

\[
\boxed{b_Y\downarrow c.}
\tag{7}
\]

Suppose along an unbounded sequence of such block maximizers

\[
\liminf q>0.
\tag{8}
\]

Then the full source projections force

\[
\boxed{
q\asymp1,
\qquad
F_\Theta(\log Y)=c\,q+o(1),
\qquad
G_\Theta(\log Y)=\Theta\,q+o(1).
}
\tag{9}
\]

Equivalently the limiting mixed-race slope is the endpoint ray

\[
\boxed{
\frac{G_\Theta(\log Y)}{F_\Theta(\log Y)}
\longrightarrow
\frac{\Theta}{1-\Theta}.
}
\tag{10}
\]

Condition (8) is not an artificial extra branch if one is trying to close the surviving near-minimal recovery regime. `RE-113` proves that any unbounded fixed-constant near-minimal recovery family has

\[
h(C_0)Y_0^c\log Y_0\asymp1.
\tag{11}
\]

On every corresponding positive block, the `B_Theta` maximizer satisfies

\[
B_\Theta(C)\ge B_\Theta(C_0)\gg1,
\tag{12}
\]

so (8) follows automatically. Hence every surviving near-minimal family generates a second, edge-normalized family of genuine regular CA selectors obeying (9).

The endpoint ray is nevertheless spectrally noncoercive. In fact `RE-114` can be strengthened uniformly **through the endpoint**. There exist constants

\[
\delta>0,\qquad \eta>0,\qquad L<\infty
\tag{13}
\]

depending only on the attained edge face such that

\[
[c,c+\delta]\subset(0,1/2)
\tag{14}
\]

and, for every `b in [c,c+delta]`, every interval of logarithmic phase of length `L` contains a point `u` satisfying

\[
\boxed{
bG_\Theta(u)-(1-b)F_\Theta(u)=0,
\qquad
F_\Theta(u)\ge\eta,
\qquad
G_\Theta(u)\ge\eta.
}
\tag{15}
\]

The constants are uniform in `b`. In particular (15) applies to the moving exponents `b_Y=c+1/log Y` for all sufficiently large `Y`. At the endpoint itself the ray equation is simply a stationary-point condition for the stable-filter state of `RE-114`.

Therefore pushing the adaptive threshold all the way down to the natural finite-edge amplitude does not evade the `RE-114` obstruction. It produces a sharper arithmetic selector and an order-one endpoint ray, but the complete actual edge spectrum still realizes that ray with bounded phase gaps and uniform positive amplitude. Any contradiction must still use **where the arithmetic CA maximizers land inside those windows**, a lower-order source coordinate, or recovery geometry not preserved by the leading edge almost-periodic model.

## 1. The edge-normalized block maximum has an exact moving tangent

Fix a finite positive CA block and let `C` be its rightmost maximizer of (4). With `q=B_Theta(C)`, maximality is equivalent on the block to

\[
h(D)\le \tau_q(X),
\qquad
X:=\log D,
\tag{16}
\]

where

\[
\boxed{
\tau_q(x):=
\log\!\left(1+\frac{q}{x^c\log x}\right).
}
\tag{17}
\]

Equality holds at `C`. At either immediate CA neighbor outside the positive block one has `h<=0<tau_q`, so `C` is also a local CA maximum of

\[
h(D)-\tau_q(\log D).
\tag{18}
\]

Put

\[
r(x):=\frac{q}{x^c\log x},
\qquad
a_x:=\frac{r(x)}{1+r(x)}.
\tag{19}
\]

Then

\[
\frac{r'(x)}{r(x)}
=-\frac1x\left(c+\frac1{\log x}\right)
\tag{20}
\]

and hence

\[
\boxed{
\tau_q'(x)
=-\frac{a_x}{x}
\left(c+\frac1{\log x}\right).
}
\tag{21}
\]

At `x=Y`, `a_Y=a(C)`. Therefore, for

\[
H_q(x):=\log\log x+\tau_q(x),
\tag{22}
\]

we obtain the exact derivative

\[
\boxed{
H_q'(Y)
=g(Y)-\frac{b_Ya(C)}Y,
\qquad
g(x):=\frac1{x\log x},
\qquad b_Y=c+\frac1{\log Y}.
}
\tag{23}
\]

The strict-concavity argument of `RE-034`--`RE-040` is uniform for this moving barrier. Indeed

\[
a_x'=-a_x(1-a_x)\frac1x
\left(c+\frac1{\log x}\right),
\tag{24}
\]

so on an `O(log Y)` CA-neighbor interval

\[
\tau_q''(x)=O\!\left(\frac{e^{h(C)}-1}{Y^2}\right).
\tag{25}
\]

The global positive-CA estimate from `RE-034`,

\[
h(C)\log Y\to0,
\tag{26}
\]

therefore gives

\[
\frac{\tau_q''(x)}{|(\log\log x)''|}
=O\bigl((e^{h(C)}-1)\log Y\bigr)
=o(1).
\tag{27}
\]

Consecutive CA neighbors are at logarithmic distance `O(log Y)` by the same Alaoglu--Erdos/event-location argument used in `RE-034`. Hence `H_q` is eventually strictly concave throughout the needed neighboring interval. If `epsilon_-(C)` and `epsilon_+(C)` are the adjacent CA supporting slopes, local maximality gives

\[
\varepsilon_+(C)
<H_q'(Y)
<\varepsilon_-(C).
\tag{28}
\]

Because `b_Ya(C)log Y=o(1)`, the middle term in (28) is positive and smaller than `g(Y)`. Since `g` is strictly decreasing, there is a unique `Z>Y` satisfying (6), and the CA support interval says exactly that the event selector at `Z` chooses `C`. Thus `Y=Phi(Z)`.

This proves the first part of the claim without assuming (8) or any zero formula. The logarithmic factor in (4) is not heuristic decoration: differentiating it produces precisely the endpoint-approaching correction `1/log Y` in (6).

## 2. Nondegenerate edge-normalized maxima live at the full edge scale

Assume now (8). Since `e^h-1=h(1+o(1))`,

\[
q
=h(C)Y^c\log Y\,(1+o(1)).
\tag{29}
\]

The mean-value argument of `RE-034`, applied to (6), yields

\[
Z-Y
=(b_Y+o(1))h(C)Y\log Y.
\tag{30}
\]

The lower bound `q>>1` and (29) imply

\[
Z-Y\gg Y^{1-c}=Y^\Theta.
\tag{31}
\]

Because `Theta>1/2`, this dominates the deterministic higher-layer and endpoint corrections

\[
\Phi_{\ge2}(Z)=O(\sqrt{Z\log Z}),
\qquad
\delta_\vartheta(Z)=O(\log Z).
\tag{32}
\]

Using `Y=Phi(Z)` as in `RE-034`, we therefore get

\[
\boxed{
Z-\vartheta(Z)
=(b_Y+o(1))h(C)Z\log Z.
}
\tag{33}
\]

The finite-edge projection of `RE-113` gives

\[
Z-\vartheta(Z)
=Z^\Theta\bigl(F_\Theta(\log Z)+o(1)\bigr).
\tag{34}
\]

Combining (29)--(34), using `Z/Y->1`, yields

\[
F_\Theta(\log Z)+o(1)
=(b_Y+o(1))q.
\tag{35}
\]

Since `F_Theta` is bounded and `b_Y->c>0`, equation (35) first forces

\[
\boxed{q=O(1).}
\tag{36}
\]

Together with (8), `q asy 1`. Uniform continuity of `F_Theta` and `log Z-log Y->0` then sharpen (35) to

\[
\boxed{F_\Theta(\log Y)=c q+o(1).}
\tag{37}
\]

Thus any useful edge-normalized maximum automatically has exactly the order-one amplitude for which (4) was designed; an unbounded overshoot is excluded by the bounded actual edge profile.

## 3. The reciprocal coordinate lands on the endpoint ray

The exponent tail for a regular CA selector is, from `RE-034`,

\[
T(C)=O(Z^{-1/2}).
\tag{38}
\]

By (8), (29), and `c<1/2`,

\[
T(C)=o(h(C)).
\tag{39}
\]

The exact Euler-product accounting of `RE-034` is

\[
h(C)
=E(Z)-\delta_\ell(Z)-T(C)
+\log\frac{\log Z}{\log Y},
\qquad
\delta_\ell(Z)=O(Z^{-1}).
\tag{40}
\]

Equation (30) gives

\[
\log\frac{\log Z}{\log Y}
=(b_Y+o(1))h(C)
=(c+o(1))h(C).
\tag{41}
\]

Hence

\[
\boxed{E(Z)=(\Theta+o(1))h(C).}
\tag{42}
\]

`RE-114` supplies the actual edge projection

\[
E(Z)
=\frac{Z^{\Theta-1}}{\log Z}
\bigl(G_\Theta(\log Z)+o(1)\bigr).
\tag{43}
\]

Multiplying (42) by `Z^c log Z`, using `q asy 1`, `Z/Y->1`, and uniform continuity of `G_Theta`, proves

\[
\boxed{G_\Theta(\log Y)=\Theta q+o(1).}
\tag{44}
\]

Equations (37) and (44) are (9), and their ratio gives (10).

The exact finite-`Y` slope carried by the tangent is already the moving ray associated with `b_Y`; (37)--(44) state its limiting endpoint form. The extra `1/log Y` in `b_Y` is lower order in the edge projection but is essential in the exact variational derivative.

## 4. Near-minimal recovery forces the nondegenerate endpoint selector

Take an unbounded fixed-constant near-minimal recovery family from `RE-113`. Its selected fixed-`b` states `C_0` satisfy

\[
\lambda_{Y_0}
:=h(C_0)Y_0^c\log Y_0
\asymp1.
\tag{45}
\]

Because `h(C_0)->0`,

\[
B_\Theta(C_0)
=Y_0^c\log Y_0\,(e^{h(C_0)}-1)
=\lambda_{Y_0}(1+o(1))
\asymp1.
\tag{46}
\]

Let `C` be the rightmost `B_Theta` maximizer on the same positive block. Then

\[
q=B_\Theta(C)\ge B_\Theta(C_0)\gg1.
\tag{47}
\]

The positive blocks in the family escape to infinity, so the selected `C` also form an unbounded sequence. Sections 1--3 therefore apply and show that every surviving near-minimal family forces a genuine edge-normalized selector sequence satisfying the endpoint phase lock (9).

No claim is made that the new `B_Theta` maximizer has the same recovery length as `C_0`; that is not needed. The point is a necessary blockwise consequence: if the near-minimal branch survives, each of its blocks contains an order-one endpoint-normalized maximum with exact CA tangent geometry.

## 5. The actual edge face realizes all nearby rays uniformly

It remains to test whether approaching `b=c` changes the spectral compatibility result of `RE-114`. It does not.

Use the stable-filter state from `RE-114`,

\[
J_\Theta(u)
:=
\int_0^\infty e^{-cs}F_\Theta(u+s)\,ds,
\qquad
G_\Theta=J_\Theta-F_\Theta,
\tag{48}
\]

which obeys

\[
J_\Theta'(u)=cJ_\Theta(u)-F_\Theta(u).
\tag{49}
\]

For any `b`, define

\[
K_b(u):=bG_\Theta(u)-(1-b)F_\Theta(u).
\tag{50}
\]

Then exactly

\[
\boxed{
K_b(u)
=J_\Theta'(u)+(b-c)J_\Theta(u)
=bJ_\Theta(u)-F_\Theta(u).
}
\tag{51}
\]

At the endpoint,

\[
\boxed{K_c(u)=J_\Theta'(u).}
\tag{52}
\]

The attained edge makes `J_Theta` nonzero. It has zero Bohr mean, hence both signs. As in `RE-114`, choose a bounded positive connected component `(a,d)` of `J_Theta`. There exist points

\[
a<u_-<u_+<d
\tag{53}
\]

and constants `alpha,m,M>0` such that

\[
J_\Theta'(u_-)\ge\alpha,
\qquad
J_\Theta'(u_+)\le-\alpha,
\tag{54}
\]

\[
J_\Theta(u)\ge m
\quad(u\in[u_-,u_+]),
\qquad
|J_\Theta(u)|\le M
\quad(u\in\mathbb R).
\tag{55}
\]

Choose

\[
0<\delta<\min\left\{
\frac12-c,
\frac{\alpha}{2M}
\right\}.
\tag{56}
\]

For every `b in [c,c+delta]`, equations (51), (54), and (55) give fixed opposite endpoint signs,

\[
K_b(u_-)>0,
\qquad
K_b(u_+)<0,
\tag{57}
\]

with margins bounded away from zero uniformly in `b`.

The pair `(J_Theta,F_Theta)` is uniformly almost periodic by the absolutely convergent edge expansions already established in `RE-114`. Choose a common approximate-period tolerance small enough to preserve half of the positive `J_Theta` margin in (55) and the uniform sign margins in (57). Such common approximate periods are relatively dense. Translating `[u_-,u_+]` by them and applying the intermediate value theorem gives constants `L<infinity` and `m_0>0`, independent of `b`, such that every interval of length `L` contains a point `u` with

\[
K_b(u)=0,
\qquad
J_\Theta(u)\ge m_0.
\tag{58}
\]

At such a zero, (50) and `G=J-F` give exactly

\[
F_\Theta(u)=bJ_\Theta(u),
\qquad
G_\Theta(u)=(1-b)J_\Theta(u).
\tag{59}
\]

Since `b>=c>0` and `1-b>=1-c-delta>0`, (59) yields one uniform `eta>0` and proves (15).

This strengthens `RE-114` in the only direction relevant to an endpoint-moving selector: its constants need not degenerate as `b downarrow 1-Theta`. The exact endpoint is not exceptional. It is the stationary-point case `J_Theta'=0` of the same stable-filter geometry.

## 6. Stress tests, prior art, and research consequence

Several boundaries are load-bearing.

First, `Theta>1/2` is needed twice: it makes `c<1/2`, so the moving exponent eventually remains in the adaptive range, and it makes the order-`Y^Theta` tangent displacement dominate the deterministic square-root CA corrections. Second, (8) is required for the endpoint-scale source law; without a nondegenerate edge-normalized amplitude, the exponent tail need not be `o(h)` and no order-one edge ray is asserted. For the live fixed-constant near-minimal branch, however, (8) follows from `RE-113` by the blockwise maximum argument in Section 4. Third, edge attainment is essential for the spectral compatibility statement: if the edge is not attained, `RE-113` already eliminates the fixed-constant near-minimal family and `J_Theta` is zero.

The endpoint theorem does not claim that a fixed-power Robin theorem is valid at `b=c`. Robin's quantitative false-RH result remains used only for fixed `b>c`. The new functional (4) is selected **inside blocks already forced by the existing argument**; it does not smuggle in an endpoint quantitative theorem. This distinction prevents the logarithmic retuning from silently assuming the conclusion it is meant to test.

The almost-periodic ingredients are classical. Bohr relative density of common approximate periods and the standard zero-expansion coefficients are not claimed as new. The current literature audit across Robin/CA extremal work, Mertens--Chebyshev joint errors, and almost-periodic prime-error frameworks located no source coupling the log-corrected edge amplitude (4) to the exact CA support derivative (6), nor a uniform-through-endpoint version of the adaptive mixed-ray compatibility (15). Robin, Alaoglu--Erdos, Mantovanelli, Lamzouri, and Bhattacharya--Martin--Simpson already bound the surrounding ingredients in `SOURCES.md`; no new external theorem is load-bearing here, so that file needs no change.

A one-conjugate-pair edge is a matched control. Then `J_Theta` is a single sinusoid, its positive stationary points recur periodically, and (52), (59) realize the endpoint ray explicitly. The full proof shows that an arbitrary attained edge face with the summability established in `RE-113` retains the same qualitative obstruction uniformly for `b` approaching `c`.

The research consequence is negative but sharp. A natural attempt to exploit the scale mismatch left by fixed `b>1-Theta` is to normalize the Robin excess at the actual edge scale `Y^(Theta-1)/log Y`. That attempt produces genuine new arithmetic structure -- the exact moving tangent `b_Y=c+1/log Y` -- but **not a spectral contradiction**. The edge face supplies uniform order-one compatible windows all the way to the endpoint. The unresolved information is therefore not the choice of threshold exponent. It is the arithmetic placement of these edge-normalized CA maxima inside the compatible windows, a lower-order source term, or a recovery constraint that survives the leading-edge almost-periodic control.