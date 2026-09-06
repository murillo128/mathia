# WI-177 — affine vector source assemblies are period-33 cancelled

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + ROUTE-SPECIFIC-BARRIER + CLASSICAL-CONVEX-FRAMEWORK + NO-NOVELTY-CLAIM`. WI-176 closes arbitrary scalar local potentials when global accounting remembers only one universal scalar tax. The current source-constrained frontier explicitly leaves a vector/state-resolved observable as a possible escape. Merely retaining several additive coordinates is not sufficient: if the global proof ultimately consumes that vector through affine/support-function dual directions, the period-33 witness cancels every direction simultaneously. Any such direction gives a theorem output strictly below the witness density `0.67361`; in the usual nonnegative-local-floor regime it obeys the same uniform `0.673604` ceiling as WI-176.

No unconditional simple-critical-zero proportion changes here. The finding narrows what “non-scalar global assembly” must mean: a successful vector route must preserve genuinely joint information that cannot be reduced to valid affine scalarizations on the same deterministic witness class, or must add information that excludes the witness.

## 1. Vector-valued local state and affine dual channels

Fix a block size `m>=2`. For an ordered `m`-point Montgomery--Taylor translation Gram block `B`, retain

\[
D(B)=\operatorname{tr}\Psi(G_B)
\]

as in WI-011--WI-176. Let

\[
U(B)\in V
\]

be an arbitrary translation-covariant local observable taking values in a finite-dimensional real vector space `V`. Its coordinates may encode several source-conditioned gap statistics, several local pressure ledgers, several pair-interaction rows, or any other additive block data. No positivity or linearity of the map `B\mapsto U(B)` is assumed.

Let `Theta` be any index set of affine dual channels. For `theta in Theta`, choose a linear functional

\[
\ell_\theta\in V^*
\]

and suppose a universal local theorem proves

\[
\boxed{
D(B)+\ell_\theta(U(B))\ge C_\theta
}
\tag{1}
\]

for every block in the intended deterministic source class.

Suppose the shifted/global assembly controls the same direction by a universal pre-division tax

\[
\boxed{
\sum_i \ell_\theta(U(B_i))
\le \tau_\theta N+o(N)
}
\tag{2}
\]

and otherwise uses the same stable rank--trace bridge as WI-176, producing

\[
\boxed{
R_\theta
=
\frac{mH_{\rm MT}-\tau_\theta}{m-C_\theta},
\qquad C_\theta<m,
\qquad mH_{\rm MT}-\tau_\theta>0.
}
\tag{3}
\]

The theorem below does not require `Theta` to be finite. It applies pointwise to every affine direction for which (1)--(3) are valid on the same deterministic class.

## 2. The period-33 witness gives one vector rotation point

Use the interval-certified positive periodic Montgomery--Taylor configuration of WI-019/WI-026. Its retained density is

\[
r=\frac{67361}{100000}=0.67361,
\tag{4}
\]

its full directed pair-energy per retained atom obeys

\[
d<d_*:=
\frac{1637}{10^6}
+
\frac{45379580714321}{74507812500000000000},
\tag{5}
\]

and WI-026/WI-176 record

\[
H_{\rm MT}<H_*:=\frac{672500704}{10^9}
\tag{6}
\]

with exact margin

\[
\delta:=r(1-d_*)-H_*
=
\frac{46091743024440123119}
{7450781250000000000000000}
>\frac6{10^6}.
\tag{7}
\]

Cut the periodic configuration at each of its `33` phases. Write `B_a` for the resulting `m`-point block and define the phase-average vector

\[
\bar U:=\frac1{33}\sum_{a=1}^{33}U(B_a)\in V.
\tag{8}
\]

WI-026's positive-energy argument is independent of every auxiliary source observable and gives

\[
\frac1{33}\sum_{a=1}^{33}D(B_a)<md_*.
\tag{9}
\]

Average (1) over all phases. Linearity is used only in the dual functional, not in `U` itself:

\[
C_\theta
<md_*+\ell_\theta(\bar U).
\tag{10}
\]

The global tax (2) must also be valid on this same periodic deterministic source configuration. There are asymptotically `rN` retained blocks per ambient normalization, and their phase distribution is uniform, hence

\[
\boxed{
\tau_\theta\ge r\,\ell_\theta(\bar U).
}
\tag{11}
\]

Thus the entire vector state enters the witness test only through the single directional number `ell_theta(bar U)`, and that number appears once as local credit and once as global cost.

## 3. Exact directional cancellation

Subtract (3) from the witness density. Since `m-C_theta>0`,

\[
\begin{aligned}
r-R_\theta
&=
\frac{m(r-H_{\rm MT})-rC_\theta+\tau_\theta}
     {m-C_\theta}.
\end{aligned}
\tag{12}
\]

Insert (10), (11), and `H_MT<H_*`:

\[
\begin{aligned}
m(r-H_{\rm MT})-rC_\theta+\tau_\theta
&>
 m(r-H_*)
-r\bigl(md_*+\ell_\theta(\bar U)\bigr)
+\tau_\theta\\
&\ge
m\bigl(r(1-d_*)-H_*\bigr)\\
&=m\delta.
\end{aligned}
\tag{13}
\]

Therefore every valid affine channel satisfies

\[
\boxed{
r-R_\theta>
\frac{m\delta}{m-C_\theta}>0.
}
\tag{14}
\]

In particular,

\[
\boxed{R_\theta<0.67361.}
\tag{15}
\]

If the local floor lies in the standard nonnegative regime `0<=C_theta<m`, then `m/(m-C_theta)>=1`, so (7) strengthens (14) uniformly to

\[
\boxed{
R_\theta<r-\delta<0.673604.
}
\tag{16}
\]

The cancellation is independent of the dimension of `V`, the number of coordinates, the nonlinear way in which a block produces `U(B)`, and the chosen dual direction.

## 4. Support-function optimization does not escape

Suppose the proof retains the full vector `U` until the end and then optimizes over a family of affine directions, for example

\[
R_{\rm supp}:=\sup_{\theta\in\Theta}R_\theta.
\tag{17}
\]

Equation (15) is pointwise and has the same witness for every direction. Hence no support-function optimization can cross the witness density. In the nonnegative-floor regime, the margin in (16) is uniform, so even an infinite family satisfies

\[
\boxed{
R_{\rm supp}\le 0.673604.
}
\tag{18}
\]

This is stronger than saying that one scalar potential fails. The vector may be retained exactly through all local manipulations; what kills the gain is that the final global theorem asks only affine questions of its invariant average.

There is an equivalent rotation-set interpretation. The period-33 orbit defines the rotation vector `bar U`. Any affine inequality that is universal for the same source class must contain this point. Optimizing supporting hyperplanes can expose a face of the convex set of allowed averages, but it cannot separate a point that the source class actually realizes.

## 5. Finite positive LP/conic dual combinations reduce to one channel

The same obstruction covers a common apparently more joint construction. Suppose one has finitely many local affine certificates

\[
D(B)+\ell_j(U(B))\ge C_j
\qquad(1\le j\le J)
\tag{19}
\]

and combines them with nonnegative dual multipliers `mu_j`, not all zero. Put

\[
M:=\sum_j\mu_j>0,
\qquad
\ell:=\frac1M\sum_j\mu_j\ell_j,
\qquad
C:=\frac1M\sum_j\mu_jC_j.
\tag{20}
\]

Dividing the positive combination of (19) by `M` gives exactly

\[
D(B)+\ell(U(B))\ge C.
\tag{21}
\]

Any valid global affine accounting for that combined dual direction must, on the period-33 witness, pay at least `r ell(bar U)`. Thus (21) is already an instance of Sections 1--3.

Consequently, a finite-dimensional linear-program or conic-dual assembly built only from additive vector statistics and universal affine constraints cannot evade the witness merely because several coordinates are kept simultaneously. Weak duality collapses each final dual certificate to an affine direction, and the witness is a feasible primal test for that direction.

This statement does **not** claim that every possible vector-valued proof is an LP. It closes the large subclass in which jointness survives only as affine/support-function dualization.

## 6. What remains genuinely outside the theorem

The distinction sharpens the current `CLUE-kernel-constrained-positive-cover-escape` frontier. A successful non-scalar source argument must break at least one load-bearing hypothesis above.

A genuinely joint nonlinear constraint on the invariant vector can escape if it is not implied by affine taxes valid on the period-33 class and, in particular, if it excludes the witness rotation point or a neighborhood required by near-extremizers. A vector of several profiles can also escape if their **joint arithmetic/source realization** is stronger than separate additive ledgers and the period-33 configuration is not admissible for that joint object. Coupling to the exceptional indefinite block is outside the theorem because the witness models only the retained positive MT Gram interface. A zeta-specific spacing, correlation, multiplicity, or support theorem that the periodic configuration does not satisfy also invalidates (11) and is a genuine new input.

Conversely, merely introducing more coordinates, delaying scalarization, choosing the best affine direction after seeing the source state, using finitely many positive dual multipliers, or replacing a scalar tax by the support function of a vector tax set does not by itself constitute an escape. If the resulting proof can be written as (1)--(3) for its final dual direction, the cancellation above applies.

This also explains why WI-176's phrase “vector/state-resolved observable” needs a stronger reading. **The useful information must remain joint beyond affine dual consumption**, not merely be stored in a vector before the final scalar certificate is selected.

## 7. Prior-art and novelty audit

The convex framework is classical. Krystyna Ziemian, *Rotation sets for subshifts of finite type*, Fundamenta Mathematicae 146 (1995), 189--201, DOI `10.4064/fm-146-2-189-201`, studies vector observables and rotation sets; for the finite-type/local setting considered there the rotation set is a convex polyhedron and periodic rotation vectors are dense. Oliver Jenkinson, *Ergodic Optimization*, DCDS 15 (2006), 197--224, DOI `10.3934/dcds.2006.15.197`, treats optimization of invariant scalar averages. The reduction of positive LP dual combinations to one affine functional is ordinary weak duality/convex analysis. None of that abstract machinery is claimed as new.

The closest Mathia predecessors are distinct in scope. WI-156 closes adaptive portfolios of separately valid scalar Lamzouri censuses at the Montgomery--Taylor one-delta barrier. WI-165 closes positive mixtures of already scalarized fixed-block bounds by the weighted-mediant identity. WI-176 closes one arbitrary scalar local potential under a universal scalar tax. The present result uses the certified WI-019 period-33 source witness to show that **an arbitrary finite-dimensional additive state remains capped even if scalarization is postponed, provided the eventual global use is affine/support-functional**.

A targeted literature audit around rotation sets, ergodic optimization, support functions, and recent zeta multi-profile/block constructions found the classical convex principles above but no source-specific theorem identified here as a novelty claim. The durable point is the route classification for the current Weil-inertia program, not priority for the abstract convex observation.

## 8. Consequence for the research line

WI-172 proved that genuine Montgomery--Taylor source coupling contains information beyond the arbitrary positive-cover relaxation, while WI-174--WI-176 progressively removed fixed-constant squeezing and scalar pressure retuning as scalable escapes. The next frontier cannot be described merely as “retain a vector instead of a scalar.”

The decisive test is now stricter: exhibit a joint source invariant whose global admissible set excludes the WI-019 rotation point in a way not representable as affine taxes valid on that same point, or couple the retained source geometry to information absent from the collapsed single-profile witness. Without such a separation, affine dual optimization inherits the period-33 ceiling exactly.