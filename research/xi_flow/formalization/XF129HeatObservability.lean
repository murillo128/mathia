import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.Complex.Polynomial.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
# Upper-half Newton heat-history observability

Associated finding:
`research/xi_flow/findings/XF-129-upper-half-heat-histories-determine-unit-circle-divisors-up-to-central-rotation.md`.

Formalized boundary: finite diagonal heat/Newton observability under coefficient
self-inversivity, including the exceptional even central sign/rotation classification.
The normalized observable is defined by the finite Newton recurrence
`m A_m = m e_m - ∑_{0<k<m} k A_k e_(m-k)`; equivalently
`A_m = (-1)^(m-1) P_m / m`. No coefficient recovery is assumed.
Circle-rootedness implies the coefficient symmetry in the source, but that geometric
bridge is not formalized here. Root multisets, multiplicities and Lambda_per,
XF-128's negative construction, Xi source accessibility of degree-scale histories,
and any conclusion about the actual de Bruijn--Newman constant are outside this file.
-/

noncomputable section
open scoped BigOperators
open Filter Topology
namespace Mathia.XF129

/-- Subtraction is in ℝ, never truncated in ℕ. -/
def rate (N : ℕ) (α : ℝ) (k : ℕ) : ℝ := α * k * ((N : ℝ) - k)

theorem rate_add (N : ℕ) (α : ℝ) (a b : ℕ) :
    rate N α a + rate N α b - rate N α (a+b) = 2*α*a*b := by
  simp only [rate, Nat.cast_add]; ring

/-- The pair sum over an ordered composition, expressed recursively. -/
def pairs : List ℕ → ℕ
  | [] => 0
  | k :: ks => k * ks.sum + pairs ks

theorem composition_gap (N : ℕ) (α : ℝ) (ks : List ℕ) :
    (ks.map (rate N α)).sum - rate N α ks.sum = 2*α*(pairs ks : ℝ) := by
  induction ks with
  | nil => simp [rate, pairs]
  | cons k ks ih =>
    simp only [List.map_cons, List.sum_cons, pairs, Nat.cast_add, Nat.cast_mul]
    have h := rate_add N α k ks.sum
    push_cast at *
    linarith

theorem pairs_pos (ks : List ℕ) (hp : ∀ k ∈ ks, 0 < k) (hl : 2 ≤ ks.length) :
    0 < pairs ks := by
  match ks with
  | [] => simp at hl
  | [a] => simp at hl
  | a :: b :: ks =>
    have ha := hp a (by simp)
    have hb := hp b (by simp)
    simp only [pairs, List.sum_cons]
    positivity

theorem composition_gap_pos (N : ℕ) {α : ℝ} (ha : 0 < α)
    (ks : List ℕ) (hp : ∀ k ∈ ks, 0 < k) (hl : 2 ≤ ks.length) :
    rate N α ks.sum < (ks.map (rate N α)).sum := by
  have h := composition_gap N α ks
  have hpos : 0 < (pairs ks : ℝ) := Nat.cast_pos.mpr (pairs_pos ks hp hl)
  have : 0 < 2*α*(pairs ks : ℝ) := by positivity
  linarith

/-- Finite normalized Newton recurrence. The k=0 summand is identically zero. -/
def newton (e : ℕ → ℂ) : ℕ → ℂ
  | 0 => 0
  | m+1 => e (m+1) - (∑ k : Fin (m+1), (k.val : ℂ) * newton e k.val * e (m+1-k.val)) / (m+1 : ℕ)
termination_by m => m

theorem newton_eq (e : ℕ → ℂ) {m : ℕ} (hm : 0 < m) :
    newton e m = e m - (∑ k : Fin m, (k.val : ℂ) * newton e k.val * e (m-k.val)) / (m : ℂ) := by
  cases m with
  | zero => omega
  | succ m => rw [newton]

def heat (N : ℕ) (α : ℝ) (E : ℕ → ℂ) (s : ℝ) (k : ℕ) : ℂ :=
  E k * (Real.exp (-rate N α k*s) : ℂ)

def history (N : ℕ) (α : ℝ) (E : ℕ → ℂ) (m : ℕ) (s : ℝ) : ℂ :=
  newton (heat N α E s) m

@[simp] theorem heat_zero (N : ℕ) (α : ℝ) (E : ℕ → ℂ) : heat N α E 0 = E := by
  funext k; simp [heat]

/-- Finite-prefix dependence is proved, rather than assumed by the observable interface. -/
theorem newton_congr {e f : ℕ → ℂ} {m : ℕ}
    (h : ∀ k, 0 < k → k ≤ m → e k = f k) : newton e m = newton f m := by
  induction m using Nat.strong_induction_on with
  | h m ih =>
    rcases m.eq_zero_or_pos with rfl | hm
    · simp [newton]
    rw [newton_eq e hm, newton_eq f hm, h m hm le_rfl]
    congr 2
    apply Finset.sum_congr rfl
    intro k _
    by_cases hk : k.val = 0
    · simp [hk]
    rw [ih k.val k.isLt (fun j hj hjk => h j hj (by omega)), h (m-k.val) (by omega) (by omega)]

/-- A least active shell has normalized Newton coefficient equal to that shell. -/
theorem newton_of_vanishing {e : ℕ → ℂ} {r : ℕ} (hr : 0 < r)
    (h : ∀ k, 0 < k → k < r → e k = 0) : newton e r = e r := by
  rw [newton_eq e hr]
  have hz : (∑ k : Fin r, (k.val : ℂ) * newton e k.val * e (r-k.val)) = 0 := by
    apply Finset.sum_eq_zero
    intro k _
    by_cases hk : k.val = 0
    · simp [hk]
    rw [h (r-k.val) (by omega) (by omega), mul_zero]
  rw [hz]; simp

def expC (t : ℝ) : ℂ := (Real.exp t : ℂ)

@[simp] theorem expC_zero : expC 0 = 1 := by simp [expC]
theorem expC_add (a b : ℝ) : expC (a+b) = expC a * expC b := by
  simp [expC, Real.exp_add]

theorem expC_decay {d : ℝ} (hd : 0 < d) :
    Tendsto (fun s : ℝ => expC (-d*s)) atTop (𝓝 0) := by
  have h := Real.tendsto_exp_neg_atTop_nhds_zero.comp
    (tendsto_id.const_mul_atTop hd)
  simpa only [expC, Function.comp_def, id_eq, neg_mul, Complex.ofReal_zero] using Complex.continuous_ofReal.continuousAt.tendsto.comp h

theorem scaled_product (N : ℕ) (α : ℝ) (E : ℕ → ℂ) (m k : ℕ) (s : ℝ) :
    expC (rate N α m*s) * (history N α E k s * heat N α E s (m-k)) =
    (expC (rate N α k*s) * history N α E k s) * E (m-k) *
      expC (-(rate N α k + rate N α (m-k) - rate N α m)*s) := by
  change expC _ * (history N α E k s * (E (m-k) * expC _)) = _
  have h : expC (rate N α m*s) * expC (-rate N α (m-k)*s) =
      expC (rate N α k*s) * expC (-(rate N α k + rate N α (m-k) - rate N α m)*s) := by
    rw [← expC_add, ← expC_add]
    congr 1; ring
  calc
    _ = (expC (rate N α m*s) * expC (-rate N α (m-k)*s)) *
        history N α E k s * E (m-k) := by ring
    _ = _ := by rw [h]; ring

/-- The scaled Newton tail recovers its coefficient, including the terminal degree.
The proof inducts through the triangular recurrence and uses strict binary rate gaps. -/
theorem tail_recovery (N : ℕ) {α : ℝ} (ha : 0 < α) (E : ℕ → ℂ)
    (m : ℕ) (hm : 0 < m) :
    Tendsto (fun s : ℝ => expC (rate N α m*s) * history N α E m s)
      atTop (𝓝 (E m)) := by
  induction m using Nat.strong_induction_on with
  | h m ih =>
    have hterm (k : Fin m) :
        Tendsto (fun s : ℝ => expC (rate N α m*s) *
          ((k.val : ℂ) * history N α E k.val s * heat N α E s (m-k.val)))
          atTop (𝓝 0) := by
      by_cases hk : k.val = 0
      · simp [hk]
      have hkp : 0 < k.val := by omega
      have hrp : 0 < m-k.val := by omega
      have hgap : 0 < rate N α k.val + rate N α (m-k.val) - rate N α m := by
        have hg := rate_add N α k.val (m-k.val)
        rw [Nat.add_sub_of_le (Nat.le_of_lt k.isLt)] at hg
        rw [hg]
        positivity
      have ht := ((ih k.val k.isLt hkp).mul_const (E (m-k.val))).mul (expC_decay hgap)
      have ht' := ht.const_mul (k.val : ℂ)
      simp only [mul_zero] at ht'
      apply ht'.congr
      intro s
      rw [← scaled_product]
      ring
    have hs := tendsto_finsetSum Finset.univ (fun k _ => hterm k)
    have heq (s : ℝ) :
        expC (rate N α m*s) * history N α E m s = E m -
        (∑ k : Fin m, expC (rate N α m*s) *
          ((k.val : ℂ) * history N α E k.val s * heat N α E s (m-k.val))) / (m : ℂ) := by
      unfold history
      rw [newton_eq _ hm, mul_sub, ← mul_div_assoc, Finset.mul_sum]
      congr 1
      change expC _ * (E m * expC _) = E m
      rw [mul_left_comm, ← expC_add]
      have : rate N α m*s + -rate N α m*s = 0 := by ring
      rw [this, expC_zero, mul_one]
    have ht := (tendsto_const_nhds (x := E m)).sub (hs.div_const (m : ℂ))
    simp only [Finset.sum_const_zero, zero_div, sub_zero] at ht
    exact ht.congr (fun s => (heq s).symm)

theorem terminal_recovery {N : ℕ} (hN : 0 < N) {α : ℝ} (ha : 0 < α)
    (E : ℕ → ℂ) : Tendsto (history N α E N) atTop (𝓝 (E N)) := by
  simpa [rate] using tail_recovery N ha E N hN

def SameHistories (N : ℕ) (α : ℝ) (E F : ℕ → ℂ) : Prop :=
  ∀ m, N < 2*m → m ≤ N → ∀ s : ℝ, 0 ≤ s → history N α E m s = history N α F m s

theorem high_coefficients {N : ℕ} {α : ℝ} (ha : 0 < α) {E F : ℕ → ℂ}
    (h : SameHistories N α E F) {m : ℕ} (hm : N < 2*m) (hmN : m ≤ N) :
    E m = F m := by
  have he : (fun s : ℝ => expC (rate N α m*s) * history N α E m s) =ᶠ[atTop]
      (fun s : ℝ => expC (rate N α m*s) * history N α F m s) := by
    filter_upwards [eventually_ge_atTop (0 : ℝ)] with s hs
    rw [h m hm hmN s hs]
  exact tendsto_nhds_unique (tail_recovery N ha E m (by omega))
    ((tail_recovery N ha F m (by omega)).congr' he.symm)

/-- Coefficient self-inversivity, restricted to the polynomial degree. -/
def SelfInversive (N : ℕ) (E : ℕ → ℂ) : Prop :=
  E 0 = 1 ∧ ∀ k, k ≤ N → E (N-k) = E N * star (E k)

theorem noncentral_coefficients {N : ℕ} (hN : 0 < N) {α : ℝ} (ha : 0 < α)
    {E F : ℕ → ℂ} (he : SelfInversive N E) (hf : SelfInversive N F)
    (hh : SameHistories N α E F) {k : ℕ} (hk : k ≤ N) (hnc : 2*k ≠ N) :
    E k = F k := by
  have htop := high_coefficients ha hh (m := N) (by omega) le_rfl
  rcases lt_or_gt_of_ne hnc with hlo | hhi
  · have hhigh := high_coefficients ha hh (m := N-k) (by omega) (by omega)
    have he' := he.2 (N-k) (by omega)
    have hf' := hf.2 (N-k) (by omega)
    rw [Nat.sub_sub_self hk] at he' hf'
    rw [he', hf', htop, hhigh]
  · exact high_coefficients ha hh hhi hk

theorem odd_injectivity {N : ℕ} (hodd : Odd N) {α : ℝ} (ha : 0 < α)
    {E F : ℕ → ℂ} (he : SelfInversive N E) (hf : SelfInversive N F)
    (hh : SameHistories N α E F) : ∀ k, k ≤ N → E k = F k := by
  obtain ⟨n, hn⟩ := hodd
  intro k hk
  exact noncentral_coefficients (by omega) ha he hf hh hk (by omega)

theorem newton_zero {e : ℕ → ℂ} {m : ℕ}
    (h : ∀ k, 0 < k → k ≤ m → e k = 0) : newton e m = 0 := by
  rcases m.eq_zero_or_pos with rfl | hm
  · simp [newton]
  rw [newton_of_vanishing hm (fun k hk hkm => h k hk (by omega)), h m hm le_rfl]

/-- Before the first cross-shell interaction, changing only shell c changes no other
normalized Newton coefficient. All hypotheses refer to coefficients, not observables. -/
theorem difference_below {e f : ℕ → ℂ} {c r : ℕ} (_hr : 0 < r) (hrc : r < c)
    (heq : ∀ k, 0 < k → k ≤ c+r → k ≠ c → e k = f k)
    (hz : ∀ k, 0 < k → k < r → e k = 0)
    {n : ℕ} (hn : n < c+r) (hnc : n ≠ c) : newton e n = newton f n := by
  have hzf : ∀ k, 0 < k → k < r → f k = 0 := by
    intro k hk hkr
    rw [← heq k hk (by omega) (by omega), hz k hk hkr]
  induction n using Nat.strong_induction_on with
  | h n ih =>
    rcases n.eq_zero_or_pos with rfl | hnp
    · simp [newton]
    rw [newton_eq e hnp, newton_eq f hnp, heq n hnp (by omega) hnc]
    congr 2
    apply Finset.sum_congr rfl
    intro k _
    by_cases hk0 : k.val = 0
    · simp [hk0]
    by_cases hkc : k.val = c
    · have hsmall : n-k.val < r := by omega
      rw [hz (n-k.val) (by omega) hsmall, hzf (n-k.val) (by omega) hsmall]
      simp
    by_cases hrest : n-k.val = c
    · have hsmall : k.val < r := by omega
      have hze : newton e k.val = 0 := newton_zero (fun j hj hjk => hz j hj (by omega))
      have hzf' : newton f k.val = 0 := newton_zero (fun j hj hjk => hzf j hj (by omega))
      rw [hze, hzf']; simp
    rw [ih k.val k.isLt (by omega) hkc,
      heq (n-k.val) (by omega) (by omega) hrest]

theorem difference_at_center {e f : ℕ → ℂ} {c : ℕ} (hc : 0 < c)
    (heq : ∀ k, 0 < k → k < c → e k = f k) :
    newton e c - newton f c = e c - f c := by
  rw [newton_eq e hc, newton_eq f hc]
  have hsum : (∑ k : Fin c, (k.val : ℂ) * newton e k.val * e (c-k.val)) =
      ∑ k : Fin c, (k.val : ℂ) * newton f k.val * f (c-k.val) := by
    apply Finset.sum_congr rfl
    intro k _
    by_cases hk : k.val = 0
    · simp [hk]
    rw [newton_congr (fun j hj hjk => heq j hj (by omega)),
      heq (c-k.val) (by omega) (by omega)]
  rw [hsum]; ring

/-- The exact least-active-shell identity at c+r; the two ordered quadratic
contributions have weights c and r, which sum to the Newton denominator. -/
theorem least_shell_difference {e f : ℕ → ℂ} {c r : ℕ} (hr : 0 < r) (hrc : r < c)
    (heq : ∀ k, 0 < k → k ≤ c+r → k ≠ c → e k = f k)
    (hz : ∀ k, 0 < k → k < r → e k = 0) :
    newton e (c+r) - newton f (c+r) = -(e c-f c)*e r := by
  have hcr : 0 < c+r := by omega
  have hzf : ∀ k, 0 < k → k < r → f k = 0 := by
    intro k hk hkr
    rw [← heq k hk (by omega) (by omega), hz k hk hkr]
  have hcenter := difference_at_center (c := c) (e := e) (f := f) (by omega)
    (fun k hk hkc => heq k hk (by omega) (by omega))
  have hrnew : newton f r = e r := by
    rw [newton_of_vanishing hr hzf, ← heq r hr (by omega) (by omega)]
  let u : Fin (c+r) := ⟨c, by omega⟩
  let v : Fin (c+r) := ⟨r, by omega⟩
  have huv : u ≠ v := by intro h; have := congrArg Fin.val h; simp [u,v] at this; omega
  have hs : (∑ k : Fin (c+r),
      ((k.val : ℂ) * newton e k.val * e (c+r-k.val) -
        (k.val : ℂ) * newton f k.val * f (c+r-k.val))) =
      (c+r : ℕ)*(e c-f c)*e r := by
    calc
      _ = ∑ k ∈ ({u,v} : Finset (Fin (c+r))),
          ((k.val : ℂ) * newton e k.val * e (c+r-k.val) -
            (k.val : ℂ) * newton f k.val * f (c+r-k.val)) := by
        symm
        apply Finset.sum_subset (Finset.subset_univ _)
        intro k _ hnot
        have hkc : k.val ≠ c := by
          intro h; apply hnot; simp [show k = u from Fin.ext h]
        have hkr : k.val ≠ r := by
          intro h; apply hnot; simp [show k = v from Fin.ext h]
        by_cases hk0 : k.val = 0
        · simp [hk0]
        rw [difference_below hr hrc heq hz (by omega) hkc,
          heq (c+r-k.val) (by omega) (by omega) (by omega)]
        ring
      _ = _ := by
        rw [Finset.sum_pair huv]
        simp only [u, v, Nat.add_sub_cancel_left, Nat.add_sub_cancel_right]
        rw [← heq r hr (by omega) (by omega),
          difference_below hr hrc heq hz (n := r) (by omega) (by omega), hrnew]
        push_cast
        linear_combination (c : ℂ) * e r * hcenter
  rw [newton_eq e hcr, newton_eq f hcr,
    ← heq (c+r) hcr le_rfl (by omega)]
  have hden : (c+r : ℂ) ≠ 0 := by exact_mod_cast (show c+r ≠ 0 by omega)
  rw [Finset.sum_sub_distrib] at hs
  push_cast at hs
  push_cast
  field_simp [hden]
  linear_combination -hs

theorem least_shell_heat_difference {c r : ℕ} (hr : 0 < r) (hrc : r < c)
    (α : ℝ) {E F : ℕ → ℂ}
    (heq : ∀ k, 0 < k → k ≤ c+r → k ≠ c → E k = F k)
    (hz : ∀ k, 0 < k → k < r → E k = 0) (s : ℝ) :
    history (2*c) α E (c+r) s - history (2*c) α F (c+r) s =
      -(E c-F c)*E r*expC (-(rate (2*c) α c+rate (2*c) α r)*s) := by
  have h := least_shell_difference hr hrc
    (e := heat (2*c) α E s) (f := heat (2*c) α F s)
    (by intro k hk hkb hkc; simp only [heat, heq k hk hkb hkc])
    (by intro k hk hkr; simp [heat, hz k hk hkr])
  change _ = _ at h
  rw [show history (2*c) α E (c+r) s - history (2*c) α F (c+r) s =
    -(heat (2*c) α E s c-heat (2*c) α F s c)*heat (2*c) α E s r from h]
  change -(E c*expC _-F c*expC _)*(E r*expC _) = _
  rw [neg_add, add_mul, expC_add]
  ring

theorem even_active_injectivity {c : ℕ} (hc : 0 < c) {α : ℝ} (ha : 0 < α)
    {E F : ℕ → ℂ} (he : SelfInversive (2*c) E) (hf : SelfInversive (2*c) F)
    (hh : SameHistories (2*c) α E F)
    (hactive : ∃ r, 0 < r ∧ r < c ∧ E r ≠ 0) :
    ∀ k, k ≤ 2*c → E k = F k := by
  have heq : ∀ k, k ≤ 2*c → k ≠ c → E k = F k := by
    intro k hk hkc
    exact noncentral_coefficients (by omega) ha he hf hh hk (by omega)
  let r := Nat.find hactive
  have hr := Nat.find_spec hactive
  change 0 < r ∧ r < c ∧ E r ≠ 0 at hr
  have hz : ∀ k, 0 < k → k < r → E k = 0 := by
    intro k hk hkr
    have hmin := Nat.find_min hactive hkr
    by_contra hne
    exact hmin ⟨hk, by omega, hne⟩
  have hid := least_shell_difference hr.1 hr.2.1
    (fun k _ hk hkc => heq k (by omega) hkc) hz
  have hequal := hh (c+r) (by omega) (by omega) 0 le_rfl
  simp only [history, heat_zero] at hequal
  rw [hequal, sub_self] at hid
  have hcentral : E c = F c := by
    have hp : (E c-F c)*E r = 0 := by linear_combination hid
    exact sub_eq_zero.mp ((mul_eq_zero.mp hp).resolve_right hr.2.2)
  intro k hk
  by_cases hkc : k = c
  · simpa [hkc] using hcentral
  · exact heq k hk hkc

/-- Only the central shell may be active among proper positive coefficients. -/
def CentralOnly (c : ℕ) (e : ℕ → ℂ) : Prop :=
  ∀ k, 0 < k → k < 2*c → k ≠ c → e k = 0

theorem central_newton_below {c : ℕ} (_hc : 0 < c) {e : ℕ → ℂ}
    (hz : CentralOnly c e) {n : ℕ} (hn : 0 < n) (hnc : n < 2*c) :
    newton e n = e n := by
  rw [newton_eq e hn]
  have hs : (∑ k : Fin n, (k.val : ℂ)*newton e k.val*e (n-k.val)) = 0 := by
    apply Finset.sum_eq_zero
    intro k _
    by_cases hk : k.val = 0
    · simp [hk]
    by_cases hrest : n-k.val = c
    · have hsmall : k.val < c := by omega
      have hnz : newton e k.val = 0 := newton_zero (by
        intro j hj hjk
        exact hz j hj (by omega) (by omega))
      rw [hnz]; ring
    · rw [hz (n-k.val) (by omega) (by omega) hrest, mul_zero]
  rw [hs]; simp

/-- At the terminal shell the sole nonlinear contribution is -C²/2. -/
theorem central_newton_terminal {c : ℕ} (hc : 0 < c) {e : ℕ → ℂ}
    (hz : CentralOnly c e) : newton e (2*c) = e (2*c) - e c^2/2 := by
  rw [newton_eq e (by omega)]
  have hs : (∑ k : Fin (2*c), (k.val : ℂ)*newton e k.val*e (2*c-k.val)) =
      (c : ℂ)*e c^2 := by
    rw [Finset.sum_eq_single (⟨c, by omega⟩ : Fin (2*c))]
    · simp only [show 2*c-c=c by omega]
      rw [central_newton_below hc hz hc (by omega)]; ring
    · intro k _ hkc
      by_cases hk : k.val = 0
      · simp [hk]
      have hknc : k.val ≠ c := by intro h; exact hkc (Fin.ext h)
      rw [hz (2*c-k.val) (by omega) (by omega) (by omega), mul_zero]
    · simp
  rw [hs]
  have hc0 : (c : ℂ) ≠ 0 := by exact_mod_cast hc.ne'
  push_cast
  field_simp

theorem heat_centralOnly {c : ℕ} {E : ℕ → ℂ} (hz : CentralOnly c E) (α s : ℝ) :
    CentralOnly c (heat (2*c) α E s) := by
  intro k hk hkn hkc
  simp [heat, hz k hk hkn hkc]

theorem central_terminal_history {c : ℕ} (hc : 0 < c) {E : ℕ → ℂ}
    (hz : CentralOnly c E) (α s : ℝ) :
    history (2*c) α E (2*c) s =
      E (2*c) - E c^2/2 * expC (-(2*rate (2*c) α c)*s) := by
  unfold history
  rw [central_newton_terminal hc (heat_centralOnly hz α s)]
  have ht : heat (2*c) α E s (2*c) = E (2*c) := by simp [heat, rate]
  rw [ht]
  change _ - (E c * expC _)^2/2 = _
  rw [show -(2*rate (2*c) α c)*s = -rate (2*c) α c*s + -rate (2*c) α c*s by ring,
    expC_add]
  ring

theorem central_square {c : ℕ} (hc : 0 < c) {α : ℝ} (ha : 0 < α)
    {E F : ℕ → ℂ} (he : CentralOnly c E) (hf : CentralOnly c F)
    (hh : SameHistories (2*c) α E F) : E c^2 = F c^2 := by
  have htop := high_coefficients ha hh (m := 2*c) (by omega) le_rfl
  have h := hh (2*c) (by omega) le_rfl 0 le_rfl
  rw [central_terminal_history hc he, central_terminal_history hc hf, htop] at h
  simp only [mul_zero, expC_zero, mul_one] at h
  linear_combination -2*h

/-- Equal top coefficient and equal central square suffice for all observed histories. -/
theorem central_sameHistories {c : ℕ} (hc : 0 < c) (α : ℝ) {E F : ℕ → ℂ}
    (he : CentralOnly c E) (hf : CentralOnly c F)
    (htop : E (2*c) = F (2*c)) (hsq : E c^2 = F c^2) :
    SameHistories (2*c) α E F := by
  intro m hm hmN s _
  by_cases hmn : m = 2*c
  · rw [hmn, central_terminal_history hc he, central_terminal_history hc hf, htop, hsq]
  · have hml : m < 2*c := by omega
    unfold history
    rw [central_newton_below hc (heat_centralOnly he α s) (by omega) hml,
      central_newton_below hc (heat_centralOnly hf α s) (by omega) hml]
    simp [heat, he m (by omega) hml (by omega), hf m (by omega) hml (by omega)]

/-- Reflection fills in the upper vanishing shells as well. -/
theorem centralOnly_of_lower_zero {c : ℕ} {E : ℕ → ℂ}
    (he : SelfInversive (2*c) E) (hz : ∀ r, 0 < r → r < c → E r = 0) :
    CentralOnly c E := by
  intro k hk hkn hkc
  by_cases hkl : k < c
  · exact hz k hk hkl
  · have hlow : 0 < 2*c-k ∧ 2*c-k < c := by omega
    have hs := he.2 (2*c-k) (by omega)
    rw [Nat.sub_sub_self (by omega), hz (2*c-k) hlow.1 hlow.2] at hs
    simpa using hs

/-- This is the sole possible nonidentity ambiguity. -/
def CentralFlip (c : ℕ) (E F : ℕ → ℂ) : Prop :=
  CentralOnly c E ∧ CentralOnly c F ∧ F (2*c) = E (2*c) ∧ F c = -E c

theorem even_classification {c : ℕ} (hc : 0 < c) {α : ℝ} (ha : 0 < α)
    {E F : ℕ → ℂ} (he : SelfInversive (2*c) E) (hf : SelfInversive (2*c) F) :
    SameHistories (2*c) α E F ↔
      (∀ k, k ≤ 2*c → E k = F k) ∨ CentralFlip c E F := by
  constructor
  · intro hh
    by_cases hactive : ∃ r, 0 < r ∧ r < c ∧ E r ≠ 0
    · exact Or.inl (even_active_injectivity hc ha he hf hh hactive)
    have hz : ∀ r, 0 < r → r < c → E r = 0 := by
      intro r hr hrc
      by_contra hne
      exact hactive ⟨r, hr, hrc, hne⟩
    have hec := centralOnly_of_lower_zero he hz
    have heq : ∀ k, k ≤ 2*c → k ≠ c → E k = F k := by
      intro k hk hkc
      exact noncentral_coefficients (by omega) ha he hf hh hk (by omega)
    have hfc : CentralOnly c F := by
      intro k hk hkn hkc
      rw [← heq k (by omega) hkc, hec k hk hkn hkc]
    have hsq := central_square hc ha hec hfc hh
    rcases sq_eq_sq_iff_eq_or_eq_neg.mp hsq with hplus | hminus
    · left
      intro k hk
      by_cases hkc : k = c
      · simpa [hkc] using hplus
      · exact heq k hk hkc
    · right
      exact ⟨hec, hfc, (heq (2*c) le_rfl (by omega)).symm, by linear_combination hminus⟩
  · rintro (heq | hflip)
    · intro m _ hm s _
      apply newton_congr
      intro k _ hkm
      simp only [heat, heq k (by omega)]
    · apply central_sameHistories hc α hflip.1 hflip.2.1 hflip.2.2.1.symm
      rw [hflip.2.2.2]; ring

/-- The upper-half history map is injective modulo precisely the exceptional central
sign flip. The reverse implication certifies that the exception is an actual ambiguity. -/
theorem upper_half_classification {N : ℕ} (hN : 0 < N) {α : ℝ} (ha : 0 < α)
    {E F : ℕ → ℂ} (he : SelfInversive N E) (hf : SelfInversive N F) :
    SameHistories N α E F ↔
      (∀ k, k ≤ N → E k = F k) ∨ ∃ c, N = 2*c ∧ CentralFlip c E F := by
  rcases Nat.even_or_odd N with heven | hodd
  · obtain ⟨c, hc⟩ := heven
    have hNc : N = 2*c := by omega
    clear hc
    subst N
    rw [even_classification (by omega) ha he hf]
    constructor
    · rintro (h | h)
      · exact Or.inl h
      · exact Or.inr ⟨c, rfl, h⟩
    · rintro (h | ⟨d, hd, h⟩)
      · exact Or.inl h
      · have : c = d := by omega
        subst d; exact Or.inr h
  · constructor
    · intro hh
      exact Or.inl (odd_injectivity hodd ha he hf hh)
    · rintro (heq | ⟨c, hc, _⟩)
      · intro m _ hm s _
        apply newton_congr
        intro k _ hkm
        simp only [heat, heq k (by omega)]
      · obtain ⟨d, hd⟩ := hodd
        omega

/-- Exact existence of a unit-circle rotation; no numerical trigonometry is used. -/
theorem exists_central_rotation {c : ℕ} (hc : 0 < c) :
    ∃ ω : ℂ, ω^c = -1 ∧ ω^(2*c) = 1 ∧ ‖ω‖ = 1 := by
  obtain ⟨ω, hω⟩ := IsAlgClosed.exists_pow_nat_eq (-1 : ℂ) hc
  have htop : ω^(2*c) = 1 := by
    rw [Nat.mul_comm 2 c, pow_mul, hω]; norm_num
  exact ⟨ω, hω, htop, Complex.norm_eq_one_of_pow_eq_one htop (by omega)⟩

/-- Diagonal heat flow commutes with coefficient-level rotation at every real time. -/
theorem heat_rotation (N : ℕ) (α : ℝ) (E : ℕ → ℂ) (ω : ℂ) (s : ℝ) (k : ℕ) :
    heat N α (fun j => ω^j*E j) s k = ω^k * heat N α E s k := by
  simp only [heat]; ring

theorem central_flip_rotation {c : ℕ} (hc : 0 < c) {E F : ℕ → ℂ}
    (he0 : E 0 = 1) (hf0 : F 0 = 1) (hflip : CentralFlip c E F) (α : ℝ) :
    ∃ ω : ℂ, ω^c = -1 ∧ ω^(2*c) = 1 ∧ ‖ω‖ = 1 ∧
      ∀ s : ℝ, ∀ k, k ≤ 2*c → heat (2*c) α F s k = ω^k*heat (2*c) α E s k := by
  obtain ⟨ω, hωc, hωN, hnorm⟩ := exists_central_rotation hc
  refine ⟨ω, hωc, hωN, hnorm, ?_⟩
  intro s k hk
  have hcoeff : F k = ω^k*E k := by
    by_cases hk0 : k = 0
    · simp [hk0, he0, hf0]
    by_cases hkc : k = c
    · simpa [hkc, hωc] using hflip.2.2.2
    by_cases hkN : k = 2*c
    · simpa [hkN, hωN] using hflip.2.2.1
    rw [hflip.1 k (by omega) (by omega) hkc,
      hflip.2.1 k (by omega) (by omega) hkc, mul_zero]
  simp only [heat, hcoeff]; ring

/-- A concise geometric-free consequence: identical observed histories imply identical
coefficient heat trajectories up to a fixed unit-circle rotation. The exact exceptional
support and sign are additionally classified by `upper_half_classification`. -/
theorem upper_half_rotation {N : ℕ} (hN : 0 < N) {α : ℝ} (ha : 0 < α)
    {E F : ℕ → ℂ} (he : SelfInversive N E) (hf : SelfInversive N F)
    (hh : SameHistories N α E F) :
    ∃ ω : ℂ, ‖ω‖ = 1 ∧ ∀ s : ℝ, ∀ k, k ≤ N →
      heat N α F s k = ω^k * heat N α E s k := by
  rcases (upper_half_classification hN ha he hf).mp hh with heq | ⟨c, hNc, hflip⟩
  · refine ⟨1, by simp, ?_⟩
    intro s k hk
    simp [heat, heq k hk]
  · subst N
    obtain ⟨ω, _, _, hnorm, hrot⟩ := central_flip_rotation (by omega) he.1 hf.1 hflip α
    exact ⟨ω, hnorm, hrot⟩

end Mathia.XF129
