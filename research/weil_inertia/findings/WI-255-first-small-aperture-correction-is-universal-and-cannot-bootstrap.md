# WI-255 — The first small-aperture correction is universal and cannot bootstrap firstness

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED`.

`WI-254` leaves a source-sensitive subleading small-aperture expansion of the sliding profile as one possible way to strengthen the first-crossing inequality. The first non-leading term can in fact be computed rigorously for the actual first global zero mode. Before imposing the zero-mode equation it contains the prime autocorrelations and the regular archimedean remainder, but **all of those terms cancel exactly once `Q_W(v)=0` is used**.

If RH is false, let `a_*` and the normalized first global zero mode `v` be as in `WI-253`--`WI-254`:

\[
\|v\|_2=1,\qquad A_{a_*}v=0,
\qquad C(h)=\operatorname{Re}\int_{\mathbb R}v(x+h)\overline{v(x)}\,dx.
\]

Then, as `r -> 0+`,

\[
\boxed{
\mathcal F_v(r)
=r\log(1/r)
+r\bigl(\psi(2)-\log(4\pi)\bigr)
+o(r).
}
\tag{1}
\]

The coefficient is independent of `v`, `a_*`, the prime-power autocorrelations, and the location or depth of the hypothetical RH failure. Combining (1) with Suzuki's small-window ground-state asymptotic gives

\[
\boxed{
\mathcal F_v(r)-r\lambda_r
=igl(1-\log2-\mu_1\bigr)r+o(r),
}
\tag{2}
\]

where `mu_1` is the lowest Rayleigh value of Suzuki's limiting logarithmic form `\overline{\mathcal L}` on `(-1,1)`. Firstness therefore yields only

\[
\mu_1\le1-\log2.
\tag{3}
\]

But (3) is already the elementary variational upper bound obtained by inserting the normalized constant function into `\overline{\mathcal L}`. Thus the complete `O(r)` refinement of `WI-254` contains **no new arithmetic constraint at all**. Any small-aperture bootstrap must go beyond the first subleading order, or introduce information not already collapsed by the null equation.

## 1. `H^log` regularity makes the logarithmic autocorrelation defect finite

Suzuki proves that the form domain of every localized Weil operator is contained in the logarithmic Sobolev-type space `H^log`; in his normalization the closed limiting form has Fourier representation

\[
\mathcal L(u)
=\frac1{2\pi}\int_{\mathbb R}(\log|z|+C_0)|\widehat u(z)|^2\,dz,
\]

and the associated form norm is equivalent to the `1+log^+|z|` Fourier weight. Since the first-crossing eigenvector belongs to the localized form domain, the zero extension of `v` has finite logarithmic translation energy.

For `h>0` put

\[
D(h):=\|\tau_hv-v\|_2^2=2(1-C(h)).
\tag{4}
\]

The physical-space logarithmic form on `(-a_*,a_*)` is

\[
\mathcal L_{a_*}(v)
=\frac14\iint_{(-a_*,a_*)^2}
\frac{|v(x)-v(y)|^2}{|x-y|}\,dx\,dy
-\frac12\int_{-a_*}^{a_*}
\log(a_*^2-x^2)|v(x)|^2\,dx.
\tag{5}
\]

For a smooth form-core vector, splitting the translation difference into the interior overlap and the two zero-extension boundary pieces gives

\[
\int_0^{2a_*}\frac{D(h)}h\,dh
=rac12\iint_{(-a_*,a_*)^2}
\frac{|v(x)-v(y)|^2}{|x-y|}\,dx\,dy
+\int_{-a_*}^{a_*}
\log\!\frac{4a_*^2}{a_*^2-x^2}|v(x)|^2\,dx.
\tag{6}
\]

Using `||v||_2=1`, (5)--(6) give the exact identity

\[
\boxed{
\int_0^{2a_*}\frac{C(h)-1}{h}\,dh
=-\mathcal L_{a_*}(v)-\log(2a_*).
}
\tag{7}
\]

The identity extends from the smooth core to the closed form domain by form-norm approximation; all singular terms in (6) are exactly those controlled by the closed logarithmic form. In particular, the integral in (7) is finite. This is the extra regularity needed to improve `WI-254` from `o(r log(1/r))` to a genuine first-order expansion.

As a normalization check, for the normalized constant on `(-a,a)`, `C(h)=1-h/(2a)` on `[0,2a]`, so the left side of (7) is `-1`; (5) gives `\mathcal L_a=1-\log(2a)`, and the right side is also `-1`.

## 2. The aperture profile has an explicit first-order coefficient

Retain the `WI-254` notation

\[
\kappa(h)=\frac{e^{-5h/2}}{1-e^{-2h}},
\qquad
w(h)=\kappa(h)-e^{h/2}.
\]

Near zero,

\[
\kappa(h)=\frac1{2h}-\frac34+O(h),
\qquad
w(h)=\frac1{2h}-\frac74+O(h).
\]

Define the regular remainder

\[
q(h):=w(h)-\frac1{2h}.
\tag{8}
\]

It is continuous at zero and integrable on every fixed finite interval. For `r<(log 2)/2`, every prime-power atom lies on the linear branch of `min(log n,2r)`. Put

\[
P_v:=\sum_{\log n<2a_*}
\frac{\Lambda(n)}{\sqrt n}C(\log n).
\]

The exact `WI-253` profile becomes

\[
\begin{aligned}
\mathcal F_v(r)
={}&2rP_v
+\int_0^{2r}h\,w(h)C(h)\,dh
+2r\int_{2r}^{2a_*}w(h)C(h)\,dh.
\end{aligned}
\tag{9}
\]

Split `w=1/(2h)+q`. Continuity gives

\[
\frac12\int_0^{2r}C(h)\,dh=r+o(r),
\]

while (7) gives

\[
r\int_{2r}^{2a_*}\frac{C(h)}h\,dh
=r\log(1/r)
+r\left(\log a_*-\mathcal L_{a_*}(v)-\log(2a_*)\right)
+o(r).
\]

The regular part contributes

\[
2r\int_0^{2a_*}q(h)C(h)\,dh+o(r).
\]

Hence

\[
\boxed{
\mathcal F_v(r)
=r\log(1/r)+rB_v+o(r),
}
\tag{10}
\]

with

\[
\boxed{
B_v
=1-\log2-\mathcal L_{a_*}(v)
+2P_v
+2\int_0^{2a_*}q(h)C(h)\,dh.
}
\tag{11}
\]

At this stage the coefficient looks source-sensitive: it retains both the finite von Mangoldt sample and the regular archimedean autocorrelation integral.

## 3. The zero-mode equation cancels the entire source-sensitive coefficient

The apparent information in (11) is exactly the information already used by the null equation. Suzuki's decomposition of the screw function writes, away from the prime hinges,

\[
g''(h)=\frac1{2h}+r''(h).
\]

His explicit remainder decomposition gives

\[
r_0''(h)=-(e^{h/2}+e^{-h/2}),
\qquad
r_1''(h)=\frac{e^{-h/2}}{1-e^{-2h}}-\frac1{2h}.
\]

Therefore

\[
\begin{aligned}
r''(h)
&=\frac{e^{-h/2}}{1-e^{-2h}}
-e^{h/2}-e^{-h/2}-\frac1{2h}\\
&=\frac{e^{-5h/2}}{1-e^{-2h}}-e^{h/2}-\frac1{2h}\\
&=q(h).
\end{aligned}
\tag{12}
\]

The same identity follows directly by differentiating Suzuki's exact Lerch expression for `g`, so it is not restricted by the local power-series radius used in one presentation of `r_1`.

For a normalized form-domain vector the closed extension of Suzuki/Bombieri's Lagrangian formula is

\[
Q_W(v)
=\mathcal L_{a_*}(v)-(2A+1)-2P_v
-2\int_0^{2a_*}r''(h)C(h)\,dh,
\tag{13}
\]

where

\[
2A=\log(2\pi)-\psi(2).
\tag{14}
\]

At the first crossing `Q_W(v)=0`. Combining (12)--(14),

\[
\mathcal L_{a_*}(v)
=2A+1+2P_v+2\int_0^{2a_*}q(h)C(h)\,dh.
\tag{15}
\]

Substitution into (11) cancels `P_v`, the whole regular archimedean integral, the dependence on `a_*`, and the mode itself:

\[
\boxed{
B_v=-\log2-2A
=\psi(2)-\log(4\pi).
}
\tag{16}
\]

Equations (10) and (16) prove (1). Numerically the coefficient is

\[
\psi(2)-\log(4\pi)
=-2.1082399118708236535\ldots.
\]

The cancellation is the substantive negative result: the first correction initially appears to expose exactly the prime autocorrelations sought by the sliding-symbol clue, but the zero-mode equation removes them identically.

## 4. Firstness at this order is exactly an old variational trial bound

Suzuki's Theorem 1.4 gives

\[
\lambda_r
=\log(1/r)+\mu_1-\log(2\pi)+\psi(2)-1+O(r),
\tag{17}
\]

where `mu_1>0` is the lowest Rayleigh value of the closed limiting form `\overline{\mathcal L}` on `(-1,1)`. Multiplying by `r` and subtracting from (1) yields (2):

\[
\mathcal F_v(r)-r\lambda_r
=\left(1-\log2-\mu_1\right)r+o(r).
\tag{18}
\]

Thus the first-crossing inequality `\mathcal F_v(r)>=r\lambda_r` implies only (3).

That inequality is already built into the definition of `mu_1`. For the normalized constant

\[
u_0(x)=\frac1{\sqrt2},\qquad -1<x<1,
\]

the jump term in Suzuki's limiting form vanishes and

\[
\begin{aligned}
\mathcal L(u_0)
&=-\frac14\int_{-1}^1\log(1-x^2)\,dx\\
&=1-\log2.
\end{aligned}
\tag{19}
\]

Approximating `u_0` by the form core if desired gives immediately

\[
\mu_1\le1-\log2=0.3068528194400546905\ldots.
\]

So the `O(r)` comparison supplies no new condition on a hypothetical first-crossing mode. It is a repackaging of an elementary trial-vector upper bound in the universal small-window model.

## 5. What this closes, and what it does not

This closes the most immediate subleading route left open by `WI-254`:

\[
\text{compute the first }O(r)\text{ correction}
\;\not\Rightarrow\;
\text{new prime-sensitive rigidity}.
\]

The obstruction is stronger than mere leading-order saturation. The full first correction exists, but on an actual null mode the arithmetic contribution is algebraically redundant with `Q_W(v)=0`.

It does **not** show that all small-aperture information is redundant. A finer term could in principle survive if enough regularity is available to define it, and medium-radius curvature or prime-threshold coupling remains untouched. Nor does this affect the quantitative simple-critical-zero proportion. The result is instead a no-go statement for one specific bootstrap mechanism in the source-side first-crossing program.

The next useful tests are therefore:

1. a genuinely higher-order small-`r` invariant that is not determined by the single null equation, if the first-crossing mode has enough regularity to justify such an expansion; or
2. medium-radius / multi-threshold relations, where the prime hinges are not collapsed into the single scalar `P_v`; or
3. an additional equation obtained from the zero-mode operator relation rather than its scalar quadratic-form value alone.

## 6. Stress tests and evidence boundary

- **No differentiation of an inequality.** The argument never differentiates `\mathcal F_v(r)>=r\lambda_r`; it expands the exact profile and the independently established asymptotic for `lambda_r`, then compares coefficients.
- **No unproved `H^1` regularity.** The logarithmic autocorrelation integral is justified by Suzuki's closed `H^log` form domain. The smooth identities are passed through a form core.
- **No RH input.** The construction is conditional only in the standard contradiction sense: assume RH fails so that the first global crossing exists. Suzuki's operator/form identities and small-window asymptotic are unconditional.
- **No hidden prime truncation.** For fixed `a_*` the prime sum is finite. The restriction `r<(log2)/2` only ensures that every existing prime atom is on the linear aperture branch; it does not discard any atom in range.
- **No claim about a second-order coefficient.** `H^log` regularity is exactly enough for the first correction derived here; stronger expansions would require a separate regularity audit.

## 7. Prior art and novelty audit

Primary source: Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (17 Aug 2026), especially equations (2.3)--(2.7), the `r_0+r_1` decomposition and formula for `r_1''`, the closed `H^log` form-domain analysis in §4, and Theorem 1.4 / §5: https://arxiv.org/abs/2606.09096.

Classical antecedents: Enrico Bombieri, **Remarks on Weil's quadratic functional in the theory of prime numbers. I** (2001), and **A variational approach to the explicit formula** (2003), supply the variational/Lagrangian explicit-formula background that Suzuki reformulates. The translation identity `1-C(h)=||tau_h v-v||_2^2/2` and the logarithmic Gagliardo bookkeeping are standard harmonic-analysis identities; no novelty is claimed for them.

A targeted search for localized Weil first crossings combined with sliding-window `min(h,2r)` profiles, subleading aperture asymptotics, and prime-threshold autocorrelation did not locate a primary source stating (1), (16), or the resulting no-go (18)--(19). Search absence is audit context only, not a priority claim. `WI-253` and `WI-254` are the persisted Mathia inputs that make this particular question meaningful.

## Consequence for the research line

The accepted sliding-autocorrelation clue remains live, but its small-radius branch is narrower. `WI-254` already showed that the leading `r log(1/r)` scale is saturated. The present finding shows that the **entire first subleading `O(r)` term is universal on a null mode and firstness merely recovers the constant-function variational bound for `mu_1`**. The next attempt should therefore not spend effort estimating the first correction more sharply; it must seek information beyond one scalar null identity, most naturally at medium radii, across prime thresholds, or from the full zero-mode equation.