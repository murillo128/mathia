# RE-028 — threshold-tangent Robin witnesses force off-critical mixed-race excursions

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + THRESHOLD-TANGENT-CA + MIXED-RACE-OMEGA + JOINT-SOURCE-SELECTION + BLOCK-STRETCH-BYPASS + PRIOR-ART-ALIGNED`. `RE-027` converts Robin's quantitative false-RH excess into a moving-threshold CA selector and proves that the resulting external event coordinate `Z` has a super-square-root prime-layer defect `D(Z)=Z-\Phi(Z)`. That source defect can be coupled back to the Robin height without returning to an ordinary self-tangent block maximum.

Assume RH is false and put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12.
\tag{1}
\]

Fix

\[
1-\Theta<b<\frac12.
\tag{2}
\]

Let `c_b>0` be the constant supplied by Robin's quantitative CA oscillation theorem and let `C` run through the infinite threshold-tangent sequence furnished by `RE-027`. Write

\[
Y:=\log C,
\qquad
\tau_b(Y):=\log(1+c_bY^{-b}),
\tag{3}
\]

so that

\[
\log G(C)-\gamma\ge \tau_b(Y).
\tag{4}
\]

Let `Z>Y` be the external CA event coordinate selected by the modified tangent,

\[
\frac1{Z\log Z}
=
\frac1{Y\log Y}
-
\frac{b c_b}{Y(Y^b+c_b)},
\tag{5}
\]

and let `p` be the largest active first-layer prime at `Z`. Then `RE-027` gives

\[
Y=\Phi(Z),
\qquad
D(Z):=Z-Y
\sim b c_b Z^{1-b}\log Z.
\tag{6}
\]

Define, exactly as in `RE-008`--`RE-009`,

\[
E(p)
:=
\sum_{r\le p}-\log(1-r^{-1})-\gamma-\log\log p,
\tag{7}
\]

\[
h(p):=\frac{-\log(1-p^{-1})}{\log p},
\qquad
\mathcal M_*(p):=E(p)-(\vartheta(p)-p)h(p),
\tag{8}
\]

and

\[
\mathscr Y(p):=\sqrt p\log p\,\mathcal M_*(p).
\tag{9}
\]

Then the same threshold-selected states satisfy

\[
\boxed{
\mathcal M_*(p)
\ge
(c_b+o(1))p^{-b}.
}
\tag{10}
\]

Consequently

\[
\boxed{
\mathscr Y(p)
\ge
(c_b+o(1))p^{1/2-b}\log p
\longrightarrow+\infty.
}
\tag{11}
\]

Thus the moving-threshold selection of `RE-027` removes the block-stretch escape of `RE-026` on **both** source coordinates at once. On one and the same infinite CA-selected sequence,

\[
\boxed{
\frac{D(Z)}{\sqrt p}\longrightarrow+\infty,
\qquad
\mathscr Y(p)\longrightarrow+\infty.
}
\tag{12}
\]

The first condition is a prime-layer staircase defect; the second is the endpoint-subtracted Mertens--Chebyshev mixed race identified in `RE-009`. Global divergence of the mixed race under false RH is not new and is not enough for Robin. The new repository-level content is that Robin's quantitative moving threshold forces the positive off-critical-scale mixed excursion at the **same sparse boundary primes selected by the CA extremum**, while `RE-027` simultaneously fixes the associated event-workload defect.

## 1. The threshold-selected state has an exact off-self-tangent height splice

The state `C` is the ordinary CA maximizer at event coordinate `Z`. Its active first layers are precisely the primes `r<=p`, while the higher active layers contribute

\[
\Phi_{\ge2}(Z)
:=
\sum_{\substack{r\ \mathrm{prime},\ j\ge2\\\eta_{r,j}<Z}}
\log r.
\tag{13}
\]

Regularity keeps `Z` away from tied event parameters, so endpoint conventions are immaterial. Since `Y=\Phi(Z)`, splitting first and higher layers gives the exact relation

\[
\boxed{
Y=\vartheta(p)+\Phi_{\ge2}(Z).
}
\tag{14}
\]

Let

\[
T(C):=-\sum_{r\le p}\log(1-r^{-(a_r+1)})\ge0.
\tag{15}
\]

The finite Euler-product factorization used in `RE-008` is valid for this CA state without self-tangency:

\[
\log G(C)-\gamma
=
E(p)-T(C)+\log\frac{\log p}{\log Y}.
\tag{16}
\]

Substitute

\[
E(p)=\mathcal M_*(p)+(\vartheta(p)-p)h(p)
\tag{17}
\]

and use (14):

\[
\vartheta(p)-p
=Y-p-\Phi_{\ge2}(Z).
\tag{18}
\]

Also

\[
\log\frac{\log p}{\log Y}
=-\int_p^Y\frac{dt}{t\log t},
\tag{19}
\]

where the integral is oriented if `Y<p`. Define the oriented geometric remainder

\[
Q(p,Y)
:=
\int_p^Y
\left(
h(p)-\frac1{t\log t}
\right)dt.
\tag{20}
\]

Equations (16)--(20) give the exact identity

\[
\boxed{
\log G(C)-\gamma
=
\mathcal M_*(p)
-T(C)
-\Phi_{\ge2}(Z)h(p)
+Q(p,Y).
}
\tag{21}
\]

This is the off-self-tangent analogue of the splice in `RE-008`. There the intrinsic state coordinate and the external event coordinate coincide. Here they do not: the higher-layer mass is evaluated at the selector `Z`, while the normalization correction runs only between the largest first-layer prime `p` and the intrinsic logarithmic size `Y=\log C`.

The separation is important because `D(Z)=Z-Y` is intentionally large. One must not replace `Y` by `Z` inside the Robin normalization and then treat the resulting term as negligible.

## 2. The only potentially harmful geometric term is negligible at Robin's off-critical scale

Let `q` be the ordinary prime following `p`. First-layer event order and regularity give

\[
\eta_{p,1}<Z<\eta_{q,1}.
\tag{22}
\]

The first-layer localization already established in this line is

\[
r\le\eta_{r,1}<r+1.
\tag{23}
\]

Together with the currently anchored unconditional prime-gap input this yields

\[
Z-p=O(p^{0.52}),
\qquad
p\sim Z.
\tag{24}
\]

Equation (6) has `1-b<1`, hence `D(Z)=o(Z)` and therefore

\[
Y=Z-D(Z)\sim Z\sim p.
\tag{25}
\]

Put

\[
s:=Y-p=(Z-p)-D(Z).
\tag{26}
\]

Then

\[
|s|
=O\!\left(p^{0.52}+p^{1-b}\log p\right)
=o(p).
\tag{27}
\]

The endpoint weight satisfies the elementary expansion

\[
h(p)
=
\frac1{p\log p}
+O\!\left(\frac1{p^2\log p}\right).
\tag{28}
\]

For every `t` between `p` and `Y`, equation (27) keeps `t\asymp p`, and

\[
\left|\frac{d}{dt}\frac1{t\log t}\right|
\ll\frac1{p^2\log p}.
\tag{29}
\]

Equations (20), (28), and (29) therefore give

\[
\boxed{
|Q(p,Y)|
\ll
\frac{|s|+s^2}{p^2\log p}.
}
\tag{30}
\]

This is `o(p^{-b})` for every `b` in (2). Indeed, if `1-b>=0.52`, then (27) gives

\[
|Q(p,Y)|
\ll
p^{-2b}\log p+o(p^{-b})
=o(p^{-b}),
\tag{31}
\]

because `b>0`. If `1-b<0.52`, then `b>0.48` and

\[
|Q(p,Y)|
\ll p^{-0.96+o(1)}
=o(p^{-b}).
\tag{32}
\]

The equality case is covered by either estimate. Thus

\[
\boxed{Q(p,Y)=o(p^{-b}).}
\tag{33}
\]

No Mertens estimate, PNT error estimate for `vartheta`, or sign information on the mixed race has entered this step. The short-interval input is used only to make the selector-to-frontier displacement sufficiently sublinear that the exact geometric correction is below the off-critical Robin scale.

## 3. Positivity of the CA tails turns the height lower bound into a mixed-race lower bound

Rearrange (21):

\[
\mathcal M_*(p)
=
\log G(C)-\gamma
+T(C)
+\Phi_{\ge2}(Z)h(p)
-Q(p,Y).
\tag{34}
\]

Both omitted CA terms are nonnegative:

\[
T(C)\ge0,
\qquad
\Phi_{\ge2}(Z)h(p)\ge0.
\tag{35}
\]

Hence the exact identity immediately gives

\[
\boxed{
\mathcal M_*(p)
\ge
\log G(C)-\gamma-|Q(p,Y)|.
}
\tag{36}
\]

This is the useful direction: no asymptotic evaluation of the exponent tail or of the higher prime-power layers is required.

By construction of the threshold-selected state in `RE-027`, equation (4) holds. Since

\[
\tau_b(Y)
=
\log(1+c_bY^{-b})
=c_bY^{-b}+O(Y^{-2b}),
\tag{37}
\]

and `Y\sim p`, equations (33), (36), and (37) yield

\[
\mathcal M_*(p)
\ge
c_b p^{-b}+o(p^{-b}),
\tag{38}
\]

which is (10). Multiplication by `sqrt(p) log p` proves (11) because `b<1/2`.

The sign is worth auditing. In the exact height identity (21), both the exponent tail and higher-layer term enter with a minus sign. Solving for `mathcal M_*` therefore makes them positive. Dropping them can only weaken the required source excursion; no hidden cancellation is being assumed.

## 4. The same selector now carries both quantitative false-RH source defects

`RE-027` already gives

\[
D(Z)
\sim b c_b Z^{1-b}\log Z.
\tag{39}
\]

Together with `p\sim Z`, equations (11) and (39) show that the threshold-selected sequence carries the pair

\[
D(Z)
\asymp_b p^{1-b}\log p,
\qquad
\mathscr Y(p)
\gg_b p^{1/2-b}\log p.
\tag{40}
\]

For any fixed

\[
0<\varepsilon<\Theta-\frac12,
\tag{41}
\]

one may take

\[
b=1-\Theta+\varepsilon.
\tag{42}
\]

Then an infinite threshold-selected CA subsequence satisfies

\[
D(Z)
\asymp_{\varepsilon}
 p^{\Theta-\varepsilon}\log p,
\tag{43}
\]

and

\[
\boxed{
\mathscr Y(p)
\gg_{\varepsilon}
 p^{\Theta-1/2-\varepsilon}\log p.
}
\tag{44}
\]

The constants and selected sequence depend on `b`, as they already do in Robin's quantitative theorem; (43)--(44) do not describe one common subsequence as `epsilon` varies.

This reformulates the false-RH exponent in the line's two current source coordinates. It does not create a new zero-detection theorem: Robin's inverse-power excursion is the load-bearing analytic input. What changes is the selection geometry. `RE-026` could transfer a quantitative witness to an ordinary self-tangent maximum only at the cost of a race-or-block-stretch dichotomy. `RE-027` removed that stretch for `D` by tilting the tangent. Equation (21) now shows that the same tilt also preserves enough of the original height to force the mixed source race itself at the corresponding first-layer boundary prime.

## 5. Relation to the ordinary self-tangent route

The ordinary self-tangent counterexample route and the threshold-tangent route answer different questions.

For an ordinary self-tangent state the event coordinate equals its intrinsic logarithmic size, `Z=Y`, so `D(Y)=0`. `RE-021`--`RE-023` then show that Robin failure forces the normalized mixed coordinate only past a fixed square-root threshold, while `RE-026` shows that Robin's stronger inverse-power excess can be lost when the strong witness and the selected block maximum are far apart.

For the present threshold-tangent state, `Z>Y` and `D(Z)` is deliberately nonzero. There is no transport to another state: the same `C` that maximizes the moving-threshold functional satisfies the quantitative Robin excess (4). The exact identity (21) therefore retains that excess and turns it into (10)--(11).

This does **not** solve the original accepted clean-selector clue. Its live question concerns whether ordinary self-tangent counterexample peaks can realize the finite-annulus mixed-race threshold infinitely often. The present theorem instead supplies a second, quantitatively stronger selector that every false-RH world must realize. A future contradiction may therefore target the joint conditions (39)--(40) directly, without first controlling total counterexample-block span.

## 6. Prior art and novelty boundary

Robin's 1984 Proposition 1 remains the load-bearing external theorem. Its quantitative inverse-power oscillation under hypothetical RH failure is classical and no novelty is claimed for the exponent range `1-Theta<b<1/2`. Alaoglu--Erdos supply the CA variational structure, while Mantovanelli's 2026 preprint is the closest current prior art for the prime-layer event coordinate and exact workload representation.

`RE-009` already identifies `mathscr Y` with the normalized reciprocal-minus-standard prime-error race studied by Bhattacharya--Martin--Simpson, up to an unconditional vanishing correction. Their results make global one-sided boundedness of this race RH-equivalent. Thus a divergent mixed excursion somewhere under false RH is not a new phenomenon and cannot be used by itself as progress.

The substantive delta here is the exact **selector-conditioned splice** (21) and its consequence (10)--(12): the moving quantitative Robin tangent from `RE-027` forces the mixed excursion at the largest first-layer primes of those same threshold-selected CA states, simultaneously with the prescribed prime-layer defect. A targeted search across Robin quantitative oscillations, current CA counterexample-window work, Mertens/Chebyshev formulations, and the recent prime-layer workload terminology did not locate this exact moving-threshold/mixed-race coupling. This is a bounded prior-art assessment, not a claim that its constituent analytic oscillations are new.

No new `SOURCES.md` entry is required; every load-bearing source is already anchored there.

## 7. Falsification boundaries and research consequence

The theorem is conditional on hypothetical RH failure. It does not provide an unconditional upper bound for `D(Z)` or `mathscr Y(p)`, and an attempt to exclude (11) by a global one-sided bound for the mixed race would simply invoke an RH-equivalent statement by `RE-009`.

The threshold-selected states are not asserted to be ordinary local maxima of `G` or ordinary self-tangent zeros. Therefore the adjacent-peak clearance and directional layer-depth conclusions of `RE-025` cannot be imported without a new argument. The selected state is instead a local maximum of the explicit moving-threshold functional from `RE-027`.

The estimate of `Q` uses only the already anchored sub-three-quarter-power quality of ordinary prime gaps; the line's current `0.52` input is more than sufficient. If that input were weakened past the scale at which (30) is `o(p^{-b})`, the quantitative mixed lower bound would have to be re-audited.

Finally, (10) is one-sided only on this threshold-selected sequence. It says nothing about arbitrary primes and does not imply that the ordinary self-tangent counterexample selector has the same power-scale growth. The next genuinely useful theorem is an **independent incompatibility for the joint selected pair**

\[
D(Z)\sim b c_b Z^{1-b}\log Z,
\qquad
\mathcal M_*(p)\ge(c_b+o(1))p^{-b},
\tag{45}
\]

using the CA event structure or a source-conditioned correlation estimate weaker than global RH-equivalent control. That is now a sharper target than either source coordinate in isolation.