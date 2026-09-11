# PF-293 — critical normalized source has exactly one Sobolev derivative

**Status:** `EXACT-DERIVED + SPECTRAL-REGULARITY-THRESHOLD + ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-278-mass-one-branch-forces-critical-normalized-fixed-row-leakage|PF-278]] closes the fixed-axis Robin-homotopy leakage route because every fixed normalized Robin row has the sharp coefficient tail

\[
\langle e_n,B_w^*\varphi_i\rangle
=
C_{i,w}\,n^{-3/2}(\log n)^{-3/2}
\left(1+O((\log n)^{-1})\right)
\tag{1}
\]

along its matching parity, with `C_{i,w}\ne0`. That tail is too large for every supercritical PF-271 low-output estimate. But the same asymptotic has a different consequence for the later fixed-window obstruction in [[research/prime_flute/findings/PF-291-fixed-window-high-pass-annihilates-compact-response-profiles|PF-291]]--[[research/prime_flute/findings/PF-292-fixed-physical-high-pass-forces-diverging-local-frequency-floor|PF-292]]: it is still regular enough to carry **one full local spectral derivative**.

Let

\[
A=-\partial_\theta^2+\csc^2\theta,
\qquad
K_0=A^{1/2},
\qquad
K_0e_n=(n+\alpha)e_n,
\qquad
\alpha=\frac{1+\sqrt5}{2}.
\tag{2}
\]

For each fixed admissible seam parameter choice and fixed output row `i`, the physical normalized source column

\[
y_{i,w}:=B_w^*\varphi_i
\tag{3}
\]

satisfies

\[
\boxed{y_{i,w}\in\operatorname{Dom}K_0,}
\tag{4}
\]

but for every `\varepsilon>0`,

\[
\boxed{y_{i,w}\notin\operatorname{Dom}K_0^{1+\varepsilon}.}
\tag{5}
\]

Thus the mass-one branch that is critical for PF-271 is **not** itself a zero-regularity or frequency-escape mechanism of the type required by PF-292. The two gates spend different currencies: PF-271 needs polynomially supercritical high-to-low leakage, whereas PF-292 kills the local shorting mechanism as soon as the complete normalized response family has any uniform positive Sobolev control.

The surviving question is consequently one of **uniformity and reassembly**, not the mere existence of the fixed-axis mass-one branch. To keep a positive PF-290 deficit, the genuine tail family must make the relevant Sobolev norm diverge with the pant index, acquire additional roughness through the unresolved mixed/global Schur response, lose normalized amplitude control, or migrate out of the fixed-window model. The already-controlled hypercycle and variable-corridor transports of [[research/prime_flute/findings/PF-255-hypercycle-compactification-transport-is-a-parity-local-flow-with-a-two-derivative-leakage-bound|PF-255]]--[[research/prime_flute/findings/PF-256-variable-corridor-graph-equivalence-transfers-two-derivative-locality-to-the-actual-transverse-scale|PF-256]] do not by themselves lower this one-derivative threshold.

## Claim

Fix `r,s>0`, put `w=rs`, fix one parity sector, and let `\varphi_i` be one fixed corridor basis vector as in PF-278. Let `y_{i,w}=B_w^*\varphi_i`. Then:

1. `y_{i,w}\in\operatorname{Dom}K_0`;
2. `y_{i,w}\notin\operatorname{Dom}K_0^{1+\varepsilon}` for every `\varepsilon>0`;
3. hence the PF-278 normalized mass-one branch is exactly critical at one `K_0` derivative;
4. any family obtained from such columns by uniformly bounded finite linear combination and uniformly `K_0`-graph-bounded transport retains a uniform positive-Sobolev bound **provided the corresponding `K_0` norms of the source columns are uniformly bounded**;
5. therefore PF-292 reduces the local positive-deficit route to proving or disproving that uniformity for the actual normalized mixed response, rather than to improving PF-278's fixed-parameter coefficient exponent.

No uniform bound in the canonical pant index is asserted in item 4. PF-278 explicitly allows its constants to depend on `r,s,i`, so uniformity remains a genuine open gate.

## 1. PF-278's critical row tail is square-summable after one derivative

PF-278 proves the nonzero asymptotic (1), with opposite parity coefficients identically zero. Therefore, for all sufficiently large matching-parity `n`,

\[
|\langle e_n,y_{i,w}\rangle|
\asymp
n^{-3/2}(\log n)^{-3/2}.
\tag{6}
\]

The spectral theorem gives

\[
\|K_0y_{i,w}\|_2^2
=
\sum_{n\ge0}(n+\alpha)^2
|\langle e_n,y_{i,w}\rangle|^2.
\tag{7}
\]

The tail of (7) is comparable to

\[
\sum_{n\gg1}\frac1{n(\log n)^3},
\tag{8}
\]

which converges. The finitely many remaining coefficients are harmless, proving (4).

The inverse logarithm is load-bearing at the endpoint. Without it, a bare `n^{-3/2}` coefficient law would be logarithmically divergent after one derivative. Robin normalization supplies exactly enough slowly varying gain to put the source in `\operatorname{Dom}K_0`.

## 2. No positive fraction beyond one derivative survives

For `\varepsilon>0`,

\[
\|K_0^{1+\varepsilon}y_{i,w}\|_2^2
=
\sum_{n\ge0}(n+\alpha)^{2+2\varepsilon}
|\langle e_n,y_{i,w}\rangle|^2.
\tag{9}
\]

By the nonzero two-sided asymptotic (6), its matching-parity tail is comparable from below to

\[
\sum_{n\gg1}
\frac{n^{-1+2\varepsilon}}{(\log n)^3},
\tag{10}
\]

which diverges for every `\varepsilon>0`. This proves (5). Thus the spectral regularity boundary is exact:

\[
\boxed{
B_w^*\varphi_i\in\operatorname{Dom}K_0
\setminus
\bigcup_{\varepsilon>0}\operatorname{Dom}K_0^{1+\varepsilon}.
}
\tag{11}
\]

This is compatible with PF-277/PF-278's endpoint singularity. The mass-one square-root branch destroys supercritical coefficient decay but does not destroy first-order Sobolev regularity.

## 3. Controlled geometry does not create the missing roughness

PF-255 proves two-derivative graph locality for the exact hypercycle half-density transport and its scalar density factors relative to `A=K_0^2`. In particular, interpolation between `L^2` and `\operatorname{Dom}A` preserves `\operatorname{Dom}K_0` with tail-uniform bounds for those transports.

PF-256 then upgrades the actual variable corridor to a uniformly graph-equivalent second-order operator and transfers the already-proved two-derivative locality to the actual transverse scale. Its form/graph comparison therefore preserves the one-derivative class needed here. These results do not prove a uniform bound for the full PF-290 Riesz response, but they remove the already-controlled coordinate/density and corridor-basis changes as a source of an automatic loss from one derivative to zero derivatives.

Consequently a PF-292 frequency escape cannot be blamed solely on the PF-278 mass-one branch plus PF-255/PF-256 transport. A surviving escape must occur in a parameter-dependent growth of the normalized source norm, in the genuinely mixed/global Schur response not represented by one fixed-axis source column, in support migration beyond the fixed window, or in another normalization effect.

## 4. Consequence for the PF-290/PF-292 local falsifier

PF-292 states that for the fixed-window high-pass projections there is a moving threshold `R_n\to\infty` such that every `L^2`-bounded response family with any uniform positive fractional Sobolev bound has vanishing high projection. One full derivative is therefore far more than PF-292 requires.

The fixed-parameter asymptotic (11) does **not** yet close PF-290 because PF-292 needs a uniform bound along the canonical pant tail for the actual normalized mixed Riesz representatives `G_{n,r}`. PF-291 already warns that these representatives contain the complete mixed response, not merely the scalar width profile, and PF-279 shows that Schur reservoirs can alter naive local corridor expectations.

The decisive next test can now be stated more sharply. Extract `G_{n,r}` in a realization where the PF-278 fixed-axis source columns and PF-255/PF-256 graph-local transports are explicit, and estimate

\[
\sup_{n,r}\|K_D^\sigma G_{n,r}\|_2
\tag{12}
\]

for any one `\sigma>0`. If the only potentially critical component is the PF-278 mass-one source, its exact one-derivative regularity leaves ample room. A failure of every positive `\sigma` bound must therefore identify a genuinely parameter-growing or globally reassembled component rather than cite the mass-one branch itself.

## Prior-art and novelty audit

No new general Sobolev or Jacobi theorem is claimed. The implication from coefficient decay to membership in powers of `K_0` is the elementary spectral characterization of the domain of a positive self-adjoint operator. PF-278 already audits the classical approximation-theory literature for algebraic/logarithmic Jacobi and Gegenbauer coefficient decay, including Xiang's 2021 sharp projection estimates and Wang's 2016 Gegenbauer coefficient estimates. A targeted literature check confirms that this is standard coefficient-regularity territory; the present finding imports no stronger external theorem.

The project-specific point is the **comparison of two previously separate Prime-Flute thresholds**. PF-278's `n^{-3/2}(\log n)^{-3/2}` law is negative for the PF-271 supercritical leakage route but positive at the exact one-derivative Sobolev threshold relevant to PF-292. That distinction narrows where genuine local frequency escape can still come from.

## Boundaries and falsification

1. **No canonical-tail uniformity is proved.** PF-278's asymptotic constant depends on the fixed seam/source parameters. Equation (11) is a fixed-parameter theorem, not a bound on `\sup_{n,r}\|K_DG_{n,r}\|`.
2. **The PF-290 Riesz response is not identified with one PF-278 column.** The finding only removes the fixed-axis mass-one branch as a sufficient explanation for zero positive regularity. Mixed/global Schur terms may still be rougher.
3. **The endpoint logarithm matters.** The `\operatorname{Dom}K_0` inclusion uses the exact `(\log n)^{-3/2}` factor from PF-278. Dropping it changes the endpoint conclusion.
4. **The upper regularity boundary uses the nonzero leading coefficient.** PF-276--PF-278 rule out threshold cancellation, so the lower bound needed for divergence in (10) is genuine.
5. **Graph-local transport only preserves regularity already present.** PF-255/PF-256 do not create a uniform source bound and do not control an unresolved global Schur complement.
6. **No compactness theorem follows.** Even a future uniform positive-Sobolev bound would close only the PF-290 fixed-window local noncompactness witness. It would not prove weak trace class, full heavy-range essential orthogonality, scattering/determinants, a zeta-zero correspondence, the critical line, or RH.

The finding is falsified if PF-278's nonzero coefficient asymptotic is wrong, if `K_0e_n=(n+\alpha)e_n` is not the spectral scale used there, or if the elementary series tests (8)--(10) are misapplied. Its route-narrowing consequence is invalidated if the actual `G_{n,r}` contains a different component whose positive-Sobolev regularity fails; that would not contradict (11), but would identify the missing mechanism explicitly.