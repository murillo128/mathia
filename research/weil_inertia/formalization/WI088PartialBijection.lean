import Mathlib

/-!
# WI-088 finite partial-bijection dimension bound

Associated finding:
`research/weil_inertia/findings/WI-088-residual-prime-ramanujan-rank-defect-is-sharply-capped-at-one-third.md`

Formalized theorem boundary:
for a finite partial bijection from `D` onto the complement of a forced-zero set `Z`, with no
directed cycles of length one or two, the complex vector space of zero-mean functions which are
constant on directed edges and vanish on `Z` has dimension at most
`((|V| - |Z|) / 3) - 1` (with natural-number truncation).

Not formalized:
the prime/Fourier reduction producing this partial bijection, any residual Ramanujan cross-Gram
rank theorem, the WI-087 equality family or asymptotic sharpness, Yang covariance conclusions,
many-modulus inertia, or any zeta zero-proportion claim.
-/

noncomputable section

open scoped BigOperators

namespace Mathia.WI088

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- The undirected graph underlying the directed partial map `x ↦ g x` on `D`. -/
def partialGraph (D : Finset V) (g : V → V) : SimpleGraph V :=
  SimpleGraph.fromRel fun x y ↦ x ∈ D ∧ g x = y

@[simp]
lemma partialGraph_adj {D : Finset V} {g : V → V} {x y : V} :
    (partialGraph D g).Adj x y ↔
      x ≠ y ∧ ((x ∈ D ∧ g x = y) ∨ (y ∈ D ∧ g y = x)) :=
  Iff.rfl

/-- Functions obeying the selected edge equations, forced zeros, and zero-mean equation. -/
def solutionSpace (D Z : Finset V) (g : V → V) : Submodule ℂ (V → ℂ) where
  carrier := {f | (∀ x ∈ D, f (g x) = f x) ∧ (∀ z ∈ Z, f z = 0) ∧ ∑ x, f x = 0}
  zero_mem' := by simp
  add_mem' := by
    rintro f h ⟨hf_edge, hf_zero, hf_sum⟩ ⟨hh_edge, hh_zero, hh_sum⟩
    refine ⟨?_, ?_, ?_⟩
    · intro x hx
      simp only [Pi.add_apply]
      rw [hf_edge x hx, hh_edge x hx]
    · intro z hz
      simp [hf_zero z hz, hh_zero z hz]
    · simpa only [Pi.add_apply, Finset.sum_add_distrib, hf_sum, hh_sum, add_zero]
  smul_mem' := by
    rintro a f ⟨hf_edge, hf_zero, hf_sum⟩
    refine ⟨?_, ?_, ?_⟩
    · intro x hx
      simp only [Pi.smul_apply, smul_eq_mul]
      rw [hf_edge x hx]
    · intro z hz
      simp [hf_zero z hz]
    · change Finset.univ.sum (fun x : V ↦ a • f x) = 0
      rw [← Finset.smul_sum, hf_sum, smul_zero]

@[simp]
lemma mem_solutionSpace {D Z : Finset V} {g : V → V} {f : V → ℂ} :
    f ∈ solutionSpace D Z g ↔
      (∀ x ∈ D, f (g x) = f x) ∧ (∀ z ∈ Z, f z = 0) ∧ ∑ x, f x = 0 :=
  Iff.rfl

private lemma value_eq_of_adj {D Z : Finset V} {g : V → V}
    (f : solutionSpace D Z g) {x y : V} (hxy : (partialGraph D g).Adj x y) :
    f.1 x = f.1 y := by
  rcases hxy.2 with hxy | hyx
  · exact (f.2.1 x hxy.1).symm.trans (congr_arg f.1 hxy.2)
  · exact (congr_arg f.1 hyx.2.symm).trans (f.2.1 y hyx.1)

private lemma value_eq_of_reachable {D Z : Finset V} {g : V → V}
    (f : solutionSpace D Z g) {x y : V} (hxy : (partialGraph D g).Reachable x y) :
    f.1 x = f.1 y := by
  rw [SimpleGraph.reachable_eq_reflTransGen] at hxy
  induction hxy with
  | refl => rfl
  | tail _ h ih => exact ih.trans (value_eq_of_adj f h)

/-- Connected components which do not meet the forced-zero set. -/
def FreeComponent (D Z : Finset V) (g : V → V) :=
  {c : (partialGraph D g).ConnectedComponent // Disjoint c.supp (↑Z : Set V)}

noncomputable local instance freeComponentFintype (D Z : Finset V) (g : V → V) :
    Fintype (FreeComponent D Z g) := by
  classical
  letI : Fintype (partialGraph D g).ConnectedComponent := Fintype.ofFinite _
  unfold FreeComponent
  infer_instance

noncomputable local instance componentSuppFintype (D : Finset V) (g : V → V)
    (c : (partialGraph D g).ConnectedComponent) : Fintype c.supp :=
  Fintype.ofFinite _

private def componentValue {D Z : Finset V} {g : V → V}
    (f : solutionSpace D Z g) : (partialGraph D g).ConnectedComponent → ℂ :=
  Quot.lift f.1 fun _ _ h ↦ value_eq_of_reachable f h

@[simp]
private lemma componentValue_mk {D Z : Finset V} {g : V → V}
    (f : solutionSpace D Z g) (x : V) :
    componentValue f ((partialGraph D g).connectedComponentMk x) = f.1 x :=
  rfl

private lemma componentValue_add {D Z : Finset V} {g : V → V}
    (f h : solutionSpace D Z g) (c : (partialGraph D g).ConnectedComponent) :
    componentValue (f + h) c = componentValue f c + componentValue h c := by
  refine SimpleGraph.ConnectedComponent.ind (G := partialGraph D g) (fun _ ↦ ?_) c
  rfl

private lemma componentValue_smul {D Z : Finset V} {g : V → V}
    (a : ℂ) (f : solutionSpace D Z g) (c : (partialGraph D g).ConnectedComponent) :
    componentValue (a • f) c = a • componentValue f c := by
  refine SimpleGraph.ConnectedComponent.ind (G := partialGraph D g) (fun _ ↦ ?_) c
  rfl

private def freeEvaluation {D Z : Finset V} {g : V → V} :
    solutionSpace D Z g →ₗ[ℂ] (FreeComponent D Z g → ℂ) where
  toFun f c := componentValue f c.1
  map_add' f h := by
    funext c
    exact componentValue_add f h c.1
  map_smul' a f := by
    funext c
    exact componentValue_smul a f c.1

private lemma freeEvaluation_injective {D Z : Finset V} {g : V → V} :
    Function.Injective (freeEvaluation (D := D) (Z := Z) (g := g)) := by
  intro f h hfh
  apply Subtype.ext
  funext x
  by_cases hc : Disjoint
      ((partialGraph D g).connectedComponentMk x).supp (↑Z : Set V)
  · have hv := congr_fun hfh
        (⟨(partialGraph D g).connectedComponentMk x, hc⟩ : FreeComponent D Z g)
    exact hv
  · rw [Set.not_disjoint_iff] at hc
    obtain ⟨z, hzx, hzZ⟩ := hc
    have hr : (partialGraph D g).Reachable x z := by
      exact SimpleGraph.ConnectedComponent.exact hzx.symm
    have hfz : f.1 z = 0 := f.2.2.1 z hzZ
    have hhz : h.1 z = 0 := h.2.2.1 z hzZ
    exact (value_eq_of_reachable f hr).trans (hfz.trans (hhz.symm.trans
      (value_eq_of_reachable h hr).symm))

private lemma freeComponent_three_le_card {D Z : Finset V} {g : V → V}
    (hbij : Set.BijOn g (↑D : Set V) (↑Z : Set V)ᶜ)
    (hfix : ∀ x ∈ D, g x ≠ x)
    (htwo : ∀ x ∈ D, ∀ y ∈ D, g x = y → g y = x → False)
    (c : FreeComponent D Z g) : 3 ≤ Fintype.card c.1.supp := by
  classical
  obtain ⟨x, hxc⟩ := c.1.nonempty_supp
  have hxZ : x ∉ Z := fun hx ↦ Set.disjoint_left.1 c.2 hxc hx
  obtain ⟨y, hyD, hyx⟩ := hbij.2.2 (by simpa using hxZ)
  have hyx_ne : y ≠ x := by
    intro h
    exact hfix y hyD (hyx.trans h.symm)
  have hadj_yx : (partialGraph D g).Adj y x := by
    exact ⟨hyx_ne, Or.inl ⟨hyD, hyx⟩⟩
  have hyc : y ∈ c.1.supp := c.1.mem_supp_of_adj_mem_supp hxc hadj_yx.symm
  have hyZ : y ∉ Z := fun hy ↦ Set.disjoint_left.1 c.2 hyc hy
  obtain ⟨z, hzD, hzy⟩ := hbij.2.2 (by simpa using hyZ)
  have hzy_ne : z ≠ y := by
    intro h
    exact hfix z hzD (hzy.trans h.symm)
  have hadj_zy : (partialGraph D g).Adj z y := by
    exact ⟨hzy_ne, Or.inl ⟨hzD, hzy⟩⟩
  have hzc : z ∈ c.1.supp := c.1.mem_supp_of_adj_mem_supp hyc hadj_zy.symm
  have hzx_ne : z ≠ x := by
    intro hzx
    subst z
    exact htwo x hzD y hyD hzy hyx
  have hcard : 2 < c.1.supp.ncard := (Set.two_lt_ncard_iff c.1.supp.toFinite).2
    ⟨x, y, z, hxc, hyc, hzc, hyx_ne.symm, hzx_ne.symm, hzy_ne.symm⟩
  have heq : c.1.supp.ncard = Fintype.card c.1.supp := by
    calc
      c.1.supp.ncard = Nat.card c.1.supp := (Nat.card_coe_set_eq _).symm
      _ = Fintype.card c.1.supp := Nat.card_eq_fintype_card
  omega

private def freeVerticesEmbedding {D Z : Finset V} {g : V → V} :
    (Σ c : FreeComponent D Z g, c.1.supp) ↪ {x : V // x ∉ Z} where
  toFun v := ⟨v.2.1, Set.disjoint_left.1 v.1.2 v.2.2⟩
  inj' := by
    rintro ⟨c, x⟩ ⟨d, y⟩ hxy
    have hval : x.1 = y.1 := congr_arg Subtype.val hxy
    have hcd : c = d := by
      apply Subtype.ext
      exact SimpleGraph.ConnectedComponent.eq_of_common_vertex x.2
        (hval ▸ y.2)
    subst d
    have hxy' : x = y := Subtype.ext hval
    subst y
    rfl

private lemma freeComponent_card_le_third {D Z : Finset V} {g : V → V}
    (hbij : Set.BijOn g (↑D : Set V) (↑Z : Set V)ᶜ)
    (hfix : ∀ x ∈ D, g x ≠ x)
    (htwo : ∀ x ∈ D, ∀ y ∈ D, g x = y → g y = x → False) :
    Fintype.card (FreeComponent D Z g) ≤ (Fintype.card V - Z.card) / 3 := by
  classical
  have hsum : 3 * Fintype.card (FreeComponent D Z g) ≤
      Fintype.card (Σ c : FreeComponent D Z g, c.1.supp) := by
    rw [Fintype.card_sigma]
    calc
      3 * Fintype.card (FreeComponent D Z g) =
          ∑ _c : FreeComponent D Z g, 3 := by simp [Nat.mul_comm]
      _ ≤ ∑ c : FreeComponent D Z g, Fintype.card c.1.supp := by
        exact Finset.sum_le_sum fun _ _ ↦ freeComponent_three_le_card hbij hfix htwo _
  have hinj := Fintype.card_le_of_injective
    (freeVerticesEmbedding (D := D) (Z := Z) (g := g))
    (freeVerticesEmbedding (D := D) (Z := Z) (g := g)).injective
  have hcompl : Fintype.card {x : V // x ∉ Z} = Fintype.card V - Z.card := by
    simpa using (Fintype.card_subtype_compl (fun x : V ↦ x ∈ Z))
  rw [hcompl] at hinj
  omega

private def otherEvaluation {D Z : Finset V} {g : V → V}
    (c₀ : FreeComponent D Z g) :
    solutionSpace D Z g →ₗ[ℂ] ({c : FreeComponent D Z g // c ≠ c₀} → ℂ) where
  toFun f c := componentValue f c.1.1
  map_add' f h := by
    funext c
    exact componentValue_add f h c.1.1
  map_smul' a f := by
    funext c
    exact componentValue_smul a f c.1.1

private lemma otherEvaluation_injective {D Z : Finset V} {g : V → V}
    (c₀ : FreeComponent D Z g) :
    Function.Injective (otherEvaluation c₀) := by
  intro f h hfh
  apply Subtype.ext
  funext x
  have hzero : otherEvaluation c₀ (f - h) = 0 := by
    rw [map_sub, hfh, sub_self]
  let u : solutionSpace D Z g := f - h
  have hu_other : ∀ c : FreeComponent D Z g, c ≠ c₀ → componentValue u c.1 = 0 := by
    intro c hc
    exact congr_fun hzero ⟨c, hc⟩
  have hu_outside : ∀ y : V,
      (partialGraph D g).connectedComponentMk y ≠ c₀.1 → u.1 y = 0 := by
    intro y hy
    by_cases hc : Disjoint
        ((partialGraph D g).connectedComponentMk y).supp (↑Z : Set V)
    · exact hu_other ⟨_, hc⟩ (fun he ↦ hy (congr_arg Subtype.val he))
    · rw [Set.not_disjoint_iff] at hc
      obtain ⟨z, hzc, hzZ⟩ := hc
      have hryz : (partialGraph D g).Reachable y z :=
        SimpleGraph.ConnectedComponent.exact hzc.symm
      exact (value_eq_of_reachable u hryz).trans (u.2.2.1 z hzZ)
  have hu_on : ∀ y ∈ c₀.1.supp, u.1 y = componentValue u c₀.1 := by
    intro y hy
    rw [← componentValue_mk u y, hy]
  have hsum : (∑ y, u.1 y) =
      (c₀.1.supp.toFinset.card : ℂ) * componentValue u c₀.1 := by
    calc
      (∑ y, u.1 y) = ∑ y ∈ c₀.1.supp.toFinset, u.1 y := by
        symm
        apply Finset.sum_subset (Finset.subset_univ _)
        intro y _ hy
        exact hu_outside y fun he ↦ hy (by simpa using he)
      _ = ∑ _y ∈ c₀.1.supp.toFinset, componentValue u c₀.1 := by
        apply Finset.sum_congr rfl
        intro y hy
        exact hu_on y (by simpa using hy)
      _ = (c₀.1.supp.toFinset.card : ℂ) * componentValue u c₀.1 := by simp
  have hcard_pos : c₀.1.supp.toFinset.card ≠ 0 := by
    exact Finset.card_ne_zero.mpr (by
      obtain ⟨y, hy⟩ := c₀.1.nonempty_supp
      exact ⟨y, by simpa using hy⟩)
  have hcoeff : (c₀.1.supp.toFinset.card : ℂ) ≠ 0 := by exact_mod_cast hcard_pos
  have hu_c₀ : componentValue u c₀.1 = 0 := by
    exact (mul_eq_zero.mp (by rw [← hsum]; exact u.2.2.2)).resolve_left hcoeff
  have hux : u.1 x = 0 := by
    by_cases hx : (partialGraph D g).connectedComponentMk x = c₀.1
    · have : u.1 x = componentValue u c₀.1 := by
        rw [← hx]
        rfl
      exact this.trans hu_c₀
    · exact hu_outside x hx
  apply sub_eq_zero.mp
  simpa [u] using hux

/-- The abstract finite mechanism behind WI-088's one-third defect cap. -/
theorem finrank_solutionSpace_le {D Z : Finset V} {g : V → V}
    (hbij : Set.BijOn g (↑D : Set V) (↑Z : Set V)ᶜ)
    (hfix : ∀ x ∈ D, g x ≠ x)
    (htwo : ∀ x ∈ D, ∀ y ∈ D, g x = y → g y = x → False) :
    Module.finrank ℂ (solutionSpace D Z g) ≤ ((Fintype.card V - Z.card) / 3) - 1 := by
  classical
  by_cases hF : Nonempty (FreeComponent D Z g)
  · let c₀ : FreeComponent D Z g := Classical.choice hF
    have hinj : Function.Injective (otherEvaluation c₀) := otherEvaluation_injective c₀
    have hdim := (otherEvaluation c₀).finrank_le_finrank_of_injective hinj
    rw [Module.finrank_fintype_fun_eq_card] at hdim
    have hlt : Fintype.card {c : FreeComponent D Z g // c ≠ c₀} <
        Fintype.card (FreeComponent D Z g) := by
      apply Fintype.card_lt_of_injective_of_notMem (fun c ↦ c.1) Subtype.val_injective
      rintro ⟨c, hc⟩
      exact c.2 hc
    have hfree := freeComponent_card_le_third hbij hfix htwo
    omega
  · have hempty : IsEmpty (FreeComponent D Z g) := not_nonempty_iff.mp hF
    have hinj : Function.Injective (freeEvaluation (D := D) (Z := Z) (g := g)) :=
      freeEvaluation_injective
    have hdim := (freeEvaluation (D := D) (Z := Z) (g := g)).finrank_le_finrank_of_injective hinj
    rw [Module.finrank_fintype_fun_eq_card, Fintype.card_eq_zero] at hdim
    exact hdim.trans (Nat.zero_le _)

#print axioms finrank_solutionSpace_le

end Mathia.WI088
