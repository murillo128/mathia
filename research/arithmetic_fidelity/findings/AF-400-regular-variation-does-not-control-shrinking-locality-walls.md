# AF-400 — Regular variation does not control shrinking locality walls

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `NEGATIVE/OBSTRUCTION` · `REGULAR-VARIATION` · `MOVING-SCALE` · `QUANTITATIVE-SAMPLING` · `LOCAL-TO-GLOBAL` · `NO-NOVELTY-CLAIM`

## Claim

AF-399's fixed-wall law does **not** extend from a fixed physical reach `h>0` to an arbitrary shrinking reach `h_N\downarrow0` under ordinary regular variation alone.

For a strictly increasing source `(a_n)`, write

\[
B_N(h)=\max\left\{R\ge0:\log\frac{a_{N+R}}{a_N}\le h\right\}.
\tag{1}
\]

There exist `C^\infty`, strictly increasing regularly varying sources of any prescribed index `\rho>0` for which, with the concrete moving wall

\[
h_N=\frac1{(\log N)^2},
\tag{2}
\]

the normalized successor cost

\[
\frac{B_N(h_N)}{Nh_N}
\tag{3}
\]

has two different subsequential limits. Thus the fixed-scale Karamata law in AF-399 does not determine even the leading mesoscopic conversion coefficient.

A simple sufficient repair is **local logarithmic-slope control**. Let `f:[x_0,\infty)\to(0,\infty)` be `C^1` and strictly increasing, let `a_n=f(n)`, and assume

\[
\frac{x f'(x)}{f(x)}\longrightarrow\rho>0.
\tag{4}
\]

Then for every sequence `h_N>0` satisfying

\[
h_N\to0,
\qquad
Nh_N\to\infty,
\tag{5}
\]

one has

\[
\boxed{
B_N(h_N)\sim \frac{Nh_N}{\rho}.
}
\tag{6}
\]

For the rational-prime source a differentiable interpolation is not needed. The exact identity

\[
B_N(h)=\pi(e^h p_N)-N
\tag{7}
\]

shows that a quantitative prime-number theorem provides the scale-matched replacement. If

\[
\pi(x)=\operatorname{li}(x)+O(x\delta(x))
\tag{8}
\]

with an eventually comparable error profile on `[x,e^{o(1)}x]`, and

\[
h_N\to0,
\qquad Nh_N\to\infty,
\qquad
\delta(p_N)\log p_N=o(h_N),
\tag{9}
\]

then

\[
\boxed{B_N(h_N)\sim Nh_N.}
\tag{10}
\]

In particular, the classical Korobov--Vinogradov prime-number-theorem error implies `(10)` for every polylogarithmically shrinking wall

\[
h_N=(\log N)^{-A}
\qquad(A>0\text{ fixed}).
\tag{11}
\]

The durable fidelity boundary is therefore stronger than AF-399's fixed-wall statement:

> **Fixed physical walls require only global regular variation; shrinking physical walls require source information at the same moving scale.**

The relevant extra resource can be a local logarithmic derivative, a short-interval counting theorem, or another scale-matched modulus. Global source asymptotics do not supply it automatically.

## Explicit smooth counterexample

Fix `\rho>0` and choose

\[
0<c<\frac{\rho}{4}.
\tag{12}
\]

For `x\ge e`, define

\[
f(x)
=x^\rho
\exp\left(
\frac{c}{\log x}\sin((\log x)^2)
\right),
\qquad
a_n=f(n).
\tag{13}
\]

Put `t=\log x`. Then

\[
\log f(e^t)
=\rho t+\frac{c}{t}\sin(t^2),
\tag{14}
\]

so

\[
\frac{d}{dt}\log f(e^t)
=
\rho+2c\cos(t^2)-\frac{c}{t^2}\sin(t^2).
\tag{15}
\]

For `t\ge1`, the right side is at least `\rho-3c>0`; hence `f` is strictly increasing. Also

\[
\frac{f(\lambda x)}{f(x)}
=
\lambda^\rho
\exp\left(
\frac{c}{\log(\lambda x)}\sin((\log(\lambda x))^2)
-
\frac{c}{\log x}\sin((\log x)^2)
\right)
\longrightarrow\lambda^\rho,
\tag{16}
\]

so `f` and `(a_n)` are regularly varying with index `\rho`.

However, their local logarithmic slope does not converge: the oscillatory term in `(15)` retains amplitude `2c`.

Take `h_N=(\log N)^{-2}` and write

\[
t_N=\log N,
\qquad
r=\frac{R}{N}.
\]

On any block `r=O(t_N^{-2})`,

\[
\Delta=\log(1+r)=r+O(r^2)=O(t_N^{-2}).
\tag{17}
\]

For `u\in[t_N,t_N+\Delta]`,

\[
u^2-t_N^2=O(t_N^{-1}),
\]

and therefore, uniformly on such blocks,

\[
\frac{d}{du}\log f(e^u)
=
\rho+2c\cos(t_N^2)+o(1).
\tag{18}
\]

Integration gives

\[
\log\frac{a_{N+R}}{a_N}
=
\left(\rho+2c\cos(t_N^2)+o(1)\right)\frac{R}{N}
\tag{19}
\]

uniformly for `R=O(Nh_N)`. Since `Nh_N\to\infty`, integer rounding is negligible relative to `Nh_N`, so the exact crossing in `(1)` satisfies

\[
\frac{B_N(h_N)}{Nh_N}
=
\frac{1}{\rho+2c\cos((\log N)^2)+o(1)}.
\tag{20}
\]

Choose integer subsequences

\[
N_k=\left\lfloor e^{\sqrt{2\pi k}}\right\rfloor,
\qquad
M_k=\left\lfloor e^{\sqrt{(2k+1)\pi}}\right\rfloor.
\tag{21}
\]

The integer rounding changes their logarithms by an exponentially small amount, hence

\[
\cos((\log N_k)^2)\to1,
\qquad
\cos((\log M_k)^2)\to-1.
\tag{22}
\]

Consequently

\[
\boxed{
\frac{B_{N_k}(h_{N_k})}{N_kh_{N_k}}
\to\frac1{\rho+2c},
\qquad
\frac{B_{M_k}(h_{M_k})}{M_kh_{M_k}}
\to\frac1{\rho-2c}.
}
\tag{23}
\]

Ordinary regular variation therefore leaves a genuine mesoscopic degree of freedom even for smooth monotone sources. The obstruction is not discontinuity, integer noise, or failure of global asymptotics; it is loss of the local convergence rate when the multiplier itself approaches `1`.

## Local-slope repair

Assume `(4)` and fix `\varepsilon\in(0,\rho)`. For all sufficiently large `x`,

\[
\rho-\varepsilon
\le
\frac{x f'(x)}{f(x)}
\le
\rho+\varepsilon.
\tag{24}
\]

Thus for every `y\ge x` in the tail,

\[
(\rho-\varepsilon)\log\frac{y}{x}
\le
\log\frac{f(y)}{f(x)}
\le
(\rho+\varepsilon)\log\frac{y}{x}.
\tag{25}
\]

Let `B=B_N(h_N)`. By maximality,

\[
\log\frac{f(N+B)}{f(N)}\le h_N
<
\log\frac{f(N+B+1)}{f(N)}.
\tag{26}
\]

Combining `(25)` and `(26)` yields

\[
\log\left(1+\frac{B}{N}\right)
\le
\frac{h_N}{\rho-\varepsilon}
\tag{27}
\]

and

\[
\frac{h_N}{\rho+\varepsilon}
<
\log\left(1+\frac{B+1}{N}\right).
\tag{28}
\]

Because `h_N\to0`, `(27)` first gives `B/N=O(h_N)`. Expanding the logarithms and using `Nh_N\to\infty` to absorb the one-index rounding in `(28)` gives

\[
\frac1{\rho+\varepsilon}
\le
\liminf_{N\to\infty}\frac{B_N(h_N)}{Nh_N}
\le
\limsup_{N\to\infty}\frac{B_N(h_N)}{Nh_N}
\le
\frac1{\rho-\varepsilon}.
\tag{29}
\]

Letting `\varepsilon\downarrow0` proves `(6)`.

This hypothesis is sufficient, not claimed necessary. The moving-wall law only needs enough control of average logarithmic slope on the specific shrinking windows under consideration. Equation `(4)` is a clean source-side condition that supplies that control simultaneously for every such `h_N` above integer scale.

## Rational-prime specialization

For `a_n=p_n`, strict monotonicity gives the exact counting identity `(7)`. Put

\[
x=p_N,
\qquad y=e^{h_N}x.
\]

Under `(8)` and the local comparability assumed there,

\[
\pi(y)-\pi(x)
=
\operatorname{li}(y)-\operatorname{li}(x)
+O(x\delta(x)).
\tag{30}
\]

Since `h_N\to0`,

\[
\operatorname{li}(e^{h_N}x)-\operatorname{li}(x)
=
\int_x^{e^{h_N}x}\frac{dt}{\log t}
=
\frac{x h_N}{\log x}(1+o(1)).
\tag{31}
\]

Condition `(9)` makes the error in `(30)` little-oh of the main term. Hence

\[
B_N(h_N)
=
\frac{p_N h_N}{\log p_N}(1+o(1)).
\tag{32}
\]

The prime number theorem also gives

\[
\frac{p_N}{\log p_N}\sim N,
\tag{33}
\]

so `(10)` follows.

The unconditional Korobov--Vinogradov error has the form

\[
\delta(x)
\ll
\exp\left(
-d(\log x)^{3/5}(\log\log x)^{-1/5}
\right)
\tag{34}
\]

for some `d>0`. Therefore

\[
\delta(p_N)\log p_N
=o((\log N)^{-A})
\tag{35}
\]

for every fixed `A>0`, proving `(11)`.

This is an important distinction from the counterexample: the rational primes possess stronger scale-matched counting information than the bare statement `p_N\in RV_1`. At polylogarithmically shrinking walls, that extra arithmetic information repairs the moving-scale conversion.

## Prior-art and novelty audit

N. H. Bingham, C. M. Goldie, and J. L. Teugels, ***Regular Variation***, Cambridge University Press (1987), DOI `10.1017/CBO9780511721434`, is the standard source for Karamata regular variation, the Uniform Convergence Theorem, representation theorems, smooth variation, asymptotic inversion, and de Haan/Beurling refinements. Ordinary Karamata uniformity is on compact multiplier sets; it does not by itself supply a first-order expansion when the multiplier approaches `1` at a prescribed rate.

N. H. Bingham and A. J. Ostaszewski, **“Beurling slow and regular variation,”** *Transactions of the London Mathematical Society* **1** (2014), 29--56, DOI `10.1112/tlms/tlu002`, develops scale-dependent Beurling regular variation, self-neglecting auxiliary functions, uniform convergence, and smooth representations. It is direct neighboring prior art for the principle that moving scales require their own asymptotic control rather than an unqualified reuse of fixed-multiplier Karamata theory.

NIST DLMF §27.12 records the classical Korobov--Vinogradov estimate

\[
|\pi(x)-\operatorname{li}(x)|
=O\left(
 x\exp\{-d(\log x)^{3/5}(\log\log x)^{-1/5}\}
\right),
\]

which is more than sufficient for the prime specialization `(11)`.

The counterexample `(13)`--`(23)`, the sufficient transfer criterion `(4)`--`(6)`, and the prime counting composition `(7)`--`(10)` are derived here. **No novelty is claimed for regular/smooth/Beurling variation, logarithmic-derivative criteria, the prime-number-theorem error term, or short-interval deduction from a quantitative counting formula.** The Arithmetic Fidelity contribution is the resource separation: AF-399's fixed-wall conversion and a shrinking-wall conversion consume different source information, and the latter must be audited at the same physical scale as the discriminator.

## Boundaries and falsification

The explicit counterexample only proves insufficiency of ordinary regular variation for moving walls; it does not say that every regularly varying source is unstable at shrinking scales.

Condition `(4)` is deliberately sufficient rather than minimal. A source may obey `(6)` for one or many moving scales while its pointwise logarithmic derivative fails to converge. The truly minimal datum is scale-dependent control of the averaged log increment

\[
\log f(Ne^u)-\log f(N)
\]

for `u` of the same order as `h_N`.

The condition `Nh_N\to\infty` separates physical-scale asymptotics from integer granularity. When `Nh_N=O(1)`, successor quantization is itself a leading-order resource and `(6)` need not be the right normalization.

The prime implication `(10)` is only as strong as the available counting error at the requested scale. It does not give asymptotics in genuinely very short intervals where the global PNT error is larger than the expected local count. Maier-type phenomena are a separate warning that sufficiently short prime intervals can have systematic fluctuations even when global density is well controlled.

Nothing here proves that a shrinking PF3 topology wall occurs in the RH program. The theorem says what source information would be required **if** a downstream discriminator asks for one. AF-395--AF-399 concern a fixed physical wall and therefore remain unchanged.

No RH consequence follows from `(10)`: it is a representation-resource statement about how much successor breadth is needed to realize a shrinking logarithmic reach.

## Consequences

AF-399's boundary is now sharp in the following sense. Fixed `h` can be converted by regular variation alone; moving `h_N\to0` cannot. Before translating a shrinking physical discriminator into index depth, the watch must name and prove a source theorem at that same scale.

For generic sources, local logarithmic-slope control is one sufficient certificate. For the rational primes, quantitative prime counting supplies such a certificate throughout every polylogarithmically shrinking logarithmic scale, so those scales are not blocked by the abstract counterexample.

The next useful question is therefore not to compute another successor coefficient from global source asymptotics. It is to identify the smallest physical scale demanded by a live discriminator and compare it directly with the strongest source-side local-density or short-interval theorem available at that scale.