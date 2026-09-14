# VIS-220 — simple-cycle packing has a universal envelope ceiling and cannot reach RMS saturation

## Claim

Keep the finite Hermitian zero-diagonal setup of `VIS-215`. For each oriented simple support cycle `C`, write

`rho_+(C)=|1-H_+(C)|^2/R(C)`,

`rho_-(C)=|1-H_-(C)|^2/R(C)`,

with

`R(C)=sum_(e in C) 1/w_e`,

and let `P_+`, `P_-` be the corresponding optimal fractional cycle-packing values under the edge-capacity constraints

`sum_(C contains e) lambda_C <= 1`.

Let `g` be the girth of the support graph, with `g=+infinity` when the graph is acyclic. Put

`W_1=sum_e w_e`, `B=2W_1`, `R=2 sum_e w_e^2`,

and `N_eff=W_1^2/sum_e w_e^2` as in `VIS-219`.

Then, whenever the graph has a cycle,

`P_+ <= (4/g^2) W_1 = (2/g^2) B`,

`P_- <= (4/g^2) W_1 = (2/g^2) B`.

Hence the `VIS-215` packing certificate obeys the universal lower floor

`U_pack := B-min(P_+,P_-)`
`        >= (1-2/g^2) B`,

and therefore

`D_pack := U_pack/sqrt(R)`
`        >= (1-2/g^2) sqrt(2 N_eff)`.

For an ordinary simple support graph, `g>=3`, so in particular

`P_+,P_- <= 2B/9`,

`U_pack >= 7B/9`,

`D_pack >= (7/9) sqrt(2 N_eff)`.

Thus the fractional simple-cycle packing certificate of `VIS-215` can **never** approach the envelope saturation demanded by `VIS-219`; its relative deficit is bounded below by the universal constant `7/9` before any arithmetic information enters.

Applied to the strictly subcritical prime-phase matrices `A_(y,H)` of `VIS-218`, where

`N_eff asymp_(alpha,v) y^2/[H (log y)^2] -> infinity`,

one gets

`D_pack(y,H) >>_(alpha,v) y/[sqrt(H) log y] -> infinity`.

Therefore the `VIS-215` fractional simple-cycle packing route is parametrically incapable of certifying Haar-RMS-scale worst-start suppression throughout the strictly subcritical regime. This closes the current packing relaxation itself; it does **not** lower-bound the exact fixed-modulus torus optimum, rule out stronger non-packing frustration certificates, or address one-parameter orbit access.

**Evidence/status:** `EXACT-DERIVED + UNIVERSAL CERTIFICATE CEILING + NEGATIVE RELAXATION CLOSURE + NO-NOVELTY-CLAIM`.

## 1. Every simple-cycle reward is at most a fixed fraction of its edge mass

Let `C` have length `k=|C|`. Since `H_+(C)` and `H_-(C)` lie on the unit circle,

`|1-H_+(C)|^2 <= 4`,

`|1-H_-(C)|^2 <= 4`.

Weighted Cauchy-Schwarz gives

`(sum_(e in C) w_e)(sum_(e in C) 1/w_e) >= k^2`.

Hence

`1/R(C) <= [sum_(e in C) w_e]/k^2`.

Combining the two inequalities yields, for either sign,

`rho_±(C)`
` = |1-H_±(C)|^2/R(C)`
` <= 4 [sum_(e in C) w_e]/k^2`.

If the graph has girth `g`, every simple cycle has `k>=g`, so

`rho_±(C) <= (4/g^2) sum_(e in C) w_e`.

No phase assumption is used. Even a maximally frustrated cycle cannot convert more than this fraction of its total edge mass into the `VIS-215` reward because the same cycle inequality that creates the certificate pays the harmonic-resistance factor `1/R(C)`.

## 2. Edge capacity turns the local ceiling into a global ceiling

For any feasible fractional packing `lambda_C`, summing the preceding bound gives

`sum_C lambda_C rho_±(C)`
` <= (4/g^2) sum_C lambda_C sum_(e in C) w_e`
` =  (4/g^2) sum_e w_e sum_(C contains e) lambda_C`
` <= (4/g^2) sum_e w_e`
` =  (4/g^2) W_1`.

Maximizing over all feasible packings proves

`P_± <= (4/g^2)W_1`.

Since `B=2W_1`, this is

`P_±/B <= 2/g^2`.

For a simple graph `g>=3`, so `P_±/B<=2/9`. The result is stronger than saying that near-saturation has not yet been found: **near-saturation is structurally impossible for this certificate**.

The acyclic boundary is consistent. When there are no cycles, `P_+=P_-=0`, so the certificate is exactly the trivial envelope `U_pack=B`.

## 3. The packing certificate stays on the absolute-envelope scale

`VIS-219` derived the exact normalized identity

`U_pack/sqrt(R)`
` = sqrt(2N_eff) [1-min(P_+,P_-)/B]`.

The universal packing ceiling gives

`1-min(P_+,P_-)/B >= 1-2/g^2`.

Therefore

`D_pack >= (1-2/g^2) sqrt(2N_eff)`.

In a simple graph this becomes

`D_pack >= (7/9)sqrt(2N_eff)`.

Thus the fractional packing relaxation cannot improve the absolute envelope by more than a fixed fraction, whereas an RMS-scale certificate with diverging `N_eff` requires the relative residual to shrink like `N_eff^(-1/2)`.

This identifies the exact failure mode. The obstruction is not insufficient arithmetic frustration, poor cycle selection, weak LP optimization, or failure to enumerate enough cycles. It is already built into the combination of the one-cycle harmonic-resistance reward and the unit edge-capacity packing rule.

## 4. Strictly subcritical prime-phase consequence

`VIS-218` proves

`N_eff asymp_(alpha,v) y^2/[H(log y)^2]`

under

`H->infinity`, `H log y/y ->0`.

Hence

`sqrt(N_eff) asymp_(alpha,v) y/[sqrt(H) log y] -> infinity`.

Applying the simple-graph floor gives

`D_pack(y,H)`
` >= (7/9)sqrt(2N_eff)`
` >>_(alpha,v) y/[sqrt(H) log y]`
` -> infinity`.

So the proposed near-saturation test from `CLUE-magnetic-packing-envelope-saturation` has a decisive analytic answer: the `VIS-215` certificate cannot saturate even on an optimally chosen family of cycles and even under the most favorable possible holonomies.

This is a closure of the **certificate family**, not of the prime-phase torus problem. A stronger argument may couple overlapping cycle constraints nonlinearly, use a different dual relaxation, or attack the exact unit-modulus quadratic optimization of `VIS-213`. Such a mechanism would be a new research thread because it would no longer be the fractional simple-cycle packing certificate analyzed here.

## 5. Prior-art and novelty boundary

The ambient setting is classical magnetic/gain-graph synchronization and frustration. `VIS-215` already anchors that boundary to Bandeira--Singer--Spielman, Lange--Liu--Peyerimhoff--Post, and the cycle-holonomy literature. A targeted literature check again found standard frustration-index, magnetic-cycle, gain-Laplacian, and cycle-holonomy treatments, including exact single-cycle magnetic frustration formulas, but this finding makes no claim that the elementary packing ceiling is absent from that literature.

The proof here uses only `|1-H|<=2`, weighted Cauchy-Schwarz, and the existing edge-capacity LP. Its Mathia value is not theorem novelty but the consequence for the live certificate: the saturation target isolated in `VIS-219` is algebraically unreachable by `VIS-215`.

## Boundaries and falsification

The `2/g^2` fraction concerns exactly the `VIS-215` LP built from **simple-cycle rewards** `|1-H_±(C)|^2/R(C)` and per-edge capacity at most one. It does not apply automatically to a different relaxation that assigns stronger rewards, couples cycles nonlinearly, permits another resource accounting, or directly optimizes the torus energy.

The support graph is the ordinary simple graph induced by nonzero off-diagonal matrix entries. If a future construction genuinely uses parallel-edge or higher-order objects, its minimum circuit size and accounting must be rederived rather than importing `g>=3` blindly.

Falsify this result by finding an error in the unit-circle bound `|1-H|^2<=4`, the harmonic-mean inequality `1/R(C)<=sum_C w_e/|C|^2`, the exchange of the cycle/edge sums, or the application of the packing capacity constraint.

## Research consequence

The cycle-packing saturation clue is resolved negatively. Further work on the strictly subcritical worst-start problem should leave the `VIS-215` fractional simple-cycle packing relaxation, just as `VIS-218` already closed the normalized magnetic spectral relaxation. The remaining static object is the exact fixed-modulus torus optimization or a genuinely stronger certificate that preserves interactions discarded by both relaxations; finite-time prime-log access remains a separate problem.