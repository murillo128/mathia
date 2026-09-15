import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.MeasureTheory.Integral.IntegralEqImproper
import Mathlib.Topology.Order.Compact
import Mathlib.Analysis.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Asymptotics
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FunProp
import Mathlib.Tactic.Abel

/-!
# Coercive jump-kernel endpoint tail comparison

Associated finding:
`research/prime_lattice/findings/PL-323-coercive-tail-comparison-closes-pointwise-flux.md`.

Formalized theorem boundary: for Q₀ > 0, a complex-valued function m continuous
on [Q₀, ∞), tending to zero, and having finite pointwise symmetric singular
jump limits F on an eventual tail satisfies Q m(Q) → 0 whenever
F(Q) + 2 Q m(Q) → 0. `coercive_tail_limit` is the principal theorem;
`tail_bound` proves the explicit ε/Q + B exp(-(Q-R)/2) comparison.

The concrete kernel is 1/(exp(h)-1). `truncJump` uses the split coordinates
P = Q-h and P = Q+h of PL319-3 / PL322-2, with the same cutoff h > δ on
both sides and the left side restricted to h ≤ Q-Q₀. `HasJump` is the limit
as δ → 0 from above. Absolute integrability at the diagonal is not assumed
for m: only positive-cutoff integrability is derived from continuity and decay.
The two explicit smooth barriers have separately proved absolute integrability.

Not formalized: the upstream completed-Weil source identity, the derivation
of actual-state pointwise realizability, PL-321's moving-Green application,
and any arithmetic or RH-facing consequence. Continuity alone is not asserted
to supply the assumed finite pointwise singular limits. No novelty claim for
the maximum principle is made.
-/

noncomputable section

open Filter Set MeasureTheory Topology
open scoped Topology
namespace Mathia.PL323

def kernel (h : ℝ) : ℝ := (Real.exp h - 1)⁻¹

def jumpIntegrand {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    (q0 : ℝ) (u : ℝ → E) (q h : ℝ) : E :=
  kernel h • ((if h ≤ q - q0 then u q - u (q - h) else 0) + (u q - u (q + h)))

def truncJump {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    (q0 : ℝ) (u : ℝ → E) (q δ : ℝ) : E :=
  ∫ h in Ioi δ, jumpIntegrand q0 u q h

def HasJump {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    (q0 : ℝ) (u : ℝ → E) (q : ℝ) (z : E) : Prop :=
  Tendsto (truncJump q0 u q) (𝓝[>] (0 : ℝ)) (𝓝 z)

def TailContinuous {E : Type*} [NormedAddCommGroup E]
    (q0 : ℝ) (u : ℝ → E) : Prop :=
  ContinuousOn u (Ici q0) ∧ Tendsto u atTop (𝓝 0)

end Mathia.PL323

open Filter Set MeasureTheory Topology
open scoped Topology
namespace Mathia.PL323

lemma kernel_pos {h : ℝ} (hh : 0 < h) : 0 < kernel h := by
  unfold kernel
  exact inv_pos.mpr (sub_pos.mpr ((Real.one_lt_exp_iff).mpr hh))

lemma kernel_le_exp {h : ℝ} (hh : 0 < h) :
    kernel h ≤ (2 / h) * Real.exp (-h / 2) := by
  have ht : 1 ≤ Real.exp (h / 2) := Real.one_le_exp (by linarith)
  have he := Real.add_one_le_exp (h / 2)
  have heq : Real.exp h = Real.exp (h / 2) * Real.exp (h / 2) := by
    rw [← Real.exp_add]
    congr 1; ring
  have hden : 0 < Real.exp h - 1 := sub_pos.mpr (Real.one_lt_exp_iff.mpr hh)
  have hprod : h / 2 * Real.exp (h / 2) ≤ Real.exp h - 1 := by
    rw [heq]
    nlinarith [mul_nonneg (show 0 ≤ Real.exp (h/2) from (Real.exp_pos _).le)
      (show 0 ≤ Real.exp (h/2) - (h/2 + 1) from by linarith)]
  have hexp : Real.exp (-h / 2) * Real.exp (h / 2) = 1 := by
    rw [← Real.exp_add]
    convert Real.exp_zero using 1
    congr 1
    ring
  have hb : h ≤ 2 * Real.exp (-h / 2) * (Real.exp h - 1) := by
    have := mul_le_mul_of_nonneg_left hprod (Real.exp_pos (-h / 2)).le
    nlinarith [hexp]
  unfold kernel
  rw [inv_eq_one_div]
  apply (div_le_iff₀ hden).2
  rw [div_mul_eq_mul_div, div_mul_eq_mul_div]
  exact (le_div_iff₀ hh).2 (by simpa using hb)

lemma mul_kernel_le_exp {h : ℝ} (hh : 0 < h) :
    h * kernel h ≤ 2 * Real.exp (-h / 2) := by
  calc
    h * kernel h ≤ h * ((2 / h) * Real.exp (-h / 2)) :=
      mul_le_mul_of_nonneg_left (kernel_le_exp hh) hh.le
    _ = 2 * Real.exp (-h / 2) := by field_simp

lemma integrableOn_exp_neg_half (δ : ℝ) :
    IntegrableOn (fun h : ℝ => Real.exp (-h / 2)) (Ioi δ) := by
  convert integrableOn_exp_mul_Ioi (a := -(1/2 : ℝ)) (by norm_num) δ using 1
  ext h
  congr 1
  ring

lemma integral_exp_neg_half : (∫ h : ℝ in Ioi 0, Real.exp (-h / 2)) = 2 := by
  have := integral_exp_mul_Ioi (a := -(1/2 : ℝ)) (by norm_num) 0
  convert this using 1
  · congr 1
    ext h
    congr 1
    ring
  · norm_num

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

lemma hasJump_of_integrable {q0 : ℝ} {u : ℝ → E} {q : ℝ}
    (hi : IntegrableOn (jumpIntegrand q0 u q) (Ioi 0)) :
    HasJump q0 u q (∫ h in Ioi 0, jumpIntegrand q0 u q h) := by
  exact hi.continuousWithinAt_Ici_primitive_Ioi.mono (Ioi_subset_Ici_self)

omit [NormedSpace ℝ E] in
lemma TailContinuous.norm_bounded {q0 : ℝ} {u : ℝ → E} (hu : TailContinuous q0 u) :
    ∃ M > 0, ∀ q, q0 ≤ q → ‖u q‖ ≤ M := by
  have hb : ∀ᶠ q in atTop, ‖u q‖ < 1 := by
    simpa using hu.2.norm.eventually (gt_mem_nhds (show ‖(0 : E)‖ < (1 : ℝ) by simp))
  obtain ⟨R, hR⟩ := eventually_atTop.1 hb
  obtain ⟨M, hM⟩ := isCompact_Icc.exists_bound_of_continuousOn
    (hu.1.mono (show Icc q0 R ⊆ Ici q0 from fun _ hx => hx.1))
  refine ⟨max M 1, lt_of_lt_of_le zero_lt_one (le_max_right _ _), ?_⟩
  intro q hq
  by_cases hqR : q ≤ R
  · exact (hM q ⟨hq, hqR⟩).trans (le_max_left _ _)
  · exact (hR q (le_of_not_ge hqR)).le.trans (le_max_right _ _)

lemma jumpIntegrand_aestronglyMeasurable {q0 : ℝ} {u : ℝ → E} {q : ℝ}
    (hu : ContinuousOn u (Ici q0)) (hq : q0 ≤ q) :
    AEStronglyMeasurable (jumpIntegrand q0 u q) (volume.restrict (Ioi 0)) := by
  let v : ℝ → E := fun x => u (max q0 x)
  have hv : Continuous v := hu.comp_continuous (continuous_const.max continuous_id)
    (fun x => le_max_left q0 x)
  have hk : StronglyMeasurable kernel :=
    (Real.continuous_exp.stronglyMeasurable.sub stronglyMeasurable_const).inv₀
  have hm : StronglyMeasurable (jumpIntegrand q0 v q) := by
    apply hk.smul
    apply StronglyMeasurable.add
    · exact StronglyMeasurable.ite measurableSet_Iic
        (stronglyMeasurable_const.sub (hv.comp (continuous_const.sub continuous_id)).stronglyMeasurable)
        stronglyMeasurable_const
    · exact stronglyMeasurable_const.sub
        (hv.comp (continuous_const.add continuous_id)).stronglyMeasurable
  apply hm.aestronglyMeasurable.congr
  filter_upwards [ae_restrict_mem measurableSet_Ioi] with h hh
  have hvq : v q = u q := by simp [v, max_eq_right hq]
  have hvp : v (q+h) = u (q+h) := by
    simp [v, max_eq_right (show q0 ≤ q+h from by linarith [hh.out])]
  unfold jumpIntegrand
  rw [hvq, hvp]
  by_cases hb : h ≤ q - q0
  · simp [hb, v, max_eq_right (show q0 ≤ q-h from by linarith)]
  · simp [hb]

lemma norm_jumpIntegrand_le {q0 : ℝ} {u : ℝ → E} {q h M : ℝ}
    (hM : 0 ≤ M) (hu : ∀ r, q0 ≤ r → ‖u r‖ ≤ M) (hq : q0 ≤ q) (hh : 0 < h) :
    ‖jumpIntegrand q0 u q h‖ ≤ kernel h * (4 * M) := by
  have hqM := hu q hq
  have hpM := hu (q+h) (by linarith)
  have hplus : ‖u q - u (q+h)‖ ≤ 2*M := by
    calc
      _ ≤ ‖u q‖ + ‖u (q+h)‖ := norm_sub_le _ _
      _ ≤ 2*M := by linarith
  have hminus : ‖if h ≤ q-q0 then u q-u (q-h) else 0‖ ≤ 2*M := by
    split_ifs with hb
    · have hmM := hu (q-h) (by linarith)
      exact (norm_sub_le _ _).trans (by linarith)
    · simp only [norm_zero]
      positivity
  unfold jumpIntegrand
  rw [norm_smul, Real.norm_eq_abs, abs_of_pos (kernel_pos hh)]
  apply mul_le_mul_of_nonneg_left _ (kernel_pos hh).le
  exact (norm_add_le _ _).trans (by linarith)

lemma TailContinuous.integrableOn_jumpIntegrand {q0 : ℝ} {u : ℝ → E} {q δ : ℝ}
    (hu : TailContinuous q0 u) (hq : q0 ≤ q) (hδ : 0 < δ) :
    IntegrableOn (jumpIntegrand q0 u q) (Ioi δ) := by
  obtain ⟨M, hM, hMu⟩ := hu.norm_bounded
  apply ((integrableOn_exp_neg_half δ).const_mul (8*M/δ)).mono'
    ((jumpIntegrand_aestronglyMeasurable hu.1 hq).mono_set (Ioi_subset_Ioi hδ.le))
  filter_upwards [ae_restrict_mem measurableSet_Ioi] with h hh
  have hh0 : 0 < h := hδ.trans hh
  have hk : kernel h ≤ (2/δ) * Real.exp (-h/2) := by
    exact (kernel_le_exp hh0).trans (mul_le_mul_of_nonneg_right
      (div_le_div_of_nonneg_left (by norm_num) hδ hh.le) (Real.exp_pos _).le)
  calc
    ‖jumpIntegrand q0 u q h‖ ≤ kernel h * (4*M) :=
      norm_jumpIntegrand_le hM.le hMu hq hh0
    _ ≤ ((2/δ)*Real.exp (-h/2))*(4*M) := mul_le_mul_of_nonneg_right hk (by positivity)
    _ = (8*M/δ)*Real.exp (-h/2) := by ring

omit [NormedSpace ℝ E] in
lemma TailContinuous.add {q0 : ℝ} {u v : ℝ → E}
    (hu : TailContinuous q0 u) (hv : TailContinuous q0 v) :
    TailContinuous q0 (fun q => u q + v q) := by
  exact ⟨hu.1.add hv.1, by simpa using hu.2.add hv.2⟩

omit [NormedSpace ℝ E] in
lemma TailContinuous.sub {q0 : ℝ} {u v : ℝ → E}
    (hu : TailContinuous q0 u) (hv : TailContinuous q0 v) :
    TailContinuous q0 (fun q => u q - v q) := by
  exact ⟨hu.1.sub hv.1, by simpa using hu.2.sub hv.2⟩

lemma TailContinuous.smul {q0 : ℝ} {u : ℝ → E}
    (hu : TailContinuous q0 u) (a : ℝ) :
    TailContinuous q0 (fun q => a • u q) := by
  exact ⟨continuousOn_const.smul hu.1, by simpa using (tendsto_const_nhds (x := a)).smul hu.2⟩

lemma TailContinuous.map {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    {q0 : ℝ} {u : ℝ → E} (hu : TailContinuous q0 u) (L : E →L[ℝ] F) :
    TailContinuous q0 (fun q => L (u q)) := by
  exact ⟨L.continuous.comp_continuousOn hu.1, by simpa only [Function.comp_def, map_zero] using (L.continuous.tendsto 0).comp hu.2⟩

lemma jumpIntegrand_add {q0 : ℝ} {u v : ℝ → E} {q h : ℝ} :
    jumpIntegrand q0 (fun r => u r + v r) q h =
      jumpIntegrand q0 u q h + jumpIntegrand q0 v q h := by
  by_cases hb : h ≤ q-q0 <;> simp [jumpIntegrand, hb, smul_add, smul_sub] <;> abel

lemma jumpIntegrand_sub {q0 : ℝ} {u v : ℝ → E} {q h : ℝ} :
    jumpIntegrand q0 (fun r => u r - v r) q h =
      jumpIntegrand q0 u q h - jumpIntegrand q0 v q h := by
  by_cases hb : h ≤ q-q0 <;> simp [jumpIntegrand, hb, smul_add, smul_sub] <;> abel

lemma jumpIntegrand_smul {q0 : ℝ} {u : ℝ → E} {q h : ℝ} (a : ℝ) :
    jumpIntegrand q0 (fun r => a • u r) q h = a • jumpIntegrand q0 u q h := by
  by_cases hb : h ≤ q-q0
  · simp only [jumpIntegrand, ite_eq_left hb, ← smul_sub, ← smul_add]
    exact smul_comm _ _ _
  · simp only [jumpIntegrand, ite_eq_right hb, zero_add, ← smul_sub]
    exact smul_comm _ _ _

lemma jumpIntegrand_map {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    {q0 : ℝ} {u : ℝ → E} {q h : ℝ} (L : E →L[ℝ] F) :
    jumpIntegrand q0 (fun r => L (u r)) q h = L (jumpIntegrand q0 u q h) := by
  by_cases hb : h ≤ q-q0 <;> simp [jumpIntegrand, hb]

lemma HasJump.add {q0 : ℝ} {u v : ℝ → E} {q : ℝ} {z w : E}
    (hj : HasJump q0 u q z) (hk : HasJump q0 v q w)
    (hu : TailContinuous q0 u) (hv : TailContinuous q0 v) (hq : q0 ≤ q) :
    HasJump q0 (fun r => u r + v r) q (z+w) := by
  apply (Filter.Tendsto.add hj hk).congr'
  filter_upwards [self_mem_nhdsWithin] with δ hδ
  simp only [truncJump, jumpIntegrand_add]
  exact (integral_add (hu.integrableOn_jumpIntegrand hq hδ)
    (hv.integrableOn_jumpIntegrand hq hδ)).symm

lemma HasJump.sub {q0 : ℝ} {u v : ℝ → E} {q : ℝ} {z w : E}
    (hj : HasJump q0 u q z) (hk : HasJump q0 v q w)
    (hu : TailContinuous q0 u) (hv : TailContinuous q0 v) (hq : q0 ≤ q) :
    HasJump q0 (fun r => u r - v r) q (z-w) := by
  apply (Filter.Tendsto.sub hj hk).congr'
  filter_upwards [self_mem_nhdsWithin] with δ hδ
  simp only [truncJump, jumpIntegrand_sub]
  exact (integral_sub (hu.integrableOn_jumpIntegrand hq hδ)
    (hv.integrableOn_jumpIntegrand hq hδ)).symm

lemma HasJump.smul {q0 : ℝ} {u : ℝ → E} {q : ℝ} {z : E}
    (hj : HasJump q0 u q z) (a : ℝ) :
    HasJump q0 (fun r => a • u r) q (a • z) := by
  change Tendsto (fun δ => ∫ h in Ioi δ, jumpIntegrand q0 (fun r => a • u r) q h)
    (𝓝[>] (0 : ℝ)) (𝓝 (a • z))
  simp only [jumpIntegrand_smul, integral_smul]
  exact (tendsto_const_nhds (x := a)).smul hj

lemma HasJump.map [CompleteSpace E]
    {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F]
    {q0 : ℝ} {u : ℝ → E} {q : ℝ} {z : E}
    (hj : HasJump q0 u q z) (hu : TailContinuous q0 u) (hq : q0 ≤ q)
    (L : E →L[ℝ] F) : HasJump q0 (fun r => L (u r)) q (L z) := by
  apply ((L.continuous.tendsto z).comp hj).congr'
  filter_upwards [self_mem_nhdsWithin] with δ hδ
  simp only [truncJump, jumpIntegrand_map]
  exact (L.integral_comp_comm (hu.integrableOn_jumpIntegrand hq hδ)).symm

lemma HasJump.nonneg_of_isMax {q0 : ℝ} {u : ℝ → ℝ} {q z : ℝ}
    (hj : HasJump q0 u q z) (hq : q0 ≤ q)
    (hmax : ∀ r, q0 ≤ r → u r ≤ u q) : 0 ≤ z := by
  apply ge_of_tendsto hj
  filter_upwards [self_mem_nhdsWithin] with δ hδ
  apply integral_nonneg_of_ae
  filter_upwards [ae_restrict_mem measurableSet_Ioi] with h hh
  have hh0 : 0 < h := lt_trans hδ hh
  unfold jumpIntegrand
  simp only [smul_eq_mul]
  apply mul_nonneg (kernel_pos hh0).le
  apply add_nonneg
  · split_ifs with hb
    · exact sub_nonneg.mpr (hmax (q-h) (by linarith))
    · exact le_rfl
  · exact sub_nonneg.mpr (hmax (q+h) (by linarith))

end Mathia.PL323

open Filter Set MeasureTheory Topology
open scoped Topology
namespace Mathia.PL323

def reciprocal (q : ℝ) : ℝ := 1 / q

def expBarrier (R q : ℝ) : ℝ := Real.exp (-(q - R) / 2)

lemma reciprocal_tailContinuous {q0 : ℝ} (hq0 : 0 < q0) :
    TailContinuous q0 reciprocal := by
  constructor
  · exact continuousOn_const.div continuousOn_id (fun q hq => ne_of_gt (lt_of_lt_of_le hq0 hq))
  · change Tendsto (fun q : ℝ => 1/q) atTop (𝓝 0)
    simpa only [one_div] using (tendsto_inv_atTop_zero (𝕜 := ℝ))

lemma expBarrier_pos (R q : ℝ) : 0 < expBarrier R q := Real.exp_pos _

lemma expBarrier_tailContinuous (q0 R : ℝ) : TailContinuous q0 (expBarrier R) := by
  constructor
  · unfold expBarrier
    fun_prop
  · have h := (Real.tendsto_exp_neg_atTop_nhds_zero.comp
        (tendsto_id.atTop_div_const (by norm_num : (0:ℝ) < 2))).mul_const (Real.exp (R/2))
    simp only [zero_mul] at h
    convert h using 1
    ext q
    simp only [expBarrier, Function.comp_apply, id_eq, ← Real.exp_add]
    congr 1
    ring

lemma expBarrier_ge_one {R q : ℝ} (hq : q ≤ R) : 1 ≤ expBarrier R q := by
  apply Real.one_le_exp_iff.mpr
  linarith

lemma expBarrier_weighted_tendsto (R : ℝ) :
    Tendsto (fun q => q * expBarrier R q) atTop (𝓝 0) := by
  have h := (tendsto_rpow_mul_exp_neg_mul_atTop_nhds_zero (1 : ℝ) (1/2) (by norm_num)).mul_const (Real.exp (R/2))
  simp only [zero_mul, Real.rpow_one] at h
  convert h using 1
  ext q
  simp only [expBarrier, mul_assoc, ← Real.exp_add]
  congr 2
  ring

lemma reciprocal_diff_right {q0 q h : ℝ} (hq0 : 0 < q0) (hq : q0 ≤ q) (hh : 0 < h) :
    0 ≤ reciprocal q - reciprocal (q + h) ∧
      reciprocal q - reciprocal (q + h) ≤ h / (q * q0) := by
  have hqpos : 0 < q := lt_of_lt_of_le hq0 hq
  have hqh : 0 < q + h := by positivity
  have heq : reciprocal q - reciprocal (q+h) = h / (q*(q+h)) := by
    unfold reciprocal
    field_simp
    ring
  rw [heq]
  constructor
  · positivity
  · apply div_le_div_of_nonneg_left (le_of_lt hh) (by positivity)
    exact mul_le_mul_of_nonneg_left (by linarith) hqpos.le

lemma reciprocal_diff_left {q0 q h : ℝ} (hq0 : 0 < q0) (hq : q0 ≤ q)
    (hh : 0 < h) (hhq : h ≤ q - q0) :
    -(h / (q*q0)) ≤ reciprocal q - reciprocal (q-h) ∧
      reciprocal q - reciprocal (q-h) ≤ 0 := by
  have hqpos : 0 < q := lt_of_lt_of_le hq0 hq
  have hqh0 : q0 ≤ q-h := by linarith
  have hqh : 0 < q-h := lt_of_lt_of_le hq0 hqh0
  have heq : reciprocal q - reciprocal (q-h) = -(h / (q*(q-h))) := by
    unfold reciprocal
    field_simp
    ring
  rw [heq]
  constructor
  · apply neg_le_neg
    apply div_le_div_of_nonneg_left hh.le (by positivity)
    exact mul_le_mul_of_nonneg_left hqh0 hqpos.le
  · exact neg_nonpos.mpr (by positivity)

lemma reciprocal_difference_abs {q0 q h : ℝ} (hq0 : 0 < q0) (hq : q0 ≤ q)
    (hh : 0 < h) :
    |(if h ≤ q-q0 then reciprocal q - reciprocal (q-h) else 0) +
        (reciprocal q - reciprocal (q+h))| ≤ h / (q*q0) := by
  obtain ⟨hr0, hr⟩ := reciprocal_diff_right hq0 hq hh
  rw [abs_le]
  split_ifs with hhq
  · obtain ⟨hl, hl0⟩ := reciprocal_diff_left hq0 hq hh hhq
    constructor <;> linarith
  · simpa using And.intro (by linarith : -(h/(q*q0)) ≤ reciprocal q - reciprocal (q+h)) hr

lemma expBarrier_shift_left (R q h : ℝ) :
    expBarrier R (q-h) = expBarrier R q * Real.exp (h/2) := by
  simp only [expBarrier, ← Real.exp_add]
  congr 1
  ring

lemma expBarrier_shift_right (R q h : ℝ) :
    expBarrier R (q+h) = expBarrier R q * Real.exp (-h/2) := by
  simp only [expBarrier, ← Real.exp_add]
  congr 1
  ring

lemma exp_neg_half_le_one {h : ℝ} (hh : 0 ≤ h) : Real.exp (-h/2) ≤ 1 := by
  exact Real.exp_le_one_iff.mpr (by linarith)

lemma exp_one_sub_neg_half_le {h : ℝ} (hh : 0 ≤ h) :
    1 - Real.exp (-h/2) ≤ Real.exp (h/2) - 1 := by
  have he : Real.exp (h/2) * Real.exp (-h/2) = 1 := by
    rw [← Real.exp_add]
    rw [show h/2 + -h/2 = 0 by ring, Real.exp_zero]
  have hp := Real.exp_pos (h/2)
  have hh1 := Real.one_le_exp_iff.mpr (by linarith : 0 ≤ h/2)
  have hh2 := exp_neg_half_le_one hh
  nlinarith [mul_nonneg (sub_nonneg.mpr hh1) (sub_nonneg.mpr hh2)]

lemma expBarrier_difference_abs {q0 R q h : ℝ} (hh : 0 < h) :
    |(if h ≤ q-q0 then expBarrier R q - expBarrier R (q-h) else 0) +
        (expBarrier R q - expBarrier R (q+h))| ≤
      expBarrier R q * (Real.exp (h/2)-1) := by
  rw [expBarrier_shift_left, expBarrier_shift_right, abs_le]
  have hp := (expBarrier_pos R q).le
  have he1 := Real.one_le_exp_iff.mpr (by linarith : 0 ≤ h/2)
  have he2 := exp_neg_half_le_one hh.le
  have he3 := exp_one_sub_neg_half_le hh.le
  have hl : expBarrier R q - expBarrier R q * Real.exp (h/2) ≤ 0 := by nlinarith
  have hr : 0 ≤ expBarrier R q - expBarrier R q * Real.exp (-h/2) := by nlinarith
  have hrb : expBarrier R q - expBarrier R q * Real.exp (-h/2) ≤
      expBarrier R q * (Real.exp (h/2)-1) := by nlinarith
  split_ifs <;> constructor <;> nlinarith


lemma jumpIntegrand_measurable_real {q0 q : ℝ} {u : ℝ → ℝ} (hu : Measurable u) :
    Measurable (jumpIntegrand q0 u q) := by
  unfold jumpIntegrand kernel
  simp only [smul_eq_mul]
  apply Measurable.mul
  · exact (Real.measurable_exp.sub measurable_const).inv
  · apply Measurable.add
    · apply Measurable.ite (measurableSet_le measurable_id measurable_const)
      · exact measurable_const.sub (hu.comp (measurable_const.sub measurable_id))
      · exact measurable_const
    · exact measurable_const.sub (hu.comp (measurable_const.add measurable_id))

lemma kernel_exp_half_bound {h : ℝ} (hh : 0 < h) :
    kernel h * (Real.exp (h/2)-1) ≤ Real.exp (-h/2) := by
  have hd : 0 < Real.exp h - 1 := sub_pos.mpr (Real.one_lt_exp_iff.mpr hh)
  have he : Real.exp (-h/2) * Real.exp h = Real.exp (h/2) := by
    rw [← Real.exp_add]
    congr 1
    ring
  have hn := exp_neg_half_le_one hh.le
  rw [kernel, inv_mul_eq_div]
  apply (div_le_iff₀ hd).2
  nlinarith

lemma reciprocal_jump_abs_bound {q0 q h : ℝ} (hq0 : 0 < q0) (hq : q0 ≤ q)
    (hh : 0 < h) :
    |jumpIntegrand q0 reciprocal q h| ≤ (2/(q*q0))*Real.exp (-h/2) := by
  have hqpos : 0 < q := lt_of_lt_of_le hq0 hq
  have hk := (kernel_pos hh).le
  have hd := reciprocal_difference_abs hq0 hq hh
  simp only [jumpIntegrand, smul_eq_mul, abs_mul, abs_of_nonneg hk]
  calc
    _ ≤ kernel h * (h/(q*q0)) := mul_le_mul_of_nonneg_left hd hk
    _ = (h*kernel h)/(q*q0) := by ring
    _ ≤ (2*Real.exp (-h/2))/(q*q0) :=
      div_le_div_of_nonneg_right (mul_kernel_le_exp hh) (by positivity)
    _ = _ := by ring

lemma expBarrier_jump_abs_bound {q0 R q h : ℝ} (hh : 0 < h) :
    |jumpIntegrand q0 (expBarrier R) q h| ≤ expBarrier R q * Real.exp (-h/2) := by
  have hk := (kernel_pos hh).le
  simp only [jumpIntegrand, smul_eq_mul, abs_mul, abs_of_nonneg hk]
  calc
    _ ≤ kernel h * (expBarrier R q * (Real.exp (h/2)-1)) :=
      mul_le_mul_of_nonneg_left (expBarrier_difference_abs hh) hk
    _ = expBarrier R q * (kernel h * (Real.exp (h/2)-1)) := by ring
    _ ≤ _ := mul_le_mul_of_nonneg_left (kernel_exp_half_bound hh) (expBarrier_pos R q).le

lemma reciprocal_jump_integrable {q0 q : ℝ} (hq0 : 0 < q0) (hq : q0 ≤ q) :
    IntegrableOn (jumpIntegrand q0 reciprocal q) (Ioi 0) := by
  apply ((integrableOn_exp_neg_half 0).const_mul (2/(q*q0))).mono'
  · exact (jumpIntegrand_measurable_real (measurable_const.div measurable_id)).aestronglyMeasurable
  · filter_upwards [ae_restrict_mem measurableSet_Ioi] with h hh
    simpa only [Real.norm_eq_abs] using reciprocal_jump_abs_bound hq0 hq hh

lemma expBarrier_jump_integrable (q0 R q : ℝ) :
    IntegrableOn (jumpIntegrand q0 (expBarrier R) q) (Ioi 0) := by
  apply ((integrableOn_exp_neg_half 0).const_mul (expBarrier R q)).mono'
  · apply (jumpIntegrand_measurable_real _).aestronglyMeasurable
    unfold expBarrier
    fun_prop
  · filter_upwards [ae_restrict_mem measurableSet_Ioi] with h hh
    simpa only [Real.norm_eq_abs] using expBarrier_jump_abs_bound (q0 := q0) (R := R) (q := q) hh

noncomputable def reciprocalJump (q0 q : ℝ) : ℝ :=
  ∫ h in Ioi 0, jumpIntegrand q0 reciprocal q h

noncomputable def expBarrierJump (q0 R q : ℝ) : ℝ :=
  ∫ h in Ioi 0, jumpIntegrand q0 (expBarrier R) q h

lemma reciprocal_hasJump {q0 q : ℝ} (hq0 : 0 < q0) (hq : q0 ≤ q) :
    HasJump q0 reciprocal q (reciprocalJump q0 q) :=
  hasJump_of_integrable (reciprocal_jump_integrable hq0 hq)

lemma expBarrier_hasJump (q0 R q : ℝ) :
    HasJump q0 (expBarrier R) q (expBarrierJump q0 R q) :=
  hasJump_of_integrable (expBarrier_jump_integrable q0 R q)

lemma reciprocalJump_lower {q0 q : ℝ} (hq0 : 0 < q0) (hq : q0 ≤ q) :
    -(4/(q*q0)) ≤ reciprocalJump q0 q := by
  have hi := reciprocal_jump_integrable hq0 hq
  have hc := (integrableOn_exp_neg_half 0).const_mul (-(2/(q*q0)))
  have hle : ∀ᵐ h ∂volume.restrict (Ioi 0),
      -(2/(q*q0))*Real.exp (-h/2) ≤ jumpIntegrand q0 reciprocal q h := by
    filter_upwards [ae_restrict_mem measurableSet_Ioi] with h hh
    have hb := (abs_le.mp (reciprocal_jump_abs_bound hq0 hq hh)).1
    nlinarith
  have hint := integral_mono_ae hc hi hle
  rw [integral_const_mul, integral_exp_neg_half] at hint
  unfold reciprocalJump
  convert hint using 1
  ring

lemma expBarrierJump_lower (q0 R q : ℝ) :
    -(2*expBarrier R q) ≤ expBarrierJump q0 R q := by
  have hi := expBarrier_jump_integrable q0 R q
  have hc := (integrableOn_exp_neg_half 0).const_mul (-expBarrier R q)
  have hle : ∀ᵐ h ∂volume.restrict (Ioi 0),
      -expBarrier R q*Real.exp (-h/2) ≤ jumpIntegrand q0 (expBarrier R) q h := by
    filter_upwards [ae_restrict_mem measurableSet_Ioi] with h hh
    have hb := (abs_le.mp (expBarrier_jump_abs_bound (q0 := q0) (R := R) (q := q) hh)).1
    nlinarith
  have hint := integral_mono_ae hc hi hle
  rw [integral_const_mul, integral_exp_neg_half] at hint
  unfold expBarrierJump
  convert hint using 1
  ring

lemma reciprocal_operator_ge_one {q0 q : ℝ} (hq0 : 0 < q0) (hq : q0 ≤ q)
    (hlarge : 4/q0 ≤ q) :
    1 ≤ reciprocalJump q0 q + 2*q*reciprocal q := by
  have hqpos : 0 < q := lt_of_lt_of_le hq0 hq
  have hp : 2*q*reciprocal q = 2 := by unfold reciprocal; field_simp
  rw [hp]
  have hb := reciprocalJump_lower hq0 hq
  have hprod : 4 ≤ q*q0 := (div_le_iff₀ hq0).mp hlarge
  have hratio : 4/(q*q0) ≤ 1 := (div_le_one (by positivity)).mpr hprod
  linarith

lemma expBarrier_operator_nonneg {q0 R q : ℝ} (hq : 1 ≤ q) :
    0 ≤ expBarrierJump q0 R q + 2*q*expBarrier R q := by
  have hb := expBarrierJump_lower q0 R q
  have hp := expBarrier_pos R q
  nlinarith

end Mathia.PL323

open Filter Set Topology
open scoped Topology
namespace Mathia.PL323

theorem exists_positive_max {q0 : ℝ} {u : ℝ → ℝ}
    (hc : ContinuousOn u (Ici q0)) (hz : Tendsto u atTop (𝓝 0))
    {x : ℝ} (hx : q0 ≤ x) (hp : 0 < u x) :
    ∃ q, q0 ≤ q ∧ 0 < u q ∧ ∀ p, q0 ≤ p → u p ≤ u q := by
  obtain ⟨T, hT⟩ := eventually_atTop.1 ((tendsto_order.1 hz).2 (u x) hp)
  obtain ⟨q, hq, hmax⟩ := isCompact_Icc.exists_isMaxOn
    (show (Icc q0 (max T x)).Nonempty from ⟨x, hx, le_max_right _ _⟩)
    (hc.mono (fun _ h ↦ h.1))
  have hxq : u x ≤ u q := hmax ⟨hx, le_max_right _ _⟩
  refine ⟨q, hq.1, hp.trans_le hxq, fun p hp0 ↦ ?_⟩
  by_cases hpT : p ≤ max T x
  · exact hmax ⟨hp0, hpT⟩
  · exact (hT p ((le_max_left T x).trans (le_of_not_ge hpT))).le.trans hxq

/-- The only operator input in the coercive comparison is its sign at a positive maximum. -/
theorem coercive_comparison {q0 R : ℝ} (hq0 : 0 < q0)
    {u w U W : ℝ → ℝ}
    (hu : ContinuousOn u (Ici q0)) (hw : ContinuousOn w (Ici q0))
    (huz : Tendsto u atTop (𝓝 0)) (hwz : Tendsto w atTop (𝓝 0))
    (hpast : ∀ q, q0 ≤ q → q ≤ R → u q ≤ w q)
    (hsource : ∀ q, R < q → U q + 2*q*u q ≤ W q + 2*q*w q)
    (hmax : ∀ q, q0 ≤ q → R < q →
      (∀ p, q0 ≤ p → u p - w p ≤ u q - w q) → 0 ≤ U q - W q) :
    ∀ q, q0 ≤ q → u q ≤ w q := by
  intro x hx
  by_contra hn
  have hp : 0 < u x - w x := sub_pos.mpr (lt_of_not_ge hn)
  obtain ⟨q, hq0', hpos, hqmax⟩ := exists_positive_max (u := fun q ↦ u q - w q) (hu.sub hw)
    (by simpa using huz.sub hwz) hx hp
  have hRq : R < q := by
    by_contra h
    have := hpast q hq0' (le_of_not_gt h)
    linarith
  have hJ := hmax q hq0' hRq hqmax
  have hf := hsource q hRq
  have hc : 0 < 2*q*(u q-w q) := mul_pos (by linarith) hpos
  nlinarith

/-- A unit phase exposes the complex norm, without choosing an argument. -/
theorem exists_unit_phase (z : ℂ) :
    ∃ c : ℂ, ‖c‖ = 1 ∧ (c*z).re = ‖z‖ := by
  by_cases hz : z = 0
  · subst z
    exact ⟨1, by simp, by simp⟩
  have hn : ‖z‖ ≠ 0 := norm_ne_zero_iff.mpr hz
  refine ⟨(starRingEnd ℂ) z / (‖z‖ : ℂ), ?_, ?_⟩
  · simp [hn]
  · rw [div_mul_eq_mul_div, Complex.conj_mul']
    simp only [Complex.div_ofReal_re, ← Complex.ofReal_pow, Complex.ofReal_re]
    field_simp

theorem norm_le_of_unit_phases {z : ℂ} {b : ℝ}
    (h : ∀ c : ℂ, ‖c‖ = 1 → (c*z).re ≤ b) : ‖z‖ ≤ b := by
  obtain ⟨c, hc, he⟩ := exists_unit_phase z
  rw [← he]
  exact h c hc

theorem complex_coercive_comparison {q0 R : ℝ} (hq0 : 0 < q0)
    {m F : ℝ → ℂ} {w W : ℝ → ℝ}
    (hm : ContinuousOn m (Ici q0)) (hw : ContinuousOn w (Ici q0))
    (hmz : Tendsto m atTop (𝓝 0)) (hwz : Tendsto w atTop (𝓝 0))
    (hpast : ∀ q, q0 ≤ q → q ≤ R → ‖m q‖ ≤ w q)
    (hsource : ∀ q, R < q → ‖F q + (2*q : ℝ) • m q‖ ≤ W q + 2*q*w q)
    (hmax : ∀ (c : ℂ), ‖c‖ = 1 → ∀ q, q0 ≤ q → R < q →
      (∀ p, q0 ≤ p → (c*m p).re - w p ≤ (c*m q).re - w q) →
      0 ≤ (c*F q).re - W q) :
    ∀ q, q0 ≤ q → ‖m q‖ ≤ w q := by
  intro q hq
  apply norm_le_of_unit_phases
  intro c hc
  apply coercive_comparison (U := fun q ↦ (c*F q).re) (W := W) hq0
      (u := fun q ↦ (c*m q).re) (w := w) _ hw _ hwz _ _ (hmax c hc) q hq
  · exact Complex.continuous_re.comp_continuousOn (continuousOn_const.mul hm)
  · have hz : Tendsto (fun q ↦ c*m q) atTop (𝓝 0) := by
      simpa using tendsto_const_nhds.mul hmz
    exact (Complex.continuous_re.tendsto (0 : ℂ)).comp hz
  · intro p hp hpR
    exact (Complex.re_le_norm _).trans (by simpa [norm_mul, hc] using hpast p hp hpR)
  · intro p hpR
    have hs := (Complex.re_le_norm (c*(F p + (2*p : ℝ) • m p))).trans
      (by simpa [norm_mul, hc] using hsource p hpR)
    simp only [mul_add, Complex.add_re, Complex.mul_re, Complex.smul_re,
      Complex.smul_im, smul_eq_mul] at hs ⊢
    nlinarith [hs]

end Mathia.PL323

open Filter Set MeasureTheory Topology
open scoped Topology
namespace Mathia.PL323

def phaseProjection (c : ℂ) : ℂ →L[ℝ] ℝ :=
  c.re • Complex.reCLM - c.im • Complex.imCLM

@[simp] lemma phaseProjection_apply (c z : ℂ) : phaseProjection c z = (c*z).re := by
  simp [phaseProjection, Complex.mul_re]

def combinedBarrier (ε B R q : ℝ) : ℝ :=
  ε * reciprocal q + B * expBarrier R q

def combinedJump (q0 ε B R q : ℝ) : ℝ :=
  ε * reciprocalJump q0 q + B * expBarrierJump q0 R q

lemma combinedBarrier_tailContinuous {q0 : ℝ} (hq0 : 0 < q0) (ε B R : ℝ) :
    TailContinuous q0 (combinedBarrier ε B R) := by
  change TailContinuous q0 (fun q ↦ ε*reciprocal q + B*expBarrier R q)
  simpa only [smul_eq_mul] using
    ((reciprocal_tailContinuous hq0).smul ε).add ((expBarrier_tailContinuous q0 R).smul B)

lemma combinedBarrier_hasJump {q0 q : ℝ} (hq0 : 0 < q0) (hq : q0 ≤ q) (ε B R : ℝ) :
    HasJump q0 (combinedBarrier ε B R) q (combinedJump q0 ε B R q) := by
  change HasJump q0 (fun q ↦ ε*reciprocal q + B*expBarrier R q) q
    (ε*reciprocalJump q0 q+B*expBarrierJump q0 R q)
  simpa only [smul_eq_mul] using
    ((reciprocal_hasJump hq0 hq).smul ε).add ((expBarrier_hasJump q0 R q).smul B)
      ((reciprocal_tailContinuous hq0).smul ε) ((expBarrier_tailContinuous q0 R).smul B) hq

lemma combinedBarrier_operator_ge {q0 q ε B R : ℝ}
    (hq0 : 0 < q0) (hq : q0 ≤ q) (hp : 4/q0 ≤ q) (he : 1 ≤ q)
    (hε : 0 ≤ ε) (hB : 0 ≤ B) :
    ε ≤ combinedJump q0 ε B R q + 2*q*combinedBarrier ε B R q := by
  have h1 := mul_le_mul_of_nonneg_left (reciprocal_operator_ge_one hq0 hq hp) hε
  have h2 := mul_nonneg hB (expBarrier_operator_nonneg (q0 := q0) (R := R) he)
  unfold combinedJump combinedBarrier
  nlinarith

/-- Concrete two-barrier comparison for complex residuals. -/
theorem tail_bound {q0 : ℝ} (hq0 : 0 < q0) {m F : ℝ → ℂ}
    (hm : TailContinuous q0 m)
    (hJ : ∀ᶠ q in atTop, HasJump q0 m q (F q))
    (hF : Tendsto (fun q ↦ F q + (2*q : ℝ) • m q) atTop (𝓝 0))
    {ε : ℝ} (hε : 0 < ε) :
    ∃ R B : ℝ, 0 < B ∧ ∀ q, q0 ≤ q → ‖m q‖ ≤ ε/q + B*expBarrier R q := by
  have hs : ∀ᶠ q in atTop, ‖F q + (2*q : ℝ) • m q‖ ≤ ε := by
    have := hF.norm.eventually (gt_mem_nhds (by simpa using hε))
    filter_upwards [this] with q hq using le_of_lt hq
  obtain ⟨R, hR⟩ := eventually_atTop.1
    (hJ.and (hs.and ((eventually_ge_atTop q0).and
      ((eventually_ge_atTop (4/q0)).and (eventually_ge_atTop (1 : ℝ))))))
  obtain ⟨B, hB, hBm⟩ := hm.norm_bounded
  have hw := combinedBarrier_tailContinuous hq0 ε B R
  refine ⟨R, B, hB, ?_⟩
  have hb : ∀ q, q0 ≤ q → ‖m q‖ ≤ combinedBarrier ε B R q := by
    apply complex_coercive_comparison (R := R) (F := F) (W := combinedJump q0 ε B R) hq0
      hm.1 hw.1 hm.2 hw.2
    · intro q hq hqR
      have he := mul_le_mul_of_nonneg_left (expBarrier_ge_one hqR) hB.le
      have hp : 0 ≤ ε * reciprocal q := by
        unfold reciprocal
        have hqp := hq0.trans_le hq
        positivity
      unfold combinedBarrier
      linarith [hBm q hq]
    · intro q hqR
      have hr := hR q hqR.le
      exact hr.2.1.trans
        (combinedBarrier_operator_ge hq0 hr.2.2.1 hr.2.2.2.1 hr.2.2.2.2 hε.le hB.le)
    · intro c _ q hq hqR hmax
      have hj := (hR q hqR.le).1
      have hmapped := hj.map hm hq (phaseProjection c)
      have hdiff := hmapped.sub (combinedBarrier_hasJump hq0 hq ε B R)
        (hm.map (phaseProjection c)) hw hq
      apply hdiff.nonneg_of_isMax hq
      simpa only [phaseProjection_apply] using hmax
  intro q hq
  simpa only [combinedBarrier, reciprocal, mul_one_div] using hb q hq

/-- PL-323: finite pointwise symmetric singular realizations and vanishing coercive
forcing imply the endpoint residual law, for complex-valued residuals. -/
theorem coercive_tail_limit {q0 : ℝ} (hq0 : 0 < q0) {m F : ℝ → ℂ}
    (hm : ContinuousOn m (Ici q0)) (hm0 : Tendsto m atTop (𝓝 0))
    (hJ : ∀ᶠ q in atTop, HasJump q0 m q (F q))
    (hF : Tendsto (fun q ↦ F q + (2*q : ℝ) • m q) atTop (𝓝 0)) :
    Tendsto (fun q : ℝ ↦ (q : ℂ) * m q) atTop (𝓝 0) := by
  apply Metric.tendsto_atTop.2
  intro ε hε
  obtain ⟨R, B, hB, hb⟩ := tail_bound hq0 ⟨hm, hm0⟩ hJ hF (half_pos hε)
  have he : Tendsto (fun q ↦ B * (q * expBarrier R q)) atTop (𝓝 0) := by
    simpa using (expBarrier_weighted_tendsto R).const_mul B
  obtain ⟨T, hT⟩ := eventually_atTop.1 ((tendsto_order.1 he).2 (ε/2) (half_pos hε))
  refine ⟨max T q0, fun q hq ↦ ?_⟩
  have hq0' := (le_max_right T q0).trans hq
  have hqpos := hq0.trans_le hq0'
  have hbound := mul_le_mul_of_nonneg_left (hb q hq0') hqpos.le
  have ht := hT q ((le_max_left T q0).trans hq)
  have hc : q * (ε/2/q) = ε/2 := by field_simp
  rw [dist_zero_right, norm_mul, Complex.norm_real, Real.norm_eq_abs, abs_of_pos hqpos]
  nlinarith

end Mathia.PL323

#print axioms Mathia.PL323.HasJump.nonneg_of_isMax
#print axioms Mathia.PL323.reciprocal_operator_ge_one
#print axioms Mathia.PL323.expBarrier_operator_nonneg
#print axioms Mathia.PL323.tail_bound
#print axioms Mathia.PL323.coercive_tail_limit
