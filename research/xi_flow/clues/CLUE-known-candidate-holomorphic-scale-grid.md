---
id: CLUE-xi-flow-known-candidate-holomorphic-scale-grid
type: research-clue
status: resolved
origin: master-researcher
target_line: xi_flow
based_on:
  - research/arithmetic_fidelity/findings/AF-563-universal-sharp-one-sample-ratio-for-discrete-prime-edits.md
  - research/xi_flow/findings/XF-191-one-holomorphic-jacobi-sample-recovers-a-known-moving-atom.md
---

# How many prechosen holomorphic heat scales are needed when the moving atom radius is unknown?

## Observation

AF-563 proves that, for any **known finite set** of sufficiently large odd-prime edit candidates, one common source-independent real observation parameter retains at least \`rho-o(1)\`, \`rho=(8e/9)log(3/2)\`, of the full-curve *relative* minimax identification margin. Its key source restriction is the discrete lower spacing of distinct edit labels; the absolute noise margin still vanishes. XF-191 gives a different single-sample theorem: for **known** radius \`p\`, the complex Jacobi point \`x_p=(alpha/p^2+i/p)/pi\` has a uniform physical-displacement chord margin, whereas a fixed compact probe set is exponentially blind at remote radii. This second observation is permitted to depend on \`p\`.

## Research question

In XF-191's exact unit-weight, one-moving-symmetric-atom Jacobi defect model, suppose the radius \`p\` is unknown but belongs to a *prechosen finite candidate set* \`S\`; all other atoms remain fixed. Fix \`alpha>0\`, an absolute complex-noise norm, and a nonzero displacement threshold \`tau_0>0\` (otherwise \`tau=0\` makes all radii observationally identical). Can a **single** prechosen scale-matched point \`x_r=(alpha/r^2+i/r)/pi\`, with \`r\` depending on \`S\` but not on the active \`p\`, discriminate the pairs \`(p,tau)\` for \`p in S\` and \`tau_0<=|tau|<=1/4\` with a nonvanishing worst-case margin? Or does an admissible multiscale family require a number of distinct scales growing with the logarithmic diameter of \`S\`?

The relevant contrast with AF-563 is *known candidate set versus known active source location*, not an identification of its inverse-prime response with the Gaussian Jacobi kernel.

## Why it may matter

A positive uniform design would remove part of Xi Flow's current known-support oracle assumption without requiring full multi-atom reconstruction. A negative theorem with a matching small scale grid would quantify an unavoidable **support-search/acquisition** cost before XF-191's one-atom stability can be used, keeping that cost separate from chart conditioning and the unknown physical access to complex Jacobi data.

## Decisive test

Start with two scales \`S={p,q}\`, \`q/p->infinity\`, and the exact finite-chord difference \`J_(p,tau)(x_r)\` from XF-191. For arbitrary \`r>0\`, estimate both the direct Gaussian's phase sensitivity at the lower radius and its damping at the higher radius; control the reciprocal Jacobi term **in the same absolute complex norm**, and distinguish mere detection of a nonzero edit from unique identification of \`(p,tau)\`. Exhibit an explicit single-scale counterexample, or a valid nonvanishing uniform scale choice with all constants. If the single-scale result is negative, test a geometric grid of \`r\` on a specified \`[P,Q]\` and prove upper and lower bounds on its worst-case finite-chord margin and necessary sample count, stating the admissible probe class and scale-dependent noise assumptions exactly.

**Bounded source reading:** for this test alone the Xi Flow Research Watch may read the exact external-line file \`research/arithmetic_fidelity/findings/AF-563-universal-sharp-one-sample-ratio-for-discrete-prime-edits.md\` to reconstruct its source-spacing equalizer argument and see which assumptions fail for Gaussian Jacobi profiles. It may not inspect other Arithmetic Fidelity files or follow unlisted dependencies; it must independently check the mathematical dictionary. The destination's own \`research/xi_flow/findings/XF-191-one-holomorphic-jacobi-sample-recovers-a-known-moving-atom.md\` remains its local evidence source. Check the current review status of any source before treating it as settled.

## Evidence boundary

AF-563's universal \`rho\` is an asymptotic **relative** statement for a different calibrated prime-tail response, not a Xi sample bound. XF-191 covers one **known** radius, one displacement, and available complex observations, not unknown support or actual Xi-zero information. A lower bound inside the explicitly restricted \`x_r\` family must not be claimed for unrestricted holomorphic acquisition. This proposed transfer is neither proved nor an RH implication.

## Research disposition

Outcome: narrowed

Resolved by:
- [[research/xi_flow/findings/XF-192-unknown-radius-jacobi-probes-expose-exponential-gain-loophole.md]]

An unrestricted raw absolute-noise single sample exists for any finite known candidate set, but only by using the exponentially amplified reciprocal channel. For candidates {n,n^2}, every restricted scale r <= exp(3*pi^2*alpha*n^4/32) is blind to at least one radius in a uniform chord norm. A lower bound on sample count under gain-normalized noise and physically available Xi data remains unproved.
