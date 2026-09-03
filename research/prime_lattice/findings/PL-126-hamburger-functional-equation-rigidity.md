# PL-126 — Hamburger rigidity defeats integer Grosswald–Schnitzer deformations once the Riemann functional equation is imposed

## Claim

`PL-125` supplies a severe falsification control for prime-lattice spectral proposals: Grosswald–Schnitzer may replace the rational primes by nearby numbers `q_n` and obtain a modified Euler product with exactly the same zero divisor as `zeta` in `Re(s)>0`. That control is decisive against mechanisms that depend only on the zero set, on an Euler-product-shaped transfer construction, or on a self-adjoint model fed by inverse coefficients.

However, the control does **not** preserve the full global zeta structure demanded by the canonical `prime_lattice` mandate. Grosswald and Schnitzer themselves state that their modified functions have Dirichlet-series and Euler-product representations but, in general, satisfy no functional equation and often cannot be analytically continued beyond `Re(s)>0`. Classical Hamburger converse theory makes this failure rigid for the integer-valued deformations used by Sierra.

Let `q_n` be rational integers with

`p_n <= q_n <= p_(n+1)`

and define for `Re(s)>1`

`Z_q(s)=prod_(n>=1) (1-q_n^(-s))^(-1)`.

Absolute convergence lets this product expand as an ordinary Dirichlet series

`Z_q(s)=sum_(m>=1) a_q(m)m^(-s)`

with nonnegative integer coefficients. Suppose, in addition, that `Z_q` lies in Hamburger's standard finite-order meromorphic class and satisfies the **same completed Riemann functional equation** as `zeta`. Hamburger's theorem then forces

`Z_q(s)=zeta(s)`.

Since `a_q(1)=1`, no nontrivial scalar multiple remains. Moreover, if the integer sequence `q_n` differs from the prime sequence at all, then `Z_q != zeta`: at the first index `j` with `q_j != p_j`, the prime `p_j` never occurs among the generators `q_n`, so the coefficient of `p_j^(-s)` in `Z_q` is `0`, whereas the corresponding zeta coefficient is `1`.

Therefore every **nontrivial integer Grosswald–Schnitzer deformation is incompatible with the Riemann functional equation inside Hamburger's analytic class**, despite preserving the nontrivial zero divisor in `Re(s)>0`.

**Evidence/status:** `LITERATURE+DERIVED + PRIOR-ART-REDIRECT + POSITIVE-DISCRIMINATOR`.

This is not an RH proof and does not show that the functional equation forces zeros onto `Re(s)=1/2`. It identifies a precise global structure that *does* pass the line's Grosswald–Schnitzer arithmetic-specificity control: compatibility between an ordinary integer Dirichlet expansion and the Riemann self-dual functional equation is rigid enough to recover `zeta` itself. The missing RH step remains positivity/localization of the zero divisor, not identification of the distinguished completed function.

## Grosswald–Schnitzer preserves zeros but explicitly loses the functional equation

Grosswald and Schnitzer define, initially for `Re(s)>1`,

`zeta*(s)=prod_n (1-q_n^(-s))^(-1),    p_n <= q_n <= p_(n+1)`.

Their Theorem 1 proves meromorphic continuation to `Re(s)>0`, a simple pole at `1`, and exactly the same zeros with multiplicity as ordinary zeta in that half-plane. The proof writes

`zeta*(s)=phi(s) zeta(s)`

where `phi` is analytic and nonvanishing in `Re(s)>0`.

The crucial point for the present audit appears already in their introduction: the new functions have a Dirichlet-series representation and an Euler product, but **in general do not satisfy any functional equation**, and often have no continuation past `Re(s)>0`. Thus their theorem deliberately preserves a divisor while relaxing the global analytic structure that Tate/Poisson duality supplies for ordinary zeta.

Primary source:

- Emil Grosswald, F. J. Schnitzer, “A class of modified zeta and L-functions,” *Pacific Journal of Mathematics* **74**(2) (1978), 357–364. DOI: https://doi.org/10.2140/pjm.1978.74.357. The introduction explicitly contrasts the preserved Dirichlet-series/Euler-product structure with the general loss of a functional equation; Theorem 1 proves the same-zero continuation in `Re(s)>0`.

This distinction matters because `PL-125` used the Grosswald–Schnitzer class as a matched control against the claim that exact rational-prime mirror positions or the square-free Möbius lattice by themselves explain the zero spectrum. The present finding does not weaken that conclusion. It shows instead that the control ceases to be matched once a proposal genuinely uses the **full completed functional equation** rather than only the zero divisor or the Euler product.

## Integer deformations remain ordinary Dirichlet series

Sierra uses integer choices of the `q_n`; his explicit example begins `2,4,6,8,12,...`. More generally, assume each `q_n` is an integer satisfying the Grosswald–Schnitzer interval condition. For `sigma>1`,

`sum_n q_n^(-sigma) <= sum_n p_n^(-sigma) < infinity`.

Hence the Euler product converges absolutely. Expanding each geometric series gives

`prod_n sum_(k>=0) q_n^(-ks)`.

Every finite product of integer generators is again an integer, so grouping equal products gives

`Z_q(s)=sum_(m>=1) a_q(m)m^(-s)`,

where `a_q(m)` is the number of multisets of the generators whose product is `m`. Absolute convergence justifies the grouping for `Re(s)>1`. Unique factorization of the `q_n` themselves is not required; indeed, non-unique representations are exactly why some `a_q(m)` can exceed one.

Thus the integer deformation sits inside the ordinary Dirichlet-series category used by Hamburger, not merely the broader category of generalized Dirichlet series with arbitrary frequencies.

## Hamburger's theorem supplies the rigidity

A standard modern statement of Hamburger's theorem is recalled by Kaczorowski, Molteni, and Perelli. Let

`f(s)=sum a(n)n^(-s),    g(s)=sum b(n)n^(-s)`

be absolutely convergent for `Re(s)>1`; suppose `(s-1)f(s)` and `(s-1)g(s)` are entire of finite order and that they satisfy the paired Riemann functional equation

`pi^(-s/2) Gamma(s/2) f(s)
 = pi^(-(1-s)/2) Gamma((1-s)/2) g(1-s)`.

Then

`f(s)=g(s)=c zeta(s)`

for some constant `c`. The same paper notes weaker variants and emphasizes the connection with uniqueness of Poisson summation.

Source:

- Jerzy Kaczorowski, Giuseppe Molteni, Alberto Perelli, “A converse theorem for Dirichlet L-functions,” *Commentarii Mathematici Helvetici* **85**(2) (2010), 463–483. DOI: https://doi.org/10.4171/CMH/202. The introduction states Hamburger's theorem in exactly this form and stresses that the Riemann case is exceptional: the relevant solution space is one-dimensional.

Apply the theorem with `f=g=Z_q`. If `Z_q` has the required finite-order continuation and obeys the same self-dual Riemann equation, then

`Z_q=c zeta`.

The coefficient of `1^(-s)` in every Euler product above is `1`, so comparison in the half-plane of absolute convergence gives `c=1`. Therefore `Z_q=zeta` identically.

The logic is important: the Grosswald–Schnitzer theorem by itself gives only continuation to `Re(s)>0`, so Hamburger cannot be applied to the deformation *as constructed*. The result here is a conditional incompatibility statement: **if** one tries to promote a nontrivial integer Grosswald–Schnitzer deformation to the global finite-order Riemann functional-equation class, converse theory forces that promotion to collapse back to ordinary zeta.

## Any nontrivial integer deformation is genuinely different from zeta

The coefficient distinction can be proved without analyzing complicated representation multiplicities. Let `j` be the first index at which `q_j != p_j`. Then

`q_i=p_i` for `i<j`

and, because `q_j` is an integer with `p_j <= q_j <= p_(j+1)`, nontriviality gives

`q_j > p_j`.

For every `i>j`,

`q_i >= p_i > p_j`.

Hence no generator `q_i` equals the prime `p_j`. A product of two or more generators is composite, so no such product can equal `p_j` either. Therefore

`a_q(p_j)=0`.

For ordinary zeta the Dirichlet coefficient at every positive integer, in particular at `p_j`, is `1`. Thus `Z_q != zeta` whenever the integer generator sequence is nontrivial.

Combining this elementary observation with Hamburger gives the exact no-go:

`nontrivial integer Grosswald–Schnitzer deformation`

`+ ordinary Dirichlet-series structure`

`+ Hamburger finite-order continuation`

`+ exact Riemann functional equation`

`=> contradiction`.

The zero-preserving deformation therefore cannot preserve all of these structures simultaneously.

## Why this is a genuine arithmetic-specificity discriminator

The prime-exponent lattice by itself is too flexible in several senses already recorded in this line: phase twists, generalized-prime systems, generic trace formulas, and even square-free-lattice scattering models can preserve large amounts of apparent zeta structure. `PL-125` sharpened this by exhibiting a deformation that preserves the actual zero divisor while destroying the rational-prime basis.

Hamburger rigidity shows that the **global self-dual completion plus the ordinary integer Dirichlet basis is different**. The functional equation is not merely an extra symmetry of the zero set. In the converse theorem it couples the right-half-plane coefficient expansion to its reflected analytic data so strongly that the whole function is unique.

This dovetails with `PL-014`. Tate explains *why* ordinary zeta has the completed functional equation: additive Fourier transform on the adeles, the archimedean gamma factor, and Poisson summation supply the continuation and the involution `s <-> 1-s`. Hamburger supplies the converse-side rigidity: among ordinary finite-order Dirichlet series, that same global boundary relation already singles out zeta.

The mathematically meaningful discriminator is therefore not

`same primes -> same zeros`,

nor

`same zeros -> same arithmetic`,

both of which `PL-125` warns against. It is closer to

`ordinary integer coefficient geometry + global Fourier/Poisson self-duality -> distinguished zeta function`.

That is classical prior art, but it is exactly the kind of rational-prime/global coupling required by the README's falsification controls.

## What this does not prove

The conclusion must not be over-read.

First, Hamburger uniqueness identifies the **function**, not the location of its zeros. Once `zeta` has been recovered, RH remains untouched. The functional equation explains the symmetric axis `Re(s)=1/2` but allows pairs of zeros off the axis.

Second, the finite-order/whole-plane analytic hypotheses matter. A nonvanishing factor `phi(s)` with a suitable reflection symmetry can formally preserve a functional equation outside the ordinary Hamburger class; symmetry alone does not force `phi` to be constant. The rigidity comes from the conjunction of the functional equation with ordinary Dirichlet-series and growth/continuation hypotheses.

Third, arbitrary real Grosswald–Schnitzer generators `q_n` lead naturally to generalized Dirichlet frequencies `log q_n`, and Hamburger's ordinary integer Dirichlet-series theorem does not directly apply. Those deformations are still valid controls against mechanisms that ignore the exact integer coefficient lattice. The present discriminator is strongest precisely for the integer deformations relevant to Sierra and for candidate mechanisms claiming to remain in the ordinary arithmetic Dirichlet category.

Fourth, functional equations are not universally characterizing for other `L`-functions. Kaczorowski–Molteni–Perelli emphasize that the one-dimensional Hamburger phenomenon is exceptional; for many Dirichlet `L` functional equations the solution space has dimension greater than one unless additional Euler-product/multiplicativity information is imposed. The conclusion here is specifically about the Riemann zeta functional equation and its Hamburger class.

## Prior-art and novelty audit

No novelty is claimed for Hamburger's theorem, converse theorems, Grosswald–Schnitzer deformations, or Tate's functional equation. Grosswald–Schnitzer already explicitly note the generic loss of functional equations in their same-zero class, and Kaczorowski–Molteni–Perelli present Hamburger's uniqueness theorem as classical.

The durable contribution for this research line is the **matched-control synthesis** after `PL-125`: the Grosswald–Schnitzer control is decisive against zero-set-only and transfer-only prime-lattice mechanisms, but it is not a control for a mechanism that genuinely derives the Riemann global functional equation inside the ordinary integer Dirichlet class. Classical converse theory proves that distinction exactly.

A literature search around Grosswald–Schnitzer, Hamburger uniqueness, converse theorems, and modified zeta functional equations found the two ingredients as established prior art but no separate claim of novelty is attached to their conjunction here.

## Falsification boundary and consequence for the line

A future `prime_lattice` mechanism should therefore be subjected to two different controls rather than one.

If it uses only the zero divisor, Euler-factor-shaped local data, transfer matrices, or self-adjoint realizations fed by inverse coefficients, it must survive Grosswald–Schnitzer and related generalized-prime deformations. `PL-125` shows that the canonical square-free lattice alone fails this test.

If instead it claims to use a **global completion mechanism**, the relevant test is whether it derives enough of the Riemann Fourier/Poisson functional equation and ordinary Dirichlet coefficient structure for Hamburger-type rigidity to apply. Passing that test can genuinely distinguish ordinary zeta from the integer same-zero deformations.

But even passing it does not solve RH. The surviving target is sharper:

`exact integer prime/exponent structure`

`+ canonical global self-dual continuation`

`+ an independent positivity/unitarity/Hodge mechanism`

`=> force the already-distinguished zeta divisor onto its self-dual axis`.

The first two ingredients have a classical rigidity theorem; the third remains the unresolved RH content.