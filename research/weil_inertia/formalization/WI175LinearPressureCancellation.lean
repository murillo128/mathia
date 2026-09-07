import Mathlib.Data.ZMod.Basic
import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.BigOperators.Field
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# WI-175: cyclic linear-pressure averaging and scalar witness cancellation

Associated finding:
`research/weil_inertia/findings/WI-175-linear-gap-pressure-reweighting-is-periodic-witness-cancelled.md`.
The exact witness constants come from that finding and
`research/weil_inertia/findings/WI-026-periodic-witness-caps-arbitrary-four-point-local-surplus.md`.

Formalized boundary: averaging a fixed linear gap pressure over every cyclic phase retains
only its coefficient sum. A universal local lower bound and a strict mean-defect cap then
bound the local constant. Under the explicitly assumed scalar assembly identity, the
nontrivial branch has positive denominators and lies below the witness density minus its
exact margin, giving the rational ceiling `673604 / 10^6` for the WI-175 constants.

The period-33 energy certificate (including MPFR intervals and the analytic tail), the
Montgomery--Taylor kernel/Gram interpretation, and the zeta asymptotic passage are outside
this formalized boundary. Their consequences are imported as mathematical premises, not
as new Lean axioms. This is conditional on the stated scalar assembly identity.
-/

noncomputable section

open scoped BigOperators

namespace Mathia.WI175

/-- Uniform mean over a nonempty cyclic set of phases. -/
def phaseMean {q : ℕ} [NeZero q] (f : ZMod q → ℝ) : ℝ :=
  (∑ s, f s) / q

/-- Zero-based `j.val` is the source's relative gap position `j - 1`.
Offsets wrap cyclically even when the block is longer than the period. -/
def linearPressure {q : ℕ} (m : ℕ) (gap : ZMod q → ℝ)
    (alpha : Fin (m - 1) → ℝ) (s : ZMod q) : ℝ :=
  ∑ j, alpha j * gap (s + (j.val : ZMod q))

theorem phaseMean_translate {q : ℕ} [NeZero q] (f : ZMod q → ℝ) (t : ZMod q) :
    phaseMean (fun s => f (s + t)) = phaseMean f := by
  unfold phaseMean
  congr 1
  exact Equiv.sum_comp (Equiv.addRight t) f

theorem phaseMean_add {q : ℕ} [NeZero q] (f g : ZMod q → ℝ) :
    phaseMean (fun s => f s + g s) = phaseMean f + phaseMean g := by
  simp only [phaseMean, Finset.sum_add_distrib, add_div]

/-- Linearity and cyclic translation alone prove the pressure identity; neither the gaps
nor the coefficients need a sign assumption here. -/
theorem linearPressure_phaseMean {q m : ℕ} [NeZero q]
    (gap : ZMod q → ℝ) (alpha : Fin (m - 1) → ℝ) :
    phaseMean (linearPressure m gap alpha) = (∑ j, alpha j) * phaseMean gap := by
  unfold phaseMean linearPressure
  rw [Finset.sum_comm]
  simp_rw [← Finset.mul_sum]
  have hshift (j : Fin (m - 1)) :
      (∑ s : ZMod q, gap (s + (j.val : ZMod q))) = ∑ s, gap s :=
    Equiv.sum_comp (Equiv.addRight (j.val : ZMod q)) gap
  simp_rw [hshift]
  rw [← Finset.sum_mul]
  ring

theorem linearPressure_mean_of_gap_mean {q m : ℕ} [NeZero q]
    (gap : ZMod q → ℝ) (alpha : Fin (m - 1) → ℝ) {r : ℝ}
    (hgap : phaseMean gap = 1 / r) :
    phaseMean (linearPressure m gap alpha) = (∑ j, alpha j) / r := by
  rw [linearPressure_phaseMean, hgap]
  ring

/-- Finite phase averaging yields the source's local cap, with no boundary loss.
The mean-defect bound is a premise; its analytic provenance is outside this module. -/
theorem local_constant_cap {q m : ℕ} [NeZero q]
    (gap defect : ZMod q → ℝ) (alpha : Fin (m - 1) → ℝ) {r dstar C : ℝ}
    (hgap : phaseMean gap = 1 / r)
    (hdefect : phaseMean defect < (m : ℝ) * dstar)
    (hlocal : ∀ s, C ≤ defect s + linearPressure m gap alpha s) :
    C < (m : ℝ) * dstar + (∑ j, alpha j) / r := by
  have hq : (0 : ℝ) < q := Nat.cast_pos.mpr (NeZero.pos q)
  have hlower : C ≤ phaseMean (fun s => defect s + linearPressure m gap alpha s) := by
    apply (le_div_iff₀ hq).2
    have hs := Finset.sum_le_sum (s := Finset.univ) (fun s _ => hlocal s)
    simpa [ZMod.card, mul_comm] using hs
  rw [phaseMean_add, linearPressure_mean_of_gap_mean gap alpha hgap] at hlower
  linarith

/-- The repaired sign surface: the comparison denominator lies in `(0,1]`.
Nonnegativity of `dstar` is essential for its upper bound. -/
theorem comparison_denominator_bounds {r a dstar H Hstar eps : ℝ}
    (hr : 0 < r) (ha : 0 ≤ a) (hd : 0 ≤ dstar) (hH : H < Hstar)
    (hmargin : eps < r * (1 - dstar) - Hstar) (heps : 0 < eps)
    (haH : a < H) :
    0 < 1 - dstar - a / r ∧ 1 - dstar - a / r ≤ 1 := by
  have har : a / r < 1 - dstar := (div_lt_iff₀ hr).2 (by nlinarith)
  have hnonneg : 0 ≤ a / r := div_nonneg ha hr.le
  constructor <;> linarith

/-- Exact pressure cancellation in the witness comparison (WI-175 (17)). -/
theorem witness_difference {r a dstar Hstar : ℝ} (hr : r ≠ 0)
    (hb : 1 - dstar - a / r ≠ 0) :
    r - (Hstar - a) / (1 - dstar - a / r) =
      (r * (1 - dstar) - Hstar) / (1 - dstar - a / r) := by
  apply (eq_div_iff hb).2
  rw [sub_mul, div_mul_cancel₀ _ hb]
  field_simp
  ring

/-- The scalar implication in normalized variables `a = A/m`, `c = C/m`. -/
theorem normalized_scalar_cancellation {r a c dstar H Hstar eps : ℝ}
    (hr : 0 < r) (ha : 0 ≤ a) (hd : 0 ≤ dstar) (hH : H < Hstar)
    (hmargin : eps < r * (1 - dstar) - Hstar) (heps : 0 < eps)
    (haH : a < H) (hcap : c < dstar + a / r) :
    0 < 1 - c ∧ (H - a) / (1 - c) < r - eps := by
  obtain ⟨hb, hb1⟩ := comparison_denominator_bounds hr ha hd hH hmargin heps haH
  have hbc : 1 - dstar - a / r < 1 - c := by linarith
  have hc : 0 < 1 - c := lt_trans hb hbc
  refine ⟨hc, ?_⟩
  have hcompare : (H - a) / (1 - c) < (Hstar - a) / (1 - dstar - a / r) :=
    lt_trans (div_lt_div_of_pos_left (sub_pos.mpr haH) hb hbc)
      (div_lt_div_of_pos_right (by linarith) hb)
  have hdelta : eps < (r * (1 - dstar) - Hstar) / (1 - dstar - a / r) := by
    apply (lt_div_iff₀ hb).2
    have := mul_le_mul_of_nonneg_left hb1 heps.le
    nlinarith
  rw [← witness_difference (ne_of_gt hr) (ne_of_gt hb)] at hdelta
  linarith

/-- Explicit connection to the finding's unnormalized scalar bridge. -/
theorem scalar_bridge_normalization {m : ℝ} (hm : m ≠ 0) (H A C : ℝ) :
    (m * H - A) / (m - C) = (H - A / m) / (1 - C / m) := by
  have hn : H - A / m = (m * H - A) / m := by field_simp
  have hd : 1 - C / m = (m - C) / m := by field_simp
  rw [hn, hd, div_div_div_cancel_right₀ hm]

/-- WI-175's repaired generic endpoint, conditional on its scalar assembly identity.
The conclusion also certifies positivity of both comparison and assembly denominators. -/
theorem scalar_cancellation {m r A dstar H Hstar eps C R : ℝ}
    (hm : 0 < m) (hr : 0 < r) (hA : 0 ≤ A) (hd : 0 ≤ dstar)
    (hH : H < Hstar) (hmargin : eps < r * (1 - dstar) - Hstar)
    (heps : 0 < eps) (hbranch : A / m < H) (hcap : C < m * dstar + A / r)
    (hR : R = (m * H - A) / (m - C)) :
    0 < 1 - dstar - A / (m * r) ∧ 1 - dstar - A / (m * r) ≤ 1 ∧
      0 < m - C ∧ R < r - eps := by
  have ha : 0 ≤ A / m := div_nonneg hA hm.le
  have hc : C / m < dstar + (A / m) / r := by
    apply (div_lt_iff₀ hm).2
    have heq : (dstar + (A / m) / r) * m = m * dstar + A / r := by
      field_simp
    rw [heq]
    exact hcap
  obtain ⟨hb, hb1⟩ := comparison_denominator_bounds hr ha hd hH hmargin heps hbranch
  obtain ⟨hden, hresult⟩ := normalized_scalar_cancellation hr ha hd hH hmargin heps
    hbranch hc
  have hCm : C < m := (div_lt_one hm).mp (by linarith : C / m < 1)
  rw [div_div] at hb hb1
  refine ⟨hb, hb1, sub_pos.mpr hCm, ?_⟩
  rw [hR, scalar_bridge_normalization (ne_of_gt hm)]
  exact hresult

/-- Nonnegative individual coefficients are consumed here to obtain nonnegative total
pressure mass; the bare phase-average identity above is valid for signed coefficients. -/
theorem cyclic_pressure_cancellation {q m : ℕ} [NeZero q]
    (hm : 0 < m) (gap defect : ZMod q → ℝ) (alpha : Fin (m - 1) → ℝ)
    (halpha : ∀ j, 0 ≤ alpha j) {r dstar H Hstar eps C R : ℝ}
    (hr : 0 < r) (hd : 0 ≤ dstar) (hH : H < Hstar)
    (hmargin : eps < r * (1 - dstar) - Hstar) (heps : 0 < eps)
    (hgap : phaseMean gap = 1 / r) (hdefect : phaseMean defect < (m : ℝ) * dstar)
    (hlocal : ∀ s, C ≤ defect s + linearPressure m gap alpha s)
    (hbranch : (∑ j, alpha j) / (m : ℝ) < H)
    (hR : R = ((m : ℝ) * H - ∑ j, alpha j) / ((m : ℝ) - C)) :
    R < r - eps := by
  exact (scalar_cancellation (Nat.cast_pos.mpr hm) hr
    (Finset.sum_nonneg fun j _ => halpha j) hd hH hmargin heps hbranch
    (local_constant_cap gap defect alpha hgap hdefect hlocal) hR).2.2.2

/-- Exact WI-019/WI-026 witness inputs, with no decimal or floating-point premises. -/
def witnessDensity : ℝ := 67361 / 100000
def witnessDefectCap : ℝ := 1637 / 10^6 + 45379580714321 / 74507812500000000000
def baselineCap : ℝ := 672500704 / 10^9
def witnessEpsilon : ℝ := 6 / 10^6

theorem exact_witness_margin :
    witnessDensity * (1 - witnessDefectCap) - baselineCap =
      46091743024440123119 / 7450781250000000000000000 := by
  norm_num [witnessDensity, witnessDefectCap, baselineCap]

/-- Exact WI-175 rational ceiling under the source's local cap and scalar bridge. -/
theorem wi175_rational_ceiling {m A H C R : ℝ} (hm : 0 < m) (hA : 0 ≤ A)
    (hH : H < baselineCap) (hbranch : A / m < H)
    (hcap : C < m * witnessDefectCap + A / witnessDensity)
    (hR : R = (m * H - A) / (m - C)) :
    R < 673604 / 10^6 := by
  have h := scalar_cancellation hm (by norm_num [witnessDensity]) hA
    (by norm_num [witnessDefectCap]) hH
    (show witnessEpsilon < witnessDensity * (1 - witnessDefectCap) - baselineCap by
      rw [exact_witness_margin]; norm_num [witnessEpsilon])
    (by norm_num [witnessEpsilon]) hbranch hcap hR
  norm_num [witnessDensity, witnessEpsilon] at h
  norm_num
  exact h.2.2.2

/-- Complete finite/algebraic WI-175 composition at the exact witness constants.
No restriction compares block length with period length. -/
theorem cyclic_wi175_rational_ceiling {q m : ℕ} [NeZero q]
    (hm : 0 < m) (gap defect : ZMod q → ℝ) (alpha : Fin (m - 1) → ℝ)
    (halpha : ∀ j, 0 ≤ alpha j) {H C R : ℝ}
    (hH : H < baselineCap) (hgap : phaseMean gap = 1 / witnessDensity)
    (hdefect : phaseMean defect < (m : ℝ) * witnessDefectCap)
    (hlocal : ∀ s, C ≤ defect s + linearPressure m gap alpha s)
    (hbranch : (∑ j, alpha j) / (m : ℝ) < H)
    (hR : R = ((m : ℝ) * H - ∑ j, alpha j) / ((m : ℝ) - C)) :
    R < 673604 / 10^6 := by
  exact wi175_rational_ceiling (Nat.cast_pos.mpr hm)
    (Finset.sum_nonneg fun j _ => halpha j) hH hbranch
    (local_constant_cap gap defect alpha hgap hdefect hlocal) hR

#print axioms linearPressure_mean_of_gap_mean
#print axioms scalar_cancellation
#print axioms cyclic_pressure_cancellation
#print axioms wi175_rational_ceiling
#print axioms cyclic_wi175_rational_ceiling

end Mathia.WI175
