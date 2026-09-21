# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Separate full exact-omission reachability from the linear-density and source-admissibility boundaries

**Linked intuitions:** `MI-041-sublinear-point-sampling-cannot-make-divisor-response-signed-coercive`, `MI-042-subfull-point-sampling-density-cannot-make-divisor-response-signed-coercive`, `MI-043-approximate-density-one-sampling-has-a-defect-plus-residual-coercivity-ledger`, `MI-044-finite-exact-omissions-are-triangular-response-columns-not-arbitrary-sparse-increments`, `MI-045-exact-omission-cost-is-a-harmonic-location-profile`, `MI-046-cross-scale-divisibility-not-low-location-drives-exact-omission-amplification`, `MI-047-alternating-rank-merges-create-factorial-incidence-conditioning-without-reaching-the-macroscopic-scale`, `MI-048-ordered-factorization-entropy-caps-exact-omission-conditioning`, `MI-049-parity-dilation-moves-the-exact-omission-frontier-from-support-to-paired-coefficients`, `MI-050-companion-incidence-not-full-support-incidence-controls-isolated-paired-omissions`, `MI-051-congruence-restricted-companion-chains-lower-the-ordered-factorization-conditioning-exponent`, `MI-052-restricted-inverse-conditioning-counts-only-after-global-extension`.

FD-241--FD-247 separate qualitative density-one sampling, approximate residual cost, triangular exact omission columns, harmonic support reach and the primitive-support regime. FD-248 identifies the support-side conditioning statistic `kappa(D)` for a freely prescribed active increment support.

FD-249--FD-251 show that restricted divisor-incidence matrices can be badly conditioned but obey an ordered-factorization ceiling. FD-252 shows that the exact-omission support shape `D subset E union (E+1)` does not by itself improve that ceiling. FD-253--FD-254 then incorporate the paired image: isolated omissions are controlled first by companion divisibility geometry, and fixed dilations `E=LD` have a thinner congruence-restricted chain exponent `rho_L-1`.

FD-255 closes the remaining polynomial-amplification question at the **full coefficient** level. The missing constraints are the global Möbius rows. If `g=mu*b=Delta Y`, `D=supp(g)`, `|b_n|<=C_b n`, and `Y` vanishes outside `K` omitted locations, then `|D|<=2K` and

`|g(d)|/d <= C_b sigma_{-1}(d)`.

Using the FD-244 sparse reciprocal-divisor estimate gives, for `eta=min(1,2K/H)` and `Phi(eta)=eta log(e+log(1/eta))`,

`sum_(d in D) |g(d)|/d << C_b H Phi(eta)`,

`sum_(n<=H) |b_n| << C_b H^2 Phi(eta)`.

Hence every exact-omission family with `K=o(H)` has vanishing normalized coefficient mass at the macroscopic `H^2` scale. In particular, every polynomial regime `K=H^(alpha+o(1))` with `alpha<1` is response-side coercive. Polynomial active-support or companion inverse norms remain valid properties of those restricted matrices, but their extremizing row data are not globally extendable under the coefficient envelope.

The live exact-zero response question has therefore moved to the **linear-density boundary** `K=Theta(H)` and to sharpness inside the fully extendable image. If macroscopic hidden coefficient mass exists there, it must satisfy the global Möbius row constraints rather than merely saturate a restricted incidence inverse. Separately, one can ask whether the sparse double-log ceiling is quantitatively sharp below linear density, but improving that factor does not reopen the already closed macroscopic sublinear branch.

The independent source-side question remains whether positivity, finite reservoir capacity, squarefree realization or arithmetic coherence further restrict the signed directions that survive the full response map. Approximate residual control remains separate from exact-zero incidence.

## Separate support conditioning, paired reachability, global extension and source admissibility

Response-space rounding makes bulk integrality cheap once a real reservoir profile is safely inside its capacity box. The remaining discrete obstruction is source admissibility and exact defect geometry.

The exact hierarchy now has four distinct layers. `kappa(D)` prices free coordinates on an active support; the omission map restricts those coordinates to paired/telescoping amplitudes; the global identities `g=mu*b` and `b=1*g` require those restricted data to extend through every divisor coefficient row under the envelope; and only then does physical source admissibility impose positivity and arithmetic realization. FD-255 shows that the third layer can collapse polynomial conditioning visible in the first two all the way to a sparse double-log reachable scale. A large support or companion inverse norm is therefore not evidence of a large exact-omission response unless its extremizer extends through the full coefficient system.