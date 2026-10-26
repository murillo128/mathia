# MI-082 — Integer jet rigidity does not supply rational precision

**Evidence level:** supported synthesis of [AF-592](../../findings/AF-592-remote-unit-weight-edits-repair-finite-endpoint-jets.md) and [AF-593](../../findings/AF-593-integer-first-jet-rigidity-does-not-give-a-rational-precision-gap.md), using [AF-591](../../findings/AF-591-matched-prime-endpoints-admit-arbitrarily-many-crossover-minima.md) for the separated crossover depressions. These sources give analytic derivations; no formal verification or independent adversarial approval is asserted. Unique factorization, finite-moment methods and the equal-entropy self-power identity are classical.

Let `S` be a finite nonempty set of ordinary primes and `G` a finite collection of generators greater than one, with unit coefficient per occurrence. The entire finite difference is

\[
H_G(z)=\sum_{g\in G}g^{-1-z}-\sum_{p\in S}p^{-1-z}.
\]

Matching the first regular endpoint jet means matching both reciprocal mass and reciprocal logarithmic moment: `H_G(0)=H_G'(0)=0`. The admissible generator category changes what those two equations imply.

For rational generators, let `v_ell(g)` be the signed prime valuation. Prime-log independence makes the derivative equation equivalent to

\[
\sum_{g\in G}\frac{v_\ell(g)}g
=\frac{\mathbf1_{\ell\in S}}\ell\qquad(\text{every prime }\ell).
\]

If all generators are integers, summing these coordinates and subtracting the mass equation yields

\[
\sum_{g\in G}\frac{\Omega(g)-1}{g}=0,
\qquad \Omega(g)=\sum_\ell v_\ell(g)\ge1.
\]

Every summand is nonnegative, so every generator is prime; the individual valuation equations then force `G=S`, including multiplicities. No equal-cardinality, range or subdyadic assumption is needed. The derivative equation alone does not suffice: `G={9,27}` matches the logarithmic moment of `S={3}` but has the wrong mass.

For a reduced rational `g=a/b`, the same certificate contains `Omega(a)-Omega(b)-1`, which can be negative. Even signed degree one does not identify a prime (`25/3` has that degree). The integer rigidity proof therefore supplies neither rational uniqueness nor rational counterexamples.

The continuous escape is explicit. For each fixed order `m>=1` and supplied derivative vector `(d_1,...,d_m)`, AF-592 moves unit-weight primes in `m+2` separated logarithmic blocks by `p -> exp(theta_i)p`; write `J` for the resulting finite difference. At remote scale `log p ~ T`, the coordinates `A_j=(-1)^j T^(-j) J^(j)(0)` have Jacobian at zero tending to `-M`, where

\[
M_{ji}=\int_{\alpha_i}^{\beta_i}v^{j-1}\,dv,
\qquad 0\le j\le m.
\]

The maximal minors of `M` are positive integrated Vandermonde determinants when the positive intervals are ordered and disjoint. Shifts `theta_i=O_d(T^{-1})` give a simple nonintegral real replacement block with

\[
J(0)=0,\qquad J^{(j)}(0)=d_j\ (1\le j\le m),
\qquad \sup_{z\ge0}|J(z)|=O_d(T^{-1}).
\]

The extra block lets the exact solution avoid integer generators. Unbounded logarithmic factors price the derivatives while the value norm tends to zero. Nonzero prescribed `J(0)` would prevent this. The order and derivative vector are fixed before sending the blocks outward; no bound on edit count or generator range is retained.

Rationalization preserves the mass equation exactly, but only approximates the other jets. In reciprocal coordinates `x_i=1/g_i`, the mass hyperplane `sum x_i=sum_(p in S)1/p` has dense rational points. On a fixed finite source neighborhood, all prescribed derivatives of `sum x_i^(1+z)` vary continuously, uniformly for `z>=0`. Distinctness, nonintegrality and a strict lower generator cutoff also survive sufficiently small perturbations.

Consequently, for every `Y>2`, integers `m,N>=1`, tolerance `delta>0`, `tau_*>0` and `0<eta<3/4`, AF-593 chooses a finite set `S` of primes above `Y` and distinct nonintegral rational replacements `G` above `Y` such that

\[
H_G(0)=0,\qquad \max_{1\le j\le m}|H_G^{(j)}(0)|<\delta,
\]

yet, for `Q(s)=sum_(q in (P\S) union G) q^(-s)`,

\[
F_Q(\tau)=\frac{e^{B_1}}{2\tau}E_1^{-1}(Q(1+2\tau)),
\qquad E_1(a)=\int_a^\infty e^{-t}\,dt/t,
\]

has at least `N` strict local minima below `eta` in `(0,tau_*)`, separated by values above `3/4`. Here `P` denotes the ordinary primes and `B_1` their reciprocal Mertens constant. The real repair first restores the jets without destroying finitely many strict high/low inequalities; rational approximation then preserves those inequalities. The inverse transport uses `d log(E_1^{-1}(w))/dw=-exp(E_1^{-1}(w))` only on fixed positive neighborhoods of those finitely many values, not uniformly on the whole ray.

Thus no positive finite-jet tolerance bounds this turning complexity over the rational class with unrestricted finite edits. This does **not** settle the exact rational jet equations. Both endpoint limits remain `1` and `exp(B_1)log 2`, and the finite Euler factor

\[
Z_Q(s)/\zeta(s)=
\frac{\prod_{p\in S}(1-p^{-s})}{\prod_{g\in G}(1-g^{-s})}
\]

is analytic and nonzero on `Re s>0`. The changing discriminator is crossover shape; all nontrivial zeta zeros and multiplicities remain the same.

The unresolved exact rational problem has an integer certificate. Choose a positive integer `D` divisible by every `p in S` and every reduced numerator of a candidate `g`. With `n_g=D/g` and `r_p=D/p`, exact mass and first derivative matching are equivalent to

\[
\sum_g n_g=\sum_p r_p,\qquad
\prod_g n_g^{n_g}=\prod_p r_p^{r_p}.
\]

For the prefix-preserving class take `S` above `Y>2`. Distinct nonintegral replacements above `Y` require distinct integers `1<=n_g<D/Y` with `n_g` not dividing `D`. All prime factors of each `n_g` must divide `D`; otherwise its nonnegative valuation could not cancel in the product identity. At fixed `S,D,Y` this is a finite zero-one selection problem, checkable through mass and prime valuations without numerical logarithms. Every rational solution appears for some `D`; failure at finitely many denominators cannot prove rigidity. Rational density on the mass hyperplane provides no reason for a rational point to lie on this exact self-power level set.
