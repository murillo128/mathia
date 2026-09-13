# VIS-197 — same-sign gap fibers have an explicit finite local conductor and only polylogarithmic local inflation

## Claim

Continue the fixed normalized same-sign near-collision regime of `VIS-196`. Fix a sign and write

`d=g d_0`, `e=g e_0`, `gcd(d_0,e_0)=1`,

`m=+/- h/g != 0`,

so that the gap-balance equation is

`d_0 r-e_0 p=m`.

Choose one integer solution `(p_0,r_0)`. The corresponding four affine forms are

`L_1(t)=p_0+d_0 t`,

`L_2(t)=p_0+d_0(t+g)`,

`L_3(t)=r_0+e_0 t`,

`L_4(t)=r_0+e_0(t+g)`.

Put

`D=d_0 e_0`

and define the integer

`Q=d_0 e_0 g m (m^2-g^2 D^2)`.

There are two structurally different cases.

### Nondegenerate case: `Q != 0`

For every prime `ell` not dividing `Q`, all four forms have nonzero slope modulo `ell` and their four zero residues are distinct. Thus, if `nu_ell` denotes the number of residue classes `t mod ell` on which at least one `L_i(t)` vanishes, then

`nu_ell=4`

for every `ell` not dividing `Q`.

Equivalently, every departure from the generic four-root local geometry is supported on the finite set of prime divisors of `Q`.

For a prime-realized `VIS-196` fiber — one containing an actual top-scale parameter value for which all four `L_i(t)` are prime and exceed `3` — the system is automatically locally admissible. Its classical Hardy–Littlewood/Dickson local-density product

`S(L)=prod_ell (1-nu_ell/ell)(1-1/ell)^(-4)`

therefore converges to a positive value. Moreover

`S(L) << (|Q|/phi(|Q|))^4`

with an absolute implied constant, and hence

`S(L) << (1+log log(3+|Q|))^4`.

In the fixed-`A` normalized crowding regime of `VIS-195`--`VIS-196`, `h` ranges over a finite set and `g|h`, so `g` and `m=h/g` are `O_A(1)`. Since `d_0,e_0<=y`,

`|Q|=O_A(y^6)`.

Consequently every nondegenerate dangerous fiber satisfies the uniform local-factor bound

`S(L) <<_A (1+log log(3+y))^4`.

Thus **local congruence amplification cannot by itself produce a power-scale obstruction** to the desired subquadratic weighted crowding estimate. Any remaining power-scale difficulty must come from how many gap fibers occur, how long their parameter ranges are, and how the actual taper weights aggregate across them, not from an uncontrolled singular-series explosion on one fiber.

### Degenerate case: `Q=0`

Because `d_0,e_0,g,m` are nonzero, degeneracy means

`m=+/- gD`.

On a prime-realized top-scale fiber this forces

`d_0=e_0=1`.

If `m=gD`, then `L_2=L_3` on the prime realization and the three distinct primes form

`p, p+g, p+2g`.

If `m=-gD`, then `L_1=L_4` and the three distinct primes form the reflected three-term progression

`p-g, p, p+g`.

In either case `h=g^2`. Since all three primes are greater than `3`, necessarily `6|g`, hence `36|h`. The degenerate branch is therefore a finite family of fixed-shift three-prime progressions for each fixed crowding multiplier `A`; it does not carry a growing four-form local conductor.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL PRIME-TUPLE LOCAL-FACTOR FRAMEWORK + ARITHMETIC-REDUCTION + NO-NOVELTY-CLAIM`.

No coefficient-uniform upper-bound sieve for the aggregate over `(d,e)` is proved here, and no improvement of `D_v=o(y^2)` is claimed.

## 1. The four local roots form a translated residue parallelogram

Assume first that `ell` does not divide `d_0 e_0`. Let

`alpha=-p_0 d_0^(-1) mod ell`,

`beta=-r_0 e_0^(-1) mod ell`.

The zero residues of the four forms are

`alpha`, `alpha-g`, `beta`, `beta-g`.

Because

`d_0 r_0-e_0 p_0=m`,

one has

`beta-alpha=-m(d_0 e_0)^(-1) mod ell`.

After translating by `-alpha`, the entire local root pattern is therefore

`{0,-g,-u,-u-g}`,

where

`u=m D^(-1) mod ell`.

This makes the collision geometry explicit. The four residues fail to be distinct only when at least one of

`g=0`, `u=0`, `u=g`, `u=-g`

holds modulo `ell`. Multiplying by the invertible `D` shows that these are exactly the congruence conditions

`ell | g`,

`ell | m`,

`ell | (m-gD)`,

`ell | (m+gD)`.

If `ell` divides `d_0 e_0`, it is already included in the exceptional set because it divides `Q`. Hence every prime outside `Q` sees exactly four distinct bad residues.

The same conclusion can be expressed by the six pairwise affine resultants. Up to sign, they are

`d_0^2 g`, `e_0^2 g`, `m`, `m`, `m+gD`, `m-gD`.

So `Q` is only a compact square-free-support carrier for the slopes and pair-resultant primes relevant to this specific four-form system. No new general discriminant or sieve invariant is being introduced.

## 2. Prime-realized fibers are admissible

Take a parameter value `t_*` from the `VIS-196` top-scale collision that generated the fiber, so all four values `L_i(t_*)` are primes greater than `3`.

For `ell=2` or `3`, the residue `t_* mod ell` makes none of the forms vanish. Therefore

`nu_ell<ell`.

Now let `ell>=5`. If no form is identically zero modulo `ell`, each nonconstant affine form contributes at most one bad residue, so

`nu_ell<=4<ell`.

It remains only to rule out an identically zero form. If, for example, `L_1` is identically zero modulo `ell`, then `ell|d_0` and `ell|p_0`. But `L_2-L_1=g d_0`, so `L_2` is identically zero as well. At `t_*`, both distinct primes `L_1(t_*)` and `L_2(t_*)` would then be divisible by `ell`, forcing both to equal `ell`, impossible because their positive gap is `d=g d_0`. The same argument applies to the `L_3,L_4` pair.

Thus no prime covers every parameter residue, and the fiber is admissible.

This statement is deliberately modest. It does not predict infinitely many prime points on the fiber; it only records the exact absence of a local congruence obstruction for a fiber already known to contain the prime point that instantiated it.

## 3. Exceptional-prime inflation is controlled by `Q/phi(Q)`

For an admissible nondegenerate fiber define

`beta_ell=(1-nu_ell/ell)(1-1/ell)^(-4)`.

For `ell>=5` with `ell` not dividing `Q`, Section 1 gives `nu_ell=4`, so the generic factor is

`b_ell=(1-4/ell)(1-1/ell)^(-4)`.

The product

`C_4=prod_(ell>=5) b_ell`

converges to a positive constant because

`log b_ell=O(ell^(-2))`.

For an exceptional prime `ell>=5`, admissibility implies that no form is identically zero, hence `0<=nu_ell<=4`. Therefore

`1 <= beta_ell/b_ell`

and

`beta_ell/b_ell <= (1-4/ell)^(-1)`.

Separating the two small primes gives the exact factorization

`S(L)=beta_2 beta_3 C_4`

`     * prod_(ell>=5, ell|Q) [(1-nu_ell/ell)/(1-4/ell)]`.

The small-prime factor `beta_2 beta_3` is bounded by an absolute constant. For `ell>=5`,

`(1-4/ell)^(-1)`

` = (1-1/ell)^(-4) * [(1-1/ell)^4/(1-4/ell)]`.

The product of the bracketed ratios over all `ell>=5` converges, again because its logarithm is `O(ell^(-2))`. Hence

`S(L) << prod_(ell|Q) (1-1/ell)^(-4)`

`     = (|Q|/phi(|Q|))^4`.

The classical Mertens/totient bound

`n/phi(n) << 1+log log(3+n)`

then yields the stated polylogarithmic estimate.

This is only a bound on the local-density product. It does not replace the upper-bound sieve required to count prime values of the four affine forms uniformly as their coefficients vary.

## 4. The zero-conductor branch is exactly a three-prime progression

Suppose

`m=gD`.

Then the cross resultant between `L_2` and `L_3` vanishes identically, giving

`e_0 L_2(t)=d_0 L_3(t)`

for every `t`.

At a prime realization, write `q=L_2(t_*)` and `r=L_3(t_*)`. Since `gcd(d_0,e_0)=1`,

`e_0 q=d_0 r`

implies `d_0|q` and `e_0|r`. But `d_0=d/g<q`, because `d=q-p<q`, so primality forces `d_0=1`. The displayed proportionality then forces `e_0=1` and `q=r`. The four forms reduce to the three shifts

`p`, `p+g`, `p+2g`.

The case `m=-gD` is symmetric: the vanishing cross resultant is between `L_1` and `L_4`, and primality forces `d_0=e_0=1` and `p=s`, leaving the reflected three-term progression.

Since `|m|=h/g` and `|m|=g` in this branch,

`h=g^2`.

For three primes greater than `3` in arithmetic progression, parity gives `2|g`, while reduction modulo `3` forces `3|g`; otherwise the three terms occupy all residue classes modulo `3` and one is divisible by `3`. Hence `6|g` and `36|h`.

For a fixed normalized crowding multiplier `A`, `VIS-195` allows only finitely many fixed `h`. Thus this degenerate family consists of finitely many fixed prime-triplet patterns and can be separated from the coefficient-growing four-form branch before any uniform sieve estimate.

## Prior-art audit

The local-density formalism is classical. The generalized Hardy–Littlewood/Dickson framework for affine-linear prime patterns assigns exactly such products of local factors; Ben Green and Terence Tao, **Linear equations in primes**, *Annals of Mathematics* 171:3 (2010), 1753–1850, DOI `10.4007/annals.2010.171.1753`, is a modern authoritative formulation of these local factors. Their theorem does **not** settle the present one-parameter four-prime system: the paper explicitly excludes affinely related/binary-type systems from its general theorem. It is used here only as prior-art authority for the local-factor language.

Henryk Iwaniec and Emmanuel Kowalski, **Analytic Number Theory**, AMS Colloquium Publications 53 (2004), DOI `10.1090/coll/053`, is a standard reference for elementary sieve local densities and upper-bound sieve methods. The classical Mertens product estimate already anchored in `research/visual_exploration/SOURCES.md` supplies the standard `n/phi(n) << log log n` consequence used above.

A targeted search by affine prime tuples, local factors, singular series, and coefficient-dependent linear forms found the general sieve/Hardy–Littlewood machinery but no reason to treat the specialized integer `Q` above as a new invariant. It is simply the product, for the `VIS-196` forms, of the slope primes and the primes dividing pairwise resultants. The exact evaluation of those resultants and the resulting Mathia-specific reduction are derived here; **no novelty is claimed for the general local-density, resultant, singular-series, or sieve principles**.

## Boundaries and falsification

The four-form singular-series statement applies only to the nondegenerate branch `Q!=0`. The branch `Q=0` has a repeated cross form at prime realizations and must be treated as the three-form progression isolated in Section 4.

The quantity `S(L)` is a local arithmetic density product. A polylogarithmic bound on it does not prove a comparable count of prime parameter values without a sieve theorem whose constants and error terms are uniform in the varying coefficients and in the parameter interval relevant to `VIS-196`.

The argument uses the fixed-`A` consequence of `VIS-195`: `h` belongs to a finite set independent of `y`, and `g|h`. If the normalized crowding multiplier is allowed to grow with `y`, then `g`, `m`, and the bound `|Q|=O_A(y^6)` must be revisited.

The result controls local congruence amplification fiber by fiber. It does not control the number of possible gap pairs `(d,e)`, the overlap between fibers, or the taper-weighted coefficient mass placed on them.

Falsify the finding by finding a prime `ell` not dividing `Q` for which the four local roots are not distinct, an identically-zero form on a prime-realized top-scale fiber, an error in the exceptional-factor decomposition, a nondegenerate admissible fiber whose singular series violates the displayed `Q/phi(Q)` bound, or a `Q=0` prime realization that does not reduce to the stated three-term progression.

## Research consequence

`VIS-196` reduced dangerous same-sign crowding to one-parameter four-prime fibers. The present result removes a second possible source of uncontrolled growth: their local congruence geometry is generic at every prime outside an explicit finite conductor, and the entire exceptional singular-series amplification is at most polylogarithmic in `y` for fixed normalized crowding scale.

The remaining quantitative frontier is therefore sharper. A useful next theorem should give a **coefficient-uniform upper-bound sieve for the parameter values on the nondegenerate fibers and then sum those bounds with the actual taper weights over `(d,e,h)`**. The finite three-prime-progression branch can be separated first. Any argument that loses a power of `y` solely through the singular series is using substantially less of the gap-fiber structure than is now available.