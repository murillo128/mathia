# PC-063 Gate 0: growing-conductor anchor/Haar crossover

Checkpoint target for issue #87. This document freezes the theorem surface before proof
implementation. The proposed outcome is **safe progression**, subject to the required independent
Checkpoint-A verdict on the published commit.

## Authoritative claim and scope

The authoritative research source is
`research/prime_circle/findings/PC-063-growing-conductor-root-projection-is-anchor-haar-mixture.md`
at Mathia revision `c111a29655289d094e049f149d61c3d8d396c644`. No adjacent PC-063 adversarial
sidecar exists at this checkpoint, and the finding's canonical statement has not changed from the
issue contract.

The accepted theorem boundary is the logarithmic-series probability law, its canonical projection
to growing roots of unity, and weak convergence to the exact anchor/Haar mixture for both finite
and divergent logarithmic scale ratios. The separate log-scale law for `N_x`, the centered matched-
boundary profile, nonlinear mode families, novelty, RH, and the claim that no other arithmetic
spectral construction can exist remain outside Lean.

## Frozen representation and conventions

- The asymptotic parameter is a sequence `j : ℕ`. The theorem quantifies over every pair of
  sequences `x : ℕ → ℝ` and `q : ℕ → ℕ` satisfying the displayed hypotheses below. Because the
  parameter spaces and the weak topology on probability measures over the compact metrizable
  circle are first countable, this is the sequential form of the persisted pathwise asymptotic
  claim, not a finite-instance weakening.
- `x → 1⁻` is represented by `∀ j, x j ∈ Set.Ioo 0 1` together with
  `Filter.Tendsto x Filter.atTop (nhds 1)`.
- `q → ∞` is `Filter.Tendsto q Filter.atTop Filter.atTop`; `∀ j, 0 < q j` makes division and
  `Real.log (q j)` explicit at every index rather than merely eventually.
- `L(x)` is `logScale x := -Real.log (1 - x)`. The domain hypotheses imply `0 < logScale x` and
  `logScale (x j) → +∞`.
- The atom indexed by Lean's `n : ℕ` represents the research integer `N = n + 1`, so the mass is
  exactly `x^(n+1) / ((n+1) * L(x))`; no atom at zero is introduced.
- Proof work is performed first on `UnitAddCircle = AddCircle 1`. The root map is
  `n ↦ ((n + 1 : ℝ) / q : UnitAddCircle)`. Its `k : ℤ` character is mathlib's
  `AddCircle.fourier k`, hence uses `exp(2 * π * I * k * (n+1) / q)` with the positive sign.
- The delivered principal theorem is on mathlib's complex unit circle `Circle`, obtained through
  `AddCircle.homeomorphCircle one_ne_zero`. Under this homeomorphism the additive anchor `0` is the
  common complex root `1`, so the final measure is literally on `S¹`, not merely a coefficient
  surrogate.
- Normalized Haar measure on `UnitAddCircle` is `AddCircle.haarAddCircle`. Circle Haar is its
  pushforward through the homeomorphism. The mixture is a `ProbabilityMeasure Circle`, and its
  underlying measure is proved equal to
  `c • Measure.dirac (1 : Circle) + (1-c) • circleHaar` with real coefficients represented through
  the measure API's nonnegative scalar type.

## Frozen public theorem surface

Names may receive only namespace- or elaboration-level adjustments. The mathematical arguments and
conclusions below are frozen.

```lean
namespace Mathia.PC063

abbrev Torus := AddCircle 1

def logScale (x : ℝ) : ℝ := -Real.log (1 - x)
def logSeriesWeight (x : ℝ) (n : ℕ) : ℝ :=
  x ^ (n + 1) / ((n + 1 : ℝ) * logScale x)

theorem logScale_pos {x : ℝ} (hx : x ∈ Set.Ioo 0 1) : 0 < logScale x
theorem hasSum_logSeriesWeight {x : ℝ} (hx : x ∈ Set.Ioo 0 1) :
  HasSum (logSeriesWeight x) 1

noncomputable def logSeriesPMF (x : ℝ) (hx : x ∈ Set.Ioo 0 1) : PMF ℕ
noncomputable def torusRootProjection
    (x : ℝ) (q : ℕ) (hx : x ∈ Set.Ioo 0 1) : ProbabilityMeasure Torus
noncomputable def circleRootProjection
    (x : ℝ) (q : ℕ) (hx : x ∈ Set.Ioo 0 1) : ProbabilityMeasure Circle

noncomputable def torusHaar : ProbabilityMeasure Torus
noncomputable def circleHaar : ProbabilityMeasure Circle
noncomputable def circleAnchor : ProbabilityMeasure Circle
noncomputable def torusAnchorHaar (c : Set.Icc (0 : ℝ) 1) : ProbabilityMeasure Torus
noncomputable def circleAnchorHaar (c : Set.Icc (0 : ℝ) 1) : ProbabilityMeasure Circle

theorem circleAnchorHaar_toMeasure (c : Set.Icc (0 : ℝ) 1) :
  (circleAnchorHaar c : Measure Circle) =
    ENNReal.ofReal c.1 • Measure.dirac (1 : Circle) +
      ENNReal.ofReal (1 - c.1) • (circleHaar : Measure Circle)
theorem circleAnchorHaar_zero : circleAnchorHaar ⟨0, by simp⟩ = circleHaar
theorem circleAnchorHaar_one : circleAnchorHaar ⟨1, by simp⟩ = circleAnchor

theorem torusRootProjection_fourier
    {x : ℝ} (hx : x ∈ Set.Ioo 0 1) {q : ℕ} (hq : 0 < q) (k : ℤ) :
  ∫ z, AddCircle.fourier k z ∂(torusRootProjection x q hx : Measure Torus) =
    -Complex.log
        (1 - (x : ℂ) * Complex.exp (2 * Real.pi * Complex.I * k / q)) /
      logScale x

theorem root_modulus_sq (x θ : ℝ) :
  ‖1 - (x : ℂ) * Complex.exp (θ * Complex.I)‖ ^ 2 =
    (1 - x) ^ 2 + 4 * x * Real.sin (θ / 2) ^ 2

theorem finiteRatio_mode_limit
    (x : ℕ → ℝ) (q : ℕ → ℕ) (β : ℝ)
    (hx : ∀ j, x j ∈ Set.Ioo 0 1) (hq : ∀ j, 0 < q j)
    (hx1 : Tendsto x atTop (nhds 1)) (hq_top : Tendsto q atTop atTop)
    (hβ : 0 ≤ β)
    (hratio : Tendsto (fun j => Real.log (q j : ℝ) / logScale (x j))
      atTop (nhds β))
    {k : ℤ} (hk : k ≠ 0) :
  Tendsto
    (fun j => -Complex.log
        (1 - (x j : ℂ) * Complex.exp (2 * Real.pi * Complex.I * k / q j)) /
      logScale (x j))
    atTop (nhds (min 1 β : ℂ))

theorem divergentRatio_mode_limit
    (x : ℕ → ℝ) (q : ℕ → ℕ)
    (hx : ∀ j, x j ∈ Set.Ioo 0 1) (hq : ∀ j, 0 < q j)
    (hx1 : Tendsto x atTop (nhds 1)) (hq_top : Tendsto q atTop atTop)
    (hratio : Tendsto (fun j => Real.log (q j : ℝ) / logScale (x j))
      atTop atTop)
    {k : ℤ} (hk : k ≠ 0) :
  Tendsto
    (fun j => -Complex.log
        (1 - (x j : ℂ) * Complex.exp (2 * Real.pi * Complex.I * k / q j)) /
      logScale (x j))
    atTop (nhds (1 : ℂ))

theorem tendsto_torus_probabilityMeasure_of_fourier
    {μ : ℕ → ProbabilityMeasure Torus} {ν : ProbabilityMeasure Torus}
    (h : ∀ k : ℤ,
      Tendsto (fun j => ∫ z, AddCircle.fourier k z ∂(μ j : Measure Torus))
        atTop (nhds (∫ z, AddCircle.fourier k z ∂(ν : Measure Torus)))) :
  Tendsto μ atTop (nhds ν)

/-- Principal theorem A: finite logarithmic scale ratio. -/
theorem finiteScale_circleRootProjection_tendsto
    (x : ℕ → ℝ) (q : ℕ → ℕ) (β : ℝ)
    (hx : ∀ j, x j ∈ Set.Ioo 0 1) (hq : ∀ j, 0 < q j)
    (hx1 : Tendsto x atTop (nhds 1)) (hq_top : Tendsto q atTop atTop)
    (hβ : 0 ≤ β)
    (hratio : Tendsto (fun j => Real.log (q j : ℝ) / logScale (x j))
      atTop (nhds β)) :
  Tendsto (fun j => circleRootProjection (x j) (q j) (hx j)) atTop
    (nhds (circleAnchorHaar ⟨min 1 β, by constructor <;> simp [hβ]⟩))

/-- Principal theorem B: divergent logarithmic scale ratio. -/
theorem divergentScale_circleRootProjection_tendsto
    (x : ℕ → ℝ) (q : ℕ → ℕ)
    (hx : ∀ j, x j ∈ Set.Ioo 0 1) (hq : ∀ j, 0 < q j)
    (hx1 : Tendsto x atTop (nhds 1)) (hq_top : Tendsto q atTop atTop)
    (hratio : Tendsto (fun j => Real.log (q j : ℝ) / logScale (x j))
      atTop atTop) :
  Tendsto (fun j => circleRootProjection (x j) (q j) (hx j)) atTop
    (nhds circleAnchor)

end Mathia.PC063
```

The implementation must also compile explicit corollaries specializing principal theorem A to
`β = 0`, `β = 1`, and `β = 2`, plus the principal divergent theorem. These expose the Haar,
endpoint-anchor, above-threshold-anchor, and infinite-ratio conventions without relying on
numerical evidence.

## Adversarial audit

1. **Limit formulation.** The sequence theorem is universally quantified over admissible paths,
   includes `x → 1`, and concludes convergence in mathlib's actual weak topology on
   `ProbabilityMeasure Circle`. It is not a theorem about a selected finite set of test functions.
2. **Infinite endpoint.** The `+∞` regime is a separate theorem using an `atTop` ratio limit and has
   the pure Dirac probability measure as its conclusion. No extended-real coercion ambiguity is
   introduced.
3. **Domain and normalization.** `n+1` fixes the atom support at the positive integers. The
   logarithmic-series identity gives total mass one. Positivity of `x`, `1-x`, `L(x)`, and `q` is
   explicit; in particular, `q=0` never enters an accepted theorem.
4. **Complex logarithm branch.** Mathlib's
   `Complex.hasSum_taylorSeries_neg_log'` proves the exact series identity for `‖z‖ < 1` and returns
   the principal `Complex.log`. Taking `z = x * exp(iθ)` has norm `x < 1`, so the formal transform
   uses precisely the branch selected by the convergent power series. A modulus-only replacement
   would not satisfy the frozen surface.
5. **Fourier conventions.** `AddCircle.fourier_coe_apply` fixes the positive exponent and the
   `2π` normalization. Indices are integers. The `k=0` coefficient is exactly one, and the
   homeomorphism sends additive zero to complex one.
6. **Mode limit.** For `k ≠ 0`, the modulus identity compares the two positive scales `1-x` and
   `2*sqrt(x)*|sin(πk/q)|`. The latter is `q⁻¹` times a factor tending to `2π|k|`; logarithms
   therefore reduce the real part to the minimum of exponent ratios. The principal-log imaginary
   part lies in `(-π, π]` and vanishes after division by `L(x) → ∞`. This derivation includes
   `β=0`, `β=1`, negative `k`, and all finite `β>1`.
7. **Weak-convergence bridge.** Compactness makes every family of circle probability measures
   tight. Mathlib's Fourier star-subalgebra on `AddCircle 1` separates points and is the linear span
   of the characters. `ProbabilityMeasure.tendsto_of_tight_of_separatesPoints` therefore upgrades
   all-character convergence to weak convergence. Continuous pushforward transfers that theorem
   to `Circle`.
8. **Mixture coefficient.** From `0 ≤ β`, `min 1 β ∈ [0,1]`. The mixture accepts only a subtype of
   that interval, its masses add to one, and the endpoint lemmas identify `c=0` with Haar and
   `c=1` with the anchor.
9. **Prior art and formal reuse.** No existing Mathia PC-063 artifact or duplicate issue/PR was
   found. The implementation will reuse, rather than recreate, at least:
   `Real.hasSum_pow_div_log_of_abs_lt_one`, `Complex.hasSum_taylorSeries_neg_log'`, `PMF.toMeasure`,
   `AddCircle.haarAddCircle`, `AddCircle.fourierSubalgebra_coe`,
   `AddCircle.fourierSubalgebra_separatesPoints`, `IsTightMeasureSet.of_compactSpace`,
   `ProbabilityMeasure.tendsto_of_tight_of_separatesPoints`,
   `ProbabilityMeasure.tendsto_map_of_tendsto_of_continuous`, and
   `AddCircle.homeomorphCircle`. No exact or stronger PC-063 theorem was found in current mathlib.
10. **Current research state.** The canonical finding and issue agree. Gate 0 found no
    counterexample, stale statement, hidden finite-instance restriction, or required repair.

## Dependency and trust decision

Gate 0 resolved current mathlib at revision `2ca39e62989124794bd8405bb2e60805f63d37bc`, whose local
toolchain is Lean `4.34.0-rc2`. These are execution evidence, not a new repository pin. The focused
module will import the smallest modules exposing probability-measure weak convergence, AddCircle
Fourier/Haar infrastructure, the complex logarithm bounds/series, and required real asymptotics.
No generic Mathia harmonic-analysis framework is authorized.

The implementation must pass `lake build`, contain no `sorry`, `admit`, new axiom, `unsafe` proof,
floating-point premise, or unchecked certificate, and preserve `#print axioms` output for both
principal theorems.

Formalization research handoff: none at Gate 0. The AddCircle-to-Circle route and the identified
mathlib declarations are proof-engineering reuse, not new mathematical claims.
