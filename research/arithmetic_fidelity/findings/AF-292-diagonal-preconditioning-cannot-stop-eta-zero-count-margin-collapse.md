# AF-292 — Optimal diagonal preconditioning cannot stop eta zero-count margin collapse in the RH-relevant half-plane

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `ZERO-COUNT`, `TARGET-RELATIVE`, `CONDITIONING`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-291 leaves open whether the vanishing relative zero-count margin of raw Dirichlet eta truncations is merely an artifact of the unweighted coefficient `ell^2` geometry. For the full class of invertible **diagonal Hilbert preconditioners**, the answer is exact: coordinatewise reweighting can improve the breadth law in some right-half-plane regimes, but it cannot prevent the normalized margin from vanishing on any fixed contour whose left edge lies at or to the left of `Re(s)=1`. In the genuinely RH-relevant case, where a contour surrounds critical-line zeros and therefore has left edge strictly below `1/2`, even the decay exponent from AF-291 is already optimal among all diagonal reweightings.

Let

\[
\eta_N(s)=\sum_{n=1}^N(-1)^{n-1}n^{-s},
\qquad
b^{(N)}_n=(-1)^{n-1},
\]

and let `Gamma` be a fixed compact rectifiable Jordan curve contained in `Re(s)>0` on which `eta` has no zero. Write

\[
\alpha:=\min_{z\in\Gamma}\operatorname{Re}z>0.
\]

Choose arbitrary positive diagonal weights

\[
D_N=\operatorname{diag}(d_1,\ldots,d_N),
\qquad d_n>0,
\]

which may depend on `N` and on `Gamma`. Measure coefficient perturbations in the weighted Hilbert norm

\[
\|c\|_{D_N}:=\|D_Nc\|_2
=\left(\sum_{n\le N}d_n^2|c_n|^2\right)^{1/2}.
\]

Let `Delta_{Gamma,N}` be AF-290's boundary-zero discriminant: the set of coefficient vectors whose degree-`N` Dirichlet polynomial has a zero somewhere on `Gamma`. Define the normalized weighted margin

\[
\delta^{(D)}_{\Gamma,N}
:=
\frac{\operatorname{dist}_{D_N}(b^{(N)},\Delta_{\Gamma,N})}
{\|b^{(N)}\|_{D_N}}.
\]

Then for all sufficiently large `N`, with constants depending only on `Gamma`,

\[
\boxed{
\delta^{(D)}_{\Gamma,N}
\asymp_{\Gamma}
\frac{1}
{\left(\sum_{n\le N}d_n^2\right)^{1/2}
 \left(\sum_{n\le N}d_n^{-2}n^{-2\alpha}\right)^{1/2}}.
}
\]

Consequently,

\[
\boxed{
\sup_{D_N\ \mathrm{diagonal}}
\delta^{(D)}_{\Gamma,N}
\asymp_{\Gamma}
\frac{1}{\sum_{n\le N}n^{-\alpha}}.
}
\]

The optimum is attained, up to an irrelevant common scale, by the explicit weights

\[
\boxed{d_n^2\propto n^{-\alpha},\qquad d_n\propto n^{-\alpha/2}.}
\]

Thus the best possible diagonal breadth law is

\[
\boxed{
\sup_D\delta^{(D)}_{\Gamma,N}
\asymp_{\Gamma}
\begin{cases}
N^{\alpha-1}, & 0<\alpha<1,\\[1mm]
(\log N)^{-1}, & \alpha=1,\\[1mm]
1, & \alpha>1.
\end{cases}
}
\]

In particular, **every diagonal preconditioner still has vanishing best-case normalized zero-count radius whenever `alpha<=1`**. If `Gamma` surrounds any point on the critical line, then necessarily `alpha<1/2`, and the optimal diagonal rate `N^{alpha-1}` has exactly the same power of `N` as the raw AF-291 rate. Diagonal reweighting cannot improve the critical-strip exponent at all.

## Exact weighted distance to the boundary-zero discriminant

AF-290 is a Hilbert-space distance-to-hyperplane calculation, so it extends immediately to a diagonal coefficient metric once the dual evaluation norm is recomputed.

For fixed `z`, evaluation is

\[
L_z(c)=\sum_{n\le N}c_n n^{-z}.
\]

Under the change of coordinates `x=D_Nc`,

\[
L_z(D_N^{-1}x)
=
\sum_{n\le N}x_n d_n^{-1}n^{-z}.
\]

Hence the operator norm of evaluation in the weighted coefficient geometry is

\[
\|L_z\|_{D_N,*}
=
\left(\sum_{n\le N}d_n^{-2}n^{-2\operatorname{Re}z}\right)^{1/2}.
\]

Distance to the hyperplane `ker L_z` is therefore

\[
\operatorname{dist}_{D_N}(b^{(N)},\ker L_z)
=
\frac{|\eta_N(z)|}
{\left(\sum_{n\le N}d_n^{-2}n^{-2\operatorname{Re}z}\right)^{1/2}}.
\]

Taking the minimum over the compact boundary gives the exact weighted analogue of AF-290:

\[
\operatorname{dist}_{D_N}(b^{(N)},\Delta_{\Gamma,N})
=
\min_{z\in\Gamma}
\frac{|\eta_N(z)|}
{\left(\sum_{n\le N}d_n^{-2}n^{-2\operatorname{Re}z}\right)^{1/2}}.
\]

As in AF-291, local uniform convergence `eta_N -> eta` on `Re(s)>0` and the zero-free boundary imply constants `0<m_Gamma<=M_Gamma<infinity`, independent of `N`, such that for all sufficiently large `N`,

\[
m_\Gamma\le |\eta_N(z)|\le M_\Gamma
\qquad(z\in\Gamma).
\]

The weighted evaluation norm is decreasing in `Re(z)`. If `z_* in Gamma` satisfies `Re(z_*)=alpha`, compactness gives

\[
\frac{m_\Gamma}
{\left(\sum d_n^{-2}n^{-2\alpha}\right)^{1/2}}
\le
\operatorname{dist}_{D_N}(b^{(N)},\Delta_{\Gamma,N})
\le
\frac{M_\Gamma}
{\left(\sum d_n^{-2}n^{-2\alpha}\right)^{1/2}}.
\]

Since `|b_n^(N)|=1`,

\[
\|b^{(N)}\|_{D_N}
=
\left(\sum_{n\le N}d_n^2\right)^{1/2},
\]

which proves the first displayed equivalence. The constants are uniform over **all** positive diagonal choices, including weights that depend on `N`; no compactness or bounded-condition-number hypothesis on `D_N` is being smuggled into the result.

A complex diagonal change of coordinates gives nothing additional: only the moduli `|d_n|` enter the source norm and the dual evaluation norm, so positive weights are without loss for this Euclidean diagonal class.

## Cauchy-Schwarz gives the exact optimal diagonal geometry

Set

\[
A_D^2:=\sum_{n\le N}d_n^2,
\qquad
B_D^2:=\sum_{n\le N}d_n^{-2}n^{-2\alpha}.
\]

Cauchy-Schwarz applied to the sequences `d_n` and `d_n^{-1}n^{-alpha}` gives

\[
A_DB_D
\ge
\sum_{n\le N}n^{-\alpha}.
\]

Equality holds exactly when the two sequences are proportional, equivalently

\[
d_n^2=c\,n^{-\alpha}
\]

for one common `c>0`. Therefore every diagonal metric obeys

\[
\delta^{(D)}_{\Gamma,N}
\le
\frac{M_\Gamma}{\sum_{n\le N}n^{-\alpha}},
\]

while the equality-case weights satisfy

\[
\delta^{(D_*)}_{\Gamma,N}
\ge
\frac{m_\Gamma}{\sum_{n\le N}n^{-\alpha}}.
\]

This proves the optimal asymptotic law and shows that allowing the preconditioner to adapt arbitrarily with `N` cannot escape it.

The common scaling `D_N -> cD_N` cancels between source size and dual evaluation norm. The optimization is therefore genuinely projective in the diagonal metric, as a normalized conditioning quantity should be.

## Comparison with the raw eta geometry

AF-291 gives, in the unweighted geometry,

\[
\delta_{\Gamma,N}^{(I)}
\asymp
\frac{1}{\sqrt N\,H_N(\alpha)}.
\]

The diagonal optimum separates three behaviors inside `0<alpha<1`.

For `0<alpha<1/2`,

\[
\delta_{\Gamma,N}^{(I)}\asymp N^{\alpha-1}
\]

already has the optimal diagonal power. Coordinate reweighting can change constants but not the breadth exponent.

At `alpha=1/2`, raw coordinates pay an additional factor `(log N)^(-1/2)`:

\[
\delta_{\Gamma,N}^{(I)}\asymp (N\log N)^{-1/2},
\qquad
\sup_D\delta_{\Gamma,N}^{(D)}\asymp N^{-1/2}.
\]

So the optimal diagonal metric removes that logarithmic penalty, but the radius still vanishes.

For `1/2<alpha<1`, the raw margin is `N^{-1/2}` while the optimum is `N^{alpha-1}`. Diagonal preconditioning can materially improve conditioning there, but cannot make it breadth-uniform until the contour moves strictly to the right of `Re(s)=1`.

At `alpha=1` the best radius is only `1/log N`; for `alpha>1` the sum `sum n^{-alpha}` is bounded and a nonvanishing diagonal margin becomes possible. The transition therefore occurs exactly at the abscissa where the `ell^1` evaluation profile `sum n^{-alpha}` changes from divergent to summable.

## Critical-strip consequence

For a Jordan domain to contain a zero on `Re(s)=1/2` as an interior point, its boundary must extend to some real part strictly less than `1/2`. Hence any fixed contour used to count a finite set of critical-line zeta zeros through the eta representation has

\[
0<\alpha<\frac12.
\]

On exactly that regime,

\[
\sup_D\delta^{(D)}_{\Gamma,N}
\asymp N^{\alpha-1},
\]

which is the same `N`-power already present in AF-291's raw coefficient geometry.

This closes the simplest preconditioning escape from AF-291. The collapse is not just a poor choice of coordinate scales. Within every coordinatewise Hilbert renorming, the source-size factor and the dual evaluation factor obey an uncertainty-like product constraint whose minimum is the `ell^1` mass of the boundary evaluation profile.

Any genuinely better RH-relevant conditioning mechanism must therefore leave this class: for example through non-diagonal relational mixing, a nonlinear representation, a quotient that removes target-irrelevant source directions, or a different target/source topology with its own recovery theorem. AF-292 does **not** assert that any of those larger classes also fail.

## Prior art and novelty assessment

The ingredients are classical and no broad novelty is claimed.

- Weighted Hilbert spaces of Dirichlet series are standard. Athanasios Kouroupis and Karl-Mikael Perfekt, **“Composition operators on weighted Hilbert spaces of Dirichlet series,”** *Journal of the London Mathematical Society* 108(2), 680–715 (2023), DOI `10.1112/jlms.12771`, study coefficient-weighted Dirichlet-series Hilbert spaces and use the corresponding weighted reproducing kernels and point-evaluation norms.
- John E. McCarthy and Orr Moshe Shalit, **“Spaces of Dirichlet series with the complete Pick property,”** *Israel Journal of Mathematics* 220(2), 509–530 (2017), DOI `10.1007/s11856-017-1527-6`, treat reproducing-kernel Hilbert spaces with Dirichlet kernels of the form `k(s,u)=sum a_n n^(-s-conj(u))`, providing established RKHS language for positive coefficient weights and evaluation geometry.
- The optimization of `A_D B_D` is the elementary equality case of Cauchy-Schwarz. AF-290 already supplies the distance-to-boundary-zero theorem, and AF-291 supplies the compact-uniform eta boundary bounds.

The retained Arithmetic Fidelity result is the composition of those elementary structures into the exact channel question left by AF-291: **how much of the vanishing eta zero-count margin can any coordinatewise Hilbert preconditioner repair?** The answer is a complete optimizer and a sharp no-go boundary. No novelty is claimed for weighted Dirichlet spaces, reproducing kernels, Cauchy-Schwarz, eta truncations, or zero-count perturbation theory.

## Boundaries and failure modes

- The result optimizes only diagonal/in-coordinate Hilbert metrics. A general positive-definite coefficient metric can mix coordinates, and a nonlinear encoder can change the geometry more radically. Neither is ruled out.
- The target is still finite zero count inside a fixed compact contour. Exact zero locations, multiplicities, growing-height windows, global zero divisors, and RH require additional target control.
- The conclusion is relative to perturbation size normalized by the weighted source norm. It does not say `eta_N` itself has unstable zero counts; AF-291's compact-uniform convergence still gives the correct eventual zero count on a fixed zero-free boundary.
- The optimal weights depend on the contour through `alpha`. Treating that dependence as allowed only strengthens the obstruction: even a target-aware, `N`-dependent diagonal metric cannot beat the stated law.
- The `alpha>1` regime does admit a nonvanishing optimal diagonal margin, so the theorem is not a blanket statement that diagonal weighting never works. Its obstruction is precisely aligned with the non-summability of the evaluation profile at and left of `Re(s)=1`.
- Nothing here proves RH or excludes a non-diagonal or nonlinear route from arithmetic data to a zero-sensitive target.

## Consequence for the research line

AF-291's phrase “different coefficient norm or preconditioner” can now be narrowed. **Positive diagonal Hilbert renorming is fully classified and is insufficient in every RH-relevant zero-count window.** The next meaningful escape test must introduce genuinely relational source geometry rather than merely rescale individual Dirichlet coordinates, and it must show that the improved source geometry composes with AF-290's target discriminant rather than hiding the same breadth bill in a different norm.