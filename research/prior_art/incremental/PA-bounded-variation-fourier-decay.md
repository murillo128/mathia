---
id: PA-bounded-variation-fourier-decay
type: prior-art
canonical_name: Fourier coefficient decay for functions of bounded variation
aliases:
  - Bounded-variation Fourier decay
kind: Fourier coefficient estimate
topics:
  - harmonic analysis
  - bounded variation
---

# Fourier coefficient decay for functions of bounded variation

## What it is

For a complex, periodic function of bounded variation, the nonzero Fourier coefficients decay at least inversely with frequency. With period `2π`, coefficients `fhat(n)=(2π)^(-1)∫_0^(2π) f(t)e^(-int) dt`, and total variation `V(f)` over a period, the classical bound is `|fhat(n)| <= V(f)/(2π|n|)` for `n != 0`. Wu's publisher abstract states this estimate explicitly as an already known result.

## Relation to RH / Mathia research

The triggering source is [[research/visual_exploration/findings/VIS-465-capped-variation-tariff-for-farey-transport-spectrum|VIS-465]], which explicitly identifies its finite Dirichlet-sine estimate as the discrete analogue of this classical mechanism. Its endpoint-inclusive discrete variation controls a sine-tail majorant; Parseval separately caps the normalized tail at one. The finite normalization and the Farey transport application are established in that source, not attributed to the continuum theorem.

## Known scope and limits

Variation supplies a one-sided decay bound. It does not identify the spectrum, force depletion when variation is large, compare a vanishing transport energy with an arithmetic residual, or prove any bound on genuine Farey discrepancy. In VIS-465 the uncapped majorant can exceed one; the probability cap belongs to the tail inequality. No new general Fourier theorem or RH consequence is asserted.

## Related prior art

The local application combines this estimate with finite sine orthogonality and normalized-vector stability. These are separate ingredients; no new implication between RH criteria is supplied by this node.

## Evidence and provenance

- Jie Wu, *Coefficients de Fourier de fonctions à variation bornée*, Proc. Amer. Math. Soc. **117** (1993), 689–690, [DOI and publisher abstract](https://www.ams.org/proc/1993-117-03/S0002-9939-1993-1150658-3/), DOI `10.1090/S0002-9939-1993-1150658-3`. The indexed publisher abstract supplies the statement; full-text access was not needed for this identity resolution.
- Mitchell Taibleson, *Fourier coefficients of functions of bounded variation*, Proc. Amer. Math. Soc. **18** (1967), 766, [DOI](https://doi.org/10.1090/S0002-9939-1967-0212477-6); bibliographic identity verified in Wu's publisher reference list. No priority claim is made.
- Persisted trigger: `research/visual_exploration/findings/VIS-465-capped-variation-tariff-for-farey-transport-spectrum.md`, “Abel summation and the finite sine-tail estimate” and its explicit prior-art comparison, at source revision `d173b1d2a30b3e698f236df92bf8672affe19080`.
