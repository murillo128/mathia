---
id: CLUE-mobius-cancellation-mean-absolute-mertens-transfer-budget
type: research-clue
status: accepted
origin: master-researcher
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-001-local-to-global-exceptional-mass-barrier.md
  - research/mobius_cancellation/findings/MC-006-averaged-chowla-vdc-logarithmic-ceiling.md
  - research/mobius_cancellation/findings/MC-009-pintz-mean-absolute-zero-boundary.md
  - research/mobius_cancellation/findings/MC-013-discrete-tanaka-l1-feedback-carrier.md
  - research/mobius_cancellation/findings/MC-016-random-walk-excursion-overconstraint-path-energy.md
  - research/mobius_cancellation/findings/MC-019-path-energy-coarse-riesz-rh-equivalence.md
  - research/mobius_cancellation/findings/MC-044-growing-riesz-endpoint-visibility-delay.md
  - research/mobius_cancellation/findings/MC-115-mean-absolute-mertens-mellin-zero-free.md
  - research/mobius_cancellation/findings/MC-116-subpower-dense-mean-absolute-checkpoints.md
  - research/mobius_cancellation/findings/MC-117-fractional-mertens-moment-transfer-ceiling.md
  - research/mobius_cancellation/findings/MC-118-balanced-prime-block-multiplicative-fractional-moment-barrier.md
  - research/mobius_cancellation/findings/MC-119-uniform-polynomial-window-fractional-moment-barrier.md
---

# Can a source-natural local statistic transfer polynomially to mean-absolute Mertens scale?

## Observation

The current local and averaged inputs remain below the polynomial information budget needed for RH-scale summatory control. `MC-001` isolates the exceptional-mass barrier for almost-all short intervals, while `MC-006` shows that the available averaged two-point Chowla input yields only logarithmic saving through the audited black-box van der Corput route.

The endpoint is now cleaner than when this clue was created. Define

`D_M(X)=X^(-1) integral_1^X |M(x)| dx`.

`MC-115` proves directly, without the fresh Pintz theorem, that

`RH iff D_M(X)=O_epsilon(X^(1/2+epsilon)) for every epsilon>0`.

The reason is absolute Mellin convergence: an RH-scale upper bound for the first absolute moment analytically continues `1/zeta(s)` into every half-plane `Re(s)>1/2+epsilon` and therefore excludes off-critical zeros. `MC-009` now has a narrower role: Pintz's still-audited theorem proposes the stronger full logarithmic-order identity tying `D_M`, a terminal-window maximum, and the rightmost zero boundary.

`MC-116` further reduces the required scale coverage. The RH-scale bound for `D_M` need not be proved at every cutoff: it is enough to prove it along any fixed checkpoint sequence with `log X_(j+1)/log X_j -> 1`. Monotonicity of the cumulative absolute mass fills the intervening scales without exponent loss, even when the multiplicative checkpoint gaps tend to infinity. Fixed power-lacunary checkpoints instead pay an explicit interpolation loss.

`MC-117` closes another apparent weakening. For every `0<p<1`, bounded increments give a sharp transfer ceiling from the fractional time quasi-mean `P_p(X)=(X^(-1) integral_0^X |M(u)|^p du)^(1/p)` to the first absolute mean. At square-root scale the generic exponent lands at `1/(p+1)>1/2`. More strongly, an exact-square-free-support qualitative-Chowla control can satisfy `P_p(X_j)=O_epsilon(X_j^(1/2+epsilon))` on the subpower-dense mesh `X_j=floor(exp(j^2))` while its first absolute mean is `Omega(X_j^(1/(p+1)))`. Thus moving below `L^1` does not evade the source-to-endpoint burden unless additional source-specific structure beats that pathwise ceiling.

`MC-118` removes **generic multiplicativity** as the obvious missing structure. A balanced terminal block of prime signs can be embedded in an exact-square-free-support multiplicative function, produce a super-square-root first-absolute excursion, return exactly to its auxiliary endpoint, and retain square-root `p`-moment bounds both at the source scale and at a future scale `T=Q exp(sqrt(log Q))`. The exact transport identity shows why: endpoint matching replicates the excursion into thin multiplier windows, and for `p<1` the total replicated mass remains below the critical power budget.

`MC-119` now removes the immediate finite-scale-density repair as well. The same balanced-block construction can be chosen so that, for a fixed `theta>1`, the RH-scale fractional bound holds **uniformly at every cutoff `Q<=X<=Q^theta`**, up to a polylogarithmic factor, while `D_1(Q)` still has exponent strictly above `1/2`. The admissible polynomial horizon is explicit: for each `p<1`, every `theta<(5-3p)/(4-2p)` is achievable with some super-square-root excursion exponent. Thus continuity of the weak statistic across all intermediate scales in a substantial finite window is still not the missing recovery principle.

## Research question

Can a source-natural signed local, bilinear, multiplicative, or multiscale **Möbius-specific** statistic control `D_M(X)` with a genuine polynomial-gain transfer inequality strong enough to yield

`D_M(X)=O_epsilon(X^(1/2+epsilon))`

at least on a predetermined subpower-dense checkpoint sequence, without first proving a pointwise RH-scale bound for `M(X)` or inserting an equivalent global/coarse statistic into the hypotheses?

After `MC-119`, a viable source condition must use information not present in a moving exact-support multiplicative comparator even when that comparator satisfies the weak statistic uniformly through a polynomial future window. Exact agreement with `mu(p)=-1` at every prime, together with exact support and multiplicativity, is not a useful intermediate condition because `MC-005` already notes that it reconstructs Möbius tautologically. The live candidates are therefore **quantitative intermediate** conditions: one fixed function coherently through an unbounded scale sequence, a genuinely joint correlation-plus-multiplicativity constraint, a quantitative prime-local law weaker than exact identification, or another exact Möbius identity that forbids balanced prime-block transport without encoding the target itself.

The missing bridge is still entirely arithmetic: once the mean-absolute estimate is proved on a qualifying scale mesh, `MC-116` fills the physical-scale gaps and `MC-115` closes zero exclusion.

## Why it may matter

Mean-absolute control is formally weaker than pointwise Mertens control and is insensitive to some sparse pointwise spikes. It is nevertheless RH-complete. A successful transfer to this endpoint could therefore avoid solving a needlessly strong uniform problem while still closing the RH implication exactly.

The checkpoint reduction makes the output surface smaller: a source-natural argument that only produces estimates at selected resolutions can still be sufficient if consecutive checkpoint logarithms have ratio tending to one. Conversely, matched controls `MC-117`--`MC-119` show progressively that weak sub-`L^1` information can coexist with excessive first-absolute mass even after exact support, qualitative correlation information, multiplicativity, and finally continuous scale coverage over a polynomial horizon are added separately. The remaining question is no longer whether a denser finite set of weak-statistic observations repairs the loss, but what **source-specific coherence** prevents the rare balanced excursion itself.

## Decisive test

Fix an explicit source-natural statistic and prove one of two outcomes:

1. derive a source-compatible implication from a quantitatively polynomial hypothesis on that statistic to `D_M(X_j)=O_epsilon(X_j^(1/2+epsilon))` on a predetermined sequence with `log X_(j+1)/log X_j -> 1`, with exceptional sets, scale transitions, correlation range, coarse modes, smoothing, reconstruction losses, and checkpoint coverage explicit; or
2. construct a **fixed-function or equally source-faithful** matched control satisfying the proposed local/multiscale hypothesis while its mean-absolute partial-sum process retains exponent `>1/2`.

A candidate fails if the proposed transfer input already contains an RH-equivalent fixed Riesz/coarse mode, if smoothing makes the desired scale vacuous, if inversion reintroduces the original partial-sum burden, if the only gain comes from a triangle inequality that spends the polynomial saving on exceptional mass, if a sub-`L^1` compression discards rare coherent amplitude without a source-specific recovery mechanism, if it relies only on generic multiplicativity or exact square-free support, if merely demanding the same weak bound throughout a finite polynomial window is its recovery mechanism, or if the controlled checkpoints are power-lacunary and no additional source-specific interpolation pays the resulting exponent gap.

## Evidence boundary

`MC-115` independently establishes the RH implication of the mean-absolute upper bound, so that implication no longer inherits the `NEEDS-AUDIT` status of `MC-009`. The stronger Pintz claims about the **full limiting logarithmic exponent** and the terminal-window maximum remain audit-sensitive and must not be treated as independently verified.

`MC-116` is only an exact scale-interpolation reduction. It does not produce cancellation at any checkpoint and does not show that power-lacunary scale meshes are impossible when additional arithmetic information is available.

`MC-117` is a sharp generic transfer obstruction plus a nonmultiplicative exact-support qualitative-Chowla control. `MC-118` restores exact support and multiplicativity and transports the weak statistic to a future subpower scale. `MC-119` strengthens that same multiplicative control to every cutoff throughout a fixed polynomial window. The `MC-118`/`MC-119` comparator still depends on the source scale and does not preserve qualitative Chowla. These findings therefore do **not** rule out a theorem for the actual Möbius function that exploits one fixed function across unbounded scales, a genuinely joint quantitative correlation/multiplicativity condition, or another intermediate arithmetic constraint unavailable to the moving comparator.

No current local theorem in this line proves the required RH-scale bound for `D_M` even on a qualifying checkpoint mesh. The Mellin and interpolation bridges reduce the downstream burden; they do not reduce the upstream arithmetic difficulty of producing the bound.

## Research disposition

**Accepted, narrowed by `MC-115`--`MC-119`.** Earlier work eliminated several tempting but over-strong or information-losing carriers. The Tanaka/excursion branch showed that long excursions can coexist with diffusive mean-absolute behavior; the path-energy branch exposed an RH-equivalent first Riesz coarse mode; fixed-order Riesz smoothing remains RH-equivalent, while growing-order smoothing either becomes normalization-vacuous or delays endpoint visibility and requires a nontrivial inversion carrier. `MC-117` ruled out sub-`L^1` time moments as a free relaxation even with exact support, qualitative Chowla, and subpower-dense scale coverage. `MC-118` showed that generic multiplicativity does not repair that loss. `MC-119` now shows that **making the weak multiplicative control uniform over every scale in a polynomial window does not repair it either**.

The active residual is consequently source-specific and long-range. A surviving statistic must preserve first-moment sensitivity to rare coherent amplitude or prove that a single fixed arithmetic source cannot reproduce the balanced-block mechanism across an unbounded sequence of scales. The strongest concrete frontier is now a quantitative joint condition tying multiplicative consistency to correlations or prime-local structure without simply specifying Möbius itself. The clue remains accepted rather than resolved because no polynomial transfer from such genuinely Möbius-specific information to `D_M` has yet been established.