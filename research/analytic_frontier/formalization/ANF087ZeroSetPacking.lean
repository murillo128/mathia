import Mathlib.Analysis.SpecialFunctions.Trigonometric.Sinc
import Mathlib.Data.Finset.Card
import Mathlib.Tactic

/-!
# Montgomery--Taylor real zero-set rigidity

Associated finding:
`research/analytic_frontier/findings/ANF-087-montgomery-taylor-equality-is-a-two-site-real-zero-set-packing.md`.

Formalized theorem boundary: the continuous explicit Montgomery--Taylor factor has exactly
one positive zero in each interval `(n, n + 1/2)`, for integers `n ≥ 1`, with strictly
decreasing offsets. Its positive zero set is sum-free, and a finite real set whose distinct
pair differences are zeros has at most two sites. The removable points are not zeros.
The addition-formula argument in fact proves sum-freeness of the entire real zero set.

Not formalized: Lamzouri's global Hilbert inequality, exclusion of nonreal equality,
stationary/Palm closure, zeta implications, and the ANF-086 quantitative near-extremizer
problem. No numerical root evidence is used.
-/

open Set

noncomputable section

namespace Mathia.ANF087

def theta : ℝ := 1 / Real.sqrt 2

def a : ℝ := Real.sqrt 2 * Real.pi * (Real.cos theta / Real.sin theta)

/-- A continuous definition which resolves both apparent poles simultaneously. -/
def K (x : ℝ) : ℝ := theta / (2 * Real.sin theta) *
  (Real.sinc (Real.pi * x - theta) + Real.sinc (Real.pi * x + theta))

def numerator (x : ℝ) : ℝ := Real.cos (Real.pi * x) - a * x * Real.sin (Real.pi * x)

def denominator (x : ℝ) : ℝ := 1 - 2 * Real.pi ^ 2 * x ^ 2

def x0 : ℝ := theta / Real.pi

lemma theta_pos : 0 < theta := by unfold theta; positivity

lemma sqrt_two_eq : Real.sqrt 2 = 2 * theta := by
  have hs := Real.sq_sqrt (show (0 : ℝ) ≤ 2 by norm_num)
  have hn : Real.sqrt 2 ≠ 0 := by positivity
  unfold theta
  field_simp
  nlinarith

lemma theta_sq : theta ^ 2 = 1 / 2 := by
  have hs := Real.sq_sqrt (show (0 : ℝ) ≤ 2 by norm_num)
  rw [sqrt_two_eq] at hs
  nlinarith

lemma theta_lt_one : theta < 1 := by nlinarith [theta_sq, theta_pos]

lemma theta_lt_pi_div_two : theta < Real.pi / 2 := by
  linarith [theta_lt_one, Real.two_le_pi]

lemma sin_theta_pos : 0 < Real.sin theta :=
  Real.sin_pos_of_pos_of_lt_pi theta_pos (by linarith [theta_lt_pi_div_two, Real.pi_pos])

lemma cos_theta_pos : 0 < Real.cos theta :=
  Real.cos_pos_of_mem_Ioo ⟨by linarith [theta_pos, Real.pi_pos], theta_lt_pi_div_two⟩

lemma a_pos : 0 < a := by
  unfold a
  exact mul_pos (mul_pos (by positivity) Real.pi_pos) (div_pos cos_theta_pos sin_theta_pos)

theorem continuous_K : Continuous K := by unfold K; fun_prop

theorem K_even (x : ℝ) : K (-x) = K x := by
  unfold K
  rw [show Real.pi * -x - theta = -(Real.pi * x + theta) by ring,
    show Real.pi * -x + theta = -(Real.pi * x - theta) by ring,
    Real.sinc_neg, Real.sinc_neg, add_comm]

private lemma mul_sinc (t : ℝ) : t * Real.sinc t = Real.sin t := by
  by_cases ht : t = 0
  · simp [ht]
  · rw [Real.sinc_of_ne_zero ht]
    field_simp

/-- The cancellation identity is valid even at the removable points. -/
theorem K_mul_denominator (x : ℝ) : K x * denominator x = numerator x := by
  have hd : denominator x = -2 * (Real.pi * x - theta) * (Real.pi * x + theta) := by
    unfold denominator
    nlinarith [theta_sq]
  rw [K, hd]
  calc
    _ = -theta / Real.sin theta *
        ((Real.pi * x + theta) * ((Real.pi * x - theta) * Real.sinc (Real.pi * x - theta)) +
         (Real.pi * x - theta) * ((Real.pi * x + theta) * Real.sinc (Real.pi * x + theta))) := by ring
    _ = -theta / Real.sin theta *
        ((Real.pi * x + theta) * Real.sin (Real.pi * x - theta) +
         (Real.pi * x - theta) * Real.sin (Real.pi * x + theta)) := by rw [mul_sinc, mul_sinc]
    _ = numerator x := by
      rw [Real.sin_sub, Real.sin_add, numerator, a, sqrt_two_eq]
      field_simp [sin_theta_pos.ne']
      linear_combination 2 * Real.cos (Real.pi * x) * Real.sin theta * theta_sq

theorem denominator_eq_zero_iff (x : ℝ) : denominator x = 0 ↔ x = x0 ∨ x = -x0 := by
  have hp := Real.pi_pos
  have he : denominator x = -2 * (Real.pi * x - theta) * (Real.pi * x + theta) := by
    unfold denominator
    nlinarith [theta_sq]
  rw [he]
  rw [mul_eq_zero, mul_eq_zero]
  norm_num
  unfold x0
  constructor
  · rintro (h | h)
    · left; apply (eq_div_iff hp.ne').2; linarith
    · right; rw [← neg_div]; apply (eq_div_iff hp.ne').2; linarith
  · rintro (rfl | rfl) <;> simp [hp.ne', mul_div_cancel₀]

theorem K_eq_quotient {x : ℝ} (hx : x ≠ x0) (hx' : x ≠ -x0) :
    K x = numerator x / denominator x := by
  exact (eq_div_iff (fun h => (denominator_eq_zero_iff x).1 h |>.elim hx hx')).2
    (K_mul_denominator x)

theorem K_x0 : K x0 = (theta / Real.sin theta + Real.cos theta) / 2 := by
  have hp := Real.pi_pos.ne'
  have ht := theta_pos.ne'
  have hs := sin_theta_pos.ne'
  have hx : Real.pi * x0 = theta := by unfold x0; field_simp
  rw [K, hx, sub_self, Real.sinc_zero, show theta + theta = 2 * theta by ring,
    Real.sinc_of_ne_zero (mul_ne_zero (by norm_num) ht), Real.sin_two_mul]
  field_simp

theorem K_x0_exact : K x0 = (1 / Real.sin theta + theta⁻¹ * Real.cos theta) / (4 * theta) := by
  rw [K_x0]
  field_simp [sin_theta_pos.ne', theta_pos.ne']
  rw [theta_sq]
  ring

theorem K_neg_x0 : K (-x0) = (theta / Real.sin theta + Real.cos theta) / 2 := by
  rw [K_even, K_x0]

theorem K_x0_pos : 0 < K x0 := by
  rw [K_x0]
  exact div_pos (add_pos (div_pos theta_pos sin_theta_pos) cos_theta_pos) (by norm_num)

theorem K_neg_x0_pos : 0 < K (-x0) := by rw [K_even]; exact K_x0_pos

theorem removable_cancellation : numerator x0 = 0 ∧ denominator x0 = 0 := by
  have hd := (denominator_eq_zero_iff x0).2 (Or.inl rfl)
  exact ⟨by simpa [hd] using (K_mul_denominator x0).symm, hd⟩

theorem numerator_eq_zero_of_K_eq_zero {x : ℝ} (hx : K x = 0) : numerator x = 0 := by
  simpa [hx] using (K_mul_denominator x).symm

theorem K_eq_zero_iff {x : ℝ} (hx : x ≠ x0) (hx' : x ≠ -x0) :
    K x = 0 ↔ numerator x = 0 := by
  rw [K_eq_quotient hx hx', div_eq_zero_iff]
  exact or_iff_left (fun h => (denominator_eq_zero_iff x).1 h |>.elim hx hx')

/-- The numerator in a cell, with its harmless periodic sign removed. -/
def cell (n : ℕ) (d : ℝ) : ℝ :=
  Real.cos (Real.pi * d) - a * (n + d) * Real.sin (Real.pi * d)

lemma numerator_cell (n : ℕ) (d : ℝ) :
    numerator (n + d) = (-1) ^ n * cell n d := by
  unfold numerator cell
  rw [show Real.pi * (n + d) = Real.pi * d + n * Real.pi by ring,
    Real.sin_add_nat_mul_pi, Real.cos_add_nat_mul_pi]
  ring

lemma numerator_cell_eq_zero_iff (n : ℕ) (d : ℝ) :
    numerator (n + d) = 0 ↔ cell n d = 0 := by
  rw [numerator_cell, mul_eq_zero]
  simp

lemma continuous_cell (n : ℕ) : Continuous (cell n) := by unfold cell; fun_prop

lemma cell_zero (n : ℕ) : cell n 0 = 1 := by simp [cell]

lemma cell_half (n : ℕ) : cell n (1 / 2) = -a * (n + 1 / 2) := by
  unfold cell
  rw [show Real.pi * (1 / 2) = Real.pi / 2 by ring, Real.cos_pi_div_two, Real.sin_pi_div_two]
  ring

lemma cell_half_neg (n : ℕ) : cell n (1 / 2) < 0 := by
  rw [cell_half]
  have hn : (0 : ℝ) ≤ n := Nat.cast_nonneg n
  nlinarith [a_pos]

lemma cell_strictAnti (n : ℕ) : StrictAntiOn (cell n) (Icc 0 (1 / 2)) := by
  intro d hd e he hde
  have hp := Real.pi_pos
  have hn : (0 : ℝ) ≤ n := Nat.cast_nonneg n
  have hpd : Real.pi * d ∈ Icc 0 Real.pi := by constructor <;> nlinarith [hd.1, hd.2]
  have hpe : Real.pi * e ∈ Icc 0 Real.pi := by constructor <;> nlinarith [he.1, he.2]
  have hc := Real.strictAntiOn_cos hpd hpe (mul_lt_mul_of_pos_left hde hp)
  have hs : Real.sin (Real.pi * d) ≤ Real.sin (Real.pi * e) :=
    Real.monotoneOn_sin (by constructor <;> nlinarith [hd.1, hd.2])
      (by constructor <;> nlinarith [he.1, he.2]) (by nlinarith)
  have hsd : 0 ≤ Real.sin (Real.pi * d) :=
    Real.sin_nonneg_of_nonneg_of_le_pi hpd.1 hpd.2
  have hm : (n + d) * Real.sin (Real.pi * d) ≤ (n + e) * Real.sin (Real.pi * e) :=
    mul_le_mul (by linarith) hs hsd (by linarith [he.1])
  have := mul_le_mul_of_nonneg_left hm a_pos.le
  unfold cell
  nlinarith

/-- Existence includes cell zero; that cell's numerator root is later removed. -/
lemma existsUnique_cell_root (n : ℕ) :
    ∃! d : ℝ, d ∈ Ioo 0 (1 / 2) ∧ cell n d = 0 := by
  have hi := intermediate_value_Icc' (show (0 : ℝ) ≤ 1 / 2 by norm_num)
    (continuous_cell n).continuousOn
  obtain ⟨d, hd, hz⟩ := hi ⟨(cell_half_neg n).le, by rw [cell_zero]; norm_num⟩
  have hd0 : 0 < d := by
    by_contra! h
    have : d = 0 := le_antisymm h hd.1
    subst d
    simp [cell_zero] at hz
  have hd1 : d < 1 / 2 := by
    by_contra! h
    have : d = 1 / 2 := le_antisymm hd.2 h
    subst d
    linarith [cell_half_neg n]
  refine ⟨d, ⟨⟨hd0, hd1⟩, hz⟩, ?_⟩
  intro e he
  exact (cell_strictAnti n).injOn ⟨he.1.1.le, he.1.2.le⟩ hd (he.2.trans hz.symm)

lemma cell_neg_second_half (n : ℕ) {d : ℝ} (hd : d ∈ Ico (1 / 2) 1) :
    cell n d < 0 := by
  have hp := Real.pi_pos
  have hn : (0 : ℝ) ≤ n := Nat.cast_nonneg n
  have hc : Real.cos (Real.pi * d) ≤ 0 :=
    Real.cos_nonpos_of_pi_div_two_le_of_le (by nlinarith [hd.1]) (by nlinarith [hd.2])
  have hs : 0 < Real.sin (Real.pi * d) :=
    Real.sin_pos_of_pos_of_lt_pi (by nlinarith [hd.1]) (by nlinarith [hd.2])
  have hm : 0 < a * (n + d) * Real.sin (Real.pi * d) :=
    mul_pos (mul_pos a_pos (by linarith [hd.1])) hs
  unfold cell
  linarith

lemma cell_root_mem {n : ℕ} {d : ℝ} (hd : d ∈ Ico 0 1) (hz : cell n d = 0) :
    d ∈ Ioo 0 (1 / 2) := by
  constructor
  · by_contra! h
    have : d = 0 := le_antisymm h hd.1
    subst d
    simp [cell_zero] at hz
  · by_contra! h
    linarith [cell_neg_second_half n ⟨h, hd.2⟩]

lemma x0_mem : x0 ∈ Ioo 0 (1 / 2) := by
  unfold x0
  constructor
  · exact div_pos theta_pos Real.pi_pos
  · apply (div_lt_iff₀ Real.pi_pos).2
    linarith [theta_lt_pi_div_two]

lemma cell_zero_x0 : cell 0 x0 = 0 := by
  simpa using (numerator_cell_eq_zero_iff 0 x0).1 (by simpa using removable_cancellation.1)

/-- The complete classification excludes the initial cell and all half-cell endpoints. -/
theorem positive_zero_localization {x : ℝ} (hx : 0 < x) (hz : K x = 0) :
    ∃ n : ℕ, 1 ≤ n ∧ x - n ∈ Ioo 0 (1 / 2) ∧ cell n (x - n) = 0 := by
  let n : ℕ := ⌊x⌋₊
  have hnle : (n : ℝ) ≤ x := Nat.floor_le hx.le
  have hnx : x < n + 1 := Nat.lt_floor_add_one x
  have hd : x - n ∈ Ico 0 1 := ⟨by linarith, by linarith⟩
  have hc : cell n (x - n) = 0 := (numerator_cell_eq_zero_iff n _).1 (by
    simpa using numerator_eq_zero_of_K_eq_zero hz)
  have hmem := cell_root_mem hd hc
  have hn : 1 ≤ n := by
    by_contra! h
    have hn0 : n = 0 := by omega
    have heq : x - n = x0 := (cell_strictAnti 0).injOn
      ⟨hmem.1.le, hmem.2.le⟩ ⟨x0_mem.1.le, x0_mem.2.le⟩ (by simpa [hn0, cell_zero_x0] using hc)
    have hxx : x = x0 := by simpa [hn0] using heq
    rw [hxx] at hz
    linarith [K_x0_pos]
  exact ⟨n, hn, hmem, hc⟩

lemma K_cell_eq_zero_iff {n : ℕ} (hn : 1 ≤ n) {d : ℝ} (hd : d ∈ Ioo 0 (1 / 2)) :
    K (n + d) = 0 ↔ cell n d = 0 := by
  have hn' : (1 : ℝ) ≤ n := by exact_mod_cast hn
  rw [K_eq_zero_iff (by linarith [hd.1, x0_mem.2]) (by linarith [hd.1, x0_mem.1]),
    numerator_cell_eq_zero_iff]

theorem existsUnique_positive_root (n : ℕ) (hn : 1 ≤ n) :
    ∃! x : ℝ, x ∈ Ioo (n : ℝ) (n + 1 / 2) ∧ K x = 0 := by
  obtain ⟨d, hd, hu⟩ := existsUnique_cell_root n
  refine ⟨n + d, ⟨⟨by linarith [hd.1.1], by linarith [hd.1.2]⟩,
    (K_cell_eq_zero_iff hn hd.1).2 hd.2⟩, ?_⟩
  intro x hx
  have hm : x - n ∈ Ioo 0 (1 / 2) := ⟨by linarith [hx.1.1], by linarith [hx.1.2]⟩
  have hc : cell n (x - n) = 0 := (K_cell_eq_zero_iff hn hm).1 (by simpa using hx.2)
  have := hu (x - n) ⟨hm, hc⟩
  linarith

/-- Includes the half-integer endpoint, in every nonnegative cell. -/
theorem K_ne_zero_second_half (n : ℕ) {d : ℝ} (hd : d ∈ Ico (1 / 2) 1) :
    K (n + d) ≠ 0 := by
  intro hz
  have hc := (numerator_cell_eq_zero_iff n d).1 (numerator_eq_zero_of_K_eq_zero hz)
  linarith [cell_neg_second_half n hd]

theorem K_ne_zero_nat (n : ℕ) : K n ≠ 0 := by
  intro hz
  have hc := (numerator_cell_eq_zero_iff n 0).1 (by
    simpa using numerator_eq_zero_of_K_eq_zero hz)
  simp [cell_zero] at hc

theorem K_ne_zero_initial_cell {x : ℝ} (hx : x ∈ Ioo 0 1) : K x ≠ 0 := by
  intro hz
  obtain ⟨n, hn, hd, _⟩ := positive_zero_localization hx.1 hz
  have hn' : (1 : ℝ) ≤ n := by exact_mod_cast hn
  linarith [hd.1, hx.2]

/-- The exact implicit tangent equation, with all denominators nonzero. -/
theorem root_tangent_equation {n : ℕ} {d : ℝ} (hd : d ∈ Ioo 0 (1 / 2))
    (hz : cell n d = 0) : Real.tan (Real.pi * d) = 1 / (a * (n + d)) := by
  have hp := Real.pi_pos
  have hn : (0 : ℝ) ≤ n := Nat.cast_nonneg n
  have hc : Real.cos (Real.pi * d) ≠ 0 :=
    (Real.cos_pos_of_mem_Ioo ⟨by nlinarith [hd.1], by nlinarith [hd.2]⟩).ne'
  have ha : a * (n + d) ≠ 0 := (mul_pos a_pos (by linarith [hd.1])).ne'
  rw [Real.tan_eq_sin_div_cos]
  apply (div_eq_div_iff hc ha).2
  unfold cell at hz
  nlinarith

/-- Increasing the cell index strictly decreases the offset of its unique root. -/
theorem cell_root_offsets_strict {m n : ℕ} (hmn : m < n) {d e : ℝ}
    (hd : d ∈ Ioo 0 (1 / 2)) (he : e ∈ Ioo 0 (1 / 2))
    (hmd : cell m d = 0) (hne : cell n e = 0) : e < d := by
  have hp := Real.pi_pos
  have hmn' : (m : ℝ) < n := by exact_mod_cast hmn
  have hs : 0 < Real.sin (Real.pi * d) :=
    Real.sin_pos_of_pos_of_lt_pi (by nlinarith [hd.1]) (by nlinarith [hd.2])
  have hdiff : cell m d - cell n d = a * (n - m) * Real.sin (Real.pi * d) := by
    unfold cell
    ring
  have hnd : cell n d < 0 := by
    have := mul_pos (mul_pos a_pos (sub_pos.mpr hmn')) hs
    linarith
  by_contra! h
  have := (cell_strictAnti n).antitoneOn ⟨hd.1.le, hd.2.le⟩ ⟨he.1.le, he.2.le⟩ h
  linarith

theorem positive_root_offsets_strict {m n : ℕ} (hmn : m < n) {u v : ℝ}
    (hu : u ∈ Ioo (m : ℝ) (m + 1 / 2)) (hv : v ∈ Ioo (n : ℝ) (n + 1 / 2))
    (hzu : K u = 0) (hzv : K v = 0) : v - n < u - m := by
  apply cell_root_offsets_strict hmn
    (show u - m ∈ Ioo 0 (1 / 2) from ⟨by linarith [hu.1], by linarith [hu.2]⟩)
    (show v - n ∈ Ioo 0 (1 / 2) from ⟨by linarith [hv.1], by linarith [hv.2]⟩)
  · exact (numerator_cell_eq_zero_iff m _).1 (by
      simpa using numerator_eq_zero_of_K_eq_zero hzu)
  · exact (numerator_cell_eq_zero_iff n _).1 (by
      simpa using numerator_eq_zero_of_K_eq_zero hzv)

lemma sin_ne_zero_of_numerator_zero {x : ℝ} (hx : numerator x = 0) :
    Real.sin (Real.pi * x) ≠ 0 := by
  intro hs
  have hc : Real.cos (Real.pi * x) = 0 := by simpa [numerator, hs] using hx
  have := Real.sin_sq_add_cos_sq (Real.pi * x)
  simp [hs, hc] at this

/-- Addition formulas give a direct additive obstruction, even without sign hypotheses. -/
lemma numerator_add_ne_zero {u v : ℝ} (hu : numerator u = 0) (hv : numerator v = 0) :
    numerator (u + v) ≠ 0 := by
  have hcu : Real.cos (Real.pi * u) = a * u * Real.sin (Real.pi * u) := by
    unfold numerator at hu
    linarith
  have hcv : Real.cos (Real.pi * v) = a * v * Real.sin (Real.pi * v) := by
    unfold numerator at hv
    linarith
  have hid : numerator (u + v) =
      -(1 + a ^ 2 * (u ^ 2 + u * v + v ^ 2)) * Real.sin (Real.pi * u) * Real.sin (Real.pi * v) := by
    unfold numerator
    rw [mul_add, Real.cos_add, Real.sin_add, hcu, hcv]
    ring
  have hq : 0 ≤ u ^ 2 + u * v + v ^ 2 := by
    nlinarith [sq_nonneg u, sq_nonneg v, sq_nonneg (u + v)]
  have hb : 0 < 1 + a ^ 2 * (u ^ 2 + u * v + v ^ 2) := by
    nlinarith [mul_nonneg (sq_nonneg a) hq]
  rw [hid]
  exact mul_ne_zero (mul_ne_zero (neg_ne_zero.mpr hb.ne')
    (sin_ne_zero_of_numerator_zero hu)) (sin_ne_zero_of_numerator_zero hv)

theorem zero_add_ne_zero {u v : ℝ} (hu : K u = 0) (hv : K v = 0) : K (u + v) ≠ 0 := by
  intro huv
  exact numerator_add_ne_zero (numerator_eq_zero_of_K_eq_zero hu)
    (numerator_eq_zero_of_K_eq_zero hv) (numerator_eq_zero_of_K_eq_zero huv)

def positiveZeros : Set ℝ := {x | 0 < x ∧ K x = 0}

theorem positive_zero_sum_free {u v : ℝ} (hu : u ∈ positiveZeros) (hv : v ∈ positiveZeros) :
    u + v ∉ positiveZeros := fun h => zero_add_ne_zero hu.2 hv.2 h.2

theorem three_point_obstruction {x₁ x₂ x₃ : ℝ}
    (h₁₂ : K (x₂ - x₁) = 0) (h₂₃ : K (x₃ - x₂) = 0) : K (x₃ - x₁) ≠ 0 := by
  have := zero_add_ne_zero h₁₂ h₂₃
  simpa using this

/-- Ordered pair hypotheses supply the needed orientations directly; no evenness is used. -/
theorem packing_card_le_two (X : Finset ℝ)
    (hX : ∀ x ∈ X, ∀ y ∈ X, x ≠ y → K (x - y) = 0) : X.card ≤ 2 := by
  by_contra! h
  obtain ⟨x, y, z, hx, hy, hz, hxy, hxz, hyz⟩ := Finset.two_lt_card_iff.1 h
  exact three_point_obstruction (hX y hy x hx hxy.symm)
    (hX z hz y hy hyz.symm) (hX z hz x hx hxz.symm)

end Mathia.ANF087
