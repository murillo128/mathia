# MI-017 — Sliding first-crossing localization becomes a phase-coupled source cone after generic regularity fails

**Evidence level:** supported by WI-253--WI-258; no incompatibility with a compactly supported global first zero mode is proved.

At a hypothetical first unrestricted localized Weil crossing, translation freedom produces an exact sliding-aperture profile whose Fourier representation averages explicit source symbols against the nonnegative density `|vhat|^2`. WI-253--WI-254 show that the full profile is information-complete for the real autocorrelation: prime-power shifts appear as slope changes and the continuous archimedean part can be reconstructed between thresholds.

Firstness does not expose all of that information. It gives only a pointwise lower envelope, and the small-aperture leading term is asymptotically saturated. WI-255 shows that the first additive correction is also unusable: before the zero-mode equation it contains source-sensitive prime and archimedean terms, but `Q_W(v)=0` cancels them exactly. The surviving linear coefficient is universal.

WI-256 shows that simply going to the next Taylor coefficient is not legitimate. The exact remainder contains a universal `7r^2/2` term plus a nonnegative local translation-defect modulus `E_v(r)`. The known logarithmic form regularity controls only an integral of `(1-C(h))/h`; it does not force `E_v(r)` to be quadratic, and generic operator-domain membership does not determine its coefficient.

WI-257 closes the generic regularity escape. After unitary scaling to `(-1,1)`, Suzuki's localized Weil operator has the form `T_a=T_0+K_a`, where `T_0` is one fixed logarithmic self-adjoint operator and `K_a` is bounded self-adjoint. Every normalized `u in D(T_0)` can be made a zero mode of some bounded rank-at-most-two self-adjoint perturbation, while vectors in that domain realize incompatible quadratic behavior of `E(r)`. Generic bounded-perturbation zero-modehood therefore cannot determine the needed translation modulus.

WI-258 supplies a different exact variational family that uses the actual source decomposition. For the first-crossing null mode and its source-weighted autocorrelation measure `mu_v`, phase modulation `v_t(x)=e^{itx}v(x)` preserves support and gives

`M_v(t)=int_0^(2a*) (1-cos(th)) dmu_v(h) >= 0`.

Combining the same modulation with translated-window localization gives

`S_v(r)+J_v(r,t) >= 0`,

with `S_v(r)=F_v(r)-r lambda_r` and

`J_v(r,t)=int_0^(2r) (2r-h)(1-cos(th)) dmu_v(h)`.

Hence a negative localized cosine defect `J_v(r,t)<=-epsilon` cannot be hidden by the scalar aperture lower envelope: it forces at least `epsilon` of strict firstness slack. In the explicit source expansion, each prime-power atom enters only after `2r>log n` and then carries the triangular phase weight `(2r-log n)(1-cos(t log n))`. Frequency can therefore suppress or emphasize source shifts without enlarging spatial support.

This phase cone is genuinely additional to scalar `min`-transform positivity as an inequality constraint, but it is not yet a contradiction. Analogous modulation inequalities exist for generic translation-invariant nonnegative forms, and the exact aperture profile already determines `mu_v` distributionally. The missing theorem is specifically a **zeta-source sign theorem**: the von-Mangoldt atoms, archimedean density, compact support and positive-definiteness of `C_v` must force `inf_t J_v(r,t)<0` for some medium radius, or else a source-compatible autocorrelation model must demonstrate that all scalar and phase inequalities can coexist.

The reusable lesson is that source information can survive the scalar envelope and generic-regularity barriers only if one introduces a variational family whose weights couple directly to the arithmetic source. Here phase modulation provides such weights, and the remaining difficulty is no longer abstract smoothness but the sign geometry of a concrete two-parameter source transform.

**Boundary.** WI-258 does not prove a negative phase defect, an RH contradiction, or a regularity improvement. The pure logarithmic core and generic bounded-perturbation controls remain valid falsifiers for arguments using modulation abstractly. Any gain must come from the explicit zeta factorization of `mu_v` together with compact-support/autocorrelation constraints.