# MI-042 — Finite-prefix and scalar-counting fidelity need a structural source class; class plus normalization can restore rigidity

**Evidence level:** exact-derived boundary statement from [AF-366](../../findings/AF-366-finite-prefix-observations-need-tail-class-for-dirichlet-pole-fidelity.md), strengthened inside positive generalized-prime categories by [AF-367](../../findings/AF-367-finite-prime-prefix-plus-square-root-beurling-regularity-does-not-determine-zero-geometry.md), [AF-368](../../findings/AF-368-logarithmic-integer-counting-proximity-does-not-identify-rational-primes.md), and the category-specific recovery theorem [AF-369](../../findings/AF-369-integer-supported-delone-zero-divisors-universal-residue-restores-prime-identity.md), complementary to the global Riesz principal-part theorem AF-365.

AF-366 isolates unrestricted completion freedom. A finite observation depending on the first `N` Dirichlet coefficients is blind to tails that vanish on that prefix yet insert prescribed poles in the critical strip. Arbitrarily long exact finite observations therefore do not determine meromorphic principal parts without an admissible tail class.

AF-367 shows that this is not merely an artifact of arbitrary signed coefficients. For every finite cutoff, positive Beurling generalized-prime systems can agree exactly with the ordinary rational primes and induced integers below that cutoff, satisfy near-square-root generalized-integer counting, and nevertheless have different Beurling-RH zero geometry. Finite exact arithmetic data plus positivity, multiplicativity and that global counting class remain target-mixed.

AF-368 moves the source-side obstruction much closer to the ordinary integers. For every `c>0`, there is a nonordinary Beurling prime system `Q` with

`|N_Q(x)-floor(x)| < c log x`.

Thus **no fixed positive logarithmic scalar counting envelope identifies the rational-prime source** inside the unrestricted Beurling category, even when its constant is arbitrarily small. This is a source-identity obstruction, not a claim of different RH status for the matched system.

AF-369 gives the complementary positive boundary. If the generalized integers are Delone and satisfy `N_Q subset N`, Lagarias' classification forces only finitely many ordinary-prime deletions/composite replacements. Every such source still has exactly the Riemann zero/pole divisor in `Re s>0`, so exact integer support plus Delone structure does not make the divisor faithful. But now

`Res_(s=1) zeta_Q(s) = dens(N_Q)`

and, **inside this declared source class only**,

`Res_(s=1) zeta_Q(s)=1  <=>  N_Q=N  <=>  Q=P`.

So the missing resource is not “more scalar accuracy” in isolation. A scalar becomes discriminating only after the admissible completion fibre has been narrowed enough that the scalar is rigid on that fibre. AF-368 and AF-369 together force the audit to be two-dimensional: **source category + retained normalization**. The same numerical datum can be insufficient in a broad category and complete for a binary discriminator in a narrow one.

The complementary transform currency remains structural as well. A coefficient-tail bound `|a_n-b_n| <= M n^(theta-1)` makes the Dirichlet-transform difference holomorphic on `Re s>theta`, so principal parts there agree. On the arithmetic side, exact support, factorization structure, cancellation laws, functional-equation coupling or another rigidity theorem can shrink completion fibres before a retained scalar or analytic layer is asked to distinguish them.

The reusable rule is therefore stricter than “preserve many primes and tighten the counting error.” Before inferring a pole, zero or source discriminator, specify the admissible source category, identify the exact analytic/scalar datum retained by the destination, and prove that their joint fibre is target-pure. Progressively smaller fixed multiples of `log x` are still on the wrong side of that gate; conversely, AF-369 shows that a category-specific pole-residue theorem can cross it without reconstructing the whole source.

**Boundary.** AF-369 recovers only the binary statement `Q=P` inside the integer-supported Delone class; it does not reconstruct a nonordinary source and does not generalize density-one rigidity to arbitrary Beurling systems. The common-divisor statement is for `Re s>0`, and the finite Euler factors can change boundary-line behavior and the functional equation.