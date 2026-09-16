# PC-319 — small Mordell–Tornheim coupling preserves off-critical zeros

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-BOUNDARY` for the zero-selection question left open by PC-316.

PC-316 identifies the canonical two-prime nonlinear Poisson product with the source-specific Mordell–Tornheim packet

\[
Z_{q,r}^{f,g}(s,t,u)
=\sum_{k,l\ge1}\frac{a(k)b(l)}{k^s l^t(k+l)^u},
\qquad
a(k)=\widehat f(k\bmod q),\quad b(l)=\widehat g(l\bmod r).
\tag{1}
\]

It deliberately leaves open whether the *specific* Prime-Circle coefficient vector might satisfy an additional zero-selection theorem not present for generic Mordell–Tornheim functions. There is now an exact obstruction to the strongest natural version of that hope.

For the smallest canonical pair `(q,r)=(5,7)`, there exist a real `T>1`, a disk `D` compactly contained in `Re(s)>1`, and `epsilon>0` such that for **every** real

\[
0<u<\epsilon,
\tag{2}
\]

the genuinely coupled function

\[
\boxed{
Z_{5,7}(s,T,u)
=\sum_{k,l\ge1}\frac{a_5(k)b_7(l)}{k^s l^T(k+l)^u}
}
\tag{3}
\]

has at least one zero in `D`. These zeros lie in the domain of absolute convergence. Thus the source-specific PC-316 bundle does not merely inherit complicated zero geometry after meromorphic continuation: an open one-sided neighborhood of its decoupled face `u=0` already contains exact canonical slices with zeros strictly to the right of `Re(s)=1`.

This rules out coordinatewise Riemann-line confinement for the canonical Mordell–Tornheim carrier near `u=0`. It does **not** rule out a more selective completion, diagonal, distinguished positive-`u` slice bounded away from zero, or a genuinely multivariable zero-locus theorem.

## 1. The canonical `q=5` one-level factor is a nonexceptional periodic Dirichlet series

For the canonical prime-support source at level `5`,

\[
P_5=\{3\},\qquad f_5=\delta_3-\frac15.
\tag{4}
\]

Let

\[
\omega:=e^{-2\pi i/5}.
\tag{5}
\]

With the unnormalized finite Fourier convention of PC-306--PC-318,

\[
a_5(k)=\widehat f_5(k\bmod5)
=\begin{cases}
\omega^{3k},&5\nmid k,\\
0,&5\mid k.
\end{cases}
\tag{6}
\]

Hence

\[
A_5(s):=\sum_{k\ge1}\frac{a_5(k)}{k^s}
\tag{7}
\]

is a nonzero Dirichlet series with period `5`, absolutely convergent for `Re(s)>1`.

The theorem of Saias--Weingartner on zeros of periodic Dirichlet series has one exceptional class: `P(s)L(s,chi)`, with `P` a Dirichlet polynomial and `chi` a Dirichlet character. The present `A_5` is not in that class. This can be certified exactly from three residue values rather than by genericity.

Assume for contradiction that

\[
A_5(s)=P(s)L(s,\chi),
\qquad
P(s)=\sum_{d\le D}p_d d^{-s}.
\tag{8}
\]

For every sufficiently large prime `ell`, comparison of absolutely convergent Dirichlet coefficients gives

\[
a_5(\ell)=p_1\chi(\ell).
\tag{9}
\]

The left side is nonzero for every large prime, so `p_1\neq0`. Let `Q` be a modulus for `chi` and `M=lcm(5,Q)`. Dirichlet's theorem supplies arbitrarily large primes in every unit class modulo `M`; therefore (9) identifies the corresponding periodic residue values.

First use the class `1 mod M` to get

\[
p_1=a_5(1)=\omega^3.
\tag{10}
\]

Choose any unit `v mod M` with `v=2 mod 5`; such a class exists by CRT. Applying (9) in the prime classes `v` and `v^2` and using multiplicativity of `chi` forces

\[
a_5(4)=\frac{a_5(2)^2}{a_5(1)}.
\tag{11}
\]

But (6) gives

\[
a_5(1)=\omega^3,\qquad
a_5(2)=\omega,\qquad
a_5(4)=\omega^2,
\tag{12}
\]

whereas the right side of (11) equals

\[
\frac{\omega^2}{\omega^3}=\omega^4\ne\omega^2.
\tag{13}
\]

Contradiction. Therefore

\[
\boxed{A_5(s)\ne P(s)L(s,\chi)}
\tag{14}
\]

for every Dirichlet polynomial `P` and Dirichlet character `chi`.

## 2. Saias--Weingartner supplies zeros already in `Re(s)>1`

Eric Saias and Andreas Weingartner, **Zeros of Dirichlet series with periodic coefficients**, *Acta Arithmetica* 140:4 (2009), 335--344, DOI `10.4064/aa140-4-4`, arXiv:`0807.0783`, prove that for a periodic Dirichlet series outside the exceptional class (14), there exists `eta>0` such that for every

\[
\frac12<\sigma_1<\sigma_2<1+\eta
\tag{15}
\]

the number of zeros in

\[
\sigma_1<\Re s<\sigma_2,\qquad |\Im s|\le X
\tag{16}
\]

is bounded above and below by positive constant multiples of `X` for sufficiently large `X`.

Choose

\[
1<\sigma_1<\sigma_2<1+\eta.
\tag{17}
\]

Then `A_5` has infinitely many zeros in the half-plane of absolute convergence. Fix one such zero `s_0`. Since `A_5` is analytic and not identically zero in `Re(s)>1`, there is a closed disk

\[
\overline D\subset\{\Re s>1\}
\tag{18}
\]

containing `s_0` in its interior and no zero of `A_5` on its boundary.

No simplicity assumption on `s_0` is needed below.

## 3. The second canonical factor can be frozen at a nonzero real exponent

For the canonical level `7` source,

\[
P_7=\{3,5\},
\tag{19}
\]

so for nonzero Fourier frequency

\[
b_7(l)=\frac12\left(\xi^{3l}+\xi^{5l}\right),
\qquad
\xi:=e^{-2\pi i/7},
\tag{20}
\]

and `b_7(l)=0` when `7|l`. In particular

\[
b_7(1)=\frac12(\xi^3+\xi^5)\ne0,
\tag{21}
\]

because two seventh roots of unity cannot have ratio `-1`.

Define

\[
B_7(t):=\sum_{l\ge1}\frac{b_7(l)}{l^t},
\qquad \Re t>1.
\tag{22}
\]

As real `t\to+\infty`, absolute convergence gives

\[
B_7(t)\longrightarrow b_7(1)\ne0.
\tag{23}
\]

Therefore choose once and for all a real

\[
T>1\quad\text{with}\quad B_7(T)\ne0.
\tag{24}
\]

At the decoupled face `u=0`, the exact PC-316 control is

\[
\boxed{
Z_{5,7}(s,T,0)=A_5(s)B_7(T).
}
\tag{25}
\]

Thus every zero of `A_5` in `D` is a zero of the canonical two-source packet on that face.

## 4. Rouché persistence turns the decoupled zero into a genuinely coupled zero

For real `u\ge0`, put

\[
F_u(s):=Z_{5,7}(s,T,u).
\tag{26}
\]

Let

\[
\sigma_*:=\min_{s\in\overline D}\Re s>1.
\tag{27}
\]

The canonical Fourier coefficients are bounded. Hence, for `s in D` and `u\ge0`, the difference from the decoupled face is dominated termwise by a constant multiple of

\[
k^{-\sigma_*}l^{-T},
\tag{28}
\]

whose double sum converges. Since

\[
(k+l)^{-u}\longrightarrow1
\qquad(u\to0^+)
\tag{29}
\]

for every `(k,l)`, dominated convergence gives the uniform compact limit

\[
\boxed{
\sup_{s\in\overline D}
|F_u(s)-A_5(s)B_7(T)|\longrightarrow0
\quad(u\to0^+).
}
\tag{30}
\]

On `partial D`, define

\[
m:=\min_{s\in\partial D}|A_5(s)B_7(T)|>0.
\tag{31}
\]

By (30), there exists `epsilon>0` such that for every `0<u<epsilon`,

\[
|F_u(s)-A_5(s)B_7(T)|<m
\qquad(s\in\partial D).
\tag{32}
\]

Rouché's theorem then gives the exact equality of zero counts, with multiplicity,

\[
\boxed{
N_D(F_u)=N_D(A_5)>0
\qquad(0<u<\epsilon).
}
\tag{33}
\]

For every such positive `u`, the denominator `(k+l)^u` is genuinely nonseparable. Moreover `Re(s)>1`, `T>1`, and `u>0` put (3) safely inside its absolute-convergence region. Thus (33) is not a continuation artifact or a boundary zero inherited only at `u=0`: the exact source-specific coupled series itself has zeros there.

## 5. Prior art and novelty audit

No novelty is claimed for the two analytic ingredients. Saias--Weingartner supplies the load-bearing zero theorem for nonexceptional periodic Dirichlet series, and Rouché stability under uniform analytic perturbation is classical complex analysis. PC-315 already uses the same Saias--Weingartner theorem for finite-Fourier eigensectors of a different mixed packet.

There is also neighboring multiple-zeta prior art pointing in the same qualitative direction. Takashi Nakamura, **The universality for linear combinations of Lerch zeta functions and the Tornheim–Hurwitz type of double zeta functions**, *Monatshefte für Mathematik* 162 (2011), 167--178, DOI `10.1007/s00605-009-0164-5`, proves universality and nontrivial zeros in a region of absolute convergence for a Tornheim--Hurwitz-type double-zeta family. PC-316 already records this as a warning against interpreting multiple-zeta functional structure as zero selection. The present argument does not claim Nakamura's theorem for the exact character-weighted Prime-Circle packet.

The durable line-specific content is instead the exact bridge (6)--(33): the **actual smallest canonical Prime-Circle source** has a one-level periodic factor that is provably outside the Saias--Weingartner exceptional class, and those source-generated off-critical zeros survive every sufficiently small *positive* Mordell--Tornheim coupling. No genericity assumption, numerical zero search, simple-zero hypothesis, or meromorphic continuation is used.

## 6. Research consequence and boundary

PC-316 left a legitimate question: although its analytic species is classical, perhaps the canonical Prime-Circle coefficient vector selects an exceptional zero geometry. PC-319 rules out the strongest coordinatewise version of that possibility in an open coupled regime.

Specifically, there cannot be a theorem of the form

\[
\text{“for the canonical }Z_{5,7}(s,T,u),
\text{ all nontrivial }s\text{-zeros lie on }\Re s=1/2”
\tag{34}
\]

for all positive `u` near zero, even after fixing a perfectly regular real `T>1`: (33) gives zeros with `Re(s)>1` for every sufficiently small positive `u`.

This is a boundary result, not a no-go for the full multivariable frontier. It does **not** exclude:

- a distinguished completion whose relevant zero locus mixes `s,t,u` rather than selecting one coordinate;
- a special diagonal or positive-`u` locus separated from the decoupled face;
- a source-forced operation different from the additive `(k+l)` Mordell--Tornheim coupling;
- a theorem about another invariant of the full multivariable field rather than coordinatewise zeros.

What it does exclude is treating the exact PC-316 coefficient vector by itself as sufficient evidence for Riemann-like coordinatewise zero confinement. Near the natural decoupling face, its source-specific zeros demonstrably behave like the generic periodic/multiple-zeta side of the prior-art boundary.

## 7. Audit and falsification tests

The result can be falsified at seven exact bridges:

1. reconstruct the canonical `q=5` source and verify (6);
2. verify the residue values in (12);
3. test the exceptional-class contradiction (9)--(13), including the Dirichlet-theorem passage from large prime coefficients to unit residue classes;
4. apply the precise Saias--Weingartner theorem to obtain a zero of `A_5` in a strip contained in `Re(s)>1`;
5. verify `b_7(1)\ne0` and hence the existence of a real `T>1` with (24);
6. check the exact face factorization (25) against PC-316;
7. verify the uniform dominated-convergence estimate (30) and Rouché count (33).

Failure of any one of these bridges invalidates the claimed coupled off-critical-zero persistence. Otherwise the conclusion is theorem-level and entirely inside the original Prime-Circle harmonic/Mordell--Tornheim construction.
