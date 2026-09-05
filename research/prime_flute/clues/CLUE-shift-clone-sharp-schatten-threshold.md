---
id: CLUE-prime-flute-shift-clone-sharp-schatten-threshold
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-107-shift-clone-cuff-defect-is-l2-not-l1.md
  - research/prime_flute/findings/PF-109-shift-clone-preserves-canonical-separator-pinching-multiplicatively.md
  - research/prime_flute/findings/PF-112-first-relative-resolvent-is-not-trace-class.md
  - research/prime_flute/findings/PF-125-shift-clone-has-compact-relative-resolvent.md
  - research/prime_flute/findings/PF-126-shift-clone-metric-defect-is-Lp-above-one.md
  - research/prime_flute/findings/PF-127-collapsing-canonical-collar-is-schatten-benign-above-trace-endpoint.md
  - research/prime_flute/findings/PF-130-lambert-shift-metric-defect-is-strong-L1-summable.md
  - research/prime_flute/findings/PF-147-square-resolvent-S1-forces-first-resolvent-S2.md
  - research/prime_flute/findings/PF-150-square-resolvent-S1-is-sharp-at-S2-without-geometry.md
  - research/prime_flute/findings/PF-169-all-margulis-short-central-squared-resolvent-blocks-are-trace-summable.md
  - research/prime_flute/findings/PF-171-all-margulis-short-central-first-resolvent-blocks-have-sharp-Sr-threshold.md
---

# Does the prime/shift relative resolvent have the sharp Schatten threshold `S_r`, `r>1`?

## Observation

PF-112 fixes the unavoidable local endpoint for any genuinely different two-dimensional metric pair: the first relative resolvent is locally of critical order `-2`, so `S_1` is impossible while every exponent `r>1` remains compatible with microlocal order. PF-125 proves global compact relative resolvent for the exact prime flute versus the exact all-composite shift clone, and PF-126 places the transported coefficient defect in weak `L^1` and every `L^r`, `r>1`.

The closed-thin central geometry is now much more settled. PF-127 proves on one fixed central Dirichlet collar that the first relative resolvent lies in every `S_r`, `r>1`, with

\[
\|A_{L,L_+}^{(R)}\|_{\mathcal S_r}^r
\le C_{R,r}|\log(L_+/L)|^rL^{2r-1},
\]

while remaining outside `S_1` whenever `L_+ != L`. PF-169 sums the corresponding **squared** relative-resolvent blocks over every Margulis-short core and obtains trace class. PF-171 now performs the sharper first-resolvent summation itself: using PF-138's complete short-core count and PF-109's `O(P^-3)` logarithmic length defect,

\[
\boxed{
\bigoplus_{\eta\in\mathcal S}A_\eta
\in\mathcal S_r\ \text{for every }r>1,
\qquad
\bigoplus_{\eta\in\mathcal S}A_\eta\notin\mathcal S_1.
}
\]

Thus zero systole, collar pinching, and the **full multiplicity** of Margulis-short central blocks are no longer candidate obstructions, even in the difficult interval `1<r<2`.

PF-130 independently shows that the isolated Lambert body comparison has summable strong-`L^1` metric/density mass. PF-147 says a future global squared-resolvent `S_1` result would force the full first relative resolvent into `S_2`, while PF-150 proves that this abstract implication cannot by itself cross below `2`. PF-171 is therefore informative precisely because the actual collar geometry *does* cross below `2`; any surviving sub-`2` obstruction must be created by the uncut global assembly rather than by the central thin blocks.

## Research question

For the common-manifold Laplacians associated with the PF-125 marking, does

\[
A
:=
(\Delta_{g_+}+1)^{-1}
-
(\Delta_g+1)^{-1}
\]

satisfy

\[
\boxed{
A\in\mathcal S_r\quad\text{for every }r>1,
\qquad
A\notin\mathcal S_1?
}
\]

PF-112 proves the second statement for the full non-isometric pair. The positive side is now localized much more sharply: the complete decoupled central short-collar family already has the desired threshold by PF-171. What remains is whether complementary pant/body pieces, outer collar sectors, cutoff commutators, boundary transmission, and repeated interactions created by removing the Dirichlet interfaces preserve that threshold.

## Why it may matter

A positive answer would finish the natural operator-ideal classification between PF-112 and PF-125 and show that even the sharp first-resolvent ideal scale is compatible with an exact all-composite control. It would also make `S_2`-level regularized determinant machinery available while ordinary trace-class determinant constructions remain excluded. None of that would be prime-specific by itself.

A negative answer for some `r>1` would now be more informative than before: it would identify a genuinely global amplification mechanism absent from every isolated and collectively summed central short collar. Such a body/interface/transmission obstruction would be a new structural feature of the infinite assembly rather than another manifestation of zero systole.

## Decisive test

A positive resolution must control the **uncut** operator. Two routes remain complementary. First, proving the global squared-resolvent difference is `S_1` would, through PF-147, settle `r>=2`; PF-150 shows that additional surface-specific estimates would still be required for `1<r<2`. Second, a direct IMS/resolvent, boundary-transmission, or heat-kernel Schatten decomposition could attack the first resolvent and potentially preserve PF-171's sharp threshold across the remaining body/interface terms.

A decisive negative resolution must produce an actual singular-value lower bound in a channel excluded from PF-171 — for example a non-summable boundary-transmission or commutator family. Concentration solely in fixed-central Margulis-short collars, either one at a time or over their complete orthogonal family, is no longer a viable counterexample.

## Evidence boundary

PF-171 is a theorem about the **Dirichlet-decoupled fixed-central collar direct sum**. It does not estimate the full uncut Laplacian, outer collar pieces, body terms, or the operators created when infinitely many Dirichlet interfaces are removed. PF-130 is likewise a coefficient estimate on the explicit Lambert comparison rather than a global Schatten theorem.

PF-147 remains conditional on the still-open full-surface squared-resolvent `S_1` gate, and PF-150 is only an abstract limitation of functional calculus. Standard compact/bounded-geometry pseudodifferential theorems cannot simply be globalized across this zero-systole infinite-type surface. The existing Güneysu--Thalmaier scattering criterion is useful for wave operators but is not a Schatten theorem, and the Behrndt--Langer--Lotoreichik resolvent-power results concern smooth-domain boundary-condition perturbations rather than this metric assembly.

## Research disposition

The clue remains `accepted`, but PF-171 materially narrows it. The **entire closed-thin central sector already satisfies the conjectured sharp `S_r`, `r>1`, classification**, including the previously delicate range below `2`. Future work should therefore focus on body/interface/transmission and uncut infinite assembly. The clue will be resolved only when those remaining terms either preserve the sharp threshold globally or yield a genuine operator-level counterexample for some `r>1`.