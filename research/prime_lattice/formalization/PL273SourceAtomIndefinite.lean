import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.Real.Pi.Bounds
import Mathlib.Algebra.Order.Floor.Semiring
import Mathlib.LinearAlgebra.QuadraticForm.Basic

/-!
# Universal interior Weil source-atom indefiniteness

Associated finding:
`research/prime_lattice/findings/PL-273-universal-interior-weil-source-atom-indefiniteness.md`.

Formalized theorem boundary: for every real 0 < ω < 1, a positive natural
cosine frequency k has strictly negative scalar source value
2ω cos(2πkω) + sin(2πkω)/(πk), whereas the constant mode has value 2ω > 0.
The same negative mode persists in every larger band. Any real quadratic form
realizing the stated mode values is therefore indefinite.

The normalized product-to-sum and oriented interval-integral identities are
proved for sqrt(2) cos(2πkt), k > 0. The constant function is treated separately.
The zero-endpoint integral vanishes for every function; at the unit endpoint
each pure normalized cosine mode and the constant mode has scalar value 2.
A finite phase selection after reflection to min(ω, 1-ω) proves the interior
claim without a rational/irrational split or orbit-density assumption.

Not formalized: Groskin's identification of the integral with his source
matrix Q_N[δ_ω], the full endpoint matrix identity 2I (including cross-mode
orthogonality), the complete Weil form, prime-power specialization, moving
cutoff derivative jumps, or RH consequences. Indefiniteness passes from a
compression to its containing form by retaining the same vectors; applying
this to Groskin's matrices still requires that external identification.
No novelty claim is made for the kernel, trigonometric identities, or phase
selection. No quantitative first-negative-mode bound is asserted here.
-/

noncomputable section

open MeasureTheory

namespace Mathia.PL273

def modeValue (ω : ℝ) (k : ℕ) : ℝ :=
  2 * ω * Real.cos (2 * Real.pi * k * ω) +
    Real.sin (2 * Real.pi * k * ω) / (Real.pi * k)

def cosineMode (k : ℕ) (t : ℝ) : ℝ :=
  Real.sqrt 2 * Real.cos (2 * Real.pi * k * t)

def sourceValue (f : ℝ → ℝ) (ω : ℝ) : ℝ :=
  2 * ∫ t in 0..ω, f t * f (ω - t)

@[simp] theorem constant_mode (ω : ℝ) : modeValue ω 0 = 2 * ω := by
  simp [modeValue]

@[simp] theorem sourceValue_zero (f : ℝ → ℝ) : sourceValue f 0 = 0 := by
  simp [sourceValue]

@[simp] theorem sourceValue_constant (ω : ℝ) : sourceValue (fun _ => 1) ω = 2 * ω := by
  simp [sourceValue]

@[simp] theorem modeValue_zero (k : ℕ) : modeValue 0 k = 0 := by
  simp [modeValue]

@[simp] theorem modeValue_one (k : ℕ) : modeValue 1 k = 2 := by
  have ha : 2 * Real.pi * (k : ℝ) * 1 = (k : ℝ) * (2 * Real.pi) := by ring
  have hs := Real.sin_nat_mul_two_pi_sub 0 k
  simp only [sub_zero, Real.sin_zero, neg_zero] at hs
  simp [modeValue, ha, Real.cos_nat_mul_two_pi, hs]

theorem cosine_product (ω t : ℝ) (k : ℕ) :
    2 * cosineMode k t * cosineMode k (ω - t) =
      2 * Real.cos (2 * Real.pi * k * ω) +
        2 * Real.cos (4 * Real.pi * k * t - 2 * Real.pi * k * ω) := by
  have hs : Real.sqrt 2 * Real.sqrt 2 = 2 := Real.mul_self_sqrt (by norm_num)
  have ha : 2 * Real.pi * (k : ℝ) * ω =
      2 * Real.pi * k * t + 2 * Real.pi * k * (ω - t) := by ring
  have hb : 4 * Real.pi * (k : ℝ) * t - 2 * Real.pi * k * ω =
      2 * Real.pi * k * t - 2 * Real.pi * k * (ω - t) := by ring
  rw [hb, ha, Real.cos_add, Real.cos_sub]
  dsimp [cosineMode]
  linear_combination 2 * Real.cos (2 * Real.pi * k * t) *
    Real.cos (2 * Real.pi * k * (ω - t)) * hs

theorem sourceValue_cosine (ω : ℝ) {k : ℕ} (hk : 0 < k) :
    sourceValue (cosineMode k) ω = modeValue ω k := by
  have hkR : (k : ℝ) ≠ 0 := by exact_mod_cast hk.ne'
  have hc : 4 * Real.pi * (k : ℝ) ≠ 0 := by positivity
  have hcInt : IntervalIntegrable
      (fun t : ℝ => 2 * Real.cos (4 * Real.pi * k * t - 2 * Real.pi * k * ω))
      volume 0 ω := by
    apply Continuous.intervalIntegrable
    fun_prop
  have hproduct : (fun t => 2 * (cosineMode k t * cosineMode k (ω - t))) =
      (fun t => 2 * Real.cos (2 * Real.pi * k * ω) +
        2 * Real.cos (4 * Real.pi * k * t - 2 * Real.pi * k * ω)) := by
    funext t
    simpa only [mul_assoc] using cosine_product ω t k
  unfold sourceValue
  rw [← intervalIntegral.integral_const_mul, hproduct]
  rw [intervalIntegral.integral_add intervalIntegrable_const hcInt,
    intervalIntegral.integral_const, intervalIntegral.integral_const_mul,
    intervalIntegral.integral_comp_mul_sub Real.cos hc, integral_cos]
  have ha : 4 * Real.pi * (k : ℝ) * ω - 2 * Real.pi * k * ω =
      2 * Real.pi * k * ω := by ring
  simp only [mul_zero, zero_sub, sub_zero, smul_eq_mul, ha, Real.sin_neg]
  unfold modeValue
  field_simp
  ring

/-- One finite progression reaches the negative cosine arc. The proof uses a ceiling
when the step is at most one third, and its first term otherwise. -/
private lemma exists_phase {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ ≤ 1 / 2) :
    ∃ k : ℕ, 0 < k ∧ 1 / 3 ≤ (k : ℝ) * δ ∧ (k : ℝ) * δ ≤ 2 / 3 := by
  by_cases hδ3 : δ ≤ 1 / 3
  · let k : ℕ := ⌈1 / (3 * δ)⌉₊
    have hdiv : 0 < 1 / (3 * δ) := by positivity
    have hk : 0 < k := Nat.one_le_ceil_iff.mpr hdiv
    have hlo : 1 / (3 * δ) ≤ (k : ℝ) := Nat.le_ceil _
    have hhi : (k : ℝ) < 1 / (3 * δ) + 1 := Nat.ceil_lt_add_one hdiv.le
    have hid : (1 / (3 * δ)) * δ = 1 / 3 := by field_simp
    refine ⟨k, hk, ?_, ?_⟩
    · nlinarith [mul_le_mul_of_nonneg_right hlo hδ0.le]
    · nlinarith [mul_lt_mul_of_pos_right hhi hδ0]
  · refine ⟨1, by decide, ?_, ?_⟩ <;> norm_num <;> linarith

/-- The central third of a turn has cosine at most minus one half. -/
private lemma cos_phase_bound {x : ℝ} (hx0 : 1 / 3 ≤ x) (hx1 : x ≤ 2 / 3) :
    Real.cos (2 * Real.pi * x) ≤ -(1 / 2) := by
  have hπ := Real.pi_pos
  have hcos : Real.cos (2 * Real.pi / 3) = -(1 / 2) := by
    rw [show 2 * Real.pi / 3 = Real.pi - Real.pi / 3 by ring,
      Real.cos_pi_sub, Real.cos_pi_div_three]
  by_cases hx : x ≤ 1 / 2
  · rw [← hcos]
    exact Real.cos_le_cos_of_nonneg_of_le_pi (by positivity)
      (by nlinarith) (by nlinarith)
  · rw [← Real.cos_two_pi_sub (2 * Real.pi * x), ← hcos]
    exact Real.cos_le_cos_of_nonneg_of_le_pi (by positivity)
      (by nlinarith) (by nlinarith)

/-- Every interior atom has a strictly negative positive-frequency cosine mode.
Reflection to the nearer endpoint gives a finite phase witness. Its phase lower
bound also controls the sine correction, so no orbit-density argument is needed. -/
theorem exists_negative_mode {ω : ℝ} (hω0 : 0 < ω) (hω1 : ω < 1) :
    ∃ k : ℕ, 0 < k ∧ modeValue ω k < 0 := by
  let δ := min ω (1 - ω)
  have hδ0 : 0 < δ := lt_min hω0 (by linarith)
  have hδω : δ ≤ ω := min_le_left _ _
  have hδ1 : δ ≤ 1 / 2 := by
    have hd := min_le_right ω (1 - ω)
    change min ω (1 - ω) ≤ 1 / 2
    linarith
  obtain ⟨k, hk, hlo, hhi⟩ := exists_phase hδ0 hδ1
  have hkR : (0 : ℝ) < k := by exact_mod_cast hk
  have hphase := cos_phase_bound hlo hhi
  have hcos : Real.cos (2 * Real.pi * k * ω) ≤ -(1 / 2) := by
    by_cases hw : ω ≤ 1 - ω
    · simpa [δ, min_eq_left hw, mul_assoc] using hphase
    · have hd : δ = 1 - ω := min_eq_right (le_of_not_ge hw)
      have hreflect : Real.cos (2 * Real.pi * k * ω) =
          Real.cos (2 * Real.pi * ((k : ℝ) * δ)) := by
        rw [hd]
        calc
          Real.cos (2 * Real.pi * k * ω) =
              Real.cos ((k : ℝ) * (2 * Real.pi) - 2 * Real.pi * ((k : ℝ) * (1 - ω))) := by congr 1; ring
          _ = Real.cos (2 * Real.pi * ((k : ℝ) * (1 - ω))) :=
            Real.cos_nat_mul_two_pi_sub _ k
      rw [hreflect]
      exact hphase
  have hkw : 1 / 3 ≤ (k : ℝ) * ω :=
    hlo.trans (mul_le_mul_of_nonneg_left hδω hkR.le)
  have hden : 0 < Real.pi * (k : ℝ) := mul_pos Real.pi_pos hkR
  have herr : 1 / (Real.pi * (k : ℝ)) < ω := by
    apply (div_lt_iff₀ hden).2
    nlinarith [Real.pi_gt_three]
  have hmain : 2 * ω * Real.cos (2 * Real.pi * k * ω) ≤ -ω := by
    nlinarith
  have hsin : Real.sin (2 * Real.pi * k * ω) / (Real.pi * k) ≤
      1 / (Real.pi * k) := div_le_div_of_nonneg_right (Real.sin_le_one _) hden.le
  refine ⟨k, hk, ?_⟩
  unfold modeValue
  linarith

/-- Both signs occur among the actual scalar mode values in a finite Fourier band. -/
def HasBothSignsInBand (ω : ℝ) (N : ℕ) : Prop :=
  ∃ p ≤ N, ∃ n ≤ N, 0 < modeValue ω p ∧ modeValue ω n < 0

/-- One fixed negative mode, paired with the constant mode, works in every larger band. -/
theorem permanent_two_signs {ω : ℝ} (hω0 : 0 < ω) (hω1 : ω < 1) :
    ∃ k : ℕ, 0 < k ∧ modeValue ω k < 0 ∧
      ∀ N : ℕ, k ≤ N → HasBothSignsInBand ω N := by
  obtain ⟨k, hk, hneg⟩ := exists_negative_mode hω0 hω1
  refine ⟨k, hk, hneg, ?_⟩
  intro N hN
  refine ⟨0, Nat.zero_le N, k, hN, ?_, hneg⟩
  simpa using mul_pos (by norm_num : (0 : ℝ) < 2) hω0

/-- A real quadratic form is indefinite when it takes both strictly positive and
strictly negative values. No choice of diagonal or off-diagonal entries is imposed. -/
def IsIndefinite {V : Type*} [AddCommGroup V] [Module ℝ V]
    (Q : QuadraticForm ℝ V) : Prop :=
  (∃ v, 0 < Q v) ∧ (∃ v, Q v < 0)

theorem indefinite_of_two_values {V : Type*} [AddCommGroup V] [Module ℝ V]
    (Q : QuadraticForm ℝ V) {p n : V} (hp : 0 < Q p) (hn : Q n < 0) :
    IsIndefinite Q := ⟨⟨p, hp⟩, ⟨n, hn⟩⟩

/-- The two-sign condition excludes either semidefinite sign. -/
theorem IsIndefinite.not_semidefinite {V : Type*} [AddCommGroup V] [Module ℝ V]
    {Q : QuadraticForm ℝ V} (hQ : IsIndefinite Q) :
    ¬ (∀ v, 0 ≤ Q v) ∧ ¬ (∀ v, Q v ≤ 0) := by
  obtain ⟨⟨p, hp⟩, ⟨n, hn⟩⟩ := hQ
  exact ⟨fun h => (not_lt_of_ge (h n)) hn,
    fun h => (not_lt_of_ge (h p)) hp⟩

/-- Any quadratic form realizing these mode values is indefinite. The realization
hypothesis is explicit: this lemma does not construct Groskin's source matrix. -/
theorem indefinite_of_band_values {ω : ℝ} {N : ℕ}
    (hband : HasBothSignsInBand ω N)
    {V : Type*} [AddCommGroup V] [Module ℝ V]
    (Q : QuadraticForm ℝ V) (v : Fin (N + 1) → V)
    (hv : ∀ i, Q (v i) = modeValue ω i.val) : IsIndefinite Q := by
  obtain ⟨p, hpN, n, hnN, hp, hn⟩ := hband
  let i : Fin (N + 1) := ⟨p, Nat.lt_succ_of_le hpN⟩
  let j : Fin (N + 1) := ⟨n, Nat.lt_succ_of_le hnN⟩
  apply indefinite_of_two_values Q (p := v i) (n := v j)
  · simpa [hv, i] using hp
  · simpa [hv, j] using hn

#print axioms cosine_product
#print axioms sourceValue_cosine
#print axioms sourceValue_constant
#print axioms sourceValue_zero
#print axioms modeValue_one
#print axioms exists_negative_mode
#print axioms permanent_two_signs
#print axioms indefinite_of_band_values
#print axioms IsIndefinite.not_semidefinite

end Mathia.PL273
