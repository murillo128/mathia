# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Replace one-notch source coercivity by a destination-level carrier-band obstruction

**Linked intuitions:** `MI-062-the-critical-ford-mark-is-a-growing-moment-observable`, `MI-063-demodulated-ford-energy-is-bandlimited-at-the-window-scale`, `MI-064-signed-scalar-coherence-shrinks-only-by-paying-total-variation`, `MI-065-signed-carrier-cost-must-be-measured-after-quotienting-unresolved-microscopic-dipoles`, `MI-066-resolved-carrier-channels-can-amortize-hilbert-cancellation-at-j-two-thirds`.

NB-245--NB-250 fix the representation and order of operations. The Ford-scaled Cauchy pole must be Hardy-projected through positive Mellin frequencies before Hilbert-space squaring; the remaining second moment is a positive carrier-band form factor with natural width `Theta(H)=Theta(X/J)`.

NB-251--NB-255 progressively show that carrier widening has a coherence cost: literal shell dilation changes the effective population, equal-weight combs create a `1/W` peak, arbitrary positive mixtures retain a compulsory `Theta(1/W)` window, and signed/complex mixtures with Euler-normalized total variation `V` retain a worst-case coherent disk of radius `c/(WV)`. NB-256 then shows why raw `V` is not a physical norm: microscopic opposite dipoles can make it arbitrarily large while changing neither the synthesized source nor the Ford-scale carrier appreciably.

NB-257 tests the most concrete repair, an `H`-separated carrier dictionary. Separation makes the translated shells disjoint, so source `L^2` is genuinely coercive on coefficient `ell^2`. Yet a filled `K`-channel grid can create one order-one Ford-scale notch with minimum shell-Hilbert cost `Theta(J/K^(3/2))`. The threshold `K~J^(2/3)` is sharp: at that scale the source Hilbert cost is only order one while `W/R~J^(-1/3)->0`. The construction is physically resolved and pays `WV~R`, so this is not the microscopic-dipole artifact of NB-256.

The scalar frontier has therefore moved beyond asking for a resolution-sensitive source norm that prices a **single** Ford-scale cancellation. `H`-separation supplies such a norm, but Hilbert geometry can amortize one notch over sufficiently many resolved channels. The live question is whether the actual destination requires a stronger object that cannot be amortized at the same cost: a family of Ford-scale interpolation constraints, suppression of the full positive carrier-band form factor, or the Hardy-projected Nyman norm itself. Any claimed obstruction must be proved after the legal projection rather than imported from `L^1` or transport geometry.

## Keep carrier coherence, physical source cost and the final Hardy/Nyman energy separate

NB-250 gives a sufficient full-line carrier-energy route, not an equivalence. NB-255 supplies a worst-case coherence radius from span and variation; NB-256 removes unresolved coefficient artifacts; NB-257 shows that even after making coefficient geometry physical, a single-notch Hilbert cost has a `J^(2/3)` channel-count crossover.

Future signed-scalar arguments must therefore state the Euler normalization, carrier span, working resolution, channel separation/conditioning, smooth-shell synthesis norm, number and geometry of imposed Ford-scale constraints, and the destination projection. A divergent `L^1` or transport cost is not automatically a Hilbert obstruction, while bounded source `L^2` for one notch is not evidence that a whole carrier band can be suppressed. The missing theorem is now explicitly multi-constraint or destination-level.