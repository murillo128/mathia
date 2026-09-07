# WP-191 — Burnol's adelic Lax–Phillips assembly is global, but its causality criterion is RH-equivalent

**Status:** `LITERATURE+DERIVED + EXACT-PRIOR-ART-REDIRECT + GLOBAL-ADELIC-SCATTERING + CAUSALITY-RH-EQUIVALENCE + ZETA-SECTOR-CONTROL + INDEPENDENCE-GATE-FAILURE + DECISIVE-NARROWING + NOT-WEIL-POSITIVITY`.

`WP-189` and `WP-190` sharpened the local scattering dictionary on both sides of the explicit formula. At the real place, Burnol's Fourier reflection system carries the exact Gamma phase on independently nonnegative supersymmetric Hamiltonians, but the relevant phase velocity changes sign. At a finite prime, Burnol's nonnegative p-adic time delay is exactly the Prime-Circle Poisson ray, while the local Weil/conductor block is the indefinite affine defect of that positive carrier.

The natural next question is therefore whether the missing sign could arise only after these local scattering ingredients are assembled globally. A targeted prior-art audit finds that the closest canonical version of precisely that move is already classical: Burnol constructs an adelic Lax–Phillips scattering system from Tate--Iwasawa harmonic analysis on a global field. The construction is genuinely global and couples the local places through the adelic Fourier transform and the idele class group. But its decisive order-like property is not an independent theorem of geometry:

\[
\boxed{
{\cal D}_{-}\perp {\cal D}_{+}
\quad\Longleftrightarrow\quad
\text{RH for all abelian }L\text{-functions of }K.
}
\tag{1}
\]

Thus **adelic causality itself cannot serve as Mathia's missing independent positivity theorem**. In the Riemann-zeta specialization Burnol gives the same obstruction without invoking the full family of abelian `L`-functions: the scattering multiplier is inner exactly when its Blaschke factor contains no zeros in `Re(s)>1/2`, i.e. exactly when RH holds.

This is a prior-art redirect rather than a claim that every global scattering completion is impossible. What is closed is the tempting route

\[
\text{local positive scattering carriers}
\longrightarrow
\text{adelic Lax--Phillips causality}
\longrightarrow
\text{independent Weil positivity}.
\tag{2}
\]

The middle implication is already the arithmetic target in disguise.

## 1. Burnol's construction is genuinely global rather than a direct sum of local responses

Let `K` be a global field, `A_K` its adele ring, and

\[
{\cal C}_K=\mathbb A_K^\times/K^\times
\tag{3}
\]

its idele class group. Burnol uses the self-dual additive Fourier transform on `A_K`, the Tate--Iwasawa multiplicative harmonic analysis, and a map

\[
E:{\cal S}(\mathbb A_K)\longrightarrow L^2({\cal C}_K,d^*u)
\tag{4}
\]

whose Fourier--Mellin transform is, up to a field-dependent scalar normalization, the associated Tate `L`-function restricted to the critical line. The map intertwines adelic dilations with the regular action of the idele class group, while Poisson--Tate summation intertwines the additive Fourier transform with inversion on `C_K`.

From this structure Burnol constructs outgoing and incoming subspaces

\[
{\cal D}_+,
\qquad
{\cal D}_-=I({\cal D}_+)
\subset L^2({\cal C}_K,d^*u),
\tag{5}
\]

and verifies the Lax--Phillips axioms apart from the possible causality/orthogonality condition. This matters for the present research line: the assembly is not merely a formal sum of separately chosen prime and real-place kernels. The arithmetic places have already been combined inside a single global Hilbert-space construction through adelic Fourier duality and the quotient by `K^×`.

So Burnol is a stronger matched control than the local failures of `WP-189` and `WP-190`. It reaches exactly the kind of **globalized scattering category** those findings leave open.

## 2. The missing global property is exactly RH-equivalent

Burnol's main causality theorem is

\[
\boxed{
\text{RH for every abelian }L\text{-function of }K
\iff
{\cal D}_-\perp {\cal D}_+.
}
\tag{6}
\]

He also gives an equivalent closure criterion for the adelic Hardy space. Hence the part of the Lax--Phillips package that is not already forced unconditionally by the adelic construction is precisely the part that detects the zero-free half-plane beyond the critical line.

This fails the `weil_positivity` independence gate in the strongest possible way. The branch is not looking for another exact statement equivalent to RH; it requires a nonnegative/ordered geometric object whose sign is established independently and only **then** identified with the Weil quadratic form. Equation (6) has the opposite logical structure: the desired causal orthogonality is itself equivalent to RH.

A useful way to expose the issue is to turn orthogonality into an ordinary positive defect. Let `P_+` and `P_-` be the orthogonal projections onto the two scattering subspaces and define

\[
C=P_-P_+.
\tag{7}
\]

Then for every `f`,

\[
\|Cf\|^2\ge0
\tag{8}
\]

holds tautologically, independently of arithmetic. But causality is the **vanishing** condition

\[
C=0
\quad\Longleftrightarrow\quad
{\cal D}_-\perp{\cal D}_+,
\tag{9}
\]

and by (6) this vanishing is RH-equivalent. Repackaging causality as a positive norm therefore does not manufacture an independent sign theorem: positivity of the defect is automatic, while the arithmetic content lies entirely in proving that the defect vanishes.

## 3. The Riemann-zeta sector is already circular on its own

For `K=Q`, one might try to evade the family-level statement in (6) by keeping only the trivial character/Riemann-zeta sector. Burnol treats that specialization separately through the Nyman--Beurling/Hardy-space model.

Let `B(s)` denote the Blaschke product formed from zeta zeros in the half-plane `Re(s)>1/2`, with multiplicity. Burnol computes the corresponding scattering multiplier as

\[
S_\zeta(s)
=
\left(\frac{s-1}{s}\right)^2 B(s)^{-2}
\tag{10}
\]

in his normalization. The multiplier is inner exactly when `B` has no zero in `Re(s)>1/2`. Equivalently,

\[
\boxed{
S_\zeta\text{ is inner}
\iff
B=1
\iff
\text{RH for }\zeta.
}
\tag{11}
\]

The scattering pair is causal/orthogonal exactly in the same inner case. Thus even after restricting to the Riemann sector, the candidate global sign condition is not a theorem supplied independently by the scattering geometry. The off-critical zero divisor enters precisely as the obstruction to innerness.

This also blocks a subtler loophole: one cannot count `S_zeta` as a source-forced positive/causal completion and then use its innerness as evidence for Weil positivity. Innerness is already the RH-equivalent assertion being sought.

## 4. Local positivity does not propagate to global causality

`WP-190` gives an unusually sharp control. For each finite prime `p`, Burnol's time-delay multiplier

\[
T_p(\theta)
=(\log p)P_{p^{-1/2}}(\theta)
\tag{12}
\]

is nonnegative by an unconditional scattering theorem. Its exponent-ray Toeplitz compression is exactly the positive Prime-Circle matrix `K_p`. Nevertheless the local Weil/conductor observable is

\[
H_p=(\log p)-T_p,
\tag{13}
\]

which is indefinite after the relevant compression and enters the local explicit formula through a grading/supertrace.

At infinity, `WP-189` gives the complementary control: Burnol's exact Gamma reflection phase is carried by nonnegative supersymmetric Hamiltonians, yet its phase velocity changes sign. Therefore both classes of local scattering carrier have strong independent positivity, but neither local theorem orders the local explicit-formula observable.

Burnol's adelic paper shows that assembling the local harmonic analysis globally does not automatically repair this mismatch. The global scattering system exists unconditionally, while its causal orthogonality remains equivalent to RH. Hence there is no valid inference

\[
\boxed{
\text{unconditional local positivity at every place}
\not\Rightarrow
\text{unconditional global causality/Weil positivity}.
}
\tag{14}
\]

The missing operation is still the one identified throughout this branch: a source-forced global coupling whose **assembled observable itself** has an independent sign theorem.

## 5. Function-field comparison confirms the logical boundary

Burnol emphasizes that the adelic formulation applies equally to number fields and function fields. In the latter case RH is already a theorem by independent algebro-geometric methods, yet the scattering construction does not supply an alternative proof. He explicitly lists this as a deficiency of the approach.

That comparison is useful here because it separates representation from mechanism. The adelic scattering formalism correctly packages the RH condition in both settings, but in the function-field case the actual independent positivity/cohomological input comes from elsewhere. The scattering causality criterion records the theorem once true; it does not itself supply the geometric reason for truth.

This is exactly the distinction imposed by the Mathia mandate between a new representation of known zero data/RH-equivalent structure and a geometry whose own positivity forces the Weil statement.

## 6. Prior art and novelty boundary

The global scattering theorem is classical prior art:

- Jean-François Burnol, *An adelic causality problem related to abelian L-functions*, Journal of Number Theory **87** (2001), no. 2, 253--269, DOI `10.1006/jnth.2000.2616`, arXiv `math/0001013`. Burnol constructs the adelic Lax--Phillips system, proves that all scattering axioms except possibly causality hold, and proves the causality criterion (6). Section 2 gives the Riemann-zeta/Nyman specialization and the inner scattering multiplier (10)--(11).
- The local ingredients compared above are Burnol's p-adic scattering/time-delay theory already audited in `WP-190`, and his archimedean Fourier-scattering theory audited in `WP-189`.

No novelty is claimed for adelic scattering, the causality theorem, Nyman--Beurling closure criteria, Blaschke factorization, or their equivalence to RH.

The Mathia-specific durable delta is the **cross-classification** forced by `WP-189` and `WP-190`: once the two most promising source-native local positive scattering carriers are recognized as Burnol objects, their most natural classical global scattering environment is already available, and its only missing Lax--Phillips axiom is exactly RH-equivalent. This closes the hope that merely passing from the local carriers to canonical adelic causality supplies the independent positivity theorem that the local constructions lacked.

## 7. What remains open

The finding does **not** rule out all global scattering, relative-index, or cohomological routes. It rules out treating Burnol's causal orthogonality/innerness as the independent sign mechanism.

A surviving construction must cross a stricter gate. It must produce, before using RH or the off-critical zero divisor, a global finite--archimedean operator/form `Q` for which

\[
Q\ge0
\tag{15}
\]

follows from a source-forced geometric theorem. Only afterward may one identify the local-to-global decomposition of `Q` with the finite Mangoldt term, the Gamma term, and the polar/global counterterms of the Weil functional.

In particular, generalized or renormalized scattering remains admissible only if its counterterms and coercivity are intrinsic to the construction. Replacing Burnol's `D_-\perp D_+` by another innerness, closure, spectral-defect, or zero-exclusion condition equivalent to RH would be another reformulation, not progress on the mandate.

The strongest surviving directions therefore remain genuinely different category changes: nonseparable finite--archimedean incidence before scalarization, an infinite/noncommutative relative pairing with an independent index or coercivity theorem, or a cohomological intersection structure whose positivity is established without importing the zeta zero divisor.

## Dependencies

- `research/weil_positivity/findings/WP-189-burnol-gamma-reflection-has-positive-supersymmetric-hamiltonians-but-no-weil-sign.md`
- `research/weil_positivity/findings/WP-190-prime-circle-poisson-ray-is-burnol-p-adic-time-delay-and-weil-block-is-its-conductor-defect.md`
- `research/weil_positivity/SOURCES.md`

## Bottom line

Burnol already provides a genuinely adelic Lax--Phillips assembly in which Tate--Iwasawa local harmonic analysis is coupled through the global field. But the decisive causal condition is

\[
{\cal D}_-\perp{\cal D}_+
\iff \text{RH},
\]

and in the zeta sector the scattering multiplier is inner exactly when the off-critical Blaschke factor is absent. The unconditional positivity seen in the local finite and archimedean carriers therefore does not become an unconditional global Weil sign after adelic assembly.

The natural Burnol globalization is an exact and valuable **RH-equivalent representation**, not the independent geometric positivity mechanism sought by `weil_positivity`. Any successful continuation must supply a different assembled observable whose positivity is proved before the arithmetic/RH identification.