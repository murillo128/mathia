# MI-012 — The Xi theta-tail hazard is source-specific but not yet coercive

**Evidence level:** exact theta-source asymptotics and matched Gaussian-mixture separation through XF-162

## Core intuition

The actual Xi Fourier source now has a quantitative invariant that the strongest positive analytic maximal-contact controls fail. Its tail is not merely smooth or rapidly decaying: after normalization by `e^{4u}`, the logarithmic action, hazard, and curvature approach fixed nonzero constants determined by the leading theta term.

This identifies genuine Xi-specific source information. It does **not** yet show that the information reaches the transition. Far-tail asymptotics may coexist with substantial freedom at the finite/mesoscopic scales where maximal contact is assembled.

## Strongest justified principle

XF-160 constructs nonnegative even source controls with prescribed asymptotic transition gaps, and XF-161 Appell-smooths them to strictly positive real-analytic Gaussian-mixture densities while preserving the gap on any fixed finite heat window. Positivity and ordinary analytic regularity are therefore insufficient.

XF-162 computes the actual theta source asymptotics. With `T_rho(u)=-e^{-4u}log rho(u)` and `H_rho(u)=-e^{-4u}(log rho)'(u)`, Xi satisfies `T_Phi->pi`, `H_Phi->4pi`, and `-e^{-4u}(log Phi)''->16pi`. It also admits all positive quadratic exponential moments. The fixed-width Gaussian mixtures instead have normalized hazard/curvature tending to zero and moment radius exactly `sigma^2/2`; the hazard separation remains nonvanishing at the outer maximal-contact scale.

The atomic controls pass the all-time moment test despite failing the positive-density condition, so moment admissibility alone is not the invariant. The robust distinction is the Xi-scale double-exponential tail law, possibly together with finer theta coefficient structure.

## Program consequence

Try to propagate the tail hazard inward. Derive an exact theta identity, differential inequality, or all-time compatibility law that couples the far-tail jet to mesoscopic source mass strongly enough to exclude the folded maximal-contact controls. In parallel, attack the intuition by attempting a positive smooth all-time source with the same normalized Xi hazard but a prescribed nonzero transition gap.

## Counterevidence / boundary

XF-162 only excludes the concrete XF-160/XF-161 source families from the Xi tail class. It does not prove that every Xi-hazard source is transition-rigid, and modifications on bounded or slowly growing source regions may preserve the same asymptotic hazard. The accepted source-tail clue therefore remains open.

## Epistemic status

**Supported Xi-specific source discriminator with exact asymptotics, but no established implication from that discriminator to transition visibility or RH.**

## Falsification criterion

Construct a strictly positive smooth all-time source with the same normalized tail action/hazard/curvature limits as Xi and a prescribed maximal-contact transition gap, or prove that such a source is impossible by a source identity that does not assume the desired transition behavior.