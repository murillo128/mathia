# AF-023 — Regular finite-Weil-test points have positive-dimensional Beurling fibers

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `NEGATIVE/OBSTRUCTION`

## Claim

Fix `A>0` and real test functions

\[
F_1,\ldots,F_d\in C_c^\infty(0,A),
\qquad d\ge1.
\]

For a locally finite generalized-prime multiset `Q={q_j}` with generator logarithms `\ell_j=\log q_j`, retain the finite Weil-test vector

\[
\mathcal W_{\mathcal F}(Q)
=
\bigl(W_Q(F_1),\ldots,W_Q(F_d)\bigr),
\]

where

\[
W_Q(F_i)
=
\sum_j\sum_{m\ge1}
\ell_j e^{-m\ell_j/2}F_i(m\ell_j).
\]

Select `N>d` generator logarithms and vary only those, keeping all remaining generators in a fixed background `B`. For `t>0` define the exact one-generator response

\[
G_i(t)
=
\sum_{m\ge1}
 t e^{-mt/2}F_i(mt).
\]

The sum is locally finite in `t`, hence `G_i` is smooth. On any sufficiently small ordered deformation chamber `U\subset(0,\infty)^N` around a center

\[
c=(c_1,\ldots,c_N),
\qquad c_1<\cdots<c_N,
\]

the exact retained map is

\[
\Psi(\ell_1,\ldots,\ell_N)
=
C_B+
\left(
\sum_{j=1}^N G_1(\ell_j),\ldots,
\sum_{j=1}^N G_d(\ell_j)
\right),
\]

with Jacobian

\[
\boxed{
J(c)_{ij}=G_i'(c_j).
}
\]

Then:

1. **Constant-rank points have an exact same-test manifold through the point.** If `J` has constant rank `r` on a neighborhood of `c`, the level set
   \[
   \Psi^{-1}(\Psi(c))
   \]
   is locally a smooth submanifold of dimension
   \[
   \boxed{N-r.}
   \]
   Since `r\le d<N`, this dimension is positive. Therefore every neighborhood of `c` contains distinct deformation tuples `\ell\ne c` with
   \[
   \Psi(\ell)=\Psi(c).
   \]

2. **Full row rank is a simple sufficient test and needs no constant-rank hypothesis beyond the point.** If
   \[
   \operatorname{rank}J(c)=d,
   \]
   some `d\times d` minor is nonzero at `c` and remains nonzero nearby. Thus `\Psi` is a submersion near `c`, and its exact fiber through `c` has dimension
   \[
   \boxed{N-d.}
   \]
   For the minimal choice `N=d+1`, the same-test fiber through `c` is locally a smooth curve.

3. **This closes AF-022's special-point escape whenever the rational-prime center is regular.** If the selected center is
   \[
   c_j=\log p_j
   \]
   for `N>d` ordinary rational primes, with all other rational primes in the background, then full row rank gives generalized-prime systems arbitrarily close to the ordinary primes whose values under every retained `F_i` are **exactly the same as the ordinary-prime value itself**. The controls differ only by finitely many continuously moved generator norms.

4. **Any surviving pointwise-rigidity claim must be singular.** If a center `c` were locally the unique source point with test vector `\Psi(c)`, then `J` cannot have locally constant rank there. In particular it cannot have full row rank. For `N>d`, special-point identifiability can occur only on a rank-stratification singularity where the Jacobian rank rises arbitrarily close to `c`.

5. **Regularity is generic in the unconstrained smooth test class at visible nonresonant centers.** Assume
   \[
   0<c_j<A
   \qquad(1\le j\le N)
   \]
   and
   \[
   c_j\ne m c_k
   \]
   for every `j\ne k` and every integer `m\ge1` with `m c_k<A`. Then the matrix entries `G_i'(c_j)` can be perturbed independently by arbitrarily small compactly supported smooth perturbations of the tests near the `c_j`. Full-row-rank matrices are open dense in `\mathbb R^{d\times N}`. Hence the full-row-rank condition is open and locally jet-generic among unconstrained finite smooth test families at every such center. For a rational-prime center the nonresonance condition is automatic once the selected primes satisfy `\log p_j<A`.

6. The genericity statement is **category-dependent**. Positivity cones, Fourier-support constraints, evenness, Paley--Wiener conditions, transform relations, or another intrinsic admissibility restriction may forbid the independent local test perturbations used above. In such a constrained class, pointwise rational-prime rigidity is not ruled out merely by ambient genericity; the rank and singular-locus audit must be repeated inside the actual admissible family.

The result is a point-fiber theorem, not just a neighborhood noninjectivity theorem. AF-022 showed that every sufficiently small neighborhood contains a pair of generalized-prime deformations with equal finite-test vectors, but that pair need not contain the center. AF-023 proves that every **regular** center itself lies on a positive-dimensional exact collision fiber.

## The one-generator response is smooth without the upper-half support restriction

AF-022 used generator logs in `(A/2,A)` so that every higher power was invisible and the retained contribution reduced to the first-power term. That restriction is convenient but unnecessary for smooth finite-dimensional analysis.

For each test `F_i`, define

\[
G_i(t)=\sum_{m\ge1} t e^{-mt/2}F_i(mt).
\]

Fix `t_0>0`. Because `F_i` has compact support in `(0,A)`, there is a neighborhood `V` of `t_0` and an integer `M` such that

\[
F_i(mt)=0
\qquad
(t\in V,\ m>M).
\]

Indeed, after shrinking `V` one may assume `t\ge t_0/2`, so `mt<A` requires `m<2A/t_0`. Thus on `V`, `G_i` is a finite sum of smooth functions and is itself smooth.

If only selected generator logs `\ell_1,\ldots,\ell_N` are varied, additivity over generators gives exactly

\[
W_{Q_\ell}(F_i)
=C_{B,i}+\sum_{j=1}^N G_i(\ell_j).
\]

No approximation and no deletion of the higher-prime-power structure has occurred; every visible multiple `m\ell_j` is already contained in `G_i`.

Differentiating gives

\[
J(\ell)_{ij}
=G_i'(\ell_j),
\]

where explicitly

\[
G_i'(t)
=
\sum_{m\ge1}e^{-mt/2}
\left[
\left(1-\frac{mt}{2}\right)F_i(mt)
+mtF_i'(mt)
\right].
\]

Again the derivative sum is locally finite.

In the special upper-half chamber `t>A/2`, only `m=1` survives, recovering AF-022's response

\[
G_i(t)=t e^{-t/2}F_i(t).
\]

The current point-fiber argument therefore applies both there and in chambers where several prime powers remain visible.

## Constant rank converts dimension mismatch into an exact fiber through the center

Assume `J` has constant rank `r` near `c`. The constant-rank theorem gives local source and target coordinates in which `\Psi` has normal form

\[
(u_1,\ldots,u_N)
\longmapsto
(u_1,\ldots,u_r,0,\ldots,0).
\]

Consequently the level set through `c` is locally a coordinate slice of codimension `r` and dimension

\[
N-r.
\]

Because `N>d\ge r`, this dimension is at least one. Thus there is a nonconstant smooth curve

\[
\gamma:(-\varepsilon,\varepsilon)\to U,
\qquad
\gamma(0)=c,
\]

such that

\[
\Psi(\gamma(t))=\Psi(c)
\]

for all sufficiently small `t`.

If `J(c)` has full row rank `d`, no extra rank assumption is needed. A nonzero `d\times d` minor remains nonzero on a neighborhood, while the rank can never exceed `d`. Hence rank is identically `d` nearby and the fiber dimension is `N-d`.

This is the exact local-identifiability dual of the ordinary implicit/regular-level-set theorem: when there are more free source coordinates than retained scalar outputs, a regular point cannot be point-identified.

## Rational-prime specialization

Choose `N>d` distinct ordinary primes

\[
p_1<\cdots<p_N
\]

whose logarithms lie in the region being varied, and let

\[
c=(\log p_1,\ldots,\log p_N).
\]

Put every other rational prime in the fixed background `B`. Since the prime logarithms form a discrete set, choose pairwise disjoint small intervals around the selected `\log p_j` that contain no other background generator. Restrict the deformation chamber so that each `\ell_j` remains in its own interval.

Every nearby tuple then defines an unambiguous generalized-prime multiset

\[
Q_\ell
=B\sqcup\{e^{\ell_1},\ldots,e^{\ell_N}\},
\]

and `Q_c` is exactly the rational-prime generator multiset.

If

\[
\operatorname{rank}
\bigl[G_i'(\log p_j)\bigr]_{1\le i\le d,\,1\le j\le N}
=d,
\]

the regular-level-set theorem produces arbitrarily close `\ell\ne c` with

\[
\boxed{
W_{Q_\ell}(F_i)=W_{\mathbb P}(F_i)
\qquad(1\le i\le d).
}
\]

This is stronger than the AF-022 conclusion

\[
\Psi(c+u)=\Psi(c-u),
\]

because one member of the collision is now the ordinary-prime system itself.

The deformation is finite and can be made arbitrarily small in generator-log coordinates. It preserves the entire unperturbed prime background and the exact prime-power formula for every changed generator.

## What a special-point escape must look like

Suppose a finite-test route claims that the rational primes are nevertheless locally unique among the allowed generalized-prime controls.

For any chosen `N>d` perturbable prime block, full row rank is impossible. More generally, if the rank were equal to some constant `r` on a neighborhood, the fiber would have dimension `N-r>0` and uniqueness would again fail.

Therefore local singleton fidelity requires the center to be a genuinely singular point of the test map: the Jacobian rank at the center must be lower than ranks attained arbitrarily nearby.

For `N=d+1`, a necessary first audit is therefore

\[
\boxed{
\det J_S(c)=0
\quad
\text{for every }d\text{-column subset }S.
}
\]

But vanishing of all maximal minors is only necessary, not sufficient for point rigidity. A rank-deficient point may still lie on a positive-dimensional level set. The elementary model

\[
(x,y)\mapsto x^2+y^2
\]

shows why singular points require a separate higher-order analysis: the origin has zero derivative yet an isolated zero-level fiber.

Thus the residual escape left after AF-023 is sharply localized:

\[
\boxed{
\text{finite-test rational-prime point rigidity}
\Longrightarrow
\text{singular rank-drop geometry}
\Longrightarrow
\text{higher-order audit required}.
}
\]

A proof route cannot appeal merely to the precision or nonlinear nature of its finite test values; it must explain why the rational-prime configuration is an exceptional singular source point and why the higher-order terms isolate it.

## Local jet genericity of the regular case

The singular escape is not generic in the ambient smooth test space, but the local bump argument requires the center to be both visible to the tests and nonresonant with the other selected generator multiples.

Assume

\[
0<c_j<A
\qquad(1\le j\le N)
\]

and

\[
c_j\ne m c_k
\]

for every `j\ne k` and every integer `m\ge1` with `m c_k<A`. The finite set

\[
S=\{m c_k:1\le k\le N,\ m\ge1,\ m c_k<A\}
\]

then contains each `c_j` only as the first multiple of its own coordinate. Hence one can choose pairwise disjoint neighborhoods `V_j` of the `c_j` such that

\[
V_j\cap\bigl(S\setminus\{c_j\}\bigr)=\varnothing.
\]

For a perturbation `\varphi_i` of the `i`-th test supported in `V_j` with

\[
\varphi_i(c_j)=0,
\]

every contribution to every column `k\ne j` vanishes, and all higher-multiple contributions to column `j` vanish as well. The induced Jacobian perturbation is therefore exactly

\[
\boxed{
\Delta J_{ij}=c_j e^{-c_j/2}\varphi_i'(c_j).
}
\]

Because `c_j e^{-c_j/2}\ne0`, the derivative `\varphi_i'(c_j)` can be prescribed independently. Summing disjoint bumps over `j`, independently for each row `i`, realizes an arbitrary sufficiently small perturbation of the whole `d\times N` Jacobian while remaining inside `C_c^\infty(0,A)^d`.

Full-row-rank `d\times N` matrices are open dense for `N\ge d`. Hence at every visible nonresonant center the full-row-rank condition is open dense in the unconstrained smooth finite-test class.

For a rational-prime center `c_j=\log p_j`, nonresonance is automatic for distinct selected primes: an equality

\[
\log p_j=m\log p_k
\]

would imply `p_j=p_k^m`, impossible for distinct primes. The visibility hypothesis is not automatic: this genericity statement applies only to selected prime blocks satisfying

\[
\boxed{\log p_j<A.}
\]

If `c_j\ge A`, every admissible test vanishes near every `m c_j`, so the corresponding Jacobian column is identically zero and ambient full-row-rank genericity can fail. Resonant visible centers likewise require a separate coupled-jet analysis and are not covered by the independent-bump argument.

This is **not** a statement that every analytically admissible explicit-formula test class is generic in this sense. If admissibility links values and derivatives nonlocally, imposes Fourier positivity, restricts to a finite-dimensional special family, or otherwise forbids independent local bumps, the relevant genericity space is smaller and must be analyzed separately.

## Prior art and novelty assessment

The differential-topological mechanism is classical.

- John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Graduate Texts in Mathematics 218, Springer (2012), DOI `10.1007/978-1-4419-9982-5`, is a standard source for the rank theorem, submersions, regular level sets, and the identification of the tangent space of a regular fiber with the kernel of the differential. AF-007 already uses the same classical machinery for vertical-fidelity defects.
- Jacobian-rank criteria and singular parameter loci are standard language in identifiability theory. Jean-Jacques Forneron, **“Detecting identification failure in moment condition models,”** *Journal of Econometrics* 238(1) (2024), 105552, DOI `10.1016/j.jeconom.2023.105552`, uses Jacobian/quasi-Jacobian rank to diagnose local or global identification failure in moment-condition models. This is neighboring methodology, not a source for the Beurling specialization.
- Elizabeth Gross, Nicolette Meshkat, and Anne Shiu, **“Identifiability of linear compartmental models: The singular locus,”** *Advances in Applied Mathematics* 133 (2022), 102268, DOI `10.1016/j.aam.2021.102268`, is direct prior art for organizing exceptional identifiability behavior through the rank-drop/singular locus of a parametrization map in a different model class.

No novelty is claimed for the constant-rank theorem, regular-level-set theorem, Jacobian identifiability criteria, singular loci, or smooth bump interpolation.

The Arithmetic Fidelity contribution is the exact specialization to the finite Weil-test / generalized-prime map and the resulting closure of AF-022's explicit boundary: **at every regular rational-prime center, the ordinary-prime system itself lies on a positive-dimensional exact same-test Beurling fiber.** Hence any finite-test claim of rational-prime special-point rigidity is forced into a checkable singular-rank and then higher-order regime.

A targeted literature search did not identify an established Beurling-prime theorem formulated as this finite-Weil-test point-fiber criterion. That absence is not treated as a novelty proof; the result is classified primarily as a direct application of classical differential topology to the exact Mathia compression.

## Boundaries and failure modes

- The source family is the continuously deformable Beurling generalized-prime category. If a route declares the rational primes to be the only admissible source by definition, this control family is excluded, but that exclusion itself cannot serve as evidence that downstream data encode rational-prime specificity.
- `N>d` counts free **real** generator-log coordinates against effective real retained outputs. Complex tests should be split into real and imaginary components, and algebraically redundant outputs should be removed before rank is interpreted.
- The constant-rank conclusion is local. It gives arbitrarily close exact controls, not a global classification of the whole finite-test fiber.
- Full row rank is sufficient, not necessary, for a positive-dimensional fiber. Rank-deficient but locally constant points also have positive-dimensional fibers.
- Rank deficiency alone does not prove special-point rigidity. Singular points require higher-order or global analysis, and many singular points still have large fibers.
- The genericity statement is for unconstrained smooth test functions at visible nonresonant centers. It must not be exported to invisible/resonant centers or unchanged to Fourier-positive, band-limited, Paley--Wiener, transform-coupled, positivity, or other restricted test categories.
- Moving finitely many generalized-prime generators preserves local finiteness and the exact multiplicative prime-power construction, but it need not preserve stronger global Beurling counting asymptotics unless those are imposed and checked separately.
- The theorem concerns a finite test vector. AF-020's complete infinite test family on a support interval is a different destination and can recover the visible prime-power measure exactly.
- The result says nothing about the location, multiplicity, or simplicity of zeta zeros and is not evidence for RH.

## Decisive audit test

For any finite-test explicit-formula, trace, positivity, or moment route claiming rational-prime specificity:

1. write the exact finite-dimensional map from a finite block of admissibly movable generator logs to every retained real output, including all visible prime-power contributions;
2. compute the Jacobian at the ordinary-prime center;
3. remove output redundancies and test whether the Jacobian has full row rank;
4. if it does, conclude immediately that the rational-prime point lies on a positive-dimensional exact matched-control fiber;
5. if rank is lower but locally constant, apply the constant-rank theorem and reach the same conclusion;
6. if point rigidity survives, identify the precise rank-drop singularity and prove a higher-order isolation theorem rather than citing finite-test precision;
7. repeat the rank calculation inside the **actual admissible test/control category** if positivity, transform, symmetry, or counting constraints reduce the ambient deformation freedom.

A route that does not pass steps 2--6 has not established finite-test rational-prime fidelity.

## Consequence for the line

AF-020, AF-021, and AF-022 separated three increasingly strict losses:

\[
\text{fixed support}
\to
\text{finite test dimension}
\to
\text{actual Beurling deformation collisions}.
\]

AF-023 now resolves the main special-point loophole at regular centers:

\[
\boxed{
\operatorname{rank}J(c)=d,\ N>d
\Longrightarrow
\dim_c\Psi^{-1}(\Psi(c))=N-d>0.
}
\]

For ordinary primes, finite-test point fidelity therefore cannot be a generic consequence of exact scalar measurements. Any surviving mechanism must make the rational-prime source an intrinsically forced **singular** point of the retained map and then prove that higher-order structure isolates that singular fiber.

This gives the next sharp research frontier: classify which intrinsic constraints can force such singular isolation without merely hard-coding the rational primes, and determine whether the constrained positivity/spectral test families used by concrete RH routes actually possess that exceptional geometry.