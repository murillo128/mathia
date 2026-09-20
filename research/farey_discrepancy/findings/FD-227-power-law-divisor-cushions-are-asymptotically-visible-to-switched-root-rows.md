# FD-227 — Power-law divisor cushions are asymptotically visible to switched root rows

- **Date:** 2026-09-20
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response asymptotic / Jordan-totient transform / scale-adapted reservoir capacity / switched-nullspace obstruction / Mertens-cushion diagnosis
- **Depends on:** FD-226, FD-225, FD-005
- **Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + JORDAN-TOTIENT-RESPONSE + CAPACITY-SHAPE-VETO + SWITCHED-NULLSPACE`

## Claim

The most direct way to exploit the scale-adapted reservoir capacities of FD-226 does not work. A positive cushion whose occupancy grows smoothly like a power of the divisor index cannot lie, even asymptotically, in the switched nullspace.

Let

\[
(\mathscr A b)(m)
=
\sum_{d\le m}b_dM\!\left(\left\lfloor\frac md\right\rfloor\right)
\tag{1}
\]

be the exact divisor-response operator of FD-225. Fix `sigma>0` and suppose

\[
b_d=c d^\sigma+o(d^\sigma),
\qquad c\ne0.
\tag{2}
\]

Then

\[
\boxed{
(\mathscr A b)(m)
=
\frac{c}{(\sigma+1)\zeta(\sigma+1)}
 m^{\sigma+1}
+o(m^{\sigma+1}).
}
\tag{3}
\]

Consequently, for every fixed integer `r>=1`,

\[
\boxed{
(T-I)^r(\mathscr A b)(m)
=
\frac{c(2^{\sigma+1}-1)^r}
{(\sigma+1)\zeta(\sigma+1)}
 m^{\sigma+1}
+o(m^{\sigma+1}),
}
\tag{4}
\]

where `(TF)(m)=F(2m)`. The leading coefficient is nonzero for every `sigma>0`. Thus no asymptotically power-law growing occupancy profile can be annihilated by either row used in the switched schedule of FD-212--FD-226.

The case relevant to the natural capacities of the scale-adapted cells is `sigma=1`. If

\[
b_d=c d+o(d),
\tag{5}
\]

then

\[
(\mathscr A b)(m)
=
\frac{3c}{\pi^2}m^2+o(m^2),
\tag{6}
\]

and therefore

\[
(T-I)(\mathscr A b)(m)
=
\frac{9c}{\pi^2}m^2+o(m^2),
\tag{7}
\]

while

\[
(T-I)^4(\mathscr A b)(m)
=
\frac{243c}{\pi^2}m^2+o(m^2).
\tag{8}
\]

So the obvious FD-226 proposal — fill a fixed positive fraction of every scale-adapted prime reservoir, making the cushion proportional to its available capacity `asymp dN/(D log(dN))`, and then use a relatively small correction — produces a **quadratic switched signal**, not a null target.

More precisely, put

\[
B_N=\frac{N}{D\log N}.
\tag{9}
\]

Under the prime-resolution condition already proved in FD-226, the natural cell capacity satisfies uniformly for `1<=d<=D`

\[
P_{N,d}:=|I_d^*\cap\mathbb P|
=
\left(\frac14+o(1)\right)B_Nd,
\tag{10}
\]

because `D=N^{o(1)}` makes `log(dN)=(1+o(1))log N`. If a total occupancy profile satisfies, for some fixed `0<theta<1`,

\[
k_{N,d}=(\theta+o(1))P_{N,d}
\tag{11}
\]

uniformly over every cell used by a growing switched row, then the source-side reservoir contribution to that row is

\[
2(T-I)^r\mathscr A k_N(m)
=
\begin{cases}
\left(\dfrac{9\theta}{2\pi^2}+o(1)\right)B_Nm^2,&r=1,\\[6pt]
\left(\dfrac{243\theta}{2\pi^2}+o(1)\right)B_Nm^2,&r=4,
\end{cases}
\tag{12}
\]

for `m->infinity` with the deepest sample still at most `D`. In particular this cannot be `O(1)`, or even `o(B_Nm^2)`.

Hence any successful nonconstant switched-null cushion that exploits the larger `d`-cells must be genuinely non-regular: it needs order-one relative oscillation, depletion, or redistribution across divisor scales. A fixed-fraction capacity fill plus a subrelative correction cannot remove the remaining FD-226 bottleneck.

## 1. The divisor response sends a power profile to a Jordan-totient summatory profile

For the exact power profile `b_d=d^sigma`, expand the Mertens kernel:

\[
\begin{aligned}
(\mathscr A b)(m)
&=
\sum_{d\le m}d^\sigma
\sum_{a\le m/d}\mu(a)\\
&=
\sum_{n\le m}
\sum_{a\mid n}\mu(a)\left(\frac na\right)^\sigma.
\end{aligned}
\tag{13}
\]

Define

\[
J_\sigma(n)
:=
\sum_{a\mid n}\mu(a)\left(\frac na\right)^\sigma
=
 n^\sigma\prod_{p\mid n}(1-p^{-\sigma}).
\tag{14}
\]

For integer `sigma` this is the classical Jordan totient; formula (14) makes sense directly for every real `sigma>0`. Thus

\[
\mathscr A(d^\sigma)(m)
=
\sum_{n\le m}J_\sigma(n).
\tag{15}
\]

The required leading asymptotic is elementary. Writing the divisor sum in the other order and using

\[
\sum_{d\le x}d^\sigma
=
\frac{x^{\sigma+1}}{\sigma+1}
+O_\sigma(x^\sigma+1),
\tag{16}
\]

we get

\[
\sum_{n\le m}J_\sigma(n)
=
\frac{m^{\sigma+1}}{\sigma+1}
\sum_{a\le m}\frac{\mu(a)}{a^{\sigma+1}}
+o(m^{\sigma+1}).
\tag{17}
\]

Because `sigma+1>1`, the Dirichlet series is absolutely convergent and

\[
\sum_{a\ge1}\frac{\mu(a)}{a^{\sigma+1}}
=
\frac1{\zeta(\sigma+1)}.
\tag{18}
\]

This proves (3) for an exact power profile. No cancellation estimate for `M` is used.

For the perturbation in (2), write `b_d=cd^sigma+e_d` and

\[
E(x)=\sum_{d\le x}e_d=o(x^{\sigma+1}).
\]

From (1),

\[
\mathscr A e(m)
=
\sum_{a\le m}\mu(a)E\!\left(\left\lfloor\frac ma\right\rfloor\right).
\tag{19}
\]

Fix a large cutoff `Y`. On terms with `m/a>=Y`, the definition of `o(x^(sigma+1))` bounds the contribution by an arbitrarily small multiple of

\[
m^{\sigma+1}
\sum_{a\ge1}a^{-\sigma-1}.
\]

On the remaining terms `m/a<Y`, the values of `E` are bounded in terms of `Y`, so their total is `O_Y(m)=o(m^(sigma+1))`. Hence

\[
\mathscr A e(m)=o(m^{\sigma+1}),
\tag{20}
\]

which completes (3).

## 2. Every fixed root row sees the leading power

Apply one fixed dilation difference of order `r` to (3):

\[
(T-I)^r(\mathscr A b)(m)
=
\sum_{j=0}^r
(-1)^{r-j}\binom rj
(\mathscr A b)(2^jm).
\tag{21}
\]

The leading term is multiplied by

\[
\sum_{j=0}^r
(-1)^{r-j}\binom rj
2^{j(\sigma+1)}
=
(2^{\sigma+1}-1)^r.
\tag{22}
\]

For `sigma>0` this is strictly nonzero. Equation (4) follows.

At `sigma=1`, `J_1=phi`, so (15) becomes the familiar totient summatory function

\[
\mathscr A(d)(m)=\sum_{n\le m}\varphi(n)
=
\frac{3}{\pi^2}m^2+o(m^2).
\tag{23}
\]

The two switched rows use `r=q+1` with `r=1` and `r=4`, and `(4-1)^r=3^r`, giving (7)--(8).

This also explains why the constant cushion of FD-225 is exceptional rather than the first member of a harmless power family. At exponent zero the Dirichlet-series coefficient in (3) hits the pole of `zeta(1)`, and in fact the exact identity from FD-005 is

\[
\boxed{\mathscr A\mathbf1=\mathbf1.}
\tag{24}
\]

The constant occupancy is therefore exactly invisible to every positive-order dilation difference. As soon as the occupancy has any genuine positive power growth, the response acquires a nonzero power-law main term and becomes visible at full leading order.

## 3. Application to the scale-adapted prime capacities

FD-226 proved

\[
|I_d^*\cap\mathbb P|
\sim
\frac{dN}{4D\log(dN)}
\tag{25}
\]

uniformly in the certified range once

\[
D\,\operatorname{polylog}(DN)e^{-c\Phi(N)}=o(1).
\]

Since `D=N^(o(1))`, equation (25) is exactly (10). Therefore a profile that uses asymptotically the same positive fraction `theta` of every reservoir satisfies

\[
\frac{k_{N,d}}{B_N}
=
\frac\theta4d+o(d)
\tag{26}
\]

uniformly across the cells seen by any growing row.

For completeness, the finite-range uniformity needed here does not require a new asymptotic theorem. If

\[
r_{N,d}=o(B_Nd)
\]

uniformly for `d<=L_N`, then for `m<=L_N`

\[
\left|\mathscr A r_N(m)\right|
\le
\sum_{d\le m}|r_{N,d}|
\left|M\!\left(\left\lfloor\frac md\right\rfloor\right)\right|.
\tag{27}
\]

Using only the trivial bound `|M(x)|<=x`, the large-`d` part is `o(B_Nm^2)` and every fixed initial segment contributes only `O(B_Nm)=o(B_Nm^2)`. Thus the asymptotic (6) transfers uniformly to the triangular capacity profile. Applying the fixed row coefficients and restoring the factor `2` from one prime flip gives (12).

Rounding each occupancy to an integer changes every cell by `O(1)`. The same trivial estimate makes the resulting row error `O(m^2)` at worst, which is `o(B_Nm^2)` because `B_N=N/(D log N)->infinity` in the present subpower-depth regime.

Therefore an `o(1)` relative perturbation of a fixed-fraction capacity fill cannot cancel the leading switched leakage. Any switched-null use of the variable capacities must alter the capacity profile by order one on a non-negligible set of relevant divisor scales.

## 4. Prior-art and novelty boundary

The arithmetic core of (14)--(23) is classical. Jordan totients satisfy `J_k=mu*id^k`, and their summatory functions have the standard leading term `x^(k+1)/((k+1)zeta(k+1))`; the error term and its oscillation have a substantial literature, for example Y.-F. S. Pétermann, *Oscillations d'un terme d'erreur lié à la fonction totient de Jordan*, Journal de théorie des nombres de Bordeaux **3** (1991), 311--335, DOI `10.5802/jtnb.53`. No claim of novelty is made for Jordan totients, their average order, or Dirichlet convolution.

No external error-term theorem is load-bearing here: (3) is derived directly from absolute convergence at `sigma+1>1`, and the `sigma=1` consequence needs only its leading term. The literature search found the expected classical Jordan/totient summatory theory, but no treatment of the FD-225 divisor-reservoir operator coupled to the periodically switched Farey root rows.

The repository-specific result is the capacity-shape veto: the natural `d`-growth exposed by the scale-adapted exact floor cells of FD-226 is transformed into a quadratic totient-summatory mode, and both switched annihilators see that mode with explicit nonzero leading constants.

## 5. Boundary and research consequence

FD-227 does **not** prove that the smallest-cell cushion in FD-226 is intrinsic. It rules out a much narrower but natural escape: a smooth capacity-adapted positive baseline, or any total occupancy that differs from a fixed positive fraction of cell capacity by only a subrelative amount.

Strongly oscillatory occupancy profiles remain open. In particular, the periodically switched system has nontrivial Floquet null modes from FD-212, and this finding does not show that an arithmetic/divisor-scale analogue of such a mode cannot be realized with nonnegative reservoir occupancies and enough local slack to absorb the physical Mertens correction.

The next discriminating test is therefore more specific than in FD-226. Rather than searching over smooth nonconstant targets, one must determine whether the switched nullspace contains a **capacity-feasible oscillatory occupancy profile** whose cellwise lower slack grows on the same scale as the Mertens correction. If every such null profile must have order-one depletions that repeatedly expose small-capacity cells, that would be a genuine capacity obstruction. If one can construct an oscillatory null profile with positive proportional slack, the remaining `D^2` cushion loss can still be reduced.

No clue status changes follow from this finding. No new literature dependency is required in `SOURCES.md`: the classical Jordan-totient fact used for prior-art classification is reproved to the needed precision above.