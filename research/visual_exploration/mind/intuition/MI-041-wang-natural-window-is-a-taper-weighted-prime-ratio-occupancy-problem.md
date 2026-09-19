# MI-041 — Wang natural windows reduce to fixed-gap prime-pair runs, and only subpolynomial run length remains hard

**Evidence level:** exact/literature-backed synthesis from `VIS-313`--`VIS-324` plus classical rational mechanical/Christoffel geometry and the classical dimension-two Selberg upper-bound sieve. No prime-pair asymptotic or RH consequence is claimed.

The cutoff-free Wang remainder has no useful global nearest-frequency spacing, but dyadic shells reduce the finite-window loss to prime-ratio occupancy with destination taper. VIS-317--VIS-319 identify the faithful coordinates: scalar determinant projection erases the two prime exclusions, while the unimodular Bézout chart preserves both of them exactly.

VIS-320--VIS-322 compress the surviving geometry. The thin domain has at most three mechanical branches, gate motion can be frozen up to `O(1)` points, and decimation by `k=|v-u|` turns each branch into at most `min(k,L)+1` fixed-gap diagonal runs. This converts path complexity into an explicit fragmentation parameter without losing either primality condition.

VIS-323 shows that fragmentation is arithmetically milder than the run count suggests. Run gaps occupy an interval of width `<k+1`, determinant residue determines the gap residue modulo `k`, and the aggregate Hardy--Littlewood weight satisfies `sum_s ell_s S(g_s) << L+k`. In particular, when `k<=L`, large local singular-series factors cannot accumulate into a new loss.

VIS-324 prices the remaining branchwise sample length. Applying the standard translation-uniform two-linear-form Selberg sieve to the exact runs gives

`P_j << L/log^2(3+L/k) + k`

for every frozen branch with `1<=k<=L`. At the natural Wang scale `L asymp M/log log M`, if `k<=M^(1-delta)` for any fixed `delta>0`, then `L/k` is polynomially large and the bound becomes `P_j <<_delta L/log^2 M`, exactly the required two-prime upper-bound scale.

The load-bearing threshold is therefore sharper than “short runs.” **Every polynomially long run is already long enough for the classical upper-bound sieve.** Any unresolved worst-cell excess must concentrate where `k=M^(1-o(1))`, so `L/k=M^(o(1))`, or in the fully fragmented range `k>L` where most residue classes contain at most one determinant index.

The reusable lesson is that representation fidelity, fragmentation count, local arithmetic factors, per-fragment sample length and cross-fragment aggregation are separate resources. Exact geometry can first make a problem look fragmented, exact averaging can neutralize the local factors, and a classical theorem can then close the entire polynomial-sample regime. What remains is not a need for a stronger theorem on each fragment but a need to **change the unit of averaging** when fragments become subpolynomial or singleton-sized.

For Wang, plausible surviving mechanisms are a multi-run sieve, coefficient-weighted energy estimate, or destination-taper aggregation that couples many short fragments. Each must be tested through the transition `k~L` and into `k>L`; simply applying a fixed-gap theorem independently to each run cannot recover two powers of `log M` once `log(L/k)=o(log M)`.

**Boundary.** VIS-324 is an upper bound only. It proves no prime-pair asymptotic, lower bound, sign/phase estimate, full worst-cell estimate or Wang natural-window theorem. The fixed `delta>0` in the polynomial regime is essential, and the result does not solve `k=M^(1-o(1))` or `k>L`. Its exact contribution is to remove every fixed polynomial power-saving range from the branchwise sieve frontier.