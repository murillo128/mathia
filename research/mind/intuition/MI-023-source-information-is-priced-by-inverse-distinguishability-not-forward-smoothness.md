# MI-023 — Source information is priced by inverse distinguishability, not forward smoothness

**Evidence level:** supported cross-line synthesis from [FD-167](../../farey_discrepancy/findings/FD-167-full-field-l2-inversion-has-uniform-square-root-prefix-conditioning.md), [FD-168](../../farey_discrepancy/findings/FD-168-prefix-mobius-rows-give-coordinate-minimal-stable-partial-farey-sampling.md), [MC-342](../../mobius_cancellation/findings/MC-342-forward-source-regularity-does-not-price-analog-capacity.md), and [MC-343](../../mobius_cancellation/findings/MC-343-gaussian-noise-transcript-capacity.md), with their respective exact inversion/information predecessors. No common transform theorem is claimed.

Farey Discrepancy and Möbius Cancellation give opposite exact controls on the same information-geometric question: when does a large discrete source remain *stably distinguishable* after being represented by an analytic object?

FD-167 gives the first positive inverse theorem. The complete Farey discrepancy field determines the consecutive source prefix through `floor(sqrt(H))`, and the inverse has an `H`-independent modulus in the natural unnormalized `L^2` field norm:

`max_(r<=sqrt H) |A(r)-M(r)| <= sqrt(30) ||E_H||_2`.

FD-168 shows that this conditioning is not an artifact of observing the complete field. For a target prefix `r<=R`, the union `S_(H,R)` of the nonzero Möbius inverse rows is the unique coordinate-minimal subset of the raw positive Fourier coordinates that recovers that prefix over the full formal real source space, and

`max_(r<=R)|A(r)-M(r)| <= sqrt(30) ||Pi_(H,R)E_H||_2`.

When `R<=H^(1/2-delta)`, this sampler uses only `R H^(o(1))=o(sqrt H)` coordinates. A growing amount of discrete source information can therefore be robustly encoded in a sparse observation because the actual inverse identifies both which coordinates matter and a uniform lower distinguishability bound on them.

MC-342 gives the adversarial opposite. A scalar dyadic transcript can carry essentially `R` source bits while its range, forward Hamming Lipschitz constant and every fixed positive-moment source-edge energy remain uniformly bounded. The encoding pays only through inverse geometry: minimum separation is exponentially small, so exact recovery requires linearly many precision bits even though every forward regularity statistic looks benign.

MC-343 turns that hidden precision into a quantitative capacity bill once the readout has positive Gaussian noise. If `Z=T+N`, `N~N(0,sigma^2 I_d)`, and `V_T=E||T-ET||^2`, then

`I(X;Z) <= (d/2) log(1+V_T/(d sigma^2)) <= V_T/(2 sigma^2)`.

Combining this with the reciprocal endpoint's `Theta(R)` joint-information requirement forces explicit variance/SNR and diameter/noise costs; fixed-dimensional transcripts require exponential SNR/spread. Exact recovery is impossible at every positive Gaussian noise scale because distinct Gaussian output laws overlap. Thus the MC-342 loophole survives only to the extent that arbitrarily fine noiseless real precision is granted for free.

Together these examples isolate a reusable distinction. **Forward regularity bounds how much source perturbations can move the representation; it does not say how far distinct source states remain apart. Stable source coercivity is an inverse statement relative to the resolution actually consumed downstream.** The relevant currencies are a lower distinguishability bound, inverse modulus/co-Lipschitz estimate, stable singular value, declared noise-channel capacity, finite-precision budget, or a dual witness that prevents sub-resolution state packing.

This also separates ambient dimension from useful observation size. FD-168 discards almost all raw Fourier coordinates in a substantial regime without degrading the prefix inverse modulus because those modes were outside the inverse support. MC-343 shows the converse: merely putting a transcript in few coordinates does not make its source information cheap; under noise the required information reappears as SNR or spread. Count coordinates only after identifying the source quotient, the exact observation map and its native inverse geometry.

The next line-specific questions differ. Farey must determine what happens for spatial/coarsened or custom mixed observations, for the near-square-root prefix, and at the Franel--Landau destination. Möbius must justify the source-natural readout/noise model of any genuine arithmetic transcript or prove an alternative distinguishability theorem strong enough to price its required joint information. Neither conclusion transfers automatically to the other line.

**Boundary.** FD-167--FD-168 concern a linear/Fourier Farey transform and raw-coordinate subsampling; MC-342--MC-343 concern adversarial finite transcripts and a Gaussian readout model. This synthesis does not provide a universal inverse theorem, declare Gaussian noise canonical for every analytic representation, or prove an RH estimate. It supplies an audit rule: whenever source information is claimed to be analytically usable, state and prove the inverse distinguishability resource in the observation norm and resolution actually consumed downstream.