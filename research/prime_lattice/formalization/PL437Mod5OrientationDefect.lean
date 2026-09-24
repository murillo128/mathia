import Mathlib.Analysis.Complex.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# PL-437 mod-5 orientation defect

Associated finding:
`research/prime_lattice/findings/PL-437-mod5-orientation-defect-rank-two.md`.

Formalized theorem boundary: the explicit real skew matrix for the mod-5 blind
sector has rank at most two (and exactly two unless all three coordinates
vanish); its normalized four-point Fourier conjugate after multiplication by
`i` is the displayed real-symmetric matrix, whose diagonal determines `d - b`.
After splitting that visible coordinate, the residual family has exactly the
two coordinates `(s, f)` and satisfies its corresponding cubic spectral
polynomial identity. Both `iB` and its residual have explicit Hermitian,
rank-at-most-two, zero-trace, and cubic polynomial certificates; these imply
the stated two nonzero eigenvalues in the nondegenerate case. The identities use
residue order `(1, 2, 4, 3)` and
`F[r,j] = (1/2) * (-i)^(r*j)`.

Lean verifies only the finite mod-5 Fourier/rank reduction. The arithmetic
source estimates, admission of the actual prime covariance to the cone, and
any RH consequence remain outside the formal theorem. The cubic identities,
together with Hermitian symmetry and the rank statements, are exact finite
spectral certificates; the operator-norm corollaries are not separately
formalized.
-/

noncomputable section

namespace Mathia.PL437

open Matrix
open scoped Matrix

abbrev I4 := Fin 4
abbrev I2 := Fin 2

def B (b d f : ℝ) : Matrix I4 I4 ℝ :=
  !![0, b, 0, -b;
     -b, 0, -d, f;
     0, d, 0, -d;
     b, -f, d, 0]

def leftFactor (b d f : ℝ) : Matrix I4 I2 ℝ :=
  !![0, b;
     1, 0;
     0, d;
     -1, -f]

def rightFactor (b d f : ℝ) : Matrix I2 I4 ℝ :=
  !![-b, 0, -d, f;
     0, 1, 0, -1]

def complexLeftFactor (b d f : ℝ) : Matrix I4 I2 ℂ :=
  Complex.I • (leftFactor b d f).map (algebraMap ℝ ℂ)

def complexRightFactor (b d f : ℝ) : Matrix I2 I4 ℂ :=
  (rightFactor b d f).map (algebraMap ℝ ℂ)

def iB (b d f : ℝ) : Matrix I4 I4 ℂ :=
  Complex.I • (B b d f).map (algebraMap ℝ ℂ)

def fourier : Matrix I4 I4 ℂ :=
  !![(1 / 2 : ℂ), (1 / 2), (1 / 2), (1 / 2);
     (1 / 2), (-Complex.I / 2), (-1 / 2), (Complex.I / 2);
     (1 / 2), (-1 / 2), (1 / 2), (-1 / 2);
     (1 / 2), (Complex.I / 2), (-1 / 2), (-Complex.I / 2)]

def fourierImage (b d f : ℝ) : Matrix I4 I4 ℂ :=
  fourier * iB b d f * fourier.conjTranspose

def expectedImage (b d f : ℝ) : Matrix I4 I4 ℂ :=
  !![0, ((-b - d + f) / 2 : ℝ), 0, ((b + d - f) / 2 : ℝ);
     ((-b - d + f) / 2 : ℝ), (-b + d : ℝ), ((-b - d - f) / 2 : ℝ), 0;
     0, ((-b - d - f) / 2 : ℝ), 0, ((b + d + f) / 2 : ℝ);
     ((b + d - f) / 2 : ℝ), 0, ((b + d + f) / 2 : ℝ), (b - d : ℝ)]

def rPart (r : ℝ) : Matrix I4 I4 ℝ := B (-r / 2) (r / 2) 0

def residual (s f : ℝ) : Matrix I4 I4 ℝ := B (s / 2) (s / 2) f

def iResidual (s f : ℝ) : Matrix I4 I4 ℂ :=
  Complex.I • (residual s f).map (algebraMap ℝ ℂ)

def residualImage (s f : ℝ) : Matrix I4 I4 ℂ :=
  fourier * iResidual s f * fourier.conjTranspose

theorem transpose_B (b d f : ℝ) : (B b d f)ᵀ = -B b d f := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [B]

theorem factorization (b d f : ℝ) :
    B b d f = leftFactor b d f * rightFactor b d f := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [B, leftFactor, rightFactor, Matrix.mul_apply]

theorem iB_factorization (b d f : ℝ) :
    iB b d f = complexLeftFactor b d f * complexRightFactor b d f := by
  simp only [iB, factorization, Matrix.map_mul, complexLeftFactor, complexRightFactor]
  rw [← Matrix.smul_mul]

theorem rank_B_le_two (b d f : ℝ) : (B b d f).rank ≤ 2 := by
  rw [factorization]
  calc
    (leftFactor b d f * rightFactor b d f).rank ≤ (leftFactor b d f).rank :=
      Matrix.rank_mul_le_left _ _
    _ ≤ 2 := by
      simpa using (Matrix.rank_le_card_width (leftFactor b d f))

theorem rank_iB_le_two (b d f : ℝ) : (iB b d f).rank ≤ 2 := by
  rw [iB_factorization]
  calc
    (complexLeftFactor b d f * complexRightFactor b d f).rank ≤
        (complexLeftFactor b d f).rank := Matrix.rank_mul_le_left _ _
    _ ≤ 2 := by
      simpa [I2] using (Matrix.rank_le_card_width (complexLeftFactor b d f))

theorem det_B_eq_zero (b d f : ℝ) : (B b d f).det = 0 := by
  by_contra hdet
  have hfull := Matrix.rank_of_det_ne_zero hdet
  have hcard : Fintype.card I4 = 4 := by simp [I4]
  rw [hcard] at hfull
  have hle := rank_B_le_two b d f
  omega

def embed01 (i : I2) : I4 := ⟨i.val, by omega⟩
def embed12 (i : I2) : I4 := ⟨i.val + 1, by omega⟩
def embed13 (i : I2) : I4 := ⟨2 * i.val + 1, by omega⟩

private theorem minor_det (b d f : ℝ) (e : I2 → I4) (v : ℝ)
    (hminor : (B b d f).submatrix e e = !![0, v; -v, 0]) :
    ((B b d f).submatrix e e).det = v ^ 2 := by
  rw [hminor, Matrix.det_fin_two]
  simp [Matrix.of_apply, pow_two]

theorem rank_B_two_of_nonzero (b d f : ℝ)
    (h : b ≠ 0 ∨ d ≠ 0 ∨ f ≠ 0) : (B b d f).rank = 2 := by
  apply le_antisymm (rank_B_le_two b d f)
  rcases h with hb | hd | hf
  · have hminor : (B b d f).submatrix embed01 embed01 = !![0, b; -b, 0] := by
      ext i j
      fin_cases i <;> fin_cases j <;> simp [B, embed01]
    have hdet : ((B b d f).submatrix embed01 embed01).det ≠ 0 := by
      rw [minor_det b d f embed01 b hminor]
      exact pow_ne_zero 2 hb
    have hminorRank : ((B b d f).submatrix embed01 embed01).rank = 2 := by
      simpa [I2] using Matrix.rank_of_det_ne_zero hdet
    have hsub := Matrix.rank_submatrix_le (B b d f) embed01 embed01
    omega
  · have hminor : (B b d f).submatrix embed12 embed12 = !![0, -d; -(-d), 0] := by
      ext i j
      fin_cases i <;> fin_cases j <;> simp [B, embed12]
    have hdet : ((B b d f).submatrix embed12 embed12).det ≠ 0 := by
      rw [minor_det b d f embed12 (-d) hminor]
      exact pow_ne_zero 2 (neg_ne_zero.mpr hd)
    have hminorRank : ((B b d f).submatrix embed12 embed12).rank = 2 := by
      simpa [I2] using Matrix.rank_of_det_ne_zero hdet
    have hsub := Matrix.rank_submatrix_le (B b d f) embed12 embed12
    omega
  · have hminor : (B b d f).submatrix embed13 embed13 = !![0, f; -f, 0] := by
      ext i j
      fin_cases i <;> fin_cases j <;> simp [B, embed13]
    have hdet : ((B b d f).submatrix embed13 embed13).det ≠ 0 := by
      rw [minor_det b d f embed13 f hminor]
      exact pow_ne_zero 2 hf
    have hminorRank : ((B b d f).submatrix embed13 embed13).rank = 2 := by
      simpa [I2] using Matrix.rank_of_det_ne_zero hdet
    have hsub := Matrix.rank_submatrix_le (B b d f) embed13 embed13
    omega

theorem rank_B_eq_zero_iff (b d f : ℝ) :
    (B b d f).rank = 0 ↔ b = 0 ∧ d = 0 ∧ f = 0 := by
  constructor
  · intro hr
    by_contra hnot
    have hpos : b ≠ 0 ∨ d ≠ 0 ∨ f ≠ 0 := by
      by_cases hb : b = 0
      · by_cases hd : d = 0
        · by_cases hf : f = 0
          · exact False.elim (hnot ⟨hb, hd, hf⟩)
          · exact Or.inr (Or.inr hf)
        · exact Or.inr (Or.inl hd)
      · exact Or.inl hb
    have := rank_B_two_of_nonzero b d f hpos
    omega
  · rintro ⟨rfl, rfl, rfl⟩
    have hzero : B (0 : ℝ) 0 0 = 0 := by
      ext i j
      fin_cases i <;> fin_cases j <;> simp [B]
    rw [hzero, Matrix.rank_zero]

theorem B_cube (b d f : ℝ) :
    B b d f ^ 3 = -(2 * b ^ 2 + 2 * d ^ 2 + f ^ 2) • B b d f := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [B, Matrix.mul_apply, pow_succ, Fin.sum_univ_succ] <;> ring

theorem iB_hermitian (b d f : ℝ) : (iB b d f).conjTranspose = iB b d f := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [iB, B, Matrix.conjTranspose_apply, Complex.conj_I]

theorem iB_cube (b d f : ℝ) :
    iB b d f ^ 3 = (2 * b ^ 2 + 2 * d ^ 2 + f ^ 2 : ℝ) • iB b d f := by
  let M : Matrix I4 I4 ℂ := (B b d f).map (algebraMap ℝ ℂ)
  have hM : M ^ 3 = -(2 * b ^ 2 + 2 * d ^ 2 + f ^ 2 : ℝ) • M := by
    have hmap := congrArg (fun X : Matrix I4 I4 ℝ => X.map (algebraMap ℝ ℂ))
      (B_cube b d f)
    rw [Matrix.map_pow] at hmap
    rw [Matrix.map_smul (algebraMap ℝ ℂ) _ (by intro x; simp)] at hmap
    simpa [M] using hmap
  rw [iB, show (Complex.I • M) ^ 3 = Complex.I ^ 3 • M ^ 3 by rw [smul_pow]]
  rw [hM]
  have hI3 : Complex.I ^ 3 = -Complex.I := by
    rw [pow_succ, Complex.I_sq]
    simp
  rw [hI3]
  calc
    (-Complex.I) • (-(2 * b ^ 2 + 2 * d ^ 2 + f ^ 2 : ℝ) • M) =
        -(2 * b ^ 2 + 2 * d ^ 2 + f ^ 2 : ℝ) • ((-Complex.I) • M) :=
      smul_comm _ _ _
    _ = (2 * b ^ 2 + 2 * d ^ 2 + f ^ 2 : ℝ) • (Complex.I • M) := by
      simp only [neg_smul, smul_neg, neg_neg]

theorem iB_trace (b d f : ℝ) : Matrix.trace (iB b d f) = 0 := by
  simp [Matrix.trace, iB, B, Fin.sum_univ_succ]

theorem iResidual_hermitian (s f : ℝ) :
    (iResidual s f).conjTranspose = iResidual s f := by
  simpa [iResidual, residual, iB] using iB_hermitian (s / 2) (s / 2) f

theorem iResidual_trace (s f : ℝ) : Matrix.trace (iResidual s f) = 0 := by
  simpa [iResidual, residual, iB] using iB_trace (s / 2) (s / 2) f

theorem rank_iResidual_le_two (s f : ℝ) : (iResidual s f).rank ≤ 2 := by
  simpa [iResidual, residual, iB] using rank_iB_le_two (s / 2) (s / 2) f

theorem iResidual_cube (s f : ℝ) :
    iResidual s f ^ 3 = (s ^ 2 + f ^ 2 : ℝ) • iResidual s f := by
  have hcoef : 2 * (s / 2) ^ 2 + 2 * (s / 2) ^ 2 + f ^ 2 = s ^ 2 + f ^ 2 := by ring
  simpa [iResidual, residual, iB, hcoef] using iB_cube (s / 2) (s / 2) f

theorem fourier_entry_eq (r j : I4) :
    fourier r j = (2 : ℂ)⁻¹ * (-Complex.I) ^ (r.val * j.val) := by
  fin_cases r <;> fin_cases j <;> norm_num [fourier, pow_succ, Complex.I_sq] <;> ring

theorem fourierImage_eq (b d f : ℝ) :
    fourierImage b d f = expectedImage b d f := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [fourierImage, fourier, iB, B, expectedImage, Matrix.mul_apply,
      Matrix.vecMul, dotProduct, Fin.sum_univ_succ,
      Complex.ofReal_mul, Complex.ofReal_add,
      Complex.ofReal_sub, Complex.ofReal_neg, Complex.I_sq, Complex.I_mul_I]
      <;> (try simp [starRingEnd_apply])
      <;> (try field_simp)
      <;> ring_nf
      <;> (try simp_rw [Complex.I_sq])
      <;> ring

theorem fourierImage_diagonal (b d f : ℝ) :
    (fourierImage b d f 0 0 = 0) ∧
    (fourierImage b d f 1 1 = (d - b : ℝ)) ∧
    (fourierImage b d f 2 2 = 0) ∧
    (fourierImage b d f 3 3 = (b - d : ℝ)) := by
  rw [fourierImage_eq]
  norm_num [expectedImage]; ring

theorem expectedImage_symmetric (b d f : ℝ) :
    (expectedImage b d f)ᵀ = expectedImage b d f := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [expectedImage]

theorem split_coordinates (b d f : ℝ) :
    B b d f = rPart (d - b) + residual (b + d) f := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [B, rPart, residual] <;> ring

theorem residual_injective : Function.Injective (fun p : ℝ × ℝ => residual p.1 p.2) := by
  intro p q hpq
  rcases p with ⟨s, f⟩
  rcases q with ⟨s', f'⟩
  have hs : s / 2 = s' / 2 := by
    simpa [residual, B] using congrFun (congrFun hpq 0) 1
  have hf : f = f' := by
    simpa [residual, B] using congrFun (congrFun hpq 1) 3
  apply Prod.ext
  · linarith
  · exact hf

theorem residual_fourier_diagonal (s f : ℝ) :
    (residualImage s f 0 0 = 0) ∧
    (residualImage s f 1 1 = 0) ∧
    (residualImage s f 2 2 = 0) ∧
    (residualImage s f 3 3 = 0) := by
  have h := fourierImage_diagonal (s / 2) (s / 2) f
  simpa [residualImage, iResidual, residual, iB, fourierImage, fourier] using h

theorem residual_cube (s f : ℝ) :
    residual s f ^ 3 = -(s ^ 2 + f ^ 2) • residual s f := by
  have hcoef : 2 * (s / 2) ^ 2 + 2 * (s / 2) ^ 2 + f ^ 2 = s ^ 2 + f ^ 2 := by ring
  rw [← hcoef]
  simpa [residual] using (B_cube (s / 2) (s / 2) f)

theorem residual_parameters_unique {s f s' f' : ℝ}
    (h : residual s f = residual s' f') : s = s' ∧ f = f' := by
  have hs := congrFun (congrFun h 0) 1
  have hf := congrFun (congrFun h 1) 3
  constructor
  · dsimp [residual, B] at hs ⊢
    linarith
  · exact hf

#print axioms rank_B_le_two
#print axioms rank_B_two_of_nonzero
#print axioms det_B_eq_zero
#print axioms rank_iB_le_two
#print axioms iB_hermitian
#print axioms iB_cube
#print axioms iB_trace
#print axioms B_cube
#print axioms fourierImage_eq
#print axioms residual_cube
#print axioms rank_iResidual_le_two
#print axioms iResidual_hermitian
#print axioms iResidual_trace
#print axioms iResidual_cube

end Mathia.PL437
