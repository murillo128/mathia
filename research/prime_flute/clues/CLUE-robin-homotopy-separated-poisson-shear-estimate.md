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

The proof chooses, after `q` is specified, one sufficiently small **fixed** positive mass slice from PF-273's continuum and uses Green positivity plus PF-262's fixed-source tail. Thus the raw square-root source already fails every supercritical PF-271 exponent, even on a fixed output row. A sharper `t\log N=O(1)` asymptotic may still determine the exact critical law, but it is no longer needed to decide whether `X_w` itself has an `R>1` margin.

PF-257 identifies the actual fixed-axis injection as

\[
B_w=(I+\mathcal R^0_{s,r})^{-1}X_w.
\]

Therefore the **entire** possible supercritical gain must now come from the noncommuting rational normalization. PF-274 supplies an exact continuous-Hahn transform for the underlying fixed-axis functional calculus, so the remaining question can be posed as a threshold-cancellation problem rather than as generic operator smoothing.

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

The key discriminator is now sharper than in PF-273. It is not enough for `(I+\mathcal R^0_{s,r})^{-1}` to be bounded, positive, or mildly local: PF-275 proves that `X_w` has no hidden strict exponent to preserve. The normalization must specifically remove or cancel the threshold contribution responsible for the fixed-row `q\downarrow1` obstruction.

If the fixed-axis normalized source passes, only then transport the one-sided leakage estimate through PF-255/PF-256 to the actual corridor and use PF-254/PF-270 to keep reflection conversion on the propagated side of the factorization.

## Why it may matter

A positive answer to (1) would identify a genuinely nontrivial Robin mechanism: the nonlinear normalization would create spectral locality that is absent from the raw square-root Dirichlet-to-Neumann source. The remaining work would then become geometric/uniform — transfer to the actual `K_a` corridor, control canonical-tail and homotopy constants, and pay later reflection/output derivatives with positive separation.

A negative answer is equally decisive. PF-275 shows that the mass-one continuum is not merely suggestive; it already produces an exact fixed-row obstruction for `X_w`. If one nonzero threshold coefficient survives the normalization, the PF-271 route fails before sheared-coordinate, hypercycle-transport, or global reassembly issues enter.

## Decisive test

Work with a fixed output parity mode `f_i`. The normalized row has the exact adjoint form

\[
B_w^*f_i
=s^{-1/2}g_w(L)z_i,
\qquad
z_i:=A^{-1/4}(I+\mathcal R^0_{s,r})^{-1}f_i.
\tag{2}
\]

Use PF-274's continuous-Hahn representation, or an equivalent Green formulation, to identify the coefficient of the nearest `\xi=\pm i` / `\mu=1` threshold contribution for the special vector `z_i`. PF-275 shows that the corresponding coefficient is nonzero for an unnormalized basis row; the question is whether the Robin-normalized `z_i` acquires an exact zero or sufficient vanishing at that threshold.

There are two decisive outcomes:

- **survival:** prove that the threshold coefficient is nonzero for at least one fixed row. Then a PF-275-type fixed-mass-slice lower bound should propagate through the normalization and forbid every PF-271-compatible `R>1` estimate;
- **cancellation:** prove that the normalized source vector has a threshold zero of sufficient order, and convert that zero into a strict high-to-low block exponent on one PF-271 window.

Do not first spend effort deriving a sharp raw-`X_w` boundary-layer asymptotic merely to test supercritical smoothing; PF-275 has already ruled that out. Such an asymptotic is useful only if it is needed to quantify the normalized cancellation. Do not return to PF-268's proportional block or reprove PF-272's naked-seam estimate, and do not split off a polar partial isometry.

If the fixed-axis test passes, carry only the required one-sided leakage through PF-255/PF-256 and the exact PF-254 factor ordering. Track `s`, corridor index, and homotopy parameter explicitly rather than identifying fixed-axis and actual spectral projectors. Reflection cycles already containing positive longitudinal propagation belong to the paid side of the decomposition.

## Evidence boundary

PF-243 certifies the fixed-seam variational derivative and the implication from separated source-to-bulk estimates to the local trace bound. PF-269--PF-271 reduce the necessary pre-propagation requirement to deep low-output leakage. PF-272 proves the naked fixed-axis relative seam has a strict sublinear exponent at every fixed finite seam scale. PF-273 proves that the square-root factor entering `X_w` is instead a positive complete-Bernstein Green continuum with support reaching the mass-one edge. PF-274 gives the exact continuous-Hahn spectral representation. PF-275 proves that the **raw source `X_w` itself fails every exponent `q>1` already on a fixed output row**.

What is not established is any corresponding obstruction or positive estimate for `B_w`, any theorem forcing or excluding a threshold zero for `z_i`, uniformity in the canonical corridor parameters, preservation under actual `K_a` transport, or the final uniform far-leg elliptic estimate. PF-275 does not prove a sharp `N^{-1}` asymptotic and does not claim that the noncommuting normalization is incapable of cancellation.

No full weak-trace theorem, physical `P/H` recoupling theorem, finite-pant theorem, neighboring-cell theorem, scattering/determinant result, prime/control separation, zeta-zero statement, or RH consequence is established by this clue.

## Research disposition

The clue remains `accepted`, with a narrower and more falsifiable fixed-axis target. PF-275 removes raw square-root smoothing as a possible source of the required margin. The next discriminator is whether `(I+\mathcal R^0_{s,r})^{-1}` creates an exact threshold cancellation in the special normalized source vector (2); without such a mechanism, the mass-one fixed-row obstruction survives and the PF-271 route closes.