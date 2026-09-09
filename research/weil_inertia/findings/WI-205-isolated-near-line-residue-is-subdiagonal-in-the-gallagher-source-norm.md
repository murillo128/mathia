# WI-205 — an isolated near-line zero residue is sub-diagonal in the Gallagher source norm

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + DECISIVE-NEGATIVE`.

WI-195 identifies the surviving count-saturating bow problem with a source-fixed multiplicative short-interval quadratic norm. A natural RH-facing shortcut is then to tune the prime twist to the ordinate of one hypothetical off-critical zero and hope that the zero's own explicit-formula residue already forces a diagonal-scale contribution to that norm. The exact residue bookkeeping below shows that this shortcut fails in the hard near-line regime.

For a zero `rho=beta+i gamma` of multiplicity `m_rho`, the residue of the twisted Perron integrand for

\[
M_U(y):=\sum_{n\le y}\Lambda(n)n^{-iU}
\]

at `s=rho-iU` contributes to a short interval `(x,x+K]` the term

\[
R_{\rho,U}(x,K)
=-m_\rho\,\frac{(x+K)^{\rho-iU}-x^{\rho-iU}}{\rho-iU}
=-m_\rho\int_x^{x+K}y^{\rho-iU-1}\,dy.
\]

Hence, uniformly in the twist `U`, for `x in [X,2X]`, `0<K<=X`, and `0<beta<=1`,

\[
\boxed{|R_{\rho,U}(x,K)|\le m_\rho K X^{\beta-1}}.
\tag{1}
\]

Consequently a finite packet `F` of zero residues, with total multiplicity `M_F=sum_{rho in F}m_rho` and `beta_rho<=1/2+delta_*`, satisfies

\[
\boxed{
\int_X^{2X}\left|\sum_{\rho\in F}R_{\rho,U}(x,K)\right|^2dx
\le M_F^2K^2X^{2\delta_*}.
}
\tag{2}
\]

WI-195's raw prime-square diagonal is of order `X K log X`. With its bow localization `K=X/H`, (2) is therefore at most the fraction

\[
\boxed{
\frac{M_F^2X^{2\delta_*}}{H\log X}
}
\tag{3}
\]

of the diagonal scale. In particular, at the source-compatible bow scale

\[
X=T^{1/2+o(1)},
\qquad
H=\frac{T^\vartheta}{\log T},
\qquad
\delta_*\log T=O(1),
\]

one has

\[
\boxed{
\frac{\text{finite-packet residue }L^2}
{XK\log X}
\ll M_F^2T^{-\vartheta+o(1)}.
}
\tag{4}
\]

Thus a bounded-multiplicity isolated zero, functional-equation pair, or finite mirror/conjugation packet is polynomially below the Gallagher diagonal for every fixed `vartheta>0` in the normalized-depth regime. Even at the widest single dyadic scale `H` of constant order, the same bounded packet is only `O(1/log X)` of the diagonal. To reach diagonal scale from the extracted residues alone requires coherent packet multiplicity at least

\[
\boxed{
M_F\ \gtrsim\ \sqrt{H\log X}\,X^{-\delta_*}.
}
\tag{5}
\]

which is `T^(vartheta/2+o(1))` at bounded normalized depth. This is a mesoscopic population requirement, not an individual-zero detector.

The conclusion is deliberately narrow. It does **not** give an upper or lower bound for the full WI-195 short-interval norm of `Lambda-Lambda^sharp`; other zero residues, the pole/main terms, the arithmetic approximant, and signed cross terms remain coupled. It does not prove the macroscopic off-diagonal cancellation asked for by `CLUE-bow-distinguished-twist-offdiagonal-cancellation`, nor does it refute such cancellation. What it rules out is the simpler mechanism in which the target off-line zero's own explicit-formula pole, after tuning to its ordinate, is already large enough by itself to force the needed diagonal-scale source defect.

## 1. Classical residue calculation

For `Re(s)>1`,

\[
-\frac{\zeta'}{\zeta}(s+iU)
=\sum_{n\ge1}\frac{\Lambda(n)n^{-iU}}{n^s}.
\]

Truncated Perron inversion gives the cumulative twisted prime sum from the integral of

\[
-\frac{\zeta'}{\zeta}(s+iU)\frac{y^s}{s}.
\]

If `rho` is a nontrivial zero of multiplicity `m_rho`, then `-zeta'/zeta(s+iU)` has residue `-m_rho` at `s=rho-iU`. Crossing this pole therefore contributes

\[
-m_\rho\frac{y^{\rho-iU}}{\rho-iU}.
\tag{6}
\]

Subtracting (6) at `x+K` and `x` and using the fundamental theorem of calculus gives the integral representation above. Since

\[
|y^{\rho-iU-1}|=y^{\beta-1},
\]

(1) follows immediately. Notice that the denominator `rho-iU` disappears after differentiation. Setting `U=gamma` makes the target term nonoscillatory,

\[
R_{\rho,\gamma}(x,K)
=-m_\rho\frac{(x+K)^\beta-x^\beta}{\beta},
\]

but cannot improve its order beyond (1); indeed (1) is uniform in `U`.

This is the standard von-Mangoldt explicit-formula residue mechanism, not a new identity. Classical references include Davenport, *Multiplicative Number Theory*, Chapter 17 (explicit formula for `Psi(x)`), and Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed.; a modern lecture-note statement is A. J. Harper, Theorem 6.5, which derives the von-Mangoldt formula by truncated Perron and contour shifting. The only new deduction asserted here is the comparison of a selected residue packet with the exact WI-195 Gallagher scale.

## 2. Packet bound and the Gallagher diagonal

Let `F` be any finite collection of zero residues and suppose

\[
\beta_\rho\le\frac12+\delta_*
\qquad(\rho\in F).
\]

Summing (1) before squaring gives, uniformly for `x in [X,2X]`,

\[
\left|\sum_{\rho\in F}R_{\rho,U}(x,K)\right|
\le M_F K X^{-1/2+\delta_*}.
\]

Integration over an interval of `x`-length `X` proves (2). This estimate is intentionally worst-case coherent: no cancellation between the residues is used. It therefore also covers a functional-equation/conjugation packet after replacing the packet by its total multiplicity and largest real part.

WI-195 proves the exact multiplicative Gallagher identity and then identifies, for the raw short sum at `K=X/H`, a von-Mangoldt diagonal of order

\[
D_X\asymp XK\log X.
\tag{7}
\]

Dividing (2) by (7) gives (3). The normalization `H^2/X^2` used to return to the localized source square multiplies both quantities equally, so it does not change this ratio.

For a hypothetical right-half zero with

\[
\beta=\frac12+\delta,
\]

the hard screened regime is precisely the one in which `delta log T=O(1)`. Since `X=T^(1/2+o(1))`, one then has `X^(2delta)=O(1)`. Substituting WI-195's `H=T^vartheta/log T` yields (4).

The same formula also records where the barrier stops. If `delta>0` is fixed rather than normalized-depth, then

\[
X^{2\delta}=T^{\delta+o(1)},
\]

so an isolated residue is no longer forced below diagonal once the horizontal depth is comparable with or larger than the localization exponent (`delta>=vartheta`, at this scale). Likewise a growing multiplicity or a coherent packet reaching (5) can evade the finite-packet conclusion. The result must therefore not be paraphrased as a universal invisibility theorem for off-line zeros.

## 3. What this removes from the RH-facing search

The canonical mandate asks whether an individual off-line pair or quadruple can force a detectable defect under a source-justified test family even when the exceptional set has zero density. The calculation above gives a negative answer for one particularly natural implementation of that idea: **extracting the target zero's own pole from the source-side `-zeta'/zeta` formula inside the current WI-195 quadratic observable is too weak at normalized depth.**

This matters because the failure is not logarithmic bookkeeping. At any fixed bow exponent `vartheta>0`, a bounded packet loses the polynomial factor `T^(-vartheta+o(1))` relative to the diagonal. Tuning `U` exactly to `gamma` cannot recover that factor. The current source-fixed program therefore needs genuinely collective information: a coercive identity involving the full zero/source configuration, a signed off-diagonal theorem, another source relation that couples the distinguished bow to a mesoscopic population, or a different observable whose individual-zero response is not diluted by the `XK log X` diagonal.

The accepted `CLUE-bow-distinguished-twist-offdiagonal-cancellation` remains unresolved. WI-205 narrows its target: any successful cancellation/coercivity theorem must exploit the coupled arithmetic covariance, not merely point to the explicit-formula residue of the distinguished zero.

## 4. Prior-art and falsification audit

The classical explicit formula already contains (6), so no novelty is claimed for Perron inversion, the residue at `rho`, or the idea of tuning an Archimedean twist. The new exact statement is the scale comparison (2)--(5) after importing WI-195's source-fixed Gallagher normalization.

Two nearby modern theorem surfaces do not supply the missing conclusion. Matomäki--Radziwill--Shao--Tao--Teravainen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, Invent. Math. 244 (2026), 967--1091, DOI `10.1007/s00222-026-01408-6`, gives very strong almost-all short-interval decorrelation for `Lambda-Lambda^sharp`, but its exceptional-set quantifier does not control a source-selected distinguished bow. Guth--Maynard, *New large value estimates for Dirichlet polynomials*, Ann. of Math. 203 (2026), 623--675, DOI `10.4007/annals.2026.203.2.6`, supplies powerful large-value/zero-density consequences and primes in intervals of length `x^(17/30+o(1))`, but not a pointwise source-fixed quadratic coercivity statement of the WI-195 type. These are theorem-type mismatches, not claims that their methods could never contribute after additional work.

The decisive falsifiers for WI-205 are explicit. The finding would not apply if the relevant off-line contribution necessarily came in a packet whose total multiplicity satisfies (5), if the horizontal depth is fixed far enough from `1/2` that `X^(2delta)` offsets `H`, or if a different source-justified observable gives an individual zero a larger response than (6) inside its own noise/diagonal scale. It also makes no assertion about cancellation among the complete set of explicit-formula residues.

## Research consequence

Do not spend further research cycles trying to close the hard normalized-depth bow by isolating one target pole in the WI-195 Gallagher square. The exact amplitude is already too small. Preserve the full `Lambda-Lambda^sharp` source covariance and search for a collective signed relation at the distinguished twist, or for an observable/source theorem with genuinely stronger individual-exception sensitivity.

## Evidence status

- `CLASSICAL-IDENTITY`: the Perron/log-derivative explicit-formula residue.
- `EXACT-DERIVED`: equations (1)--(5) and the packet threshold follow algebraically from that residue and WI-195's exact scale bookkeeping.
- `LITERATURE+DERIVED`: the comparison uses the already-audited WI-195 Gallagher bridge; the modern nearby theorem surfaces are used only to delimit what current black boxes do and do not state.
- `DECISIVE-NEGATIVE`: this closes the isolated-target-residue shortcut in the hard normalized-depth regime, but does not close the source-fixed covariance program or prove RH.