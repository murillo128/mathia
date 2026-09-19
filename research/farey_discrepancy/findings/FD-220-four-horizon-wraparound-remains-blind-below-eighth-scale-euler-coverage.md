# FD-220 — Four-horizon wraparound remains blind below eighth-scale Euler coverage

- **Date:** 2026-09-19
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** same-source multi-horizon coherence / switched root-filter countermodel / wraparound support geometry / exact prime-reservoir cancellation / sharp finite-block representation boundary
- **Depends on:** FD-219, FD-029
- **Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + FOUR-HORIZON-COHERENCE + SCHEDULE-WRAPAROUND + SHARP-EIGHTH-SCALE-THRESHOLD + EXACT-RESERVOIR-CANCELLATION`

## Claim

`FD-219` proves that one source can remain blind through the complete switched period `(0,3,3)` at the horizons `N,2N,4N`, provided the final Euler cutoff has not yet reached the original prefix. It left the next horizon open because the schedule wraps from depth `3` back to depth `0`, so the sampled-support geometry is no longer monotone.

That wraparound does **not** create coercivity before literal prime-prefix coverage.

Let

\[
q_j=(0,3,3,0,3,3,\ldots),
\qquad
q(n)=q_{\lfloor\log_2 n\rfloor},
\]

and

\[
\mathcal C_q^X(n)=(T-I)^{q+1}X(n),
\qquad (TF)(n)=F(2n).
\]

Fix `0<theta<1/8`. For every sufficiently large integer `N` satisfying

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
(p\le8\theta N,\ p\nmid n).
}
\tag{1}
\]

Hence the same source satisfies every requested Euler relation `p<=theta H` at all four horizons

\[
H\in\{N,2N,4N,8N\}.
\]

Writing

\[
X_N(x)=\sum_{n\le x}\xi_n^{(N)},
\]

one can arrange simultaneously

\[
\boxed{|\mathcal C_0^{X_N}(N)|\le1,}
\qquad
\boxed{|\mathcal C_3^{X_N}(2N)|\le20,}
\]

\[
\boxed{|\mathcal C_3^{X_N}(4N)|\le24,}
\qquad
\boxed{|\mathcal C_0^{X_N}(8N)|\le4,}
\tag{2}
\]

while

\[
\boxed{
X_N(N)\asymp_\theta \frac{N}{\log N}.
}
\tag{3}
\]

The congruence condition makes the four scheduled depths exactly `(0,3,3,0)`, so (2) crosses the first period boundary and includes the depth-zero wraparound observation.

The threshold is sharp for prefix identification in this four-horizon source class. If `theta>=1/8`, the requirement at `8N` includes every prime `p<=N`. Squarefree support, `xi_1=1`, and the Euler law then force

\[
\boxed{
\xi_n=\mu(n)\quad(n\le N).
}
\tag{4}
\]

Thus the wraparound itself supplies no earlier rigidity: the first-crossing threshold moves from `1/4` in FD-219 to `1/8`, exactly when the latest Euler window reaches the original prefix.

As in FD-218--FD-219, (4) is an information statement, not an RH estimate. It recovers the physical Möbius prefix but gives no new bound for `M(N)`.

## 1. One source carries all four Euler windows

Put

\[
Y=8\theta N,
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

Start from the physical core `eta_m=mu(m)` and alter only selected unconstrained core primes `r>Y`, changing `eta_r` from `-1` to `+1` and leaving every other core coordinate physical.

All four observations in (2) sample `X_N(x)` only at

\[
x\in\{N,2N,4N,8N,16N,32N,64N\}.
\]

We will choose every flipped prime with

\[
r>\frac{64}{65}N.
\]

Therefore `floor(x/r)<=64` at every sampled point. Since `theta>0` is fixed, all primes at most `64` belong to `P_N` for sufficiently large `N`. The contribution of one flipped core prime is then exactly

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

at every sampled point. Thus the wraparound problem is again an exact finite response-vector problem, now with four simultaneous observation coordinates.

## 2. Five fixed prime reservoirs span the wraparound block

Let

\[
a_\theta=\max\{8\theta,64/65\}
\]

and use the low reservoir

\[
L=(a_\theta N,N]
\]

and four disjoint high reservoirs

\[
\begin{aligned}
H_1&=(64N/53,16N/13),\\
H_2&=(64N/9,8N),\\
H_3&=(32N/3,64N/5),\\
H_4&=(16N,64N/3).
\end{aligned}
\tag{6}
\]

Every prime in these intervals exceeds `Y`. On the seven sampled multiples of `N`, the floor vectors are constant inside each open high interval:

\[
\begin{array}{c|ccccccc}
 &N&2N&4N&8N&16N&32N&64N\\ \hline
L   &1&2&4&8&16&32&64\\
H_1 &0&1&3&6&13&26&52\\
H_2 &0&0&0&1&2&4&8\\
H_3 &0&0&0&0&1&2&5\\
H_4 &0&0&0&0&0&1&3.
\end{array}
\tag{7}
\]

The only small Mertens values needed are

\[
\begin{gathered}
M(0)=0,\ M(1)=1,\ M(2)=0,\ M(3)=-1,\ M(4)=-1,\\
M(5)=-2,\ M(6)=-1,\ M(8)=-2,\ M(13)=-3,\\
M(16)=-1,\ M(26)=-1,\ M(32)=-4,\ M(52)=-2,\ M(64)=-1.
\end{gathered}
\]

Using (5), the exact response quadruple

\[
(\Delta\mathcal C_0(N),
 \Delta\mathcal C_3(2N),
 \Delta\mathcal C_3(4N),
 \Delta\mathcal C_0(8N))
\]

is

\[
\begin{cases}
(-2,-16,+32,+2),&r\in L,\\
(+2,+20,-26,-4),&r\in H_1,\\
(0,+10,-4,-2),&r\in H_2,\\
(0,-8,+8,+2),&r\in H_3,\\
(0,+2,-10,0),&r\in H_4.
\end{cases}
\tag{8}
\]

The high-reservoir response matrix is

\[
V=
\begin{pmatrix}
2&0&0&0\\
20&10&-8&2\\
-26&-4&8&-10\\
-4&-2&2&0
\end{pmatrix},
\qquad
\det V=112.
\tag{9}
\]

So the four high reservoirs span all four observations over `R`. More importantly, the low response lies in the **positive** cone of the high responses. If `v_L=(-2,-16,32,2)^T`, then

\[
\boxed{
V
\begin{pmatrix}
1\\[2pt]3/7\\[2pt]10/7\\[2pt]11/7
\end{pmatrix}
=-v_L.
}
\tag{10}
\]

This positivity is the exact reason the fourth, wrapped observation can be repaired without undoing the macroscopic prefix defect.

The prime number theorem yields

\[
|L|\sim(1-a_\theta)\frac N{\log N},
\]

and

\[
|H_1|\sim\frac{16}{689}\frac N{\log N},
\qquad
|H_2|\sim\frac89\frac N{\log N},
\]

\[
|H_3|\sim\frac{32}{15}\frac N{\log N},
\qquad
|H_4|\sim\frac{16}{3}\frac N{\log N}.
\tag{11}
\]

All five constants are positive when `theta<1/8`.

## 3. Repair all four observations while retaining a macroscopic prefix

Choose a fixed `kappa_theta>0` small enough that the required subreservoirs fit comfortably inside all five intervals in (11), and put

\[
A=\left\lfloor\kappa_\theta\frac N{\log N}\right\rfloor.
\]

Let the physical Möbius baselines be

\[
\begin{aligned}
b_0&=\mathcal C_0^M(N),\\
b_1&=\mathcal C_3^M(2N),\\
b_2&=\mathcal C_3^M(4N),\\
b_3&=\mathcal C_0^M(8N).
\end{aligned}
\]

Each is a fixed finite linear combination of values `M(cN)`. The Davenport cancellation bound already anchored in `SOURCES.md` gives

\[
b_0,b_1,b_2,b_3=o(N/\log N).
\tag{12}
\]

Flip `A` low-reservoir primes. If the four high-reservoir counts were allowed to be real, the unique vector `(B_*,C_*,D_*,E_*)` cancelling the four physical baselines and the low response satisfies

\[
\begin{pmatrix}B_*\\C_*\\D_*\\E_*\end{pmatrix}
= -V^{-1}\!\left(A v_L+
\begin{pmatrix}b_0\\b_1\\b_2\\b_3\end{pmatrix}
\right).
\tag{13}
\]

By (10)--(12),

\[
B_*=(1+o(1))A,
\qquad
C_*=(3/7+o(1))A,
\]

\[
D_*=(10/7+o(1))A,
\qquad
E_*=(11/7+o(1))A.
\tag{14}
\]

Hence, after choosing `kappa_theta` sufficiently small, all four real counts are positive and lie strictly inside the capacities in (11).

Take `B,C,D,E` to be nearest integers to `B_*,C_*,D_*,E_*` and flip that many primes from `H_1,H_2,H_3,H_4`. The exact real solution cancels all four observations, while each rounding error has size at most `1/2`. Using the row sums of absolute values in (9),

\[
|\mathcal C_0^{X_N}(N)|\le1,
\]

\[
|\mathcal C_3^{X_N}(2N)|
\le\frac12(20+10+8+2)=20,
\]

\[
|\mathcal C_3^{X_N}(4N)|
\le\frac12(26+4+8+10)=24,
\]

and

\[
|\mathcal C_0^{X_N}(8N)|
\le\frac12(4+2+2)=4.
\]

This proves (2).

Only the `A` low-reservoir primes lie below `N`, so

\[
X_N(N)=M(N)+2A
=(2\kappa_\theta+o(1))\frac N{\log N}
\tag{15}
\]

by Davenport again, proving (3).

As in FD-219, the integer lattice generated by the response vectors has finite index rather than index one; fixed `O(1)` residuals are therefore the natural statement after nearest-integer rounding. They are negligible at the RH-critical scale.

## 4. Eighth scale is the exact first-crossing point for the prefix

Suppose now `theta>=1/8`. The requirement at the last horizon includes every prime

\[
p\le8\theta N\ge N.
\]

For any squarefree `n<=N`, all prime factors of `n` are therefore constrained. Starting from `xi_1=1`, repeated application of the Euler law gives

\[
\xi_n=(-1)^{\omega(n)}=\mu(n).
\]

Both sequences vanish on nonsquarefree integers, so (4) follows.

The four-horizon threshold is therefore another literal first-crossing law. The schedule has now wrapped from depth `3` back to depth `0`, but that change of observation support does **not** close the unconstrained source reservoir before the latest exact-prime window reaches the original prefix.

The result does not prove an arbitrary-length theorem. The next horizon `16N` returns to depth `3`, so a five-observation block has a different response system again. A general finite-block statement would require either a uniform reservoir construction or a structural rank/positive-cone theorem for these response matrices; neither is established here.

## 5. Stress test, prior art, and research consequence

The countermodel uses one arithmetic source for all four horizons. Its squarefree zero set and unit amplitudes are physical, and every Euler relation through the largest requested cutoff holds globally. The only nonphysical freedom is explicit: unconstrained core-prime coordinates above `8 theta N` are selected once for the complete four-horizon block.

The exact finite part was checked independently before promotion. The floor cells in (7) are fixed-ratio disjoint prime intervals; substituting the displayed small Mertens values gives (8); the high matrix has determinant `112`; and (10) gives a strictly positive repair vector. The only asymptotic inputs are PNT for reservoir capacity and the already-anchored Davenport estimate making the physical baselines negligible compared with `N/log N`. No probabilistic independence, prime-gap hypothesis, or RH-strength estimate is used.

A prior-art audit again found Marco Aymone, *A note on multiplicative functions resembling the Möbius function* (J. Number Theory **212** (2020), 113--121; arXiv `1908.11014`), and Qingyang Liu, *Multiplicative functions resembling the Möbius function* (arXiv `2205.00972`), as neighboring work on globally multiplicative squarefree-supported functions with prescribed prime signs and summatory cancellation. Those papers do not provide the finite-horizon switched response-vector construction above, and no theorem from them is used. PNT and Davenport are already anchored in line-local `SOURCES.md`, so no source update is required.

The live boundary after FD-219 is therefore resolved in the negative: **the first scheduler wraparound does not create coercivity before literal Euler-prefix coverage.** The useful remaining question is no longer whether one wrap is special, but whether the finite-block repair matrices admit a general positive-cone mechanism for arbitrarily many fixed horizons, or whether some later block loses that property before prime-prefix coverage becomes exhaustive.

That distinction matters. Proving a uniform finite-block reservoir theorem would show that every fixed amount of same-source persistence remains a representation-level relaxation; finding the first block whose response cone fails would instead isolate a genuinely new observation-geometric obstruction.