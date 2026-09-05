import WI137OperatorDistance

/-!
# WI-168 same-deficit quantized flag rank budget

Associated finding:
`research/weil_inertia/findings/WI-168-same-deficit-quantized-flag-rank-is-at-most-four-delta.md`

Formalized theorem boundary:
for finite real matrices, `Δ = ‖X‖²_HS + L` and `‖X - J‖²_HS ≤ Δ` imply the exact
midpoint budget `‖X - J/2‖²_HS + ‖J‖²_HS/4 + L/2 ≤ Δ`. With `L ≥ 0`, equality in
the coarse energy bound forces `L = 0` and `X = J/2`. A diagonal operator whose nonzero
entries have squared magnitude at least one has rank at most its squared HS mass.
In particular, natural-number depths have mass `∑ i, q(i)²`, support cardinality equal
to matrix rank, and rank at most `4Δ`; a nonzero depth operator requires `Δ ≥ 1/4`.
The HS convention is exactly `Mathia.WI137.hilbertSchmidtSq`, already identified with
the squared Frobenius norm. No symmetry, positivity, or nestedness is needed for the
midpoint theorem; the diagonal floor lemma isolates the hypothesis used for rank.

Not formalized:
the zeta/source bridge, Lamzouri's analytic proposition, the derivation of the source
normal form, or the assertion that an actual candidate flag is same-deficit-funded.
The normal form and same-deficit inequality remain explicit premises. A nested flag
is represented by its depths in a common orthonormal coordinate basis; construction
of that basis from nested projections and the asymptotic zero-population consequences
remain outside Lean. No novelty is claimed for the underlying matrix algebra.
-/

noncomputable section

open scoped BigOperators Matrix.Norms.Frobenius
open Mathia.WI137

namespace Mathia.WI168

variable {I : Type*} [Fintype I]

theorem hilbertSchmidtSq_nonneg (A : Matrix I I ℝ) : 0 ≤ hilbertSchmidtSq A := by
  unfold hilbertSchmidtSq
  positivity

theorem hilbertSchmidtSq_eq_zero_iff (A : Matrix I I ℝ) :
    hilbertSchmidtSq A = 0 ↔ A = 0 := by
  rw [hilbertSchmidtSq_eq_frobenius_norm_sq, sq_eq_zero_iff, norm_eq_zero]

/-- The exact parallelogram identity in WI-137's finite HS convention. -/
theorem midpoint_identity (X J : Matrix I I ℝ) :
    hilbertSchmidtSq X + hilbertSchmidtSq (X - J) =
      2 * hilbertSchmidtSq (X - (1 / 2 : ℝ) • J) +
        (1 / 2 : ℝ) * hilbertSchmidtSq J := by
  simp only [hilbertSchmidtSq, Matrix.sub_apply, Matrix.smul_apply, smul_eq_mul,
    Finset.mul_sum, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro i hi
  apply Finset.sum_congr rfl
  intro j hj
  ring

/-- Same-deficit funding is a premise, not a conclusion about source-derived flags.
The exact midpoint estimate itself does not require a sign assumption on `L`. -/
theorem midpoint_budget (X J : Matrix I I ℝ) (Δ L : ℝ)
    (hΔ : Δ = hilbertSchmidtSq X + L)
    (hfund : hilbertSchmidtSq (X - J) ≤ Δ) :
    hilbertSchmidtSq (X - (1 / 2 : ℝ) • J) +
      (1 / 4 : ℝ) * hilbertSchmidtSq J + L / 2 ≤ Δ := by
  linarith [midpoint_identity X J]

/-- The coarse budget discards midpoint error and the nonnegative source charge. -/
theorem energy_le_four_deficit (X J : Matrix I I ℝ) (Δ L : ℝ)
    (hL : 0 ≤ L) (hΔ : Δ = hilbertSchmidtSq X + L)
    (hfund : hilbertSchmidtSq (X - J) ≤ Δ) :
    hilbertSchmidtSq J ≤ 4 * Δ := by
  have hmid := midpoint_budget X J Δ L hΔ hfund
  have hnonneg := hilbertSchmidtSq_nonneg (X - (1 / 2 : ℝ) • J)
  linarith

/-- Equality at the sharp quarter-energy threshold forces midpoint rigidity. -/
theorem coarse_equality (X J : Matrix I I ℝ) (Δ L : ℝ)
    (hL : 0 ≤ L) (hΔ : Δ = hilbertSchmidtSq X + L)
    (hfund : hilbertSchmidtSq (X - J) ≤ Δ)
    (heq : Δ = (1 / 4 : ℝ) * hilbertSchmidtSq J) :
    L = 0 ∧ X = (1 / 2 : ℝ) • J := by
  have hmid := midpoint_budget X J Δ L hΔ hfund
  have hnonneg := hilbertSchmidtSq_nonneg (X - (1 / 2 : ℝ) • J)
  have hz : hilbertSchmidtSq (X - (1 / 2 : ℝ) • J) = 0 := by linarith
  exact ⟨by linarith, sub_eq_zero.mp ((hilbertSchmidtSq_eq_zero_iff _).mp hz)⟩

variable [DecidableEq I]

/-- Diagonal HS energy retains the full squared depth, before rank relaxation. -/
theorem hilbertSchmidtSq_diagonal (d : I → ℝ) :
    hilbertSchmidtSq (Matrix.diagonal d) = ∑ i, (d i) ^ 2 := by
  classical
  simp [hilbertSchmidtSq, Matrix.diagonal_apply]

/-- A diagonal spectral floor suffices; signs and integer quantization are unnecessary. -/
theorem diagonal_rank_le_energy (d : I → ℝ)
    (hfloor : ∀ i, d i ≠ 0 → 1 ≤ (d i) ^ 2) :
    ((Matrix.diagonal d).rank : ℝ) ≤ hilbertSchmidtSq (Matrix.diagonal d) := by
  classical
  rw [Matrix.rank_diagonal, Fintype.card_subtype, hilbertSchmidtSq_diagonal]
  rw [← Finset.sum_boole]
  apply Finset.sum_le_sum
  intro i hi
  by_cases h : d i = 0
  · simp [h]
  · simpa [h] using hfloor i h

/-- The rank budget for any real diagonal target with the unit squared spectral floor. -/
theorem diagonal_rank_budget (X : Matrix I I ℝ) (d : I → ℝ) (Δ L : ℝ)
    (hfloor : ∀ i, d i ≠ 0 → 1 ≤ (d i) ^ 2)
    (hL : 0 ≤ L) (hΔ : Δ = hilbertSchmidtSq X + L)
    (hfund : hilbertSchmidtSq (X - Matrix.diagonal d) ≤ Δ) :
    ((Matrix.diagonal d).rank : ℝ) ≤ 4 * Δ :=
  (diagonal_rank_le_energy d hfloor).trans
    (energy_le_four_deficit X (Matrix.diagonal d) Δ L hL hΔ hfund)

/-- A finite quantized flag in a common orthonormal coordinate basis. -/
def depthOperator (q : I → ℕ) : Matrix I I ℝ :=
  Matrix.diagonal fun i => (q i : ℝ)

theorem depth_energy (q : I → ℕ) :
    hilbertSchmidtSq (depthOperator q) = ∑ i, (q i : ℝ) ^ 2 :=
  hilbertSchmidtSq_diagonal _

/-- The support count is proved equal to matrix rank, not merely named rank. -/
theorem depth_rank_eq_support (q : I → ℕ) :
    (depthOperator q).rank = Fintype.card {i // 0 < q i} := by
  classical
  rw [depthOperator, Matrix.rank_diagonal]
  simp only [Nat.cast_ne_zero, Nat.pos_iff_ne_zero]

omit [Fintype I] [DecidableEq I] in
private theorem depth_floor (q : I → ℕ) (i : I) (h : (q i : ℝ) ≠ 0) :
    1 ≤ (q i : ℝ) ^ 2 := by
  have hn : 1 ≤ q i := Nat.one_le_iff_ne_zero.mpr (by exact_mod_cast h)
  have hr : (1 : ℝ) ≤ q i := by exact_mod_cast hn
  nlinarith

/-- Depth-weighted energy and its full rank/support relaxation under the same deficit. -/
theorem quantized_budget (X : Matrix I I ℝ) (q : I → ℕ) (Δ L : ℝ)
    (hL : 0 ≤ L) (hΔ : Δ = hilbertSchmidtSq X + L)
    (hfund : hilbertSchmidtSq (X - depthOperator q) ≤ Δ) :
    (Fintype.card {i // 0 < q i} : ℝ) ≤ ∑ i, (q i : ℝ) ^ 2 ∧
      (∑ i, (q i : ℝ) ^ 2) ≤ 4 * Δ := by
  constructor
  · rw [← depth_rank_eq_support, ← depth_energy]
    exact diagonal_rank_le_energy _ (depth_floor q)
  · rw [← depth_energy]
    exact energy_le_four_deficit X (depthOperator q) Δ L hL hΔ hfund

theorem quantized_rank_budget (X : Matrix I I ℝ) (q : I → ℕ) (Δ L : ℝ)
    (hL : 0 ≤ L) (hΔ : Δ = hilbertSchmidtSq X + L)
    (hfund : hilbertSchmidtSq (X - depthOperator q) ≤ Δ) :
    ((depthOperator q).rank : ℝ) ≤ 4 * Δ :=
  diagonal_rank_budget X _ Δ L (depth_floor q) hL hΔ hfund

/-- Any nonzero same-deficit quantized extension consumes at least a quarter unit. -/
theorem nonzero_depth_budget (X : Matrix I I ℝ) (q : I → ℕ) (Δ L : ℝ)
    (hL : 0 ≤ L) (hΔ : Δ = hilbertSchmidtSq X + L)
    (hfund : hilbertSchmidtSq (X - depthOperator q) ≤ Δ)
    (hne : depthOperator q ≠ 0) : (1 / 4 : ℝ) ≤ Δ := by
  have hex : ∃ i, 0 < q i := by
    by_contra! hall
    apply hne
    have hq : q = 0 := funext fun i => Nat.eq_zero_of_le_zero (hall i)
    simp [depthOperator, hq]
  have hpos : 0 < (depthOperator q).rank := by
    rw [depth_rank_eq_support, Fintype.card_pos_iff]
    obtain ⟨i, hi⟩ := hex
    exact ⟨⟨i, hi⟩⟩
  have hone : (1 : ℝ) ≤ (depthOperator q).rank := by exact_mod_cast hpos
  have hbound := quantized_rank_budget X q Δ L hL hΔ hfund
  linarith

#print axioms midpoint_identity
#print axioms midpoint_budget
#print axioms energy_le_four_deficit
#print axioms coarse_equality
#print axioms diagonal_rank_le_energy
#print axioms diagonal_rank_budget
#print axioms depth_energy
#print axioms depth_rank_eq_support
#print axioms quantized_budget
#print axioms quantized_rank_budget
#print axioms nonzero_depth_budget

end Mathia.WI168
