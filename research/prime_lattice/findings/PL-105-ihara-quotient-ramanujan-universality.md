# PL-105 — Ihara quotient zeta turns the half-axis into graph Ramanujan temperedness, and generic regular graphs pass the same RH test

## Claim

The arithmetic-quotient escape left open by `PL-104` has a precise classical first test, and it is negative for the Prime-Lattice objective.

Let `X` be a finite connected `(q+1)`-regular graph with adjacency matrix `A`, `n` vertices, and `m` edges. Its Ihara zeta function

```text
Z_X(u)
 = product_[C] (1-u^(ell(C)))^(-1)
```

runs over primitive closed non-backtracking cycle classes. Bass's determinant formula gives

```text
Z_X(u)^(-1)
 = (1-u^2)^(m-n)
   det(I - A u + q u^2 I).
```

Hence every adjacency eigenvalue `lambda` contributes the quadratic factor

```text
1-lambda u+q u^2.
```

For a nontrivial adjacency eigenvalue, the two roots satisfy

```text
u_+ u_- = q^(-1).
```

They both lie on the circle

```text
|u|=q^(-1/2)
```

if and only if

```text
|lambda| <= 2 sqrt(q).
```

After the standard reparametrization

```text
u=q^(-s),
```

the circle is exactly

```text
Re(s)=1/2.
```

Thus the graph-theoretic Riemann hypothesis for `Z_X` — nontrivial poles of `Z_X(q^(-s))`, equivalently nontrivial zeros of its reciprocal, lying on `Re(s)=1/2` — is exactly the **Ramanujan bound** on the nontrivial adjacency spectrum.

This is the cycle/determinant completion of the local tempered half-axis found in `PL-104`. Adding a finite quotient really does add closed geodesics, an Euler product, a determinant formula, and an exact RH-like root-location statement. But the resulting half-axis is still not rational-prime-specific.

Marcus--Spielman--Srivastava prove that there are infinite families of bipartite Ramanujan graphs of **every degree `d>2`**. Taking

```text
d=7,
q=d-1=6,
```

gives infinite families whose Ihara zeta functions satisfy the same exact graph RH on

```text
|u|=6^(-1/2)
<=>
Re(s)=1/2,
```

even though no finite field has cardinality `6`, hence there is no non-archimedean local field whose Bruhat--Tits tree has residue parameter `q=6`.

So the matched-control obstruction strengthens from `PL-104`:

```text
homogeneous-tree spectrum
+ canonical Re(s)=1/2 tempered axis
```

was already branching-universal, and now even

```text
finite quotient cycles
+ Ihara Euler product
+ Bass determinant
+ functional-equation half-axis
+ exact graph RH
```

survives an abstract regular-graph control with no rational-prime/local-field origin.

Arithmetic quotients such as the Lubotzky--Phillips--Sarnak Ramanujan graphs are genuine and important, but their extra arithmetic is used to prove a Ramanujan/tempered spectral bound for the **graph/automorphic quotient**. The Ihara determinant does not identify its cycle zeta with the ordinary Riemann zeta function, nor does it turn Riemann zeros into graph adjacency eigenvalues. A route from an arithmetic tree quotient to ordinary `zeta(s)` therefore still needs an additional global theorem coupling that quotient to the Riemann divisor; the graph-zeta package alone does not supply it.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE` for the route

```text
Bruhat--Tits/local regular-tree geometry
    -> add a finite/arithmetic quotient with cycles
    -> Ihara determinant and graph RH
    -> infer a new mechanism localizing ordinary Riemann zeros.
```

The negative statement is deliberately scoped. It does **not** say that every arithmetic quotient is spectrally generic or that automorphic quotients contain no arithmetic information. It says that the specific package `regular-tree quotient + Ihara zeta + Ramanujan half-axis` is already a universal graph-theoretic mechanism and therefore cannot, without additional arithmetic coupling, be the missing discriminator for the rational-prime exponent lattice.

## Exact determinant-to-half-axis calculation

For a `(q+1)`-regular graph, Bass's formula reduces to

```text
Z_X(u)^(-1)
 = (1-u^2)^(m-n)
   product_j (1-lambda_j u+q u^2),
```

where `{lambda_j}` is the real adjacency spectrum.

Fix one eigenvalue `lambda`. The quadratic roots are

```text
u_+/-
 = (lambda +/- sqrt(lambda^2-4q))/(2q).
```

If

```text
|lambda| < 2 sqrt(q),
```

write

```text
lambda = 2 sqrt(q) cos(theta).
```

Then

```text
u_+/-
 = q^(-1/2) exp(+/- i theta),
```

so both have modulus `q^(-1/2)`.

At the endpoints `lambda=+/-2sqrt(q)`, the two roots coincide at `+/-q^(-1/2)`, still on the same circle.

Conversely, because `A` is self-adjoint, `lambda` is real. If both roots have modulus `q^(-1/2)`, their sum is real and can be written

```text
u_+ + u_-
 = 2 q^(-1/2) cos(theta).
```

Since the sum also equals `lambda/q`, one gets

```text
lambda = 2 sqrt(q) cos(theta),
```

hence `|lambda|<=2sqrt(q)`.

The trivial adjacency eigenvalue `q+1` factors as

```text
1-(q+1)u+q u^2
 = (1-u)(1-q u),
```

and, in the bipartite case, `-(q+1)` gives the corresponding negative trivial factors. These are excluded in the standard graph-RH convention. Therefore

```text
boxed:
all nontrivial Ihara poles lie on |u|=q^(-1/2)
<=>
all nontrivial adjacency eigenvalues satisfy
|lambda|<=2sqrt(q).
```

This is exactly the Ramanujan condition.

Putting `u=q^(-s)` gives

```text
|u|=q^(-Re(s)),
```

so

```text
|u|=q^(-1/2)
<=>
Re(s)=1/2.
```

The reciprocal-root involution

```text
u -> 1/(q u)
```

is correspondingly

```text
s -> 1-s.
```

Thus the same Weyl/self-dual half-axis already seen in the tree recurrence of `PL-104` becomes the exact symmetry axis of the finite quotient determinant.

## What quotient cycles genuinely add

`PL-104` stopped at the universal covering tree. A tree has no primitive closed cycles, so its intrinsic spectral data did not yet produce an Ihara Euler product.

Passing to a finite quotient changes that:

```text
T_q
  -> Gamma\T_q = X
  -> primitive closed geodesics in X
  -> Ihara Euler product
  -> finite determinant through A.
```

This is genuine extra global topology. The cycle lengths are not present in the local radial recurrence, and Bass's formula is a real trace/determinant bridge between them and the adjacency spectrum.

So the negative conclusion is not that quotienting adds nothing. It adds exactly the sort of structure the Prime-Lattice search has been asking for: cycles, a prime-geodesic Euler product, a determinant, a functional symmetry, and a spectral root-location criterion.

The decisive question is whether that added structure knows the **rational-prime norm map** or the ordinary Riemann divisor. The generic-degree control shows that the answer is no at the level of the bare Ihara/Ramanujan mechanism.

## Generic-degree control: `q=6`

Every connected `(q+1)`-regular finite graph has the homogeneous `(q+1)`-regular tree as its universal cover. Nothing in the Bass determinant or in the graph-RH/Ramanujan equivalence requires that `q` be a prime power.

Marcus--Spielman--Srivastava prove that for every integer degree

```text
d>2
```

there are infinite families of `d`-regular bipartite Ramanujan graphs.

Choose

```text
d=7,
q=6.
```

Then the nontrivial adjacency spectrum obeys

```text
|lambda| <= 2 sqrt(6),
```

so every nontrivial pole of the associated Ihara zeta lies on

```text
|u|=1/sqrt(6),
```

or `Re(s)=1/2` after `u=6^(-s)`.

But a finite residue field has prime-power cardinality. There is no finite field of order `6`, and hence no local field with a Bruhat--Tits tree whose residue parameter is `6`.

This control is stronger than merely replacing `p` by a free branching parameter in the infinite-tree formulas of `PL-104`. It preserves the full finite object:

```text
closed geodesics,
Euler product,
rational continuation,
Bass determinant,
self-adjoint adjacency spectrum,
and exact graph RH.
```

Therefore none of these structures, separately or together, singles out rational primes.

## Arithmetic Ramanujan quotients do not change what the graph RH means

Lubotzky--Phillips--Sarnak construct explicit regular Cayley graphs with the optimal nontrivial spectral bound

```text
|lambda| <= 2 sqrt(d-1).
```

These are arithmetic constructions and belong naturally to the Bruhat--Tits/automorphic lineage. Their arithmetic is substantial: it provides a mechanism for proving tempered/Ramanujan spectral behavior that is unavailable for a generic explicitly presented graph.

But once a finite regular graph is known to be Ramanujan, its Ihara RH follows from the same determinant algebra above. The graph zeta does not remember *why* the spectral bound holds.

This separates two statements that should not be conflated:

```text
arithmetic input can force a quotient to be Ramanujan
    -- true and classical;

Ihara RH of that quotient localizes zeros of ordinary Riemann zeta
    -- no such implication follows from the graph determinant.
```

In particular, the primitive objects in the Ihara Euler product are closed graph geodesics. They are not the rational primes `p`, and their lengths are not the exponent-lattice energies `log p` unless an additional dictionary is imposed.

Any proposal that identifies those cycle factors with rational-prime Euler factors must therefore justify a new global correspondence rather than treating the formal similarity of Euler products as evidence.

## Analytic-continuation boundary

This comparison makes the continuation issue especially sharp.

For a finite graph, Bass's formula shows that

```text
Z_X(u)
```

is a rational function. Its continuation away from its initial small-`u` Euler-product disk is algebraic and finite-dimensional. The graph RH is therefore a root-location theorem for the polynomial

```text
det(I-Au+q u^2 I)
```

after removing trivial factors.

For ordinary Riemann zeta,

```text
product_p (1-p^(-s))^(-1)
```

converges only in `Re(s)>1`. Its continuation and functional equation require global Fourier/Poisson or automorphic scattering structure, as recorded in `PL-014` and `PL-039`.

Thus one cannot transfer the successful graph argument by analogy:

```text
finite graph:
cycle Euler product
 -> Bass finite determinant
 -> adjacency self-adjointness
 -> graph RH iff Ramanujan;

Riemann zeta:
prime Euler product
 -/-> known finite/self-adjoint determinant
across Re(s)=1.
```

The missing arrow is exactly the hard part. An Ihara quotient supplies a determinant for its **own** zeta function, not a determinant for the analytically continued Riemann zeta function.

## Prior art and novelty audit

The mathematical ingredients are classical; no novelty is claimed for graph zeta functions, determinant formulas, Ramanujan graphs, or their RH analogy.

- **Hyman Bass**, “The Ihara-Selberg zeta function of a tree lattice,” *International Journal of Mathematics* **3**(6) (1992), 717--797. DOI `10.1142/S0129167X92000357`. Primary source for the determinant formula in the tree-lattice/graph setting.
- **Harold M. Stark, Audrey A. Terras**, “Zeta functions of finite graphs and coverings,” *Advances in Mathematics* **121** (1996), 124--165. DOI `10.1006/aima.1996.0050`. Classical finite-graph zeta and covering reference; the regular-graph RH/Ramanujan equivalence belongs to this established theory.
- **Alexander Lubotzky, Ralph Phillips, Peter Sarnak**, “Ramanujan graphs,” *Combinatorica* **8** (1988), 261--277. DOI `10.1007/BF02126799`. Arithmetic explicit regular graphs with the optimal `2sqrt(d-1)` nontrivial spectral bound.
- **Adam W. Marcus, Daniel A. Spielman, Nikhil Srivastava**, “Interlacing families I: Bipartite Ramanujan graphs of all degrees,” *Annals of Mathematics* **182**(1) (2015), 307--325. DOI `10.4007/annals.2015.182.1.7`. Provides the decisive matched control: infinite families of bipartite Ramanujan graphs for every degree greater than `2`, including degrees for which `q=d-1` is not a prime power.

The durable Mathia contribution is only the **line-specific collision** with the escape explicitly left open in `PL-104`: moving from the universal tree to finite quotient cycles does create a full zeta/determinant/RH package, but that package still survives a non-local-field regular-graph control. Therefore its critical half-axis remains a manifestation of Ramanujan/tempered graph spectrum, not evidence that the rational-prime exponent lattice has acquired a new zero-localization mechanism.

A targeted novelty search around Ihara/Bass graph zeta, Ramanujan graphs, Bruhat--Tits quotients, and modern all-degree Ramanujan constructions found the ingredients above to be standard. No paper was found that needs to be credited for the specific Mathia bookkeeping statement because that statement is a direct falsification comparison between already-classical theorems.

## Adversarial boundaries

1. **Arithmetic quotients are not claimed to be generic.** The `q=6` control shows that the *Ihara/Ramanujan mechanism* is generic enough to exist without a local-field origin. It does not erase additional Hecke, Galois, or automorphic structure present in a specific arithmetic quotient.

2. **The graph RH is about poles of graph zeta, not zeros of Riemann zeta.** Calling both statements “RH” is an analogy justified by the determinant symmetry, not an identification of divisors.

3. **The finite determinant is real and exact.** The negative result does not dismiss the determinant as cosmetic. It is precisely because Bass gives a genuine determinant and self-adjoint adjacency spectrum that the non-arithmetic control is strong.

4. **Prime-power `q` is not enough.** Even when `q=p` and the universal tree is genuinely Bruhat--Tits, the graph determinant still describes quotient cycles. Recovering the ordinary local Euler factor `1/(1-p^(-s))` returns to the scalar Satake/Tate channel already classicalized in `PL-039` and `PL-104`.

5. **An automorphic global `L`-function is a different object.** If quotient eigenvalues are assembled as Hecke/Satake parameters into an automorphic `L`-function, its continuation and functional equation come from automorphic theory. That is not a hidden consequence of the graph's Ihara zeta alone and must be audited as a separate global mechanism.

6. **A genuinely global quotient coupling all rational primes remains outside this no-go.** The finding rules out treating a collection of local-tree quotients or the ordinary Ihara/Ramanujan package as sufficient. It does not preclude a new global arithmetic object whose trace formula has the ordinary `zeta` divisor and an independent positivity theorem.

## Decisive falsification test for any proposed repair

A repair of the quotient route must exhibit an invariant `I` satisfying all of the following:

```text
1. I is defined canonically from the arithmetic quotient/global object,
   not by inserting Riemann zeros or Euler factors by hand;

2. I is not determined solely by the regular-graph adjacency spectrum,
   Ihara cycle lengths, or the Ramanujan bound;

3. I fails or changes on all-degree generic Ramanujan controls
   such as q=6;

4. I couples to the ordinary rational-prime norm map across infinitely
   many primes;

5. the coupling survives a legitimate continuation theorem into the
   critical strip;

6. a positivity/self-adjointness/localization statement for I actually
   constrains the ordinary Riemann divisor.
```

Without such an invariant, replacing a prime axis by an arithmetic tree quotient merely upgrades the universal local half-axis of `PL-104` to the equally classical graph-RH/Ramanujan half-axis.

## Consequence for the research line

The Bruhat--Tits branch is now closed one level farther than `PL-104`:

```text
bare local tree
    -> half-axis is universal temperedness                       (PL-104)

finite/arithmetic regular-tree quotient
    -> cycles + Ihara Euler product + exact determinant
    -> graph RH iff Ramanujan
    -> still universal under non-local-field all-degree controls (PL-105)
```

So neither the existence of a canonical `1/2` axis nor the addition of an honest cycle determinant is enough. A future local-to-global construction must carry information **beyond the Ihara/Ramanujan quotient package** and must explicitly reconnect that information to the ordinary Riemann zeta continuation.

This also means there is no reason to escalate the resolved Bruhat--Tits clue merely to obtain more elaborate regular-building quotients. Higher-rank or arithmetic-quotient work becomes relevant only when a concrete global invariant is specified that escapes the generic Ramanujan-control test and acts back on the ordinary zeta channel.