# FD-223 — Vinogradov–Korobov-scale switched blocks remain blind below literal Euler coverage

- **Date:** 2026-09-20
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** growing same-source horizon block / Vinogradov–Korobov uniformization / divisor-reservoir countermodel / quantitative triangular repair / pre-coverage obstruction
- **Depends on:** FD-222, FD-005
- **Classification:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + GROWING-HORIZON + VINOGRADOV-KOROBOV-SCALE + UNIFORM-DIVISOR-RESERVOIRS`

## Claim

FD-222 proves switched blindness uniformly for every fixed multiple of `log log N`. Its only quantitative losses are exponential in the block length, while the analytic inputs used there were deliberately only a classical prime-number-theorem remainder and arbitrary fixed log-power Mertens cancellation. Replacing those two inputs by their unconditional Vinogradov–Korobov-scale forms extends the same countermodel much further.

Put

\[
\Phi(x)=\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}},
\]

and retain the periodic scheduler

\[
q_t=\begin{cases}
0,&t\equiv0\pmod3,\\
3,&t\equiv1,2\pmod3,
\end{cases}
\qquad
q(n)=q_{\lfloor\log_2 n\rfloor},
\]

with

\[
\mathcal C_q^X(n)=(T-I)^{q+1}X(n),
\qquad (TF)(n)=F(2n).
\]

Fix `0<beta<1`. There is a constant `kappa_beta>0` such that, for all sufficiently large integers `N` and every integer

\[
1\le J\le \kappa_\beta\Phi(N),
\]

there is one deterministic sequence

\[
\xi_n^{(N)}\in\{-1,0,1\},
\qquad
(\xi_n^{(N)})^2=\mu(n)^2,
\qquad
\xi_1^{(N)}=1,
\]

which obeys the exact Euler relation

\[
\boxed{
\xi_{pn}^{(N)}=-\xi_n^{(N)}
\quad(p\le\beta N,\ p\nmid n)
}
\]

globally. Writing

\[
X_N(x)=\sum_{n\le x}\xi_n^{(N)},
\]

and, as in FD-222,

\[
e_j=j+q(2^jN)+1,
\qquad
E=\max_{0\le j<J}e_j,
\qquad
D=2^E,
\]

so that `2^J<=D<=8*2^J`, one can arrange simultaneously

\[
\boxed{
\max_{0\le j<J}
\left|
\mathcal C_{q(2^jN)}^{X_N}(2^jN)
\right|
\ll_\beta D
}
\]

and

\[
\boxed{
X_N(N)\asymp_\beta\frac{N}{D\log N}.
}
\]

Consequently, throughout the certified range,

\[
\max_{j<J}|
\mathcal C_{q(2^jN)}^{X_N}(2^jN)|
\le
\exp(O_\beta(\Phi(N)))
=N^{o(1)},
\]

whereas

\[
|X_N(N)|
=
N\exp(-O_\beta(\Phi(N)))/\log N
=N^{1-o(1)}.
\]

Thus the switched observation block can have **stretched-logarithmic length** while remaining subpower-small, even though the same source has an almost-linear earlier-prefix defect and satisfies every selected Möbius Euler law through the fixed fraction `beta N`.

As in FD-222, this is a finite-horizon comparison source: it may depend on `(N,J)`. No permanent source valid on a cofinal sequence of horizons is constructed.

## 1. The exact FD-222 skeleton needs no change

All finite identities from FD-222 remain valid for arbitrary `J` as long as the relevant prime reservoirs exist and the triangular correction fits inside them. In particular,

\[
J\le E\le J+3,
\qquad
2^J\le D\le8\,2^J.
\]

Choose

\[
h=
\min\left\{
\frac{1-\beta}{2},
\frac{1}{2(D+1)}
\right\},
\qquad
I_d=((d-h)N,dN),
\quad 1\le d\le D.
\]

Then `h asymp_beta D^{-1}`, the intervals are disjoint and lie above the constrained-prime cutoff `beta N`, and the floor table freezes exactly:

\[
\left\lfloor\frac{2^kN}{r}\right\rfloor
=
\left\lfloor\frac{2^k}{d}\right\rfloor
\qquad
(r\in I_d,\ 0\le k\le E).
\]

Let `Q_N` be the product of the primes at most `beta N`. Starting from the physical squarefree core signs and flipping a core prime `r in I_d` changes every sampled prefix by exactly

\[
2M\!\left(\left\lfloor\frac{2^k}{d}\right\rfloor\right).
\]

Hence flipping the same number `A` of primes in every reservoir produces the constant sample perturbation `2A`, by the exact FD-005 identity

\[
\sum_{d\le n}M\!\left(\left\lfloor\frac nd\right\rfloor\right)=1.
\]

Every scheduled positive-order difference annihilates that constant vector. None of this has a `J`-dependent conditioning loss.

The only two places where FD-222 used `J=O(log log N)` were therefore analytic: guaranteeing `A` primes in every shrinking reservoir and showing that the correction of the physical Möbius baseline is small compared with `A`.

## 2. Vinogradov–Korobov inputs

Two unconditional estimates are now used as load-bearing literature inputs. The current Lee--Leong bound gives constants `c_M>0` and `C_M>0` such that, for all sufficiently large `x`,

\[
|M(x)|
\le
C_M x\log x\,e^{-c_M\Phi(x)}.
\tag{1}
\]

For primes, the Korobov--Vinogradov zero-free region together with the prime-number-theorem remainder machinery gives constants `c_theta>0` and `C_theta>0` such that

\[
|\vartheta(x)-x|
\le
C_\vartheta x\,e^{-c_\vartheta\Phi(x)}
\tag{2}
\]

for all sufficiently large `x`; harmless fixed powers of logarithms in modern explicit formulations may be absorbed by reducing `c_theta`.

Now suppose

\[
J\le\kappa\Phi(N).
\]

Then

\[
\log D\le (\kappa\log2)\Phi(N)+O(1)=o(\log N),
\]

so `D=N^{o(1)}`. Uniformly for `N<=x<=DN`,

\[
\Phi(x)=(1+o(1))\Phi(N),
\qquad
\log x=(1+o(1))\log N.
\tag{3}
\]

After weakening the constants once, (1)--(2) can therefore be used uniformly over every sampled scale appearing in the block.

## 3. Every divisor reservoir still has macroscopic prime capacity

For `d<=D`, (2)--(3) give

\[
\vartheta(dN)-\vartheta((d-h)N)
=
hN
+O\!\left(
DN e^{-c'_\vartheta\Phi(N)}
\right)
\]

for some `c'_theta>0`. Since `h asymp_beta D^{-1}`, the error-to-main ratio is

\[
O_\beta\!\left(
D^2e^{-c'_\vartheta\Phi(N)}
\right).
\]

Because `D<=8*2^J`, this tends to zero whenever `kappa` is sufficiently small that

\[
2\kappa\log2<c'_\vartheta.
\tag{4}
\]

Thus, uniformly for every `d<=D`,

\[
|I_d\cap\mathbb P|
\gg_\beta
\frac{N}{D\log N}.
\tag{5}
\]

Choose a sufficiently small fixed `a_beta>0` and put

\[
A=\left\lfloor
 a_\beta\frac{N}{D\log N}
\right\rfloor.
\tag{6}
\]

The positive divisor-reservoir null cycle from FD-222 therefore survives unchanged throughout the stretched-logarithmic block.

## 4. The triangular repair also fits at Vinogradov–Korobov depth

Let

\[
b_j=
\mathcal C_{q(2^jN)}^{M}(2^jN)
\]

be the physical baseline vector. FD-222 constructs pivot reservoirs `d_j=2^{e_j}` and a response matrix `V`. Ordered by increasing `e_j`, it is lower triangular with diagonal `2` and satisfies

\[
|V_{ij}|\le32\,2^{e_i-e_j}.
\]

With

\[
R=\operatorname{diag}(2^{e_i}),
\qquad
B=R^{-1}VR,
\]

one has the elementary conditioning bound

\[
\|B^{-1}\|_\infty\le17^J.
\tag{7}
\]

Estimate (1), the `l^1` norm at most `16` of every scheduled difference, and (3) give

\[
\|R^{-1}b\|_\infty
\ll
N\log N\,e^{-c'_M\Phi(N)}
\tag{8}
\]

for some `c'_M>0`. Hence the exact real correction `delta=-V^{-1}b` satisfies

\[
\|\delta\|_\infty
\ll
D\,17^J N\log N\,e^{-c'_M\Phi(N)}.
\tag{9}
\]

Relative to the reservoir occupancy (6),

\[
\frac{\|\delta\|_\infty}{A}
\ll_\beta
D^2 17^J(\log N)^2e^{-c'_M\Phi(N)}
\ll_\beta
68^J(\log N)^2e^{-c'_M\Phi(N)}.
\tag{10}
\]

Choose `kappa_beta>0` smaller, if necessary, so that in addition to (4),

\[
\kappa_\beta\log68<c'_M.
\tag{11}
\]

Then (10) tends to zero. The real correction therefore stays well inside every prime capacity. Rounding each corrected count to the nearest integer produces, exactly as in FD-222, a residual row error at most `16D`. This proves the observation bound in the claim.

## 5. The earlier-prefix defect remains almost linear

Only `I_1` lies below `N`, while every pivot reservoir has `d_j>=2`. Thus the triangular repair does not modify the first prefix. Each of the `A` low-reservoir flips changes `X_N(N)` by exactly `2`, so

\[
X_N(N)=M(N)+2A.
\]

From (1) and (6),

\[
\frac{|M(N)|}{A}
\ll_\beta
D(\log N)^2e^{-c_M\Phi(N)}=o(1)
\]

after the same choice of a sufficiently small `kappa_beta`. Therefore

\[
X_N(N)=(2a_\beta+o(1))\frac{N}{D\log N},
\]

which is `N^(1-o(1))` because `log D=O(Phi(N))=o(log N)`.

The selected Euler relations remain exact. Since `D=N^{o(1)}`, eventually `beta N>D`, so every small quotient entering the response table has all prime factors already inside `Q_N`; the exact response formula used by FD-222 is therefore still valid.

## 6. Boundary, prior art, and consequence

This result moves the certified noncoercive regime from `J=O(log log N)` to

\[
J=O\!\left(
(\log N)^{3/5}(\log\log N)^{-1/5}
\right).
\]

The exponent is **not claimed sharp**. It is where the present construction can balance its exponential-in-`J` geometric/conditioning losses against the unconditional stretched-exponential prime and Möbius savings supplied by the Korobov--Vinogradov zero-free region. Failure of this proof beyond that range is not an obstruction.

A literature audit found the expected classical and modern sources for the Vinogradov--Korobov prime-number-theorem remainder and Mertens decay, and the established literature on Farey discrepancy, but no source for this partial-Euler, divisor-reservoir switched-horizon countermodel or the resulting capacity law. The novelty claim is therefore only the repository-specific derived consequence: combining those analytic estimates with the exact FD-005/FD-222 response geometry.

The quantifier boundary is unchanged and remains essential. For each pair `(N,J)` the comparison source may be rebuilt. The theorem neither constructs one persistent source along infinitely many horizons nor weakens the elementary fact that eventually exhaustive exact Euler coherence forces the Möbius function itself.

Thus `log log N` was not a structural threshold. **Below literal Euler prefix coverage, switched blindness survives at least through a Vinogradov--Korobov stretched-logarithmic number of coherently observed dyadic horizons.** The live boundary is pushed to substantially faster block growth or to a persistence requirement that prevents retuning the source with `(N,J)`.