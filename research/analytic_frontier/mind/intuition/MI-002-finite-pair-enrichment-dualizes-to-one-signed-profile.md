# MI-002 — Universal affine scalar pair certificates are positive-band and nearly periodization-saturated

**Evidence level:** supported by ANF-003--ANF-005 and ANF-010--ANF-014

## Core intuition

Finite enrichment does not create new pair information when all channels are ultimately compressed into one translation-invariant scalar affine counting functional. The surviving scalar branch is now much narrower than a generic signed support-one profile: universal validity over conjugation-invariant multisets forces the compact-band spectral profile to be nonnegative, and long duplicated lattices then impose an all-scale periodization floor tied by an exact Mellin identity to the analytic pair-correlation cost.

Thus the residual scalar question is an extremal problem near simultaneous saturation of a continuum of deterministic controls, not a search over arbitrary signed kernels.

## Strongest justified principle

ANF-003--ANF-005 reduce finite global pair enrichments to one scalar support-one witness plus explicit normalization slack. ANF-010--ANF-011 independently close the tempting out-of-band escape: the favorable positive BGSST tail cannot be harvested by giving a universal affine scalar witness a nontrivial negative Fourier tail.

ANF-012 strengthens the in-band constraint. Multiplicity amplification first forces nonnegativity of the pair energy for every finite conjugation-invariant multiset. Conjugate binomial combs can then concentrate spectral weight at any prescribed band frequency, so every continuous compact-band profile in this universal affine class must satisfy `J(alpha)>=0` pointwise. Signed spectral density is therefore unavailable even before the scalar extremal problem is optimized.

ANF-013 adds thermodynamic controls. Long equally spaced real configurations give the scale-free periodization floor

`p(J)=inf_{h>0} h^{-1} sum_k J(k/h)`,

and any fixed profile can beat Montgomery--Taylor only if `C(J)/p(J)<C_MT`.

ANF-014 shows that the numerator and denominator of this ratio are not independent. Its Mellin identity gives

`C(J)/p(J) >= 1+3/pi^2 = 1.3039635509...`,

leaving only about `0.0235357` of ratio room below the Montgomery--Taylor constant. Equality would require the periodization and central-value constraints to saturate essentially everywhere; the Möbius profile from ANF-013 is the formal equality candidate.

## What remains possible

The positive-band scalar branch is not yet proved empty. A decisive scalar result must either show that the full finite-configuration constraints raise the Mellin floor to Montgomery--Taylor, or construct a genuinely valid profile below it. The latter must satisfy the universal counting inequality, not only the periodization necessary conditions.

Out-of-band gain, matrix/inertia order, source-specific inequalities, nonlinear configuration functionals, and genuine higher correlations remain outside this scalar-affine classification.

## Status / novelty

Fourier positivity, Fejér periodization, Mellin transforms, and the underlying pair-correlation input are classical. The persisted synthesis is the information boundary: **universal affine scalar pair enrichment is forced into a nonnegative compact-band cone whose remaining improvement budget is quantitatively tiny and all-scale constrained**.

## Falsification criterion

Exhibit a universal affine scalar certificate in the stated compact-band class with a negative spectral value, contradicting ANF-012, or construct a profile satisfying the complete deterministic certificate with `C(J)/p(J)<C_MT`. A non-scalar or non-affine carrier would evade rather than falsify this intuition.

## Lean-formalizable core

- Affine scalarization of finite pair channels.
- Conjugate-comb localization forcing `J>=0`.
- Duplicated-lattice periodization constraints.
- Mellin identity for `C(J)` and the universal ratio floor.
