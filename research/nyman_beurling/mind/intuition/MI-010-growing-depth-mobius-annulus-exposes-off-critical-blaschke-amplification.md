# MI-010 — Finite distinct off-critical zero states add their normalized growing-depth volume repair

**Evidence level:** exact through [NB-092](../../findings/NB-092-growing-depth-mobius-annulus-mode-forces-polynomial-blaschke-gram-gain.md), [NB-093](../../findings/NB-093-single-zero-growing-depth-gram-gain-is-rank-one-causal-state-leverage.md), [NB-094](../../findings/NB-094-zero-cancellation-keeps-coordinate-state-cost-bounded-while-leverage-grows.md), and [NB-095](../../findings/NB-095-finite-distinct-zero-states-add-their-growing-depth-volume-repair.md) for every fixed finite set of pairwise distinct actual zeros `rho_r=beta_r+i gamma_r` with `beta_r>1/2`. Growing-cardinality divisors, repeated zeros, and any final Nyman-distance implication remain open.

Growing multiplicative depth exposes a genuine arithmetic near-kernel. On the band `m<=j<mq`, NB-092 constructs a canonical Möbius annulus whose raw Gram energy becomes small while an off-critical Blaschke factor repairs the same direction at scale `q^(2beta-1)`. NB-093 identifies the one-zero repair as a causal-state rank-one update, and NB-094 uses the exact zero identity to show that every state coordinate is only `O_rho(R^(-1/2))` even while inverse-Gram leverage grows like `q^(2beta-1)`. Diagonal normalization therefore costs only `O_rho(1)` and retains the full one-zero exponent.

NB-095 closes the fixed finite-state interaction problem. For a fixed set `F={rho_1,...,rho_d}` of distinct right-half zeros, successive causal states on partially deflated sources are a **fixed invertible triangular transform** of the raw single-zero state vectors. After the anisotropic scaling by `q^(rho_r-1/2)`, the raw inverse-Gram interaction converges uniformly to a positive Cauchy/model-space Gram of the exponentials `e^(-(rho_r-1/2)t)` on `[0,log q]`. Distinct zero directions therefore remain linearly independent rather than collapsing into the largest one.

If

`A_F=sum_r (beta_r-1/2)`,

then for `R=mq`, uniformly for `m` sufficiently large and every `q>=2`,

`det R_(m,mq)^[F] / det R_tilde_(m,mq) asymp_F q^(2A_F)`.

Equivalently,

`log(det R^[F]/det R_tilde)=2 sum_r(beta_r-1/2) log q + O_F(1)`.

Thus finite distinct zero interactions do not screen the normalized volume repair: **their horizontal masses add**. The centered correlation-entropy sign remains the same as for one zero—a repair/entropy deficit, not a positive entropy charge.

This changes the residual problem. One-state normalization and fixed finite-state interaction are both closed. A genuinely new obstruction must appear only when the divisor is no longer a fixed finite set: growing state count with depth, repeated/multiple zeros, loss of uniform conditioning of the model-space Gram as ordinates/real parts vary, or the separate step converting the determinant repair into the target Nyman distance.

The structural lesson is that coordinate smallness and collective leverage remain different resources even for several zeros. Exact source cancellation keeps each raw state cheap in the generator coordinates, while the inverse-Gram geometry retains their independent horizontal directions. Any future screening mechanism must therefore exploit a limit in the zero family, not merely finite nonorthogonality among causal states.

**Boundary.** NB-095's constants depend on the fixed set `F`; it does not give estimates uniform in `|F|`, in close/confluent zero configurations, or in an infinite Blaschke divisor. Additivity for every fixed finite set is not yet an infinite-divisor theorem and does not by itself produce a lower bound for the Nyman distance.
