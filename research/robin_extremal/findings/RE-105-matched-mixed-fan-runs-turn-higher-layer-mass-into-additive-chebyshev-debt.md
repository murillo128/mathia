# RE-105 — matched mixed fan runs turn higher-layer mass into additive Chebyshev debt

**Status:** `EXACT-DERIVED + CORRECTION/GENERALIZATION + MIXED-PACKET + MATCHED-FRINGE + CHEBYSHEV-DEFICIT + HIGHER-LAYER-MASS + FAN-RUN + NO-CANCELLATION + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-070` proved that a matched `0 -> 0` **first-layer-only** tied fan switch forces a positive Chebyshev deficit through common-amplitude selector dilation, and `RE-072` accumulated that sign along a run of such switches. The later radical identity of `RE-075`/`RE-083` shows that the purity hypothesis was stronger than necessary for the standard-prime source. For the Chebyshev coordinate, arbitrary higher-layer events do not create an extra cancellation term: they enter with the **same sign as the selector dilation**.

More precisely, assume RH is false, put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12,
\]

fix

\[
J=[b_0,b_1]\Subset(1-\Theta,\tfrac12),
\tag{1}
\]

and work on a sufficiently late common positive CA counterexample block from `RE-040`. At a rightmost-fan breakpoint `b in J`, let

\[
C_-<C_+,
\qquad
Y_\pm:=\log C_\pm,
\tag{2}
\]

be consecutive exposed states tied at common adaptive amplitude

\[
c:=A_b(C_-)=A_b(C_+)>0,
\tag{3}
\]

with tangent selectors `Z_-<Z_+`. The complete physical CA packet from `C_-` to `C_+` may contain **arbitrarily many events at arbitrary depths**. Assume only that the endpoint first-layer fringe bits of `RE-059` are matched and zero,

\[
\chi_- = \chi_+ =0.
\tag{4}
\]

Write

\[
P_C:=\log C-\log\operatorname{rad}(C)
=\sum_{p^a\Vert C}(a-1)\log p
\tag{5}
\]

for the active depth-at-least-two log-mass, and put

\[
\Delta P:=P_{C_+}-P_{C_-}\ge0.
\tag{6}
\]

Let `Z_c(Y)` be the same formal common-amplitude selector curve as in `RE-070`, determined by

\[
a_c(Y):=\frac{cY^{-b}}{1+cY^{-b}},
\qquad
g(Z_c(Y))=g(Y)-\frac{b\,a_c(Y)}Y,
\qquad
g(x)=\frac1{x\log x}.
\tag{7}
\]

Then the two exposed endpoints satisfy `Z_c(Y_\pm)=Z_\pm`, and the Chebyshev deficit

\[
H_\vartheta(x):=x-\vartheta(x)
\tag{8}
\]

obeys the exact decomposition

\[
\boxed{
H_\vartheta(Z_+)-H_\vartheta(Z_-)
=
\Delta P
+
\int_{Y_-}^{Y_+}\bigl(Z_c'(t)-1\bigr)\,dt.
}
\tag{9}
\]

`RE-070` proves, independently of packet purity, that uniformly on late tied common-amplitude segments

\[
Z_c'(Y)-1
=b(1-b)a_c(Y)\log Y
\left(
1+O_J\!\left(\frac1{\log Y}+a_c(Y)\log Y\right)
\right)>0.
\tag{10}
\]

Hence every sufficiently late matched mixed switch satisfies

\[
\boxed{
H_\vartheta(Z_+)-H_\vartheta(Z_-)
=
\Delta P
+b(1-b)
\int_{Y_-}^{Y_+}a_c(t)\log t\,dt
\,(1+o_J(1))
>0.
}
\tag{11}
\]

The correction is structural: the first-layer-only condition in the Chebyshev part of `RE-070` is unnecessary. A higher-layer event cannot pay for the common-amplitude prime-density deficit. Its entire log-mass is added one-for-one to that deficit.

The same correction propagates to fan runs. Let

\[
\beta_1<\cdots<\beta_m,
\qquad
C_0<C_1<\cdots<C_m
\tag{12}
\]

be consecutive exposed rightmost-fan breakpoints and states. Suppose every switch packet `C_(i-1) -> C_i` has matched fringe `0 -> 0`, but impose **no restriction at all** on its higher-layer events. Let `Z_L,Z_R` be the initial and terminal selectors as in `RE-072`. For an internal state `C_i`, let `I_i=(\beta_i,\beta_{i+1})` and `Z_i(b)` be its fixed-state selector. Then

\[
\boxed{
\begin{aligned}
H_\vartheta(Z_R)-H_\vartheta(Z_L)
={}&
\sum_{i=1}^{m-1}
\int_{I_i}\frac{dZ_i}{db}\,db\\
&+
\sum_{i=1}^{m}
\int_{Y_{i-1}}^{Y_i}
\bigl(Z_{c_i}'(t)-1\bigr)\,dt\\
&+
\bigl(P_{C_m}-P_{C_0}\bigr).
\end{aligned}
}
\tag{13}
\]

Every term on the right is nonnegative and every nondegenerate cell or switch contributes positively. Thus `H_vartheta` is still monotone increasing along the whole selected path. If

\[
X:=\min_iY_i,
\qquad
w:=\beta_m-\beta_1,
\tag{14}
\]

then the common-block amplitude floor used in `RE-072` gives

\[
\boxed{
H_\vartheta(Z_R)-H_\vartheta(Z_L)
\ge
P_{C_m}-P_{C_0}
+c_JX^{1-b_1}\log X\,w
}
\tag{15}
\]

for some `c_J>0` and all sufficiently late blocks. The threshold-width cost from `RE-072` therefore survives unchanged, while the total higher-layer event mass becomes an additional positive source debt rather than an interruption currency.

## 1. The radical identity makes the mixed-switch correction exact

`RE-075`/`RE-083` upgrade the fixed-cell source identity of `RE-059` to

\[
\vartheta(Z)-\delta_\vartheta(Z)
=Y-P_C
=\log\operatorname{rad}(C),
\tag{16}
\]

where

\[
\delta_\vartheta(Z)=\chi\log r,
\qquad \chi\in\{0,1\}.
\tag{17}
\]

At the two matched endpoints (4), the correction vanishes, so subtraction gives

\[
\boxed{
\vartheta(Z_+)-\vartheta(Z_-)
=(Y_+-Y_-)-\Delta P.
}
\tag{18}
\]

This has a direct event interpretation. Every physical CA event increases `Y=log C` by its mass `log p`. First-layer events also increase `log rad(C)` by `log p`; higher-layer events do not. Therefore `Delta P` is exactly the total logarithmic mass of all depth-at-least-two events in the complete packet, including multiplicities and ties.

Using `Z_\pm=Z_c(Y_\pm)`, equation (18) gives

\[
\begin{aligned}
H_\vartheta(Z_+)-H_\vartheta(Z_-)
&=(Z_+-Z_-)-\bigl((Y_+-Y_-)-\Delta P\bigr)\\
&=\Delta P+
\left[(Z_+-Z_-)-(Y_+-Y_-)\right]\\
&=\Delta P+
\int_{Y_-}^{Y_+}(Z_c'(t)-1)\,dt,
\end{aligned}
\tag{19}
\]

which is (9). No prime-number-theorem estimate and no bound on packet cardinality or depth is used.

This also identifies precisely why the old purity restriction appeared. `RE-070` used the first-layer packet identity

\[
\vartheta(Z_+)-\vartheta(Z_-)=Y_+-Y_-.
\tag{20}
\]

For a mixed packet, (20) is false, but its correct replacement is not an uncontrolled error term. Equation (18) says the discrepancy is the positive quantity `Delta P`, and the sign in `H_vartheta=Z-vartheta` is favorable.

## 2. Mixed packets strengthen the prime-density deficit

Put

\[
\Delta Y:=Y_+-Y_-,
\qquad
D:=Z_+-Z_- -\Delta Y>0.
\tag{21}
\]

Then (18)--(19) give the exact pair

\[
\boxed{
\vartheta(Z_+)-\vartheta(Z_-)=\Delta Y-\Delta P,
\qquad
Z_+-Z_-=\Delta Y+D.
}
\tag{22}
\]

Consequently

\[
\boxed{
1-
\frac{\vartheta(Z_+)-\vartheta(Z_-)}{Z_+-Z_-}
=
\frac{\Delta P+D}{\Delta Y+D}.
}
\tag{23}
\]

The two mechanisms are therefore additive in the numerator of the exact relative underdensity: `Delta P` is the fraction of state growth spent on repeated prime powers rather than new prime supports, while `D` is the geometric dilation imposed by the tied adaptive selector.

For a sublinear packet `Delta Y=o(Y_-)`, write `Y=Y_-` and `a_-=a_c(Y)`. From `RE-070`,

\[
D
=b(1-b)a_-\log Y\,\Delta Y\,(1+o_J(1)).
\tag{24}
\]

Thus

\[
\boxed{
H_\vartheta(Z_+)-H_\vartheta(Z_-)
=
\Delta P
+b(1-b)a_-\log Y\,\Delta Y\,(1+o_J(1)).
}
\tag{25}
\]

If `rho:=Delta P/Delta Y`, then (23) becomes

\[
1-
\frac{\vartheta(Z_+)-\vartheta(Z_-)}{Z_+-Z_-}
=
\frac{\rho+s}{1+s},
\qquad
s=b(1-b)a_-\log Y\,(1+o_J(1)).
\tag{26}
\]

This interpolates correctly between the pure first-layer law `rho=0` of `RE-070` and a packet dominated by repeated-prime layers, where the selector interval must be correspondingly sparse in ordinary-prime Chebyshev mass.

The extreme control is a pure higher-layer packet. Then `Delta P=Delta Y`, the radical is unchanged, and (18) forces

\[
\vartheta(Z_+)-\vartheta(Z_-)=0.
\tag{27}
\]

Equation (9) reduces to

\[
H_\vartheta(Z_+)-H_\vartheta(Z_-)=Z_+-Z_-=\Delta Y+D,
\tag{28}
\]

exactly as it should: the adaptive selector crosses an interval carrying no new ordinary-prime support mass. This stress test fixes both the sign and the normalization of the `Delta P` term.

## 3. The no-cancellation run theorem also survives arbitrary higher layers

At an internal exposed state `C_i`, the left switch ends with fringe bit zero and the right switch begins with fringe bit zero. `RE-059` shows that inside one fixed support chamber the possible first-layer fringe bit is a monotone indicator of the increasing selector `Z_i(b)`, so it must remain identically zero throughout `I_i`. Therefore `vartheta(Z_i(b))` is constant on the cell and

\[
\boxed{
\frac{d}{db}H_\vartheta(Z_i(b))
=\frac{dZ_i}{db}>0.
}
\tag{29}
\]

At switch `i`, equation (9) gives

\[
\Delta_iH_\vartheta
=
\Delta_iP
+
\int_{Y_{i-1}}^{Y_i}
(Z_{c_i}'(t)-1)\,dt
>0.
\tag{30}
\]

Summing the positive cell increments and switch increments proves (13), because monotonic CA exponent growth gives

\[
\sum_{i=1}^m\Delta_iP
=P_{C_m}-P_{C_0}.
\tag{31}
\]

For the quantitative threshold-width term, `RE-072` already proves on every internal cell that

\[
\frac{dZ_i}{db}
=a_iY_i\log Y_i\,(1+o_J(1)),
\tag{32}
\]

while the common positive block supplies

\[
a_i\ge \frac{c_0}{2}Y_i^{-b_1}
\tag{33}
\]

uniformly late. The cells partition total threshold width `w`, and `Y_i>=X`, so

\[
\sum_{i=1}^{m-1}\int_{I_i}\frac{dZ_i}{db}\,db
\gg_J X^{1-b_1}\log X\,w.
\tag{34}
\]

Discarding the positive switch-dilation integrals but retaining the telescoped higher-layer mass gives (15).

This corrects the Chebyshev half of the boundary statement in `RE-072`: higher-layer packets are **not** a sign-changing interruption for `H_vartheta` when the switch fringes remain matched `0 -> 0`. They increase the same monotone ledger.

## 4. What is and is not generalized

The matched fringe condition remains load-bearing. Without it, (16) gives the exact general switch identity

\[
\boxed{
\Delta H_\vartheta
=
\Delta P+D
+\chi_-\log r_-
-\chi_+\log r_+.
}
\tag{35}
\]

An outgoing fringe `chi_+=1` can therefore insert a negative boundary pulse of order `log r_+`; the lacunary fringe machinery of `RE-048`--`RE-050` and `RE-063`--`RE-067` remains genuinely separate. The present theorem removes **higher-layer mixing**, not fringe interruptions, from the list of possible Chebyshev cancellation mechanisms.

Nor does this automatically generalize the reciprocal-Mertens half of `RE-071`--`RE-072`. A higher-layer exponent increment changes `sigma(C)/C` through a layer-dependent Euler-factor ratio, so the exact first-layer prime-product decomposition used there acquires additional terms whose sign relative to the normalized Mertens drift has not been eliminated by the radical identity. The durable claim here is intentionally one-source: the standard Chebyshev coordinate.

The theorem also does not contradict false RH. Since `b_1>1-Theta`, the threshold-width term in (15) has exponent `1-b_1<Theta`, below the natural off-critical prime-number-theorem fluctuation scale. The additive `P` term can be large only when the selected mixed run itself spends that much logarithmic state mass on higher layers; (15) records the required standard-source excursion but does not independently upper-bound it.

Finally, the result does not assert that a macroscopic matched run must exist. `RE-104` now forces either near-square-root fan complexity or huge physical stretch above the current local-boundary threshold, but that assembly may still be repeatedly interrupted by nonzero fringe behavior. What (13)--(15) show is that **arbitrary higher-layer packet complexity cannot serve as such an interruption once the endpoint fringe remains matched**.

## 5. Prior-art boundary and research consequence

The identities `Y-P_C=log rad(C)` and monotone CA exponent growth are elementary consequences of the classical Alaoglu--Erdos staircase; `RE-075`/`RE-083` already isolated their exact adaptive-selector support meaning. The common-amplitude selector derivative is the Mathia calculation of `RE-070`. A directed current search of Robin/CA work, including the August 2026 prime-layer workload preprint of Mantovanelli and recent CA-counterexample papers, found no external result coupling an adaptive false-RH tied fan switch to the exact decomposition (9), nor the run ledger (13) in which total higher-layer event mass enters additively with the Chebyshev selector-dilation cost. No external theorem beyond sources already anchored in `SOURCES.md` is load-bearing, so that file requires no change.

The live assembly frontier is narrower after `RE-104`. A bounded-stretch false-RH fan already needs almost square-root-many exposed ordinary-prime-gap chambers; a low-complexity escape requires enormous stretch. The present result removes one plausible way of neutralizing the standard-prime source while assembling either branch: **packing many higher-layer events into matched switch packets only makes the required Chebyshev excursion larger**. To reset or reverse this ledger, the fan must leave the matched-fringe regime, move through a different source coordinate, or exploit a genuinely nonlocal mechanism not represented by repeated-prime mass.

This is the useful correction to carry forward: for the standard Chebyshev source, the mixed staircase has an exact positive decomposition

\[
\boxed{
\text{fan excursion}
=
\text{fixed-cell selector motion}
+
\text{tied-switch selector dilation}
+
\text{higher-layer log-mass}.
}
\tag{36}
\]

The third term is not noise and not an escape. It is additional debt.