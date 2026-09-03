# PL-137 — Pretentious distance is the canonical weighted prime-torus metric, but its established rigidity stops at mean-value and PNT-edge scales

## Claim

For a completely multiplicative function `f` with `|f(p)|=1` at every prime, write

`f(p)=exp(i theta_p)`

and therefore, in prime-exponent coordinates,

`f(n)=exp(i <v(n),theta>)`.

The standard truncated pretentious distance to the vertical character `n^(it)` is exactly

`D_x(f,n^(it))^2 = sum_(p<=x) (1-Re(f(p)p^(-it)))/p`

`= (1/2) sum_(p<=x) |exp(i theta_p)-exp(i t log p)|^2/p`.

Thus classical pretentious multiplicative-function theory already equips the prime torus with a canonical arithmetic metric: a `1/p`-weighted chordal distance from the phase point `(f(p))_p` to the Kronecker orbit `(p^(it))_p`, whose frequencies are precisely the lattice energy coefficients `log p`.

This geometry is mathematically substantive rather than decorative. Halász's theorem, in the explicit Granville--Soundararajan formulation, controls the mean value of a bounded multiplicative function through

`M(f;x)=min_(t in R) D_x(f,n^(it))^2`

with principal decay of size `(1+M)e^(-M)`. Modern pretentious metrics also recover the classical Mertens `3-4-1` zero-free-region argument, and a 2026 extension to automorphic `L`-functions replaces the prime-only distance by a prime-power/logarithmic-derivative metric and obtains standard zero-free regions.

However these established metric mechanisms do **not** naturally reach the RH scale. The standard prime-only distance has diameter only logarithmic in `log x`:

`D_x(f,n^(it))^2 <= 2 sum_(p<=x) 1/p = 2 log log x + O(1)`.

Consequently the distance term in the Halász bound can never itself generate normalized cancellation of order `x^(-1/2+epsilon)`: even at its maximal possible scale it yields only polylogarithmic decay. The prime-power `D_sigma` metrics used for zero-free regions are defined for `sigma>1` and connect to logarithmic derivatives in their honest absolute-convergence half-plane; the metric argument supplies PNT-edge zero repulsion, not a continuation mechanism selecting `Re(s)=1/2`.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE/OBSTRUCTION`.

No new theorem is claimed. The torus interpretation and diameter bound are elementary consequences of the standard definitions. The durable value is to identify an established arithmetic geometry that matches the line's prime-coordinate/Kronecker language almost exactly, and to record the quantitative boundary preventing the standard distance-only Halász mechanism from being mistaken for an RH-scale mechanism.

## Exact exponent-lattice interpretation

Let `f` be completely multiplicative and unitary. Unique factorization gives

`f(n)=product_p f(p)^(v_p(n))`.

Writing `f(p)=e^(i theta_p)` yields

`f(n)=e^(i <v(n),theta>)`.

The vertical multiplicative character is

`n^(it)=e^(it log n)=e^(it <v(n),(log p)_p>)`,

so its prime coordinates form the Kronecker curve

`gamma(t)=(e^(it log p))_p`.

For two unit complex numbers `z,w`,

`1-Re(z conjugate(w))=(1/2)|z-w|^2`.

Hence the usual pretentious distance becomes exactly

`D_x(f,n^(it))^2`

`= sum_(p<=x) [1-Re(f(p)p^(-it))]/p`

`= (1/2) sum_(p<=x) |e^(i theta_p)-e^(it log p)|^2/p`.

The distance is therefore not an arbitrary metric imposed on exponent vectors. It is the standard number-theoretic metric on prime phases, and its distinguished comparison family is exactly the one-parameter prime-log Kronecker flow emphasized by the `prime_lattice` mandate.

The geometry lives on the dual prime coordinates rather than directly on the positive exponent cone. The pairing with `v(n)` is nevertheless exact: the same coordinate phases that enter the distance determine the character `f(n)=e^(i<v(n),theta>)` on every lattice point.

## Halász turns this geometry into cancellation

Granville and Soundararajan summarize Halász's theorem for multiplicative `|f(n)|<=1` by the parameter

`M = min_(y in R) sum_(p<=x) [1-Re(f(p)p^(-iy))]/p`.

Their explicit upper bound for the normalized mean value has the characteristic factor

`(1+M)e^(-M)`.

Thus closeness to some vertical character `n^(iy)` is the obstruction to cancellation: a multiplicative function whose prime-phase point lies close to the Kronecker orbit may have a large mean, while large distance forces mean-value decay. This is an established and highly developed mechanism connecting prime-coordinate geometry to global arithmetic cancellation.

In prime-lattice language, Halász theory therefore already realizes the schematic bridge

`prime phases -> distance from the log-prime flow -> cancellation of sums over lattice points`.

This is stronger prior art than merely observing equidistribution of the Kronecker flow. It supplies a quantitative geometric functional that controls an arithmetic observable.

Primary literature anchor:

- Andrew Granville and K. Soundararajan, “Decay of Mean Values of Multiplicative Functions,” *Canadian Journal of Mathematics* **55**(6) (2003), 1191--1230. DOI: https://doi.org/10.4153/CJM-2003-047-0. The abstract explicitly identifies Halász's minimizing prime sum and the bound `<<(1+M)e^(-M)`.

## Quantitative obstruction to RH-scale cancellation from the standard distance alone

Each summand in the squared distance satisfies

`0 <= 1-Re(f(p)p^(-it)) <= 2`.

Therefore for every `f,t`,

`D_x(f,n^(it))^2 <= 2 sum_(p<=x) 1/p`.

Mertens' theorem for the reciprocal-prime sum gives

`sum_(p<=x) 1/p = log log x + O(1)`,

hence

`M(f;x) <= 2 log log x + O(1)`.

This is a geometric diameter bound: with the standard `1/p` weights, the squared distance across the entire truncated prime torus grows only like `log log x`.

The function `(1+M)e^(-M)` is decreasing for `M>0`. Even if a particular multiplicative function attains distance of the maximal possible order, the smallest scale that this principal Halász term can reach is therefore only

`(1+O(log log x)) exp(-2 log log x+O(1))`

`= (log log x) (log x)^(-2+O(1/log log x))`,

up to constants and the precise theorem's auxiliary terms. This is polylogarithmic normalized decay.

By contrast, an RH-strength Mertens estimate would require

`sum_(n<=x) mu(n) = O_epsilon(x^(1/2+epsilon))`,

that is, normalized cancellation `O_epsilon(x^(-1/2+epsilon))`. To obtain such a scale from an exponential factor `e^(-M)` alone would require `M` of order `log x`, which the standard prime distance cannot have.

The conclusion is intentionally narrow: **the standard Halász distance term by itself cannot certify RH-scale square-root cancellation**. This does not say that pretentious methods can never participate in an RH argument, nor that special multiplicative functions cannot have much stronger cancellation for reasons invisible to the generic Halász bound.

## Prime-only information loss

There is another exact limitation. The standard pretentious distance uses only values at primes. Consequently it is a pseudometric on the class of general multiplicative functions: two functions can have distance zero while differing on prime powers.

The simplest arithmetic control is Möbius versus Liouville. At every prime,

`mu(p)=lambda(p)=-1`,

so their standard prime-only distance is zero, even though

`mu(p^2)=0`, while `lambda(p^2)=1`.

Therefore the standard metric sees the first prime-axis layer `e_p` but not the full axis rays `k e_p`. This does **not** affect the exact character interpretation above for unitary completely multiplicative functions, whose prime values determine all prime powers. It does matter when the target arithmetic function is Möbius or when zero-sensitive logarithmic derivatives naturally live on all prime powers.

This distinction is important for the line because the von Mangoldt skeleton of the explicit formula occupies every point `k e_p`, not just `e_p`.

## Prime-power metrics already repair that loss at the PNT edge

Koukoulopoulos formalized the classical Hadamard--de la Vallée Poussin/Mertens `3-4-1` mechanism using a family of pretentious metrics `D_sigma` for `sigma>1`. A recent paper by Wattanawanichkul makes the prime-power structure explicit and extends the approach to automorphic `L`-functions.

For automorphic representations the modified squared metric is a weighted sum over prime powers of squared differences of logarithmic-derivative coefficients, with weights proportional to

`log N(p) / N(p)^(k sigma)`, `sigma>1`.

It can be rewritten in terms of logarithmic derivatives of Rankin--Selberg `L`-functions. Wattanawanichkul then applies triangle inequalities to prove classical zero-free regions; in the Riemann-zeta specialization the construction recasts Mertens' `3-4-1` inequality. This shows that the metric idea can carry genuine zero-exclusion content and that adding the full prime-power rays is mathematically meaningful.

Relevant sources:

- Dimitris Koukoulopoulos, *The Distribution of Prime Numbers*, Graduate Studies in Mathematics **203**, American Mathematical Society, 2019. Theorem 8.3 is the metric formulation cited by the modern extension.
- Nawapan Wattanawanichkul, “A metric approach to zero-free regions for L-functions,” *European Journal of Mathematics* **12** (2026), Article 30, published 6 July 2026. DOI: https://doi.org/10.1007/s40879-026-00913-5. The paper defines the prime-power/logarithmic-derivative metric for `sigma>1`, relates it to `L'/L`, recovers the `3-4-1` argument, and proves zero-free regions for standard and Rankin--Selberg `L`-functions under the stated self-duality hypotheses.

The analytic-domain distinction is load-bearing. The metric sums and the logarithmic-derivative Dirichlet series are formed for `sigma>1`, where the Euler/logarithmic-derivative expansions converge. The resulting contradiction excludes zeros in a region near `Re(s)=1` by combining those inequalities with the meromorphic/analytic structure of the `L`-functions. The metric is not itself an analytically continued Euler product in the critical strip.

## Adversarial controls

The most dangerous overstatement would be to say that the prime-torus metric “explains the critical line.” It does not. The established theorems demonstrate a different boundary: prime-phase geometry controls generic multiplicative mean values and supports classical zero-free-region repulsion near `Re(s)=1`.

The mechanism is also deliberately broad. Pretentious distance applies to large classes of multiplicative functions, and the 2026 prime-power metric extends to broad automorphic `L`-functions. Therefore the mere existence of a metric, triangle inequality, or Kronecker comparison cannot distinguish the Riemann zeta function from matched controls. Any RH-level strengthening would have to use additional exact global structure such as the Riemann functional equation/archimedean factor, a positivity principle, or a zeta-specific trace/model-space coupling.

A second control is the weight scale. The `1/p` geometry has total mass only `~log log x`; this is exactly why Halász's generic cancellation mechanism is logarithmic rather than square-root. Changing the weights to force total mass `~log x` would not be a discovery unless the new weights arose canonically from an arithmetic/spectral identity and survived the README's generalized-prime and deformation controls.

A third control is analytic continuation. The prime-power `D_sigma` framework is powerful precisely where its weighted sums are absolutely convergent. A proposal that simply substitutes `sigma=1/2` into those Euler/log-derivative sums without a separate continuation or renormalization theorem fails the line's domain gate.

## Prior-art and novelty audit

The underlying arithmetic theory is established prior art. Halász's mean-value theorem is classical; Granville--Soundararajan developed the explicit pretentious formulation; Koukoulopoulos turned the metric viewpoint into a systematic prime-number tool; Wattanawanichkul's 2026 work extends the metric/logarithmic-derivative mechanism to automorphic zero-free regions.

The exact expression of `D_x` as a weighted chordal distance from `(f(p))_p` to `(p^(it))_p` is an elementary rewrite of the standard definition. Searches around pretentious multiplicative functions, Halász distance, prime phases, Koukoulopoulos metrics, Mertens `3-4-1`, and metric zero-free regions show that describing this as a new geometric invariant would be inappropriate.

The useful research-line contribution is instead the boundary synthesis: the canonical prime-coordinate metric sought by the lattice program already exists and already couples the `log p` Kronecker orbit to arithmetic cancellation, but its generic diameter is `O(log log x)` and its established zero-sensitive prime-power variants operate from `sigma>1`. Neither ingredient supplies a natural square-root/critical-line localization mechanism.

## Consequence for the research line

This finding removes a broad reinvention target. Future work should not spend cycles constructing an arbitrary Euclidean or chordal metric on prime phases and then asking whether distance from the vertical orbit controls cancellation; pretentious multiplicative-function theory is already the canonical realization of that idea.

The surviving target is sharper. An RH-relevant metric mechanism would need an additional structure that changes the scale or the meaning of the distance in a way forced by ordinary zeta: for example a critical renormalization with a proved continuation theorem, an archimedean/self-dual completion that couples the prime metric to `s <-> 1-s`, or a positivity/trace identity whose zero-sensitive term cannot be reproduced by generic multiplicative or automorphic controls.

Combined with `PL-136`, the boundary is especially clear: degree-one global converse rigidity can collapse the ambient phase torus to the zeta point, while pretentious geometry can quantify distance from vertical characters and force PNT-edge cancellation. **The missing RH ingredient is neither phase selection nor a generic prime-phase metric; it is a new global mechanism that converts the selected zeta arithmetic into critical-line positivity or square-root cancellation.**
