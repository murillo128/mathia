---
id: CLUE-prime-flute-positive-width-transition-schur-complement
type: research-clue
status: proposed
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-342-sharp-physical-cutoff-forces-order-one-direct-angle-correlation.md
  - research/prime_flute/findings/PF-343-uniformly-small-physical-hard-sector-gaps-force-order-one-direct-angle-correlation.md
---

# Can a positive-width transition band absorb the collapsing-corridor mode after exact Schur elimination?

## Observation

PF-342 shows that the canonical sharp fixed physical \`L/H\` split has order-one low/high canonical correlation. PF-343 strengthens the mechanism: the direct hard-sector angle is still noncompact whenever opposite sectors contain bounded physical Fourier modes separated by at most one sufficiently small fixed physical distance.

Therefore moving the hard cutoff or inserting only a narrow direct gap does not address the obstruction. The first representation change not covered by the argument is a genuine three-sector decomposition

\[
\mathcal H=L\oplus T\oplus H
\]

in which the transition band \`T\` has a physical width bounded below independently of the cuff period and is **retained in the full positive boundary form** before being eliminated.

Schur-complement realizations of Dirichlet-to-Neumann operators are classical, so the operation itself is not new. The unresolved issue is its quantitative effect on the exact collapsing Prime-Flute corridor.

## Research question

Let

\[
M_n=Q_n+\Lambda_{E,n}>0
\]

be the raw completed positive boundary form on one tail module. Choose bounded physical cutoffs

\[
0<\kappa_-<\kappa_+
\]

with fixed separation \`\eta=\kappa_+-\kappa_->0\`, and decompose Fourier modes into

\[
L_n=\{|\xi|\le\kappa_-\},
\qquad
T_n=\{\kappa_-<|\xi|<\kappa_+\},
\qquad
H_n=\{|\xi|\ge\kappa_+\}.
\]

Form the exact positive shorted/Schur-complement form on \`L_n\oplus H_n\`,

\[
M_n^{/T}
=
M_{LH,LH}
-
M_{LH,T}M_{TT}^{-1}M_{T,LH},
\]

with the appropriate quadratic-form interpretation if an inverse must be taken on the supported transition range.

After normalizing by the \`L\` and \`H\` diagonal blocks of \`M_n^{/T}\`, does the resulting effective low/high canonical-correlation operator become compact, Hilbert--Schmidt, or weak trace class at the scale needed by the Prime-Flute endpoint?

Equivalently: **does the fixed-width transition band absorb the leading collapsing-corridor response, or does an order-one canonical correlation survive the Schur complement?**

## Why it may matter

PF-343 removes cosmetic versions of cutoff smoothing. A positive answer here would be the first direct-angle representation in which low and high are genuinely separated at finite physical scale while all intermediate boundary degrees of freedom are still accounted for exactly.

A negative answer would close a much larger family of completed-angle architectures: not only hard binary cutoffs, but also the natural finite-width transition-band repair suggested by PF-342/PF-343.

The test is also structurally clean. It asks whether the leading thin-corridor response is carried by a transition subspace that can be shorted out, rather than asking for another absolute estimate on the same obstructed binary angle.

## Decisive test

Work first on one PF-341 tail pant, then on the symmetric two-pant module.

At corridor scale the leading positive self-DtN form behaves like a large, highly coherent boundary response concentrated near the finite-finite foot. Resolve that leading form in the physical Fourier basis across \`L/T/H\`.

The decisive calculation is the leading Schur complement of the transition block:

1. obtain uniform-in-\`L\` asymptotics for \`M_{LT}\`, \`M_{TT}\`, and \`M_{TH}\` on a fixed physical transition interval;
2. determine whether
   \[
   M_{LH}-M_{LT}M_{TT}^{-1}M_{TH}
   \]
   cancels the full \`1/(sL)\` corridor contribution between low and high;
3. normalize by the Schur-complement diagonal energies, not by the pre-elimination blocks;
4. if the normalized mixed response is \`o(1)\` with a summable/ideal-compatible rate, continue to separated-module reassembly;
5. if it remains bounded below on infinitely many separated modules, reject the route by the PF-342/PF-343 noncompactness template.

A useful first finite model is the corridor-leading Gram form restricted to all Fourier modes in a fixed compact physical interval. Because the number of transition modes grows like \`\eta L/(2\pi)\`, the test must keep the whole growing transition block; a fixed-rank surrogate would not answer the question.

## Evidence boundary

No cancellation theorem is established here. PF-343 only proves that **direct** opposite hard sectors cannot be physically too close. It does not determine the Schur complement after a positive-width intermediate band is retained.

General DtN/Schur-complement theory guarantees algebraic positivity properties under suitable hypotheses but does not supply the Prime-Flute asymptotic cancellation or Schatten estimate.

This clue therefore proposes a new operator calculation; it is not evidence that transition-band elimination succeeds, and it does not establish any scattering, determinant, zeta-zero, critical-line, or RH consequence.
