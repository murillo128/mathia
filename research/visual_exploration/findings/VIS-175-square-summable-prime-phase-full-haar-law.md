# VIS-175 — square-summable weighted prime phases have a full growing-cutoff Haar law

## Claim

Fix positive weights `w_p` on the primes with

`0 < Q_infty = sum_p w_p^2 < infinity`.

For `y>=2`, write

`W_y = sum_(p<=y) w_p`,

`Q_y = sum_(p<=y) w_p^2`,

and define the centered weighted prime-phase field

`S_y(t) = Q_y^(-1/2) sum_(p<=y) w_p [sin^2(t log p/2)-1/2]`.

Let `Theta_p` be independent Haar-uniform angles on `[0,2pi)` and let

`S_infty^Haar = Q_infty^(-1/2) sum_p w_p [sin^2(Theta_p/2)-1/2]`.

The Haar series converges in `L^2`. Suppose `H->infinity`, `y=y(H)->infinity`, and

`y W_y^2 / H -> 0`.

Then for every bounded Lipschitz `F : R -> R`, uniformly over arbitrary interval starts `T=T(H)`,

`(1/H) int_T^(T+H) F(S_y(t)) dt -> E[F(S_infty^Haar)]`.

Equivalently, the empirical laws of the deterministic weighted prime-log field on `[T,T+H]` converge weakly, uniformly in the choice of starting heights, to the infinite representation-matched weighted Haar law.

The limiting characteristic function is

`phi_infty(u) = product_p J_0(u w_p/(2 sqrt(Q_infty)))`,

where `J_0` is the Bessel function. The product converges locally uniformly. The limit has

`Var(S_infty^Haar)=1/8`

and fourth cumulant

`kappa_4(S_infty^Haar) = -(3/128) [sum_p w_p^4]/Q_infty^2 < 0`.

Thus the limiting law is non-Gaussian for every nontrivial positive square-summable weight family.

For the prime-power taper

`w_p=p^(-alpha)`, `alpha>1/2`,

one has `Q_infty=P(2alpha)`, and every polylogarithmic cutoff

`y(H)=(log H)^A`, `A>0`,

satisfies the sufficient growth condition. Therefore the deterministic continuous prime-log field converges in full weak law to the corresponding infinite weighted Haar distribution for every `alpha>1/2`, not merely in each preassigned fixed moment. Its fourth cumulant is

`-3 P(4alpha)/(128 P(2alpha)^2)`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL ALMOST-PERIODIC/VALUE-DISTRIBUTION SPECIALIZATION + QUANTITATIVE GROWING-CUTOFF NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This is not a theorem about Gram-point sampling, hybrid prime/zero residuals, shrinking rare-event tests, unbounded observables, nonsquare-summable weight families, optimal cutoff growth, or RH.

## 1. Infinite Haar law exists by square summability

Put

`V(theta)=sin^2(theta/2)-1/2 = -(1/2) cos(theta)`.

For Haar `Theta`,

`E[V(Theta)]=0`, `E[V(Theta)^2]=1/8`.

Hence the independent series

`sum_p w_p V(Theta_p)`

is Cauchy in `L^2` because `sum_p w_p^2<infinity`. After normalization by `sqrt(Q_infty)` it defines `S_infty^Haar` with variance `1/8`.

For one coordinate,

`E exp(i u w V(Theta)/sqrt(Q_infty))`
` = J_0(u w/(2 sqrt(Q_infty)))`.

Since `1-J_0(z)=O(z^2)` locally at the origin and `sum_p w_p^2<infinity`, the infinite product for `phi_infty` converges locally uniformly. Thus the limit law is an ordinary infinite convolution of the one-prime arcsine-type factors.

The fourth cumulant of `V` is

`3/128 - 3(1/8)^2 = -3/128`.

Cumulants add for independent variables, so normalization gives the displayed strictly negative fourth cumulant whenever at least one weight is nonzero. Persistent non-Gaussianity is therefore built into the matched weighted representation; it is not by itself source evidence.

## 2. A uniform finite-window bound kills the high-prime tail

Fix a cutoff `M<y` and write the unnormalized tail

`R_(M,y)(t) = sum_(M<p<=y) w_p V(t log p)`
`             = -(1/2) sum_(M<p<=y) w_p cos(t log p)`.

For distinct primes `p,q<=y`,

`|log p-log q| = log(max(p,q)/min(p,q)) >= log(1+1/y) >= 1/(y+1)`,

while

`log p+log q = log(pq) >= log 6`.

For every nonzero frequency `lambda` and every interval start `T`,

`| (1/H) int_T^(T+H) cos(lambda t) dt | <= 2/(H|lambda|)`.

Using `cos a cos b = [cos(a-b)+cos(a+b)]/2`, the diagonal bound `cos^2<=1`, and `sum_(p<q) w_p w_q <= W_y^2/2`, one obtains uniformly in `T`

`(1/H) int_T^(T+H) |R_(M,y)(t)|^2 dt`
` <= (1/4) sum_(M<p<=y) w_p^2`
`    + [(y+1)+1/log 6] W_y^2/(4H)`.

Under `y W_y^2/H->0`, the second term vanishes. The first can be made arbitrarily small by sending `M->infinity`, because the weights are square summable.

After division by `Q_y`, which tends to the positive number `Q_infty`, the same conclusion holds for the normalized high-prime tail of `S_y`. Cauchy--Schwarz then turns this mean-square estimate into a uniform-in-start bound for every Lipschitz test function.

## 3. The fixed low-prime block already has the Haar law

For fixed `M`, keep only primes `p<=M`. Unique factorization makes the finite frequency vector `(log p)_(p<=M)` rationally independent. `VIS-071` therefore gives Haar equidistribution of the corresponding continuous torus orbit.

The needed version is uniform in the interval start. For each nonzero finite torus character with frequency `lambda`,

`| (1/H) int_T^(T+H) exp(i lambda t) dt | <= 2/(H|lambda|)`,

independently of `T`. Trigonometric-polynomial approximation on the fixed compact torus then gives, for every continuous test of the fixed low-prime block, convergence to its finite Haar expectation uniformly in `T`.

The normalization causes no extra obstruction: for fixed `M`, replacing `Q_y^(-1/2)` by `Q_infty^(-1/2)` changes the low-prime field uniformly by a quantity tending to zero as `y->infinity`.

## 4. Low block plus small tail gives the full weak limit

Let `F` be bounded and Lipschitz. Compare the deterministic average of `F(S_y)` with the Haar expectation in three steps:

1. delete primes `M<p<=y` from the deterministic field;
2. apply fixed-dimensional torus equidistribution to the remaining primes `p<=M`;
3. restore the infinite Haar tail `p>M`.

The first error is bounded by the Lipschitz constant times the deterministic mean absolute tail, hence by the square root of the mean-square estimate in Section 2. The middle error tends to zero for fixed `M`, uniformly in `T`. The final error is bounded by the Haar `L^2` tail,

`[ (1/(8Q_infty)) sum_(p>M) w_p^2 ]^(1/2)`.

Taking `H->infinity` first along the prescribed `y(H)`, and then `M->infinity`, proves the claimed bounded-Lipschitz convergence. Since bounded-Lipschitz convergence metrizes weak convergence on `R`, this is a full distributional transfer, not merely a fixed-moment statement.

## 5. Prime-power tapers satisfy the gate on polylogarithmic support

Take `w_p=p^(-alpha)` with `alpha>1/2`. Then

`Q_infty=sum_p p^(-2alpha)=P(2alpha)<infinity`.

No delicate prime asymptotic is needed for the growth gate. For `1/2<alpha<1`, comparison with all integers gives

`W_y <= sum_(n<=y) n^(-alpha) = O(y^(1-alpha))`,

so

`y W_y^2/H = O(y^(3-2alpha)/H)`.

For `alpha=1`, the crude bound `W_y=O(log y)` gives `y W_y^2/H=O(y(log y)^2/H)`. For `alpha>1`, `W_y=O(1)`, so the ratio is `O(y/H)`.

With `y=(log H)^A`, every one of these bounds tends to zero. Thus the entire square-summable prime-power phase `alpha>1/2` admits the full weak weighted-Haar transfer under any fixed polylogarithmic support exponent.

At `alpha=1`, this strictly strengthens the control in `VIS-174`: not only every preassigned fixed moment but every bounded continuous distributional witness converges to the same persistent low-prime non-Gaussian null.

## 6. Prior art and novelty boundary

The existence and analysis of limiting distributions for almost-periodic functions and zeta-related Dirichlet objects is classical. Børge Jessen and Aurel Wintner, **Distribution Functions and the Riemann Zeta Function**, *Transactions of the American Mathematical Society* 38:1 (1935), 48--88, DOI `10.1090/S0002-9947-1935-1501802-5`, develops infinite-convolution/Fourier-transform methods for distributions arising from sums of independent variables and applies them to almost-periodic functions and the Riemann zeta function.

`VIS-071` already records the classical Kronecker--Weyl/Bohr finite-prime vertical-limit boundary, including the Hedenmalm--Lindqvist--Seip reference. The present finding does not claim a new general value-distribution theorem or almost-periodic convergence theorem.

The Mathia-specific content is a direct elementary control statement for the active weighted visual representation: square-summability plus the explicit sufficient finite-window gate `yW_y^2/H->0` lets the fixed-finite torus law pass to a genuinely growing prime cutoff, with uniformity in the starting height. This closes a specific source-interpretation loophole without claiming optimality.

## 7. Boundaries and falsification

The theorem concerns continuous vertical averaging of the additive field `S_y`. It does not automatically transfer to Gram-point or other discrete sampling, sparse selectors, a hybrid Euler--Hadamard residual, or an observable involving zeta zeros.

The test function is fixed and bounded Lipschitz. Moving thresholds, shrinking targets, rare collision events, decoder singularities, and unbounded moments require stronger control than weak convergence. `VIS-174` separately supplies fixed-moment transfer in explicit regimes; neither result controls all moments uniformly in order.

Square summability is essential to this proof because it makes the discarded Haar and deterministic high-prime tails small in `L^2`. The regime `sum_p w_p^2=infinity`, including prime-power tapers `alpha<=1/2`, is outside the theorem and needs a different normalization and a genuinely growing-dimensional argument.

The growth condition `yW_y^2/H->0` is sufficient and deliberately crude. Better separation of prime-log frequencies, cancellation among cross terms, or stronger almost-periodic discrepancy estimates may permit much faster support growth.

Falsify the finding by finding an error in the prime-log separation bound, the deterministic tail mean-square estimate, the fixed-block uniform equidistribution step, or the infinite-Haar `L^2` passage.

## Research consequence

For square-summable coordinate weights, a persistent limiting distribution of the growing deterministic prime-phase field is no longer a candidate source signal merely because it is non-Gaussian or visibly low-prime dominated. Under the stated support/window gate, the **entire bounded-continuous law** is already the matched weighted Haar law.

The active prime-phase route must therefore leave this representation class: use a statistic whose zeta-facing component is not a bounded continuous functional of the same additive square-summable prime torus, move to a genuinely different sampling regime such as Gram/discrete sampling with its own matched control, enter the nonsquare-summable growing-dimensional boundary, or exhibit a source-sensitive hybrid/zero contribution. A visual residual that remains inside the theorem is a representation effect, not evidence for RH-facing arithmetic structure.
