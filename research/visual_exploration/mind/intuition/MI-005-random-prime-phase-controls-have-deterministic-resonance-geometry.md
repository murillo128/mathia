# MI-005 — Prime-phase geometry is controlled by the exact sampling null and filtered energy

**Evidence level:** exact finite-dimensional null law, classical Kronecker/Gram equidistribution, exact window-energy controls, and local Gram-spacing controls through VIS-085

## Core intuition

Prime-phase pictures are meaningful only after the sampling law and the window filter are modeled exactly. Long vertical averaging already gives Haar on every fixed finite prime torus, and VIS-083 shows that replacing ordinary heights by Gram points does not change that population law. Conversely, short consecutive Gram blocks do not look Haar because the sampling clock itself freezes the phases; VIS-084 identifies the logarithmic Gram-count scale at which the cloud first opens into a deterministic local arc.

VIS-085 makes the control robust to broad growing support. Once that first-order arc is subtracted, the residual clock curvature vanishes uniformly across all primes up to `P_n` whenever `H_n^2 log P_n=o(g_n (log g_n)^3)`. Thus visually interesting clustering or motion must survive the **correct deterministic sampling null**, not just differ from an iid picture.

## Strongest justified principle

VIS-067--VIS-071 determine the fixed-support shared-phase law and show that deterministic prime flow has the same long-average Haar distribution. VIS-072--VIS-082 then separate signed support, small divisors, coefficient mass, and actual finite-window energy. For the signed triangular Euler witness, the exact normalized energy threshold is `log X/L`: certificate growth and tiny reciprocal frequencies can coexist with vanishing observable energy.

VIS-083 adds Gram population control. Every fixed collection of prime phases sampled over all Gram points is Haar-equidistributed. VIS-084 adds local control: if a consecutive Gram block has `H=o(log g_n)`, it collapses to its starting phase; if `H=O(log g_n)`, its first-order geometry is an explicit torus arc with velocity proportional to `(log p)_p/log g_n`.

VIS-085 subtracts that arc and bounds the remaining coordinatewise error by `H_n^2 log P_n/[g_n (log g_n)^3]`. At logarithmic block length, every polynomial and much larger prime cutoff remains in the collapsing regime. Growing dimension alone is therefore not a new local information source.

## Counterevidence / boundary

The results do not prove growing-dimensional Haar equidistribution, classify blocks much longer than `log g_n`, or remove coordinates such as Gram occupancy, `Z(g_n)`, derivatives, nearby-zero geometry, or another source field not determined by prime phases. Statistics whose Lipschitz constants grow strongly with dimension also require their own normalization.

## Epistemic status

**Exact control of the declared finite-Euler energy and fixed/logarithmic Gram sampling regimes; longer blocks and genuinely additional coordinates remain open.**

## Falsification criterion

Find a fixed-prime Gram population violating VIS-083, a sublogarithmic block whose phase diameter stays macroscopic, or an arc-corrected logarithmic block inside the VIS-085 support corridor with nonvanishing coordinate residual. A positive visual route must instead demonstrate residual structure after the exact sampling/energy null appropriate to its scale.