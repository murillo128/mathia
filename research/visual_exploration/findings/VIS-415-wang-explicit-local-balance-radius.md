# VIS-415 — Wang cycle holonomy has an explicit local balance radius

## Claim

Keep a finite labelled family of real Wang shell functions from `VIS-413`,

`F_i(T)=sum_(lambda in Lambda_i) B_(i,lambda) exp(-i lambda T)`,

with the conjugate symmetry that makes each `F_i` real on the real axis. For each shell define the global derivative budget

`L_i = sum_(lambda in Lambda_i) |lambda B_(i,lambda)|`.

Then `|F_i'(T)| <= L_i` for every real `T`.

Fix a height `T_0` with `F_i(T_0) != 0` for every selected shell. For every shell with `L_i>0`, put

`rho_i(T_0)=|F_i(T_0)|/L_i`,

and set `rho_i(T_0)=+infinity` when `L_i=0`. Define the finite-family balance radius

`rho_*(T_0)=min_i rho_i(T_0)`.

For every `0<r<rho_*(T_0)` and every nonzero nonnegative window `w` supported in `[T_0-r,T_0+r]`, all selected shells are sign-definite on the window support. Therefore the weighted Gram signing from `VIS-414` is balanced and every nonzero Bargmann cycle product is positive.

Conversely, if a nonzero weighted cycle on a centered interval window of radius `r` is negative, then some shell `i` on that cycle satisfies

`|F_i(T_0)| <= r L_i`.

Thus a negative `Z_2` Wang cycle cannot appear below the explicit pointwise margin-to-slope scale `rho_*(T_0)`. The local-triviality statement in `VIS-414` is therefore quantitative: the first possible nontrivial cycle scale is controlled by how close at least one participating shell is to a zero relative to its available frequency-weighted slope budget.

**Evidence/status:** `EXACT-DERIVED + ELEMENTARY-LIPSCHITZ SPECIALIZATION + NEGATIVE REPRESENTATION BOUNDARY + NO-NOVELTY-CLAIM`.

This is a sufficient local-balance radius, not an exact zero distance in general. The derivative triangle bound can be very loose when shell-frequency terms cancel.

## 1. Exact derivative budget

Differentiate the finite exponential sum term by term:

`F_i'(T) = -i sum_(lambda in Lambda_i) lambda B_(i,lambda) exp(-i lambda T)`.

Hence the triangle inequality gives

`|F_i'(T)| <= sum_(lambda in Lambda_i) |lambda B_(i,lambda)| = L_i`.

No asymptotic estimate or spacing input is used. The bound depends only on the finite shell frequencies and coefficients already present in the Wang representation.

If `L_i=0`, every nonzero-frequency coefficient vanishes and the shell is constant in `T`; because `F_i(T_0) != 0`, it is sign-definite on every interval, so assigning `rho_i=+infinity` is natural.

## 2. Margin-to-slope control forces sign stability

For `|T-T_0|<=r`, the mean-value estimate gives

`|F_i(T)-F_i(T_0)| <= L_i |T-T_0| <= L_i r`.

If `r<rho_i(T_0)`, then

`L_i r < |F_i(T_0)|`.

Therefore `F_i(T)` cannot reach zero anywhere in the interval and must keep the sign of `F_i(T_0)` throughout it. If `r<rho_*(T_0)`, this holds simultaneously for the full selected family.

`VIS-414` then applies directly: after switching each shell by its fixed sign, every weighted Gram entry is nonnegative, so every nonzero closed-cycle product is positive.

The argument is independent of the detailed shape of `w`; only nonnegativity and support inside the certified interval matter.

## 3. Negative cycles certify a failed margin inequality

Suppose a centered interval window of radius `r` has a nonzero negative cycle product. By `VIS-414`, at least one shell on that cycle is not sign-definite on the interval. Because the shell is continuous and real, it has a zero `T_z` with

`|T_z-T_0|<=r`.

Using the same derivative bound between `T_0` and `T_z`,

`|F_i(T_0)| = |F_i(T_0)-F_i(T_z)| <= L_i |T_0-T_z| <= r L_i`.

Hence negative cycle incidence has a necessary local condition: at least one participating shell must lie within its frequency-weighted Lipschitz margin of a zero.

This is stronger than the qualitative zero-crossing witness in `VIS-414`, but it is still only necessary. A failed margin inequality or a shell zero does not force a negative cycle, because several edge signs may change coherently and leave all cycle parities positive.

## 4. A sharper local version and its limitation

The global coefficient budget `L_i` is convenient because it is explicit before choosing a window. For a specific interval `I`, one can replace it by the exact local derivative norm

`L_i(I)=sup_(T in I) |F_i'(T)|`.

Then the same proof gives the sharper condition

`r < |F_i(T_0)|/L_i(I)`

for a centered interval of radius `r` contained in `I`.

This does not solve the growing-family problem. If the retained shell family expands, either the smallest pointwise amplitude may approach zero or the largest derivative budget may grow, so `rho_*(T_0)` may collapse. Establishing a scale-uniform positive radius would require new information about simultaneous shell zero avoidance and coefficient-frequency growth.

## 5. Representation consequence

The finite-window Wang cycle ladder now has a quantitative local obstruction:

- `VIS-412`: intrinsic Bohr cross-shell Gram edges vanish;
- `VIS-413`: finite real windows can restore edges but quantize cycle phase to `Z_2`;
- `VIS-414`: sign-definite windows force the `Z_2` sector to be trivial;
- this finding: sign-definiteness is guaranteed below an explicit margin-to-slope radius.

So an observed negative-cycle event is not merely evidence that the window spans some shell zero. It also identifies a scale at which at least one shell amplitude has become small relative to its available frequency-weighted slope budget.

That suggests a more intrinsic mesoscopic statistic than raw cycle sign: study the distribution, across height and shell families, of normalized margins such as

`m_i(T)=|F_i(T)|/L_i`

and compare the first negative-cycle scale with the lower envelope of those margins. Any arithmetic claim would still need matched controls that preserve coarse frequency support and coefficient norms while removing the specific Wang source organization.

## 6. Prior art and novelty boundary

The analytical estimate is the elementary Lipschitz/mean-value bound for a finite trigonometric polynomial. No novelty is claimed for derivative triangle inequalities, zero-exclusion by a Lipschitz margin, or structural balance of signed graphs.

`VIS-414` already records Harary's classical structural-balance theorem and proves its specialization to sign-definite Wang shell windows. The present Mathia-specific contribution is only the explicit insertion of the Wang shell frequency/coefficient data into that local sign-stability boundary.

No new theorem about zero spacing, trigonometric-polynomial extremality, Wang's original arithmetic estimates, or RH is claimed.

## 7. Boundaries and falsification

The result uses a **finite** selected shell family. It gives no uniform lower bound when the number or scale of shells tends to infinity.

The window remains real and nonnegative, exactly as in `VIS-413`--`VIS-414`. Signed or complex kernels fall outside the balance argument.

The coefficient budget `L_i` is representation-specific. Rescaling a shell by a nonzero constant scales both `|F_i(T_0)|` and `L_i` by the same factor, so `rho_i` is invariant under shell amplitude normalization and sign flips, but a genuinely different packetization can change it.

To falsify the main statement it would be enough to exhibit a selected shell and radius `r<|F_i(T_0)|/L_i` for which the shell vanishes inside `[T_0-r,T_0+r]`, or a family satisfying all displayed margin inequalities whose nonnegative-window Gram graph contains a negative nonzero cycle. Either would contradict the mean-value or switching argument directly.

## Dependencies

- `VIS-413`: the canonical Wang finite-window shell functions are real and their Bargmann phases lie in `Z_2`.
- `VIS-414`: simultaneous sign-definiteness makes every nonzero cycle positive and a negative cycle witnesses a shell sign transition.

## Research consequence

The next independent question is the **scaling law of `rho_*(T)` for growing Wang shell families**. A useful positive result would have to show that the lower envelope of shell margins behaves differently for the arithmetic Wang source than for controls matched in shell frequencies, coefficient energies, and one-shell zero-crossing density. That requires a new visual/control experiment and is intentionally left for a later invocation.
