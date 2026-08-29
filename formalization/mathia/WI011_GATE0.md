# WI-011 Gate 0: current finite splice audit

Controlling issue: [Mathia #74](https://github.com/murillo128/mathia/issues/74)

Status: `OBSERVED` fresh Gate-0 evidence on Mathia `main`
`e936a41da1dec54c03c61521c89a37d853bcb466`. Proposed verdict: `PASS_TO_PROOF`, subject to
the required independent review of this exact published target.

This document freezes the finite theorem surfaces before any Lean proof is added to Mathia. The
earlier qwen-lean artifact at `f0a725df855ef0147aaadb763065ad5030a59652` is reusable technical
evidence, not the controlling issue, current Gate, or delivery target.

## 1. Current source and bounded outcome

The current mathematical sources are:

- `research/weil_inertia/findings/WI-011-refined-four-point-envelope-improves-certified-bound.md`,
  last materially changed by `24226ee6142f604e21cfcb7c75f1b4a86b3b71fd`;
- `research/weil_inertia/findings/WI-009-kernel-checked-four-point-gram-defect-improves-bound.md`,
  last materially changed by `6cd37a34ca66624a9b397c508e3d73168614a230`;
- `research/weil_inertia/findings/WI-020-trace-energy-envelope-sharp-one-spike-extremizers.md`,
  last materially changed by `342402227212ad9c185ab18439b86a4917da27d5`.

Current WI-011 already contains the large-coordinate compression repair. This Gate formalizes
that repaired derivation, not the superseded shortcut that only proved `D > 2` for `k >= 2`.
WI-020 proves a sharper fixed-energy extremizer classification, but issue #74 does not require
that stronger theorem.

The accepted finite outcome is:

1. the scalar trace--energy envelope and nonnegative-pressure transfer;
2. exact four-point pair-spend accounting and the local-certificate-to-block implication;
3. exact finite window/shift containment and endpoint-loss statements;
4. the exact `epsilon = 231/100000`, `m = 438` branch and radical arithmetic;
5. a combined finite splice theorem whose local four-point certificate remains an explicit
   hypothesis.

The matrix spectral theorem, analytic zeta bridge, compact-uniform asymptotic, final decimal
simple-zero proportion, larger certificates, bound optimization, and RH are outside the formal
boundary.

## 2. Lean environment and dependency decision

Mathia has no Lean project or active default Elan toolchain at this Gate. The execution machine
has these installed toolchains:

```text
leanprover/lean4:v4.27.0
leanprover/lean4:v4.32.0
leanprover/lean4:v4.32.2
```

After Gate approval, the smallest coherent setup is a root `lean-toolchain`, a root
`lakefile.toml`, and two Lean files under `formalization/mathia/`. The initial implementation may
use the already installed Lean `v4.32.0` with Mathlib `v4.32.0` (source revision
`81a5d257c8e410db227a6665ed08f64fea08e997`). These versions are recorded execution evidence, not
a scientific acceptance gate; a mechanically necessary available-toolchain adjustment must be
reported without changing the frozen theorem surfaces.

The external `teal-sea/zeta-lab` package is not imported. At inspected revision
`c02ad1a56ce18d99c326d87e9318d064621d3fea`, its `four_point_cert` is sorry-free at the stated
surface, but its package depends by path on the larger zeta bridge and uses Lean
`v4.33.0-rc2`. Porting that dependency graph would exceed issue #74. The finite Mathia theorem
therefore takes the local certificate as a visibly parameterized hypothesis.

No matrix corollary is planned. Mathlib exposes Hermitian eigenvalues, trace as their sum, and
PSD eigenvalue nonnegativity, but connecting the piecewise scalar profile to matrix functional
calculus would add machinery not consumed by the finite splice. A theorem over
`lambda : Fin m -> Real` is the smallest truthful boundary.

## 3. Frozen Lean theorem surfaces

Names may receive only mechanically necessary argument-order or coercion adjustments. Their
mathematical hypotheses and conclusions are frozen.

### 3.1 Scalar trace--energy layer

```lean
namespace Mathia.WI011

def psi (t : Real) : Real :=
  if t <= 2 then (t - 1) ^ 2 else 2 * t - 3

def energy {m : Nat} (lambda : Fin m -> Real) : Real :=
  sum i, (lambda i - 1) ^ 2

def defect {m : Nat} (lambda : Fin m -> Real) : Real :=
  sum i, psi (lambda i)

def centered {m : Nat} (lambda : Fin m -> Real) (i : Fin m) : Real :=
  lambda i - 1

def largeSet {m : Nat} (lambda : Fin m -> Real) : Finset (Fin m) :=
  Finset.univ.filter fun i => 1 < centered lambda i

def phi (m : Nat) (E : Real) : Real :=
  if E <= (m : Real) / ((m : Real) - 1) then E
  else 2 * Real.sqrt ((((m : Real) - 1) / (m : Real)) * E) - 1
    + E / (m : Real)

theorem defect_eq_energy_add_large_correction
    {m : Nat} (lambda : Fin m -> Real) :
    defect lambda = energy lambda
      + 2 * (sum i in largeSet lambda, centered lambda i)
      - (largeSet lambda).card
      - (sum i in largeSet lambda, (centered lambda i) ^ 2)

theorem phi_monoOn_nonneg {m : Nat} (hm : 2 <= m) :
    MonotoneOn (phi m) (Set.Ici 0)

theorem phi_increment_le {m : Nat} (hm : 2 <= m)
    {x y : Real} (hx : 0 <= x) (hxy : x <= y) :
    phi m y <= phi m x + (y - x)

theorem traceEnergy_envelope {m : Nat} (hm : 2 <= m)
    (lambda : Fin m -> Real)
    (hlambda : forall i, 0 <= lambda i)
    (htrace : (sum i, lambda i) = m) :
    phi m (energy lambda) <= defect lambda

theorem traceEnergy_pressure {m : Nat} (hm : 2 <= m)
    (lambda : Fin m -> Real)
    (hlambda : forall i, 0 <= lambda i)
    (htrace : (sum i, lambda i) = m)
    {A P : Real} (hA : 0 <= A) (hP : 0 <= P)
    (hbudget : A <= energy lambda + P) :
    phi m A <= defect lambda + P
```

The pressure theorem deliberately has no unstated upper bound on `A`, `E`, or `P`. Its domain is
`m >= 2`, nonnegative eigenvalues of trace `m`, `A >= 0`, `P >= 0`, and `A <= E + P`.

### 3.2 Four-point and block layer

Write the number of block points as `m = q + 4`, so there are `q + 1 = m - 3` consecutive
four-point windows.

```lean
def fourPointPairSpend (w : Nat -> Nat -> Real) (s : Nat) : Real :=
  (2 / 3 : Real) *
      (w s (s + 1) + w (s + 1) (s + 2) + w (s + 2) (s + 3))
    + (w s (s + 2) + w (s + 1) (s + 3))
    + 2 * w s (s + 3)

def blockPairEnergy (q : Nat) (w : Nat -> Nat -> Real) : Real :=
  2 * sum r in Finset.range (q + 3),
        sum i in Finset.range (q + 3 - r), w i (i + r + 1)

theorem blockPairEnergy_eq_pairSum (q : Nat) (w : Nat -> Nat -> Real) :
    blockPairEnergy q w =
      2 * sum i in Finset.range (q + 4),
            sum j in Finset.Ico (i + 1) (q + 4), w i j

theorem fourPointPairSpend_sum_le_blockPairEnergy
    (q : Nat) (w : Nat -> Nat -> Real)
    (hw : forall i j, 0 <= w i j) :
    (sum s in Finset.range (q + 1), fourPointPairSpend w s)
      <= blockPairEnergy q w

theorem localCertificate_to_block
    (q : Nat) (w : Nat -> Nat -> Real) (pressure : Nat -> Real)
    (epsilon : Real)
    (hw : forall i j, 0 <= w i j)
    (hpressure : forall s, s < q + 1 -> 0 <= pressure s)
    (hcert : forall s, s < q + 1 ->
      epsilon <= fourPointPairSpend w s + pressure s) :
    epsilon * (q + 1) <=
      blockPairEnergy q w + sum s in Finset.range (q + 1), pressure s

theorem localCertificate_to_spectralDefect ... :
    phi (q + 4) (epsilon * (q + 1)) <=
      defect lambda + sum s in Finset.range (q + 1), pressure s
```

The pair weights are arbitrary and nonnegative. No translation invariance, symmetry, kernel
identity, or zeta-specific assumption is hidden in these statements. The combined theorem also
assumes that scalar `energy lambda` equals the generic block pair energy.

### 3.3 Exact finite shift and endpoint layer

```lean
def threeGapSpan (g : Nat -> Real) (s : Nat) : Real :=
  g s + g (s + 1) + g (s + 2)

theorem threeGapSpan_boundary_identity (q : Nat) (g : Nat -> Real) :
    3 * (sum j in Finset.range (q + 3), g j) =
      (sum s in Finset.range (q + 1), threeGapSpan g s)
        + 2 * g 0 + g 1 + g (q + 1) + 2 * g (q + 2)

def fourPointContainingOffsets (m : Nat) : Finset Nat :=
  (Finset.range m).filter fun a => a + 3 < m

theorem fourPoint_containing_shift_count {m : Nat} (hm : 4 <= m) :
    (fourPointContainingOffsets m).card = m - 3

def fullBlockOffsets (n q s : Nat) : Finset Nat :=
  (Finset.range (q + 1)).filter
    (fun t => t <= s && s - t + (q + 4) <= n)

theorem fullBlockOffsets_card_of_interior {n q s : Nat}
    (hleft : q <= s) (hright : s + q + 4 <= n) :
    (fullBlockOffsets n q s).card = q + 1

theorem exceptional_fourPoint_starts_card_le {n q : Nat} :
    (exceptionalFourPointStarts n q).card <= 2 * q

theorem finite_containment_incidence_with_boundary {n q : Nat} :
    (q + 1) * (n - 3) <=
      (sum s in Finset.range (n - 3), (fullBlockOffsets n q s).card)
        + 2 * q * (q + 1)
```

The endpoint identity intentionally retains repeated terms when `q = 0` (`m = 4`). The final
theorem exposes a literal finite loss `2q(q+1)` before any analytic `o(N)` passage.

### 3.4 Exact `m = 438` layer

```lean
def epsilon4 : Real := 231 / 100000
def A438 : Real := 20097 / 20000

theorem A438_eq : epsilon4 * (438 - 3) = A438
theorem A438_gt_branch : (438 : Real) / 437 < A438
theorem phi438_exact :
    phi 438 A438 =
      2 * Real.sqrt (8782389 / 8760000) - 1 + 20097 / 8760000
theorem phi438_interval :
    (1004848 / 1000000 : Real) < phi 438 A438
      /\ phi 438 A438 < 1004849 / 1000000
theorem phi438_lt_two : phi 438 A438 < 2

theorem wi011_m438_finite_splice ... :
    phi 438 A438 <= defect lambda +
      sum s in Finset.range 435, pressure s
```

The interval theorem is a small exact regression. No floating-point approximation is a proof
premise.

## 4. Adversarial mathematical audit

### 4.1 Trace--energy envelope

Set `x_i = lambda_i - 1`. Then `x_i >= -1`, `sum x_i = 0`, and
`E = sum x_i^2`. For `L = {i | x_i > 1}`, with `k = |L|`, `R = sum_L x_i`, and
`Q = sum_L x_i^2`, direct branch splitting gives

```text
D = E + 2R - k - Q.
```

- If `k = 0`, then `D = E`, and `phi_m(E) <= E`.
- If `k = 1`, let the large coordinate be `r`. Cauchy--Schwarz on the other `m-1`
  coordinates gives `m*r^2 <= (m-1)E`. The difference from the second envelope branch factors
  into nonnegative terms.
- If `k >= 2`, write each large coordinate as `1 + z_i`, `z_i > 0`, and set
  `Z = sum z_i`. Replace them by `1+Z, 1, ..., 1`. The trace and defect are unchanged, while
  energy increases by `Z^2 - sum z_i^2 >= 0`. The transformed vector has at most one coordinate
  above the branch threshold, so the valid `k <= 1` bound at energy `E'` and monotonicity of
  `phi_m` imply the global envelope at `E`.

This is the repaired current WI-011 route. The historical `k >= 2 => D > 2` shortcut remains
sufficient only for the fixed application where `phi_438(A438) < 2`; it is not used to prove the
global theorem.

At the branch `E = m/(m-1)`, both formulas equal `m/(m-1)`. On the nonnegative domain, `phi_m`
is nondecreasing and one-sided 1-Lipschitz. Therefore

```text
A <= E + P,  A >= 0,  P >= 0
=> phi_m(A) <= phi_m(E + P) <= phi_m(E) + P <= D + P.
```

No upper range for `A`, `E`, or `P` is needed.

### 4.2 Four-point and boundary accounting

WI-009's non-pressure coefficients are `2/3`, `1`, and `2` for pairs separated by one, two,
and three adjacent gaps. Such pairs occur in at most `3`, `2`, and `1` consecutive four-point
windows, so every total spend is at most `2`, the coefficient available in block energy.
Boundary pairs occur less often and create slack.

The three-gap identity keeps the exact endpoint loss

```text
2*g_0 + g_1 + g_(m-3) + 2*g_(m-2).
```

For `m = 4`, the two middle names refer to the same gap and must both remain. A fixed
four-point window is inside a block in exactly `m-3` of the `m` alignments. In a finite frame,
at most `2(m-4)` window starts are exceptional and at most
`2(m-4)(m-3)` containment incidences are lost.

### 4.3 Exact constant

Fresh rational computation gives

```text
(231/100000) * 435 = 20097/20000,
20097/20000 - 438/437 = 22389/8740000 > 0,
(437/438) * (20097/20000) = 8782389/8760000
                                  = 2927463/2920000.
```

Thus the square-root branch and exact radical are correct.

## 5. Executable falsification evidence

A fresh exact-rational quarter-grid enumeration checked all nonnegative spectra of trace `m` for
`m = 2,...,6`. The envelope comparison used rational squaring on the second branch, not floating
point.

| `m` | spectra | `k=0` | `k=1` | `k>=2` |
|---:|---:|---:|---:|---:|
| 2 | 9 | 9 | 0 | 0 |
| 3 | 91 | 61 | 30 | 0 |
| 4 | 969 | 489 | 480 | 0 |
| 5 | 10,626 | 3,951 | 6,525 | 150 |
| 6 | 118,755 | 32,661 | 79,164 | 6,930 |

All `130,450` spectra passed.

Direct small-block enumeration produced:

| `m` | gap-in-span multiplicities | pair multiplicities at separations `1;2;3` | containing shifts |
|---:|---|---|---:|
| 4 | `1,1,1` | `1,1,1 ; 1,1 ; 1` | 1 |
| 5 | `1,2,2,1` | `1,2,2,1 ; 1,2,1 ; 1,1` | 2 |
| 6 | `1,2,3,2,1` | `1,2,3,2,1 ; 1,2,2,1 ; 1,1,1` | 3 |

The finite exceptional-start and incidence inequalities were also exhaustively checked for
`q = 0,...,8` and `n = 0,...,20`. Exact rational squaring verified
`1.004848 < phi_438(A438) < 1.004849` and `phi_438(A438) < 2`.

These computations are falsification aids only. The delivered mathematical claims must be Lean
theorems.

## 6. Prior art and Mathlib reuse

The cited public revisions remain accessible:

| source | revision | classification |
|---|---|---|
| current Mathia WI-009/WI-011/WI-020 | Mathia `e936a41da1dec54c03c61521c89a37d853bcb466` | Scientific source. WI-011 includes the repaired compression; WI-020 is a stronger out-of-scope extremizer theorem. |
| `tawanerguo-cn/zeta-simple-zeros` | `45149f6d403059a71be73c5e3f884cee7cd62b20` | MIT prior art for the fixed-application trace--energy implication and window-in-frame accounting; no Lean source in the inspected tree. |
| `trmdy/zeta-simple-zeros-673137` | `0102fd8915c88fdd7c66231467745c17c0005fe4` | MIT independent prose rederivation using the same envelope/shift mechanism; no Lean implementation of the WI-011 splice. |
| `teal-sea/zeta-lab` | `c02ad1a56ce18d99c326d87e9318d064621d3fea` | MIT external `four_point_cert` and zeta bridge. The exact theorem surface is `forall g : Fin 3 -> Real, nonnegative g -> 2310/1000000 <= F 4 2500 g`. |
| qwen-lean PR #105 | `f0a725df855ef0147aaadb763065ad5030a59652` | Previously reviewed implementation evidence. It does not replace the fresh Mathia Gate, Mathia-native proof target, or final review. |

Fresh GitHub code searches for `wi011_m438_finite_splice`, the pair
`8782389 8760000`, and `four_point_cert` found no additional public implementation indexed by
those exact terms. Absence from code search is not a novelty proof. No novelty claim is made for
the envelope, compression, shift accounting, stability bridge, or local certificate.

The inspected Mathlib source supplies:

- `Finset.sq_sum_le_card_mul_sum_sq`;
- `Finset.sum_sq_le_sq_sum_of_nonneg`;
- finite ranges, intervals, filters, and big-operator identities;
- `Real.sqrt` order and square lemmas;
- `norm_num`, `linarith`, `nlinarith`, `ring_nf`, `field_simp`, and `omega`;
- optional matrix declarations `Matrix.IsHermitian.eigenvalues`,
  `Matrix.IsHermitian.trace_eq_sum_eigenvalues`, and `Matrix.PosSemidef.eigenvalues_nonneg`.

No new generic algebra, graph, matrix, certificate, or formalization framework is justified.

## 7. Gate verdict and research handoff

Proposed verdict: `PASS_TO_PROOF`.

The current finding, exact finite theorem surfaces, pressure domain, coefficient ledger,
small-frame endpoint behavior, exact constant, prior-art classification, and dependency boundary
survived the fresh audit. The earlier global-envelope defect is already repaired in current
WI-011 and is explicitly represented in the frozen theorem route.

Formalization research handoff: none. This Gate found no new material mathematical observation
beyond the already persisted WI-011 repair and the separately resolved WI-020 extremizer result.
Proof work remains blocked until an independent reviewer accepts this exact Gate target.
