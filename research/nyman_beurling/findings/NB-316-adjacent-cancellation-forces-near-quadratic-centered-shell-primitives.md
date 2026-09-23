# NB-316 — Adjacent cancellation forces near-quadratic centered shell primitives

- **Date:** 2026-09-24
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-304, NB-314, NB-315
- **Classification:** `EXACT-DERIVED + SOURCE-SIDE + METHOD-BOUNDARY + SHARPNESS-CONTROL + CENTERED-SHELL-PRIMITIVE + ADJACENT-WITNESS + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_N:=\operatorname{span}\{g_2,\ldots,g_N\},
\]

and, for `u in U_N`, let its reciprocal profile, reciprocal mean, centered profile, and centered primitive be

\[
F_u(t):=u(1/t),
\qquad
\mu_N(u):=\text{the zero-frequency reciprocal-shell mean},
\]

\[
\widetilde F_u(t):=F_u(t)-\mu_N(u),
\qquad
G_u(T):=\int_0^T \widetilde F_u(s)\,ds.
\]

Define the finite-section primitive amplification

\[
\Pi_N
:=
\sup_{0\ne u\in U_N}
\frac{\|G_u\|_\infty}{\|u\|_2}.
\tag{1}
\]

`NB-315` proves the uniform upper bound

\[
\Pi_N\le C_{\rm prim}N^{5/2}.
\tag{2}
\]

The exponent cannot be pushed below `2` by any uniform estimate of this same primitive quantity. For every `N>=3`, the scaled adjacent cancellation

\[
u_N:=g_N-\frac{N-1}{N}g_{N-1}
\tag{3}
\]

satisfies the exact primitive identity

\[
\boxed{
\|G_{u_N}\|_\infty
=
\frac{\lfloor N^2/4\rfloor}{2N},
}
\tag{4}
\]

while `NB-304` gives

\[
\|u_N\|_2^2
\le
\frac{2H_{N-2}+1+\pi^2/18}{N^2}.
\tag{5}
\]

Consequently

\[
\boxed{
\Pi_N
\ge
\frac{\lfloor N^2/4\rfloor}
{2\sqrt{2H_{N-2}+1+\pi^2/18}}
\asymp_{\rm lower}
\frac{N^2}{\sqrt{\log N}}.
}
\tag{6}
\]

In particular, for every fixed `p<2`,

\[
\frac{\Pi_N}{N^p}\to\infty.
\tag{7}
\]

Thus the `N^(5/2)` primitive estimate in `NB-315` still has a genuine half-power window for improvement, but the natural hope of replacing it by `N^(3/2)`, `N^(1+epsilon)`, or any other fixed power below `N^2` is impossible. The obstruction already occurs in a two-generator adjacent cancellation.

This is a boundary for the **uniform centered-primitive route** used by `NB-315`, not a lower bound for the actual mixing error `||sqrt(m)T_(N,m)-R_N||`, not a lower bound for `beta_(N+1)(m)`, and not a target-occupation statement.

## 1. The adjacent witness has reciprocal mean `1/(2N)`

For the canonical discrete Nyman generator,

\[
F_{g_j}(t)
=
\left\{\frac tj\right\}
-\frac1j\{t\},
\]

and its reciprocal-shell mean is, as recorded in `NB-314`,

\[
\mu_N(g_j)=\frac{j-1}{2j}.
\tag{8}
\]

Therefore the witness (3) has

\[
\begin{aligned}
\mu_N(u_N)
&=
\frac{N-1}{2N}
-
\frac{N-1}{N}\frac{N-2}{2(N-1)}\\
&=
\boxed{\frac1{2N}}.
\end{aligned}
\tag{9}
\]

`NB-304` gives its exact reciprocal-shell value. On the shell indexed by

\[
k=aN+r,
\qquad
0\le a\le N-2,
\qquad
0\le r<N,
\]

inside the first period `L_N=N(N-1)`, one has

\[
 u_{N,aN+r}
 =
 \begin{cases}
 -a/N,&0\le r<N-1-a,\\[2mm]
 (N-1-a)/N,&N-1-a\le r<N.
 \end{cases}
\tag{10}
\]

Put

\[
x_{N,k}:=u_{N,k}-\frac1{2N}.
\tag{11}
\]

Because `F_(u_N)` is constant on each unit reciprocal cell, the centered primitive at integer arguments is simply

\[
G_{u_N}(K)=\sum_{k=0}^{K-1}x_{N,k}.
\tag{12}
\]

## 2. The centered primitive can be computed exactly block by block

The total centered increment across block `a` is obtained directly from (10). The uncentered block sum is

\[
\sum_{r=0}^{N-1}u_{N,aN+r}
=
\frac{N-1-a}{N},
\]

so after subtracting the mean on all `N` cells,

\[
\boxed{
D_a
:=
\sum_{r=0}^{N-1}x_{N,aN+r}
=
\frac{N-2-2a}{2N}.
}
\tag{13}
\]

Hence the primitive at the start of block `a` is

\[
P_a
:=G_{u_N}(aN)
=
\sum_{b=0}^{a-1}D_b
=
\boxed{
\frac{a(N-1-a)}{2N}}.
\tag{14}
\]

Inside the first part of block `a`, equation (10) gives the constant centered increment

\[
-\frac{2a+1}{2N}<0.
\]

Thus the primitive decreases monotonically until the jump location `r=N-1-a`. At that point its value is

\[
\begin{aligned}
Q_a
&=
P_a
-
(N-1-a)\frac{2a+1}{2N}\\
&=
\boxed{
-\frac{(a+1)(N-1-a)}{2N}}.
\end{aligned}
\tag{15}
\]

On the remaining `a+1` cells, the centered increment is

\[
\frac{2N-2a-3}{2N}>0,
\]

so the primitive increases monotonically from `Q_a` to `P_(a+1)`.

The extrema over each block therefore occur at `P_a` or `Q_a`. Since

\[
\max_{0\le a\le N-2}
(a+1)(N-1-a)
=
\max_{1\le b\le N-1}b(N-b)
=
\left\lfloor\frac{N^2}{4}\right\rfloor,
\tag{16}
\]

while `a(N-1-a)` has a no larger maximum, the largest absolute integer-time primitive in one period is

\[
\frac{\lfloor N^2/4\rfloor}{2N}.
\tag{17}
\]

Equation (13) sums to zero over `a=0,...,N-2`, so the centered primitive returns to zero after the period `N(N-1)`. It therefore repeats from period to period. Between successive integers the centered reciprocal profile is constant, so `G_(u_N)` is linear and creates no larger interior extremum. This proves the exact identity (4).

## 3. Normalizing by the Nyman norm forces a near-quadratic primitive scale

The norm estimate from `NB-304` is

\[
\|u_N\|_2^2
\le
\frac{B_N}{N^2},
\qquad
B_N:=2H_{N-2}+1+\frac{\pi^2}{18}.
\tag{18}
\]

Combining (4) and (18),

\[
\frac{\|G_{u_N}\|_\infty}{\|u_N\|_2}
\ge
\frac{\lfloor N^2/4\rfloor}{2\sqrt{B_N}},
\tag{19}
\]

which proves (6). Since `B_N=2 log N+O(1)`,

\[
\Pi_N
\ge
\left(\frac1{8\sqrt2}+o(1)\right)
\frac{N^2}{\sqrt{\log N}}.
\tag{20}
\]

This lower bound uses the same explicit two-generator family that made the universal support-localization scale power-sharp in `NB-304`, but the mechanism is different. There the important fact was that order-one shell spikes survive through reciprocal depth `N^2`; here their centered cumulative drift forms a triangular primitive of height order `N`, while the Hilbert norm is only order `sqrt(log N)/N`.

The separation from `NB-305` is also important. `NB-305` shows that the same witness is almost self-orthogonal under normalized dilation. A large centered primitive therefore does **not** imply a large projected-dilation singular value or even a large self-correlation. It certifies only that taking `||G_u||_infinity` before the weighted shell pairing can be expensive.

## 4. Consequence for the `NB-315` proof architecture

The moving rank-one estimate in `NB-315` proceeds in two logically separate steps. First it bounds every centered shell primitive by `Pi_N ||u||`. Then integration by parts and weighted Cauchy--Schwarz convert that scalar supremum into

\[
\left|
\left\langle
(\sqrt m\,T_{N,m}-R_N)v,u
\right\rangle
\right|
\lesssim
\frac{\Pi_N}{m}
\|u\|_2\|v\|_2.
\tag{21}
\]

The new lower bound says that the first step can never have a polynomial section loss smaller than `N^2`: no uniform estimate

\[
\|G_u\|_\infty
\le C N^p\|u\|_2
\qquad(u\in U_N)
\tag{22}
\]

can hold with any fixed `p<2`.

This does **not** say that the operator error in (21) is itself at least `N^2/(m sqrt(log N))`. Inequality (21) may be very lossy because the weighted pairing can cancel even when one primitive reaches a large supremum. Therefore the result rules out only a natural proof branch: improving `NB-315` all the way into the merely-superlinear regime cannot come from proving a subquadratic universal bound for the same centered primitive norm.

The remaining options are now more sharply separated. One can still try to close the genuine primitive gap

\[
\frac{N^2}{\sqrt{\log N}}
\lesssim
\Pi_N
\lesssim
N^{5/2},
\tag{23}
\]

but pushing projected-dilation mixing substantially further may instead require cancellation in the weighted shell pairing itself, frequency-sensitive primitive norms, or direct control of the bilinear error rather than its `L^infinity` primitive envelope. None of those possibilities is excluded here.

## 5. Adversarial checks and prior-art audit

The mean subtraction is exact: `mu_N(u_N)=1/(2N)` follows from the reciprocal means of the two generators, so (13) is the increment of the same centered primitive used in `NB-315`, not a different centering convention. The first-period formula includes the block `a=0`; the centered period sum is zero, so repeating periods introduces no secular drift. Continuous times cannot increase the supremum because the primitive is linear on each unit cell. The norm comparison uses only the proved upper bound from `NB-304`; an upper bound on the witness norm is in the correct direction for the lower bound (19).

The claim is also deliberately restricted to the primitive method. It does not contradict `NB-305`'s self-dilation decorrelation, `NB-313`'s positive external correlation channel, or `NB-315`'s relative rank-one mixing at superquadratic scale. A large primitive may be invisible after the particular weighted pairing defining the projected dilation.

A fresh literature search compared the result against the nearby fractional-part and Nyman--Beurling literature: Balazard--Martin, *Sur l'autocorrélation multiplicative de la fonction partie fractionnaire et une fonction définie par J. R. Wilton* (arXiv:1305.4395), which studies multiplicative autocorrelation and Wilton/continued-fraction structure; Maier--Rassias, *Explicit estimates of sums related to the Nyman-Beurling criterion for the Riemann Hypothesis* (arXiv:1806.05070), which treats different Möbius/cotangent sums; Ehm, *On certain Gram matrices and their associated series* (arXiv:2405.06349), which derives Nyman--Beurling Gram formulae and reciprocity structures; and Carvill, *Beurling Nyman Geometry and Gram Matrix Structure, Ladder Density and Polynomial Decay via Mellin Smoothing* (arXiv:2510.18132), which studies Gram decay on multiplicative ladders. The material located in this audit did not expose the finite-section centered reciprocal-primitive norm `Pi_N`, the exact formula (4), or the resulting power barrier (7). This is recorded only as a prior-art boundary from the sources reviewed, not as a claim of bibliographic novelty.

No external theorem is load-bearing for the proof above, so this finding does not add a durable source dependency to `SOURCES.md`.

## Classification and next discriminator

This is a rigorous negative/method-boundary finding. It converts the qualitative caveat at the end of `NB-315` into a quantitative obstruction: the uniform primitive route has at most a half-power polynomial improvement left before it reaches a near-quadratic lower wall.

The next decisive question is therefore not whether the same primitive can be made `N^(3/2)`; it cannot. The useful alternatives are to determine the true scale of `Pi_N` inside the interval (23), or to bypass `Pi_N` and estimate the weighted bilinear mixing error directly. A direct estimate that exploits cancellation invisible to `||G_u||_infinity` could still move the rank-one transition into `N << m <= O(N^2)` and is not constrained by this finding.
