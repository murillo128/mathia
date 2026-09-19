# FD-221 — Every fixed switched block remains blind until literal Euler prefix coverage

- **Date:** 2026-09-19
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** arbitrary fixed same-source horizon block / switched root-filter countermodel / divisor-reservoir null cycle / exact triangular repair / sharp finite-block representation boundary
- **Depends on:** FD-220, FD-005
- **Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + ARBITRARY-FIXED-BLOCK + DIVISOR-RESERVOIR-NULL-CYCLE + TRIANGULAR-REPAIR + SHARP-LITERAL-COVERAGE-THRESHOLD`

## Claim

`FD-218--FD-220` showed blindness for two, three, and four coupled dyadic horizons, but left open whether a later finite block might finally lose positive-cone repair because the switched schedule keeps wrapping between depths `0` and `3`.

It does not. For the present scheduler, **every fixed finite block remains blind until the latest Euler window literally reaches the original prefix**.

Let

\[
q_t=
\begin{cases}
0,&t\equiv0\pmod3,\\
3,&t\equiv1,2\pmod3,
\end{cases}
\qquad
q(n)=q_{\lfloor\log_2 n\rfloor},
\]

and

\[
\mathcal C_q^X(n)=(T-I)^{q+1}X(n),
\qquad (TF)(n)=F(2n).
\]

Fix an integer `J>=1` and a constant

\[
0<\theta<2^{-(J-1)}.
\tag{1}
\]

Then for every sufficiently large integer `N` there is one deterministic sequence

\[
\xi_n^{(N)}\in\{-1,0,1\},
\qquad
(\xi_n^{(N)})^2=\mu(n)^2,
\qquad
\xi_1^{(N)}=1,
\]

which obeys globally every selected Euler relation required anywhere in the block,

\[
\boxed{
\xi_{pn}^{(N)}=-\xi_n^{(N)}
\quad
\left(p\le \theta 2^{J-1}N,\ p\nmid n\right),
}
\tag{2}
\]

and hence in particular all relations `p<=theta H` at the horizons

\[
H=N,2N,\ldots,2^{J-1}N.
\]

Writing

\[
X_N(x)=\sum_{n\le x}\xi_n^{(N)},
\]

there is a constant `C_J<infinity` such that simultaneously

\[
\boxed{
\left|
\mathcal C_{q(2^jN)}^{X_N}(2^jN)
\right|
\le C_J
\qquad(0\le j<J),
}
\tag{3}
\]

while

\[
\boxed{
X_N(N)\asymp_{J,\theta}\frac{N}{\log N}.
}
\tag{4}
\]

The threshold is sharp for prefix identification in this source class. If

\[
\theta\ge2^{-(J-1)},
\tag{5}
\]

then the Euler requirement at the last horizon already includes every prime `p<=N`; squarefree support and `xi_1=1` therefore force

\[
\boxed{\xi_n=\mu(n)\qquad(n\le N).}
\tag{6}
\]

Thus no **fixed** number of same-source switched observations closes the relaxed source before literal prime-prefix coverage. What remains open is genuinely growing or infinite-horizon coherence, where `J` itself increases with scale and the finite construction below is no longer uniform.

As in FD-218--FD-220, (6) is an information statement, not an RH estimate. Recovering the physical Möbius prefix does not by itself bound `M(N)`.

## 1. Exact selected-Euler source and its prime response

Put

\[
Y=\theta 2^{J-1}N<N,
\qquad
P_N=\{p\text{ prime}:p\le Y\},
\qquad
Q_N=\prod_{p\in P_N}p.
\tag{7}
\]

Every squarefree integer has a unique factorization `n=am`, with `a|Q_N` and `(m,Q_N)=1`. Choose signs `eta_m in {-1,+1}` on squarefree cores coprime to `Q_N`, define

\[
\xi_{am}=\mu(a)\eta_m,
\tag{8}
\]

and put `xi_n=0` on nonsquarefree integers. Then (2) holds identically for every constrained prime.

Start from the physical choice `eta_m=mu(m)`. We will alter only selected unconstrained core primes `r>Y`, changing `eta_r` from `-1` to `+1` and leaving every other core coordinate physical. For such a flip,

\[
\Delta X_N(x)
=
2\sum_{\substack{a\mid Q_N\\a\le x/r}}\mu(a).
\tag{9}
\]

The complete block samples only finitely many dyadic points. Let

\[
s=\lfloor\log_2N\rfloor\pmod3,
\qquad
q_j=q_{s+j},
\qquad
e_j=j+q_j+1
\quad(0\le j<J),
\tag{10}
\]

and set

\[
E=\max_{0\le j<J}e_j,
\qquad
D=2^E.
\tag{11}
\]

Every observation in (3) is a linear combination of `X_N(2^kN)` with `0<=k<=E`. Since `J` is fixed, so are `E` and `D`; for sufficiently large `N`,

\[
Y>D.
\tag{12}
\]

Therefore, whenever a selected prime satisfies `floor(2^kN/r)<=D`, every prime factor of every squarefree integer up to that floor lies in `Q_N`. Equation (9) then becomes the exact finite response

\[
\boxed{
\Delta X_N(2^kN)
=2M\!\left(\left\lfloor\frac{2^kN}{r}\right\rfloor\right).
}
\tag{13}
\]

This is the same arithmetic response mechanism used in the previous finite blocks, but we now arrange it structurally rather than solving a new reservoir matrix for each `J`.

## 2. Floor-stable divisor reservoirs

For every integer `1<=d<=D`, choose a constant `a_d` with

\[
d-\frac12<a_d<d
\tag{14}
\]

such that for every `0<=k<=E` and every `c in (a_d,d)`,

\[
\left\lfloor\frac{2^k}{c}\right\rfloor
=
\left\lfloor\frac{2^k}{d}\right\rfloor.
\tag{15}
\]

Such an `a_d` exists because only finitely many floor functions are involved and each is constant on a sufficiently small left-neighborhood of `d`. For `d=1`, choose it additionally so that

\[
a_1>\theta2^{J-1}=Y/N,
\tag{16}
\]

which is possible by (1).

Define the pairwise disjoint fixed-ratio prime reservoirs

\[
I_d=(a_dN,dN),
\qquad 1\le d\le D.
\tag{17}
\]

Every prime in every `I_d` exceeds `Y`: this is explicit for `I_1` by (16), while `I_d` with `d>=2` lies above `N>Y`. The prime number theorem gives

\[
|I_d\cap\mathbb P|
\sim(d-a_d)\frac{N}{\log N},
\tag{18}
\]

so each reservoir contains `Theta_J(N/log N)` primes.

For `r in I_d`, (13) and (15) give the exact response table

\[
\boxed{
\Delta X_N(2^kN)
=2M\!\left(\left\lfloor\frac{2^k}{d}\right\rfloor\right)
\qquad(0\le k\le E).
}
\tag{19}
\]

No asymptotic approximation enters this table.

## 3. A strictly positive null cycle for every finite block

Choose a small fixed constant `kappa_{J,theta}>0` below the capacity constant of every reservoir in (18), with a fixed margin, and put

\[
A=\left\lfloor
\kappa_{J,\theta}\frac{N}{\log N}
\right\rfloor.
\tag{20}
\]

First flip exactly `A` primes in **every** reservoir `I_d`, `1<=d<=D`. At a sampled point `2^kN`, the total perturbation is, by (19),

\[
2A\sum_{d=1}^{D}
M\!\left(\left\lfloor\frac{2^k}{d}\right\rfloor\right).
\tag{21}
\]

For `d>2^k` the summand is `M(0)=0`. The exact divisor identity already isolated in FD-005 gives

\[
\sum_{d=1}^{2^k}
M\!\left(\left\lfloor\frac{2^k}{d}\right\rfloor\right)=1.
\tag{22}
\]

Hence

\[
\boxed{
\Delta X_N(2^kN)=2A
\qquad(0\le k\le E).
}
\tag{23}
\]

The perturbation is therefore **constant on every dyadic sample used by the entire block**. Since every scheduled observable has positive difference order `q_j+1>=1`,

\[
(T-I)^{q_j+1}(2A)=0.
\]

Thus the equal-count vector across the `D` divisor reservoirs is a strictly positive null direction for *all* `J` observations at once. This is the structural positive-cone mechanism missing from FD-220: later wraps of the `(0,3,3)` scheduler cannot remove this null direction at any fixed finite length.

## 4. Triangular pivots repair the physical Möbius baselines

The positive null cycle leaves the scheduled observations equal to their physical Möbius baselines

\[
b_j=
\mathcal C_{q_j}^{M}(2^jN),
\qquad 0\le j<J.
\tag{24}
\]

Each `b_j` is a fixed finite linear combination of `M(cN)` with `c` depending only on the fixed block. The Davenport estimate already anchored in `SOURCES.md` gives

\[
\boxed{b_j=o(N/\log N)}
\qquad(0\le j<J).
\tag{25}
\]

It remains to make small `o(N/log N)` adjustments to the reservoir counts without losing positivity. For row `j`, use the pivot reservoir

\[
d_j=2^{e_j}.
\tag{26}
\]

The endpoint exponents `e_j` are pairwise distinct. Indeed, if `i<j` and `e_i=e_j`, then

\[
j-i=q_i-q_j.
\tag{27}
\]

The right side belongs to `{-3,0,3}`. Since `j-i>0`, equality would force `j-i=3` and `q_i-q_j=3`; but the scheduler has period three, so `q_i=q_j`, a contradiction.

Let `V` be the `J x J` response matrix whose `j`-th column is the observation vector produced by one additional flip in `I_{d_j}`. Order rows and columns by increasing endpoint exponent `e_j`. If `e_i<e_j`, then every dyadic sample entering row `i` has exponent `k<=e_i`, so

\[
\left\lfloor\frac{2^k}{d_j}\right\rfloor=0
\]

and therefore `V_{ij}=0`. On the diagonal, all lower samples vanish while the top sample has

\[
\left\lfloor\frac{2^{e_j}}{2^{e_j}}\right\rfloor=1,
\qquad M(1)=1.
\]

The coefficient of the top sample in `(T-I)^{q_j+1}` is `+1`, hence

\[
\boxed{V_{jj}=2.}
\tag{28}
\]

Consequently `V` is triangular with

\[
\boxed{\det V=2^J\ne0.}
\tag{29}
\]

Let

\[
\delta=-V^{-1}b.
\tag{30}
\]

By (25) and fixed `J`, every coordinate of `delta` is `o(N/log N)=o(A)`. Change the count in pivot reservoir `I_{d_j}` from `A` to

\[
A+s_j,
\qquad
s_j=\operatorname{round}(\delta_j).
\tag{31}
\]

For sufficiently large `N`, all these counts remain positive and remain strictly below their PNT capacities because the initial `kappa_{J,theta}` was chosen with margin. The remaining observation vector is

\[
b+Vs=V(s-\delta),
\tag{32}
\]

so nearest-integer rounding gives

\[
\boxed{\|b+Vs\|_\infty=O_J(1).}
\tag{33}
\]

This proves (3). The finite-index lattice issue seen explicitly in FD-219--FD-220 has become the harmless fixed rounding constant in (33).

## 5. The prefix defect survives untouched

Only `I_1` lies below `N`; every reservoir `I_d` with `d>=2` lies above `N`. All pivots also satisfy

\[
d_j=2^{e_j}\ge2,
\]

so the triangular repairs never alter the number of flipped primes below `N`.

For `r in I_1`, floor stability at `k=0` gives `floor(N/r)=1`, hence each of the `A` low flips changes the prefix sum by exactly `2M(1)=2`. Therefore

\[
X_N(N)=M(N)+2A.
\tag{34}
\]

Davenport gives `M(N)=o(N/log N)`, and (20) yields

\[
\boxed{
X_N(N)=
(2\kappa_{J,\theta}+o(1))\frac{N}{\log N}.
}
\tag{35}
\]

This proves (4). The same source therefore has a macroscopic, strongly super-square-root prefix while every one of the `J` coupled switched observations stays bounded.

## 6. Literal Euler coverage is the sharp finite-block threshold

Suppose now that (5) holds. At the latest horizon `2^{J-1}N`, the requested Euler window contains every prime

\[
p\le\theta2^{J-1}N\ge N.
\]

For any squarefree `n<=N`, every prime factor of `n` is therefore constrained. Starting from `xi_1=1`, repeated application of the exact Euler law forces

\[
\xi_n=(-1)^{\omega(n)}=\mu(n).
\]

Both sequences vanish on nonsquarefree integers, proving (6).

Hence the exact prefix-rigidity threshold for a fixed `J`-horizon block is

\[
\boxed{\theta_J=2^{-(J-1)}.}
\tag{36}
\]

Below it, the divisor-reservoir null cycle plus triangular pivots produce one blind same-source countermodel for the complete block. At or above it, the final Euler cutoff literally determines the original Möbius prefix. No intermediate finite-block coercivity appears.

## 7. Stress test, prior art, and research consequence

The construction keeps the strongest physical features used in FD-215--FD-220: the exact squarefree zero set, unit amplitudes on squarefrees, one shared arithmetic source across the entire block, and every selected Euler relation through the largest requested cutoff. The nonphysical freedom is explicit and localized to unconstrained core primes above `Y`.

The exact finite mechanism has three independently checkable parts. First, the floor-stable intervals make every prime in a reservoir share the response (19). Second, the Mertens divisor identity (22) makes equal occupancy of all divisor reservoirs a strictly positive null cycle, so no scheduler wrap can spoil it. Third, the endpoint exponents of the `(0,3,3)` schedule are distinct, giving the triangular pivot matrix with determinant `2^J`. The only asymptotic inputs are PNT for reservoir capacity and Davenport for the `o(N/log N)` physical baselines. No probabilistic independence, prime-gap hypothesis, or RH-strength cancellation is used.

A prior-art audit found the same neighboring literature as FD-215--FD-220 on Möbius-like multiplicative functions and classical floor-quotient/Mertens identities, but no result matching this finite-horizon divisor-reservoir null-cycle construction. No new external theorem is load-bearing here, so `SOURCES.md` requires no update.

This closes the specific frontier left by FD-220: **testing longer fixed blocks one by one cannot reveal a first positivity/rank failure**. Every fixed block has a structural positive null direction and an exact full-rank repair system. The constants are not uniform in `J`: `D=2^E`, the floor-cell widths, `kappa_{J,theta}`, and the required lower bound on `N` can deteriorate rapidly as `J` grows. The proof therefore does **not** produce one fixed source valid for infinitely many horizons, nor does it handle `J=J(N)->infinity`.

The next live boundary is consequently genuine growing-horizon or infinite-time coherence. Any route that hopes to recover rigidity before literal Euler coverage must exploit a condition whose complexity grows with scale, or a cross-horizon structure not reducible to finitely many switched root-filter observations.