# WP-069 — positive Hardy extensions cannot carry the unbounded Mangoldt anchor at finite energy

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CLASSICAL-FUNCTIONAL-ANALYSIS` for the regular positive-extension branch left open by WP-068. The only abstract ingredient is Cauchy--Schwarz for a positive semidefinite Hermitian form. The Mathia-specific obstruction comes from the exact Hardy-shell null sequence constructed in WP-068. No theorem-level historical novelty is claimed.

WP-068 proved that the canonical Hardy-shell Mangoldt functional

\[
L(B)=\operatorname{Tr}(HB)
\]

is unbounded for the positive shell energy

\[
Q_H(B)=\operatorname{Tr}(B^*HB).
\]

More sharply, the full-root cumulative shells give explicit vectors

\[
X_N=\frac{1}{\log N}
\sum_{\substack{d\mid N\\d>1}}\Gamma_d
\]

such that

\[
\boxed{
Q_H(X_N)\longrightarrow0,
\qquad
L(X_N)=1.
}
\tag{1}
\]

WP-068 used (1) to close every **finite scalar counterterm** preserving the same Hardy square. A natural remaining hope is more geometric: enlarge the positive space by an archimedean, boundary, cohomological, or other auxiliary sector and realize the exact Mangoldt term as a mixed pairing against a distinguished finite-energy global vector.

That entire regular positive-extension mechanism is impossible if the original Hardy energy is retained on the finite shell sector.

Let `V=\mathcal A_0` be the algebraic Hardy-shell span and let `\widetilde V` be any complex vector space containing `V`. Suppose `\widetilde q` is a positive semidefinite Hermitian sesquilinear form on `\widetilde V` whose restriction to `V` is exactly the Hardy form:

\[
\widetilde q(B,B)=Q_H(B),
\qquad B\in V.
\tag{2}
\]

Then there is **no** vector `a\in\widetilde V` of finite `\widetilde q`-energy satisfying

\[
\boxed{
\widetilde q(B,a)=L(B)
\qquad(B\in V).
}
\tag{3}
\]

Indeed positivity forces

\[
|\widetilde q(B,a)|^2
\le
\widetilde q(B,B)\widetilde q(a,a)
=Q_H(B)\widetilde q(a,a).
\tag{4}
\]

Putting `B=X_N` and using (1) gives

\[
1
\le
Q_H(X_N)\widetilde q(a,a)
\longrightarrow0,
\]

an immediate contradiction.

Thus **no finite-dimensional or infinite-dimensional positive Hilbert/form extension, no bounded or unbounded positive operator realization, and no regular positive block completion can turn the WP-067/WP-068 Mangoldt anchor into polarization against a finite-energy vector while leaving the Hardy finite block unchanged.** The obstruction is dimension-free and does not assume compactness, passivity, locality, or a Schur-complement model.

The escape route is correspondingly sharp. Any viable positive global construction must do at least one of the following before the Mangoldt cross term is represented:

- change the finite-shell energy by a new term that is non-negligible on the normalized full-root differences `X_N`;
- use a singular/infinite-energy boundary object together with additional mathematics controlling its renormalized limit;
- abandon ordinary positive Hilbert polarization in favor of a genuinely different quotient, grading, intersection/cohomological sign theorem, or other structure.

A stable bounded perturbation of the Hardy norm is not enough. If a modified positive finite energy is

\[
Q_{\rm new}(B)=Q_H(B)+R(B),
\qquad R(B)\ge0,
\tag{5}
\]

and a finite-energy vector `a` represents `L`, then Cauchy--Schwarz gives

\[
1=|L(X_N)|^2
\le
\bigl(Q_H(X_N)+R(X_N)\bigr)Q_{\rm new}(a).
\tag{6}
\]

Hence

\[
\boxed{
\liminf_{N\to\infty}R(X_N)>0
}
\tag{7}
\]

whenever `Q_new(a)<\infty`. In particular every perturbation satisfying

\[
R(B)\le C Q_H(B)
\tag{8}
\]

for a finite constant `C` still fails, because then `R(X_N)\to0`. So a successful archimedean/global sector must be **singular relative to the Hardy-shell topology in a precisely testable sense**: it has to see order-one energy on a sequence that the intrinsic finite Hardy geometry sends to zero.

## 1. Positive block forms automatically make every finite-energy mixed functional bounded

The same obstruction can be written in the language of the non-scalar coupling that WP-068 explicitly left open.

Let `K` be any auxiliary complex vector space, let `A` be a positive semidefinite Hermitian form on `K`, and let `\beta:V\times K\to\mathbb C` be sesquilinear. Consider the block quadratic form

\[
\mathcal Q(B,y)
=
Q_H(B)+2\operatorname{Re}\beta(B,y)+A(y).
\tag{9}
\]

Assume

\[
\mathcal Q(B,y)\ge0
\qquad(B\in V,\ y\in K).
\tag{10}
\]

Fix `B` and `y`. Positivity of

\[
\mathcal Q(tB,y)
=|t|^2Q_H(B)+2\operatorname{Re}\bigl(t\beta(B,y)\bigr)+A(y)
\]

for every complex scalar `t` forces the discriminant inequality

\[
\boxed{
|\beta(B,y)|^2\le Q_H(B)A(y).
}
\tag{11}
\]

This is simply Cauchy--Schwarz derived directly from block positivity; no prior boundedness assumption on `\beta` is needed.

If a distinguished auxiliary state `y_\infty` is supposed to supply the exact finite arithmetic anchor,

\[
\beta(B,y_\infty)=-L(B),
\tag{12}
\]

then (11) and (1) imply

\[
1
\le
Q_H(X_N)A(y_\infty)
\longrightarrow0
\]

whenever `A(y_\infty)<\infty`. Therefore such a positive block form does not exist.

This strengthens the scalar conclusion of WP-068 in exactly the direction that was still open there: replacing a scalar finite part by an arbitrarily complicated **regular positive auxiliary sector** does not help if the arithmetic is still read as polarization against one finite-energy auxiliary state and the finite diagonal remains `Q_H`.

## 2. Completion and quotient cannot hide the obstruction

Let `\mathcal H_H` be the completion of `V` in the norm `Q_H^{1/2}`. Equation (1) says

\[
X_N\longrightarrow0
\qquad\text{in }\mathcal H_H,
\]

while `L(X_N)=1`. Hence `L` cannot descend to a continuous functional on this completion.

More generally, suppose a positive extension contains `V` **isometrically** for the `Q_H` seminorm, possibly after quotienting the radical of the enlarged form. Every finite-energy vector in the resulting pre-Hilbert/Hilbert space defines a continuous polarization functional on the embedded copy of `V`. Equation (1) excludes `L` from all of them.

Thus quotienting or completing the same positive geometry does not turn the formal identity anchor of WP-067 into a legitimate finite-energy class. To preserve the exact Mangoldt values, the quotient/completion must alter the topology seen by the sequence `X_N`, not merely remove null vectors or complete the existing shell norm.

## 3. The obstruction is stronger than finite-dimensionality

It would be easy to interpret WP-068 as saying only that one scalar counterterm is insufficient, and then try a finite collection of archimedean modes. The present argument shows that dimension is irrelevant.

For any auxiliary dimension -- one, finite, countable, or arbitrary -- each fixed finite-energy auxiliary state `y` generates through a positive block form a functional bounded by

\[
|\beta(B,y)|
\le \sqrt{A(y)}\,Q_H(B)^{1/2}.
\tag{13}
\]

The exact Mangoldt anchor violates this estimate along `X_N`. Adding more regular modes cannot change that fact unless the finite-shell restriction itself changes or the arithmetic is carried by a singular object outside the finite-energy form domain.

This is distinct from the passive Kron obstruction of WP-026. WP-026 uses the stronger `M`-matrix/Markov sign structure of resistor-network Schur complements to show that passive elimination cannot manufacture the negative Weil self-energy. Here there is no passivity, graph Laplacian, finite-dimensionality, or Schur hypothesis at all; the only assumption is **positivity plus preservation of the Hardy-shell finite energy**. Conversely, the present result concerns the specific Hardy-shell Mangoldt anchor of WP-067/WP-068 and does not subsume WP-026's finite-Weil-comb statement.

## 4. Stable positive corrections must fail on the same full-root control

Equation (7) supplies a reusable matched-control test for any proposed archimedean or global correction to this Hardy branch.

Suppose a candidate adds a positive term `R` while claiming to preserve the intrinsic Hardy geometry at finite places. If its construction is regular enough that

\[
R(X_N)\longrightarrow0,
\tag{14}
\]

then the exact Mangoldt anchor still cannot be represented by finite-energy polarization. In particular this kills every correction continuous with respect to the `Q_H` topology, including every relative bound of the form (8).

A genuine escape therefore has to make the same canonical full-root sequence expensive:

\[
Q_H(X_N)\to0
\quad\text{but}\quad
R(X_N)\not\to0.
\tag{15}
\]

That requirement is useful because the `X_N` are not tuned prime test vectors. They are the full-root cumulative shells forced by PC-079, and they exist for every integer `N`. Any proposed global correction can therefore be tested against them before invoking zeta zeros, analytic continuation, or an RH-equivalent positivity criterion.

## 5. Adversarial boundaries

The claim deliberately does **not** rule out several materially different mechanisms.

1. **A changed finite geometry.** If the global construction changes the shell norm so that `X_N` no longer tends to zero, Cauchy--Schwarz no longer gives the contradiction. Equation (7) states exactly how large that change must be for a finite-energy anchor.
2. **A singular anchor net.** A family `a_T` with `\widetilde q(a_T,a_T)\to\infty` may converge only distributionally to the Mangoldt functional. WP-067 already exhibits the analogous divergent cutoff anchor. Positivity of each cutoff does not by itself control a renormalized finite part; proving a canonical signed limit would be new mathematics.
3. **Test-dependent auxiliary data.** A construction may map each finite test object `B` to an auxiliary state `y(B)` rather than pairing against one fixed global anchor. Then the effective finite energy has changed and must be analyzed as a new geometry rather than as an extension of (2).
4. **Indefinite or graded pairings.** Krein, supertrace, intersection, or cohomological mechanisms can escape ordinary Hilbert Cauchy--Schwarz, but their desired final nonnegativity must then come from a separate theorem rather than from the positive block form excluded here.
5. **Nonlinear selectors.** Determinants, top volumes, and other nonlinear readouts such as WP-030 are outside the linear polarization hypothesis. They still face the separate global-Weil bridge problems already recorded in this line.

The finding therefore does not say that every conceivable finite--archimedean coupling is impossible. It says that **a regular positive enlargement of the exact Hardy-shell square cannot host its exact Mangoldt anchor at finite energy**.

## 6. Prior-art and novelty audit

The abstract functional-analysis statement is classical. A positive semidefinite Hermitian form satisfies Cauchy--Schwarz, and a finite-energy vector defines a bounded polarization functional; after completion this is the elementary Hilbert-space/Riesz framework already used in WP-067. No novelty is claimed for those facts.

The Mathia-specific content is their combination with the exact sequence (1), which itself depends on PC-079's full-root cumulative-shell identity and PC-080's exact resultant/Mangoldt trace through WP-068. The consequence is not a new formulation of Weil's criterion: it uses no zeta zeros, completed zeta function, explicit-formula positivity assumption, or RH-equivalent kernel. It is instead a no-go for one concrete Mathia-native attempt to obtain the required sign geometrically.

A targeted comparison against classical Weil positivity, Hilbert-space positive-form theory, and neighboring RH positivity formulations did not reveal an external theorem asserting this specific Hardy-shell obstruction. That absence is not used as a novelty claim. The durable result is the exact internal boundary: **WP-068's unboundedness rules out every finite-energy positive extension preserving `Q_H`, not merely finite scalar renormalizations.**

## 7. Falsification tests

The result is exact and has direct failure modes.

1. Falsify WP-068's sequence by finding an error in either `L(X_N)=1` or `Q_H(X_N)\to0`.
2. Exhibit a positive semidefinite Hermitian extension `\widetilde q` satisfying (2) and a finite-energy vector `a` satisfying (3). This would contradict Cauchy--Schwarz applied to `X_N`.
3. Exhibit a positive block form (9)--(10) with finite `A(y_\infty)` and (12). This is the same contradiction in block coordinates.
4. For the perturbed escape (5), exhibit a finite-energy anchor with `R(X_N)\to0`. Equation (6) forbids it.

A construction that changes the finite restriction, uses infinite anchor energy, or leaves the ordinary positive-form category does not falsify the finding; it lies outside its hypotheses.

## Research consequence

The Hardy/Hilbert branch now has a sharper global-completion boundary than the scalar no-go of WP-068:

\[
\boxed{
\text{exact Mangoldt anchor}
+\text{ ordinary positive polarization}
+\text{ finite anchor energy}
\Longrightarrow
\text{the global geometry must change the }Q_H\text{ topology.}
}
\]

More concretely, the canonical normalized full-root differences `X_N` are now a mandatory discriminator. Any proposed positive archimedean/global completion that remains bounded or asymptotically invisible on them cannot work. A surviving route must supply a genuinely new nonlocal/singular energy with order-one response on `X_N`, or leave the regular positive-extension framework entirely. This is the exact place where new geometry, rather than a larger auxiliary Hilbert space, has to enter.