# NB-020 — early-shell Möbius inversion forces an inverse-distance coefficient core

**Status:** `EXACT-DERIVED + EARLY-SHELL-MOBIUS-INVERSION + TARGET-APPROXIMATION-RIGIDITY + COEFFICIENT-BUDGET-LOWER-BOUND + NEGATIVE/MIXING-SCALE-BOUNDARY`. `NB-019` replaces the exponential lcm mixing scale by the intrinsic coefficient budget

\[
\mathfrak A_N:=\sum_{j=2}^{N}j|a_{N,j}|,
\qquad
P_{V_N}e=\sum_{j=2}^{N}a_{N,j}g_j,
\]

and shows that `\mathfrak A_N/m` controls the consecutive-shell mixing error of the canonical residual. The live question is therefore whether the target-selected coefficients make `\mathfrak A_N` small enough, on a growing scale, to enter the diagonal `NB-015` visibility regime.

There is an exact source-side lower boundary on how small this budget can be. Let

\[
r_N=e-P_{V_N}e,
\qquad d_N=\|r_N\|,
\]

and write `r_{N,n}` for the value of `r_N` on Bagchi's harmonic shell

\[
I_n=\left(\frac1{n+1},\frac1n\right].
\]

Set `r_{N,0}:=1`. Then every canonical projection coefficient is recovered **triangularly from the first `n` residual shell differences**:

\[
\boxed{
 a_{N,n}
 =\sum_{d\mid n}\mu\!\left(\frac nd\right)
   \bigl(r_{N,d}-r_{N,d-1}\bigr),
 \qquad 2\le n\le N.
}
\tag{1}
\]

Consequently

\[
\boxed{
 |a_{N,n}+\mu(n)|
 \le 2d_N\sigma(n),
 \qquad 2\le n\le N,
}
\tag{2}
\]

where `\sigma(n)=\sum_{d\mid n}d`. Thus a small Nyman residual forces a growing low-index coefficient core to lock onto the Möbius pattern `-\mu(n)` in the real-space Bagchi sign convention. In particular there are absolute constants `c,C>0` such that, whenever
`\min(N,d_N^{-1})\ge C`,

\[
\boxed{
 \mathfrak A_N
 \ge c\,\min\{N^2,d_N^{-2}\}.
}
\tag{3}
\]

The estimate is not specific to least squares until the notation is specialized: (1)--(2) hold for **any** finite combination `v=\sum_{j=2}^N a_jg_j` with residual `r=e-v`, replacing `d_N` by `\|r\|`. What is target-specific is that the canonical best residual supplies the coefficient budget used by `NB-019` and the distance scale used throughout the line.

Equation (3) changes the interpretation of the coefficient-discrepancy route. Along any subsequence with `d_N\to0`, a sufficient mixing condition of the form

\[
\frac{\mathfrak A_N}{M_N}\longrightarrow0
\]

necessarily requires

\[
\boxed{
 M_N d_N^2\longrightarrow\infty
}
\tag{4}
\]

once the classical Burnol floor is used to put `d_N^{-1}\ll\sqrt{\log N}\ll N`. Hence the `NB-019` absolute-coefficient majorant cannot make the shell-mixing error vanish **before** the inverse-distance scale. This does not kill the route: `NB-015` permits much deeper multiplicative windows. It does show that an eventual upper bound on `\mathfrak A_N` cannot win by making the coefficient budget anomalously tiny; a Möbius-sized core is forced by the target itself.

## 1. The first `N` shell differences form a triangular divisor system

Bagchi's exact shell formula is

\[
g_j|_{I_n}=\left\{\frac nj\right\}.
\tag{5}
\]

For the finite approximation

\[
v_N:=P_{V_N}e
=\sum_{j=2}^{N}a_{N,j}g_j,
\]

write `v_{N,n}` for its value on `I_n`. The discrete derivative of one generator is

\[
\left\{\frac nj\right\}
-\left\{\frac{n-1}{j}\right\}
=\frac1j-\mathbf 1_{j\mid n}.
\tag{6}
\]

Therefore

\[
v_{N,n}-v_{N,n-1}
=A_N^{(0)}-
\sum_{\substack{j\mid n\\2\le j\le N}}a_{N,j},
\qquad
A_N^{(0)}:=\sum_{j=2}^{N}\frac{a_{N,j}}j.
\tag{7}
\]

The constant in (7) is itself the first shell value:

\[
v_{N,1}=A_N^{(0)},
\tag{8}
\]

because `{1/j}=1/j`. Since `r_{N,n}=1-v_{N,n}` and we set `r_{N,0}=1` (equivalently `v_{N,0}=0`), equations (7)--(8) give for every `1\le n\le N`

\[
\boxed{
F_N(n):=
A_N^{(0)}+r_{N,n}-r_{N,n-1}
=
\sum_{\substack{j\mid n\\j\ge2}}a_{N,j}.
}
\tag{9}
\]

For `n=1` both sides are zero. For `n\le N`, no coefficient of index larger than `n` occurs in the divisor sum on the right. Thus the first `N` shell differences are a genuinely triangular observation system, despite the global conditioning issues of the Gram matrix.

Finite Möbius inversion of (9) yields, for `2\le n\le N`,

\[
a_{N,n}
=\sum_{d\mid n}\mu\!\left(\frac nd\right)F_N(d).
\tag{10}
\]

The constant `A_N^{(0)}` disappears because

\[
\sum_{d\mid n}\mu(n/d)=0
\qquad(n>1),
\]

leaving exactly (1). No normal equation, Gram inversion, lcm period, RH assumption, or asymptotic estimate is used.

This also explains the Möbius sign without appealing to a limiting Dirichlet polynomial. If a finite approximation were locally exact on the first `n` shells, then `r_{N,1}=\cdots=r_{N,n}=0` while `r_{N,0}=1`, and (1) would force

\[
a_{N,n}=-\mu(n).
\tag{11}
\]

The appearance of Möbius coefficients is therefore already encoded in the finite shell incidence geometry.

## 2. Hilbert error gives a quantitative local Möbius-locking estimate

The residual is constant on every harmonic shell and

\[
\|r_N\|^2
=\sum_{k\ge1}
\frac{|r_{N,k}|^2}{k(k+1)}.
\tag{12}
\]

Hence each shell value obeys the exact pointwise consequence

\[
|r_{N,k}|
\le d_N\sqrt{k(k+1)}.
\tag{13}
\]

Separate the `d=1` term in (1). Since `r_{N,0}=1`,

\[
a_{N,n}+\mu(n)
=\mu(n)r_{N,1}
+
\sum_{\substack{d\mid n\\d\ge2}}
\mu\!\left(\frac nd\right)
\bigl(r_{N,d}-r_{N,d-1}\bigr).
\tag{14}
\]

For every `d\ge2`, concavity of the square root gives

\[
\sqrt{d(d+1)}+\sqrt{d(d-1)}<2d.
\tag{15}
\]

Using (13), `|\mu|\le1`, and `|r_{N,1}|\le\sqrt2d_N`, we obtain

\[
\begin{aligned}
|a_{N,n}+\mu(n)|
&\le
\sqrt2d_N
+2d_N\sum_{\substack{d\mid n\\d\ge2}}d\\
&=
d_N\bigl(\sqrt2+2\sigma(n)-2\bigr)\\
&\le 2d_N\sigma(n),
\end{aligned}
\tag{16}
\]

which proves (2).

Several useful readings are immediate. For each fixed `n`, `d_N\to0` forces `a_{N,n}\to-\mu(n)`. More generally the locking is uniform on any collection of indices satisfying `d_N\sigma(n)\to0`. This statement concerns the actual coefficient coordinates, not merely the value of a Dirichlet polynomial or a Gram Rayleigh quotient.

## 3. A positive weighted density of squarefree indices forces the budget floor

To turn (2) into an absolute-coefficient lower bound, only an elementary divisor-counting lemma is needed. There are absolute constants `C_0,c_0,x_0>0` such that for all `x\ge x_0`,

\[
\boxed{
\sum_{\substack{n\le x\\\mu(n)^2=1\\\sigma(n)\le C_0n}}n
\ge c_0x^2.
}
\tag{17}
\]

One can prove (17) without a prime number theorem. Every nonsquarefree integer is divisible by some square `m^2`, `m\ge2`, so

\[
\#\{n\le x:\mu(n)^2=1\}
\ge
\lfloor x\rfloor
-x\sum_{m=2}^{\infty}\frac1{m^2}
=
\left(2-\zeta(2)\right)x+O(1).
\tag{18}
\]

Thus the weighted sum of all squarefree integers up to `x` is `\gg x^2`: among any fixed positive proportion of `1,\ldots,\lfloor x\rfloor`, the smallest possible weighted sum already has quadratic order.

On the other hand,

\[
\sum_{n\le x}\sigma(n)
=
\sum_{d\le x}d\left\lfloor\frac xd\right\rfloor
\le x^2.
\tag{19}
\]

Therefore the weighted contribution of indices with `\sigma(n)>C_0n` is at most `x^2/C_0`. Choosing `C_0` sufficiently large leaves a fixed positive fraction of the squarefree weighted mass and proves (17).

Now choose a sufficiently small absolute `c_*>0` and set

\[
x_N=
\left\lfloor
\min\left\{N,\frac{c_*}{d_N}\right\}
\right\rfloor,
\tag{20}
\]

with `c_*` small enough that `2C_0c_*\le1/2`. For every index counted by (17) with `n\le x_N`, equation (2) gives

\[
|a_{N,n}+\mu(n)|\le\frac12.
\tag{21}
\]

Because those indices are squarefree, `|\mu(n)|=1`, hence

\[
|a_{N,n}|\ge\frac12.
\tag{22}
\]

It follows from (17) that

\[
\mathfrak A_N
\ge
\frac12
\sum_{\substack{n\le x_N\\\mu(n)^2=1\\\sigma(n)\le C_0n}}n
\gg x_N^2
\gg \min\{N^2,d_N^{-2}\},
\tag{23}
\]

once the minimum is larger than an absolute constant. This is (3).

The same argument applies to any finite coefficient vector whose residual has norm `d`: a genuinely accurate approximation cannot make all low coefficients simultaneously small, because a positive weighted density of them is forced to lie a fixed distance from zero near the Möbius values.

## 4. Burnol places the coefficient-core boundary inside the finite section

For the best Nyman residual, Burnol's zero-sensitive lower bound, already used in `NB-009`--`NB-011`, gives an absolute `c_B>0` such that for all sufficiently large `N`,

\[
d_N^2\ge\frac{c_B}{\log N}.
\tag{24}
\]

Consequently

\[
d_N^{-1}\ll\sqrt{\log N}\ll N,
\tag{25}
\]

so the `d_N^{-1}` branch of (3) is the relevant one whenever `d_N` is small enough for the asymptotic coefficient core to be nontrivial. Thus

\[
\boxed{
\mathfrak A_N\gg d_N^{-2}
}
\tag{26}
\]

in that regime.

Now recall the sufficient consecutive-mixing estimate of `NB-019`,

\[
\|Q_mr_N-\mu_Ne\|_\infty
\le\frac{\mathfrak A_N}{4m}.
\tag{27}
\]

If one tries to make the right side tend to zero along scales `m=M_N`, (26) implies the necessary scale separation

\[
\frac{\mathfrak A_N}{M_N}\to0
\quad\Longrightarrow\quad
M_Nd_N^2\to\infty,
\tag{28}
\]

which is (4).

This puts a clean lower boundary under the `NB-019` coefficient-majorant mechanism. The first parity normal equation in `NB-009`--`NB-010` already forces source-visible structure at the inverse-distance scale `K\asymp d_N^{-2}`. The absolute-coefficient mixing certificate cannot asymptotically settle **earlier** than that scale; to make its error vanish it must go strictly deeper by a diverging factor.

This is a method boundary, not a contradiction. The `NB-015` visibility architecture allows multiplicative depths much larger than `d_N^{-2}`, and (26) gives no useful upper bound on `\mathfrak A_N`. In particular it does not rule out a subquadratic estimate `\mathfrak A_N=o(N^2)`, which would still place mixing inside the largest diagonal windows contemplated after `NB-019`.

## 5. Prior-art boundary and adversarial controls

The **Möbius role itself is classical**. Báez-Duarte's natural approximation uses Möbius coefficients, and the strengthened criterion already explains why the arithmetic inverse of `\zeta` enters the discrete family. Bettin--Conrey--Farmer later use the mollified Dirichlet polynomial

\[
\sum_{n\le N}
\left(1-\frac{\log n}{\log N}\right)
\frac{\mu(n)}{n^s}
\]

for the conditional optimal asymptotic. Those sources are already anchored in `SOURCES.md`; this finding makes no novelty claim for the appearance of `\mu` in Nyman--Beurling approximants.

The narrower delta is finite and target-relative: the coefficient `a_{N,n}` of an **arbitrary finite approximation** is exactly the Möbius transform of its own first `n` shell differences, and the Hilbert residual norm therefore gives the explicit local stability estimate (2). A targeted check of Báez-Duarte's strengthening, Bagchi's semigroup/shell presentation, Bettin--Conrey--Farmer's Möbius mollifier, Ehm's finite Gram analysis, and searches for finite optimal-coefficient/Möbius inversion formulas did not locate (1), (2), or the budget consequence (3) in this residual-coordinate form. Search absence is not used as proof of novelty, and no new specialized external estimate is load-bearing, so `SOURCES.md` is unchanged.

Several falsification boundaries are essential. First, (2) becomes weak for indices with large `\sigma(n)` and does **not** say that the whole vector `a_N` is close to `-\mu` up to `N`. Second, (3) is a lower bound on `\mathfrak A_N`, whereas the live mixing problem needs an upper bound or a cancellation-sensitive replacement for that absolute budget. Third, (28) constrains only the sufficient `NB-019` majorant; it is not a lower bound on the true mixing time of `Q_mr_N`, which may benefit from cancellations invisible to `\mathfrak A_N`. Fourth, if the limiting distance is positive, the inverse-distance core need not grow and no contradiction follows. Finally, the real-space coefficients here approach `-\mu(n)` because of Bagchi's generator sign convention; Hardy-space Dirichlet-polynomial conventions may display the opposite sign.

## 6. Research consequence

`NB-019` shows that lcm periodicity is not the intrinsic finite mixing scale; the correct first replacement is a source-dependent coefficient/discrepancy budget. `NB-020` now shows that this budget has an arithmetic floor dictated by the target: early shell incidence Möbius-inverts the approximation error, forcing a positive weighted density of low coefficients to retain Möbius size until the shell error itself becomes too large to resolve them.

The live upper-bound problem therefore has a sharper form. It is not enough to hope that best approximation makes `\sum j|a_{N,j}|` globally tiny. Any successful estimate must accommodate an unavoidable low-index Möbius core of size at least `\asymp d_N^{-2}` while controlling the much larger high-index tail, or replace the absolute coefficient budget by a cancellation-sensitive discrepancy that can exploit the signs/phases of those coefficients. This keeps the `NB-015` scale-coupled visibility route open, but removes one overly optimistic way of making the `NB-019` mixing threshold small.