---
id: CLUE-weil-inertia-residual-defect-triangular-islands
type: research-clue
status: proposed
origin: research-watch
target_line: weil_inertia
based_on:
  - research/visual_exploration/visualizations/weil-inertia-defect-triangles.md
  - research/weil_inertia/findings/WI-096-residual-prime-rank-defect-is-exact-free-cycle-count.md
  - research/weil_inertia/findings/WI-099-residual-prime-rank-defect-is-single-rotation-resonance.md
  - research/weil_inertia/findings/WI-100-near-saturated-prime-rotation-resonances-have-bounded-incidence.md
  - research/weil_inertia/findings/WI-101-prime-rotation-resonances-have-gap-coprime-odd-denominators.md
---

# Is every residual Ramanujan defect sector an exact triangular island?

## Observation

WI-096 identifies the exact residual prime-pair row-rank defect with `max(0,c-1)`, where `c` is the free-cycle count of the boundary partial map. WI-099 shows that each nonzero state has a single rotation phase, and WI-100 gives a two-sided capacity tent but explicitly only as an upper envelope outside the special three-cycle sector.

The linked visual experiment scans the exact partial map as the boundary remainder `s` moves. For all distinct odd prime pairs with `11 <= p < 150` and all admissible `(k,s)`, every connected positive-defect component found was an exact unit-slope symmetric triangle. The same tent geometry survives a broad odd coprime composite control, suggesting that the phenomenon may be a structural law of the cyclic-order partial map rather than prime-specific arithmetic.

## Research question

For fixed admissible `(p,q,k)`, let `[L,R]` be a maximal connected interval of boundary remainders on which the WI-096 defect is positive. Is it always true in the prime residual regime that

\[
\boxed{\tau(s)=\min\{s-L+1,\;R-s+1\}\qquad(L\le s\le R)?}
\]

More strongly, does an analogous theorem hold for the abstract odd-coprime partial-rotation model, with boundary-truncated components obtained by restricting one universal triangular profile? Can `L` and `R` be characterized explicitly from the common WI-099 rotation phase `(m,\ell)` and the first/last collision of the moving deleted intervals?

## Why it may matter

A proof would sharpen WI-100 from a capacity upper tent to an exact defect profile and replace pointwise cycle counting by explicit resonance-support intervals. That could simplify incidence and many-modulus aggregation questions in the only remaining low/zero-defect sector.

Equally importantly, the composite matched control suggests a negative interpretation: the visually striking triangular islands may be universal cyclic-order geometry. Proving that universality would prevent the program from mistaking this structure for rational-prime specificity and would isolate whatever residual feature actual Yang coefficients or simultaneous many-modulus coupling must contribute beyond the pairwise boundary model.

## Decisive test

Prove or refute the triangular formula directly from the WI-096/WI-099 partial map as `s` increments by one. A promising route is to track how the two moving interval boundaries create and destroy recurrent rotation orbits and prove that, within one fixed reduced phase `(m,\ell)`, the free-cycle count changes by exactly one at each endpoint step until the center and then reverses.

The strongest version should:

1. derive explicit endpoint conditions `L(p,q,k,m,\ell)` and `R(p,q,k,m,\ell)`;
2. explain the symmetric unit slopes rather than fit them;
3. classify what changes when `p` is merely odd and coprime to `q`;
4. identify boundary-truncated control components as restrictions of the same profile, or exhibit a counterexample;
5. only after this control theorem, test whether actual prime/Yang many-modulus coupling has a residual statistic not determined by the universal tent data.

A single exact prime residual counterexample to the boxed formula kills the strongest conjecture.

## Evidence boundary

The current support is finite exact computation plus the persisted structural classification in WI-096, WI-099, WI-100, and WI-101. No general proof of the triangular law or endpoint characterization is known here, no novelty claim has been established, and the composite control makes prime-specific significance doubtful rather than stronger. The visualization is motivation, not canonical mathematical evidence. Nothing in this clue improves the current fourth-moment bound or implies a new statement about zeta zeros.
