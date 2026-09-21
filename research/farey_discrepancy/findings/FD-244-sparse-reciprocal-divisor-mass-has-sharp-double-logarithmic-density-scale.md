# FD-244 — Sparse reciprocal-divisor mass has sharp double-logarithmic density scale

- **Date:** 2026-09-21
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response sampling / sparse omissions / reciprocal-divisor large values / quantitative inverse
- **Depends on:** FD-225, FD-241, FD-242, FD-243
- **Classification:** `EXACT-DERIVED + SHARP-SPARSE-WEIGHT-SCALE + DOUBLE-LOG-DEFECT + FINER-THAN-CAPACITY`

## Claim

FD-243 improved the omitted-sample contribution from a square-root defect to

\[
\delta\log(e/\delta)
\]

by proving the high-moment estimate `||n/phi(n)||_q << q`. That moment bound is still far from the true large-value scale. Replacing the crude small-prime product in FD-243 by the Mertens prime product gives

\[
\left(\frac1N\sum_{n\le N}\left(\frac n{\varphi(n)}\right)^q\right)^{1/q}
\ll \log(2q),
\tag{1}
\]

uniformly for every integer `q>=1` and every `N>=1`.

Define, for `0<delta<=1`,

\[
L(\delta):=\log\!\left(e+\log\frac1\delta\right),
\qquad
H(\delta):=\delta L(\delta),
\tag{2}
\]

and put `H(0)=0`. Then for every `A subset [1,N]`, with `|A|=delta N`,

\[
\boxed{
\sum_{m\in A}\sigma_{-1}(m)
\ll
N\,\delta\log\!\left(e+\log\frac1\delta\right).
}
\tag{3}
\]

The implied constant is absolute. The order in (3) is sharp up to constants as `delta -> 0`: along the primorial densities

\[
\delta_y=\frac1{P_y},
\qquad
P_y:=\prod_{p\le y}p,
\tag{4}
\]

there are `N_y` and sets `A_y subset [1,N_y]` of density `delta_y` for which

\[
\boxed{
\sum_{m\in A_y}\sigma_{-1}(m)
\gg
N_y\,\delta_y
\log\!\left(e+\log\frac1{\delta_y}\right).
}
\tag{5}
\]

Thus the entropy-scale factor `log(1/delta)` in FD-243 is not intrinsic. For the reciprocal-divisor weight itself the correct sparse-set scale is, up to constants,

\[
\boxed{\delta\log\log(1/\delta)}
\]

with the harmless regularization in (2) near `delta=1`.

Transferred through the exact divisor inversion of FD-225, this sharpens the omission term in FD-242--FD-243. With their notation

\[
Y(m)=(\mathscr A b)(m),
\qquad
|b_n|\le Cn,
\tag{6}
\]

and

\[
T_N=
\{1\le m\le N:m\notin S\ \text{or}\ m-1\notin S_0\},
\qquad
\rho_N=|T_N|/N,
\tag{7}
\]

one has

\[
\boxed{
\frac{\sum_{N/2<n\le N}|b_n|}
     {\sum_{N/2<n\le N}n}
\ll
C\,H(\rho_N)
+
\frac{V_S(N)}N.
}
\tag{8}
\]

Since `|T_N|<=2R(N)`, writing

\[
\eta_N:=\min\!\left(1,\frac{2R(N)}N\right)
\tag{9}
\]

gives

\[
\boxed{
\frac{\sum_{N/2<n\le N}|b_n|}
     {\sum_{N/2<n\le N}n}
\ll
C\,\eta_N
\log\!\left(e+\log\frac1{\eta_N}\right)
+
\frac{V_S(N)}N,
}
\tag{10}
\]

with the first term interpreted as zero when `R(N)=0`. As before, `V_S(N)<=2Q_S(N)` gives the corresponding `Q_S` version.

## The high moments are logarithmic, not linear

As in FD-243,

\[
\sigma_{-1}(n)
\le
\frac n{\varphi(n)}
=:F(n).
\tag{11}
\]

Fix an integer `q>=1` and set

\[
a_p:=\left(1-\frac1p\right)^{-q}.
\tag{12}
\]

The same nonnegative squarefree-divisor expansion used in FD-243 gives

\[
\sum_{n\le N}F(n)^q
\le
N C_q,
\qquad
C_q:=
\prod_p
\left(1+\frac{a_p-1}{p}\right).
\tag{13}
\]

Split the product at `2q`. For `p<=2q`, since `a_p>=1`,

\[
1+\frac{a_p-1}{p}\le a_p,
\]

hence

\[
\prod_{p\le2q}
\left(1+\frac{a_p-1}{p}\right)^{1/q}
\le
\prod_{p\le2q}
\left(1-\frac1p\right)^{-1}.
\tag{14}
\]

The quantitative prime-number theorem already anchored in `SOURCES.md` implies by partial summation

\[
\sum_{p\le x}\frac1p=\log\log x+O(1),
\]

and therefore

\[
\prod_{p\le x}
\left(1-\frac1p\right)^{-1}
\asymp \log x.
\tag{15}
\]

Thus the small-prime part of `C_q^(1/q)` is `O(log(2q))`.

For `p>2q`,

\[
-q\log\left(1-\frac1p\right)
\ll \frac qp<1,
\]

so

\[
a_p-1\ll\frac qp.
\]

Consequently

\[
\log
\prod_{p>2q}
\left(1+\frac{a_p-1}{p}\right)
\ll
q\sum_{p>2q}\frac1{p^2}
\ll1.
\tag{16}
\]

Combining (13)--(16) proves (1).

## Hölder gives the double-log sparse bound

Let `t=|A|=delta N`. Hölder and (1) give, for every integer `q>=1`,

\[
\begin{aligned}
\sum_{m\in A}\sigma_{-1}(m)
&\le
\sum_{m\in A}F(m)\\
&\le
t^{1-1/q}
\left(\sum_{m\le N}F(m)^q\right)^{1/q}\\
&\ll
N\,\delta^{1-1/q}\log(2q).
\end{aligned}
\tag{17}
\]

Choose

\[
q=\left\lceil\log\frac e\delta\right\rceil.
\tag{18}
\]

Then `delta^(-1/q)=O(1)` and

\[
\log(2q)
\ll
\log\!\left(e+\log\frac1\delta\right).
\tag{19}
\]

Equations (17)--(19) give (3).

This also shows precisely where FD-243 lost the extra logarithm: its elementary estimate

\[
\prod_{p\le2q}
\left(1-\frac1p\right)^{-1}
\le 2q
\]

kept the proof self-contained but replaced the true `log q` small-prime scale by `q`.

## Primorial multiples show the sparse scale is sharp

Let

\[
P_y=\prod_{p\le y}p,
\qquad
N_y=P_y^2,
\qquad
A_y=\{m\le N_y:P_y\mid m\}.
\tag{20}
\]

Then `|A_y|=P_y`, so its density is exactly `delta_y=1/P_y`. Every `m in A_y` is divisible by `P_y`, hence

\[
\sigma_{-1}(m)
\ge
\sigma_{-1}(P_y)
=
\prod_{p\le y}\left(1+\frac1p\right).
\tag{21}
\]

Using

\[
1+\frac1p
=
\left(1-\frac1{p^2}\right)
\left(1-\frac1p\right)^{-1},
\tag{22}
\]

the first product in (22) stays bounded below by `1/zeta(2)`, while (15) gives

\[
\sigma_{-1}(P_y)\gg\log y.
\tag{23}
\]

The prime-number theorem also gives

\[
\log P_y=\vartheta(y)\sim y,
\tag{24}
\]

so

\[
\log\!\left(e+\log\frac1{\delta_y}\right)
=
\log(e+\log P_y)
\asymp
\log y.
\tag{25}
\]

Therefore

\[
\sum_{m\in A_y}\sigma_{-1}(m)
\ge
|A_y|\,\sigma_{-1}(P_y)
\gg
N_y\delta_y
\log\!\left(e+\log\frac1{\delta_y}\right),
\tag{26}
\]

which proves (5). This lower bound concerns the sparse arithmetic weight itself. It does **not** claim that every step of the Farey sampling inequality (8) is simultaneously saturated by a realizable coefficient sequence.

## Transfer to density-one response sampling

Use again

\[
g=\mu*b,
\qquad
b=\mathbf1*g,
\qquad
g(m)=Y(m)-Y(m-1).
\tag{27}
\]

For `m in T_N`, the coefficient envelope gives

\[
|g(m)|\le Cm\sigma_{-1}(m).
\tag{28}
\]

When the reconstruction `b=1*g` is summed over `N/2<n<=N`, the contribution from those uncontrolled increments is at most

\[
\ll
CN\sum_{m\in T_N}\sigma_{-1}(m)
\ll
CN^2 H(\rho_N)
\tag{29}
\]

by (3). The controlled increments outside `T_N` contribute exactly as in FD-242--FD-243,

\[
\ll N V_S(N).
\tag{30}
\]

Since

\[
\sum_{N/2<n\le N}n\asymp N^2,
\tag{31}
\]

(29)--(31) prove (8). The function `H(delta)=delta log(e+log(1/delta))` is increasing on `(0,1]`, so `rho_N<=eta_N` gives (10).

In particular, for exact observed zeros, if

\[
R(N)=O(N^\alpha),
\qquad 0\le\alpha<1,
\tag{32}
\]

then

\[
\boxed{
\sum_{N/2<n\le N}|b_n|
\ll_C
N^{1+\alpha}\log\log N.
}
\tag{33}
\]

For a bounded number of omitted samples this becomes `O_C(N log log N)`, improving the `O_C(N log N)` consequence of FD-243.

## Prior-art and dependency audit

Large-value and distribution questions for `sigma(n)/n`, `phi(n)/n`, and therefore the closely related weight `n/phi(n)` are classical. In particular, Erdős's 1974 paper *On the distribution of numbers of the form sigma(n)/n and on some related questions* studies the distribution of `sigma(n)/n` and related totient questions. No novelty is claimed here for that general distribution theory or for Mertens' prime-product scale.

The contribution needed by the present line is narrower: (3) identifies, by an elementary moment argument, the sharp order of the **finite sparse-subset norm** that enters the exact divisor-response inversion, and (8)--(10) transfer that order directly to the Farey sampling defect. The lower construction (20)--(26) is included to prevent the sparse arithmetic factor from being optimized away in later passes.

No new external theorem is load-bearing. The only asymptotic input beyond the exact divisor algebra is the prime-number theorem / quantitative prime-number-theorem anchor already recorded in `research/farey_discrepancy/SOURCES.md`, from which (15) and (24) follow by standard partial summation. Therefore `SOURCES.md` requires no change.

## Consequence for the frontier

FD-243 left open whether the entropy factor was structural. It is not: the sparse omission ledger can be sharpened from

\[
\delta\log(1/\delta)
\]

to the sharp reciprocal-divisor scale

\[
\boxed{\delta\log\log(1/\delta)}.
\]

This closes the immediate response-side optimization of the **omission-count term** up to constants. Further progress in the sampled inverse must now come from elsewhere: exploiting extra structure of the actual defect set `T_N`, improving the residual term `V_S(N)/N`, or adding source-side positivity/capacity/arithmetic coherence. Merely taking still higher moments of the same unrestricted sparse reciprocal-divisor weight cannot remove the double logarithm, because primorial multiples already force it.