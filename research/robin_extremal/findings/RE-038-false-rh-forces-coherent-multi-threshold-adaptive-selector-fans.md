# RE-038 — false RH forces coherent multi-threshold adaptive selector fans

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + SAME-BLOCK-MULTI-THRESHOLD-SELECTION + MONOTONE-CONVEX-ENVELOPE + EXACT-BREAKPOINT-SECANTS + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-034`--`RE-037` fix one exponent `b` with `1-Theta<b<1/2` and show that hypothetical RH failure forces adaptive CA-selected states satisfying an increasingly rigid standard/reciprocal prime-race relation. The fixed-`b` formulation leaves a coherence question: Robin's quantitative false-RH theorem is available for every admissible exponent, but the previous reductions allowed the states selected for different `b` to be treated as unrelated sequences.

They need not be. Fix a compact interval

\[
J=[b_0,b_1]\Subset(1-\Theta,1/2).
\tag{1}
\]

If RH is false, there are infinitely many **single finite Robin-counterexample blocks** on which the adaptive amplitude of `RE-034` has a maximizer for every `b in J`, all inherited from one quantitative witness at the left endpoint `b_0`. Inside each such block the rightmost maximizer is a monotone step function of `b`; equivalently, the selected states are the exposed vertices of one finite upper convex envelope. If the selector switches from an exposed state `C` to a later exposed state `D`, the switching exponent is exactly

\[
\boxed{
\beta(C,D)
=
\frac{
\log(e^{h(C)}-1)-\log(e^{h(D)}-1)
}{
\log Y_D-\log Y_C
},
}
\tag{2}
\]

where `Y_C=log C` and `h(C)=log G(C)-gamma>0`. Thus every switch in `J` obeys the exact power law

\[
\boxed{
\frac{e^{h(D)}-1}{e^{h(C)}-1}
=
\left(\frac{Y_C}{Y_D}\right)^{\beta(C,D)}.
}
\tag{3}
\]

For a chain of exposed states selected as `b` increases across `J`, these secants telescope into a same-block cone: if `C_-` and `C_+` are the first and last distinct exposed states encountered, then

\[
\boxed{
\left(\frac{Y_-}{Y_+}\right)^{b_1}
\le
\frac{e^{h(C_+)}-1}{e^{h(C_-)}-1}
\le
\left(\frac{Y_-}{Y_+}\right)^{b_0}.
}
\tag{4}
\]

The main gain is not another one-parameter asymptotic. Hypothetical RH failure now supplies a **common block family carrying a whole ordered threshold fan**. The fixed-`b` finite spectral controls of `RE-033`--`RE-037` only show realizability one exponent at a time; they do not yet reproduce this blockwise cross-`b` coherence. Conversely, no simultaneous regularity theorem across a continuum of `b` is proved here, so one must not simply impose the `RE-037` prime-race normal form for all `b` on one block. That missing uniform bridge is now a precise part of the live obstruction.

## 1. One `b_0` witness makes the same block quantitative for all larger `b`

For a CA state `C` with positive Robin excess write

\[
Y_C:=\log C,
\qquad
h_C:=\log G(C)-\gamma>0,
\qquad
R_C:=e^{h_C}-1>0,
\tag{5}
\]

and retain the adaptive amplitude from `RE-034`,

\[
A_b(C):=Y_C^bR_C.
\tag{6}
\]

Robin's quantitative false-RH theorem gives a constant `c_0>0` and infinitely many CA states `N` satisfying

\[
A_{b_0}(N)\ge c_0.
\tag{7}
\]

As in `RE-034`, these witnesses lie in infinitely many finite CA counterexample blocks. Fix one such block `\mathcal B` and one witness `N in \mathcal B`. For every `b>=b_0`, the same state satisfies

\[
\boxed{
A_b(N)
=Y_N^{b-b_0}A_{b_0}(N)
\ge c_0Y_N^{b-b_0}.
}
\tag{8}
\]

Therefore, with

\[
M_{\mathcal B}(b)
:=\max_{C\in\mathcal B}A_b(C),
\tag{9}
\]

we have on the whole interval `J`

\[
\boxed{
M_{\mathcal B}(b)
\ge c_0Y_N^{b-b_0}.
}
\tag{10}
\]

This is the first coherence gain. No diagonal extraction over the continuum of exponents is needed to obtain quantitative blockwise maxima: one left-endpoint witness already makes its entire block quantitative for every larger exponent in `J`.

The statement is stronger than merely saying that Robin's theorem can be applied separately for each `b`. The block itself is fixed before `b` varies.

## 2. The adaptive maxima are one finite convex envelope

Define for `C in \mathcal B`

\[
x_C:=\log Y_C,
\qquad
y_C:=\log R_C.
\tag{11}
\]

Then

\[
\log A_b(C)=y_C+bx_C,
\tag{12}
\]

and hence

\[
\boxed{
m_{\mathcal B}(b)
:=\log M_{\mathcal B}(b)
=\max_{C\in\mathcal B}(y_C+bx_C).
}
\tag{13}
\]

Thus `m_B` is the upper envelope of finitely many affine functions. It is convex and piecewise affine. Let `C_B(b)` be the rightmost maximizer, using exactly the tie convention of `RE-034`. Since `C<D` implies `Y_C<Y_D` and therefore `x_C<x_D`, the standard monotone-argmax calculation gives

\[
\boxed{
b'<b''
\Longrightarrow
C_{\mathcal B}(b')
\le C_{\mathcal B}(b'').
}
\tag{14}
\]

Indeed, if `C_B(b')=D` and `C_B(b'')=C` with `D>C`, the two maximizing inequalities imply

\[
(y_D+b'x_D)-(y_C+b'x_C)\ge0,
\]

\[
(y_C+b''x_C)-(y_D+b''x_D)\ge0.
\]

Adding them gives `(b''-b')(x_C-x_D)>=0`, impossible because both factors have opposite signs. At a tie, the rightmost convention chooses the line with largest slope, so

\[
\boxed{
m'_{\mathcal B,+}(b)
=\log Y_{C_{\mathcal B}(b)}.
}
\tag{15}
\]

The selector is therefore an ordered step function, not a collection of independent maximizers. In convex-geometric terms, increasing `b` walks monotonically through the exposed vertices of the finite point set

\[
\{(\log Y_C,\log R_C):C\in\mathcal B\}.
\tag{16}
\]

The exact integral identity

\[
\boxed{
m_{\mathcal B}(b_1)-m_{\mathcal B}(b_0)
=
\int_{b_0}^{b_1}
\log Y_{C_{\mathcal B}(b)}\,db
}
\tag{17}
\]

is another way of recording the same fan. It requires no differentiability at the finitely many breakpoints.

## 3. Every switch obeys an exact Robin-height secant law

Suppose two consecutive exposed vertices of the envelope are `C<D`, and let `beta=beta(C,D)` be the unique exponent at which their affine scores tie. Then

\[
y_C+\beta x_C=y_D+\beta x_D.
\tag{18}
\]

Solving gives exactly

\[
\boxed{
\beta
=
\frac{y_C-y_D}{x_D-x_C}
=
\frac{
\log R_C-\log R_D
}{
\log Y_D-\log Y_C
},
}
\tag{19}
\]

which is (2), and exponentiating gives (3). Because the exposed slopes are encountered in increasing order, their switching exponents are nondecreasing.

For large positive CA states, `RE-034` proves

\[
h(C)\log Y_C\to0.
\tag{20}
\]

Hence `R_C=e^{h(C)}-1=h(C)(1+o(1))`, uniformly in the large positive regime. At a switch this yields the asymptotic height law

\[
\boxed{
\frac{h(D)}{h(C)}
=
\left(\frac{Y_C}{Y_D}\right)^\beta(1+o(1)).
}
\tag{21}
\]

No division by the possibly small spacing `log(Y_D/Y_C)` is used in (21); the exact statement remains (3).

Now take all distinct exposed states encountered while `b` runs through `J`, ordered as

\[
C_0<C_1<\cdots<C_k,
\tag{22}
\]

and let `beta_i in J` be the switch from `C_{i-1}` to `C_i`. Multiplying (3) over the chain gives

\[
\log\frac{R_{C_0}}{R_{C_k}}
=
\sum_{i=1}^k
\beta_i\log\frac{Y_{C_i}}{Y_{C_{i-1}}}.
\tag{23}
\]

Every logarithmic weight on the right is positive and every `beta_i` lies between `b_0` and `b_1`. Therefore

\[
b_0\log\frac{Y_{C_k}}{Y_{C_0}}
\le
\log\frac{R_{C_0}}{R_{C_k}}
\le
b_1\log\frac{Y_{C_k}}{Y_{C_0}},
\tag{24}
\]

which exponentiates to (4). If no switch occurs, the fan consists of a single state and (4) is vacuous; that possibility is explicitly allowed.

Equation (24) is a useful same-block restriction: whenever the adaptive maximizer moves right as the threshold exponent increases, its positive Robin excess must fall along an exact weighted power-law secant whose exponent never leaves the chosen admissible interval.

## 4. What can and cannot yet be transferred to `RE-037`

For any **fixed** `b in J`, the common blocks above are quantitative at that exponent by (10). Applying the fixed-`b` argument of `RE-034` to those maxima gives the same kind of unbounded regular adaptive subsequence used by `RE-034`--`RE-037`; on that subsequence the translated nonlinear prime-race condition of `RE-037` applies.

What is not proved is a single subsequence of blocks on which the adaptive maximizers are regular simultaneously for every `b in J`, or even for an arbitrarily large prescribed set of exponents. Tied/higher-layer CA transitions can obstruct the ordinary open supporting chamber, and the regular subsequence extracted for one exponent may depend on that exponent. The convex-envelope fan (13)--(24) itself does not remove this issue.

This distinction matters. It would be invalid to combine the fixed-`b` formula

\[
V(Z_b)-
\sqrt{Z_b}\log Z_b\,
\Psi_{b,\log Z_b}
\left(
\frac{U(Z_b)}{\sqrt{Z_b}\log Z_b}
\right)
=
\sqrt2\,\frac{2b-1}{b}+o_b(1)
\tag{25}
\]

for a continuum of `b` on one block without first proving a uniform regularity/selection theorem. `RE-038` therefore creates a sharper but honest next bridge: the amplitude selectors are already coupled on the same blocks, while the prime-race normal forms are still known only after fixed-parameter regular extraction.

A successful continuation could exploit this in either direction. One route is to prove that a positive-length subinterval of `J` must be carried by regular adaptive states on the same late blocks, after which the family (25) becomes genuinely simultaneous. Another is to show directly that the convex-envelope secant fan (19)--(24) is incompatible with the CA event geometry or with a source-specific constraint on how `h(C)` can decay inside one positive block. Both are stronger targets than another fixed-`b` sign condition.

## 5. Why the fixed-`b` finite-packet controls do not settle the fan

`RE-033`--`RE-037` deliberately stress-test the source-side implications against finite dominant packets of zeta-zero modes. Those controls are effective because for each fixed `b` the relevant linear ray, nonlinear curve, and finally the translated `o(1)` tube can all be hit in recurrent logarithmic phase windows.

The present condition is different. A matched control for the **full** false-RH implication would have to explain not only why each fixed `b` target is individually realizable, but how the corresponding arithmetic witnesses can be organized on the same finite counterexample blocks with the monotone ordering (14) and exact switch law (19). Independent phase choices for separate values of `b` do not establish that.

This does not prove that finite packets fail the stronger test. They may admit a coherent multi-parameter realization once the block variable is represented correctly. The point is narrower: the existing finite-packet falsification has exhausted the one-parameter obstruction, but it has not falsified the new same-block fan because that structure was absent from the previous target.

The fan also exposes a natural negative case. It is possible that one CA state maximizes `A_b` throughout all of `J`, in which case there are no secant switches to exploit. Any argument based on (19) must therefore either force selector motion or handle the robust single-state alternative separately. Recording this escape prevents the convex-envelope reformulation from being mistaken for an automatic strengthening to a contradiction.

## 6. Prior-art boundary and research consequence

The load-bearing external input is unchanged and already anchored in `SOURCES.md`: Robin supplies the quantitative false-RH excursions, and Alaoglu--Erdos supplies the CA framework underlying the adaptive construction. Mantovanelli, Zimov, Kalyabin, and the current joint prime-race literature bound the neighboring fixed-parameter CA and Mertens/Chebyshev mechanisms already used by `RE-034`--`RE-037`.

A targeted current search checked recent Robin/CA work on explicit counterexample windows, consecutive-CA transitions, Ramanujan/highest-abundant convex envelopes, and adaptive-looking threshold formulations. The located work still treats fixed Robin thresholds, different extremal envelopes, or one-step CA geometry. No source found in the audit couples Robin's whole admissible exponent interval through the specific scale-invariant amplitude `A_b(C)=Y_C^b(e^{h(C)}-1)` and extracts the same-block monotone fan and breakpoint law (19). No new theorem from that search is load-bearing here, so `SOURCES.md` does not need expansion.

The novelty claim is deliberately narrow. Convex envelopes and monotone argmax maps are elementary and not claimed as new mathematics in isolation. The line-specific delta is their splice to the adaptive Robin amplitude: **one quantitative `b_0` witness forces the same counterexample block to carry every larger threshold in a compact admissible interval, and the resulting threshold selectors are coupled by exact Robin-height secants.**

This finding does not prove RH, does not bound counterexample-block length, does not force the selector to move, and does not establish simultaneous regularity across `b`. It changes the live problem from unrelated fixed-parameter hits to a coherent blockwise family and isolates the next missing theorem: transfer enough of that family through the regular CA selector to make the prime-race constraints simultaneous, or show directly that the required same-block height fan cannot occur.