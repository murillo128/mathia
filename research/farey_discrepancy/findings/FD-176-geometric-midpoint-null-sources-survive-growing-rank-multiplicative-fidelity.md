# FD-176 — Geometric midpoint null sources survive growing-rank multiplicative fidelity

- **Date:** 2026-09-17
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** restricted temporal acquisition / growing-rank compatibility / geometric null construction / multiplicativity boundary
- **Depends on:** FD-117, FD-170, FD-172, FD-173, FD-174, FD-175
- **Classification:** `EXACT-DERIVED + PERMANENT-SOURCE + GEOMETRIC-NULL + GROWING-RANK-FIDELITY + NONMULTIPLICATIVE`

## Claim

`FD-175` shows that any fixed multiplicative-rank cutoff can be kept exactly Möbius while a sparse squarefree deletion source remains invisible on an entire geometric midpoint ladder. The fixed-rank restriction can be strengthened to a genuinely growing rank.

Fix an integer base `B>=3` and put

\[
D_B:=\lfloor B/2\rfloor,
\qquad
\lambda_B:=1+D_B,
\qquad
\alpha_B:=\log_B\lambda_B,
\qquad
\beta_B:=1-\alpha_B>0.
\tag{1}
\]

For every

\[
0<\rho<\beta_B
\tag{2}
\]

and every finite cutoff `X`, there exists one permanent arithmetic source `a\not\equiv\mu` such that

\[
a(n)\in\{0,\mu(n)\}\qquad(n\ge1),
\tag{3}
\]

\[
a(n)=\mu(n)\qquad(n\le X),
\tag{4}
\]

and, for every sufficiently large squarefree `n`,

\[
\omega(n)\le \rho\frac{\log n}{\log\log n}
\quad\Longrightarrow\quad
a(n)=\mu(n).
\tag{5}
\]

The construction can be started far enough out that (5), together with (4), covers all smaller integers as well. In particular every prime coefficient is untouched and, throughout the entire growing low-rank region (5),

\[
a(n)=\mu(n)=\prod_{p\mid n}a(p).
\tag{6}
\]

Nevertheless

\[
\boxed{
P_a(B^m)=P_\mu(B^m)
\qquad\text{for every }m\ge1.
}
\tag{7}
\]

Moreover the deletion set `S={n:a(n)=0,\mu(n)\ne0}` satisfies

\[
S(x)=O_{B,\rho,X}(x^{\alpha_B}),
\tag{8}
\]

so it has natural density zero.

Thus exact multiplicative compatibility on a rank window growing like a positive constant times `log n/log log n` still does not recover geometric-midpoint target rigidity. The full cross-coordinate multiplicative law used in `FD-172`--`FD-174` remains substantially stronger.

## 1. The old-support repair budget grows with exponent `alpha_B`

Retain the notation of `FD-175`. If `S` is the set of deleted squarefree coefficients, midpoint matching at height `H` is equivalent to

\[
C_H(S)
=
\sum_{\substack{d\in S\\d\le H}}
-\mu(d)W_H(d)
=0,
\tag{9}
\]

where

\[
W_H(d)=\#\{r\le H/d:r\text{ odd}\}.
\tag{10}
\]

For consecutive geometric horizons `h` and `H=Bh`, `FD-175` proves

\[
|W_{Bh}(d)-B W_h(d)|\le D_B
\qquad(d\le h).
\tag{11}
\]

Hence, if the old deletion set is balanced at `h` and contains `N` points, its residual at `H` has magnitude at most

\[
|R_H|\le D_B N.
\tag{12}
\]

Every fresh deletion in `(H/2,H]` has `W_H(d)=1`, so `|R_H|` fresh squarefree integers of the appropriate Möbius sign repair the next sample exactly. If `N_m` denotes the number of deletions chosen through `B^m`, this gives the same recurrence as `FD-175`,

\[
N_m\le\lambda_B N_{m-1},
\qquad
\lambda_B=1+D_B,
\tag{13}
\]

and therefore

\[
N_m\ll \lambda_B^m=(B^m)^{\alpha_B}.
\tag{14}
\]

The only new issue is whether those correction tokens can be forced to have multiplicative rank well above a growing threshold.

## 2. Every fresh half-shell contains enough prescribed-sign high-rank squarefrees

Choose an intermediate constant

\[
\rho<\rho'<\beta_B=1-\alpha_B.
\tag{15}
\]

At a large active horizon `H=B^m`, choose an integer

\[
r=r(H)=\left\lfloor
\rho'\frac{\log H}{\log\log H}
\right\rfloor
\tag{16}
\]

with its parity adjusted by at most one according to the Möbius sign needed. Let

\[
P_r:=p_1p_2\cdots p_r
\tag{17}
\]

be the `r`-th primorial. The prime number theorem, already anchored in `SOURCES.md`, gives

\[
\log P_r=(1+o(1))r\log r
=(\rho'+o(1))\log H,
\tag{18}
\]

hence

\[
P_r=H^{\rho'+o(1)}.
\tag{19}
\]

For every prime

\[
\frac{H}{2P_r}<q\le\frac{H}{P_r},
\tag{20}
\]

the integer

\[
n=P_rq
\tag{21}
\]

lies in `(H/2,H]`. For large `H` the primes in (20) satisfy `q>p_r`, so `n` is squarefree and

\[
\omega(n)=r+1
=(\rho'+o(1))\frac{\log H}{\log\log H}.
\tag{22}
\]

The PNT in the fixed-ratio interval (20) supplies

\[
H^{1-\rho'+o(1)}
\tag{23}
\]

such integers. Replacing `r` by an adjacent integer reverses the parity of `r+1` and therefore supplies the opposite Möbius sign with the same exponent. Thus both correction signs occur in the fresh shell with cardinality `H^{1-rho'+o(1)}`.

Because `rho'<1-alpha_B`,

\[
1-\rho'>\alpha_B.
\tag{24}
\]

Consequently the reservoir (23) eventually dominates the entire required correction budget `O(H^{alpha_B})` from (12)--(14).

Finally, since every selected `n` lies between `H/2` and `H`, (22) and `rho'>rho` imply, after choosing the starting horizon sufficiently large,

\[
\omega(n)>
\rho\frac{\log n}{\log\log n}
\tag{25}
\]

for every deletion made by the construction.

## 3. Seed once, then repair forever

Choose the first active horizon so large that its top half lies beyond `X` and that the estimates above hold. In that first fresh half-shell choose one admissible squarefree integer of each Möbius sign. Their unit contributions to (9) cancel, so the source is already nontrivial while the first active midpoint remains exact. All earlier ladder samples are unchanged because the two deletions lie beyond their horizons.

Inductively, suppose the geometric sample at `h=B^(m-1)` is exact. Compute the old-support residual at `H=B^m`; by (12) it has size at most `D_B N_(m-1)`. Select exactly that many unused integers from the prescribed-sign high-rank reservoir of Section 2. They lie in the fresh top half-shell, each contributes one unit with the required sign, and restore `C_H(S)=0`. The reservoir dominates the required count by (24), so the induction continues indefinitely.

The recurrence (13) proves (8). Equation (25) proves that no deletion enters the growing low-rank region (5), while starting beyond `X` proves (4). This establishes the claim.

## 4. What the exponent means, and what it does not mean

The new threshold is

\[
\boxed{
\rho<\beta_B
=1-\log_B\bigl(1+\lfloor B/2\rfloor\bigr).
}
\tag{26}
\]

For example, `beta_3≈0.3691`, `beta_4≈0.2075`, and `beta_5≈0.3174`. Since the maximal possible order of `omega(n)` is `(1+o(1))log n/log log n`, this preserves exact Möbius behavior on a positive fraction of the full multiplicative-rank range, not merely on every fixed rank.

The constant in (26) is **not claimed to be sharp**. It is the threshold delivered by the particular one-shell repair mechanism of `FD-175`: the old-support population grows like `H^alpha_B`, while a rank-`rho'` primorial reservoir has size `H^(1-rho'+o(1))`. A more efficient balancing construction could raise the admissible rank.

The case `B=2` is also genuinely unresolved by this argument. There `lambda_2=B`, so `alpha_2=1` and `beta_2=0`; the crude deletion-count recurrence consumes the full linear exponent and leaves no room for a positive growing-rank primorial reservoir. `FD-175` still preserves every fixed rank in the dyadic case, but this pass does not extend that to `rho log n/log log n`.

## Representation audit

No observable, norm, or coordinate system is changed relative to `FD-170` and `FD-175`. The construction stays inside the same exact midpoint transform and the same squarefree sign-compatible alphabet `a(n) in {0,mu(n)}`. The extra fidelity is imposed directly in the source coordinates: all coefficients through an arbitrary finite prefix, all primes, and now an unbounded multiplicative-rank window are exactly physical.

The generic mechanism is a dilation-balanced linear sensor with a fresh-shell correction budget growing like `H^alpha_B`. The Farey/Möbius-specific ingredients are the exact odd-multiple weight `W_H`, the bounded dilation defect (11), and the availability of squarefree prescribed-sign correction tokens. The latter is obtained here by an explicit primorial-times-prime construction, not by changing the representation.

This remains an identifiability counterexample in a relaxed, nonmultiplicative source class. It does not derive new Möbius cancellation and does not weaken the full multiplicativity hypothesis of `FD-172` into a sufficient condition. Instead it rules out a substantial candidate weakening: exact product compatibility through any rank `rho log n/log log n` with `rho<beta_B` is still insufficient for geometric midpoint rigidity when `B>=3`.

## Prior-art audit

Targeted searches for Farey-midpoint geometric sampling, Möbius rigidity under lacunary observations, and truncated/growing-rank multiplicativity did not locate a direct analogue of this null construction. The ingredients used to populate the fresh shell are classical: primorial asymptotics and the number of primes in a fixed-ratio interval are immediate consequences of the prime number theorem. That theorem is already anchored in `SOURCES.md` (Newman, *Simple Analytic Proof of the Prime Number Theorem*), so no new durable source dependency is introduced.

Nearby literature on primes or squarefrees in short intervals is stronger than needed and is not load-bearing here. The line-specific step is the coupling of the `FD-175` geometric repair exponent with a prescribed-sign high-rank squarefree reservoir inside the exact Farey midpoint sensor.

## Consequence for the research frontier

`FD-175` left open whether letting the protected multiplicative rank grow with the coefficient size could block recursive geometric repair. For every integer base `B>=3`, the answer is negative at least throughout the explicit range (26). The next meaningful boundary is therefore either a faster-growing rank approaching the extremal `omega(n)` scale, a compatibility law that couples low- and high-rank products rather than checking ranks independently, or the dyadic case where this repair-count argument loses its exponent gap.

No clue status changes follow from this result.