import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.Ring

/-!
# AF-153 transported reset covariance

Associated finding:
`research/arithmetic_fidelity/findings/AF-153-endpoint-shtarkov-drift-is-transported-reset-covariance.md`

Formalized theorem boundary: for a finite prefix of a possibly heterogeneous
chain of real linear maps and moving references, the propagated initial reference
minus the final reference is the sum of local reset defects transported through
all subsequent maps. Evaluating each term equals evaluating its local defect on
the pulled-back endpoint functional. Finite matrices realize forward transport of
real weight vectors and backward transport of observables. Under explicit local
density and normalization hypotheses, the endpoint response is the sum of the
pulled-back covariances divided by the local nonzero normalizers.

The transport identities require only linearity, so include probability vectors
and Markov kernels without requiring positivity. Finite moment covariance below
agrees with the centered expression when the weights sum to one; outside that
case it is an algebraic extension, not mathlib's centered-integral covariance.
All real observables on a finite type are bounded. Empty chains/types are allowed;
probability normalization excludes empty types wherever it is assumed. No density
is obtained by dividing by a reference coordinate, so zero support is harmless.

Not formalized: the Shtarkov/NML max-envelope construction or AF-151's derivation
of the density and its normalizer. Those enter as explicit hypotheses. Dobrushin
coefficients, total-variation/variance bounds, and prime or RH consequences are
outside this theorem. No novelty is claimed for the classical transport calculus.
-/

namespace Mathia.AF153

open scoped BigOperators Matrix

noncomputable section

section LinearChain

variable {E : ℕ → Type*} [∀ n, AddCommGroup (E n)] [∀ n, Module ℝ (E n)]
  (K : ∀ n, E n →ₗ[ℝ] E (n + 1)) (M : ∀ n, E n)

/-- `K n` is AF-153's channel from stage `n` to stage `n+1`. -/
def propagated : ∀ n, E n
  | 0 => M 0
  | n + 1 => K n (propagated n)

/-- The reset at stage `n+1`, with the sign propagated reference minus new reference. -/
def defect (n : ℕ) : E (n + 1) := K n (M n) - M (n + 1)

/-- At endpoint `n`, index `j : Fin n` is the defect injected at stage `n-j`.
The newest term has identity suffix; every older term passes through `K n` when
the endpoint advances. This is the suffix transport, enumerated without casts. -/
def transported (D : ∀ n, E (n + 1)) : ∀ n, Fin n → E n
  | 0 => Fin.elim0
  | n + 1 => Fin.cases (D n) (fun j => K n (transported D n j))

theorem transported_defect_sum (n : ℕ) :
    propagated K M n - M n = ∑ j : Fin n, transported K (defect K M) n j := by
  induction n with
  | zero => simp [propagated]
  | succ n ih =>
    rw [Fin.sum_univ_succ]
    simp only [transported, Fin.cases_zero, Fin.cases_succ]
    rw [← map_sum, ← ih]
    simp only [propagated, defect, map_sub]
    abel

/-- Responses retain each local injection separately and pull the endpoint
functional backward through precisely the maps following that injection. -/
def responses (D : ∀ n, E (n + 1)) :
    ∀ n, (E n →ₗ[ℝ] ℝ) → Fin n → ℝ
  | 0, _ => Fin.elim0
  | n + 1, f => Fin.cases (f (D n)) (responses D n (f.comp (K n)))

theorem responses_eq (D : ∀ n, E (n + 1)) (n : ℕ)
    (f : E n →ₗ[ℝ] ℝ) (j : Fin n) :
    responses K D n f j = f (transported K D n j) := by
  induction n with
  | zero => exact Fin.elim0 j
  | succ n ih =>
    refine Fin.cases ?_ (fun j => ?_) j
    · rfl
    · exact ih (f.comp (K n)) j

theorem response_sum (n : ℕ) (f : E n →ₗ[ℝ] ℝ) :
    f (propagated K M n - M n) = ∑ j : Fin n, responses K (defect K M) n f j := by
  rw [transported_defect_sum, map_sum]
  apply Finset.sum_congr rfl
  intro j _
  exact (responses_eq K _ n f j).symm

end LinearChain

section FiniteKernels

variable {X Y Z : Type*} [Fintype X] [Fintype Y] [Fintype Z]

/-- Pair a real signed weight vector with a finite observable. -/
abbrev pairing (f : X → ℝ) : (X → ℝ) →ₗ[ℝ] ℝ :=
  (dotProductBilin ℝ ℝ).flip f

theorem pairing_apply (w f : X → ℝ) : pairing f w = w ⬝ᵥ f := rfl

/-- `K x y = K(y|x)`: row weights move forward by `vecMul`; observables
move backward by `mulVec`. This also fixes the order for heterogeneous stages. -/
theorem pairing_pullback (K : Matrix X Y ℝ) (f : Y → ℝ) :
    (pairing f).comp K.vecMulLinear = pairing (K *ᵥ f) := by
  ext w
  exact (Matrix.dotProduct_mulVec w K f).symm

omit [Fintype Z] in
theorem two_stage (K : Matrix X Y ℝ) (L : Matrix Y Z ℝ)
    (M₀ : X → ℝ) (M₁ : Y → ℝ) (M₂ : Z → ℝ) :
    (M₀ ᵥ* K) ᵥ* L - M₂ = (M₀ ᵥ* K - M₁) ᵥ* L + (M₁ ᵥ* L - M₂) := by
  rw [Matrix.sub_vecMul]
  abel

/-- Normalized row sums preserve total mass, independently of positivity. -/
theorem mass_forward (K : Matrix X Y ℝ) (hK : K *ᵥ (1 : Y → ℝ) = 1)
    (w : X → ℝ) : (w ᵥ* K) ⬝ᵥ 1 = w ⬝ᵥ 1 := by
  rw [← Matrix.dotProduct_mulVec, hK]

end FiniteKernels

section Covariance

variable {X : Type*} [Fintype X]

/-- Finite moment covariance. For probability weights this is ordinary covariance;
for arbitrary signed or unnormalized weights it is only the displayed expression. -/
def covariance (M a g : X → ℝ) : ℝ :=
  M ⬝ᵥ (a * g) - (M ⬝ᵥ a) * (M ⬝ᵥ g)

/-- The moment convention agrees with centered covariance for unit total mass. -/
theorem covariance_eq_centered (M a g : X → ℝ) (hM : ∑ x, M x = 1) :
    covariance M a g = ∑ x, M x * (a x - M ⬝ᵥ a) * (g x - M ⬝ᵥ g) := by
  have hterm (x : X) :
      M x * (a x - M ⬝ᵥ a) * (g x - M ⬝ᵥ g) =
        M x * (a x * g x) - (M x * a x) * (M ⬝ᵥ g) -
          (M ⬝ᵥ a) * (M x * g x) + ((M ⬝ᵥ a) * (M ⬝ᵥ g)) * M x := by ring
  simp_rw [hterm]
  simp only [Finset.sum_add_distrib, Finset.sum_sub_distrib, ← Finset.sum_mul,
    ← Finset.mul_sum, hM, mul_one]
  change covariance M a g =
    M ⬝ᵥ (a * g) - (M ⬝ᵥ a) * (M ⬝ᵥ g) -
      (M ⬝ᵥ a) * (M ⬝ᵥ g) + (M ⬝ᵥ a) * (M ⬝ᵥ g)
  simp [covariance]

theorem density_response (M R ρ g : X → ℝ)
    (hR : R = M * ρ) (hρ : M ⬝ᵥ ρ = 1) :
    (R - M) ⬝ᵥ g = covariance M ρ g := by
  subst R
  rw [sub_dotProduct, covariance, hρ, one_mul]
  congr 1
  apply Finset.sum_congr rfl
  intro x _
  exact mul_assoc _ _ _

/-- Normalization of the likelihood follows from the propagated law's unit mass
and the explicit density relation, including coordinates where `M x = 0`. -/
theorem density_normalized (M R ρ : X → ℝ)
    (hR : R = M * ρ) (hmass : ∑ x, R x = 1) : M ⬝ᵥ ρ = 1 := by
  simpa [hR, dotProduct] using hmass

theorem expectation_div (M κ : X → ℝ) (μ : ℝ) :
    M ⬝ᵥ (fun x => κ x / μ) = (M ⬝ᵥ κ) / μ := by
  simp only [dotProduct, div_eq_mul_inv, ← mul_assoc, ← Finset.sum_mul]

theorem covariance_div_left (M κ g : X → ℝ) (μ : ℝ) :
    covariance M (fun x => κ x / μ) g = covariance M κ g / μ := by
  unfold covariance
  rw [expectation_div]
  have h : M ⬝ᵥ ((fun x => κ x / μ) * g) = (M ⬝ᵥ (κ * g)) / μ := by
    simp only [dotProduct, Pi.mul_apply, div_eq_mul_inv]
    simp_rw [mul_right_comm (κ _) μ⁻¹, ← mul_assoc, ← Finset.sum_mul]
  rw [h]
  ring

/-- The nonzero normalizer and its mean are separate from the density relation.
No claim about the Shtarkov construction is used to manufacture any hypothesis. -/
theorem scaled_density_response (M R κ g : X → ℝ) (μ : ℝ)
    (hμ : μ ≠ 0) (hmean : M ⬝ᵥ κ = μ)
    (hR : R = M * (fun x => κ x / μ)) :
    (R - M) ⬝ᵥ g = covariance M κ g / μ := by
  rw [density_response M R (fun x => κ x / μ) g hR, covariance_div_left]
  rw [expectation_div, hmean, div_self hμ]

end Covariance

section FiniteChain

variable {X : ℕ → Type*} [∀ n, Fintype (X n)]
  (K : ∀ n, Matrix (X n) (X (n + 1)) ℝ) (M : ∀ n, X n → ℝ)

/-- Finite observable form of the local/suffix response enumeration. -/
def finiteResponses (D : ∀ n, X (n + 1) → ℝ) :
    ∀ n, (X n → ℝ) → Fin n → ℝ
  | 0, _ => Fin.elim0
  | n + 1, f => Fin.cases (D n ⬝ᵥ f) (finiteResponses D n (K n *ᵥ f))

theorem finiteResponses_eq (D : ∀ n, X (n + 1) → ℝ) (n : ℕ)
    (f : X n → ℝ) :
    finiteResponses K D n f = responses (fun i => (K i).vecMulLinear) D n (pairing f) := by
  induction n with
  | zero => rfl
  | succ n ih =>
    simp only [finiteResponses, responses, pairing_pullback, ih, pairing_apply]

theorem finite_response_sum (n : ℕ) (f : X n → ℝ) :
    (propagated (fun i => (K i).vecMulLinear) M n - M n) ⬝ᵥ f =
      ∑ j : Fin n, finiteResponses K (defect (fun i => (K i).vecMulLinear) M) n f j := by
  rw [finiteResponses_eq]
  exact response_sum (fun i => (K i).vecMulLinear) M n (pairing f)

/-- Each covariance uses its own reference and conflict profile. The endpoint
observable is pulled back through the actual suffix, newest contribution first. -/
def covarianceResponses (κ : ∀ n, X (n + 1) → ℝ) (μ : ℕ → ℝ) :
    ∀ n, (X n → ℝ) → Fin n → ℝ
  | 0, _ => Fin.elim0
  | n + 1, f => Fin.cases (covariance (M (n + 1)) (κ n) f / μ n)
      (covarianceResponses κ μ n (K n *ᵥ f))

theorem finiteResponses_eq_covarianceResponses
    (κ : ∀ n, X (n + 1) → ℝ) (μ : ℕ → ℝ) (n : ℕ)
    (hμ : ∀ i, i < n → μ i ≠ 0)
    (hmean : ∀ i, i < n → M (i + 1) ⬝ᵥ κ i = μ i)
    (hdensity : ∀ i, i < n →
      M i ᵥ* K i = M (i + 1) * (fun x => κ i x / μ i)) (f : X n → ℝ) :
    finiteResponses K (defect (fun i => (K i).vecMulLinear) M) n f =
      covarianceResponses K M κ μ n f := by
  induction n with
  | zero => rfl
  | succ n ih =>
    funext j
    refine Fin.cases ?_ (fun j => ?_) j
    · exact scaled_density_response (M (n + 1)) (M n ᵥ* K n) (κ n) f (μ n)
        (hμ n (Nat.lt_succ_self n)) (hmean n (Nat.lt_succ_self n))
        (hdensity n (Nat.lt_succ_self n))
    · exact congrFun (ih
        (fun i hi => hμ i (Nat.lt_succ_of_lt hi))
        (fun i hi => hmean i (Nat.lt_succ_of_lt hi))
        (fun i hi => hdensity i (Nat.lt_succ_of_lt hi)) (K n *ᵥ f)) j

/-- AF-153's endpoint covariance identity for every finite prefix. Only stages
strictly before this endpoint need satisfy the stated density/mean hypotheses. -/
theorem endpoint_covariance_sum
    (κ : ∀ n, X (n + 1) → ℝ) (μ : ℕ → ℝ) (n : ℕ)
    (hμ : ∀ i, i < n → μ i ≠ 0)
    (hmean : ∀ i, i < n → M (i + 1) ⬝ᵥ κ i = μ i)
    (hdensity : ∀ i, i < n →
      M i ᵥ* K i = M (i + 1) * (fun x => κ i x / μ i)) (f : X n → ℝ) :
    (propagated (fun i => (K i).vecMulLinear) M n - M n) ⬝ᵥ f =
      ∑ j : Fin n, covarianceResponses K M κ μ n f j := by
  rw [finite_response_sum,
    finiteResponses_eq_covarianceResponses K M κ μ n hμ hmean hdensity]

end FiniteChain

end

end Mathia.AF153
