# PL-293 — Optimal logarithmic boundary saturation blocks a generic `H^{1/2}` endpoint route

**Evidence:** `LITERATURE+EXACT-DERIVED + NEGATIVE/ROUTE-RESTRICTION + MATCHED-CONTROL`

**Status:** `OPTIMAL-LOG-BOUNDARY-LAW + H-HALF-OBSTRUCTION + FEYNMAN-HELLMANN-GATE-NARROWED`

## Claim

The endpoint-cancellation escape left open by `PL-292` cannot be obtained merely from the universal one-dimensional Dirichlet logarithmic-Laplacian geometry. The sharp boundary theory for

\[
L_\Delta u=f,\qquad u=0\ \text{outside the interval},
\]

has the optimal boundary scale

\[
\ell(t)^{1/2},\qquad
\ell(t)=\frac1{|\log(\min\{t,0.1\})|}.
\]

Hernández-Santamaría--López Ríos--Saldaña prove that bounded Dirichlet solutions satisfy the upper bound `O(ell(dist)^{1/2})`; for the torsion function on sufficiently small balls they prove a two-sided bound of exactly this order; and their Hopf-type theorem gives the same lower order for nontrivial nonnegative supersolutions at an interior-sphere boundary point.

In one dimension this boundary lower law has an exact Sobolev consequence. If a zero-exterior function satisfies, at one endpoint `x_0`,

\[
|u(x_0-t)|\ge c\,\ell(t)^{1/2}
\qquad(0<t<t_0),
\]

then its zero extension `Eu` does **not** belong to `H^s(R)` for any `s>=1/2`. In particular,

\[
\boxed{Eu\notin H^{1/2}(\mathbb R).}
\]

Therefore the standard absolute first-frequency-moment condition

\[
\int_{\mathbb R}|\xi|\,|\widehat{Eu}(\xi)|^2\,d\xi<\infty,
\]

which would justify differentiating translation autocorrelations by dominated convergence and hence support a routine Feynman--Hellmann treatment of the moving prime shifts, is **not** a generic consequence of the logarithmic principal operator, Dirichlet exterior condition, positivity, or Hopf boundary structure. A canonical matched control -- the positive logarithmic-Laplacian torsion solution -- violates that threshold.

This is a route restriction, not a theorem that Suzuki's `a=0.8` ground state lacks `H^{1/2}` regularity. Suzuki's localized Weil operator contains the zeta-specific bounded remainder and moving prime-power channels. Proving `H^{1/2}` for its selected ground branch would now require a source-specific cancellation or another mechanism that suppresses the canonical Hopf-scale boundary contribution. Regularity `H^s` with `0<s<1/2`, which would already yield a positive-power translation modulus, remains open and is not excluded here.

## 1. The sharp Dirichlet logarithmic boundary law

Source 97 studies the Dirichlet logarithmic Laplacian with Fourier symbol

\[
\widehat{L_\Delta u}(\xi)=2\log|\xi|\,\widehat u(\xi).
\]

For bounded domains satisfying a uniform exterior sphere condition, Theorem 1.1 proves that every bounded weak solution of

\[
L_\Delta u=f\in L^\infty(\Omega),
\qquad
u=0\ \text{on }\Omega^c,
\]

is continuous and obeys

\[
|u(x)|\le C\,\ell(\operatorname{dist}(x,\partial\Omega))^{1/2}.
\]

The paper then proves that the exponent `1/2` is sharp. For the positive torsion function `tau` of a sufficiently small ball,

\[
L_\Delta\tau=1\ \text{ in }B_r,
\qquad
\tau=0\ \text{ on }B_r^c,
\]

Theorem 1.2 gives

\[
c^{-1}\ell(r-|x|)^{1/2}
\le \tau(x)
\le c\ell(r-|x|)^{1/2}.
\]

Theorem 1.4 supplies the corresponding Hopf lower bound more generally: a nontrivial nonnegative weak supersolution vanishing at an interior-sphere boundary point satisfies

\[
\liminf_{t\downarrow0}
\frac{u(x_0-t\eta(x_0))}{\ell(t)^{1/2}}>0.
\]

Thus the logarithmic square-root boundary profile is not merely a coarse upper regularity estimate. It is attained by a canonical positive Dirichlet solution and forced for the positive supersolution class covered by the Hopf theorem.

## 2. Exact cross-boundary `H^{1/2}` obstruction

The Sobolev consequence uses only the boundary lower bound, not the equation. Put the boundary at `0`, take the interior to contain `(0,epsilon)`, and let `U=Eu` be the zero extension. For `0<s<1`, the homogeneous Gagliardo seminorm contains the cross-boundary contribution

\[
[U]_{\dot H^s(\mathbb R)}^2
\ge
C_s\int_0^{\varepsilon}|u(x)|^2
\left(
\int_{-\varepsilon}^{0}\frac{dy}{|x-y|^{1+2s}}
\right)dx.
\]

For `0<x<epsilon/2`,

\[
\int_{-\varepsilon}^{0}\frac{dy}{(x-y)^{1+2s}}
=
\frac{x^{-2s}-(x+\varepsilon)^{-2s}}{2s}
\ge c_s x^{-2s}.
\]

If the Hopf-scale lower law holds, then for sufficiently small `x`,

\[
|u(x)|^2\ge \frac{c}{\log(1/x)}.
\]

Consequently

\[
[U]_{\dot H^s}^2
\ge
c_s\int_0^{\varepsilon/2}
\frac{x^{-2s}}{\log(1/x)}\,dx.
\]

This integral diverges for every `s>=1/2`. At the threshold,

\[
\int_0^{\varepsilon/2}\frac{dx}{x\log(1/x)}=\infty.
\]

Hence

\[
\boxed{
|u(x_0-t)|\gtrsim \ell(t)^{1/2}
\quad\Longrightarrow\quad
Eu\notin H^s(\mathbb R)\ \text{for all }s\ge\tfrac12.
}
\]

The torsion function from source 97 therefore provides an explicit theorem-backed matched control inside the same zero-order Dirichlet geometry for which the `H^{1/2}` threshold fails.

## 3. Why `H^{1/2}` is the natural derivative threshold for the moving-shift route

For a compactly supported state `u`, its translation autocorrelation is

\[
F_u(h)=\langle S_hu,u\rangle
=\frac1{2\pi}\int_{\mathbb R}
e^{ih\xi}|\widehat{Eu}(\xi)|^2\,d\xi.
\]

A standard dominated-convergence differentiation requires

\[
\int |\xi|\,|\widehat{Eu}(\xi)|^2\,d\xi<\infty,
\]

which is precisely the high-frequency part of the `H^{1/2}` norm. Under that condition,

\[
F_u'(h)=\frac1{2\pi}\int i\xi e^{ih\xi}|\widehat{Eu}(\xi)|^2\,d\xi
\]

is absolutely defined and bounded. Since Suzuki's source-static arithmetic term is a finite linear combination of such autocorrelations evaluated at

\[
h_n(a)=\frac{\log n}{a},
\]

this is the clean regularity threshold for the straightforward Feynman--Hellmann/differentiable-translation route contemplated after `PL-289`--`PL-292`.

The matched control above shows that this threshold cannot be obtained from a generic theorem of the form

\[
\text{Dirichlet log-Laplacian state + positivity}
\Longrightarrow H^{1/2}.
\]

The canonical positive torsion state has the opposite behavior. The optimal boundary theorem identifies the obstruction geometrically: zero extension across a Hopf-saturating `ell^{1/2}` boundary creates exactly enough cross-boundary fractional energy to diverge at `s=1/2`.

## 4. Relation to the localized Weil eigenbranch

`PL-289` identifies Suzuki's fixed-domain principal operator on `I=(-1,1)` with

\[
T=\frac12L_\Delta+\gamma I
\]

in the exact zero-extension Fourier sense and proves the squared-log graph-domain estimate. `PL-291`--`PL-292` then bootstrap actual source-static Weil eigenstates through all finite logarithmic Fourier moments, but the constants grow too rapidly to yield a positive Sobolev exponent by the generic cutoff argument.

Source 97 now explains why one particularly tempting repair is not generic. Optimal boundary behavior for the underlying logarithmic Dirichlet equation is **slow**, not power-like, and canonical positive solutions need not cross the `H^{1/2}` threshold. Therefore a proof that the actual Weil ground branch lies in `H^{1/2}` cannot be justified merely by invoking boundedness, continuity, positivity of a principal state, or the universal logarithmic-Laplacian boundary theory.

There is, however, no direct contradiction with a zeta-specific `H^{1/2}` theorem. Suzuki's full operator is

\[
A_a=T+K_a,
\]

where `K_a` contains the finite von-Mangoldt translation comb and the continuous bounded remainder. At `a=0.8`, `PL-284` certifies a simple even ground state conditional on source 58's computer-assisted bounds, but the current evidence does **not** prove that this state is a nonnegative `L_Delta` supersolution satisfying the hypotheses of source 97's Hopf theorem. The arithmetic perturbation could in principle change the endpoint coefficient or produce cancellation.

The precise surviving question is therefore source-specific:

\[
\boxed{
\text{Does the rational-prime Weil eigen-equation cancel the universal }
\ell^{1/2}\text{ boundary channel strongly enough to gain Sobolev power?}
}
\]

For an actual derivative/Feynman--Hellmann route the required gain reaches at least `H^{1/2}` under the standard absolute-moment argument. For a merely Hölder transport estimate, any `H^s` with `0<s<1/2` could already be useful and is not ruled out by the boundary calculation.

## 5. Prior-art and novelty audit

The optimal `ell^{1/2}` boundary estimate, the torsion two-sided bound, and the Hopf-type lower estimate are theorems of Hernández-Santamaría--López Ríos--Saldaña. No novelty is claimed for those PDE results. Source 96 supplies the earlier Dirichlet logarithmic-Laplacian framework used in `PL-289`, while Feulefack--Jarohs--Weth (2022) already prove boundedness/continuity properties of logarithmic-Laplacian eigenfunctions and uniform boundary decay in the small-order fractional limit.

The added line-local statement is the exact `H^{1/2}` obstruction obtained by combining the sharp lower boundary law with the cross-boundary Gagliardo seminorm, and its use as a matched-control falsification test for the differentiable moving-prime-shift route. A structure-based literature search (`logarithmic Laplacian` + sharp boundary/Hopf + fractional Sobolev `H^{1/2}`/zero extension) did not locate this exact bridge stated as a theorem. It is elementary once the sharp boundary theorem is known, so it is recorded as `EXACT-DERIVED`, not as a broad novelty claim in logarithmic-Laplacian regularity.

The conclusion is also deliberately narrower than `PL-292`'s open positive-order question. A `ell^{1/2}` boundary profile is compatible with `H^s` for `s<1/2` as far as the cross-boundary integral is concerned, because

\[
\int_0^\varepsilon
\frac{x^{-2s}}{\log(1/x)}\,dx<\infty
\qquad(0<s<1/2).
\]

So the result blocks the generic **half-derivative/absolute-differentiation** upgrade, not every possible power-law transport theorem.

## 6. Adversarial checks and boundaries

- **Matched control, not the zeta state.** The torsion solution is used to falsify a universal regularity inference from the logarithmic principal geometry. It is not substituted for Suzuki's actual ground state.
- **Hopf hypotheses matter.** The general lower law requires nonnegativity and the weak supersolution inequality. Those hypotheses are not currently established for the full `A_0.8` ground state relative to the bare `L_Delta` operator.
- **Small-ball condition is sufficient.** Source 97's torsion theorem requires a sufficiently small ball. A single admissible canonical Dirichlet control is enough to disprove a universal `H^{1/2}` consequence; no claim is made for torsion on every interval size.
- **No claim below `1/2`.** The cross-boundary integral converges at the model lower-law scale for every `s<1/2`. Interior oscillation could still obstruct such Sobolev regularity, but this finding does not establish that.
- **No converse from Fourier moments.** Failure of `H^{1/2}` rules out the standard absolute first-moment differentiation argument. It does not prove that an autocorrelation derivative cannot exist conditionally at a particular nonzero lag.
- **No positivity transport yet.** Even a future `H^s`, `0<s<1/2`, estimate would still need quantitative constants strong enough to propagate the tiny `a=0.8` margin and handle source activations.
- **No RH conclusion.** This is a regularity-route restriction inside the localized Weil program, not a zero-localization theorem.

## Consequence for the line

`PL-292` left endpoint cancellation as one possible way around the factorial cutoff cost. The sharp Dirichlet boundary theory now supplies a decisive matched control: **the universal logarithmic principal operator naturally supports positive states with a nonvanishing `ell^{1/2}` boundary amplitude, and that amplitude is already incompatible with `H^{1/2}` after zero extension.**

Accordingly, a differentiable prime-shift/Feynman--Hellmann continuation theorem cannot come from generic logarithmic-Laplacian regularity. It must either prove zeta-specific cancellation of the Hopf-scale boundary channel, exploit a non-absolute differentiability mechanism, or bypass differentiation entirely. The weaker but still potentially useful target `H^s` for some `0<s<1/2` remains live and becomes the sharper next regularity threshold to test.

## Sources

- Source 97 in `research/prime_lattice/SOURCES.md`: Víctor Hernández-Santamaría, Luis Fernando López Ríos, Alberto Saldaña, *Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian*, DCDS **45** (2025), 1--36, DOI `10.3934/dcds.2024084`, arXiv:`2401.18033`; Theorems 1.1, 1.2 and 1.4.
- Source 96: Huyuan Chen, Tobias Weth, *The Dirichlet problem for the logarithmic Laplacian*; Dirichlet logarithmic-Laplacian framework used by `PL-289`.
- Source 56: Masatoshi Suzuki, *Weil's quadratic form via the screw function*; canonical localized Weil operator and fixed-domain decomposition.
- `PL-289`, `PL-291`, `PL-292`: graph-domain, all-log, and quantified source-static eigenstate regularity leading to the present endpoint question.
