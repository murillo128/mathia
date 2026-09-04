# PC-172 — finite-support singular Robin forms collapse to the anchor delta-prime

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-STRUCTURE` + `DECISIVE-NEGATIVE` for the finite-support distributional boundary-form escape left open by PC-170/PC-171. If a fixed singular boundary coefficient is supported on finitely many points of the root circle and its sesquilinear multiplication form obeys the exact first-order covariance forced by the Prime-Circle power refinements, then the full refinement semigroup collapses it to a single universal distribution: a multiple of `delta'_1` at the common anchor. Finite atomic root weights vanish identically. The formal `delta'` survivor is reflection-odd, contains no shell arithmetic, and is not a semibounded perturbation of the canonical second-order bulk form.

PC-170 ruled out every bounded, compact, or finite-rank boundary operator under exact second-order refinement covariance and explicitly left raw point-supported/distributional boundary data outside its theorem. PC-171 then classified the stronger fixed self-adjoint operator intertwining law but again left singular point-supported relations outside the common Fourier-core setting. The most direct singular continuation is therefore to replace the bounded boundary operator by a finite-support distribution acting multiplicatively on smooth boundary traces. This finding classifies that continuation exactly.

## 1. Distributional boundary covariance

Write the boundary circle as `theta in R/(2 pi Z)` with common anchor at `theta=0`, and let

\[
T_n(\theta)=n\theta\pmod{2\pi},
\qquad
(C_nf)(\theta)=f(T_n\theta).
\tag{1}
\]

Let `u` be a distribution on `S^1` with finite support. On trigonometric polynomials define the sesquilinear multiplication form

\[
b_u(f,g)=\langle u,\overline f g\rangle.
\tag{2}
\]

This includes finite atomic root weights `u=sum_j w_j delta_{theta_j}` as well as finite linear combinations of derivatives of point masses. Demand the same first-order covariance that appears in the Robin term of PC-170,

\[
\boxed{
b_u(C_nf,C_ng)=n\,b_u(f,g)
\qquad(n\ge2).
}
\tag{3}
\]

Taking `f=1` shows that (3) is exactly the distributional push-forward eigenrelation

\[
\boxed{(T_n)_*u=n u\qquad(n\ge2),}
\tag{4}
\]

because

\[
\langle (T_n)_*u,h\rangle
=\langle u,h\circ T_n\rangle.
\]

Thus there is no ambiguity from the quadratic-form notation: every smooth test function is already probed by setting one factor equal to the constant mode.

## 2. Exact finite-support classification

Let

\[
a_k=\langle u,e^{ik\theta}\rangle,
\qquad k\in\mathbb Z.
\tag{5}
\]

Equation (4) gives

\[
\boxed{a_{nk}=n a_k}
\tag{6}
\]

for every integer `n>=2` and every `k`. In particular, taking `k=1`,

\[
\boxed{a_m=m a_1\qquad(m\ge1).}
\tag{7}
\]

The derivative of the Dirac distribution at the anchor satisfies

\[
\langle\delta'_0,e^{im\theta}\rangle=-im.
\tag{8}
\]

Hence, with `c=i a_1`, the finite-support distribution

\[
v=u-c\delta'_0
\tag{9}
\]

has

\[
\langle v,e^{im\theta}\rangle=0
\qquad(m\ge1).
\tag{10}
\]

Now use only the standard local structure of a finite-support distribution. For distinct support points `theta_j`,

\[
v=\sum_{j=1}^J\sum_{r=0}^{M_j}c_{j,r}\,\delta_{\theta_j}^{(r)}.
\tag{11}
\]

Its positive Fourier coefficients therefore form a finite exponential polynomial,

\[
\langle v,e^{im\theta}\rangle
=\sum_{j=1}^J P_j(m)e^{im\theta_j},
\tag{12}
\]

with ordinary polynomials `P_j`. Distinct exponential-polynomial sequences `m^r lambda^m` are linearly independent on the positive integers. One elementary proof is to form the generating function of (12): it is rational, with its only possible poles at the distinct points `z=e^{-i theta_j}` and pole orders determined by `deg P_j+1`; if every coefficient in (10) vanishes, the generating function is identically zero, so every principal part and hence every `P_j` vanishes.

Therefore `v=0`, and the complete classification is

\[
\boxed{u=c\,\delta'_0.}
\tag{13}
\]

Conversely, direct differentiation gives

\[
(T_n)_*\delta'_0=n\delta'_0,
\tag{14}
\]

so (13) is sharp.

If `b_u` is Hermitian, then `u` is a real distribution and `c` is real. If `u` is a finite complex Borel measure — in particular any finite weighted set of primitive roots — then (13) forces

\[
\boxed{u=0,}
\tag{15}
\]

because `delta'_0` is not a measure. The measure subcase also has an even shorter proof: push-forward is a contraction in total variation, whereas `(T_n)_*u=n u` would multiply the norm by `n>1`.

Thus **no fixed finite collection of root point masses, with arbitrary complex weights, can supply the missing exactly covariant Robin datum.** Allowing finite-order point singularities buys only the first derivative at the universal fixed anchor.

## 3. The unique survivor is universal and reflection-odd

The Prime-Circle configuration with anchor `1` is preserved by complex conjugation, which acts on the boundary as

\[
J(\theta)=-\theta.
\tag{16}
\]

But

\[
J_*\delta'_0=-\delta'_0.
\tag{17}
\]

Consequently a reflection-invariant finite-support distribution satisfying exact refinement covariance must vanish:

\[
\boxed{J_*u=u\ \Longrightarrow\ u=0.}
\tag{18}
\]

Even if orientation is retained and the `delta'` term is allowed, it is not arithmetic. Equations (13)--(14) use only the bare circle, the common fixed point of all power maps, and first-order homogeneity. The same survivor exists before primitive roots, cyclotomic layers, old/new incidence, or prime labels are introduced. It is therefore a matched non-prime control rather than a Prime-Circle information carrier.

This is the distributional analogue of the universality seen in PC-170/PC-171: exact refinement determines the scaling order, while the only finite-support object at that order is the derivative of the fixed-point delta distribution.

## 4. `delta'` is not an admissible semibounded Robin form for the canonical bulk

There is a second obstruction. The canonical second-order half-cylinder bulk form from PC-170 is

\[
q_0[F]=\int_0^\infty\int_{S^1}
\left(|\partial_tF|^2+|\partial_\theta F|^2\right)
\frac{d\theta}{2\pi}\,dt.
\tag{19}
\]

For a smooth boundary trace `f`,

\[
b_{\delta'_0}(f,f)
=\langle\delta'_0,|f|^2\rangle
=-\frac{d}{d\theta}|f(\theta)|^2\bigg|_{\theta=0}.
\tag{20}
\]

Take, for `N>=1` and `sigma in {+1,-1}`,

\[
F_{N,\sigma}(t,\theta)
=e^{-t}+\sigma i N^{-1/2}e^{-Nt}e^{iN\theta}.
\tag{21}
\]

Its boundary value is

\[
f_{N,\sigma}(\theta)
=1+\sigma iN^{-1/2}e^{iN\theta}.
\tag{22}
\]

The two Fourier modes are orthogonal in `theta`, so the bulk energy is exactly

\[
\boxed{q_0[F_{N,\sigma}]=\frac32}
\tag{23}
\]

for every `N` and either sign. Its `L^2` norm is also uniformly bounded. But (20) gives

\[
\boxed{b_{\delta'_0}(f_{N,\sigma},f_{N,\sigma})
=2\sigma\sqrt N.}
\tag{24}
\]

Hence for every nonzero real `c`, choosing `sigma=-sgn(c)` yields

\[
q_0[F_{N,\sigma}]+c\,b_{\delta'_0}(f_{N,\sigma},f_{N,\sigma})
=\frac32-2|c|\sqrt N\longrightarrow-\infty.
\tag{25}
\]

Equivalently, the `delta'` boundary form is not continuous on the natural `H^{1/2}(S^1)` trace space: the traces (22) have uniformly bounded `H^{1/2}` norm while (24) diverges. Thus the sole nonzero finite-support covariant distribution is **not** a standard semibounded Robin-form perturbation of the canonical bulk operator.

This does not prove that every conceivable renormalized singular self-adjoint boundary relation is impossible. It proves that the straightforward distributional multiplication-form realization either vanishes or leaves the ordinary semibounded Robin framework.

## 5. Stress tests and exact boundary of the no-go

The full power semigroup matters. For one fixed map `T_n`, first-derivative distributions supported on finite periodic cycles of that map can be transported around the cycle. Requiring (3) for every integer `n>=2` collapses that freedom to the common fixed anchor. Thus PC-172 is a full-refinement statement, not a claim about a single dilation.

Finite support also matters. Infinite or dense distributional data can have much richer transfer-operator behavior under expanding circle maps. Likewise a level-dependent family `u_n`, a shell-dependent singular relation, or a cross-level boundary condition need not satisfy the fixed-distribution equation (4). Those remain outside the theorem.

Finally, the theorem concerns multiplication forms `b_u(f,g)=<u,bar f g>`. General singular self-adjoint boundary relations can mix trace and normal-derivative channels, add finite-dimensional extension spaces, or require renormalization rather than arise from multiplication by a distribution. PC-172 must not be read as a classification of that broader extension theory.

A direct falsification test for the stated class is simple: exhibit a finitely supported distribution `u` not proportional to `delta'_0` for which `(T_n)_*u=n u` for every `n>=2`. The Fourier argument (5)--(13) rules this out exactly.

## 6. Prior art and novelty audit

The ingredients around the result are classical. The fact that a distribution supported on finitely many points is a finite sum of derivatives of Dirac masses is standard distribution theory (Schwartz/Hörmander). `delta'` point interactions and singular self-adjoint extensions are also classical objects; they are not being proposed here as new operators. The generalized Robin framework already anchored in `SOURCES.md` by Gesztesy--Mitrea covers the ordinary self-adjoint nonlocal Robin setting used by PC-170, while the Steklov/DtN source there fixes the natural `H^{1/2}` boundary scale.

Targeted searches across expanding-circle push-forwards/eigenmeasures, point-supported distributions, `delta'` point interactions, and singular Robin extensions did not locate this exact finite-support simultaneous-eigenrelation for all power maps. That absence is **not** treated as a novelty claim. Once the covariance equation (4) is posed, the classification is elementary Fourier/distribution algebra. The durable contribution is the Prime-Circle-specific obstruction: the raw finite root-incidence escape explicitly left outside PC-170 cannot carry exact fixed boundary arithmetic; its only distributional survivor is the universal anchor derivative and that survivor is outside the semibounded form class.

## 7. Consequence for the Prime-Circle/RH search

The natural repair

\[
\text{finite primitive-root point data}
\longrightarrow
\text{singular fixed Robin coefficient}
\longrightarrow
\text{exact power refinement}
\longrightarrow
\text{new spectral/RH mechanism}
\]

is therefore closed for finite-support multiplication distributions. Finite atomic weights are killed outright. Allowing derivatives produces exactly one formal mode, `delta'_1`, which is fixed-point geometry rather than arithmetic, is odd under the intrinsic conjugation symmetry, and destroys semiboundedness of the canonical second-order Robin form.

What remains genuinely open is narrower and structurally different: shell- or level-dependent singular families, infinite-support transfer-operator data, renormalized point interactions/general boundary relations mixing trace and normal derivative, weaker form-covariant unbounded operators whose primitive lattice coefficients are actually derived from old/new geometry, and genuinely nonlinear or cross-level constructions. No `s`-parameter, zeta zero set, functional equation, or critical-line mechanism is produced here; this finding instead removes the simplest singular fixed-point repair from the viable Prime-Circle search space.
