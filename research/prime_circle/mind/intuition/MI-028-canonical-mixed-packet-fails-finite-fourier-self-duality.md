# MI-028 — The canonical mixed-conductor packet fails finite-Fourier self-duality

**Evidence level:** exact-derived source-specific obstruction from [PC-312](../../findings/PC-312-mixed-conductor-periodic-packet-fails-finite-fourier-self-duality.md), sharpening the classicalization of PC-311.

PC-311 leaves the direct bilinear mixed-conductor Poisson pairing as an exact-period `N=qr` periodic coefficient `d` whose Mellin transform is a finite bundle of ordinary Dirichlet `L(s+t,chi)` functions. A residual possibility is that the **particular coefficient vector forced by the canonical Prime-Circle sources** might be a finite-Fourier eigenvector, causing those classical components to recombine into a scalar degree-one Riemann-type functional equation.

PC-312 rules this out exactly. Centering forces

`d(k)=0` whenever `(k,N)>1`,

so in particular `d(q)=d(r)=0`. But the normalized finite Fourier transform can be written explicitly as the symmetrized CRT tensor of the original source values, and for the canonical centered prime-support sources

`(F_N d)(q)=(F_N d)(r)=2/sqrt(N)`.

Therefore `F_N d` is not proportional to `d`. The coefficient has exact period `qr`, so the classical finite-Fourier characterization of even periodic degree-one Dirichlet series applies at the intrinsic conductor and excludes a source-native scalar self-dual functional equation for this packet.

The deeper audit is that **classicalization and self-duality are separate gates**. A mixed packet may already be a classical finite `L`-bundle, and the source weights can still fail the extra modular/Fourier compatibility needed to close that bundle into one scalar functional equation. Here the failure is visible at support level: the source packet vanishes at nonunit residues precisely where its Fourier dual is nonzero.

A surviving mixed-conductor route must therefore retain more than the scalar periodic packet. Natural possibilities left open by the finding are a vector/matrix object that keeps both `d` and `F_N d`, a source-forced coupling of that pair before scalarization, or a genuinely nonlinear/non-circulant construction whose transform does not reduce to the PC-311 coefficient class.

**Boundary.** This is a no-go for the canonical scalar packet `D_d` at product conductor, not for all periodic Dirichlet series or all mixed-conductor constructions. Manually symmetrizing `d` with its Fourier dual would require an independent Prime-Circle reason before it could count as source-native structure.