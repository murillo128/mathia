# MI-049 — Prime-phase rank survives density-one acquisition filters beyond fixed dimension

**Evidence level:** exact synthesis from NB-184, [NB-185](../../findings/NB-185-prime-phase-hadamard-codes-survive-density-one-euler-acquisition-filters.md), and [NB-186](../../findings/NB-186-pairwise-phase-decorrelation-recovers-growing-raw-rank-at-the-cubic-width-scale.md). The growing-rank statement concerns raw prime phases and nuclear mass, not source-faithful Euler amplitudes.

NB-185 shows that every fixed finite Hadamard prime-phase code survives the density-one NB-184 acquisition filter: finite-dimensional Kronecker--Weyl recurrence cannot be destroyed by removing an `o(T)` set of heights. Its weakness is quantitative growth, because prescribing an `N`-dimensional phase box can have exponentially small Haar measure.

NB-186 removes that box-hitting bottleneck by weakening the required geometry to exactly what the nuclear certificate needs. If `G subset [T,2T]` has complement density `epsilon`, pairwise prime-phase correlations on `G` are bounded by

`rho_(N,T,G)=(epsilon+2p_N/T)/(1-epsilon)`.

A fourth-moment selection gives `N` good heights whose raw first-`N`-prime phase matrix satisfies

`||P||_* >= N^(3/2)/sqrt(2+N rho_(N,T,G)^2)`.

Hence `N rho^2=O(1)` already yields Hadamard-scale nuclear mass without quantitative high-dimensional Kronecker recurrence. Combining this with the NB-184 exceptional-density estimate and `N asymp 1/a` gives growing raw phase rank at the cubic simultaneous-selection scale `T a^3 \gtrsim 1`; when `T a^3 -> infinity`, the lower constant approaches `1/sqrt(2)` while the good-height acquisition threshold can tend slowly to zero.

The obstruction has therefore moved again. **Growing phase coherence is not the scarce source resource.** The remaining load-bearing issue is whether a source-faithful acquisition map can retain a positive fraction of this nuclear mass after restoring the true Euler amplitudes `log p/p^(1+a)` and charging weak channels in the Wiener/capped-Poisson currency of NB-182. A negative theorem should show that every such amplitude-balanced map collapses the raw rank; a positive theorem must exhibit one that does not.

**Boundary.** NB-186 selects continuum heights and controls raw unit phases. It does not independently expose prime channels at bounded source cost, preserve growing rank after the true Euler weights are inserted, settle the finite-height quadratic boundary `T a^2=O(1)`, or connect the selected matrix directly to Nyman approximation. The cubic scale is the boundary of the present simultaneous-selection argument, not a claimed intrinsic RH threshold.