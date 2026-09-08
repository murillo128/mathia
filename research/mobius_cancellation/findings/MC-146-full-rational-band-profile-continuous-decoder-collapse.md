# MC-146 — Continuous scalarization of the full rational Bost–Connes band profile remains profinite

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Work in the canonical number-state representation of the Bost–Connes algebra `A_BC` used in `MC-144`–`MC-145`. Let

\[
\mathbb Q_{>0}=\{q=a_q/b_q:\gcd(a_q,b_q)=1\}
\]

with one reduced positive pair `(a_q,b_q)` chosen for each positive rational. For a fixed bounded observable `A\in A_{BC}`, define its **full fixed-rational band profile** at `k\ge1` by

\[
\Phi_A(k)
=
\bigl(R_q(A)(k)\bigr)_{q\in\mathbb Q_{>0}},
\qquad
R_q(A)(k)
=
\langle\varepsilon_{a_qk},\pi(A)\varepsilon_{b_qk}\rangle.
\tag{1}
\]

`MC-145` proves separately for every fixed `q` that `R_q(A)` extends uniquely to a continuous function

\[
f_q\in C(\widehat{\mathbb Z}),
\qquad
\|f_q\|_\infty\le \|A\|.
\tag{2}
\]

Therefore the **entire countable band profile** extends canonically to the continuous map

\[
\boxed{
\widetilde\Phi_A:
\widehat{\mathbb Z}
\longrightarrow
K_A:=
\prod_{q\in\mathbb Q_{>0}}
\overline{D}(0,\|A\|),
\qquad
x\longmapsto(f_q(x))_q,
}
\tag{3}
\]

where `K_A` carries the product topology. Its image

\[
Y_A:=\widetilde\Phi_A(\widehat{\mathbb Z})
\tag{4}
\]

is compact.

Consequently **no continuous scalar decoder of the full infinite profile can uniformly recover Möbius orientation on the square-free integers with error below one**. Precisely,

\[
\boxed{
\inf_{D\in C(Y_A)}
\sup_{\substack{k\ge1\\ \mu(k)\ne0}}
\left|D(\Phi_A(k))-\mu(k)\right|
=1.
}
\tag{5}
\]

More generally the same lower bound holds for any decoder with continuous profinite side information,

\[
G:\widehat{\mathbb Z}\times Y_A\to\mathbb C,
\qquad
k\longmapsto G(k,\Phi_A(k)).
\tag{6}
\]

Thus the infinite-family loophole left open explicitly by `MC-145` does **not** survive merely by taking all fixed positive-rational bands at once and applying a product-topology-continuous scalarization. A surviving bounded Bost–Connes route must use a discontinuous/singular infinite-coordinate readout, genuinely relational data not reduced to one continuous scalar profile, a different state/representation geometry, an unbounded or measurable construction, or an aggregate source-to-Mertens mechanism not requiring pointwise Möbius recovery.

There is also a useful varying-ratio corollary. If a selector

\[
s:\widehat{\mathbb Z}\to\mathbb Q_{>0}
\tag{7}
\]

is continuous when `\mathbb Q_{>0}` has the discrete topology, then `s` has finite image and

\[
x\longmapsto f_{s(x)}(x)
\tag{8}
\]

is continuous on `\widehat{\mathbb Z}`. Hence

\[
\boxed{
\sup_{\substack{k\ge1\\ \mu(k)\ne0}}
|R_{s(k)}(A)(k)-\mu(k)|\ge1.
}
\tag{9}
\]

So allowing the rational ray to depend on `k` helps only if the selection rule itself fails to extend continuously in the profinite topology, or if some other hypothesis of the theorem is abandoned.

## 1. Coordinatewise band continuity gives continuity of the full profile

For every reduced `q=a_q/b_q`, `MC-145` gives the exact identity

\[
R_q(A)(k)
=
\left\langle
\varepsilon_k,
\pi(\mu_{a_q}^*A\mu_{b_q})
\varepsilon_k
\right\rangle.
\tag{10}
\]

`MC-144` then identifies the right side with the restriction of a unique coefficient-algebra function

\[
f_q
=
E_{\mathrm{diag}}(\mu_{a_q}^*A\mu_{b_q})
\in C(\widehat{\mathbb Z}).
\tag{11}
\]

Because `\mu_{a_q}` and `\mu_{b_q}` are isometries and `E_diag` is contractive,

\[
\|f_q\|_\infty\le\|A\|.
\tag{12}
\]

Hence `(3)` is well defined. By the defining universal property of the product topology, a map into a product is continuous exactly when every coordinate projection is continuous. Since

\[
\operatorname{pr}_q\circ\widetilde\Phi_A=f_q,
\]

all coordinates are continuous and therefore `\widetilde\Phi_A` is continuous.

The profinite integers are compact, while `K_A` is Hausdorff. Thus `Y_A` in `(4)` is compact. No summability, decay in `q`, or uniform convergence across rational rays is required: product continuity is deliberately the weakest standard topology for which all fixed-band coordinates remain continuous observables.

## 2. Every continuous full-profile decoder lands back in the profinite quotient

Take `D\in C(Y_A)`. Composition gives

\[
g_D:=D\circ\widetilde\Phi_A
\in C(\widehat{\mathbb Z}).
\tag{13}
\]

On positive integers,

\[
g_D(k)=D(\Phi_A(k)).
\tag{14}
\]

`MC-143` proves the exact profinite Möbius obstruction

\[
\inf_{g\in C(\widehat{\mathbb Z})}
\sup_{\mu(k)\ne0}|g(k)-\mu(k)|=1.
\tag{15}
\]

Applying `(15)` to `g_D` gives the lower bound in `(5)` for every continuous decoder. The constant decoder `D\equiv0` has uniform error exactly `1` on square-free integers, proving equality.

The same argument proves `(6)`: if `G` is continuous on `\widehat{\mathbb Z}\times Y_A`, then

\[
x\longmapsto G(x,\widetilde\Phi_A(x))
\tag{16}
\]

is continuous because `x\mapsto(x,\widetilde\Phi_A(x))` is continuous. Thus adding any side information that is itself profinite-continuous cannot repair the lost Möbius orientation.

The obstruction can also be seen directly through the collision behind `MC-143`. There exist primes `p_j` and products of two distinct primes `r_js_j` such that

\[
p_j\to1,
\qquad
r_js_j\to1
\quad\text{in }\widehat{\mathbb Z},
\tag{17}
\]

while

\[
\mu(p_j)=-1,
\qquad
\mu(r_js_j)=+1.
\tag{18}
\]

Continuity of `\widetilde\Phi_A` forces both full infinite profiles to converge to the same point `\widetilde\Phi_A(1)`. Any continuous scalarization must therefore assign asymptotically the same value to two arithmetic sequences whose target signs remain opposite.

## 3. Continuous infinite-coordinate decoding is the uniform closure of finite-coordinate decoding

The result is not merely a formal use of composition. On the compact profile space `Y_A`, continuous dependence on infinitely many rational rays is itself uniformly approximable by finite-coordinate dependence.

Let `\mathcal A` be the unital `*`-algebra on `Y_A` generated by the coordinate restrictions

\[
y\longmapsto y_q,
\qquad q\in\mathbb Q_{>0},
\tag{19}
\]

and their complex conjugates. Every member of `\mathcal A` depends on only finitely many rational-band coordinates. The algebra separates points of `Y_A`, because two distinct product points differ in at least one coordinate. By the complex Stone–Weierstrass theorem,

\[
\overline{\mathcal A}^{\|\cdot\|_\infty}
=C(Y_A).
\tag{20}
\]

Therefore every continuous full-profile decoder is a uniform limit of polynomial finite-band decoders. `MC-145` already classifies every finite stage as profinite-continuous; `(20)` shows that completing those readouts in the natural uniform/product-continuous sense does not create a new scalar information class.

This pinpoints the escape requirement more sharply than the finite-family statement: merely taking **more and more fixed bands** is insufficient whenever the final infinite-family statistic remains continuous on the compact profile it generates. Any genuine escape must fail that closure mechanism or avoid scalar pointwise decoding altogether.

## 4. A profinite-continuous varying-ratio selector is automatically finite-valued

Give `\mathbb Q_{>0}` the discrete topology and let `s` satisfy `(7)`. Since `\widehat{\mathbb Z}` is compact, the image

\[
s(\widehat{\mathbb Z})
\tag{21}
\]

is compact in a discrete space, hence finite. Each fiber

\[
s^{-1}(\{q\})
\tag{22}
\]

is clopen. On that clopen fiber, the selected readout `(8)` equals the continuous function `f_q`. A finite clopen pasting of continuous functions is continuous, so `(8)` belongs to `C(\widehat{\mathbb Z})`. Equation `(9)` follows again from `MC-143`.

Equivalently, a `k`-dependent rational ray that is stable under sufficiently fine congruence information can use only finitely many rays globally. To exploit genuinely unbounded ratio complexity, the selector must become discontinuous with respect to the profinite topology or depend on information not present in the profinite coordinate `k`.

This is a topological statement about the **selection rule**, not a claim that every scale-varying or adaptive off-diagonal construction is impossible.

## 5. Relation to the full two-index matrix kernel

Every pair of positive integers `(m,n)` admits the unique decomposition

\[
m=a_q d,
\qquad
n=b_q d,
\qquad
d=\gcd(m,n),
\tag{23}
\]

for the reduced rational ratio `q=m/n`. Thus the complete matrix of a bounded observable can be coordinatized by rational ray and common scale:

\[
(m,n)
\longleftrightarrow
(q,d).
\tag{24}
\]

The profile `(1)` collects, at each fixed common scale `k`, all rational-ray coefficients

\[
\bigl\langle\varepsilon_{a_qk},\pi(A)\varepsilon_{b_qk}\bigr\rangle_q.
\tag{25}
\]

The theorem therefore reaches beyond any finite subset of the two-index kernel. But it still does **not** collapse the full matrix object as a relational/operator-valued structure. It classifies only scalar outputs obtained continuously from the profile at the same profinite scale, optionally with continuous side information.

For example, a mechanism comparing coefficients at different `k`, taking a singular supremum/selection over ratios, using a topology stronger or different from the product topology, or retaining an operator rather than scalarizing it is outside the theorem until an additional continuity or factorization argument is proved.

## 6. Prior art and novelty audit

The operator-algebraic framework is established prior art.

- Jean-Benoît Bost and Alain Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica (N.S.) **1** (1995), 411–457, DOI `10.1007/BF01589495`, introduced the arithmetic `C^*`-dynamical system used here.
- Marcelo Laca and Iain Raeburn, *A Semigroup Crossed Product Arising in Number Theory*, Journal of the London Mathematical Society **59** (1999), 330–344, DOI `10.1112/S0024610798006620`, realize the Bost–Connes algebra as a semigroup crossed product and supply the established language behind the homogeneous monomials used in `MC-145`.
- Marcelo Laca, *From Endomorphisms to Automorphisms and Back: Dilations and Full Corners*, Journal of the London Mathematical Society **61** (2000), 893–904, DOI `10.1112/S0024610799008492`, explicitly dilates the Bost–Connes system to the positive-rational action on finite adeles, so the `\mathbb Q_{>0}` homogeneous organization is not new.
- The product-topology continuity criterion, compactness of products, compact-to-discrete finite-image fact, and Stone–Weierstrass theorem used in Sections 1–4 are standard general topology/functional analysis.

A targeted search for Bost–Connes off-diagonal matrix coefficients, positive-rational grading, and rational-band observables found the established crossed-product/dilation literature above but did not identify a source stating `(5)` as a named theorem. **No novelty inference is drawn from that search outcome.** The proof is an immediate exact synthesis of `MC-143`–`MC-145` with standard topology.

The line-specific mathematical delta is narrower: the explicit infinite-family escape left open by `MC-145` is closed under the natural product-continuity hypothesis, and a profinite-continuous scale-dependent ratio choice is shown to collapse back to finitely many fixed rays.

## Boundaries and falsification tests

- **Product-topology continuity is load-bearing.** A discontinuous or singular decoder of the infinite profile is not classified by `(5)`. In particular, an infinite-coordinate rule may evade Stone–Weierstrass uniform closure if the final operation is not continuous on `Y_A`.
- **The selector corollary requires profinite continuity.** An adaptive ratio rule on ordinary integers that does not extend continuously to `\widehat{\mathbb Z}` may have infinite image and is outside `(9)`.
- **The observable is bounded and fixed.** Scale-dependent families `A_k`, unbounded affiliated operators, or measurable constructions can escape the norm/topological framework.
- **The representation is the canonical number-state representation.** Other coherent state geometries or representations are not classified.
- **The theorem concerns pointwise scalar recovery.** An aggregate statistic may control `M(x)` without approximating `\mu(k)` term by term; such a route must supply an independent quantitative source-to-excursion theorem.
- **The full two-index kernel is not declared profinite-trivial.** Cross-scale relations, operator-valued structure, singular selections, and nonlocal comparisons across `(q,k)` remain open unless separately shown to factor through a continuous scalar profile.
- **No RH implication or Mertens improvement follows.** This is an exact information-loss obstruction.

A proposed escape is decisively killed by this finding if its bounded canonical-number-state readout can be written as

\[
k\longmapsto
G\bigl(k,\Phi_A(k)\bigr)
\tag{26}
\]

for one fixed `A` and a continuous `G` on the corresponding compact profinite/profile domain. It survives this finding only by proving why its actual readout does not admit that factorization, or why pointwise Möbius recovery is not the relevant transfer target.

## Consequence for the line

`MC-145` reduced every fixed positive-rational matrix band, and every finite continuously decoded family of fixed bands, to the coefficient/profinite quotient. The present finding closes the natural continuous completion of that family: **all fixed rational rays may be retained simultaneously without gaining a pointwise Möbius scalar carrier, provided their infinite profile is decoded continuously**.

The residual bounded Bost–Connes frontier is therefore no longer “use infinitely many off-diagonal bands” in the abstract. It must identify a mathematically justified source of genuinely discontinuous/adaptive ratio information, a cross-scale relation not representable by one continuous profile at `k`, an alternative state/readout geometry, or an aggregate mechanism that transfers to first-absolute Mertens excursion without reconstructing the sign pointwise.

This remains subordinate to the broader line objective: even a surviving noncommutative carrier is useful only if it yields source information quantitatively cheaper than the RH-complete Mertens endpoint.