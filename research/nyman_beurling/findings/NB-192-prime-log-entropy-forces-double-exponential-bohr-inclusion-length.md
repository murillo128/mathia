# NB-192 — Prime-log entropy forces double-exponential Bohr inclusion length

**Date:** 2026-09-17  
**Status:** `DERIVED + NEGATIVE/OBSTRUCTION + SOURCE-ACQUISITION + COUPLED-SCALING + BOHR-RECURRENCE + METRIC-ENTROPY + NB-191-REFINEMENT`.

`NB-191` proves that, for every fixed exterior width `a` and fixed positive synthesis accuracy, finite-frequency Bohr recurrence eventually transports the sharp `NB-190` band synthesizers into every sufficiently high dyadic block. Its own self-audit leaves one quantity unresolved: the common-return inclusion length when `a=a_T->0` and the active Euler frequency set grows.

That nonuniformity is not mild. Already the prime frequencies in **one** fixed log-width band force any syndetic common-return guarantee to have double-exponential scale in `1/a`. More precisely, if `L_(a,epsilon)` is an inclusion length for the common phase returns used by `NB-191`, then for every fixed `0<epsilon<1`,

\[
\boxed{
\log L_{a,\epsilon}
\gg_{r_0,\Delta,\epsilon}
a\,e^{r_0/a}.
}
\tag{1}
\]

Consequently the recurrent-transplant mechanism of `NB-191` can be guaranteed inside a block of length `T` only if, necessarily,

\[
\boxed{
a
\ge
\frac{r_0}
{\log\log T+\log\log\log T+O_{r_0,\Delta,\epsilon}(1)}.
}
\tag{2}
\]

This is a lower bound on the **worst-gap/syndetic Bohr transport mechanism**, not on the optimal high-block synthesis problem. A particular dyadic block may contain an unusually early common return, and a different acquisition architecture may preserve the band masks without requiring every active phase to recur coordinatewise. What (1) closes is the possibility that the qualitative fixed-`a` recurrence theorem from `NB-191` becomes uniform in the coupled limit at anything like polynomial cost.

## Setup

Retain the notation of `NB-189`--`NB-191`. Thus the balanced Euler bands have

\[
S_{k,a}
=
\{n:L_k\le\log n<L_k+\Delta\},
\qquad
L_k=\frac{r_0}{a}+k\Delta,
\tag{3}
\]

where `0<r_0<r_1<2`, `Delta>0` is fixed and `K(a)\asymp1/a`. Their active frequency union is

\[
\Lambda_a^{\rm band}
=
\left\{
\log n:\alpha_{n,a}>0,
\ n\in\bigcup_{k=0}^{K-1}S_{k,a}
\right\}.
\tag{4}
\]

For `0<delta<1`, write

\[
\mathcal P_a(\delta)
:=
\left\{
\tau\in\mathbb R:
\max_{\lambda\in\Lambda_a^{\rm band}}
|e^{-i\tau\lambda}-1|<\delta
\right\}.
\tag{5}
\]

An inclusion length `L_a(delta)` means that every real interval of length `L_a(delta)` intersects `mathcal P_a(delta)`. `NB-191` uses a fixed tolerance

\[
0<\delta\le\delta_\epsilon
:=
\frac{\epsilon}{2+\epsilon},
\tag{6}
\]

so `delta_epsilon` is independent of `a` when the target coefficient error `epsilon` is fixed.

It is enough to restrict (5) to the prime frequencies in the first band. Put

\[
\mathcal Q_a
:=
\left\{
p\ \text{prime}:
\frac{r_0}{a}
\le\log p<
\frac{r_0}{a}+\Delta
\right\},
\qquad
m_a:=|\mathcal Q_a|.
\tag{7}
\]

Every such prime has positive von-Mangoldt/Euler weight, hence `log p` belongs to `Lambda_a^band`. Therefore any common return for the full active union is also a common return for the `m_a` prime coordinates in (7).

## Claim 1: one fixed Euler band already contains exponentially many independent phase coordinates

The frequencies

\[
\{\log p:p\in\mathcal Q_a\}
\tag{8}
\]

are linearly independent over `Q`. Indeed, if integers `h_p` satisfy

\[
\sum_{p\in\mathcal Q_a}h_p\log p=0,
\]

then

\[
\prod_{p\in\mathcal Q_a}p^{h_p}=1,
\]

and unique factorization forces every `h_p=0`.

Hence the continuous phase flow

\[
\Phi_a(t)
:=
\bigl(e^{-it\log p}\bigr)_{p\in\mathcal Q_a}
\in\mathbb T^{m_a}
\tag{9}
\]

has dense image in the full `m_a`-torus. There is no hidden quotient reducing this prime-coordinate dimension.

The prime number theorem gives a sharp asymptotic for that dimension. Setting `x_a=exp(r_0/a)`,

\[
\begin{aligned}
m_a
&=
\pi(e^\Delta x_a)-\pi(x_a)\\
&=
\left(
\frac{e^\Delta-1}{r_0}+o(1)
\right)
 a e^{r_0/a}.
\end{aligned}
\tag{10}
\]

Thus a **single** band of fixed width in `log n` already carries exponentially many rationally independent prime phases as `a downarrow0`.

## Claim 2: a syndetic return set forces a short orbit segment to fill the whole prime torus

Let `L` be any inclusion length for the full return set `mathcal P_a(delta)`. It is then also an inclusion length for the weaker prime-coordinate return condition

\[
\max_{p\in\mathcal Q_a}
|e^{-i\tau\log p}-1|<\delta.
\tag{11}
\]

We claim that the orbit segment

\[
\Phi_a([0,L])
\tag{12}
\]

is `delta`-dense in `mathbb T^{m_a}` for the product chord metric

\[
d_\infty(z,w)
:=
\max_j|z_j-w_j|.
\tag{13}
\]

To see this, fix any target `y in mathbb T^(m_a)`. Density of the full flow lets us choose `x` with `Phi_a(-x)` arbitrarily close to `y`. Since every interval of length `L` contains a return, there is

\[
\tau\in[x,x+L]
\]

satisfying (11). Put `s=tau-x`, so `0<=s<=L`. The homomorphism law gives

\[
\Phi_a(s)
=
\Phi_a(\tau)\Phi_a(-x).
\tag{14}
\]

Because `Phi_a(tau)` is `delta`-close to the identity, `Phi_a(s)` is `delta`-close to `Phi_a(-x)`. Letting the initial approximation to `y` tend to zero proves the claim.

This implication is the reverse quantitative content hidden inside the compactness argument of `NB-191`: **relative density of identity returns at gap `L` forces the length-`L` orbit segment itself to be a filling curve for the whole orbit closure**.

## Claim 3: a one-dimensional phase curve cannot fill an m-torus before exponential time

Let

\[
\lambda_{\max}(a)
:=
\max_{p\in\mathcal Q_a}\log p
<
\frac{r_0}{a}+\Delta.
\tag{15}
\]

The phase curve (9) is `lambda_max(a)`-Lipschitz in the metric (13):

\[
d_\infty(\Phi_a(t),\Phi_a(s))
\le
\lambda_{\max}(a)|t-s|.
\tag{16}
\]

Partition `[0,L]` into at most

\[
J
\le
1+rac{L\lambda_{\max}(a)}{\delta}
\tag{17}
\]

subintervals so that every orbit point lies within `delta` of one sampled point. By Claim 2, those `J` sampled points are therefore `2delta`-dense in the full torus.

For one circle coordinate, a chord ball of radius `2delta` has normalized Haar measure

\[
\frac{2\arcsin\delta}{\pi}
\le\delta
\qquad(0<\delta<1),
\tag{18}
\]

where the last inequality is the convex-chord bound `arcsin(delta)<=pi delta/2`. Hence a product `d_infty` ball of radius `2delta` in `mathbb T^(m_a)` has Haar measure at most

\[
\delta^{m_a}.
\tag{19}
\]

If `J` such balls cover the torus, Haar measure gives

\[
1
\le
J\delta^{m_a}.
\tag{20}
\]

Combining (17) and (20),

\[
\boxed{
L
\ge
\frac{\delta}{\lambda_{\max}(a)}
\left(
\delta^{-m_a}-1
\right).
}
\tag{21}
\]

No Diophantine lower bound is used here. This is pure metric entropy: a one-dimensional Lipschitz curve needs at least `delta^{-(m-1)}` units of normalized travel to become `delta`-dense in an `m`-dimensional torus.

## Claim 4: the NB-191 inclusion length is double-exponential in 1/a

Insert (10) and (15) into (21). For every fixed `0<delta<1`,

\[
\begin{aligned}
\log L_a(\delta)
&\ge
(m_a-1)\log\frac1\delta
-
\log\lambda_{\max}(a)
+O_\delta(1)\\
&=
\left(
\frac{e^\Delta-1}{r_0}
\log\frac1\delta
+o(1)
\right)
 a e^{r_0/a}.
\end{aligned}
\tag{22}
\]

In particular,

\[
\boxed{
L_a(\delta)
\ge
\exp\!\left(
 c_{r_0,\Delta,\delta}
 a e^{r_0/a}
\right)
}
\tag{23}
\]

for all sufficiently small `a`, with `c_(r_0,Delta,delta)>0`.

For the fixed-accuracy transplant of `NB-191`, take `delta=delta_epsilon` from (6). Any smaller tolerance only increases the return-set difficulty, so (23) proves (1).

This scale is double-exponential in the natural resolution parameter `1/a`: the logarithm of the inclusion length is itself exponential in `1/a`. It comes from two separate facts: there are `m_a asymp a exp(r_0/a)` independent prime phases already in one band, and filling an `m_a`-torus at fixed accuracy requires time exponential in `m_a`.

## Claim 5: uniform recurrent transport imposes a log-log width floor

Suppose the `NB-191` common-return argument is to be guaranteed inside a block whose available length is `T`. Necessarily its inclusion length must satisfy, up to the seed-support margin,

\[
L_{a,\epsilon}\lesssim T.
\tag{24}
\]

Equations (1) and (24) force

\[
a e^{r_0/a}
\ll_{r_0,\Delta,\epsilon}
\log T.
\tag{25}
\]

Set

\[
x:=\frac{r_0}{a}.
\]

Then (25) becomes

\[
\frac{e^x}{x}
\ll
\log T,
\]

or

\[
x-\log x
\le
\log\log T+O_{r_0,\Delta,\epsilon}(1).
\tag{26}
\]

Inverting this standard relation gives

\[
\boxed{
\frac{r_0}{a}
\le
\log\log T
+
\log\log\log T
+
O_{r_0,\Delta,\epsilon}(1),
}
\tag{27}
\]

which is equivalent to the width floor (2).

Thus the fixed-`a` conclusion of `NB-191` is maximally nonuniform on ordinary shrinking-width scales. For example, any polynomial coupling `a=T^{-gamma}` lies vastly below (2); the qualitative syndetic-recurrence proof gives no route for placing its common-return transplant inside the contemporaneous block.

## What this rules out, and what it does not

The result closes the simplest optimistic reading of `NB-191`: one cannot hope that its finite-frequency recurrence threshold is merely polynomial, singly exponential, or otherwise modest in `1/a`. The active source contains an exponentially large independent prime-log subsystem before one even uses all `K asymp1/a` bands, and metric entropy alone forces the common-return inclusion length to be at least (23).

The conclusion is deliberately narrower than a high-block no-go theorem. Equation (21) bounds a **syndetic inclusion length**: the worst gap required to guarantee a return in every interval. It does not imply that the particular interval `[T,2T]` lacks a common return whenever `T<L_a(delta)`. An individual block can be lucky. Nor does it show that the optimal high-block Fourier--Stieltjes synthesizer must arise by translating the low-height seed from `NB-190`.

Likewise, coordinatewise recurrence of every active prime phase is a sufficient condition used by `NB-191`, not a proved necessary condition for preserving the weighted coefficient error. An aggregate phase condition could potentially exploit the positive Euler weights and require much less than filling the full prime torus. Such a mechanism would escape the present bound and is now exactly the interesting positive route.

Finally, the support radius `R_(a,epsilon)` of the compact seed from `NB-191` may itself grow rapidly. The present theorem does not estimate it. This omission only makes the recurrent-transplant threshold potentially larger; it cannot weaken the lower bound on the Bohr inclusion length itself.

## Representation and prior-art audit

The geometric part of the proof is representation-agnostic. Once a one-parameter flow is dense in an `m`-torus, a fixed-accuracy filling segment must have length exponential in `m`; (17)--(21) are a direct covering-volume proof of that metric-entropy fact. Quantitative filling times for linear torus flows are a classical subject. A focused search found H. Scott Dumas and Stéphane Fischler, *Filling Times for Linear Flow on the Torus with Truncated Diophantine Conditions: A Brief Review and New Proof*, Qualitative Theory of Dynamical Systems 21 (2022), 103, DOI `10.1007/s12346-022-00637-3`, and Victor Shirandami, *Dense forests constructed from grids*, Mathematische Zeitschrift 305 (2023), article 15, whose Section 3 explicitly formulates filling times for linear torus flows. These are context-only: no external filling-time theorem is used in the derivation above.

The arithmetic-specific content is not the generic torus entropy. It is that the **actual Euler acquisition source** from `NB-189`--`NB-191` contains, inside a single fixed log-width band, `m_a asymp a exp(r_0/a)` active prime coordinates whose logarithms are rationally independent. Unique factorization supplies the independence; the prime number theorem supplies the dimension growth. That converts a generic `delta^{-m}` filling tariff into the source-specific double-exponential scale (23).

The PNT is already an anchored dependency in `research/nyman_beurling/SOURCES.md`, and the independence argument is elementary. The prior-art search did not identify a theorem needed beyond those existing anchors, so `SOURCES.md` remains unchanged. The absence of a paper making this exact Euler-band/Bohr-threshold comparison is not used as evidence of novelty.

## Self-adversarial audit

The largest possible overclaim would be to replace “the `NB-191` syndetic common-return mechanism cannot be uniform below the log-log width floor” by “high-block synthesis is impossible below that floor.” The latter has not been proved. The lower bound concerns the worst-gap return set defined in (5), not the optimal coefficient-topology acquisition problem.

A second possible loophole is rational dependence among the Euler frequencies. Prime powers certainly introduce such dependencies, because `log p^j=j log p`. The proof avoids that issue by discarding everything except distinct prime coordinates in one band. Their logarithms are exactly `Q`-independent, so the orbit closure on that subsystem is the full torus and the entropy dimension cannot collapse.

A third concern is that the first balanced band has only source mass `Theta(a)`. That does not matter for this statement: `NB-191` requires a common phase return on the entire active union to transplant all normalized bands, and therefore in particular requires recurrence on every prime in this first band. The result does **not** claim that a future weighted/aggregate recurrence argument must resolve those phases individually.

The covering estimate also keeps the dimensional constants explicit enough not to hide the conclusion. The ball-volume factor is `delta^(m_a)` and the curve-cover cardinality is linear in `L lambda_max/delta`; there is no factorial or exponentially growing geometric constant capable of cancelling the `m_a log(1/delta)` exponent.

## Research consequence

`NB-191` removed a universal high-block surcharge by taking `a` fixed before sending `T` to infinity. `NB-192` quantifies exactly why that order of limits cannot simply be interchanged: the common-return inclusion length required by its own transplant construction is at least

\[
\exp\!\left(c_\epsilon a e^{r_0/a}\right).
\]

The next discriminator is therefore no longer the generic Bohr inclusion length. Its entropy scale is already too large. The useful questions are more specific:

- can the **particular** dyadic block `[T,2T]` contain sufficiently early prime-log returns much sooner than the worst-gap inclusion length predicts, for the relevant coupling `a=a_T`;
- can weighted or band-averaged recurrence preserve the `NB-190` coefficient masks without coordinatewise recurrence of exponentially many prime phases; or
- can one prove a source-native lower bound showing that every such aggregate shortcut still pays a comparable acquisition tariff?

Those are genuinely arithmetic/source-topology questions. Generic finite-dimensional almost periodicity has now been priced sharply enough to stop carrying the coupled-limit argument by itself.

## Evidence ledger

**Internal load-bearing dependencies:** `NB-189` for the balanced bands and their fixed log-width geometry; `NB-190` for the normalized Euler band acquisition topology; `NB-191` for the common-return transplant mechanism and its fixed tolerance `delta<=epsilon/(2+epsilon)`. `NB-006` is a line-local precedent for simultaneous prime-log recurrence but is not used in the proof.

**External load-bearing dependencies:** the prime number theorem for (10), already anchored in `research/nyman_beurling/SOURCES.md`.

**Elementary source-specific input:** unique factorization, used to prove rational independence of distinct prime logarithms.

**Context-only prior art consulted:** Dumas--Fischler (2022) and Shirandami (2023) on quantitative filling times for linear flows on tori; classical Kronecker/Bohr recurrence as already audited in `NB-191`.
