# VIS-360 — pooled rescaling prices colliding Wang cluster centers

## Claim

Fix a finite Wang asymptotic depth `q>=1`, an invertible diagonal tail matrix

`D_beta=diag(beta_1,...,beta_q)`,

a compact positive center range `0<r<=c<=R`, and a fixed normalized radius bound `T>=1`.

For `N>=q`, choose nodes

`x_j=c+rho t_j`, `1<=j<=N`,

with `|t_j|<=T` and `0<rho<=rho_0`, where `rho_0 T<=r/2`. Let

`V=(x_j^k)_(1<=k<=q,1<=j<=N)`,
`A=D_beta V`,

and let `S` be the normalized polynomial-sampling matrix

`S=(t_j^d)_(1<=j<=N,0<=d<=q-1)`.

Assume the pooled normalized cloud has a uniform degree-`q-1` moment floor:

`lambda_min((1/N) S^* S) >= gamma > 0`.

Then there are constants `C_1,C_2>0`, depending only on `q,r,R,T,D_beta,gamma`, such that

`C_1 sqrt(N) rho^(q-1) <= s_q(A) <= C_2 sqrt(N) rho^(q-1)`.

Thus any collection of subclusters whose centers themselves collide inside an outer width `rho` is, after pooling at that outer scale, just another one-cluster polynomial-sampling problem whenever the rescaled cloud keeps a nondegenerate `q`-moment Gram. The decomposition into subclusters is irrelevant to the fixed-depth quotient floor in that regime.

In particular, suppose the empirical measures

`mu_N=(1/N) sum_j delta_(t_j)`

converge weakly on `[-T,T]` to a probability measure `mu` whose support contains at least `q` distinct points. Then the degree-`q-1` moment Gram of `mu` is positive definite, so the uniform Gram hypothesis holds for all sufficiently large `N`; hence the same `sqrt(N) rho^(q-1)` law follows.

Therefore **collapsing inter-center separation is not by itself a new compact Wang escape**. It becomes a genuinely new conditioning regime only when the pooled cloud is still degenerate after the correct outer rescaling — equivalently, when its normalized polynomial-sampling Gram loses a positive eigenvalue, so fewer than `q` outer-scale polynomial modes remain stably visible and finer scales or weights must be priced.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL RECTANGULAR-VANDERMONDE/POLYNOMIAL-SAMPLING GEOMETRY + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This result uses the current unweighted Euclidean coefficient norm and fixed asymptotic depth. It does not classify a hierarchy whose pooled normalized Gram is itself degenerating, nonuniform column weights, a changing coefficient norm, growing `q`, scale escape, or infinite-dimensional topologies.

## 1. The pooled cloud is one Taylor block at its outer scale

For `y in C^q`, write

`p_y(x)=sum_(k=1)^q conjugate(y_k) beta_k x^k=x Q_y(x)`,

with `deg Q_y<=q-1`. Since `D_beta` is fixed and invertible, and `c` stays in `[r,R]`, the ordinary coefficient norm of `Q_y` and its Taylor-coefficient norm at `c` are uniformly equivalent to `||y||_2`.

Write

`Q_y(c+rho t)=sum_(d=0)^(q-1) b_d t^d`,

where

`b_d=rho^d Q_y^(d)(c)/d!`.

If `a(c)` is the Taylor vector `(Q_y^(d)(c)/d!)_(d=0)^(q-1)`, then

`b=D_rho a(c)`,
`D_rho=diag(1,rho,...,rho^(q-1))`.

Uniform invertibility of translation on the fixed finite-dimensional polynomial space gives

`||a(c)||_2 >= c_0 ||y||_2`.

Since `0<rho<=1`,

`||b||_2 >= rho^(q-1) ||a(c)||_2 >= c_0 rho^(q-1) ||y||_2`.

This step does not know whether the `t_j` came from one cloud, several subclusters, or colliding cluster centers. Once all points are expressed in one outer coordinate, their only remaining geometric information is the pooled normalized sampling matrix `S`.

## 2. A nondegenerate pooled moment Gram gives the lower bound

Because `x_j>=r/2`,

`||A^* y||_2^2 = sum_j |x_j Q_y(x_j)|^2 >= (r/2)^2 sum_j |Q_y(x_j)|^2`.

But

`(Q_y(x_j))_j = S b`,

so the Gram hypothesis gives

`||S b||_2^2 >= gamma N ||b||_2^2`.

Combining with the Taylor rescaling yields

`||A^* y||_2^2 >= C N rho^(2(q-1)) ||y||_2^2`.

Taking the infimum over unit `y` proves

`s_q(A) >= C_1 sqrt(N) rho^(q-1)`.

The key point is that the whole colliding-center configuration contributes through one pooled moment Gram. If that Gram stays positive definite, no further pairwise center-separation factor appears in the smallest fixed-depth singular scale.

## 3. The exponent is still sharp

Take

`Q_0(x)=(x-c)^(q-1)`,
`p_0(x)=x Q_0(x)`.

After normalizing the corresponding fixed coefficient direction in the Wang row space, every sample satisfies

`|p_0(x_j)| <= C rho^(q-1) |t_j|^(q-1) <= C T^(q-1) rho^(q-1)`.

Therefore

`||A^* y_0||_2^2 <= C N rho^(2(q-1))`,

which gives

`s_q(A) <= C_2 sqrt(N) rho^(q-1)`.

So the outer pooled width is the exact fixed-depth collision exponent whenever the normalized cloud retains all `q` polynomial modes.

## 4. Weak limits with at least `q` support points automatically pass the Gram gate

Let

`G_mu=(int t^(a+b) dmu(t))_(0<=a,b<=q-1)`.

For a coefficient vector `u`,

`u^* G_mu u = int |P_u(t)|^2 dmu(t)`,

where `P_u` has degree at most `q-1`. If `supp(mu)` contains at least `q` distinct points, a nonzero polynomial of degree at most `q-1` cannot vanish on all of them. Hence

`u^* G_mu u>0`

for every nonzero `u`, so `G_mu` is positive definite.

On the compact interval `[-T,T]`, weak convergence of `mu_N` implies convergence of all moments through degree `2q-2`, hence

`(1/N)S^*S -> G_mu`.

Therefore its smallest eigenvalue is eventually bounded below by (for example) `lambda_min(G_mu)/2`.

This gives a simple multicluster corollary. If several centers collide at outer scale `rho` but, after division by `rho`, at least `q` distinct normalized locations retain positive limiting mass, their collision does not create a new small direction. Those locations already interpolate every degree-`q-1` polynomial at the outer scale.

## 5. What remains when the pooled Gram degenerates

The theorem deliberately stops when

`lambda_min((1/N)S^*S)->0`.

That failure is the real compact geometric frontier. It means the outer rescaling has not exposed `q` stably independent polynomial modes. Examples include normalized mass collapsing onto fewer than `q` points, vanishing mass on some normalized centers, or a point cloud whose effective weighting concentrates onto a lower-rank moment configuration.

At that point pairwise center separation still is not the invariant. One must rescale the deficient directions again and price the next hierarchy of inner widths, occupancies, and weights. `VIS-359` describes the opposite regime of fixed separated macroscopic centers with local Hermite jets; the present result describes the first outer fusion step when those centers themselves collapse. Together they reduce a genuine remaining compact loophole to **hierarchical degeneration of successive rescaled sampling Grams**, rather than generic cluster collision.

## Prior-art audit

No novelty is claimed for the linear algebra. The proof is the standard finite-dimensional rescaling of a rectangular Vandermonde/polynomial-sampling matrix followed by positivity of a moment Gram.

Walter Gautschi's classical confluent-Vandermonde work, including **On inverses of Vandermonde and confluent Vandermonde matrices II**, *Numerische Mathematik* 5 (1963), 425–430, and **On inverses of Vandermonde and confluent Vandermonde matrices III**, *Numerische Mathematik* 29 (1978), 445–450, DOI `10.1007/BF01432880`, establishes the classical interpolation/conditioning setting around coalescing nodes.

The closer rectangular clustered-node literature is the same boundary already used in `VIS-358`--`VIS-359`: Dmitry Batenkov, Laurent Demanet, Gil Goldman, and Yosef Yomdin, **Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes**, *SIAM Journal on Matrix Analysis and Applications* 41:1 (2020), 199–220, DOI `10.1137/18M1212197`, and Dmitry Batenkov, Benedikt Diederichs, Gil Goldman, and Yosef Yomdin, **The spectral properties of Vandermonde matrices with clustered nodes**, *Linear Algebra and Its Applications* 609 (2021), 37–72, DOI `10.1016/j.laa.2020.08.034`. Those works make clustered singular-value scales and cluster multiplicity classical territory.

The Mathia-specific delta is only the Wang bookkeeping: once colliding compact centers are pooled at their common outer scale, a nondegenerate normalized moment Gram restores exactly the ordinary one-cluster occupancy-width law. A claimed compact escape must therefore exhibit a further rescaled Gram degeneration rather than cite center collision itself.

## Dependencies

- `VIS-354`: fixed-depth Wang tail coefficients form a truncated inverse-scale Vandermonde map.
- `VIS-357`: loss of every compact square anchor forces shrinking cluster geometry.
- `VIS-358`: one regular dense cluster has quotient scale `sqrt(N) epsilon^(q-1)`.
- `VIS-359`: fixed separated regular clusters add Hermite-jet capacities.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue narrowed by this result.

## Research consequence

A major part of the remaining colliding-center loophole is now closed. **If the entire compact bank, after pooling at its outer shrinking diameter, has a uniformly nondegenerate degree-`q-1` sampling Gram, then its smallest positive Wang singular value is exactly of order `sqrt(N) rho^(q-1)`; splitting the cloud into centers whose separation also tends to zero creates no extra cancellation resource.**

The next compact question is therefore sharper: can a hierarchical, irregular, or weighted cloud make the pooled normalized Gram genuinely degenerate at one scale and continue to lose capacity after the deficient modes are rescaled at finer scales? Anything with a stable pooled Gram is already priced by this finding.