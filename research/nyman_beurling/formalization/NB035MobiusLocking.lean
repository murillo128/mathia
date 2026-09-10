import NB034WeightedShell

/-!
# NB-035 uniform reciprocal-Möbius tail locking

Associated finding:
`research/nyman_beurling/findings/NB-035-weighted-tail-scalar-is-uniformly-mobius-locked.md`

Formalized theorem boundary: for arbitrary real source coefficients and
`2 ≤ M ≤ N`, the harmonic tail `sum_{n=M}^N a_n/n` differs from
`sum_{k=1}^{M-1} μ(k)/k` by a quantity whose square is at most 22 times the
first `M-1` residual shell energy. In particular, the requested constant 49
holds uniformly in both cutoffs. The shell observations, divisor inverse,
and source normalization reuse NB034.

The proof exposes the exact endpoint functional, its summation-by-parts row,
and a uniform weighted dual norm. A direct floor-block estimate and injection
of the first integers of nonempty blocks give a squared block bound of 8,
without a square-root cutoff split. Only the elementary Möbius divisor identity,
absolute bounds, and finite reciprocal-square estimates enter the proof.

Not formalized: the L²(0,1) realization and comparison with the full residual
norm, best-approximant normal equations, the PNT limit, growing-cutoff asymptotics,
or RH-facing closure and distance bounds. The auxiliary residual equals zero
at index zero; the canonical residual convention r(0)=1 is not used there.
The uniformly controlled coordinate is the normalized tail tau/M, not tau.
-/

noncomputable section
namespace Mathia.NB035
open Finset
open scoped BigOperators ArithmeticFunction

/-! ## Definitions -/

def reciprocalMobius (L : ℕ) : ℝ :=
  ∑ k ∈ Ioc 0 L, (ArithmeticFunction.moebius k : ℝ) / k

def endpointWeight (L d : ℕ) : ℝ := reciprocalMobius (L / d) / d

def endpointFunctional (L : ℕ) (u : ℕ → ℝ) : ℝ :=
  ∑ d ∈ Ioc 0 L, endpointWeight L d * (u d - u (d - 1))

def residualEnergy (L : ℕ) (u : ℕ → ℝ) : ℝ :=
  ∑ t ∈ Ioc 0 L, u t ^ 2 / ((t : ℝ) * (t + 1))

/-! ## Disjoint quotient blocks -/

/-- Each nonempty quotient block contributes its first positive integer only once. -/
theorem quotient_block_first_injective (L : ℕ) :
    Set.InjOn (fun t => L / (t + 1) + 1)
      ((Ico 1 L).filter (fun t => L / (t + 1) < L / t) : Set ℕ) := by
  intro t ht s hs heq
  change L / (t + 1) + 1 = L / (s + 1) + 1 at heq
  have ht' := mem_filter.mp ht
  have hs' := mem_filter.mp hs
  have horder : ∀ i j : ℕ, 0 < i → i < j → L / (j + 1) < L / j →
      L / (j + 1) + 1 < L / (i + 1) + 1 := by
    intro i j hi hij hj
    have hdiv := Nat.div_le_div_left (a := L) (by omega : i + 1 ≤ j) (by omega : 0 < i + 1)
    omega
  rcases lt_trichotomy t s with h | h | h
  · have := horder t s (by have := (mem_Ico.mp ht'.1).1; omega) h hs'.2
    omega
  · exact h
  · have := horder s t (by have := (mem_Ico.mp hs'.1).1; omega) h ht'.2
    omega

theorem quotient_block_first_square_sum_le (L : ℕ) :
    (∑ t ∈ (Ico 1 L).filter (fun t => L / (t + 1) < L / t),
      (((L / (t + 1) + 1 : ℕ) : ℝ) ^ 2)⁻¹) ≤ 2 := by
  let s := (Ico 1 L).filter (fun t => L / (t + 1) < L / t)
  have hsub : s.image (fun t => L / (t + 1) + 1) ⊆ Ioc 0 L := by
    intro k hk
    obtain ⟨t, ht, rfl⟩ := mem_image.mp hk
    have ht' := mem_filter.mp ht
    have hdiv := Nat.div_le_self L t
    exact mem_Ioc.mpr ⟨Nat.zero_lt_succ _, (Nat.succ_le_of_lt ht'.2).trans hdiv⟩
  calc
    _ = ∑ k ∈ s.image (fun t => L / (t + 1) + 1), ((k : ℝ) ^ 2)⁻¹ := by
      rw [sum_image]
      exact quotient_block_first_injective L
    _ ≤ ∑ k ∈ Ioc 0 L, ((k : ℝ) ^ 2)⁻¹ :=
      sum_le_sum_of_subset_of_nonneg hsub (fun _ _ _ => by positivity)
    _ ≤ 2 := by
      have h := sum_Ioo_inv_sq_le (α := ℝ) 0 (L + 1)
      simpa [show Ioo 0 (L + 1) = Ioc 0 L by ext; simp] using h

/-! ## Elementary reciprocal-Möbius and block estimates -/

lemma moebius_real_abs_le_one (k : ℕ) :
    |(ArithmeticFunction.moebius k : ℝ)| ≤ 1 := by
  exact_mod_cast (ArithmeticFunction.abs_moebius_le_one (n := k))

lemma moebius_floor_sum {Q : ℕ} (hQ : 0 < Q) :
    (∑ k ∈ Ioc 0 Q, (ArithmeticFunction.moebius k : ℝ) * (Q / k : ℕ)) = 1 := by
  have hi := ArithmeticFunction.sum_Ioc_mul_zeta_eq_sum
    (ArithmeticFunction.moebius : ArithmeticFunction ℝ) Q
  rw [ArithmeticFunction.coe_moebius_mul_coe_zeta] at hi
  simpa [ArithmeticFunction.one_apply, show 1 ≤ Q by omega] using hi.symm

lemma reciprocalMobius_abs_le_one (Q : ℕ) : |reciprocalMobius Q| ≤ 1 := by
  by_cases hQ : Q = 0
  · simp [hQ, reciprocalMobius]
  have hQpos : 0 < Q := Nat.pos_of_ne_zero hQ
  have hQR : (0 : ℝ) < Q := by positivity
  let f : ℕ → ℝ := fun k => (ArithmeticFunction.moebius k : ℝ) *
    ((Q : ℝ) / k - (Q / k : ℕ))
  have hid : (Q : ℝ) * reciprocalMobius Q = 1 + ∑ k ∈ Ioc 0 Q, f k := by
    have hf := moebius_floor_sum hQpos
    dsimp [reciprocalMobius, f]
    simp only [mul_sub, sum_sub_distrib, mul_sum]
    rw [hf]
    have hs : (∑ k ∈ Ioc 0 Q, (Q : ℝ) * ((ArithmeticFunction.moebius k : ℝ) / k)) =
        ∑ k ∈ Ioc 0 Q, (ArithmeticFunction.moebius k : ℝ) * ((Q : ℝ) / k) := by
      apply sum_congr rfl
      intro k _
      ring
    linarith
  have hf1 : f 1 = 0 := by simp [f]
  have hfbound : ∀ k ∈ (Ioc 0 Q).erase 1, |f k| ≤ 1 := by
    intro k hk
    have hkpos : 0 < k := (mem_Ioc.mp (mem_of_mem_erase hk)).1
    have hkR : (0 : ℝ) < k := by positivity
    have hb : (Q : ℝ) / k - (Q / k : ℕ) ≤ 1 := by
      have h := Nat.lt_mul_div_succ Q hkpos
      have h' : (Q : ℝ) < (k : ℝ) * ((Q / k : ℕ) + 1) := by exact_mod_cast h
      have hd : (Q : ℝ) / k < (Q / k : ℕ) + 1 :=
        (div_lt_iff₀ hkR).mpr (by nlinarith)
      linarith
    have ha : 0 ≤ (Q : ℝ) / k - (Q / k : ℕ) := sub_nonneg.mpr Nat.cast_div_le
    dsimp [f]
    rw [abs_mul, abs_of_nonneg ha]
    calc
      _ ≤ 1 * ((Q : ℝ) / k - (Q / k : ℕ)) :=
        mul_le_mul_of_nonneg_right (moebius_real_abs_le_one k) ha
      _ ≤ 1 := by simpa using hb
  have hsum : |∑ k ∈ Ioc 0 Q, f k| ≤ (Q : ℝ) - 1 := by
    rw [← sum_erase_add _ _ (show 1 ∈ Ioc 0 Q by simp; omega), hf1, add_zero]
    calc
      _ ≤ ∑ k ∈ (Ioc 0 Q).erase 1, |f k| := abs_sum_le_sum_abs _ _
      _ ≤ ∑ _k ∈ (Ioc 0 Q).erase 1, (1 : ℝ) := sum_le_sum hfbound
      _ = (Q : ℝ) - 1 := by
        simp [card_erase_of_mem (show 1 ∈ Ioc 0 Q by simp; omega)]
        rw [Nat.cast_sub (by omega : 1 ≤ Q)]
        norm_num
  have hprod : |(Q : ℝ) * reciprocalMobius Q| ≤ Q := by
    rw [hid]
    calc
      _ ≤ |(1 : ℝ)| + |∑ k ∈ Ioc 0 Q, f k| := abs_add_le _ _
      _ ≤ Q := by norm_num; linarith
  rw [abs_mul, abs_of_pos hQR] at hprod
  nlinarith

lemma reciprocalMobius_sub_eq {a b : ℕ} (hab : a ≤ b) :
    reciprocalMobius b - reciprocalMobius a =
      ∑ k ∈ Ioc a b, (ArithmeticFunction.moebius k : ℝ) / k := by
  have h := sum_Ioc_consecutive
    (fun k => (ArithmeticFunction.moebius k : ℝ) / k) (Nat.zero_le a) hab
  dsimp [reciprocalMobius]
  linarith

lemma reciprocalMobius_sub_abs_le {a b : ℕ} (hab : a ≤ b) :
    |reciprocalMobius b - reciprocalMobius a| ≤ ((b : ℝ) - a) / (a + 1) := by
  rw [reciprocalMobius_sub_eq hab]
  calc
    _ ≤ ∑ k ∈ Ioc a b, |(ArithmeticFunction.moebius k : ℝ) / k| :=
      abs_sum_le_sum_abs _ _
    _ ≤ ∑ _k ∈ Ioc a b, (1 : ℝ) / (a + 1) := by
      apply sum_le_sum
      intro k hk
      have hk' : a + 1 ≤ k := by have := (mem_Ioc.mp hk).1; omega
      have hkR : (0 : ℝ) < k := by exact_mod_cast (by omega : 0 < k)
      rw [abs_div, abs_of_pos hkR]
      calc
        _ ≤ 1 / (k : ℝ) := div_le_div_of_nonneg_right (moebius_real_abs_le_one k) hkR.le
        _ ≤ 1 / (a + 1 : ℝ) := by
          apply one_div_le_one_div_of_le (by positivity)
          exact_mod_cast hk'
    _ = ((b : ℝ) - a) / (a + 1) := by
      simp [Nat.cast_sub hab, nsmul_eq_mul, div_eq_mul_inv]

lemma quotient_block_abs_le {L t : ℕ} (ht : 0 < t) :
    |reciprocalMobius (L / t) - reciprocalMobius (L / (t + 1))| ≤
      1 / (t : ℝ) + 1 / ((L / (t + 1) : ℕ) + 1 : ℝ) := by
  have hab : L / (t + 1) ≤ L / t := Nat.div_le_div_left (by omega) ht
  have h1 := Nat.mul_div_le L t
  have h2 := Nat.lt_mul_div_succ L (show 0 < t + 1 by omega)
  have h1R : (t : ℝ) * (L / t : ℕ) ≤ L := by exact_mod_cast h1
  have h2R : (L : ℝ) < ((t : ℝ) + 1) * ((L / (t + 1) : ℕ) + 1) := by
    exact_mod_cast h2
  have htR : (0 : ℝ) < t := by positivity
  have haR : (0 : ℝ) < (L / (t + 1) : ℕ) + 1 := by positivity
  apply (reciprocalMobius_sub_abs_le hab).trans
  apply (div_le_iff₀ haR).mpr
  field_simp
  nlinarith

lemma quotient_block_sq_le {L t : ℕ} (ht : 0 < t) :
    (reciprocalMobius (L / t) - reciprocalMobius (L / (t + 1))) ^ 2 ≤
      2 * ((t : ℝ) ^ 2)⁻¹ + 2 * (((L / (t + 1) + 1 : ℕ) : ℝ) ^ 2)⁻¹ := by
  have h := quotient_block_abs_le (L := L) ht
  have hs := mul_self_le_mul_self (abs_nonneg _) h
  rw [← sq, sq_abs] at hs
  have hc := sq_nonneg (1 / (t : ℝ) - 1 / ((L / (t + 1) : ℕ) + 1 : ℝ))
  push_cast
  convert (show (reciprocalMobius (L / t) - reciprocalMobius (L / (t + 1))) ^ 2 ≤
      2 * (1 / (t : ℝ)) ^ 2 + 2 * (1 / ((L / (t + 1) : ℕ) + 1 : ℝ)) ^ 2 by
    nlinarith) using 1
  simp

lemma quotient_block_square_sum_le_of_first_bound (L : ℕ)
    (hfirst : (∑ t ∈ (Ico 1 L).filter (fun t => L / (t + 1) < L / t),
      (((L / (t + 1) + 1 : ℕ) : ℝ) ^ 2)⁻¹) ≤ 2) :
    (∑ t ∈ Ico 1 L,
      (reciprocalMobius (L / t) - reciprocalMobius (L / (t + 1))) ^ 2) ≤ 8 := by
  let E := (Ico 1 L).filter (fun t => L / (t + 1) < L / t)
  have hEsub : E ⊆ Ico 1 L := filter_subset _ _
  have heq : (∑ t ∈ Ico 1 L,
      (reciprocalMobius (L / t) - reciprocalMobius (L / (t + 1))) ^ 2) =
      ∑ t ∈ E, (reciprocalMobius (L / t) - reciprocalMobius (L / (t + 1))) ^ 2 := by
    symm
    apply sum_subset hEsub
    intro t ht htE
    have htpos : 0 < t := by have := (mem_Ico.mp ht).1; omega
    have hab : L / (t + 1) ≤ L / t :=
      Nat.div_le_div_left (show t ≤ t + 1 by omega) htpos
    have hn : ¬ L / (t + 1) < L / t := by
      intro h
      exact htE (mem_filter.mpr ⟨ht, h⟩)
    have hab' : L / t = L / (t + 1) := by omega
    simp [hab']
  have hsecond : (∑ t ∈ E, ((t : ℝ) ^ 2)⁻¹) ≤ 2 := by
    calc
      _ ≤ ∑ t ∈ Ioo 0 L, ((t : ℝ) ^ 2)⁻¹ := by
        apply sum_le_sum_of_subset_of_nonneg
        · intro t ht
          have hm := mem_Ico.mp (hEsub ht)
          exact mem_Ioo.mpr ⟨by omega, hm.2⟩
        · intros; positivity
      _ ≤ 2 := by simpa using (sum_Ioo_inv_sq_le (α := ℝ) 0 L)
  rw [heq]
  calc
    _ ≤ ∑ t ∈ E, (2 * ((t : ℝ) ^ 2)⁻¹ +
        2 * (((L / (t + 1) + 1 : ℕ) : ℝ) ^ 2)⁻¹) := by
      apply sum_le_sum
      intro t ht
      exact quotient_block_sq_le (by have := (mem_Ico.mp (hEsub ht)).1; omega)
    _ = 2 * (∑ t ∈ E, ((t : ℝ) ^ 2)⁻¹) +
        2 * (∑ t ∈ E, (((L / (t + 1) + 1 : ℕ) : ℝ) ^ 2)⁻¹) := by
      rw [sum_add_distrib, ← mul_sum, ← mul_sum]
    _ ≤ 8 := by dsimp [E] at *; linarith

/-- Quotient blocks have a cutoff-independent square sum, without Möbius cancellation. -/
theorem quotient_block_square_sum_le (L : ℕ) :
    (∑ t ∈ Ico 1 L,
      (reciprocalMobius (L / t) - reciprocalMobius (L / (t + 1))) ^ 2) ≤ 8 :=
  quotient_block_square_sum_le_of_first_bound L (quotient_block_first_square_sum_le L)

/-! ## Summation by parts and the weighted dual norm -/

def dualCoefficient (L t : ℕ) : ℝ :=
  if t = L then endpointWeight L L else endpointWeight L t - endpointWeight L (t + 1)

def dualNormSq (L : ℕ) : ℝ :=
  ∑ t ∈ Ioc 0 L, (t : ℝ) * (t + 1) * dualCoefficient L t ^ 2

theorem summation_by_parts (q u : ℕ → ℝ) (hu : u 0 = 0) {L : ℕ} (hL : 1 ≤ L) :
    (∑ d ∈ Ioc 0 L, q d * (u d - u (d - 1))) =
      q L * u L + ∑ t ∈ Ico 1 L, (q t - q (t + 1)) * u t := by
  induction L, hL using Nat.le_induction with
  | base => simp [hu]
  | succ L hL ih =>
    rw [sum_Ioc_succ_top (by omega), sum_Ico_succ_top hL, ih]
    simp only [Nat.add_sub_cancel]
    ring

theorem endpointFunctional_eq_dual {L : ℕ} (hL : 1 ≤ L) (u : ℕ → ℝ)
    (hu : u 0 = 0) :
    endpointFunctional L u = ∑ t ∈ Ioc 0 L, dualCoefficient L t * u t := by
  rw [endpointFunctional, summation_by_parts _ _ hu hL]
  rw [show Ioc 0 L = Icc 1 L by ext; simp; omega,
    ← sum_Ico_add_eq_sum_Icc hL]
  simp only [dualCoefficient]
  rw [add_comm]
  congr 1
  apply sum_congr rfl
  intro t ht
  rw [ite_eq_right (by have := (mem_Ico.mp ht).2; omega)]

theorem endpoint_weight_last {L : ℕ} (hL : 1 ≤ L) :
    endpointWeight L L = 1 / (L : ℝ) := by
  simp [endpointWeight, Nat.div_self (by omega : 0 < L), reciprocalMobius]

theorem dualNormSq_eq {L : ℕ} (hL : 1 ≤ L) :
    dualNormSq L =
      (∑ t ∈ Ico 1 L, (t : ℝ) * (t + 1) *
        (endpointWeight L t - endpointWeight L (t + 1)) ^ 2) +
      (L : ℝ) * (L + 1) * (1 / (L : ℝ)) ^ 2 := by
  rw [dualNormSq, show Ioc 0 L = Icc 1 L by ext; simp; omega,
    ← sum_Ico_add_eq_sum_Icc hL]
  simp only [dualCoefficient, endpoint_weight_last hL]
  congr 1
  apply sum_congr rfl
  intro t ht
  rw [ite_eq_right (by have := (mem_Ico.mp ht).2; omega)]

theorem endpoint_weight_difference {L t : ℕ} (ht : 0 < t) :
    endpointWeight L t - endpointWeight L (t + 1) =
      reciprocalMobius (L / t) / ((t : ℝ) * (t + 1)) +
      (reciprocalMobius (L / t) - reciprocalMobius (L / (t + 1))) / (t + 1) := by
  have htR : (t : ℝ) ≠ 0 := by positivity
  have ht1 : (t : ℝ) + 1 ≠ 0 := by positivity
  simp only [endpointWeight, Nat.cast_add, Nat.cast_one]
  field_simp
  ring

theorem weighted_difference_bound {x D t : ℝ} (ht : 1 ≤ t) (hx : |x| ≤ 1) :
    t * (t + 1) * (x / (t * (t + 1)) + D / (t + 1)) ^ 2 ≤
      2 * (t ^ 2)⁻¹ + 2 * D ^ 2 := by
  have ht0 : 0 < t := by linarith
  have ht1 : 0 < t + 1 := by linarith
  have hx2 : x ^ 2 ≤ 1 := by nlinarith [abs_le.mp hx]
  have hs := sq_nonneg (x - t * D)
  apply (mul_le_mul_iff_right₀ (show 0 < t ^ 2 * (t + 1) by positivity)).mp
  field_simp
  nlinarith [sq_nonneg D, mul_nonneg (sq_nonneg D) ht0.le,
    mul_nonneg (sub_nonneg.mpr hx2) ht0.le]

theorem reciprocal_square_sum_le (L : ℕ) :
    (∑ t ∈ Ico 1 L, ((t : ℝ) ^ 2)⁻¹) ≤ 2 := by
  have h := sum_Ioo_inv_sq_le (α := ℝ) 0 L
  simpa [show Ico 1 L = Ioo 0 L by ext; simp; omega] using h

theorem dualNormSq_le_of_bounds {L : ℕ} (hL : 1 ≤ L)
    (hm : ∀ Q : ℕ, |reciprocalMobius Q| ≤ 1)
    {B : ℝ}
    (hB : (∑ t ∈ Ico 1 L,
      (reciprocalMobius (L / t) - reciprocalMobius (L / (t + 1))) ^ 2) ≤ B) :
    dualNormSq L ≤ 6 + 2 * B := by
  rw [dualNormSq_eq hL]
  have hinter : (∑ t ∈ Ico 1 L, (t : ℝ) * (t + 1) *
      (endpointWeight L t - endpointWeight L (t + 1)) ^ 2) ≤ 4 + 2 * B := by
    calc
      _ ≤ ∑ t ∈ Ico 1 L, (2 * ((t : ℝ) ^ 2)⁻¹ +
          2 * (reciprocalMobius (L / t) - reciprocalMobius (L / (t + 1))) ^ 2) := by
        apply sum_le_sum
        intro t ht
        have ht1 := (mem_Ico.mp ht).1
        rw [endpoint_weight_difference (by omega)]
        exact weighted_difference_bound (by exact_mod_cast ht1) (hm _)
      _ ≤ 4 + 2 * B := by
        rw [sum_add_distrib, ← mul_sum, ← mul_sum]
        linarith [reciprocal_square_sum_le L]
  have hLR : (1 : ℝ) ≤ L := by exact_mod_cast hL
  have hlast : (L : ℝ) * (L + 1) * (1 / (L : ℝ)) ^ 2 ≤ 2 := by
    have hp : (0 : ℝ) < L := by linarith
    field_simp
    nlinarith
  linarith

theorem endpointFunctional_sq_le_dualNormSq {L : ℕ} (hL : 1 ≤ L)
    (u : ℕ → ℝ) (hu : u 0 = 0) :
    endpointFunctional L u ^ 2 ≤ dualNormSq L * residualEnergy L u := by
  rw [endpointFunctional_eq_dual hL u hu]
  apply sum_sq_le_sum_mul_sum_of_sq_le_mul
  · intro t ht
    have ht0 : (0 : ℝ) < t := by exact_mod_cast (mem_Ioc.mp ht).1
    positivity
  · intro t ht
    have ht0 : (0 : ℝ) < t := by exact_mod_cast (mem_Ioc.mp ht).1
    positivity
  · intro t ht
    have ht0 : (0 : ℝ) < t := by exact_mod_cast (mem_Ioc.mp ht).1
    field_simp
    ring_nf
    rfl

/-! ## The source-faithful endpoint and residual identities -/

theorem divisorCoefficients_reconstruction (N : ℕ) (a : ℕ → ℝ) {n : ℕ}
    (hn : 0 < n) :
    NB034.divisorCoefficients N a n =
      -(∑ d ∈ n.divisors, (ArithmeticFunction.moebius (n / d) : ℝ) *
        (NB034.observe N a d - NB034.observe N a (d - 1))) := by
  have hi := (ArithmeticFunction.sum_eq_iff_sum_mul_moebius_eq
    (f := NB034.divisorCoefficients N a)
    (g := fun t => -(NB034.observe N a t - NB034.observe N a (t - 1)))).mp
      (fun t ht => NB034.divisor_factorization N a ht) n hn
  rw [Nat.sum_divisorsAntidiagonal' (fun x y => (ArithmeticFunction.moebius x : ℝ) *
    -(NB034.observe N a y - NB034.observe N a (y - 1)))] at hi
  simpa only [mul_neg, sum_neg_distrib] using hi.symm

set_option backward.isDefEq.respectTransparency false in
theorem endpointFunctional_observe (L N : ℕ) (a : ℕ → ℝ) :
    endpointFunctional L (NB034.observe N a) =
      -(∑ n ∈ Ioc 0 L, NB034.divisorCoefficients N a n / n) := by
  let f : ArithmeticFunction ℝ := ⟨fun d =>
    (NB034.observe N a d - NB034.observe N a (d - 1)) / d, by simp⟩
  let g : ArithmeticFunction ℝ := ⟨fun k =>
    (ArithmeticFunction.moebius k : ℝ) / k, by simp⟩
  have hmul (n : ℕ) (hn : 0 < n) :
      (f * g) n = -(NB034.divisorCoefficients N a n / n) := by
    rw [divisorCoefficients_reconstruction N a hn, neg_div, neg_neg, sum_div]
    rw [ArithmeticFunction.mul_apply,
      Nat.sum_divisorsAntidiagonal (fun x y => f x * g y)]
    apply sum_congr rfl
    intro d hd
    dsimp [f, g]
    rw [Nat.cast_div_charZero (Nat.dvd_of_mem_divisors hd)]
    have hd0 : (d : ℝ) ≠ 0 := by
      exact_mod_cast (Nat.pos_of_mem_divisors hd).ne'
    have hn0 : (n : ℝ) ≠ 0 := by exact_mod_cast hn.ne'
    field_simp
  have hi := ArithmeticFunction.sum_Ioc_mul_eq_sum_sum f g L
  simp only [f, g, ArithmeticFunction.coe_mk] at hi
  have he : (∑ n ∈ Ioc 0 L,
      (NB034.observe N a n - NB034.observe N a (n - 1)) / n *
        ∑ k ∈ Ioc 0 (L / n), (ArithmeticFunction.moebius k : ℝ) / k) =
      endpointFunctional L (NB034.observe N a) := by
    apply sum_congr rfl
    intro d _
    dsimp [endpointWeight, reciprocalMobius]
    ring
  rw [he] at hi
  rw [← hi, ← sum_neg_distrib]
  apply sum_congr rfl
  intro n hn
  exact hmul n (mem_Ioc.mp hn).1

theorem weighted_tail_endpoint {M N : ℕ} (hM : 2 ≤ M) (hMN : M ≤ N)
    (a : ℕ → ℝ) :
    (∑ n ∈ Icc M N, a n / n) =
      endpointFunctional (M - 1) (NB034.observe N a) := by
  rw [endpointFunctional_observe]
  have hhead : (∑ n ∈ Ioc 0 (M - 1),
      (if n ∈ Icc 2 N then a n else 0) / n) = ∑ n ∈ Ico 2 M, a n / n := by
    simp only [ite_div, zero_div]
    rw [← sum_filter]
    congr 1
    ext n
    simp only [mem_filter, mem_Ioc, mem_Icc, mem_Ico]
    omega
  have hcoef : (∑ n ∈ Ioc 0 (M - 1), NB034.divisorCoefficients N a n / n) =
      (∑ n ∈ Ico 2 M, a n / n) - NB034.observe N a 1 := by
    simp only [NB034.divisorCoefficients, sub_div, sum_sub_distrib]
    rw [hhead]
    simp only [ite_div, zero_div, sum_ite_eq']
    simp [mem_Ioc, show 1 ≤ M - 1 by omega]
  rw [hcoef, NB034.observe_one]
  have hsplit : (∑ n ∈ Ico 2 M, a n / n) + (∑ n ∈ Icc M N, a n / n) =
      ∑ n ∈ Icc 2 N, a n / n := by
    have hright : Icc M N = Ico M (N + 1) := by ext; simp
    have hfull : Icc 2 N = Ico 2 (N + 1) := by ext; simp
    rw [hright, hfull]
    exact sum_Ico_consecutive _ hM (by omega)
  linarith

/-- The auxiliary residual is zero at index zero, as required by the endpoint functional. -/
def earlyResidual (N : ℕ) (a : ℕ → ℝ) (t : ℕ) : ℝ :=
  if t = 0 then 0 else 1 - NB034.observe N a t

@[simp] theorem earlyResidual_zero (N : ℕ) (a : ℕ → ℝ) :
    earlyResidual N a 0 = 0 := by simp [earlyResidual]

theorem endpointFunctional_earlyResidual {L : ℕ} (hL : 0 < L)
    (N : ℕ) (a : ℕ → ℝ) :
    endpointFunctional L (NB034.observe N a) =
      reciprocalMobius L - endpointFunctional L (earlyResidual N a) := by
  have hsum : endpointFunctional L (NB034.observe N a) =
      (∑ d ∈ Ioc 0 L, if d = 1 then endpointWeight L d else 0) -
        endpointFunctional L (earlyResidual N a) := by
    simp only [endpointFunctional, ← sum_sub_distrib]
    apply sum_congr rfl
    intro d hd
    have hd0 : d ≠ 0 := (mem_Ioc.mp hd).1.ne'
    by_cases hd1 : d = 1
    · simp [hd1, earlyResidual]
      ring
    · have hpred : d - 1 ≠ 0 := by have := (mem_Ioc.mp hd).1; omega
      simp only [hd1, ite_false, earlyResidual, hd0, hpred]
      ring
  rw [hsum, sum_ite_eq']
  simp [mem_Ioc, show 1 ≤ L by omega, endpointWeight]

/-- Exact reciprocal-Möbius locking identity before the analytic estimate. -/
theorem weighted_tail_residual_identity {M N : ℕ} (hM : 2 ≤ M) (hMN : M ≤ N)
    (a : ℕ → ℝ) :
    (∑ n ∈ Icc M N, a n / n) =
      reciprocalMobius (M - 1) - endpointFunctional (M - 1) (earlyResidual N a) := by
  rw [weighted_tail_endpoint hM hMN a,
    endpointFunctional_earlyResidual (by omega : 0 < M - 1)]

/-- At the smallest cutoff the harmonic aggregate is the first shell value. -/
theorem weighted_tail_two (N : ℕ) (a : ℕ → ℝ) :
    (∑ n ∈ Icc 2 N, a n / n) = 1 - earlyResidual N a 1 := by
  simp only [earlyResidual, one_ne_zero, ite_false, sub_sub_cancel]
  exact (NB034.observe_one N a).symm

/-! ## Uniform locking of the harmonic tail -/

theorem residualEnergy_nonneg (L : ℕ) (u : ℕ → ℝ) : 0 ≤ residualEnergy L u := by
  apply sum_nonneg
  intro t ht
  have ht0 : (0 : ℝ) < t := by exact_mod_cast (mem_Ioc.mp ht).1
  positivity

theorem residualEnergy_earlyResidual (M N : ℕ) (a : ℕ → ℝ) :
    residualEnergy (M - 1) (earlyResidual N a) =
      ∑ t ∈ Ico 1 M, (1 - NB034.observe N a t) ^ 2 / ((t : ℝ) * (t + 1)) := by
  have hset : Ioc 0 (M - 1) = Ico 1 M := by ext; simp; omega
  rw [residualEnergy, hset]
  apply sum_congr rfl
  intro t ht
  rw [earlyResidual, ite_eq_right (by have := (mem_Ico.mp ht).1; omega)]

theorem weighted_tail_bound_of_dual {M N : ℕ} (hM : 2 ≤ M) (hMN : M ≤ N)
    (a : ℕ → ℝ) {C : ℝ} (hC : dualNormSq (M - 1) ≤ C) :
    |(∑ n ∈ Icc M N, a n / n) - reciprocalMobius (M - 1)| ^ 2 ≤
      C * ∑ t ∈ Ico 1 M,
        (1 - NB034.observe N a t) ^ 2 / ((t : ℝ) * (t + 1)) := by
  have h := endpointFunctional_sq_le_dualNormSq (by omega : 1 ≤ M - 1)
    (earlyResidual N a) (earlyResidual_zero N a)
  have hbound := h.trans (mul_le_mul_of_nonneg_right hC
    (residualEnergy_nonneg (M - 1) (earlyResidual N a)))
  rw [residualEnergy_earlyResidual] at hbound
  rw [weighted_tail_residual_identity hM hMN a, sub_sub_cancel_left, sq_abs, neg_sq]
  exact hbound

/-- The endpoint row has an absolute squared norm, independent of the cutoff. -/
theorem dualNormSq_le {L : ℕ} (hL : 1 ≤ L) : dualNormSq L ≤ 22 := by
  have h := dualNormSq_le_of_bounds hL reciprocalMobius_abs_le_one
    (quotient_block_square_sum_le L)
  norm_num at h
  exact h

/-- Uniform boundedness of the discrete reciprocal-Möbius endpoint operator. -/
theorem uniform_functional_bound {L : ℕ} (hL : 1 ≤ L) (u : ℕ → ℝ)
    (hu : u 0 = 0) : endpointFunctional L u ^ 2 ≤ 22 * residualEnergy L u := by
  exact (endpointFunctional_sq_le_dualNormSq hL u hu).trans
    (mul_le_mul_of_nonneg_right (dualNormSq_le hL) (residualEnergy_nonneg L u))

/-- A stronger finite coefficient/shell estimate than the issue's constant 49. -/
theorem uniform_tail_locking_strong {M N : ℕ} (hM : 2 ≤ M) (hMN : M ≤ N)
    (a : ℕ → ℝ) :
    |(∑ n ∈ Icc M N, a n / n) - reciprocalMobius (M - 1)| ^ 2 ≤
      22 * ∑ t ∈ Ico 1 M,
        (1 - NB034.observe N a t) ^ 2 / ((t : ℝ) * (t + 1)) := by
  exact weighted_tail_bound_of_dual hM hMN a (dualNormSq_le (by omega))

/-- The frozen NB-035 finite theorem: the normalized tail is uniformly Möbius-locked. -/
theorem uniform_tail_locking {M N : ℕ} (hM : 2 ≤ M) (hMN : M ≤ N)
    (a : ℕ → ℝ) :
    |(∑ n ∈ Icc M N, a n / n) - reciprocalMobius (M - 1)| ^ 2 ≤
      49 * ∑ t ∈ Ico 1 M,
        (1 - NB034.observe N a t) ^ 2 / ((t : ℝ) * (t + 1)) := by
  apply weighted_tail_bound_of_dual hM hMN a
  exact (dualNormSq_le (by omega)).trans (by norm_num)

end Mathia.NB035

#print axioms Mathia.NB035.reciprocalMobius_abs_le_one
#print axioms Mathia.NB035.quotient_block_first_injective
#print axioms Mathia.NB035.quotient_block_square_sum_le
#print axioms Mathia.NB035.weighted_tail_residual_identity
#print axioms Mathia.NB035.dualNormSq_le
#print axioms Mathia.NB035.uniform_functional_bound
#print axioms Mathia.NB035.uniform_tail_locking_strong
#print axioms Mathia.NB035.uniform_tail_locking
#print axioms Mathia.NB035.weighted_tail_two
