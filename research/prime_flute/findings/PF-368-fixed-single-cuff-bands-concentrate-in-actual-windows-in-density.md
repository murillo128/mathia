# PF-368 — fixed single-cuff bands concentrate in actual windows in density

**Status:** EXACT-DERIVED + CLASSICAL-CAUCHY-ALGEBRA + PRIME-INDEX-DENSITY-COMPARISON + COUPLED-RESIDUAL-OPEN.

PF-367 proves that its explicit fixed-width binomial packet stays inside the
prescribed embedded corridor window in prime-index density. The conclusion
extends **uniformly to every coefficient combination in any fixed finite
frequency interval on one exact cuff lattice**. The interval need not be
narrow. In particular it covers all real traces with `|xi|<=K`, for every
fixed finite `K`.

The mechanism is an explicit Cauchy inverse bound whose exponential rate
`c(W)` is strictly less than `1/2` for every finite frequency span `W`.
That rate is also the exact exponential rate of the least Gram eigenvalue.
Together with PF-367's exceptional-gap count, this rules out failure on a
positive-density family of cuffs by choosing more elaborate single-cuff
fixed-band packets. It does not control differences from two unequal cuff
lattices, exceptional prime subsequences, or the actual shorted angle.

## 1. A finite, coefficient-uniform estimate

Let `L>0`, let `m>=0` be an integer, set `N=m+1`, and take

\[
 f(t)=\sum_{j=0}^{m}z_j e^{2\pi i(k_0+j)t/L},\qquad k_0\in\mathbb Z,
 \quad W_m=2\pi m/L\le W<\infty.
\]

Missing modes are allowed by setting coefficients to zero. Thus every
exact-lattice trace in an interval of length `W` is included with
`N<=floor(WL/(2pi))+1`. Set

\[
 H[f]=\int_{\mathbb R}|f(t)|^2\operatorname{sech}t\,dt,
 \qquad H_{>T}[f]=\int_{|t|>T}|f(t)|^2\operatorname{sech}t\,dt,
\]
\[
 c(W)=\frac4{\pi^2}\int_0^{\pi W/4}\log\coth u\,du,
 \qquad c(0)=0.
\tag{1}
\]

For every `T>=0` and every nonzero `f`,

\[
 \boxed{\frac{H_{>T}[f]}{H[f]}
 \le\min\left\{1,\frac{4N^2}{\pi}e^{c(W)L-T}\right\}.}
\tag{2}
\]

For `W>0`,

\[
 0<c(W)<\frac12,\qquad
 \frac12-c(W)=\frac4{\pi^2}
 \sum_{r=0}^{\infty}
 \frac{e^{-(2r+1)\pi W/2}}{(2r+1)^2}.
\tag{3}
\]

Consequently, whenever `c(W)<theta<1/2` and `T>=theta L`, the supremum
of the tail fraction over the entire band is
`O_W(L^2 exp(-(theta-c(W))L))`. Band location and coefficients do not enter
the constant. For real sine/cosine traces in `|xi|<=K`, use `W=2K`;
one must include both signs when determining the frequency span.

## 2. Exact Cauchy conditioning on a cuff lattice

The Fourier transform of `sech` gives the Gram matrix

\[
 G_{jk}=\pi\operatorname{sech}(a(j-k)),\qquad a=\pi^2/L,
 \quad H[f]=z^*Gz.
\tag{4}
\]

For completeness, substitute `x=e^(2t)` in the transform integral to obtain
`integral_0^infinity x^((1+i omega)/2-1)/(1+x) dx`.
The beta integral and gamma reflection formula give
`pi/cosh(pi omega/2)`. This also fixes all Fourier factors in (4).

Put `x_j=e^(2aj)`. Then

\[
 G_{jk}=\frac{2\pi\sqrt{x_jx_k}}{x_j+x_k}.
\]

For `C_jk=1/(x_j+x_k)`, the Cauchy determinant is

\[
 \det C=\frac{\prod_{j<k}(x_k-x_j)^2}
 {\prod_j2x_j\prod_{j<k}(x_j+x_k)^2}.
\]

Taking the principal cofactor ratio and then undoing the diagonal scaling
proves, without any matrix asymptotic theorem,

\[
 (G^{-1})_{jj}=\frac1\pi
 \prod_{k\ne j}\coth^2(a|j-k|)
 =\frac1\pi\exp\{2S_j+2S_{m-j}\},
 \quad S_q=\sum_{r=1}^{q}\log\coth(ar).
\tag{5}
\]

Let `F(v)=integral_0^v log coth(u) du`. Its integrand is positive,
decreasing and integrable at zero, so `F` is increasing and concave.
The right-endpoint sum satisfies `S_q<=F(aq)/a`. Hence

\[
 2S_j+2S_{m-j}
 \le\frac2a\{F(aj)+F(a(m-j))\}
 \le\frac4a F(am/2)
 =c(W_m)L\le c(W)L.
\tag{6}
\]

Since `G` is positive definite,

\[
 \|G^{-1}\|\le\operatorname{Tr}G^{-1}
 \le\frac N\pi e^{c(W)L},\qquad
 \boxed{\lambda_{\min}(G)\ge\frac\pi N e^{-c(W)L}.}
\tag{7}
\]

On the other hand `|f(t)|^2<=N||z||_2^2` and
`integral_(|t|>T) sech(t)dt<=4e^(-T)`. Combining this with (7) proves (2).
No orthogonality on a shorter-than-period interval was assumed.

To verify the strict margin in (3), expand the positive series

\[
 \log\coth u
 =2\sum_{r\ge0}\frac{e^{-2(2r+1)u}}{2r+1}.
\]

Termwise integration gives
`F(infinity)=sum_(r>=0)(2r+1)^(-2)=pi^2/8`, and the remaining tail integral
is exactly (3). The margin is positive for every fixed finite `W`, but is
asymptotic to `4 exp(-pi W/2)/pi^2` for large `W`. There is no useful
width-independent margin.

### The conditioning exponent is exact

For complete consecutive bands with `m=WL/(2pi)+O(1)` and fixed `W>0`,

\[
 \boxed{\lim_{L\to\infty}\frac1L\log\lambda_{\min}(G)=-c(W).}
\tag{8}
\]

Indeed the decreasing increments of `S_q` put the largest inverse diagonal
at `j=floor(m/2)` or `ceil(m/2)`. If that value is `M`, positivity yields

\[
 M\le\|G^{-1}\|\le NM.
\tag{9}
\]

For either central index, the Riemann sums in (5), divided by `L`, tend
to the corresponding integral in (1). The logarithmic singularity causes
no problem: for `q>=1`,

\[
 \int_a^{a(q+1)}\log\coth u\,du
 \le aS_q\le\int_0^{aq}\log\coth u\,du,
\]

and both endpoints tend to the same limit. Equation (9) and
`log N/L->0` prove (8). Exactness here concerns the **Gram conditioning
exponent**; (2) is not claimed to have the optimal spatial-window threshold.

## 3. Uniform concentration in the prescribed prime windows

Use exactly PF-367's prescribed embedded window, with its fixed sufficiently
small `0<vartheta<1`:

\[
 P=p_{i-1},\quad a_i=p_i-p_{i-1},\quad b_i=p_{i+1}-p_i,
 \quad s_i=(h_i+h_{i+1})/2,
\]
\[
 L_i=2\log\coth(h_i/4),\qquad
 T_i=\operatorname{arsinh}(\vartheta/\sinh s_i)-1.
\tag{10}
\]

This is not a claim about the maximal embedded domain. The exact cotangent
mesh and the sublinear prime-gap bound give uniformly on the tail

\[
 L_i=2\log(4P/a_i)+o(1),\qquad
 T_i=\log(4\vartheta P/(a_i+b_i))-1+o(1),
 \quad L_i\longrightarrow\infty.
\tag{11}
\]

As proved in PF-367, for each fixed `0<theta<1/2`,

\[
 T_i\le\theta L_i
 \quad\Longrightarrow\quad
 b_i\ge c_\theta P^{1-2\theta}a_i^{2\theta},
\]
\[
 \#\{i:p_{i-1}\le X,\ T_i\le\theta L_i\}
 =O_\theta(X^{2\theta}).
\tag{12}
\]

The count uses only `a_i>=2` and the telescoping sum of the disjoint gaps
`b_i` in each dyadic prime block. The prime number theorem converts it to
an exceptional proportion `O_theta(X^(2theta-1) log X)`.

Fix any finite `W>0` and choose `c(W)<theta<1/2`. Let `I_i` be any real
interval of length at most `W`, and let `B_i` be its exact cuff Fourier
span. Outside the exceptional indices of (12), (2) gives

\[
 \boxed{\sup_{0\ne f\in B_i}
 \frac{H_{>T_i}[f]}{H[f]}
 \le\frac4\pi\left(\frac{WL_i}{2\pi}+1\right)^2
 e^{-(\theta-c(W))L_i}\longrightarrow0.}
\tag{13}
\]

If `B_i={0}`, set its supremum to zero. Convergence is uniform over all
remaining sufficiently far indices and all interval locations. Thus the
left-hand side tends to zero **in prime-index density**, with an explicit
exceptional set independent of the coefficient vector or band location.
For example one can take `theta=(c(W)+1/2)/2`, giving exceptional count
`O_W(X^(c(W)+1/2))`.

This strengthens the packet-specific conclusion of PF-367. Arbitrary
coefficients, holes in the band, constants, realification, or dependence
of the coefficients on the geometry cannot create positive-density escape
for a single cuff with a fixed bounded frequency span. It also explains
why the full-period lower bound of PF-347, with exponent `1/2`, was too
coarse for this inference: the strict finite-span improvement is essential.

## 4. Scope, controls and the remaining implication

- A difference `f_(i+1)-f_i` on **two unequal lattices** need not belong to
  a single lattice of spacing `2pi/L_i`. Applying (13) separately controls
  its tail by `H[f_i]+H[f_(i+1)]`, not by `H[f_(i+1)-f_i]`. Cancellation
  can make the latter arbitrarily smaller. No coupled residual estimate
  or broad-band replacement for PF-361/PF-363 follows.
- The exceptional set may be infinite. Density-one scalar control does
  not imply compactness, a Schatten bound, or a uniform all-tail comparison.
  PF-367's rare power-gap escape question remains open.
- The crude certified subwindow `T=(19/80)L+O(1)` need not meet
  `T>c(W)L`. Its broad-band binomial counterexample is unchanged. The
  present argument uses the larger **prescribed actual window** and (12).
- The result applies to every fixed finite `W`; it makes no uniform
  assertion for widths growing with `i`. Formula (3) quantifies the
  deteriorating margin. For real bounded-frequency bands the span is
  `2K`, not just the positive-frequency width.
- The scalar theorem (2) is universal. Any nonprime control with the
  same period/window condition satisfies it. Prime arithmetic supplies
  only the exceptional count here; no primality detector or RH consequence
  is constructed.
- Actual pant mass, tangential energy, seam normalization, global transition
  minimization and the completed low/high angle remain outside the claim.
  Even a minimizing residual confined to one cuff is covered only when
  its **whole frequency span**, including its retained carrier, is bounded
  by the chosen `W`.

The next substantive obstacle is therefore simultaneous cancellation
between distinct neighboring lattices or the exceptional modules, rather
than finding a different fixed-band packet on a positive-density family
of individual cuffs.

## 5. Prior art and validation

The determinant and cofactor identity are classical Cauchy algebra; see
Dario Fasino, *Orthogonal Cauchy-like matrices*, Numerical Algorithms 92
(2023), 619–637, [Section 2.1, equations (5)–(7)](https://doi.org/10.1007/s11075-022-01391-y).
Equations (5)–(9) specialize that algebra to an equally spaced `sech` Gram
matrix; no new matrix-inversion method is claimed. PF-348/PF-366 used
related Cauchy inverse bounds for narrow cosine clusters. The complex
exponential representation here retains the exact difference spacing and
the strict rate `c(W)<1/2` for every finite span.

The Fourier identity is also classical: the beta integral and reflection
formula are [DLMF 5.12.3](https://dlmf.nist.gov/5.12#E3) and
[DLMF 5.5.3](https://dlmf.nist.gov/5.5#E3). Gaillac–Gautier,
*Estimates for the SVD of the Truncated Fourier Transform on L2(cosh(b·))
and Stable Analytic Continuation*, [author manuscript](https://publications.ut-capitole.fr/id/eprint/32479/1/wp_tse_1013.pdf),
Proposition 1 and Theorem 1, studies the continuous truncated transform,
its `sech` kernel and spectral bounds. That continuous operator is not the
simultaneously growing finite lattice matrix (4); no sampling or eigenvalue
transfer from it is assumed. The estimate above is proved directly.

The literature audit covered Cauchy inverse formulas, hyperbolic-secant
Toeplitz matrices and weighted Fourier concentration. This is a
literature-derived finite-matrix estimate and its prime-window application,
not a claim of a new general uncertainty theorem. The arithmetic inputs
are exactly PF-367's (17)–(19), S6's Baker–Harman–Pintz sublinear gap bound,
and the classical prime number theorem; no stronger gap theorem is used.

Supplementary 100-digit standard-library Decimal checks used 12 matrices:
`W in {1/2,1,2}` with `L in {16,32,64}`, and `W=4` with `L in {8,16,32}`,
each with `m=floor(WL/(2pi))`. Direct Gaussian inversion agreed with every
inverse diagonal in (5) to relative error below `1e-88`. Positive-pivot
Cholesky checks verified (7), positivity of the window Gram matrix, and
the relative tail inequality at `T=(c(W)+1/2)L/2`. The tail matrix was
evaluated from the integrated exponential series for `sech`.
These finite checks audit factors and signs; they are not interval
certificates, asymptotic evidence, or pant-PDE computations. Scratch is
outside Git. The displayed proof establishes the result.

Formalizing the classical cofactor step alone would not test the remaining
two-lattice cancellation or actual-energy passage. No compute or Lean
handoff is proposed for that peripheral target.
