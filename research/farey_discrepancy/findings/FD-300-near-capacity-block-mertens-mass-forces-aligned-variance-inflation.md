# FD-300 — Near-capacity block-Mertens mass forces aligned variance inflation

- **Date:** 2026-09-24
- **Status:** proved necessary aligned-variance inflation and masked two-point correlation consequence
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** block-Mertens field / divisor replication / dyadic shell energy / aligned short intervals / masked Möbius correlations / capacity obstruction
- **Depends on:** FD-261, FD-263, FD-265, FD-298, FD-299
- **Classification:** `EXACT-DERIVED + NECESSARY-L2-INFLATION + MASKED-CORRELATION-OBSTRUCTION + CAPACITY-BOUNDARY + ROUTE-REDUCTION`

## Claim

After FD-298 and FD-299, the live low-height hard-complement question is essentially whether the block-Mertens divisor convolution

\[
G_N(d)=\sum_{q\mid d}U_N(q),
\qquad
U_N(q)=M(Nq)-M(N(q-1))
\tag{1}
\]

can have near-capacity band mass

\[
L_N(x):=\sum_{x<d\le2x}|G_N(d)|.
\tag{2}
\]

Let

\[
c:=1-\log_2(3/2)=0.4150374992\ldots,
\tag{3}
\]

and let the current near-capacity scale be

\[
B_{N,x}:=
\frac{N^{1/2}x^{1+c}}{\ell(x)},
\qquad
\ell(x)=x^{o(1)}.
\tag{4}
\]

The new reduction is that any lower bound

\[
L_N(x)\ge B_{N,x}x^{-o(1)}
\tag{5}
\]

forces a large second moment of the **aligned length-`N` Mertens blocks** on at least one dyadic denominator shell. More precisely, there exists a dyadic `Q` with `1\le Q\le2x` such that

\[
\boxed{
\frac1Q
\sum_{Q<q\le2Q}
|U_N(q)|^2
\ge
N x^{2c-o(1)}.
}
\tag{6}
\]

If instead `L_N(x)\ge\delta B_{N,x}` for a fixed `\delta>0`, one may keep the explicit logarithmic loss:

\[
\boxed{
\frac1Q
\sum_{Q<q\le2Q}
|U_N(q)|^2
\gg
\frac{\delta^2 N x^{2c}}
{\ell(x)^2(\log x)^2}.
}
\tag{7}
\]

Thus near-capacity mass after divisor replication cannot be generated from block increments having only square-root-scale mean energy on every dyadic shell. Some shell must have root-mean-square size

\[
\boxed{
\operatorname{RMS}_{Q<q\le2Q}U_N(q)
\ge
N^{1/2}x^{c-o(1)}.
}
\tag{8}
\]

Conversely, any fixed power saving below this threshold on **every** dyadic shell kills the route. If for some fixed `\eta>0`, uniformly for all relevant `Q`,

\[
\frac1Q
\sum_{Q<q\le2Q}|U_N(q)|^2
\ll
N x^{2c-\eta},
\tag{9}
\]

then

\[
\boxed{
L_N(x)
\ll
N^{1/2}x^{1+c-\eta/2+o(1)}
=o(B_{N,x}).
}
\tag{10}
\]

So the remaining magnitude gate can be falsified by a source-side variance estimate before one analyzes any further divisor cancellation.

## 1. Dyadic shell forcing from the exact replication ledger

For

\[
I_x=(x,2x]\cap\mathbb Z,
\qquad
m_x(q):=\#\{d\in I_x:q\mid d\},
\tag{11}
\]

FD-263 gives the exact triangle-ledger upper bound

\[
L_N(x)
\le
W_N(x)
:=
\sum_{q\le2x}m_x(q)|U_N(q)|.
\tag{12}
\]

Split `q\le2x` into `K=O(\log x)` dyadic shells. If (5) holds, one shell `(Q,2Q]` satisfies

\[
W_Q
:=
\sum_{Q<q\le2Q}m_x(q)|U_N(q)|
\ge
\frac{L_N(x)}K.
\tag{13}
\]

On such a shell,

\[
m_x(q)\ll \frac{x}{Q},
\qquad
\sum_{Q<q\le2Q}m_x(q)\ll x.
\tag{14}
\]

Cauchy-Schwarz therefore gives

\[
\begin{aligned}
W_Q^2
&\le
\left(\sum_{Q<q\le2Q}m_x(q)\right)
\left(\sum_{Q<q\le2Q}m_x(q)|U_N(q)|^2\right)\\
&\ll
x\cdot\frac{x}{Q}
\sum_{Q<q\le2Q}|U_N(q)|^2.
\end{aligned}
\tag{15}
\]

Hence

\[
\boxed{
\frac1Q
\sum_{Q<q\le2Q}|U_N(q)|^2
\gg
\frac{W_Q^2}{x^2}.
}
\tag{16}
\]

Substituting (4), (5), and (13) proves (6), while a fixed `\delta` gives (7).

This implication is deliberately one-sided. The ledger (12) may lose heavily when contributions from different divisors cancel inside `G_N(d)`. Therefore large aligned block variance is **necessary, not sufficient**, for a large `L_N(x)`. That makes (6) suitable as a falsification target: if the source itself cannot supply this much energy, no later divisor geometry can recover the missing capacity.

## 2. Uniform shell variance saving kills near-capacity mass

The same estimate runs backward as an upper-bound mechanism. If (9) holds on a dyadic shell, then (15) gives

\[
W_Q
\ll
x
\left(
\frac1Q\sum_{Q<q\le2Q}|U_N(q)|^2
\right)^{1/2}
\ll
N^{1/2}x^{1+c-\eta/2}.
\tag{17}
\]

Summing over `O(\log x)=x^{o(1)}` shells yields

\[
W_N(x)
\ll
N^{1/2}x^{1+c-\eta/2+o(1)}.
\tag{18}
\]

Since `L_N\le W_N`, this proves (10). For subpolynomial `\ell(x)`, every fixed `\eta>0` wins against the near-capacity budget.

This identifies a clean quantitative target that is upstream of the divisor convolution. It is enough to prove a **fixed power saving** in the aligned block second moment relative to `N x^{2c}` on every shell. Merely showing a logarithmic saving does not cross the current capacity exponent.

## 3. The required energy forces a positive same-block two-point bias

The second moment has an exact Möbius interpretation. Write

\[
U_N(q)
=
\sum_{r=1}^{N}
\mu(N(q-1)+r).
\tag{19}
\]

For one block,

\[
\begin{aligned}
U_N(q)^2
={}&
\sum_{r=1}^{N}\mu(N(q-1)+r)^2\\
&+2\sum_{h=1}^{N-1}
\sum_{r=1}^{N-h}
\mu(N(q-1)+r)
\mu(N(q-1)+r+h).
\end{aligned}
\tag{20}
\]

After summing over a shell, define

\[
D_Q
:=
\sum_{Q<q\le2Q}
\sum_{r=1}^{N}
\mu(N(q-1)+r)^2,
\tag{21}
\]

and

\[
C_{Q,h}
:=
\sum_{Q<q\le2Q}
\sum_{r=1}^{N-h}
\mu(N(q-1)+r)
\mu(N(q-1)+r+h).
\tag{22}
\]

Then exactly

\[
\sum_{Q<q\le2Q}U_N(q)^2
=
D_Q+2\sum_{h=1}^{N-1}C_{Q,h}.
\tag{23}
\]

The diagonal satisfies only

\[
0\le D_Q\le NQ.
\tag{24}
\]

If (6) is forced, then

\[
\sum_{Q<q\le2Q}U_N(q)^2
\ge
QN x^{2c-o(1)}.
\tag{25}
\]

Because `c>0`, the diagonal (24) is negligible relative to (25). Consequently

\[
\boxed{
\sum_{h=1}^{N-1}C_{Q,h}
\ge
QN x^{2c-o(1)}.
}
\tag{26}
\]

Here and below harmless fixed factors are absorbed into the `x^{o(1)}` term. Pigeonholing over the `N-1` lags gives at least one `h=h(Q,N,x)` such that

\[
\boxed{
C_{Q,h}
\ge
Q x^{2c-o(1)}.
}
\tag{27}
\]

This is a **positive** correlation requirement. Since `C_{Q,h}` contains at most `Q(N-h)` summands of magnitude at most one, (27) also forces

\[
N-h\ge x^{2c-o(1)}
\tag{28}
\]

and a relative same-block bias of at least

\[
\boxed{
\frac{C_{Q,h}}{Q(N-h)}
\ge
\frac{x^{2c-o(1)}}{N}.
}
\tag{29}
\]

The mask in (22) matters. It retains pairs separated by `h` only when both endpoints lie in the **same aligned length-`N` block**. Pairs crossing a boundary `Nq` are absent. Thus (27) is not the ordinary global Chowla correlation at fixed shift; its period grows with `N`, and the shift selected by pigeonhole may grow as well.

## 4. Polynomial-depth calibration

Suppose

\[
x=N^{\lambda+o(1)}.
\tag{30}
\]

Then the forced root-mean-square scale (8) is

\[
N^{1/2+c\lambda-o(1)}.
\tag{31}
\]

The trivial pointwise bound `|U_N(q)|\le N` already rules this out when

\[
\frac12+c\lambda>1,
\tag{32}
\]

namely

\[
\boxed{
\lambda>
\frac1{2c}
=
1.2047104198\ldots.
}
\tag{33}
\]

This recovers, from the source-energy side, the same capacity ceiling already visible elsewhere in the repair ledger. No arithmetic theorem is needed beyond that point: the block increments are simply too short to carry the required energy.

At balanced depth `\lambda=1`, near-capacity mass requires

\[
\operatorname{RMS} U_N(q)
\ge
N^{1/2+c-o(1)}
=
N^{0.9150374992\ldots-o(1)},
\tag{34}
\]

or equivalently mean square

\[
\frac1Q\sum_{Q<q\le2Q}U_N(q)^2
\ge
N^{1+2c-o(1)}
=
N^{1.8300749985\ldots-o(1)}.
\tag{35}
\]

The corresponding masked correlation (29) requires relative positive bias at least

\[
N^{2c-1-o(1)}
=
N^{-\log_2(9/8)-o(1)},
\tag{36}
\]

because

\[
1-2c
=
\log_2(9/8)
=
0.1699250014\ldots.
\tag{37}
\]

Thus a source-side variance theorem saving any fixed exponent beyond `1-2c=0.169925...` from the natural RH pointwise envelope in the deepest balanced shells would eliminate this near-capacity route.

## 5. Relation to existing short-interval Möbius results

This finding does **not** claim a new theorem on short-interval Möbius cancellation. Its content is the exact quantitative reduction from the Farey divisor-replication capacity problem to the aligned second-moment threshold (6), followed by the masked two-point consequence (27).

The short-interval literature already anchored in `SOURCES.md` lies close to this target. Matomäki--Teräväinen give cancellation for the Möbius function in all sufficiently long short intervals, and Matomäki--Radziwiłł--Shao--Tao--Teräväinen give strong almost-all short-interval uniformity results. Those results are evidence that the required inflation is arithmetically demanding, but they do not directly supply the fixed polynomial saving in (9) uniformly on the sparse aligned starts `N(q-1)` that this reduction needs.

Likewise, standard averaged or fixed-shift Chowla-type statements do not immediately control (22): the same-block mask has period `N`, excludes boundary-crossing pairs, and the relevant lag may grow with `N`. Replacing (22) by an unmasked global correlation would therefore require a separate boundary analysis rather than a formal citation.

No new external theorem is load-bearing in the proof of (6)--(29), so no new source anchor is required for this finding.

## 6. Adversarial review and failure modes

Several tempting stronger readings are not justified.

First, (6) is only a **necessary** source-energy condition. Cauchy-Schwarz and the triangle ledger deliberately forget cancellation among different divisor ancestors. Even a shell satisfying (6) may contribute very little to `G_N` after divisor convolution.

Second, sparse exceptional blocks do not evade the condition. For fixed weighted `l^1` contribution, concentrating the mass on fewer `q` only increases the second moment required by Cauchy-Schwarz. The broad-occupancy configuration is the cheapest possible way to satisfy the ledger.

Third, the positive lag in (27) is not a fixed universal lag, and no global Chowla violation is asserted. It can depend on the shell and on `N`; moreover the aligned block mask is essential. A proof about ordinary unweighted correlations cannot be substituted without controlling the omitted boundary-crossing pairs.

Fourth, the diagonal term cannot itself create the near-capacity energy. It is at most `NQ`, whereas (25) is larger by `x^{2c-o(1)}`. Hence any near-capacity source variance genuinely requires positive off-diagonal correlation in aggregate.

Fifth, almost-all short-interval theorems do not automatically control these aligned starts. A sparse deterministic grid can, in principle, concentrate in a Lebesgue-exceptional set unless the theorem has the required uniformity or an additional sampling argument is supplied.

Finally, no RH assumption is needed for the forcing implication (6), the converse criterion (9)--(10), or the correlation consequence (27). RH is relevant only when comparing the demanded variance with the current RH-calibrated surrounding framework and with pointwise Mertens envelopes.

## Consequences for the research line

FD-299 removed sign polarization as an independent near-capacity escape under RH. FD-300 now isolates the **magnitude** problem one step further upstream:

\[
\boxed{
L_N(x)\text{ near capacity}
\Longrightarrow
\text{aligned block-Mertens RMS }
\ge N^{1/2}x^{c-o(1)}.
}
\tag{38}
\]

Therefore the next useful attack need not start with the divisor convolution itself. A uniform aligned-block second-moment upper bound with any fixed power saving past the threshold (9) would decisively kill the low-height near-capacity `G_N` route. Conversely, if numerical or theoretical work indicates that (6) can actually occur, (27) says where the arithmetic anomaly must be visible: a positive, growing-period, same-block Möbius two-point bias of strength at least `x^{2c-o(1)}/N` on some dyadic denominator shell.

This leaves a sharper fork than the raw question `how large can L_N be?`: either prove source variance below `N x^{2c}` on every shell, or explain how the aligned Möbius blocks sustain the variance inflation and masked positive correlation forced above.