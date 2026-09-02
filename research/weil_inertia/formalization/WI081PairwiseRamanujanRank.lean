import Mathlib

/-!
# WI-081 pairwise Ramanujan boundary-rank sharpness

Associated finding:
`research/weil_inertia/findings/WI-081-pairwise-lcm-boundary-rank-controls-finite-window-ramanujan-leakage.md`

Formalized theorem boundary:
for distinct positive moduli, the cross Gram of the two primitive-frequency sampling matrices on
`0, ..., N - 1` has rank at most the distance from `N` to the nearest multiple of the pairwise
LCM.  When that boundary defect is at most both Euler-totient dimensions, its rank is exactly the
boundary defect.

Not formalized:
the prime maximal-mixing theorem, the close-prime rank-eight certificate, the many-family inertia
gate, the Yang--Yang source reduction, and the surrounding analytic or novelty conclusions.
-/

noncomputable section

open scoped BigOperators ComplexConjugate ComplexOrder

namespace Mathia.WI081

/-- Primitive Fourier frequencies of exact order `m`. -/
abbrev PrimitiveFrequency (m : ℕ) := ↑(primitiveRoots m ℂ)

/-- Consecutive primitive-frequency samples, with an explicit starting coordinate. -/
def shiftedSamplingMatrix (m N start : ℕ) :
    Matrix (Fin N) (PrimitiveFrequency m) ℂ :=
  fun x z ↦ (z : ℂ) ^ (start + x.val)

/-- The canonical Ramanujan/Fourier sampling matrix on coordinates `0, ..., N - 1`. -/
def samplingMatrix (m N : ℕ) : Matrix (Fin N) (PrimitiveFrequency m) ℂ :=
  shiftedSamplingMatrix m N 0

/-- The cross Gram `(U_m^(N))⁺ U_n^(N)`. -/
def crossGram (m n N : ℕ) : Matrix (PrimitiveFrequency m) (PrimitiveFrequency n) ℂ :=
  (samplingMatrix m N).conjTranspose * samplingMatrix n N

/-- Distance from `N` to the nearest multiple of `lcm(m,n)`. -/
def boundaryDefect (m n N : ℕ) : ℕ :=
  let ell := Nat.lcm m n
  let r := N % ell
  min r (ell - r)

/-- The subtype of primitive roots is exactly the reduced-frequency indexing used in WI-081. -/
theorem mem_primitiveRoots_iff_reduced_frequency {m : ℕ} (hm : 0 < m) (z : ℂ) :
    z ∈ primitiveRoots m ℂ ↔
      ∃ a < m, ∃ _ha : a.Coprime m,
        Complex.exp (2 * Real.pi * Complex.I * ((a : ℂ) / (m : ℂ))) = z := by
  rw [mem_primitiveRoots hm, Complex.isPrimitiveRoot_iff z m hm.ne']

private lemma primitive_isPrimitiveRoot {m : ℕ} (z : PrimitiveFrequency m) :
    IsPrimitiveRoot (z : ℂ) m :=
  isPrimitiveRoot_of_mem_primitiveRoots z.property

private lemma primitive_ne_zero {m : ℕ} (hm : 0 < m) (z : PrimitiveFrequency m) :
    (z : ℂ) ≠ 0 :=
  (primitive_isPrimitiveRoot z).isUnit hm.ne' |>.ne_zero

private lemma primitive_norm_eq_one {m : ℕ} (hm : 0 < m) (z : PrimitiveFrequency m) :
    ‖(z : ℂ)‖ = 1 :=
  (primitive_isPrimitiveRoot z).norm'_eq_one hm.ne'

private lemma primitive_ne_of_orders_ne {m n : ℕ} (hmn : m ≠ n)
    (z : PrimitiveFrequency m) (w : PrimitiveFrequency n) : (z : ℂ) ≠ (w : ℂ) := by
  intro h
  apply hmn
  have hz : IsPrimitiveRoot (w : ℂ) m := h ▸ primitive_isPrimitiveRoot z
  exact hz.unique (primitive_isPrimitiveRoot w)

private def crossRatio {m n : ℕ} (z : PrimitiveFrequency m) (w : PrimitiveFrequency n) : ℂ :=
  (z : ℂ)⁻¹ * (w : ℂ)

private lemma crossRatio_ne_one {m n : ℕ} (hm : 0 < m) (hmn : m ≠ n)
    (z : PrimitiveFrequency m) (w : PrimitiveFrequency n) : crossRatio z w ≠ 1 := by
  intro h
  exact primitive_ne_of_orders_ne hmn z w
    ((inv_mul_eq_one₀ (primitive_ne_zero hm z)).mp h)

private lemma crossRatio_pow_lcm {m n : ℕ} (_hm : 0 < m) (_hn : 0 < n)
    (z : PrimitiveFrequency m) (w : PrimitiveFrequency n) :
    crossRatio z w ^ Nat.lcm m n = 1 := by
  have hz : (z : ℂ) ^ Nat.lcm m n = 1 :=
    ((primitive_isPrimitiveRoot z).pow_eq_one_iff_dvd _).2 (Nat.dvd_lcm_left m n)
  have hw : (w : ℂ) ^ Nat.lcm m n = 1 :=
    ((primitive_isPrimitiveRoot w).pow_eq_one_iff_dvd _).2 (Nat.dvd_lcm_right m n)
  simp [crossRatio, mul_pow, hz, hw]

private lemma crossRatio_pow_mod_lcm {m n N : ℕ} (hm : 0 < m) (hn : 0 < n)
    (z : PrimitiveFrequency m) (w : PrimitiveFrequency n) :
    crossRatio z w ^ N = crossRatio z w ^ (N % Nat.lcm m n) := by
  let ell := Nat.lcm m n
  have hell : crossRatio z w ^ ell = 1 := crossRatio_pow_lcm hm hn z w
  calc
    crossRatio z w ^ N =
        crossRatio z w ^ (N % ell + ell * (N / ell)) := by
          rw [Nat.mod_add_div N ell]
    _ = crossRatio z w ^ (N % ell) * (crossRatio z w ^ ell) ^ (N / ell) := by
          rw [pow_add, pow_mul]
    _ = crossRatio z w ^ (N % ell) := by simp [hell]

private lemma geometric_sum_remainder {m n N : ℕ} (hm : 0 < m) (hn : 0 < n)
    (hmn : m ≠ n) (z : PrimitiveFrequency m) (w : PrimitiveFrequency n) :
    (∑ x ∈ Finset.range N, crossRatio z w ^ x) =
      ∑ x ∈ Finset.range (N % Nat.lcm m n), crossRatio z w ^ x := by
  rw [geom_sum_eq (crossRatio_ne_one hm hmn z w),
    geom_sum_eq (crossRatio_ne_one hm hmn z w), crossRatio_pow_mod_lcm hm hn]

private lemma geometric_sum_full_period {m n : ℕ} (hm : 0 < m) (hn : 0 < n)
    (hmn : m ≠ n) (z : PrimitiveFrequency m) (w : PrimitiveFrequency n) :
    (∑ x ∈ Finset.range (Nat.lcm m n), crossRatio z w ^ x) = 0 := by
  rw [geom_sum_eq (crossRatio_ne_one hm hmn z w), crossRatio_pow_lcm hm hn]
  simp

private lemma crossGram_apply {m n N : ℕ} (hm : 0 < m)
    (z : PrimitiveFrequency m) (w : PrimitiveFrequency n) :
    crossGram m n N z w = ∑ x ∈ Finset.range N, crossRatio z w ^ x := by
  classical
  simp only [crossGram, samplingMatrix, shiftedSamplingMatrix, Matrix.mul_apply,
    Matrix.conjTranspose_apply, star_pow, zero_add]
  rw [← Fin.sum_univ_eq_sum_range]
  apply Finset.sum_congr rfl
  intro x hx
  rw [show star (z : ℂ) = (z : ℂ)⁻¹ by
    symm
    exact Complex.inv_eq_conj (primitive_norm_eq_one hm z)]
  simp [crossRatio, mul_pow]

private lemma shifted_boundary_product_apply {m n d start : ℕ} (hm : 0 < m)
    (z : PrimitiveFrequency m) (w : PrimitiveFrequency n) :
    ((shiftedSamplingMatrix m d start).conjTranspose *
        shiftedSamplingMatrix n d start) z w =
      ∑ x ∈ Finset.range d, crossRatio z w ^ (start + x) := by
  classical
  simp only [shiftedSamplingMatrix, Matrix.mul_apply, Matrix.conjTranspose_apply, star_pow]
  rw [← Fin.sum_univ_eq_sum_range]
  apply Finset.sum_congr rfl
  intro x hx
  rw [show star (z : ℂ) = (z : ℂ)⁻¹ by
    symm
    exact Complex.inv_eq_conj (primitive_norm_eq_one hm z)]
  simp [crossRatio, mul_pow]

private lemma crossGram_eq_remainder {m n N : ℕ} (hm : 0 < m) (hn : 0 < n)
    (hmn : m ≠ n) :
    crossGram m n N = crossGram m n (N % Nat.lcm m n) := by
  ext z w
  rw [crossGram_apply hm, crossGram_apply hm]
  exact geometric_sum_remainder hm hn hmn z w

lemma crossGram_eq_short_boundary {m n N : ℕ} (hm : 0 < m) (hn : 0 < n)
    (hmn : m ≠ n) :
    let ell := Nat.lcm m n
    let r := N % ell
    let d := min r (ell - r)
    crossGram m n N =
      if r ≤ ell - r then
        (shiftedSamplingMatrix m d 0).conjTranspose * shiftedSamplingMatrix n d 0
      else
        (-1 : ℂ) •
          ((shiftedSamplingMatrix m d r).conjTranspose * shiftedSamplingMatrix n d r) := by
  classical
  dsimp only
  let ell := Nat.lcm m n
  let r := N % ell
  have hell : 0 < ell := Nat.lcm_pos hm hn
  have hrlt : r < ell := Nat.mod_lt N hell
  have hrle : r ≤ ell := hrlt.le
  by_cases hshort : r ≤ ell - r
  · rw [ite_eq_left hshort, min_eq_left hshort]
    ext z w
    rw [crossGram_apply hm, shifted_boundary_product_apply hm]
    simpa [r, ell] using geometric_sum_remainder hm hn hmn z w
  · rw [ite_eq_right hshort, min_eq_right (Nat.le_of_not_ge hshort)]
    ext z w
    rw [crossGram_apply hm, Matrix.smul_apply, shifted_boundary_product_apply hm]
    have hrem := geometric_sum_remainder (N := N) hm hn hmn z w
    have hfull := geometric_sum_full_period hm hn hmn z w
    have hsplit := Finset.sum_range_add
      (fun x : ℕ ↦ crossRatio z w ^ x) r (ell - r)
    have hradd : r + (ell - r) = ell := Nat.add_sub_of_le hrle
    have hzero :
        (∑ x ∈ Finset.range r, crossRatio z w ^ x) +
          (∑ x ∈ Finset.range (ell - r), crossRatio z w ^ (r + x)) = 0 := by
      rw [← hsplit, hradd]
      exact hfull
    rw [hrem]
    simp only [neg_smul, one_smul]
    exact (eq_neg_iff_add_eq_zero).2 hzero

lemma primitiveFrequency_card (m : ℕ) :
    Fintype.card (PrimitiveFrequency m) = Nat.totient m := by
  rw [Fintype.card_coe, Complex.card_primitiveRoots]

lemma shiftedSamplingMatrix_rows_linearIndependent {m d start : ℕ}
    (hm : 0 < m) (hd : d ≤ Nat.totient m) :
    LinearIndependent ℂ (shiftedSamplingMatrix m d start).row := by
  classical
  have hcard : d ≤ Fintype.card (PrimitiveFrequency m) := by
    rw [primitiveFrequency_card]
    exact hd
  let e : Fin d ↪ PrimitiveFrequency m :=
    (Fin.castLEEmb hcard).trans
      (Fintype.equivFin (PrimitiveFrequency m)).symm.toEmbedding
  have heval : Function.Injective (fun i : Fin d ↦ ((e i : PrimitiveFrequency m) : ℂ)) := by
    intro i j hij
    exact e.injective (Subtype.ext hij)
  rw [Fintype.linearIndependent_iff]
  intro c hc
  have hpoly : ∀ j : Fin d,
      (∑ i : Fin d, c i * ((e j : PrimitiveFrequency m) : ℂ) ^ (i : ℕ)) = 0 := by
    intro j
    have hj := congr_fun hc (e j)
    simp only [Finset.sum_apply, Pi.smul_apply, smul_eq_mul, Matrix.row_apply,
      shiftedSamplingMatrix, Pi.zero_apply] at hj
    have hfactor :
        ((e j : PrimitiveFrequency m) : ℂ) ^ start *
            (∑ i : Fin d, c i * ((e j : PrimitiveFrequency m) : ℂ) ^ (i : ℕ)) = 0 := by
      rw [Finset.mul_sum]
      calc
        (∑ i : Fin d,
            ((e j : PrimitiveFrequency m) : ℂ) ^ start *
              (c i * ((e j : PrimitiveFrequency m) : ℂ) ^ (i : ℕ))) =
            ∑ i : Fin d,
              c i * ((e j : PrimitiveFrequency m) : ℂ) ^ (start + (i : ℕ)) := by
                apply Finset.sum_congr rfl
                intro i hi
                rw [pow_add]
                ring
        _ = 0 := hj
    exact (mul_eq_zero.mp hfactor).resolve_left
      (pow_ne_zero _ (primitive_ne_zero hm (e j)))
  exact fun i ↦ congr_fun
    (Matrix.eq_zero_of_forall_index_sum_mul_pow_eq_zero heval hpoly) i

private lemma shiftedSamplingMatrix_rank {m d start : ℕ}
    (hm : 0 < m) (hd : d ≤ Nat.totient m) :
    (shiftedSamplingMatrix m d start).rank = d := by
  simpa using (shiftedSamplingMatrix_rows_linearIndependent hm hd).rank_matrix

private lemma shiftedSamplingMatrix_rank_min {m d start : ℕ} (hm : 0 < m) :
    (shiftedSamplingMatrix m d start).rank = min d (Nat.totient m) := by
  by_cases hd : d ≤ Nat.totient m
  · rw [min_eq_left hd, shiftedSamplingMatrix_rank hm hd]
  · have htot : Nat.totient m ≤ d := Nat.le_of_not_ge hd
    rw [min_eq_right htot]
    apply le_antisymm
    · have hrank := Matrix.rank_le_card_width (shiftedSamplingMatrix m d start)
      rw [primitiveFrequency_card] at hrank
      exact hrank
    · have hsub := Matrix.rank_submatrix_le (shiftedSamplingMatrix m d start)
          (Fin.castLE htot) (Equiv.refl (PrimitiveFrequency m))
      have hsubmatrix :
          (shiftedSamplingMatrix m d start).submatrix (Fin.castLE htot)
              (Equiv.refl (PrimitiveFrequency m)) =
            shiftedSamplingMatrix m (Nat.totient m) start := by
        ext i z
        rfl
      rw [hsubmatrix, shiftedSamplingMatrix_rank hm le_rfl] at hsub
      exact hsub

private lemma shiftedSamplingMatrix_surjective {m d start : ℕ}
    (hm : 0 < m) (hd : d ≤ Nat.totient m) :
    Function.Surjective (shiftedSamplingMatrix m d start).mulVec := by
  change Function.Surjective (shiftedSamplingMatrix m d start).mulVecLin
  rw [← LinearMap.range_eq_top]
  apply Submodule.eq_top_of_finrank_eq
  rw [← Matrix.rank, shiftedSamplingMatrix_rank hm hd,
    Module.finrank_fintype_fun_eq_card, Fintype.card_fin]

private lemma shifted_boundary_product_rank_of_right_surjective {m n d start : ℕ}
    (hm : 0 < m) (hn : 0 < n) (hdn : d ≤ Nat.totient n) :
    ((shiftedSamplingMatrix m d start).conjTranspose *
        shiftedSamplingMatrix n d start).rank = min d (Nat.totient m) := by
  rw [Matrix.rank, Matrix.mulVecLin_mul,
    LinearMap.range_comp_of_range_eq_top _
      (LinearMap.range_eq_top.mpr (shiftedSamplingMatrix_surjective hn hdn)),
    ← Matrix.rank, Matrix.rank_conjTranspose, shiftedSamplingMatrix_rank_min hm]

private lemma shiftedSamplingMatrix_conjTranspose_injective {m d start : ℕ}
    (hm : 0 < m) (hd : d ≤ Nat.totient m) :
    Function.Injective (shiftedSamplingMatrix m d start).conjTranspose.mulVec := by
  classical
  change Function.Injective (shiftedSamplingMatrix m d start).conjTranspose.mulVecLin
  rw [← LinearMap.ker_eq_bot]
  rw [← Submodule.finrank_eq_zero]
  have hdim := LinearMap.finrank_range_add_finrank_ker
    (shiftedSamplingMatrix m d start).conjTranspose.mulVecLin
  have hrank : (shiftedSamplingMatrix m d start).conjTranspose.rank = d := by
    rw [Matrix.rank_conjTranspose, shiftedSamplingMatrix_rank hm hd]
  rw [← Matrix.rank, hrank, Module.finrank_fintype_fun_eq_card, Fintype.card_fin] at hdim
  omega

private lemma shifted_boundary_product_rank {m n d start : ℕ}
    (hm : 0 < m) (hn : 0 < n) (hdm : d ≤ Nat.totient m)
    (hdn : d ≤ Nat.totient n) :
    ((shiftedSamplingMatrix m d start).conjTranspose *
        shiftedSamplingMatrix n d start).rank = d := by
  rw [Matrix.rank, Matrix.mulVecLin_mul,
    LinearMap.range_comp_of_range_eq_top _
      (LinearMap.range_eq_top.mpr (shiftedSamplingMatrix_surjective hn hdn)),
    LinearMap.finrank_range_of_inj (shiftedSamplingMatrix_conjTranspose_injective hm hdm),
    Module.finrank_fintype_fun_eq_card, Fintype.card_fin]

private lemma shifted_boundary_product_rank_of_le_max_totient {m n d start : ℕ}
    (hm : 0 < m) (hn : 0 < n)
    (hd : d ≤ max (Nat.totient m) (Nat.totient n)) :
    ((shiftedSamplingMatrix m d start).conjTranspose *
        shiftedSamplingMatrix n d start).rank =
      min d (min (Nat.totient m) (Nat.totient n)) := by
  by_cases hmn : Nat.totient m ≤ Nat.totient n
  · have hdn : d ≤ Nat.totient n := by
      simpa [max_eq_right hmn] using hd
    simpa [min_eq_left hmn] using
      shifted_boundary_product_rank_of_right_surjective hm hn hdn
  · have hnm : Nat.totient n ≤ Nat.totient m := Nat.le_of_not_ge hmn
    have hdm : d ≤ Nat.totient m := by
      simpa [max_eq_left hnm] using hd
    calc
      ((shiftedSamplingMatrix m d start).conjTranspose *
          shiftedSamplingMatrix n d start).rank =
          (((shiftedSamplingMatrix m d start).conjTranspose *
            shiftedSamplingMatrix n d start).conjTranspose).rank :=
        (Matrix.rank_conjTranspose _).symm
      _ = ((shiftedSamplingMatrix n d start).conjTranspose *
            shiftedSamplingMatrix m d start).rank := by
        rw [Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose]
      _ = min d (Nat.totient n) :=
        shifted_boundary_product_rank_of_right_surjective hn hm hdm
      _ = min d (min (Nat.totient m) (Nat.totient n)) := by
        rw [min_eq_right hnm]

/-- The pairwise cross Gram is supported on at most the nearest-period boundary coordinates. -/
theorem crossGram_rank_le {m n N : ℕ} (hm : 0 < m) (hn : 0 < n) (hmn : m ≠ n) :
    (crossGram m n N).rank ≤ boundaryDefect m n N := by
  classical
  rw [crossGram_eq_short_boundary hm hn hmn]
  simp only [boundaryDefect]
  let ell := Nat.lcm m n
  let r := N % ell
  let d := min r (ell - r)
  by_cases hshort : r ≤ ell - r
  · rw [ite_eq_left hshort]
    change ((shiftedSamplingMatrix m d 0).conjTranspose *
      shiftedSamplingMatrix n d 0).rank ≤ d
    exact (Matrix.rank_mul_le_left _ _).trans (by
      simpa using Matrix.rank_le_card_width
        (shiftedSamplingMatrix m d 0).conjTranspose)
  · rw [ite_eq_right hshort, Matrix.rank_smul_of_mem_nonZeroDivisors]
    · change ((shiftedSamplingMatrix m d r).conjTranspose *
        shiftedSamplingMatrix n d r).rank ≤ d
      exact (Matrix.rank_mul_le_left _ _).trans (by
        simpa using Matrix.rank_le_card_width
          (shiftedSamplingMatrix m d r).conjTranspose)
    · simp

/-- In the small-boundary regime the nearest-period rank upper bound is exact. -/
theorem crossGram_rank_eq_of_boundaryDefect_le_totient {m n N : ℕ}
    (hm : 0 < m) (hn : 0 < n) (hmn : m ≠ n)
    (hδ : boundaryDefect m n N ≤ min (Nat.totient m) (Nat.totient n)) :
    (crossGram m n N).rank = boundaryDefect m n N := by
  classical
  have hdm : boundaryDefect m n N ≤ Nat.totient m := hδ.trans (min_le_left _ _)
  have hdn : boundaryDefect m n N ≤ Nat.totient n := hδ.trans (min_le_right _ _)
  rw [crossGram_eq_short_boundary hm hn hmn]
  simp only [boundaryDefect]
  let ell := Nat.lcm m n
  let r := N % ell
  let d := min r (ell - r)
  change d ≤ Nat.totient m at hdm
  change d ≤ Nat.totient n at hdn
  by_cases hshort : r ≤ ell - r
  · rw [ite_eq_left hshort, shifted_boundary_product_rank hm hn hdm hdn]
  · rw [ite_eq_right hshort, Matrix.rank_smul_of_mem_nonZeroDivisors,
      shifted_boundary_product_rank hm hn hdm hdn]
    simp

/-!
## WI-086 strengthened max-totient threshold

Associated finding:
`research/weil_inertia/findings/WI-086-pairwise-ramanujan-rank-defect-starts-past-both-totient-dimensions.md`

The theorem below formalizes only the strengthened pairwise statement that the cross Gram has
maximal possible rank while the nearest-period boundary defect is at most the larger Euler-totient
dimension.  It does not formalize WI-086's residual transversality/cyclotomic analysis or any
surrounding Yang or zeta conclusion.
-/

/-- Up to the larger totient dimension, the pairwise cross Gram has maximal possible rank. -/
theorem crossGram_rank_eq_of_boundaryDefect_le_max_totient {m n N : ℕ}
    (hm : 0 < m) (hn : 0 < n) (hmn : m ≠ n)
    (hδ : boundaryDefect m n N ≤ max (Nat.totient m) (Nat.totient n)) :
    (crossGram m n N).rank =
      min (boundaryDefect m n N) (min (Nat.totient m) (Nat.totient n)) := by
  classical
  rw [crossGram_eq_short_boundary hm hn hmn]
  simp only [boundaryDefect]
  let ell := Nat.lcm m n
  let r := N % ell
  let d := min r (ell - r)
  change d ≤ max (Nat.totient m) (Nat.totient n) at hδ
  by_cases hshort : r ≤ ell - r
  · rw [ite_eq_left hshort,
      shifted_boundary_product_rank_of_le_max_totient hm hn hδ]
  · rw [ite_eq_right hshort, Matrix.rank_smul_of_mem_nonZeroDivisors,
      shifted_boundary_product_rank_of_le_max_totient hm hn hδ]
    simp

#print axioms crossGram_rank_le
#print axioms crossGram_rank_eq_of_boundaryDefect_le_totient
#print axioms crossGram_rank_eq_of_boundaryDefect_le_max_totient

end Mathia.WI081
