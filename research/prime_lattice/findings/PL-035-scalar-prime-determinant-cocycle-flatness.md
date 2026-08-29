# PL-035 — Scalar prime determinant cocycle compatibility is flat and freely forgeable

## Claim

The simplest joint compatibility law left open by `PL-034` does **not** provide arithmetic rigidity. Suppose a scalar relative invariant is indexed by positive integers and the prime action shifts a spectral parameter by the exponent-lattice energy

```text
E(n) = log n = <v(n),(log p)_p>.
```

For every nonzero meromorphic function `F` on a shift-stable domain, define

```text
Delta_n^F(z) = F(z + log n) / F(z).
```

Then, identically wherever the ratios are defined,

```text
Delta_(mn)^F(z)
  = Delta_m^F(z) Delta_n^F(z + log m)
  = Delta_n^F(z) Delta_m^F(z + log n).
```

Thus the exact `p`, `q`, `pq` compatibility suggested by the surviving trace-class clue is satisfied by a completely arbitrary scalar transfer function `F`. The law is a translation **1-coboundary**, hence its elementary prime-square consistency is flat rather than an arithmetic interaction.

The same construction works after replacing the rational-prime weights `log p` by arbitrary Beurling weights `lambda_j=log q_j`:

```text
Delta_alpha^F(z)
  = F(z + <alpha,lambda>) / F(z),
alpha in N_0^(N) with finite support.
```

Consequently, ordinary scalar multiplicativity or translated determinant/ spectral-shift chain-rule compatibility across `p`, `q`, and `pq` cannot by itself distinguish the rational-prime exponent lattice from the Beurling controls of `PL-015`, and cannot select the Riemann zero divisor. One may choose `F` first — including a function carrying any prescribed finite divisor, or `F=xi` if one wants to insert the Riemann divisor — and the compatibility follows automatically.

**Evidence/status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the route

```text
scalar prime-indexed relative determinant
+ ordinary multiplicative / translation 1-cocycle law
    -> arithmetic rigidity or RH zero localization.
```

The decisive negative is the explicit arbitrary-`F` family above. Classical spectral-shift theory supplies a close prior-art control: Krein spectral-shift functions obey an additive chain rule for trace-class perturbation triples, and standard perturbation determinants obey the corresponding product functoriality. No novelty is claimed for cocycles, coboundaries, determinant chain rules, or spectral-shift additivity.

This result does **not** rule out a canonically forced invariant with genuinely additional joint structure: a nontrivial projective/higher cocycle, operator-valued relation, global adelic/product-formula normalization, or another constraint proved not to reduce to a freely chosen scalar transfer function and proved to distinguish rational primes from matched Beurling systems.

## Exact coboundary calculation

Let the positive integer semigroup act on meromorphic functions by translation,

```text
(tau_n F)(z) = F(z + log n).
```

Since `log(mn)=log m+log n`, one has

```text
Delta_n^F = (tau_n F)/F.
```

Therefore

```text
Delta_(mn)^F(z)
 = F(z+log m+log n)/F(z)

 = [F(z+log m)/F(z)]
   [F(z+log m+log n)/F(z+log m)]

 = Delta_m^F(z) (tau_m Delta_n^F)(z).
```

Interchanging `m` and `n` gives the same endpoint and hence

```text
Delta_m^F(z) Delta_n^F(z+log m)
 = Delta_n^F(z) Delta_m^F(z+log n).
```

For primes `p,q`, define the elementary prime-square defect

```text
K_(p,q)(z)
 := [Delta_p(z) Delta_q(z+log p)]
    /[Delta_q(z) Delta_p(z+log q)].
```

Every scalar coboundary of the displayed form has

```text
boxed: K_(p,q)(z) = 1.
```

This equality is not hidden arithmetic content. It says that both paths around the commuting prime square terminate at the same translated value `F(z+log p+log q)`.

The exponent-vector formulation makes the same point globally. For

```text
alpha = v(n),
E(alpha)=<alpha,(log p)_p>,
```

set

```text
Delta_alpha^F(z)=F(z+E(alpha))/F(z).
```

Then for all finite-support `alpha,beta`,

```text
Delta_(alpha+beta)^F(z)
 = Delta_alpha^F(z)
   Delta_beta^F(z+E(alpha)).
```

Unique factorization supplies the semigroup coordinates, but places no restriction on `F`.

## Why arbitrary divisors survive the compatibility law

The compatibility equation constrains how a chosen scalar datum propagates under translations; it does not constrain the datum from which it starts.

For any finite multiset `{rho_1,...,rho_r}`, take for example

```text
F(z)=product_j (z-rho_j).
```

Then `Delta_n^F` satisfies every displayed prime compatibility exactly, while its zeros and poles are inherited from the arbitrarily chosen divisor of `F` and its translates. More elaborate meromorphic `F` allow correspondingly richer divisors.

In particular, choosing a completed zeta function as `F` would make the family sensitive to Riemann zeros, but only because those zeros were inserted into `F` before the cocycle law was applied. The law would be equally valid for a function carrying a completely different divisor.

This supplies a direct falsification control for any proposed scalar determinant mechanism:

```text
if the only cross-prime theorem is the 1-cocycle / chain rule,
replace its transfer function by an unrelated F.
```

If the theorem survives unchanged, it cannot be the structure that localizes the Riemann divisor.

## Beurling matched control

The obstruction is not special to the weights `log p`. Let `{lambda_j}` be any positive frequency list and let

```text
E_lambda(alpha)=sum_j alpha_j lambda_j.
```

Then

```text
Delta_alpha^F(z)
 = F(z+E_lambda(alpha))/F(z)
```

obeys the identical semigroup cocycle law because

```text
E_lambda(alpha+beta)
 = E_lambda(alpha)+E_lambda(beta).
```

Taking `lambda_j=log q_j` for a Beurling prime system therefore reproduces the entire scalar compatibility pattern. Rational independence of the weights, when imposed to recover unique generalized factorization, does not change the calculation.

This strengthens the `PL-015` control in a very specific way. A proposed prime-family determinant does not become arithmetic merely because its local pieces compose correctly according to exponent addition. That composition is shared by every additive energy assignment.

A surviving construction must exhibit an extra invariant that Zhang-type controls do not preserve — for example a completed global Fourier/product-formula constraint — rather than only the semigroup law itself.

## The untwisted multiplicative law is even weaker

If the proposed scalar invariant has no translated spectral parameter and merely satisfies

```text
c(mn)=c(m)c(n),
```

then the freedom is more obvious. Since the positive integers form the free commutative monoid on the primes,

```text
c(n)=product_p c(p)^(v_p(n))
```

for arbitrary generator values `c(p)` in the target multiplicative group.

Thus neither of the two elementary notions of prime compatibility supplies the missing rigidity:

```text
untwisted multiplicativity
    -> arbitrary data on prime generators;

translated scalar 1-cocycle
    -> arbitrary transfer function F via a coboundary.
```

## Classical spectral-shift chain rule as prior-art control

The same type of compatibility is standard in relative spectral theory rather than special to arithmetic.

Gesztesy, Makarov and Naboko, in *The Spectral Shift Operator*, state for self-adjoint `H_0,H_1,H_2` with pairwise trace-class differences the Krein spectral-shift chain rule

```text
xi(lambda,H_0,H_2)
 = xi(lambda,H_0,H_1)
 + xi(lambda,H_1,H_2)
```

for almost every `lambda`. Their Remark 3.9 treats this as the ordinary chain rule for the scalar spectral-shift function; the surrounding determinant formalism is the standard relative-operator setting in which additive spectral shifts correspond to multiplicative perturbation data.

Primary source:

- Fritz Gesztesy, Konstantin A. Makarov, Serguei N. Naboko, “The Spectral Shift Operator,” in *Mathematical Results in Quantum Mechanics* (Prague, 1998), *Operator Theory: Advances and Applications* **108**, Birkhäuser, Basel, 1999, pp. 59–90; arXiv:`math/9901112`.

This literature is not needed to prove the arbitrary-`F` counterexample. Its role is novelty control: chain-rule compatibility is generic relative spectral machinery, so observing it in a prime-indexed family is not evidence that arithmetic has forced the scalar data.

## Relation to PL-034 and the accepted local clue

`PL-034` narrowed `CLUE-trace-class-prime-resolvent-cocycle` from ideal membership to joint arithmetic compatibility. This finding kills the **first** and most obvious version of that residual target:

```text
Delta_(pq)
 determined consistently by Delta_p and Delta_q
through the ordinary scalar translation cocycle law.
```

That property is automatic for every scalar coboundary and survives arbitrary Beurling frequency replacement.

The clue therefore remains open only at a stronger level. A candidate must show why its joint prime data are **not** freely reducible to

```text
Delta_n(z)=F(z+log n)/F(z)
```

or to arbitrary values on prime generators. Merely obtaining a Fredholm determinant, spectral-shift function, or exact `p,q,pq` chain rule does not pass this test.

## Boundary conditions and adversarial checks

### Not every scalar cocycle is claimed to be a coboundary

The negative needs no such classification theorem. It is enough that the displayed compatibility law admits an arbitrarily large family of coboundaries parameterized by unrestricted meromorphic `F`. Therefore the law **alone** cannot select a particular arithmetic divisor.

A construction with a separately proved canonicality condition that uniquely fixes its cohomology class could lie outside the negative.

### The result does not identify a useful non-flat invariant

`K_(p,q)=1` is a diagnostic for the elementary scalar-coboundary route, not a claim that nontrivial curvature would imply RH. A projective or operator-valued prime action would require its own existence theorem, domain analysis, determinant theory, and novelty audit.

### A global functional equation can add information absent here

If a determinant family is tied to the archimedean place, additive Fourier duality, the adelic product formula, Weil positivity, or an equivalent completed constraint, then its compatibility may be much more restrictive than the free translation law. Those mechanisms remain outside this finding and are consistent with the surviving routes in `PL-013` and `PL-014`.

### Exact analytic domains still matter

The calculation is meromorphic and local to any common shift-stable domain. It does not create analytic continuation. Choosing `F=xi` uses an already completed entire function; choosing an Euler product valid only in `Re(s)>1` does not license the same expression in the critical strip without an independent continuation theorem.

## Falsification / escape tests

A future prime-family invariant escapes this negative only if at least one of the following is proved rather than assumed:

1. its joint `p,q,pq` law contains information not implied by semigroup addition and cannot be represented by an arbitrary scalar transfer function;
2. its cohomology/normalization is canonically fixed by arithmetic data that fail for matched Beurling systems;
3. it is operator-valued/projective in a way that produces a nontrivial, well-defined higher obstruction not removable by gauge/coboundary change;
4. a global completion couples the finite prime directions to an archimedean/Fourier constraint and this coupling is what restricts the divisor.

Conversely, if replacing the candidate transfer function by arbitrary meromorphic `F`, or replacing `log p` by arbitrary Beurling weights, preserves every theorem used to claim zero localization, then the proposed rigidity is falsified by this finding.

## Consequence for the research line

The accepted trace-class clue should no longer treat **multiplicative/cocycle compatibility itself** as the missing arithmetic ingredient. That compatibility is one level too low: it is the natural bookkeeping of an additive semigroup and relative determinants.

The surviving question is sharper:

```text
can the rational-prime family force a canonical joint invariant
that is not a freely chosen scalar 1-coboundary,
and whose nontrivial global constraint fails for Beurling controls?
```

This shifts attention from ordinary determinant functoriality to genuinely global or higher structure. Until such a constraint is exhibited, a prime-indexed determinant family can realize spectral data without explaining why those data are the Riemann zeros.