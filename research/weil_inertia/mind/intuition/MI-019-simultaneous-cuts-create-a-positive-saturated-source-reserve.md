# MI-019 — Simultaneous cuts turn firstness into a positive saturated source reserve

**Evidence level:** exact at a hypothetical attained first unrestricted Suzuki crossing through [WI-274](../../findings/WI-274-simultaneous-cuts-create-a-positive-saturated-source-reserve.md). The main saturated reserve is sign-independent. The prime-overlap corollary remains conditional on a one-signed null mode and is not yet numerically contradictory.

Single-cut localization prices each cut separately and, on the one-signed branch, runs into the sharp Carleman wall as an internal gap shrinks. WI-274 changes the order of operations: impose the firstness inequalities for **all** sharp cuts and integrate the cut family before estimating the source.

For a real normalized first null mode `v`, each cut `t` gives complementary left/right lower bounds on the same cut energy `Q_t`. A source pair at lag `h` crosses exactly a set of cuts of length `h`, so Fubini gives the exact identity

`integral J_t(h) dt = h C_v(h)`.

The lag factor regularizes the short-range archimedean singularity automatically. Integrating the two firstness bounds and using monotonicity of the lower eigenvalue curve yields the saturated source functional

`S_v >= 2 integral_(a/2)^a lambda_r dr > 0`.

This is stronger than sending a single localization radius to the first crossing, where the pointwise lower bound can collapse. **The whole cut family stores the accumulated positivity of the interior spectral curve even though the endpoint eigenvalue is zero.**

On a one-signed branch, `0<=C_v(h)<=1`. The positive archimedean contribution then has a finite exact budget `K_+`, so the weighted prime overlap obeys

`P_v >= 2 integral_(a/2)^a lambda_r dr - K_+`.

Complete prime screening is therefore possible only if the spectral area is at most `K_+/2`. This does not yet prove that the inequality fails, but it replaces the zero-gap operator-norm wall by a source-specific scalar comparison between an **integrated firstness reserve** and a finite archimedean budget.

For sign-changing modes the reserve remains valid, but prime and archimedean pieces can still cancel inside `S_v`; the one-signed overlap inequality cannot simply be imported.

**Research consequence.** The one-signed narrow-gap route should now quantify `integral_(a/2)^a lambda_r dr` or strengthen the integrated cut inequality using local null-mode structure. The sign-changing route should ask how the PSD/nodal family constrains cancellation inside the already-positive total reserve. Another refinement of a single-cut global Hankel norm is no longer the natural next step.

**Boundary.** WI-274 does not prove fixed sign, nonzero prime overlap on the sign-changing branch, or RH. It proves that simultaneous localization carries strictly more firstness information than the degenerating endpoint cut.
