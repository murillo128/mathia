# RE-216 — Off-center binomial synthesis lifts the constructive vertical budget

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + OFF-CENTER-POLYNOMIAL-PREDICTION + ORDINARY-PRIME-REALIZATION + SELECTOR-DEBT-SCALE + LOGARITHMIC-HEIGHT + KV-FIDELITY + INTEGER-MULTIPLICITIES`.

**Parent findings:** RE-204, RE-208, RE-213--RE-215.

`RE-208` realizes every separated continuum synthesis whose reciprocal coefficient variation is `Q^{kappa+o(1)}` with `kappa<1/2`, but its concrete spectral synthesis still inherits the centered expansion of `RE-204`. That expansion writes `z^{-m}` as a power series in `1-z`; at logarithmic height it gives

\[
\log A_Q\le (12\log 2+o(1))HT_Q,
\]

so with `H=log 8` the known ordinary-prime construction reaches only `c<0.0289079...` for `T_Q=c log Q`.

The factor `12 log 2` is not intrinsic even to elementary polynomial prediction. Expanding the same negative power about a point **outside** the unit circle reduces the coefficient `ell^1` growth while retaining a uniform exponentially small error on the observed arc. A completely explicit choice gives

\[
\boxed{
\log A_Q\le (6.081+o(1))HT_Q,
}
\tag{1}
\]

with all repair delays still confined to a fixed corridor `[H,5H+o(1)]`. Feeding this synthesis into the reservoir-centroid realization of `RE-208` yields an ordinary-prime `{0,1,2}` perturbation with KV fidelity whenever

\[
\boxed{
6.081\,Hc<\frac12.
}
\tag{2}
\]

For the current corridor `H=log 8`, this gives

\[
\boxed{
0<c<\frac{1}{2(6.081)\log 8}
=0.0395410\ldots .
}
\tag{3}
\]

Thus the constructive vertical window grows by about `36.8%` over `RE-208`, and the fixed-constant gap to the source-capacity ceiling `1/(2H)` shrinks from the factor `12 log 2=8.3177...` to at most `6.081`. This does **not** close the gap: the point is that a substantial part of the previous loss was representation cost in the predictor, not arithmetic prime-placement cost.

## 1. Shift the expansion center away from one

Put

\[
A:=HT,
\qquad
\alpha:=\frac{13}{25},
\qquad
a:=\frac94,
\qquad
\delta:=\frac{\alpha}{T},
\qquad
m:=\left\lceil\frac{H}{\delta}\right\rceil,
\qquad
z:=e^{-i\delta t}.
\tag{4}
\]

For `|t|<=T`, the relevant unit-circle arc has `|arg z|<=alpha`. Instead of expanding at `z=1`, use

\[
z^{-m}
=a^{-m}\left(1-\frac{a-z}{a}\right)^{-m}
=
\sum_{k=0}^{\infty}
\binom{m+k-1}{k}
a^{-m-k}(a-z)^k.
\tag{5}
\]

The expansion converges uniformly on the whole arc because

\[
r:=\max_{|\theta|\le\alpha}
\frac{|a-e^{-i\theta}|}{a}
=
\frac{\sqrt{a^2+1-2a\cos\alpha}}{a}
=0.65279096\ldots<0.653<1.
\tag{6}
\]

Truncate at

\[
N:=4m.
\tag{7}
\]

For the absolute tail terms, once `k>=4m` the consecutive-term ratio is at most

\[
r\frac{m+k}{k+1}
<0.653\frac54
<0.817.
\tag{8}
\]

Hence the tail is bounded by a fixed multiple of its first term. Stirling's formula at `k=4m+O(1)` gives

\[
\frac1m\log
\left[
 a^{-m}\binom{5m}{4m}r^{4m}
\right]
=
-\log a+5\log5-4\log4+4\log r+o(1).
\tag{9}
\]

Using `r<0.653`, the constant on the right is `<-0.0136`. Therefore for some absolute `eta>0`, uniformly on `|t|<=T`,

\[
\left|
z^{-m}-
\sum_{k=0}^{4m}
\binom{m+k-1}{k}a^{-m-k}(a-z)^k
\right|
\le e^{-\eta m}.
\tag{10}
\]

Multiplying by `z^m` produces a real exponential polynomial supported only at delays

\[
L_j=(m+j)\delta,
\qquad 0\le j\le4m.
\tag{11}
\]

Thus

\[
L_j\ge H,
\qquad
L_{\max}\le5H+O(1/T),
\tag{12}
\]

and the repair remains in a fixed multiplicative corridor. At `t=0` the truncation differs from one by `O(e^{-eta m})`; dividing all coefficients by that value makes `G(0)=1` exactly and changes neither the exponent nor the support.

## 2. The coefficient norm drops from `12 log 2` to `6.081`

Expand each `(a-z)^k` in powers of `z`. For every fixed output degree `j`, all contributions have sign `(-1)^j`. There is therefore no hidden cancellation in the coefficient `ell^1` norm, and before the harmless `G(0)` normalization it is exactly

\[
A_{m}:=
 a^{-m}
\sum_{k=0}^{4m}
\binom{m+k-1}{k}
\left(\frac{a+1}{a}\right)^k.
\tag{13}
\]

The terms increase with `k`, so the final term controls the exponential scale. Since `(a+1)/a=13/9`, Stirling gives

\[
\begin{aligned}
\frac1m\log A_m
&\le
-\log\frac94
+5\log5-4\log4
+4\log\frac{13}{9}
+o(1)\\
&=3.16198102\ldots+o(1).
\end{aligned}
\tag{14}
\]

Meanwhile

\[
m=\frac{HT}{\alpha}+O(1)
=\frac{25}{13}HT+O(1).
\tag{15}
\]

Combining (14)--(15),

\[
\boxed{
\log A_m
\le
(6.08073274\ldots+o(1))HT.
}
\tag{16}
\]

Equation (1) uses the rounded safe constant `6.081`.

This is the entire spectral improvement. No stronger prime theorem, denser carrier set or relaxed multiplicity model is used.

## 3. Reuse the `RE-208` arithmetic realization unchanged

Now set

\[
T_Q=c\log Q,
\qquad
H=\log8,
\qquad
d_Q=\frac1{\sqrt Q\log Q}.
\tag{17}
\]

Equations (10) and (15) give a polynomially decaying continuum error

\[
\epsilon_Q
\le
\exp(-\eta m)
=Q^{-\rho_c+o(1)}
\tag{18}
\]

for some fixed `rho_c>0` depending only on `c`. Equation (16) gives

\[
A_Q\le Q^{\kappa+o(1)},
\qquad
\kappa:=6.081\,Hc.
\tag{19}
\]

The reservoir-centroid construction of `RE-208` depends on the spectral synthesis only through four properties: `O(log Q)` real coefficients, spacing `asymp1/log Q`, a fixed logarithmic support corridor, and total reciprocal coefficient variation `Q^{kappa+o(1)}`. Equations (11)--(19) provide exactly those properties. The same Guth--Maynard short-interval reservoirs, empirical-centroid moment cancellation and subset balancing therefore realize every shell by distinct ordinary primes with edit coefficients in `{-1,+1}` whenever

\[
\kappa<\frac12.
\tag{20}
\]

All error estimates from `RE-208` then remain `o(d_Q)`: integer population rounding contributes `O(log Q/Q)`, exact Euler prime powers cost an additional factor `Q^{-1+o(1)}`, and the empirical-centroid placement errors are absorbed by choosing the fixed moment order after the strict margin in (20).

The total absolute Chebyshev edit mass is

\[
Q^{1/2+\kappa+o(1)},
\tag{21}
\]

so (20) also leaves a fixed power margin below every fixed KV envelope `xe^{-bV(x)}`. Before the first repair cloud, which remains beyond the same gap `H=log8`, the local packet still has `D_{Q,local}(1)=Theta(d_Q)`. Thus the selector-scale transient and the ordinary-prime `{0,1,2}` fidelity statements of `RE-208` are unchanged.

## 4. Representation audit and prior-art boundary

The off-center Taylor/binomial expansion is generic approximation theory, not a prime-specific idea. Broad prior-art search also finds classical band-limited prediction by difference/Newton formulas and more recent limited-memory predictors built from polynomial approximations of periodic exponentials. No novelty is claimed for polynomial prediction itself, and no external theorem from that literature is load-bearing here: equations (5)--(16) are self-contained.

The line-specific contribution is quantitative. The exact coefficient norm of this explicit predictor is inserted into the ordinary-prime reservoir-centroid realization, where its exponent directly controls whether bounded multiplicity and KV fidelity can coexist with continuum hiding. That coupling lifts the realized logarithmic-height constant from `0.0289079...` to `0.0395410...` without changing the arithmetic source class.

No `SOURCES.md` update is required because the only load-bearing external arithmetic input remains the short-interval PNT already anchored for `RE-208`.

## 5. Adversarial checks and remaining gap

The shifted center does not introduce negative-delay atoms: `(a-z)^k` is a polynomial in nonnegative powers of `z`, and multiplication by `z^m` moves every atom to `[H,5H+o(1)]`. The coefficients are real, and the alternating output signs are compatible with deletion/duplication. The uniform tail estimate uses the maximum of `|a-z|/a` over the **entire** observed arc, not only a local expansion at `t=0`. The DC normalization is `1+o(1)` and cannot change the coefficient exponent.

The improvement also survives prime quantization because `RE-208` never uses the special centered-binomial coefficient formula; it uses only the aggregate variation exponent and fixed-corridor geometry. Conversely, this finding does not claim that `6.0807...` is optimal among off-center choices, polynomial predictors, or general separated repair measures. Numerical optimization of the same two-parameter representation suggests only modest further improvement inside this exact family, but that is not used as a theorem here.

Most importantly, `RE-213`--`RE-215` still force unit exponential signed-prefix cost on the converse side. The new construction therefore reduces, but does not qualitatively resolve, the gap between an explicit predictor with coefficient-rate at most `6.081` and the source-capacity rate `1`. The next high-value constructive step is no longer to tune the old centered binomial constants; it is to seek a genuinely lower-Wiener-norm causal predictor or a source realization whose signed-prefix cost is substantially smaller than its absolute coefficient variation.

## Research consequence

The `12 log 2` tariff in `RE-208` was partly a coordinate choice. A simple off-center analytic expansion removes more than a quarter of that exponent and increases the rigorously realizable logarithmic-height continuum by about `36.8%` with no new arithmetic hypothesis.

For `H=log8`, separated ordinary-prime `{0,1,2}` continuum hiding with fixed KV fidelity is now explicit for every fixed `c<0.0395410...`, while bounded prime capacity still forbids every fixed `c>0.240449...`. The remaining factor is at most `6.081`, and closing it requires a different predictor norm or a different source architecture rather than another short-interval prime improvement.