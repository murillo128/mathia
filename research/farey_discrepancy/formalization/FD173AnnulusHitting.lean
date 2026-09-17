import Mathlib.Data.Nat.PrimeFin
import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity

/-!
# FD-173 prime-power annulus hitting

Associated finding:
`research/farey_discrepancy/findings/FD-173-prime-power-annulus-hitting-exactly-classifies-sparse-midpoint-target-rigidity.md`

Formalized theorem boundary: for real defects nonnegative at primes, the product
of defects over distinct prime factors defines an odd mass. Observations consist
of its mass in (H/2,H] plus the defect at 2 times the lower odd prefix. For a
nonempty family of integer horizons H ≥ 2, these observations distinguish zero
prime defect from every admissible alternative exactly when every odd prime's
positive-power orbit meets an observed annulus. The explicit invisible
single-prime defect and the primewise stability bound are also proved.

Natural division implements the real half-cutoff exactly on integer atoms.
The product is defined on all naturals, but only odd positive inputs enter the
observations; its value at 0 is never used.

Not formalized: the identification of this product with the odd part of the
squarefree multiplicative source convolution, the FD-172 Farey midpoint identity
Obs(H) = -2 E_H, extension from prime coordinates to equality with Möbius,
the squarefree coefficient error estimate, geometric-ladder recurrence,
Franel--Landau destination estimates, or RH. Thus this is the FD-173 source-side
classification in defect coordinates, conditional on the external midpoint
bridge when interpreted as a theorem about Farey observations. It is target
rigidity, not pairwise injectivity among arbitrary sources.
-/

noncomputable section
namespace Mathia.FD173
open Finset Classical

/-- Only prime coordinates enter the mass and observations. -/
def Admissible (δ : ℕ → ℝ) : Prop := ∀ p, Nat.Prime p → 0 ≤ δ p

/-- Each distinct prime contributes once, independently of its exponent. -/
def mass (δ : ℕ → ℝ) (m : ℕ) : ℝ := ∏ p ∈ m.primeFactors, δ p

def oddPrefix (x : ℕ) : Finset ℕ := (range (x + 1)).filter (fun m => m % 2 = 1)

def annulus (H : ℕ) : Finset ℕ := (oddPrefix H).filter (fun m => H / 2 < m)

def prefixMass (δ : ℕ → ℝ) (x : ℕ) : ℝ := ∑ m ∈ oddPrefix x, mass δ m

def observation (δ : ℕ → ℝ) (H : ℕ) : ℝ :=
  (∑ m ∈ annulus H, mass δ m) + δ 2 * prefixMass δ (H / 2)

@[simp] theorem mem_oddPrefix {m x : ℕ} : m ∈ oddPrefix x ↔ m ≤ x ∧ m % 2 = 1 := by
  simp [oddPrefix, Nat.lt_succ_iff]

@[simp] theorem mem_annulus {m H : ℕ} :
    m ∈ annulus H ↔ m ≤ H ∧ m % 2 = 1 ∧ H / 2 < m := by
  simp [annulus, and_assoc]

/-- In particular, an odd horizon does not shift the open lower endpoint. -/
theorem half_lt_iff {H m : ℕ} : H / 2 < m ↔ H < 2 * m := by omega

theorem real_half_lt_iff {H m : ℕ} : (H : ℝ) / 2 < m ↔ H / 2 < m := by
  rw [half_lt_iff]
  constructor
  · intro h
    have : (H : ℝ) < 2 * (m : ℝ) := by linarith
    exact_mod_cast this
  · intro h
    have : (H : ℝ) < 2 * (m : ℝ) := by exact_mod_cast h
    linarith

@[simp] theorem mass_one (δ : ℕ → ℝ) : mass δ 1 = 1 := by simp [mass]

theorem mass_nonneg {δ : ℕ → ℝ} (hδ : Admissible δ) (m : ℕ) : 0 ≤ mass δ m := by
  exact prod_nonneg fun p hp => hδ p (Nat.prime_of_mem_primeFactors hp)

theorem mass_prime_pow (δ : ℕ → ℝ) {p j : ℕ} (hp : Nat.Prime p) (hj : 1 ≤ j) :
    mass δ (p ^ j) = δ p := by
  simp [mass, Nat.primeFactors_prime_pow (by omega : j ≠ 0) hp]

theorem prefixMass_nonneg {δ : ℕ → ℝ} (hδ : Admissible δ) (x : ℕ) :
    0 ≤ prefixMass δ x := sum_nonneg fun m _ => mass_nonneg hδ m

theorem one_le_prefixMass {δ : ℕ → ℝ} (hδ : Admissible δ) {x : ℕ} (hx : 1 ≤ x) :
    1 ≤ prefixMass δ x := by
  have h := single_le_sum (fun m (_ : m ∈ oddPrefix x) => mass_nonneg hδ m)
    (show 1 ∈ oddPrefix x by simp [hx])
  simpa only [mass_one, prefixMass] using h

theorem annulus_eq_sdiff (H : ℕ) : annulus H = oddPrefix H \ oddPrefix (H / 2) := by
  ext m
  simp only [mem_annulus, mem_sdiff, mem_oddPrefix]
  omega

theorem observation_eq_prefix (δ : ℕ → ℝ) (H : ℕ) :
    observation δ H = prefixMass δ H - prefixMass δ (H / 2) +
      δ 2 * prefixMass δ (H / 2) := by
  have hs : oddPrefix (H / 2) ⊆ oddPrefix H := by
    intro m hm
    obtain ⟨hm, ho⟩ := mem_oddPrefix.mp hm
    exact mem_oddPrefix.mpr ⟨hm.trans (Nat.div_le_self H 2), ho⟩
  have heq := sum_sdiff (f := mass δ) hs
  rw [← annulus_eq_sdiff] at heq
  unfold observation prefixMass
  linarith

theorem observation_nonneg {δ : ℕ → ℝ} (hδ : Admissible δ) (H : ℕ) :
    0 ≤ observation δ H := by
  exact add_nonneg (sum_nonneg fun m _ => mass_nonneg hδ m)
    (mul_nonneg (hδ 2 Nat.prime_two) (prefixMass_nonneg hδ _))

theorem two_defect_le_observation {δ : ℕ → ℝ} (hδ : Admissible δ)
    {H : ℕ} (hH : 2 ≤ H) : δ 2 ≤ observation δ H := by
  have hp := one_le_prefixMass hδ (show 1 ≤ H / 2 by omega)
  have hd := hδ 2 Nat.prime_two
  have hs : 0 ≤ ∑ m ∈ annulus H, mass δ m := sum_nonneg fun m _ => mass_nonneg hδ m
  unfold observation
  nlinarith

theorem mass_le_observation {δ : ℕ → ℝ} (hδ : Admissible δ)
    {H m : ℕ} (hm : m ∈ annulus H) : mass δ m ≤ observation δ H := by
  have hs := single_le_sum (fun n (_ : n ∈ annulus H) => mass_nonneg hδ n) hm
  have hp := mul_nonneg (hδ 2 Nat.prime_two) (prefixMass_nonneg hδ (H / 2))
  unfold observation
  linarith

theorem observation_zero {δ : ℕ → ℝ} (hδ : Admissible δ)
    {H : ℕ} (hH : 2 ≤ H) (hz : observation δ H = 0) :
    δ 2 = 0 ∧ ∀ m ∈ annulus H, mass δ m = 0 := by
  constructor
  · exact le_antisymm (hz ▸ two_defect_le_observation hδ hH) (hδ 2 Nat.prime_two)
  · intro m hm
    exact le_antisymm (hz ▸ mass_le_observation hδ hm) (mass_nonneg hδ m)

@[simp] theorem observation_two (δ : ℕ → ℝ) : observation δ 2 = δ 2 := by
  norm_num [observation, annulus, oddPrefix, prefixMass, mass, range_add_one, filter_insert, filter_singleton]

/-- Every odd prime is sensed at some positive power, possibly above the prime itself. -/
def Hits (Hs : Set ℕ) : Prop := ∀ p, Nat.Prime p → p % 2 = 1 →
  ∃ j, 1 ≤ j ∧ ∃ H ∈ Hs, H / 2 < p ^ j ∧ p ^ j ≤ H

def Rigid (Hs : Set ℕ) : Prop := ∀ δ, Admissible δ →
  (∀ H ∈ Hs, observation δ H = 0) → ∀ p, Nat.Prime p → δ p = 0

/-- Quantitative local witness for an odd prime defect. -/
theorem prime_defect_le_observation {δ : ℕ → ℝ} (hδ : Admissible δ)
    {p j H : ℕ} (hp : Nat.Prime p) (ho : p % 2 = 1) (hj : 1 ≤ j)
    (hl : H / 2 < p ^ j) (hu : p ^ j ≤ H) : δ p ≤ observation δ H := by
  rw [← mass_prime_pow δ hp hj]
  apply mass_le_observation hδ
  exact mem_annulus.mpr ⟨hu, by simp [Nat.pow_mod, ho], hl⟩

theorem rigid_of_hits {Hs : Set ℕ} (hne : Hs.Nonempty)
    (hHs : ∀ H ∈ Hs, 2 ≤ H) (hhit : Hits Hs) : Rigid Hs := by
  intro δ hδ hz p hp
  rcases hp.eq_two_or_odd with rfl | ho
  · obtain ⟨H, hH⟩ := hne
    exact (observation_zero hδ (hHs H hH) (hz H hH)).1
  · obtain ⟨j, hj, H, hH, hl, hu⟩ := hhit p hp ho
    exact le_antisymm (hz H hH ▸ prime_defect_le_observation hδ hp ho hj hl hu) (hδ p hp)

/-- The alternative source has just one nonzero prime coordinate. -/
def singleDefect (p q : ℕ) : ℝ := if q = p then 1 else 0

theorem singleDefect_admissible (p : ℕ) : Admissible (singleDefect p) := by
  intro q _
  simp only [singleDefect]
  split_ifs <;> norm_num

/-- The atom at 1 is the zeroth power. The positive-input hypothesis excludes 0. -/
theorem mass_singleDefect {p m : ℕ} (hp : Nat.Prime p) (hm : 0 < m) :
    mass (singleDefect p) m = if ∃ j : ℕ, m = p ^ j then 1 else 0 := by
  classical
  by_cases hpow : ∃ j : ℕ, m = p ^ j
  · obtain ⟨j, rfl⟩ := hpow
    rw [ite_eq_left ⟨j, rfl⟩]
    by_cases hj : j = 0
    · simp [hj]
    · simp [mass_prime_pow _ hp (by omega : 1 ≤ j), singleDefect]
  · rw [ite_eq_right hpow]
    have hfactor : ∃ q ∈ m.primeFactors, q ≠ p := by
      by_contra h
      push Not at h
      have heq := Nat.eq_prime_pow_of_unique_prime_dvd (by omega : m ≠ 0)
        (fun {q} hq hd => h q (Nat.mem_primeFactors.mpr ⟨hq, hd, by omega⟩))
      exact hpow ⟨_, heq⟩
    obtain ⟨q, hq, hqp⟩ := hfactor
    exact prod_eq_zero hq (by simp [singleDefect, hqp])

/-- A complete missed orbit produces a nonzero defect invisible at every horizon. -/
theorem singleDefect_invisible {Hs : Set ℕ} (hHs : ∀ H ∈ Hs, 2 ≤ H)
    {p : ℕ} (hp : Nat.Prime p) (ho : p % 2 = 1)
    (hmiss : ∀ j, 1 ≤ j → ∀ H ∈ Hs, ¬ (H / 2 < p ^ j ∧ p ^ j ≤ H)) :
    (∀ H ∈ Hs, observation (singleDefect p) H = 0) ∧ singleDefect p p = 1 := by
  have hp2 : 2 ≠ p := by omega
  refine ⟨?_, by simp [singleDefect]⟩
  intro H hH
  have hH2 := hHs H hH
  have hs : ∑ m ∈ annulus H, mass (singleDefect p) m = 0 := by
    apply sum_eq_zero
    intro m hm
    obtain ⟨hu, _, hl⟩ := mem_annulus.mp hm
    rw [mass_singleDefect hp (by omega)]
    apply ite_eq_right
    rintro ⟨j, rfl⟩
    have hj : 1 ≤ j := by
      by_contra h
      have : j = 0 := by omega
      simp [this] at hl
      omega
    exact hmiss j hj H hH ⟨hl, hu⟩
  simp [observation, hs, singleDefect, hp2]

/-- Exact target-rigidity classification; arbitrary-source pairwise injectivity is not asserted. -/
theorem rigid_iff_hits {Hs : Set ℕ} (hne : Hs.Nonempty)
    (hHs : ∀ H ∈ Hs, 2 ≤ H) : Rigid Hs ↔ Hits Hs := by
  classical
  refine ⟨?_, rigid_of_hits hne hHs⟩
  intro hr p hp ho
  by_contra hmiss
  have hm : ∀ j, 1 ≤ j → ∀ H ∈ Hs, ¬ (H / 2 < p ^ j ∧ p ^ j ≤ H) := by
    intro j hj H hH h
    exact hmiss ⟨j, hj, H, hH, h⟩
  obtain ⟨hz, hone⟩ := singleDefect_invisible hHs hp ho hm
  have hzero := hr (singleDefect p) (singleDefect_admissible p) hz p hp
  linarith

/-- The same witnesses control every prime defect with the observation error modulus. -/
theorem primewise_stability {Hs : Set ℕ} (hne : Hs.Nonempty)
    (hHs : ∀ H ∈ Hs, 2 ≤ H) (hhit : Hits Hs)
    {δ : ℕ → ℝ} (hδ : Admissible δ) {ε : ℝ}
    (hb : ∀ H ∈ Hs, observation δ H ≤ 2 * ε) :
    ∀ p, Nat.Prime p → 0 ≤ δ p ∧ δ p ≤ 2 * ε := by
  intro p hp
  refine ⟨hδ p hp, ?_⟩
  rcases hp.eq_two_or_odd with rfl | ho
  · obtain ⟨H, hH⟩ := hne
    exact (two_defect_le_observation hδ (hHs H hH)).trans (hb H hH)
  · obtain ⟨j, hj, H, hH, hl, hu⟩ := hhit p hp ho
    exact (prime_defect_le_observation hδ hp ho hj hl hu).trans (hb H hH)

end Mathia.FD173
