# MI-031 — Wang transfer admits moving tests only within a seminorm budget that excludes fixed physical prime windows

**Evidence level:** literature-backed/exact synthesis from [VIS-265](../../findings/VIS-265-wang-short-interval-support-law-blocks-bounded-window-edge-transfer.md) through [VIS-273](../../findings/VIS-273-wang-fixed-q-pullbacks-hit-derivative-budget.md). The proof-interface obstruction is exact for the audited Wang estimate; it is not a theorem that the underlying asymptotic is false beyond that interface.

Wang's short-interval pair-correlation proof does allow `T`-dependent tests when Fourier support stays inside a fixed margin and the test seminorms grow slowly enough. With `L=log T`, the normalized error contains the term

`||g_T'||_inf / L`

along with lower-order support and amplitude terms. For a smooth normalized moment packet of width `b`, the unavoidable derivative growth is `b^(-(2m+2))`, giving the familiar sufficient shrinking-window gate `L b^(2m+2) -> infinity`.

VIS-271--VIS-272 identify the exact source-coordinate pullback. In the physical logarithmic prime coordinate `q=log x/(2pi)`, Wang's diagonal field is a Green potential of the same weighted prime-power measure that appears in Rodgers. A literal fixed prime therefore corresponds in Wang's variable to a center and width of order `1/L`, not to a fixed positive `alpha` band.

VIS-273 inserts that exact pullback into the audited theorem interface. Any nontrivial fixed-width packet in the physical `q` coordinate becomes a Wang test with `alpha` width `Theta(1/L)`. Rescaling a fixed profile to that width forces

`||g_T'||_inf = Theta(L)`,

so the derivative contribution `||g_T'||_inf/L` is only `Theta(1)`, not `o(1)`. Damping the packet amplitude and renormalizing the extracted statistic does not change this relative obstruction.

The reusable lesson is that **an exact representation dictionary does not imply theorem transfer at the pulled-back source scale**. The physical coordinate map can move a fixed source window exactly onto the boundary of the proof's seminorm budget. Here the obstruction is not support access or packet design; it is the stability of the asymptotic theorem under a derivative cost forced by the coordinate change itself.

A successful continuation therefore needs a genuinely stronger theorem interface: improved dependence on `||g'||`, a structure-sensitive integrated identity that pairs directly with the Green kernel/adjoint, or another estimate that controls the fixed-`q` functional without differentiating an uncontrolled remainder.

**Boundary.** VIS-273 does not prove that Wang's pair-correlation asymptotic fails for `1/L`-scale moving tests. It proves that the currently audited bound does not make the error vanish there. It also does not extend the support edge, supply four-level covariance, or establish a source-sensitive residual. The next step is theorem-level, not another coordinate transform.