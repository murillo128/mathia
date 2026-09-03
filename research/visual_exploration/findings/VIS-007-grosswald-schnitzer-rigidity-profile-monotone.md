# VIS-007 — Grosswald–Schnitzer integer rigidity has a monotone prime-scale resolution profile

## Claim

`PL-127` defines

`g(x) = log(x)/(sqrt(x)-1)`,  `x>1`,

and proves that the central Grosswald–Schnitzer reflection-phase slope is

`D(q) = sum_n [g(p_n)-g(q_n)]`,

with nonnegative summands for the one-sided deformations `p_n <= q_n`. For integer deformations it introduces the cutoff threshold

`delta(X) = min_{p prime, p<=X} [g(p)-g(p+1)]`.

That minimum has no hidden prime-scale irregularity. Define

`h(x) = g(x)-g(x+1)`.

Then `g` is strictly decreasing and **strictly convex** on `(1,infinity)`, so `h(x)>0` and `h` is strictly decreasing on `(1,infinity)`. Therefore, if

`P_X = max {p prime : p<=X}`,

then exactly

`delta(X) = h(P_X) = g(P_X)-g(P_X+1)`.

Consequently the `PL-127` certificate can be written without a minimization over earlier primes:

`D(q) < g(P_X)-g(P_X+1)`

forces `q_n=p_n` for every prime generator `p_n<=X`.

Likewise, if `P` is the first altered prime, the lower certificate `D(q)>=h(P)` deteriorates monotonically as the first defect is moved to larger prime scale. Together with the asymptotic already derived in `PL-127`,

`h(P) = ((1/2)log P - 1) P^(-3/2) + O(log P / P^2)`,

the integer rigidity threshold is therefore a canonical one-dimensional resolution profile rather than an irregular minimum over the prime set.

**Evidence/status:** `EXACT-DERIVED + VISUAL-TO-EXACT + REFINEMENT`.

This is a sharpening of the `PL-127` cutoff formulation, not a new Grosswald–Schnitzer theorem and not an RH implication.

## Exact convexity derivation

The monotonicity of `g` was already proved in `PL-127`. To control the one-step threshold, it is enough to prove strict convexity.

Put `x=y^2` with `y>1`. Direct differentiation gives

`g''(y^2) = N(y) / [2 y^4 (y-1)^3]`,

where

`N(y) = 3 y^2 log y - 4 y^2 - y log y + 6y - 2`.

The denominator is positive for `y>1`. At the endpoint,

`N(1)=0`,  `N'(1)=0`,

while

`N''(y) = 6 log y + 1 - 1/y`.

For every `y>1`, both `log y>0` and `1-1/y>0`, hence `N''(y)>0`. Thus `N'` is strictly increasing from zero and `N(y)>0` for all `y>1`. Therefore

`g''(x)>0`  for every `x>1`.

Now

`h'(x)=g'(x)-g'(x+1)`.

Strict convexity makes `g'` strictly increasing, so `g'(x)<g'(x+1)` and hence `h'(x)<0`. Since `g` is strictly decreasing, `h(x)>0`. This proves both positivity and strict decay of the one-step rigidity threshold on the whole real interval, not merely on sampled primes.

Restricting a strictly decreasing `h` to the primes immediately gives

`min_{p prime, p<=X} h(p) = h(P_X)`.

No prime-gap estimate is involved.

## Visual and computational audit

Visualization: [[research/visual_exploration/visualizations/grosswald-schnitzer-rigidity-profile.md]].

The retained log-log view plots `h(p)` for primes `11<=p<=100000` together with the `PL-127` asymptotic. It was motivated by a visual question: whether prime sampling introduced local dips into the cutoff threshold or whether the thresholds lay on a single monotone envelope. The picture strongly suggested the latter, and the calculus argument above removes dependence on the picture.

As a renderer/formula audit, exact floating-point evaluations were checked at every prime through `200000`; the sampled sequence was strictly decreasing. Representative values are

- `h(101) ~= 1.69865528e-3`;
- `h(1009) ~= 8.27619606e-5`;
- `h(10007) ~= 3.68477735e-6`;
- `h(100003) ~= 1.51461604e-7`.

The asymptotic curve approaches the exact profile smoothly. These numerical checks are not evidence for the theorem; the sign of `g''` is decisive.

The committed PNG is palette-quantized only after rendering and was fully decoded with Pillow `Image.verify()`, then reopened and loaded before publication.

## Prior-art and novelty assessment

The arithmetic deformation, zero-preserving quotient, phase-slope identity, positivity, integer cutoff certificate, and its asymptotic are already grounded and audited in `PL-127`, ultimately against Grosswald–Schnitzer's 1978 deformation theorem and the Hamburger-converse literature used by that line.

A targeted search for the particular convexity/one-step-threshold observation around `g(x)=log(x)/(sqrt(x)-1)` did not expose a named theorem or a source using this exact resolution-profile formulation. No broad novelty claim is made: the result is an elementary calculus consequence of the `PL-127` observable. Its durable value is to eliminate a seemingly arithmetic minimization and expose the exact scale ordering of that certificate.

## Boundary conditions and counterarguments

The result does **not** remove the discreteness boundary from `PL-127`. For unrestricted real deformations one may perturb a fixed generator by an arbitrarily small amount, so there is no corresponding positive one-step threshold.

The scalar `D(q)` also remains a lossy summary. Its monotone resolution profile certifies an untouched prime prefix, but it does not by itself identify the complete later deformation pattern: different collections of positive summands can in principle have the same total. Recovering more than a prefix certificate requires additional phase information.

Finally, the critical line enters because the reflection cocycle is sampled at its self-dual fixed point. This is a rigidity diagnostic inside a zero-preserving deformation family, not a mechanism forcing zeta zeros onto that line.

## Consequence for the research line

The visually suggested cutoff geometry formalizes to a particularly simple rule: **larger prime scale means strictly weaker minimum detectable integer phase defect**. The `PL-127` threshold is a monotone staircase when indexed by the largest prime below the requested resolution.

That makes a richer next question precise. If the full critical-line phase contains more information than the single slope `D(q)`, can a finite phase fingerprint reconstruct the actual low-scale deformation pattern rather than only certify that a prefix is unchanged? That question is handed back to Prime Lattice as a proposed clue.