import WI088PrimePartialMap

/-!
# WI-102 full-packing collapsed rotation

Associated finding:
`research/weil_inertia/findings/WI-102-full-recurrent-packing-is-an-exact-collapsed-circle-rotation.md`

Formalized theorem boundary:
under `0 < d < s < p`, equality of the WI-088 forced-zero interval with the omitted
interval is equivalent to the boundary residue `[(k+1)d]_p = s`.  In that case the
order-preserving collapse of the common hole conjugates the exceptional map to addition by
`s-d` on `ZMod (p-d)`.  The generated rotation subgroup has cardinality
`(p-d) / gcd (s-d) (p-d)`, and its orbit quotient has cardinality
`gcd (s-d) (p-d)`.

Not formalized:
the Ramanujan/Fourier bridge, the full cross-Gram rank formula, WI-096's `tau = c-1`
identity, the positive-slack `U != 1` theorem, Yang consequences, or zeta-zero bounds.
-/

namespace Mathia.WI102

open Mathia.WI088

/-- The ordinary nonwrapping interval `[s-d,s)` omitted from the exceptional domain. -/
def exceptionalHole (p d s : ℕ) [NeZero p] : Finset (ZMod p) :=
  Finset.univ.filter fun x ↦ s - d ≤ x.val ∧ x.val < s

@[simp]
theorem mem_exceptionalHole {p d s : ℕ} [NeZero p] (x : ZMod p) :
    x ∈ exceptionalHole p d s ↔ s - d ≤ x.val ∧ x.val < s := by
  simp [exceptionalHole]

/-- The existing WI-088 exceptional domain is exactly the complement of the omitted interval. -/
theorem exceptionalDomain_eq_hole_compl {p d s : ℕ} [NeZero p] :
    exceptionalDomain p d s = (exceptionalHole p d s)ᶜ := by
  ext x
  simp only [mem_exceptionalDomain, Finset.mem_compl, mem_exceptionalHole]
  omega

private theorem mem_exceptionalZero_iff {p d k : ℕ} [NeZero p] (x : ZMod p) :
    x ∈ exceptionalZero p d k ↔
      ∃ y : ZMod p, y.val < d ∧ y + (k * d : ZMod p) = x := by
  simp only [exceptionalZero, Finset.mem_map, mem_exceptionalBase]
  constructor
  · rintro ⟨y, hy, rfl⟩
    exact ⟨y, hy, by simp [exceptionalShift, add_comm]⟩
  · rintro ⟨y, hy, hxy⟩
    refine ⟨y, hy, ?_⟩
    simpa [exceptionalShift] using hxy

private theorem nextResidue_of_currentResidue {p d s k : ℕ} [NeZero p]
    (hds : d < s) (hsp : s < p)
    (hcur : ((k * d : ℕ) : ZMod p).val = s - d) :
    (((k + 1) * d : ℕ) : ZMod p).val = s := by
  have hcurEq : ((k * d : ℕ) : ZMod p) = (s - d : ℕ) := by
    apply ZMod.val_injective
    simpa only [Nat.cast_mul, ZMod.val_natCast,
      Nat.mod_eq_of_lt (by omega : s - d < p)] using hcur
  have hnextEq : (((k + 1) * d : ℕ) : ZMod p) = (s : ℕ) := by
    calc
      (((k + 1) * d : ℕ) : ZMod p) =
          ((k * d : ℕ) : ZMod p) + (d : ZMod p) := by
            simp [Nat.add_mul, Nat.cast_add]
      _ = (s - d : ℕ) + (d : ZMod p) := by rw [hcurEq]
      _ = (s : ℕ) := by
        rw [← Nat.cast_add, Nat.sub_add_cancel hds.le]
  rw [hnextEq]
  simp [ZMod.val_natCast, Nat.mod_eq_of_lt hsp]

private theorem currentResidue_of_nextResidue {p d s k : ℕ} [NeZero p]
    (hds : d < s) (hsp : s < p)
    (hnext : (((k + 1) * d : ℕ) : ZMod p).val = s) :
    ((k * d : ℕ) : ZMod p).val = s - d := by
  have hnextEq : (((k + 1) * d : ℕ) : ZMod p) = (s : ℕ) := by
    apply ZMod.val_injective
    simpa only [Nat.cast_mul, Nat.cast_add, Nat.cast_one, ZMod.val_natCast,
      Nat.mod_eq_of_lt hsp] using hnext
  have hsum : ((k * d : ℕ) : ZMod p) + (d : ZMod p) = (s : ℕ) := by
    simpa [Nat.add_mul, Nat.cast_add] using hnextEq
  have hcurEq : ((k * d : ℕ) : ZMod p) = (s - d : ℕ) := by
    apply add_right_cancel (b := (d : ZMod p))
    calc
      ((k * d : ℕ) : ZMod p) + (d : ZMod p) = (s : ℕ) := hsum
      _ = (s - d : ℕ) + (d : ZMod p) := by
        rw [← Nat.cast_add, Nat.sub_add_cancel hds.le]
  rw [hcurEq]
  simp [ZMod.val_natCast, Nat.mod_eq_of_lt (by omega : s - d < p)]

private theorem exceptionalZero_eq_hole_of_currentResidue {p d s k : ℕ} [NeZero p]
    (hd : 0 < d) (hds : d < s) (hsp : s < p)
    (hcur : ((k * d : ℕ) : ZMod p).val = s - d) :
    exceptionalZero p d k = exceptionalHole p d s := by
  have hcurEq : ((k * d : ℕ) : ZMod p) = (s - d : ℕ) := by
    apply ZMod.val_injective
    simpa only [Nat.cast_mul, ZMod.val_natCast,
      Nat.mod_eq_of_lt (by omega : s - d < p)] using hcur
  have hcurEq' : (k : ZMod p) * d = (s - d : ℕ) := by
    simpa only [Nat.cast_mul] using hcurEq
  ext x
  rw [mem_exceptionalZero_iff, mem_exceptionalHole]
  constructor
  · rintro ⟨y, hyd, rfl⟩
    have hsum : y.val + (s - d) < p := by omega
    constructor
    · rw [hcurEq', ZMod.val_add_of_lt (by
          simpa [ZMod.val_natCast, Nat.mod_eq_of_lt (by omega : s - d < p)] using hsum)]
      simp [ZMod.val_natCast, Nat.mod_eq_of_lt (by omega : s - d < p)]
    · rw [hcurEq', ZMod.val_add_of_lt (by
          simpa [ZMod.val_natCast, Nat.mod_eq_of_lt (by omega : s - d < p)] using hsum)]
      simp only [ZMod.val_natCast, Nat.mod_eq_of_lt (by omega : s - d < p)]
      omega
  · rintro ⟨hlo, hhi⟩
    let y : ZMod p := (x.val - (s - d) : ℕ)
    have hyNat : x.val - (s - d) < p := by omega
    have hyval : y.val = x.val - (s - d) := by
      simp [y, ZMod.val_natCast, Nat.mod_eq_of_lt hyNat]
    have hyd : y.val < d := by omega
    refine ⟨y, hyd, ?_⟩
    rw [hcurEq']
    apply ZMod.val_injective
    have hsum : y.val + (s - d) < p := by omega
    rw [ZMod.val_add_of_lt (by
      simpa [ZMod.val_natCast, Nat.mod_eq_of_lt (by omega : s - d < p)] using hsum)]
    simp only [ZMod.val_natCast, Nat.mod_eq_of_lt (by omega : s - d < p), hyval]
    omega

/-- Equality of the two deleted sets forces the least residue `[kd]_p = s-d`. -/
theorem currentResidue_of_exceptionalZero_eq_hole {p d s k : ℕ} [NeZero p]
    (hd : 0 < d) (hds : d < s) (hsp : s < p)
    (hfull : exceptionalZero p d k = exceptionalHole p d s) :
    ((k * d : ℕ) : ZMod p).val = s - d := by
  let a : ZMod p := (k : ZMod p) * d
  let r := a.val
  have hrp : r < p := ZMod.val_lt a
  have hRpos : 0 < s - d := Nat.sub_pos_of_lt hds
  have hrd : r + d ≤ p := by
    by_contra hnot
    have hwrap : p < r + d := Nat.lt_of_not_ge hnot
    let y : ZMod p := (p - r : ℕ)
    have hyrp : p - r < p := by omega
    have hyval : y.val = p - r := by
      simp [y, ZMod.val_natCast, Nat.mod_eq_of_lt hyrp]
    have hyd : y.val < d := by omega
    have hya : y + a = 0 := by
      rw [← ZMod.natCast_zmod_val a]
      dsimp only [y]
      change ((p - r : ℕ) : ZMod p) + (r : ZMod p) = 0
      rw [← Nat.cast_add, Nat.sub_add_cancel hrp.le, ZMod.natCast_self]
    have hzZero : (0 : ZMod p) ∈ exceptionalZero p d k := by
      rw [mem_exceptionalZero_iff]
      exact ⟨y, hyd, by simpa [a] using hya⟩
    have hzHole : (0 : ZMod p) ∈ exceptionalHole p d s := by simpa [hfull] using hzZero
    have := (mem_exceptionalHole (0 : ZMod p)).mp hzHole
    simp only [ZMod.val_zero] at this
    omega
  have haZero : a ∈ exceptionalZero p d k := by
    rw [mem_exceptionalZero_iff]
    exact ⟨0, by simpa using hd, by simp [a]⟩
  have haHole : a ∈ exceptionalHole p d s := by simpa [hfull] using haZero
  have hRr : s - d ≤ r := (mem_exceptionalHole a).mp haHole |>.1
  let Rz : ZMod p := (s - d : ℕ)
  have hRval : Rz.val = s - d := by
    simp [Rz, ZMod.val_natCast, Nat.mod_eq_of_lt (by omega : s - d < p)]
  have hRHole : Rz ∈ exceptionalHole p d s := by
    rw [mem_exceptionalHole, hRval]
    omega
  have hRZero : Rz ∈ exceptionalZero p d k := by simpa [hfull] using hRHole
  obtain ⟨y, hyd, hya⟩ := (mem_exceptionalZero_iff Rz).mp hRZero
  change y + a = Rz at hya
  have hsum : y.val + a.val < p := by omega
  have hval := congrArg ZMod.val hya
  rw [ZMod.val_add_of_lt hsum, hRval] at hval
  dsimp only [r] at hRr
  have haVal : a.val = s - d := by omega
  simpa only [a, Nat.cast_mul] using haVal

/-- Coincidence of the deleted sets yields both boundary residues in WI-102 (21)--(22). -/
theorem boundaryResidues_of_exceptionalZero_eq_hole {p d s k : ℕ} [NeZero p]
    (hd : 0 < d) (hds : d < s) (hsp : s < p)
    (hfull : exceptionalZero p d k = exceptionalHole p d s) :
    ((k * d : ℕ) : ZMod p).val = s - d ∧
      (((k + 1) * d : ℕ) : ZMod p).val = s := by
  have hcur := currentResidue_of_exceptionalZero_eq_hole hd hds hsp hfull
  exact ⟨hcur, nextResidue_of_currentResidue hds hsp hcur⟩

/-- Under the interval side conditions, the next boundary residue is exactly equivalent to
coincidence of the forced-zero and omitted intervals. -/
theorem exceptionalZero_eq_hole_iff_nextResidue {p d s k : ℕ} [NeZero p]
    (hd : 0 < d) (hds : d < s) (hsp : s < p) :
    exceptionalZero p d k = exceptionalHole p d s ↔
      (((k + 1) * d : ℕ) : ZMod p).val = s := by
  constructor
  · intro hfull
    exact (boundaryResidues_of_exceptionalZero_eq_hole hd hds hsp hfull).2
  · intro hnext
    exact exceptionalZero_eq_hole_of_currentResidue hd hds hsp
      (currentResidue_of_nextResidue hds hsp hnext)

/-- The representative used by the order-preserving collapse of the omitted interval. -/
def collapseValue {p : ℕ} (d s : ℕ) [NeZero p] (x : ZMod p) : ℕ :=
  if x.val < s - d then x.val else x.val - d

/-- The inverse representative which re-inserts the omitted interval. -/
def expandValue {p : ℕ} (d s : ℕ) (y : Fin (p - d)) : ℕ :=
  if y.val < s - d then y.val else y.val + d

/-- The explicit representative-level collapse as an equivalence with `Fin (p-d)`. -/
def exceptionalCollapseFin {p d s : ℕ} [NeZero p] (hds : d < s) (hsp : s < p) :
    {x : ZMod p // x ∈ exceptionalDomain p d s} ≃ Fin (p - d) where
  toFun x := ⟨collapseValue d s x.1, by
    have hxD := (mem_exceptionalDomain x.1).mp x.2
    rw [collapseValue]
    split
    · omega
    · have hxhigh : s ≤ x.1.val := hxD.resolve_left (by assumption)
      exact Nat.sub_lt_sub_right (by omega : d ≤ x.1.val) (ZMod.val_lt x.1)⟩
  invFun y := ⟨(expandValue d s y : ℕ), by
    rw [mem_exceptionalDomain]
    rw [expandValue]
    split
    · left
      simpa [ZMod.val_natCast, Nat.mod_eq_of_lt (by omega : y.val < p)]
    · right
      have hy : y.val + d < p := by omega
      have hval : (((y.val + d : ℕ) : ZMod p)).val = y.val + d := by
        rw [ZMod.val_natCast, Nat.mod_eq_of_lt hy]
      rw [hval]
      omega⟩
  left_inv x := by
    by_cases hlow : x.1.val < s - d
    · apply Subtype.ext
      apply ZMod.val_injective
      simp [collapseValue, expandValue, hlow, ZMod.val_natCast,
        Nat.mod_eq_of_lt (by omega : x.1.val < p)]
    · have hxhigh : s ≤ x.1.val :=
        ((mem_exceptionalDomain x.1).mp x.2).resolve_left hlow
      have hxsub : x.1.val - d < p - d :=
        Nat.sub_lt_sub_right (by omega : d ≤ x.1.val) (ZMod.val_lt x.1)
      have hsubNot : ¬x.1.val - d < s - d := by omega
      apply Subtype.ext
      apply ZMod.val_injective
      simp [collapseValue, expandValue, hlow, hsubNot,
        Nat.sub_add_cancel (by omega : d ≤ x.1.val), ZMod.val_natCast,
        Nat.mod_eq_of_lt (by omega : x.1.val < p)]
  right_inv y := by
    by_cases hlow : y.val < s - d
    · apply Fin.ext
      simp [collapseValue, expandValue, hlow, ZMod.val_natCast,
        Nat.mod_eq_of_lt (by omega : y.val < p)]
    · have hyadd : y.val + d < p := by omega
      have haddNot : ¬y.val + d < s - d := by omega
      have hcastval : (((y.val + d : ℕ) : ZMod p)).val = y.val + d := by
        rw [ZMod.val_natCast, Nat.mod_eq_of_lt hyadd]
      apply Fin.ext
      simp only [collapseValue, expandValue, hlow, if_false]
      rw [hcastval, if_neg haddNot]
      omega

/-- The standard representative equivalence between `Fin n` and nonzero `ZMod n`, exposed
locally so its representative formula remains transparent. -/
def finZModEquiv (n : ℕ) [NeZero n] : Fin n ≃ ZMod n where
  toFun y := (y.val : ℕ)
  invFun z := ⟨z.val, ZMod.val_lt z⟩
  left_inv y := by
    apply Fin.ext
    simp [ZMod.val_natCast, Nat.mod_eq_of_lt y.isLt]
  right_inv z := by
    apply ZMod.val_injective
    simp [ZMod.val_natCast, Nat.mod_eq_of_lt (ZMod.val_lt z)]

/-- The genuine collapse equivalence from the exceptional domain to the cyclic set of size
`p-d`. -/
noncomputable def exceptionalCollapse {p d s : ℕ} [NeZero p]
    (hds : d < s) (hsp : s < p) :
    {x : ZMod p // x ∈ exceptionalDomain p d s} ≃ ZMod (p - d) := by
  letI : NeZero (p - d) := ⟨by omega⟩
  exact (exceptionalCollapseFin hds hsp).trans (finZModEquiv (p - d))

@[simp]
theorem exceptionalCollapse_val {p d s : ℕ} [NeZero p]
    (hds : d < s) (hsp : s < p)
    (x : {x : ZMod p // x ∈ exceptionalDomain p d s}) :
    (exceptionalCollapse hds hsp x).val = collapseValue d s x.1 := by
  letI : NeZero (p - d) := ⟨by omega⟩
  change ((finZModEquiv (p - d)) (exceptionalCollapseFin hds hsp x)).val = _
  rw [show (finZModEquiv (p - d)) (exceptionalCollapseFin hds hsp x) =
      (((exceptionalCollapseFin hds hsp x).val : ℕ) : ZMod (p - d)) from rfl]
  rw [ZMod.val_natCast]
  rw [Nat.mod_eq_of_lt (exceptionalCollapseFin hds hsp x).isLt]
  rfl

/-- The collapse preserves the ordinary order of least representatives. -/
theorem exceptionalCollapse_order {p d s : ℕ} [NeZero p]
    (hds : d < s) (hsp : s < p)
    (x y : {x : ZMod p // x ∈ exceptionalDomain p d s}) :
    (exceptionalCollapse hds hsp x).val < (exceptionalCollapse hds hsp y).val ↔
      x.1.val < y.1.val := by
  rw [exceptionalCollapse_val, exceptionalCollapse_val]
  simp only [collapseValue]
  have hxD := (mem_exceptionalDomain x.1).mp x.2
  have hyD := (mem_exceptionalDomain y.1).mp y.2
  split <;> split <;> omega

private theorem exceptionalMap_mem_domain_of_full {p d s k : ℕ} [NeZero p]
    (hds : d < s) (hsp : s < p)
    (hfull : exceptionalZero p d k = exceptionalHole p d s)
    (x : ZMod p) (hx : x ∈ exceptionalDomain p d s) :
    exceptionalMap p d s k x ∈ exceptionalDomain p d s := by
  have hnotZero : exceptionalMap p d s k x ∉ exceptionalZero p d k :=
    (exceptionalMap_bijOn hds hsp).mapsTo hx
  rw [exceptionalDomain_eq_hole_compl, Finset.mem_compl]
  simpa only [← hfull] using hnotZero

/-- Under coincidence of the deleted sets, the WI-088 partial map restricts to a genuine
permutation of its exceptional domain. -/
noncomputable def fullPackingExceptionalPerm {p d s k : ℕ} [NeZero p]
    (hds : d < s) (hsp : s < p)
    (hfull : exceptionalZero p d k = exceptionalHole p d s) :
    Equiv.Perm {x : ZMod p // x ∈ exceptionalDomain p d s} := by
  let f : {x : ZMod p // x ∈ exceptionalDomain p d s} →
      {x : ZMod p // x ∈ exceptionalDomain p d s} :=
    fun x ↦ ⟨exceptionalMap p d s k x.1,
      exceptionalMap_mem_domain_of_full hds hsp hfull x.1 x.2⟩
  apply Equiv.ofBijective f
  constructor
  · intro x y hxy
    apply Subtype.ext
    apply (exceptionalMap_bijOn hds hsp).injOn x.2 y.2
    exact congrArg Subtype.val hxy
  · intro y
    have hyNotZero : y.1 ∈ (↑(exceptionalZero p d k) : Set (ZMod p))ᶜ := by
      rw [Set.mem_compl_iff]
      have hyNotHole : y.1 ∉ exceptionalHole p d s := by
        rw [← Finset.mem_compl, ← exceptionalDomain_eq_hole_compl]
        exact y.2
      intro hyZero
      apply hyNotHole
      have hyZero' : y.1 ∈ exceptionalZero p d k := hyZero
      rw [hfull] at hyZero'
      exact hyZero'
    obtain ⟨x, hxD, hxy⟩ := (exceptionalMap_bijOn hds hsp).surjOn hyNotZero
    refine ⟨⟨x, hxD⟩, ?_⟩
    exact Subtype.ext hxy

@[simp]
theorem fullPackingExceptionalPerm_apply_val {p d s k : ℕ} [NeZero p]
    (hds : d < s) (hsp : s < p)
    (hfull : exceptionalZero p d k = exceptionalHole p d s)
    (x : {x : ZMod p // x ∈ exceptionalDomain p d s}) :
    (fullPackingExceptionalPerm hds hsp hfull x).1 = exceptionalMap p d s k x.1 :=
  rfl

/-- Pointwise collapsed-rotation conjugacy. -/
theorem exceptionalCollapse_conjugacy_apply {p d s k : ℕ} [NeZero p]
    (hd : 0 < d) (hds : d < s) (hsp : s < p)
    (hfull : exceptionalZero p d k = exceptionalHole p d s)
    (x : {x : ZMod p // x ∈ exceptionalDomain p d s}) :
    exceptionalCollapse hds hsp (fullPackingExceptionalPerm hds hsp hfull x) =
      exceptionalCollapse hds hsp x + ((s - d : ℕ) : ZMod (p - d)) := by
  letI : NeZero (p - d) := ⟨by omega⟩
  have hbounds := boundaryResidues_of_exceptionalZero_eq_hole hd hds hsp hfull
  have hcurEq : (k : ZMod p) * d = (s - d : ℕ) := by
    apply ZMod.val_injective
    simpa only [Nat.cast_mul, ZMod.val_natCast,
      Nat.mod_eq_of_lt (by omega : s - d < p)] using hbounds.1
  have hnextEq : (k : ZMod p) * d + d = (s : ℕ) := by
    have hnextEq' : (((k + 1) * d : ℕ) : ZMod p) = (s : ℕ) := by
      apply ZMod.val_injective
      simpa only [Nat.cast_mul, Nat.cast_add, Nat.cast_one, ZMod.val_natCast,
        Nat.mod_eq_of_lt hsp] using hbounds.2
    simpa [Nat.add_mul, Nat.cast_add, Nat.cast_mul] using hnextEq'
  have hRval : ((s - d : ℕ) : ZMod (p - d)).val = s - d := by
    rw [ZMod.val_natCast, Nat.mod_eq_of_lt (by omega : s - d < p - d)]
  apply ZMod.val_injective
  rw [exceptionalCollapse_val, ZMod.val_add, exceptionalCollapse_val, hRval]
  simp only [fullPackingExceptionalPerm_apply_val]
  have hxD := (mem_exceptionalDomain x.1).mp x.2
  by_cases hxlow : x.1.val < s - d
  · have hmap : exceptionalMap p d s k x.1 = x.1 + (s : ℕ) := by
      rw [exceptionalMap, if_pos hxlow]
      calc
        (k : ZMod p) * d + (x.1 + d) = x.1 + ((k : ZMod p) * d + d) := by abel
        _ = x.1 + (s : ℕ) := by rw [hnextEq]
    by_cases hnowrap : x.1.val + s < p
    · have hgval : (exceptionalMap p d s k x.1).val = x.1.val + s := by
        rw [hmap, ZMod.val_add_of_lt]
        · simp [ZMod.val_natCast, Nat.mod_eq_of_lt hsp]
        · simp [ZMod.val_natCast, Nat.mod_eq_of_lt hsp]
          exact hnowrap
      rw [collapseValue, hgval, if_neg (by omega : ¬x.1.val + s < s - d)]
      rw [collapseValue, if_pos hxlow]
      rw [Nat.mod_eq_of_lt (by omega : x.1.val + (s - d) < p - d)]
      omega
    · have hwrap : p ≤ x.1.val + s := Nat.le_of_not_gt hnowrap
      have hgval : (exceptionalMap p d s k x.1).val = x.1.val + s - p := by
        rw [hmap, ZMod.val_add_of_le]
        · simp [ZMod.val_natCast, Nat.mod_eq_of_lt hsp]
        · simpa [ZMod.val_natCast, Nat.mod_eq_of_lt hsp] using hwrap
      rw [collapseValue, hgval, if_pos (by omega : x.1.val + s - p < s - d)]
      rw [collapseValue, if_pos hxlow]
      rw [Nat.mod_eq_sub_mod (by omega : p - d ≤ x.1.val + (s - d))]
      rw [Nat.mod_eq_of_lt (by omega : x.1.val + (s - d) - (p - d) < p - d)]
      omega
  · have hxhigh : s ≤ x.1.val := hxD.resolve_left hxlow
    have hmap : exceptionalMap p d s k x.1 = x.1 + (s - d : ℕ) := by
      rw [exceptionalMap, if_neg hxlow, hcurEq]
      abel
    by_cases hnowrap : x.1.val + (s - d) < p
    · have hgval : (exceptionalMap p d s k x.1).val = x.1.val + (s - d) := by
        rw [hmap, ZMod.val_add_of_lt]
        · simp [ZMod.val_natCast, Nat.mod_eq_of_lt (by omega : s - d < p)]
        · simp [ZMod.val_natCast, Nat.mod_eq_of_lt (by omega : s - d < p)]
          exact hnowrap
      rw [collapseValue, hgval, if_neg (by omega : ¬x.1.val + (s - d) < s - d)]
      rw [collapseValue, if_neg hxlow]
      rw [Nat.mod_eq_of_lt (by omega : x.1.val - d + (s - d) < p - d)]
      omega
    · have hwrap : p ≤ x.1.val + (s - d) := Nat.le_of_not_gt hnowrap
      have hgval : (exceptionalMap p d s k x.1).val = x.1.val + (s - d) - p := by
        rw [hmap, ZMod.val_add_of_le]
        · simp [ZMod.val_natCast, Nat.mod_eq_of_lt (by omega : s - d < p)]
        · simpa [ZMod.val_natCast, Nat.mod_eq_of_lt (by omega : s - d < p)] using hwrap
      have hgLow : x.1.val + (s - d) - p < s - d := by
        rw [Nat.sub_lt_iff_lt_add hwrap]
        have hxp := ZMod.val_lt x.1
        omega
      rw [collapseValue, hgval,
        if_pos hgLow]
      rw [collapseValue, if_neg hxlow]
      have hmodWrap : p - d ≤ x.1.val - d + (s - d) := by omega
      have hxCollapsedLt : x.1.val - d < p - d :=
        Nat.sub_lt_sub_right (by omega : d ≤ x.1.val) (ZMod.val_lt x.1)
      have hremLt : x.1.val - d + (s - d) - (p - d) < p - d := by
        have hsubadd : x.1.val - d + (s - d) - (p - d) + (p - d) =
            x.1.val - d + (s - d) := Nat.sub_add_cancel hmodWrap
        omega
      rw [Nat.mod_eq_sub_mod hmodWrap]
      rw [Nat.mod_eq_of_lt hremLt]
      omega

/-- The full-packing exceptional permutation is semiconjugate (indeed conjugate, since the
collapse is an equivalence) to addition by `s-d` on `ZMod (p-d)`. -/
theorem exceptionalCollapse_conjugacy {p d s k : ℕ} [NeZero p]
    (hd : 0 < d) (hds : d < s) (hsp : s < p)
    (hfull : exceptionalZero p d k = exceptionalHole p d s) :
    Function.Semiconj (exceptionalCollapse hds hsp)
      (fullPackingExceptionalPerm hds hsp hfull)
      (Equiv.addRight ((s - d : ℕ) : ZMod (p - d))) := by
  intro x
  exact exceptionalCollapse_conjugacy_apply hd hds hsp hfull x

/-- The subgroup generated by one rotation step.  Its cosets are exactly the rotation orbits. -/
def rotationSubgroup (t R : ℕ) : AddSubgroup (ZMod t) :=
  AddSubgroup.zmultiples ((R : ℕ) : ZMod t)

/-- The quotient which indexes the orbits of translation by `R` on `ZMod t`. -/
abbrev RotationOrbitSpace (t R : ℕ) :=
  (ZMod t) ⧸ rotationSubgroup t R

/-- Every rotation orbit is a coset of the generated subgroup and therefore has this common
length. -/
theorem rotation_common_orbit_length (t R : ℕ) (ht : 0 < t) :
    Nat.card (rotationSubgroup t R) = t / Nat.gcd R t := by
  letI : NeZero t := ⟨ht.ne'⟩
  rw [rotationSubgroup, Nat.card_zmultiples, ZMod.addOrderOf_coe R ht.ne']
  rw [Nat.gcd_comm]

/-- Translation by `R` on `ZMod t` has exactly `gcd R t` orbits. -/
theorem rotation_orbit_count (t R : ℕ) (ht : 0 < t) :
    Nat.card (RotationOrbitSpace t R) = Nat.gcd R t := by
  letI : NeZero t := ⟨ht.ne'⟩
  change (AddSubgroup.zmultiples ((R : ℕ) : ZMod t)).index = Nat.gcd R t
  have hgen : AddSubgroup.zmultiples (1 : ZMod t) = ⊤ := by
    rw [eq_top_iff]
    intro x _
    rw [AddSubgroup.mem_zmultiples_iff]
    refine ⟨(x.val : ℤ), ?_⟩
    rw [natCast_zsmul]
    simp
  have h := AddSubgroup.index_zmultiples_zsmul hgen (R : ℤ)
  simpa [ZMod.addOrderOf_one, Int.gcd_eq_natAbs_gcd_natAbs, Nat.gcd_comm] using h

/-- The exact cycle count and common cycle length for the WI-102 collapsed rotation. -/
theorem fullPacking_rotation_cycle_data {p d s : ℕ}
    (hds : d < s) (hsp : s < p) :
    Nat.card (RotationOrbitSpace (p - d) (s - d)) = Nat.gcd (s - d) (p - d) ∧
      Nat.card (rotationSubgroup (p - d) (s - d)) =
        (p - d) / Nat.gcd (s - d) (p - d) := by
  have ht : 0 < p - d := by omega
  exact ⟨rotation_orbit_count (p - d) (s - d) ht,
    rotation_common_orbit_length (p - d) (s - d) ht⟩

#print axioms exceptionalZero_eq_hole_iff_nextResidue
#print axioms exceptionalCollapse_conjugacy
#print axioms fullPacking_rotation_cycle_data

end Mathia.WI102
