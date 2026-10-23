# FD-337 — Sublinear rank-sine bands transfer to the Mertens spectrum

**Status:** LITERATURE+DERIVED + EXACT-FINITE-INEQUALITY + UNCONDITIONAL-BAND-TRANSFER + ARITHMETIC-COLLAPSE-BOUNDARY.

FD-002 equates the **total** Franel energy with a continuous Fourier–Mertens energy. That isometry does not identify their frequency bands: one transform uses the uniform **rank** coordinate, the other the actual fraction coordinate. The distinction matters for the spectral-allocation question calibrated by FD-335–FD-336.

There is nevertheless a quantitative band transfer. For every cutoff `q=o(Q)`, the genuine order-`Q` Farey rank-sine energy share differs by `o(1)` from the corresponding truncated Ramanujan–Mertens energy share. The error is `O(q/Q+(q/Q)^2+1/Q)`. Thus both predeclared bands have an arithmetic description with a vanishing **additive** error. This identifies their information content; it proves neither a limiting share nor new Möbius cancellation.

## 1. Objects and finite statement

Use the same endpoint and rank conventions as FD-335–FD-336:
\[
0=x_0<x_1<\cdots<x_N=1,\qquad
N=\sum_{d\le Q}\varphi(d),\qquad Q\ge3,
\]
\[
D_k=x_k-k/N,\quad
E=\sum_{k=1}^{N-1}D_k^2,\quad
\Delta=\max_{1\le k\le N}|D_k|,
\]
\[
d_{2j}=\sqrt{2/N}\sum_{k=1}^{N-1}D_k\sin(2\pi jk/N),
\qquad E_q=\sum_{j=1}^q d_{2j}^2,
\quad 1\le q\le N/2-1.
\tag{1}
\]
Here `N` is even. Reflection kills the odd Dirichlet modes, and orthogonality gives `E_q<=E`.

Write `M(t)=sum_(n<=t) mu(n)` and define the classical divisor modes
\[
B_Q(j)=\sum_{\substack{d\mid j\\d\le Q}}d M(\lfloor Q/d\rfloor),
\qquad a_j=-\frac{B_Q(j)}{\pi j\sqrt{2N}},
\tag{2}
\]
\[
T_q=\sum_{j\le q}a_j^2,\qquad
T_\infty=\frac1{2\pi^2N}\sum_{j\ge1}\frac{B_Q(j)^2}{j^2}
=E+\frac1{12N},\qquad R_q=\frac{T_q}{T_\infty}.
\tag{3}
\]
The last equality is exactly FD-002, with its Farey order renamed `Q` and its number of gaps renamed `N`. In particular, `0<=R_q<=1`. The infinite series converges for each fixed `Q`.

**Finite transfer theorem.** Put `C=8 pi/3` and `kappa=C q Delta`. Then
\[
\boxed{\left(\sum_{j\le q}|d_{2j}-a_j|^2\right)^{1/2}
\le Cq\left(\sum_{k=1}^N D_k^4\right)^{1/2}
\le\kappa\sqrt E.}
\tag{4}
\]
Consequently,
\[
\boxed{\left|\frac{E_q}{E}-R_q\right|
\le 2\kappa+\kappa^2+\frac1{12NE}.}
\tag{5}
\]
Dress's absolute-discrepancy theorem implies `Delta<=1/Q`. Also, for
`h=floor(N/(2Q))`, the first empty Farey interval gives
\[
E\ge\frac{h}{4Q^2},\qquad NE\gg Q
\quad(Q\longrightarrow\infty).
\tag{6}
\]
Thus (5) gives, uniformly over allowed cutoffs,
\[
\boxed{\frac{E_q}{E}=R_q+
O\!\left(\frac qQ+\frac{q^2}{Q^2}+\frac1Q\right).}
\tag{7}
\]
In particular the errors are `O(Q^(-1/2))` at `q=floor(sqrt Q)` and `O(Q^(-1/3))` at `q=floor(Q^(2/3))`. No RH hypothesis, prime number theorem, or assumption that `E` is small is needed for this transfer.

## 2. A deterministic rank-to-position Fourier lemma

The norm estimate (4) is not specifically arithmetic. Let
`0<x_1<...<x_N=1` be any ordered grid, put `t_k=k/N`, `D_k=x_k-t_k`, and replace `B_Q(j)` in (2) by
\[
C_j=\sum_{k=1}^N\cos(2\pi jx_k).
\]
For `1<=q<N/2`, the same bound (4) holds. Reflection is unnecessary for this lemma.

Interpolate monotonically from uniform ranks to actual positions:
\[
y_k(s)=(1-s)t_k+sx_k,\qquad 0\le s<1.
\]
Every consecutive gap is at least `(1-s)/N`. The circular gap from `y_N(s)=1` to `y_1(s)` has the same lower bound. Hence all these points are separated modulo one by
\[
\delta_s\ge(1-s)/N.
\tag{8}
\]

For an integer `1<=j<N`, the uniform-grid cosine sum is zero. Taylor's formula with its integral remainder therefore gives exactly
\[
C_j=-2\pi j\sqrt{N/2}\,d_{2j}
 -(2\pi j)^2\int_0^1(1-s)F_j(s)\,ds,
\qquad
F_j(s)=\sum_{k=1}^N D_k^2\cos(2\pi j y_k(s)).
\tag{9}
\]
The endpoint `k=N` has `D_N=0`; its contribution `cos(2 pi j)=1` to `C_j` must still be retained to cancel the uniform-grid sum correctly.

The dual form of Montgomery–Vaughan's large-sieve inequality, applied at the separated points in (8), states
\[
\sum_{j=1}^q\left|\sum_{k=1}^N w_k e^{2\pi i j y_k(s)}\right|^2
\le(q+\delta_s^{-1})\sum_{k=1}^N|w_k|^2.
\tag{10}
\]
This is the usual sampling inequality with its matrix transposed/conjugated; the operator norm is unchanged. Use `w_k=D_k^2` and bound the real parts by the complex moduli. With `a_j=-C_j/(pi j sqrt(2N))`, Minkowski's inequality in (9) gives
\[
\begin{aligned}
\|(d_{2j}-a_j)_{j\le q}\|_2
&\le2\pi q\sqrt{2/N}\,\|D^2\|_2
 \int_0^1(1-s)\sqrt{q+N/(1-s)}\,ds\\
&\le2\pi q\sqrt{2/N}\,\|D^2\|_2
 \sqrt{2N}\int_0^1\sqrt{1-s}\,ds\\
&=\frac{8\pi}{3}q\|D^2\|_2.
\end{aligned}
\tag{11}
\]
The second line uses only `q<=N`. The apparent loss at `s=1` is integrable: Taylor's weight `(1-s)` leaves the factor `sqrt(1-s)`. The value at that one endpoint is immaterial. Finally `||D^2||_2<=Delta sqrt(E)`. This proves (4).

A termwise Taylor bound alone would give an error proportional to `q^(3/2) E/sqrt(N)`. Summing with the large sieve is what removes that extra frequency-count loss and permits the full range `q=o(Q)` using the known supremum bound.

## 3. Arithmetic identification and normalized energy

For the actual positive Farey points, including `1`, Ramanujan's divisor identity gives
\[
\sum_{k=1}^N e^{2\pi i jx_k}
=\sum_{d\le Q}c_d(j)
=\sum_{r\mid j,\ r\le Q} r\sum_{m\le Q/r}\mu(m)
=B_Q(j).
\tag{12}
\]
These quantities are real. Thus the generic cosine coefficient `C_j` in (9) is exactly (2), including the denominator-one contribution. This is the same classical arithmetic as FD-001–FD-002.

The reverse triangle inequality in (4) gives
`|sqrt(T_q)-sqrt(E_q)|<=kappa sqrt(E)`. Since `E_q<=E`,
\[
|T_q-E_q|\le(2\kappa+\kappa^2)E.
\tag{13}
\]
Using (3),
\[
\frac{T_q}{E}-R_q=\frac{R_q}{12NE}\in
\left[0,\frac1{12NE}\right],
\]
which proves (5).

Dress's theorem, in the positive-point convention, bounds
`|x-A_Q(x)/N|` by `1/Q`. At `x=x_k`, `A_Q(x_k)=k`, proving the needed `Delta<=1/Q`; there is no midpoint shift. For (6), each `x_k>=1/Q`, so for `1<=k<=h`,
\[
D_k\ge1/Q-h/N\ge1/(2Q).
\]
There are `h` such terms. The classical totient asymptotic
`N~3Q^2/pi^2` gives `h~3Q/(2 pi^2)` and hence `NE>>Q`. In particular `E>0` for `Q>=3`, and the continuity correction in (3) is negligible after normalization. This proves (7).

## 4. Consequence for the calibrated spectral-allocation statistic

For either FD-335's reflected single-gap null or any deterministic block choice `1<=b(Q)<=Q/log(2Q)` in FD-336, let
\[
f_q^{\rm null}=\frac{\mathbb E_{\rm null}E_q}
                         {\mathbb E_{\rm null}E},
\qquad
S_q^{\rm actual}=\frac{E_q/E}{f_q^{\rm null}}.
\]
The numerator is always evaluated on the **genuine** Farey grid; the expectations use the chosen null's own calibration. FD-335–FD-336 give `f_q^null ->1` for every diverging cutoff. Combining that result with (7), for `q->infinity` and `q=o(Q)`,
\[
\boxed{S_q^{\rm actual}=R_q+o(1)
=\frac{\sum_{j\le q}j^{-2}|\sum_{d\mid j}dM(\lfloor Q/d\rfloor)|^2}
        {\sum_{j\ge1}j^{-2}|\sum_{d\mid j}dM(\lfloor Q/d\rfloor)|^2}
 +o(1),}
\tag{14}
\]
where terms with `d>Q` vanish. The same conclusion holds for any other null for which `f_q^null ->1` is independently proved.

There is no rate for `f_q^null ->1` supplied here. The explicit rates following (7) concern the rank-band share versus `R_q`; they must not be reported as rates for the null-normalized statistic in (14). There is also no relative-error claim when `R_q` tends to zero.

This closes a specific interpretive branch of the gap-ordering clue: an order-one asymptotic allocation deficit in either predeclared band is the same deficit in the classical divisor-transformed Mertens spectrum. Passing from position modes to rank modes does not create an independent low-frequency arithmetic carrier. The ratio still retains **more information than total scalar energy or `M(Q)` alone**. A new estimate for it could be useful; the theorem does not supply one. Local-order controls remain useful finite diagnostics, but their limiting deficit cannot by itself establish information outside (14).

## 5. Audit, prior art, and limits

A standard-library Python audit independently enumerated the genuine Farey points for all `3<=Q<=60`, sieved the exact integer Mertens values, and formed both the rank sine coefficients and the actual-position cosine sums. All 11,436 admissible mode/prefix checks satisfied the pointwise Taylor bound, (4), and (5). The largest floating-point discrepancy between a direct cosine sum and its exact integer divisor sum was below `1.0e-11`. For all 58 orders, exact rational arithmetic also verified the endpoint lower bound and
\[
\sum_{d,e\le Q}\frac{\gcd(d,e)^2}{de}
 M(\lfloor Q/d\rfloor)M(\lfloor Q/e\rfloor)=12NE+1,
\]
which checks the total-energy normalization used in (3). Twelve nonarithmetic monotone controls at `N=8,20,48`—uniform, strongly clustered, and two smooth perturbations—also satisfied the generic inequality. These checks guard signs, the endpoint term, and normalization. They are not a numerical proof of the large sieve, Dress's theorem, or the asymptotic statement. The clue's larger-order comparison panel was not evaluated or tuned.

The primary analytic inputs are François Dress, *Discrépance des suites de Farey*, JTNB **11**(2) (1999), 345–367, [paper](https://www.numdam.org/item/JTNB_1999__11_2_345_0/), and H. L. Montgomery and R. C. Vaughan, *The large sieve*, Mathematika **20**(2) (1973), 119–134, [Theorem 1](https://doi.org/10.1112/S0025579300004708). Both are already anchored in SOURCES.md. The Farey/Ramanujan transform and full-energy identity are classical, as reconstructed in FD-001–FD-002; Huxley's *Identities involving Farey fractions*, Proc. Steklov Inst. Math. **276** (2012), 125–139, [DOI](https://doi.org/10.1134/S0081543812010105), is a neighboring weighted discrete/continuous Franel-identity reference, not an input asserting bandwise equality.

The general tools—Taylor expansion, monotone interpolation, large-sieve duality and quadratic norm comparison—are classical. No priority claim is made for this deterministic Fourier perturbation argument. The line-local delta is the **quantitative cutoff-preserving** identification (7)–(14), which the exact total-energy identity alone does not establish. It redirects the specified sublinear spectral test to a definite existing arithmetic object instead of extending the null calibration again.

The parameter condition is consequential: `q Delta ->0` makes the norm remainder negligible relative to `sqrt(E)`. At `q=Theta(Q)`, Dress's bound alone no longer supplies that conclusion. The argument neither proves this threshold sharp nor controls such endpoint-scale bands. Applying (4) to an artificial reordered grid does not entitle it to Dress's genuine-Farey bound or to the Ramanujan identity (12). No improved Franel exponent, RH implication beyond the classical criterion, denominator-conditioned null law, or independent adversarial approval is claimed.
