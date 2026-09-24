# WI-430 — Hardy-projected Kunik energy has a first-defect quantum

Status: `EXACT-DERIVED + STRUCTURAL-CONSTRAINT + DEFECT-TO-ZERO + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`

Parents: `WI-424`, `WI-426`, `WI-429`

## Claim

`WI-429` gives an exact Hardy/Riesz projection of Kunik's interior Blaschke logarithmic derivative which keeps precisely the zeros deeper than the probe line. Its positive pair formula has a stronger global consequence than was recorded there: the projected energy has a **uniform first-defect quantum**, and therefore gives an exact quantitative count coercivity for all zeros beyond any fixed horizontal depth.

Write every right-half off-critical zeta zero as

\[
\rho=\frac12+d_\rho+i\gamma_\rho,
\qquad 0<d_\rho<\frac12,
\]

with multiplicity \(m_\rho\). Fix

\[
0<a<\frac12.
\]

For \(T>0\), let

\[
F_a(T)=\{\rho:\ d_\rho>a,\ |\gamma_\rho|\le T\}
\]

and form the finite Kunik subproduct over this set. Define its positive-frequency projected energy by

\[
\mathcal E_a(T)
:=
\left\|
P_+\frac{B_{F_a(T)}'}{B_{F_a(T)}}
\left(\frac12+a+i\,\cdot\right)
\right\|_2^2.
\tag{1}
\]

Then `WI-429` gives exactly

\[
\mathcal E_a(T)
=
2\pi
\sum_{\rho,\rho'\in F_a(T)}
 m_\rho m_{\rho'}
\frac{\delta_\rho+\delta_{\rho'}}
{(\delta_\rho+\delta_{\rho'})^2+(\gamma_\rho-\gamma_{\rho'})^2},
\qquad
\delta_\rho=d_\rho-a>0.
\tag{2}
\]

Every summand is nonnegative. Retaining only the diagonal terms gives

\[
\mathcal E_a(T)
\ge
\pi\sum_{\rho\in F_a(T)}
\frac{m_\rho^2}{d_\rho-a}.
\tag{3}
\]

Because every nontrivial zeta zero satisfies \(\Re\rho<1\), one has

\[
d_\rho-a<\frac12-a.
\]

Hence each surviving zero contributes more than the universal amount

\[
\boxed{
q(a):=\frac{\pi}{\frac12-a},
}
\tag{4}
\]

per unit of multiplicity. If

\[
N_{>a}(T):=
\sum_{\rho\in F_a(T)}m_\rho,
\]

then

\[
\boxed{
\mathcal E_a(T)>q(a)N_{>a}(T)
\quad\text{whenever }N_{>a}(T)>0.
}
\tag{5}
\]

In particular,

\[
\boxed{
N_{>a}(T)
<
\frac{\frac12-a}{\pi}\,\mathcal E_a(T)
}
\tag{6}
\]

for every nonempty finite window. This estimate is independent of the ordinates and does not require spacing, density, or cancellation information.

Now define the extended canonical deeper-defect energy

\[
\boxed{
\mathcal E_a
:=
\sup_{T>0}\mathcal E_a(T)
\in[0,\infty].
}
\tag{7}
\]

The positivity of every pair term makes \(\mathcal E_a(T)\) monotone under enlargement of the finite zero set, so (7) is unambiguous. Then

\[
\boxed{
\mathcal E_a<\infty
\iff
\#\{\rho:\Re\rho>\tfrac12+a\}<\infty
}
\tag{8}
\]

when zeros are counted with multiplicity. Moreover,

\[
\boxed{
\mathcal E_a\le q(a)
\Longrightarrow
\zeta(s)\ne0
\quad(\Re s>\tfrac12+a).
}
\tag{9}
\]

Thus the first surviving off-line zero costs a fixed positive energy quantum. The threshold tends to

\[
q(a)\downarrow2\pi
\qquad(a\downarrow0).
\tag{10}
\]

This yields an exact defect-to-zero criterion for the canonical projected energy:

\[
\boxed{
\mathrm{RH}
\iff
\liminf_{a\downarrow0}\mathcal E_a\le2\pi.
}
\tag{11}
\]

The implication from right to left is strict in the non-RH case. If one right-half zero has depth \(d_0>0\), then for every \(0<a<d_0\),

\[
\mathcal E_a
\ge
\frac{\pi}{d_0-a},
\]

and therefore

\[
\liminf_{a\downarrow0}\mathcal E_a
\ge
\frac{\pi}{d_0}
>2\pi,
\tag{12}
\]

because \(d_0<1/2\). Conversely RH makes every \(F_a(T)\) empty and hence \(\mathcal E_a=0\).

Equation (11) is **not an RH proof** and must not be used as one. Its value is diagnostic: a global source-side bound on the Hardy-projected Kunik term near the critical boundary is not a mild regularity estimate. Once it reaches the subquantum scale in (9), or the asymptotic threshold in (11), it has already excluded every off-line zero. The safe target for unconditional work is therefore the localized finite-height inequality (6), together with an independently justified upper bound whose dependence on \(a\) and \(T\) is explicit.

## 1. Local count coercivity

For a finite set \(F_a(T)\), equation (3) is `WI-429`'s diagonal lower bound. Since

\[
0<d_\rho<\frac12,
\]

we have

\[
0<d_\rho-a<\frac12-a
\]

for every \(\rho\in F_a(T)\). Therefore

\[
\frac{1}{d_\rho-a}
>
\frac{1}{\frac12-a}.
\tag{13}
\]

Also \(m_\rho^2\ge m_\rho\). Substitution into (3) gives

\[
\begin{aligned}
\mathcal E_a(T)
&\ge
\pi\sum_{\rho\in F_a(T)}
\frac{m_\rho^2}{d_\rho-a}\\
&>
\frac{\pi}{\frac12-a}
\sum_{\rho\in F_a(T)}m_\rho\\
&=q(a)N_{>a}(T),
\end{aligned}
\tag{14}
\]

whenever the set is nonempty. This proves (5)--(6).

The constant is uniform over the entire critical strip. It is not sharp for a specified defect depth: a zero at depth \(d>a\) actually pays \(\pi/(d-a)\). The point of \(q(a)\) is that it removes all unknown zero parameters and leaves a threshold depending only on the predetermined probe line.

The same argument also separates multiplicity from geometry. A zero of multiplicity \(m\) pays at least

\[
\frac{\pi m^2}{d-a},
\]

so repeated zeros are more expensive than their contribution to the multiplicity count. No use is made of that extra quadratic gain in (6).

## 2. The global extended energy is finite exactly when the deep population is finite

The finite sets \(F_a(T)\) increase with \(T\), up to harmless choices when \(T\) hits an ordinate. By (2), adding zeros adds their positive diagonal terms and positive cross terms. Hence \(\mathcal E_a(T)\) is monotone and its supremum in (7) equals the extended positive double-series limit.

If there are infinitely many zeros with \(d_\rho>a\), then their multiplicity count \(N_{>a}(T)\) tends to infinity. Equation (5) forces

\[
\mathcal E_a(T)\to\infty,
\]

so \(\mathcal E_a=\infty\).

If there are only finitely many such zeros, choose \(T\) above all of their ordinates. Then the set stabilizes and (2) is a finite sum of finite positive terms, because every surviving depth satisfies \(d_\rho-a>0\). Thus \(\mathcal E_a<\infty\). This proves (8).

This equivalence is deliberately about the **canonical projected Blaschke defect energy**, not about an ordinary global \(L^2\) norm of \(\zeta'/\zeta\) on the line. `WI-429` already warns that the latter may have pole singularities and requires localization or a distributional formulation. No such global zeta-level norm is asserted here.

A useful consequence is that even proving mere finiteness of \(\mathcal E_a\) for one fixed \(a\) would already be a strong zero-density statement: it would say that only finitely many zeta zeros lie in the half-plane \(\Re s>1/2+a\). A proof of a small numerical upper bound is stronger still. This is a publication gate for any proposed source-side estimate: one must check that the hypothesis used to obtain the bound has not already smuggled in the same zero exclusion.

## 3. First-defect quantum and the cofinal boundary criterion

If at least one zero satisfies \(d_\rho>a\), equation (14) gives

\[
\mathcal E_a>q(a).
\tag{15}
\]

Therefore \(\mathcal E_a\le q(a)\) forces the deeper-zero set to be empty, proving (9). The functional equation then supplies the symmetric exclusion on the left of the critical line, but (9) itself only needs the right-half formulation.

Now suppose RH is false. By the functional equation there is at least one zero on the right of the critical line; fix one with depth \(d_0\in(0,1/2)\). For every sufficiently small \(a>0\), that zero survives the Hardy projection. Its diagonal contribution alone gives

\[
\mathcal E_a
\ge
\frac{\pi m_0^2}{d_0-a}
\ge
\frac{\pi}{d_0-a}.
\tag{16}
\]

Taking \(a\downarrow0\) proves (12). Since \(d_0<1/2\), the limit lower bound is strictly greater than \(2\pi\). Under RH the energy vanishes identically. This proves (11).

The same argument works along any predetermined cofinal sequence \(a_n\downarrow0\). Thus, for example,

\[
\liminf_{n\to\infty}\mathcal E_{a_n}\le2\pi
\]

already implies RH. This does not require choosing the line after seeing an unknown zero. What remains difficult is obtaining the required upper bound from independent arithmetic data.

There is no contradiction with `WI-426`. That finding integrates the unprojected line energy through the unknown pole depth and obtains a locally nonintegrable strip singularity. Here no depth continuum is integrated. Instead, each predetermined line is projected by a norm-one Hardy operator, and the conclusion follows from the positive energy of whatever defects lie deeper than that line. The price is transferred entirely to the source-side control of the resulting one-dimensional projected energy.

## 4. Relation to the current defect-to-zero program

`WI-424` gives the critical-boundary Poisson flux and its reciprocal-depth \(L^2\) tariff. `WI-425`--`WI-428` show that fixed-safe-strip processing is cubically blind to shallow defects. `WI-429` crosses the geometric threshold and isolates the deeper population by Hardy projection.

The new conclusion is that the surviving projected energy is already a quantitative defect counter:

\[
N_{>a}(T)
<
\frac{\frac12-a}{\pi}\mathcal E_a(T).
\tag{17}
\]

This is stronger than saying merely that a defect is visible. It gives an explicit conversion from any independently proved projected-energy upper bound into a count bound, with no unknown horizontal depth on the right-hand side.

For the main research mandate, this clarifies what a useful bootstrap would have to look like. A source-side estimate of the form

\[
\mathcal E_a(T)\le U(a,T)
\]

immediately yields

\[
N_{>a}(T)
<
\frac{\frac12-a}{\pi}U(a,T).
\tag{18}
\]

If the bound is global in height and eventually falls at or below \(q(a)\), the defect is eliminated outright. If only localized bounds are available, (18) can still be combined with zero-density or height-local information without pretending that the uncertified complement consists solely of off-line zeros.

The next useful source-side question is therefore narrower than a global `L^2` theorem for \(\zeta'/\zeta\): can Kunik's projected identity from `WI-429` be localized in height with boundary errors small enough to bound \(\mathcal E_a(T)\) from independently accessible prime-side or critical-line data? The present finding supplies the exact target constant against which such a theorem must be measured.

## Prior art and novelty audit

No novelty or priority claim is made.

- The analytic input is exactly the Kunik/Hardy projection identity and positive pair formula established and source-audited in `WI-429`, ultimately based on Matthias Kunik, *Logarithmic Fourier integrals for the Riemann Zeta Function*, arXiv:0804.4829v2 (2009). No new literature theorem is imported here.
- `WI-424` already proves the boundary Poisson-flux count relation and the diagonal tariff \(2\pi/d\). It does not record the fixed-interior Hardy-projected count bound (6), the global finiteness equivalence (8), or the first-defect threshold (9).
- `WI-426` proves that positive multiscale unprojected `L^2` energy is either safe-strip blind or singular when integrated through possible zero depths. Its RH-equivalent strip-integrability criterion is driven by local pole nonintegrability. The criterion (11) here is different: it uses no strip integral and follows from a positive one-dimensional Hardy-projected energy quantum on a cofinal family of predetermined lines.
- `WI-429` proves the exact projection and finite-set lower bound but explicitly stops before a full-zeta/global-norm conclusion because convergence and source independence are unresolved. The present statement preserves that warning by defining \(\mathcal E_a\) monotonically from finite subproducts. The repository-local delta is the count coercivity, the extended-energy finiteness classification, and the resulting subquantum/cofinal defect-to-zero criterion.
- A targeted external audit found neighboring literature on growth and integrability of derivatives/logarithmic derivatives of Blaschke products, including Heittokangas and the later Zabolotskyi--Gal--Mostova work on logarithmic derivatives and zero counting. That literature concerns general growth/zero-distribution relations; the audit did not locate this exact zeta/Kunik Hardy-projected threshold packaging. Absence from the search is not evidence of priority.

## Boundary, stress tests, and falsification

1. **The global object is an extended positive energy, not an asserted full-line source norm.** Equation (7) is defined through finite Kunik subproducts and monotone positive pair energies. Identifying it with a global Hardy projection of the full zeta logarithmic derivative would require a separate convergence theorem.

2. **The result does not provide the upper bound.** All inequalities here run from the unknown defect set to a lower bound on its canonical energy. An arithmetic proof still needs an independently controlled upper estimate. Deriving that estimate from the same off-line zero set would be circular.

3. **The threshold uses the known strip bound \(0<\Re\rho<1\).** The universal quantum \(q(a)\) is obtained by replacing the unknown \(d_\rho\) with its maximal possible value \(1/2\). Better a priori horizontal localization would raise the quantum and strengthen the count conversion.

4. **Multiplicity only helps.** The passage from \(m_\rho^2\) to \(m_\rho\) discards a positive amount. The count bound is therefore valid for multiplicity-weighted zeros and is not relying on simplicity.

5. **No statement is made about multiple critical-line zeros.** They have \(d=0\) and do not enter the right-half Kunik defect set. This finding addresses only the off-line component of the uncertified complement, as required by the line mandate.

6. **The RH criterion is intentionally diagnostic.** It is falsified if one can produce a non-RH right-half zero configuration for which the positive pair formula of `WI-429` has \(\liminf_{a\downarrow0}\mathcal E_a\le2\pi\). The one-zero diagonal contribution (16) excludes that exactly.

The substantive consequence is a clean source-control gate: **localized projected energy gives an unconditional quantitative deep-zero count, while global subquantum control is already a zero-free theorem.** Future Kunik/Hardy work should therefore seek a genuinely independent localized bound first, not assume global Hardy-energy regularity as an innocuous analytic hypothesis.
