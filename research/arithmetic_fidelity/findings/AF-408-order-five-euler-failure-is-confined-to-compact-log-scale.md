# AF-408 — Order-five Euler failure is confined to compact log scale

## Status

`EXACT-DERIVED` · `FINITE-ORDER-POSITIVE-GATE` · `ARITHMETIC-FIDELITY` · `TOTAL-POSITIVITY` · `CONFLUENT-CERTIFICATE` · `TODA` · `ASYMPTOTIC-RIGIDITY` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
L(x):=-\log(1-e^{-x}),\qquad x>0,
\]

and

\[
f(t):=L(e^t).
\]

For the oriented confluent determinants

\[
H_m(t):=(-1)^{m(m-1)/2}
\det\bigl(f^{(i+j)}(t)\bigr)_{i,j=0}^{m-1},
\]

write, as in AF-404,

\[
q:=-(\log f)'',
\qquad
R_m:=\frac{H_m}{f^m}.
\]

AF-405 proves

\[
R_3(t)>0,\qquad R_4(t)>0
\qquad(t\in\mathbb R).
\]

The next Toda gate is therefore

\[
A_4(t):=4q(t)-(\log R_4(t))'',
\]

because AF-404 gives

\[
R_5R_3=R_4^2A_4.
\]

Hence `H_5` has the same sign as `A_4`.

The order-five gate is **strictly positive in both asymptotic tails**. More precisely:

1. as `t\to-\infty`, with `x=e^t` and `u=-t=-\log x`,

\[
\boxed{
A_4(t)=\frac{24}{5}x^2\bigl(1+o(1)\bigr)
=\frac{24}{5}e^{2t}\bigl(1+o(1)\bigr)>0;
}
\tag{1}
\]

2. as `t\to+\infty`, with `x=e^t` and `y=e^{-x}`,

\[
\boxed{
A_4(t)=4x\bigl(1+o(1)\bigr)
=4e^t\bigl(1+o(1)\bigr)>0.
}
\tag{2}
\]

Consequently there exists `T>0` such that

\[
\boxed{
H_5(t)>0\qquad(|t|>T).
}
\tag{3}
\]

Thus, if the full Euler-log kernel first fails strict total positivity at order five, the failure cannot escape to either logarithmic tail. Any order-five counterexample must pass through a **compact interior scale window** where the scalar curvature gate `A_4` changes sign or vanishes.

AF-217 still proves that some finite order eventually fails, while AF-405 proves success through order four. AF-408 does **not** prove order-five positivity globally; it removes both asymptotic tails from the possible order-five failure mechanism.

## Left-tail derivation

Put

\[
x=e^t,\qquad u=-t=-\log x,
\]

so `x\downarrow0` and `u\to\infty`. The Euler-log profile has the classical local expansion

\[
f(t)=L(x)
=u+\frac{x}{2}-\frac{x^2}{24}+O(x^4).
\tag{4}
\]

When a coefficient is viewed as a function of the formal variables `(x,u)`, differentiation in `t` acts as

\[
\mathcal D:=\frac d{dt}=x\partial_x-\partial_u.
\tag{5}
\]

Expanding `q=-\mathcal D^2\log f` from `(4)` gives

\[
\begin{aligned}
q={}&\frac1{u^2}
-x\left(\frac1{2u}+\frac1{u^2}+\frac1{u^3}\right)\\
&+x^2\left(
\frac1{6u}+\frac2{3u^2}+\frac{13}{12u^3}+\frac3{4u^4}
\right)
+O\!\left(\frac{x^3}{u^2}\right).
\end{aligned}
\tag{6}
\]

Using the normalized Toda recursion of AF-404,

\[
R_{m+1}R_{m-1}
=R_m^2\left(mq-(\log R_m)''\right),
\tag{7}
\]

one obtains successively

\[
R_3
=\frac{x}{2u^3}
-x^2\left(\frac2{3u^3}+\frac3{4u^4}\right)
+O\!\left(\frac{x^3}{u^2}\right),
\tag{8}
\]

and

\[
R_4
=\frac{x^3}{3u^4}
\left[
1-\frac{2x}{u}
+x^2\left(
-\frac65+\frac1{6u}+\frac5{2u^2}
\right)
+O(x^3)
\right].
\tag{9}
\]

The `O(x^3)` in `(9)` is uniform for `u>=1`; the coefficients generated from `(4)` are rational functions of `u` bounded there. Taking the logarithm,

\[
\begin{aligned}
\log R_4={}&3\log x-\log3-4\log u-\frac{2x}{u}\\
&+x^2\left(
-\frac65+\frac1{6u}+\frac1{2u^2}
\right)
+O(x^3).
\end{aligned}
\tag{10}
\]

The important point is that the apparent leading curvature cancels **exactly** against `4q`. Applying `\mathcal D^2` to `(10)` gives

\[
\begin{aligned}
(\log R_4)''={}&\frac4{u^2}
-x\left(\frac2u+\frac4{u^2}+\frac4{u^3}\right)\\
&+x^2\left(
-\frac{24}{5}
+\frac2{3u}+\frac8{3u^2}+\frac{13}{3u^3}+\frac3{u^4}
\right)
+O(x^3u^0).
\end{aligned}
\tag{11}
\]

while four times `(6)` is

\[
\begin{aligned}
4q={}&\frac4{u^2}
-x\left(\frac2u+\frac4{u^2}+\frac4{u^3}\right)\\
&+x^2\left(
\frac2{3u}+\frac8{3u^2}+\frac{13}{3u^3}+\frac3{u^4}
\right)
+O\!\left(\frac{x^3}{u^2}\right).
\end{aligned}
\tag{12}
\]

Subtracting `(11)` from `(12)` leaves

\[
A_4(t)=\frac{24}{5}x^2+o(x^2),
\tag{13}
\]

which proves `(1)`.

A longer algebraic expansion, useful only as an audit check, begins

\[
A_4(t)
=\frac{24}{5}x^2
-\frac{32}{5}x^3
+\left(\frac45u+\frac{1686}{175}\right)x^4
-\frac{328}{21}x^5+\cdots.
\tag{14}
\]

Because `u=-\log x`, every displayed correction in `(14)` is lower order than the positive `x^2` term.

## Right-tail derivation

Now let `x=e^t\to\infty` and put

\[
y=e^{-x}.
\]

Then

\[
f(t)
=y+\frac{y^2}{2}+\frac{y^3}{3}+O(y^4),
\tag{15}
\]

so

\[
\log f
=-x+\frac y2+\frac5{24}y^2+O(y^3).
\tag{16}
\]

Here `d/dt=x\,d/dx` and `y'=-xy`. Direct substitution into the same Toda recursion gives

\[
q
=x+\left(-\frac{x^2}{2}+\frac x2\right)y
+O(x^2y^2),
\tag{17}
\]

\[
R_3
=2x^3+\left(\frac{x^5}{2}-5x^4+4x^3\right)y
+O(x^5y^2),
\tag{18}
\]

and

\[
R_4
=12x^6
+\left(-x^9+21x^8-102x^7+66x^6\right)y
+O(x^{10}y^2).
\tag{19}
\]

Therefore

\[
\begin{aligned}
A_4(t)
={}&4x\\
&+xy\left(
\frac{x^4}{12}-\frac{7x^3}{3}+18x^2-40x+16
\right)
+O(x^8y^2).
\end{aligned}
\tag{20}
\]

Since every polynomial factor is dominated by `e^x`, `(20)` yields

\[
A_4(t)=4x(1+o(1)),
\tag{21}
\]

which proves `(2)`.

## From the scalar gate to the fifth confluent determinant

AF-404 at `m=4` gives

\[
R_5R_3=R_4^2A_4.
\tag{22}
\]

AF-405 proves `R_3,R_4>0` globally. Since also `f>0`, equations `(1)` and `(2)` imply `R_5>0`, hence `H_5=f^5R_5>0`, in both tails. Continuity then provides a finite `T` for `(3)`.

This is stronger than merely observing numerically that the fifth determinant appears positive at large `|t|`: the tail signs and their leading margins are forced analytically by the Euler profile and the Toda normalization.

## Arithmetic-fidelity interpretation

The compression target here is finite-order ordered-sign fidelity of the full Euler-log observation kernel. AF-403 and AF-404 compress arbitrary node-placement tests first to a confluent flag and then to a scalar Toda curvature hierarchy. AF-405 certifies the hierarchy through order four. AF-408 shows that the **next possible loss of fidelity is not an asymptotic-resolution effect** at either endpoint of the logarithmic scale.

At `t\to-\infty`, substantial cancellations occur: the leading curvature of `R_4` reproduces `4q` through orders `1` and `x`, and the first surviving discriminator is the positive `24x^2/5` term. At `t\to+\infty`, the first Euler harmonic dominates and leaves the much larger margin `4e^t(1+o(1))`.

Thus an order-five failure, if present, must be an **interior interaction phenomenon** created where several Euler harmonics have comparable influence. That distinction matters for the line's general compression program: a globally lost property need not fail where information is coarsest asymptotically; it can survive both degenerate limits and be destroyed only in the intermediate regime where discarded components interact.

No rational-prime discriminator is produced by this theorem. The result is a property of the universal one-generator Euler-log kernel. Any RH-facing consequence still requires a separate arithmetic source theorem, exactly as in AF-405.

## Prior-art and novelty audit

The Toda/Hankel identity and the reduction of successive confluent determinants to nested log-concavity are classical and already audited in AF-404. The globalization from complete confluent flags to translation-kernel total positivity is classical ECT/total-positivity theory and is already audited in AF-403. AF-405 supplies the line-specific global positivity through order four.

A fresh structural search for combinations of the Euler-log profile, total positivity, Pólya-frequency kernels, Hankel determinants, and Toda/log-concavity did not identify an established theorem giving this concrete order-five tail localization. The nearby literature remains general total-positivity/Pólya-frequency theory or general Hankel/Toda machinery rather than this exact Euler-log scalar gate. No novelty claim is made: `(1)`--`(21)` are an elementary asymptotic specialization of the already-classical Toda representation to Mathia's concrete Euler profile.

## Boundaries and falsification checks

- AF-408 proves only **eventual** order-five positivity in each tail. It supplies no explicit optimal cutoff `T` and no sign theorem on the remaining compact interval.
- A positive tail asymptotic cannot be promoted to global `STP_5`. One zero or negative value of `A_4` in the interior would kill the fifth confluent flag and, by coalescence, rule out strict order-five total positivity.
- Conversely, proving `A_4>0` on the compact remainder would certify `H_5>0` globally and, via AF-403, upgrade AF-405 from order four to order five.
- The result does not weaken AF-217. Some finite order still fails even if order five eventually turns out to succeed everywhere.
- The asymptotic expansions use the exact Euler profile, not a first-harmonic replacement. The right tail becomes first-harmonic dominated only as a proved asymptotic statement.
- The left-tail cancellation is sensitive to the full normalized Toda geometry. Keeping only `f(t)\sim -t` would make `R_3` and higher certificates degenerate and would miss the positive `24x^2/5` fifth-order margin.
- No numerical scan, finite precision sign check, or unproved zero-location statement is used in the theorem.

## Consequence for the research line

The immediate order-five problem is now compact rather than global in scale. The next useful step is to prove or refute

\[
A_4(t)=4q(t)-(\log R_4(t))''>0
\]

on the remaining bounded interval, preferably by an exact decomposition or a certified interval argument rather than by unconstrained sampling. If it is positive, the first possible bad order moves to six; if it fails, the first order-five witness is necessarily an interior multi-harmonic phenomenon rather than a tail degeneration.