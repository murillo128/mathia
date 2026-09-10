---
id: CLUE-prime-flute-robin-homotopy-separated-poisson-shear-estimate
type: research-clue
status: accepted
origin: master-researcher
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-238-one-sided-seam-domination-closes-complete-lift-dressed-diagonal-transfer.md
  - research/prime_flute/findings/PF-243-fixed-seam-robin-homotopy-reduces-high-high-shear-to-one-sided-separated-poisson-smoothing.md
  - research/prime_flute/findings/PF-254-normalized-noncommuting-robin-injection-splits-square-root-amplitude-from-polar-transport.md
  - research/prime_flute/findings/PF-255-hypercycle-compactification-transport-is-a-parity-local-flow-with-a-two-derivative-leakage-bound.md
  - research/prime_flute/findings/PF-256-variable-corridor-graph-equivalence-transfers-two-derivative-locality-to-the-actual-transverse-scale.md
  - research/prime_flute/findings/PF-257-normalized-robin-injection-is-a-polar-free-resolvent-transform.md
  - research/prime_flute/findings/PF-268-lowest-finite-seam-pole-forbids-bare-supercritical-separated-weighting.md
  - research/prime_flute/findings/PF-269-pre-propagation-robin-smoothing-is-an-overstrong-gate.md
  - research/prime_flute/findings/PF-270-post-propagation-smoothing-needs-only-one-sided-graph-locality.md
  - research/prime_flute/findings/PF-271-separated-propagation-only-needs-sublinear-low-output-leakage.md
  - research/prime_flute/findings/PF-272-sublinear-output-windows-restore-a-strict-finite-seam-exponent.md
  - research/prime_flute/findings/PF-273-seam-square-root-is-a-complete-bernstein-green-continuum-with-mass-one-edge.md
  - research/prime_flute/findings/PF-274-fixed-axis-massive-jacobi-chain-is-a-squared-continuous-hahn-operator.md
  - research/prime_flute/findings/PF-275-mass-one-continuum-forbids-supercritical-raw-source-fixed-row-leakage.md
  - research/prime_flute/findings/PF-276-robin-normalization-is-inverse-positive-and-cannot-zero-the-fixed-axis-threshold-moment.md
  - research/prime_flute/clues/CLUE-weak-trace-reassembly-with-summable-local-mass.md
---

# Can normalized Robin injection suppress the mass-one square-root continuum before far propagation?

## Observation

PF-243 reduces the fixed-seam shear derivative to source-to-bulk energy legs observed a fixed positive distance from their forcing boundary. PF-269--PF-271 identify the correct order of operations: full pre-propagation smoothing is too strong, and the composed argument only needs control of the conversion that sends high input into a **sublinear low-output window**. With an exact exponential far propagator the dangerous output window shrinks to logarithmic size.

PF-272 settles the naked fixed-axis relative seam positively. Its odd discrete Green ladder has a lowest mass

\[
\mu_0=\sqrt{1+\pi^2/(4r^2s^2)}>1,
\]

and therefore a strict deep-block exponent for every fixed `0<\theta<1`. PF-273 then shows why that exponent is not inherited by the square-root source: if

\[
X_w=s^{-1/2}A^{-1/4}g_w(L),
\qquad
\mathcal R^0_{s,r}=X_wX_w^*,
\qquad
w=rs,
\]

then `g_w` is a complete Bernstein function whose positive resolvent measure reaches `t=0`, equivalently the Green threshold `\mu(t)=\sqrt{1+t}\downarrow1`.

PF-275 turns that structural edge into an exact leakage obstruction without requiring a shrinking-mass asymptotic. For every fixed low parity row `P_i` and every `q>1`,

\[
N^q\|P_iX_wE_N\|\to\infty.
\]

Thus the raw square-root source already fails every supercritical PF-271 exponent even on a fixed output row. PF-257 identifies the actual fixed-axis injection as

\[
B_w=(I+\mathcal R^0_{s,r})^{-1}X_w.
\]

PF-276 now removes the simplest possible normalization escape. In each parity chain `\mathcal R^0_{s,r}` is a positive operator with strictly negative off-diagonal corridor matrix entries, so `(I+\mathcal R^0_{s,r})^{-1}` is positivity preserving and its basis columns are strictly positive. Combining this with PF-251's exact generalized zero mode gives an exact conserved weighted mass for the normalized column. For

\[
z_i:=A^{-1/4}(I+\mathcal R^0_{s,r})^{-1}f_i,
\]

the zero-mode moment is finite and strictly nonzero; PF-274 identifies the corresponding absolutely convergent corridor-coefficient functional with nonzero values at both nearest branch points `\xi=\pm i`, up to the fixed odd-parity sign.

Therefore the normalization cannot gain its missing exponent by manufacturing an **exact threshold zero through coefficient cancellation**. The remaining fixed-axis question is whether that nonzero threshold functional really controls the large-mode coefficient of `g_w(L)z_i` with the expected mass-one power, or whether some subtler analytic mechanism invalidates the naive branch-to-coefficient transfer.

## Research question

Can the complete fixed-axis normalized source

\[
B_w=(I+\mathcal R^0_{s,r})^{-1}X_w
\]

suppress the mass-one edge strongly enough that, for some fixed `\theta<1`, `R>1`, and `\varepsilon>0`,

\[
\left\|F_{\Lambda,\theta}B_wE_\Lambda\right\|
\lesssim\Lambda^{-R-\varepsilon},
\tag{1}
\]

uniformly in the fixed-axis parameter range needed by the canonical tail? If the following separated propagation is exactly `e^{-dK}`, use PF-271's logarithmic output window.

The possible mechanism is now narrower than before PF-276. PF-275 proves that `X_w` has no hidden strict exponent to preserve, and PF-276 proves that the normalized source vector does not acquire an exact zero in the natural mass-one threshold coefficient functional. Any surviving strict exponent must therefore come from a more subtle analytic cancellation in the continuous-Hahn coefficient asymptotics, not from ordinary sign cancellation of the normalized corridor coefficients.

If the fixed-axis normalized source passes, only then transport the one-sided leakage estimate through PF-255/PF-256 to the actual corridor and use PF-254/PF-270 to keep reflection conversion on the propagated side of the factorization.

## Why it may matter

A positive answer to (1) would identify a genuinely nontrivial Robin mechanism: despite a nonzero mass-one threshold moment, the full continuous-Hahn asymptotic would have to suppress the dangerous high-to-low channel by some structure not visible in the raw source or in coefficientwise positivity. The remaining work would then become geometric/uniform — transfer to the actual `K_a` corridor, control canonical-tail and homotopy constants, and pay later reflection/output derivatives with positive separation.

A negative answer is now especially plausible and equally decisive. PF-275 supplies the raw mass-one obstruction, while PF-276 shows that the Robin inverse cannot eliminate the natural threshold moment by sign cancellation. If the nonzero moment is the leading Darboux/Green coefficient, the PF-271 route fails before sheared-coordinate, hypercycle-transport, or global reassembly issues enter.

## Decisive test

Work with a fixed output parity mode `f_i`. The normalized row has the exact adjoint form

\[
B_w^*f_i
=s^{-1/2}g_w(L)z_i,
\qquad
z_i:=A^{-1/4}(I+\mathcal R^0_{s,r})^{-1}f_i.
\tag{2}
\]

PF-276 proves that the absolutely convergent PF-274 threshold coefficient functional of `z_i` at `\xi=\pm i` is nonzero. The decisive task is therefore to establish, or refute, the analytic bridge from that nonzero functional to the large-degree continuous-Hahn coefficients of `g_w(L)z_i`.

Use PF-274's exact equal-parameter continuous-Hahn representation to prove a local analytic-continuation and Darboux/contour theorem around `\xi=\pm i`, or an equivalent Green/Tauberian statement, strong enough to determine the fixed-row leakage exponent. The useful outcomes are now:

- **threshold transfer:** show that PF-276's nonzero coefficient functional produces a nonzero mass-one leading term, or at least a PF-275-style lower bound forbidding every fixed-row exponent `q>1`; this negatively resolves the fixed-axis PF-271 route;
- **transfer failure:** prove that the nonzero threshold functional does not control the large-degree coefficient and identify the exact analytic reason. Any surviving strict exponent must then be traced to that mechanism rather than described as a threshold zero.

Do not return to PF-268's proportional block, reprove PF-272's naked-seam estimate, or derive a sharper raw-`X_w` asymptotic unless it is needed inside the normalized branch-to-coefficient theorem. Do not split off a polar partial isometry.

If the fixed-axis test passes, carry only the required one-sided leakage through PF-255/PF-256 and the exact PF-254 factor ordering. Track `s`, corridor index, and homotopy parameter explicitly rather than identifying fixed-axis and actual spectral projectors. Reflection cycles already containing positive longitudinal propagation belong to the paid side of the decomposition.

## Evidence boundary

PF-243 certifies the fixed-seam variational derivative and the implication from separated source-to-bulk estimates to the local trace bound. PF-269--PF-271 reduce the necessary pre-propagation requirement to deep low-output leakage. PF-272 proves the naked fixed-axis relative seam has a strict sublinear exponent at every fixed finite seam scale. PF-273 proves that the square-root factor entering `X_w` is instead a positive complete-Bernstein Green continuum with support reaching the mass-one edge. PF-274 gives the exact continuous-Hahn spectral representation. PF-275 proves that the **raw source `X_w` itself fails every exponent `q>1` already on a fixed output row**. PF-276 proves that the Robin-normalized source column retains a finite strictly positive generalized zero-mode moment and a nonzero corridor-coefficient functional at `\xi=\pm i`; exact threshold cancellation by coefficient signs is therefore excluded.

What is not established is the Darboux/contour or Green theorem converting that nonzero threshold functional into a sharp large-mode asymptotic for `g_w(L)z_i`, any corresponding obstruction or positive estimate for `B_w`, uniformity in the canonical corridor parameters, preservation under actual `K_a` transport, or the final uniform far-leg elliptic estimate. PF-276 does not claim that a nonzero branch-point coefficient functional automatically determines continuous-Hahn coefficient asymptotics.

No full weak-trace theorem, physical `P/H` recoupling theorem, finite-pant theorem, neighboring-cell theorem, scattering/determinant result, prime/control separation, zeta-zero statement, or RH consequence is established by this clue.

## Research disposition

The clue remains `accepted`, but its fixed-axis escape route is narrower. PF-275 removes raw square-root smoothing as a source of supercritical margin, and PF-276 removes an exact threshold zero generated by the noncommuting Robin inverse. The next discriminator is solely the analytic branch-to-coefficient transfer for `g_w(L)z_i`: if the nonzero PF-276 threshold functional survives as the mass-one leading term, the PF-271 route closes; if it does not, the failure mechanism must be identified explicitly before any positive smoothing claim is made.