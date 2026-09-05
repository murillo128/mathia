import Mathlib

/-!
# WI-137 Lamzouri 2/1/0 operator-distance identity

Associated finding:
`research/weil_inertia/findings/WI-137-lamzouri-slack-is-exact-quantized-operator-distance.md`

Formalized theorem boundary:
after choosing a real orthonormal basis adapted to the three orthogonal blocks `U`, `M`, and
`H`, the exact WI-126 remainder equations recombine into the squared Hilbert--Schmidt distance
from the diagonal operator with weights `2`, `1`, and `0`.  The file also proves that this target
is the sum of the coordinate projections onto `U` and `U ⊕ M`, and proves the expanded
population/horizontal form.

Not formalized:
Lamzouri's analytic proposition, the construction of the real form inside complex `L²`, the
adapted-basis and tensor-to-self-adjoint-operator bridges, the full Parseval identification of the
Bessel remainder with off-diagonal mass, or the spectral consequences of the distance identity.
Those source bridges are hypotheses of the finite theorem below.
-/

noncomputable section

open scoped BigOperators Matrix.Norms.Frobenius

namespace Mathia.WI137

/-- Coordinates of the orthogonal decomposition `W = U ⊕ M ⊕ H`. -/
abbrev BlockIndex (U M H : Type*) := U ⊕ M ⊕ H

/-- The diagonal value of the `2/1/0` target on the three adapted blocks. -/
def targetWeight {U M H : Type*} : BlockIndex U M H → ℝ
  | Sum.inl _ => 2
  | Sum.inr (Sum.inl _) => 1
  | Sum.inr (Sum.inr _) => 0

/-- Diagonal matrix of the orthogonal projection onto the first block `U`. -/
def projectionU {U M H : Type*} [DecidableEq (BlockIndex U M H)] :
    Matrix (BlockIndex U M H) (BlockIndex U M H) ℝ :=
  Matrix.diagonal fun i =>
    match i with
    | Sum.inl _ => 1
    | Sum.inr _ => 0

/-- Diagonal matrix of the orthogonal projection onto `V = U ⊕ M`. -/
def projectionV {U M H : Type*} [DecidableEq (BlockIndex U M H)] :
    Matrix (BlockIndex U M H) (BlockIndex U M H) ℝ :=
  Matrix.diagonal fun i =>
    match i with
    | Sum.inl _ => 1
    | Sum.inr (Sum.inl _) => 1
    | Sum.inr (Sum.inr _) => 0

/-- The canonical target: `2` on `U`, `1` on `M`, and `0` on `H`. -/
def quantizedTarget {U M H : Type*} [DecidableEq (BlockIndex U M H)] :
    Matrix (BlockIndex U M H) (BlockIndex U M H) ℝ :=
  Matrix.diagonal targetWeight

/-- In adapted coordinates, `P_U + P_V` is exactly the `2/1/0` target. -/
theorem projectionU_add_projectionV {U M H : Type*}
    [DecidableEq (BlockIndex U M H)] :
    projectionU (U := U) (M := M) (H := H) + projectionV = quantizedTarget := by
  ext i j
  by_cases hij : i = j
  · subst j
    rcases i with u | mh
    · norm_num [projectionU, projectionV, quantizedTarget, targetWeight]
    · rcases mh with m | h
      · simp [projectionU, projectionV, quantizedTarget, targetWeight]
      · simp [projectionU, projectionV, quantizedTarget, targetWeight]
  · simp [projectionU, projectionV, quantizedTarget, hij]

/-- The diagonal coefficient of an operator matrix in the adapted basis. -/
def diagonalCoeff {I : Type*} (A : Matrix I I ℝ) (i : I) : ℝ :=
  A i i

/-- Squared Hilbert--Schmidt mass in finite real orthonormal coordinates. -/
def hilbertSchmidtSq {I : Type*} [Fintype I] (A : Matrix I I ℝ) : ℝ :=
  ∑ i, ∑ j, (A i j) ^ 2

/-- The preceding coordinate sum is the square of Mathlib's Frobenius matrix norm. -/
theorem hilbertSchmidtSq_eq_frobenius_norm_sq {I : Type*} [Fintype I]
    (A : Matrix I I ℝ) :
    hilbertSchmidtSq A = ‖A‖ ^ 2 := by
  change (∑ i, ∑ j, (A i j) ^ 2) = ‖A‖ ^ 2
  rw [Matrix.frobenius_norm_def, ← Real.sqrt_eq_rpow, Real.sq_sqrt]
  · simp only [Real.rpow_two, Real.norm_eq_abs, sq_abs]
  · positivity

/-- Full ordered-pair off-diagonal Hilbert--Schmidt mass. -/
def offDiagonalSq {I : Type*} [Fintype I] [DecidableEq I]
    (A : Matrix I I ℝ) : ℝ :=
  ∑ i, ∑ j, if i = j then 0 else (A i j) ^ 2

/-- The completed-square contribution of the `U` diagonal block. -/
def uTargetSq {U M H : Type*} [Fintype U]
    (A : Matrix (BlockIndex U M H) (BlockIndex U M H) ℝ) : ℝ :=
  ∑ u, (diagonalCoeff A (Sum.inl u) - 2) ^ 2

/-- The completed-square contribution of the middle block `M = V ⊖ U`. -/
def middleRemainder {U M H : Type*} [Fintype M]
    (A : Matrix (BlockIndex U M H) (BlockIndex U M H) ℝ) : ℝ :=
  ∑ m, (diagonalCoeff A (Sum.inr (Sum.inl m)) - 1) ^ 2

/-- The square contribution of the horizontal block `H = W ⊖ V`. -/
def hTargetSq {U M H : Type*} [Fintype H]
    (A : Matrix (BlockIndex U M H) (BlockIndex U M H) ℝ) : ℝ :=
  ∑ h, (diagonalCoeff A (Sum.inr (Sum.inr h))) ^ 2

/-- WI-126's uncompleted `U`-block remainder. -/
def uRemainder {U M H : Type*} [Fintype U]
    (A : Matrix (BlockIndex U M H) (BlockIndex U M H) ℝ) : ℝ :=
  ∑ u, ((diagonalCoeff A (Sum.inl u)) ^ 2 - 2 * diagonalCoeff A (Sum.inl u))

/-- WI-126's uncompleted horizontal-block remainder. -/
def hRemainder {U M H : Type*} [Fintype H]
    (A : Matrix (BlockIndex U M H) (BlockIndex U M H) ℝ) : ℝ :=
  ∑ h, ((diagonalCoeff A (Sum.inr (Sum.inr h))) ^ 2 -
    2 * diagonalCoeff A (Sum.inr (Sum.inr h)))

/-- The exact `U`-coefficient excess `Σ_U α - 2 dim(U)`. -/
def uExcess {U M H : Type*} [Fintype U]
    (A : Matrix (BlockIndex U M H) (BlockIndex U M H) ℝ) : ℝ :=
  ∑ u, diagonalCoeff A (Sum.inl u) - 2 * (Fintype.card U : ℝ)

/-- The signed horizontal diagonal sum appearing in WI-126. -/
def horizontalSum {U M H : Type*} [Fintype H]
    (A : Matrix (BlockIndex U M H) (BlockIndex U M H) ℝ) : ℝ :=
  ∑ h, -diagonalCoeff A (Sum.inr (Sum.inr h))

private theorem uRemainder_eq {U M H : Type*} [Fintype U]
    (A : Matrix (BlockIndex U M H) (BlockIndex U M H) ℝ) :
    uRemainder A = uTargetSq A + 2 * uExcess A := by
  rw [uRemainder, uTargetSq, uExcess]
  calc
    (∑ u, (diagonalCoeff A (Sum.inl u) ^ 2 - 2 * diagonalCoeff A (Sum.inl u))) =
        ∑ u, ((diagonalCoeff A (Sum.inl u) - 2) ^ 2 +
          2 * (diagonalCoeff A (Sum.inl u) - 2)) := by
      apply Finset.sum_congr rfl
      intro u hu
      ring
    _ = (∑ u, (diagonalCoeff A (Sum.inl u) - 2) ^ 2) +
        2 * ((∑ u, diagonalCoeff A (Sum.inl u)) - 2 * (Fintype.card U : ℝ)) := by
      simp only [Finset.sum_add_distrib]
      rw [← Finset.mul_sum]
      simp only [Finset.sum_sub_distrib, Finset.sum_const, nsmul_eq_mul, Finset.card_univ]
      ring

private theorem hRemainder_eq {U M H : Type*} [Fintype H]
    (A : Matrix (BlockIndex U M H) (BlockIndex U M H) ℝ) :
    hRemainder A = hTargetSq A + 2 * horizontalSum A := by
  rw [hRemainder, hTargetSq, horizontalSum]
  calc
    (∑ h, (diagonalCoeff A (Sum.inr (Sum.inr h)) ^ 2 -
        2 * diagonalCoeff A (Sum.inr (Sum.inr h)))) =
        ∑ h, (diagonalCoeff A (Sum.inr (Sum.inr h)) ^ 2 +
          2 * (-diagonalCoeff A (Sum.inr (Sum.inr h)))) := by
      apply Finset.sum_congr rfl
      intro h hh
      ring
    _ = (∑ h, diagonalCoeff A (Sum.inr (Sum.inr h)) ^ 2) +
        2 * ∑ h, -diagonalCoeff A (Sum.inr (Sum.inr h)) := by
      rw [Finset.sum_add_distrib, Finset.mul_sum]

private theorem hilbertSchmidtSq_sub_diagonal {I : Type*} [Fintype I] [DecidableEq I]
    (A : Matrix I I ℝ) (d : I → ℝ) :
    hilbertSchmidtSq (A - Matrix.diagonal d) =
      offDiagonalSq A + ∑ i, (diagonalCoeff A i - d i) ^ 2 := by
  rw [hilbertSchmidtSq, offDiagonalSq]
  rw [← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro i hi
  have hdiag :
      (diagonalCoeff A i - d i) ^ 2 =
        ∑ j, if i = j then (diagonalCoeff A i - d i) ^ 2 else 0 := by
    simp
  rw [hdiag, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro j hj
  by_cases hij : i = j
  · subst j
    simp [diagonalCoeff]
  · simp [hij]

/-- Entrywise completion of squares for the canonical `2/1/0` target. -/
theorem hilbertSchmidtSq_sub_quantizedTarget {U M H : Type*}
    [Fintype U] [Fintype M] [Fintype H]
    [DecidableEq U] [DecidableEq M] [DecidableEq H]
    (A : Matrix (BlockIndex U M H) (BlockIndex U M H) ℝ) :
    hilbertSchmidtSq (A - quantizedTarget) =
      offDiagonalSq A + uTargetSq A + middleRemainder A + hTargetSq A := by
  rw [quantizedTarget, hilbertSchmidtSq_sub_diagonal]
  simp only [Fintype.sum_sum_type]
  simp [targetWeight, diagonalCoeff, uTargetSq, middleRemainder, hTargetSq]
  ring

/-- Exact WI-137 normal form in a finite real adapted basis.

The Hermitian hypothesis records that `A` is the matrix of the source self-adjoint operator.  The
completion-of-squares argument itself does not need symmetry. -/
theorem operatorDistanceIdentity {U M H : Type*}
    [Fintype U] [Fintype M] [Fintype H]
    [DecidableEq U] [DecidableEq M] [DecidableEq H]
    (A : Matrix (BlockIndex U M H) (BlockIndex U M H) ℝ)
    (_hA : A.IsHermitian)
    (Δ R_B R_U R_M R_H B H_V : ℝ)
    (hΔ : Δ = R_B + R_U + R_M + R_H)
    (hRB : R_B = offDiagonalSq A)
    (hRU : R_U = uRemainder A)
    (hRM : R_M = middleRemainder A)
    (hRH : R_H = hRemainder A)
    (hB : B = uExcess A)
    (hHV : horizontalSum A = 2 * H_V) :
    Δ = ‖A - quantizedTarget‖ ^ 2 + 2 * B + 4 * H_V := by
  calc
    Δ = offDiagonalSq A + uRemainder A + middleRemainder A + hRemainder A := by
      rw [hΔ, hRB, hRU, hRM, hRH]
    _ = (offDiagonalSq A + uTargetSq A + middleRemainder A + hTargetSq A) +
        2 * B + 4 * H_V := by
      rw [uRemainder_eq, hRemainder_eq, ← hB, hHV]
      ring
    _ = ‖A - quantizedTarget‖ ^ 2 + 2 * B + 4 * H_V := by
      rw [← hilbertSchmidtSq_sub_quantizedTarget,
        hilbertSchmidtSq_eq_frobenius_norm_sq]

/-- The expanded WI-137 identity after substituting WI-126's exact formula for `B`. -/
theorem operatorDistanceIdentity_expanded {U M H : Type*}
    [Fintype U] [Fintype M] [Fintype H]
    [DecidableEq U] [DecidableEq M] [DecidableEq H]
    (A : Matrix (BlockIndex U M H) (BlockIndex U M H) ℝ)
    (hA : A.IsHermitian)
    (Δ R_B R_U R_M R_H B H_V S₁ E_R E_C H_U : ℝ)
    (hΔ : Δ = R_B + R_U + R_M + R_H)
    (hRB : R_B = offDiagonalSq A)
    (hRU : R_U = uRemainder A)
    (hRM : R_M = middleRemainder A)
    (hRH : R_H = hRemainder A)
    (hB : B = uExcess A)
    (hHV : horizontalSum A = 2 * H_V)
    (hBExpanded : B = S₁ + E_R + 2 * E_C + 2 * H_U) :
    Δ = ‖A - quantizedTarget‖ ^ 2 +
      2 * S₁ + 2 * E_R + 4 * E_C + 4 * H_U + 4 * H_V := by
  rw [operatorDistanceIdentity A hA Δ R_B R_U R_M R_H B H_V
    hΔ hRB hRU hRM hRH hB hHV, hBExpanded]
  ring

#print axioms projectionU_add_projectionV
#print axioms hilbertSchmidtSq_sub_quantizedTarget
#print axioms operatorDistanceIdentity
#print axioms operatorDistanceIdentity_expanded

end Mathia.WI137
