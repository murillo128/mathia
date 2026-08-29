# PF-091 finite weighted-path memory: Gate 0

This is the blocking statement, adversarial, prior-art, and Mathlib-reuse gate
for Mathia issue #75.  It freezes only the finite weighted-path/Feshbach core of
PF-080, PF-081, and PF-091.  No Lean proof may be added on this branch until a
fresh independent review accepts this gate.

## Recommendation

`PORT_REUSE_PASS`, subject to independent review.

The exact finite theorem chain already exists as the child execution artifact
[murillo128/qwen-lean#103](https://github.com/murillo128/qwen-lean/pull/103)
at reviewed head `ca9902e052904391ad403d16c2b0b7f680ed6b6d`.  That repository is
not scientific authority for the claim.  It is an exact prior formalization to
port into Mathia after this gate passes, with Mathia issue #75 controlling the
statement, scope, evidence, and research handoff.

## Formal boundary

The accepted Lean file will establish:

1. the characteristic factorization of the three-vertex weighted path and the
   displayed positive eigenvalues
   `a + b ± sqrt (a^2 - a*b + b^2)` for `a,b > 0`;
2. the right-hand dimensionless limit with coefficient `-3/8`, plus the scaled
   normalization by `b^2/a` for fixed `a > 0`;
3. normalization and orthogonality of the two Feshbach modes and the squared
   coupling coefficient `3/4`;
4. the endpoint-minus-average weak equation, energy identity, and exact weighted
   path resistance formula with positive conductances and the centered source
   exposed;
5. deterministic `j = 2,3,4` indexing corollaries and the `j = 2` bookkeeping
   identity `-3*b^2/(8*a)`.

It will not establish:

- a Moore--Penrose inverse theory or a theorem stated using an unqualified
  pseudoinverse;
- arbitrary-`j` Feshbach eigenvalue asymptotics or hierarchy dominance;
- Burger's surface approximation, collar/PDE error estimates, or promotion of
  a graph coefficient to the true hyperbolic spectrum;
- prime-gap realization, scattering consequences, novelty, or RH consequences;
- correctness of surrounding PF-080/PF-081/PF-091 claims outside the finite
  declarations below.

## Frozen declaration surfaces

The file will use zero-based `Fin` indices: `n` edges mean `n + 1` vertices and
Lean edge `e : Fin n` is mathematical edge `m = e.val + 1`.  Namespace or path
qualification may change harmlessly; the following mathematical statements may
not be weakened during proof engineering.

```lean
def weightedPath3 (a b : ℝ) : Matrix (Fin 3) (Fin 3) ℝ
def muMinus (a b : ℝ) : ℝ
def muPlus (a b : ℝ) : ℝ
def IsEigenvalue (M : Matrix (Fin 3) (Fin 3) ℝ) (mu : ℝ) : Prop

theorem weightedPath3_characteristic_factor (a b lambda : ℝ) :
    (lambda • (1 : Matrix (Fin 3) (Fin 3) ℝ) - weightedPath3 a b).det =
      lambda * (lambda ^ 2 - 2 * (a + b) * lambda + 3 * a * b)

theorem zero_isEigenvalue (a b : ℝ) : IsEigenvalue (weightedPath3 a b) 0
theorem muMinus_isEigenvalue (ha : 0 < a) (hb : 0 < b) :
    IsEigenvalue (weightedPath3 a b) (muMinus a b)
theorem muPlus_isEigenvalue (ha : 0 < a) (hb : 0 < b) :
    IsEigenvalue (weightedPath3 a b) (muPlus a b)
theorem muMinus_pos (ha : 0 < a) (hb : 0 < b) : 0 < muMinus a b
theorem muMinus_lt_muPlus (ha : 0 < a) (hb : 0 < b) :
    muMinus a b < muPlus a b

def h (r : ℝ) : ℝ := 1 + r - Real.sqrt (1 - r + r ^ 2)
theorem h_quadratic_limit :
    Tendsto (fun r => (h r - (3 / 2) * r) / r ^ 2)
      (𝓝[>] (0 : ℝ)) (𝓝 (-3 / 8 : ℝ))
theorem muMinus_scaled_limit (a : ℝ) (ha : 0 < a) :
    Tendsto
      (fun b => (muMinus a b - (3 / 2) * b) / (b ^ 2 / a))
      (𝓝[>] (0 : ℝ)) (𝓝 (-3 / 8 : ℝ))

def feshbachU : Fin 3 → ℝ
def feshbachPsi : Fin 3 → ℝ
def weakEdgeMatrix : Matrix (Fin 3) (Fin 3) ℝ
theorem feshbachU_norm_sq : feshbachU ⬝ᵥ feshbachU = 1
theorem feshbachPsi_norm_sq : feshbachPsi ⬝ᵥ feshbachPsi = 1
theorem feshbachU_orthogonal_psi : feshbachU ⬝ᵥ feshbachPsi = 0
theorem feshbach_overlap_sq :
    |feshbachU ⬝ᵥ (weakEdgeMatrix *ᵥ feshbachPsi)| ^ 2 = 3 / 4

def pathCurrent (n : ℕ) (e : Fin n) : ℝ
def pathPotential {n : ℕ} (w : Fin n → ℝ) : Fin (n + 1) → ℝ
def pathEnergy {n : ℕ} (w : Fin n → ℝ) (x : Fin (n + 1) → ℝ) : ℝ
def pathAverage {n : ℕ} (x : Fin (n + 1) → ℝ) : ℝ

theorem pathPotential_edge_increment (e : Fin n) :
    pathPotential w e.succ - pathPotential w e.castSucc = pathCurrent n e / w e
theorem pathPotential_weak_equation (hpos : ∀ e, 0 < w e)
    (y : Fin (n + 1) → ℝ) :
    (∑ e, w e *
      (pathPotential w e.succ - pathPotential w e.castSucc) *
      (y e.succ - y e.castSucc)) =
      y (Fin.last n) - pathAverage y
theorem pathEnergy_eq_resistance (hpos : ∀ e, 0 < w e) :
    pathEnergy w (pathPotential w) =
      pathPotential w (Fin.last n) - pathAverage (pathPotential w)
theorem pathResistance_eq (hpos : ∀ e, 0 < w e) :
    pathPotential w (Fin.last n) - pathAverage (pathPotential w) =
      (1 / (n + 1 : ℝ) ^ 2) *
        ∑ e, (e.val + 1 : ℝ) ^ 2 / w e
```

The regression corollaries will state, respectively,
`1/(4*w₁)`, `(1/w₁ + 4/w₂)/9`, and
`(1/w₁ + 4/w₂ + 9/w₃)/16`.

## Independent mathematical audit

### Three-vertex spectrum

Direct determinant expansion gives

```text
det(lambda*I - G) =
  lambda * (lambda^2 - 2*(a+b)*lambda + 3*a*b).
```

The quadratic discriminant is
`4*(a^2-a*b+b^2)`.  For `a,b > 0`, the radicand is positive and is
strictly below `(a+b)^2` by `3*a*b`.  Hence both displayed nonzero roots are
positive, and the minus root is strictly smaller.  No ordering assumption
`a > b` is used.  The controls `b=0`, `a=0`, and `a=b>0` give respectively
`(0,0,2a)`, `(0,0,2b)`, and `(0,a,3a)`.

### The `-3/8` coefficient

With `s = sqrt(1-r+r^2)`, exact rationalization for `r>0` gives

```text
(h(r) - (3/2)*r) / r^2
  = -3 / (2*(1+r+s)*(1-r+s)).
```

Continuity at zero sends the right side to `-3/8`.  For fixed `a>0`,
`muMinus(a,b)=a*h(b/a)` and `a*(b/a)^2=b^2/a`, which fixes both the sign and
the scale of the second theorem without asserting a uniform remainder.

### Feshbach normalization

For

```text
u   = (1,-1,0)/sqrt(2),
psi = (1,1,-2)/sqrt(6),
B₂  = [[0,0,0],[0,1,-1],[0,-1,1]],
```

direct multiplication gives `u·u=1`, `psi·psi=1`, `u·psi=0`, and
`|u·(B₂ psi)|^2=3/4`.  Reversing the edge orientation leaves `B₂` unchanged;
changing either vector sign does not affect the squared overlap.

### Centered source, gauge, and indexing

This gate incorporates the open PF-091 adversarial review.  Put `j=n+1` and

```text
q = e_last - (1/j)*1.
```

The source sums to zero.  Orienting edge `m` from `m-1` to `m`, conservation
forces current `I_m=m/j`.  With positive conductance `w_m`, define potential
increments `x_m-x_(m-1)=I_m/w_m`.  Discrete summation by parts yields

```text
sum_m w_m*(x_m-x_(m-1))*(y_m-y_(m-1))
  = y_last - average(y).
```

Taking `y=x` and substituting the currents gives

```text
x_last - average(x)
  = sum_m I_m^2/w_m
  = (1/j^2) * sum_m m^2/w_m.
```

This is invariant under adding a constant to `x`.  It is also the exact content
needed to interpret the prose shorthand: if `L⁺` is the Moore--Penrose inverse
of the connected path Laplacian, then `L⁺1=0`, so with the centered `q`,

```text
e_lastᵀ L⁺ e_last = qᵀ L⁺ q.
```

The Lean target deliberately proves the centered weak equation and energy
identity instead of introducing pseudoinverse infrastructure or leaving the
zero-mode convention implicit.  Thus the open review is an input to the frozen
surface, not a defect to prove around.

For the PF-091 dominance sentence, fixed `j ≥ 3` and monotonicity imply

```text
sum_{m<j-1} m^2/w_m
  ≤ (sum_{m<j-1} m^2)/w_(j-2).
```

Consequently `w_(j-1)/w_(j-2) → 0` makes all earlier terms negligible relative
to `(j-1)^2/w_(j-1)`.  No separate dominance theorem is needed for the bounded
formal target, but the legacy warning that every earlier ratio is additionally
required is not adopted.

## Prior-art and reuse classification

- The spectrum of a finite weighted path, the quadratic expansion, electrical
  resistance, Moore--Penrose Laplacian characterization, and Schur/Feshbach
  elimination are standard; no novelty is claimed for them.
- Mathlib's unweighted `SimpleGraph.lapMatrix` and invertible
  `Matrix.SchurComplement` do not directly supply this weighted centered-source
  theorem.  The child artifact found no Mathlib Moore--Penrose/effective-
  resistance API that would avoid a small elementary proof.
- The exact endpoint-minus-average path formula is a series-network
  specialization of standard effective-resistance theory.
- No Lean source currently exists on Mathia `main`; no Mathia declaration is
  available to reuse.
- The exact qwen-lean artifact already proves the frozen declarations.  The
  smallest coherent implementation is therefore a source-level port into
  Mathia, followed by fresh compilation and review here, not a second proof
  designed from scratch.

Low-level declarations to reuse from Mathlib include `Matrix.mulVec`,
`dotProduct`, `Matrix.det_fin_three`, `Matrix.exists_mulVec_eq_zero_iff`,
`Real.sq_sqrt`, continuity and `Tendsto`, `Fin.partialSum`, finite sums, matrix
notation, and ordinary algebraic tactics.

## Mathia-local environment decision

Mathia currently has no Lean/Lake project.  The execution machine has Lean
toolchains `v4.27.0`, `v4.32.0`, and `v4.32.2` installed but no global default.
After Gate approval, the branch may add the smallest local setup:

- `lean-toolchain` selecting the already-installed Lean `v4.32.0`;
- `lakefile.toml` with one Mathlib dependency at `v4.32.0`;
- `formalization/PF091WeightedPathMemory.lean`.

The version is reproducibility evidence for this execution, not a scientific
premise or a permanent repository-wide formalization policy.  A temporary
checkout of the child artifact resolved Mathlib to commit
`81a5d257c8e410db227a6665ed08f64fea08e997`; fresh compilation was not claimed
at Gate time because cache extraction in `/tmp` exhausted that temporary
filesystem.  Final progression requires a successful compile in the Mathia
worktree on persistent storage.

## Proof-integrity and final validation

Before ready-for-review handoff, the exact source must:

- pass `lake env lean formalization/PF091WeightedPathMemory.lean`;
- contain no `sorry`, `admit`, new `axiom`, or `unsafe` declaration used to
  discharge the target;
- print the axiom footprints of all principal theorems;
- retain the frozen statements and finite-only scope;
- include the `j=2,3,4` regressions and two-scale bookkeeping check;
- pass `git diff --check` and a complete changed-path audit;
- record any new material mathematical observation in issue #75, or record
  `Formalization research handoff: none`;
- receive a fresh independent final review of the complete published target.
