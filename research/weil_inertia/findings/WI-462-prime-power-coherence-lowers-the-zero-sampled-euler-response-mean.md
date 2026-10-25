# WI-462 — prime-power coherence lowers the zero-sampled Euler-response mean

**Status:** LITERATURE+EXACT-DERIVED + CLASSICAL-LANDAU-SPECIALIZATION + NO-NOVELTY-CLAIM + NON-RH

**Local dependencies:** [WI-457](WI-457-normalized-euler-hankel-symbols-have-local-blindness-and-recurrent-peaks.md), for the Euler–Hankel response and its coherent expansion; [WI-458](WI-458-euler-hankel-peaks-have-exponentially-small-height-density.md), for its height mean; [WI-461](WI-461-fixed-scale-euler-peaks-have-positive-density-at-zeta-zero-ordinates.md), for the leading zero-sampled Haar law.

## Claim: the first mean correction is strictly negative

Fix \(\varepsilon,r>0\), put \(\sigma=1+\varepsilon\), and use
\[
A_\varepsilon=-\zeta'(1+\varepsilon)/\zeta(1+\varepsilon),\qquad
a_n=\frac{\Lambda(n)}{A_\varepsilon n^\sigma},\qquad
\varphi_\varepsilon(t)=\sum_{n\ge2}a_ne^{-it\log n}.
\]
Thus \(a_n\ge0\) and \(\sum a_n=1\). With the Fourier phase
\(e^{-it\xi}\), let
\[
k_{r,t}(u)=\frac{\sqrt{r/\pi}}{r-i(u-t)},\qquad
Q_\varepsilon(r,t)=\|P_-(\varphi_\varepsilon k_{r,t})\|_2^2.
\]
Write \(\rho=\beta+i\gamma\), and let \(N(T)\) count all nontrivial zeta zeros with
\(0<\gamma\le T\), counting multiplicity and counting zeros with different
real parts separately even when their ordinates agree. Put
\(D_T=N(2T)-N(T)\). Define
\[
\mu_\varepsilon(r)=\sum_{n\ge2}a_n^2(1-n^{-2r}).
\tag{1}
\]
Unconditionally, at these **fixed** parameters,
\[
\boxed{
\sum_{T<\gamma\le2T}Q_\varepsilon(r,\gamma)
=D_T\mu_\varepsilon(r)-\frac{T}{2\pi}B_\varepsilon(r)+o_{\varepsilon,r}(T),
\qquad B_\varepsilon(r)>0.}
\tag{2}
\]
The correction has the explicit absolutely convergent prime series
\[
\boxed{
B_\varepsilon(r)=\frac{2}{A_\varepsilon^2}\sum_p(\log p)^3
\frac{p^{-(\sigma+r+1/2)}}{1-p^{-(\sigma+r+1/2)}}
\left\{\frac{p^{-2\sigma}}{1-p^{-2\sigma}}
-\frac{p^{-(2\sigma+2r)}}{1-p^{-(2\sigma+2r)}}\right\}.}
\tag{3}
\]
In particular, since \(D_T\sim T\log T/(2\pi)\),
\[
\log T\left\{\frac1{D_T}\sum_{T<\gamma\le2T}Q_\varepsilon(r,\gamma)
-\mu_\varepsilon(r)\right\}\longrightarrow-B_\varepsilon(r)<0.
\tag{4}
\]
The same correction holds if the subtracted mean in (4) is replaced by
\(T^{-1}\int_T^{2T}Q_\varepsilon(r,t)\,dt\).

The leading Haar law therefore misses a signed arithmetic correlation. Its
first mean correction favors smaller response, and comes entirely from
coherence between different powers of the **same** prime. This is a bulk
sampling statement, not an inequality at an individual zero or a statement
about the off-line subpopulation.

## A uniform rational-frequency interface

For real \(x>1\), set \(\Lambda_*(x)=\log p\) if \(x=p^j\) for a prime
\(p\) and integer \(j\ge1\), and zero otherwise. The required source input
is the uniform Landau formula in Ford–Zaharescu, Lemma 1, and the unconditional
ordinate/weighted-zero comparison in Ford–Meng–Zaharescu, Lemma 2. The latter
states, for \(1<x\le\exp(\log U/(50\log\log U))\),
\[
\sum_{0<\gamma\le U}(x^{i\gamma}-x^{\rho-1/2})
\ll\frac{U(\log x)^2}{\log U}+\frac{U}{(\log U)^{10}}.
\tag{5}
\]
No assumption \(\beta=1/2\) is made: this comparison uses functional-equation
pairing and a Selberg zero-density bound.

Here is the precise specialization that permits an infinite response rather
than just a fixed trigonometric polynomial. Fix \(b>0\), set
\(X=(\log T)^b\), and consider integers \(2\le m<n\le X\). Uniformly for
\(x=n/m\), applying those two lemmas at \(U=2T,T\) gives
\[
\frac1T\sum_{T<\gamma\le2T}\cos(\gamma\log x)
=-\frac{\Lambda_*(x)}{2\pi\sqrt{x}}+O(E(T,X)),
\tag{6}
\]
where one may take
\[
E(T,X)=\frac{(\log X)^2}{\log T}+\frac1{(\log T)^{10}}
+\frac{X\log^2(2XT)+X^2\log(2X)}{T}=o(1).
\tag{7}
\]

To check the uniformity, let \(n_x\) be the nearest prime power to \(x\).
The Landau main term before multiplication by \(x^{-1/2}\) is
\[
-\frac{\Lambda(n_x)}{2\pi}
\frac{e^{iU\log(x/n_x)}-1}{i\log(x/n_x)}.
\]
At \(x=n_x\) it equals \(-U\Lambda(x)/(2\pi)\). Otherwise rationality
gives \(|x-n_x|\ge1/m\ge1/X\). Also \(n_x\le2x\le2X\), by the powers
of two, so
\[
|\log(x/n_x)|\ge\frac1{2X^2},\qquad
\log x\ge\frac{n-m}{n}\ge\frac1X.
\tag{8}
\]
The nonresonant main term is therefore \(O(X^2\log(2X))\), and the Landau
error, after multiplication by \(x^{-1/2}\le1\), is
\(O(X\log^2(2XT))\). Equation (5) supplies the first two errors in (7).
The source range in (5) contains every \(x\le X\) for sufficiently large
\(T\) at each fixed \(b\). Subtracting the two cumulative sums gives exactly
the dyadic coefficient \(-T/(2\pi)\), not \(-2T/(2\pi)\).

## Passing to the full coherent response

The tone Gram factor is
\[
G_r(n,m)=e^{-r|\log(n/m)|}-(nm)^{-r}\in[0,1].
\]
WI-457's projection calculation gives
\[
Q_\varepsilon(r,t)=\mu_\varepsilon(r)
+2\sum_{n>m\ge2}a_na_mG_r(n,m)\cos(t\log(n/m)).
\tag{9}
\]
This is absolutely and uniformly convergent. Its off-diagonal coefficient
mass is at most one; averaging (6) consequently costs \(O(E(T,X))\), with
no factor for the number of pairs.

Let \(Q_X\) be the squared norm with only \(n\le X\) in the symbol, and
\(\mu_X\) the corresponding diagonal sum. The coefficient tail obeys
\[
\delta_X=\sum_{n>X}a_n\ll_\varepsilon X^{-\varepsilon}\log(2X),
\quad \|Q-Q_X\|_\infty\le2\delta_X,
\quad |\mu-\mu_X|\le\delta_X.
\tag{10}
\]
The first inequality follows already from \(\Lambda(n)\le\log n\); the
second follows by comparing two vectors of norm at most one. Choose
\(b\varepsilon>1\). Since \(D_T/T\ll\log T\), (10) makes the difference
between
\(T^{-1}(\sum Q-D_T\mu)\) and
\(T^{-1}(\sum Q_X-D_T\mu_X)\) tend to zero. Thus the infinite truncation
error is controlled at the **order \(T\)** scale, not just at order
\(T\log T\).

Equations (6)–(10) give (2), initially with
\[
B_\varepsilon(r)=2\sum_{n>m\ge2}a_na_mG_r(n,m)
\frac{\Lambda_*(n/m)}{\sqrt{n/m}}.
\tag{11}
\]
Convergence follows from the coefficient-mass bound and boundedness of
\(\Lambda_*(x)/\sqrt x\) on \(x>1\). This also justifies removing the
cutoff from the resonant term.

For the continuous-height average, every truncated nonconstant character
has average at most \(2/(T|\log(n/m)|)\le2X/T\). The same tail bound (10)
therefore proves
\[
\frac1T\int_T^{2T}Q_\varepsilon(r,t)\,dt
-\mu_\varepsilon(r)=o_{\varepsilon,r}(1/\log T).
\tag{12}
\]
This proves the continuous-mean version of (4) for every fixed positive
\(\varepsilon\), without a uniformity claim as \(\varepsilon\) tends to zero.

## Same-prime powers are exactly the surviving arithmetic terms

In (11), both \(n\) and \(m\) are prime powers. Their ratio is an integer
prime power precisely when
\(n=p^{\ell+j},m=p^\ell\), with \(\ell,j\ge1\). Unique factorization
excludes all distinct-prime pairs. For the surviving terms,
\[
a_na_mG_r(n,m)\frac{\Lambda_*(n/m)}{\sqrt{n/m}}
=\frac{(\log p)^3}{A_\varepsilon^2}
p^{-2\sigma\ell}(1-p^{-2r\ell})
p^{-j(\sigma+r+1/2)}.
\tag{13}
\]
Summing the two geometric series proves (3). Every summand is positive;
already \(m=p,n=p^2\) gives strict positivity for every \(r>0\).

Two controls separate the mechanism. Deleting all off-diagonal terms makes
the response the constant \(\mu\) and removes the correction identically.
Keeping the coherent Hankel response but retaining only primes, with
coefficients \(a_p\) and the original normalization, also gives zero
order-\(1/\log T\) correction: distinct primes have no prime-power ratio.
The proof above applies to that subseries with its own diagonal mean.
Thus the negative sign is not a generic consequence of a positive norm or
the leading equidistribution law; it uses prime-power coherence.

For comparison with the shallow scale, fix \(q>0\) and only **after** taking
the height limit let \(r=q\varepsilon\), \(\varepsilon\downarrow0\). Formula
(3) and \(A_\varepsilon^{-2}=\varepsilon^2(1+O(\varepsilon))\) give
\[
B_\varepsilon(q\varepsilon)=4q\varepsilon^3 C_B+O_q(\varepsilon^4),
\quad
C_B=\sum_p\frac{(\log p)^4p^{-7/2}}
{(1-p^{-3/2})(1-p^{-2})^2}>0.
\tag{14}
\]
Indeed the bracket in (3) is
\(2q\varepsilon(\log p)p^{-2}/(1-p^{-2})^2+O_q(\varepsilon^2(\log p)^2p^{-2})\);
the other factor tends to \(p^{-3/2}/(1-p^{-3/2})\). Summable logarithmic
majorants justify the expansion. WI-458's mean is also cubic, namely
\[
\mu_\varepsilon(q\varepsilon)=2q\varepsilon^3
\sum_p\frac{(\log p)^3p^{-2}}{(1-p^{-2})^2}+O_q(\varepsilon^4).
\tag{15}
\]
Both coefficients are positive and finite. Their comparable parameter
scale does not remove the extra factor \(1/\log T\) in the sampling bias.
No simultaneous shrinking-parameter asymptotic is asserted.

## Consequence, audit boundary, and prior art

The exact delta from WI-461 is a signed first correction to its leading
response law, with an infinite-series error budget and an explicit
same-prime-power formula. The negative correction coexists with that
finding's positive frequency of rare peaks; a mean bias is not stochastic
dominance or a threshold-by-threshold inequality.

This correction is unconditional and fully compatible with RH. It averages
all zeros, does not distinguish their real parts or simplicity, and leaves
the response at every selected exceptional zero uncontrolled. A finite
change in an ordinate multiset cannot alter (2): once the dyadic window
passes that finite set it changes nothing. More generally, changing
\(o(T)\) entries in a dyadic window alters both the bounded response sum and
the diagonal centering by only \(o(T)\). This is an information boundary of
the statistic, not a claim that modified multisets satisfy zeta's explicit
formula. Zero-density exceptions of that size remain invisible even after
retaining this first arithmetic correction.

The load-bearing checks are the unconditional comparison (5), the near-one
and near-prime-power separations (8), paying \(\log T\,\delta_X\) before
removing the cutoff, the dyadic \(2\pi\) normalization, and retaining the
same-prime powers in (13). No numerical experiment or formal proof is used.
The geometric sums are routine; formalizing them alone would not verify the
analytic sampling input or supply a separate structural fertility target.

Kevin Ford and Alexandru Zaharescu, *On the distribution of imaginary parts
of zeros of the Riemann zeta function*, **J. reine angew. Math. 579** (2005),
145–158, [arXiv:math/0405459v2](https://arxiv.org/abs/math/0405459v2), Lemmas
1–2 and §3, supply the Landau and zero-density framework. Kevin Ford,
Xianchang Meng and Alexandru Zaharescu, *Simultaneous distribution of
fractional parts of Riemann zeta zeros*, **Bull. London Math. Soc. 49** (2017),
1–9, [arXiv:1511.06814v2](https://arxiv.org/abs/1511.06814v2), Lemma 2,
states (5) with its uniform range and residual error; Theorem 1 and Corollary
1.1 supply neighboring finite-dimensional lower-order sampling theory.

Hung M. Bui, Alexandra Florea and Micah B. Milinovich, *Negative discrete
moments of the derivative of the Riemann zeta-function*, **Bull. London Math.
Soc. 56** (2024), 2680–2703,
[Theorem 3.1](https://doi.org/10.1112/blms.13092), is a particularly close
scalar Dirichlet-polynomial mean formula with the same prime-power
off-diagonal mechanism. That theorem assumes RH and allows a different
length/error regime. It is not an input to (2): the unconditional comparison
(5) suffices here because the fixed absolutely convergent symbol permits
polylogarithmic truncation. This does not remove RH from their stated theorem.

Prime-resonant lower-order bias is established prior art. The new local
calculation specializes that classical mechanism to this coherent
Euler–Hankel observable and proves the full-series passage; it is not a new
Landau theorem, new zero-density result, or claim of literature priority.
Neither a better critical-line proportion nor exclusion of a single
off-critical zero follows.
