# MI-027 — Direct bilinear mixed-conductor Poisson coupling is only a finite Dirichlet-`L` bundle

**Evidence level:** exact-derived and classicalized by [PC-311](../../findings/PC-311-bilinear-mixed-conductor-poisson-pairing-is-a-finite-dirichlet-L-bundle.md), closing the most direct mixed-conductor escape left by PC-310.

Take centered cyclic source data at distinct conductors `q` and `r`, Poisson-extend each source radially, and form the direct bilinear same-circle pairing. The radial variables do couple, but only through their sum. After passing to the common refinement `Z/(qr)Z`, the angular coefficient is periodic and supported on the units.

That periodic source has an ordinary finite character expansion. Its double Mellin transform is therefore a finite linear combination of classical one-variable Dirichlet functions

`L(s+t,chi)`

with the spectral variables collapsed to `s+t`. Chinese remainder factorization further splits the character coefficients into the corresponding one-level transforms, and the symmetry of the bilinear pairing retains only the expected parity sector.

So the first cross-level construction after PC-310 does not create a genuinely two-variable analytic species, a new functional-equation orientation, or an independent critical-line mechanism. It packages already classical finite periodic arithmetic into a Dirichlet-`L` bundle. The fact that two conductors appear before diagonalization is not enough: the common-refinement algebra still scalarizes the coupling to one classical Mellin variable.

The reusable audit is concrete. A mixed-conductor proposal should be reduced on the common refinement before it is interpreted. If the coupling becomes a periodic coefficient system whose Mellin transform is a finite character bundle in one combined variable, it has not escaped the classical packet algebra. A surviving route must keep genuinely nonseparable conductor information — for example a nonlinear operation before diagonalization, a non-circulant pointed interaction, or another source-forced coupling whose transform cannot be reduced to finitely many ordinary `L(s+t,chi)` factors — and still supply a destination theorem.

**Boundary.** PC-311 treats the direct bilinear Poisson pairing. It does not rule out higher/nonlinear mixed-conductor constructions, non-circulant geometry, or a separate theorem that uses a classical Dirichlet-`L` bundle in a new coercive way.