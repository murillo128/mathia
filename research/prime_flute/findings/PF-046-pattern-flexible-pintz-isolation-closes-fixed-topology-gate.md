# PF-046 — pattern-flexible Pintz isolation closes the fixed-topology modulus gate

**Status:** `POSITIVE / PROOF-LEVEL EXTENSION + LITERATURE-AUDITED`.

PF-045 isolated one remaining arithmetic gate: Pintz's published Theorem 2 chooses its bounded candidate offsets with a diameter controlled only by `k0`, whereas PF-045 needs, for each prescribed `B`, a fixed candidate set whose successive offsets grow by a factor `>B`.  This note audits Pintz's Section 4 proof at the level needed here, makes the required non-uniform extension explicit, and removes a second nuisance left implicit in PF-045: possible primes at the reflected offsets `ell-h_i`.

The conclusion is that the fixed-topology modulus-driven spectral mechanism of PF-045 does not require a uniform-in-pattern theorem.  For each fixed `B`, one may fix a very spread-out finite pattern first, then let the Pintz/Maynard--Tao asymptotic variable tend to infinity.  All constants and the starting point are allowed to depend on that fixed pattern.

## 1. What Pintz actually uses from the upper bound on the offsets

In Section 4 of Pintz, *On the ratio of consecutive gaps between primes* (arXiv:1406.2658v2), the proof of Theorem 2 starts by choosing

```text
an arbitrary set of m different primes H={h_1<...<h_m}
```

with

```text
m<C_3(m)<h_1<...<h_m<C_4(m),
h_t does not divide h_i-h_j  (i != j).
```

The proof then constructs a residue class `z mod W` such that

```text
(z+h_i,W)=1
```

for all candidates, while all other shifts in a growing Erdos--Rankin window are forced composite; Maynard--Tao supplies at least `k0` primes among `ell+h_i`.

A line-by-line audit of the proof shows that the **upper** bound `h_m<C_4(m)` is not used in any asymptotic estimate except to keep all pattern-dependent quantities bounded by a constant depending only on `m` (and ultimately only on `k0`).  The symbol `C_4(m)` appears at the initial choice and again in the final remark that possible primes at `ell-h_i` still lie in one bounded central block.

The other appearances of the offsets are of the following forms:

1. finite factors such as
   ```text
   prod_i (1-1/h_i)^(-1);
   ```
2. the fixed finite family of forbidden residue classes `-h_i mod p`;
3. prime divisors of the fixed nonzero differences `h_i-h_j`, written in Pintz's (4.47) as `O_m(1)` because his chosen offsets were uniformly bounded;
4. powers of the fixed `h_i` in the auxiliary factorization used in the Erdos--Rankin sieve.

For an **arbitrary fixed** finite `H`, these become `O_H(1)` constants.  As the sieve parameter `R` (equivalently `log L`) tends to infinity, every such constant is eventually below the growing sieve cutoffs.  The key estimates (Pintz (4.28), (4.31), (4.35)--(4.37), and the modified Bombieri--Vinogradov/Maynard step (4.43)--(4.50)) are unchanged after replacing a uniform threshold `L(k0)` by a threshold `L(k0,H)`.

This is consistent with Banks--Freiberg--Maynard's uniform Maynard--Tao theorem: their method explicitly permits the tuple offsets to be fixed (indeed, in the uniform version they may even grow slowly with the main asymptotic parameter), provided the pre-sieved progression keeps all candidate forms coprime to `W` and the finitely many exceptional prime divisors of differences are controlled.

Hence Pintz's proof yields the following non-uniform lemma.

### Fixed-pattern isolated-cluster lemma

Fix `k0>=2`.  Let `m` be sufficiently large for the Maynard--Tao step.  Let

```text
H={h_1<...<h_m}
```

be **any fixed set of distinct primes** satisfying

```text
h_1>m,
h_t does not divide h_i-h_j for all i!=j and all t.
```

Then there are arbitrarily large `ell` such that at least `k0` of the numbers

```text
ell+h_1,...,ell+h_m
```

are prime and the intervals immediately outside the fixed central `H`-window are prime-free with lengths tending to infinity on the Erdos--Rankin scale.  The implied constants and the first admissible `ell` may depend on `H`.

This is a proof-level non-uniform extraction from Pintz's Section 4, not a claim that Pintz states this version as a separate theorem.

## 2. Removing the reflected-candidate nuisance

Pintz's original congruence construction leaves both signs of the special shifts `h_i` unsieved.  He remarks that possible additional primes at

```text
ell-h_i
```

do not affect his theorem because they still lie in the same bounded block.

For PF-045 it is cleaner to eliminate them, so that **every prime in the central window lies at a positive candidate `ell+h_i`**.  This requires only a finite modification of Pintz's residue assignment.

Reserve `m` otherwise unused primes

```text
r_i in (R/2,R],  i=1,...,m,
```

from the `P_4` stage.  Since `H` is fixed, for large `R` we may require

```text
r_i > 2 h_m
```

and avoid the possible exceptional prime `q`.  Add the congruences

```text
z == h_i (mod r_i).
```

Then

```text
z-h_i == 0 (mod r_i),
```

so every `ell-h_i` is composite.  At the same time, for every positive candidate,

```text
z+h_j == h_i+h_j (mod r_i),
```

and

```text
0 < h_i+h_j < 2h_m < r_i,
```

so none of the desired `ell+h_j` is accidentally sieved out.

Only finitely many `P_4` primes have been reserved.  Pintz's argument uses a positive proportion of the primes in `(R/2,R]` and already tolerates finitely many forbidden choices at each stage, so deleting these `m` primes changes none of the asymptotics.

Thus the fixed-pattern lemma can be strengthened to:

```text
inside the whole central interval [ell-h_m,ell+h_m],
all primes occur at positions ell+h_i only.
```

Consequently the prime subset selected by Maynard--Tao is an actual block of consecutive primes and has no hidden negative-offset punctures in the prime-flute tangent.

## 3. Arbitrarily spread fixed patterns satisfying Pintz's divisibility condition

Fix `m` and `B>2`.  We can construct primes

```text
h_1<...<h_m
```

such that

```text
h_{j+1}>B h_j
```

and

```text
h_t does not divide h_i-h_j
```

for every distinct pair `i,j` and every `t`.

Inductively suppose `h_1,...,h_{j-1}` are chosen, all `>m`.  For each previous prime `h_t`, avoid the fewer than `m<h_t` residue classes

```text
h_i mod h_t,  i<j,
```

and also avoid `0 mod h_t`.  Choose one allowed nonzero class modulo every `h_t`, combine them by CRT, and apply Dirichlet's theorem to choose a prime `h_j` in the resulting reduced residue class with

```text
h_j>B h_{j-1}.
```

The congruence choices ensure that no old `h_t` divides a new difference `h_j-h_i`.  The new prime `h_j` cannot divide an old difference because it is larger than every old absolute difference, and it cannot divide `h_j-h_i` because it would then divide the distinct prime `h_i`.

So the candidate sets required by PF-045 exist for every `B`.

## 4. Every selected prime subset inherits the extreme ratio

Let

```text
a_1<a_2<a_3<... 
```

be any subset of a super-geometric candidate set, with at least three elements.  Since the selected candidates are themselves members of the sequence `h_j`,

```text
a_3 > B a_2.
```

For the first two consecutive prime gaps inside the selected block,

```text
d_1=a_2-a_1 < a_2,
d_2=a_3-a_2 > (B-1)a_2.
```

Therefore, independently of which candidates the sieve selects,

```text
boxed:
d_1/d_2 < 1/(B-1).
```

The one-sided sieving modification in Section 2 guarantees that these are genuinely the first two consecutive gaps of the whole isolated prime block, not merely of its positive-candidate subsequence.

## 5. Recurrence and fixed topology

For a fixed `B`, the central interval contains primes at a subset of the finite set `H_B` and nowhere else.  There are only finitely many subsets.  The fixed-pattern lemma supplies infinitely many successful translations, so one exact subset

```text
H_B^*={eta_1<...<eta_{r_B}},
3<=r_B<=m,
```

recurs infinitely often while the two exterior prime gaps tend to infinity.

Let `B_j -> infinity`.  Since `r_B` lies in the finite set `{3,...,m}`, pass to a subsequence with

```text
r_B=r_*
```

constant.  PF-034 then gives genuine pointed tangents

```text
Y_B = Y_{H_B^*} in M_{0,r_*+1}
```

all of the same topological type.

This closes the only arithmetic uniformity gate stated in PF-045.

## 6. Spectral consequence survives unchanged

For the first three offsets of the recurrent pattern, PF-029 gives exactly

```text
sinh(L_B/4)^2=d_1/d_2,
```

where `L_B` is the simple separating geodesic enclosing the first two finite cusps of the tangent.  Hence

```text
L_B=4 asinh(sqrt(d_1/d_2))
   <=4/sqrt(B-1)
   ->0.
```

A collar Rayleigh test on the fixed-topology finite-area tangent gives

```text
0<lambda_1(Y_B)<=C_{r_*} L_B ->0.
```

For large `B`, `lambda_1(Y_B)<1/4`; PF-034 transplants it to the essential spectrum of the single infinite prime-flute:

```text
boxed:
lambda_1(Y_B) in sigma_ess(Delta_Xprime),
0<lambda_1(Y_B)->0,
Y_B all in the same M_{0,r_*+1}.
```

Thus the accumulation is genuinely **modulus-driven at fixed topology**.

For occurrences of the same bounded pattern near prime scale `P`, the distinguished cuffs satisfy

```text
ell_i(P)=2 log(4P/d_i)+o(1),
```

so

```text
boxed:
exp(-(ell_1(P)-ell_2(P))/2) -> d_1/d_2
                             = sinh(L_B/4)^2.
```

Therefore the relative cuff fluctuation, not a single cuff, survives into a true finite-type hyperbolic modulus and forces real Laplace spectrum:

```text
large (ell_1-ell_2)
 -> small tangent separating geodesic
 -> small tangent eigenvalue
 -> positive essential spectral point of X_prime.
```

This is not a generating function of prime gaps and does not use a Selberg product for the infinite flute.

## 7. Novelty audit

Known separately:

- Pintz's Erdos--Rankin + Maynard--Tao isolated-cluster proof;
- Banks--Freiberg--Maynard's uniform Maynard--Tao framework;
- CRT/Dirichlet construction of finite prime offset sets;
- hyperbolic collar degeneration and small eigenvalues;
- pointed geometric convergence and Weyl transplantation.

The new content claimed here is limited to the **proof-level extraction and composition** needed by the prime-flute construction:

1. Pintz's Section 4 remains valid for an arbitrary fixed spread-out prime candidate set when constants are allowed to depend on that set;
2. a finite extra congruence assignment removes the otherwise possible reflected candidates `ell-h_i` without disturbing the Maynard step;
3. this makes PF-045's recurrent exact patterns genuinely one-sided and closes its stated arithmetic gate.

Targeted literature searches found no theorem formulated as this exact fixed-pattern + two-sided-isolation + prescribed-ratio statement.  The extension should therefore be cited as an explicit lemma proved by modifying Pintz, not attributed verbatim to Pintz.

## 8. Remaining limitations

- This does not connect the resulting eigenvalues to Riemann zeros.
- The spectral response `L -> lambda_1` is standard hyperbolic degeneration; the prime-specific statement is the forced recurrence of the moduli inside the exact prime-flute.
- The argument forces spectral variation by approaching the boundary of a fixed moduli space.  It still does not prove that two generic nondegenerate recurrent gap patterns of equal cardinality have different unmarked spectra.
- Before publication, the fixed-pattern Pintz lemma should be written in conventional analytic-number-theory notation as a standalone lemma, with the finite `P_4` reservation incorporated directly into the congruence construction.  The dependence on `H` is now explicit rather than hidden, but a specialist number-theory review remains appropriate.
