import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.LinearAlgebra.SesquilinearForm.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-!
# WI-276: PSD cross-cut geometry and the sharp finite-path reserve

Associated finding:
`research/weil_inertia/findings/WI-276-cross-cut-energy-obeys-a-sharp-nilpotent-shift-reserve.md`.

Formalized boundary: null orthogonality for a real symmetric positive-semidefinite
bilinear form, the exact three-piece square-root bounds, the sharp N-vertex path
correlation bound with positive sine-vector equality, and scalar reserve algebra.
The path bound also holds for signed real coordinates. No positive definiteness is assumed.

Not formalized: the continuous truncated-translation/L² chain decomposition, its
ceiling/support realization, Suzuki's localized Weil framework, sharp-cut domain
admissibility, the sliding-window identity `integral q(window) = 2 F`, or the
integrated-source identity `S = integral Q`. Their scalar consequence `|F-S| ≤ I`
is an explicit premise. Sharpness is for the finite support-only relaxation, not
attainment by an actual Suzuki source profile, one-signedness, or prime overlap.
-/

noncomputable section
open scoped BigOperators
namespace Mathia.WI276

section PSD
variable {V : Type*} [AddCommGroup V] [Module ℝ V]
variable (B : LinearMap.BilinForm ℝ V) (hpos : ∀ x, 0 ≤ B x x) (hsym : B.IsSymm)
include hpos hsym

/-- A PSD null vector is form-orthogonal to every vector, even for a degenerate form. -/
theorem null_orthogonal {v : V} (hv : B v v = 0) (y : V) : B v y = 0 := by
  have hker := (B.apply_apply_same_eq_zero_iff hpos hsym).mp hv
  have hzero : B v = 0 := LinearMap.mem_ker.mp hker
  exact LinearMap.congr_fun hzero y

/-- Exact ordinary and reverse triangle bounds in the PSD form seminorm. -/
theorem three_piece_bounds (u w z : V) (hv : B (u + w + z) (u + w + z) = 0) :
    (Real.sqrt (B u u) - Real.sqrt (B z z)) ^ 2 ≤ B w w ∧
      B w w ≤ (Real.sqrt (B u u) + Real.sqrt (B z z)) ^ 2 := by
  have hu := null_orthogonal B hpos hsym hv u
  have hw := null_orthogonal B hpos hsym hv w
  have hz := null_orthogonal B hpos hsym hv z
  simp only [map_add, LinearMap.add_apply] at hu hw hz
  have hwu : B w u = B u w := hsym.eq w u
  have hzu : B z u = B u z := hsym.eq z u
  have hzw : B z w = B w z := hsym.eq z w
  have he : B w w = B u u + B z z + 2 * B u z := by linarith
  have hcs := B.apply_sq_le_of_symm hpos hsym u z
  have hsu := Real.sq_sqrt (hpos u)
  have hsz := Real.sq_sqrt (hpos z)
  have hn : 0 ≤ Real.sqrt (B u u) * Real.sqrt (B z z) := mul_nonneg
    (Real.sqrt_nonneg _) (Real.sqrt_nonneg _)
  have hp : (Real.sqrt (B u u) * Real.sqrt (B z z)) ^ 2 = B u u * B z z := by
    rw [mul_pow, hsu, hsz]
  have habs : |B u z| ≤ Real.sqrt (B u u) * Real.sqrt (B z z) := by
    apply (sq_le_sq₀ (abs_nonneg _) hn).mp
    simpa only [sq_abs, hp] using hcs
  obtain ⟨hl, hh⟩ := abs_le.mp habs
  constructor <;> nlinarith
end PSD

/-- Redistribute edge terms to their two incident interior vertices. -/
private theorem edge_redistribute (n : ℕ) (a t : ℕ → ℝ) :
    (∑ k ∈ Finset.range (n + 1), (a (k + 1) * t k + a k * t (k + 1))) =
      (∑ k ∈ Finset.range n, (a k + a (k + 2)) * t (k + 1)) +
        a 1 * t 0 + a n * t (n + 1) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, ih, Finset.sum_range_succ]
    ring

/-- Weighted Young inequality; the positive weights will be sine coordinates. -/
private theorem weighted_edge {a b : ℝ} (ha : 0 < a) (hb : 0 < b) (x y : ℝ) :
    2 * x * y ≤ b * (x ^ 2 / a) + a * (y ^ 2 / b) := by
  apply (mul_le_mul_iff_left₀ (mul_pos ha hb)).mp
  field_simp
  nlinarith [sq_nonneg (b * x - a * y)]

/-- A positive Dirichlet eigenvector bounds every real path vector.
Indices `1,...,n` are interior vertices; `0,n+1` are zero boundary values. -/
theorem path_bound_of_positive_eigenvector {n : ℕ}
    (b x : ℕ → ℝ) (c : ℝ)
    (b0 : b 0 = 0) (bn : b (n + 1) = 0)
    (bp : ∀ k, 1 ≤ k → k ≤ n → 0 < b k)
    (brec : ∀ k, k < n → b k + b (k + 2) = 2 * c * b (k + 1))
    (x0 : x 0 = 0) (xn : x (n + 1) = 0) :
    (∑ k ∈ Finset.range (n + 1), x k * x (k + 1)) ≤
      c * ∑ k ∈ Finset.range n, x (k + 1) ^ 2 := by
  have hedge : ∀ k ∈ Finset.range (n + 1),
      2 * x k * x (k + 1) ≤
        b (k + 1) * (x k ^ 2 / b k) + b k * (x (k + 1) ^ 2 / b (k + 1)) := by
    intro k hk
    have hk' := Finset.mem_range.mp hk
    by_cases hz : k = 0
    · subst k; simp [x0, b0]
    by_cases he : k = n
    · subst k; simp [xn, bn]
    exact weighted_edge (bp k (by omega) (by omega))
      (bp (k + 1) (by omega) (by omega)) _ _
  have hs := Finset.sum_le_sum hedge
  rw [edge_redistribute n b (fun k => x k ^ 2 / b k)] at hs
  have hterm : (∑ k ∈ Finset.range n,
      (b k + b (k + 2)) * (x (k + 1) ^ 2 / b (k + 1))) =
        2 * c * ∑ k ∈ Finset.range n, x (k + 1) ^ 2 := by
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro k hk
    rw [brec k (Finset.mem_range.mp hk)]
    have hb := ne_of_gt (bp (k + 1) (by omega) (by have := Finset.mem_range.mp hk; omega))
    field_simp
  rw [hterm] at hs
  simp only [b0, bn, div_zero, mul_zero, add_zero] at hs
  have hsum : (∑ k ∈ Finset.range (n + 1), 2 * x k * x (k + 1)) =
      2 * ∑ k ∈ Finset.range (n + 1), x k * x (k + 1) := by
    rw [Finset.mul_sum]; apply Finset.sum_congr rfl; intros; ring
  rw [hsum] at hs
  linarith

/-- The eigenvector itself has exactly the claimed correlation. -/
theorem path_eigenvector_equality {n : ℕ} (b : ℕ → ℝ) (c : ℝ)
    (b0 : b 0 = 0) (bn : b (n + 1) = 0)
    (brec : ∀ k, k < n → b k + b (k + 2) = 2 * c * b (k + 1)) :
    (∑ k ∈ Finset.range (n + 1), b k * b (k + 1)) =
      c * ∑ k ∈ Finset.range n, b (k + 1) ^ 2 := by
  have h := edge_redistribute n b b
  simp only [b0, bn, mul_zero, add_zero] at h
  have hl : (∑ k ∈ Finset.range (n + 1),
      (b (k + 1) * b k + b k * b (k + 1))) =
      2 * ∑ k ∈ Finset.range (n + 1), b k * b (k + 1) := by
    rw [Finset.mul_sum]; apply Finset.sum_congr rfl; intros; ring
  have hr : (∑ k ∈ Finset.range n, (b k + b (k + 2)) * b (k + 1)) =
      2 * c * ∑ k ∈ Finset.range n, b (k + 1) ^ 2 := by
    rw [Finset.mul_sum]; apply Finset.sum_congr rfl
    intro k hk; rw [brec k (Finset.mem_range.mp hk)]; ring
  rw [hl, hr] at h
  linarith

/-- The sharp coefficient for an N-vertex path (half its adjacency eigenvalue). -/
def pathConstant (n : ℕ) : ℝ := Real.cos (Real.pi / (n + 1))

/-- Sine ground state, with zero boundary coordinates at `0,n+1`. -/
def sineState (n k : ℕ) : ℝ := Real.sin (k * (Real.pi / (n + 1)))

private theorem sineState_zero (n : ℕ) : sineState n 0 = 0 := by simp [sineState]
private theorem sineState_end (n : ℕ) : sineState n (n + 1) = 0 := by
  have hd : (n : ℝ) + 1 ≠ 0 := by positivity
  simp [sineState, Nat.cast_add, Nat.cast_one, mul_div_cancel₀ _ hd]

theorem sineState_pos {n k : ℕ} (hk : 1 ≤ k) (hkn : k ≤ n) : 0 < sineState n k := by
  unfold sineState
  apply Real.sin_pos_of_pos_of_lt_pi
  · positivity
  · have hd : (0 : ℝ) < n + 1 := by positivity
    rw [← mul_div_assoc, div_lt_iff₀ hd]
    have hcast : (k : ℝ) < n + 1 := by exact_mod_cast (show k < n + 1 by omega)
    nlinarith [Real.pi_pos]

private theorem sineState_recurrence (n k : ℕ) :
    sineState n k + sineState n (k + 2) = 2 * pathConstant n * sineState n (k + 1) := by
  let θ : ℝ := Real.pi / (n + 1)
  have hl : (k : ℝ) * θ = ((k : ℝ) + 1) * θ - θ := by ring
  have hr : ((k : ℝ) + 2) * θ = ((k : ℝ) + 1) * θ + θ := by ring
  simp only [sineState, pathConstant, Nat.cast_add, Nat.cast_one, Nat.cast_ofNat]
  change Real.sin ((k : ℝ) * θ) + Real.sin (((k : ℝ) + 2) * θ) =
    2 * Real.cos θ * Real.sin (((k : ℝ) + 1) * θ)
  rw [hl, hr, Real.sin_sub, Real.sin_add]
  ring

/-- Exact cosine bound with explicit zero Dirichlet boundaries. -/
theorem dirichlet_path_bound {n : ℕ} (_hn : 2 ≤ n) (x : ℕ → ℝ)
    (x0 : x 0 = 0) (xn : x (n + 1) = 0) :
    (∑ k ∈ Finset.range (n + 1), x k * x (k + 1)) ≤
      pathConstant n * ∑ k ∈ Finset.range n, x (k + 1) ^ 2 :=
  path_bound_of_positive_eigenvector (sineState n) x (pathConstant n)
    (sineState_zero n) (sineState_end n) (fun _ hk hkn => sineState_pos hk hkn)
    (fun _ _ => sineState_recurrence _ _) x0 xn

/-- Removing the two zero boundary edges leaves exactly `n-1` edges. -/
private theorem boundary_edges {n : ℕ} (hn : 1 ≤ n) (x : ℕ → ℝ)
    (x0 : x 0 = 0) (xn : x (n + 1) = 0) :
    (∑ k ∈ Finset.range (n + 1), x k * x (k + 1)) =
      ∑ k ∈ Finset.range (n - 1), x (k + 1) * x (k + 2) := by
  rw [Finset.sum_range_succ']
  simp only [x0, zero_mul, add_zero]
  have hn' : n - 1 + 1 = n := by omega
  have hs := Finset.sum_range_succ (fun k => x (k + 1) * x (k + 1 + 1)) (n - 1)
  rw [hn'] at hs
  rw [hs]
  simp [xn, Nat.add_assoc]

private def pad (n : ℕ) (x : ℕ → ℝ) : ℕ → ℝ
  | 0 => 0
  | k + 1 => if k < n then x k else 0

/-- The sharp path bound for arbitrary real coordinates. Only the first `n` entries
are used, and `range (n-1)` counts each of the `n-1` edges exactly once. -/
theorem sharp_path_correlation {n : ℕ} (hn : 2 ≤ n) (x : ℕ → ℝ) :
    (∑ k ∈ Finset.range (n - 1), x k * x (k + 1)) ≤
      pathConstant n * ∑ k ∈ Finset.range n, x k ^ 2 := by
  have hx0 : pad n x 0 = 0 := rfl
  have hxn : pad n x (n + 1) = 0 := by simp [pad]
  have h := dirichlet_path_bound hn (pad n x) hx0 hxn
  rw [boundary_edges (by omega) (pad n x) hx0 hxn] at h
  have he : (∑ k ∈ Finset.range (n - 1), pad n x (k + 1) * pad n x (k + 2)) =
      ∑ k ∈ Finset.range (n - 1), x k * x (k + 1) := by
    apply Finset.sum_congr rfl
    intro k hk
    have hk' := Finset.mem_range.mp hk
    simp [pad, show k < n by omega, show k + 1 < n by omega]
  have hq : (∑ k ∈ Finset.range n, pad n x (k + 1) ^ 2) =
      ∑ k ∈ Finset.range n, x k ^ 2 := by
    apply Finset.sum_congr rfl
    intro k hk; simp [pad, Finset.mem_range.mp hk]
  simpa only [he, hq] using h

/-- In particular, the issue's nonnegative-coordinate version holds. -/
theorem nonnegative_path_correlation {n : ℕ} (hn : 2 ≤ n) (x : ℕ → ℝ)
    (_hx : ∀ k < n, 0 ≤ x k) :
    (∑ k ∈ Finset.range (n - 1), x k * x (k + 1)) ≤
      pathConstant n * ∑ k ∈ Finset.range n, x k ^ 2 :=
  sharp_path_correlation hn x

/-- The source's zero-based sine vector is strictly positive at every vertex. -/
theorem sine_witness_positive {n k : ℕ} (hk : k < n) :
    0 < Real.sin (((k : ℝ) + 1) * (Real.pi / (n + 1))) := by
  simpa [sineState] using (sineState_pos (n := n) (k := k + 1) (by omega) (by omega))

/-- Exact equality at the positive sine vector, without numerical approximation. -/
theorem sine_witness_equality {n : ℕ} (hn : 2 ≤ n) :
    (∑ k ∈ Finset.range (n - 1), sineState n (k + 1) * sineState n (k + 2)) =
      pathConstant n * ∑ k ∈ Finset.range n, sineState n (k + 1) ^ 2 := by
  have h := path_eigenvector_equality (sineState n) (pathConstant n)
    (sineState_zero n) (sineState_end n) (fun _ _ => sineState_recurrence _ _)
  rwa [boundary_edges (by omega) (sineState n) (sineState_zero n) (sineState_end n)] at h

/-- The equality witness has nonzero energy, so its equality certifies optimality. -/
theorem sine_witness_energy_pos {n : ℕ} (hn : 2 ≤ n) :
    0 < ∑ k ∈ Finset.range n, sineState n (k + 1) ^ 2 := by
  apply Finset.sum_pos' (fun _ _ => sq_nonneg _)
  refine ⟨0, Finset.mem_range.mpr (by omega), ?_⟩
  exact sq_pos_of_pos (sineState_pos (by omega) (by omega))

/-- No smaller coefficient works uniformly, even restricted to nonnegative vectors. -/
theorem path_constant_optimal {n : ℕ} (hn : 2 ≤ n) {d : ℝ}
    (hd : ∀ x : ℕ → ℝ, (∀ k < n, 0 ≤ x k) →
      (∑ k ∈ Finset.range (n - 1), x k * x (k + 1)) ≤
        d * ∑ k ∈ Finset.range n, x k ^ 2) : pathConstant n ≤ d := by
  have h := hd (fun k => sineState n (k + 1))
    (fun k hk => (sineState_pos (by omega) (by omega)).le)
  rw [sine_witness_equality hn] at h
  exact (mul_le_mul_iff_left₀ (sine_witness_energy_pos hn)).mp h

/-- Only the upper half of the absolute-value premise is needed for this reserve. -/
theorem reserve_upper {S F I c : ℝ} (hcut : |F - S| ≤ I) (hcorr : I ≤ c * S) :
    F ≤ (1 + c) * S := by
  have h := (abs_le.mp hcut).2
  nlinarith

/-- Nonnegativity of c suffices; c<1 and nonnegativity of S,F,I are unnecessary. -/
theorem scalar_reserve {S F I c : ℝ} (hcut : |F - S| ≤ I) (hcorr : I ≤ c * S)
    (hc : 0 ≤ c) : F / (1 + c) ≤ S := by
  apply (div_le_iff₀ (by linarith : 0 < 1 + c)).mpr
  simpa only [mul_comm] using reserve_upper hcut hcorr

/-- Both sides of the cross-cut premise retain a two-sided scalar squeeze. -/
theorem reserve_squeeze {S F I c : ℝ} (hcut : |F - S| ≤ I) (hcorr : I ≤ c * S) :
    (1 - c) * S ≤ F ∧ F ≤ (1 + c) * S := by
  obtain ⟨hl, hu⟩ := abs_le.mp hcut
  constructor <;> nlinarith

theorem pathConstant_nonneg {n : ℕ} (hn : 2 ≤ n) : 0 ≤ pathConstant n := by
  unfold pathConstant
  apply Real.cos_nonneg_of_neg_pi_div_two_le_of_le
  · have h : 0 ≤ Real.pi / ((n : ℝ) + 1) := by positivity
    linarith [Real.pi_pos]
  · apply (div_le_iff₀ (by positivity : (0 : ℝ) < n + 1)).mpr
    have hn' : (2 : ℝ) ≤ n := by exact_mod_cast hn
    nlinarith [Real.pi_pos]

/-- WI-276's reserve conditional on its external correlation and cut identities. -/
theorem cosine_reserve {n : ℕ} (hn : 2 ≤ n) {S F I : ℝ}
    (hcut : |F - S| ≤ I) (hcorr : I ≤ pathConstant n * S) :
    F / (1 + pathConstant n) ≤ S :=
  scalar_reserve hcut hcorr (pathConstant_nonneg hn)

theorem pathConstant_two : pathConstant 2 = 1 / 2 := by
  norm_num [pathConstant, Real.cos_pi_div_three]

theorem pathConstant_three : pathConstant 3 = Real.sqrt 2 / 2 := by
  norm_num [pathConstant, Real.cos_pi_div_four]

/-- Exact two-vertex reserve regression: S ≥ 2F/3. -/
theorem two_vertex_reserve {S F I : ℝ}
    (hcut : |F - S| ≤ I) (hcorr : I ≤ pathConstant 2 * S) : 2 * F / 3 ≤ S := by
  have h := cosine_reserve (n := 2) (by omega) hcut hcorr
  rw [pathConstant_two] at h
  norm_num at h
  linarith

/-- Exact three-vertex correlation regression, with the radical coefficient. -/
theorem three_vertex_correlation (x : ℕ → ℝ) :
    x 0 * x 1 + x 1 * x 2 ≤ Real.sqrt 2 / 2 * (x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2) := by
  have h := sharp_path_correlation (n := 3) (by omega) x
  simpa [pathConstant_three, Finset.sum_range_succ] using h

#print axioms null_orthogonal
#print axioms three_piece_bounds
#print axioms sharp_path_correlation
#print axioms sine_witness_equality
#print axioms path_constant_optimal
#print axioms scalar_reserve
#print axioms cosine_reserve
#print axioms two_vertex_reserve

end Mathia.WI276
