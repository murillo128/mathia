# VIS-406 — fixed decoder complexity forces a quantitative uniform target component

## Claim

Continue the one-dimensional monotone-decoder setting of `VIS-404`--`VIS-405`. Let

`Q:[0,1] -> I=[a,b]`

be nondecreasing and onto, let `ell=b-a>0`, let `U~Uniform(0,1)`, and let `nu=Q_#Leb_[0,1]`.

`VIS-405` proved that any independently fixed bound `Lip(Q)<=L` implies the exact measure floor

`nu >= L^(-1) Leb_I`,

so a total uniform component of mass at least `ell/L` is mandatory. Several standard finite-complexity decoder restrictions give such an `L` automatically.

### Fixed differentiable basis with a coefficient budget

Suppose

`Q(u)=c_0 + sum_(j=1)^d c_j phi_j(u)`,

where the basis functions are continuously differentiable, `||c||_p<=B`, and `q` is conjugate to `p`. Define

`M_q = sup_(u in [0,1]) ||(phi_1'(u),...,phi_d'(u))||_q < infinity`.

Then Hölder's inequality gives

`Lip(Q) <= B M_q`.

Consequently, whenever `B M_q>0`,

`nu >= (B M_q)^(-1) Leb_I`.

Because `Q` is onto, necessarily `B M_q>=ell`; the forced uniform component has mass at least `ell/(B M_q)`.

### Degree-`n` polynomial decoder

If `Q` is a real polynomial of degree at most `n>=1`, then the classical Markov inequality on `[-1,1]` gives

`Lip(Q) <= n^2 ell`.

Therefore

`nu >= [n^2 ell]^(-1) Leb_I`,

and every such monotone polynomial decoder forces a uniform component of total mass at least `1/n^2`.

### Ordered Bernstein-coefficient decoder

If, more specifically,

`Q(u)=sum_(k=0)^n c_k B_(k,n)(u)`,

with Bernstein basis `B_(k,n)`, endpoint coefficients `c_0=a`, `c_n=b`, and ordered coefficients

`a=c_0 <= c_1 <= ... <= c_n=b`,

then

`Q'(u)=n sum_(k=0)^(n-1) (c_(k+1)-c_k) B_(k,n-1)(u)`.

Hence, writing `Delta=max_k(c_(k+1)-c_k)`,

`Lip(Q) <= n Delta <= n ell`.

Thus

`nu >= (n Delta)^(-1) Leb_I >= (n ell)^(-1) Leb_I`.

The exact coefficient-gap bound forces a uniform component of mass at least `ell/(n Delta)`; the coarser degree/basis statement forces at least `1/n`.

These are **capacity consequences**, not Wang/source-packet estimates. They show that once a representation family and its numerical complexity budget are frozen before target inspection, the abstract regularity requirement in `VIS-405` becomes an explicit observable mass floor.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-INEQUALITY/REPRESENTATION + CONTROL/CAPACITY-CALIBRATION + NO-NOVELTY-CLAIM`.

No Wang-derived degree, coefficient norm, basis derivative norm, Bernstein gap budget, arithmetic anomaly, destination gain, zeta-zero statement, or RH consequence is claimed.

## 1. Fixed basis plus coefficient norm gives a Lipschitz budget

Differentiate the fixed-basis representation:

`Q'(u)=sum_(j=1)^d c_j phi_j'(u)`.

For every `u`, Hölder gives

`|Q'(u)| <= ||c||_p ||phi'(u)||_q <= B M_q`.

Since `Q` is continuously differentiable on `[0,1]`, the mean-value theorem yields

`Lip(Q)<=B M_q`.

Applying `VIS-405` with `L=B M_q` gives

`nu((x,y]) >= (y-x)/(B M_q)`

for every `a<=x<y<=b`, equivalently

`nu >= (B M_q)^(-1) Leb_I`.

This is the generic bridge sought in the current Wang clue: a **fixed representation plus a fixed coefficient budget** becomes a quantitative target-law restriction without inspecting the target. The bound may be loose, and a particular basis family can impose additional structure, but the mass floor follows from these two numbers alone.

The onto condition itself provides a consistency check. Any map from `[0,1]` onto an interval of length `ell` has Lipschitz constant at least `ell`; hence an admitted basis/coefficient budget must satisfy `B M_q>=ell`.

## 2. Polynomial degree alone gives a source-free universal calibration

Let `Q` be a polynomial of degree at most `n`, nondecreasing from `a` to `b`. Put

`p(t)=Q((t+1)/2)-(a+b)/2`,  `-1<=t<=1`.

Because `Q([0,1])=[a,b]`,

`||p||_infinity <= ell/2`.

The classical first-derivative Markov inequality gives

`||p'||_infinity <= n^2 ||p||_infinity <= n^2 ell/2`.

Since

`Q'(u)=2 p'(2u-1)`,

we obtain

`Lip(Q)<=n^2 ell`.

Composing this with `VIS-405` yields the target-independent null

`nu >= [n^2 ell]^(-1) Leb_I`.

The total forced uniform mass is therefore at least `1/n^2`. In degree one the bound is sharp in the strongest possible sense: a monotone onto affine decoder pushes uniform measure to the uniform law on `I`.

This is deliberately only a universal degree control. Particular polynomial parameterizations can be much more restrictive.

## 3. Ordered Bernstein coefficients improve the generic degree floor

For the Bernstein basis

`B_(k,n)(u)=binom(n,k) u^k (1-u)^(n-k)`,

the standard derivative identity is

`Q'(u)=n sum_(k=0)^(n-1) Delta_k B_(k,n-1)(u)`,

where

`Delta_k=c_(k+1)-c_k`.

If the coefficients are ordered, every `Delta_k>=0`. This condition is a **sufficient fixed representation restriction for monotonicity**; it is not claimed to characterize all monotone polynomials written in Bernstein form at a fixed degree.

Because the degree-`n-1` Bernstein basis is nonnegative and sums to one,

`0 <= Q'(u) <= n max_k Delta_k = n Delta`.

Thus

`Lip(Q)<=n Delta`.

The endpoint identities `Q(0)=c_0=a` and `Q(1)=c_n=b` give

`sum_k Delta_k=ell`,

so `ell/n <= Delta <= ell`; the lower bound follows because the maximum of `n` nonnegative gaps is at least their average. Consequently `n Delta>=ell`, as required for an onto decoder.

Applying `VIS-405` now gives the sharper exact capacity implication

`nu >= (n Delta)^(-1) Leb_I`.

Its forced uniform mass is `ell/(n Delta)`, lying between `1/n` and `1`. Forgetting the individual coefficient gaps but keeping only degree and ordered endpoints still gives the valid coarse floor

`nu >= (n ell)^(-1) Leb_I`.

This demonstrates why the **representation budget matters**, not merely the abstract degree. A coefficient geometry can turn the same finite-dimensional decoder class into a stronger falsifiable null.

## 4. What this does and does not buy for the Wang packet clue

`CLUE-wang-fixed-source-packet-localization` asks for a source-free packet control whose admissible nuisance family is fixed independently of the observed qutrit residual. `VIS-404` showed that a fixed uniform latent plus arbitrary monotone transport is universal. `VIS-405` showed that a frozen numerical Lipschitz budget is not universal and is exactly a uniform mass floor.

The present finding closes the next **generic** bridge. One does not need to posit `L` as an unexplained primitive if the source-free mechanism already supplies a fixed finite representation and numerical capacity bound. A basis coefficient norm `B`, a polynomial degree `n`, or ordered Bernstein coefficient gaps immediately produce a predeclared `L` and therefore an exact target-law floor.

What remains load-bearing is specifically Wang/source-packet mathematics: derive one of those complexity budgets, or a stronger decoder restriction, from the packet construction **before** seeing the candidate residual. Nothing here says that the actual Wang decoder is polynomial, has bounded Bernstein gaps, or belongs to any fixed basis family with a target-independent coefficient norm.

Therefore a source analysis that merely chooses a convenient polynomial degree or coefficient budget after inspecting the target would still be circular. The value of this result is to make the missing interface explicit: source mechanism -> frozen representation capacity -> observable residual mass floor.

## 5. Prior art and novelty audit

The ingredients are classical approximation theory and elementary norm inequalities. The first-derivative Markov brothers inequality on `[-1,1]`,

`||p'||_infinity <= n^2 ||p||_infinity`,

is the classical sharp polynomial derivative inequality originating with A. A. Markov. A modern overview of Markov extremal problems is Gradimir V. Milovanovic, **On the Markov extremal problem in the L2-norm with the classical weight functions** (2021), arXiv `2111.01094`; the uniform-norm Markov inequality is treated there as the classical starting point.

For Bernstein polynomials, the derivative-by-forward-differences identity and positivity/partition-of-unity geometry are standard. Useful modern references are Rida T. Farouki, **The Bernstein polynomial basis: A centennial retrospective**, *Computer Aided Geometric Design* 29:6 (2012), 379--419, DOI `10.1016/j.cagd.2012.03.001`, and E. H. Doha, A. H. Bhrawy, M. A. Saker, **On the Derivatives of Bernstein Polynomials: An Application for the Solution of High Even-Order Differential Equations**, *Boundary Value Problems* 2011, 829543, DOI `10.1155/2011/829543`.

No novelty is claimed for Hölder's inequality, Markov's inequality, Bernstein derivative formulas, coefficient-monotonicity sufficiency, or their ordinary approximation-theory consequences. The Mathia-specific result is the exact **capacity calibration obtained by composing those fixed representation bounds with the monotone-transport equivalence in `VIS-405`**: each independently frozen decoder budget yields a mandatory uniform component in the current residual law.

## Boundaries

- The result concerns one-dimensional **monotone** decoders from a fixed uniform latent. It does not characterize non-monotone maps, multidimensional latents, or general neural decoders.
- The fixed-basis statement requires an independently specified basis and coefficient norm budget. Allowing the basis, dimension, or norm bound to depend on the observed target destroys the intended pre-candidate control.
- The degree-`n` polynomial floor is a universal consequence of degree and range only; it need not be sharp for a particular polynomial family.
- Ordered Bernstein coefficients are a sufficient subclass. The `1/n` coarse mass floor is not asserted for every monotone degree-`n` polynomial.
- A decoder family may imply stronger restrictions than the Lipschitz floor. This finding records only what follows through `VIS-405` from the displayed capacity bounds.
- No Wang/source-packet argument in this finding supplies `B`, `M_q`, `n`, or `Delta`. That source-to-capacity step remains unresolved.
- No retained visualization is required because the result is an exact representation-capacity calculation.

## Dependencies

- `VIS-404`: a fixed uniform latent with unrestricted monotone quantile transport remains universal.
- `VIS-405`: a frozen monotone Lipschitz budget is exactly a uniform target-mass floor.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue requiring a pre-candidate source-free decoder/packet restriction.

## Research consequence

The generic decoder-capacity side of the Wang clue is now quantitative. If a source-free packet derivation can justify a fixed basis and `||c||_p<=B`, a degree bound `n`, ordered Bernstein coefficients with bounded gaps, or another representation estimate implying `Lip(Q)<=L`, the resulting residual null is immediately testable through the corresponding `VIS-405` mass floor.

The next coherent research step is therefore narrower: derive such a representation/capacity bound from the actual Wang/source-packet construction, rather than introduce another target-dependent decoder family.