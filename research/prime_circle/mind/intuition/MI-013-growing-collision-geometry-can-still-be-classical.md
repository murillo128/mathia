# MI-013 — Prime-Circle complexity survives only in a primitive parity-reduced long torus cocycle

**Evidence level:** proved structural boundary

## Core intuition

Growing collision geometry is not enough. In the shared-upper construction, rank, orientation, determinant volume, full finite singular spectrum, and every fixed local window are classicalizable. The surviving fixed-width torus-return cocycle has now lost two further apparent sources of complexity: common dilation produces exact block repetition, and reflection makes the collision word exactly palindromic.

Any arithmetic information must therefore live in a **primitive, parity-reduced, depth-growing invariant** of the return cocycle.

## Strongest justified claim

PC-253--PC-258 reduce the complete shared-upper defect to a pathwidth-two transfer recursion whose local coefficients are rational-torus return observables. Growing rank increases word length but not interaction width, and every fixed local window has the corresponding classical return law.

PC-259 proves an exact dilation identity: after simultaneous integer refinement the normalized defect is `I_m tensor Delta`. The complete normalized spectrum and block transfer dynamics are copied `m` times. Common conductor growth therefore does not create new cocycle depth.

PC-260 proves exact reversal symmetry. Collision weights and adjacency bits are palindromic; the operator commutes with reversal; and the squared-singular-value problem splits into even and odd sectors. Since the collision count is even, one half-word together with the parity boundary condition determines the other half.

## Synthesis of evidence

The live discriminator has become highly specific. First reduce a conductor triple to its primitive ratio data; then quotient the exact reversal symmetry; only after these controls ask whether the remaining growing transfer product has an asymptotic not determined by ordinary rational-torus dynamics.

Candidates include parity-sector Lyapunov rates, rare-return resonances, or another statistic whose observation depth grows with the primitive denominator. Another fixed-depth trace, common refinement limit, or forward/backward comparison cannot escape the established closure.

## Counterevidence / boundary cases

PC-259 concerns common integer dilation, not arbitrary sequences of primitive prime triples. PC-260 halves the independent input but does not make the long product finite or prove its two parity sectors universal. Rational torus returns at prime-linked denominators may still have nonlocal arithmetic correlations.

Thus the remaining branch is not closed; it is stripped of two misleading notions of growth.

## Epistemic status

**Exact primitive/parity boundary:** full finite spectral data are fixed-width torus-coded, common refinement is exact direct-sum repetition, and reflection removes independent backward-word information. Only primitive parity-reduced long-range cocycle behavior remains unclassified.

## Novelty/prior-art status

The lattice, transfer, mechanical-word, direct-sum, and reflection ingredients retain their finding-level classifications. This intuition records their joint information boundary.

## Falsification criterion

Find a normalized common-dilation family that changes a block-normalized transfer invariant despite PC-259, or a collision word violating the exact reversal parity of PC-260. Strategically, prove that every primitive parity-sector depth-growing invariant is determined by classical torus-return data; that would close the surviving branch.

## Lean-formalizable core

The direct-sum dilation identity, reflection of the collision coding, and parity decomposition are finite combinatorial linear-algebra targets.