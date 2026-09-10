import NB033TailQuotient
import Mathlib.NumberTheory.ArithmeticFunction.Moebius
import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.Analysis.PSeries
import Mathlib.Tactic

/-!
# NB-034 weighted shell kernel and finite coercivity

Associated finding:
`research/nyman_beurling/findings/NB-034-weighted-tail-shell-kernel-gives-uniform-source-conditioning.md`

Formalized theorem boundary: real finite shell observations `(t % n) / n`, their
divisor/Möbius inverse, the weighted-tail coefficient kernel and normal form, and
the energy lower bound `sum c_n^2 / (49 M^4)` for `M ≥ 2`. An abstract real
inner-product-space corollary transports the same coefficient normal form to
`I - P_W` for the weighted generator edges, reusing NB033.

The principal estimate is over `ℝ`. Its complex analogue follows by applying the
real estimate separately to real and imaginary parts and adding; that lift is
outside the principal theorem. The fractional-part generators in `L²(0,1)`, the
comparison with their full Hilbert Gram matrix, spectral condition numbers,
Burnol's bound, relative-distance asymptotics, Möbius locking, and RH-facing
consequences are not formalized here.
-/

noncomputable section

namespace Mathia.NB034

open Finset
open scoped BigOperators ArithmeticFunction Pointwise

def shell (t n : ℕ) : ℝ := (t % n : ℕ) / (n : ℝ)

def observe (M : ℕ) (c : ℕ → ℝ) (t : ℕ) : ℝ :=
  ∑ n ∈ Icc 2 M, c n * shell t n

def energy (M : ℕ) (c : ℕ → ℝ) : ℝ :=
  ∑ t ∈ Ico 1 M, observe M c t ^ 2 / ((t : ℝ) * (t + 1))

@[simp] theorem observe_zero (M : ℕ) (c : ℕ → ℝ) : observe M c 0 = 0 := by
  simp [observe, shell]

theorem shell_of_lt {t n : ℕ} (h : t < n) : shell t n = (t : ℝ) / n := by
  simp [shell, Nat.mod_eq_of_lt h]

theorem weighted_edge_vanishes {t n : ℕ} (h : t < n) :
    (n : ℝ) * shell t n - (n + 1 : ℝ) * shell t (n + 1) = 0 := by
  rw [shell_of_lt h, shell_of_lt (by omega)]
  have hn : (n : ℝ) ≠ 0 := by exact_mod_cast (by omega : n ≠ 0)
  push_cast
  field_simp
  ring

theorem shell_difference {t n : ℕ} (ht : 0 < t) (hn : 2 ≤ n) :
    shell t n - shell (t - 1) n = 1 / (n : ℝ) - if n ∣ t then 1 else 0 := by
  have hn0 : 0 < n := by omega
  have hnR : (n : ℝ) ≠ 0 := by positivity
  have hmod := Nat.mod_lt (t - 1) hn0
  have heq : t = (t - 1) + 1 := by omega
  have hadd : t % n = ((t - 1) % n + 1) % n := by
    conv_lhs => rw [heq, Nat.add_mod]
    rw [Nat.mod_eq_of_lt (by omega : 1 < n)]
  by_cases hd : n ∣ t
  · have hz := Nat.mod_eq_zero_of_dvd hd
    have hp : (t - 1) % n = n - 1 := by
      by_contra hh
      have hlt : (t - 1) % n + 1 < n := by omega
      rw [Nat.mod_eq_of_lt hlt] at hadd
      omega
    simp only [shell, hz, hp, ite_eq_left hd]
    rw [Nat.cast_sub (by omega : 1 ≤ n)]
    push_cast
    field_simp
    ring
  · have hlt : (t - 1) % n + 1 < n := by
      by_contra hh
      have he : (t - 1) % n + 1 = n := by omega
      rw [he, Nat.mod_self] at hadd
      exact hd (Nat.dvd_of_mod_eq_zero hadd)
    rw [Nat.mod_eq_of_lt hlt] at hadd
    simp only [shell, hadd, Nat.cast_add, Nat.cast_one, ite_eq_right hd, sub_zero]
    ring

theorem observe_one (M : ℕ) (c : ℕ → ℝ) :
    observe M c 1 = ∑ n ∈ Icc 2 M, c n / n := by
  apply sum_congr rfl
  intro n hn
  rw [shell_of_lt (by have := (mem_Icc.mp hn).1; omega)]
  simp [div_eq_mul_inv]

theorem observe_difference (M : ℕ) (c : ℕ → ℝ) {t : ℕ} (ht : 0 < t) :
    observe M c t - observe M c (t - 1) =
      observe M c 1 - ∑ n ∈ Icc 2 M, if n ∣ t then c n else 0 := by
  rw [observe_one]
  simp only [observe, ← sum_sub_distrib]
  apply sum_congr rfl
  intro n hn
  rw [← mul_sub, shell_difference ht (mem_Icc.mp hn).1]
  split_ifs <;> ring

/-- A single exceptional coordinate absorbs the constant in the first differences. -/
def divisorCoefficients (M : ℕ) (c : ℕ → ℝ) (n : ℕ) : ℝ :=
  (if n ∈ Icc 2 M then c n else 0) - if n = 1 then observe M c 1 else 0

theorem divisor_factorization (M : ℕ) (c : ℕ → ℝ) {t : ℕ} (ht : 0 < t) :
    (∑ n ∈ t.divisors, divisorCoefficients M c n) =
      -(observe M c t - observe M c (t - 1)) := by
  have hsum : (∑ n ∈ t.divisors, if n ∈ Icc 2 M then c n else 0) =
      ∑ n ∈ Icc 2 M, if n ∣ t then c n else 0 := by
    rw [← sum_filter, ← sum_filter]
    congr 1
    ext n
    simp only [mem_filter, Nat.mem_divisors, ne_eq, ht.ne', not_false_eq_true, and_true]
    tauto
  simp only [divisorCoefficients, sum_sub_distrib]
  rw [hsum, sum_ite_eq', ite_eq_left (Nat.one_mem_divisors.mpr ht.ne'), observe_difference M c ht]
  ring

/-- Exact inverse, with the `d = 1` term retained and `v 0 = 0`.
At `n = M` this identity uses the additional observation `v M`; reconstruction
from only the early shells instead uses `final_coordinate` for that endpoint. -/
theorem moebius_reconstruction (M : ℕ) (c : ℕ → ℝ) {n : ℕ} (hn : n ∈ Icc 2 M) :
    c n = -(∑ d ∈ n.divisors, (ArithmeticFunction.moebius (n / d) : ℝ) *
      (observe M c d - observe M c (d - 1))) := by
  have hi := (ArithmeticFunction.sum_eq_iff_sum_mul_moebius_eq
    (f := divisorCoefficients M c)
    (g := fun t => -(observe M c t - observe M c (t - 1)))).mp
      (fun t ht => divisor_factorization M c ht) n (by have := (mem_Icc.mp hn).1; omega)
  rw [Nat.sum_divisorsAntidiagonal' (fun x y => (ArithmeticFunction.moebius x : ℝ) *
    -(observe M c y - observe M c (y - 1)))] at hi
  have hn1 : n ≠ 1 := by have := (mem_Icc.mp hn).1; omega
  simp only [divisorCoefficients, hn, hn1, ite_true, ite_false, sub_zero,
    mul_neg, sum_neg_distrib] at hi
  exact hi.symm

theorem final_coordinate {M : ℕ} (hM : 2 ≤ M) (c : ℕ → ℝ) :
    c M = (M : ℝ) * (observe M c 1 - ∑ n ∈ Ico 2 M, c n / n) := by
  rw [observe_one, ← sum_Ico_add_eq_sum_Icc hM]
  have hMR : (M : ℝ) ≠ 0 := by positivity
  field_simp
  ring

def sigma (n : ℕ) : ℝ := ∑ d ∈ n.divisors, (d : ℝ)

theorem sigma_nonneg (n : ℕ) : 0 ≤ sigma n := by
  exact sum_nonneg (fun _ _ => Nat.cast_nonneg _)

set_option backward.isDefEq.respectTransparency false in
theorem sum_sigma_le (x : ℕ) : (∑ n ∈ Ioc 0 x, sigma n) ≤ (x : ℝ) ^ 2 := by
  have hi := ArithmeticFunction.sum_Ioc_mul_zeta_eq_sum
    (⟨fun n => (n : ℝ), by simp⟩ : ArithmeticFunction ℝ) x
  simp only [ArithmeticFunction.coe_mul_zeta_apply, ArithmeticFunction.coe_mk] at hi
  change (∑ n ∈ Ioc 0 x, ∑ d ∈ n.divisors, (d : ℝ)) ≤ _
  rw [hi]
  calc
    (∑ n ∈ Ioc 0 x, (n : ℝ) * (x / n : ℕ)) ≤ ∑ _n ∈ Ioc 0 x, (x : ℝ) := by
      apply sum_le_sum
      intro n _
      exact_mod_cast Nat.mul_div_le x n
    _ = (x : ℝ) ^ 2 := by simp; ring

theorem sigma_div_eq (n : ℕ) : sigma n / n = ∑ d ∈ n.divisors, (d : ℝ)⁻¹ := by
  by_cases hn : n = 0
  · simp [hn, sigma]
  rw [← Nat.sum_div_divisors n (fun d => (d : ℝ)⁻¹)]
  simp only [sigma, sum_div]
  apply sum_congr rfl
  intro d hd
  rw [Nat.cast_div_charZero (Nat.dvd_of_mem_divisors hd)]
  simp [inv_div]

set_option backward.isDefEq.respectTransparency false in
theorem sum_sigma_div_le (x : ℕ) :
    (∑ n ∈ Ioc 0 x, sigma n / n) ≤ 2 * (x : ℝ) := by
  have hi := ArithmeticFunction.sum_Ioc_mul_zeta_eq_sum
    (⟨fun n => (n : ℝ)⁻¹, by simp⟩ : ArithmeticFunction ℝ) x
  simp only [ArithmeticFunction.coe_mul_zeta_apply, ArithmeticFunction.coe_mk] at hi
  simp_rw [sigma_div_eq]
  rw [hi]
  calc
    (∑ n ∈ Ioc 0 x, (n : ℝ)⁻¹ * (x / n : ℕ)) ≤
        ∑ n ∈ Ioc 0 x, (x : ℝ) * ((n : ℝ) ^ 2)⁻¹ := by
      apply sum_le_sum
      intro n hn
      calc
        (n : ℝ)⁻¹ * (x / n : ℕ) ≤ (n : ℝ)⁻¹ * ((x : ℝ) / n) :=
          mul_le_mul_of_nonneg_left Nat.cast_div_le (by positivity)
        _ = (x : ℝ) * ((n : ℝ) ^ 2)⁻¹ := by ring
    _ = (x : ℝ) * ∑ n ∈ Ioo 0 (x + 1), ((n : ℝ) ^ 2)⁻¹ := by
      rw [← mul_sum]
      congr 2
    _ ≤ 2 * (x : ℝ) := by
      have hb := sum_Ioo_inv_sq_le (α := ℝ) 0 (x + 1)
      norm_num at hb
      nlinarith [mul_le_mul_of_nonneg_left hb (Nat.cast_nonneg (α := ℝ) x)]

theorem energy_nonneg (M : ℕ) (c : ℕ → ℝ) : 0 ≤ energy M c := by
  exact sum_nonneg (fun t _ => by positivity)

theorem observe_sq_le {M t : ℕ} (c : ℕ → ℝ) (ht : t < M) :
    observe M c t ^ 2 ≤ energy M c * ((t : ℝ) * (t + 1)) := by
  by_cases hz : t = 0
  · simp [hz]
  have hpos : 0 < (t : ℝ) * (t + 1) := by
    have : 0 < t := Nat.pos_of_ne_zero hz
    positivity
  have hi : observe M c t ^ 2 / ((t : ℝ) * (t + 1)) ≤ energy M c := by
    apply single_le_sum (f := fun i : ℕ => observe M c i ^ 2 / ((i : ℝ) * (i + 1)))
    · intro i _; positivity
    · exact mem_Ico.mpr ⟨by omega, ht⟩
  exact (div_le_iff₀ hpos).mp hi

theorem difference_bound {M d : ℕ} (c : ℕ → ℝ) (hd : 0 < d) (hdM : d < M)
    {δ : ℝ} (hδ : 0 ≤ δ) (he : energy M c ≤ δ ^ 2) :
    |observe M c d - observe M c (d - 1)| ≤ 2 * δ * d := by
  have h₁ := (observe_sq_le c hdM).trans
    (mul_le_mul_of_nonneg_right he (by positivity))
  have h₂ := (observe_sq_le c (show d - 1 < M by omega)).trans
    (mul_le_mul_of_nonneg_right he (by positivity))
  have hc : ((d - 1 : ℕ) : ℝ) = (d : ℝ) - 1 := by
    rw [Nat.cast_sub (by omega : 1 ≤ d), Nat.cast_one]
  rw [hc] at h₂
  have hab := sq_abs (observe M c d - observe M c (d - 1))
  have hR : 0 ≤ 2 * δ * (d : ℝ) := by positivity
  nlinarith [sq_nonneg (observe M c d + observe M c (d - 1))]

theorem coefficient_bound {M n : ℕ} (c : ℕ → ℝ) (hn : n ∈ Ico 2 M)
    {δ : ℝ} (hδ : 0 ≤ δ) (he : energy M c ≤ δ ^ 2) :
    |c n| ≤ 2 * δ * sigma n := by
  rw [moebius_reconstruction M c (mem_Icc.mpr ⟨(mem_Ico.mp hn).1, (mem_Ico.mp hn).2.le⟩),
    abs_neg]
  calc
    |∑ d ∈ n.divisors, (ArithmeticFunction.moebius (n / d) : ℝ) *
        (observe M c d - observe M c (d - 1))| ≤
        ∑ d ∈ n.divisors, |(ArithmeticFunction.moebius (n / d) : ℝ) *
          (observe M c d - observe M c (d - 1))| := abs_sum_le_sum_abs _ _
    _ ≤ ∑ d ∈ n.divisors, 2 * δ * d := by
      apply sum_le_sum
      intro d hd
      rw [abs_mul]
      have hμ : |(ArithmeticFunction.moebius (n / d) : ℝ)| ≤ 1 := by
        exact_mod_cast (ArithmeticFunction.abs_moebius_le_one (n := n / d))
      have hdM : d < M := lt_of_le_of_lt
        (Nat.le_of_dvd (by have := (mem_Ico.mp hn).1; omega) (Nat.dvd_of_mem_divisors hd))
        (mem_Ico.mp hn).2
      exact (mul_le_mul_of_nonneg_right hμ (abs_nonneg _)).trans
        (by simpa using difference_bound c (Nat.pos_of_mem_divisors hd) hdM hδ he)
    _ = 2 * δ * sigma n := by simp [sigma, mul_sum]

theorem coefficient_l1_bound {M : ℕ} (hM : 2 ≤ M) (c : ℕ → ℝ)
    {δ : ℝ} (hδ : 0 ≤ δ) (he : energy M c ≤ δ ^ 2) :
    (∑ n ∈ Icc 2 M, |c n|) ≤ 7 * (M : ℝ) ^ 2 * δ := by
  have hs : Ico 2 M ⊆ Ioc 0 M := by intro n hn; simp only [mem_Ico, mem_Ioc] at *; omega
  have hhead : (∑ n ∈ Ico 2 M, |c n|) ≤ 2 * δ * (M : ℝ) ^ 2 := by
    calc
      _ ≤ ∑ n ∈ Ico 2 M, 2 * δ * sigma n :=
        sum_le_sum (fun n hn => coefficient_bound c hn hδ he)
      _ = 2 * δ * ∑ n ∈ Ico 2 M, sigma n := by rw [mul_sum]
      _ ≤ 2 * δ * (M : ℝ) ^ 2 := by
        apply mul_le_mul_of_nonneg_left _ (by positivity)
        exact (sum_le_sum_of_subset_of_nonneg hs (fun n _ _ => sigma_nonneg n)).trans
          (sum_sigma_le M)
  have hweighted : (∑ n ∈ Ico 2 M, |c n| / n) ≤ 4 * δ * M := by
    calc
      _ ≤ ∑ n ∈ Ico 2 M, (2 * δ * sigma n) / n := by
        apply sum_le_sum
        intro n hn
        exact div_le_div_of_nonneg_right (coefficient_bound c hn hδ he) (by positivity)
      _ = 2 * δ * ∑ n ∈ Ico 2 M, sigma n / n := by simp [mul_sum, mul_div_assoc]
      _ ≤ 2 * δ * (2 * M) := by
        apply mul_le_mul_of_nonneg_left _ (by positivity)
        exact (sum_le_sum_of_subset_of_nonneg hs (fun n _ _ =>
          div_nonneg (sigma_nonneg n) (by positivity))).trans (sum_sigma_div_le M)
      _ = 4 * δ * M := by ring
  have hv : |observe M c 1| ≤ 2 * δ := by
    simpa using difference_bound c (by omega : 0 < 1) (by omega : 1 < M) hδ he
  have hlast : |c M| ≤ 5 * (M : ℝ) ^ 2 * δ := by
    rw [final_coordinate hM c, abs_mul, abs_of_nonneg (Nat.cast_nonneg M)]
    have hsum : |∑ n ∈ Ico 2 M, c n / n| ≤ ∑ n ∈ Ico 2 M, |c n| / n := by
      simpa only [abs_div, Nat.abs_cast] using
        (abs_sum_le_sum_abs (fun n => c n / (n : ℝ)) (Ico 2 M))
    have hi := (abs_sub (observe M c 1) (∑ n ∈ Ico 2 M, c n / n)).trans
      (add_le_add hv (hsum.trans hweighted))
    have hi' := mul_le_mul_of_nonneg_left hi (Nat.cast_nonneg (α := ℝ) M)
    have hMR : 2 ≤ (M : ℝ) := by exact_mod_cast hM
    nlinarith [mul_nonneg hδ (show 0 ≤ (M : ℝ) * (M - 2) by positivity)]
  rw [← sum_Ico_add_eq_sum_Icc hM]
  linarith

/-- NB-034 (8), expressed as an unconditional finite quadratic-energy estimate. -/
theorem coercive_energy {M : ℕ} (hM : 2 ≤ M) (c : ℕ → ℝ) :
    (∑ n ∈ Icc 2 M, c n ^ 2) / (49 * (M : ℝ) ^ 4) ≤ energy M c := by
  have he := energy_nonneg M c
  have hs := Real.sq_sqrt he
  have hb := coefficient_l1_bound hM c (Real.sqrt_nonneg (energy M c)) hs.ge
  have hl : 0 ≤ ∑ n ∈ Icc 2 M, |c n| := sum_nonneg (fun _ _ => abs_nonneg _)
  have hsq := sum_sq_le_sq_sum_of_nonneg (s := Icc 2 M) (fun n _ => abs_nonneg (c n))
  simp only [sq_abs] at hsq
  have hh := mul_self_le_mul_self hl hb
  have hden : 0 < 49 * (M : ℝ) ^ 4 := by
    have : 0 < M := by omega
    positivity
  apply (div_le_iff₀ hden).mpr
  nlinarith [hsq, hh]

/-- Vanishing observations determine every coefficient in the finite head interval. -/
theorem head_injective {M : ℕ} (hM : 2 ≤ M) (c : ℕ → ℝ)
    (hc : ∀ t ∈ Ico 1 M, observe M c t = 0) : ∀ n ∈ Icc 2 M, c n = 0 := by
  have he : energy M c = 0 := by
    apply sum_eq_zero
    intro t ht
    rw [hc t ht]
    simp
  have hb := coefficient_l1_bound hM c (δ := 0) le_rfl (by simp [he])
  simp only [mul_zero] at hb
  intro n hn
  have hi : |c n| ≤ ∑ n ∈ Icc 2 M, |c n| :=
    single_le_sum (f := fun n => |c n|) (fun _ _ => abs_nonneg _) hn
  exact abs_nonpos_iff.mp (hi.trans hb)

/-! ## Weighted coefficient quotient

Use NB033's finite indices with `M = h + 2` and `N = h + t + 2`.
The head index `i` denotes `i+2`, and the tail index `j` denotes `M+j`.
Thus `h=0` and `t=0` cover `M=2` and `M=N` without extra assumptions.
-/

open NB033 Submodule

def sourceIndex (h t : ℕ) : Index h t → ℕ :=
  Sum.elim (fun i => i.val + 2) (fun j => h + 2 + j.val)

/-- Original source coefficients to the ordinary NB033 path coordinates. -/
def diagonal (h t : ℕ) : Coeff ℝ h t ≃ₗ[ℝ] Coeff ℝ h t where
  toFun a := Sum.elim (fun i => a (.inl i))
    (fun j => (h + 2 : ℝ) * a (.inr j) / (h + 2 + j.val : ℝ))
  invFun a := Sum.elim (fun i => a (.inl i))
    (fun j => (h + 2 + j.val : ℝ) * a (.inr j) / (h + 2 : ℝ))
  left_inv a := by
    ext i
    cases i with
    | inl i => rfl
    | inr j => dsimp; field_simp
  right_inv a := by
    ext i
    cases i with
    | inl i => rfl
    | inr j => dsimp; field_simp
  map_add' a b := by
    ext i
    cases i with
    | inl i => rfl
    | inr j => dsimp; ring
  map_smul' r a := by
    ext i
    cases i with
    | inl i => rfl
    | inr j => dsimp; ring

def weightedCollapse (h t : ℕ) : Coeff ℝ h t →ₗ[ℝ] Reduced ℝ h :=
  (collapse ℝ h t).comp (diagonal h t).toLinearMap

theorem weightedCollapse_apply (h t : ℕ) (a : Coeff ℝ h t) :
    weightedCollapse h t a =
      (fun i => a (.inl i), (h + 2 : ℝ) * ∑ j, a (.inr j) / (h + 2 + j.val : ℝ)) := by
  ext <;> simp [weightedCollapse, collapse, diagonal, mul_sum, mul_div_assoc]

def weightedEdge (h t : ℕ) (j : Fin t) : Coeff ℝ h t :=
  (h + 2 + j.val : ℝ) • Pi.single (.inr j.castSucc) 1 -
    (h + 2 + (j.val + 1) : ℝ) • Pi.single (.inr j.succ) 1

def weightedSpace (h t : ℕ) : Submodule ℝ (Coeff ℝ h t) :=
  span ℝ (Set.range (weightedEdge h t))

theorem diagonal_edge (h t : ℕ) (j : Fin t) :
    diagonal h t (weightedEdge h t j) = (h + 2 : ℝ) • edge ℝ h t j := by
  have hj : j.succ ≠ j.castSucc := by
    intro he
    have he' : j.val + 1 = j.val := congrArg Fin.val he
    omega
  ext i
  cases i with
  | inl i => simp [diagonal, weightedEdge, edge, Pi.single_apply]
  | inr i =>
    simp only [diagonal, weightedEdge, edge, LinearEquiv.coe_mk,
      Pi.sub_apply, Pi.smul_apply, smul_eq_mul, Pi.single_apply]
    split_ifs <;> simp_all <;> field_simp
    ring

theorem weightedSpace_eq_ker (h t : ℕ) : weightedSpace h t = (weightedCollapse h t).ker := by
  have hne : (h + 2 : ℝ) ≠ 0 := by positivity
  have hmap : (weightedSpace h t).map (diagonal h t).toLinearMap = tailSpace ℝ h t := by
    simp only [weightedSpace, map_span, ← Set.range_comp, Function.comp_def,
      LinearEquiv.coe_coe, diagonal_edge]
    rw [show Set.range (fun j : Fin t => (h + 2 : ℝ) • edge ℝ h t j) =
      (h + 2 : ℝ) • Set.range (edge ℝ h t) by
        ext x; simp only [Set.mem_range, Set.mem_smul_set]; aesop]
    exact span_smul_eq_of_isUnit _ _ (isUnit_iff_ne_zero.mpr hne)
  rw [weightedCollapse, LinearMap.ker_comp, ← tailSpace_eq_ker, ← hmap]
  exact (comap_map_eq_of_injective (diagonal h t).injective _).symm

theorem weightedCollapse_surjective (h t : ℕ) : Function.Surjective (weightedCollapse h t) :=
  (collapse_surjective ℝ h t).comp (diagonal h t).surjective

/-- The weighted quotient, in original source coordinates, keeps the harmonic tail scalar. -/
def weightedQuotientEquiv (h t : ℕ) :
    (Coeff ℝ h t ⧸ weightedSpace h t) ≃ₗ[ℝ] Reduced ℝ h :=
  (Submodule.quotEquivOfEq _ _ (weightedSpace_eq_ker h t)).trans
    ((weightedCollapse h t).quotKerEquivOfSurjective (weightedCollapse_surjective h t))

@[simp] theorem weightedQuotientEquiv_mk (h t : ℕ) (a : Coeff ℝ h t) :
    weightedQuotientEquiv h t (Submodule.Quotient.mk a) = weightedCollapse h t a := by
  simp [weightedQuotientEquiv]

def earlyObservation (h t : ℕ) : Coeff ℝ h t →ₗ[ℝ] (Fin (h + 1) → ℝ) where
  toFun a k := ∑ i, a i * shell (k.val + 1) (sourceIndex h t i)
  map_add' a b := by ext; simp [add_mul, sum_add_distrib]
  map_smul' r a := by ext; simp [mul_assoc, mul_sum, mul_add]

def reducedObservation (h : ℕ) : Reduced ℝ h →ₗ[ℝ] (Fin (h + 1) → ℝ) where
  toFun b k := (∑ i : Fin h, b.1 i * shell (k.val + 1) (i.val + 2)) +
    b.2 * shell (k.val + 1) (h + 2)
  map_add' a b := by ext; simp [add_mul, sum_add_distrib]; ring
  map_smul' r a := by ext; simp [mul_assoc, mul_sum, mul_add]

theorem observation_factorization (h t : ℕ) :
    earlyObservation h t = (reducedObservation h).comp (weightedCollapse h t) := by
  ext a k
  simp only [earlyObservation, LinearMap.coe_mk, AddHom.coe_mk, Fintype.sum_sum_type,
    sourceIndex, Sum.elim_inl, Sum.elim_inr, LinearMap.comp_apply,
    reducedObservation, weightedCollapse_apply]
  congr 1
  rw [shell_of_lt (by omega : k.val + 1 < h + 2), mul_sum, sum_mul]
  apply sum_congr rfl
  intro j _
  rw [shell_of_lt (by omega : k.val + 1 < h + 2 + j.val)]
  push_cast
  field_simp

private theorem sum_head_range (h : ℕ) (f : ℕ → ℝ) :
    (∑ n ∈ Ico 2 (h + 2), f n) = ∑ i : Fin h, f (i.val + 2) := by
  apply sum_bij (fun n hn => (⟨n - 2, by have := mem_Ico.mp hn; omega⟩ : Fin h))
  · intro n hn; simp
  · intro n hn m hm he
    have he' : n - 2 = m - 2 := congrArg Fin.val he
    have := mem_Ico.mp hn
    have := mem_Ico.mp hm
    omega
  · intro i _
    exact ⟨i.val + 2, mem_Ico.mpr ⟨by omega, by omega⟩, by ext; simp⟩
  · intro n hn
    have := mem_Ico.mp hn
    congr 1
    simp only
    omega

def reducedCoefficients (h : ℕ) (b : Reduced ℝ h) (n : ℕ) : ℝ :=
  if hn : n ∈ Ico 2 (h + 2) then b.1 ⟨n - 2, by have := mem_Ico.mp hn; omega⟩
  else if n = h + 2 then b.2 else 0

@[simp] theorem reducedCoefficients_head (h : ℕ) (b : Reduced ℝ h) (i : Fin h) :
    reducedCoefficients h b (i.val + 2) = b.1 i := by
  simp [reducedCoefficients, show i.val + 2 ∈ Ico 2 (h + 2) from
    mem_Ico.mpr ⟨by omega, by omega⟩]

@[simp] theorem reducedCoefficients_last (h : ℕ) (b : Reduced ℝ h) :
    reducedCoefficients h b (h + 2) = b.2 := by simp [reducedCoefficients]

theorem observe_reduced (h : ℕ) (b : Reduced ℝ h) (k : Fin (h + 1)) :
    observe (h + 2) (reducedCoefficients h b) (k.val + 1) = reducedObservation h b k := by
  rw [observe, ← sum_Ico_add_eq_sum_Icc (by omega : 2 ≤ h + 2), sum_head_range]
  simp [reducedObservation]

theorem reducedObservation_injective (h : ℕ) : Function.Injective (reducedObservation h) := by
  apply (injective_iff_map_eq_zero _).mpr
  intro b hb
  have hc : ∀ n ∈ Icc 2 (h + 2), reducedCoefficients h b n = 0 := by
    apply head_injective (by omega : 2 ≤ h + 2)
    intro k hk
    let i : Fin (h + 1) := ⟨k - 1, by have := mem_Ico.mp hk; omega⟩
    have hi : i.val + 1 = k := by have := mem_Ico.mp hk; dsimp [i]; omega
    rw [← hi, observe_reduced]
    exact congrFun hb i
  apply Prod.ext
  · ext i
    simpa using hc (i.val + 2) (mem_Icc.mpr ⟨by omega, by omega⟩)
  · simpa using hc (h + 2) (mem_Icc.mpr ⟨by omega, le_rfl⟩)

/-- The source-defined weighted path span is exactly early-shell invisibility. -/
theorem earlyObservation_ker (h t : ℕ) : (earlyObservation h t).ker = weightedSpace h t := by
  rw [observation_factorization, LinearMap.ker_comp,
    LinearMap.ker_eq_bot.mpr (reducedObservation_injective h), Submodule.comap_bot,
    ← weightedSpace_eq_ker]

theorem finrank_weightedSpace (h t : ℕ) : Module.finrank ℝ (weightedSpace h t) = t := by
  have hr := (weightedCollapse h t).finrank_range_add_finrank_ker
  rw [LinearMap.range_eq_top.mpr (weightedCollapse_surjective h t),
    ← weightedSpace_eq_ker] at hr
  simp [Reduced, Coeff, Index, Module.finrank_prod] at hr
  have hr' : h + 1 + Module.finrank ℝ (weightedSpace h t) = h + (t + 1) := hr
  omega

theorem finrank_weightedQuotient (h t : ℕ) :
    Module.finrank ℝ (Coeff ℝ h t ⧸ weightedSpace h t) = h + 1 := by
  simpa [Reduced] using (weightedQuotientEquiv h t).finrank_eq

theorem energy_two (c : ℕ → ℝ) : energy 2 c = c 2 ^ 2 / 8 := by
  norm_num [energy, observe, shell, Finset.sum_Ico_succ_top]
  ring

theorem weightedCollapse_singleton_tail (h : ℕ) (a : Coeff ℝ h 0) :
    weightedCollapse h 0 a = (fun i => a (.inl i), a (.inr 0)) := by
  rw [weightedCollapse_apply]
  ext <;> simp
  field_simp

section OrthogonalCorollary

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

def weightedGenerators {h t : ℕ} (g : Index h t → E) : Index h t → E :=
  Sum.elim (fun i => g (.inl i)) (fun j => (h + 2 + j.val : ℝ) • g (.inr j))

/-- This nuisance subspace has the actual weighted source-generator edges. -/
theorem weighted_generator_edge {h t : ℕ} (g : Index h t → E) (j : Fin t) :
    generatorEdge (weightedGenerators g) j =
      (h + 2 + j.val : ℝ) • g (.inr j.castSucc) -
      (h + 2 + (j.val + 1) : ℝ) • g (.inr j.succ) := by
  simp [generatorEdge, weightedGenerators]

/-- Abstract orthogonal realization of NB-034 (5). No independence hypothesis is
needed for this pushforward identity; canonical `L²` generators remain outside Lean. -/
theorem weighted_projection_pushforward {h t : ℕ} (g : Index h t → E) (a : Coeff ℝ h t) :
    quotientProjection ℝ (weightedGenerators g) (∑ i, a i • g i) =
      (∑ i : Fin h, a (.inl i) • quotientProjection ℝ (weightedGenerators g) (g (.inl i))) +
      ((h + 2 : ℝ) * ∑ j : Fin (t + 1), a (.inr j) / (h + 2 + j.val : ℝ)) •
        quotientProjection ℝ (weightedGenerators g) (g (.inr 0)) := by
  let b : Coeff ℝ h t := Sum.elim (fun i => a (.inl i))
    (fun j => a (.inr j) / (h + 2 + j.val : ℝ))
  have hsyn : (∑ i, b i • weightedGenerators g i) = ∑ i, a i • g i := by
    apply sum_congr rfl
    intro i _
    cases i with
    | inl i => rfl
    | inr j =>
      dsimp [b, weightedGenerators]
      rw [smul_smul, div_mul_cancel₀ _ (by positivity)]
  have hp := coefficient_pushforward ℝ (weightedGenerators g) b
  rw [hsyn] at hp
  simpa only [b, weightedGenerators, Sum.elim_inl, Sum.elim_inr,
    Fin.val_zero, Nat.cast_zero, add_zero, map_smul, smul_smul, mul_comm] using hp

end OrthogonalCorollary

end Mathia.NB034

#print axioms Mathia.NB034.shell_difference
#print axioms Mathia.NB034.divisor_factorization
#print axioms Mathia.NB034.moebius_reconstruction
#print axioms Mathia.NB034.final_coordinate
#print axioms Mathia.NB034.coefficient_l1_bound
#print axioms Mathia.NB034.coercive_energy
#print axioms Mathia.NB034.head_injective
#print axioms Mathia.NB034.weighted_edge_vanishes
#print axioms Mathia.NB034.weightedSpace_eq_ker
#print axioms Mathia.NB034.weightedQuotientEquiv_mk
#print axioms Mathia.NB034.weightedCollapse_apply
#print axioms Mathia.NB034.observation_factorization
#print axioms Mathia.NB034.earlyObservation_ker
#print axioms Mathia.NB034.finrank_weightedSpace
#print axioms Mathia.NB034.finrank_weightedQuotient
#print axioms Mathia.NB034.energy_two
#print axioms Mathia.NB034.weightedCollapse_singleton_tail
#print axioms Mathia.NB034.weighted_projection_pushforward
