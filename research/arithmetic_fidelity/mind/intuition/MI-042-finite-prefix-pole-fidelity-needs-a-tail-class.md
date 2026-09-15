# MI-042 — Finite-prefix fidelity needs a structural source class; class plus normalization or symmetry can restore rigidity

**Evidence level:** exact-derived boundary statement from [AF-366](../../findings/AF-366-finite-prefix-observations-need-tail-class-for-dirichlet-pole-fidelity.md), strengthened inside positive generalized-prime categories by [AF-367](../../findings/AF-367-finite-prime-prefix-plus-square-root-beurling-regularity-does-not-determine-zero-geometry.md), [AF-368](../../findings/AF-368-logarithmic-integer-counting-proximity-does-not-identify-rational-primes.md), and the positive category-specific recovery theorems [AF-369](../../findings/AF-369-integer-supported-delone-zero-divisors-universal-residue-restores-prime-identity.md) and [AF-370](../../findings/AF-370-hamburger-source-class-functional-equation-rigidity.md), complementary to the global Riesz principal-part theorem AF-365.

AF-366--AF-368 isolate completion freedom. Arbitrarily long exact finite observations, positivity and multiplicativity, near-square-root generalized-integer counting, and even arbitrarily small fixed `O(log x)` counting discrepancy can leave the source or zero geometry undetermined. The missing resource is not simply another digit of scalar accuracy: the admissible completion fibre remains too large.

AF-369 gives one positive boundary. Inside integer-supported Delone Beurling systems, Lagarias reduces the source to finite arithmetic modifications. The Riemann divisor in `Re s>0` is still universal across that class, but

`Res_(s=1) zeta_Q(s)=1  <=>  N_Q=N  <=>  Q=P`.

The pole residue becomes a complete binary discriminator only because the source category has already narrowed the fibre enough.

AF-370 gives a different positive boundary. Let `H` be Hamburger's class of ordinary Dirichlet series, absolutely convergent in `Re s>1`, with `(s-1)f(s)` entire of finite order. Within `H`, the exact completed Riemann functional equation forces

`f=c zeta`.

The ordinary-Dirichlet normalization `a(1)=1` then forces `c=1`. Thus the conjunction

`ordinary Dirichlet source + finite-order continuation + exact Riemann reflection + one scalar normalization`

recovers `zeta` exactly. The same reflection symmetry on a broader function class has a large fibre, so the symmetry is not intrinsically faithful; its power is **source-class-relative**.

The reusable audit is therefore two-dimensional. Before inferring a pole, zero or source discriminator, specify the admissible source category and the exact analytic/scalar relation retained by the destination, then prove that their joint fibre is target-pure. Narrowing the category can be as information-bearing as adding an observable, and the same observable can be useless on one category and complete on another.

This does not collapse source recovery into RH. AF-370 identifies the distinguished analytic function but does not select its nontrivial zeros; the functional equation supplies a reflection axis, not a zero-confinement theorem. A downstream RH route still needs an additional positivity, sign, unitarity, localization or equivalent mechanism.

**Boundary.** AF-369 is a binary recovery theorem inside the integer-supported Delone class. AF-370 is Hamburger rigidity inside an ordinary-Dirichlet finite-order class. Neither is a category-independent lower bound, neither reconstructs arbitrary Beurling sources, and neither by itself advances zero confinement. Their common lesson is the resource accounting: **source class and retained analytic structure must be priced jointly.**
