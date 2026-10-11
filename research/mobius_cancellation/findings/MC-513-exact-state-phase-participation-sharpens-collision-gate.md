# MC-513 — Exact state-phase participation sharpens the same-state collision gate

**Evidence:** \`EXACT-DERIVED · SOURCE-RESOLVED-COLLISION-CERTIFICATE · CLASSICAL-ORDER-TWO-DIVERSITY+DERIVED-SPECIALIZATION · PRIOR-ART-AUDITED · NO-GENERAL-NOVELTY-CLAIM · NON-RH\`

## Claim

Retain the actual nonnegative pair-resolved first-exit coefficients of \`MC-511/512\`:
\[
b_u(t)\ge 0,\quad u\in\mathcal P,\quad t\in\mathbf F_p,\qquad
W=\sum_{u,t}b_u(t)>0.
\]
Each ordered source pair has its exact gauge-invariant relative state \(\sigma(u)=\Lambda_z(u)\). Put
\[
c_{\sigma,t}=\sum_{u:\sigma(u)=\sigma}b_u(t),\quad
c_t=\sum_\sigma c_{\sigma,t},\quad
C_{\rm same}=\sum_{\sigma,t}c_{\sigma,t}^2,\quad
C=\sum_t c_t^2.
\]
For states with \(w_\sigma:=\sum_t c_{\sigma,t}>0\), define
\[
\beta_\sigma=w_\sigma/W,\qquad
\pi_\sigma(t)=c_{\sigma,t}/w_\sigma,\qquad
S_\sigma=\left(\sum_t\pi_\sigma(t)^2\right)^{-1}.
\]
Define **effective state participation** and the squared-state-mass-weighted harmonic phase participation by
\[
R_{\rm state}=\left(\sum_\sigma\beta_\sigma^2\right)^{-1},\qquad
\lambda_\sigma=\frac{\beta_\sigma^2}{\sum_\tau\beta_\tau^2},\qquad
S_{\rm state\text{-}phase}
=\left(\sum_\sigma\frac{\lambda_\sigma}{S_\sigma}\right)^{-1}.
\]
Then the effective participation *after exact-state aggregation* is
\[
\boxed{
R_{\rm same}:=\frac{W^2}{C_{\rm same}}
=R_{\rm state}S_{\rm state\text{-}phase}.
}\tag{1}
\]
Consequently the normalized same-state tariff is an **identity**, not the maximum-fibre bound of \`MC-511\`:
\[
\boxed{
\frac{p C_{\rm same}}{W^2}
=\frac{p}{R_{\rm state}S_{\rm state\text{-}phase}}
=\frac p{R_{\rm same}}.
}\tag{2}
\]
Thus \(R_{\rm same}\ge p\) is *equivalent* to same-state collision mass not exceeding the physical uniform baseline \(W^2/p\). If \(R_{\rm same}/p\to\infty\), that mass is \(o(W^2/p)\). This is a coefficient-level criterion, not a source-proved bound on its factors.

## Derivation and comparison with MC-511/512

For each active state,
\[
\sum_t c_{\sigma,t}^2
=w_\sigma^2\sum_t\pi_\sigma(t)^2
=\frac{w_\sigma^2}{S_\sigma}.
\]
Therefore
\[
\frac{C_{\rm same}}{W^2}
=\sum_\sigma\frac{\beta_\sigma^2}{S_\sigma}
=\left(\sum_\sigma\beta_\sigma^2\right)
 \left(\sum_\sigma\frac{\lambda_\sigma}{S_\sigma}\right),
\]
proving (1)--(2). Each \(S_\sigma\in[1,p]\), so
\(1\le S_{\rm state\text{-}phase}\le p\).

Write
\[
E_{\rm pair-phase}=\sum_{u,t}b_u(t)^2,\qquad
R_*=\frac{W^2}{E_{\rm pair-phase}}
=R_{\rm pair}S_{\rm phase}
\]
as in \`MC-512\`. If each exact state has at most \(L\) source pairs, positivity and Cauchy on each state fibre imply
\[
E_{\rm pair-phase}\le C_{\rm same}\le L E_{\rm pair-phase}.
\]
Hence
\[
\boxed{\frac{R_*}{L}\le R_{\rm same}\le R_*},\qquad
\boxed{1\le A_{\rm same}:=\frac{C_{\rm same}}{E_{\rm pair-phase}}\le L},\qquad
R_{\rm same}=\frac{R_*}{A_{\rm same}}.\tag{3}
\]
The previous sufficient gate \(R_*\ge pL\) implies \(R_{\rm same}\ge p\), but it need not be necessary. The loss is exactly the *actual within-state overlap amplification* \(A_{\rm same}\), which may be much smaller than the crude maximum multiplicity \(L\).

From \`MC-506\` let \(\Delta=pC/W^2-1\ge0\). The exact decomposition yields
\[
\boxed{
\frac{pC_{\rm cross}}{W^2}
=1+\Delta-\frac p{R_{\rm same}}.
}\tag{4}
\]
In particular \(R_{\rm same}\ge p\) forces
\(C_{\rm cross}\ge\Delta W^2/p\). A centered quadratic conductor bias
\(|\mathcal C_F|/W\ge\eta\) implies
\(\Delta\ge\eta^2/\sigma_F^2\) by \`MC-506\`; hence in this regime
\[
\frac{pC_{\rm cross}}{W^2}\ge\frac{\eta^2}{\sigma_F^2}.
\tag{5}
\]
This is a **necessary cross-state carrier condition**, not a bound on cross-state collisions or a sufficient condition for bias.

## Sharp controls

**Maximum-fibre slack is real.** For any prime \(p\), take one relative state containing \(L=p\) labelled pairs, one pair at each distinct phase \(t\), each with mass \(1/p\). Then \(W=1\), \(C_{\rm same}=E_{\rm pair-phase}=1/p\), \(R_*=R_{\rm same}=p\), and \(A_{\rm same}=1\). The exact normalized tariff is \(1\), while \`MC-511\`'s \(pL/R_*=p\) overestimates it by a factor \(p\). Conversely, if \(L\) equal-weight pairs of one state sit on one phase, \(A_{\rm same}=L\), proving the upper extreme of (3).

**Cross-state excess survives the exact gate.** Take \(p\) distinct states, each with one pair carrying mass \(1/p\) on the *same* phase \(t_0\). Then \(R_{\rm same}=p\), \(C_{\rm same}=1/p\), but \(C=1\), \(\Delta=p-1\), and (4) gives \(pC_{\rm cross}=p-1\). Thus vanishing or baseline-sized same-state collisions alone do not control the physical pushforward: distinct states may still concentrate maximally.

These are abstract nonnegative source-table controls, **not** asserted constructions of the actual prime first-exit source.

## Prior art and novelty audit

Inverse-Simpson/order-two Hill effective numbers, conditional collision probabilities and their squared-mass weighting are classical. \`MC-S57\` (Hill 1973), \`MC-S58\` (Jost 2006), and \`MC-S59\` (Jost 2007, on diversity partitioning) are the closest diversity-language anchors. No novelty is claimed for the abstract harmonic factorization or for a general entropy chain rule. The source-specific delta is its use *after grouping by the exact \(\Lambda_z\) state*, replacing the maximum-fibre inequality in \`MC-511\` by the exact physical same-state collision certificate, and exposing precisely the gap \(A_{\rm same}\).

## Boundaries and decisive test

- All quantities require **actual** nonnegative \(b_u(t)\) and recoverable source-pair/state provenance. No independence, completed source, uniform surrogate or random model is imported.
- There is no independent source estimate for \(R_{\rm state}\) or \(S_{\rm state\text{-}phase}\). Their exact factorization is not an improvement over \`MC-511\` unless the localized prime source supplies a usable lower bound.
- The conditional state laws need not be uniform. State support cardinality without collision-weight control is insufficient.
- The kernel sees \(c_t=\sum_\sigma c_{\sigma,t}\), not the state labels. Even \(R_{\rm same}\gg p\) does not prohibit large \(\Delta\) produced by different-state phase alignment.
- Signed or complex pre-aggregation coefficients require a different argument; the probability interpretation here is only for the present nonnegative branch.
- This remains conductor-local, with no bound on \(M(x)\), no zero-free result, and no implication of RH.

**Decisive source audit:** measure or bound \(R_{\rm state}\) and its squared-mass-weighted \(S_{\rm state\text{-}phase}\) for the *physical* localized first-exit coefficients. If their product exceeds \(p\), (2) excludes same-state excess without paying \(L_z\). Any surviving excess must be tested in the cross-state pushforward (4), including signed alignment with the centered conductor kernel. Do not claim a theorem about Möbius cancellation from the abstract controls alone.
