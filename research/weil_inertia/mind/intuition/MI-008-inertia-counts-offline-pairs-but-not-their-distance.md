# MI-008 — Inertia counts off-line pairs exactly, while both continuous charges and naive singular repairs fail at confluence

**Evidence level:** proved for the Lamzouri finite Hilbert-space model through WI-167; source-level quantitative exclusion remains open

## Core intuition

Sign information and coercive magnitude are distinct. Lamzouri's finite tensor has an exact discontinuous discriminator: its negative index counts distinct off-line conjugate pairs. But the magnitude of those directions can collapse continuously as an off-line pair approaches a critical-line double.

The newer results show that simply making the detector more singular does not solve this. Schur normalization cancels the collapsing horizontal scale instead of charging it, while an added quantized projection step is too large for the vanishing source deficit. A useful singular detector therefore needs an independently source-determined scale or interaction; discontinuity alone is not coercivity.

## Strongest justified principle

WI-138 gives the exact inertia theorem; WI-139 aligns near-sharp negative eigenspaces with the canonical horizontal defect quotient. WI-140 constructs explicit confluence controls: a simple off-line pair retains one negative eigenvalue for every nonzero displacement while its negative magnitude and total Lamzouri deficit vanish quadratically.

WI-141--WI-142 show that every fixed finite package, and every preassigned size-dependent family, of continuous spectral regularizations can be defeated by choosing the horizontal displacement below its continuity scale. Quantitative use of inertia therefore cannot come from a smoother approximation chosen independently of the source configuration.

WI-164 tests the natural Schur singularity. Decomposing the odd synthesis into retained and horizontal pieces gives an exact normalized correction `K_V K_V^*`; the inverse horizontal block cancels through a unitary polar factor, so no inverse power of the collapsing `K_H` survives. On the isolated simple off-line pair, `K_V=0`, and the Schur charge vanishes identically.

WI-167 tests the opposite strategy: make the target jump by adding a nonzero integer-depth flag projection. Every such step has Hilbert--Schmidt norm at least one, whereas the whole one-pair source deficit tends to zero. Near confluence the distance to the refined target alone exceeds the available deficit. Thus a universal nonnegative refinement cannot be funded merely by the existence of the off-line direction.

## What remains possible

The confluence controls are not asserted to model the full zeta source. A successful theorem may derive an anti-confluence scale from zero density, separation, multiplicity, horizontal displacement, correlations, or another explicit-formula input. Alternatively a singular detector may activate only through a rigorously controlled multi-zero interaction that is absent on the isolated pair.

Such an observable must come with its own source identity or inequality. It cannot be obtained by choosing ever finer continuous smoothing, normalizing by the collapsing horizontal block, or inserting an autonomous quantized flag step after the fact.

## Status / novelty

Sylvester inertia, spectral continuity, Schatten convergence, Schur complements, polar decomposition, and projection-rank norms are classical ingredients. The line-specific synthesis is exact: **negative index identifies the exceptional zero type, but neither continuous spectral mass nor the two most natural singular repairs provide a source-funded quantitative cost as the off-line pair confluences**.

## Falsification criterion

Derive from unconditional zeta information a quantitative source scale that prevents positive-density or individual off-line pairs from hiding at confluence, or construct a source-natural singular/multi-zero detector with a positive lower bound that survives the WI-140 isolated-pair controls without contradicting the available deficit.

## Lean-formalizable core

- Congruence inertia count and one-pair confluence eigenvalues.
- Continuity defeat for detector families.
- Schur normalization identity and singular-value cancellation.
- Quantized flag norm floor versus vanishing source deficit.
