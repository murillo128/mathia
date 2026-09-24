# WI-433 — localized Hardy transport separates edge forcing from zero residues

Status: `CLASSICAL-DISTRIBUTION-IDENTITY + EXACT-DERIVED + STRUCTURAL-REDIRECTION + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`

Parents: `WI-429`, `WI-430`, `WI-431`, `WI-432`

## Claim

The horizontal continuation problem left open by `WI-432` has an exact distributional transport identity. It cleanly separates the localized positive-frequency logarithmic derivative into three terms: damped safe-line Hardy leakage, a height-window edge forcing term, and explicit residues of right-half zeros crossed during horizontal continuation.

Put

\[
F(s):=\frac{\zeta'(s)}{\zeta(s)}+\frac1{s-1}.
\tag{1}
\]

The pole at `s=1` is canceled. In the open half-plane `Re s>1/2`, the remaining poles of `F` are precisely the nontrivial zeros

\[
\rho=\beta+i\gamma,\qquad \beta>\frac12,
\]

with residue equal to their multiplicity `m_\rho`. Hence, with `s=\sigma+it` and

\[
\bar\partial=\frac12(\partial_\sigma+i\partial_t),
\]

the classical distribution identity `\bar\partial(1/z)=\pi\delta_0` gives

\[
\boxed{
(\partial_\sigma+i\partial_t)F(\sigma+it)
=
2\pi\!\sum_{\rho:\,\beta>1/2}
 m_\rho\,\delta(\sigma-\beta)\delta(t-\gamma).
}
\tag{2}
\]

Let `\chi\in C_c^\infty(\mathbb R)` and use the Fourier convention

\[
\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-it\xi}\,dt.
\tag{3}
\]

For `\xi>0` define

\[
H_\sigma(\xi)
:=1_{\xi>0}\widehat{\chi(t)F(\sigma+it)}(\xi),
\qquad
K_\sigma(\xi)
:=1_{\xi>0}\widehat{\chi'(t)F(\sigma+it)}(\xi).
\tag{4}
\]

Then, distributionally in `\sigma`,

\[
\boxed{
\partial_\sigma H_\sigma(\xi)
=
\xi H_\sigma(\xi)
+iK_\sigma(\xi)
+2\pi\!\sum_{\rho:\,\beta>1/2}
 m_\rho\chi(\gamma)e^{-i\gamma\xi}\delta(\sigma-\beta),
\qquad \xi>0.
}
\tag{5}
\]

Consequently, if `\sigma<\sigma_0`, neither endpoint is the real part of a zero, and `\sigma_0>1`, then

\[
\boxed{
\begin{aligned}
H_\sigma(\xi)
={}&e^{-(\sigma_0-\sigma)\xi}H_{\sigma_0}(\xi)\\
&-i\int_\sigma^{\sigma_0}
 e^{-(u-\sigma)\xi}K_u(\xi)\,du\\
&-2\pi\!\sum_{\rho:\,\sigma<\beta<\sigma_0}
 m_\rho\chi(\gamma)
 e^{-(\beta-\sigma)\xi}e^{-i\gamma\xi},
\qquad \xi>0.
\end{aligned}
}
\tag{6}
\]

Equation (6) is the missing exact bookkeeping behind the `WI-429`--`WI-432` branch. In particular, `WI-432` makes the first term small for adiabatic safe-line windows. The residue term is exactly the horizontal defect signal one wants to detect. Therefore **all non-residue compensation is forced into the edge term involving `\chi'F`**. A continuation argument that keeps only the safe-line positive Hardy source and omits this edge term cannot be valid.

This is a structural redirection, not a new proportion theorem. The next live theorem is now precise: control the edge integral in (6) from independently available source-side information without re-importing the same right-half zeros. If that can be done strongly enough, the residue term can be combined with the first-defect quantum of `WI-430`; if it cannot, an exact circularity barrier should be provable at the level of (6).

## 1. Distributional derivation

For a meromorphic function with a simple local principal part `m/(s-\rho)`, the Cauchy-kernel identity gives

\[
\bar\partial\frac{m}{s-\rho}=m\pi\delta_\rho.
\tag{7}
\]

Because `\zeta'/\zeta` has residue `m_\rho` at a zero of multiplicity `m_\rho` and residue `-1` at `s=1`, the added term `1/(s-1)` removes the pole at `1`. Trivial zeros lie to the left of `Re s=1/2`. Summing the local divisor currents therefore gives (2) on every compact subset of the open half-plane `Re s>1/2`.

Multiplying (2) by `\chi(t)` gives

\[
\partial_\sigma(\chi F)
=
-i\partial_t(\chi F)
+i\chi'F
+2\pi\!\sum_\rho
m_\rho\chi(\gamma)
\delta(\sigma-\beta)\delta(t-\gamma).
\tag{8}
\]

Under (3),

\[
\widehat{\partial_t f}(\xi)=i\xi\widehat f(\xi).
\]

Thus the transform of `-i\partial_t(\chi F)` is `+\xi\widehat{\chi F}`. Restricting to `\xi>0` proves (5).

Multiplying (5) by the integrating factor `e^{-\sigma\xi}` and integrating from `\sigma` to `\sigma_0` gives

\[
\begin{aligned}
e^{-\sigma_0\xi}H_{\sigma_0}(\xi)
-e^{-\sigma\xi}H_\sigma(\xi)
={}&i\int_\sigma^{\sigma_0}
e^{-u\xi}K_u(\xi)\,du\\
&+2\pi\!\sum_{\sigma<\beta<\sigma_0}
m_\rho\chi(\gamma)e^{-\beta\xi}e^{-i\gamma\xi},
\end{aligned}
\]

which is exactly (6).

The compact support of `\chi` makes all Fourier transforms in (4) well defined as tempered distributions even though `F` is only meromorphic. On vertical lines not passing through a zero they are ordinary transforms of a smooth compactly supported function. Equation (5) is the correct object across the exceptional values `\sigma=\beta` because the delta jump is retained explicitly.

## 2. One-pole sign check

The sign of the residue term matters. Take the model

\[
F(s)=\frac1{s-\rho},
\qquad \rho=\beta+i\gamma.
\]

Ignoring the cutoff for the moment, on a line to the left of the pole, `\sigma<\beta`,

\[
F(\sigma+it)
=\frac1{-(\beta-\sigma)+i(t-\gamma)}.
\]

Closing the Fourier contour for `\xi>0` in the lower half-plane gives

\[
\widehat{F(\sigma+i\cdot)}(\xi)
=-2\pi e^{-(\beta-\sigma)\xi}e^{-i\gamma\xi},
\qquad \xi>0,
\tag{9}
\]

whereas on a line to the right of the pole the positive-frequency transform is zero. Taking `H_{\sigma_0}=0` for `\sigma_0>\beta` and `K=0` in the unlocalized model, (6) reproduces (9) exactly. This fixes both the factor `2\pi` and the minus sign in the integrated residue term.

The same check also shows why the horizontal residue source cannot be dropped: crossing a zero changes the positive Hardy component by a finite exponential atom.

## 3. Exact relation to the safe-line barrier

On a safe line `\sigma_0>1`,

\[
F(\sigma_0+it)
=-\sum_{n\ge2}\Lambda(n)n^{-\sigma_0}e^{-it\log n}
+\frac1{\sigma_0-1+it}.
\tag{10}
\]

Every prime frequency in the Dirichlet series is strictly negative under (3), and the Cauchy term also has negative Fourier support. Thus the unlocalized positive Hardy component vanishes there. `WI-431` records that exact one-sided spectrum; `WI-432` quantifies what happens after multiplying by an adiabatic height window `\chi_T(t)=\chi(t/T)`: the safe-line leakage `H_{\sigma_0}` tends to zero, with the prime part decreasing faster than every power and the Cauchy tail costing only `O(T^{-1/2})` in `L^2`.

Equation (6) now shows exactly where the interior positive-frequency mass can come from despite that vanishing source term. It has only two places to hide:

1. explicit crossed-zero residues;
2. the transported edge forcing `P_+(\chi'F)`.

There is no third bulk source term. The prime information visible on `\sigma_0>1` is already contained in `H_{\sigma_0}` and is damped further by `e^{-(\sigma_0-\sigma)\xi}` during continuation.

For a plateau window, `\chi'` is supported only in the upper and lower transition zones. This makes the next desired estimate geometrically clear: bound the horizontal integral of the Hardy projection of `F` **at the height edges**, while leaving `\chi=1` on the target zero interval. However, (6) does not itself provide that bound. The edge integrand contains the full meromorphic continuation `F(u+it)`, not merely its absolutely convergent safe-line Dirichlet series.

That distinction prevents a false RH shortcut. Making the safe-line source small does not make `H_\sigma` small: the residue sum and the edge forcing are precisely the terms generated by analytic continuation into the strip.

## 4. Relation to the Kunik/Hardy factorization

`WI-429` used Kunik's Poisson--Schwarz/Blaschke factorization to show that, on an interior line, the positive-frequency projection isolates right-half zero defects deeper than that line. Equation (6) is the localized horizontal-transport version of the same phenomenon.

Formally taking a sequence of windows tending to `1`, under whatever tail bounds justify that limit, makes `\chi'` disappear and makes the safe-line positive projection vanish. Equation (6) then reduces to the pure residue expansion

\[
P_+F_\sigma
=-2\pi\!\sum_{\rho:\,\beta>\sigma}
m_\rho e^{-(\beta-\sigma)\xi}e^{-i\gamma\xi},
\qquad \xi>0,
\tag{11}
\]

which is the Fourier-side Hardy/Blaschke defect formula behind `WI-429`. The compactly localized formula therefore does not invent a new source of defect mass; it exposes the exact edge correction required when the global Hardy identity is cut to a finite height window.

This also clarifies the role of the commutator identity from `WI-431`,

\[
\chi P_+F=P_+(\chi F)-[P_+,\chi]F.
\tag{12}
\]

The term `K_u=P_+(\chi'F_u)` in (6) is a horizontal evolution term for that same localization defect. It is not an independent prime-only observable. Any attempt to upper-bound it by quantities that already assume control of the right-half zeros would be circular.

## 5. What would constitute a real bootstrap

The exact identity suggests a falsifiable defect-to-zero route. Choose a family of plateau windows that equal one on a target height interval and move their transition zones away from that interval. A genuine bootstrap would consist of an independently proved estimate of the form

\[
\left\|
\int_\sigma^{\sigma_0}
e^{-(u-\sigma)\xi}K_u(\xi)\,du
\right\|_{L^2(\xi>0)}
\le \mathcal E_T,
\tag{13}
\]

where `\mathcal E_T` is controlled by prime-side or boundary data and is quantitatively smaller than the `WI-430` first-defect energy quantum for any zero retained in the plateau. Together with the `WI-432` safe-line estimate, (6) would then force a contradiction unless the relevant right-half residue sum is absent.

The crucial word is **independently**. Standard pointwise bounds for `\zeta'/\zeta` inside the strip can themselves contain reciprocal distances to zeros. Substituting such a bound into (13) merely moves the defect from the explicit residue term into the edge estimate. The next audit should therefore classify candidate controls for `K_u` by whether they depend on zero-free distance, zero density, averaged boundary values, or genuinely source-side explicit-formula information.

A negative result would also be substantive: if every admissible estimate for the edge integral strong enough to beat the defect quantum can be shown to require equivalent control of the same right-half divisor, then the localized Hardy transport route is circular at this level and should be closed.

## Prior art and novelty audit

No novelty or priority claim is made for the distributional or Hardy-space ingredients.

- The identity `\bar\partial(1/z)=\pi\delta_0`, its meromorphic divisor version, and the corresponding Cauchy--Pompeiu/Poincare--Lelong calculus are classical. Equation (2) is their direct application to the pole-cancelled logarithmic derivative.
- Matthias Kunik, **Logarithmic Fourier integrals for the Riemann Zeta Function**, arXiv:0804.4829 (2008, revised 2009), derives zeta factorizations from symmetric Poisson--Schwarz formulas in `Re s>1/2` and explicitly separates critical-line integrals from Blaschke zero factors. This is the closest classical zeta-specific prior art to the Hardy/zero decomposition used in `WI-429`--`WI-431`; the present finding does not claim that the underlying residue mechanism is new.
- Joseph Najnudel and Ashkan Nikeghbali, **Cauchy laws for zeta logarithmic derivatives and stationary Stieltjes transforms**, arXiv:2609.15862v1 (14 Sep 2026; updated 15 Sep 2026), is a fresh unrefereed neighboring result. It compares a normalized critical-line logarithmic derivative with a Stieltjes transform of zero ordinates under the hypothesis that the total horizontal distance of right-half zeros is `o(T)`. Its published abstract therefore runs in the opposite logical direction from the desired bootstrap here: horizontal defect control is an input to the comparison, not a consequence of a safe-line localized Hardy transport estimate. It is contextual prior art only, not load-bearing evidence.
- `WI-429`--`WI-432` already established the local line-specific ingredients: Hardy selectivity for deeper defects, the first-defect energy quantum, the residue-only nature of the bare safe-line positive source, and the failure of adiabatic localization to create a persistent prime Hardy signal. A targeted repository and literature audit did not locate this exact cutoff-dependent horizontal evolution formula as an existing theorem. Absence from that audit is not evidence of priority; the durable contribution here is the exact bookkeeping and the resulting identification of the edge term as the sole non-residue continuation gate.

Relevant public sources: Kunik, https://arxiv.org/abs/0804.4829; Najnudel--Nikeghbali, https://arxiv.org/abs/2609.15862.

## Boundary, stress tests, and falsification

1. **Critical-line zeros are boundary data, not interior residues in (2).** The distribution identity is stated on the open half-plane `Re s>1/2`. It detects the right-half member of an off-line functional-equation pair. It does not reclassify multiple critical-line zeros as off-line defects.

2. **Endpoint lines must avoid zero abscissas.** If `\sigma` or `\sigma_0` equals some `\beta`, half-jump conventions have to be specified. The clean form (6) deliberately avoids that bookkeeping.

3. **The window derivative is indispensable.** Replacing (8) by `\chi\partial_\sigma F=-i\partial_t(\chi F)+residues` would miss the term `i\chi'F` and is false. This is exactly the localization error that the finding isolates.

4. **The sign is convention-dependent but internally fixed.** Equations (3), (5), (6), and the one-pole test (9) use the same `e^{-it\xi}` convention. Reversing the Fourier convention exchanges the Hardy half-spaces and changes the corresponding signs.

5. **No bound on the edge term is claimed.** Equation (13) is a research target, not an established estimate. In particular this finding does not improve the unconditional simple-critical proportion and does not prove RH.

6. **No independent-zero assumption is used.** Multiplicities enter as the exact residues `m_\rho`; zeros sharing an ordinate or real part are simply summed with multiplicity in the distributional formula.

## Research consequence

The `WI-432` continuation target is now no longer informal. The exact local balance is

\[
\boxed{
\text{interior localized Hardy signal}
=
\text{damped safe-line leakage}
-\text{edge forcing}
-\text{crossed-zero residues}.
}
\]

For adiabatic windows the first term is already controlled by `WI-432`. The next useful work should therefore focus narrowly on the edge forcing in (13): either derive a source-side estimate that is genuinely independent of the right-half divisor and compare it with `WI-430`'s first-defect quantum, or prove that every sufficiently strong edge estimate necessarily smuggles in equivalent zero information. Optimizing the safe-line leakage further cannot by itself advance the defect-to-zero program.