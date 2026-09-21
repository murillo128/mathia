# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Separate the signed exact-omission density threshold from the nonnegative source boundary

**Linked intuitions:** `MI-041-sublinear-point-sampling-cannot-make-divisor-response-signed-coercive`, `MI-042-subfull-point-sampling-density-cannot-make-divisor-response-signed-coercive`, `MI-043-approximate-density-one-sampling-has-a-defect-plus-residual-coercivity-ledger`, `MI-044-finite-exact-omissions-are-triangular-response-columns-not-arbitrary-sparse-increments`, `MI-045-exact-omission-cost-is-a-harmonic-location-profile`, `MI-046-cross-scale-divisibility-not-low-location-drives-exact-omission-amplification`, `MI-047-alternating-rank-merges-create-factorial-incidence-conditioning-without-reaching-the-macroscopic-scale`, `MI-048-ordered-factorization-entropy-caps-exact-omission-conditioning`, `MI-049-parity-dilation-moves-the-exact-omission-frontier-from-support-to-paired-coefficients`, `MI-050-companion-incidence-not-full-support-incidence-controls-isolated-paired-omissions`, `MI-051-congruence-restricted-companion-chains-lower-the-ordered-factorization-conditioning-exponent`, `MI-052-restricted-inverse-conditioning-counts-only-after-global-extension`, `MI-053-top-half-antichains-make-linear-density-the-sharp-signed-omission-threshold`, `MI-054-bounded-switched-response-forces-power-law-depletion-of-positive-capacity`, `MI-055-first-row-mertens-forcing-caps-polynomial-reservoir-depth`.

FD-241--FD-255 separate qualitative density-one sampling, paired exact-omission reachability, restricted incidence conditioning and the full global Möbius extension constraint. The decisive global result is FD-255: under `|b_n|<=C_b n`, every exact-omission family with `K=o(H)` has `o(H^2)` total coefficient mass. Polynomially bad support or companion inverse directions therefore do not by themselves give globally extendable macroscopic responses.

FD-256 proves that this sublinear hypothesis is sharp in order on the signed response side. Put disjoint response spikes at left endpoints of adjacent pairs entirely in `(H/2,H]`. Because every active divisor there has no second multiple below `H`, the Möbius/divisor map becomes coordinate-local: `b_e=e`, `b_(e+1)=-e`. For every `K<=H/4` this hides more than `KH` top-band coefficient mass while the response is exactly zero outside the `K` omitted locations. At `K=H/4` the construction asymptotically saturates the entire top-half coefficient envelope. Thus `K=o(H)` is coercive at macroscopic scale, while `K=Theta(H)` can fail maximally without any incidence ill-conditioning.

The remaining signed exact-omission question is quantitative rather than qualitative. In the regime `K/H->0`, FD-255 and FD-256 leave only the slowly varying gap between the constructive `KH` scale and the upper bound `KH log(e+log(H/K))`; closing that factor would sharpen the extremal norm but cannot reopen the already-settled macroscopic density threshold.

The physical source boundary is stricter because FD-256 is intrinsically signed. FD-257 gives the first quantitative positive-side rate at the bounded switched-response scale. If `0<=b_d<=Cd` and the scheduled switched rows stay uniformly bounded, the relative mass on the dyadic band `[x,2x)` satisfies

`relative capacity << (C+B)x^(-beta)`, `beta=log_2(24/23)>0`.

So a nonnegative cushion cannot keep even a slowly vanishing fraction such as `1/log x` of every deep band's linear capacity while remaining switched-invisible. The theorem is causal and survives finite growing blocks, but it does not yet rule out the canonical Mertens repair: that still requires a matching lower bound showing that the concrete repair needs more than this polynomially depleted slack on some deep bands.

FD-258 adds an independent source-side ceiling that appears before those deep bands if the same exact reservoir geometry is pushed to polynomial depth. The first switched row satisfies

`X_N(2N)-X_N(N)=M(2N)-M(N)+2(a_2-a_1)`,

while the first two physical cells provide only `O(N/D)` possible flips. Since `M(2N)-M(N)` has the full zeta-zero limsup exponent `Theta`, any all-large-`N` realization with first-row tolerance `N^{o(1)}` must satisfy

`liminf log D_N/log N <= 1-Theta <= 1/2`.

This does not touch the present `D=N^{o(1)}` Vinogradov--Korobov regime. It does say that later-row conditioning, rounding or positive-capacity improvements cannot extend this same architecture uniformly past the zero-frontier depth ceiling; a route seeking a larger polynomial exponent must change which source variables can affect the first two samples or change the reservoir geometry itself.

The live Farey source question therefore has two scales. At the currently certified subpolynomial depth, determine the minimum nonnegative slack required by the actual Mertens correction and compare it against the FD-257 polynomial capacity depletion. For any future polynomial-depth extension of the same exact cells, treat `1-Theta` as an independent first-row ceiling rather than expecting a better late-band argument to remove it.

## Separate support conditioning, paired reachability, global extension and source admissibility

The exact hierarchy has four layers. `kappa(D)` prices free active coordinates; the omission map restricts them to paired/telescoping amplitudes; the global identities `g=mu*b` and `b=1*g` require those amplitudes to extend through every divisor row under the coefficient envelope; and only then does physical source admissibility impose positivity, capacity and arithmetic realization.

FD-255 shows that the third layer removes all sublinear macroscopic signed extremizers. FD-256 shows that globally extendable signed directions return at linear omission density by a trivial top-half antichain, so large restricted inverse norms are not needed to locate the density transition. FD-257 and FD-258 then split the fourth layer into two distinct mechanisms: bounded switched response depletes nonnegative capacity across deep dyadic bands, while the first row of the exact selected-prime reservoir already ties polynomial depth to the dyadic Mertens zero frontier. Future arguments must state which layer and which source-side mechanism supplies the obstruction instead of transferring a signed reachability example or a late-band capacity estimate into a regime it does not control.