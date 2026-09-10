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
\boxed{F\text{ extends meromorphically to }0\text{ and }\infty,\text{ hence }F\text{ is rational.}}
\tag{3}
\]

The local statement is slightly stronger than the usual essential-singularity slogan. A meromorphic function on `\mathbb C^*` may have poles accumulating at `0` or `\infty`, so an endpoint need not initially be an isolated holomorphic singularity. But such accumulating poles pull back under the finite local ramification of a zero or pole of `m` and would accumulate at the corresponding point of `X`, which is incompatible with a meromorphic continuation of `F\circ m`. Once pole accumulation is excluded, any remaining essential isolated singularity survives ramified composition by its Laurent series. Thus continuation of the composition forces an ordinary removable singularity or pole of `F` at each endpoint.

Combining (3) with `WP-240` gives a complete trichotomy for one-variable meromorphic scalar postprocessing:

1. a **nonrational** meromorphic `F` fails to extend meromorphically at `0` or `\infty`, so `F\circ m` fails meromorphic continuation at a corresponding original zero or pole of `m`;
2. a **rational nonmonomial** `F` remains meromorphic but introduces finite nonzero level-set divisors and is not divisor-faithful under the scalar-normalizer matched control of `WP-240`;
3. a **monomial** `F(z)=c z^k` is meromorphic and divisor-faithful, but

\[
\frac{d}{ds}\log F(m(s))=k\frac{m'(s)}{m(s)},
\tag{4}
\]

so it transports the entire completed zero/prime/Gamma/polar package without separating its constituents.

Thus a fixed scalar postprocessor cannot evade the central-normalizer obstruction merely by replacing rational functional calculus with a transcendental meromorphic function. To stay in the same meromorphic explicit-formula channel it falls back into `WP-240`; to remain genuinely nonrational it must abandon ordinary meromorphic continuation at an original zero or pole. Any positivity theorem for such a transcendental boundary transform would therefore need a **new analytic bridge**, not just the standard logarithmic-derivative/divisor mechanism.

## 1. Local continuation at a zero forces meromorphicity of the postprocessor at zero

Let `x_0\in X` be a zero of `m` of order `r\ge1`. In a local coordinate `t` centered at `x_0`,

\[
m(t)=t^r u(t),\qquad u(0)\ne0.
\tag{5}
\]

After shrinking the coordinate disk, choose a holomorphic `r`-th root of the nonvanishing unit `u`. Replacing `t` by

\[
w=t\,u(t)^{1/r}
\tag{6}
\]

gives a local coordinate in which

\[
m=w^r.
\tag{7}
\]

There are two ways in which a meromorphic function on `\mathbb C^*` can fail to extend meromorphically at `0`.

First, poles of `F` may accumulate at `0`. Suppose `a_j\to0` are distinct poles. For every sufficiently large `j`, choose an `r`-th root `w_j` of `a_j` in the local disk. Then `w_j\to0`, and (7) shows that every `w_j` is a pole of `F(m(w))`. Hence poles of `F\circ m` accumulate at `x_0`; no meromorphic continuation through `x_0` is possible.

Therefore meromorphic continuation of `F\circ m` forces the existence of a punctured disk `0<|z|<\varepsilon` containing no poles of `F`. On that punctured disk `F` is holomorphic, so `0` becomes an ordinary isolated singularity. If it is essential, its Laurent expansion has infinitely many negative terms,

\[
F(z)=\sum_{n=-\infty}^{\infty}a_n z^n,
\tag{8}
\]

and composition with (7) gives

\[
F(m(w))=F(w^r)=\sum_{n=-\infty}^{\infty}a_n w^{rn}.
\tag{9}
\]

Infinitely many negative exponents remain and remain distinct, so `w=0` is essential for the composition. Thus the essential case is also impossible.

The only remaining possibilities are a removable singularity or a pole of `F` at `0`. Equivalently,

\[
\boxed{
F\circ m\text{ meromorphic through a zero of }m
\Longrightarrow
F\text{ extends meromorphically to }0.
}
\tag{10}
\]

This is purely local and survives arbitrary zero multiplicity.

## 2. Local continuation at a pole forces meromorphicity at infinity

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

Applying Section 1 to `G\circ n` shows that meromorphic continuation of `F\circ m` through `x_\infty` forces `G` to extend meromorphically to `0`. This is exactly the statement that `F` extends meromorphically to `\infty`. In particular, poles of `F` accumulating toward infinity would pull back to poles accumulating at `x_\infty`, and an isolated essential singularity at infinity would survive the finite ramification.

Hence

\[
\boxed{
F\circ m\text{ meromorphic through a pole of }m
\Longrightarrow
F\text{ extends meromorphically to }\infty.
}
\tag{14}
\]

## 3. One zero and one pole collapse the scalar postprocessor to rational calculus

If `m` has at least one zero and one pole and `F\circ m` extends meromorphically through both, equations (10) and (14) show that `F` is meromorphic not only on `\mathbb C^*` but also at `0` and `\infty`. Hence it extends to a meromorphic function

\[
F:\widehat{\mathbb C}\longrightarrow\widehat{\mathbb C}.
\tag{15}
\]

Every meromorphic function on the compact Riemann sphere is rational, proving (3). Conversely, rational `F` composed with meromorphic `m` is meromorphic. What rationality does **not** guarantee is preservation of the original divisor; that is the distinction already classified by `WP-240`.

Thus

\[
\boxed{
\begin{array}{c}
\text{fixed scalar postprocessing}\\
+\ \text{meromorphic continuation across a zero and a pole of }m
\end{array}
\Longrightarrow
\text{rational scalar postprocessing}.
}
\tag{16}
\]

No finite-order, Hardy-space, bounded-characteristic, or asymptotic assumption is needed. The obstruction occurs before any positivity estimate: it is forced by the analytic category required for the usual divisor/logarithmic-derivative explicit formula.

## 4. Adding divisor fidelity leaves only multiplicative characters

Once `F` is rational, `WP-240` applies exactly. If the divisor of `F` on the sphere is supported only at `0` and `\infty`, then

\[
F(z)=c z^k,
\qquad c\ne0,\quad k\in\mathbb Z.
\tag{17}
\]

Otherwise `F` has a zero or pole at some finite nonzero value `a`. Wherever `m(s)=a`, the divisor of `F(m(s))` contains the corresponding pullback point. More importantly for source independence, fix any regular point `s_0` with

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

Consequently, among fixed one-variable scalar postprocessors satisfying both meromorphic continuation across the original zero/pole fibers and divisor fidelity stable under the algebraic scalar-normalizer control (19), the only possibilities are the characters (17). Their logarithmic derivatives obey (4), so no independent weighting of zeros, finite primes, Gamma terms, or poles appears.

## 5. The zero-free entire escape from WP-240 fails at the pole fiber

`WP-240` correctly left functions such as

\[
F(z)=e^{G(z)}
\tag{21}
\]

outside its rational theorem. They can be zero-free, so they need not create finite level-set zeros or poles. The continuation test identifies the exact cost.

If `G` is a nonconstant polynomial, `F` is entire and zero-free but has an essential singularity at `\infty`. Therefore `e^{G(m(s))}` has an essential singularity at every pole of `m`. In particular,

\[
F(z)=e^z
\tag{22}
\]

is harmless at zeros of `m` but becomes essential at poles of `m`. Conversely,

\[
F(z)=e^{1/z}
\tag{23}
\]

is harmless at the infinity endpoint but essential at zero, so it fails at zeros of `m`.

More general transcendental meromorphic functions on `\mathbb C^*` may also have poles accumulating at an endpoint rather than an isolated holomorphic essential singularity. Section 1 shows that this does not help: the accumulating poles are inherited by the composition. Any genuinely nonrational meromorphic `F` must fail meromorphic extension at at least one endpoint, because extension at both would make it rational.

The conclusion is not that such transforms are meaningless. Their boundary values may have useful positivity, contractivity, Herglotz, or passivity properties. The conclusion is that the transformed object no longer belongs to the same global meromorphic-divisor category from which the ordinary zero-sum explicit formula is extracted.

## 6. Application to the scalar zeta scattering normalizer

In the `SL(2)` specialization audited in `WP-237`--`WP-240`, Wong's scalar factor can be written, in his parameter normalization, as

\[
m(s)=\frac{\xi(s)}{\xi(1+s)}.
\tag{24}
\]

The only property needed here is that this meromorphic function has both zeros and poles. If `\rho` is a nontrivial zero of the completed zeta function, the numerator produces a zero at `s=\rho`, while the shifted denominator produces a pole at `s=\rho-1`; these lie in disjoint real strips, so the local zero/pole test does not require RH.

The continuous spectral explicit formula uses the logarithmic derivative of this scalar factor. If a fixed scalar transform `F(m)` is to remain a meromorphic scattering normalizer to which the same ordinary divisor/logarithmic-derivative machinery applies across those fibers, Section 3 forces `F` to be rational. Section 4 then imports the `WP-240` dichotomy.

Therefore the complete fixed scalar-meromorphic route is

\[
\boxed{
\begin{array}{rcl}
F\text{ nonrational}
&\Longrightarrow&
F(m)\text{ fails meromorphic continuation at an original zero or pole fiber},\\[2mm]
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

## 7. Failure of meromorphic continuation is a real bridge failure

The ordinary explicit-formula divisor mechanism depends on a meromorphic logarithmic differential: zeros and poles contribute isolated logarithmic singularities with integer residues, and contour deformation converts those residues into evaluations of the common test function on the divisor.

If `F(m)` is nonmeromorphic at an original divisor point, there is no finite zero/pole order for the transformed object there. Even when a formal punctured-domain identity such as

\[
\frac{d}{ds}\log e^{G(m(s))}=G'(m(s))m'(s)
\tag{26}
\]

is available, it need not have only logarithmic singularities. For example, `G(z)=z` turns a simple pole of `m` into a double pole of (26); more general endpoint behavior can be essential. Such terms pair with derivatives or more complicated local data of a test function rather than with the original divisor multiplicity alone.

Thus one cannot claim that a positive transcendental transform has produced the Weil zero form merely because it is a function of the same scalar scattering coefficient. A new theorem would have to show, with its own domain and test class, how the nonmeromorphic or higher-jet contribution cancels or reorganizes into exactly the original Weil functional. That theorem would be genuinely new analytic structure and is not inherited from scalar functional calculus.

## 8. Aggressive falsification and exact scope

**Could a nonrational `F` be meromorphic on `\mathbb C^*` and nevertheless extend meromorphically at both endpoints?** No. It would then be meromorphic on the sphere and hence rational.

**Could poles of `F` accumulate at an endpoint and evade the isolated-essential-singularity argument?** They evade the naive Laurent argument but not the theorem. Local surjectivity of `m=w^r` pulls those poles back to poles accumulating at the corresponding zero or pole of `m`, directly contradicting meromorphic continuation.

**Could ramification of a high-multiplicity zero or pole remove an isolated essential singularity?** No. Equation (9) multiplies each Laurent exponent by the positive ramification order; infinitely many negative powers remain infinitely many negative powers.

**Could the actual zeta normalizer avoid the bad endpoint?** No for this continuation test: it has both zero and pole fibers. The argument does not require the normalizer to attain arbitrary finite nonzero values and therefore does not use the matched scalar control on the nonrational branch.

**Does this prove that every nonrational boundary transform is unusable?** No. A transform defined only on the unitary axis, in a Hardy/Smirnov boundary class, by Borel functional calculus, or as a distributional response may be mathematically canonical and positive. It simply no longer inherits the ordinary meromorphic divisor explicit formula. It must supply a separate continuation/distribution theorem and a separate bridge to the full Weil test class.

**Does this cover multivalued transforms such as a logarithm or fractional power?** No. They are not single-valued meromorphic functions on `\mathbb C^*`. A source-forced covering space, line bundle, monodromy rule, or branch choice would be additional geometry. An arbitrary branch selected for the desired sign would fail the mandate's canonicity test.

**Does this cover genuinely operator-valued functional calculus?** Only when the construction actually scalarizes to one fixed meromorphic function `F(m)`. A Fredholm determinant, matrix normalizer, noncommuting finite--archimedean coupling, or infinite-dimensional response can contain additional spectral data. If its final response is literally a fixed meromorphic function of the one scalar `m`, (25) applies; otherwise the added structure must be audited separately.

**Could higher-order terms from (26) integrate away?** Some exact derivatives have zero residue, but the explicit formula is paired with nonconstant test functions. Higher-order poles produce test derivatives or boundary terms rather than the original divisor evaluation. A full-class cancellation identity could exist, but it would be an additional theorem, not automatic divisor fidelity.

**Does the algebraic control `m\mapsto c_0m` represent a physical unitary scattering system?** Not necessarily, as already stated in `WP-240`. It is used only on the rational branch to distinguish divisor information from scalar-value-coordinate dependence. The nonrational-to-rational collapse in Sections 1--3 does not use that control.

## 9. Prior art and novelty boundary

No historical novelty is claimed for the complex-analysis ingredients. The discreteness of poles of a meromorphic function, classification of isolated singularities, Laurent expansion under finite ramified composition, and the theorem that meromorphic functions on the Riemann sphere are rational are standard textbook facts. The logarithmic-derivative/divisor correspondence is likewise classical. A bounded literature audit found the expected general complex-analysis statements and no reason to present (3) as a new theorem about meromorphic functions.

The automorphic input is also not new here. Wong's `SL(2)` explicit-formula calculation and the scalar completed-`L` normalizer have already been audited in `WP-237`--`WP-240` and anchored in `SOURCES.md` through those findings.

The Mathia-specific delta is the **closure of an explicitly surviving research escape**. `WP-240` left zero-free entire and more general nonrational scalar transforms outside its rational divisor theorem. The local continuation lemma shows that this freedom is incompatible with retaining the same meromorphic normalizer category once the source scalar has both zeros and poles. Combining that fact with the already-persisted rational classification yields the complete trichotomy (25).

Searches around nonlinear/Cayley/scattering postprocessing did not identify a prior result whose mathematical content is the present Weil-routing conclusion. That absence is not treated as evidence of historical novelty; the durable claim is only the exact Mathia-specific narrowing obtained from classical ingredients.

## 10. Consequence for the research line

The scalar post-normalizer frontier is now substantially closed. `WP-238` rules out fixed channel projection after central scalarization, `WP-239` rules out scalar-homogeneous moving and zero-shift Schur reductions, `WP-240` rules out divisor-faithful rational nonhomogeneity, and the present result shows that **nonrational meromorphic scalar postprocessing cannot preserve the meromorphic explicit-formula channel at both zero and pole fibers**.

Accordingly, merely choosing a more sophisticated one-variable scalar function is no longer a credible route to the missing sign. A surviving mechanism must add structure genuinely outside this classification: a matrix-valued arithmetic normalizer, noncommuting or all-orders mixed-prime information before scalarization, a source-forced finite--archimedean pairing, a canonical covering/monodromy object, or a boundary/distributional construction equipped with a new theorem reconstructing the full Weil functional from its nonmeromorphic response.

The preferred frontier remains the one isolated by the local `mind`: derive the all-orders/global coupling **before** the arithmetic and archimedean information has collapsed into a single scalar normalizer. The present result does not prove positivity or RH; it prevents transcendental scalar postprocessing from being mistaken for that missing geometric operation.
