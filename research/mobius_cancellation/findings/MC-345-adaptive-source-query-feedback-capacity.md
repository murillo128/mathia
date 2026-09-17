# MC-345 — Adaptive source querying cannot beat per-access BSC capacity

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-344` prices a fixed set of source coordinates passed once through independent bit-flip noise. A natural escape is to choose which source coordinate to inspect **adaptively**: query one source phase, inspect the noisy answer, choose the next coordinate using that answer, possibly revisit coordinates, and stop when enough source information appears to have been recovered.

That feedback does not increase the information gained per source access.

Keep the reciprocal endpoint source law of `MC-340`:

\[
G=\mathbf F_2^R,\qquad
\Xi=G\setminus\{0\},\qquad
m=2^R-1,
\]

with `A` uniform on `Xi` and

\[
X=(X_1,\ldots,X_R)\in\{-1,+1\}^R.
\]

Let `U` be private/public controller randomness independent of `X`. At active query time `t`, choose an index

\[
J_t=\phi_t(U,J_{<t},Z_{<t})\in[R]
\tag{1}
\]

using only the previous transcript, and observe

\[
Z_t=X_{J_t}N_t,
\qquad
\mathbf P(N_t=-1)=q,
\qquad
q\in[0,1/2],
\tag{2}
\]

where the `N_t` are independent of `X`, `U`, and each other. Allow an adapted stopping time `\tau`, including deterministic fixed depth as a special case, and any downstream randomized postprocessing of the complete transcript

\[
T=(U,\tau,J_1,Z_1,\ldots,J_\tau,Z_\tau)
\]

to an admitted observation `Y`. Write, in natural units,

\[
h(q)=-q\log q-(1-q)\log(1-q),
\qquad
c(q)=\log2-h(q).
\tag{3}
\]

Whenever `\mathbf E\tau<\infty`, the adaptive transcript obeys

\[
\boxed{
I(X;Y)\le I(X;T)\le c(q)\,\mathbf E\tau.
}
\tag{4}
\]

Thus adaptive coordinate choice, source-dependent through past noisy answers, cannot create more than one BSC-capacity unit per actual source access. The query indices themselves carry no extra source information once the history that selected them is retained.

Combining `(4)` with the global transcript obstruction `MC-340` gives the source-access lower bound

\[
\boxed{
\mathbf E\tau\,c(q)
\ge
\frac R2
\left(
\frac{\eta^2}{C}-\frac1{m^2}
\right)
-\operatorname{TC}(X)
}
\tag{5}
\]

whenever

\[
\mathcal E(W)\le C,
\qquad
\delta(W)\le1-\eta.
\]

Since `\operatorname{TC}(X)=O(1)`, fixed `C,\eta>0` and fixed `q<1/2` force

\[
\boxed{
\frac{\mathbf E\tau}{R}
\ge
\frac{\eta^2}{2C\,c(q)}+o(1).
}
\tag{6}
\]

In particular, if `\mathbf E\tau=O(R)` but `c(q_R)=o(1)`, then `I(X;T)=o(R)` and bounded-energy constant-factor dephasing is impossible. Adaptive search cannot rescue a per-access channel whose capacity vanishes.

At the matched-filter energy floor, `MC-340` gives a stronger rate requirement. If

\[
\mathcal E(W)\le1,
\qquad
\delta(W)\le\varepsilon,
\qquad
\alpha_\varepsilon:=\varepsilon-\frac{\varepsilon^2}{2},
\]

then

\[
\boxed{
\mathbf E\tau\,c(q)
\ge
H(X)-R h(\alpha_\varepsilon).
}
\tag{7}
\]

Because `H(X)=R\log2-O(1)`, fixed query density `\mathbf E\tau/R` must pay explicitly for both the source entropy and the BSC entropy loss. For noiseless queries, `(7)` says near-exact unit-energy dephasing needs asymptotically one source-bit query per independent source bit.

There is also an exact zero-error statement. If `q=0` and a decision tree has hard depth at most `k`, exact unit-energy dephasing forces exact recovery of `X` by `MC-340`; hence the tree needs at least as many leaves as the support of the reciprocal source law. Therefore

\[
\boxed{
k\ge R\quad(R\ \mathrm{even}),}
\tag{8}
\]

while

\[
\boxed{
k\ge R-1\quad(R\ \mathrm{odd}).}
\tag{9}
\]

The odd-rank saving is exactly the single parity relation `X_1\cdots X_R=1`; querying any `R-1` coordinates determines the last one. For even `R`, the source support has `2^R-1` states, so fewer than `R` binary answers cannot identify it.

If `0<q<1/2`, no almost-surely finite adaptive BSC-query protocol can recover `X` with zero error: every finite transcript compatible with one source state has positive probability under every source state. Consequently exact unit-energy dephasing is impossible for any protocol with `\mathbf E\tau<\infty`.

No estimate for `M(x)` follows. The result closes an adaptive-control loophole in the finite reciprocal-endpoint model: a future arithmetic architecture cannot evade the source-information budget merely by deciding online which noisy source phase to inspect next.

## 1. Feedback chain rule gives the per-query capacity bound

First take a deterministic query budget `k`. Condition on the independent seed `U` and define the history

\[
\mathcal H_t=(U,J_{<t},Z_{<t}).
\]

By construction `J_t` is a deterministic function of `\mathcal H_t`, so

\[
I(X;J_t\mid\mathcal H_t)=0.
\tag{10}
\]

Conditioned on `X`, `\mathcal H_t`, and `J_t`, the only uncertainty in `Z_t` is the fresh BSC noise `N_t`. Hence

\[
H(Z_t\mid X,\mathcal H_t,J_t)=h(q).
\tag{11}
\]

Since `Z_t` is binary,

\[
H(Z_t\mid\mathcal H_t,J_t)\le\log2.
\tag{12}
\]

Therefore

\[
I(X;Z_t\mid\mathcal H_t,J_t)
\le\log2-h(q)=c(q).
\tag{13}
\]

The chain rule, `(10)`, and `(13)` give

\[
I(X;U,J_{1:k},Z_{1:k})
\le
\sum_{t=1}^k c(q)
=k c(q),
\tag{14}
\]

because `I(X;U)=0`. Data processing then gives the same upper bound for every downstream `Y`.

For a stopping time `\tau`, expose at each integer time an activity indicator `A_t=1_{\{\tau\ge t\}}`, which is measurable from the previous history, and use a dummy symbol when `A_t=0`. The stopping decision itself contributes no new conditional source information; an active step contributes at most `c(q)` by the same argument as `(13)`, while an inactive step contributes zero. Thus

\[
I(X;T)
\le
c(q)\sum_{t\ge1}\mathbf P(\tau\ge t)
=c(q)\,\mathbf E\tau,
\tag{15}
\]

which proves `(4)`.

The dependence among the reciprocal source coordinates is irrelevant to this converse. The input bit selected at time `t` may have an arbitrary history-dependent conditional distribution; the BSC still transmits at most `c(q)` nats about that bit, and therefore at most `c(q)` nats about the complete source vector.

## 2. Coupling to the endpoint dephasing requirement

`MC-340` proves that `\mathcal E(W)\le C` and `\delta(W)\le1-\eta` require

\[
I(X;Y)
\ge
\frac R2
\left(
\frac{\eta^2}{C}-\frac1{m^2}
\right)
-\operatorname{TC}(X).
\tag{16}
\]

Combining `(16)` with `(4)` gives `(5)`. The exact source-law calculation in `MC-340` gives

\[
\operatorname{TC}(X)\to0
\quad(R\to\infty,\ R\ \mathrm{even}),
\qquad
\operatorname{TC}(X)\to\log2
\quad(R\to\infty,\ R\ \mathrm{odd}),
\tag{17}
\]

so `(6)` follows immediately.

At `\mathcal E(W)\le1` and `\delta(W)\le\varepsilon`, the Fano argument of `MC-340` gives

\[
I(X;Y)
\ge
H(X)-R h(\alpha_\varepsilon).
\tag{18}
\]

Combining `(18)` with `(4)` proves `(7)`. The exact entropy formulas from `MC-340` imply `H(X)=R\log2-O(1)`, with the `O(1)` term representing only puncturing and, for odd rank, one parity relation.

The result should not be overread as an achievability theorem. If `\mathbf E\tau\,c(q)` exceeds the right side of `(7)`, the information budget is merely no longer an obstruction. Repeated noisy measurements still have to be converted into the specific coherent coefficient family required by endpoint dephasing.

## 3. Exact noiseless depth and positive-noise zero-error obstruction

When `q=0`, a hard-depth-`k` adaptive query strategy is a binary decision tree with at most `2^k` leaves. Exact unit-energy dephasing forces `H(X\mid T)=0` by `MC-340`, so distinct source states must end in distinct leaves.

For even `R`, `MC-340` identifies `X` as uniform on the `2^R-1` cube points other than the all-`+1` word. Hence

\[
2^k\ge2^R-1,
\]

which forces `k\ge R` and proves `(8)`.

For odd `R`, the support is the `2^{R-1}` even-parity words satisfying `X_1\cdots X_R=1`. Hence

\[
2^k\ge2^{R-1},
\]

which gives `(9)`. The bound is sharp at the source-recovery level because any `R-1` coordinates determine the remaining coordinate from parity.

Now let `0<q<1/2`. Fix the controller seed `U=u` and any finite transcript path admitted by the adaptive rule. Along that path the queried indices are fixed functions of the preceding observed signs. For every source vector `x` in the support, each required BSC output has conditional probability either `q` or `1-q`, both strictly positive. Therefore every finite path that has positive probability for one source state has positive probability for every source state.

If an almost-surely finite stopping protocol recovered `X` with zero error, some finite terminal transcript assigned to one source state would have positive probability under that state but zero probability under every other state, contradicting the common-support property above. Finite expected stopping time implies almost-sure finite stopping, so exact source recovery—and therefore exact unit-energy dephasing—is impossible whenever `0<q<1/2` and `\mathbf E\tau<\infty`.

This zero-error statement is stronger than the Shannon-capacity inequality only at the endpoint `\varepsilon=0`. It does not say that fixed positive noise prevents arbitrarily small nonzero error when the query budget per source grows; repeated observations can drive estimation error down, at an additional access cost that `(7)` prices only from below.

## Prior art and novelty boundary

The feedback-capacity mechanism is classical. R. L. Dobrushin, *Information Transmission in a Channel with Feedback*, Theory of Probability & Its Applications **3** (1958), 367–383, DOI `10.1137/1103031`, proves that feedback does not increase the capacity of channels without memory. Standard modern treatments derive the discrete-memoryless feedback converse by the same conditional mutual-information chain rule used in `(10)`–`(15)`.

Cover and Thomas, *Elements of Information Theory*, 2nd ed., Wiley (2006), Chapter 7, develop discrete memoryless channel capacity and the BSC capacity `1-H_2(q)`; `MC-344` already uses that classical channel bound for a fixed coordinate set.

A targeted literature audit on 17 September 2026 therefore makes no novelty claim for feedback not increasing memoryless-channel capacity, adaptive decision trees, stopping-time chain rules, or binary-source coding bounds. The durable Mathia delta is the exact specialization to the reciprocal endpoint source-access model and its coupling to the independent `MC-340` dephasing-information lower bound. Equations `(5)`–`(9)` show that **online coordinate selection is not a free source-information resource**: it cannot evade the linear access budget, and the exact even/odd source geometry determines the noiseless zero-error depth.

## Boundaries and falsification tests

- **The controller may adapt only through the admitted transcript.** If the index selector can inspect `X` by some side channel before choosing `J_t`, then the indices themselves can encode source information and `(10)` fails. Such a side channel must be included in the transcript budget rather than hidden in the query policy.
- **The channel is memoryless conditional on the queried source bit.** Correlated, stateful, or source-dependent noise need not obey the per-use bound `c(q)` and requires its own capacity audit.
- **Repeated queries are allowed.** The theorem does not rely on a fixed subset and therefore genuinely strengthens the fixed-`J` converse of `MC-344`.
- **Linear or even superlinear access can survive the obstruction.** Equations `(5)` and `(7)` are necessary conditions, not sufficiency. The result does not rule out an arithmetic architecture that genuinely exposes enough source information.
- **Positive noise blocks exact recovery, not arbitrarily accurate recovery.** With growing repeated-query budget one can reduce estimation error; this finding does not derive the sharp reliability exponent or the minimum budget for a specified small nonzero error.
- **The even/odd hard-depth bounds concern exact source recovery.** They use the exact reciprocal support computed in `MC-340`; they are not generic statements about arbitrary dependent binary sources.
- **No arithmetic source-access theorem is supplied.** The missing step remains to prove that a natural Möbius-derived observable admits a source-query/channel representation with controlled aggregate capacity.
- **No RH or Mertens estimate follows.** This remains a finite reciprocal-endpoint admission theorem.

## Consequence for the research line

`MC-344` shows that an extensive one-shot noisy digital transcript can retain `Theta(R)` source information. The present result shows that **adaptivity does not enlarge that budget per access**. A future low-capacity obstruction may therefore count genuine source accesses even when the architecture chooses them online; there is no need to forbid feedback syntactically.

The remaining arithmetic question is sharper: identify a natural Möbius-derived transcript, expose the side information available to its selector, and prove a bound on the number or total capacity of source accesses needed to realize it. If the arithmetic mechanism can access `Theta(R)` informative source degrees of freedom—or more through repeated measurements—the finite information obstruction alone is exhausted and a different structural restriction is needed.