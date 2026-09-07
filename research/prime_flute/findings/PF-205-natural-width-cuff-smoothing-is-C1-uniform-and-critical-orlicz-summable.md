# PF-205 — natural-width cuff smoothing has uniform `C^1` geometry and summable critical Orlicz mass

**Status:** `EXACT-DERIVED + POSITIVE/BOUNDARY`. PF-202 proves that distinguished decomposition-cuff smoothing can be made arbitrarily small in the critical `L\log L` coefficient currency, but deliberately leaves a circular-looking operator concern: forcing the support arbitrarily thin may make higher derivatives and local pseudodifferential constants arbitrarily bad. That loss is **not intrinsic at the first metric-derivative level used by PF-200**. The exact PF-179 finite-cuff transport has a closed arclength formula whose first three derivatives differ from the identity by `O(d_n)`, where `d_n` is the prime/shift half-cuff length defect. PF-032 and PF-107 then provide a canonical smoothing width of order `d_n` that fits inside the standard collar on both source and clone cuffs. With that width, the PF-182 exact-area generating-function cutoff has `DF-I=O(d_n)` and **uniformly bounded `D^2F`**, so the pulled metric is uniformly elliptic with a uniform `C^1` bound across the smoothed cuff family. At the same time the seam coefficient has total critical Orlicz cost `O((\log p_n)^2/p_n^2)`, hence is absolutely summable. Thus PF-202's arbitrary-support derivative circularity can be avoided by one explicit arithmetic/geometric scale choice. This does not yet prove a weak-`S_1` seam operator estimate: the remaining smooth-route question is scale/aspect-ratio uniform critical localization on the `O(d_n)`-thin collar family. PF-203/PF-204's unsmoothed native-resolvent route remains available and does not require this smoothing at all. The PF-138 true-short-collar splice is independent and remains open.

## Claim

Let `C_n\subset X` and `C_n^+\subset X_+` be the matched distinguished decomposition cuffs of the exact prime flute and the all-composite shift clone. Write

\[
L_n=2a_n,
\qquad
L_n^+=2a_n^+,
\qquad
d_n:=a_n^+-a_n>0
\tag{1}
\]

on the tail. Let

\[
P_n:=p_{n-1},
\qquad
g_n:=p_n-p_{n-1},
\qquad
h_n=\log\frac{u_n}{u_{n-1}},
\tag{2}
\]

with the indexing convention of PF-107. Then

\[
d_n=\frac1{P_n}+o(P_n^{-1}),
\qquad
h_n=\frac{g_n}{P_n}(1+o(1)).
\tag{3}
\]

There is a constant `\kappa>0`, independent of `n`, and an exact-area PF-182 smoothing of the decomposition seams supported in the signed Fermi-area collars

\[
U_n=\{|x|<w_n\},
\qquad
w_n:=\kappa d_n,
\tag{4}
\]

such that, after a finite head:

1. `U_n` and the corresponding target support lie inside the standard embedded collars of `C_n,C_n^+`;
2. the smoothed global comparison is exactly area preserving and agrees with the original PF-179--PF-181 pantwise map outside `U_n`;
3. in the universal signed Fermi coordinates
   \[
   g=\frac{dx^2}{1+x^2}+(1+x^2)ds^2,
   \qquad d\mu=dx\,ds,
   \tag{5}
   \]
   its seam restriction satisfies
   \[
   \boxed{
   \|DF_n-I\|_{L^\infty(U_n)}\le C d_n,
   \qquad
   \|D^2F_n\|_{L^\infty(U_n)}\le C;
   }
   \tag{6}
   \]
4. consequently the pulled target metric `h_n^{\rm pull}=F_n^*g_+` and its inverse form a uniformly elliptic family with a uniform local `C^1` bound on the seam supports;
5. if `C_n^{\rm seam}` is the PF-175 cotangent coefficient on `U_n`, then for `\Phi(t)=t\log(e+t)`,
   \[
   \boxed{
   \|C_n^{\rm seam}\|_{L_\Phi(X)}
   +\|(C_n^{\rm seam})^+\|_{L_\Phi(X_+)}
   \le
   C\,a_n d_n^2\log\!\left(e+\frac1{a_n d_n}\right).
   }
   \tag{7}
   \]
   In particular,
   \[
   \boxed{
   \sum_n
   \left(
   \|C_n^{\rm seam}\|_{L_\Phi}
   +\|(C_n^{\rm seam})^+\|_{L_\Phi}
   \right)<\infty.
   }
   \tag{8}
   \]

The point of (6)--(8) is simultaneous control: the support is thin enough to be critically summable but **not** chosen by an arbitrary `q_n\downarrow0` that can drive the metric derivatives through an uncontrolled scale. No uniform Ponge constant on the shrinking physical collars is asserted.

## 1. The exact PF-179 finite-cuff trace has tame higher derivatives

PF-179 writes the finite Lambert branch in the Fermi area coordinates `(\tau,y)` as

\[
\tau'=\psi_\beta(\tau)
=\operatorname{arsinh}(\lambda\sinh\tau),
\qquad
 y'=\frac{y}{\psi_\beta'(\tau)},
\qquad
\lambda=\frac{\sinh a'}{\sinh a},
\tag{9}
\]

for `a'=a+d`. Its finite upper boundary has

\[
Y_a(\tau)
=\frac{\cosh\tau}
{\sqrt{\sinh^2a-\sinh^2\tau}}.
\tag{10}
\]

Let `u` be intrinsic arclength along that finite boundary, measured from `\tau=0`. A direct differentiation of (10) gives

\[
1+Y_a^2
=\frac{\cosh^2a}{\sinh^2a-\sinh^2\tau},
\tag{11}
\]

and

\[
Y_a'
=\frac{\cosh^2a\sinh\tau}
{(\sinh^2a-\sinh^2\tau)^{3/2}}.
\tag{12}
\]

Therefore the induced arclength element is

\[
\boxed{
\frac{du}{d\tau}
=\frac{\sinh a\cosh a}
{\sinh^2a-\sinh^2\tau}.
}
\tag{13}
\]

Integrating (13) from zero yields the exact identity

\[
\boxed{
\tanh u=\coth a\,\tanh\tau.
}
\tag{14}
\]

At the Lambert corner `\tau=T_a`, equation (14) gives `u=a`, as required.

Apply the same identity on the target boundary after (9). Eliminating `\tau` gives a closed formula for the induced arclength trace:

\[
\boxed{
B_{a,a'}^{\rm bulk}(u)
=\operatorname{arsinh}\!\left(
\frac{\cosh a'}{\cosh a}\sinh u
\right).
}
\tag{15}
\]

Put

\[
\kappa_a:=\frac{\cosh a'}{\cosh a}.
\]

Then

\[
(B^{\rm bulk})'(u)
=\frac{\kappa_a\cosh u}
{\sqrt{1+\kappa_a^2\sinh^2u}},
\tag{16}
\]

\[
\boxed{
((B^{\rm bulk})')^2-1
=\frac{\kappa_a^2-1}
{1+\kappa_a^2\sinh^2u},
}
\tag{17}
\]

and

\[
\boxed{
\frac d{du}\log(B^{\rm bulk})'
=\frac{(1-\kappa_a^2)\tanh u}
{1+\kappa_a^2\sinh^2u}.
}
\tag{18}
\]

Since

\[
\log\kappa_a
=\int_a^{a+d}\tanh t\,dt,
\tag{19}
\]

we have `|\kappa_a-1|\le Cd` for the tail family. The rational hyperbolic factors in (17)--(18), together with one derivative of (18), are uniformly bounded for `u\ge0`. Hence

\[
\boxed{
\|(B^{\rm bulk})'-1\|_\infty
+\|(B^{\rm bulk})''\|_\infty
+\|(B^{\rm bulk})'''\|_\infty
\le C d.
}
\tag{20}
\]

This is stronger information than the `1+O(d)` bilipschitz trace estimate used in PF-182.

PF-179 uses a fixed recentered corner patch to join the finite transport to the outer exact isometry. The source/target corner data differ by `O(d)` on that one fixed smooth reference domain. Choose once a smooth reflection-compatible boundary interpolation and the fixed-domain relative Moser correction with bounded linear extension/divergence operators. Standard smooth dependence of that fixed-domain construction gives the same bound (20) for the full half-cuff trace after changing the constant. If a seam-foot endpoint smoothing is needed before reflection, perform it on one fixed tangential arclength scale; the input jet mismatch is `O(d)`, so its first three trace derivatives remain `O(d)`. Thus the reflected full-cuff map `B_n` may be chosen with

\[
\boxed{
\|B_n'-1\|_\infty
+\|B_n''\|_\infty
+\|B_n'''\|_\infty
\le C d_n.
}
\tag{21}
\]

Only this finite derivative statement is used below. No uniform `C^\infty` claim is needed.

## 2. The standard collar supplies a canonical width of order `d_n`

PF-032 proves the exact identity for the distinguished cuff

\[
w(\ell_n)=\frac{h_n}{2},
\tag{22}
\]

where `w(\ell)` is the standard collar half-width in normal distance. In the signed Fermi area coordinate `x=\sinh r`, the guaranteed source half-width is therefore

\[
\xi_n:=\sinh(h_n/2).
\tag{23}
\]

The clone satisfies the identical geometric relation with `h_n^+`.

PF-107 gives (3) and also `h_n^+/h_n\to1`. Since every odd-prime gap satisfies `g_n\ge2`,

\[
\frac{\xi_n}{d_n}
=\frac{g_n}{2}(1+o(1))
\ge1+o(1),
\tag{24}
\]

and the same lower bound holds for the target half-width. Consequently one may fix, for example, any sufficiently small absolute `\kappa<1/4` and set

\[
\boxed{w_n=\kappa d_n.}
\tag{25}
\]

Then `|x|<2w_n` lies inside both standard collars for every sufficiently large `n`; a finite head is irrelevant to the summability statements.

This choice is the key difference from PF-202. The support width is neither an arbitrary vanishing sequence nor the full collar width. It is tied to the **actual size of the boundary mismatch**.

## 3. At width `w_n\asymp d_n`, the exact-area cutoff has uniform second derivatives

PF-182 uses the common area-preserving cuff germ

\[
E_n(x,s)
=\left(\frac{x}{b_n(s)},B_n(s)\right),
\qquad b_n=B_n',
\tag{26}
\]

in the universal metric/area chart (5). Equations (21) and `|x|\le2w_n=O(d_n)` give

\[
\boxed{
DE_n-I=O(d_n),
\qquad
D^2E_n=O(d_n)
}
\tag{27}
\]

with uniform constants.

The one-sided PF-179 exact-area pant germ has the same finite-derivative control near the genuine cuff. On the explicit finite branch this follows by differentiating (9); all derivatives through second order of the map difference are `O(d_n)`. The only non-explicit part is the fixed recentered corner correction, where the same fixed-domain smooth choice used in Section 1 gives `C^2` difference `O(d_n)`. PF-180 is the identity near the genuine finite cuff and PF-181 acts only in the cusp. Thus, after choosing the constructions consistently,

\[
F_{n,\pm}-E_n=O(d_n)
\quad\text{in }C^2
\tag{28}
\]

on the one-sided collar germ.

Set

\[
H_{n,\pm}=E_n^{-1}\circ F_{n,\pm}.
\tag{29}
\]

It preserves `dx\wedge ds`, fixes `x=0` pointwise, and satisfies

\[
DH_{n,\pm}-I=O(d_n),
\qquad
D^2H_{n,\pm}=O(d_n).
\tag{30}
\]

In the fixed Weinstein graph chart used by PF-182, write the relative exact symplectic graph as `dS_n`. Boundary fixing and (30) give the quantitative relative vanishing

\[
|S_n|\le C d_n x^2,
\qquad
|dS_n|\le C d_n|x|,
\qquad
|D^2S_n|\le C d_n,
\qquad
|D^3S_n|\le C d_n.
\tag{31}
\]

Let `\chi` be one fixed cutoff and put

\[
S_{n,\rm cut}(x,s)
=\chi(x/w_n)S_n(x,s).
\tag{32}
\]

PF-182 already observes that the first three terms in (31) cancel the dangerous inverse-width factors at the `D^2S` level. One more differentiation gives, on `|x|\lesssim w_n`,

\[
|D^3S_{n,\rm cut}|
\le C\left(
\frac{|S_n|}{w_n^3}
+\frac{|dS_n|}{w_n^2}
+\frac{|D^2S_n|}{w_n}
+|D^3S_n|
\right).
\tag{33}
\]

Using `|x|\le Cw_n` and `w_n=\kappa d_n`,

\[
\boxed{
\|D^2S_{n,\rm cut}\|_\infty\le C d_n,
\qquad
\|D^3S_{n,\rm cut}\|_\infty\le C.
}
\tag{34}
\]

The graph-to-diffeomorphism map is fixed and smooth on the `D^2S=O(d_n)` neighborhood. Hence the resulting exact-area cutoff has (6). In particular, differentiating `F_n^*g_+` once uses at most `D^2F_n`; equation (6) therefore gives a uniform `C^1` bound for the pulled metric and inverse. This is exactly the coefficient regularity level used in PF-200's fixed-window interior `H^2` argument.

The conclusion is intentionally finite-order. Derivatives of order three and above of the **map** may still grow like powers of `d_n^{-1}` after further differentiation of (32). PF-205 neither needs nor controls them.

## 4. The natural-width seam is already critically summable

Because `d\mu=dx\,ds` in (5), the source area of the two-sided seam support satisfies

\[
\mu(U_n)
\le C w_n L_n
\le C a_n d_n.
\tag{35}
\]

Exact area preservation gives the same scale on the target. Equation (6) and the smooth dependence of PF-175's cotangent matrix coefficient on the relative metric tensor imply

\[
\|C_n^{\rm seam}\|_\infty
+\|(C_n^{\rm seam})^+\|_\infty
\le C d_n.
\tag{36}
\]

Therefore

\[
\|C_n^{\rm seam}\|_1
+\|(C_n^{\rm seam})^+\|_1
\le C a_n d_n^2.
\tag{37}
\]

Apply PF-196's elementary Luxemburg estimate

\[
\|u\|_{L_\Phi}
\le
\|u\|_1
\log\!\left(e+\frac{\|u\|_\infty}{\|u\|_1}\right)
\tag{38}
\]

to the pointwise matrix norm. Equations (36)--(38) give (7), up to harmless changes of absolute constants when `a_nd_n` is not yet below one in the finite head.

It remains only to check the arithmetic scale. PF-107 gives

\[
d_n\asymp P_n^{-1}
\tag{39}
\]

on the tail. Since `g_n\ge2` and `h_n\sim g_n/P_n`, the exact cuff transform `a_n=\log\coth(h_n/4)` gives

\[
a_n=O(\log P_n).
\tag{40}
\]

Consequently

\[
a_nd_n^2
\log\!\left(e+\frac1{a_nd_n}\right)
=O\!\left(\frac{(\log P_n)^2}{P_n^2}\right).
\tag{41}
\]

The right-hand side is summable even over all integers, hence certainly over the prime-indexed tail. This proves (8).

Thus the critical coefficient does **not** force the support to be thinner than the derivative-safe width `w_n\asymp d_n`.

## 5. What PF-205 removes, and what it does not

PF-202 left two competing intuitions:

- support can always be thinned enough to pay any critical coefficient logarithm;
- but the same thinning might make the local operator constants grow too quickly to use that coefficient budget.

PF-205 removes the need for that arbitrary competition. The explicit prime/shift scales already admit a deterministic intermediate choice

\[
\boxed{
\text{support width }\asymp d_n
\quad+\quad
\text{uniform pulled-metric }C^1
\quad+\quad
\ell^1(L\log L)\text{ coefficient budget}.}
\tag{42}
\]

So a future smooth-route proof may assume this normalized seam family rather than an adversarially thin PF-202 family.

What remains is genuinely operator-theoretic. The collars in (25) still have normal width `O(d_n)` while their circumference is `O(a_n)`. PF-200's existing proof uses fixed-size recentered windows with fixed buffers; it cannot simply be copied to this shrinking/aspect-ratio family. One must prove a scale-uniform critical estimate, exploit critical two-dimensional rescaling, or use another exact factorization whose constant grows slowly enough to preserve (8). PF-205 does not assert such a theorem.

Nor does PF-205 make smoothing mandatory. PF-203 shows that the piecewise area-preserving comparison has an exact global quadratic form without a seam surface term, and PF-204 gives a native two-Hilbert-space resolvent factorization with both resolvents smooth. Those findings keep the **unsmoothed piecewise-transport route** as the preferred way to avoid seam regularization entirely. PF-205 says only that the smooth alternative no longer has an uncontrolled `C^1`-regularity/support tradeoff.

Finally, none of this touches the PF-138 true Margulis-short collars. Their PF-183 endpoint splice is a bulk body/core interpolation problem, not a decomposition-seam smoothing problem.

## Prior art and novelty assessment

No novelty is claimed for the hyperbolic collar lemma, the standard width

\[
w(\ell)=\operatorname{arsinh}(1/\sinh(\ell/2)),
\]

or Fermi coordinates. PF-032 already audits their exact prime-flute specialization. No novelty is claimed for Weinstein's Lagrangian-neighborhood/generating-function framework or conservative local pasting; those inputs and the support-controlled Moser literature are already audited in PF-182. The relevant classical references remain Alan Weinstein, *Symplectic manifolds and their Lagrangian submanifolds*, Advances in Mathematics 6 (1971), 329--346, DOI `10.1016/0001-8708(71)90020-X`, and Pedro Teixeira's support-controlled Dacorogna--Moser work, DCDS 37 (2017), 4071--4089, arXiv:1608.06213, with the pullback addendum arXiv:1705.01416.

Likewise, the critical matrix-valued `L\log L` weak-trace theorem is Ponge's prior art already audited in PF-197/PF-200: Raphaël Ponge, *Weyl's Laws and Connes' Integration Formulas for Matrix-Valued `L log L`-Orlicz Potentials*, Mathematical Physics, Analysis and Geometry 25 (2022), article 10, DOI `10.1007/s11040-022-09422-9`, arXiv:2107.13605. PF-205 does not strengthen that theorem.

A fresh structure-directed audit around hyperbolic collar smoothing, support-controlled conservative pasting, and critical `L\log L` Cwikel localization found no theorem that supplies the project-specific combination (42), and absence of an exact match is not treated as a novelty theorem. The durable custom deduction is the combination of four already grounded ingredients: the explicit PF-179 boundary transport, the exact PF-032 collar width, the PF-107 prime/shift scale `d_n\asymp P_n^{-1}`, and PF-196's critical concentration logarithm. Together they show that the **same natural seam width simultaneously satisfies the geometric derivative and critical coefficient budgets**.

## Falsification and boundary checks

A later adversary can audit PF-205 through the following finite chain:

1. differentiate PF-179's boundary graph (10) in its area metric and verify the arclength identity (13)--(14);
2. substitute PF-179's exact triangular map (9) and derive the arclength trace (15);
3. differentiate (15) through third order and verify the uniform `O(d)` bounds (20), including the fixed-corner/reflection smoothing choice rather than inferring them from bilipschitz control alone;
4. use PF-032 to convert the exact standard normal collar width to `\xi_n=\sinh(h_n/2)` and PF-107 plus `g_n\ge2` to verify that one fixed `w_n=\kappa d_n` fits source and target collars on the tail;
5. insert the trace derivative bounds into PF-182's common germ (26) and check (27)--(30);
6. in the fixed Weinstein chart, verify that `C^2` closeness of the relative germ gives the last estimate in (31), then differentiate the cutoff once beyond PF-182 to obtain (33)--(34);
7. check that uniform `D^2F_n` really implies uniform `C^1` pulled-metric coefficients in the universal Fermi chart, but does **not** imply uniform higher symbol seminorms;
8. compute the support area (35), pointwise coefficient scale (36), and critical Luxemburg bound (37)--(38);
9. use only the persisted arithmetic estimates `d_n\asymp P_n^{-1}` and `a_n=O(\log P_n)` to obtain the summable majorant (41);
10. refuse any upgrade to a seam weak-`S_1` operator theorem until scale/aspect-ratio localization constants are controlled, and keep the PF-183 true-short-collar endpoint separate.

PF-205 must be narrowed if the fixed PF-179 corner correction cannot be chosen with the finite `C^2` parameter control used in (28), if the standard collar has insufficient room for (25), or if one extra derivative of the relative generating-function chart does not give the `D^3S=O(d_n)` bound in (31). Failure of a future scale-uniform Cwikel estimate on the thin collars would **not** refute PF-205; it would realize exactly the remaining operator boundary stated here.

## Consequences for the research line

The smooth distinguished-cuff branch now has a cleaner normal form. PF-202's arbitrary-support construction proves maximal coefficient flexibility; PF-205 adds a deterministic support choice that also preserves the finite metric regularity used by the existing critical machinery. Therefore the smooth-route interface gate should no longer be phrased as an unspecified competition between `L\log L` concentration and derivative blow-up. It is now the concrete question whether the critical operator estimate can be made stable under the explicit thin-cylinder scale `w_n\asymp p_n^{-1}` with circumference `O(\log p_n)`.

The primary PF-204 unsmoothed route remains sharper: prove the critical estimate for the native-resolvent/piecewise cotangent-transport product. Either route would still have to be combined with the independent PF-183 true-short-collar endpoint splice before any complete weak-`S_1` classification is available.