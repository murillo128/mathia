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
  - research/prime_flute/findings/PF-265-unbounded-gap-combes-thomas-makes-mass-mode-green-decay-uniform.md
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

PF-262--PF-264 identify the sharp fixed-mass mode geometry behind that Green sum. PF-262 derives the double-root indicial exponents `-1/2\pm\mu`, `\mu=\sqrt{1+a^2}`. PF-263 removes the integer-difference caveat: at resonant masses the logarithm belongs only to the discarded dominant solution, so the `\ell^2` Green tail keeps the pure recessive power. PF-264 then lets the source index enter the tail and uses the exact Jacobi Wronskian to cancel the unknown left connection coefficient. For every fixed mass,

\[
\langle e_{2i+\varepsilon},(L+a^2)^{-1}e_{2j+\varepsilon}\rangle
\sim
\frac{1}{2\mu\sqrt{ij}}
\left(\frac{i}{j}\right)^\mu,
\qquad i\le j\to\infty.
\]

PF-265 now separates the remaining uniformity problem into two genuinely different pieces. A classical unbounded-Jacobi Combes--Thomas theorem, specialized using the exact fact that every PF parity block satisfies `L_\varepsilon\ge I`, gives constants `c_p>0` and an explicit all-mass prefactor such that

\[
|G_{ij}^{(\varepsilon)}(a)|
\le \frac4{\mu^2}
\exp\!\left[-\sum_{m=i}^{j-1}
\min\!\left(1,\frac{c_p\mu}{m+1}\right)\right].
\]

In the unsaturated regime this already gives a uniform ratio exponent `( (i+1)/(j+1) )^{c_p\mu}`, and a second adaptive estimate gives polynomial-in-mass decay of order `j-i` once `\mu\gtrsim j`. Hence the sufficiently large odd-mass tail is absolutely summable for every separated mode pair. The unresolved issue is **not** mass-uniform off-diagonal recession itself; it is recovery of PF-264's additional sharp `1/\sqrt{ij}` Green amplitude uniformly while `a`, `i`, and `j` move together.

## Research question

Does the **full odd-mass Green sum** supplied by PF-261 preserve some uniform separated high-to-low exponent `R>1` after the endpoint weights and the combined bounded Robin transform are included, uniformly through the crossover `rs\sqrt L\asymp1`?

After PF-265, sharpen this to the load-bearing question: can one place a **uniform sharp mode-amplitude estimate** on top of the now-controlled mass/mode decay metric, strongly enough that summing the actual odd ladder retains the extra mode power needed to cross the one-dimensional `R=1` threshold?

The question is deliberately stronger than proving decay for one fixed mass, one fixed output row, one fixed `s`, or the tangent alone. PF-262--PF-265 settle the indicial exponent, resonance issue, fixed-mass Wronskian normalization, uniform Combes--Thomas metric, and sufficiently large-mass recession. What remains is the coupled amplitude regime and the operator-level summation.

## Why it may matter

PF-259/PF-260 show that the correctly normalized tangent has enough margin, while PF-261 shows that finite seam scale is not an uncontrolled perturbation: it is a concrete massive-resolvent family with an exact complete-axis Green representation. PF-264 adds the sharp fixed-mass structural signal `1/(\mu\sqrt{ij})(i/j)^\mu`, and PF-265 shows that the ratio-decay mechanism itself survives uniformly across mass.

This is a useful narrowing because the generic uniform Green estimate stops naturally at a critical mode amplitude after PF-261's endpoint weights, whereas PF-264's extra `1/\sqrt{ij}` is precisely what can provide strict `R>1` room. A positive uniform amplitude estimate would remove the last specifically **fixed-axis finite-`s`** obstruction and justify spending the remaining margin on PF-256's actual-corridor transport and PF-243's Robin--Poisson factorization. A negative estimate would be equally decisive: if a transition regime destroys the sharp amplitude even though the decay exponent remains uniform, the present Jacobi/Robin route fails before the more expensive actual-corridor and global reassembly stages.

## Decisive test

Start from PF-261's exact off-diagonal identity

\[
\langle e_i,\mathcal R_{s,r}^0e_j\rangle
=-\frac{2}{rs^2\sqrt{\kappa_i\kappa_j}}
\sum_{k\ge0}a_k^2
\langle e_i,(L+a_k^2)^{-1}e_j\rangle,
\qquad i\ne j,
\]

inside one parity sector. Use PF-265's uniform Combes--Thomas metric as the **already solved decay envelope** rather than rebuilding a separate mass-uniform exponent theorem. The next target is a uniform amplitude normalization compatible with both PF-264's fixed-mass asymptotic and the trivial high-mass resolvent scale. A natural diagonal discriminator is

\[
G_{ii}^{(\varepsilon)}(a)
\lesssim \frac{1}{\mu(i+\mu)}.
\]

For `i\gg\mu` this has PF-264's `1/(\mu i)` scale; for `\mu\gg i` it becomes `O(\mu^{-2})`. Prove this bound, or another bound carrying the same load-bearing mode gain, and determine whether it combines with PF-265's off-diagonal metric to yield on `j\ge2i+2`

\[
|G_{ij}^{(\varepsilon)}(a)|
\lesssim
\frac{1}{\mu\sqrt{ij}}
\left(\frac{i+1}{j+1}\right)^{c\mu}
\]

with constants uniform across the coupled mass/mode regimes. A proof may use the exact continuous-axis realization, a uniform discrete Wronskian/transfer estimate, or an exact spectral representation, but it must preserve the physical parity normalization rather than hide the amplitude in an `a`-dependent connection constant.

Then sum the actual odd masses `a_k=(2k+1)\pi/(2rs)` **before** taking the weighted operator norm. PF-265 already proves that sufficiently large masses are absolutely summable for each separated pair, so the decisive summation analysis should isolate the low/intermediate crossover where the sharp amplitude matters and prove the resulting separated weighted bound uniformly in `s`.

If the relative-seam estimate survives, propagate it through the **combined** bounded source map

\[
B_{s,r}^0=X_{s,r}^0(I+(X_{s,r}^0)^*X_{s,r}^0)^{-1}
\]

rather than separating a naked polar partial isometry. Only after this fixed-axis test succeeds should the surviving margin be transferred through PF-256's actual `K_a` basis, PF-255's hypercycle transport, reflection factors, and PF-243's separated Robin--Poisson factorization.

Kill the route if the uniform sharp amplitude fails in a transition regime strongly enough that the exact finite-`s` mass sum or combined Robin map cannot retain any strict `R>1` weight. Failure of a sharper exponential coefficient alone is no longer decisive, because PF-265 already supplies a fixed positive uniform decay metric.

## Evidence boundary

PF-258 establishes the intrinsic-six thin-seam tangent. PF-259/PF-260 establish its full fixed-axis **upper** fractional window. PF-261 establishes finite-`s` boundedness, fixed-axis complete-lift closure of the relative square-root/Robin algebra, the positive odd-pole resolvent expansion, and the exact complete-axis Green representation of every massive resolvent term.

PF-262 gives the fixed-source indicial powers; PF-263 proves that resonant masses retain the same pure recessive Green exponent; PF-264 proves the universal two-index **fixed-mass** leading law and cancellation of the left connection coefficient. PF-265 adds an all-mass/all-mode Combes--Thomas envelope with explicit prefactor, a uniform positive fraction of the ratio exponent in the unsaturated regime, and sufficient high-mass path decay to make the far odd-mass tail absolutely summable for each separated pair.

PF-265 does **not** make PF-264's `1/(\mu\sqrt{ij})` amplitude uniform, does not sum the complete odd ladder in the required weighted operator norm, and does not prove strict `R>1` finite-seam smoothing. Nor has any result transferred such a finite-`s` bound to the actual `K_a` corridor, hypercycle compactification, PF-243 Robin--Poisson map, trace-class shear block, finite-pant completion, or global weak-`S_1` reassembly. Nothing here proves a scattering/determinant identity, a zeta-zero statement, or RH.

## Research disposition

Accepted. The fixed-axis tangent, fixed-mass Green mechanism, resonant behavior, and mass-uniform off-diagonal recession are now structurally controlled. The active discriminator is narrower: **recover PF-264's sharp mode amplitude uniformly across the coupled mass/mode regimes, sum the low/intermediate odd-mass crossover together with PF-265's controlled high-mass tail, and test whether the combined Robin transform retains strict `R>1` margin**. Further work on the decay exponent alone is secondary unless it directly supplies the missing amplitude or operator-level summation.