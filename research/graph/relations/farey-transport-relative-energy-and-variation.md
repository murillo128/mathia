---
id: RG-farey-transport-relative-energy-and-variation
type: research-graph-relation
derived: true
---

# Farey transport: relative energy and rank variation

[[research/farey_discrepancy/graph/farey-discrepancy|Farey Discrepancy]] · [[research/visual_exploration/graph/visual-exploration|Visual Exploration]]

This mechanism follows the explicit dependency passages in [[research/visual_exploration/findings/VIS-465-capped-variation-tariff-for-farey-transport-spectrum|VIS-465]] and the surviving synthesis [[research/visual_exploration/mind/intuition/MI-071-farey-spectral-transfer-pays-relative-energy-and-rank-variation|MI-071]]. Its two controls have different denominators.

- [[research/farey_discrepancy/findings/FD-320-all-prime-farey-excursion-permutations-have-an-exact-transport-spectrum|FD-320]], equations (1)–(4), gives `y=P_sigma D+v`, transport energy `T=||v||²`, and absolute all-mode error `E=||D||²=o(1)` for complete prime-Farey excursion permutations. The block displacement comes from cumulative excursion lengths. Absolute smallness does not by itself determine normalized energy allocation when `T` also vanishes.
- [[research/visual_exploration/findings/VIS-447-uniform-normalized-farey-transport-spectrum|VIS-447]], equations (1)–(3), bounds the total-variation distance between normalized sine-energy distributions by `min(1,sqrt(E/T))`, for `T>0` and `y!=0`. It controls every mode subset simultaneously. A null-normalized statistic additionally divides by that null's own expected band fraction.
- VIS-465, equations (1)–(4), applies [[research/prior_art/incremental/PA-bounded-variation-fourier-decay|classical bounded-variation Fourier decay]] through exact finite summation by parts. With zero endpoints, `V=sum |v_j-v_(j-1)|` and `R=N V²/T`, the high-band share is at most `min(1,B_q) <= min(1,R/(2q))`. The independent Parseval cap does not assert `B_q<=1`: the source's exact `N=3`, `v=(1,-1)`, `q=1` control has `B_q=16/9` and tail one. Combining the two source inequalities gives tail at most `min(1,R/(2q))+min(1,sqrt(E/T))` for the reassembled discrepancy.

## Explicit controls and scope

VIS-465 applies this sufficient condition to [[research/farey_discrepancy/findings/FD-319-four-vanishing-farey-index-defects-carry-macroscopic-energy|FD-319]] and [[research/farey_discrepancy/findings/FD-322-three-near-one-farey-index-defects-carry-macroscopic-energy|FD-322]]: their positive limiting transport energies and bounded roughness give low-band saturation for every divergent full-mode cutoff. The reflected control has `R->16`; the unreflected control has limits `32` or `64/3` in its two prime residue classes. This recovers an established consequence through variation, not a new arithmetic estimate.

[[research/visual_exploration/findings/VIS-032-reflection-null-sublinear-band-saturates-green-energy|VIS-032]] uses the first `q` even modes; in the reflected case this means full cutoff `2q` and roughness term `R/(4q)`. [[research/visual_exploration/findings/VIS-034-farey-low-band-suppression-factorization|VIS-034]] separates total-energy suppression from allocation relative to the null. An unreflected control needs the full sine basis and its own comparator normalization.

Large roughness is necessary, not sufficient, for transport-dominated depletion. Genuine Farey order has `T=0` and lies outside this normalized transport comparison. These are labeled-edge reassemblies, not alternative genuine Farey sequences. The cap correction, source linking and classical-method registration create no frontier episode and change no Atlas state or mass.

## Exact reflection and stitch assignment

[[research/visual_exploration/findings/VIS-466-reflected-farey-transport-parity-is-a-stitch-boundary-term|VIS-466]] evaluates the reflected sector of [[research/farey_discrepancy/findings/FD-320-all-prime-farey-excursion-permutations-have-an-exact-transport-spectrum|FD-320]] under its right-endpoint convention. The full reconstructed discrepancy `y=e+v` is rank-antisymmetric; the raw transport and residual separately need not be. With `Jz(k)=z(N-k)`, `s=(v+Jv)/2`, `a=(v-Jv)/2`, and zero sentinel block values, the symmetric transport is supported at stitches: `s(r_t)=(c_t-c_(t+1))/2`. Its odd-mode energy is exactly `L=(1/4) sum_t (c_(t+1)-c_t)^2<=E`. For nonzero transport, `0<L<T`; the residual cancels this symmetric part.

The surviving projected-sector inequality of [[research/visual_exploration/findings/VIS-450-projected-parity-transfer-sharpens-farey-gate|VIS-450]] therefore uses the exact energies `T-L` and `E-L`: `TV(pi(y),pi(a))<=min(1,sqrt((E-L)/(T-L)))`, while `TV(pi(v),pi(a))=L/T`, on the same full mode-index set. This qualifies FD-320 §3's odd-mode sentence: exact vanishing belongs to `y`, not separately to the two summands. FD-320's vector identity and absolute error survive. The first q even modes coincide with full cutoff 2q for `y` and `a`, but not for raw `v`. The earlier full-band transfer estimate for `y` remains valid.

Source discrepancy: VIS-466 prints order-seven excursion lengths `(3,4,2,4,3)`, whereas [[research/farey_discrepancy/findings/FD-331-joint-farey-defect-ranks-and-values-invert-all-excursion-permutations|FD-331]] and [[research/farey_discrepancy/findings/FD-344-reflection-makes-three-farey-defect-erasures-recoverable-four-need-not-be|FD-344]] give `(4,3,2,3,4)` for the same genuine excursions. This projection does not use VIS-466's illustrative tuple as support; it retains the general endpoint identities and the canonical gap-count definition. Correction of that source sentence belongs to its owner.

This is a finite representation correction and specialization of classical reflection and orthogonal projection, not a separate frontier episode. Projection is an analysis vector, not a new admissible reassembly. Small `L/T` supplies no small `E/T`, source-natural null normalization or RH estimate.

## Conditioning on a fixed high band

[[research/visual_exploration/findings/VIS-467-vanishing-stitch-parity-dominates-farey-high-bands|VIS-467]] realizes the conditioning obstruction inside FD-319's actual four-defect control, using the exact stitch vector of VIS-466 rather than an arbitrary perturbation. Set `B_alpha={m:alpha<=m/N<1}` with fixed `0<alpha<1`, and normalize each law by its own energy inside that band. The four exact sine-coefficient residue classes give the finite-measure limits `N sum_(m in B_alpha, odd) pi_m(v) delta_(m/N) -> dx` and `N sum_(m in B_alpha, even) pi_m(v) delta_(m/N) -> g(x) dx`, where `g(x)=2 cos²(pi x) cot²(pi x/2)` on `[alpha,1]`.

Writing `M(alpha)=1-alpha+integral_alpha^1 g(x) dx`, the odd fraction tends to `(1-alpha)/M(alpha)`. Since the antisymmetric projection retains precisely the even coefficients, this is also the limiting conditional distance `TV(pi^B(v),pi^B(a))`. For the upper half it equals `pi/(16-4pi)`, about `0.914948`, although the global distance is only `1/(N-4)`. This does not contradict the full-spectrum transfer bound: the selected band has vanishing global mass. Its raw energy is asymptotic to `b² M(alpha)`, and its odd energy to `b²(1-alpha)`, with `b=1/(2p)`.

The full reconstructed `y` has no odd modes, so `TV(pi^B(y),pi^B(v))` is at least the raw odd fraction whenever its conditional law exists. This lower bound does not identify the even-band laws of `y` and `a`. After projection, VIS-450 still requires the separate sufficient gate `||Pi_B Q_- P_sigma D||² / ||Pi_B a||² -> 0`; the corrected global ratio `(E-L)/(T-L)` cannot replace it. The high-band limits hold with alpha fixed before dimension grows, not uniformly for shrinking bands. Projection remains an analysis vector, and no genuine Farey anomaly, matched-null expectation or RH estimate follows.

Classical finite sine sums, reflection and conditioning are the background; VIS-467's additional result is the source-realized quantitative obstruction. Its new frontier episode concerns conditional high-band reliability, separately from the finite parity correction and erasure-identification problem. Atlas masses and states remain unchanged.

## Inherited source sector after stitch projection

[[research/visual_exploration/findings/VIS-468-four-defect-farey-reassembly-preserves-source-sector|VIS-468]], equations (1)–(5), resolves the finite residual representation for the specific FD-319 four-defect `BCA` order. With `N=2h`, `b=1/(2p)`, periodically extended genuine discrepancy D and half-shift `CD(k)=D((k+h) mod N)`, the exact identity is `y=CD+w`. The step w is b on `1<=k<h`, minus b on `h<k<N`, and zero at the endpoints and midpoint. The genuine values at ranks 1 and h+1 make the identity valid even at the two fixed boundary ranks.

On the same absolute sine indices, odd coefficients vanish. For `m=0 mod 4`, `yhat_m=Dhat_m` but `ahat_m=0`. For `m=2 mod 4`, with `theta_m=pi m/N`,

- `yhat_m=-Dhat_m+2b sqrt(2/N) cot(theta_m/2)`;
- `ahat_m=2b sqrt(2/N) cos(theta_m) cot(theta_m/2)`.

Thus removing odd stitches leaves a genuine-source sector that projected transport entirely omits. For a band B with both laws defined, VIS-468 (6) gives `TV(pi^B(y),pi^B(a)) >= sum_(m in B,4|m)|Dhat_m|² / ||Pi_B y||²`. That source fraction must vanish for conditional convergence; it is not generally the full distance. Its equation (7) also evaluates VIS-450's sufficient projected-error ratio exactly: the residual coefficients are Dhat on multiples of four, and `-Dhat_m+2b sqrt(2/N) sin(theta_m)` on `m=2 mod 4`. On a fixed high band the denominator remains asymptotic to `b² integral_alpha^1 g(x) dx`, so source cancellation at scale `p^(-2)` is still unproved. Vanishing residual ratio is sufficient, not necessary for convergence of squared-energy laws.

The circular-shift phase rule is classical; the source's cited [McFee, Digital Signals Theory, Theorem 6.1](https://brianmcfee.net/dstbook-site/content/ch06-dft-properties/Shifting.html) states it explicitly. The finite endpoint dictionary specializes that rule and does not establish an asymptotic arithmetic estimate. A spectral match on multiples of four copies source information; the finite panel is exploratory and does not show a positive limiting mass. This refines the existing conditional-band question without adding a frontier episode or changing Atlas states. It proves no theorem for arbitrary excursion orders and does not make either analysis vector a source-natural null ensemble.
