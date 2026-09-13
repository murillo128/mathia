# PL-293 — Optimal logarithmic boundary saturation blocks a generic `H^{1/2}` endpoint route

**Evidence:** `LITERATURE+EXACT-DERIVED + NEGATIVE/ROUTE-RESTRICTION + MATCHED-CONTROL`

**Status:** `OPTIMAL-LOG-BOUNDARY-LAW + H-HALF-OBSTRUCTION + FEYNMAN-HELLMANN-GATE-NARROWED`

## Claim

The endpoint-cancellation escape left open by `PL-292` cannot come merely from universal one-dimensional Dirichlet logarithmic-Laplacian regularity. Hernández-Santamaría--López Ríos--Saldaña prove the optimal boundary scale

\[
\ell(t)^{1/2},\qquad
\ell(t)=\frac1{|\log(\min\{t,0.1\})|},
\]

for bounded Dirichlet solutions of the logarithmic Laplacian. Their torsion solution on sufficiently small balls has a two-sided bound of exactly this order, and their Hopf theorem gives the same lower order for nontrivial nonnegative supersolutions at an interior-sphere boundary point.

In one dimension that lower law has an exact Sobolev consequence. If a zero-exterior function satisfies, at one endpoint `x_0`,

\[
|u(x_0-t)|\ge c\,\ell(t)^{1/2}
\qquad(0<t<t_0),
\]

then its zero extension `Eu` is not in `H^s(R)` for any `s>=1/2`. In particular,

\[
\boxed{Eu\notin H^{1/2}(\mathbb R).}
\]

Hence the standard absolute first-frequency-moment condition

\[
\int_{\mathbb R}|\xi|\,|\widehat{Eu}(\xi)|^2\,d\xi<\infty,
\]

which would justify a routine differentiation of translation autocorrelations and a straightforward Feynman--Hellmann treatment of the moving prime shifts, is **not** a generic consequence of the logarithmic principal operator, exterior Dirichlet condition, positivity, or Hopf boundary structure. The positive logarithmic-Laplacian torsion state is a canonical matched control that violates this threshold.

This does **not** prove that Suzuki's localized-Weil ground state fails `H^{1/2}`. A zeta-specific cancellation in the bounded arithmetic remainder could suppress the canonical boundary channel. It also does not exclude `H^s` for `0<s<1/2`, which would already give a positive-power translation modulus.

## 1. Sharp logarithmic boundary law

For the logarithmic Laplacian

\[
\widehat{L_\Delta u}(\xi)=2\log|\xi|\,\widehat u(\xi),
\]

Hernández-Santamaría--López Ríos--Saldaña prove that bounded weak solutions of

\[
L_\Delta u=f\in L^\infty(\Omega),
\qquad
u=0\text{ on }\Omega^c,
\]

on bounded domains with a uniform exterior sphere condition satisfy

\[
|u(x)|\le C\,\ell(\operatorname{dist}(x,\partial\Omega))^{1/2}.
\]

Their sharpness theorem gives, for the positive torsion function `tau` on a sufficiently small ball,

\[
L_\Delta\tau=1\text{ in }B_r,
\qquad
\tau=0\text{ on }B_r^c,
\]

and

\[
c^{-1}\ell(r-|x|)^{1/2}
\le \tau(x)
\le c\ell(r-|x|)^{1/2}.
\]

Their Hopf theorem further gives, for a nontrivial nonnegative weak supersolution at an interior-sphere boundary point,

\[
\liminf_{t\downarrow0}
\frac{u(x_0-t\eta(x_0))}{\ell(t)^{1/2}}>0.
\]

Thus the square-root logarithmic boundary scale is not merely an upper estimate: it is attained by a canonical positive Dirichlet solution and forced in the Hopf class.

## 2. Exact cross-boundary `H^{1/2}` obstruction

Place the boundary at `0`, take the interior to contain `(0,epsilon)`, and let `U=Eu` be the zero extension. For `0<s<1`, the Gagliardo seminorm contains

\[
[U]_{\dot H^s(\mathbb R)}^2
\ge
C_s\int_0^{\varepsilon}|u(x)|^2
\left(\int_{-\varepsilon}^{0}\frac{dy}{|x-y|^{1+2s}}\right)dx.
\]

For `0<x<epsilon/2`, the inner integral is bounded below by `c_s x^{-2s}`. A Hopf-scale lower bound gives `|u(x)|^2 >= c/log(1/x)` for small `x`, hence

\[
[U]_{\dot H^s}^2
\ge
c_s\int_0^{\varepsilon/2}
\frac{x^{-2s}}{\log(1/x)}\,dx.
\]

This diverges for every `s>=1/2`; at the endpoint it is the classical divergent integral

\[
\int_0^{\varepsilon/2}\frac{dx}{x\log(1/x)}=\infty.
\]

Therefore

\[
\boxed{
|u(x_0-t)|\gtrsim \ell(t)^{1/2}
\Longrightarrow
Eu\notin H^s(\mathbb R)\quad(s\ge1/2).
}
\]

The torsion theorem supplies an explicit theorem-backed matched control in the same zero-order Dirichlet geometry.

## 3. Why the half derivative matters for the moving prime shifts

For compactly supported `u`,

\[
F_u(h)=\langle S_hu,u\rangle
=\frac1{2\pi}\int_{\mathbb R}e^{ih\xi}|\widehat{Eu}(\xi)|^2\,d\xi.
\]

The standard dominated-convergence differentiation is justified by

\[
\int |\xi|\,|\widehat{Eu}(\xi)|^2\,d\xi<\infty,
\]

which is exactly the high-frequency part of the `H^{1/2}` norm. It then gives

\[
F_u'(h)=\frac1{2\pi}\int i\xi e^{ih\xi}|\widehat{Eu}(\xi)|^2\,d\xi.
\]

Suzuki's source-static arithmetic term is a finite linear combination of such autocorrelations at `h_n(a)=log(n)/a`. The matched control therefore rules out any generic implication

\[
\text{Dirichlet log-Laplacian state + positivity}
\Longrightarrow H^{1/2}
\]

as the missing differentiability mechanism.

## 4. Relation to the localized-Weil eigenbranch

`PL-289` identifies Suzuki's fixed-domain principal operator on `I=(-1,1)` with

\[
T=\frac12L_\Delta+\gamma I
\]

in the zero-extension Fourier sense. `PL-291`--`PL-292` show that actual source-static Weil eigenstates have every finite logarithmic Fourier moment, but the generic cutoff cost prevents that bootstrap from yielding a positive Sobolev exponent.

The sharp boundary theory now eliminates one tempting generic repair: positivity and ordinary Dirichlet logarithmic-Laplacian regularity do not force the half derivative needed by the absolute-moment Feynman--Hellmann route. At `a=0.8`, `PL-284` gives a simple even ground state conditional on source 58's computer-assisted certificate, but there is currently no proof that this state is a nonnegative `L_\Delta` supersolution to which the Hopf theorem applies. The full equation `A_a=T+K_a` contains the finite von-Mangoldt translation comb and the continuous bounded remainder, so arithmetic cancellation remains logically possible.

The surviving source-specific question is therefore whether the rational-prime Weil eigen-equation cancels the universal `ell^{1/2}` boundary channel strongly enough to gain Sobolev power. For a routine derivative argument that gain must reach `H^{1/2}`; for power-law transport without differentiation, any `H^s`, `0<s<1/2`, could already be useful and remains open.

## 5. Prior art, adversarial checks, and boundaries

The optimal `ell^{1/2}` upper bound, torsion two-sided bound, and Hopf lower estimate are literature theorems; no novelty is claimed for them. The line-local exact step is the cross-boundary Gagliardo calculation and its use as a matched-control obstruction for the differentiable moving-prime-shift route. A structure-based literature audit did not locate this exact bridge stated as a theorem. It is elementary once the boundary theorem is known, so it is classified as `EXACT-DERIVED`, not as a broad novelty claim.

The obstruction is deliberately narrow. The torsion state is not substituted for the zeta state. The general Hopf lower law requires nonnegativity and a supersolution inequality not presently established for the full localized-Weil ground state. The small-ball torsion theorem is nevertheless enough to falsify a universal `H^{1/2}` consequence of the principal geometry. For `s<1/2`, the model cross-boundary integral converges, so no negative claim is made there. Failure of `H^{1/2}` also rules out only the standard absolute first-moment differentiation argument; it does not exclude a conditionally existing derivative at a particular nonzero lag.

## Consequence for the line

`PL-292` left endpoint cancellation as one possible escape from the factorial cutoff barrier. The matched control here shows that **the universal logarithmic principal operator naturally supports positive states with a nonvanishing `ell^{1/2}` boundary amplitude, and that amplitude is already incompatible with `H^{1/2}` after zero extension**. A differentiable prime-shift continuation theorem must therefore prove zeta-specific suppression of that boundary channel, exploit a non-absolute differentiability identity, or bypass differentiation. The sharper live regularity test is now whether the actual low Weil branch gains any `H^s` power with `0<s<1/2`.

## Sources

- Víctor Hernández-Santamaría, Luis Fernando López Ríos, Alberto Saldaña, “Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian,” *Discrete and Continuous Dynamical Systems* **45**(1) (2025), 1--36. DOI `10.3934/dcds.2024084`; arXiv:`2401.18033`. Theorems 1.1, 1.2 and 1.4 are the load-bearing literature inputs.
- Source 96 in `research/prime_lattice/SOURCES.md`: Huyuan Chen, Tobias Weth, *The Dirichlet problem for the logarithmic Laplacian*.
- Source 56: Masatoshi Suzuki, *Weil's quadratic form via the screw function*.
- `PL-289`, `PL-291`, `PL-292`: graph-domain, all-log, and quantified source-static eigenstate regularity leading to the present endpoint question.
