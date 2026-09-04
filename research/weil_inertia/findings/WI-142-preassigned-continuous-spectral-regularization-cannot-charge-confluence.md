# WI-142 — preassigned continuous spectral regularization cannot charge Lamzouri confluence

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY`. WI-138 shows that Lamzouri's finite tensor has exactly one negative eigenvalue for every distinct off-line conjugate pair. WI-140 shows that a simple off-line pair can confluence to a critical-line double while the complete finite deficit tends to zero, and WI-141 shows that every **fixed finite** package of continuous spectral statistics is blind to that confluence. A natural escape left open in WI-141 was to let the regularization scale itself shrink with the zero height or matrix size, for example by using an increasingly sharp resolvent, smoothed sign, or log-determinant probe near zero.

That escape does not work at the level of Lamzouri's abstract finite inequality unless the shrinking scale is backed by an additional source-specific lower bound or interaction theorem. More precisely, **any preassigned finite family of continuous operator/spectral detectors, even when the detectors and all of their regularization scales vary arbitrarily with the configuration size, can be defeated by choosing the off-line horizontal depths still smaller**. One can do this while keeping a positive-density negative index and simultaneously making Lamzouri's normalized deficit tend to zero.

Equivalently, the quantifier obstruction is exact:

\[
\boxed{
\text{preassign continuous detector at size }N
\quad\Longrightarrow\quad
\text{choose }y_N>0\text{ below its continuity scale}
\quad\Longrightarrow\quad
\text{off-line pair }\sim\text{ real double for that detector}.}
\]

Thus a defect-to-zero bootstrap cannot be obtained merely by sharpening a **continuous** spectral approximation to inertia on a predetermined scale. To recover pair count uniformly one needs either the genuinely discontinuous inertia/sign projector, a source-specific spectral/horizontal gap that tells us how far the regularization scale may be pushed below zero, an adaptive observable whose validity is itself proved from zeta data, or another interaction invariant that prevents extensive confluence.

## 1. Exact one-pair confluence and the missing gap

Use the notation already reconstructed from Proposition 2.1 of Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1. For one simple non-real conjugate pair

\[
z=x+iy,\qquad \bar z=x-iy,\qquad y>0,
\]

WI-140 and WI-141 give the orthogonal even/odd vectors

\[
g_y(u)=\eta(u)e^{-2\pi iux}\cosh(2\pi uy),
\qquad
h_y(u)=-i\eta(u)e^{-2\pi iux}\sinh(2\pi uy),
\]

with

\[
t(y):=\|h_y\|^2
=4\pi^2\mu_2y^2+O(y^4),
\qquad
\mu_2=\int u^2\eta(u)^2\,du>0.
\tag{1}
\]

The tensor operator is

\[
\mathcal A_y=2(g_y\otimes g_y-h_y\otimes h_y)
\tag{2}
\]

and has exact nonzero spectrum

\[
\boxed{
\lambda_+(y)=2(1+t(y)),
\qquad
\lambda_-(y)=-2t(y).}
\tag{3}
\]

At the confluent real double, padded by the disappearing odd direction,

\[
\operatorname{spec}(\mathcal A_0)=\{2,0\}.
\tag{4}
\]

Moreover WI-141 proves, on Lamzouri's common ambient Hilbert space,

\[
\boxed{
\|\mathcal A_y-\mathcal A_0\|_{S_p}=O(y^2)
\qquad(1\le p\le\infty).}
\tag{5}
\]

The negative index therefore remains one for every `y>0`, while the entire operator approaches the real-double operator quadratically. The obstruction is not a failure of a particular moment formula; it is the absence of a uniform spectral gap separating the negative eigenvalue from zero.

## 2. A shrinking regularization scale is still defeatable

Consider first a concrete negative-eigenvalue detector at scale `epsilon>0`:

\[
r_\varepsilon(\lambda)
=
\begin{cases}
\dfrac{\lambda^2}{\lambda^2+\varepsilon^2},&\lambda<0,\\[2mm]
0,&\lambda\ge0.
\end{cases}
\tag{6}
\]

It is continuous, equals zero at the confluent eigenvalue, and approaches the exact indicator of `lambda<0` whenever `|lambda|/epsilon -> infinity`. For the exact pair spectrum (3),

\[
\boxed{
r_\varepsilon(\lambda_-(y))
=
\frac{4t(y)^2}{4t(y)^2+\varepsilon^2}.}
\tag{7}
\]

Hence a fixed regularization is blind when `t(y)<<epsilon`. More importantly, **the same remains true for an arbitrary preassigned sequence** `epsilon_N>0`, even if `epsilon_N` tends to zero faster than any conventional asymptotic scale. Since `t(y)->0` continuously as `y->0`, choose `y_N>0` so that

\[
t(y_N)\le\frac{\varepsilon_N}{N}.
\tag{8}
\]

Then

\[
\boxed{
r_{\varepsilon_N}(\lambda_-(y_N))
\le\frac{4}{N^2}.}
\tag{9}
\]

Thus `k_N asy N` genuine negative eigenvalues can contribute only `O(1/N)` in total to this regularized count, despite exact inertia `k_N`. In the quadratic regime (1), the condition is simply the scale mismatch

\[
y_N^2\ll\varepsilon_N.
\tag{10}
\]

Making `epsilon_N` smaller therefore does not solve the abstract problem: without a lower bound on the horizontal depth or on `|lambda_-|`, the configuration can always confluence faster.

Equation (7) is only an example. The argument below removes the choice of regularizer entirely.

## 3. Diagonal no-go for arbitrary preassigned continuous detector families

Fix any sequence of finite detector families

\[
\mathscr F_N=\{F_{N,1},\ldots,F_{N,J_N}\},
\qquad J_N<\infty,
\tag{11}
\]

where each `F_{N,j}` is a scalar functional continuous, at the relevant finite-rank operators, in trace norm. The detectors may depend arbitrarily on `N`; their Lipschitz constants, transition widths, polynomial degrees, resolvent scales, or other conditioning parameters may diverge arbitrarily quickly. There is no uniform modulus-of-continuity assumption.

Choose integers `a_N,b_N` with

\[
M_N:=a_N+2b_N\to\infty,
\qquad
\frac{b_N}{M_N}\longrightarrow\delta>0.
\tag{12}
\]

Start with a collapsed Lamzouri configuration consisting of `a_N` simple real points and `b_N` real double points at distinct centers. As in WI-140, the centers can be separated sufficiently far that the Riemann--Lebesgue decay of the kernel makes all cross-block terms arbitrarily small; in particular choose them so that the collapsed deficit satisfies

\[
\frac{\Delta_N(0)}{M_N}<\frac1N.
\tag{13}
\]

Now replace every real double at center `x_j` by the simple conjugate pair

\[
x_j\pm i y.
\]

For this **fixed finite** size `N`, the resulting operator `\mathcal A_N(y)` converges to the collapsed operator `\mathcal A_N(0)` in trace norm as `y->0`. This follows directly by summing the finite number of rank-one estimates behind (5); no spacing assumption is needed for this convergence. The complete Lamzouri deficit is likewise continuous in `y` because it is a finite polynomial expression in the kernel inner products.

Therefore, for each `N`, continuity of the finitely many detectors in (11) lets us choose one nonzero depth `y_N` so small that simultaneously

\[
\left|F_{N,j}(\mathcal A_N(y_N))
      -F_{N,j}(\mathcal A_N(0))\right|<1
\qquad(1\le j\le J_N)
\tag{14}
\]

and

\[
|\Delta_N(y_N)-\Delta_N(0)|<1.
\tag{15}
\]

After normalization by `M_N`, (13)--(15) give

\[
\boxed{
\frac{F_{N,j}(\mathcal A_N(y_N))
      -F_{N,j}(\mathcal A_N(0))}{M_N}
\longrightarrow0
}
\tag{16}
\]

for every detector actually present at stage `N`, and

\[
\boxed{\frac{\Delta_N(y_N)}{M_N}\longrightarrow0.}
\tag{17}
\]

Yet every `y_N` is strictly positive. WI-138's exact congruence inertia theorem therefore gives

\[
\boxed{
n_-(\mathcal A_N(y_N))=b_N,
\qquad
\frac{n_-(\mathcal A_N(y_N))}{M_N}\longrightarrow\delta>0.}
\tag{18}
\]

Equations (16)--(18) are the promised diagonal obstruction. A detector may sharpen with `N` as aggressively as desired; once it is fixed at that stage, the off-line depth can be chosen below its continuity scale. The argument works simultaneously for any finite number `J_N` of continuous detectors at each size, even when `J_N` itself grows without bound.

For ordinary spectral statistics, take

\[
F_{N,j}(A)=\operatorname{tr} f_{N,j}(A)
\]

with continuous scalar functions `f_{N,j}` and `f_{N,j}(0)=0`; finite-rank functional calculus makes these trace-norm continuous at each fixed stage. Thus (16) includes arbitrarily high but finite packages of smoothed spectral projectors, regularized inverse powers, bounded resolvent combinations, continuous determinant transforms, and `N`-dependent trace-moment combinations whenever they remain continuous at the zero crossing.

## 4. Exact inertia is precisely the discontinuous exception

For a nonsingular Hermitian matrix, the classical matrix sign function satisfies

\[
\operatorname{sign}(A)
=U\,\operatorname{diag}(\operatorname{sign}\lambda_i)\,U^*,
\]

and

\[
\frac{I-\operatorname{sign}(A)}2
\]

is the spectral projector onto the negative eigenspace. Thus the negative index itself is exactly a trace of a **discontinuous** spectral step. This is standard matrix-function theory; see Nicholas J. Higham, *Functions of Matrices: Theory and Computation*, SIAM (2008), Chapter 5, and the classical matrix-sign literature.

The discontinuity at zero is not incidental here. For the pair family (3),

\[
n_-(\mathcal A_y)=1\quad(y>0),
\qquad
n_-(\mathcal A_0)=0,
\tag{19}
\]

while (5) gives norm convergence. Any continuous replacement of the step must therefore lose uniform count sensitivity near the crossing. Classical invariant-subspace perturbation theory expresses the same conditioning fact from the other direction: stable spectral projectors require a separating spectral gap; the Davis--Kahan theorem makes the reciprocal gap the relevant sensitivity scale. No novelty is claimed for these matrix-analysis principles.

The new Mathia consequence is their exact coupling to the Lamzouri confluence family and the quantifier order in (11)--(18): **allowing the regularization scale to depend on `N` does not restore a universal pair charge unless some independent zeta input prevents the negative spectrum from following that scale into zero.**

## 5. Stress tests and boundaries

The finding is intentionally an abstract barrier, not a zeta counterexample. The many-block configurations use Lamzouri's finite proposition but are not asserted to satisfy the vertical density, arithmetic correlations, or other global constraints of the actual zeta zero set. A source-specific theorem can still rule them out.

The result also does not say that exact inertia is useless. On the contrary, WI-138 already proves that it counts distinct off-line pairs exactly. What fails is converting that discontinuous sign information into a **uniform positive quantitative charge** through a preassigned continuous approximation when no spectral gap is known.

An adaptive rule can escape only if its adaptation is supported by information not already contained in the abstract continuous data. For example, if an independent zeta theorem supplied a lower bound

\[
|\lambda_-|\ge g(T)>0
\]

on a positive-density subset of off-line pairs, one could choose a regularization scale `epsilon(T)<<g(T)` and recover their count. The present argument does not rule that out. It says that the gap theorem, not the subsequent regularization, would be the new information.

Likewise, a genuinely singular observable such as exact sign/inertia, a divided-difference normalization, or a detector whose scale is chosen from an independently certified smallest negative eigenvalue lies outside the continuity no-go. WI-132--WI-136 already show that one natural divided-difference/Schur normalization has its own screening problem, so singularity by itself is not sufficient.

Known near-line zero-density input does not remove this abstract obstruction. WI-029 provides an **upper tail** on large normalized horizontal depth and hence localizes any positive-density off-line population toward bounded depth; it does not by itself furnish the lower horizontal/spectral gap needed to choose a universal regularization scale below every confluent pair.

## 6. Prior-art and novelty audit

The external matrix-analysis ingredients are classical. The sign function and its spectral projectors are standard; a modern authoritative reference is Higham, *Functions of Matrices: Theory and Computation*, SIAM (2008), Chapter 5, DOI `10.1137/1.9780898717778.ch5`. The dependence of invariant-subspace stability on a separating spectral gap is classical Davis--Kahan perturbation theory: Chandler Davis and W. M. Kahan, **The Rotation of Eigenvectors by a Perturbation. III**, *SIAM Journal on Numerical Analysis* 7:1 (1970), 1--46, DOI `10.1137/0707001`. No novelty is claimed for continuity of functional calculus, matrix-sign projectors, Weyl/Davis--Kahan perturbation principles, or the elementary diagonalization argument that a continuous approximation cannot uniformly equal a step at its discontinuity.

The zeta-side source remains Lamzouri, arXiv:2609.02882v1, Proposition 2.1. A targeted search of the recent Lamzouri follow-up material and the standard matrix-sign/invariant-subspace literature did not locate a zeta-specific statement of the `N`-dependent diagonal obstruction above. This absence is **not** used as a priority claim. The durable content is the derived boundary: WI-141 left a shrinking resolvent/spectral scale as a logical escape, while (11)--(18) show that any scale fixed in advance of the actual off-line depths remains defeatable inside the same finite Lamzouri class.

## 7. Research consequence

The defect-to-zero program is now forced to separate two tasks that a regularization can otherwise obscure. The spectral **sign** problem is already solved exactly by WI-138: off-line pairs create negative directions. The missing problem is a source-specific **gap or anti-confluence** theorem.

Accordingly, ordinary escalation from moments to sharper continuous filters is not a new information carrier. A viable next step must prove one of the following kinds of input before a smoothed inertia count can help: a positive-density lower bound on horizontal depth or negative-eigenvalue magnitude; an interaction theorem preventing many shallow pairs from confluencing simultaneously at zeta density; a singular observable with an independently evaluated arithmetic identity; or a genuinely different horizontal statistic that survives the screening mechanisms already recorded in WI-005--WI-007 and WI-115--WI-125.

This does not improve the current unconditional simple-critical proportion. It decisively closes only the **preassigned continuous-regularization** repair of the Lamzouri negative-index cloud.