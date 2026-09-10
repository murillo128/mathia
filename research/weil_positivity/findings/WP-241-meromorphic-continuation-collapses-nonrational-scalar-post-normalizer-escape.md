# WP-241 — Meromorphic continuation collapses the nonrational scalar post-normalizer escape

**Status:** `EXACT-DERIVED + MEROMORPHIC-COMPOSITION-RIGIDITY + TRANSCENDENTAL-SCALAR-NO-GO + DIVISOR-FIDELITY-CLASSIFICATION + MATCHED-SCALAR-CONTROL + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-240` classifies fixed **rational** postprocessors of the already-formed scalar scattering normalizer. A monomial retains the complete logarithmic derivative `m'/m` with one common integer multiplicity, while a nonmonomial rational function introduces divisor points on finite nonzero level sets `m(s)=a`. That finding deliberately leaves nonrational scalar functional calculus open.

For the meromorphic/divisor channel relevant to an ordinary explicit-formula argument, that remaining scalar escape closes almost completely. Let `X` be a Riemann surface and let

\[
m:X\longrightarrow \widehat{\mathbb C}
\tag{1}
\]

be a nonconstant meromorphic scalar normalizer having at least one zero and at least one pole. Let

\[
F:\mathbb C^*\longrightarrow \widehat{\mathbb C}
\tag{2}
\]

be a fixed nonzero meromorphic postprocessor. Assume that `F(m(s))`, initially defined away from zeros and poles of `m`, is required to extend **meromorphically through both kinds of divisor point** so that its logarithmic derivative remains in the ordinary meromorphic divisor/argument-principle category.

Then

\[
\boxed{F\text{ must be rational.}}
\tag{3}
\]

Indeed, meromorphic extendability of `F\circ m` through a zero of `m` forces the isolated singularity of `F` at `0` to be nonessential, while extendability through a pole of `m` forces the isolated singularity of `F` at `\infty` to be nonessential. Hence `F` extends meromorphically to the Riemann sphere and is rational.

Combining (3) with `WP-240` gives a complete trichotomy for one-variable meromorphic scalar postprocessing:

1. a **nonrational** meromorphic `F` has an essential singularity at `0` or `\infty`, so `F\circ m` acquires an essential singularity at a corresponding original zero or pole of `m` and leaves the meromorphic divisor framework;
2. a **rational nonmonomial** `F` remains meromorphic but introduces finite nonzero level-set divisors and is not divisor-faithful under the scalar-normalizer matched control of `WP-240`;
3. a **monomial** `F(z)=c z^k` is meromorphic and divisor-faithful, but

\[
\frac{d}{ds}\log F(m(s))=k\frac{m'(s)}{m(s)},
\tag{4}
\]

so it transports the entire completed zero/prime/Gamma/polar package without separating its constituents.

Thus a fixed scalar postprocessor cannot evade the central-normalizer obstruction merely by replacing rational functional calculus with a transcendental meromorphic function. To stay in the same meromorphic explicit-formula channel it falls back into `WP-240`; to remain genuinely nonrational it must abandon ordinary divisor meromorphicity at an original zero or pole. Any positivity theorem for such a transcendental boundary transform would therefore need a **new analytic bridge**, not just the standard logarithmic-derivative/divisor mechanism.

## 1. Local lemma at a zero: essential singularities survive ramified composition

Let `x_0\in X` be a zero of `m` of order `r\ge1`. In a local coordinate `t` centered at `x_0`,

\[
m(t)=t^r u(t),\qquad u(0)\ne0.
\tag{5}
\]

After shrinking the coordinate disk, choose a holomorphic `r`-th root of the nonvanishing unit `u`. Replacing `t` by the local coordinate

\[
w=t\,u(t)^{1/r}
\tag{6}
\]

gives

\[
m=w^r.
\tag{7}
\]

Because `F` is meromorphic on `\mathbb C^*`, its only possible obstruction at `0` is an isolated removable singularity, a pole, or an essential singularity. If `0` is essential, its Laurent expansion contains infinitely many negative powers,

\[
F(z)=\sum_{n=-\infty}^{\infty}a_n z^n
\tag{8}
\]

with infinitely many nonzero `a_n` for `n<0`. Composition with (7) gives

\[
F(m(w))=F(w^r)=\sum_{n=-\infty}^{\infty}a_n w^{rn}.
\tag{9}
\]

The negative exponents remain infinite in number and remain distinct. Hence `w=0` is an essential singularity of `F\circ m`; ramification cannot turn it into a pole or removable point.

Therefore

\[
\boxed{
F\circ m\text{ meromorphic through a zero of }m
\Longrightarrow
F\text{ is meromorphic at }0.
}
\tag{10}
\]

No value-distribution theorem is being used here. The statement is purely local and survives arbitrary zero multiplicity.

## 2. Local lemma at a pole

Let `x_\infty` be a pole of `m` of order `q\ge1`. Then

\[
n:=\frac1m
\tag{11}
\]

has a zero of order `q`. Put

\[
G(z):=F(1/z).
\tag{12}
\]

Near `x_\infty`,

\[
F(m)=G(n).
\tag{13}
\]

Applying the zero lemma to `n` shows that meromorphic continuation of `F\circ m` through `x_\infty` forces `G` to be meromorphic at `0`, equivalently `F` to be meromorphic at `\infty`. Thus

\[
\boxed{
F\circ m\text{ meromorphic through a pole of }m
\Longrightarrow
F\text{ is meromorphic at }\infty.
}
\tag{14}
\]

Again an essential singularity cannot be hidden by the finite ramification of the pole.

## 3. Meromorphic continuation through one zero and one pole forces rationality

Equations (10) and (14) show that if `m` has one zero and one pole and `F\circ m` is meromorphic through both, then `F` is meromorphic not only on `\mathbb C^*` but also at `0` and `\infty`. Hence it extends to a meromorphic function

\[
F:\widehat{\mathbb C}\longrightarrow\widehat{\mathbb C}.
\tag{15}
\]

Every meromorphic function on the compact Riemann sphere is rational. Therefore (3) follows.

The converse at the level of meromorphicity is immediate: rational `F` composed with meromorphic `m` is meromorphic. What rationality does **not** guarantee is preservation of the original divisor. That is precisely the distinction classified by `WP-240`.

This gives a useful exact boundary:

\[
\boxed{
\begin{array}{c}
\text{fixed scalar postprocessing}\\
+\ \text{ordinary meromorphic continuation across }\operatorname{div}(m)
\end{array}
\Longrightarrow
\text{rational scalar postprocessing}.
}
\tag{16}
\]

The statement is stronger than a growth heuristic. No finite-order, Hardy-space, bounded-characteristic, or asymptotic assumption is needed; meromorphic continuation through both endpoint fibers already forces the collapse.

## 4. Adding divisor fidelity leaves only characters of the multiplicative scalar

Once `F` is rational, `WP-240` applies exactly. If the divisor of `F` on the sphere is supported only at `0` and `\infty`, then

\[
F(z)=c z^k,
\qquad c\ne0,\quad k\in\mathbb Z.
\tag{17}
\]

Otherwise `F` has a zero or pole at some finite nonzero value `a`. Wherever `m(s)=a`, the divisor of `F(m(s))` contains a corresponding point. More importantly for source independence, fix any regular point `s_0` with

\[
m(s_0)\ne0,\infty,
\qquad m'(s_0)\ne0,
\tag{18}
\]

and replace the scalar normalizer by

\[
\widetilde m=c_0m,
\qquad
c_0=\frac{a}{m(s_0)}.
\tag{19}
\]

Then

\[
\operatorname{div}(\widetilde m)=\operatorname{div}(m),
\tag{20}
\]

but `F(\widetilde m)` has a zero or pole at `s_0`. Hence a rational nonmonomial reads a chosen scalar-value coordinate rather than only the original divisor.

Consequently, among fixed one-variable scalar postprocessors that satisfy both

- meromorphic continuation across the original zero and pole fibers; and
- divisor fidelity stable under the algebraic scalar-normalizer control (19),

the only possibilities are the multiplicative characters (17). Their logarithmic derivatives obey (4), so no independent weighting of zeros, finite primes, Gamma terms, or poles appears.

This is the scalar analogue of a rigidity statement: **preserving the meromorphic divisor channel forces the postprocessor back to a character of `\mathbb C^*`.**

## 5. The zero-free entire escape from WP-240 fails exactly at the pole fiber

`WP-240` correctly left functions such as

\[
F(z)=e^{G(z)}
\tag{21}
\]

outside its rational theorem. They can be zero-free, so they need not create finite level-set zeros or poles. That fact alone looked like a possible escape from the rational divisor dichotomy.

The continuation test identifies the cost exactly. If `G` is a nonconstant polynomial, then `F` is entire and zero-free, but `\infty` is an essential singularity of `F`. Therefore `e^{G(m(s))}` has an essential singularity at every pole of `m` of the corresponding local type. In particular,

\[
F(z)=e^z
\tag{22}
\]

is harmless at zeros of `m` but becomes essential at poles of `m`.

Conversely,

\[
F(z)=e^{1/z}
\tag{23}
\]

is harmless at poles of `m` after the reciprocal variable is taken, but is essential at zeros of `m`. More general transcendental meromorphic functions on `\mathbb C^*` may place their essential singularity at one or both endpoints, but if they are genuinely nonrational they must place one somewhere. Because the zeta scattering normalizer has both zero and pole fibers, one endpoint is inevitably encountered.

The conclusion is not that such transforms are meaningless. Their boundary values may have useful positivity, contractivity, Herglotz, or passivity properties. The conclusion is that the transformed object no longer belongs to the same global meromorphic-divisor category from which the ordinary zero-sum explicit formula is extracted.

## 6. Application to the scalar zeta scattering normalizer

In the `SL(2)` specialization audited in `WP-237`--`WP-240`, Wong's scalar factor can be written, in his parameter normalization, as

\[
m(s)=\frac{\xi(s)}{\xi(1+s)}.
\tag{24}
\]

The only property needed here is that this meromorphic function has both zeros and poles. If `\rho` is a nontrivial zero of the completed zeta function, then the numerator produces a zero at `s=\rho`, while the shifted denominator produces a pole at `s=\rho-1`; these lie in disjoint real strips, so the local zero/pole test does not require RH.

The continuous spectral explicit formula uses the logarithmic derivative of this scalar factor. If a fixed scalar transform `F(m)` is to remain a meromorphic scattering normalizer to which the same ordinary divisor/logarithmic-derivative machinery applies across those fibers, Section 3 forces `F` to be rational. Section 4 then imports the `WP-240` dichotomy.

Therefore the complete fixed scalar-meromorphic route is

\[
\boxed{
\begin{array}{rcl}
F\text{ nonrational}
&\Longrightarrow&
F(m)\text{ essential at an original zero or pole fiber},\\[2mm]
F\text{ rational nonmonomial}
&\Longrightarrow&
\text{finite nonzero level-set divisor sensitivity},\\[2mm]
F(z)=cz^k
&\Longrightarrow&
k\,m'/m\text{ with the whole completed package intact}.
\end{array}
}
\tag{25}
\]

No branch of (25) supplies the missing Weil orientation from scalar postprocessing alone.

## 7. Why an essential singularity is a real bridge failure, not merely a cosmetic analytic defect

The ordinary explicit-formula divisor mechanism depends on a meromorphic logarithmic differential: zeros and poles contribute isolated logarithmic singularities with integer residues, and contour deformation converts those residues into evaluations of the common test function on the divisor.

At an essential singularity there is no finite zero/pole order to insert into that divisor calculus. Even when a formally differentiated expression such as

\[
\frac{d}{ds}\log e^{G(m(s))}=G'(m(s))m'(s)
\tag{26}
\]

can be written on a punctured domain, it need not have only logarithmic singularities. For example, `G(z)=z` turns a simple pole of `m` into a higher-order pole of the differential (26); more general essential behavior can produce an essential singularity. Such terms pair with derivatives or more complicated local data of a test function rather than with the original divisor multiplicity alone.

Thus one cannot claim that a positive transcendental transform has produced the Weil zero form merely because it is a function of the same scalar scattering coefficient. A new theorem would have to show, with its own domain and test class, how the nonmeromorphic or higher-jet boundary contribution cancels or reorganizes into exactly the original Weil functional. That theorem would be genuinely new analytic structure and is not inherited from scalar functional calculus.

## 8. Aggressive falsification and exact scope

**Could a nonrational `F` be meromorphic on `\mathbb C^*` and nevertheless have only poles/removable singularities at both `0` and `\infty`?** No. It would then extend meromorphically to the sphere and hence be rational. This is exactly why at least one essential endpoint is unavoidable.

**Could ramification of a high-multiplicity zero or pole of `m` remove the essential singularity?** No. Equation (9) multiplies every Laurent exponent by the positive integer ramification order; infinitely many negative powers remain infinitely many negative powers.

**Could the actual zeta normalizer avoid the bad endpoint?** No for this continuation test: it has both zero and pole fibers. The argument does not require the scalar normalizer to attain arbitrary finite values and therefore is stronger, on the nonrational branch, than the level-set matched control used for rational nonmonomials.

**Does this prove that every nonrational boundary transform is unusable?** No. A transform defined only on the unitary axis, in a Hardy/Smirnov boundary class, as a Borel functional calculus, or as a distributional object may be mathematically canonical and positive. It simply no longer inherits the ordinary meromorphic divisor explicit formula. It must supply a separate continuation/distribution theorem and a separate bridge to the full Weil test class.

**Does this cover multivalued transforms such as a chosen logarithm or fractional power?** No. They are not single-valued meromorphic functions on `\mathbb C^*`. A source-forced covering space, line bundle, monodromy rule, or branch choice could be additional geometry. An arbitrary branch selected to obtain the desired sign would fail the mandate's canonicity test.

**Does this cover genuinely operator-valued functional calculus?** Only when the construction actually reduces to one scalar meromorphic function `F(m)`. A Fredholm determinant, matrix normalizer, noncommuting finite--archimedean coupling, or infinite-dimensional response can contain additional spectral data. If after determinant/scalarization it is literally a fixed meromorphic function of the one scalar `m`, (25) applies; otherwise the added operator structure must be audited on its own merits.

**Could higher-order poles in (26) still disappear after contour integration?** Some exact derivatives can have zero residue, but Weil's explicit formula is paired with nonconstant admissible test functions. Higher jets then contribute test derivatives or boundary terms rather than the original divisor evaluation. An exact cancellation for the full test class would require an additional identity. This finding does not preclude such an identity; it refuses to count it as automatic divisor fidelity.

**Does the algebraic control `m\mapsto c_0m` represent a physical unitary scattering system?** Not necessarily, as already stated in `WP-240`. It is used only on the rational branch to distinguish divisor information from scalar-value-coordinate dependence. The nonrational-to-rational collapse in Sections 1--3 does not use that control at all.

## 9. Prior art and novelty boundary

No historical novelty is claimed for the complex-analysis ingredients. The classification of isolated singularities, Laurent expansion under finite ramified composition, and the theorem that meromorphic functions on the Riemann sphere are rational are standard textbook facts. The logarithmic-derivative/divisor correspondence is likewise classical. A bounded literature audit found the expected general complex-analysis statements and no reason to present (3) as a new theorem about meromorphic functions.

The automorphic input is also not new here. Wong's `SL(2)` explicit-formula calculation and the scalar completed-`L` normalizer have already been audited in `WP-237`--`WP-240` and anchored in `SOURCES.md` through those findings.

The Mathia-specific delta is the **closure of an explicitly surviving research escape**. `WP-240` left zero-free entire and more general nonrational scalar transforms outside its rational divisor theorem. The local continuation lemma shows that this freedom is incompatible with retaining the same meromorphic normalizer category once the source scalar has both zeros and poles. Combining that elementary fact with the already-persisted rational classification yields the complete trichotomy (25).

Searches around nonlinear/Cayley/scattering postprocessing did not identify a prior result whose mathematical content is the present Weil-routing conclusion. That absence is not treated as evidence of historical novelty; the durable claim is only the exact Mathia-specific narrowing obtained from classical ingredients.

## 10. Consequence for the research line

The scalar post-normalizer frontier is now substantially closed. `WP-238` rules out fixed channel projection after central scalarization, `WP-239` rules out scalar-homogeneous moving and zero-shift Schur reductions, `WP-240` rules out divisor-faithful rational nonhomogeneity, and the present result shows that **nonrational meromorphic scalar postprocessing cannot preserve the meromorphic explicit-formula channel at both zero and pole fibers**.

Accordingly, merely choosing a more sophisticated one-variable scalar function is no longer a credible route to the missing sign. A surviving mechanism must add structure that is genuinely outside this classification: a matrix-valued arithmetic normalizer, noncommuting or all-orders mixed-prime information before scalarization, a source-forced finite--archimedean pairing, a canonical covering/monodromy object, or a boundary/distributional construction equipped with a new theorem that reconstructs the full Weil functional from its nonmeromorphic response.

The preferred frontier remains the one isolated by the local `mind`: derive the all-orders/global coupling **before** the arithmetic and archimedean information has collapsed into a single scalar normalizer. The present result does not prove positivity or RH; it prevents transcendental scalar postprocessing from being mistaken for that missing geometric operation.
