import Mathlib.Analysis.CStarAlgebra.Matrix
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Analysis.Calculus.Deriv.MeanValue
import Mathlib.Analysis.InnerProductSpace.Calculus
import Mathlib.Tactic.Abel
import Mathlib.Tactic.GCongr
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NoncommRing
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
# Mixed-Gram damping and nonlinear chord stability

Associated finding:
`research/xi_flow/findings/XF-186-holomorphic-packet-banks-are-uniformly-bi-lipschitz-on-a-lattice-scale-nonlinear-cell.md`

Only the conditional mixed-Gram/damping/chord/perturbation implication is proved.
All vector norms are Euclidean l2 norms and matrix norms are their operator norms.
The mixed Gram need not be Hermitian. Real derivatives within a convex set suffice;
the anchored scalar mean-value theorem controls the whole chord, including its endpoints.

Not formalized: Fejer kernel inequalities, quadratic-packet sample construction,
reciprocal-image asymptotics, physical-coordinate/raw-noise transfer, unknown
support/weights, Xi zeros or RH. No originality claim relative to superresolution
literature or verification of the complete source-side XF-186 chart is made.
-/

noncomputable section
open scoped BigOperators Matrix.Norms.L2Operator ComplexInnerProductSpace
open WithLp Set

namespace Mathia.XF186

variable {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- The finite l2 Schur bound uses both absolute row and column sums. -/
theorem schur_bound (A : Matrix ι ι ℂ) {r : ℝ} (hr : 0 ≤ r)
    (hrow : ∀ i, ∑ j, ‖A i j‖ ≤ r) (hcol : ∀ j, ∑ i, ‖A i j‖ ≤ r) :
    ‖A‖ ≤ r := by
  rw [← Matrix.l2_opNorm_toEuclideanCLM]
  apply ContinuousLinearMap.opNorm_le_bound _ hr
  intro x
  apply (sq_le_sq₀ (norm_nonneg _) (mul_nonneg hr (norm_nonneg _))).mp
  rw [EuclideanSpace.norm_sq_eq, mul_pow, EuclideanSpace.norm_sq_eq]
  have hrowx (i : ι) : ‖((Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) A x) i‖ ^ 2 ≤
      r * ∑ j, ‖A i j‖ * ‖x j‖ ^ 2 := by
    have hn : ‖((Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) A x) i‖ ≤ ∑ j, ‖A i j‖ * ‖x j‖ := by
      change ‖∑ j, A i j * x j‖ ≤ _
      simpa only [norm_mul] using norm_sum_le (Finset.univ : Finset ι) (fun j => A i j * x j)
    have hcs := Finset.sum_sq_le_sum_mul_sum_of_sq_le_mul (R := ℝ) Finset.univ
      (f := fun j => ‖A i j‖) (g := fun j => ‖A i j‖ * ‖x j‖ ^ 2)
      (r := fun j => ‖A i j‖ * ‖x j‖)
      (by intros; positivity) (by intros; positivity) (by intros; nlinarith)
    exact (pow_le_pow_left₀ (norm_nonneg _) hn 2).trans
      (hcs.trans (mul_le_mul_of_nonneg_right (hrow i) (by positivity)))
  calc
    _ ≤ ∑ i, r * ∑ j, ‖A i j‖ * ‖x j‖ ^ 2 := Finset.sum_le_sum (fun i _ => hrowx i)
    _ = r * ∑ j, (∑ i, ‖A i j‖) * ‖x j‖ ^ 2 := by
      rw [← Finset.mul_sum, Finset.sum_comm]
      simp_rw [Finset.sum_mul]
    _ ≤ r * ∑ j, r * ‖x j‖ ^ 2 := by
      gcongr with j
      exact hcol j
    _ = _ := by rw [← Finset.mul_sum]; ring

def off (C : Matrix ι ι ℂ) : Matrix ι ι ℂ := C - Matrix.diagonal (fun j => C j j)

/-- Entrywise assumptions, with both off-diagonal sums and no symmetry premise. -/
structure GramBounds (C : Matrix ι ι ℂ) (L dm dp rho : ℝ) : Prop where
  diag_lower : ∀ j, dm * L ≤ (C j j).re
  diag_upper : ∀ j, ‖C j j‖ ≤ dp * L
  row : ∀ i, ∑ j, ‖off C i j‖ ≤ rho * L
  col : ∀ j, ∑ i, ‖off C i j‖ ≤ rho * L

theorem off_bound {C : Matrix ι ι ℂ} {L dm dp rho : ℝ}
    (h : GramBounds C L dm dp rho) (hL : 0 ≤ L) (hr : 0 ≤ rho) :
    ‖off C‖ ≤ rho * L := schur_bound _ (mul_nonneg hr hL) h.row h.col

theorem gram_norm {C : Matrix ι ι ℂ} {L dm dp rho : ℝ}
    (h : GramBounds C L dm dp rho) (hL : 0 ≤ L) (hr : 0 ≤ rho) (hp : 0 ≤ dp) :
    ‖C‖ ≤ (dp + rho) * L := by
  have hd : ‖Matrix.diagonal (fun j => C j j)‖ ≤ dp * L := by
    rw [Matrix.l2_opNorm_diagonal]
    exact (pi_norm_le_iff_of_nonneg (mul_nonneg hp hL)).mpr h.diag_upper
  have he : C = Matrix.diagonal (fun j => C j j) + off C := by unfold off; abel
  calc
    ‖C‖ = ‖Matrix.diagonal (fun j => C j j) + off C‖ := congrArg norm he
    _ ≤ ‖Matrix.diagonal (fun j => C j j)‖ + ‖off C‖ := norm_add_le _ _
    _ ≤ dp * L + rho * L := add_le_add hd (off_bound h hL hr)
    _ = _ := by ring

theorem gram_coercive {C : Matrix ι ι ℂ} {L dm dp rho : ℝ}
    (h : GramBounds C L dm dp rho) (hL : 0 ≤ L) (hr : 0 ≤ rho)
    (x : EuclideanSpace ℂ ι) :
    (dm - rho) * L * ‖x‖ ^ 2 ≤ (inner ℂ x ((Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) C x)).re := by
  have hd : dm * L * ‖x‖ ^ 2 ≤
      (inner ℂ x ((Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) (Matrix.diagonal (fun j => C j j)) x)).re := by
    simp only [PiLp.inner_apply, RCLike.inner_apply, Matrix.ofLp_toEuclideanCLM,
      Matrix.mulVec_diagonal]
    change dm * L * ‖x‖ ^ 2 ≤ (∑ j, (C j j * x j) * star (x j)).re
    have he (j : ι) : ((C j j * x j) * star (x j)).re = (C j j).re * ‖x j‖ ^ 2 := by
      change ((C j j * x j) * (starRingEnd ℂ) (x j)).re = _
      rw [mul_assoc, Complex.mul_conj']
      simp [← Complex.ofReal_pow]
    rw [Complex.re_sum, EuclideanSpace.norm_sq_eq, Finset.mul_sum]
    exact Finset.sum_le_sum (fun j _ => by rw [he]; exact mul_le_mul_of_nonneg_right (h.diag_lower j) (sq_nonneg _))
  have ho : ‖(Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) (off C) x‖ ≤ rho * L * ‖x‖ :=
    ((Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) (off C)).le_of_opNorm_le
      (by simpa only [Matrix.l2_opNorm_toEuclideanCLM] using off_bound h hL hr) x
  have hi := norm_inner_le_norm (𝕜 := ℂ) x ((Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) (off C) x)
  have hre := (abs_le.mp (Complex.abs_re_le_norm (inner ℂ x ((Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) (off C) x)))).1
  have he : C = Matrix.diagonal (fun j => C j j) + off C := by unfold off; abel
  rw [he, map_add, add_apply, inner_add_right, Complex.add_re]
  nlinarith [mul_le_mul_of_nonneg_left ho (norm_nonneg x)]

def margin (dm dp rho eps : ℝ) : ℝ := dm - rho - (dp + rho) * eps

/-- Right damping is estimated as C + C(E-I), without commuting C and E.
In fact this bound holds for every small operator perturbation of the identity. -/
theorem damped_coercive {C E : Matrix ι ι ℂ} {L dm dp rho eps : ℝ}
    (h : GramBounds C L dm dp rho) (hL : 0 ≤ L) (hr : 0 ≤ rho) (hp : 0 ≤ dp)
    (he : ‖E - 1‖ ≤ eps) (x : EuclideanSpace ℂ ι) :
    margin dm dp rho eps * L * ‖x‖ ^ 2 ≤
      (inner ℂ x ((Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) (C * E) x)).re := by
  have hn : ‖C * (E - 1)‖ ≤ (dp + rho) * L * eps :=
    (norm_mul_le _ _).trans (mul_le_mul (gram_norm h hL hr hp) he
      (norm_nonneg _) (by positivity))
  have hx : ‖(Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) (C * (E - 1)) x‖ ≤ (dp + rho) * L * eps * ‖x‖ :=
    ((Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) _).le_of_opNorm_le (by simpa only [Matrix.l2_opNorm_toEuclideanCLM] using hn) x
  have hi := norm_inner_le_norm (𝕜 := ℂ) x ((Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) (C * (E - 1)) x)
  have hre := (abs_le.mp (Complex.abs_re_le_norm (inner ℂ x ((Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) (C * (E - 1)) x)))).1
  have hc := gram_coercive h hL hr x
  rw [show C * E = C + C * (E - 1) by noncomm_ring, map_add,
    add_apply, inner_add_right, Complex.add_re]
  unfold margin
  nlinarith [mul_le_mul_of_nonneg_left hx (norm_nonneg x)]

section Chord
variable {P H : Type*} [NormedAddCommGroup P] [NormedSpace ℝ P]
  [NormedAddCommGroup H] [InnerProductSpace ℂ H]

/-- Scalarizing against one fixed vector preserves the lower margin on the entire
segment. No pointwise lower singular-value premise is substituted for this anchor. -/
theorem anchored_chord {S : Set P} (hS : Convex ℝ S) {F : P → H}
    {J : P → P →L[ℝ] H} (hF : ∀ z ∈ S, HasFDerivWithinAt F (J z) S z)
    {h g : P} (hh : h ∈ S) (hg : g ∈ S) (a : H) {k : ℝ}
    (ha : ∀ z ∈ S, k ≤ (inner ℂ a (J z (h - g))).re) :
    k ≤ (inner ℂ a (F h - F g)).re := by
  let q : H →L[ℝ] ℝ := Complex.reCLM.comp ((innerSL ℂ a).restrictScalars ℝ)
  let line := (AffineMap.lineMap g h : ℝ → P)
  have seg : MapsTo line (Icc 0 1) S := hS.mapsTo_lineMap hg hh
  have hd (t : ℝ) (ht : t ∈ Icc (0 : ℝ) 1) :
      HasDerivWithinAt (fun t => q (F (line t))) (q (J (line t) (h-g))) (Icc 0 1) t := by
    exact q.hasFDerivAt.comp_hasDerivWithinAt t
      ((hF _ (seg ht)).comp_hasDerivWithinAt t AffineMap.hasDerivWithinAt_lineMap seg)
  have hc : ContinuousOn (fun t => q (F (line t))) (Icc (0 : ℝ) 1) :=
    fun t ht => (hd t ht).continuousWithinAt
  have hd' (t : ℝ) (ht : t ∈ interior (Icc (0 : ℝ) 1)) :
      HasDerivAt (fun t => q (F (line t))) (q (J (line t) (h-g))) t :=
    (hd t (interior_subset ht)).hasDerivAt (mem_interior_iff_mem_nhds.mp ht)
  have hm := (convex_Icc (0 : ℝ) 1).mul_sub_le_image_sub_of_le_deriv hc
    (fun t ht => (hd' t ht).differentiableAt.differentiableWithinAt)
    (C := k) (fun t ht => by rw [(hd' t ht).deriv]; exact ha _ (seg (interior_subset ht)))
    0 (by simp) 1 (by simp) zero_le_one
  simpa [q, line, ← map_sub, inner_sub_right] using hm

omit [NormedSpace ℝ P] [InnerProductSpace ℂ H] in
/-- Stable lower and upper distances under a separately bounded additive error. -/
theorem perturbation_bounds {S : Set P} {F R : P → H} {lo hi t : ℝ}
    (hF : ∀ h ∈ S, ∀ g ∈ S,
      lo * ‖h-g‖ ≤ ‖F h-F g‖ ∧ ‖F h-F g‖ ≤ hi * ‖h-g‖)
    (hR : ∀ h ∈ S, ∀ g ∈ S, ‖R h-R g‖ ≤ t * ‖h-g‖) :
    ∀ h ∈ S, ∀ g ∈ S,
      (lo-t) * ‖h-g‖ ≤ ‖(F h+R h)-(F g+R g)‖ ∧
      ‖(F h+R h)-(F g+R g)‖ ≤ (hi+t) * ‖h-g‖ := by
  intro h hh g hg
  have hf := hF h hh g hg
  have hr := hR h hh g hg
  have hu := norm_add_le (F h-F g) (R h-R g)
  have hl := norm_sub_le ((F h+R h)-(F g+R g)) (R h-R g)
  rw [show (F h+R h)-(F g+R g)-(R h-R g) = F h-F g by abel] at hl
  rw [show (F h-F g)+(R h-R g) = (F h+R h)-(F g+R g) by abel] at hu
  constructor <;> nlinarith

omit [NormedSpace ℝ P] [InnerProductSpace ℂ H] in
theorem injective_of_lower_bound {S : Set P} {F : P → H} {c : ℝ} (hc : 0 < c)
    (hF : ∀ h ∈ S, ∀ g ∈ S, c * ‖h-g‖ ≤ ‖F h-F g‖) : Set.InjOn F S := by
  intro h hh g hg he
  have hb := hF h hh g hg
  rw [he, sub_self, norm_zero] at hb
  have : ‖h-g‖ = 0 := by nlinarith [norm_nonneg (h-g)]
  exact sub_eq_zero.mp (norm_eq_zero.mp this)

/-- A derivative bound on a convex set supplies the error Lipschitz premise. -/
theorem perturbation_derivative_bound {S : Set P} (hS : Convex ℝ S)
    {R : P → H} {J : P → P →L[ℝ] H} {t : ℝ}
    (hR : ∀ z ∈ S, HasFDerivWithinAt R (J z) S z)
    (hJ : ∀ z ∈ S, ‖J z‖ ≤ t) :
    ∀ h ∈ S, ∀ g ∈ S, ‖R h-R g‖ ≤ t * ‖h-g‖ := by
  intro h hh g hg
  exact hS.norm_image_sub_le_of_norm_hasFDerivWithin_le hR hJ hg hh
end Chord

/-- Isometric realification of parameter directions, with the Euclidean norm. -/
def complexify : EuclideanSpace ℝ ι →ₗᵢ[ℝ] EuclideanSpace ℂ ι where
  toFun x := toLp 2 (fun j => (x j : ℂ))
  map_add' x y := by ext j; simp
  map_smul' c x := by ext j; simp
  norm_map' x := by
    apply (sq_eq_sq₀ (norm_nonneg _) (norm_nonneg _)).mp
    simp [EuclideanSpace.norm_sq_eq]

def realDiag (d : ι → ℝ) : Matrix ι ι ℂ := Matrix.diagonal (fun j => (d j : ℂ))

theorem realDiag_norm {d : ι → ℝ} {u : ℝ} (hu : 0 ≤ u)
    (hd : ∀ j, |d j| ≤ u) : ‖realDiag d‖ ≤ u := by
  rw [realDiag, Matrix.l2_opNorm_diagonal]
  exact (pi_norm_le_iff_of_nonneg hu).mpr (by simpa using hd)

theorem realDiag_lower {d : ι → ℝ} {l : ℝ} (hl : 0 ≤ l)
    (hd : ∀ j, l ≤ d j) (x : EuclideanSpace ℂ ι) :
    l * ‖x‖ ≤ ‖(Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) (realDiag d) x‖ := by
  apply (sq_le_sq₀ (mul_nonneg hl (norm_nonneg _)) (norm_nonneg _)).mp
  simp only [mul_pow, EuclideanSpace.norm_sq_eq, realDiag,
    Matrix.ofLp_toEuclideanCLM, Matrix.mulVec_diagonal, norm_mul, Complex.norm_real,
    Real.norm_eq_abs, sq_abs, Finset.mul_sum]
  exact Finset.sum_le_sum (fun j _ => mul_le_mul_of_nonneg_right
    (pow_le_pow_left₀ hl (hd j) 2) (sq_nonneg _))

theorem realDiag_commute (d e : ι → ℝ) : realDiag d * realDiag e = realDiag e * realDiag d := by
  simp only [realDiag, Matrix.diagonal_mul_diagonal]
  congr 1
  ext j
  exact mul_comm _ _

variable {κ : Type*} [Fintype κ]

/-- Rectangular complex matrices represented by their canonical Euclidean operators. -/
abbrev Frame (ι κ : Type*) [Fintype ι] [Fintype κ] :=
  EuclideanSpace ℂ ι →L[ℂ] EuclideanSpace ℂ κ

def mixedGram (V0 V : Frame ι κ) : Matrix ι ι ℂ :=
  (Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)).symm (V0.adjoint.comp V)

/-- The derivative with respect to real parameters; D and E act on the right. -/
def chartDerivative (V : Frame ι κ) (d e : ι → ℝ) :
    EuclideanSpace ℝ ι →L[ℝ] EuclideanSpace ℂ κ :=
  ((V.comp ((Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) (realDiag d * realDiag e))).restrictScalars ℝ).comp
    complexify.toContinuousLinearMap

/-- The finite symbolic hypotheses of the conditional XF-186 chart. Frame fields are
exactly complex p-by-m matrices in the canonical orthonormal bases. -/
structure Chart (ι κ : Type*) [Fintype ι] [DecidableEq ι] [Fintype κ] where
  S : Set (EuclideanSpace ℝ ι)
  convex : Convex ℝ S
  F : EuclideanSpace ℝ ι → EuclideanSpace ℂ κ
  V0 : Frame ι κ
  V : EuclideanSpace ℝ ι → Frame ι κ
  d : ι → ℝ
  e : EuclideanSpace ℝ ι → ι → ℝ
  L : ℝ
  dm : ℝ
  dp : ℝ
  rho : ℝ
  eps : ℝ
  b : ℝ
  d0 : ℝ
  d1 : ℝ
  L_pos : 0 < L
  rho_nonneg : 0 ≤ rho
  dm_gt : rho < dm
  dp_nonneg : 0 ≤ dp
  eps_nonneg : 0 ≤ eps
  eps_lt : eps < 1
  margin_pos : 0 < margin dm dp rho eps
  b_pos : 0 < b
  d0_pos : 0 < d0
  d0_le_d1 : d0 ≤ d1
  d_lower : ∀ j, d0 ≤ d j
  d_upper : ∀ j, d j ≤ d1
  ref_norm : ‖V0‖ ≤ b * Real.sqrt L
  frame_norm : ∀ z ∈ S, ‖V z‖ ≤ b * Real.sqrt L
  gram : ∀ z ∈ S, GramBounds (mixedGram V0 (V z)) L dm dp rho
  damping : ∀ z ∈ S, ‖realDiag (e z) - 1‖ ≤ eps
  deriv : ∀ z ∈ S, HasFDerivWithinAt F (chartDerivative (V z) d (e z)) S z

namespace Chart
variable (T : Chart ι κ)

def lowerConstant : ℝ := margin T.dm T.dp T.rho T.eps * T.d0 ^ 2 / (T.b * T.d1)
def upperConstant : ℝ := T.b * T.d1 * (1 + T.eps)

theorem d1_pos : 0 < T.d1 := T.d0_pos.trans_le T.d0_le_d1

theorem diagonal_norm : ‖realDiag T.d‖ ≤ T.d1 :=
  realDiag_norm T.d1_pos.le (fun j => by
    rw [abs_of_nonneg (T.d0_pos.le.trans (T.d_lower j))]; exact T.d_upper j)

theorem damping_norm {z : EuclideanSpace ℝ ι} (hz : z ∈ T.S) :
    ‖realDiag (T.e z)‖ ≤ 1 + T.eps := by
  have h := norm_add_le (realDiag (T.e z) - 1) (1 : Matrix ι ι ℂ)
  rw [sub_add_cancel] at h
  have hi : ‖(1 : Matrix ι ι ℂ)‖ ≤ 1 := by
    rw [← Matrix.l2_opNorm_toEuclideanCLM, map_one]
    exact ContinuousLinearMap.norm_id_le
  linarith [T.damping z hz]

/-- The fixed anchor pairs with the actual derivative via the mixed Gram. -/
theorem anchored_differential {z : EuclideanSpace ℝ ι} (hz : z ∈ T.S)
    (v : EuclideanSpace ℝ ι) :
    margin T.dm T.dp T.rho T.eps * T.L *
        ‖(Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) (realDiag T.d) (complexify v)‖ ^ 2 ≤
      (inner ℂ (T.V0 ((Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) (realDiag T.d) (complexify v)))
        (chartDerivative (T.V z) T.d (T.e z) v)).re := by
  have h := damped_coercive (T.gram z hz) T.L_pos.le T.rho_nonneg T.dp_nonneg
    (T.damping z hz) ((Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) (realDiag T.d) (complexify v))
  rw [map_mul, mul_apply_eq_comp, mixedGram, StarAlgEquiv.apply_symm_apply,
    ContinuousLinearMap.comp_apply, ContinuousLinearMap.adjoint_inner_right] at h
  convert h using 1
  congr 2
  change T.V z ((Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) (realDiag T.d * realDiag (T.e z)) (complexify v)) = _
  rw [realDiag_commute, map_mul, mul_apply_eq_comp]

/-- The common-reference inequality survives the full nonlinear chord. -/
theorem anchored_chord {h g : EuclideanSpace ℝ ι} (hh : h ∈ T.S) (hg : g ∈ T.S) :
    margin T.dm T.dp T.rho T.eps * T.L *
        ‖(Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) (realDiag T.d) (complexify (h-g))‖ ^ 2 ≤
      (inner ℂ (T.V0 ((Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) (realDiag T.d) (complexify (h-g))))
        (T.F h-T.F g)).re :=
  Mathia.XF186.anchored_chord T.convex T.deriv hh hg _
    (fun _ hz => T.anchored_differential hz (h-g))

theorem derivative_norm {z : EuclideanSpace ℝ ι} (hz : z ∈ T.S) :
    ‖chartDerivative (T.V z) T.d (T.e z)‖ ≤ T.upperConstant * Real.sqrt T.L := by
  apply ContinuousLinearMap.opNorm_le_bound _ (by
    dsimp [upperConstant]
    exact mul_nonneg (mul_nonneg (mul_nonneg T.b_pos.le T.d1_pos.le)
      (by linarith [T.eps_nonneg])) (Real.sqrt_nonneg _))
  intro v
  change ‖T.V z ((Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι))
    (realDiag T.d * realDiag (T.e z)) (complexify v))‖ ≤ _
  have hm : ‖realDiag T.d * realDiag (T.e z)‖ ≤ T.d1 * (1+T.eps) :=
    (norm_mul_le _ _).trans (mul_le_mul T.diagonal_norm (T.damping_norm hz)
      (norm_nonneg _) T.d1_pos.le)
  have hx := ((Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι))
    (realDiag T.d * realDiag (T.e z))).le_of_opNorm_le
      (by simpa only [Matrix.l2_opNorm_toEuclideanCLM] using hm) (complexify v)
  rw [complexify.norm_map] at hx
  calc
    _ ≤ (T.b * Real.sqrt T.L) * ‖(Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι))
        (realDiag T.d * realDiag (T.e z)) (complexify v)‖ :=
      (T.V z).le_of_opNorm_le (T.frame_norm z hz) _
    _ ≤ (T.b * Real.sqrt T.L) * (T.d1 * (1+T.eps) * ‖v‖) :=
      mul_le_mul_of_nonneg_left hx (mul_nonneg T.b_pos.le (Real.sqrt_nonneg _))
    _ = _ := by dsimp [upperConstant]; ring

theorem upper_bound {h g : EuclideanSpace ℝ ι} (hh : h ∈ T.S) (hg : g ∈ T.S) :
    ‖T.F h-T.F g‖ ≤ T.upperConstant * Real.sqrt T.L * ‖h-g‖ :=
  T.convex.norm_image_sub_le_of_norm_hasFDerivWithin_le T.deriv
    (fun _ hz => T.derivative_norm hz) hg hh

theorem lowerConstant_pos : 0 < T.lowerConstant := by
  dsimp [lowerConstant]
  exact div_pos (mul_pos T.margin_pos (sq_pos_of_pos T.d0_pos))
    (mul_pos T.b_pos T.d1_pos)

/-- Cauchy--Schwarz applied to the common anchor gives the issue's exact lower
constant. The zero chord is handled before cancelling its length. -/
theorem lower_bound {h g : EuclideanSpace ℝ ι} (hh : h ∈ T.S) (hg : g ∈ T.S) :
    T.lowerConstant * Real.sqrt T.L * ‖h-g‖ ≤ ‖T.F h-T.F g‖ := by
  by_cases he : h = g
  · simp [he]
  have hv : 0 < ‖h-g‖ := norm_pos_iff.mpr (sub_ne_zero.mpr he)
  let x := (Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) (realDiag T.d) (complexify (h-g))
  have hxlo : T.d0 * ‖h-g‖ ≤ ‖x‖ := by
    simpa only [x, complexify.norm_map] using realDiag_lower T.d0_pos.le T.d_lower (complexify (h-g))
  have hxhi : ‖x‖ ≤ T.d1 * ‖h-g‖ := by
    simpa only [x, complexify.norm_map] using ((Matrix.toEuclideanCLM (𝕜 := ℂ) (n := ι)) (realDiag T.d)).le_of_opNorm_le
      (by simpa only [Matrix.l2_opNorm_toEuclideanCLM] using T.diagonal_norm) (complexify (h-g))
  have ha : ‖T.V0 x‖ ≤ T.b * Real.sqrt T.L * T.d1 * ‖h-g‖ := by
    calc
      _ ≤ (T.b * Real.sqrt T.L) * ‖x‖ := T.V0.le_of_opNorm_le T.ref_norm x
      _ ≤ (T.b * Real.sqrt T.L) * (T.d1 * ‖h-g‖) :=
        mul_le_mul_of_nonneg_left hxhi (mul_nonneg T.b_pos.le (Real.sqrt_nonneg _))
      _ = _ := by ring
  have han := T.anchored_chord hh hg
  change margin T.dm T.dp T.rho T.eps * T.L * ‖x‖ ^ 2 ≤
    (inner ℂ (T.V0 x) (T.F h-T.F g)).re at han
  have hcs := (Complex.re_le_norm _).trans (norm_inner_le_norm (𝕜 := ℂ) (T.V0 x) (T.F h-T.F g))
  have hx2 := pow_le_pow_left₀ (mul_nonneg T.d0_pos.le (norm_nonneg _)) hxlo 2
  have hmain : margin T.dm T.dp T.rho T.eps * T.L * T.d0 ^ 2 * ‖h-g‖ ^ 2 ≤
      (T.b * Real.sqrt T.L * T.d1 * ‖h-g‖) * ‖T.F h-T.F g‖ := by
    have hl := mul_le_mul_of_nonneg_left hx2 (mul_nonneg T.margin_pos.le T.L_pos.le)
    have hu := mul_le_mul_of_nonneg_right ha (norm_nonneg (T.F h-T.F g))
    nlinarith
  have hc : margin T.dm T.dp T.rho T.eps * T.d0 ^ 2 * Real.sqrt T.L * ‖h-g‖ ≤
      T.b * T.d1 * ‖T.F h-T.F g‖ := by
    apply (mul_le_mul_iff_right₀ (mul_pos (Real.sqrt_pos.mpr T.L_pos) hv)).mp
    convert hmain using 1 <;> ring_nf
    rw [Real.sq_sqrt T.L_pos.le]
    ring
  dsimp [lowerConstant]
  rw [div_mul_eq_mul_div, div_mul_eq_mul_div]
  exact (div_le_iff₀ (mul_pos T.b_pos T.d1_pos)).mpr (by nlinarith [hc])

/-- The finite mixed-Gram specialization gives the full two-sided chart bound. -/
theorem bounds {h g : EuclideanSpace ℝ ι} (hh : h ∈ T.S) (hg : g ∈ T.S) :
    T.lowerConstant * Real.sqrt T.L * ‖h-g‖ ≤ ‖T.F h-T.F g‖ ∧
    ‖T.F h-T.F g‖ ≤ T.upperConstant * Real.sqrt T.L * ‖h-g‖ :=
  ⟨T.lower_bound hh hg, T.upper_bound hh hg⟩

/-- Error size is in units of sqrt(L); the lower and upper constants lose/gain tau. -/
theorem perturbed_bounds (R : EuclideanSpace ℝ ι → EuclideanSpace ℂ κ) {tau : ℝ}
    (hR : ∀ h ∈ T.S, ∀ g ∈ T.S, ‖R h-R g‖ ≤ tau * Real.sqrt T.L * ‖h-g‖)
    {h g : EuclideanSpace ℝ ι} (hh : h ∈ T.S) (hg : g ∈ T.S) :
    (T.lowerConstant-tau) * Real.sqrt T.L * ‖h-g‖ ≤ ‖(T.F h+R h)-(T.F g+R g)‖ ∧
    ‖(T.F h+R h)-(T.F g+R g)‖ ≤ (T.upperConstant+tau) * Real.sqrt T.L * ‖h-g‖ := by
  simpa only [sub_mul, add_mul] using perturbation_bounds
    (fun _ hx _ hy => T.bounds hx hy) hR h hh g hg

theorem perturbed_injective (R : EuclideanSpace ℝ ι → EuclideanSpace ℂ κ) {tau : ℝ}
    (_htau : 0 ≤ tau) (ht : tau < T.lowerConstant)
    (hR : ∀ h ∈ T.S, ∀ g ∈ T.S, ‖R h-R g‖ ≤ tau * Real.sqrt T.L * ‖h-g‖) :
    Set.InjOn (fun h => T.F h+R h) T.S :=
  injective_of_lower_bound (mul_pos (sub_pos.mpr ht) (Real.sqrt_pos.mpr T.L_pos))
    (fun _ hh _ hg => (T.perturbed_bounds R hR hh hg).1)

/-- Sufficient real derivative control for the additive reciprocal-image model. -/
theorem perturbed_of_derivative_bound
    (R : EuclideanSpace ℝ ι → EuclideanSpace ℂ κ)
    (J : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι →L[ℝ] EuclideanSpace ℂ κ)
    {tau : ℝ} (htau : 0 ≤ tau) (ht : tau < T.lowerConstant)
    (hR : ∀ z ∈ T.S, HasFDerivWithinAt R (J z) T.S z)
    (hJ : ∀ z ∈ T.S, ‖J z‖ ≤ tau * Real.sqrt T.L) :
    Set.InjOn (fun h => T.F h+R h) T.S ∧
    ∀ h ∈ T.S, ∀ g ∈ T.S,
      (T.lowerConstant-tau) * Real.sqrt T.L * ‖h-g‖ ≤ ‖(T.F h+R h)-(T.F g+R g)‖ ∧
      ‖(T.F h+R h)-(T.F g+R g)‖ ≤ (T.upperConstant+tau) * Real.sqrt T.L * ‖h-g‖ := by
  have hr := perturbation_derivative_bound T.convex hR hJ
  exact ⟨T.perturbed_injective R htau ht hr, fun _ hh _ hg => T.perturbed_bounds R hr hh hg⟩

end Chart
end Mathia.XF186
