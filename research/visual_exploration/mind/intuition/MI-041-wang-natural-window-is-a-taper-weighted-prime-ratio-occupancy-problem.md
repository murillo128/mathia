# MI-041 — Wang natural windows reduce to fixed-gap prime-pair runs whose live cost is run length, not singular-series mass

**Evidence level:** exact synthesis from `VIS-313`--`VIS-323` plus classical rational mechanical/Christoffel geometry and classical prime-pair singular-series averaging. No prime-pair asymptotic or RH consequence is claimed.

The cutoff-free Wang remainder has no useful global nearest-frequency spacing, but dyadic shells reduce the finite-window loss to prime-ratio occupancy with destination taper. VIS-317--VIS-319 identify the faithful coordinates: scalar determinant projection erases the two prime exclusions, while the unimodular Bézout chart preserves both of them exactly.

VIS-320--VIS-322 compress the surviving geometry. The thin domain has at most three mechanical branches, gate motion can be frozen up to `O(1)` points, and decimation by `k=|v-u|` turns each branch into at most `min(k,L)+1` fixed-gap diagonal runs. This converts path complexity into an explicit fragmentation parameter without losing either primality condition.

VIS-323 shows that this fragmentation is arithmetically milder than the run count suggests. Run gaps occupy an interval of width `<k+1`, determinant residue determines the gap residue modulo `k`, and the aggregate Hardy--Littlewood weight satisfies `sum_s ell_s S(g_s) << L+k`. In particular, when `k<=L`, the singular-series contribution across all fragments is only `O(L)`. Large local factors cannot by themselves explain the Wang loss in this regime.

The unresolved currency is therefore **effective run length `L/k` and the uniformity of the available sieve theorem**. Small `k` gives long fixed-gap runs; increasing `k` creates many shorter runs, but not an extra singular-series tax. The first serious breakdown should occur when each run is too short to deliver the required logarithmic saving uniformly in its moving gap and offset, or when `k>L` and maximal fragmentation takes over.

The reusable lesson is that representation fidelity, fragmentation count, arithmetic local factors and sample length are separate resources. An exact decomposition can make a problem look more fragmented while a second exact average shows the local arithmetic weights are neutral; the load-bearing cost may then be only the amount of data available per fragment.

**Boundary.** VIS-323 proves no prime-pair asymptotic and no Wang natural-window estimate. It does not classify the `k>L` regime or supply the short-run sieve uniformity needed downstream. It only moves the frontier from singular-series accumulation to the run-length/sieve-depth interface.