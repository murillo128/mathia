# MC-054 — Venturini closes the fixed complex completely multiplicative Liouville-close comparator escape

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Let

\[
f:\mathbb N\to\mathbb C
\]

be completely multiplicative with

\[
|f(n)|\le 1
\qquad(n\ge1),
\]

and write

\[
S_f(x)=\sum_{n\le x}f(n),
\qquad
F(s)=\sum_{n\ge1}\frac{f(n)}{n^s}.
\]

Assume that for some fixed

\[
0<\alpha<1
\]

one has

\[
S_f(x)\ll x^\alpha.
\tag{1}
\]

Let `lambda` be the Liouville function. Suppose also that `f` is at finite global ordinary pretentious distance from `lambda`:

\[
\boxed{
\mathbb D(f,\lambda;\infty)^2
=
\sum_p\frac{1+\operatorname{Re}f(p)}p
<\infty.
}
\tag{2}
\]

Then `F` has a simple zero at `s=1`, and Sergio Venturini's nonvanishing theorem (`MC-S17`) applies directly to give

\[
\boxed{
\zeta(s)\ne0
\qquad(\operatorname{Re}s>\alpha).
}
\tag{3}
\]

Thus allowing arbitrary bounded complex phases does **not** create a fixed completely multiplicative comparator that is simultaneously globally Liouville-close, independently power-cancellative, and cheaper than the corresponding zeta zero-free problem. At the RH scale, if one fixed such `f` satisfies

\[
S_f(x)=O_\varepsilon(x^{1/2+\varepsilon})
\qquad\text{for every }\varepsilon>0,
\tag{4}
\]

then RH follows.

The zero-free implication `(3)` is established prior art: it is exactly the type of conclusion proved by Venturini for bounded completely multiplicative Dirichlet series that are holomorphic in a left half-plane and vanish at `1`. The line-specific derived point is that, under the independent power bound `(1)`, the apparently separate source hypothesis `F(1)=0` is already forced by the ordinary global Liouville distance `(2)`, even for complex-valued `f`.

No standalone novelty claim is made.

## 1. Power cancellation makes the comparator Dirichlet series holomorphic past `1`

Partial summation gives

\[
F(s)
=s\int_1^\infty S_f(x)x^{-s-1}\,dx
\tag{5}
\]

throughout

\[
\operatorname{Re}s>\alpha.
\tag{6}
\]

Hence `F` is holomorphic on the exact half-plane needed below, and in particular in a neighborhood of `s=1`.

This step uses only the independently proposed comparator estimate `(1)`. No zero-free region for zeta and no continuation of `1/zeta` has entered.

## 2. Global Liouville closeness forces an exact simple zero at `s=1`

For real `sigma>1`, complete multiplicativity gives

\[
F(\sigma)
=
\prod_p\left(1-f(p)p^{-\sigma}\right)^{-1}.
\tag{7}
\]

The Liouville Dirichlet series is

\[
L_\lambda(s)
:=
\sum_{n\ge1}\frac{\lambda(n)}{n^s}
=
\prod_p(1+p^{-s})^{-1}
=
\frac{\zeta(2s)}{\zeta(s)}.
\tag{8}
\]

Therefore

\[
R_f(\sigma)
:=
\frac{F(\sigma)}{L_\lambda(\sigma)}
=
\prod_p
\frac{1+p^{-\sigma}}
     {1-f(p)p^{-\sigma}}.
\tag{9}
\]

Put `u=p^{-sigma}`. Uniformly for `|a|<=1` and real `sigma>=1`,

\[
\log\left|\frac{1+u}{1-au}\right|
=
(1+\operatorname{Re}a)u+O(u^2).
\tag{10}
\]

Indeed, `log(1+u)=u+O(u^2)` and

\[
\log|1-au|
=-\operatorname{Re}(a)u+O(u^2),
\]

with an absolute uniform remainder because `u<=1/2` at the smallest prime and `|a|<=1`.

Now `(2)` makes the first-order prime terms at `sigma=1` summable, while

\[
\sum_p p^{-2}<\infty.
\]

Since `1+Re f(p)>=0`, dominated convergence in `(10)` yields

\[
\boxed{
|R_f(\sigma)|\longrightarrow C_f
\in(0,\infty)
\qquad(\sigma\downarrow1).
}
\tag{11}
\]

The phase of `R_f` need not converge. That is irrelevant: only its modulus is needed.

From the pole of zeta at `1`,

\[
L_\lambda(\sigma)
=
\frac{\zeta(2\sigma)}{\zeta(\sigma)}
\sim
\zeta(2)(\sigma-1).
\tag{12}
\]

Combining `(9)`--`(12)` gives

\[
\boxed{
\frac{|F(\sigma)|}{\sigma-1}
\longrightarrow
C_f\zeta(2)
\in(0,\infty).
}
\tag{13}
\]

But `F` is holomorphic at `1` by `(6)`. Hence `(13)` forces

\[
F(1)=0,
\qquad
F'(1)\ne0.
\tag{14}
\]

Thus the zero is exactly simple. This is the completely multiplicative analogue of the boundary-modulus argument in `MC-052`: complex phases can destroy coefficientwise positivity, but finite ordinary distance still fixes enough modulus at the Liouville quotient boundary to force the pole-cancelling zero.

## 3. Venturini turns the automatic boundary zero into the matching zeta zero-free half-plane

Venturini (`MC-S17`) proves the following established nonvanishing principle: if `a(n)` is bounded and completely multiplicative, its Dirichlet series

\[
L(s)=\sum_{n\ge1}a(n)n^{-s}
\]

extends holomorphically to

\[
\operatorname{Re}s>1-\delta
\]

for some `delta>0`, and `L(1)=0`, then that whole half-plane is zero-free for the Riemann zeta function.

Apply the theorem to the present `f` with

\[
\delta=1-\alpha.
\]

Equation `(6)` supplies the required holomorphic continuation and `(14)` supplies the required zero at `1`. Therefore

\[
\zeta(s)\ne0
\qquad(\operatorname{Re}s>\alpha),
\]

which is `(3)`.

The proof does not derive `(3)` by contour shifting, by assuming the desired continuation of `1/zeta`, or by an RH-equivalent Möbius estimate. The zero-free conclusion enters through the independently established Venturini theorem once the comparator hypotheses have been shown to imply its analytic interface.

## 4. The RH-scale consequence

Suppose `(2)` holds for one fixed bounded completely multiplicative `f` and `(4)` holds for every positive `epsilon`.

For arbitrary

\[
0<\eta<\frac12,
\]

use the instance

\[
S_f(x)=O_\eta(x^{1/2+\eta})
\]

and apply `(3)` with

\[
\alpha=\frac12+\eta.
\]

Then zeta is zero-free in every half-plane

\[
\operatorname{Re}s>\frac12+\eta.
\]

Letting `eta` vary excludes every nontrivial zero to the right of the critical line. The functional-equation symmetry then excludes every nontrivial zero to the left of it, so RH follows.

This is strategically the same burden exposed for the real completely multiplicative class in `MC-049`, but the prior-art bridge is different. Aymone's theorem used there is formulated for real coefficients in `[-1,1]` and also supplies a stronger weighted-prime conclusion. The present complex extension requires neither a real-valued reduction nor a new positivity construction: Venturini's theorem already covers bounded complex completely multiplicative coefficients once `F(1)=0` is available.

## 5. Cancellation alone is not enough

The global Liouville-closeness condition `(2)` is essential. A fixed nonprincipal Dirichlet character `chi` is completely multiplicative, bounded by one, and has bounded partial sums, hence satisfies a much stronger form of `(1).` Nevertheless the classical nonvanishing theorem gives

\[
L(1,\chi)\ne0.
\tag{15}
\]

Consequently such a character cannot also satisfy `(2)`: if it did, the argument in Section 2 would force `L(1,chi)=0`.

Thus the finding does **not** say that any bounded completely multiplicative function with excellent cancellation constrains zeta. The load-bearing information is the conjunction of independently controlled power cancellation with finite global ordinary proximity to Liouville.

The reverse implication is also deliberately not claimed in the complex class. Unlike `MC-049`, where Aymone's real-valued theorem gives an equivalence between the zero at `1` and global Liouville pretentiousness under the power bound, the present argument only needs and establishes

\[
\mathbb D(f,\lambda;\infty)<\infty
\quad\Longrightarrow\quad
F(1)=0.
\]

Venturini then supplies the zero-free consequence from the analytic zero. Nothing here proves that every complex completely multiplicative `f` with `F(1)=0` must be globally Liouville-pretentious.

## 6. Prior art and novelty boundary

Venturini, *Non vanishing of Dirichlet series of completely multiplicative functions* (`MC-S17`), is the decisive prior art. Its published abstract already states the needed theorem for a **bounded completely multiplicative function**, without a real-valued restriction: holomorphic continuation to `Re(s)>1-delta` together with `L(1)=0` forces the same half-plane to be zero-free for zeta.

`MC-049` used the neighboring real-valued result of Aymone because that theorem also identifies Liouville pretentiousness and provides a weighted prime discrepancy estimate. The end of `MC-049` therefore correctly left complex-valued completely multiplicative comparators outside that specific real theorem. The present audit shows that this was not a genuine remaining zero-free escape: the already-catalogued Venturini theorem closes it once the elementary modulus argument above makes `F(1)=0` automatic from finite global Liouville distance.

`MC-052` independently established the same simple-zero boundary phenomenon for complex square-free-supported multiplicative comparators, and `MC-053` then closed that non-completely-multiplicative square-free class using conjugate-square positivity. Those findings and the present one use different downstream mechanisms. Here complete multiplicativity places the comparator directly inside Venturini's established theorem, so no conjugate-square Landau reconstruction is needed.

Accordingly, the zero-free theorem is classical literature, the simple-zero deduction is an exact specialization of elementary Euler-product/holomorphy reasoning already visible in the current line, and **no standalone novelty claim is made**.

## 7. Consequence for the comparator frontier

The recent comparator chain has now closed three natural fixed globally-close escape classes at the exponent they were meant to simplify:

- real completely multiplicative Liouville-close comparators (`MC-049`);
- real or complex square-free-supported Möbius-close comparators (`MC-050`--`MC-053`);
- bounded complex completely multiplicative Liouville-close comparators (this finding).

A fixed comparator route that still hopes to be independently easier must therefore leave these hypotheses in a mathematically substantive way. Remaining possibilities must involve, for example, genuinely non-completely-multiplicative structure beyond the closed square-free quotient class, scale-dependent/local relations rather than finite global ordinary distance, or signed/bilinear couplings whose useful information is not summarized by one comparator summatory estimate.

The first falsification test for any future fixed bounded completely multiplicative complex comparator is now cheap: if its proposed relation to Liouville makes

\[
\sum_p\frac{1+\operatorname{Re}f(p)}p
\]

finite, then an independently proved exponent `alpha` for its partial sums already implies zeta zero-freeness in `Re(s)>alpha`. The comparator has relocated the target burden rather than weakened it.