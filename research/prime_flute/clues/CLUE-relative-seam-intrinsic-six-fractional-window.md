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

PF-261 now removes two further ambiguities at finite seam scale. For every `s>0`, the exact fixed-axis relative seam

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

## Research question

Does the **full odd-mass Green sum** supplied by PF-261 preserve some uniform separated high-to-low exponent `R>1` after the endpoint weights and the combined bounded Robin transform are included, uniformly through the crossover `rs\sqrt L\asymp1`?

The question is deliberately stronger than proving decay for one fixed mass, one fixed output row, one fixed `s`, or the tangent alone. It asks for the uniform estimate actually needed before the fixed-axis margin can be transported to the variable corridor.

## Why it may matter

PF-259/PF-260 show that the correctly normalized tangent has enough margin, while PF-261 shows that finite seam scale is not an uncontrolled perturbation: it is a concrete massive-resolvent family with an exact complete-axis Green representation. A positive uniform estimate would remove the last specifically **fixed-axis finite-`s`** obstruction and justify spending the remaining `1<R<2` margin on PF-256's actual-corridor transport and PF-243's Robin--Poisson factorization.

A negative estimate would be equally decisive. If the exact Green sum itself develops enough high-to-low mode leakage to destroy every strict `R>1`, the present Jacobi/Robin route fails before the more expensive actual-corridor and global reassembly stages.

## Decisive test

Start from PF-261's exact off-diagonal identity

\[
\langle e_i,\mathcal R_{s,r}^0e_j\rangle
=-\frac{2}{rs^2\sqrt{\kappa_i\kappa_j}}
\sum_{k\ge0}a_k^2
\langle e_i,(L+a_k^2)^{-1}e_j\rangle,
\qquad i\ne j,
\]

inside one parity sector. Use either the explicit complete-axis Green kernel or its equivalent Gegenbauer/continuous-Hahn Fourier representation to estimate the **summed** expression uniformly in the coupled variables `s,k,i,j` on a separated cone such as `j\ge2i+2`.

The target is a weighted operator estimate retaining any fixed `R>1`, not sharpness of the tangent threshold. The mass sum must be controlled before taking an operator norm; PF-261's positive strong expansion does not license termwise use of a non-summable norm majorant. Exponential locality in the `\tau` coordinate is also not by itself Gegenbauer-mode locality and must be converted quantitatively.

If the relative-seam estimate survives, propagate it through the **combined** bounded source map

\[
B_{s,r}^0=X_{s,r}^0(I+(X_{s,r}^0)^*X_{s,r}^0)^{-1}
\]

rather than separating a naked polar partial isometry. Only after this fixed-axis test succeeds should the surviving margin be transferred through PF-256's actual `K_a` basis, PF-255's hypercycle transport, reflection factors, and PF-243's separated Robin--Poisson factorization.

Kill the route if the exact finite-`s` Green sum or the combined Robin map destroys every strict `R>1` weight uniformly in the canonical tail.

## Evidence boundary

PF-258 establishes the intrinsic-six thin-seam tangent. PF-259/PF-260 establish its full fixed-axis **upper** fractional window. PF-261 establishes finite-`s` boundedness, fixed-axis complete-lift closure of the relative square-root/Robin algebra, the positive odd-pole resolvent expansion, and the exact complete-axis Green representation of every massive resolvent term.

None of these findings proves the required uniform Gegenbauer high-to-low estimate for the full mass sum. The explicit exponential Green kernel is in the `\tau` coordinate and does not automatically yield weighted mode decay. Nor has any result transferred a finite-`s` bound to the actual `K_a` corridor, hypercycle compactification, PF-243 Robin--Poisson map, trace-class shear block, finite-pant completion, or global weak-`S_1` reassembly.

Nothing here proves a scattering/determinant identity, a zeta-zero statement, or RH.

## Research disposition

Accepted. The fixed-axis tangent stage is complete at the upper-bound level, and PF-261 turns the formerly opaque finite-`s` crossover into an exact massive-resolvent Green-sum problem while closing the fixed-axis complete-lift domain gate. The active discriminator is now uniform separated mode decay for that **summed finite-seam operator and its combined Robin transform**. Sharpness of the tangent window and isolated fixed-mass estimates are secondary unless they resolve this uniform test.