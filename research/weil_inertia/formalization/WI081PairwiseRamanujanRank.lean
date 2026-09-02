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

/-!
## WI-087 close-prime Loewner--Bezout rank family

Associated finding:
`research/weil_inertia/findings/WI-087-close-prime-ramanujan-cross-grams-have-an-exact-loewner-bezout-rank-family.md`

The theorem below formalizes the exact cross-Gram rank on the close-prime congruence family.  Its
proof makes the finite Loewner coefficient matrix and its cyclic three-term kernel recurrence
explicit.  It does not formalize prime-distribution or asymptotic existence claims, the wider
many-family inertia mechanism, the Yang--Yang reduction, or any zeta-function conclusion.
-/

private def wi087PowerEval (b : ℕ) {I : Type*} (x : I → ℂ) : Matrix I (Fin b) ℂ :=
  fun i j ↦ x i ^ (j : ℕ)

private def wi087EvalKernel (b : ℕ) (B : Matrix (Fin b) (Fin b) ℂ) (x y : ℂ) : ℂ :=
  ∑ i : Fin b, ∑ j : Fin b, B i j * x ^ (i : ℕ) * y ^ (j : ℕ)

private lemma wi087_powerEval_mul_apply {b : ℕ} {I J : Type*}
    (x : I → ℂ) (y : J → ℂ) (B : Matrix (Fin b) (Fin b) ℂ) (i : I) (j : J) :
    (wi087PowerEval b x * B * (wi087PowerEval b y).transpose) i j =
      wi087EvalKernel b B (x i) (y j) := by
  simp only [wi087PowerEval, wi087EvalKernel, Matrix.mul_apply, Matrix.transpose_apply]
  simp_rw [Finset.sum_mul]
  rw [Finset.sum_comm]
  simp only [mul_assoc, mul_comm]

private lemma wi087_powerEval_mulVec_injective {b : ℕ} {I : Type*} [Fintype I]
    (x : I → ℂ) (e : Fin b → I) (he : Function.Injective (x ∘ e)) :
    Function.Injective (wi087PowerEval b x).mulVec := by
  intro c d hcd
  have hpoly : ∀ j : Fin b,
      (∑ i : Fin b, (c i - d i) * (x (e j)) ^ (i : ℕ)) = 0 := by
    intro j
    have hj := congr_fun hcd (e j)
    simp only [wi087PowerEval, Matrix.mulVec, dotProduct] at hj
    calc
      (∑ i : Fin b, (c i - d i) * (x (e j)) ^ (i : ℕ)) =
          ∑ i : Fin b,
            ((x (e j)) ^ (i : ℕ) * c i - (x (e j)) ^ (i : ℕ) * d i) := by
            apply Finset.sum_congr rfl
            intro i hi
            ring
      _ = (∑ i : Fin b, (x (e j)) ^ (i : ℕ) * c i) -
          ∑ i : Fin b, (x (e j)) ^ (i : ℕ) * d i := by
            rw [Finset.sum_sub_distrib]
      _ = 0 := sub_eq_zero.mpr hj
  have hz := Matrix.eq_zero_of_forall_index_sum_mul_pow_eq_zero he hpoly
  funext i
  exact sub_eq_zero.mp (congr_fun hz i)

private lemma wi087_powerEval_transpose_mulVec_surjective {b : ℕ} {J : Type*} [Fintype J]
    (y : J → ℂ) (e : Fin b → J) (he : Function.Injective (y ∘ e)) :
    Function.Surjective (wi087PowerEval b y).transpose.mulVec := by
  change Function.Surjective (wi087PowerEval b y).transpose.mulVecLin
  rw [← LinearMap.range_eq_top]
  apply Submodule.eq_top_of_finrank_eq
  change (wi087PowerEval b y).transpose.rank = Module.finrank ℂ (Fin b → ℂ)
  rw [Matrix.rank_transpose, Matrix.rank,
    LinearMap.finrank_range_of_inj (wi087_powerEval_mulVec_injective y e he),
    Module.finrank_fintype_fun_eq_card, Fintype.card_fin]

private theorem wi087_rank_diagonal_powerEval_mul_of_injective
    {b : ℕ} {I J : Type*} [Fintype I] [Fintype J]
    [DecidableEq I] [DecidableEq J] [DecidableEq (Fin b)]
    (x : I → ℂ) (y : J → ℂ) (B : Matrix (Fin b) (Fin b) ℂ)
    (leftScale : I → ℂ) (rightScale : J → ℂ)
    (ex : Fin b → I) (ey : Fin b → J)
    (hx : Function.Injective (x ∘ ex)) (hy : Function.Injective (y ∘ ey))
    (hB : Function.Injective B.mulVec)
    (hleft : ∀ i, leftScale i ≠ 0) (hright : ∀ j, rightScale j ≠ 0) :
    (Matrix.diagonal leftScale * (wi087PowerEval b x * B *
        (wi087PowerEval b y).transpose) * Matrix.diagonal rightScale).rank = b := by
  have hldet : (Matrix.diagonal leftScale).det ≠ 0 := by
    rw [Matrix.det_diagonal]
    exact Finset.prod_ne_zero_iff.mpr (fun i hi ↦ hleft i)
  have hrdet : (Matrix.diagonal rightScale).det ≠ 0 := by
    rw [Matrix.det_diagonal]
    exact Finset.prod_ne_zero_iff.mpr (fun j hj ↦ hright j)
  rw [Matrix.rank_mul_eq_left_of_det_ne_zero _ _ hrdet,
    Matrix.rank_mul_eq_right_of_det_ne_zero _ _ hldet, Matrix.rank,
    Matrix.mulVecLin_mul, Matrix.mulVecLin_mul,
    LinearMap.range_comp_of_range_eq_top _
      (LinearMap.range_eq_top.mpr (wi087_powerEval_transpose_mulVec_surjective y ey hy)),
    LinearMap.finrank_range_of_inj]
  · simp
  · exact (wi087_powerEval_mulVec_injective x ex hx).comp hB

private def wi087PowerDiffMatrix (d u v : ℕ) (huv : u < v) (hvd : v ≤ d) :
    Matrix (Fin d) (Fin d) ℂ :=
  ∑ k : Fin (v - u), Matrix.single
    ⟨u + (k : ℕ), by omega⟩
    ⟨v - 1 - (k : ℕ), by omega⟩ 1

private lemma wi087_powerDiffMatrix_eval (d u v : ℕ) (huv : u < v) (hvd : v ≤ d)
    (z w : ℂ) :
    wi087EvalKernel d (wi087PowerDiffMatrix d u v huv hvd) z w =
      ∑ k : Fin (v - u), z ^ (u + (k : ℕ)) * w ^ (v - 1 - (k : ℕ)) := by
  calc
    wi087EvalKernel d (wi087PowerDiffMatrix d u v huv hvd) z w =
        ((wi087PowerEval d (fun _ : Unit ↦ z)) *
          wi087PowerDiffMatrix d u v huv hvd *
          (wi087PowerEval d (fun _ : Unit ↦ w)).transpose) () () := by
            simpa using (wi087_powerEval_mul_apply
              (fun _ : Unit ↦ z) (fun _ : Unit ↦ w)
              (wi087PowerDiffMatrix d u v huv hvd) () ()).symm
    _ = _ := by
      rw [wi087PowerDiffMatrix, Matrix.mul_sum, Matrix.sum_mul]
      simp only [Matrix.sum_apply]
      apply Finset.sum_congr rfl
      intro k hk
      let i₀ : Fin d := ⟨u + (k : ℕ), by omega⟩
      let j₀ : Fin d := ⟨v - 1 - (k : ℕ), by omega⟩
      change (((wi087PowerEval d (fun _ : Unit ↦ z)) *
          Matrix.single i₀ j₀ (1 : ℂ)) *
          (wi087PowerEval d (fun _ : Unit ↦ w)).transpose) () () = _
      rw [Matrix.mul_apply, Finset.sum_eq_single j₀]
      · simp [i₀, j₀, wi087PowerEval]
      · intro j hj hne
        rw [Matrix.mul_single_apply_of_ne]
        · simp
        · exact hne
      · simp

private lemma wi087_shifted_geom_sum (u n : ℕ) (hn : 0 < n) (z w : ℂ) :
    (∑ k : Fin n, z ^ (u + (k : ℕ)) * w ^ (u + n - 1 - (k : ℕ))) * (z - w) =
      z ^ (u + n) * w ^ u - z ^ u * w ^ (u + n) := by
  rw [Fin.sum_univ_eq_sum_range
    (fun k : ℕ ↦ z ^ (u + k) * w ^ (u + n - 1 - k))]
  calc
    (∑ k ∈ Finset.range n, z ^ (u + k) * w ^ (u + n - 1 - k)) * (z - w) =
        (z ^ u * w ^ u) *
          ((∑ k ∈ Finset.range n, z ^ k * w ^ (n - 1 - k)) * (z - w)) := by
            rw [← mul_assoc]
            congr 1
            rw [Finset.mul_sum]
            apply Finset.sum_congr rfl
            intro k hk
            have hkn : k < n := Finset.mem_range.mp hk
            rw [show u + n - 1 - k = u + (n - 1 - k) by omega, pow_add, pow_add]
            ring
    _ = (z ^ u * w ^ u) * (z ^ n - w ^ n) := by rw [geom_sum₂_mul]
    _ = z ^ (u + n) * w ^ u - z ^ u * w ^ (u + n) := by
      rw [pow_add, pow_add]
      ring

private lemma wi087_powerDiffMatrix_mul_sub (d u v : ℕ) (huv : u < v) (hvd : v ≤ d)
    (z w : ℂ) :
    wi087EvalKernel d (wi087PowerDiffMatrix d u v huv hvd) z w * (z - w) =
      z ^ v * w ^ u - z ^ u * w ^ v := by
  rw [wi087_powerDiffMatrix_eval]
  have huv' : u + (v - u) = v := Nat.add_sub_of_le huv.le
  simpa [huv'] using wi087_shifted_geom_sum u (v - u) (by omega) z w

private def wi087P (a g : ℕ) (z : ℂ) : ℂ := 1 + z ^ a + z ^ (a + g)

private def wi087Q (a g : ℕ) (z : ℂ) : ℂ := 1 + z ^ g + z ^ (a + g)

private def wi087CoefficientMatrix (a g : ℕ) (ha : 0 < a) (hag : a < g) :
    Matrix (Fin (a + g)) (Fin (a + g)) ℂ :=
  wi087PowerDiffMatrix (a + g) 0 a ha (by omega) -
  wi087PowerDiffMatrix (a + g) 0 g (by omega) (by omega) -
  wi087PowerDiffMatrix (a + g) a g hag (by omega) -
  wi087PowerDiffMatrix (a + g) a (a + g) (by omega) le_rfl +
  wi087PowerDiffMatrix (a + g) g (a + g) (by omega) le_rfl

private lemma wi087_coefficientMatrix_mul_sub (a g : ℕ) (ha : 0 < a) (hag : a < g)
    (z w : ℂ) :
    wi087EvalKernel (a + g) (wi087CoefficientMatrix a g ha hag) z w * (z - w) =
      wi087P a g z * wi087Q a g w - wi087Q a g z * wi087P a g w := by
  calc
    wi087EvalKernel (a + g) (wi087CoefficientMatrix a g ha hag) z w * (z - w) =
        (((wi087PowerEval (a + g) (fun _ : Unit ↦ z)) *
          wi087CoefficientMatrix a g ha hag *
          (wi087PowerEval (a + g) (fun _ : Unit ↦ w)).transpose) () ()) *
            (z - w) := by
              rw [wi087_powerEval_mul_apply]
    _ = _ := by
      simp only [wi087CoefficientMatrix, Matrix.mul_add, Matrix.mul_sub,
        Matrix.add_mul, Matrix.sub_mul, Matrix.add_apply, Matrix.sub_apply]
      rw [add_mul, sub_mul, sub_mul, sub_mul]
      simp_rw [wi087_powerEval_mul_apply, wi087_powerDiffMatrix_mul_sub]
      simp only [wi087P, wi087Q, pow_zero, mul_one]
      ring

private lemma wi087_powerDiffMatrix_mulVec_sum (d u v : ℕ) (huv : u < v)
    (hvd : v ≤ d) (x : Fin d → ℂ) (r : Fin d) :
    (wi087PowerDiffMatrix d u v huv hvd).mulVec x r =
      ∑ k : Fin (v - u), if r = ⟨u + (k : ℕ), by omega⟩ then
        x ⟨v - 1 - (k : ℕ), by omega⟩ else 0 := by
  simp [wi087PowerDiffMatrix, Matrix.sum_mulVec, Matrix.single_mulVec,
    Function.update_apply]

private lemma wi087_powerDiffMatrix_mulVec_of_mem (d u v : ℕ) (huv : u < v)
    (hvd : v ≤ d) (x : Fin d → ℂ) (r : ℕ) (hrd : r < d) (hur : u ≤ r)
    (hrv : r < v) :
    (wi087PowerDiffMatrix d u v huv hvd).mulVec x ⟨r, hrd⟩ =
      x ⟨v - 1 - (r - u), by omega⟩ := by
  rw [wi087_powerDiffMatrix_mulVec_sum]
  let k₀ : Fin (v - u) := ⟨r - u, by omega⟩
  rw [Finset.sum_eq_single k₀]
  · simp only [k₀]
    split
    · rfl
    · rename_i hne
      exfalso
      apply hne
      apply Fin.ext
      simp
      omega
  · intro k hk hne
    simp only [Finset.mem_univ, ite_eq_right_iff]
    intro hrk
    exfalso
    apply hne
    apply Fin.ext
    change (k : ℕ) = r - u
    have hval := congrArg Fin.val hrk
    simp only [Fin.val_mk] at hval
    omega
  · simp

private lemma wi087_powerDiffMatrix_mulVec_of_lt (d u v : ℕ) (huv : u < v)
    (hvd : v ≤ d) (x : Fin d → ℂ) (r : ℕ) (hrd : r < d) (hru : r < u) :
    (wi087PowerDiffMatrix d u v huv hvd).mulVec x ⟨r, hrd⟩ = 0 := by
  rw [wi087_powerDiffMatrix_mulVec_sum]
  apply Finset.sum_eq_zero
  intro k hk
  simp only [ite_eq_right_iff]
  intro hrk
  have := congrArg Fin.val hrk
  simp at this
  omega

private lemma wi087_powerDiffMatrix_mulVec_of_ge (d u v : ℕ) (huv : u < v)
    (hvd : v ≤ d) (x : Fin d → ℂ) (r : ℕ) (hrd : r < d) (hvr : v ≤ r) :
    (wi087PowerDiffMatrix d u v huv hvd).mulVec x ⟨r, hrd⟩ = 0 := by
  rw [wi087_powerDiffMatrix_mulVec_sum]
  apply Finset.sum_eq_zero
  intro k hk
  simp only [ite_eq_right_iff]
  intro hrk
  have := congrArg Fin.val hrk
  simp at this
  have hklt := k.isLt
  omega

private def wi087RevVec (a g : ℕ) (x : Fin (a + g) → ℂ) : Fin (a + g) → ℂ :=
  fun r ↦ x ⟨a + g - 1 - (r : ℕ), by omega⟩

private lemma wi087_kernel_left {a g : ℕ} (ha : 0 < a) (hag : a < g)
    (x : Fin (a + g) → ℂ) (hx : (wi087CoefficientMatrix a g ha hag).mulVec x = 0)
    (r : ℕ) (hr : r < a) :
    wi087RevVec a g x ⟨r + g, by omega⟩ = wi087RevVec a g x ⟨r + a, by omega⟩ := by
  have hrow := congr_fun hx (⟨r, by omega⟩ : Fin (a + g))
  simp only [wi087CoefficientMatrix, Matrix.add_mulVec, Matrix.sub_mulVec, Pi.add_apply,
    Pi.sub_apply, Pi.zero_apply] at hrow
  rw [wi087_powerDiffMatrix_mulVec_of_mem, wi087_powerDiffMatrix_mulVec_of_mem,
    wi087_powerDiffMatrix_mulVec_of_lt, wi087_powerDiffMatrix_mulVec_of_lt,
    wi087_powerDiffMatrix_mulVec_of_lt] at hrow
  · unfold wi087RevVec
    have hleft : (⟨a + g - 1 - (r + g), by omega⟩ : Fin (a + g)) =
        ⟨a - 1 - r, by omega⟩ := by apply Fin.ext; simp; omega
    have hright : (⟨a + g - 1 - (r + a), by omega⟩ : Fin (a + g)) =
        ⟨g - 1 - r, by omega⟩ := by apply Fin.ext; simp; omega
    rw [hleft, hright]
    linear_combination hrow
  all_goals omega

private lemma wi087_kernel_middle {a g : ℕ} (ha : 0 < a) (hag : a < g)
    (x : Fin (a + g) → ℂ) (hx : (wi087CoefficientMatrix a g ha hag).mulVec x = 0)
    (r : ℕ) (har : a ≤ r) (hrg : r < g) :
    wi087RevVec a g x ⟨r + a, by omega⟩ + wi087RevVec a g x ⟨r, by omega⟩ +
        wi087RevVec a g x ⟨r - a, by omega⟩ = 0 := by
  have hrow := congr_fun hx (⟨r, by omega⟩ : Fin (a + g))
  simp only [wi087CoefficientMatrix, Matrix.add_mulVec, Matrix.sub_mulVec, Pi.add_apply,
    Pi.sub_apply, Pi.zero_apply] at hrow
  rw [wi087_powerDiffMatrix_mulVec_of_ge, wi087_powerDiffMatrix_mulVec_of_mem,
    wi087_powerDiffMatrix_mulVec_of_mem, wi087_powerDiffMatrix_mulVec_of_mem,
    wi087_powerDiffMatrix_mulVec_of_lt] at hrow
  · unfold wi087RevVec
    have hfirst : (⟨a + g - 1 - (r + a), by omega⟩ : Fin (a + g)) =
        ⟨g - 1 - r, by omega⟩ := by apply Fin.ext; simp; omega
    have hsecond : (⟨g - 1 - (r - a), by omega⟩ : Fin (a + g)) =
        ⟨a + g - 1 - r, by omega⟩ := by apply Fin.ext; simp; omega
    rw [hfirst, ← hsecond]
    linear_combination -hrow
  all_goals omega

private lemma wi087_kernel_right {a g : ℕ} (ha : 0 < a) (hag : a < g)
    (x : Fin (a + g) → ℂ) (hx : (wi087CoefficientMatrix a g ha hag).mulVec x = 0)
    (r : ℕ) (hgr : g ≤ r) (hr : r < a + g) :
    wi087RevVec a g x ⟨r - a, by omega⟩ = wi087RevVec a g x ⟨r - g, by omega⟩ := by
  have hrow := congr_fun hx (⟨r, hr⟩ : Fin (a + g))
  simp only [wi087CoefficientMatrix, Matrix.add_mulVec, Matrix.sub_mulVec, Pi.add_apply,
    Pi.sub_apply, Pi.zero_apply] at hrow
  rw [wi087_powerDiffMatrix_mulVec_of_ge, wi087_powerDiffMatrix_mulVec_of_ge,
    wi087_powerDiffMatrix_mulVec_of_ge, wi087_powerDiffMatrix_mulVec_of_mem,
    wi087_powerDiffMatrix_mulVec_of_mem] at hrow
  · unfold wi087RevVec
    linear_combination -hrow
  all_goals omega

private lemma wi087_kernel_period {a g : ℕ} (ha : 0 < a) (hag : a < g)
    (x : Fin (a + g) → ℂ) (hx : (wi087CoefficientMatrix a g ha hag).mulVec x = 0)
    (t : ℕ) (ht : t + (g - a) < a + g) :
    wi087RevVec a g x ⟨t + (g - a), ht⟩ = wi087RevVec a g x ⟨t, by omega⟩ := by
  by_cases hta : t < a
  · have h := wi087_kernel_right ha hag x hx (t + g) (by omega) (by omega)
    have h₁ : (⟨t + (g - a), ht⟩ : Fin (a + g)) =
        ⟨t + g - a, by omega⟩ := by apply Fin.ext; simp; omega
    have h₂ : (⟨t, by omega⟩ : Fin (a + g)) =
        ⟨t + g - g, by omega⟩ := by apply Fin.ext; simp
    rw [h₁, h₂]
    exact h
  · have h := wi087_kernel_left ha hag x hx (t - a) (by omega)
    have h₁ : (⟨t + (g - a), ht⟩ : Fin (a + g)) =
        ⟨t - a + g, by omega⟩ := by apply Fin.ext; simp; omega
    have h₂ : (⟨t, by omega⟩ : Fin (a + g)) =
        ⟨t - a + a, by omega⟩ := by apply Fin.ext; simp; omega
    rw [h₁, h₂]
    exact h

private lemma wi087_revVec_eq_mod {a g : ℕ} (ha : 0 < a) (hag : a < g)
    (x : Fin (a + g) → ℂ) (hx : (wi087CoefficientMatrix a g ha hag).mulVec x = 0)
    (n : ℕ) (hn : n < a + g) :
    wi087RevVec a g x ⟨n, hn⟩ =
      wi087RevVec a g x
        ⟨n % (g - a), by have := Nat.mod_lt n (by omega : 0 < g - a); omega⟩ := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
      by_cases hnd : n < g - a
      · have heq : (⟨n, hn⟩ : Fin (a + g)) =
            ⟨n % (g - a), by have := Nat.mod_lt n (by omega : 0 < g - a); omega⟩ := by
          apply Fin.ext
          simp [Nat.mod_eq_of_lt hnd]
        exact congrArg (wi087RevVec a g x) heq
      · have hdn : g - a ≤ n := by omega
        have hsub : n - (g - a) < n := by omega
        have hsub_bound : n - (g - a) < a + g := by omega
        have hstep := wi087_kernel_period ha hag x hx (n - (g - a)) (by omega)
        have hind := ih (n - (g - a)) hsub hsub_bound
        have hmod : (n - (g - a)) % (g - a) = n % (g - a) := by
          conv_rhs => rw [← Nat.sub_add_cancel hdn]
          rw [Nat.add_mod, Nat.mod_self, add_zero, Nat.mod_mod]
        have hfirst : (⟨n, hn⟩ : Fin (a + g)) =
            ⟨n - (g - a) + (g - a), by omega⟩ := by
          apply Fin.ext
          simp
          omega
        have hlast :
            (⟨(n - (g - a)) % (g - a), by
                have := Nat.mod_lt (n - (g - a)) (by omega : 0 < g - a)
                omega⟩ : Fin (a + g)) =
              ⟨n % (g - a), by
                have := Nat.mod_lt n (by omega : 0 < g - a)
                omega⟩ := by
          apply Fin.ext
          exact hmod
        calc
          wi087RevVec a g x ⟨n, hn⟩ =
              wi087RevVec a g x ⟨n - (g - a), hsub_bound⟩ := by
                rw [hfirst]
                exact hstep
          _ = wi087RevVec a g x
              ⟨(n - (g - a)) % (g - a), by
                have := Nat.mod_lt (n - (g - a)) (by omega : 0 < g - a)
                omega⟩ := hind
          _ = wi087RevVec a g x ⟨n % (g - a), by
                have := Nat.mod_lt n (by omega : 0 < g - a)
                omega⟩ := congrArg (wi087RevVec a g x) hlast

private lemma wi087_cyclic_three_term_eq_zero {d : ℕ} (hd : d % 3 ≠ 0)
    (a : ZMod d) (f : ZMod d → ℂ)
    (hrec : ∀ r, f (r + a) + f r + f (r - a) = 0) : f = 0 := by
  have htwo : ∀ r, f (r + 2 * a) = f (r - a) := by
    intro r
    have h0 := hrec r
    have h1 := hrec (r + a)
    have h1' : f (r + 2 * a) + f (r + a) + f r = 0 := by
      convert h1 using 1 <;> ring_nf
    linear_combination h1' - h0
  have hshift3 : ∀ r, f (r + 3 * a) = f r := by
    intro r
    have h := htwo (r + a)
    convert h using 1 <;> ring_nf
  have hperiod : ∀ (n : ℕ) r, f (r + n • (3 * a)) = f r := by
    intro n
    induction n with
    | zero => intro r; simp
    | succ n ih =>
        intro r
        rw [succ_nsmul, ← add_assoc, hshift3, ih]
  have hcases : d % 3 = 1 ∨ d % 3 = 2 := by
    have hlt := Nat.mod_lt d (by omega : 0 < 3)
    omega
  have hinv : ∀ r, f (r + a) = f r := by
    rcases hcases with hmod | hmod
    · intro r
      let k := d / 3
      have hdform : d = 3 * k + 1 := by
        dsimp [k]
        omega
      have hcoeff : (1 : ZMod d) + (k : ZMod d) * 3 = (d : ZMod d) := by
        rw [hdform]
        push_cast
        ring
      have hindex : (r + a) + k • (3 * a) = r := by
        rw [nsmul_eq_mul]
        calc
          (r + a) + (k : ZMod d) * (3 * a) =
              r + ((1 : ZMod d) + (k : ZMod d) * 3) * a := by ring
          _ = r + (d : ZMod d) * a := by rw [hcoeff]
          _ = r := by rw [ZMod.natCast_self]; ring
      have hp := hperiod k (r + a)
      rw [hindex] at hp
      exact hp.symm
    · intro r
      let k := d / 3
      have hdform : d = 3 * k + 2 := by
        dsimp [k]
        omega
      have hcoeff : (2 : ZMod d) + (k : ZMod d) * 3 = (d : ZMod d) := by
        rw [hdform]
        push_cast
        ring
      have hshift2 : ∀ s, f (s + 2 * a) = f s := by
        intro s
        have hindex : (s + 2 * a) + k • (3 * a) = s := by
          rw [nsmul_eq_mul]
          calc
            (s + 2 * a) + (k : ZMod d) * (3 * a) =
                s + ((2 : ZMod d) + (k : ZMod d) * 3) * a := by ring
            _ = s + (d : ZMod d) * a := by rw [hcoeff]
            _ = s := by rw [ZMod.natCast_self]; ring
        have hp := hperiod k (s + 2 * a)
        rw [hindex] at hp
        exact hp.symm
      calc
        f (r + a) = f (r + 3 * a) := by
          symm
          convert hshift2 (r + a) using 1 <;> ring_nf
        _ = f r := hshift3 r
  funext r
  have hminus : f (r - a) = f r := by
    have h := hinv (r - a)
    convert h.symm using 1 <;> ring_nf
  have hr := hrec r
  rw [hinv r, hminus] at hr
  have hz : (3 : ℂ) * f r = 0 := by linear_combination hr
  exact (mul_eq_zero.mp hz).resolve_left (by norm_num)

private lemma wi087_coefficientMatrix_kernel_eq_zero {a g : ℕ}
    (ha : 0 < a) (hag : a < g) (hdmod : (g - a) % 3 ≠ 0)
    (x : Fin (a + g) → ℂ) (hx : (wi087CoefficientMatrix a g ha hag).mulVec x = 0) :
    x = 0 := by
  let d := g - a
  have hdpos : 0 < d := by dsimp [d]; omega
  letI : NeZero d := ⟨Nat.ne_of_gt hdpos⟩
  let f : ZMod d → ℂ := fun s ↦
    wi087RevVec a g x ⟨s.val, by have := s.val_lt; dsimp [d] at this; omega⟩
  have hcast (n : ℕ) (hn : n < a + g) :
      wi087RevVec a g x ⟨n, hn⟩ = f (n : ZMod d) := by
    rw [wi087_revVec_eq_mod ha hag x hx n hn]
    unfold f
    apply congrArg (wi087RevVec a g x)
    apply Fin.ext
    simp [ZMod.val_natCast, d]
  have hforward : ∀ s : ZMod d,
      f (s + 2 * (a : ZMod d)) + f (s + (a : ZMod d)) + f s = 0 := by
    intro s
    let t := s.val
    have htlt : t < d := s.val_lt
    have hm := wi087_kernel_middle ha hag x hx (a + t) (by omega)
      (by dsimp [d] at htlt; omega)
    have h₂ : (⟨a + t + a, by dsimp [d] at htlt; omega⟩ : Fin (a + g)) =
        ⟨t + 2 * a, by dsimp [d] at htlt; omega⟩ := by apply Fin.ext; simp; omega
    have h₁ : (⟨a + t, by dsimp [d] at htlt; omega⟩ : Fin (a + g)) =
        ⟨t + a, by dsimp [d] at htlt; omega⟩ := by apply Fin.ext; simp; omega
    have h₀ : (⟨a + t - a, by dsimp [d] at htlt; omega⟩ : Fin (a + g)) =
        ⟨t, by dsimp [d] at htlt; omega⟩ := by apply Fin.ext; simp
    rw [h₂, h₁, h₀] at hm
    rw [hcast (t + 2 * a) (by dsimp [d] at htlt; omega),
      hcast (t + a) (by dsimp [d] at htlt; omega),
      hcast t (by dsimp [d] at htlt; omega)] at hm
    have hts : (t : ZMod d) = s := ZMod.natCast_zmod_val s
    convert hm using 1 <;> congr 1 <;> rw [← hts] <;> push_cast <;> ring
  have hfzero : f = 0 := by
    apply wi087_cyclic_three_term_eq_zero (by simpa [d] using hdmod) (a : ZMod d) f
    intro r
    have h := hforward (r - (a : ZMod d))
    convert h using 1 <;> ring_nf
  funext i
  have hrev : wi087RevVec a g x ⟨a + g - 1 - (i : ℕ), by omega⟩ = 0 := by
    rw [hcast]
    exact congr_fun hfzero _
  unfold wi087RevVec at hrev
  have hi : i =
      (⟨a + g - 1 - (⟨a + g - 1 - (i : ℕ), by omega⟩ : Fin (a + g)), by omega⟩ :
        Fin (a + g)) := by
    apply Fin.ext
    simp
    omega
  rw [hi]
  exact hrev

private theorem wi087_coefficientMatrix_mulVec_injective {a g : ℕ}
    (ha : 0 < a) (hag : a < g) (hdmod : (g - a) % 3 ≠ 0) :
    Function.Injective (wi087CoefficientMatrix a g ha hag).mulVec := by
  intro x y hxy
  apply sub_eq_zero.mp
  apply wi087_coefficientMatrix_kernel_eq_zero ha hag hdmod
  rw [Matrix.mulVec_sub, hxy, sub_self]

private def wi087Alpha (p q : ℕ) : ℕ := (2 * p - q) / 3

private def wi087Beta (p q : ℕ) : ℕ := (p + q) / 3

private def wi087Delta (p q : ℕ) : ℕ := (p * q + p - q) / 3

private def wi087Gamma (p q : ℕ) : ℕ := wi087Beta p q - wi087Alpha p q

private lemma wi087_alpha_pos {p q : ℕ} (hpmod : p % 3 = 2) (hqmod : q % 3 = 1)
    (hclose : q < 2 * p) : 0 < wi087Alpha p q := by
  simp only [wi087Alpha]
  omega

private lemma wi087_three_mul_alpha {p q : ℕ}
    (hpmod : p % 3 = 2) (hqmod : q % 3 = 1) (hclose : q < 2 * p) :
    3 * wi087Alpha p q = 2 * p - q := by
  simp only [wi087Alpha]
  omega

private lemma wi087_three_mul_beta {p q : ℕ}
    (hpmod : p % 3 = 2) (hqmod : q % 3 = 1) :
    3 * wi087Beta p q = p + q := by
  simp only [wi087Beta]
  omega

private lemma wi087_alpha_add_beta {p q : ℕ}
    (hpmod : p % 3 = 2) (hqmod : q % 3 = 1) (hclose : q < 2 * p) :
    wi087Alpha p q + wi087Beta p q = p := by
  simp only [wi087Alpha, wi087Beta]
  omega

private lemma wi087_beta_le_pred {p q : ℕ}
    (hpmod : p % 3 = 2) (hqmod : q % 3 = 1) (hclose : q < 2 * p) :
    wi087Beta p q ≤ p - 1 := by
  simp only [wi087Beta]
  omega

private lemma wi087_beta_eq_alpha_add_gamma {p q : ℕ}
    (hpmod : p % 3 = 2) (hqmod : q % 3 = 1) (hpq : p < q)
    (hclose : q < 2 * p) :
    wi087Beta p q = wi087Alpha p q + wi087Gamma p q := by
  have ha := wi087_alpha_pos hpmod hqmod hclose
  have hab := wi087_alpha_add_beta hpmod hqmod hclose
  have h3a := wi087_three_mul_alpha hpmod hqmod hclose
  have h3b := wi087_three_mul_beta hpmod hqmod
  simp only [wi087Gamma]
  omega

private lemma wi087_alpha_lt_gamma {p q : ℕ}
    (hpmod : p % 3 = 2) (hqmod : q % 3 = 1) (hpq : p < q)
    (hclose : q < 2 * p) : wi087Alpha p q < wi087Gamma p q := by
  have h3a := wi087_three_mul_alpha hpmod hqmod hclose
  have h3b := wi087_three_mul_beta hpmod hqmod
  have hab := wi087_beta_eq_alpha_add_gamma hpmod hqmod hpq hclose
  omega

private lemma wi087_gamma_sub_alpha {p q : ℕ}
    (hpmod : p % 3 = 2) (hqmod : q % 3 = 1) (hpq : p < q)
    (hclose : q < 2 * p) :
    wi087Gamma p q - wi087Alpha p q = q - p := by
  have h3a := wi087_three_mul_alpha hpmod hqmod hclose
  have h3b := wi087_three_mul_beta hpmod hqmod
  have hag := wi087_alpha_lt_gamma hpmod hqmod hpq hclose
  simp only [wi087Gamma]
  omega

private lemma wi087_gamma_add_beta {p q : ℕ}
    (hpmod : p % 3 = 2) (hqmod : q % 3 = 1) (hpq : p < q)
    (hclose : q < 2 * p) :
    wi087Gamma p q + wi087Beta p q = q := by
  have h3a := wi087_three_mul_alpha hpmod hqmod hclose
  have h3b := wi087_three_mul_beta hpmod hqmod
  have hab := wi087_beta_eq_alpha_add_gamma hpmod hqmod hpq hclose
  omega

private lemma wi087_three_mul_delta {p q : ℕ} (hp : p.Prime)
    (hpmod : p % 3 = 2) (hqmod : q % 3 = 1) :
    3 * wi087Delta p q = p * q + p - q := by
  have hpqmod : (p * q) % 3 = 2 := by
    rw [Nat.mul_mod, hpmod, hqmod]
  have hqle : q ≤ p * q + p := by
    have hqmul : q ≤ p * q := by
      simpa [Nat.mul_comm] using Nat.le_mul_of_pos_left q hp.pos
    omega
  have hnum_mod : (p * q + p - q) % 3 = 0 := by omega
  exact Nat.mul_div_cancel' (Nat.dvd_of_mod_eq_zero hnum_mod)

private lemma wi087_delta_eq_alpha_add {p q : ℕ} (hp : p.Prime)
    (hpmod : p % 3 = 2) (hqmod : q % 3 = 1) (hclose : q < 2 * p) :
    wi087Delta p q = wi087Alpha p q + p * ((q - 1) / 3) := by
  have h3d := wi087_three_mul_delta hp hpmod hqmod
  have h3a := wi087_three_mul_alpha hpmod hqmod hclose
  have h3q : 3 * ((q - 1) / 3) = q - 1 := by omega
  have hrhs :
      3 * (wi087Alpha p q + p * ((q - 1) / 3)) = p * q + p - q := by
    calc
      3 * (wi087Alpha p q + p * ((q - 1) / 3)) =
          3 * wi087Alpha p q + p * (3 * ((q - 1) / 3)) := by ring
      _ = (2 * p - q) + p * (q - 1) := by rw [h3a, h3q]
      _ = p * q + p - q := by
        rw [Nat.mul_sub_left_distrib]
        have hqpos : 0 < q := by omega
        have hpmul : p ≤ p * q := Nat.le_mul_of_pos_right p hqpos
        omega
  exact Nat.mul_left_cancel (by norm_num) (h3d.trans hrhs.symm)

private lemma wi087_delta_eq_beta_add {p q : ℕ} (hp : p.Prime)
    (hpmod : p % 3 = 2) (hqmod : q % 3 = 1) :
    wi087Delta p q = wi087Beta p q + q * ((p - 2) / 3) := by
  have h3d := wi087_three_mul_delta hp hpmod hqmod
  have h3b := wi087_three_mul_beta hpmod hqmod
  have h3p : 3 * ((p - 2) / 3) = p - 2 := by omega
  have hrhs :
      3 * (wi087Beta p q + q * ((p - 2) / 3)) = p * q + p - q := by
    calc
      3 * (wi087Beta p q + q * ((p - 2) / 3)) =
          3 * wi087Beta p q + q * (3 * ((p - 2) / 3)) := by ring
      _ = (p + q) + q * (p - 2) := by rw [h3b, h3p]
      _ = p * q + p - q := by
        rw [Nat.mul_sub_left_distrib, Nat.mul_comm q p, Nat.mul_comm q 2]
        have hp2 := hp.two_le
        have h2q : 2 * q ≤ p * q := by
          simpa [Nat.mul_comm] using Nat.mul_le_mul_right q hp2
        omega
  exact Nat.mul_left_cancel (by norm_num) (h3d.trans hrhs.symm)

private lemma wi087_two_delta_lt_product {p q : ℕ} (hp : p.Prime) (hpq : p < q)
    (hpmod : p % 3 = 2) (hqmod : q % 3 = 1) :
    2 * wi087Delta p q < p * q := by
  have h3 := wi087_three_mul_delta hp hpmod hqmod
  have hqmul : q ≤ p * q := by
    simpa [Nat.mul_comm] using Nat.le_mul_of_pos_left q hp.pos
  omega

private lemma wi087_lcm_eq_mul {p q : ℕ} (hp : p.Prime) (hq : q.Prime)
    (hpq : p < q) : Nat.lcm p q = p * q := by
  apply Nat.Coprime.lcm_eq_mul
  rw [hp.coprime_iff_not_dvd]
  intro hpq_dvd
  rcases (Nat.dvd_prime hq).mp hpq_dvd with h | h
  · exact hp.ne_one h
  · omega

private def wi087PrimitivePhase (m start : ℕ) :
    Matrix (PrimitiveFrequency m) (PrimitiveFrequency m) ℂ :=
  Matrix.diagonal fun z ↦ (z : ℂ) ^ start

private lemma wi087_shiftedSamplingMatrix_eq_mul_phase {m d start : ℕ} :
    shiftedSamplingMatrix m d start =
      shiftedSamplingMatrix m d 0 * wi087PrimitivePhase m start := by
  classical
  ext x z
  simp only [shiftedSamplingMatrix, wi087PrimitivePhase]
  rw [Matrix.mul_diagonal, pow_add]
  have hz : shiftedSamplingMatrix m d 0 x z = (z : ℂ) ^ (x : ℕ) := by
    simp [shiftedSamplingMatrix]
  rw [hz]
  ring

private lemma wi087_shifted_boundary_product_eq_phase_mul {m n d start : ℕ} :
    (shiftedSamplingMatrix m d start).conjTranspose *
        shiftedSamplingMatrix n d start =
      (wi087PrimitivePhase m start).conjTranspose *
        ((shiftedSamplingMatrix m d 0).conjTranspose *
          shiftedSamplingMatrix n d 0) * wi087PrimitivePhase n start := by
  rw [wi087_shiftedSamplingMatrix_eq_mul_phase (m := m) (d := d) (start := start),
    wi087_shiftedSamplingMatrix_eq_mul_phase (m := n) (d := d) (start := start),
    Matrix.conjTranspose_mul]
  simp only [Matrix.mul_assoc]

private lemma wi087_primitivePhase_det_isUnit {m start : ℕ} (hm : 0 < m) :
    IsUnit (wi087PrimitivePhase m start).det := by
  rw [isUnit_iff_ne_zero, wi087PrimitivePhase, Matrix.det_diagonal,
    Finset.prod_ne_zero_iff]
  intro z hz
  exact pow_ne_zero _ (primitive_ne_zero hm z)

private lemma wi087_primitivePhase_conjTranspose_det_isUnit {m start : ℕ} (hm : 0 < m) :
    IsUnit (wi087PrimitivePhase m start).conjTranspose.det := by
  rw [isUnit_iff_ne_zero, Matrix.det_conjTranspose, star_ne_zero]
  exact (wi087_primitivePhase_det_isUnit hm).ne_zero

private lemma wi087_shifted_boundary_product_rank_eq_start_zero {m n d start : ℕ}
    (hm : 0 < m) (hn : 0 < n) :
    ((shiftedSamplingMatrix m d start).conjTranspose *
        shiftedSamplingMatrix n d start).rank =
      ((shiftedSamplingMatrix m d 0).conjTranspose *
        shiftedSamplingMatrix n d 0).rank := by
  rw [wi087_shifted_boundary_product_eq_phase_mul,
    Matrix.rank_mul_eq_left_of_isUnit_det
      (wi087PrimitivePhase n start)
      ((wi087PrimitivePhase m start).conjTranspose *
        ((shiftedSamplingMatrix m d 0).conjTranspose * shiftedSamplingMatrix n d 0))
      (wi087_primitivePhase_det_isUnit hn),
    Matrix.rank_mul_eq_right_of_isUnit_det
      (wi087PrimitivePhase m start).conjTranspose
      ((shiftedSamplingMatrix m d 0).conjTranspose * shiftedSamplingMatrix n d 0)
      (wi087_primitivePhase_conjTranspose_det_isUnit hm)]

private lemma wi087_crossGram_rank_eq_of_boundary_product_rank_at_zero
    {m n N d k : ℕ} (hm : 0 < m) (hn : 0 < n) (hmn : m ≠ n)
    (hd : boundaryDefect m n N = d)
    (hrank :
      ((shiftedSamplingMatrix m d 0).conjTranspose *
        shiftedSamplingMatrix n d 0).rank = k) :
    (crossGram m n N).rank = k := by
  classical
  rw [crossGram_eq_short_boundary hm hn hmn]
  simp only [boundaryDefect] at hd
  let ell := Nat.lcm m n
  let r := N % ell
  let d' := min r (ell - r)
  change d' = d at hd
  subst d
  by_cases hshort : r ≤ ell - r
  · rw [ite_eq_left hshort]
    exact hrank
  · rw [ite_eq_right hshort, Matrix.rank_smul_of_mem_nonZeroDivisors,
      wi087_shifted_boundary_product_rank_eq_start_zero hm hn, hrank]
    simp

private lemma wi087_P_eq_pow_a_mul_Q {a g p : ℕ} (z : ℂ)
    (hap : a + (a + g) = p) (hz : z ^ p = 1) :
    wi087P a g z = z ^ a * wi087Q a g z := by
  have hlast : z ^ (a + (a + g)) = 1 := by simpa [hap] using hz
  rw [wi087P, wi087Q, mul_add, mul_add, mul_one, ← pow_add, ← pow_add, hlast]
  ring

private lemma wi087_P_eq_pow_beta_mul_Q {a g q : ℕ} (z : ℂ)
    (hgq : (a + g) + g = q) (hdouble : (a + g) + (a + g) = q + a)
    (hz : z ^ q = 1) :
    wi087P a g z = z ^ (a + g) * wi087Q a g z := by
  have hfirst : z ^ ((a + g) + g) = 1 := by simpa [hgq] using hz
  have hsecond : z ^ ((a + g) + (a + g)) = z ^ a := by
    rw [hdouble, pow_add, hz, one_mul]
  rw [wi087P, wi087Q, mul_add, mul_add, mul_one, ← pow_add, ← pow_add,
    hfirst, hsecond]
  ring

private lemma wi087_Q_ne_zero_of_primitive {a g m : ℕ} (ha : 0 < a) (hag : a < g)
    (hgm : g - a < m) (z : ℂ) (hz0 : z ≠ 0) (hzprim : IsPrimitiveRoot z m)
    (hPQ : wi087P a g z = z ^ a * wi087Q a g z ∨
      wi087P a g z = z ^ (a + g) * wi087Q a g z) :
    wi087Q a g z ≠ 0 := by
  intro hQ
  have hP : wi087P a g z = 0 := by rcases hPQ with h | h <;> simp [h, hQ]
  have hpow : z ^ a = z ^ g := by
    simp only [wi087P, wi087Q] at hP hQ
    linear_combination hP - hQ
  have hga : a + (g - a) = g := Nat.add_sub_of_le hag.le
  have hperiod : z ^ (g - a) = 1 := by
    apply mul_left_cancel₀ (pow_ne_zero _ hz0)
    rw [← pow_add, hga, hpow]
    simp
  have hdvd : m ∣ g - a := (hzprim.pow_eq_one_iff_dvd _).mp hperiod
  exact (Nat.not_dvd_of_pos_of_lt (by omega) hgm) hdvd

private lemma wi087_primitive_pow_delta_p {p q : ℕ}
    (hp : p.Prime) (hpmod : p % 3 = 2) (hqmod : q % 3 = 1)
    (hclose : q < 2 * p) (z : PrimitiveFrequency p) :
    (z : ℂ) ^ wi087Delta p q = (z : ℂ) ^ wi087Alpha p q := by
  rw [wi087_delta_eq_alpha_add hp hpmod hqmod hclose, pow_add, pow_mul]
  have hz : (z : ℂ) ^ p = 1 :=
    (primitive_isPrimitiveRoot z).pow_eq_one_iff_dvd p |>.2 dvd_rfl
  rw [hz, one_pow, mul_one]

private lemma wi087_primitive_pow_delta_q {p q : ℕ}
    (hp : p.Prime) (hpmod : p % 3 = 2) (hqmod : q % 3 = 1)
    (w : PrimitiveFrequency q) :
    (w : ℂ) ^ wi087Delta p q = (w : ℂ) ^ wi087Beta p q := by
  rw [wi087_delta_eq_beta_add hp hpmod hqmod, pow_add, pow_mul]
  have hw : (w : ℂ) ^ q = 1 :=
    (primitive_isPrimitiveRoot w).pow_eq_one_iff_dvd q |>.2 dvd_rfl
  rw [hw, one_pow, mul_one]

private lemma wi087_P_eq_pow_alpha_mul_Q_at_p {p q : ℕ}
    (hpmod : p % 3 = 2) (hqmod : q % 3 = 1) (hpq : p < q)
    (hclose : q < 2 * p) (z : PrimitiveFrequency p) :
    wi087P (wi087Alpha p q) (wi087Gamma p q) z =
      (z : ℂ) ^ wi087Alpha p q *
        wi087Q (wi087Alpha p q) (wi087Gamma p q) z := by
  apply wi087_P_eq_pow_a_mul_Q
    (a := wi087Alpha p q) (g := wi087Gamma p q) (p := p) (z := (z : ℂ))
  · have hab := wi087_alpha_add_beta hpmod hqmod hclose
    have hbg := wi087_beta_eq_alpha_add_gamma hpmod hqmod hpq hclose
    omega
  · exact (primitive_isPrimitiveRoot z).pow_eq_one_iff_dvd p |>.2 dvd_rfl

private lemma wi087_P_eq_pow_beta_mul_Q_at_q {p q : ℕ}
    (hpmod : p % 3 = 2) (hqmod : q % 3 = 1) (hpq : p < q)
    (hclose : q < 2 * p) (w : PrimitiveFrequency q) :
    wi087P (wi087Alpha p q) (wi087Gamma p q) w =
      (w : ℂ) ^ wi087Beta p q *
        wi087Q (wi087Alpha p q) (wi087Gamma p q) w := by
  rw [wi087_beta_eq_alpha_add_gamma hpmod hqmod hpq hclose]
  apply wi087_P_eq_pow_beta_mul_Q
    (a := wi087Alpha p q) (g := wi087Gamma p q) (q := q) (z := (w : ℂ))
  · have hgb := wi087_gamma_add_beta hpmod hqmod hpq hclose
    have hbg := wi087_beta_eq_alpha_add_gamma hpmod hqmod hpq hclose
    omega
  · have h3a := wi087_three_mul_alpha hpmod hqmod hclose
    have h3b := wi087_three_mul_beta hpmod hqmod
    have hgb := wi087_gamma_add_beta hpmod hqmod hpq hclose
    have hbg := wi087_beta_eq_alpha_add_gamma hpmod hqmod hpq hclose
    omega
  · exact (primitive_isPrimitiveRoot w).pow_eq_one_iff_dvd q |>.2 dvd_rfl

private lemma wi087_Q_ne_zero_at_p {p q : ℕ} (hp : p.Prime)
    (hpmod : p % 3 = 2) (hqmod : q % 3 = 1) (hpq : p < q)
    (hclose : q < 2 * p) (z : PrimitiveFrequency p) :
    wi087Q (wi087Alpha p q) (wi087Gamma p q) z ≠ 0 := by
  apply wi087_Q_ne_zero_of_primitive
    (a := wi087Alpha p q) (g := wi087Gamma p q) (m := p) (z := (z : ℂ))
    (wi087_alpha_pos hpmod hqmod hclose)
    (wi087_alpha_lt_gamma hpmod hqmod hpq hclose)
  · rw [wi087_gamma_sub_alpha hpmod hqmod hpq hclose]
    omega
  · exact primitive_ne_zero hp.pos z
  · exact primitive_isPrimitiveRoot z
  · exact Or.inl (wi087_P_eq_pow_alpha_mul_Q_at_p hpmod hqmod hpq hclose z)

private lemma wi087_Q_ne_zero_at_q {p q : ℕ} (hp : p.Prime) (hq : q.Prime)
    (hpmod : p % 3 = 2) (hqmod : q % 3 = 1) (hpq : p < q)
    (hclose : q < 2 * p) (w : PrimitiveFrequency q) :
    wi087Q (wi087Alpha p q) (wi087Gamma p q) w ≠ 0 := by
  apply wi087_Q_ne_zero_of_primitive
    (a := wi087Alpha p q) (g := wi087Gamma p q) (m := q) (z := (w : ℂ))
    (wi087_alpha_pos hpmod hqmod hclose)
    (wi087_alpha_lt_gamma hpmod hqmod hpq hclose)
  · rw [wi087_gamma_sub_alpha hpmod hqmod hpq hclose]
    have hp0 := hp.pos
    omega
  · exact primitive_ne_zero hq.pos w
  · exact primitive_isPrimitiveRoot w
  · apply Or.inr
    rw [← wi087_beta_eq_alpha_add_gamma hpmod hqmod hpq hclose]
    exact wi087_P_eq_pow_beta_mul_Q_at_q hpmod hqmod hpq hclose w

private lemma wi087_geometric_sum_scaled (d : ℕ) (z w : ℂ)
    (hz : z ≠ 0) (hzw : z ≠ w) :
    (∑ x ∈ Finset.range d, (z⁻¹ * w) ^ x) =
      z * (z ^ d)⁻¹ * ((z ^ d - w ^ d) / (z - w)) := by
  have hr : z⁻¹ * w ≠ 1 := by
    intro h
    exact hzw ((inv_mul_eq_one₀ hz).mp h)
  rw [geom_sum_eq hr]
  have hratio : z⁻¹ * w = w / z := by field_simp
  rw [hratio, div_pow]
  field_simp
  ring

private lemma wi087_evalKernel_div_eq_delta_div {p q : ℕ}
    (hp : p.Prime) (hq : q.Prime) (hpmod : p % 3 = 2) (hqmod : q % 3 = 1)
    (hpq : p < q) (hclose : q < 2 * p)
    (z : PrimitiveFrequency p) (w : PrimitiveFrequency q) :
    wi087EvalKernel (wi087Alpha p q + wi087Gamma p q)
        (wi087CoefficientMatrix (wi087Alpha p q) (wi087Gamma p q)
          (wi087_alpha_pos hpmod hqmod hclose)
          (wi087_alpha_lt_gamma hpmod hqmod hpq hclose)) z w /
      (wi087Q (wi087Alpha p q) (wi087Gamma p q) z *
        wi087Q (wi087Alpha p q) (wi087Gamma p q) w) =
      (((z : ℂ) ^ wi087Delta p q - (w : ℂ) ^ wi087Delta p q) /
        ((z : ℂ) - (w : ℂ))) := by
  let a := wi087Alpha p q
  let g := wi087Gamma p q
  have ha : 0 < a := wi087_alpha_pos hpmod hqmod hclose
  have hag : a < g := wi087_alpha_lt_gamma hpmod hqmod hpq hclose
  have hQz := wi087_Q_ne_zero_at_p hp hpmod hqmod hpq hclose z
  have hQw := wi087_Q_ne_zero_at_q hp hq hpmod hqmod hpq hclose w
  have hzw := primitive_ne_of_orders_ne (Nat.ne_of_lt hpq) z w
  apply (div_eq_div_iff (mul_ne_zero hQz hQw) (sub_ne_zero.mpr hzw)).2
  have hcoeff := wi087_coefficientMatrix_mul_sub a g ha hag (z : ℂ) (w : ℂ)
  have hPz := wi087_P_eq_pow_alpha_mul_Q_at_p hpmod hqmod hpq hclose z
  have hPw := wi087_P_eq_pow_beta_mul_Q_at_q hpmod hqmod hpq hclose w
  have hzd := wi087_primitive_pow_delta_p hp hpmod hqmod hclose z
  have hwd := wi087_primitive_pow_delta_q hp hpmod hqmod w
  dsimp [a, g] at hcoeff ⊢
  calc
    wi087EvalKernel (wi087Alpha p q + wi087Gamma p q)
          (wi087CoefficientMatrix (wi087Alpha p q) (wi087Gamma p q) ha hag)
          (z : ℂ) (w : ℂ) * ((z : ℂ) - (w : ℂ)) =
        wi087P (wi087Alpha p q) (wi087Gamma p q) z *
          wi087Q (wi087Alpha p q) (wi087Gamma p q) w -
        wi087Q (wi087Alpha p q) (wi087Gamma p q) z *
          wi087P (wi087Alpha p q) (wi087Gamma p q) w := hcoeff
    _ = (((z : ℂ) ^ wi087Delta p q - (w : ℂ) ^ wi087Delta p q) *
        (wi087Q (wi087Alpha p q) (wi087Gamma p q) z *
          wi087Q (wi087Alpha p q) (wi087Gamma p q) w)) := by
      rw [hPz, hPw, hzd, hwd]
      ring

private def wi087LeftScale (p q : ℕ) (z : PrimitiveFrequency p) : ℂ :=
  (z : ℂ) * ((z : ℂ) ^ wi087Delta p q)⁻¹ *
    (wi087Q (wi087Alpha p q) (wi087Gamma p q) z)⁻¹

private def wi087RightScale (p q : ℕ) (w : PrimitiveFrequency q) : ℂ :=
  (wi087Q (wi087Alpha p q) (wi087Gamma p q) w)⁻¹

private lemma wi087_boundary_product_eq_factorization {p q : ℕ}
    (hp : p.Prime) (hq : q.Prime) (hpmod : p % 3 = 2) (hqmod : q % 3 = 1)
    (hpq : p < q) (hclose : q < 2 * p) :
    (shiftedSamplingMatrix p (wi087Delta p q) 0).conjTranspose *
        shiftedSamplingMatrix q (wi087Delta p q) 0 =
      Matrix.diagonal (wi087LeftScale p q) *
        (wi087PowerEval (wi087Alpha p q + wi087Gamma p q)
            (fun z : PrimitiveFrequency p ↦ (z : ℂ)) *
          wi087CoefficientMatrix (wi087Alpha p q) (wi087Gamma p q)
            (wi087_alpha_pos hpmod hqmod hclose)
            (wi087_alpha_lt_gamma hpmod hqmod hpq hclose) *
          (wi087PowerEval (wi087Alpha p q + wi087Gamma p q)
            (fun w : PrimitiveFrequency q ↦ (w : ℂ))).transpose) *
        Matrix.diagonal (wi087RightScale p q) := by
  classical
  ext z w
  rw [shifted_boundary_product_apply hp.pos]
  simp only [zero_add, crossRatio]
  rw [wi087_geometric_sum_scaled _ (z : ℂ) (w : ℂ)
    (primitive_ne_zero hp.pos z)
    (primitive_ne_of_orders_ne (Nat.ne_of_lt hpq) z w)]
  rw [← wi087_evalKernel_div_eq_delta_div hp hq hpmod hqmod hpq hclose z w]
  rw [Matrix.mul_diagonal, Matrix.diagonal_mul, wi087_powerEval_mul_apply]
  simp only [wi087LeftScale, wi087RightScale]
  have hQz := wi087_Q_ne_zero_at_p hp hpmod hqmod hpq hclose z
  have hQw := wi087_Q_ne_zero_at_q hp hq hpmod hqmod hpq hclose w
  field_simp

private lemma wi087_boundary_product_rank {p q : ℕ}
    (hp : p.Prime) (hq : q.Prime) (hpmod : p % 3 = 2) (hqmod : q % 3 = 1)
    (hpq : p < q) (hclose : q < 2 * p) :
    ((shiftedSamplingMatrix p (wi087Delta p q) 0).conjTranspose *
        shiftedSamplingMatrix q (wi087Delta p q) 0).rank = wi087Beta p q := by
  classical
  let a := wi087Alpha p q
  let g := wi087Gamma p q
  let b := a + g
  have ha : 0 < a := wi087_alpha_pos hpmod hqmod hclose
  have hag : a < g := wi087_alpha_lt_gamma hpmod hqmod hpq hclose
  have hbeta : b = wi087Beta p q := by
    dsimp [a, g, b]
    exact (wi087_beta_eq_alpha_add_gamma hpmod hqmod hpq hclose).symm
  have hbp : b ≤ Fintype.card (PrimitiveFrequency p) := by
    rw [primitiveFrequency_card, Nat.totient_prime hp, hbeta]
    exact wi087_beta_le_pred hpmod hqmod hclose
  have hbq : b ≤ Fintype.card (PrimitiveFrequency q) := by
    rw [primitiveFrequency_card, Nat.totient_prime hq, hbeta]
    have hle := wi087_beta_le_pred hpmod hqmod hclose
    have hp2 := hp.two_le
    omega
  let ep : Fin b ↪ PrimitiveFrequency p :=
    (Fin.castLEEmb hbp).trans
      (Fintype.equivFin (PrimitiveFrequency p)).symm.toEmbedding
  let eq : Fin b ↪ PrimitiveFrequency q :=
    (Fin.castLEEmb hbq).trans
      (Fintype.equivFin (PrimitiveFrequency q)).symm.toEmbedding
  have hep : Function.Injective
      ((fun z : PrimitiveFrequency p ↦ (z : ℂ)) ∘ (ep : Fin b → PrimitiveFrequency p)) := by
    intro i j hij
    exact ep.injective (Subtype.ext hij)
  have heq : Function.Injective
      ((fun w : PrimitiveFrequency q ↦ (w : ℂ)) ∘ (eq : Fin b → PrimitiveFrequency q)) := by
    intro i j hij
    exact eq.injective (Subtype.ext hij)
  have hdmod : (g - a) % 3 ≠ 0 := by
    dsimp [a, g]
    rw [wi087_gamma_sub_alpha hpmod hqmod hpq hclose]
    omega
  have hB : Function.Injective (wi087CoefficientMatrix a g ha hag).mulVec :=
    wi087_coefficientMatrix_mulVec_injective ha hag hdmod
  rw [wi087_boundary_product_eq_factorization hp hq hpmod hqmod hpq hclose]
  have hrank := wi087_rank_diagonal_powerEval_mul_of_injective
    (fun z : PrimitiveFrequency p ↦ (z : ℂ))
    (fun w : PrimitiveFrequency q ↦ (w : ℂ))
    (wi087CoefficientMatrix a g ha hag)
    (wi087LeftScale p q) (wi087RightScale p q)
    (ep : Fin b → PrimitiveFrequency p) (eq : Fin b → PrimitiveFrequency q)
    hep heq hB
    (fun z ↦ by
      exact mul_ne_zero
        (mul_ne_zero (primitive_ne_zero hp.pos z)
          (inv_ne_zero (pow_ne_zero _ (primitive_ne_zero hp.pos z))))
        (inv_ne_zero (wi087_Q_ne_zero_at_p hp hpmod hqmod hpq hclose z)))
    (fun w ↦ by
      exact inv_ne_zero (wi087_Q_ne_zero_at_q hp hq hpmod hqmod hpq hclose w))
  dsimp [a, g, b] at hrank
  exact hrank.trans hbeta

/-- On the close-prime congruence family, the WI-087 Loewner--Bezout boundary has exact rank
`(p + q) / 3`. -/
theorem crossGram_rank_eq_closePrime_loewner_bezout
    {p q N : ℕ}
    (hp : p.Prime) (hq : q.Prime)
    (hpq : p < q)
    (hpmod : p % 3 = 2)
    (hqmod : q % 3 = 1)
    (hclose : q < 2 * p)
    (hN : Mathia.WI081.boundaryDefect p q N =
      (p * q + p - q) / 3) :
    (Mathia.WI081.crossGram p q N).rank = (p + q) / 3 := by
  have hlcm : Nat.lcm p q = p * q := wi087_lcm_eq_mul hp hq hpq
  have hdelta_short : 2 * wi087Delta p q < Nat.lcm p q := by
    rw [hlcm]
    exact wi087_two_delta_lt_product hp hpq hpmod hqmod
  exact wi087_crossGram_rank_eq_of_boundary_product_rank_at_zero
    hp.pos hq.pos (Nat.ne_of_lt hpq) (by simpa [wi087Delta] using hN)
    (wi087_boundary_product_rank hp hq hpmod hqmod hpq hclose)

#print axioms crossGram_rank_le
#print axioms crossGram_rank_eq_of_boundaryDefect_le_totient
#print axioms crossGram_rank_eq_of_boundaryDefect_le_max_totient
#print axioms crossGram_rank_eq_closePrime_loewner_bezout

end Mathia.WI081
