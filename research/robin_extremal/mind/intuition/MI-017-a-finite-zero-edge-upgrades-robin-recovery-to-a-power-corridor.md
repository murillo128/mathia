# MI-017 — A finite zero edge upgrades Robin recovery to the true Theta-scale power corridor

**Evidence level:** exact consequence of the strengthened [RE-112](../../findings/RE-112-finite-zero-edge-forces-power-scale-robin-recovery-corridors.md), using its persisted truncated explicit-formula and off-line zero-density argument. No contradiction with false RH or density theorem for selected CA blocks is claimed.

Let `Theta=sup Re(rho)`. In the false-RH finite-edge regime `1/2<Theta<1`, RE-112 improves the textbook `x^Theta log^2 x` envelope. A fixed strip strictly to the right of the critical line has sublinear zero density, so its reciprocal-ordinate mass is summable; combining that with the truncated Riemann--von Mangoldt formula yields

`psi(x)-x = O_Theta(x^Theta)`.

The full CA event sweep therefore satisfies `Phi(x)=x+O_Theta(x^Theta)`. Inserting this **true Theta-scale source envelope** into RE-110's exact one-sided recovery workload gives, for a positive CA state at scale `Y` recovering to a later nonpositive state at `V`,

`V-Y >>_Theta h(C) Y^(2-Theta) log Y`.

For adaptive quantitative false-RH witnesses with `h(C) >> Y^(-b)`, this becomes

`V-Y >>_(Theta,b) Y^(2-Theta-b) log Y`.

Choosing `b=1-Theta+eta` gives almost-linear spacing `Y^(1-eta) log Y` and fixed-`eta` dyadic packing `O_(Theta,eta)(T^eta/log T)`. The logarithm now helps separation rather than being lost to a coarse PNT envelope.

RE-112 also sharpens the source-side saturation statement. If a short recovery is within a constant factor of this minimum, then a fixed positive fraction of the crossed physical mass must come from ordinary first-layer primes with

`p-vartheta(p) asy Y^Theta`

and the recovery-favorable sign. The required packet has at least `gg h(C)Y^(2-Theta)` distinct primes. Thus improving the finite-edge frontier means ruling out **CA-selected one-sided saturation of the actual Theta-scale prime-source envelope**, not repairing a logarithmic artifact.

This changes the meaning of the RE-111 Korobov--Vinogradov obstruction. The unconditional KV minimum is only the right source scale in the extreme branch `Theta=1`. For every fixed `Theta<1`, the zero-edge source law already forces a polynomially larger recovery corridor; the live question is whether zero density/phase or another selected-corridor coordinate forbids saturation of the `Y^Theta` workload itself.

The reusable split is spectral. **Finite zero edge (`Theta<1`)** gives a genuine power corridor at the sharp source exponent and isolates a same-sign first-layer saturation packet on that scale. **Extreme edge (`Theta=1`)** leaves the unconditional RE-109--RE-111 KV saturation problem alive.

**Boundary.** The exponent `Theta` is the source scale extracted from edge location plus the persisted zero-density input; improving the corridor exponent requires information beyond the scalar edge. The packing estimate is for a fixed quantitative family selected by `b`/`eta`, not a simultaneous `T^(o(1))` theorem for all witnesses.