# PF-300 — prime seam weights realize logarithmic quadrature with a beta-one loss threshold

**Status:** `EXACT-DERIVED + ASYMPTOTIC-QUADRATURE + RETURN-ACCUMULATION-THRESHOLD + ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-299-prime-seam-scale-has-critical-ell-one-accumulation|PF-299]] shows that the tight-pant seam scale

\[
s_n=\frac{h_n+h_{n+1}}2,
\qquad
h_n=F(p_n)-F(p_{n-1}),
\qquad
F(x)=\log\cot\frac{\pi}{x},
\]

lies in every `\ell^q`, `q>1`, but not in `\ell^1`. That identifies linear seam loss as an endpoint, but it does not yet resolve **logarithmic improvements of the endpoint**. The exact ordered prime coordinate gives a sharper answer without using any further prime-distribution theorem.

Put

\[
t_n:=F(p_n),
\qquad
h_n=t_n-t_{n-1}.
\]

PF-299 gives `t_n\to\infty` and `h_n\to0`. For every nonnegative nonincreasing function `\phi` on a tail of `[0,\infty)`, the seam-weighted sum

\[
\sum_n s_n\phi(t_n)
\]

has exactly the same convergence behavior as

\[
\int^\infty \phi(t)\,dt.
\]

More precisely, the symmetric seam weights are the average of a right and a left Riemann sum in the intrinsic coordinate `t=F(p)`, with a tail error controlled by the maximal mesh size. Consequently

\[
\boxed{
\sum_n \frac{s_n}{(1+F(p_n))^\beta}
\begin{cases}
=\infty,&0\le\beta\le1,\\
<\infty,&\beta>1.
\end{cases}}
\]

Since `F(p)=\log(p/\pi)+O(p^{-2})`, the same threshold may be written with `(\log p_n)^{-\beta}`. In particular, suppressing PF-298's linear seam loss by **one power of `\log p_n` is still not enough** to make the accumulated loss finite; any fixed power strictly greater than one is enough.

This sharpens the scalar sub-gate of `CLUE-source-weighted-return-potential-controls-mixed-response`. The next pant calculation need not be forced into the coarse dichotomy “linear in `s_n` versus a power `s_n^{1+\delta}`.” If the relative killing has the form

\[
\frac{\kappa_n}{c_n}
\asymp
s_n\,\phi(F(p_n)),
\]

then its accumulated constant-channel effect is governed by the ordinary integral of `\phi`. Prime-gap irregularity has already been absorbed into the exact mesh `dt=h_n` at this stage.

## Claim

Let

\[
t_n:=F(p_n),
\qquad
F(x):=\log\cot\frac{\pi}{x},
\qquad
h_n:=t_n-t_{n-1},
\qquad
s_n:=\frac{h_n+h_{n+1}}2.
\tag{1}
\]

After a finite head, PF-299 gives

\[
h_n>0,
\qquad
h_n\to0,
\qquad
t_n\to\infty.
\tag{2}
\]

Let `\phi:[T,\infty)\to[0,\infty)` be nonincreasing. Then, after choosing `N` with `t_{N-1}\ge T`,

\[
\boxed{
\sum_{n=N}^\infty s_n\phi(t_n)<\infty
\iff
\int_{t_{N-1}}^\infty\phi(t)\,dt<\infty.
}
\tag{3}
\]

There is a quantitative finite-interval comparison. Define

\[
\delta_N:=\sup_{n\ge N}h_n,
\tag{4}
\]

so `\delta_N\to0`. For `M\ge N`, put

\[
S_{N,M}:=\sum_{n=N}^M s_n\phi(t_n),
\]

\[
I^-_{N,M}:=\int_{t_{N-1}}^{t_M}\phi(t)\,dt,
\qquad
I^+_{N,M}:=\int_{t_N}^{t_{M+1}}\phi(t)\,dt.
\tag{5}
\]

Then

\[
\boxed{
\left|
S_{N,M}-\frac{I^-_{N,M}+I^+_{N,M}}2
\right|
\le
\frac{\delta_N\phi(t_{N-1})+\delta_{N+1}\phi(t_N)}2.
}
\tag{6}
\]

For

\[
\phi_\beta(t):=(1+t)^{-\beta},
\qquad \beta\ge0,
\tag{7}
\]

this implies

\[
\boxed{
\sum_n s_n\phi_\beta(t_n)
\text{ diverges exactly for }0\le\beta\le1.
}
\tag{8}
\]

It also gives the asymptotic calibration

\[
\sum_{n=N}^M \frac{s_n}{(1+t_n)^\beta}
\sim
\begin{cases}
\dfrac{(1+t_M)^{1-\beta}}{1-\beta},&0\le\beta<1,\\[1.1ex]
\log(1+t_M),&\beta=1,
\end{cases}
\qquad M\to\infty,
\tag{9}
\]

and, for `\beta>1`,

\[
\boxed{
\sum_{n=N}^\infty \frac{s_n}{(1+t_n)^\beta}
\sim
\frac{(1+t_N)^{1-\beta}}{\beta-1}
\qquad(N\to\infty).
}
\tag{10}
\]

The choices `t_N` versus `t_{N-1}` in the tail equivalent are immaterial because `h_N\to0` while `t_N\to\infty`.

## 1. The seam sum is an intrinsic Riemann quadrature

Split the symmetric weight exactly as

\[
S_{N,M}
=
\frac12\sum_{n=N}^M h_n\phi(t_n)
+
\frac12\sum_{n=N}^M h_{n+1}\phi(t_n).
\tag{11}
\]

The first term is a right-endpoint Riemann sum for the partition intervals `[t_{n-1},t_n]`. Monotonicity gives

\[
0\le
I^-_{N,M}-\sum_{n=N}^M h_n\phi(t_n)
\le
\sum_{n=N}^M h_n\bigl(\phi(t_{n-1})-\phi(t_n)\bigr).
\tag{12}
\]

Using `h_n\le\delta_N`, the last expression telescopes in `\phi`:

\[
0\le
I^-_{N,M}-\sum_{n=N}^M h_n\phi(t_n)
\le
\delta_N\bigl(\phi(t_{N-1})-\phi(t_M)\bigr)
\le
\delta_N\phi(t_{N-1}).
\tag{13}
\]

The second term in (11) is a left-endpoint sum for `[t_n,t_{n+1}]`. Similarly,

\[
0\le
\sum_{n=N}^M h_{n+1}\phi(t_n)-I^+_{N,M}
\le
\delta_{N+1}\phi(t_N).
\tag{14}
\]

Averaging (13) and (14) proves (6). Since `\delta_N\to0`, this is stronger than a qualitative integral test: on late tails the seam quadrature error tends to zero uniformly in the terminal index `M`.

The two comparison integrals differ only by one interval at each endpoint. Therefore they have the same finite/infinite tail behavior, which proves (3).

No regularity of `\phi` beyond monotonicity is needed. In particular, this argument does not average prime gaps probabilistically and does not invoke a prime number theorem. The only arithmetic input already established in PF-299 is that the exact logarithmic mesh size `h_n` tends to zero.

## 2. The logarithmic beta-one threshold

Take `\phi=\phi_\beta` from (7). Elementary integration gives

\[
\int^X(1+t)^{-\beta}\,dt
=
\begin{cases}
\dfrac{(1+X)^{1-\beta}}{1-\beta}+O(1),&0\le\beta<1,\\[1.1ex]
\log(1+X)+O(1),&\beta=1,
\end{cases}
\tag{15}
\]

whereas for `\beta>1`,

\[
\int_X^\infty(1+t)^{-\beta}\,dt
=
\frac{(1+X)^{1-\beta}}{\beta-1}.
\tag{16}
\]

Equation (6) transfers these asymptotics to the seam sum. For the convergent case the relative quadrature error is negligible because

\[
\frac{\delta_N(1+t_N)^{-\beta}}
     {(1+t_N)^{1-\beta}}
=
\frac{\delta_N}{1+t_N}
\longrightarrow0.
\tag{17}
\]

Finally PF-299 records

\[
F(p_n)=\log\frac{p_n}{\pi}+O(p_n^{-2}),
\tag{18}
\]

so `(1+F(p_n))^{-\beta}` and `(\log p_n)^{-\beta}` are asymptotically equivalent up to a factor tending to one. Thus the transition in (8) is genuinely a `1/\log p` endpoint refinement of PF-299's linear seam scale.

## 3. Consequence for scalar pant transmission

For the PF-298 constant compression, write

\[
\theta_n=1-\varepsilon_n,
\qquad
\varepsilon_n
=
\frac{\kappa_n}{c_n+\kappa_n},
\qquad
0<\theta_n\le1.
\tag{19}
\]

Suppose a future local calculation gives, after a finite head,

\[
\varepsilon_n
\le
C\frac{s_n}{(1+F(p_n))^\beta}
\qquad\text{for some }\beta>1.
\tag{20}
\]

Then (8) gives `\sum\varepsilon_n<\infty`, hence

\[
\boxed{\prod_n\theta_n>0.}
\tag{21}
\]

So such logarithmically suppressed killing is too small to absorb the scalar constant channel completely even though it remains only *linear* in the seam width.

Conversely, if for some `0\le\beta\le1`

\[
\varepsilon_n
\ge
c\frac{s_n}{(1+F(p_n))^\beta}
\tag{22}
\]

eventually, then (8) gives `\sum\varepsilon_n=\infty`, and therefore

\[
\boxed{\prod_n\theta_n=0.}
\tag{23}
\]

The critical logarithmic case is particularly informative. If

\[
\varepsilon_n
\sim
a\frac{s_n}{1+F(p_n)},
\qquad a>0,
\tag{24}
\]

then (9) and the positive-weight averaging principle imply

\[
\sum_{n\le M}\varepsilon_n
\sim
a\log(1+F(p_M)).
\tag{25}
\]

Moreover `\sum\varepsilon_n^2<\infty`: by (24), eventually `\varepsilon_n^2\lesssim s_n^2`, and PF-299 proves `(s_n)\in\ell^2`. Hence

\[
\sum_{n\le M}\log(1-\varepsilon_n)
=-\sum_{n\le M}\varepsilon_n+O(1),
\tag{26}
\]

so

\[
\boxed{
\prod_{n\le M}\theta_n
=(1+F(p_M))^{-a+o(1)}
=(\log p_M)^{-a+o(1)}.
}
\tag{27}
\]

Thus the exact logarithmic endpoint does not merely decide extinction: it predicts polynomial decay in `\log p` if that asymptotic loss law is eventually established.

## 4. What this removes from the live ambiguity

PF-299 correctly identified `s_n` versus `s_n^{1+\delta}` as a sufficient discriminator, but that is not the full endpoint picture. The present result shows that a much smaller perturbation already changes the global answer:

\[
s_n(\log p_n)^{-\beta}
\quad\text{is non-summable for }\beta\le1
\quad\text{and summable for }\beta>1.
\tag{28}
\]

Therefore the next useful pant asymptotic is not merely the power of `s_n`. If one can factor the relative killing as

\[
\frac{\kappa_n}{c_n}
=s_n\,a_n
\tag{29}
\]

with `a_n` controlled by a monotone function of the intrinsic coordinate `F(p_n)`, then (3) converts the accumulated-loss question into an ordinary one-dimensional integral test. Detailed oscillations of the individual prime gaps do not need to be re-analyzed at the accumulation stage.

This is still only the scalar constant channel. Nothing here identifies its product with the full physical `P/H` mixed return operator, and nothing implies a global Green bound, compactness, a weak-trace estimate, scattering control, or an RH consequence.

## 5. Prior art and novelty audit

No novelty is claimed for monotone Riemann-sum comparison, the integral test, or the infinite-product criterion. The proof of (3) is elementary once the exact coordinate increments `h_n=t_n-t_{n-1}` and the symmetric seam identity `s_n=(h_n+h_{n+1})/2` are in place.

A structure-directed literature search for weighted series of consecutive prime gaps and logarithmically normalized gap sums primarily returned the standard literature on limit points of normalized gaps, such as Banks--Freiberg--Maynard, *On limit points of the sequence of normalized prime gaps*, Proc. London Math. Soc. **113** (2016), 515--539, DOI `10.1112/plms/pdw036`, and later refinements. Those works study the arithmetic distribution of `(p_{n+1}-p_n)/\log p_n`; they do not provide or need the project-specific seam quadrature (3). No standalone number-theory theorem is claimed here.

The Mathia-specific content is the exact use of the prime-flute seam weights as a quadrature mesh and the resulting `\beta=1` calibration for PF-298's accumulated killed-conductance transmission. No new external theorem is needed beyond the already audited PF-299 inputs, so `SOURCES.md` requires no additional dependency entry.

## 6. Boundaries and falsification

1. **Monotone weight class.** Equation (3) is proved for nonnegative nonincreasing `\phi`. Highly oscillatory source-dependent coefficients can correlate with the irregular mesh and are not reduced to the same integral without an additional argument.
2. **Scalar compression only.** Equations (20)--(27) concern PF-298's isolated constant-boundary compression. The complete `P/H` reassembly can add nonconstant transfer, cancellation, or escape.
3. **Conditional killing law.** This finding does not prove any asymptotic for `\kappa_n/c_n`; it supplies the exact accumulation test once such an asymptotic or one-sided bound is derived.
4. **No prime-gap averaging assumption.** The proof does not replace actual prime gaps by their average size. Its robustness comes from using the exact `F(p_n)` partition and the fact that its mesh tends to zero.
5. **No hidden novelty claim.** The analytic lemma is elementary. The research value is that it closes the logarithmic endpoint calibration left open by PF-299 and makes the next local pant computation more precise.

A refutation would have to break the exact seam identity in PF-299, the established tail property `h_n\to0`, or the elementary left/right Riemann-sum inequalities (12)--(14).

## Consequence for the research line

The scalar source/escape gate now has a continuous endpoint calibration rather than only a power-law one. For a loss of size `s_n\phi(F(p_n))`, monotone `\phi`, accumulated constant-channel absorption is governed by `\int\phi`. In particular, `1/\log p` suppression remains critical and still kills the scalar product, whereas `(\log p)^{-1-\delta}` suppression is summable. The next high-value local calculation is therefore a first-order estimate of `\kappa_n/c_n` precise enough to distinguish these logarithmic scales before returning to the full mixed `P/H` reassembly.