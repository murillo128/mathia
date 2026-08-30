# PL-043 — Fourier–Sonine spectral geometry is too flexible; zeta-specific canonical-system positivity is the missing condition

## Claim

A substantially richer completion of the prime-exponent picture than the bare Bohr torus already exists in the Fourier/co-Poisson/de Branges literature, but it does **not** by itself localize the Riemann zero divisor.

Jean-François Burnol links the Riemann zeros, the co-Poisson formula, additive Fourier transform, and de Branges Sonine spaces. Inside that setting there are distinguished Sonine-cosine structure functions `A_a(s)` and `B_a(s)` whose zeros lie on the symmetry line and admit a genuine self-adjoint Dirac/Schrödinger spectral interpretation. Burnol also proves that these special functions have, to first order, the same asymptotic zero density as the completed Riemann zeta function.

However, the ambient Sonine class is far too flexible to force RH: Burnol explicitly notes that RH does not hold for all Sonine functions, that one may add arbitrarily chosen zeros, and that one can construct a Sonine function with no zeros in the critical strip. Thus the route

```text
additive Fourier/co-Poisson completion
+ Sonine/de Branges Hilbert geometry
+ self-adjoint spectral realization for special structure functions
+ zeta-like first-order zero density
    -> force the actual Riemann zeros onto Re(s)=1/2
```

fails at the localization step. The ambient harmonic/Hilbert structure supports both perfectly localized special structure functions and Sonine functions with freely movable zero data.

Masatoshi Suzuki's zeta-specific canonical-system program identifies precisely what additional statement would be needed. For

```text
Theta_omega(z)
  = xi(1/2-omega-i z) / xi(1/2+omega-i z),
omega > 0,
```

he proves that, for every `omega_0 >= 0`,

```text
zeta(s) != 0 for Re(s) > 1/2 + omega_0
    <=>
Theta_omega is a meromorphic inner function
for every omega > omega_0.
```

Hence RH is equivalent to the corresponding innerness condition for every `omega>0`. When the relevant Hermite–Biehler/de Branges condition holds, the zeros of the associated real entire functions are spectra of self-adjoint extensions, and a positive-semidefinite canonical Hamiltonian exists. Suzuki constructs the zeta-derived canonical system unconditionally in a safer range (`omega>1` in the stated theorem) and explains that an unconditional extension through all `omega>0` would yield an RH criterion in terms of the positive-semidefiniteness of the Hamiltonian family.

Therefore **the de Branges/canonical-system machinery does not make the critical-line positivity automatic**. In the zeta specialization, the required positivity/innerness is already equivalent to, or contains, the hard zero-free statement. The mathematically live problem is not to find another Hilbert-space or self-adjoint representation of a related entire function, but to derive the zeta-specific Hermite–Biehler/Hamiltonian positivity from independent arithmetic structure.

**Evidence/status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the specific route that treats ambient Fourier/co-Poisson/Sonine/de Branges spectral geometry, or the existence of nearby self-adjoint zero models, as sufficient localization rigidity for the Riemann divisor. This finding does **not** rule out a de Branges proof of RH; it isolates the exact additional arithmetic positivity theorem such a proof would have to establish.

## The Fourier/co-Poisson completion is genuinely beyond the Euler product

This candidate is materially stronger than another reformulation inside the prime torus.

Burnol's construction starts from additive Fourier analysis and the co-Poisson formula. Mellin transform then connects support conditions for a function and its Fourier transform to entire-function Hilbert spaces of Sonine type. In the 2004 paper he explicitly links three previously separate themes:

```text
Hilbert-space properties of the Riemann zeros
        +
co-Poisson / dual Poisson summation
        +
de Branges Sonine spaces.
```

This matters for `prime_lattice` because `PL-014` already showed that the bare valuation/exponent lattice is only the finite multiplicative skeleton: genuine continuation and the functional equation require additive Fourier structure and the archimedean completion. Burnol works on precisely that richer side of the boundary. The negative below therefore cannot be dismissed as another failure caused merely by staying inside `Re(s)>1` or by forgetting the additive Fourier transform.

The prime-exponent coordinates still enter through the ordinary Dirichlet/Mellin arithmetic of zeta,

```text
log n = <v(n),(log p)_p>,
```

but the Sonine/co-Poisson completion is an external global structure rather than an operation on the free exponent cone alone.

## Special Sonine structure functions really do have the hoped-for spectral geometry

Burnol constructs distinguished de Branges Sonine-cosine structure functions, denoted in his paper by complete Mellin transforms `A_a(s)` and `B_a(s)`. He records three properties that make them an unusually strong matched comparison for a Hilbert–Pólya search.

First, they satisfy the analogue of RH: their zeros lie on the symmetry axis. This is not a numerical observation; it follows from their role as de Branges structure functions.

Second, Burnol associates intrinsic differential operators to the Fourier transform. Under suitable boundary conditions the relevant second-order operators are self-adjoint with discrete spectrum, and the squared imaginary parts of the zeros of `A_a(s)` and `B_a(s)` occur as eigenvalues. Thus this is a genuine spectral theorem, not merely a determinant engineered to vanish at prescribed points.

Third, Burnol proves that these special structure functions have, to principal order, the same asymptotic zero density as

```text
pi^(-s/2) Gamma(s/2) zeta(s).
```

So a superficial checklist would look extremely favorable:

```text
Fourier self-duality        yes
Hilbert space of entire functions  yes
symmetry line singled out   yes
self-adjoint operator       yes
discrete spectrum           yes
zeta-like zero density      yes.
```

Nevertheless these facts do not transfer the localization theorem to zeta.

## Decisive matched control: the ambient Sonine class admits arbitrary zero defects

Burnol states the obstruction explicitly in his conclusion. The zeta/Dirichlet completeness theorems he studies are instances of more general Sonine-space statements, and **RH does not hold for all Sonine functions**. He notes that arbitrarily chosen zeros may be added and that it is easy to construct a Sonine function with no zeros in the critical strip.

This is the exact matched control needed for the research line. It shows that the following properties, taken as ambient structure, are insufficient:

```text
Sonine support constraints,
Fourier-transform compatibility,
complete Mellin transform,
functional symmetry,
Hilbert-space evaluation/completeness machinery.
```

The special structure functions `A_a,B_a` are much more rigid than a generic Sonine vector. Their real-zero property is a consequence of the de Branges **structure-function** role, not a theorem saying every zeta-linked Sonine transform must have such zeros.

Accordingly, one cannot argue

```text
zeta is linked by co-Poisson to Sonine spaces
and Sonine structure functions have self-adjoint real spectra
therefore zeta zeros should be forced to the same axis.
```

That inference confuses a special Hermite–Biehler structure function with an arbitrary vector/function living in, or linked to, the broader Sonine framework.

## Suzuki isolates the zeta-specific hard condition

Suzuki's construction makes the remaining gap unusually explicit. Define

```text
E^omega(z) = xi(1/2 + omega - i z)
```

and

```text
Theta_omega(z)
  = E^omega_sharp(z) / E^omega(z)
  = xi(1/2-omega-i z) / xi(1/2+omega-i z).
```

If `E^omega` satisfies the Hermite–Biehler inequality in the upper half-plane, it generates a de Branges space. General de Branges theory then supplies a symmetric multiplication operator with self-adjoint extensions whose discrete spectra are the zeros of the associated real entire functions `A^omega` and `B^omega`, together with a canonical first-order system

```text
d/da [A_a(z); B_a(z)]
  = z J H(a) [A_a(z); B_a(z)]
```

with a real positive-semidefinite Hamiltonian matrix `H(a)`.

But the Hermite–Biehler/inner property is exactly where the arithmetic difficulty lives. Suzuki proves the zero-free/inner equivalence

```text
zeta(s) != 0 on Re(s) > 1/2 + omega_0
    <=>
Theta_omega is meromorphic inner for every omega > omega_0.
```

Taking `omega_0=0` gives an RH-equivalent family condition. Thus the fact that a de Branges space, positive Hamiltonian, or self-adjoint spectral family would localize the corresponding zeros is not the missing theorem; **showing that the zeta-derived data actually satisfy the hypotheses throughout the critical range is the missing theorem**.

Suzuki constructs the relevant canonical system explicitly and unconditionally for `omega>1`. His stated program is to extend the construction to all `omega>0`; doing so with the required positivity/boundary properties would give a criterion for RH. This is direct prior art for the exact route a prime-lattice completion might otherwise rediscover.

## Relation to `PL-041` and `PL-042`

`PL-041` and `PL-042` showed that standard model-space and Clark spectralizations are universal once an inner divisor has already been supplied. An arbitrary Blaschke zero has the same co-shift eigenmode structure and positive Clark boundary measure, so those constructions cannot localize the divisor.

The Fourier/Sonine candidate is a stronger escape because it brings in additive Fourier transform, support duality, and co-Poisson arithmetic rather than merely repackaging an arbitrary inner function. Burnol's matched control shows that this stronger ambient structure is still not enough: the general Sonine class retains zero flexibility.

Suzuki then identifies the precise non-universal layer absent from the controls:

```text
zeta-specific Theta_omega
        +
Hermite–Biehler / innerness
        +
positive-semidefinite canonical Hamiltonian.
```

Unlike Clark positivity, this positivity is **not automatic** for arbitrary data. That makes it a legitimate possible carrier of RH rigidity — but also means that proving it is essentially the hard arithmetic step rather than a consequence of general spectral theory.

## Analytic-continuation boundary

No Euler product is termwise continued into the critical strip in this finding.

Burnol's Sonine statements concern complete Mellin transforms and Fourier/co-Poisson identities in Hilbert spaces of entire functions. The special structure functions and their spectral interpretation are entire-function/Fourier results.

Suzuki works with the completed entire function `xi(s)` and the meromorphic quotient `Theta_omega`. His zero-free/inner equivalence is an analytic theorem about the continued zeta/xi functions, not an Euler-product identity asserted outside absolute convergence.

Therefore the negative survives the continuation boundary correctly: even after supplying a genuine additive-Fourier completion and entire-function spectral framework, localization still requires an extra zeta-specific positivity statement.

## Prior art and novelty audit

The mathematical ingredients are established prior art:

- **Louis de Branges**, “A conjecture which implies the Riemann hypothesis,” *Journal of Functional Analysis* **121**(1) (1994), 117–184, DOI `10.1006/jfan.1994.1046`. This is direct classical prior art for seeking an RH mechanism through Hilbert spaces of entire functions/canonical systems; no novelty is claimed for that research program.
- **Jean-François Burnol**, “Two complete and minimal systems associated with the zeros of the Riemann zeta function,” *Journal de Théorie des Nombres de Bordeaux* **16**(1) (2004), 65–94, DOI `10.5802/jtnb.434`, arXiv:`math/0203120`. This is the main source for the co-Poisson/Sonine/zeta bridge, the special de Branges structure functions, their first-order zeta-like zero density, and the explicit warning that generic Sonine functions can have arbitrarily chosen zeros.
- **Jean-François Burnol**, “Des équations de Dirac et de Schrödinger pour la transformation de Fourier,” *Comptes Rendus Mathématique* **336**(11) (2003), 919–924, DOI `10.1016/S1631-073X(03)00223-1`, arXiv:`math/0302102`. This supplies the intrinsic Fourier Dirac/Schrödinger systems and self-adjoint spectral background cited in the 2004 paper.
- **Masatoshi Suzuki**, “A canonical system of differential equations arising from the Riemann zeta-function,” *RIMS Kôkyûroku Bessatsu* **B34** (2012), 397–435; arXiv:`1204.1827` (revised 2016). This gives the explicit `Theta_omega` innerness criterion and zeta-derived canonical-system program, including the unconditional construction in the stated `omega>1` range and the all-`omega` RH criterion.

The durable contribution here is **not** any of these constructions. It is the research-line audit tying them to the current escape route: adding global Fourier/co-Poisson/Sonine/de Branges spectral geometry does not by itself overcome the zero-flexibility obstructions already seen in simpler models, while the non-universal zeta-specific Hamiltonian positivity needed to overcome them is itself classical prior art and encodes the hard RH condition.

A targeted literature audit also finds later canonical-system work extending this program to broader L-function classes and modern Weil/de Branges formulations. That reinforces, rather than weakens, the prior-art redirect: canonical-system positivity is an established RH-equivalent target, not a new consequence of exponent-lattice geometry.

## Boundaries and escape tests

### This does not rule out de Branges as a route to RH

A proof that constructs the correct zeta canonical system **unconditionally** in the full range and proves the required Hamiltonian positivity would be highly substantive and could prove RH. The finding only says that general de Branges/Sonine/Fourier machinery does not supply that positivity for free.

### Special structure functions are not generic Sonine functions

The fact that Burnol's `A_a,B_a` have symmetry-line zeros must not be generalized to all Sonine transforms. The arbitrary-zero control is precisely why the distinction matters.

### Matching first-order zero density is not localization

Burnol's special functions sharing the principal asymptotic density of zeta zeros is a useful spectral analogy, but it does not determine individual zero locations. The generic Sonine zero flexibility makes this failure explicit.

### A genuine arithmetic positivity identity remains open

This result would be escaped by a theorem deriving the zeta-specific Hermite–Biehler or Hamiltonian positivity from an independent arithmetic identity — for example a non-circular bridge to Weil positivity, the distinguished Nyman target/Möbius data, or another exact observable that fails for generic Sonine functions and arbitrary inner controls.

Such a theorem would not be “another spectral representation”; it would be the missing rigidity mechanism.

## Consequence for the research line

The surviving chain can now be stated more sharply:

```text
bare prime exponent lattice / Bohr torus
    -> insufficient for continuation or zero localization          [PL-003, PL-014]

standard target-relative inner/model spectralization
    -> universal for arbitrary Blaschke data                       [PL-041, PL-042]

global additive Fourier/co-Poisson/Sonine completion
    -> genuinely zeta-adjacent and has special self-adjoint
       symmetry-line models
    -> but ambient Sonine class permits arbitrary zero defects     [PL-043]

zeta-specific de Branges/canonical-system positivity
    -> exact non-universal localization condition
    -> already a classical RH-equivalent/conditional program
    -> not yet derived from the prime lattice or another
       independent arithmetic positivity mechanism.
```

Accordingly, the next useful search should not be “find a Fourier/de Branges operator whose related structure function has real zeros.” That already exists. The live target is an **independent arithmetic mechanism forcing the zeta-derived Hermite–Biehler/canonical Hamiltonian positivity**, ideally one that can be expressed in the prime-exponent/explicit-formula language and that fails under Burnol's arbitrary-Sonine and earlier Beurling/inner-function controls.