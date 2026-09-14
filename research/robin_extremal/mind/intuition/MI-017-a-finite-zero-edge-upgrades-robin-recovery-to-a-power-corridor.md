# MI-017 — A finite zero edge upgrades Robin recovery to a phase-locked power corridor

**Evidence level:** exact consequence of [RE-112](../../findings/RE-112-finite-zero-edge-forces-power-scale-robin-recovery-corridors.md) and [RE-113](../../findings/RE-113-edge-zero-phase-locking-rules-out-sublinear-minimal-robin-recovery.md), using the persisted truncated explicit-formula and off-line zero-density inputs. No contradiction with false RH or density theorem for selected CA blocks is claimed.

Let `Theta=sup Re(rho)`. In the false-RH finite-edge regime `1/2<Theta<1`, RE-112 first replaces the textbook `x^Theta log^2 x` bound by the log-free envelope

`psi(x)-x = O_Theta(x^Theta)`

and transfers it to the full CA event sweep. RE-110 then forces the scalar recovery corridor

`V-Y >>_Theta h(C) Y^(2-Theta) log Y`.

RE-113 shows that the scalar envelope still discards decisive information. The same high-strip reciprocal summability projects the normalized source onto the actual rightmost zero face:

`x-vartheta(x) = x^Theta(F_Theta(log x)+o(1))`,

where `F_Theta` is the absolutely convergent real almost-periodic sum over zeros with `Re rho=Theta`; the full CA event sweep has the same leading profile. The adaptive RE-034 selector locks this phase to the selected Robin height:

`F_Theta(log Y) = b h(C) Y^(1-Theta) log Y + o(1)`.

This has an important dynamical consequence. If the first recovery is genuinely sublinear, `V-Y=o(Y)`, the scalar corridor already forces the dimensionless height `lambda_Y=h(C)Y^(1-Theta)log Y` to tend to zero. The selector phase therefore tends to zero as well, and uniform continuity makes every crossed event see the same vanishing edge phase. Hence the forward workload is `o(Y^Theta)`, not merely `O(Y^Theta)`, and

`V-Y = omega(h(C) Y^(2-Theta) log Y)`.

So **sublinear selected recoveries cannot saturate the scalar finite-edge minimum**. If a fixed-constant near-minimal family exists under the short condition `V-Y<=Y`, it must instead be macroscopic and edge-amplitude:

`h(C) asy Y^(Theta-1)/log Y`, `V-Y asy Y`, and `F_Theta(log Y) asy 1` with the favorable sign. If the supremum `Theta` is not attained by a zeta zero, `F_Theta` vanishes identically and such a near-minimal family is impossible.

This refines the RE-112 first-layer packet frontier. The live finite-edge obstruction is no longer merely a positive-mass packet with `p-vartheta(p) asy Y^Theta`; near-minimal recovery requires an **attained edge line, a positive edge phase at the adaptive selector, full spectral-scale Robin height, and macroscopic recovery**. The natural next source test is recurrence of that phase-lock, preferably coupled to the reciprocal-Mertens coordinate already tied to the same selector in RE-034.

The reusable split is now sharper. **Finite zero edge (`Theta<1`)** has a phase-resolved source law: sublinear recovery is automatically super-minimal, while fixed-constant near-minimal recovery is forced to macroscopic edge amplitude. **Extreme edge (`Theta=1`)** still leaves the unconditional RE-109--RE-111 Korobov--Vinogradov saturation problem alive.

**Boundary.** The almost-periodic organization of prime-counting errors is classical; the durable Mathia content is the selector-conditioned phase lock and its recovery consequence. The fixed-constant qualifier is essential in the near-minimal statement, and none of these estimates combines varying `b`/`eta` families into a single uniform counting theorem.