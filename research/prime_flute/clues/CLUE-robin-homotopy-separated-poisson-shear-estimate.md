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
  - research/prime_flute/clues/CLUE-weak-trace-reassembly-with-summable-local-mass.md
---

# Can normalized Robin injection suppress the mass-one square-root continuum before far propagation?

## Observation

PF-243 reduces the fixed-seam shear derivative to source-to-bulk energy legs observed a fixed positive distance from their forcing boundary. PF-269--PF-271 identify the correct order of operations: full pre-propagation smoothing is too strong, and the composed argument only needs control of the conversion that sends high input into a **sublinear low-output window**. With an exact exponential far propagator the dangerous output window shrinks to logarithmic size.

PF-272 settles the naked fixed-axis relative seam positively. Its odd discrete Green ladder has a lowest mass

\[
\mu_0=\sqrt{1+\pi^2/(4r^2s^2)}>1,
\]

and therefore a strict deep-block exponent for every fixed `0<\theta<1`:

\[
\|F_{N^\theta}\mathcal R^0_{s,r}E_N\|
\asymp
N^{-\alpha_s(\theta)},
\qquad
\alpha_s(\theta)=1+(1-\theta)(\mu_0-1/2)>1.
\]

PF-273 now shows why that exponent is **not** the right calibration for the square-root source. Writing `w=rs`,

\[
Q_w^{1/2}=g_w(L),
\qquad
g_w(\lambda)=\sqrt{\sqrt\lambda\tanh(w\sqrt\lambda)},
\]

`g_w` is a complete Bernstein function whose exact positive resolvent measure is absolutely continuous and reaches `t=0`; in the PF-264 Green variable `\mu(t)=\sqrt{1+t}`, the square-root continuum therefore reaches `\mu=1`. The raw seam's first-pole gap has been closed by the square root itself.

At the same time, PF-273 makes the remaining fixed-axis object more concrete. If

\[
X_w=s^{-1/2}A^{-1/4}g_w(L),
\qquad
\mathcal R^0_{s,r}=X_wX_w^*,
\]

then PF-257's polar-free normalized injection is exactly

\[
B_w=(I+\mathcal R^0_{s,r})^{-1}X_w.
\]

PF-254 also places every nontrivial reflection cycle behind positive longitudinal propagation. Thus the first unsmoothed fixed-axis discriminator is `B_w` itself; reflection cycles should not be bundled into an artificial pre-propagation obstruction when their scale conversion is already propagation-dressed.

## Research question

Can the **complete fixed-axis normalized source**

\[
B_w=(I+\mathcal R^0_{s,r})^{-1}X_w
\]

suppress the mass-one edge of `X_w` strongly enough that, for some fixed `\theta<1`, `R>1`, and `\varepsilon>0`,

\[
\left\|
F_{\Lambda,\theta}
B_w
E_\Lambda
\right\|
\lesssim
\Lambda^{-R-\varepsilon},
\tag{1}
\]

uniformly in the fixed-axis parameter range needed by the canonical tail? Here `E_\Lambda` is the high input shell for `K_s^0` and `F_{\Lambda,\theta}` is the PF-271 sublinear low-output projector. If the following separated propagation is exactly `e^{-dK}`, use PF-271's sharper logarithmic output window.

The central issue is no longer whether the raw seam has a strict first-pole exponent: PF-272 proves that it does. Nor is it whether the square-root source is an arbitrary polar mixer: PF-273 replaces it by a sign-coherent continuum of massive axis Green resolvents. The unresolved question is whether the **noncommuting rational normalization** `(I+\mathcal R^0_{s,r})^{-1}` removes enough of the continuum touching `\mu=1` to recover the strict margin required by PF-271.

If the fixed-axis normalized source passes, only then transport the one-sided leakage estimate through PF-255/PF-256 to the actual corridor and use PF-254/PF-270 to keep reflection conversion on the propagated side of the factorization.

## Why it may matter

A positive answer to (1) would close the last genuinely unsmoothed fixed-axis scale-conversion gate in the PF-243 high-high shear route. The remaining work would become geometric/uniform: transfer the estimate to the actual `K_a` corridor, keep constants uniform in the canonical tail and Robin homotopy, and pay later reflection/output derivatives with the positive separation already present in the exact factor ordering.

A negative answer would also be decisive. PF-273 identifies a specific candidate obstruction rather than a generic failure of smoothing: the square-root Dirichlet-to-Neumann factor replaces PF-272's discrete mass gap by a continuum down to `\mu=1`. If that contribution survives `(I+\mathcal R^0_{s,r})^{-1}` with a stable lower bound, then the normalized source itself blocks the PF-271 route before any sheared-coordinate or hypercycle transport issue enters.

## Decisive test

Remain on the fixed axis and use PF-273's exact Stieltjes decomposition of `X_w`. Split its positive Green continuum into a small-mass sector and its complement. Near the lower edge,

\[
t\,d\nu_w(t)
\sim
\frac{\sqrt w}{\pi}t^{1/2}\,dt,
\]

while PF-264's fixed-mass Green law has `\mu(t)=\sqrt{1+t}`. The natural boundary layer is therefore `t\log(j/i)=O(1)`. First prove a small-mass Green estimate uniform enough to control that layer; do not integrate PF-264's fixed-`t` asymptotic without such uniformity.

Then estimate the same high-to-low block after left multiplication by `(I+\mathcal R^0_{s,r})^{-1}`. There are two genuinely decisive outcomes:

- prove that the rational normalization converts the mass-one continuum into a strict `R>1` block on at least one sublinear output window (or on the logarithmic window for exact exponential propagation); or
- prove a sign/size-stable lower bound showing that a mass-one contribution survives normalization strongly enough to forbid every PF-271-compatible `R>1` estimate.

Do not return to PF-268's proportional block or reprove PF-272's naked-seam estimate: neither decides this question. Do not split off a polar partial isometry: PF-257 and PF-273 give the combined scalar/Green structure needed to attack the actual normalized source.

If the fixed-axis test passes, carry only the required one-sided leakage through PF-255/PF-256 and the exact PF-254 factor ordering. Track `s`, corridor index, and homotopy parameter explicitly rather than identifying fixed-axis and actual spectral projectors. Reflection cycles already containing positive longitudinal propagation belong to the paid side of the decomposition.

## Evidence boundary

PF-243 certifies the fixed-seam variational derivative and the implication from separated source-to-bulk estimates to the local trace bound. PF-269--PF-271 reduce the necessary pre-propagation requirement to deep low-output leakage. PF-272 proves the **naked fixed-axis relative seam** has a strict sublinear exponent at every fixed finite seam scale. PF-273 proves that the square-root factor entering `X_w` is instead a positive complete-Bernstein Green continuum with support reaching the mass-one edge, and identifies the exact polar-free normalized source `B_w=(I+\mathcal R^0_{s,r})^{-1}X_w`.

What is not established is a sharp small-mass two-index asymptotic uniform in the shrinking boundary layer, the block estimate (1) for `B_w`, any obstruction theorem showing that (1) fails, uniformity in the canonical corridor parameters, preservation under actual `K_a` transport, or the final uniform far-leg elliptic estimate. The mass-one edge is an exact structural fact about the square-root representation; it is **not** by itself a proof of critical leakage for the normalized source.

No full weak-trace theorem, physical `P/H` recoupling theorem, finite-pant theorem, neighboring-cell theorem, scattering/determinant result, prime/control separation, zeta-zero statement, or RH consequence is established by this clue.

## Research disposition

The clue remains `accepted`, but its fixed-axis target is materially narrower. PF-272 removes the naked relative seam as the obstruction; PF-273 shows that the square-root source loses the same first-pole mass gap; and PF-254 places reflection cycles after positive propagation. The next discriminator is therefore the **complete polar-free normalized source** `(I+\mathcal R^0_{s,r})^{-1}X_w` acting on the mass-one Green continuum.