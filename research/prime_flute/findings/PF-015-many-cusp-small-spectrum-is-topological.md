# PF-015 — many-cusp small spectrum is topological, not prime-specific

**Status:** NEGATIVE/OBSTRUCTION; literature-backed.

## Claim

The abundance of Laplace eigenvalues below `1/4` on the finite-area punctured-sphere right limits proposed in PF-008 is not, by itself, a prime-specific spectral signature.

Let `S` be a finite-area hyperbolic surface of genus `g` with `n` cusps. Hide and Thomas prove that for every `a > 0` there is `b > 0` such that, whenever

```text
g < a n,
```

`S` has at least

```text
b (2g+n-2)
```

small Laplace eigenvalues in `[0,1/4)`.

For the genus-zero right-limit surfaces `S_H` envisioned in PF-008 this gives a linear-in-cusp-count lower bound regardless of whether the cusp positions came from prime patterns.

Otal–Rosas give the complementary topological upper bound: a surface of signature `(g,n)` has at most `2g+n-2` small eigenvalues. Thus, in the many-cusp genus-zero regime, the *number* of small eigenvalues is already controlled to linear order by topology.

Moreover, for genus `0` or `1`, small positive eigenvalues are known to be residual rather than cuspidal: they arise from poles of the scattering matrix. Hence a large number of real scattering poles with spectral parameters

```text
s in (1/2,1),
lambda = s(1-s) in (0,1/4)
```

is likewise not sufficient evidence of prime arithmetic.

## Consequence for the prime-flute program

PF-008 may still yield a valid right-limit/Weyl-sequence theorem after its analytic hypotheses are closed, but the following observables should **not** be treated as prime-specific:

```text
existence of small eigenvalues,
number of eigenvalues below 1/4,
existence of many residual scattering poles in (1/2,1).
```

If the finite prime-pattern limits `S_H` retain arithmetic information spectrally, it must be sought in finer data such as pole locations, multiplicities, scattering eigenchannels/eigenphases, or comparisons against non-prime surfaces with the same signature.

## Literature anchors

- Will Hide and Joe Thomas, *Small eigenvalues of hyperbolic surfaces with many cusps*, arXiv:2410.06093. Current Theorem 1.3 gives the linear lower bound for `g < a n`.
  - https://arxiv.org/abs/2410.06093
- J.-P. Otal and E. Rosas, *Pour toute surface hyperbolique de genre g, lambda_{2g-2} > 1/4*, J. Differential Geom. 82 (2009), underlying the sharp topological upper bound quoted by Hide–Thomas.
- The genus `0/1` residual-spectrum fact is summarized in current literature on many-cusp hyperbolic surfaces; when used in a formal paper, pin the original Otal reference rather than relying on a secondary summary.

## Novelty status

The spectral theorems are known. The project-specific conclusion is a **negative control**: the low-energy eigenvalue count of prime-pattern punctured-sphere limits is topologically confounded and cannot serve as a discriminating prime/RH signal.