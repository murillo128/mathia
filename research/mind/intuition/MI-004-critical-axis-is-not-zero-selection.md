# MI-004 — A canonically selected critical axis is not a zero-selection theorem

**Evidence level:** supported by the exact dilation/Gram/Hilbert constructions in Prime Circle, Weil Positivity and [PL-366](../../prime_lattice/findings/PL-366-l2-pole-neutral-filter-square-root-no-go.md). No zero-location statement is inferred from the shared exponent.

The compatible punctured-plane power-map tower splits as `R x Sigma_Q`. Its radial coordinates satisfy `x_n=x_1/n`; the solenoid does not supply an additional radial constraint. On Haar `L^2(dx dmu)`, raw pullback by `(x,sigma)->(nx,D_n sigma)` has norm `n^-1/2`, so unitary normalization forces the half-density. The resulting dilation generator has continuous spectrum. Formally summing the integer pullbacks displays `zeta(1/2-it)`, but that sum is not a bounded operator and does not supply a discrete zero-selecting spectrum.

The distinction persists when prime-local critical weights are present exactly. Weil-positive Gram constructions can carry the same `p^-1/2` local scaling with inequivalent mixed-prime laws, so the half-density does not determine the global pairing. Prime Circle adds a stronger warning: ordinary downstream Green inversion can canonically force a Hilbert-matrix boundary at `Re(s)=1/2` for an entire periodic coefficient class. The source-specific packet changes vectors inside the Hilbert space; it does not arithmeticize the boundary.

PL-366 now supplies the coefficient-space version directly. For every pole-neutral divisor filter `c in ell^2`, with `b=c*1` and `C(1)=0`, Cauchy--Schwarz gives

`sum_(n<=x)b_n=O(sqrt(x)||c||_2)`.

The output Dirichlet series therefore converges on `Re(s)>1/2`. This half-plane appears for the whole pole-neutral Hilbert class because the floor-function residual has `ell^2` norm `O(sqrt x)`. Hypothetical off-line zeta zeros are merely inherited by `B(s)=zeta(s)C(s)`; no sign, positivity or spectral law forces them onto the boundary.

So canonicality is not the missing criterion. A geometry, normalization or ambient norm may naturally select exactly the RH-looking exponent `1/2` while matched controls share the same threshold. The exponent becomes arithmetic evidence only when the construction also proves a source-specific zero/sign/spectral statement that generic members of the same geometry cannot reproduce.

**Boundary.** This synthesis does not say that every appearance of `1/2` is universal or irrelevant. It says that critical scaling, convergence radius and zero selection are separate claims. A source-forced structure may still use a half-density, but it must add a discriminator beyond the ambient operator/Hilbert threshold itself.
