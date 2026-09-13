# MI-016 — Actual localized-Weil eigenstates have optimized all-log transport, but the generic cutoff blocks a Hölder upgrade

**Evidence level:** proved for the one-dimensional source-static localized Weil eigen-equation through PL-292, conditional on the PL-283--PL-284 finite spectral certificate at `a=0.8` where that endpoint is invoked. Positive-order Sobolev regularity and a quantitatively useful macroscopic aperture theorem remain open.

PL-285--PL-290 identify two generic regularity ceilings: the logarithmic form ball has inverse-log transport, and the graph ball has inverse-squared-log transport. PL-291 shows that actual eigenstates form a much smaller class: the source-static eigen-equation bootstraps them into every finite logarithmic Fourier space.

PL-292 quantifies the cost of that bootstrap. Uniformly on compact source-static aperture intervals, normalized bounded-eigenvalue states satisfy `||Eu||_(X_m) <= exp(C m^2 log(m+2))`. Optimizing `m` against a small translation gives a modulus

`exp(-c (log log(1/|delta|))^2 / log log log(1/|delta|))`.

This is genuinely stronger than every fixed inverse power of `log(1/|delta|)`, so uncontrolled constants are no longer the immediate gap. But it remains subpower in `|delta|` and therefore does not justify differentiating moving prime translations.

The same proof architecture has a concrete obstruction: a physical half-line cutoff on `X_m` has norm at least `(c m)^m`. Boundary truncation creates a `1/xi` Fourier tail whose high logarithmic moments have factorial scale. Thus the generic all-log induction cannot become Hölder merely by replacing coarse cutoff estimates with uniformly exponential ones.

The remaining escape must be eigenstate-specific: endpoint cancellation, a source identity avoiding worst-case cutoffs, a direct positive-order moment, or a positivity continuation argument that bypasses aperture differentiation.

**Boundary.** The cutoff lower bound is for the operator on the full logarithmic space, not for the actual ground state. It is a method barrier, not a theorem that localized-Weil eigenfunctions lack Sobolev regularity.