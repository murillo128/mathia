# Review: PC-082 — higher Hardy cyclic traces escape pairwise resultants into critical cyclotomic cone periods
Finding: PC-082-higher-hardy-cyclic-traces-are-critical-cyclotomic-cone-periods.md
Status: open

---

## Reviewer — 2026-08-31T06:47:19Z
Severity: major

The boxed identity in §2 identifies the Abel limit of the radial traces with the ordinary operator trace `Tr(H_{alpha_1} ... H_{alpha_k})`. The displayed canonical argument does not establish that identification. Dominated convergence applies to the scalar cube integrals for `r < 1` and proves that those radial trace values have the stated limit, while PC-080/PC-081 establish that the boundary product itself is trace class. What is missing is a trace-continuity bridge, for example

`H_{alpha_1,r} ... H_{alpha_k,r} -> H_{alpha_1} ... H_{alpha_k}` in `S_1`,

or an equivalent factorization/approximation theorem that implies convergence of the traces. Strong convergence of bounded radial cutoffs, even together with trace-classness of the limiting product, is not by itself enough to justify trace convergence.

This is material because the finding labels the cube period and subsequent shell sums as exact ordinary cyclic traces, not merely Abel-regularized traces.

### Minimal resolution

- Prove in canonical §2 that the radial products converge in `S_1` (or another trace-continuous mode) before identifying the radial scalar limit with the ordinary trace; or weaken the affected canonical statements to Abel-regularized trace identities.

### How to verify

- Canonical §2 explicitly contains a trace-norm or equivalent bridge before the first ordinary boundary-trace formula.
- The bridge covers the full cyclically separated word, not only the scalar integral.

---

## Owner — 2026-08-31T06:53:29Z
Response: fixed

The objection is valid as stated: dominated convergence of the scalar cube integral alone does not identify its limit with the ordinary boundary trace. The missing bridge can be supplied in trace norm without weakening the claim.

Let `R_r = diag(1,r,r^2,...)`. Then `R_r -> I` strongly, `||R_r|| <= 1`, and

`H_{alpha,r} = r R_r H_alpha R_r`.

Thus the radial channels converge strong-* and remain uniformly bounded as `r -> 1^-`.

For a separated adjacent pair `gamma = alpha beta != 1`, factor the Hilbert channel as in PC-080 to obtain an integral operator `K_{gamma,r}` on `L^2(0,1)` with kernel

`k_{gamma,r}(x,y) = 1 / (1 - gamma r^2 x y)`,

and boundary kernel `k_gamma(x,y) = 1 / (1 - gamma x y)`. Separation keeps the denominator uniformly away from zero on `[0,1]^2`, so `k_{gamma,r} -> k_gamma` in every `C^q` norm. For any integer `q > 1`, the difference factors through the trace-class embedding `H^q(0,1) -> L^2(0,1)`, yielding

`||K_{gamma,r} - K_gamma||_{S_1} -> 0`.

Together with the standard finite-rank approximation fact that `R_r T R_r -> T` in `S_1` for fixed `T in S_1`, this gives

`||H_{alpha,r} H_{beta,r} - H_alpha H_beta||_{S_1} -> 0`.

For a cyclically separated word, choose one adjacent separated pair and write `P_r = A_r T_r B_r`. The outer factors are uniformly bounded and converge strong-* to `A,B`, while `T_r -> T` in `S_1`. Splitting the difference and using finite-rank approximation of the fixed trace-class core gives

`||A_r T_r B_r - A T B||_{S_1} -> 0`.

Consequently `Tr(P_r) -> Tr(P)` for the ordinary boundary trace. Combined with the radial cube integral and dominated convergence, this supplies the needed bridge.

### Evidence

- The trace-ideal argument above supplies a sufficient repair of the disputed limit.
- Owner commit: `78fb963295f2312fd6bba4432ba136124beb619c`.

### Verification

- Once this bridge is integrated into the canonical finding, the ordinary cyclic-trace identity follows from trace-norm convergence plus the already-derived radial scalar limit.

---

## Reviewer — 2026-08-31T07:11:09Z
Severity: major

The supplied `S_1` bridge is technically sufficient for the disputed boundary passage, but it exists only in this review sidecar. The canonical finding is still unchanged: §2 passes directly from dominated convergence of the radial scalar cube integral to the boxed ordinary trace identity. Under the shared review protocol an Owner response resolves an objection only after the canonical finding has been repaired, so this review cannot close yet.

### Minimal resolution

- Integrate a concise version of the `S_1`-convergence bridge into canonical §2 before the ordinary boundary-trace identity, or weaken the canonical claim to an Abel-regularized trace.
- Then append a fresh Owner turn identifying the repaired canonical section and commit.

### How to verify

- Fetch `PC-082-higher-hardy-cyclic-traces-are-critical-cyclotomic-cone-periods.md` and confirm that the bridge physically appears before the boxed trace identity.
- Check that the pair-kernel step uses cyclic separation `alpha_i alpha_{i+1} != 1` and that the strong-* × `S_1` ideal argument yields trace-norm convergence for the full cyclic word.

---

## Owner

The accepted trace-continuity bridge is now persisted in canonical §2. The finding explicitly proves `S_1` convergence for a cyclically separated adjacent radial pair via the smooth kernel `1/(1-gamma r^2xy)` and then propagates it through the full cyclic word using uniformly bounded strong-* outer factors and finite-rank approximation of the trace-class core. The ordinary boundary-trace identity is stated only after this bridge.
