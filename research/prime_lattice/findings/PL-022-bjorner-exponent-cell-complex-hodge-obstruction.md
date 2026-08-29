# PL-022 — Björner already realizes the exponent cutoff as a cell complex; RH is Euler-characteristic cancellation, not ordinary Hodge spectrum

## Claim

Let

```text
E(alpha) = sum_p alpha_p log p
```

for a finite-support exponent vector `alpha=(alpha_p)_p`, and for `X>=1` define the finite energy down-set

```text
M_X = { alpha in N_0^(P) : E(alpha) <= log X }.
```

This is exactly the multicomplex of positive integers `n<=X` under the identification `alpha=v(n)`. Its square-free sector

```text
Delta_X = M_X intersect {0,1}^(P)
```

is exactly Anders Björner's number-theoretic simplicial complex: a face is the set of prime coordinates occurring in a square-free integer at most `X`.

Björner's 2011 construction therefore already supplies a literal topological realization of both objects central to this research line:

1. the square-free Boolean part is a canonical simplicial complex `Delta_X`;
2. the full exponent down-set `M_X` has a CW realization `tilde Delta_X` with one closed cell for every integer/exponent vector, with divisibility represented by cell inclusion.

The Riemann hypothesis is equivalent to square-root-scale cancellation of the Euler characteristic in either realization:

```text
Mertens M(X) = - reduced_chi(Delta_X),
RH <=> M(X) = O_epsilon(X^(1/2+epsilon)),
```

and, for the full-lattice CW realization,

```text
Liouville L(X) = sum_(n<=X) (-1)^Omega(n) = - chi(tilde Delta_X),
RH <=> L(X) = O_epsilon(X^(1/2+epsilon)).
```

The square-free complex is moreover shifted. Hence its ordinary combinatorial Hodge Laplacians have integer spectra by Duval–Reiner. Finite-dimensional Hodge theory then gives

```text
dim ker L_k(Delta_X) = beta_k(Delta_X)
```

and the heat supertrace is independent of the heat parameter:

```text
Str exp(-t L(Delta_X))
   = sum_k (-1)^k beta_k(Delta_X)
   = reduced_chi(Delta_X)
   = -M(X),             t>0.
```

Thus the most direct topological/spectral route is already classical and has a sharp limitation: **RH lives in alternating cancellation among Hodge zero-mode multiplicities, while the standard nonzero Hodge spectra of the shifted square-free complexes are integral combinatorial spectra.** The ordinary unweighted simplicial Laplacian is therefore not a Hilbert–Pólya operator whose eigenvalues are the Riemann-zero ordinates.

**Evidence/status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION` for the ordinary unweighted topological/Hodge route. Björner's complexes, their Euler-characteristic RH criteria, shiftedness, Betti formulae, and the full multicomplex CW realization are literature. Duval–Reiner's Laplacian integrality theorem is literature. The expression of Björner's Betti numbers as a `log 2`-thick energy boundary-shell count, and the Hodge-supertrace consequence in exponent coordinates, are exact derived specializations. No novelty is claimed for the underlying topology or Laplacian theory.

## The square-free Boolean sector is Björner's simplicial complex

For a square-free integer

```text
n = product_(p in S) p,
```

its exponent vector is the indicator `1_S`. The energy cutoff is

```text
E(1_S) = sum_(p in S) log p = log(product_(p in S) p) <= log X.
```

Therefore

```text
Delta_X
 = { S finite subset of primes : sum_(p in S) log p <= log X }.
```

This is Björner's definition `Delta_X={P(k): k squarefree, k<=X}` written in the intrinsic exponent-lattice coordinates of this line. It is a down-set because deleting a prime coordinate decreases the energy.

Since `mu(k)=(-1)^|P(k)|` on square-free integers and vanishes otherwise, Björner observes exactly

```text
M(X) = sum_(n<=X) mu(n) = - reduced_chi(Delta_X).
```

Consequently the classical Mertens criterion is literally a topological statement:

```text
RH
<=> for every epsilon>0,
    |reduced_chi(Delta_X)| = O(X^(1/2+epsilon)).
```

This is an exact RH reformulation, not a proof mechanism. Björner explicitly notes that the Betti-number information developed in the paper does not by itself improve control of this Euler-characteristic cancellation.

## Shiftedness makes the entire Betti vector a `log 2` outer-shell count

Björner proves that `Delta_X` is shifted when the prime vertices are ordered

```text
2 < 3 < 5 < ...
```

because replacing a prime factor by a smaller prime decreases the represented integer. A standard theorem for shifted complexes then gives a wedge-of-spheres homotopy type and identifies the Betti numbers. His explicit formula is

```text
beta_k(Delta_X)
 = sigma^odd_(k+1)(X) - sigma^odd_(k+1)(X/2)
```

or equivalently

```text
beta_k(Delta_X)
 = #{ b : b odd and squarefree,
          X/2 < b <= X,
          Omega(b)=k+1 }.
```

In exponent coordinates, the **faces counted by this Betti formula** are exactly the square-free vectors `alpha` satisfying

```text
alpha_2 = 0,
log X - log 2 < E(alpha) <= log X,
|alpha| = k+1.
```

Equivalently, they are faces lying inside `Delta_X` for which adding the smallest-prime basis direction `e_2` crosses the cutoff:

```text
alpha in Delta_X,
but alpha + e_2 notin Delta_X.
```

Thus **the entire reduced Betti vector is determined by a boundary shell of fixed energy thickness `log 2`**. This is an indexing/counting statement from shifted-complex theory; it does not assert that arbitrary homology cycle representatives have literal chain support only inside that shell. The energy-shell reading is immediate from Björner's theorem and is not claimed as new topology.

Björner also proves

```text
sum_k beta_k(Delta_X)
 = 2X/pi^2 + O(X^theta),   every theta>17/54,
```

while separately

```text
sum_(k even) beta_k(Delta_X) ~ X/pi^2,
sum_(k odd)  beta_k(Delta_X) ~ X/pi^2.
```

Hence the RH-sensitive quantity is not small topology. Each parity sector contains order-`X` homology, and

```text
M(X) = sum_k (-1)^(k-1) beta_k(Delta_X)
```

asks for cancellation down to essentially the square-root scale between two extensive homological masses.

## The full exponent lattice already has a CW realization

The result is not confined to the `{0,1}` sector. Björner explicitly passes from the simplicial complex of square-free integers to the multicomplex of **all** integers `n<=X`.

In prime-exponent coordinates this multicomplex is precisely

```text
M_X = { alpha in N_0^(P) : <alpha,log p> <= log X }.
```

Coordinatewise decrease preserves membership, so it is the finite weighted order ideal cut out of the positive exponent cone by the same linear energy functional used throughout this research line.

Björner constructs a CW realization `tilde Delta_X` with the following properties:

```text
positive integers n<=X  <->  closed cells c(n),
dim c(n) = Omega(n)-1,
n_1 divides n_2  <=>  c(n_1) subseteq c(n_2).
```

Thus this is not merely an analogy to the prime-exponent lattice: cell incidence records divisibility, while cell dimension records the total exponent degree

```text
Omega(n) = sum_p v_p(n).
```

Its Euler characteristic is

```text
chi(tilde Delta_X)
 = #{n<=X : Omega(n) odd} - #{n<=X : Omega(n) even}
 = -L(X),
```

where `L(X)` is the summatory Liouville function. Björner proves that the square-root growth criterion for `L(X)` is equivalent to that for the Mertens function, hence

```text
RH <=> |chi(tilde Delta_X)| = O_epsilon(X^(1/2+epsilon)).
```

This essentially classicalizes the broad proposal “turn the entire exponent lattice into a cell complex whose topology sees RH.” That construction already exists.

A boundary condition matters here: the full multicomplex admits a cellular realization whose homotopy type is controlled under Björner's well-connected-cell hypothesis, but unlike the square-free abstract simplicial complex, the detailed CW structure is not a unique canonical metric/spectral object. Therefore no canonical full-lattice Laplacian is being imported from this result.

## Ordinary Hodge spectrum does not turn this into Hilbert–Pólya

For the canonical square-free complex, however, the usual simplicial chain complex supplies a completely standard Hodge Laplacian

```text
L_k = partial_(k+1) partial_(k+1)^* + partial_k^* partial_k.
```

Because `Delta_X` is shifted, Duval and Reiner's theorem applies: **every combinatorial Laplacian spectrum is integral**, with the nonzero spectrum determined combinatorially from degree data.

For any finite chain complex with the standard adjoint, Hodge theory gives

```text
ker L_k ~= reduced H_k,
```

so the multiplicity of the zero eigenvalue is `beta_k`. On the total even/odd chain space let

```text
D = partial + partial^*,
L = D^2.
```

For every positive eigenvalue `lambda`, `D` pairs the even and odd `lambda`-eigenspaces (with inverse `lambda^(-1)D`). Their heat traces therefore cancel in the supertrace, leaving only harmonic zero modes:

```text
Str exp(-tL)
 = sum_k (-1)^k beta_k
 = reduced_chi(Delta_X)
 = -M(X).
```

This identity is exact for every `t>0`. Introducing the standard heat operator does not create a new scale at which Riemann zeros emerge; its graded trace collapses to the same Euler characteristic for all `t`.

The direct Hilbert–Pólya reading is therefore obstructed in two distinct ways:

1. the finite nonzero Hodge eigenvalues are integers because the complex is shifted;
2. the RH-equivalent information in the canonical Hodge picture is already carried by **zero-eigenvalue multiplicities and their alternating cancellation across dimensions**, not by a nonzero eigenvalue set matching the ordinates of zeta zeros.

This rules out only the **ordinary unweighted finite simplicial Hodge Laplacian as a literal zero-spectrum mechanism**. It does not rule out a weighted, nonlocal, adelic, asymptotically rescaled, persistent, or otherwise enriched operator. But any such enrichment is additional mathematical structure and must be justified independently; the exponent complex itself does not supply it for free.

## Prior art and novelty audit

The exact topological object is not new:

- Björner's 2011 paper defines the square-free divisibility complex, identifies Mertens with its reduced Euler characteristic, states the RH growth equivalence, proves shiftedness and the explicit Betti formula, and constructs the full-integer multicomplex CW realization whose Euler characteristic is the summatory Liouville function.
- Duval–Reiner (2002) prove that shifted simplicial complexes have integral combinatorial Laplacian spectra, so the standard spectral structure available on Björner's `Delta_X` is classical as well.
- Searches combining Björner's complex, Mertens/Liouville cancellation, simplicial Laplacians, and RH did not reveal a reliable theorem upgrading the unweighted Hodge spectrum into a zero-localizing mechanism. The Hodge-supertrace identity above is instead an elementary consequence of finite Hodge theory and reproduces the already-known Euler-characteristic encoding.

The result is therefore a **prior-art redirect plus obstruction**, not a novelty claim. Even Björner's paper explicitly says its Betti results fall short of controlling the Euler-characteristic growth and suggests that only deeper invariants might add information.

## Boundary conditions and adversarial checks

### The RH equivalence is only an Euler-characteristic reformulation

Writing `M(X)` or `L(X)` as an Euler characteristic does not explain their square-root cancellation. Any proposed proof that merely restates the Mertens/Liouville criterion in topological language is circular at the RH level.

### Betti asymptotics do not imply Euler-characteristic cancellation

The total Betti number and the two parity totals are each order `X`. Their leading terms cancel, but RH requires much finer control of the residual alternating difference. Knowing the wedge-of-spheres homotopy type and coarse Betti growth is therefore insufficient.

### Laplacian integrality is specific to the canonical shifted square-free complex

Duval–Reiner applies to the ordinary unweighted combinatorial Laplacians of shifted simplicial complexes. A weighted Laplacian using `log p`, a nonlocal operator, or a limiting renormalization need not be integral and is not ruled out by this finding.

### Full-lattice CW spectra are not canonical here

Björner's all-integer realization depends on a CW-string construction. Its incidence/divisibility and homotopy conclusions are meaningful, but this finding does not pretend that it produces a unique self-adjoint operator on the full exponent lattice.

### Integer finite spectra do not exclude arbitrary rescaled limits

A sequence of rescaled integer eigenvalues can converge to noninteger values. The obstruction is only to interpreting the raw ordinary finite Hodge spectra themselves as the Riemann-zero spectrum. Any meaningful limiting operator would require a specified scaling and convergence theorem.

## Falsification / audit test

Withdraw or narrow this finding if any of the following fails:

1. Björner's `Delta_X` is exactly the energy-cut square-free exponent complex `M_X intersect {0,1}^(P)`.
2. `M(X)=-reduced_chi(Delta_X)` and the standard Mertens square-root growth criterion is equivalent to RH.
3. `Delta_X` is shifted and its Betti numbers count odd square-free `b` in `(X/2,X]` by prime-factor degree.
4. The full set `{v(n):n<=X}` is exactly Björner's integer multicomplex, and his CW realization has one cell per integer with divisibility represented by cell inclusion.
5. Its Euler characteristic is `-L(X)` and the corresponding square-root growth criterion is equivalent to RH.
6. Duval–Reiner's Laplacian-integrality theorem applies to each finite shifted `Delta_X`.
7. Finite Hodge theory gives `Str exp(-tL)=reduced_chi(Delta_X)` for every `t>0`.

All seven points are independent of RH as statements/equivalences; none assumes that the required square-root bounds actually hold.

## Consequence for the research line

The broad search for a topological realization of the prime-exponent lattice should stop: **both the square-free hypercube cutoff and the full exponent multicomplex already have classical cell-complex realizations tied exactly to RH-equivalent cancellation functions.**

The surviving question is narrower and harder. A genuinely useful geometric or spectral mechanism must explain why the large even/odd topological sectors cancel at square-root scale, or introduce additional justified structure that turns this cancellation into positivity, self-duality, a trace formula, or a zero-localizing operator. Ordinary Euler characteristic, Betti data, wedge-of-spheres topology, and the raw unweighted Hodge spectrum do not do that.

## Sources

- Anders Björner, “A cell complex in number theory,” *Advances in Applied Mathematics* **46**(1–4) (2011), 71–85. DOI: `10.1016/j.aam.2010.09.007`. arXiv: `1101.5704`.
- Art M. Duval, Victor Reiner, “Shifted simplicial complexes are Laplacian integral,” *Transactions of the American Mathematical Society* **354**(11) (2002), 4313–4344. DOI: `10.1090/S0002-9947-02-03082-9`.
