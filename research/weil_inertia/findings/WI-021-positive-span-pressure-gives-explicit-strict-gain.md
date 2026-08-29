# WI-021 — positive span pressure gives an explicit strict gain beyond the WI-011 envelope bound

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED`. This is an unconditional refinement of WI-011 using only the same Lean-proved four-point certificate, the same Montgomery--Taylor Gram kernel, and the exact trace--energy envelope already audited in WI-011/WI-020. No new prime-side moment, no new computer-assisted gap certificate, and no support beyond one is introduced. The durable new point is that the pressure-transfer step in WI-011 cannot actually attain equality on a Montgomery--Taylor gap block: a short-span/positive-pressure dichotomy gives an explicit uniform slack.

## 1. Statement

Retain the notation of WI-011 with

\[
m=438,
\qquad
A=\frac{20097}{20000},
\qquad
p=\frac1{2500},
\]

and

\[
\Phi_m(E)=
\begin{cases}
E,&0\le E\le m/(m-1),\\[1mm]
2\sqrt{\frac{m-1}{m}E}-1+\frac Em,&E\ge m/(m-1).
\end{cases}
\]

For a limiting Montgomery--Taylor Gram block of `m` consecutive simple critical zeros let

\[
E=\operatorname{tr}(G-I)^2,
\qquad
D=\operatorname{tr}\Psi(G),
\]

and let `P` be the sum of the nonnegative span-pressure terms obtained by summing the Lean-proved four-point inequality over the `m-3` consecutive four-point windows. WI-011 gives

\[
E+P\ge A,
\qquad
D+P\ge\Phi_m(A).
\]

The second inequality is not sharp on this geometric class. In fact one has the explicit strengthening

\[
\boxed{
D+P\ge\Phi_{438}(A)+\delta_0,
\qquad
\delta_0:=\frac{49}{250000000}=1.96\times10^{-7}.
}
\tag{1}
\]

Consequently the WI-011 global assembly improves to

\[
\boxed{
\liminf_{T\to\infty}\frac{N_0^s(T,2T)}{N(T,2T)}
\ge
\frac{
438H_{\rm MT}-261/500
}{
438-\Phi_{438}(20097/20000)-49/250000000
}.
}
\tag{2}
\]

A high-precision non-load-bearing evaluation of (2) is

\[
0.6728525642585670387\ldots,
\]

compared with WI-011's

\[
0.6728525639567808470\ldots.
\]

Thus the certified proportion increases by about `3.02e-10`. The numerical size is tiny; the structural point is that the exact envelope value used by WI-011 is provably unattainable by the actual pressure-carrying Montgomery--Taylor blocks.

## 2. Exact pressure ledger

Write the normalized consecutive gaps as

\[
g_i=y_{i+1}-y_i\ge0,
\qquad 1\le i\le m-1,
\]

and let

\[
Y:=y_m-y_1=\sum_{i=1}^{m-1}g_i
\]

be the block span. The four-point certificate has pressure `p` times each three-gap span, hence after summing the `m-3` internal windows

\[
P
=p\sum_{i=1}^{m-3}(g_i+g_{i+1}+g_{i+2}).
\]

Every gap occurs at least once, so exactly

\[
\boxed{P\ge pY.}
\tag{3}
\]

This elementary inequality is the extra geometric information not used by the scalar implication

\[
E+P\ge A\Longrightarrow D+P\ge\Phi_m(A).
\]

## 3. Short spans have far too much Gram energy

For the Montgomery--Taylor window

\[
v(t)=\cos(\sqrt2\,t),
\qquad |t|\le\frac12,
\]

the normalized on-line overlap kernel is

\[
k_{\rm MT}(x)
=
\frac{
\int_{-1/2}^{1/2}v(t)\cos(2\pi xt)\,dt
}{
\int_{-1/2}^{1/2}v(t)\,dt
},
\qquad
w(x)=k_{\rm MT}(x)^2.
\tag{4}
\]

The weight `v` is positive. If

\[
0\le x\le\frac{49}{100}<\frac12,
\]

then `|2 pi x t| <= pi x < pi/2`, so monotonicity of cosine gives

\[
k_{\rm MT}(x)
\ge
\cos(\pi x)
\ge
\cos\frac{49\pi}{100}
=
\sin\frac{\pi}{100}.
\]

The elementary concavity bound `sin u >= 2u/pi` on `[0,pi/2]` yields

\[
\boxed{k_{\rm MT}(x)\ge\frac1{50},
\qquad
w(x)\ge\frac1{2500}.}
\tag{5}
\]

Therefore, if `Y <= 49/100`, every pair distance in the block lies in this interval and

\[
E
=2\sum_{1\le i<j\le m}w(y_j-y_i)
\ge
\frac{m(m-1)}{2500}
=
\frac{95703}{1250}.
\tag{6}
\]

This is enormously larger than `A`. In particular the exact WI-020 envelope gives

\[
D+P\ge\Phi_m(E)>A.
\tag{7}
\]

For later comparison note that, with

\[
r_A^2:=\frac{m-1}{m}A
=\frac{2927463}{2920000},
\]

one has the exact rational check

\[
r_A^2-\left(\frac{1001}{1000}\right)^2
=\frac{20251}{36500000}>0.
\]

Hence

\[
A-\Phi_m(A)=(r_A-1)^2>10^{-6}>\delta_0.
\tag{8}
\]

Combining (7)--(8), every block of span at most `49/100` satisfies (1) with room to spare.

## 4. Longer spans force enough pressure to make the 1-Lipschitz step strictly costly

Now suppose

\[
Y\ge\frac{49}{100}.
\]

By (3),

\[
P\ge P_0:=\frac1{2500}\frac{49}{100}
=\frac{49}{250000}.
\tag{9}
\]

The four-point certificate still gives `E+P >= A`, while WI-020 gives `D >= Phi_m(E)`. If `P>=A`, then trivially

\[
D+P\ge A>\Phi_m(A)+\delta_0
\]

by (8). Assume therefore `P<A`. Monotonicity of `Phi_m` gives

\[
D+P
\ge
\Phi_m(A-P)+P.
\tag{10}
\]

Define

\[
f(P):=\Phi_m(A-P)+P,
\qquad 0\le P\le A.
\]

On the linear branch of `Phi_m`, `f` is constant; on the square-root branch,

\[
f'(P)=1-\Phi_m'(A-P)\ge0.
\]

Thus `f` is nondecreasing, so (9)--(10) reduce the problem to `P=P_0`.

Put

\[
E_0:=A-P_0=\frac{502327}{500000}.
\]

This remains above the kink `m/(m-1)=438/437`. On the square-root branch

\[
1-\Phi_m'(E)
=1-\frac1m-\sqrt{\frac{m-1}{mE}}.
\tag{11}
\]

At `E=E_0`, the exact comparison

\[
\left(1-\frac1{438}-\frac1{1000}\right)^2
-
\frac{437}{438E_0}
=
\frac{8421106974247}{24092105247000000}>0
\tag{12}
\]

shows

\[
1-\Phi_m'(E_0)>\frac1{1000}.
\]

The left side of (11) increases with `E`, hence throughout `[E_0,A]`

\[
1-\Phi_m'(E)>\frac1{1000}.
\]

Integrating exactly over an interval of length `P_0` gives

\[
\begin{aligned}
f(P_0)-\Phi_m(A)
&=P_0-\bigl(\Phi_m(A)-\Phi_m(E_0)\bigr)\\
&=\int_{E_0}^{A}\bigl(1-\Phi_m'(E)\bigr)\,dE\\
&>\frac{P_0}{1000}
=\boxed{\frac{49}{250000000}}
=\delta_0.
\end{aligned}
\tag{13}
\]

This proves (1) also for every block of span at least `49/100`.

## 5. Global assembly

WI-011 averages the `m` shifted block partitions and obtains

\[
\mathcal D(M^\circ)
\ge
\frac{\Phi_m(A)}mS
-
\frac{m-3}{m}\frac3{2500}N
-o(N).
\]

Equation (1) upgrades each full block by the same fixed `delta_0`, so the identical pinching and shift-averaging argument gives

\[
\boxed{
\mathcal D(M^\circ)
\ge
\frac{\Phi_m(A)+\delta_0}{m}S
-
\frac{m-3}{m}\frac3{2500}N
-o(N).
}
\tag{14}
\]

The finite-`T` issue is harmless. In the long-span case pressure itself already supplies the lower bound. In the short-span case all relevant configurations lie in a fixed compact span interval, exactly the regime where the Montgomery--Taylor Gram asymptotic used by WI-009/WI-011 is uniform. The strict margin `delta_0` therefore survives as `delta_0-o(1)` per fixed-size block.

Substituting (14) into the stability bridge

\[
S\ge H_{\rm MT}N+\mathcal D(M^\circ)-o(N)
\]

and solving for `S/N` gives (2).

## 6. Why this is not an improvement of the abstract trace--energy envelope

WI-020 proves that `Phi_m` is the exact optimal scalar function of the energy `E` for arbitrary unit-diagonal PSD Gram matrices. Nothing here contradicts that result.

The gain comes from retaining one additional piece of information that the scalar envelope discards:

\[
\boxed{
\text{the certificate pressure is the span of the same ordered point configuration that generates the Gram matrix.}
}
\]

For an arbitrary abstract pair `(E,P)` with `E+P=A`, the 1-Lipschitz transfer can approach the WI-011 value. For an actual Montgomery--Taylor block, making `P` very small collapses all points into a short interval, which forces the Gram energy to be huge by (5)--(6). Conversely, once the span is macroscopic, (3) forces a definite positive `P`, and the derivative of `Phi_m` is strictly below one at the operating energy. The two equality mechanisms are incompatible.

This is therefore a small concrete example of the broader principle suggested by WI-012/WI-020: additional realizability information about the ordered Gram geometry can produce a strict gain even after the scalar spectral inequality itself is optimal.

## 7. Prior-art and novelty audit

The ingredients are not new individually:

- the Montgomery--Taylor window/kernel and four-point stability framework are the sources already recorded in `SOURCES.md`;
- the four-point inequality used here is the existing `teal-sea/zeta-lab` Lean theorem imported by WI-009/WI-011;
- the trace--energy envelope and pressure assembly are prior art from `tawanerguo-cn/zeta-simple-zeros` and the independent `trmdy/zeta-simple-zeros-673137` re-derivation;
- the elementary cosine and concavity estimates in (5) are classical.

A targeted search for the exact strengthened constant, the rational slack `49/250000000`, or an explicit short-span/strict-pressure refinement of the WI-011 four-point splice found no matching public statement. Absence of a search hit is not a priority claim.

Recent public candidates give substantially larger numbers (`0.6733...` and Devine's claimed `0.673399`), but those depend on new external interval certificates and/or multiple profiles and remain at the evidence levels recorded in `SOURCES.md`. The point of (2) is different: it raises the strongest bound in this line obtained from the already Lean-proved local certificate plus exact finite-dimensional deductions, without importing a new computational certificate.

## 8. Boundaries and falsification tests

- The improvement is intentionally tiny. It does **not** challenge WI-019's interval-certified `0.67361` obstruction for the collapsed single-profile MT interface.
- The proof uses the actual Montgomery--Taylor kernel through (4)--(6); it is not a window-independent statement.
- The pressure ledger must be the same three-gap pressure appearing in the Lean-proved four-point certificate. Replacing it by a weaker bookkeeping variable would invalidate (3).
- A clean formalization target is to add the two-case lemma (5)--(13) to the existing `zeta-lab` four-point bridge and replace `Phi_m(A)` by `Phi_m(A)+delta_0` at `m=438`.

The decisive finite checks are exact rational comparisons (8) and (12); no floating-point inequality is load-bearing.

## 9. Consequence for `weil_inertia`

WI-011 showed that better global assembly recovers slack without new arithmetic. WI-020 then proved that the scalar energy-to-defect envelope itself is optimal. The present result isolates the next layer of recoverable information: **the span pressure and the Gram energy cannot independently sit at their abstract equality values.**

Even the crude threshold `49/100` yields a certified strict gain. A worthwhile next optimization is therefore not to sharpen `Phi_m(E)` again, but to solve or lower-bound the joint finite-dimensional functional

\[
\inf_{g_1,\ldots,g_{m-1}\ge0}
\left\{
\mathcal D(G_{\rm MT}(g))+P(g)
\right\}
\]

subject to the same four-point certificate. Any rigorous improvement of the crude two-case split above feeds directly into (14), still within Fourier support one.