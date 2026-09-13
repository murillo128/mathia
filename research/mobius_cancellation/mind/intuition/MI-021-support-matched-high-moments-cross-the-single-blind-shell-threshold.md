# MI-021 — Endpoint-optimal detection reduces the blind-shell problem to one flat sparse quadratic second moment

**Evidence level:** exact for the support threshold and basis reductions through [MC-264](../../findings/MC-264-support-matched-high-moment-blind-threshold.md), [MC-265](../../findings/MC-265-even-support-central-krawtchouk-balance-obstruction.md), [MC-266](../../findings/MC-266-tensor-pair-krawtchouk-radial-source-walk-collapse.md), [MC-267](../../findings/MC-267-krawtchouk-source-hierarchy-amplitude-duality.md), for the endpoint-optimal positive detector through [MC-268](../../findings/MC-268-christoffel-endpoint-detector.md), and for its exact sparse second-moment form through [MC-269](../../findings/MC-269-christoffel-flat-sparse-quadratic-large-sieve-energy.md). The required arithmetic large-sieve estimate remains open.

Let `b_y(T)` be the Hamming weight of negative lower-prime Legendre signs for a shell subset `T`; a blind relation is exactly the endpoint event `b_y(T)=0`. MC-267 shows that the support layers `H_s` are the Krawtchouk transform of the empirical histogram of `b_y(T)`. Universal Krawtchouk identities therefore reorganize the same scalar distribution and do not supply arithmetic cancellation.

MC-268 identifies the least-wasteful positive endpoint detector. Among degree-`m` polynomials with `P(0)=1`, the Christoffel extremal polynomial

`P_m(b)=Z_m(k)^(-1) sum_(s=0)^m K_s(b;k)`, with `Z_m(k)=sum_(s=0)^m binom(k,s)`,

minimizes binomial `L^2` mass. At the live support `t~(log log y)/(log 2)`, degree `2t` already reaches the natural one-blind-atom scale; keeping `m=t+1` leaves the much more forgiving loss budget `o(k_y/m)`.

MC-269 then removes the remaining detector algebra. Writing `B_m` for lower-prime subsets of size at most `m` and `q_S` for their products, the Christoffel value on the arithmetic sign vector is exactly

`P_m(b_y(T)) = Z^(-1) sum_(S in B_m) chi_T(q_S)`.

Hence the desired endpoint estimate is equivalent to the flat sparse quadratic large-sieve inequality

`sum_(|T|=t) |sum_(S in B_m) chi_T(q_S)|^2 <= L_y binom(N_y,t) Z`,

whose literal diagonal is exactly `binom(N_y,t) Z`. The high-order moment problem has become a **second-moment problem after the correct nonlinear lift**. Every source column has coefficient one; no Gaussian/Rademacher multiplicity penalty remains.

The radial Krawtchouk expansion is still useful diagnostically, but MC-269 shows why it is a dangerous proof route if absolute values are taken layer by layer. Its coefficients are a Hamming-ball self-convolution probability law whose diagonal atom is only `1/Z`. To prove a diagonal-scale total estimate termwise, even the first nonzero layers would need precision far beyond ordinary cancellation—for example `eta_2=o(m^-2)` at `m=t+1`, with increasingly severe requirements higher up. Signed cancellation among off-diagonal source pairs is therefore part of the resource, not expendable bookkeeping.

Generic quadratic large-sieve machinery also misses the target. Embedding the exact row family into all square-free moduli pays the ambient source length `y^m` and is vastly larger than the desired fixed-weight shell diagonal. The remaining theorem must exploit the **simultaneous sparse structures on both sides**: row moduli are fixed-weight products of shell primes and columns are products of at most `m~log log y` lower primes.

The frontier is now unusually concrete. Prove the flat second-moment bound at `m=t+1` with `L_y=o(k_y/m)`, or produce an arithmetic lower bound/counterexample showing that the diagonal-scale target itself fails. More universal Krawtchouk algebra, higher monomial moments, or termwise absolute estimates do not address this residual.

**Boundary.** MC-269 excludes no blind relation and gives no new global Möbius bound. Christoffel/Krawtchouk/Hamming-ball identities are classical finite harmonic analysis; the open content is arithmetic orthogonality for this exact sparse quadratic-character matrix.
