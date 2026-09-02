import WI081PairwiseRamanujanRank
import WI088PrimePartialMap

/-!
# WI-088 residual prime Ramanujan rank floor

Associated finding:
`research/weil_inertia/findings/WI-088-residual-prime-ramanujan-rank-defect-is-sharply-capped-at-one-third.md`

Formalized theorem boundary:
for distinct odd primes `p < q`, if the nearest-`p*q` boundary defect is larger than `q - 1`,
then the primitive-frequency cross Gram has rank at least
`min (p - 1) ((p + q + 2) / 3)`.  The file also formalizes the finite row-kernel and partial-
bijection lemmas used in that bound.

Not formalized:
the WI-087 prime-number-theorem asymptotic sharpness family, Yang covariance conclusions,
many-modulus inertia, or any improvement to a zeta zero-proportion bound.
-/

noncomputable section

open scoped BigOperators ComplexConjugate ComplexOrder

namespace Mathia.WI088

open Mathia.WI081

private lemma primitive_isPrimitiveRoot {m : ℕ} (z : PrimitiveFrequency m) :
    IsPrimitiveRoot (z : ℂ) m :=
  isPrimitiveRoot_of_mem_primitiveRoots z.property

private lemma primitive_ne_zero {m : ℕ} (hm : 0 < m) (z : PrimitiveFrequency m) :
    (z : ℂ) ≠ 0 :=
  (primitive_isPrimitiveRoot z).isUnit hm.ne' |>.ne_zero

private lemma primitive_norm_eq_one {m : ℕ} (hm : 0 < m) (z : PrimitiveFrequency m) :
    ‖(z : ℂ)‖ = 1 :=
  (primitive_isPrimitiveRoot z).norm'_eq_one hm.ne'

/-- The `p`-periodic sequence represented by a primitive-frequency row coefficient vector. -/
def rowSequence (p : ℕ) [NeZero p] (c : PrimitiveFrequency p → ℂ) (r : ZMod p) : ℂ :=
  ∑ z : PrimitiveFrequency p, c z * star ((z : ℂ) ^ r.val)

/-- `rowSequence` as a complex-linear map. -/
def rowSequenceLinear (p : ℕ) [NeZero p] :
    (PrimitiveFrequency p → ℂ) →ₗ[ℂ] (ZMod p → ℂ) where
  toFun := rowSequence p
  map_add' c c' := by
    ext r
    simp only [rowSequence, Pi.add_apply, add_mul, Finset.sum_add_distrib]
  map_smul' a c := by
    ext r
    simp only [rowSequence, Pi.smul_apply, smul_eq_mul, RingHom.id_apply, Finset.mul_sum,
      mul_assoc]

private lemma sum_zmod_powers_eq_zero {p : ℕ} [NeZero p] (hp : p.Prime)
    (z : PrimitiveFrequency p) :
    (∑ r : ZMod p, (z : ℂ) ^ r.val) = 0 := by
  cases p with
  | zero => exact (NeZero.ne 0 rfl).elim
  | succ n =>
      rw [← Fintype.sum_equiv (ZMod.finEquiv (n + 1))
        (fun i : Fin (n + 1) ↦ (z : ℂ) ^ i.val)
        (fun r : ZMod (n + 1) ↦ (z : ℂ) ^ r.val) (by
          intro i
          rfl)]
      rw [Fin.sum_univ_eq_sum_range]
      exact (primitive_isPrimitiveRoot z).geom_sum_eq_zero hp.one_lt

/-- A primitive-frequency row sequence has zero mean over one `p`-period. -/
theorem rowSequence_sum_eq_zero {p : ℕ} [NeZero p] (hp : p.Prime)
    (c : PrimitiveFrequency p → ℂ) :
    ∑ r : ZMod p, rowSequence p c r = 0 := by
  simp_rw [rowSequence]
  rw [Finset.sum_comm]
  apply Finset.sum_eq_zero
  intro z hz
  rw [← Finset.mul_sum]
  have hstar : (∑ r : ZMod p, star ((z : ℂ) ^ r.val)) = 0 := by
    have h := congrArg star (sum_zmod_powers_eq_zero hp z)
    simpa only [star_sum, star_zero] using h
  rw [hstar, mul_zero]

/-- Primitive-frequency coefficients are recovered from their `p`-periodic row sequence. -/
theorem rowSequenceLinear_injective {p : ℕ} [NeZero p] (hp : p.Prime) :
    Function.Injective (rowSequenceLinear p) := by
  let A := shiftedSamplingMatrix p (p - 1) 0
  let B := A.conjTranspose
  have htot : p - 1 = Nat.totient p := (Nat.totient_prime hp).symm
  have hLI : LinearIndependent ℂ A.row := by
    apply shiftedSamplingMatrix_rows_linearIndependent hp.pos
    rw [← htot]
  have hrankA : A.rank = p - 1 := by
    simpa using hLI.rank_matrix
  have hrankB : B.rank = p - 1 := by
    change A.conjTranspose.rank = p - 1
    rw [Matrix.rank_conjTranspose, hrankA]
  have hB : Function.Injective B.vecMulLinear := by
    rw [← LinearMap.ker_eq_bot, ← Submodule.finrank_eq_zero]
    have hdim := LinearMap.finrank_range_add_finrank_ker B.vecMulLinear
    have hrange : Module.finrank ℂ (LinearMap.range B.vecMulLinear) = p - 1 := by
      rw [range_vecMulLinear, ← B.rank_eq_finrank_span_row, hrankB]
    rw [hrange, Module.finrank_fintype_fun_eq_card, primitiveFrequency_card,
      Nat.totient_prime hp] at hdim
    omega
  intro c c' hcc'
  apply hB
  ext i
  have hip : i.val < p := lt_of_lt_of_le i.isLt (Nat.sub_le p 1)
  have hi := congr_fun hcc' (i.val : ZMod p)
  simpa [rowSequenceLinear, rowSequence, Matrix.vecMulLinear_apply, B, A, Matrix.vecMul,
    dotProduct, shiftedSamplingMatrix, ZMod.val_natCast_of_lt hip] using hi

private lemma primitive_pow_mod {p n : ℕ} (hp : p.Prime) (z : PrimitiveFrequency p) :
    (z : ℂ) ^ n = (z : ℂ) ^ (n % p) := by
  calc
    (z : ℂ) ^ n = (z : ℂ) ^ (n % p + p * (n / p)) := by
      rw [Nat.mod_add_div]
    _ = (z : ℂ) ^ (n % p) * ((z : ℂ) ^ p) ^ (n / p) := by
      rw [pow_add, pow_mul]
    _ = (z : ℂ) ^ (n % p) := by
      rw [(primitive_isPrimitiveRoot z).pow_eq_one, one_pow, mul_one]

/-- Evaluating a row sequence at a natural residue may be done before reducing modulo `p`. -/
theorem rowSequence_natCast {p : ℕ} [NeZero p] (hp : p.Prime)
    (c : PrimitiveFrequency p → ℂ) (n : ℕ) :
    rowSequence p c (n : ZMod p) =
      ∑ z : PrimitiveFrequency p, c z * star ((z : ℂ) ^ n) := by
  rw [rowSequence]
  apply Finset.sum_congr rfl
  intro z hz
  rw [ZMod.val_natCast, ← primitive_pow_mod hp z]

/-- A shifted short-boundary cross Gram, before the final nearest-boundary transport. -/
def boundaryProduct (p q δ start : ℕ) :
    Matrix (PrimitiveFrequency p) (PrimitiveFrequency q) ℂ :=
  (shiftedSamplingMatrix p δ start).conjTranspose *
    shiftedSamplingMatrix q δ start

private lemma boundaryProduct_vecMul_eq {p q δ start : ℕ} [NeZero p]
    (hp : p.Prime) (c : PrimitiveFrequency p → ℂ) (w : PrimitiveFrequency q) :
    (boundaryProduct p q δ start).vecMul c w =
      (w : ℂ) ^ start *
        ∑ x : Fin δ, rowSequence p c ((start + x.val : ℕ) : ZMod p) *
          (w : ℂ) ^ x.val := by
  simp only [boundaryProduct, Matrix.vecMul, Matrix.mul_apply, dotProduct,
    Matrix.conjTranspose_apply, shiftedSamplingMatrix]
  rw [Finset.mul_sum]
  simp_rw [rowSequence_natCast hp, Finset.sum_mul, Finset.mul_sum]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro x hx
  apply Finset.sum_congr rfl
  intro z hz
  rw [pow_add, pow_add]
  ring

/-- A row-kernel vector gives a vanishing boundary polynomial of its periodic row sequence. -/
theorem rowSequence_boundary_relation {p q δ start : ℕ} [NeZero p]
    (hp : p.Prime) (hq : q.Prime) (c : PrimitiveFrequency p → ℂ)
    (hc : c ∈ LinearMap.ker (boundaryProduct p q δ start).vecMulLinear)
    (w : PrimitiveFrequency q) :
    ∑ x : Fin δ, rowSequence p c ((start + x.val : ℕ) : ZMod p) *
      (w : ℂ) ^ x.val = 0 := by
  have hzero := congr_fun hc w
  rw [Matrix.vecMulLinear_apply, boundaryProduct_vecMul_eq hp] at hzero
  exact (mul_eq_zero.mp hzero).resolve_left (pow_ne_zero _ (primitive_ne_zero hq.pos w))

/-- Sum of a finite sequence over one residue class modulo `q`. -/
def residueSum (q δ : ℕ) (a : ℕ → ℂ) (j : Fin q) : ℂ :=
  ∑ x ∈ Finset.range δ, if x % q = j.val then a x else 0

private lemma boundary_sum_eq_residue_sums {q δ : ℕ} (hq : q.Prime)
    (a : ℕ → ℂ) (w : PrimitiveFrequency q) :
    (∑ x ∈ Finset.range δ, a x * (w : ℂ) ^ x) =
      ∑ j : Fin q, residueSum q δ a j * (w : ℂ) ^ j.val := by
  calc
    (∑ x ∈ Finset.range δ, a x * (w : ℂ) ^ x) =
        ∑ x ∈ Finset.range δ, a x * (w : ℂ) ^ (x % q) := by
      apply Finset.sum_congr rfl
      intro x hx
      rw [primitive_pow_mod hq w]
    _ = ∑ x ∈ Finset.range δ,
        ∑ j : Fin q, if x % q = j.val then a x * (w : ℂ) ^ j.val else 0 := by
      apply Finset.sum_congr rfl
      intro x hx
      let jx : Fin q := ⟨x % q, Nat.mod_lt x hq.pos⟩
      have hiff (j : Fin q) : x % q = j.val ↔ j = jx := by
        constructor
        · intro h
          apply Fin.ext
          exact h.symm
        · intro h
          simpa [jx, h]
      simp only [hiff]
      rw [Fintype.sum_ite_eq' jx]
    _ = ∑ j : Fin q, residueSum q δ a j * (w : ℂ) ^ j.val := by
      rw [Finset.sum_comm]
      apply Finset.sum_congr rfl
      intro j hj
      rw [residueSum, Finset.sum_mul]
      apply Finset.sum_congr rfl
      intro x hx
      by_cases h : x % q = j.val <;> simp [h]

/-- Primitive-`q` vanishing of a boundary polynomial forces all residue sums to agree. -/
theorem residueSums_eq_of_vanish {q δ : ℕ} (hq : q.Prime) (a : ℕ → ℂ)
    (hvanish : ∀ w : PrimitiveFrequency q,
      ∑ x ∈ Finset.range δ, a x * (w : ℂ) ^ x = 0) :
    ∀ i j : Fin q, residueSum q δ a i = residueSum q δ a j := by
  let lastQ : Fin q := ⟨q - 1, Nat.sub_lt hq.pos Nat.one_pos⟩
  let coeff : Fin (q - 1) → ℂ := fun i ↦
    residueSum q δ a (Fin.castLE (Nat.sub_le q 1) i) - residueSum q δ a lastQ
  let A := shiftedSamplingMatrix q (q - 1) 0
  have hLI : LinearIndependent ℂ A.row := by
    apply shiftedSamplingMatrix_rows_linearIndependent hq.pos
    rw [Nat.totient_prime hq]
  have hcomb : ∑ i : Fin (q - 1), coeff i • A.row i = 0 := by
    funext w
    simp only [Finset.sum_apply, Pi.smul_apply, smul_eq_mul, A, Matrix.row_apply,
      shiftedSamplingMatrix, zero_add]
    change (∑ i : Fin (q - 1), coeff i * (w : ℂ) ^ i.val) = 0
    have hres := hvanish w
    rw [boundary_sum_eq_residue_sums hq] at hres
    have hsplit : q - 1 + 1 = q := Nat.sub_add_cancel hq.pos
    let e : Fin (q - 1 + 1) ≃ Fin q := finCongr hsplit
    have hres' :
        (∑ i : Fin (q - 1 + 1),
          residueSum q δ a (e i) * (w : ℂ) ^ (e i).val) = 0 := by
      calc
        (∑ i : Fin (q - 1 + 1),
            residueSum q δ a (e i) * (w : ℂ) ^ (e i).val) =
            ∑ j : Fin q, residueSum q δ a j * (w : ℂ) ^ j.val :=
          e.sum_comp (fun j ↦ residueSum q δ a j * (w : ℂ) ^ j.val)
        _ = 0 := hres
    have hgeom : (∑ i : Fin q, (w : ℂ) ^ i.val) = 0 := by
      rw [Fin.sum_univ_eq_sum_range]
      exact (primitive_isPrimitiveRoot w).geom_sum_eq_zero hq.one_lt
    have hgeom' :
        (∑ i : Fin (q - 1 + 1), (w : ℂ) ^ (e i).val) = 0 := by
      calc
        (∑ i : Fin (q - 1 + 1), (w : ℂ) ^ (e i).val) =
            ∑ j : Fin q, (w : ℂ) ^ j.val := e.sum_comp (fun j ↦ (w : ℂ) ^ j.val)
        _ = 0 := hgeom
    have e_castSucc (i : Fin (q - 1)) :
        e i.castSucc = Fin.castLE (Nat.sub_le q 1) i := by
      apply Fin.ext
      rfl
    have e_last : e (Fin.last (q - 1)) = lastQ := by
      apply Fin.ext
      rfl
    rw [Fin.sum_univ_castSucc] at hres' hgeom'
    simp only [e_castSucc, e_last, Fin.val_castLE, Fin.val_castSucc, Fin.val_last] at hres' hgeom'
    simp only [coeff, Fin.val_castLE] at ⊢
    simp_rw [sub_mul]
    rw [Finset.sum_sub_distrib, ← Finset.mul_sum]
    linear_combination hres' - residueSum q δ a lastQ * hgeom'
  rw [Fintype.linearIndependent_iff] at hLI
  have hcoeff : ∀ i, coeff i = 0 := hLI coeff hcomb
  intro i j
  have hi : residueSum q δ a i = residueSum q δ a lastQ := by
    by_cases hilast : i.val = q - 1
    · exact congrArg (residueSum q δ a) (Fin.ext hilast)
    · have hiLt : i.val < q - 1 := by omega
      let i' : Fin (q - 1) := ⟨i.val, hiLt⟩
      have hz := hcoeff i'
      simp only [coeff, sub_eq_zero] at hz
      simpa [i', Fin.castLE] using hz
  have hj : residueSum q δ a j = residueSum q δ a lastQ := by
    by_cases hjlast : j.val = q - 1
    · exact congrArg (residueSum q δ a) (Fin.ext hjlast)
    · have hjLt : j.val < q - 1 := by omega
      let j' : Fin (q - 1) := ⟨j.val, hjLt⟩
      have hz := hcoeff j'
      simp only [coeff, sub_eq_zero] at hz
      simpa [j', Fin.castLE] using hz
  exact hi.trans hj.symm

/-- Explicit block formula for residue sums when `δ = k*q+s`, `s<q`. -/
theorem residueSum_eq_blocks {q k s : ℕ} (hq : 0 < q) (hs : s < q)
    (a : ℕ → ℂ) (j : Fin q) :
    residueSum q (k * q + s) a j =
      ∑ l ∈ Finset.range (if j.val < s then k + 1 else k), a (j.val + l * q) := by
  classical
  rw [residueSum, ← Finset.sum_filter]
  have hset :
      (Finset.range (k * q + s)).filter (fun x ↦ x % q = j.val) =
        (Finset.range (if j.val < s then k + 1 else k)).image
          (fun l ↦ j.val + l * q) := by
    ext x
    simp only [Finset.mem_filter, Finset.mem_range, Finset.mem_image]
    constructor
    · rintro ⟨hx, hmod⟩
      refine ⟨x / q, ?_, ?_⟩
      · split_ifs with hj
        · have hxq : x < (k + 1) * q := by nlinarith
          exact (Nat.div_lt_iff_lt_mul hq).2 hxq
        · have hxle : x / q ≤ k := by
            have hxq : x < (k + 1) * q := by nlinarith
            exact Nat.le_of_lt_succ ((Nat.div_lt_iff_lt_mul hq).2 hxq)
          have hne : x / q ≠ k := by
            intro heq
            have hdecomp := Nat.mod_add_div x q
            nlinarith
          omega
      · have hdecomp := Nat.mod_add_div x q
        nlinarith
    · rintro ⟨l, hl, rfl⟩
      have hjq : j.val < q := j.isLt
      constructor
      · split_ifs at hl with hj
        · have hle : l ≤ k := by omega
          by_cases hlk : l = k
          · subst l
            nlinarith
          · have hlt : l < k := by omega
            nlinarith
        · have hlt : l < k := hl
          nlinarith
      · simpa [Nat.add_mul_mod_self_left, Nat.mod_eq_of_lt hjq]
  rw [hset, Finset.sum_image]
  intro l₁ hl₁ l₂ hl₂ h
  have : l₁ * q = l₂ * q := by nlinarith
  exact Nat.eq_of_mul_eq_mul_right hq this

private lemma eq_zero_of_translation_invariant {p : ℕ} [NeZero p] (hp : p.Prime)
    (f : ZMod p → ℂ) (step : ZMod p) (hstep : step ≠ 0)
    (htrans : ∀ r, f (r + step) = f r) (hmean : ∑ r, f r = 0) :
    f = 0 := by
  letI : Fact p.Prime := ⟨hp⟩
  have hn : ∀ n : ℕ, f ((n : ZMod p) * step) = f 0 := by
    intro n
    induction n with
    | zero => simp
    | succ n ih =>
        rw [Nat.cast_succ, add_mul, one_mul, htrans, ih]
  have hconst : ∀ r : ZMod p, f r = f 0 := by
    intro r
    let n : ZMod p := r * step⁻¹
    have hrepr : (n.val : ZMod p) * step = r := by
      rw [ZMod.natCast_zmod_val]
      dsimp [n]
      rw [mul_assoc, inv_mul_cancel₀ hstep, mul_one]
    rw [← hrepr, hn]
  have hcard : Fintype.card (ZMod p) = p := ZMod.card p
  have hpC : (p : ℂ) ≠ 0 := by exact_mod_cast hp.ne_zero
  have hf0 : f 0 = 0 := by
    rw [show (∑ r : ZMod p, f r) = (p : ℂ) * f 0 by
      simp_rw [hconst]
      simp [hcard]] at hmean
    exact (mul_eq_zero.mp hmean).resolve_left hpC
  funext r
  simp [hconst r, hf0]

/-- The space of row relations of a shifted boundary product. -/
abbrev boundaryRowKernel (p q δ start : ℕ) :=
  LinearMap.ker (boundaryProduct p q δ start).vecMulLinear

/-- A boundary row relation sent to its periodic sequence. -/
def kernelSequenceLinear (p q δ start : ℕ) [NeZero p] :
    boundaryRowKernel p q δ start →ₗ[ℂ] (ZMod p → ℂ) :=
  (rowSequenceLinear p).comp (boundaryRowKernel p q δ start).subtype

theorem kernelSequenceLinear_injective {p q δ start : ℕ} [NeZero p] (hp : p.Prime) :
    Function.Injective (kernelSequenceLinear p q δ start) := by
  intro c c' h
  apply Subtype.ext
  exact rowSequenceLinear_injective hp h

/-- Rank-nullity for the row action of a shifted boundary product. -/
theorem boundaryProduct_rank_add_rowKernel {p q δ start : ℕ} :
    (boundaryProduct p q δ start).rank +
      Module.finrank ℂ (boundaryRowKernel p q δ start) = Nat.totient p := by
  have hdim := LinearMap.finrank_range_add_finrank_ker
    (boundaryProduct p q δ start).vecMulLinear
  rw [range_vecMulLinear,
    ← (boundaryProduct p q δ start).rank_eq_finrank_span_row,
    Module.finrank_fintype_fun_eq_card, primitiveFrequency_card] at hdim
  exact hdim

/-- The `q` residue sums of every boundary row-kernel sequence are equal. -/
theorem boundaryKernel_residueSums_eq {p q δ start : ℕ} [NeZero p]
    (hp : p.Prime) (hq : q.Prime) (c : boundaryRowKernel p q δ start) :
    let f := kernelSequenceLinear p q δ start c
    let a := fun n : ℕ ↦ f ((start + n : ℕ) : ZMod p)
    ∀ i j : Fin q, residueSum q δ a i = residueSum q δ a j := by
  dsimp only
  apply residueSums_eq_of_vanish hq
  intro w
  rw [← Fin.sum_univ_eq_sum_range]
  exact rowSequence_boundary_relation hp hq c.1 c.2 w

private lemma first_eq_last_of_shifted_sum {n : ℕ} (b : ℕ → ℂ)
    (h : (∑ l ∈ Finset.range (n + 1), b l) =
      ∑ l ∈ Finset.range (n + 1), b (l + 1)) :
    b 0 = b (n + 1) := by
  rw [Finset.sum_range_succ', Finset.sum_range_succ] at h
  linear_combination h

private lemma first_eq_last_of_shifted_sum_pos {n : ℕ} (hn : 0 < n) (b : ℕ → ℂ)
    (h : (∑ l ∈ Finset.range n, b l) =
      ∑ l ∈ Finset.range n, b (l + 1)) :
    b 0 = b n := by
  obtain ⟨m, rfl⟩ := Nat.exists_eq_succ_of_ne_zero hn.ne'
  exact first_eq_last_of_shifted_sum b h

/-- Translate a kernel sequence so the boundary starts at residue zero. -/
def translatedKernelSequence {p q δ start : ℕ} [NeZero p]
    (c : boundaryRowKernel p q δ start) (r : ZMod p) : ℂ :=
  kernelSequenceLinear p q δ start c ((start : ZMod p) + r)

private lemma boundaryKernel_residue_block_eq {p q δ start k s d : ℕ} [NeZero p]
    (hp : p.Prime) (hq : q.Prime) (hqd : q = p + d) (hδ : δ = k * q + s)
    (hsq : s < q) (c : boundaryRowKernel p q δ start) (i j : Fin q) :
    (∑ l ∈ Finset.range (if i.val < s then k + 1 else k),
        translatedKernelSequence c ((i.val + l * d : ℕ) : ZMod p)) =
      ∑ l ∈ Finset.range (if j.val < s then k + 1 else k),
        translatedKernelSequence c ((j.val + l * d : ℕ) : ZMod p) := by
  subst δ
  let f := kernelSequenceLinear p q (k * q + s) start c
  let a := fun n : ℕ ↦ f ((start + n : ℕ) : ZMod p)
  have heq := boundaryKernel_residueSums_eq hp hq c i j
  rw [residueSum_eq_blocks hq.pos hsq a i,
    residueSum_eq_blocks hq.pos hsq a j] at heq
  convert heq using 1 <;>
    simp only [translatedKernelSequence, a, f] <;>
    apply Finset.sum_congr rfl
  all_goals
    intro l hl
    congr 1
    simp only [Nat.cast_add, Nat.cast_mul, hqd, ZMod.natCast_self, zero_add, add_zero]

/-- In the exceptional strip, duplicated `q`-classes force a translated interval of zeros. -/
theorem boundaryKernel_forced_zero {p q δ start k s d : ℕ} [NeZero p]
    (hp : p.Prime) (hq : q.Prime) (hqd : q = p + d) (hδ : δ = k * q + s)
    (hds : d < s) (hsp : s < p) (c : boundaryRowKernel p q δ start)
    (j : ℕ) (hjd : j < d) :
    translatedKernelSequence c ((j + k * d : ℕ) : ZMod p) = 0 := by
  have hjq : j < q := by omega
  have hjpq : j + p < q := by omega
  let i : Fin q := ⟨j, hjq⟩
  let i' : Fin q := ⟨j + p, hjpq⟩
  have heq := boundaryKernel_residue_block_eq hp hq hqd hδ (by omega) c i i'
  have hi : i.val < s := by dsimp [i]; omega
  have hi' : ¬ i'.val < s := by dsimp [i']; omega
  dsimp [i, i'] at heq
  simp only [if_pos (show j < s by omega), if_neg (show ¬ j + p < s by omega)] at heq
  have heq' :
      (∑ l ∈ Finset.range (k + 1),
        translatedKernelSequence c ((j + l * d : ℕ) : ZMod p)) =
      ∑ l ∈ Finset.range k,
        translatedKernelSequence c ((j + l * d : ℕ) : ZMod p) := by
    convert heq using 1
    apply Finset.sum_congr rfl
    intro l hl
    congr 1
    simp only [Nat.cast_add, ZMod.natCast_self, zero_add]
    abel
  rw [Finset.sum_range_succ] at heq'
  linear_combination heq'

/-- Equal long residue sums give the selected long-region edge equation. -/
theorem boundaryKernel_long_edge {p q δ start k s d : ℕ} [NeZero p]
    (hp : p.Prime) (hq : q.Prime) (hqd : q = p + d) (hδ : δ = k * q + s)
    (hsq : s < q) (c : boundaryRowKernel p q δ start)
    (j : ℕ) (hj : j < s - d) :
    translatedKernelSequence c ((j + (k + 1) * d : ℕ) : ZMod p) =
      translatedKernelSequence c (j : ZMod p) := by
  have hjq : j < q := by omega
  have hjdq : j + d < q := by omega
  let i : Fin q := ⟨j, hjq⟩
  let i' : Fin q := ⟨j + d, hjdq⟩
  have heq := boundaryKernel_residue_block_eq hp hq hqd hδ hsq c i i'
  have hi : i.val < s := by dsimp [i]; omega
  have hi' : i'.val < s := by dsimp [i']; omega
  dsimp [i, i'] at heq
  simp only [if_pos (show j < s by omega), if_pos (show j + d < s by omega)] at heq
  have heq' :
      (∑ l ∈ Finset.range (k + 1),
        translatedKernelSequence c ((j + l * d : ℕ) : ZMod p)) =
      ∑ l ∈ Finset.range (k + 1),
        translatedKernelSequence c ((j + (l + 1) * d : ℕ) : ZMod p) := by
    convert heq using 1
    apply Finset.sum_congr rfl
    intro l hl
    congr 1
    push_cast
    ring
  simpa only [Nat.zero_mul, Nat.add_zero] using (first_eq_last_of_shifted_sum
    (fun l ↦ translatedKernelSequence c ((j + l * d : ℕ) : ZMod p)) heq').symm

/-- Equal short residue sums give the selected short-region edge equation. -/
theorem boundaryKernel_short_edge {p q δ start k s d : ℕ} [NeZero p]
    (hp : p.Prime) (hq : q.Prime) (hqd : q = p + d) (hδ : δ = k * q + s)
    (hsq : s < q) (hk : 0 < k) (c : boundaryRowKernel p q δ start)
    (j : ℕ) (hsj : s ≤ j) (hjp : j < p) :
    translatedKernelSequence c ((j + k * d : ℕ) : ZMod p) =
      translatedKernelSequence c (j : ZMod p) := by
  have hjq : j < q := by omega
  have hjdq : j + d < q := by omega
  let i : Fin q := ⟨j, hjq⟩
  let i' : Fin q := ⟨j + d, hjdq⟩
  have heq := boundaryKernel_residue_block_eq hp hq hqd hδ hsq c i i'
  have hi : ¬ i.val < s := by dsimp [i]; omega
  have hi' : ¬ i'.val < s := by dsimp [i']; omega
  dsimp [i, i'] at heq
  simp only [if_neg (show ¬ j < s by omega), if_neg (show ¬ j + d < s by omega)] at heq
  have heq' :
      (∑ l ∈ Finset.range k,
        translatedKernelSequence c ((j + l * d : ℕ) : ZMod p)) =
      ∑ l ∈ Finset.range k,
        translatedKernelSequence c ((j + (l + 1) * d : ℕ) : ZMod p) := by
    convert heq using 1
    apply Finset.sum_congr rfl
    intro l hl
    congr 1
    push_cast
    ring
  simpa only [Nat.zero_mul, Nat.add_zero] using (first_eq_last_of_shifted_sum_pos hk
    (fun l ↦ translatedKernelSequence c ((j + l * d : ℕ) : ZMod p)) heq').symm

/-- A full period of long residue classes forces translation invariance. -/
theorem boundaryKernel_long_translation {p q δ start k s d : ℕ} [NeZero p]
    (hp : p.Prime) (hq : q.Prime) (hqd : q = p + d) (hδ : δ = k * q + s)
    (hsq : s < q) (hps : p ≤ s) (c : boundaryRowKernel p q δ start) (r : ZMod p) :
    translatedKernelSequence c (r + ((k + 1) * d : ℕ)) =
      translatedKernelSequence c r := by
  let rd : ZMod p := r + (d : ℕ)
  have hrp : r.val < p := r.val_lt
  have hrdp : rd.val < p := rd.val_lt
  have hrq : r.val < q := by omega
  have hrdq : rd.val < q := by omega
  let i : Fin q := ⟨r.val, hrq⟩
  let i' : Fin q := ⟨rd.val, hrdq⟩
  have heq := boundaryKernel_residue_block_eq hp hq hqd hδ hsq c i i'
  have hi : i.val < s := by dsimp [i]; omega
  have hi' : i'.val < s := by dsimp [i']; omega
  simp only [if_pos hi, if_pos hi'] at heq
  have heq' :
      (∑ l ∈ Finset.range (k + 1),
        translatedKernelSequence c (r + (l * d : ℕ))) =
      ∑ l ∈ Finset.range (k + 1),
        translatedKernelSequence c (r + ((l + 1) * d : ℕ)) := by
    convert heq using 1 <;> apply Finset.sum_congr rfl
    · intro l hl
      congr 1
      dsimp [i]
      push_cast
      rw [ZMod.natCast_zmod_val]
    · intro l hl
      congr 1
      dsimp [i']
      simp only [rd, ZMod.natCast_zmod_val, Nat.cast_add, Nat.cast_mul]
      ring
  simpa only [Nat.zero_mul, Nat.cast_zero, add_zero] using (first_eq_last_of_shifted_sum
    (fun l ↦ translatedKernelSequence c (r + (l * d : ℕ))) heq').symm

/-- A full period of short residue classes forces translation invariance. -/
theorem boundaryKernel_short_translation {p q δ start k s d : ℕ} [NeZero p]
    (hp : p.Prime) (hq : q.Prime) (hqd : q = p + d) (hδ : δ = k * q + s)
    (hsq : s < q) (hkp : 0 < k) (hspq : s + p ≤ q)
    (c : boundaryRowKernel p q δ start) (x : ZMod p) :
    translatedKernelSequence c (x + (k * d : ℕ)) = translatedKernelSequence c x := by
  let r : ZMod p := x - (s : ℕ)
  let rd : ZMod p := r + (d : ℕ)
  have hrp : r.val < p := r.val_lt
  have hrdp : rd.val < p := rd.val_lt
  have hiq : s + r.val < q := by omega
  have hiq' : s + rd.val < q := by omega
  let i : Fin q := ⟨s + r.val, hiq⟩
  let i' : Fin q := ⟨s + rd.val, hiq'⟩
  have heq := boundaryKernel_residue_block_eq hp hq hqd hδ hsq c i i'
  have hi : ¬ i.val < s := by dsimp [i]; omega
  have hi' : ¬ i'.val < s := by dsimp [i']; omega
  simp only [if_neg hi, if_neg hi'] at heq
  have heq' :
      (∑ l ∈ Finset.range k,
        translatedKernelSequence c ((s : ZMod p) + r + (l * d : ℕ))) =
      ∑ l ∈ Finset.range k,
        translatedKernelSequence c ((s : ZMod p) + r + ((l + 1) * d : ℕ)) := by
    convert heq using 1 <;> apply Finset.sum_congr rfl
    · intro l hl
      congr 1
      dsimp [i]
      push_cast
      rw [ZMod.natCast_zmod_val]
    · intro l hl
      congr 1
      dsimp [i']
      simp only [rd, ZMod.natCast_zmod_val, Nat.cast_add, Nat.cast_mul]
      ring
  have hedge := (first_eq_last_of_shifted_sum_pos hkp
    (fun l ↦ translatedKernelSequence c ((s : ZMod p) + r + (l * d : ℕ))) heq').symm
  simpa only [r, Nat.zero_mul, Nat.cast_zero, add_zero, add_sub_cancel] using hedge

/-- Translation does not change the zero-mean equation for a kernel sequence. -/
theorem translatedKernelSequence_sum_eq_zero {p q δ start : ℕ} [NeZero p]
    (hp : p.Prime) (c : boundaryRowKernel p q δ start) :
    ∑ r : ZMod p, translatedKernelSequence c r = 0 := by
  calc
    (∑ r : ZMod p, translatedKernelSequence c r) =
        ∑ r : ZMod p, kernelSequenceLinear p q δ start c r := by
      exact Equiv.sum_comp (Equiv.addLeft (start : ZMod p))
        (kernelSequenceLinear p q δ start c)
    _ = 0 := rowSequence_sum_eq_zero hp c.1

private lemma natCast_mul_ne_zero {p a b : ℕ} (hp : p.Prime) (ha : 0 < a) (hap : a < p)
    (hb : 0 < b) (hbp : b < p) : ((a * b : ℕ) : ZMod p) ≠ 0 := by
  change ¬ ((a * b : ℕ) : ZMod p) = 0
  rw [ZMod.natCast_eq_zero_iff]
  intro hdvd
  rcases (hp.dvd_mul.mp hdvd) with hpa | hpb
  · exact (Nat.not_dvd_of_pos_of_lt ha hap) hpa
  · exact (Nat.not_dvd_of_pos_of_lt hb hbp) hpb

private lemma natCast_ne_zero_of_pos_lt {p a : ℕ} (ha : 0 < a) (hap : a < p) :
    (a : ZMod p) ≠ 0 := by
  intro hzero
  exact (Nat.not_dvd_of_pos_of_lt ha hap) ((ZMod.natCast_eq_zero_iff a p).mp hzero)

private lemma boundaryKernel_eq_zero_of_translated_eq_zero {p q δ start : ℕ} [NeZero p]
    (hp : p.Prime) (c : boundaryRowKernel p q δ start)
    (hzero : translatedKernelSequence c = 0) : c = 0 := by
  apply kernelSequenceLinear_injective hp
  funext r
  have hz := congrFun hzero (r - (start : ZMod p))
  rw [map_zero]
  simpa only [translatedKernelSequence, Pi.zero_apply, add_sub_cancel] using hz

/-- The row kernel is trivial when the long block region contains a complete `p`-period. -/
theorem boundaryKernel_eq_zero_of_long {p q δ start k s d : ℕ} [NeZero p]
    (hp : p.Prime) (hq : q.Prime) (hqd : q = p + d) (hδ : δ = k * q + s)
    (hsq : s < q) (hps : p ≤ s) (hk1p : k + 1 < p)
    (hdne : (d : ZMod p) ≠ 0) (c : boundaryRowKernel p q δ start) : c = 0 := by
  letI : Fact p.Prime := ⟨hp⟩
  have hstep : (((k + 1) * d : ℕ) : ZMod p) ≠ 0 := by
    rw [Nat.cast_mul]
    exact mul_ne_zero (natCast_ne_zero_of_pos_lt (by omega) hk1p) hdne
  have hzero := eq_zero_of_translation_invariant hp (translatedKernelSequence c)
    (((k + 1) * d : ℕ) : ZMod p) hstep
    (boundaryKernel_long_translation hp hq hqd hδ hsq hps c)
    (translatedKernelSequence_sum_eq_zero hp c)
  exact boundaryKernel_eq_zero_of_translated_eq_zero hp c hzero

/-- The row kernel is trivial when the short block region contains a complete `p`-period. -/
theorem boundaryKernel_eq_zero_of_short {p q δ start k s d : ℕ} [NeZero p]
    (hp : p.Prime) (hq : q.Prime) (hqd : q = p + d) (hδ : δ = k * q + s)
    (hsq : s < q) (hk : 0 < k) (hkp : k < p) (hspq : s + p ≤ q)
    (hdne : (d : ZMod p) ≠ 0) (c : boundaryRowKernel p q δ start) : c = 0 := by
  letI : Fact p.Prime := ⟨hp⟩
  have hstep : ((k * d : ℕ) : ZMod p) ≠ 0 := by
    rw [Nat.cast_mul]
    exact mul_ne_zero (natCast_ne_zero_of_pos_lt hk hkp) hdne
  have hzero := eq_zero_of_translation_invariant hp (translatedKernelSequence c)
    ((k * d : ℕ) : ZMod p) hstep
    (boundaryKernel_short_translation hp hq hqd hδ hsq hk hspq c)
    (translatedKernelSequence_sum_eq_zero hp c)
  exact boundaryKernel_eq_zero_of_translated_eq_zero hp c hzero

/-- Outside the close-prime exceptional strip, the shifted boundary product has full row rank. -/
theorem boundaryProduct_rank_eq_full_of_outside {p q δ start k s d : ℕ} [NeZero p]
    (hp : p.Prime) (hq : q.Prime) (hqd : q = p + d) (hδ : δ = k * q + s)
    (hsq : s < q) (hk : 0 < k) (hkp : k < p) (hk1p : k + 1 < p)
    (hdne : (d : ZMod p) ≠ 0) (hout : p ≤ s ∨ s + p ≤ q) :
    (boundaryProduct p q δ start).rank = p - 1 := by
  have hker : boundaryRowKernel p q δ start = ⊥ := by
    rw [Submodule.eq_bot_iff]
    intro c hc
    let c' : boundaryRowKernel p q δ start := ⟨c, hc⟩
    have hc' : c' = 0 := hout.elim
      (fun hlong ↦ boundaryKernel_eq_zero_of_long hp hq hqd hδ hsq hlong hk1p hdne c')
      (fun hshort ↦ boundaryKernel_eq_zero_of_short hp hq hqd hδ hsq hk hkp hshort hdne c')
    exact congrArg Subtype.val hc'
  have hdim := boundaryProduct_rank_add_rowKernel
    (p := p) (q := q) (δ := δ) (start := start)
  rw [hker] at hdim
  simpa [Nat.totient_prime hp] using hdim

/-- Exceptional-strip row relations embedded into the selected partial-map solution space. -/
def exceptionalKernelToSolution {p q δ start k s d : ℕ} [NeZero p]
    (hp : p.Prime) (hq : q.Prime) (hqd : q = p + d) (hδ : δ = k * q + s)
    (hds : d < s) (hsp : s < p) (hk : 0 < k) :
    boundaryRowKernel p q δ start →ₗ[ℂ]
      solutionSpace (exceptionalDomain p d s) (exceptionalZero p d k)
        (exceptionalMap p d s k) where
  toFun c := ⟨translatedKernelSequence c, by
    refine ⟨?_, ?_, translatedKernelSequence_sum_eq_zero hp c⟩
    · intro x hx
      by_cases hlow : x.val < s - d
      · have hedge := boundaryKernel_long_edge hp hq hqd hδ (by omega) c x.val hlow
        have hmap : exceptionalMap p d s k x =
            ((x.val + (k + 1) * d : ℕ) : ZMod p) := by
          simp only [exceptionalMap, if_pos hlow]
          push_cast
          rw [ZMod.natCast_zmod_val]
          ring
        calc
          translatedKernelSequence c (exceptionalMap p d s k x) =
              translatedKernelSequence c ((x.val + (k + 1) * d : ℕ) : ZMod p) :=
            congrArg (translatedKernelSequence c) hmap
          _ = translatedKernelSequence c (x.val : ZMod p) := hedge
          _ = translatedKernelSequence c x :=
            congrArg (translatedKernelSequence c) (ZMod.natCast_zmod_val x)
      · have hxhigh : s ≤ x.val := (mem_exceptionalDomain x).mp hx |>.resolve_left hlow
        have hedge := boundaryKernel_short_edge hp hq hqd hδ (by omega) hk c x.val
          hxhigh x.val_lt
        have hmap : exceptionalMap p d s k x =
            ((x.val + k * d : ℕ) : ZMod p) := by
          simp only [exceptionalMap, if_neg hlow]
          push_cast
          rw [ZMod.natCast_zmod_val]
          ring
        calc
          translatedKernelSequence c (exceptionalMap p d s k x) =
              translatedKernelSequence c ((x.val + k * d : ℕ) : ZMod p) :=
            congrArg (translatedKernelSequence c) hmap
          _ = translatedKernelSequence c (x.val : ZMod p) := hedge
          _ = translatedKernelSequence c x :=
            congrArg (translatedKernelSequence c) (ZMod.natCast_zmod_val x)
    · intro z hz
      rw [exceptionalZero, Finset.mem_map] at hz
      obtain ⟨r, hr, rfl⟩ := hz
      have hrlt : r.val < d := (mem_exceptionalBase r).mp hr
      have hzero := boundaryKernel_forced_zero hp hq hqd hδ hds hsp c r.val hrlt
      change translatedKernelSequence c (r + (k * d : ZMod p)) = 0
      convert hzero using 1
      push_cast
      rw [ZMod.natCast_zmod_val]
      ⟩
  map_add' c c' := by
    apply Subtype.ext
    funext r
    simp [translatedKernelSequence]
  map_smul' a c := by
    apply Subtype.ext
    funext r
    simp [translatedKernelSequence]

theorem exceptionalKernelToSolution_injective {p q δ start k s d : ℕ} [NeZero p]
    (hp : p.Prime) (hq : q.Prime) (hqd : q = p + d) (hδ : δ = k * q + s)
    (hds : d < s) (hsp : s < p) (hk : 0 < k) :
    Function.Injective (exceptionalKernelToSolution (start := start) hp hq hqd hδ hds hsp hk) := by
  intro c c' hcc'
  apply Subtype.ext
  apply rowSequenceLinear_injective hp
  funext r
  have hv := congrArg Subtype.val hcc'
  have hr := congrFun hv (r - (start : ZMod p))
  change translatedKernelSequence c (r - (start : ZMod p)) =
    translatedKernelSequence c' (r - (start : ZMod p)) at hr
  simpa only [translatedKernelSequence, kernelSequenceLinear, LinearMap.comp_apply,
    Submodule.coe_subtype, add_sub_cancel] using hr

/-- The selected partial-map equations give the exact one-third row-kernel cap. -/
theorem boundaryProduct_rank_ge_exceptional {p q δ start k s d : ℕ} [NeZero p]
    (hp : p.Prime) (hq : q.Prime) (hpodd : Odd p)
    (hqd : q = p + d) (hδ : δ = k * q + s)
    (hd : 0 < d) (hdeven : Even d) (hds : d < s) (hsp : s < p)
    (hk : 0 < k) (hkbound : 2 * k + 1 ≤ p) :
    min (p - 1) ((p + q + 2) / 3) ≤ (boundaryProduct p q δ start).rank := by
  have hpkg := exceptionalMap_package hp hpodd hd hdeven hds hsp hk hkbound
  let L := exceptionalKernelToSolution (start := start) hp hq hqd hδ hds hsp hk
  have hdimL := L.finrank_le_finrank_of_injective
    (exceptionalKernelToSolution_injective (start := start) hp hq hqd hδ hds hsp hk)
  have hdimS := finrank_solutionSpace_le hpkg.2.1 hpkg.2.2.1 hpkg.2.2.2
  have hkerle : Module.finrank ℂ (boundaryRowKernel p q δ start) ≤
      ((p - d) / 3) - 1 := by
    have := hdimL.trans hdimS
    rw [ZMod.card, hpkg.1] at this
    exact this
  have hdim := boundaryProduct_rank_add_rowKernel
    (p := p) (q := q) (δ := δ) (start := start)
  rw [Nat.totient_prime hp] at hdim
  omega

/-- Universal residual rank floor for an arbitrary shifted nearest-boundary product. -/
theorem boundaryProduct_rank_ge_residual {p q δ start : ℕ}
    (hp : p.Prime) (hq : q.Prime) (hp2 : 2 < p) (hpq : p < q)
    (hres : q - 1 < δ) (hhalf : 2 * δ ≤ p * q) :
    min (p - 1) ((p + q + 2) / 3) ≤ (boundaryProduct p q δ start).rank := by
  letI : NeZero p := ⟨hp.ne_zero⟩
  let k := δ / q
  let s := δ % q
  let d := q - p
  have hqd : q = p + d := by dsimp [d]; omega
  have hδ : δ = k * q + s := by
    dsimp [k, s]
    simpa [Nat.mul_comm] using (Nat.div_add_mod δ q).symm
  have hsq : s < q := Nat.mod_lt δ hq.pos
  have hk : 0 < k := by
    apply Nat.div_pos (b := q)
    · omega
    · exact hq.pos
  have hk2 : 2 * k ≤ p := by nlinarith
  have hpodd : Odd p := hp.odd_of_ne_two (by omega)
  have hqodd : Odd q := hq.odd_of_ne_two (by omega)
  obtain ⟨a, ha⟩ := hpodd
  obtain ⟨b, hb⟩ := hqodd
  have hkbound : 2 * k + 1 ≤ p := by omega
  have hkp : k < p := by omega
  have hk1p : k + 1 < p := by omega
  have hd : 0 < d := by dsimp [d]; omega
  have hdeven : Even d := by
    refine ⟨b - a, ?_⟩
    dsimp [d]
    omega
  have hdne : (d : ZMod p) ≠ 0 := by
    intro hzero
    have hpd : p ∣ d := (ZMod.natCast_eq_zero_iff d p).mp hzero
    have hpqdiv : p ∣ q := by
      rw [hqd]
      exact Nat.dvd_add (Nat.dvd_refl p) hpd
    have hpqe : p = q := (Nat.prime_dvd_prime_iff_eq hp hq).mp hpqdiv
    omega
  by_cases hps : p ≤ s
  · have hrank := boundaryProduct_rank_eq_full_of_outside (start := start) hp hq hqd hδ hsq hk hkp
      hk1p hdne (Or.inl hps)
    omega
  · have hsp : s < p := Nat.lt_of_not_ge hps
    by_cases hds : d < s
    · exact boundaryProduct_rank_ge_exceptional hp hq ⟨a, ha⟩ hqd hδ hd hdeven hds hsp
        hk hkbound
    · have hshort : s + p ≤ q := by omega
      have hrank := boundaryProduct_rank_eq_full_of_outside (start := start) hp hq hqd hδ hsq hk hkp
        hk1p hdne (Or.inr hshort)
      omega

/-- WI-088: every genuinely residual odd-prime cross Gram obeys the sharp universal rank floor. -/
theorem crossGram_rank_ge_residual_prime {p q N : ℕ}
    (hp : p.Prime) (hq : q.Prime) (hp2 : 2 < p) (hpq : p < q)
    (hres : q - 1 < boundaryDefect p q N) :
    min (p - 1) ((p + q + 2) / 3) ≤ (crossGram p q N).rank := by
  let ell := Nat.lcm p q
  let r := N % ell
  let δ := min r (ell - r)
  have hcop : p.Coprime q := (Nat.coprime_primes hp hq).2 (ne_of_lt hpq)
  have hell_eq : ell = p * q := by
    dsimp [ell]
    exact hcop.lcm_eq_mul
  have hellpos : 0 < ell := Nat.lcm_pos hp.pos hq.pos
  have hrlt : r < ell := Nat.mod_lt N hellpos
  have hrle : r ≤ ell := hrlt.le
  have hhalf : 2 * δ ≤ p * q := by
    have hadd : r + (ell - r) = ell := Nat.add_sub_of_le hrle
    dsimp [δ]
    rw [← hell_eq]
    by_cases hshort : r ≤ ell - r
    · rw [min_eq_left hshort]
      omega
    · rw [min_eq_right (Nat.le_of_not_ge hshort)]
      omega
  have hres' : q - 1 < δ := by
    simpa only [boundaryDefect, ell, r, δ] using hres
  rw [crossGram_eq_short_boundary hp.pos hq.pos (ne_of_lt hpq)]
  by_cases hshort : r ≤ ell - r
  · rw [ite_eq_left hshort]
    change min (p - 1) ((p + q + 2) / 3) ≤ (boundaryProduct p q δ 0).rank
    exact boundaryProduct_rank_ge_residual hp hq hp2 hpq hres' hhalf
  · rw [ite_eq_right hshort, Matrix.rank_smul_of_mem_nonZeroDivisors]
    · change min (p - 1) ((p + q + 2) / 3) ≤ (boundaryProduct p q δ r).rank
      exact boundaryProduct_rank_ge_residual hp hq hp2 hpq hres' hhalf
    · simp

#print axioms boundaryProduct_rank_ge_residual
#print axioms crossGram_rank_ge_residual_prime

end Mathia.WI088
