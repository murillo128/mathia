import Mathlib.Analysis.Normed.Module.Seminorm.Basic
import Mathlib.Data.Fintype.Fin

/-!
# AF-134 minimal compositional witness saturation

Associated finding:
`research/arithmetic_fidelity/findings/AF-134-minimal-compositional-witness-saturation.md`

Formalized theorem boundary: the join of a baseline real seminorm and an upstream
seminorm pulled back along a linear map is the least seminorm dominating both.
For every finite prefix of a chain of possibly different real vector spaces,
recursive saturation is the maximum of all transported baseline seminorms, is
minimal among baseline-dominating families making each map nonexpansive, and
has zero set exactly the intersection of the transported baseline zero sets.
Kernels are expressed as zero sets, including degenerate seminorms and zero maps.

Not formalized: the convex witness bodies, support-function duality and its
bridge to minimality by body inclusion, the dual spanning/observability criterion,
weighted caps, or arithmetic applications. The seminorm ingredients are classical
and reuse mathlib's join and pullback; no novelty is claimed.
-/

namespace Mathia.AF134

open scoped NNReal

noncomputable section

section OneStep

variable {X Y : Type*} [AddCommGroup X] [Module ℝ X]
  [AddCommGroup Y] [Module ℝ Y]

/-- Adjoin exactly the upstream seminorm required by the prescribed linear recovery. -/
def saturate (pX : Seminorm ℝ X) (pY : Seminorm ℝ Y) (L : Y →ₗ[ℝ] X) :
    Seminorm ℝ Y := pY ⊔ pX.comp L

theorem saturate_apply (pX : Seminorm ℝ X) (pY : Seminorm ℝ Y)
    (L : Y →ₗ[ℝ] X) (y : Y) :
    saturate pX pY L y = max (pY y) (pX (L y)) := rfl

theorem baseline_le_saturate (pX : Seminorm ℝ X) (pY : Seminorm ℝ Y)
    (L : Y →ₗ[ℝ] X) : pY ≤ saturate pX pY L := le_sup_left

theorem pullback_le_saturate (pX : Seminorm ℝ X) (pY : Seminorm ℝ Y)
    (L : Y →ₗ[ℝ] X) (y : Y) : pX (L y) ≤ saturate pX pY L y :=
  (le_sup_right : pX.comp L ≤ pY ⊔ pX.comp L) y

theorem saturate_le_iff (pX : Seminorm ℝ X) (pY r : Seminorm ℝ Y)
    (L : Y →ₗ[ℝ] X) :
    saturate pX pY L ≤ r ↔ pY ≤ r ∧ pX.comp L ≤ r := sup_le_iff

theorem saturate_eq_zero_iff (pX : Seminorm ℝ X) (pY : Seminorm ℝ Y)
    (L : Y →ₗ[ℝ] X) (y : Y) :
    saturate pX pY L y = 0 ↔ pY y = 0 ∧ pX (L y) = 0 := by
  rw [saturate_apply]
  constructor
  · intro h
    exact ⟨le_antisymm (h ▸ le_max_left _ _) (apply_nonneg _ _),
      le_antisymm (h ▸ le_max_right _ _) (apply_nonneg _ _)⟩
  · rintro ⟨hY, hX⟩
    simp [hY, hX]

theorem saturate_zero_set (pX : Seminorm ℝ X) (pY : Seminorm ℝ Y)
    (L : Y →ₗ[ℝ] X) :
    {y | saturate pX pY L y = 0} =
      {y | pY y = 0} ∩ L ⁻¹' {x | pX x = 0} := by
  ext y
  exact saturate_eq_zero_iff pX pY L y

end OneStep

section Chain

variable {E : ℕ → Type*} [∀ n, AddCommGroup (E n)] [∀ n, Module ℝ (E n)]
  (p : ∀ n, Seminorm ℝ (E n)) (L : ∀ n, E (n + 1) →ₗ[ℝ] E n)

/-- Saturation on finite prefixes; `L n` transports from stage `n+1` to stage `n`. -/
def chain : ∀ n, Seminorm ℝ (E n)
  | 0 => p 0
  | n + 1 => saturate (chain n) (p (n + 1)) (L n)

/-- Transported baseline seminorms, newest first. Index `j` at stage `n` is the
baseline at stage `n-j` pulled back along `L (n-j), …, L (n-1)` in that order.
The recursive enumeration avoids casts between the different vector spaces. -/
def transported : ∀ n, Fin (n + 1) → Seminorm ℝ (E n)
  | 0 => fun _ => p 0
  | n + 1 => Fin.cases (p (n + 1)) (fun j => (transported n j).comp (L n))

theorem chain_succ_apply (n : ℕ) (x : E (n + 1)) :
    chain p L (n + 1) x = max (p (n + 1) x) (chain p L n (L n x)) := rfl

theorem baseline_le_chain (n : ℕ) : p n ≤ chain p L n := by
  cases n with
  | zero => exact le_rfl
  | succ n => exact baseline_le_saturate _ _ _

theorem chain_nonexpansive (n : ℕ) (x : E (n + 1)) :
    chain p L n (L n x) ≤ chain p L (n + 1) x :=
  pullback_le_saturate _ _ _ _

/-- Leastness only assumes compatibility through the finite prefix being tested. -/
theorem chain_minimal (r : ∀ n, Seminorm ℝ (E n)) (n : ℕ)
    (hbase : ∀ i, i ≤ n → p i ≤ r i)
    (hcomp : ∀ i, i < n → (r i).comp (L i) ≤ r (i + 1)) :
    chain p L n ≤ r n := by
  induction n with
  | zero => exact hbase 0 le_rfl
  | succ n ih =>
    apply (saturate_le_iff _ _ _ _).2
    refine ⟨hbase (n + 1) le_rfl, ?_⟩
    exact (Seminorm.comp_mono (L n)
      (ih (fun i hi => hbase i (Nat.le.step hi))
        (fun i hi => hcomp i (Nat.lt_succ_of_lt hi)))).trans (hcomp n (Nat.lt_succ_self n))

/-- A bound on the saturation is equivalent to the same bound on each transported witness. -/
theorem chain_apply_le_iff (n : ℕ) (x : E n) (a : ℝ) :
    chain p L n x ≤ a ↔ ∀ j, transported p L n j x ≤ a := by
  induction n with
  | zero => simp [chain, transported]
  | succ n ih =>
    simp only [chain_succ_apply, max_le_iff, ih, Fin.forall_fin_succ,
      transported, Fin.cases_zero, Fin.cases_succ, Seminorm.comp_apply]

/-- All transported observations are bounded exactly when the saturated seminorm is. -/
theorem chain_le_iff (n : ℕ) (r : Seminorm ℝ (E n)) :
    chain p L n ≤ r ↔ ∀ j, transported p L n j ≤ r := by
  simp only [Seminorm.le_def, chain_apply_le_iff]
  exact forall_comm

/-- AF-134's maximum over all transported witnesses, as an equality of seminorms. -/
theorem chain_eq_sup (n : ℕ) :
    chain p L n = Finset.univ.sup (transported p L n) := by
  apply le_antisymm
  · exact (chain_le_iff p L n _).2 fun j => Finset.le_sup (Finset.mem_univ j)
  · exact Finset.sup_le fun j _ => (chain_le_iff p L n _).1 le_rfl j

/-- The finite maximum is taken in nonnegative reals, then coerced to real values. -/
theorem chain_apply_eq_max (n : ℕ) (x : E n) :
    chain p L n x = (↑(Finset.univ.sup (fun j =>
      (⟨transported p L n j x, apply_nonneg _ _⟩ : ℝ≥0)) : ℝ≥0) : ℝ) := by
  rw [chain_eq_sup, Seminorm.finset_sup_apply]
  rfl

theorem chain_eq_zero_iff (n : ℕ) (x : E n) :
    chain p L n x = 0 ↔ ∀ j, transported p L n j x = 0 := by
  induction n with
  | zero => simp [chain, transported]
  | succ n ih =>
    rw [chain, saturate_eq_zero_iff, ih]
    simp only [Fin.forall_fin_succ, transported, Fin.cases_zero, Fin.cases_succ,
      Seminorm.comp_apply]

/-- The remaining blind space is exactly the intersection of all transported blind spaces. -/
theorem chain_zero_set (n : ℕ) :
    {x | chain p L n x = 0} = ⋂ j : Fin (n + 1), {x | transported p L n j x = 0} := by
  ext x
  simpa only [Set.mem_ofPred_eq, Set.mem_iInter] using chain_eq_zero_iff p L n x

end Chain

end

end Mathia.AF134
