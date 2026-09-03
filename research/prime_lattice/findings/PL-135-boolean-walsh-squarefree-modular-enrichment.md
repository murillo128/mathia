# PL-135 — Squarefree Boolean-Walsh modular symmetry is a finite-level enrichment, not a zeta-zero localization mechanism

## Claim

For a fixed squarefree level

`M = product_(p|M) p`,

the divisor set `D(M)` is literally the finite Boolean sector of the prime-exponent lattice,

`D(M) <-> {0,1}^{P_M}`,

and the Boolean/Walsh Fourier basis diagonalizes several natural operators attached to squarefree modular data. A July 2026 preprint of K. Srinivasa Raghava organizes this explicitly: the same Walsh characters diagonalize the squarefree Ligozat cusp-order matrix, Fricke complementation, Atkin--Lehner action on cusp labels, and the constant-term map for logarithmic weight-two Eisenstein series.

This is a genuine enrichment beyond the bare exponent-vector encoding: the finite prime cube is coupled to modular units, cusps, and modular involutions. But it does **not** supply a Riemann-Hypothesis mechanism. In the associated Dirichlet series the Boolean cube contributes only a finite Euler polynomial, while the infinite analytic factor is the classical Eisenstein product `zeta(u) zeta(u-1)`. The modular continuation and Fricke symmetry come from the eta/Eisenstein structure in the modular variable `tau`; they neither derive a symmetry in the Riemann spectral variable `s` from the bare lattice nor force zeta zeros onto `Re(s)=1/2`.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE/OBSTRUCTION`.

The finite Boolean identities below are elementary and are independently derivable. The modular-unit/Eisenstein claims are attributed to Raghava's unrefereed arXiv preprint and are used as current prior-art/structural evidence, not promoted beyond the paper's status. No novelty is claimed for Boolean Fourier analysis, eta transformations, Ligozat cusp orders, Atkin--Lehner theory, or Eisenstein Dirichlet series.

Primary current source:

- K. Srinivasa Raghava, “Boolean Walsh Eta Units and Eisenstein Bases For Squarefree Levels,” arXiv:2607.11926v1 [math.GM], submitted 10 July 2026, preprint. https://arxiv.org/abs/2607.11926.

## Exact Boolean-cube diagonalization

Identify a divisor `d|M` with its support vector

`alpha(d) = (v_p(d))_(p|M) in {0,1}^{P_M}`.

For `T subseteq P_M`, define the Walsh character

`chi_T(d) = (-1)^{|T intersect supp(d)|}`.

The Fricke complement on divisor labels is

`d -> M/d`,

which in exponent coordinates is simply

`alpha -> 1-alpha`.

Therefore

`chi_T(M/d) = (-1)^{|T|} chi_T(d)`.

So complement is diagonal in the Walsh basis with spectrum `{+1,-1}`. This fact is generic finite-cube harmonic analysis; no arithmetic beyond the chosen coordinate labels is needed.

The squarefree Ligozat matrix used in the preprint has entries

`A_M(c,d) = M gcd(c,d)^2/(cd)`.

At one prime coordinate `p|M`, with local exponents ordered as `0,1`, its local matrix is

`A_p = [[p,1],[1,p]]`.

Hence

`A_M ~= tensor_(p|M) A_p`.

The local Walsh vectors `(1,1)` and `(1,-1)` have eigenvalues `p+1` and `p-1`; tensoring gives the exact eigenvalue

`Lambda_T^(M) = product_(p in T)(p-1) product_(p|M, p notin T)(p+1)`

on the character `chi_T`. This tensor/Walsh diagonalization follows directly from the displayed matrix and does not depend on the stronger modular claims of the preprint.

## The modular enrichment is real but imported

Raghava associates to each nonempty Walsh mode the eta quotient

`R_T^(M)(tau) = product_(d|M) eta(d tau)^{chi_T(d)}`.

The paper claims, and derives from the classical eta transformation and squarefree Ligozat formula, that `(R_T^(M))^24` is a modular unit on `X_0(M)`, with cusp-order vector proportional to the same Walsh character:

`ord_(1/c) R_T^(M) = (Lambda_T^(M)/24) chi_T(c)`.

It further states the Fricke law

`R_T^(M)(-1/(M tau)) = c_T^(M) R_T^(M)(tau)^{(-1)^{|T|}}`,

with an explicit constant `c_T^(M)`, and that exact-divisor Atkin--Lehner involutions act on the corresponding logarithmic derivatives through the eigenvalue `chi_T(Q)`.

This is more than merely redrawing divisors as cube vertices. The extra data couples the Boolean cube to the modular curve, its cusps, eta transformation law, and Eisenstein space. In particular, the same finite Fourier basis simultaneously diagonalizes several independently meaningful modular operators. That makes the construction a useful benchmark for future claims that the squarefree exponent lattice should acquire arithmetic meaning through harmonic duality.

But the enrichment is not intrinsic to the abstract free Boolean cube. A generic finite cube has the same Walsh/complement spectrum and the same tensor diagonalization for any chosen local matrices of the form `[[a,b],[b,a]]`; it has no Dedekind eta function, modular curve, cusp widths, or Atkin--Lehner involutions. The arithmetic content enters through these external modular structures.

## The Dirichlet series exposes where zeta enters

Let

`E_T^(M)(tau) = D log R_T^(M)(tau) = (1/24) sum_(d|M) chi_T(d) d E_2(d tau)`,

with `D = q d/dq`. Using

`E_2(tau)=1-24 sum_(n>=1) sigma_1(n)q^n`,

the nonconstant Fourier coefficients are exactly

`a_T(n) = - sum_(d|M, d|n) chi_T(d) d sigma_1(n/d)`.

For `Re(u)>2`, where the divisor-series manipulations are absolutely convergent,

`sum_(n>=1) a_T(n)n^(-u)
 = - zeta(u) zeta(u-1) sum_(d|M) chi_T(d)d^(1-u)`

and, because `M` is squarefree,

`sum_(d|M) chi_T(d)d^(1-u)
 = product_(p|M) (1 + chi_T(p)p^(1-u))`.

Thus

`sum_(n>=1) a_T(n)n^(-u)
 = -zeta(u)zeta(u-1) product_(p|M)(1+chi_T(p)p^(1-u))`.

This factorization is an exact derived identity in the honest half-plane `Re(u)>2`. Any continuation beyond it comes from the classical meromorphic continuation of the Eisenstein/zeta factors, not from a formal continuation of the finite Boolean Euler factor.

The consequence for `prime_lattice` is sharp: the finite exponent cube alters only finitely many local factors. The two infinite zeta factors are already present in the standard weight-two Eisenstein Dirichlet series. Hence the construction does not convert the Boolean lattice into an operator whose spectrum is the Riemann zero set; rather, it provides a finite-level modular organization around an already classical global analytic object.

## Why Fricke symmetry does not single out the Riemann critical line

On divisor labels, Fricke is complement and Walsh modes have signs `(-1)^{|T|}`. On the upper half-plane it is the modular involution

`tau -> -1/(M tau)`.

Its positive-imaginary fixed point is

`tau_M = i/sqrt(M)`.

That fixed point depends on the arbitrarily chosen squarefree level `M`. It is not a universal vertical axis and is not the Riemann reflection `s -> 1-s`. Sending `M` through larger squarefree levels drives `tau_M` toward the cusp `0`; it does not converge to a canonical counterpart of `Re(s)=1/2`.

Likewise, the Walsh/Atkin--Lehner eigenvalues are finite signs, and the good-prime Hecke eigenvalue stated in the paper is the standard Eisenstein value `1+ell`. None of these quantities yields the imaginary ordinates of the nontrivial Riemann zeros or a positivity condition equivalent to locating them on a line.

This distinction is especially important after `PL-014` and `PL-134`. Tate's adelic Fourier theory and the Hilberdink--Lapidus modular-inversion converse show that genuine zeta functional equations require global additive/Fourier or reciprocal-summation data. The present squarefree construction supplies a concrete modular duality, but in a separate modular variable and at a finite chosen level. It therefore illustrates rather than removes the same boundary: **Boolean exponent geometry can organize global arithmetic structure once that structure is supplied, but does not by itself generate the Riemann functional equation or RH localization.**

## Adversarial controls and failure modes

The strongest tempting interpretation is that complement `alpha -> 1-alpha` is a finite-dimensional shadow of `s -> 1-s`. That analogy fails as a mechanism. Complement exists for every Boolean cube, its fixed locus is combinatorial rather than an analytic zero locus, and its Walsh spectrum is only `+/-1`. The nontrivial analytic symmetry in Raghava's construction is supplied by Dedekind eta inversion and the modular curve.

A second tempting route is to take `M` through primorials and seek an infinite-level limit. The exact Dirichlet factorization already shows the obstruction to a naive version: at every finite level the Walsh choice contributes a finite Euler polynomial multiplying the same global `zeta(u)zeta(u-1)`. A limit would require a separately justified topology, normalization, convergence theorem, and analytic continuation. Without those, passing formally to infinitely many primes would merely rebuild an Euler product and reintroduce the continuation problem that the research mandate forbids hiding.

A third control is Beurling/generalized-prime replacement. The abstract Boolean divisor cube and Walsh complement survive for any finite set of formal prime coordinates. The eta/modular-curve and Atkin--Lehner structures do not survive generically. This is evidence that the interesting arithmetic content is extra global structure specific to classical modular theory, not a consequence of unique factorization or exponent coordinates alone.

Finally, the paper is a current unrefereed preprint in `math.GM`. Its finite tensor/Walsh identities and the displayed Dirichlet factorization are independently checkable, but stronger modular-unit, cusp-divisor, and basis claims should remain attributed to the preprint unless corroborated by peer-reviewed/classical sources. This source-status caveat is part of the finding, not an incidental bibliographic note.

## Prior-art and novelty audit

The paper itself cites the classical foundations: Dedekind eta transformation, Newman/Ligozat eta-quotient theory, modular units, Atkin--Lehner involutions, and standard modular/Eisenstein theory. Searches for combinations of “Walsh/Hadamard,” “Ligozat,” “Atkin--Lehner,” and squarefree eta quotients did not expose an earlier source with the same simultaneous Boolean-Walsh packaging, but that absence is not evidence of novelty. The preprint presents the packaging as its contribution; Mathia makes no independent priority claim.

The durable value here is instead as **matched prior art and a falsification benchmark** for the research line. It demonstrates that a finite squarefree slice of the exponent lattice can genuinely participate in nontrivial harmonic/modular structure. At the same time, the exact Dirichlet factorization localizes what that slice contributes: finitely many Euler factors, while the global zeta/Eisenstein continuation is inherited from classical modular analysis.

This does not duplicate `PL-014`: that finding identifies the adelic additive Fourier mechanism selecting the self-dual Riemann axis. It also does not duplicate `PL-134`: that finding gives a general Beurling theorem equating completed functional equations with reciprocal smoothed summation. The present finding supplies a concrete **squarefree-Boolean modular example** and shows why its natural Fricke/Walsh symmetry remains finite-level and does not become zero localization for Riemann zeta.

## Audit test and consequence for the line

For any future proposal using the squarefree `{0,1}` sector, Walsh characters, divisor complement, or an Atkin--Lehner-like involution as an RH mechanism, separate three layers explicitly:

1. the generic Boolean identities that hold for any finite cube;
2. the additional arithmetic/modular structure that couples those coordinates to a global analytic object;
3. the step that is claimed to constrain the Riemann zero divisor.

If the third layer reduces to a finite Euler polynomial, a level-dependent modular fixed point, or a `+/-1` involution spectrum, it has not supplied zero localization. A surviving route must instead show how an infinite-prime limit or global duality produces a rigorously continued object in the Riemann spectral variable and then adds a positivity/unitarity/Hodge mechanism strong enough to force its zero divisor onto `Re(s)=1/2`.