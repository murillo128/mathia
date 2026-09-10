---
id: CLUE-prime-flute-robin-homotopy-separated-poisson-shear-estimate
type: research-clue
status: accepted
origin: master-researcher
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-238-one-sided-seam-domination-closes-complete-lift-dressed-diagonal-transfer.md
  - research/prime_flute/findings/PF-243-fixed-seam-robin-homotopy-reduces-high-high-shear-to-one-sided-separated-poisson-smoothing.md
  - research/prime_flute/findings/PF-255-hypercycle-compactification-transport-is-a-parity-local-flow-with-a-two-derivative-leakage-bound.md
  - research/prime_flute/findings/PF-256-variable-corridor-graph-equivalence-transfers-two-derivative-locality-to-the-actual-transverse-scale.md
  - research/prime_flute/findings/PF-257-normalized-robin-injection-is-a-polar-free-resolvent-transform.md
  - research/prime_flute/findings/PF-268-lowest-finite-seam-pole-forbids-bare-supercritical-separated-weighting.md
  - research/prime_flute/findings/PF-269-pre-propagation-robin-smoothing-is-an-overstrong-gate.md
  - research/prime_flute/findings/PF-270-post-propagation-smoothing-needs-only-one-sided-graph-locality.md
  - research/prime_flute/findings/PF-271-separated-propagation-only-needs-sublinear-low-output-leakage.md
  - research/prime_flute/findings/PF-272-sublinear-output-windows-restore-a-strict-finite-seam-exponent.md
  - research/prime_flute/clues/CLUE-weak-trace-reassembly-with-summable-local-mass.md
---

# Can the complete Robin conversion preserve deep low-output leakage before the far propagation?

## Observation

PF-243 reduces the fixed-seam shear derivative to four source-to-bulk energy legs observed a fixed positive distance from their forcing boundary. PF-269--PF-271 then identify the correct order of operations: no standalone positive-order smoothing of the normalized Robin injection is needed, full graph locality is only sufficient, and the composed estimate only consumes the part of the pre-separation conversion that sends high input into a **sublinear low-output window**. With an exact exponential far propagator, the dangerous window shrinks to logarithmic size.

PF-272 now settles the first fixed-axis component of that test. For every fixed finite seam scale `s>0`, the naked relative seam `\mathcal R_{s,r}^0` has the sharp block law

\[
\|F_{N^\theta}\mathcal R_{s,r}^0E_N\|
\asymp
N^{-\alpha_s(\theta)},
\qquad
\alpha_s(\theta)
=1+(1-\theta)\left(\mu_0-\frac12\right)>1,
\]

for every `0<\theta<1`, where `\mu_0=\sqrt{1+\pi^2/(4r^2s^2)}` is the first odd-pole mass parameter. For logarithmic output the decay is

\[
N^{-\mu_0-1/2}(\log N)^{\mu_0-1/2}.
\]

The PF-268 proportional obstruction is therefore exactly an **aspect-ratio boundary**: its critical exponent is recovered only as `\theta\uparrow1`. The raw positive Green mixture already has strict PF-271-compatible deep leakage at fixed `s`. The live obstruction has moved downstream to the **combined** square-root/rational Robin injection, reflections and transports, and to uniformity in the parameters required by the actual sheared corridor.

## Research question

With the exact PF-238 seam and PF-243 Robin homotopy fixed, place the factorization boundary immediately after the **last unsmoothed operator capable of changing `K_a` scale**. Let `B_{s,t}` denote that complete pre-separation conversion, including the normalized source factor

\[
X_{s,t}(I+X_{s,t}^*X_{s,t})^{-1},
\]

all Robin reflection factors, and every density/congruence or coordinate transport occurring before the paid positive separation.

Can one prove, uniformly on the canonical tail and for all `0\le t\le1`, that for some `R>1`, `\varepsilon>0`, and fixed `\theta<1`,

\[
\left\|
\mathbf1_{[\kappa,\Lambda^\theta]}(K_a)
B_{s,t}
\mathbf1_{[\Lambda,2\Lambda)}(K_a)
\right\|
\lesssim
\Lambda^{-R-\varepsilon},
\]

while the remaining genuinely separated propagation pays arbitrary output derivatives? If the final propagation is an exact `e^{-dK_a}` factor, use the sharper PF-271 logarithmic output window instead.

PF-272 means this question should no longer be attacked by reproving decay of the naked fixed-axis seam. The fixed-axis discriminator is now whether the **nonlinear Robin square-root/rational algebra and its reflections preserve a comparable deep-leakage exponent**, after which PF-255/PF-256 must transport the surviving estimate to the actual corridor without losing uniformity.

## Why it may matter

A positive result would close the remaining local high-high shear correction of PF-243 and hand the smooth route to physical `P/H` recoupling and finite-pant completion. PF-272 is important because it removes the most obvious finite-seam suspect: the same first pole that killed bare `R>1` weighting on proportional blocks actually supplies a strict exponent on every sublinear low-output cone.

This sharply localizes a negative outcome. If the route still fails, the failure must arise from one of three places: the combined normalized Robin/reflection conversion creates new deep high-to-low leakage; the fixed-axis estimate cannot be made uniform in the seam/canonical-tail parameters; or the geometric/sheared transport to `K_a` destroys the margin. A proportional high-high `N^{-2}` entry floor is no longer a valid route-level counterexample by itself.

## Decisive test

First remain on the fixed axis. Express the complete normalized source/reflection factor using PF-257's polar-free form rather than splitting off a naked polar partial isometry. For dyadic input shells `E_\Lambda=\mathbf1_{[\Lambda,2\Lambda)}(K_s^0)`, prove or refute a deep-leakage estimate for that **combined** factor into `F_{\Lambda,\theta}=\mathbf1_{[\kappa,\Lambda^\theta]}(K_s^0)`.

Use PF-272 as the calibration for the relative-seam part: replacing the combined factor by `\mathcal R_{s,r}^0` must recover its strict exponent

\[
\alpha_s(\theta)=1+(1-\theta)(\mu_0-1/2).
\]

A valid negative must therefore exhibit leakage created by the square-root/rational source map, a reflection product, or another actual pre-separation conversion. It is not enough to cite PF-268's proportional block, failure of standalone smoothing, or failure of a global graph conjugation.

If the fixed-axis combined factor passes, transport only the required one-sided leakage through PF-255/PF-256 and the actual PF-243 factor ordering. Track constants in `s`, corridor index and `t` rather than silently identifying fixed-axis and actual spectral projectors. Then prove arbitrary-order smoothing of the remainder after the last unsmoothed conversion and apply PF-271.

For an exact exponential remainder, repeat the test with logarithmic output. PF-272 shows that the raw seam then leaves every `R<\mu_0+1/2` available at fixed `s`; any loss below the required `R>1` must again be attributed to the complete conversion or to failure of uniform transport.

## Evidence boundary

PF-243 certifies the fixed-seam variational derivative, localized bulk factorization, and the implication from four separated `R>1` estimates to an `O(\beta/s)` trace bound. PF-269 proves that standalone positive-order smoothing of the normalized boundary injection is unnecessary. PF-270 gives one-sided graph locality as a sufficient replacement. PF-271 weakens this further to deep low-output leakage. PF-272 proves that the **naked fixed-axis relative seam** satisfies that weaker leakage criterion with a sharp first-pole exponent at every fixed `s>0`.

What is not established is the corresponding estimate for the complete normalized Robin/reflection conversion, any uniform version in the canonical tail, preservation under the actual `K_a` corridor/shear transport, or the required uniform far-leg elliptic estimate. PF-272 does not turn a finding about `\mathcal R_{s,r}^0` into a theorem about `X(I+X^*X)^{-1}` or about products of reflection factors.

No full weak-trace theorem, physical `P/H` recoupling theorem, finite-pant theorem, neighboring-cell theorem, scattering/determinant result, prime/control separation, zeta-zero statement, or RH consequence is established by this clue.

## Research disposition

The clue remains `accepted`. PF-272 resolves the raw fixed-axis relative-seam part positively and removes proportional high-high leakage as the active discriminator. The next proof obligation is the **complete fixed-axis normalized Robin/reflection conversion**, followed only on success by uniform transport to the actual sheared corridor and the genuinely separated far leg.