---
id: CLUE-prime-flute-relative-seam-intrinsic-six-fractional-window
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-253-bessel-four-jacobi-fractional-powers-have-sharp-separated-window.md
  - research/prime_flute/findings/PF-257-normalized-robin-injection-is-a-polar-free-resolvent-transform.md
  - research/prime_flute/findings/PF-258-thin-seam-relative-edge-is-a-linearly-weighted-jacobi-tangent-with-intrinsic-dimension-six.md
  - research/prime_flute/findings/PF-259-intrinsic-six-tangent-has-anchored-gaussian-large-time-control.md
  - research/prime_flute/findings/PF-260-davies-gaffney-closes-short-time-intrinsic-six-fractional-window.md
  - research/prime_flute/findings/PF-261-finite-seam-crossover-is-a-bounded-positive-mixture-of-massive-axis-resolvents.md
  - research/prime_flute/findings/PF-262-massive-jacobi-resolvents-have-exact-double-root-indicial-law.md
  - research/prime_flute/findings/PF-263-resonant-mass-green-tail-keeps-the-pure-recessive-power.md
  - research/prime_flute/findings/PF-264-fixed-mass-green-kernel-has-universal-two-index-leading-law.md
  - research/prime_flute/clues/CLUE-critical-jacobi-square-root-decay-window.md
---

# Does the intrinsic-six thin-seam margin survive the exact finite-seam crossover?

## Observation

PF-258 corrects the fixed-axis bridge between PF-253 and PF-257. In the canonical thin-seam scaling `w=rs`, the dimensionless positive relative seam tends to

\[
H=A^{-1/4}LA^{-1/4}=A^{1/4}JA^{1/4},
\]

not to the bounded Bessel-four operator `J`. PF-259 and PF-260 prove that this intrinsic-six tangent nevertheless retains the full fixed-axis upper fractional window

\[
|\langle e_i,H^\sigma e_j\rangle|
\lesssim
(i+1)(j+1)^{-2-\sigma}
\qquad(j\ge2i+2),
\]

so at `\sigma=1/2` every strict `1<R<2` survives. The fixed-axis tangent is therefore no longer the route-admission obstruction.

PF-261 removes two further ambiguities at finite seam scale. For every `s>0`, the exact fixed-axis relative seam

\[
\mathcal R_{s,r}^0
=s^{-1}A^{-1/4}f_{rs}(L)A^{-1/4},
\qquad
f_w(\lambda)=\sqrt\lambda\tanh(w\sqrt\lambda),
\]

is a bounded positive operator, the relative square-root map closes on the untruncated fixed-axis complete lift, and PF-257's combined Robin transform is therefore well-defined there without Galerkin truncation. More importantly, the entire nonlinear `rs\sqrt L\asymp1` crossover is an exact positive partial-fraction mixture of massive resolvents `(L+a_k^2)^{-1}` with

\[
a_k=\frac{(2k+1)\pi}{2rs}.
\]

For off-diagonal Gegenbauer matrix elements, the identity terms cancel and the crossover is exactly a weighted sum of those massive Green matrices. Since `L=U(1-\partial_\tau^2)U^*`, each term has the explicit complete-axis kernel `e^{-\sqrt{1+a_k^2}|\tau-\sigma|}/(2\sqrt{1+a_k^2})`.

PF-262--PF-264 now identify the fixed-mass mode geometry behind that Green sum. PF-262 derives the double-root indicial exponents `-1/2\pm\mu`, `\mu=\sqrt{1+a^2}`. PF-263 removes the integer-difference caveat: at resonant masses the logarithm belongs only to the discarded dominant solution, so the `\ell^2` Green tail keeps the pure recessive power. PF-264 then lets the source index enter the tail and uses the exact Jacobi Wronskian to cancel the unknown left connection coefficient. For every fixed mass,

\[
\langle e_{2i+\varepsilon},(L+a^2)^{-1}e_{2j+\varepsilon}\rangle
\sim
\frac{1}{2\mu\sqrt{ij}}
\left(\frac{i}{j}\right)^\mu,
\qquad i\le j\to\infty.
\]

After PF-261's outer `A^{-1/4}` weights, one fixed mass therefore has leading separated profile proportional to `j^{-2}(i/j)^{\mu-1}`. The formerly vague source-connection problem has narrowed to **uniformity of this two-index law as the mass moves with the seam scale and the mode indices**.

## Research question

Does the **full odd-mass Green sum** supplied by PF-261 preserve some uniform separated high-to-low exponent `R>1` after the endpoint weights and the combined bounded Robin transform are included, uniformly through the crossover `rs\sqrt L\asymp1`?

The question is deliberately stronger than proving decay for one fixed mass, one fixed output row, one fixed `s`, or the tangent alone. PF-262--PF-264 settle those fixed-mass asymptotic mechanisms far enough that the active issue is now the coupled parameter regime: can the two-index Green law be made uniform as `a=a_k` moves relative to `i` and `j`, strongly enough to sum the entire odd mass ladder?

## Why it may matter

PF-259/PF-260 show that the correctly normalized tangent has enough margin, while PF-261 shows that finite seam scale is not an uncontrolled perturbation: it is a concrete massive-resolvent family with an exact complete-axis Green representation. PF-264 adds a favorable structural signal: on a separated cone the fixed-mass leading term gains the ratio damping `(i/j)^{\mu-1}`, so larger mass should become easier rather than harder **if** the asymptotic constants can be controlled uniformly.

A positive uniform estimate would remove the last specifically **fixed-axis finite-`s`** obstruction and justify spending the remaining `1<R<2` margin on PF-256's actual-corridor transport and PF-243's Robin--Poisson factorization. A negative estimate would be equally decisive: if a transition regime in `a/i` destroys every strict `R>1` despite the fixed-mass law, the present Jacobi/Robin route fails before the more expensive actual-corridor and global reassembly stages.

## Decisive test

Start from PF-261's exact off-diagonal identity

\[
\langle e_i,\mathcal R_{s,r}^0e_j\rangle
=-\frac{2}{rs^2\sqrt{\kappa_i\kappa_j}}
\sum_{k\ge0}a_k^2
\langle e_i,(L+a_k^2)^{-1}e_j\rangle,
\qquad i\ne j,
\]

inside one parity sector. Use PF-264's universal fixed-mass Wronskian law as the target asymptotic and prove or refute a **parameter-uniform** Green estimate on a separated cone such as `j\ge2i+2`. Split the coupled region by the relative size of `a`, `i`, and `j` if necessary; for example `a\lesssim i`, `i\lesssim a\lesssim j`, and `a\gtrsim j`. A useful target is any estimate retaining a fixed positive fraction of the ratio exponent,

\[
|G_{ij}^{(\varepsilon)}(a)|
\lesssim
\frac{1}{\mu\sqrt{ij}}
\left(\frac{i+1}{j+1}\right)^{c\mu}
\]

with `c>0` and constants uniform in the canonical tail.

Then sum the actual odd masses `a_k=(2k+1)\pi/(2rs)` **before** taking the weighted operator norm. PF-264's factor `(i/j)^{\mu-1}` indicates exponential-in-mass damping on a strict separated cone, but its current `O_a` error cannot be interchanged with the infinite mass sum. The decisive issue is therefore a uniform theorem, not another pointwise asymptotic or a separate analysis of resonant masses.

If the relative-seam estimate survives, propagate it through the **combined** bounded source map

\[
B_{s,r}^0=X_{s,r}^0(I+(X_{s,r}^0)^*X_{s,r}^0)^{-1}
\]

rather than separating a naked polar partial isometry. Only after this fixed-axis test succeeds should the surviving margin be transferred through PF-256's actual `K_a` basis, PF-255's hypercycle transport, reflection factors, and PF-243's separated Robin--Poisson factorization.

Kill the route if the uniform two-index Green estimate fails in a transition regime strongly enough that the exact finite-`s` mass sum or the combined Robin map destroys every strict `R>1` weight in the canonical tail.

## Evidence boundary

PF-258 establishes the intrinsic-six thin-seam tangent. PF-259/PF-260 establish its full fixed-axis **upper** fractional window. PF-261 establishes finite-`s` boundedness, fixed-axis complete-lift closure of the relative square-root/Robin algebra, the positive odd-pole resolvent expansion, and the exact complete-axis Green representation of every massive resolvent term.

PF-262 gives the fixed-source indicial powers; PF-263 proves that resonant masses retain the same pure recessive Green exponent; PF-264 proves the universal two-index **fixed-mass** leading law and cancellation of the left connection coefficient. None of these findings makes the error term uniform as `a`, `i`, and `j` move together, and therefore none justifies summing PF-261's infinite odd-mass family under the required weighted norm.

Nor has any result transferred a finite-`s` bound to the actual `K_a` corridor, hypercycle compactification, PF-243 Robin--Poisson map, trace-class shear block, finite-pant completion, or global weak-`S_1` reassembly. Nothing here proves a scattering/determinant identity, a zeta-zero statement, or RH.

## Research disposition

Accepted. The fixed-axis tangent stage and the fixed-mass Green asymptotic mechanism are now structurally understood. Resonant masses are not exceptional, and the moving-source connection coefficient cancels at leading order. The active discriminator is **parameter-uniform two-index control across the coupled mass/mode regimes, followed by the full odd-mass sum and the combined Robin transform**. Further fixed-mass asymptotics are secondary unless they supply the uniformity needed for that test.