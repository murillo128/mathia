# PL-032 — LogPrime persistent homology is classical, and its exact barcode has universal `log 2` lifetime

## Claim

The persistent-topology route suggested by the energy filtration of the square-free prime-exponent lattice is already very close to classical prior art, and its remaining persistent module admits an exact elementary classification.

Let

```text
Delta_X = { F finite set of primes : product_(p in F) p <= X }
```

for `X>=1`. Under `F <-> v(product F)`, this is the square-free sector of the prime-exponent energy down-set

```text
sum_(p in F) log p <= log X.
```

Pakianathan and Winfree explicitly introduced the same construction as the `LogPrime` quota complex, with vertex weights `log p`, studied its topology as the quota varies in the language of persistent homology, proved the general minimal-weight shell theorem for scalar quota complexes, and recovered the Mertens/RH Euler-characteristic criterion. Björner independently supplies the equivalent square-free divisibility complex and its static Betti formula.

More strongly, for the closed filtration `Delta_X` the **entire reduced persistent homology is exactly determined**. For every odd square-free integer

```text
b = product_(p in F) p > 1,
```

with `r=Omega(b)=|F|`, there is one persistence interval in reduced homological degree `r-1`,

```text
[b, 2b)
```

in the multiplicative `X` parameter, equivalently

```text
[log b, log b + log 2)
```

in logarithmic energy. There are no other reduced bars.

Thus every positive-degree/reduced-`H_0` class has the **same logarithmic lifetime `log 2`**. Equivalently, for `1<=X<=Y`, over any field,

```text
rank im(
  Htilde_k(Delta_X) -> Htilde_k(Delta_Y)
)
 = #{ b odd square-free :
        Omega(b)=k+1,
        Y/2 < b <= X }.
```

In particular,

```text
Y >= 2X
    -> Htilde_k(Delta_X) -> Htilde_k(Delta_Y) is the zero map
```

for every `k>=0`.

This strengthens the static shell description in `PL-022`: not only are the Betti numbers at scale `X` supported by the multiplicative shell `(X/2,X]`; **each individual homology class is born at an odd square-free integer `b` and is killed exactly when the simplex obtained by adjoining the prime `2` enters at `2b`.**

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION` for the route

```text
canonical square-free log-prime filtration
    -> persistent homology lifetimes / long bars
    -> new critical-line or zero-ordinate mechanism.
```

The LogPrime quota complex, its persistent-homology framing, the minimal-weight shell theorem, and its RH-equivalent Euler characteristic are literature. The filtered chain-basis decomposition and resulting exact interval formula below are derived here. A targeted novelty search found the very close Pakianathan–Winfree prior art but did not locate the exact `[b,2b)` barcode statement; because the derivation is an elementary filtered refinement of their shell collapse, **no novelty claim is made for the barcode formula**.

## Prior art: the persistent LogPrime complex already exists

Pakianathan and Winfree define a scalar quota complex `X[w:q]` by assigning positive weights to vertices and including a face when the sum of its vertex weights is below the quota. They explicitly frame the variation with `q` as a persistent-homology/Morse-type problem.

Their general theorem says that if `v_min` has minimum weight, a scalar quota complex is homotopy equivalent to a bouquet with one sphere for each face `F` not containing `v_min` whose weight lies in the shell

```text
q - w(v_min) <= w(F) < q.
```

They then introduce `LogPrime(q)` with vertices the rational primes and

```text
w(p)=log p.
```

A face `F` corresponds to the square-free integer `n=product_(p in F)p`, and its weight is `log n`. Hence, modulo their strict-quota endpoint convention,

```text
LogPrime(log X) = Delta_X.
```

The minimum-weight vertex is `2`, so their shell has fixed logarithmic width `log 2`. They also prove

```text
chi(LogPrime(q))
    = - sum_(2 <= n < exp(q)) mu(n)
```

and recover the classical Mertens growth criterion equivalent to RH. Therefore both the logarithmic prime weights and the idea of following this topology through the filtration are prior art, not a new prime-lattice construction.

Primary source:

- Jonathan Pakianathan and Troy Winfree, *Quota Complexes, Persistent Homology and the Goldbach Conjecture*, arXiv:1104.4324v3 (2011); journal version: *Threshold complexes and connections to number theory*, Turkish Journal of Mathematics 37 (2013), 511–539, DOI `10.3906/mat-1112-14`.

The static identification with the square-free exponent complex and the Betti shell count are also consistent with Anders Björner, *A cell complex in number theory*, Advances in Applied Mathematics 46 (2011), 71–85, already recorded in `PL-022`.

## Exact filtered chain decomposition

Use the closed filtration `Delta_X`; changing to the strict quota convention only changes endpoint bookkeeping, not the lifetime or the persistence maps away from event values.

Let `F={p_1,...,p_r}` be a nonempty finite set of **odd** primes and write

```text
b(F)=product_(p in F) p.
```

Orient the simplex

```text
u_F = [2,p_1,...,p_r].
```

Its filtration value is

```text
fil(nu_F)=2 b(F).
```

Define the one-degree-lower chain

```text
z_F = boundary(nu_F).
```

Expanding the boundary gives

```text
z_F
 = +/- [p_1,...,p_r]
   + sum_i +/- [2,p_1,...,hat(p_i),...,p_r].
```

The first term has filtration value `b(F)`. Every other term has filtration value

```text
2 b(F)/p_i < b(F)
```

because every `p_i` is odd. Consequently

```text
fil(z_F)=b(F),
fil(nu_F)=2 b(F),
boundary(nu_F)=z_F,
boundary(z_F)=0.
```

Now fix chain degree `k`. Every standard `k`-simplex is uniquely of one of two forms:

```text
F                    with F odd and |F|=k+1,
{2} union G           with G odd and |G|=k.
```

Replace the first family by `{z_F}` and keep the second family as `{nu_G}`. Since

```text
z_F = +/- F + terms of strictly smaller filtration,
```

the change of basis is triangular with diagonal entries `+/-1`; it is therefore unimodular and filtration-preserving, with filtration-preserving inverse. In this basis the reduced differential is simply

```text
boundary(nu_F)=z_F,
boundary(z_F)=0.
```

Apart from the usual augmentation pair associated with the vertex `2`, the reduced filtered chain complex therefore splits as the direct sum, over nonempty odd prime sets `F`, of two-term filtered complexes

```text
<nu_F>  --1-->  <z_F>,

fil(z_F)=b(F),
fil(nu_F)=2b(F).
```

Over any field this is already the interval decomposition of the persistence module. The class represented by `z_F` is born when `X=b(F)` and dies when its unique paired filling simplex `nu_F` enters at `X=2b(F)`. Hence the barcode is exactly

```text
{ [b,2b) :
    b odd square-free,
    b>1 },
```

with the bar for `b` placed in degree `Omega(b)-1`.

The same basis works integrally; the field assumption is needed only for standard barcode language, not for the chain decomposition itself.

## Persistent ranks and the factor-two nilpotence

A bar `[b,2b)` contributes to the image from scale `X` to scale `Y>=X` exactly when

```text
b <= X
and
Y < 2b.
```

Thus in degree `k`,

```text
rank im(
  Htilde_k(Delta_X) -> Htilde_k(Delta_Y)
)
 = #{ b odd square-free :
        Omega(b)=k+1,
        Y/2 < b <= X }.
```

Setting `Y=X` recovers Björner's/Pakianathan–Winfree's shell formula

```text
beta_k(Delta_X)
 = #{ b odd square-free :
        Omega(b)=k+1,
        X/2 < b <= X }.
```

If `Y>=2X`, no `b` can satisfy both `b<=X` and `Y<2b`, so every induced reduced-homology map is zero. The canonical filtration has no topological feature with multiplicative persistence ratio greater than or equal to `2`.

In log energy `E=log X`, this statement is especially rigid: every bar has length exactly

```text
log(2b)-log b = log 2.
```

The shortest prime direction controls every homology lifetime.

## What remains RH-sensitive

The universal lifetime does **not** mean the barcode is information-free. Its birth locations and dimensions still encode all odd square-free integers:

```text
birth = b,
degree = Omega(b)-1.
```

At scale `X`, the alternating count of the currently alive bars is

```text
sum_(X/2 < b <= X, b odd square-free)
    (-1)^(Omega(b)-1)
 = - sum_(X/2 < b <= X, b odd) mu(b)
 = -M(X),
```

using the exact decomposition of the Mertens sum into odd and twice-odd square-free terms. This is just the Euler-characteristic identity already underlying `PL-022` and the LogPrime RH criterion.

Therefore persistent homology does not make RH disappear; rather, it localizes the difficulty sharply:

```text
persistence lifetime geometry
    -> completely rigid: every lifetime is log 2

RH-sensitive information
    -> cancellation among the birth locations and parity/degrees
       of an extensive family of equal-lifetime bars.
```

A transform of all birth locations can of course re-encode Möbius or `1/zeta`, but that is arithmetic information already present in the filtration and is not a new persistence mechanism.

## Analytic-continuation boundary

The finite filtered-chain and barcode statements are purely algebraic and require no Euler product or analytic continuation.

If one forms a Dirichlet transform of the odd square-free birth data, then in the absolutely convergent region one obtains familiar Euler products. For example,

```text
sum_(b odd square-free) mu(b) b^(-s)
 = product_(p>2) (1-p^(-s))
 = 1 / ((1-2^(-s)) zeta(s)),
```

initially for `Re(s)>1`.

Nothing in the barcode decomposition itself analytically continues that identity into the critical strip. Pakianathan–Winfree's RH formulation likewise becomes substantive only when one assumes/proves square-root control of the Mertens/Euler-characteristic cancellation. The topological encoding is exact; the required cancellation is still the number-theoretic problem.

## Prior-art and novelty audit

The closest source is stronger than a generic persistent-homology analogy: Pakianathan–Winfree explicitly

1. study scalar quota complexes as the quota changes and describe the problem as persistent homology;
2. prove the minimal-weight shell theorem;
3. introduce the exact `log p`-weighted `LogPrime` complex;
4. identify its Euler characteristic with the Mertens function and state the RH-equivalent growth condition.

Björner independently provides the equivalent square-free number complex and explicit Betti shell formula used in `PL-022`.

A targeted search for persistent homology/barcodes of the LogPrime, square-free divisibility, and Björner number-theoretic complexes did not locate the explicit filtered basis or the exact interval list `[b,2b)`. This absence is **not** evidence of novelty: the decomposition is an elementary chain-level globalization of the classical minimum-weight shell argument. The durable value here is the exact obstruction it gives this research line, not a claim of discovering a new persistence theorem.

## Boundary conditions and falsification tests

The negative is deliberately narrow.

- It applies to the canonical square-free simplicial filtration with additive weights `log p` and ordinary simplicial homology.
- It does not apply to the full exponent multicomplex/CW realization, to nonlocal or weighted boundary operators, to filtrations carrying archimedean/adelic data, or to invariants that deliberately add information beyond the ordinary inclusion persistence module.
- The fact that all lifetimes equal `log 2` does not make birth locations universal; those locations are arithmetic and can still support Möbius cancellation questions.
- A different filtration could have nonconstant lifetimes, but it must be justified intrinsically rather than chosen to manufacture a desired spectrum.

The exact claim is falsified if any nonempty odd square-free `b` fails to produce a bar in degree `Omega(b)-1` from `b` to `2b`, if an additional reduced bar exists, or if an inclusion map `Htilde_k(Delta_X)->Htilde_k(Delta_Y)` is nonzero for some `Y>=2X`. The filtration-preserving unimodular basis above reduces all three checks to direct simplicial-boundary identities.

## Consequence for the research line

`PL-022` left open the possibility that **persistent** rather than static Hodge topology might reveal a more informative spectral scale. The combination of Pakianathan–Winfree prior art and the filtered decomposition closes that simple escape:

```text
log-prime square-free filtration
    -> classical LogPrime quota/persistent topology
    -> exact bars [log b, log b+log 2)
    -> every lifetime = log 2
    -> RH remains signed Möbius cancellation of bar births/degrees.
```

Thus ordinary persistence cannot produce Riemann-zero ordinates as distinguished lifetimes, resonances, or long-lived topological features of this canonical exponent filtration. A viable topological continuation of the prime-lattice program must add genuinely new global structure — for example a nonlocal completed operator or adelic/archimedean coupling — rather than only tracking the ordinary homology of the existing energy cutoff through `X`.