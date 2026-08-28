# PL-003 — Ambient prime torus does not rigidly determine a zero set

## Claim

The infinite prime torus and its log-prime frequency structure are **not by themselves sufficient to determine the Riemann zero set or even a rigid continuation domain**.

Completely multiplicative unimodular functions `chi` are determined by independent choices `chi(p)` on the primes and therefore live on the same infinite character torus used in the Bohr correspondence. Their Helson zeta functions

```text
zeta_chi(s) = sum_{n>=1} chi(n) n^{-s}
```

share that ambient multiplicative/Bohr structure but can have radically different analytic zero, pole, and continuation behavior.

**Evidence/status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE`.

The literature supplies the contrasting Helson-zeta behaviors; the Mathia-specific consequence is the obstruction to an undistinguished torus-only RH mechanism.

## Literature facts

Hedenmalm–Lindqvist–Seip describe multiplicative characters as points of the infinite character space and the corresponding twisted Dirichlet series as vertical limit functions in the Bohr framework.

Helson's classical result gives the generic/random side: if the prime values `chi(p)` are chosen independently and uniformly on the unit circle, the associated Helson zeta function is almost surely analytic and zero-free for

```text
Re(s) > 1/2.
```

Bochkov–Romanov established the opposite extreme: Helson zeta functions can have essentially arbitrary prescribed zeros and poles in

```text
21/40 < Re(s) < 1
```

unconditionally, and in the full strip

```text
1/2 < Re(s) < 1
```

under RH.

Johan Andersson's 2024 Mittag-Leffler theorem strengthens this substantially and removes that RH-dependent strip limitation. Subject to the ordinary discreteness requirements for a meromorphic divisor, a Helson zeta function can be chosen with prescribed zeros and poles throughout

```text
Re(s) < 1.
```

The same work also shows that an arbitrary open connected set `U` containing `Re(s)>1` can occur as the maximal domain of holomorphy/meromorphy of a suitable zero-free Helson zeta function.

Thus the flexibility is not confined to a substrip near `Re(s)=1`: it extends across the whole half-plane to the left of the Euler-product region and even to the topology of the continuation domain.

## Derived obstruction

The ambient objects

```text
infinite prime character torus,
coordinate directions indexed by primes,
log-prime frequency list (log p)_p,
Kronecker-type phase evolution,
```

do not rigidly impose either a zero set or a continuation geometry. The choice of character can change the meromorphic divisor and maximal continuation domain drastically while retaining those ambient ingredients.

Therefore any candidate mechanism that depends **only** on the undistinguished topology/measure of the prime torus, on the bare frequency multiset `{log p}`, or on generic Euler-product form cannot by itself explain why the Riemann zeta function has its particular analytic continuation and zero set.

A successful mechanism must use structure that distinguishes the Riemann case `chi(p)=1` from generic and exceptional twists rather than treating all torus points equivalently.

## Relevance to the Mathia construction

The prime-exponent lattice makes the infinite torus look geometrically canonical, and the flow

```text
t -> (e^{-i t log p})_p
```

is a natural harmonic object. This finding prevents that ambient geometry from being mistaken for a complete RH mechanism.

The strengthened Andersson result makes the negative conclusion sharper: the same prime-phase framework supports essentially arbitrary meromorphic divisors throughout `Re(s)<1` and even arbitrary maximal continuation domains compatible with containing `Re(s)>1`.

It narrows the search from

```text
"find the zeros in the prime torus"
```

to the stricter requirement

```text
"identify canonical extra structure that singles out the untwisted Riemann object,
forces its continuation, and survives into the critical strip."
```

## Prior art and novelty assessment

The Helson-zeta flexibility results are established literature, not Mathia discoveries. Andersson's strengthening is also prior art and is retained because it materially tightens an existing obstruction.

The stored contribution is the explicit consequence for this research line: **ambient Bohr-torus geometry, log-prime frequencies, and bare Euler-product form are insufficient invariants not only for the Riemann zero set but even for the analytic continuation domain**.

No claim is made that this logical consequence is a new theorem in analytic number theory.

## Boundary conditions and counterarguments

- The result does not say that the distinguished character `chi=1` is geometrically uninteresting.
- It does not rule out a mechanism that depends essentially on the distinguished untwisted point, the completed zeta functional equation, the archimedean factor, self-duality, positivity, or another structure that changes under twisting.
- Andersson's theorem is an existence result for specially chosen completely multiplicative unimodular characters; it does not say that a typical character has arbitrary behavior.
- Prescribed zero/pole sets must satisfy the ordinary discreteness conditions required of zeros and poles of meromorphic functions.
- The obstruction is against **torus-only**, **frequency-only**, or generic-Euler-product explanations, not against every construction formulated using torus coordinates.

## Audit criterion

A proposed prime-torus mechanism escapes this obstruction only if it identifies a mathematically canonical datum that is absent or different for the flexible Helson twists and demonstrates that the predicted continuation/zero structure depends essentially on that datum.

If the candidate is invariant under arbitrary changes of the prime phases `chi(p)` while retaining only the same torus, `log p` frequencies, and generic Euler-product form, then the Helson-zeta constructions falsify its ability to determine the Riemann continuation or zero set.

## Consequence for the research line

The prime torus is a useful representation space, but it is **not a rigid spectral or analytic object for RH by itself**. Any credible mechanism must explain the exceptional status of the untwisted Riemann zeta function and identify extra structure strong enough to constrain both analytic continuation and zeros.