# WI-198 — Karatsuba forces a critical-line reservoir inside long bows

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + STRUCTURAL-RIGIDITY + PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE`.

The live `weil_inertia` frontier WI-183--WI-197 treats the Maynard--Pratt bow as a source-compatible sparse obstruction that may require a distinguished-height prime covariance estimate. There is a classical zero-distribution input that sharply reduces the exponent range where that source problem is actually needed. Karatsuba proved that, for every fixed `eta>0`, every sufficiently high interval of length

\[
L=S^{27/82+\eta}
\]

contains `\gg_\eta L\log S` odd-order zeros of `zeta(1/2+it)`. Combining this **every-interval** theorem with the exact mirror/count bookkeeping of WI-184 gives the following consequence.

Let a source-compatible Maynard--Pratt bow at height `T` have

\[
m=T^\theta,
\qquad 0<\theta<\frac12,
\]

right-half bow labels, ordinate step `c_T/\log T` with `c_T\asymp1`, and hence vertical span

\[
H_{\rm bow}
=\left(c_T+o(1)\right)\frac{m}{\log T}.
\]

Assume, as in the displayed Maynard--Pratt bow and WI-184, that all but `O(1)` selected right-half labels are genuinely off the critical line, and include their compulsory same-ordinate functional-equation mirrors. If

\[
\boxed{\theta>\frac{27}{82}},
\]

then the bow interval necessarily contains

\[
\boxed{\gg_{\theta} m}
\]

odd-order critical-line zeros. Apart from the `O(1)` selected endpoint labels that may themselves lie on the line, these are a **complementary critical-line population**. In the WI-184 notation for the excess local zero-count budget,

\[
\boxed{E_I\gg_\theta m.}
\]

Consequently a mirror-closed bow with exponent `theta>27/82` cannot be count-saturating in the sense `E_I=o(m)`. In particular the `c_T=4\pi+o(1)` count-saturating bow that drives WI-188--WI-197 is impossible throughout that exponent range.

No simple-critical-zero proportion changes here and RH is not proved. The theorem does not rule out shorter bows, nor does it rule out longer bows accompanied by a positive-density local reservoir. Its durable effect is to identify part of that reservoir unconditionally: above `27/82`, it must contain linearly many odd-order critical-line zeros. Thus the distinguished source-covariance problem remains necessary for the count-saturating bow only in the fixed-power range `0<theta<=27/82`, with the endpoint unresolved by this argument.

## 1. Primary-source theorem: every interval above the Karatsuba exponent contains many critical-line zeros

A. A. Karatsuba, **On the zeros of the function zeta(s) on short intervals of the critical line**, *Mathematics of the USSR-Izvestiya* 24:3 (1985), 523--537, DOI `10.1070/IM1985v024n03ABEH001246` (Russian original: *Izv. Akad. Nauk SSSR Ser. Mat.* 48:3 (1984), 569--584), proves the following theorem. For every fixed `eta>0` there exist `c_eta>0` and `S_0(eta)` such that, for `S>=S_0(eta)` and

\[
L=S^{27/82+\eta},
\]

one has

\[
\boxed{
N_{0,\mathrm{odd}}(S+L)-N_{0,\mathrm{odd}}(S)
\ge c_\eta L\log S.
}
\tag{1}
\]

Here `N_{0,odd}(S)` counts odd-order zeros of `zeta(1/2+it)` with ordinate in `(0,S)`. MathNet's record for the English translation states exactly this theorem and its quantifiers. A later survey-level paper by Do Duc Tam, *Chebyshevskii Sbornik* 17:1 (2016), 71--89, explicitly contrasts this Karatsuba result on **every** interval `[S,S+S^{27/82+eta}]` with the much shorter later results that hold only for almost all intervals.

The exponent is

\[
\frac{27}{82}
=\frac13-\frac1{246}
=0.329268\ldots .
\tag{2}
\]

Nothing below needs this exponent to be best possible. The argument uses only the established theorem (1). Later improvements or alternative every-interval theorems with a smaller exponent would strengthen the cutoff automatically.

Odd-order critical-line zeros are sufficient for the present count argument. Even if `N_{0,odd}` counts zero locations rather than their full multiplicities, each such location contributes at least one zero label to the ordinary Riemann--von Mangoldt count.

## 2. Exact bow length and mirror population

Maynard--Pratt Section 8 gives the schematic bow

\[
\gamma_j=T_0+\frac{cj}{\log T},
\qquad 1\le j\le T^\theta,
\qquad T_0\asymp T,
\tag{3}
\]

with real parts rising from `1/2` to `3/4`, staying at `3/4`, and returning to `1/2`. Their displayed equation (22) has only `O(1)` selected labels on the critical line; all other selected right-half labels satisfy `beta_j>1/2`.

WI-184 imposes the actual-zeta symmetry that the one-sided schematic model suppresses. Every off-line right-half zero `rho=beta+i gamma` forces the distinct same-ordinate zero

\[
1-\overline\rho=(1-\beta)+i\gamma.
\]

Thus `m=T^theta` selected right-half bow labels contribute the mirror-closed baseline

\[
B_I=2m+O(1)
\tag{4}
\]

zero labels in the same vertical interval. If the ordinate step is `c_T/\log T`, with `c_T\asymp1`, the span is

\[
H_{\rm bow}
=\frac{c_T(m-1)}{\log T}
=\left(c_T+o(1)\right)\frac{T^\theta}{\log T}.
\tag{5}
\]

The Riemann--von Mangoldt calculation in WI-184 gives

\[
N_I
=\left(\frac{c_T}{2\pi}+o(1)\right)m
\tag{6}
\]

when `c_T` tends to a fixed positive scale. Hence source compatibility requires `c_T>=4\pi-o(1)`. If the bow plus mirrors accounts for all but `o(m)` of the local zero count, then

\[
E_I:=N_I-B_I=o(m)
\tag{7}
\]

and necessarily `c_T=4\pi+o(1)`.

The new argument below does not initially assume (7). It first shows that every bow with `theta>27/82` and bounded positive spacing scale has `E_I\gg m` because of critical-line zeros. Count saturation is then an immediate contradiction.

## 3. Pack the bow interval by Karatsuba intervals

Fix

\[
\theta>\frac{27}{82}.
\]

Choose a fixed `eta>0` such that

\[
a:=\frac{27}{82}+\eta<\theta.
\tag{8}
\]

If desired one may take `eta<10^{-3}` as well; the primary theorem itself is stated for arbitrary positive `eta`.

Because `theta<1/2`, equation (5) gives `H_bow=o(T)`. Therefore every base point `S` inside the bow interval satisfies

\[
S\asymp T,
\qquad
S^a=T^{a+o(1)},
\qquad
\log S=(1+o(1))\log T.
\tag{9}
\]

Starting at the lower endpoint of the bow, construct successive half-open intervals

\[
I_j=(S_j,S_{j+1}],
\qquad
S_{j+1}=S_j+S_j^a,
\tag{10}
\]

for as long as `I_j` remains inside the bow interval. They are disjoint, and each is exactly of the form to which (1) applies. Since

\[
\frac{H_{\rm bow}}{T^a}
\asymp
\frac{T^{\theta-a}}{\log T}
\longrightarrow\infty,
\tag{11}
\]

the uncovered remainder has length `O(T^a)=o(H_bow)` and the number `J` of complete intervals satisfies

\[
J=(1+o(1))\frac{H_{\rm bow}}{T^a}.
\tag{12}
\]

Apply Karatsuba to every `I_j` and sum. Disjointness prevents double counting, while (9) makes all logarithms and powers uniform. Hence

\[
\begin{aligned}
N_{0,\mathrm{odd}}(I_{\rm bow})
&\ge
\sum_{j=1}^{J}
\left(
N_{0,\mathrm{odd}}(S_{j+1})
-N_{0,\mathrm{odd}}(S_j)
\right)\\
&\ge
c_\eta\sum_{j=1}^{J}S_j^a\log S_j\\
&\gg_\eta J T^a\log T\\
&\asymp H_{\rm bow}\log T\\
&\asymp c_T T^\theta.
\end{aligned}
\tag{13}
\]

Since `c_T\asymp1`, this is

\[
\boxed{N_{0,\mathrm{odd}}(I_{\rm bow})\gg_\eta m.}
\tag{14}
\]

The logarithm in Karatsuba's lower bound is load-bearing here: it exactly compensates the `1/\log T` in the physical bow height. A single Karatsuba interval would contribute only `T^a\log T=o(m)`; the contradiction appears only after packing the entire bow span.

## 4. These critical-line zeros are a forced complementary population

All but `O(1)` selected right-half bow labels are off the line, and their compulsory mirrors are off the line as well. Thus the mirror-closed selected bow contains only `O(1)` critical-line zero locations. Equation (14) therefore forces at least

\[
\gg_\eta m-O(1)=\gg_\eta m
\tag{15}
\]

additional critical-line zero locations in the same interval.

Each contributes at least one unit to the ordinary local zero count `N_I`, so WI-184's excess budget satisfies

\[
\boxed{E_I\gg_\eta m.}
\tag{16}
\]

This conclusion is independent of what else the excess contains. There may also be multiplicity at bow points, further off-line pairs, or additional critical-line zeros. Equation (16) identifies a compulsory positive-density component: odd-order critical-line zeros.

If the bow were count-saturating, WI-184 gives `E_I=o(m)`. Equations (16) and (7) are incompatible. Therefore

\[
\boxed{
\theta>\frac{27}{82}
\quad\Longrightarrow\quad
\text{no count-saturating mirror-closed Maynard--Pratt bow.}
}
\tag{17}
\]

The contradiction does not depend on a numerical lower bound for Karatsuba's constant `c_eta`; any fixed positive constant suffices against `o(m)`.

## 5. Boundary cases and falsification controls

Several restrictions are essential.

First, the endpoint `theta=27/82` is **not** excluded. The bow height there is only

\[
H_{\rm bow}\asymp\frac{T^{27/82}}{\log T},
\]

which is shorter than `T^{27/82+eta}` for every fixed `eta>0`. No endpoint claim is imported by taking `eta` to zero after `T`.

Second, a bow with fixed spacing `c>4\pi` already has a positive-density excess budget by WI-184. Karatsuba does not rule such a bow out; it says that, when `theta>27/82`, a positive-density part of the local reservoir must consist of odd-order critical-line zeros. This is a structural classification of the complement, not a contradiction unless one also assumes count saturation or another upper bound on the reservoir.

Third, the almost-all short-interval theorems of Karatsuba and later authors are not used. The argument requires the **every-interval** theorem (1), because the bow location is source-selected. This avoids exactly the exceptional-set problem isolated for other arithmetic inputs in WI-190 and WI-196.

Fourth, the theorem says nothing about simple critical-line zeros specifically. An odd-order zero may have multiplicity greater than one. That distinction is harmless for (16), which needs only extra critical-line zero mass, but it must not be promoted to a simple-zero proportion.

Finally, this is not a proof that no off-critical bow-like geometry can occur. It eliminates only the long, locally count-saturating realization that had been used as the hardest sparse cancellation model. Shorter bows and bows embedded in a substantial reservoir remain admissible targets.

## 6. Prior-art audit and research redirection

The primary sources checked for this deduction are:

- James Maynard and Kyle Pratt, **Half-Isolated Zeros and Zero-Density Estimates**, *International Mathematics Research Notices* 2024:19 (2024), 12978--13014, DOI `10.1093/imrn/rnae191`, arXiv:2206.11729v2, Section 8 and equation (22): source for the `T^theta` bow and its role as a zero-detection obstruction.
- A. A. Karatsuba, **On the zeros of the function zeta(s) on short intervals of the critical line**, *Math. USSR-Izv.* 24:3 (1985), 523--537, DOI `10.1070/IM1985v024n03ABEH001246`: source for (1), including the `27/82+eta` exponent, the `H log T` lower bound, odd-order critical-line zeros, and the every-interval quantifier.
- Do Duc Tam, **On the zeros of the Riemann zeta function, lying in almost all short intervals of the critical line**, *Chebyshevskii Sbornik* 17:1 (2016), 71--89: secondary confirmation that Karatsuba's `27/82+eta` theorem is the every-interval result, distinct from later almost-all shorter-interval statements.
- WI-184: line-local exact functional-equation mirror and Riemann--von Mangoldt bookkeeping that turns a one-sided schematic bow into an actual-zeta local count problem.

A bounded search around Maynard--Pratt bows, Karatsuba's short-interval critical-line theorem, and the exponent `27/82` did not locate this particular combination. That absence is not evidence of priority and no priority claim is made. The new durable content is the exact packing implication (13)--(17) for the already-defined `weil_inertia` adversarial geometry.

This materially narrows several recent route analyses. WI-190's almost-all alias-locus dichotomy changes at `theta=1/3`, but

\[
\frac{27}{82}
=\frac13-\frac1{246}<\frac13.
\tag{18}
\]

Hence the whole `theta>1/3` regime in which the deterministic stationary alias locus could hide inside a published almost-all exceptional set is already impossible for a **count-saturating** bow by the stronger every-interval zero theorem. The difficult source-fixed covariance remains relevant only below that cutoff.

Combining (17) with the scale barrier of WI-193 also gives a useful map of the remaining power range. An ideal fixed-shift square-root estimate assembled absolutely would be exponent-sufficient for `theta>1/4`, while it is information-theoretically insufficient below `1/4`. Therefore the unresolved count-saturating bow regime separates into

\[
0<\theta<\frac14
\]

where cross-shift cancellation is structurally necessary for that architecture, and the narrow intermediate range

\[
\frac14<\theta\le\frac{27}{82}
\]

where a genuine uniform square-root fixed-shift theorem would already be scale-sufficient, though no such theorem is supplied here. The endpoints retain the logarithmic/rate caveats of WI-193 and the Karatsuba endpoint caveat above.

## Research consequence

The bow program should no longer spend arithmetic effort on count-saturating exponents above `27/82`. Classical critical-line occupancy already forbids those configurations after the functional-equation mirror count is imposed. The live RH-facing problem is smaller and sharper: exclude count-saturating bows at exponent at most `27/82`, or prove that any shorter exceptional geometry must still carry a source-controlled critical-line/off-line/multiplicity reservoir that prevents negative inertia from surviving.

For any future proposed bow countermodel, the first gate should therefore be local critical-line occupancy before the BGSTB prime covariance is opened. If its vertical span contains many Karatsuba-scale subintervals while its selected off-line labels already consume `1-o(1)` of the Riemann--von Mangoldt count, the model is internally inconsistent and should be killed at the zero-count level rather than sent through the more expensive source analysis.