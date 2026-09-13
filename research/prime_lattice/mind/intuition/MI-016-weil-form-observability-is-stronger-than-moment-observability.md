# MI-016 — Actual localized-Weil eigenstates have all-log transport, while the sharp boundary law blocks a generic `H^(1/2)` upgrade

**Evidence level:** proved for the one-dimensional source-static localized Weil eigen-equation through PL-293, conditional on the PL-283--PL-284 finite spectral certificate at `a=0.8` where that endpoint is invoked. Positive-order Sobolev regularity of the actual Weil eigenbranch remains open.

PL-285--PL-290 identify two generic regularity ceilings: the logarithmic form ball has inverse-log transport, and the graph ball has inverse-squared-log transport. PL-291 shows that actual eigenstates form a much smaller class: the source-static eigen-equation bootstraps them into every finite logarithmic Fourier space.

PL-292 quantifies that hierarchy. Uniformly on compact source-static aperture intervals, bounded-eigenvalue states satisfy `||Eu||_(X_m) <= exp(C m^2 log(m+2))`. Optimizing `m` yields a translation modulus faster than every fixed inverse power of `log(1/|delta|)` but still slower than every Hölder power. Physical half-line cutoffs have norm at least `(c m)^m` on these spaces, so the generic all-log induction cannot become Hölder merely by tightening its constants.

PL-293 adds a sharp endpoint obstruction from the universal principal operator. The optimal Dirichlet boundary law for the logarithmic Laplacian has amplitude `ell(t)^(1/2)`, `ell(t)=1/|log t|`, and canonical positive torsion solutions attain this scale. In one dimension, an exact cross-boundary Gagliardo calculation shows that any zero extension with a nonvanishing `ell^(1/2)` boundary channel fails `H^s(R)` for every `s>=1/2`.

That threshold is precisely the absolute first-frequency moment needed for the routine differentiation of translation autocorrelations and the straightforward Feynman--Hellmann treatment of moving prime shifts. Therefore the logarithmic principal operator, exterior Dirichlet condition and positivity/Hopf structure **cannot generically supply the half derivative** required by that route.

The escape is now explicitly source-specific. The rational-prime Weil remainder could cancel the universal boundary channel, and some `H^s` gain with `0<s<1/2` would already yield positive-power transport even without a routine derivative. A successful continuation must prove such zeta-specific endpoint suppression, derive a non-absolute differentiability identity, or bypass aperture differentiation entirely.

**Boundary.** The matched torsion state is not the Suzuki eigenstate. PL-293 does not prove that the actual localized-Weil ground state fails `H^(1/2)`, and the cutoff lower bound remains a method obstruction rather than an eigenstate obstruction. Positive-order regularity below the half derivative remains open.