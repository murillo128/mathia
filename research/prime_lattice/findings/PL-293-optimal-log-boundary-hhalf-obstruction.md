# PL-293 — Optimal logarithmic boundary saturation blocks a generic `H^{1/2}` endpoint route

**Evidence:** `LITERATURE+EXACT-DERIVED + NEGATIVE/ROUTE-RESTRICTION + MATCHED-CONTROL`

**Status:** `OPTIMAL-LOG-BOUNDARY-LAW + H-HALF-OBSTRUCTION + FEYNMAN-HELLMANN-GATE-NARROWED`

## Claim

The endpoint-cancellation escape left open by `PL-292` cannot come merely from universal one-dimensional Dirichlet logarithmic-Laplacian regularity. Hernández-Santamaría--López Ríos--Saldaña prove the optimal boundary scale

\[
\ell(t)^{1/2},\qquad
\ell(t)=\frac1{|\log(\min\{t,0.1\})|},
\]

for bounded solutions with zero exterior data. Their positive torsion solution on sufficiently small balls has a two-sided bound of exactly this order, and their Hopf theorem gives the same lower order for nontrivial nonnegative supersolutions at an interior-sphere boundary point.

In one dimension this lower law has an exact Sobolev consequence. If a zero-exterior function satisfies

\[
|u(x_0-t)|\ge c\,\ell(t)^{1/2}
\qquad(0<t<t_0),
\]

at one endpoint, then its zero extension `Eu` is not in `H^s(R)` for any `s>=1/2`. In particular,

\[
\boxed{Eu\notin H^{1/2}(\mathbb R).}
\]

Thus the absolute first-frequency-moment condition

\[
\int_{\mathbb R}|\xi|\,|\widehat{Eu}(\xi)|^2\,d\xi<\infty,
\]

which would justify routine differentiation of translation autocorrelations and the straightforward Feynman--Hellmann route for moving prime shifts, is **not** a generic consequence of the logarithmic principal operator, exterior Dirichlet condition, positivity, or Hopf boundary structure. The torsion state is a canonical matched control that violates this threshold.

This does **not** prove that Suzuki's localized-Weil ground state fails `H^{1/2}`. A zeta-specific cancellation in the bounded arithmetic remainder could suppress the canonical boundary channel. It also does not exclude `H^s` for `0<s<1/2`, which would already give a positive-power translation modulus.

## Exact cross-boundary obstruction

Place the boundary at `0`, let the interior contain `(0,epsilon)`, and let `U=Eu` be zero outside. For `0<s<1`, the Gagliardo seminorm contains

\[
[U]_{\dot H^s(\mathbb R)}^2
\ge
C_s\int_0^{\varepsilon}|u(x)|^2
\left(\int_{-\varepsilon}^{0}\frac{dy}{|x-y|^{1+2s}}\right)dx.
\]

For `0<x<epsilon/2`, the inner integral is at least `c_s x^{-2s}`. The sharp Hopf-scale lower bound gives `|u(x)|^2 >= c/log(1/x)` for small `x`, hence

\[
[U]_{\dot H^s}^2
\ge
c_s\int_0^{\varepsilon/2}
\frac{x^{-2s}}{\log(1/x)}\,dx.
\]

This diverges for every `s>=1/2`; at the endpoint,

\[
\int_0^{\varepsilon/2}\frac{dx}{x\log(1/x)}=\infty.
\]

Therefore

\[
\boxed{
|u(x_0-t)|\gtrsim\ell(t)^{1/2}
\Longrightarrow
Eu\notin H^s(\mathbb R)\quad(s\ge1/2).
}
\]

The literature torsion theorem supplies an explicit theorem-backed matched control in the same zero-order Dirichlet geometry.

## Relation to the moving prime shifts

For compactly supported `u`,

\[
F_u(h)=\langle S_hu,u\rangle
=\frac1{2\pi}\int_{\mathbb R}e^{ih\xi}|\widehat{Eu}(\xi)|^2\,d\xi.
\]

The standard dominated-convergence derivative is justified by the displayed first-frequency moment, exactly the high-frequency part of the `H^{1/2}` norm. Suzuki's source-static arithmetic term is a finite linear combination of these autocorrelations at `h_n(a)=log(n)/a`. Hence the matched control rules out a universal implication from a positive Dirichlet logarithmic-Laplacian state to the half derivative required by that routine differentiability mechanism.

`PL-289` identifies Suzuki's principal fixed-domain operator with `T=(1/2)L_Delta+gamma I`. `PL-291`--`PL-292` place actual source-static Weil eigenstates in every finite logarithmic Fourier scale, but the generic cutoff cost does not yield a positive Sobolev exponent. At `a=0.8`, `PL-284` gives a simple even ground state conditional on source 58's computer-assisted certificate, but there is no current proof that this full Weil state belongs to the nonnegative supersolution class of the Hopf theorem. The arithmetic remainder can therefore still, in principle, cancel the universal boundary channel.

The live source-specific question is whether the rational-prime Weil eigen-equation suppresses that `ell^{1/2}` channel strongly enough to gain Sobolev power. A routine derivative argument needs `H^{1/2}`; power-law transport without differentiation could already follow from some `H^s`, `0<s<1/2`, which remains open.

## Prior art, boundaries, and consequence

The optimal `ell^{1/2}` upper bound, torsion two-sided bound, and Hopf lower estimate are literature theorems; no novelty is claimed for them. The line-local exact step is the cross-boundary Gagliardo calculation and its use as a matched-control obstruction for the differentiable moving-prime-shift route. A structure-based literature audit did not locate this exact bridge stated as a theorem. It is elementary once the sharp boundary theorem is known, so it is classified as `EXACT-DERIVED`, not as a broad novelty claim.

The obstruction is deliberately narrow. The torsion state is not the zeta state. The Hopf law has hypotheses not presently established for the full localized-Weil ground state. For `s<1/2`, the model cross-boundary integral converges, so no negative claim is made there. Failure of `H^{1/2}` also blocks only the standard absolute first-moment differentiation argument; it does not exclude a conditionally existing derivative at a particular nonzero lag.

`PL-292` left endpoint cancellation as one escape from the factorial cutoff barrier. This matched control shows that **the universal logarithmic principal operator naturally supports positive states with a nonvanishing `ell^{1/2}` boundary amplitude, and that amplitude is incompatible with `H^{1/2}` after zero extension**. A differentiable prime-shift continuation theorem must therefore prove zeta-specific suppression of that channel, exploit a non-absolute differentiability identity, or bypass differentiation. The sharper live regularity test is whether the actual low Weil branch gains any `H^s` power with `0<s<1/2`.

## Sources

- Víctor Hernández-Santamaría, Luis Fernando López Ríos, Alberto Saldaña, “Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian,” *Discrete and Continuous Dynamical Systems* **45**(1) (2025), 1--36. DOI `10.3934/dcds.2024084`; arXiv:`2401.18033`. Theorems 1.1, 1.2 and 1.4 are the load-bearing literature inputs.
- Source 96 in `research/prime_lattice/SOURCES.md`: Huyuan Chen, Tobias Weth, *The Dirichlet problem for the logarithmic Laplacian*.
- Source 56: Masatoshi Suzuki, *Weil's quadratic form via the screw function*.
- `PL-289`, `PL-291`, `PL-292`: graph-domain, all-log, and quantified source-static eigenstate regularity leading to the present endpoint question.
