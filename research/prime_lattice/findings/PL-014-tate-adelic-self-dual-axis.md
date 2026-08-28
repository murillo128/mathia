# PL-014 — Tate’s adelic Fourier duality identifies the critical line as the unitary self-dual axis beyond the bare prime torus

## Claim

The prime-exponent lattice has a canonical place inside classical adelic harmonic analysis, but the comparison sharply separates what the bare lattice supplies from what is required for the zeta functional equation.

For the finite ideles of `Q`, the valuation map gives

```text
A_f^× / Zhat^×  ≅  direct_sum_p Z,
```

and the positive-integer exponent vectors `v(n)=(v_p(n))_p` form the positive cone `N_0^(P)` in this signed valuation lattice. Moreover,

```text
log n = sum_p v_p(n) log p
      = -sum_p log |n|_p
      = log |n|_infinity,
```

where the last equality is exactly the global product formula. Thus the familiar prime-lattice energy `log n` is the finite idelic logarithmic norm, balanced by the archimedean place.

Tate’s thesis then supplies the missing harmonic structure. On the full adele ring, additive Fourier transform and multiplicative Mellin/zeta integration yield a twisted duality

```text
chi^vee = chi^(-1) |.|.
```

Writing an idele-class character as

```text
chi = eta |.|^s
```

with `eta` unitary gives

```text
chi^vee = eta^(-1) |.|^(1-s),
conj(chi) = eta^(-1) |.|^(conj(s)).
```

Hence

```text
chi^vee = conj(chi)  <=>  Re(s)=1/2.
```

Equivalently, the normalized character `chi |.|^(-1/2)` is unitary exactly on the critical line. In this precise classical sense, `Re(s)=1/2` is the Hermitian/unitary self-dual axis of the Fourier–Mellin functional-equation involution.

For the standard self-dual factorizable Schwartz–Bruhat function over `Q`, Tate’s global zeta integral initially factors for `Re(s)>1` into the finite Euler factors and the archimedean gamma factor, giving the completed Riemann zeta function. The global theorem then meromorphically continues this zeta integral and proves its functional equation by adelic Fourier/Poisson duality. This continuation is not a termwise continuation of the Euler product.

**Evidence/status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION` — classical prior-art redirect.

The theorem and harmonic mechanism are classical Tate theory. The Mathia-specific consequence is the exact identification of the exponent lattice as the valuation skeleton/quotient of the finite ideles and of `log n` as its idelic norm coordinate. This shows that a functional-equation mechanism based only on the infinite prime torus is structurally incomplete: Tate’s natural mechanism requires additive local-field Fourier structure, local unit groups, the archimedean place, self-dual measures, and Poisson summation.

## The exponent lattice is the valuation skeleton of the finite ideles

For each prime `p`,

```text
Q_p^× = p^Z x Z_p^×.
```

The restricted-product definition of the finite ideles therefore gives the valuation homomorphism

```text
nu : A_f^× -> direct_sum_p Z,
nu(x) = (v_p(x_p))_p,
```

whose kernel is

```text
Zhat^× = product_p Z_p^×.
```

Consequently

```text
A_f^× / Zhat^×  ≅  Z^(P),
```

where `Z^(P)` means finite-support integer vectors indexed by primes.

The exponent vector of a positive rational number lives naturally in this signed lattice. Positive integers are exactly the nonnegative cone:

```text
n = product_p p^{v_p(n)},   v_p(n)>=0
      -> v(n) in N_0^(P) subset Z^(P).
```

Taking the Pontryagin dual of `Z^(P)` gives the infinite prime torus. Thus the Bohr torus is naturally the compact dual of this **valuation quotient**, not the full adelic object. Passing to the quotient has discarded all local unit data and all additive field structure.

This identification is standard arithmetic structure, not a novelty claim.

## `log n` is the finite idelic norm coordinate

Normalize the local absolute values by

```text
|p|_p = p^(-1).
```

For a positive integer `n`,

```text
|n|_p = p^(-v_p(n)),
```

so

```text
-log |n|_p = v_p(n) log p.
```

Summing over the finite places gives exactly the prime-lattice linear functional:

```text
-sum_p log |n|_p
    = sum_p v_p(n) log p
    = log n.
```

The global product formula for `Q` says

```text
|a|_infinity product_p |a|_p = 1
```

for every nonzero rational `a`. Therefore, for positive integers,

```text
log |n|_infinity = -sum_p log |n|_p.
```

The archimedean coordinate is therefore not an arbitrary correction added later to the prime energies: it is the exact global balancing coordinate forced by the product formula.

## Tate’s zeta integral supplies the genuine continuation bridge

Let `A` be the adele ring and let `f` be a Schwartz–Bruhat function. Tate defines the global zeta integral

```text
Z(f,chi) = integral_{A^×} f(x) chi(x) d^×x.
```

For a character of exponent `sigma>1`, this integral converges and factorizes into local zeta integrals. For the standard unramified data over `Q`:

- at every finite prime, `f_p=1_{Z_p}` and `chi_p=|.|_p^s` produce the local factor `(1-p^(-s))^(-1)`;
- at infinity, the self-dual Gaussian `f_infinity(x)=exp(-pi x^2)` produces `pi^(-s/2) Gamma(s/2)`.

Thus in its initial domain

```text
Z(f,|.|^s)
  = pi^(-s/2) Gamma(s/2) zeta(s).
```

The important domain distinction is that this factorization is initially an `Re(s)>1` statement. Tate’s global theorem separately proves that `Z(f,chi)` has meromorphic continuation and satisfies

```text
Z(f,chi) = Z(f_hat, chi^vee),
chi^vee = chi^(-1)|.|.
```

For the standard self-dual test function `f_hat=f`, the functional equation of the completed zeta follows. The critical-strip identity is therefore justified by the **global Fourier/Poisson theorem**, not by pretending that the prime Euler product still converges there.

## Why `Re(s)=1/2` is canonical in the completed harmonic picture

Every idele-class character can be written

```text
chi = eta |.|^s
```

for a unitary character `eta`. Tate’s twisted dual is

```text
chi^vee
  = chi^(-1)|.|
  = eta^(-1)|.|^(1-s).
```

Since `eta` is unitary,

```text
conj(eta)=eta^(-1),
```

and hence

```text
conj(chi)=eta^(-1)|.|^(conj(s)).
```

Therefore

```text
chi^vee = conj(chi)
  <=> 1-s = conj(s)
  <=> Re(s)=1/2.
```

The same statement can be expressed by centering the modulus:

```text
chi |.|^(-1/2)
  = eta |.|^(s-1/2),
```

which is unitary precisely when `Re(s)=1/2`.

This gives a rigorous geometric/harmonic meaning to the critical line that is stronger than merely rewriting `s -> 1-s` in prime coordinates: the line is the unitary/Hermitian fixed axis of the duality induced by additive Fourier transform and multiplicative Mellin theory.

It does **not** imply RH. The functional equation forces symmetry of the zero divisor under reflection across the line; it does not force every nontrivial zero onto the fixed axis.

## Why the bare prime torus is insufficient

The Bohr prime torus is the Pontryagin dual of the signed valuation lattice

```text
Z^(P) = A_f^× / Zhat^×.
```

That quotient remembers prime valuations and therefore the frequencies `log p`, but it forgets precisely the structures Tate uses to produce analytic continuation and the functional equation:

- the additive groups of the local fields `Q_p`;
- additive characters and self-dual Haar measures;
- the local unit groups `Z_p^×` and ramification data;
- the archimedean additive place and its Gaussian/gamma factor;
- the global embedding of `Q` in the adeles and Poisson summation on `A/Q`.

Consequently a proposal of the form

```text
prime exponent lattice / T^infinity alone
    -> Fourier duality
    -> s <-> 1-s
```

has not yet supplied the classical mechanism that actually makes the functional equation true. To succeed, it must add structure equivalent in mathematical force to the missing adelic/archimedean completion, or exhibit a genuinely different canonical continuation mechanism.

This is the negative component of the finding: **the ordinary Fourier theory of the prime torus does not by itself contain Tate’s Fourier–Mellin duality.**

## Relation to previous `prime_lattice` findings

This result sharpens several earlier obstructions rather than contradicting them.

- `PL-001` showed that `1/2` is already a natural Hardy evaluation boundary. Tate supplies a different, completed harmonic reason for the same numerical line: the unitary axis of twisted duality.
- `PL-003` and `PL-012` showed that generic prime-phase geometry does not single out the Riemann function. Tate identifies concrete additional global structure absent from those phase-only models.
- `PL-011` ruled out mixing/resonance arising from the bare Kronecker rotation. Tate’s mechanism does not require such mixing; it uses additive Fourier duality and Poisson summation on the full adele ring.
- `PL-013` showed that the completed Weil explicit-formula route needs the archimedean contribution in addition to prime-power data. Tate explains at an earlier harmonic level why finite-prime data and the archimedean place belong to one global self-dual object.

The recurring pattern is therefore no longer only negative: the natural completion of the prime valuation skeleton is known, and it is **adelic rather than merely toral**.

## Prior art and novelty assessment

The mathematical mechanism is classical.

- Tate’s 1950 thesis, published in the Cassels–Fröhlich volume in 1967, introduced the adelic Fourier-analysis proof of meromorphic continuation and functional equations for Hecke zeta/L-functions.
- Poonen’s modern notes give an explicit audit-friendly treatment of the twisted dual `chi^vee=chi^(-1)|.|`, the decomposition `chi=eta|.|^s`, global zeta integrals, the product formula, and the global functional equation.
- Ramakrishnan–Valenza give a comprehensive modern treatment of Fourier analysis on number fields and Tate’s thesis.

No novelty is claimed for the adelic construction, the product formula, or the self-dual axis. The derived Mathia consequence is the exact placement of the prime exponent lattice inside this classical machinery: it is the valuation quotient/positive cone, while its `log n` functional is the finite idelic norm balanced by the archimedean place. This materially redirects the search from inventing a functional equation inside the bare torus toward asking whether any genuinely new lattice structure survives or assists the full adelic/completed problem.

## Boundary conditions and failure modes

- The Euler product and local-factor multiplication giving `zeta(s)` are initially justified only for `Re(s)>1`. The critical-strip continuation comes from Tate’s meromorphic continuation theorem for global zeta integrals.
- The completed function in the Tate integral convention is `pi^(-s/2)Gamma(s/2)zeta(s)`; this should not be confused with conventions that call the entire function obtained by also multiplying by `s(s-1)/2` the Riemann `xi` function.
- `Re(s)=1/2` being the unitary self-dual axis does not establish the location of zeros. It explains the symmetry axis, not RH.
- The quotient `A_f^×/Zhat^×` captures valuations only. Claims about ramified characters, additive Fourier transforms, epsilon factors, or the gamma factor cannot be reconstructed from that quotient without additional data.
- The exponent-vector interpretation applies directly to positive rationals/integers inside the valuation lattice; the full idele class group contains far more information.
- A different non-adelic mechanism is not logically ruled out. The obstruction applies to claims that the **bare** prime torus or valuation lattice already contains the natural Fourier mechanism of the functional equation.

## Audit / falsification criterion

The finding is auditable through four independent checks:

1. Verify the local decomposition `Q_p^×=p^Z x Z_p^×`, hence `A_f^×/Zhat^× ≅ direct_sum_p Z` and the embedding of exponent vectors as its nonnegative cone.
2. Verify the product formula and the exact identity `log n=-sum_p log|n|_p=log|n|_infinity` for positive integers.
3. Verify Tate’s definitions and theorem: `chi^vee=chi^(-1)|.|`, every idele-class character is `eta|.|^s` with `eta` unitary, and `Z(f,chi)=Z(f_hat,chi^vee)` after meromorphic continuation.
4. Check algebraically that `chi^vee=conj(chi)` is equivalent to `Re(s)=1/2`.

The negative conclusion would be falsified by an explicit construction on the valuation quotient / prime torus alone that canonically recovers the required additive Fourier transform, archimedean gamma factor, and global continuation without importing equivalent additional structure. Merely writing the already-known functional equation in torus coordinates does not satisfy that test.

## Consequence for the research line

The prime exponent lattice is not an isolated alternative geometry: it is the positive valuation skeleton of a much richer classical harmonic object. In that completed object, the critical line has a precise and natural meaning as the unitary/Hermitian self-dual axis of Tate’s Fourier–Mellin involution, and analytic continuation is achieved by a genuine global Fourier/Poisson mechanism.

This is a substantial prior-art redirect. The remaining RH problem is no longer to explain why `1/2` is the natural symmetry axis; classical adelic harmonic analysis already does that. A `prime_lattice` advance would need to explain **why the zero divisor should concentrate on that self-dual axis**, or show that some nontrivial information in the exponent lattice can control a completed adelic/Weil positivity or spectral mechanism beyond what Tate’s theory already provides.