# PL-071 — Adaptive finite-horizon prime/zero character resonances are Diophantine-universal

## Claim

The finite-time approximate-resonance escape left explicitly open by `PL-070` is nonselective at the level of prime/zero **character correlations**.

Let

```text
Gamma_P = <log p : p prime>_Z = log(Q_{>0})
```

be the signed prime-lattice Koopman frequency group from `PL-011` and `PL-070`. Fix any finite set of real target frequencies

```text
F={mu_1,...,mu_m} subset R
```

—not necessarily zeta-zero frequencies—and write

```text
Lambda=<F>_Z.
```

For every observation horizon `T>=1` and every `0<eta<=1`, there is a group homomorphism

```text
phi_(T,eta): Lambda -> Gamma_P
```

such that, for every `mu_j in F`,

```text
|mu_j-phi_(T,eta)(mu_j)| <= eta/T.
```

Moreover the approximating prime-lattice characters can be chosen with only logarithmic weighted exponent complexity. If

```text
ell_P(log(a/b))
 = sum_p |v_p(a)-v_p(b)| log p
```

for coprime positive integers `a,b`, then

```text
ell_P(phi_(T,eta)(mu_j))
 <= C_F (log T + log(1/eta) + 1),
```

where `C_F` depends only on the fixed finite frequency pattern and the choice of a `Z`-basis of `Lambda`.

Consequently the normalized same-time character correlation

```text
C_T(mu_j,phi(mu_j))
 = (1/T) integral_0^T
     exp(i(mu_j-phi(mu_j))t) dt
```

satisfies

```text
|C_T(mu_j,phi(mu_j))|
 >= sin(eta/2)/(eta/2)
 >= 1-eta^2/24.
```

Thus **every fixed finite real frequency pattern can be shadowed over an arbitrarily long finite time window by signed rational-prime lattice characters, while preserving all of the target pattern's exact integer relations and using weighted lattice radius only `O_F(log T)`**.

In particular, under RH one may take `mu_j=2 gamma_j` from the `PL-069` zero hull. But nothing in the construction uses zeta, zeros, the explicit formula, or the critical line. The same finite-horizon coherence occurs for an arbitrary chosen set of real frequencies.

**Evidence/status:** `CLASSICAL-APPROXIMATION + EXACT-DERIVED + DECISIVE-NEGATIVE` for the route

```text
finite observation horizon
+ T-dependent choice of prime-lattice characters
+ near-unit prime/zero character correlations
    -> rational-prime / RH rigidity.
```

This finding does **not** classify general finite-time near-joinings or moving Weil operators. It closes the bare adaptive character-resonance mechanism that `PL-070` left outside its exact invariant-joining theorem.

## Quantitative approximation by signed prime-lattice frequencies

The quantitative statement is more elementary than the full Dirichlet approximation theorem.

Fix a real number `nu` and put

```text
x=exp(nu)>0.
```

Given a desired logarithmic error `epsilon in (0,1]`, choose an integer denominator `b` with

```text
b >= max(1/x, 1/(epsilon x)).
```

Let `a` be the nearest integer to `b x`. Then `a>=1` and

```text
|a/b-x| <= 1/(2b).
```

Hence

```text
|(a/b)/x-1|
 <= 1/(2 b x)
 <= epsilon/2.
```

Because `epsilon<=1`, the ratio `(a/b)/x` lies in `[1/2,3/2]`. On this interval the logarithm is `2`-Lipschitz, so

```text
|log(a/b)-nu|
 = |log((a/b)/x)|
 <= 1/(b x)
 <= epsilon.
```

After reducing `a/b`, the rational value is unchanged and its height can only decrease. Since `b=O_nu(1/epsilon)` and `a<=b x+1/2`, one has

```text
H(a/b)=max(a,b)=O_nu(1/epsilon).
```

Unique factorization now turns this ordinary rational approximation into an exact signed exponent-lattice statement. For reduced `a/b`, define

```text
k(a/b)=v(a)-v(b) in Z^(P),

log(a/b)=<k(a/b),(log p)_p>.
```

The positive and negative prime supports are disjoint, and therefore

```text
sum_p |k_p(a/b)| log p
 = log a + log b
 <= 2 log H(a/b)
 = O_nu(log(1/epsilon)+1).
```

Taking `epsilon` proportional to `1/T` gives a `1/T` frequency approximation inside `Gamma_P` at weighted exponent radius only `O(log T)`.

The stronger classical context is Dirichlet's theorem on Diophantine approximation: for every real `theta` and `Q>1`, there are coprime integers `p,q`, `0<q<Q`, with `|q theta-p|<=1/Q`. A standard source is Alan Baker, *A Concise Introduction to the Theory of Numbers*, Chapter 6, Cambridge University Press (1984; online 2012), DOI `10.1017/CBO9781139171601.008`. The present height bound does not need that stronger theorem; nearest-integer rational approximation already suffices.

## Relation-compatible approximation of a finite frequency pattern

A finitely generated subgroup of `R` is torsion-free and hence free abelian. Choose a `Z`-basis

```text
nu_1,...,nu_r
```

of `Lambda=<F>_Z`. Write

```text
mu_j = sum_(l=1)^r c_(j,l) nu_l,

c_(j,l) in Z,
```

and put

```text
A=max(1, max_j sum_l |c_(j,l)|).
```

Apply the previous approximation independently to each basis frequency with

```text
epsilon = eta/(A T).
```

This gives

```text
lambda_l=log q_l in Gamma_P,

|nu_l-lambda_l| <= eta/(A T),

ell_P(lambda_l)
 <= C_F (log T+log(1/eta)+1).
```

Define the homomorphism `phi_(T,eta)` by

```text
phi_(T,eta)(nu_l)=lambda_l
```

and extend `Z`-linearly. Then

```text
|mu_j-phi(mu_j)|
 <= sum_l |c_(j,l)| |nu_l-lambda_l|
 <= eta/T.
```

Because `phi` is a group homomorphism, every exact integer relation already present among the target frequencies is preserved. If

```text
sum_j d_j mu_j=0,
```

then automatically

```text
sum_j d_j phi(mu_j)=0.
```

The map need not be injective; it may introduce additional accidental relations. No injectivity is needed for the negative result. A mechanism that requires a canonical injective identification, fixed prime support, or some stronger arithmetic compatibility lies outside this theorem.

For the lattice complexity, subadditivity gives

```text
ell_P(phi(mu_j))
 <= sum_l |c_(j,l)| ell_P(lambda_l)
 <= C_F (log T+log(1/eta)+1).
```

Thus the whole fixed finite pattern can be shadowed without paying a lattice radius proportional to `T`. The cost is only logarithmic in the observation horizon.

## Finite-time correlation cannot distinguish the shadow

For two real frequencies `mu,lambda`, direct integration gives

```text
(1/T) integral_0^T exp(i(mu-lambda)t) dt

 = exp(i(mu-lambda)T/2)
   sin((mu-lambda)T/2)/((mu-lambda)T/2).
```

Therefore if

```text
|mu-lambda| <= eta/T,
```

then, for `0<eta<=1`,

```text
|C_T(mu,lambda)|
 >= sin(eta/2)/(eta/2)
 >= 1-eta^2/24.
```

For any prescribed correlation tolerance one may choose `eta` once and then let `T` grow. At every horizon, a new signed prime-lattice character of weighted radius `O(log T)` shadows the target character to that tolerance.

This is exactly the finite-frequency resolution scale of a length-`T` Fourier observation. The prime lattice is not revealing a relation with the target frequency: its signed character group is simply rich enough to place an adaptive frequency inside the `1/T` resolution cell around any prescribed real number.

## Application to the `PL-070` prime/zero coupling

Under RH, `PL-069` gives the zero-hull frequency module generated by real frequencies `2 gamma`, and `PL-070` proves that an **exact invariant** same-time joining with the prime Kronecker system exists only through the exact intersection

```text
Gamma_P intersect Gamma_Z.
```

That exact result remains untouched.

What fails is the most immediate finite-time relaxation. Given any fixed finite set of zero ordinates and any observation horizon `T`, the theorem above produces prime frequencies

```text
lambda_j in log(Q_{>0})
```

with

```text
|2 gamma_j-lambda_j| <= eta/T
```

and hence near-unit pairwise time correlations. The construction also preserves every integer relation among the selected zero frequencies because it is defined on their finitely generated frequency module.

But the same statement holds if the `2 gamma_j` are replaced by arbitrary real numbers chosen by hand. Therefore

```text
large finite-time prime/zero character correlation
```

is not evidence of a zeta-specific prime/zero coupling, even if the allowed prime-lattice complexity grows only logarithmically with the observation time.

This strengthens the information audit of `PL-070`: exact common frequencies would be genuine extra arithmetic data, whereas adaptive `1/T`-near common frequencies are automatic.

## Prime-lattice geometry of the approximation cost

The relevant geometry is the **signed** exponent lattice because Koopman characters of the prime torus are indexed by

```text
Z^(P),
```

not only by the positive integer cone `N_0^(P)`.

For a rational approximant `a/b`, the vector

```text
v(a)-v(b)
```

has energy

```text
< v(a)-v(b), log p > = log(a/b)
```

and weighted `l^1` radius

```text
sum_p |v_p(a)-v_p(b)| log p = log a+log b.
```

The theorem therefore says geometrically that a slab of energy thickness `O(1/T)` around **any fixed real energy** contains a signed exponent-lattice point at radius `O(log T)`.

This is a property of the rational logarithm group itself, not of the zeta divisor. It is exactly why finite-window phase matching loses the exact-intersection rigidity seen by invariant joinings.

The distinction with the positive cone matters. This finding does not assert that the set `{log n:n in N}` can approximate an arbitrary fixed real frequency to `1/T` as `T` grows. The automatic shadowing uses ratios of integers, hence positive and negative prime exponents, because that is the full frequency group of the compact prime Kronecker flow studied in `PL-011` and `PL-070`.

## Prior-art and novelty audit

No novelty is claimed for any of the general ingredients:

- density and elementary rational approximation in `Q` are classical;
- Dirichlet's stronger rational approximation theorem is classical and is documented in the Baker reference above;
- finitely generated torsion-free abelian groups are free;
- the finite-time correlation of two exponentials is the elementary sinc kernel;
- the signed prime character group is already identified as `log(Q_{>0})` in `PL-011` and `PL-070`.

A targeted literature check around Diophantine approximation and finite-frequency resonance found the general approximation machinery as classical, not a zeta-specific theorem. Exact wording linking it to the `PL-070` prime/zero character coupling is not treated as novelty evidence.

The durable line-specific content is a **negative specialization/information audit**: the finite-time escape explicitly left open by `PL-070` is automatic for any fixed finite target frequency pattern as soon as one is allowed to choose `T`-dependent signed prime characters. The quantitative `O(log T)` exponent-radius estimate makes the obstruction robust against the objection that the approximating lattice vectors might require exponentially large geometric complexity.

## Matched-control and adversarial audit

The strongest control is that the target frequencies are arbitrary. The construction does not inspect whether a target is a zeta zero ordinate, a generalized-prime zero, a random real number, or a manually prescribed frequency. Hence success of the bare correlation test cannot distinguish the rational-prime/zeta pair from a fake target spectrum.

Several possible overclaims are explicitly excluded:

1. **No exact relation is produced.** For fixed `T`, `phi(mu)` is only within `O(1/T)` of `mu`. Letting the approximant depend on `T` does not imply `mu in Gamma_P`.
2. **No invariant joining is produced.** `PL-070` remains the exact classification of invariant same-time Kronecker joinings. A large finite-window character correlation is not an invariant probability joining with Haar marginals.
3. **The target set is fixed and finite.** The constants depend on `F`. A number of zero frequencies growing with `T`, uniform control over an infinite zero module, or a moving spectral window requires new estimates.
4. **The approximating prime characters are adaptive.** They are chosen after the target frequencies and horizon are known. A canonical prime observable fixed independently of the zero data is not covered.
5. **Prime support may move with `T`.** The rational approximants can use new primes as the height grows. Fixed-prime-support or sharply sparse-support approximations are different Diophantine problems.
6. **Only signed lattice characters are covered.** Positive-semigroup constraints can restore rigidity and must be analyzed separately if a proposed construction really has no access to inverse prime directions.
7. **Internal integer relations are preserved, but injectivity is not guaranteed.** A mechanism that needs a faithful embedding of the finite target module into the prime module is stronger than pairwise or relation-compatible finite-window resonance.
8. **RH is not derived.** Applying the result to real zero frequencies uses the RH-side zero hull of `PL-069`. Off-line zeros would introduce growth/decay rather than a unitary real-frequency character; that distinction is already part of the second-scale boundedness mechanism analyzed in `PL-067`--`PL-068`.

These boundaries identify what a surviving finite-time coupling would have to add: target-independent selection, growing/infinite frequency control, constrained prime support, noncharacter amplitudes, a positive-cone restriction, or another structure not erased by `1/T` Fourier resolution.

## Analytic-continuation audit

No Euler product and no prime Dirichlet series is continued here.

The prime side uses only the exact character group

```text
Gamma_P=log(Q_{>0}),
```

which follows from unique factorization. The approximation theorem is elementary real/rational approximation. The finite-time correlation identity is an exact integral.

When the target frequencies are chosen to be doubled zeta-zero ordinates, they enter only through the already-continued completed explicit-formula hull established in `PL-067`--`PL-069`, and only under RH so that those frequencies are real. The present finding adds no analytic-continuation claim.

## Consequence for the research line

The compact-dynamical branch now separates cleanly into exact and finite-horizon regimes:

```text
exact invariant prime/zero coupling
    -> only Gamma_P intersect Gamma_Z (`PL-070`);

adaptive finite-horizon character coupling
    -> automatic 1/T shadowing for arbitrary targets (`PL-071`).
```

Therefore the next useful coupling cannot merely relax exact common eigenfrequencies to approximate common eigenfrequencies while allowing the lattice character to vary with the observation horizon. That move destroys the arithmetic discriminator before any RH mechanism appears.

A surviving mesoscopic construction must impose additional structure that prevents this adaptive Diophantine shadowing—for example a prime-side observable fixed independently of the zeros, a moving family whose target dimension grows fast enough to defeat finite-pattern approximation, a support/complexity constraint stronger than weighted radius `O(log T)`, or a genuinely non-Kronecker operator/form coupling. Those possibilities remain open and are not claimed here.