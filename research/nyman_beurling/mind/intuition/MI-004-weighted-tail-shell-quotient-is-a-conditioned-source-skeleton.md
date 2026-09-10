# MI-004 — Weighted tail-shell quotient is a conditioned source-faithful skeleton

**Evidence level:** exact quotient identities, relative-distance preservation, Möbius-core retention, and N-uniform Gram conditioning through NB-034

## Core intuition

A useful Nyman compression need not preserve the whole canonical dictionary. It can quotient a large moving-tail nuisance sector provided three facts are proved simultaneously: the discarded sector is target-poor, the retained coordinates preserve the source-locked arithmetic core, and the retained geometry remains quantitatively conditioned independently of how far the original section extends.

Weighted tail adjacency realizes exactly this combination. It converts the large tail into one source-defined scalar while keeping the low canonical coefficients unchanged.

## Strongest justified principle

NB-031--NB-032 identify moving-tail adjacency as a Gram-whitened target-poor sector and show that removing it preserves the limiting target distance. NB-033 upgrades this to an explicit finite-dimensional source statement: a polylogarithmic cutoff preserves the finite-section distance multiplicatively, every head coefficient survives unchanged, and the whole ordinary tail collapses to one endpoint quotient scalar while the forced Möbius core remains present.

NB-034 replaces ordinary adjacency by weighted edges `n g_n-(n+1)g_{n+1}`. Their span is exactly the kernel of the first `M-1` shell observations. The quotient therefore has a concrete early-shell meaning, dimension `M-1`, unchanged head coefficients, and one weighted tail sum `M sum_{n>=M} a_n/n`. Its Gram matrix is squeezed between an explicit early-shell matrix and the original finite Gram matrix, with `lambda_min >= 1/(14 M^2 H_M^2)` and condition number `O(M^2 (log M)^3)` uniformly in `N`. The target-distance loss is at most `1/M`, so any cutoff `M/log N -> infinity` preserves the finite-section distance relatively.

## Program consequence

Work inside the conditioned skeleton. The next arithmetic theorem should constrain the retained Möbius-locked head or weighted tail scalar strongly enough to change the Nyman distance. Because conditioning no longer deteriorates with `N`, failures can be attributed more cleanly to missing source structure rather than to an uncontrolled quotient metric.

A larger nuisance quotient is worthwhile only if it keeps the same three certificates: explicit source coordinates, quantitative target preservation, and controlled conditioning.

## Counterevidence / boundary

The quotient does not itself prove the Báez-Duarte/Nyman approximation rate or RH. Polynomial conditioning in `M` can still be expensive when `M` grows, and the retained weighted tail scalar may hide hard Möbius cancellation. The theorem certifies a representation, not the source estimate needed on that representation.

The early-shell kernel is tailored to the canonical generators and target; it is not a generic principle that arbitrary weighted differences are harmless.

## Epistemic status

**Exact positive representation theorem: a near-logarithmic-dimensional weighted tail-shell quotient preserves the target distance and Möbius core while remaining polynomially conditioned, now at `O(M^2 (log M)^3)`, independently of the discarded upper section; the unresolved burden is an arithmetic constraint on the retained source coordinates.**

## Falsification criterion

Exhibit an admitted `M,N` for which the weighted-edge span is not the early-shell kernel, the target-loss bound or uniform Gram lower bound fails, or show that the forced Möbius core disappears from the retained coordinates under the stated quotient.
