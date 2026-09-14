# MI-017 — Scalar zero-order boundary stress needs Pohozaev regularity, not a mixed Hadamard theorem

**Evidence level:** supported by PL-297--PL-305, sharpened by PL-306 and [PL-307](../../findings/PL-307-fractional-pohozaev-virial-stress.md). Pohozaev-admissibility of the actual completed-Weil branch, the finite-`s` dilation pairing, source-structured derivative convergence, and the rational-prime sign theorem remain open.

PL-297 separates renormalized boundary stress from the critical Fourier first moment. PL-298--PL-304 show that generic spectral stability and ordinary forcing norms do not make the logarithmic resolvent a `BV` smoother. PL-305 then removes the kernel-side concern: once a fixed state lies in `C_0 cap BV_0`, every prime-power activation and the completed remainder are already first-order differentiable in the aperture.

PL-306 showed that squared boundary-stress compactness is not an independent gate if one has both Feynman--Hellmann and a mixed moving-domain fractional Hadamard law. PL-307 shortens the route further: the mixed Hadamard theorem itself is unnecessary for the scalar stress.

For a regularized eigenstate satisfying Ros-Oton--Serra's fractional Pohozaev hypotheses and the lower-order dilation pairing,

`2 Re<xw',B_a w> = -b_a(w)-a partial_a b_a(w)`,

the fixed-domain Pohozaev identity plus the eigen-equation gives exactly

`Gamma(1+s)^2/(2s) (|tau_+|^2+|tau_-|^2) = E_s(w) - a^(2s+1) partial_a b_a(w)`.

No eigenvalue derivative or moving-boundary shape theorem enters this identity. If the branch has a finite zero-order limit and `partial_a b_a(w_(s,a)) -> partial_a b_a(w_(0,a))`, then `E_s(w)->1` and

`lim_(s->0) (|tau_+|^2+|tau_-|^2)/(2s) = 1-a partial_a b_a(w_0)`.

Zero-order Feynman--Hellmann, when valid, then identifies the right side with `-a lambda_0'(a)`.

The analytic frontier is therefore **source-structured regularity of the actual state**: prove enough boundary/interior regularity for the existing Pohozaev theorem, justify the lower-order virial pairing, and pass PL-305's explicit derivative through `s->0`. A full mixed fractional/completed-Weil Hadamard theorem should not be pursued merely to recover the scalar endpoint-square quantity.

The arithmetic sign gate remains independent. Even a perfectly defined squared stress only identifies the derivative; a closing argument must still constrain its sign through rational-prime source structure strongly enough to control the first crossing.

**Boundary.** PL-307 does not prove Pohozaev regularity, finite-`s` virial admissibility, BV compactness, signed/pointwise boundary traces or an RH mechanism. Moving-domain shape calculus can remain relevant for stronger boundary data beyond the scalar squared stress.
