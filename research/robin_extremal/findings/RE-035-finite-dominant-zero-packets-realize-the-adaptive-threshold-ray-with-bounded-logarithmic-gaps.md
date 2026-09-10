# RE-035 — finite dominant zero packets realize the adaptive threshold ray with bounded logarithmic gaps

**Status:** `EXACT-DERIVED + FINITE-SPECTRAL-CONTROL + ADAPTIVE-RAY-COMPATIBILITY + LOG-SYNDETIC-RECURRENCE + STABLE-UNDER-VANISHING-LOWER-TAIL + NEGATIVE/OBSTRUCTION + PRIOR-ART-ALIGNED`. `RE-034` sharpens the false-RH threshold reduction from the opposite-sign cone of `RE-029` to the exact asymptotic ray

\[
\frac{\mathcal E_{\pi_\ell}(Z)}{-\mathcal E_\vartheta(Z)}
\longrightarrow\frac{1-b}{b}.
\tag{1}
\]

A natural hope is that this extra equality might restore a coefficient-level obstruction that was absent for the weaker cone in `RE-030`--`RE-033`. It does not. **Every finite spectral packet with a rightmost zero strictly beyond the threshold line `Re(s)=1-b` has exact ray points recurring with bounded gaps in logarithmic phase, with the standard coordinate negative and the reciprocal coordinate positive at the packet's full rightmost power scale.** The conclusion remains true after adding any lower-order spectral remainder that vanishes relative to that rightmost scale.

Let `P` be a nonempty finite packet of conjugate-paired zero modes

\[
\rho_j=\beta_j+i\gamma_j,
\qquad
0<\beta_j<1,
\qquad
\gamma_j>0,
\tag{2}
\]

with positive integer multiplicities. Define, as in `RE-030`--`RE-033`,

\[
\Theta_P(x)
:=-2\Re\sum_j\frac{\nu_jx^{\rho_j-1/2}}{\rho_j},
\tag{3}
\]

\[
L_P(x)
:=-2\Re\sum_j\frac{\nu_jx^{\rho_j-1/2}}{\rho_j-1}.
\tag{4}
\]

Fix

\[
0<b<\frac12,
\qquad
\beta_*:=\max_j\beta_j,
\qquad
a_*:=\beta_*-\frac12.
\tag{5}
\]

If

\[
\beta_*\le1-b,
\tag{6}
\]

then `RE-033` already gives the threshold-invisible regime

\[
\Theta_P(x),L_P(x)=o(x^{1/2-b}\log x).
\tag{7}
\]

Assume instead

\[
\boxed{\beta_*>1-b.}
\tag{8}
\]

Then there are constants `eta>0`, `L<infinity`, and `u_0` such that every interval `[U,U+L]` with `U>=u_0`, after enlarging `L` once by a fixed packet-dependent amount, contains a point `u` for which, with `x=e^u`,

\[
\boxed{
bL_P(x)+(1-b)\Theta_P(x)=0,}
\tag{9}
\]

and simultaneously

\[
\boxed{
\Theta_P(x)\le-\eta x^{a_*},
\qquad
L_P(x)\ge\eta x^{a_*}.}
\tag{10}
\]

At every such point,

\[
\boxed{
\frac{L_P(x)}{-\Theta_P(x)}=\frac{1-b}{b}.}
\tag{11}
\]

Thus the exact `RE-034` slope is not a thin or exceptional relation for a finite dominant packet: its compatible points are **syndetic in `u=log x`**, equivalently they have bounded gaps on logarithmic scale.

## 1. On the rightmost face, the exact ray residual is one weighted derivative

Let `P_*` be the nonempty rightmost face `beta_j=beta_*`, put

\[
c:=1-\beta_*,
\tag{12}
\]

and write `u=log x`. Because of (8),

\[
0<c<b.
\tag{13}
\]

After factoring out `x^{a_*}`, define the finite trigonometric profiles

\[
S(u):=-2\Re\sum_{\beta_j=\beta_*}
\frac{\nu_je^{i\gamma_ju}}{\rho_j},
\tag{14}
\]

\[
R(u):=-2\Re\sum_{\beta_j=\beta_*}
\frac{\nu_je^{i\gamma_ju}}{\rho_j-1}.
\tag{15}
\]

`RE-032` derives the exact stable-filter relation

\[
J(u):=\int_0^\infty e^{-cs}S(u+s)\,ds,
\qquad
R(u)=S(u)-J(u),
\tag{16}
\]

and

\[
J'(u)=cJ(u)-S(u).
\tag{17}
\]

The `RE-034` ray residual for the rightmost face is

\[
K_b(u):=bR(u)+(1-b)S(u)=S(u)-bJ(u).
\tag{18}
\]

Put

\[
\lambda:=b-c>0.
\tag{19}
\]

Using (17),

\[
\boxed{
K_b(u)=-(J'(u)+\lambda J(u))
=-e^{-\lambda u}\frac d{du}\bigl(e^{\lambda u}J(u)\bigr).
}
\tag{20}
\]

This identity is the key difference from merely asking whether the two packet coordinates can have opposite signs. The exact slope `(1-b)/b` converts into a stationary-point condition for an exponentially weighted stable-filter state.

## 2. Every nonzero rightmost face has a sign-correct exact ray crossing

The finite trigonometric polynomial `J` is nonzero whenever `S` is nonzero, because the multiplier `(c-i\gamma_j)^{-1}` in (16) never vanishes. It has no zero-frequency term and hence zero Cesaro mean. Therefore it changes sign infinitely often.

Choose a bounded sign component `(a,d)` on which

\[
J(u)<0,
\qquad
J(a)=J(d)=0.
\tag{21}
\]

The real-analytic function

\[
F(u):=e^{\lambda u}J(u)
\tag{22}
\]

is negative inside and zero at the endpoints, so it has a strict interior local minimum `u_*`. By (20),

\[
K_b(u_*)=0.
\tag{23}
\]

At this point (20) gives `J'(u_*)=-lambda J(u_*)`. Substitution in (17) yields

\[
S(u_*)=bJ(u_*)<0,
\tag{24}
\]

while

\[
R(u_*)=S(u_*)-J(u_*)=(b-1)J(u_*)>0.
\tag{25}
\]

Consequently

\[
\boxed{
R(u_*)/(-S(u_*))=(1-b)/b.}
\tag{26}
\]

Because `F` is real analytic and the minimum is strict, after shrinking to a compact interval `I=[u_*-r,u_*+r]` there exist fixed `m,eta_0>0` such that

\[
S(u)<-m,
\qquad
R(u)>m
\qquad(u\in I),
\tag{27}
\]

while `K_b` has opposite signs at the two endpoints, each with magnitude at least `eta_0`.

Thus the exact ray crossing is robust under sufficiently small uniform perturbations of both packet coordinates.

## 3. Finite-frequency recurrence makes the ray crossings logarithmically syndetic

`RE-032` used unbounded approximate periods. For a finite frequency set one can strengthen this to **relative density**, without any linear-independence assumption.

Let

\[
v(t):=(e^{i\gamma_1t},\ldots,e^{i\gamma_mt})
\tag{28}
\]

for the frequencies occurring on the rightmost face, and let `H` be the compact closure of `{v(t):t in R}` in the finite torus. Translation by the one-parameter subgroup is minimal on `H` by definition of the closure. Given a sufficiently small neighborhood `U` of the identity in `H`, compactness supplies finitely many nonnegative times `t_1,...,t_M` such that

\[
H\subset\bigcup_{j=1}^M v(-t_j)U.
\tag{29}
\]

Put `L_0=max_j t_j`. For every real `T`, some `j` satisfies

\[
v(T+t_j)\in U,
\tag{30}
\]

so every interval `[T,T+L_0]` contains an `epsilon`-almost period of all rightmost-face frequencies.

Choose `U` small enough that translation by any such almost period changes `S`, `R`, and `K_b` uniformly by less than a fixed fraction of the margins in (27). Then every sufficiently late interval of logarithmic phase contains a translate `I+tau` on which

\[
S<-m/2,
\qquad
R>m/2,
\tag{31}
\]

and `K_b` still has opposite endpoint signs. The intermediate value theorem supplies an exact zero of `K_b` inside every such translated window.

After absorbing the fixed width of `I` into `L`, the set of sign-correct exact-ray points is therefore syndetic in `u`. This is stronger than the unbounded recurrent subsequences used to establish cone compatibility in `RE-032`--`RE-033`.

The relative-density statement is standard Bohr almost-periodic behavior for a finite trigonometric polynomial. The compact-torus argument above is included so that no external recurrence theorem is load-bearing.

## 4. Lower spectral faces cannot remove the syndetic ray crossings

Return to the full finite packet. As in `RE-033`, after factoring out `x^{a_*}` write

\[
x^{-a_*}\Theta_P(x)=S(u)+H_S(u),
\qquad
x^{-a_*}L_P(x)=R(u)+H_R(u),
\tag{32}
\]

where finiteness gives a positive gap below `beta_*` and hence

\[
H_S(u),H_R(u)=O_P(e^{-\kappa u})
\tag{33}
\]

for some `kappa>0` whenever lower faces are present. The full normalized ray residual is

\[
K_{P,b}(u)
:=b(R(u)+H_R(u))+(1-b)(S(u)+H_S(u)).
\tag{34}
\]

By (33), on every sufficiently late translated window from Section 3 the perturbation in (34) is smaller than the fixed endpoint margin of `K_b`, while the perturbations of `S` and `R` are smaller than the sign margins in (31). Therefore the intermediate value theorem gives a point in each such window with

\[
K_{P,b}(u)=0,
\tag{35}
\]

and

\[
S(u)+H_S(u)<-m/4,
\qquad
R(u)+H_R(u)>m/4.
\tag{36}
\]

Multiplication by `x^{a_*}` proves (9)--(10).

Notice that this argument does not require the lower faces to be negligible at the much smaller fixed-threshold scale `x^{1/2-b}log x`. They need only vanish relative to the full rightmost amplitude. This is the same robust-window mechanism that removed the common-real-part restriction in `RE-033`, now applied to the stricter exact-ray equation.

## 5. The obstruction survives an infinite lower tail if it is `o` of the rightmost scale

The finite-packet conclusion has a useful stability extension. Suppose a pair of source coordinates admits, on `u=log x`, a decomposition

\[
x^{-a_*}\Theta(x)=S(u)+\epsilon_S(u),
\qquad
x^{-a_*}L(x)=R(u)+\epsilon_R(u),
\tag{37}
\]

with the same nonzero finite rightmost face `S,R` as above and

\[
\epsilon_S(u)\to0,
\qquad
\epsilon_R(u)\to0
\qquad(u\to\infty).
\tag{38}
\]

No finiteness of the lower contribution is needed. Equations (27), the syndetic almost periods, and the same perturbative intermediate-value argument show that sign-correct exact-ray points remain syndetic for the full pair.

Thus an **infinite spectral tail is not by itself a possible escape from the finite-packet obstruction**. To make coefficient geometry incompatible with `RE-034` while an isolated finite rightmost face is present, the omitted contribution would have to remain non-negligible at the rightmost power scale on every relevant recurrent window, or otherwise destroy the uniform approximation (38). A genuinely nonuniform top-edge tail, accumulation of real parts at the spectral supremum, or selector-dependent truncation may still do so.

## 6. Relation to the adaptive Robin scale and research consequence

At the exact ray points of (9)--(10), both packet coordinates have natural size `x^{a_*}`. If one interprets the standard coordinate through the `RE-034` identity

\[
-\mathcal E_\vartheta(x)\sim b h\sqrt x\log x,
\tag{39}
\]

the corresponding positive height scale is

\[
h\asymp x^{\beta_*-1}/\log x.
\tag{40}
\]

Because `beta_*>1-b`,

\[
x^{\beta_*-1}/\log x\gg x^{-b}
\tag{41}
\]

up to the diverging power `x^{beta_*+b-1}/log x`. Hence these finite-packet ray points are not excluded by the lower quantitative Robin amplitude in `RE-034`; the adaptive blockwise coefficient `c=Y^b(e^h-1)` is allowed to grow.

This is a negative spectral control, not an admissible prime sequence and not evidence that the CA selector actually visits these points. It does not prove RH false, nor does it establish one dominant spectral face for the true zeta errors. What it proves is narrower and directly adversarial to a tempting continuation of `RE-034`: **the exact ray itself is still not a finite-coefficient obstruction, even when one asks for recurrent rather than isolated compatibility.**

Bhattacharya--Martin--Simpson remain the current source boundary for the standard/reciprocal coefficient relation and global joint prime-race behavior; no novelty is claimed for those coefficients or for Bohr recurrence of finite trigonometric sums. `RE-030`--`RE-033` are the direct repository controls. The Mathia-specific delta is that the stricter adaptive ray from `RE-034` can be realized robustly and with bounded logarithmic gaps by every finite rightmost packet beyond the threshold line, and this remains true under any `o(x^{a_*})` lower spectral remainder.

The live route is therefore narrower again. A successful exclusion must use the arithmetic placement of the threshold-tangent CA selector relative to these syndetic ray windows, or prove that the actual zeta explicit-formula contribution near the right edge has no uniformly negligible remainder of the form (38). Merely strengthening the `RE-029` cone to the `RE-034` exact ray does not make finite spectral coefficient geometry coercive.