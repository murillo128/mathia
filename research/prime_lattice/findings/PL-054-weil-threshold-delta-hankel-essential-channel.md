# PL-054 — Prime-power thresholds create essential delta-Hankel channels, not discrete spectral-flow eigenvalue births

## Claim

`PL-051`--`PL-053` leave threshold-by-threshold spectral evolution as one possible way to retain arithmetic information before the fixed-depth Weil boundary shell homogenizes. The most direct version of that route fails at the level of an individual entering prime-power channel.

Fix a boundary depth `R>0`. For a prime power

```text
q=p^k,
omega_q=log q,
L_q=(1/2)log q,
```

consider `L>L_q` with

```text
delta=2L-log q in (0,R).
```

In the normalized fixed-depth boundary operator of `PL-051`, the single `q`-term contributes

```text
W_(q,L)
 = a_q(L)
   [ 0        H_delta ]
   [ H_delta 0       ],

a_q(L)=exp(-L) Lambda(q)/sqrt(q),
```

where

```text
(H_delta f)(b)
 = f(delta-b),     0<b<delta,
 = 0,              delta<b<R.
```

Then

```text
boxed:
||H_delta|| = ||H_delta||_ess = 1
```

for every `delta>0`, and `+1` and `-1` are eigenvalues of `H_delta` with infinite multiplicity. At the threshold,

```text
H_delta -> 0 strongly as delta downarrow 0,
```

but not in norm and not in the Calkin quotient. Since

```text
a_q(L) -> Lambda(q)/q
```

as `L downarrow L_q`, the entering channel has the one-sided behavior

```text
W_(q,L) -> 0 strongly,

lim_(L downarrow L_q)
  ||W_(q,L)||_ess
 = Lambda(q)/q > 0.
```

Thus a prime-power threshold in the raw boundary operator is **not** the birth of an isolated finite-multiplicity eigenvalue. It is the appearance, in strong topology, of a delta-Hankel reflection channel whose nonzero spectral values already have infinite multiplicity and whose essential norm is macroscopic relative to its coefficient.

Consequently the naive route

```text
prime-power thresholds L=(k log p)/2
    -> discrete eigenvalue births/crossings
    -> ordinary Fredholm spectral flow
    -> arithmetic zero-counting invariant
```

is not available for the unsmoothed fixed-depth boundary decomposition. Any threshold-flow construction that survives this obstruction must first add a mathematically justified compactification, smoothing, Fredholm reference, or weaker topology and then prove that the added structure is arithmetic rather than universal.

**Evidence/status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION`, and `DECISIVE-NEGATIVE` only for the naive interpretation of raw prime-power threshold events as ordinary finite-multiplicity Fredholm spectral-flow crossings. The delta-Hankel/reflection phenomenon is classical operator theory; no novelty claim is made.

This finding does **not** determine the essential spectrum of the full sum `B_(L,R)` at a threshold, because different atomic channels can interact. It does not rule out generalized non-Fredholm spectral flow, a canonically smoothed path, mesoscopic scaling, or spectral evolution of the completed Weil operator including archimedean and pole terms.

## One prime-power threshold in boundary coordinates

Recall from `PL-051` that the outer-shell cross-end block is

```text
H_(mu_(L,R)),
```

with

```text
mu_(L,R)
 = exp(-L)
   sum_(2L-2R<log n<2L)
     Lambda(n)/sqrt(n)
     delta_(2L-log n).
```

For a fixed prime power `q=p^k`, its outer-shell atom is present exactly while

```text
0 < delta_q(L)=2L-log q < 2R.
```

Near its entrance time

```text
L_q=(1/2)log q,
```

we have `0<delta_q(L)<R`, and its cross-end contribution is therefore

```text
a_q(L) H_(delta_q(L)),

a_q(L)=exp(-L) Lambda(q)/sqrt(q).
```

The full two-end contribution is the self-adjoint block `W_(q,L)` stated above. At exact equality `2L=log q`, the strict cutoff `log n<2L` means the atom is absent. Hence the threshold is naturally a one-sided entry event.

In exponent-lattice coordinates this is the axis point

```text
v(q)=k e_p
```

crossing the moving energy boundary

```text
<v(q),(log r)_r>
 = k log p
 = 2L.
```

So these threshold times are not an arbitrary operator parametrization: they are precisely the moments at which prime-power lattice points enter the compact Weil support.

## The atomic Hankel operator is a partial reflection

For general `0<delta<2R`, define

```text
I_delta
 = (max(0,delta-R), min(R,delta)).
```

The atomic operator can be written

```text
(H_delta f)(b)
 = 1_(I_delta)(b) f(delta-b).
```

The map

```text
b -> delta-b
```

preserves `I_delta` and is an involutive reflection. Therefore

```text
H_delta^*=H_delta,
H_delta^2=P_(I_delta),
```

where `P_(I_delta)` is the orthogonal projection onto `L^2(I_delta)`.

On `L^2(I_delta)`, translate the midpoint `delta/2` to the origin. The operator becomes ordinary reflection

```text
(Rf)(x)=f(-x).
```

Its even and odd subspaces are both infinite dimensional, so

```text
+1 and -1
```

are eigenvalues of infinite multiplicity. If `I_delta` does not fill `(0,R)`, zero is also an eigenvalue of infinite multiplicity on the complement.

It follows immediately that

```text
||H_delta||=1,
||H_delta||_ess=1.
```

The two-end block

```text
A_delta
 = [ 0        H_delta ]
   [ H_delta 0       ]
```

is unitarily equivalent to

```text
H_delta direct_sum (-H_delta),
```

so it has the same unit essential-norm scale and infinite-multiplicity nonzero spectral channels.

This is the finite-depth version of the classical delta-Hankel phenomenon. Yafaev records that for a Hankel kernel

```text
h(t)=h_0 delta(t-t_0)
```

on `L^2(R_+)`, the `K=0` case has exactly the spectral values `0`, `h_0`, and `-h_0`, each with infinite multiplicity; the operator reduces to reflection plus shift. See D. R. Yafaev, “Diagonalizations of two classes of unbounded Hankel operators,” *Bulletin of Mathematical Sciences* **4** (2014), 175–198, DOI `10.1007/s13373-013-0044-0`, arXiv:`1306.3676`.

## Strong threshold birth but essential-norm jump

For the threshold regime `0<delta<R`,

```text
I_delta=(0,delta).
```

For every fixed `f in L^2(0,R)`, a change of variable gives

```text
||H_delta f||_2^2
 = integral_0^delta |f(delta-b)|^2 db
 = integral_0^delta |f(a)|^2 da.
```

Absolute continuity of the `L^2` integral therefore yields

```text
H_delta f -> 0
```

for every fixed `f` as `delta downarrow 0`. Hence

```text
H_delta -> 0 strongly.
```

But the exact reflection calculation above gives, for every `delta>0`,

```text
||H_delta||
 = ||H_delta||_ess
 = 1.
```

So the threshold family is neither norm-continuous nor Calkin-continuous at its entry point.

The arithmetic coefficient has the one-sided limit

```text
a_q(L_q)
 = exp(-(log q)/2)
   Lambda(q)/sqrt(q)
 = Lambda(q)/q.
```

Thus

```text
lim_(L downarrow L_q)
 ||W_(q,L)||_ess
 = Lambda(q)/q.
```

For `q=p^k`, this is

```text
(log p)/p^k.
```

The coefficient becomes small for high thresholds, but the topology of the event does not change: each individual atom enters as an infinite-dimensional essential channel rather than as a finite-rank perturbation.

## Why ordinary spectral flow is not the raw threshold invariant

The standard bounded spectral-flow framework, for example John Phillips, “Self-Adjoint Fredholm Operators and Spectral Flow,” *Canadian Mathematical Bulletin* **39**(4) (1996), 460–467, DOI `10.4153/CMB-1996-054-4`, concerns continuous paths of self-adjoint Fredholm operators and counts net spectral passage through zero.

The atomic threshold family misses both ingredients in the most direct interpretation.

First, for `0<delta<R`, the complement

```text
L^2(delta,R)
```

is an infinite-dimensional kernel of `H_delta`; correspondingly the two-end atom has zero in its essential spectrum. The newborn channel itself is therefore not Fredholm.

Second, extending the channel by zero at the entry time gives a strongly continuous one-sided birth but a positive norm and essential-norm jump. Hence it is not a norm-continuous bounded Fredholm path to which the standard discrete-crossing picture can simply be applied.

This is a scoped obstruction, not a theorem that “spectral flow is impossible.” There are generalized spectral-flow formalisms for other topologies and non-Fredholm settings, and one may add a reference operator or smoothing that changes the Fredholm properties. But doing so is **additional mathematical structure**. The prime-power cutoff by itself does not supply a canonical finite-multiplicity crossing invariant.

## Why this does not determine the full boundary spectrum

The exact normalized boundary operator contains the sum of all active atoms plus the vanishing same-end small-lag terms:

```text
B_(L,R)
 ~ sum_q W_(q,L).
```

Essential spectra of noncommuting sums cannot be obtained by unioning the essential spectra of the summands. Another atom can alter or cancel spectral structure of a given channel. Therefore the result above does **not** assert that `+/-a_q(L)` belong to the essential spectrum of the full `B_(L,R)` at every `L`.

What is exact is the channel-level statement needed to audit the naive threshold picture: the elementary event associated with one new exponent-lattice axis point is already an infinite-dimensional reflection, not an isolated eigenvector entering the spectrum.

`PL-053` gives a complementary aggregate fact: after subtracting the universal PNT boundary model, the full fixed-depth residual has a positive essential-norm defect for large `L`. The present finding explains why looking instead at individual cutoff events does not automatically replace that essential structure by a discrete eigenvalue-counting process.

## Beurling and universality audit

Nothing in the reflection calculation knows that

```text
omega_q=k log p
```

came from a rational prime. Any positive atomic frequency system whose boundary compression contains a point mass at deficit `delta` produces the same operator

```text
H_delta f(b)=f(delta-b)
```

with the same infinite-multiplicity `+/-1` channels and the same strong-versus-essential-norm threshold behavior.

Only the coefficient and the set of threshold locations change. A matched generalized-prime/Beurling system therefore exhibits the same local event geometry.

Consequently this threshold phenomenon is **not arithmetic rigidity**. It is a universal feature of compressing atomic translation measures to two endpoint layers. Any useful threshold invariant must depend on relations among many rational-prime thresholds, on the archimedean coupling, on a zeta-specific target/positivity structure, or on another ingredient that fails the matched-control test.

## Analytic-continuation boundary

No Euler product or Dirichlet series is continued here. The prime-power atom is part of the finite non-archimedean distribution in the already-completed Weil explicit formula. The argument then uses only the exact compressed-translation geometry of a single atom.

Thus the obstruction lives entirely on the completed explicit-formula side. It cannot be dismissed as an artifact of remaining in `Re(s)>1`.

## Prior-art and novelty audit

The two ingredients are classical.

- Delta-supported Hankel kernels acting by reflection/shift and carrying infinite-multiplicity symmetric spectrum are standard; Yafaev's 2014 paper gives an explicit prior-art anchor and cites the earlier sign-definite-Hankel analysis for the `K=0` spectrum.
- Spectral flow for continuous paths of self-adjoint Fredholm operators is classical; Phillips 1996 is a standard primary reference for the bounded setting used as the comparison class here.

A targeted search across compact-window Weil operators, prime-power threshold evolution, delta-Hankel channels, and spectral flow did not locate a theorem attaching a discrete Fredholm spectral-flow count to these raw boundary-shell threshold atoms. That search absence is **not** evidence of novelty. The durable content is the direct specialization to the persisted `PL-051` boundary operator and the resulting no-go for one specific surviving route from `PL-053`.

## Falsification and boundary tests

The exact claim reduces to six checks:

1. a prime-power atom entering at `2L=log q` contributes the displayed `H_delta` cross-end block;
2. `H_delta^2=P_(I_delta)`;
3. reflection on `L^2(I_delta)` has infinite-dimensional `+1` and `-1` eigenspaces;
4. for `delta downarrow 0`, `||H_delta f||^2=integral_0^delta |f|^2 ->0` for every fixed `f`;
5. the normalized coefficient tends to `Lambda(q)/q` at the threshold;
6. for `0<delta<R`, the infinite-dimensional kernel puts zero in the essential spectrum of the atomic channel.

Items 1 and 5 follow from the exact boundary-shell formula of `PL-051`. Items 2--4 and 6 are elementary functional analysis. Failure of any one of them falsifies the threshold obstruction as stated.

## Consequence for the research line

The fixed-depth boundary branch now has a sharper topology ledger:

```text
PNT boundary blow-up
    -> strong universal rank-one limit                         [PL-051]

raw centered boundary residual
    -> norm gap from prime-log recurrence                     [PL-052]
    -> essential-norm gap; no compact/Schatten repair         [PL-053]

individual prime-power threshold
    -> delta-Hankel reflection channel
    -> strong birth from zero
    -> nonzero essential-norm jump
    -> no naive discrete Fredholm eigenvalue crossing         [PL-054]
```

So threshold information is indeed finer than first-order PNT homogenization, but its raw operator manifestation is still **essential and universal**, not a discrete zeta-zero spectrum.

A surviving threshold-based route must therefore add something that changes this topology in a canonical and arithmetic way. Examples include a smoothing or reference operator whose Fredholmization is forced by the full Weil form, an invariant built from relations among many threshold events rather than one atom, or an archimedean/positivity coupling that turns the universal reflection channels into a zeta-specific sign/localization statement. Merely counting prime-power entries as if each created an isolated eigenvalue is ruled out.