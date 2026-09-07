# MI-004 — Mean-absolute Mertens control is RH-complete, and sub-L1 moments do not transport the needed excursion mass

**Evidence level:** exact Mellin/checkpoint results and exact matched-control barriers through MC-120, with stronger Pintz profile still `NEEDS-AUDIT`

## Core intuition

The mean-absolute endpoint is RH-complete, but statistics below `L^1` forget exactly the rare coherent amplitude that the endpoint consumes. MC-117--MC-120 show that this is not repaired merely by imposing square-free support, multiplicativity, uniform control across a polynomial window, or even one fixed multiplicative function recurring on infinitely many such windows.

The surviving distinction is quantitative cross-scale/source coherence. The fixed comparator in MC-120 can hide its excursions only by placing the controlled windows very far apart and does not reproduce Möbius-specific correlation information. Dense logarithmic checkpoints and genuine arithmetic correlations therefore remain materially different inputs rather than technical refinements of the same moment bound.

## Strongest justified principle

MC-115 proves that square-root-scale mean absolute Mertens control continues `1/zeta(s)` to every half-plane `Re s>1/2+epsilon`, giving the exact RH equivalence. MC-116 lowers only the scale-coverage burden: a subpower-dense deterministic checkpoint sequence interpolates with no exponent loss.

For every `0<p<1`, MC-117 quantifies the information gap from a fractional moment to the first absolute mean. MC-118 realizes the missing excursion using balanced prime blocks inside a multiplicative square-free-supported comparator. MC-119 keeps the weak moment controlled throughout a full polynomial window rather than at one cutoff. MC-120 removes the moving-comparator objection: one fixed multiplicative function can exhibit the same separation on infinitely many windows while retaining large first-absolute mass at their base scales.

What MC-120 does not provide is equally important. Its scales are intentionally lacunary, and the construction neither fixes Möbius's exact prime signs nor preserves known Möbius correlation information. The live transfer must therefore use a condition that couples excursions across sufficiently dense scales or constrains them through genuinely Möbius-specific arithmetic.

## Counterevidence / boundary

The comparator class is much larger than Möbius. Exact agreement with Möbius at every prime would identify the function tautologically, so the useful target is an intermediate quantitative source law. MC-120 also does not defeat MC-116's subpower-dense checkpoint geometry and does not address the endpoint `p=1`, where there is no sub-`L1` information gap.

## Epistemic status

**Proved endpoint equivalence and matched-control obstruction; open source mechanism.** The stronger Pintz asymptotic remains optional pending audit.

## Falsification criterion

Derive the RH-scale first absolute mean from a source condition genuinely weaker than that conclusion and satisfied by Möbius, while showing why the MC-117--MC-120 coherent-excursion comparators cannot satisfy it. A successful dense-scale or correlation-coupled theorem would narrow this intuition in exactly the intended way.