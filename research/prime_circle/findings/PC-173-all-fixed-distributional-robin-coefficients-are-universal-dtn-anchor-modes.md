# PC-173 — all fixed distributional Robin coefficients are universal DtN-anchor modes

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-STRUCTURE` + `DECISIVE-NEGATIVE` for the arbitrary-distribution continuation explicitly left open by PC-172. If a fixed distributional multiplication coefficient on the root circle obeys the exact first-order covariance forced by every Prime-Circle power refinement, then without any support assumption it lies in the two-dimensional universal space spanned by the anchor derivative `delta'_1` and the distributional Dirichlet-to-Neumann image `|D| delta_1`. Reflection symmetry removes the odd `delta'` direction but leaves only the classical even `|D| delta` direction. Every nonzero Hermitian member of this two-dimensional family makes the canonical second-order bulk-plus-boundary form unbounded below, so no fixed distributional multiplication coefficient supplies a semibounded prime-sensitive Robin repair.

PC-170 ruled out bounded boundary operators and identified `|D|` as the classical first-order scale-correct operator. PC-171 then collapsed the strong self-adjoint intertwining problem to four universal first-order operator parameters. PC-172 treated singular multiplication forms but assumed finite support, obtaining only `delta'_1` and explicitly leaving infinite-support transfer-operator data open. The finite-support hypothesis is in fact unnecessary for the fixed-distribution multiplication problem: the full power semigroup determines every Fourier coefficient immediately.

## 1. Exact covariance on arbitrary circle distributions

Write the common anchor `1` as `theta=0` on `S^1`, and let

\[
T_n(\theta)=n\theta\pmod{2\pi},
\qquad
(C_nf)(\theta)=f(T_n\theta),
\qquad n\ge2.
\tag{1}
\]

Let `u` now be an **arbitrary distribution** on `S^1`; no finite-support, measure, or regularity hypothesis is imposed. On smooth boundary traces define the formal multiplication form

\[
b_u(f,g)=\langle u,\overline f g\rangle.
\tag{2}
\]

Demand the exact first-order covariance inherited from the Robin term in PC-170,

\[
\boxed{
b_u(C_nf,C_ng)=n\,b_u(f,g)
\qquad(n\ge2).
}
\tag{3}
\]

As in PC-172, setting `f=1` shows that (3) is equivalent to the simultaneous distributional push-forward relation

\[
\boxed{(T_n)_*u=n u\qquad(n\ge2).}
\tag{4}
\]

Indeed every smooth test function is already reached in (2) by taking one factor equal to the constant mode. Thus the classification problem is exact and linear; no positivity or self-adjoint-extension theory is being inserted into the derivation.

## 2. The full distribution space collapses to two Fourier rays

For

\[
a_k=\langle u,e^{ik\theta}\rangle,
\qquad k\in\mathbb Z,
\tag{5}
\]

relation (4) gives

\[
\boxed{a_{nk}=n a_k}
\tag{6}
\]

for every `n>=2` and every integer `k`. Taking `k=0` gives `a_0=0`. Taking `k=1` and `k=-1` gives, for every `m>=1`,

\[
\boxed{
a_m=mA,
\qquad
a_{-m}=mB,
}
\qquad
A=a_1,
\quad B=a_{-1}.
\tag{7}
\]

There are no further coefficients to choose. Conversely, the sequence (7) has only linear growth and therefore defines a distribution on the circle, so every pair `(A,B)` really occurs.

Introduce the standard first-order Fourier multiplier

\[
D=-i\partial_\theta,
\qquad
|D|e_k=|k|e_k.
\tag{8}
\]

Distributionally,

\[
\langle\delta'_0,e^{ik\theta}\rangle=-ik,
\qquad
\langle |D|\delta_0,e^{ik\theta}\rangle=|k|.
\tag{9}
\]

Hence (7) is equivalent to the complete classification

\[
\boxed{
u=\alpha\,|D|\delta_0+\beta\,\delta'_0,}
\tag{10}
\]

with

\[
\alpha=\frac{A+B}{2},
\qquad
\beta=\frac{B-A}{2i}.
\tag{11}
\]

For a real distribution, equivalently for a Hermitian form (2), `B=overline A`, so `alpha,beta` are real. Thus the Hermitian solution space is exactly two-dimensional over `R`.

PC-172 is recovered as the finite-support subcase. The distribution `delta'_0` is supported at the anchor, whereas `|D|delta_0` is not finitely supported. In Abel regularization its Fourier series is

\[
\sum_{k\in\mathbb Z}|k|r^{|k|}e^{ik\theta}
=2\operatorname{Re}\frac{re^{i\theta}}{(1-re^{i\theta})^2},
\tag{12}
\]

which tends away from the anchor to

\[
-\frac{1}{2\sin^2(\theta/2)}.
\tag{13}
\]

So the one extra direction unlocked by dropping finite support is precisely the standard order-one nonlocal circle singularity.

## 3. Reflection leaves only the classical DtN singularity

Complex conjugation of the Prime-Circle configuration acts on the boundary by

\[
J(\theta)=-\theta.
\tag{14}
\]

The two universal distributions have opposite parity,

\[
J_*\delta'_0=-\delta'_0,
\qquad
J_*(|D|\delta_0)=|D|\delta_0.
\tag{15}
\]

Therefore an intrinsically reflection-symmetric fixed coefficient has the exact form

\[
\boxed{u=\alpha |D|\delta_0.}
\tag{16}
\]

This sharpens the finite-support conclusion of PC-172: reflection no longer forces an arbitrary distribution to vanish, but the unique even survivor is still completely prime-blind. It is determined by the bare circle, the universal fixed anchor, and first-order homogeneity before primitive roots, cyclotomic shells, old/new incidence, or prime labels are introduced.

The appearance of `|D|` is also analytically classical rather than a new spectral mechanism. The source already recorded in `research/prime_circle/SOURCES.md` for PC-170 identifies `|D|=sqrt(-partial_theta^2)` with the Dirichlet-to-Neumann/Steklov operator of the Euclidean unit disk. Equation (10) uses its distributional extension applied to the anchor delta; it does **not** create a new Prime-Circle Hamiltonian or a zeta-dependent symbol.

## 4. Every nonzero Hermitian survivor destroys semiboundedness

The two-dimensional classification alone leaves a possible objection: perhaps the reflection-even `|D|delta_0` direction, unlike the `delta'_0` survivor tested in PC-172, defines an admissible singular Robin correction. It does not.

Use the canonical half-cylinder bulk form from PC-170,

\[
q_0[F]=\int_0^\infty\int_{S^1}
\left(|\partial_tF|^2+|\partial_\theta F|^2\right)
\frac{d\theta}{2\pi}\,dt.
\tag{17}
\]

For `N>=1` and a unit complex number `eta`, set

\[
F_{N,\eta}(t,\theta)
=e^{-t}+N^{-1/2}\eta\,e^{-Nt}e^{iN\theta}.
\tag{18}
\]

Orthogonality of the two angular modes gives

\[
\boxed{q_0[F_{N,\eta}]=\frac32}
\tag{19}
\]

for every `N` and `eta`, while the bulk `L^2` norm is uniformly bounded. Its boundary trace is

\[
f_{N,\eta}(\theta)=1+N^{-1/2}\eta e^{iN\theta}.
\tag{20}
\]

Directly from (9),

\[
\langle |D|\delta_0,|f_{N,\eta}|^2\rangle
=2\sqrt N\,\operatorname{Re}\eta,
\tag{21}
\]

and

\[
\langle\delta'_0,|f_{N,\eta}|^2\rangle
=2\sqrt N\,\operatorname{Im}\eta.
\tag{22}
\]

For a nonzero real pair `(alpha,beta)`, choose

\[
\eta=-\frac{\alpha+i\beta}{\sqrt{\alpha^2+\beta^2}}.
\tag{23}
\]

Then the boundary term of (10) is

\[
\boxed{
b_u(f_{N,\eta},f_{N,\eta})
=-2\sqrt{\alpha^2+\beta^2}\,\sqrt N.
}
\tag{24}
\]

Consequently

\[
q_0[F_{N,\eta}]+b_u(f_{N,\eta},f_{N,\eta})
\longrightarrow-\infty,
\tag{25}
\]

although both the bulk energy (19) and the `L^2` norm remain bounded. Equivalently, no nonzero real solution of (4) extends as a lower-bounded distributional multiplication perturbation on the natural `H^{1/2}` trace scale.

Thus dropping finite support does reveal one additional even nonlocal distribution, but **it does not restore an admissible semibounded fixed Robin form**. The obstruction is now complete for arbitrary fixed Hermitian distributional multiplication coefficients satisfying exact power covariance.

## 5. Stress tests and exact boundary of the no-go

The full semigroup condition is load-bearing. A single expanding map `T_n` has many dilation or transfer-operator orbits; equation (7) follows because the same eigenrelation is imposed for every integer refinement. The Prime-Circle contract supplies precisely that full power semigroup.

The fixed-coefficient assumption is also load-bearing. A level-dependent or shell-dependent family `u_n`, or a cross-level relation, need not solve one simultaneous equation (4). Likewise the theorem concerns the multiplication form (2). Singular self-adjoint boundary relations that mix trace and normal derivative, introduce auxiliary extension spaces, or require renormalization are not classified by (10).

Finally, the result does not classify the weak form-covariant **operator** problem `C_n^*AC_n=nA` left open by PC-170/PC-171. An operator has two Fourier indices and can retain primitive lattice-direction data; a multiplication distribution has only the single Fourier sequence (5), which is why the simultaneous power relations are much more rigid here.

A direct falsification test is exact: a counterexample in the stated class must be a distribution `u` satisfying `(T_n)_*u=nu` for all `n>=2` whose Fourier coefficients are not of the two-ray form (7). Since distributions on `S^1` are uniquely determined by their Fourier coefficients, equations (6)--(11) exclude such a counterexample.

## 6. Prior art and novelty audit

All surrounding analytic ingredients are classical. Fourier coefficients characterize distributions on the torus; expanding-map push-forwards and their adjoint composition/Koopman operators are standard transfer-operator constructions; and PC-170 already records the classical identification of the disk Dirichlet-to-Neumann operator with `|D|`. Targeted literature searches across expanding-circle transfer operators, power-map push-forwards on distributions, simultaneous eigen-distributions, fractional Laplacians on the torus, and singular Robin/point-interaction form theory did not locate this exact two-dimensional simultaneous-eigenspace statement for the complete family `theta -> n theta`.

That search boundary is **not** a novelty claim. Once (4) is written, the Fourier classification is elementary, and `|D|delta_0` is standard fractional/DtN distributional structure. The durable result is the Prime-Circle-specific closure statement: the infinite-support loophole explicitly left by PC-172 adds exactly one universal classical direction and no prime-shell degree of freedom, while the semiboundedness test (18)--(25) eliminates that direction together with `delta'_0` from the canonical Robin-form route.

## 7. Consequence for the Prime-Circle/RH search

The fixed distributional repair

\[
\text{singular boundary coefficient}
\longrightarrow
\text{exact power refinement}
\longrightarrow
\text{semibounded Robin spectrum}
\longrightarrow
\text{new RH mechanism}
\]

is closed for **all** Hermitian multiplication distributions, not merely finite root support. Exact covariance leaves only the universal anchor pair `|D|delta_1` and `delta'_1`; intrinsic reflection leaves only the classical DtN-derived member; and every nonzero real combination is unbounded below relative to the canonical bulk form.

What remains open is structurally different rather than a larger distribution class: shell- or level-dependent singular families, genuinely renormalized boundary relations, the weaker two-index form-covariant operator problem with geometry-derived primitive-direction coefficients, cross-level boundary couplings, or nonlinear constructions. No `s`-parameter, zeta zero set, functional equation, or critical-line selector is produced here. PC-173 instead closes the fixed distributional multiplication branch that PC-172 had deliberately left open.