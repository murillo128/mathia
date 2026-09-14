# VIS-217 — normalized magnetic spectral certificates have a vertex-dimension floor

## Claim

Keep the finite Hermitian zero-diagonal weighted support-graph setup of `VIS-213`--`VIS-216`. On each nontrivial connected support component `K`, let

`A_K` be the Hermitian coefficient matrix,

`D_K=diag(d_u)` with `d_u=sum_v |A_(u,v)|`,

`M_K=D_K^(-1/2) A_K D_K^(-1/2)`,

and let `B_K=sum_(u in K)d_u`. Write `n_K=|K|>=2` and denote the extreme eigenvalues of `M_K` by

`a_K=lambda_max(M_K)>0`,

`-b_K=lambda_min(M_K)<0`, with `b_K>0`.

Then the normalized magnetic certificate of `VIS-216` is exactly

`U_spec = B(A)-min(S_+,S_-)`
`       = max(sum_K B_K a_K, sum_K B_K b_K)`.

For one connected component this reduces to

`U_spec = B(A) ||M||_op`.

Moreover every connected component obeys the phase-independent dimension floor

`a_K+b_K >= 2/sqrt(n_K-1)`

and therefore

`U_spec >= sum_K B_K/sqrt(n_K-1)`.

In particular, for a connected support graph on `n` vertices,

`||M||_op >= 1/sqrt(n-1)`

and hence

`U_spec >= B(A)/sqrt(n-1)`.

Let, as in `VIS-216`,

`R(A)=2 sum_e w_e^2`,

`N_eff=(sum_e w_e)^2 / sum_e w_e^2`,

with `B(A)=2 sum_e w_e`. Then for a connected component

`U_spec/sqrt(R(A)) >= sqrt(2 N_eff/(n-1))`.

Consequently the normalized magnetic-Laplacian relaxation **cannot by itself certify Haar-RMS-scale worst-start suppression when `N_eff/n -> infinity`**, regardless of the edge phases or cycle holonomies. A necessary condition for this spectral relaxation to prove `U_spec=O(sqrt(R(A)))` is `N_eff=O(n)`.

This is a limitation of the relaxation, not of the exact unit-modulus torus problem. Fractional cycle packing or the exact torus minimum may still be much stronger.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL LINEAR-ALGEBRA/NORMALIZED-ADJACENCY SPECIALIZATION + NEGATIVE RELAXATION BOUND + NO-NOVELTY-CLAIM`.

No new magnetic-Laplacian theorem, graph spectral theorem, prime asymptotic, or RH consequence is claimed.

## 1. The `VIS-216` ground-state certificate is an operator-norm relaxation

On one connected component,

`calL_+ = I-M`,

`calL_- = I+M`.

Therefore

`lambda_+ = 1-lambda_max(M)=1-a`,

`lambda_- = 1+lambda_min(M)=1-b`.

For several components, `VIS-216` defines

`S_+ = sum_K B_K lambda_+(K)`
`    = B(A)-sum_K B_K a_K`,

and

`S_- = sum_K B_K lambda_-(K)`
`    = B(A)-sum_K B_K b_K`.

Hence

`B(A)-min(S_+,S_-)`
` = max(sum_K B_K a_K, sum_K B_K b_K)`.

For a connected graph this is simply

`B(A) max(a,b)=B(A)||M||_op`.

Thus the normalized magnetic ground-state route in `VIS-216` is exactly the ordinary normalized-adjacency operator-norm relaxation of the unit-modulus quadratic optimization. The magnetic language remains useful for interpreting balance and frustration, but it does not create a stronger spectral upper bound than this operator norm.

## 2. Phase removal fixes a minimum Frobenius mass

Fix a connected component with `n>=2` vertices. Let `W=|A|` entrywise and define the unsigned normalized adjacency

`N=D^(-1/2) W D^(-1/2)`.

`M` and `N` have identical entry magnitudes, so

`||M||_F=||N||_F`.

The unsigned matrix `N` has eigenvalue `1` with eigenvector `D^(1/2) 1`. Because the diagonal is zero, `tr(N)=0`. If its remaining eigenvalues are `nu_2,...,nu_n`, then

`sum_(j=2)^n nu_j=-1`.

Cauchy--Schwarz gives

`sum_(j=2)^n nu_j^2 >= 1/(n-1)`.

Therefore

`||M||_F^2=||N||_F^2 >= 1+1/(n-1)=n/(n-1)`.

This lower bound is independent of all magnetic phases. Phases may redistribute the spectrum, but they cannot reduce the total squared spectral mass below the unsigned normalized-adjacency floor fixed by the support weights and degree normalization.

## 3. Tracelessness forces both spectral sides to span that mass

The magnetic matrix `M` is Hermitian and has zero diagonal, hence `tr(M)=0`. Its spectrum lies in `[-b,a]` with mean zero.

For every eigenvalue `x` in this interval,

`(a-x)(x+b)>=0`,

so

`x^2 <= (a-b)x + ab`.

Summing over all eigenvalues and using `sum x=0` yields

`||M||_F^2 <= n a b`.

Combining with the previous section gives

`ab >= 1/(n-1)`.

Therefore

`a+b >= 2 sqrt(ab) >= 2/sqrt(n-1)`.

In particular

`||M||_op=max(a,b) >= 1/sqrt(n-1)`.

For multiple connected components, put

`A_spec=sum_K B_K a_K`,

`B_spec=sum_K B_K b_K`.

Since `U_spec=max(A_spec,B_spec)`,

`U_spec >= (A_spec+B_spec)/2`
`       = (1/2) sum_K B_K(a_K+b_K)`
`       >= sum_K B_K/sqrt(n_K-1)`.

This is the advertised componentwise dimension floor.

## 4. Effective-edge density decides whether the spectral route can reach RMS scale

For one connected component write

`W_1=sum_e w_e`,

`W_2=sum_e w_e^2`.

Then

`B(A)=2W_1`,

`R(A)=2W_2`,

`N_eff=W_1^2/W_2`.

The dimension floor gives

`U_spec/sqrt(R(A))`
` >= [2W_1/sqrt(n-1)] / sqrt(2W_2)`
` = sqrt(2 N_eff/(n-1))`.

So the near-one ground-state requirement isolated in `VIS-216` has an equivalent structural obstruction:

`||M||_op=O(N_eff^(-1/2))`

can hold only if

`N_eff=O(n)`.

If the weight mass is spread over an effectively superlinear number of edges, `N_eff/n -> infinity`, the spectral upper bound is necessarily asymptotically larger than the Haar RMS scale by at least `sqrt(N_eff/n)` up to constants. No phase arrangement can repair this because the obstruction comes from the phase-blind Frobenius mass of normalized adjacency.

Conversely, `N_eff=O(n)` is only a necessary condition. It does not imply that `||M||_op` is small enough, nor that the exact torus optimum is RMS-scale.

## 5. Prior-art and novelty boundary

The ingredients are classical. The normalized-Laplacian identity `calL=I-M`, the relation between its ground state and extreme normalized-adjacency eigenvalues, the Frobenius/operator norm inequality, and the trace/Cauchy--Schwarz argument are elementary spectral graph theory and linear algebra. `VIS-216` already anchors the magnetic/connection-Laplacian framework to Bandeira--Singer--Spielman and Lange--Liu--Peyerimhoff--Post.

The present result makes no claim that the dimension floor is a new graph theorem. Its value inside this research line is diagnostic: it combines the exact `VIS-216` coefficient-mass normalization with the Haar variance scale to show that dense effective support creates a phase-independent obstruction to this particular relaxation reaching the desired scale.

## 6. Prime-phase consequence and next discriminating question

For the prime-weighted matrix `A_(y,H)` from `VIS-213`, the spectral branch now has a sharp preliminary gate before any detailed magnetic-gap analysis:

- determine the number `n(y,H)` of nonisolated prime-phase vertices in the relevant connected component(s);
- determine or bound the effective edge count `N_eff(y,H)`;
- compare `N_eff(y,H)` with `n(y,H)`.

If `N_eff/n -> infinity` in the target regime, `VIS-217` closes normalized magnetic ground-state bounds as a standalone route to Haar-RMS-scale pointwise suppression. The useful remaining static possibilities would then be a substantially stronger cycle-packing certificate or a genuinely tighter use of the fixed-modulus torus constraint.

If instead `N_eff=O(n)`, the dimension floor does not kill the spectral route, but one still has to prove the much stronger quantitative estimate on the actual extreme eigenvalues identified by `VIS-216`.

This finding does not establish the asymptotic behavior of `N_eff(y,H)/n(y,H)`. That arithmetic estimate is the next separate question and should not be assumed from visual graph density alone.