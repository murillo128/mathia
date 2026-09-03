# PL-136 — Degree-one Selberg rigidity collapses the full unimodular prime-phase torus to zeta

## Claim

Let `omega=(omega_p)_p` be an arbitrary point of the full prime torus, with `|omega_p|=1` for every rational prime, and extend it completely multiplicatively by

`omega(n)=product_p omega_p^(v_p(n))`.

For `Re(s)>1` define the associated Helson/Euler product

`F_omega(s)=sum_(n>=1) omega(n)n^(-s)=product_p (1-omega_p p^(-s))^(-1)`.

The prime-exponent lattice and the unimodular phase choice automatically supply the two local/coefficient conditions that are usually the easy part of the Selberg-class axioms: `|omega(n)|=1`, and

`log F_omega(s)=sum_(p,k>=1) omega_p^k/(k p^(ks))`

in the half-plane of absolute convergence, with prime-power logarithmic coefficients bounded uniformly. If, in addition, `F_omega` satisfies the **global analytic and functional-equation package of a degree-one Selberg-class element**, then classical degree-one classification forces

`F_omega(s)=zeta(s)`

and therefore

`omega_p=1` for every prime `p`.

Equivalently, in phase coordinates `omega_p=e^(i theta_p)`, the full infinite-dimensional torus collapses to the identity point once the degree-one Selberg global constraints are imposed.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + POSITIVE-DISCRIMINATOR`.

The degree-one classification is classical prior art of Kaczorowski--Perelli, with a short proof by Soundararajan. The specialization to an everywhere-unimodular completely multiplicative prime phase is an immediate derived corollary. No novelty is claimed for the classification theorem, Dirichlet characters, or the Selberg class. The durable value is as a matched rigidity benchmark against the Helson flexibility in `PL-003` and the converse-theorem rigidity in `PL-126`.

## The prime torus automatically gives the easy Selberg data

Unique factorization gives

`omega(n)=product_p omega_p^(v_p(n))`,

so `omega` is completely multiplicative and `|omega(n)|=1`. Hence its Dirichlet series is absolutely convergent for `Re(s)>1`, and in that same honest half-plane

`F_omega(s)=product_p (1-omega_p p^(-s))^(-1)`.

Taking logarithms there gives

`log F_omega(s)=sum_p sum_(k>=1) omega_p^k/(k p^(ks))`.

In Soundararajan's normalization of Selberg Axiom 4,

`log F(s)=sum_(n>=2) b(n)n^(-s) Lambda(n)/log n`,

the factor `Lambda(p^k)/log(p^k)=1/k` is already explicit. Hence for the present product

`b(p^k)=omega_p^k`,

and `b(n)=0` off prime powers. Thus `|b(p^k)|=1`, satisfying the required `b(n) << n^vartheta` for any fixed `vartheta>0` (in particular for some `vartheta<1/2`). The Ramanujan coefficient condition is also automatic because `|omega(n)|=1`.

Nothing in these local facts gives analytic continuation or a functional equation. This is exactly the distinction already exposed by the Helson-zeta controls: arbitrary prime phases can have highly flexible continuation and zero/pole geometry. The additional assumptions below are genuinely global.

## Degree-one classification forces a shifted Dirichlet L-function

Kaczorowski and Perelli classified the degree-one part of the Selberg class. Soundararajan's short proof states the result in a form especially convenient here: for a degree-one element `F`, the Dirichlet coefficients become periodic after multiplication by a phase `n^(-iA)`; after the Euler-product axiom is imposed, multiplicativity identifies the periodic sequence with a primitive Dirichlet character. In particular there exist a real number `A` and a primitive Dirichlet character `chi` such that

`F(s)=L(s+iA,chi)`.

Primary classification references:

- Jerzy Kaczorowski, Alberto Perelli, “On the structure of the Selberg class, I: `0 <= d <= 1`,” *Acta Mathematica* **182** (1999), 207--241. DOI: https://doi.org/10.1007/BF02392574.
- Kannan Soundararajan, “Degree 1 elements of the Selberg class,” *Expositiones Mathematicae* **23**(1) (2005), 65--70. DOI: https://doi.org/10.1016/j.exmath.2005.01.013. arXiv: https://arxiv.org/abs/math/0306300.

The theorem is a classification of the global analytic class. It must not be read as a formal continuation of the Euler product from `Re(s)>1`.

Apply it to `F_omega`. In the common half-plane of absolute convergence, uniqueness of Dirichlet-series coefficients gives

`omega(n)=chi(n)n^(-iA)`

for every `n>=1`. In particular, at every prime,

`omega_p=chi(p)p^(-iA)`.

Because `|omega_p|=1` for **every** rational prime, `chi(p)` cannot vanish. A primitive character of conductor `q>1` vanishes at every prime dividing `q`, so this is impossible. Hence the primitive conductor is `q=1`, and `chi` is the trivial character. Therefore

`F_omega(s)=zeta(s+iA)`

and

`omega_p=p^(-iA)`.

The standard Selberg analytic axiom allows a pole only at `s=1`. But `zeta(s+iA)` has its pole at `s=1-iA`; therefore `A=0`. Consequently

`F_omega(s)=zeta(s)`

and coefficient comparison in `Re(s)>1` yields

`omega_p=1` for every prime.

This last pole argument matters. Nontrivial vertical shifts of entire primitive Dirichlet `L`-functions can occur in the degree-one classification, but the everywhere-nonzero unimodular local coefficients force conductor one first; once the resulting function is shifted zeta, the allowed pole location removes the shift.

## Relation to the prime-exponent geometry

In exponent coordinates, the deformation is exactly

`omega(n)=exp(i <v(n),theta>)`,

with `theta=(theta_p)_p`. Thus this is not a deformation of an auxiliary representation: it is the full Pontryagin-dual phase freedom of the free positive prime-exponent monoid itself.

`PL-003` records the opposite ambient fact: without strong global constraints, this torus is far too flexible. Helson-zeta constructions can prescribe broad zero/pole data after continuation. `PL-136` identifies a sharp complementary boundary:

`bare prime-phase torus + Euler product` remains flexible,

whereas

`bare prime-phase torus + degree-one Selberg continuation/functional equation/growth package` is rigid enough to leave only ordinary zeta.

This gives a precise answer to one part of the research mandate. The global analytic continuation and functional equation do not merely reduce the phase freedom perturbatively; in the degree-one Selberg category they eliminate it completely.

## Why this is not an RH mechanism

The rigidity theorem identifies the distinguished function, not the location of its zeros. Once the phase torus has collapsed to `omega_p=1`, the surviving object is simply ordinary zeta and the statement

`all nontrivial zeros have Re(s)=1/2`

is still exactly RH. Degree-one Selberg classification therefore supplies **arithmetic identity rigidity**, not spectral positivity or zero localization.

The critical line is also not derived from the abstract exponent lattice. It enters through the global degree-one functional equation supplied as a Selberg-class hypothesis. This is analogous to `PL-126`, where Hamburger rigidity distinguishes zeta from integer Grosswald--Schnitzer deformations once the exact Riemann completion is imposed. The present result is nevertheless distinct: it treats the canonical **full unimodular prime torus** directly and uses the broader degree-one Selberg classification rather than the exact Hamburger self-dual equation.

## Adversarial controls and boundary conditions

The degree-one hypothesis is load-bearing. This finding does not show that an arbitrary unimodular completely multiplicative Dirichlet series satisfying some weaker functional equation must be zeta, nor does it exclude a hypothetical higher-degree analytic completion built from such coefficients. The classification theorem used here is specifically the `d=1` Selberg theorem.

The full-modulus condition `|omega_p|=1` at every prime is also load-bearing. Ordinary primitive Dirichlet characters of conductor `q>1` have zero local coefficients at ramified primes, which is exactly how nontrivial degree-one Selberg elements escape the conclusion. If the prime torus is enlarged to allow coordinates of modulus zero at finitely many primes, the natural surviving objects are Dirichlet `L`-functions rather than only zeta.

The Euler product and Dirichlet coefficient comparison are used only for `Re(s)>1`. Meromorphic continuation and the functional equation are invoked through the Selberg classification theorem. No Euler product is asserted in the critical strip.

A Beurling/generalized-prime replacement also breaks the argument at its arithmetic hinge: Kaczorowski--Perelli classify ordinary Dirichlet series on the integer frequency set `log n`. The result therefore says that **ordinary integer prime/exponent coordinates plus the global degree-one analytic package** are rigid; it does not claim that a free generalized-prime monoid has the same classification.

## Prior-art and novelty audit

The classification `degree 1 Selberg => shifted primitive Dirichlet L-function` is established classical literature. Searches around Helson zeta functions, completely multiplicative unimodular coefficients, degree-one Selberg elements, and functional equations did not expose a source presenting the exact full-prime-torus corollary as a separate theorem, but that absence is not evidence of novelty. The corollary is elementary once the classification is known and should be treated as derived organization for this research line.

Modern Helson literature points strongly in the opposite direction when the global Selberg package is absent. Bochkov--Romanov and later work construct Helson zeta functions with very flexible prescribed continuation divisors. Those results remain valid matched controls: `PL-136` does not retract `PL-003`; it identifies exactly which added global assumptions make that control cease to be matched.

The closest internal overlap is `PL-126`. That finding uses Hamburger's theorem to show that an integer Grosswald--Schnitzer same-zero deformation cannot preserve the exact Riemann functional equation in the ordinary finite-order Dirichlet class. `PL-136` instead starts from the canonical dual torus of the exponent lattice, allows arbitrary unimodular phases at every prime, and shows that the **degree-one Selberg class itself has no nontrivial point on that torus**. This is a different falsification boundary and is worth storing separately.

## Audit test and consequence for the line

Any future proposal claiming an RH-relevant mechanism from a special phase point of the prime torus should first ask whether its proposed analytic package reaches the hypotheses of degree-one Selberg classification.

If it does, then the phase-selection problem is already solved classically: the only everywhere-unimodular point is the zeta point. The proposal must contribute something genuinely beyond identification, such as positivity, unitarity, a Hodge-type form, or a trace/resonance principle that constrains the zero divisor.

If it does not, then the proposal must explain why its weaker structure defeats the Helson flexibility of `PL-003`. Merely having an Euler product, a prime-frequency flow, or an approximate reflection symmetry is insufficient.

The resulting boundary for `prime_lattice` is therefore sharp: **global degree-one converse rigidity can canonically select the identity point of the prime torus, but the unresolved RH content begins only after that selection.**