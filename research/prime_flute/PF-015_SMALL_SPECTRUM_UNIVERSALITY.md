# PF-015 — many-cusp small spectrum is topological, not prime-specific

**Status:** NEGATIVE/OBSTRUCTION with literature-backed finite-type input.

## Result

The proposed use of the existence, abundance, or mere accumulation of Laplace spectrum below `1/4` on large prime-flute right-limit islands as a prime-specific spectral fingerprint is too weak. For genus-zero finite-area hyperbolic surfaces with many cusps, a large small spectrum is forced by topology alone, independently of the prime-gap geometry.

This substantially weakens the interpretation of PF-008. Exact eigenvalue locations may still depend on the right-limit pattern, but the *presence and linear abundance* of sub-`1/4` spectral data do not distinguish prime-derived punctured spheres from generic punctured spheres.

## External theorem 1 — universal many-cusp lower bound

Hide and Thomas, `Small eigenvalues of hyperbolic surfaces with many cusps`, arXiv:2410.06093v2 (30 July 2026), prove:

```text
For every a > 0 there exists b > 0 such that,
if X has genus g and n cusps with g < a n,
then X has at least b (2g+n-2) Laplace eigenvalues in [0,1/4).
```

For genus `g=0`, choose any fixed `a>0`. Hence every sufficiently large `n`-cusped hyperbolic sphere has at least

```text
b (n-2)
```

small eigenvalues. At most one of these is the constant zero mode, so the number of positive small eigenvalues is still linear in `n`.

Reference:

- W. Hide, J. Thomas, *Small eigenvalues of hyperbolic surfaces with many cusps*, arXiv:2410.06093v2.
- Current arXiv abstract explicitly states the linear lower bound for all `g < a n`; this is stronger than the original v1 logarithmic bound.

## External theorem 2 — genus-zero small eigenvalues are residual

Otal's topological theorem on small eigenfunctions implies that finite-area hyperbolic surfaces of genus `0` or `1` have no cuspidal eigenfunctions with eigenvalue `<= 1/4`.

Therefore, on an `n`-cusped sphere, every positive eigenvalue in `(0,1/4)` is **residual**: it arises from a pole of the Eisenstein/scattering matrix at a real spectral parameter

```text
s in (1/2,1),
lambda = s(1-s).
```

References:

- J.-P. Otal, *Three Topological Properties of Small Eigenfunctions on Hyperbolic Surfaces*, in *Geometry and Dynamics of Groups and Spaces*, Progress in Mathematics 265, 2008, pp. 685-695.
- The result is also cited explicitly in Hide–Thomas' 2025 work on punctured spheres: for genus `0` or `1`, any small eigenvalue is residual.

## Consequence for the prime-flute right-limit program

Suppose PF-008 is completed rigorously and an isolated prime block has a finite-area genus-zero right-limit surface `S_H` with `n_H` cusps, where `n_H` grows with the block size.

Then Hide–Thomas already forces

```text
# { lambda in spectrum(S_H) : 0 <= lambda < 1/4 }
    >= b (n_H - 2),
```

regardless of the arithmetic pattern `H`.

Moreover, apart from the constant zero mode, this entire sub-`1/4` spectrum is residual/scattering spectrum by Otal.

Thus the chain

```text
large isolated prime cluster
    -> many sub-1/4 eigenvalues
    -> many real scattering poles
```

is **not** by itself a prime-specific spectral phenomenon. Any sufficiently many-cusped hyperbolic sphere has the same qualitative and linear-count property.

## Decisive negative conclusion

Do not use any of the following as evidence for a new prime/Riemann spectral mechanism:

```text
- existence of sub-1/4 eigenvalues on S_H;
- number of such eigenvalues growing with the number of cusps;
- existence of many residual poles s in (1/2,1);
- accumulation toward low energy obtained only by increasing the number of cusps.
```

Those effects have a topology-driven background that is already present without prime-gap input.

This also sharpens an earlier warning about a Hilbert–Pólya interpretation: the low-energy right-limit sector is not a collection of prime-specific cusp forms. In genus zero it is residual scattering spectrum.

## What remains potentially informative

A prime-specific signal could only survive in **finer data after removing this universal background**, for example:

```text
- the detailed locations and multiplicities of residual poles;
- scattering-matrix eigenvectors/channel structure;
- correlations between pole positions and exact multi-gap cross-ratios;
- a relative statistic comparing S_H to a non-prime punctured sphere with the same cusp count.
```

Even these are only candidates. Before promoting them, one must show that the statistic is not determined predominantly by generic moduli/topology and that it does not merely restate the input cross-ratios.

## Effect on existing findings

- **PF-008:** keep `NEEDS-AUDIT`, but downgrade the interpretation of *abundance* of sub-`1/4` spectrum from possible arithmetic fingerprint to universal many-cusp background.
- **PF-014:** low-energy graph couplings from specific short cross-ratio necks remain geometrically meaningful; however, the mere production of many small eigenvalues is not specific evidence for the prime construction.
- Future work should ask whether **pole locations conditioned on fixed topology/cusp count** contain stable information about the prime pattern. If not, the low-energy/scattering branch should be closed entirely.

## Novelty assessment

The two ingredients are known theorems. The useful new conclusion for this project is a **negative synthesis**: recent Hide–Thomas v2 removes the main reason to regard the many-small-eigenvalue consequence of PF-008 as prime-specific. This is exactly the kind of structural dead end that should be retained for Mathia/Lean research memory.