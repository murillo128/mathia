# PC-411 — meet-regularized descendant Gram restores only a universal zeta rectangle

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-REFORMULATION` + `DECISIVE-NEGATIVE` for the simplest canonical escape from the join-only obstruction of PC-410: a Mellin-diagonal descendant Gram coupling weighted simultaneously by the least common refinement and the greatest common ancestor. Adding the meet does restore every fresh-prime direction that PC-410 cancels, but the restored all-prime divisor is an explicit universal rectangle of shifted Riemann zeta factors, multiplied by an Euler product already absolutely convergent for `Re(s)>1/2` and finite corrections at primes dividing the parent shell. The same factorization occurs for an arbitrary matched base profile propagated by the universal PC-405 descendant semigroup. Thus this meet repair changes the information law, but not in a Prime-Circle-specific way.

This does **not** classify arbitrary functions of both `(m,k)` and `[m,k]`, non-Mellin-diagonal kernels, source-derived angular/chord/old-new cross-level interactions, nonlinear state-space changes, or conductor-growing interaction complexity. Those remain outside the result.

## 1. The canonical meet-plus-join test

PC-410 proves that every Mellin-diagonal coupling whose two descendant labels enter only through their join `[m,k]` deletes all primes not already dividing the parent shell. The most economical way to break that hypothesis without importing a new geometric object is to let the kernel also see the divisibility-lattice meet `(m,k)`.

For a fixed parent shell `n>1`, keep the PC-405/PC-407 Mellin descendant multipliers

\[
\widehat{h_{nm}}(t)=c_{n,m}(t)\widehat h_n(t),
\]

with prime-power factors

\[
c_{n,p^a}(t)=
\begin{cases}
1,&a=0,\\[1mm]
p^{iat},&a\ge1,\ p\mid n,\\[1mm]
p^{i(a-1)t}(p^{it}-1),&a\ge1,\ p\nmid n.
\end{cases}
\tag{1}
\]

Fix real `t`, real `u>0`, and initially `Re(s)>1`. Define the two-index symbol

\[
\boxed{
K_n(s,u;t)
:=
\sum_{m,k\ge1}
\frac{c_{n,m}(t)\overline{c_{n,k}(t)}}
{[m,k]^s(m,k)^u}.
}
\tag{2}
\]

The series is absolutely convergent in this native half-plane. At a fresh prime its local excess is `O(p^{-Re(s)})`, while the positive exponent tails are geometric in `p^{-s}` and `p^{-(s+u)}`. Only finitely many repeated parent primes require separate factors.

The kernel itself is not new arithmetic technology. Since `(m,k)[m,k]=mk`,

\[
\frac1{[m,k]^s(m,k)^u}
=
\frac{(m,k)^{s-u}}{m^sk^s},
\tag{3}
\]

so it is a diagonally weighted power-GCD / meet-join kernel. GCD/LCM matrices, meet/join matrices and their incidence factorizations are classical territory; the Prime-Circle question is only what happens when this kernel is paired with the source-forced fresh-prime difference cocycle (1).

## 2. Exact fresh-prime local factor

Fix a fresh prime `p\nmid n` and write

\[
A=p^{it},\qquad x=p^{-s},\qquad y=p^{-u},
\qquad q=|A-1|^2=2-A-A^{-1}.
\tag{4}
\]

The local descendant sequence is

\[
e_0=1,
\qquad
e_a=A^a-A^{a-1}=(A-1)A^{a-1}\quad(a\ge1).
\tag{5}
\]

The fresh local factor of (2) is therefore

\[
F_p(s,u;t)
=
\sum_{a,b\ge0}
e_a\overline{e_b}\,
 x^{\max(a,b)}y^{\min(a,b)}.
\tag{6}
\]

Splitting (6) into the diagonal, `a>b`, and `b>a` geometric sums gives the exact rational identity

\[
\boxed{
F_p(s,u;t)
=
\frac{
(1-x)^2(1-xy)-q\,x(x-y)
}
{(1-Ax)(1-A^{-1}x)(1-xy)}.
}
\tag{7}
\]

The join-only theorem PC-410 is recovered without a limit. Setting `u=0`, hence `y=1`, reduces the numerator to

\[
(1-x)\bigl((1-x)^2+qx\bigr)
=(1-x)(1-Ax)(1-A^{-1}x),
\]

so

\[
\boxed{F_p(s,0;t)=1.}
\tag{8}
\]

For every `u>0`, however, the cancellation is broken. Expanding at a large fresh prime gives

\[
F_p(s,u;t)
=1-q\,p^{-s}(1-p^{-u})+O(p^{-2\operatorname{Re}s}),
\tag{9}
\]

so the meet really does restore a first-order fresh-prime signal. The question is whether that restored signal is source-specific.

## 3. The restored signal factors as a universal zeta rectangle

Introduce the local factor

\[
R_p(s,t)
:=
\frac{(1-p^{-s})^2}
{(1-p^{-(s-it)})(1-p^{-(s+it)})}.
\tag{10}
\]

Its Euler product is the classical shifted-zeta ratio

\[
R(s,t)
=
\prod_p R_p(s,t)
=
\frac{\zeta(s-it)\zeta(s+it)}{\zeta(s)^2}
\qquad(\Re(s)>1).
\tag{11}
\]

Direct algebra in (7) yields the sharper factorization

\[
\boxed{
F_p(s,u;t)
=
\frac{R_p(s,t)}{R_p(s+u,t)}\,H_p(s,u;t),
}
\tag{12}
\]

where

\[
\boxed{
H_p(s,u;t)
=
1-
\frac{
q\,p^{-2s}(1-p^{-u})^2
}
{(1-p^{-s})^2
 (1-p^{-(s+u-it)})(1-p^{-(s+u+it)})}.
}
\tag{13}
\]

For fixed real `t` and `u>0`,

\[
H_p(s,u;t)=1+O_{t,u}(p^{-2\operatorname{Re}s})
\tag{14}
\]

uniformly on compacta away from the displayed local denominators. Hence

\[
H(s,u;t):=\prod_p H_p(s,u;t)
\tag{15}
\]

converges normally and absolutely for `Re(s)>1/2` on such compacta. No zero-free claim is made for `H`; the point is only that the first-order all-prime divisor has already been extracted completely.

Multiplying (12) over the fresh primes exposes the universal zeta factor

\[
\boxed{
Q(s,u;t)
:=
\frac{R(s,t)}{R(s+u,t)}
=
\frac{
\zeta(s-it)\zeta(s+it)\zeta(s+u)^2
}
{
\zeta(s)^2\zeta(s+u-it)\zeta(s+u+it)
}.
}
\tag{16}
\]

This is exactly a multiplicative finite difference in the real scale variable `s`: the meet penalty compares the same universal shifted-zeta ratio at `s` and `s+u`. At `u=0` the rectangle collapses to `1`, matching the exact PC-410 cancellation.

Equation (16) is an explicit factorization of the native series in `Re(s)>1`. Using the right-hand side outside that domain is meromorphic continuation of the factorization; zeros and poles there must not be reinterpreted automatically as spectrum of the original absolutely convergent Gram sum.

## 4. Parent primes contribute only a finite correction

If `p\mid n`, the local descendants contain no fresh-prime difference: `e_a=A^a`. The corresponding meet-plus-join factor is

\[
\boxed{
G_p(s,u;t)
=
\sum_{a,b\ge0}
A^{a-b}x^{\max(a,b)}y^{\min(a,b)}
=
\frac{1-x^2}
{(1-Ax)(1-A^{-1}x)(1-xy)}.
}
\tag{17}
\]

Relative to the universal fresh factor (7), the parent-prime correction is therefore

\[
\boxed{
C_p(s,u;t)
:=\frac{G_p}{F_p}
=
\frac{1-x^2}
{(1-x)^2(1-xy)-q\,x(x-y)}.
}
\tag{18}
\]

Combining (12)--(18) gives, in the native domain `Re(s)>1`,

\[
\boxed{
K_n(s,u;t)
=
Q(s,u;t)\,H(s,u;t)
\prod_{p\mid n}C_p(s,u;t).
}
\tag{19}
\]

All parent dependence is a finite Euler correction. The infinite all-prime part is the same zeta rectangle and the same absolutely convergent remainder for every parent.

As another exact consistency check, setting `u=0` in (17) gives

\[
G_p(s,0;t)
=
\frac{1+p^{-s}}
{(1-p^{-(s-it)})(1-p^{-(s+it)})},
\]

which is precisely the repeated-parent local factor of PC-409/PC-410.

## 5. Matched arbitrary-profile control

The decisive source-specificity test does not use cyclotomic geometry. Let `h` be any Mellin-tame profile in the PC-407 Hilbert space and generate synthetic descendants with the same universal operators `C_{n,m}` from PC-405. Weight their pairings by the same meet-plus-join kernel (2). Mellin-Plancherel gives an integrand

\[
|\widehat h(t)|^2K_n(s,u;t),
\tag{20}
\]

with exactly the same factorization (19).

Thus the zeta rectangle (16), the fresh-prime restoration, the correction Euler product (15), and the finite parent factors are all reproduced by a matched nonarithmetic base profile. The actual Prime-Circle source enters only through its already-known one-shell spectral density `|\widehat h_n(t)|^2`.

This is the same identifiability failure diagnosed in PC-406--PC-410 in a genuinely changed kernel class. The meet term escapes the **algebraic cancellation** of join-only kernels, but the information it restores is generated by the universal descendant semigroup rather than by roots-of-unity geometry retained through the coupling.

## 6. Prior-art and novelty audit

No novelty is claimed for the meet/join kernel itself. Identity (3) places it directly in classical GCD/LCM matrix territory. The line's existing source anchors already include Aistleitner--Berkes--Seip on GCD sums and Poisson/dilated-function structure, while the meet/join matrix literature used in PC-410 treats GCD and LCM as the meet and join of the divisibility lattice and includes power-GCD and reciprocal-power-LCM families. A targeted audit against Korkee--Haukkanen's meet/join incidence-matrix theory and Mattila--Haukkanen's power GCD/LCM examples gives no basis for a historical novelty claim.

Nor is the zeta rectangle in (16) a new zeta mechanism. Its four shifted sides are forced by taking the quotient of the universal PC-408/PC-407 quadratic shifted-zeta ratio at two values of the conductor exponent. The project-local result is the exact interaction (7), (12), and (19): the most canonical meet regularization of the PC-410 join coupling does restore fresh primes, but classicalizes immediately to a finite-difference zeta package plus a more convergent Euler correction.

Nothing here supplies an intrinsic gamma factor, a new `s\leftrightarrow1-s` symmetry, or a critical-line selector. Any RH-sensitive zero/pole criterion read directly from `Q` is therefore inherited universal zeta data, not evidence that the original Prime-Circle geometry produced a new spectral carrier.

## 7. Falsification and boundary of the obstruction

The exact local formulas make the claim easy to attack. For any fresh prime `p`, real `t`, `u>0`, and `Re(s)>1`, directly summing the truncated version of (6) over `0\le a,b\le R` must converge to (7). Setting `u=0` must give `1` identically for every cutoff after max-shell grouping, recovering PC-410. For a repeated parent prime the analogous truncation must converge to (17). Failure of any of these tests falsifies the factorization before any global Euler-product argument is used.

The negative result is intentionally not a theorem about every two-label descendant kernel. It closes the canonical one-parameter meet repair

\[
[m,k]^{-s}
\quad\longrightarrow\quad
[m,k]^{-s}(m,k)^{-u},
\qquad u>0,
\]

and more generally shows what this power meet deformation buys: a universal scale finite difference of the already-known descendant zeta ratio.

The live boundary is therefore sharper after PC-410. Merely adding the canonical GCD/meet weight is insufficient. A surviving distinct-descendant mechanism must use a genuinely more informative dependence on the two labels, mix Mellin frequencies, couple source-derived angular/chord/old-new data to refinement, alter the product/state space, or let interaction complexity grow with conductor in a way not reducible to this fixed Euler-local calculus. Those possibilities are not ruled out by PC-411.
