# WI-310 — Capping the clipped tail preserves the uniform witness without endpoint overcharge

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY`.

**Parent findings:** WI-307, WI-308, WI-309, WI-247.

WI-309 makes the clipped-tail coercive floor uniform in the outer aperture by adapting an endpoint-singular unit-window localizer to the reserve level `B`. That succeeds at the lower end of the tail multiplier, but the same adaptation has a previously unrecorded opposite effect: if one retains the **entire** unbounded clipped excess

\[
q_B(t)=(\sigma_1(t)-B)_+,
\]

then its localized multiplier grows like `1/eta_B` on every fixed bounded frequency interval as `B -> infinity`. The reserve gate used in WI-307/WI-309 necessarily forces `B -> infinity` with the outer aperture. Consequently the bounded Fredholm comparison

\[
Q=\mathcal D_{L,\chi_B,B}+\mathcal T_{\chi_B,B}
\]

must develop arbitrarily deep **discrete negative modes** along the adaptive family, regardless of whether RH is true. Thus a uniform lower bound of the form

\[
\mathcal D_{L,\chi_B,B}\succeq-c_0I
\]

cannot be the large-aperture endgame for the uncapped WI-309 split.

There is, however, an exact source-valid repair that keeps the useful part of WI-309 and removes this artificial overcharge. Replace the full excess by its bounded cap

\[
\widehat q_B(t):=\min\{q_B(t),1/2\}.
\]

The corresponding localized tail satisfies the **uniform two-sided operator bound**

\[
\boxed{
\frac1{64\pi e}I\preceq\widehat{\mathcal T}_{\chi_B,B}
\preceq\frac12I,
}
\]

while the exact source identity remains

\[
Q=\widehat{\mathcal D}_{L,\chi_B,B}
 +\widehat{\mathcal T}_{\chi_B,B}.
\]

Moreover

\[
\widehat{\mathcal D}_{L,\chi_B,B}
\succeq \mathcal D_{L,\chi_B,B},
\]

so its negative index is still finite whenever the WI-307 reserve gate is imposed. A first-crossing zero mode from WI-247 still forces a negative direction at depth at least `1/(64 pi e)`, but the capped comparison can no longer acquire diverging negativity merely because the retained positive tail was allowed to grow without bound.

The mathematical consequence is a correction of the live finite-sector target after WI-309: **the full uncapped Fredholm comparison is the wrong quantity to control uniformly; a bounded retained-tail comparison preserves the uniform RH-failure witness without manufacturing arbitrarily deep negative spectrum.**

## 1. The WI-307 reserve gate necessarily sends `B` to infinity

Use the notation of WI-307/WI-309. For the unit-window localizer `chi_B`,

\[
A_{L,\chi_B}
=\sum_{\log n<2L}
 c_n\bigl(1-\rho_B(\log n)\bigr)J_{\log n},
\qquad
c_n=\frac{2\Lambda(n)}{\sqrt n}.
\tag{1}
\]

The support of `chi_B` has length one. Hence

\[
\rho_B(a)=0\qquad(a\ge1).
\tag{2}
\]

Let

\[
u_L=(2L)^{-1/2}\mathbf1_{(-L,L)}.
\]

For `0 <= a <= 2L`, direct overlap of the interval with its translate gives

\[
\langle u_L,J_a u_L\rangle
=1-\frac{a}{2L}.
\tag{3}
\]

For `e <= n <= e^L`, equations (2)--(3) imply

\[
1-\rho_B(\log n)=1,
\qquad
1-\frac{\log n}{2L}\ge\frac12.
\]

Therefore

\[
\begin{aligned}
\|A_{L,\chi_B}\|
&\ge \langle u_L,A_{L,\chi_B}u_L\rangle\\
&\ge \frac12\sum_{e\le n\le e^L}c_n\\
&=\sum_{e\le n\le e^L}\frac{\Lambda(n)}{\sqrt n}.
\end{aligned}
\tag{4}
\]

By the prime number theorem and partial summation,

\[
\sum_{n\le x}\frac{\Lambda(n)}{\sqrt n}
\sim2\sqrt x,
\tag{5}
\]

so the right side of (4) diverges like `2 e^(L/2)`. In particular, every reserve choice satisfying the sufficient WI-307/WI-309 norm gate

\[
B_L>\|A_{L,\chi_{B_L}}\|
\tag{6}
\]

must obey

\[
B_L\longrightarrow\infty.
\tag{7}
\]

WI-309's explicit choice `B_L=P_L+1` is one such sequence, but the conclusion (7) is not tied to that crude upper bound. It follows already from the active translations with shift between `1` and `L`.

This statement concerns the norm gate actually used in WI-307/WI-309. It does not claim that every conceivable proof of positive essential spectrum for every alternative comparison must use a reserve satisfying (6).

## 2. The full clipped excess grows like `1/eta_B` on bounded frequencies

Recall the WI-309 definitions

\[
T_B=\max\{1000,2\pi e^{B+C_1+1}\},
\qquad
\eta_B=\frac1{\log(2T_B)},
\tag{8}
\]

and

\[
\beta_B=\frac{1+\eta_B}{2}.
\]

For sufficiently large `B`, the exponential branch in (8) is active. WI-309 proves the pointwise Fourier lower bound

\[
|F_{\chi_B}(s)|^2
\ge
\frac{\eta_B\Gamma(\beta_B)^2}{4}s^{-1-\eta_B}
\qquad(s\ge S_{\eta_B}),
\tag{9}
\]

with `S_eta < 128 < 2T_B`, and also `eta_B<1/7` and `Gamma(beta_B)>1/2`.

The large-frequency source bound used in WI-307 gives, for `t >= T_B`,

\[
q_B(t)
\ge
\log\frac{t}{T_B}+1-\frac1t.
\tag{10}
\]

Fix `xi` with `|xi| <= T_B`, put `s=t-xi`, and restrict to `s >= 4T_B`. Then

\[
t=s+\xi\ge s-T_B\ge\frac{s}{2},
\]

and, since `T_B >= 1000`, (10) yields

\[
q_B(s+\xi)
\ge
\log\frac{s}{2T_B}+\frac12.
\tag{11}
\]

The exact localized tail multiplier from WI-308 is

\[
r_B(\xi)
=\frac1{2\pi}\int_{\mathbb R}
 q_B(t)|F_{\chi_B}(t-\xi)|^2\,dt.
\tag{12}
\]

Combining (9), (11), and nonnegativity gives

\[
\begin{aligned}
r_B(\xi)
&\ge
\frac{\eta_B\Gamma(\beta_B)^2}{8\pi}
\int_{4T_B}^{\infty}
\left(\log\frac{s}{2T_B}+\frac12\right)
 s^{-1-\eta_B}\,ds\\
&=
\frac{\Gamma(\beta_B)^2}{8\pi}
(4T_B)^{-\eta_B}
\left(
\frac1{\eta_B}+\log2+\frac12
\right).
\end{aligned}
\tag{13}
\]

The integral in (13) is exact; it uses

\[
\int_R^\infty \log(s/A)s^{-1-\eta}\,ds
=R^{-\eta}
\left(
\frac{\log(R/A)}\eta+\frac1{\eta^2}
\right).
\]

Since

\[
(4T_B)^{-\eta_B}
=e^{-1}2^{-\eta_B}
\ge e^{-1}2^{-1/7}
\]

and `Gamma(beta_B)^2>1/4`, (13) gives the explicit uniform-on-the-window estimate

\[
\boxed{
r_B(\xi)
\ge
\kappa
\left(
\frac1{\eta_B}+\log2+\frac12
\right)
\quad(|\xi|\le T_B),
}
\tag{14}
\]

where

\[
\kappa:=\frac{e^{-1}2^{-1/7}}{32\pi}>0.00331.
\tag{15}
\]

On the exponential branch of (8),

\[
\frac1{\eta_B}
=\log(2T_B)
=B+C_1+1+\log(4\pi).
\tag{16}
\]

Thus the lower edge proved in WI-309 is not the whole story: **the full localized tail grows at least linearly in `B` on every fixed bounded frequency region.**

## 3. The uncapped Fredholm comparison has arbitrarily deep negative modes

Fix once and for all a nonzero smooth compactly supported test `f`, normalized by `||f||_2=1`, and choose a finite `R` such that

\[
m_f(R):=
\frac1{2\pi}\int_{-R}^{R}|F_f(\xi)|^2\,d\xi>0.
\tag{17}
\]

For every sufficiently large `B`, `R<T_B`, so (14) and the multiplier formula imply

\[
\mathcal T_{\chi_B,B}(f)
\ge
\kappa m_f(R)
\left(
\frac1{\eta_B}+\log2+\frac12
\right).
\tag{18}
\]

Take now any sequence of outer apertures `L -> infinity` and reserves satisfying (6). By (7), (16), and (18),

\[
\mathcal T_{\chi_{B_L},B_L}(f)\longrightarrow+\infty.
\tag{19}
\]

For all large `L`, the fixed test `f` belongs to the outer-aperture form domain. The exact split of WI-308/WI-309 gives

\[
\langle f,\mathcal D_{L,\chi_{B_L},B_L}f\rangle
=Q(f)-\mathcal T_{\chi_{B_L},B_L}(f),
\tag{20}
\]

where `Q(f)` is independent of `L`. Hence

\[
\boxed{
\langle f,\mathcal D_{L,\chi_{B_L},B_L}f\rangle
\longrightarrow-\infty.
}
\tag{21}
\]

Under (6), WI-307 gives strictly positive essential spectrum for every individual bounded comparison `D`. Therefore the increasingly negative Rayleigh quotients in (21) force **discrete** negative eigenvalues whose depth is unbounded along the family.

This is an architecture-level warning about the chosen coordinates, not evidence against RH. The exact source form `Q(f)` is fixed; the divergence is created by moving an ever larger positive part of `Q` into `T` and subtracting that same part from `D`.

In particular, the fixed-aperture criterion from WI-308,

\[
\mathcal D_{L,\chi,B}\succeq-c_{\chi,B}I,
\]

remains correct at any one aperture, but **cannot be promoted to a uniform large-aperture strategy for the WI-309 adaptive uncapped split**. The problem is stronger than merely losing uniform compactness constants: the comparison itself necessarily acquires unbounded negative depth.

## 4. A bounded tail cap preserves the uniform witness exactly

Define

\[
\widehat q_B(t):=\min\{q_B(t),1/2\}.
\tag{22}
\]

Carry this nonnegative multiplier through the same sliding-localization identity as WI-308. Thus

\[
\widehat r_B(\xi)
=\frac1{2\pi}\int_{\mathbb R}
\widehat q_B(t)|F_{\chi_B}(t-\xi)|^2\,dt
\tag{23}
\]

and

\[
\widehat{\mathcal T}_{\chi_B,B}(f)
=\frac1{2\pi}\int_{\mathbb R}
\widehat r_B(\xi)|F_f(\xi)|^2\,d\xi.
\tag{24}
\]

Because `||chi_B||_2=1`, Plancherel gives

\[
\frac1{2\pi}\int_{\mathbb R}|F_{\chi_B}(s)|^2\,ds=1.
\]

The pointwise bound `0 <= qhat_B <= 1/2` therefore yields

\[
0\le\widehat r_B(\xi)\le\frac12
\qquad\text{for all }\xi.
\tag{25}
\]

On the other hand, WI-309 proved

\[
q_B(t)>\frac12
\qquad(|t|>T_B).
\tag{26}
\]

Hence `qhat_B=1/2` on exactly the exterior region used in WI-309's lower-floor argument. No estimate in that argument used values of `q_B` larger than `1/2`. The same proof therefore gives, with the same constant,

\[
\widehat r_B(\xi)
\ge c_0,
\qquad
c_0:=\frac1{64\pi e},
\tag{27}
\]

uniformly in `B` and `xi`.

Equations (24)--(27) give the two-sided source-exact reserve

\[
\boxed{
c_0I
\preceq
\widehat{\mathcal T}_{\chi_B,B}
\preceq
\frac12I.
}
\tag{28}
\]

Now define the capped comparison by the exact identity

\[
\widehat{\mathcal D}_{L,\chi_B,B}
:=Q-\widehat{\mathcal T}_{\chi_B,B}.
\tag{29}
\]

The capped tail is bounded, so (29) is a bounded-form perturbation of the closed fixed-aperture logarithmic Weil form and has the same form domain. Since

\[
0\le\widehat{\mathcal T}_{\chi_B,B}
\le\mathcal T_{\chi_B,B},
\]

we also have the exact form ordering

\[
\boxed{
\widehat{\mathcal D}_{L,\chi_B,B}
=\mathcal D_{L,\chi_B,B}
 +\bigl(\mathcal T_{\chi_B,B}-\widehat{\mathcal T}_{\chi_B,B}\bigr)
\succeq
\mathcal D_{L,\chi_B,B}.
}
\tag{30}
\]

If (6) holds, WI-307 gives finite negative index for `D`. Any subspace on which `Dhat` is negative is also negative for `D`, so

\[
\boxed{
n_-(\widehat{\mathcal D}_{L,\chi_B,B})
\le n_-(\mathcal D_{L,\chi_B,B})<\infty.
}
\tag{31}
\]

Thus the cap does not reintroduce an infinite negative sector.

Most importantly, the RH-failure witness survives. If WI-247 supplies a first-crossing vector `v_* != 0` with

\[
Q(v_*)=0,
\]

then (28)--(29) give

\[
\boxed{
\langle v_*,\widehat{\mathcal D}_{L,\chi_B,B}v_*\rangle
=-\widehat{\mathcal T}_{\chi_B,B}(v_*)
\le-c_0\|v_*\|_2^2.
}
\tag{32}
\]

Conversely,

\[
\widehat{\mathcal D}_{L,\chi_B,B}\succeq-c_0I
\quad\Longrightarrow\quad
Q\succeq0
\tag{33}
\]

at that aperture. Unlike the uncapped comparison, however, (28) also gives for every test `f`

\[
\boxed{
\langle f,\widehat{\mathcal D}_{L,\chi_B,B}f\rangle
\ge Q(f)-\frac12\|f\|_2^2,
}
\tag{34}
\]

so the localization coordinates can no longer manufacture arbitrarily deep negative Rayleigh quotients from a fixed source direction by increasing `B`.

The numerical value `1/2` is not mystical. More generally one may cap at any fixed `h>=1/2`; the WI-309 lower proof still sees at least `1/2` on the exterior while the resulting tail is bounded above by `hI`. The choice `h=1/2` is the smallest cap that preserves that proof verbatim.

## 5. Consequence for the post-WI-309 program

WI-309 correctly established an aperture-independent source tail gap. What fails is the stronger implicit hope that the **same full-tail split** could also have a uniformly tame negative comparison sector. Equations (18)--(21) show that it cannot: once the reserve is raised according to the WI-307 norm gate, the endpoint singularity makes the retained full logarithmic tail increasingly visible at ordinary frequencies, and `D=Q-T` must compensate by becoming deeply negative.

This separates two questions that were conflated by the uncapped coordinates:

\[
\text{retain enough tail to force a uniform RH-failure gap}
\]

and

\[
\text{retain the entire unbounded positive tail}.
\]

Only the first is needed. The capped comparison (29) keeps exactly that property while bounding the bookkeeping subtraction uniformly.

The next useful gate is therefore not a lower bound for the uncapped `lambda_min(D)`. It is a source-specific estimate on the finite negative sector of `Dhat`, or another bounded retained-tail comparison with the same two-sided reserve. Such an estimate would have to use genuine structure of the Weil source or first-crossing vector; (28) alone does not prove positivity.

This finding does **not** prove RH, does not bound the number of capped negative eigenvalues uniformly in `L`, and does not show that `Dhat >= -c_0 I`. It only removes a false target and supplies a source-valid normalization in which a uniform lower-bound program is not already impossible for bookkeeping reasons.

## 6. Prior art and novelty audit

The load-bearing ingredients are separated as follows.

- WI-307 supplies the reserve-lifted comparison, the compressed prime-power translation operator, and the finite-negative-index conclusion under `B>||A||`.
- WI-308 supplies the exact clipped-tail multiplier formula and the fixed-aperture source identity `Q=D+T`.
- WI-309 supplies the endpoint-singular localizer, the quantitative Fourier tail lower bound, and the uniform constant `c_0=1/(64 pi e)`.
- WI-247 supplies the finite-aperture first-crossing zero mode under RH failure.
- The divergence in (4)--(7) uses only the classical prime number theorem and partial summation. The bounded-cap ordering, Plancherel bound, and finite-negative-index monotonicity are standard quadratic-form/spectral facts.

A fresh targeted audit on 16 September 2026 checked the closest recent fixed-window Weil-positivity work and searched for bounded/capped tail, clipped multiplier, endpoint-singular localization, and Moyal-tail formulations. Vincent Liu's 15 September 2026 manuscript retains a fixed-window Fourier complement and selected positive low-rank tail directions; it does not state the adaptive endpoint overcharge (14)--(21) or the bounded cap (22)--(34). The recent finite Galerkin tail-order literature likewise studies cutoff certification rather than this sliding adaptive split. No equivalent statement was located.

Search absence is not a priority claim. The durable contribution here is the exact internal correction: the WI-309 localizer makes the **upper** size of the full retained tail diverge under the reserve gate, and scalar capping preserves the already-proved uniform **lower** gap while preventing that coordinate artifact.

### Validation and falsification boundary

The result should be corrected or withdrawn if any of the following fails:

1. the WI-309 Fourier lower bound (9), its normalization, or its admissibility on the closed logarithmic form domain is invalid;
2. the source lower envelope used in (10) has a missing constant or Fourier normalization that destroys the `log(t/T_B)` growth;
3. the Moyal multiplier normalization in WI-308 differs from (12)/(23);
4. the support-length-one identity `rho_B(a)=0` for `a>=1` is incompatible with the actual WI-309 localizer convention;
5. the reserve gate being analyzed is not the WI-307/WI-309 condition `B>||A||`;
6. the capped multiplier cannot be carried through the exact localization identity as a bounded positive sub-tail of the already established `T`.

All six interfaces were checked against WI-307--WI-309 in this pass. The result uses no unverified finite matrix certificate, no zero-spacing conjecture, and no RH-conditional arithmetic estimate.