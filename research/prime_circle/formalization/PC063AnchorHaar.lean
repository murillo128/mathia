import Mathlib.Analysis.Fourier.AddCircle
import Mathlib.Analysis.SpecialFunctions.Complex.LogBounds
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Sinc
import Mathlib.MeasureTheory.Group.Circle
import Mathlib.MeasureTheory.Measure.LevyConvergence
import Mathlib.Probability.ProbabilityMassFunction.Integrals

/-!
# PC-063: the growing-conductor anchor/Haar crossover

This module formalizes the bounded analytic statement from PC-063.  It does not formalize the
finding's novelty discussion, RH interpretation, log-scale law for `N_x`, centered boundary-layer
profile, or claims about observables other than the canonical root projection.
-/

open Filter MeasureTheory Set Topology
open scoped ENNReal NNReal

noncomputable section

namespace Mathia.PC063

/-- The additive unit circle used for Fourier analysis before transport to `Circle`. -/
abbrev Torus := AddCircle (1 : ℝ)

/-- The logarithmic normalization `L(x) = -log(1-x)`. -/
def logScale (x : ℝ) : ℝ := -Real.log (1 - x)

/-- The positive-integer logarithmic-series atom at the Lean index `n`, representing `n+1`. -/
def logSeriesWeight (x : ℝ) (n : ℕ) : ℝ :=
  x ^ (n + 1) / ((n + 1 : ℝ) * logScale x)

theorem logScale_pos {x : ℝ} (hx : x ∈ Ioo 0 1) : 0 < logScale x := by
  rw [logScale]
  exact neg_pos.mpr (Real.log_neg (sub_pos.mpr hx.2) (sub_lt_self 1 hx.1))

theorem logSeriesWeight_nonneg {x : ℝ} (hx : x ∈ Ioo 0 1) (n : ℕ) :
    0 ≤ logSeriesWeight x n := by
  rw [logSeriesWeight]
  exact div_nonneg (pow_nonneg hx.1.le _)
    (mul_nonneg (by positivity) (logScale_pos hx).le)

theorem hasSum_logSeriesWeight {x : ℝ} (hx : x ∈ Ioo 0 1) :
    HasSum (logSeriesWeight x) 1 := by
  have hseries := Real.hasSum_pow_div_log_of_abs_lt_one
    (x := x) (by simpa [abs_of_pos hx.1] using hx.2)
  have hscale_ne : logScale x ≠ 0 := (logScale_pos hx).ne'
  have hscaled := hseries.div_const (logScale x)
  have hsum : -Real.log (1 - x) / logScale x = 1 := by
    rw [show -Real.log (1 - x) = logScale x by rfl, div_self hscale_ne]
  rw [hsum] at hscaled
  have hfun : logSeriesWeight x =
      fun n : ℕ => x ^ (n + 1) / (n + 1) / logScale x := by
    funext n
    rw [logSeriesWeight]
    field_simp
  rw [hfun]
  exact hscaled

/-- The normalized logarithmic-series law on positive integers, indexed in Lean from zero. -/
def logSeriesPMF (x : ℝ) (hx : x ∈ Ioo 0 1) : PMF ℕ :=
  ⟨fun n => ENNReal.ofReal (logSeriesWeight x n), by
    have hnn := (hasSum_logSeriesWeight hx).toNNReal (logSeriesWeight_nonneg hx)
    exact ENNReal.hasSum_coe.mpr (by simpa using hnn)⟩

/-- The logarithmic-series law as a probability measure. -/
def logSeriesProbability (x : ℝ) (hx : x ∈ Ioo 0 1) : ProbabilityMeasure ℕ :=
  ⟨(logSeriesPMF x hx).toMeasure, inferInstance⟩

/-- The `q`-th-root image of the positive integer represented by `n`. -/
def rootPoint (q n : ℕ) : Torus :=
  (((n + 1 : ℕ) : ℝ) / (q : ℝ) : AddCircle (1 : ℝ))

/-- The canonical logarithmic-series projection to the additive unit circle. -/
def torusRootProjection (x : ℝ) (q : ℕ) (hx : x ∈ Ioo 0 1) :
    ProbabilityMeasure Torus :=
  (logSeriesProbability x hx).map (rootPoint q)

/-- The canonical homeomorphism from the additive unit circle to the complex unit circle. -/
def torusCircleHomeomorph : Torus ≃ₜ Circle :=
  AddCircle.homeomorphCircle (by norm_num)

/-- The canonical logarithmic-series projection as a probability measure on the complex circle. -/
def circleRootProjection (x : ℝ) (q : ℕ) (hx : x ∈ Ioo 0 1) :
    ProbabilityMeasure Circle :=
  (torusRootProjection x q hx).map torusCircleHomeomorph

local instance : Fact (0 < (1 : ℝ)) := ⟨zero_lt_one⟩

/-- Normalized Haar probability measure on the additive unit circle. -/
def torusHaar : ProbabilityMeasure Torus :=
  ⟨AddCircle.haarAddCircle, inferInstance⟩

/-- Normalized Haar probability measure on the complex unit circle. -/
def circleHaar : ProbabilityMeasure Circle :=
  torusHaar.map torusCircleHomeomorph

/-- The common anchor as a Dirac probability measure on the complex unit circle. -/
def circleAnchor : ProbabilityMeasure Circle :=
  ⟨Measure.dirac (1 : Circle), inferInstance⟩

/-- The anchor as a Dirac probability measure on the additive unit circle. -/
def torusAnchor : ProbabilityMeasure Torus :=
  ⟨Measure.dirac (0 : Torus), inferInstance⟩

/-- The normalized anchor/Haar mixture on the additive unit circle. -/
def torusAnchorHaar (c : Icc (0 : ℝ) 1) : ProbabilityMeasure Torus where
  val := ENNReal.ofReal c.1 • (torusAnchor : Measure Torus) +
    ENNReal.ofReal (1 - c.1) • (torusHaar : Measure Torus)
  property := ⟨by
    rw [Measure.add_apply]
    simp only [Measure.smul_apply, measure_univ, smul_eq_mul, mul_one]
    rw [← ENNReal.ofReal_add c.2.1 (sub_nonneg.mpr c.2.2)]
    norm_num⟩

/-- The literal anchor/Haar probability mixture on the complex unit circle. -/
def circleAnchorHaar (c : Icc (0 : ℝ) 1) : ProbabilityMeasure Circle :=
  (torusAnchorHaar c).map torusCircleHomeomorph

@[simp] theorem torusCircleHomeomorph_zero : torusCircleHomeomorph (0 : Torus) = (1 : Circle) := by
  simp [torusCircleHomeomorph, AddCircle.homeomorphCircle_apply]

theorem circleAnchorHaar_toMeasure (c : Icc (0 : ℝ) 1) :
    (circleAnchorHaar c : Measure Circle) =
      ENNReal.ofReal c.1 • Measure.dirac (1 : Circle) +
        ENNReal.ofReal (1 - c.1) • (circleHaar : Measure Circle) := by
  change Measure.map torusCircleHomeomorph
      (ENNReal.ofReal c.1 • (torusAnchor : Measure Torus) +
        ENNReal.ofReal (1 - c.1) • (torusHaar : Measure Torus)) = _
  rw [Measure.map_add _ _ torusCircleHomeomorph.continuous.measurable]
  rw [Measure.map_smul _ torusCircleHomeomorph.continuous.aemeasurable]
  rw [Measure.map_smul _ torusCircleHomeomorph.continuous.aemeasurable]
  simp [torusAnchor, circleHaar, torusCircleHomeomorph_zero,
    Measure.map_dirac' torusCircleHomeomorph.continuous.measurable]

@[simp] theorem circleAnchorHaar_zero :
    circleAnchorHaar ⟨0, by simp⟩ = circleHaar := by
  apply ProbabilityMeasure.toMeasure_injective
  simp [circleAnchorHaar_toMeasure]

@[simp] theorem circleAnchorHaar_one :
    circleAnchorHaar ⟨1, by simp⟩ = circleAnchor := by
  apply ProbabilityMeasure.toMeasure_injective
  simp [circleAnchorHaar_toMeasure, circleAnchor]

theorem torusRootProjection_fourier
    {x : ℝ} (hx : x ∈ Ioo 0 1) {q : ℕ} (hq : 0 < q) (k : ℤ) :
    ∫ z, fourier k z ∂(torusRootProjection x q hx : Measure Torus) =
      -Complex.log
          (1 - (x : ℂ) * Complex.exp (2 * Real.pi * Complex.I * k / q)) /
        logScale x := by
  have hroot_meas : Measurable (rootPoint q) := measurable_of_countable _
  change ∫ z, fourier k z ∂Measure.map (rootPoint q) (logSeriesPMF x hx).toMeasure = _
  rw [integral_map hroot_meas.aemeasurable
    ((fourier k).continuous.aestronglyMeasurable)]
  have hint : Integrable (fun n => fourier k (rootPoint q n))
      (logSeriesPMF x hx).toMeasure := by
    refine Integrable.of_bound (by fun_prop) 1 ?_
    exact ae_of_all _ fun n => by simpa [fourier_apply] using (Circle.norm_coe
      (AddCircle.toCircle (k • rootPoint q n)))
  rw [PMF.integral_eq_tsum _ _ hint]
  let ζ : ℂ := Complex.exp (2 * Real.pi * Complex.I * k / q)
  have hζ_norm : ‖ζ‖ = 1 := by
    dsimp [ζ]
    rw [Complex.norm_exp]
    simp
  have hxζ_norm : ‖(x : ℂ) * ζ‖ < 1 := by
    rw [norm_mul, Complex.norm_real, hζ_norm, mul_one, Real.norm_eq_abs,
      abs_of_pos hx.1]
    exact hx.2
  have hlog := (Complex.hasSum_taylorSeries_neg_log' hxζ_norm).div_const (logScale x)
  change _ = -Complex.log (1 - (x : ℂ) * ζ) / logScale x
  rw [← hlog.tsum_eq]
  apply tsum_congr
  intro n
  change ENNReal.toReal (ENNReal.ofReal (logSeriesWeight x n)) •
      fourier k (rootPoint q n) = _
  rw [ENNReal.toReal_ofReal (logSeriesWeight_nonneg hx n), Complex.real_smul]
  rw [show rootPoint q n =
    ((((n + 1 : ℕ) : ℝ) / (q : ℝ) : ℝ) : AddCircle (1 : ℝ)) by rfl]
  rw [fourier_coe_apply]
  simp only [Complex.ofReal_one]
  have hqC : (q : ℂ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hq)
  have hexp :
      Complex.exp (2 * (Real.pi : ℂ) * Complex.I * (k : ℂ) *
        (((((n + 1 : ℕ) : ℝ) / (q : ℝ)) : ℝ) : ℂ) / (1 : ℂ)) = ζ ^ (n + 1) := by
    rw [← Complex.exp_nat_mul]
    congr 1
    push_cast
    field_simp
  rw [hexp, logSeriesWeight, mul_pow]
  push_cast
  field_simp

theorem root_modulus_sq (x θ : ℝ) :
    ‖1 - (x : ℂ) * Complex.exp (θ * Complex.I)‖ ^ 2 =
      (1 - x) ^ 2 + 4 * x * Real.sin (θ / 2) ^ 2 := by
  rw [Complex.sq_norm, Complex.normSq_sub]
  simp [Complex.normSq_mul, Complex.normSq_eq_norm_sq,
    Complex.norm_exp_ofReal_mul_I, Complex.exp_ofReal_mul_I_re,
    Real.sin_sq_eq_half_sub]
  ring

/-- A target-local logarithmic comparison: after normalization by a divergent positive scale,
the logarithm of a sum of two positive terms is governed by the larger term. -/
private theorem neg_log_add_div_tendsto_min
    {a b L : ℕ → ℝ} {A B : ℝ}
    (ha : ∀ᶠ j in atTop, 0 < a j) (hb : ∀ᶠ j in atTop, 0 < b j)
    (hL : ∀ᶠ j in atTop, 0 < L j)
    (hL_top : Tendsto L atTop atTop)
    (ha_lim : Tendsto (fun j => -Real.log (a j) / L j) atTop (nhds A))
    (hb_lim : Tendsto (fun j => -Real.log (b j) / L j) atTop (nhds B)) :
    Tendsto (fun j => -Real.log (a j + b j) / L j) atTop (nhds (min A B)) := by
  let r : ℕ → ℝ := fun j => (a j + b j) / max (a j) (b j)
  have hbounds : ∀ᶠ j in atTop,
      0 < max (a j) (b j) ∧ 0 < r j ∧ 1 ≤ r j ∧ r j ≤ 2 := by
    filter_upwards [ha, hb] with j haj hbj
    have hmj : 0 < max (a j) (b j) := haj.trans_le (le_max_left _ _)
    have hrj : 0 < r j := div_pos (add_pos haj hbj) hmj
    refine ⟨hmj, hrj, ?_, ?_⟩
    · rw [le_div_iff₀ hmj]
      simpa using max_le_add_of_nonneg haj.le hbj.le
    · rw [div_le_iff₀ hmj]
      nlinarith [le_max_left (a j) (b j), le_max_right (a j) (b j)]
  have hlogr_nonneg : ∀ᶠ j in atTop, 0 ≤ Real.log (r j) := by
    filter_upwards [hbounds] with j hj
    simpa using Real.log_nonneg hj.2.2.1
  have hlogr_le : ∀ᶠ j in atTop, Real.log (r j) ≤ Real.log 2 := by
    filter_upwards [hbounds] with j hj
    exact Real.strictMonoOn_log.monotoneOn hj.2.1 (by norm_num) hj.2.2.2
  have hcorr : Tendsto (fun j => Real.log (r j) / L j) atTop (nhds 0) := by
    apply squeeze_zero'
    · filter_upwards [hlogr_nonneg, hL] with j hj hLj
      exact div_nonneg hj hLj.le
    · filter_upwards [hlogr_le, hL] with j hj hLj
      exact (div_le_div_iff_of_pos_right hLj).mpr hj
    · exact hL_top.const_div_atTop (Real.log 2)
  have hmax : Tendsto
      (fun j => -Real.log (max (a j) (b j)) / L j) atTop (nhds (min A B)) := by
    apply (ha_lim.min hb_lim).congr'
    filter_upwards [ha, hb, hL] with j haj hbj hLj
    rcases le_total (a j) (b j) with hab | hba
    · have hlog := Real.strictMonoOn_log.monotoneOn haj hbj hab
      have hnorm : -Real.log (b j) / L j ≤ -Real.log (a j) / L j := by
        rw [div_le_div_iff_of_pos_right hLj]
        exact neg_le_neg hlog
      simp [max_eq_right hab, min_eq_right hnorm]
    · have hlog := Real.strictMonoOn_log.monotoneOn hbj haj hba
      have hnorm : -Real.log (a j) / L j ≤ -Real.log (b j) / L j := by
        rw [div_le_div_iff_of_pos_right hLj]
        exact neg_le_neg hlog
      simp [max_eq_left hba, min_eq_left hnorm]
  have hmain := hmax.sub hcorr
  simpa only [sub_zero] using hmain.congr' (by
    filter_upwards [hbounds] with j hj
    have hm : max (a j) (b j) ≠ 0 := hj.1.ne'
    have hr : r j ≠ 0 := hj.2.1.ne'
    have hfactor : max (a j) (b j) * r j = a j + b j := by
      dsimp [r]
      exact mul_div_cancel₀ _ hm
    rw [← hfactor, Real.log_mul hm hr]
    ring)

private theorem neg_log_add_div_tendsto_left_of_right_atTop
    {a b L : ℕ → ℝ} {A : ℝ}
    (ha : ∀ᶠ j in atTop, 0 < a j) (hb : ∀ᶠ j in atTop, 0 < b j)
    (hL : ∀ᶠ j in atTop, 0 < L j) (hL_top : Tendsto L atTop atTop)
    (ha_lim : Tendsto (fun j => -Real.log (a j) / L j) atTop (nhds A))
    (hb_lim : Tendsto (fun j => -Real.log (b j) / L j) atTop atTop) :
    Tendsto (fun j => -Real.log (a j + b j) / L j) atTop (nhds A) := by
  have hdom : ∀ᶠ j in atTop, b j ≤ a j := by
    have ha_lt := ha_lim.eventually (eventually_lt_nhds (lt_add_one A))
    have hb_gt := hb_lim.eventually (eventually_gt_atTop (A + 1))
    filter_upwards [ha, hb, hL, ha_lt, hb_gt] with j haj hbj hLj haj_lt hbj_gt
    by_contra hba
    have hab : a j < b j := lt_of_not_ge hba
    have hlog := Real.strictMonoOn_log.monotoneOn haj hbj hab.le
    have hnorm : -Real.log (b j) / L j ≤ -Real.log (a j) / L j := by
      rw [div_le_div_iff_of_pos_right hLj]
      exact neg_le_neg hlog
    linarith
  let r : ℕ → ℝ := fun j => (a j + b j) / a j
  have hbounds : ∀ᶠ j in atTop, 0 < r j ∧ 1 ≤ r j ∧ r j ≤ 2 := by
    filter_upwards [ha, hb, hdom] with j haj hbj hba
    have hrj : 0 < r j := div_pos (add_pos haj hbj) haj
    refine ⟨hrj, ?_, ?_⟩
    · rw [le_div_iff₀ haj]
      linarith
    · rw [div_le_iff₀ haj]
      linarith
  have hcorr : Tendsto (fun j => Real.log (r j) / L j) atTop (nhds 0) := by
    apply squeeze_zero'
    · filter_upwards [hbounds, hL] with j hj hLj
      exact div_nonneg (Real.log_nonneg hj.2.1) hLj.le
    · filter_upwards [hbounds, hL] with j hj hLj
      apply (div_le_div_iff_of_pos_right hLj).mpr
      exact Real.strictMonoOn_log.monotoneOn hj.1 (by norm_num) hj.2.2
    · exact hL_top.const_div_atTop (Real.log 2)
  have hmain := ha_lim.sub hcorr
  simpa only [sub_zero] using hmain.congr' (by
    filter_upwards [ha, hbounds] with j haj hrj
    have hfactor : a j * r j = a j + b j := by
      dsimp [r]
      exact mul_div_cancel₀ _ haj.ne'
    rw [← hfactor, Real.log_mul haj.ne' hrj.1.ne']
    ring)

theorem logScale_tendsto_atTop
    {x : ℕ → ℝ} (hx : ∀ j, x j ∈ Ioo 0 1)
    (hx1 : Tendsto x atTop (nhds 1)) :
    Tendsto (fun j => logScale (x j)) atTop atTop := by
  have hsub : Tendsto (fun j => 1 - x j) atTop (nhds 0) := by
    convert tendsto_const_nhds.sub hx1 using 1 <;> simp
  have hwithin : Tendsto (fun j => 1 - x j) atTop (nhdsWithin 0 (Ioi 0)) :=
    tendsto_nhdsWithin_iff.mpr ⟨hsub, Filter.Eventually.of_forall fun j => sub_pos.mpr (hx j).2⟩
  have hlog : Tendsto (fun j => Real.log (1 - x j)) atTop atBot :=
    Real.tendsto_log_nhdsGT_zero.comp hwithin
  change Tendsto (fun j => -Real.log (1 - x j)) atTop atTop
  exact (tendsto_neg_atBot_atTop.comp hlog).congr'
    (Filter.Eventually.of_forall fun _ => rfl)

/-- The chord scale contributed by a fixed nonzero Fourier mode. -/
private def angularScale (x : ℝ) (q : ℕ) (k : ℤ) : ℝ :=
  2 * Real.sqrt x * |Real.sin (Real.pi * (k : ℝ) / (q : ℝ))|

private theorem angularScale_mul_q_tendsto
    (x : ℕ → ℝ) (q : ℕ → ℕ) (hq : ∀ j, 0 < q j)
    (hx1 : Tendsto x atTop (nhds 1)) (hq_top : Tendsto q atTop atTop)
    (k : ℤ) (hk : k ≠ 0) :
    Tendsto (fun j => (q j : ℝ) * angularScale (x j) (q j) k) atTop
      (nhds (2 * |Real.pi * (k : ℝ)|)) := by
  have hqR : Tendsto (fun j => (q j : ℝ)) atTop atTop :=
    tendsto_natCast_atTop_atTop.comp hq_top
  let t : ℕ → ℝ := fun j => Real.pi * (k : ℝ) / (q j : ℝ)
  have ht : Tendsto t atTop (nhds 0) := by
    exact tendsto_const_nhds.div_atTop hqR
  have hsqrt : Tendsto (fun j => Real.sqrt (x j)) atTop (nhds 1) := by
    change Tendsto ((fun y => Real.sqrt y) ∘ x) atTop (nhds 1)
    simpa only [Real.sqrt_one] using Real.continuous_sqrt.continuousAt.tendsto.comp hx1
  have hsinc : Tendsto (fun j => |Real.sinc (t j)|) atTop (nhds 1) := by
    simpa using (Real.continuous_sinc.continuousAt.tendsto.comp ht).abs
  have hproduct : Tendsto
      (fun j => 2 * Real.sqrt (x j) * |Real.pi * (k : ℝ)| * |Real.sinc (t j)|)
      atTop (nhds (2 * |Real.pi * (k : ℝ)|)) := by
    convert (((tendsto_const_nhds.mul hsqrt).mul tendsto_const_nhds).mul hsinc) using 1 <;>
      norm_num
  apply hproduct.congr'
  filter_upwards with j
  have hqjR : (0 : ℝ) < q j := by exact_mod_cast hq j
  have hkR : (k : ℝ) ≠ 0 := by exact_mod_cast hk
  have ht_ne : t j ≠ 0 := div_ne_zero (mul_ne_zero Real.pi_ne_zero hkR) hqjR.ne'
  have hsin : Real.sin (t j) = t j * Real.sinc (t j) := by
    rw [Real.sinc_of_ne_zero ht_ne]
    field_simp
  symm
  change (q j : ℝ) * (2 * Real.sqrt (x j) * |Real.sin (t j)|) = _
  rw [hsin, abs_mul]
  dsimp [t]
  rw [abs_div, abs_mul, abs_of_pos hqjR]
  field_simp

private theorem angularScale_eventually_pos
    (x : ℕ → ℝ) (q : ℕ → ℕ) (hq : ∀ j, 0 < q j)
    (hx1 : Tendsto x atTop (nhds 1)) (hq_top : Tendsto q atTop atTop)
    {k : ℤ} (hk : k ≠ 0) :
    ∀ᶠ j in atTop, 0 < angularScale (x j) (q j) k := by
  have hkR : (k : ℝ) ≠ 0 := by exact_mod_cast hk
  have hc : 0 < 2 * |Real.pi * (k : ℝ)| :=
    mul_pos (by norm_num) (abs_pos.mpr (mul_ne_zero Real.pi_ne_zero hkR))
  have hp := (angularScale_mul_q_tendsto x q hq hx1 hq_top k hk).eventually
    (eventually_gt_nhds hc)
  filter_upwards [hp] with j hj
  have hqjR : (0 : ℝ) < q j := by exact_mod_cast hq j
  nlinarith

private theorem angularProduct_log_div_tendsto_zero
    (x : ℕ → ℝ) (q : ℕ → ℕ)
    (hx : ∀ j, x j ∈ Ioo 0 1) (hq : ∀ j, 0 < q j)
    (hx1 : Tendsto x atTop (nhds 1)) (hq_top : Tendsto q atTop atTop)
    {k : ℤ} (hk : k ≠ 0) :
    Tendsto
      (fun j => Real.log ((q j : ℝ) * angularScale (x j) (q j) k) / logScale (x j))
      atTop (nhds 0) := by
  have hkR : (k : ℝ) ≠ 0 := by exact_mod_cast hk
  have hc_ne : 2 * |Real.pi * (k : ℝ)| ≠ 0 :=
    (mul_ne_zero (by norm_num) (abs_ne_zero.mpr (mul_ne_zero Real.pi_ne_zero hkR)))
  have hp := angularScale_mul_q_tendsto x q hq hx1 hq_top k hk
  have hlog : Tendsto
      (fun j => Real.log ((q j : ℝ) * angularScale (x j) (q j) k)) atTop
      (nhds (Real.log (2 * |Real.pi * (k : ℝ)|))) := by
    change Tendsto (Real.log ∘ (fun j => (q j : ℝ) * angularScale (x j) (q j) k))
      atTop (nhds (Real.log (2 * |Real.pi * (k : ℝ)|)))
    exact Real.continuousAt_log hc_ne |>.tendsto.comp hp
  exact hlog.div_atTop (logScale_tendsto_atTop hx hx1)

private theorem neg_log_angularScale_div_tendsto
    (x : ℕ → ℝ) (q : ℕ → ℕ) (β : ℝ)
    (hx : ∀ j, x j ∈ Ioo 0 1) (hq : ∀ j, 0 < q j)
    (hx1 : Tendsto x atTop (nhds 1)) (hq_top : Tendsto q atTop atTop)
    (hratio : Tendsto (fun j => Real.log (q j : ℝ) / logScale (x j))
      atTop (nhds β)) {k : ℤ} (hk : k ≠ 0) :
    Tendsto (fun j => -Real.log (angularScale (x j) (q j) k) / logScale (x j))
      atTop (nhds β) := by
  have hcorr := angularProduct_log_div_tendsto_zero x q hx hq hx1 hq_top hk
  have hpos := angularScale_eventually_pos x q hq hx1 hq_top hk
  have hmain := hratio.sub hcorr
  simpa only [sub_zero] using hmain.congr' (by
    filter_upwards [hpos] with j hbj
    have hqjR : (q j : ℝ) ≠ 0 := by exact_mod_cast (hq j).ne'
    rw [Real.log_mul hqjR hbj.ne']
    ring)

private theorem neg_log_angularScale_div_tendsto_atTop
    (x : ℕ → ℝ) (q : ℕ → ℕ)
    (hx : ∀ j, x j ∈ Ioo 0 1) (hq : ∀ j, 0 < q j)
    (hx1 : Tendsto x atTop (nhds 1)) (hq_top : Tendsto q atTop atTop)
    (hratio : Tendsto (fun j => Real.log (q j : ℝ) / logScale (x j))
      atTop atTop) {k : ℤ} (hk : k ≠ 0) :
    Tendsto (fun j => -Real.log (angularScale (x j) (q j) k) / logScale (x j))
      atTop atTop := by
  have hcorr := angularProduct_log_div_tendsto_zero x q hx hq hx1 hq_top hk
  have hpos := angularScale_eventually_pos x q hq hx1 hq_top hk
  have hmain : Tendsto
      (fun j => Real.log (q j : ℝ) / logScale (x j) +
        -(Real.log ((q j : ℝ) * angularScale (x j) (q j) k) / logScale (x j)))
      atTop atTop := hratio.atTop_add hcorr.neg
  apply hmain.congr'
  filter_upwards [hpos] with j hbj
  have hqjR : (q j : ℝ) ≠ 0 := by exact_mod_cast (hq j).ne'
  rw [Real.log_mul hqjR hbj.ne']
  ring

private theorem root_norm_sq_eq
    (x : ℝ) (hx : 0 ≤ x) {q : ℕ} (hq : 0 < q) (k : ℤ) :
    ‖1 - (x : ℂ) * Complex.exp (2 * Real.pi * Complex.I * k / q)‖ ^ 2 =
      (1 - x) ^ 2 + angularScale x q k ^ 2 := by
  have hqR : (q : ℝ) ≠ 0 := by exact_mod_cast hq.ne'
  have h := root_modulus_sq x (2 * Real.pi * (k : ℝ) / (q : ℝ))
  convert h using 1
  · congr 3
    push_cast
    field_simp
  · rw [angularScale]
    rw [show 2 * Real.pi * (k : ℝ) / (q : ℝ) / 2 =
      Real.pi * (k : ℝ) / (q : ℝ) by field_simp]
    rw [mul_pow, mul_pow, sq_abs, Real.sq_sqrt]
    · ring
    · exact hx

private theorem finiteRatio_root_norm_limit
    (x : ℕ → ℝ) (q : ℕ → ℕ) (β : ℝ)
    (hx : ∀ j, x j ∈ Ioo 0 1) (hq : ∀ j, 0 < q j)
    (hx1 : Tendsto x atTop (nhds 1)) (hq_top : Tendsto q atTop atTop)
    (hratio : Tendsto (fun j => Real.log (q j : ℝ) / logScale (x j))
      atTop (nhds β)) {k : ℤ} (hk : k ≠ 0) :
    Tendsto
      (fun j => -Real.log
        ‖1 - (x j : ℂ) * Complex.exp (2 * Real.pi * Complex.I * k / q j)‖ /
          logScale (x j))
      atTop (nhds (min 1 β)) := by
  let u2 : ℕ → ℝ := fun j => (1 - x j) ^ 2
  let b2 : ℕ → ℝ := fun j => angularScale (x j) (q j) k ^ 2
  let L : ℕ → ℝ := fun j => logScale (x j)
  have hu2_pos : ∀ᶠ j in atTop, 0 < u2 j :=
    Filter.Eventually.of_forall fun j => sq_pos_of_pos (sub_pos.mpr (hx j).2)
  have hb_pos := angularScale_eventually_pos x q hq hx1 hq_top hk
  have hb2_pos : ∀ᶠ j in atTop, 0 < b2 j := by
    filter_upwards [hb_pos] with j hj
    exact sq_pos_of_pos hj
  have hL_pos : ∀ᶠ j in atTop, 0 < L j :=
    Filter.Eventually.of_forall fun j => logScale_pos (hx j)
  have hu2_lim : Tendsto (fun j => -Real.log (u2 j) / L j) atTop (nhds 2) := by
    apply tendsto_const_nhds.congr'
    filter_upwards with j
    rw [show u2 j = (1 - x j) ^ 2 by rfl, Real.log_pow]
    dsimp [L, logScale]
    have hne : Real.log (1 - x j) ≠ 0 := by
      exact neg_ne_zero.mp (logScale_pos (hx j)).ne'
    field_simp
  have hb_lim := neg_log_angularScale_div_tendsto x q β hx hq hx1 hq_top hratio hk
  have hb2_lim : Tendsto (fun j => -Real.log (b2 j) / L j) atTop (nhds (2 * β)) := by
    apply (hb_lim.const_mul 2).congr'
    filter_upwards [hb_pos] with j hj
    rw [show b2 j = angularScale (x j) (q j) k ^ 2 by rfl, Real.log_pow]
    dsimp [L]
    ring
  have hsum := neg_log_add_div_tendsto_min hu2_pos hb2_pos hL_pos
    (logScale_tendsto_atTop hx hx1) hu2_lim hb2_lim
  have hsum' : Tendsto (fun j => -Real.log (u2 j + b2 j) / L j) atTop
      (nhds (2 * min 1 β)) := by
    convert hsum using 1
    rcases le_total 1 β with h | h
    · simp [min_eq_left h, min_eq_left (by linarith : 2 ≤ 2 * β)]
    · simp [min_eq_right h, min_eq_right (by linarith : 2 * β ≤ 2)]
  have hhalf := hsum'.const_mul (1 / 2 : ℝ)
  convert hhalf using 1
  · ext j
    rw [← root_norm_sq_eq (x j) (hx j).1.le (hq j) k]
    rw [Real.log_pow]
    dsimp [L]
    ring
  · ring

private theorem root_log_im_div_tendsto_zero
    (x : ℕ → ℝ) (q : ℕ → ℕ)
    (hx : ∀ j, x j ∈ Ioo 0 1) (hx1 : Tendsto x atTop (nhds 1)) (k : ℤ) :
    Tendsto
      (fun j => (-Complex.log
        (1 - (x j : ℂ) * Complex.exp (2 * Real.pi * Complex.I * k / q j)) /
          logScale (x j)).im)
      atTop (nhds 0) := by
  let z : ℕ → ℂ := fun j =>
    1 - (x j : ℂ) * Complex.exp (2 * Real.pi * Complex.I * k / q j)
  let L : ℕ → ℝ := fun j => logScale (x j)
  have hL_top : Tendsto L atTop atTop := logScale_tendsto_atTop hx hx1
  have hupper : Tendsto (fun j => Real.pi / L j) atTop (nhds 0) :=
    hL_top.const_div_atTop Real.pi
  have hlower : Tendsto (fun j => -Real.pi / L j) atTop (nhds 0) := by
    simpa only [neg_div, neg_zero] using hupper.neg
  apply tendsto_of_tendsto_of_tendsto_of_le_of_le' hlower hupper
  · filter_upwards with j
    have hLj : 0 < L j := logScale_pos (hx j)
    have him : (Complex.log (z j)).im ≤ Real.pi := Complex.log_im_le_pi _
    have heq : (-Complex.log (z j) / (L j : ℂ)).im =
        -(Complex.log (z j)).im / L j := by
      rw [Complex.div_im]
      simp only [Complex.neg_im, Complex.ofReal_re, Complex.ofReal_im, mul_zero, sub_zero,
        Complex.normSq_ofReal]
      field_simp
      ring
    rw [heq]
    exact (div_le_div_iff_of_pos_right hLj).mpr (by linarith)
  · filter_upwards with j
    have hLj : 0 < L j := logScale_pos (hx j)
    have him : -Real.pi < (Complex.log (z j)).im := Complex.neg_pi_lt_log_im _
    have heq : (-Complex.log (z j) / (L j : ℂ)).im =
        -(Complex.log (z j)).im / L j := by
      rw [Complex.div_im]
      simp only [Complex.neg_im, Complex.ofReal_re, Complex.ofReal_im, mul_zero, sub_zero,
        Complex.normSq_ofReal]
      field_simp
      ring
    rw [heq]
    exact (div_le_div_iff_of_pos_right hLj).mpr (by linarith)

theorem finiteRatio_mode_limit
    (x : ℕ → ℝ) (q : ℕ → ℕ) (β : ℝ)
    (hx : ∀ j, x j ∈ Ioo 0 1) (hq : ∀ j, 0 < q j)
    (hx1 : Tendsto x atTop (nhds 1)) (hq_top : Tendsto q atTop atTop)
    (_hβ : 0 ≤ β)
    (hratio : Tendsto (fun j => Real.log (q j : ℝ) / logScale (x j))
      atTop (nhds β)) {k : ℤ} (hk : k ≠ 0) :
    Tendsto
      (fun j => -Complex.log
        (1 - (x j : ℂ) * Complex.exp (2 * Real.pi * Complex.I * k / q j)) /
          logScale (x j))
      atTop (nhds ((min (1 : ℝ) β : ℝ) : ℂ)) := by
  let z : ℕ → ℂ := fun j =>
    -Complex.log
      (1 - (x j : ℂ) * Complex.exp (2 * Real.pi * Complex.I * k / q j)) /
        logScale (x j)
  have hre0 := finiteRatio_root_norm_limit x q β hx hq hx1 hq_top hratio hk
  have hre : Tendsto (fun j => (z j).re) atTop (nhds (min 1 β)) := by
    apply hre0.congr'
    filter_upwards with j
    dsimp [z]
    rw [Complex.div_re]
    simp only [Complex.neg_re, Complex.neg_im, Complex.ofReal_re, Complex.ofReal_im, mul_zero,
      add_zero, Complex.normSq_ofReal, Complex.log_re]
    have hL : logScale (x j) ≠ 0 := (logScale_pos (hx j)).ne'
    field_simp
    ring
  have him : Tendsto (fun j => (z j).im) atTop (nhds 0) := by
    simpa only [z] using root_log_im_div_tendsto_zero x q hx hx1 k
  have hparts := hre.ofReal.add (him.ofReal.mul (tendsto_const_nhds :
    Tendsto (fun _ : ℕ => Complex.I) atTop (nhds Complex.I)))
  have hz : Tendsto z atTop (nhds ((min (1 : ℝ) β : ℝ) : ℂ)) := by
    convert hparts using 1
    · ext j
      exact (Complex.re_add_im (z j)).symm
    · simp
  exact hz

private theorem divergentRatio_root_norm_limit
    (x : ℕ → ℝ) (q : ℕ → ℕ)
    (hx : ∀ j, x j ∈ Ioo 0 1) (hq : ∀ j, 0 < q j)
    (hx1 : Tendsto x atTop (nhds 1)) (hq_top : Tendsto q atTop atTop)
    (hratio : Tendsto (fun j => Real.log (q j : ℝ) / logScale (x j))
      atTop atTop) {k : ℤ} (hk : k ≠ 0) :
    Tendsto
      (fun j => -Real.log
        ‖1 - (x j : ℂ) * Complex.exp (2 * Real.pi * Complex.I * k / q j)‖ /
          logScale (x j))
      atTop (nhds 1) := by
  let u2 : ℕ → ℝ := fun j => (1 - x j) ^ 2
  let b2 : ℕ → ℝ := fun j => angularScale (x j) (q j) k ^ 2
  let L : ℕ → ℝ := fun j => logScale (x j)
  have hu2_pos : ∀ᶠ j in atTop, 0 < u2 j :=
    Filter.Eventually.of_forall fun j => sq_pos_of_pos (sub_pos.mpr (hx j).2)
  have hb_pos := angularScale_eventually_pos x q hq hx1 hq_top hk
  have hb2_pos : ∀ᶠ j in atTop, 0 < b2 j := by
    filter_upwards [hb_pos] with j hj
    exact sq_pos_of_pos hj
  have hL_pos : ∀ᶠ j in atTop, 0 < L j :=
    Filter.Eventually.of_forall fun j => logScale_pos (hx j)
  have hu2_lim : Tendsto (fun j => -Real.log (u2 j) / L j) atTop (nhds 2) := by
    apply tendsto_const_nhds.congr'
    filter_upwards with j
    rw [show u2 j = (1 - x j) ^ 2 by rfl, Real.log_pow]
    dsimp [L, logScale]
    have hne : Real.log (1 - x j) ≠ 0 :=
      neg_ne_zero.mp (logScale_pos (hx j)).ne'
    field_simp
  have hb_lim := neg_log_angularScale_div_tendsto_atTop x q hx hq hx1 hq_top hratio hk
  have hb2_lim : Tendsto (fun j => -Real.log (b2 j) / L j) atTop atTop := by
    apply (Filter.Tendsto.const_mul_atTop (r := (2 : ℝ)) (by norm_num) hb_lim).congr'
    filter_upwards [hb_pos] with j hj
    rw [show b2 j = angularScale (x j) (q j) k ^ 2 by rfl, Real.log_pow]
    dsimp [L]
    ring
  have hsum := neg_log_add_div_tendsto_left_of_right_atTop hu2_pos hb2_pos hL_pos
    (logScale_tendsto_atTop hx hx1) hu2_lim hb2_lim
  have hhalf := hsum.const_mul (1 / 2 : ℝ)
  convert hhalf using 1
  · ext j
    rw [← root_norm_sq_eq (x j) (hx j).1.le (hq j) k]
    rw [Real.log_pow]
    dsimp [L]
    ring
  · ring

theorem divergentRatio_mode_limit
    (x : ℕ → ℝ) (q : ℕ → ℕ)
    (hx : ∀ j, x j ∈ Ioo 0 1) (hq : ∀ j, 0 < q j)
    (hx1 : Tendsto x atTop (nhds 1)) (hq_top : Tendsto q atTop atTop)
    (hratio : Tendsto (fun j => Real.log (q j : ℝ) / logScale (x j))
      atTop atTop) {k : ℤ} (hk : k ≠ 0) :
    Tendsto
      (fun j => -Complex.log
        (1 - (x j : ℂ) * Complex.exp (2 * Real.pi * Complex.I * k / q j)) /
          logScale (x j))
      atTop (nhds (1 : ℂ)) := by
  let z : ℕ → ℂ := fun j =>
    -Complex.log
      (1 - (x j : ℂ) * Complex.exp (2 * Real.pi * Complex.I * k / q j)) /
        logScale (x j)
  have hre0 := divergentRatio_root_norm_limit x q hx hq hx1 hq_top hratio hk
  have hre : Tendsto (fun j => (z j).re) atTop (nhds 1) := by
    apply hre0.congr'
    filter_upwards with j
    dsimp [z]
    rw [Complex.div_re]
    simp only [Complex.neg_re, Complex.neg_im, Complex.ofReal_re, Complex.ofReal_im, mul_zero,
      add_zero, Complex.normSq_ofReal, Complex.log_re]
    have hL : logScale (x j) ≠ 0 := (logScale_pos (hx j)).ne'
    field_simp
    ring
  have him : Tendsto (fun j => (z j).im) atTop (nhds 0) := by
    simpa only [z] using root_log_im_div_tendsto_zero x q hx hx1 k
  have hparts := hre.ofReal.add (him.ofReal.mul (tendsto_const_nhds :
    Tendsto (fun _ : ℕ => Complex.I) atTop (nhds Complex.I)))
  have hz : Tendsto z atTop (nhds (1 : ℂ)) := by
    convert hparts using 1
    · ext j
      exact (Complex.re_add_im (z j)).symm
    · simp
  exact hz

/-- On the compact additive circle, convergence of every integer Fourier coefficient upgrades to
weak convergence of probability measures. -/
theorem tendsto_torus_probabilityMeasure_of_fourier
    {μ : ℕ → ProbabilityMeasure Torus} {ν : ProbabilityMeasure Torus}
    (h : ∀ k : ℤ,
      Tendsto (fun j => ∫ z, fourier k z ∂(μ j : Measure Torus)) atTop
        (nhds (∫ z, fourier k z ∂(ν : Measure Torus)))) :
    Tendsto μ atTop (nhds ν) := by
  let φ := BoundedContinuousFunction.toContinuousMapStarₐ (α := Torus) (β := ℂ) ℂ
  let A : StarSubalgebra ℂ (BoundedContinuousFunction Torus ℂ) := fourierSubalgebra.comap φ
  have hmap : A.map φ = (@fourierSubalgebra (1 : ℝ)) := by
    ext f
    constructor
    · intro hf
      rw [StarSubalgebra.mem_map] at hf
      obtain ⟨g, hg, rfl⟩ := hf
      exact (StarSubalgebra.mem_comap _ _ _).mp hg
    · intro hf
      let g : BoundedContinuousFunction Torus ℂ :=
        ContinuousMap.equivBoundedOfCompact Torus ℂ f
      refine (StarSubalgebra.mem_map).mpr ⟨g, ?_, ?_⟩
      · apply (StarSubalgebra.mem_comap _ _ _).mpr
        convert hf using 1
        ext z
        rfl
      · ext z
        rfl
  apply ProbabilityMeasure.tendsto_of_tight_of_separatesPoints ℂ
    (IsTightMeasureSet.of_compactSpace) (A := A)
  · rw [hmap]
    exact fourierSubalgebra_separatesPoints
  · intro g hg
    have hspan : g.toContinuousMap ∈ Submodule.span ℂ (range (@fourier (1 : ℝ))) := by
      rw [← fourierSubalgebra_coe]
      exact (StarSubalgebra.mem_comap _ _ _).mp hg
    let P : C(Torus, ℂ) → Prop := fun f =>
      Tendsto (fun j => ∫ z, f z ∂(μ j : Measure Torus)) atTop
        (nhds (∫ z, f z ∂(ν : Measure Torus)))
    have hint (f : C(Torus, ℂ)) (ρ : ProbabilityMeasure Torus) :
        Integrable f (ρ : Measure Torus) := by
      exact (ContinuousMap.equivBoundedOfCompact Torus ℂ f).integrable _
    have hP : P g.toContinuousMap := by
      refine Submodule.span_induction (p := fun f _ => P f) ?_ ?_ ?_ ?_ hspan
      · intro f hf
        obtain ⟨k, rfl⟩ := hf
        exact h k
      · simpa [P]
      · intro f₁ f₂ _ _ hf₁ hf₂
        dsimp [P] at hf₁ hf₂ ⊢
        simpa only [ContinuousMap.add_apply, integral_add (hint f₁ _) (hint f₂ _)] using hf₁.add hf₂
      · intro c f _ hf
        dsimp [P] at hf ⊢
        simpa only [ContinuousMap.smul_apply, smul_eq_mul, integral_const_mul] using hf.const_mul c
    exact hP

theorem torusHaar_fourier (k : ℤ) :
    ∫ z, fourier k z ∂(torusHaar : Measure Torus) = if k = 0 then 1 else 0 := by
  by_cases hk : k = 0
  · subst k
    simp [torusHaar]
  · rw [if_neg hk]
    change ∫ z, fourier k z ∂AddCircle.haarAddCircle = 0
    exact integral_eq_zero_of_add_right_eq_neg
      (fourier_add_half_inv_index hk (by norm_num))

theorem torusAnchorHaar_fourier (c : Icc (0 : ℝ) 1) (k : ℤ) :
    ∫ z, fourier k z ∂(torusAnchorHaar c : Measure Torus) =
      if k = 0 then 1 else (c.1 : ℂ) := by
  have hint (ρ : Measure Torus) [IsFiniteMeasure ρ] : Integrable (fourier k) ρ := by
    exact (ContinuousMap.equivBoundedOfCompact Torus ℂ (fourier k)).integrable _
  change ∫ z, fourier k z ∂(ENNReal.ofReal c.1 • (torusAnchor : Measure Torus) +
    ENNReal.ofReal (1 - c.1) • (torusHaar : Measure Torus)) = _
  rw [integral_add_measure]
  · rw [integral_smul_measure, integral_smul_measure]
    change ENNReal.toReal (ENNReal.ofReal c.1) •
        ∫ z, fourier k z ∂Measure.dirac (0 : Torus) +
      ENNReal.toReal (ENNReal.ofReal (1 - c.1)) •
        ∫ z, fourier k z ∂(torusHaar : Measure Torus) = _
    rw [integral_dirac, torusHaar_fourier]
    by_cases hk : k = 0
    · subst k
      simp [c.2.1, sub_nonneg.mpr c.2.2]
    · simp [hk, c.2.1]
  · exact (hint (torusAnchor : Measure Torus)).smul_measure ENNReal.ofReal_ne_top
  · exact (hint (torusHaar : Measure Torus)).smul_measure ENNReal.ofReal_ne_top

/-- Principal theorem A: finite logarithmic scale ratio. -/
theorem finiteScale_circleRootProjection_tendsto
    (x : ℕ → ℝ) (q : ℕ → ℕ) (β : ℝ)
    (hx : ∀ j, x j ∈ Ioo 0 1) (hq : ∀ j, 0 < q j)
    (hx1 : Tendsto x atTop (nhds 1)) (hq_top : Tendsto q atTop atTop)
    (hβ : 0 ≤ β)
    (hratio : Tendsto (fun j => Real.log (q j : ℝ) / logScale (x j))
      atTop (nhds β)) :
    Tendsto (fun j => circleRootProjection (x j) (q j) (hx j)) atTop
      (nhds (circleAnchorHaar ⟨min 1 β, by constructor <;> simp [hβ]⟩)) := by
  let c : Icc (0 : ℝ) 1 := ⟨min 1 β, by constructor <;> simp [hβ]⟩
  have htorus : Tendsto (fun j => torusRootProjection (x j) (q j) (hx j)) atTop
      (nhds (torusAnchorHaar c)) := by
    apply tendsto_torus_probabilityMeasure_of_fourier
    intro k
    by_cases hk : k = 0
    · subst k
      simp [torusAnchorHaar_fourier]
    · have hm := finiteRatio_mode_limit x q β hx hq hx1 hq_top hβ hratio hk
      convert hm using 1
      · ext j
        exact torusRootProjection_fourier (hx j) (hq j) k
      · rw [torusAnchorHaar_fourier, if_neg hk]
  have hmap := ProbabilityMeasure.tendsto_map_of_tendsto_of_continuous
    _ _ htorus torusCircleHomeomorph.continuous
  simpa [circleRootProjection, circleAnchorHaar, c] using hmap

theorem torusAnchor_fourier (k : ℤ) :
    ∫ z, fourier k z ∂(torusAnchor : Measure Torus) = 1 := by
  change ∫ z, fourier k z ∂Measure.dirac (0 : Torus) = 1
  simp [fourier_apply]

/-- Principal theorem B: divergent logarithmic scale ratio. -/
theorem divergentScale_circleRootProjection_tendsto
    (x : ℕ → ℝ) (q : ℕ → ℕ)
    (hx : ∀ j, x j ∈ Ioo 0 1) (hq : ∀ j, 0 < q j)
    (hx1 : Tendsto x atTop (nhds 1)) (hq_top : Tendsto q atTop atTop)
    (hratio : Tendsto (fun j => Real.log (q j : ℝ) / logScale (x j))
      atTop atTop) :
    Tendsto (fun j => circleRootProjection (x j) (q j) (hx j)) atTop
      (nhds circleAnchor) := by
  have htorus : Tendsto (fun j => torusRootProjection (x j) (q j) (hx j)) atTop
      (nhds torusAnchor) := by
    apply tendsto_torus_probabilityMeasure_of_fourier
    intro k
    by_cases hk : k = 0
    · subst k
      simp [torusAnchor_fourier]
    · have hm := divergentRatio_mode_limit x q hx hq hx1 hq_top hratio hk
      convert hm using 1
      · ext j
        exact torusRootProjection_fourier (hx j) (hq j) k
      · rw [torusAnchor_fourier]
  have hmap := ProbabilityMeasure.tendsto_map_of_tendsto_of_continuous
    _ _ htorus torusCircleHomeomorph.continuous
  have hanchor : torusAnchor.map torusCircleHomeomorph = circleAnchor := by
    apply ProbabilityMeasure.toMeasure_injective
    change Measure.map torusCircleHomeomorph (Measure.dirac (0 : Torus)) = Measure.dirac (1 : Circle)
    rw [Measure.map_dirac' torusCircleHomeomorph.continuous.measurable]
    rw [torusCircleHomeomorph_zero]
  simpa [circleRootProjection, hanchor] using hmap

theorem finiteScale_circleRootProjection_tendsto_zero
    (x : ℕ → ℝ) (q : ℕ → ℕ)
    (hx : ∀ j, x j ∈ Ioo 0 1) (hq : ∀ j, 0 < q j)
    (hx1 : Tendsto x atTop (nhds 1)) (hq_top : Tendsto q atTop atTop)
    (hratio : Tendsto (fun j => Real.log (q j : ℝ) / logScale (x j))
      atTop (nhds 0)) :
    Tendsto (fun j => circleRootProjection (x j) (q j) (hx j)) atTop
      (nhds circleHaar) := by
  have h := finiteScale_circleRootProjection_tendsto x q 0 hx hq hx1 hq_top (by norm_num) hratio
  have hc : (⟨min 1 (0 : ℝ), by constructor <;> norm_num⟩ : Icc (0 : ℝ) 1) =
      ⟨0, by constructor <;> norm_num⟩ := by ext; norm_num
  rw [hc, circleAnchorHaar_zero] at h
  exact h

theorem finiteScale_circleRootProjection_tendsto_one
    (x : ℕ → ℝ) (q : ℕ → ℕ)
    (hx : ∀ j, x j ∈ Ioo 0 1) (hq : ∀ j, 0 < q j)
    (hx1 : Tendsto x atTop (nhds 1)) (hq_top : Tendsto q atTop atTop)
    (hratio : Tendsto (fun j => Real.log (q j : ℝ) / logScale (x j))
      atTop (nhds 1)) :
    Tendsto (fun j => circleRootProjection (x j) (q j) (hx j)) atTop
      (nhds circleAnchor) := by
  have h := finiteScale_circleRootProjection_tendsto x q 1 hx hq hx1 hq_top (by norm_num) hratio
  have hc : (⟨min 1 (1 : ℝ), by constructor <;> norm_num⟩ : Icc (0 : ℝ) 1) =
      ⟨1, by constructor <;> norm_num⟩ := by ext; norm_num
  rw [hc, circleAnchorHaar_one] at h
  exact h

theorem finiteScale_circleRootProjection_tendsto_two
    (x : ℕ → ℝ) (q : ℕ → ℕ)
    (hx : ∀ j, x j ∈ Ioo 0 1) (hq : ∀ j, 0 < q j)
    (hx1 : Tendsto x atTop (nhds 1)) (hq_top : Tendsto q atTop atTop)
    (hratio : Tendsto (fun j => Real.log (q j : ℝ) / logScale (x j))
      atTop (nhds 2)) :
    Tendsto (fun j => circleRootProjection (x j) (q j) (hx j)) atTop
      (nhds circleAnchor) := by
  have h := finiteScale_circleRootProjection_tendsto x q 2 hx hq hx1 hq_top (by norm_num) hratio
  have hc : (⟨min 1 (2 : ℝ), by constructor <;> norm_num⟩ : Icc (0 : ℝ) 1) =
      ⟨1, by constructor <;> norm_num⟩ := by ext; norm_num
  rw [hc, circleAnchorHaar_one] at h
  exact h

#print axioms finiteScale_circleRootProjection_tendsto
#print axioms divergentScale_circleRootProjection_tendsto

end Mathia.PC063
