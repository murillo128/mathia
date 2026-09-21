# FD-245 — Finite exact omission geometry removes the sparse double-log penalty

- **Date:** 2026-09-21
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response sampling / exact omissions / finite-defect algebra / triangular reconstruction / quantitative inverse
- **Depends on:** FD-225, FD-241, FD-242, FD-244
- **Classification:** `EXACT-DERIVED + FINITE-DEFECT-GEOMETRY + TRIANGULAR-OMISSION-BOUND + DOUBLE-LOG-NOT-TRANSFERRED + SHARP-ONE-HOLE`

## Claim

FD-244 proves that an arbitrary set of `R(N)` uncontrolled Möbius-inverted increments can carry a reciprocal-divisor penalty of order

\[
\frac{R(N)}N
\log\!\left(e+\log\frac{N}{R(N)}\right),
\]

and that the corresponding sparse `sigma_{-1}` norm is sharp up to constants. FD-244 explicitly leaves open whether that arithmetic lower construction can actually saturate the **sampling** problem, because exact missing samples do not generate arbitrary sparse increments: they generate adjacent differences of a response supported only on the omitted locations.

For a bounded number of exact omissions, that distinction removes the double logarithm completely.

Let

\[
Y(m)=(\mathscr A b)(m),
\qquad Y(0)=0,
\]

and assume the linear coefficient envelope

\[
|b_n|\le Cn\qquad(n\ge1).
\tag{1}
\]

Fix `N>=1`. Suppose there is a set

\[
E_N\subseteq\{1,\ldots,N\},
\qquad |E_N|=K,
\tag{2}
\]

such that

\[
Y(m)=0
\qquad
(1\le m\le N,\ m\notin E_N).
\tag{3}
\]

Thus `E_N` contains all response locations that were omitted from exact-zero sampling; some of those locations may themselves happen to have zero response.

Then

\[
\boxed{
\sum_{n\le N}|b_n|
\le
2CN\,(2^K-1).
}
\tag{4}
\]

In particular,

\[
\boxed{
\sum_{N/2<n\le N}|b_n|
\ll
C N\,2^K,
}
\tag{5}
\]

and therefore

\[
\boxed{
\frac{\sum_{N/2<n\le N}|b_n|}
     {\sum_{N/2<n\le N}n}
\ll
C\frac{2^K}{N}.
}
\tag{6}
\]

For every fixed `K`, exact-zero sampling with at most `K` omitted locations therefore leaves only `O_{C,K}(N)` coefficient mass below `N`, rather than the `O_{C,K}(N log log N)` consequence obtained by treating the defect increments as an arbitrary sparse set in FD-244.

The linear order in `N` is already sharp for one omission. For every `e>=2` there is an integer sequence with `|b_n|<=n` whose divisor response is zero at every positive integer except `e`, while

\[
\sum_{e/2<n\le e}|b_n|\ge e.
\tag{7}
\]

Thus the double logarithm in FD-244 is genuinely a cost of forgetting the finite exact-omission geometry; it is not forced by one missing response value. This does **not** show that the double logarithm disappears when `K=K(N)->infinity`: the present triangular bound has an exponential `2^K` dependence, so FD-244 remains stronger in most growing-defect regimes.

## Exact omissions give adjacent divisor-difference columns

Use the exact inversion of FD-225. Put

\[
g=\mu*b.
\tag{8}
\]

Then

\[
b=\mathbf1*g,
\qquad
g(m)=Y(m)-Y(m-1).
\tag{9}
\]

For `n<=N`, substitute the second identity of (9) into the first:

\[
\begin{aligned}
b_n
&=\sum_{d\mid n}\bigl(Y(d)-Y(d-1)\bigr)\\
&=\sum_{m=1}^{N}Y(m)
\left(\mathbf1_{m\mid n}-\mathbf1_{m+1\mid n}\right).
\end{aligned}
\tag{10}
\]

Only `m<=n` can contribute to the first indicator, and only `m+1<=n` to the second, so values of `Y` beyond `N` are irrelevant for (10). Under (3), this becomes the finite column decomposition

\[
\boxed{
b_n
=\sum_{m\in E_N}Y(m)
\left(\mathbf1_{m\mid n}-\mathbf1_{m+1\mid n}\right)
\qquad(n\le N).}
\tag{11}
\]

This is the extra structure discarded by the sparse-weight argument of FD-244. One omitted response location does not create an arbitrary increment at a divisor-rich integer `m`; it creates the paired column

\[
Y(m)\bigl(\mathbf1_{m\mid n}-\mathbf1_{m+1\mid n}\bigr).
\tag{12}
\]

Consecutive omissions can make neighboring columns interact, but the map from the omitted response amplitudes to the coordinates `b_m` remains triangular in increasing `m`.

## Triangularity controls all omitted amplitudes when their number is finite

Write the active omitted locations in increasing order,

\[
E_N=\{e_1<e_2<\cdots<e_K\},
\]

and define

\[
z_i:=\frac{|Y(e_i)|}{e_i},
\qquad
Z_i:=\sum_{j\le i}z_j,
\qquad Z_0=0.
\tag{13}
\]

Evaluate (11) at `n=e_i`. The column `m=e_i` contributes exactly `Y(e_i)`, because `e_i|e_i` while `e_i+1` does not divide `e_i`. A later omitted location cannot contribute at all. Every earlier column has coefficient in `{-1,0,1}`. Hence

\[
|Y(e_i)|
\le
|b_{e_i}|+
\sum_{j<i}|Y(e_j)|.
\tag{14}
\]

Using (1) and `e_j<e_i`,

\[
\begin{aligned}
z_i
&\le
C+
\sum_{j<i}z_j\frac{e_j}{e_i}\\
&\le C+Z_{i-1}.
\end{aligned}
\tag{15}
\]

Therefore

\[
Z_i
\le C+2Z_{i-1}.
\tag{16}
\]

Induction gives the explicit finite-defect bound

\[
\boxed{
Z_K
=\sum_{m\in E_N}\frac{|Y(m)|}{m}
\le
C(2^K-1).
}
\tag{17}
\]

No reciprocal-divisor weight occurs. The reason is exactly the support information (3): instead of bounding an arbitrary increment `g(m)=mu*b(m)` separately by `Cm sigma_{-1}(m)`, we solve for the omitted response amplitudes in their own triangular coordinates.

The factor `2^K` is only a uniform finite-dimensional bound. No optimality in `K` is claimed. In particular, the divisibility signs in (11) may force substantially better conditioning for structured omission patterns. What matters here is that for each fixed `K`, the constant is independent of `N`.

## Column counting gives linear total coefficient mass

Take absolute values in (11) and sum over `n<=N`. For a fixed omitted location `m`, its two indicators are supported on multiples of `m` and `m+1`. Hence

\[
\sum_{n\le N}
\left|
\mathbf1_{m\mid n}-\mathbf1_{m+1\mid n}
\right|
\le
\left\lfloor\frac Nm\right\rfloor
+
\left\lfloor\frac N{m+1}\right\rfloor
\le
\frac{2N}{m}.
\tag{18}
\]

Combining (11), (17), and (18),

\[
\begin{aligned}
\sum_{n\le N}|b_n|
&\le
\sum_{m\in E_N}|Y(m)|
\left(
\left\lfloor\frac Nm\right\rfloor
+
\left\lfloor\frac N{m+1}\right\rfloor
\right)\\
&\le
2N
\sum_{m\in E_N}\frac{|Y(m)|}{m}\\
&\le
\boxed{2CN(2^K-1),}
\end{aligned}
\tag{19}
\]

which proves (4). Equations (5)--(6) follow immediately.

Combining this with FD-244 yields, for exact observed zeros and `1<=K=R(N)<=N/2`, the two-regime estimate

\[
\boxed{
\sum_{N/2<n\le N}|b_n|
\ll
CN\min\!\left\{
2^K,
K\log\!\left(e+\log\frac NK\right)
\right\}.
}
\tag{20}
\]

The second term is the unrestricted sparse-weight estimate of FD-244; the first is the new exact finite-omission estimate. Thus FD-244 remains the useful bound once `K` grows, while (19) removes its artificial `log log N` loss for every fixed number of omissions.

## One omitted sample already gives the sharp linear order

Fix `e>=2` and define a response sequence

\[
Y(m)=
\begin{cases}
e,&m=e,\\
0,&m\ne e.
\end{cases}
\tag{21}
\]

Set `g=Delta Y` and `b=1*g`. By the exact inversion of FD-225, `mathscr A b=Y`. Explicitly,

\[
\boxed{
b_n
=e\left(
\mathbf1_{e\mid n}-
\mathbf1_{e+1\mid n}
\right).}
\tag{22}
\]

If `b_n` is nonzero, then `n` is divisible by `e` or `e+1`, so `n>=e` and

\[
|b_n|=e\le n.
\tag{23}
\]

Thus the unit linear envelope holds. At horizon `N=e`, the response is exactly zero at every sampled location in `[1,N]` except the single omitted point `e`, and

\[
b_e=e.
\tag{24}
\]

Consequently

\[
\sum_{e/2<n\le e}|b_n|\ge e,
\]

proving (7). Therefore no universal finite-one-hole estimate can replace the `O(N)` scale in (4) by `o(N)`.

## What this changes in the FD-241--FD-244 sampling frontier

FD-241--FD-244 progressively sharpened the cost of sparse missing data by localizing the unknown increments of `g=mu*b` and then optimizing the sparse norm of the bound

\[
|g(m)|\le Cm\sigma_{-1}(m).
\]

FD-244 correctly shows that this reciprocal-divisor sparse norm has sharp order `delta log log(1/delta)`. The present result shows that **sharpness of that auxiliary sparse norm is not yet sharpness of the exact sampling inverse**. Exact response omissions impose the adjacent-difference representation (11), and for finite defect that structure is strong enough to remove the reciprocal-divisor factor entirely.

The result does not contradict FD-244. Its exponential dependence on `K` is deliberately crude and becomes useless well before the general sparse bound does. The remaining quantitative question is now more precise: determine how the conditioning of the triangular omission-column system in (11) grows with `K` and with the arithmetic geometry of `E_N`. Any subexponential or polynomial control there would improve the actual omission term beyond FD-244 in a genuinely growing-defect regime; conversely, a matching bad family would explain where reciprocal-divisor-type losses re-enter the physical sampling problem.

This also separates the omission-count issue from the residual-variation issue of FD-242. The argument here uses exact sampled zeros. It does not improve the `V_S(N)/N` term for approximate observations, whose linear threshold is already known to be order-sharp for unrestricted signed profiles.

## Prior-art / dependency audit

A targeted search found the classical Möbius/Dirichlet inversion framework and general uncertainty-principle results about supports of Möbius pairs. Those results concern qualitative or density restrictions on simultaneous supports; they do not supply the finite-horizon triangular estimate (17)--(19) for the response coordinates used here.

No external theorem is load-bearing. Equations (9)--(11) are the exact divisor inversion already established in FD-225, and the rest is finite triangular algebra plus counting multiples. No update to `SOURCES.md` is required. No general literature-priority claim is made for triangular inversion itself; the line-specific contribution is the quantitative consequence for exact Farey/Mertens response omissions and the resulting separation from the sharp unrestricted sparse `sigma_{-1}` scale of FD-244.

## Status

**Proved.** The finite column representation, the `C(2^K-1)` omitted-amplitude bound, the `O(CN2^K)` coefficient-mass estimate, and the one-hole `Omega(N)` example are exact. The theorem concerns the relaxed signed divisor-response inverse problem. It does not assert nonnegative prime-reservoir realizability, improve a physical Mertens bound, or imply RH.