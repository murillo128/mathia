# MC-455 — Standard q-vdC conductor reduction preserves the coefficient product quotient

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `QVDC-CONDUCTOR-REDUCTION` · `PRODUCT-QUOTIENT-STABILITY` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-454` left a precise escape for one genuine well-factorable component: expose its internal convolution variables and carry them through the **first nontrivial analytic operation** before they recombine into the product divisors. The standard source-side `q`-van-der-Corput conductor reduction does not by itself realize that escape.

Let the internal coefficient labels be

\[
z=(r_1,r_2,r'_1,r'_2),
\qquad
\Pi(z)=(r_1r_2,r'_1r'_2)=(d,e).
\tag{1}
\]

For the shifted divisor-pair family of `MC-413`, write the incomplete translated source kernel abstractly as

\[
F_z(k)
=
\chi(k+U_{\Pi(z)}+A_{\Pi(z)})
\overline{\chi(k+U_{\Pi(z)})},
\qquad k\in I_{\Pi(z)}.
\tag{2}
\]

Here `U`, `A`, and the interval are determined by the product-level CRT data `(d,e)`; concretely `A\equiv h[d,e]^{-1}\pmod q` in the coprime regime of `MC-413`. Equation `(2)` is therefore already a pullback through `\Pi`.

Now factor the squarefree source conductor as

\[
q=q_0q_1,
\qquad (q_0,q_1)=1,
\qquad \chi=\chi_0\chi_1,
\tag{3}
\]

with primitive local characters, and perform the standard `A`-process shift

\[
S=q_1t.
\tag{4}
\]

Put `x=k+U_{\Pi(z)}`. Since the `q_1`-part is periodic under `(4)`, the exact differenced kernel is

\[
\boxed{
F_z(k+S)\overline{F_z(k)}
=
\mathbf 1_{(x(x+A_{\Pi(z)}),q_1)=1}
\,G_{q_0}(x;A_{\Pi(z)},S),
}
\tag{5}
\]

where

\[
G_{q_0}(x;A,S)
=
\chi_0(x+S+A)\overline{\chi_0(x+S)}
\overline{\chi_0(x+A)}\chi_0(x).
\tag{6}
\]

Thus the `A`-process performs a real analytic operation: it removes the `q_1` **oscillatory phase**, leaving only a `q_1` unit-support mask, while the residual character oscillation has conductor `q_0`. This is exactly the classical source-modulus reduction exploited by Heath-Brown/Irving.

But `(5)` also proves a separate structural fact relevant to the Mathia branch: every dependence on the internal coefficient labels still factors through

\[
z\longmapsto\Pi(z)=(d,e).
\tag{7}
\]

The new shift `S` is chosen from the source-conductor split, not from a representative of the multiplication fiber `\Pi^{-1}(d,e)`. Hence two internal factorizations with the same products `(d,e)` still produce the same support mask, residual phase, translated source start, and interval intersection after the `A`-process.

More generally, any finite sequence of standard source-variable `A`/`B` operations whose conductor splits, shifts, completions, and transform parameters are fixed independently of the internal factor representative preserves this quotient property. Fourier completion may introduce a new dual frequency and repeated differencing may lower the oscillatory conductor further, but neither operation can distinguish two points in the same multiplication fiber unless some parameter is made to depend separately on the internal coefficient variables.

Therefore **source-conductor factorization and coefficient well-factorability are distinct analytic resources at this stage**. Standard `q`-vdC can improve an individual incomplete source estimate by reducing its conductor, but that improvement is available already for the collapsed product-indexed kernel. It does not, by itself, turn the internal factor tuples of `lambda=alpha*beta` into new source-frame occupancy or a new post-Cauchy diagonal geometry.

This does not kill the conductor-factorization route. It sharpens its success condition: to couple conductor reduction to well-factorability, one must introduce a justified operation whose conductor split, shift family, congruence, dispersion variable, or transformed phase depends separately on the internal coefficient factors **before** the multiplication quotient is restored, or else derive a strong enough source-only conductor saving that the existing product-level occupancy tariff is beaten without using those internal factors at all.

No estimate for `M(x)`, no new character-sum exponent, and no RH consequence follows.

## 1. Exact first `A`-process factorization

Write

\[
F_z(k)=F_{0,z}(k)F_{1,z}(k),
\tag{8}
\]

with

\[
F_{i,z}(k)
=
\chi_i(k+U_{\Pi(z)}+A_{\Pi(z)})
\overline{\chi_i(k+U_{\Pi(z)})}.
\tag{9}
\]

Because `S=q_1t`,

\[
F_{1,z}(k+S)=F_{1,z}(k).
\tag{10}
\]

Therefore

\[
\begin{aligned}
F_z(k+S)\overline{F_z(k)}
&=
F_{0,z}(k+S)\overline{F_{0,z}(k)}
\,|F_{1,z}(k)|^2\\
&=
F_{0,z}(k+S)\overline{F_{0,z}(k)}
\,\mathbf 1_{(x(x+A_{\Pi(z)}),q_1)=1},
\end{aligned}
\tag{11}
\]

which is `(5)`--`(6)`. The only use of squarefreeness here is the clean primitive CRT factorization in `(3)`; the quotient statement itself is simply about how the parameter dependence enters.

The interval produced by van der Corput is an intersection such as

\[
I_{\Pi(z)}\cap(I_{\Pi(z)}-S),
\tag{12}
\]

so its dependence on `z` also continues to factor through `\Pi` when `S` is source-only. Thus the quotient preservation is not an artifact of suppressing the incomplete boundary.

If the residual factor is an odd prime `q_0=p`, then on units `(6)` can be written as the multiplicative-character phase

\[
\chi_0\!\left(
\frac{(x+S+A)x}{(x+S)(x+A)}
\right).
\tag{13}
\]

For `A\not\equiv0\pmod p` and `S\not\equiv0\pmod p`, the rational function in `(13)` is nonconstant and its divisor has a zero or pole of multiplicity not divisible by the order of the nontrivial character. The standard Weil bound therefore gives square-root cancellation for the corresponding complete prime-modulus sum, up to the usual bounded-degree constant. The degeneracies `A\equiv0` or `S\equiv0` are precisely cases in which the translated/differenced phase can collapse and must be separated rather than credited with generic cancellation.

This is a source-conductor gain, but its parameters remain product-level.

## 2. Pullback stability under source-only transforms

The preceding calculation is an instance of a simple general lemma.

Let `Z` be any coefficient-parameter space, let `Y` be its product-level quotient, and let

\[
\Pi:Z\to Y.
\tag{14}
\]

Suppose a family of source functions satisfies

\[
K_z=\widetilde K_{\Pi(z)}.
\tag{15}
\]

Let `T_\theta` be an operation acting on the source variable -- translation, conjugation/product differencing, restriction to shifted interval intersections, finite Fourier transformation/completion, or a composition of such operations -- and suppose its parameter satisfies

\[
\theta_z=\widetilde\theta_{\Pi(z)}.
\tag{16}
\]

Then tautologically

\[
T_{\theta_z}K_z
=
T_{\widetilde\theta_{\Pi(z)}}\widetilde K_{\Pi(z)},
\tag{17}
\]

so the transformed family still factors through `\Pi`. Induction gives the same conclusion for any finite composition satisfying `(16)` at every stage.

For the current application, `Z` is the internal factor tuple in `(1)` and `Y` is the divisor pair `(d,e)`. A standard `q`-vdC conductor factorization chooses its modulus factors from `q` and its shift multiples from those factors. If that choice is uniform across the coefficient fiber, equations `(15)`--`(17)` show that no sequence of such source-only transforms can make two representatives of the same products analytically distinct.

This is stronger than merely observing that the first difference in `(5)` has product-level parameters. It supplies a stopping rule: **iterating standard source-only `A`/`B` steps after the product quotient has already formed cannot by itself recover the internal coefficient variables.**

## 3. What conductor reduction can still buy

The quotient obstruction must not be confused with a claim that the `A`-process is analytically weak. Irving's formulation of the `q`-analogue of van der Corput explicitly uses a factorization `q=q_0q_1`, shifts by the periodic factor, and Cauchy to reduce the oscillatory modulus from `q` to `q_0`; iterating such steps and combining them with completion is the engine behind smooth-modulus character-sum improvements.

That gain remains fully available here. If the incomplete translated correlation in `MC-413` is difficult only because its source conductor is too large relative to its interval, a sufficiently favorable factorization of `q` may lower the residual conductor enough to improve the **individual** or collectively averaged source estimate.

What the present finding rules out is a different inference:

\[
\text{well-factorable coefficient}
+\text{source-conductor factorization}
\not\Rightarrow
\text{factor-level source occupancy}
\tag{18}
\]

when the two factorizations are used independently after the kernel has collapsed to `(d,e)`. The source split acts on the modulus of the character; the coefficient split acts on representations of `d` and `e`. Unless an analytic step couples those two decompositions, their coexistence is not a new retained-variable mechanism.

There are therefore two genuinely distinct surviving possibilities.

First, **source-only improvement**: prove that conductor factorization reduces the translated-correlation cost enough that the old product-level source frame already wins. This would be valuable even if coefficient factorability contributes nothing beyond bounded weights.

Second, **factor/conductor coupling**: arrange the argument before product collapse so that a conductor factor, differencing shift, congruence, or post-Cauchy condition depends separately on `r_1,r_2,r'_1,r'_2`. Such a transform violates `(16)` and is not covered by the quotient-stability lemma. It is the minimal structural shape required if well-factorability is to supply additional source observations rather than only coefficient organization.

## 4. Prior art and novelty boundary

The `q`-analogue of van der Corput and the modulus-reduction mechanism are classical prior art. A. J. Irving, *Estimates for character sums and Dirichlet L-functions to smooth moduli*, arXiv:1503.07156, explains in the introduction that Heath-Brown's `A`-process reduces a factorized modulus `q=q_0q_1` from `q` to `q_0`, and §2 formulates the general `A`-process for a product `f=f_0f_1`; see https://arxiv.org/abs/1503.07156. Irving's Lemma 2.1 uses the periodicity of the `q_1` factor and Cauchy, exactly the source-side mechanism specialized in `(8)`--`(11)`. His `B`-process is ordinary completion/Fourier transformation, and later sections combine these operations with square-root bounds for complete sums.

`MC-413` had already identified this literature as the relevant analytic prior art for the incomplete translated correlations, and `MC-382` separately audited the depth cost of iterating a related `q`-vdC architecture. The present result does not improve those character-sum theorems and makes no novelty claim for the `A`/`B` processes, CRT factorization of primitive characters, or Weil bounds.

The durable Mathia-specific contribution is the interaction classification with the post-`MC-454` coefficient representation: when the standard source-conductor process is applied **after** the translated kernel is indexed only by the product divisors, its transformed kernel remains a pullback through the same multiplication quotient. Conductor reduction is therefore a real source gain but not, without an additional coupling, the missing factor-level occupancy mechanism.

A targeted literature check on 22 September 2026 confirmed the classical modulus-reduction description in Irving and adjacent arithmetic-exponent-pair work; this finding should be read as a frontier no-go for the current coefficient/source coupling, not as a new theorem about `q`-van der Corput.

## Boundaries and falsification tests

- **Uniform source-side parameters are load-bearing.** If the choice of conductor factor, differencing scale, shift family, or completion is made separately as a function of an internal coefficient representative, condition `(16)` fails and the finding does not rule out a gain. Such a construction must still be shown to be a legitimate estimate of the original weighted sum rather than duplicated freedom introduced by representation.
- **The `q_1` factor is not literally erased pointwise.** Equation `(5)` retains its unit-support mask. What is reduced is the oscillatory character phase; discarding or exploiting the mask is a later analytic choice.
- **Residual complete sums have degeneracies.** The square-root statement following `(13)` requires the usual nondegeneracy. Shifts for which the rational phase collapses must be counted separately.
- **Coefficient cancellation inside multiplication fibers remains possible.** As in `MC-454`, cancellation among factor coefficients may alter the effective product-level weight even when it creates no new source sample.
- **Collective source estimates remain live.** A theorem averaging the residual `q_0`-conductor correlations over the existing product-level family could beat the current source tariff without ever exposing internal coefficient factors.
- **A pre-quotient dispersion or bilinear transformation remains live.** If the kernel is transformed while the internal coefficient variables still occupy separate arithmetic roles, the pullback hypothesis `(15)` may fail from the start.
- **No analytic continuation or zero-free assumption is used.** The structural identities are finite CRT/character algebra and source-variable transformations.
- **No global Möbius consequence is asserted.** The finding only classifies one proposed mechanism for improving the current translated-character source estimate.

A counterexample to the obstruction must therefore do more than exhibit conductor reduction. It must show that two internal coefficient factorizations of the same product divisors acquire analytically different source kernels under a justified transformation, or else show quantitatively that source-only conductor reduction beats the product-level occupancy barrier without requiring such a distinction.

## Consequence for the research line

`MC-454` asked for the exact transformed kernel after the first nontrivial operation on a genuine factorable component. The standard first `q`-vdC `A`-step now has that classification: **it lowers the oscillatory source conductor but preserves the multiplication quotient of the coefficient variables.** Repeating source-only `A`/`B` operations with fiber-independent parameters cannot change that conclusion.

The next useful calculation should therefore not merely iterate the same source-side process and recount internal factor tuples. It should pursue one of two falsifiable targets: either propagate the reduced-conductor estimate all the way through the existing product-level source-frame summation and test whether it actually beats the occupancy budget, or formulate one concrete pre-quotient dispersion/conductor-splitting scheme in which the conductor factor or differencing geometry depends separately on the well-factorable variables and then check whether that dependence survives Cauchy, completion, and recombination.