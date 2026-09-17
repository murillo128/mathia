# WI-333 — square-root phase pseudorandomness still leaves diagonal bow variance

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED`.

The current bow frontier asks for a source-fixed estimate of the form

\[
\int_X^{2X}
\left|
\sum_{x<n\le x+K}
(\Lambda(n)-\Lambda_X^\sharp(n))n^{iU}
\right|^2dx
=o(XK\log X)
\tag{1}
\]

at the distinguished bow twist. WI-331 and WI-332 show that the available all-interval nilsequence and local `U^2` estimates do not reach this scale. The obstruction is stronger than their quantitative logarithmic loss: **even essentially square-root one-point cancellation against every fixed-degree polynomial phase, uniformly over every short interval and arithmetic subprogression, is logically compatible with a full diagonal-scale variance**.

Thus no route whose only new arithmetic input is a stronger one-point polynomial/nilsequence pseudorandomness estimate can prove (1). The missing information is genuinely two-point and sign-sensitive: it must force macroscopic negative off-diagonal covariance at the distinguished twist (or introduce an equivalent source-fixed diagonal subtraction with independently controlled residual).

## 1. Abstract countermodel at the exact bow scaling

Fix `0<alpha<1` and put

\[
K=N^{\alpha+o(1)},\qquad L=\log N.
\]

Let `d>=1` be fixed and let `u_1,\ldots,u_N` be **any prescribed unit complex numbers**. The choice

\[
u_n=n^{iU}
\]

is allowed, as is any fixed polynomialized version of the bow carrier.

For all sufficiently large `N`, there exists a real sign sequence

\[
\varepsilon_n\in\{-1,1\},\qquad
b_n:=\sqrt L\,\varepsilon_n,
\tag{2}
\]

with the following two simultaneous properties.

First, for every interval `I subset {1,...,N}` of length at most `K`, every arithmetic progression `Q subset I`, and every real polynomial `P` of degree at most `d`,

\[
\boxed{
\left|\sum_{n\in Q} b_n e(P(n))\right|
\le C_d\sqrt K\,\log N.
}
\tag{3}
\]

Since `K=N^{alpha+o(1)}`, for every fixed `A>0`,

\[
C_d\sqrt K\log N
=o\!\left(K\log^{-A}N\right).
\tag{4}
\]

So (3) is asymptotically much stronger than an arbitrary fixed logarithmic saving of the all-interval form used in WI-331, while retaining its relevant maximal-subprogression feature for polynomial phases.

Second, the twisted sliding variance stays at full diagonal scale:

\[
\boxed{
\sum_{x=0}^{N-K}
\left|
\sum_{j=1}^{K} b_{x+j}u_{x+j}
\right|^2
=(1+o(1))NK\log N.
}
\tag{5}
\]

In particular it is not `o(NK log N)`. Equations (3)--(5) coexist for the **same** coefficients.

This is an information-interface counterexample, not a model for the von Mangoldt function. It says that one-point phase decorrelation, even strengthened far past the currently available theorem, does not contain enough information to imply the norm-matched bow estimate.

## 2. Uniform square-root polynomial-phase cancellation

Take independent Rademacher variables `epsilon_n`. For a fixed arithmetic progression `Q` of at most `K` integers and a fixed polynomial phase `P`, the complex random sum

\[
Z_{Q,P}:=\sum_{n\in Q}\epsilon_n e(P(n))
\]

has subgaussian tails. Applying Hoeffding separately to real and imaginary parts gives an absolute `c>0` such that

\[
\Pr(|Z_{Q,P}|>t)
\le 4\exp(-c t^2/K).
\tag{6}
\]

The continuum of degree-`d` phases causes only polynomial entropy. Write

\[
P(n)=\sum_{r=0}^{d}\beta_r n^r,
\qquad \beta_r\in\mathbb R/\mathbb Z.
\]

For a target `t`, place a circular mesh of spacing

\[
\delta_r=
\frac{t}{16\pi(d+1)K N^r}
\tag{7}
\]

on the `r`th coefficient. If `P_0` is the nearest mesh polynomial, then for every `n<=N`,

\[
|e(P(n))-e(P_0(n))|
\le
2\pi\sum_{r=0}^{d}\delta_rN^r
\le \frac{t}{8K},
\]

and hence on every `Q` with `|Q|<=K`,

\[
|Z_{Q,P}-Z_{Q,P_0}|\le t/8.
\tag{8}
\]

For fixed `d`, the total number of mesh phases is `N^{O_d(1)}` whenever `1<=t<=K`, and the number of arithmetic progressions contained in intervals of length at most `K` is at most polynomial in `N`. Therefore a union bound in (6), with

\[
t=C_d\sqrt{K\log N}
\tag{9}
\]

and `C_d` sufficiently large, gives with probability `1-o(1)`

\[
\sup_{I,Q,P}|Z_{Q,P}|
\le C_d\sqrt{K\log N}.
\tag{10}
\]

Multiplication by `sqrt(log N)` yields (3).

The mechanism is classical random-sign harmonic analysis. Salem and Zygmund, *Some properties of trigonometric series whose terms have random signs*, Acta Math. 91 (1954), 245--301, is classical prior art for square-root-times-logarithm sup-norm behavior of random trigonometric sums. The finite-degree coefficient-net argument above is included explicitly because the exact all-interval/arithmetic-progression interface needed here is a derived statement; no priority claim is made.

## 3. The same sequence has asymptotically diagonal sliding variance

For the same independent signs, define

\[
S_x:=\sum_{j=1}^{K}\epsilon_{x+j}u_{x+j},
\qquad
V:=\sum_{x=0}^{N-K}|S_x|^2.
\]

Because the signs are independent and `|u_n|=1`,

\[
\mathbb E|S_x|^2=K,
\qquad
\mathbb EV=(N-K+1)K.
\tag{11}
\]

A fourth-moment Khintchine bound gives, uniformly in the prescribed phases,

\[
\mathbb E|S_x|^4\le 3K^2.
\tag{12}
\]

If `|x-y|>=K`, the two windows are disjoint, so `|S_x|^2` and `|S_y|^2` are independent and their covariance vanishes. There are `O(NK)` overlapping ordered pairs, and by Cauchy--Schwarz plus (12) each covariance has absolute value `O(K^2)`. Hence

\[
\operatorname{Var}(V)=O(NK^3).
\tag{13}
\]

Since `K=o(N)`,

\[
\frac{\operatorname{Var}(V)}{(\mathbb EV)^2}
=O(K/N)=o(1).
\tag{14}
\]

Chebyshev therefore gives

\[
V=(1+o(1))NK
\tag{15}
\]

with probability `1-o(1)`. The high-probability events (10) and (15) have nonempty intersection for all sufficiently large `N`, so there exists one deterministic sign sequence satisfying both. Rescaling by `sqrt(log N)` proves (5).

Note that the prescribed twist `u_n` was arbitrary. In particular, replacing linear phases by the exact bow carrier in the variance does not weaken the countermodel.

## 4. What this closes beyond WI-331 and WI-332

WI-331 shows that the published all-interval bound

\[
|\sum f_X(n)e(P(n))|\ll_A K\log^{-A}X
\]

is too large after naive squaring. That leaves open the possibility that a sufficiently strong quantitative upgrade of the **same one-point theorem surface** might eventually reach the variance scale.

The countermodel closes that route. Its pointwise bound is already

\[
O_d(\sqrt K\log N),
\]

which is square-root cancellation up to a logarithm and is smaller than `K log^{-A}N` for every fixed `A`; nevertheless the moving-window `L^2` norm remains `(1+o(1))NK log N`. The obstruction is therefore not merely that the known logarithmic saving is too weak.

WI-332 similarly shows that black-box logarithmic local `U^2` control misses the variance scale and that `U^2` does not absorb the nonlinear bow carrier. WI-333 identifies the more basic structural issue underneath both observations: **generic pseudorandom cancellation suppresses off-diagonal correlations toward zero, whereas (1) needs the signed off-diagonal to cancel a positive diagonal of size `XK log X`.** Making a one-point pseudorandomness theorem quantitatively stronger does not manufacture that negative covariance.

This does not rule out using nilsequence or Gowers technology as one ingredient inside a genuinely bilinear argument. It rules out an implication whose arithmetic hypothesis consists only of one-point phase decorrelation of the source, however close to square-root scale, together with its diagonal `L^2` size.

## 5. Consequence for the distinguished-twist clue

The accepted clue `CLUE-bow-distinguished-twist-offdiagonal-cancellation` should now be read literally. A resolving source theorem must expose at least one datum absent from the countermodel, for example:

- a signed two-point asymptotic for `(Lambda-Lambda^sharp)(n+h)(Lambda-Lambda^sharp)(n)` with the distinguished oscillatory weight;
- a bilinear/operator estimate that couples different starts before taking absolute values;
- an arithmetic identity forcing the off-diagonal toward `-D_X` rather than toward zero; or
- a canonical source-fixed diagonal subtraction whose residual can be controlled in the same norm.

Pure strengthening of all-interval polynomial/nilsequence cancellation, even to essentially square-root size, is no longer a credible standalone route to the WI-195 gate.

## 6. Evidence and novelty audit

The random-sign subgaussian mechanism is classical; Salem--Zygmund is prior art for the underlying harmonic-analysis phenomenon. The exact coexistence statement (3)--(5), its arithmetic-subprogression coefficient-net proof, and its use as an information-interface obstruction for the WI-195 distinguished bow variance are derived here. A bounded search did not locate this zeta/bow formulation. **No priority claim is made.**

The finding does not assert anything about the actual sign pattern of `Lambda-Lambda^sharp`, does not use the transferred `ANF-102` statement as evidence, and does not resolve the bow or RH. Its durable content is a decisive negative result about proof architecture: one-point pseudorandomness cannot by itself eliminate the diagonal-scale source defect that the current Weil-inertia bootstrap must remove.
