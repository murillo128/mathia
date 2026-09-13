# MI-006 — Stationary boundary zeros price prediction, but the actual Nyman descendant symbol is an aliased energy spectrum

**Evidence level:** exact for the stationary outer-polynomial matched controls through NB-083 and for the integer-descendant Toeplitz reduction of the actual Nyman innovations in NB-084. No quantitative decay rate for the actual periodized spectra is yet proved.

NB-082 identifies finite-prediction excess as the resource controlling prediction-volume charge. Qualitative outerness says only that the excess tends to zero; bounded screening at prefix size `R` needs a rate of order `1/R` after aggregation.

NB-083 makes the stationary calibration sharp. For an outer polynomial filter, a unit-circle zero of multiplicity `k` contributes `k^2/L` to the anchored prediction excess, so boundary singularity forces depth `L=Omega(R)` and an exponential-size physical future merely for bounded screening. If every zero lies strictly outside the unit circle, the inverse is analytic through the boundary and prediction is geometric.

NB-084 shows why that boundary-zero heuristic cannot be applied directly to the arithmetic source. Exact integer branching makes the shifts `U_(r log q)D_j` genuine future descendants, but fiberizing one dilation ray produces the periodized nonnegative spectrum

`W_(j,q)(theta)=(1/log q) sum_(k in Z) |D_j(1/2+i(theta+2pi k)/log q)|^2`.

The depth-`L` radial prediction error is the anchored Toeplitz minimum for this `W_(j,q)`. A zero of one continuous Mellin boundary sample removes only one summand. To obtain a genuine unit-circle zero of the prediction symbol, the whole alias class would have to vanish simultaneously. Since each nonzero Hardy innovation has nonzero boundary value almost everywhere, `W_(j,q)>0` almost everywhere unconditionally.

The new source-facing gate is therefore not “do zeta zeros lie on the boundary?” but **how deep are the valleys of the alias-periodized Nyman spectrum, and how fast do the associated anchored Toeplitz errors fall relative to the visible causal innovation scale?** Ordinary isolated critical zeros do not automatically impose the reciprocal-depth penalty of the stationary control.

NB-084 also gives the exact one-sided certificate: at horizon `q^L R-1`, the stable-tail charge is bounded above by the sum of logarithms of radial Toeplitz errors divided by the causal prediction errors. A sufficiently small aggregate immediately excludes a stable tail. Failure of the radial certificate is inconclusive because the complete nonstationary future can use cross-ray combinations.

**Boundary.** Almost-everywhere positivity of `W_(j,q)` gives no useful prediction rate; arbitrarily deep thin valleys remain possible. NB-084 does not exclude an entire aliased arithmetic progression of boundary zeros, prove zero-spacing input, or show the radial family is optimal. The stationary `1/L` law remains a matched control, not a theorem about the actual source.