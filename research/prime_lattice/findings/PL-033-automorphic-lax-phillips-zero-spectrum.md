# PL-033 — Automorphic Lax–Phillips scattering already realizes zeta zeros as generator eigenvalues; RH is axis localization, not spectral realization

## Claim

There is a classical operator-theoretic realization much closer to the desired “zeros as spectrum/resonances” mechanism than the bare prime torus: automorphic Lax–Phillips scattering for the modular surface.

For the continuous scattering system of `SL_2(Z)`, after removal of elementary factors the causal scattering factor used by Uetake is

```text
S_c0(s) = xi(2s) / xi(-2s),
```

where

```text
xi(s) = (1/2) s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)
```

is the completed entire Riemann xi-function. Uetake constructs the Lax–Phillips infinitesimal generator `A_c` on a scattering model space `K` and proves:

```text
rho is a nontrivial zero of zeta, with multiplicity m
    <=>
rho is an eigenvalue of -2 A_c, with algebraic multiplicity m.
```

Moreover the generalized eigenvectors form a basis of `K`, and

```text
RH
  <=> sigma(2 A_c + (1/2) I) lies on the imaginary axis.
```

Thus a genuine operator whose eigenvalues are *precisely* the nontrivial Riemann zeros, with multiplicity, already exists in classical automorphic scattering theory. What it does **not** do is force the critical line: the generator is not supplied as a self-adjoint Hilbert–Pólya operator whose spectral theorem makes the axis condition automatic. RH becomes the statement that this already-existing non-self-adjoint scattering spectrum lies on its distinguished symmetry axis.

For the prime-lattice program this is a prior-art redirect. The route

```text
prime/Euler data
    -> completed meromorphic object
    -> scattering poles / resolvent poles
    -> operator eigenvalues equal zeta zeros
```

is not missing. The missing step is a structural reason — self-adjointness, normality after the correct centering/rotation, positivity, or an equivalent global constraint — that forces those eigenvalues onto the critical axis.

**Evidence/status:** `LITERATURE+DERIVED + CLASSICAL-IDENTITY + NEGATIVE/OBSTRUCTION`.

The automorphic scattering construction and zero/eigenvalue theorem are literature. The derived consequence for this line is that merely finding an operator, semigroup generator, determinant, resonance system, or resolvent whose poles/eigenvalues reproduce the zeta zero divisor cannot itself be the sought new prime-exponent mechanism.

## The scattering coefficient contains the completed zeta function

For the modular surface `SL_2(Z)\H`, the Eisenstein series gives the continuous spectral channel of the hyperbolic Laplacian. In Uetake's shifted spectral parameter, the continuous scattering matrix has the form

```text
S_c(s)
 = -((s-1/2)/(s+1/2))^2
     Gamma(1/2) Gamma(s) zeta(2s)
     / (Gamma(s+1/2) zeta(2s+1))

 = -((s-1/2)/(s+1/2)) xi(2s)/xi(-2s).
```

The non-elementary causal factor is therefore

```text
S_c0(s) = xi(2s)/xi(-2s).
```

Since the zeros of `xi` are exactly the nontrivial zeros of `zeta`, the non-real poles of this factor in

```text
-1/2 < Re(s) < 0
```

are the reflected/scaled zero divisor. The Riemann hypothesis is exactly the assertion that the relevant poles lie on

```text
Re(s) = -1/4
```

(and equivalently the corresponding zeros on `Re(s)=1/4`). This is simply the usual critical line under the affine scaling used by the scattering parameter.

The critical point here is analytic: this scattering formula is **not** an Euler product being formally evaluated inside the critical strip. The meromorphic continuation comes from the automorphic Eisenstein/scattering theory. Lax–Phillips developed meromorphic continuation and pole/resolvent correspondence for the automorphic wave equation; Uetake then isolates the causal factor carrying precisely the nontrivial zeta divisor.

Thus this construction genuinely survives the analytic-continuation boundary that invalidates many bare Bohr/Euler-product manipulations.

## The zero divisor is an actual operator spectrum

Let `K` be the Lax–Phillips interaction space and

```text
A_c = P_K L |_K
```

its infinitesimal generator. Uetake proves that the resolvent of `-2 A_c` is meromorphic on the whole complex plane and that its spectrum consists of eigenvalues of finite algebraic multiplicity. His Theorem 4.4 states exactly:

```text
rho is a nontrivial zeta zero of multiplicity m
  iff
rho is an eigenvalue of -2 A_c of algebraic multiplicity m.
```

It also states that the generalized eigenvectors corresponding to the eigenvalues form a basis of `K`. Therefore this is stronger than an identity of the form

```text
spectral-zeta(operator) contains zeta(s),
```

which was the limitation isolated in `PL-016`. Here the zeta zeros themselves are the spectrum of the generator, not zeros of a secondary spectral zeta function.

In the outgoing translation representation the construction is also explicit. Uetake identifies a model space of the form

```text
K_c = L^2(R_-) \ominus S_c0 L^2(R_-)
```

and represents the generator as a compression/restriction of the translation derivative. This is standard scattering/model-space geometry: the inner/causal scattering factor determines an interaction subspace, and its poles become resolvent poles/eigenvalues of the compressed generator.

## Why this is not Hilbert–Pólya

The same theorem makes the unresolved step completely transparent:

```text
RH
  <=>
sigma(2 A_c + (1/2) I) is contained in i R.
```

If one formally writes

```text
H_candidate = -i (2 A_c + (1/2) I),
```

then RH is equivalent to `H_candidate` having real spectrum. But this does not prove that `H_candidate` is self-adjoint or even normal. Real spectrum of a non-normal operator is not automatic, and demanding it is essentially the RH content rather than a consequence of the construction.

This distinction is decisive for the research line:

```text
existence of an operator with zeta zeros as eigenvalues
    !=
existence of a self-adjoint operator whose spectral theorem forces RH.
```

The Lax–Phillips generator solves the first problem classically. It leaves the second problem untouched.

This also explains why a resonance/scattering formulation can coexist with hypothetical off-critical zeros: off-line zeros simply appear as eigenvalues/poles off the distinguished axis. The scattering system represents the divisor faithfully rather than constraining it.

## Relation to the exponent lattice

The construction does not arise from the bare infinite prime torus, so it must not be presented as an intrinsic consequence of `v(n)`.

On the Euler-product side, for `Re(s)>1`, the ordinary prime-exponent data enters through

```text
-zeta'(s)/zeta(s)
  = sum_p sum_{k>=1} (log p) p^(-ks),
```

whose exponent-lattice support is the prime-power axis set `k e_p` identified in `PL-013`. The completed function `xi`, however, also contains the archimedean gamma factor and the functional-equation completion. In the present route this completed object is realized as the automorphic scattering coefficient of the modular surface.

The structural chain is therefore more accurately

```text
prime-power / Euler data in its convergence half-plane
        +
archimedean completion and modular automorphic geometry
        +
meromorphic Eisenstein scattering
        ->
causal scattering factor xi(2s)/xi(-2s)
        ->
Lax–Phillips model space and generator
        ->
zeta zeros as resolvent poles / eigenvalues.
```

The new geometry that makes analytic continuation and spectral realization possible is hyperbolic/automorphic scattering geometry, not the free exponent lattice itself. This is consistent with `PL-014`: genuine continuation and the functional equation repeatedly require global/archimedean harmonic structure absent from the bare prime torus.

## Cyclicity is also already part of the scattering formulation

There is a second prior-art warning relevant to `PL-017`–`PL-020`. Uetake gives a weak-resolvent realization of the discrete scattering factor and derives a cyclic-vector criterion equivalent to RH. For each test point in the off-axis critical region he constructs an augmented system `(A_aug,b_aug)` such that

```text
that point is not a zero of the scattering factor
    <=>
b_aug is cyclic for A_aug,
```

and RH is equivalent to this cyclicity holding for every such point.

Therefore even the combination

```text
zeta divisor
    + operator model
    + cyclicity/controllability criterion
```

is established prior art in scattering theory. A new prime-lattice cyclicity proposal must supply extra arithmetic structure or a proof mechanism, not merely another equivalent cyclic formulation.

## Prior art and novelty audit

The direct source is:

- **Yoichi Uetake**, “The Lax–Phillips infinitesimal generator and the scattering matrix for automorphic functions,” *Annales Polonici Mathematici* **92**(2) (2007), 99–122, DOI `10.4064/ap92-2-1`. The abstract explicitly states that the constructed operator has precisely the nontrivial zeta zeros as eigenvalues with algebraic multiplicity. Theorem 4.4 gives the exact zero/eigenvalue equivalence and the RH axis criterion; Theorem 6.3 gives the cyclic-vector RH criterion.

The underlying automorphic scattering machinery is older:

- **Peter D. Lax and Ralph S. Phillips**, *Scattering Theory for Automorphic Functions*, Annals of Mathematics Studies 87, Princeton University Press, 1976. The monograph develops the automorphic wave-equation scattering system, meromorphic Eisenstein/scattering theory, and the correspondence between scattering poles and resolvent poles of the Lax–Phillips generator.
- Uetake traces the first application of Lax–Phillips scattering to the non-Euclidean automorphic wave equation to **B. S. Pavlov and L. D. Faddeev** (1972), with later Lax–Phillips development.

No novelty is claimed for scattering theory, the modular scattering coefficient, the zero/eigenvalue correspondence, or the cyclicity criterion. The durable contribution here is the novelty audit against the prime-lattice search space: an operator-theoretic realization of the zero divisor is already classical once automorphic scattering structure is admitted.

This appears to be distinct from the current stored prime-lattice prior-art anchors. `PL-013` records Weil positivity and recent self-adjoint finite spectral triples; `PL-014` records Tate's adelic Fourier self-duality; `PL-016` distinguishes eigenvalues from zeros of a spectral-zeta function. The present result fills the complementary slot in which the zeros really *are* generator eigenvalues, while showing why that fact still does not localize them.

## Boundary conditions and counterarguments

### The finding does not say spectral approaches are exhausted

It rules out only the claim that producing *some* operator/resonance generator with zeta zeros as its spectrum is itself the missing mechanism. A self-adjoint realization, a positivity theorem, a normality theorem, or a canonical symmetry forcing the spectrum onto the centered axis would be substantially stronger and remains RH-level content.

### The model is not intrinsic to the bare prime lattice

The modular surface, Eisenstein series, archimedean factors, and scattering theory are additional global structures. This is precisely why the construction can cross `Re(s)=1` rigorously. It should not be counted as evidence that the infinite torus alone has hidden resonances at the zeta zeros.

### Scattering poles are meaningful rather than a tautological determinant encoding

The pole/eigenvalue correspondence comes from a Lax–Phillips semigroup and its resolvent, with an explicit `L^2(R)` model and generalized eigenvectors. It is structurally stronger than defining an arbitrary diagonal operator after first listing the zeta zeros. The negative conclusion is therefore not “every spectral encoding is arbitrary”; it is that a serious classical encoding already exists and still leaves RH as the axis-location statement.

### Critical-line centering must not be mistaken for proof

The affine transform `2 A_c + (1/2)I` singles out the critical symmetry axis because the completed zeta functional equation already supplies that symmetry. Saying that RH is equivalent to the transformed spectrum being imaginary does not explain why it must be imaginary.

### This does not resolve the trace-class prime-resolvent clue

`CLUE-trace-class-prime-resolvent-cocycle` asks for a **specified prime action** whose action-dependent relative resolvent is trace class after subtracting scalar translation. Automorphic Lax–Phillips scattering supplies a noncompact-reference resonance mechanism, but not such a prime-coordinate action. It therefore remains a separate proposed clue rather than being accepted, rejected, or resolved by this finding.

## Audit / falsification tests

This finding would be falsified or materially narrowed if any of the following failed:

1. the modular automorphic scattering matrix does not contain the causal factor `xi(2s)/xi(-2s)` in Uetake's normalization;
2. the Lax–Phillips generator's resolvent is not meromorphic or its poles fail to match the causal scattering poles with multiplicity;
3. Uetake's `-2 A_c` does not have the nontrivial zeta zeros as eigenvalues with matching algebraic multiplicity;
4. `sigma(2 A_c + (1/2)I) subset iR` is not equivalent to RH;
5. the claimed operator is actually proved self-adjoint/normal in a way that forces the axis condition unconditionally, which would be a vastly stronger result than represented here;
6. this same exact zero-as-generator-spectrum mechanism is already stored elsewhere in the current `prime_lattice` corpus, in which case `PL-033` should be treated as duplication rather than a distinct prior-art redirect.

The first four are explicit theorems/formulas in the primary source. The fifth is not claimed by that source; the sixth was checked against the current finding inventory and literature anchors.

## Consequence for the research line

The spectral design space can now be separated more sharply:

```text
bare prime Kronecker flow
    -> pure-point rational-log spectrum, no zeta divisor        [PL-011]

multiplicative Hilbert / lattice tensor operators
    -> genuine spectra, but zeros are absent or live only
       in a secondary spectral-zeta continuation                [PL-010, PL-016]

completed automorphic scattering
    -> zeta zeros are genuine generator eigenvalues             [PL-033]
    -> RH remains the assertion that this spectrum is axial

Weil / self-adjoint finite-truncation route
    -> real spectra by construction at finite level
    -> convergence to Xi / all zeros remains the hard step      [PL-013]
```

Accordingly, another construction whose main achievement is “the zeta zeros are poles/eigenvalues of this operator” should be presumed prior art or insufficient. A genuinely new mechanism must explain **localization**: why completed global arithmetic data force the already-representable divisor onto the self-dual line `Re(s)=1/2`.
