# MI-016 — Actual localized-Weil eigenstates need source-specific regularity or sign beyond the generic boundary mechanisms

**Evidence level:** proved for the one-dimensional source-static localized Weil eigen-equation through PL-294, conditional on the PL-283--PL-284 finite spectral certificate at `a=0.8` where that endpoint is invoked. PL-293 gives the sharp universal boundary obstruction; PL-294 gives the exact standard Beurling--Deny positivity-preservation window. Positive-order Sobolev regularity and fixed sign of the actual `a=0.8` ground state remain open.

PL-285--PL-290 identify two generic regularity ceilings: the logarithmic form ball has inverse-log transport, and the graph ball has inverse-squared-log transport. PL-291 shows that actual eigenstates form a much smaller class: the source-static eigen-equation bootstraps them into every finite logarithmic Fourier space.

PL-292 quantifies that hierarchy. Uniformly on compact source-static aperture intervals, bounded-eigenvalue states satisfy `||Eu||_(X_m) <= exp(C m^2 log(m+2))`. Optimizing `m` yields a translation modulus faster than every fixed inverse power of `log(1/|delta|)` but still slower than every Hölder power. Physical half-line cutoffs have norm at least `(c m)^m` on these spaces, so the generic all-log induction cannot become Hölder merely by tightening its constants.

PL-293 adds a sharp endpoint obstruction from the universal principal operator. The optimal Dirichlet boundary law for the logarithmic Laplacian has amplitude `ell(t)^(1/2)`, `ell(t)=1/|log t|`, and canonical positive torsion solutions attain this scale. In one dimension, an exact cross-boundary Gagliardo calculation shows that any zero extension with a nonvanishing `ell^(1/2)` boundary channel fails `H^s(R)` for every `s>=1/2`. That threshold blocks the routine first-frequency-moment differentiation route generically.

PL-294 shows that ordinary positivity does not rescue the Hopf strategy at the certified aperture. Combining the singular logarithmic jump with Suzuki's smooth archimedean kernel makes the first Beurling--Deny criterion hold exactly up to

`a_BD=(1/2)log(rho_pl)=0.140599787...`, `rho_pl^3-rho_pl-1=0`.

The threshold lies below `(1/2)log 2`, before any prime-power translation enters. For every `a>a_BD`, a two-bump sign-changing test can be placed away from the finitely many prime lags and violates the absolute-value contraction inequality. Thus the standard positivity-preserving/improving semigroup argument cannot be continued from the small-aperture archimedean regime to `a=0.8`.

This sharpens the source-specific escape. The rational-prime Weil remainder may still select a ground state with extra boundary cancellation or fixed sign even though neither property follows from the generic operator. Some `H^s` gain with `0<s<1/2` would already yield positive-power transport; alternatively a source-specific sign theorem could activate the PL-293 Hopf obstruction without requiring generic semigroup positivity. A non-absolute derivative identity or a route that bypasses aperture differentiation and Hopf geometry remains possible.

**Boundary.** Failure of Beurling--Deny positivity preservation does not imply that the actual localized-Weil ground state changes sign. PL-293's matched torsion state is not the Suzuki eigenstate, and neither PL-293 nor PL-294 proves failure of positive-order regularity for the selected eigenbranch. The exact `a_BD` value is purely archimedean and is not an RH-sensitive critical aperture.