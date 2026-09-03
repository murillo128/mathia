# PL-137 — Pretentious distance is a canonical weighted prime-torus geometry, but quantitative Halász control is bounded-time and stops at mean-value/PNT-edge scales

## Claim

For a completely multiplicative function `f` with `|f(p)|=1` at every prime, write

`f(p)=exp(i theta_p)`,

so that in prime-exponent coordinates

`f(n)=exp(i <v(n),theta>)`.

For fixed `x` and real `t`, the standard prime sum

`D_x(f,n^(it))^2 = sum_(p<=x) (1-Re(f(p)p^(-it)))/p`

is exactly

`D_x(f,n^(it))^2 = (1/2) sum_(p<=x) |exp(i theta_p)-exp(i t log p)|^2/p`.

Thus pretentious multiplicative-function theory supplies a canonical arithmetic geometry on the finite prime torus: a `1/p`-weighted chordal distance from the phase point `(f(p))_(p<=x)` to the log-prime Kronecker trajectory `(p^(it))_(p<=x)`.

The quantitative Halász parameter relevant at finite scale is **not** the unrestricted distance to the full trajectory. Granville--Soundararajan use

`M(x,T)=min_(|t|<=2T) D_x(f,n^(it))^2`,

so the correct geometric object is distance to a **bounded-time orbit segment**, with an analytic cutoff/location tradeoff. Their explicit completely-multiplicative corollary gives a main factor of order `(M+O(1))e^(-M)` together with `O(1/T + log log x/log x)`; the preceding Halász--Montgomery--Tenenbaum formulation has the related error `O(T^(-1/2))`.

This cutoff is load-bearing. Because the finitely many numbers `{log p:p<=x}` are rationally independent over `Q`, Kronecker's theorem makes the unrestricted trajectory dense in the finite prime torus. Hence for every unitary prescribed prime phase vector,

`inf_(t in R) D_x(f,n^(it))^2 = 0`.

The unrestricted full-orbit infimum is therefore geometrically meaningful only as a density statement; it is **not** the nontrivial finite-scale cancellation parameter.

Even after this correction, the established pretentious mechanism does not naturally reach the RH scale. For every cutoff `T`,

`M(x,T) <= 2 sum_(p<=x) 1/p = 2 log log x + O(1)`.

Therefore the exponential distance term alone can provide at best polylogarithmic normalized decay, not the `x^(-1/2+epsilon)` scale associated with an RH-strength Mertens estimate. Prime-power pretentious metrics used for zero-free regions repair the loss of prime-power data but live initially in `sigma>1`, where logarithmic-derivative expansions are absolutely convergent, and support PNT-edge zero repulsion rather than a continuation/localization mechanism for `Re(s)=1/2`.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE/OBSTRUCTION`.

No new theorem is claimed. The torus rewrite, Kronecker-density correction, and diameter bound are elementary consequences of standard definitions and unique factorization. The durable value is to identify an established arithmetic geometry that matches the line's prime-coordinate/log-prime-flow language almost exactly, while recording the two quantitative gates that prevent the standard distance-only mechanism from being mistaken for an RH mechanism: unrestricted finite-truncation density makes the full-orbit infimum zero, whereas the theoremically relevant bounded-time distance has total mass only `O(log log x)`.

## Exact exponent-lattice interpretation

Unique factorization gives

`f(n)=product_p f(p)^(v_p(n)) = exp(i <v(n),theta>)`.

The vertical character is

`n^(it)=exp(it log n)=exp(i t <v(n),(log p)_p>)`,

so its prime coordinates form the Kronecker curve

`gamma_x(t)=(exp(i t log p))_(p<=x)`.

For unit complex numbers `z,w`,

`1-Re(z conjugate(w))=(1/2)|z-w|^2`.

Consequently the standard prime sum is literally the weighted squared chordal distance from the prime-phase point to `gamma_x(t)`. The pairing with the exponent lattice is exact: the same prime phases determine the character `f(n)` on every lattice point.

This geometry lives on the Pontryagin-dual prime coordinates, rather than directly on the positive cone. It is nevertheless a substantially stronger benchmark than inventing an arbitrary Euclidean metric on exponent vectors: it is the metric already used by multiplicative-number-theory machinery.

## Why the unrestricted orbit distance degenerates at fixed truncation

Fix `x` and enumerate the primes `p_1,...,p_r<=x`. If

`q_1 log p_1 + ... + q_r log p_r = 0`

with rational `q_j`, clearing denominators and exponentiating gives a multiplicative relation among distinct primes. Unique factorization forces every coefficient to vanish. Hence the frequencies `log p_j` are rationally independent.

Kronecker approximation therefore implies that

`t -> (exp(i t log p_1),...,exp(i t log p_r))`

is dense in the finite torus `T^r`. For every unitary completely multiplicative `f`, every `epsilon>0`, and fixed `x`, there is a sufficiently large `|t|` with

`D_x(f,n^(it))^2 < epsilon`.

Thus

`inf_(t in R) D_x(f,n^(it))^2=0`.

This resolves an apparent paradox in the abstract-level shorthand sometimes used for Halász theory. The asymptotic theorem may discuss whether `f` resembles a fixed vertical character, but a finite prime truncation cannot use an unrestricted orbit minimization as a positive quantitative separation parameter: arbitrarily long times eventually approximate every finite phase vector.

## The quantitative Halász geometry is a bounded orbit segment

Granville and Soundararajan define, in equation (1.2),

`M(x,T)=min_(|t|<=2T) sum_(p<=x) [1-Re(f(p)p^(-it))]/p`,

for `x>=3` and `T>=1`. The Halász--Montgomery--Tenenbaum estimate quoted immediately afterward is

`|x^(-1) sum_(n<=x) f(n)| << (1+M)e^(-M) + O(T^(-1/2))`.

Their Theorem 1 refines the constants through the associated truncated Euler product, and Corollary 1 gives, for completely multiplicative `f`,

`|x^(-1) sum_(n<=x) f(n)| <= (M+12/7)e^(gamma-M) + O(1/T + log log x/log x)`.

All of these statements use the same bounded-frequency parameter `M(x,T)`. The paper subsequently tracks the location of a minimizing frequency and develops hybrid estimates that penalize large `|t|`; this is exactly the information lost by collapsing the trajectory to its full dense closure.

Primary literature anchor:

- Andrew Granville and K. Soundararajan, “Decay of Mean Values of Multiplicative Functions,” *Canadian Journal of Mathematics* **55**(6) (2003), 1191--1230. DOI: https://doi.org/10.4153/CJM-2003-047-0. Equation (1.2), the Halász--Montgomery--Tenenbaum estimate, Theorem 1, Corollary 1, and the subsequent hybrid bounds make the time cutoff/location dependence explicit.

The corrected lattice interpretation is therefore:

`prime phases -> distance from a bounded segment of the log-prime flow -> mean-value cancellation, with a cutoff/location error`.

That bridge is classical and quantitative. It is not a distance from the entire Kronecker orbit at fixed prime truncation.

## Quantitative obstruction to RH-scale cancellation from the standard distance term

For every prime and every `f,t`,

`0 <= 1-Re(f(p)p^(-it)) <= 2`.

Therefore, uniformly in `T`,

`M(x,T) <= 2 sum_(p<=x) 1/p = 2 log log x + O(1)`.

This is a diameter bound for every bounded-time orbit-segment problem: restricting the available times can make the minimum nonzero, but cannot increase it beyond the total `1/p` mass.

The principal function `(1+M)e^(-M)` is decreasing for positive `M`. Even at the largest possible order of `M`, it has only polylogarithmic size, roughly

`(log log x)/(log x)^2`

up to constants and the theorem's auxiliary errors. By contrast, RH-strength Mertens cancellation would require

`sum_(n<=x) mu(n)=O_epsilon(x^(1/2+epsilon))`,

or normalized size `O_epsilon(x^(-1/2+epsilon))`. Producing that scale from an exponential term `e^(-M)` alone would require `M` of order `log x`, impossible for the standard `1/p` metric.

The conclusion is deliberately narrow: **the standard bounded-time Halász distance term by itself cannot certify RH-scale square-root cancellation**. This does not exclude stronger cancellation for special functions, nor does it exclude pretentious inputs as one component of a different argument.

## Prime-only information loss and prime-power repair

For general multiplicative functions the standard distance looks only at primes, so it is a pseudometric if prime-power values are allowed to vary independently. Möbius and Liouville give the simplest control:

`mu(p)=lambda(p)=-1`

for every prime, while

`mu(p^2)=0`, `lambda(p^2)=1`.

The prime-only distance cannot see this difference. For unitary completely multiplicative functions this issue disappears because prime values determine all prime powers; it reappears for Möbius and for logarithmic derivatives, whose arithmetic skeleton occupies every lattice point `k e_p`.

Koukoulopoulos formalized classical zero-free-region arguments using pretentious metrics `D_sigma` for `sigma>1`. Wattanawanichkul's 2026 extension to automorphic `L`-functions makes the prime-power/logarithmic-derivative form explicit: the squared metric sums differences of local logarithmic-derivative coefficients over prime powers with weights proportional to `log N(p)/N(p)^(k sigma)`. It can be rewritten using logarithmic derivatives of Rankin--Selberg `L`-functions and yields standard zero-free regions, including the Riemann-zeta `3-4-1` mechanism as a specialization.

Relevant sources:

- Dimitris Koukoulopoulos, *The Distribution of Prime Numbers*, Graduate Studies in Mathematics **203**, American Mathematical Society, 2019.
- Nawapan Wattanawanichkul, “A metric approach to zero-free regions for L-functions,” *European Journal of Mathematics* **12** (2026), Article 30, published 6 July 2026. DOI: https://doi.org/10.1007/s40879-026-00913-5.

The domain distinction remains load-bearing. These logarithmic-derivative metric sums are set up for `sigma>1`, where the relevant Euler/Dirichlet expansions converge. The analytic continuation of the underlying `L`-functions is separate input used to turn inequalities into zero-free regions. One cannot simply substitute `sigma=1/2` into the prime-power series and call the result a critical-line metric.

## Adversarial controls

The most important falsification control is now internal to the torus picture itself. At fixed prime truncation, the full log-prime orbit is dense, so an unrestricted minimum contains no separation information for unitary phases. Any proposed finite-dimensional prime-torus metric must specify the time/frequency window or another compactness/regularization mechanism before interpreting distance from the orbit quantitatively.

The second control is the weight scale. The `1/p` geometry has total mass `~log log x`, explaining why the generic Halász distance term can only produce logarithmic-strength normalized decay. Reweighting the coordinates to manufacture total mass `~log x` is not a mechanism unless the weights arise canonically from a proved arithmetic/spectral identity and survive the line's deformation/generalized-prime controls.

The third control is analytic continuation. Prime-power `D_sigma` methods have real zero-exclusion content near the PNT edge, but start in their honest half-plane of convergence. A proposed critical-line version needs an independent continuation or renormalization theorem plus a reason that the resulting object retains metric/positivity properties.

Finally, pretentious theory is deliberately broad: analogous geometries apply to many multiplicative and automorphic objects. The existence of a metric, triangle inequality, or log-prime orbit therefore does not distinguish ordinary zeta. An RH mechanism needs additional zeta-specific global structure, such as the completed functional equation together with positivity, Hodge structure, or a trace/model-space coupling that constrains the zero divisor.

## Prior-art and novelty audit

Halász mean-value theory, the Granville--Soundararajan pretentious formulation, Koukoulopoulos's metric methods, Kronecker approximation, and the 2026 automorphic zero-free-region extension are prior art. No priority claim is made for the chordal rewrite or for the bounded-time correction.

The useful synthesis for `prime_lattice` is the matched boundary. The canonical prime-coordinate geometry sought by the lattice program already exists and couples the same frequencies `log p` to arithmetic cancellation. But at finite truncation its entire orbit is dense, so quantitative cancellation requires a bounded-frequency window; and once that correct window is imposed, the metric's total mass remains only `O(log log x)`. Its established prime-power variants reach zero-free regions from `sigma>1`, not RH localization.

This finding complements `PL-136`. Degree-one global converse rigidity can collapse the ambient unimodular phase torus to the zeta point. Pretentious geometry then quantifies bounded-frequency proximity to vertical characters and controls mean values/PNT-edge phenomena. **The missing RH ingredient is neither phase selection nor a generic prime-phase metric: it is a global mechanism that converts the selected zeta arithmetic into critical-line positivity or square-root cancellation.**

## Consequence for the research line

Future work should not construct another arbitrary distance on the prime torus and ask whether distance from the full Kronecker orbit controls cancellation. At finite prime level that full-orbit distance is identically zero on unitary phase points, while classical pretentious theory already provides the correct bounded-time version.

A surviving metric route would need genuinely new structure: for example a canonical critical renormalization with a proved continuation theorem, an archimedean/self-dual completion coupling the prime metric to `s <-> 1-s`, or a positive trace/formula whose zero-sensitive contribution cannot be reproduced by generic multiplicative or automorphic controls. Any such proposal must preserve the time/frequency localization explicitly rather than hiding it behind unrestricted Kronecker density.