# FD-259 — Monotone divisor response forces sharp inverse-linear capacity depletion

- **Date:** 2026-09-21
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response positivity / nonnegative Möbius increments / switched finite differences / sharp dyadic capacity depletion / scale-adapted cushion obstruction
- **Depends on:** FD-225, FD-226, FD-257
- **Classification:** `EXACT-DERIVED + POSITIVITY-OBSTRUCTION + NONNEGATIVE-MOBIUS-INCREMENTS + MONOTONE-DIVISOR-RESPONSE + SHARP-INVERSE-LINEAR-CAPACITY-DEPLETION`

## Claim

FD-257 proves that an arbitrary nonnegative linear-capacity cushion with bounded switched rows must lose a fixed positive power of its relative dyadic capacity. There is a natural source-side subclass in which the depletion is much stronger and, at aggregate scale, sharp.

Retain the exact divisor-response operator

\[
(\mathscr A b)(m)
=
\sum_{d\le m}b_dM\!\left(\left\lfloor\frac md\right\rfloor\right),
\tag{1}
\]

and suppose

\[
0\le b_n\le Cn.
\tag{2}
\]

Define its Möbius increment sequence

\[
g:=\mu*b.
\tag{3}
\]

Assume in addition that

\[
\boxed{g(n)\ge0\qquad(n\ge1).}
\tag{4}
\]

By the exact inversion behind FD-225,

\[
(\mathscr A b)(m)=\sum_{n\le m}g(n),
\tag{5}
\]

so (4) is exactly the condition that the divisor response is nondecreasing on the integer grid.

Let

\[
Y_j=(\mathscr A b)(2^j),
\qquad
r_j=(1,4,4,1,4,4,\ldots),
\tag{6}
\]

and suppose that for one finite `B`,

\[
\boxed{
|(E-I)^{r_j}Y_j|\le B
\qquad(j\ge0).
}
\tag{7}
\]

Then there is an absolute constant `A` such that

\[
\boxed{
(\mathscr A b)(m)
=\sum_{n\le m}g(n)
\le A\bigl(C+B\log(2m)\bigr),
}
\tag{8}
\]

\[
\boxed{
b_n\le A\bigl(C+B\log(2n)\bigr),}
\tag{9}
\]

and, more importantly,

\[
\boxed{
\sum_{n\le x}b_n\le A(C+B)x.
}
\tag{10}
\]

Consequently, on every dyadic band `B_k=[2^k,2^(k+1))`,

\[
\boxed{
\frac{\sum_{n\in B_k}b_n}
     {\sum_{n\in B_k}n}
\ll
\frac{C+B}{2^k}.
}
\tag{11}
\]

Thus the relative nonnegative capacity decays at the **inverse-linear** rate `x^(-1)`, rather than merely at the small fixed power supplied by the general FD-257 argument.

The aggregate exponent in (11) is sharp inside this subclass. The constant cushion `b_n=1` has `g=epsilon`, exact constant response `\mathscr A b=1`, zero switched rows, and dyadic mass `asymp x`; hence its relative capacity is `asymp1/x`. The pointwise logarithm in (9) is also sharp in order: taking

\[
g(n)=\mathbf1_{\{1,2,4,8,\ldots\}}(n)
\tag{12}
\]

gives

\[
b(n)=(\mathbf1*g)(n)=v_2(n)+1,
\tag{13}
\]

while `Y_j=j+1`, so every order-one scheduled row equals `1` and every order-four scheduled row equals `0`.

For the scale-adapted reservoirs of FD-226, (11) has a direct interpretation. After normalizing by

\[
L_N=\frac{N}{D\log N},
\tag{14}
\]

a positive cushion whose Möbius increments are nonnegative and whose switched contribution stays bounded can use only `O(L_N x)` aggregate occupancy in a divisor band of scale `x`, while the available reservoir capacity there is `asymp L_Nx^2`. It therefore cannot exploit a polynomial fraction of the growing `d`-dependent capacity. Any positive cushion that hopes to beat the common-cushion geometry by a power of `D` must leave this monotone-response cone and develop sign changes in `mu*b`.

This does not say that every physical nonnegative occupancy satisfies (4). It does not. The extra sign condition is load-bearing, and the remaining frontier is precisely the genuinely signed Möbius-increment case.

## 1. The divisor response is the cumulative Möbius transform

Expanding the Mertens kernel in (1), exactly as in FD-225,

\[
\begin{aligned}
(\mathscr A b)(m)
&=
\sum_{d\le m}b_d
\sum_{a\le m/d}\mu(a)\\
&=
\sum_{n\le m}(b*\mu)(n).
\end{aligned}
\tag{15}
\]

Since Dirichlet convolution is commutative, `b*mu=g`, proving (5). Put

\[
G(m):=\sum_{n\le m}g(n)=(\mathscr A b)(m).
\tag{16}
\]

Under (4), `G` is nonnegative and nondecreasing.

Conversely, because `1*mu=epsilon`,

\[
\boxed{b=\mathbf1*g.}
\tag{17}
\]

Thus the additional hypothesis has a transparent source-side meaning: the positive cushion itself is a divisor sum of nonnegative response increments.

This class contains the constant cushion used by FD-225, but it is much larger. The theorem below shows that bounded switched rows nevertheless prevent it from acquiring polynomially growing cellwise slack.

## 2. Positivity turns the switched stencil into a local bound on every dyadic increment

Define the nonnegative dyadic increments

\[
x_j:=Y_{j+1}-Y_j\ge0.
\tag{18}
\]

At every scheduler index `j=3n`, the row has order one. Hence (7) gives directly

\[
\boxed{0\le x_{3n}\le B.}
\tag{19}
\]

The order-four rows control the two increments between consecutive order-one rows. Since

\[
(E-I)^4Y_j
=x_{j+3}-3x_{j+2}+3x_{j+1}-x_j,
\tag{20}
\]

fix `n>=1` and abbreviate

\[
p=x_{3n-1},\quad
q=x_{3n},\quad
a=x_{3n+1},\quad
b=x_{3n+2},\quad
c=x_{3n+3},\quad
d=x_{3n+4}.
\tag{21}
\]

All six quantities are nonnegative, while (19) gives `q,c<=B`.

The order-four row at `j=3n-1` gives

\[
|b-3a+3q-p|\le B.
\tag{22}
\]

Using `p>=0` and `q<=B`,

\[
\boxed{b\ge3a-4B.}
\tag{23}
\]

The order-four row at `j=3n+1` gives

\[
|d-3c+3b-a|\le B.
\tag{24}
\]

Using `d>=0` and `c<=B`, its upper half yields

\[
3b\le a+3c+B-d\le a+4B,
\]
so

\[
\boxed{b\le\frac a3+\frac{4B}{3}.}
\tag{25}
\]

Combining (23) and (25),

\[
3a-4B
\le
\frac a3+\frac{4B}{3},
\]
which gives

\[
\boxed{a\le2B.}
\tag{26}
\]

Substituting this back into (25) gives

\[
\boxed{b\le2B.}
\tag{27}
\]

Therefore every dyadic increment after the finite initial segment satisfies

\[
\boxed{x_j\le2B\qquad(j\ge3).}
\tag{28}
\]

This is the key gain over FD-257. There, `mu*b` may change sign, so the response can oscillate and only normalized stability plus the positive Mertens-tail inequality are available. Under (4), every dyadic response increment is itself nonnegative, and the two neighboring fourth-order stencils trap the otherwise-unobserved phases between the bounded order-one phases.

## 3. The response grows only logarithmically

The coefficient envelope gives a uniform bound on the finite initial response. Using only `|M(q)|<=q`,

\[
\begin{aligned}
0\le Y_3
&=|(\mathscr A b)(8)|\\
&\le
\sum_{d\le8}Cd
\left|M\!\left(\left\lfloor\frac8d\right\rfloor\right)\right|\\
&\le
\sum_{d\le8}Cd\frac8d
\le64C.
\end{aligned}
\tag{29}
\]

Equations (28)--(29) give, for `j>=3`,

\[
Y_j
\le64C+2B(j-3).
\tag{30}
\]

For an arbitrary integer `m>=8`, choose `j=ceil(log_2 m)`. Monotonicity gives

\[
G(m)\le G(2^j)=Y_j,
\]
so

\[
\boxed{
G(m)\ll C+B\log(2m).
}
\tag{31}
\]

This proves (8).

Since `b=1*g` and `g>=0`,

\[
b_n
=
\sum_{d\mid n}g(d)
\le
\sum_{d\le n}g(d)
=G(n),
\tag{32}
\]

which proves the pointwise logarithmic bound (9).

The logarithm is real rather than an artifact of the proof. For the example (12), `G(2^j)=j+1` and `b(2^j)=j+1`, while the switched rows remain bounded exactly as stated above.

## 4. Harmonic summation improves logarithmic pointwise slack to linear aggregate mass

The aggregate estimate is stronger than summing (9) naively. By Abel summation and the monotonicity of `G`,

\[
\begin{aligned}
\sum_{d\le x}\frac{g(d)}d
&=
\frac{G(x)}x
+
\sum_{d<x}G(d)
\left(\frac1d-\frac1{d+1}\right).
\end{aligned}
\tag{33}
\]

Equation (31) and the convergence of

\[
\sum_{d\ge1}\frac{1+\log(2d)}{d^2}
\]
therefore give the uniform bound

\[
\boxed{
\sum_{d\le x}\frac{g(d)}d
\ll C+B.
}
\tag{34}
\]

Now sum the divisor representation (17):

\[
\begin{aligned}
\sum_{n\le x}b_n
&=
\sum_{d\le x}g(d)
\left\lfloor\frac xd\right\rfloor\\
&\le
x\sum_{d\le x}\frac{g(d)}d\\
&\ll(C+B)x.
\end{aligned}
\tag{35}
\]

This proves (10), and (11) follows because

\[
\sum_{2^k\le n<2^{k+1}}n\asymp4^k.
\tag{36}
\]

The exponent `1` in (11) cannot be improved uniformly in this class: `b_n=1` has numerator `asymp2^k` and denominator `asymp4^k`.

## 5. Finite growing blocks inherit the same interior estimate

The proof is local in the switched row window. Suppose `b` is given only through a finite divisor depth `D`, define `g=mu*b` on `n<=D`, assume

\[
0\le b_n\le Cn,
\qquad
g(n)\ge0
\quad(n\le D),
\tag{37}
\]

and impose (7) on every scheduled row whose complete stencil lies inside the depth.

To bound an increment `x_i` in phases `1` or `2`, equations (22)--(25) use no sample beyond dyadic exponent `i+3`. Therefore, for a band

\[
B_k=[2^k,2^{k+1})
\]
with

\[
\boxed{2^{k+3}\le D,}
\tag{38}
\]

the complete argument above applies to all cumulative values needed in the Abel sum up to the top of the band. With the same absolute constants,

\[
\boxed{
\sum_{n\in B_k}b_n
\ll(C+B)2^k.
}
\tag{39}
\]

Thus the inverse-linear relative-capacity depletion is uniform on every fixed-stencil interior of a growing block. No limiting compactness argument is needed.

## 6. Consequence for the FD-226 Mertens-cushion bottleneck

In the scale-adapted exact floor cells of FD-226, the natural occupancy scale is

\[
L_N=\frac{N}{D\log N},
\qquad
|I_d^*\cap\mathbb P|\asymp L_Nd
\tag{40}
\]

throughout the certified prime-resolution regime.

Let `a_{N,d}` be a nonnegative physical cushion and normalize

\[
b_{N,d}:=\frac{a_{N,d}}{L_N}.
\tag{41}
\]

The capacity bound gives `b_{N,d}<=Cd` for a fixed `C`. If, in addition,

\[
(\mu*b_N)(d)\ge0
\tag{42}
\]

through the relevant depth and the cushion's actual switched contribution is `O(L_N)` or smaller, then its normalized rows satisfy (7) with bounded `B`. Equations (9) and (39) yield

\[
\boxed{
a_{N,d}\ll L_N\bigl(1+\log d\bigr),}
\tag{43}
\]

and, for every interior dyadic band of scale `x`,

\[
\boxed{
\sum_{x\le d<2x}a_{N,d}
\ll L_Nx.
}
\tag{44}
\]

The available capacity in that same band is `asymp L_Nx^2`. Hence a monotone-response cushion can occupy only an `O(1/x)` aggregate fraction. It cannot provide slack of size `L_Nd^gamma` for any fixed `gamma>0` throughout large divisor scales.

This also shows why this subclass cannot remove the quadratic `D`-loss diagnosed in FD-226 by a power of `D` using the currently available uniform Mertens correction envelope. FD-236 gives, schematically,

\[
|\widetilde c_N(d)|
\ll
N\log N\,e^{-\eta\Phi(N)}d\tau(d).
\tag{45}
\]

At `d=D`, the largest pointwise slack permitted by (43) is only

\[
O\!\left(\frac{N\log D}{D\log N}\right).
\tag{46}
\]

Therefore a proof that dominates (45) uniformly by such a cushion would still need, up to fixed constants,

\[
\boxed{
D^2T(D)(\log N)^2e^{-\eta\Phi(N)}
\ll\log D,
}
\tag{47}
\]

with `T(D)=max_(n<=D)tau(n)`. Compared with FD-226's common-cushion sufficient condition, this buys at most a logarithm, not a power of `D`.

Equation (47) is a statement about what the present uniform correction bound can certify, not an intrinsic lower bound on the actual negative part of the Mertens repair. The repair may be much smaller on particular cells. The exact structural conclusion is (43)--(44): **within the nonnegative-Möbius-increment cone, bounded switched response cannot exploit polynomially growing reservoir slack.**

## 7. Prior-art boundary and failure modes

A targeted prior-art audit found the expected classical Möbius-inversion/divisor-sum identities and generic finite-difference stability literature, but no result matching the repository-specific statement above: the period-three `(1,4,4)` Farey switched schedule, combined with a nonnegative Dirichlet-Möbius increment cone, forcing the sharp aggregate `O(x)` divisor-cushion mass bound.

No external theorem is load-bearing. Equations (15), (17) and (33) are elementary Möbius inversion and Abel summation; the decisive local estimate (22)--(28) is proved directly from the exact switched stencil. No new source anchor is therefore required in `SOURCES.md`.

The sign condition (4) is essential. A nonnegative coefficient profile `b` need not have `mu*b>=0`; sign changes in `g` allow the divisor response itself to oscillate, and then the local increment argument fails. FD-257 remains the applicable theorem for that larger cone. Consequently this finding does not settle the full physical positivity problem and does not improve any Mertens estimate.

The result instead removes a broad natural escape from the FD-226 bottleneck. Constant cushions, positive combinations of divisor atoms, staircase response targets with nonnegative increments, and every other cushion in the cone `b=1*g`, `g>=0`, are all aggregate-linear under bounded switched rows. A future positive cushion that genuinely exploits the larger scale-adapted cells must use **signed Möbius increments**, equivalently a nonmonotone divisor response, even though its occupancies themselves remain nonnegative.

**Verdict.** The weak polynomial depletion of FD-257 is needed only because arbitrary positive occupancies may have a signed Möbius transform. If the transform is nonnegative, the switched schedule is far more coercive: every late dyadic response increment is uniformly bounded, the cumulative response grows only logarithmically, the coefficient mass up to `x` is only `O(x)`, and the relative dyadic capacity decays at the sharp rate `1/x`. This monotone-response subclass cannot remove the FD-226 quadratic Mertens-cushion pressure by a power of the divisor depth.