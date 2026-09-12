# MI-017 — Sliding first-crossing localization is useful only beyond envelope loss, null-equation redundancy, and generic bounded-perturbation regularity

**Evidence level:** supported by WI-253--WI-257; no incompatibility with a compactly supported global first zero mode is proved.

At a hypothetical first unrestricted localized Weil crossing, translation freedom produces an exact sliding-aperture profile whose Fourier representation averages explicit source symbols against the nonnegative density `|vhat|^2`. WI-253--WI-254 show that the full profile is information-complete for the real autocorrelation: prime-power shifts appear as slope changes and the continuous archimedean part can be reconstructed between thresholds.

Firstness does not expose all of that information. It gives only a pointwise lower envelope, and the small-aperture leading term is asymptotically saturated. WI-255 shows that the first additive correction is also unusable: before the zero-mode equation it contains source-sensitive prime and archimedean terms, but `Q_W(v)=0` cancels them exactly. The surviving linear coefficient is universal.

WI-256 shows that simply going to the next Taylor coefficient is not legitimate. The exact remainder contains a universal `7r^2/2` term plus a nonnegative local translation-defect modulus `E_v(r)`. The known logarithmic form regularity controls only an integral of `(1-C(h))/h`; it does not force `E_v(r)` to be quadratic, and generic operator-domain membership does not determine its coefficient.

WI-257 closes the next generic escape. After unitary scaling to `(-1,1)`, Suzuki's localized Weil operator has the form

`T_a = T_0 + K_a`,

where `T_0` is one fixed logarithmic self-adjoint operator and `K_a` is bounded self-adjoint. Hence every scaled operator has the same domain `D(T_0)`. More strongly, every normalized `u in D(T_0)` can be made a zero mode of **some** bounded rank-at-most-two self-adjoint perturbation. The common domain contains a constant with `E(r)=r^2/2` and smooth compactly supported vectors with `E(r)=O(r^3)`. Therefore bounded-perturbation zero-modehood, by itself, cannot determine even the quadratic translation coefficient.

The missing resource is no longer merely “use the zero-mode equation.” A successful small-radius argument must use the **specific arithmetic structure of `K_(a*)`**: the von-Mangoldt weighted translations, their prime-power thresholds, the fixed archimedean kernel, or a relation among several apertures that is false for arbitrary bounded perturbations. Otherwise the useful information must come from medium-radius threshold coupling or another operator identity not reducible to the scalar null value.

The reusable lesson is that a representation may retain source information while the proof pipeline loses access to it through four distinct mechanisms: envelope replacement, algebraic redundancy, insufficient regularity, and abstraction of a source-specific perturbation into an arbitrary bounded operator.

**Boundary.** WI-257 does not show that Suzuki's actual zero mode has poor regularity or that source-specific threshold identities cannot control `E_v`. It rules out only conclusions obtainable from the common domain plus generic bounded self-adjoint zero-mode structure.