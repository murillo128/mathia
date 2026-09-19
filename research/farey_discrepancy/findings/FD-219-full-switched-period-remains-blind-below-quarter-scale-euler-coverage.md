# FD-219 — A full switched period remains blind below quarter-scale Euler coverage

- **Date:** 2026-09-19
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** same-source multi-horizon coherence / switched root-filter countermodel / exact prime-reservoir cancellation / sharp finite-block representation boundary
- **Depends on:** FD-218, FD-029
- **Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + THREE-HORIZON-COHERENCE + FULL-SWITCHED-PERIOD + SHARP-QUARTER-SCALE-THRESHOLD + EXACT-RESERVOIR-CANCELLATION`

## Claim

`FD-218` shows that one source can remain blind at the adjacent horizons `N` and `2N` whenever the later fractional Euler cutoff has not yet reached the earlier prefix. The next persistence test is a **complete period** of the switched schedule,

\[
q_j=(0,3,3,0,3,3,\ldots),
\qquad
q(n)=q_{\lfloor\log_2 n\rfloor},
\]

with

\[
\mathcal C_q^X(n)=(T-I)^{q+1}X(n),
\qquad (TF)(n)=F(2n).
\]

Fix `0<theta<1/4`. For every sufficiently large integer `N` satisfying

\[
\lfloor\log_2N\rfloor\equiv0\pmod3,
\]

there is one deterministic sequence

\[
\xi_n^{(N)}\in\{-1,0,1\},
\qquad
(\xi_n^{(N)})^2=\mu(n)^2,
\qquad
\xi_1^{(N)}=1,
\]

which obeys globally

\[
\boxed{
\xi_{pn}^{(N)}=-\xi_n^{(N)}
\quad
(p\le4\theta N,\ p\nmid n).
}
\tag{1}
\]

Hence the same source satisfies every requested Euler relation `p<=theta H` at all three horizons

\[
H\in\{N,2N,4N\}.
\]

Writing

\[
X_N(x)=\sum_{n\le x}\xi_n^{(N)},
\]

one can arrange simultaneously

\[
\boxed{|\mathcal C_0^{X_N}(N)|\le1,}
\qquad
\boxed{|\mathcal C_3^{X_N}(2N)|\le12,}
\qquad
\boxed{|\mathcal C_3^{X_N}(4N)|\le21,}
\tag{2}
\]

while

\[
\boxed{
X_N(N)\asymp_\theta \frac{N}{\log N}.
}
\tag{3}
\]

The congruence condition makes the three scheduled depths exactly `(0,3,3)`, so (2) controls one complete switching period rather than two selected phases.

The threshold is sharp for prefix identification in this three-horizon source class. If `theta>=1/4`, the requirement at `4N` includes every prime `p<=N`. Squarefree support, `xi_1=1`, and the Euler law then force

\[
\boxed{
\xi_n=\mu(n)\quad(n\le N).
}
\tag{4}
\]

Thus adding the third coupled horizon pushes the first-crossing threshold from `1/2` to `1/4`, but persistence through a whole switched period still does not by itself remove the blind reservoir below that geometric coverage point.

As in `FD-218`, (4) is an information statement, not an RH estimate: it returns the physical Möbius prefix but gives no new bound for `M(N)`.

## 1. One source carries all three Euler windows

Put

\[
Y=4\theta N,
\qquad
P_N=\{p\text{ prime}:p\le Y\},
\qquad
Q_N=\prod_{p\in P_N}p.
\]

Every squarefree integer has a unique factorization `n=dm`, with `d|Q_N` and `(m,Q_N)=1`. Choose core signs `eta_m in {-1,+1}`, set

\[
\xi_{dm}=\mu(d)\eta_m
\]

on squarefree integers, and put `xi_n=0` on nonsquarefree integers. Then (1) holds identically for every constrained prime.

Start from the physical core `eta_m=mu(m)` and alter only selected unconstrained core primes `r>Y`, changing `eta_r` from `-1` to `+1` and leaving every other core coordinate physical. For the reservoirs below, every selected prime satisfies

\[
r>\frac{64}{65}N.
\]

All switched observations in (2) sample `X_N(x)` only at

\[
x\in\{N,2N,4N,8N,16N,32N,64N\}.
\]

Therefore `floor(x/r)<=64`. Since `theta>0` is fixed, all primes at most `64` belong to `P_N` for sufficiently large `N`, and the contribution of one flipped core prime is exactly

\[
2\sum_{\substack{d\mid Q_N\\d\le x/r}}\mu(d)
=
2M\!\left(\left\lfloor\frac xr\right\rfloor\right).
\]

For any finite flip set `R`,

\[
\boxed{
X_N(x)-M(x)
=
2\sum_{r\in R}M\!\left(\left\lfloor\frac xr\right\rfloor\right)
}
\tag{5}
\]

at every sampled point. Thus the three-horizon problem again becomes an exact finite response-vector problem, but now with three simultaneous observation coordinates.

## 2. Four fixed prime reservoirs span the full period

Let

\[
a_\theta=\max\{4\theta,64/65\}
\]

and use the four disjoint prime reservoirs

\[
\begin{aligned}
L&=(a_\theta N,N],\\
H_1&=(32N/29,64N/57),\\
H_2&=(64N/21,16N/5),\\
H_3&=(32N/7,64N/13).
\end{aligned}
\tag{6}
\]

Every prime in these intervals exceeds `Y`. On the seven sampled multiples of `N`, the floor vectors are constant inside each open interval:

\[
\begin{array}{c|ccccccc}
 &N&2N&4N&8N&16N&32N&64N\\ \hline
L   &1&2&4&8&16&32&64\\
H_1 &0&1&3&7&14&28&57\\
H_2 &0&0&1&2&5&10&20\\
H_3 &0&0&0&1&3&6&13.
\end{array}
\tag{7}
\]

Using the exact small Mertens values

\[
\begin{gathered}
M(1)=1,\ M(2)=0,\ M(3)=-1,\ M(4)=-1,\ M(5)=-2,\ M(6)=-1,\ M(7)=-2,\\
M(8)=-2,\ M(10)=-1,\ M(13)=-3,\ M(14)=-2,\ M(16)=-1,\ M(20)=-3,\\
M(28)=-1,\ M(32)=-4,\ M(57)=-1,\ M(64)=-1,
\end{gathered}
\]

formula (5) gives the exact response triple

\[
(\Delta\mathcal C_0(N),\Delta\mathcal C_3(2N),\Delta\mathcal C_3(4N))
=
\begin{cases}
(-2,-16,+32),&r\in L,\\
(+2,0,-4),&r\in H_1,\\
(0,+6,-20),&r\in H_2,\\
(0,+18,-18),&r\in H_3.
\end{cases}
\tag{8}
\]

The high-reservoir response matrix

\[
\begin{pmatrix}
2&0&0\\
0&6&18\\
-4&-20&-18
\end{pmatrix}
\]

has determinant `504`, so the three high reservoirs span all three observation coordinates over `R`. More importantly for the construction, the real repair counts needed after `A` low flips are positive multiples of `A`.

The prime number theorem yields

\[
|L|\sim(1-a_\theta)\frac N{\log N},
\]

and

\[
|H_1|\sim\frac{32}{1653}\frac N{\log N},
\qquad
|H_2|\sim\frac{16}{105}\frac N{\log N},
\qquad
|H_3|\sim\frac{32}{91}\frac N{\log N}.
\tag{9}
\]

All four constants are positive when `theta<1/4`.

## 3. Repair all three observations while retaining a macroscopic prefix

Choose a fixed `kappa_theta>0` small enough that a `kappa_theta N/log N` subreservoir fits comfortably inside each interval in (9), and put

\[
A=\left\lfloor\kappa_\theta\frac N{\log N}\right\rfloor.
\]

Let the physical Möbius baselines be

\[
b_0=\mathcal C_0^M(N),
\qquad
b_1=\mathcal C_3^M(2N),
\qquad
b_2=\mathcal C_3^M(4N).
\]

Each is a fixed finite linear combination of values `M(cN)`. The Davenport cancellation bound already anchored in `SOURCES.md` gives

\[
b_0,b_1,b_2=o(N/\log N).
\tag{10}
\]

If the high-reservoir counts were allowed to be real, the exact solution cancelling all three coordinates after `A` low flips would be

\[
\begin{aligned}
B_*&=A-\frac{b_0}{2},\\
C_*&=\frac67A+\frac17b_0+\frac1{14}b_1+\frac1{14}b_2,\\
D_*&=\frac{38}{63}A-\frac1{21}b_0-\frac5{63}b_1-\frac1{42}b_2.
\end{aligned}
\tag{11}
\]

By (10), these are respectively `(1+o(1))A`, `(6/7+o(1))A`, and `(38/63+o(1))A`. Hence, after choosing `kappa_theta` sufficiently small, all three counts lie strictly inside the capacities in (9).

Take `B,C,D` to be nearest integers to `B_*,C_*,D_*` and flip that many primes from `H_1,H_2,H_3`. Equation (8) and independent nearest-integer errors of size at most `1/2` give

\[
|\mathcal C_0^{X_N}(N)|\le1,
\]

\[
|\mathcal C_3^{X_N}(2N)|\le 6/2+18/2=12,
\]

and

\[
|\mathcal C_3^{X_N}(4N)|
\le4/2+20/2+18/2=21.
\]

This proves (2). Only the `A` low-reservoir primes lie below `N`, so

\[
X_N(N)=M(N)+2A
=(2\kappa_\theta+o(1))\frac N{\log N}
\tag{12}
\]

by Davenport again, proving (3).

The integer lattice generated by the high response vectors has finite index rather than index one; this is why the statement keeps fixed `O(1)` residuals instead of claiming exact zero. That distinction is harmless at the RH-critical scale and prevents an artificial divisibility assumption on the physical baselines.

## 4. Quarter scale is the exact first-crossing point for the prefix

Suppose now `theta>=1/4`. The requirement at the last horizon includes every prime

\[
p\le4\theta N\ge N.
\]

For any squarefree `n<=N`, all prime factors of `n` are therefore constrained. Starting from `xi_1=1`, repeated application of the Euler law gives

\[
\xi_n=(-1)^{\omega(n)}=\mu(n).
\]

Both sequences vanish on nonsquarefree integers, so (4) follows.

The three-horizon threshold is therefore a literal first-crossing law: the final constraint window reaches the original prefix exactly at `theta=1/4`. Below that point, even **one full period of the nonstationary switched observable** can be repaired by a common source while preserving an `N/log N` defect at the initial horizon. Above it, the source prefix is already physically identified before the observation bounds are used.

This does not yet classify arbitrary longer blocks. In particular, after the `(0,3,3)` period the next scheduled depth returns to `0`, so the largest dyadic sample used by the observation drops relative to the preceding `q=3` phase. The simple strictly increasing support geometry exploited in (6)--(8) does not automatically iterate to a fourth horizon. Treating that next phase requires a new coupled reservoir construction rather than a formal repetition of the present argument.

## 5. Representation audit, prior art, and research consequence

The countermodel uses one arithmetic source for all three horizons, not three retuned sources. Its squarefree zero set and unit amplitudes are physical, and every Euler relation through the largest requested cutoff holds globally. The remaining nonphysical freedom is explicit: unconstrained core-prime coordinates above `4 theta N` may be chosen independently, and the resulting source still depends on the finite horizon block.

The construction was stress-tested at the exact finite level: the floor cells in (7) are disjoint fixed-ratio prime intervals, the response matrix in (8) has nonzero determinant `504`, and the only asymptotic inputs are PNT capacity and the already-anchored Davenport estimate that makes the physical baselines negligible compared with `N/log N`. No probabilistic independence or unproved prime-gap statement is used.

A prior-art search again located Aymone, *A note on multiplicative functions resembling the Möbius function* (arXiv `1908.11014`), and Liu, *Multiplicative functions resembling the Möbius function* (arXiv `2205.00972`), as nearby work on genuinely multiplicative squarefree-supported functions with prescribed prime signs. Those results do not supply this finite-block response-vector cancellation, and no theorem from them is used here. PNT and Davenport are already anchored in line-local `SOURCES.md`, so no source update is required.

The live boundary is now narrower than after `FD-218`: **same-source persistence through an entire `(0,3,3)` switching period is still noncoercive until later Euler coverage actually reaches the earlier prefix.** The next nontrivial scale is the fourth horizon `8N`, where the scheduler cycles back to depth `0` and the observation-support geometry ceases to be monotone. A successful continuation must determine whether the repair reservoir can survive that wraparound, or whether the wrap itself creates coercivity before literal prime-prefix coverage does.
