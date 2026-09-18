# NB-203 — Van der Corput hierarchy pushes positive Euler returns beyond every fixed polynomial shell scale

**Date:** 2026-09-18  
**Status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + SOURCE-ACQUISITION + POSITIVE-EULER + INTEGER-DISCREPANCY + NB-202-REFINEMENT`.

`NB-202` showed that integer-carrier discrepancy excludes an `o(1/X_a)` positive Euler-shell return through the second-derivative corridor `|t| \ll x_a^2/X_a^3`, and explicitly left that upper scale as a method boundary. That boundary is not intrinsic even at the generic integer-carrier level. The same Erdős--Turán reduction can be paired with the full classical van der Corput `k`-th derivative test, for each fixed `k`. The resulting frequency windows overlap, so the positive-return obstruction propagates through **every fixed polynomial power of the shell scale**.

Keep

\[
x_a=e^{r_0/a},\qquad X_a=\log x_a=\frac{r_0}{a},\qquad y_a=e^\Delta x_a,
\]

\[
D_a:=\sum_{x_a\le n<y_a}\Lambda(n)n^{-1-a},
\qquad
w_{n,a}:=\frac{\Lambda(n)n^{-1-a}}{D_a}\mathbf 1_{[x_a,y_a)}(n),
\]

and

\[
\mathcal A_a(t):=\sum_n w_{n,a}|e^{-it\log n}-1|.
\]

Then for every fixed integer `K>=3` there are constants `c_K,C_K>0`, depending only on `K,r_0,Delta`, such that for all sufficiently small `a`,

\[
\boxed{
X_a^2\le |t|\le c_K\frac{x_a^K}{X_a^{2^K-1}}
\quad\Longrightarrow\quad
\mathcal A_a(t)\ge \frac{C_K}{X_a}.
}
\tag{1}
\]

Consequently, for every fixed real `B>0` there is `c_B>0` such that, for all sufficiently small `a`,

\[
\boxed{
X_a^2\le |t|\le x_a^B
\quad\Longrightarrow\quad
\mathcal A_a(t)\ge \frac{c_B}{X_a}.
}
\tag{2}
\]

Thus any high-ordinate positive-return sequence with `|t_a|>=X_a^2` and

\[
X_a\mathcal A_a(t_a)\longrightarrow0
\]

must satisfy

\[
\boxed{
\frac{\log |t_a|}{X_a}\longrightarrow\infty.
}
\tag{3}
\]

Equivalently, such a return height is superpolynomial in the Mellin shell scale `x_a`. This is a qualitative superpolynomial statement: the argument fixes the derivative order before sending `a->0` and does **not** provide a uniform growing-`k` rate.

## 1. The full derivative test gives a fixed-`k` discrepancy window

Use the favorable integer carrier from `NB-202`, for a fixed small `q>0`,

\[
E_{a,t}(q)
:=
\left\{
n\in\mathbb Z\cap[x_a,y_a):
\operatorname{dist}(t\log n,2\pi\mathbb Z)\le\frac q{X_a}
\right\}.
\tag{4}
\]

Erdős--Turán with truncation parameter `H` gives

\[
\#E_{a,t}(q)
\ll_\Delta
\frac{q x_a}{X_a}
+\frac{x_a}{H}
+\sum_{1\le m\le H}\frac{|S_m(t)|}{m},
\tag{5}
\]

where

\[
S_m(t):=\sum_{x_a\le n<y_a}e^{imt\log n}.
\tag{6}
\]

Fix an integer `k>=3` and put

\[
D_k:=2^k-2,
\qquad
\delta_k:=2^{2-k}.
\tag{7}
\]

For the `e(u)=e^{2\pi iu}` phase

\[
f_m(u)=\frac{mt}{2\pi}\log u,
\]

its `k`-th derivative has one sign and, throughout the fixed multiplicative shell,

\[
|f_m^{(k)}(u)|
\asymp_{k,\Delta}
\frac{m|t|}{x_a^k}.
\tag{8}
\]

The classical van der Corput `k`-th derivative test (Theorem 3 in Olivier Robert's 2016 survey already anchored in `SOURCES.md`) therefore gives

\[
\boxed{
|S_m(t)|
\ll_{k,\Delta}
 x_a\left(\frac{m|t|}{x_a^k}\right)^{1/D_k}
+
 x_a^{1-\delta_k}
 \left(\frac{m|t|}{x_a^k}\right)^{-1/D_k}.
}
\tag{9}
\]

Here the factors depending on `(k-1)!` and on the fixed shell ratio are absorbed into the fixed-`k` constant. No uniformity in `k` is asserted.

Choose

\[
H=\left\lfloor\frac{X_a}{q}\right\rfloor.
\tag{10}
\]

Using

\[
\sum_{m\le H}m^{-1+1/D_k}\ll_k H^{1/D_k},
\qquad
\sum_{m\ge1}m^{-1-1/D_k}\ll_k1,
\]

(5) and (9) give

\[
\boxed{
\#E_{a,t}(q)
\ll_{k,\Delta}
\frac{q x_a}{X_a}
+
q^{-1/D_k}|t|^{1/D_k}x_a^{1-k/D_k}X_a^{1/D_k}
+
|t|^{-1/D_k}x_a^{1-\delta_k+k/D_k}.
}
\tag{11}
\]

For `k=2`, the analogous calculation is exactly the second-derivative estimate used by `NB-202`; (11) is the fixed-order hierarchy that was left unused there.

## 2. Euler normalization turns (11) into an overlapping frequency corridor

As in `NB-202`, the prime-number theorem gives `D_a\asymp1` on this fixed shell, while every normalized von-Mangoldt atom satisfies

\[
w_{n,a}\ll_{r_0,\Delta}\frac{X_a}{x_a}.
\tag{12}
\]

Multiplying (11) by this point-mass cap gives

\[
\boxed{
\sum_{n\in E_{a,t}(q)}w_{n,a}
\ll_{k,r_0,\Delta}
q
+
q^{-1/D_k}X_a^{1+1/D_k}
\left(\frac{|t|}{x_a^k}\right)^{1/D_k}
+
X_a x_a^{-\delta_k}
\left(\frac{x_a^k}{|t|}\right)^{1/D_k}.
}
\tag{13}
\]

Choose `q` first, sufficiently small. The second error in (13) is small provided

\[
|t|
\le
c_k\frac{x_a^k}{X_a^{D_k+1}},
\tag{14}
\]

and the third is small provided

\[
|t|
\ge
C_k X_a^{D_k}x_a^{k-\delta_kD_k}.
\tag{15}
\]

Since

\[
\delta_kD_k
=2^{2-k}(2^k-2)
=4-2^{3-k},
\]

(15) is

\[
|t|
\ge
C_k X_a^{2^k-2}
 x_a^{k-4+2^{3-k}}.
\tag{16}
\]

Inside the window (14)--(16), after changing the fixed constants, at most half of the normalized positive Euler mass can lie in the favorable phase cells. Every remaining atom has

\[
|e^{-it\log n}-1|
\ge
2\sin\frac{q}{2X_a}
\gg_q\frac1{X_a}.
\]

Positivity therefore yields

\[
\boxed{
C_k X_a^{2^k-2}x_a^{k-4+2^{3-k}}
\le |t|
\le c_k\frac{x_a^k}{X_a^{2^k-1}}
\quad\Longrightarrow\quad
\mathcal A_a(t)\gg_k\frac1{X_a}.
}
\tag{17}
\]

The right endpoint is the only part that will matter after the fixed-order windows are chained.

## 3. The derivative windows overlap and remove every fixed polynomial scale

For `k=3`, the lower edge in (17) is only `C_3X_a^6`, whereas `NB-202` already reaches `c x_a^2/X_a^3`. Hence the `k=3` window overlaps the `NB-202` corridor by an exponentially large margin and extends it to

\[
|t|\ll\frac{x_a^3}{X_a^7}.
\]

For every fixed `k>=4`, compare the upper edge supplied by order `k-1`,

\[
\frac{x_a^{k-1}}{X_a^{2^{k-1}-1}},
\]

with the lower edge (16) for order `k`. Their ratio is

\[
\frac{x_a^{3-2^{3-k}}}
{X_a^{3\cdot2^{k-1}-3}},
\tag{18}
\]

which tends to infinity as `a->0` for each fixed `k`. Thus there is eventually no gap between successive derivative orders. Induction from `NB-202` proves (1).

Now fix an arbitrary real `B>0`. Choose one fixed integer `K>B`. Since

\[
\frac{x_a^K/X_a^{2^K-1}}{x_a^B}
=\frac{x_a^{K-B}}{X_a^{2^K-1}}
\longrightarrow\infty,
\]

(1) contains the entire interval through `x_a^B` for sufficiently small `a`; this proves (2).

If (3) failed for a sequence satisfying `X_a A_a(t_a)->0`, some fixed `B` and a subsequence would have `|t_a|<=x_a^B`. Equation (2) would then give a fixed positive lower bound for `X_a A_a(t_a)`, a contradiction. This proves the superpolynomial conclusion.

For a physical block `[T_a,2T_a]`, if `T_a>=X_a^2` and some `t_a` in that block realizes

\[
X_a\mathcal A_a(t_a)\to0,
\]

then necessarily

\[
\boxed{
\frac{\log T_a}{X_a}\to\infty,
\qquad\text{equivalently}\qquad
a\log T_a\to\infty.
}
\tag{19}
\]

So no coupled width of the form `a~c/log T` with fixed `c>0` can support this positive-shell return. This remains a **source-acquisition condition**, not a lower bound for the optimal Nyman--Beurling distance.

## Stress tests and limits

The most important quantifier is that `k` is fixed before `a->0`. The constants in Robert's derivative estimate, and hence in (17), are allowed to depend on `k`. The passage from (1) to (3) is legitimate because a superpolynomial statement tests one fixed power `B` at a time. It would **not** be legitimate to choose `k=k(a)` in (17) and infer a specific bound such as `exp(cX_a log X_a)` without a separate theorem controlling the `k`-dependence of all constants.

Positivity remains load-bearing exactly as in `NB-202`: the carrier estimate only proves that a positive fraction of the source mass lies outside favorable phase cells, and positivity converts that escaped mass into chord defect. Signed or complex combinations can cancel across phase sectors and are not controlled here.

The high-ordinate hypothesis is also essential. There is of course an exact return at `t=0`, and this finding does not attempt to exclude microscopic returns below the established `X_a^2` corridor. Its content concerns the coupled high-height regime relevant to the current source-acquisition program.

Finally, the mechanism is still generic carrier geometry. No prime-specific distribution estimate enters beyond the facts already used in `NB-202`: the normalized source has total mass comparable to one and each von-Mangoldt atom is `O(X_a/x_a)`. Any positive measure on the same integer shell with that point-mass cap inherits the same fixed-polynomial obstruction. Thus the result does not claim new prime-distribution technology.

## Prior-art and novelty audit

The analytic input is classical. Olivier Robert, *On van der Corput's k-th derivative test for exponential sums*, Indagationes Mathematicae 27 (2016), 559--589, DOI `10.1016/j.indag.2015.11.009`, states the full fixed-`k` estimate used in (9) as Theorem 3 and discusses logarithmic phases in the classical zeta application. The same paper was already anchored in `SOURCES.md` for the second-derivative step of `NB-202`, so no new source dependency is introduced here. Erdős--Turán is likewise already anchored there.

A focused prior-art search around `t log n` discrepancy, logarithmic exponential sums, derivative tests, and lattice-point applications found the expected classical machinery but no source used here that states the normalized positive Euler-shell consequence (1)--(3). No novelty is claimed for the derivative hierarchy itself, for discrepancy of generic logarithmic phases, or for the observation that higher derivative estimates extend an exponential-sum range.

The line-local derived content is the coupling of the full fixed-order hierarchy to the `NB-202` Euler normalization, the exact overlap calculation (18), and the resulting conclusion that an `o(1/X_a)` positive Euler return must escape **every fixed polynomial shell height**. This materially removes the `x_a^2/X_a^3` scale as a candidate structural frontier.

## Consequence for the research frontier

`NB-202` left two possible positive-source continuations: improve the generic carrier discrepancy beyond the second-derivative window, or introduce genuinely von-Mangoldt occupancy. The first route is now qualitatively exhausted throughout all fixed polynomial heights by classical fixed-order derivative tests. Prime-specific occupancy is therefore not needed merely to pass from quadratic to cubic or any other fixed power.

The next positive-source frontier is genuinely non-polynomial. One option is to obtain derivative estimates with sufficiently explicit **uniform dependence on the derivative order** to allow `k` to grow with `a`; another is to exploit von-Mangoldt structure directly at superpolynomial Mellin heights. Any such claim must keep the fixed-`k` versus growing-`k` quantifier visible. The independent destination bridge—showing that successful Nyman approximation actually forces this positive Euler-shell acquisition condition—and the signed/complex synthesis problem remain open and unchanged.