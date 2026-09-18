# AF-420 — The critical derivative window has a sharp subthreshold absolute-resummation domain

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DOUBLE-SCALING` · `DERIVATIVE-SHIFT` · `CRITICAL-WINDOW` · `UNIFORM-TAIL` · `SCHUR-PIERI` · `SHARP-THRESHOLD` · `NO-NOVELTY-CLAIM`

## Claim

Continue AF-417--AF-419 with

\[
a=\frac{c^2}{4\pi^2}\ge0
\]

and the normalized exceptional-`1` Cauchy--Binet sector

\[
S_n^{(s)}(a)
=
\sum_{\ell(\lambda)\le n}
(-1)^{|\lambda|}
\left(\frac{a}{n^2}\right)^{|\lambda|}
s_\lambda(1^n)^2
R_{n,\lambda}^{(s)},
\tag{1}
\]

where

\[
R_{n,\lambda}^{(s)}
=
\prod_{i=1}^{n}
\left(\frac{k_i}{i}\right)^{s-1}
\frac{\zeta(2k_i)}{\zeta(2i)}
\left(\frac{2k_i-1}{2i-1}\right)^2,
\qquad
k_i=i+\lambda_{n+1-i}.
\tag{2}
\]

Let `s_n` be nonnegative integers with

\[
\frac{s_n}{n}\longrightarrow2.
\tag{3}
\]

For a fixed finite `A>0`, define the critical effective parameter

\[
b_n(A)
:=
A\,n^{\,s_n/n-2}.
\tag{4}
\]

If

\[
\boxed{
\limsup_{n\to\infty} b_n(A)<1,
}
\tag{5}
\]

then

\[
\boxed{
\sup_{0\le a\le A}
\left|
S_n^{(s_n)}(a)
-
\exp\!\left(-a e^{s_n/n}\right)
\right|
\longrightarrow0.
}
\tag{6}
\]

Thus AF-419's absolute resummation extends into the full `n/log n` critical window on a sharply delimited `a`-domain.

Writing

\[
\tau_n
=
\left(\frac{s_n}{n}-2\right)\log n,
\tag{7}
\]

if `tau_n -> tau` is finite, then `(6)` holds on every compact interval

\[
0\le a\le A<e^{-\tau}.
\tag{8}
\]

In particular, on the exact critical sequence `s_n=2n`,

\[
\boxed{
S_n^{(2n)}(a)\longrightarrow e^{-e^2 a}
}
\tag{9}
\]

uniformly for `a` in every compact subinterval of `[0,1)`, equivalently for `c` in every compact subinterval of `[0,2pi)`.

This threshold is sharp for the **absolute-uniform-integrability mechanism**. If `tau_n -> tau` and

\[
a e^\tau>1,
\tag{10}
\]

then the single full-height column `lambda=(1^n)` already has normalized absolute contribution growing exponentially. At the exact boundary `s_n=2n`, `a=1`, that one term grows linearly:

\[
\boxed{
\left|
\frac{T_{n,(1^n)}^{(2n)}}{T_{n,\varnothing}^{(2n)}}
\right|
\sim
\frac{24e^2}{\pi^2}\,n.
}
\tag{11}
\]

Therefore for `s_n=2n` the interval `a<1` is exactly the maximal open `a`-domain on which this absolute-tail architecture can prove the complete resummation. Equations `(10)`--`(11)` do **not** rule out signed cancellation at or beyond the threshold.

## 1. The effective critical coordinate comes from a full-height column

AF-418 showed that fixed partitions only see the coarse derivative-depth ratio `s_n/n`, while full-height rectangles retain the finer critical window `(7)`. For the first such rectangle, `lambda=(1^n)`, equation AF-418 gives exactly

\[
C_n(a)
:=
\left|
\frac{T_{n,(1^n)}^{(s_n)}}{T_{n,\varnothing}^{(s_n)}}
\right|
=
\left(\frac{a}{n^2}\right)^n
(n+1)^{s_n-1}
\frac{\zeta(2n+2)}{\zeta(2)}
(2n+1)^2.
\tag{12}
\]

When `s_n/n -> 2`,

\[
C_n(a)^{1/n}
=
a\,n^{s_n/n-2}(1+o(1)).
\tag{13}
\]

Hence the natural critical coordinate is not `a` or `s_n/n` separately but

\[
\boxed{
b_n(a)=a\,n^{s_n/n-2}=a e^{\tau_n}.
}
\tag{14}
\]

This immediately proves the exponential obstruction `(10)`.

For `s_n=2n` and `a=1`, `(12)` gives

\[
C_n(1)
=
n^{-2n}(n+1)^{2n-1}
\frac{\zeta(2n+2)}{\zeta(2)}
(2n+1)^2.
\tag{15}
\]

Using

\[
\left(1+\frac1n\right)^{2n-1}\to e^2,
\qquad
\zeta(2n+2)\to1,
\qquad
\zeta(2)=\frac{\pi^2}{6},
\]

one obtains `(11)`.

The remaining work is to prove the converse direction: below the threshold `b=1`, **every** growing partition is absolutely negligible except the bounded-complexity family already resummed by AF-417.

## 2. A polynomial-cost bound replaces the crude `9^{|lambda|}` factor near the boundary

Put

\[
P_{n,\lambda}
=
\prod_{i=1}^n\frac{k_i}{i}.
\tag{16}
\]

AF-419 used the elementary all-shape estimate

\[
R_{n,\lambda}^{(s)}
\le
9^{|\lambda|}P_{n,\lambda}^{\,s}.
\tag{17}
\]

That is appropriate below the critical ratio but is too expensive for a full-height column: `9^{|lambda|}` would move the true threshold by an artificial exponential factor.

The odd-distance product admits a sharper global comparison. Write

\[
O_{n,\lambda}
:=
\prod_{i=1}^n
\frac{2k_i-1}{2i-1}.
\]

Then

\[
\frac{O_{n,\lambda}}{P_{n,\lambda}}
=
\prod_{i=1}^n
\frac{2-1/k_i}{2-1/i}.
\tag{18}
\]

Since `k_i>=i`,

\[
\frac{2-1/k_i}{2-1/i}
=
1+
\frac{1/i-1/k_i}{2-1/i},
\]

and therefore

\[
\log\frac{2-1/k_i}{2-1/i}
\le
\frac1i.
\]

Consequently

\[
O_{n,\lambda}
\le
e^{H_n}P_{n,\lambda}
\le
e n\,P_{n,\lambda}.
\tag{19}
\]

The zeta ratio in `(2)` is at most one because `zeta(x)` decreases for real `x>1`. Equations `(2)` and `(19)` therefore give the boundary-adapted estimate

\[
\boxed{
0<R_{n,\lambda}^{(s)}
\le
e^{2H_n}P_{n,\lambda}^{\,s+1}
\le
e^2 n^2 P_{n,\lambda}^{\,s+1}.
}
\tag{20}
\]

The important point is that the extra cost in `(20)` is only polynomial in `n`; it is not exponential in the partition degree.

## 3. Column decomposition isolates the only critical family

Let

\[
h_m=\lambda'_m
\]

be the column heights. AF-419 proved the exact identity

\[
P_{n,\lambda}
=
\prod_{m\ge1}
\frac{n+m}{n-h_m+m}.
\tag{21}
\]

Fix once and for all

\[
\frac12<\eta<1.
\tag{22}
\]

Call a column tall when `h_m>eta n`. If there are `r>=1` tall columns, they are exactly `h_1,...,h_r`. Delete them and call the remaining partition `mu`.

Repeated Pieri multiplication by elementary symmetric functions gives the AF-419 dimension bound

\[
s_\lambda(1^n)
\le
s_\mu(1^n)
\prod_{m=1}^r\binom n{h_m}.
\tag{23}
\]

For the residual columns, `(21)` and `h_m<=eta n` imply

\[
P_{\mathrm{res}}
\le
\exp\!\left(
\frac{|\mu|}{(1-\eta)n}
\right).
\tag{24}
\]

Because `s_n/n -> 2`, for large `n`

\[
P_{\mathrm{res}}^{s_n+1}
\le
C_\eta^{|\mu|}
\tag{25}
\]

for a constant `C_eta` independent of `n` and `mu`.

Combining `(20)`, `(23)`--`(25)`, the absolute normalized weight of `lambda` is bounded by

\[
e^2n^2
\left(\frac{C_\eta a}{n^2}\right)^{|\mu|}
s_\mu(1^n)^2
\prod_{m=1}^r
B_{n,m}(h_m;a),
\tag{26}
\]

where

\[
B_{n,m}(h;a)
:=
\left(\frac{a}{n^2}\right)^h
\binom nh^2
\left(
\frac{n+m}{n-h+m}
\right)^{s_n+1}.
\tag{27}
\]

For fixed `h`, the last ratio decreases with `m`. Hence

\[
B_{n,m}(h;a)\le B_{n,1}(h;a).
\tag{28}
\]

The positive Schur Cauchy identity gives

\[
\sum_\mu
\left(\frac{C_\eta A}{n^2}\right)^{|\mu|}
s_\mu(1^n)^2
=
\left(1-\frac{C_\eta A}{n^2}\right)^{-n^2},
\tag{29}
\]

which is uniformly bounded for fixed `A`. Thus all tall-column control reduces to one scalar maximum,

\[
\varepsilon_n(A)
:=
\max_{\eta n<h\le n}
B_{n,1}(h;A).
\tag{30}
\]

## 4. Below `b=1`, the tall-column maximum decays exponentially

Put

\[
j=n-h,
\qquad
0\le j<(1-\eta)n.
\]

Then

\[
B_{n,1}(n-j;A)
=
\left(\frac{A}{n^2}\right)^{n-j}
\binom nj^2
\left(\frac{n+1}{j+1}\right)^{s_n+1}.
\tag{31}
\]

By `(5)`, choose `rho<1` such that for all sufficiently large `n`,

\[
A n^{s_n/n-2}\le\rho.
\tag{32}
\]

For `j=0`, equation `(31)` becomes

\[
B_{n,1}(n;A)
=
\left(A n^{s_n/n-2}\right)^n
n
\left(1+\frac1n\right)^{s_n+1}.
\tag{33}
\]

Since `s_n/n -> 2`, the final factor is bounded, so

\[
B_{n,1}(n;A)
\le
C n\rho^n.
\tag{34}
\]

Now suppose `1<=j<=sqrt(n)`. Dividing `(31)` by its `j=0` value gives

\[
\frac{B_{n,1}(n-j;A)}
{B_{n,1}(n;A)}
=
\left(\frac{n^2}{A}\right)^j
\binom nj^2
(j+1)^{-(s_n+1)}.
\tag{35}
\]

Using `binom(n,j)<=n^j`, the logarithm of the right side is at most

\[
j\bigl(4\log n+|\log A|\bigr)
-(s_n+1)\log2.
\tag{36}
\]

Uniformly for `1<=j<=sqrt(n)`, the first term is `o(n)` while the second is `-(2\log2+o(1))n`. Hence this entire range is exponentially smaller than `(34)`.

Finally suppose

\[
\sqrt n\le j<(1-\eta)n.
\]

Then `h=n-j>=eta n`, `binom(n,j)<=2^n`, and

\[
\frac{n+1}{j+1}\le2\sqrt n
\]

for large `n`. Therefore

\[
\begin{aligned}
\log B_{n,1}(h;A)
&\le
h(\log A-2\log n)
+2n\log2
+(s_n+1)\left(\frac12\log n+\log2\right)\\
&\le
-\bigl(2\eta-1+o(1)\bigr)n\log n
+O_A(n),
\end{aligned}
\tag{37}
\]

which is superexponentially negative because `eta>1/2`.

Equations `(34)`--`(37)` prove that for some `kappa>0`,

\[
\boxed{
\varepsilon_n(A)\le e^{-\kappa n}
}
\tag{38}
\]

for all sufficiently large `n`.

For a fixed number `r` of tall columns there are at most `n^r` possible height sequences. Summing `(26)` with `(29)` and `(38)` therefore bounds the absolute contribution of **all** partitions containing at least one tall column by

\[
C_A n^2
\sum_{r\ge1}
\bigl(n\varepsilon_n(A)\bigr)^r
\longrightarrow0.
\tag{39}
\]

Thus the critical full-height family is not merely termwise small below `b=1`; the complete unbounded tall-column sector vanishes absolutely.

## 5. The remaining no-tall family has the AF-417 moving exponential

For partitions with no tall columns, AF-419's original estimate `(17)` is better than `(20)`. From `(21)`,

\[
P_{n,\lambda}
\le
\exp\!\left(
\frac{|\lambda|}{(1-\eta)n}
\right).
\tag{40}
\]

Since `s_n/n -> 2`, there is a constant `C` such that

\[
R_{n,\lambda}^{(s_n)}
\le C^{|\lambda|}
\tag{41}
\]

uniformly over the no-tall family. The positive Schur Cauchy identity then gives the same degree-tail estimate as AF-419: for every fixed `A`, the contribution of no-tall partitions with `|\lambda|>D` tends to zero as `D->infinity`, uniformly in all sufficiently large `n` and uniformly for `0<=a<=A`.

For each fixed partition `lambda` of degree `d`, AF-417/AF-419 give

\[
P_{n,\lambda}^{s_n-1}
=
e^{(s_n/n)d}(1+o_\lambda(1)),
\tag{42}
\]

the zeta and odd-distance ratios tend to one, and

\[
\frac{s_\lambda(1^n)}{n^d}
\longrightarrow
\frac1{H_\lambda}.
\tag{43}
\]

Therefore the complete fixed-degree contribution satisfies

\[
\sum_{\lambda\vdash d}
(-1)^d
\left(\frac{a}{n^2}\right)^d
s_\lambda(1^n)^2
R_{n,\lambda}^{(s_n)}
-
\frac{(-a e^{s_n/n})^d}{d!}
\longrightarrow0
\tag{44}
\]

uniformly for `a in [0,A]`, using

\[
\sum_{\lambda\vdash d}\frac1{H_\lambda^2}
=
\frac1{d!}.
\tag{45}
\]

The no-tall uniform degree tail, the tall-column estimate `(39)`, and the finite-head convergence `(44)` prove `(6)`.

## 6. Critical-window phase diagram

The theorem turns AF-418's finer scaling variable into an exact open-domain phase diagram for the available absolute method.

If

\[
\tau_n\to\tau\in\mathbb R,
\]

then

\[
b_n(a)\to a e^\tau.
\]

Hence:

- for every `a<e^{-tau}`, the complete exceptional-`1` partition family is absolutely controlled and converges to the AF-417 candidate;
- for every `a>e^{-tau}`, the single full-height column grows exponentially, so no absolute-majorant proof can control the full sum;
- the boundary `a=e^{-tau}` is genuinely finer-scale and is not decided by the nth-root test alone.

For `s_n=2n`, the boundary is `a=1`, or `c=2pi`. Equation `(11)` strengthens the boundary statement there: even at equality the first full-height column grows linearly. Thus absolute uniform integrability fails on and beyond `c=2pi`, while `(9)` proves it strictly below that value.

The signed sum may still exhibit cancellation in the boundary/superthreshold region. That is now the only unresolved issue inside the finite-`tau` critical window.

## 7. Arithmetic-fidelity interpretation

AF-417 showed that every bounded partition compresses derivative depth to the single coarse statistic `s_n/n`. AF-418 proved that full-height partitions retain information discarded by that compression. AF-420 identifies the retained coordinate exactly:

\[
a\,n^{s_n/n-2}=a e^{\tau_n}.
\]

The same transformation therefore has two fidelity regimes. Bounded-complexity observations see only the coarse limit and predict one universal exponential, while an unbounded observation family carries an additional scale that determines whether that prediction is uniformly recoverable.

The result also sharpens the role of relational structure. Total partition degree is still insufficient. Column height relative to ambient rank isolates the critical fiber, and the full-height column gives the exact threshold. Below that threshold, Pieri compatibility and the Schur Cauchy normalization recover uniform control; above it, the lost scaling coordinate becomes exponentially visible.

No rational-prime discriminator appears here, and no RH consequence follows. The theorem is a structural result about preservation of asymptotic information under a complexity-unbounded limiting transformation.

## Prior-art and novelty audit

The hook-content formula, Pieri rule, Schur Cauchy identity, and `GL_n` specialization `s_lambda(1^n)` are classical symmetric-function and representation theory; Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed. (1995), Chapter I, remains the standard source used by AF-415--AF-419. Okounkov's *Infinite wedge and random partitions*, *Selecta Mathematica* 7 (2001), 57--81, arXiv:`math/9907127`, is established prior art for Schur-measure normalization and large random partitions.

A targeted prior-art search around Schur-measure tail control, full-height/rectangular partitions, rank-growth ratios, and critical varying specializations found broad asymptotic and integrable-probability literature but no source stating the specific Euler-log perturbation `(2)`, the effective coordinate `(14)`, or the threshold theorem `(5)`--`(6)`. No novelty is claimed for the classical Schur/Pieri ingredients. The durable contribution is the exact boundary-adapted estimate `(20)` and its application to the AF-417 derivative-shift family.

## Boundaries and falsification checks

- The theorem controls only the exceptional-`1` Cauchy--Binet sector defined in `(1)`.
- It does not yet extend AF-416's omitted-`1`, one-singular-block, or zero-singular-block estimates to growing derivative shift.
- The condition `(5)` is sufficient for absolute uniform integrability, not a claim that the signed sum fails when it is violated.
- The obstruction `(10)` proves failure of absolute domination, not failure of signed convergence.
- At a general boundary `a e^tau=1`, subleading information beyond `tau` may matter. Only the exact sequence `s_n=2n`, `a=1` is sharpened here to the linear asymptotic `(11)`.
- The theorem keeps `a` in a fixed compact interval. It does not treat `a=a_n` growing with `n`.
- No statement about total positivity, zeta zeros, rational-prime fidelity, or RH is made.

## Consequence for the research line

The critical regime is no longer a single unresolved block. The finite-`tau` window now has an exact **subthreshold absolute phase** governed by `a e^tau<1`, and the full-height column proves that this absolute mechanism cannot cross the complementary superthreshold region.

The accepted `CLUE-linear-derivative-shift-full-tail` should therefore narrow to the boundary/superthreshold signed problem: determine whether cancellations preserve the candidate exponential when `a e^tau>=1`, and then treat genuinely supercritical derivative ratios `s_n/n>2`.
