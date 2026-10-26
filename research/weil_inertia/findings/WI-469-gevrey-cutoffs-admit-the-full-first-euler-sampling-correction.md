# WI-469 — Gevrey cutoffs admit the full first Euler sampling correction

**Status:** LITERATURE+EXACT-DERIVED + CLASSICAL-FUNCTIONAL-CALCULUS-SPECIALIZATION + NO-NOVELTY-CLAIM + NON-RH.

**Local dependencies:** [WI-464](WI-464-full-euler-correction-has-an-integrable-threshold-primitive.md), for the integrable cumulative coefficient and its finite-panel limit; [WI-465](WI-465-analytic-euler-observables-have-a-full-first-zero-sampling-correction.md), for the rational-character arithmetic interface and the preceding analytic class. The hard-threshold boundary remains [WI-463](WI-463-first-euler-threshold-correction-exceeds-logarithmic-bracket-bandwidth.md).

## Claim and significance

Fix `sigma>1` and `r>0`. The full coherent Euler response has its first
zero-sampling correction for every fixed periodic Gevrey test of order
`1<s<sigma`. This includes nonnegative smooth cutoffs with exact zero
and one plateaus. Thus analyticity of the scalar test is not necessary:
there are localized smooth amplitude tests at every fixed
safe line, including arbitrarily small fixed `sigma-1>0`.

The proof supplies two quantitative interfaces. A fourth logarithmic
moment of the rational Fourier coefficients suffices for arithmetic
transport with error `O(T/log T)`. For the actual Euler response, its
oscillatory exponential has subexponential growth in that coefficient
norm, so Gevrey Fourier decay pays the infinite-panel cost.

All test functions, widths, periods, Gevrey constants and source
parameters are fixed before the sampling height tends to infinity.
This is not a hard-threshold theorem or a claim that `s<sigma` is sharp.
It needs neither the far-right scalar smoothing condition of WI-467
nor a finite signed measure representing the correction at small
`sigma-1`. It gives no exclusion of an individual off-line zero.

## Objects and theorem

On the product prime torus use probability Haar measure `m` and set

\[
 A=\sum_{n\ge2}\Lambda(n)n^{-\sigma},\qquad
 a_n=\Lambda(n)n^{-\sigma}/A,\qquad
 G_r(n,m)=e^{-r|\log(n/m)|}-(nm)^{-r},
\]
\[
 Q(z)=\sum_{n,m\ge2}a_na_mG_r(n,m)\chi_{n/m}(z),\qquad
 \chi_u(z)=\prod_p z_p^{\nu_p(u)}.
 \tag{1}
\]

Only prime powers have nonzero `a_n`. The coefficients before and
after collecting equal rational characters are nonnegative;
`0<=Q<=q_*:=Q(1)<=1`. The Gram realization in WI-464 gives the first
inequality. Let `Q_M` retain the pairs `n,m<=M`, with the original
normalization. Along `z_p(t)=exp(-it log p)` these are the Euler
responses. Let `D_T=N(2T)-N(T)` count all nontrivial zeros, with
multiplicity, in the ordinate window.

For definiteness take a four-periodic scalar function

\[
 f(x)=\sum_{j\in\mathbb Z}c_j e^{i\pi jx/2},\qquad
 |c_j|\le C_f e^{-c_f|j|^{1/s}},\qquad 1<s<\sigma,
 \tag{2}
\]

with positive fixed `C_f,c_f`. Any other fixed period works by changing
the frequency constant. The Fourier series and every differentiated
series converge absolutely. Then

\[
 \boxed{\sum_{T<\gamma\le2T}f(Q(\gamma))
 =D_T\int f(Q)\,dm+\frac{T}{2\pi}\mathcal L(f)
       +O_{f,\sigma,r}\!\left(\frac T{\log T}\right),}
 \qquad
 \mathcal L(f)=-\int_0^{q_*}f'(x)C(x)\,dx.
 \tag{3}
\]

Here `C` is precisely WI-464's `L^1` cumulative coefficient, extended
by zero off the response interval. The Haar mean in (3) may be replaced
by `T^(-1) integral_T^(2T) f(Q(t))dt` with the same error order.

## Logarithmic rational height is enough for arithmetic transport

For a reduced positive rational `u=a/b`, write `H(u)=ab` and

\[
 \|F\|_{[4]}=\sum_u |d_u|(1+\log H(u))^4,
 \qquad F=\sum_u d_u\chi_u.
 \tag{4}
\]

This is a unital Banach algebra norm: `H(uv)<=H(u)H(v)` and
`1+x+y<=(1+x)(1+y)` for nonnegative `x,y`. Put

\[
 \kappa(u)=
 \begin{cases}
  (\log p)p^{-j/2},&u=p^{j}\text{ or }p^{-j},\ j\ge1,\\
  0,&\text{otherwise}.
 \end{cases}
 \tag{5}
\]

It is bounded and `kappa(1)=0`. We claim that for every `F` with finite
norm (4),

\[
 \frac1T\left(\sum_{T<\gamma\le2T}F(z(\gamma))-D_Td_1\right)
 =-\frac1{2\pi}\sum_u d_u\kappa(u)
       +O\!\left(\frac{\|F\|_{[4]}}{\log T}\right).
 \tag{6}
\]

Here is the required check beyond WI-465's polylogarithmic cutoff.
Write `L=log T`, take `X=exp(sqrt(L))`, and retain `H(u)<=X`.
For a retained nonconstant character, replace `u` by its reciprocal
when necessary and put `x=a/b>1`. Then `a,b<=X`, `log x>=1/X`.
If `x` is not an integer prime power and `n_x` is a nearest prime
power, then `n_x<=2x` and

\[
 |x-n_x|\ge X^{-1},\qquad
 |\log(x/n_x)|\ge(2X^2)^{-1}.
 \tag{7}
\]

Ford–Meng–Zaharescu, Lemmas 1–2, apply because
`X<=exp(L/(50 log L))` for sufficiently large `T`. Subtracting their
formulas at `2T` and `T`, including the complex comparison rather than
only its real part, gives

\[
 \frac1T\sum_{T<\gamma\le2T}x^{\pm i\gamma}
 =-\frac{\Lambda_*(x)}{2\pi\sqrt x}
 +O\!\left(\frac{(\log x)^2}{L}+L^{-10}
       +\frac{X\log^2(2XT)+X^2\log(2X)}{T}\right).
 \tag{8}
\]

`Lambda_*(x)=log p` at `x=p^j` and is zero otherwise. At resonance the
dyadic main term is exactly the displayed term. Away from resonance
(7) bounds the nearest-prime-power term. The near-one error in Lemma 1
is also covered by the displayed majorant. Negative frequencies follow
by conjugation.

Crucially, sum the first error in (8) with its own `(log x)^2` weight,
instead of replacing every `log x` by `log X`. Since
`log x<=log H(u)`, this costs at most `||F||_[4]/L`. The sum costs
coefficient mass, not the number of retained rationals. The remaining
non-tail errors are `O(||F||_[4]/L)` as well, since `X=exp(sqrt L)`.
The omitted coefficients satisfy

\[
 \sum_{H(u)>X}|d_u|
 \le(1+\log X)^{-4}\|F\|_{[4]}=O(L^{-2}\|F\|_{[4]}).
 \tag{9}
\]

Multiplication by `D_T/T=O(L)` costs `O(||F||_[4]/L)`; the omitted
resonant correction costs only `O(||F||_[4]/L^2)`. This proves (6).
The same truncation, integrating each nonconstant frequency, gives

\[
 \left|\frac1T\int_T^{2T}F(z(t))\,dt-d_1\right|
 \le\|F\|_{[4]}\{2X/T+(1+\log X)^{-4}\}
 =O(\|F\|_{[4]}/L^2).
 \tag{10}
\]

No fixed-dimensional simultaneous-distribution theorem has been used
with a growing hidden dimension.

## Subexponential composition bound for this Euler source

We next prove, with `U=2+|t|`,

\[
 \boxed{\|e^{itQ}\|_{[4]},\quad
        \sup_{M\ge2}\|e^{itQ_M}\|_{[4]}
 \ \le\exp\{K_{\sigma,r}U^{1/\sigma}(\log U)^5\}.}
 \tag{11}
\]

The algebra bound `exp(|t| ||Q||_[4])` alone would be too expensive for
a nonanalytic test. The improvement uses the number of active prime
coordinates and the decay of the omitted Euler coefficients together.

First, integer-sum comparison and `Lambda(n)<=log n` give

\[
 \|Q-Q_M\|_{[4]}
 \le K_{\sigma,r}M^{1-\sigma}(\log(2M))^5.
 \tag{12}
\]

Indeed `H(n/m)<=nm` and
`(1+log(nm))^4<=(1+log n)^4(1+log m)^4`. Sum the positive
coefficients over pairs with at least one index exceeding `M`.
The unrestricted weighted factor is finite, and the other factor is
bounded by `sum_(n>M) n^(-sigma)(log(2n))^5`, which has the order in
(12). Thus `Q_M->Q` in (4).

For the finite polynomial `Q_M`, let `d` be the number of primes at
most `M`; the crude bound `d<=M` suffices. Regard its Fourier polynomial
as holomorphic in the complex angles. This is the Laurent extension
of (1), not the expression `||V(z)||^2` evaluated at nonunit `z`.
There are constants `rho_0>0,K_sigma,r` independent of `M,d` such that

\[
 |\operatorname{Im} Q_M(\theta+i y)|\le K_{\sigma,r}\rho
 \quad\text{if }\max_p|y_p|\le\rho\le\rho_0.
 \tag{13}
\]

To verify this uniformly, the exponent vector of `n/m` has `ell^1`
length at most `(log n+log m)/log 2`. Choose
`rho_0<=((sigma-1)log 2)/4`. The difference from the real-angle
polynomial is bounded by

\[
 \frac{\rho}{\log2}\sum_{n,m}a_na_m
  (\log n+\log m)(nm)^{\rho_0/\log2}<K_{\sigma,r}\rho.
 \tag{14}
\]

All factors converge since `sigma-rho_0/log2>1`.
Take `rho=min(rho_0,1,1/U)`. Equation (13) bounds
`|exp(it Q_M)|` on that polystrip by a fixed constant. Moving each
Fourier contour according to the sign of its integer exponent gives

\[
 |\widehat{e^{itQ_M}}(k)|\le K_{\sigma,r}e^{-\rho|k|_1},
 \qquad k\in\mathbb Z^d.
 \tag{15}
\]

For this character `log H<=|k|_1 log M`. The geometric series and its
fourth moment yield

\[
 \sum_{k\in\mathbb Z^d} e^{-\rho|k|_1}
                  (1+|k|_1\log M)^4
 \le K(C/\rho)^d(1+d\log M/\rho)^4.
 \tag{16}
\]

For example, normalize the product geometric weights to probability:
each `|k_p|` has fourth moment `O(rho^(-4))`, and Minkowski gives
`E|k|_1^4=O(d^4 rho^(-4))`. Its normalizing mass is at most
`(C/rho)^d`. Thus, at any finite cutoff,

\[
 \|e^{itQ_M}\|_{[4]}
 \le K_{\sigma,r}(C_{\sigma,r}U)^d
                 (1+C_{\sigma,r}dU\log M)^4.
 \tag{17}
\]

Now choose `M_0=max(2,ceil(U^(1/sigma)))`. In the commutative algebra,

\[
 e^{itQ}=e^{itQ_{M_0}}e^{it(Q-Q_{M_0})},\qquad
 \|e^{it(Q-Q_{M_0})}\|_{[4]}
 \le\exp\{|t|\|Q-Q_{M_0}\|_{[4]}\}.
 \tag{18}
\]

The logarithm of (17) costs `O_sigma,r(M_0 log U)`.
Equations (12) and (18) cost
`O_sigma,r(U M_0^(1-sigma)(log(2M_0))^5)`.
Both are bounded by the exponent in (11). To prove the uniform
finite-panel statement, split a panel at `min(M,M_0)`. If `M<M_0`,
use (17) directly. Otherwise its tail has coefficient norm bounded by
(12) at `M_0`, because the coefficients being omitted are nonnegative.
This establishes both assertions in (11).

## Gevrey summation and identification of the correction

With `t_j=pi j/2`, (2) and (11) imply

\[
 \sum_j |c_j|\sup_M\|e^{it_jQ_M}\|_{[4]}<\infty,
 \qquad \sum_j|c_j|\|e^{it_jQ}\|_{[4]}<\infty,
 \tag{19}
\]

because `1/s>1/sigma`. Consequently `f(Q)` belongs to (4).
For fixed `j`, algebra continuity of the exponential and (12) give
`e^(it_jQ_M)->e^(it_jQ)` in (4); dominated summation in (19) gives
`f(Q_M)->f(Q)` in the same norm. Pointwise these are the usual scalar
compositions, by absolute convergence of (2).

Write `d_(M,u),d_u` for their rational Fourier coefficients. Since
`kappa` is bounded, the coefficient functional converges:

\[
 -\sum_u d_{M,u}\kappa(u)\longrightarrow-\sum_u d_u\kappa(u).
 \tag{20}
\]

For the finite panel, Fourier orthogonality identifies its left side
with `integral f(Q_M) h_M dm`, where
`h_M=-2 sum_(p<=M) log p sum_(j>=1) p^(-j/2) cos(j theta_p)`.
WI-464 proves this equals `-integral f'(x)C_M(x)dx` and that
`C_M->C` in `L^1`. The derivative of this fixed Gevrey test is bounded,
so (20) is exactly `mathcal L(f)` in (3). Applying (6) and (10) proves
the theorem. No infinite signed density `sum_p h_p` is asserted.

The class really contains localized cutoffs. One direct classical
construction starts with centered uniform probability laws of widths
`b_j=c j^(-s)`, `s>1`. Their infinite convolution has compact support
since `sum b_j<infinity`. Its Fourier transform is a product of sinc
factors. For each sufficiently large `|t|`, at least
`c'|t|^(1/s)` factors have `b_j|t|/2>=2`, hence modulus at most `1/2`.
The product is therefore bounded by `exp(-c''|t|^(1/s))`; Fourier
inversion gives a nonnegative smooth compactly supported density.
Convolving an interval indicator with a suitably rescaled such density
and then periodizing gives a test in (2), valued in `[0,1]`, equal to
one on any chosen interior interval and zero outside a slightly larger
one within `[0,q_*]`. The transition widths can be arbitrarily small
but are fixed.

## Prior art, falsification controls, and remaining boundary

The arithmetic input is classical: Ford–Meng–Zaharescu,
*Simultaneous distribution of the fractional parts of Riemann zeta
zeros*, **Bull. London Math. Soc. 49** (2017), 1–9,
[Lemmas 1–2](https://arxiv.org/pdf/1511.06814), together with the
uniform Landau formula of Ford–Zaharescu,
*On the distribution of imaginary parts of zeros of the Riemann zeta
function*, **J. reine angew. Math. 579** (2005), 145–158,
[Lemma 1](https://ford126.web.illinois.edu/wwwpapers/fz.pdf).
The larger rational cutoff in (8) is checked directly against their
range. Their fixed-dimensional smooth-test theorem is not an
infinite-dimensional composition estimate.

Gevrey Fourier decay is classical; see Dasgupta–Ruzhansky,
*Gevrey functions and ultradistributions on compact Lie groups and
homogeneous spaces*, **Bull. Sci. Math. 138** (2014), 756–782,
[Theorem 2.3](https://arxiv.org/pdf/1208.1883), specialized to the
circle. Nonanalytic functional calculus in weighted group algebras is
also established background; compare Dziubański–Ludwig–Molitor-Braun,
*Functional calculus in weighted group algebras*, **Rev. Mat. Complut.
17** (2004), 321–357,
[publisher abstract](https://www.mat.ucm.es/serv/revista/vol17-2/vol17-2d.html).
That paper's compactly generated polynomial-growth group framework is
not directly an assertion about the infinite-rank rational character
group here. The source-specific estimates (11)–(19) are supplied
explicitly; no general functional-calculus novelty or literature
priority is claimed.

The substantive local delta is the nonanalytic, exact-plateau test
class for the full Euler series, with a quantitative arithmetic error.
WI-465's positive power of rational height would require exponential
Fourier decay along each prime axis and did not establish this class.
The weaker logarithmic height norm and the source's finite-panel/tail
balance pay a different, sufficient cost.

The following limitations survive all of the estimates:

- The threshold `s<sigma` and the logarithmic power five are sufficient
  bounds, not optimality claims. Nothing here proves failure at
  `s>=sigma`, or transport for arbitrary `C^infinity` or Lipschitz tests.
- The norm in (19) depends on the full test, including its transition
  width and Gevrey constants. No bound supplied here stays uniform as
  cutoffs approach an indicator. Taking fixed-test limits in sequence
  does not commute with the height limit at order `T`. The hard-threshold
  problem in WI-463 remains open to different arithmetic input.
- All constants are at fixed `sigma>1,r>0`. In particular, the analytic
  strip (13), the tail constant (12), and the margin `1/s-1/sigma`
  degenerate in possible pole-limit regimes. No joint limit is proved.
- Prime-only responses have zero correction for this whole class:
  common rotation preserves the response and kills all nonconstant
  prime-axis characters. Diagonal responses are constant. The theorem
  does not create a correction without prime-power coherence or force
  its sign for localized tests.
- Sampling counts all zero ordinates with multiplicity. Statistical
  correction at order `T` does not distinguish a fixed or sufficiently
  sparse off-critical divisor, prove universal simplicity, or improve a
  simple-critical proportion.

The decisive audit points are summing the individual logarithmic
comparison errors in (8), keeping original panel normalization,
the dimension-independent strip estimate (14), paying the factor
`(C/rho)^d` in (16), and domination uniform in the panel in (19).
This is an analytic derivation with checked primary-source hypotheses;
no numerical, Lean, or independent adversarial certification is claimed.
The bounded investigation closes at this enlarged test class. No
separate finite formalization target with a presently identified
verification or fertility advantage is selected from its elementary
coefficient algebra.
