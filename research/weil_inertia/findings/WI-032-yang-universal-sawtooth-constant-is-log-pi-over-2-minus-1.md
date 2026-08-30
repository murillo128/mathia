# WI-032 — Yang--Yang's universal sawtooth constant is exactly `log(pi/2)-1`

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + PRIOR-ART-REDIRECTION + NEEDS-AUDIT`. This finding does **not** promote the Yang--Yang one-sided fourth-moment theorem to established evidence and does not change Mathia's current unconditional simple-critical proportion. It closes a narrower analytic subproblem left explicit in the public Yang--Yang reproduction package: for the universal `(1,1)` parity-mean sawtooth object used in their continuum quadrature,

\[
\boxed{
 c^*=\log\frac{\pi}{2}-1
 =-0.548417294710545\ldots
}
\]

and therefore their remaining mean-oscillation constant is also explicit:

\[
\boxed{
\overline{\mathrm{osc}}
=\gamma-1+\log 2
=0.270362845461478\ldots .
}
\]

The result is exact for the universal deterministic object. The still-load-bearing zeta-side reduction to that object, the structured-shift/MRT transfer, and the global remainder ledger remain separate audit obligations.

## 1. Source and evidence boundary

The calculation audits the public repository

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`,

especially:

- `paper.tex`, Lemma `CL` and Appendix N2, where the authors state that the continuum ensemble collapses to a universal `(1,1)` class, prove the slope to be `1`, identify the partial-sum constant `c0=gamma-2`, but leave the mean oscillation inside `c*` computed rather than certified;
- `certification/n2_c0_certification.py`, which gives the exact `(1,1)` free coefficients and the parity-mean shift;
- `scripts/m1_suite.py`, where `g0_sawtooth` is the exact infinite-row sawtooth;
- `scripts/quadrature_cert.py`, where the deep-zone law is written as `y(theta)=log(1/theta)+c*` and `c*` is numerically pinned.

Pinned source URLs:

- https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/paper.tex
- https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/certification/n2_c0_certification.py
- https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/scripts/m1_suite.py
- https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/scripts/quadrature_cert.py

The paper records

\[
c^*=\log\pi+\gamma-2-\overline{\mathrm{osc}}
\]

and a finite numerical ladder near `c*=-0.5433`, with `oscbar approximately 0.2652`. It explicitly grades this part of N2 as computed. The exact calculation below replaces that computed constant **only after entering the same universal `(1,1)` model**.

## 2. Exact Dirichlet series of the universal coefficients

Let

\[
a_d=d\,\gamma_d.
\]

Before the parity-mean convention shift, the source gives

\[
\gamma_{2m}^{\rm raw}
=C_2\prod_{p\mid m}\frac{1}{p(p-2)}
\]

for odd squarefree `m`, and zero otherwise. Hence

\[
a_{2m}^{\rm raw}
=2C_2\prod_{p\mid m}\frac1{p-2}.
\]

For `Re s>0`, absolute convergence gives

\[
\begin{aligned}
A_{\rm raw}(s)
&:=\sum_{d\ge1}a_d^{\rm raw}d^{-s}\\
&=2^{1-s}C_2
  \prod_{p>2}\left(1+\frac{p^{-s}}{p-2}\right)\\
&=\zeta(1+s)E(s),
\end{aligned}
\tag{1}
\]

where

\[
E(s)=2^{1-s}C_2(1-2^{-1-s})
\prod_{p>2}
(1-p^{-1-s})
\left(1+\frac{p^{-s}}{p-2}\right).
\tag{2}
\]

The odd-prime local correction in (2) is

\[
1+O(p^{-2-\Re s})+O(p^{-2-2\Re s}),
\]

so `E` is analytic at least for `Re s>-1/2`.

At `s=0`, the twin-prime product cancels exactly and gives

\[
E(0)=1.
\tag{3}
\]

More importantly, the logarithmic derivative vanishes **prime by prime**. The two `p=2` factors contribute `-log 2` and `+log 2`. For every odd prime,

\[
\left.\frac d{ds}\log(1-p^{-1-s})\right|_{s=0}
=\frac{\log p}{p-1},
\]

while

\[
\left.\frac d{ds}
\log\left(1+\frac{p^{-s}}{p-2}\right)
\right|_{s=0}
=-\frac{\log p}{p-1}.
\]

Therefore

\[
\boxed{E'(0)=0.}
\tag{4}
\]

Using

\[
\zeta(1+s)=\frac1s+\gamma+O(s),
\]

we recover

\[
A_{\rm raw}(s)=\frac1s+\gamma+O(s).
\tag{5}
\]

The source's parity-mean convention changes only `gamma_2` by `-1`, so it subtracts `2\,2^{-s}` from (5). Thus

\[
\boxed{
A(s)=\sum_{d\ge1}a_dd^{-s}
=\frac1s+(\gamma-2)+O(s).
}
\tag{6}
\]

Equation (6) independently recovers Yang--Yang's exact `c0=gamma-2` and fixes the normalization used below.

## 3. Mellin transform of the source sawtooth kernel

The source defines

\[
G_0(x)
=2\sum_{h\ge1}
\frac{\sin(2hx)-\sin(hx)}h,
\tag{7}
\]

with the equivalent periodic sawtooth implementation in `m1_suite.py`. Put

\[
K(x):=-\frac{G_0(x)}x.
\tag{8}
\]

On `0<x<pi`, the exact sawtooth formula gives `G0(x)=-x`, hence `K(x)=1`; at infinity `G0` is bounded, so `K(x)=O(1/x)`. Its Mellin transform therefore has fundamental strip

\[
0<\Re s<1.
\]

Applying the classical sine Mellin transform to the Abel-regularized Fourier series in (7), then taking the Abel limit (equivalently, starting from the piecewise-periodic sawtooth and analytically continuing), gives

\[
\boxed{
\mathcal M K(s)
=-2\Gamma(s-1)
\sin\frac{\pi(s-1)}2
\bigl(2^{1-s}-1\bigr)\zeta(s).
}
\tag{9}
\]

This identity is independently checkable by integrating the two linear pieces of `G0` on each period. Expanding (9) at zero and using the classical value

\[
\zeta'(0)=-\frac12\log(2\pi)
\]

gives

\[
\boxed{
\mathcal M K(s)
=\frac1s+
\left(1-\gamma+\log\frac\pi2\right)
+O(s).
}
\tag{10}
\]

No numerical fit enters (9)--(10).

## 4. The double pole gives `c*` exactly

The universal source quantity is

\[
y(\theta)
=-\frac{\mathcal G(\theta)}{\theta}
=\sum_{d\ge1}a_dK(d\theta).
\tag{11}
\]

For a vertical line in the common fundamental half-plane, Mellin inversion gives

\[
y(\theta)
=\frac{1}{2\pi i}
\int
\mathcal M K(s)A(s)\theta^{-s}\,ds.
\tag{12}
\]

The factorization (1)--(2) continues `A(s)` meromorphically through a strip to the left of zero; for any fixed `0<delta<1/2`, the only pole crossed when shifting (12) from `Re s>0` to `Re s=-delta` is `s=0`. The gamma factor in (9) supplies exponential vertical decay, while the remaining zeta/Euler factors have standard polynomial growth in fixed strips, so the shifted integral is `O_delta(theta^delta)`.

From (6) and (10), the integrand has the double-pole expansion

\[
\left(\frac1s+k_0+O(s)\right)
\left(\frac1s+c_0+O(s)\right)
\theta^{-s},
\]

with

\[
k_0=1-\gamma+\log\frac\pi2,
\qquad
c_0=\gamma-2.
\]

The residue is therefore

\[
\log\frac1\theta+c_0+k_0.
\]

Hence

\[
\boxed{
y(\theta)
=\log\frac1\theta
+\log\frac\pi2-1
+O_\delta(\theta^\delta),
\qquad 0<\delta<\frac12.
}
\tag{13}
\]

In the notation of the public quadrature,

\[
\boxed{
c^*=\log\frac\pi2-1.}
\tag{14}
\]

The cancellation of Euler's constant is structural: `+gamma` enters through the coefficient Dirichlet series, while `-gamma` enters through the Mellin transform of the sawtooth kernel.

## 5. Exact mean oscillation

Yang--Yang's source relation is

\[
c^*=\log\pi+\gamma-2-\overline{\mathrm{osc}}.
\]

Combining it with (14) gives

\[
\boxed{
\overline{\mathrm{osc}}
=\gamma-1+\log2.
}
\tag{15}
\]

Numerically,

\[
c^*=-0.548417294710545\ldots,
\qquad
\overline{\mathrm{osc}}
=0.270362845461478\ldots .
\]

Thus the object that the source described as the remaining computed piece of N2 has an exact closed form in the universal model.

## 6. Independent numerical falsifier

As a non-evidentiary implementation check, summing the source's exact parity-mean coefficients through `d=4,000,000` and evaluating (11) gives the following values of

\[
y(\theta)-\log(1/\theta):
\]

| `theta` | truncated replay |
|---:|---:|
| `1e-3` | `-0.53632...` |
| `3e-4` | `-0.54508...` |
| `1e-4` | `-0.548786...` |
| `3e-5` | `-0.548485...` |

against the exact target `-0.548417294710545...`. The convergence direction changes with the sawtooth oscillation, as expected; this table is only a normalization/sign falsifier and is not used in the proof.

## 7. Consequence for WI-028/WI-030

WI-030 already showed that the finite-offset `c*` term is lower order in the normalized universal continuum core and evaluated that core exactly as

\[
C_{\rm core}=-\frac1{48}.
\]

The present result strengthens the diagnosis: even the universal finite-offset constant itself does not require Richardson extrapolation or an empirical mean-oscillation band. The open part of the Yang--Yang continuum step is therefore **not** the constant `c*`; it is the analytic bridge proving that the actual deterministic arithmetic core collapses to this universal `(1,1)` object with a valid error in the fourth-moment normalization.

Likewise, WI-031 already replaced the heuristic infinite gamma-shell extrapolation by a rigorous Rankin--Euler bound. The remaining one-sided program is increasingly localized to:

\[
\boxed{
\text{zeta/shifted-correlation reduction}
\;\longrightarrow\;
\text{universal-collapse proof}
\; + \;
\text{finite outward-rounded remainder replay}.
}
\]

This finding alone does **not** provide a new unconditional simple-critical proportion.

## 8. Prior-art and novelty audit

The ingredients used here are classical: Euler products and Dirichlet series, Mellin inversion, the sine Mellin transform, the Laurent expansion of `zeta` at `1`, and `zeta'(0)=-(1/2)log(2pi)`. The source's gamma coefficients, parity-mean convention, sawtooth kernel, and `c*` relation belong to Yang--Yang's public work.

Targeted searches of the pinned repository and public web sources found no occurrence of the closed forms `c*=log(pi/2)-1` or `oscbar=gamma-1+log 2`, and no Mellin evaluation closing their N2 mean-oscillation item. This absence is **not** a priority claim. The Mathia contribution recorded here is the exact combination of the source coefficient Dirichlet series with the source sawtooth Mellin transform and the resulting residue calculation.

The appropriate classification is therefore `EXACT-DERIVED` for equations (1)--(15), `CLASSICAL-IDENTITY` for the transform/Euler-product tools, and `LITERATURE+DERIVED + NEEDS-AUDIT` for any use of the constant inside the external zeta proof chain.

## 9. Decisive audit tests

The exact claim should be rejected or corrected if any of the following fails:

1. reconstruct the source `(1,1)` coefficients and verify the local Euler product (1);
2. verify `E(0)=1` and the prime-by-prime cancellation `E'(0)=0`;
3. verify the parity-mean change is exactly `gamma_2 -> gamma_2-1`, hence `A -> A-2*2^{-s}`;
4. derive (9) independently from the piecewise-periodic source sawtooth or an Abel-regularized Fourier series;
5. expand (9) at zero and recover `1-gamma+log(pi/2)`;
6. shift the Mellin contour through `s=0` in a strip narrower than `Re s>-1/2` and recover (13);
7. numerically replay the exact coefficients at decreasing `theta` and observe convergence toward (14), without using that replay as proof.

The zeta-side conclusion must remain `NEEDS-AUDIT` unless the separate universal-collapse and shifted-correlation/remainder bridges are proved at the exact strength consumed.