# WI-360 — prime-power eight blocks tail-dropping localization past its activation radius

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT + NON-RH`.

## Claim

A recent fixed-window Weil-form manuscript of Vincent Liu contains an analytic obstruction that is directly relevant to the current `weil_inertia` first-crossing program. The obstruction is substantially more specific than the generic norm barriers in WI-248, WI-358, and WI-359: once the support half-width passes the activation radius of the prime power `8`, a natural localization scheme that imports the unit-window lower comparison, drops the exterior Fourier tail, and then tries to repair the resulting defect by a **fixed compact operator** is impossible.

Use Liu's normalization of the classical Weil form on

\[
\mathcal D_L=C_c^\infty((-L,L);\mathbb C).
\]

Let `R_1` be the bounded unit-window lower comparison used in his Theorem A, whose scalar floor is

\[
\beta_0=\frac1{16}.
\tag{1}
\]

Fix a real normalized localizer `\chi\in\mathcal D_1`, set

\[
f_y(u)=\chi(u)f(u+y),
\]

and define

\[
\mathcal L_\chi(f)=\int_{\mathbb R}Q(f_y)\,dy,
\qquad
\mathcal E_\chi(f)=\mathcal L_\chi(f)-Q(f),
\]

\[
\mathcal M_\chi(f)=\int_{\mathbb R}R_1(f_y)\,dy,
\qquad
\mathcal D_\chi(f)=\mathcal M_\chi(f)-\mathcal E_\chi(f).
\tag{2}
\]

Then for every

\[
L>\frac{\log8}{2}=1.03972077\ldots
\tag{3}
\]

there is a fixed nonzero real `g\in\mathcal D_L` and a high-frequency modulation sequence

\[
f_k(u)=e^{iT_ku}g(u),
\qquad
T_k=\frac{2\pi k}{\log8},
\tag{4}
\]

such that

\[
\boxed{
\lim_{k\to\infty}
\frac{\mathcal D_\chi(f_k)}{\|f_k\|_2^2}
=
\frac1{16}-\frac{\log2}{2\sqrt2}
< -\frac18.
}
\tag{5}
\]

Consequently, for **every fixed bounded compact self-adjoint** operator `K_c` on `L^2(-L,L)`,

\[
\mathcal D_\chi(f)+\langle f,K_cf\rangle
\]

cannot be nonnegative for all `f\in\mathcal D_L`. More generally, any compensating quadratic form `\mathcal U` satisfying

\[
\mathcal D_\chi+\mathcal U\ge0
\]

must retain an asymptotically nonvanishing payment along the same modulated sequence:

\[
\boxed{
\liminf_{k\to\infty}
\frac{\mathcal U(f_k)}{\|f_k\|_2^2}
\ge
\frac{\log2}{2\sqrt2}-\frac1{16}.
}
\tag{6}
\]

The mathematical content of (5)--(6) is prior art from Liu's Obstruction Theorem, not a new theorem claimed by Mathia. The contribution of this finding is an independent audit of the short proof and its placement in the current `weil_inertia` program: **a compact correction cannot replace the Fourier-tail/source information discarded by this localization once prime-power `8` becomes active.**

This does not obstruct source-exact tail retention, noncompact compensation, or a first-crossing argument that uses the actual null mode. It closes one tempting propagation architecture, not localized Weil positivity itself.

## 1. Exact source normalization and the localization defect

Liu writes the classical Weil form as

\[
Q(f)=\mathcal P(f)
+\frac1{2\pi}\int_{\mathbb R}A(t)|F_f(t)|^2dt
-\sum_{n\ge2}\frac{2\Lambda(n)}{\sqrt n}H_f(\log n),
\tag{7}
\]

where

\[
A(t)=\Re\psi\!\left(\frac14+\frac{it}{2}\right)-\log\pi,
\]

and compact support makes the prime-power sum finite: only `\log n<2L` occurs.

For the unit window, `2<2L` is false at the endpoint for `n=8`, so the active list in Liu's unit comparison is

\[
\{2,3,4,5,7\}.
\tag{8}
\]

As soon as

\[
2L>\log8,
\]

the additional prime-power channel `8` enters the full form. This is exactly the threshold in (3).

Put

\[
\rho_\chi(x)=\int_{\mathbb R}\chi(v+x)\chi(v)\,dv.
\tag{9}
\]

Because `\chi` is supported in `(-1,1)`, `\rho_\chi` is even, supported in `(-2,2)`, and

\[
1-\rho_\chi(x)=O(x^2)
\qquad(x\to0).
\tag{10}
\]

A direct Fubini calculation gives

\[
\int_{\mathbb R}h_{f_y}(x)\,dy
=
\rho_\chi(x)h_f(x).
\tag{11}
\]

Substitution into the explicit formula therefore gives the exact defect identity

\[
\begin{aligned}
\mathcal E_\chi(f)
={}&
\int_0^{2L}(1-\rho_\chi(x))
\left(
\frac{2e^{-x/2}}{1-e^{-2x}}
-4\cosh\frac x2
\right)H_f(x)\,dx
\\
&+
\sum_{\log n<2L}
\frac{2\Lambda(n)}{\sqrt n}
(1-\rho_\chi(\log n))H_f(\log n).
\end{aligned}
\tag{12}
\]

The continuous kernel in (12) is integrable at the origin because its singular factor is `O(1/x)` while (10) supplies `O(x^2)`. Thus the localization defect is a bounded quadratic form at every fixed `L`.

The unit-window comparison satisfies

\[
Q=\mathcal D_\chi+\mathcal S_\chi,
\qquad
\mathcal S_\chi:=\mathcal L_\chi-\mathcal M_\chi\ge0,
\tag{13}
\]

on the legal smooth domain. The issue is whether the lower comparison `\mathcal D_\chi` can itself be made nonnegative after discarding the source/frequency information contained in `\mathcal S_\chi`.

## 2. A two-bump witness isolates prime-power eight exactly

Let

\[
a=\log8>2
\]

and choose

\[
d=\min\!\left(\frac1{256},\frac{L-a/2}{2}\right)>0.
\tag{14}
\]

Take a nonzero smooth bump `\phi` supported in `(-d,d)` and define

\[
g(u)=\phi(u+a/2)+\phi(u-a/2).
\tag{15}
\]

The two bumps are disjoint and lie inside `(-L,L)`. Their autocorrelation is supported in the `2d`-neighborhoods of

\[
0,\quad a,\quad -a,
\]

and satisfies

\[
h_g(a)=\frac12\|g\|_2^2.
\tag{16}
\]

The choice `d\le1/256` separates those neighborhoods from every integer logarithm except `\log8`. Indeed the nearest competing integer logarithms are separated from `\log8` by more than `2d`; Liu records the elementary margins using `\log(8/7)>1/8` and `\log(9/8)>1/9`.

Also, since `a>2` and `\rho_\chi` is supported in `(-2,2)`,

\[
\rho_\chi(a)=0.
\tag{17}
\]

Now modulate by (4). At the selected lag,

\[
e^{iT_ka}=1.
\tag{18}
\]

Therefore the discrete contribution of (12), normalized by `\|g\|_2^2`, is exactly

\[
\frac12\frac{2\Lambda(8)}{\sqrt8}
=
\frac{\log2}{2\sqrt2},
\tag{19}
\]

because `\Lambda(8)=\log2`.

The continuous part of (12) tends to zero under the same modulation by the Riemann--Lebesgue lemma. Hence

\[
\frac{\mathcal E_\chi(f_k)}{\|g\|_2^2}
\longrightarrow
\frac{\log2}{2\sqrt2}.
\tag{20}
\]

This is the source-specific core of the obstruction. It does not use a uniform supremum over all prime phases as in WI-248: one prime-power channel is isolated geometrically and phase-locked exactly.

## 3. Every fixed compact repair disappears on the witness

Liu's unit-window comparison has the form

\[
R_1=\frac1{16}I+C_1,
\tag{21}
\]

where `C_1` is compact: it consists of a continuous finite-band integral kernel together with finite-rank pole terms.

For each translated local piece `f_{k,y}`, high-frequency modulation makes the sequence weakly converge to zero. Therefore

\[
\langle f_{k,y},C_1f_{k,y}\rangle\to0.
\]

The `y`-support is uniformly bounded and the integrand has an `L^1(dy)` majorant, so dominated convergence yields

\[
\frac{\mathcal M_\chi(f_k)}{\|g\|_2^2}
\longrightarrow
\frac1{16}.
\tag{22}
\]

Subtracting (20) from (22) proves (5).

Exactly the same weak-null argument applies to any fixed compact `K_c` on `L^2(-L,L)`:

\[
\frac{\langle f_k,K_cf_k\rangle}{\|g\|_2^2}
\longrightarrow0.
\tag{23}
\]

Since the limit in (5) is strictly negative, no such correction can make the comparison globally nonnegative. The numerical margin does not require floating point: `\log2>2/3` and `\sqrt2<3/2` give

\[
\frac{\log2}{2\sqrt2}-\frac1{16}
>
\frac{23}{144}
>
\frac18.
\tag{24}
\]

Equation (6) follows immediately for an arbitrary compensating quadratic form that does succeed.

## 4. Relation to the present first-crossing program

WI-355 shows that any RH failure produces a finite first zero crossing of Suzuki's localized Weil ground energy. WI-356--WI-359 then narrow the propagation problem: threshold activation is singular in the raw `L^2` operator norm but tame in the logarithmic form topology, actual null states have bounded logarithmic energy, and neither budget-only nor norm-compressed continuity can be iterated cofinally.

The present obstruction closes a different shortcut. Suppose one tries to propagate positivity by localizing a larger-window test into unit-window pieces, applies a known positive unit-window comparison to each piece, discards the exterior Fourier tail, and hopes that the discrepancy can be repaired by a fixed compact operator. Equations (5) and (23) show that this architecture already fails immediately after the `8`-channel activates.

The failure is informative because the escaping witness is not a low-energy endpoint concentration. It is a **high-frequency coherent mode** whose spatial autocorrelation isolates `\log8`. Any correction that is compact on the fixed `L^2` window loses that mode. Therefore a viable cofinal localization scheme must retain at least one ingredient whose quadratic value does not vanish on such weakly-null modulations. Examples include:

- the true exterior Fourier tail or another noncompact frequency coercivity term;
- a source-exact compensation that retains the active prime-power channel rather than replacing it by a compact remainder;
- a first-crossing/null-equation restriction strong enough to exclude the two-bump coherent witness from the relevant state class.

This sharpens WI-359's conclusion. WI-359 says scalar norm control of the true bounded perturbation is too coarse. WI-360 says that even a seemingly stronger **compact-operator correction architecture** can be defeated by one exact prime-power resonance if the noncompact tail is removed.

It is also narrower than WI-248. WI-248 proves that a phase-blind uniform prime-symbol envelope has exact recurrent spikes arbitrarily far in frequency. Here no simultaneous recurrence is needed: the lag `\log8` is isolated by support geometry and locked by the explicit sequence `T_k=2\pi k/\log8`.

## 5. The neighboring positive certificate is not imported as established evidence

The same Liu manuscript states a computer-assisted theorem at

\[
L=\frac{17}{16}=1.0625>\frac{\log8}{2},
\]

namely

\[
Q(f)\ge2^{-49162}\|f\|_2^2
\qquad(f\in\mathcal D_{17/16}).
\tag{25}
\]

Its proof architecture deliberately retains all active prime powers `\{2,3,4,5,7,8\}` and a quantitative exterior Fourier-tail term, with a rank-two retained tail contribution and an exact finite Gram certificate. This is consistent with the obstruction: the no-go targets **tail dropping plus fixed compact repair**, not source-exact tail retention.

However, the public release explicitly states

`EXTERNAL_REPRODUCTION = NOT_YET_COMPLETED`.

The full frozen package is supplied for independent review, and the release documentation itself warns that archive/hash checks are not mathematical verification. Mathia therefore records (25) only as

`COMPUTATIONAL-CERTIFICATE + NEEDS-INDEPENDENT-REPLAY`.

It is not load-bearing for WI-360. The analytic obstruction (5)--(6) has been reconstructed directly from the submitted source and uses only Fubini, the explicit formula, a two-bump support calculation, Riemann--Lebesgue, and compactness on weakly-null sequences.

## 6. Boundary conditions and falsification

The no-go has several essential boundaries.

First, it begins only for

\[
L>\frac{\log8}{2}.
\]

The witness requires the two bumps separated by `\log8` to fit strictly inside the support window. No claim is made at the endpoint.

Second, the correction is required to be **fixed and compact**. Equation (6) explicitly leaves open noncompact corrections and `k`-dependent or source-adapted compensation whose high-frequency quadratic value stays positive.

Third, the obstruction concerns the comparison `\mathcal D_\chi`, not the full Weil form. Equation (13) contains a nonnegative remainder `\mathcal S_\chi`, and discarding precisely that information is what the witness exploits.

Fourth, `g` is an adversarial legal smooth test, not an asserted Suzuki first-crossing eigenfunction. A successful RH argument may use structural restrictions of an actual ground/null state to exclude this geometry.

The proof is falsified only if one of the following exact steps fails:

1. the localization identity (12) is inconsistent with the classical explicit-formula normalization;
2. the two-bump support fails to isolate `\log8` from every other active integer logarithm;
3. the phase choice (18) does not preserve the `8`-channel;
4. the continuous defect fails the Riemann--Lebesgue limit;
5. `R_1-(1/16)I` or a proposed repair `K_c` is not compact, so the weak-null limit cannot be used.

All five checks are explicit in the source and were independently reconstructed in this audit. None depends on the manuscript's large interval certificate.

## 7. Prior art and novelty audit

Primary source:

- Vincent Liu, **Certified Weil Positivity Beyond the Unit Window: Source-Exact Block-Schur and Tail-Compensation Bounds for the Riemann Zeta Function**, manuscript dated 14 September 2026, public frozen source repository `luciferyu666/certified-weil-positivity`, commit `b6cd2183c1e79c6c27a34267812a7b2d73ed1b59`. The Obstruction Theorem supplies (5)--(6); Theorem B supplies the separate `17/16` computational candidate discussed above.

The repository release is a journal submission package, not a peer-reviewed publication, and explicitly reports no completed external reproduction. That evidence boundary is preserved here.

The local `weil_inertia` corpus was searched for `log8`, `prime-power eight`, and `Vincent Liu`; no prior finding or source anchor contained this obstruction. The nearest internal results are WI-248's uniform prime-symbol recurrence barrier, WI-355--WI-359's localized first-crossing/threshold program, and the exact source-specific multiplier constraints of WI-258 and WI-269.

No priority is claimed for the obstruction: it is Liu's theorem. Mathia's contribution is the independent reconstruction, the separation of its analytic content from the unreproduced numerical certificate, and the programmatic consequence that **fixed compact repair of a tail-dropped localization is not a viable cofinal RH mechanism past the first relevant larger prime-power threshold.**

## Research consequence

The current source-side frontier should not spend further effort trying to make a tail-dropped unit-window localization cofinal by adding a fixed compact correction. The obstruction is exact and already appears at `L>\log8/2`.

The surviving direction is aligned with the current mandate and WI-359: preserve the actual arithmetic/frequency structure. A useful next theorem must exploit the full source-exact tail, the first-crossing null equation, or another noncompact coercive invariant whose reserve cannot disappear on high-frequency coherent two-bump states. This is a restriction of method, not progress toward a density-only surrogate for RH.