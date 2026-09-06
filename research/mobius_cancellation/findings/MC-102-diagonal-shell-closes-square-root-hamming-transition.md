# MC-102 — Diagonal shell closes the square-root Hamming transition

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `BOUNDARY/CONDITIONAL-GAIN`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

For the source-forced Hamming deformation of `MC-092`--`MC-101`,

\[
\mathcal Q_N(t)
=\sum_{k=0}^{D_N}(-t)^k C_{k,N}
=C_{0,N}-tC_{1,N}+t^2C_{2,N}+\mathcal R_{\ge3,N}(t),
\qquad 0\le t\le1,
\tag{1}
\]

the degree-zero shell is not merely `O(N)`. It has the exact positive linear asymptotic

\[
\boxed{
C_{0,N}=c_0N+O(N^{2/3}),
\qquad
c_0=
\frac{\zeta(1/2)}{\zeta(2)}+\frac9{\pi^2}
=\frac{6\zeta(1/2)+9}{\pi^2}
>0.
}
\tag{2}
\]

Numerically `c_0=0.02410156856...`. Combining `(2)` with the already established source estimates

\[
C_{1,N}=O(N\log\log N),
\qquad
C_{2,N}\sim c_2\frac{N^2}{(\log N)^2},
\qquad
c_2=\frac{15}{\pi^2}\left(\gamma+\gamma_1-\frac12\right)>0,
\tag{3}
\]

and

\[
|\mathcal R_{\ge3,N}(t)|\le\frac12N^2t^3,
\tag{4}
\]

gives a single asymptotic that crosses the regime boundary left open by `MC-101`.

Let `t_N` be any sequence with

\[
0\le t_N\le1,
\qquad
t_N(\log N)^2\longrightarrow0.
\tag{5}
\]

Then

\[
\boxed{
\mathcal Q_N(t_N)
=
c_0N
+c_2\frac{N^2t_N^2}{(\log N)^2}
+o\!\left(
N+\frac{N^2t_N^2}{(\log N)^2}
\right).
}
\tag{6}
\]

Consequently the whole low-bias transition is classified:

\[
t_N\ll\frac{\log N}{\sqrt N}
\quad\Longrightarrow\quad
\mathcal Q_N(t_N)\sim c_0N,
\tag{7}
\]

while for every fixed `u>=0`,

\[
t_N=u\frac{\log N}{\sqrt N}
\quad\Longrightarrow\quad
\boxed{
\frac{\mathcal Q_N(t_N)}N\longrightarrow c_0+c_2u^2>0,
}
\tag{8}
\]

and

\[
\frac{\log N}{\sqrt N}\ll t_N\ll\frac1{(\log N)^2}
\quad\Longrightarrow\quad
\mathcal Q_N(t_N)
\sim c_2\frac{N^2t_N^2}{(\log N)^2},
\tag{9}
\]

recovering the mesoscopic degree-two profile of `MC-101` in its overlap.

Thus the apparent loss of control at square-root bias in `MC-101` was caused by the coarse bound on `C_{0,N}`, not by a genuine unresolved cancellation between the diagonal and degree-two shells. At and below the transition, the diagonal shell itself supplies a positive critical-power floor. At the transition, the positive degree-zero and degree-two terms add rather than cancel.

This closes **amplitude shrinking around the unbiased endpoint** as a route to a subcritical source power: moving from fixed bias down through `t\asymp(\log N)/\sqrt N` regularizes the almost-square degree-two source only until the positive `c_0N` diagonal floor takes over. It does not estimate the hard endpoint `\mathcal Q_N(1)`, `M(N)`, or `M(N^2)`, and it does not rule out a signed recurrence, a moving interior window, or a different source coupling.

## 1. Exact degree-zero shell

The product-fiber normal form of `MC-092` is

\[
\mathcal Q_N(t)
=\sum_{\substack{a,b\ \mathrm{squarefree}\\(a,b)=1\\ab^2\le N^2}}
R_N(a,b)(-t)^{\omega(a)}
 z\!\left(\frac{N^2}{ab^2}\right),
\tag{10}
\]

where

\[
R_N(a,b)
=\#\left\{d\mid a:\frac{ab}{N}\le d\le\frac Nb\right\},
\qquad
z(x)=\lfloor x\rfloor+\frac12-x.
\tag{11}
\]

Degree zero means `a=1`. Its only divisor is `d=1`, and both inequalities in `(11)` are then equivalent to `b\le N`. Hence

\[
\boxed{
C_{0,N}
=\sum_{\substack{b\le N\\b\ \mathrm{squarefree}}}
 z\!\left(\frac{N^2}{b^2}\right).
}
\tag{12}
\]

Put

\[
A(X):=
\sum_{b\le\sqrt X}\mu(b)^2
\left\lfloor\frac X{b^2}\right\rfloor,
\qquad
Q(x):=\sum_{n\le x}\mu(n)^2.
\tag{13}
\]

Expanding the sawtooth in `(12)` gives the exact identity

\[
C_{0,N}
=A(N^2)+\frac12Q(N)
-N^2\sum_{b\le N}\frac{\mu(b)^2}{b^2}.
\tag{14}
\]

The three terms in `(14)` each have a linear contribution after their quadratic main terms cancel. That contribution is what the previous `O(N)` treatment hid.

## 2. The square-divisor count has the classical asymmetric-divisor secondary term

Use

\[
\mu(b)^2=\sum_{d^2\mid b}\mu(d)
\tag{15}
\]

and write `b=d^2c`. Then

\[
A(X)
=\sum_{d\le X^{1/4}}\mu(d)
 B\!\left(\frac X{d^4}\right),
\tag{16}
\]

where

\[
B(Y):=\sum_{c\le\sqrt Y}\left\lfloor\frac Y{c^2}\right\rfloor
=\#\{(m,c)\in\mathbb N^2:mc^2\le Y\}.
\tag{17}
\]

This is the `(1,2)` asymmetric divisor count. A standard Dirichlet-hyperbola split at `U=Y^{1/3}+O(1)` gives

\[
\boxed{
B(Y)=\zeta(2)Y+\zeta(1/2)Y^{1/2}+O(Y^{1/3}).
}
\tag{18}
\]

For completeness, the two pieces make the secondary term transparent. The `c\le U` side is

\[
Y\sum_{c\le U}\frac1{c^2}+O(U)
=\zeta(2)Y-Y^{2/3}+O(Y^{1/3}),
\tag{19}
\]

while the complementary side, after summing first over `m\ll Y^{1/3}`, uses

\[
\sum_{m\le V}m^{-1/2}
=2V^{1/2}+\zeta(1/2)+O(V^{-1/2})
\tag{20}
\]

and equals

\[
Y^{2/3}+\zeta(1/2)Y^{1/2}+O(Y^{1/3}).
\tag{21}
\]

The `Y^{2/3}` boundary terms cancel, proving `(18)`.

Substituting `(18)` into `(16)` and using the absolutely convergent Möbius sums

\[
\sum_{d\ge1}\frac{\mu(d)}{d^4}=\frac1{\zeta(4)},
\qquad
\sum_{d\ge1}\frac{\mu(d)}{d^2}=\frac1{\zeta(2)},
\tag{22}
\]

gives

\[
\boxed{
A(X)
=
\frac{\zeta(2)}{\zeta(4)}X
+\frac{\zeta(1/2)}{\zeta(2)}X^{1/2}
+O(X^{1/3}).
}
\tag{23}
\]

Indeed, truncating the two convergent series in `(22)` costs only `O(X^{1/4})`, and the accumulated error from `(18)` is

\[
X^{1/3}\sum_{d\le X^{1/4}}d^{-4/3}=O(X^{1/3}).
\]

No zero-free-region information is used.

## 3. Square-free density completes the linear constant

The classical square-free count retained in `MC-S12` gives

\[
Q(N)=\delta N+O(N^{1/2}),
\qquad
\delta=\frac6{\pi^2}.
\tag{24}
\]

Partial summation therefore yields

\[
\sum_{b>N}\frac{\mu(b)^2}{b^2}
=\frac\delta N+O(N^{-3/2}),
\tag{25}
\]

and hence

\[
N^2\sum_{b\le N}\frac{\mu(b)^2}{b^2}
=
\frac{\zeta(2)}{\zeta(4)}N^2
-\delta N
+O(N^{1/2}).
\tag{26}
\]

Apply `(23)` with `X=N^2` and insert `(24)` and `(26)` into `(14)`. The quadratic terms cancel exactly, leaving

\[
C_{0,N}
=
\left(
\frac{\zeta(1/2)}{\zeta(2)}
+\frac32\delta
\right)N
+O(N^{2/3}),
\tag{27}
\]

which is `(2)`.

The positivity does not need an RH-sensitive estimate. Since `\zeta(2)=\pi^2/6`, it is equivalent to the elementary inequality `\zeta(1/2)>-3/2`. Using the Dirichlet eta identity retained through the standard factor `\eta(s)=(1-2^{1-s})\zeta(s)`, write

\[
\eta(1/2)
=\sum_{k\ge1}\left((2k-1)^{-1/2}-(2k)^{-1/2}\right).
\tag{28}
\]

For the tail after `K` pairs, the mean-value theorem and monotonicity give

\[
0<\sum_{k>K}\left((2k-1)^{-1/2}-(2k)^{-1/2}\right)
\le\frac1{2\sqrt{2K-1}}.
\tag{29}
\]

At `K=5`, the five explicit pair differences plus the right side of `(29)` are less than `0.618`, while

\[
\frac32(\sqrt2-1)>0.621.
\]

Thus `\eta(1/2)<\tfrac32(\sqrt2-1)`. Since `1-\sqrt2<0`, this gives `\zeta(1/2)>-3/2` and therefore `c_0>0`. The displayed numerical value is only a convenience, not an input to the sign proof.

## 4. Uniform crossover asymptotic

Let

\[
L:=\log N,
\qquad
S_N:=N+\frac{N^2t_N^2}{L^2}.
\tag{30}
\]

The diagonal-shell error in `(2)` is `o(N)` and hence `o(S_N)`. From `(3)` and `(5)`,

\[
t_NC_{1,N}
=O(Nt_N\log\log N)
=o(N)
=o(S_N).
\tag{31}
\]

The degree-two asymptotic gives

\[
t_N^2C_{2,N}
=c_2\frac{N^2t_N^2}{L^2}
+o\!\left(\frac{N^2t_N^2}{L^2}\right).
\tag{32}
\]

Finally `(4)` factors relative to the degree-two scale without a case split:

\[
N^2t_N^3
=
\left(\frac{N^2t_N^2}{L^2}\right)(t_NL^2)
=o\!\left(\frac{N^2t_N^2}{L^2}\right)
\tag{33}
\]

whenever `t_N>0`; at `t_N=0` the tail vanishes identically. Thus it is also `o(S_N)`. Equations `(2)`, `(31)`--`(33)` in `(1)` prove `(6)`.

The transition statements `(7)`--`(9)` are now just comparisons of the two positive scales in `(6)`. In particular, at

\[
t_N=u\frac{L}{\sqrt N},
\]

the degree-two contribution is exactly asymptotic to `c_2u^2N`, on the same linear scale as `C_{0,N}`. There is no hidden sign competition at this boundary.

## 5. Prior art and novelty boundary

The Huxley--Watt source and its Hamming/product-fiber reduction are already represented by `MC-S24` and `MC-092`; the positive degree-two asymptotic and cubic source tail are `MC-097` and `MC-100`. Square-free counting is classical and already retained as `MC-S12`.

The auxiliary count `B(Y)` in `(17)` belongs to the classical asymmetric divisor problem: it is the summatory function for representations `n=mc^2`, with Dirichlet series `\zeta(s)\zeta(2s)`. The broader asymmetric-divisor literature includes Werner Georg Nowak, *A two-sides omega-theorem for an asymmetric divisor problem*, Manuscripta Mathematica 69 (1990), 153--172, DOI `10.1007/BF02567917`, and Hartmut Menzer and Werner Georg Nowak, *On an asymmetric divisor problem with congruence conditions*, Manuscripta Mathematica 64 (1989), 107--120, DOI `10.1007/BF01182087`. The present proof uses only the elementary two-term hyperbola calculation `(18)`; these papers are a prior-art boundary for the surrounding divisor-problem language, not evidence for a novelty claim.

A targeted search around asymmetric divisor sums, square-divisor counts, Hamming/noise deformations, biased prime-sign multiplicative functions, and the square-root bias transition found no basis for claiming a new external theorem. **No novelty claim is made.** The durable line-specific result is the insertion of the exact diagonal-shell asymptotic into this already-defined Möbius/Huxley--Watt deformation, which removes the unresolved transition identified explicitly by `MC-101`.

## 6. Boundaries and falsification tests

- Equation `(6)` is a low-bias theorem. Its hypothesis `t_N(\log N)^2\to0` does not approach the hard endpoint `t=1`, so it supplies no new bound for `M(N)` or any zero-free region.
- The result closes only intervals anchored at the unbiased endpoint through their individual amplitudes. A moving interior interval or a signed relation among several deformation values is a different object and is not ruled out.
- The linear floor comes from the exact `a=1` product fiber. Altering the source kernel, removing the diagonal fiber, or adding a compensating signed observable requires a new audit; one may not carry `c_0` into such a construction by analogy.
- The transition is positive because both `c_0` and `c_2` are positive. The proof does not assert coefficientwise positivity for higher Hamming degrees; `MC-098` and `MC-099` show that large signed higher-degree cancellation is essential away from the low-bias regime.
- The `O(N^{2/3})` error is more than sufficient for the transition and is not claimed optimal. Improving the classical asymmetric-divisor error term would not alter the power boundary established here.
- No random-multiplicative heuristic enters the derivation. The result is deterministic and source-local.

## Consequence for the research line

`MC-101` left three possible escapes for the Hamming branch: enter at or below square-root bias where degree two no longer controlled the source, obtain a reconstruction whose stability cost beats the regularization gain, or use a different signed coupling. The first escape is now closed for the present endpoint-anchored amplitude strategy. Below the transition the deformation does not continue shrinking in power; it saturates at the explicit positive `c_0N` diagonal floor. At the transition it has the positive limit `(8)`.

The live burden therefore moves from **how small can an individual low-bias deformation value become?** to **can several such values be coupled with signed information whose reconstruction cost is genuinely subcritical, or can the source be changed without merely deleting the arithmetic obstruction by hand?** Any recurrence/interpolation proposal should be measured against the full crossover `(6)`, not only against the degree-two profile of `MC-101`.