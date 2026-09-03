# PL-138 — Power-sensitive pretentious metrics are classical transfer geometries, not a source of RH-scale cancellation

## Claim

A natural repair to the `PL-137` obstruction is to strengthen the prime-torus metric by replacing the classical `1/p` weight with a heavier radial weight and, if necessary, to include prime powers. This route is already established prior art. Jung and Lemke Oliver introduced, for `beta in (0,1]`,

`D_beta(f,g)^2 = sum_p (1-Re(f(p) conjugate(g(p))))/p^beta`,

and a stronger prime-power distance

`Dhat_(beta,k)(f,g) = sum_p sum_(j=1)^k |f(p^j)-g(p^j)|/p^(j beta)`.

For unitary completely multiplicative prime phases `f(p)=exp(i theta_p)` and `g(p)=exp(i phi_p)`, the first is exactly the weighted prime-torus chordal geometry

`D_beta(f,g)^2 = (1/2) sum_p |exp(i theta_p)-exp(i phi_p)|^2 exp(-beta log p)`.

Thus the most immediate scale-sensitive reweighting of prime coordinates by the log-prime energy is not new. It genuinely detects power cancellation better than ordinary Halasz distance, but the proved mechanism is a **relative transfer theorem**: it transfers a cancellation exponent already known for a comparator `f` to a sufficiently close `g`. It does not create the comparator's cancellation, analytically continue an Euler product into the critical strip, or supply a zeta-specific positivity principle.

For completely multiplicative `f,g`, Jung--Lemke Oliver prove that if

`S_f(x) << x^alpha`

and `D_beta(f,g)<infinity`, then

`S_g(x) << x^max(alpha,(1+beta)/2)`.

They also prove an optimality statement showing that the `(1+beta)/2` barrier is genuine for this notion of distance in the complex completely multiplicative class. Since every fixed `beta>0` gives `(1+beta)/2>1/2`, this prime-only metric does not itself single out square-root cancellation. The RH-style exponent `1/2+epsilon` can only be approached by choosing `beta` correspondingly small, so the half exponent is not generated as an intrinsic metric threshold.

Their stronger prime-power distance removes that particular floor for finite-degree multiplicative functions: if `f,g` lie in their class `S_d`, `Dhat_(beta,d)(f,g)<infinity`, and `S_f(x)<<x^alpha`, then

`S_g(x) << x^max(alpha,beta)`.

This is mathematically stronger and is directly relevant to the exponent lattice because it samples the axis rays `j e_p`, not only the first prime layer `e_p`. But the logical direction remains transfer: one must already possess the power cancellation of `f`. The metric does not manufacture an RH-scale reference function from prime-exponent geometry.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE/OBSTRUCTION`.

No novelty is claimed for pretentious distances, power-cancellation transfer, strong pretentiousness, or the prime-power refinement. The durable `prime_lattice` consequence is a falsification boundary: simply changing the radial weights of the prime torus, or adding finitely many prime-power rays, does not by itself provide the missing RH mechanism. A surviving metric proposal must explain where the reference square-root cancellation or equivalent positivity comes from and why that input is specific to ordinary zeta rather than a broad multiplicative-function control class.

## Exact prime-lattice geometry of the beta distance

For unitary completely multiplicative functions, write

`f(n)=exp(i <v(n),theta>)`, `g(n)=exp(i <v(n),phi>)`.

At a prime coordinate,

`1-Re(f(p) conjugate(g(p))) = (1/2)|exp(i theta_p)-exp(i phi_p)|^2`.

Therefore

`D_beta(f,g)^2 = (1/2) sum_p |exp(i theta_p)-exp(i phi_p)|^2 p^(-beta)`.

Since `p^(-beta)=exp(-beta log p)`, the parameter `beta` is exactly an exponential radial damping in the same energy coordinate `log p` that defines the prime-exponent lattice. This is a canonical-looking family of geometries from the viewpoint of the current mandate: the coordinate phases are Pontryagin-dual to the exponent directions and the radial weight is a function of the log-prime energy.

The important limitation is that `beta` is a free analytic parameter. The abstract lattice does not select a distinguished positive `beta`, and the transfer theorem does not produce `beta=1/2` from a self-duality or spectral condition. In fact, for the prime-only theorem the output floor is `(1+beta)/2`, so the square-root exponent is only a limiting endpoint as `beta downarrow 0`, outside the stated `beta>0` metric family.

This differs from the finite-truncation issue corrected in `PL-137`. There the dangerous object was an unrestricted minimum over the full Kronecker orbit at fixed `x`, which degenerates to zero by density. Here `D_beta(f,g)` is a global infinite-prime distance to a **fixed comparator** `g`; no minimization over all vertical times is involved. The two obstructions are separate.

## The classical distance really is too weak for power cancellation

Jung--Lemke Oliver start from the standard Granville--Soundararajan distance and show why ordinary pretentiousness does not directly preserve power savings. They construct a multiplicative function that remains pretentious to a character while having partial sums `>> x/log x` infinitely often. Their introduction explicitly notes that quantitative Halasz-type theorems are essentially unable to detect cancellation below `x log log x/log x` and motivates stronger notions for power cancellation.

Their first replacement is `D_beta`. The completely multiplicative case of Theorem 1.1 states

`S_g(x) << x^max(alpha,(1+beta)/2)`

whenever `S_f(x)<<x^alpha` and `D_beta(f,g)<infinity`. The theorem's optimality clause is load-bearing for the audit: when `beta>=2 alpha-1`, there exists a completely multiplicative `f'` that is `beta`-pretentious to `f` but whose partial sums are not

`O(x^((1+beta)/2-epsilon))`

for any `epsilon>0`. Thus the exponent barrier is not merely a weakness of one estimate that can be ignored when importing this metric into prime-torus language.

For general multiplicative functions the theorem has additional hypotheses, including convergence of a small-prime correction series and the stated `sigma>3/4` restriction. Those hypotheses must not be erased by quoting only the cleaner completely multiplicative specialization.

Primary source:

- Junehyuk Jung, Robert J. Lemke Oliver, “Pretentiously detecting power cancellation,” *Mathematical Proceedings of the Cambridge Philosophical Society* **154**(3) (2013), 481–498. DOI: https://doi.org/10.1017/S0305004112000655. arXiv: https://arxiv.org/abs/1111.1921. Theorem 1.1 gives the `D_beta` transfer and optimality; Theorems 1.3--1.4 give the strong prime-power version.

## Prime-power strong pretentiousness reaches below the square-root barrier, but only relatively

To treat general multiplicative functions and more-than-square-root cancellation, Jung--Lemke Oliver define

`Dhat_(beta,k)(f,g) = sum_p sum_(j=1)^k |f(p^j)-g(p^j)|/p^(j beta)`.

In exponent coordinates the terms `p^j` are exactly the lattice points `j e_p`. This is therefore an established example in which a genuinely stronger arithmetic metric uses more of each prime axis than the first layer seen by classical pretentious distance.

For the class `S_d` of multiplicative functions that are Dirichlet convolutions of `d` bounded completely multiplicative functions, Theorem 1.4 says that finiteness of `Dhat_(beta,d)(f,g)` transfers

`S_f(x)<<x^alpha`

to

`S_g(x)<<x^max(alpha,beta)`.

This matters adversarially because it prevents an overstatement: weighted pretentious geometry is not intrinsically stuck above square-root cancellation. With a sufficiently strong prime-power notion and a comparator already known to cancel at exponent `alpha`, the theorem can preserve that exponent whenever `beta<=alpha`.

But precisely that conditional structure is the obstruction for the RH program. To use this as an explanation of square-root-scale cancellation for a zeta-related multiplicative function, one must provide a comparator whose partial sums already enjoy the relevant square-root-scale bound and prove strong closeness to it. The metric theorem then transports the difficult input; it does not derive that input from the prime lattice. Choosing `beta=1/2` by hand likewise does not explain why the Riemann self-dual axis should be `1/2`.

## Analytic-domain audit

The paper's proofs do not justify continuing an Euler product by formal substitution. A basic step is the Dirichlet-convolution factorization

`g=f*h`, hence `L(s,g)=L(s,f)L(s,h)`

in a region where the corresponding series are controlled. Bounds on `S_f` provide analyticity of `L(s,f)` in a right half-plane, while the pretentious hypotheses yield convergence/analyticity for the correction factor `L(s,h)` in another right half-plane. Perron-type arguments then return partial-sum bounds.

This is legitimate analytic number theory, but it is conceptually different from the missing continuation problem for the zeta Euler product. The metric controls convergence of a **relative correction** once a reference function and its cancellation are given. It does not define a continuation of `product_p(1-p^(-s))^(-1)` through `Re(s)=1`, nor does it locate the zeros of that continuation.

## Matched controls and novelty audit

The central literature result applies to broad classes of multiplicative functions. Nothing in `D_beta` uses the Riemann functional equation, the archimedean gamma factor, Weil positivity, or the rational-prime additive structure beyond the ordinary prime indexing and weights. The strong distance similarly measures finitely many prime-power values for functions in a broad finite-degree class.

That breadth is exactly why these results are useful as a control for `prime_lattice`. They show that a geometrically appealing radial prime metric can have real arithmetic force while still failing to distinguish the Riemann zeta problem. The correct lesson is not that metric geometry is useless; it is that **metric closeness is a stability mechanism, not a source mechanism**.

The closest persisted finding is `PL-137`, which handles the standard `1/p` distance, the bounded-time log-prime orbit geometry required by quantitative Halasz estimates, and PNT-edge prime-power zero-free metrics. The present result is distinct: it audits the obvious next move of strengthening the radial weights specifically to detect power cancellation and records the classical transfer thresholds and their optimality.

Searches around `beta`-pretentiousness, strong pretentiousness, power cancellation, and modern pretentious multiplicative-function literature did not reveal a later theorem converting these relative metrics into a zeta-specific RH localization principle. That absence is not a novelty claim; the positive mathematics stored here is the 2013 prior art and the elementary exponent-lattice translation.

## Adversarial limits

Several stronger conclusions would be invalid.

First, this finding does **not** prove that every weighted prime metric is incapable of participating in an RH proof. Jung--Lemke Oliver analyze specific relative distances and function classes. A new metric coupled to an independent zeta-specific positivity or trace identity could behave differently.

Second, the strong prime-power theorem can transfer cancellation below `x^(1/2)` in suitable classes. It would be false to claim that pretentious methods have an absolute square-root barrier. The narrower statement is that the transfer theorem presupposes the reference cancellation and therefore does not explain its origin.

Third, RH-strength estimates are normally of `x^(1/2+epsilon)` type for every `epsilon>0`, not necessarily an exact `O(sqrt x)` bound. The prime-only `D_beta` theorem can approach that exponent by taking arbitrarily small positive `beta`, provided the required relative hypotheses and a sufficiently good comparator are already available. This again demonstrates transfer, not an intrinsic selection of the half exponent.

Finally, the weight `p^(-beta)` is natural analytically but not uniquely forced by exponent-lattice geometry. Treating a visually distinguished choice of `beta` as a discovery would merely move the arbitrary parameter into the metric.

## Consequence for the research line

After `PL-137`, the next metric proposal should not be “replace `1/p` by a stronger `p^(-beta)` weight so that the prime torus has enough mass to see power cancellation,” nor simply “add the prime-power rays.” Both ideas have theorem-level classical realizations.

A surviving metric mechanism must supply something these relative theories deliberately assume: a canonical zeta-specific reference state, positivity, self-dual completion, trace identity, or other global structure that **generates** square-root-scale cancellation rather than merely preserves it under a chosen notion of closeness. It must also explain why its critical normalization is forced and why the same construction does not work unchanged for broad multiplicative or generalized-prime controls.