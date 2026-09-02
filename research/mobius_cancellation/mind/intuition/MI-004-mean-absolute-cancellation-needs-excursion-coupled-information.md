# MI-004 — Mean-absolute cancellation needs a source-faithful carrier that survives diffusive controls

**Evidence level:** supported for the exact pathwise decompositions and matched controls; RH relevance of the mean-absolute endpoint remains conditional on the still-audited Pintz input

## Core intuition

Passing from pointwise Mertens bounds to mean-absolute size can weaken the endpoint, but many natural positive or excursion-based carriers are still much stronger than the cancellation they are meant to explain. The exact Tanaka decomposition loses the mechanism if its large pieces are bounded separately, and the excursion-square budget is already falsified by a support-matched random-sign control with diffusive mean-absolute behavior.

The next lossless carrier, path energy, preserves amplitude information but encounters the opposite obstruction: its coarse constant mode is itself an RH-equivalent first Riesz sum. The research problem is therefore not to find another norm of the path, but to isolate **signed, growing-scale information upstream of the RH-equivalent coarse mode**.

## Strongest justified principle

MC-013 gives the exact discrete Tanaka identity `N D_M(N)=C_sgn(N)+L_0(N)`. MC-014 gives the decisive multiplicative control: a real character modulo `3` has bounded summatory walk while both triangular pieces are quadratic and cancel to linear order. Separate positive budgets on those pieces are therefore structurally misaligned.

MC-014 also proposed the excursion-square statistic `E_2=sum ell_j^2` as a cancellation-preserving sufficient carrier. MC-015 shows that qualitative index-two Chowla plus exact squarefree support can still allow near-quadratic excursion mass. MC-016 is sharper: a support-matched random-sign walk can have a macroscopic excursion and `E_2~N^2` while its mean-absolute size is only diffusive. Thus `E_2` is not the right necessary-scale model for the desired endpoint.

MC-016--MC-017 replace it by the exact path energy `V_a(N)=sum_{k<N}|A(k)|^2`, with `D_a(N)^2<=V_a(N)/N` and an exact boundary-cancelled Fourier representation weighted by `sin(pi t)^{-2}`. This correctly identifies low-frequency phase coherence rather than raw support as the relevant information.

MC-019 then closes the naive path-energy escape: the constant/coarse component of `V_M` contains the first Riesz sum `R_1(N)=sum_{k<N}M(k)`, and RH-scale control of that coarse mode is already RH-equivalent. The carrier is faithful, but the desired estimate has not become easier merely by squaring and averaging the path.

## What remains possible

A useful mean-absolute mechanism must expose signed information that is neither a separately positive Tanaka budget, an overstrong excursion-duration budget, nor a norm whose coarse component already restates RH. Plausible categories include multiscale phase-sensitive decompositions, source-natural cancellation between coarse and oscillatory Fourier pieces, or identities where an independently controlled arithmetic factor cancels the RH-equivalent coarse mode before positivity is taken.

Any proposed statistic should be tested against the character control, support-matched random signs, and the coarse-Riesz projection before being promoted.

## Status / novelty

Discrete Tanaka identities, excursion decompositions, Fourier summation, and Riesz means are classical in spirit. The Mathia synthesis is the sequence of matched-control eliminations: **lossless is not sufficient, positive is often too strong, and a faithful Hilbert norm can still hide an RH-equivalent coarse coordinate**.

## Falsification criterion

Exhibit a proposed source-natural carrier that passes the character and random-sign controls, whose RH-scale bound does not already imply the required Riesz estimate by a trivial projection, and derive its bound from independent Möbius arithmetic. Conversely, show that every candidate in a claimed class necessarily contains an RH-equivalent coarse component.

## Lean-formalizable core

- Discrete Tanaka identity and character cancellation.
- Excursion-area versus excursion-square bounds and random-walk counterexample.
- Path-energy/Cauchy transfer to mean absolute size.
- Boundary-cancelled Fourier path-energy identity.
- Coarse-mode projection onto the first Riesz sum.