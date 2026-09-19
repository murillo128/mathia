# FD-210 — Fixed signed root filters have a supercritical spectral blind annulus at critical random cost

- **Date:** 2026-09-19
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** collective signed root filter / spectral blind-mode obstruction / bounded-alphabet source countermodel / random-multiplicative benchmark
- **Depends on:** FD-197, FD-206, FD-207, FD-209
- **Classification:** `EXACT-DERIVED + FIXED-POLYNOMIAL-ROOT-FILTER + SUPERCRITICAL-SPECTRAL-BLIND-ANNULUS + BOUNDED-ALPHABET-COUNTERMODEL + CRITICAL-RANDOM-COST + ROUTE-RESTRICTION`

## Claim

`FD-209` leaves a genuinely collective signed relation across different root edges as one live escape from the common-depth binomial family. Fixed signed combinations can indeed have the same favorable squarefree-random power budget as the earlier root differences, but that budget alone does not tell whether the combination sees the RH-relevant growth modes.

Let

\[
\Delta(n):=M(2n)-M(n),
\qquad
(TF)(n):=F(2n),
\]

and let

\[
P(z)=\sum_{j=0}^{d}a_jz^j\in\mathbb R[z]
\]

be a fixed nonzero polynomial. Define the signed root filter

\[
\mathcal F_P(n)
:=P(T)\Delta(n)
=\sum_{j=0}^{d}a_j\bigl(M(2^{j+1}n)-M(2^jn)\bigr).
\tag{1}
\]

By the root-aligned realization of `FD-206`, if `H_m=m p_m` with `p_m` the largest prime at most `m`, then

\[
\boxed{
\mathcal F_P(n)
=
\sum_{j=0}^{d}a_j
S_{2,H_{2^jn}}(p_{2^jn}).
}
\tag{2}
\]

Thus every fixed polynomial filter is an exact finite signed combination of physical Farey root sensors.

For the squarefree Rademacher multiplicative comparator of `FD-197`, every such nonzero fixed filter has critical random cost. If

\[
W(P):=\sum_{j=0}^{d}a_j^2\,2^j>0,
\]

then

\[
\boxed{
\mathbb E|\mathcal F_P^f(n)|^2
=
\frac6{\pi^2}W(P)n+O_P(n^{1/2}).
}
\tag{3}
\]

Consequently, on the root-aligned Farey scale `H_n=n p_n`, `K_n=floor(sqrt(H_n))`,

\[
\boxed{
\mathbb E\!\left[K_n|\mathcal F_P^f(n)|^2\right]
=
\left(\frac6{\pi^2}W(P)+o(1)\right)H_n.
}
\tag{4}
\]

The analytic usefulness of the filter is nevertheless constrained by its characteristic roots. Suppose `P` has a zero `rho` in the annulus

\[
\boxed{
\sqrt2<|\rho|\le2.
}
\tag{5}
\]

Then there exists a real sequence `u_m in {-1,0,1}` with summatory function

\[
A(N):=\sum_{m\le N}u_m
\]

such that

\[
\boxed{
P(T)\bigl(A(2n)-A(n)\bigr)=O_P(1)
\qquad(n\ge1),
}
\tag{6}
\]

but `A` violates the RH square-root scale: for some fixed `delta>0`,

\[
\boxed{
|A(N_k)|\gg N_k^{1/2+\delta}
}
\tag{7}
\]

along an unbounded sequence `N_k`.

Thus a fixed signed root filter may simultaneously

1. have the favorable `Theta(H)` squarefree-random Farey benchmark;
2. be uniformly tiny on a source with the same pointwise coefficient alphabet `{-1,0,1}` as Möbius;
3. fail to see a genuine super-square-root summatory mode.

The blind region has a natural interpretation. The inner radius `sqrt(2)` is the dyadic eigenvalue corresponding to the RH destination exponent `1/2`, while the outer radius `2` is the largest dyadic growth compatible with a bounded-coefficient summatory source. A characteristic root strictly between those radii is therefore a source-admissible but RH-supercritical homogeneous mode.

For a finite family `P_1,...,P_r`, the same construction defeats all filters simultaneously whenever they have a common zero in (5). Hence a necessary spectral audit for a fixed collective family is

\[
\boxed{
\gcd(P_1,\ldots,P_r)
\text{ has no zero }\rho\text{ with }\sqrt2<|\rho|\le2.
}
\tag{8}
\]

This is only a necessary condition, not a converse theorem. In particular, (8) does not show that a filter family without a common annular zero is RH-complete for the physical Möbius source.

## 1. Every fixed root filter keeps the critical random exponent

For the squarefree Rademacher multiplicative source

\[
f(m)=\mu(m)^2\prod_{p\mid m}X_p,
\qquad
A_f(x)=\sum_{m\le x}f(m),
\]

put

\[
\Delta_f(n)=A_f(2n)-A_f(n)
=\sum_{n<m\le2n}f(m).
\]

The dyadic blocks

\[
(2^jn,2^{j+1}n],
\qquad 0\le j\le d,
\]

are pairwise disjoint. As in `FD-197` and `FD-207`, squarefree Rademacher orthogonality gives

\[
\mathbb E[f(a)f(b)]
=
\mu(b)^2\mathbf1_{a=b}.
\]

Therefore all cross-block terms vanish exactly:

\[
\mathbb E|P(T)\Delta_f(n)|^2
=
\sum_{j=0}^{d}a_j^2
\sum_{2^jn<m\le2^{j+1}n}\mu(m)^2.
\tag{9}
\]

The elementary squarefree count

\[
\sum_{m\le x}\mu(m)^2
=
\frac6{\pi^2}x+O(\sqrt x)
\]

turns (9) into

\[
\mathbb E|P(T)\Delta_f(n)|^2
=
\frac6{\pi^2}n\sum_{j=0}^{d}a_j^2 2^j
+
O\!\left(
 n^{1/2}\sum_{j=0}^{d}a_j^2 2^{j/2}
\right).
\]

Because `P` is fixed, this is exactly (3).

On the root-aligned horizons of `FD-206`, the prime number theorem gives

\[
p_n\sim n,
\qquad
H_n=n p_n\sim n^2,
\qquad
K_n\sim n.
\]

Multiplying (3) by `K_n` proves (4). Therefore **every** nonzero fixed signed polynomial filter pays the same critical power exponent in this random comparator. Random cost alone does not distinguish a useful filter from a spectrally blind one.

## 2. An annular characteristic root creates an exact supercritical blind mode

Let `rho` satisfy (5) and `P(rho)=0`. Since `P` has real coefficients, a nonreal root occurs with its conjugate. Choose real numbers `alpha,beta` such that

\[
\rho=2^{\alpha+i\beta},
\qquad
\alpha=\log_2|\rho|.
\tag{10}
\]

Condition (5) is exactly

\[
\frac12<\alpha\le1.
\tag{11}
\]

For `x>0`, define

\[
Z(x):=x^{\alpha+i\beta}.
\]

Then dilation by two acts diagonally:

\[
Z(2x)=\rho Z(x),
\qquad
TZ=\rho Z.
\]

Choose a phase `phi` and a positive constant `c`, and set

\[
A_0(n):=c\,\Re\!\left(e^{i\phi}Z(n)\right),
\qquad n\ge1,
\qquad
A_0(0):=0.
\tag{12}
\]

Because `T` and `P(T)` have real coefficients,

\[
P(T)(T-I)A_0
=
c\,\Re\!\left(
 e^{i\phi}P(\rho)(\rho-1)Z
\right)
=0.
\tag{13}
\]

So the smooth source (12) is annihilated **exactly** by the signed root filter.

At the same time, (11) makes this source compatible with bounded increments. Differentiating,

\[
|Z'(x)|
=|\alpha+i\beta|x^{\alpha-1}
\le |\alpha+i\beta|
\qquad(x\ge1).
\]

Choose `c` small enough that

\[
|A_0(n)-A_0(n-1)|\le\frac14
\qquad(n\ge1).
\tag{14}
\]

The upper endpoint `|rho|=2` is important here: it corresponds to `alpha=1`, the last power for which this derivative remains uniformly bounded. Roots outside the radius `2` do not produce this bounded-increment countermodel by the same construction.

## 3. Rounding upgrades the blind mode to the Möbius coefficient alphabet

The continuous-valued source in (12) can be discretized without losing the obstruction. Let

\[
A(n):=\operatorname{round}(A_0(n)),
\qquad
A(0):=0,
\]

and define its coefficients by

\[
u_n:=A(n)-A(n-1).
\]

Write

\[
e(n):=A(n)-A_0(n).
\]

Then `|e(n)|<=1/2`. From (14),

\[
|u_n|
\le
|A_0(n)-A_0(n-1)|+|e(n)|+|e(n-1)|
\le\frac54.
\]

Since `u_n` is an integer,

\[
\boxed{u_n\in\{-1,0,1\}.}
\tag{15}
\]

Now use (13):

\[
P(T)(T-I)A
=P(T)(T-I)e.
\]

Therefore

\[
\begin{aligned}
|P(T)(T-I)A(n)|
&=
\left|
\sum_{j=0}^{d}a_j
\bigl(e(2^{j+1}n)-e(2^jn)\bigr)
\right|\\
&\le
\sum_{j=0}^{d}|a_j|,
\end{aligned}
\]

which proves (6).

Rounding changes the summatory function by only `O(1)`. If `beta=0`, choose `phi` so that the real coefficient in (12) is nonzero. If `beta!=0`, choose integers `N_k` approaching the exponentially spaced real points where `beta log N + phi` is a multiple of `2pi`; the relative rounding error in `N_k` tends to zero, so the cosine factor tends to `1` along a subsequence. In either case,

\[
|A(N_k)|\asymp N_k^\alpha.
\]

Since `alpha>1/2`, choose any

\[
0<\delta<\alpha-\frac12.
\]

Then (7) follows.

This is stronger than an unconstrained transform-space extremizer: the counterexample is the summatory function of a **real discrete bounded-alphabet source**. It still is not Möbius. The coefficients in (15) need not vanish on nonsquarefrees and need not satisfy multiplicative sign compatibility. Therefore the construction does not disprove any Möbius estimate; it identifies exactly what additional arithmetic structure a proof must use if its chosen filter has an annular blind root.

## 4. A concrete critical-cost filter that is analytically blind

Take

\[
P(z)=2z-3.
\]

Its root is

\[
\rho=\frac32,
\qquad
\sqrt2<\frac32<2,
\]

and the signed root observable is

\[
\boxed{
\mathcal F_P(n)
=2\Delta(2n)-3\Delta(n).
}
\tag{16}
\]

The random coefficient mass is

\[
W(P)=(-3)^2+2(2^2)=17,
\]

so

\[
\mathbb E|\mathcal F_P^f(n)|^2
=
\frac{102}{\pi^2}n+O(n^{1/2}),
\]

and the corresponding root-aligned Farey square has `Theta(H_n)` mean cost.

But

\[
\alpha=\log_2\frac32\approx0.58496>\frac12.
\]

The construction above supplies `u_m in {-1,0,1}` with

\[
A(N_k)\asymp N_k^{0.58496\ldots}
\]

while

\[
2\bigl(A(4n)-A(2n)\bigr)
-3\bigl(A(2n)-A(n)\bigr)
=O(1).
\]

Thus even a two-edge signed relation can look strictly better than the RH scale on its own observable while being blind to a source whose summatory growth is genuinely worse than square root.

This separates two notions that the previous random-budget calculations did not distinguish: **cost** measures how large the observable is on a random multiplicative comparator, while **spectral visibility** asks whether the observable actually sees every bounded-source mode above the destination exponent.

## 5. Finite collective families and the necessary gcd test

Let `P_1,...,P_r` be fixed real polynomials. If they have a common root `rho` satisfying (5), then the same `A_0`, and hence the same rounded bounded-alphabet source `A`, gives

\[
P_\ell(T)(T-I)A(n)=O_{P_\ell}(1)
\qquad
(1\le\ell\le r),
\]

while `A(N_k)` remains super-square-root. Therefore adding finitely many filters does not help if all of them share the same blind mode.

Equivalently, the greatest common divisor of the filter polynomials must avoid the physical supercritical annulus if the family is even to have a chance of being destination-complete using only bounded-source information. This proves the necessity in (8).

No converse is claimed. A family with no common annular root may still fail for other reasons, and the physical Möbius source has much more structure than the bounded alphabet used in the countermodel. The point is a **design veto**: any proposed fixed collective signed root statistic with a common annular zero has a concrete source-side blind direction and should not be treated as an RH-facing observable merely because its random-multiplicative variance is critical.

## 6. Representation audit and relation to the current frontier

The observable side of the statement is representation-native. Equation (2) uses the exact root-aligned Farey sensors of `FD-206`; no transformed extremizer is interpreted as a Möbius source.

The countermodel is also source-side rather than an arbitrary Fourier-coordinate vector: it is a summatory function of coefficients in `{-1,0,1}`. But it intentionally does **not** impose Möbius multiplicativity or squarefree support. Accordingly, the valid conclusion is not that the physical Möbius source realizes the blind mode. The valid conclusion is that any inversion or coercivity argument that uses only bounded coefficients, dyadic root geometry and the filtered pointwise estimate cannot rule it out. A successful proof with such a filter would have to invoke additional arithmetic structure.

The binomial family from `FD-207--FD-209` passes this particular audit. Its polynomial is

\[
P_q(z)=(z-1)^q,
\]

whose only root is `1`, strictly inside the RH radius `sqrt(2)`. `FD-207` then proves by a physical odd-step argument that fixed depth is destination-complete, and `FD-209` keeps that conclusion through common sublogarithmic depth on scale windows. The present result explains spectrally why that family has no source-admissible supercritical homogeneous mode of the type constructed here.

The collective opening after `FD-209` therefore needs a stronger test than a favorable random benchmark. A candidate fixed filter family should first have no common root in `sqrt(2)<|z|<=2`. If it does have one, the route is structurally blind unless it uses specifically Möbius arithmetic to exclude the corresponding bounded-alphabet mode. If it does not, the question remains open: absence of an annular common root may permit a stable collective inverse, but no such converse is proved here.

The other live opening from `FD-209` — a genuinely pointwise scale-dependent depth `q=q(n)` that changes along binary ancestor chains — is untouched by this fixed-polynomial theorem.

## 7. Prior-art and dependency audit

The algebraic fact behind the blind mode is classical recurrence theory: exponential sequences are eigenvectors of the shift operator, and zeros of a characteristic polynomial annihilate the corresponding modes. A web spot check found this standard fact in generic treatments of linear recurrences and shift operators, but no result applying the `sqrt(2)<|rho|<=2` source/destination annulus to Farey root sensors or Mertens recovery.

No external theorem is load-bearing here. The random second moment is derived from the same squarefree-Rademacher orthogonality and elementary squarefree count already used in `FD-197`, while the bounded-alphabet obstruction is proved explicitly above. `SOURCES.md` therefore does not need a new dependency.

## Consequence

`FD-207--FD-209` showed that the most obvious binomial signed root filters remain RH-complete despite critical random cost. The converse lesson is now explicit: **critical random cost does not by itself make an arbitrary signed filter useful**. Fixed filters have a spectral visibility problem, and any characteristic root in the physical supercritical annulus `sqrt(2)<|rho|<=2` creates a bounded-alphabet source direction that the filter cannot detect at RH scale.

The next collective constructions should therefore be screened in two stages: first by random/source cost, then by spectral visibility. For a finite fixed family, a common annular characteristic root is a decisive veto. The remaining high-value cases are scale-varying depth and collective filters whose characteristic polynomials have no common supercritical physical root.