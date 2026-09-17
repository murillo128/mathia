# MI-023 — Source information is priced by inverse distinguishability and aggregate capacity, not forward smoothness

**Evidence level:** supported cross-line synthesis from [FD-167](../../farey_discrepancy/findings/FD-167-full-field-l2-inversion-has-uniform-square-root-prefix-conditioning.md), [FD-168](../../farey_discrepancy/findings/FD-168-prefix-mobius-rows-give-coordinate-minimal-stable-partial-farey-sampling.md), [MC-342](../../mobius_cancellation/findings/MC-342-forward-source-regularity-does-not-price-analog-capacity.md), [MC-343](../../mobius_cancellation/findings/MC-343-gaussian-noise-transcript-capacity.md), [MC-344](../../mobius_cancellation/findings/MC-344-bit-flip-source-readout-capacity.md), [NB-176](../../nyman_beurling/findings/NB-176-euler-weighted-fourier-fingerprints-certify-source-complexity.md), and [NB-177](../../nyman_beurling/findings/NB-177-square-summable-euler-spectrum-caps-canonical-complexity-certificate.md). No common transform theorem is claimed.

Farey Discrepancy, Möbius Cancellation and Nyman--Beurling expose three sides of the same information-geometric question: when does a large discrete or adaptive source remain *usefully distinguishable* after analytic representation?

FD-167 gives a positive inverse theorem. The complete Farey discrepancy field determines the consecutive source prefix through `floor(sqrt(H))`, with an `H`-independent modulus in the natural unnormalized `L^2` field norm:

`max_(r<=sqrt H) |A(r)-M(r)| <= sqrt(30) ||E_H||_2`.

FD-168 shows that this conditioning is not an artifact of observing the complete field. For a target prefix `r<=R`, the union of the nonzero Möbius inverse rows is the unique coordinate-minimal subset of raw positive Fourier coordinates that recovers that prefix, with the same `sqrt(30)` inverse modulus. When `R<=H^(1/2-delta)`, only `R H^(o(1))=o(sqrt H)` coordinates are needed. A growing source prefix can therefore be robustly encoded in a sparse observation because the exact inverse identifies both the relevant coordinates and their lower distinguishability scale.

MC-342 gives the adversarial opposite. A scalar dyadic transcript can carry essentially `R` source bits while range, forward Hamming Lipschitz constant and every fixed positive-moment source-edge energy stay uniformly bounded. The cost appears only in inverse geometry: minimum separation is exponentially small. Forward smoothness therefore does not price information.

MC-343 converts that hidden precision into a quantitative bill under Gaussian readout noise. If `Z=T+N`, `N~N(0,sigma^2 I_d)`, then

`I(X;Z) <= (d/2) log(1+V_T/(d sigma^2)) <= V_T/(2 sigma^2)`.

The reciprocal endpoint requires `Theta(R)` joint information, so fixed-dimensional transcripts need exponential SNR/spread and every positive Gaussian noise scale destroys exact recovery.

MC-344 prevents the opposite overstatement. If only `k` source coordinates are exposed through independent bit-flip noise with crossover `q`, then

`I(X;Y) <= k c(q)`

for `c(q)=log 2-h(q)`, so any fixed dephasing gain requires `k=Omega(R)` at fixed noise. But if all `R` coordinates are exposed at fixed `q<1/2`, the punctured source still carries `R c(q)-o(R)=Theta(R)` information. **Noise is not itself the invariant obstruction.** What matters is aggregate capacity at the resolution actually consumed downstream.

NB-176 supplies a source-native *dual* distinguishability certificate: the actual Euler frequencies of `zeta'/zeta` form one capped-Poisson-contracting Hilbert feature map, and its response Gram can prove that many template distinctions survive above a declared source resolution. NB-177 then shows that even this canonical witness can become too compact. Square-summability of the Euler amplitudes forces

`tr sqrt(G^Eul) <= C X N^(3/4) sqrt(log(2N))`,

so the mean singular scale decays with the number of templates. The resulting lower certificate can be `o((log T)^2)` even when the true approximate source complexity is not known to be small. A source-native representation may therefore under-price complexity if its own inverse/dual geometry compresses distinctions below resolution.

Together these examples isolate the reusable accounting rule. **Source information is usable only relative to an observation map, a resolution, and an inverse or dual distinguishability theorem; total surviving channel capacity must then be large enough for the downstream task.** Forward regularity controls how much representations move under source perturbations, not how far distinct source states remain apart. Noise matters through the capacity it removes. Sparse coordinates can be sufficient when an inverse is uniformly conditioned, while many canonical features can still be insufficient as a certificate when their singular spectrum collapses.

The relevant currencies are therefore lower separation/inverse modulus, stable singular values, aggregate channel capacity, finite-precision/noise budget, or a dual witness that stays nondegenerate at the declared source resolution. Ambient dimension, coordinate count, smoothness, source-native labeling and positive noise should be counted only after those quantities are explicit.

**Boundary.** FD-167--FD-168 concern a linear/Fourier Farey transform; MC-342--MC-344 concern finite-source transcripts under specific analog or bit-flip readouts; NB-176--NB-177 concern a one-sided Hilbert certificate for Nyman approximate complexity. This synthesis does not provide a universal inverse theorem, declare any one noise model canonical, upper-bound Nyman complexity, or prove an RH estimate. It supplies an audit rule: whenever source information is claimed to be analytically usable, state the resolution, prove the inverse/dual distinguishability resource, and show that the resulting aggregate capacity reaches the destination.