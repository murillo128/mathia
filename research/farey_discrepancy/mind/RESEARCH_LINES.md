# Farey-discrepancy research lines

This file records the current mathematical questions that survive the Farey-discrepancy evidence. It is not a roadmap, task queue, status page, or history.

## Force block-Mertens magnitude past the positive-capacity boundary, or rule out the required low-frequency source carrier

FD-255--FD-265 separate the signed exact-omission threshold from the physical nonnegative-source boundary. The positive switched-response cone has a genuine capacity loss, while canonical full-grid inversion supplies only `O(D log D)` repair mass after explicit forcing terms are removed. Dense deep blocks or a negative signed mean therefore do not by themselves produce the one-sided amplification required by the physical destination.

FD-298 reduces the low-height zero-safe hard-complement problem, below the aggregate rigidity floor, to the physical block-Mertens field

`G_N(d)=sum_(q|d) [M(Nq)-M(N(q-1))]`.

Writing `L_N(x)=sum_(x<d<=2x)|G_N(d)|`, the near-capacity budget is `N^(1/2)x^(1+c)/ell(x)`, with `c=1-log_2(3/2)` and subpolynomial `ell`. FD-299 removes sign polarization under RH, and FD-300 shows that near-capacity `L_N(x)` forces a dyadic denominator shell whose block-Mertens increments have RMS `N^(1/2)x^(c-o(1))`. Because each length-`N` block has absolute sum at most `N`, the same energy reduction already gives the unconditional source ceiling

`lambda <= lambda_src := 1/(2c) = 1.2047104198...`

when `x=N^(lambda+o(1))`.

FD-303 thickens sufficiently large aligned shell energy into a complete sliding second moment. FD-304 uses RH to force every carrying shell past `Q>=x^(2c-o(1))`, to populate it by power-many large blocks, and above `lambda>3/(10c)=0.7228262519...` to transfer the anomaly to many fixed-window positive Möbius correlations on one common interval. FD-305 compresses that family into an exact additive-spectral certificate for the fixed Möbius block `F_X(alpha)`, and FD-306 shows that sufficiently large coefficients in deeper parameter ranges must lie on rational major arcs.

FD-307 recovers source localization that the unrestricted fourth-moment compression had discarded. The common-window sliding moment is a Fejer-weighted spectrum,

`int |F_X(alpha)|^2 |D_N(alpha)|^2 d alpha`,

so near-capacity mass forces a source-selected low-frequency coefficient satisfying

`||alpha_*|| <= N^(-1/4-(3c/2)lambda+o(1))`

and

`|F_X(alpha_*)| >= X^(1/2) N^((9c/4)lambda-5/8-o(1))`.

FD-307 also derived shell-dependent thresholds at which current minor-arc control would force that witness onto the principal `q=1` major arc and then contradict it there. FD-308 performs the required dominance audit and changes the frontier: after the RH shell floor `rho>=2c` is imposed, both the major-arc localization threshold and the principal-arc kill threshold lie **strictly above** the earlier unconditional source ceiling `lambda_src`. Those later implications remain correct, but their antecedent is already impossible by FD-300. The apparent FD-307 shell squeeze is likewise nonbinding throughout the source-live range.

FD-309 stress-tests the remaining low-frequency witness against the classical GRH additive Möbius bounds. Under GRH for Dirichlet `L`-functions, both the uniform Baker--Harman `X^(3/4+epsilon)` estimate and its sharper principal-arc form

`|F_X(alpha)| << X^(1/2+epsilon) (1+X||alpha||)^(1/2)`

become contradictory only at thresholds that are **tangent to or above** the same source ceiling. With shell depth `rho>=2c`, the principal-frequency threshold is `lambda>1/(3c-rho/2)` and the uniform threshold is `lambda>7/[2(9c-rho)]`; both attain their minimum exactly at `rho=2c`, where that minimum equals `1/(2c)=lambda_src`. Because a power contradiction requires a strict inequality, GRH removes none of the live interval. This closes the generic classical pointwise additive-bound repair: even the frequency-sensitive principal-arc theorem is exactly too weak at the source boundary.

FD-310 turns “improve the principal-frequency bound” into a quantitative theorem-design threshold. If one had, on the same fixed block and throughout the FD-307 principal neighborhood,

`|F_X(alpha)| <= X^(1/2+o(1)) (1+X||alpha||)^theta`,

then survival of the near-capacity witness forces `lambda<=Lambda_theta(rho)=(5+6theta)/(18c+12c theta-8theta rho)`. The shell-uniform contradiction threshold enters below the source ceiling exactly when `theta<c=0.4150374992...`. At balanced depth `lambda=1`, killing every allowed shell is substantially harder: it requires `theta<theta_bal=0.2739244180...`; `theta=0.3` only pushes the carrier to `rho>=0.902004...`. Equality is only tangency because the unresolved `o(1)` terms do not yield a power contradiction.

FD-311 exposes an independent physical-space route before the Fejer/Fourier compression. The same FD-303 reduction forces the sliding second moment

`J_mu(X,N)=sum_(X<=y<2X) |M(y+N)-M(y)|^2`

to satisfy `J_mu(X,N)>=X N^(1/2+3c lambda-o(1))`. Therefore a uniform source-window estimate `J_mu(X,N)<=X N^(2-eta+o(1))` rules out near-capacity whenever `eta>3/2-3c lambda`. At balanced depth this asks only for a fixed power saving `eta>0.2548875...`, equivalently `J_mu(X,N)<<X N^(1.7451125-epsilon)`. Under RH the required intervals lie in the concrete band `N=X^(beta+o(1))` with `1/2<=beta<=0.5464257...`. This is a different theorem class from the FD-310 pointwise-frequency barrier: an `L^2` saving across the source-selected dyadic start interval can close the balanced route without controlling every short interval or every principal frequency.

The live block-Mertens question therefore has two quantitatively distinct exits. One can prove a principal-frequency estimate whose effective phase-growth exponent crosses the FD-310 barrier (`theta<c` source-uniformly, and `theta<0.273924...` to close balanced depth on every allowed shell), or prove the FD-311 source-window variance saving (`eta>0.2548875...` at balanced depth). The second route is weaker than pointwise square-root cancellation but must hold on the exact source-selected window; log-power savings or almost-all bounds with an uncontrolled exceptional contribution do not cross its fixed-power threshold. A third possibility is to strengthen the source reduction or exploit shell structure not visible in either generic template. Once the Farey divisor-replication geometry has been discharged and only fixed-block Möbius cancellation remains, ownership naturally overlaps `mobius_cancellation` unless new Farey structure constrains the witness.

## Force physical occupation of the complete zero-packet regime

FD-282--FD-292 show that the grouped strict-right Perron collar retains a prime witness unless a high-order near-one `zeta'/zeta` phase event occurs, and that such phase-bad sets have arbitrarily strong fixed inverse-logarithmic measure savings on polynomial windows. The remaining occupation theorem is therefore a statement about the **complete physical hard remainder**, not about rebuilding phase synchronization gap by gap.

FD-293 shows that reciprocal-log-safe occupation of positive measure already requires `H^(1-o(1))` remainder-good gaps under RH. FD-294 converts such occupation into near-linear many short complete zero-packet cancellations, and FD-295 shows that below square-root height those complete packets are automatically capacity-subcritical. FD-296--FD-297 identify a lower-height rigidity regime in which the whole zero-safe trajectory is controlled, up to `o(B)`, by one fixed low-height complete hard remainder rather than by return frequency.

Inside that rigidity regime FD-298--FD-311 expose the fixed baseline as the block-Mertens source field and then, under a near-capacity premise, as an inflated sliding variance together with low-frequency spectral carriers and explicit theorem-design thresholds in both physical and Fourier space. Outside it, but still in the short-complete-packet range, the unresolved theorem remains near-linear safe occupation or a stronger source-side path-control statement. The current Montgomery--Vaughan phase selector is intrinsically aggregate at zero-gap scale and cannot simply be rerun independently on each RH zero gap.
