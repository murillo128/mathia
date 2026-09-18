# MI-031 — The centered prime endpoint is a classical Riesz zero spectrum before completion

**Evidence level:** literature-backed exact synthesis from [PL-344](../../findings/PL-344-bounded-modulation-pnt-edge-cancelled-by-pole.md) and [PL-345](../../findings/PL-345-schur-endpoint-log-riesz-zero-spectrum.md). The explicit-formula/Riesz mechanism is classical; the Mathia content is its identification inside the Prime-Lattice endpoint channel and the exact completion mismatch.

After subtracting the PNT continuum from the outer prime endpoint response, PL-345 identifies the surviving residual with the classical first logarithmic Riesz mean. For fixed bounded modulation `tau`,

`R_a(tau) = -e^(2ia tau) sum_rho e^((2rho-1)a)/(rho+i tau)^2 + O_T(ae^-a)`,

and the Prime-Lattice outer-shell residual satisfies `E_a(tau)=R_a(tau)+o_T(1)`.

This gives a precise scale dictionary. A zero `rho` contributes with exponential weight `e^((2 Re rho-1)a)`, so the critical line `Re rho=1/2` is exactly the neutral square-root scale. At `tau=0`, boundedness of the centered Riesz residual as `a->infinity` is already equivalent to RH. The critical scale therefore appears naturally in the centered prime channel, but **its first exact appearance is a classical RH-equivalent observable, not an independent coercive mechanism**.

PL-345 also prevents identifying that prime residual with the fully completed Weil endpoint form at `O(1)` precision. The exact pole contribution and the PNT continuum differ by `3a-1+o(1)`, which is larger than the bounded zero signal on RH scale. Archimedean and scalar completion terms must therefore be retained before the centered prime residual can be used to infer a completed operator sign.

The useful frontier is no longer to discover the zero spectrum of the centered prime endpoint; that spectrum is explicit. The missing theorem must control the exact completed same-state form and explain how the Riesz zero signal competes with the pole/archimedean correction and the unbounded logarithmic principal energy.

**Boundary.** The Riesz expansion does not prove RH, completed coercivity, or a negative direction. Its boundedness criterion is already equivalent to RH, and the `O(a)` completion mismatch prevents treating the prime-centered residual alone as the completed destination observable.