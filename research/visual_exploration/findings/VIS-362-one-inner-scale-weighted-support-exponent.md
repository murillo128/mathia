# VIS-362 — one weighted inner scale has a sharp support-count exponent

## Claim

Fix a finite Wang asymptotic depth `q>=2`, an invertible diagonal tail matrix

`D_beta=diag(beta_1,...,beta_q)`,

a compact positive center range `0<r<=c<=R`, and fixed bounds for the normalized coordinates below.

Let `1<=L<q` and choose distinct outer normalized centers

`z_1,...,z_L`

in a fixed compact interval, with pairwise separation bounded below by a positive constant. For cluster `ell`, choose bounded inner nodes `u_(ell,j)`, positive weights `w_(ell,j)>0`, cluster mass

`M_ell=sum_j w_(ell,j)`,

and total mass `M=sum_ell M_ell`. Assume every cluster keeps a positive mass fraction,

`M_ell/M >= alpha > 0`.

At inner scale `epsilon`, put

`t_(ell,j)=z_ell+epsilon u_(ell,j)`,
`x_(ell,j)=c+rho t_(ell,j)`.

Let `U_ell` be the local polynomial-sampling matrix with columns `1,u,...,u^(q-1)` and let `W_ell=diag(w_(ell,j))`. Assume every local normalized weighted moment Gram is uniformly nondegenerate:

`lambda_min(M_ell^(-1) U_ell^* W_ell U_ell) >= gamma > 0`.

Let `V` be the `q x N` matrix whose column at `x` is `(x,x^2,...,x^q)^T`, let `W` be the diagonal matrix of all weights, and set

`A_w=D_beta V W^(1/2)`.

Define

`h=floor((q-1)/L)`.

Then, for sufficiently small `epsilon` and `rho` while all nodes remain in the fixed positive compact range, there are constants `C_1,C_2>0`, depending only on the fixed data above, such that

`C_1 sqrt(M) rho^(q-1) epsilon^h <= s_q(A_w) <= C_2 sqrt(M) rho^(q-1) epsilon^h`.

Equivalently, if `S_epsilon` is the global degree-`q-1` sampling matrix in the outer normalized coordinate `t`, then its normalized weighted moment Gram satisfies

`lambda_min(M^(-1) S_epsilon^* W S_epsilon) asymp epsilon^(2h)`.

Thus a first hierarchical weighted-Gram collapse has a completely explicit fixed-depth price. If the outer weighted measure collapses onto exactly `L<q` separated atoms but every atom retains positive mass and resolves a healthy inner polynomial cloud at one common finer scale, the lost polynomial modes reappear with exponent

`h=floor((q-1)/L)`.

A one-level positive weighted hierarchy is therefore **not** an unpriced compact Wang cancellation resource. To obtain further compact degeneration, the hierarchy itself must continue: some cluster mass fraction must vanish, a local weighted Gram must also degenerate, another finer scale must be introduced in the deficient modes, or the coefficient geometry must leave the positive diagonal Hilbert setting.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL HERMITE/CONFLUENT-VANDERMONDE MULTISCALE GEOMETRY + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This result is source-free. It proves no new estimate for `theta`, the normalized remainder `G`, the zeta zero set, or RH.

## 1. The outer Gram loses rank because only `L` value modes survive

Work first entirely in the normalized `t` coordinate. For a polynomial

`P(t)=sum_(d=0)^(q-1) a_d t^d`,

its normalized weighted sampling energy is

`E_epsilon(P)=M^(-1) sum_(ell,j) w_(ell,j) |P(z_ell+epsilon u_(ell,j))|^2`.

When `epsilon=0`, this sees only the `L` values `P(z_ell)`, so its Gram has rank at most `L<q`. The question is the exact rate at which the missing modes return for `epsilon>0`.

For cluster `ell`, Taylor expansion gives

`P(z_ell+epsilon u)=sum_(d=0)^(q-1) epsilon^d P^(d)(z_ell) u^d/d!`.

By the local weighted Gram hypothesis,

`M_ell^(-1) sum_j w_(ell,j) |P(z_ell+epsilon u_(ell,j))|^2`
` >= gamma sum_(d=0)^(q-1) epsilon^(2d) |P^(d)(z_ell)/d!|^2`.

The positive mass-fraction hypothesis then gives

`E_epsilon(P) >= alpha gamma sum_ell sum_(d=0)^(q-1) epsilon^(2d) |P^(d)(z_ell)/d!|^2`.

So the hierarchy is already expressed as a weighted Hermite-jet budget: value data cost order one, first derivatives cost `epsilon`, second derivatives cost `epsilon^2`, and so on.

## 2. Hermite interpolation gives the lower exponent

Write

`q=L h+s`, `1<=s<=L`,

which is equivalent to `h=floor((q-1)/L)`.

Choose Hermite multiplicities

`m_ell=h+1` for `s` centers,
`m_ell=h` for the other `L-s` centers.

Then

`sum_ell m_ell=q`

and every selected derivative order satisfies `0<=d<m_ell<=h+1`, hence `d<=h`. For `0<epsilon<=1`,

`epsilon^(2d) >= epsilon^(2h)`.

Therefore

`E_epsilon(P)`
` >= C epsilon^(2h) sum_ell sum_(d=0)^(m_ell-1) |P^(d)(z_ell)|^2`.

The selected `q` value/derivative functionals form an ordinary Hermite interpolation map on the distinct fixed centers `z_ell`. Its confluent Vandermonde matrix is invertible. Since the centers remain in a fixed separated compact configuration, this map has a fixed inverse bound, so

`sum_ell sum_(d<m_ell) |P^(d)(z_ell)|^2 >= C' ||a||_2^2`.

Consequently

`E_epsilon(P) >= C'' epsilon^(2h) ||a||_2^2`,

which proves

`lambda_min(M^(-1) S_epsilon^* W S_epsilon) >= C'' epsilon^(2h)`.

The exponent is controlled only by how many distinct outer support points remain visible. `L` outer value modes are free; the remaining `q-L` conditions must be purchased as inner Hermite jets, and balancing those jets across `L` centers makes the deepest required order exactly `h`.

## 3. A balanced vanishing polynomial makes the exponent sharp

Since

`q-1=L h+(s-1)`,

choose integers `r_ell` by taking

`r_ell=h+1` at `s-1` centers,
`r_ell=h` at the remaining `L-s+1` centers.

Then

`sum_ell r_ell=q-1`

and every `r_ell>=h`. Define the fixed degree-`q-1` polynomial

`P_0(t)=prod_(ell=1)^L (t-z_ell)^(r_ell)`.

On cluster `ell`, boundedness of the inner coordinates and separation of the other outer centers give

`|P_0(z_ell+epsilon u)| <= C epsilon^(r_ell) <= C epsilon^h`.

After normalizing the coefficient vector of `P_0`,

`E_epsilon(P_0) <= C epsilon^(2h)`.

Hence

`lambda_min(M^(-1) S_epsilon^* W S_epsilon) <= C epsilon^(2h)`.

Together with the lower bound this proves the sharp Gram law

`lambda_min(M^(-1) S_epsilon^* W S_epsilon) asymp epsilon^(2h)`.

The witness is important conceptually: the small direction is not produced by mysterious cancellation among weights. It is simply the degree-`q-1` polynomial that vanishes as evenly as possible across the `L` surviving outer atoms.

## 4. Transfer back to the Wang bank

For `y in C^q`, write as in `VIS-360`--`VIS-361`

`p_y(x)=sum_(k=1)^q conjugate(y_k) beta_k x^k=x Q_y(x)`,

with `deg Q_y<=q-1`. In the outer coordinate `x=c+rho t`, write

`Q_y(c+rho t)=sum_(d=0)^(q-1) b_d t^d`.

Uniform finite-dimensional translation and invertibility of `D_beta` imply

`||b||_2 >= c_0 rho^(q-1) ||y||_2`.

Since `x` stays uniformly away from zero, the weighted Gram law above gives

`||A_w^* y||_2^2`
` >= C M epsilon^(2h) ||b||_2^2`
` >= C' M rho^(2(q-1)) epsilon^(2h) ||y||_2^2`.

Thus

`s_q(A_w) >= C_1 sqrt(M) rho^(q-1) epsilon^h`.

For the matching upper bound, use the degree-`q-1` polynomial in the original variable

`Q_(rho)(x)=prod_ell (x-c-rho z_ell)^(r_ell)`.

Its coefficient vector stays uniformly bounded above and below as `rho->0` because it is monic of fixed degree with roots in a fixed compact set. On cluster `ell`,

`Q_(rho)(c+rho(z_ell+epsilon u))`
` = rho^(q-1) P_0(z_ell+epsilon u)`
` = O(rho^(q-1) epsilon^(r_ell))`.

After normalizing the corresponding Wang row direction,

`||A_w^* y_0||_2^2 <= C M rho^(2(q-1)) epsilon^(2h)`.

This proves the claimed two-sided Wang scale.

## 5. What this closes and what it does not

`VIS-361` stopped precisely when the normalized positive weighted outer Gram became singular. The present result prices the simplest genuine continuation: the outer measure loses rank because it collapses to `L<q` separated atoms, but each atom carries a positive fraction of the mass and, after one common finer rescaling, its local weighted sampling geometry is healthy.

In that regime there is no indefinite new cancellation reservoir. One inner rescaling restores the missing polynomial modes at the explicit exponent `h=floor((q-1)/L)`, and the full Wang quotient pays exactly the additional factor `epsilon^h`.

The unresolved compact frontier is therefore narrower. A further escape requires at least one of:

- vanishing outer mass fractions, so some nominal support points disappear from the weighted geometry;
- local normalized weighted Grams that themselves lose rank or conditioning;
- more than one nested inner scale in the deficient modes;
- changing asymptotic depth `q` or a noncompact scale range;
- a non-diagonal or indefinite coefficient topology;
- source-dependent signed information whose gain must be established at the arithmetic source rather than inferred from source-free conditioning.

This finding does **not** classify an arbitrary recursive cluster tree. It handles exactly one positive weighted inner scale after an `L`-atom outer collapse.

## Prior-art audit

No novelty is claimed for the underlying interpolation or clustered-Vandermonde geometry. Hermite interpolation and confluent Vandermonde matrices classically identify derivative jets as the correct coordinates when nodes coalesce. Hao Lu, **Fast Solution of Confluent Vandermonde Linear Systems**, *SIAM Journal on Matrix Analysis and Applications* 15:4 (1994), 1277–1289, DOI `10.1137/S089547989324416X`, is a standard reference for this setting.

The modern clustered-Vandermonde literature already shows that singular scales are controlled by local cluster multiplicity rather than by raw global node count. Dmitry Batenkov, Laurent Demanet, Gil Goldman, and Yosef Yomdin, **Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes**, *SIAM Journal on Matrix Analysis and Applications* 41:1 (2020), 199–220, DOI `10.1137/18M1212197`, gives sharp cluster-controlled smallest-singular-value bounds; Dmitry Batenkov, Benedikt Diederichs, Gil Goldman, and Yosef Yomdin, **The spectral properties of Vandermonde matrices with clustered nodes**, *Linear Algebra and Its Applications* 609 (2021), 37–72, DOI `10.1016/j.laa.2020.08.034`, develops the corresponding multicluster spectral decomposition.

The Mathia-specific delta is only the fixed-depth Wang bookkeeping. In the positive weighted two-scale model above, the first degenerate outer moment Gram has the sharp exponent `floor((q-1)/L)`, so a one-level hierarchy is completely priced before any arithmetic source information is credited.

## Dependencies

- `VIS-354`: the fixed-depth Wang tail coefficient map is a truncated inverse-scale Vandermonde map.
- `VIS-359`: separated regular clusters add Hermite-jet capacities.
- `VIS-360`: a nondegenerate pooled outer Gram has the ordinary `sqrt(N) rho^(q-1)` scale.
- `VIS-361`: positive diagonal weights reduce the compact problem to a normalized weighted moment Gram.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue narrowed by this result.

## Research consequence

The first genuinely hierarchical positive-weight loophole is now priced. **If a degenerate outer weighted cloud collapses onto `L<q` separated support points, each with nonvanishing mass, and one finer rescaling exposes a uniformly healthy local weighted polynomial cloud, then the smallest Wang singular value is exactly of order `sqrt(M) rho^(q-1) epsilon^floor((q-1)/L)`.**

So an outer Gram eigenvalue going to zero is not by itself evidence of a new compact cancellation mechanism. The degeneration must survive the first inner Hermite rescaling — through vanishing masses, another local Gram collapse, or a deeper nested scale — before the compact Wang branch contains any still-unpriced positive weighted geometry.