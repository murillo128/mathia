# WI-308 — Clipped source tails turn finite odd zero modes into gapped Fredholm witnesses

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY`.

**Parent findings:** WI-307, WI-247, WI-236, WI-303.

WI-307 removes the frozen-reserve essential-spectrum obstruction at every fixed aperture: after raising the exterior reserve to `B`, the localized bounded comparison has positive essential spectrum once `B>||A_{L,chi}||`, but an arbitrary finite-rank repair is not source-valid. The omitted high-frequency source tail supplies exactly the missing structure. With a canonical clipping of the true unit-window symbol, that tail remains positive after sliding localization and becomes a Fourier multiplier whose symbol has a **strictly positive global minimum**. Consequently the full Weil form dominates the Fredholm comparison by a positive scalar reserve.

More precisely, for every nonzero real

\[
\chi\in C_c^\infty((-1,1))
\]

(normalized by `||chi||_2=1`) and every finite reserve `B`, there is an exact source decomposition on each fixed outer aperture `L`,

\[
\boxed{
Q=\mathcal D_{L,\chi,B}+\mathcal T_{\chi,B},
\qquad
\mathcal T_{\chi,B}\ge c_{\chi,B}I,
\qquad
c_{\chi,B}>0.
}
\tag{1}
\]

If in addition `B>||A_{L,chi}||`, then `D_{L,chi,B}` has strictly positive essential spectrum by WI-307. Thus positivity of `Q` at that fixed aperture is reduced to the finite discrete negative sector of `D`: it is enough to certify

\[
\boxed{
\lambda_{\min}(\mathcal D_{L,\chi,B})\ge -c_{\chi,B}.
}
\tag{2}
\]

Conversely, the first-crossing zero mode forced by WI-247 under an RH failure must satisfy

\[
\boxed{
\lambda_{\min}(\mathcal D_{L,\chi,B})\le -c_{\chi,B}<0.
}
\tag{3}
\]

So a hypothetical first off-critical crossing cannot hide merely at zero spectral margin in the clipped comparison: it forces a discrete Fredholm witness separated from zero by the source-exact tail reserve `c_{chi,B}`.

This is a fixed-aperture reduction, not an RH proof. The unresolved problem is to make `c_{chi,B}` effective and control the finite discrete spectrum uniformly as the aperture grows.

## 1. Canonical clipping preserves the omitted source exactly

Use the unit-window source symbol from WI-307,

\[
\sigma_1(t)
=A(t)-\sum_{n\in\{2,3,4,5,7\}}c_n\cos(t\log n),
\qquad
c_n=\frac{2\Lambda(n)}{\sqrt n}.
\tag{4}
\]

The large-frequency estimate already audited there gives

\[
\sigma_1(t)\to+\infty
\qquad(|t|\to\infty).
\tag{5}
\]

For a finite real `B`, define the clipped symbol and its omitted positive tail by

\[
m_B(t):=\min\{\sigma_1(t),B\},
\qquad
q_B(t):=(\sigma_1(t)-B)_+.
\tag{6}
\]

Then

\[
\sigma_1=m_B+q_B,
\qquad q_B\ge0.
\tag{7}
\]

Because of (5), the sublevel set `{t:sigma_1(t)<B}` is compact. Hence

\[
m_B-B=-(B-\sigma_1)_+
\tag{8}
\]

is bounded and compactly supported in frequency. If `P(h)` denotes the finite-rank pole contribution in the normalization of WI-307, put

\[
\begin{aligned}
R_B(h)
&:=\mathcal P(h)
 +\frac1{2\pi}\int_{\mathbb R}m_B(t)|F_h(t)|^2\,dt,\\
T_B(h)
&:=\frac1{2\pi}\int_{\mathbb R}q_B(t)|F_h(t)|^2\,dt.
\end{aligned}
\tag{9}
\]

Then, on the smooth unit-window core,

\[
\boxed{Q(h)=R_B(h)+T_B(h),\qquad T_B(h)\ge0.}
\tag{10}
\]

Moreover

\[
R_B=B I+C_B
\tag{11}
\]

with `C_B` compact. Indeed (8) gives a bounded compact-frequency-support multiplier; its inverse-Fourier compression to the bounded unit window is Hilbert--Schmidt, and the pole term is finite rank. This is the same compactness mechanism as WI-307, but the clipping (6) makes the omitted source an exact positive form rather than an unspecified lower-comparison gap.

## 2. Sliding localization turns the tail into an exact multiplier

For an outer-aperture test `f`, use the same sliding localizer as WI-307,

\[
f_y(u)=\chi(u)f(u+y),
\tag{12}
\]

and the source-exact localization identity

\[
Q(f)=\int Q(f_y)\,dy-\mathcal E_\chi(f).
\tag{13}
\]

Define

\[
\mathcal D_{L,\chi,B}(f)
:=\int R_B(f_y)\,dy-\mathcal E_\chi(f),
\qquad
\mathcal T_{\chi,B}(f):=\int T_B(f_y)\,dy.
\tag{14}
\]

Equations (10) and (13) give the exact identity

\[
\boxed{Q(f)=\mathcal D_{L,\chi,B}(f)+\mathcal T_{\chi,B}(f).}
\tag{15}
\]

The tail can be evaluated without approximation. With the Fourier convention

\[
F_h(t)=\int h(x)e^{-itx}\,dx,
\qquad
\|h\|_2^2=\frac1{2\pi}\int|F_h(t)|^2dt,
\tag{16}
\]

direct expansion of (12), followed by Plancherel in the translation variable `y`, gives the classical spectrogram/Moyal marginal

\[
\int_{\mathbb R}|F_{f_y}(t)|^2dy
=
\frac1{2\pi}
\int_{\mathbb R}|F_f(\xi)|^2
|F_\chi(t-\xi)|^2d\xi.
\tag{17}
\]

The normalization in (17) is rederived here rather than imported from a convention-dependent statement of Moyal's identity. Tonelli is applicable because the tail integrand is nonnegative. Substituting (17) into (14) gives

\[
\boxed{
\mathcal T_{\chi,B}(f)
=
\frac1{2\pi}
\int_{\mathbb R}r_{\chi,B}(\xi)|F_f(\xi)|^2d\xi,
}
\tag{18}
\]

where

\[
\boxed{
r_{\chi,B}(\xi)
=
\frac1{2\pi}
\int_{\mathbb R}q_B(t)
|F_\chi(t-\xi)|^2dt.
}
\tag{19}
\]

Thus the source tail that was discarded in the lower comparison of WI-307 becomes an explicit positive Fourier multiplier after localization.

## 3. The tail multiplier has a strictly positive bottom

The key point is stronger than pointwise positivity:

\[
\boxed{
c_{\chi,B}:=\inf_{\xi\in\mathbb R}r_{\chi,B}(\xi)>0.}
\tag{20}
\]

There are three steps.

First, (5) implies that there is `T_B<infinity` such that

\[
q_B(t)>0\qquad(|t|>T_B).
\tag{21}
\]

For a fixed `xi`, if `r_{chi,B}(xi)=0`, then the nonnegative integrand in (19) forces `F_chi(t-xi)=0` almost everywhere on either open tail in (21). Since `chi` is compactly supported, `F_chi` is entire; continuity upgrades the almost-everywhere vanishing to interval vanishing, and the identity theorem would give `F_chi identically 0`, contradicting `chi nonzero`. Hence

\[
r_{\chi,B}(\xi)>0
\qquad\text{for every finite }\xi.
\tag{22}
\]

Second, `r_{chi,B}` is continuous. The archimedean/digamma expression underlying (4) gives the standard upper growth

\[
q_B(t)=O(\log(2+|t|)),
\tag{23}
\]

while `F_chi` is Schwartz. This gives a common integrable majorant on compact `xi`-sets and therefore continuity by dominated convergence.

Third, `r_{chi,B}(xi)` tends to `+infinity` as `|xi|->infinity`. Choose a bounded interval `I` with

\[
\int_I|F_\chi(s)|^2ds>0.
\tag{24}
\]

Changing variables `t=xi+s` in (19) and restricting to `s in I` gives

\[
r_{\chi,B}(\xi)
\ge
\frac1{2\pi}
\int_Iq_B(\xi+s)|F_\chi(s)|^2ds.
\tag{25}
\]

The lower envelope used in WI-307 implies

\[
\inf_{s\in I}q_B(\xi+s)\to+\infty
\qquad(|\xi|\to\infty),
\tag{26}
\]

so (25) diverges. A continuous positive function tending to `+infinity` at both ends attains a strictly positive minimum on a compact interval. This proves (20).

Combining (18), (20), and Plancherel gives the source-valid coercive estimate

\[
\boxed{
\mathcal T_{\chi,B}(f)
\ge c_{\chi,B}\|f\|_2^2.
}
\tag{27}
\]

The identities above are first established on the smooth compact core. Since `D_{L,chi,B}` is bounded by the WI-307 decomposition and the tail is the positive logarithmic-growth multiplier (18), they extend by form closure to the fixed-aperture logarithmic form domain used in WI-247.

## 4. The hypothetical first zero mode becomes a gapped discrete witness

WI-307 gives

\[
\mathcal D_{L,\chi,B}
= B I-A_{L,\chi}+K_{L,\chi,B},
\tag{28}
\]

where `A_{L,chi}` is the finite active prime-power compressed-translation sum and `K_{L,chi,B}` is compact. If

\[
B>\|A_{L,\chi}\|,
\tag{29}
\]

then the essential spectrum of `D_{L,chi,B}` lies strictly to the right of zero. Consequently only finitely many eigenvalues can lie at or below the negative level `-c_{chi,B}`.

Now suppose the first-crossing framework of WI-247 applies and RH fails. It then supplies a finite aperture `L=a_*` and a nonzero odd form-domain vector `v_*` with

\[
Q(v_*)=0.
\tag{30}
\]

Using (15) and (27),

\[
\langle v_*,\mathcal D_{a_*,\chi,B}v_*\rangle
=-\mathcal T_{\chi,B}(v_*)
\le-c_{\chi,B}\|v_*\|^2.
\tag{31}
\]

Therefore

\[
\boxed{
\lambda_{\min}(\mathcal D_{a_*,\chi,B})
\le-c_{\chi,B}<0.
}
\tag{32}
\]

Because of (29), this witness lies in a finite discrete spectral sector below the positive essential spectrum. This is stronger than the zero-margin obstruction in WI-236: after canonical clipping, a first source zero forces a quantitatively negative comparison direction.

More generally, any near-zero source direction satisfying

\[
Q(f)\le\varepsilon\|f\|^2
\tag{33}
\]

obeys

\[
\langle f,\mathcal D_{L,\chi,B}f\rangle
\le(\varepsilon-c_{\chi,B})\|f\|^2.
\tag{34}
\]

Thus the implication is stable at fixed aperture: source modes with `epsilon<c_{chi,B}` still force a negative Fredholm witness separated from zero.

## 5. Fixed-aperture positivity is a finite-sector spectral problem

Equation (1) gives an immediate converse certificate. If for some fixed `L`, nonzero real `chi`, and reserve satisfying (29), one proves

\[
\mathcal D_{L,\chi,B}\ge-c_{\chi,B}I,
\tag{35}
\]

then

\[
Q\ge0
\tag{36}
\]

on that aperture. If the left side of (35) is instead bounded below by `-c_{chi,B}+delta` for some `delta>0`, then

\[
Q\ge\delta I.
\tag{37}
\]

Since the essential spectrum of `D` is positive, verifying (35) concerns only finitely many discrete eigenvalues below zero. This is a source-valid replacement for the arbitrary finite-rank repair explicitly rejected in WI-307: no artificial repair is inserted; the reserve comes from the exact omitted part of the original Weil source.

This does **not** yet produce a uniform-in-`L` argument. Two quantitative quantities can deteriorate as `L` grows. The reserve required by (29) grows with the active prime-power translation mass, while moving `B` upward pushes the region where `q_B` is positive farther into the Fourier tails of `chi`. The strict number `c_{chi,B}` can therefore be extremely small. WI-248 already records the severe radius cost of uniform prime-symbol envelopes, so this finding does not relabel that growth as a new obstruction.

The next decisive gate is consequently effective rather than existential: obtain a computable lower bound for `c_{chi,B}` together with a certified lower bound for the finitely many negative eigenvalues of `D_{L,chi,B}`, in a regime whose deterioration with `L` is controlled strongly enough to exclude a first crossing.

## 6. Prior art, novelty, and boundaries

The ingredients are separated deliberately.

- The unit-window source normalization, the large-frequency lower envelope for `sigma_1`, the sliding-localization identity, and the Fredholm structure `B I-A+K` are inherited from and audited in WI-307.
- The implication from RH failure to a finite-aperture nonzero odd zero mode is the Yoshida--Suzuki first-crossing framework as isolated in WI-247.
- The spectrogram/Moyal marginal (17) is classical time-frequency analysis. Its precise normalization is rederived above, so the present argument does not depend on a convention imported from a secondary formula.
- The new exact deduction within this line is to choose the canonical clipped symbol `min(sigma_1,B)`, retain the omitted positive source tail through sliding localization, prove that its convolution multiplier has the strict global floor (20), and combine that floor with WI-307 and WI-247 to obtain the finite-sector criterion (35) and the gapped zero-mode witness (32).

A targeted audit of the own-line finding corpus found no earlier statement of this clipped-tail coercivity mechanism. A targeted literature search found the Moyal/STFT ingredient as classical but did not locate a source asserting this combined Weil-form criterion. No priority claim is made from that search outcome.

The result also respects the warning of WI-303: it does not assign invariant meaning to a noncanonical finite-rank tail decomposition. The split (6) is a canonical scalar clipping of the exact unit-window source symbol, and the positive tail is carried through the localization identity without replacement.

## Consequence

At fixed aperture, the architectural gap left by WI-307 is closed: the omitted source is not merely nonnegative but supplies a strictly positive scalar coercive reserve after localization. A hypothetical first RH-failure zero mode must therefore appear as a **strictly negative discrete Fredholm eigenvalue** of the clipped comparison, and positivity can be certified by ruling out only that finite negative sector against the explicit threshold `-c_{chi,B}`.

The remaining RH-level problem is no longer the existence of a source-valid repair at a fixed aperture. It is the quantitative, uniform control of the coercive floor and of the finite discrete spectrum as the aperture varies.