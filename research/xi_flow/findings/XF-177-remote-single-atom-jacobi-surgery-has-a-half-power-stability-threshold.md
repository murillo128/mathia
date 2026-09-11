---
type: theorem
research_line: xi_flow
finding_id: XF-177
status: canonical
---

# XF-177 — Remote single-atom Jacobi surgery has a half-power stability threshold

**Evidence classification:** `EXACT-DERIVED + SHARP-SCALING + INVERSE-STABILITY-NO-GO`. XF-176 gives exact rigidity: exact Jacobi reciprocity plus asymptotic Xi atom matching forces the integer comb. The present finding stress-tests the quantitative version of that statement. Moving one unit-mass atom from `N` to `N+delta`, with fixed `0<delta<1/2`, preserves positivity, uniform separation, unit weights, and even eventual exact agreement with the Xi comb, while its real-axis Jacobi defect tends to zero. More precisely, if the defect is measured with small-`x` weight `x^(-alpha)`, then its norm is asymptotic to an explicit constant times `delta N^(2 alpha-1)`. Thus every weight weaker than `x^(-1/2)` is blind to a fixed absolute remote displacement, while the half-power weight is the sharp single-atom threshold. Any fixed collection of logarithmic scale derivatives has the same threshold. No specialized external theorem is load-bearing.

## Statement

Fix

\[
0<\delta<\frac12.
\tag{1}
\]

For an integer `N>=2`, start from the integer comb and move only the symmetric pair at `+-N` to `+-(N+delta)`:

\[
\boxed{
\rho_{N,\delta}
:=\delta_0
+\sum_{\substack{n\ge1\\n\ne N}}
 (\delta_n+\delta_{-n})
+\delta_{N+\delta}+\delta_{-(N+\delta)}.
}
\tag{2}
\]

Its positive support can be numbered by

\[
r_n=n\quad(n\ne N),
\qquad
r_N=N+\delta,
\tag{3}
\]

with every mass equal to one. Hence

\[
\inf_n(r_{n+1}-r_n)\ge1-\delta>\frac12,
\qquad
r_n-n\to0,
\qquad
w_n\to1.
\tag{4}
\]

So `(2)` satisfies the asymptotic matching and sparsity hypotheses of XF-176 as strongly as possible: it is exactly Xi outside one finite atom surgery. It cannot satisfy exact Jacobi reciprocity unless `delta=0`.

Let

\[
\Theta_{N,\delta}(x)
:=\langle\rho_{N,\delta},e^{-\pi x(\cdot)^2}\rangle
\qquad(x>0)
\tag{5}
\]

and define its real-axis Jacobi residual

\[
\boxed{
\mathcal J_{N,\delta}(x)
:=\Theta_{N,\delta}(x)
-x^{-1/2}\Theta_{N,\delta}(1/x).
}
\tag{6}
\]

For `0<=alpha<1`, put

\[
\|\mathcal J\|_\alpha
:=\sup_{x>0}x^{-\alpha}|\mathcal J(x)|.
\tag{7}
\]

Then, as `N->infinity`,

\[
\boxed{
\|\mathcal J_{N,\delta}\|_\alpha
=
C_\alpha\,\delta\,N^{2\alpha-1}
\bigl(1+o(1)\bigr),
}
\tag{8}
\]

where

\[
\boxed{
C_\alpha
=4\pi^\alpha
\left(\frac{1-\alpha}{e}\right)^{1-\alpha}.
}
\tag{9}
\]

In particular,

\[
\boxed{
\|\mathcal J_{N,\delta}\|_0
\sim\frac{4\delta}{eN},
}
\tag{10}
\]

while

\[
\boxed{
\|\mathcal J_{N,\delta}\|_{1/2}
\longrightarrow
2\sqrt{\frac{2\pi}{e}}\,\delta.
}
\tag{11}
\]

Therefore every `alpha<1/2` gives

\[
\|\mathcal J_{N,\delta}\|_\alpha\to0
\tag{12}
\]

although the support never approaches the integer comb in uniform absolute displacement:

\[
\boxed{
\sup_n|r_n-n|=\delta.
}
\tag{13}
\]

The same scaling survives any fixed number of logarithmic scale derivatives. With

\[
L:=x\frac{d}{dx},
\tag{14}
\]

for every fixed integer `k>=0` and every `0<=alpha<1`,

\[
\boxed{
\sup_{x>0}
 x^{-\alpha}|L^k\mathcal J_{N,\delta}(x)|
=O_{k,\alpha,\delta}\!\left(N^{2\alpha-1}\right).
}
\tag{15}
\]

Thus at `alpha=0`, `mathcal J_(N,delta)->0` in every seminorm

\[
p_k(f):=\sup_{x>0}|L^kf(x)|,
\tag{16}
\]

even though `(13)` stays fixed. Exact Jacobi rigidity from XF-176 consequently has no continuous inverse from this natural logarithmic `C^infinity` defect topology to uniform absolute atom placement.

## 1. One remote atom gives an exact two-scale residual

Write the ordinary theta comb as `delta_Z`. Since it obeys Jacobi exactly, only the moved pair contributes to `(6)`. Define

\[
A_{N,\delta}(x)
:=e^{-\pi(N+\delta)^2x}-e^{-\pi N^2x}.
\tag{17}
\]

Then

\[
\boxed{
\mathcal J_{N,\delta}(x)
=2\left[
 A_{N,\delta}(x)
-x^{-1/2}A_{N,\delta}(1/x)
\right].
}
\tag{18}
\]

Set

\[
h:=\frac\delta N,
\qquad
y:=N^2x,
\qquad
v:=\frac{N^2}{x},
\qquad
yv=N^4,
\tag{19}
\]

and

\[
F_h(t):=e^{-\pi(1+h)^2t}-e^{-\pi t}.
\tag{20}
\]

Equation `(18)` becomes the exact identity

\[
\boxed{
\frac12\mathcal J_{N,\delta}(x)
=F_h(y)-\frac{\sqrt v}{N}F_h(v).
}
\tag{21}
\]

This separates the scale where the moved atom is directly visible, `x~N^(-2)`, from the reciprocal Jacobi image. The latter carries an additional factor `N^(-1)` after the natural rescaling.

## 2. The direct term has the sharp `N^(2 alpha-1)` scale

For `h->0`, differentiation in `h` gives

\[
\frac{F_h(t)}h
\longrightarrow
-2\pi t e^{-\pi t}.
\tag{22}
\]

For every fixed `0<=alpha<1`, this convergence is uniform after multiplication by `t^(-alpha)`. Indeed, the first two `h`-derivatives are a polynomial in `t` times `e^(-pi(1+h)^2t)`, and

\[
\sup_{t>0}t^{1-\alpha}e^{-ct}<\infty
\qquad(c>0).
\tag{23}
\]

Hence

\[
\sup_{t>0}
 t^{-\alpha}|F_h(t)|
=
2\pi|h|
\sup_{t>0}t^{1-\alpha}e^{-\pi t}
+o(|h|).
\tag{24}
\]

The maximizer is

\[
t_\alpha=\frac{1-\alpha}{\pi},
\tag{25}
\]

so

\[
\sup_{t>0}t^{1-\alpha}e^{-\pi t}
=
\left(\frac{1-\alpha}{\pi}\right)^{1-\alpha}
 e^{-(1-\alpha)}.
\tag{26}
\]

For the first term in `(21)`, `x^(-alpha)=N^(2alpha)y^(-alpha)`. Combining `(19)`, `(24)`, and `h=delta/N` therefore gives

\[
2\sup_{x>0}
 x^{-\alpha}|F_h(N^2x)|
=
C_\alpha\delta N^{2\alpha-1}
\bigl(1+o(1)\bigr),
\tag{27}
\]

with exactly the constant `(9)`.

## 3. The reciprocal image is lower order

Using `x=N^2/v`, the weighted reciprocal term in `(21)` is

\[
x^{-\alpha}\frac{\sqrt v}{N}F_h(v)
=
N^{-2\alpha-1}
 v^{\alpha+1/2}F_h(v).
\tag{28}
\]

The mean-value formula

\[
F_h(v)
=-2\pi v
\int_0^h
(1+s)e^{-\pi(1+s)^2v}\,ds
\tag{29}
\]

shows, uniformly for small positive `h`, that

\[
\sup_{v>0}
 v^{\alpha+1/2}|F_h(v)|
=O_\alpha(h).
\tag{30}
\]

Thus `(28)` is

\[
O_{\alpha,\delta}\!\left(N^{-2\alpha-2}\right),
\tag{31}
\]

which is negligible compared with `N^(2alpha-1)` for every `alpha>=0`. This proves `(8)`. At `alpha=0`, `(9)` gives `(10)`; at `alpha=1/2`, it gives `(11)`.

The same argument proves `(15)`. On the direct term, `L` acts as `y d/dy`; on the reciprocal term it acts as `-v d/dv` on `N^(-1)sqrt(v)F_h(v)`. Any fixed number of such derivatives only inserts a fixed polynomial in the rescaled variable before the same exponential, so it does not change the power of `N`.

## 4. The XF-176 inverse is discontinuous in absolute support distance

Each comb `(2)` has eventual exact Xi matching, not merely asymptotic matching. In particular, XF-176 says that if its Jacobi residual vanished identically, the surgery would have to disappear. But `(10)` and `(15)` show that a fixed surgery can be moved to arbitrarily large index while the full real-axis Jacobi residual, together with every fixed logarithmic scale derivative, tends to zero.

Consequently there is no function `omega(epsilon)->0` such that a bound of the form

\[
\sup_n|r_n-n|
\le
\omega\!\left(
\max_{0\le k\le K}
 \sup_{x>0}|L^k\mathcal J(x)|
\right)
\tag{32}
\]

can hold uniformly over this positive uniformly separated matched-comb class for any fixed `K`. In fact the counterexample is stronger: all seminorms `(16)` tend to zero along the same sequence.

The XF-175 logarithmic Laplace displacement of the moved atom is

\[
a_N
=\frac14\log\frac{\pi(N+\delta)^2}{\pi N^2}
=\frac12\log\left(1+\frac\delta N\right)
=\frac\delta{2N}+O(N^{-2}).
\tag{33}
\]

Thus

\[
\boxed{
N|a_N|\longrightarrow\frac\delta2,
}
\tag{34}
\]

while the unweighted Jacobi residual is only order `|a_N|`. Equivalently, the absolute Laplace displacement is

\[
\widetilde\lambda_N-\pi N^2
=2\pi\delta N+\pi\delta^2,
\tag{35}
\]

which grows linearly even as `(10)` tends to zero. The natural unweighted Jacobi topology therefore sees the **relative logarithmic scale error**, not the index-amplified absolute matching scale used by XF-176.

## 5. Relation to XF-175 and the remaining quantitative gate

XF-175 showed that fixed-strip Xi transform geometry is Gaussian-blind to remote atom motion. For the present fixed spatial displacement, `(33)` and the XF-175 shell derivative asymptotic give a transform perturbation no larger than

\[
O_q\!\left(\delta N^3e^{-\pi N^2}
\right)
\tag{36}
\]

on every fixed horizontal strip. The real-axis Jacobi scan is therefore much more sensitive than finite-height zero geometry: it sees the same remote surgery at polynomial order `1/N` rather than Gaussian order `e^(-pi N^2)`. Nevertheless, `(10)` shows that this extra modular sensitivity is still insufficient to recover fixed absolute atom placement uniformly in the index.

The half-power threshold in `(8)` identifies the minimum small-`x` amplification required even for this simplest inverse problem. Since the atom at spatial radius `N` is resolved at heat scale `x~N^(-2)`, multiplying the defect by `x^(-1/2)~N` exactly compensates the `1/N` loss. Equation `(11)` proves this necessity and sharpness for one-atom surgery only; it does **not** prove that the half-power norm controls arbitrary many-atom deformations, where cancellations may introduce a new obstruction.

The quantitative route left by XF-176 should therefore not ask for stability in an unweighted or sub-half-power real-axis Jacobi norm. A viable theorem must either use an index-resolving modular norm at least as strong as the half-power scale suggested here, impose a structural condition that transports remote errors to low spectral indices, or target a weaker tail metric aligned with relative logarithmic displacement. Only after such a source-side stability theorem exists does comparison with height-growing Xi contour margins become meaningful.

## Stress tests and boundary conditions

The construction is positive, even, uniformly separated, and has exactly unit masses. It does not exploit signed cancellation, loss of sparsity, a bad tail density, or a failure of XF-176's asymptotic matching. Its only missing hypothesis is exact Jacobi reciprocity, replaced by a defect that vanishes quantitatively.

The threshold `alpha=1/2` is not asserted as a global sufficiency theorem. It is a **necessary single-atom inverse-stability threshold** for norms of the form `(7)`. Multi-atom cancellation can only make the inverse problem harder.

The result also does not weaken XF-176. Exact defect zero remains rigid. It shows that the exact theorem is not continuously invertible in the stated weak modular topologies, so a quantitative version needs a stronger topology or extra source structure.

## Prior-art and novelty audit

The exact qualitative rigidity input remains the Fourier-quasicrystal/Favorov framework already recorded for XF-176, but no part of that theorem is needed for the calculation `(17)--(31)`. A targeted search of perturbative Poisson-summation, Fourier-quasicrystal stability, and perturbed-lattice literature found neighboring continuity and statistical-stability questions, not an inverse estimate for this Xi/Jacobi Gaussian residual with the explicit `alpha=1/2` threshold. No external result is therefore load-bearing and `SOURCES.md` needs no new dependency.

No broad novelty claim is made for the elementary Gaussian asymptotics themselves. The durable line-specific content is the exact remote-atom stress test, the sharp weighted scaling `(8)`, and the resulting obstruction to the quantitative XF-176 program.

## Consequence for `xi_flow`

XF-176 answers the qualitative cross-index question: exact Jacobi plus sufficiently fine asymptotic atom matching collapses to the Xi comb. XF-177 fixes the topology required by any quantitative continuation of that result. A fixed absolute atom error at index `N` creates only an `N^(-1)` unweighted Jacobi defect, and all fixed logarithmic derivative seminorms share that blindness. The first scale weight that can even see such a displacement uniformly is `x^(-1/2)`.

Do not spend further passes seeking a uniform absolute-support stability modulus from `sup |Jacobi defect|`, from any sub-half-power weighted version, or from finitely many logarithmic scale derivatives of those norms. The next useful source-side test is whether the half-power-weighted modular defect admits a many-atom coercive estimate under positivity/sparsity, or whether coordinated atom motions can cancel even at that critical resolution. Either outcome would materially sharpen the bridge from exact modular rigidity to finite-height transition control.