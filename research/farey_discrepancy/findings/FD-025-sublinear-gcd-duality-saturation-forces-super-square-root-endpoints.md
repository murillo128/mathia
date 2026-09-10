# FD-025 — sublinear GCD-duality saturation forces super-square-root endpoints

**Status:** `EXACT-DERIVED + HORIZON-FREE-SOURCE-OBSTRUCTION + SHARP-HALF-POWER-ENVELOPE-BOUNDARY + NEGATIVE/OBSTRUCTION`.

`FD-023` shows that a polynomial-growth common source cannot Cesàro-saturate the sharp GCD-duality constant along a hierarchy whose logarithmic horizon growth per retained scale stays bounded. `FD-024` gives the complementary sparse construction: for every fixed exponent `alpha>1/2` and every prescribed horizon sequence with `H_j/H_(j-1)->infinity`, one can construct a single real source satisfying `|A(n)|<=n^alpha` whose normalized ratios tend to `zeta(2)`.

The endpoint left open by `FD-024` is not merely a limitation of its weighted-tail estimate. There is a different obstruction at exactly the square-root scale, and it does **not** depend on horizon density.

Let

\[
K_H(d,e)=\frac{\gcd(d,e)^2}{de},
\qquad
Z:=\zeta(2),
\]

and for a real source `A(1),A(2),...` define

\[
m_d^{(H)}:=A\!\left(\left\lfloor\frac Hd\right\rfloor\right),
\qquad
E_H:=(m^{(H)})^TK_Hm^{(H)},
\qquad
R_H:=\frac{A(H)^2}{E_H},
\tag{1}
\]

with `R_H:=0` when the horizon vector is zero. Also write

\[
C_H:=(K_H^{-1})_{11}\uparrow Z.
\tag{2}
\]

Fix any nonzero source `A`, and let

\[
n_0:=\min\{n\ge1:A(n)\ne0\},
\qquad
a_0:=A(n_0)\ne0.
\tag{3}
\]

Then along **every** sequence of horizons `H->infinity` on which

\[
A(H)=o(H),
\tag{4}
\]

the distance from the GCD equality ray has a linear floor-quotient plateau lower bound:

\[
\boxed{
\liminf_{H\to\infty}
\frac{E_H-A(H)^2/C_H}{H}
\ge
\frac{a_0^2}{Z\,n_0(n_0+1)}.
}
\tag{5}
\]

Consequently, if `R_(H_j)->Z` on any unbounded horizon sequence and `A(H_j)=o(H_j)`, then necessarily

\[
\boxed{
\frac{|A(H_j)|}{\sqrt{H_j}}\longrightarrow\infty.
}
\tag{6}
\]

Thus every **sublinear** common source that saturates GCD duality on any sparse set of horizons must have super-square-root endpoint amplitude on those horizons. In particular, for every fixed `C<infinity`, a nonzero source satisfying

\[
|A(n)|\le C\sqrt n
\tag{7}
\]

cannot saturate `Z` along any horizon sequence. More quantitatively,

\[
\boxed{
\limsup_{H\to\infty}R_H
\le
\left(
\frac1Z+
\frac{a_0^2}{C^2Z\,n_0(n_0+1)}
\right)^{-1}
<Z.
}
\tag{8}
\]

If instead `A(H)=o(sqrt(H))`, then

\[
\boxed{R_H\longrightarrow0.}
\tag{9}
\]

Combining (8) with `FD-024` makes `alpha=1/2` a sharp phase boundary for the **fixed power-envelope-only relaxation** on supermultiplicatively separated horizons: every exponent strictly above one half permits a synthetic saturating source, while exponent one half or below forbids saturation for every nonzero source under a fixed global power bound. This remains a theorem about a relaxed common source, not a new bound for the physical Mertens function.

## 1. The first nonzero source value creates a macroscopic terminal plateau

The key object is not the endpoint coordinate itself but a block of divisor-incidence rows on which no earlier source value can cancel `a_0`.

For each sufficiently large `H`, define the exact floor-quotient fiber

\[
I_H(n_0)
:=
\left\{d\le H:
\left\lfloor\frac Hd\right\rfloor=n_0
\right\}.
\tag{10}
\]

Equivalently,

\[
I_H(n_0)
=
\left(
\frac{H}{n_0+1},\frac{H}{n_0}
\right]\cap\mathbb Z,
\tag{11}
\]

so

\[
|I_H(n_0)|
=\left\lfloor\frac H{n_0}\right\rfloor
-\left\lfloor\frac H{n_0+1}\right\rfloor
=rac{H}{n_0(n_0+1)}+O(1).
\tag{12}
\]

For an arbitrary vector `x in R^H`, introduce the divisor-incidence transform

\[
T_r(x)
:=
\sum_{\substack{d\le H\\r\mid d}}\frac{x_d}{d}
=
\sum_{k\le H/r}\frac{x_{rk}}{rk}.
\tag{13}
\]

Take `x=m^(H)` and `d in I_H(n_0)`. Its first term is

\[
\frac{m_d^{(H)}}d=\frac{a_0}{d}.
\tag{14}
\]

Every possible later term has `k>=2`. If `n_0>=2`, then from `H/d<n_0+1`,

\[
\frac{H}{kd}<\frac{n_0+1}{2}<n_0,
\]

hence

\[
\left\lfloor\frac{H}{kd}\right\rfloor<n_0.
\tag{15}
\]

By minimality of `n_0`, its source value vanishes. If `n_0=1`, no `k>=2` can occur at all, because `d>H/2`. Therefore in every case

\[
\boxed{
T_d(m^{(H)})=\frac{a_0}{d}
\qquad(d\in I_H(n_0)).
}
\tag{16}
\]

This is an exact one-sided plateau identity. It uses only that the source has a first nonzero value, not sign, multiplicativity, bounded increments, or a growth hypothesis.

## 2. The equality ray is negligible on the same plateau for sublinear endpoints

Retain the `FD-014` equality-ray notation

\[
u^{(H)}:=K_H^{-1}e_1,
\qquad
v^{(H)}:=\frac{u^{(H)}}{C_H},
\tag{17}
\]

so `v_1^(H)=1`. The Smith/Jordan factorization from `FD-003` is

\[
K_H=D^{-1}E^TJE D^{-1},
\tag{18}
\]

where `E_(r,d)=1_(r|d)` and `J=diag(J_2(1),...,J_2(H))`. Consequently

\[
x^TK_Hx
=\sum_{r\le H}J_2(r)T_r(x)^2.
\tag{19}
\]

There is also an exact formula for the incidence transform of the equality ray. Since `K_Hu^(H)=e_1`, multiplying the `d`-th coordinate by `d` gives

\[
\sum_{r\mid d}J_2(r)T_r(u^{(H)})=\mathbf1_{d=1}.
\tag{20}
\]

Möbius inversion therefore yields

\[
J_2(d)T_d(u^{(H)})=\mu(d),
\]

and hence

\[
\boxed{
T_d(v^{(H)})
=\frac{\mu(d)}{C_HJ_2(d)}.
}
\tag{21}
\]

Now set

\[
t_H:=A(H),
\qquad
w^{(H)}:=m^{(H)}-t_Hv^{(H)}.
\tag{22}
\]

For `d in I_H(n_0)`, equations (16) and (21) give

\[
T_d(w^{(H)})
=
\frac{a_0}{d}
-
\frac{t_H\mu(d)}{C_HJ_2(d)}.
\tag{23}
\]

Because

\[
C_H\ge1,
\qquad
J_2(d)\ge\frac{d^2}{Z},
\tag{24}
\]

we have uniformly on the entire plateau

\[
\left|
\frac{t_H\mu(d)}{C_HJ_2(d)}
\right|
\le\frac{Z|t_H|}{d^2}.
\tag{25}
\]

Since every `d in I_H(n_0)` satisfies `d>H/(n_0+1)`, the ratio of the correction in (25) to the main term `|a_0|/d` is at most

\[
\frac{Z(n_0+1)|t_H|}{|a_0|H}.
\tag{26}
\]

Under the sole endpoint assumption `t_H=o(H)`, this tends to zero uniformly. Thus

\[
\boxed{
T_d(w^{(H)})
=\frac{a_0}{d}\bigl(1+o(1)\bigr)
}
\tag{27}
\]

uniformly for `d in I_H(n_0)`.

## 3. The plateau contributes linear irreducible off-ray energy

The equality-ray projection identity from `FD-014` is exact:

\[
\|w^{(H)}\|_{K_H}^2
=E_H-\frac{t_H^2}{C_H}.
\tag{28}
\]

Applying the positive decomposition (19) and keeping only rows in `I_H(n_0)`,

\[
E_H-\frac{t_H^2}{C_H}
\ge
\sum_{d\in I_H(n_0)}
J_2(d)T_d(w^{(H)})^2.
\tag{29}
\]

Using (24) and the uniform estimate (27), each retained row contributes at least

\[
\frac{a_0^2}{Z}\bigl(1+o(1)\bigr).
\tag{30}
\]

Together with (12),

\[
E_H-\frac{t_H^2}{C_H}
\ge
\frac{a_0^2}{Z\,n_0(n_0+1)}H\bigl(1+o(1)\bigr),
\tag{31}
\]

in the one-sided liminf sense. This proves (5).

For an entirely explicit but weaker finite constant, (26) is eventually at most `1/2`, while (12) is eventually at least `H/[2n_0(n_0+1)]`. Hence for all sufficiently large horizons satisfying the chosen sublinear tail,

\[
\boxed{
E_H-\frac{t_H^2}{C_H}
\ge
\frac{a_0^2}{8Z\,n_0(n_0+1)}H.
}
\tag{32}
\]

No cancellation between selected rows can reduce this cost because (19) is a sum of nonnegative squares.

## 4. Saturation requires super-square-root endpoint amplitude

When `t_H\ne0`, equations (1) and (28) give

\[
\frac1{R_H}-\frac1{C_H}
=
\frac{E_H-t_H^2/C_H}{t_H^2}.
\tag{33}
\]

Suppose `H_j->infinity`, `t_(H_j)=o(H_j)`, and `R_(H_j)->Z`. Since `C_(H_j)->Z`, the left side of (33) tends to zero. But (5) gives

\[
\frac1{R_{H_j}}-
\frac1{C_{H_j}}
\ge
\left(
\frac{a_0^2}{Z\,n_0(n_0+1)}+o(1)
\right)
\frac{H_j}{|A(H_j)|^2}.
\tag{34}
\]

The right side can tend to zero only if

\[
\frac{H_j}{|A(H_j)|^2}\to0,
\]

which is exactly (6).

This conclusion is horizon-free: no relation at all is required between successive `H_j`. The density, integer-ratio, squarefree-transition, and horizon-entropy mechanisms of `FD-014`--`FD-023` are absent. The obstruction comes from one macroscopic floor-quotient fiber attached to the earliest nonzero source value.

## 5. The fixed square-root envelope has a strict global saturation gap

Assume now that for some finite `C>0`,

\[
|A(H)|\le C\sqrt H
\tag{35}
\]

for all sufficiently large `H`. This is sublinear, so (5) applies. Equation (33), together with `C_H->Z`, yields

\[
\liminf_{H\to\infty}
\frac1{R_H}
\ge
\frac1Z+
\frac{a_0^2}{C^2Z\,n_0(n_0+1)},
\tag{36}
\]

where horizons with `A(H)=0` already have `R_H=0`. Taking reciprocals proves (8).

If `A(H)=o(sqrt H)`, then `H/|A(H)|^2->infinity` along every nonzero endpoint. Equation (34) forces `1/R_H->infinity`, while zero endpoints again give `R_H=0`. This proves (9).

In particular, for a fixed power envelope

\[
|A(n)|\le Cn^\alpha,
\tag{37}
\]

one gets the clean trichotomy on the lower side:

- if `alpha<1/2`, then `R_H->0`;
- if `alpha=1/2`, then `limsup R_H<Z` by an explicit source-dependent constant;
- if `alpha>1/2`, `FD-024` shows that on every prescribed supermultiplicative horizon sequence there exists a source obeying such an envelope with `R_(H_j)->Z`.

Thus the square-root exponent is not merely where the `FD-024` GCD-tail estimate stops decaying. It is the exact envelope threshold separating a universal obstruction from sparse synthetic saturation.

## 6. Relation to the Farey/Mertens problem

The new theorem strengthens the relaxation boundary rather than importing hidden RH information. It does **not** assert that the physical Mertens function satisfies a fixed `O(sqrt n)` bound, and it does not obtain such a bound from Farey discrepancy. The physical source is still distinguished from the synthetic sources of `FD-024` by its Möbius increments, squarefree support, divisor identities, and multiplicative sign structure.

What changes is the interpretation of sparse-horizon interpolation. `FD-024` left open the possibility that the exponent `1/2` failed only because its inherited-tail estimate was too weak. Equation (5) rules that out: at or below the square-root envelope, the obstruction already appears in a positive block of Smith/Jordan coordinates and persists no matter how far apart the sampled horizons are.

The surviving route therefore has a precise source-specific target. To improve on this relaxation boundary at the RH-relevant `1/2+epsilon` scale, one must exploit structure that suppresses or couples the synthetic freedom **above** the square-root amplitude threshold. Horizon sparsity and endpoint power growth alone are now classified on both sides of `1/2`.

## 7. Stress tests and prior-art boundary

Several edge cases are load-bearing. If `A` is identically zero then `R_H=0` and there is no `n_0`; the theorem is stated for nonzero sources. If `n_0=1`, the plateau `I_H(1)` lies above `H/2`, so no multiple `kd<=H` with `k>=2` exists and (16) remains exact. If `n_0>=2`, inequality (15) ensures every later multiple samples a strictly smaller source index. Zero endpoint values cause no division problem because their ratio was defined to be zero.

The equality-ray transform (21) is an exact Möbius inversion of the Smith/Jordan incidence factorization, not an asymptotic ansatz. The only limiting input in the plateau comparison is `A(H)=o(H)`. The constant in (5) is one-sided; no matching upper asymptotic for the off-ray energy is claimed. The strict gap at `alpha=1/2` depends on the fixed source through its first nonzero value and therefore is not a uniform gap over all nonzero real sources.

The closest classical ingredients remain the Smith/meet-matrix factorization and Möbius inversion already anchored in `SOURCES.md`. A targeted literature audit also checked neighboring work on symmetric matrices related to the Mertens function, floor-quotient Möbius formulations, and GCD-matrix extremality. No directly matching theorem about the first nonzero floor-quotient plateau forcing linear distance from the normalized GCD equality ray was located; absence of a search hit is not used as a novelty claim. No new external theorem is needed for the proof, so the durable source list does not change.

A decisive falsification would be a nonzero source and unbounded horizons with `A(H)=o(H)` for which the normalized off-ray energy in (5) falls below the stated liminf. Such an example would have to break one of the exact steps (16), (21), or the positive Smith/Jordan decomposition (29). The argument is otherwise independent of unproved cancellation estimates.

The durable conclusion is the sharp relaxation boundary: **for sublinear common sources, GCD-duality saturation at any horizons requires endpoint amplitude `omega(sqrt H)`; hence fixed square-root growth already forbids saturation, while `FD-024` shows every fixed exponent strictly above one half permits it on supermultiplicatively sparse horizons.**