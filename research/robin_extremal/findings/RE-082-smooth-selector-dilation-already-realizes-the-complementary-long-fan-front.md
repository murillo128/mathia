# RE-082 — smooth selector dilation already realizes the complementary long-fan front

**Status:** `EXACT-SETUP + ASYMPTOTIC-DERIVED + COMMON-AMPLITUDE-CONTROL + SELECTOR-DILATION-DENSITY + LONG-STRETCH-FRONT-REALIZATION + NEGATIVE/ROUTE-NARROWING + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-081` removes the discrete higher-layer atoms from the leading long-fan transport and leaves the continuous selector-dilation measure `mu_dil` as the carrier of both corrected Lyapunov moments. A natural next attack is therefore to hope that the smooth dilation geometry itself is too rigid to realize the complementary power front of `RE-080`.

That hope fails at the level of the common-amplitude differential law. The exact selector interpolation already used in `RE-070`, `RE-076`, and `RE-079` has a regularly varying dilation density whose two natural moments separate at exactly the exponent `1-b`.

Fix

\[
0<b<\frac12,
\]

and let

\[
T_0\to\infty,
\qquad
T_1=T_0r,
\qquad
r\to\infty.
\]

Let `c=c(T_0)>0` satisfy the late small-height condition

\[
\boxed{
cT_0^{-b}\log T_0\longrightarrow0.}
\tag{1}
\]

Define the same common-amplitude selector arc as in the genuine tied-switch analysis,

\[
a_c(t):=\frac{ct^{-b}}{1+ct^{-b}},
\qquad
g(x):=\frac1{x\log x},
\]

\[
\boxed{
g(Z_c(t))=g(t)-\frac{b\,a_c(t)}t,}
\tag{2}
\]

and put

\[
D_c(t):=Z_c(t)-t.
\]

On `[T_0,T_1]`, condition (1) is uniform because `t^{-b} log t` is eventually decreasing. The selector is therefore well defined, `Z_c(t)/t -> 1` uniformly, and the expansion already derived in `RE-070` gives

\[
\boxed{
D_c'(t)
=b(1-b)c\,t^{-b}\log t\,(1+o(1))
}
\tag{3}
\]

uniformly on the whole long arc.

Let `nu_c` be the smooth dilation measure obtained by pushing `dD_c(t)` to selector coordinate `s=Z_c(t)`. Then `nu_c` is absolutely continuous and

\[
\boxed{
\frac{d\nu_c}{ds}(s)
=b(1-b)c\,s^{-b}\log s\,(1+o(1)).
}
\tag{4}
\]

If

\[
M_c:=\nu_c([Z_c(T_0),Z_c(T_1)])
\]

and

\[
W_c:=\int\frac{d\nu_c(s)}{s\log s},
\]

then

\[
\boxed{
M_c
=bc\,T_1^{1-b}\log T_1\,(1+o(1)),
}
\tag{5}
\]

while

\[
\boxed{
W_c
=(1-b)c\,T_0^{-b}\,(1+o(1)).
}
\tag{6}
\]

Hence

\[
\boxed{
\frac{W_c}{M_c}
=
\frac{1-b}{b}
\frac{1+o(1)}{T_0^bT_1^{1-b}\log T_1}.
}
\tag{7}
\]

If `Z_eff,c` is defined by

\[
g(Z_{\rm eff,c})=\frac{W_c}{M_c},
\]

then

\[
\boxed{
\frac{\log(Z_{\rm eff,c}/T_0)}{\log r}
=1-b+o(1).
}
\tag{8}
\]

Thus the complementary exponent `1-b` appearing in `RE-080` is not merely compatible with an arbitrary positive measure. It is the native effective-selector exponent of the **same smooth common-amplitude dilation law from which the actual fan transport is built**.

The match is stronger than the barycenter. For fixed `0<alpha<1`, put

\[
t_\alpha:=T_0r^\alpha,
\qquad
s_\alpha:=Z_c(t_\alpha).
\]

Then

\[
\boxed{
\frac{\nu_c([Z_c(T_0),s_\alpha])}{M_c}
=r^{-(1-\alpha)(1-b)+o(1)},
}
\tag{9}
\]

and

\[
\boxed{
\frac{
\displaystyle\int_{[s_\alpha,Z_c(T_1)]}
\frac{d\nu_c(s)}{s\log s}
}{W_c}
=r^{-\alpha b+o(1)}.
}
\tag{10}
\]

At the crossover `alpha=1-b`, both unwanted tails are already polynomially small,

\[
\boxed{
r^{-b(1-b)+o(1)}.}
\tag{11}
\]

So the two one-sided fronts of `RE-080` are not fighting the local selector-dilation geometry. In a narrow threshold band around `b`, the smooth law produces exactly the required power front; for a wider band `J=[b_0,b_1]`, every fixed `b in J` places its crossover exponent `1-b` inside the permitted interval `[1-b_1,1-b_0]`.

This is a **negative control**, not an arithmetic realization of a false-RH CA fan. A single formal common-amplitude arc need not coincide with the actual sequence of exposed integer CA states over a long stretch. What it proves is narrower and strategically important: positivity, absolute continuity, the exact `g`-duality, the common-amplitude selector ODE, and its late density asymptotic cannot by themselves exclude the `RE-080` front. A contradiction must use the way genuine CA states splice these arcs and fixed-state cells through the ordinary-prime-supported staircase — for example the support-slope capacity budget of `RE-040`, exact first-layer prime-set conservation where applicable, or a source estimate controlling how much long selector dilation can be assembled from actual CA transitions.

## 1. The pushforward density is explicit

`RE-070` derives uniformly along a late common-amplitude segment

\[
\frac{D_c(t)}t
=b\,a_c(t)\log t\,(1+o(1))
\tag{12}
\]

and

\[
D_c'(t)
=b(1-b)a_c(t)\log t\,(1+o(1)).
\tag{13}
\]

Condition (1) gives `ct^{-b}=o(1)` uniformly for `t>=T_0`, hence

\[
a_c(t)=ct^{-b}(1+o(1)).
\tag{14}
\]

Equations (13)--(14) give (3). They also imply `D_c'(t)=o(1)` uniformly. Since

\[
s=Z_c(t)=t+D_c(t),
\qquad
ds=(1+D_c'(t))dt,
\]

pushing forward `dD_c=D_c'(t)dt` yields

\[
\frac{d\nu_c}{ds}
=
\frac{D_c'(t)}{1+D_c'(t)}.
\tag{15}
\]

Using `Z_c(t)/t -> 1`, equations (3) and (15) give (4). In particular, the continuous fan transport is not allowed to be a point mass, but this regularization does not obstruct the moving front: its natural density already has the right regularly varying shape.

## 2. Its two moments are controlled by opposite endpoints

Because `nu_c` is the pushed-forward increment of `D_c`,

\[
M_c=D_c(T_1)-D_c(T_0).
\tag{16}
\]

From (12)--(14),

\[
D_c(t)=bc\,t^{1-b}\log t\,(1+o(1)).
\tag{17}
\]

Since `r=T_1/T_0 -> infinity` and `1-b>0`, the lower endpoint is negligible relative to the upper one, proving (5).

For the weighted moment, use selector coordinate or pull back to `t`:

\[
W_c
=
\int_{T_0}^{T_1}g(Z_c(t))D_c'(t)\,dt.
\tag{18}
\]

Uniformly, `Z_c(t)/t -> 1`, so

\[
g(Z_c(t))
=\frac{1+o(1)}{t\log t}.
\tag{19}
\]

Combining (3) and (19),

\[
W_c
=b(1-b)c(1+o(1))
\int_{T_0}^{T_1}t^{-b-1}\,dt.
\]

The integral is

\[
\frac1b(T_0^{-b}-T_1^{-b}),
\]

and `r -> infinity`, giving (6). Thus the unweighted moment is asymptotically an **upper-endpoint** quantity while the Robin-kernel moment is a **lower-endpoint** quantity. This is exactly the endpoint-decoupling mechanism that drives `RE-080`, now reproduced inside one smooth selector law.

Dividing (6) by (5) gives (7). Since `g` is strictly decreasing, `Z_eff,c` is unique. Equation (7) is equivalent to

\[
Z_{\rm eff,c}\log Z_{\rm eff,c}
=
\left(\frac{b}{1-b}+o(1)\right)
T_0^bT_1^{1-b}\log T_1.
\tag{20}
\]

The logarithm of the factor multiplying `T_0^bT_1^{1-b}` is `o(log r)`, so (8) follows.

## 3. The full front profile follows from regular variation

For `t_alpha=T_0r^alpha`, equation (17) gives

\[
\frac{D_c(t_\alpha)-D_c(T_0)}
{D_c(T_1)-D_c(T_0)}
=
r^{-(1-\alpha)(1-b)+o(1)},
\]

which is (9). No density estimate beyond the same exact selector expansion is needed.

Similarly, applying (18)--(19) on `[t_alpha,T_1]` gives

\[
\int_{[s_\alpha,Z_c(T_1)]}g\,d\nu_c
=(1-b)c\,t_\alpha^{-b}(1+o(1)),
\]

because `T_1^{-b}=o(t_alpha^{-b})`. Division by (6) gives (10).

At `alpha=1-b`, both exponents in (9)--(10) equal `b(1-b)`, proving (11). This is the sharpest falsification test for a density-only attack on `RE-081`: the smooth law does not merely place its kernel barycenter at the correct exponent; it places asymptotically almost all unweighted mass to its right and almost all weighted mass to its left.

## 4. Boundary controls and what this does not prove

The control is deliberately **not** claimed to be a genuine long tied switch between actual CA endpoints. The common-amplitude curve is an exact analytic interpolation used to compare tied fan states; extending it over `[T_0,T_1]` preserves the same local selector equation but does not impose the integer event staircase, CA supporting-slope admissibility at every intermediate point, or exact ordinary-prime labels. Those omitted conditions are precisely where any successful arithmetic obstruction must now enter.

The condition `r -> infinity` is load-bearing. For bounded stretch, neither endpoint dominates its corresponding moment and `RE-079` already gives the correct bounded-dilation description. The condition `b>0` is also needed for the weighted integral to be lower-endpoint dominated; the Mathia false-RH fan has `b in J subset (1-Theta,1/2)`, so this is automatic.

The small-height condition (1) is not an extra favorable assumption invented for the control. It is exactly the regime used in the genuine late fan: `RE-040` proves `h log Y -> 0` uniformly, and on a tied common-amplitude curve `ct^{-b}=e^{h(t)}-1`, so `ct^{-b} log t -> 0`. The false-RH lower amplitude `c>=c_0` is compatible with (1), but the moment ratio (7) does not need it because `c` cancels.

A lower density bound of the form `dmu_dil/ds >= const * s^(-b_1) log s`, obtainable from the false-RH amplitude floor on genuine switch arcs, therefore cannot by itself contradict `RE-080`; the model density (4) is of exactly that scale and realizes the front. Likewise the elementary upper bound `dmu_dil/ds<=1`, coming from `D_c'>0`, is far too weak. The missing information is not regularity of the continuous measure but its **assembly from actual CA cells and admissible transition spans**.

## 5. Prior-art boundary and next target

The asymptotic integrations in (5)--(10) are elementary. Alaoglu--Erdos and Robin provide the classical CA variational background, Musin bounds the convex-envelope prior-art boundary, and Mantovanelli's August 2026 preprint develops the discrete prime-layer event workload and its Robin-kernel moment structure. A directed current search found no external statement of the adaptive common-amplitude selector-dilation density (4), nor the observation that this smooth law by itself produces the complementary effective exponent `1-b` and both long-fan fronts. No external theorem is load-bearing here beyond sources already anchored in `SOURCES.md`, so that file requires no change.

The long-stretch target after `RE-081` is therefore more specific than “show that a continuous measure cannot realize the front.” It can. The next useful theorem has to constrain how the **genuine CA staircase assembles** selector dilation: how much threshold-cell width is spent in fixed-state pieces, how large the admissible tied spans can be under the adjacent supporting slopes, or how ordinary-prime first-layer conservation limits repeated realization of the smooth `s^(-b) log s` profile. A contradiction, if available, must live in that discrete assembly layer rather than in the continuous transport kernel itself.