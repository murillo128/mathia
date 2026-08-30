---
id: CLUE-prime-flute-affine-composite-clone-relative-operator-class
type: research-clue
status: resolved
origin: mind
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-106-affine-composite-clone-is-l1-close.md
  - research/prime_flute/findings/PF-107-shift-clone-cuff-defect-is-l2-not-l1.md
  - research/prime_flute/findings/PF-108-shift-clone-collar-and-spine-defects-are-summable.md
  - research/prime_flute/findings/PF-109-shift-clone-preserves-canonical-separator-pinching-multiplicatively.md
  - research/prime_flute/findings/PF-111-shift-clone-has-summable-pant-local-marked-length-distortion.md
  - research/prime_flute/findings/PF-112-first-relative-resolvent-is-not-trace-class.md
  - research/prime_flute/findings/PF-114-shift-clone-pant-waves-telescope-but-seam-relative-mode-does-not.md
  - research/prime_flute/findings/PF-118-shift-clone-pants-are-arc-lipschitz-close.md
  - research/prime_flute/findings/PF-119-canonical-cusp-split-gluing-offset-has-summable-shift-clone-defect.md
  - research/prime_flute/findings/PF-120-cusp-busemann-shifts-must-synchronize.md
  - research/prime_flute/findings/PF-121-ideal-lambert-shift-comparison-is-asymptotically-bilipschitz.md
  - research/prime_flute/findings/PF-122-canonical-cusp-strip-gluing-cost-is-summable.md
  - research/prime_flute/findings/PF-123-asymptotic-metric-equivalence-forces-compact-relative-resolvent.md
  - research/prime_flute/findings/PF-124-lambert-cuff-trace-is-zero-twist-coherent.md
  - research/prime_flute/findings/PF-125-shift-clone-has-compact-relative-resolvent.md
---

# Affine composite clone and the relative Laplacian class

## Observation

The exact all-composite shift clone `p_n -> p_n+1` survives every tail control tested in PF-106--PF-124. Endpoint, cross-ratio, separator, collar/spine, pant-wave, and marked-length comparisons either vanish or are summable, while PF-112 shows that first-resolvent trace class is too strong for a generic two-dimensional metric perturbation. PF-123 isolates the relevant weaker operator gate: a global marked comparison whose metric coefficients and volume density tend to the prime metric at infinity would already force compact relative resolvent and equality of essential spectra.

PF-119--PF-124 progressively reduced the missing geometry to boundary coherence. The one-cusp pentagon splits into two one-parameter Lambert pieces; their deep cusp can be synchronized, and finite-cuff maps can be chosen neighbor-independently and made exactly zero-twist coherent. The last unresolved issue was whether the two Lambert pieces could be reconciled through the bounded-height region without a distortion floor when neighboring gap ratios are extreme.

## Research question

Can one construct a marked global homeomorphism

\[
F:X_{\rm prime}\longrightarrow X_{\rm shift}
\]

with tail bilipschitz constants tending to `1`, so that after transporting the clone metric to the prime surface,

\[
\|F^*g_{\rm shift}-g_{\rm prime}\|_{g_{\rm prime}}\to0
\]

uniformly at infinity and the volume-density ratio also tends to `1`?

The originally proposed implementation tried to combine the particular PF-121/PF-122 maps while retaining PF-124's explicit cuff trace. Research is allowed to replace that implementation if a direct construction supplies the same intrinsic requirements: one common split trace, neighbor-independent finite-cuff traces, exact zero-twist gluing, and `K_n->1`.

## Why it may matter

A positive answer makes the accepted all-composite control spectral rather than merely geometric. By PF-123 it forces compact difference of the transported first resolvents and equality of essential Laplace spectra, proving that the essential spectral class cannot be a primality/RH selector for the exact prime-flute construction.

A negative answer would have identified a genuine nonlocal amplification mechanism surviving all of PF-106--PF-124 rather than a coordinate, cusp-gauge, collar, or finite-cuff artifact.

## Decisive test

A positive resolution must:

1. construct pant-local marked homeomorphisms with bilipschitz constants `K_n->1` uniformly over arbitrary neighboring gap ratios;
2. make the two Lambert halves agree exactly on their artificial split ray;
3. make finite-cuff traces depend only on the matched cuff pair and commute with the zero-twist gluing after reflection;
4. glue the complete tail and verify uniform metric/density convergence at infinity;
5. invoke PF-123 only after those geometric hypotheses are established.

A decisive negative resolution would need an invariant distortion lower bound or a Weyl/limit-operator obstruction that survives the local Lambert, cusp-strip, and zero-twist controls already proved.

## Evidence boundary

The clue itself is not evidence. Its earlier `accepted` status asserted only that the operator-class question was worth investigation.

PF-125 now supplies the durable outcome. Its direct Fermi-coordinate comparison fixes the natural split-ray Busemann coordinate, and the PF-119 chart scales then give an exact identity forcing the left and right Lambert traces to agree. The induced finite-cuff trace is a new neighbor-independent trace rather than PF-124's particular formula; reflection gives the same exact zero-twist commuting square, so the earlier fixed-trace implementation is superseded rather than assumed.

PF-125 reaches compact relative resolvent and equality of essential spectra through PF-123. It does not establish trace-class first resolvent, higher Schatten membership, wave/scattering equivalence, resonance equality, relative determinants, discrete-spectrum equality, Selberg/Ruelle equivalence, or any RH statement.

## Research disposition

Outcome: supported

Resolved by:
- [[research/prime_flute/findings/PF-125-shift-clone-has-compact-relative-resolvent.md]]

The original global asymptotic-equivalence question has a positive answer at exactly the strength needed for PF-123. The consequence is adversarial for the research program: an exact all-composite flute lies in the same compact-resolvent/essential-spectrum class as the prime flute, so that spectral class cannot encode primality by itself.
