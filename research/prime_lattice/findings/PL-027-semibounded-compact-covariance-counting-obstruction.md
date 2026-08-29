# PL-027 — Semibounded compact-cocycle covariance forces at most linear eigenvalue density

## Claim

The compact-but-non-trace-class escape left open by `PL-026` disappears for a semibounded Hilbert–Pólya operator.

Let `H` be self-adjoint, bounded below, with compact resolvent on an infinite-dimensional Hilbert space. Define the finite one-sided counting function

```text
N_H(E) = Tr 1_(-infinity,E](H).
```

Assume that for some `a>0` there are a unitary `U` and a bounded self-adjoint compact operator `K` such that

```text
U^* H U = H + a I + K.
```

Then

```text
boxed: N_H(E) = O(E).
```

More precisely, for every `0<epsilon<a` there is a finite integer `r_epsilon` such that, with `delta=a-epsilon`,

```text
N_H(E) - N_H(E-delta) <= r_epsilon
```

for every real `E`.

Consequently no semibounded compact-resolvent operator whose eigenvalue count grows superlinearly can obey such a covariance. In particular, a positive-ordinate Hilbert–Pólya Hamiltonian with the Riemann-zero counting law cannot satisfy, for even one prime `p`,

```text
U_p^* H U_p = H + (log p) I + K_p
```

with `K_p` compact self-adjoint, whether or not `K_p` belongs to any Schatten class.

**Evidence/status:** `EXACT-DERIVED + DECISIVE-NEGATIVE` for the route

```text
semibounded compact-resolvent zero Hamiltonian
    + reversible prime shift
    + exact log-prime scalar increment
    + bounded compact cocycle
    -> Riemann-zero eigenvalue density.
```

The perturbation ingredients are standard min-max/interlacing facts. The prime-lattice consequence and counting contradiction are derived here from those elementary facts and the classical Riemann–von Mangoldt law already used in `PL-026`. No novelty is claimed for finite-rank interlacing or compact approximation.

## Exact counting argument

Set

```text
A = H + a I,
B = A + K = U^* H U.
```

Fix any

```text
0 < epsilon < a.
```

Because `K` is compact and self-adjoint, choose a finite-rank self-adjoint `F` such that

```text
rank(F) = r < infinity,
||K-F|| < epsilon.
```

Write

```text
R = K-F.
```

Then, as quadratic forms on `Dom(H)`,

```text
-epsilon I <= R <= epsilon I,
```

so

```text
B = A+F+R >= A+F-epsilon I.
```

For semibounded self-adjoint compact-resolvent operators, form ordering reverses the eigenvalue-count inequality below a fixed threshold. Hence

```text
N_B(E) <= N_(A+F)(E+epsilon).
```

A rank-`r` self-adjoint perturbation can change the dimension of a spectral subspace below a threshold by at most `r`; equivalently,

```text
N_(A+F)(x) <= N_A(x) + r.
```

For completeness, this finite-rank inequality can be seen directly. If the spectral subspace of `A+F` below `x` had dimension greater than `N_A(x)+r`, then it would contain a nonzero vector lying simultaneously in `ker(F)` and in the spectral subspace of `A` above `x`. On that vector the quadratic form of `A+F` equals that of `A`, giving both `<=x` and `>x`, a contradiction. This is the standard finite-rank interlacing argument.

Now use the exact unitary equivalence and scalar translation:

```text
N_B(E) = N_H(E),
N_A(E+epsilon)
  = N_H(E+epsilon-a).
```

Therefore

```text
N_H(E)
  <= N_H(E+epsilon-a) + r.
```

With

```text
delta = a-epsilon > 0,
```

this is

```text
boxed:
N_H(E) - N_H(E-delta) <= r.
```

Thus every energy window of the fixed width `delta` contains at most `r` eigenvalues, counted with multiplicity.

Because `H` is bounded below, choose a fixed base energy `E_0` below which only finitely many eigenvalues occur. Iterating the inequality downward in steps of `delta` gives

```text
N_H(E)
  <= C + r ceil((E-E_0)/delta)
  = O(E).
```

No trace ideal, determinant, spectral-shift function, commutation relation between different prime shifts, or asymptotic approximation is used. A single nonzero scalar covariance step and compactness of its additive correction suffice once the target Hamiltonian is semibounded.

## Application to a positive Riemann-zero Hamiltonian

Let `N_zeta(T)` count nontrivial zeros `rho=beta+i gamma` with

```text
0 < gamma <= T,
```

including multiplicity. The unconditional Riemann–von Mangoldt formula gives

```text
N_zeta(T)
 = T/(2 pi) log(T/(2 pi))
   - T/(2 pi)
   + O(log T).
```

Hence

```text
N_zeta(T)/T -> infinity.
```

Suppose a semibounded self-adjoint compact-resolvent `H` has, up to an irrelevant fixed affine energy normalization, the positive zero ordinates as its eigenvalues. If for one prime `p`

```text
U_p^* H U_p
  = H + (log p) I + K_p,
```

with `U_p` unitary and `K_p` compact self-adjoint, the theorem above would imply

```text
N_zeta(T) = O(T),
```

contradicting Riemann–von Mangoldt.

This contradiction uses only the known density of all nontrivial zeros. It does not assume RH and does not use any hypothesis about their real parts.

## Why this materially sharpens PL-025 and PL-026

`PL-025` ruled out the exact reversible covariance

```text
U_p^* H U_p = H + (log p) I
```

for a discrete Hilbert–Pólya spectrum: two independent prime steps force the full real spectral set.

`PL-026` then allowed an additive cocycle

```text
U_p^* H U_p = H + (log p) I + K_p
```

and proved that `K_p in S_1` is still too small. Its Lifshits–Krein argument is strong enough to treat an **indefinite/two-sided** compact-resolvent Hamiltonian, but deliberately left general compact non-`S_1` corrections open.

The present result closes that compact escape under a different structural assumption:

```text
K_p compact of arbitrary singular-value decay
    + H bounded below
    -> N_H(E)=O(E).
```

Thus the remaining gap after `PL-026` is much narrower than “try a compact cocycle rougher than trace class.” Such a cocycle can only remain relevant to an eigenvalue model if the zero Hamiltonian is essentially two-sided/indefinite, or if another hypothesis of the covariance ansatz is abandoned.

The contrast is useful:

```text
S_1 correction
    -> linear counting obstruction even for two-sided H       [PL-026]

arbitrary compact correction
    -> linear counting obstruction for semibounded H          [PL-027]
```

So trace class is not the true threshold for a positive-energy realization.

## Prime-lattice interpretation

For the signed exponent lattice, exact unitary translation in the `p`-direction naturally changes the logarithmic energy by

```text
log p.
```

The cocycle ansatz tries to let global arithmetic structure repair this local translation law:

```text
prime shift
    -> + log p in energy
    -> + compact arithmetic correction K_p.
```

For a semibounded discrete spectrum, compactness says that this repair can be approximated, to any fixed accuracy smaller than `log p`, by a perturbation of finite rank. The finite-rank part can move only finitely many spectral dimensions across any threshold, while the residual norm error cannot cancel the positive scalar step. The covariance therefore forces a uniform bound on the number of states in fixed-width high-energy windows.

The Riemann zero divisor has too many states globally for such a geometry: its cumulative count grows like `T log T`, not linearly.

This is a structural obstruction rather than another encoding of zeta. It depends on the prime-lattice proposal only through the exact positive energy increment `a=log p` and tests a concrete operator design condition.

## Prior art and novelty audit

The mathematical tools used above are classical:

- compact self-adjoint operators are norm limits of finite-rank self-adjoint operators;
- the min-max principle gives monotonicity of ordered eigenvalues under form ordering;
- a rank-`r` self-adjoint perturbation changes an eigenvalue counting function across a fixed threshold by at most `r`;
- the Riemann–von Mangoldt formula gives the unconditional `T log T` zero density.

Standard perturbation references such as Reed–Simon, *Methods of Modern Mathematical Physics IV: Analysis of Operators*, and Kato, *Perturbation Theory for Linear Operators*, contain the min-max/compact-perturbation background. The derivation is included above so the finding does not depend on importing a stronger theorem than needed.

A novelty search around unitary equivalence to scalar translates modulo compact perturbations, finite-rank counting interlacing, spectral shift, and compact-resolvent perturbation theory did not locate this exact prime-shift/Riemann-zero application. That absence is not evidence of novelty, and no novelty claim is made. The durable value is the exact elimination of a previously explicit escape route in `PL-026`.

## Boundary conditions and escape routes

### Semiboundedness is essential to this proof

The one-sided counting function

```text
N_H(E)=Tr 1_(-infinity,E](H)
```

must be finite. For a two-sided operator carrying both `+gamma` and `-gamma`, it is infinite, and the iteration argument does not apply. Compact perturbations outside `S_1` may therefore still be relevant to an indefinite realization.

This is precisely where `PL-026` remains stronger: its trace-class spectral-shift argument controls symmetric two-sided counting.

### Compactness is essential

The proof needs a finite-rank approximation `F` with residual norm strictly smaller than the scalar step `a`. A bounded noncompact cocycle is not covered.

### The scalar increment must remain exact

If the prime action satisfies an energy-dependent, nonlinear, asymptotic, projective, or only averaged covariance rather than

```text
+ (log p) I,
```

the fixed-width recurrence does not follow.

### Nonunitary or compressed prime actions remain outside the theorem

Proper isometries, Toeplitz/compressed actions, partial isometries, transfer operators, and scattering constructions need not preserve the counting function under conjugation. `PL-024` is the canonical one-sided example.

### Resonance and trace-formula pictures are not eigenvalue models

Continuous-spectrum systems may encode zeta zeros as resonances, absorption lines, scattering poles, or trace-formula distributions. The result only constrains a semibounded compact-resolvent eigenvalue realization with the stated reversible covariance.

## Audit / falsification tests

The finding would be falsified or materially narrowed by any of the following:

1. a semibounded compact-resolvent self-adjoint `H` with `N_H(E)/E -> infinity` and operators `U,K` satisfying the hypotheses;
2. failure of the finite-rank bound `N_(A+F)(x) <= N_A(x)+rank(F)` for semibounded compact-resolvent self-adjoint operators;
3. failure to approximate a bounded compact self-adjoint `K` in norm by finite-rank self-adjoint operators;
4. an error in the form-order implication `B>=A+F-epsilon I => N_B(E)<=N_(A+F)(E+epsilon)`;
5. a proposed zero Hamiltonian that is genuinely two-sided, non-semibounded, non-compact-resolvent, resonance-based, nonunitarily shifted, or uses a noncompact/nonadditive cocycle, in which case it lies outside the theorem rather than contradicting it.

The first four are excluded by the exact argument and standard operator theory. The fifth identifies the remaining design boundary.

## Consequence for the research line

The reversible prime-shift branch now has the sharper constraint ladder

```text
exact unitary log-prime covariance
    -> full real spectrum                                    [PL-025]

+ S_1 cocycle
    -> N_H(T)=O(T), including two-sided compact-resolvent H  [PL-026]

+ arbitrary compact cocycle, with H semibounded
    -> N_H(E)=O(E)                                           [PL-027]
```

Therefore a positive-energy Hilbert–Pólya model cannot rescue exact reversible prime-lattice covariance merely by replacing a trace-class correction with a rougher compact one. Any surviving operator route must instead use an essentially indefinite/two-sided compact correction outside `S_1`, a noncompact/global correction, a nonunitary/compressed action, or a trace/scattering/adelic mechanism rather than direct prime-coordinate spectral translation.