# PL-296 — A recent Volterra formula for logarithmic-Laplacian ball torsion has the wrong boundary order

**Evidence:** `LITERATURE+EXACT-DERIVED + CORRECTION/ROUTE-GUARDRAIL`

**Status:** `RECENT-LITERATURE-INCONSISTENCY + BOUNDARY-ASYMPTOTIC-REFUTATION + EXPLICIT-INVERSE-ROUTE-REJECTED`

## Claim

A recent published formula of Alejandro Ortega for the zero-exterior Poisson problem of the logarithmic Laplacian on a ball is incompatible with the sharp boundary theory already audited in `PL-293`.

Ortega considers the standard logarithmic Laplacian with Fourier symbol

\[
\widehat{L_\Delta u}(\xi)=2\log|\xi|\,\widehat u(\xi),
\]

and claims that the solution of

\[
L_\Delta u=1\quad\text{in }B_r(x_0),
\qquad
u=0\quad\text{on }\mathbb R^N\setminus B_r(x_0)
\]

is

\[
u(x)=\Lambda\!\left((r^2-|x-x_0|^2)_+;N\right).
\]

In dimension `N=1` the paper simplifies this to

\[
\boxed{
 u_{\rm O}(x)=\frac12\,\nu\!\left(\sqrt{r^2-|x-x_0|^2}\right)
}
\]

inside the interval, extended by zero outside, where the Volterra function is

\[
\nu(y)=\int_0^\infty\frac{y^t}{\Gamma(1+t)}\,dt.
\]

However, if `delta=r-|x-x_0|` denotes distance to the boundary, this candidate satisfies the exact asymptotic

\[
\boxed{
 u_{\rm O}(x)\sim \frac1{\log(1/\delta)}
 =\ell(\delta)
}
\qquad(\delta\downarrow0),
\]

whereas Hernández-Santamaría--López Ríos--Saldaña prove that the positive zero-exterior logarithmic-Laplacian torsion function on sufficiently small balls has two-sided boundary order

\[
\boxed{
 \tau(x)\asymp \ell(\delta)^{1/2}.
}
\]

Since

\[
\ell(\delta)=o\!\left(\ell(\delta)^{1/2}\right),
\]

the two statements cannot both describe the same Dirichlet solution. On every sufficiently small one-dimensional ball covered by the sharp torsion theorem, Ortega's compactly supported Volterra profile therefore **cannot solve the claimed zero-exterior Poisson problem**.

The mismatch is not a normalization issue: both papers use the logarithmic Laplacian with Fourier symbol `2 log|xi|`. It is also visible directly in Ortega's semigroup argument. The whole-space multiplier `L_Delta` is not positive, so

\[
\int_0^\infty e^{-tL_\Delta}\,dt=L_\Delta^{-1}
\]

is not a globally convergent positive-semigroup identity: at Fourier frequency `|xi|<1`, the multiplier `e^{-2t log|xi|}=|xi|^{-2t}` grows with `t`, and its `t`-integral diverges. In addition, the compactly supported fractional torsion profile used later in the proof solves the restricted Dirichlet equation only **inside** the ball; it is not the whole-space inverse multiplier `(-Delta)^{-t} chi_B` asserted earlier. These two constructions cannot be interchanged.

For the `prime_lattice` program this is a useful route guardrail. The Volterra formula must not be used as an explicit model for the boundary coefficient of Suzuki's localized-Weil eigenfunctions or as evidence that the generic `ell^{1/2}` channel from `PL-293` can be improved to `ell`. The source-specific boundary/sign problem left by `PL-293`--`PL-295` remains open.

## 1. Ortega's one-dimensional formula has boundary order `ell(delta)`

Ortega defines

\[
\nu(y)=\int_0^\infty\frac{y^t}{\Gamma(1+t)}\,dt,
\qquad y>0.
\]

Let `y` tend to zero and put

\[
L=\log(1/y)\to\infty.
\]

Then

\[
\nu(y)=\int_0^\infty e^{-Lt}\frac{dt}{\Gamma(1+t)}.
\]

Near `t=0`,

\[
\frac1{\Gamma(1+t)}=1+O(t),
\]

while `1/Gamma(1+t)` is bounded on `[0,infinity)` and decays rapidly for large `t`. Splitting at any fixed small `eta>0` gives

\[
\int_0^\eta e^{-Lt}\frac{dt}{\Gamma(1+t)}
=
\frac1L+O\!\left(\frac1{L^2}\right)+O(e^{-\eta L}),
\]

and

\[
\int_\eta^\infty e^{-Lt}\frac{dt}{\Gamma(1+t)}
=O(e^{-\eta L}).
\]

Hence

\[
\boxed{
\nu(y)=\frac1{\log(1/y)}
+O\!\left(\frac1{\log^2(1/y)}\right).
}
\]

For an endpoint of the interval, write

\[
|x-x_0|=r-\delta.
\]

Then

\[
r^2-|x-x_0|^2
=2r\delta-\delta^2,
\]

so

\[
y=\sqrt{r^2-|x-x_0|^2}
=\sqrt{2r\delta}\,(1+o(1))
\]

and therefore

\[
\log(1/y)
=\frac12\log(1/\delta)+O(1).
\]

Substituting into Ortega's formula gives

\[
\frac12\nu(y)
\sim
\frac1{\log(1/\delta)}.
\]

This is an exact first-order asymptotic derived from the displayed formula itself; no numerical fit or special-function table is needed.

## 2. The asymptotic contradicts the sharp zero-exterior torsion theorem

`PL-293` audited the 2025 theorem of Hernández-Santamaría, López Ríos and Saldaña for the same logarithmic-Laplacian normalization. On sufficiently small balls, their positive torsion solution satisfies a two-sided estimate

\[
c^{-1}\ell(\delta)^{1/2}
\le \tau(x)
\le c\ell(\delta)^{1/2}
\]

near the boundary, with

\[
\ell(\delta)
=\frac1{|\log(\min\{\delta,0.1\})|}.
\]

The ratio of Ortega's candidate to this sharp scale is

\[
\frac{u_{\rm O}(x)}{\ell(\delta)^{1/2}}
\sim \ell(\delta)^{1/2}
\longrightarrow0.
\]

Thus no change of multiplicative constant can reconcile the two. In particular, on any sufficiently small interval where the torsion theorem applies, the Volterra profile violates the theorem's lower boundary bound by an asymptotically unbounded factor.

This comparison is deliberately local in radius. It does not require a statement about all balls and does not infer anything from large-domain positivity. A single sufficiently small interval is enough to refute the formula as a general solution of the claimed Dirichlet problem.

## 3. Where the semigroup derivation changes operators

The paper first considers the whole-space evolution

\[
\partial_t v+L_\Delta v=0,
\qquad
v(\cdot,0)=\chi_B,
\]

and formally writes

\[
\widehat v(\xi,t)
=|\xi|^{-2t}\widehat{\chi_B}(\xi),
\qquad
v(\cdot,t)=(-\Delta)^{-t}\chi_B.
\]

There are already two problems with using this as an inverse representation for the zero-exterior Dirichlet operator.

First, `L_Delta` on the whole space has symbol `2 log|xi|`, which takes both signs. Consequently the formal resolvent integral

\[
\int_0^\infty |\xi|^{-2t}\,dt
\]

converges only for `|xi|>1`; it diverges for `0<|xi|<=1`. Since `hat chi_B(0)=|B|` is nonzero, the asserted identity

\[
\int_0^\infty e^{-tL_\Delta}\chi_B\,dt
=L_\Delta^{-1}\chi_B
\]

cannot be justified as the displayed whole-space Fourier integral. In particular, this is not the usual inverse-of-a-positive-generator semigroup formula.

Second, the proof then replaces that whole-space inverse profile by the well-known compactly supported fractional torsion solution

\[
v_D(x,t)
=C_{N,t}(r^2-|x-x_0|^2)_+^t,
\]

which solves

\[
(-\Delta)^t v_D=1
\quad\text{in }B,
\qquad
v_D=0
\quad\text{on }B^c.
\]

This is a **restricted Dirichlet** statement. It does not say

\[
(-\Delta)^t v_D=\chi_B
\quad\text{on all of }\mathbb R^N,
\]

and in fact the nonlocal fractional Laplacian of a nonzero compactly supported profile has a nonzero exterior tail. Hence

\[
v_D(\cdot,t)\ne(-\Delta)^{-t}\chi_B
\]

as a whole-space Fourier multiplier identity. The passage from the first construction to the second therefore changes the operator problem precisely at the step needed to obtain compact support.

The boundary contradiction above is an independent diagnostic of the same mismatch: integrating the Dirichlet fractional torsion family in the order parameter produces a profile, but not the zero-exterior inverse of the logarithmic Dirichlet operator claimed in the paper.

## 4. Relevance to the localized-Weil boundary program

The live frontier after `PL-293`--`PL-295` is whether the **actual rational-prime completed-Weil eigen-equation** suppresses, modifies, or fixes the generic logarithmic-Laplacian boundary channel. The Ortega formula might superficially appear to supply exactly the missing explicit inverse and a stronger boundary decay, because `ell(delta)` would lie below the generic `ell(delta)^{1/2}` scale and would materially alter the Sobolev endpoint discussion.

The present audit rules out that shortcut. The `ell` decay comes from integrating the fractional torsion profiles through a semigroup identification that does not preserve the zero-exterior Dirichlet operator. It therefore supplies no evidence for extra `H^{1/2}` regularity, a vanishing Hopf coefficient, or a fixed-sign continuation of Suzuki's ground state.

Accordingly, the source-specific target from `PL-295` is unchanged: any improved boundary decay for the localized-Weil eigenstate must be proved from the completed Weil equation itself, for example through an arithmetic cancellation in the finite prime-shift/remainder term or an independently controlled boundary observable. It cannot be imported from this Volterra formula.

## 5. Evidence, novelty, and adversarial audit

The published-source facts used here are narrow and checkable. Ortega's 2026 paper explicitly uses the symbol `2 log|xi|`, states the zero-exterior ball Poisson problem, writes the whole-space Fourier multiplier `|xi|^{-2t}`, integrates it formally as `L_Delta^{-1}`, then substitutes the compactly supported fractional ball-torsion profile. Its one-dimensional formula is exactly `u=(1/2)nu(sqrt(r^2-|x-x0|^2))`.

The sharp `ell^{1/2}` boundary theorem is prior literature already audited in `PL-293`; no novelty is claimed for it. The new Mathia contribution is the exact incompatibility check against the 2026 Volterra formula, together with the elementary asymptotic and the identification of the operator switch in the semigroup derivation.

A targeted current search for the Ortega title/DOI together with `correction`, `erratum`, `comment`, and the boundary/Volterra terminology found no published correction or response as of 13 September 2026. The journal page still presents the result as the version of record. Absence of a located correction is not evidence that none exists; it only records the present audit surface.

Adversarial boundaries:

- **Same normalization.** The contradiction is not caused by a factor-of-two convention: Ortega explicitly states Fourier symbol `2 log|xi|`, matching the Chen--Weth/Hernández-Santamaría--López Ríos--Saldaña convention used in `PL-293`.
- **Small balls suffice.** The refutation needs only the sufficiently small balls for which the sharp positive torsion estimate is established. No all-radius maximum principle is assumed.
- **Formula, not all of Ortega's surrounding special-function identities.** The conclusion rejects the claimed identification of the Volterra profile with the zero-exterior logarithmic-Poisson solution. It does not challenge the algebraic Volterra identities themselves.
- **No claim about Suzuki's actual boundary coefficient.** The contradiction removes a tempting shortcut; it neither proves nor disproves cancellation of the `ell^{1/2}` channel for the completed-Weil ground state.
- **No reliance on analytic continuation.** The decisive asymptotic is an elementary positive real integral estimate, and the comparison is between two zero-exterior boundary statements.
- **Whole-space versus Dirichlet distinction is essential.** The formal whole-space multiplier equation and the restricted fractional Dirichlet problem are different nonlocal operator problems even though both use the notation `(-Delta)^t`.

## Consequence for the line

Treat Ortega's compactly supported Volterra profile as **disqualified evidence** for the localized-Weil boundary program unless the source is corrected or a different operator/domain interpretation is supplied that removes the contradiction. `PL-293` remains the authoritative generic boundary control: the universal logarithmic principal operator supports the `ell^{1/2}` boundary channel, while any stronger decay for the zeta-specific eigenstate must come from additional arithmetic structure.

The durable lesson is methodological but mathematically concrete: **integrating restricted fractional Dirichlet torsion states over the order parameter is not the same as applying the inverse of the Dirichlet logarithmic Laplacian.** Any future fractional-order interpolation used in the prime-lattice/Weil program must establish the relevant domain-dependent functional calculus before transporting semigroup or inverse identities across `s=0`.

## Sources

- Alejandro Ortega, “Explicit solutions for the Poisson problem in a ball for the logarithmic Laplacian,” *Carpathian Mathematical Publications* **18**(1) (2026), 111--116. DOI: `10.15330/cmp.18.1.111-116`. The load-bearing statements are the Fourier symbol and problem (3) on pp. 111--112, the semigroup/inverse passage and formula (5) on p. 113, and the one-dimensional Volterra formula (7) on p. 114.
- Víctor Hernández-Santamaría, Luis Fernando López Ríos, Alberto Saldaña, “Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian,” *Discrete and Continuous Dynamical Systems* **45**(1) (2025), 1--36. DOI: `10.3934/dcds.2024084`; arXiv:`2401.18033`. The sharp boundary/torsion and Hopf results are the load-bearing contradiction control already audited in `PL-293`.
- Source 96 in `research/prime_lattice/SOURCES.md`: Huyuan Chen, Tobias Weth, *The Dirichlet problem for the logarithmic Laplacian*, for the standard symbol/Dirichlet realization.
- `PL-293`, `PL-294`, `PL-295`: current boundary, positivity, and sign-continuation frontier to which this correction applies.
