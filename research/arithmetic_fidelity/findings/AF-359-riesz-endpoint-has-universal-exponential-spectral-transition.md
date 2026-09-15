# AF-359 — Riesz endpoint comparison has a universal exponential spectral transition

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `ARITHMETIC-FIDELITY`, `QUANTITATIVE-FIDELITY`, `MOVING-PARAMETER-OBSTRUCTION`, `ZERO-SENSITIVE-SOURCE`, `CONDITIONAL-RH`, `NO-NOVELTY-CLAIM`

## Claim

Retain AF-358's logarithmically normalized Riesz family and assume RH. For a distinct positive zeta-zero ordinate `gamma`, with multiplicity `m_gamma`, write

\[
\rho_\gamma=\frac12+i\gamma,
\qquad
b_\delta(\rho)
=
\frac{\Gamma(\rho)\Gamma(1+\delta)}{\Gamma(\rho+1+\delta)},
\tag{1}
\]

and introduce the exact relative Riesz multiplier

\[
M_\delta(\rho)
:=
\rho b_\delta(\rho)
=
\Gamma(1+\delta)\frac{\Gamma(\rho+1)}{\Gamma(\rho+1+\delta)}.
\tag{2}
\]

Thus the nontrivial-zero coefficients satisfy

\[
\widehat E_\delta(\gamma)
=M_\delta(\rho_\gamma)\widehat E_0(\gamma),
\qquad
\widehat E_\delta(\gamma)-\widehat E_0(\gamma)
=
\bigl(M_\delta(\rho_\gamma)-1\bigr)\widehat E_0(\gamma).
\tag{3}
\]

For `T>0`, define the critical half-derivative shell energies

\[
\mathcal A_\delta(T)
:=
2\sum_{T<\gamma\le2T}
(1+\gamma^2)^{1/2}
\left|\widehat E_\delta(\gamma)\right|^2,
\tag{4}
\]

and

\[
\mathcal D_\delta(T)
:=
2\sum_{T<\gamma\le2T}
(1+\gamma^2)^{1/2}
\left|\widehat E_\delta(\gamma)-\widehat E_0(\gamma)\right|^2.
\tag{5}
\]

Let `delta_j -> 0+` and `T_j -> infinity`. If

\[
\delta_j\log T_j\longrightarrow u\in[0,\infty],
\tag{6}
\]

then, with `e^{-\infty}:=0`,

\[
\boxed{
\frac{\mathcal A_{\delta_j}(T_j)}{\mathcal A_0(T_j)}
\longrightarrow e^{-2u}
}
\tag{7}
\]

and

\[
\boxed{
\frac{\mathcal D_{\delta_j}(T_j)}{\mathcal A_0(T_j)}
\longrightarrow \bigl(1-e^{-u}\bigr)^2.
}
\tag{8}
\]

The transition therefore occurs at the **exponential zero-frequency scale**

\[
T\asymp \exp\!\left(\frac{1}{\delta}\right).
\tag{9}
\]

More precisely, if `T_delta = exp((u+o(1))/delta)` for a fixed `u>0`, then the smoothed profile retains the fraction `e^{-2u}` of the endpoint critical shell energy, while the endpoint difference carries the fraction `(1-e^{-u})^2`. If instead

\[
\delta\log T_\delta\to0,
\tag{10}
\]

then the relative shell defect in `(8)` tends to zero. If

\[
\delta\log T_\delta\to\infty,
\tag{11}
\]

then the smoothed shell becomes negligible relative to the endpoint shell and the difference carries asymptotically all of the endpoint critical energy.

Thus AF-358's fixed-`delta` half-derivative obstruction has a sharp two-parameter form: **subexponential spectral bandwidth in `1/delta` is asymptotically blind to the singular endpoint tail, while an order-one fraction of that tail first appears at frequencies exponential in `1/delta`.**

This is the spectral counterpart of AF-357's Beta-kernel law

\[
-\delta\log W_\delta\Rightarrow\operatorname{Exp}(1),
\tag{12}
\]

which places a fixed amount of physical kernel mass at relative lags `W_delta=exp(-Theta(1/delta))`. The reciprocal exponential scales in `(9)` and `(12)` are not asserted to be a general uncertainty principle; here they arise directly from the exact Riesz multiplier on the zeta-zero side and the exact Beta kernel on the source side.

## Derivation

### 1. The moving-order multiplier has a uniform shell limit

Equation `(2)` is convenient because it removes the endpoint factor `1/rho` exactly. For `0<=delta<=1`, use

\[
\log M_\delta(\rho)
=
\log\Gamma(1+\delta)
-
\int_0^\delta \psi(\rho+1+t)\,dt,
\tag{13}
\]

where `psi=Gamma'/Gamma`. In the vertical sector containing `rho_gamma`, the classical uniform asymptotic

\[
\psi(z)=\log z+O(|z|^{-1})
\tag{14}
\]

holds, and the error remains uniform for the bounded shift `0<=t<=1`. Hence

\[
\log M_\delta(\rho_\gamma)
=
-\delta\log\rho_\gamma
+O(\delta)+O\!\left(\frac{\delta}{\gamma}\right),
\tag{15}
\]

uniformly for `0<=delta<=1` and large `gamma`. Equivalently, this is the compact-parameter form of the standard Gamma-ratio asymptotic.

Now restrict to `T<gamma<=2T`. Uniformly on that shell,

\[
\log|\rho_\gamma|
=
\log T+O(1),
\qquad
\arg\rho_\gamma=O(1).
\tag{16}
\]

Therefore, whenever `delta_j -> 0`, `T_j -> infinity`, and `delta_j log T_j -> u`,

\[
\sup_{T_j<\gamma\le2T_j}
\left|M_{\delta_j}(\rho_\gamma)-e^{-u}\right|
\longrightarrow0.
\tag{17}
\]

For finite `u`, the phase `exp(-i delta_j arg rho_gamma)` tends uniformly to `1`; for `u=infinity`, `(15)` gives uniform decay of the multiplier magnitude to zero. This is the decisive moving-parameter statement missing from AF-358's fixed-order asymptotics.

### 2. Critical shell ratios are weighted averages of the same multiplier

From `(3)`, define positive endpoint weights

\[
w_\gamma(T)
:=
2(1+\gamma^2)^{1/2}
\left|\widehat E_0(\gamma)\right|^2
=
2m_\gamma^2(1+\gamma^2)^{1/2}|\rho_\gamma|^{-2}.
\tag{18}
\]

Then exactly

\[
\frac{\mathcal A_\delta(T)}{\mathcal A_0(T)}
=
\frac{\sum_{T<\gamma\le2T}w_\gamma(T)|M_\delta(\rho_\gamma)|^2}
{\sum_{T<\gamma\le2T}w_\gamma(T)},
\tag{19}
\]

and

\[
\frac{\mathcal D_\delta(T)}{\mathcal A_0(T)}
=
\frac{\sum_{T<\gamma\le2T}w_\gamma(T)|M_\delta(\rho_\gamma)-1|^2}
{\sum_{T<\gamma\le2T}w_\gamma(T)}.
\tag{20}
\]

Riemann--von Mangoldt guarantees that the denominator is nonzero for every sufficiently large dyadic shell. Because `(17)` is uniform across the shell, the weighted averages `(19)`--`(20)` converge to the corresponding constants, proving `(7)`--`(8)`.

No simplicity assumption enters. Repeated zeros merely alter the positive weights through `m_gamma^2` and cancel from the limiting ratio.

### 3. The critical shell has an explicit exponential detection law

For any desired relative defect fraction `theta in (0,1)`, equation `(8)` reaches that fraction when

\[
\bigl(1-e^{-u}\bigr)^2=\theta,
\qquad
u_\theta
:=-\log(1-\sqrt\theta).
\tag{21}
\]

Thus an order-one relative defect requires

\[
\log T
\asymp
\frac1\delta,
\tag{22}
\]

and the precise transition location for fraction `theta` is

\[
T
=
\exp\!\left(\frac{\nu_\theta+o(1)}{\delta}\right).
\tag{23}
\]

Any cutoff with `log T=o(1/delta)` lies strictly before this transition. Conversely, once `delta log T -> infinity`, the fixed positive-order multiplier has died relative to the endpoint coefficient and `(8)` tends to one.

This sharpens the qualitative statement in AF-358 that frequencies `gamma >> exp(1/delta)` look endpoint-sized in the difference. The relevant scale is not only an upper/lower heuristic: after normalization by the actual endpoint shell energy, the entire transition profile is the universal function `(1-e^{-u})^2`.

## Arithmetic-fidelity interpretation

AF-357 and AF-358 left a specific ambiguity. The physical Beta kernel showed exponentially thin endpoint localization, while the quadratic spectral result showed that every fixed positive order eventually differs from the endpoint by an unsmoothed `1/rho` tail. Neither result by itself quantified what happens when the smoothing order and zero height move together.

Equations `(7)`--`(8)` close that gap. The singular endpoint is not visible at an ordinary polynomial bandwidth in `1/delta`: if `T_delta=delta^{-A}` for fixed `A`, then `delta log T_delta -> 0` and the relative critical-shell defect vanishes. To expose a fixed fraction of the endpoint tail one must reach `T_delta=exp(Theta(1/delta))`.

This matters for the live fidelity question because it prices the missing resource more sharply. A proposed moving-order argument that only controls zero modes through subexponential height cannot see the coefficient-level transition responsible for the endpoint obstruction. A successful route to uniform endpoint fidelity must therefore either reach this exponentially moving spectral band or exploit source-native phase/cancellation information that bypasses magnitude-only shell energy altogether.

The result does **not** show that exponentially high zero information is logically necessary for every possible arithmetic proof. It is a no-go statement for the present Riesz coefficient channel and its quadratic magnitude diagnostics. Phase-sensitive, maximal, signed short-interval, cross-scale, or other nonlinear arithmetic information may encode the endpoint earlier.

## Boundaries and falsification

- The result assumes RH so that the normalized nontrivial-zero terms are Fourier modes with real ordinates and the AF-358 shell interpretation applies.
- The shell normalization is relative to `mathcal A_0(T)`. Both the endpoint and the fixed-positive-order difference have divergent global `H^{1/2}_{B,zeta}` energy; `(7)`--`(8)` describe how that divergence is distributed across moving dyadic shells, not a finite global norm.
- No simplicity, pair-correlation, linear-independence, or multiplicity conjecture is used. Multiplicity enters only through the positive weights `(18)`.
- The transition profile is specific to the Riesz multiplier `(2)`. It does not automatically transfer to a different smoothing family unless its high-frequency multiplier has an audited joint small-parameter/high-frequency asymptotic.
- The result is magnitude-based. It deliberately discards cross-frequency phase cancellation, so it cannot rule out a source-native phase mechanism.
- At `u=0`, `(8)` gives relative convergence to zero but does not by itself claim a sharp rate for an arbitrary simultaneous path. AF-356's coefficient estimate supplies rates in stricter regimes when needed.
- The match between spectral scale `exp(+Theta(1/delta))` and physical relative lag `exp(-Theta(1/delta))` is a comparison of two exact descriptions of this Riesz family, not a general Fourier-uncertainty theorem.

A direct falsification would require failure of the exact coefficient factorization `(3)` or of the compact-parameter Gamma/psi asymptotic leading to `(17)`. Both are classical analytic inputs. A narrower falsification is to exhibit a moving sequence `delta_j,T_j` with the declared product limit for which `M_delta(rho)` does not converge uniformly on the dyadic shell; `(13)`--`(16)` exclude such a sequence.

## Source / prior-art audit

The Riesz multiplier itself is classical. G. H. Hardy and J. E. Littlewood, **“Contributions to the Theory of the Riemann Zeta-Function and the Theory of the Distribution of Primes,”** *Acta Mathematica* **41** (1916), 119--196, DOI `10.1007/BF02422942`, gives the Riesz mean

\[
\sum_{n\le x}\left(1-\frac nx\right)^\delta\Lambda(n)
\]

and its explicit-formula zero multiplier `Gamma(1+delta) Gamma(rho) / Gamma(1+delta+rho)`; their formulas (2.251)--(2.252) are the direct classical ancestor of `(1)`--`(3)`.

NIST DLMF §5.11 records the standard vertical-sector asymptotics for `psi(z)` and for Gamma-function ratios, including Eqs. 5.11.12--5.11.13. Applying the `psi` asymptotic inside the exact integral `(13)` gives the uniform compact-parameter form used here. Riemann--von Mangoldt zero counting is classical; see E. C. Titchmarsh, revised by D. R. Heath-Brown, *The Theory of the Riemann Zeta-function*, 2nd ed., Oxford (1986), Chapter 9.

A targeted search over Riesz means of the von Mangoldt function, small-order Riesz limits, Gamma-ratio asymptotics, and Sobolev/Besicovitch formulations did not locate the specific simultaneous law `(7)`--`(8)` with `delta log T -> u`. Absence from that search is not evidence of novelty. The durable contribution claimed here is narrower: the classical Riesz multiplier, when combined with AF-358's critical-shell fidelity metric, yields an exact moving-bandwidth obstruction and identifies the exponential spectral scale at which endpoint loss becomes order one.