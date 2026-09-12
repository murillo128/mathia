# PL-289 — One-dimensional Weil graph domain forces a squared-log Fourier moment

**Evidence:** `LITERATURE+EXACT-DERIVED + POSITIVE-REFINEMENT + ROUTE-NARROWING`

**Status:** `EXACT-1D-GRAPH-DOMAIN + EIGENSTATE-LOG2-MOMENT + LOG2-TRANSLATION-MODULUS`

## Claim

The state-specific regularity target left open by `PL-287` and `PL-288` can be reached one full logarithmic order beyond the ambient form estimate. On the fixed interval `I=(-1,1)`, the principal closed form in Suzuki's scaled localized Weil operator has Fourier symbol

\[
m(\xi)=\log|\xi|+\gamma,
\]

and its self-adjoint operator `T` has the exact one-dimensional graph domain

\[
\boxed{
D(T)=\left\{u\in L^2(I):m(\xi)\widehat{Eu}(\xi)\in L^2(\mathbb R)\right\},
}
\]

where `Eu` denotes zero extension to `R`. More quantitatively, every `u in D(T)` satisfies

\[
\boxed{
\frac1{2\pi}\int_{\mathbb R}(\log|\xi|+\gamma)^2|\widehat{Eu}(\xi)|^2\,d\xi
\le
\|Tu\|_2^2+\frac{\pi^2}{2}\|u\|_2^2.
}
\]

The mechanism is specific to one dimension. Chen--Weth's integral realization of the logarithmic Laplacian shows that outside `I` the whole-space multiplier applied to a zero-extended function is a pair of Carleman transforms. The classical `L^2` norm `||C||=pi` then controls the exterior exactly; a small negative-Sobolev argument rules out hidden distributions supported at the two endpoints.

Suzuki's fixed-domain canonical Weil operator is a bounded perturbation `A_a=T+K_a` of this principal operator on every source-static aperture interval. Consequently every normalized eigenstate `u_a` obeys a **squared-log Fourier moment** bound

\[
\frac1{2\pi}\int (\log|\xi|+\gamma)^2|\widehat{Eu_a}(\xi)|^2\,d\xi
\le
(|\lambda_a|+\|K_a\|)^2+\frac{\pi^2}{2}.
\]

This converts the qualitative compact-family improvement in `PL-287` into an explicit state-specific modulus. If

\[
F_u(h)=\langle S_hu,u\rangle
=\frac1{2\pi}\int e^{ih\xi}|\widehat{Eu}(\xi)|^2\,d\xi,
\]

then eigenstates on a compact source-static aperture interval satisfy

\[
|F_u(h+\delta)-F_u(h)|
=O\!\left(\frac1{\log^2(1/|\delta|)}\right),
\]

with an explicit constant controlled by the graph norm. This is a strict power-of-log improvement over the ambient `Theta(1/log(1/|delta|))` quadratic modulus of `PL-285` and is stronger than the merely qualitative `o(1/log(1/|delta|))` conclusion of `PL-287`.

It does **not** by itself produce a useful certified transport radius from the `a=0.8` positivity margin: a coefficient of ordinary size multiplying `1/log^2(1/|delta|)` is still far too large at any practical aperture increment compared with the `~8.9e-18` margin. The result removes the ambient regularity barrier but leaves the quantitative constant/source-activation barrier intact.

## 1. Identification with the one-dimensional logarithmic Laplacian

Source 56 (Suzuki) rewrites the scaled localized Weil form on `I=(-1,1)` as a fixed principal closed form plus bounded aperture-dependent terms. With the Fourier convention used there, the principal part is

\[
\mathcal L(u,v)
=
\frac1{2\pi}\int_{\mathbb R}
(\log|\xi|+\gamma)\widehat{Eu}(\xi)\overline{\widehat{Ev}(\xi)}\,d\xi.
\]

Source 96 (Chen--Weth) studies the whole-space logarithmic Laplacian `L_Delta`, whose Fourier symbol is `2 log|xi|`, and gives

\[
L_\Delta f(x)
=
c_N\int_{\mathbb R^N}
\frac{f(x)\mathbf 1_{|x-y|<1}-f(y)}{|x-y|^N}\,dy
+\rho_N f(x),
\]

where

\[
c_N=\pi^{-N/2}\Gamma(N/2),
\qquad
\rho_N=2\log2+\psi(N/2)-\gamma.
\]

For `N=1`, `c_1=1` and `psi(1/2)=-gamma-2 log 2`, so `rho_1=-2 gamma`. Therefore

\[
H:=\frac12L_\Delta+\gamma I
\]

has Fourier multiplier exactly `m(xi)=log|xi|+gamma`, matching Suzuki's principal form.

This identification is only an operator-theoretic bridge. It does not import any RH information from logarithmic-Laplacian theory.

## 2. Exterior Carleman estimate gives the missing graph norm

Let `T` be the self-adjoint operator associated with `mathcal L` on `L^2(I)`. For `u in D(T)`, testing against compactly supported smooth functions inside `I` gives, distributionally,

\[
H(Eu)|_I=Tu.
\]

Outside the support, Chen--Weth's integral formula loses the local term. For `x>1`,

\[
H(Eu)(x)
=-\frac12\int_{-1}^{1}\frac{u(y)}{x-y}\,dy.
\]

Put `t=x-1`, `s=1-y`, and `f(s)=u(1-s)` for `0<s<2`, extended by zero to `(0,infinity)`. Then the right exterior restriction is `-(1/2)Cf`, where

\[
(Cf)(t)=\int_0^\infty\frac{f(s)}{t+s}\,ds
\]

is the classical Carleman operator. Mellin diagonalization gives multiplier `pi/cosh(pi tau)` and hence

\[
\|C\|_{L^2(0,\infty)\to L^2(0,\infty)}=\pi.
\]

Thus

\[
\|1_{(1,\infty)}H(Eu)\|_2
\le\frac\pi2\|u\|_2.
\]

The left endpoint gives the same estimate, so

\[
\boxed{
\|1_{I^c}H(Eu)\|_2^2
\le\frac{\pi^2}{2}\|u\|_2^2.
}
\]

There is one endpoint subtlety: the interior and exterior formulas determine the distribution only away from `{-1,1}`. But `Eu in L^2(R)` and `m(xi)=O_epsilon((1+|xi|)^epsilon)` imply `H(Eu) in H^{-epsilon}(R)` for every `epsilon>0`. Choose `epsilon<1/2`. No nonzero distribution supported at a point (a delta or one of its derivatives) belongs to `H^{-epsilon}` at that regularity. Hence there is no hidden endpoint-supported residual, and `H(Eu)` is precisely the piecewise `L^2` function above.

Plancherel now yields

\[
\begin{aligned}
\frac1{2\pi}\int m(\xi)^2|\widehat{Eu}(\xi)|^2\,d\xi
&=\|H(Eu)\|_2^2\\
&=\|Tu\|_2^2+\|1_{I^c}H(Eu)\|_2^2\\
&\le\|Tu\|_2^2+\frac{\pi^2}{2}\|u\|_2^2.
\end{aligned}
\]

Conversely, if `u in L^2(I)` and `m widehat(Eu) in L^2(R)`, then `H(Eu) in L^2(R)`. Restricting `H(Eu)` to `I` represents `mathcal L(u,v)` against every form-domain vector `v`, so the representation theorem gives `u in D(T)`. This proves the displayed graph-domain characterization.

The apparent logarithmic singularity at `xi=0` causes no extra condition: finite support gives `Eu in L^1 cap L^2`, hence `widehat(Eu)` is bounded, while `log^2|xi|` is locally integrable at zero.

## 3. Bounded perturbation transfers the estimate to Weil eigenstates

On a source-static aperture interval, Source 56 decomposes the fixed-domain scaled canonical operator as

\[
\widetilde A_a=T+K_a,
\]

where `K_a` is bounded self-adjoint: it contains the scalar term, finitely many compressed prime-power translations, and a continuous-kernel remainder. Bounded perturbation preserves the operator domain,

\[
D(\widetilde A_a)=D(T).
\]

If `u_a` is a normalized eigenstate with eigenvalue `lambda_a`, then

\[
Tu_a=(\lambda_a-K_a)u_a,
\qquad
\|Tu_a\|_2\le |\lambda_a|+\|K_a\|.
\]

Consequently

\[
\boxed{
M_2(u_a):=
\frac1{2\pi}\int m(\xi)^2|\widehat{Eu_a}(\xi)|^2\,d\xi
\le
(|\lambda_a|+\|K_a\|)^2+\frac{\pi^2}{2}.
}
\]

For a compact source-static aperture interval, the bounded remainder is uniformly bounded and the relevant isolated eigenbranch is bounded. The corresponding eigenstates therefore have a uniform squared-log moment.

A convenient positive weight is

\[
E_2(u)=\frac1{2\pi}\int
\bigl(1+(\log^+|\xi|)^2\bigr)|\widehat{Eu}(\xi)|^2\,d\xi.
\]

For normalized eigenstates,

\[
E_2(u_a)
\le
2(|\lambda_a|+\|K_a\|)^2+\pi^2+1+2\gamma^2.
\]

No simplicity assumption is needed for this regularity statement; simplicity is needed only when one wants a canonically tracked eigenvector branch.

## 4. The eigenstate translation modulus is `O(log^-2)`

For every normalized `u` with finite `E_2(u)`, Fourier representation gives

\[
|F_u(h+\delta)-F_u(h)|
\le E_2(u)\,\omega_2(\delta),
\]

where

\[
\omega_2(\delta)
:=\sup_{\xi\in\mathbb R}
\frac{|e^{i\delta\xi}-1|}{1+(\log^+|\xi|)^2}.
\]

Let `L=log(1/|delta|)`. Choosing `xi=pi/|delta|` gives

\[
\omega_2(\delta)
\ge
\frac{2}{1+(L+\log\pi)^2}.
\]

For the upper bound split at

\[
|\xi|=|\delta|^{-1}e^{-\sqrt L}.
\]

Below the split, `|e^{i delta xi}-1|<=|delta xi|<=e^{-sqrt L}`. Above it, the numerator is at most `2` and `log^+|xi|>=L-sqrt L`. Hence

\[
\omega_2(\delta)
\le
e^{-\sqrt L}
+\frac{2}{1+(L-\sqrt L)^2}.
\]

Therefore

\[
\boxed{
\omega_2(\delta)
=\frac{2+o(1)}{\log^2(1/|\delta|)}.
}
\]

The canonical eigenstate family thus improves the worst-case form-domain autocorrelation modulus by an entire power of `log`.

## 5. Adversarial audit

**Boundary-supported distributions.** The most dangerous gap in the exterior argument is an unnoticed delta term at `x=+-1`. The negative-Sobolev regularity of the logarithmic multiplier excludes it before Plancherel is invoked.

**Operator domain versus form domain.** The squared-log estimate is *not* an ambient form-domain statement. It uses `u in D(T)`, and the canonical Weil eigen-equation supplies exactly that stronger hypothesis because the arithmetic remainder is bounded.

**One-dimensionality.** The sharp exterior reduction to the Carleman kernel `1/(t+s)` is a one-dimensional mechanism. No higher-dimensional analogue is asserted here.

**Aperture activations.** The bound is cleanest on a compact source-static interval. At a source activation, the operator family acquires a new prime-power translation term and continuity must be handled with the existing activation analysis; this finding does not remove that bookkeeping.

**Quantitative positivity transport.** `O(log^-2)` is asymptotically stronger than `O(log^-1)`, but it remains extremely soft numerically. With a coefficient of order one, matching an `~10^-17` positivity margin requires `log(1/|delta|)` of order `10^8`. Thus this result is a genuine regularity mechanism, not yet a practical positivity-propagation certificate.

**Matched controls.** The graph-domain upgrade comes from finite-interval support plus the universal one-dimensional logarithmic multiplier. It is not rational-prime rigidity and therefore cannot by itself distinguish zeta from a matched nonarithmetic control. The arithmetic content enters only through `K_a` and any later source-specific cancellation or quantitative constant.

## 6. Prior art and novelty audit

Source 96 supplies the logarithmic-Laplacian symbol, singular-integral formula, and bounded-domain Dirichlet framework. Source 56 supplies the localized Weil decomposition and the fixed principal logarithmic form. The Carleman operator and its norm are classical.

The inspected literature did **not** reveal the exact interval statement

\[
D(T)=\{u:m\widehat{Eu}\in L^2\}
\]

with the explicit exterior estimate `pi^2/2`, nor its transfer to Suzuki's canonical Weil eigenstates and the resulting `log^-2` autocorrelation modulus. This is therefore recorded as an exact derived line-local refinement, **not** as a broad novelty claim about the logarithmic Laplacian.

Searches were made by the mathematical structure (`logarithmic Laplacian` + operator/graph domain + interval/Fourier `log^2` + Carleman), not only by the wording used here. No inspected source supplied the same bridge.

## 7. Consequence for the research line

`PL-288` showed that finite-dimensional `L^2` localization cannot beat a square-root transport barrier. `PL-289` now supplies the missing stronger regularity directly from the infinite-dimensional eigen-equation:

\[
\text{Weil eigenstate}
\Longrightarrow
\text{operator graph domain}
\Longrightarrow
(\log|\xi|)^2\text{ moment}
\Longrightarrow
O(\log^{-2})\text{ prime-shift modulus}.
\]

This removes the ambient `H_log` modulus as the immediate obstruction. The next falsifiable question is narrower: whether the **arithmetic bounded remainder** or the finite certificate can give a sufficiently small *state-specific constant* or a cancellation identity in the moving prime-shift channel. Without such additional arithmetic input, the improved logarithmic power remains far too weak to bridge a certified `10^-17` ground-state margin across a nontrivial aperture interval.
