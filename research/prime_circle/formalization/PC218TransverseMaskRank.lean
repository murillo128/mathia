import Mathlib.Analysis.InnerProductSpace.Adjoint
import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.RingTheory.Polynomial.Cyclotomic.Eval
import Mathlib.Tactic

/-!
# PC-218: transverse-mask rank and cyclotomic coefficient sparsity

Associated finding:
`research/prime_circle/findings/PC-218-full-transverse-mask-nullity-equals-cyclotomic-zero-count.md`

Formalized theorem boundary:
Lean verifies only the finite rank/nullity theorem and its explicit algebraic bridge: the finite
signed-compression kernel mechanism, the unique cyclotomic relation among primitive-root evaluation
rows, and the resulting exact rank/nullity formula for the canonical finite transverse matrix.

Not formalized:
the surviving nonzero spectrum, inertia, singular values, cross-level asymptotics, or any RH-facing
consequence.
-/

noncomputable section

open scoped BigOperators ComplexConjugate ComplexOrder Matrix

namespace Mathia.PC218

section SignedCompression

variable {S U : Type*} [Fintype S] [DecidableEq S] [Fintype U]

/-- An indefinite diagonal compression has no extra kernel when its sole left relation is sent
from a vector nonorthogonal to that relation. -/
theorem signedCompression_ker_eq
    (A : Matrix S U ℂ) (d a e : S → ℂ)
    (hker : LinearMap.ker A.conjTranspose.mulVecLin = ℂ ∙ a)
    (hd : ∀ i, d i ≠ 0)
    (hde : ∀ i, d i * e i = a i)
    (hanchor : star a ⬝ᵥ e ≠ 0) :
    LinearMap.ker (A.conjTranspose * Matrix.diagonal d * A).mulVecLin =
      LinearMap.ker A.mulVecLin := by
  ext x
  simp only [LinearMap.mem_ker, Matrix.mulVecLin_apply]
  constructor
  · intro hx
    have hz : (A.conjTranspose) *ᵥ (Matrix.diagonal d *ᵥ (A *ᵥ x)) = 0 := by
      simpa only [Matrix.mulVec_mulVec, Matrix.mul_assoc] using hx
    have hzmem : Matrix.diagonal d *ᵥ (A *ᵥ x) ∈
        LinearMap.ker A.conjTranspose.mulVecLin := hz
    rw [hker, Submodule.mem_span_singleton] at hzmem
    obtain ⟨c, hc⟩ := hzmem
    have hy : A *ᵥ x = c • e := by
      funext i
      have hi := congr_fun hc i
      simp only [Matrix.mulVec_diagonal, Pi.smul_apply, smul_eq_mul] at hi
      rw [← hde i] at hi
      apply (mul_left_cancel₀ (hd i))
      simpa [mul_assoc, mul_comm, mul_left_comm] using hi.symm
    have ha_mem : a ∈ LinearMap.ker A.conjTranspose.mulVecLin := by
      rw [hker]
      exact Submodule.mem_span_singleton_self a
    have ha_zero : (A.conjTranspose) *ᵥ a = 0 := ha_mem
    have hrow : star a ᵥ* A = 0 := by
      rw [Matrix.mulVec_conjTranspose] at ha_zero
      apply_fun star at ha_zero
      simpa using ha_zero
    have horth : star a ⬝ᵥ (A *ᵥ x) = 0 := by
      rw [Matrix.dotProduct_mulVec, hrow, zero_dotProduct]
    rw [hy] at horth
    have hcprod : c * (star a ⬝ᵥ e) = 0 := by
      simpa [dotProduct, Finset.mul_sum, mul_comm, mul_left_comm, mul_assoc] using horth
    have hc : c = 0 := (mul_eq_zero.mp hcprod).resolve_right hanchor
    simp [hy, hc]
  · intro hx
    rw [← Matrix.mulVec_mulVec, hx, Matrix.mulVec_zero]

/-- Rank is preserved by the same signed-compression hypotheses. -/
theorem signedCompression_rank_eq
    (A : Matrix S U ℂ) (d a e : S → ℂ)
    (hker : LinearMap.ker A.conjTranspose.mulVecLin = ℂ ∙ a)
    (hd : ∀ i, d i ≠ 0)
    (hde : ∀ i, d i * e i = a i)
    (hanchor : star a ⬝ᵥ e ≠ 0) :
    (A.conjTranspose * Matrix.diagonal d * A).rank = A.rank := by
  rw [Matrix.rank, Matrix.rank]
  have hleft := LinearMap.finrank_range_add_finrank_ker
    (A.conjTranspose * Matrix.diagonal d * A).mulVecLin
  have hright := LinearMap.finrank_range_add_finrank_ker A.mulVecLin
  rw [signedCompression_ker_eq A d a e hker hd hde hanchor] at hleft
  omega

end SignedCompression

section CyclotomicEvaluation

/-- Primitive complex roots of exact order `n`, used directly as Fourier frequencies. -/
abbrev PrimitiveFrequency (n : ℕ) := ↑(primitiveRoots n ℂ)

/-- The nonzero coefficient positions of the complex cyclotomic polynomial. -/
abbrev CyclotomicSupport (n : ℕ) := ↑(Polynomial.cyclotomic n ℂ).support

/-- The cyclotomic coefficient vector after zero coefficients have been removed. -/
def coeffVector (n : ℕ) : CyclotomicSupport n → ℂ :=
  fun r ↦ (Polynomial.cyclotomic n ℂ).coeff r

/-- The primitive-root evaluation frame.  The conjugated-root convention makes its adjoint the
ordinary polynomial evaluation map; reversing this convention only conjugates the final matrix. -/
def evaluationMatrix (n : ℕ) : Matrix (CyclotomicSupport n) (PrimitiveFrequency n) ℂ :=
  fun r z ↦ star (z : ℂ) ^ (r : ℕ)

/-- Reconstruct a polynomial from coordinates on the cyclotomic support. -/
def supportPolynomial (n : ℕ) (c : CyclotomicSupport n → ℂ) : Polynomial ℂ :=
  ∑ r : CyclotomicSupport n, Polynomial.monomial (r : ℕ) (c r)

@[simp] lemma supportPolynomial_coeff (n : ℕ) (c : CyclotomicSupport n → ℂ)
    (r : CyclotomicSupport n) :
    (supportPolynomial n c).coeff r = c r := by
  classical
  simp [supportPolynomial, Polynomial.coeff_monomial]

lemma supportPolynomial_coeff_of_not_mem (n : ℕ) (c : CyclotomicSupport n → ℂ)
    {k : ℕ} (hk : k ∉ (Polynomial.cyclotomic n ℂ).support) :
    (supportPolynomial n c).coeff k = 0 := by
  classical
  rw [supportPolynomial]
  change Polynomial.lcoeff ℂ k (∑ r : CyclotomicSupport n,
    Polynomial.monomial (r : ℕ) (c r)) = 0
  rw [map_sum]
  change (∑ r : CyclotomicSupport n,
    (Polynomial.monomial (r : ℕ) (c r)).coeff k) = 0
  simp only [Polynomial.coeff_monomial]
  apply Finset.sum_eq_zero
  intro r _
  by_cases hr : (r : ℕ) = k
  · exact (hk (hr ▸ r.property)).elim
  · simp [hr]

lemma supportPolynomial_natDegree_le (n : ℕ) (c : CyclotomicSupport n → ℂ) :
    (supportPolynomial n c).natDegree ≤ Nat.totient n := by
  rw [Polynomial.natDegree_le_iff_coeff_eq_zero]
  intro k hk
  apply supportPolynomial_coeff_of_not_mem
  intro hmem
  have hle := Polynomial.le_natDegree_of_ne_zero
    (Polynomial.mem_support_iff.mp hmem)
  rw [Polynomial.natDegree_cyclotomic] at hle
  omega

@[simp] lemma supportPolynomial_eval (n : ℕ) (c : CyclotomicSupport n → ℂ) (z : ℂ) :
    (supportPolynomial n c).eval z = ∑ r, c r * z ^ (r : ℕ) := by
  classical
  rw [supportPolynomial]
  change Polynomial.evalRingHom z (∑ r : CyclotomicSupport n,
    Polynomial.monomial (r : ℕ) (c r)) = _
  rw [map_sum]
  simp

@[simp] lemma supportPolynomial_smul (n : ℕ) (s : ℂ)
    (c : CyclotomicSupport n → ℂ) :
    supportPolynomial n (s • c) = s • supportPolynomial n c := by
  classical
  simp [supportPolynomial, Finset.smul_sum, Polynomial.smul_monomial]

lemma supportPolynomial_coeffVector (n : ℕ) :
    supportPolynomial n (coeffVector n) = Polynomial.cyclotomic n ℂ := by
  classical
  ext k
  by_cases hk : k ∈ (Polynomial.cyclotomic n ℂ).support
  · let r : CyclotomicSupport n := ⟨k, hk⟩
    simpa [r, coeffVector] using supportPolynomial_coeff n (coeffVector n) r
  · rw [supportPolynomial_coeff_of_not_mem n (coeffVector n) hk]
    exact (Polynomial.notMem_support_iff.mp hk).symm

lemma evaluationMatrix_conjTranspose_mulVec (n : ℕ)
    (c : CyclotomicSupport n → ℂ) (z : PrimitiveFrequency n) :
    (evaluationMatrix n).conjTranspose.mulVec c z =
      (supportPolynomial n c).eval (z : ℂ) := by
  classical
  simp [evaluationMatrix, Matrix.mulVec, supportPolynomial_eval, dotProduct, mul_comm]

lemma totient_mem_cyclotomicSupport (n : ℕ) :
    Nat.totient n ∈ (Polynomial.cyclotomic n ℂ).support := by
  rw [Polynomial.mem_support_iff]
  rw [← Polynomial.natDegree_cyclotomic n ℂ,
    (Polynomial.cyclotomic.monic n ℂ).coeff_natDegree]
  exact one_ne_zero

private lemma primitive_isRoot {n : ℕ} (hn : 0 < n) (z : PrimitiveFrequency n) :
    (Polynomial.cyclotomic n ℂ).eval (z : ℂ) = 0 := by
  rw [← Polynomial.IsRoot.def,
    Polynomial.isRoot_cyclotomic_iff_charZero hn]
  exact isPrimitiveRoot_of_mem_primitiveRoots z.property

/-- The only coefficient relation that vanishes on all primitive roots is the cyclotomic one. -/
theorem evaluationMatrix_leftKernel {n : ℕ} (hn : 1 < n) :
    LinearMap.ker (evaluationMatrix n).conjTranspose.mulVecLin = ℂ ∙ coeffVector n := by
  classical
  ext c
  rw [Submodule.mem_span_singleton]
  constructor
  · intro hc
    have hzero : ∀ z : PrimitiveFrequency n,
        (supportPolynomial n c).eval (z : ℂ) = 0 := by
      intro z
      rw [← evaluationMatrix_conjTranspose_mulVec]
      exact congr_fun (LinearMap.mem_ker.mp hc) z
    let top : CyclotomicSupport n := ⟨Nat.totient n, totient_mem_cyclotomicSupport n⟩
    let q : Polynomial ℂ :=
      supportPolynomial n c - c top • Polynomial.cyclotomic n ℂ
    have hqeval : ∀ z : PrimitiveFrequency n, q.eval (z : ℂ) = 0 := by
      intro z
      simp [q, hzero z, primitive_isRoot (Nat.zero_lt_of_lt hn) z]
    have hqle : q.natDegree ≤ Nat.totient n := by
      dsimp only [q]
      exact (Polynomial.natDegree_sub_le _ _).trans <| max_le
        (supportPolynomial_natDegree_le n c)
        ((Polynomial.natDegree_smul_le _ _).trans_eq
          (Polynomial.natDegree_cyclotomic n ℂ))
    have hqcoeff : q.coeff (Nat.totient n) = 0 := by
      dsimp only [q]
      rw [Polynomial.coeff_sub]
      change (supportPolynomial n c).coeff (top : ℕ) -
        c top * (Polynomial.cyclotomic n ℂ).coeff (top : ℕ) = 0
      rw [supportPolynomial_coeff]
      have htop : (Polynomial.cyclotomic n ℂ).coeff (top : ℕ) = 1 := by
        change (Polynomial.cyclotomic n ℂ).coeff (Nat.totient n) = 1
        rw [← Polynomial.natDegree_cyclotomic n ℂ,
          (Polynomial.cyclotomic.monic n ℂ).coeff_natDegree]
      rw [htop, mul_one, sub_self]
    have hqdeg : q.natDegree < Nat.totient n := by
      by_cases hq : q = 0
      · simp [hq, Nat.totient_pos.mpr (Nat.zero_lt_of_lt hn)]
      · have hlead : q.coeff q.natDegree ≠ 0 := by
          rw [Polynomial.coeff_natDegree]
          exact Polynomial.leadingCoeff_ne_zero.mpr hq
        exact lt_of_le_of_ne hqle fun heq ↦ hlead (heq ▸ hqcoeff)
    have hqzero : q = 0 :=
      Polynomial.eq_zero_of_natDegree_lt_card_of_eval_eq_zero q
        Subtype.val_injective hqeval (by
          simpa [Fintype.card_coe, Complex.card_primitiveRoots] using hqdeg)
    have hpoly : supportPolynomial n c = c top • Polynomial.cyclotomic n ℂ :=
      sub_eq_zero.mp hqzero
    refine ⟨c top, ?_⟩
    funext r
    have hr := congrArg (fun p : Polynomial ℂ ↦ p.coeff (r : ℕ)) hpoly
    simpa [coeffVector] using hr.symm
  · rintro ⟨s, rfl⟩
    rw [LinearMap.mem_ker]
    change (evaluationMatrix n).conjTranspose.mulVec (s • coeffVector n) = 0
    funext z
    rw [evaluationMatrix_conjTranspose_mulVec, supportPolynomial_smul,
      supportPolynomial_coeffVector]
    simp [primitive_isRoot (Nat.zero_lt_of_lt hn) z]

lemma coeffVector_ne_zero (n : ℕ) : coeffVector n ≠ 0 := by
  intro h
  let top : CyclotomicSupport n := ⟨Nat.totient n, totient_mem_cyclotomicSupport n⟩
  have htop := congr_fun h top
  have hcoeff : (Polynomial.cyclotomic n ℂ).coeff (top : ℕ) = 1 := by
    change (Polynomial.cyclotomic n ℂ).coeff (Nat.totient n) = 1
    rw [← Polynomial.natDegree_cyclotomic n ℂ,
      (Polynomial.cyclotomic.monic n ℂ).coeff_natDegree]
  simp [coeffVector, hcoeff] at htop

lemma eval_one_cyclotomic_ne_zero {n : ℕ} (hn : 1 < n) :
    (Polynomial.cyclotomic n ℂ).eval 1 ≠ 0 := by
  intro hzero
  have hroot : (Polynomial.cyclotomic n ℂ).IsRoot 1 := hzero
  have hprim : IsPrimitiveRoot (1 : ℂ) n :=
    (Polynomial.isRoot_cyclotomic_iff_charZero (Nat.zero_lt_of_lt hn)).mp hroot
  have horder := hprim.eq_orderOf
  have hn_one : n = 1 := horder.trans orderOf_one
  exact hn.ne hn_one.symm

lemma coeffVector_anchor_ne_zero {n : ℕ} (hn : 1 < n) :
    star (coeffVector n) ⬝ᵥ (fun _ ↦ (1 : ℂ)) ≠ 0 := by
  have hsum : (∑ r : CyclotomicSupport n, coeffVector n r) ≠ 0 := by
    intro hzero
    apply eval_one_cyclotomic_ne_zero hn
    rw [← supportPolynomial_coeffVector n, supportPolynomial_eval]
    simpa using hzero
  intro hzero
  apply hsum
  apply_fun star at hzero
  simpa [dotProduct] using hzero

/-- The unnormalized signed Gram matrix in primitive-frequency coordinates. -/
def signedGram (n : ℕ) : Matrix (PrimitiveFrequency n) (PrimitiveFrequency n) ℂ :=
  (evaluationMatrix n).conjTranspose * Matrix.diagonal (coeffVector n) * evaluationMatrix n

/-- The cyclotomic coefficient diagonal creates no kernel beyond the evaluation kernel. -/
theorem signedGram_ker_eq {n : ℕ} (hn : 1 < n) :
    LinearMap.ker (signedGram n).mulVecLin =
      LinearMap.ker (evaluationMatrix n).mulVecLin := by
  apply signedCompression_ker_eq (evaluationMatrix n) (coeffVector n) (coeffVector n)
    (fun _ ↦ (1 : ℂ)) (evaluationMatrix_leftKernel hn)
  · intro r
    exact Polynomial.mem_support_iff.mp r.property
  · intro r
    simp
  · exact coeffVector_anchor_ne_zero hn

/-- The primitive-root evaluation frame has rank one less than the cyclotomic support size. -/
theorem evaluationMatrix_rank {n : ℕ} (hn : 1 < n) :
    (evaluationMatrix n).rank = Fintype.card (CyclotomicSupport n) - 1 := by
  have hdim := LinearMap.finrank_range_add_finrank_ker
    (evaluationMatrix n).conjTranspose.mulVecLin
  have hkerdim : Module.finrank ℂ
      (LinearMap.ker (evaluationMatrix n).conjTranspose.mulVecLin) = 1 := by
    rw [evaluationMatrix_leftKernel hn]
    exact finrank_span_singleton (coeffVector_ne_zero n)
  rw [← Matrix.rank, hkerdim, Module.finrank_fintype_fun_eq_card] at hdim
  rw [← Matrix.rank_conjTranspose]
  omega

/-- Exact rank of the signed cyclotomic Gram matrix. -/
theorem signedGram_rank {n : ℕ} (hn : 1 < n) :
    (signedGram n).rank = Fintype.card (CyclotomicSupport n) - 1 := by
  rw [signedGram]
  exact (signedCompression_rank_eq (evaluationMatrix n) (coeffVector n) (coeffVector n)
    (fun _ ↦ (1 : ℂ)) (evaluationMatrix_leftKernel hn)
    (fun r ↦ Polynomial.mem_support_iff.mp r.property)
    (fun r ↦ by simp) (coeffVector_anchor_ne_zero hn)).trans (evaluationMatrix_rank hn)

lemma primitiveFrequency_card (n : ℕ) :
    Fintype.card (PrimitiveFrequency n) = Nat.totient n := by
  rw [Fintype.card_coe, Complex.card_primitiveRoots]

/-- Exact nullity of the signed cyclotomic Gram matrix. -/
theorem signedGram_nullity {n : ℕ} (hn : 1 < n) :
    Module.finrank ℂ (LinearMap.ker (signedGram n).mulVecLin) =
      Nat.totient n + 1 - Fintype.card (CyclotomicSupport n) := by
  have hdim := LinearMap.finrank_range_add_finrank_ker (signedGram n).mulVecLin
  rw [← Matrix.rank, signedGram_rank hn, Module.finrank_fintype_fun_eq_card,
    primitiveFrequency_card] at hdim
  have hrankle := Matrix.rank_le_card_width (signedGram n)
  rw [signedGram_rank hn, primitiveFrequency_card] at hrankle
  have hsupport : 0 < Fintype.card (CyclotomicSupport n) := Fintype.card_pos_iff.mpr
    ⟨⟨Nat.totient n, totient_mem_cyclotomicSupport n⟩⟩
  have hsupport_le : Fintype.card (CyclotomicSupport n) ≤ Nat.totient n + 1 := by
    omega
  omega

/-- The squared coefficient norm `hₙ` from the finding, restricted to nonzero coefficients. -/
def coefficientEnergy (n : ℕ) : ℝ :=
  ∑ r : CyclotomicSupport n, Complex.normSq (coeffVector n r)

lemma coefficientEnergy_pos (n : ℕ) : 0 < coefficientEnergy n := by
  classical
  apply Finset.sum_pos'
  · intro r _
    exact Complex.normSq_nonneg _
  · let top : CyclotomicSupport n := ⟨Nat.totient n, totient_mem_cyclotomicSupport n⟩
    refine ⟨top, Finset.mem_univ _, ?_⟩
    exact Complex.normSq_pos.mpr (Polynomial.mem_support_iff.mp top.property)

/-- The nonzero Fourier normalization `1 / sqrt(n hₙ)`. -/
def transverseScale (n : ℕ) : ℂ :=
  ((Real.sqrt ((n : ℝ) * coefficientEnergy n) : ℝ) : ℂ)⁻¹

lemma transverseScale_ne_zero {n : ℕ} (hn : 1 < n) : transverseScale n ≠ 0 := by
  unfold transverseScale
  apply inv_ne_zero
  rw [Complex.ofReal_ne_zero, Real.sqrt_ne_zero']
  exact mul_pos (by positivity) (coefficientEnergy_pos n)

/-- The canonical normalized transverse compression matrix in the conjugated primitive-frequency
convention. -/
def transverseMatrix (n : ℕ) : Matrix (PrimitiveFrequency n) (PrimitiveFrequency n) ℂ :=
  transverseScale n • signedGram n

/-- Entrywise bridge from the signed Gram factorization to cyclotomic evaluation. -/
theorem signedGram_apply (n : ℕ) (u v : PrimitiveFrequency n) :
    signedGram n u v =
      (Polynomial.cyclotomic n ℂ).eval ((u : ℂ) * star (v : ℂ)) := by
  classical
  rw [← supportPolynomial_coeffVector n, supportPolynomial_eval]
  simp [signedGram, Matrix.mul_apply, evaluationMatrix,
    Matrix.diagonal_apply, mul_pow, mul_left_comm, mul_assoc]

/-- The normalized matrix has the cyclotomic Fourier entry from PC-218. -/
theorem transverseMatrix_apply (n : ℕ) (u v : PrimitiveFrequency n) :
    transverseMatrix n u v = transverseScale n *
      (Polynomial.cyclotomic n ℂ).eval ((u : ℂ) * star (v : ℂ)) := by
  rw [transverseMatrix, Matrix.smul_apply, smul_eq_mul, signedGram_apply]

/-- Exact PC-218 rank formula for the normalized transverse matrix. -/
theorem transverseMatrix_rank {n : ℕ} (hn : 1 < n) :
    (transverseMatrix n).rank = Fintype.card (CyclotomicSupport n) - 1 := by
  rw [transverseMatrix,
    Matrix.rank_smul_of_mem_nonZeroDivisors _ (by simp [transverseScale_ne_zero hn]),
    signedGram_rank hn]

/-- Exact PC-218 nullity formula, written without truncated-subtraction ambiguity. -/
theorem transverseMatrix_nullity {n : ℕ} (hn : 1 < n) :
    Module.finrank ℂ (LinearMap.ker (transverseMatrix n).mulVecLin) =
      Nat.totient n + 1 - Fintype.card (CyclotomicSupport n) := by
  have hdim := LinearMap.finrank_range_add_finrank_ker (transverseMatrix n).mulVecLin
  rw [← Matrix.rank, transverseMatrix_rank hn, Module.finrank_fintype_fun_eq_card,
    primitiveFrequency_card] at hdim
  have hrankle := Matrix.rank_le_card_width (transverseMatrix n)
  rw [transverseMatrix_rank hn, primitiveFrequency_card] at hrankle
  have hsupport : 0 < Fintype.card (CyclotomicSupport n) := Fintype.card_pos_iff.mpr
    ⟨⟨Nat.totient n, totient_mem_cyclotomicSupport n⟩⟩
  omega

/-- Coefficient positions up through degree `φ(n)` where the cyclotomic coefficient vanishes. -/
def zeroCoefficientPositions (n : ℕ) : Finset ℕ :=
  Finset.range (Nat.totient n + 1) \ (Polynomial.cyclotomic n ℂ).support

@[simp] theorem mem_zeroCoefficientPositions_iff (n r : ℕ) :
    r ∈ zeroCoefficientPositions n ↔
      r ≤ Nat.totient n ∧ (Polynomial.cyclotomic n ℂ).coeff r = 0 := by
  simp [zeroCoefficientPositions, Polynomial.mem_support_iff]

lemma cyclotomicSupport_subset_range (n : ℕ) :
    (Polynomial.cyclotomic n ℂ).support ⊆ Finset.range (Nat.totient n + 1) := by
  intro r hr
  rw [Finset.mem_range]
  have hle := Polynomial.le_natDegree_of_ne_zero (Polynomial.mem_support_iff.mp hr)
  rw [Polynomial.natDegree_cyclotomic] at hle
  omega

theorem zeroCoefficientPositions_card (n : ℕ) :
    (zeroCoefficientPositions n).card =
      Nat.totient n + 1 - Fintype.card (CyclotomicSupport n) := by
  rw [zeroCoefficientPositions,
    Finset.card_sdiff_of_subset (cyclotomicSupport_subset_range n),
    Finset.card_range, Fintype.card_coe]

/-- The transverse nullity is exactly the number of zero cyclotomic coefficient positions. -/
theorem transverseMatrix_nullity_eq_zeroCoefficientCount {n : ℕ} (hn : 1 < n) :
    Module.finrank ℂ (LinearMap.ker (transverseMatrix n).mulVecLin) =
      (zeroCoefficientPositions n).card := by
  rw [transverseMatrix_nullity hn, zeroCoefficientPositions_card]

end CyclotomicEvaluation

#print axioms signedCompression_ker_eq
#print axioms evaluationMatrix_leftKernel
#print axioms signedGram_ker_eq
#print axioms signedGram_rank
#print axioms transverseMatrix_apply
#print axioms transverseMatrix_rank
#print axioms transverseMatrix_nullity_eq_zeroCoefficientCount

end Mathia.PC218
