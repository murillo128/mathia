---
id: RG-arithmetic-fidelity-euler-harmonic-collision-budget
type: research-graph-relation
scope: arithmetic_fidelity
derived: true
---

# Euler harmonic collision budget

[[research/arithmetic_fidelity/graph/arithmetic-fidelity|Arithmetic Fidelity research graph]]

## Source restriction and observation boundary

[[research/arithmetic_fidelity/findings/AF-216-ordered-sign-complexity-caps-moment-and-dirichlet-cancellation|AF-216]] gives exact finite Dirichlet detection from bounded ordered sign variation. [[research/arithmetic_fidelity/findings/AF-217-nontrivial-zeta-zeros-obstruct-all-order-euler-total-positivity|AF-217]] obstructs its unrestricted all-order transfer to the full Euler logarithm; this does not refute a fixed-order theorem with additional sampling restrictions. [[research/arithmetic_fidelity/findings/AF-218-full-euler-log-is-strictly-sign-regular-of-order-two|AF-218]] and [[research/arithmetic_fidelity/findings/AF-219-full-euler-log-is-strictly-sign-regular-of-order-three|AF-219]] establish global orders two and three, while [[research/arithmetic_fidelity/findings/AF-220-curvature-separation-certifies-finite-order-euler-sign-regularity|AF-220]] supplies a finite-order curvature/separation certificate. A collapsing sufficient certificate is not a counterexample to sign regularity.

## Harmonic tail versus inherited collisions

[[research/arithmetic_fidelity/findings/AF-337-deep-half-plane-harmonic-tail-restores-finite-euler-sign-regularity|AF-337]], especially its “Relation to the existing Euler obstruction chain,” supplies a different finite-order regime: for fixed order `r`, spacing `h>0`, window ratio `A>1`, and distinct integer norms in `[P,AP]`, sufficiently large `P` and `sigma>(h+1) binom(r,2)` make the full-Euler sampling matrix strictly sign-regular through order `r`.

[[research/arithmetic_fidelity/findings/AF-338-harmonic-collision-count-reduces-euler-sign-depth-to-linear-order|AF-338]] strengthens that sufficient depth to `sigma>r-1`. Its relative determinant comparison preserves pairwise collision factors between columns carrying equal harmonic labels; only unequal labels spend an inverse source-gap factor. Counting those losses by extra harmonic order yields a relative remainder `O(P^-(sigma-(r-1)))`. The constants and tail onset still depend on `r,h,A,sigma`.

## Qualifications

The newer theorem strengthens AF-337's uniform tail bound; it does not withdraw AF-337 or contradict AF-217. Integer spacing and the fixed multiplicative window are hypotheses. The depth threshold is sufficient, not claimed optimal; the earlier order-two and order-three theorems remain stronger in their global low-order regimes. Primes and matched composite/integer controls all satisfy the tail theorem. Exact detection is not uniform stable inversion, and for `r>=2` the sufficient depth remains in `sigma>1`; neither prime-specific source sign control nor zero-sensitive transport is supplied.

[[research/arithmetic_fidelity/mind/intuition/MI-018-signed-complexity-only-transfers-through-sign-regular-observations|MI-018]] retains the AF-337 margin principle. The linear-depth refinement above is grounded directly in AF-338, without rewriting that synthesis.

The direct AF-337/AF-338 references are native links in the canonical source prose. This mechanism note supplements those directed dependencies and scoped comparisons; it does not assert reverse or transitive implications.
