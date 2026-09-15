# RE-149 — zero-horizontal-spread product packets isolate vertical reciprocal escape

**Status:** `EXACT-DERIVED + MATCHED-CONTROL + FINITE-ZERO-EDGE + LEADING-ROBIN-PACKET + ZERO-HORIZONTAL-SPREAD + PURE-VERTICAL-ESCAPE + SCALE-MAXIMAL-ANCHOR + EXPONENTIAL-RADIUS-SUPPRESSION + ARBITRARILY-SLOW-SCALED-ESCAPE + DECISIVE-NEGATIVE + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

`RE-148` removes the positional mismatch between the cardinality-free reciprocal-box floor and the Pintz right-shell estimate. It leaves three genuinely different quantitative obligations: improve the local exponential rate, control the one-sided near-left geometry exposed by `RE-144`, and control modes that are horizontally locked to the anchor but escape vertically from the chosen reciprocal box.

The third obstruction is real on its own. The subset-product mechanism does not need any horizontal displacement at all. For every fixed relative observation window and every prescribed divergent scaled-radius envelope, one can build a formal simple finite-edge spectrum in which the active cancellation packet lies **exactly on one vertical line**, its lowest-ordinate atom is the unique scale-maximal Robin atom, and the complete packet is exponentially small in its vertical scaled radius. The radius may diverge as slowly as prescribed.

Consequently, excluding the near-left cluster of `RE-144` is not enough to close the `RE-148` splice. In the matched class, horizontal locking can be perfect while vertical reciprocal escape alone hides the anchor. Any actual-zeta closure now needs source-specific control of the vertical occupancy/phase geometry, or an argument that couples that geometry to information not present in the abstract positive-measure model.

Fix

\[
\frac12<\sigma_0<\Theta<1,
\qquad A>0,
\qquad 0<\kappa<\frac12,
\tag{1}
\]

and let `W(U)` and `L(T)` be arbitrary nondecreasing functions tending to infinity. There exists a single formal simple spectrum `Z_ctl`, closed under conjugation and `rho -> 1-rho`, with an attained finite right edge `Re rho=Theta`, together with phases `U_j->infinity` and strict-subedge target atoms

\[
\rho_{0,j}=\beta_j+i\Gamma_j,
\tag{2}
\]

such that, for the leading Robin coefficient

\[
a_{\rho,0}(u)
:=
\frac{e^{-(\Theta-\beta)u}}{\rho(1-\rho)},
\tag{3}
\]

the following hold along the stage sequence.

The target is algebraically strong and scale-maximal,

\[
M_0^{\rm ctl}(U_j)
=
(1+o(1))|a_{\rho_{0,j},0}(U_j)|
\asymp U_j^{-A}.
\tag{4}
\]

Every atom responsible for order-one stage cancellation has exactly the same real part as the target,

\[
\boxed{\beta=\beta_j,}
\tag{5}
\]

while its scaled vertical displacement obeys

\[
0\le U_j(\gamma-\Gamma_j)\le W(U_j).
\tag{6}
\]

Nevertheless

\[
\boxed{
\sup_{|u-U_j|\le\kappa U_j}
|\mathcal S_0^{\rm ctl}(u)|
=o\!\left(M_0^{\rm ctl}(U_j)\right).
}
\tag{7}
\]

More quantitatively, if `R_j` is the scaled vertical radius of the active stage, then for some constants `c_kappa,C_kappa>0`,

\[
R_j\asymp_\kappa j,
\qquad
\sup_{|u-U_j|\le\kappa U_j}
|\mathcal S_{0,j}(u)|
\le C_\kappa e^{-c_\kappa R_j}
|a_{\rho_{0,j},0}(U_j)|.
\tag{8}
\]

The one-level off-critical counting function can simultaneously satisfy

\[
N_{\rm ctl}(\sigma_0,T)\le L(T)
\tag{9}
\]

for all sufficiently large `T`, up to the same harmless fixed enlargement used in the earlier matched controls if the attained-edge quartet is included in the count.

## 1. A purely vertical contractive factor exists on every allowed relative window

Write

\[
I_\kappa=[1-\kappa,1],
\qquad
x_c:=1-\frac\kappa2,
\qquad
\omega_\kappa:=\frac\pi{x_c}.
\tag{10}
\]

Then `e^{i omega_kappa x_c}=-1`. For `x in I_kappa`,

\[
1+e^{i\omega_\kappa x}
=
1-e^{i\omega_\kappa(x-x_c)},
\tag{11}
\]

and therefore

\[
\left|1+e^{i\omega_\kappa x}\right|
\le
2\sin\!\left(
\frac{\pi\kappa}{4(1-\kappa/2)}
\right)
=:q_\kappa.
\tag{12}
\]

The restriction `kappa<1/2` is exactly enough to make this factor strictly contractive:

\[
\frac{\pi\kappa}{4(1-\kappa/2)}<\frac\pi6,
\qquad
\boxed{0<q_\kappa<1.}
\tag{13}
\]

Thus no horizontal damping is needed to obtain a factor below one on the whole macroscopic window. The phase increment alone suffices.

This is stronger, for the present purpose, than the factor used in `RE-133/144`. There the horizontal decrement `lambda/U` supplied the amplitude ratio `r`; here the amplitude ratio is one at the frozen-coefficient level and the entire contraction is purchased by vertical phase geometry.

## 2. A simple same-real-part cluster realizes the product

Choose `U_j` recursively and put

\[
\Gamma_j:=U_j^{A/2},
\qquad
\delta_j:=U_j^{-2},
\qquad
\beta_j:=\Theta-\delta_j.
\tag{14}
\]

For `1<=ell<=j`, let

\[
\varepsilon_{j,\ell}:=U_j^{-3}3^{-\ell},
\qquad
\omega_{j,\ell}:=\omega_\kappa+\varepsilon_{j,\ell}.
\tag{15}
\]

For every subset `S` of `{1,...,j}` define

\[
\rho_{j,S}
:=
\beta_j+i\gamma_{j,S},
\qquad
\gamma_{j,S}
:=
\Gamma_j+
\frac1{U_j}
\sum_{\ell\in S}\omega_{j,\ell}.
\tag{16}
\]

All `2^j` right-half-strip coordinates have **exactly** the same real part. They are simple: different cardinalities are separated by an integer multiple of `omega_kappa` up to a perturbation much smaller than `omega_kappa`, while equal cardinalities are separated by uniqueness of the finite ternary subset sums in (15).

Let the empty-subset atom be the target,

\[
\rho_{0,j}=\rho_{j,\varnothing}=\beta_j+i\Gamma_j.
\tag{17}
\]

At fixed `beta_j in (1/2,1)`,

\[
|\rho(1-\rho)|^2
=(\beta_j^2+\gamma^2)
((1-\beta_j)^2+\gamma^2)
\tag{18}
\]

is strictly increasing for `gamma>0`. Hence, within the entire stage, the target is the **unique exact maximizer** of the leading coefficient magnitude: every nonempty subset has larger ordinate and smaller `|d_rho|`, where `d_rho=1/[rho(1-rho)]`.

At the center,

\[
|a_{\rho_{0,j},0}(U_j)|
=
(1+o(1))\Gamma_j^{-2}
=(1+o(1))U_j^{-A}.
\tag{19}
\]

For `u=U_jx`, `x in I_kappa`, the exponential damping is identical for every member of the stage, while logarithmic differentiation of `d_rho` gives uniformly in `S`

\[
\frac{d_{\rho_{j,S}}}{d_{\rho_{0,j}}}
=
1+O\!\left(
\frac{j}{U_j\Gamma_j}
\right).
\tag{20}
\]

The relative carrier is

\[
e^{i(\gamma_{j,S}-\Gamma_j)u}
=
\prod_{\ell\in S}e^{i\omega_{j,\ell}x}.
\tag{21}
\]

Freezing the harmless bracket variation in (20), the whole positive-frequency stage therefore factors exactly as

\[
a_{\rho_{0,j},0}(u)e^{i\Gamma_j u}
\prod_{\ell=1}^{j}
\left(1+e^{i\omega_{j,\ell}x}\right).
\tag{22}
\]

By (12)--(15), choose once and for all `q_1` with

\[
q_\kappa<q_1<1.
\tag{23}
\]

For all sufficiently large `j`, every factor in (22) has modulus at most `q_1` uniformly on `I_kappa`. Restoring the exact Robin brackets costs at most

\[
|a_{\rho_{0,j},0}(u)|
O\!\left(\frac{j}{U_j\Gamma_j}\right)2^j.
\tag{24}
\]

The recursive choice of `U_j` is free enough to impose

\[
\frac{j2^j}{U_j\Gamma_j}\le q_1^j.
\tag{25}
\]

Hence the actual stage satisfies

\[
\boxed{
\sup_{u\in[(1-\kappa)U_j,U_j]}
\left|
\sum_{S}a_{\rho_{j,S},0}(u)e^{i\gamma_{j,S}u}
\right|
\ll q_1^j |a_{\rho_{0,j},0}(U_j)|.
}
\tag{26}
\]

Taking `2 Re` preserves the same exponential order.

## 3. The exponential radius law is already sharp on a vertical line

The current-stage scaled horizontal radius is identically zero. Its scaled vertical radius is

\[
R_j
:=
U_j\max_S|\gamma_{j,S}-\Gamma_j|
=
j\omega_\kappa+o(1).
\tag{27}
\]

Thus (26) becomes

\[
\sup_I|\mathcal S_{0,j}|
\ll
\exp\!\left[-
\left(
\frac{-\log q_1}{\omega_\kappa}+o(1)
\right)R_j
\right]
|a_{\rho_{0,j},0}(U_j)|.
\tag{28}
\]

Since `q_1` can be taken arbitrarily close to `q_kappa`, any constant

\[
0<c<
\frac{-\log q_\kappa}{\omega_\kappa}
\tag{29}
\]

is achievable in the exponent for all sufficiently large stages.

There is also a normalized positive-measure form directly relevant to `RE-145/148`. The empirical measure of the `2^j` scaled offsets is supported on the vertical segment `Re lambda=0`, `0<=Im lambda<=R_j`, and its Laplace transform is

\[
Q_j(x)
=
2^{-j}
\prod_{\ell=1}^{j}
(1+e^{i\omega_{j,\ell}x}).
\tag{30}
\]

Therefore

\[
\sup_{I_\kappa}|Q_j(x)|
\le
\left(\frac{q_1}{2}\right)^j
=
\exp[-\Omega_\kappa(R_j)].
\tag{31}
\]

So the `exp(-O(R))` functional order of the cardinality-free floor is already sharp after deleting the horizontal dimension of the reciprocal box altogether. Any improvement relevant to actual zeta must use more than horizontal localization plus positivity.

Finally, because `W(U)->infinity`, enlarge each phase until

\[
W(U_j)\ge j(1+\omega_\kappa).
\tag{32}
\]

Then (27) implies (6). The vertical scaled diameter may therefore escape every fixed box as slowly as one wishes.

## 4. The construction embeds in one sparse finite-edge spectrum

Close every stage under conjugation and `rho -> 1-rho`, and adjoin a fixed simple quartet with right member on `Re rho=Theta` to make the formal edge attained. The reflected stage points lie to the left of `1/2` and do not enter the strict-subedge right-half-strip packet.

Choose the phases with strong lacunarity, for instance starting with `U_{j+1}>=U_j^4`, and enlarge them further so that all earlier stages are exponentially damped on the stage-`j` window. Because the earlier horizontal edge distances `delta_n=U_n^{-2}` are fixed once stage `n` is chosen, this can be arranged exactly as in `RE-133`:

\[
\sum_{n<j}2^n
\frac{
 e^{-(1-\kappa)U_j/(2U_n^2)}
}{1+\Gamma_n^2}
=o(U_j^{-A}).
\tag{33}
\]

Likewise choose every future phase so large that the full future coefficient tail is summable and

\[
\sum_{n>j}2^n U_n^{-A}
=o(U_j^{-A}).
\tag{34}
\]

Equations (26), (33), and (34) prove the full-packet hiding statement (7), while (18)--(19) and the same tail budgets give the global scale-maximality claim (4).

The same freedom preserves an arbitrary divergent one-level count. Require

\[
L(\Gamma_j)\ge2^{j+3}
\tag{35}
\]

when choosing `U_j`. Between consecutive stage heights the completed positive-ordinate population is `<2^{j+1}+O(1)`, so monotonicity of `L` gives (9) after an immaterial fixed adjustment for the edge quartet.

For the height-truncated geometry, take `T_j=2\Gamma_j`. The entire current stage lies below `T_j`, while future stages lie above it. Previous stages have smaller real part because `beta_n=Theta-U_n^{-2}<beta_j`. Thus for every fixed `R>0`, the strict-subedge shell

\[
\{\rho:0<\Im\rho\le T_j,\ \Re\rho\ge\beta_j+R/U_j\}
\tag{36}
\]

is empty for all large `j`. The active cancellation is neither a near-left packet nor a sufficiently-rightward shell: it is entirely vertical at `beta=beta_j`.

## 5. Adversarial and representation audit

This is a matched-control theorem, not a claim about the actual zero set of `zeta`. The construction preserves simplicity, conjugation/functional-equation symmetry, an attained finite edge, the exact leading Robin coefficient law, an algebraically strong scale-maximal anchor, and arbitrarily sparse one-level off-critical counting. It does not assert an Euler product, explicit-formula compatibility, pair correlation, local zero-density lower bounds, determinant positivity, or any other source-specific law that could forbid the vertical subset geometry.

There is no hidden horizontal amplitude parameter. Equation (5) is exact throughout every active stage. The contraction in (22) is purely phase-driven. The target remains the unique leading-coefficient maximizer because the subset increments are one-sided in ordinate, so (18) makes every companion coefficient slightly smaller even though all real parts coincide.

The construction also does not contradict `RE-145/148`. Those findings say that a packet contained in a fixed scaled box has a positive visibility floor and that a radius-`R` box loses at most exponentially in `R`. Here `R_j->infinity`, and (31) shows that exponential deterioration is already attainable on a vertical segment. Nor does it contradict `RE-144`: that finding isolates a one-sided horizontal escape; the present finding removes that geometry and exhibits an independent vertical escape.

## 6. Prior-art boundary and research effect

The finite-product identity in (22) belongs to the classical Riesz-product / finite trigonometric-product neighborhood. A targeted audit of Riesz-product references and Turan--Nazarov observability results confirms that product-generated frequency sets and exponential-polynomial interval control are classical harmonic-analysis mechanisms. No external theorem is load-bearing here: the contractive factor is the elementary identity (11)--(13), and the Robin transfer is the explicit coefficient comparison (18)--(25). `SOURCES.md` therefore needs no update.

The line-specific consequence is sharper. After `RE-148`, one might try to eliminate the near-left cluster and then splice the local floor with the Pintz right shell. `RE-149` shows that this is insufficient in the matched class: even **zero horizontal spread plus an empty truncated right shell** leaves a vertically growing packet capable of exponential hiding. The next source-specific target is therefore a vertical one: control the number, spacing, phase entropy, or coefficient correlation of zeros with

\[
|\beta-\beta_0|\ll U^{-1}
\tag{37}
\]

across growing ordinate windows, or prove that actual-zeta structure couples such vertical growth to a compensating observable. Improving horizontal localization alone cannot close the remaining visibility problem.
