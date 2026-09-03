# MI-006 — Mirror symmetry and pre-scalar Hilbert geometry force quantitative leakage in fixed-period screens; source extraction remains the gate

**Evidence level:** supported by WI-115--WI-127, with exact quantitative fixed-period results and literature-backed zeta source inputs in the stated regimes

## Core intuition

Screening can erase one marginal while forced information survives in another. The recent results substantially strengthen this from qualitative alias existence. For mirror-symmetric periodic cells, off-line displacement forces a **period-uniform packet of lower-half reciprocal alias energy**; in Lamzouri's Hilbert-space formulation, off-real pairs also carry an exact nonnegative anti-invariant transversality remainder before scalar inequalities are applied; and fixed-period repetition makes that remainder extensive.

The remaining problem is no longer whether a canonical fixed-period screen can hide everything. It is whether comparable coercivity survives **growing-period, aperiodic, source-admissible zeta configurations and the complete global assembly**.

## Strongest justified principle

WI-115--WI-122 establish the screening baseline. Support-one termwise positivity can be screened; Fujii moments rule out one long double-density extremizer at positive density; and finite compensated motifs show that bounded counting discrepancy and moving-edge cancellation can coexist with off-line mass.

WI-123--WI-124 then use conjugation and same-ordinate mirror symmetry to force reciprocal leakage. A genuinely off-line mirror-symmetric period-`P` cell cannot make all first `floor(P/2)` reciprocal power sums vanish; some alias must occur at `alpha<=1/2`.

WI-125 makes that leakage quantitative uniformly in `P`. If `p_m=C(m/P)` and `q=floor(P/2)`, the weighted first-half mass `sum_{m<=q}|p_m|/m` at or below `log 2` forces every reciprocal root onto the unit circle. Hence any off-line cell has strictly larger weighted mass and, by Cauchy--Schwarz, a period-uniform positive lower bound on total first-half squared alias energy. Growing period cannot make the entire selected-cell lower-half packet disappear in aggregate.

WI-126 exposes a second, pre-scalar carrier inside Lamzouri's finite Hilbert inequality. Reconstructing the discarded terms gives an exact decomposition

`Q-(2N-n)=R_B+R_U+R_M+R_H`,

with every remainder nonnegative. The horizontal block satisfies

`R_H >= 4 sum m_z dist(h_z,V)^2`,

so off-real conjugate pairs carry a basis-independent transversality charge before the final scalar estimate. Finite equality is impossible in the presence of off-real mass, although asymptotic screening can still drive the charge small.

WI-127 closes the fixed-period screening escape for that stronger carrier. Repeating a simple conjugation-symmetric cell with distinct reciprocal roots fiberizes the complete `g/h` system to an invertible Vandermonde matrix. Each omitted anti-invariant `h` direction stays a fixed positive distance from the even/real span, so the Lamzouri horizontal remainder grows linearly with the number of periods, uniformly along the smoothing family approaching the Montgomery--Taylor optimizer.

## Evidence synthesis and boundaries

These results do not yet improve the unconditional zeta proportion. The constants can degenerate when period grows, reciprocal roots approach collision, multiplicities appear, or the selected cell is embedded in a large irregular reservoir. WI-125 controls aggregate reciprocal alias energy of the selected periodic cell, while WI-126--WI-127 control Hilbert transversality for fixed-period repetition; neither yet proves that actual zeta off-line density forces an extensive remainder after arbitrary surrounding zeros are included.

The live theorem is therefore a source-transfer/coercivity statement: show that sustained off-line mass in the actual zeta zero process forces a quantitative lower bound on the Lamzouri horizontal remainder or another pre-scalar channel, using unconditional density/correlation inputs to exclude the remaining screening geometries.

## Status / novelty

Self-inversive polynomial criteria, Newton identities, Vandermonde conditioning, shift-invariant fiberization, and Hilbert/Bessel decompositions are classical. The persisted synthesis is the sharpened channel-transfer principle: **fixed-period compensation is quantitatively charged before scalarization; only source-valid global screening remains unresolved**.

## Falsification criterion

Construct a fixed-period simple mirror-symmetric off-line cell with vanishing first-half aggregate alias energy, or repeated fixed-period cells whose Lamzouri anti-invariant distance is sublinear despite the WI-127 hypotheses. A growing-period/aperiodic source-admissible family with vanishing global transversality would instead delimit the remaining boundary.

## Lean-formalizable core

- Self-inversive first-half coefficient/alias energy bound.
- Exact Lamzouri slack decomposition.
- Basis-independent horizontal transversality lower bound.
- Fixed-period Vandermonde fiberization and extensive distance.
