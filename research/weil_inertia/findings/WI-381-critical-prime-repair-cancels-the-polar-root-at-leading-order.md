# WI-381 — Critical-prime repair cancels the polar root at leading order

**Status:** `EXACT-DERIVED + CLASSICAL-PNT + PRIMARY-SOURCE-OPERATOR-AUDIT + DECISIVE-ROUTE-REDIRECTION + PRIOR-ART-AUDITED + NON-ESTABLISHED-RH`.

## Claim

WI-380 localizes every favorable inherited arithmetic contribution on its fixed-width source-zero gamma-negative trials to the critical shift window

\[
\log n=A_k+O(1),
\qquad
A_k=\log(k+1).
\]

The gross critical-annulus mass is indeed large: on the WI-380 trials it is positive of order `\sqrt{k}` and therefore, considered in isolation, overwhelms any fixed gamma tariff. But this is not usable free repair. In the exact Desogus rooted operator the polar rank-one term has an equal and opposite `\sqrt{k}` main term.

More precisely, put

\[
x_k=e^{A_k}=k+1.
\]

For the WI-380 trial `f_k`, let `Q_k^{\rm crit}` be the arithmetic quadratic-form contribution from the cross-lobe critical window and `Q_k^{\rm pol}` the exact polar contribution. Then

\[
\boxed{
 x_k^{-1/2}
 \left(Q_k^{\rm crit}+Q_k^{\rm pol}\right)
 \longrightarrow0.
}
\tag{1}
\]

The cancellation can be sharpened to an exact reduction. If

\[
E(u):=\psi(u)-u
\]

is the Chebyshev error and `w_k` is the compactly supported weight defined below, then

\[
\boxed{
Q_k^{\rm crit}+Q_k^{\rm pol}
=
4I_{k,+}I_{k,-}
-2x_k^{-1/2}I_{k,-}^2
+2\int w_k(u)\,dE(u).
}
\tag{2}
\]

The remaining same-lobe arithmetic is only `O_L(1)`. Consequently, after the leading critical-prime/polar cancellation, the unresolved arithmetic datum on these trials is a **fixed-log-width smoothed Chebyshev-error functional**, not the gross Mangoldt mass in the critical annulus.

This materially redirects the live WI-380 question. Estimating only the positive critical-annulus mass cannot prove repair of the gamma-negative band because its leading term is already committed to the polar debt. A successful continuation must control the renormalized remainder in (2), exploit an additional exact rooted identity, or exclude the WI-380 trials by domain/graph compatibility.

## 1. Primary-source normalization

The operator input is the exact localized odd model in Marco Desogus, *The Three Gates: A Rooted-Operator Approach to Weil Positivity*, arXiv:2609.20367v1 (17 September 2026). After the unitary rescaling to `(-1,1)`, its arithmetic part is

\[
-
\sum_{2\le n<e^{2a}}
\frac{\Lambda(n)}{\sqrt n}
\left(S_{r_n}+S_{r_n}^*\right),
\qquad
r_n=\frac{\log n}{a},
\tag{3}
\]

and its polar term is

\[
-2|s_a\rangle\langle s_a|.
\tag{4}
\]

In physical log coordinates the polar profile is

\[
s^{\rm ph}(y)=\sinh(y/2).
\tag{5}
\]

The physical Mellin support relation is `Y=e^{2a}`. In the present target-cell normalization `a=A_k=\log(k+1)`, so the exact arithmetic cutoff is `n<x_k^2`. Every critical shift `n=x_ke^{O(1)}` considered below lies below that cutoff for all sufficiently large `k`.

No Riemann-hypothesis conclusion from the Desogus preprint is used here. Only the displayed operator identities and normalizations are used as primary-source input.

## 2. Centering the WI-380 trial

Fix a depth `0\le\eta<C_\Gamma` and the corresponding finite width `L=L_\eta` from WI-380. Its positive half-line trial `F_k` is supported in

\[
I_k=
\left[
\frac{A_k-L}{2},
\frac{A_k+L}{2}
\right].
\]

Center the positive lobe by

\[
p_k(s):=F_k(A_k/2+s),
\qquad |s|\le L/2.
\tag{6}
\]

The unperforated normalized first Dirichlet mode becomes the fixed profile

\[
g(s)=
\sqrt{\frac2L}
\cos\!\left(\frac{\pi s}{L}\right),
\qquad |s|\le L/2.
\tag{7}
\]

The WI-380 construction has `F_k=\chi_kG_k`, `0\le F_k\le G_k`, and

\[
\|F_k\|_2^2=(1-o(1))\|G_k\|_2^2.
\]

Because `\chi_k` is an indicator,

\[
(G_k-F_k)^2\le G_k^2-F_k^2
\]

pointwise. Hence

\[
\boxed{\|p_k-g\|_2\to0.}
\tag{8}
\]

Define the ordinary convolution

\[
q_k(t):=(p_k*p_k)(t).
\tag{9}
\]

Young's inequality gives the uniform convergence

\[
\|q_k-g*g\|_\infty
\le
\|p_k-g\|_2
\left(\|p_k\|_2+\|g\|_2\right)
\longrightarrow0.
\tag{10}
\]

For the odd extension `f_k` from WI-380, a cross-lobe shift `h=A_k+t`, `|t|\le L`, gives exactly

\[
\boxed{
C_k(A_k+t)
:=\int f_k(x+A_k+t)f_k(x)\,dx
=-q_k(t).
}
\tag{11}
\]

This identity does not require `p_k` to be even. It follows directly by writing the negative lobe as the odd reflection of the positive one.

For reference, the limiting convolution `q=g*g` is explicit. For `0\le t\le L`,

\[
q(t)=
\left(1-\frac tL\right)
\cos\!\left(\frac{\pi t}{L}\right)
+
\frac1\pi
\sin\!\left(\frac{\pi t}{L}\right).
\tag{12}
\]

Writing `u=t/L`,

\[
\frac{dq}{du}=\pi(u-1)\sin(\pi u)\le0
\qquad(0\le u\le1).
\]

Thus, for example,

\[
q(t)\ge q(L/2)=\frac1\pi
\qquad (|t|\le L/2).
\tag{13}
\]

Together with (10), this already shows that a fixed subannulus contributes `\gg\sqrt{x_k}` favorable arithmetic by the prime number theorem. The next sections show why that gross lower bound is not the relevant quantity.

## 3. Exact critical arithmetic term

The quadratic form of one arithmetic branch in physical coordinates is

\[
-2\frac{\Lambda(n)}{\sqrt n}C_k(\log n).
\]

By the support/sign geometry of WI-380 and (11), the favorable cross-lobe contribution is therefore exactly

\[
\boxed{
Q_k^{\rm crit}
=
2\sum_n
\frac{\Lambda(n)}{\sqrt n}
q_k\!\left(\log\frac n{x_k}\right),
}
\tag{14}
\]

where `q_k` is supported on `[-L,L]`. For large `k`, every integer in this fixed logarithmic annulus lies below `x_k^2`, so (14) uses only branches actually present in the exact localized operator.

The only unfavorable same-lobe arithmetic shifts satisfy `0<\log n<L`. Since `L` is fixed, these involve only the fixed finite set `n<e^L`. Their total contribution `Q_k^{\rm small}` is therefore

\[
Q_k^{\rm small}=O_L(1),
\qquad
Q_k^{\rm small}\le0.
\tag{15}
\]

There are no arithmetic contributions from the middle shift region because the autocorrelation there vanishes exactly.

## 4. Weighted PNT and the `\sqrt{x_k}` main term

A standard Stieltjes-summation consequence of the classical prime number theorem `\psi(u)\sim u` is that for every fixed continuous compactly supported `\phi`,

\[
x^{-1/2}
\sum_n
\frac{\Lambda(n)}{\sqrt n}
\phi\!\left(\log\frac nx\right)
\longrightarrow
\int_{\mathbb R}e^{t/2}\phi(t)\,dt.
\tag{16}
\]

Although `q_k` varies with `k`, (10) upgrades (16) to this family: the support is the same fixed compact interval and the uniform difference is `o(1)`, while the total weighted Mangoldt mass in the annulus is `O(\sqrt{x_k})` by PNT.

Now define

\[
I_{k,+}:=\int e^{s/2}p_k(s)\,ds,
\qquad
I_{k,-}:=\int e^{-s/2}p_k(s)\,ds.
\tag{17}
\]

Fubini gives the exact factorization

\[
\int e^{t/2}q_k(t)\,dt
=
\left(\int e^{s/2}p_k(s)\,ds\right)^2
=I_{k,+}^2.
\tag{18}
\]

By (8), `I_{k,+}\to I_+>0`. Consequently (14)--(18) give

\[
\boxed{
x_k^{-1/2}Q_k^{\rm crit}\longrightarrow2I_+^2.}
\tag{19}
\]

In particular, the favorable critical arithmetic is genuinely `+\Theta(\sqrt{k})`; the issue is not a shortage of prime mass.

## 5. The polar root has the opposite main term

Using the exact physical polar profile (5) and oddness of `f_k`,

\[
\begin{aligned}
\langle s^{\rm ph},f_k\rangle
&=
2\int_0^{A_k}\sinh(y/2)F_k(y)\,dy\\
&=
x_k^{1/4}I_{k,+}-x_k^{-1/4}I_{k,-}.
\end{aligned}
\tag{20}
\]

Therefore the exact polar quadratic-form contribution is

\[
\boxed{
Q_k^{\rm pol}
=-2
\left(
 x_k^{1/4}I_{k,+}
 -x_k^{-1/4}I_{k,-}
\right)^2.
}
\tag{21}
\]

Expanding,

\[
Q_k^{\rm pol}
=
-2x_k^{1/2}I_{k,+}^2
+4I_{k,+}I_{k,-}
-2x_k^{-1/2}I_{k,-}^2.
\tag{22}
\]

Thus

\[
x_k^{-1/2}Q_k^{\rm pol}\longrightarrow-2I_+^2,
\tag{23}
\]

and (19) plus (23) proves the leading cancellation (1).

This cancellation is structural: the same exponential weight `e^{s/2}` that appears in the PNT density after the change of variables `n=x_ke^t` is the weight selected by the polar profile `\sinh(y/2)` on a lobe centered at `A_k/2`.

## 6. Exact reduction to a smoothed Chebyshev error

The leading asymptotic can be sharpened without approximation. Let

\[
E(u):=\psi(u)-u,
\qquad
w_k(u):=
 u^{-1/2}
 q_k\!\left(\log\frac u{x_k}\right).
\tag{24}
\]

Stieltjes summation rewrites (14) as

\[
Q_k^{\rm crit}
=2\int w_k(u)\,d\psi(u)
=2\int w_k(u)\,du
 +2\int w_k(u)\,dE(u).
\tag{25}
\]

With `u=x_ke^t`, the Lebesgue main term is exactly

\[
2\int w_k(u)\,du
=2x_k^{1/2}
\int e^{t/2}q_k(t)\,dt
=2x_k^{1/2}I_{k,+}^2.
\tag{26}
\]

Combining (22), (25), and (26) yields the exact identity

\[
\boxed{
Q_k^{\rm crit}+Q_k^{\rm pol}
=
4I_{k,+}I_{k,-}
-2x_k^{-1/2}I_{k,-}^2
+2\int w_k(u)\,d(\psi(u)-u).
}
\tag{27}
\]

Including (15), the full arithmetic-plus-polar layer on the WI-380 trials is

\[
\boxed{
Q_k^{\rm arith}+Q_k^{\rm pol}
=
Q_k^{\rm small}
+4I_{k,+}I_{k,-}
-2x_k^{-1/2}I_{k,-}^2
+2\int w_k(u)\,d(\psi(u)-u).
}
\tag{28}
\]

All deterministic terms in (28) other than the final Stieltjes error functional are `O_L(1)`. Thus the unresolved arithmetic question has been compressed to one precise object:

\[
\boxed{
\mathcal E_k
:=2\int w_k(u)\,d(\psi(u)-u).
}
\tag{29}
\]

Classical PNT proves only `\mathcal E_k=o(\sqrt{x_k})`, which is exactly what is needed for (1), but it does not determine the fixed-scale sign or magnitude required to decide whether the rooted form repairs the fixed gamma defect. Standard unconditional PNT error estimates do not, merely by insertion, provide a uniform `O(1)` estimate for (29) on these moving fixed-log-width weights. This is an information barrier for this reduction, not a claim that `\mathcal E_k` is unbounded.

## 7. Consequences for the research line

WI-380 asked whether exact inherited arithmetic could meet the fixed gamma tariff on the source-zero negative band. The present calculation resolves the **leading-order** version of that question and rules out one tempting shortcut.

The favorable critical-annulus term cannot be compared directly with the fixed `O(1)` gamma tariff while omitting the polar rank-one term: both critical arithmetic and polar debt are `\Theta(\sqrt{k})`, and their main coefficients cancel exactly. The correct object is the renormalized remainder (28), whose genuinely arithmetic part is (29).

This does **not** prove that the full rooted form remains negative, nor that it becomes positive, on the WI-380 trials. It instead identifies the missing information sharply. A continuation must do at least one of the following: obtain a sign/coercive estimate for (29) strong enough at fixed scale; expose a further exact rooted identity that cancels or controls (29); or prove that the source-zero gamma-negative trials are excluded by the actual graph/domain conditions before this quadratic-form comparison becomes relevant.

The result also keeps the bookkeeping requested by the line mandate explicit: the gamma-negative core, direct critical arithmetic repair, the polar rank-one debt, and source/domain constraints remain separate mechanisms. No component is silently reclassified as a population of off-critical zeta zeros.

## 8. Prior-art and provenance audit

- **Primary operator source:** Marco Desogus, *The Three Gates: A Rooted-Operator Approach to Weil Positivity*, arXiv:2609.20367v1, 17 September 2026. Equations used here are the localized arithmetic translations, polar rank-one term, physical polar profile, and the relation between physical and normalized support. The paper is a fresh unrefereed RH-claim preprint; none of its RH conclusions are imported as established evidence.
- **Classical input:** the only asymptotic arithmetic theorem used in (16)--(19) is the prime number theorem `\psi(x)\sim x`, plus elementary Stieltjes summation. The exact identity (27) itself does not require an asymptotic theorem.
- **Nearby qualitative prior art:** recent exploratory notes around the same rooted-operator program discuss a qualitative/numerical "just-in-time" or completion-critical prime rescue. That is treated as prior art for the qualitative criticality mechanism, not as evidence for the exact cancellation (27).
- **Novelty posture:** the exact centered-trial cancellation and reduction to (29) were not found as a stated result in the audited local or external sources. This is recorded only as an audit outcome, not as a priority claim.
- **Relation to Mathia:** WI-379 established that inherited translations cannot be removed by source-rank counting; WI-380 localized favorable arithmetic on the chosen gamma-negative source-zero trial to critical shifts. WI-381 computes that critical layer together with the polar root and shows why gross critical mass is not the deciding invariant.

## 9. Falsification and next test

The derivation is falsified if any of the following normalization identities fails in the exact localized operator used by the line: the arithmetic branch coefficient in (3), the physical polar coefficient `-2`, the profile `s^{\rm ph}(y)=\sinh(y/2)`, or the target-cell identification `a=A_k`. Those items were rechecked against the primary source and the preceding normalization findings before persistence.

Within those conventions, equations (11), (18), (20), and (27) are algebraic identities. The only asymptotic step is the classical PNT passage to (19).

The next high-value audit is therefore **not** a larger lower bound for raw critical-annulus Mangoldt mass. It is a rigorous estimate or structural identity for the smoothed Chebyshev-error functional (29) on the WI-380 family, together with the bounded deterministic terms in (28). If that route cannot beat the fixed gamma tariff, the alternative live route is to show that graph/domain compatibility excludes these centered source-zero trials.