# MI-009 — Arithmetic identifiability is readout-relative and remains independent of zero selection

**Evidence level:** supported by PL-125--PL-141; exact for the stated Grosswald--Schnitzer and prime-phase quotient controls, with literature-backed pretentious/inverse inputs

## Core intuition

Prime Lattice now separates three questions that are easily conflated: whether the arithmetic source is identifiable, whether the chosen readout has already quotiented away part of that source, and whether the resulting analytic object has any mechanism forcing its zero divisor onto the critical line.

Discrete arithmetic can make an analytic phase family finitely identifying, while a metric projection can remain exactly blind even after all positive powers are added. Conversely, inverse small-sum structure can recover a prime phase that was already known while looking at the wrong divisor orientation for the Riemann zeros. Strong source information is therefore not automatically the missing RH selector.

## Strongest justified principle

PL-130--PL-132 give the Grosswald--Schnitzer hierarchy. Continuous generator controls have exact finite phase aliases; accumulating critical-line phase data identify the whole deformation; integer discreteness compresses any fixed low-generator prefix to finitely many phase samples uniformly over arbitrary integer tails. PL-133 keeps the boundary explicit: all members already share the relevant zeta zero divisor.

PL-139 adds an exact power-tomography gate. For exact positive powers indexed by `K`, `d=gcd(K)>1` leaves the independent prime-wise torsion gauge `product_p mu_d`; when `d=1`, exact phase values recover the base phase and simultaneous pretentiousness collapses to ordinary pretentiousness. Merely taking several powers creates no intermediate qualitative source rigidity.

PL-140 shows that the situation is stricter after metric scalarization. Pretentious distances of **all** positive powers depend prime-wise only on `cos(phi_p)` or chord magnitudes and are invariant under independent reflections `r_p -> conjugate(r_p)`. The full cutoff profile at power one already determines the higher power distances, but not orientation. Exact complex power data or the full Kronecker time profile escape because they retain oriented coefficients. Thus enrichment cannot repair a quotient that the readout itself has imposed.

PL-141 closes a complementary inverse route for Möbius. Small-sum inverse structure specializes to the already exact phase `mu(p)=-1` (or `-p^{i gamma}` after twisting), while its zero-transition theorem is oriented toward zeros of `L(s,mu)=1/zeta(s)` near `1`. Nontrivial zeta zeros are poles of this reciprocal. RH-strength Möbius cancellation excludes them directly through analytic continuation of `1/zeta`; the inverse phase theorem does not manufacture a new localization mechanism.

## Evidence synthesis and boundaries

These results do not say phase metrics or inverse theorems are weak. Pretentious distances transfer cancellation from a comparator, full time profiles can recover oriented prime coefficients, and inverse theorems strongly constrain general multiplicative functions. The restriction is explanatory: one must identify what the readout retains and whether the theorem acts on the same divisor orientation as the target.

A viable RH mechanism may combine source rigidity with functional equation, explicit-formula positivity, a pole-sensitive reciprocal theorem, or a different zero-sensitive observable. Those are additional structures rather than consequences of source identification alone.

## Status / novelty

Grosswald--Schnitzer rigidity, pretentious metrics, structured-power theorems, and inverse small-sum results are literature or persisted exact inputs. The synthesis is the readout-relative hierarchy: **source fidelity can be exact, finite, or metrically stable while still missing orientation or acting on the wrong analytic divisor, and none of those achievements is zero selection by itself**.

## Falsification criterion

Construct an all-positive-power pretentious metric that distinguishes independent prime-wise conjugation within the PL-140 hypotheses, or show that the current Möbius inverse theorem localizes poles of `1/zeta` rather than its zeros without an additional analytic input. For RH relevance, derive the missing sign/unitary/pole-sensitive theorem on a zero-sensitive representation.

## Lean-formalizable core

- Finite-prefix phase identification under discrete controls.
- GCD torsion kernel for exact power observations.
- Independent reflection quotient for real-part/chord power metrics.
- Logical zero/pole orientation for reciprocal Dirichlet series.
