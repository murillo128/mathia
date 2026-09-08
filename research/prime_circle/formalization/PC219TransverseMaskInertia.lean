import PC218TransverseMaskRank
import Mathlib.LinearAlgebra.Dimension.Finite
import Mathlib.LinearAlgebra.Matrix.Hermitian
import Mathlib.LinearAlgebra.Pi

/-!
# PC-219: transverse-mask inertia and cyclotomic coefficient signs

Associated finding:
`research/prime_circle/findings/PC-219-full-transverse-mask-inertia-equals-cyclotomic-coefficient-sign-counts.md`

Formalized theorem boundary:
Lean verifies the finite Hermitian inertia/signature theorem and its algebraic bridge.  Inertia is
expressed intrinsically as the maximal complex dimensions of positive- and negative-definite
subspaces of the matrix quadratic form, together with the complex dimension of its kernel.

Not formalized:
coefficient-sign asymptotics, the nonzero spectrum or eigenvectors, cross-level structure, the
source Hilbert-space compression outside the finite matrix bridge inherited from PC-218, or any
RH-facing consequence.
-/

noncomputable section

open scoped BigOperators ComplexConjugate ComplexOrder Matrix

namespace Mathia.PC219

/-- The real quadratic value of a complex matrix.  For a Hermitian matrix this is its ordinary
Hermitian quadratic form, regarded as a real-valued function. -/
def matrixForm {I : Type*} [Fintype I] (H : Matrix I I ℂ) (x : I → ℂ) : ℝ :=
  (star x ⬝ᵥ (H *ᵥ x)).re

lemma dotProduct_conjTranspose_mulVec {I J : Type*} [Fintype I] [Fintype J]
    (A : Matrix I J ℂ) (x : J → ℂ) (y : I → ℂ) :
    star x ⬝ᵥ (A.conjTranspose *ᵥ y) = star (A *ᵥ x) ⬝ᵥ y := by
  rw [Matrix.dotProduct_mulVec, Matrix.vecMul_conjTranspose]
  simp

/-- A complex subspace is positive definite for a real-valued quadratic function. -/
def PositiveOn {E : Type*} [AddCommGroup E] [Module ℂ E]
    (q : E → ℝ) (V : Submodule ℂ E) : Prop :=
  ∀ x : V, x ≠ 0 → 0 < q x

open scoped Classical in
/-- The maximal complex dimension of a positive-definite subspace. -/
def positiveIndex {E : Type*} [AddCommGroup E] [Module ℂ E]
    [FiniteDimensional ℂ E] (q : E → ℝ) : ℕ :=
  Finset.max' {r ∈ Finset.Iic (Module.finrank ℂ E) |
      ∃ V : Submodule ℂ E, Module.finrank ℂ V = r ∧ PositiveOn q V}
    ⟨Module.finrank ℂ (⊥ : Submodule ℂ E), by
      simp only [Finset.mem_filter, Finset.mem_Iic]
      refine ⟨Submodule.finrank_le _, ⊥, rfl, ?_⟩
      intro x hx
      exact (hx (Subsingleton.elim x 0)).elim⟩

/-- The maximal complex dimension of a negative-definite subspace. -/
def negativeIndex {E : Type*} [AddCommGroup E] [Module ℂ E]
    [FiniteDimensional ℂ E] (q : E → ℝ) : ℕ :=
  positiveIndex (-q)

lemma positiveIndex_isGreatest {E : Type*} [AddCommGroup E] [Module ℂ E]
    [FiniteDimensional ℂ E] (q : E → ℝ) :
    IsGreatest
      {r | ∃ V : Submodule ℂ E, Module.finrank ℂ V = r ∧ PositiveOn q V}
      (positiveIndex q) := by
  classical
  unfold positiveIndex
  constructor
  · exact (Finset.mem_filter.mp (Finset.max'_mem _ _)).2
  · rintro _ ⟨V, rfl, hV⟩
    apply Finset.le_max'
    rw [Finset.mem_filter, Finset.mem_Iic]
    exact ⟨V.finrank_le, V, rfl, hV⟩

lemma exists_positiveIndex_subspace {E : Type*} [AddCommGroup E] [Module ℂ E]
    [FiniteDimensional ℂ E] (q : E → ℝ) :
    ∃ V : Submodule ℂ E,
      Module.finrank ℂ V = positiveIndex q ∧ PositiveOn q V :=
  (positiveIndex_isGreatest q).1

lemma le_positiveIndex {E : Type*} [AddCommGroup E] [Module ℂ E]
    [FiniteDimensional ℂ E] {q : E → ℝ} {V : Submodule ℂ E}
    (hV : PositiveOn q V) :
    Module.finrank ℂ V ≤ positiveIndex q :=
  (positiveIndex_isGreatest q).2 ⟨V, rfl, hV⟩

lemma positiveIndex_comp_range {E F : Type*}
    [AddCommGroup E] [Module ℂ E] [FiniteDimensional ℂ E]
    [AddCommGroup F] [Module ℂ F] [FiniteDimensional ℂ F]
    (f : E →ₗ[ℂ] F) (q : F → ℝ) (hq0 : q 0 = 0) :
    positiveIndex (fun x ↦ q (f x)) =
      positiveIndex (fun y : LinearMap.range f ↦ q y) := by
  classical
  apply le_antisymm
  · obtain ⟨V, hVdim, hVpos⟩ := exists_positiveIndex_subspace (fun x ↦ q (f x))
    let g : V →ₗ[ℂ] LinearMap.range f := f.rangeRestrict.comp V.subtype
    have hg_inj : Function.Injective g := by
      rw [← LinearMap.ker_eq_bot]
      rw [LinearMap.ker_eq_bot']
      intro x hx
      by_contra hx0
      have hpos := hVpos x hx0
      have hfx : f x = 0 := congrArg Subtype.val hx
      change 0 < q (f x) at hpos
      rw [hfx, hq0] at hpos
      exact (lt_irrefl 0 hpos).elim
    have hgdim : Module.finrank ℂ (LinearMap.range g) = Module.finrank ℂ V :=
      LinearMap.finrank_range_of_inj hg_inj
    have hgpos : PositiveOn (fun y : LinearMap.range f ↦ q y) (LinearMap.range g) := by
      intro y hy
      obtain ⟨x, hx⟩ := y.property
      have hx0 : x ≠ 0 := by
        intro hxzero
        apply hy
        apply Subtype.ext
        simpa [hxzero] using hx.symm
      have hval : (y : LinearMap.range f) = g x := by
        apply Subtype.ext
        exact congrArg Subtype.val hx.symm
      rw [hval]
      exact hVpos x hx0
    rw [← hVdim, ← hgdim]
    exact le_positiveIndex hgpos
  · obtain ⟨W, hWdim, hWpos⟩ :=
      exists_positiveIndex_subspace (fun y : LinearMap.range f ↦ q y)
    obtain ⟨g, hg⟩ :=
      f.rangeRestrict.exists_rightInverse_of_surjective f.range_rangeRestrict
    have hg_right : Function.RightInverse g f.rangeRestrict := LinearMap.congr_fun hg
    have hg_inj : Function.Injective g := hg_right.injective
    let k : W →ₗ[ℂ] E := g.comp W.subtype
    have hk_inj : Function.Injective k := hg_inj.comp Subtype.val_injective
    have hkdim : Module.finrank ℂ (LinearMap.range k) = Module.finrank ℂ W :=
      LinearMap.finrank_range_of_inj hk_inj
    have hkpos : PositiveOn (fun x ↦ q (f x)) (LinearMap.range k) := by
      intro y hy
      obtain ⟨x, hx⟩ := y.property
      have hx0 : x ≠ 0 := by
        intro hxzero
        apply hy
        apply Subtype.ext
        simpa [hxzero] using hx.symm
      have hyval : (y : E) = k x := hx.symm
      rw [hyval]
      have hfg : f (g x) = x := by
        exact congrArg Subtype.val (hg_right x)
      change 0 < q (f (g x))
      rw [hfg]
      exact hWpos x hx0
    rw [← hWdim, ← hkdim]
    exact le_positiveIndex hkpos

lemma negativeIndex_comp_range {E F : Type*}
    [AddCommGroup E] [Module ℂ E] [FiniteDimensional ℂ E]
    [AddCommGroup F] [Module ℂ F] [FiniteDimensional ℂ F]
    (f : E →ₗ[ℂ] F) (q : F → ℝ) (hq0 : q 0 = 0) :
    negativeIndex (fun x ↦ q (f x)) =
      negativeIndex (fun y : LinearMap.range f ↦ q y) := by
  unfold negativeIndex
  apply positiveIndex_comp_range f (-q)
  simp [hq0]

lemma positiveIndex_submodule_eq {E : Type*} [AddCommGroup E] [Module ℂ E]
    [FiniteDimensional ℂ E]
    {S T : Submodule ℂ E} (q : E → ℝ) (h : S = T) :
    positiveIndex (fun x : S ↦ q x) = positiveIndex (fun x : T ↦ q x) := by
  subst T
  rfl

lemma negativeIndex_submodule_eq {E : Type*} [AddCommGroup E] [Module ℂ E]
    [FiniteDimensional ℂ E]
    {S T : Submodule ℂ E} (q : E → ℝ) (h : S = T) :
    negativeIndex (fun x : S ↦ q x) = negativeIndex (fun x : T ↦ q x) := by
  subst T
  rfl

lemma positiveIndex_pos_mul {E : Type*} [AddCommGroup E] [Module ℂ E]
    [FiniteDimensional ℂ E] (q : E → ℝ) {a : ℝ} (ha : 0 < a) :
    positiveIndex (fun x ↦ a * q x) = positiveIndex q := by
  apply le_antisymm
  · obtain ⟨V, hVdim, hVpos⟩ := exists_positiveIndex_subspace (fun x ↦ a * q x)
    rw [← hVdim]
    apply le_positiveIndex
    intro x hx
    have hp := hVpos x hx
    nlinarith
  · obtain ⟨V, hVdim, hVpos⟩ := exists_positiveIndex_subspace q
    rw [← hVdim]
    apply le_positiveIndex
    intro x hx
    exact mul_pos ha (hVpos x hx)

lemma negativeIndex_pos_mul {E : Type*} [AddCommGroup E] [Module ℂ E]
    [FiniteDimensional ℂ E] (q : E → ℝ) {a : ℝ} (ha : 0 < a) :
    negativeIndex (fun x ↦ a * q x) = negativeIndex q := by
  unfold negativeIndex
  have hfun : -(fun x ↦ a * q x) = fun x ↦ a * (-q) x := by
    funext x
    simp
  rw [hfun, positiveIndex_pos_mul (-q) ha]

lemma matrixForm_ofReal_smul {I : Type*} [Fintype I]
    (H : Matrix I I ℂ) (a : ℝ) (x : I → ℂ) :
    matrixForm ((a : ℂ) • H) x = a * matrixForm H x := by
  rw [matrixForm, matrixForm, Matrix.smul_mulVec, dotProduct_smul]
  simp

/-- Removing the kernel of a complex linear functional whose complementary line is strictly
positive removes exactly one positive square and no negative square.  The displayed decomposition
identity is the coordinate-free content of orthogonality of that line and the kernel. -/
theorem indices_on_ker_of_positive_line {E : Type*}
    [AddCommGroup E] [Module ℂ E] [FiniteDimensional ℂ E]
    (q : E → ℝ) (c : E →ₗ[ℂ] ℂ) (e : E)
    (hq0 : q 0 = 0) (hce : c e = 1) (he : 0 < q e)
    (hdecomp : ∀ x, q x = Complex.normSq (c x) * q e + q (x - c x • e)) :
    positiveIndex (fun x : LinearMap.ker c ↦ q x) = positiveIndex q - 1 ∧
      negativeIndex (fun x : LinearMap.ker c ↦ q x) = negativeIndex q := by
  classical
  let K : Submodule ℂ E := LinearMap.ker c
  have hKmem (x : E) : x - c x • e ∈ K := by
    change c (x - c x • e) = 0
    simp [hce]
  have hqsplit (z : ℂ) (x : K) :
      q (z • e + x) = Complex.normSq z * q e + q x := by
    rw [hdecomp]
    have hcx : c (z • e + (x : E)) = z := by
      simp [hce]
    rw [hcx]
    congr 1
    simp

  have hpos_upper :
      positiveIndex (fun x : K ↦ q x) ≤ positiveIndex q - 1 := by
    obtain ⟨W, hWdim, hWpos⟩ :=
      exists_positiveIndex_subspace (fun x : K ↦ q x)
    let f : ℂ × W →ₗ[ℂ] E :=
      (LinearMap.fst ℂ ℂ W).smulRight e +
        (K.subtype.comp W.subtype).comp (LinearMap.snd ℂ ℂ W)
    have hf_inj : Function.Injective f := by
      intro x y hxy
      have hcxy := congrArg c hxy
      have hfirst : x.1 = y.1 := by
        simpa [f, hce, x.2.property, y.2.property] using hcxy
      apply Prod.ext hfirst
      apply Subtype.ext
      apply Subtype.ext
      change x.1 • e + (x.2 : E) = y.1 • e + (y.2 : E) at hxy
      rw [hfirst] at hxy
      exact add_left_cancel hxy
    have hfpos : PositiveOn q (LinearMap.range f) := by
      intro y hy
      obtain ⟨x, hx⟩ := y.property
      have hx0 : x ≠ 0 := by
        intro hxzero
        apply hy
        apply Subtype.ext
        simpa [hxzero] using hx.symm
      have hyval : (y : E) = f x := hx.symm
      rw [hyval]
      change 0 < q (x.1 • e + (x.2 : E))
      rw [hqsplit]
      have hleft : 0 ≤ Complex.normSq x.1 * q e :=
        mul_nonneg (Complex.normSq_nonneg _) he.le
      by_cases hx2 : x.2 = 0
      · have hx1 : x.1 ≠ 0 := by
          intro hx1
          exact hx0 (Prod.ext hx1 hx2)
        exact add_pos_of_pos_of_nonneg
          (mul_pos (Complex.normSq_pos.mpr hx1) he) (by simp [hx2, hq0])
      · exact add_pos_of_nonneg_of_pos hleft (hWpos x.2 hx2)
    have hfdim : Module.finrank ℂ (LinearMap.range f) = 1 + Module.finrank ℂ W := by
      rw [LinearMap.finrank_range_of_inj hf_inj, Module.finrank_prod]
      simp
    have hle := le_positiveIndex hfpos
    rw [hfdim, hWdim] at hle
    omega

  have hpos_lower :
      positiveIndex q - 1 ≤ positiveIndex (fun x : K ↦ q x) := by
    obtain ⟨P, hPdim, hPpos⟩ := exists_positiveIndex_subspace q
    let cp : P →ₗ[ℂ] ℂ := c.comp P.subtype
    let KP : Submodule ℂ P := LinearMap.ker cp
    let toK : KP →ₗ[ℂ] K :=
      { toFun := fun x ↦ ⟨(x : E), x.property⟩
        map_add' := by intro x y; rfl
        map_smul' := by intro z x; rfl }
    have htoK_inj : Function.Injective toK := by
      intro x y hxy
      apply Subtype.ext
      apply Subtype.ext
      simpa [toK] using congrArg Subtype.val hxy
    have htoKpos : PositiveOn (fun x : K ↦ q x) (LinearMap.range toK) := by
      intro y hy
      obtain ⟨x, hx⟩ := y.property
      have hx0 : x ≠ 0 := by
        intro hxzero
        apply hy
        apply Subtype.ext
        simpa [hxzero] using hx.symm
      have hyval : (y : K) = toK x := by
        apply Subtype.ext
        exact congrArg Subtype.val hx.symm
      rw [hyval]
      exact hPpos x (fun h ↦ hx0 (Subtype.ext h))
    have htoKdim : Module.finrank ℂ (LinearMap.range toK) = Module.finrank ℂ KP :=
      LinearMap.finrank_range_of_inj htoK_inj
    have hranknull := LinearMap.finrank_range_add_finrank_ker cp
    have hrange : Module.finrank ℂ (LinearMap.range cp) ≤ 1 := by
      simpa using (LinearMap.range cp).finrank_le
    have hKP : positiveIndex q - 1 ≤ Module.finrank ℂ KP := by
      rw [← hPdim]
      change Module.finrank ℂ P - 1 ≤ Module.finrank ℂ (LinearMap.ker cp)
      omega
    exact hKP.trans (htoKdim ▸ le_positiveIndex htoKpos)

  have hneg_upper :
      negativeIndex (fun x : K ↦ q x) ≤ negativeIndex q := by
    obtain ⟨W, hWdim, hWpos⟩ :=
      exists_positiveIndex_subspace (fun x : K ↦ (-q) x)
    let f : W →ₗ[ℂ] E := K.subtype.comp W.subtype
    have hf_inj : Function.Injective f :=
      Subtype.val_injective.comp Subtype.val_injective
    have hfpos : PositiveOn (-q) (LinearMap.range f) := by
      intro y hy
      obtain ⟨x, hx⟩ := y.property
      have hx0 : x ≠ 0 := by
        intro hxzero
        apply hy
        apply Subtype.ext
        simpa [hxzero] using hx.symm
      have hyval : (y : E) = f x := hx.symm
      rw [hyval]
      exact hWpos x hx0
    unfold negativeIndex
    calc
      positiveIndex (fun x : K ↦ -q x) = Module.finrank ℂ W := by
        simpa only [Pi.neg_apply] using hWdim.symm
      _ = Module.finrank ℂ (LinearMap.range f) :=
        (LinearMap.finrank_range_of_inj hf_inj).symm
      _ ≤ positiveIndex (fun x : E ↦ -q x) := le_positiveIndex hfpos

  have hneg_lower :
      negativeIndex q ≤ negativeIndex (fun x : K ↦ q x) := by
    obtain ⟨N, hNdim, hNpos⟩ := exists_positiveIndex_subspace (-q)
    let proj : E →ₗ[ℂ] E := LinearMap.id - c.smulRight e
    let projK : E →ₗ[ℂ] K := proj.codRestrict K (by
      intro x
      simpa [proj] using hKmem x)
    let f : N →ₗ[ℂ] K := projK.comp N.subtype
    have hf_inj : Function.Injective f := by
      rw [← LinearMap.ker_eq_bot, LinearMap.ker_eq_bot']
      intro x hx
      by_contra hx0
      have hn := hNpos x hx0
      have hprojzero : (x : E) - c x • e = 0 := by
        have h := congrArg Subtype.val hx
        simpa [f, projK, proj] using h
      have hdec := hdecomp (x : E)
      rw [hprojzero, hq0] at hdec
      have hnonneg : 0 ≤ q (x : E) := by
        rw [hdec]
        exact add_nonneg (mul_nonneg (Complex.normSq_nonneg _) he.le) le_rfl
      have hn' : q (x : E) < 0 := by simpa using hn
      exact (not_lt_of_ge hnonneg hn').elim
    have hfpos : PositiveOn (fun x : K ↦ (-q) x) (LinearMap.range f) := by
      intro y hy
      obtain ⟨x, hx⟩ := y.property
      have hx0 : x ≠ 0 := by
        intro hxzero
        apply hy
        apply Subtype.ext
        simpa [hxzero] using hx.symm
      have hyval : (y : K) = f x := by
        apply Subtype.ext
        exact congrArg Subtype.val hx.symm
      rw [hyval]
      have hn := hNpos x hx0
      have hn' : q (x : E) < 0 := by simpa using hn
      have hdec := hdecomp (x : E)
      have hnonneg : 0 ≤ Complex.normSq (c (x : E)) * q e :=
        mul_nonneg (Complex.normSq_nonneg _) he.le
      change 0 < -q (projK x)
      change 0 < -q ((x : E) - c x • e)
      nlinarith
    unfold negativeIndex
    calc
      positiveIndex (-q) = Module.finrank ℂ N := hNdim.symm
      _ = Module.finrank ℂ (LinearMap.range f) :=
        (LinearMap.finrank_range_of_inj hf_inj).symm
      _ ≤ positiveIndex (fun x : K ↦ (-q) x) := le_positiveIndex hfpos
      _ = positiveIndex (-(fun x : K ↦ q x)) := by
        congr 1

  constructor
  · exact le_antisymm hpos_upper hpos_lower
  · exact le_antisymm hneg_upper hneg_lower

lemma positiveIndex_add_finrank_le_of_nonpos {E : Type*}
    [AddCommGroup E] [Module ℂ E] [FiniteDimensional ℂ E]
    (q : E → ℝ) {V : Submodule ℂ E} (hV : ∀ x ∈ V, q x ≤ 0) :
    positiveIndex q + Module.finrank ℂ V ≤ Module.finrank ℂ E := by
  obtain ⟨P, hr, hP⟩ := exists_positiveIndex_subspace q
  rw [← hr]
  apply Submodule.finrank_add_finrank_le_of_disjoint
  intro W hWP hWV
  rw [le_bot_iff, Submodule.eq_bot_iff]
  intro x hx
  by_contra hx0
  have hp := hP ⟨x, hWP hx⟩ (by simpa using hx0)
  have hn := hV x (hWV hx)
  linarith

/-- The diagonal Hermitian quadratic form with real weights. -/
def diagonalForm {I : Type*} [Fintype I] (d : I → ℝ) (x : I → ℂ) : ℝ :=
  ∑ i, d i * Complex.normSq (x i)

lemma positiveOn_diagonal_span {I : Type*} [Fintype I]
    (d : I → ℝ) (s : Set I) (hs : ∀ i ∈ s, 0 < d i) :
    PositiveOn (diagonalForm d) (Pi.spanSubset ℂ s) := by
  classical
  intro x hx
  rw [diagonalForm]
  apply Finset.sum_pos'
  · intro i _
    by_cases hi : i ∈ s
    · exact mul_nonneg (hs i hi).le (Complex.normSq_nonneg _)
    · rw [Pi.mem_spanSubset_iff.mp x.property i hi]
      simp
  · have hx' : ∃ i, (x : I → ℂ) i ≠ 0 := by
      by_contra hall
      apply hx
      apply Subtype.ext
      funext i
      simp only [not_exists, not_not] at hall
      exact hall i
    obtain ⟨i, hi⟩ := hx'
    have his : i ∈ s := by
      contrapose hi
      exact Pi.mem_spanSubset_iff.mp x.property i hi
    exact ⟨i, Finset.mem_univ _, mul_pos (hs i his) (Complex.normSq_pos.mpr hi)⟩

lemma nonposOn_diagonal_span {I : Type*} [Fintype I]
    (d : I → ℝ) (s : Set I) (hs : ∀ i ∈ s, d i ≤ 0) :
    ∀ x ∈ Pi.spanSubset ℂ s, diagonalForm d x ≤ 0 := by
  classical
  intro x hx
  rw [diagonalForm]
  apply Finset.sum_nonpos
  intro i _
  by_cases hi : i ∈ s
  · exact mul_nonpos_of_nonpos_of_nonneg (hs i hi) (Complex.normSq_nonneg _)
  · rw [Pi.mem_spanSubset_iff.mp hx i hi]
    simp

theorem diagonalForm_positiveIndex {I : Type*} [Fintype I] (d : I → ℝ) :
    positiveIndex (diagonalForm d) = {i | 0 < d i}.ncard := by
  classical
  let p : Set I := {i | 0 < d i}
  let m : Set I := {i | d i ≤ 0}
  have hcard : p.ncard + m.ncard = Nat.card I := by
    convert Set.ncard_add_ncard_compl p
    ext i
    simp [p, m]
  have hposlower : p.ncard ≤ positiveIndex (diagonalForm d) := by
    simpa [Pi.dim_spanSubset] using
      le_positiveIndex (positiveOn_diagonal_span d p (by simp [p]))
  have hposupper : positiveIndex (diagonalForm d) ≤ p.ncard := by
    have hle := positiveIndex_add_finrank_le_of_nonpos (diagonalForm d)
      (nonposOn_diagonal_span d m (by simp [m]))
    rw [Pi.dim_spanSubset] at hle
    have hfinrank : Module.finrank ℂ (I → ℂ) = Nat.card I := by simp
    rw [hfinrank] at hle
    omega
  exact le_antisymm hposupper hposlower

/-- Positive and negative indices of a real diagonal Hermitian form are exactly its sign counts. -/
theorem diagonalForm_indices {I : Type*} [Fintype I] (d : I → ℝ) :
    positiveIndex (diagonalForm d) = {i | 0 < d i}.ncard ∧
      negativeIndex (diagonalForm d) = {i | d i < 0}.ncard := by
  constructor
  · exact diagonalForm_positiveIndex d
  · unfold negativeIndex
    have hfun : -(diagonalForm d) = diagonalForm (-d) := by
      funext x
      simp [diagonalForm]
    rw [hfun, diagonalForm_positiveIndex]
    congr 1
    ext i
    simp

/-- The complex-linear weighted coordinate sum attached to real diagonal weights. -/
def weightSum {I : Type*} [Fintype I] (d : I → ℝ) : (I → ℂ) →ₗ[ℂ] ℂ where
  toFun x := ∑ i, (d i : ℂ) * x i
  map_add' x y := by simp [mul_add, Finset.sum_add_distrib]
  map_smul' z x := by
    simp only [Pi.smul_apply, RingHom.id_apply, smul_eq_mul]
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro i _
    ring

@[simp] lemma weightSum_apply {I : Type*} [Fintype I] (d : I → ℝ) (x : I → ℂ) :
    weightSum d x = ∑ i, (d i : ℂ) * x i := rfl

/-- Completing the square along the all-ones direction for a real diagonal Hermitian form. -/
lemma diagonalForm_positiveLine_decomposition {I : Type*} [Fintype I]
    (d : I → ℝ) (hs : 0 < ∑ i, d i) (x : I → ℂ) :
    diagonalForm d x =
      Complex.normSq (((∑ i, d i : ℝ) : ℂ)⁻¹ * weightSum d x) * (∑ i, d i) +
        diagonalForm d
          (x - (((∑ i, d i : ℝ) : ℂ)⁻¹ * weightSum d x) • (fun _ ↦ 1)) := by
  classical
  let s : ℝ := ∑ i, d i
  let z : ℂ := (s : ℂ)⁻¹ * weightSum d x
  have hs0 : s ≠ 0 := ne_of_gt hs
  have hweighted : weightSum d x = (s : ℂ) * z := by
    dsimp [z]
    rw [← mul_assoc, mul_inv_cancel₀ (by exact_mod_cast hs0), one_mul]
  have hcross : ∑ i, d i * (x i * star z).re = Complex.normSq z * s := by
    calc
      ∑ i, d i * (x i * star z).re =
          (∑ i, (d i : ℂ) * (x i * star z)).re := by
            simp
      _ = ((weightSum d x) * star z).re := by
            rw [weightSum_apply, Finset.sum_mul]
            apply congrArg Complex.re
            apply Finset.sum_congr rfl
            intro i _
            ring
      _ = (((s : ℂ) * z) * star z).re := by rw [hweighted]
      _ = Complex.normSq z * s := by
            rw [mul_assoc]
            change ((s : ℂ) * (z * (starRingEnd ℂ) z)).re = _
            rw [Complex.mul_conj]
            simp [mul_comm]
  change diagonalForm d x = Complex.normSq z * s + diagonalForm d (x - z • fun _ ↦ 1)
  rw [diagonalForm, diagonalForm]
  simp only [Pi.sub_apply, Pi.smul_apply, smul_eq_mul, mul_one, Complex.normSq_sub]
  have hconst : ∑ i, d i * Complex.normSq z = s * Complex.normSq z := by
    rw [← Finset.sum_mul]
  have hcross2 : ∑ i, d i * (2 * (x i * star z).re) =
      2 * (Complex.normSq z * s) := by
    calc
      ∑ i, d i * (2 * (x i * star z).re) =
          2 * ∑ i, d i * (x i * star z).re := by
            rw [Finset.mul_sum]
            apply Finset.sum_congr rfl
            intro i _
            ring
      _ = 2 * (Complex.normSq z * s) := by rw [hcross]
  change (∑ i, d i * (2 * (x i * (starRingEnd ℂ) z).re)) =
    2 * (Complex.normSq z * s) at hcross2
  simp_rw [mul_sub, mul_add]
  rw [Finset.sum_sub_distrib, Finset.sum_add_distrib, hconst]
  nlinarith [hcross2]

/-- The weighted sum normalized to take the all-ones vector to one when the weight sum is nonzero. -/
def normalizedWeightSum {I : Type*} [Fintype I] (d : I → ℝ) : (I → ℂ) →ₗ[ℂ] ℂ where
  toFun x := (((∑ i, d i : ℝ) : ℂ)⁻¹) * weightSum d x
  map_add' x y := by rw [map_add, mul_add]
  map_smul' z x := by
    simp only [map_smul, RingHom.id_apply, smul_eq_mul]
    ring

@[simp] lemma normalizedWeightSum_apply {I : Type*} [Fintype I]
    (d : I → ℝ) (x : I → ℂ) :
    normalizedWeightSum d x = (((∑ i, d i : ℝ) : ℂ)⁻¹) * weightSum d x := rfl

lemma normalizedWeightSum_one {I : Type*} [Fintype I]
    (d : I → ℝ) (hs : (∑ i, d i) ≠ 0) :
    normalizedWeightSum d (fun _ ↦ 1) = 1 := by
  rw [normalizedWeightSum_apply, weightSum_apply]
  have hcast : ∑ i, (d i : ℂ) = ((∑ i, d i : ℝ) : ℂ) := by simp
  simp only [mul_one]
  rw [hcast, inv_mul_cancel₀]
  exact_mod_cast hs

lemma diagonalForm_normalizedWeightSum_decomposition {I : Type*} [Fintype I]
    (d : I → ℝ) (hs : 0 < ∑ i, d i) (x : I → ℂ) :
    diagonalForm d x =
      Complex.normSq (normalizedWeightSum d x) * diagonalForm d (fun _ ↦ 1) +
        diagonalForm d (x - normalizedWeightSum d x • (fun _ ↦ 1)) := by
  rw [diagonalForm_positiveLine_decomposition d hs x]
  simp [diagonalForm]

section CyclotomicInertia

open Mathia.PC218

/-- The real cyclotomic coefficient on the complex-support subtype inherited from PC-218. -/
def realCoeffVector (n : ℕ) : CyclotomicSupport n → ℝ :=
  fun r ↦ (Polynomial.cyclotomic n ℝ).coeff r

lemma coeffVector_eq_ofReal (n : ℕ) (r : CyclotomicSupport n) :
    coeffVector n r = (realCoeffVector n r : ℂ) := by
  change (Polynomial.cyclotomic n ℂ).coeff (r : ℕ) =
    ((Polynomial.cyclotomic n ℝ).coeff (r : ℕ) : ℂ)
  rw [← Polynomial.map_cyclotomic n (algebraMap ℝ ℂ), Polynomial.coeff_map]
  rfl

lemma realCoeffVector_ne_zero (n : ℕ) (r : CyclotomicSupport n) :
    realCoeffVector n r ≠ 0 := by
  intro hr
  have hc := Polynomial.mem_support_iff.mp r.property
  apply hc
  change coeffVector n r = 0
  rw [coeffVector_eq_ofReal]
  simp [hr]

/-- Number of positive cyclotomic coefficients; zero positions do not affect this support count. -/
def positiveCoefficientCount (n : ℕ) : ℕ :=
  {r : CyclotomicSupport n | 0 < realCoeffVector n r}.ncard

/-- Number of negative cyclotomic coefficients; zero positions do not affect this support count. -/
def negativeCoefficientCount (n : ℕ) : ℕ :=
  {r : CyclotomicSupport n | realCoeffVector n r < 0}.ncard

lemma eval_one_cyclotomic_real_pos {n : ℕ} (hn : 1 < n) :
    0 < (Polynomial.cyclotomic n ℝ).eval 1 := by
  by_cases htwo : n = 2
  · subst n
    norm_num [Polynomial.cyclotomic_two]
  · exact Polynomial.cyclotomic_pos (by omega) 1

lemma realCoeffVector_sum_eq_eval_one (n : ℕ) :
    ∑ r : CyclotomicSupport n, realCoeffVector n r =
      (Polynomial.cyclotomic n ℝ).eval 1 := by
  have hC : ∑ r : CyclotomicSupport n, coeffVector n r =
      (Polynomial.cyclotomic n ℂ).eval 1 := by
    rw [← supportPolynomial_coeffVector n, supportPolynomial_eval]
    simp
  have hre := congrArg Complex.re hC
  have hev : (Polynomial.cyclotomic n ℂ).eval (1 : ℂ) =
      Complex.ofReal ((Polynomial.cyclotomic n ℝ).eval (1 : ℝ)) :=
    Polynomial.cyclotomic.eval_apply_ofReal 1 n
  rw [hev] at hre
  simpa [coeffVector_eq_ofReal] using hre

lemma realCoeffVector_sum_pos {n : ℕ} (hn : 1 < n) :
    0 < ∑ r : CyclotomicSupport n, realCoeffVector n r := by
  rw [realCoeffVector_sum_eq_eval_one]
  exact eval_one_cyclotomic_real_pos hn

/-- The evaluation frame fills exactly the hyperplane cut out by the cyclotomic coefficients. -/
theorem evaluationMatrix_range_eq_ker_normalizedWeightSum {n : ℕ} (hn : 1 < n) :
    LinearMap.range (evaluationMatrix n).mulVecLin =
      LinearMap.ker (normalizedWeightSum (realCoeffVector n)) := by
  classical
  apply Submodule.eq_of_le_of_finrank_eq
  · rintro y ⟨x, rfl⟩
    rw [LinearMap.mem_ker]
    have ha_mem : coeffVector n ∈
        LinearMap.ker (evaluationMatrix n).conjTranspose.mulVecLin := by
      rw [evaluationMatrix_leftKernel hn]
      exact Submodule.mem_span_singleton_self (coeffVector n)
    have ha_zero : (evaluationMatrix n).conjTranspose *ᵥ coeffVector n = 0 := ha_mem
    have hrow : star (coeffVector n) ᵥ* evaluationMatrix n = 0 := by
      rw [Matrix.mulVec_conjTranspose] at ha_zero
      apply_fun star at ha_zero
      simpa using ha_zero
    rw [normalizedWeightSum_apply]
    simp only [Matrix.mulVecLin_apply]
    have hweighted : weightSum (realCoeffVector n)
        ((evaluationMatrix n).mulVec x) = 0 := by
      rw [weightSum_apply]
      calc
        ∑ r, (realCoeffVector n r : ℂ) * (evaluationMatrix n *ᵥ x) r =
            star (coeffVector n) ⬝ᵥ (evaluationMatrix n *ᵥ x) := by
              apply Finset.sum_congr rfl
              intro r _
              simp [coeffVector_eq_ofReal]
        _ = (star (coeffVector n) ᵥ* evaluationMatrix n) ⬝ᵥ x := by
              rw [Matrix.dotProduct_mulVec]
        _ = 0 := by rw [hrow, zero_dotProduct]
    rw [hweighted, mul_zero]
  · rw [← Matrix.rank, evaluationMatrix_rank hn]
    let c := normalizedWeightSum (realCoeffVector n)
    have hcone : c (fun _ ↦ 1) = 1 :=
      normalizedWeightSum_one _ (ne_of_gt (realCoeffVector_sum_pos hn))
    have hc_surj : Function.Surjective c := by
      intro z
      refine ⟨z • (fun _ ↦ 1), ?_⟩
      rw [map_smul, hcone, smul_eq_mul, mul_one]
    have hrange : LinearMap.range c = ⊤ := LinearMap.range_eq_top.mpr hc_surj
    have hdim := LinearMap.finrank_range_add_finrank_ker c
    dsimp [c] at hdim
    rw [hrange] at hdim
    simp only [finrank_top, Module.finrank_self] at hdim
    rw [Module.finrank_fintype_fun_eq_card] at hdim
    have hsupport : 0 < Fintype.card (CyclotomicSupport n) := Fintype.card_pos_iff.mpr
      ⟨⟨Nat.totient n, totient_mem_cyclotomicSupport n⟩⟩
    omega

/-- The signed Gram quadratic form is the cyclotomic coefficient diagonal form pulled back along
the primitive-root evaluation frame. -/
theorem matrixForm_signedGram (n : ℕ) (x : PrimitiveFrequency n → ℂ) :
    matrixForm (signedGram n) x =
      diagonalForm (realCoeffVector n) (evaluationMatrix n *ᵥ x) := by
  classical
  let A := evaluationMatrix n
  let y := A *ᵥ x
  let w := Matrix.diagonal (coeffVector n) *ᵥ y
  have hmul : signedGram n *ᵥ x = A.conjTranspose *ᵥ w := by
    simp only [signedGram, A, y, w, Matrix.mulVec_mulVec]
    rw [Matrix.mul_assoc]
  rw [matrixForm, hmul, dotProduct_conjTranspose_mulVec]
  change (star y ⬝ᵥ w).re = diagonalForm (realCoeffVector n) y
  rw [diagonalForm]
  simp only [dotProduct, Complex.re_sum]
  apply Finset.sum_congr rfl
  intro i _
  rw [show w i = coeffVector n i * y i by
    exact Matrix.mulVec_diagonal (coeffVector n) y i]
  rw [coeffVector_eq_ofReal]
  simp [Complex.normSq]
  ring

/-- Exact positive and negative indices of the unnormalized signed Gram matrix. -/
theorem signedGram_indices {n : ℕ} (hn : 1 < n) :
    positiveIndex (matrixForm (signedGram n)) = positiveCoefficientCount n - 1 ∧
      negativeIndex (matrixForm (signedGram n)) = negativeCoefficientCount n := by
  classical
  let d := realCoeffVector n
  let A := (evaluationMatrix n).mulVecLin
  let c := normalizedWeightSum d
  let e : CyclotomicSupport n → ℂ := fun _ ↦ 1
  have hsum : 0 < ∑ i, d i := realCoeffVector_sum_pos hn
  have hce : c e = 1 := normalizedWeightSum_one d (ne_of_gt hsum)
  have he : 0 < diagonalForm d e := by
    simpa [diagonalForm, d, e] using hsum
  have hsplit := indices_on_ker_of_positive_line (diagonalForm d) c e
    (by simp [diagonalForm]) hce he
    (diagonalForm_normalizedWeightSum_decomposition d hsum)
  have hrange : LinearMap.range A = LinearMap.ker c := by
    simpa [A, c, d] using evaluationMatrix_range_eq_ker_normalizedWeightSum hn
  have hdiag := diagonalForm_indices d
  constructor
  · calc
      positiveIndex (matrixForm (signedGram n)) =
          positiveIndex (fun x ↦ diagonalForm d (A x)) := by
            congr 1
            funext x
            exact matrixForm_signedGram n x
      _ = positiveIndex (fun y : LinearMap.range A ↦ diagonalForm d y) :=
        positiveIndex_comp_range A (diagonalForm d) (by simp [diagonalForm])
      _ = positiveIndex (fun y : LinearMap.ker c ↦ diagonalForm d y) :=
        positiveIndex_submodule_eq (diagonalForm d) hrange
      _ = positiveIndex (diagonalForm d) - 1 := hsplit.1
      _ = positiveCoefficientCount n - 1 := by
        rw [hdiag.1]
        rfl
  · calc
      negativeIndex (matrixForm (signedGram n)) =
          negativeIndex (fun x ↦ diagonalForm d (A x)) := by
            congr 1
            funext x
            exact matrixForm_signedGram n x
      _ = negativeIndex (fun y : LinearMap.range A ↦ diagonalForm d y) :=
        negativeIndex_comp_range A (diagonalForm d) (by simp [diagonalForm])
      _ = negativeIndex (fun y : LinearMap.ker c ↦ diagonalForm d y) :=
        negativeIndex_submodule_eq (diagonalForm d) hrange
      _ = negativeIndex (diagonalForm d) := hsplit.2
      _ = negativeCoefficientCount n := by
        rw [hdiag.2]
        rfl

theorem signedGram_isHermitian (n : ℕ) : (signedGram n).IsHermitian := by
  apply Matrix.isHermitian_conjTranspose_mul_mul (evaluationMatrix n)
  apply Matrix.isHermitian_diagonal_of_self_adjoint
  rw [isSelfAdjoint_iff]
  funext r
  simp [coeffVector_eq_ofReal]

/-- The real form of PC-218's positive Fourier normalization. -/
def transverseScaleReal (n : ℕ) : ℝ :=
  (Real.sqrt ((n : ℝ) * coefficientEnergy n))⁻¹

lemma transverseScaleReal_pos {n : ℕ} (hn : 1 < n) : 0 < transverseScaleReal n := by
  unfold transverseScaleReal
  exact inv_pos.mpr (Real.sqrt_pos.2 (mul_pos (by positivity) (coefficientEnergy_pos n)))

lemma transverseScale_eq_ofReal (n : ℕ) :
    transverseScale n = (transverseScaleReal n : ℂ) := by
  simp [transverseScale, transverseScaleReal]

theorem transverseMatrix_isHermitian (n : ℕ) : (transverseMatrix n).IsHermitian := by
  rw [transverseMatrix, transverseScale_eq_ofReal]
  apply (signedGram_isHermitian n).smul
  rw [isSelfAdjoint_iff]
  exact Complex.conj_ofReal _

/-- Positive normalization preserves both signed indices. -/
theorem transverseMatrix_indices {n : ℕ} (hn : 1 < n) :
    positiveIndex (matrixForm (transverseMatrix n)) = positiveCoefficientCount n - 1 ∧
      negativeIndex (matrixForm (transverseMatrix n)) = negativeCoefficientCount n := by
  have hscale := transverseScaleReal_pos hn
  have hform : matrixForm (transverseMatrix n) =
      fun x ↦ transverseScaleReal n * matrixForm (signedGram n) x := by
    funext x
    rw [transverseMatrix, transverseScale_eq_ofReal,
      matrixForm_ofReal_smul]
  rw [hform, positiveIndex_pos_mul _ hscale, negativeIndex_pos_mul _ hscale]
  exact signedGram_indices hn

end CyclotomicInertia

/-- The intrinsic inertia certificate used by PC-219. -/
def HasInertia {I : Type*} [Fintype I]
    (H : Matrix I I ℂ) (p m z : ℕ) : Prop :=
  H.IsHermitian ∧
    positiveIndex (matrixForm H) = p ∧
    negativeIndex (matrixForm H) = m ∧
    Module.finrank ℂ (LinearMap.ker H.mulVecLin) = z

open Mathia.PC218

/-- PC-219: the canonical transverse mask has inertia given exactly by the signs and zeros of the
cyclotomic coefficients. -/
theorem transverseMatrix_inertia {n : ℕ} (hn : 1 < n) :
    HasInertia (transverseMatrix n)
      (positiveCoefficientCount n - 1)
      (negativeCoefficientCount n)
      (zeroCoefficientPositions n).card := by
  unfold HasInertia
  exact ⟨transverseMatrix_isHermitian n,
    (transverseMatrix_indices hn).1, (transverseMatrix_indices hn).2,
    transverseMatrix_nullity_eq_zeroCoefficientCount hn⟩

/-- Signature of a finite Hermitian matrix, computed from the intrinsic signed indices. -/
def signature {I : Type*} [Fintype I] (H : Matrix I I ℂ) : ℤ :=
  (positiveIndex (matrixForm H) : ℤ) - (negativeIndex (matrixForm H) : ℤ)

/-- The equivalent PC-219 signature formula. -/
theorem transverseMatrix_signature {n : ℕ} (hn : 1 < n) :
    signature (transverseMatrix n) =
      (positiveCoefficientCount n : ℤ) - (negativeCoefficientCount n : ℤ) - 1 := by
  rw [signature, (transverseMatrix_indices hn).1, (transverseMatrix_indices hn).2]
  have hpos : 0 < positiveCoefficientCount n := by
    have hsum := realCoeffVector_sum_pos hn
    have hexists : ∃ i : CyclotomicSupport n, 0 < realCoeffVector n i := by
      by_contra hnone
      push Not at hnone
      have hnonpos : ∑ i : CyclotomicSupport n, realCoeffVector n i ≤ 0 :=
        Finset.sum_nonpos fun i _ ↦ hnone i
      linarith
    rw [positiveCoefficientCount, Set.ncard_pos]
    exact hexists
  omega

#print axioms indices_on_ker_of_positive_line
#print axioms evaluationMatrix_range_eq_ker_normalizedWeightSum
#print axioms signedGram_indices
#print axioms transverseMatrix_inertia
#print axioms transverseMatrix_signature

end Mathia.PC219
