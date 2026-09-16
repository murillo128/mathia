import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Analysis.Normed.Operator.Basic
import Mathlib.Data.Finset.Lattice.Fold
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FinCases
import Mathlib.Topology.Algebra.Module.ContinuousLinearMap.PiProd

/-!
# Sharp propagation bounds for finite martingale kernels

Associated finding:
`research/weil_positivity/findings/WP-336-ucp-kadison-defect-is-controlled-by-channel-norm-times-bidirectional-propagation.md`

Formalized theorem boundary: the finite martingale-kernel propagation inequality,
the exact induced sup-norm/escape identity and resulting global bound, and the
WP-335 three-point equality certificate (including the endpoint case `a = 1`).
The row proof gives the exact endpoint slack of the classical Bhatia--Davis bound.
Coordinates may be arbitrary real functions; an injective realization specializes
to a finite subset of the real line. The three-point realization is injective.

Norm convention: real functions have mathlib's finite Pi sup norm; `channel` is
an actual continuous linear map. Signed-row variation is the full sum of absolute
weights, with no factor of one half. This real-valued realization has the same
numerical norm as the commutative complex channel; no C*-algebra interface is used.

Not formalized: the Mangoldt source construction, infinite/asymptotic statements,
Stinespring couplings, archimedean completion, the Weil form, or RH consequences.
-/

noncomputable section
open Finset
namespace Mathia.WP336

/-- A finite Markov kernel; barycentricity is imposed only on the chosen observable. -/
structure Kernel (ι : Type*) [Fintype ι] where
  weight : ι → ι → ℝ
  nonneg : ∀ x y, 0 ≤ weight x y
  sum_one : ∀ x, ∑ y, weight x y = 1

variable {ι : Type*} [Fintype ι] [DecidableEq ι]

def escape (P : Kernel ι) (x : ι) : ℝ := 1 - P.weight x x

def defect (P : Kernel ι) (X : ι → ℝ) (x : ι) : ℝ :=
  ∑ y, P.weight x y * X y ^ 2 - X x ^ 2

/-- The support of a stochastic row uses strictly positive weights. -/
def rowSupport (P : Kernel ι) (x : ι) : Finset ι :=
  univ.filter fun y => 0 < P.weight x y

omit [DecidableEq ι] in
lemma mem_rowSupport (P : Kernel ι) (x y : ι) :
    y ∈ rowSupport P x ↔ 0 < P.weight x y := by
  simp [rowSupport]

omit [DecidableEq ι] in
lemma rowSupport_nonempty (P : Kernel ι) (x : ι) : (rowSupport P x).Nonempty := by
  by_contra h
  have hz : ∀ y, P.weight x y = 0 := by
    intro y
    have : ¬ 0 < P.weight x y := by
      intro hp
      exact h ⟨y, (mem_rowSupport P x y).mpr hp⟩
    exact le_antisymm (le_of_not_gt this) (P.nonneg x y)
  have := P.sum_one x
  simp [hz] at this

/-- Actual minimum and maximum coordinates of the positive support. -/
def supportMin (P : Kernel ι) (X : ι → ℝ) (x : ι) : ℝ :=
  (rowSupport P x).inf' (rowSupport_nonempty P x) X

def supportMax (P : Kernel ι) (X : ι → ℝ) (x : ι) : ℝ :=
  (rowSupport P x).sup' (rowSupport_nonempty P x) X

def leftRadius (P : Kernel ι) (X : ι → ℝ) (x : ι) : ℝ := X x - supportMin P X x

def rightRadius (P : Kernel ι) (X : ι → ℝ) (x : ι) : ℝ := supportMax P X x - X x

omit [DecidableEq ι] in
lemma supportMin_le (P : Kernel ι) (X : ι → ℝ) (x y : ι)
    (hy : 0 < P.weight x y) : supportMin P X x ≤ X y := by
  exact Finset.inf'_le X ((mem_rowSupport P x y).mpr hy)

omit [DecidableEq ι] in
lemma le_supportMax (P : Kernel ι) (X : ι → ℝ) (x y : ι)
    (hy : 0 < P.weight x y) : X y ≤ supportMax P X x := by
  exact Finset.le_sup' X ((mem_rowSupport P x y).mpr hy)

omit [DecidableEq ι] in
lemma center_mem_support_interval (P : Kernel ι) (X : ι → ℝ) (x : ι)
    (hmean : ∑ y, P.weight x y * X y = X x) :
    supportMin P X x ≤ X x ∧ X x ≤ supportMax P X x := by
  constructor
  · calc
      supportMin P X x = ∑ y, P.weight x y * supportMin P X x := by
        rw [← sum_mul, P.sum_one, one_mul]
      _ ≤ ∑ y, P.weight x y * X y := by
        apply sum_le_sum
        intro y _
        by_cases hy : 0 < P.weight x y
        · exact mul_le_mul_of_nonneg_left (supportMin_le P X x y hy) (P.nonneg x y)
        · have hz : P.weight x y = 0 := le_antisymm (le_of_not_gt hy) (P.nonneg x y)
          simp [hz]
      _ = X x := hmean
  · calc
      X x = ∑ y, P.weight x y * X y := hmean.symm
      _ ≤ ∑ y, P.weight x y * supportMax P X x := by
        apply sum_le_sum
        intro y _
        by_cases hy : 0 < P.weight x y
        · exact mul_le_mul_of_nonneg_left (le_supportMax P X x y hy) (P.nonneg x y)
        · have hz : P.weight x y = 0 := le_antisymm (le_of_not_gt hy) (P.nonneg x y)
          simp [hz]
      _ = supportMax P X x := by rw [← sum_mul, P.sum_one, one_mul]

omit [DecidableEq ι] in
lemma radii_nonneg (P : Kernel ι) (X : ι → ℝ) (x : ι)
    (hmean : ∑ y, P.weight x y * X y = X x) :
    0 ≤ leftRadius P X x ∧ 0 ≤ rightRadius P X x := by
  have hm := center_mem_support_interval P X x hmean
  exact ⟨sub_nonneg.mpr hm.1, sub_nonneg.mpr hm.2⟩

omit [DecidableEq ι] in
/-- Exact centering, using the barycentric condition and row mass one. -/
theorem defect_eq_centered (P : Kernel ι) (X : ι → ℝ) (x : ι)
    (hmean : ∑ y, P.weight x y * X y = X x) :
    defect P X x = ∑ y, P.weight x y * (X y - X x) ^ 2 := by
  have hpoly : (∑ y, P.weight x y * (X y - X x) ^ 2) =
      (∑ y, P.weight x y * X y ^ 2) - 2 * (∑ y, P.weight x y * X y) * X x +
      (∑ y, P.weight x y) * X x ^ 2 := by
    simp only [sum_mul, mul_sum, ← sum_sub_distrib, ← sum_add_distrib]
    apply sum_congr rfl
    intro y _
    ring
  rw [hpoly, hmean, P.sum_one]
  unfold defect
  ring

/-- The exact Bhatia--Davis slack, with the diagonal contribution removed.
It avoids conditioning, so deterministic rows require no exceptional definition. -/
theorem propagation_slack (P : Kernel ι) (X : ι → ℝ) (x : ι)
    (hmean : ∑ y, P.weight x y * X y = X x) :
    escape P x * leftRadius P X x * rightRadius P X x - defect P X x =
      ∑ y ∈ univ.erase x, P.weight x y *
        (X y - supportMin P X x) * (supportMax P X x - X y) := by
  let m := supportMin P X x
  let M := supportMax P X x
  have hpoly : (∑ y, P.weight x y * (X y - m) * (M - X y)) =
      (M + m) * (∑ y, P.weight x y * X y) -
      (∑ y, P.weight x y * X y ^ 2) - m * M * (∑ y, P.weight x y) := by
    simp only [mul_sum, ← sum_sub_distrib]
    apply sum_congr rfl
    intro y _
    ring
  have herase := sum_erase_add univ
    (fun y => P.weight x y * (X y - m) * (M - X y)) (mem_univ x)
  rw [hpoly, hmean, P.sum_one] at herase
  change (1 - P.weight x x) * (X x - m) * (M - X x) -
    ((∑ y, P.weight x y * X y ^ 2) - X x ^ 2) = _
  nlinarith only [herase]

/-- Sharp propagation bound for each exact martingale row. -/
theorem row_propagation_bound (P : Kernel ι) (X : ι → ℝ) (x : ι)
    (hmean : ∑ y, P.weight x y * X y = X x) :
    0 ≤ defect P X x ∧
      defect P X x ≤ escape P x * leftRadius P X x * rightRadius P X x := by
  constructor
  · rw [defect_eq_centered P X x hmean]
    exact sum_nonneg fun y _ => mul_nonneg (P.nonneg x y) (sq_nonneg _)
  · have hslack := propagation_slack P X x hmean
    have hnonneg : 0 ≤ ∑ y ∈ univ.erase x, P.weight x y *
        (X y - supportMin P X x) * (supportMax P X x - X y) := by
      apply sum_nonneg
      intro y _
      by_cases hy : 0 < P.weight x y
      · exact mul_nonneg (mul_nonneg (P.nonneg x y)
          (sub_nonneg.mpr (supportMin_le P X x y hy)))
          (sub_nonneg.mpr (le_supportMax P X x y hy))
      · have hz : P.weight x y = 0 := le_antisymm (le_of_not_gt hy) (P.nonneg x y)
        simp [hz]
    linarith


omit [DecidableEq ι] in
/-- A useful way to compute the genuine support minimum without enumerating zero weights. -/
lemma supportMin_eq_of_bounds (P : Kernel ι) (X : ι → ℝ) (x : ι) (m : ℝ)
    (hb : ∀ y, 0 < P.weight x y → m ≤ X y)
    (he : ∃ y, 0 < P.weight x y ∧ X y = m) : supportMin P X x = m := by
  apply le_antisymm
  · obtain ⟨y, hy, rfl⟩ := he
    exact supportMin_le P X x y hy
  · exact Finset.le_inf' (rowSupport_nonempty P x) X
      (fun y hy => hb y ((mem_rowSupport P x y).mp hy))

omit [DecidableEq ι] in
lemma supportMax_eq_of_bounds (P : Kernel ι) (X : ι → ℝ) (x : ι) (M : ℝ)
    (hb : ∀ y, 0 < P.weight x y → X y ≤ M)
    (he : ∃ y, 0 < P.weight x y ∧ X y = M) : supportMax P X x = M := by
  apply le_antisymm
  · exact Finset.sup'_le (rowSupport_nonempty P x) X
      (fun y hy => hb y ((mem_rowSupport P x y).mp hy))
  · obtain ⟨y, hy, rfl⟩ := he
    exact le_supportMax P X x y hy

/-- A deterministic row has zero propagation radii, including singleton spectra. -/
lemma deterministic_radii (P : Kernel ι) (X : ι → ℝ) (x : ι)
    (hrow : ∀ y, P.weight x y = if y = x then 1 else 0) :
    leftRadius P X x = 0 ∧ rightRadius P X x = 0 := by
  have hs : ∀ y, 0 < P.weight x y → y = x := by
    intro y hy
    by_contra h
    simp [hrow y, h] at hy
  have hpos : 0 < P.weight x x := by simp [hrow x]
  have hlo := supportMin_eq_of_bounds P X x (X x)
    (fun y hy => by rw [hs y hy]) ⟨x, hpos, rfl⟩
  have hhi := supportMax_eq_of_bounds P X x (X x)
    (fun y hy => by rw [hs y hy]) ⟨x, hpos, rfl⟩
  simp [leftRadius, rightRadius, hlo, hhi]




variable {ι : Type*} [Fintype ι] [DecidableEq ι]

omit [DecidableEq ι] in
lemma weight_le_one (P : Kernel ι) (x y : ι) : P.weight x y ≤ 1 := by
  have h := Finset.single_le_sum (fun z _ => P.nonneg x z) (Finset.mem_univ y)
  simpa only [P.sum_one x] using h

omit [DecidableEq ι] in
lemma escape_nonneg (P : Kernel ι) (x : ι) : 0 ≤ escape P x :=
  sub_nonneg.mpr (weight_le_one P x x)

/-- The stochastic matrix acts on real functions with mathlib's finite Pi sup norm. -/
def channel (P : Kernel ι) : (ι → ℝ) →L[ℝ] (ι → ℝ) :=
  ContinuousLinearMap.pi fun x => ∑ y, P.weight x y • ContinuousLinearMap.proj y

omit [DecidableEq ι] in
@[simp] lemma channel_apply (P : Kernel ι) (f : ι → ℝ) (x : ι) :
    channel P f x = ∑ y, P.weight x y * f y := by
  simp [channel]

lemma channel_sub_id_apply (P : Kernel ι) (f : ι → ℝ) (x : ι) :
    (channel P - ContinuousLinearMap.id ℝ (ι → ℝ)) f x =
      ∑ y, (P.weight x y - if y = x then 1 else 0) * f y := by
  simp [Finset.sum_sub_distrib, sub_mul]

/-- Full variation of a signed row, with no factor of one half. -/
lemma signed_row_variation (P : Kernel ι) (x : ι) :
    ∑ y, |P.weight x y - if y = x then 1 else 0| = 2 * escape P x := by
  rw [← Finset.sum_erase_add _ _ (Finset.mem_univ x)]
  have hsum : (∑ y ∈ Finset.univ.erase x,
      |P.weight x y - if y = x then 1 else 0|) =
      ∑ y ∈ Finset.univ.erase x, P.weight x y := by
    apply Finset.sum_congr rfl
    intro y hy
    simp [Finset.mem_erase.mp hy, abs_of_nonneg (P.nonneg x y)]
  rw [hsum]
  simp only [ite_true]
  rw [abs_of_nonpos (sub_nonpos.mpr (weight_le_one P x x))]
  have htotal := P.sum_one x
  rw [← Finset.sum_erase_add _ _ (Finset.mem_univ x)] at htotal
  dsimp [escape]
  linarith

/-- A sign function that attains the full variation of row `x`. -/
def rowWitness (x : ι) : ι → ℝ := fun y => if y = x then -1 else 1

lemma rowWitness_norm (x : ι) : ‖rowWitness x‖ = 1 := by
  apply le_antisymm
  · apply (pi_norm_le_iff_of_nonneg (by norm_num : (0 : ℝ) ≤ 1)).2
    intro y
    dsimp [rowWitness]
    split_ifs <;> norm_num
  · have h := norm_le_pi_norm (rowWitness x) x
    simpa [rowWitness] using h

lemma rowWitness_attains (P : Kernel ι) (x : ι) :
    (channel P - ContinuousLinearMap.id ℝ (ι → ℝ)) (rowWitness x) x =
      2 * escape P x := by
  rw [channel_sub_id_apply, ← signed_row_variation]
  apply Finset.sum_congr rfl
  intro y _
  by_cases hy : y = x
  · subst y
    simp [rowWitness, abs_of_nonpos (sub_nonpos.mpr (weight_le_one P x x))]
  · simp [rowWitness, hy, abs_of_nonneg (P.nonneg x y)]

lemma channel_row_norm_le (P : Kernel ι) (f : ι → ℝ) (x : ι) :
    ‖(channel P - ContinuousLinearMap.id ℝ (ι → ℝ)) f x‖ ≤
      (2 * escape P x) * ‖f‖ := by
  rw [channel_sub_id_apply, ← signed_row_variation, Finset.sum_mul]
  apply (norm_sum_le _ _).trans
  apply Finset.sum_le_sum
  intro y _
  rw [norm_mul, Real.norm_eq_abs]
  exact mul_le_mul_of_nonneg_left (norm_le_pi_norm f y) (abs_nonneg _)

lemma channel_row_variation_le_norm (P : Kernel ι) (x : ι) :
    2 * escape P x ≤ ‖channel P - ContinuousLinearMap.id ℝ (ι → ℝ)‖ := by
  have h := (norm_le_pi_norm
    ((channel P - ContinuousLinearMap.id ℝ (ι → ℝ)) (rowWitness x)) x).trans
      ((channel P - ContinuousLinearMap.id ℝ (ι → ℝ)).le_opNorm (rowWitness x))
  rw [rowWitness_attains, rowWitness_norm, mul_one,
    Real.norm_eq_abs, abs_of_nonneg (mul_nonneg (by norm_num) (escape_nonneg P x))] at h
  exact h

lemma channel_norm_eq [Nonempty ι] (P : Kernel ι) :
    ‖channel P - ContinuousLinearMap.id ℝ (ι → ℝ)‖ =
      2 * Finset.univ.sup' Finset.univ_nonempty (escape P) := by
  let M := Finset.univ.sup' Finset.univ_nonempty (escape P)
  have hM : 0 ≤ M := (escape_nonneg P (Classical.arbitrary ι)).trans
    (Finset.le_sup' (escape P) (Finset.mem_univ _))
  apply le_antisymm
  · apply ContinuousLinearMap.opNorm_le_bound _ (mul_nonneg (by norm_num) hM)
    intro f
    apply (pi_norm_le_iff_of_nonneg (mul_nonneg (mul_nonneg (by norm_num) hM)
      (norm_nonneg f))).2
    intro x
    exact (channel_row_norm_le P f x).trans
      (mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left
        (Finset.le_sup' (escape P) (Finset.mem_univ x)) (by norm_num)) (norm_nonneg f))
  · have h : M ≤ ‖channel P - ContinuousLinearMap.id ℝ (ι → ℝ)‖ / 2 := by
      apply Finset.sup'_le
      intro x _
      have hx := channel_row_variation_le_norm P x
      linarith
    dsimp [M] at h
    linarith

lemma channel_norm_eq_max_row_variation [Nonempty ι] (P : Kernel ι) :
    ‖channel P - ContinuousLinearMap.id ℝ (ι → ℝ)‖ =
      Finset.univ.sup' Finset.univ_nonempty
        (fun x => ∑ y, |P.weight x y - if y = x then 1 else 0|) := by
  simp_rw [signed_row_variation]
  rw [channel_norm_eq]
  apply le_antisymm
  · have h : Finset.univ.sup' Finset.univ_nonempty (escape P) ≤
        (Finset.univ.sup' Finset.univ_nonempty (fun x => 2 * escape P x)) / 2 := by
      apply Finset.sup'_le
      intro x _
      have hx := Finset.le_sup' (fun x => 2 * escape P x) (Finset.mem_univ x)
      linarith
    linarith
  · apply Finset.sup'_le
    intro x _
    exact mul_le_mul_of_nonneg_left
      (Finset.le_sup' (escape P) (Finset.mem_univ x)) (by norm_num)


/-- The genuine maximum of the products of the one-sided support radii. -/
def propagationBudget [Nonempty ι] (P : Kernel ι) (X : ι → ℝ) : ℝ :=
  univ.sup' univ_nonempty fun x => leftRadius P X x * rightRadius P X x

omit [DecidableEq ι] in
lemma propagationBudget_nonneg [Nonempty ι] (P : Kernel ι) (X : ι → ℝ)
    (hmean : ∀ x, ∑ y, P.weight x y * X y = X x) :
    0 ≤ propagationBudget P X := by
  let x : ι := Classical.arbitrary ι
  exact (mul_nonneg (radii_nonneg P X x (hmean x)).1
    (radii_nonneg P X x (hmean x)).2).trans
    (le_sup' (fun z => leftRadius P X z * rightRadius P X z) (mem_univ x))

omit [DecidableEq ι] in
/-- The coordinate Kadison defect is literally the channel's square defect. -/
lemma channel_square_defect (P : Kernel ι) (X : ι → ℝ) :
    channel P (fun x => X x ^ 2) - (fun x => X x ^ 2) = defect P X := by
  funext x
  simp [defect]

/-- WP-336's global propagation bound, in the actual induced finite sup norm. -/
theorem global_propagation_bound [Nonempty ι] (P : Kernel ι) (X : ι → ℝ)
    (hmean : ∀ x, ∑ y, P.weight x y * X y = X x) :
    ‖channel P (fun x => X x ^ 2) - (fun x => X x ^ 2)‖ ≤
      (1 / 2 : ℝ) * ‖channel P - ContinuousLinearMap.id ℝ (ι → ℝ)‖ *
        propagationBudget P X := by
  rw [channel_square_defect]
  apply (pi_norm_le_iff_of_nonneg (by
    have := propagationBudget_nonneg P X hmean
    positivity)).mpr
  intro x
  rw [Real.norm_eq_abs, abs_of_nonneg (row_propagation_bound P X x (hmean x)).1]
  have hr := radii_nonneg P X x (hmean x)
  have he : escape P x ≤
      (1 / 2 : ℝ) * ‖channel P - ContinuousLinearMap.id ℝ (ι → ℝ)‖ := by
    have := channel_row_variation_le_norm P x
    linarith
  calc
    defect P X x ≤ escape P x * leftRadius P X x * rightRadius P X x :=
      (row_propagation_bound P X x (hmean x)).2
    _ = escape P x * (leftRadius P X x * rightRadius P X x) := by ring
    _ ≤ ((1 / 2 : ℝ) * ‖channel P - ContinuousLinearMap.id ℝ (ι → ℝ)‖) *
        (leftRadius P X x * rightRadius P X x) :=
      mul_le_mul_of_nonneg_right he (mul_nonneg hr.1 hr.2)
    _ ≤ _ := mul_le_mul_of_nonneg_left (le_sup' (fun z => leftRadius P X z * rightRadius P X z) (mem_univ x)) (by positivity)




/-- WP-335 coordinates relative to the central source point. -/
def threeCoordinate (a : ℕ) (h : ℝ) : Fin 3 → ℝ := ![-(a : ℝ) * h, 0, h]

/-- The endpoint rows are deterministic; only the central row can escape. -/
def threeWeight (a : ℕ) (x y : Fin 3) : ℝ :=
  if x = 1 then ![1 / ((a : ℝ) * ((a : ℝ) + 1)), 1 - 1 / (a : ℝ),
    1 / ((a : ℝ) + 1)] y else if x = y then 1 else 0

/-- The exact three-point martingale kernel, including the boundary case `a = 1`. -/
def threeKernel (a : ℕ) (ha : 1 ≤ a) : Kernel (Fin 3) where
  weight := threeWeight a
  nonneg := by
    have haR : (1 : ℝ) ≤ a := by exact_mod_cast ha
    have hapos : (0 : ℝ) < a := lt_of_lt_of_le zero_lt_one haR
    intro x y
    fin_cases x <;> fin_cases y <;> simp [threeWeight]
    · positivity
    · simpa only [one_div] using (div_le_one hapos).mpr haR
    · positivity
  sum_one := by
    have haR : (1 : ℝ) ≤ a := by exact_mod_cast ha
    have hapos : (0 : ℝ) < a := lt_of_lt_of_le zero_lt_one haR
    have ha0 : (a : ℝ) ≠ 0 := ne_of_gt hapos
    have hap0 : (a : ℝ) + 1 ≠ 0 := by positivity
    intro x
    fin_cases x <;> simp [threeWeight, Fin.sum_univ_succ]
    field_simp
    ring

@[simp] theorem threeKernel_weight (a : ℕ) (ha : 1 ≤ a) (x y : Fin 3) :
    (threeKernel a ha).weight x y = threeWeight a x y := rfl

theorem threeKernel_barycentric (a : ℕ) (ha : 1 ≤ a) (h : ℝ) (x : Fin 3) :
    ∑ y, (threeKernel a ha).weight x y * threeCoordinate a h y =
      threeCoordinate a h x := by
  have haR : (1 : ℝ) ≤ a := by exact_mod_cast ha
  have ha0 : (a : ℝ) ≠ 0 := ne_of_gt (lt_of_lt_of_le zero_lt_one haR)
  have hap0 : (a : ℝ) + 1 ≠ 0 := by positivity
  fin_cases x <;> simp [threeWeight, threeCoordinate, Fin.sum_univ_succ]
  field_simp
  ring

@[simp] theorem threeKernel_escape (a : ℕ) (ha : 1 ≤ a) (x : Fin 3) :
    escape (threeKernel a ha) x = if x = 1 then 1 / (a : ℝ) else 0 := by
  fin_cases x <;> simp [escape, threeWeight]

@[simp] theorem threeKernel_defect (a : ℕ) (ha : 1 ≤ a) (h : ℝ) (x : Fin 3) :
    defect (threeKernel a ha) (threeCoordinate a h) x =
      if x = 1 then h ^ 2 else 0 := by
  have haR : (1 : ℝ) ≤ a := by exact_mod_cast ha
  have ha0 : (a : ℝ) ≠ 0 := ne_of_gt (lt_of_lt_of_le zero_lt_one haR)
  have hap0 : (a : ℝ) + 1 ≠ 0 := by positivity
  fin_cases x <;> simp [defect, threeWeight, threeCoordinate, Fin.sum_univ_succ]
  field_simp

theorem threeKernel_left_pos (a : ℕ) (ha : 1 ≤ a) :
    0 < (threeKernel a ha).weight 1 0 := by
  have haR : (1 : ℝ) ≤ a := by exact_mod_cast ha
  simp only [threeKernel_weight, threeWeight, ↓reduceIte, Matrix.cons_val_zero]
  positivity

theorem threeKernel_right_pos (a : ℕ) (ha : 1 ≤ a) :
    0 < (threeKernel a ha).weight 1 2 := by
  simp [threeWeight]
  positivity

theorem threeCoordinate_bounds (a : ℕ) (ha : 1 ≤ a) (h : ℝ) (hh : 0 < h)
    (x : Fin 3) :
    -(a : ℝ) * h ≤ threeCoordinate a h x ∧ threeCoordinate a h x ≤ h := by
  have haR : (1 : ℝ) ≤ a := by exact_mod_cast ha
  fin_cases x <;> simp [threeCoordinate] <;> (try constructor) <;> nlinarith

theorem threeCoordinate_injective (a : ℕ) (ha : 1 ≤ a) (h : ℝ) (hh : 0 < h) :
    Function.Injective (threeCoordinate a h) := by
  have haR : (1 : ℝ) ≤ a := by exact_mod_cast ha
  have ha0 : a ≠ 0 := Nat.ne_of_gt (lt_of_lt_of_le Nat.zero_lt_one ha)
  intro x y hxy
  fin_cases x <;> fin_cases y <;>
    simp [threeCoordinate, ha0, ne_of_gt hh] at hxy ⊢ <;> nlinarith


/-- Both support endpoints have positive weight even when the central weight vanishes. -/
theorem threeKernel_center_radii (a : ℕ) (ha : 1 ≤ a) (h : ℝ) (hh : 0 < h) :
    leftRadius (threeKernel a ha) (threeCoordinate a h) 1 = (a : ℝ) * h ∧
    rightRadius (threeKernel a ha) (threeCoordinate a h) 1 = h := by
  have hlo := supportMin_eq_of_bounds (threeKernel a ha) (threeCoordinate a h) 1
    (-(a : ℝ) * h) (fun y _ => (threeCoordinate_bounds a ha h hh y).1)
    ⟨0, threeKernel_left_pos a ha, rfl⟩
  have hhi := supportMax_eq_of_bounds (threeKernel a ha) (threeCoordinate a h) 1
    h (fun y _ => (threeCoordinate_bounds a ha h hh y).2)
    ⟨2, threeKernel_right_pos a ha, rfl⟩
  unfold leftRadius rightRadius
  rw [hlo, hhi]
  simp [threeCoordinate]

/-- Exact radii computed from the positive row supports. -/
theorem threeKernel_radii (a : ℕ) (ha : 1 ≤ a) (h : ℝ) (hh : 0 < h)
    (x : Fin 3) :
    leftRadius (threeKernel a ha) (threeCoordinate a h) x =
      (if x = 1 then (a : ℝ) * h else 0) ∧
    rightRadius (threeKernel a ha) (threeCoordinate a h) x =
      (if x = 1 then h else 0) := by
  by_cases hx : x = 1
  · subst x
    simpa only [↓reduceIte] using threeKernel_center_radii a ha h hh
  · have hrow : ∀ y, (threeKernel a ha).weight x y = if y = x then 1 else 0 := by
      intro y
      simp [threeWeight, hx, eq_comm]
    simpa only [hx, ↓reduceIte] using
      deterministic_radii (threeKernel a ha) (threeCoordinate a h) x hrow

/-- The sharp row propagation inequality is equality on every row of the certificate. -/
theorem threeKernel_row_equality (a : ℕ) (ha : 1 ≤ a) (h : ℝ) (hh : 0 < h)
    (x : Fin 3) :
    defect (threeKernel a ha) (threeCoordinate a h) x =
      escape (threeKernel a ha) x *
        leftRadius (threeKernel a ha) (threeCoordinate a h) x *
        rightRadius (threeKernel a ha) (threeCoordinate a h) x := by
  rw [threeKernel_defect, threeKernel_escape,
    (threeKernel_radii a ha h hh x).1, (threeKernel_radii a ha h hh x).2]
  by_cases hx : x = 1
  · have haR : (1 : ℝ) ≤ a := by exact_mod_cast ha
    have ha0 : (a : ℝ) ≠ 0 := ne_of_gt (lt_of_lt_of_le zero_lt_one haR)
    simp only [hx, ↓reduceIte]
    field_simp
  · simp [hx]



/-- The example's operator norm is exactly `2/a`, with the full-variation convention. -/
theorem threeKernel_channel_norm (a : ℕ) (ha : 1 ≤ a) :
    ‖channel (threeKernel a ha) - ContinuousLinearMap.id ℝ (Fin 3 → ℝ)‖ =
      2 / (a : ℝ) := by
  rw [channel_norm_eq]
  have hm : univ.sup' univ_nonempty (escape (threeKernel a ha)) = 1 / (a : ℝ) := by
    apply le_antisymm
    · apply sup'_le
      intro x _
      rw [threeKernel_escape]
      split_ifs <;> first | exact le_rfl | positivity
    · have hb := le_sup' (escape (threeKernel a ha)) (mem_univ (1 : Fin 3))
      simp only [threeKernel_escape, ite_true] at hb
      exact hb
  rw [hm]
  ring

/-- Identity endpoint rows contribute zero to the maximum propagation budget. -/
theorem threeKernel_budget (a : ℕ) (ha : 1 ≤ a) (h : ℝ) (hh : 0 < h) :
    propagationBudget (threeKernel a ha) (threeCoordinate a h) = (a : ℝ) * h * h := by
  unfold propagationBudget
  apply le_antisymm
  · apply sup'_le
    intro x _
    rw [(threeKernel_radii a ha h hh x).1, (threeKernel_radii a ha h hh x).2]
    split_ifs <;> (try simp only [zero_mul]) <;> first | exact le_rfl | positivity
  · have hb := le_sup'
      (fun x => leftRadius (threeKernel a ha) (threeCoordinate a h) x *
        rightRadius (threeKernel a ha) (threeCoordinate a h) x) (mem_univ (1 : Fin 3))
    simpa only [(threeKernel_center_radii a ha h hh).1,
      (threeKernel_center_radii a ha h hh).2] using hb

/-- The central square defect attains the finite sup norm. -/
theorem threeKernel_defect_norm (a : ℕ) (ha : 1 ≤ a) (h : ℝ) :
    ‖channel (threeKernel a ha) (fun x => threeCoordinate a h x ^ 2) -
      (fun x => threeCoordinate a h x ^ 2)‖ = h ^ 2 := by
  rw [channel_square_defect]
  apply le_antisymm
  · apply (pi_norm_le_iff_of_nonneg (sq_nonneg h)).mpr
    intro x
    rw [threeKernel_defect]
    split_ifs <;> simp [Real.norm_eq_abs, sq_nonneg h]
  · have hb := norm_le_pi_norm (defect (threeKernel a ha) (threeCoordinate a h)) 1
    simpa [Real.norm_eq_abs, abs_of_nonneg (sq_nonneg h)] using hb

/-- The WP-335 certificate saturates WP-336's global propagation inequality exactly. -/
theorem threeKernel_global_equality (a : ℕ) (ha : 1 ≤ a) (h : ℝ) (hh : 0 < h) :
    ‖channel (threeKernel a ha) (fun x => threeCoordinate a h x ^ 2) -
      (fun x => threeCoordinate a h x ^ 2)‖ =
      (1 / 2 : ℝ) *
        ‖channel (threeKernel a ha) - ContinuousLinearMap.id ℝ (Fin 3 → ℝ)‖ *
        propagationBudget (threeKernel a ha) (threeCoordinate a h) := by
  rw [threeKernel_defect_norm, threeKernel_channel_norm, threeKernel_budget a ha h hh]
  have haR : (1 : ℝ) ≤ a := by exact_mod_cast ha
  have ha0 : (a : ℝ) ≠ 0 := ne_of_gt (lt_of_lt_of_le zero_lt_one haR)
  field_simp

end Mathia.WP336
