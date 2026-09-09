import Mathlib.Algebra.Polynomial.Eval.Degree
import Mathlib.Algebra.Polynomial.Degree.Operations
import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# Ordered sign variation obstructs moment cancellation

Associated finding:
`research/arithmetic_fidelity/findings/AF-216-ordered-sign-complexity-caps-moment-and-dirichlet-cancellation.md`

Formalized theorem boundary: a nonempty strictly ordered finite real support with
nonzero real coefficients that annihilates every monomial of degree below `m`
has at least `m` adjacent sign changes. `Fin (n + 1)` makes the nonzero-source
boundary explicit. All coefficients are assumed nonzero; zero deletion is not
formalized. The auxiliary polynomial has degree at most the sign variation and
strictly positive coefficient-weighted evaluations at every support node.

Not formalized: sharpness, the Dirichlet corollary, quantitative conditioning,
Euler-factor recovery, intrinsic prime sign budgets, or RH consequences. This is
classical sign-variation mathematics; no novelty claim is made.
-/

open Polynomial Finset

namespace Mathia.ArithmeticFidelity.AF216

/-- The number of genuine consecutive gaps with opposite coefficient signs.
The support has `n + 1` points and there are exactly `n` gaps, with no wraparound. -/
noncomputable def signVariation {n : ℕ} (a : Fin (n + 1) → ℝ) : ℕ :=
  ∑ i : Fin n, if a i.castSucc * a i.succ < 0 then 1 else 0

private lemma signVariation_tail {n : ℕ} (a : Fin (n + 2) → ℝ) :
    signVariation a = (if a 0 * a (Fin.succ 0) < 0 then 1 else 0) +
      signVariation (fun i => a i.succ) := by
  classical
  simp only [signVariation, Fin.sum_univ_succ, Fin.castSucc_zero, Fin.castSucc_succ]
  rfl

/-- A separator polynomial matching every coefficient sign. The extra left-ray
condition supports induction when a new leftmost node is inserted. -/
theorem exists_signMatching_polynomial {n : ℕ} (x a : Fin (n + 1) → ℝ)
    (hx : StrictMono x) (ha : ∀ i, a i ≠ 0) :
    ∃ p : ℝ[X], p.natDegree ≤ signVariation a ∧
      (∀ i, 0 < a i * p.eval (x i)) ∧
      (∀ t : ℝ, t ≤ x 0 → 0 < a 0 * p.eval t) := by
  classical
  induction n with
  | zero =>
      refine ⟨C (a 0), ?_, ?_, ?_⟩
      · simp [signVariation]
      · intro i
        have hi : i = 0 := Fin.eq_zero i
        subst i
        simpa using mul_self_pos.mpr (ha 0)
      · intro t ht
        simpa using mul_self_pos.mpr (ha 0)
  | succ n ih =>
      have hxt : StrictMono (fun i : Fin (n + 1) => x i.succ) :=
        fun i j hij => hx (Fin.succ_lt_succ_iff.mpr hij)
      obtain ⟨p, hpdeg, hpnode, hpray⟩ :=
        ih (fun i => x i.succ) (fun i => a i.succ) hxt (fun i => ha i.succ)
      have hgap : x 0 < x (Fin.succ 0) := hx (by simp)
      have hapos : a 0 * a (Fin.succ 0) ≠ 0 := mul_ne_zero (ha 0) (ha _)
      by_cases hflip : a 0 * a (Fin.succ 0) < 0
      · let c : ℝ := (x 0 + x (Fin.succ 0)) / 2
        have hc0 : x 0 < c := by dsimp only [c]; linarith
        have hc1 : c < x (Fin.succ 0) := by dsimp only [c]; linarith
        have hleft : ∀ t : ℝ, t ≤ x 0 → 0 < a 0 * ((t - c) * p.eval t) := by
          intro t ht
          have hp := hpray t (le_trans ht hgap.le)
          have htc : t - c < 0 := by linarith
          rcases mul_neg_iff.mp hflip with h | h <;>
            rcases mul_pos_iff.mp hp with hp | hp <;>
            rcases h with ⟨h0, h1⟩ <;> rcases hp with ⟨hp1, hp2⟩
          · linarith
          · exact mul_pos h0 (mul_pos_of_neg_of_neg htc hp2)
          · exact mul_pos_of_neg_of_neg h0 (mul_neg_of_neg_of_pos htc hp2)
          · linarith
        refine ⟨(X - C c) * p, ?_, ?_, ?_⟩
        · calc
            ((X - C c) * p).natDegree ≤ 1 + p.natDegree := by
              have hd := natDegree_mul_le (p := X - C c) (q := p)
              rw [natDegree_X_sub_C] at hd
              exact hd
            _ ≤ signVariation a := by rw [signVariation_tail, ite_eq_left hflip]; omega
        · intro i
          refine Fin.cases ?_ (fun j => ?_) i
          · simpa using hleft (x 0) le_rfl
          · have hcj : c < x j.succ :=
              lt_of_lt_of_le hc1 (hx.monotone (Fin.succ_le_succ_iff.mpr (Fin.zero_le j)))
            have hpos := mul_pos (sub_pos.mpr hcj) (hpnode j)
            simpa [mul_assoc, mul_left_comm] using hpos
        · intro t ht
          simpa using hleft t ht
      · have hsame : 0 < a 0 * a (Fin.succ 0) :=
          lt_of_le_of_ne (le_of_not_gt hflip) (Ne.symm hapos)
        have hleft : ∀ t : ℝ, t ≤ x 0 → 0 < a 0 * p.eval t := by
          intro t ht
          have hp := hpray t (le_trans ht hgap.le)
          rcases mul_pos_iff.mp hsame with h | h <;>
            rcases mul_pos_iff.mp hp with hp | hp <;>
            rcases h with ⟨h0, h1⟩ <;> rcases hp with ⟨hp1, hp2⟩
          · exact mul_pos h0 hp2
          · linarith
          · linarith
          · exact mul_pos_of_neg_of_neg h0 hp2
        refine ⟨p, ?_, ?_, hleft⟩
        · rw [signVariation_tail, ite_eq_right hflip, zero_add]
          exact hpdeg
        · intro i
          exact Fin.cases (hleft (x 0) le_rfl) hpnode i

/-- Vanishing monomial moments annihilate every polynomial below the same degree. -/
theorem sum_mul_eval_eq_zero {n m : ℕ} (x a : Fin n → ℝ)
    (hmom : ∀ k < m, ∑ i, a i * x i ^ k = 0)
    (p : ℝ[X]) (hp : p.natDegree < m) : ∑ i, a i * p.eval (x i) = 0 := by
  simp_rw [Polynomial.eval_eq_sum_range' hp, Finset.mul_sum]
  rw [Finset.sum_comm]
  apply Finset.sum_eq_zero
  intro k hk
  calc
    ∑ i, a i * (p.coeff k * x i ^ k) = p.coeff k * ∑ i, a i * x i ^ k := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro i hi
      ring
    _ = 0 := by rw [hmom k (Finset.mem_range.mp hk), mul_zero]

/-- AF-216: annihilating the first `m` moments requires at least `m` sign changes.
The statement also covers `m = 0`, when the conclusion is automatic. -/
theorem moment_order_le_signVariation {n m : ℕ} (x a : Fin (n + 1) → ℝ)
    (hx : StrictMono x) (ha : ∀ i, a i ≠ 0)
    (hmom : ∀ k < m, ∑ i, a i * x i ^ k = 0) : m ≤ signVariation a := by
  by_contra h
  have hlt : signVariation a < m := Nat.lt_of_not_ge h
  obtain ⟨p, hpdeg, hpnode, _⟩ := exists_signMatching_polynomial x a hx ha
  have hz := sum_mul_eval_eq_zero x a hmom p (lt_of_le_of_lt hpdeg hlt)
  have hpos : 0 < ∑ i, a i * p.eval (x i) :=
    Finset.sum_pos (fun i _ => hpnode i) Finset.univ_nonempty
  linarith

end Mathia.ArithmeticFidelity.AF216
