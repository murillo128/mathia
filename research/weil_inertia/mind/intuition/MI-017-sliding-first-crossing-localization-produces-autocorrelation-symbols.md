# MI-017 — Sliding first-crossing localization becomes a phase-coupled source cone, but prime activation first needs finite-scale positivity past `log 2/2`

**Evidence level:** supported by WI-253--WI-259. The phase-cone identities are exact, while the public `FP-0.35` positivity certificate used to cross the first-prime threshold remains computational evidence requiring independent replay; no incompatibility with a compactly supported global first zero mode is proved.

At a hypothetical first unrestricted localized Weil crossing, translation freedom produces an exact sliding-aperture profile whose Fourier representation averages explicit source symbols against the nonnegative density `|vhat|^2`. WI-253--WI-254 show that the full profile is information-complete for the real autocorrelation, but firstness exposes only a lower envelope.

WI-255--WI-257 close generic small-radius and regularity escapes. The first additive correction becomes universal after imposing the zero-mode equation, the next remainder contains a local translation-defect modulus not controlled quadratically by `H^log`, and common-domain bounded-perturbation zero-modehood cannot determine that modulus.

WI-258 supplies a genuinely source-explicit replacement. Phase modulation gives

`M_v(t)=int (1-cos(th)) dmu_v(h) >= 0`,

and the translated-window version gives

`S_v(r)+J_v(r,t) >= 0`,

where `J_v(r,t)` is the triangularly localized cosine transform of the von-Mangoldt/archimedean source-weighted autocorrelation. A negative localized source defect would force strict firstness slack.

WI-259 identifies a prerequisite that was implicit in that program. The first von-Mangoldt atom enters only when `r>(log 2)/2`. Existence of a first crossing alone does not guarantee that any prime atom is active. If one can establish strict finite-scale positivity at

`r=7/20=0.35`,

then monotonicity forces `a_*>7/20`, and since `log 2 < 7/10 < log 3`, the fixed radius `r=7/20` is valid for every hypothetical first crossing and contains **exactly the single prime atom `n=2`**.

That reduction is exact, but its current external input is not yet certified by Mathia. The public `FP-0.35` project reports a corrected positive certificate after fixing a load-bearing interval-construction bug, yet its public theorem/status artifacts are inconsistent and no independent cold replay of the post-fix certificate has been accepted here. The correct evidence boundary is therefore `COMPUTATIONAL-CERTIFICATE + NEEDS-INDEPENDENT-REPLAY`, not theorem.

The live phase program is consequently ordered. First establish or independently replay finite-scale positivity beyond `(log 2)/2`. If the `7/20` gate survives, freeze that radius and attack the exact **one-prime** phase identity before enlarging to multi-prime radii. Even then, prime activation alone is not instability: the first-prime shift is indefinite but can be absorbed locally by the archimedean potential, so the needed theorem must use first-crossing structure plus the coupled source cone.

The reusable lesson is that a source-specific inequality can still be unavailable because the relevant source atom has not been proved to lie inside the admissible localization radius. **Source activation is a separate gate from source sign.**

**Boundary.** WI-259 does not prove `lambda_(7/20)>0`, a negative phase defect, or RH. If the external certificate fails, the exact conditional implication remains valid but the prime-coupled first-crossing argument must return to the prime-free regime until another positivity theorem crosses the threshold.