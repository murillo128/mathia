# RE-252 — Guth–Maynard short-interval PNT stretches the self-tangent Robin-invisible window

**Status:** LITERATURE+DERIVED + EXACT-KERNEL-BOUND + UNCONDITIONAL-ORDINARY-PRIME-LOCALIZATION + PRIOR-ART-BOUNDED; independent adversarial audit pending.

**Dependencies:** RE-021 (universal selected first-layer endpoint and Robin tax), RE-022 (exact mixed-race kernel and remote-tail splice); Guth–Maynard (2026), Corollary 1.3.

RE-022 proves that the near-frontier contribution to the selected Robin mixed-race integral is negligible whenever the local horizon is \(o(p^{3/4}/\sqrt{\log p})\). Its upper bound deliberately discards cancellation in the ordinary-prime counting function. Applying a uniform, unconditional prime number theorem in short intervals replaces the previous quadratic local loss by a stretched-exponentially discounted quadratic loss. This extends the invisible horizon beyond \(p^{3/4}\), for every regular self-tangent colossally abundant state, including exceptional adjacent-transition chambers.

## Precise theorem

Let \(C\) range through sufficiently large regular self-tangent colossally abundant integers, and put \(X=\log C\). Let \(p\) be the largest prime whose first-layer event is active at \(X\), as defined in RE-021. Set
\[
L=\log p,\quad
\Delta(t)=\vartheta(t)-t,\quad
h(t)=\frac{-\log(1-t^{-1})}{\log t},\quad
k(t)=\frac1{t\log t},\quad
I(t)=\Delta(t)h'(t)-(h(t)-k(t)).
\]
By RE-021, this *selected* ordinary prime satisfies \(|\Delta(p)|\ll p^{0.52}\). For every fixed \(0<\delta<1/2\), define
\[
H_\delta(p)=p^{3/4}
  \exp\!\left((1/2-\delta)(\log p)^{1/4}\right).
\]
Then the following is **uniform in every real \(0\le H\le H_\delta(p)\)**:
\[
\boxed{
\sqrt p\log p\,\left|\int_p^{p+H}I(t)\,dt\right|
\ll_\delta (\log p)\exp\!\bigl(-2\delta(\log p)^{1/4}\bigr)+p^{-1/5}.
}\tag{1}
\]
Thus the left side is \(O_{\delta,M}((\log p)^{-M})\) for every fixed \(M>0\). In particular, the same all-logarithmic-order negligibility holds for \(H=p^{3/4}(\log p)^B\), for any fixed real \(B\).

For the remote PNT horizon from RE-022,
\[
U_A(p)=\exp\!\left(A(\log p)^{5/3}(\log\log p)^{1/3}\right),
\quad A>A_0\ \text{fixed},
\]
one consequently has, for every fixed \(M>0\),
\[
\boxed{
\mathscr Y(p):=\sqrt p\log p\int_p^\infty I(t)\,dt
=\sqrt p\log p\int_{p+H_\delta(p)}^{U_A(p)}I(t)\,dt
+O_{\delta,A,M}((\log p)^{-M}).
}\tag{2}
\]
The universal tax identity and its expansion in RE-021 then give
\[
\boxed{
\sqrt p\log p\,(\log G(C)-\gamma)
=\sqrt p\log p\int_{p+H_\delta(p)}^{U_A(p)}I(t)\,dt
-2\sqrt2+\frac{\sqrt2(2+\log2)}{\log p}
+O_{\delta,A}((\log p)^{-2}).
}\tag{3}
\]
In particular, an unbounded family of regular self-tangent counterexamples to Robin's inequality must carry a normalized mixed-race contribution with lower limit at least \(2\sqrt2\) **outside** this longer near-frontier window. None of (1)–(3) asserts that such a contribution cannot exist.

## Uniform prime-counting input and Chebyshev transfer

Larry Guth and James Maynard, *New large value estimates for Dirichlet polynomials*, Annals of Mathematics **203** (2026), 623–675, Corollary 1.3 (DOI 10.4007/annals.2026.203.2.6; arXiv:2405.20552v2), prove the following *pointwise/uniform*, not almost-all, short-interval estimate for each fixed \(\varepsilon>0\):
\[
\pi(x+y)-\pi(x)
=\frac{y}{\log x}
+O_\varepsilon\!\left(y e^{-(\log x)^{1/4}}\right),
\quad x^{17/30+\varepsilon}\le y\le x^{0.99}.
\tag{4}
\]
Take \(\varepsilon=1/30\), so the lower endpoint is \(y_0=p^{3/5}\). For large \(p\), the entire interval \([y_0,H_\delta(p)]\) lies in the range of (4). The exact prime-weight decomposition is
\[
\vartheta(p+y)-\vartheta(p)
=L\bigl(\pi(p+y)-\pi(p)\bigr)
+\sum_{p<r\le p+y}\log(r/p).
\]
Every summand in the final sum is bounded by \(y/p\), and the number of such primes is at most \(y+1\). Hence, uniformly for \(y_0\le y\le H_\delta(p)\),
\[
\vartheta(p+y)-\vartheta(p)-y
=O\!\left(yL e^{-L^{1/4}}+\frac{y^2}{p}\right).
\tag{5}
\]
The trivial integer-count bound for \(0\le y\le y_0\), combined with the selected endpoint estimate, gives
\[
|\Delta(p+y)|\ll p^{0.52}+(y+1)L
\quad(0\le y\le y_0),
\tag{6}
\]
whereas (5) gives
\[
|\Delta(p+y)|\ll p^{0.52}+yL e^{-L^{1/4}}+\frac{y^2}{p}
\quad(y_0\le y\le H_\delta(p)).
\tag{7}
\]
These bounds concern the *ordinary* Chebyshev function; there is no generalized-prime replacement or assumed equidistribution of the selected CA primes.

## Integrating the actual Robin kernel

Since \(H_\delta(p)=p^{3/4+o(1)}=o(p)\), the exact \(h,k\) obey, uniformly for \(p\le t\le p+H_\delta(p)\),
\[
|h'(t)|\ll\frac1{p^2L},
\qquad 0<h(t)-k(t)\ll\frac1{p^2L}.
\tag{8}
\]
Split at \(y_0=p^{3/5}\). From (6)–(8), for any \(H\le H_\delta(p)\),
\[
\begin{aligned}
\sqrt pL\left|\int_p^{p+H}I(t)\,dt\right|
&\ll p^{-3/2}\left[
 H p^{0.52}+p^{6/5}L
 +H^2L e^{-L^{1/4}}
 +\frac{H^3}{p}+H
\right].
\end{aligned}
\tag{9}
\]
This estimate remains valid for \(H<y_0\), simply by harmless overestimation of the short initial segment. At \(H=H_\delta(p)\), the third summand after multiplying by \(p^{-3/2}\) is exactly bounded by
\[
p^{-3/2}H_\delta(p)^2 L e^{-L^{1/4}}
=L e^{-2\delta L^{1/4}}.
\tag{10}
\]
The remaining four summands are \(O_\delta(p^{-1/5})\) for sufficiently large \(p\): their dominant powers are \(p^{-0.23+o(1)}\), \(p^{-0.3}L\), \(p^{-1/4+o(1)}\), and \(p^{-3/4+o(1)}\). All contributions increase monotonically with \(H\), proving the uniform bound (1).

The unconditional Korobov–Vinogradov remote-tail estimate already proved and parameterized in RE-022 makes
\[
\sqrt pL\int_{U_A(p)}^\infty I(t)\,dt
=O_{A,M}(L^{-M})
\]
for every fixed \(M>0\), provided \(A>A_0\) strictly. Split the exact defining integral for \(\mathscr Y(p)\) at \(p+H_\delta(p)\) and \(U_A(p)\) and apply (1) and the remote estimate to obtain (2). The exact self-tangent height identity and all-orders deterministic CA tax in RE-021 then yield (3). No clean-adjacent-boundary assumption enters.

## Prior art, falsification and scope

The uniform short-interval prime theorem and its error exponent are Guth–Maynard's; the transfer (5) is elementary partial summation. The local kernel and CA endpoint dictionary were established in RE-021–RE-022. The mathematical delta here is their quantitative composition: the *cancellation-free* \(p^{3/4}/\sqrt{\log p}\) horizon is not an arithmetic barrier, and the CA-selected Robin height remains insensitive to a strictly longer **ordinary-prime** window with error below every fixed inverse power of \(\log p\). A targeted prior-art search found the Guth–Maynard theorem but not this exact CA-selected Robin-kernel deduction; no claim of exhaustive external novelty is made.

Checks that are load-bearing: use the **uniform** Corollary 1.3 rather than the almost-all Corollary 1.4; retain the factor \(L\) when converting prime counts to \(\vartheta\); use the actual selected endpoint \(\Delta(p)=O(p^{0.52})\), not an unjustified generic PNT estimate at arbitrary \(p\); split at \(p^{3/5}\); keep the \(y^2/p\) logarithmic-weight correction; use the exact \(h,k\) kernel and the strict \(A>A_0\) remote margin. The constants depend on fixed \(\delta\), and the theorem does not cover \(\delta=0\) or horizons \(p^{3/4+\varepsilon}\) with fixed \(\varepsilon>0\).

Nothing here bounds the remaining annular integral by the Robin threshold, proves monotonicity of CA values, constrains a genuinely prime-specific counterexample profile beyond this source localization, or proves RH. Independent adversarial review of the derived localization remains outstanding.
