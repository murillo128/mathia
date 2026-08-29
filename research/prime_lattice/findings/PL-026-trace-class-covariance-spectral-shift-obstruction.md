# PL-026 — Trace-class corrections cannot rescue a zero-density prime-shift Hamiltonian

## Claim

The trace-class escape left open by `PL-025` is incompatible with a Hilbert–Pólya operator having the Riemann-zero counting density.

Let `H` be self-adjoint with compact resolvent on an infinite-dimensional Hilbert space. Write its eigenvalues with multiplicity as `{lambda_j}` and

```text
N_H(T) = #{j : |lambda_j| <= T}.
```

Assume that for some `a>0` there are a unitary `U` and a self-adjoint trace-class operator `K in S_1` such that

```text
U^* H U = H + a I + K.
```

Then necessarily

```text
N_H(T) = O(T).
```

Consequently, if

```text
N_H(T)/T -> infinity,
```

no such covariance can exist. In particular, an operator whose spectrum with multiplicity is the Riemann-zero ordinates cannot satisfy

```text
U_p^* H U_p = H + (log p) I + K_p,
K_p in S_1,
```

for even one prime `p`, because the Riemann–von Mangoldt formula gives superlinear zero counting,

```text
N_zeta(T) asymp T log T.
```

Thus allowing a trace-class arithmetic cocycle does **not** evade the exact reversible-covariance obstruction of `PL-025`. Any viable cocycle-corrected unitary prime-shift model for a Riemann-zero Hamiltonian must use a correction rougher than ordinary trace class, or abandon one of the other hypotheses.

**Evidence/status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the route

```text
compact-resolvent zero Hamiltonian
    + exact unitary prime shift
    + scalar log-prime increment
    + additive S_1 correction
    -> Hilbert–Pólya spectrum.
```

The Lifshits–Krein trace formula and `L^1` spectral-shift theorem for trace-class perturbations are classical. The counting obstruction below is an exact specialization to the prime-lattice covariance considered in `PL-025`. No novelty is claimed for spectral-shift theory itself.

## Exact derivation from the spectral-shift function

Set

```text
A = H + a I,
B = U^* H U = A + K.
```

Because `K` is self-adjoint trace class, classical Lifshits–Krein theory provides a real spectral-shift function

```text
xi in L^1(R)
```

for the pair `(B,A)`, with, for smooth compactly supported `f`,

```text
Tr(f(B)-f(A)) = integral_R f'(x) xi(x) dx.
```

Since `H` has compact resolvent, `f(H)` is finite rank for compactly supported `f`. Unitary equivalence therefore gives

```text
Tr f(B) = Tr f(H),
Tr f(A) = Tr f(H+aI),
```

and hence

```text
Tr(f(B)-f(A))
 = sum_j ( f(lambda_j) - f(lambda_j+a) ).
```

For `a>0`, define the locally integrable integer-valued function

```text
eta_a(x) = - sum_j 1_[lambda_j, lambda_j+a](x).
```

Local finiteness follows from compact resolvent. Termwise integration is finite on the support of `f'`, and

```text
f(lambda_j)-f(lambda_j+a)
 = - integral_[lambda_j,lambda_j+a] f'(x) dx.
```

Therefore

```text
integral f'(x) xi(x) dx
 = integral f'(x) eta_a(x) dx
```

for every `f in C_c^infinity(R)`. Thus, in distributions,

```text
xi - eta_a = C
```

for some real constant `C`; equivalently,

```text
eta_a(x) = xi(x) - C
```

up to the immaterial sign convention for the constant. The only property needed below is that `eta_a` differs from an `L^1` function by a constant.

It follows that

```text
| integral_[-T,T] eta_a(x) dx | <= 2 |C| T + ||xi||_1 = O(T).
```

But every eigenvalue with

```text
|lambda_j| <= T-a
```

contributes the full interval length `a` to `[-T,T]`, all contributions have the same sign, and hence

```text
| integral_[-T,T] eta_a(x) dx |
 >= a N_H(T-a).
```

Combining the two inequalities gives

```text
boxed: N_H(T) = O(T).
```

This argument needs no commutation relation among different prime shifts and no assumption that `H` is semibounded. A **single** nonzero scalar covariance step with an additive trace-class correction already imposes the linear counting ceiling.

## Application to the Riemann-zero spectrum

Let `N(T)` denote the number of nontrivial zeta zeros `rho=beta+i gamma` with `0<gamma<=T`, counted with multiplicity. The classical Riemann–von Mangoldt formula is

```text
N(T)
 = T/(2 pi) log(T/(2 pi)) - T/(2 pi) + O(log T).
```

If a self-adjoint Hilbert–Pólya operator carries both signs of the ordinates, its symmetric counting function is therefore of order

```text
N_H(T) ~ (T/pi) log T,
```

up to the harmless convention at `gamma=0`. If one instead models only the positive ordinates, the count is still of order `T log T`.

Either way,

```text
N_H(T)/T -> infinity,
```

contradicting the `O(T)` consequence above. Hence exact prime-shift covariance corrected only by `S_1` terms cannot coexist with the required zero density.

Importantly, this uses the **counting law**, not RH. The Riemann–von Mangoldt asymptotic holds unconditionally and counts all nontrivial zeros in the critical strip. The obstruction therefore does not presuppose that those zeros lie on `Re(s)=1/2`.

## Why this materially sharpens PL-025

`PL-025` proved that the exact relation

```text
U_p^* H U_p = H + (log p) I
```

forces `sigma(H)=R` once two multiplicatively independent unitary prime shifts are present, because `Z log 2 + Z log 3` is dense. It deliberately left open cocycle-corrected relations such as

```text
U_p^* H U_p = H + (log p) I + K_p,
```

including compact or trace-class `K_p`.

The present result closes the ordinary trace-class part of that escape in a different way. Exact translation invariance of the spectral **set** is lost, so the dense-subgroup proof no longer applies. But trace-class perturbation theory remembers the translation through an integrable spectral-shift function. A scalar shift by `a` sweeps an interval of length `a` across every eigenvalue. If the perturbed operator is nevertheless unitarily equivalent to the original one, those swept intervals must collectively be represented by

```text
constant + L^1(R).
```

That is possible only when the number of eigenvalues in `[-T,T]` grows at most linearly.

The Riemann zero divisor is denser by a logarithmic factor, so an `S_1` cocycle is too small to absorb the mismatch.

## Prime-lattice interpretation

The natural exponent-lattice energy step is

```text
a_p = log p.
```

In the exact signed-lattice completion of `PL-025`, a unitary coordinate translation `U_p` shifts the logarithmic generator by exactly `log p`. A cocycle correction attempts to let global arithmetic data perturb this local rule:

```text
prime coordinate shift
    -> energy translation by log p
    -> plus K_p carrying the nonlocal correction.
```

`PL-026` says that if `K_p` lies in the smallest standard perturbative ideal `S_1`, then it cannot carry enough global spectral rearrangement to turn that covariance into a Riemann-zero spectrum. The obstruction is quantitative: trace-class perturbations have an `L^1` spectral shift, while translating a spectrum with `T log T` states up to height `T` generates a spectral-shift mass of order `T log T`.

This is more specific than saying that the lattice alone is insufficient. It places a lower regularity requirement on any exact reversible prime-lattice cocycle that hopes to interact with a Hilbert–Pólya spectrum.

## Prior art and novelty audit

The perturbation-theoretic input is classical. Standard trace-ideal and spectral-shift references include:

- Barry Simon, *Trace Ideals and Their Applications*, 2nd ed., Mathematical Surveys and Monographs 120, American Mathematical Society, 2005. This is a standard reference for trace ideals and Krein spectral-shift theory.
- Aleksei B. Aleksandrov and Vladimir V. Peller, “Relatively bounded and relatively trace class perturbations,” *Comptes Rendus. Mathématique* **363** (2025), 377–382, DOI `10.5802/crmath.722`. The paper gives a modern treatment of trace formulas and spectral-shift integrability in the more general relatively trace-class setting; ordinary additive `S_1` perturbations used here are classical special cases.

The Riemann–von Mangoldt counting formula is classical number theory. The novelty search did not locate a source proposing this exact prime-shift/Hilbert–Pólya covariance or the above counting contradiction as an RH mechanism. That absence is **not** a novelty claim: the argument is an elementary consequence of classical spectral-shift theory once the `PL-025` ansatz is posed.

The durable contribution for this line is the obstruction itself: the previously explicit `trace-class K_p` escape route in `PL-025` is not viable for the zero-density spectrum.

## Boundary conditions and escape routes

### Compact but non-trace-class corrections remain open

The proof uses `xi in L^1(R)`, which is specific to ordinary trace-class perturbations. A compact correction outside `S_1` is not covered. Hilbert–Schmidt or weaker corrections may have higher-order spectral-shift theories, but they do not satisfy the exact `L^1` argument above without additional hypotheses.

### Relatively trace-class unbounded corrections are not automatically covered

Modern spectral-shift theory extends to relatively trace-class perturbations with weighted integrability. That is not the same as a bounded additive `K in S_1`. The present finding does not silently promote the `L^1` counting ceiling to those broader classes.

### Nonunitary and compressed prime actions remain open

Proper isometries, partial isometries, Toeplitz compressions, semigroup representations, and boundary/scattering constructions are outside the hypothesis. Bost–Connes in `PL-024` is precisely one-sided rather than unitary.

### Resonances are not eigenvalue counting

A system with continuous spectrum may encode zeta zeros as resonances, scattering poles, absorption lines, or a trace-formula distribution. `PL-026` rules out a compact-resolvent **eigenvalue** realization with the stated trace-class covariance; it does not constrain Connes-type resonance/absorption pictures.

### The scalar increment must be exact

The proof uses a fixed nonzero `a=log p`. If the covariance is nonlinear, energy-dependent, only asymptotic, or corrected before the scalar shift is separated, a new analysis is required.

## Audit / falsification tests

The finding would be falsified or materially narrowed by any of the following:

1. a compact-resolvent self-adjoint `H` with `N_H(T)/T -> infinity`, a unitary `U`, `a>0`, and self-adjoint `K in S_1` satisfying `U^*HU=H+aI+K`;
2. failure of the classical Lifshits–Krein conclusion `xi in L^1(R)` for bounded additive trace-class self-adjoint perturbations;
3. failure of the trace identity for `f in C_c^infinity`, for which all spectral sums are finite under compact resolvent;
4. an error in the interval identity `f(lambda)-f(lambda+a)=-int_[lambda,lambda+a]f'` or in the bound `a N_H(T-a) <= |int_[-T,T] eta_a|`;
5. a proposed prime-lattice model whose correction is only compact, Hilbert–Schmidt, relatively trace class, nonadditive, or attached to a nonunitary/compressed action, in which case it lies outside the theorem rather than contradicting it.

The first four tests are excluded by the exact argument and standard perturbation theory. The fifth identifies the genuine remaining design boundary.

## Consequence for the research line

The operator-design constraints now sharpen to

```text
exact prime-shift invariance + normality
    -> scalar/trivial                                      [PL-023]

one-sided isometric shifts + exact log covariance
    -> Bost–Connes; thermodynamic boundary beta=1         [PL-024]

reversible unitary shifts + exact log covariance
    -> full real spectrum                                  [PL-025]

reversible unitary shifts + log covariance + S_1 cocycle
    -> eigenvalue count O(T)
    -> incompatible with Riemann N(T) ~ T log T            [PL-026]
```

So the next plausible reversible-covariance escape cannot merely add a small trace-class arithmetic correction. It must either cross to a rougher perturbation class where the accumulated spectral shift can scale like the zero density, or abandon exact unitary prime translation in favor of compression, scattering, adelic trace formulas, or another genuinely global mechanism.