# PC-151 — full-chord first-Mertens spectral displacement is the prime-pair singular-series law

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY`. PC-147 proves that the primorial primitive-shell inverse-square operator is uniformly approximable in operator norm by bounded chord windows for its isolated top band. PC-149 classifies every fixed local noncommutative moment by generalized totients / Hardy--Littlewood local densities, and PC-150 upgrades every **fixed-radius** scalar spectral function to a finite atomic first-Mertens correction. The remaining natural scalar loophole is to let the chord radius grow all the way to the actual full primitive-shell operator before taking the spectral observable.

That loophole also closes at the first nonzero arithmetic scale. The normalized trace norm of all chords longer than a fixed radius `H`, after multiplication by the natural `log x / phi(N_x)` Mertens factor, is uniformly bounded by a summable prime-pair tail and tends to zero as `H -> infinity`. Consequently the complete all-chord primitive-shell inverse-square Laplacian has an exact limiting Lipschitz spectral-displacement functional obtained by sending the finite atomic law of PC-150 to infinite radius.

More importantly, the resulting atomic coefficients are not merely reminiscent of classical prime-pair arithmetic: their Dirichlet generating function is **literally the singular-series generating function studied by Goldston--Suriajaya**. Its meromorphic continuation contains Riemann-zeta zeros through the classical factor `1/zeta(2s+2)`. Therefore analytic continuation of the Prime-Circle spectral Mellin displacement does expose zeta zeros, but only because the full spectral law has already reduced to the standard Hardy--Littlewood prime-pair singular series. This is a classicalized zero bridge, not a new spectral mechanism.

## 1. The full normalized primitive-shell Laplacian

Let

\[
N_x:=\prod_{p\le x}p,
\qquad
\phi_x:=\varphi(N_x),
\qquad
U_x:=(\mathbb Z/N_x\mathbb Z)^\times.
\]

Let `L_{N_x}^{int}` be the inverse-square chord Laplacian using all edges whose endpoints both lie in the primitive shell `U_x`, and normalize it by the ambient circle scale:

\[
\boxed{
A_x:=N_x^{-2}L_{N_x}^{\rm int}.
}
\tag{1}
\]

For a positive cyclic offset `1 <= h < N_x/2`, one such edge has normalized conductance

\[
 g_{N_x,h}
 :=\frac{1}{4N_x^2\sin^2(\pi h/N_x)}.
\tag{2}
\]

Let

\[
J_h(N_x)
:=\#\{a\bmod N_x:(a,N_x)=(a+h,N_x)=1\}.
\tag{3}
\]

As in PC-149/PC-150, `J_h(N_x)` is the exact number of undirected positive-offset-`h` edges when `h<N_x/2`. For the primorial modulus, CRT gives the exact pair law. If `h` is odd, the modulus-2 obstruction gives

\[
J_h(N_x)=0.
\tag{4}
\]

If `h` is even, put

\[
B_x:=\prod_{3\le p\le x}\frac{p-2}{p-1},
\qquad
G_x(h):=\prod_{\substack{3\le p\le x\\p\mid h}}
\frac{p-1}{p-2}.
\tag{5}
\]

Then

\[
\boxed{
\frac{J_h(N_x)}{\phi_x}=B_xG_x(h).
}
\tag{6}
\]

Writing

\[
C_2:=\prod_{p>2}\frac{p(p-2)}{(p-1)^2}
\tag{7}
\]

for the twin-prime constant in the convention used in PC-150, one has the exact factorization

\[
B_x
=2\left(\prod_{p\le x}\left(1-\frac1p\right)\right)
\left(\prod_{3\le p\le x}\left(1-\frac1{(p-1)^2}\right)\right),
\tag{8}
\]

and hence by Mertens

\[
\boxed{
B_x\sim\frac{2C_2e^{-\gamma}}{\log x}.
}
\tag{9}
\]

Thus for every fixed `h`,

\[
\boxed{
\frac{\log x}{\phi_x}J_h(N_x)
\longrightarrow e^{-\gamma}\mathfrak S_2(h),
}
\tag{10}
\]

where

\[
\mathfrak S_2(h)
=
\begin{cases}
0,&2\nmid h,\\[1mm]
2C_2\displaystyle\prod_{\substack{p\mid h\\p>2}}
\frac{p-1}{p-2},&2\mid h.
\end{cases}
\tag{11}
\]

This is the ordinary Hardy--Littlewood prime-pair singular series for the pair `{0,h}`.

## 2. Long chords vanish uniformly at the first Mertens spectral scale

Let `A_{x,H}` be the radius-`H` truncation used in PC-150, retaining positive offsets `h<=H`, and put

\[
D_{x,H}:=A_x-A_{x,H}.
\tag{12}
\]

Every omitted edge contributes a positive-semidefinite rank-one Laplacian block, so

\[
D_{x,H}\succeq0
\]

and its trace is exactly

\[
\boxed{
\operatorname{Tr}D_{x,H}
=2\sum_{H<h<N_x/2}J_h(N_x)g_{N_x,h}.
}
\tag{13}
\]

For `0<=t<=pi/2`, `sin t >= 2t/pi`; therefore

\[
\boxed{
 g_{N_x,h}\le\frac1{16h^2}
 \qquad (h<N_x/2).
}
\tag{14}
\]

Also define the infinite local factor

\[
G(h):=\prod_{\substack{p\mid h\\p>2}}\frac{p-1}{p-2},
\tag{15}
\]

so `G_x(h)<=G(h)`. For every odd prime `p`,

\[
\frac{p-1}{p-2}\le\left(1-\frac1p\right)^{-2},
\]

hence

\[
G(h)\le\left(\frac{h}{\varphi(h)}\right)^2
\ll (\log\log(3h))^2.
\tag{16}
\]

The last estimate is the standard maximal-order bound for `h/phi(h)`. Since `(log x)B_x` is bounded, equations (6), (13)--(16) give a constant independent of `x` such that

\[
\boxed{
\frac{\log x}{\phi_x}\operatorname{Tr}D_{x,H}
\ll
\sum_{h>H}\frac{(\log\log(3h))^2}{h^2}
\ll
\frac{(\log\log(3H))^2}{H}.
}
\tag{17}
\]

In particular,

\[
\boxed{
\lim_{H\to\infty}\limsup_{x\to\infty}
\frac{\log x}{\phi_x}\|A_x-A_{x,H}\|_1=0.
}
\tag{18}
\]

This is stronger than merely observing that individual long chord weights decay. It proves that **the entire growing-radius tail is negligible in trace norm at exactly the scale where the first arithmetic spectral displacement survives**.

## 3. Exact full-chord Lipschitz spectral-displacement law

The full regular-polygon inverse-square Laplacian has normalized operator norm at most `1/8`; deleting edges can only decrease its quadratic form. Hence the spectra of `A_x` and all `A_{x,H}` lie in the common compact interval `[0,1/8]`.

Let `f` be real Lipschitz on this interval. Since `D_{x,H}\succeq0`, Weyl monotonicity and the sum of eigenvalue displacements give, exactly as in PC-150,

\[
\left|
\operatorname{Tr}f(A_x)-\operatorname{Tr}f(A_{x,H})
\right|
\le
\operatorname{Lip}(f)\operatorname{Tr}D_{x,H}.
\tag{19}
\]

For fixed `H`, PC-150 gives

\[
\frac{\log x}{\phi_x}
\left(
\operatorname{Tr}f(A_{x,H})-\phi_x f(0)
\right)
\longrightarrow
 e^{-\gamma}
\sum_{\substack{1\le h\le H\\2\mid h}}
\mathfrak S_2(h)
\left[
 f\!\left(\frac1{2\pi^2h^2}\right)-f(0)
\right].
\tag{20}
\]

The infinite right-hand series converges absolutely because

\[
|f(1/(2\pi^2h^2))-f(0)|
\le \frac{\operatorname{Lip}(f)}{2\pi^2h^2}
\]

and `mathfrak S_2(h) << (log log(3h))^2`. Letting first `x->infinity` and then `H->infinity` in (17)--(20) proves

\[
\boxed{
\frac{\log x}{\phi_x}
\left(
\operatorname{Tr}f(A_x)-\phi_x f(0)
\right)
\longrightarrow
 e^{-\gamma}
\sum_{\substack{h\ge1\\2\mid h}}
\mathfrak S_2(h)
\left[
 f\!\left(\frac1{2\pi^2h^2}\right)-f(0)
\right].
}
\tag{21}
\]

Complex-valued Lipschitz functions follow by real and imaginary parts.

There is one useful measure-theoretic caution. Because `sum_h mathfrak S_2(h)` diverges, the formal expression

\[
e^{-\gamma}\sum_{2\mid h}\mathfrak S_2(h)
\left(\delta_{1/(2\pi^2h^2)}-\delta_0\right)
\tag{22}
\]

is not a finite signed measure in total variation. Equation (21) defines instead an absolutely convergent **spectral-displacement functional on Lipschitz tests modulo constants**. The cancellation between each edge atom and the zero atom is essential.

Thus the finite atomic law of PC-150 is not hiding a new global scalar spectrum at large chord radius. Its infinite-radius completion is simply the complete prime-pair singular-series atomic hierarchy.

## 4. The first moment closes exactly against PC-140 and Artin's constant

Taking `f(t)=t` in (21) gives

\[
\boxed{
\lim_{x\to\infty}
\frac{\log x}{\phi_x}\operatorname{Tr}A_x
=
\frac{e^{-\gamma}}{2\pi^2}
\sum_{2\mid h}\frac{\mathfrak S_2(h)}{h^2}.
}
\tag{23}
\]

PC-140 independently computed the complete primitive-shell trace and proved

\[
\frac{12\operatorname{Tr}L_{N_x}^{\rm int}+\phi_x}{N_x^3}
=A_x^{\rm Artin}\left(\frac{\phi_x}{N_x}\right)^2,
\]

where

\[
A_x^{\rm Artin}:=
\prod_{p\le x}\left(1-\frac1{p(p-1)}\right)
\longrightarrow A
\]

and `A` is Artin's constant. Combining that exact identity with Mertens gives

\[
\boxed{
\lim_{x\to\infty}
\frac{\log x}{\phi_x}\operatorname{Tr}A_x
=\frac{Ae^{-\gamma}}{12}.
}
\tag{24}
\]

Equating (23) and (24) yields the consistency identity

\[
\boxed{
\sum_{2\mid h}\frac{\mathfrak S_2(h)}{h^2}
=\frac{\pi^2A}{6}.
}
\tag{25}
\]

This also follows directly from the Euler product below. Indeed the `p=2` factor contributes `1/2`, while for every odd prime

\[
\frac{p(p-2)}{(p-1)^2}
\left(1+\frac1{p^2(p-2)}\right)
=
1-\frac1{p(p-1)}.
\]

Equation (25) is therefore an exact independent audit tying the all-chord atomic law back to the previously classicalized Artin × Nicolas trace formula. The same scalar first moment has been reached from two different decompositions and both reduce to standard Euler products.

## 5. The spectral Mellin family is literally the classical singular-series generating function

Define, initially for `Re(s)>1`,

\[
F_{\mathfrak S}(s)
:=\sum_{h\ge1}\frac{\mathfrak S_2(h)}{h^s}.
\tag{26}
\]

Since the singular series vanishes on odd `h`, writing `h=2m` and using multiplicativity of

\[
g(m)=\prod_{\substack{p\mid m\\p>2}}\frac{p-1}{p-2}
\]

gives directly

\[
\boxed{
F_{\mathfrak S}(s)
=2^{1-s}C_2\zeta(s)
\prod_{p>2}\left(1+\frac{p^{-s}}{p-2}\right).
}
\tag{27}
\]

Factor

\[
\mathcal G(s)
:=\prod_{p>2}
\frac{1+p^{-s}/(p-2)}{1+p^{-s-1}}.
\tag{28}
\]

The local ratio is `1+O(p^{-sigma-2})`, locally uniformly for `sigma=Re(s)>-1`, so `mathcal G` is holomorphic there (it need not be zero-free). Since

\[
\prod_{p>2}(1+p^{-s-1})
=
\frac{\zeta(s+1)}{\zeta(2s+2)}
\frac1{1+2^{-s-1}},
\]

we obtain

\[
\boxed{
F_{\mathfrak S}(s)
=
\frac{4C_2}{2^{s+1}+1}
\frac{\zeta(s)\zeta(s+1)}{\zeta(2s+2)}
\mathcal G(s).
}
\tag{29}
\]

This is **not a new Prime-Circle Euler product**. It is exactly equation (2.2) of D. A. Goldston and Ade Irma Suriajaya, *A singular series average and the zeros of the Riemann zeta-function*, **Acta Arithmetica** 200 (2021), 71--90, DOI `10.4064/aa200821-24-2`, arXiv:`2007.16099`. Their paper defines

\[
F(s)=\sum_{k\ge1}\mathfrak S(k)k^{-s}
\]

for the same Hardy--Littlewood prime-pair singular series, continues it to `Re(s)>-1`, and uses the poles from `1/zeta(2s+2)` to obtain explicit zero-dependent formulas for Riesz means of the singular series.

The connection to the intrinsic spectral family is immediate. For `Re(q)>1`, the function `t^q` is Lipschitz on `[0,1/8]` after setting `0^q=0`, so (21) gives

\[
\boxed{
\mathcal M(q)
:=\lim_{x\to\infty}
\frac{\log x}{\phi_x}\operatorname{Tr}(A_x^q)
=
e^{-\gamma}(2\pi^2)^{-q}F_{\mathfrak S}(2q).
}
\tag{30}
\]

Combining with (29),

\[
\boxed{
\mathcal M(q)
=
e^{-\gamma}(2\pi^2)^{-q}
\frac{4C_2}{2^{2q+1}+1}
\frac{\zeta(2q)\zeta(2q+1)}{\zeta(4q+2)}
\mathcal G(2q).
}
\tag{31}
\]

The right side has a meromorphic continuation inherited from the classical singular-series generating function. In particular, nontrivial zeta zeros `rho` appear in the denominator channel at

\[
q=\frac{\rho}{4}-\frac12,
\tag{32}
\]

subject, as always, to possible local/numerator cancellations. Goldston--Suriajaya exploit precisely the corresponding poles `s=rho/2-1` of `F_{mathfrak S}(s)` in their explicit formulas.

This is the decisive novelty audit. A Mellin continuation of the full Prime-Circle spectral displacement **can be made zeta-zero-sensitive**, but the dependence is already completely present in a classical arithmetic generating function before any Prime-Circle spectral interpretation. No new self-adjoint spectrum places zeros on a critical line, no functional-equation symmetry is generated by the chord operator, and the complex Mellin parameter is a post hoc transform of the already-classicalized edge-density law.

## 6. Prior-art classification, falsification surface, and surviving scope

The exact finite pair counts are the generalized-totient / reduced-residue counts already audited in PC-149 and PC-150. The all-radius step in (17)--(21) adds a Prime-Circle-specific analytic closure: the actual inverse-square geometry makes the complete long-chord tail summable strongly enough that the fixed-radius spectral law passes to the full operator at first Mertens order. This closure does not create new arithmetic coefficients; it proves that **there are no additional scalar coefficients waiting at large chord radius on this scale**.

The strongest prior-art collision is exact rather than neighboring. Goldston--Suriajaya's singular-series generating function is equation (29) itself, and their explicit formula already explains how zeta zeros enter its continuation. The same paper proves zero-dependent error terms and conditional/unconditional oscillation statements for Riesz means. Therefore any future claim that the Mellin transform of the PC-151 atomic tail discovers a new zeta-zero channel must first exhibit additional geometric information not contained in `F_{mathfrak S}`.

The result has several direct falsifiers:

1. Direct CRT enumeration must satisfy (6) for every tested primorial and offset. One failure invalidates the tail reduction.
2. Direct matrix construction must satisfy the trace identity (13), because every omitted weighted edge contributes trace `2g_{N,h}`.
3. The scaled long-chord trace tail in (17) must decrease to zero with `H`; a sequence with a nonzero fixed lower tail would falsify passage from PC-150 to (21).
4. Taking `f(t)=t` must reproduce PC-140, equivalently the Euler-product identity (25).
5. The Dirichlet series formed from the PC-150 coefficients must agree term-for-term with the Hardy--Littlewood singular-series generating function and hence with Goldston--Suriajaya equation (2.2).

The boundary is deliberately limited to the **first nonzero `1/log x` scalar spectral-displacement scale** of the full inverse-square primitive-shell operator. It does not classify the `1/log^2 x` connected multi-edge correction, finer spectral-projector/eigenvector organization, conductor-growing word complexity at subleading scales, coherent cross-level transport, or the accepted clue's remaining intrinsically non-Cauchy / infinite-depth coupling boundary. Those sectors may still carry information that trace-level pair densities discard.

There is also an important warning for that surviving work. If a subleading calculation merely produces Riesz/Cesàro/Mellin transforms of the same prime-pair or higher prime-tuple singular series, zero dependence by itself is not progress: the prime-pair case is already a classical explicit-formula phenomenon. A genuinely new Prime-Circle RH mechanism must retain geometric/operator structure that does **not** factor through those standard local-density generating functions.