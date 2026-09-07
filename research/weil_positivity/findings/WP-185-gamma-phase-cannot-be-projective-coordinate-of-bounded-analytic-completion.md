# WP-185 — The exact Gamma phase cannot be a projective coordinate of any bounded-analytic completion

**Status:** `EXACT-DERIVED + PROJECTIVE-BOUNDED-CHARACTERISTIC-NO-GO + PRE-QUOTIENT-COMMON-NORMALIZATION-OBSTRUCTION + STABLE-RATIONAL-DECODER-NO-GO + MATCHED-INNER-CONTROL + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-WEIL-POSITIVITY`.

`WP-169` isolates the exact real-place relative phase

\[
R_\infty(z)
=\pi^{iz}
\frac{\Gamma(\tfrac14-\tfrac{iz}{2})}
     {\Gamma(\tfrac14+\tfrac{iz}{2})},
\tag{1}
\]

between the Mathia pointed-shell spectral factor and the Nyman comparator. `WP-184` proves that the upper-half-plane continuation of (1) is **not** of bounded characteristic because its zeros

\[
z_n=i\left(2n+\frac12\right),\qquad n\ge0,
\tag{2}
\]

violate the Blaschke condition. It therefore closes post-quotient bounded-type Möbius repairs, while explicitly leaving source-derived coupling **before** the quotient as the preferred surviving architecture.

There is a first pre-quotient escape that can now be closed without imposing any bounded-type hypothesis on the compensator itself. The exact Gamma phase cannot occur as the projective ratio of two bounded-analytic, or even bounded-characteristic, channels. Consequently the two unnormalized factors of `WP-169` cannot be simultaneously stabilized by a **common scalar normalization** into a bounded analytic vector while preserving their exact analytic relative phase. The common normalizer may be arbitrarily singular or lie outside bounded characteristic; the obstruction remains because it cancels from the projective ratio.

More generally, no finite family of bounded-characteristic output channels can retain `R_infty` in a way recoverable by a finite rational decoder with bounded-characteristic coefficients. Thus a successful pre-quotient construction must genuinely change the projective coordinate, keep at least one channel outside bounded characteristic, use a non-rational/infinite decoding mechanism, or work only at the boundary with a new sign theorem. Merely applying the same source-derived denominator or outer normalization to both factors does not evade `WP-184`.

This is a project-specific corollary of classical Nevanlinna field structure, not a new theorem of function theory and not a Weil positivity result.

## 1. Projective-coordinate obstruction

Let

\[
\mathcal N_{bc}(\mathbb H)
\]

denote the meromorphic field of functions of bounded characteristic in the upper half-plane. Equivalently, every element is a quotient of two bounded analytic functions on `H`, and the class is closed under the field operations wherever the denominator is not identically zero.

`WP-184` establishes

\[
\boxed{R_\infty\notin\mathcal N_{bc}(\mathbb H).}
\tag{3}
\]

Suppose there were two functions

\[
U,V\in\mathcal N_{bc}(\mathbb H),
\qquad V\not\equiv0,
\tag{4}
\]

with the exact meromorphic identity

\[
\frac{U}{V}=R_\infty.
\tag{5}
\]

Because `N_bc(H)` is a field, (4) would imply `U/V in N_bc(H)`, contradicting (3). Hence

\[
\boxed{
R_\infty\text{ is not the projective coordinate }[U:V]
\text{ of any }\mathcal N_{bc}\text{ two-channel vector.}
}
\tag{6}
\]

In particular there are no bounded analytic `U,V in H^infinity(H)` with exact ratio `R_infty`.

This is stronger than the bounded linear-mixer theorem of `WP-183` in one direction and orthogonal to the Möbius theorem of `WP-184`. Here there is **no hypothesis at all on how `U` and `V` were produced**. The encoder may be nonlinear, source-dependent, singular, or outside bounded characteristic. Once both visible channels land in bounded characteristic and their exact projective ratio is the Gamma phase, the contradiction is automatic.

## 2. A finite stable channel packet cannot rationally encode the phase

The same field argument is not limited to two coordinates.

Let

\[
F_1,\ldots,F_m\in\mathcal N_{bc}(\mathbb H)
\tag{7}
\]

and let `Q` be any finite rational expression in the variables `F_j` whose coefficients lie in `N_bc(H)` and whose denominators are not identically zero. Field closure gives

\[
Q(F_1,\ldots,F_m)\in\mathcal N_{bc}(\mathbb H).
\tag{8}
\]

Therefore

\[
\boxed{
Q(F_1,\ldots,F_m)\neq R_\infty
}
\tag{9}
\]

as a meromorphic identity.

So increasing the number of bounded analytic completion channels does not by itself evade the Gamma divisor. A finite Schur/Pythagorean, conservative-scattering, or other bounded analytic packet may contain many source-derived coordinates, but if the exact phase is to remain recoverable from those coordinates by ordinary finite algebraic/rational channel operations, it would belong to bounded characteristic.

This strengthens the architectural boundary from `WP-184`: the obstruction is not specifically a single scalar Möbius regularizer. It applies to **any finite projectively faithful bounded-characteristic encoding with a bounded-type rational decoder**, regardless of the complexity of the encoder.

An infinite limiting procedure is not covered. A non-normal limit of bounded-characteristic expressions can leave the class, and an infinite decoder may encode singularity not visible at any finite stage. Such a mechanism would require its own domain, convergence, and positivity theorem.

## 3. Direct application to the two unnormalized WP-169 spectral factors

The pre-quotient statement can be made concrete using the factors already present in `WP-169`. Their meromorphic continuations in the spectral variable are

\[
B(z)
:=-\frac{\zeta(\tfrac12+iz)}{\tfrac12-iz},
\qquad
C(z)
:=-\frac{\zeta(\tfrac12-iz)}{\tfrac12-iz}.
\tag{10}
\]

On the real line these are exactly the Fourier/Mellin factors `bhat` and `chat` of `WP-169`. The Riemann functional equation gives, as a meromorphic identity and hence through removable common zero sets,

\[
\boxed{
\frac{B(z)}{C(z)}=R_\infty(z).
}
\tag{11}
\]

Now let `q` be **any** nonzero meromorphic function on `H`. No boundedness, bounded-characteristic, Smirnov, Hardy, passivity, or finite-order assumption is made on `q`. Suppose a common pre-quotient normalization produced

\[
U=qB,
\qquad
V=qC,
\tag{12}
\]

with

\[
U,V\in\mathcal N_{bc}(\mathbb H).
\tag{13}
\]

Since the common factor cancels wherever the ratios are defined, and the identities continue meromorphically,

\[
\frac{U}{V}
=\frac{B}{C}
=R_\infty.
\tag{14}
\]

Equations (13)--(14) contradict (6). Therefore

\[
\boxed{
\text{no common scalar normalizer, however singular, can put both}
\ B\text{ and }C\text{ into bounded characteristic while preserving their exact ratio.}
}
\tag{15}
\]

In particular there is no common outer denominator, common Hardy renormalization, common stable weighting, or common source-dependent scalar gauge that turns `(B,C)` into an `H^infinity` column with projective coordinate `R_infty`.

This closes a genuine part of the pre-quotient category left open by `WP-184`. Acting before division helps only if the operation **changes more than the common scale**. A common scale cannot alter the offending projective divisor.

## 4. Asymmetric normalization must itself carry the non-bounded-characteristic defect

One may try to evade (15) by normalizing the two factors differently. Let

\[
U=q_B B,
\qquad
V=q_C C,
\tag{16}
\]

where `q_B,q_C` are nonzero meromorphic functions and suppose again that

\[
U,V\in\mathcal N_{bc}(\mathbb H).
\tag{17}
\]

Then

\[
\frac{U}{V}
=\frac{q_B}{q_C}R_\infty
\in\mathcal N_{bc}(\mathbb H).
\tag{18}
\]

If the relative compensator `q_C/q_B` were also of bounded characteristic, multiplying (18) by it would put `R_infty` in bounded characteristic, contradicting (3). Thus any successful asymmetric stabilization must satisfy

\[
\boxed{
\frac{q_C}{q_B}\notin\mathcal N_{bc}(\mathbb H).
}
\tag{19}
\]

The significance is architectural rather than terminological. An asymmetric denominator can succeed only by carrying a relative analytic defect at least severe enough to leave the entire bounded-characteristic field. The missing Gamma complexity has not disappeared; it has been moved into the **relative compensator**.

Therefore a proposed source-derived asymmetric completion must explain why the geometry independently produces this non-Blaschke relative factor. Choosing `q_B/q_C` after inspecting the known Gamma divisor is only a repackaging of the target and fails the branch's no-hand-picked-regularization gate.

## 5. Matched controls

The obstruction is specific to the exact Gamma phase, not to projective bounded analytic completion in general.

Let `J` be an ordinary inner function on `H`. Then

\[
(J,1)^T\in H^\infty(\mathbb H;\mathbb C^2)
\tag{20}
\]

and its projective coordinate is exactly

\[
\frac{J}{1}=J.
\tag{21}
\]

Likewise the Hadamard split from `WP-183`,

\[
\left(\frac{1+J}{2},\frac{1-J}{2}\right)^T,
\tag{22}
\]

is bounded analytic and retains `J` through an ordinary bounded-type rational inversion away from the degenerate set. So genuine passive inner phases admit exactly the kind of finite bounded analytic packet ruled out for `R_infty`.

There is also a common-normalization control. Start from any pair `(JO,O)` with a nonzero analytic common factor `O` for which division by `O` is meaningful. The common scalar gauge `q=1/O` recovers `(J,1)`. This works because the projective ratio `J` already belongs to bounded characteristic. Equation (15) says the analogous operation cannot exist for the `WP-169` pair because its projective ratio lies outside that field.

Finally, boundary-only factorization remains a real control rather than a contradiction. Since `|R_infty(t)|=1` for real `t`, the measurable boundary vector `(R_infty(t),1)` is perfectly bounded. What fails is its realization as the boundary trace of an analytic `H^infinity` pair whose **interior meromorphic ratio is the same analytic continuation** (1). The theorem must not be read as a prohibition on arbitrary `L^infinity` boundary encodings.

## 6. Aggressive falsification and exact scope

Several stronger claims would be false or unsupported.

**The result does not close all pre-quotient coupling.** A source-derived matrix or nonlinear operation on `(B,C)` may genuinely change their projective ratio before bounded scalarization. If the resulting positive geometry retains the required archimedean Weil contribution through a different observable, (15) does not apply.

**Boundary equality alone is not enough for the contradiction.** Outside bounded characteristic, an analytic function need not be determined by merely prescribing an almost-everywhere boundary representative in the way Hardy/Smirnov uniqueness arguments are normally used. The claim here is about preserving the exact analytic/meromorphic relative phase (11), not merely matching its unimodular boundary values.

**An infinite or non-rational decoder remains open.** Equation (9) uses finite field operations. A singular limit, an infinite determinant, a changing domain, or a nonlocal operator can leave bounded characteristic even if finite stages do not. Such a category change must establish its own convergence and sign theorem rather than inherit positivity rhetorically from the finite approximants.

**At least one unbounded or non-bounded-characteristic channel may retain the phase.** The raw pair `(B,C)` already does. The theorem says that one cannot regularize both into the ordinary bounded-type analytic category while keeping the exact projective coordinate.

**No finite-prime selector or polar term is produced.** This is an archimedean architecture obstruction. It does not create Mangoldt support, the critical `p^{-1/2}` coefficient, mixed-prime incidence, or the polar counterterms, and it proves no equality with the Weil quadratic form.

**No RH assumption or zero data enter the argument.** The only divisor used is the explicit Gamma zero sequence (2), not the zeros of zeta. The relation (11) is the classical functional equation identity already established in `WP-169`.

The decisive falsification test is correspondingly simple: produce nonzero `U,V in N_bc(H)` with the exact meromorphic ratio `U/V=R_infty`, or produce a common meromorphic `q` such that `qB` and `qC` both lie in `N_bc`. Either construction would contradict the classical quotient characterization together with the established non-Blaschke divisor of `R_infty`.

## 7. Prior-art and novelty audit

Nothing in the abstract function theory is new. The characterization of bounded-characteristic/Nevanlinna functions as quotients of bounded analytic functions, their field closure, and the Blaschke condition on zero divisors are classical. `WP-184` already anchors these facts to Louis de Branges, *Hilbert Spaces of Entire Functions* (Prentice-Hall, 1968), Chapter 1, §9, and John B. Garnett, *Bounded Analytic Functions* (Springer GTM 236, 2007). Modern statements of the quotient characterization give the same algebra immediately.

The projective viewpoint is classical as well. R. E. Molzon and G. Patrizio, *Meromorphic maps in the Nevanlinna class*, Proceedings of the American Mathematical Society 91 (1984), 395--398, DOI `10.1090/S0002-9939-1984-0744637-X`, studies Nevanlinna-class meromorphic maps into projective space. The present argument does not claim or need a new theorem about such maps; it uses only the elementary scalar fact that a projective ratio of bounded-characteristic coordinates remains of bounded characteristic.

A targeted literature search for bounded characteristic, quotient representations, projective Nevanlinna maps, and Gamma ratios found the expected classical quotient/projective theory and unrelated Gamma-ratio function classes. No external result was found or required that turns the Mathia-specific Gamma factor into a bounded projective coordinate. Absence of such wording is not treated as novelty evidence.

The substantive delta is entirely the application to the exact `WP-169` source factors. `WP-184` left **pre-quotient** coupling open and noted that coefficients outside bounded characteristic might carry the required infinite divisor compensation. Equations (12)--(15) show that a *common* pre-quotient compensation cannot work even if that compensator itself lies arbitrarily far outside bounded characteristic, because common scalar compensation leaves the forbidden projective ratio unchanged. Equations (16)--(19) then identify the exact burden on any asymmetric repair: its relative compensator must itself be outside bounded characteristic.

That is a new project-specific narrowing, not a new theorem of Nevanlinna theory.

## 8. Consequence for the Weil-positivity search

The live Pythagorean lesson of `WP-182` remains valid: positivity may belong to a completed multi-channel geometry rather than to the signed phase of one scalar response. But `WP-183`--`WP-185` now impose a much sharper analytic gate on using the exact real-place phase exposed by `WP-169`.

A bounded analytic completed channel cannot first isolate `R_infty` and then stabilize it linearly (`WP-183`); bounded-type Möbius/Cayley algebra cannot repair it (`WP-184`); and even **before the quotient**, no arbitrary common scalar normalization can turn the two exact source factors into bounded-type channels while retaining their projective Gamma phase (`WP-185`). Finite bounded channel packets cannot hide the phase behind a rational decoder either.

Thus the preferred surviving architecture is no longer merely "couple before quotienting." It must satisfy a stronger requirement:

\[
\boxed{
\text{the source-derived coupling must genuinely alter the projective analytic category}
\text{ before bounded positive scalarization,}
}
\tag{23}
\]

or else keep an intrinsically singular/non-bounded-characteristic channel all the way to a new positivity theorem. A common gauge, common denominator, ordinary outer stabilization, or finite bounded rational encoding is insufficient.

For the branch mandate this is useful because it prevents a large amount of apparent freedom from being mistaken for new geometry. The real remaining target is still a single finite--archimedean object in which the signed finite arithmetic selector, the real-place contribution, and the final sign theorem are assembled before the information is forced through a bounded-type projective quotient.

## Dependencies

- `research/weil_positivity/findings/WP-169-pointed-nyman-relative-phase-is-exact-archimedean-scattering.md`
- `research/weil_positivity/findings/WP-170-archimedean-phase-is-not-a-passive-inner-boundary-response.md`
- `research/weil_positivity/findings/WP-182-pythagorean-defect-completion-cancels-dissipative-pole-but-controls-total-phase.md`
- `research/weil_positivity/findings/WP-183-gamma-relative-phase-cannot-survive-bounded-analytic-linear-channel-mixing.md`
- `research/weil_positivity/findings/WP-184-gamma-phase-is-outside-bounded-characteristic-and-bounded-type-mobius-repairs-degenerate.md`

## Bottom line

The exact Gamma phase is not merely hard to make Schur. Because it lies outside bounded characteristic, it cannot be the exact analytic projective ratio of **any** two bounded-characteristic channels. Applied before the `WP-169` quotient, this gives a strong common-normalization no-go: no shared scalar compensator, even an arbitrarily singular one outside bounded characteristic, can simultaneously regularize both source factors into bounded-type channels without losing the exact relative phase. Any asymmetric repair that succeeds must carry a relative compensator outside bounded characteristic, while any finite bounded channel packet loses rational recoverability of the phase.

So pre-quotient coupling remains open only in a genuinely stronger sense: it must change the projective coordinate/category, retain singular data, or use an infinite/non-rational mechanism with its own independent positivity theorem. The ordinary common-stabilization escape is closed.