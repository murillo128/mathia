# WP-161 — Radial cyclotomic boundary value is Mangoldt, but its differential jet is Jordan-totient

**Status:** `EXACT-DERIVED + DECISIVE-NARROWING + PRIME-CIRCLE + REAL-RADIAL-INCIDENCE + MANGOLDT-BOUNDARY-VALUE + JORDAN-TOTIENT-JET + LOCAL-CURVATURE-POSITIVITY + PRIME-POWER-SUPPORT-LOSS + MATCHED-CONTROLS + PRIOR-ART-CLASSICALIZATION` for the direct local differential/curvature use of a source-forced real radial parameter against primitive Prime-Circle shells.

`WP-158`--`WP-160` close fixed character and fixed finite-arity algebraic torsion incidence as a scalable source of mixed-prime geometry. The accepted noncharacter-incidence clue therefore leaves a genuinely different escape: let a **non-torsion real parameter** participate in the source geometry before determinant, norm, or positivity is taken.

Prime Circle has an immediate canonical test of that escape. Move the distinguished real point radially to `r=e^s` and measure its logarithmic chord product against the primitive shell of exact order `n`. After removing the forced reciprocal linear drift, the resulting centered radial potential is

\[
\mathcal R_n(s)
:=
\log\left|\Phi_n(e^s)\right|
-\frac{\varphi(n)}2\,s,
\qquad n>1.
\tag{1}
\]

This construction does escape the fixed torsion-subvariety hypothesis of `WP-160`: `s` is a genuine real deformation variable. It also contains a striking exact arithmetic boundary value,

\[
\boxed{\mathcal R_n(0)=\log\Phi_n(1)=\Lambda(n).}
\tag{2}
\]

But the arithmetic selector exists **only at zero order**. The complete centered differential germ is controlled by Jordan totients:

\[
\boxed{
\mathcal R_n(s)
=
\Lambda(n)
+
\sum_{k\ge1}
\frac{B_{2k}\,J_{2k}(n)}
{2k(2k)!}\,s^{2k},
}
\tag{3}
\]

locally around `s=0`. In particular,

\[
\boxed{
\mathcal R_n''(0)=\frac{J_2(n)}{12}>0
\quad\text{for every }n>1,
}
\tag{4}
\]

whereas `\Lambda(n)=0` on every non-prime-power `n`. Thus the first independently positive geometric response has **full shell support** and loses exactly the prime-power sparsity carried by the boundary value.

The smallest control is already decisive:

\[
\mathcal R_6(0)=0,
\qquad
\mathcal R_6''(0)=2.
\tag{5}
\]

So a source-forced real radial variable does exist and does meet the Mangoldt selector at the boundary, but direct local curvature does not transport that selector into a Weil-compatible positive form. Any surviving radial route must be genuinely nonlocal in the radial variable or introduce additional global structure before the sign theorem; it cannot claim that the local radial Hessian is the desired finite--archimedean positivity mechanism.

## 1. The radial deformation is intrinsic and non-torsion

Let

\[
P_n^*
=
\left\{
e^{2\pi i a/n}:(a,n)=1
\right\}
\tag{6}
\]

be the primitive `n`th-root shell. For a positive real radial point `r=e^s`, the total logarithmic chord potential is

\[
F_n(s)
=
\sum_{\zeta\in P_n^*}\log|e^s-\zeta|
=
\log|\Phi_n(e^s)|.
\tag{7}
\]

No coefficient depending on prime factorization has been inserted: (7) is simply the product defining the cyclotomic polynomial evaluated at the moving real point.

For `n>1`, cyclotomic reciprocity gives

\[
\Phi_n(x)=x^{\varphi(n)}\Phi_n(x^{-1}).
\tag{8}
\]

Hence subtracting the unavoidable linear drift produces (1), with exact reflection symmetry

\[
\boxed{\mathcal R_n(-s)=\mathcal R_n(s).}
\tag{9}
\]

Equivalently, if `\zeta=e^{i\theta}`,

\[
\log|e^s-\zeta|-\frac s2
=
\frac12\log\!\left(2(\cosh s-\cos\theta)\right),
\tag{10}
\]

so

\[
\boxed{
\mathcal R_n(s)
=
\frac12
\sum_{\substack{1\le a\le n\\(a,n)=1}}
\log\!\left(
2\left(\cosh s-\cos\frac{2\pi a}{n}\right)
\right).
}
\tag{11}
\]

This is a genuine metric/differential real-variable incidence outside the fixed torsion-locus category of `WP-160`. The issue is not whether such an incidence exists; it is whether its own sign-bearing differential geometry preserves the arithmetic selector.

## 2. The boundary value is exactly von Mangoldt

At `s=0`, (7) is the chord product from the point `1` to the primitive shell,

\[
e^{F_n(0)}
=
\prod_{\zeta\in P_n^*}|1-\zeta|
=
\Phi_n(1).
\tag{12}
\]

For `n>1` the classical cyclotomic value is

\[
\Phi_n(1)
=
\begin{cases}
p,&n=p^a\text{ for a prime }p,\ a\ge1,\\
1,&n\text{ has at least two distinct prime divisors}.
\end{cases}
\tag{13}
\]

Therefore

\[
\boxed{
\mathcal R_n(0)=F_n(0)=\Lambda(n).
}
\tag{14}
\]

This is not a fitted identification. It is the `m=1` boundary case of the same cyclotomic log-product/resultant geometry whose prime-power support underlies the finite Prime-Circle coefficients.

Equation (14) is nevertheless only a **scalar potential value**. Its nonnegativity does not by itself give a positive semidefinite quadratic form on Weil test functions, and `WP-001`, `WP-005`, and the later resultant findings already show why positive local Mangoldt coefficients are not equivalent to the assembled Weil sign.

## 3. Möbius factorization gives the entire radial germ

Use the standard cyclotomic product formula

\[
\Phi_n(x)
=
\prod_{d\mid n}(x^d-1)^{\mu(n/d)}.
\tag{15}
\]

For real `s>0`,

\[
\log\Phi_n(e^s)
=
\sum_{d\mid n}
\mu(n/d)
\left[
\frac{ds}{2}
+
\log\left(2\sinh\frac{ds}{2}\right)
\right].
\tag{16}
\]

Since

\[
\sum_{d\mid n}\mu(n/d)d=\varphi(n),
\tag{17}
\]

the centered profile is exactly

\[
\boxed{
\mathcal R_n(s)
=
\sum_{d\mid n}
\mu(n/d)
\log\left(2\sinh\frac{ds}{2}\right),
\qquad s>0.
}
\tag{18}
\]

The apparent logarithmic singularities at `s=0` cancel because

\[
\sum_{d\mid n}\mu(n/d)=0
\qquad(n>1).
\tag{19}
\]

Writing

\[
2\sinh\frac{ds}{2}
=
ds\,
\frac{\sinh(ds/2)}{ds/2},
\tag{20}
\]

the constant term is

\[
\sum_{d\mid n}\mu(n/d)\log d
=
\Lambda(n),
\tag{21}
\]

while the classical expansion

\[
\log\frac{\sinh z}{z}
=
\sum_{k\ge1}
\frac{2^{2k-1}B_{2k}}
{k(2k)!}\,z^{2k}
\tag{22}
\]

gives

\[
\mathcal R_n(s)
=
\Lambda(n)
+
\sum_{k\ge1}
\frac{B_{2k}}
{2k(2k)!}
\left(
\sum_{d\mid n}\mu(n/d)d^{2k}
\right)s^{2k}.
\tag{23}
\]

The inner divisor sum is the Jordan totient

\[
J_{2k}(n)
=
n^{2k}
\prod_{p\mid n}(1-p^{-2k}),
\tag{24}
\]

which proves (3).

Equivalently, the complete centered Taylor jet is

\[
\boxed{
\mathcal R_n^{(2k)}(0)
=
\frac{B_{2k}}{2k}J_{2k}(n),
\qquad
\mathcal R_n^{(2k+1)}(0)=0.
}
\tag{25}
\]

For the uncentered potential `F_n`, the only additional local datum is

\[
F_n'(0)=\frac{\varphi(n)}2.
\tag{26}
\]

Thus the radial germ has a sharp arithmetic level separation:

\[
\boxed{
\text{zero order: }\Lambda(n);
\qquad
\text{first drift: }\varphi(n)/2;
\qquad
\text{higher even jet: }J_{2k}(n).
}
\tag{27}
\]

The prime-power selector is not carried by the differential response.

## 4. The local Hessian is genuinely positive, but on the wrong support

Differentiate the root expression (11). At the boundary,

\[
\begin{aligned}
\mathcal R_n''(0)
&=
\frac12
\sum_{(a,n)=1}
\frac{1}{1-\cos(2\pi a/n)}
\\
&=
\frac14
\sum_{(a,n)=1}
\csc^2\!\left(\frac{\pi a}{n}\right)
\\
&=
\boxed{\frac{J_2(n)}{12}}.
\end{aligned}
\tag{28}
\]

The first equality makes the sign independent of any number-theoretic theorem: **each individual chord contributes a strictly positive second variation**. Hence (4) is an honest local geometric positivity statement.

But `J_2(n)>0` for every `n>1`. This destroys the load-bearing support property of (14). The exact non-prime-power control `n=6` is especially transparent because

\[
\Phi_6(x)=x^2-x+1
\tag{29}
\]

and therefore

\[
\boxed{
\mathcal R_6(s)
=
\log(2\cosh s-1).
}
\tag{30}
\]

Consequently

\[
\mathcal R_6(0)=0
\tag{31}
\]

while

\[
\boxed{
\mathcal R_6''(0)=2.
}
\tag{32}
\]

So the simplest shell on which the Mangoldt selector vanishes has a strictly positive radial Hessian. No shell normalization can reinterpret this as preservation of prime-power support without introducing an additional selector.

This is the radial analogue of the level mismatch in `WP-145`, but it is not the same construction. `WP-145` differentiates the two-shell angular resultant interaction. Here a **single primitive shell is coupled to a moving non-torsion real point**, exactly the kind of escape left open by `WP-160`, and the whole local germ can be classified by (25).

## 5. Prime-power rays make the normalization mismatch quantitative

For `n=p^a`,

\[
\Phi_{p^a}(x)
=
\frac{x^{p^a}-1}{x^{p^{a-1}}-1}.
\tag{33}
\]

Hence the centered radial profile has the exact form

\[
\boxed{
\mathcal R_{p^a}(s)
=
\log
\frac{\sinh(p^a s/2)}
{\sinh(p^{a-1}s/2)}.
}
\tag{34}
\]

At the boundary,

\[
\mathcal R_{p^a}(0)=\log p,
\tag{35}
\]

independent of the depth `a`, as required by `\Lambda(p^a)`.

Its positive curvature instead is

\[
\boxed{
\mathcal R_{p^a}''(0)
=
\frac{p^{2a}-p^{2a-2}}{12}
=
\frac{1-p^{-2}}{12}\,p^{2a}.
}
\tag{36}
\]

The exact critical half-density that turns the zero-order value into the finite Weil ray coefficient gives

\[
p^{-a/2}\mathcal R_{p^a}(0)
=
\frac{\log p}{p^{a/2}},
\tag{37}
\]

but on the curvature it gives

\[
\boxed{
p^{-a/2}\mathcal R_{p^a}''(0)
=
\frac{1-p^{-2}}{12}\,p^{3a/2}.
}
\tag{38}
\]

The target decays geometrically with prime-power depth; the positive radial Hessian grows geometrically. Even allowing a fixed power normalization cannot repair both features: cancelling the `p^{2a}` depth dependence would require a factor `p^{-2a}`, leaving `(1-p^{-2})/12`, not `\log p`.

A normalization proportional to `\Lambda(p^a)/J_2(p^a)` would of course force the desired coefficient, but that simply inserts the target arithmetic into the metric and fails the source-forcing control.

## 6. The radial potential is not even globally convex on all shells

One might try to use the full radial Hessian rather than only its boundary value. From (18),

\[
\boxed{
\mathcal R_n''(s)
=
-\frac14
\sum_{d\mid n}
\mu(n/d)d^2
\operatorname{csch}^2\!\left(\frac{ds}{2}\right).
}
\tag{39}
\]

For `n=6`, differentiating (30) gives

\[
\boxed{
\mathcal R_6''(s)
=
\frac{2(2-\cosh s)}
{(2\cosh s-1)^2}.
}
\tag{40}
\]

It is positive near `s=0` but becomes negative once

\[
s>\operatorname{arcosh}2.
\tag{41}
\]

So even after accepting the wrong full support, the log-chord radial potential does not provide a globally convex family across all arithmetic shells.

More generally, let

\[
d_0=\frac{n}{\operatorname{rad}(n)}.
\tag{42}
\]

The smallest divisor `d` for which `\mu(n/d)\ne0` is `d_0`, and therefore as `s\to+\infty`,

\[
\boxed{
\mathcal R_n''(s)
\sim
-\mu(\operatorname{rad}n)\,
d_0^2 e^{-d_0s}.
}
\tag{43}
\]

Whenever `n` has an even number of distinct prime factors, the far-radial curvature is negative. Thus the direct radial log potential has no shell-uniform convexity theorem that could serve as the global sign mechanism.

This does not exclude a different positive operator built from the radial family. It excludes reading convexity of the raw log-chord potential as that theorem.

## 7. A shared real parameter still does not create cross-prime incidence by itself

The radial variable is genuinely common and non-torsion, but the log-product remains additive over shells. If a finite collection of shell multiplicities or amplitudes `a_n` is introduced,

\[
\mathcal R(s;a)
=
\sum_n a_n\mathcal R_n(s),
\tag{44}
\]

then

\[
\boxed{
\frac{\partial^2\mathcal R}
{\partial a_m\,\partial a_n}=0
\qquad(m\ne n).
}
\tag{45}
\]

Thus merely making several shells see the same radial coordinate does not create an irreducible finite-finite interaction before scalarization. A nonlinear outer determinant, square, Schur complement, or other completion can create mixed terms, but then the mixed coupling comes from that additional operation and must pass its own canonicality and sign audit.

This matters for the accepted noncharacter-incidence clue. The radial deformation is a real example outside fixed torsion algebraic geometry, but it remains **place-separable at the logarithmic potential level**. It solves the existence-of-a-real-parameter problem, not the missing global incidence problem.

## 8. Adversarial controls and escape boundary

Several immediate repairs fail for distinct reasons.

**Use the boundary value itself.** Equation (14) gives exactly `\Lambda(n)` and is nonnegative, but it is a scalar log-product value, not a quadratic positivity theorem. Turning positive coefficients into the standard translation/autocorrelation lift returns to the indefinite finite Weil form already isolated earlier in this line.

**Use the positive Hessian.** Equation (32) kills the support match: a shell with zero Mangoldt coefficient has positive curvature. Equations (36)--(38) kill the prime-power scale match.

**Use a higher local derivative.** Equation (25) shows that every nonzero centered even derivative is a Bernoulli multiple of `J_{2k}(n)`, which is nonzero on every `n>1`; the Bernoulli signs also alternate. Higher finite-order local differential data therefore do not restore Mangoldt sparsity.

**Average over primitive vertices.** The failure is already present after the canonical full primitive-shell product. Changing to a population average divides by `\varphi(n)` and loses the exact boundary identity (14) rather than improving it.

**Matched nonarithmetic point clouds.** The positivity in (28) is generic. For any finite set of unit-circle points avoiding `1`, each centered radial log-chord has positive second derivative at `s=0`. Primitive-shell arithmetic is what makes the **product value** collapse to (13), not what proves the local sign.

The main escape left open is therefore nonlocal: an integral transform, boundary operator, quotient, or global finite--archimedean construction could use the whole radial family before taking positivity. `WP-036` is evidence that nonlocal radial operations can indeed produce nontrivial archimedean functions: its Mellin transform contains the exact `\psi(s/2)` Riemann Gamma scale. But `WP-036` also shows that the arithmetic and Gamma pieces there appear only after finite-part subtractions from the positive parent family. The present result says that the even more direct cyclotomic radial selector has the same kind of level separation already in its local germ.

## 9. Prior art and novelty audit

No new theorem about cyclotomic derivatives is claimed.

D. H. Lehmer, *Some properties of the cyclotomic polynomial*, Journal of Mathematical Analysis and Applications **15** (1966), 105--117, DOI `10.1016/0022-247X(66)90144-2`, gives classical formulas for derivatives of cyclotomic polynomials at `1` in terms of Euler/Jordan-totient data.

Andrés Herrera-Poyatos and Pieter Moree, *Coefficients and higher order derivatives of cyclotomic polynomials: old and new*, Expositiones Mathematicae **39** (2021), 309--343, DOI `10.1016/j.exmath.2019.07.003`, surveys and unifies these derivative formulas through logarithmic derivatives. Pieter Moree, Sumaia Saad Eddin, Alisa Sedunova, and Yuta Suzuki, *Jordan totient quotients*, arXiv:`1810.04742`, likewise uses Jordan totients in the normalized derivatives of `\Phi_n` at `1`. Toshiki Matsusaka and Genki Shibukawa, *Curious congruences for cyclotomic polynomials II*, Research in Number Theory **10** (2024), Article 3, DOI `10.1007/s40993-023-00489-z`, explicitly frames the higher derivative values through Lehmer's Euler/Jordan-totient formulas.

The value formula `\Phi_n(1)=p` for prime powers and `1` otherwise is classical; Bartłomiej Bzdęga, Andrés Herrera-Poyatos, and Pieter Moree, *Cyclotomic polynomials at roots of unity*, Acta Arithmetica **184** (2018), 215--230, DOI `10.4064/aa170112-20-12`, records the broader root-of-unity value theory.

The Mathia-specific contribution is the **branch-local synthesis and falsification**: the most direct source-forced non-torsion real-radial deformation outside the `WP-160` torsion-coset closure does hit `\Lambda(n)` exactly, but only as its zero-order boundary potential. Its independently positive local Hessian is `J_2(n)/12`, and its entire centered differential jet is Jordan-totient rather than Mangoldt. This is a precise obstruction to promoting the radial cyclotomic germ itself into the missing Weil-positive geometry.

## 10. Research consequence

The accepted noncharacter finite--archimedean clue can now be narrowed again.

A source-forced varying real parameter **does** exist in the embedded-root geometry, and it is arithmetically nontrivial:

\[
\boxed{
\text{primitive shell}
+
\text{real radial point}
\longrightarrow
\mathcal R_n(0)=\Lambda(n).
}
\tag{46}
\]

But its sign-bearing local geometry separates from that arithmetic value:

\[
\boxed{
\Lambda(n)
\ \text{at zero order}
\quad\not\Rightarrow\quad
\frac{J_2(n)}{12}
\ \text{at positive curvature}.
}
\tag{47}
\]

Therefore the next finite--archimedean candidate should not merely add a real scale variable to a cyclotomic log product and differentiate locally. It must make the **same global operation** both retain the prime-power cancellation and produce an independently positive quadratic form, with the Gamma/polar terms included under the same normalization. A genuinely nonlocal radial boundary response remains open; the direct local radial Hessian/finite-jet route is closed.
