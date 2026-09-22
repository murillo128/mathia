# NB-278 — Finite differentiated Nyman sources have identically zero interior divisor current

**Date:** 2026-09-22  
**Status:** `EXACT-DERIVED + FINITE-TRUNCATION-NO-GO + DIVISOR-CURRENT-TOPOLOGY + HOLOMORPHIC-CLOSURE + SOURCE-TO-FORD-BRIDGE + NB-276/NB-277-COUPLING + PRIOR-ART-AUDITED`.

`NB-276` identifies the Ford logarithmic-derivative current as the singular Mellin derivative of the canonical reciprocal-zeta Nyman source. `NB-277` then removes the Abel parameter as a useful Ford-faithful regularizer and leaves one apparently discriminating question: can a **signed finite truncation** of the differentiated Möbius source reproduce the first-order Ford current while using Möbius cancellation to keep the Nyman cost controlled?

For the direct interior current topology used by the Ford `\bar\partial` representation, the answer is stronger than a norm lower bound: **no finite legal differentiated Nyman source carries any interior divisor current at all**.

Let

\[
\mathcal N[P](s)
:=
\frac{\zeta(s)}s\bigl(P(s)-P(1)\bigr)
\tag{1}
\]

be the canonical synthesis from `NB-276`, and let `P` be any finite Dirichlet polynomial, not necessarily Möbius. Define its differentiated synthesized current by

\[
\mathcal C_P(s)
:=-s\,\mathcal N[P'](s)
=-\zeta(s)\bigl(P'(s)-P'(1)\bigr).
\tag{2}
\]

Because `P'` is entire and the bracket in `(2)` vanishes at `s=1`, the pole of `\zeta` at `1` cancels. Hence

\[
\boxed{
\mathcal C_P\text{ is entire.}
}
\tag{3}
\]

Consequently, for every compactly supported smooth test `\Psi`,

\[
\boxed{
-\frac1\pi
\int_{\mathbb C}
\mathcal C_P(s)\,\bar\partial\Psi(s)\,dA(s)
=0.
}
\tag{4}
\]

By contrast, the limiting meromorphic current of `NB-276`,

\[
\mathcal C_0(s)
:=
\frac{\zeta'}{\zeta}(s)+\zeta(s),
\tag{5}
\]

is regular at the Euler pole but has residue `m(\rho)` at every zeta zero `\rho`. Therefore, whenever the support of `\Psi` avoids the Euler pole and its boundary contains no zero,

\[
\boxed{
-\frac1\pi
\int_{\mathbb C}
\mathcal C_0(s)\,\bar\partial\Psi(s)\,dA(s)
=
\sum_\rho m(\rho)\Psi(\rho),
}
\tag{6}
\]

with the sum over zeros in the support of `\Psi` (including trivial zeros if the support reaches them).

Equations `(4)` and `(6)` give an exact finite-truncation gap:

\[
\boxed{
-\frac1\pi
\int
\bigl(\mathcal C_0-\mathcal C_P\bigr)
\bar\partial\Psi\,dA
=
\sum_\rho m(\rho)\Psi(\rho).
}
\tag{7}
\]

The right-hand side is independent of the truncation length, the Möbius signs, the Abel weight, and the Hardy norm of the finite vector. Thus a finite linear Nyman synthesis cannot approximate a nonzero Ford divisor statistic in this interior-current pairing. The residue appears only after the singular infinite-source limit and meromorphic continuation identified in `NB-276`.

This closes the **direct finite-truncation route** left open by `NB-277`. It does not close every possible Ford-to-Nyman bridge: a boundary/contour representation, a test family whose boundary terms are retained, or a nonlinear operation that creates its own poles may still transfer arithmetic information. What is ruled out is the idea that signed cancellation in a finite differentiated Möbius sum can by itself make the legal finite linear current converge to the meromorphic zero divisor in the same `\bar\partial` topology.

## 1. Every finite differentiated canonical source is entire after the Euler anchor

Take an arbitrary finite Dirichlet polynomial

\[
P(s)=\sum_{k\le M}a_k k^{-s}.
\tag{8}
\]

Then

\[
P'(s)=-\sum_{k\le M}a_k(\log k)k^{-s}
\tag{9}
\]

is entire. The canonical differentiated synthesis is

\[
\mathcal N[P'](s)
=
\frac{\zeta(s)}s
\bigl(P'(s)-P'(1)\bigr).
\tag{10}
\]

Multiplying by `-s` gives `(2)`. Near `s=1`, Taylor expansion yields

\[
P'(s)-P'(1)
=(s-1)P''(1)+O((s-1)^2),
\tag{11}
\]

while

\[
\zeta(s)=\frac1{s-1}+O(1).
\tag{12}
\]

Therefore

\[
\mathcal C_P(s)
=-P''(1)+O(s-1)
\tag{13}
\]

near `1`. The only pole of `\zeta` is removable in `(2)`, and every other factor is entire. This proves `(3)`.

In particular, the exact family singled out by `NB-276`/`NB-277`,

\[
P_{\epsilon,M}(s)
=
\sum_{k\le M}\mu(k)k^{-\epsilon}k^{-s},
\tag{14}
\]

has

\[
\mathcal C_{\epsilon,M}(s)
=-\zeta(s)
\left(
P_{\epsilon,M}'(s)-P_{\epsilon,M}'(1)
\right)
\tag{15}
\]

entire for every finite `M` and every `\epsilon\ge0`. No special property of the Möbius coefficients is required for this statement.

The contrast with the infinite closed source is structural. For fixed `\epsilon>0`, first taking `M\to\infty` only in the Euler half-plane gives

\[
P_\epsilon(s)=\frac1{\zeta(s+\epsilon)}.
\tag{16}
\]

After **meromorphic continuation of this closed form**, the corresponding current acquires poles at shifted zeros `\rho-\epsilon`. Sending `\epsilon\downarrow0` then returns the zero divisor of `(5)`. The poles are therefore created by the infinite-limit/continuation step, not by any finite legal synthesized vector.

## 2. The interior `\bar\partial` current of every finite vector vanishes exactly

Normalize the Cauchy--Riemann distribution by

\[
\bar\partial\frac1{\pi(s-\rho)}=\delta_\rho.
\tag{17}
\]

For a locally integrable function `F`, define the tested current

\[
\mathfrak D_\Psi(F)
:=-\frac1\pi
\int_{\mathbb C}
F(s)\,\bar\partial\Psi(s)\,dA(s),
\qquad
\Psi\in C_c^\infty(\mathbb C).
\tag{18}
\]

If `F` is holomorphic on a neighborhood of `supp \Psi`, distributional integration by parts gives

\[
\mathfrak D_\Psi(F)=0.
\tag{19}
\]

Applying `(19)` to `(3)` proves `(4)` for every finite source.

For the meromorphic current `(5)`, the Euler pole cancels as in `NB-276`, while at a zero `\rho` of multiplicity `m(\rho)`,

\[
\mathcal C_0(s)
=
\frac{m(\rho)}{s-\rho}+O(1).
\tag{20}
\]

Hence

\[
\bar\partial\mathcal C_0
=
\pi\sum_\rho m(\rho)\delta_\rho
\tag{21}
\]

on any compact region avoiding unresolved boundary singularities, which yields `(6)`.

The same statement can be read without distribution notation. Choose `\Psi` equal to one near a single zero and supported in a disk containing no other zero and not containing `1`. Then the right-hand side of `(6)` is exactly the multiplicity of that zero, while `(4)` is exactly zero for every finite truncation. There is no asymptotic coefficient estimate left to optimize.

## 3. No distributional convergence across a zero is possible

The previous calculation gives a topology-level obstruction stronger than failure of local uniform convergence.

Let `U` be any open set containing at least one zeta zero and no Euler pole issue, and let `P_n` be any sequence of finite Dirichlet polynomials. Suppose, for contradiction, that

\[
\mathcal C_{P_n}
\longrightarrow
\mathcal C_0
\quad\text{in }\mathcal D'(U).
\tag{22}
\]

Distributional differentiation is continuous, so

\[
\bar\partial\mathcal C_{P_n}
\longrightarrow
\bar\partial\mathcal C_0.
\tag{23}
\]

But every term on the left is zero by holomorphy, whereas `(21)` is nonzero on `U`. Contradiction. Therefore

\[
\boxed{
\mathcal C_{P_n}\not\to\mathcal C_0
\text{ in distributions on any neighborhood containing a zeta zero.}
}
\tag{24}
\]

This does not depend on boundedness of the Nyman `H^2` norms. Even allowing those norms, coefficient norms, or pointwise amplitudes to diverge cannot turn a distributional limit of holomorphic currents into `(5)` across a zero. The obstruction is analytic, not energetic.

There is also no contradiction with approximation on zero-free compact sets. On a compact set disjoint from the divisor, `(5)` is holomorphic, and the finite source may approximate its closed form there by ordinary analytic methods. What fails is crossing the divisor while retaining the interior current.

This distinction sharpens the language in `NB-276`: the Ford bridge is not merely an unbounded operator on the Hardy space. At the divisor-current level it also changes analytic class after the infinite-source continuation.

## 4. Consequence for the signed finite Möbius truncation proposed in NB-277

The question left by `NB-277` was whether keeping the Möbius signs could improve the finite truncation enough to recover the first-order Ford current with controlled source cost. Equations `(4)`--`(7)` split that question into two logically different tasks.

Möbius cancellation can certainly improve approximation of

\[
P_*'(s)
=-\frac{\zeta'(s)}{\zeta(s)^2}
\tag{25}
\]

on the Euler half-plane or on zero-free regions where the reciprocal-zeta Dirichlet series is represented analytically. It can also reduce some physical norms of signed Nyman combinations relative to unsigned coefficient estimates. Those are legitimate finite-regularization gains.

But **none of them changes the interior divisor current of a finite linear synthesis**. For every `M`,

\[
\mathfrak D_\Psi(\mathcal C_{\epsilon,M})=0,
\tag{26}
\]

whereas the desired current gives `(6)`. Thus a tail estimate of the form

\[
P_{\epsilon,M}'\approx P_*'
\tag{27}
\]

on `\Re s>1` cannot, by itself, be continued through the zero divisor and inserted into the Ford `\bar\partial` representation. The missing step is not a sharper Mertens bound; it is the singular passage from holomorphic finite sources to a meromorphic divisor current.

This means the crude unsigned tail audit in `NB-276` and the Abel audit in `NB-277` were testing only the **Euler-half-plane ancestry**. They are not the decisive bottleneck for the direct interior-current representation. Even a hypothetical perfect cancellation estimate making `(27)` exponentially accurate to the right of `1` would leave `(26)` unchanged at finite `M`.

## 5. The Ford-scaled version is pointwise in the carrier parameter

The argument does not require a fixed physical neighborhood as the carrier `X` grows. Let `\Psi_X` be any smooth compactly supported Ford test at height/scale `X`, including translated and rescaled tests whose support moves with the zero window. For every finite source `P_X`, regardless of how its truncation length depends on `X`,

\[
\mathfrak D_{\Psi_X}(\mathcal C_{P_X})=0.
\tag{28}
\]

For the meromorphic current,

\[
\mathfrak D_{\Psi_X}(\mathcal C_0)
=
\sum_\rho m(\rho)\Psi_X(\rho).
\tag{29}
\]

Hence whenever the Ford statistic selected by `\Psi_X` is nonzero,

\[
\boxed{
\left|
\mathfrak D_{\Psi_X}
(\mathcal C_0-\mathcal C_{P_X})
\right|
=
\left|
\sum_\rho m(\rho)\Psi_X(\rho)
\right|.
}
\tag{30}
\]

There is no choice of `M(X)` that makes this error small by coefficient cancellation alone. The only way `(30)` can be small is if the **selected divisor statistic itself** is small because of the chosen test or the actual zero configuration.

This preserves the caveat used throughout the Ford findings: a matched compatibility packet is not an assertion that the actual zeta zeros occupy prescribed carrier-locked sites. The present statement is conditional only on whatever actual weighted divisor statistic the chosen test sees; it does not manufacture zeros.

## 6. What kind of bridge can still work

The no-go applies to a very specific architecture: finite legal Dirichlet source, linear canonical Nyman synthesis, Mellin differentiation, multiplication by `s`, and then the same compactly supported interior `\bar\partial` test used for the meromorphic Ford current.

Several genuinely different mechanisms remain possible.

A **boundary representation** may retain contour terms rather than convert them immediately into an interior `\bar\partial` current. Finite analytic functions can have large boundary traces even though their interior divisor current is zero, and a singular limit may concentrate through the boundary.

A **nonlinear operation** can change analytic class. For example, taking a logarithmic derivative of an analytic finite approximant creates poles at its own zeros. Such an object would no longer be the linear canonical Nyman synthesis classified here, and its norm/zero stability would have to be controlled separately.

A **moving or pinching contour** can also make the limit singular before the contour is collapsed to an interior current. Again, the boundary error is then part of the theorem and cannot be discarded as in `(19)`.

Finally, the Ford representation may remain useful as a dual diagnostic rather than as something approximated by legal finite Nyman vectors. That interpretation is fully consistent with `NB-275`, which showed that the direct resolved Ford channel is exponentially target-poor.

The next useful calculation should therefore not optimize the Möbius truncation length in `(14)` inside the same interior-current pairing. It should derive an exact **finite boundary/contour identity before the singular continuation step** and ask whether the boundary term admits a Hardy/Nyman estimate that survives the Ford scaling.

## 7. Adversarial audit

### 7.1 This is not a no-go for Nyman approximation

Finite Nyman combinations are supposed to approximate the analytic target `1/s`, not the meromorphic function `\zeta'/\zeta`. The fact that their differentiated synthesized currents have zero interior divisor current does not obstruct the Nyman criterion itself. It only closes the proposed direct linear route from those finite currents to the Ford zero divisor.

### 7.2 Large norms do not evade the distributional obstruction

It is tempting to think that an unbounded sequence of finite vectors could converge to a pole. Pointwise behavior can indeed blow up near the zero, but convergence in `\mathcal D'(U)` across the zero would still commute with `\bar\partial`. Since every finite term has zero `\bar\partial`, the limit would have zero `\bar\partial` as well. Thus `(24)` does not assume norm boundedness.

### 7.3 Zero-free approximation remains possible

Nothing prevents `\mathcal C_{P_M}` from approximating `\mathcal C_0` on compact subsets that avoid the zero divisor. The obstruction appears only when the topology is strong enough to retain the divisor current. This is exactly why the two-stage limit in `NB-276` is legal on `\Re s>1` and only becomes singular after continuation.

### 7.4 A vanishing weighted divisor statistic is not contradicted

If a particular complex Ford test has

\[
\sum_\rho m(\rho)\Psi_X(\rho)=0,
\]

then `(30)` gives zero for that test. The theorem is not a lower bound for every cutoff. It says that the finite current contributes **identically zero**, so any nonzero divisor statistic cannot be approximated by this route.

### 7.5 The Euler pole cancellation is essential

Without subtracting `P'(1)`, the factor `\zeta(s)P'(s)` would generally retain the pole at `1`, and the finite current would not be entire. The canonical Nyman anchor removes exactly that pole. This is why the statement applies cleanly to legal canonical finite vectors and is not merely a generic observation about multiplying by `\zeta`.

## 8. Prior-art boundary

The distributional fact used above is classical: holomorphic functions satisfy `\bar\partial F=0` in distributions, distributional differentiation is continuous, and therefore a distributional limit of holomorphic functions is holomorphic in the distributional sense. Likewise `\bar\partial(1/(\pi z))=\delta_0` is the standard Cauchy-kernel identity.

The Nyman ingredients are also classical individually. Báez-Duarte's Möbius-based criteria place finite Möbius sums inside the Nyman--Beurling approximation problem, and the Bagchi Hardy formulation uses the generators

\[
G_k(s)=\left(k^{-s}-k^{-1}\right)\frac{\zeta(s)}s.
\]

A fresh prior-art search found the expected literature on Möbius Nyman approximants and the general closure of holomorphic functions under analytic/distributional limits, but no source making the scale-local statement used here: **after canonical Euler anchoring, every finite differentiated Nyman source has exactly zero interior Ford divisor current, while the reciprocal-zeta limit acquires the full zero divisor only after the singular infinite-source continuation**.

No external theorem beyond standard complex/distribution theory is load-bearing; the proof is contained in `(2)`--`(24)`. No `SOURCES.md` update is required.

## Conclusion

`NB-277` left signed finite Möbius truncation as the remaining regularization mechanism inside the canonical ancestry of the differentiated reciprocal-zeta source. In the direct Ford `\bar\partial` topology, that route is now closed for a simpler reason than source norm growth.

Every finite canonical differentiated source produces an entire current after the Euler anchor, so its interior divisor current is **exactly zero**. The desired limit `\zeta'/\zeta+\zeta` has the full zeta zero divisor. Therefore no choice of finite truncation length, Möbius cancellation, Abel damping, or coefficient budget can make the finite linear current converge to the Ford divisor current on a neighborhood containing a zero.

The singularity identified in `NB-276` is thus not merely quantitative. It is topological/analytic: the zero residues are created only after the infinite reciprocal-zeta source is closed and meromorphically continued. The next viable bridge must keep a boundary term, introduce a nonlinear operation that can create poles, or otherwise avoid commuting the finite analytic limit with the interior `\bar\partial` current.