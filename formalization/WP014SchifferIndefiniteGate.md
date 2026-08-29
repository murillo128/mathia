# WP-014 Schiffer two-point formalization gate

## Verdict

`PASS_TO_PROOF`, pending the blocking independent Gate-0 review required by
Mathia issue [#73](https://github.com/murillo128/mathia/issues/73).

The current WP-014/PF-085 statements determine a faithful finite theorem with
explicit singular cases.  The determinant reduction is exact, the scalar
inequality has a feasible elementary mathlib route, and no current Mathia or
mathlib declaration already supplies the specialized theorem.  The historical
qwen-lean PR #104 is non-authoritative evidence under the updated issue and does
not replace this Mathia-local gate or artifact.

## Fixed sources and environment

Gate 0 was run from Mathia `main` commit
`e936a41da1dec54c03c61521c89a37d853bcb466` against:

- `research/weil_positivity/findings/WP-014-exact-schiffer-kernel-is-not-positive-definite.md`,
  the authoritative target;
- `research/prime_flute/findings/PF-085-grunsky-schiffer-completion-is-trace-class-and-misses-quarter-threshold.md`,
  only for the specialized kernel formula and diagonal extension.

Mathia had no Lean project or Lean source before this issue.  The smallest
local setup uses the newest compatible pair already installed on the execution
machine:

```text
Lean:    v4.32.2, commit f3b06c705e6c85f5314019d5d3baab0fec5b580c
mathlib: v4.32.2, commit 905b95818eb32af7874a58b427f50c1711a5e96c
```

The repository root `lean-toolchain`, `lakefile.toml`, and generated
`lake-manifest.json` pin that environment.  The globally newer v4.33.1 release
was not installed locally; the formalization skill makes the environment used
reproducibility evidence, not a scientific progression gate.

## Frozen formal surface

The implementation may add private helpers, but the public declarations are
frozen to the following mathematical surface:

```lean
noncomputable section

namespace Mathia.WP014

abbrev TailPoint := {x : ℝ // 2 < x}

def delta (x y : TailPoint) : ℝ :=
  Real.pi * (1 / (x : ℝ) - 1 / (y : ℝ))

def offDiagonalKernel (x y : TailPoint) (_hxy : x ≠ y) : ℝ :=
  Real.pi ^ 2 / ((x : ℝ) ^ 2 * (y : ℝ) ^ 2) *
    (1 / Real.sin (delta x y) ^ 2 - 1 / delta x y ^ 2)

def kernel (x y : TailPoint) : ℝ :=
  if hxy : x = y then Real.pi ^ 2 / (3 * (x : ℝ) ^ 4)
  else offDiagonalKernel x y hxy

def twoPointGram (x y : TailPoint) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![kernel x x, kernel x y; kernel y x, kernel y y]

theorem abs_delta_mem (x y : TailPoint) (hxy : x ≠ y) :
    0 < |delta x y| ∧ |delta x y| < Real.pi / 2

theorem schifferScalar_gt_one_third {t : ℝ}
    (ht₀ : 0 < |t|) (htπ : |t| < Real.pi / 2) :
    1 / Real.sin t ^ 2 - 1 / t ^ 2 > 1 / 3

theorem det_twoPointGram (x y : TailPoint) (hxy : x ≠ y) :
    (twoPointGram x y).det =
      Real.pi ^ 4 / ((x : ℝ) ^ 4 * (y : ℝ) ^ 4) *
        (1 / 9 -
          (1 / Real.sin (delta x y) ^ 2 - 1 / delta x y ^ 2) ^ 2)

theorem det_twoPointGram_neg (x y : TailPoint) (hxy : x ≠ y) :
    (twoPointGram x y).det < 0

theorem twoPointGram_not_posSemidef (x y : TailPoint) (hxy : x ≠ y) :
    ¬ (twoPointGram x y).PosSemidef

end Mathia.WP014
```

The scalar expression deliberately uses `1 / Real.sin t ^ 2`; no cosecant API
is introduced.  `offDiagonalKernel` requires a distinctness witness even
though the closed expression does not consume it, so the singular domain is
visible at the API boundary.  `kernel` is piecewise: the diagonal uses the
PF-085 continuous-extension value and the off-diagonal branch uses the
specialized formula.  No arbitrary value at a zero denominator encodes the
diagonal.

The gate accepts the specialized formula and diagonal extension from PF-085.
Deriving either from
`V'(x)V'(y)/(V(y)-V(x))^2 - 1/(y-x)^2`, or proving the diagonal limit, is
outside the finite boundary frozen by #73.

## Independent mathematical reconstruction

For tail points `x,y`, both are positive and

```text
0 < 1/x < 1/2,
0 < 1/y < 1/2.
```

Consequently `|1/x - 1/y| < 1/2`.  If `x ≠ y`, injectivity of inversion on
nonzero reals makes the difference nonzero.  Since `pi > 0`, this gives

```text
0 < |pi * (1/x - 1/y)| < pi/2.
```

The displacement is therefore nonzero and lies strictly inside the first
half-period.  In particular `sin(delta) ≠ 0`; every denominator in the
off-diagonal kernel is nonzero under its explicit proof argument.

Writing

```text
d = delta x y,
f = 1 / sin(d)^2 - 1 / d^2,
```

swapping `x,y` sends `d` to `-d`.  Oddness of sine and both squares leave `f`
unchanged, so the two off-diagonal entries agree.  The diagonal entries are
`pi^2/(3*x^4)` and `pi^2/(3*y^4)`.  Direct field normalization gives

```text
det = pi^4/(x^4*y^4) * (1/9 - f^2).
```

The prefactor is strictly positive.  Thus the scalar inequality `f > 1/3`
implies `1/9 - f^2 < 0` and hence the required negative determinant.

### Scalar proof route

For `0 < t < pi/2`, put

```text
q(t) = t - t^3/6 + t^5/120,
u = t^2.
```

Starting from mathlib's strict cubic lower bound for sine, two derivative and
strict-monotonicity arguments give

```text
0 < sin(t) < q(t).
```

The exact derivative identities and the following terminal polynomial identity
were elaborated with the pinned Lean/mathlib environment during the gate:

```text
(3 + u) * q(t)^2 - 3*u
  = u^3/14400 * (u^3 - 37*u^2 + 520*u - 2880).
```

From `t < pi/2` and `pi < 4`, one has `0 < u < 4`.  On that interval,
`u^2*(u-37) ≤ 0` and `520*u - 2880 < -800`, so the last polynomial is
strictly negative.  It follows that

```text
(3 + t^2) * sin(t)^2 < 3*t^2,
```

which is exactly the desired reciprocal inequality after clearing the already
positive denominators.  The negative half-interval follows by applying the
positive result to `-t` and using `Real.sin_neg`.  This route covers the full
open interval and requires no series, limit, numerical premise, or unchecked
certificate.

## Adversarial checks

1. **Order and sign.** Swapping the two tail points negates `delta` but leaves
   the scalar and determinant unchanged.  The explicit Gram matrix is
   symmetric.
2. **Diagonal boundary.** As `x` approaches `y`, `delta` approaches zero and
   the determinant approaches zero from below, while strict negativity holds
   only for distinct points.  The piecewise definition does not evaluate the
   singular formula on the diagonal.
3. **Tail boundary.** In the extreme `x → 2+`, `y → ∞`, `|delta|`
   approaches `pi/2` from below; for fixed `x` and `y → ∞`, the negative
   scalar bracket is multiplied by a positive prefactor tending to zero.
   Neither boundary is included by the theorem.
4. **Denominators.** Tail membership gives `x,y ≠ 0`; distinctness gives
   `delta ≠ 0`; the strict half-period bound gives `sin(delta) ≠ 0`.
   Field simplification is authorized only after these facts are established.
5. **Determinant convention.** `Matrix.det_fin_two` uses row/column order
   `0,1` and the formula `a*d - b*c`; a pinned-Lean probe checked the displayed
   determinant identity by exact `field_simp` and `ring`.
6. **Full scalar interval.** The proof route uses only `0 < t < pi/2`, relaxed
   to `t < 2` for the terminal polynomial.  It is not a near-zero argument.
7. **Overall kernel sign.** Negating all four entries multiplies a `2 x 2`
   determinant by `(-1)^2`; the obstruction survives an overall sign change.
8. **PSD semantics.** `Matrix.PosSemidef` includes the Hermitian requirement.
   The corollary needs no separate symmetry hypothesis because
   `Matrix.PosSemidef.det_nonneg` contradicts the strict negative determinant;
   symmetry is nevertheless true by item 1.
9. **Scope fidelity.** The theorem proves only the exact finite specialized
   obstruction.  It does not formalize PF-085 trace/Schatten statements,
   global Weil positivity, test-function extensions, or RH consequences.

Fresh double-precision samples at `t = 10^-3, 10^-2, 0.1, pi/4` and near
`pi/2` produced positive margins over `1/3`; near-diagonal, near-tail, and
widely separated point pairs produced negative determinants.  These samples
were falsification aids only.  They are neither proof evidence nor premises.

## Current prior-art and reuse audit

Searches on 2026-08-29 covered the current Mathia tree, mathlib v4.32.2 source,
and public GitHub code for:

- `Schiffer` in Lean;
- the exact `pi*cot(pi/x)` specialization;
- the scalar combination `1 / sin(t)^2 - 1 / t^2` and cosecant spellings;
- a Schiffer kernel described as positive semidefinite.

No current Mathia Lean source exists, and no exact or stronger compatible
declaration was found in mathlib or public GitHub code.  Mathlib has real and
complex cotangent definitions, but using cotangent or adding cosecant notation
would obscure the already-specialized formula.  Generic Grunsky/Schiffer
theory, determinant tests, and PSD theory remain prior art; the formalization
makes no novelty claim for them.

Historical qwen-lean PR #104 contains an earlier proof of the same intended
claim.  The updated #73 contract explicitly classifies it as non-authoritative
historical evidence and requires the accepted artifact to live in Mathia.
Therefore its existence does not produce a reuse-only outcome.  It may be used
as a later comparison/falsification control, but every declaration, import,
and proof must compile in this pinned Mathia-local project and the final target
requires a fresh independent review.

Exact reusable mathlib declarations/imports found in the current audit:

- `Mathlib.Analysis.Matrix.PosDef`:
  `Matrix.PosSemidef.det_nonneg`;
- `Mathlib.Analysis.Real.Pi.Bounds`:
  `Real.pi_pos`, `Real.pi_lt_four`;
- `Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds`:
  `Real.sin_gt_sub_cube`, plus the basic sine declarations it imports;
- determinant infrastructure:
  `Matrix.det_fin_two`;
- ordered-field and calculus infrastructure:
  `one_div_lt_one_div_of_lt`, `inv_inj`,
  `strictMonoOn_of_deriv_pos`;
- exact automation already in mathlib:
  `fun_prop`, `field_simp`, `ring`, `linarith`, `nlinarith`, `positivity`, and
  `grind`.

No external Lean dependency beyond mathlib is justified.

## Gate boundary

If independent review finds a missing hypothesis, a mismatch with the current
WP-014/PF-085 formulas, a singularity hidden by the proposed API, or an exact
stronger Mathia-local declaration that should be reused, proof work must stop
and #73 must return to design/investigation.  Otherwise Phase 1 may implement
only the frozen theorem chain above.
