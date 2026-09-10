# RE-033 — arbitrary finite zero packets cannot obstruct the threshold race cone

**Status:** `EXACT-DERIVED + FINITE-SPECTRAL-DICHOTOMY + NEGATIVE/OBSTRUCTION + MULTI-REAL-PART-CONE-COMPATIBILITY + PRIOR-ART-ALIGNED`. `RE-029` forces a hypothetical quantitative Robin witness into an opposite-sign Chebyshev/Mertens cone at one common threshold-tangent event parameter. `RE-030` shows that one off-critical zero pair is compatible with that cone, and `RE-032` extends compatibility to every finite packet whose zeros share one real part. The common-real-part restriction is not a genuine finite-spectrum escape: **every finite packet of zero modes, with arbitrarily many distinct real parts, is either asymptotically too small to affect the `RE-029` threshold scale or has infinitely many points realizing the required negative standard coordinate while the reciprocal coordinate stays positive at the packet's full rightmost power scale.**

Fix

\[
0<b<\frac12,
\qquad
d:=\frac12-b>0,
\tag{1}
\]

and let `P` be a nonempty finite packet

\[
\rho_j=\beta_j+i\gamma_j,
\qquad
0<\beta_j<1,
\qquad
\gamma_j>0,
\qquad
1\le j\le m,
\tag{2}
\]

with positive integer multiplicities `nu_j`. After pairing with the conjugates, define the standard and reciprocal normalized packet profiles

\[
\Theta_P(x)
:=-2\Re\sum_{j=1}^m
\frac{\nu_j x^{\rho_j-1/2}}{\rho_j},
\tag{3}
\]

\[
L_P(x)
:=-2\Re\sum_{j=1}^m
\frac{\nu_j x^{\rho_j-1/2}}{\rho_j-1}.
\tag{4}
\]

These are the same per-zero coefficient profiles used in `RE-030`--`RE-032`. Put

\[
\beta_*:=\max_j\beta_j,
\qquad
a_*:=\beta_*-\frac12.
\tag{5}
\]

Then exactly one of the following two regimes holds.

### Threshold-invisible regime

If

\[
\beta_*\le1-b,
\tag{6}
\]

then

\[
\boxed{
\Theta_P(x)=O_P(x^d),
\qquad
L_P(x)=O_P(x^d),
}
\tag{7}
\]

and therefore

\[
\boxed{
\frac{\Theta_P(x)}{x^d\log x}\to0,
\qquad
\frac{L_P(x)}{x^d\log x}\to0.
}
\tag{8}
\]

A finite packet whose rightmost zero lies on or to the left of `Re(s)=1-b` cannot supply, cancel, or obstruct a leading term of the `RE-029` size `x^d log x`.

### Cone-compatible regime

If

\[
\beta_*>1-b,
\tag{9}
\]

put

\[
\delta:=\beta_*+b-1=a_*-d>0.
\tag{10}
\]

Then there is a constant `eta_P>0` such that, for every `A>0`, an unbounded sequence `x_k` satisfies

\[
\boxed{
\Theta_P(x_k)=-A x_k^d\log x_k,
}
\tag{11}
\]

while simultaneously

\[
\boxed{
L_P(x_k)\ge\eta_P x_k^{a_*}>0.
}
\tag{12}
\]

Consequently

\[
\boxed{
\frac{L_P(x_k)}{x_k^d\log x_k}
\ge
\eta_P\frac{x_k^\delta}{\log x_k}
\longrightarrow+\infty.
}
\tag{13}
\]

Taking `A=b c_b`, where `c_b` is the quantitative Robin constant of `RE-027`--`RE-029`, makes (11) exactly the standard-error magnitude forced by `RE-029`; (13) then exceeds its required positive reciprocal lower bound by an unbounded factor.

Thus **no finite zero packet has a coefficient-geometry obstruction to the threshold cone**. It is either below the threshold resolution or explicitly cone-compatible. Any spectral obstruction must therefore use information not present in a fixed finite packet: the arithmetic placement of the CA selector, a nonuniform/infinite explicit-formula tail, or another source relation tying those two objects together.

## 1. Packets left of `Re(s)=1-b` are logarithmically below threshold

Because `P` is finite, the coefficients in (3)--(4) are fixed constants. Hence

\[
|\Theta_P(x)|+|L_P(x)|
\ll_P x^{a_*}.
\tag{14}
\]

Under (6), `a_*<=d`, so (7) follows. Division by the extra `log x` in the `RE-029` scale proves (8), including the boundary case `beta_*=1-b`.

This gives an exact threshold line for finite spectral controls. A mode at `Re(rho)=1-b` has normalized size `x^d`, not `x^d log x`; the logarithm in Robin's quantitative selector still separates it from the required leading excursion.

## 2. Split an arbitrary finite packet into its rightmost face and decaying lower faces

Assume (9). Let `P_*` be the nonempty subpacket with `beta_j=beta_*`. Write `u=log x` and factor out the common rightmost power `x^{a_*}`. Define

\[
S_*(u)
:=-2\Re\sum_{\beta_j=\beta_*}
\frac{\nu_j e^{i\gamma_j u}}{\rho_j},
\qquad
R_*(u)
:=-2\Re\sum_{\beta_j=\beta_*}
\frac{\nu_j e^{i\gamma_j u}}{\rho_j-1}.
\tag{15}
\]

For the lower faces put

\[
H_S(u)
:=-2\Re\sum_{\beta_j<\beta_*}
\frac{\nu_j e^{-(\beta_*-\beta_j)u}e^{i\gamma_j u}}{\rho_j},
\tag{16}
\]

\[
H_R(u)
:=-2\Re\sum_{\beta_j<\beta_*}
\frac{\nu_j e^{-(\beta_*-\beta_j)u}e^{i\gamma_j u}}{\rho_j-1}.
\tag{17}
\]

Then exactly

\[
x^{-a_*}\Theta_P(x)=S_*(u)+H_S(u),
\qquad
x^{-a_*}L_P(x)=R_*(u)+H_R(u).
\tag{18}
\]

If lower faces are present, finiteness gives a positive spectral gap

\[
\kappa
:=\min_{\beta_j<\beta_*}(\beta_*-\beta_j)>0,
\tag{19}
\]

and therefore

\[
\boxed{
H_S(u)=O_P(e^{-\kappa u}),
\qquad
H_R(u)=O_P(e^{-\kappa u}).
}
\tag{20}
\]

The important point is what (20) is and is not used for. A lower face with `beta_j>1-b` can be much larger than the tiny target level `u e^{-delta u}` after rightmost normalization. We do **not** discard it relative to that target. We use only that every lower face tends to zero relative to the order-one rightmost-face crossing geometry.

## 3. `RE-032` supplies a robust reciprocal-positive crossing window on the rightmost face

The rightmost face `P_*` satisfies the hypotheses of `RE-032`: it is a finite nonzero packet on one vertical line `Re(s)=beta_*`. The proof there gives more than isolated cone points. It supplies a fixed compact interval `I=[v-r,v+r]`, constants `m,eta>0`, and unbounded recurrence shifts `tau_k` such that for all sufficiently large `k`,

\[
S_*(v-r+\tau_k)>m,
\qquad
S_*(v+r+\tau_k)<-m,
\tag{21}
\]

and

\[
R_*(u)>2\eta
\qquad
(u\in I+\tau_k).
\tag{22}
\]

No recurrence of the lower faces is required. By (20), after increasing `k` if necessary,

\[
|H_S(u)|<\frac m4,
\qquad
|H_R(u)|<\eta
\qquad
(u\in I+\tau_k).
\tag{23}
\]

Hence the **full** normalized packet still has opposite signs at the two endpoints,

\[
S_*(v-r+\tau_k)+H_S(v-r+\tau_k)>\frac{3m}{4},
\tag{24}
\]

\[
S_*(v+r+\tau_k)+H_S(v+r+\tau_k)<-\frac{3m}{4},
\tag{25}
\]

while throughout the entire window

\[
\boxed{
R_*(u)+H_R(u)>\eta.
}
\tag{26}
\]

This is the step that removes the common-real-part restriction. Lower faces may shift the location of the standard zero by much more than the eventual Robin threshold level, but they cannot remove a robust sign-changing window or consume the fixed positive reciprocal margin once their amplitude is small relative to the rightmost face.

## 4. The full packet hits the exact Robin threshold level inside those windows

Set

\[
q(u):=Aue^{-\delta u},
\tag{27}
\]

with `A>0` arbitrary and `delta` from (10). Since `delta>0`, `q(u)>0` and `q(u)->0`. On every sufficiently late recurrent window,

\[
q(u)<\frac m4.
\tag{28}
\]

Define

\[
F(u):=S_*(u)+H_S(u)+q(u).
\tag{29}
\]

Equations (24)--(25) and (28) give opposite signs for `F` at the two endpoints of `I+tau_k`. The intermediate value theorem therefore gives `u_k` in that window with

\[
S_*(u_k)+H_S(u_k)
=-A u_k e^{-\delta u_k}.
\tag{30}
\]

At the same point, (26) gives

\[
R_*(u_k)+H_R(u_k)>\eta.
\tag{31}
\]

Put `x_k=e^{u_k}`. Since `a_*-delta=d`, multiplying (30) by `x_k^{a_*}` proves (11), while multiplying (31) proves (12) with `eta_P=eta`. The recurrence shifts are unbounded, so `x_k->infinity`.

The proof is deliberately topological at threshold resolution. It does not need a quantitative estimate for how far the lower faces move the crossing. This is why lower modes that are larger than `x^d log x` can still be harmless to the **existence** of cone-compatible points: they perturb a robust order-one sign change and vanish relative to that geometry.

## 5. False-RH specialization isolates the only finite-spectrum alternatives

Assume the false-RH setting of `RE-027`--`RE-029`, with

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12.
\tag{32}
\]

For any fixed

\[
0<\varepsilon<\Theta-\frac12,
\tag{33}
\]

choose

\[
b=1-\Theta+\varepsilon,
\qquad
d=\Theta-\frac12-\varepsilon.
\tag{34}
\]

Then the finite-packet threshold line is

\[
1-b=\Theta-\varepsilon.
\tag{35}
\]

Every finite packet whose zeros all satisfy `Re(rho)<=Theta-epsilon` is `o(x^d log x)` in both normalized coordinates. Every finite packet containing at least one zero with `Re(rho)>Theta-epsilon` has a rightmost member `beta_*>1-b` and is cone-compatible by (11)--(13).

Thus, at the exact power scale forced by Robin's quantitative selector, **there is no third finite-packet regime**. A contradiction cannot be obtained merely by taking more finitely many zeros, allowing several real parts, or adding any finite amount of lower spectral clutter to the `RE-032` control.

This does not say that an actual zeta explicit formula can be replaced by one finite packet. If `Theta` is not attained, if zeros approach the right edge through infinitely many real parts, or if the truncation remainder is not uniform at the `x^d log x` scale, the omitted spectrum can remain load-bearing. Those are precisely infinite/nonuniform effects rather than finite coefficient geometry.

## 6. Stress tests and boundary conditions

The packet is a **spectral control**, not an admissible prime sequence and not a theorem that the actual Chebyshev and Mertens errors visit the constructed points. The `x_k` come from recurrence of the packet's rightmost face; no claim is made that the threshold-tangent CA selector of `RE-027` visits those windows. Selector avoidance therefore remains a fully viable closing mechanism.

The finiteness hypothesis is essential to (19)--(20). For infinitely many real parts accumulating at `beta_*`, or when the supremum is not attained, there need be no positive decay gap. Even with one attained rightmost face, an infinite tail can fail to be uniformly negligible on the recurrent windows unless an explicit truncation theorem controls it. `RE-031` already shows that the accuracy required to combine spectral approximation with fine CA event spacing can be power-sensitive.

The boundary `beta_*=1-b` is included in the invisible regime because the forced Robin scale has the extra factor `log x`. There is no hidden equality case in which a fixed finite coefficient can recover that logarithm.

Multiplicity is harmless and is absorbed into `nu_j`. Rational relations among rightmost ordinates are also harmless because `RE-032` uses finite-frequency recurrence without LI. Lower-face phases need no simultaneous recurrence at all.

The reciprocal coefficient model (4) is the same one already audited in `RE-030`: its line-local tail transform gives the `rho -> rho-1` leading response, with lower-order `1/log x` corrections for each fixed mode. For a finite packet in the compatible regime, such corrections are `o_P(x^{a_*})` and cannot reverse the positive full-power margin in (12). This observation does not control the omitted infinite zero sum.

## 7. Prior art and research consequence

The explicit-formula coefficient `1/rho`, the reciprocal coefficient `1/(rho-1)`, and the correlation of standard and reciprocal weighted-prime errors are existing analytic-number-theory structure; Bhattacharya--Martin--Simpson remain the closest current source anchor in `SOURCES.md`. Dominance by a fixed rightmost exponential power, finite trigonometric recurrence, and stability of a sign-changing zero under a vanishing perturbation are elementary and are not claimed as new results in isolation.

A targeted search of current Robin/CA work and joint Chebyshev--Mertens error literature did not identify this Mathia-specific dichotomy at the moving Robin threshold `x^(1/2-b) log x`. The repository-level delta is the combination of the exact `RE-029` threshold scale with the robust crossing theorem of `RE-032`: it shows that the finite same-real-part limitation of `RE-032` is not an actual finite-spectrum loophole. No new load-bearing external theorem is introduced, so `SOURCES.md` does not require expansion.

The live source-side obstruction is therefore narrower. **Finite spectral coefficient geometry is exhausted as a route to contradiction.** A successful continuation must exploit the arithmetic sampling of the recurrent windows by the CA threshold selector, prove a sufficiently uniform theorem for the genuinely infinite/right-edge spectral tail, or identify a source constraint that couples those two. Merely enlarging a zero model from one mode to any fixed finite number of modes, even across multiple real parts, cannot close the Robin route.