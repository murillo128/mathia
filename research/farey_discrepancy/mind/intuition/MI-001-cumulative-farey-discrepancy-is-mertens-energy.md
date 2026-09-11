# MI-001 — Projective Farey rigidity now depends on excluding source-specific hyperbola amplification

**Evidence level:** supported

## Core intuition

Linear Möbius ancestry does expose a genuine normalized projective defect, but generic local regularity cannot make that defect pointwise. The remaining escape has become much more specific: sparse low Jordan rows may sample anomalously large quotient-shell values and overwhelm the universal positive occupation carried by the terminal bulk.

This is not an arbitrary free-model loophole. Terminal quotient blocks already have a fixed nonsquarefree Jordan density, and every finite supercritical Mellin packet is coercively sampled by nonsquarefree rows. A physical failure must therefore use genuinely source-specific hyperbola amplification, growing/infinite spectral complexity, or another mechanism outside both controls.

## Strongest justified claim

FD-031 reduces linear-prefix saturation to alignment with one distinguished Schur direction. FD-032--FD-034 show that the physical tail has macroscopic nonsquarefree mismatch and that square-divisor self-similarity forces a positive geometric/Cesaro projective defect along every complete `4`-adic chain, while FD-033 proves that absolute energy is the wrong currency because the physical Schur tail is superlinear.

FD-035--FD-037 show why this does not automatically become pointwise: multiplicative descendants leave gaps, and bounded increments only localize a possible occupation failure toward low Jordan rows. FD-038 then proves a universal terminal-block theorem. For every fixed `alpha<1/3`, the range `k<=H^alpha` carries a fixed positive nonsquarefree Jordan fraction independently of the nonnegative shell profile, and the physical terminal energy is already superlinear.

FD-039 is the decisive generic countercontrol. One can construct a one-Lipschitz shell profile with divergent critical energy for which sparse low-row hyperbola samples dominate the terminal bulk and drive the global nonsquarefree occupation ratio to zero along a subsequence. Thus bounded increments, exact hyperbola geometry, and divergent energy are insufficient.

FD-040 narrows the escape again. Nonsquarefree rows form a positive frame on every finite Mellin-frequency span at fixed `beta>1/2`; consequently any finite supercritical Mellin asymptotic has a uniform positive occupation fraction. The FD-039 spike mechanism cannot be reproduced by finitely many fixed logarithmic frequencies.

## Synthesis of evidence

The projective problem has separated into a universal bulk and a source-specific amplification channel. The universal bulk is already favorable; the free-model counterexample must concentrate outside it. Finite spectral models are also favorable. The missing theorem therefore lies between them: control the complexity with which the physical quotient-shell source can place large values on the sparse hyperbola samples corresponding to low Jordan rows.

The exact coefficient identity for the physical shell increments is the most concrete surviving source distinction. A spectral alternative would need uniform frame constants as the Mellin packet grows or loses a rightmost gap.

## Counterevidence / boundary cases

FD-040 is conditional when transferred to the physical source: it assumes a finite dominant Mellin packet with fixed supercritical real exponent. It does not control infinitely many comparable poles, a growing packet, a critical accumulation, or cancellations that destroy any fixed spectral gap.

FD-039 is synthetic and does not satisfy the physical multiplicative increment law. It proves only that generic smoothness/energy arguments cannot close the problem.

## Epistemic status

**Supported source-specific narrowing:** normalized Farey rigidity is unconditional on average and terminal nonsquarefree occupation is universal; generic one-Lipschitz sources can still evade globally, but every fixed finite supercritical Mellin packet is coerced. The unresolved burden is physical hyperbola-sampling amplification in the genuinely infinite/growing spectral regime or an equivalent use of the exact arithmetic increment law.

## Novelty/prior-art status

No broad novelty claim is made beyond the persisted finding-level audits. This note synthesizes the exact Mathia boundaries FD-031--FD-040.

## Falsification criterion

Construct a physical-compatible shell profile obeying the exact arithmetic increment law that realizes the FD-039 low-row amplification while remaining compatible with the surviving Farey geometry, or prove that a finite-packet coercivity constant can collapse under a physically admissible growing packet in a way that reproduces the same escape. Either would narrow or refute the current source-specific diagnosis.
