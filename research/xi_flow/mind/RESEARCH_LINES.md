# Xi-flow research lines

This file holds the current mathematical questions suggested by the durable Xi-flow intuitions. It is not a roadmap, task queue, status page, or history.

## Turn local nonlinear holomorphic packet charts into unknown-support source coercivity

**Linked intuitions:** `MI-004-endpoint-prime-free-fourier-sector-is-volterra-triangular`, `MI-008-gaussian-reference-localization-is-relatively-exact-but-not-global`, `MI-011-cross-scale-observability-can-compress-to-one-off-circle-heat-trace`, `MI-012-xi-tail-hazard-is-source-specific-but-not-yet-coercive`, `MI-013-adapted-cusp-coordinates-separate-depth-from-conditioning`.

XF-154--XF-184 separate exact source identification, adaptive depth, inverse conditioning, and positive-real versus holomorphic acquisition. Fixed known packets can be acquired uniformly with mesoscopic complex Jacobi samples even when positive-real observations are exponentially ill-scaled.

XF-185 shows that growing packet complexity is not a local linear-conditioning barrier. For a known consecutive packet with `2<=m<=N`, an explicit Fejer-overcomplete bank of `O(m)` complex samples has singular values `asymp sqrt(m)` with constants uniform in remote location `N` and packet width `m`.

XF-186 upgrades that frame to a genuine nonlinear chart. On the normalized cube `||h||_infty<=kappa/m`, corresponding to constant-size physical lattice displacements, the same holomorphic bank is uniformly bi-Lipschitz with constants independent of `N` and `m`; reciprocal Jacobi contamination remains exponentially negligible. Once the ambient consecutive window is known, zero and nonzero atom displacements inside it can therefore be recovered together without a local nonlinear conditioning loss.

The live theorem is now genuinely global: locate and recenter unknown packet windows without an oracle, control several separated or multiscale packets and regimes such as `m>>N`, handle weight uncertainty only where source-admissible, justify the required complex samples directly from the physical Xi/Jacobi source, and transport the recovered source control to a zero-sensitive quantity rather than merely reconstructing the theta-side deformation.

## Treat sample complexity, local nonlinear conditioning, support search, and source access as different currencies

In the holomorphic category, lattice-scale packet complexity costs linearly many measurements but does not worsen either the linear condition number or the local nonlinear inverse on a constant physical cell. Future obstructions must target support discovery, global assembly, source-side analytic access, or the bridge to Xi-zero control rather than remote known-packet conditioning.

## Which source-derived calibration information makes singleton detection uniformly finite?

[MI-014](intuition/MI-014-endpoint-preserving-calibration-joins-force-sharp-randomized-stopping-tails.md) retains a separate obstruction even when the singleton source window is known. For the complete Jacobi response, the exact threshold is `L_*=min_tau |F_tau'(Q)|/2`. An unknown positive slack `delta=L_*-||B'||_infinity` admits exact input-dependent finite stopping with a known total squared-noise cap, but XF-204 forces `sup_x P(nu_x>N)>=1-2 alpha` for every finite `N` when per-input error is at most `alpha<1/2`. Its endpoint-preserving complex join prevents a value query at `Q` from removing the obstruction.

Can physical source access supply a positive slack floor or a calibration law that excludes the source-plus-polynomial directions in [MI-015](intuition/MI-015-positive-noise-retains-analytic-calibration-stopping-obstruction.md)? XF-205's noisy obstruction already uses only `B=±(1-epsilon)F/2`; that known direction is one-query identifiable without noise. XF-206 closes the noiseless full holomorphic class by adding `P_a=sum_(k<N) a_k ((r-Q)/Q)^(2k)`. For `v=|F'|`, the exact speed decrease `kappa=min_I(-v')>0` permits a coefficient region `sum_(k>=1) 2k|a_k|<=kappa Q^2/4` independent of the shrinking slack. Every distinct `N`-query bank has independent evaluation rows, including the endpoint. Small Gaussian priors conditioned into that region make finite transcript laws arbitrarily close as `epsilon->0`. Capped minimax error `1/2` and the sharp tail `1-2 alpha` therefore survive at zero noise as well. The polynomial dimension grows with the cap; this does not rule out a smaller prescribed calibration model.

With a supplied slack floor, XF-203's sufficient certificate remains concrete: `C Q^(-3/2)h+2 sigma sqrt(2/n)/h<delta` for distinct-row differences near `Q`. The source-derived calibration separation, exact threshold and coordinate/precision access remain separate from local nonlinear conditioning and from any Xi-zero implication.
