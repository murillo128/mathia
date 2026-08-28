# PL-004 — Prime-exponent gas is classical prior art

## Claim

The statistical-mechanical interpretation of the prime-exponent vector `v(n)=(v_p(n))_p` as occupation numbers of independent prime modes with energies `E_p=log p` is classical. The total energy is

```text
E(n) = sum_p v_p(n) log p = log n,
```

and therefore

```text
Z(beta) = sum_{n>=1} exp(-beta E(n)) = sum_{n>=1} n^{-beta} = zeta(beta).
```

**Evidence/status:** `CLASSICAL-IDENTITY` — prior-art redirect.

This finding prevents the prime-lattice line from treating the free occupation-number picture as a novel spectral mechanism.

## Prior art already identified in the investigation

Bernard Julia's 1990 “Statistical theory of numbers” explicitly develops the free Riemann/primon gas dictionary: primes are elementary modes with energies `log p`; bosonic occupation numbers reproduce arbitrary positive integers by unique factorization; fermionic exclusion restricts states to square-free integers; the bosonic grand-canonical partition function is the Riemann zeta function; and Möbius-related signs admit a corresponding fermionic/supertrace interpretation.

This matches the prime-exponent construction essentially coordinate for coordinate.

Bost–Connes later constructed a richer operator-algebraic dynamical system whose partition function is also the Riemann zeta function and which carries arithmetic symmetry and a phase transition at inverse temperature `beta=1`.

Connes later gave a noncommutative adelic trace-formula interpretation in which critical zeta zeros appear as an absorption spectrum and hypothetical noncritical zeros as resonances.

## Relevance to the Mathia construction

The exponent lattice remains a useful conceptual representation:

```text
multiplication -> addition of occupation vectors,
log n          -> additive energy,
square-free    -> fermionic 0/1 occupation sector.
```

But that dictionary is not itself new. The prior art redirects the research question away from whether `v_p(n)` can be called an energy-occupation geometry and toward what additional structure could make such a representation sensitive to analytic continuation and the Riemann zero set.

The Bost–Connes and Connes constructions are important here only as evidence that richer arithmetic/dynamical or noncommutative structures have already been introduced in the literature. They do not imply that the bare prime lattice inherits those spectral conclusions.

## Novelty assessment

- Prime-exponent occupation numbers are a classical consequence of unique factorization.
- Energies `log p`, total energy `log n`, and partition function `zeta(beta)` are explicitly classical in Julia's Riemann gas.
- The square-free/fermionic connection and Möbius signs are also classical in this statistical-mechanics literature.
- The richer dynamical zeta partition function and adelic spectral interpretations are established prior art of Bost–Connes and Connes.

No Mathia novelty is claimed for these identifications.

## Boundary conditions and failure modes

- A partition function equal to `zeta(beta)` in its convergence domain does not by itself provide analytic continuation or a spectral realization of nontrivial zeros.
- The richer Bost–Connes/Connes structures are not equivalent to the bare exponent lattice; importing their conclusions without their extra structure would be invalid.
- Rephrasing the exponent vector as a state label or `log n` as energy is therefore not a substantive new RH mechanism.

## Audit criterion

Any novelty claim based only on `v_p(n)` as occupation number, `log p` as one-particle energy, `log n` as total energy, and zeta as partition function fails the novelty audit against Julia's construction. A genuinely additional claim must identify mathematical structure not already contained in that free-gas dictionary and must not silently import the extra structure of Bost–Connes or Connes.

## Consequence for the research line

The free prime-exponent statistical mechanics is baseline prior art, not a candidate discovery. Its value is as a clean coordinate model; any substantive RH contribution must arise from structure beyond that classical model.
