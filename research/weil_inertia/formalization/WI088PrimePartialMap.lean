import WI088PartialBijection

/-!
# WI-088 exceptional-strip partial map

Associated finding:
`research/weil_inertia/findings/WI-088-residual-prime-ramanujan-rank-defect-is-sharply-capped-at-one-third.md`

Formalized theorem boundary:
the explicit partial bijection on `ZMod p` used in the exceptional close-prime strip.  Its
domain omits an interval of length `d`, its forced-zero set is a translate of the initial
interval of length `d`, and the directed map has no cycles of length one or two under the
arithmetic hypotheses arising from the residual boundary decomposition.

Not formalized:
the Fourier reduction producing the edge and forced-zero equations, the final Ramanujan
cross-Gram rank inequality, the WI-087 asymptotic family, or any analytic number theory.
-/

namespace Mathia.WI088

open scoped BigOperators

/-- The interval of `d` residues which will be translated to the forced-zero set. -/
def exceptionalBase (p d : ℕ) [NeZero p] : Finset (ZMod p) :=
  Finset.univ.filter fun x ↦ x.val < d

/-- The exceptional-strip domain: the complement of `[s-d,s)`. -/
def exceptionalDomain (p d s : ℕ) [NeZero p] : Finset (ZMod p) :=
  Finset.univ.filter fun x ↦ x.val < s - d ∨ s ≤ x.val

/-- Before the common translation, the lower part of the domain is shifted by `d`. -/
def exceptionalCore (p d s : ℕ) [NeZero p] (x : ZMod p) : ZMod p :=
  if x.val < s - d then x + d else x

/-- Translation by `k*d` on `ZMod p`. -/
def exceptionalShift (p d k : ℕ) [NeZero p] : ZMod p ≃ ZMod p :=
  Equiv.addRight (k * d : ZMod p)

/-- The forced-zero set, a translate by `k*d` of the initial `d` residues. -/
def exceptionalZero (p d k : ℕ) [NeZero p] : Finset (ZMod p) :=
  (exceptionalBase p d).map (exceptionalShift p d k).toEmbedding

/-- The exceptional-strip directed partial map. -/
def exceptionalMap (p d s k : ℕ) [NeZero p] (x : ZMod p) : ZMod p :=
  (k * d : ZMod p) + if x.val < s - d then x + d else x

@[simp] lemma mem_exceptionalBase {p d : ℕ} [NeZero p] (x : ZMod p) :
    x ∈ exceptionalBase p d ↔ x.val < d := by
  simp [exceptionalBase]

@[simp] lemma mem_exceptionalDomain {p d s : ℕ} [NeZero p] (x : ZMod p) :
    x ∈ exceptionalDomain p d s ↔ x.val < s - d ∨ s ≤ x.val := by
  simp [exceptionalDomain]

lemma exceptionalBase_card {p d : ℕ} [NeZero p] (hdp : d ≤ p) :
    (exceptionalBase p d).card = d := by
  classical
  apply Finset.card_eq_of_bijective (fun i (_hi : i < d) ↦ (i : ZMod p))
  · intro x hx
    refine ⟨x.val, (mem_exceptionalBase x).mp hx, ?_⟩
    simpa using ZMod.natCast_zmod_val x
  · intro i hi
    exact (mem_exceptionalBase _).mpr (by
      simp [ZMod.val_natCast, Nat.mod_eq_of_lt (hi.trans_le hdp), hi])
  · intro i j hi hj hij
    have hi' : i < p := hi.trans_le hdp
    have hj' : j < p := hj.trans_le hdp
    have hval := congrArg ZMod.val hij
    simpa [ZMod.val_natCast, Nat.mod_eq_of_lt hi', Nat.mod_eq_of_lt hj'] using hval

/-- The forced-zero translate has exactly `d` elements. -/
theorem exceptionalZero_card {p d k : ℕ} [NeZero p] (hdp : d ≤ p) :
    (exceptionalZero p d k).card = d := by
  rw [exceptionalZero, Finset.card_map, exceptionalBase_card hdp]

private lemma exceptionalCore_bijOn {p d s : ℕ} [NeZero p]
    (hds : d < s) (hsp : s < p) :
    Set.BijOn (exceptionalCore p d s)
      (↑(exceptionalDomain p d s) : Set (ZMod p))
      (↑(exceptionalBase p d) : Set (ZMod p))ᶜ := by
  classical
  refine ⟨?_, ?_, ?_⟩
  · intro x hx
    rw [Set.mem_compl_iff]
    by_cases hlow : x.val < s - d
    · have hsum : x.val + d < p := by omega
      simp only [exceptionalCore, if_pos hlow, mem_exceptionalBase, Finset.mem_coe]
      rw [ZMod.val_add_of_lt (by
        simpa [ZMod.val_natCast, Nat.mod_eq_of_lt (by omega : d < p)] using hsum)]
      simp only [ZMod.val_natCast, Nat.mod_eq_of_lt (by omega : d < p)]
      omega
    · have hxhigh : s ≤ x.val := (mem_exceptionalDomain x).mp hx |>.resolve_left hlow
      simp [exceptionalCore, hlow, exceptionalBase]
      omega
  · intro x hx y hy hxy
    by_cases hxlow : x.val < s - d
    · by_cases hylow : y.val < s - d
      · simp only [exceptionalCore, if_pos hxlow, if_pos hylow] at hxy
        exact add_right_cancel hxy
      · have hyhigh : s ≤ y.val := (mem_exceptionalDomain y).mp hy |>.resolve_left hylow
        have hxsum : x.val + d < p := by omega
        have hval := congrArg ZMod.val hxy
        simp only [exceptionalCore, if_pos hxlow, if_neg hylow] at hval
        rw [ZMod.val_add_of_lt (by
          simpa [ZMod.val_natCast, Nat.mod_eq_of_lt (by omega : d < p)] using hxsum)] at hval
        simp only [ZMod.val_natCast, Nat.mod_eq_of_lt (by omega : d < p)] at hval
        omega
    · have hxhigh : s ≤ x.val := (mem_exceptionalDomain x).mp hx |>.resolve_left hxlow
      by_cases hylow : y.val < s - d
      · have hysum : y.val + d < p := by omega
        have hval := congrArg ZMod.val hxy
        simp only [exceptionalCore, if_neg hxlow, if_pos hylow] at hval
        rw [ZMod.val_add_of_lt (by
          simpa [ZMod.val_natCast, Nat.mod_eq_of_lt (by omega : d < p)] using hysum)] at hval
        simp only [ZMod.val_natCast, Nat.mod_eq_of_lt (by omega : d < p)] at hval
        omega
      · simpa [exceptionalCore, hxlow, hylow] using hxy
  · intro y hy
    have hyd : d ≤ y.val := by
      simpa [exceptionalBase] using hy
    by_cases hys : y.val < s
    · let x : ZMod p := (y.val - d : ℕ)
      have hxp : y.val - d < p := by omega
      have hxval : x.val = y.val - d := by
        simp [x, ZMod.val_natCast, Nat.mod_eq_of_lt hxp]
      have hxlow : x.val < s - d := by omega
      refine ⟨x, (mem_exceptionalDomain x).mpr (Or.inl hxlow), ?_⟩
      rw [exceptionalCore, if_pos hxlow]
      apply ZMod.val_injective
      rw [ZMod.val_add_of_lt (by
        simp only [hxval, ZMod.val_natCast, Nat.mod_eq_of_lt (by omega : d < p)]
        omega)]
      simp only [hxval, ZMod.val_natCast, Nat.mod_eq_of_lt (by omega : d < p)]
      exact Nat.sub_add_cancel hyd
    · have hsy : s ≤ y.val := Nat.le_of_not_gt hys
      have hnotlow : ¬y.val < s - d := by omega
      refine ⟨y, (mem_exceptionalDomain y).mpr (Or.inr hsy), ?_⟩
      simp [exceptionalCore, hnotlow]

private lemma equiv_bijOn_compl_map {V : Type*} [Fintype V] [DecidableEq V]
    (e : V ≃ V) (S : Finset V) :
    Set.BijOn e (↑S : Set V)ᶜ (↑(S.map e.toEmbedding) : Set V)ᶜ := by
  classical
  refine ⟨?_, e.injective.injOn, ?_⟩
  · intro x hx
    simp only [Set.mem_compl_iff, Finset.mem_coe, Finset.mem_map]
    intro he
    obtain ⟨y, hy, hyx⟩ := he
    exact hx (e.injective hyx ▸ hy)
  · intro y hy
    refine ⟨e.symm y, ?_, e.apply_symm_apply y⟩
    rw [Set.mem_compl_iff]
    intro hmem
    apply hy
    simp only [Finset.mem_coe, Finset.mem_map]
    exact ⟨e.symm y, hmem, e.apply_symm_apply y⟩

/-- The explicit exceptional-strip map is a bijection from its domain onto the complement of
the forced-zero translate. -/
theorem exceptionalMap_bijOn {p d s k : ℕ} [NeZero p]
    (hds : d < s) (hsp : s < p) :
    Set.BijOn (exceptionalMap p d s k)
      (↑(exceptionalDomain p d s) : Set (ZMod p))
      (↑(exceptionalZero p d k) : Set (ZMod p))ᶜ := by
  have hcomp := (equiv_bijOn_compl_map (exceptionalShift p d k) (exceptionalBase p d)).comp
    (exceptionalCore_bijOn hds hsp)
  apply hcomp.congr
  intro x hx
  simp [exceptionalMap, exceptionalCore, exceptionalShift, add_comm, Nat.cast_mul]

private lemma natCast_mul_ne_zero {p a b : ℕ} (hp : p.Prime)
    (ha : 0 < a) (hap : a < p) (hb : 0 < b) (hbp : b < p) :
    ((a * b : ℕ) : ZMod p) ≠ 0 := by
  intro hzero
  have hdvd : p ∣ a * b := (ZMod.natCast_eq_zero_iff (a * b) p).mp hzero
  rcases (hp.dvd_mul).mp hdvd with ha' | hb'
  · exact (Nat.not_dvd_of_pos_of_lt ha hap) ha'
  · exact (Nat.not_dvd_of_pos_of_lt hb hbp) hb'

private lemma natCast_mul_ne_zero_of_lt_two_mul {p a b : ℕ} (hp : p.Prime)
    (ha : 0 < a) (ha2p : a < 2 * p) (hne : a ≠ p)
    (hb : 0 < b) (hbp : b < p) :
    (((a * b : ℕ) : ZMod p)) ≠ 0 := by
  intro hzero
  have hdvd : p ∣ a * b := (ZMod.natCast_eq_zero_iff (a * b) p).mp hzero
  have hpa : p ∣ a := (hp.dvd_mul.mp hdvd).resolve_right fun hpb ↦
    (Nat.not_dvd_of_pos_of_lt hb hbp) hpb
  obtain ⟨c, rfl⟩ := hpa
  have hcpos : 0 < c := by
    by_contra hc
    have : c = 0 := Nat.eq_zero_of_not_pos hc
    subst c
    simp at ha
  have hc2 : c < 2 := by
    apply (Nat.mul_lt_mul_left hp.pos).mp
    simpa [Nat.mul_comm] using ha2p
  have hc : c = 1 := by omega
  subst c
  exact hne (by simp)

/-- No point of the exceptional domain is fixed. -/
theorem exceptionalMap_ne_self {p d s k : ℕ} [NeZero p]
    (hp : p.Prime) (hdpos : 0 < d) (hds : d < s) (hsp : s < p)
    (hkpos : 0 < k) (hkbound : 2 * k + 1 ≤ p)
    (x : ZMod p) (hx : x ∈ exceptionalDomain p d s) :
    exceptionalMap p d s k x ≠ x := by
  intro hfix
  by_cases hlow : x.val < s - d
  · have hk1p : k + 1 < p := by omega
    have hne := natCast_mul_ne_zero hp (by omega : 0 < k + 1) hk1p hdpos (by omega : d < p)
    apply hne
    simp [exceptionalMap, hlow] at hfix
    have hzero : (k * d : ZMod p) + (d : ZMod p) = 0 := by
      linear_combination hfix
    simpa [Nat.add_mul, Nat.cast_add, Nat.cast_mul] using hzero
  · have hkp : k < p := by omega
    have hne := natCast_mul_ne_zero hp hkpos hkp hdpos (by omega : d < p)
    apply hne
    simp [exceptionalMap, hlow] at hfix
    have hzero : (k * d : ZMod p) = 0 := by
      linear_combination hfix
    simpa [Nat.cast_mul] using hzero

/-- The exceptional-strip directed map has no directed cycle of length two on its domain.  In
the critical case `2*k+1=p`, oddness of `p` and evenness of `d` identify a half-step which
lands in the omitted interval. -/
theorem exceptionalMap_no_two_cycle {p d s k : ℕ} [NeZero p]
    (hp : p.Prime) (hpodd : Odd p) (hdpos : 0 < d) (hdeven : Even d)
    (hds : d < s) (hsp : s < p) (hkpos : 0 < k) (hkbound : 2 * k + 1 ≤ p)
    (x : ZMod p) (hx : x ∈ exceptionalDomain p d s)
    (y : ZMod p) (hy : y ∈ exceptionalDomain p d s)
    (hxy : exceptionalMap p d s k x = y)
    (hyx : exceptionalMap p d s k y = x) : False := by
  have hdltp : d < p := hds.trans hsp
  by_cases hxlow : x.val < s - d
  · by_cases hylow : y.val < s - d
    · have hcoeffpos : 0 < 2 * (k + 1) := by omega
      have hcoefflt : 2 * (k + 1) < 2 * p := by omega
      have hcoeffne : 2 * (k + 1) ≠ p := by
        intro heq
        have hpEven : Even p := heq ▸ even_two_mul (k + 1)
        exact (Nat.not_even_iff_odd.mpr hpodd) hpEven
      have hne := natCast_mul_ne_zero_of_lt_two_mul hp hcoeffpos hcoefflt hcoeffne
        hdpos hdltp
      apply hne
      simp [exceptionalMap, hxlow, hylow] at hxy hyx
      push_cast
      linear_combination hxy + hyx
    · have hyhigh : s ≤ y.val := (mem_exceptionalDomain y).mp hy |>.resolve_left hylow
      by_cases hcrit : 2 * k + 1 = p
      · obtain ⟨e, rfl⟩ := hdeven
        have hz : ((2 * k + 1 : ℕ) : ZMod p) = 0 := by
          rw [hcrit]
          exact CharP.cast_eq_zero (ZMod p) p
        have hyxe : y = x + (e : ZMod p) := by
          simp [exceptionalMap, hxlow] at hxy
          rw [← hxy]
          push_cast at hz ⊢
          linear_combination e * hz
        have he_lt_p : e < p := by omega
        have hsum : x.val + e < p := by omega
        have hval := congrArg ZMod.val hyxe
        rw [ZMod.val_add_of_lt (by
          simpa [ZMod.val_natCast, Nat.mod_eq_of_lt he_lt_p] using hsum)] at hval
        simp only [ZMod.val_natCast, Nat.mod_eq_of_lt he_lt_p] at hval
        omega
      · have hcoefflt : 2 * k + 1 < p := lt_of_le_of_ne hkbound hcrit
        have hne := natCast_mul_ne_zero hp (by omega : 0 < 2 * k + 1) hcoefflt
          hdpos hdltp
        apply hne
        simp [exceptionalMap, hxlow, hylow] at hxy hyx
        push_cast
        linear_combination hxy + hyx
  · have hxhigh : s ≤ x.val := (mem_exceptionalDomain x).mp hx |>.resolve_left hxlow
    by_cases hylow : y.val < s - d
    · by_cases hcrit : 2 * k + 1 = p
      · obtain ⟨e, rfl⟩ := hdeven
        have hz : ((2 * k + 1 : ℕ) : ZMod p) = 0 := by
          rw [hcrit]
          exact CharP.cast_eq_zero (ZMod p) p
        have hxye : x = y + (e : ZMod p) := by
          simp [exceptionalMap, hylow] at hyx
          rw [← hyx]
          push_cast at hz ⊢
          linear_combination e * hz
        have he_lt_p : e < p := by omega
        have hsum : y.val + e < p := by omega
        have hval := congrArg ZMod.val hxye
        rw [ZMod.val_add_of_lt (by
          simpa [ZMod.val_natCast, Nat.mod_eq_of_lt he_lt_p] using hsum)] at hval
        simp only [ZMod.val_natCast, Nat.mod_eq_of_lt he_lt_p] at hval
        omega
      · have hcoefflt : 2 * k + 1 < p := lt_of_le_of_ne hkbound hcrit
        have hne := natCast_mul_ne_zero hp (by omega : 0 < 2 * k + 1) hcoefflt
          hdpos hdltp
        apply hne
        simp [exceptionalMap, hxlow, hylow] at hxy hyx
        push_cast
        linear_combination hxy + hyx
    · have hne := natCast_mul_ne_zero hp (by omega : 0 < 2 * k)
        (by omega : 2 * k < p) hdpos hdltp
      apply hne
      simp [exceptionalMap, hxlow, hylow] at hxy hyx
      push_cast
      linear_combination hxy + hyx

/-- All finite-map facts needed by `finrank_solutionSpace_le`, packaged with the exact
exceptional-strip parameters. -/
theorem exceptionalMap_package {p d s k : ℕ} [NeZero p]
    (hp : p.Prime) (hpodd : Odd p) (hdpos : 0 < d) (hdeven : Even d)
    (hds : d < s) (hsp : s < p) (hkpos : 0 < k) (hkbound : 2 * k + 1 ≤ p) :
    (exceptionalZero p d k).card = d ∧
      Set.BijOn (exceptionalMap p d s k)
        (↑(exceptionalDomain p d s) : Set (ZMod p))
        (↑(exceptionalZero p d k) : Set (ZMod p))ᶜ ∧
      (∀ x ∈ exceptionalDomain p d s, exceptionalMap p d s k x ≠ x) ∧
      (∀ x ∈ exceptionalDomain p d s, ∀ y ∈ exceptionalDomain p d s,
        exceptionalMap p d s k x = y → exceptionalMap p d s k y = x → False) := by
  refine ⟨exceptionalZero_card (hds.trans hsp).le, exceptionalMap_bijOn hds hsp, ?_, ?_⟩
  · exact fun x hx ↦ exceptionalMap_ne_self hp hdpos hds hsp hkpos hkbound x hx
  · exact fun x hx y hy ↦ exceptionalMap_no_two_cycle hp hpodd hdpos hdeven hds hsp hkpos
      hkbound x hx y hy

#print axioms exceptionalMap_package

end Mathia.WI088
