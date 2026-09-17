import FD173AnnulusHitting
import Mathlib.NumberTheory.DiophantineApproximation.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.GCongr
import Mathlib.Tactic.Ring

/-!
# FD-174 quantitative geometric midpoint certification

Associated finding:
`research/farey_discrepancy/findings/FD-174-integer-geometric-midpoint-ladders-have-explicit-finite-scale-certification.md`

Formalized theorem boundary: for an integer base B ≥ 3, every odd prime-power
orbit meets (B^k/2, B^k] with the explicit FD-174 bounds on both exponent and
ladder index. The first K_B(X) horizons hit all odd primes through real scale
X ≥ 3 and control their nonnegative defect coordinates via FD-173.

The Farey/source-stability interpretation is inherited from the already-formalized
FD-173 hitting interface plus the external midpoint bridge. The Farey midpoint
identity itself, extension to source coefficients, sharper dyadic bounds,
optimality, Franel--Landau estimates, and RH are not formalized here.
-/

noncomputable section
namespace Mathia.FD174

/-- Bounded denominator used for the near-return. -/
def Q (B : ℕ) : ℕ := ⌊Real.log B / Real.log 2⌋₊ + 1

/-- The explicit constant of FD-174. -/
def C (B : ℕ) : ℝ := (Q B : ℝ) * (1 + Real.sqrt B * Real.log B)

/-- Number of horizons sufficient through source scale X. -/
def K (B : ℕ) (X : ℝ) : ℕ :=
  ⌈C B * X ^ Q B * (Real.log X / Real.log B)⌉₊ + 1

private theorem log_base_pos {B : ℕ} (hB : 3 ≤ B) : 0 < Real.log B :=
  Real.log_pos (by exact_mod_cast (show 1 < B by omega))

private theorem window_bounds {B : ℕ} (hB : 3 ≤ B) :
    0 < Real.log 2 / Real.log B ∧ Real.log 2 / Real.log B < 1 ∧
    2 ≤ Q B ∧ 1 / (Q B : ℝ) < Real.log 2 / Real.log B := by
  have hb := log_base_pos hB
  have h2 : 0 < Real.log 2 := Real.log_pos (by norm_num)
  have h2b : Real.log 2 < Real.log B :=
    Real.log_lt_log (by norm_num) (by exact_mod_cast (show 2 < B by omega))
  have hfloor : 1 ≤ ⌊Real.log B / Real.log 2⌋₊ := by
    apply (Nat.le_floor_iff (by positivity)).2
    norm_num
    exact (le_div_iff₀ h2).2 (by linarith)
  have hQ : 2 ≤ Q B := by unfold Q; omega
  have hqr : (0 : ℝ) < Q B := by exact_mod_cast (show 0 < Q B by omega)
  have hlt : Real.log B / Real.log 2 < (Q B : ℝ) := by
    simpa [Q] using Nat.lt_floor_add_one (Real.log B / Real.log 2)
  refine ⟨div_pos h2 hb, (div_lt_one hb).2 h2b, hQ, ?_⟩
  apply (div_lt_div_iff₀ hqr hb).2
  have := (div_lt_iff₀ h2).1 hlt
  nlinarith

/-- Elementary logarithmic separation, in a form without division. -/
private theorem log_separation {x y : ℝ} (hx : 0 < x) (hy : 0 < y) :
    |x - y| ≤ |Real.log x - Real.log y| * max x y := by
  suffices h : ∀ a b : ℝ, 0 < a → 0 < b → a ≤ b →
      b - a ≤ (Real.log b - Real.log a) * b by
    rcases le_total x y with hxy | hyx
    · rw [abs_of_nonpos (sub_nonpos.mpr hxy),
        abs_of_nonpos (sub_nonpos.mpr (Real.log_le_log hx hxy)), max_eq_right hxy]
      linarith [h x y hx hy hxy]
    · rw [abs_of_nonneg (sub_nonneg.mpr hyx),
        abs_of_nonneg (sub_nonneg.mpr (Real.log_le_log hy hyx)), max_eq_left hyx]
      exact h y x hy hx hyx
  intro a b ha hb _
  have hl := Real.log_le_sub_one_of_pos (div_pos ha hb)
  rw [Real.log_div ha.ne' hb.ne'] at hl
  have := (mul_le_mul_of_nonneg_right hl hb.le)
  have he : (a / b - 1) * b = a - b := by field_simp
  rw [he] at this
  nlinarith

/-- Distinct natural atoms have separation at least one after casting to reals. -/
private theorem integer_separation {u v : ℕ} (hne : u ≠ v) :
    (1 : ℝ) ≤ |(u : ℝ) - v| := by
  rcases lt_or_gt_of_ne hne with h | h
  · have hh : (u : ℝ) + 1 ≤ v := by exact_mod_cast h
    rw [abs_of_nonpos (by linarith)]
    linarith
  · have hh : (v : ℝ) + 1 ≤ u := by exact_mod_cast h
    rw [abs_of_nonneg (by linarith)]
    linarith

/-- A bounded-denominator nonexact return cannot be too small: its two
exponentials are distinct integers. Primality is not needed in this estimate. -/
private theorem inverse_error_bound {B p q m : ℕ} (hB : 3 ≤ B) (hp : 2 ≤ p)
    (hq : q ≤ Q B)
    (hne : (q : ℝ) * (Real.log p / Real.log B) - m ≠ 0)
    (hsmall : |(q : ℝ) * (Real.log p / Real.log B) - m| < 1 / 2) :
    1 / |(q : ℝ) * (Real.log p / Real.log B) - m| ≤
      Real.sqrt B * Real.log B * (p : ℝ) ^ Q B := by
  let d := |(q : ℝ) * (Real.log p / Real.log B) - m|
  have hd : 0 < d := abs_pos.mpr hne
  have hb : (0 : ℝ) < B := by exact_mod_cast (show 0 < B by omega)
  have hp0 : (0 : ℝ) < p := by exact_mod_cast (show 0 < p by omega)
  have hp1 : (1 : ℝ) ≤ p := by exact_mod_cast (show 1 ≤ p by omega)
  have hlb := log_base_pos hB
  have hs : 0 < Real.sqrt B := Real.sqrt_pos.mpr hb
  have hs1 : 1 ≤ Real.sqrt (B : ℝ) := Real.one_le_sqrt.mpr (by exact_mod_cast (show 1 ≤ B by omega))
  have hx : (0 : ℝ) < (p : ℝ)^q := pow_pos hp0 _
  have hy : (0 : ℝ) < (B : ℝ)^m := pow_pos hb _
  have he : Real.log ((p : ℝ)^q) - Real.log ((B : ℝ)^m) =
      ((q : ℝ) * (Real.log p / Real.log B) - m) * Real.log B := by
    rw [Real.log_pow, Real.log_pow]
    field_simp
  have heabs : |Real.log ((p : ℝ)^q) - Real.log ((B : ℝ)^m)| = d * Real.log B := by
    rw [he, abs_mul, abs_of_pos hlb]
  have hneq : p^q ≠ B^m := by
    intro hh
    have hh' : (p : ℝ)^q = (B : ℝ)^m := by exact_mod_cast hh
    have hz : Real.log ((p : ℝ)^q) - Real.log ((B : ℝ)^m) = 0 := by rw [hh']; ring
    rw [he] at hz
    exact hne ((mul_eq_zero.mp hz).resolve_right hlb.ne')
  have hsep : (1 : ℝ) ≤ |(p : ℝ)^q - (B : ℝ)^m| := by
    exact_mod_cast integer_separation hneq
  have hmax : max ((p : ℝ)^q) ((B : ℝ)^m) ≤ Real.sqrt B * (p : ℝ)^q := by
    apply max_le
    · nlinarith
    · apply (Real.log_le_log_iff hy (mul_pos hs hx)).mp
      rw [Real.log_mul hs.ne' hx.ne', Real.log_sqrt hb.le]
      have hlog := (abs_le.mp (le_of_lt (show d < 1 / 2 from hsmall))).1
      have hh := mul_le_mul_of_nonneg_right hlog hlb.le
      have he' : (q : ℝ) * Real.log p - (m : ℝ) * Real.log B =
          ((q : ℝ) * (Real.log p / Real.log B) - m) * Real.log B := by
        field_simp
      rw [Real.log_pow, Real.log_pow]
      nlinarith [he']
  have hlogsep := log_separation hx hy
  rw [heabs] at hlogsep
  have hpow := pow_le_pow_right₀ hp1 hq
  have hbound : 1 ≤ d * (Real.sqrt B * Real.log B * (p : ℝ)^Q B) := by
    calc
      1 ≤ d * Real.log B * max ((p : ℝ)^q) ((B : ℝ)^m) := hsep.trans hlogsep
      _ ≤ d * Real.log B * (Real.sqrt B * (p : ℝ)^q) :=
        mul_le_mul_of_nonneg_left hmax (by positivity)
      _ ≤ d * Real.log B * (Real.sqrt B * (p : ℝ)^Q B) := by gcongr
      _ = _ := by ring
  exact (div_le_iff₀ hd).2 (by nlinarith [hbound])

/-- Amplify a positive small return into the one-sided window, without wrap. -/
private theorem amplify {L d : ℝ} (_hL0 : 0 < L) (hL1 : L < 1)
    (hd : 0 < d) (hdL : d < L) :
    ∃ n : ℕ, 1 ≤ n ∧ 1 - L < (n : ℝ) * d ∧ (n : ℝ) * d < 1 ∧
      (n : ℝ) ≤ 1 + 1 / d := by
  let n : ℕ := ⌊(1 - L) / d⌋₊ + 1
  have hn : (n : ℝ) = (⌊(1 - L) / d⌋₊ : ℝ) + 1 := by simp [n]
  have hlo := Nat.lt_floor_add_one ((1 - L) / d)
  have hup := Nat.floor_le (show 0 ≤ (1 - L) / d by positivity)
  refine ⟨n, by dsimp [n]; omega, ?_, ?_, ?_⟩
  · rw [← hn] at hlo
    exact (div_lt_iff₀ hd).1 hlo
  · have ht : (n : ℝ) * d ≤ 1 - L + d := by
      rw [hn]
      have hh := (le_div_iff₀ hd).1 hup
      nlinarith
    linarith
  · rw [hn]
    have : (1 - L) / d ≤ 1 / d := by gcongr; linarith
    linarith

private theorem exponent_budget {B p : ℕ} (hB : 3 ≤ B) (hp : 2 ≤ p) :
    (Q B : ℝ) * (1 + Real.sqrt B * Real.log B * (p : ℝ)^Q B) ≤
      C B * (p : ℝ)^Q B := by
  have hlb := log_base_pos hB
  have hpow : (1 : ℝ) ≤ (p : ℝ)^Q B :=
    one_le_pow₀ (by exact_mod_cast (show 1 ≤ p by omega))
  dsimp [C]
  nlinarith [mul_nonneg (show (0 : ℝ) ≤ Q B by positivity) (sub_nonneg.mpr hpow)]

/-- The logarithmic recurrence proof works for every integer orbit generator ≥ 2.
The closed endpoint includes exact returns. -/
private theorem logarithmic_hit {B p : ℕ} (hB : 3 ≤ B) (hp : 2 ≤ p) :
    ∃ j k : ℕ, 1 ≤ j ∧ 1 ≤ k ∧
      0 ≤ (k : ℝ) - (j : ℝ) * (Real.log p / Real.log B) ∧
      (k : ℝ) - (j : ℝ) * (Real.log p / Real.log B) < Real.log 2 / Real.log B ∧
      (j : ℝ) ≤ C B * (p : ℝ)^Q B := by
  let a := Real.log p / Real.log B
  let L := Real.log 2 / Real.log B
  have ha : 0 < a := div_pos
    (Real.log_pos (by exact_mod_cast (show 1 < p by omega))) (log_base_pos hB)
  obtain ⟨hL0, hL1, hQ2, hQL⟩ := window_bounds hB
  have hQ0 : 0 < Q B := by omega
  obtain ⟨q, hq0, hqQ, happrox⟩ := Real.exists_nat_abs_mul_sub_round_le a hQ0
  have hr : 0 ≤ round ((q : ℝ) * a) := by
    rw [round_eq]
    apply Int.floor_nonneg.mpr
    positivity
  let m := (round ((q : ℝ) * a)).toNat
  have hm : (m : ℝ) = (round ((q : ℝ) * a) : ℝ) := by
    exact_mod_cast Int.toNat_of_nonneg hr
  rw [← hm] at happrox
  have hqpos : (0 : ℝ) < q := by exact_mod_cast hq0
  have hqr : (q : ℝ) ≤ Q B := by exact_mod_cast hqQ
  have hQr : (0 : ℝ) < Q B := by exact_mod_cast hQ0
  have hsmall : |(q : ℝ) * a - m| < 1 / (Q B : ℝ) :=
    happrox.trans_lt (by apply one_div_lt_one_div_of_lt hQr; linarith)
  have hhalf : |(q : ℝ) * a - m| < 1 / 2 := by
    have hQr2 : (2 : ℝ) ≤ Q B := by exact_mod_cast hQ2
    exact hsmall.trans_le (one_div_le_one_div_of_le (by norm_num) hQr2)
  have hwindow : |(q : ℝ) * a - m| < L := hsmall.trans hQL
  have hD : 0 ≤ Real.sqrt B * Real.log B * (p : ℝ)^Q B := by
    have := (log_base_pos hB).le
    positivity
  have hbudget := exponent_budget hB hp
  by_cases hside : (q : ℝ) * a ≤ m
  · have hmpos : (0 : ℝ) < m := (mul_pos hqpos ha).trans_le hside
    have hm1 : 1 ≤ m := by exact_mod_cast hmpos
    refine ⟨q, m, by omega, hm1, sub_nonneg.mpr hside, ?_, ?_⟩
    · rw [abs_of_nonpos (sub_nonpos.mpr hside)] at hwindow
      linarith
    · have : (Q B : ℝ) ≤ (Q B : ℝ) *
          (1 + Real.sqrt B * Real.log B * (p : ℝ)^Q B) := by nlinarith
      exact hqr.trans (this.trans hbudget)
  · have hdiff : 0 < (q : ℝ) * a - m := by linarith
    have hdL : (q : ℝ) * a - m < L := by
      rwa [abs_of_pos hdiff] at hwindow
    obtain ⟨n, hn1, hnlo, hnhi, hnb⟩ := amplify hL0 hL1 hdiff hdL
    have hinv := inverse_error_bound hB hp hqQ (ne_of_gt hdiff) hhalf
    rw [abs_of_pos hdiff] at hinv
    refine ⟨n*q, n*m+1, Nat.mul_pos hn1 hq0, by omega, ?_, ?_, ?_⟩
    · push_cast
      nlinarith
    · push_cast
      nlinarith
    · have hn : (n : ℝ) ≤ 1 + Real.sqrt B * Real.log B * (p : ℝ)^Q B :=
        hnb.trans (by linarith)
      calc
        ((n*q : ℕ) : ℝ) = (n : ℝ) * q := by push_cast; rfl
        _ ≤ (1 + Real.sqrt B * Real.log B * (p : ℝ)^Q B) * Q B :=
          mul_le_mul hn hqr (by positivity) (by positivity)
        _ ≤ C B * (p : ℝ)^Q B := by nlinarith [hbudget]

/-- FD-174's quantitative recurrence with its original constants and endpoints. -/
theorem prime_power_hit {B p : ℕ} (hB : 3 ≤ B) (hp : Nat.Prime p)
    (_ho : p % 2 = 1) :
    ∃ j k : ℕ, 1 ≤ j ∧ 1 ≤ k ∧
      (B : ℝ)^k / 2 < (p : ℝ)^j ∧ (p : ℝ)^j ≤ (B : ℝ)^k ∧
      (j : ℝ) ≤ C B * (p : ℝ)^Q B ∧
      (k : ℝ) ≤ C B * (p : ℝ)^Q B * (Real.log p / Real.log B) + 1 := by
  obtain ⟨j, k, hj, hk, hlo, hhi, hjb⟩ := logarithmic_hit hB hp.two_le
  have hb := log_base_pos hB
  have hB0 : (0 : ℝ) < B := by exact_mod_cast (show 0 < B by omega)
  have hp0 : (0 : ℝ) < p := by exact_mod_cast hp.pos
  have ha : 0 < Real.log p / Real.log B := div_pos hp.log_pos hb
  have hid : ((k : ℝ) - (j : ℝ) * (Real.log p / Real.log B)) * Real.log B =
      (k : ℝ) * Real.log B - (j : ℝ) * Real.log p := by field_simp
  have hloglo : (j : ℝ) * Real.log p ≤ (k : ℝ) * Real.log B := by
    have := mul_nonneg hlo hb.le
    rw [hid] at this
    linarith
  have hloghi : (k : ℝ) * Real.log B - Real.log 2 < (j : ℝ) * Real.log p := by
    have := (lt_div_iff₀ hb).1 hhi
    rw [hid] at this
    linarith
  refine ⟨j, k, hj, hk, ?_, ?_, hjb, ?_⟩
  · apply (Real.log_lt_log_iff (by positivity) (pow_pos hp0 _)).mp
    rw [Real.log_div (by positivity) (by norm_num), Real.log_pow, Real.log_pow]
    exact hloghi
  · apply (Real.log_le_log_iff (pow_pos hp0 _) (pow_pos hB0 _)).mp
    simpa only [Real.log_pow] using hloglo
  · have hL1 := (window_bounds hB).2.1
    have hjba := mul_le_mul_of_nonneg_right hjb ha.le
    linarith

/-- The first K_B(X) horizons hit every odd prime through X. Natural half-cutoffs
agree exactly with the real open-left endpoint by FD-173. -/
theorem finite_scale_hit {B : ℕ} (hB : 3 ≤ B) {X : ℝ} (hX : 3 ≤ X)
    {p : ℕ} (hp : Nat.Prime p) (ho : p % 2 = 1) (hpX : (p : ℝ) ≤ X) :
    ∃ j k : ℕ, 1 ≤ j ∧ 1 ≤ k ∧ k ≤ K B X ∧
      B^k / 2 < p^j ∧ p^j ≤ B^k := by
  obtain ⟨j, k, hj, hk, hlo, hhi, _, hkb⟩ := prime_power_hit hB hp ho
  have hb := log_base_pos hB
  have hC : 0 ≤ C B := by unfold C; positivity
  have hp0 : (0 : ℝ) < p := by exact_mod_cast hp.pos
  have hlog : Real.log p / Real.log B ≤ Real.log X / Real.log B := by
    exact div_le_div_of_nonneg_right (Real.log_le_log hp0 hpX) hb.le
  have hmono : C B * (p : ℝ)^Q B * (Real.log p / Real.log B) ≤
      C B * X^Q B * (Real.log X / Real.log B) := by
    apply mul_le_mul
    · gcongr
    · exact hlog
    · exact (div_pos hp.log_pos hb).le
    · positivity
  have hceil := Nat.le_ceil (C B * X^Q B * (Real.log X / Real.log B))
  have hkK : (k : ℝ) ≤ (K B X : ℝ) := by
    simp only [K, Nat.cast_add, Nat.cast_one]
    linarith
  refine ⟨j, k, hj, hk, by exact_mod_cast hkK, ?_, by exact_mod_cast hhi⟩
  apply FD173.real_half_lt_iff.mp
  simpa only [Nat.cast_pow] using hlo

/-- Finite-scale prime-defect stability; the external midpoint bridge identifies
FD-173's observation with minus twice the Farey midpoint error. -/
theorem finite_scale_stability {B : ℕ} (hB : 3 ≤ B) {X : ℝ} (hX : 3 ≤ X)
    {δ : ℕ → ℝ} (hδ : FD173.Admissible δ) {ε : ℝ}
    (hobs : ∀ k : ℕ, 1 ≤ k → k ≤ K B X → FD173.observation δ (B^k) ≤ 2 * ε) :
    ∀ p : ℕ, Nat.Prime p → (p : ℝ) ≤ X → 0 ≤ δ p ∧ δ p ≤ 2 * ε := by
  intro p hp hpX
  refine ⟨hδ p hp, ?_⟩
  rcases hp.eq_two_or_odd with rfl | ho
  · have hK : 1 ≤ K B X := by unfold K; omega
    have hbound := hobs 1 (by omega) hK
    simpa using (FD173.two_defect_le_observation hδ (show 2 ≤ B by omega)).trans
      (by simpa using hbound)
  · obtain ⟨j, k, hj, hk, hkK, hlo, hhi⟩ := finite_scale_hit hB hX hp ho hpX
    exact (FD173.prime_defect_le_observation hδ hp ho hj hlo hhi).trans (hobs k hk hkK)

end Mathia.FD174
