# PF-369 — nearly equal cuff lattices hide broad-band residual mass beyond actual windows

**Status:** EXACT-DERIVED + CLASSICAL-FOURIER-AND-DIVIDED-DIFFERENCE-CONSTRUCTION + MATCHED-CONTROL-OBSTRUCTION + PRIME-REALIZATION-OPEN.

PF-368's coefficient-uniform single-cuff concentration does not extend to
differences of neighboring cuff traces from the available geometric bounds
alone. Two distinct, exponentially close periods admit fixed-band differences
whose weighted mass escapes even the entire central fundamental interval.
The exact cotangent construction on equally spaced composite labels realizes
the required period separation and the prescribed actual corridor window.

This is a counterexample to a **uniform scalar window/full-norm comparison**
under those geometric hypotheses. It is not a prime subsequence theorem or an
actual pant-energy or shorted-angle counterexample. The individual traces have
large coefficients; their cancellation is precisely the information lost by
applying PF-368 separately to the two cuffs.

## 1. A quantitative two-period obstruction

Fix `alpha>1/log(16)`. Let `L->infinity`, `n=ceil(alpha L)`, and

\[
 L'=L+\delta_L>0,\qquad
 0<|\delta_L|=o(L^2e^{-L/2}).
\tag{1}
\]

There are trigonometric polynomials `f_L` and `f_(L')` on the respective
**exact** Fourier lattices, each using only indices `n,...,3n`, such that,
with `g_L=f_(L')-f_L` and

\[
 H[g]=\int_{\mathbb R}|g(t)|^2\operatorname{sech}t\,dt,
\]

\[
 \boxed{
 \frac{\displaystyle\int_{-L/2}^{L/2}|g_L(t)|^2\operatorname{sech}t\,dt}
 {H[g_L]}
 \le C_\alpha\left(
 \frac{e^L}{n^2 16^n}
 +\frac{\delta_L^2e^L}{L^4}\right)\longrightarrow0.}
\tag{2}
\]

The same bound holds for every smaller symmetric window. All positive
frequencies lie in any fixed open interval containing
`[2pi alpha,6pi alpha]`, on a sufficiently far tail. Thus the bandwidth is
fixed, not growing. For example `alpha=1/2` gives limiting positive support
`[pi,3pi]`. No assertion of an optimal width or period-separation threshold
is made.

At least one real or imaginary component of `g_L` has no larger mass ratio.
Taking that same component of both traces gives real, zero-mean cuff traces
with the identical obstruction. Their positive sine/cosine frequencies stay
in the stated interval.

## 2. A periodic approximation to a nonperiodic linear factor

Set

\[
 q(t)=\cos^{2n}(\pi t/L),\qquad
 y(t)=tq(t)\quad(-L/2\le t\le L/2).
\]

Extend `y` periodically and let `P_n` be its Fourier partial sum with
indices `-n,...,n`. The endpoint values vanish. Its discarded coefficients
are explicitly summable, giving

\[
 \boxed{\sup_{|t|\le L/2}|tq(t)-P_n(t)|
 \le E_{L,n}:=\frac{L}{2\pi n4^n}.}
\tag{3}
\]

Here is the coefficient calculation, including normalization. The classical
cosine beta integral gives

\[
 J_n(\nu):=\int_{-1/2}^{1/2}\cos^{2n}(\pi x)e^{-2\pi i\nu x}\,dx
 =\frac{(2n)!}{4^n\Gamma(n+\nu+1)\Gamma(n-\nu+1)}.
\tag{4}
\]

Reciprocal gamma at its zeros interprets the right side continuously. If
`a_k` is the Fourier coefficient of `y`, differentiation under this finite
integral gives

\[
 a_k=\frac{iL}{2\pi}J_n'(k).
\]

For `k=n+r`, `r>=1`, the simple zero of the reciprocal gamma factor yields

\[
 |a_{n+r}|=\frac{L}{2\pi}\frac{(2n)!}{4^n}
                   \frac{(r-1)!}{(2n+r)!}.
\tag{5}
\]

Since `y` is real, the negative-index magnitudes are the same. The telescoping
identity

\[
 \sum_{r=1}^{\infty}\frac{(r-1)!}{(2n+r)!}
 =\frac{1}{2n(2n)!}
\tag{6}
\]

proves (3). For example each summand is `1/(2n)` times the difference
`(r-1)!/(2n+r-1)! - r!/(2n+r)!`. The coefficients are absolutely summable;
the resulting uniformly convergent Fourier series equals the continuous
periodic function `y`. Thus (3) is a uniform bound, not a sampled estimate.

Modulate to avoid the common zero frequency:

\[
 Q(t)=e^{4\pi int/L}q(t)
     =\sum_{j=n}^{3n}c_je^{2\pi ijt/L},\qquad
 c_j=4^{-n}\binom{2n}{j-n},\quad c_j\ge0,\quad\sum_jc_j=1,
\]
\[
 A(t)=e^{4\pi int/L}P_n(t),\qquad R(t)=tQ(t)-A(t).
\tag{7}
\]

Both `Q` and `A` have period `L` and the specified index support. On the
central interval `|R|<=E_(L,n)`, whereas periodicity gives

\[
 R(L+s)=LQ(s)+R(s).
\tag{8}
\]

Uniformly for `|s|<=1`, `|Q(s)|=cos^(2n)(pi s/L)->1`, since `n=O(L)`.
Consequently `|R(L+s)|>=L/2` for all sufficiently large `L`. The function
`R` is an intermediate exponential polynomial with a linear factor;
the next step replaces it by two genuine cuff traces.

## 3. Exact neighboring lattices and an error relative to the escaping mass

Put

\[
 \xi_j=2\pi j/L,\quad \xi'_j=2\pi j/L',\quad
 d_j=\xi'_j-\xi_j\ne0,
\]
\[
 f_{L'}(t)=\sum_{j=n}^{3n}\frac{c_j}{id_j}e^{i\xi'_jt},\qquad
 f_L(t)=A(t)+\sum_{j=n}^{3n}\frac{c_j}{id_j}e^{i\xi_jt}.
\tag{9}
\]

These are finite exact-lattice polynomials. The elementary remainder bound
`|exp(ix)-1-ix|<=x^2/2` for real `x` implies, for all real `t`,

\[
 |g_L(t)-R(t)|
 \le\frac12\sum_jc_j|d_j|t^2
 \le\frac{3\pi n|\delta_L|}{LL'}t^2
 \le C_\alpha\frac{|\delta_L|}{L}t^2.
\tag{10}
\]

In particular, the error on `[L-1,L+1]` is `O_alpha(|delta_L|L)=o(L)`.
Equations (8) and (10), with `sech(t)>=exp(-|t|)`, prove

\[
 H[g_L]\ge cL^2e^{-L}.
\tag{11}
\]

On the central interval, use (3), (10), `integral sech(t)dt=pi`, and the
finite fourth weighted moment. This gives

\[
 \int_{-L/2}^{L/2}|g_L|^2\operatorname{sech}t\,dt
 \le 2\pi E_{L,n}^2+C_\alpha\delta_L^2/L^2.
\tag{12}
\]

Dividing (12) by (11) proves (2). The two terms tend to zero by
`alpha log(16)>1` and (1). This quantitative estimate matters: convergence
of divided differences for each fixed `L` alone would not justify a joint
limit in which the escaping weighted mass is exponentially small.

## 4. Exact cotangent geometry realizes the control

Consider the infinite endpoint-label sequence `x_m=6m+3`, `m>=1`, all of
whose labels are composite, with `u_m=cot(pi/x_m)`. Consecutive triples
are `P,P+a,P+2a`, `a=6`. Use the same exact cuff and prescribed-window
formulas as PF-001 and PF-367:

\[
 F(x)=\log\cot(\pi/x),\quad
 h=F(P+a)-F(P),\quad h'=F(P+2a)-F(P+a),
\]
\[
 L=2\log\coth(h/4),\quad L'=2\log\coth(h'/4),\quad
 s=(h+h')/2,
\]
\[
 T=\operatorname{arsinh}(\vartheta/\sinh s)-1,
 \qquad 0<\vartheta<1\text{ fixed sufficiently small}.
\tag{13}
\]

For fixed `a`, differentiating `F` gives
`F'(x)=1/x+O(x^-3)` and `F''(x)=-1/x^2+O(x^-4)`. Hence, with the
derivative taken in `P` while `a` is fixed,

\[
 h=a/P+O(P^{-2}),\qquad
 \frac{dh}{dP}=-a/P^2+O(P^{-3}),\qquad
 \frac{dL}{dP}=-\frac{dh/dP}{\sinh(h/2)}=2/P+O(P^{-2}).
\]

Integration from `P` to `P+a`, and the exact identity
`exp(-L/2)=tanh(h/4)`, now give

\[
 \boxed{\delta_L=L'-L=2a/P+O(P^{-2})
                =(8+o(1))e^{-L/2}>0.}
\tag{14}
\]

This satisfies (1). The actual prescribed window obeys

\[
 L/2=\log(4P/a)+o(1),\quad
 T=\log(2\vartheta P/a)-1+o(1),
\]
\[
 \boxed{L/2-T=\log(2/\vartheta)+1+o(1)>0.}
\tag{15}
\]

Consequently the residuals (9) escape these actual windows on every
sufficiently far module of this control flute. With `alpha=1/2`, (2)
is `O(L^-4)`; the other term is exponentially smaller.

The same windows satisfy `T/L->1/2` and `T/L'->1/2`. By the scalar
theorem in PF-368, **each individual fixed-band trace** on either cuff
concentrates in this window, uniformly in its coefficients. Their difference
does not. There is no conflict: the large central parts cancel to much
higher relative precision than a bound in `H[f_L]+H[f_(L')]` can detect.

For the actual prime flute, (1), together with `T_i<=L_i/2` from PF-367,
is a sufficient conditional obstruction on any subsequence satisfying it.
This finding does not establish such a prime subsequence. No power-sized
neighboring gap jump was used in the composite realization; PF-367's
single-cuff packet escape condition therefore does not classify coupled
two-cuff cancellation.

## 5. What this excludes, and what remains

- Exact cotangent sampling, sublinear endpoint gaps, `L'/L->1`, and
  `T/L,T/L'->1/2` do not suffice for a coefficient-uniform, broad-band
  coupled comparison. The counterexample uses the prescribed full window,
  not a smaller certified subwindow.
- The periods must be distinct. At `L'=L` the divided differences in (9)
  are unavailable and the union collapses to a single lattice. The
  coefficient-uniform question is singular at that limit. The sufficient
  closeness scale (1) is not asserted to be necessary.
- The scalar theorem allows arbitrary coefficients. In (9), `f_(L')`
  has coefficient absolute sum `Theta_alpha(L/|delta_L|)`, hence
  exponential growth in the control (14). Scaling both traces changes
  neither the ratio (2) nor their relative energy costs. Nonsingular
  coefficient, tangential, mass and seam costs cannot be discarded when
  asking whether these are actual minimizing residuals.
- PF-361's sufficiently narrow combined-band theorem is unchanged. No
  narrow-band counterexample, full pant-energy comparison, global
  transition minimizer, compactness/Schatten conclusion, or RH consequence
  is proved here. The construction is neither a new intrinsic spectral
  observable nor a detector of primality.

The remaining broad-band argument must exploit arithmetic that excludes
the relevant period regime, restrictions on the minimizing fields, or
coercive energy beyond the scalar difference. Separate single-cuff
concentration and asymptotic period agreement cannot supply that argument.

## 6. Prior art and validation

Equation (4) is the classical cosine beta integral
[DLMF 5.12.5](https://dlmf.nist.gov/5.12#E5), combined with the beta/gamma
identity. Fourier partial sums, the binomial window and the tail telescoping
are classical ingredients. The discarded-coefficient estimate (3) and its
use in (2) are derived explicitly here; no new general Fourier approximation
theorem is claimed.

S. A. Avdonin and S. A. Ivanov, *Exponential Riesz bases of subspaces and
divided differences*, [primary manuscript](https://arxiv.org/abs/math/0103160),
Introduction and Section 2.2, treats clustered exponentials through divided
differences and their polynomial-times-exponential limits. This is the
closest mechanism behind (9). Its Riesz-basis theorem is not needed or
imported into the weighted, growing-period estimate above. The explicit
remainder (10) handles the relevant joint limit.

The literature audit also checked the Turan--Nazarov concentration theorem
used in PF-361 (S34); its term-count dependence is consistent with this
broad-band construction. The derived local addition is the quantitative
two-exact-lattice residual, its realization by the sampled composite flute,
and the failure of a proposed inference from separate concentration. No
novelty claim rests on failure to find identical wording.

Supplementary standard-library checks used exact rational arithmetic for
(6), including its finite-sum remainder, at `n=1,...,32`. At 100-digit
Decimal precision, `L=20,40,80,120`, `n=L/2`, and
`delta=8 exp(-L/2)` passed (3) and (10) at 81 central sample points per
period and the lower witness `|g_L|>L/4` at `L-1,L,L+1`.
For exact composite triples `P=6*10^k+3`, `a=6`,
`k=6,12,24,36`, direct cotangent/cuff evaluation gave
`delta exp(L/2)->8` and, for `vartheta=0.1`,
`L/2-T->1+log(20)`. These are finite factor/sign checks, not interval
certificates, prime evidence, or pant-PDE computations. Scratch stays
outside Git; the displayed proof establishes the result.

A standalone formalization of the beta coefficient identity would not
settle either prime realization or the omitted energy terms. No compute
or formalization handoff is proposed for that peripheral step.
