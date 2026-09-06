---
id: CLUE-analytic-frontier-even-moment-radial-coercivity
type: research-clue
status: accepted
origin: research-watch
target_line: analytic_frontier
based_on:
  - research/analytic_frontier/findings/ANF-045-two-pair-five-point-obstruction-scalarizes-to-a-strict-hilbert-coherence-gap.md
  - research/analytic_frontier/findings/ANF-057-reciprocal-sinh-control-sharpens-the-support-free-relative-height-tube.md
  - research/analytic_frontier/findings/ANF-059-exact-montgomery-taylor-curvature-transform-shrinks-the-five-point-separation-annulus.md
  - research/analytic_frontier/findings/ANF-061-quadratic-height-renormalization-closes-the-common-translation-escape.md
  - research/analytic_frontier/findings/ANF-062-validated-interval-certificate-proves-montgomery-taylor-five-point-zero-freeness.md
---

# Does an even-moment inequality give the sharp all-height five-point margin?

## Observation

Independent compute execution of [issue #121](https://github.com/murillo128/mathia/issues/121) certified the fixed Montgomery–Taylor defect `H_MT>0`, conditional on the issue's canonical outer-domain exclusions and Arb/FLINT arithmetic. The result is now canonicalized in `ANF-062`. A complete rational interval cover inspected 804375 boxes at 128 bits, escalating unresolved boxes to 512 bits, and left no unresolved cells. On the residual enclosure it certified `H_MT/(y1²+y2²)>3.9e-6`; the separately validated small-height face and analytic common-translation tail complete the sign decision. The tiny interval margin is slack in a sufficient enclosure, not evidence of a nearly vanishing geometry.

The computation's quadratic normalization exposes a stronger candidate. Put

`M_n(t)=∫ α^(2n) J_MT(α) cos(2παt) dα`,

so `M_1=K_MT` and `m5=2M_1(0)+3 inf_t M_1(t)`. For `y1=y(1+q)`, `y2=y(1−q)`, the zero-height limit has exact infimum `2π²m5`: its three curvature terms are bounded below separately, and the bound is approached with `q→1`, `d` at a curvature minimum, and `t2=0`. Numerical evaluation gives approximately `0.7140599927`. The certified sign decision does not establish that this boundary value is the infimum at positive height.

A bounded audit found no decrease of `H_MT/(y1²+y2²)` along a common height ray in a deterministic numerical search on the residual box. More specifically, 128-node Gauss–Legendre quadrature and one-dimensional numerical searches over `|t|≤8` supported

`inf_t M_n(t)/M_n(0) ≥ −2^(2n−1)/(1+2^(2n−1))`

at `n=2,3,4,5,6,8,12,20`. The sampled gaps above these thresholds ranged from about `0.1086` to `0.00567`. These controls are numerical leads only.

## Research question

Does the displayed moment inequality hold for every integer `n≥2` and every real `t` for the exact Montgomery–Taylor spectrum? If it does, it supplies an all-height explanation and the sharp global bound

`H_MT ≥ 2π²m5 (y1²+y2²)`,

with the infimum approached at the degenerate zero-height, one-pair face, and makes the normalized defect nondecreasing under simultaneous height dilation.

The sufficient bridge is explicit. Write `yj=λfj`, `f1,f2>0`, `d=t1−t2`, `A_n=f1^(2n)+f2^(2n)` and `B_n=(f1+f2)^(2n)+(f1−f2)^(2n)`. The coefficient of `λ^(2n)` in `H_MT` is `(2π)^(2n)/(2n)!` times

`2^(2n−1) A_n M_n(0) + f1^(2n) M_n(t1) + f2^(2n) M_n(t2) + B_n M_n(d)`.

The elementary bound `B_n≤2^(2n−1)A_n` shows that the proposed moment inequality makes every coefficient for `n≥2` nonnegative. The quadratic term is already bounded below by `2π²m5(f1²+f2²)`.

## Why it may matter

This would strengthen the positive interval cover of `ANF-062` into a sharp coercivity theorem and explain why finite height adds a nonnegative remainder. The resulting spectral-moment criterion could distinguish spectra with this stronger property from profiles that merely pass the quadratic curvature gate. It is a different test from repeating base zero-freeness or selecting a notch parameter.

## Decisive test

Prove the moment bound uniformly in both `n` and `t`, using validated finite cases only when accompanied by analytic control of the remaining moment orders and the full horizontal tails. Alternatively, certify a violating moment/order to kill this sufficient moment route. Such a violation alone would not refute the sharp bound, because the coefficient estimate discarded linkage between the three horizontal arguments. A certified decreasing normalized height ray would directly refute the proposed monotonicity.

## Evidence boundary

`ANF-062` settles only the exact sign question. It does not prove the all-moment inequality, radial monotonicity, or the proposed sharp global constant. The additional searches cover only the stated finite orders and horizontal range and use ordinary numerical arithmetic. The elementary series bridge is a sufficient condition, not an equivalence. No uniqueness of boundary minimizers, notch choice, larger-multiset conclusion, external novelty, or RH consequence is asserted.

## Research disposition

Accepted as a **structural strengthening**, not as a prerequisite for the already closed five-point zero-freeness problem. Research Watch independently checked the series bridge: expanding the exact `ANF-045` integrand under `y_j=lambda f_j` gives the displayed coefficient, and for `n>=2` the proposed lower bound together with `B_n<=2^(2n-1)A_n` makes that coefficient nonnegative. For `n=1`, the canonical curvature combination gives the stated `2 pi^2 m5(f1^2+f2^2)` floor. Hence the proposed moment inequality would indeed make `H_MT/lambda^2` nondecreasing and upgrade `ANF-062` to the sharp boundary coercivity constant.

The finite numerical checks are not evidence for the universal moment inequality. A targeted literature search found only the general positive-definite/characteristic-function framework and the established Montgomery--Taylor extremal setting, not this all-order moment lower bound. The accepted task is therefore narrow: prove the bound uniformly in `n,t`, or kill this sufficient route with one certified violating order. Even success would strengthen only the fixed five-point profile unless a separate argument exports the criterion to larger multisets.