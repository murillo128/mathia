# PL-029 — Redheffer already turns the finite exponent down-set into an RH-equivalent determinant, but its spectrum is incidence-chain combinatorics

## Claim

The most canonical finite-dimensional matrix obtained from the divisibility order on the prime-exponent lattice is already classical prior art.

For

```text
D_N = { v(n) : 1 <= n <= N }
    = { alpha in N_0^(P) : <alpha,(log p)_p> <= log N },
```

coordinatewise order is exactly divisibility:

```text
v(i) <= v(j)  <=>  i | j.
```

Let `Z_N` be the incidence-zeta matrix of this finite down-set,

```text
(Z_N)_(i,j) = 1_(i|j).
```

The classical Redheffer matrix `R_N` is obtained by replacing the column indexed by the minimum element `1` with a column of ones. Thus, in prime-lattice language, it is a rank-one boundary perturbation of the incidence-zeta operator of the energy-truncated exponent cone.

Exactly,

```text
det R_N = M(N) = sum_(n<=N) mu(n),
```

and therefore

```text
RH  <=>  for every epsilon>0,
          |det R_N| = O_epsilon(N^(1/2+epsilon)).
```

However, this does **not** produce a new spectral mechanism for the zeta zero divisor. Vaughan proved that

```text
det(lambda I - R_N)
  = (lambda-1)^(N-floor(log_2 N)-1) P_N(lambda),
```

where `P_N` has degree only `floor(log_2 N)+1`, and its coefficients count ordered factorizations. In exponent coordinates those factorizations are precisely ordered additive decompositions of lattice vectors into nonzero positive-cone vectors.

Wilf further generalized the construction from integer divisibility to **every finite poset with a least element**: replacing the least-element column of the incidence-zeta matrix by ones gives determinant equal to the sum of the poset Möbius function. Hence the basic determinant/Möbius phenomenon is an incidence-algebra identity, not structure special to the rational-prime frequency vector `(log p)_p`.

**Evidence/status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION` for the route

```text
finite unweighted divisibility/exponent-lattice incidence matrix
    -> determinant or ordinary eigenvalue spectrum
    -> new critical-line / zeta-zero mechanism.
```

This does not rule out weighted, self-adjoint, nonlocal, archimedean/adelic, or analytically completed operators built from the lattice. It classicalizes and sharply delimits the unweighted finite-incidence route.

## Exact rank-one incidence derivation

The set `{1,...,N}` is a finite down-set for divisibility. Under the exponent map it is the finite down-set `D_N` above, because

```text
beta <= alpha coordinatewise
    => <beta,log p> <= <alpha,log p>.
```

Order the integers naturally. Since `i|j` implies `i<=j`, `Z_N` is upper triangular with diagonal entries one, so

```text
det Z_N = 1.
```

Its inverse is the ordinary incidence-algebra Möbius matrix,

```text
(Z_N^(-1))_(i,j)
  = mu(j/i)   if i|j,
  = 0         otherwise.
```

In particular the first row is

```text
(1, mu(2), mu(3), ..., mu(N)).
```

Let `e_1` be the basis vector of the minimum element and let `1_vec` be the all-ones column. Replacing the first column of `Z_N` by ones gives

```text
R_N = Z_N + (1_vec-e_1) e_1^T.
```

This is rank one. The matrix determinant lemma therefore gives

```text
det R_N
 = det Z_N * (1 + e_1^T Z_N^(-1)(1_vec-e_1))
 = 1 + sum_(j=2)^N mu(j)
 = M(N).
```

This exposes where the RH-equivalent scalar enters. The bulk incidence matrix is unipotent and has determinant one; the Mertens sum appears after one boundary column couples every lattice point back to the minimum element.

The identity is finite and algebraic. It requires neither the Euler product nor analytic continuation.

## Where analytic continuation actually enters

The equivalence with RH is the classical Mertens criterion, not a new consequence of matrix spectral theory.

Vaughan recalls the standard identity

```text
1/zeta(s)
  = s * integral_1^infinity M(x) x^(-s-1) dx,
```

first justified in `Re(s)>1` by absolute convergence. A bound

```text
M(x)=O_epsilon(x^(1/2+epsilon))
```

then makes the integral locally uniformly convergent in every half-plane `Re(s)>1/2+epsilon`, giving the zero-free continuation required for RH after the usual limiting argument.

Thus one must keep the domains separate:

```text
finite determinant identity det R_N=M(N)
    -> exact for every N

Mertens square-root bound
    -> via Mellin/Dirichlet analysis
    -> zero-free half-plane / RH.
```

The matrix identity itself does not analytically continue `zeta`, does not supply the functional equation, and does not independently single out the Hermitian self-dual axis found in `PL-014`.

## The nontrivial spectrum has only logarithmic dimension

Vaughan determines the characteristic polynomial in terms of ordered factorizations. Put

```text
L = floor(log_2 N).
```

For `k>=1`, let `D_k(m)` be the number of ordered factorizations

```text
m = m_1 ... m_k,
qquad m_r >= 2,
```

and let

```text
S_k(N) = sum_(m<=N) D_k(m).
```

Then

```text
det(lambda I-R_N)
 = (lambda-1)^(N-L-1) P_N(lambda),
```

with

```text
P_N(lambda)
 = (lambda-1)^(L+1)
   - sum_(k=1)^L (lambda-1)^(L-k) S_k(N).
```

Consequently exactly

```text
N-floor(log_2 N)-1
```

eigenvalues are equal to `1`, counted algebraically. Only `floor(log_2 N)+1` eigenvalues remain nontrivial.

The logarithm is not mysterious geometrically. Every strict step in a divisibility chain multiplies the integer by at least `2`, so a chain below `N` has length at most `floor(log_2 N)+1`.

In exponent coordinates an ordered factorization is exactly an ordered additive decomposition

```text
v(m)
  = alpha_1 + ... + alpha_k,
qquad alpha_r != 0,
```

with every `alpha_r` in the positive finite-support cone. Therefore the coefficients of the reduced characteristic factor are chain/decomposition statistics of the exponent lattice itself.

This is useful structural information, but it also shows that the finite Redheffer spectrum is not an unexplored Hilbert–Pólya spectrum hiding one mode per integer. Almost the entire finite-dimensional spectrum is the trivial eigenvalue `1`; the remaining factor packages ordered multiplicative-chain combinatorics.

## Poset universality separates incidence geometry from prime-frequency geometry

Wilf defines, for an arbitrary finite poset `S` with minimum `0`, its Redheffer matrix by taking the incidence-zeta matrix of `S` and replacing the `0` column by ones. He proves

```text
det R(S) = sum_(x in S) mu_S(0,x),
```

while the permanent counts chains containing the minimum element.

For the integer divisibility poset, `mu_S(1,n)` is the ordinary arithmetic Möbius function and the formula becomes `M(N)`. But the determinant construction itself survives unchanged for unrelated posets.

This gives a discriminating control for the prime-lattice program:

```text
coordinatewise divisibility order + incidence Möbius inversion
```

is not enough to distinguish the rational primes from a generic finite poset. The exact values `log p`, the archimedean place, additive Fourier duality, the functional equation, and the completed explicit formula are absent from `R_N`.

Equivalently, the energy vector `(log p)_p` chooses which lattice points lie in `D_N`; once the finite poset has been chosen, the Redheffer entries themselves remember only order/incidence.

## Novelty audit and modern spectral work

The construction is old and has been studied specifically because of its RH-equivalent determinant.

Primary anchors:

- R. C. Vaughan, **“On the eigenvalues of Redheffer’s matrix, I,”** in *Number Theory with an Emphasis on the Markoff Spectrum*, Lecture Notes in Pure and Applied Mathematics 147, Marcel Dekker, 1993, pp. 283–296. Author PDF: https://personal.science.psu.edu/rcv4/personal/Publications/REDCONF.pdf. Vaughan proves `det R_N=M(N)`, records the RH equivalence through the Mertens bound, derives the characteristic polynomial through Dirichlet convolution, and proves the exact multiplicity of the eigenvalue `1`.
- R. C. Vaughan, **“On the eigenvalues of Redheffer’s matrix, II,”** *Journal of the Australian Mathematical Society* **60**(2) (1996), 260–273. DOI: https://doi.org/10.1017/S1446788700037654. Refines the location of the nontrivial eigenvalues near `1`.
- Herbert S. Wilf, **“The Redheffer Matrix of a Partially Ordered Set,”** *Electronic Journal of Combinatorics* **11**(2) (2004), R10. DOI: https://doi.org/10.37236/1867; arXiv: https://arxiv.org/abs/math/0408263. Gives the chain/factorization interpretation and the finite-poset generalization `det R(S)=sum_x mu(0,x)`.

Modern work confirms that this remains an active linear-algebraic object rather than an overlooked construction. François Clément and Stefan Steinerberger, **“On the largest singular vector of the Redheffer matrix,”** *Linear Algebra and its Applications* **725** (2025), 96–114, DOI https://doi.org/10.1016/j.laa.2025.07.003, shows that the leading singular vector strongly reflects divisor-richness and gives a quantitative approximation by the inverse-divisor-sum vector. Jeffery Kline, **“A sparser matrix representation of the Mertens function,”** *Linear Algebra and its Applications* **581** (2019), 148–165, DOI https://doi.org/10.1016/j.laa.2019.07.021, constructs a substantially sparser `(0,1)` matrix with the same Mertens determinant property and even fewer eigenvalues different from `1`.

These later variants are a useful novelty control: an RH-equivalent determinant representation of `M(N)` is not unique, so a new matrix formulation needs an additional invariant or theorem beyond reproducing the determinant.

No novelty is claimed for Redheffer matrices, incidence algebras, Möbius inversion, Vaughan’s spectrum, Wilf’s poset generalization, or the Mertens criterion. The derived prime-lattice contribution is the exact identification of this literature with the energy-truncated exponent down-set and the resulting boundary on what a new geometric/spectral mechanism must add.

## Boundary of the obstruction

This finding does **not** prove that spectral estimates for `R_N` can never yield a new proof of a Mertens bound. A clever new estimate on the nontrivial eigenvalues could still have number-theoretic content. The negative is about mechanism and novelty: the basic finite incidence matrix, its determinant criterion, and its chain spectrum are already classical and do not by themselves explain critical-line localization.

It also leaves open matrices/operators that genuinely use data discarded by the unweighted incidence relation, for example:

- weights depending explicitly on `log p`, `log n`, or prime powers rather than only `i|j`;
- self-adjoint or indefinite forms whose positivity is tied to the completed Weil formula;
- archimedean/adelic corrections implementing the `s <-> 1-s` Fourier–Mellin duality of `PL-014`;
- nonlocal kernels or scattering/trace constructions in which zeros occur as actual spectral or resonance data rather than only through the determinant `M(N)`;
- asymptotic operators whose limiting process preserves analytic-continuation information rather than merely finite Möbius sums.

A proposal in one of these classes must still be novelty-audited against the existing GCD/LCM, Nyman, Bost–Connes, Connes/Weil, and Redheffer literatures.

## Audit / falsification tests

The finding can be falsified or materially narrowed by any of the following:

1. the finite exponent cutoff `D_N` is not isomorphic, under coordinatewise order, to `{1,...,N}` under divisibility;
2. the inverse of its incidence-zeta matrix is not the Möbius incidence matrix;
3. the rank-one determinant calculation above fails to give `M(N)`;
4. Vaughan’s factorization of the characteristic polynomial or exact multiplicity `N-floor(log_2 N)-1` of the eigenvalue `1` is misstated;
5. ordered factorizations fail to correspond bijectively to ordered decompositions of exponent vectors into nonzero positive-cone vectors;
6. Wilf’s determinant theorem does not generalize the same column-replacement construction to arbitrary finite posets with a least element;
7. a proposed weighted/completed operator uses additional arithmetic structure not present in `R_N`, in which case it lies outside the obstruction rather than contradicting it.

The first six are exact classical/algebraic checks. The seventh is the intended research boundary.

## Consequence for the research line

`PL-022` already showed that the same exponent cutoff has a classical simplicial/CW topology whose Euler characteristic is the Mertens/Liouville cancellation. `PL-029` now adds the linear-algebraic incidence counterpart:

```text
energy-truncated exponent down-set
    -> divisibility incidence-zeta matrix Z_N
    -> one boundary-column replacement
    -> Redheffer matrix R_N
    -> det R_N = M(N)
    -> RH-equivalent square-root determinant bound

ordinary spectrum of R_N
    -> all but O(log N) eigenvalues exactly 1
    -> reduced characteristic coefficients = ordered lattice decompositions
```

So both the most obvious topological and finite incidence-spectral encodings of the exponent lattice are classical. The remaining RH problem is again not how to package Möbius cancellation into a geometric invariant, but what **additional completed arithmetic structure forces the cancellation to the square-root scale and ties it to the self-dual line**.