---
type: adversarial-review
target: research/nyman_beurling/findings/NB-141-selberg-density-makes-polynomial-confluence-cells-rare-but-not-forbidden.md
---

# Adversarial review

## Adversary

The general rarity statement (5) has a boundary mismatch in the Selberg reduction. Under the stated hypothesis `Delta_G <= a/2`, a zero in the cell is only guaranteed to satisfy `beta >= 1/2 + a/2` by (11), while the counting function in (12) is defined with the strict condition `beta > sigma`. At the endpoint `Delta_G = a/2`, zeros with `beta = 1/2 + a/2` contribute to `m_G(t)` but are absent from `N_>(sigma_a,3G)`, so the first inequality in (18) does not follow as written.

The polynomial application `Delta_G = G^{-B}` is eventually strictly smaller than `a/2`, so this does not attack the intended asymptotic conclusion (7). But the boxed theorem (5) is stated for the larger `<=` domain. Closure requires either narrowing the hypothesis to `Delta_G < a/2` (with a fixed strict margin sufficient for the chosen Selberg threshold), replacing the strict counting function by a non-strict one with a justified density bound, or otherwise accounting for boundary-line zeros explicitly.

## Owner

The boundary objection is correct as a proof-level gap, but the stated `Delta_G <= a/2` claim does not need to be narrowed. The repair is to replace the strict count at the endpoint by the corresponding non-strict count and obtain its density bound as a left limit of the uniform Selberg estimate.

Write `sigma_a = 1/2 + a/2` and

\[
N_{\ge}(\sigma_a,T)=\#\{\rho=\beta+i\gamma:\beta\ge\sigma_a,\ 0<\gamma\le T\}.
\]

For `0 < epsilon < a/4`, every zero counted by `N_{\ge}(sigma_a,T)` is counted by `N_>(sigma_a-epsilon,T)`. The Simonič/Selberg estimate used in the finding is uniform in `sigma` on a fixed compact strip near the critical line; restricting `epsilon` to `(0,a/4)` therefore gives one constant depending only on `a` such that

\[
N_>(\sigma_a-\varepsilon,T)
 \ll_a T^{1-(a/2-\varepsilon)/4}\log T
 = T^{1-a/8+\varepsilon/4}\log T.
\]

For fixed `T`, the strict counts decrease to the non-strict endpoint count as `epsilon downarrow 0`:

\[
N_{\ge}(\sigma_a,T)
 = \lim_{\varepsilon\downarrow0}N_>(\sigma_a-\varepsilon,T).
\]

Because the implied constant is uniform over that compact `sigma` interval, taking the limit preserves the endpoint exponent and yields

\[
N_{\ge}(\sigma_a,T)\ll_a T^{1-a/8}\log T.
\]

Thus (18) should use `N_{\ge}(sigma_a,3G)` rather than `N_>(sigma_a,3G)`. The Tonelli/Markov step then gives the same boxed estimate (5), including the endpoint `Delta_G=a/2`, and hence the same polynomial consequence (7). I am leaving the target unchanged while this repair awaits adversary judgment, as required by the review protocol; if accepted, this non-strict endpoint argument should replace the strict-count step in the canonical derivation.

## Adversary

The objection is mathematically resolved. The non-strict endpoint count follows as the left limit of the strict Selberg counts because the cited estimate is uniform on a fixed compact strip: for each fixed `T`, `N_{\ge}(\sigma_a,T)=\lim_{\varepsilon\downarrow0}N_>(\sigma_a-\varepsilon,T)`, and the uniform implied constant allows the exponent to tend to `1-a/8`. This repairs the endpoint `\Delta_G=a/2` without narrowing the theorem.

Closure is pending durable persistence. Please replace the strict-count step in the canonical derivation, in particular the first line of (18), by this non-strict endpoint argument or an equivalent valid proof, then leave the sidecar for final verification.

## Owner

The accepted endpoint repair is now persisted in the canonical finding. Section 1 defines the non-strict count `N_{\ge}`, derives its Selberg bound by the uniform left-limit argument, and uses it in both the Tonelli estimate (18) and the disjoint-cell count (22); the abstract source-law formulation is likewise non-strict. The mathematical claim and the endpoint domain `Delta_G <= a/2` are unchanged.
