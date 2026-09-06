# WP-177 — Trace-class Fredholm Cayley determinants remain Schur; regularization is the real category change

**Status:** `LITERATURE+DERIVED + TRACE-CLASS-FREDHOLM-NO-GO + SCHUR-CLOSURE + REGULARIZED-DETERMINANT-BOUNDARY + DECISIVE-NARROWING + MATCHED-CONTROLS + PRIOR-ART-CLASSICALIZATION`.

`WP-176` closes normalized scalar coefficients and ordinary finite-dimensional determinants of Nevanlinna/Cayley passive responses, but deliberately leaves **Fredholm determinants, regularized determinants, and dimension-dependent counterterms** outside its conclusion. The first of those escapes is not genuine. If an operator-valued Schur response differs from the identity by a trace-class analytic family, then its ordinary Fredholm determinant is itself a scalar Schur function. It therefore inherits the weak-boundary Gamma obstruction of `WP-175` exactly as the finite-dimensional determinant does.

The distinction with a genuinely regularized determinant is sharp. Modified determinants such as `det_2` can already leave the scalar Schur unit ball for a one-dimensional constant unitary contraction. Thus the ordinary Fredholm passage adds no new freedom, while regularization really does change the scalar category. But that change also severs the automatic implication from operator passivity to scalar positivity: the counterterm becomes part of the proposed geometric mechanism and needs its own independently forced sign/coercivity theorem.

## 1. Ordinary Fredholm determinants of trace-class Schur defects stay in the Schur ball

Let `H` be a Hilbert space and let

\[
S:\mathbb C_+\to\mathcal B(H)
\tag{1}
\]

be holomorphic with

\[
\|S(z)\|\le 1,
\qquad z\in\mathbb C_+.
\tag{2}
\]

Assume that

\[
K(z):=S(z)-I\in\mathcal S_1(H)
\tag{3}
\]

and that `z -> K(z)` is holomorphic in trace norm. The ordinary Fredholm determinant

\[
D(z):=\det_F S(z)=\det_F(I+K(z))
\tag{4}
\]

is then holomorphic. For each fixed `z`, the standard trace-class determinant product gives

\[
D(z)=\prod_j \lambda_j(S(z)),
\tag{5}
\]

where the nontrivial eigenvalues are counted with algebraic multiplicity and accumulate, if at all, only at `1`. Equivalently, if `mu_j(K(z))` are the eigenvalues of the trace-class defect,

\[
D(z)=\prod_j(1+\mu_j(K(z))).
\tag{6}
\]

Because `S(z)` is a contraction, every spectral value satisfies

\[
|\lambda_j(S(z))|\le1.
\tag{7}
\]

The product in (5) therefore obeys

\[
\boxed{|D(z)|\le1.}
\tag{8}
\]

If `S(z)` is noninvertible, the determinant is zero and (8) is immediate. Otherwise (5)--(8) give the same conclusion by the convergent trace-class product. Hence

\[
\boxed{
S\text{ operator-valued Schur},\quad S-I\in\mathcal S_1\text{ analytically}
\Longrightarrow
\det_F S\text{ scalar Schur}.
}
\tag{9}
\]

This is the infinite-dimensional trace-class analogue of the finite determinant observation in `WP-176`; no new positivity theorem is created by taking the ordinary Fredholm determinant.

## 2. The Nevanlinna relation-valued Cayley escape remains closed in the trace-class regime

For the relation-valued family of `WP-176`, the canonical Cayley response is

\[
S_M(z)=I-2i(M(z)+iI)^{-1}.
\tag{10}
\]

If the resolvent defect satisfies

\[
(M(z)+iI)^{-1}\in\mathcal S_1(H)
\tag{11}
\]

trace-norm holomorphically on `C_+`, then

\[
S_M(z)-I=-2i(M(z)+iI)^{-1}\in\mathcal S_1(H).
\tag{12}
\]

`WP-176` already proves `||S_M(z)||<=1`. Applying (9) therefore yields

\[
\boxed{
D_M(z):=\det_F S_M(z)\in\mathcal S,
}
\tag{13}
\]

where `S` denotes the scalar Schur class on the upper half-plane.

The fixed multivalued sector from `WP-176` causes no exception. Its Cayley contribution is an identity block, so its ordinary Fredholm determinant is exactly `1`. All nonconstant determinant data comes from the trace-class active part and remains subject to (13).

The same result holds relative to any **fixed** unitary reference `U`. If

\[
S(z)U^*-I\in\mathcal S_1(H)
\tag{14}
\]

trace-norm holomorphically, then `S(z)U^*` is still a contraction and

\[
D_U(z):=\det_F(S(z)U^*)
\tag{15}
\]

is scalar Schur. Thus changing from an identity reference to a fixed lossless background does not create the missing archimedean phase.

## 3. Varying Hilbert spaces do not rescue the weak-boundary limit after scalarization

Let `S_m(z)` act on arbitrary Hilbert spaces `H_m`, with

\[
\|S_m(z)\|\le1,
\qquad S_m(z)-I\in\mathcal S_1(H_m),
\tag{16}
\]

and define

\[
D_m(z)=\det_F S_m(z).
\tag{17}
\]

Equation (8) is dimension-free, so every `D_m` belongs to the same scalar Schur unit ball. The boundary compactness and Luzin--Privalov argument of `WP-175` therefore applies verbatim. On no nonempty open real interval can the boundary traces of (17) converge, even distributionally, to the exact Gamma phase

\[
R_\infty(\tau)
=\pi^{i\tau}
\frac{\Gamma(\tfrac14-\tfrac{i\tau}{2})}
     {\Gamma(\tfrac14+\tfrac{i\tau}{2})}.
\tag{18}
\]

In particular, varying the boundary-space dimension, allowing infinite-dimensional trace-class defects, or taking a sequence of ordinary Fredholm determinants does not evade the weak-* `L^infty`, weak `L^p`, local `L^1`, convergence-in-measure, almost-everywhere, or distributional closures already excluded by `WP-175`.

Thus the Fredholm caveat left in `WP-175` and `WP-176` can be narrowed to **non-trace-class or genuinely regularized scalarizations**:

\[
\boxed{
\text{ordinary passive trace-class Fredholm determinant}
\Longrightarrow
\text{scalar Schur}
\not\to R_\infty
\text{ on any positive-length boundary window}.
}
\tag{19}
\]

## 4. A one-dimensional matched control shows exactly where regularization changes category

The trace-class theorem does **not** extend to modified determinants merely by invoking operator passivity. The failure is visible in dimension one.

Take the constant unitary contraction

\[
S=e^{i\theta},
\qquad K=S-I=e^{i\theta}-1.
\tag{20}
\]

Its ordinary determinant satisfies

\[
|\det_F S|=1.
\tag{21}
\]

For the standard second modified determinant, the trace-class identity is

\[
\det_2(I+K)
=\det_F(I+K)e^{-\operatorname{Tr}K}.
\tag{22}
\]

Hence in this one-dimensional control

\[
|\det_2 S|
=\exp(1-\cos\theta),
\tag{23}
\]

which is strictly greater than `1` whenever `theta` is not an integer multiple of `2pi`.

Therefore

\[
\boxed{
S\text{ contractive}
\centernot\Longrightarrow
|\det_2 S|\le1.
}
\tag{24}
\]

This is not a defect of the regularized determinant. It is the expected effect of its exponential trace counterterm. The control is useful because it identifies the exact logical boundary: **regularization can escape the Schur no-go precisely because it adds a scalar counterterm not controlled by the original contraction theorem**.

Any proposal based on `det_2`, higher modified determinants, zeta/heat-kernel determinants, dimension-dependent multiplicative renormalization, or another counterterm is therefore not killed by (19), but neither does it inherit the desired sign from passivity. The extra term must be intrinsic to the Mathia geometry, independently normalized, and accompanied by a new positive/coercive theorem before it can count toward Weil positivity.

## 5. Aggressive falsification and boundary conditions

**Trace-norm analyticity is a real hypothesis.** Pointwise membership `S(z)-I in S_1` together with operator-norm holomorphy is not silently promoted here to trace-norm holomorphy. The standard analytic Fredholm determinant statement requires an appropriate trace-class analytic family. A construction with a genuinely singular ideal topology lies outside this finding and must specify its domain and determinant notion explicitly.

**A parameter-dependent reference is extra mechanism.** Equation (15) permits a fixed unitary `U`. Allowing `U=U(z)` can manufacture arbitrary scalar phases and therefore cannot be treated as an innocent change of determinant origin. Such a reference would have to be produced canonically by the geometry and audited under the mandate's no-hand-picked-kernel/regularization control.

**Regularized determinants remain logically open.** Equation (24) is not a no-go for them; it proves that their scalar behavior is no longer governed by ordinary Hilbert passivity. A successful route would have to show that the exact counterterm generating the Gamma and polar pieces is source-forced and that the resulting renormalized scalar or quadratic form has an independent sign theorem.

**Nonseparable finite--archimedean assembly remains open.** As in `WP-176`, the argument assumes that an archimedean observable is scalarized through a determinant before the final global positive form is established. It does not apply if finite-prime incidence and the real-place sector are coupled first and the Gamma factor appears only as a derived signed observable after a global positivity theorem.

**Infinite negative index and true graph/domain degeneration are not classified.** Neither route is converted into positivity by this finding. They remain outside ordinary trace-class Hilbert-passive Fredholm theory and need their own coercivity mechanism.

A positive matched control is immediate: if `D` is any actual scalar Schur function with a trace-class realization, the ordinary Fredholm determinant construction is perfectly compatible with weak limits inside the Schur class. The contradiction is specific to trying to reach the exact non-Schur continuation (18), not to Fredholm determinants themselves.

## 6. Prior-art and novelty audit

All determinant theory used above is classical. Barry Simon, *Trace Ideals and Their Applications*, 2nd ed., Mathematical Surveys and Monographs 120, American Mathematical Society (2005), especially Chapter 3 on trace, determinant, and Lidskii's theorem and Chapter 9 on regularized determinants, is a standard reference for trace-class Fredholm determinants and their regularized variants.

Israel Gohberg, Seymour Goldberg, and Nahum Krupnik, *Traces and Determinants of Linear Operators*, Operator Theory: Advances and Applications 116, Birkhäuser (2000), DOI `10.1007/978-3-0348-8401-3`, treats trace-class/Hilbert--Schmidt operators, Fredholm determinants, regularized determinants, and higher-order regularized determinants systematically.

No novelty is claimed for the Fredholm product formula, analyticity of the trace-class determinant, spectral inclusion for contractions, or formula (22). The substantive Mathia-specific result is the combination of those classical facts with the exact passive-category frontier already established by `WP-175`--`WP-176`:

\[
\boxed{
\text{trace-class Fredholm scalarization is not an escape};
\quad
\text{regularization is the first determinant step that truly leaves Schur passivity}.
}
\tag{25}
\]

This is a prior-art classicalization and a decisive narrowing, not a proof of Weil positivity and not a new theorem in trace-ideal theory.

## 7. Research consequence

The determinant branch now has a clean boundary. Finite determinants and infinite-dimensional **ordinary trace-class Fredholm determinants** of passive Cayley responses remain scalar Schur and are excluded by the exact Gamma boundary obstruction. Merely increasing dimension or passing to a trace-class Fredholm limit does not help.

A surviving determinant-based construction must therefore use an operation that is mathematically stronger than ordinary Fredholm scalarization: a regularized determinant, a diverging counterterm, a singular ideal/domain limit, or a nonseparable global assembly. But once that step is taken, passivity no longer supplies the sign for free. The research obligation moves to the counterterm itself: derive it intrinsically, show that it simultaneously produces the required archimedean/global terms rather than inserting them, and prove a new coercivity/positivity theorem before matching it to the Weil explicit formula.