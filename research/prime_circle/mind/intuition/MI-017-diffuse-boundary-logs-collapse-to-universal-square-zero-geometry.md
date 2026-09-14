# MI-017 — Diffuse one-profile boundary logs collapse to universal square-zero geometry

**Evidence level:** exact asymptotic operator statement from [PC-295](../../findings/PC-295-diffuse-boundary-log-singular-spectrum-is-classical-green.md)--[PC-297](../../findings/PC-297-diffuse-boundary-log-pseudospectrum-is-universal-square-zero.md) under their diffuseness hypothesis. The conclusion is fixed-scale and one-profile; non-diffuse and joint-profile regimes remain open.

PC-295 shows that diffuse boundary-log matrices keep a nonzero deterministic Green singular spectrum. PC-296 simultaneously shows their eigenvalues collapse to zero because the left and right low-Fourier frames become mutually orthogonal. PC-297 identifies the operator geometry behind both facts: after polar normalization and an asymptotically negligible correction, the dominant left/right frames can be made exactly orthogonal, producing a square-zero approximant

`S=U D W*`, `W*U=0`, hence `S^2=0`,

with `||S||->1/2`, and the full matrix approaches this class in operator norm.

For a square-zero operator the fixed-`epsilon` pseudospectrum is exactly a disk controlled only by `||S||`. Therefore the diffuse prime matrix has the same limiting fixed-scale pseudospectrum and resolvent profile as every matched diffuse control satisfying the same frame estimates. The nonnormal bulge is real, but its shape is universal rather than arithmetic.

This changes the surviving currency. Singular strength, eigenvalue loops and fixed-scale pseudospectral amplification are not three independent source signals here; they are different projections of the same asymptotic square-zero geometry. A prime-specific invariant must retain relational information that the left/right orthogonalization discards, use several coupled profiles/levels, probe a scale comparable to the vanishing operator defect, or leave the diffuse regime.

**Boundary.** PC-297 does not say that pseudospectra at `epsilon=epsilon(q)->0` are universal at every rate, nor that all joint/noncommuting observables classicalize. Those are genuinely different questions because operator-norm closeness only transfers structure above its error scale.
