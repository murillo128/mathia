# AF-356 — Riesz endpoint is Lipschitz-stable in B² while the uniform critical norm is singular

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `QUANTITATIVE-FIDELITY`, `ZERO-SENSITIVE-SOURCE`, `TARGET-METRIC-CALIBRATION`, `CONDITIONAL-RH`, `NO-NOVELTY-CLAIM`

## Claim

Retain AF-352--AF-355's Riesz family

\[
\mathcal R_\delta[\Lambda-1](X)
:=
\sum_{n\le X}(\Lambda(n)-1)\left(1-\frac nX\right)^\delta,
\qquad \delta\ge0,
\tag{1}
\]

and put, on logarithmic scale,

\[
E_\delta(y)
:=
e^{-y/2}\mathcal R_\delta[\Lambda-1](e^y).
\tag{2}
\]

For a locally square-integrable function on `[0,\infty)`, write

\[
\|f\|_{B^2}^2
:=
\limsup_{Y\to\infty}\frac1Y\int_0^Y |f(y)|^2\,dy.
\tag{3}
\]

Assume RH. Then the Riesz family is **Lipschitz-continuous at the unsmoothed endpoint in logarithmic Besicovitch mean square**:

\[
\boxed{
\|E_\delta-E_0\|_{B^2}=O(\delta)
\qquad (\delta\downarrow0).
}
\tag{4}
\]

More precisely, after grouping repeated zeros by distinct positive ordinates `gamma`, with multiplicity `m_gamma` and

\[
\rho_\gamma=\frac12+i\gamma,
\qquad
b_\delta(\rho)
:=
B(\rho,1+\delta)
=
\frac{\Gamma(\rho)\Gamma(1+\delta)}{\Gamma(\rho+1+\delta)},
\tag{5}
\]

the `B^2` Fourier coefficients satisfy

\[
\widehat E_\delta(\gamma)
=-m_\gamma b_\delta(\rho_\gamma),
\qquad
\widehat E_0(\gamma)
=-\frac{m_\gamma}{\rho_\gamma},
\tag{6}
\]

and therefore

\[
\boxed{
\|E_\delta-E_0\|_{B^2}^2
=
2\sum_{\gamma>0}m_\gamma^2
\left|
B(\rho_\gamma,1+\delta)-\frac1{\rho_\gamma}
\right|^2.
}
\tag{7}
\]

The right side is `O(delta^2)`.

Consequently, if `mu_delta` denotes the limiting distribution of `E_delta`, then in bounded-Lipschitz distance

\[
\boxed{
d_{BL}(\mu_\delta,\mu_0)=O(\delta).
}
\tag{8}
\]

This gives a sharp qualitative separation from AF-353 and AF-355: the endpoint is regular in an averaged `B^2` / limiting-distribution topology even though the sharp uniform critical norm

\[
K(\delta)
:=
\sup_{X\ge2}X^{-1/2}
\left|\mathcal R_\delta[\Lambda-1](X)\right|
\tag{9}
\]

cannot stay bounded as `delta -> 0` under RH, and sufficiently fast moving orders inherit endpoint oscillation. Thus the moving-order obstruction is **not a loss of second-mean spectral energy**. It lies in maximal/extremal behavior, tail control, or phase alignment that `B^2` averaging does not see.

## Derivation

### 1. The zero coefficients meet continuously at the endpoint

For fixed `delta>0`, Mellin inversion for the Riesz weight gives the usual zero term

\[
-\sum_\rho b_\delta(\rho)X^\rho.
\tag{10}
\]

After subtracting the unit source and normalizing by `X^{-1/2}`, the pole, trivial-zero, floor, and endpoint correction terms contribute functions whose `B^2` seminorm is zero. Under RH, `X^\rho X^{-1/2}=e^{i\gamma y}` with `X=e^y`, so the surviving nontrivial-zero frequencies are exactly `(6)`.

At `delta=0`,

\[
b_0(\rho)
=B(\rho,1)
=\frac1\rho,
\tag{11}
\]

which is the classical coefficient in the normalized prime-number-theorem remainder. Wintner's endpoint theory gives the corresponding `B^2` almost-periodic representation. Hence the positive-order Riesz coefficients and the unsmoothed endpoint belong to the same `B^2` Fourier family; the issue is the norm in which their difference is summable.

### 2. Parseval reduces endpoint continuity to a square-summable coefficient derivative

For each distinct positive ordinate `gamma`, repeated zeros contribute the grouped coefficient `m_gamma b_delta(rho_gamma)`. Besicovitch Parseval therefore gives `(7)`; no linear-independence hypothesis on zero ordinates is required.

Differentiate `(5)` with respect to `u`:

\[
\frac{\partial}{\partial u}b_u(\rho)
=
b_u(\rho)
\bigl(\psi(1+u)-\psi(\rho+1+u)\bigr),
\tag{12}
\]

where `psi=Gamma'/Gamma`. Uniformly for `0<=u<=1`, standard Gamma-ratio and digamma estimates on the critical line give

\[
|b_u(\rho)|\ll \frac1{|\rho|},
\qquad
|\psi(1+u)-\psi(\rho+1+u)|
\ll \log(2+|\gamma|).
\tag{13}
\]

The mean-value theorem then yields

\[
\left|
b_\delta(\rho)-b_0(\rho)
\right|
\ll
\delta\,
\frac{\log(2+|\gamma|)}{|\rho|}
\qquad (0\le\delta\le1).
\tag{14}
\]

### 3. Zero multiplicities still leave a finite square budget

Because equal ordinates have already been grouped, `(7)` contains `m_gamma^2`. This does not spoil summability. The local Riemann--von Mangoldt bound gives

\[
m_\gamma\ll \log(2+\gamma).
\tag{15}
\]

Therefore

\[
m_\gamma^2
\frac{\log^2(2+\gamma)}{|\rho_\gamma|^2}
\ll
m_\gamma
\frac{\log^3(2+\gamma)}{1+\gamma^2}.
\tag{16}
\]

Summing the right side over distinct ordinates is the same as summing `log^3(2+|gamma|)/(1+gamma^2)` over zeros counted with multiplicity. By the Riemann--von Mangoldt zero-counting estimate, its dyadic shells are

\[
O\!\left(\frac{j^4}{2^j}\right),
\tag{17}
\]

and hence summable. Combining `(7)`, `(14)`, and `(16)` proves `(4)`.

### 4. The limiting laws inherit the same modulus

Wintner's normalized prime-number-theorem remainder is `B^2` almost periodic under RH, and the positive-order Riesz profiles have square-summable zero coefficients. Thus every `E_delta`, `0<=delta<=1`, has a limiting distribution.

For every bounded `1`-Lipschitz test function `F`,

\[
\begin{aligned}
\left|
\int F\,d\mu_\delta-
\int F\,d\mu_0
\right|
&=
\lim_{Y\to\infty}
\left|
\frac1Y\int_0^Y
\bigl(F(E_\delta(y))-F(E_0(y))\bigr)\,dy
\right|\\
&\le
\limsup_{Y\to\infty}
\frac1Y\int_0^Y |E_\delta(y)-E_0(y)|\,dy\\
&\le
\|E_\delta-E_0\|_{B^2}.
\end{aligned}
\tag{18}
\]

Equation `(8)` follows from `(4)`.

## Arithmetic-fidelity interpretation

AF-353 measured an **absolute zero-mode budget** and found a `delta^{-2}` divergence. AF-355 then showed that cancellation-aware pointwise control still becomes singular: even under RH, sufficiently fast `delta(X)->0` cannot preserve the sharp `O(sqrt(X))` target.

The present calculation shows that neither divergence is visible in the natural logarithmic second-mean topology. The same zero coefficients that produce an unbounded maximal conditioning problem vary smoothly in `ell^2`, and the whole limiting law varies continuously with them.

So there are now three distinct currencies at the same endpoint:

1. absolute coefficient budget: strongly singular;
2. logarithmic `B^2` / limiting-distribution geometry: Lipschitz-stable;
3. sharp uniform critical norm: singular.

This rules out a broad class of proposed repairs based only on variance, mean-square convergence, or continuity of the limiting distribution. Such observables can remain perfectly well conditioned while the RH-relevant uniform target has already lost control. Any source resource intended to close AF-355's remaining slow-order regime must therefore control **maximal/extremal coherence beyond second mean**, not merely the aggregate square energy of the zero modes.

## What this changes

The moving-Riesz frontier should no longer ask generically whether the endpoint is "continuous" or whether the zero profile has a stable limiting distribution. Both are too metric-dependent.

The useful next question is narrower: **what source-native quantity controls the passage from the stable `B^2` zero profile to the singular uniform critical norm, uniformly as `delta -> 0`?** Candidates must price phase concentration, rare peaks, maximal functions, high moments, or another tail-sensitive resource. A result that only controls variance or convergence in distribution cannot by itself cross the endpoint barrier exposed by AF-353--AF-355.

## Boundaries

- The theorem is conditional on RH because the normalization `(2)` places all nontrivial-zero frequencies on the real `gamma` axis.
- No linear-independence hypothesis for zero ordinates is used; multiplicities are grouped explicitly.
- `B^2` continuity does not imply pointwise convergence, a bounded `K(delta)`, or any sharp `O(sqrt(X))` estimate.
- Bounded-Lipschitz convergence of limiting distributions does not control rare or increasingly coherent peaks.
- Nothing here proves that any slow schedule left open by AF-355 succeeds. It only removes second-mean/limiting-law instability as the missing obstruction.
- The estimate is about the specific Riesz smoothing family and logarithmic `B^2` target. It is not a generic theorem that averaging is always faithful in mean square.

## Source / prior-art audit

The ingredients are classical or standard:

- Marcel Riesz / Hardy--Riesz theory supplies the Mellin/Beta kernel for the Riesz mean, with nontrivial-zero coefficient `B(rho,1+delta)`.
- Aurel Wintner, *On the asymptotic distribution of the remainder term of the prime-number theorem*, Amer. J. Math. **57** (1935), 534--538, gives the classical limiting-distribution / almost-periodic endpoint framework for the normalized prime-number-theorem error.
- Amir Akbary, Nathan Ng, and Majid Shahabi, *Limiting distributions of the classical error terms of prime number theory*, Quart. J. Math. **65** (2014), 743--780, arXiv:1306.1657, gives a modern `B^2`-almost-periodic framework in which such limiting distributions are systematic.
- Stirling/Gamma-ratio asymptotics, the digamma asymptotic, and the Riemann--von Mangoldt zero-counting formula supply `(13)`--`(17)`.

A targeted literature search for Riesz means of the von Mangoldt function, `B^2` almost periodicity, limiting distributions, and the `delta -> 0` endpoint did not locate this exact Lipschitz comparison or its contrast with the divergent uniform critical norm. That search is not evidence of novelty, so this finding makes **no novelty claim**. The contribution here is the Mathia-specific synthesis: the same Riesz family is well conditioned in `B^2` while AF-353--AF-355 prove that the RH-relevant uniform endpoint is not.