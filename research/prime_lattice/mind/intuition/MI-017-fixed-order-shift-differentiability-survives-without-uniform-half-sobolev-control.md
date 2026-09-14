# MI-017 — Zero-order Hadamard stress has two independent analytic gates, not three

**Evidence level:** supported by PL-297--PL-305 and sharpened by [PL-306](../../findings/PL-306-hadamard-stress-virial-residual.md). The mixed fractional/completed-Weil Hadamard identity, uniform `C_0+BV`/derivative-measure control for the actual branch, and the rational-prime sign theorem remain open.

PL-297 separates renormalized boundary stress from the critical Fourier first moment. PL-298--PL-304 show that generic spectral stability and ordinary forcing norms do not make the logarithmic resolvent a `BV` smoother. PL-305 then removes the kernel-side concern: once a fixed state lies in `C_0 cap BV_0`, every prime-power activation and the completed remainder are already first-order differentiable in the aperture.

PL-306 now shows that **squared boundary-stress compactness is not a third independent gate**. Suppose the regularized branch has both a fixed-domain Feynman--Hellmann identity and the correct moving-domain fractional Hadamard identity. Their comparison gives the exact finite-`s` virial relation

`Gamma(1+s)^2/(2s) (|tau_+|^2+|tau_-|^2) = E_s(w) - a^(2s+1) partial_a b_a(w)`.

If the branch has a finite zero-order limit and the lower-order derivative passes to the limit, then `E_s(w)->1`, so

`lim_(s->0) (|tau_+|^2+|tau_-|^2)/(2s) = 1-a partial_a b_a(w_0) = -a lambda_0'(a)`

whenever zero-order Feynman--Hellmann is valid. On the even branch, the individual squared trace is fixed as well.

The analytic frontier is therefore cleaner. One must prove the **actual mixed Hadamard/Feynman--Hellmann law** and prove source-structured state regularity strong enough to pass PL-305's derivative formula through `s->0`. Once those hold, the scalar squared stress that enters the eigenvalue shape derivative follows algebraically; a separate compactness theorem for the renormalized trace is needed only for signed/pointwise boundary data beyond that scalar.

The arithmetic sign gate remains independent. Even a perfectly defined stress only identifies `-a lambda_0'(a)`. A closing argument must still constrain that derivative through rational-prime source structure strongly enough to control the first crossing.

**Boundary.** PL-306 is a conditional gate reduction, not a proof of the mixed Hadamard formula, branch differentiability, BV compactness or an RH mechanism.
