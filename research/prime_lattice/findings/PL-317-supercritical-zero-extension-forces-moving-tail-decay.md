# PL-317 — Supercritical zero-extension Sobolev regularity forces moving-tail decay

**Evidence:** `LITERATURE+DERIVED + EXACT-SUFFICIENT-REGULARITY`

**Status:** `SUPERCRITICAL-SUFFICIENT + CRITICAL-SHARP-WITHIN-SOBOLEV-SCALE + ACTUAL-BRANCH-REGULARITY-OPEN`

## Precise claim

Let

\[
Q(x)=-\log\frac{1-x}{2},\qquad x(Q)=1-2e^{-Q},
\]

and let a physical endpoint mismatch be written as

\[
f(x)=m(Q(x)),\qquad -1<x<1.
\]

Assume that the zero extension `Ef` of `f` to `R` belongs to

\[
H^{1/2+\eta}(\mathbb R)
\]

for some `eta>0`. Then for every

\[
0<\beta<\min\{\eta,1/2\}
\]

there is a constant `C_beta` such that

\[
\boxed{|m(Q)|\le C_\beta e^{-\beta Q}\qquad(Q\ge0).}
\tag{PL317-1}
\]

Consequently

\[
m\in L^1(0,\infty),
\qquad
\boxed{Qm(Q)\longrightarrow0,}
\tag{PL317-2}
\]

and, at the moving Green observation scale of `PL-314`,

\[
\boxed{
\frac{|m(r/s)|}{s}
\le C_\beta 2^\beta s^{-1}e^{-\beta r/s}
\longrightarrow0
}
\qquad(s\downarrow0)
\tag{PL317-3}
\]

for each fixed `r>0`.

Therefore the sufficient tail theorem of `PL-314` applies:

\[
\boxed{
\mathcal A_s[m](r)
\longrightarrow
 e^{-r}\int_0^\infty m(Q)\,dQ.
}
\tag{PL317-4}
\]

Combined with `PL-316`, this locates an exact generic boundary in the zero-extension Sobolev scale for the moving-diagonal problem:

\[
H^{1/2}(\mathbb R)
\quad\text{is insufficient, while every}\quad
H^{1/2+\eta}(\mathbb R),\ \eta>0,
\quad\text{is sufficient.}
\tag{PL317-5}
\]

The statement is a sufficiency threshold for this route, not a necessity theorem for Green transfer and not a regularity theorem for the actual completed-Weil mismatch.

## 1. Fractional Morrey regularity supplies a boundary trace

Fix `beta` with

\[
0<\beta<\min\{\eta,1/2\}.
\]

The Sobolev nesting

\[
H^{1/2+\eta}(\mathbb R)
\hookrightarrow
H^{1/2+\beta}(\mathbb R)
\]

puts `Ef` in a fractional Sobolev space of order strictly between `1/2` and `1`. For `0<t<1`, the Bessel-potential space `H^t(R)` agrees with `W^{t,2}(R)` up to equivalent norms. The one-dimensional fractional Morrey embedding then gives a Hölder representative

\[
Ef\in C^{0,\beta}(\mathbb R)
\]

with

\[
|Ef(x)-Ef(y)|\le C_\beta |x-y|^\beta.
\tag{PL317-6}
\]

A standard source is Eleonora Di Nezza, Giampiero Palatucci and Enrico Valdinoci, *Hitchhiker's guide to the fractional Sobolev spaces*, *Bulletin des Sciences Mathématiques* **136**(5) (2012), 521--573, DOI `10.1016/j.bulsci.2011.12.004`; Theorem 8.2 gives `W^{t,p}->C^{0,(tp-n)/p}` when `tp>n`, which here yields exponent `beta` for `n=1`, `p=2`, `t=1/2+beta`.

Because `Ef=0` almost everywhere on the open half-line `(1,infinity)` and its Hölder representative is continuous, that representative is identically zero there and hence

\[
Ef(1)=0.
\tag{PL317-7}
\]

This is the decisive difference from the critical space in `PL-316`: strictly more than half a derivative produces an actual continuous zero boundary trace rather than only an integrable critical Hardy interaction.

## 2. The logarithmic endpoint coordinate amplifies Hölder decay to exponential tail decay

For `Q>=0`,

\[
1-x(Q)=2e^{-Q}.
\]

Using (PL317-6)--(PL317-7),

\[
|m(Q)|
=|Ef(x(Q))-Ef(1)|
\le C_\beta |1-x(Q)|^\beta
=C_\beta 2^\beta e^{-\beta Q},
\]

which is (PL317-1). In particular `m` is integrable at infinity and bounded on compact `Q`-intervals, so `m in L^1(0,infinity)`. The exponential bound also gives

\[
Q|m(Q)|\le C_\beta 2^\beta Qe^{-\beta Q}\to0,
\]

proving (PL317-2).

At the Green diagonal `Q=r/s`, the same estimate gives (PL317-3). Thus the source-independent Sobolev gain does more than imply the sufficient `PL-314` envelope: it directly suppresses the precise moving sample that the diagonal atom sees.

## 3. Transfer to the finite-s Green problem

`PL-314` proves that

\[
m\in L^1(dQ),\qquad Qm(Q)\to0
\]

is sufficient for the rank-one limit (PL317-4). The hypotheses have just been derived from zero-extension `H^{1/2+eta}` regularity, so no additional weak-convergence interchange or shrinking-neighborhood claim is needed.

The result therefore closes the generic supercritical Sobolev side of the endpoint-matching gate left open by `PL-316`. A proof that the actual completed-Weil physical mismatch lies in any fixed `H^{1/2+eta}(R)` would automatically provide the moving-tail suppression needed to pass from the finite-`s` Green transfer to the scalar endpoint moment of `PL-313`.

## Prior-art and novelty audit

The analytic input is classical. Fractional Sobolev--Morrey embedding above `sp=n` is standard, and the cited Di Nezza--Palatucci--Valdinoci theorem supplies an explicit modern reference. The fact that a globally Hölder zero extension vanishes at the boundary is immediate. Neither is a Mathia discovery.

A targeted literature check for this standard embedding combined with the specific small-order fractional Green moving-diagonal scaling `Q=r/s` did not locate an external theorem packaging the line-specific consequence. Search absence is not used as a novelty claim. The durable delta is the exact combination with `PL-314`--`PL-316`: in the logarithmic endpoint coordinate, any positive Sobolev gain beyond `1/2` becomes exponential `Q`-decay, while the endpoint space `H^{1/2}` still admits the sparse order-one moving-diagonal obstruction.

Thus `1/2` is sharp here only in the following controlled sense: it is the boundary between failure and automatic success of this **generic zero-extension Sobolev sufficient-condition strategy**. No claim is made that `H^{1/2+eta}` is necessary for the Green limit, or that this threshold has independent Riemann-zero significance.

## Adversarial controls and boundaries

1. `PL-317` does not prove that the actual completed-Weil mismatch has supercritical Sobolev regularity. Establishing such a gain from the eigen-equation remains open.
2. The result does not make `H^{1/2+eta}` necessary. Critical Besov/Dini refinements, monotone or one-sided tails, asymptotic expansions, or direct moving-sample estimates may be strictly weaker sufficient conditions.
3. The conclusion depends on **zero-extension** regularity on `R`. Interior `H^{1/2+eta}(-1,1)` without the corresponding boundary trace condition does not by itself force `f(1)=0` and therefore does not imply (PL317-1).
4. The critical negative control is exact: `PL-316` constructs zero extensions in `H^{1/2}(R)` with arbitrarily small norm for which `Q_n m(Q_n)=r` at sparse `Q_n=r/s_n` and the normalized Green transfer remains order one. Hence no norm-smallness argument at the endpoint can substitute for the strict regularity gain.
5. Nothing here supplies the rational-prime-specific sign/localization step. Once the moving-tail gate is stable, the arithmetic problem is still the source-selected endpoint balance identified after `PL-313`.

## Consequence for the research line

The generic Sobolev question is now sharply separated from the source-specific one. There is no need to search for progressively stronger unnamed global regularity classes between the already-failed critical endpoint and an arbitrary positive Sobolev gain: any fixed gain `eta>0` is enough by the classical Hölder trace mechanism.

The remaining load-bearing question is therefore concrete: **does the actual completed-Weil eigen-equation force any supercritical zero-extension gain, or some weaker source-structured substitute such as `m(Q)=o(1/Q)` or a direct estimate of `m(r/s)/s`?** If not, broad Sobolev regularity has been exhausted as a route to the corner reduction, and the proof must use a genuinely source-specific tail law.