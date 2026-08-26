# PF-045 — fixed-topology prime tangents force modulus-driven small essential spectrum

**Status:** `POSITIVE / EXACT-DERIVED + LITERATURE-BACKED`, with one explicitly audited adaptation of Pintz's proof.

PF-043 proved that prime-derived tangent eigenvalues accumulate at zero by letting the number of cusps grow.  That left an important ambiguity: the effect could have been entirely topological, caused only by increasingly many cusps.  This finding removes that ambiguity.

There is a sequence of recurrent isolated prime patterns whose tangent surfaces all have the **same topological type** `S_{0,r+1}`, while an internal consecutive-gap ratio tends to zero.  The exact PF-029 trace formula then pinches a separating geodesic of those fixed-topology tangents.  A direct Rayleigh test forces a positive Laplace eigenvalue to zero, and PF-034 implants those eigenvalues into the essential spectrum of the single infinite prime-flute.

Thus concrete **prime-gap moduli**, not only cusp count, force positive essential spectral values arbitrarily close to zero.

## 1. An arithmetic lemma extracted from Pintz's isolated-cluster proof

Pintz, *On the ratio of consecutive gaps between primes* (arXiv:1406.2658v2), Section 4, begins the proof of Theorem 2 by choosing

```text
an arbitrary set of m different primes
H = {h_1 < ... < h_m}
```

subject to

```text
h_1 > C_3(m),
h_t does not divide h_i-h_j  for i != j.
```

He then combines Erdos--Rankin covering with Maynard--Tao to obtain infinitely many translations `ell+H` containing at least `k0` consecutive primes, while the intervals immediately outside the bounded `H`-window are prime-free on an Erdos--Rankin scale tending to infinity.

The printed theorem chooses an upper bound `h_m<C_4(m)` uniformly in `k0`, because its constants are stated to depend only on `k0`.  For the present application we do not need this uniformity.  Inspecting Section 4 shows that the proof uses the `h_i` only as **fixed constants relative to the asymptotic variable**: products `(1-1/h_i)^(-1)`, finitely many forbidden congruence classes, and the assertion that prime divisors of the fixed differences `h_i-h_j` are `O(1)`.  The final Maynard--Tao step likewise only needs those exceptional primes to be fixed and eventually much smaller than the growing sieve parameters.

Therefore the same proof gives the following non-uniform form:

> For every fixed finite prime set `H` satisfying Pintz's divisibility condition, and for `m` large enough in terms of `k0`, there are infinitely many translations for which at least `k0` of `ell+h_i` are consecutive primes and the two exterior prime-free intervals tend to infinity.  The constants and starting point may now depend on `H`.

This is an **adaptation of the proof**, not a claim that it is the literal uniform statement of Pintz's Theorem 2.  The relevant proof locations are Section 4, equations (4.2)--(4.7) and (4.43)--(4.50).

The flexibility is also consistent with the independent Maynard--Tao consequence of Banks--Freiberg--Turnage-Butterbaugh, *Consecutive primes in tuples* (Acta Arith. 167 (2015), 261--266): sufficiently large arbitrary admissible tuples contain fixed-size subsets that occur infinitely often as consecutive primes.  What Pintz adds here is the growing prime-free isolation on both sides.

## 2. Fixed-cardinality candidate sets with arbitrarily extreme internal ratios

Fix `k0=3`, and let `m` be the corresponding sufficiently large constant in the Pintz/Maynard construction.  For every `B>2` we can construct primes

```text
h_1 < h_2 < ... < h_m
```

such that

```text
h_{j+1} > B h_j
```

and Pintz's condition

```text
h_t does not divide h_i-h_j  (i != j)
```

holds for every `i,j,t`.

A recursive construction is elementary.  Suppose `h_1,...,h_{j-1}` have been chosen, all greater than `m`.  For each previous prime `h_t`, avoid the fewer-than-`m<h_t` residue classes

```text
h_i mod h_t,   i<j, i != t.
```

Choose a nonzero allowed residue modulo each `h_t`, combine them by CRT, and apply Dirichlet's theorem to choose a prime in the resulting reduced residue class larger than `B h_{j-1}`.  For the new prime `h_j`, divisibility of an old difference by `h_j` is impossible because the old differences have absolute value `<h_j`.

Now take **any** subset

```text
a_1 < a_2 < ... < a_r,
r >= 3,
```

of this candidate set and write its first two consecutive spacings

```text
d_1=a_2-a_1,
d_2=a_3-a_2.
```

Geometric growth gives

```text
d_1 < a_2,
d_2 > (B-1)a_2,
```

hence

```text
boxed:
d_1/d_2 < 1/(B-1).
```

Thus the ratio is small **for every possible prime subset** selected by the sieve; we do not need to control which subset Maynard--Tao chooses.

## 3. Pigeonhole gives recurrent isolated exact patterns

Apply the non-uniform Pintz lemma to the fixed candidate set for a given `B`.  In every successful translation, all primes in the bounded central window occur at a subset of the finitely many offsets `h_i`, at least three of them, and the two exterior prime gaps tend to infinity.

There are finitely many subsets.  Passing to an infinite subsequence yields one exact pattern

```text
H_B={eta_1<...<eta_{r_B}},
3 <= r_B <= m,
```

which occurs infinitely often as a block of consecutive primes and is isolated on both sides by gaps tending to infinity.

It inherits

```text
(eta_2-eta_1)/(eta_3-eta_2) < 1/(B-1).
```

Now let `B_j -> infinity`.  Since `r_B` takes only the finitely many values `3,...,m`, a further subsequence has

```text
r_B = r_*
```

constant.

Therefore all corresponding PF-034 tangents

```text
Y_B := Y_{H_B}
```

have the same topological type

```text
boxed:
Y_B in M_{0,r_*+1}.
```

This is the key improvement over PF-043.

## 4. Exact gap-ratio pinching inside the fixed-topology tangent

PF-029 gives the cusp parabolics of `Y_H`.  The product of the first two adjacent peripheral loops represents the simple separating curve enclosing the first two finite cusps.  For

```text
d_1=eta_2-eta_1,
d_2=eta_3-eta_2,
```

direct matrix multiplication gives exactly

```text
|tr(Q_1 Q_2)|/2 = 1 + 2 d_1/d_2.
```

If `L_B` is the length of that simple separating geodesic, then

```text
boxed:
sinh(L_B/4)^2 = d_1/d_2.
```

Hence

```text
L_B = 4 asinh(sqrt(d_1/d_2))
    <= 4/sqrt(B-1)
    -> 0.
```

The curve is separating.  One component is a pair of pants with two cusps and geodesic boundary, of area `2 pi`; the other has fixed positive area because `r_*` is fixed and at least `3`.

Thus the family degenerates **inside one fixed moduli space** by a prime-gap-controlled separating pinch.

## 5. Direct spectral consequence: lambda_1(Y_B) -> 0 at fixed topology

No many-cusp theorem is needed here.

Use Fermi coordinates in a fixed-width central strip of the collar of the pinching curve:

```text
ds^2 = dr^2 + L_B^2 cosh(r)^2 dtheta^2.
```

Take a test function that is constant on the two sides, with constants chosen to have mean zero, and interpolate across `|r|<=1`.  Since the cross-sectional length in that strip is `O(L_B)`, its Dirichlet energy is

```text
O(L_B),
```

while its `L2` norm is bounded below by a positive constant depending only on the fixed topology.  The min--max principle therefore gives

```text
boxed:
0 < lambda_1(Y_B) <= C_{r_*} L_B
                 <= C'_{r_*}/sqrt(B-1)
                 -> 0.
```

For large `B` this is below `1/4`, so it is a genuine discrete `L2` eigenvalue of the finite-area tangent rather than part of its cusp continuum.

This is the standard spectral degeneration mechanism for a separating pinching geodesic; classical work of Schoen--Wolpert--Yau, Burger, Wolpert and later sharp estimates studies precisely this phenomenon.  No novelty is claimed for `L -> 0 => lambda_1 -> 0` on a fixed finite-type surface.

## 6. PF-034 implants these modulus-driven eigenvalues into the full prime-flute

Each `H_B` occurs infinitely often with exterior prime gaps tending to infinity, so PF-034 applies separately to every `B`:

```text
Spec_L2(Delta_{Y_B}) cap (0,1/4)
    subset sigma_ess(Delta_Xprime).
```

Set

```text
lambda_B=lambda_1(Y_B).
```

Then along the fixed-cardinality subsequence,

```text
boxed:
0 < lambda_B -> 0,
lambda_B in sigma_ess(Delta_Xprime),
Y_B all have the same number r_*+1 of cusps.
```

Consequently the accumulation established in PF-043 cannot be attributed only to tangent topology / increasing cusp count.  The **modulus generated by a ratio of consecutive prime gaps** already forces it at fixed topology.

## 7. Direct relation to the distinguished cuff lengths

This also gives the first clean spectral use of **relative fluctuations of the distinguished cuffs themselves** rather than a single cuff.

For an occurrence of a bounded pattern near a large prime scale `P`, let `ell_1(P), ell_2(P)` be the distinguished cuffs corresponding to the first two internal prime gaps `d_1,d_2`.  The prime-flute asymptotic gives

```text
ell_i(P)=2 log(4P/d_i)+o(1).
```

Therefore

```text
boxed:
exp(-(ell_1(P)-ell_2(P))/2) -> d_1/d_2.
```

Combining with the exact tangent identity,

```text
boxed:
sinh(L_B/4)^2
 = lim_{P->infinity}
   exp(-(ell_1(P)-ell_2(P))/2).
```

Thus a large **contrast** between neighboring distinguished cuffs survives the singular cusp-side tangent even though their common divergent part does not:

```text
ell_1-ell_2 -> +infinity
    => tangent separating length L_B -> 0
    => lambda_1(Y_B) -> 0
    => positive essential spectral values of X_prime -> 0.
```

Quantitatively, along this constructed family,

```text
lambda_1(Y_B)
  <= C L_B
  ~ 4C exp(-(ell_1-ell_2)/4)
```

in the corresponding large-scale tangent limit.

This does **not** contradict PF-032/PF-037: a single cuff still has only universal local spectral data.  The new signal is a relative two-cuff / two-gap modulus that becomes a nonlocal separating geodesic on the finite tangent.

## 8. Novelty audit

Known separately:

1. Pintz's Erdos--Rankin + Maynard--Tao isolation mechanism;
2. arbitrary/consecutive prime patterns in Maynard--Tao consequences such as Banks--Freiberg--Turnage-Butterbaugh;
3. fixed-topology hyperbolic spectral degeneration under a separating pinch;
4. the collar/min--max argument for small eigenvalues;
5. Weyl-sequence transplantation from pointed geometric limits.

Prime-flute-specific inputs are PF-004/PF-029/PF-034.

Targeted searches for combinations of `prime gaps`, `isolated prime clusters`, `punctured sphere`, `hyperbolic surface`, `fixed topology`, `essential spectrum` and `Laplacian` did not locate this composed theorem.  No novelty is claimed for the analytic-number-theory or hyperbolic-spectral ingredients individually.

The potentially new statement is narrow:

```text
engineered isolated recurrent prime patterns
  -> fixed-topology prime-flute tangents
  -> gap-ratio-controlled separating pinch
  -> lambda_1 -> 0
  -> modulus-driven positive points of the essential spectrum
     of the single deterministic prime-flute.
```

This materially strengthens PF-043 by removing its stated topological ambiguity.

## 9. Important limitations

- This is not a proof of RH and does not identify Riemann zeros.
- The small-eigenvalue response to pinching is universal once the tangent modulus is specified; the prime-specific content is that unconditional prime-pattern machinery forces those degenerating moduli to recur inside the exact prime-flute.
- The arithmetic lemma above is a non-uniform adaptation of Pintz's Section 4 proof.  Before using PF-045 in a formal paper theorem, that adaptation should be written as a standalone number-theoretic lemma with every dependency of the sieve constants exposed.
- We still have not shown that a generic pair of recurrent patterns with comparable nondegenerate moduli has distinct eigenvalues.  PF-045 instead forces spectral separation by driving one modulus to the boundary of moduli space.

## Formalization / audit targets

1. finite construction of geometrically separated prime offsets satisfying `h_t ∤ h_i-h_j` (CRT + Dirichlet as imported theorem);
2. the elementary inequality `d_1/d_2<1/(B-1)` for every subset of a geometric candidate set;
3. the exact PF-029 matrix identity `sinh(L/4)^2=d_1/d_2` for the first two cusp loops in arbitrary `r>=3`;
4. a standalone collar Rayleigh-quotient lemma `lambda_1 <= C L` for a fixed-topology separating pinch;
5. isolate the non-uniform Pintz adaptation as an explicit imported theorem interface.
