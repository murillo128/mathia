# WI-183 — Maynard--Pratt bows identify slow horizontal drift as the obstruction beyond fixed-depth screening

**Status:** `LITERATURE+DERIVED + PRIOR-ART-REDIRECT + STRUCTURAL-RIGIDITY`. This finding does **not** improve the unconditional simple-critical-zero proportion and does not assert that bow configurations occur among zeta zeros. It records a load-bearing prior-art redirect for the RH-facing part of the Weil-inertia program. Maynard and Pratt's peer-reviewed half-isolated-zero method gives an unconditional source detector for a substantial class of off-critical zeros, but their Section 8 identifies a specific remaining obstruction: a short cluster whose ordinates form an approximately critical-scale arithmetic progression while the real parts drift slowly away from `1/2` and then return. They call these configurations **bows of zeros** and explain that their local zero detector is defeated by Poisson cancellation while their global clustering mechanism also has no leverage.

The important Mathia consequence is that the source-level obstruction already known in the zero-density literature is not merely an isolated shallow off-line pair or a fixed off-line vertical lattice. It is a **two-dimensional moving-depth lattice**. After the standard Weil-inertia local normalization, Maynard--Pratt's explicit bow has constant-order vertical spacing and horizontal depth changing by `o(1)` per vertical step. Specializing their harmless fixed spacing constant to `2π` makes the vertical sites exactly the unit lattice used by the WI screening controls. Thus a source coercivity theorem that only excludes isolated confluence, or only excludes zeros on finitely many fixed vertical lines, does not address the obstruction singled out by the literature. The next serious source bridge must control horizontal drift/curvature along locally arithmetic vertical chains, or otherwise prove that functional-equation-symmetric bows cannot occur.

## 1. The primary-source result is unconditional only for half-isolated zeros

The primary source is James Maynard and Kyle Pratt, **Half-Isolated Zeros and Zero-Density Estimates**, *International Mathematics Research Notices* 2024:19 (2024), 12978--13014, DOI `10.1093/imrn/rnae191`, arXiv:2206.11729v2. They introduce a vertical-distribution-sensitive zero detector. Their Theorem 4 proves that a half-isolated zero has a short zero-detecting Dirichlet polynomial, and Corollary 5 gives the unconditional density-hypothesis-strength estimate

\[
\#\{\rho=\beta+i\gamma:\ \rho\text{ half-isolated},\ \beta\ge\sigma,\ T\le\gamma\le2T\}
\le T^{2(1-\sigma)+o(1)}.
\tag{1}
\]

The stronger zero-density conclusion for **all** zeros in their paper assumes Hypothesis `\mathcal F`, namely that the nontrivial zeros lie on finitely many fixed vertical lines. This distinction is essential here. Equation (1) is an unconditional theorem for the half-isolated subclass; it is not an unconditional density theorem for arbitrary off-line zeros.

The same paper explicitly asks what prevents removal of `\mathcal F`. Section 8 names the potential bad configurations **bows of zeros** and states that the new ideas in the paper do not detect them. This is therefore not a Mathia-invented adversarial model: it is the obstruction isolated by the primary zero-density source itself.

## 2. Maynard--Pratt's bow geometry

Their explicit model has `T^ε` consecutive hypothetical zeros with ordinate spacing

\[
\gamma_{j+1}-\gamma_j=\frac{c}{\log T},
\qquad c>0\ \text{fixed},
\tag{2}
\]

while the real parts rise linearly from `1/2` to `3/4`, remain on a middle plateau, and then descend linearly to `1/2`. On the rising ramp,

\[
\beta_j=\frac12+\frac{j}{T^\varepsilon},
\qquad
\gamma_j=T_0+\frac{cj}{\log T},
\tag{3}
\]

up to the endpoint conventions of their displayed equation (8.1); the descending ramp is symmetric at the level of this model.

Maynard--Pratt make two precise qualitative observations about this configuration. First, on every `T^{o(1)}` local scale, an interior zero looks like the middle of a vertical arithmetic progression because the real parts are almost constant on that scale. They say that the local power-sum detector from their Section 4 is then defeated by the same Poisson-summation mechanism as their arithmetic-progression control. Second, the whole bow is only `T^ε` long and is based on the critical line, so their global clustering argument does not recover the lost leverage. They conclude that detecting bows would be essentially the remaining obstacle if the only uniformly small local power sums came from a small number of vertical arithmetic progressions.

Their earlier arithmetic-progression control is explicit. For smooth weights on points in an imaginary arithmetic progression, Poisson summation makes the relevant exponential sum smaller than every power of the progression length on the detector interval. Thus the word “bow” is not only geometric terminology: its interior is deliberately engineered so that a local detector sees almost the same cancellation as a vertical progression.

## 3. Exact normalization into the Weil-inertia coordinates

Use the standard local coordinate for ordinates

\[
x_j:=\gamma_j\frac{\log T}{2\pi}
\tag{4}
\]

and the normalized horizontal depth used in the Lamzouri/Weil confluence analysis,

\[
a_j:=\left(\beta_j-\frac12\right)\frac{\log T}{2\pi}.
\tag{5}
\]

Equations (2)--(3) give, exactly on the rising ramp,

\[
x_{j+1}-x_j=\frac{c}{2\pi},
\qquad
 a_{j+1}-a_j=rac{\log T}{2\pi T^\varepsilon}.
\tag{6}
\]

Hence

\[
\boxed{a_{j+1}-a_j=o(1)}
\tag{7}
\]

while the vertical spacing remains order one. In the special case `c=2π`, which is a legitimate specialization of the fixed positive constant in the hypothetical bow model,

\[
\boxed{x_{j+1}-x_j=1.}
\tag{8}
\]

Thus the bow becomes a unit vertical lattice whose horizontal depth changes adiabatically from site to site.

If such a right-half-plane bow consisted of actual zeta zeros, the functional equation would supply the reflected zeros `1-\beta_j+i\gamma_j` at the same ordinates. Away from the critical-line endpoints, the WI local picture is therefore a sequence of symmetric off-line pairs with depths `±a_j`, not a one-sided population. The correct adversarial object for the inertia line is the **symmetrized bow**.

This exact normalization is the bridge to the existing WI controls. WI-005/WI-006 and WI-115/WI-119 expose Poisson/alias screening on critical vertical lattices, while WI-140/WI-141/WI-173 expose confluence blindness for shallow off-line pairs and bounded-bandwidth continuous spectral data. Maynard--Pratt supply independent zeta-source prior art in which the two features are combined geometrically: locally arithmetic ordinates together with slowly varying horizontal position.

## 4. What can and cannot be transferred from the existing screening theorems

There is a rigorous local transfer near the critical-line ends of the bow. Fix a horizontal-depth bound `A` and a block length `R`. On the portion of a ramp with `|a_j|\le A`, every `R`-site block satisfies

\[
\max_{0\le r<R}|a_{j+r}-a_j|
\le
R\frac{\log T}{2\pi T^\varepsilon}
=o(1).
\tag{9}
\]

For a fixed admissible Weil/Lamzouri kernel, the corresponding finite matrix entries are analytic in the horizontal shifts and therefore uniformly continuous on every bounded complex strip. Consequently, for `c=2π`, any fixed `R` matrix block in this bounded-depth endpoint region converges entrywise to the constant-depth unit-lattice block with depth `a_j`. Any fixed continuous finite-dimensional matrix functional has the same limit. Thus the fixed-depth screening controls are stable under the bow's `o(1)` site-to-site drift on bounded-depth local windows.

The bounded-depth qualification is load-bearing. In the middle of Maynard--Pratt's explicit bow, `\beta-1/2` is a fixed positive constant, so `|a_j|\asymp\log T`; an entire kernel of fixed exponential type can grow rapidly in that imaginary direction. Equation (9) alone therefore does **not** justify importing WI-173 or a finite-matrix continuity estimate uniformly across the deep interior. No such claim is made here.

That gap does not erase the prior-art redirect, because Maynard--Pratt independently analyze the deep interior with their own source detector and conclude that the local power sums are suppressed there by Poisson summation. What is shared between the two programs is the obstruction geometry, not an asserted identity between their Dirichlet-polynomial detector and the Montgomery--Taylor matrix at arbitrarily large normalized horizontal depth.

## 5. Why half-isolated detection does not close the WI confluence problem

It would be tempting to read (1) as the missing zeta-specific theorem that rules out the abstract WI confluence controls. That inference is not available. Maynard--Pratt themselves exhibit bows precisely to explain why the half-isolated method plus their clustering machinery does not yield an unconditional all-zero density theorem.

At the level of research logic, three increasingly strong adversarial controls must therefore be kept separate:

- an isolated shallow conjugate pair can make the Lamzouri continuous deficit arbitrarily small;
- a fixed-depth critical vertical lattice can be screened by the support-limited Poisson/alias mechanism;
- a bow can be locally close to a vertical arithmetic progression while its horizontal depth drifts globally, evading a source argument that relies on a finite set of fixed vertical lines.

The third control is not implied by the first two as a theorem about zeta, and the first two are not refuted by the half-isolated theorem. The useful conclusion is instead that **source coercivity must survive all three geometries simultaneously**.

## 6. Prior-art and novelty audit

The half-isolated detector, estimate (1), Hypothesis `\mathcal F`, the explicit bow (8.1), and the conclusion that Poisson cancellation makes bow interiors problematic are Maynard--Pratt prior art. No novelty is claimed for those statements or for the elementary normalization (4)--(8).

A repository-local audit found no existing `weil_inertia` finding or commit centered on half-isolated zeros, Maynard--Pratt, or bows. The closest persisted controls are WI-119 (fixed-order bandlimited higher-correlation screening), WI-141/WI-173 (continuous spectral and bounded-bandwidth confluence blindness), and WI-170--WI-182 (population budgets and source-correction/rank interfaces). Those findings identify what ordinary support-one, continuous, and finite-rank information cannot do, but they do not import the peer-reviewed zero-density obstruction in which the **horizontal coordinate itself drifts along a locally arithmetic chain**.

The durable delta of WI-183 is therefore a **prior-art redirect and strengthened falsification control**, not a new zero-density theorem. It identifies a source-generated geometry that any proposed RH-facing anti-confluence mechanism should be tested against before persistence.

## 7. Consequence for the research line

The current frontier should not ask only for a lower bound on the horizontal depth of an isolated off-line pair, nor only for a theorem excluding a fixed collection of vertical lines. A viable source bridge can instead target one of the genuinely two-dimensional features that a bow cannot hide: quantitative horizontal variation or curvature along a near-arithmetic ordinate chain, interaction between the two functional-equation-reflected arms, a source-controlled failure of local AP cancellation when the depth varies, or a theorem forcing a half-isolated/detectable zero inside every sufficiently long off-line bow.

A decisive next test is therefore:

\[
\boxed{
\text{Can established or new prime-side information assign a positive cost to horizontal drift along a critical-scale vertical AP?}
}
\tag{10}
\]

The cost must remain meaningful under slow drift and must not reduce to a bounded-bandwidth continuous observable already killed by confluence or Poisson aliasing. Conversely, an explicit symmetrized bow model satisfying the currently established Weil/pair-correlation interfaces with no additional extensive cost would close another broad class of source-coercivity proposals.

Until such an input is found, Maynard--Pratt's bow should be treated as a canonical adversarial control for any claimed defect-to-zero bootstrap. This finding does not alter the current unconditional proportion bound, does not prove the existence of bows, and does not turn the conditional finite-vertical-line density theorem into evidence for RH.