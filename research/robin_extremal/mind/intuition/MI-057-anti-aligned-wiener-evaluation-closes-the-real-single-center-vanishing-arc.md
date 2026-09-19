# MI-057 — Anti-aligned Wiener evaluation closes the real single-center vanishing arc

**Evidence level:** exact synthesis from `RE-221`--`RE-226`.

The last fixed-corridor positive-real single-center escape after RE-225 was a shrinking observed arc. Interior parameter regimes already pay Wiener rate strictly above two, truncation collapse and center escape are excluded, and contraction degeneration can occur only while the arc itself tends to zero.

RE-226 shows that the shrinking observation window does not make the coefficient vector cheap. The same polynomial is defined on the whole unit circle. At the anti-aligned point `z=-1`, a positive real expansion center makes every factor reinforce rather than cancel, while contraction bounds the real normalization denominator. For `a<=A`,

`||F_(m,N,a)||_A >= |F_(m,N,a)(-1)| >= e^(-1)(1+1/(2A))^N`.

Therefore, if `N/m` stays bounded below, `alpha_m->0`, and `m alpha_m->infinity`, then

`log ||F_m||_A /(m alpha_m) -> +infinity`.

The useful geometric lesson is that **local prediction accuracy and global coefficient cost can be separated by evaluating the same representation in an anti-aligned direction outside the observed set**. Exact cancellation on a shrinking arc cannot hide a direction where the basis functions become sign-coherent. Before developing a delicate boundary asymptotic, test whether the norm controlling the destination already dominates such an external evaluation functional.

For the Robin predictor this closes the positive-real single-center architecture family-by-family. Any route toward the global separated-prediction floor must change the geometry enough to defeat the anti-aligned probe—through complex centers, multiple centers, or a different basis—rather than tune another degeneration of the same representation.

**Boundary.** This is not a universal lower bound `C_sep>1`. It uses a positive real single center, bounded center on the relevant corridor, a positive truncation density, and the Wiener norm of that polynomial representation. Complex-center or multi-center recombination can destroy the sign coherence at `z=-1`; those cases remain open. No RH consequence follows directly.
