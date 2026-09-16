# MI-043 — Stationary cross-prime Hilbert control must already contain the arithmetic log-square

**Evidence level:** exact/classical-mechanism synthesis from [WP-339](../../findings/WP-339-every-scalar-transport-cost-needs-a-quadratic-tail.md), [WP-340](../../findings/WP-340-stationary-hilbert-transport-needs-euclidean-drift.md), and [WP-341](../../findings/WP-341-cross-prime-stationary-hilbert-transport-contains-the-arithmetic-log-square.md).

WP-339 identifies the destination scale: a scalar displacement cost can uniformly control the moving UCP/Kadison variance defect only if its tail eventually dominates squared logarithmic displacement. WP-340 shows on one prime-power ray that stationary negative-type/Hilbert geometry has such quadratic growth only through an invariant Euclidean drift.

WP-341 proves that coupling all prime directions does not create a softer escape. On the finite-support prime-exponent group

`Gamma = direct_sum_p Z e_p`,

let `L(alpha)=sum_p alpha_p log p` and let `psi` be any translation-invariant squared-Hilbert, equivalently conditionally negative-definite, cost. Its abelian Levy--Khinchin decomposition has a nonnegative quadratic sector `q` plus a spectral/jump sector. Dilation extracts the quadratic part exactly:

`q(alpha)=lim_(m->infinity) psi(m alpha)/m^2`.

Therefore eventual domination `psi(alpha)>=a L(alpha)^2` for large logarithmic displacement is equivalent to `q(alpha)>=a L(alpha)^2` everywhere. The spectral/jump component cannot manufacture the missing quadratic logarithmic control.

The equivalence has a sharper representation meaning. If `q(alpha)=||D alpha||^2`, then control of `L^2` holds exactly when `L` is already a bounded Hilbert covector of the quadratic sector:

`L(alpha)=<D alpha,w>`.

On every finite prime window this says the quadratic Gram matrix contains the rank-one PSD direction `a ell ell^T`, with `ell_p=log p`. A successful stationary cross-prime metric therefore contains the arithmetic log-square explicitly in its Gaussian/drift sector; richer stationary spectral geometry only decorates that required direction.

This closes a broad topology-escalation strategy. Moving from scalar costs to stationary Hilbert embeddings, and then to cross-prime stationary Hilbert coupling, does not derive the needed second-moment control from arithmetic. It repackages that control unless a separate source theorem explains why the required quadratic log direction is small or signed in the actual channel.

The live escape must change category: derive quadratic displacement decay from genuine prime/Mangoldt structure, or use a global/noncommutative coupling whose positivity is not reducible to rowwise stationary transport. Merely choosing a CND cost that contains the log-square is not a sign mechanism.

**Boundary.** WP-341 is a classification of stationary scalar/Hilbert transport on the full exponent-displacement group. Its matched-control argument works for arbitrary free-abelian weights, so the theorem is not itself arithmetic selectivity. It does not rule out nonstationary, noncommutative or globally coupled constructions, and it does not prove Weil positivity.