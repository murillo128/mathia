# FD-209 — Common sublogarithmic dyadic depth remains RH-complete on scale windows

- **Date:** 2026-09-19
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** growing-depth dyadic inversion / scale-window RH criterion / exact binary-prefix Green kernel / route restriction
- **Depends on:** FD-206, FD-207, FD-208
- **Classification:** `EXACT-DERIVED + UNIFORM-SUBLOG-INVERSION + SCALE-WINDOW-RH-EQUIVALENCE + NEGATIVE-BINOMIAL-GREEN-KERNEL + ROUTE-RESTRICTION`

## Claim

`FD-208` leaves sublogarithmic growing depth as the only power-critical opening inside the binomial dyadic-difference family

\[
\Delta(n):=M(2n)-M(n),
\qquad
\mathcal C_q(n):=(T-I)^q\Delta(n),
\qquad
(TF)(n):=F(2n).
\tag{1}
\]

It also notes two possible reasons why the fixed-depth inversion of `FD-207` might fail when `q` grows: the inversion constants depend on `q`, and a diagonal hypothesis on `C_(q(n))(n)` does not supply one common depth on all binary prefixes.

The first issue is not a genuine escape anywhere inside the sublogarithmic window. The fixed-depth inverse admits an exact binary-prefix Green kernel whose total amplification is only exponential in `q`, while all floor/odd-step remainders have subpower combinatorial mass whenever `q=o(log N)`.

More precisely, let `q=q(X)` be any source-independent integer-valued function satisfying

\[
q(X)=o(\log X),
\tag{2}
\]

and put `Q(X):=q(X)+1`. Then the following scale-window criterion is equivalent to RH:

\[
\boxed{
\mathrm{RH}
\iff
\forall\varepsilon>0:\quad
|\mathcal C_{q(X)}(n)|
\ll_\varepsilon
X^\varepsilon n^{1/2}
\quad
\left(\frac{\sqrt X}{2}\le n\le X\right).
}
\tag{3}
\]

The implied constant may depend on `epsilon` and on the chosen depth function, but not on `X` or `n`.

Thus `q` may tend to infinity arbitrarily inside the full `o(log X)` window identified by `FD-208`. If one common depth is controlled across each square-root scale window, growing the depth does **not** lower the theorem surface: the estimate is still RH-equivalent.

The quantitative inverse behind (3) is explicit. Let

\[
F_s(n):=(T-I)^sM(n),
\tag{4}
\]

so that

\[
F_{q+1}(n)=\mathcal C_q(n).
\tag{5}
\]

For a target integer `N`, write

\[
n_t:=\left\lfloor\frac{N}{2^t}\right\rfloor,
\qquad
0\le t\le L:=\lfloor\log_2N\rfloor.
\tag{6}
\]

For every fixed truncation depth `Q<=L`, one has the exact expansion

\[
\boxed{
F_0(N)
=
\sum_{s=0}^{Q-1}\binom Ls F_s(1)
+
\sum_{t=Q}^{L}\binom{t-1}{Q-1}F_Q(n_t)
+
\mathcal E_{N,Q},
}
\tag{7}
\]

with the source-independent error bound

\[
\boxed{
|\mathcal E_{N,Q}|
\le
\sum_{s=0}^{Q-1}3^s\binom L{s+1}.
}
\tag{8}
\]

Moreover

\[
|F_s(1)|\le3^s,
\qquad
|F_Q(m)|\le3^Qm.
\tag{9}
\]

If, on the upper half of the binary scale range,

\[
|F_Q(m)|\le A_Nm^{1/2}
\qquad
\left(\frac{\sqrt N}{2}\le m\le N\right),
\tag{10}
\]

then (7) gives

\[
\boxed{
|M(N)|
\le
A_NN^{1/2}(1+\sqrt2)^Q
+
N^{1/2}\exp\!\bigl(o(\log N)\bigr)
}
\tag{11}
\]

uniformly whenever `Q=o(log N)`. In particular, if `A_N=N^{o(1)}` and `q=o(log N)`, then

\[
\boxed{M(N)=N^{1/2+o(1)}.}
\tag{12}
\]

The key research consequence is therefore sharper than the boundary in `FD-208`. The exponentially growing Delannoy random tariff does leave a sublogarithmic power-critical window, but the **inversion constants themselves remain subpower throughout exactly that same window**. A common-depth pointwise estimate on scale windows is still destination-complete.

What remains genuinely outside the theorem is narrower: a diagonal estimate in which only `C_(q(n))(n)` is available and the depth changes along the binary ancestor chain, or a collective signed estimate that never yields a common-depth pointwise bound on a square-root window. Those are now the only live forms of the growing-depth escape inside the binomial `(T-I)^q` family.

## 1. Exact binary-prefix recurrence for every difference level

The identity

\[
F_{s+1}(n)=F_s(2n)-F_s(n)
\tag{13}
\]

implies

\[
F_s(2n)=F_s(n)+F_{s+1}(n).
\tag{14}
\]

The only complication along an arbitrary binary prefix is an odd child. Define

\[
\eta_s(n):=F_s(2n+1)-F_s(2n).
\tag{15}
\]

Expanding (4),

\[
F_s(x)
=
\sum_{j=0}^{s}(-1)^{s-j}\binom sj M(2^jx).
\tag{16}
\]

For each `j`, the arguments in the odd-child difference differ by exactly `2^j`:

\[
2^j(2n+1)-2^{j+1}n=2^j.
\]

Since `M(b)-M(a)` is a sum of `mu` over an interval of length `b-a` and `|mu|<=1`,

\[
|M(2^j(2n+1))-M(2^{j+1}n)|\le2^j.
\]

Hence

\[
\boxed{
|\eta_s(n)|
\le
\sum_{j=0}^{s}\binom sj2^j
=3^s.
}
\tag{17}
\]

This is uniform in `s`; no fixed-depth constant is hidden.

Now write the exact binary relation between consecutive ancestors in (6) as

\[
n_t=2n_{t+1}+b_t,
\qquad b_t\in\{0,1\}.
\tag{18}
\]

Combining (14)--(18),

\[
\boxed{
F_s(n_t)
=
F_s(n_{t+1})
+
F_{s+1}(n_{t+1})
+b_t\eta_s(n_{t+1}).
}
\tag{19}
\]

This two-dimensional recurrence is the growing-depth version of the one-step inversion used in `FD-207`.

## 2. Path counting gives the exact Green kernel

Ignore the last term of (19) momentarily. Every binary-parent step either keeps the difference level `s` or raises it by one. Starting from `(s,t)=(0,0)`, the number of paths that first reach level `Q` at parent depth `t` is

\[
\binom{t-1}{Q-1}.
\tag{20}
\]

Paths that never reach `Q` before the terminal ancestor `n_L=1` arrive there at level `s<Q` with multiplicity

\[
\binom Ls.
\tag{21}
\]

Restoring the odd-child terms gives (7). An error inserted at parent depth `t` and difference level `s` can be reached in at most `binom(t,s)` ways. Summing over all parent depths and using the hockey-stick identity,

\[
\sum_{t=s}^{L-1}\binom ts
=
\binom L{s+1},
\tag{22}
\]

while (17) contributes at most `3^s` per occurrence. This proves (8).

The terminal values are also uniformly harmless. From `|M(x)|<=x`,

\[
|F_s(1)|
\le
\sum_{j=0}^{s}\binom sj2^j
=3^s,
\tag{23}
\]

and, more generally,

\[
|F_Q(m)|
\le
m\sum_{j=0}^{Q}\binom Qj2^j
=3^Qm.
\tag{24}
\]

Equations (7)--(8) are therefore a completely source-valid inversion formula. They use only the physical bounded increments of the Möbius summatory function; no abstract coefficient-space extremizer is invoked.

## 3. Square-root data are amplified only by `(1+sqrt(2))^Q`

Let

\[
T_0:=\left\lfloor\frac L2\right\rfloor.
\tag{25}
\]

For `t<=T_0`, the ancestor `n_t` lies in the square-root window of (10), up to the harmless factor `1/2`. Also

\[
n_t\le N2^{-t}.
\tag{26}
\]

The part of the Green sum in (7) coming from `Q<=t<=T_0` is therefore at most

\[
A_NN^{1/2}
\sum_{t=Q}^{\infty}
\binom{t-1}{Q-1}2^{-t/2}.
\tag{27}
\]

The standard negative-binomial generating identity

\[
\sum_{t=Q}^{\infty}\binom{t-1}{Q-1}z^t
=
\left(\frac{z}{1-z}\right)^Q
\tag{28}
\]

with `z=2^(-1/2)` gives

\[
\boxed{
\sum_{t=Q}^{\infty}
\binom{t-1}{Q-1}2^{-t/2}
=(1+\sqrt2)^Q.
}
\tag{29}
\]

This is the actual critical-scale amplification of the inverse. In particular,

\[
Q=o(\log N)
\quad\Longrightarrow\quad
(1+\sqrt2)^Q=N^{o(1)}.
\tag{30}
\]

The fixed-depth constant from `FD-207` therefore remains subpower over the **entire** sublogarithmic regime, not merely for `q=O(log log N)`.

## 4. Small ancestors, terminal data and odd steps are also subpower

For the lower half of the ancestor chain, `t>T_0`, use the trivial bound (24). Since `binom(t-1,Q-1)<=binom(L,Q-1)`,

\[
\begin{aligned}
&\sum_{t>T_0}
\binom{t-1}{Q-1}|F_Q(n_t)|\\
&\qquad\le
3^QN\binom L{Q-1}
\sum_{t>T_0}2^{-t}\\
&\qquad\ll
N^{1/2}3^Q\binom L{Q-1}.
\end{aligned}
\tag{31}
\]

The boundary and odd-step contributions from (7)--(8) are bounded by

\[
\sum_{s=0}^{Q-1}3^s
\left(
\binom Ls+inom L{s+1}
\right).
\tag{32}
\]

When `Q=o(L)`, the elementary estimate

\[
\binom LQ\le\left(\frac{eL}{Q}\right)^Q
\tag{33}
\]

shows

\[
\log\!\left(3^Q\binom LQ\right)
\le
Q\log3+Q\log\frac{eL}{Q}
=o(L).
\tag{34}
\]

Indeed, if `x=L/Q -> infinity`, then

\[
\frac{Q\log(L/Q)}{L}
=
\frac{\log x}{x}
\to0.
\tag{35}
\]

The finite sum in (32) has the same subpower size. Since `L=Theta(log N)`, all contributions in (31)--(32) are `N^(1/2+o(1))` or smaller. Combining them with (29) proves (11)--(12).

This calculation identifies where the apparent nonuniformity of the repeated fixed-depth argument went: the correct path count contains factorial suppression through binomial coefficients. A crude bound such as `(log N)^q` loses that structure and would falsely suggest a much narrower inversion window.

## 5. RH implies the same growing-depth window estimate

Assume RH. By the classical Littlewood--Mertens criterion, for every `delta>0`,

\[
M(x)=O_\delta(x^{1/2+\delta}).
\tag{36}
\]

Since `F_Q=C_q`, the binomial expansion gives

\[
\begin{aligned}
|\mathcal C_q(n)|
&\le
C_\delta n^{1/2+\delta}
\sum_{j=0}^{Q}\binom Qj2^{j(1/2+\delta)}\\
&=
C_\delta n^{1/2+\delta}
\left(1+2^{1/2+\delta}\right)^Q.
\end{aligned}
\tag{37}
\]

For `sqrt(X)/2<=n<=X` and `Q=o(log X)`, the final factor is `X^(o(1))`. Given any `epsilon>0`, choose `delta` sufficiently smaller than `epsilon`; for all sufficiently large `X`, (37) is bounded by

\[
X^\varepsilon n^{1/2}
\]

up to a constant depending only on `epsilon` and the chosen depth function. This proves the forward implication in (3).

Conversely, assume the right-hand side of (3). Apply (11) with `N=X`, `A_N<<_epsilon N^epsilon`, and `Q=o(log N)`. Given any target exponent `eta>0`, use (3) with a sufficiently smaller `epsilon`; the factors in (30)--(35) are `N^(o(1))`, so

\[
M(N)=O_\eta(N^{1/2+\eta}).
\tag{38}
\]

The Littlewood--Mertens criterion then gives RH. This proves (3).

## 6. Interaction with the FD-208 random budget

`FD-208` proves for the squarefree Rademacher multiplicative comparator that

\[
\mathbb E|\mathcal C_q^f(n)|^2
=
\frac6{\pi^2}nD_q+O(n^{1/2}D_q),
\qquad
D_q=\sum_{j=0}^{q}\binom qj^22^j,
\tag{39}
\]

uniformly in `q`, and that

\[
D_{q(X)}=X^{o(1)}
\iff
q(X)=o(\log X).
\tag{40}
\]

Therefore the exact same depth window has two simultaneous properties:

1. its random-multiplicative surcharge and largest Farey observation span are only subpower (`FD-208`);
2. its common-depth binary-prefix inverse has only subpower amplification (the present finding).

So there is no intermediate sublogarithmic range in which the binomial observable has kept its critical random power scale but escaped RH-completeness merely because the fixed-depth inversion constants became too large.

For `q=O(log log X)`, the random surcharge is only polylogarithmic. The inverse factor `(1+sqrt(2))^Q` is likewise polylogarithmic. The remaining terminal/odd-step terms can be larger than a fixed polylogarithm under the crude combinatorial bound above, but they are still `X^(o(1))` and therefore irrelevant to the RH power exponent. No sharper polylogarithmic theorem is claimed here.

## 7. Farey representation audit and the remaining loophole

The scale-window criterion is still Farey-native in exactly the sense established by `FD-206--208`. For each `n` and common depth `q=q(X)`,

\[
\mathcal C_q(n)
=
\sum_{j=0}^{q}(-1)^{q-j}\binom qj
S_{2,H_{2^jn}}(p_{2^jn}),
\tag{41}
\]

where `H_m=mp_m` and `p_m` is the largest prime at most `m`. Every horizon and prime is determined by the scale, not by observed Möbius values. When `q=o(log X)` and `n<=X`, the largest horizon in (41) differs from the base `Theta(X^2)` scale by only `X^(o(1))`, exactly as priced in `FD-208`.

The result does **not** convert an arbitrary diagonal hypothesis

\[
|\mathcal C_{q(n)}(n)|\le n^{1/2+o(1)}
\tag{42}
\]

into RH. Formula (7) needs one common terminal difference level `Q` across the binary ancestors used in the inverse. Hypothesis (42) supplies different rows at those ancestors and cannot simply be substituted into the Green kernel.

This distinction is now the precise remaining opening. The issue is no longer growth of the inversion constants: those are subpower throughout the full comparator-critical window. The issue is **depth coherence across scales**. A genuine escape must exploit scale-dependent depth strongly enough that no common sublogarithmic row is controlled on a square-root window, or it must use a collective signed relation that does not imply such pointwise control.

The representation boundary is also explicit. Equation (7) is a physical identity for the actual Mertens function and its dyadic differences. No claim is made that arbitrary coefficient-space sequences can be realized by Farey data. The random multiplicative source appears only in the separate comparator statement (39)--(40).

## 8. Prior art and falsification boundary

Repeated finite differences, repeated summation, and the negative-binomial kernel in (28) are standard discrete-calculus facts. A targeted literature search for dyadic/dilation differences of the Mertens function and growing-order Mertens criteria did not identify a theorem matching the scale-window criterion (3). No novelty is claimed for the combinatorial identities themselves.

No new external theorem is load-bearing. The RH equivalence uses the same classical Littlewood--Mertens criterion already anchored in `SOURCES.md`; the rest of the proof is the exact recurrence (19), elementary path counting, `|mu|<=1`, and standard binomial estimates. `SOURCES.md` therefore requires no change.

The theorem would be falsified by any source-valid example for which one common `q=o(log X)` obeys the critical estimate on the whole square-root window but `M(X)` has a fixed power excess above `sqrt(X)`. Equations (7)--(35) exclude such an example directly. They do not exclude a construction satisfying only the diagonal varying-depth condition (42).

No clue status changes. The accepted local clues concern separate Farey-order/Jordan mechanisms. No formalization handoff is opened: the finite recurrence and path count are elementary; the live mathematical question is now the coherence or aggregation of scale-varying depths.

## Conclusion

The sublogarithmic window exposed by `FD-208` is real on the random-cost side, but it is **not** a window in which the fixed-depth inverse becomes power-expensive. For every source-independent common depth `q(X)=o(log X)`, critical pointwise control of `C_(q(X))` across the square-root scale window is RH-equivalent. The exact binary-prefix Green kernel amplifies square-root data by only `(1+sqrt(2))^(q+1)=X^(o(1))`, and all odd-step and terminal terms also have subpower mass.

This closes the inversion-constant branch of the `FD-208` frontier. Inside the binomial dyadic family, the remaining possible escape is specifically **depth incoherence or nonpointwise aggregation**, not merely letting the number of signed root differences grow.