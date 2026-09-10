import Mathlib.Analysis.InnerProductSpace.Projection.FiniteDimensional
import Mathlib.Analysis.InnerProductSpace.Projection.Submodule
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.LinearAlgebra.Basis.Prod
import Mathlib.LinearAlgebra.Dimension.OrzechProperty
import Mathlib.LinearAlgebra.Isomorphisms
import Mathlib.Tactic.Abel

/-!
# NB-033 moving-tail quotient normal form

Associated finding:
`research/nyman_beurling/findings/NB-033-polylogarithmic-tail-skeleton-preserves-relative-distance-and-mobius-core.md`

Formalized theorem boundary: consecutive tail differences span exactly the kernel of the
head-plus-tail-sum coefficient map. For an independent finite family this gives the exact
tail rank and quotient basis. In a real or complex inner-product space the quotient is
realized by `Q = I - P_W` on the generator span, including its kernel, image, dimensions,
unchanged head coefficients, summed tail coefficient, and `Q(P_V e) = P_K e`.

Indices are `Fin h ⊕ Fin (t+1)`: in NB-033, `h = M-2`, `t = N-M`, head `i` denotes
`g_(i+2)` and tail `j` denotes `g_(M+j)`. Empty heads and singleton tails are included.
Linear independence is assumed, not proved for the fractional-part generators. Shell and
Möbius inversion, Burnol's bound, polylogarithmic distance estimates, conditioning, and RH
consequences remain outside Lean. The preserved coefficients are in the induced basis.
-/

noncomputable section

namespace Mathia.NB033

open Module Submodule
open scoped BigOperators

abbrev Index (h t : ℕ) := Fin h ⊕ Fin (t + 1)
abbrev Coeff (𝕜 : Type*) (h t : ℕ) := Index h t → 𝕜
abbrev Reduced (𝕜 : Type*) (h : ℕ) := (Fin h → 𝕜) × 𝕜

section Coefficients

variable (𝕜 : Type*) [Field 𝕜] (h t : ℕ)

/-- Keep the head coordinates and sum the nonempty tail. -/
def collapse : Coeff 𝕜 h t →ₗ[𝕜] Reduced 𝕜 h where
  toFun a := (fun i => a (.inl i), ∑ j, a (.inr j))
  map_add' a b := by ext <;> simp [Finset.sum_add_distrib]
  map_smul' c a := by ext <;> simp [Finset.mul_sum]

/-- A canonical section places the surviving tail coefficient at its first vertex. -/
def sectionMap : Reduced 𝕜 h →ₗ[𝕜] Coeff 𝕜 h t where
  toFun b := Sum.elim b.1 (Pi.single 0 b.2)
  map_add' a b := by ext i; cases i <;> simp [Pi.single_add]
  map_smul' c a := by ext i; cases i <;> simp [Pi.single_apply, mul_ite]

@[simp] theorem collapse_section (b : Reduced 𝕜 h) :
    collapse 𝕜 h t (sectionMap 𝕜 h t b) = b := by
  ext <;> simp [collapse, sectionMap]

theorem collapse_surjective : Function.Surjective (collapse 𝕜 h t) :=
  fun b => ⟨sectionMap 𝕜 h t b, collapse_section 𝕜 h t b⟩

/-- Oriented consecutive coefficient differences along the tail path. -/
def edge (i : Fin t) : Coeff 𝕜 h t :=
  Pi.single (.inr i.castSucc) 1 - Pi.single (.inr i.succ) 1

def tailSpace : Submodule 𝕜 (Coeff 𝕜 h t) := span 𝕜 (Set.range (edge 𝕜 h t))

@[simp] theorem collapse_single_tail (j : Fin (t + 1)) :
    collapse 𝕜 h t (Pi.single (.inr j) 1) = (0, 1) := by
  ext <;> simp [collapse, Pi.single_apply]

@[simp] theorem collapse_edge (i : Fin t) : collapse 𝕜 h t (edge 𝕜 h t i) = 0 := by
  simp [edge]

theorem anchor_difference_mem (j : Fin (t + 1)) :
    Pi.single (.inr j) 1 - Pi.single (.inr 0) 1 ∈ tailSpace 𝕜 h t := by
  induction j using Fin.induction with
  | zero => simp
  | succ i ih =>
    have he : edge 𝕜 h t i ∈ tailSpace 𝕜 h t := subset_span ⟨i, rfl⟩
    convert (tailSpace 𝕜 h t).sub_mem ih he using 1
    simp only [edge]
    abel

/-- The path-difference span is precisely the zero-sum tail subspace. -/
theorem tailSpace_eq_ker : tailSpace 𝕜 h t = (collapse 𝕜 h t).ker := by
  apply le_antisymm
  · apply span_le.mpr
    rintro _ ⟨i, rfl⟩
    exact collapse_edge 𝕜 h t i
  · intro a ha
    have hh : ∀ i, a (.inl i) = 0 := by
      intro i
      exact congrFun (congrArg Prod.fst ha) i
    have ht : ∑ j, a (.inr j) = 0 := congrArg Prod.snd ha
    have heq : a = ∑ j, a (.inr j) •
        (Pi.single (.inr j) 1 - Pi.single (.inr 0) 1 : Coeff 𝕜 h t) := by
      simp only [smul_sub, Finset.sum_sub_distrib, ← Finset.sum_smul, ht, zero_smul,
        sub_zero]
      ext i
      cases i with
      | inl i => simp [hh]
      | inr j => simp [Pi.single_apply]
    rw [heq]
    exact sum_mem fun j _ => smul_mem _ _ (anchor_difference_mem 𝕜 h t j)

theorem finrank_tailSpace : finrank 𝕜 (tailSpace 𝕜 h t) = t := by
  have hr := (collapse 𝕜 h t).finrank_range_add_finrank_ker
  rw [LinearMap.range_eq_top.mpr (collapse_surjective 𝕜 h t)] at hr
  rw [← tailSpace_eq_ker] at hr
  simp [Reduced, Coeff, Index, finrank_prod] at hr
  have hr' : h + 1 + finrank 𝕜 (tailSpace 𝕜 h t) = h + (t + 1) := hr
  omega

theorem edge_independent : LinearIndependent 𝕜 (edge 𝕜 h t) := by
  rw [linearIndependent_iff_card_eq_finrank_span]
  rw [Fintype.card_fin, Set.finrank]
  exact (finrank_tailSpace 𝕜 h t).symm

/-- The quotient is canonically the head space plus one tail-sum coordinate. -/
def coefficientQuotientEquiv :
    (Coeff 𝕜 h t ⧸ tailSpace 𝕜 h t) ≃ₗ[𝕜] Reduced 𝕜 h :=
  (Submodule.quotEquivOfEq _ _ (tailSpace_eq_ker 𝕜 h t)).trans
    ((collapse 𝕜 h t).quotKerEquivOfSurjective (collapse_surjective 𝕜 h t))

@[simp] theorem coefficientQuotientEquiv_mk (a : Coeff 𝕜 h t) :
    coefficientQuotientEquiv 𝕜 h t (Submodule.Quotient.mk a) = collapse 𝕜 h t a := by
  simp [coefficientQuotientEquiv]

def reducedBasis : Basis (Fin h ⊕ Unit) 𝕜 (Reduced 𝕜 h) :=
  (Pi.basisFun 𝕜 (Fin h)).prod (Basis.singleton Unit 𝕜)

def coefficientQuotientBasis : Basis (Fin h ⊕ Unit) 𝕜 (Coeff 𝕜 h t ⧸ tailSpace 𝕜 h t) :=
  (reducedBasis 𝕜 h).map (coefficientQuotientEquiv 𝕜 h t).symm

theorem finrank_coefficientQuotient : finrank 𝕜 (Coeff 𝕜 h t ⧸ tailSpace 𝕜 h t) = h + 1 := by
  simpa [Reduced] using (coefficientQuotientEquiv 𝕜 h t).finrank_eq

end Coefficients

section Synthesis

variable (𝕜 : Type*) [Field 𝕜] {h t : ℕ}
variable {E : Type*} [AddCommGroup E] [Module 𝕜 E]
variable (g : Index h t → E)

def synthesis : Coeff 𝕜 h t →ₗ[𝕜] E := Fintype.linearCombination 𝕜 g
def generatorSpan : Submodule 𝕜 E := span 𝕜 (Set.range g)
def generatorEdge (i : Fin t) : E := g (.inr i.castSucc) - g (.inr i.succ)
def generatorTail : Submodule 𝕜 E := span 𝕜 (Set.range (generatorEdge g))

instance generatorSpan_finite : FiniteDimensional 𝕜 (generatorSpan 𝕜 g) :=
  FiniteDimensional.span_of_finite 𝕜 (Set.finite_range g)

instance generatorTail_finite : FiniteDimensional 𝕜 (generatorTail 𝕜 g) :=
  FiniteDimensional.span_of_finite 𝕜 (Set.finite_range (generatorEdge g))

@[simp] theorem synthesis_single (i : Index h t) :
    synthesis 𝕜 g (Pi.single i 1) = g i := by simp [synthesis]

@[simp] theorem synthesis_edge (i : Fin t) :
    synthesis 𝕜 g (edge 𝕜 h t i) = generatorEdge g i := by simp [edge, generatorEdge]

theorem synthesis_range : (synthesis 𝕜 g).range = generatorSpan 𝕜 g :=
  Fintype.range_linearCombination 𝕜 g

theorem synthesis_mem (a : Coeff 𝕜 h t) : synthesis 𝕜 g a ∈ generatorSpan 𝕜 g := by
  rw [← synthesis_range]
  exact ⟨a, rfl⟩

theorem generator_mem (i : Index h t) : g i ∈ generatorSpan 𝕜 g := subset_span ⟨i, rfl⟩

theorem tail_map_eq : (tailSpace 𝕜 h t).map (synthesis 𝕜 g) = generatorTail 𝕜 g := by
  simp only [tailSpace, Submodule.map_span, ← Set.range_comp, Function.comp_def,
    synthesis_edge, generatorTail]

theorem generatorTail_le : generatorTail 𝕜 g ≤ generatorSpan 𝕜 g := by
  apply span_le.mpr
  rintro _ ⟨i, rfl⟩
  exact sub_mem (generator_mem 𝕜 g _) (generator_mem 𝕜 g _)

variable (hg : LinearIndependent 𝕜 g)
include hg

theorem generatorEdge_independent : LinearIndependent 𝕜 (generatorEdge g) := by
  have hi := (edge_independent 𝕜 h t).map' (synthesis 𝕜 g)
    (LinearMap.ker_eq_bot.mpr hg.fintypeLinearCombination_injective)
  simpa only [Function.comp_def, synthesis_edge] using hi

theorem finrank_generatorSpan : finrank 𝕜 (generatorSpan 𝕜 g) = h + t + 1 := by
  unfold generatorSpan
  rw [finrank_span_eq_card hg]
  simp [Index, Nat.add_assoc]

theorem finrank_generatorTail : finrank 𝕜 (generatorTail 𝕜 g) = t := by
  unfold generatorTail
  rw [finrank_span_eq_card (generatorEdge_independent 𝕜 g hg)]
  exact Fintype.card_fin t

theorem synthesis_mem_tail_iff (a : Coeff 𝕜 h t) :
    synthesis 𝕜 g a ∈ generatorTail 𝕜 g ↔ collapse 𝕜 h t a = 0 := by
  rw [← tail_map_eq, Submodule.mem_map]
  constructor
  · rintro ⟨b, hb, heq⟩
    have hab : b = a := hg.fintypeLinearCombination_injective heq
    subst b
    rwa [tailSpace_eq_ker] at hb
  · intro ha
    exact ⟨a, by rwa [tailSpace_eq_ker], rfl⟩

end Synthesis

section OrthogonalRealization

variable (𝕜 : Type*) [RCLike 𝕜] {h t : ℕ}
variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
variable (g : Index h t → E)

/-- The surviving orthogonal sector inside the original finite span. -/
def skeleton : Submodule 𝕜 E := generatorSpan 𝕜 g ⊓ (generatorTail 𝕜 g)ᗮ

instance skeleton_finite : FiniteDimensional 𝕜 (skeleton 𝕜 g) :=
  Submodule.finiteDimensional_of_le (show skeleton 𝕜 g ≤ generatorSpan 𝕜 g from inf_le_left)

/-- The ambient map `I - P_W`; all range assertions below explicitly restrict it to `V`. -/
def quotientProjection : E →ₗ[𝕜] E :=
  LinearMap.id - (generatorTail 𝕜 g).starProjection.toLinearMap

@[simp] theorem quotientProjection_apply (x : E) :
    quotientProjection 𝕜 g x = x - (generatorTail 𝕜 g).starProjection x := rfl

theorem quotientProjection_eq_zero_iff (x : E) :
    quotientProjection 𝕜 g x = 0 ↔ x ∈ generatorTail 𝕜 g := by
  rw [quotientProjection_apply, sub_eq_zero, eq_comm, Submodule.starProjection_eq_self_iff]

theorem quotientProjection_mem {x : E} (hx : x ∈ generatorSpan 𝕜 g) :
    quotientProjection 𝕜 g x ∈ skeleton 𝕜 g :=
  ⟨sub_mem hx (generatorTail_le 𝕜 g (Submodule.starProjection_apply_mem _ x)),
    Submodule.sub_starProjection_mem_orthogonal x⟩

theorem quotientProjection_fixed {x : E} (hx : x ∈ skeleton 𝕜 g) :
    quotientProjection 𝕜 g x = x := by
  have hp : (generatorTail 𝕜 g).starProjection x = 0 := by
    rw [Submodule.starProjection_apply]
    exact congrArg Subtype.val (Submodule.orthogonalProjectionOnto_eq_zero_iff.mpr hx.2)
  simp [hp]

/-- Restriction of `Q` to the original generator span, with ambient codomain. -/
def restrictedProjection : generatorSpan 𝕜 g →ₗ[𝕜] E :=
  (quotientProjection 𝕜 g).comp (generatorSpan 𝕜 g).subtype

theorem restrictedProjection_ker :
    (restrictedProjection 𝕜 g).ker =
      (generatorTail 𝕜 g).comap (generatorSpan 𝕜 g).subtype := by
  ext x
  exact quotientProjection_eq_zero_iff 𝕜 g x

theorem restrictedProjection_range : (restrictedProjection 𝕜 g).range = skeleton 𝕜 g := by
  ext x
  constructor
  · rintro ⟨y, rfl⟩
    exact quotientProjection_mem 𝕜 g y.property
  · intro hx
    exact ⟨⟨x, hx.1⟩, quotientProjection_fixed 𝕜 g hx⟩

/-- Every tail generator has the image of the first tail generator. -/
theorem tail_image_eq (j : Fin (t + 1)) :
    quotientProjection 𝕜 g (g (.inr j)) = quotientProjection 𝕜 g (g (.inr 0)) := by
  apply sub_eq_zero.mp
  rw [← map_sub, quotientProjection_eq_zero_iff]
  rw [← tail_map_eq]
  refine ⟨_, anchor_difference_mem 𝕜 h t j, ?_⟩
  simp

/-- Coefficient pushforward in the generators' induced quotient coordinates. -/
theorem coefficient_pushforward (a : Coeff 𝕜 h t) :
    quotientProjection 𝕜 g (∑ i, a i • g i) =
      (∑ i : Fin h, a (.inl i) • quotientProjection 𝕜 g (g (.inl i))) +
      (∑ j : Fin (t + 1), a (.inr j)) • quotientProjection 𝕜 g (g (.inr 0)) := by
  simp only [map_add, map_sum, map_smul, Fintype.sum_sum_type, tail_image_eq,
    Finset.sum_smul]

theorem section_synthesis (b : Reduced 𝕜 h) :
    synthesis 𝕜 g (sectionMap 𝕜 h t b) =
      (∑ i : Fin h, b.1 i • g (.inl i)) + b.2 • g (.inr 0) := by
  simp [synthesis, Fintype.linearCombination_apply, Fintype.sum_sum_type, sectionMap,
    Pi.single_apply, ite_smul]

/-- A map from the retained coordinates onto the geometric quotient. -/
def reducedToSkeleton : Reduced 𝕜 h →ₗ[𝕜] skeleton 𝕜 g :=
  ((quotientProjection 𝕜 g).comp ((synthesis 𝕜 g).comp (sectionMap 𝕜 h t))).codRestrict
    (skeleton 𝕜 g) (fun _ => quotientProjection_mem 𝕜 g (synthesis_mem 𝕜 g _))

@[simp] theorem reducedToSkeleton_apply (b : Reduced 𝕜 h) :
    (reducedToSkeleton 𝕜 g b : E) = quotientProjection 𝕜 g (synthesis 𝕜 g
      (sectionMap 𝕜 h t b)) := rfl

theorem reducedToSkeleton_collapse (a : Coeff 𝕜 h t) :
    (reducedToSkeleton 𝕜 g (collapse 𝕜 h t a) : E) =
      quotientProjection 𝕜 g (synthesis 𝕜 g a) := by
  rw [reducedToSkeleton_apply, section_synthesis]
  simp only [map_add, map_sum, map_smul]
  exact (coefficient_pushforward 𝕜 g a).symm

theorem reducedToSkeleton_surjective : Function.Surjective (reducedToSkeleton 𝕜 g) := by
  intro x
  obtain ⟨a, ha⟩ := show (x : E) ∈ (synthesis 𝕜 g).range by
    rw [synthesis_range]
    exact x.property.1
  refine ⟨collapse 𝕜 h t a, Subtype.ext ?_⟩
  rw [reducedToSkeleton_collapse, ha]
  exact quotientProjection_fixed 𝕜 g x.property

theorem reducedToSkeleton_injective (hg : LinearIndependent 𝕜 g) :
    Function.Injective (reducedToSkeleton 𝕜 g) := by
  apply (injective_iff_map_eq_zero _).mpr
  intro b hb
  have hz : quotientProjection 𝕜 g (synthesis 𝕜 g (sectionMap 𝕜 h t b)) = 0 :=
    congrArg Subtype.val hb
  rw [quotientProjection_eq_zero_iff, synthesis_mem_tail_iff 𝕜 g hg,
    collapse_section] at hz
  exact hz

/-- The canonical retained-coordinate isomorphism onto the orthogonal skeleton. -/
def skeletonEquiv (hg : LinearIndependent 𝕜 g) : Reduced 𝕜 h ≃ₗ[𝕜] skeleton 𝕜 g :=
  LinearEquiv.ofBijective (reducedToSkeleton 𝕜 g)
    ⟨reducedToSkeleton_injective 𝕜 g hg, reducedToSkeleton_surjective 𝕜 g⟩

@[simp] theorem skeletonEquiv_apply (hg : LinearIndependent 𝕜 g) (b : Reduced 𝕜 h) :
    skeletonEquiv 𝕜 g hg b = reducedToSkeleton 𝕜 g b := rfl

def quotientBasis (hg : LinearIndependent 𝕜 g) : Basis (Fin h ⊕ Unit) 𝕜 (skeleton 𝕜 g) :=
  (reducedBasis 𝕜 h).map (skeletonEquiv 𝕜 g hg)

theorem quotientBasis_head (hg : LinearIndependent 𝕜 g) (i : Fin h) :
    (quotientBasis 𝕜 g hg (.inl i) : E) = quotientProjection 𝕜 g (g (.inl i)) := by
  simp [quotientBasis, Basis.map_apply, reducedToSkeleton_apply, section_synthesis,
    reducedBasis, Pi.basisFun_apply, Pi.single_apply, ite_smul]

theorem quotientBasis_tail (hg : LinearIndependent 𝕜 g) :
    (quotientBasis 𝕜 g hg (.inr ()) : E) = quotientProjection 𝕜 g (g (.inr 0)) := by
  simp [quotientBasis, Basis.map_apply, reducedToSkeleton_apply, section_synthesis,
    reducedBasis]

/-- The coordinates of a projected linear combination are exactly its collapsed coefficients. -/
theorem skeleton_coordinates (hg : LinearIndependent 𝕜 g) (a : Coeff 𝕜 h t) :
    (skeletonEquiv 𝕜 g hg).symm
      ⟨quotientProjection 𝕜 g (synthesis 𝕜 g a),
        quotientProjection_mem 𝕜 g (synthesis_mem 𝕜 g a)⟩ = collapse 𝕜 h t a := by
  apply (skeletonEquiv 𝕜 g hg).injective
  apply Subtype.ext
  simpa using (reducedToSkeleton_collapse 𝕜 g a).symm

theorem quotientBasis_repr_head (hg : LinearIndependent 𝕜 g) (a : Coeff 𝕜 h t)
    (i : Fin h) :
    (quotientBasis 𝕜 g hg).repr
      ⟨quotientProjection 𝕜 g (synthesis 𝕜 g a),
        quotientProjection_mem 𝕜 g (synthesis_mem 𝕜 g a)⟩ (.inl i) = a (.inl i) := by
  change (reducedBasis 𝕜 h).repr ((skeletonEquiv 𝕜 g hg).symm _) (.inl i) = _
  rw [skeleton_coordinates]
  simp [reducedBasis, collapse]

theorem quotientBasis_repr_tail (hg : LinearIndependent 𝕜 g) (a : Coeff 𝕜 h t) :
    (quotientBasis 𝕜 g hg).repr
      ⟨quotientProjection 𝕜 g (synthesis 𝕜 g a),
        quotientProjection_mem 𝕜 g (synthesis_mem 𝕜 g a)⟩ (.inr ()) =
        ∑ j : Fin (t + 1), a (.inr j) := by
  change (reducedBasis 𝕜 h).repr ((skeletonEquiv 𝕜 g hg).symm _) (.inr ()) = _
  rw [skeleton_coordinates]
  simp [reducedBasis, collapse]

theorem finrank_skeleton (hg : LinearIndependent 𝕜 g) :
    finrank 𝕜 (skeleton 𝕜 g) = h + 1 := by
  have he := (skeletonEquiv 𝕜 g hg).finrank_eq
  simpa [Reduced] using he.symm

/-- The three exact dimensions, with no completeness assumption on the ambient space. -/
theorem exact_dimensions (hg : LinearIndependent 𝕜 g) :
    finrank 𝕜 (generatorSpan 𝕜 g) = h + t + 1 ∧
    finrank 𝕜 (generatorTail 𝕜 g) = t ∧ finrank 𝕜 (skeleton 𝕜 g) = h + 1 :=
  ⟨finrank_generatorSpan 𝕜 g hg, finrank_generatorTail 𝕜 g hg, finrank_skeleton 𝕜 g hg⟩

/-- On `V`, `Q` is orthogonal projection onto `K`. -/
theorem quotientProjection_eq_skeletonProjection {x : E} (hx : x ∈ generatorSpan 𝕜 g) :
    quotientProjection 𝕜 g x = (skeleton 𝕜 g).starProjection x := by
  apply Eq.symm
  apply Submodule.eq_starProjection_of_mem_orthogonal (quotientProjection_mem 𝕜 g hx)
  have hW : x - quotientProjection 𝕜 g x ∈ generatorTail 𝕜 g := by
    simp
  exact (Submodule.orthogonal_le (show skeleton 𝕜 g ≤ (generatorTail 𝕜 g)ᗮ from
    inf_le_right)) ((generatorTail 𝕜 g).le_orthogonal_orthogonal hW)

/-- NB-033 (17), the finite geometric bridge needed in its best-approximant formula (6). -/
theorem project_best_approximant (e : E) :
    quotientProjection 𝕜 g ((generatorSpan 𝕜 g).starProjection e) =
      (skeleton 𝕜 g).starProjection e := by
  rw [quotientProjection_eq_skeletonProjection 𝕜 g (Submodule.starProjection_apply_mem _ e)]
  have he := Submodule.starProjection_comp_starProjection_of_le
    (show skeleton 𝕜 g ≤ generatorSpan 𝕜 g from inf_le_left)
  exact congrArg (fun f : E →L[𝕜] E => f e) he

/-- NB-033 (6): the full best coefficients push forward without changing the head. -/
theorem best_approximant_coefficients (e : E) (a : Coeff 𝕜 h t)
    (ha : (generatorSpan 𝕜 g).starProjection e = ∑ i, a i • g i) :
    (skeleton 𝕜 g).starProjection e =
      (∑ i : Fin h, a (.inl i) • quotientProjection 𝕜 g (g (.inl i))) +
      (∑ j : Fin (t + 1), a (.inr j)) • quotientProjection 𝕜 g (g (.inr 0)) := by
  rw [← project_best_approximant, ha]
  exact coefficient_pushforward 𝕜 g a

end OrthogonalRealization

end Mathia.NB033

#print axioms Mathia.NB033.tailSpace_eq_ker
#print axioms Mathia.NB033.edge_independent
#print axioms Mathia.NB033.coefficientQuotientEquiv
#print axioms Mathia.NB033.coefficientQuotientEquiv_mk
#print axioms Mathia.NB033.generatorEdge_independent
#print axioms Mathia.NB033.exact_dimensions
#print axioms Mathia.NB033.restrictedProjection_ker
#print axioms Mathia.NB033.restrictedProjection_range
#print axioms Mathia.NB033.tail_image_eq
#print axioms Mathia.NB033.quotientBasis
#print axioms Mathia.NB033.quotientBasis_head
#print axioms Mathia.NB033.quotientBasis_tail
#print axioms Mathia.NB033.quotientBasis_repr_head
#print axioms Mathia.NB033.quotientBasis_repr_tail
#print axioms Mathia.NB033.coefficient_pushforward
#print axioms Mathia.NB033.project_best_approximant
#print axioms Mathia.NB033.best_approximant_coefficients
