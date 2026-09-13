# MI-012 — Raw seam amplification does not prevent intrinsic direct-angle stability

**Evidence level:** exact for the two-metric raw-block obstruction of PF-319 and the positive-form angle perturbation theorem of PF-320, with PF-242 providing an independent coefficient-locality control. PF-320 controls the hypercycle-shear correction to the physical direct angle; it does not prove the shear-deleted reference angle or the independent conditional channel `T_H` is weak trace class.

PF-319 remains a real warning about the **wrong target**. Corridor-relative Loewner smallness does not control a raw mixed block after normalization by an unrelated seam metric: an external congruence can amplify a small relative perturbation arbitrarily. Thus no theorem should infer a seam-normalized `K_LH` estimate merely from the PF-232 corridor sandwich.

PF-320 shows why the actual PF-315/PF-317 direct angle is better behaved than that raw block. For a positive low/high block form

`M = [[A,B],[B*,C]]`,

the intrinsic angle is `T=A^(-1/2)BC^(-1/2)`. If two whole positive forms satisfy a multiplicative sandwich `(1-epsilon)M_0 <= M_1 <= (1+delta)M_0`, then after harmless low/high unitaries their angles differ by `O(max(epsilon,delta))`, **independently of anisotropy in any common external seam normalization**. The form's own diagonal energies absorb the amplification that defeats the raw-block shortcut.

For the canonical hypercycle shear, PF-232 has `beta_n=O(P_n^-1)` and the local retained low rank is `O(1+log P_n)`. PF-320 therefore gives directly

`||T_(1,n)-T_(0,n)||_(S_2)^2 = O((1+log P_n)/P_n^2)`,

up to sectorwise unitaries. This is exactly the PF-318 endpoint budget. Moreover sums of positive local pant forms reassemble through a contraction sandwich of the orthogonal direct sum of their intrinsic angles, so the local shear-error estimate survives global assembly without returning to the raw mixed precision block.

The direct-channel frontier is consequently narrower than after PF-319. **The shear correction is already endpoint-small at angle level.** What remains is the weak-`S_1` envelope for the **shear-deleted local pant angles** with actual seam energy and common finite-pant completion retained; once that reference family is controlled, the shear error can be added perturbatively. PF-242's exponential Jacobi locality remains useful structure but is no longer required merely to bridge the PF-232 shear through the seam metric.

**Boundary.** PF-320 uses multiplicative order of the complete local positive forms and a common normalization/completion; an additive error in an unrelated metric does not suffice. It gives a sufficient local-to-global route, not a characterization, and does not control `T_H`, the shear-deleted reference family, scattering, determinants or RH.