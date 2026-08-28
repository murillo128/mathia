# PF-008 — right-limit islands and sub-`1/4` essential spectrum

> Retroactive persistence from the legacy `FINDINGS.md`; no new mathematical claim or evidence upgrade is introduced here.

**Status:** `NEEDS-AUDIT`.

## Candidate claim

For a recurrent bounded prime-offset pattern `H`, the rescaling

```text
z -> pi z - P
```

sends

```text
pi cot(pi/(P+h)) - P -> h.
```

The proposed limit is a finite-area punctured-sphere surface `S_H` separated from the rest of the flute by pinching necks. If geometric and spectral convergence are made precise, an `L^2` eigenvalue of a recurrent `S_H` in `(0,1/4)` should generate an escaping Weyl sequence and therefore enter the essential spectrum of the full prime flute.

## Missing checks preserved from the legacy finding

1. exact topology/cusp count and area of `S_H`;
2. an applicable convergence theorem for the noncompact pinching pieces;
3. the small-eigenvalue test-function/domain argument;
4. construction of the escaping Weyl sequence.

## Later boundary

The separate PF-015 many-cusp result shows that mere abundance of sub-`1/4` eigenvalues is topologically confounded even if the right-limit mechanism is completed. Exact locations or marked data remain a different question.
