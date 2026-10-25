# FD-342 — Log-weighted divisor control saturates every linear Farey band

**Status:** LITERATURE+DERIVED + UNCONDITIONAL-FOURIER-TAIL-BOUND + FULL-SPECTRUM-RELATIVE-TRANSFER.

For the genuine order-`Q` Farey sequence, the position-Fourier energy above any fixed positive multiple of `Q` is `O(1/Q)`. The total Franel energy satisfies `Q E_Q -> infinity` by FD-033 and FD-341. Consequently every fixed linear band captures asymptotically all the energy, in both position and rank coordinates. The same tail bound upgrades FD-341's fixed-linear-cutoff coefficient transfer to relative `l^2` transfer of the entire rank spectrum, extended by zero beyond its last mode.

The new input is an absolutely convergent, logarithmically weighted divisor correlation. It uses only the classical unconditional estimate `M(y) << y/log^2(2y)`. It does not bound the total energy from above, improve the Franel exponent, or determine the energy shares at either predeclared sublinear cutoff.

## 1. Exact objects and conclusions

Write `M(y)=sum_(n<=y) mu(n)`. Use the conventions of FD-337 and FD-341:
\[
0=x_0<x_1<\cdots<x_N=1,\qquad
N=\sum_{b\le Q}\varphi(b),\quad Q\ge3,
\]
\[
D_k=x_k-k/N,\qquad E_Q=\sum_{k=1}^{N-1}D_k^2,
\qquad K_Q=QE_Q,
\]
\[
B_Q(j)=\sum_{\substack{b\mid j\\b\le Q}}bM(\lfloor Q/b\rfloor),
\qquad a_j=-\frac{B_Q(j)}{\pi j\sqrt{2N}},
\]
\[
d_{2j}=\sqrt{2/N}\sum_{k=1}^{N-1}D_k\sin(2\pi jk/N),
\qquad 1\le j<N/2.
\tag{1}
\]
Here `N` is even. Set `tilde d_j=d_(2j)` for `1<=j<N/2` and `tilde d_j=0` otherwise, and write `T_q=sum_(j<=q) a_j^2`. Reflection and the exact Franel identity give
\[
\sum_{j\ge1}\widetilde d_j^2=E_Q,\qquad
T_\infty:=\sum_{j\ge1}a_j^2=E_Q+\frac1{12N}.
\tag{2}
\]

Define `log_+(t)=max(0,log t)` and
\[
L(t)=1+\frac{\log_+t}{\log2}.
\]
There is an absolute constant `C`, independent of `Q` and the integer cutoff `q>=1`, such that
\[
\boxed{
\sum_{j>q}\frac{B_Q(j)^2}{j^2}
\le C\frac{Q^2}{q}L(q/Q)^4.}
\tag{3}
\]
The constant includes one fixed constant in the classical Mertens log-power bound. Since `N asymp Q^2`, this implies
\[
\boxed{T_{>q}:=\sum_{j>q}a_j^2\ll\frac{L(q/Q)^4}{q}.}
\tag{4}
\]
In particular, for every fixed `c>0`, as integer `Q -> infinity`,
\[
T_{>\lfloor cQ\rfloor}=O_c(Q^{-1}),\qquad
\frac{T_{\lfloor cQ\rfloor}}{T_\infty}\longrightarrow1,
\qquad
\frac{\sum_{j\le\lfloor cQ\rfloor}d_{2j}^2}{E_Q}
\longrightarrow1.
\tag{5}
\]
The rank cutoff is below `N/2` eventually. Moreover,
\[
\boxed{
\frac1{E_Q}\sum_{j\ge1}|\widetilde d_j-a_j|^2
\longrightarrow0.}
\tag{6}
\]
Thus normalized energy shares transfer **uniformly over all integer cutoffs**, including cutoffs depending arbitrarily on `Q`:
\[
\boxed{
\sup_{q\ge0}\left|
\frac{\sum_{j\le q}\widetilde d_j^2}{E_Q}
-\frac{\sum_{j\le q}a_j^2}{T_\infty}
\right|\longrightarrow0.}
\tag{7}
\]
These are additive share and relative total-norm statements. They do not give relative accuracy for a band whose energy share vanishes.

## 2. A divisor majorant with bounded mean square

Put
\[
u(k)=\frac1{\log^2(2k)},\qquad
h(j)=\sum_{k\mid j}u(k),\qquad
C_h=\sum_{k,l\ge1}\frac{u(k)u(l)}{\operatorname{lcm}(k,l)}.
\tag{8}
\]
The double series converges. Indeed, write `k=ga,l=gb`, with `(a,b)=1`, then discard the coprimality restriction in a nonnegative sum:
\[
C_h\le\sum_{g\ge1}\frac1g
\left(\sum_{a\ge1}\frac1{a\log^2(2ga)}\right)^2.
\tag{9}
\]
The summand in the inner series decreases with `a`, so the integral test gives
\[
\sum_{a\ge1}\frac1{a\log^2(2ga)}
\le\frac1{\log^2(2g)}+
\int_1^\infty\frac{dt}{t\log^2(2gt)}
=\frac1{\log^2(2g)}+\frac1{\log(2g)}.
\tag{10}
\]
The right side of (9) is therefore bounded by a constant times
`sum_(g>=1) 1/[g log^2(2g)]`, which converges. In particular, for every real `X>=1`, expanding the finite square gives the exact identity and bound
\[
\sum_{j\le X}h(j)^2
=\sum_{k,l\le X}u(k)u(l)
\left\lfloor\frac{X}{\operatorname{lcm}(k,l)}\right\rfloor
\le C_h X.
\tag{11}
\]
There is no replacement of a floor by a main term plus an accumulated error. Positivity justifies both the upper bound and passage to the infinite series. Replacing `h` by the ordinary divisor count would lose precisely this bounded mean-square property.

## 3. Complementary divisors retain the Mertens saving

Fix `C_M` so that, for every real `y>=1`,
\[
|M(y)|\le C_M\frac{y}{\log^2(2y)}.
\tag{12}
\]
The classical asymptotic log-power bound extends to this range by enlarging its constant. Changing to the complementary divisor `k=j/b` gives the exact finite formula
\[
\frac{B_Q(j)}j
=\sum_{\substack{k\mid j\\j/k\le Q}}
\frac{M(Qk/j)}k.
\tag{13}
\]
As usual `M(y)` includes the floor in its definition. For each term, `y=Qk/j>=1`, and
\[
\log(2k)=\log(2y)+\log(j/Q)
\le L(j/Q)\log(2y).
\tag{14}
\]
For `j<=Q` this uses `L=1`; for `j>Q` it uses `log(2y)>=log 2`. Taking absolute values only after this change of divisor yields
\[
\boxed{
\left|\frac{B_Q(j)}j\right|
\le C_M\frac Qj L(j/Q)^2h(j).}
\tag{15}
\]
Thus the proof needs cancellation in `M` but no cancellation among the divisors in (13).

On `2^n q<j<=2^(n+1)q`,
`L(j/Q)<=L(q/Q)+n+1<=(n+2)L(q/Q)`. Equations (11) and (15) give
\[
\sum_{2^nq<j\le2^{n+1}q}\frac{B_Q(j)^2}{j^2}
\le 2^{1-n}(n+2)^4 C_M^2 C_h
\frac{Q^2}{q}L(q/Q)^4.
\tag{16}
\]
Summing over all `n>=0` proves (3), for example with the finite constant
\[
C=2C_M^2C_h\sum_{n\ge0}2^{-n}(n+2)^4.
\tag{17}
\]
This controls the entire infinite tail, not only a finite Fourier truncation.

## 4. Linear-band saturation and complete relative transfer

FD-341, Section 4a, proves unconditionally `K_Q -> infinity`. Its mechanism is FD-033's divergence of the critical square norm of the quotient-shell source, followed by positive Jordan-row grouping. The analytic input is the existence of a critical-line zeta zero; neither RH nor simplicity is assumed. Equation (4) now gives
\[
\frac{T_{>\lfloor cQ\rfloor}}{E_Q}\ll_c K_Q^{-1}\longrightarrow0.
\tag{18}
\]
The continuity term in (2) is negligible since `NE_Q -> infinity`. This proves the position-coordinate limit in (5). FD-341's unconditional relative coefficient transfer at the same fixed linear cutoff gives the rank-coordinate limit.

For completeness, fix only `q_0=Q` from here on, which is admissible for all sufficiently large `Q`, and write
\[
r_Q=\frac1{E_Q}\sum_{j\le Q}|\widetilde d_j-a_j|^2=o(1),
\quad t_Q=\frac{T_{>Q}}{E_Q}=O(K_Q^{-1}),
\quad s_Q=\frac{\sum_{j>Q}\widetilde d_j^2}{E_Q}.
\]
The rank head has norm at most `sqrt(E_Q)`. The triangle inequality therefore implies
\[
|T_Q-\sum_{j\le Q}\widetilde d_j^2|
\le (2\sqrt{r_Q}+r_Q)E_Q,
\qquad
s_Q\le t_Q+2\sqrt{r_Q}+r_Q.
\tag{19}
\]
In the last inequality the positive continuity correction in `T_infinity` is dropped with the favorable sign. On the remaining coordinates use `|v-w|^2<=2|v|^2+2|w|^2`:
\[
\frac{\|\widetilde d-a\|_2^2}{E_Q}
\le r_Q+2s_Q+2t_Q
\le3r_Q+4\sqrt{r_Q}+4t_Q\longrightarrow0.
\tag{20}
\]
This proves (6) without applying the Taylor/large-sieve estimate at a growing cutoff. If `epsilon_Q=||tilde d-a||_2/sqrt(E_Q)`, every coordinate prefix satisfies
\[
\left|\frac{\sum_{j\le q}\widetilde d_j^2}{E_Q}
-\frac{\sum_{j\le q}a_j^2}{T_\infty}\right|
\le2\epsilon_Q+\epsilon_Q^2+\frac1{12NE_Q},
\tag{21}
\]
uniformly in `q`. This proves (7). FD-341's estimate for `r_Q` can be retained in (20), but it still supplies no explicit rate in `Q` for `K_Q`'s divergence.

## 5. Research consequence and limitations

The normalized genuine spectrum concentrates at frequencies `j=o(Q)` in the precise sense (5): its mass above every fixed `cQ` tends to zero. This assertion does not specify a power cutoff inside that region. In particular, no limit is established at `floor(sqrt(Q))` or `floor(Q^(2/3))`. Even though (4) gives `T_(>q)/E_Q << Q/(q K_Q)` for `q<=Q`, the known divergence of `K_Q` supplies no rate that makes this bound vanish at either predeclared cutoff.

For either calibrated null in FD-335–FD-336, the null expectation share tends to one at a diverging cutoff. Hence the genuine null-normalized allocation statistic tends to one at every fixed linear cutoff. An order-one asymptotic allocation deficit cannot persist there. This says nothing about the global amplitude factor, about a new denominator-conditioned null, or about the unrun larger-order confirmation panel.

Equation (7) also removes the earlier cutoff restriction from the additive arithmetic description of the genuine rank-band shares. It creates no new arithmetic carrier: all these shares remain asymptotically represented by the same divisor-transformed Mertens spectrum. The extra information relative to scalar total energy is still the distribution of that arithmetic energy across sublinear frequencies.

FD-339's absolute coefficient-error floor is compatible with (6): an error of squared size `1/Q` is negligible relative to `E_Q`, since `K_Q -> infinity`. There is no assertion here that the **full coefficient error** itself is `O(1/Q)`; (4) controls the position tail, whereas (20) controls coefficient error only relative to total energy. Artificial rational reassemblies need not satisfy the Mertens formula or its log-power majorant and are outside the theorem. No upper bound for total Franel energy, new zero-free region, or improvement toward RH follows.

## 6. Audit and prior-art boundary

A scratch standard-library audit checked the finite divisor-count identity (11) at 36 cutoffs through 128 using the rational test weights `u(k)=1/bit_length(k)^2`. Both the exact square identity and its least-common-multiple upper bound passed; the rational weights test the counting algebra, while (9)–(10) prove convergence for the actual logarithmic weights.

For every `3<=Q<=40`, exact rational Farey enumeration verified 38 Jordan/Franel energy identities. Across 6,536 modes `1<=j<=8Q`, the complementary-divisor formula (13) held exactly, and floating-point checks verified (15) with the finite constant obtained from all arguments `Q/b` at that order. Another 152 dyadic-block checks verified the step preceding (16). Full rank Parseval was checked at all 38 orders, with maximum absolute error below `3.2e-17`. These checks guard divisor direction, floors, logarithmic comparison, endpoint normalization and the rank-mode range. They do not certify a global value of `C_M`, an infinite sum, or an asymptotic limit; those follow from the displayed proof and its cited theorem. No independent adversarial approval or Lean validation is claimed.

The sole external arithmetic estimate in the new tail argument is Davenport's classical log-power Möbius cancellation, already anchored in SOURCES.md: H. Davenport, *On Some Infinite Series Involving Arithmetical Functions (II)*, Q. J. Math. **os-8** (1937), 313–320, [DOI](https://doi.org/10.1093/qmath/os-8.1.313). Its unconditional statement is explicitly reproduced in Xiaoguang He and Bingrong Huang, *Exponential sums involving the Möbius function*, Acta Arith. **175**(3) (2016), equation (1.2), [publisher PDF](https://www.impan.pl/shop/intranet.php?h=6534c91a557d4&p=91740&t=1697958170). Only zero frequency and log exponent two are used; none of that paper's conditional estimates enters.

The least-common-multiple square expansion, GCD grouping, integral test and dyadic summation are classical. The existing Farey Fourier/total-energy literature, including M. N. Huxley, *Identities involving Farey fractions*, Proc. Steklov Inst. Math. **276** (2012), 125–139, [primary record](https://www.mathnet.ru/eng/tm3374), is the prior-art boundary for (1)–(2). Targeted searches compared Farey Fourier truncation, discrepancy spectra and weighted divisor mean squares; absence of an identical formulation is not a priority claim. The line-local delta is the uniform infinite-tail estimate (3), which makes the fixed-linear-band share converge to one and allows complete relative spectral transfer. This is an application of classical cancellation to a previously uncontrolled frequency tail, not a new Möbius cancellation theorem or a new Franel identity.
