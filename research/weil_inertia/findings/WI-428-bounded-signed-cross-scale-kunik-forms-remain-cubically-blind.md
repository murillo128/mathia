# WI-428 — Bounded signed cross-scale Kunik forms remain cubically blind on a fixed safe strip

**Status:** `CLASSICAL-IDENTITY + EXACT-DERIVED + STRUCTURAL-CONSTRAINT + DECISIVE-NEGATIVE + FRONTIER-ADVANCE + NO-RH`.

**Parents:** [WI-412](./WI-412-haar-scale-blaschke-mixing-buys-a-count-quantum-only-at-infinite-budget.md), [WI-424](./WI-424-kunik-boundary-flux-is-a-poisson-defect-counter.md), [WI-425](./WI-425-fixed-safe-lines-are-cubically-blind-to-shallow-boundary-flux.md), [WI-426](./WI-426-kunik-multiscale-l2-has-blind-or-singular-dichotomy.md), [WI-427](./WI-427-positive-kunik-multiscale-lp-portfolios-are-cesaro-blind-below-the-pole-threshold.md).

## Claim

WI-426 closes positive diagonal multiscale `L^2` energy on a fixed safe strip, while WI-427 explicitly leaves signed or non-diagonal cross-scale forms and cancellation before taking a norm as possible escapes. For the one-defect Kunik logarithmic-derivative response, those escapes still cannot recover the boundary tariff if the cross-scale operation has a finite, depth-independent budget.

For one right-half zero

\[
\rho=\frac12+d+i\gamma,
\qquad 0<d<a_0,
\]

write, on the vertical line displaced by `a>d`,

\[
g_{a;d,\gamma}(t)
:=
\frac1{a-d+i(t-\gamma)}
-
\frac1{a+d+i(t-\gamma)}.
\tag{1}
\]

For any two safe scales `a,b>d`, translation in `gamma` drops out of the `L^2(dt)` inner product and one has the exact cross-scale kernel

\[
\boxed{
K_d(a,b)
:=
\langle g_{a;d,\gamma},g_{b;d,\gamma}\rangle_{L^2(dt)}
=
\frac{16\pi d^2}
{(a+b)\bigl((a+b)^2-4d^2\bigr)}.
}
\tag{2}
\]

In particular, at `a=b`,

\[
K_d(a,a)
=
\frac{2\pi d^2}{a(a^2-d^2)},
\tag{3}
\]

which is exactly the safe-line energy from WI-426. By contrast, the boundary energy from WI-424 is

\[
\boxed{
\|g_{0;d,\gamma}\|_2^2=\frac{2\pi}{d}.
}
\tag{4}
\]

Now let `nu` be a signed or complex Borel charge on `[a_0,\infty)^2` whose variation measure has finite weighted budget

\[
B_\nu
:=
\iint_{[a_0,\infty)^2}
(a+b)^{-3}\,d|\nu|(a,b)
<\infty,
\tag{5}
\]

and form the fully non-diagonal signed cross-scale functional

\[
Q_\nu(d)
:=
\iint K_d(a,b)\,d\nu(a,b).
\tag{6}
\]

Then for every `0<d<a_0`,

\[
\boxed{
|Q_\nu(d)|
\le
\frac{16\pi d^2}{1-d^2/a_0^2}\,B_\nu.
}
\tag{7}
\]

Hence

\[
\boxed{
\frac{|Q_\nu(d)|}{2\pi/d}
\le
\frac{8B_\nu d^3}{1-d^2/a_0^2}
\longrightarrow0.
}
\tag{8}
\]

Allowing signs and cross-scale terms therefore does **not** remove the cubic loss of WI-425 as long as the cross-scale budget stays finite on a fixed safe strip. In fact the obstruction is stronger than an `O(d^2)` estimate: `Q_\nu` is analytic in `d^2` near `d=0` and has a zero of order at least `d^2`, whereas the canonical boundary energy has a `d^{-1}` pole. Signed cancellation can erase low-order safe-strip terms and make the response smaller; it cannot manufacture the missing boundary pole at finite budget.

The same conclusion holds abstractly for bounded cancellation before taking a norm. Let `mu` be a positive Borel measure on `[a_0,\infty)` with

\[
0<M_3(\mu)
:=
\int_{[a_0,\infty)}a^{-3}\,d\mu(a)
<\infty,
\tag{9}
\]

and define the safe-scale Hilbert bundle

\[
\mathcal H
:=
L^2\!\left([a_0,\infty)\times\mathbb R,
 d\mu(a)\,dt\right),
\qquad
G_{d,\gamma}(a,t):=g_{a;d,\gamma}(t).
\tag{10}
\]

WI-426's diagonal identity gives

\[
\boxed{
\|G_{d,\gamma}\|_{\mathcal H}^2
\le
\frac{2\pi M_3(\mu)}{1-d^2/a_0^2}\,d^2.
}
\tag{11}
\]

Therefore every fixed bounded operator `A` on `\mathcal H` satisfies

\[
\boxed{
\left|
\langle G_{d,\gamma},A G_{d,\gamma}\rangle_{\mathcal H}
\right|
\le
\frac{2\pi\|A\|M_3(\mu)}{1-d^2/a_0^2}\,d^2,
}
\tag{12}
\]

and every fixed bounded linear preprocessing map `T:\mathcal H\to\mathcal K` into any Hilbert space `\mathcal K` satisfies

\[
\boxed{
\|T G_{d,\gamma}\|_{\mathcal K}^2
\le
\frac{2\pi\|T\|^2M_3(\mu)}{1-d^2/a_0^2}\,d^2.
}
\tag{13}
\]

Thus non-diagonal bounded quadratic forms and bounded cancellation-before-norm are both cubically blind relative to (4). Any family that really dominates a fixed fraction `c>0` of the boundary energy must become singular. Quantitatively, if

\[
|\langle G_{d,\gamma},A_dG_{d,\gamma}\rangle|
\ge c\frac{2\pi}{d},
\tag{14}
\]

then necessarily

\[
\boxed{
\|A_d\|
\ge
\frac{c(1-d^2/a_0^2)}{M_3(\mu)}\,d^{-3}.
}
\tag{15}
\]

Likewise, if `\|T_dG_{d,\gamma}\|^2\ge c(2\pi/d)`, then

\[
\boxed{
\|T_d\|
\ge
\sqrt{\frac{c(1-d^2/a_0^2)}{M_3(\mu)}}\,d^{-3/2}.
}
\tag{16}
\]

This converts the remaining escape route into a sharp conditioning requirement: a fixed safe-strip construction can only see the reciprocal-depth boundary charge if its operator budget blows up at least cubically at the quadratic-form level (or as `d^{-3/2}` before squaring a norm), or if some assumption above is genuinely abandoned.

## 1. Exact cross-scale kernel

Because translation by `gamma` is unitary on `L^2(dt)`, set `gamma=0`. For `a>d`, the elementary Laplace representation

\[
\frac1{c+it}
=
\int_0^\infty e^{-cx}e^{-itx}\,dx,
\qquad c>0,
\tag{17}
\]

gives

\[
g_{a;d}(t)
=
2\int_0^\infty
 e^{-ax}\sinh(dx)e^{-itx}\,dx.
\tag{18}
\]

Plancherel therefore yields

\[
K_d(a,b)
=
8\pi
\int_0^\infty
 e^{-(a+b)x}\sinh^2(dx)\,dx.
\tag{19}
\]

Writing `s=a+b>2d` and using `sinh^2 u=(cosh 2u-1)/2`,

\[
\int_0^\infty e^{-sx}\sinh^2(dx)\,dx
=
\frac{2d^2}{s(s^2-4d^2)},
\tag{20}
\]

which proves (2). This derivation avoids any Fourier-support sign convention; only the standard Plancherel normalization is used.

For `a,b\ge a_0`, one has `s\ge2a_0` and hence

\[
s^2-4d^2
\ge
s^2\left(1-\frac{d^2}{a_0^2}\right).
\tag{21}
\]

Substitution into (2), followed by total variation, gives (7).

There is also an exact convergent expansion on every closed shallow-depth interval `|d|\le\delta<a_0`:

\[
\boxed{
K_d(a,b)
=
16\pi
\sum_{n=0}^\infty
\frac{4^n d^{2n+2}}{(a+b)^{2n+3}}.
}
\tag{22}
\]

The bound (5) dominates this series uniformly because `a+b\ge2a_0`. Hence termwise integration is justified and

\[
Q_\nu(d)
=
16\pi
\sum_{n=0}^\infty
4^n d^{2n+2}
\iint(a+b)^{-2n-3}\,d\nu(a,b).
\tag{23}
\]

In particular,

\[
Q_\nu(d)
=
16\pi d^2
\iint(a+b)^{-3}\,d\nu(a,b)
+O(d^4).
\tag{24}
\]

If signs cancel the coefficient in (24), the first surviving term is of still higher even order. This is the precise sense in which finite-budget cross-scale cancellation cannot repair the missing `d^{-1}` singularity.

## 2. Bounded-operator formulation and finite symmetry blocks

Equation (11) is immediate from WI-426:

\[
\|G_{d,\gamma}\|_{\mathcal H}^2
=
\int
\frac{2\pi d^2}{a(a^2-d^2)}\,d\mu(a)
\le
\frac{2\pi M_3(\mu)}{1-d^2/a_0^2}\,d^2.
\tag{25}
\]

Then (12) is the operator-norm inequality

\[
|\langle G,AG\rangle|
\le\|A\|\,\|G\|^2,
\tag{26}
\]

and (13) follows from `\|TG\|\le\|T\|\|G\|`. Comparing with the exact boundary energy (4) proves (15)--(16).

This argument does not require `A` to be diagonal in scale, positive, translation invariant, local in the ordinate, self-adjoint, or generated by an integral kernel. It therefore covers a much larger class than the positive portfolios of WI-426. It also covers any fixed finite functional-equation/conjugation package: a sum of `O(1)` translated one-defect vectors has `\mathcal H` norm `O(d)` by the triangle inequality, so every uniformly bounded quadratic form on that finite block remains `O(d^2)`. Finite symmetry packaging changes constants, not the cubic exponent against (4).

The conclusion is still deliberately an interface theorem, not a theorem about every possible many-zero statistic. A detector may exploit collective interactions among an unbounded number of zeros, source-side arithmetic correlations, or a depth-dependent singular transform. Those are additional structures not present in the one-defect finite-budget model.

## 3. Prior art and novelty audit

No priority claim is made for the analytic ingredients.

- Matthias Kunik's *Logarithmic Fourier integrals for the Riemann Zeta Function* supplies the half-plane Poisson--Schwarz/Blaschke factorization and the zeta-specific right-half-zero factor used throughout WI-423--WI-427.
- The Laplace representation (17), Plancherel, Cauchy--Schwarz/operator-norm bounds, and the Hardy-space interpretation of half-plane Cauchy kernels are classical analysis. The exact kernel (2) is an elementary consequence of those identities.
- WI-425 proves cubic blindness for one or finitely many fixed safe lines. WI-426 extends that obstruction to arbitrary positive diagonal `L^2` scale portfolios of finite third-inverse-moment cost. WI-427 closes the positive diagonal `L^p`, `1<=p<2`, repair but explicitly leaves signed/non-diagonal cross-scale forms and cancellation-before-norm open.
- WI-412 is the nearest repository-local analogue: for a related Blaschke potential, even signed/complex Haar-scale mixing obtains a count quantum only at infinite budget. Its observable and scale transform are different from the Kunik logarithmic-derivative safe-line bundle considered here.

A targeted literature audit around Kunik's factorization, Blaschke logarithmic derivatives, half-plane Hardy/Cauchy kernels, bounded operators on Hardy spaces, and cross-scale quadratic forms located the standard analytic framework but did not locate a zeta-specific theorem packaging the fixed-safe-strip finite-budget no-go (7)--(16). Absence from that search is not used as evidence of priority.

The mathematical delta recorded here is therefore not a new transform theorem. It is the exact Kunik cross-scale Gram kernel (2), its finite-budget analytic expansion (22)--(24), and the resulting quantitative statement that the explicit signed/non-diagonal and cancellation loopholes left by WI-426--WI-427 still require a singular operator budget to reproduce the canonical boundary defect scale.

## 4. Stress tests, boundaries and falsification

1. **The safe strip is fixed.** The support condition `a,b>=a_0>0` is essential. Letting sampled scales approach the critical boundary with `d`, or cross the unknown defect depth, leaves the theorem and returns to the singular/oracle issues identified in WI-426--WI-427.

2. **The budget is depth-independent.** Equations (15)--(16) quantify exactly what must fail if one uses a family of operators depending on `d`: its norm has to diverge at the stated rate, unless additional information changes the input norm itself. A depth selector independently produced by arithmetic data is not excluded.

3. **Signed and non-diagonal does not mean arbitrary distributional.** Equation (7) assumes the weighted total variation (5) is finite; (12) assumes a bounded operator. Singular kernels, unbounded operators, renormalized distributions, and infinite-budget limits are outside the claim. The point is that signs alone do not evade the conditioning barrier.

4. **Cancellation before the norm is covered only when bounded.** Any fixed bounded linear preprocessing `T` is covered by (13). A cancellation transform whose norm grows like `d^{-3/2}` or worse is precisely one of the singular escape routes, not a counterexample.

5. **The theorem is one-defect coercivity.** It rules out a uniform finite-budget bridge that must already detect one shallow off-line factor at the correct reciprocal-depth scale. It does not rule out genuinely many-zero effects, determinant/inertia constraints, or arithmetic couplings that have no one-factor lower-bound formulation.

6. **No RH assumption and no zero construction.** The variable `d` parametrizes the response of a hypothetical Kunik factor. The result is an exact conditioning/no-go statement about the proof interface. It neither assumes nor disproves the existence of off-critical zeta zeros.

The finite-measure statement is falsified by a signed or complex `nu` satisfying (5) for which `Q_nu(d)` is not `O(d^2)` as `d->0`; equations (2), (21), and total variation exclude this. The operator statement is falsified by a uniformly bounded `A_d` or `T_d` on a fixed safe bundle whose one-defect response dominates a fixed fraction of `2pi/d`; (11)--(16) exclude this.

## Consequence for the research line

The current Kunik frontier narrows again. Merely replacing positive scale weights by signs, adding bounded non-diagonal scale couplings, or performing bounded cancellation before an `L^2` norm cannot amplify a shallow safe-line signal into the canonical boundary flux. The missing factor is exactly a cubic condition number.

A viable continuation must therefore introduce genuinely singular information: an operator budget growing at least at the rates in (15)--(16), scales moving toward the unknown boundary defect, a justified pole renormalization, an unbounded/many-zero interaction with an independently controlled cost, or zeta-specific arithmetic structure that supplies the missing depth information. Those alternatives remain open; the bounded fixed-safe-strip cross-scale route does not.
