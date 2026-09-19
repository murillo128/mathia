# FD-212 — Period-three diagonal root depth creates a source-realizable supercritical Floquet blind ray

- **Date:** 2026-09-19
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** scale-varying diagonal root filter / periodic switched recurrence / bounded-source sparse-ray countermodel / critical random-cost audit
- **Depends on:** FD-206, FD-208, FD-209, FD-211
- **Classification:** `EXACT-DERIVED + DIAGONAL-SCALE-SWITCHING + PERIODIC-FLOQUET-MULTIPLIER + BOUNDED-SOURCE-DYADIC-RAY-REALIZATION + CRITICAL-RANDOM-COST + REPRESENTATION-BOUNDARY`

## Claim

`FD-209` closes every common sublogarithmic binomial depth controlled on a whole scale window, while `FD-211` classifies every fixed finite polynomial family controlled pointwise at every scale. The remaining diagonal opening is genuinely different even when the depth does **not** grow.

Let

\[
\Delta_A(n):=A(2n)-A(n),
\qquad
\mathcal C_q^A(n):=(T-I)^q\Delta_A(n)=(T-I)^{q+1}A(n),
\qquad
(TF)(n):=F(2n).
\tag{1}
\]

On the dyadic ray `n=2^j`, choose the source-independent period-three depth schedule

\[
\boxed{
q_j=
\begin{cases}
0,&j\equiv0\pmod3,\\
3,&j\equiv1,2\pmod3.
\end{cases}}
\tag{2}
\]

There exists a real bounded source `|u_m|<=1` with summatory function

\[
A(N)=\sum_{m\le N}u_m
\tag{3}
\]

such that

\[
\boxed{
\mathcal C_{q_j}^A(2^j)=0
\qquad(j\ge0),
}
\tag{4}
\]

but along the same dyadic ray

\[
\boxed{
|A(2^{3m})|\asymp (2^{3m})^\alpha,
\qquad
\alpha=\frac43\log_2\!\frac{1+\sqrt5}{2}
\approx0.9256558848>\frac12.
}
\tag{5}
\]

Thus a bounded-depth **diagonal** root filter can be exactly blind on an infinite dyadic observation ray to a source with strongly super-square-root summatory growth. The obstruction is a periodic switched/Floquet multiplier; it is absent from the fixed-filter gcd test because only one filter is observed at each scale.

At the same time, this schedule has RH-critical random cost in the precise sense of `FD-208`. Since it uses only `q=0` and `q=3`, whose Delannoy masses are

\[
D_0=1,
\qquad
D_3=63,
\tag{6}
\]

its root-normalized squarefree-Rademacher second moment remains

\[
\mathbb E\!\left[K_n|\mathcal C_{q(n)}^f(n)|^2\right]
=\Theta(H_n)
\tag{7}
\]

for any extension of (2) to all integers that keeps the same two depths, for example by the dyadic-band phase `q(n)=q_{\lfloor\log_2 n\rfloor}`.

This does **not** disprove an all-integer diagonal RH criterion for Möbius. The bounded source constructed below is only forced to annihilate the switched filters at dyadic powers, not at every integer, and it is not multiplicative. What it does prove is that the remaining diagonal opening from `FD-209` cannot be closed by applying the fixed-family spectral argument independently on each dyadic ray: periodic scale switching itself can create a supercritical source-realizable blind multiplier while every local characteristic polynomial has only the harmless root `1`.

## 1. A period-three switched finite-difference null mode

Write `E` for the unit shift on a sequence `(a_j)`:

\[
(Ea)_j=a_{j+1}.
\]

The diagonal equation corresponding to (2) is

\[
(E-I)^{r_j}a_j=0,
\qquad
(r_j)=(1,4,4,1,4,4,\ldots),
\tag{8}
\]

where `r_j=q_j+1`.

Seek a period-three Floquet form

\[
a_{3m}=\lambda^m c_0,
\qquad
a_{3m+1}=\lambda^m c_1,
\qquad
a_{3m+2}=\lambda^m c_2.
\tag{9}
\]

The phase `r=1` equation gives immediately

\[
c_1=c_0.
\tag{10}
\]

Normalize `c_0=c_1=1`. The two fourth-difference equations become

\[
\lambda(c_2-4c_1+6c_0)-4c_2+c_1=0,
\tag{11}
\]

and

\[
\lambda^2c_0
+\lambda(-4c_2+6c_1-4c_0)
+c_2=0.
\tag{12}
\]

Eliminating `c_2` gives

\[
\boxed{
(\lambda-1)(\lambda^2+7\lambda+1)=0.
}
\tag{13}
\]

Choose the large negative root

\[
\boxed{
\lambda=-\frac{7+3\sqrt5}{2}
=-\varphi^4,
\qquad
\varphi=\frac{1+\sqrt5}{2},
}
\tag{14}
\]

and then (11) gives

\[
\boxed{
c_2=\frac{2\lambda+1}{4-\lambda}
=-\frac{5+3\sqrt5}{10}.}
\tag{15}
\]

Substitution in (11)--(12) verifies both equations exactly. Hence (8) holds at every phase.

After each period of three dyadic steps the mode is multiplied by `lambda`. Its per-step growth modulus is therefore

\[
\boxed{
\rho=|\lambda|^{1/3}=\varphi^{4/3}\approx1.89954762695.
}
\tag{16}
\]

This lies strictly in the physical supercritical band

\[
\sqrt2<\rho<2.
\tag{17}
\]

The upper inequality is exact because `|lambda|<8` is equivalent to `sqrt(5)<3`; the lower one is immediate from `|lambda|>2sqrt(2)`. Consequently

\[
|a_j|=2^{(\alpha+o(1))j},
\qquad
\alpha=\log_2\rho\approx0.9256558848.
\tag{18}
\]

The important point is structural. Neither local filter has an annular characteristic root: the only polynomials used are `(z-1)` and `(z-1)^4`, both with sole root `1`. The supercritical multiplier appears only after the filters are **switched periodically**.

## 2. The Floquet ray is realizable by an actual bounded source

The sequence in Section 1 is not merely an abstract transform-coordinate vector. Because `rho<2`, it can be embedded exactly as dyadic endpoint values of a summatory function with uniformly bounded increments.

Indeed, from (9) and (16) there is a constant `C_0` such that

\[
|a_j|\le C_0\rho^j.
\tag{19}
\]

Therefore

\[
\sup_{j\ge0}
\frac{|a_{j+1}-a_j|}{2^j}<\infty,
\tag{20}
\]

since the ratio is `O((rho/2)^j)`. Choose a fixed scale `epsilon>0` small enough that both `|epsilon a_0|<=1` and

\[
\epsilon\frac{|a_{j+1}-a_j|}{2^j}\le1
\qquad(j\ge0).
\tag{21}
\]

Define

\[
u_1=\epsilon a_0
\tag{22}
\]

and, on each dyadic block,

\[
\boxed{
u_m=
\epsilon\frac{a_{j+1}-a_j}{2^j}
\qquad(2^j<m\le2^{j+1}).}
\tag{23}
\]

Then `|u_m|<=1`, and the block sums telescope exactly:

\[
\boxed{
A(2^j)=\sum_{m\le2^j}u_m=\epsilon a_j
\qquad(j\ge0).
}
\tag{24}
\]

Now evaluate (1) at `n=2^j`. Every dyadic shift stays on the embedded endpoint ray, so

\[
\mathcal C_{q_j}^A(2^j)
=\epsilon(E-I)^{q_j+1}a_j
=0.
\tag{25}
\]

At phase zero,

\[
|A(2^{3m})|
=\epsilon|\lambda|^m
=\epsilon(2^{3m})^\alpha,
\tag{26}
\]

which proves (4)--(5).

This source-realizability check matters for the representation audit. The switched multiplier is not merely an extremizer in an unconstrained coefficient space: it can be carried by a genuine bounded increment sequence. What remains absent is the much stronger Möbius structure and all-integer annihilation.

## 3. Critical random cost survives the switching

For the squarefree Rademacher multiplicative comparator of `FD-208`, the exact coefficient mass is

\[
D_q=\sum_{k=0}^q\binom qk^2 2^k.
\tag{27}
\]

The two depths in (2) give

\[
D_0=1,
\qquad
D_3=1+18+36+8=63.
\tag{28}
\]

`FD-208` proves uniformly in the chosen depth that, at the root-aligned Farey normalization,

\[
\mathbb E\!\left[K_n|\mathcal C_q^f(n)|^2\right]
=
\left(\frac6{\pi^2}+o(1)\right)H_nD_q.
\tag{29}
\]

Since `D_(q(n))` is bounded between `1` and `63`, the switched schedule pays only a constant-factor tariff:

\[
\boxed{
\mathbb E\!\left[K_n|\mathcal C_{q(n)}^f(n)|^2\right]
=\Theta(H_n).
}
\tag{30}
\]

Thus the new blind mechanism is not bought by the growing Delannoy cost isolated in `FD-208`. It already appears at bounded depth, inside the strongest possible critical-random window.

## 4. Why this does not contradict FD-209 or FD-211

`FD-209` assumes one **common** depth `q(X)` across a whole square-root scale window. Its Green-kernel inversion is allowed to use the same level `F_Q` along all relevant binary ancestors. Schedule (2) deliberately removes that coherence: the level changes from one ancestor to the next.

`FD-211` assumes a fixed finite family `P_1,...,P_r` is controlled pointwise at every scale. The two polynomials appearing here,

\[
P_0(z)=1,
\qquad
P_3(z)=(z-1)^3
\tag{31}
\]

when applied to `Delta_A`, have gcd `1`, so simultaneous pointwise control of both is square-root complete by `FD-211`. The switched hypothesis is weaker: at each scale it reveals only **one** member of the family. Equivalently, the annihilator on `A` alternates between `(T-I)` and `(T-I)^4`.

The distinction is exactly the familiar one between stability of individual operators and stability of a prescribed switched product. Here each fixed operator is spectrally harmless in the `FD-211` sense, while the period-three monodromy of the nonautonomous recurrence has the multiplier (14).

This refines the research frontier materially. The surviving diagonal escape does not require `q(n)->infinity`; **scale variation alone is sufficient to break the fixed-filter inversion mechanism on sparse dyadic rays**.

## 5. Prior-art and novelty boundary

Periodic-coefficient difference equations and Floquet multipliers are classical, and switched linear systems are classically analyzed through growth of matrix products and joint/constrained spectral radii. The literature search therefore treats the existence of switching-induced instability as prior art, not as a new general dynamical-systems phenomenon.

The new content claimed here is only the exact specialization to the Mathia root-filter family: the explicit `(0,3,3)` diagonal depth schedule, the algebraic multiplier `-(7+3sqrt(5))/2`, its location between the square-root and bounded-source growth radii after taking the cube root, the bounded-source dyadic-ray realization, and the simultaneous `Theta(H)` random-cost audit. All of those statements are proved directly above; no Floquet or switched-systems theorem is load-bearing, so no new durable source anchor is required.

A prior-art search found no direct treatment of this dyadic `(T-I)^(q(n)+1)` root-sensor problem or its Farey/Mertens realization. This is not a claim of global novelty for periodic variable-order recurrences.

## Boundaries and research consequence

The construction proves a **sparse-ray bounded-source obstruction**, not an all-integer Möbius obstruction. In particular:

- the source in (23) is real and bounded but is not asserted to be squarefree-supported or multiplicative;
- (25) is guaranteed at `n=2^j`, not for every integer `n`;
- nothing here shows that the physical Möbius source can realize the Floquet mode;
- therefore the all-integer diagonal statement
  `C_(q(n))(n)=O_epsilon(n^(1/2+epsilon)) => RH`
  remains open for genuinely scale-varying `q(n)`.

The decisive next test is now sharper. One must determine whether additive coherence between **different dyadic rays** kills the switched multiplier when the diagonal estimate is imposed for all integers, or whether a bounded source can be constructed that preserves a super-square-root switched mode on a dense/all-integer set. A proof that only analyzes one ray at a time cannot close the opening: (23)--(26) give an exact source-side countermodel to that strategy.

For the Farey line, this means that the remaining route is no longer simply “let the depth grow.” The relevant structural question is whether scale-dependent selection can exploit nonautonomous switching while respecting the full cross-ray coherence of the Mertens source and the root-aligned Farey sensors.