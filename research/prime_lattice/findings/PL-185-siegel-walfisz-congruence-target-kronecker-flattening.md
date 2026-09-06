# PL-185 — Polylogarithmic congruence targets still scalarize under affine Kronecker averaging

## Claim

`PL-184` leaves genuinely high-variation or arithmetically conditioned one-prime targets outside its bounded-variation theorem. The cheapest such arithmetic escape is a periodic target depending on the moving prime modulo a modulus: as a function of `q/X` it can oscillate on roughly `X/m` cells and therefore lies far outside the sub-resolution BV regime even when `m` is fixed.

That escape nevertheless collapses by a different classical input. Fix `A>0`. There exists `d_A>0` such that the following holds uniformly as `X->infinity`. Let

- `2<=m_X<=(log X)^A`;
- `a_X:G_(m_X)->C`, `G_m=(Z/mZ)^*`, with `|a_X(r)|<=1`;
- `h_X>=1`, `t_X in R`;
- `kappa_X=h_X/X` and `nu_X=|t_X|h_X/(X+h_X)`;
- `nu_X<=exp(d_A sqrt(log X))`.

Write

`a_bar_X = (1/phi(m_X)) sum_(r in G_(m_X)) a_X(r)`

and

`B_(X,h,a,m)(t)
 = pi(X)^(-1) sum_(q<=X, q prime, q not dividing m)
     a([q]) exp(i t log(1+h/q))`.

Then

`boxed:
B_(X,h_X,a_X,m_X)(t_X)
 = a_bar_X I_(kappa_X,t_X) + o(1),`

where

`I_(kappa,t)=integral_0^1 exp(i t log(1+kappa/u)) du`

is the same continuum one-point-density profile as in `PL-180`--`PL-184`. The `o(1)` is uniform over the displayed family after `A` is fixed.

Consequently:

1. if `a_bar_X=0`, the congruence-conditioned readout is `o(1)` throughout this phase window;
2. if `nu_X->infinity`, then `B_(X,h_X,a_X,m_X)(t_X)->0` for every bounded residue target, because `PL-182` gives `|I_(kappa,t)|<=2/nu`;
3. at bounded `nu`, the only surviving congruence information is the finite local scalar `a_bar_X`; no nontrivial residue pattern survives the prime average.

This includes fixed-modulus target conditions on the **shifted affine destination**. If `chi` is a Dirichlet character modulo `m`, extended by zero off the units, then

`a_X(r)=chi(r+h_X)`

is an admissible residue target. For a fixed prime modulus `ell`, a nonprincipal character `chi mod ell`, and `ell` not dividing `h`,

`(1/(ell-1)) sum_(r in G_ell) chi(r+h) = -chi(h)/(ell-1)`;

if `ell|h`, the mean is zero. Thus even this explicitly arithmetic shifted-target character retains only an elementary finite local bias before the same continuum Kronecker profile.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION + PRIOR-ART-REDIRECT`. The deep input is the classical Siegel--Walfisz theorem for primes in arithmetic progressions. The weighted conclusion is ordinary Abel/partial summation combined with the already persisted `PL-182` continuum theorem. No novelty is claimed for Siegel--Walfisz, weighted prime sums in progressions, Dirichlet characters, or partial summation. The durable line-specific result is that a genuinely high-variation arithmetic target class explicitly left open by `PL-184` still does not preserve a non-Haar affine invariant at polylogarithmic congruence complexity.

## 1. This target really lies outside the bounded-variation theorem

A nonconstant residue target `a(q mod m)` is not a slowly varying function of `q/X`. If one encodes it as a step function sampled at the integers, its variation across `[1,X]` is generically of order `X/m`, which for fixed or polylogarithmic `m` is much larger than the `X^(13/15-o(1))` variation budget in `PL-184`.

Therefore this is not a disguised application of the previous one-point BV result. The arithmetic condition changes a load-bearing hypothesis: it oscillates on the integer/congruence scale rather than the macroscopic real-variable scale. The correct control is equidistribution of primes among residue classes, not short-interval quadrature against a low-variation weight.

The phase itself remains the canonical affine/Kronecker phase derived in `PL-179`--`PL-182`:

`g_(h,t)(x)=exp(i t log(1+h/x)).`

On every fixed bulk interval `x in [delta X,X]`, `0<delta<1`, its exact derivative satisfies

`|g'_(h,t)(x)| <= C_delta nu/X`,

uniformly in arbitrary `h>=1`, because

`nu=|t|h/(X+h)`

and

`|t|h/[x(x+h)] <= C_delta nu/X`.

Hence

`Var_[delta X,X](g_(h,t)) <= C_delta nu`.

This is the only phase-complexity estimate needed below.

## 2. Siegel--Walfisz kills the centered residue pattern

Set

`c_X(r)=a_X(r)-a_bar_X`,

so that

`sum_(r in G_m) c_X(r)=0`

and `|c_X(r)|<=2`. For

`C_X(y)=sum_(q<=y, q prime, q not dividing m_X) c_X([q])`,

Siegel--Walfisz gives, for every fixed modulus exponent `A`, a constant `c_A>0` such that uniformly for reduced residues and `m_X<=(log X)^A`, after harmlessly increasing the exponent in the theorem to cover all `y in [delta X,X]`,

`pi(y;m_X,r)=Li(y)/phi(m_X)+O_A(y exp(-c_A sqrt(log y))).`

Summing against `c_X(r)` cancels the common main term exactly. Since there are `phi(m_X)` reduced residue classes,

`|C_X(y)|
 <= C_A phi(m_X) y exp(-c_A sqrt(log y))
 <= C_A y (log X)^A exp(-c_A sqrt(log y))`

uniformly on the fixed bulk interval.

Abel summation therefore gives

`|sum_(delta X<q<=X, q prime, q not dividing m_X)
      c_X([q]) g_(h_X,t_X)(q)|
 <= C_(A,delta) X (log X)^A exp(-c'_A sqrt(log X)) (1+nu_X)`

for some `c'_A>0`. Dividing by `pi(X)~X/log X`, the normalized centered contribution is

`O_(A,delta)((log X)^(A+1) exp(-c'_A sqrt(log X)) (1+nu_X)).`

Choose once and for all `d_A` with `0<d_A<c'_A/2`. Then

`nu_X<=exp(d_A sqrt(log X))`

forces this bulk term to be `o(1)`. The discarded primes `q<=delta X` contribute at most

`2 pi(delta X)/pi(X)=2delta+o_delta(1)`

in absolute value. Letting `X->infinity` and then `delta->0` proves

`pi(X)^(-1) sum_(q<=X, q prime, q not dividing m_X)
 c_X([q]) g_(h_X,t_X)(q) = o(1).`

Primes dividing `m_X` are harmless: there are at most `omega(m_X)=O(log log X)` of them, so their normalized contribution tends to zero.

The argument permits `a_X` itself to vary arbitrarily with `X`; only the uniform bound `|a_X|<=1` and the polylogarithmic modulus bound are used. It also permits `h_X` to grow arbitrarily, because the exact phase parameter `nu_X` already absorbs all source-growth regimes from `PL-182`.

## 3. The uncentered part is only the old continuum profile

The decomposition

`a_X([q]) = a_bar_X + c_X([q])`

now gives

`B_(X,h,a,m)(t)
 = a_bar_X B_(X,h)(t) + o(1),`

where `B_(X,h)(t)` is the unweighted prime average from `PL-182`; excluding the finitely many primes dividing `m_X` changes it by `o(1)`.

Because

`exp(d_A sqrt(log X)) = X^(o(1)),`

the present phase window lies eventually inside every fixed polynomial window `nu_X<=X^(13/15-eta)` with `0<eta<13/15`. Therefore `PL-182` applies and yields

`B_(X,h_X)(t_X)=I_(kappa_X,t_X)+o(1).`

Combining the two estimates proves the claim.

The conclusion is stronger than saying that a fixed congruence mask has a density. The mask is allowed to change with `X`, its modulus may grow like any fixed power of `log X`, and its real-variable variation can be enormous. Nevertheless, within the corresponding Siegel--Walfisz phase-resolution band, all of its detailed residue structure is annihilated by prime equidistribution and only its average over `G_m` remains.

## 4. Shifted Dirichlet characters show what arithmetic survives

Take a Dirichlet character `chi mod m` and define the target relative to the affine destination `q+h` by

`a_h(r)=chi(r+h)`

for `r in G_m`, with the usual extension `chi(x)=0` when `(x,m)>1`. This is an especially natural test because it depends on the **target integer** created by the additive coupling, not merely on the source prime label.

The theorem gives

`pi(X)^(-1) sum_(q<=X, q prime, q not dividing m)
 chi(q+h) exp(i t log(1+h/q))
 = a_bar_h I_(h/X,t)+o(1),`

where

`a_bar_h=(1/phi(m)) sum_(r in G_m) chi(r+h).`

For prime `m=ell` and nonprincipal `chi`, the complete character sum over `F_ell` is zero. If `h` is nonzero modulo `ell`, deleting the single source residue `r=0` gives

`sum_(r in G_ell) chi(r+h)
 = sum_(x mod ell, x!=h) chi(x)
 = -chi(h),`

while `h=0 mod ell` gives zero. Hence the surviving scalar is a purely finite local congruence bias. It is not a shifted-prime factorization statistic, a Dirichlet-`L` zero contribution, or a new holonomy of the exponent lattice.

This example is useful adversarially: arithmetic target dependence can survive one-point averaging in the weak sense of a local residue bias, but that survival is completely classified before any analytic continuation or RH-sensitive object enters.

## 5. Prior art and novelty audit

The number-theoretic input is classical.

- **A. Walfisz**, “Zur additiven Zahlentheorie II,” *Mathematische Zeitschrift* **40** (1936), 592–607, DOI `10.1007/BF01218882`, is the classical source associated with the Siegel--Walfisz theorem. In its standard modern formulation, for every fixed `N` there is `c_N>0` such that uniformly for `(a,q)=1` and `q<=(log x)^N`, `pi(x;q,a)=Li(x)/phi(q)+O_N(x exp(-c_N sqrt(log x)))`; the constant is ineffective because of Siegel's theorem.
- **Jesse Thorner, Asif Zaman**, “Refinements to the prime number theorem for arithmetic progressions,” *Mathematische Zeitschrift* **306** (2024), Paper 54, DOI `10.1007/s00209-023-03414-3`, gives a modern theorem strong enough to recover Siegel--Walfisz among its corollaries and is a current audit anchor for uniform prime distribution in progressions.

A targeted literature search for weighted Siegel--Walfisz statements found no reason to treat the present weighted conclusion as a new analytic-number-theory theorem. Once the cumulative progression estimate is available, multiplying by a bounded phase of controlled total variation and applying Abel summation is standard. The exact exponent `d_A` is intentionally not optimized and is not presented as a new resolution constant.

The line-specific novelty boundary is relative to `PL-184`: **high real-variable variation caused by fixed or polylogarithmic congruence oscillation is not enough to escape one-point-density scalarization.** `PL-114` had already shown that fixed congruence pair kernels scalarize by finite character Fourier analysis, and `PL-171` had already realized periodic/Dirichlet channels inside the affine `ax+b` operator algebra. The present result does not re-claim those facts; it closes the different moving-prime/Kronecker target branch that remained open after `PL-184`.

## 6. Matched control and analytic boundary

No analytic continuation is used. The proof remains entirely on the prime-counting side and never forms an Euler product or evaluates zeta in the critical strip. Consequently the result supplies no mechanism for locating zeta zeros.

The appropriate matched control is any labeled point system that has the same uniform equidistribution among reduced residue classes up to polylogarithmic moduli and the same unweighted continuum quadrature for the phase. The same centering and partial-summation argument then produces the same scalar mean. Rational primes furnish the classical Siegel--Walfisz theorem, but the resulting observable discards the detailed arithmetic once that theorem is applied.

This also explains why the critical line is absent. The phase window `exp(d_A sqrt(log X))` is dictated by the error term in a prime-number theorem for arithmetic progressions. It is a theorem-technology resolution scale, not a spectral constant, and nothing special occurs at `Re(s)=1/2`.

## 7. Boundaries and failure modes

The following regimes remain outside the finding.

1. **Larger moduli.** A prescribed modulus growing faster than every fixed power of `log X` is not covered by Siegel--Walfisz. Bombieri--Vinogradov controls averages over moduli and does not automatically give the same pointwise statement for an adversarially selected growing modulus.
2. **Higher phase resolution.** The theorem only needs, and only claims, a subexponential phase window `nu<=exp(d_A sqrt(log X))`. The larger `X^(13/15-o(1))` phase window of `PL-181`--`PL-184` comes from short-interval prime counting without congruence conditioning; it cannot simply be imported into arithmetic progressions.
3. **Nonperiodic arithmetic targets.** Factorization data such as `lambda(q+h)`, `mu(q+h)`, squarefreeness of `q+h`, or conditions involving large prime factors do not factor through a polylogarithmic residue label and are not covered.
4. **Joint moving-prime relations.** Conditions coupling two or more independently moving primes, or nonlocal target transport, are outside this one-prime periodic theorem.
5. **A local bias is allowed.** The result does not say every arithmetic target has zero average. It says the readout retains only the finite reduced-residue mean times the universal continuum profile. Treating that explicitly computable local bias as an RH-sensitive survivor would be a category error.
6. **No effective numerical threshold is asserted.** The classical Siegel--Walfisz constant is ineffective; only existence of a positive `d_A` is used.

## Decisive audit test

To falsify the main statement, it is enough to fix `A>0` and show that for every admissible `d_A>0` there exist sequences `m_X<=(log X)^A`, bounded residue targets `a_X`, arbitrary `h_X>=1`, and phases with `nu_X<=exp(d_A sqrt(log X))` for which

`B_(X,h_X,a_X,m_X)(t_X)-a_bar_X I_(h_X/X,t_X)`

does not tend to zero.

The proof has only two load-bearing bridges: the uniform Siegel--Walfisz bound for the centered residue-class counting function and the exact bulk phase-variation estimate `Var(g)<=C_delta nu`. Once the centered term is removed, the remaining unweighted term is exactly the `PL-182` theorem. An objection must therefore identify a failure in one of those bridges or in the limit order that discards `q<=delta X`.

## Consequence for the research line

The accepted affine non-Haar clue should no longer count **fixed or polylogarithmic periodic/congruence conditioning**, even when attached to the shifted destination `q+h`, as a live high-variation arithmetic escape inside the Siegel--Walfisz phase band. This is a genuinely different no-go from `PL-184`: the target can have macroscopic total variation, but its arithmetic oscillation is still homogenized because it factors through a small finite quotient of the integers.

A surviving target-relative branch must therefore use arithmetic complexity not exhausted by polylogarithmic congruence labels, such as nonperiodic factorization of the shifted target, a prescribed larger-modulus regime with independently justified distribution estimates, joint/non-product prime relations, or a nonlocal/completed carrier that changes the averaging law before residue-class and one-point-density scalarization.