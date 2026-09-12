# MI-017 — Sliding first-crossing localization is useful only beyond envelope loss, null-equation redundancy, and generic regularity

**Evidence level:** supported by WI-253--WI-256; no incompatibility with a compactly supported global first zero mode is proved.

At a hypothetical first unrestricted localized Weil crossing, translation freedom produces an exact sliding-aperture profile whose Fourier representation averages explicit source symbols against the nonnegative density `|vhat|^2`. WI-253--WI-254 show that the full profile is information-complete for the real autocorrelation: prime-power shifts appear as slope changes and the continuous archimedean part can be reconstructed between thresholds.

Firstness does not expose all of that information. It gives only a pointwise lower envelope, and the small-aperture leading term is asymptotically saturated. WI-255 shows that the first additive correction is also unusable: before the zero-mode equation it contains source-sensitive prime and archimedean terms, but `Q_W(v)=0` cancels them exactly. The surviving linear coefficient is universal.

WI-256 shows that simply going to the next Taylor coefficient is not legitimate. The exact remainder contains a universal `7 r^2/2` term plus a nonnegative local translation-defect modulus `E_v(r)`. The known logarithmic form regularity controls only an integral of `(1-C(h))/h`; it does not force `E_v(r)` to be quadratic. Generic operator-domain membership also fails to determine the coefficient: admissible vectors can have different second-order translation behavior.

The missing resource is therefore **zero-mode-specific regularity**, not more formal expansion. A small-radius bootstrap must derive an estimate or asymptotic for `E_v(r)` from the full equation `A_(a*)v=0`. Otherwise the useful information must come from medium-radius threshold coupling or another operator identity not reducible to the scalar null value.

The reusable lesson is that a representation may retain source information while the proof pipeline loses access to it through three distinct mechanisms: envelope replacement, algebraic redundancy, and insufficient regularity for the desired asymptotic readout.

**Boundary.** WI-256 closes only a generic second-order continuation. It does not show that the actual zero mode has poor regularity, that all higher-order terms are universal, or that medium-radius relations are redundant.