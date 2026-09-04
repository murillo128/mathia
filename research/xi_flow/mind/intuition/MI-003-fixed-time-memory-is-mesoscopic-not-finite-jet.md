# MI-003 — Fixed-time Xi memory is mesoscopic; far-tail room is available, so the live bottleneck is near-boundary flux organization

**Evidence level:** supported through XF-021; finite-jet and linearized-scale statements are exact in their stated regimes, and the localization identities are used only where the real-simple flow applies

## Core intuition

Order-one heat-time memory at height `T` lives on about `log^2 T` gaps, not in a finite collision jet or bounded stencil. The Cauchy/`H^{1/2}` boundary model explains why a fixed-shape cutoff is scale critical, while capacitary and cross-ratio reorganizations show that the far exterior can be made genuinely small without pointwise lower-gap control.

The newest source audit changes the bottleneck again. Rodgers--Tao's global counting error already supplies super-mesoscopic buffers whose physical width is a diverging multiple of the `log T` core span, so lack of spatial room is not the obstruction. What remains is the near-buffer and neutral mean/span flux. A broad compact centered-convex entropy class cannot remove that difficulty source-free because compression-sensitive boundary sites generate positive collision poles.

## Strongest justified principle

XF-006 rules out every robust finite collision jet as Xi-specific; XF-007--XF-013 identify the mesoscopic `log^2 T` scale and endpoint Cauchy carrier. XF-014--XF-018 give the exact real-simple gap diffusion, finite-amplitude bulk coercivity in its stated regime, scalable capacitary cutoff, and collision-safe uncentered leakage weight `w_ik=c_ik g_i g_k` dominated by a cross-ratio/Cauchy kernel.

XF-019 aggregates that kernel before estimating it. For a core of physical span `S` separated from the far exterior by buffer width `D`, the entire tail interaction is bounded by `log(1+S/D)` on each side. Microscopic endpoint gaps disappear from this block estimate; vanishing far-tail leakage requires only `D/S->infinity`.

XF-020 shows that this scale is source-compatible. Subtracting Rodgers--Tao's global zero-counting formula gives asymptotic counts on windows `D=R(T) log T` for any slowly diverging `R(T)` in the stated range. Such buffers contain `asymp R(T) log^2 T` zeros and make the aggregate far-tail cross-ratio leakage `O(1/R(T))`. The previous diagnosis that source-valid room was missing is therefore removed.

XF-021 closes the obvious centered-entropy shortcut. For any differentiable convex single-gap entropy centered at a positive reference spacing, compact localization has an exact dichotomy: either the entropy is blind to compression below the reference, or a compressed boundary gap adjacent to an exterior collision produces an arbitrarily large **positive** flux. The uncentered square avoids that sign by keeping the gap factor positive, but then mean removal remains a nonlocal span/endpoint problem.

## What remains possible

The live theorem should organize the core--near-buffer interactions and the derivative of the block span/mean through a signed or multiblock identity, noncompact summable localization, or an Xi-specific exterior constraint. It must retain a fixed backward-time margin after the source-valid far buffer is installed and survive matched real-entire/log-repulsion controls.

## Status / novelty

Fractional localization, capacity, cross-ratios, convex entropy dissipation, and global zero counting are classical ingredients. The synthesis is the moving boundary gate: **far-tail capacity is now affordable; compact centered convexity is not a source-free repair; the unresolved information is near-boundary/mean flux at mesoscopic scale**.

## Falsification criterion

Derive a source-forced signed/span identity that controls the near buffer and endpoint flux with a positive fixed-time margin, or construct source-admissible real-simple configurations satisfying the current counting/buffer constraints while making every such proposed assembly lose its margin.

## Lean-formalizable core

- Mesoscopic `log^2 T` memory scale.
- Block cross-ratio tail bound `log(1+S/D)`.
- Super-mesoscopic count from global counting error.
- Compact centered-convex entropy collision-spike dichotomy.
