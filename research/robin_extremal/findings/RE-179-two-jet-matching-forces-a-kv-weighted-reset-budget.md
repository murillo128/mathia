# RE-179 — Two-jet matching forces a KV-weighted reset budget

**Status:** `EXACT-DERIVED + PRIME-SUPPORTED + TWO-JET-MATCHING + WEIGHTED-SIGN-RESET-COMPLEXITY + COUNTABLE-OSCILLATION + KV-TAIL-CAPACITY + ROBIN-SCALE-CONDITIONING + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-169, RE-173, RE-175, RE-176, RE-177, RE-178.

`RE-177` shows that a tail with `M` sign-constant phases can buy only `M` local resets of the Korobov--Vinogradov discrepancy envelope. Its theorem deliberately assumes a completed first positive phase before the remote cutoff and finite sign complexity. The surviving matched-control escape is therefore to begin alternating immediately after the selector packet, or to use infinitely many sign phases so that the raw count `M` is no longer useful.

The raw phase count is not the intrinsic quantity. Each sign reset occurring at prime scale `z` is worth only the local normalized KV allowance

\[
e^{-bV(z)},
\qquad
V(z):=\frac{(\log z)^{3/5}}{(\log\log z)^{1/5}}.
\]

Retain the canonical `RE-173` deletion packet

\[
D_p\subset[2p,3p],
\qquad
c_q=-1\quad(q\in D_p),
\]

with Mertens mass

\[
d_p:=\sum_{q\in D_p}H(q)
\asymp \frac1{\sqrt p\log p},
\qquad
H(q):=\log\frac q{q-1}.
\]

Fix `lambda>3`, and allow **all** other modifications to be arbitrary integer multiplicities on ordinary primes `q>=lambda p`; no clean first positive phase is assumed. Suppose the Mertens charge and first Euler boundary slope match exactly,

\[
D_Q(1+)=D_Q'(1+)=0,
\]

and the matched Chebyshev source obeys

\[
|\Delta\vartheta(x)|
:=|\vartheta_Q(x)-\vartheta(x)|
\le C_bxe^{-bV(x)}
\qquad(x\ge2p).
\]

For any cutoff `Y>=lambda p`, let `z_1,z_2,...` be the first modified primes of the maximal **negative** sign-phase fragments meeting `[Y,infinity)`. A phase already in progress at `Y` is truncated and its first modified prime at or after `Y` is used. Define the KV-weighted negative reset budget

\[
\mathcal R_b^-(Y)
:=\sum_j e^{-bV(z_j)}
\in[0,\infty].
\]

Let

\[
B(q):=\frac{\log q}{q-1},
\qquad
A(q):=\frac{B(q)}{H(q)},
\]

and let

\[
a_D:=\frac{\sum_{q\in D_p}B(q)}{d_p}.
\]

The centered first-slope kernel

\[
K_D(q):=B(q)-a_DH(q)=H(q)(A(q)-a_D)
\]

is positive throughout the repair region `q>=lambda p`. Put

\[
\delta_{\lambda,p}
:=\inf_{q\ge\lambda p}(A(q)-a_D)
\ge \log(\lambda/3)-o(1)>0
\]

and record how much required negative centered repair has already appeared before `Y`:

\[
\mathcal N_p^-(Y)
:=\sum_{\substack{\lambda p\le q<Y\\c_q<0}}
(-c_q)K_D(q).
\]

Then

\[
\boxed{
\bigl(\delta_{\lambda,p}d_p-\mathcal N_p^-(Y)\bigr)_+
\ll_b
\mathcal R_b^-(Y)
+\ell_{\rm KV}(Y)e^{-bV(Y)},
\qquad
\ell_{\rm KV}(Y):=\frac{\log Y}{V(Y)}.
}
\tag{1}
\]

This is the location-sensitive replacement for the raw `M` tariff. In particular, if less than half of the forced negative centered debt has been paid below `Y`, then

\[
\boxed{
\sqrt p\log p\,
\left[
\mathcal R_b^-(Y)
+\ell_{\rm KV}(Y)e^{-bV(Y)}
\right]
\gg_{b,\lambda}1.
}
\tag{2}
\]

Thus **infinitely many sign changes are not by themselves an escape**. They help only if their KV-weighted reset budget is large enough. A countably infinite sequence of increasingly remote alternations may have finite, even tiny, reset budget and is then controlled by the same two-jet debt. Conversely, if (2) fails, exact two-jet matching forces a fixed fraction of the negative repair workload to have occurred already below `Y`; the compensation is no longer genuinely remote.

For a finite tail with `M_-(Y)` negative sign phases, `\mathcal R_b^-(Y)<=M_-(Y)e^{-bV(Y)}`, so (2) recovers the leading `RE-177` count law without assuming that one clean positive phase has first been completed. The weighted form is strictly sharper when phase starts spread across different KV scales.

## 1. Two exact Euler coordinates force negative repair mass independently of phase order

The exact two-jet identities use the same notation as `RE-175`--`RE-177`. Separate the repair coefficients `q>=lambda p` into their positive and negative Jordan parts and define

\[
P_H:=\sum_{c_q>0}c_qH(q),
\qquad
N_H:=\sum_{c_q<0}(-c_q)H(q),
\]

and analogously

\[
P_B:=\sum_{c_q>0}c_qB(q),
\qquad
N_B:=\sum_{c_q<0}(-c_q)B(q).
\]

Whenever the reset budget below is finite these sums converge absolutely; if the reset budget is infinite, the final capacity inequality is vacuous and there is nothing to prove. Exact Mertens and first-slope matching give

\[
P_H-N_H=d_p,
\qquad
P_B-N_B=a_Dd_p.
\tag{3}
\]

Center at the actual deletion barycenter `a_D`. With

\[
P_K:=P_B-a_DP_H,
\qquad
N_K:=N_B-a_DN_H,
\]

(3) yields the exact identity

\[
\boxed{P_K=N_K.}
\tag{4}
\]

This removes the ordered-phase hypothesis of `RE-177`: it does not matter whether positive and negative repair coefficients are interlaced immediately after `lambda p`.

The elementary inequalities from `RE-175`,

\[
\log q<A(q)<\frac q{q-1}\log q,
\]

imply

\[
a_D\le(1+o(1))\log(3p),
\qquad
A(q)\ge\log(\lambda p)\quad(q\ge\lambda p).
\]

Hence `K_D(q)>=delta_{lambda,p}H(q)` on the entire repair support. Since (3) also gives `P_H=d_p+N_H>=d_p`,

\[
P_K
=\sum_{c_q>0}c_qK_D(q)
\ge\delta_{\lambda,p}P_H
\ge\delta_{\lambda,p}d_p.
\]

Using (4),

\[
\boxed{
\sum_{\substack{q\ge\lambda p\\c_q<0}}
(-c_q)K_D(q)
\ge\delta_{\lambda,p}d_p.
}
\tag{5}
\]

So two exact Euler coordinates force a Robin-scale amount of **negative centered repair** somewhere after the protected selector region, before any sign-phase decomposition is chosen.

Splitting (5) at an arbitrary `Y` gives

\[
\sum_{\substack{q\ge Y\\c_q<0}}
(-c_q)K_D(q)
\ge
\bigl(\delta_{\lambda,p}d_p-\mathcal N_p^-(Y)\bigr)_+.
\tag{6}
\]

Because `a_D>0`, on the repair support

\[
0<K_D(q)<B(q).
\tag{7}
\]

It remains only to bound the negative first-slope mass available beyond `Y` from the source envelope.

## 2. A sign reset has a local KV price, even for countably many phases

Take one maximal negative phase fragment beginning at a modified prime `z>=Y`. During this fragment define its increasing absolute Chebyshev mass

\[
M_z(x)
:=\sum_{\substack{z\le q\le x\\q\text{ in the fragment}}}
(-c_q)\log q.
\]

No positive coefficient occurs before the fragment ends, so

\[
M_z(x)
=\Delta\vartheta(z^-)-\Delta\vartheta(x).
\]

The KV envelope therefore gives

\[
M_z(x)
\le C_b\left[
ze^{-bV(z)}+xe^{-bV(x)}
\right].
\tag{8}
\]

Stieltjes summation with weight `1/t` on this phase yields

\[
\sum_{q\text{ in the fragment}}
(-c_q)\frac{\log q}{q}
\ll_b
e^{-bV(z)}
+
\int_{\text{fragment}}e^{-bV(t)}\frac{dt}{t}.
\tag{9}
\]

The endpoint at infinity vanishes for an infinite final phase because `M_z(x)/x -> 0`. For a finite phase its right endpoint contributes another local term bounded by the same `e^{-bV(z)}` scale.

Now sum (9) over all negative phase fragments meeting `[Y,infinity)`. Their interiors are disjoint, so the integral terms occupy only a subset of the full tail. Monotone convergence permits countably many phases and gives

\[
\boxed{
\sum_{\substack{q\ge Y\\c_q<0}}
(-c_q)\frac{\log q}{q}
\ll_b
\mathcal R_b^-(Y)
+
\int_Y^\infty e^{-bV(t)}\frac{dt}{t}.
}
\tag{10}
\]

The one-sided KV Laplace estimate already derived in `RE-176`--`RE-178` is

\[
\int_Y^\infty e^{-bV(t)}\frac{dt}{t}
=
\left(\frac5{3b}+o(1)\right)
\ell_{\rm KV}(Y)e^{-bV(Y)}.
\tag{11}
\]

Finally,

\[
B(q)=\frac{\log q}{q-1}
\le 2\frac{\log q}{q}
\]

for large `q`. Combining (6), (7), (10), and (11) proves (1).

This argument also explains why the weighted reset sum is the natural complexity coordinate. Replacing every phase start by the common lower bound `Y` loses its location and turns

\[
\sum_j e^{-bV(z_j)}
\]

into the cruder `M e^{-bV(Y)}` of `RE-177`. The count law is therefore a corollary of a more local budget, not the fundamental object.

## 3. Consequences for remote repair

Suppose first that

\[
\mathcal N_p^-(Y)
\le\frac12\delta_{\lambda,p}d_p.
\]

Then (1) and `d_p asymp (sqrt(p)log p)^(-1)` give (2). If the ordinary integrated KV tail is already subcritical,

\[
\ell_{\rm KV}(Y)e^{-bV(Y)}=o(d_p),
\]

then the reset term itself must satisfy

\[
\boxed{
\mathcal R_b^-(Y)\gg_{b,\lambda}d_p.
}
\tag{12}
\]

Hence arbitrarily many remote phases whose starts satisfy

\[
\sum_j e^{-bV(z_j)}=o\!\left(\frac1{\sqrt p\log p}\right)
\]

cannot repair the two boundary coordinates unless a Robin-scale fraction of the required negative centered workload has already been placed below `Y`.

For finite `M_-(Y)`, (12) and monotonicity of `V` imply

\[
M_-(Y)e^{-bV(Y)}\gg d_p,
\]

which reproduces the leading polynomial phase-count tariff of `RE-177`. But the converse interpretation is stronger: a phase beginning much farther than `Y` contributes exponentially less in the KV coordinate, so a raw count can dramatically overstate the effective complexity of a sparse infinite oscillatory tail.

The result also closes the explicit ordering loophole in `RE-177`. A control may alternate at high frequency immediately after `lambda p`; then either those early negative pieces already carry a fixed fraction of (5), or the surviving remote part must still pay (2). There is no need to identify a completed first positive phase or its barycenter.

## 4. Adversarial checks and exact boundary

**The first Euler slope is still extra source information.** Nothing here derives `D_Q'(1+)=0` from Robin's criterion, the CA selector, or the KV envelope. As in `RE-175`--`RE-178`, this theorem prices what a second source coordinate would force if legitimately available.

**Early negative repair is a genuine escape branch, not an omitted case.** Equation (1) is a localization dichotomy. If `mathcal N_p^-(Y)` is already comparable with `d_p`, the theorem intentionally stops demanding a remote reset budget: the compensation has occurred before `Y`. Ruling out such local interlacing requires a different source or selector constraint.

**Infinite reset budget remains uncontrolled.** If `mathcal R_b^-(Y)=infinity`, (1) is vacuous. The advance is that infinite *phase count* no longer suffices to evade the argument; what remains is divergence of a specific KV-weighted reset sum, or substantial early negative repair.

**The protected gap matters.** All non-deletion modifications are assumed to begin at `lambda p` with fixed `lambda>3`. This supplies the positive separation `delta_{lambda,p}`. For the `RE-173` choice `lambda=16`, the order-one Robin excursion measured before the compensators is untouched. If repair coefficients are allowed arbitrarily close to the deletion shell, `delta_{lambda,p}` can collapse and the centered two-jet debt need not be Robin-scale.

**No bounded-multiplicity assumption is used.** The coefficients `c_q` may be arbitrary integers. Within one sign phase, the KV envelope itself bounds the accumulated absolute Chebyshev mass through (8).

**Countable-phase convergence is not hidden.** When the reset sum on the right of (10) is finite, (10) gives absolute convergence of the negative first-slope tail; applying the same phasewise argument to the positive fragments gives the corresponding statement whenever their reset budget is finite. In applications where exact two-jet matching is asserted, the boundary sums are understood in the absolutely convergent sense used in `RE-175`. If a relevant reset sum diverges, the capacity statement is deliberately noncoercive.

## 5. Representation and prior-art audit

The generic layer is classical. Splitting a signed atomic source into positive/negative parts is Jordan decomposition, and (9) is Abel/Stieltjes summation on a monotone phase. The external prior-art search found the expected general signed-measure moment literature, total-variation formalism, and summation-by-parts identities, but no theorem needed as a new load-bearing input. The KV envelope remains anchored in `research/robin_extremal/SOURCES.md` through the line's prime-number-theorem source, so no new source entry is required.

The line-specific step is (4)--(5). The zeroth and first right-boundary Euler coordinates turn the `RE-173` deletion packet into equal positive and negative mass for the centered kernel `B-a_DH`; ordinary-prime support beyond a fixed multiplicative gap makes that kernel uniformly positive, and the Robin excursion fixes its debt at `d_p asymp (sqrt(p)log p)^(-1)`. The KV envelope then converts the location of each negative sign reset into the local weight `e^{-bV(z)}`.

This is not another scalar higher-jet estimate of the kind saturated by `RE-178`. It strengthens the **complexity coordinate itself** at the already useful two-jet level: raw finite sign count is replaced by a location-weighted quantity that remains meaningful for countably infinite oscillation.

## 6. Research consequence

After `RE-179`, the two-jet matched-control escape has a sharper trichotomy. A source can evade remote coercivity only by placing a Robin-scale amount of negative centered repair relatively early, by making the KV-weighted reset sum diverge or remain Robin-scale large, or by abandoning the second boundary coordinate itself. Merely declaring the tail to have infinitely many sign changes is no longer enough.

The next useful question is therefore source-specific: can ordinary-prime/integer-multiplicity structure force a bound on this weighted reset budget, or can one explicitly construct a `{0,1,2}` control with divergent reset budget while preserving the KV envelope and exact two-jet matching? Either outcome would decide whether infinite oscillation is a real arithmetic escape or only a formal one.