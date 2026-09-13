# FD-084 — annular occupation thickens into polynomial additive blocks

**Status:** `EXACT-DERIVED + DIVISOR-INCREMENT-BOUND + HIGH-ENERGY-OCCUPIED-SEEDS + POLYNOMIAL-ADDITIVE-BLOCKS + FIXED-POWER-WINDOW-RECURRENCE + TRANSPORT-GEOMETRY`.

`FD-083` removes the cardinality obstruction left by `FD-082`: for every fixed admissible occupation threshold, the physical good set has full counting exponent inside every fixed-power future window. Its explicit boundary is compatibility. A set of `X^(1-o(1))` integers can still be multiplicatively hostile, so abundance alone does not create an integer-ratio chain or another transport geometry on which the GCD/Schur deficits can accumulate.

The physical energy has an additional local rigidity that was not used in `FD-083`. Increasing the horizon from `N-1` to `N` changes the quotient `floor(N/r)` only on rows `r|N`. Since the quotient-shell source has exact increments of absolute value at most one, both the full Schur energy and its nonsquarefree part change by at most `N^(Theta+o(1))` per unit horizon. On the other hand the annular mechanism of `FD-078`--`FD-080` necessarily produces occupied horizons whose individual energy is `H^(2Theta-o(1))`. Such a horizon therefore cannot lose constant occupation until one moves a polynomial additive distance of almost `H^Theta`.

Let

\[
\Theta:=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\},
\]

fix a Schur head `D>=1`, and retain

\[
w(r):=\frac{J_2(r)}{r^2},
\qquad
E_{H,D}:=\sum_{D<r\le H}w(r)\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right)^2,
\]

\[
U_{H,D}:=\sum_{\substack{D<r\le H\\\mu(r)=0}}w(r)\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right)^2,
\qquad
\nu_{H,D}:=\frac{U_{H,D}}{E_{H,D}},
\tag{1}
\]

with `nu_(H,D)=0` when `E_(H,D)=0`. For a fixed nonsquarefree integer `q>1`, put

\[
c_q:=w(q)q^{-2\Theta}.
\tag{2}
\]

Then for every fixed

\[
0<\eta<c_q,
\qquad
0<\delta<\Theta,
\qquad
\varepsilon>0,
\tag{3}
\]

there is `X_0=X_0(D,q,eta,delta,epsilon)` such that every `X>=X_0` admits an integer `H` for which

\[
\boxed{
[H,H+\lfloor H^{\Theta-\delta}\rfloor]
\subset (X,X^{1+\varepsilon}]
}
\tag{4}
\]

and

\[
\boxed{
\nu_{N,D}>\eta
\quad\text{for every integer }N\in
[H,H+\lfloor H^{\Theta-\delta}\rfloor].
}
\tag{5}
\]

Thus the constant-occupation set is not merely of full counting exponent: **every fixed-power future window contains a consecutive additive block of occupied horizons whose length has any fixed exponent below `Theta`.** In particular, taking `q=4` gives an unconditional statement for every fixed `eta<3/64`; since `Theta>=1/2`, the guaranteed block exponent may be taken arbitrarily close to `1/2` without RH. Under RH, the admissible four-adic threshold is every `eta<3/16` and the block exponent is arbitrarily close to `1/2`.

This is a genuine strengthening of the geometry supplied by `FD-083`, but it does not finish the accumulation problem. Consecutive additive blocks need not contain two distinct horizons with an integer ratio, and a sequence of long blocks can still be placed on mutually incompatible multiplicative rays. What is removed is the stronger escape in which constant occupation consists only of isolated, combinatorially unstructured points.

## 1. One horizon step changes only divisor-indexed Jordan rows

`FD-033` gives

\[
\mathcal H(k)=\sum_{n\le k}c(n),
\qquad
c(n)=\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}n.
\tag{6}
\]

Hence

\[
|c(n)|\le1,
\qquad
\mathcal H(k)-\mathcal H(k-1)=c(k).
\tag{7}
\]

Fix `N>D`. For a row `r<=N-1`,

\[
\left\lfloor\frac Nr\right\rfloor-
\left\lfloor\frac{N-1}{r}\right\rfloor
=
\begin{cases}
1,&r\mid N,\\
0,&r\nmid N.
\end{cases}
\tag{8}
\]

The new row `r=N` obeys the same formula if the previous quotient is interpreted as zero and `mathcal H(0)=0`. Therefore the energy increment is exactly

\[
\boxed{
E_{N,D}-E_{N-1,D}
=
\sum_{\substack{r\mid N\\r>D}}
w(r)
\left[
\mathcal H(N/r)^2-
\mathcal H(N/r-1)^2
\right].
}
\tag{9}
\]

Likewise,

\[
\boxed{
U_{N,D}-U_{N-1,D}
=
\sum_{\substack{r\mid N\\r>D\\\mu(r)=0}}
w(r)
\left[
\mathcal H(N/r)^2-
\mathcal H(N/r-1)^2
\right].
}
\tag{10}
\]

These identities are stronger than a generic Lipschitz estimate for the energy: a unit change of horizon does not perturb all `H` Jordan rows, only the divisor lattice of the new horizon.

For `k>=1`, (7) gives

\[
\left|
\mathcal H(k)^2-\mathcal H(k-1)^2
\right|
\le2|\mathcal H(k-1)|+1.
\tag{11}
\]

By `FD-046`, for every fixed `sigma>Theta`,

\[
|\mathcal H(k)|\ll_\sigma k^\sigma.
\tag{12}
\]

Since `0<w(r)<=1`, equations (9)--(12) imply

\[
|E_{N,D}-E_{N-1,D}|+|U_{N,D}-U_{N-1,D}|
\ll_\sigma
N^\sigma\sum_{r\mid N}r^{-\sigma}.
\tag{13}
\]

Using the elementary divisor bound `tau(N)<<_gamma N^gamma` for every fixed `gamma>0`, we obtain the local physical-energy estimate

\[
\boxed{
|E_{N,D}-E_{N-1,D}|+|U_{N,D}-U_{N-1,D}|
\ll_{D,\sigma,\gamma}N^{\sigma+\gamma}
}
\tag{14}
\]

for every fixed `sigma>Theta` and `gamma>0`. The dependence on `D` is harmless here; in fact the displayed divisor estimate is uniform after the fixed head is removed.

## 2. Constant annular occupation must contain a near-frontier-energy point

Fix a power-annulus parameter `0<alpha<1` and write, as in `FD-078`--`FD-080`,

\[
\lambda_H:=\log\frac{H+1}{H},
\]

\[
A_\alpha(Y):=
\sum_{Y^{1-\alpha}<H\le Y}\lambda_HE_{H,D},
\qquad
B_\alpha(Y):=
\sum_{Y^{1-\alpha}<H\le Y}\lambda_HU_{H,D},
\]

\[
\Omega_\alpha(Y):=\frac{B_\alpha(Y)}{A_\alpha(Y)}.
\tag{15}
\]

`FD-078` proves the full annular energy exponent

\[
\boxed{A_\alpha(Y)=Y^{2\Theta+o(1)}.}
\tag{16}
\]

Choose fixed thresholds

\[
\eta<\eta_1<\eta_0<c_q.
\tag{17}
\]

Suppose an endpoint `Y` satisfies

\[
\Omega_\alpha(Y)>\eta_0.
\tag{18}
\]

Let

\[
\mathcal G_{\eta_1}(Y)
:=
\{H:Y^{1-\alpha}<H\le Y,\ \nu_{H,D}>\eta_1\}.
\]

Exactly as in the energy-fraction step of `FD-083`, if

\[
A_{\eta_1}(Y)
:=
\sum_{H\in\mathcal G_{\eta_1}(Y)}\lambda_HE_{H,D},
\]

then `0<=nu<=eta_1` off the good set and `nu<=1` on it give

\[
\boxed{
A_{\eta_1}(Y)
>
\frac{\eta_0-\eta_1}{1-\eta_1}
A_\alpha(Y).
}
\tag{19}
\]

Now fix any `kappa` with `0<kappa<2Theta`. The total annular weight of horizons satisfying

\[
E_{H,D}\le H^{2\Theta-\kappa}
\tag{20}
\]

is bounded, using `lambda_H<=1/H`, by

\[
\sum_{H\le Y}\lambda_HH^{2\Theta-\kappa}
\le
\sum_{H\le Y}H^{2\Theta-\kappa-1}
\ll_{\kappa,\Theta}Y^{2\Theta-\kappa}.
\tag{21}
\]

By (16), the right side is `o(A_alpha(Y))`. Therefore (19) cannot be supported entirely on the low-energy set (20). Every sufficiently large endpoint satisfying (18) contains at least one horizon `H` with

\[
\boxed{
\nu_{H,D}>\eta_1,
\qquad
E_{H,D}>H^{2\Theta-\kappa}.
}
\tag{22}
\]

This is the load-bearing refinement of the `FD-083` abundance statement. It does not merely locate an occupied point; it locates one whose full physical Schur energy is within an arbitrarily small fixed power of the maximal zero-frontier scale.

## 3. Near-frontier energy turns one occupied point into a long consecutive block

Fix the `delta` from (3), and apply (22) with

\[
\kappa:=\frac\delta2.
\tag{23}
\]

Choose in (14)

\[
\sigma:=\Theta+\frac\delta{16},
\qquad
\gamma:=\frac\delta{16}.
\tag{24}
\]

Then one unit of horizon motion costs at most

\[
N^{\Theta+\delta/8}
\]

up to a fixed constant. Let

\[
L_H:=\left\lfloor H^{\Theta-\delta}\right\rfloor.
\tag{25}
\]

Since `Theta<=1` and `delta>0`, `L_H=o(H)`. Uniformly for `0<=h<=L_H`, telescoping (14) over `[H,H+h]` gives

\[
\begin{aligned}
|E_{H+h,D}-E_{H,D}|
+|U_{H+h,D}-U_{H,D}|
&\ll
L_H H^{\Theta+\delta/8}\\
&\ll
H^{2\Theta-7\delta/8}.
\end{aligned}
\tag{26}
\]

The seed bound (22)--(23) is

\[
E_{H,D}>H^{2\Theta-\delta/2}.
\tag{27}
\]

Thus the right side of (26) is `o(E_(H,D))`, with a spare factor `H^(-3delta/8)`. Since `U_(H,D)>eta_1 E_(H,D)` and `eta_1>eta`, for all sufficiently large seeds the perturbations in (26) are small enough that

\[
U_{H+h,D}>\eta E_{H+h,D}
\qquad(0\le h\le L_H).
\tag{28}
\]

This proves the block conclusion once such a seed is placed in the desired physical window.

The same argument works two-sidedly for `|h|<=H^(Theta-delta)` after staying above the fixed head, but the one-sided form is more convenient for fitting the whole block inside a prescribed future window.

## 4. Every fixed-power future window contains one whole block

It remains only to combine the seed theorem with the first-passage placement already available from `FD-080`. Fix the target window exponent `epsilon>0`. Choose real numbers

\[
1<t<1+\varepsilon,
\qquad
\beta>0,
\qquad
t(1+\beta)<1+\varepsilon,
\tag{29}
\]

and set

\[
\alpha:=1-\frac1t.
\tag{30}
\]

For a large starting point `X`, put

\[
Z:=\lceil X^t\rceil.
\tag{31}
\]

Apply `FD-080` at threshold `eta_0<c_q`, with the fixed annulus parameter (30) and fixed-power allowance `beta`. It supplies an endpoint `Y` satisfying

\[
Z<Y\le Z^{1+\beta},
\qquad
\Omega_\alpha(Y)>\eta_0.
\tag{32}
\]

The annulus lies strictly after `X` at its lower edge:

\[
Y^{1-\alpha}=Y^{1/t}>Z^{1/t}\ge X.
\tag{33}
\]

By Section 2, this annulus contains a seed `H` satisfying (22)--(23), so `H>X`. On the other hand, (29)--(32) give

\[
H\le Y\le X^{t(1+\beta)+o(1)}
\]

with a strict exponent margin below `1+epsilon`. Since `L_H=o(H)`, for all sufficiently large `X` this margin absorbs the whole future block:

\[
H+L_H<X^{1+\varepsilon}.
\tag{34}
\]

Equations (28), (33), and (34) prove (4)--(5).

For the unconditional numerical specialization, take `q=4`. Since `w(4)=3/4` and `Theta<=1`,

\[
c_4=\frac34\,4^{-2\Theta}\ge\frac3{64}.
\tag{35}
\]

Hence every fixed `eta<3/64`, every fixed `epsilon>0`, and every fixed `0<delta<Theta` satisfy the theorem without assuming RH. Hardy's theorem gives `Theta>=1/2`, so for every fixed `0<delta<1/2` the same blocks have length at least `H^(1/2-delta)` after weakening the exponent. If RH holds, `Theta=1/2` and (35) sharpens to `c_4=3/16`.

## 5. What this changes, and the remaining obstruction

`FD-073` already thickens a strict normalized **source record** into an additive block by the one-Lipschitz law for `mathcal H`. That theorem is strongest on a false-RH record subsequence and propagates the record to causal horizons of the special form `4Y`. The present result is different in both input and output. It starts from the global annular occupation mechanism of `FD-078`--`FD-080`, requires no record, and proves that the physical occupation ratio `nu_(H,D)` itself has polynomially long constant-strength blocks recurring inside every fixed-power future window.

`FD-083` proves much greater point-count abundance but no local organization. The present theorem adds organization: the good set is **additively thick**, with recurrent blocks of length `H^(Theta-delta)` for every fixed `delta>0`. This is exactly the sort of extra geometry that a pure cardinality control such as the prime numbers would not possess.

However additive thickness is not yet the multiplicative compatibility required by the existing GCD-duality accumulation theorems. An interval `[H,H+o(H)]` contains no pair with ratio `2`, and one can place arbitrarily long additive intervals on scales chosen to avoid a prescribed multiplicative chain. Therefore (4)--(5) must not be fed directly into `FD-022` or `FD-023` as though they supplied an integer-ratio schedule. The new frontier is narrower: any remaining escape must preserve constant occupation on long consecutive horizon blocks while arranging those blocks so that no usable multiplicative or floor-quotient transport accumulates a power-scale gain.

One plausible next test is to derive a transport inequality whose cost depends continuously on the additive displacement of the horizon, rather than requiring exact integer ratios. Another is to use reciprocal-floor realizability between two long occupied blocks and ask whether block lengths of exponent `Theta` are enough to force a shared quotient coordinate before the scale separation becomes too large. Neither implication is established here.

## 6. Stress tests and prior-art boundary

The proof is fixed-head. If `D` moves with `H`, the cutoff itself crosses rows and equations (9)--(10) acquire additional terms; no growing-head block theorem is claimed. The thresholds are strict: the argument uses `eta<eta_1<eta_0<c_q`, so nothing is proved at `eta=c_q`. Likewise `delta>0` is fixed before `X` tends to infinity. The theorem gives every exponent below `Theta` separately; it does not assert a uniform `H^(Theta-o(1))` block with an unspecified rate.

The near-frontier seed extraction uses the **full limit** (16), not merely a limsup energy exponent. Its low-energy estimate also uses the logarithmic horizon weight `lambda_H`; replacing that weight by counting measure would be a different statement. The local stability step uses both the exact divisor support (9)--(10) and the source increment bound (7). If either the divisor-step identity or the exponent in (14) failed, the block length could collapse; equations (8)--(14) isolate the falsification points explicitly.

A targeted literature audit covered the Franel--Landau/Farey discrepancy literature, Mertens-based Farey formulas, recent local Farey discrepancy estimates, GCD-matrix formulations, and searches for local-stability or Jordan-energy block results. García's 2025 local-discrepancy formulas and 2026 average-local-discrepancy theorem remain neighboring prior art already anchored in `SOURCES.md`; the Cox--Ghosh--Sultanow Farey/Mertens work concerns different Mertens analogues and conjectural relations. No located source states the divisor-supported increment identities (9)--(10) for this Schur/Jordan physical energy or the consequence (4)--(5). No novelty claim is inferred from absence of a search hit.

No new external theorem is load-bearing. The analytic inputs are already persisted and sourced in the line: the exact quotient-shell coefficient law from `FD-033`, the zero-frontier envelope from `FD-046`, the annular full-energy exponent from `FD-078`, and the exact annular recurrence/first passage from `FD-080`. Accordingly `SOURCES.md` requires no new anchor.

The decisive control against overinterpretation is simple. Additive thickness alone does not imply multiplicative composability: a union of increasingly long intervals can still be placed so that no selected interval meets any fixed finite collection of its prescribed multiplicative images. Therefore this finding advances the live `FD-083` compatibility frontier but does not close it, does not improve the Franel exponent, and does not prove RH.