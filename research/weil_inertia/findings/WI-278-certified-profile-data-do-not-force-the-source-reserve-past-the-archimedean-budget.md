# WI-278 — certified scalar profile data do not force the first-crossing reserves past the archimedean budget

## Status

- **Evidence:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PROFILE-COUNTERMODEL + LITERATURE+DERIVED + PRIOR-ART-AUDITED`.
- **Scope:** logical barrier for the accepted first-crossing clue after `WI-275`--`WI-277`. It constructs an explicit scalar lowest-eigenvalue profile compatible with the presently used unconditional profile constraints, including Suzuki's small-aperture asymptotic and the certified compact-window data through `a=0.8`, while keeping both the harmonic and every commensurate multishift Toeplitz reserve below the positive archimedean budget.
- **What it does not claim:** the constructed profile is not asserted to be the actual zeta localized-Weil eigenvalue curve, nor to be realized by any self-adjoint Weil operator or null mode. It does not prove prime screening for the actual source, say anything decisive about the sign-changing null-mode branch, or contradict the certified compact-window calculations. Its purpose is to falsify deductions that use only the scalar profile information listed below together with the reserve inequalities already proved in this line.

## Claim

Let `lambda_a` denote the unrestricted bottom eigenvalue of Suzuki's localized Weil form. The presently established scalar information used by the first-crossing program includes:

1. `lambda_a` is continuous and nonincreasing under enlargement of the window;
2. as `a -> 0+`,

\[
\lambda_a
=
\log\frac1a+c+O(a),
\qquad
c=\mu_1-\log(2\pi)-\gamma,
\tag{1}
\]

where `mu_1>0` is the bottom eigenvalue of Suzuki's scaled logarithmic form;
3. the compact-window certification at `a=0.8` gives, for the unrestricted problem,

\[
8.9\times10^{-18}
\le \lambda_{0.8}
\le 2.27\times10^{-17},
\tag{2}
\]

and certified variational upper bounds are available at the larger tabulated apertures.

There exists a continuous strictly decreasing profile

\[
\widetilde\lambda:(0,1]\to[0,\infty)
\]

with `widetilde lambda(1)=0` and `widetilde lambda(a)>0` for `a<1`, satisfying (1) with the actual constant `c`, satisfying (2), and lying below every published compact-window variational upper bound at the tabulated apertures, yet

\[
\boxed{
R_{\rm multi}(1)<\frac1{20}<K_+
}
\tag{3}
\]

for **every** commensurate nonnegative Toeplitz combination from `WI-277`, and

\[
\boxed{
R_{\rm harm}(1)<2\times10^{-9}<\frac1{20}<K_+.
}
\tag{4}
\]

Consequently the currently available scalar information on `a -> lambda_a`, even when fed into the sharp mass-only reserve of `WI-275` and all fixed commensurate support-only reserves of `WI-277`, does **not** force the budget crossing needed to obtain unscreenable prime overlap on the one-signed branch.

Any successful continuation of this route must use information not encoded by those scalar constraints: for example the exact Suzuki null/source equation, the PSD signed-source multiplier family, actual null-mode shape or nodal information, a genuinely source-specific noncommensurate compatibility relation, or the archimedean sign geometry.

## 1. An exact usable range for Suzuki's small-aperture constant

Suzuki writes the scaled logarithmic form as

\[
\mathcal L(w)
=
\frac14\iint_{-1}^{1}
\frac{|w(x)-w(y)|^2}{|x-y|}\,dx\,dy
-
\frac12\int_{-1}^{1}|w(x)|^2\log(1-x^2)\,dx,
\tag{5}
\]

with `mu_1` its bottom eigenvalue. The published theorem gives `mu_1>0` and (1).

For the explicit admissible trial function

\[
w(x)=1-x^2,
\]

one obtains exactly

\[
\|w\|_2^2=\frac{16}{15},
\qquad
\frac14\iint
\frac{|w(x)-w(y)|^2}{|x-y|}\,dx\,dy
=\frac4{15},
\tag{6}
\]

and

\[
\int_{-1}^{1}(1-x^2)^2\log(1-x^2)\,dx
=-\frac{376}{225}+\frac{32}{15}\log2.
\tag{7}
\]

Therefore the Rayleigh quotient gives

\[
0<\mu_1\le\frac{31}{30}-\log2.
\tag{8}
\]

Hence

\[
-\log(2\pi)-\gamma<c
\le
\frac{31}{30}-\log(4\pi)-\gamma.
\tag{9}
\]

This elementary enclosure is enough for the whole counterprofile; no numerical value of `mu_1` is needed.

Put

\[
\delta=\frac1{20},
\qquad
L_\delta:=\log20+c.
\tag{10}
\]

Then

\[
\boxed{\frac12<L_\delta<1.}
\tag{11}
\]

For the lower bound, (9), `pi<22/7`, and `gamma<3/5` give

\[
L_\delta>
\log\frac{10}{\pi}-\gamma
>
\log\frac{35}{11}-\frac35
>
\frac12.
\]

For the last step it is enough to note `e^(11/10)<35/11`. For the upper bound, (9) gives

\[
L_\delta
\le\frac{31}{30}+\log\frac5\pi-\gamma.
\]

Using `gamma>1/2` and

\[
e^{7/15}>
1+\frac7{15}+\frac12\left(\frac7{15}\right)^2
+\frac16\left(\frac7{15}\right)^3
=\frac{16124}{10125}
>\frac{250}{157}
>\frac5\pi,
\]

where `pi>157/50`, yields `log(5/pi)<7/15` and hence `L_delta<1`.

## 2. Explicit first-crossing profile compatible with the certified data

Let

\[
\varepsilon=10^{-17},
\qquad
M=\frac43\log\frac{L_\delta}{\varepsilon}.
\tag{12}
\]

Because `L_delta>1/2`, elementary rational bounds on `e` give

\[
\boxed{M>48.}
\tag{13}
\]

For example `log 10>9/4`, so `log(L_delta/epsilon)>16 log10>36`.

Define

\[
\widetilde\lambda(r)=
\begin{cases}
\log(1/r)+c,
&0<r\le1/20,\\[1mm]
L_\delta e^{-M(r-1/20)},
&1/20\le r\le4/5,\\[1mm]
10^{-17}e^{-170(r-4/5)},
&4/5\le r\le9/10,\\[1mm]
10\,10^{-17}e^{-17}(1-r),
&9/10\le r\le1.
\end{cases}
\tag{14}
\]

The pieces agree at the junctions. In particular, from the definition of `M`,

\[
L_\delta e^{-M(3/4)}=10^{-17}.
\]

The profile is continuous, strictly decreasing, positive on `(0,1)`, and vanishes exactly at `1`. On `(0,1/20]` it agrees **exactly** with the main term in Suzuki's asymptotic, so it satisfies (1) with remainder zero there. At the certified aperture,

\[
\widetilde\lambda(0.8)=10^{-17},
\]

which lies inside (2).

The remaining published variational upper bounds are also respected with large room. Using `log10<12/5` and `M>48`,

\[
\widetilde\lambda(0.5)<10^{-9},
\qquad
\widetilde\lambda(0.6)<10^{-11},
\qquad
\widetilde\lambda(0.7)<10^{-13},
\tag{15}
\]

while

\[
\widetilde\lambda(0.9)
=10^{-17}e^{-17}<10^{-24}.
\tag{16}
\]

These are respectively below the certified upper bounds `1.05e-6`, `1.82e-9`, `4.99e-13`, and `5.91e-23`; `widetilde lambda(1)=0` is below the `a=1` upper bound `8.08e-30`. Extending (14) beyond `1` by any continuous nonincreasing negative function, for example `-(r-1)`, automatically respects the positive variational upper bounds tabulated at larger apertures.

The compact-window paper separates parity for the lower certification at `0.8`: the even sector has the tiny positive lower bound and the odd sector a stronger positive lower bound, so the unrestricted bottom is positive there. Its even trial vectors give valid upper bounds for the unrestricted infimum as well. Thus the comparison above does not confuse a restricted even eigenvalue with the unrestricted one.

## 3. Every commensurate multishift reserve stays below `1/20`

For the `WI-277` reserve, fix any base radius `r`, any active multiples `kr<1`, and nonnegative weights `alpha_k`. Recall

\[
R_\alpha
=
\frac{\sum_k\alpha_k\,kr\,\widetilde\lambda(kr)}
{\sum_k\alpha_k+\rho_N(\alpha)}.
\tag{17}
\]

The symmetric matrix `H_N(alpha)` has trace zero, so its largest eigenvalue satisfies

\[
\rho_N(\alpha)\ge0.
\]

Therefore

\[
R_\alpha
\le
\sup_{0<x<1}x\widetilde\lambda(x).
\tag{18}
\]

On the small-aperture branch,

\[
f(x)=x(\log(1/x)+c)
\]

is strictly concave and its unconstrained maximum is

\[
f(e^{c-1})=e^{c-1}.
\]

From (9) and `gamma>1/2`,

\[
e^{c-1}
\le\frac{e^{-7/15}}{4\pi}
<\frac1{20},
\tag{19}
\]

where the final inequality is equivalent to the already proved `e^(7/15)>5/pi`. In particular the critical point lies below `delta`, and the first branch never reaches `1/20`.

On the exponential branch `[delta,0.8]`,

\[
\frac d{dx}igl(x\widetilde\lambda(x)\bigr)
=\widetilde\lambda(x)(1-Mx)<0
\]

because `M>48` and `x>=1/20`. Its left endpoint is

\[
\delta L_\delta<\frac1{20}.
\]

The same derivative test is immediate on `[0.8,0.9]`, and `x(1-x)` is decreasing on `[0.9,1]`. Hence

\[
\boxed{
\sup_{0<x<1}x\widetilde\lambda(x)<\frac1{20}.
}
\tag{20}
\]

Equations (18)--(20) prove the first half of (3), simultaneously for **all** nonnegative commensurate weight vectors. Thus optimizing the finite Toeplitz denominator cannot rescue this scalar profile.

## 4. The harmonic reserve is even smaller

At `a=1`, `WI-275` gives

\[
R_{\rm harm}(1)
=4\int_0^{1/2}
\frac{\widetilde\lambda(r)\widetilde\lambda(1-r)}
{\widetilde\lambda(r)+\widetilde\lambda(1-r)}\,dr.
\tag{21}
\]

Since `AB/(A+B)<=B` for `A,B>=0`,

\[
R_{\rm harm}(1)
\le4\int_{1/2}^{1}\widetilde\lambda(s)\,ds
\le2\widetilde\lambda(1/2).
\tag{22}
\]

By `L_delta<1` and `M>48`,

\[
\widetilde\lambda(1/2)
<e^{-48(9/20)}
=e^{-108/5}
<10^{-9},
\tag{23}
\]

because `log10<12/5`. Hence

\[
\boxed{R_{\rm harm}(1)<2\times10^{-9}.}
\tag{24}
\]

## 5. The positive archimedean budget is rigorously larger than `1/20`

For the one-signed branch, `WI-274` uses

\[
K_+
=\int_0^{h_0}h\,w(h)\,dh,
\qquad
w(h)=\frac{e^{-5h/2}}{1-e^{-2h}}-e^{h/2},
\tag{25}
\]

where `h_0=log rho` and `rho` is the positive real root of

\[
\rho^3-\rho-1=0.
\]

The root satisfies `rho>13/10`, while the elementary enclosure `e<68/25` implies `e^(1/4)<13/10`; hence

\[
h_0>\frac14.
\tag{26}
\]

On `[0,1/4]`, use `1-e^{-2h}<=2h`. Then

\[
hw(h)
\ge
\frac12e^{-5h/2}-he^{h/2}.
\]

Therefore

\[
K_+
>
\frac15(1-e^{-5/8})-4+\frac72e^{1/8}.
\tag{27}
\]

The Taylor bounds

\[
e^{5/8}>\frac{233}{128},
\qquad
e^{1/8}>\frac{145}{128}
\]

give

\[
\boxed{
K_+>
\frac{3279}{59648}
>\frac1{20}.
}
\tag{28}
\]

Combining (20), (24), and (28) proves (3)--(4).

## 6. What this barrier closes

The accepted clue after `WI-277` proposed an exact fork: either prove that known information about the true spectral profile forces

\[
\max\{R_{\rm harm},R_{\rm multi}\}>K_+,
\]

or construct an admissible profile satisfying every currently proved scalar constraint while keeping both reserves below the budget. The profile (14) supplies the second outcome.

The obstruction is deliberately stronger than testing only the `N=3` ratio from `WI-277`. Equation (20) dominates the numerator of every nonnegative commensurate Toeplitz optimization, irrespective of `N` or the weights. Thus no further rearrangement of the same scalar `lambda_r` data inside the `WI-277` support-only family can force the crossing.

This does **not** show that the actual Suzuki profile has such a sharp descent between small aperture and `0.8`. It shows that the presently established scalar theorems do not forbid it. To rule the profile out one must prove genuinely new information, such as a quantitative differential/Harnack-type restriction on `lambda_r`, or use data that remember the null eigenfunction and source rather than only its lowest eigenvalue.

For the one-signed branch, the next mathematically distinct target is therefore source/eigenfunction coupling. For the unrestricted problem the sign-changing branch remains a separate obstacle, as already emphasized by `WI-268` and the later signed-source findings.

## 7. Prior art and provenance

The source-specific ingredients are established prior art:

- Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (2026), https://arxiv.org/abs/2606.09096. The paper constructs the localized self-adjoint operator, defines the attained lowest eigenvalue, proves continuity in the aperture, and proves the small-aperture expansion (1) with the logarithmic-form constant `mu_1>0`.
- Marcus Chuk, **Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau--Widom decay law**, arXiv:2608.24827v2 (2026), https://arxiv.org/abs/2608.24827. The paper supplies the certified positivity/two-sided enclosure at `a=0.8` and unconditional variational upper certificates at the larger tabulated apertures. Only those unconditional finite-window statements are used here; the RH-conditional large-window asymptotics are not.

The variational trial (6)--(9), the explicit profile (14), and the reserve comparisons are Mathia deductions. A targeted prior-art audit around localized Weil first crossings, compact-window eigenvalue profiles, harmonic/minimax reserves, and truncated-Toeplitz multishift bounds located the two primary source surfaces and classical operator ingredients already recorded by `WI-275`--`WI-277`, but no source formulating this scalar-profile countermodel or the resulting reserve-budget barrier. Search absence is audit context only and is not a priority claim.

## Audit and falsification tests

The barrier is falsified if any load-bearing compatibility check fails. In particular, an audit should verify:

1. Suzuki's asymptotic constant and the trial-function quotient (6)--(9);
2. continuity and monotonicity of (14), including exact matching at `0.8` and `0.9`;
3. the interpretation of the compact-window parity bounds as lower/upper constraints on the unrestricted bottom eigenvalue;
4. every tabulated upper-bound comparison used in (15)--(16);
5. `rho_N(alpha)>=0` for the trace-zero symmetric Toeplitz matrix and the weighted-average reduction (18);
6. the exact `1/20` estimate (19)--(20);
7. the harmonic reduction (21)--(24);
8. the sign-change location and rational lower bound (26)--(28) for `K_+`.

A new theorem ruling out (14) through additional scalar regularity of the **actual** `lambda_a` would not invalidate this finding; it would add information outside the constraint set audited here and reopen the quantitative profile route on a stronger basis.

## Formalization disposition

The core countermodel is finite and elementary, but a useful end-to-end Lean target would have to formalize several transcendental enclosures together with the already external Suzuki/compact-window theorem interfaces. That would verify bookkeeping rather than expose a new structural interface. No automatic formalization handoff is opened from this finding.

## Consequence for the research line

The generic spectral-profile / mass-support branch of the accepted first-crossing clue is resolved negatively. The sharp reserve mechanisms `WI-275`--`WI-277` remain valid; what fails is the hope that the currently known scalar facts about `lambda_a` force them above the archimedean budget. Further optimization of the same scalar support-only quotient is now low value unless accompanied by a new theorem restricting the true eigenvalue curve.

The surviving route is source-specific: retain enough of Suzuki's exact arithmetic operator, null equation, signed-source multiplier structure, or null-mode geometry to rule out scalar profiles that are legal at the level of (1)--(2) but cannot arise from an actual first-crossing eigenfunction.