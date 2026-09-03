# PL-127 — Critical-line phase slope quantitatively detects integer Grosswald–Schnitzer prime deformations

## Claim

`PL-125` uses Grosswald–Schnitzer deformations as a matched control: replacing each rational prime `p_n` by `q_n` with `p_n <= q_n <= p_(n+1)` preserves the complete zeta zero divisor in `Re(s)>0`, even though the exact prime lattice can be destroyed. `PL-126` then shows that an **exact** Riemann functional equation restores rigidity in Hamburger's ordinary-Dirichlet-series class. The remaining question was whether the functional-equation defect has a quantitative, phase-sensitive observable that sees how early the prime data were altered.

For the Grosswald–Schnitzer class there is such an observable, and it is simpler than a general quantitative Hamburger theorem. Write

`Z_q(s)=phi_q(s) zeta(s)`,

where Grosswald and Schnitzer prove that

`phi_q(s)=prod_n (1-p_n^(-s))/(1-q_n^(-s))`

is analytic and nonzero for `Re(s)>0`, with locally uniform convergence. In the critical strip define the reflection cocycle

`R_q(s)=phi_q(s)/phi_q(1-s)`.

On the critical line `s=1/2+it`, real `p_n,q_n` give `phi_q(1-s)=conj(phi_q(s))`, hence `|R_q|=1`. Thus modulus sees **no** functional-equation defect there; the information is entirely in phase, agreeing with the control in `VIS-006`.

Let

`g(x)=log(x)/(sqrt(x)-1)`,  for `x>1`,

and define the central reflection slope

`D(q) = (1/2) (d/ds log R_q(s))|_(s=1/2)`.

Then

`D(q) = phi_q'(1/2)/phi_q(1/2)
      = sum_n [g(p_n)-g(q_n)].`

The function `g` is strictly decreasing on `(1,infinity)`. Since every Grosswald–Schnitzer deformation is one-sided, `p_n <= q_n`, every summand is nonnegative. Therefore

`D(q) >= 0`,

with equality **if and only if** `q_n=p_n` for every `n`.

For integer deformations there is a genuine scale-aware stability statement. If `P=p_J` is the first altered prime, then `q_J>=P+1`, so

`g(P)-g(P+1) <= D(q) <= g(P)`.

More generally, for any cutoff `X`, put

`delta(X)=min_{p prime, p<=X} [g(p)-g(p+1)] > 0`.

If

`D(q) < delta(X)`,

then **all generators up to `X` are forced to be the actual rational primes**. Thus a sufficiently small phase-slope defect certifies agreement of the low prime/exponent directions. The scale deteriorates as expected:

`g(P)-g(P+1) = ((1/2)log P - 1) P^(-3/2) + O(log P / P^2)`.

For unrestricted real `q_n`, no analogous positive lower bound exists at fixed `P`, because one may choose `q_J=P+epsilon` with arbitrarily small `epsilon`. The quantitative rigidity is therefore supplied by the **discreteness of the integer lattice**, not merely by the Grosswald–Schnitzer interval condition.

**Evidence/status:** `LITERATURE+DERIVED + POSITIVE-DISCRIMINATOR + CLUE-RESOLUTION`.

This does not prove RH and does not provide a general stability theorem for Hamburger's converse theorem. It resolves the concrete Grosswald–Schnitzer test behind `CLUE-quantitative-hamburger-phase-rigidity`: within the zero-preserving deformation class, a first-order phase observable at the self-dual point already distinguishes the exact rational-prime system, and for integer deformations it does so quantitatively by scale.

## Derivation of the phase-slope identity

Grosswald and Schnitzer prove more than zero preservation. Their Lemma 1 shows that the product defining `phi_q` converges absolutely and uniformly on compact subsets of `Re(s)>0`, and that `phi_q` never vanishes there. Their proof works with the canonical analytic logarithm

`log phi_q(s)=sum_n [log(1-p_n^(-s))-log(1-q_n^(-s))]`

and proves locally uniform absolute convergence in the whole half-plane. Hence differentiation is legitimate on compact subsets of `Re(s)>0`.

For a single real `a>1`,

`d/ds log(1-a^(-s)) = log(a)/(a^s-1)`.

Therefore

`phi_q'(s)/phi_q(s)
 = sum_n [log(p_n)/(p_n^s-1) - log(q_n)/(q_n^s-1)].`

At `s=1/2` this is exactly `sum_n[g(p_n)-g(q_n)]`. Since

`log R_q(s)=log phi_q(s)-log phi_q(1-s)`,

we have

`(d/ds) log R_q(s)
 = phi_q'(s)/phi_q(s) + phi_q'(1-s)/phi_q(1-s)`,

so the value at the fixed point is twice `phi_q'(1/2)/phi_q(1/2)`.

If `R_q(1/2+it)=exp(i theta_q(t))` with the continuous branch normalized by `theta_q(0)=0`, then

`theta_q'(0)=2D(q)`.

Thus `D(q)` is literally half of the critical-line phase velocity of the functional-equation defect. No modulus-only observable on that line can recover it, because `|R_q(1/2+it)|=1` identically.

## Positivity comes from one-sided prime deformation

Differentiate `g`. Writing `y=sqrt(x)>1`, the sign of `g'(x)` is the sign of

`y-1-y log y`.

This expression vanishes at `y=1` and has derivative `-log y<0` for `y>1`; hence

`g'(x)<0` for every `x>1`.

The Grosswald–Schnitzer ordering `p_n<=q_n` therefore gives

`g(p_n)-g(q_n) >= 0`

term by term. There is no cancellation between prime directions. If any `q_n>p_n`, that term is strictly positive, so `D(q)>0`. Conversely `D(q)=0` forces every term to vanish and hence every `q_n=p_n`.

This is stronger than the exact Hamburger statement in one narrow sense and weaker in another. It is stronger as a diagnostic **inside this deformation family** because it needs only the nonvanishing Grosswald–Schnitzer factor in `Re(s)>0`, not whole-plane finite-order continuation. It is weaker as a converse theorem because it says nothing about arbitrary Dirichlet series near the zeta functional equation.

## Integer discreteness gives the quantitative scale certificate

Suppose now that every `q_n` is an integer, as in the Sierra control of `PL-125`, and let `J` be the first changed index. Put `P=p_J`. Then `q_J>P`, so integrality implies `q_J>=P+1`. Monotonicity of `g` yields

`g(P)-g(q_J) >= g(P)-g(P+1)`.

All later terms are nonnegative, proving the lower bound

`D(q) >= g(P)-g(P+1)`.

For the upper bound use the other half of the Grosswald–Schnitzer interval condition, `q_n<=p_(n+1)`. Again by monotonicity,

`g(p_n)-g(q_n) <= g(p_n)-g(p_(n+1))`.

Because there are no changes before `J`, summing from `J` telescopes:

`D(q) <= sum_(n>=J) [g(p_n)-g(p_(n+1))] = g(P)`.

The same lower-bound argument gives the cutoff certificate. If some generator with prime `p<=X` were altered, its contribution alone would be at least `g(p)-g(p+1)`, hence at least `delta(X)`. Therefore `D(q)<delta(X)` excludes every alteration below the cutoff.

The asymptotic follows from

`g(x)=log(x) x^(-1/2) + log(x) x^(-1) + O(log(x)x^(-3/2))`

and a one-step Taylor expansion. It confirms the scale warning in the clue: a defect moved to a very large prime produces a very small central phase slope. There is no scale-free local stability theorem.

## Adversarial controls

Several apparent strengthenings do **not** follow.

First, `D(q)>0` is not an RH-sensitive positivity theorem. It concerns the nonvanishing quotient `phi_q=Z_q/zeta`, whose purpose is precisely to compare functions with the **same** zero divisor. The observable detects arithmetic deformation that the divisor cannot detect; it does not localize that divisor on `Re(s)=1/2`.

Second, the critical line is special here only because it is the fixed set of the Riemann reflection `s -> 1-s` combined with complex conjugation. The unit-modulus identity for `R_q` is a self-duality statement, not an independent explanation of RH.

Third, the positive decomposition depends crucially on the one-sided ordering `p_n<=q_n`. For a more general perturbation allowing generators on both sides of `p_n`, the summands can have opposite signs and the central slope may cancel. This is a discriminator for the Grosswald–Schnitzer matched-control class, not a universal metric on generalized primes.

Fourth, integer discreteness is essential for the low-scale lower bound. If real `q_n` are allowed, a fixed low prime can be displaced by an arbitrarily small amount and make `D(q)` arbitrarily small. Exact positivity survives, quantitative coefficient recovery does not.

## Prior-art and novelty audit

Primary source:

- **Emil Grosswald, F. J. Schnitzer**, “A class of modified zeta and L-functions,” *Pacific Journal of Mathematics* **74**(2) (1978), 357–364. DOI: https://doi.org/10.2140/pjm.1978.74.357. Their Theorem 1 establishes the zero-preserving deformation; Lemma 1 proves the locally uniform nonvanishing product `phi_q` on `Re(s)>0` that makes the present differentiation rigorous. Their introduction explicitly notes that the modified functions generally lose functional equations.

For exact converse rigidity, `PL-126` uses:

- **Jerzy Kaczorowski, Giuseppe Molteni, Alberto Perelli**, “A converse theorem for Dirichlet L-functions,” *Commentarii Mathematici Helvetici* **85**(2) (2010), 463–483. DOI: https://doi.org/10.4171/CMH/202. Its introduction recalls Hamburger's characterization of zeta by the Riemann functional equation in the finite-order ordinary-Dirichlet-series class.

A targeted literature search for quantitative/stability versions of Hamburger's theorem, Grosswald–Schnitzer functional-equation defects, and phase/reflection-cocycle formulations found the classical exact converse theory and the original deformation theorem, but no source matching the specific positive central-slope identity and integer cutoff certificate above. **No broad novelty claim is made**: the identity is an elementary derived consequence of Grosswald–Schnitzer's convergent quotient once the correct phase-sensitive observable is chosen. Its durable value for this repository is that it settles the proposed clue's decisive Grosswald–Schnitzer test and identifies precisely where integer lattice discreteness enters quantitative rigidity.

## Consequence for the prime-lattice line

`PL-125` showed that the zero divisor does not identify the rational-prime lattice. `PL-126` showed that exact global self-duality plus ordinary Dirichlet structure does identify zeta. `PL-127` adds an intermediate, quantitative statement inside the matched deformation family:

`zero-preserving arithmetic deformation`

`+ functional-equation reflection phase`

`+ one-sided prime ordering`

`=> positive additive defect`,

and with integer generators,

`small defect => exact agreement of the prime lattice up to a controlled finite scale`.

This is a useful discriminator for future approximate spectral/geometric constructions. If a proposed mechanism claims to approximately recover the Riemann functional equation but its complex reflection phase does not control this positive Grosswald–Schnitzer defect, then it has not quantitatively recovered the rational-prime arithmetic even if it reproduces the correct zero divisor or critical-line magnitudes.

The remaining RH problem is unchanged and sharply separated: after the exact arithmetic function has been identified, one still needs an independent positivity/unitarity/Hodge mechanism that forces its already-distinguished zero divisor onto the self-dual axis.