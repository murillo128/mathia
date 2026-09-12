# WI-253 — The first global crossing has an exact sliding-autocorrelation flux constraint

## Status

- **Evidence:** `EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-IMS + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.
- **Scope:** this is a source-side necessary condition for a hypothetical first **unrestricted** localized Weil zero mode under RH failure. It does not prove RH and does not improve the current simple-critical zero proportion. Its role is to replace the centered odd radial observable of `WI-251` by an ordinary autocorrelation after averaging translated interval cutoffs.
- **Novelty boundary:** Suzuki supplies the localized closed Weil operator, the first-crossing framework used in `WI-238`, and the explicit Weil functional. The cutoff/double-commutator algebra is classical. `WI-241`, `WI-245`, and `WI-250` supply the density subtraction, positive resolvent expansion, and source-localization normalization. The new deduction is the unrestricted-first-crossing sliding average and its exact one-parameter autocorrelation inequality. A targeted prior-art search found the established localized Weil/operator framework and generic IMS localization, but no source stating this zeta-specific sliding constraint. No priority claim is made.

## Claim

Assume RH is false. Let

\[
a_*:=\inf\{a>0:\lambda_a\le0\}
\]

be the first **global** crossing of Suzuki's localized Weil ground-state energy, as in `WI-238`, and choose a normalized attained zero mode

\[
\|v\|_2=1,\qquad A_{a_*}v=0,
\qquad \lambda_r>0\quad(0<r<a_*).
\]

Extend `v` by zero to the real line and define its real autocorrelation

\[
C_v(h):=\operatorname{Re}\int_{\mathbb R}v(x+h)\overline{v(x)}\,dx.
\]

Retain the signed finite-radius von Mangoldt discrepancy measure

\[
d\nu_{a_*}(h)
=\sum_{\log n<2a_*}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}(dh)
-e^{h/2}\mathbf 1_{(0,2a_*)}(h)\,dh,
\]

and put

\[
\kappa(h):=
\sum_{m=1}^{\infty}e^{-2(m+1/4)h}
=\frac{e^{-5h/2}}{1-e^{-2h}}
\qquad(h>0).
\]

Then for every `0<r<a_*`,

\[
\boxed{
\begin{aligned}
\mathcal F_v(r)
:=&\int_0^{2a_*}\min(h,2r)C_v(h)\,d\nu_{a_*}(h)\\
&+\int_0^{2a_*}\min(h,2r)\kappa(h)C_v(h)\,dh
\ge r\lambda_r>0.
\end{aligned}
}
\tag{1}
\]

Equivalently,

\[
\boxed{
\begin{aligned}
\mathcal F_v(r)
=&\sum_{\log n<2a_*}\frac{\Lambda(n)}{\sqrt n}
\min(\log n,2r)C_v(\log n)\\
&+\int_0^{2a_*}\min(h,2r)
\left(\frac{e^{-5h/2}}{1-e^{-2h}}-e^{h/2}\right)C_v(h)\,dh
\ge r\lambda_r.
\end{aligned}
}
\tag{2}
\]

The apparent `1/h` singularity of `kappa(h)` is harmless because `min(h,2r)kappa(h)=O(1)` at the origin.

The main structural gain over the odd centered-cutoff route is that (1) depends only on the ordinary autocorrelation. In particular,

\[
\boxed{
C_v(h)=\frac1{2\pi}\int_{\mathbb R}\cos(zh)|\widehat v(z)|^2\,dz,
}
\tag{3}
\]

so the entire sliding family is tested against a nonnegative spectral density. Defining the explicit cosine symbol

\[
\begin{aligned}
\Sigma_r(z):={}&
\sum_{\log n<2a_*}\frac{\Lambda(n)}{\sqrt n}
\min(\log n,2r)\cos(z\log n)\\
&+\int_0^{2a_*}\min(h,2r)
\left(\kappa(h)-e^{h/2}\right)\cos(zh)\,dh,
\end{aligned}
\tag{4}
\]

we have the equivalent necessary condition

\[
\boxed{
\frac1{2\pi}\int_{\mathbb R}\Sigma_r(z)|\widehat v(z)|^2\,dz
\ge r\lambda_r>0
\qquad(0<r<a_*).
}
\tag{5}
\]

Thus RH failure would force one compactly supported zero mode to satisfy a continuum of explicit positive spectral averages, with prime-threshold changes built into `Sigma_r`.

## 1. The density subtraction does not require odd parity

`WI-241` used odd parity to expose the cancellation particularly transparently, but the underlying regrouping extends to an arbitrary compactly supported `v`.

Let

\[
A_v(h):=\int_{\mathbb R}v(x+h)\overline{v(x)}\,dx,
\qquad C_v(h)=\operatorname{Re}A_v(h).
\]

Then `A_v(-h)=overline{A_v(h)}`. Suzuki's general Weil functional contains the exponential term

\[
\int_{\mathbb R}A_v(h)(e^{h/2}+e^{-h/2})\,dh
=2\int_0^\infty(e^{h/2}+e^{-h/2})C_v(h)\,dh,
\tag{6}
\]

while the two prime-power translates contribute

\[
-2\sum_n\frac{\Lambda(n)}{\sqrt n}C_v(\log n).
\tag{7}
\]

Subtract and add the density-one analogue of (7),

\[
-2\int_0^\infty e^{h/2}C_v(h)\,dh.
\tag{8}
\]

The density term (8) combines with (6) to give the positive exponential resolvent

\[
R(v)=2\int_0^\infty e^{-h/2}C_v(h)\,dh
=\frac1{2\pi}\int_{\mathbb R}\frac{|\widehat v(z)|^2}{z^2+1/4}\,dz.
\tag{9}
\]

Therefore the same exact decomposition used in the odd branch holds without parity:

\[
\boxed{
Q_W(v)=Q_{\rm mean}(v)-2\Delta_\Lambda(v),
}
\tag{10}
\]

where `Q_mean=Q_gamma+R` and

\[
\Delta_\Lambda(v)
=\int_0^{2a_*}C_v(h)\,d\nu_{a_*}(h)
\]

for tests supported in `[-a_*,a_*]`. No RH input enters (6)--(10).

Primary normalization: Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (2026), especially the general Weil functional and localized quadratic form in §1 and the quadratic/distributional formulas in §2: https://arxiv.org/abs/2606.09096.

## 2. The unrestricted first crossing permits translated cutoffs

The key difference from `WI-250`--`WI-252` is to use the global first crossing of `WI-238`, not the first odd crossing. An arbitrary translated interval cutoff destroys parity, so it was unavailable to the odd branch. At the unrestricted crossing, however, every test supported in any interval of length `2r` with `r<a_*` may be translated to `(-r,r)` and is controlled by the same positive bottom `lambda_r`.

Since `A_{a_*}v=0`, the representation theorem gives the weak zero-mode equation

\[
q_{a_*}(v,w)=0
\tag{11}
\]

for every admissible form-domain test `w`. For any real smooth bounded Lipschitz multiplier `chi`, the form-domain multiplication argument of `WI-250` applies without using parity. Hence

\[
q_{a_*}(\chi v)
=q_{a_*}(\chi v)-\operatorname{Re}q_{a_*}(v,\chi^2v).
\tag{12}
\]

Using (10) and the positive resolvent expansion from `WI-245`,

\[
M(z)-M(0)
=\sum_{m=1}^\infty\frac1{b_m}
\frac{z^2}{z^2+\alpha_m^2},
\qquad b_m=m+\frac14,
\quad\alpha_m=2b_m,
\tag{13}
\]

we get the arbitrary-cutoff identity

\[
\boxed{
q_{a_*}(\chi v)
=\mathcal E_{\chi,\rm mean}(v)
+\int_0^{2a_*}D_\chi(v;h)\,d\nu_{a_*}(h),
}
\tag{14}
\]

with

\[
D_\chi(v;h)=
\int(\chi(x+h)-\chi(x))^2
\operatorname{Re}(v(x+h)\overline{v(x)})\,dx
\tag{15}
\]

and

\[
\mathcal E_{\chi,\rm mean}(v)
=\frac12\sum_{m=1}^\infty\frac1{b_m}
\iint K_{\alpha_m}(x-y)(\chi(x)-\chi(y))^2
\operatorname{Re}(v(x)\overline{v(y)})\,dx\,dy,
\tag{16}
\]

where `K_alpha(t)=alpha e^{-alpha|t|}/2`. The constant `M(0)||u||_2^2` cancels exactly in the polarization.

## 3. Sliding hard windows have an exact averaged metric

Let

\[
\eta_{c,r}(x)=\mathbf1_{|x-c|<r}.
\]

For fixed `x,y`, the set of centers whose interval contains exactly one of the two points is the symmetric difference of two intervals of centers. Its measure is

\[
\boxed{
\int_{\mathbb R}
(\eta_{c,r}(x)-\eta_{c,r}(y))^2\,dc
=2\min(|x-y|,2r).
}
\tag{17}
\]

Also

\[
\boxed{
\int_{\mathbb R}\|\eta_{c,r}v\|_2^2\,dc
=2r\|v\|_2^2=2r.
}
\tag{18}
\]

For each `h>=0`, (17) yields

\[
\boxed{
\int_{\mathbb R}D_{\eta_{c,r}}(v;h)\,dc
=2\min(h,2r)C_v(h).
}
\tag{19}
\]

Sharp multiplication need not be assumed a priori on the logarithmic form domain. To justify the passage, convolve `1_{[-r,r]}` with a standard nonnegative mollifier of width `epsilon`, translate the resulting smooth profile by `c`, and use support radius `r+epsilon<a_*`. Young's inequality gives the uniform translation bound

\[
\|\tau_h\chi_{r,\epsilon}-\chi_{r,\epsilon}\|_2^2
\le
\|\tau_h\mathbf1_{[-r,r]}-\mathbf1_{[-r,r]}\|_2^2
=2\min(h,2r),
\tag{20}
\]

which is exactly strong enough to dominate the `kappa(h)~1/(2h)` singularity at zero. The source has only finitely many atoms at fixed radius and finite continuous weight. Thus Fubini and dominated convergence pass (14) to the sharp-window average. Continuity of `lambda_a` then lets `epsilon` tend to zero.

This avoids granting `v` unproved `H^1` regularity or endpoint values.

## 4. Averaging the mean IMS term is explicit

Integrate (16) in `c` and apply (17). Since the kernel is even,

\[
\begin{aligned}
\int_{\mathbb R}\mathcal E_{\eta_{c,r},\rm mean}(v)\,dc
&=2\int_0^{2a_*}\min(h,2r)
\left[
\sum_{m=1}^\infty\frac1{b_m}K_{\alpha_m}(h)
\right]C_v(h)\,dh.
\end{aligned}
\tag{21}
\]

But `alpha_m=2b_m` gives

\[
\frac1{b_m}K_{\alpha_m}(h)=e^{-2b_mh},
\]

so the bracket in (21) is exactly `kappa(h)`. Therefore

\[
\boxed{
\int_{\mathbb R}\mathcal E_{\eta_{c,r},\rm mean}(v)\,dc
=2\int_0^{2a_*}\min(h,2r)\kappa(h)C_v(h)\,dh.
}
\tag{22}
\]

Likewise (19) gives

\[
\boxed{
\int_{\mathbb R}\int_0^{2a_*}
D_{\eta_{c,r}}(v;h)\,d\nu_{a_*}(h)\,dc
=2\int_0^{2a_*}\min(h,2r)C_v(h)\,d\nu_{a_*}(h).
}
\tag{23}
\]

Thus the entire center-averaged localization defect is an ordinary-autocorrelation functional. The reflected half-line Hankel term responsible for the `WI-252` Beurling--Deny obstruction never appears.

## 5. Interior positivity forces the sliding family to stay positive

For every smooth translated cutoff of support radius `r+epsilon`, translation invariance of the global Weil form and positivity below the first global crossing imply

\[
q_{a_*}(\chi_{c,r,\epsilon}v)
\ge
\lambda_{r+\epsilon}
\|\chi_{c,r,\epsilon}v\|_2^2.
\tag{24}
\]

Integrating over `c` and passing `epsilon` to zero gives, by (18),

\[
2\mathcal F_v(r)\ge2r\lambda_r.
\tag{25}
\]

This proves (1)--(2). Formula (3) is ordinary Wiener--Khinchin/Parseval, and inserting it into (2) proves (4)--(5).

The current certified compact-window theorem of Xuefeng Zhu gives `lambda_{0.8}>0` for the unrestricted complex test space, so any hypothetical global first crossing also satisfies

\[
a_*>0.8.
\tag{26}
\]

Source: Xuefeng Zhu, **Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau--Widom decay law**, arXiv:2608.24827v2 (2 Sep 2026), which certifies `Q(f)>=8.9e-18||f||_2^2` on support `[-0.8,0.8]`: https://arxiv.org/abs/2608.24827.

## 6. Why this changes the live source-side gate

`WI-251` eliminated the smooth-collar cost for the first odd mode but was forced to use centered radial windows. Its source observable contains `||x+h|-|x||`, and after half-line transfer that geometry is entangled with the reflected Hankel interaction isolated by `WI-252`. Generic positivity-preserving ground-state arguments therefore cannot supply the missing phase sign.

The unrestricted first crossing trades odd-sector specificity for translation freedom. Averaging all centers removes the window location exactly and returns to `C_v(h)`, whose spectral representation (3) has nonnegative density. The remaining problem is therefore sharper and different:

\[
\boxed{
\text{Can one rule out a compactly supported zero mode whose }
|\widehat v|^2
\text{ makes every explicit }\Sigma_r\text{ average positive?}
}
\tag{27}
\]

The parameter `r` is not decorative. As `r` crosses `\tfrac12\log n`, a prime atom changes from the linear branch `2r` to the saturated branch `\log n`; away from these thresholds the derivative of `mathcal F_v(r)` is a tail autocorrelation functional. Hence one candidate must satisfy a coherent continuum of arithmetic inequalities, not a single discrepancy bound.

This does not resolve the earlier odd clue, which remains valid on its own candidate class. It supplies a parallel first-failure representation in which the principal phase obstruction of `WI-252` is absent.

## 7. Stress tests and boundaries

1. **No contradiction follows from firstness alone.** Generic translation-invariant forms with a first crossing can satisfy analogous sliding localization inequalities. The closing input must use the explicit zeta symbol/source in (2) or (4).
2. **No lower rate for `lambda_r` is assumed.** Only strict positivity for each fixed `r<a_*` and Suzuki's continuity are used.
3. **Hard cutoff admissibility is obtained only after averaging/approximation.** The proof does not claim that multiplication by every interval indicator preserves the form domain pointwise.
4. **The `kappa` density is not integrable by itself at zero.** Only the weighted expression `min(h,2r)kappa(h)` occurs, and it is locally bounded. It should not be treated as a finite signed measure without this weight.
5. **The global and odd first crossings need not coincide.** This finding deliberately uses the unrestricted `a_*`; no parity identification is asserted.
6. **Equation (5) is a necessary condition, not a pointwise positivity statement for `Sigma_r`.** The zero mode may concentrate spectral mass where the symbol has mixed sign.
7. **No simple-zero percentage claim is made.** The result belongs to the defect-elimination endgame of the canonical mandate.

## Prior art and provenance

- Masatoshi Suzuki, **Aspects of the screw function corresponding to the Riemann zeta-function**, *Journal of the London Mathematical Society* 107 (2023), DOI `10.1112/jlms.12785`, supplies the localized screw-function/nondegeneracy framework.
- Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (2026), supplies the current self-adjoint localized operator, continuity of the ground-state energy, general Weil functional, and explicit screw-function/source formulas.
- Xuefeng Zhu, **Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau--Widom decay law**, arXiv:2608.24827v2 (2 Sep 2026), supplies the certified unrestricted positivity at radius `0.8` used only for (26).
- The IMS/double-commutator localization identity and Wiener--Khinchin autocorrelation representation are classical background. `WI-250` fixes their normalization in the localized Weil/source decomposition; `WI-251` supplies the related exact layer-cake strategy for centered odd cutoffs.

A targeted external search for localized/sliding Weil quadratic forms, interval cutoff IMS identities, screw-function sliding windows, and first-crossing autocorrelation constraints returned Suzuki's localization framework and generic localization material but no primary source containing (1)--(5). This search absence is recorded only as audit context, not evidence of priority.

## Falsification

The result fails if any of the following occurs: the general-parity regrouping (6)--(10) has the wrong factor or sign; smooth bounded Lipschitz multiplication fails on the localized closed form domain; the weak zero-mode equation cannot be polarized against `chi^2v`; translation changes the global Weil form; the center-average identity (17) has a different factor; the resolvent coefficients in (13) are wrong; the mollified interval family does not admit the dominated limit justified by (20); or the first global crossing does not have `lambda_r>0` for every strict interior radius. Each of these is independently checkable against Suzuki's formula, `WI-238`, and the exact algebra above.