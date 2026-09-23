# MI-070 — Any Wang-shell holonomy must pass through mesoscopic sign transitions

**Evidence level:** supported within the current Wang-shell representation by [VIS-412](../../findings/VIS-412-wang-bohr-shell-orthogonality-kills-bargmann-cycles.md), [VIS-413](../../findings/VIS-413-wang-real-shells-quantize-finite-window-bargmann-phase.md), and [VIS-414](../../findings/VIS-414-wang-sign-definite-windows-balance-cycle-holonomy.md).

VIS-412 removes the canonical Bohr-average route to shell holonomy. Distinct dyadic Wang shells are orthogonal in the near-band model, so their canonical Gram graph has no inter-shell edges and therefore no nontrivial Bargmann cycles. Any cycle seen after finite-windowing or tapering is consequently introduced through that additional representation rather than inherited automatically from the Bohr geometry.

VIS-413 then constrains what such a finite-window cycle can encode when the canonical shell functions and the window are real. The resulting Gram matrix is real symmetric, so every nonzero Bargmann cycle phase is quantized to `0` or `pi`. Generic `U(1)` phase is unavailable unless one adds a complex packetization whose source justification must be supplied separately.

VIS-414 tightens the real case further. If the participating shell functions are sign-definite on the support of the chosen nonnegative window, a diagonal sign gauge makes every relevant Gram entry nonnegative and all cycle phases trivial. A negative `Z_2` cycle therefore requires the window to encounter genuine sign or zero transitions among the coupled shells. Sign-transition incidence is a necessary local resource for any nontrivial real finite-window holonomy.

The surviving visual question is thus not whether arbitrary shell phases form interesting loops, but whether the arithmetic source forces a stable mesoscopic pattern of simultaneous sign transitions that survives a source-justified windowing rule. That is the first place where a finite-window cycle could carry information not already removable by orthogonality or diagonal gauge.

**Boundary.** The sign-transition condition is necessary, not sufficient. These findings do not prove a source-derived negative cycle, do not make finite-window holonomy canonical, and do not justify introducing complex packets solely to recover continuous phase.