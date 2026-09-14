# MI-017 — A finite zero edge upgrades Robin recovery from KV scale to a power corridor

**Evidence level:** exact consequence of [RE-112](../../findings/RE-112-finite-zero-edge-forces-power-scale-robin-recovery-corridors.md) using the classical `Theta`-conditioned PNT envelope already persisted there. No contradiction with false RH or density theorem for selected CA blocks is claimed.

Let `Theta=sup Re(rho)`. When `Theta<1`, the classical explicit-formula bound `psi(x)-x=O_Theta(x^Theta log^2 x)` transfers to the full CA event sweep. Combining that source envelope with RE-110's exact one-sided workload identity gives, for a positive CA state at logarithmic scale `Y` recovering to a later nonpositive state at `V`,

`V-Y >>_Theta h(C) Y^(2-Theta) / log Y`

up to the harmless long-corridor branch.

For the adaptive quantitative false-RH witnesses with `h(C) >> Y^(-b)`, this becomes

`V-Y >>_(Theta,b) Y^(2-Theta-b) / log Y`.

Choosing `b=1-Theta+eta` yields almost-linear spacing `Y^(1-eta)/log Y` and at most `O(T^eta log T)` selected blocks with `Y in [T,2T]` for that fixed `eta` family.

This changes the meaning of the RE-111 packet obstruction. The Korobov--Vinogradov envelope is only the right minimal-recovery currency in the extreme branch `Theta=1`. For every fixed `Theta<1`, an unbounded family of recoveries at the unconditional KV minimum is already impossible: the zero-edge PNT envelope forces a polynomially larger corridor before any same-sign saturation-packet theorem is needed.

The reusable split is therefore spectral. **Finite zero edge (`Theta<1`)** moves the frontier to whether additional zero-density/phase or source information can improve or forbid saturation of the `Y^Theta` workload on the CA-selected corridors. **Extreme edge (`Theta=1`)** leaves the unconditional RE-109--RE-111 first-layer KV saturation problem alive.

**Boundary.** The exponent `Theta` itself is the classical sharp scale available from zero-edge location alone; improving the corridor exponent requires information beyond the scalar edge. The dyadic packing estimate applies to the fixed quantitative family selected by a chosen `b` (or `eta`), not simultaneously to all witnesses and not as a `T^{o(1)}` theorem for one fixed family.
