# PL-003 — Ambient prime torus does not rigidly determine a zero set

## Claim

The infinite prime torus and its log-prime frequency structure are **not by themselves sufficient to determine the Riemann zero set**.

Completely multiplicative unimodular functions `chi` are determined by independent choices `chi(p)` on the primes and therefore live on the same infinite character torus used in the Bohr correspondence. Their Helson zeta functions

```text
zeta_chi(s) = sum_{n>=1} chi(n) n^{-s}
```

share that ambient multiplicative/Bohr structure but can have radically different analytic zero and pole behavior.

**Evidence/status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE`.

The literature supplies the contrasting Helson-zeta behaviors; the Mathia-specific consequence is the obstruction to an undistinguished torus-only RH mechanism.

## Literature facts already used in the investigation

Hedenmalm–Lindqvist–Seip describe multiplicative characters as points of the infinite character space and the corresponding twisted Dirichlet series as vertical limit functions in the Bohr framework.

Helson's classical result gives the generic/random side: if the prime values `chi(p)` are chosen independently and uniformly on the unit circle, the associated Helson zeta function is almost surely analytic and zero-free for

```text
Re(s) > 1/2.
```

At the opposite extreme, Bochkov–Romanov construct Helson zeta functions whose analytic continuations have essentially arbitrary prescribed zeros and poles in

```text
21/40 < Re(s) < 1
```

unconditionally, and in the full strip

```text
1/2 < Re(s) < 1
```

under the Riemann hypothesis.

These functions all arise from completely multiplicative unimodular prime phases `chi(p)`.

## Derived obstruction

The ambient objects

```text
infinite prime character torus,
coordinate directions indexed by primes,
log-prime frequency list (log p)_p,
Kronecker-type phase evolution,
```

do not rigidly impose one zero set. The choice of character can change the analytic zero/pole structure drastically while retaining those ambient ingredients.

Therefore any candidate mechanism that depends **only** on the undistinguished topology/measure of the prime torus or on the bare frequency multiset `{log p}` cannot, by itself, explain why the Riemann zeta function has its particular zeros.

A successful mechanism must use structure that distinguishes the Riemann case `chi(p)=1` from generic and exceptional twists rather than treating all torus points equivalently.

## Relevance to the Mathia construction

The prime-exponent lattice makes the infinite torus look geometrically canonical, and the flow

```text
t -> (e^{-i t log p})_p
```

is a natural harmonic object. This finding prevents that ambient geometry from being mistaken for a complete RH mechanism.

It is an important negative result because it narrows the search from

```text
"find the zeros in the prime torus"
```

to the more constrained requirement

```text
"identify additional canonical structure that singles out the untwisted Riemann object and survives analytic continuation."
```

## Prior art and novelty assessment

The Helson-zeta facts are established literature, not Mathia discoveries. In particular, the flexibility of zeros/poles is a published phenomenon.

The stored contribution is the explicit obstruction for this research line: **ambient Bohr-torus geometry and log-prime frequencies cannot be sufficient invariants of the Riemann zero set**.

No claim is made that this logical consequence is a new theorem in analytic number theory.

## Boundary conditions and counterarguments

- The result does not say that the distinguished character `chi=1` is geometrically uninteresting.
- It does not rule out a mechanism that depends essentially on the distinguished untwisted point, the completed zeta functional equation, the archimedean factor, self-duality, or another structure that changes under twisting.
- Bochkov–Romanov's extension to the whole strip `1/2<Re(s)<1` is conditional on RH; the unconditional arbitrary prescription quoted here is only in `21/40<Re(s)<1`.
- The obstruction is against **torus-only** or **frequency-only** explanations, not against every construction formulated using torus coordinates.

## Audit criterion

A proposed prime-torus mechanism escapes this obstruction only if it identifies a mathematically canonical datum that is absent or different for the flexible Helson twists and demonstrates that the zero prediction depends essentially on that datum.

If the candidate is invariant under arbitrary changes of the prime phases `chi(p)`, then the Helson-zeta examples falsify its ability to determine the Riemann zero set.

## Consequence for the research line

The prime torus is a useful representation space, but it is **not a rigid spectral object for RH by itself**. Any credible mechanism must explain the exceptional status of the untwisted Riemann zeta function instead of attributing the zeros to the ambient torus alone.
