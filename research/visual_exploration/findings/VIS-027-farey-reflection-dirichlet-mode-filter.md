# VIS-027 — Farey reflection symmetry annihilates odd Dirichlet discrepancy modes but leaves a large symmetry-matched baseline

## Claim

Let

`0 = x_0 < x_1 < ... < x_N = 1`

be an ordered point set with even `N=2M`, gaps `g_i=x_i-x_(i-1)`, centered gap increments

`delta_i = g_i - 1/N`,

and grid discrepancy

`D_k = x_k-k/N = sum_(i=1)^k delta_i`, `1 <= k <= N-1`.

Assume the point set is reflection symmetric,

`x_(N-k)=1-x_k`.

Then the gaps are palindromic, `delta_i=delta_(N+1-i)`, and the discrepancy path is antisymmetric,

`D_(N-k)=-D_k`.

For the orthonormal Dirichlet sine basis

`v_m(k)=sqrt(2/N) sin(pi m k/N)`, `m=1,...,N-1`,

write `d_m=<D,v_m>`. Reflection symmetry forces

`d_m=0` for every odd `m`.

Thus a spectral plot of the Franel `L^2` discrepancy automatically loses every odd Dirichlet mode; that missing half-spectrum is a symmetry artifact, not additional Farey structure.

More precisely, let `B` be the path incidence map `delta=BD` with `D_0=D_N=0`. The Dirichlet path Laplacian `L=B^T B` has eigenvalues

`lambda_m = 4 sin^2(pi m/(2N))`.

Putting `u_m=Bv_m/sqrt(lambda_m)` and `a_m=<delta,u_m>` gives the exact Green/negative-Sobolev decomposition

`E_2 := sum_(k=1)^(N-1) D_k^2`
`     = sum_(m=1)^(N-1) a_m^2/lambda_m`.

Now condition the same-gap permutation control from `VIS-026` on the exact reflection symmetry: uniformly permute the first-half centered gaps `delta_1,...,delta_M` and mirror that order into the second half. If

`sigma_g^2=(1/N) sum_i delta_i^2`,

then this reflection-preserving ensemble has the exact finite-`N` mean

`E_sym[E_2] = sigma_g^2 N(N+2)/12`.

By comparison, the unrestricted same-gap permutation mean from `VIS-026` is

`E_perm[E_2] = sigma_g^2 N(N+1)/6`.

Hence enforcing reflection symmetry reduces the matched permutation baseline only by

`E_sym[E_2]/E_perm[E_2] = (N+2)/(2(N+1))`,

which tends to `1/2`.

**Evidence/status:** `CLASSICAL-DISCRETE-SPECTRAL-GEOMETRY + EXACT-DERIVED SYMMETRY CONTROL + FINITE FAREY SPECIALIZATION`.

No asymptotic Farey estimate, new RH criterion, or new spectral theorem is claimed.

## Exact Dirichlet-mode decomposition

Let `D=(D_1,...,D_(N-1))^T` and let `B` be the `N x (N-1)` first-difference/incidence matrix satisfying

`(BD)_i = D_i-D_(i-1) = delta_i`,

with `D_0=D_N=0`. The matrix

`L=B^T B`

is the standard Dirichlet path Laplacian. Its orthonormal eigenvectors are the sine modes `v_m` above and

`L v_m = lambda_m v_m`,
`lambda_m=4 sin^2(pi m/(2N))`.

The edge vectors

`u_m=Bv_m/sqrt(lambda_m)`

form an orthonormal basis of the zero-sum subspace of `R^N`. Therefore

`a_m=<delta,u_m>`
`   = <BD,Bv_m>/sqrt(lambda_m)`
`   = sqrt(lambda_m) <D,v_m>`
`   = sqrt(lambda_m) d_m`.

Parseval gives the exact identity

`E_2=||D||_2^2=sum_m d_m^2=sum_m a_m^2/lambda_m`.

This is simply the inverse-Dirichlet-Laplacian/Green-function organization of the rank-grid discrepancy. It does not create information beyond the discrepancy path; it separates that information by spatial scale, with low `m` receiving the largest Green weights `1/lambda_m`.

## Reflection is an exact parity filter

Reflection of the point set gives

`g_i=g_(N+1-i)`

and hence the same relation for `delta`. Since `sum_i delta_i=0`,

`D_(N-k)`
` = -sum_(i=N-k+1)^N delta_i`
` = -sum_(i=1)^k delta_(N+1-i)`
` = -D_k`.

Meanwhile

`v_m(N-k)=(-1)^(m+1) v_m(k)`.

Pairing `k` with `N-k` in `<D,v_m>` therefore kills every odd `m` exactly. The lowest Dirichlet mode `m=1`, which is heavily weighted in `E_2`, is absent for purely geometric symmetry reasons.

For even `N`, the Green trace splits exactly as

`sum_(m=1)^(N-1) 1/lambda_m = (N^2-1)/6`,

`sum_(m odd) 1/lambda_m = N^2/8`,

`sum_(m even) 1/lambda_m = (N^2-4)/24`.

Thus the odd modes account for asymptotically three quarters of the unrestricted Green trace. It would nevertheless be wrong to conclude that reflection symmetry should divide the same-gap permutation mean by four, because conditioning on symmetry changes the variance carried by each surviving mode.

## Exact reflection-preserving permutation baseline

Write the first half of the palindromic centered gaps as

`y=(delta_1,...,delta_M)`.

Because the full vector is palindromic and sums to zero,

`sum_(i=1)^M y_i=0`,

and its half-vector variance is still `sigma_g^2`.

Choose a uniform random permutation `pi` of these `M` entries and form the full reflected vector

`delta^(pi)=(y_(pi(1)),...,y_(pi(M)),y_(pi(M)),...,y_(pi(1)))`.

Odd Dirichlet modes remain identically zero. For an even mode `m=2r`, the edge singular vector `u_(2r)` is palindromic. Its first half has squared norm `1/2` and zero sum. Therefore

`a_(2r)=2 sum_(i=1)^M y_(pi(i)) u_(2r)(i)`.

Uniform sampling without replacement on the zero-sum half-vector gives covariance

`Cov(y_(pi)) = [M sigma_g^2/(M-1)] (I-11^T/M)`.

Consequently every surviving normalized edge mode has the same exact variance

`E_sym[a_(2r)^2] = 2M sigma_g^2/(M-1)`.

Using

`sum_(r=1)^(M-1) 1/lambda_(2r) = (M^2-1)/6`,

we obtain

`E_sym[E_2]`
` = [2M sigma_g^2/(M-1)] [(M^2-1)/6]`
` = M(M+1) sigma_g^2/3`
` = sigma_g^2 N(N+2)/12`.

This is a stronger matched control than `VIS-026`: it holds both the complete gap multiset and the exact left-right reflection symmetry fixed while randomizing the remaining ordering information.

## Farey specialization

For the Farey sequence `F_n`, the involution `a/b -> (b-a)/b` shows that the ordered fractions satisfy

`x_(N-k)=1-x_k`.

For `n>=2`, `N=sum_(q=1)^n phi(q)` is even, since the first two totients sum to two and `phi(q)` is even for `q>2`. The reflection-parity filter and the symmetry-preserving permutation baseline therefore apply exactly.

At `n=100`, `N=3044`. Direct finite evaluation gives

`E_2(F_100) = 0.00511378780133444`,

while

`E_perm[E_2] = 0.2176486473943855`,

as already recorded in `VIS-026`, and the stronger symmetry-preserving baseline is

`E_sym[E_2] = 0.1088600623913462`.

Thus

`E_2(F_100)/E_perm[E_2] = 0.0234956102992366`,

but even after preserving the exact reflection symmetry,

`E_2(F_100)/E_sym[E_2] = 0.0469757934085197`.

For the same finite orders used in `VIS-026`,

`n = 20, 30, 40, 60, 80, 100, 120, 150, 200, 250, 300`,

the symmetry-matched ratios are respectively

`0.301610, 0.186932, 0.129315, 0.085635, 0.064376, 0.046976, 0.039306, 0.030635, 0.024323, 0.017031, 0.014028`.

These are finite diagnostics only. Their decrease is not fitted to an exponent and does not establish an asymptotic law.

## Visual and representation consequence

A raw sine-spectrum picture of Farey discrepancy has an immediately attractive checkerboard feature: every odd mode is absent. This finding classifies that feature completely as reflection symmetry.

A more responsible multiscale visualization must therefore compare only the surviving even-mode energy against a reflection-preserving same-gap control, or against a still stronger control that also preserves admitted local/denominator structure. Plotting the zero odd modes as though they were arithmetic cancellation would double-count a symmetry already forced before any number-theoretic mechanism enters.

The exact mode decomposition remains useful because it localizes where the **residual** suppression lives. It does not by itself strengthen the Franel scalar criterion: summing all modal contributions reconstructs exactly the same `E_2`.

## Prior art and novelty assessment

Franel's 1924 Farey result is the classical source for the `L^2` discrepancy criterion related to RH: J. Franel, **Les suites de Farey et le problème des nombres premiers**, *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse* (1924), 198–201.

The spectral ingredients are standard discrete linear algebra. Fan Chung and Ji Zeng, **Forest formulas of discrete Green's functions**, *Journal of Graph Theory* 102 (2023), 556–577, DOI `10.1002/jgt.22887`, provide modern general prior art for discrete Green functions as inverses/pseudoinverses of graph Laplacians and for reciprocal-eigenvalue trace formulas. The path-Dirichlet sine diagonalization used here is elementary.

The nearest Farey ordering prior art remains Rogelio Tomás García, **A General Lower Bound for Average Local Discrepancy and an Application to the Farey Sequence**, *Mathematics* 14:14 (2026), 2543, DOI `10.3390/math14142543`, together with the finite-population summation-process literature already recorded for `VIS-026`. García explicitly treats fixed-gap permutations and emphasizes the effect of Farey gap ordering; the present result adds an exact reflection-conditioned `L^2` control and a Dirichlet-mode interpretation.

No claim is made that the spectral identity, parity decomposition, or conditioned finite-population calculation is new in general probability/discrete spectral theory. A structure-based search found the ingredients as standard and did not locate this exact Farey symmetry-conditioned baseline in the nearest Farey treatment. The durable Mathia contribution is the **control boundary**: the most obvious missing-mode visual pattern is forced by reflection, while the measured Farey suppression remains much stronger even after conditioning the same-gap null on that symmetry.

## Boundary conditions and falsification

The reflection-preserving ensemble fixes only the gap multiset and exact left-right symmetry. It does not preserve adjacent gap-pair counts, bounded-depth blocks, denominator strata, mediant ancestry, or any other arithmetic relation. A residual difference from this null therefore localizes information beyond those two controls but does not identify the mechanism.

The Dirichlet-mode decomposition is an invertible orthogonal re-expression of the discrepancy path. It cannot by itself produce a stronger RH criterion. Any claim of additional information must come from a structured relation among modes, a restricted family of modes with an independently justified bound, or a control-preserving statistic not determined by the aggregate `E_2`.

The finite Farey ratios do not establish monotonicity or an asymptotic exponent. They are retained only to show that exact reflection symmetry is quantitatively insufficient to explain the previously observed suppression at the tested orders.

## Research consequence

The proposed Farey handoff

`research/farey_discrepancy/clues/CLUE-farey-gap-order-bridge-suppression.md`

should use the reflection-preserving same-gap ensemble as the next mandatory null before attributing low-frequency suppression to multiscale arithmetic ordering. The simplest parity effect is now closed: odd Dirichlet modes vanish identically from Farey reflection symmetry.

The live question is narrower and more useful: after fixing the gap multiset **and** reflection symmetry, which even-mode or cross-scale couplings account for the remaining suppression, and do they survive controls that progressively preserve local adjacency and denominator/mediant structure without collapsing back to the classical Franel–Landau/Möbius scalar channel?
