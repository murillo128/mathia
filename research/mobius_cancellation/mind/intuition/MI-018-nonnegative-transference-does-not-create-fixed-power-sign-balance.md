# MI-018 — Subpower transference or variance does not create fixed-power sign balance

**Evidence level:** supported by the first-shell scale reduction MC-232--MC-235, the exact/published-resolution audit in MC-236, and the smooth-modulus variance specialization MC-237; these are limitations of the audited theorem surfaces, not impossibility theorems for Möbius cancellation itself.

The hard first-shell coordinates require a **signed** progression estimate. For a fixed interior pair

\[
q=X^{2\alpha+o(1)},\qquad Z=X^{1-\beta+o(1)},\qquad
\delta=\frac12-2\alpha-\beta>0,
\]

the required relative sign bias is `X^{-\delta+o(1)}`, equivalently a fixed negative power of `q`.

MC-235 shows that this is not a support problem: the Linnik machinery already supplies essentially full-exponent populations of both Möbius signs in the selected progression. MC-236 isolates the first information loss. The sign-specific dense models preserve the principal signed mean exactly, so modeling transports whatever bias was already present rather than damping it. The later threshold/product-set argument converts the models into one-sided coverage information, and transferring the two signs separately has only `q^{-o(1)}` relative precision where subtraction needs `q^{-c}`.

MC-237 shows that moving to a genuinely signed second-moment theorem on the **exact smooth CRT modulus** does not repair the power mismatch. The deep modulus `Q_S` satisfies the hypotheses of the Klurman--Mangerel--Teräväinen individual smooth-modulus variance theorem, but after Möbius specialization its residual RMS is only

\[
\sqrt\varepsilon\,\frac Zq
=X^{1-\beta-2\alpha+o(1)}.
\]

The theorem therefore improves trivial progression occupancy only by `X^{-o(1)}`. The first-shell target asks for the fixed factor `X^{-\delta}`. At exponent resolution the variance estimate reaches `X^{1/2}` only on `2\alpha+\beta\ge1/2`, exactly the region already closed by support. This remains true even if one grants favorable control of the distinguished-character main term.

The selected-residue issue is secondary here: the RMS scale itself is already too large. Markov at threshold `X^{1/2}` is vacuous in the strict hard region, so averaging over residues cannot certify the source-selected residue from this second moment alone.

The reusable lesson is broader than “nonnegative arguments lose signs”: **a downstream fixed-power difference cannot be recovered from inputs whose relative accuracy is only subpower, even when those inputs are genuinely signed and perfectly adapted to the modulus family**. Support, separate sign abundance, smoothness, applicability of a variance theorem, and small logarithmic/subpower relative error are all weaker currencies than the fixed-power signed amplitude demanded here.

A viable continuation must expose a signed comparative invariant with relative accuracy tracking `\delta`, exploit correlations that make the source-selected residue atypically better than the RMS scale, or obtain cancellation only after recombining the smooth-dilation family so that separate component errors are not summed by triangle inequality.

**Boundary.** MC-236 does not rule out a stronger signed use of dense modeling, and MC-237 does not rule out additional structure inside the smooth-modulus theorem or a stronger source-coupled theorem. It only closes the inference from the currently available one-sided/subpower transference and scalar variance estimates to the fixed-power first-shell target.