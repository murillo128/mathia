# MI-013 — Autocorrelation tapers make exact difference shells noncancelling

**Evidence level:** exact for the broad autocorrelation-taper subclass constructed in VIS-203. This is a control on one admissible dephasing architecture, not a theorem for every endpoint-zero taper or for cancellation between distinct shell frequencies.

If the taper is a shifted autocorrelation `v(u)=w(u-1/2)`, its normalized Fourier kernel factors as

`kappa_v(theta)=exp(i theta/2) rho(theta)` with `rho(theta)>=0`.

The prime-ratio coefficient at frequency `lambda` therefore has the form `c_lambda=exp(iH lambda/2)b_lambda` with `b_lambda>=0`. When the finite-start error is grouped by the exact difference frequency `xi=lambda-mu`, every representation of that same `xi` carries the identical phase. Its shell coefficient is

`B_xi=sum_(lambda-mu=xi) b_lambda b_mu >=0`.

Thus **multiplicity inside one exact difference shell reinforces rather than cancels**. Coupling determinant fibers before scalarization is not by itself a signed resource: for this admissible taper class, all fibers landing on the same `xi` add positively. The long-start Cesàro error energy is exactly `sum_(xi!=0) B_xi^2 sinc^2(L xi/2)`, so any uniform small-error theorem must in particular control this shell `l^2` mass.

At the dangerous collision scale `|xi|=O(y^-2)`, every subquadratic start window `L=o(y^2)` has `sinc(Lxi/2)=1+o(1)`. The window therefore does not suppress those shells either. The remaining dephasing resource must come from **packing/spreading the positive shell masses, interference between genuinely distinct `xi`, or a taper whose centered Fourier transform changes sign**.

**Boundary.** Sign-changing or nonsymmetric tapers can carry different within-shell phases and remain open. VIS-203 does not estimate `sum B_xi^2`, improve the VIS-202 square-root-log method threshold, or prove a lower bound on the true finite-start horizon.