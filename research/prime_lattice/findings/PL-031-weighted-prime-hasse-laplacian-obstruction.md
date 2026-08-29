# PL-031 — Translation-invariant weighted prime-Hasse Laplacians are either trivial or have interval spectrum

## Claim

A natural spectral escape left open after `PL-022` and `PL-030` is to put a graph Laplacian directly on the exponent lattice, joining every integer `n` to `pn` along the prime coordinate `p` and weighting that coordinate by arithmetic data such as `log p` or the radial Bohr factor `p^(-sigma)`.

On the standard Bohr/Dirichlet Hilbert space `ell^2(N)` with counting measure, the translation-invariant coordinate-separable version has a sharp obstruction.

Let `a_p>0` and define the weighted Hasse-edge Dirichlet energy

```text
Q_a(f)
  = sum_p a_p sum_(n>=1) |f(n)-f(pn)|^2.
```

Then exactly one of the following occurs:

```text
sum_p a_p = infinity
    -> Q_a(f)=infinity for every nonzero f in ell^2(N)
    -> the finite-energy domain is {0}

sum_p a_p = A < infinity
    -> Q_a is the form of a bounded positive self-adjoint L_a
    -> sigma(L_a) = [0,4A].
```

Thus the direct `log p`-weighted Laplacian is not an unbounded arithmetic Hamiltonian with an interesting discrete spectrum: its standard counting-measure form has no nonzero finite-energy vector at all. Conversely, any summable prime-coordinate regularization makes the operator bounded with a featureless interval as its ordinary spectrum.

The most Bohr-natural summable family reproduces the familiar critical exponent without becoming zero-sensitive. If

```text
a_p(sigma)=p^(-2 sigma),
```

then

```text
A(sigma)=sum_p p^(-2 sigma)
```

is finite exactly for `sigma>1/2`. Hence

```text
sigma>1/2:
    sigma(L_sigma) = [0,4 P(2 sigma)]

0<sigma<=1/2:
    Dom(Q_sigma) = {0},
```

where `P` is the prime zeta function in its ordinary convergent half-plane. The same threshold holds for the squared vertical-tangent weights

```text
a_p(sigma)=(log p)^2 p^(-2 sigma),
```

because these are summable exactly for `sigma>1/2`.

Adding the canonical vertical Kronecker phase does not help. The magnetic edge form

```text
Q_(a,t)(f)
  = sum_p a_p sum_n |f(n)-p^(-it) f(pn)|^2
```

is unitarily gauge-equivalent to `Q_(a,0)` via

```text
(U_t f)(n)=n^(-it)f(n).
```

Therefore every ordinary spectral invariant is independent of `t`. Although the exponent Hasse graph contains many commuting squares, the phase `p^(-it)` has zero holonomy because

```text
log(pn)-log n = log p
```

is an exact lattice gradient. The vertical prime flow supplies a pure gauge connection, not a magnetic flux capable of selecting Riemann-zero ordinates.

**Evidence/status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the route

```text
standard ell^2(N) / Bohr coefficient space
    + edges n <-> pn
    + coordinate-only positive conductances a_p
    + optional vertical phase exp(-it log p)
    -> ordinary graph-Laplacian spectrum as an RH/zero mechanism.
```

The general graph-Dirichlet-form and magnetic-gauge frameworks are classical. The dichotomy and interval-spectrum calculation below are elementary specializations to the prime-exponent Cartesian product. No novelty is claimed for weighted graph Laplacians, product spectra, or gauge equivalence.

## Exact Hasse-graph form

Write `e_n` for the standard basis of `ell^2(N)` and let the prime shift be

```text
S_p e_n = e_(pn).
```

Then

```text
(S_p^* f)(n)=f(pn).
```

Each undirected Hasse edge `{n,pn}` occurs exactly once in the pair `(p,n)`, so

```text
Q_a(f)
 = sum_p a_p ||(I-S_p^*)f||_2^2.
```

Under the exponent map this is just the weighted Cartesian-product edge form on

```text
N_0^(P),
alpha <-> alpha+e_p.
```

The arithmetic enters only through the coordinate conductance `a_p`; the local one-coordinate geometry is always the half-line `N_0`.

## Non-summable coordinate weights give a trivial form domain

For any `f in ell^2(N)`,

```text
||S_p^*f||_2^2
 = sum_(n>=1) |f(pn)|^2
 <= sum_(m>=p) |f(m)|^2
 -> 0
```

as `p->infinity` through the primes. Hence, for nonzero `f`,

```text
||(I-S_p^*)f||_2 -> ||f||_2.
```

In particular, there is a prime cutoff after which

```text
||(I-S_p^*)f||_2^2 >= ||f||_2^2/4.
```

If `sum_p a_p=infinity`, then

```text
Q_a(f)
 >= (||f||_2^2/4) sum_(p large) a_p
 = infinity.
```

Therefore

```text
boxed: Dom(Q_a)={0}.
```

This is stronger than a failure of essential self-adjointness or a badly behaved unbounded spectrum: the canonical counting-measure Dirichlet form is not densely defined at all.

Consequences include immediately

```text
a_p = log p              -> trivial domain,
a_p = (log p)^2          -> trivial domain,
a_p = p^(-2 sigma)       -> trivial domain for sigma<=1/2.
```

Thus assigning the raw lattice energy `log p` as an edge conductance cannot produce the desired unbounded Hilbert–Pólya operator in this representation.

## Summable weights give a bounded tensor Laplacian

Assume now

```text
A=sum_p a_p<infinity.
```

For one prime define

```text
L_p=(I-S_p)(I-S_p^*).
```

Then `L_p` is positive and `||L_p||<=4`, and

```text
Q_a(f)=<f,L_a f>,
L_a=sum_p a_p L_p,
```

where the series converges in operator norm. Hence

```text
0 <= L_a <= 4A I.
```

Unique factorization identifies

```text
ell^2(N)
 ~= tensor_product_p ell^2(N_0)
```

with the vacuum reference vector in all but finitely many coordinates. Under this factorization `L_p` acts only on the `p`-coordinate as the standard half-line graph Laplacian

```text
(L_0 x)_0 = x_0-x_1,
(L_0 x)_k = 2x_k-x_(k-1)-x_(k+1),  k>=1.
```

Its spectrum is exactly `[0,4]`. One direct audit is to take long finitely supported plane-wave packets far from the boundary: for every `theta in [0,pi]` they are approximate eigenvectors with eigenvalue

```text
2-2 cos(theta),
```

while positivity and `||L_0||<=4` give the reverse inclusion.

For a finite prime set `F`, the operators act on distinct tensor coordinates, so

```text
L_F=sum_(p in F) a_p L_p
```

has spectrum equal to the Minkowski sum of the local intervals:

```text
sigma(L_F)=[0,4 A_F],
A_F=sum_(p in F) a_p.
```

As `F` increases through the primes,

```text
||L_a-L_F|| <= 4(A-A_F) -> 0.
```

Every `lambda in [0,4A]` can therefore be approximated by `lambda_F in [0,4A_F]` and an approximate eigenvector of `L_F`; the norm tail tends to zero. Thus

```text
boxed: sigma(L_a)=[0,4A].
```

The conclusion is about the ordinary spectrum as a set. It is already enough to rule out identifying this canonical Laplacian spectrum with the discrete Riemann-zero ordinates.

## The `1/2` boundary reappears only as summability of prime directions

For

```text
a_p(sigma)=p^(-2 sigma),
```

the total conductance is

```text
A(sigma)=sum_p p^(-2 sigma)=P(2 sigma),
```

which converges exactly for `sigma>1/2`. Therefore the standard exponent-Hasse Dirichlet form undergoes a sharp transition at the same value already found in `PL-001` and `PL-030`:

```text
sigma>1/2
    -> bounded positive Laplacian
    -> spectrum [0,4P(2sigma)]

sigma<=1/2
    -> no nonzero finite-energy vectors.
```

There is a second natural way to obtain the same threshold directly from the Bohr curve. Its vertical tangent has prime-coordinate components

```text
d/dt [p^(-sigma-it)]
  = -i (log p) p^(-sigma-it),
```

so its squared ambient `ell^2` speed is

```text
sum_p (log p)^2 p^(-2 sigma).
```

Using these squared tangent amplitudes as conductances again gives a bounded Laplacian exactly for `sigma>1/2` and a trivial form domain at and below the critical line.

This is structurally meaningful but zero-blind. The transition uses only prime-coordinate square summability and occurs independently of analytic continuation, the functional equation, or the Riemann zero divisor.

## The vertical phase is an exact gauge, not a flux

Define

```text
Q_(a,t)(f)
 = sum_p a_p sum_n |f(n)-p^(-it)f(pn)|^2.
```

Let

```text
(U_t f)(n)=n^(-it)f(n).
```

Then `U_t` is unitary and, edge by edge,

```text
|(U_t f)(n)-(U_t f)(pn)|
 = |n^(-it)[f(n)-p^(-it)f(pn)]|.
```

Therefore

```text
Q_(a,t)(f)=Q_(a,0)(U_t f).
```

Whenever the corresponding operators exist,

```text
L_(a,t)=U_t^* L_(a,0) U_t.
```

So

```text
sigma(L_(a,t))=sigma(L_(a,0))
```

and likewise for any unitary spectral invariant.

Geometrically, the Hasse graph is not a tree: distinct prime directions make squares such as

```text
n -> pn -> pqn
|            ^
v            |
qn ----------
```

but the phase around every such square is still one because the edge phase is the exact coboundary of the vertex potential `t log n`. Equivalently,

```text
log n=<v(n),(log p)_p>
```

makes the Kronecker phase an exact one-form on the exponent lattice. Magnetic graph spectra can depend on nontrivial cycle holonomy; this particular arithmetic phase has none.

This is the graph-Laplacian analogue of the diagonal-unitary gauge invariance found for the GCD/Poisson Gram matrices in `PL-030`.

## Prior art and novelty audit

The operator-theoretic setting is standard.

- Matthias Keller and Daniel Lenz, **“Unbounded Laplacians on Graphs: Basic Spectral Properties and the Heat Equation,”** *Mathematical Modelling of Natural Phenomena* **5**(4) (2010), 198–224, DOI `10.1051/mmnp/20105409`, develops weighted graph Laplacians from regular Dirichlet forms and the associated self-adjointness/spectral framework.
- Carsten Lange, Shiping Liu, Norbert Peyerimhoff and Olaf Post, **“Frustration index and Cheeger inequalities for discrete and continuous magnetic Laplacians,”** *Calculus of Variations and Partial Differential Equations* **54** (2015), 4165–4196, DOI `10.1007/s00526-015-0935-x`, is a direct prior-art anchor for gauge invariance of discrete magnetic graph potentials and the fact that cycle holonomy, rather than an exact edge phase, carries magnetic spectral information.
- Kunyu Guo and Fugang Yan, **“Toeplitz operators on the Hardy space over the infinite-dimensional polydisc,”** *Acta Scientiarum Mathematicarum* **88** (2022), 223–262, DOI `10.1007/s44146-022-00016-z`, gives modern operator-theoretic prior art for the infinite-polydisc / multiplicative-coordinate setting in which prime monomial shifts act on `H^2(T^infinity)`.

A targeted search for Laplacians on integer divisibility graphs, prime-coordinate product graphs, infinite-polydisc Toeplitz operators, and magnetic graph gauge equivalence did not locate a source claiming this exact prime-Hasse dichotomy as an RH mechanism. That absence is not evidence of novelty. The proof is elementary once the standard graph form and prime shifts are written down, and no novelty is claimed for the general ingredients.

There is also relevant nearby number-theoretic graph prior art that illustrates the boundary rather than contradicting it. Helfgott and Radziwill, **“Expansion, divisibility and parity,”** arXiv:2103.06853, construct a substantially different prime-divisibility operator with additive moves `n -> n +/- p` and a compensating `1/p` term; they prove strong local expansion and obtain Liouville-correlation consequences. That operator is not the separable Hasse graph `n <-> pn`. Its success is therefore evidence that genuinely number-theoretic graph spectra may require coupling additive position to divisibility rather than merely taking a Cartesian Laplacian of the exponent coordinates.

## Boundary conditions and escape routes

### The counting measure is part of the theorem

The obstruction is for the standard coefficient Hilbert space `ell^2(N)`, equivalently the standard Bohr `H^2` basis. A nontrivial vertex measure can change the form domain and may turn nonsummable edge conductances into a meaningful unbounded operator. Such a model would need its measure justified mathematically and novelty-audited separately.

### Coordinate separability is essential

The proof uses conductances depending only on `p` and the Cartesian edge relation `n <-> pn`. State-dependent weights `a_p(n)`, interactions between prime coordinates, boundary terms depending on `log n`, or additive-multiplicative couplings need not have interval spectrum.

### Nonzero magnetic holonomy is outside the negative

The vertical phase `p^(-it)` is special because it is the exact gradient of `n^(-it)`. A magnetic potential with genuine flux around prime-coordinate squares cannot be gauged away by the above argument. It would, however, be extra structure not supplied by the ordinary Bohr vertical flow.

### Finite truncations can have discrete spectra without contradicting the theorem

Energy cutoffs such as `n<=N` produce finite graphs and discrete eigenvalues. A viable claim would have to identify a nontrivial scaling limit or trace formula that survives `N->infinity`; merely observing finite eigenvalue patterns does not evade the infinite-product result.

### Completed or nonlocal operators remain open

Signed/indefinite Weil forms, nonlocal kernels, adelic/archimedean corrections, scattering operators, and operators whose zeros appear as resonances rather than ordinary eigenvalues are not covered. Those are precisely the kinds of additional global structure already isolated by `PL-013` and `PL-014`.

## Audit / falsification tests

The finding would be falsified or materially narrowed by any of the following:

1. a nonzero `f in ell^2(N)` with finite `Q_a(f)` when `sum_p a_p=infinity`;
2. failure of `||S_p^*f||_2->0` as `p->infinity` for some `f in ell^2(N)`;
3. a summable positive weight family for which the norm-convergent tensor Laplacian has spectrum different from `[0,4 sum_p a_p]`;
4. dependence of the magnetic spectrum on `t` despite the explicit unitary `U_t` above;
5. a proposed model using a non-counting vertex measure, state-dependent/nonseparable conductances, nonzero cycle holonomy, finite-cutoff renormalization, or completed/nonlocal structure, in which case it lies outside the theorem rather than contradicting it.

The first four are excluded by the exact derivations above. The fifth identifies the actual remaining design space.

## Consequence for the research line

`PL-022` left a weighted or nonlocal exponent-complex Laplacian as a possible escape from the integer-valued ordinary Hodge spectrum. `PL-030` then showed that the canonical weighted `l1` exponent metric produces the classical GCD/Poisson kernel and a zero-blind measure-class transition at `1/2`.

The direct **local** graph-Laplacian alternative is now sharply constrained as well:

```text
prime Hasse edges alpha <-> alpha+e_p
    + nonsummable coordinate weights (including log p)
    -> trivial finite-energy domain on standard ell^2

prime Hasse edges
    + summable coordinate weights
    -> bounded tensor Laplacian
    -> spectrum is one interval

Bohr vertical phase exp(-it log p)
    -> exact lattice gradient
    -> pure gauge
    -> no t-dependent spectrum

Bohr damping p^(-2sigma)
    -> bounded exactly for sigma>1/2
    -> critical boundary is again square summability, not zero localization.
```

A genuinely new lattice Laplacian route must therefore break at least one of the features that make this model canonical: standard counting measure, coordinate-only conductances, local Hasse edges, or exact-gradient vertical phases. In particular, merely “weighting the exponent graph by `log p`” does not create an RH-sensitive spectral geometry.