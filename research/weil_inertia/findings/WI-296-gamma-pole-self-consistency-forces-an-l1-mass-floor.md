# WI-296 — gamma-pole self-consistency forces an L1 mass floor under complete screening

## Status

- **Evidence:** `EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-BATHTUB + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.
- **Scope:** the **one-signed, completely screened** first-crossing branch of `WI-281`, `WI-284`, and `WI-294`--`WI-295`. The result keeps the actual `L^1` norm in the exact digamma bathtub instead of replacing it immediately by support measure, then feeds the resulting gamma estimate back through Suzuki's positive pole factorization.
- **Result:** if `v>=0` is a normalized first-crossing null mode and every active prime-power autocorrelation is screened, put
  \[
  M:=\|v\|_1=\int v,
  \qquad s:=M^2.
  \]
  With the exact bathtub profile `\mathcal H` of `WI-295`, the same null vector necessarily satisfies
  \[
  \boxed{\mathcal H(s)+2s<0.}
  \]
  Thus its global `L^1` mass cannot be made arbitrarily small. If
  \[
  \sigma_*:=\inf\{s>0:\mathcal H(s)+2s<0\},
  \]
  with `\inf\varnothing:=+\infty`, then any hypothetical candidate forces
  \[
  \boxed{
  \|v\|_1^2=s>\sigma_*>\mu_*,
  \qquad
  |\{v>0\}|>\sigma_*,
  \qquad
  P_a(v)>2\sigma_*.
  }
  \]
  Here `\mu_*` is the support-only threshold of `WI-295`. A non-load-bearing high-precision evaluation gives
  \[
  \sigma_*\approx0.32498422818840999,
  \qquad
  \sqrt{\sigma_*}\approx0.57007387958790920,
  \]
  so the strengthened support floor is numerically about `46.8853%` of the `log 2` selector budget. The theorem uses only the exact definition of `\sigma_*`, not these decimals.
- **What it does not claim:** this does not rule out complete screening. It supplies a **global** `L^1` floor, not a lower bound for the `L^1` mass of every remote support component. A normalized mode may still place most of its amplitude in a bounded core while retaining very small positive satellites at large distance. The remaining many-component problem is therefore spatial distribution of the forced `L^1` mass, not existence of global `L^1` mass.
- **Novelty boundary:** the exact gamma bathtub and support threshold are `WI-295`; the power-of-two selector bound is `WI-281`; Suzuki supplies the gamma-plus-pole decomposition. The pointwise Fourier `L^1 -> L^infinity` bound, Cauchy--Schwarz, and the bathtub principle are classical. The line-local deduction is to retain `\|v\|_1` as the bathtub cap and close the resulting inequality against the positive pole term on the **same** null vector. Targeted searches around Suzuki's localized Weil form, the digamma multiplier, nonnegative support-restricted vectors, Fourier `L^1` caps, and uncertainty/bathtub bounds did not locate this self-consistency inequality. Search absence is audit context only, not a priority claim.

## Claim

Let `a>0` be a Suzuki first crossing and let

\[
0\ne v\ge0,
\qquad
\|v\|_2=1,
\qquad
A_av=0,
\qquad
q_a(v)=0,
\tag{1}
\]

be a real null mode, extended by zero outside `(-a,a)`. Assume complete screening of every active prime-power autocorrelation. Put

\[
E:=\{x\in(-a,a):v(x)>0\},
\qquad
\mu:=|E|,
\tag{2}
\]

and

\[
M:=\|v\|_1=\int_{-a}^a v(x)\,dx,
\qquad
s:=M^2.
\tag{3}
\]

By `WI-284` and `WI-295`, complete screening leaves the exact prime-deleted null identity

\[
G(v)+P_a(v)=0,
\tag{4}
\]

where

\[
G(v)
=\frac1{2\pi}\int_{\mathbb R}
 m(z)|\widehat v(z)|^2\,dz,
\qquad
m(z)=\operatorname{Re}\psi\!\left(\frac14+\frac{iz}{2}\right)-\log\pi,
\tag{5}
\]

and

\[
P_a(v)=2L_-(v)L_+(v),
\qquad
L_\pm(v)=\int_{-a}^{a}v(x)e^{\pm x/2}\,dx.
\tag{6}
\]

Recall the exact monotone bathtub profile from `WI-295`,

\[
\mathcal H(u)
=\frac{u}{2\pi}
\int_{-\pi/u}^{\pi/u}m(z)\,dz,
\qquad u>0.
\tag{7}
\]

Then

\[
\boxed{
\mathcal H(s)+2s<0.
}
\tag{8}
\]

Consequently define

\[
\boxed{
\sigma_*:=\inf\{u>0:\mathcal H(u)+2u<0\},
}
\tag{9}
\]

with `\inf\varnothing=+\infty`. Every hypothetical candidate makes the set in (9) nonempty and obeys

\[
\boxed{s>\sigma_*.}
\tag{10}
\]

If `\mu_*` is the unique zero of `\mathcal H` from `WI-295`, then

\[
\boxed{\sigma_*>\mu_*.}
\tag{11}
\]

Finally Cauchy--Schwarz on the support gives `s<=\mu`, while `WI-281` gives `\mu<=\log2`; hence every such candidate must lie in the strict chain

\[
\boxed{
\mu_*<\sigma_*<s\le\mu\le\log2.
}
\tag{12}
\]

In particular

\[
\boxed{
\|v\|_1>\sqrt{\sigma_*},
\qquad
|E|>\sigma_*,
\qquad
P_a(v)>2\sigma_*.
}
\tag{13}
\]

The inequalities in (8)--(13) are exact. The decimal values quoted in the status section are numerical orientation only.

## 1. The exact bathtub sees the actual L1 mass, not only support measure

`WI-295` reached its support floor by first using

\[
|\widehat v(z)|
\le\|v\|_1
\le\sqrt\mu\,\|v\|_2
=\sqrt\mu.
\tag{14}
\]

For the present purpose, stop after the first inequality. Since `v>=0` and has compact support, `M=\|v\|_1` is finite and positive. Parseval gives

\[
p_v(z):=\frac{|\widehat v(z)|^2}{2\pi},
\qquad
\int_{\mathbb R}p_v(z)\,dz=1,
\tag{15}
\]

while (14) gives the sharper candidate-dependent cap

\[
\boxed{
0\le p_v(z)\le\frac{s}{2\pi}.
}
\tag{16}
\]

The proof in `WI-295` shows that `m(z)` is even and strictly increasing in `|z|`. The same bathtub comparison therefore applies with cap `s/(2\pi)` rather than `\mu/(2\pi)`: among all probability densities with that cap, the integral against `m` is minimized by

\[
p_s^*(z)=\frac{s}{2\pi}
\mathbf1_{[-\pi/s,\pi/s]}(z).
\tag{17}
\]

Thus

\[
G(v)\ge\mathcal H(s).
\tag{18}
\]

For the actual compactly supported nonzero `v`, the inequality is strict. Equality would force `|\widehat v|^2` to equal the saturated box (17) almost everywhere, in particular to vanish on an open real interval outside a finite band. Compact support makes `\widehat v` entire, so this would force `\widehat v\equiv0`, contradicting `\|v\|_2=1`. Hence

\[
\boxed{G(v)>\mathcal H(s).}
\tag{19}
\]

This is the information lost when `WI-295` replaced `s` by the larger support cap `\mu`.

## 2. The positive pole term controls the same L1 mass from below

Because `v>=0`, use the finite positive measure

\[
d\nu(x):=v(x)\,dx.
\tag{20}
\]

Cauchy--Schwarz applied to the functions `e^{-x/4}` and `e^{x/4}` in `L^2(d\nu)` gives

\[
\left(\int1\,d\nu\right)^2
\le
\left(\int e^{-x/2}\,d\nu\right)
\left(\int e^{x/2}\,d\nu\right).
\tag{21}
\]

The left side is `M^2=s`, while the two factors on the right are `L_-(v)` and `L_+(v)`. Therefore

\[
L_-(v)L_+(v)\ge s
\tag{22}
\]

and Suzuki's pole factorization yields

\[
\boxed{P_a(v)\ge2s.}
\tag{23}
\]

Combining the null identity (4), the strict bathtub bound (19), and (23),

\[
\mathcal H(s)
<G(v)
=-P_a(v)
\le-2s.
\tag{24}
\]

This is exactly (8).

The feedback is worth isolating. Small `L^1` mass makes the Fourier cap in (16) restrictive and drives the gamma energy upward through `\mathcal H(s)`. The same `L^1` mass cannot simultaneously disappear from the pole term, because the positive exponential moments in (6) satisfy (22). The null identity must balance the two on the same vector, producing the scalar self-consistency condition (8).

## 3. The self-consistency threshold strictly improves the support-only floor

Let

\[
J(u):=\mathcal H(u)+2u.
\tag{25}
\]

`WI-295` proves that `\mathcal H` is continuous, strictly decreasing, tends to `+infinity` at the origin, and has the unique zero `\mu_*`. Therefore

\[
J(u)>0
\qquad(0<u\le\mu_*),
\tag{26}
\]

and in fact

\[
J(\mu_*)=2\mu_*>0.
\tag{27}
\]

If a screened null mode exists, (8) supplies one `s>0` with `J(s)<0`, so the set in (9) is nonempty and `\sigma_*<\infty`. Equations (26)--(27) and continuity imply

\[
\sigma_*>\mu_*.
\tag{28}
\]

Continuity also gives `J(\sigma_*)=0`: if it were positive, there would be a right neighborhood free of negative values, contradicting the definition of the infimum; if it were negative, there would be a left neighborhood of negative values. Therefore every `s` satisfying (8) obeys the strict inequality (10).

On the other hand, normalization and support give

\[
s
=\left(\int_Ev\right)^2
\le |E|\int_Ev^2
=\mu.
\tag{29}
\]

The power-of-two screening theorem `WI-281` gives `\mu\le\log2`. This proves (12)--(13). In particular, the exact support-only threshold from `WI-295` was not yet self-consistent with the positive pole: a screened null mode must live strictly deeper in the admissible support interval.

For orientation only, direct high-precision evaluation of the exact function `J` finds its first zero at

\[
\sigma_*\approx0.3249842281884099928713097522,
\tag{30}
\]

with

\[
\sqrt{\sigma_*}\approx0.5700738795879091958,
\qquad
\frac{\sigma_*}{\log2}\approx0.46885313437454637.
\tag{31}
\]

No decimal enclosure is used in the proof; (9)--(13) are the durable exact statements.

## 4. Relation to the live many-component escape

`WI-295` ended with a genuine gap: its separated-mass estimate

\[
M_1(A)M_1(B)
<\frac{-\mathcal H(\mu)}{4\cosh(R/2)}
\tag{32}
\]

forces exponentially small cross-component `L^1` products at separation `R`, but support measure and `L^2` normalization alone do not stop every remote component from carrying arbitrarily small `L^1` mass.

The present result closes one possible escape from that gap. The **total** `L^1` mass cannot itself tend to zero: it has the universal lower bound (13). It also forces a positive universal pole scale `P_a(v)>2\sigma_*`. Thus a completely screened many-component candidate must simultaneously satisfy

\[
\|v\|_1>\sqrt{\sigma_*}
\tag{33}
\]

and the exponential separated-mass tariff (32).

This still permits a hierarchical geometry in which a bounded core carries essentially all of the mandatory `L^1` mass and distant satellites carry vanishing amplitude. The next useful bridge is therefore not another global uncertainty inequality of the same kind. It must force some of the global `L^1` budget to propagate across the full-span support, for example by combining the cutwise firstness constraints of `WI-270`--`WI-280` with the exact null equation, or by proving source-specific regularity that converts local `L^2` mass into quantitative `L^1` mass on separated regions.

There is also a no-go boundary. Once only the scalar cap `|\widehat v|\le M` and the pole inequality `P_a(v)\ge2M^2` are retained, (8) is the direct closed scalar condition supplied by those data. Any stronger spatial conclusion must use information discarded by that compression: selector geometry, cutwise mass, the exact exponential-moment imbalance, the supported-domain PSD constraint of `WI-284`, or further active prime lags.

## 5. Prior-art and provenance audit

The load-bearing operator decomposition is Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (17 Aug 2026), <https://arxiv.org/abs/2606.09096>, already source-audited in `WI-238`, `WI-240`, `WI-284`, and `SOURCES.md`. Suzuki supplies the localized Weil form and its exact gamma/von-Mangoldt/pole decomposition; the present argument does not alter that source identity.

The gamma multiplier in (5) is the classical archimedean term of Weil's explicit formula. The Fourier estimate `|\widehat v|<=\|v\|_1`, Parseval, Cauchy--Schwarz in the positive measure `v(x)dx`, and the bathtub principle are standard analysis. `WI-295` already established the only special-function input needed here: `m` is even and strictly increasing in `|z|`, so the centered saturated density is the exact optimizer of the pointwise density-cap relaxation.

The line-local novelty audit is therefore narrow. `WI-295` used `\|v\|_1<=\sqrt\mu` before applying the bathtub and obtained a support floor plus an **upper** tariff on separated `L^1` products. It did not retain `\|v\|_1` as the bathtub parameter or combine that lower gamma envelope with the pole's elementary **lower** bound (23). Targeted external searches for this combination around Suzuki's localized Weil form, support-restricted nonnegative vectors, the digamma archimedean multiplier, Fourier `L^1` caps, and uncertainty/bathtub estimates located Suzuki's framework and standard explicit-formula presentations but no statement of (8) or (12)--(13). This search result is not mathematical evidence and no historical priority claim is made.

## 6. Stress tests and limits

- **One-signedness is load-bearing twice.** It is needed upstream to turn screened autocorrelations into support-level deletion of the prime operator, and here to make `d\nu=v(x)dx` a positive measure and the pole moments in (21) positive.
- **Complete screening is load-bearing.** Without it, the null identity (4) acquires the surviving von Mangoldt term, and the scalar feedback (24) changes.
- **The strict bathtub step is analytic, not numerical.** Compact support makes `\widehat v` entire, excluding the band-limited box extremizer. The decimals in (30)--(31) are not evidence.
- **No monotonicity of `J` is assumed.** The definition (9) uses the first entry into the open negative set. The proof of `\sigma_*>\mu_*` uses only continuity and positivity of `J` through `\mu_*`; it does not require uniqueness of the zero of `J`.
- **The global `L^1` floor does not control tails.** A distant component may still have arbitrarily small `L^1` mass while the core carries (33). This finding narrows but does not close the many-component branch.
- **No simple-critical-zero proportion changes.** The result is a structural constraint on the exceptional/off-line route toward the line's ultimate RH objective.

## Research consequence

Complete one-signed screening now has a closed scalar gamma-pole feedback in addition to the selector and cut constraints:

\[
\boxed{
\mathcal H(\|v\|_1^2)+2\|v\|_1^2<0.
}
\tag{34}
\]

This upgrades the `WI-295` support-only floor to a simultaneous `L^1`, support-measure, and pole-energy floor. The unresolved escape is correspondingly sharper: a many-component candidate must keep a fixed amount of total positive amplitude while making cross-component positive masses exponentially hierarchical. The next genuinely new step must show that firstness or the exact Suzuki null equation forbids concentrating essentially all of that mandatory amplitude in one core while arbitrarily weak satellites maintain the full aperture.