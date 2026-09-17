# PC-339 — the critical Gamma strip collapses boundary-admissible global Mellin measures

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for a genuinely noncompact scalar Mellin-frequency class left open by PC-338.

PC-179 gives, for `n>1`,

\[
\mathcal R_n(s)
=U(s)A_n(s),
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

PC-335--PC-338 close bounded scalar multipliers, endpoint distributions, finite point support, and then arbitrary compact distributional support in Mellin frequency. The explicit surviving loophole was a shell-independent selector with genuinely noncompact/global frequency support.

A large natural part of that loophole also collapses. Fix `sigma>0` and let `T` be a finite complex Borel measure on the real Mellin frequency `t`. Define

\[
L_T(n)
:=\int_{\mathbb R}\mathcal R_n(\sigma+it)\,dT(t).
\tag{3}
\]

For `p=2,3`, put

\[
g_p(t):=\mathcal R_p(\sigma+it).
\tag{4}
\]

Assume only the **critical Gamma-strip boundary admissibility**

\[
\boxed{
\int_{\mathbb R}
 e^{\pi |t|/2}
 \bigl(|g_2(t)|+|g_3(t)|\bigr)
 \,d|T|(t)<\infty.
}
\tag{5}
\]

The support of `T` may be all of `R`. By Stirling's formula and any standard polynomial vertical-line bound for `zeta`, there is a finite exponent `B_sigma` such that

\[
e^{\pi|t|/2}|g_p(t)|
\ll_{\sigma,p}(1+|t|)^{B_\sigma},
\qquad p=2,3,
\tag{6}
\]

so (5) holds in particular for every finite measure with a sufficiently high polynomial moment. Thus Gaussian, Schwartz-density, and many other genuinely noncompact selectors are included.

Then the exact semiprime-null condition

\[
\boxed{
L_T(pq)=0
\qquad\text{for every pair of distinct primes }p,q
}
\tag{7}
\]

forces the same endpoint collapse as PC-338:

\[
\boxed{
\begin{array}{ll}
\sigma\neq1:&L_T(n)=0\quad(n>1),\\[1mm]
\sigma=1:&L_T(n)=c\Lambda(n)\quad(n>1)
\end{array}}
\tag{8}
\]

for one constant `c` depending on `T`.

The new point is not another compact-support Paley--Wiener argument. The exact `e^{-\pi|t|/2}` decay of the Gamma factor creates a horizontal strip of half-width `pi/2`, and **the prime logarithms sit exactly at the Blaschke uniqueness threshold for that strip**.

## 1. Semiprime nulls become zeros of a bounded analytic strip function

Fix `p=2` or `p=3`, and define the finite measure

\[
dS_p(t):=g_p(t)\,dT(t),
\qquad
C_p:=S_p(\mathbb R).
\tag{9}
\]

Condition (5) gives

\[
\int e^{\pi|t|/2}\,d|S_p|(t)<\infty.
\tag{10}
\]

Hence its Fourier--Laplace transform

\[
\widehat S_p(z)
:=\int_{\mathbb R}e^{-itz}\,dS_p(t)
\tag{11}
\]

is holomorphic for

\[
|\operatorname{Im}z|<\frac\pi2
\tag{12}
\]

and bounded continuously up to both boundary lines. Put

\[
\beta:=1-\sigma
\tag{13}
\]

and

\[
F_p(z)
:=e^{\beta z}\widehat S_p(z)-C_p.
\tag{14}
\]

For a prime `q!=p`,

\[
A_q(\sigma+it)
=q^{\beta-it}-1,
\tag{15}
\]

so at `z=log q`,

\[
\begin{aligned}
F_p(\log q)
&=\int g_p(t)\bigl(q^{\beta-it}-1\bigr)\,dT(t)\\
&=\int U(\sigma+it)A_p(\sigma+it)A_q(\sigma+it)\,dT(t)\\
&=L_T(pq).
\end{aligned}
\tag{16}
\]

Thus (7) gives

\[
F_p(\log q)=0
\qquad(q\text{ prime},\ q\neq p).
\tag{17}
\]

Although `F_p` itself can grow exponentially along the real direction when `beta!=0`, this growth is elementary. Choose an integer

\[
m>2|\beta|
\tag{18}
\]

and define

\[
H_p(z)
:=\frac{F_p(z)}{\bigl(2\cosh(z/2)\bigr)^m}.
\tag{19}
\]

The denominator has no zeros in the closed strip `|Im z|<=pi/2` and grows like `e^{m|Re z|/2}`. Since `widehat S_p` is bounded there, (18) implies

\[
\boxed{H_p\in H^\infty\!\left(\left\{z:\ |\operatorname{Im}z|<\frac\pi2\right\}\right).}
\tag{20}
\]

It has all the zeros in (17).

## 2. Prime logarithms violate the Blaschke condition exactly at Gamma width

The conformal map

\[
w=\tanh(z/2)
\tag{21}
\]

sends the strip `|Im z|<pi/2` to the unit disk. A prime-log zero `z=log q` is sent **exactly** to

\[
w_q
=\tanh\!\left(\frac{\log q}{2}\right)
=\frac{q-1}{q+1}.
\tag{22}
\]

Therefore

\[
1-|w_q|
=\frac{2}{q+1}.
\tag{23}
\]

Every nonzero bounded analytic function on the disk has a zero set satisfying the classical Blaschke condition

\[
\sum_j(1-|w_j|)<\infty.
\tag{24}
\]

But Euler's theorem on reciprocal primes gives

\[
\sum_{q\ \mathrm{prime}}
\frac{2}{q+1}
=\infty.
\tag{25}
\]

Consequently the bounded analytic function corresponding to `H_p` cannot be nonzero. Hence

\[
\boxed{H_p\equiv0,\qquad F_p\equiv0}
\tag{26}
\]

for `p=2,3`.

The width is not incidental. For a strip of half-width `a`, the analogous map is

\[
w=\tanh\!\left(\frac{\pi z}{4a}\right),
\tag{27}
\]

and at `z=log q`,

\[
1-w_q\asymp q^{-\pi/(2a)}.
\tag{28}
\]

A strictly narrower strip `a<pi/2` gives exponent `pi/(2a)>1`, for which the prime sum converges and the zero set is compatible with Blaschke. The Gamma decay gives exactly

\[
a=\frac\pi2,
\qquad
\frac\pi{2a}=1,
\tag{29}
\]

so the shell's archimedean factor lands precisely on Euler's divergent `sum_p 1/p` threshold. This is the structural reason the full boundary admissibility in (5) is decisive.

## 3. The only visible response is zero or the von Mangoldt endpoint

For real `x`, equation (26) gives

\[
e^{\beta x}\widehat S_p(x)=C_p.
\tag{30}
\]

If `sigma!=1`, then `beta!=0`. The Fourier transform of a finite measure is bounded on the real axis, while `C_pe^{-\beta x}` is unbounded at one real end unless `C_p=0`. Therefore

\[
\widehat S_p(x)=0
\qquad(x\in\mathbb R),
\tag{31}
\]

and uniqueness of Fourier transforms of finite measures gives

\[
S_2=S_3=0.
\tag{32}
\]

When `sigma!=1`, each factor

\[
A_p(\sigma+it)=p^{1-\sigma-it}-1
\tag{33}
\]

has no zeros at all, because its first term has modulus `p^{1-sigma}!=1`. Hence the common zero set of `g_2=UA_2` and `g_3=UA_3` is exactly the zero set of the universal envelope `U`. Equation (32) therefore says that the visible part of `T` is supported only where `U=0`; at such points every shell transform `mathcal R_n=UA_n` vanishes. Thus

\[
\boxed{L_T(n)=0\qquad(n>1,\ \sigma\neq1).}
\tag{34}
\]

Now let `sigma=1`, so `beta=0`. Equation (30) says that `widehat S_p` is constant. The only finite measure with constant Fourier transform is a scalar point mass at the origin:

\[
S_p=C_p\delta_0.
\tag{35}
\]

Since

\[
g_p(0)=\mathcal R_p(1)=\log p\neq0,
\tag{36}
\]

`T` has a uniquely determined visible atom `c delta_0` at the endpoint. Subtract it:

\[
T=c\delta_0+T_*.
\tag{37}
\]

Then

\[
g_2T_*=g_3T_*=0.
\tag{38}
\]

Away from `t=0`, a simultaneous zero of `A_2(1+it)` and `A_3(1+it)` would require

\[
t\log2\in2\pi\mathbb Z,
\qquad
t\log3\in2\pi\mathbb Z,
\tag{39}
\]

which is impossible unless `t=0` because `log2/log3` is irrational. The endpoint itself has already been removed, and the pole of `zeta` there is precisely what makes (36) nonzero. Thus any remaining support of `T_*` lies where the universal factor `U` vanishes, so it is invisible to **every** shell. Consequently

\[
\boxed{
L_T(n)=c\mathcal R_n(1)=c\Lambda(n)
\qquad(n>1,\ \sigma=1).
}
\tag{40}
\]

This proves (8).

## 4. Prior-art and novelty audit

Every analytic ingredient is classical: Stirling's `e^{-pi|t|/2}` decay for `Gamma`, the disk/strip conformal equivalence, the Blaschke zero condition for bounded analytic functions, uniqueness of Fourier transforms of finite measures, and Euler's divergence of `sum_p 1/p`. A directed literature search around bounded analytic functions on strips, Blaschke zero sets, logarithms of primes as uniqueness sets, Fourier--Laplace transforms of measures, and prime reciprocal divergence found the expected classical Hardy-space/Blaschke theory but no independent RH mechanism matching the shell implication (8).

No historical novelty is claimed for those theorems. The line-local contribution is the exact way in which (1) couples them: **the Gamma factor supplies precisely the strip width for which `z=log p` maps to a non-Blaschke zero sequence with defect asymptotic to `1/p`**. PC-338 used compact support to obtain an entire function of finite exponential type; the present argument instead permits genuinely noncompact support and uses the source's own archimedean decay to reach the critical bounded-analytic strip.

This remains a no-go theorem, not an RH mechanism. The appearance of the critical Blaschke threshold is structurally exact but it produces uniqueness of the classical `Lambda` endpoint channel, not a functional equation, a critical-line positivity criterion, or a Hilbert--Polya operator.

No new `SOURCES.md` entry is required: the load-bearing facts are classical textbook theorems, while the shell-specific implication and the exact threshold calculation are derived explicitly above.

## 5. Consequence and surviving frontier

PC-338 left all noncompact/global Mellin-frequency support open. Equation (8) closes a broad source-natural part of it:

\[
\boxed{
\text{boundary-admissible finite global Mellin measure}
\ +\ \text{exact semiprime nulls}
\Longrightarrow
\begin{cases}
0,&\sigma\neq1,\\
c\Lambda,&\sigma=1.
\end{cases}}
\tag{41}
\]

In particular, merely replacing a compact frequency window by a Gaussian, Schwartz, rapidly decaying, or other finite global measure with enough polynomial moments does **not** evade the compact-support obstruction. The exact Gamma strip reinstates uniqueness through Blaschke rather than Paley--Wiener.

What remains genuinely outside the theorem is now narrower: noncompact measures that fail the critical boundary condition (5), non-measure distributions or analytic functionals with more singular global growth, shell-dependent selectors, nonlinear/matrix-valued readouts, and genuinely cross-shell/cross-level couplings before scalar evaluation. Any scalar global-frequency proposal should first state why its tails must cross this exact `pi/2` boundary-admissibility threshold and why that failure is forced by the roots-of-unity geometry rather than chosen ad hoc.

The destination-theorem requirement also remains unchanged. Escaping (41) only preserves source information; it does not by itself produce a zero-sensitive sign theorem or a route to RH.

## Audit / falsification tests

A counterexample is a fixed `sigma>0` and finite complex measure `T` satisfying (5) and all exact semiprime nulls (7), but with either

- `sigma!=1` and some `n>1` for which `L_T(n)!=0`; or
- `sigma=1` and shell responses not proportional to `Lambda(n)`.

The proof has four exact checkpoints: boundary admissibility must make `widehat S_2` and `widehat S_3` bounded on the full `pi/2` strip; the normalization (19) must remain bounded and zero-free in its denominator; the map (22) must turn prime logs into a zero sequence whose Blaschke sum is exactly comparable to `sum_p1/p`; and the common-zero classification of `g_2,g_3` must leave only the universal shell-invisible factor plus the endpoint. Failure of any checkpoint invalidates the theorem.
