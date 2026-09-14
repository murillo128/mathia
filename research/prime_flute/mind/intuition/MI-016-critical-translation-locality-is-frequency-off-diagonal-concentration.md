# MI-016 — Both translation locality and the sharp physical direct-angle route are obstructed

**Evidence level:** exact necessary-condition reduction and tail obstruction from PF-337--PF-341, sharpened by the direct canonical-correlation obstruction [PF-342](../../findings/PF-342-sharp-physical-cutoff-forces-order-one-direct-angle-correlation.md). This rules out the current sharp fixed physical `L/H` split as a compact/Hilbert--Schmidt completed-angle architecture; it does not rule out a materially different splitting or observable.

PF-337--PF-341 show that the normalized-insertion translation route fails because the symmetric two-pant self-DtN contrast required to be `o(w_n)` is instead positive on both adjacent pants and diverges relative to the seam scale.

PF-342 shows that bypassing translation and attacking the direct angle does not save the same hard physical split. With cutoff `kappa` and boundary period `L`, the adjacent lattice frequencies

`xi_L=2pi floor(kappa L/(2pi))/L`,

`xi_H=xi_L+2pi/L`

lie on opposite sides of the cutoff while converging to each other. On the collapsing finite--finite corridor their normalized cosine traces are therefore almost identical. The symmetric combination has nonzero corridor value and DtN energy of order `1/(sL)`; the difference inherits the `2pi/L` frequency gap and has only `O(1+1/(sL^3))` energy. Since `sL->0`, polarization forces the low/high matrix element itself to be order `1/(sL)`.

Zero twist gives the same sign on the two adjacent pants. In the symmetric seam-parity channel the seam energy is negligible on this fixed band, so the raw low/high canonical correlation stays above a constant `rho_0`. Choosing tail modules separated by at least three indices yields arbitrarily many orthogonal witnesses. Hence the direct angle has singular values bounded below uniformly along arbitrarily large finite sections and is not compact.

The reusable mechanism is a **hard-boundary aliasing obstruction**: a fixed physical threshold separates two Fourier modes whose physical frequencies differ by the vanishing lattice spacing, while the local PDE cannot distinguish them on the collapsing region. Compact off-diagonal angle decay is therefore incompatible with that sharp partition.

A viable continuation must change a load-bearing part of the representation. A smooth or scale-dependent decomposition would have to prevent adjacent near-identical modes from becoming opposite hard sectors and then rederive the completed operator/trace-ideal statement in that new geometry. Alternatively the final observable must not require compact suppression of this canonical low/high correlation.

**Boundary.** PF-342 is specific to the canonical sharp fixed physical cutoff and its completed angle. It does not prove that every frequency decomposition or every geometric spectral invariant has the same obstruction.
