# PF-009 — the Hecke shadow is not intrinsic

> Retroactive persistence from the legacy `FINDINGS.md`; no new mathematical claim or evidence upgrade is introduced here.

**Status:** `NEGATIVE/OBSTRUCTION`.

## Claim

After replacing the exact endpoints by the linear shadow

```text
pi cot(pi/p) -> p,
```

a consecutive-prime generator can be interpreted relative to `PSL(2,Z)` through a primitive Hecke double coset. This produces genuine modular Hecke `L`-functions on the modular surface, not intrinsic spectral data of the exact prime flute.

The obstruction is structural:

- in the flute's own group the same matrix is already a deck transformation, so its own double coset is trivial;
- the exact endpoint `pi cot(pi/p)` is not in the rational projective setting required by the modular commensurator;
- a small real perturbation does not preserve commensurator membership.

## Research consequence

`gap -> Hecke degree -> zeta factors` is an external arithmetic reinterpretation of the gaps, not evidence for a spectral mechanism intrinsic to the original surface.
