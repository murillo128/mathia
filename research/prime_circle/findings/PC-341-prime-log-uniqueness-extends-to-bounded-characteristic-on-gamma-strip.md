# PC-341 — prime-log uniqueness extends exactly to bounded characteristic on the Gamma strip

**Status:** `LITERATURE+DERIVED` + `NEGATIVE/OBSTRUCTION` for the analytic-functional escape left beyond PC-339/PC-340.

PC-339 and PC-340 use the exact Gamma half-strip `|Im z|<pi/2` together with the zeros `z=log p` forced by mixed-semiprime nulls. Their proofs place the relevant interpolation function in `H^infty` after removing elementary growth: first for boundary-admissible finite measures, then for finite-order distributions with polynomial strip growth.

The polynomial-growth hypothesis is not the real analytic boundary. The same uniqueness survives for the full **Nevanlinna class / functions of bounded characteristic**, which allows much more singular growth. Moreover the strip width `pi/2` is sharp already inside `H^infty`: on every strictly narrower strip there is a nonzero bounded analytic function vanishing at every prime logarithm.

Thus a scalar Mellin-frequency proposal cannot evade PC-339/PC-340 merely by replacing finite-order growth by an arbitrarily large bounded-characteristic analytic functional. To survive the same semiprime-zero argument on the full Gamma strip, its interpolation function must leave bounded characteristic itself; alternatively it must lose part of the Gamma strip, in which case the prime-log zeros alone no longer imply uniqueness.

## 1. Exact zero-set threshold for prime logarithms

For `a>0`, let

\[
S_a:=\{z\in\mathbb C:|\operatorname{Im}z|<a\}.
\]

Let `N(S_a)` denote the holomorphic functions of bounded characteristic on this strip. Equivalently, after conformally mapping `S_a` to the disk, these are the holomorphic Nevanlinna-class functions. A nonzero function in this class has a Blaschke zero set.

The conformal map

\[
\phi_a(z)=\tanh\!\left(\frac{\pi z}{4a}\right)
\tag{1}
\]

sends `S_a` to the unit disk. For a prime `q`, put `z_q=log q`. Then

\[
\phi_a(z_q)
=\frac{q^\alpha-1}{q^\alpha+1},
\qquad
\alpha:=\frac{\pi}{2a},
\tag{2}
\]

and hence exactly

\[
1-|\phi_a(z_q)|
=\frac{2}{q^\alpha+1}.
\tag{3}
\]

Therefore

\[
\sum_{q\ \mathrm{prime}}
\bigl(1-|\phi_a(\log q)|\bigr)
\quad\text{diverges iff}\quad
\alpha\le1,
\tag{4}
\]

because `sum_q 1/q` diverges, while for `alpha>1` the prime sum is bounded by `sum_n n^{-alpha}`.

Consequently:

\[
\boxed{
 a\ge\frac\pi2,\quad F\in N(S_a),\quad
 F(\log q)=0\ \text{for all but finitely many primes }q
 \Longrightarrow F\equiv0.
}
\tag{5}
\]

Conversely, if `0<a<pi/2`, then the points `phi_a(log q)` satisfy the Blaschke condition. Hence their disk Blaschke product pulls back through `phi_a` to a nonzero function

\[
\boxed{
B_a\in H^\infty(S_a),
\qquad
B_a(\log q)=0
\quad(q\ \mathrm{prime}).
}
\tag{6}
\]

This makes the width threshold exact: below `pi/2`, even bounded holomorphic functions can carry all prime-log zeros without vanishing identically.

## 2. Prime-Circle semiprime interpolation needs only bounded characteristic

Retain the PC-179 shell factorization

\[
\mathcal R_n(s)=U(s)A_n(s),
\qquad
U(s)=-\Gamma(s)\zeta(s),
\qquad
A_n(s)=n^{1-s}\prod_{p\mid n}(1-p^{s-1}).
\tag{7}
\]

Fix `sigma>0`, put `beta=1-sigma`, and let `T` be a finite complex Borel measure on the Mellin-frequency line. Define

\[
L_T(n)=\int_{\mathbb R}\mathcal R_n(\sigma+it)\,dT(t),
\qquad
g_p(t)=\mathcal R_p(\sigma+it).
\tag{8}
\]

For `p=2,3`, let

\[
dS_p(t)=g_p(t)\,dT(t),
\qquad
G_p(x)=\widehat S_p(x)
=\int e^{-itx}\,dS_p(t),
\tag{9}
\]

and on the real axis set

\[
F_p(x)=e^{\beta x}G_p(x)-G_p(0).
\tag{10}
\]

Assume only that each real function in (10) admits a holomorphic continuation satisfying

\[
\boxed{F_2,F_3\in N(S_{\pi/2}).}
\tag{11}
\]

No boundary exponential moment and no polynomial growth bound is assumed.

For distinct primes `p,q`, the exact factorization `A_{pq}=A_pA_q` gives, exactly as in PC-339,

\[
F_p(\log q)=L_T(pq).
\tag{12}
\]

Hence exact mixed-semiprime nulls

\[
L_T(pq)=0
\qquad(p\ne q\text{ prime})
\tag{13}
\]

force `F_2=F_3=0` by (5). Therefore

\[
G_p(x)=C_pe^{-\beta x},
\qquad C_p=G_p(0).
\tag{14}
\]

Because `S_p` is a finite measure, `G_p` is bounded on the real axis. If `sigma!=1`, then `beta!=0`, so (14) is bounded at both real ends only when `C_p=0`. Fourier uniqueness gives `S_p=0`. Since `A_2(\sigma+it)` is then uniformly nonzero on the real line and

\[
\mathcal R_n(\sigma+it)
=g_2(t)\frac{A_n(\sigma+it)}{A_2(\sigma+it)},
\tag{15}
\]

the quotient is bounded and

\[
\boxed{L_T(n)=0\qquad(n>1,\ \sigma\ne1).}
\tag{16}
\]

If `sigma=1`, equation (14) says that `G_p` is constant, so

\[
g_pT=C_p\delta_0.
\tag{17}
\]

Commutativity of multiplication by `g_2,g_3` gives

\[
C_2\log3=C_3\log2,
\tag{18}
\]

so for one constant `c`, subtracting `c delta_0` leaves a finite measure annihilated by both `g_2` and `g_3`. On `Re(s)=1`, the classical zero-free theorem for `zeta` and the irrationality of `log2/log3` imply that `g_2` and `g_3` have no common real zero; also `g_p(0)=log p`. The residual measure is therefore zero. Thus

\[
\boxed{
T=c\delta_0,
\qquad
L_T(n)=c\Lambda(n)
\quad(n>1,\ \sigma=1).
}
\tag{19}
\]

So the PC-339 classification remains valid under the much weaker analytic hypothesis (11).

## 3. Why this is genuinely beyond finite-order strip growth

Bounded characteristic is not a disguised polynomial-growth assumption. On the disk, if `h` is holomorphic with positive real part, then `exp(h)` is of bounded characteristic because `exp(-h)` is bounded and zero-free. Taking

\[
h(w)=\frac{1+w}{1-w}
\tag{20}
\]

and transporting it to `S_{pi/2}` gives functions in the Nevanlinna class with growth comparable to `exp(e^x)` along a real end of the strip. Thus the class admitted by (11) contains functions far beyond the fixed polynomial growth handled in PC-340.

The result is nevertheless also sharp at the zero-set level. Equation (6) shows that if the available analytic continuation has half-width `a<pi/2`, no theorem using only membership in bounded characteristic and the zeros `log q` can force the interpolation function to vanish: an explicit nonzero `H^infty` counterexample already exists.

Accordingly there are two mathematically distinct ways left to evade this uniqueness mechanism:

- retain the full Gamma strip but produce a semiprime interpolation function outside the Nevanlinna/bounded-characteristic class;
- lose part of the strip and add genuinely new structure beyond the locations of the prime-log zeros.

Neither escape is itself an RH mechanism.

## 4. Prior-art and novelty audit

The analytic zero-set theorem is classical. W. K. Hayman, **Identity Theorems for Functions of Bounded Characteristic**, *Journal of the London Mathematical Society* 58 (1998), 127--140, DOI `10.1112/S0024610798006334`, explicitly recalls the canonical bounded-characteristic factorization and the consequence that a nonzero Nevanlinna-class function has a Blaschke zero set; a non-Blaschke zero sequence is therefore a uniqueness set.

The conformal strip calculation (1)--(4), Euler divergence at the endpoint, and the existence of the subcritical Blaschke product are elementary consequences of that classical theory. Directed searches for `prime logarithms` combined with Blaschke/Nevanlinna/bounded-characteristic uniqueness did not locate an independent zeta or RH mechanism based on this exact interpolation packet. No historical novelty is claimed for the complex-analysis ingredients.

The line-local mathematical delta is narrower and precise: **PC-339/PC-340 do not stop at bounded or polynomial strip growth; the prime-log semiprime packet forces the same collapse throughout the entire bounded-characteristic class, and `pi/2` is the exact width at which this remains true.** This is a classification/no-go result for the Prime-Circle selector mechanism, not a new theorem about Nevanlinna theory.

## 5. Consequence for the surviving frontier

The scalar global-frequency escape is now smaller than the frontier stated in PC-340. Increasing analytic-functional growth beyond every fixed polynomial does not help while the resulting semiprime interpolation function remains of bounded characteristic on the full Gamma strip. Conversely, a narrower strip cannot be repaired by a stronger use of the same prime-log zero set, because a bounded Blaschke survivor exists there.

What remains genuinely outside this result is an interpolation function of unbounded characteristic on the full strip, a construction whose natural continuation has smaller width but carries additional source-forced constraints beyond its zeros, shell-dependent symbols, nonlinear or matrix-valued readouts, and genuinely cross-shell/cross-level operators before scalar Mellin evaluation.

As with PC-339/PC-340, this gives neither the zeta functional equation nor a critical-line positivity/spectral criterion. Its role is to close a broad analytic-functional loophole and to identify exactly what analytic resource a surviving scalar proposal would have to add.

## Audit / falsification tests

The result fails if any of the following checkpoints fails:

1. `phi_a` in (1) must map `S_a` conformally to the disk and give the exact defect (3);
2. the prime sum in (4) must diverge exactly for `a>=pi/2`;
3. a nonzero bounded-characteristic function must have a Blaschke zero set;
4. for `a<pi/2`, the prime-log image must actually satisfy the Blaschke condition, yielding the bounded survivor (6);
5. in the Prime-Circle application, (12) must follow from the exact shell factorization rather than an imposed interpolation;
6. (11) is an explicit hypothesis, not something inferred automatically for every global selector.

In particular, this finding does **not** classify arbitrary analytic functionals. A selector for which the source-induced `F_p` is outside `N(S_{pi/2})` is a genuine uncovered case.