# WI-465 — analytic Euler observables have a full first zero-sampling correction

**Status:** LITERATURE+EXACT-DERIVED + CLASSICAL-LANDAU-SPECIALIZATION + NO-NOVELTY-CLAIM + NON-RH.

**Local dependencies:** [WI-462](WI-462-prime-power-coherence-lowers-the-zero-sampled-euler-response-mean.md), for the coherent response and the rational-frequency Landau estimate; [WI-464](WI-464-full-euler-correction-has-an-integrable-threshold-primitive.md), for the integrable cumulative coefficient. [WI-463](WI-463-first-euler-threshold-correction-exceeds-logarithmic-bracket-bandwidth.md) supplies the separate hard-threshold boundary.

## Claim: arithmetic transport for a fixed analytic observable

Fix `epsilon,r>0`. On the product prime torus with probability Haar
measure `m`, use

\[
 a_n=\frac{\Lambda(n)}{A_\varepsilon n^{1+\varepsilon}},
 \quad A_\varepsilon=-\zeta'(1+\varepsilon)/\zeta(1+\varepsilon),
 \quad G_r(n,m)=e^{-r|\log(n/m)|}-(nm)^{-r},
\]
\[
 Q(z)=\sum_{n,m\ge2}a_na_mG_r(n,m)\chi_{n/m}(z),
 \qquad \chi_u(z)=\prod_p z_p^{\nu_p(u)}.
 \tag{1}
\]

Here `u` is a positive rational and only prime powers have nonzero `a_n`.
The series is absolutely convergent, `0<=Q<=q_*`, and

\[
 q_*:=Q(1)=\sum_{n,m}a_na_mG_r(n,m)\le1,
 \qquad \mu:=\int Q\,dm=\sum_n a_n^2(1-n^{-2r})>0.
 \tag{2}
\]

Along `z_p(t)=exp(-it log p)`, this is the actual Euler–Hankel response
`Q_epsilon(r,t)`. Let `D_T=N(2T)-N(T)` count **all** nontrivial zeta
zeros in the ordinate window, with multiplicity and with different real
parts counted separately even at the same ordinate.

Let `f(w)=sum_(k>=0) c_k w^k` have radius of convergence strictly larger
than `q_*`. Then, unconditionally,

\[
 \boxed{
 \sum_{T<\gamma\le2T}f(Q(\gamma))
 =D_T\int f(Q)\,dm+\frac{T}{2\pi}\mathcal L(f)+o_{f,\varepsilon,r}(T),
 \qquad
 \mathcal L(f)=-\int_0^{q_*}f'(x)C(x)\,dx.}
 \tag{3}
\]

`C` is WI-464's `L^1` cumulative coefficient, which vanishes almost
everywhere outside `[0,q_*]`. Equivalently the first correction to the
normalized average, multiplied by `log T`, tends to `mathcal L(f)`.
The Haar average may also be replaced by the continuous-height average
`T^(-1) integral_T^(2T) f(Q(t))dt`.

Thus the full infinite-panel coefficient is an **actual arithmetic
asymptotic** for this analytic class, not only a candidate Haar functional.
This includes every fixed polynomial, characteristic test `exp(iu x)`
with fixed real `u`, and exponential test `exp(sx)` with fixed real `s`.
It does not establish convergence for hard thresholds, arbitrary
Lipschitz tests, or tests whose sharpness grows with height.

## A rational-frequency norm pays the infinite-panel cost

For a reduced positive rational `u=a/b`, define its height by `H(u)=ab`.
Then `H(uv)<=H(u)H(v)` and `H(u^(-1))=H(u)`. If

\[
 F(z)=\sum_{u\in\mathbb Q_{>0}}d_u\chi_u(z),\qquad
 \|F\|_\eta:=\sum_u |d_u|H(u)^\eta<\infty
 \quad\text{for some }\eta>0,
 \tag{4}
\]

this weighted coefficient norm is submultiplicative. The constant
coefficient is `d_1=integral F dm`. Put

\[
 \kappa(u)=
 \begin{cases}
  (\log p)p^{-j/2},&u=p^j\text{ or }p^{-j},\ j\ge1,\\
  0,&\text{otherwise},
 \end{cases}
 \qquad K_0:=\sup_u\kappa(u)<\infty.
 \tag{5}
\]

We first prove the general implication

\[
 \frac1T\left\{\sum_{T<\gamma\le2T}F(z(\gamma))-D_Td_1\right\}
 \longrightarrow-\frac1{2\pi}\sum_u d_u\kappa(u).
 \tag{6}
\]

Truncate (4) at `H(u)<=X`, writing `F_X` for the result. There are only
finitely many such rationals, and

\[
 \|F-F_X\|_\infty\le X^{-\eta}\|F\|_\eta.
 \tag{7}
\]

For a retained `u!=1`, replace it by its reciprocal if needed, obtaining
`x=a/b>1` with `a,b<=X`. The uniform Landau formula and unconditional
weighted-zero/ordinate comparison give

\[
 \frac1T\sum_{T<\gamma\le2T}e^{\pm i\gamma\log x}
 =-\frac{\Lambda_*(x)}{2\pi\sqrt x}+O(E(T,X)),
 \tag{8}
\]
\[
 E(T,X)=\frac{(\log X)^2}{\log T}+\frac1{(\log T)^{10}}
       +\frac{X\log^2(2XT)+X^2\log(2X)}{T},
 \qquad X=(\log T)^B,
 \tag{9}
\]

where `B>0` is fixed and `Lambda_*(x)` is `log p` at an integer prime
power `p^j`, and zero otherwise. WI-462 gives the real-part version;
the same source lemmas give (8) as a complex estimate. The resonant main
term is real, and the nonresonant main term is bounded in complex modulus.
Negative frequencies follow by conjugation.

For completeness the separation facts remain valid when `b=1` in the
fraction `a/b` (unlike the initial prime-power pair notation). If `n_x`
is a nearest prime power and `x!=n_x`, then

\[
 |x-n_x|\ge1/X,\quad n_x\le2x\le2X,\quad
 |\log(x/n_x)|\ge(2X^2)^{-1},\quad \log x\ge X^{-1}.
 \tag{10}
\]

These bound the nonresonant Landau term by `O(X^2 log(2X))` and its
error by `O(X log^2(2XT))`. The comparison lemma applies because
`X<=exp(log T/(50 log log T))` eventually for every fixed exponent `B`.
Apply both source lemmas at `2T` and `T` and subtract. At resonance the
dyadic main term is `-T Lambda_*(x)/(2 pi sqrt(x))`.

Summing (8) costs `||F||_0 E(T,X)`, with no factor for the number of
characters. Since `D_T/T=O(log T)`, (7) and the omitted resonant tail give

\[
 \left|\frac1T\left\{\sum F(z(\gamma))-D_Td_1\right\}
       +\frac1{2\pi}\sum_u d_u\kappa(u)\right|
 \ll\|F\|_\eta\{E(T,X)+(\log T)X^{-\eta}\}.
 \tag{11}
\]

Choose the fixed exponent `B` with `B eta>1`. Both errors tend to zero,
proving (6). Thus mere absolute convergence has not been substituted for
the stronger tail estimate needed at order `T`.

The same truncation proves

\[
 \left|\frac1T\int_T^{2T}F(z(t))\,dt-d_1\right|
 \le\|F\|_\eta\{2X/T+X^{-\eta}\}=o(1/\log T),
 \tag{12}
\]

because each retained nonconstant frequency has magnitude at least `1/X`.
This establishes the continuous-height centering in (3).

## Analytic composition preserves a positive weighted tail margin

Collect equal rational characters in (1), writing
`Q=sum_u q_u chi_u`. All `q_u` are nonnegative, and `q_(u^-1)=q_u`.
For `0<eta<epsilon`,

\[
 \|Q\|_\eta
 \le\sum_{n,m}a_na_mG_r(n,m)(nm)^\eta
 \le\left(\sum_n a_n n^\eta\right)^2<\infty.
 \tag{13}
\]

The final sum converges already from `Lambda(n)<=log n`. Dominated
convergence, using any fixed `eta_0<epsilon`, gives

\[
 \|Q\|_\eta\longrightarrow\|Q\|_0=q_*\qquad(\eta\downarrow0).
 \tag{14}
\]

The equality at zero uses coefficient nonnegativity, not merely the
pointwise bound `Q<=q_*`. If the radius of `f` is `R>q_*`, choose a fixed
`eta>0` sufficiently small that `||Q||_eta<R`. Submultiplicativity gives

\[
 \|f(Q)\|_\eta\le\sum_{k\ge0}|c_k|\|Q\|_\eta^k<\infty.
 \tag{15}
\]

Apply (6) to `F=f(Q)`. In particular the prime set and the order of the
analytic expansion need not be frozen before taking the height limit:
their combined tails are paid by the single fixed norm (15). This is not
an appeal to a finite-dimensional theorem with dimension-dependent
constants suppressed.

To identify the coefficient with WI-464, let `Q_M` retain prime powers
`n<=M`, with the original normalization, and write `d_(M,u)` for the
coefficients of `f(Q_M)`. The coefficient mass of `Q-Q_M` is at most
`2 delta_M`, where `delta_M=sum_(n>M) a_n`. The power-series telescoping
bound therefore gives `||f(Q_M)-f(Q)||_0 -> 0`. Hence

\[
 -\sum_u d_{M,u}\kappa(u)\longrightarrow-\sum_u d_u\kappa(u).
 \tag{16}
\]

For the finite prime set, Haar orthogonality identifies the left side as
`integral f(Q_M) h_M dm`, where

\[
 h_M=-2\sum_{p\le M}\log p\sum_{j\ge1}p^{-j/2}\cos(j\theta_p).
\]

WI-464 proves `C_M -> C` in `L^1`, with
`integral f(Q_M)h_M dm=-integral f'(x)C_M(x)dx`. Each `Q_M` lies in
`[0,q_*]`, so its cumulative coefficient is zero outside this interval;
the same holds almost everywhere for `C`. Since `f'` is bounded there,
(16) equals the functional in (3). One may extend `f` constantly beyond
`q_*` when using WI-464's formulation on `[0,1]`. No infinite signed
torus density is being asserted.

## Every fixed positive moment has a strictly negative correction

For integer `k>=1`, let `q_u^(k)` be the coefficients of `Q^k`. Then

\[
 B_k:=\sum_u q_u^{(k)}\kappa(u)>0,\qquad
 \mathcal L(x^k)=-B_k,
 \quad B_1=B_\varepsilon(r)\text{ of WI-462}.
 \tag{17}
\]

Indeed `Q=mu+R_0` has a nonconstant part with nonnegative coefficients.
Expanding its powers coefficientwise gives, at every `u!=1`,
`q_u^(k)>=k mu^(k-1) q_u`. Already the terms `n=p^2,m=p` make
`q_p>0`, since `r>0`. Consequently

\[
 \boxed{B_k\ge k\mu^{k-1}B_1>0,\qquad
        k\int_0^{q_*}x^{k-1}C(x)\,dx=B_k.}
 \tag{18}
\]

Likewise, for every fixed real `s>0`,

\[
 \mathcal L(e^{sx})=-\sum_{k\ge1}\frac{s^k}{k!}B_k<0.
 \tag{19}
\]

The exchange is absolute: `B_k<=K_0 q_*^k`. More generally the sign
holds for a real power series with nonnegative nonconstant coefficients
and at least one strictly positive such coefficient, within the radius
condition of (3). No sign is asserted for an arbitrary increasing
analytic function.

For the **prime-only** control, common rotation `z_p -> e^{i theta}z_p`
leaves the squared response, and hence every `f(Q)`, invariant. Its
Fourier coefficients vanish unless the sum of the prime exponents is
zero. Every nonconstant axis character `p^j` has nonzero exponent sum,
so all its coefficients vanish and the first correction is identically
zero for the whole analytic class. The diagonal-only control is constant
and also has zero correction. Thus (17) is not a generic norm-square
bias; it retains the same-prime-power coherence isolated by WI-462.

## Prior art, audit boundaries, and consequence

Ford–Zaharescu, *On the distribution of imaginary parts of zeros of the
Riemann zeta function*, **J. reine angew. Math. 579** (2005), 145–158,
[Lemma 1 and §3](https://ford126.web.illinois.edu/wwwpapers/fz.pdf), supply
the uniform Landau formula. Ford–Meng–Zaharescu, *Simultaneous
distribution of the fractional parts of Riemann zeta zeros*, **Bull.
London Math. Soc. 49** (2017), 1–9,
[Lemmas 1–2 and Theorem 1](https://arxiv.org/pdf/1511.06814), state the
unconditional weighted-zero/ordinate comparison and neighboring fixed
finite-dimensional smooth-test theory. The comparison includes the
`T/(log T)^10` residual and its explicit range. We retain both. Its
zero-density input, rather than an assumption about the zeros' real
parts, is why (8) is unconditional.

The coefficient-norm algebra, analytic power-series composition and
prime-axis correction are classical mechanisms. Equations (4)–(16)
prove their infinite Euler-series specialization directly. This is a
stronger local theorem than WI-462's single mean asymptotic and
WI-464's candidate coefficient construction; it is not a new Landau
formula, a new density theorem, or a claim of literature priority.

Ford–Soundararajan–Zaharescu, *On the distribution of imaginary parts of
zeros of the Riemann zeta function, II*, **Math. Ann. 343** (2009),
487–505, [§1](https://arxiv.org/pdf/0805.2745), and WI-463 distinguish
smooth sampling corrections from interval indicators. The present
argument does not supply their missing interval control. In particular:

- Polynomials determine a probability law on a compact interval, but
  the scaled signed sampling errors are not probability laws. Their
  total variation need not be uniformly bounded. Approximation by
  fixed polynomials followed by a height limit does not prove a first
  threshold correction or convergence in the Lipschitz-dual norm.
- The inequalities (18)–(19) do not imply `C>=0` almost everywhere or
  stochastic dominance. Positivity of all its power moments is weaker
  than positivity against every nonnegative test.
- The norm exponent `eta`, analytic radius, coefficients and parameters
  are fixed before `T` tends to infinity. No uniform sharp-threshold,
  pole-limit, growing-moment-order, or shrinking-width assertion follows.
- All ordinates and multiplicities are sampled. Changing `o(T)` entries
  and the corresponding count in a dyadic window changes (3) by `o(T)`
  for any fixed bounded `f(Q)`. This observation concerns statistical
  information loss, not admissible modifications of the actual zeta
  divisor. Individual or sufficiently sparse off-line defects remain
  outside the conclusion.

The decisive checks are reduced-rational height submultiplicativity,
the near-one and near-prime-power separations (10), the order-`T` tail
charge in (11), the dyadic `2 pi` factor, coefficient nonnegativity in
(14) and (18), and identifying the same `C` without a nonexistent
infinite torus density. The proof is analytic; no numerical or Lean
verification is claimed. The elementary algebra alone offers no
separate formalization-fertility target, while the arithmetic input
remains the classical analytic theorem.

The coherent investigation closes at fixed analytic observables. It
calibrates their arithmetic sampling bias beyond the mean while leaving
the hard-threshold and individual-defect problems distinct. No improved
simple-critical proportion or RH conclusion follows.
