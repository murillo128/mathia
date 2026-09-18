# PC-340 — finite-order global Mellin distributions collapse at the critical Gamma strip

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for the non-measure finite-order global Mellin-selector escape left open by PC-339.

PC-338 proves that every compactly supported distributional Mellin selector with exact mixed-semiprime nulls collapses to the von Mangoldt endpoint. PC-339 removes compact support for finite complex measures by using the exact `exp(-pi |t|/2)` decay of `Gamma(s)`: the resulting Fourier-Laplace transform is bounded on the strip `|Im z|<pi/2`, and the zeros at the prime logarithms violate the Blaschke condition exactly at that width.

Finite distributional order does not evade that mechanism. It adds only polynomial growth in the Fourier-Laplace variable, and a zero-free `cosh` factor removes any fixed polynomial growth without narrowing the strip. Consequently the same prime-log uniqueness argument applies to a broad genuinely noncompact class of **non-measure distributions**.

For `n>1`, retain the PC-179 factorization

\[
\mathcal R_n(s)=U(s)A_n(s),
\qquad
U(s):=-\Gamma(s)\zeta(s),
\qquad
A_n(s):=n^{1-s}\prod_{p\mid n}(1-p^{s-1}),
\tag{1}
\]

with the removable endpoint value

\[
\mathcal R_n(1)=\Lambda(n).
\tag{2}
\]

Fix `sigma>0`, put `beta=1-sigma`, and let

\[
T=\sum_{j=0}^{N}D^j\mu_j
\tag{3}
\]

where every `mu_j` is a finite complex Borel measure on `R` and `D` is distributional differentiation in the Mellin-frequency variable `t`. Define

\[
L_T(n):=\langle T,\mathcal R_n(\sigma+it)\rangle.
\tag{4}
\]

The pairing is well-defined because every fixed shell transform and all of its finite `t`-derivatives have Gamma decay at infinity.

For `p=2,3`, write

\[
g_p(t):=\mathcal R_p(\sigma+it).
\tag{5}
\]

Assume the following **critical Gamma-strip admissibility** for every `0<=j<=N`, every `0<=k<=j`, and `p in {2,3}`:

\[
\boxed{
\int_{\mathbb R}
 e^{\pi|t|/2}
 |g_p^{(k)}(t)|\,d|\mu_j|(t)<\infty.
}
\tag{6}
\]

The measures may have unbounded support. By Stirling's formula together with standard polynomial vertical-line bounds for `zeta` and its finitely many derivatives, (6) holds, for example, whenever the `mu_j` have sufficiently many polynomial moments. It therefore includes derivatives of Gaussian/Schwartz-density measures, derivatives of many globally supported finite measures, and finite-order singular selectors that are not measures themselves.

Then exact mixed-semiprime nulls

\[
\boxed{
L_T(pq)=0
\qquad\text{for every pair of distinct primes }p,q
}
\tag{7}
\]

force

\[
\boxed{
\begin{array}{ll}
\sigma\neq1:&L_T(n)=0\quad(n>1),\\[1mm]
\sigma=1:&T=c\delta_0\ \text{and}\ L_T(n)=c\Lambda(n)\quad(n>1)
\end{array}}
\tag{8}
\]

for one constant `c`. Thus within this finite-order global class there is not even a new invisible distributional correction on the endpoint line: the selector itself reduces to the endpoint delta.

## 1. Multiplying a finite-order selector by a prime shell still gives only polynomial strip growth

Let

\[
S_p:=g_pT.
\tag{9}
\]

For a smooth function `g`, the distributional Leibniz identity gives

\[
gD^j\mu
=
\sum_{k=0}^{j}
(-1)^k\binom jk
D^{j-k}(g^{(k)}\mu).
\tag{10}
\]

Therefore

\[
S_p
=
\sum_{j=0}^{N}\sum_{k=0}^{j}
(-1)^k\binom jk
D^{j-k}(g_p^{(k)}\mu_j).
\tag{11}
\]

By (6), every measure `g_p^{(k)}\mu_j` has a finite exponential moment of width `pi/2`. Its Fourier-Laplace transform is therefore holomorphic on

\[
|\operatorname{Im}z|<\frac\pi2
\tag{12}
\]

and bounded continuously up to both boundary lines. Taking Fourier transforms in (11) gives

\[
\widehat S_p(z)
=
\sum_{j=0}^{N}\sum_{k=0}^{j}
(-1)^k\binom jk
(iz)^{j-k}
\int_{\mathbb R}e^{-itz}g_p^{(k)}(t)\,d\mu_j(t).
\tag{13}
\]

Hence, uniformly on the closed strip,

\[
\boxed{
|\widehat S_p(z)|\le C_p(1+|z|)^N.
}
\tag{14}
\]

This is the key extension beyond PC-339. Passing from measures to any fixed distributional order costs only a polynomial factor in `z`; it does **not** reduce the available strip width.

## 2. Semiprime nulls again make every prime logarithm a zero

For a prime `q`,

\[
A_q(\sigma+it)
=q^{\beta-it}-1.
\tag{15}
\]

For distinct primes `p,q`, `A_{pq}=A_pA_q`, so

\[
\begin{aligned}
L_T(pq)
&=\langle T,g_p(t)(q^{\beta-it}-1)\rangle\\
&=q^\beta\widehat S_p(\log q)-\widehat S_p(0).
\end{aligned}
\tag{16}
\]

Set

\[
C_p:=\widehat S_p(0),
\qquad
F_p(z):=e^{\beta z}\widehat S_p(z)-C_p.
\tag{17}
\]

Condition (7) gives

\[
F_p(\log q)=0
\qquad(q\text{ prime},\ q\neq p).
\tag{18}
\]

Choose an integer `m>2|beta|` and define

\[
H_p(z):=
\frac{F_p(z)}{(2\cosh(z/2))^m}.
\tag{19}
\]

The denominator has no zero in the closed strip `|Im z|<=pi/2`. Its exponential growth in `|Re z|` dominates both the elementary factor `e^{beta z}` and the fixed polynomial growth in (14). Thus

\[
\boxed{
H_p\in H^\infty\!\left(\left\{z:|\operatorname{Im}z|<\frac\pi2\right\}\right).
}
\tag{20}
\]

Under the conformal map

\[
w=\tanh(z/2),
\tag{21}
\]

the prime-log zeros become

\[
w_q=\frac{q-1}{q+1},
\qquad
1-|w_q|=\frac{2}{q+1}.
\tag{22}
\]

Since

\[
\sum_{q\ \mathrm{prime}}\frac1q=\infty,
\tag{23}
\]

these zeros violate the Blaschke condition for any nonzero bounded analytic function on the disk. Removing the one excluded prime `p` is immaterial. Therefore

\[
\boxed{H_p\equiv0,\qquad F_p\equiv0}
\tag{24}
\]

for `p=2,3`.

The critical point is that **finite distributional order changes only the polynomial numerator in (19), not the strip width in (20)**. The exact `pi/2` Gamma strip therefore stays at the same Euler/Blaschke threshold as in PC-339.

## 3. Off the endpoint line every visible response vanishes

For real `x`, (24) yields

\[
\widehat S_p(x)=C_pe^{-\beta x}.
\tag{25}
\]

If `sigma!=1`, then `beta!=0`. The left side has at most polynomial growth by (14), whereas the right side grows exponentially at one end of the real axis unless `C_p=0`. Hence

\[
\widehat S_p(x)=0
\qquad(x\in\mathbb R),
\tag{26}
\]

and injectivity of the Fourier transform on tempered distributions gives

\[
S_p=g_pT=0.
\tag{27}
\]

Already `p=2` is then enough. Since

\[
A_2(\sigma+it)=2^{\beta-it}-1
\tag{28}
\]

has no real zero when `beta!=0`, its reciprocal is smooth with bounded derivatives. Every shell can be written

\[
\mathcal R_n(\sigma+it)
=g_2(t)\frac{A_n(\sigma+it)}{A_2(\sigma+it)},
\tag{29}
\]

where the quotient is smooth and bounded with bounded derivatives. Thus (27) implies

\[
\boxed{L_T(n)=0\qquad(n>1,\ \sigma\neq1).}
\tag{30}
\]

Any distributional mass that might sit on zeros of the universal `U` envelope is invisible to every shell; it cannot provide a prime-circle spectral selector.

## 4. On the endpoint line the selector itself is exactly a delta

Let `sigma=1`, so `beta=0`. Equation (25) is now constant, and therefore

\[
S_p=C_p\delta_0
\qquad(p=2,3).
\tag{31}
\]

Because

\[
g_p(0)=\mathcal R_p(1)=\log p,
\tag{32}
\]

commutativity of multiplication gives

\[
g_3(g_2T)=g_2(g_3T),
\]

hence

\[
C_2\log3=C_3\log2.
\tag{33}
\]

There is therefore a single constant

\[
c=\frac{C_2}{\log2}=\frac{C_3}{\log3}.
\tag{34}
\]

Put

\[
T_*:=T-c\delta_0.
\tag{35}
\]

Then

\[
g_2T_*=g_3T_*=0.
\tag{36}
\]

The smooth functions `g_2` and `g_3` have no common real zero. At `t=0` both equal the nonzero values in (32). For `t!=0`, the classical zero-free theorem for `zeta(s)` on `Re(s)=1` and the fact that `Gamma` has no zeros show that a common zero would require simultaneously

\[
2^{-it}=1,
\qquad
3^{-it}=1.
\tag{37}
\]

That would make `t log2` and `t log3` integer multiples of `2pi`, impossible for `t!=0` because `log2/log3` is irrational.

Hence

\[
a(t):=\frac{\overline{g_2(t)}}{|g_2(t)|^2+|g_3(t)|^2},
\qquad
b(t):=\frac{\overline{g_3(t)}}{|g_2(t)|^2+|g_3(t)|^2}
\tag{38}
\]

are smooth and satisfy

\[
a g_2+b g_3=1.
\tag{39}
\]

Multiplying (36) by this smooth Bezout identity gives

\[
\boxed{T_*=0,\qquad T=c\delta_0.}
\tag{40}
\]

Finally (2) gives

\[
\boxed{L_T(n)=c\Lambda(n).}
\tag{41}
\]

Thus derivatives of endpoint deltas, globally supported derivative measures, and other finite-order singular corrections cannot survive the semiprime-null condition under the critical-strip admissibility. Only the classical von Mangoldt endpoint channel remains.

## 5. Prior-art and novelty audit

The analytic ingredients are classical. Fourier-Laplace transforms of distributions of exponential growth, including their holomorphy and polynomial-growth behavior, belong to standard distribution/Paley-Wiener theory; a broader neighboring treatment is Masanori Suwa, **Distributions of Exponential Growth with Support in a Proper Convex Cone**, *Publ. RIMS* 40 (2004), 565--603, DOI `10.2977/PRIMS/1145475815`. The zero-set step is ordinary Blaschke theory for bounded analytic functions, and the endpoint classification also uses only injectivity of the Fourier transform, the classical zero-free line `Re(s)=1`, and irrationality of `log2/log3`.

A directed search around Fourier-Laplace transforms of finite-order/exponentially growing distributions, bounded-characteristic functions on strips, Blaschke uniqueness sets, and prime logarithms found the expected classical transform and zero-set theory, but no independent RH mechanism matching (8). No historical novelty is claimed for any of those analytic ingredients.

The project-local exact delta is the interaction of those classical tools with the Prime-Circle shell factorization: **the Gamma factor supplies a strip exactly wide enough that the prime-log semiprime constraints form a non-Blaschke uniqueness set, and finite distributional order cannot change that threshold because it contributes only polynomial transform growth.** This strictly extends PC-339 from finite global measures to a natural non-measure finite-order class.

The proof is self-contained and the literature is neighboring prior art rather than a load-bearing dependency, so no new `SOURCES.md` anchor is required.

## 6. Consequence and surviving frontier

PC-339 left non-measure distributions or analytic functionals with more singular global growth open. The finite-order part of that escape is now substantially narrower:

\[
\boxed{
\begin{array}{c}
T=\sum_{j=0}^{N}D^j\mu_j,\\
\text{critical Gamma-strip admissibility},\\
L_T(pq)=0\ \text{for all distinct primes }p,q
\end{array}
\Longrightarrow
\begin{cases}
0,&\sigma\neq1,\\
c\delta_0\mapsto c\Lambda,&\sigma=1.
\end{cases}}
\tag{42}
\]

More abstractly, the proof only needs `g_2T` and `g_3T` to have Fourier-Laplace transforms holomorphic on the full `pi/2` strip with at most polynomial growth there. Any finite-order selector satisfying that transform condition is subject to the same collapse.

What remains outside the theorem is correspondingly sharper: selectors whose global tails or analytic-functional order destroy polynomial control on the full Gamma strip, shell-dependent symbols, nonlinear or matrix-valued readouts, and genuinely cross-shell/cross-level operators before scalar Mellin evaluation. Merely replacing a finite measure by derivatives of measures, delta derivatives, or another fixed finite-order global distribution is not an escape.

As in PC-339, this is a source-selector no-go theorem, not an RH criterion. It supplies neither a functional equation nor a critical-line positivity theorem. Any surviving proposal must still provide an independent zero-sensitive destination theorem rather than treating preservation of prime-power support as progress by itself.

## Audit / falsification tests

A counterexample is a fixed `sigma>0` and a selector (3) satisfying (6) and all semiprime nulls (7), but violating (8). The proof has five exact checkpoints:

1. the Leibniz expansion (10) must make `g_pT` a finite sum of derivatives of exponentially finite measures;
2. (13)--(14) must give polynomial growth on the **full** closed `pi/2` strip;
3. division by the zero-free `cosh` factor must produce a bounded analytic function without narrowing that strip;
4. the prime logarithms must violate the Blaschke condition via `1-w_q=2/(q+1)`;
5. at `sigma=1`, `g_2` and `g_3` must have no common real zero, so the smooth Bezout identity forces the residual selector to vanish.

Failure of any checkpoint invalidates the classification. In particular, weakening (6) so that only a strictly narrower strip is available is a genuine boundary: the mapped prime-log defects then behave like `q^{-alpha}` with `alpha>1`, the Blaschke sum can converge, and this proof no longer forces uniqueness.