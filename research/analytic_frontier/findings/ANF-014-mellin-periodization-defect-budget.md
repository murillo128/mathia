# ANF-014 — a Mellin periodization identity leaves only a 0.0235 defect budget below Montgomery--Taylor

**Status:** `EXACT-DERIVED + CLASSICAL-MELLIN-BRIDGE + EXTREMAL-REDUCTION + STRUCTURAL-BOUNDARY`. In the residual positive-spectral affine branch isolated by `ANF-012`--`ANF-013`, the BGSST pair cost is not independent of the all-scale lattice periodization. A Mellin transform of that periodization gives the exact identity

\[
C(J)=\left(1-\frac{3}{\pi^2}\right)J(0)
+\frac{6}{\pi^2}\int_1^\infty \frac{P_J(h)}{h^2}\,dh.
\]

After normalizing by the periodization floor `p(J)`, this becomes a positive defect decomposition above the universal lattice floor `1+3/pi^2 = 1.3039635509...`. Since Montgomery--Taylor sits only `0.0235357454...` above that floor, every surviving scalar profile must be quantitatively close to simultaneous saturation of **all** duplicated-lattice constraints. In particular, the Möbius profile introduced in `ANF-013` is no longer merely a deliberately stronger boundary ansatz: it is the exact equality case of this Mellin lower bound, if equality is attainable.

## 1. Residual periodization problem

Retain the hypotheses of `ANF-013`. Let `J` be continuous, real-even, nonnegative and supported in `[-1,1]`, and define

\[
P_J(h):=\frac1h\sum_{k\in\mathbb Z}J(k/h),
\qquad
p(J):=\inf_{h>0}P_J(h),
\tag{1}
\]

and

\[
C(J):=J(0)+2\int_0^1 \alpha J(\alpha)\,d\alpha.
\tag{2}
\]

Continuity together with compact support gives `J(1)=0`. For `0<h<1` only the `k=0` term occurs in (1), so

\[
P_J(h)=\frac{J(0)}h\ge J(0),
\]

while `P_J(1)=J(0)`. Hence

\[
\boxed{p(J)=\inf_{h\ge1}P_J(h)\le J(0).}
\tag{3}
\]

If `p(J)=0`, `ANF-013` already shows that the lattice family cannot support a positive affine lower bound. The only live case is therefore `p(J)>0`.

## 2. Mellin transform of the lattice periodization

For `h>=1`, evenness and `J(1)=0` give

\[
hP_J(h)-J(0)
=2\sum_{1\le k\le h}J(k/h),
\tag{4}
\]

where including an endpoint `k=h` is harmless. Fix a real `s>1`. Since every term is nonnegative, Tonelli's theorem allows the sum and integral to be interchanged:

\[
\begin{aligned}
\int_1^\infty
\bigl(hP_J(h)-J(0)\bigr)h^{-s-1}\,dh
&=2\sum_{k\ge1}\int_k^\infty J(k/h)h^{-s-1}\,dh.
\end{aligned}
\tag{5}
\]

With `alpha=k/h`, each summand is

\[
\int_k^\infty J(k/h)h^{-s-1}\,dh
=k^{-s}\int_0^1 J(\alpha)\alpha^{s-1}\,d\alpha.
\tag{6}
\]

Therefore

\[
\boxed{
\int_1^\infty
\bigl(hP_J(h)-J(0)\bigr)h^{-s-1}\,dh
=2\zeta(s)\int_0^1J(\alpha)\alpha^{s-1}\,d\alpha
\qquad(s>1).
}
\tag{7}
\]

The appearance of `zeta(s)` is the standard Mellin/Dirichlet-series mechanism behind Müntz-type formulas: dilation sums become multiplication by a Dirichlet series under Mellin transform. The exact specialization (7) is elementary and needs no analytic continuation.

## 3. At `s=2`, the Mellin moment is exactly the BGSST pair cost

Set `s=2` in (7). Since

\[
\int_1^\infty J(0)h^{-3}\,dh=\frac{J(0)}2,
\]

we obtain

\[
\int_1^\infty\frac{P_J(h)}{h^2}\,dh-\frac{J(0)}2
=2\zeta(2)\int_0^1\alpha J(\alpha)\,d\alpha.
\tag{8}
\]

Using `zeta(2)=pi^2/6` in (2) gives the exact cost identity

\[
\boxed{
C(J)=\left(1-\frac{3}{\pi^2}\right)J(0)
+\frac{6}{\pi^2}\int_1^\infty\frac{P_J(h)}{h^2}\,dh.
}
\tag{9}
\]

Thus the BGSST cost appearing in the zeta-zero bound is itself a weighted average of the same periodized lattice energies that constrain the deterministic intercept in `ANF-013`. The two sides of the ratio `C(J)/p(J)` are not independent optimization variables.

Normalize by `p=p(J)>0`. Subtract the pointwise lower bounds `J(0)>=p` and `P_J(h)>=p` from (9). Since `int_1^infinity h^{-2}dh=1`, one gets

\[
\boxed{
\begin{aligned}
\frac{C(J)}p
={}&1+\frac{3}{\pi^2}\\
&+\left(1-\frac{3}{\pi^2}\right)
  \left(\frac{J(0)}p-1\right)\\
&+\frac{6}{\pi^2}\int_1^\infty
  \left(\frac{P_J(h)}p-1\right)\frac{dh}{h^2}.
\end{aligned}
}
\tag{10}
\]

Every term after the first line is nonnegative. Hence the lattice constraints alone imply the universal floor

\[
\boxed{
\frac{C(J)}{p(J)}\ge
c_*:=1+\frac{3}{\pi^2}
=1.3039635509270133\ldots .
}
\tag{11}
\]

This does **not** reach Montgomery--Taylor, but it identifies exactly what additional gap a complete scalar no-go theorem must force.

## 4. A sub-Montgomery--Taylor profile has only a `0.0235357...` defect budget

Recall from `ANF-013`

\[
C_{\rm MT}
=\frac12+\frac1{\sqrt2}\cot\frac1{\sqrt2}
=1.3274992963205883\ldots .
\tag{12}
\]

Define the remaining lattice-margin budget

\[
\boxed{
\Delta_{\rm MT}:=C_{\rm MT}-c_*
=0.0235357453935750\ldots .
}
\tag{13}
\]

Combining the necessary survival condition `C(J)/p(J)<C_MT` from `ANF-013` with (10) gives the stronger equivalent necessary condition

\[
\boxed{
\left(1-\frac{3}{\pi^2}\right)
\left(\frac{J(0)}p-1\right)
+\frac{6}{\pi^2}\int_1^\infty
\left(\frac{P_J(h)}p-1\right)\frac{dh}{h^2}
<\Delta_{\rm MT}.
}
\tag{14}
\]

Because both defects are nonnegative, every survivor separately satisfies

\[
\boxed{
\frac{J(0)}p<1.0338139553250711\ldots
}
\tag{15}
\]

and

\[
\boxed{
\int_1^\infty
\left(\frac{P_J(h)}p-1\right)\frac{dh}{h^2}
<0.0387147493865578\ldots .
}
\tag{16}
\]

The remaining spatial-sign escape from Montgomery--Taylor is therefore forced into a narrow near-saturation cone. It is not enough for `P_J` merely to stay positive: its weighted excess above its global floor must be very small, and the diagonal sample `J(0)` must lie within about `3.38%` of that floor.

## 5. Perfect lattice saturation is the equality case, not merely an ansatz

Equality in (11) requires both nonnegative defect terms in (10) to vanish. Thus

\[
J(0)=p
\tag{17}
\]

and

\[
P_J(h)=p
\quad\text{for almost every }h\ge1.
\tag{18}
\]

The function `P_J` is continuous on `[1,infinity)`: away from integer `h` it is a finite sum of continuous terms, and at an integer a newly entering endpoint term has value `J(1)=0`. Therefore (18) strengthens to

\[
\boxed{P_J(h)=p\qquad\text{for every }h\ge1.}
\tag{19}
\]

After scaling `J` by `1/p`, equations (17)--(19) are exactly the perfect-saturation conditions introduced in `ANF-013`. Its Möbius inversion therefore describes the **unique formal equality boundary** of the Mellin floor:

\[
J(1/t)
=\frac12\left(
t\sum_{n\le t}\frac{\mu(n)}n-M(t)
\right),
\qquad t\ge1.
\tag{20}
\]

This does not show that equality is attained in the admissible nonnegative continuous class. Indeed, `ANF-013` deliberately made no such claim. The new point is logical: any sequence attempting to drive `C/p` down toward `c_*` must, in the weighted sense of (10), approach the same all-scale saturation boundary.

## 6. Consequence for the residual scalar branch

`ANF-013` reduced the scalar problem to deciding whether `C(J)/p(J)<C_MT` is possible. Equation (10) turns that ratio test into a quantified stability problem. A lattice-only no-go theorem reaching Montgomery--Taylor must prove that compatibility of one continuous nonnegative profile `J` with its entire family of periodizations forces at least

\[
\Delta_{\rm MT}=0.0235357453\ldots
\]

of total defect in (14). Conversely, an explicit profile with defect below that threshold would survive all the current thermodynamic lattice tests, but it would still need the complete universal affine counting inequality on arbitrary conjugation-invariant complex multisets.

This sharpens the next search target. Optimizing arbitrary positive spectra is too broad; the only candidates worth testing are profiles whose periodization is almost flat at its minimum across the `h^{-2}` Mellin measure. The exact Möbius equality profile from `ANF-013` is the natural boundary object around which either a stability obstruction or a near-saturating counterexample must be built.

The configuration-level escape established in `ANF-006` is unaffected. Nothing in (7)--(16) constrains non-affine, ordered-gap, higher-order, matrix/inertia-before-compression, or zeta-specific mechanisms that do not reduce to one universal affine scalar pair kernel.

## 7. Prior-art and novelty boundary

Mellin transforms of dilation sums and the resulting multiplication by `zeta(s)` are classical Müntz-formula territory. A modern reference is Hélder Lima, **On Müntz-type formulas related to the Riemann zeta function**, *Journal of Mathematical Analysis and Applications* 463:1 (2018), 398--411, DOI `10.1016/j.jmaa.2018.03.029`, which develops this Mellin/Dirichlet-series mechanism in a broader setting. No novelty is claimed for that general transform principle, for `zeta(2)=pi^2/6`, or for Tonelli's theorem.

The Mathia-specific contribution is the specialization to the exact periodization and BGSST cost already forced by `ANF-013`: equation (10) converts the residual `C/p` extremal problem into a sum of two nonnegative saturation defects and shows that the entire numerical room below Montgomery--Taylor is only `Delta_MT`. A targeted search did not locate this exact defect decomposition in the universal simple-critical-zero affine-certificate setting. No publication-level novelty claim is made.

## 8. Decisive audit boundary

The identity is exact under the stated hypotheses. It would fail only through a normalization error in `P_J`, an invalid exchange in (5), or an incorrect `s=2` conversion to the BGSST cost. Nonnegativity of `J` makes Tonelli immediate, and the substitution in (6) fixes the zeta factor and all powers explicitly.

The structural conclusions require `p(J)>0`; the `p=0` case was already killed by `ANF-013`. The floor `c_*` is **not** asserted to be sharp or attainable in the admissible class, and (14) is a necessary condition, not a construction of a universal affine certificate. In particular, this finding does not prove `C(J)/p(J)>=C_MT` and does not close the residual scalar branch. Its decisive next test is narrower: prove that admissibility plus the remaining universal constraints force the total defect in (14) to be at least `Delta_MT`, or construct a profile strictly below that defect threshold and then subject it to the full complex-configuration inequality.
