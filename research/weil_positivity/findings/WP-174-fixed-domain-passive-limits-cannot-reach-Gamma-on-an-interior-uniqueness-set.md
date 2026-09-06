# WP-174 — Fixed-domain passive limits cannot reach the Gamma response on an interior uniqueness set

**Status:** `LITERATURE+DERIVED + NORMAL-FAMILY-NO-GO + SCHUR-LIMIT-CLOSURE + ARCHIMEDEAN-GAMMA + DECISIVE-NARROWING + MATCHED-CONTROLS + PRIOR-ART-CLASSICALIZATION`.

`WP-170` proves that the exact real-place phase

\[
R_\infty(\tau)
=\pi^{i\tau}
\frac{\Gamma(\tfrac14-\tfrac{i\tau}{2})}
     {\Gamma(\tfrac14+\tfrac{i\tau}{2})}
\tag{1}
\]

is analytic but not Schur in the upper half-plane: its zeros

\[
\tau_n=i\left(2n+\frac12\right),\qquad n\ge0,
\tag{2}
\]

violate the Blaschke condition. `WP-173` then shows that every **regular** passive Hilbert termination of a pointwise `J`-contractive transfer block collapses back to an ordinary Schur response, while explicitly leaving singular/domain-changing closure as an escape.

A singular parameter limit does not by itself provide that escape. The scalar Schur class is closed under exactly the normal-family convergence needed to identify an analytic Gamma response. More sharply, if ordinary passive responses are analytic and contractive on one common domain, they cannot converge to (1) even merely **pointwise on an interior uniqueness set**. Vitali's convergence theorem forces such a sequence to converge locally uniformly to another Schur function, and the identity theorem then forces that Schur limit to equal `R_infty`, contradicting `WP-170`.

The same obstruction survives moving domains whenever they exhaust one fixed analytic domain: the domain must genuinely degenerate, or the contractive bound must be lost, before a non-Schur Gamma transfer can appear. On the boundary there is an independent stability check: ordinary lossless passive responses with monotone continuous phase lifts cannot converge uniformly on an interval spanning the sign change of the exact Gamma phase velocity.

Thus the `WP-173` singular-feedback escape is narrower than stated there. **A regularization whose every approximant remains an ordinary passive Schur response cannot become Gamma-compatible merely because the feedback denominator becomes singular in the limit.** What remains open is genuinely category-changing singular geometry: loss of a common analytic domain, weak/boundary-only convergence that does not preserve the passive phase order, unbounded renormalization followed by a new sign theorem, or nonseparable finite--archimedean assembly before scalarization.

## 1. Fixed-domain Schur limits are closed by Vitali

Let `D` be a connected complex domain and let

\[
s_m\in\mathcal O(D),
\qquad
|s_m(z)|\le1
\quad(z\in D)
\tag{3}
\]

for every `m`. Let `E subset D` have an accumulation point in `D`, and suppose that for a holomorphic target `R in O(D)`,

\[
s_m(z)\longrightarrow R(z)
\qquad(z\in E).
\tag{4}
\]

Because the family is uniformly bounded by one, it is locally uniformly bounded. Vitali's convergence theorem therefore gives a holomorphic `s in O(D)` such that

\[
s_m\longrightarrow s
\quad\text{locally uniformly on }D.
\tag{5}
\]

The bound passes to the limit:

\[
|s(z)|\le1
\qquad(z\in D),
\tag{6}
\]

so `s` is Schur. Equations (4)--(5) give `s=R` on `E`; since `E` has an interior accumulation point, the identity theorem gives

\[
\boxed{s\equiv R\text{ on }D.}
\tag{7}
\]

Consequently:

\[
\boxed{
R\notin\operatorname{Schur}(D)
\Longrightarrow
\text{no Schur sequence on }D
\text{ can converge to }R
\text{ on an interior uniqueness set.}
}
\tag{8}
\]

Montel plus subsequence uniqueness gives the same proof; Vitali packages the two steps directly. No operator realization theory is used here. Equation (8) is a closure property of the analytic contractive class itself.

Apply (8) to the upper half-plane and the analytic orientation (1). `WP-170` proves

\[
R_\infty\notin H^\infty(\mathbb H^+),
\qquad
R_\infty\notin\operatorname{Schur}(\mathbb H^+).
\tag{9}
\]

Hence there is no sequence of scalar passive characteristic responses `s_m` satisfying (3) on the upper half-plane and

\[
s_m(\tau)\to R_\infty(\tau)
\tag{10}
\]

on any subset of the **interior** upper half-plane having an accumulation point there. This is stronger than saying that compact-open convergence cannot work: even pointwise agreement along one interior sequence accumulating at a finite point is already too much.

This matters for singular feedback. Suppose a family of regularized Redheffer/LFT closures has denominators `D_m(z)` that approach noninvertibility as `m -> infinity`, but every visible regularized response is still a Schur function on the same `D`, as guaranteed by the passive mechanism of `WP-173`. If the singular limit is claimed to identify the analytic Gamma response on an interior uniqueness set, (8) gives an immediate contradiction. The vanishing feedback denominator is irrelevant unless it also destroys one of the hypotheses that made the visible responses a common-domain Schur family.

## 2. Merely moving the domain is not enough if a common domain survives locally

A superficial escape is to let the regularized response `s_m` live on domains `D_m` rather than one literal common `D`. This does not help if the domains exhaust a fixed connected domain `D` in the ordinary sense:

\[
\forall K\Subset D\quad
K\subset D_m
\quad\text{for all sufficiently large }m,
\tag{11}
\]

with

\[
|s_m(z)|\le1
\qquad(z\in D_m).
\tag{12}
\]

Take a connected compact exhaustion of `D`. Montel on each exhaustion level, followed by a diagonal subsequence, gives a holomorphic `s` on all of `D` with `|s|<=1`. If (4) holds on an interior uniqueness set, the diagonal limit agrees with `R` there and therefore everywhere. Thus (8) remains valid under (11)--(12).

So a genuinely domain-changing escape has to be stronger than parameter-dependent notation. At least one of the following must happen: singularities pinch into every candidate common analytic domain; the domains cease to exhaust the domain on which the Gamma transfer is to be identified; the passive bound ceases to be uniform; or the limiting object is no longer a holomorphic scalar transfer function. Those are substantive changes of analytic category, not ordinary singular limits inside the Schur class.

This distinction is useful for numerical or truncated models. A family may match the Gamma factor on finitely many interior sample points without contradiction, because a finite set has no accumulation point. Such finite interpolation is therefore not evidence that the singular passive limit exists. The decisive test is whether the construction supplies a source-forced continuum/analytic identification in a topology strong enough to trigger (8).

## 3. A boundary control: lossless phase order is also closed under uniform convergence

The interior theorem intentionally does not treat convergence specified only on the critical-line boundary. There is nevertheless a separate exact obstruction for the ordinary **lossless** passive class tested in `WP-170`.

Write on the real axis

\[
R_\infty(\tau)=e^{i\phi(\tau)}.
\tag{13}
\]

`WP-170` proves

\[
\phi'(\tau)
=\log\pi-
\operatorname{Re}\psi\!\left(\frac14+\frac{i\tau}{2}\right)
=-A_\infty(\tau),
\tag{14}
\]

and that `A_infty` is strictly increasing for `tau>0`, with a unique zero

\[
\tau_0\approx6.2898359888.
\tag{15}
\]

Therefore

\[
\phi'(\tau)>0\quad(0<\tau<\tau_0),
\qquad
\phi'(\tau)<0\quad(\tau>\tau_0).
\tag{16}
\]

On any compact interval `I` containing subintervals on both sides of `tau_0`, a continuous lift of the exact Gamma phase is therefore neither nondecreasing nor nonincreasing.

Now let

\[
b_m(\tau)=e^{i\phi_m(\tau)},
\qquad \tau\in I,
\tag{17}
\]

be continuous unimodular boundary responses whose real phase lifts `phi_m` are all nondecreasing in one passive orientation. This includes the ordinary continuous lossless/meromorphic-inner phase class used as the positive-time-delay control in `WP-170`. Suppose

\[
b_m\longrightarrow R_\infty
\quad\text{uniformly on }I.
\tag{18}
\]

For sufficiently large `m`, the quotient `b_m/R_infty` lies uniformly in a small arc around `1`, so it has a unique continuous principal argument `delta_m` with

\[
\|\delta_m\|_{L^\infty(I)}\longrightarrow0.
\tag{19}
\]

After changing each phase lift by one constant multiple of `2pi`,

\[
\phi_m=\phi+\delta_m,
\tag{20}
\]

and hence `phi_m -> phi` uniformly. A uniform limit of nondecreasing real functions is nondecreasing, contradicting (16). Reversing the passive orientation makes every `phi_m` nonincreasing and contradicts the positive part of (16) instead. Therefore

\[
\boxed{
\text{continuous lossless passive phases}
\not\xrightarrow[\text{uniform on }I]{}
R_\infty
}
\tag{21}
\]

on any interval spanning the Gamma phase-velocity reversal.

Equation (21) does **not** claim that arbitrary lossy Schur boundary traces have monotone phase. It is specifically a stability test for the lossless passive/inner route. It also does not exclude weak, merely almost-everywhere, or highly singular boundary convergence for which continuous phase lifts fail. Such a limit would have to explain independently why the distributional operation used to recover the Weil archimedean symbol remains valid and why positivity survives that weaker topology.

## 4. Operator-valued and determinant readouts do not evade the fixed-domain theorem in fixed dimension

Suppose `S_m(z)` are operator-valued Schur responses on one fixed Hilbert space:

\[
S_m(z)^*S_m(z)\le I.
\tag{22}
\]

For fixed unit vectors `u,v`,

\[
f_m(z)=\langle u,S_m(z)v\rangle
\tag{23}
\]

is a scalar Schur function. Therefore a claim that one fixed matrix coefficient converges to `R_infty` on an interior uniqueness set is ruled out by (8).

Likewise, for square responses of one fixed finite dimension `d`,

\[
|\det S_m(z)|\le1,
\tag{24}
\]

and the determinants are analytic. Thus a fixed-dimensional determinant readout cannot converge to `c R_infty` on an interior uniqueness set for any unimodular constant `c`.

These statements deliberately do not cover changing dimensions, Fredholm determinants requiring renormalization, varying test vectors, or scalarizations selected separately at each `m`. Those mechanisms can evade the literal compactness argument, but their selection/renormalization becomes part of the mathematical construction and must itself inherit an independent positive theorem. A readout chosen after seeing the Gamma target is precisely the hand-picked-kernel/regularization failure mode excluded by the research mandate.

## 5. Aggressive falsification and matched controls

**The theorem does not rule out finite interpolation.** A finite set of frequency samples has no interior accumulation point. In fact, Schur interpolation is governed by the classical Pick condition, so finite successful fits can occur without an analytic Gamma realization. Any computational evidence for this route must therefore test a source-forced analytic mechanism, not just increasingly accurate finite-frequency regression.

**The theorem does not rule out boundary-only weak convergence.** The real critical line is the boundary of the causal half-plane, so pointwise or weak convergence there does not trigger Vitali. Equation (21) closes uniform approximation only for the continuous lossless monotone-phase subclass. A proposal based on weak boundary limits remains logically open, but must specify the topology in which the phase derivative/digamma term is recovered and prove that the desired positive form is closed in that topology.

**Unbounded renormalization can leave the Schur class, but also leaves the inherited sign mechanism.** If responses are multiplied, quotiented, or rescaled by factors whose norms diverge, the unit-ball compactness used above is gone. That is a genuine escape from (8), not a counterexample. It means ordinary passivity no longer proves positivity of the visible scalar, so a new source-forced coercive/intersection/quotient theorem is required.

**A true singular relation can be different from a scalar transfer limit.** If `D_m^{-1}` converges only as an unbounded operator or linear relation, or if its domain changes, the scalar theorem need not apply. The branch should then identify the actual closed form/domain and prove its sign directly. Calling such an object a limit of passive systems is not enough: the sign has to survive at the level of the limiting form.

**The obstruction is not Gamma-specific as function theory, but the arithmetic application is.** Any non-Schur holomorphic target fails (8). A matched nonarithmetic target already inside the Schur class can be reached normally; for example `r_m S -> S` locally uniformly when `0<r_m<1`, `r_m ->1`, and `S` is inner. Thus the failure is not caused by taking a singular/lossless limit per se. It is caused by asking a closed passive analytic class to converge to the exact non-Schur real-place factor forced by the Riemann completion.

**Generalized-prime controls do not rescue the analytic step.** The normal-family obstruction knows nothing about primality. This is a limitation, not a defect in the proof: `WP-174` is a filter on a proposed archimedean positivity mechanism, not an arithmetic discriminator. The finite-prime and polar terms still have to be produced by the same global construction for the branch mandate to be met.

## 6. Prior-art and novelty audit

The analytic theorem is classical. Vitali's convergence theorem states that a locally uniformly bounded sequence of holomorphic functions which converges on a set with a limit point inside the domain converges locally uniformly to a holomorphic function. A standard classical reference is E. C. Titchmarsh, *The Theory of Functions*, 2nd ed., Oxford University Press, §5.21/p. 168 in common printings. Montel's normal-family theorem plus the identity theorem gives the same result. Standard Schur/inner references such as John B. Garnett, *Bounded Analytic Functions*, Springer GTM 236 (2007), provide the bounded-analytic/inner framework used in `WP-170`.

No novelty is claimed for Vitali, Montel, identity uniqueness, compact-open closure of the Schur class, monotone limits, or inner-function phase order. The Mathia-specific result is the conjunction of those classical closure principles with the exact source-derived Gamma transfer already isolated in `WP-169`--`WP-170` and the explicit singular-feedback escape left by `WP-173`:

\[
\boxed{
\text{ordinary passive Schur regularizations}
+\text{ fixed/exhausted analytic domain}
+\text{ interior identification of }R_\infty
\Longrightarrow\bot.
}
\tag{25}
\]

This is a prior-art classicalization and a decisive narrowing, not a new theorem in complex analysis and not a proof of Weil positivity.

The closest systems-theoretic boundary remains the classical `J`-inner/Schur linear-fractional theory already audited in `WP-173`: Harry Dym, *Linear fractional transformations*, Lecture Notes in Control and Information Sciences 286 (2003), 127--133; Damir Z. Arov and Harry Dym, *J-Contractive Matrix Valued Functions and Related Topics*, Cambridge University Press (2008); and Vladimir Derkach and Harry Dym, *On Linear Fractional Transformations Associated with Generalized J-Inner Matrix Functions*, Integral Equations and Operator Theory 65 (2009), 1--50, DOI `10.1007/s00020-009-1709-7`, arXiv `0901.0193`. `WP-174` adds no new LFT theorem; it shows that taking a passive regularized sequence to a singular parameter does not circumvent the already-classical Schur closure unless the limiting category genuinely changes.

## 7. Research consequence

The passive-boundary route is now constrained at the **limit topology**, not only at each regular realization. Scalar Schur fails for the exact Gamma phase (`WP-170`); regular positive matrix and finite-negative-index repairs fail (`WP-171`--`WP-172`); passive Hilbert termination of regular `J`-contractive external channels collapses back to Schur (`WP-173`); and now fixed-domain or exhaustively common-domain Schur regularizations cannot recover Gamma in the limit even from pointwise data on an interior uniqueness set.

The remaining singular routes are therefore genuinely singular. A viable construction must make essential use of at least one of: a domain collapse/pinching that destroys a common analytic transfer domain; a boundary-only weak limit together with a separately proved closed positive form; an unbounded or relation-valued quotient with an independent coercivity theorem; an infinite-index structure whose final positive quotient is source-forced; or a **nonseparable finite--archimedean geometry assembled before the Gamma factor becomes a separate scalar response**.

The last option remains the cleanest fit to the research mandate. It avoids asking the real-place Gamma phase itself to carry ordinary passive positivity and instead requires one intrinsic global object to produce finite Mangoldt support, the archimedean term, the polar/global counterterms, and the final sign together. `WP-174` does not construct that object; it removes another way of postponing the missing global geometry to a passive singular limit.