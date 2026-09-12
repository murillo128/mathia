# MI-017 — Sliding first-crossing localization is information-complete only beyond the firstness envelope and null-equation redundancy

**Evidence level:** supported by the exact sliding-window identity WI-253, profile inversion/saturation theorem WI-254, and the universal first subleading cancellation WI-255; no incompatibility with a compactly supported global first zero mode is proved.

At the first unrestricted localized Weil crossing `a_*`, translation freedom produces for a normalized zero mode `v` an aperture profile

\[
\mathcal F_v(r)
=
\frac1{2\pi}\int\Sigma_r(z)|\widehat v(z)|^2\,dz
\ge r\lambda_r>0.
\]

WI-253--WI-254 show that the **exact** profile is information-complete for the real autocorrelation. Prime-power shifts appear as exact slope jumps and the continuous archimedean part is recovered between thresholds by distributional differentiation. The obstruction is not aperture information loss; it is that firstness supplies only a pointwise lower envelope for this profile.

At small aperture the envelope is saturated at leading order,

\[
\mathcal F_v(r)\sim r\log(1/r)
\sim r\lambda_r,
\]

so there is no fixed multiplicative reserve.

WI-255 shows that the first additive correction is also unusable for a deeper reason. The exact expansion is

\[
\mathcal F_v(r)
=
r\log(1/r)
+r\bigl(\psi(2)-\log(4\pi)\bigr)
+o(r).
\]

During the derivation the coefficient initially contains the prime autocorrelations and regular archimedean response. But on an actual zero mode the scalar identity `Q_W(v)=0` cancels all of those source-sensitive terms exactly. After comparison with the small-window ground state, firstness yields only the already-known variational inequality

\[
\mu_1\le1-\log2.
\]

This reveals a second information-loss step: **a source-sensitive coefficient can be present in an exact representation yet become algebraically redundant once the defining null equation is imposed**. Reading more precision from the same scalar equation does not necessarily expose new arithmetic content.

The live route must therefore escape both losses. It needs a higher-order invariant not fixed by `Q_W(v)=0`, an operator/eigen-equation identity independent of its scalar quadratic-form value, or medium-radius relations that compare several prime thresholds before they collapse into one integrated null condition.

**Boundary.** WI-255 closes only the complete `O(r)` refinement. It does not show that all higher-order terms are universal, that the exact profile is source-independent, or that medium-radius threshold relations are redundant. Additional regularity may be required before a higher-order expansion is even defined.
