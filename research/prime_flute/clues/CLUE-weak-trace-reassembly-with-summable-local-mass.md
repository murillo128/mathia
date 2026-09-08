---
id: CLUE-prime-flute-weak-trace-reassembly-with-summable-local-mass
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-112-first-relative-resolvent-is-not-trace-class.md
  - research/prime_flute/findings/PF-183-disjoint-thick-collar-slabs-remove-multiplicity-from-schatten-splice-budget.md
  - research/prime_flute/findings/PF-204-native-two-hilbert-factorization-removes-rough-resolvent.md
  - research/prime_flute/findings/PF-212-thin-fermi-boundary-frequency-split-closes-local-high-mode-gate.md
  - research/prime_flute/findings/PF-220-coefficient-adjacent-low-recoupling-is-weak-trace-without-schur-locality.md
  - research/prime_flute/findings/PF-221-coefficient-weight-transfer-reduces-to-a-reciprocal-prime-schur-commutator.md
  - research/prime_flute/findings/PF-222-reciprocal-prime-schur-commutator-is-compact-by-one-seam-decoupling.md
  - research/prime_flute/findings/PF-223-qualitative-cut-smoothing-does-not-force-weak-trace-schur-transport.md
  - research/prime_flute/findings/PF-225-one-seam-resolvent-dressing-saturates-raw-pant-hopping.md
  - research/prime_flute/findings/PF-226-thin-pants-force-inverse-seam-saturated-channel-multiplicity.md
  - research/prime_flute/findings/PF-227-fixed-physical-high-pass-does-not-remove-thin-pant-channel-multiplicity.md
  - research/prime_flute/findings/PF-228-flat-corridor-dressing-makes-inverse-seam-multiplicity-weak-trace-compatible.md
  - research/prime_flute/findings/PF-229-frozen-serial-schur-completion-preserves-flat-corridor-cut-scale.md
  - research/prime_flute/findings/PF-230-hyperbolic-corridor-has-pi-over-s-axis-inverse-width-budget.md
---

# Can the exact first relative resolvent be completed at the weak-trace endpoint?

## Observation

The first relative resolvent is not trace class by PF-112, while the remaining smooth decomposition-interface term has now been reduced to a much narrower operator. PF-220 closes coefficient-adjacent low sectors. PF-221 moves the physical reciprocal-prime envelope to the low endpoint except for

\[
P[D,\Omega]H
\quad\text{and its adjoint},
\qquad
\Omega=\bigoplus_nP_n^{-1}I_{\mathcal B_n},
\]

and PF-222 gives the exact norm-convergent prefix-flux expansion

\[
P[D,\Omega]H
=
\sum_{j\ge1}
\delta_j P[D,E_j]H,
\qquad
\delta_j=P_j^{-1}-P_{j+1}^{-1}>0.
\]

PF-223 proves that compactness, fixed-cut smoothing, finite-rank approximability, and qualitative low-rank information do not force the weak endpoint. PF-225 then supplies the exact dressed one-cut factorization and universal `1/2` cap, but PF-226 shows that the actual thin pant has order `s_j^{-1}` raw channels above a fixed threshold. PF-227 sharpens this: removing any fixed, or sufficiently slowly growing, physical-frequency sector does not remove that inverse-seam multiplicity. The endpoint therefore cannot be closed by raw channel counting or by declaring the dangerous band low frequency.

PF-228 changes the scale of the positive target. In the exact straight-corridor control, Schur dressing suppresses the inverse-seam band from order-one raw transmission to

\[
\rho_j:=\frac{\sqrt{w_jw_{j+1}}}{s_j},
\]

with the quantitative envelope `rho_j z/sinh(z)` in the scaled tangential frequency `z`. At canonical PF scales this makes the reciprocal-weighted top singular scale at most order `P_j^{-2}` and the orthogonal control family weak trace class even with the full inverse-seam channel population.

PF-229 then removes a second false obstruction. Repeating one frozen PF-228 channel along a complete bi-infinite serial chain changes the isolated transmission by only a fixed factor: the full prefix-to-tail cut block retains the same `w/s` scale and frequency envelope. Thus **generic scalar global shorting is not what remains**. Any destruction of the PF-228 gain must use structure absent from that control: variable hyperbolic pant geometry and tangential mode mixing, noncommuting/inhomogeneous neighboring boundary-energy operators, the physical `P/H` split, or the final overlap of the nested prefix cuts.

PF-230 now makes the first of those missing geometric features exact. The neighboring cuff-axis Fermi graph satisfies

\[
\tanh r_{s_j}(t)=\tanh s_j\,\cosh t,
\]

and after PF-205's natural-width inward offsets the fixed-window core width still has a nonconstant `cosh(t)` leading profile. Thus a constant-width cylinder is not an asymptotically exact geometric perturbation of the real central pant corridor merely because `s_j\to0`. PF-230 also gives the untrimmed axis calibration

\[
\int\frac{dt}{r_{s_j}(t)}=\frac{\pi+o(1)}{s_j},
\]

but explicitly does **not** turn that geometric integral into an operator singular-value upper count for the trimmed interfaces.

The smooth frontier is therefore a two-stage problem: first prove or refute a quantitative **actual-PF dressed cut-flux envelope** at the `w_j/s_j` scale in the variable-profile pant; only after that, solve the genuinely nested weak-`S_1` reassembly. The unsmoothed PF-204 route and the independent PF-183 true-short-collar route remain live alternatives.

## Research question

Can the exact prime/shift first relative resolvent be placed in

\[
\mathcal S_{1,\infty}
\]

while PF-112 continues to exclude `\mathcal S_1`?

For the smooth decomposition-interface route, can the actual operators

\[
P[D,E_j]H
\quad\text{and}\quad
H[D,E_j]P
\]

be given a singular-value/counting envelope comparable to the PF-228/PF-229 dressed scale after PF-230's variable Fermi profile, the PF-205 artificial seam boundaries, tangential mode mixing, neighboring-cell inhomogeneity, and global Schur inversion are retained? A useful target is any estimate with top scale `O(w_j/s_j)` on the inverse-seam band together with quantitative decay beyond that band strong enough to survive multiplication by `\delta_j`.

If such a one-cut estimate holds, can the overlapping nested expansion

\[
\sum_j\delta_jP[D,E_j]H
\]

then be reassembled in weak trace class without replacing the cuts by an artificial orthogonal direct sum? If the one-cut estimate fails, what concrete PF geometric or noncommutative mechanism destroys the favorable dressed scale?

For the competing unsmoothed route, can PF-204's exact native two-Hilbert factorization be placed directly at the critical weak endpoint without differentiating the piecewise cotangent transport? Independently, can the PF-183 true-short-collar normalized slabs be spliced in a coefficient currency sufficient for weak `S_1`?

## Why it may matter

A positive answer would identify weak trace class as the sharp first-resolvent comparison level for the exact prime/shift geometry: PF-112 excludes trace class, while the accumulated sector estimates would place the full comparison at the natural two-dimensional weak endpoint.

The recent cut-flux sequence also makes a negative answer substantially more informative. Raw pant conductance, qualitative compactness, the universal resolvent cap, fixed-frequency truncation, and generic scalar/global shorting have all been separated from the live obstruction. PF-230 additionally prevents treating the real fixed-window pant as a small constant-width geometric perturbation. A failure now has to occur in the actual normalized variable-pant/mode-mixing comparison or in the nested reassembly of quantitatively controlled cuts.

## Decisive test

Start from the exact PF-222 one-seam decoupling identity and retain PF-212's physical low/high split in its actual noncommutative order. Do not return to raw `B_j` trace budgets: PF-225--PF-227 show why those budgets are too crude.

The first gate is **actual one-cut dressing**. Use PF-230's exact variable Fermi profile as the geometric leading object rather than treating the whole central pant window as a constant-width cylinder. Compare the real one-cusp pant boundary problem with a variable-width analogue of PF-228 at the level needed for the dressed cut operator. The comparison must control the features that the frozen model suppresses: tangentially varying thickness, the nontrivial boundary correspondence, the artificial natural-width seam boundaries, mixing between physical frequency sectors, and the fact that neighboring PF cells do not share one Fourier diagonalization. A positive estimate should retain both the `w_j/s_j` inverse-seam amplitude gain and enough high-frequency decay to control the full singular-value population. Generic thin-domain limits or qualitative smoothing theorems do not by themselves supply this normalized boundary-to-boundary Schur estimate.

PF-230 supplies a geometric audit control, not an operator theorem. An argument that interprets the full logarithmic axis interval as `O(L_j/s_j)` copies of a minimum-width corridor must reconcile that interpretation with the exact hyperbolic fanout and the `pi/s_j` untrimmed axis inverse-width integral. Conversely, PF-230 cannot be used to assert an `O(s_j^{-1})` singular-value count for the PF-205 trimmed operator without the missing DtN/Poisson comparison.

A decisive negative result must exhibit the missing mechanism inside the canonical PF geometry. It is not enough to perturb an abstract positive matrix or to repeat PF-223's generic multiplicity countermodel. Show that actual tangential mixing, the normalized seam truncation, variable neighboring cells, or the physical `P/H` projections produce a dressed channel whose scale or counting law violates every corridor-comparable envelope relevant to the endpoint.

If the actual one-cut envelope survives, attack the second gate separately: the PF-222 cuts are nested and overlap. Prove a direct Lorentz/weak-ideal estimate for the weighted flux series, exploit cancellation/commutator structure that is genuinely present, or derive another exact reassembly mechanism. PF-228's orthogonal direct-sum count and PF-229's single-cut serial theorem are controls, not a proof of this final step.

As alternatives, attack PF-204's unsmoothed native factorization directly at weak `S_1`, or settle the PF-183 conservative true-short-collar splice. A complete success must ultimately use one coherent global identification and one exact first-relative-resolvent identity; incompatible smooth and unsmoothed architectures cannot simply be combined to cover missing terms.

## Evidence boundary

No full weak-`S_1` theorem is established. PF-228 proves the favorable `w/s` amplitude and frequency envelope only for an isolated straight-corridor control. PF-229 proves that the same envelope survives the full global cut only for a frozen scalar mode-preserving serial completion. PF-230 proves exact axis fanout, fixed-window natural-width asymptotics, and a `\pi/s` **untrimmed axis inverse-width integral**; it does not prove a singular-value counting theorem for the PF-205 trimmed boundary problem or the dressed cut flux. None of these results proves stability of the PF-228 envelope under actual tangential mode mixing or reassembles the true nested PF-222 cut series.

Conversely, PF-226/PF-227 prove large raw channel multiplicity in the actual pant but do not show that those channels survive Schur dressing at order one. PF-225's universal `1/2` cap is an upper bound, not evidence that saturation is attained. The current clue therefore asserts only that the variable-profile actual dressed cut-flux comparison and subsequent nested reassembly are precise, evidence-backed research targets.

PF-204's unsmoothed endpoint and the PF-183 true-short-collar endpoint remain unresolved. Clue acceptance does not imply wave-operator completeness, scattering-matrix or determinant/resonance control, prime/clone separation, or any RH consequence.

## Research disposition

The clue remains `accepted`, but its smooth-route gate is now materially sharper. PF-225--PF-227 show that raw saturated multiplicity and fixed high-pass truncation do not close the endpoint. PF-228 shows that exact local Schur dressing can nevertheless move the full inverse-seam population to the compatible `w/s` scale, and PF-229 shows that frozen serial global shorting preserves that gain. PF-230 then shows that the real natural-width central corridor retains a nonconstant hyperbolic fanout at leading order while the underlying axis graph has only a `\pi/s+o(1/s)` inverse-width calibration. The next Research Watch step is therefore a **variable-profile actual-PF dressed DtN/Poisson comparison**, not another generic scalar/global control and not a constant-strip perturbation argument. Nested weak-`S_1` reassembly remains a separate second gate after that comparison.