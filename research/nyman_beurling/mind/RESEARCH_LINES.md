# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Exclude a nonzero locally natural stable tail by controlling global causal extension cost

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`.

NB-049--NB-063 reduce the collective late quotient to a finite-rank forward-memory channel. Every compact-time defect sector is infinite-dimensional, every visible natural window has maximal causal rank, and old visible information can enter the new logarithmic cell only through the finite-rank continuation map `Gamma_R`.

NB-064--NB-065 show that persistence would force the distinguished normalized target into weaker and weaker singular sectors with finite total transmitted mass. In particular, on any scale set where a fixed target fraction sees singular values at least `eta_R`, persistence requires `sum eta_R^2<infinity` up to the standard bounded-threshold normalization.

NB-066 makes the persistence geometry much more rigid. Let

\[
\mathcal T_\infty
=\mathcal D\ominus\mathcal K_{\rm fin}.
\]

Then

\[
\boxed{
\mathcal T_\infty
=\{t\in\mathcal D:J_Rt\in\mathcal G_R\text{ for every }R\}.
}
\]

A stable-tail vector is therefore globally orthogonal to the natural Nyman space while looking **exactly natural on every finite Paley--Wiener window**. For the canonical residual `h_*`, the moving visible projections converge strongly to one fixed mode

\[
t_*=P_{\mathcal T_\infty}h_*,
\qquad
\delta_\infty=\|t_*\|.
\]

If persistence occurs, the normalized directions do not wander among unrelated bad singular sectors; they converge to `t_*/||t_*||`.

The same finding supplies a stronger source-only obstruction. For `0!=t in T_infinity`, let `E_R(t)` be the least future norm of a genuine natural vector whose finite trace equals `J_Rt`. Exact global orthogonality gives

\[
\mathfrak E_R(t)\,\|(I-J_R)t\|
\ge\|J_Rt\|^2,
\]

so `E_R(t)->infinity`. Equivalently, if `Lambda_R` is the worst minimal causal-extension ratio over the local natural space, any bound on `Lambda_R` along an unbounded sequence forces `T_infinity={0}` and eliminates every stable tail, not only the canonical one.

NB-066 also gives the fixed mode an exact unfiltered one-cell budget: for `g_R=J_Rt`, the actual transmitted pieces satisfy a square-summable identity, hence `sum ||Gamma_R g_R/||g_R||||^2<infinity`. Persistence therefore combines two apparently opposite facts: **one-cell transmission becomes square-summably weak, while exact global natural continuation of the same locally natural trace requires an exploding far-future tail**.

The live theorem is now more concrete than a uniform singular gap. Prove an oracle-free upper bound for the causal extension constants `Lambda_R` on an unbounded family of windows, or otherwise show that the canonical arithmetic trace cannot realize a nonzero vector that is locally natural at every scale but globally orthogonal to the natural closure. A moving target-transmission lower bound remains sufficient, but NB-066 exposes a stronger global continuation route.

## Treat individual disappearance, defect abundance, rank, forward memory, local naturality, extension cost, and accumulated transmission as separate gates

Late individual shifts can vanish while the collective family remains visible. Every finite window already has infinite-dimensional defect; every visible natural window already has maximal causal rank. Merely having poorly transmitted singular directions is cheap: they obstruct only if the canonical target occupies them.

NB-066 adds that exact finite-window naturality is also cheap in principle. A nonzero stable-tail mode can match the natural space on **every** finite window while failing global naturality maximally: compatible exact extensions must spend unbounded norm in the unseen future. Thus finite local interpolation, local rank, one-cell transmission, and globally controlled continuation are distinct resources.

Near-kernel tracking remains necessary, not sufficient. In the flat control `Gamma_R=0`, every visible direction is a kernel direction while the collective target tail still vanishes. Future progress can therefore attack either side of the same obstruction: force nonsummable transmitted target mass, or prove that locally natural traces admit globally controlled causal extensions often enough to exclude a stable tail.