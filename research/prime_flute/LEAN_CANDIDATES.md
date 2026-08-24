# Lean candidates for the prime-flute line

This is not a commitment to formalize the full infinite-surface construction. The first goal is to turn the **finite exact core** of the exploration into machine-checkable lemmas and use external analytic theorems only through explicit assumptions/interfaces.

## Priority 1 — matrix/cross-ratio identity

Target PF-004 first.

For real numbers `a < b < c < d`, define

```text
G(a,b) = 1/(b-a) * [[a+b, -2*a*b], [-2, a+b]]
chi(a,b,c,d) = ((c-b)*(d-a))/((b-a)*(d-c)).
```

Desired finite lemmas:

```text
det G(a,b) = 1
chi(a,b,c,d) > 0
tr (G(a,b) * (G(c,d))⁻¹) = -2 - 4*chi
```

Then isolate the elementary hyperbolic-function statement

```text
cosh(L/2) = 1 + 2*chi
  -> sinh(L/4)^2 = chi.
```

Do not make the first Lean milestone depend on a full formal definition of hyperbolic translation length. The matrix identity is already a reusable exact theorem.

### Why first

- finite algebra only;
- central custom identity behind several later observations;
- no prime-number theorem, topology of infinite surfaces, or spectral theory required;
- gives a clean falsification target for any sign/indexing error in the informal derivation.

## Priority 2 — cuff/logarithmic coordinate

Target PF-001.

For `0 < a < b`, put `h = log(b/a)` and

```text
ell = 2 * log((sqrt(b)+sqrt(a))/(sqrt(b)-sqrt(a))).
```

Desired lemma:

```text
exp(-ell/2) = tanh(h/4).
```

Then prove the finite telescope independently:

```text
h_n = log(u_n/u_{n-1})
-> sum_{n=m}^N h_n = log(u_N/u_{m-1}).
```

Possible follow-up:

```text
prod_{n=m}^N coth(ell_n/4) = sqrt(u_N/u_{m-1}).
```

This creates a formally verified negative example: a seemingly rich multiplicative geometric observable collapses to endpoint data.

## Priority 3 — shear coboundary

Target the exact half of PF-003.

For a positive sequence `Delta_n`, define

```text
phi_n   = log Delta_n
sigma_n = log(Delta_{n+1}/Delta_n).
```

Desired lemmas:

```text
sigma_n = phi_{n+1} - phi_n
sum_{n=m}^N sigma_n = phi_{N+1} - phi_m
prod_{n=m}^N exp(-s*sigma_n)
  = (Delta_m/Delta_{N+1})^s
```

The final identity may be easier to state initially over real `s`; complex powers introduce branch conventions that are irrelevant to the conceptual obstruction.

### Mathia value

This is a compact example of recognizing a **coboundary** and rejecting an apparently sophisticated transfer weight because it contains only boundary information.

## Priority 4 — short-neck limit from a three-scale cross-ratio

Still finite/elementary once the scale assumptions are abstracted.

Let positive `X_n,Y_n,Z_n` satisfy

```text
Y_n/X_n -> 0
Y_n/Z_n -> 0.
```

Define

```text
chi_n = Y_n*(X_n+Y_n+Z_n)/(X_n*Z_n)
L_n   = 4*asinh(sqrt(chi_n)).
```

Desired theorem:

```text
chi_n -> 0
L_n -> 0.
```

This should be formalized **without mentioning primes**. A later theorem can instantiate `X,Y,Z` with geometric prime gaps after importing the analytic number-theory ratio result.

## Priority 5 — finite-generated-field obstruction

Target the algebraic skeleton of PF-010 before any Fuchsian-group packaging.

Useful abstract lemma:

```text
If F/Q is a finitely generated field extension,
then the relative algebraic closure of Q in F is finite over Q.
```

Hence a family of elements of `F` that are algebraic over `Q` cannot have unbounded algebraic degree.

Combine later with:

```text
[Q(tan(pi/p)) : Q] = p-1
```

for odd primes `p`, plus the trace-ratio identity.

### Risk

Mathlib support for finitely generated fields and cyclotomic/trigonometric degree statements may make this much more expensive than Priorities 1–4. Do not let it block the elementary geometry formalization.

---

# External-theorem interfaces to keep separate

Do not attempt to reprove deep prime-gap or spectral theorems merely to formalize the local prime-flute deductions. Prefer named assumptions/theorem imports such as:

```text
PintzRatio:
  liminf (g_{n+1}/g_n) = 0 and
  limsup (g_{n+1}/g_n) = infinity

PintzThreeGap:
  limsup min(g_{n-1},g_{n+1}) /
         (g_n*(log n)^(1/632)) = infinity

PintzIsolatedCluster(k0):
  arbitrarily far out there is a bounded block of >= k0 consecutive primes
  with growing prime-free intervals on both sides

BHPShortInterval:
  sufficiently large x has a prime in [x, x+x^0.525].
```

The exact formal statements must match the cited literature, not these mnemonic forms.

For the spectral layer, keep Burger-style degeneration and Weyl-sequence arguments outside the initial Lean milestone. The valuable first formal result is that the **geometric neck length is exactly a cross-ratio function**; analytic consequences can then be attached without obscuring the finite core.

## Suggested first formalization milestone

A small file should be enough to establish:

```text
1. det G = 1
2. exact trace/cross-ratio identity
3. cross-ratio positivity
4. cuff tanh identity
5. logarithmic/shear telescoping identities
6. abstract short-neck limit
```

If these six survive Lean without hidden hypotheses or sign corrections, the central algebraic geometry of the current exploration has a reliable foundation.