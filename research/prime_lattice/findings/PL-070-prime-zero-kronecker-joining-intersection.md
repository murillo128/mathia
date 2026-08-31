# PL-070 — Prime-log/zero-hull Kronecker coupling reduces exactly to cross-frequency intersection

## Claim

The most direct rational-prime coupling left open after `PL-069` can be classified exactly, and the classification is negative for new RH rigidity.

Let

```text
Gamma_P = <log p : p prime>_Z
        = log(Q_{>0})
```

be the prime-log frequency group from `PL-011`. Assume RH and use one of the residual fixed smooth probe pairs from `PL-068`, so that every nontrivial zeta zero is active in the second-scale signal of `PL-067`--`PL-069`. Let

```text
Gamma_Z = <2 gamma : zeta(1/2+i gamma)=0>_Z
```

be the zero-frequency module of `PL-069`.

Write

```text
K_P = dual(Gamma_P),
K_Z = dual(Gamma_Z)
```

with the compact Kronecker rotations induced by real time. Couple the two systems by the **same time parameter**, i.e. take the orbit closure of the diagonal trajectory in `K_P x K_Z`.

Then its entire coupling is controlled by the exact common-eigenfrequency group

```text
Delta = Gamma_P intersect Gamma_Z.
```

More precisely, after the harmless sign convention coming from the opposite Fourier orientations in `PL-011` and `PL-069`, the annihilator of the diagonal orbit closure `H` is

```text
H^perp = {(lambda,lambda) : lambda in Delta}.
```

Consequently

```text
H = K_P x K_Z
    <=>
Gamma_P intersect Gamma_Z = {0}.
```

The same criterion is measure-theoretically sharp: the two Haar Kronecker flows are disjoint, meaning that their only invariant joining is product Haar measure, **if and only if** `Delta={0}`. If `Delta` is nontrivial, Haar measure on the proper diagonal orbit closure `H` is already a nonproduct joining with Haar marginals.

Thus a nontrivial same-time prime/zero coupling exists exactly when there is a finite integer relation

```text
log q = 2 sum_j m_j gamma_j,

q in Q_{>0}, q != 1,
m_j in Z,
```

among a rational-prime log and the ordinates of nontrivial zeta zeros. Approximate coincidences, the density of `log(Q_{>0})` in `R`, and generic recurrence do not create an invariant coupling: exact common eigenvalues are required.

Therefore the route

```text
prime-log Kronecker flow
+ RH zero-hull Kronecker flow
+ canonical same-time product / joining
    -> new rational-prime spectral constraint on the zero hull
```

has only two outcomes:

```text
Delta={0}
    -> the coupling is exactly the independent product;

Delta!={0}
    -> the extra information is precisely an already-present
       finite cross-frequency relation log q = 2 sum m_j gamma_j.
```

The joining construction itself neither produces nor explains such a relation and cannot force `Re(rho)=1/2`; the compact zero hull used here already presupposes RH. The same theorem holds for arbitrary multiplicative frequency groups and arbitrary almost-periodic zero-frequency modules.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE` for the bare same-time Kronecker-joining route. Compact-group rotations, Pontryagin annihilators, and disjointness/joining theory are classical. The line-specific exact contribution is the specialization

```text
Gamma_P = log(Q_{>0}),
Gamma_Z = <2 gamma>_Z,
```

which shows that adding the most canonical prime-flow observable to the `PL-069` zero hull does not create a new interaction invariant: it asks for exact arithmetic relations between two frequency modules.

## Exact diagonal-orbit calculation

The prime flow of `PL-011` acts on a prime character of frequency `lambda in Gamma_P` by

```text
exp(-i lambda t).
```

The zero-hull flow of `PL-069` acts on a zero-hull character of frequency `mu in Gamma_Z` by

```text
exp(+i mu t).
```

(The opposite signs are only Fourier convention; reversing time on one factor gives the equivalent same intersection criterion.)

Characters of `K_P x K_Z` are indexed by pairs

```text
(lambda,mu) in Gamma_P direct_sum Gamma_Z.
```

Along the same-time diagonal orbit, such a character acquires phase

```text
exp(i (mu-lambda) t).
```

It is identically one for all real `t` exactly when

```text
mu=lambda.
```

Hence the annihilator of the diagonal orbit closure is

```text
H^perp
 = {(lambda,lambda):
      lambda in Gamma_P intersect Gamma_Z}.
```

For a closed subgroup of a compact abelian group, trivial annihilator is equivalent to being the whole group. Therefore

```text
H=K_P x K_Z
 <=> H^perp={(0,0)}
 <=> Gamma_P intersect Gamma_Z={0}.
```

This argument is exact and does not assume any linear-independence conjecture for zeta zeros.

## Haar joinings have the same exact obstruction

Let `nu` be any probability joining of the two Haar rotations: its marginals are Haar on `K_P` and `K_Z`, and it is invariant under the same-time product flow.

For a product character `(lambda,mu)`, write its Fourier coefficient as

```text
nu_hat(lambda,mu)
 = integral chi_lambda(x) psi_mu(y) d nu(x,y).
```

Flow invariance gives, for every real `t`,

```text
nu_hat(lambda,mu)
 = exp(i(mu-lambda)t) nu_hat(lambda,mu).
```

Thus

```text
nu_hat(lambda,mu)=0
```

unless `lambda=mu`. If

```text
Gamma_P intersect Gamma_Z={0},
```

all nonconstant Fourier coefficients vanish. Fourier uniqueness on compact abelian groups then forces

```text
nu = Haar_(K_P) tensor Haar_(K_Z).
```

So the systems are disjoint.

Conversely, if `lambda!=0` belongs to the intersection, the diagonal orbit closure `H` above is proper. Its coordinate projections are surjective because each individual Kronecker orbit is dense; therefore Haar measure on `H` has Haar marginals. Since `H` is proper, this Haar measure is a nonproduct invariant joining.

Hence

```text
boxed:
prime and zero Kronecker systems are disjoint
<=> Gamma_P intersect Gamma_Z={0}.
```

This is the standard common-eigenvalue obstruction for Kronecker systems, proved here directly in the exact modules relevant to the line.

## Arithmetic meaning of a common eigenfrequency

Unique factorization gives

```text
Gamma_P
 = {sum_p k_p log p : k_p in Z, finite support}
 = {log q : q in Q_{>0}}.
```

By construction,

```text
Gamma_Z
 = {2 sum_j m_j gamma_j : m_j in Z, finite support}.
```

Therefore a nonzero element of the intersection is exactly a relation

```text
log q = 2 sum_j m_j gamma_j
```

with `q!=1`.

This is materially stronger than either module being dense. `PL-011` already shows that `Gamma_P` is dense in `R`, and a zero-frequency module may also be dense, but two countable dense subgroups of `R` can still have trivial intersection. Ordinary Kronecker approximation only produces near returns. It cannot turn an approximate relation into a nonzero invariant Fourier coefficient of a joining.

The distinction is important for the mesoscopic boundary search: a proposal that couples the `PL-069` hull to the prime torus merely by synchronizing their time variables has no continuous reservoir of weak arithmetic correlations. At the exact invariant level it sees only `Delta`.

## Why this does not supply RH rigidity

There are two independent reasons.

First, `K_Z` in this finding is the compact zero hull produced in `PL-069` **under RH**. Therefore its frequencies `2 gamma` are already real because the zeros were already placed on the critical line by the hypothesis. A joining formed afterward cannot explain why that localization happened.

Second, even within the RH-side information audit, the construction is universal. Given any two countable additive subgroups `A,B subset R`, the same diagonal-orbit and joining argument on `dual(A) x dual(B)` depends only on `A intersect B`. If one replaces the rational primes by a generalized multiplicative frequency system, or replaces the zeta zero ordinates by an arbitrary absolutely summable almost-periodic frequency set, the same criterion remains valid verbatim.

Thus a nontrivial `Delta` would itself be additional arithmetic data requiring an independent theorem. The compact joining does not create that theorem; it packages the exact relation as a common eigenvalue. If `Delta` is trivial, it packages no interaction at all.

## Relation to `PL-011` and `PL-069`

`PL-011` rules out chaotic or mixing RH information in the **bare prime** Kronecker flow: its Koopman spectrum is the pure-point module `log(Q_{>0})`.

`PL-069` rules out new rigidity in the **bare zero** translation hull: under RH its Koopman spectrum is the pure-point module generated by the doubled zero ordinates, and the natural evaluation observable merely restores the explicit-formula Fourier coefficients used to construct it.

The present finding closes their most direct product repair:

```text
prime pure-point system
    x
zero pure-point system
    + synchronize time
        -> common-eigenvalue intersection only.
```

So putting the two canonical compact rotations next to one another does not create a third spectral mechanism. Any genuinely new coupling must leave the bare Kronecker category: for example a nontranslation-equivariant arithmetic operator, a relative/scattering form, a moving noncompact topology, or another construction whose interaction is not determined solely by the two frequency modules.

## Prior-art and novelty audit

The general mechanism is classical ergodic theory, not new mathematics.

- `research/prime_lattice/SOURCES.md` source 22, Peter Walters, *An Introduction to Ergodic Theory* (1982), is already the line's compact-abelian rotation/discrete-spectrum anchor used by `PL-011` and `PL-069`.
- A targeted audit of joining/disjointness literature recovers the standard Furstenberg framework: nonproduct joinings encode common factors, and for Kronecker systems the Fourier/common-eigenvalue calculation above is the elementary classification. No novelty is claimed for disjointness, joinings, Pontryagin annihilators, or the common-eigenvalue theorem.
- A separate audit of current zeta-zero linear-independence literature confirms that even linear-independence properties internal to the zero ordinates are treated conjecturally in modern work. The present result deliberately does **not** assume such a conjecture and does not claim to determine `Delta`.

The durable line-specific result is therefore a negative information audit: the apparently natural way to inject independent rational-prime data into the `PL-069` hull either factorizes completely or reduces to exact cross-frequency relations that the joining formalism itself does not supply.

## Analytic-continuation and falsification audit

No Euler product is analytically continued here. The rational-prime module `Gamma_P` comes from the exact compact prime flow of `PL-011`; the zero module `Gamma_Z` comes from the completed explicit-formula signal already justified in `PL-067`--`PL-069` and is used here only under RH.

The claim has sharp boundaries:

1. It classifies the ordinary same-time compact Kronecker coupling. It does not rule out noncompact, nonstationary, nonunitary, or nontranslation-equivariant couplings.
2. It makes no assertion that `Gamma_P intersect Gamma_Z` is actually trivial or nontrivial for zeta. Either case is allowed.
3. It uses exact invariant joinings. Quantitative finite-time near-joinings or scale-dependent approximate resonances are outside the claim and would need a separate canonical normalization and matched-control test.
4. It does not claim that a newly proved relation `log q=2 sum m_j gamma_j` would be uninteresting. Such a theorem would be genuine extra arithmetic information; the point is that the bare joining does not prove it.
5. It remains valid if zero multiplicities are present: `Gamma_Z` depends on the active ordinates, while multiplicities and amplitudes remain in the evaluation observable as in `PL-069`.
6. It survives Beurling/generalized-prime controls at the structural level: replacing `Gamma_P` by any multiplicative frequency module gives the same intersection criterion.

The decisive falsification test is therefore simple. Any claim that synchronized prime and zero Kronecker rotations possess a nonproduct invariant coupling without a nonzero common eigenfrequency would contradict the Fourier calculation above. Any proposed escape must identify additional structure whose invariant is not a function solely of `Gamma_P`, `Gamma_Z`, and their intersection.

## Consequence for the research line

The bare compact-dynamical route is now closed one step further:

```text
prime torus alone
    -> pure-point rational-log spectrum (`PL-011`);

zero hull alone
    -> pure-point zero-frequency module (`PL-069`);

canonical same-time coupling
    -> exact common-frequency intersection (`PL-070`).
```

A rational-prime-specific mechanism cannot be obtained merely by taking the product, diagonal orbit closure, or invariant joining of those two rotations. The surviving mesoscopic search must use a coupling that changes the information geometry rather than one whose complete invariant is the intersection of two pre-existing frequency modules.
