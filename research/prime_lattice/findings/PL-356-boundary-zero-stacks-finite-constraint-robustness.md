# PL-356 — Boundary zero stacks survive every finite homogeneous coefficient repair

**Evidence:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE`.

**Parent finding:** `PL-355`.

`PL-355` shows that the natural prime-supported Hilbert completion

\[
\mathcal P^2_0
=
\left\{F_c(s)=\sum_p c_p p^{-s}:c\in\ell^2(\mathcal P)\right\}
\]

admits nonzero functions with any fixed bounded real Blaschke zero stack accumulating at `Re s=1/2`, for example

\[
S=\left\{\frac12+2^{-j}:j\ge1\right\}.
\tag{1}
\]

The tail-supported form of Seip's `\alpha=\infty` construction, already audited in `PL-355`, gives more than existence of one such vector: for every sufficiently large cutoff `N`, there is a nonzero coefficient vector supported on primes `p\ge N` whose Dirichlet series vanishes on the same prescribed stack `S`.

That tail freedom forces an exact robustness statement. If

\[
\mathcal N_S
:=
\left\{c\in\ell^2(\mathcal P):F_c(s)=0\ \text{for every }s\in S\right\},
\tag{2}
\]

then `\mathcal N_S` is infinite-dimensional. Consequently, for every finite family of bounded linear coefficient functionals

\[
L_1,\ldots,L_m\in(\ell^2(\mathcal P))^*,
\]

one has

\[
\boxed{
\dim\left(\mathcal N_S\cap\bigcap_{r=1}^m\ker L_r\right)=\infty.
}
\tag{3}
\]

Thus no finite collection of homogeneous continuous coefficient relations can repair the loss of exact-zero-stack rigidity produced by the `\ell^2` completion. This is complementary to `PL-353`: there finite coefficient constraints disappear in the local subcritical Sobolev/form closure; here even constraints that are perfectly continuous in the native prime `\ell^2` topology still leave infinitely many nonzero vectors carrying the same boundary zero stack.

## 1. Tail-supported zero-set functions force infinite dimension

Fix a bounded real sequence `S\subset(1/2,\infty)` satisfying the Seip/Dirichlet-space condition used in `PL-355`; the explicit stack (1) is the main case. The `\alpha=\infty` tail construction gives, for every sufficiently large integer `N`, a nonzero

\[
c^{(N)}\in\mathcal N_S
\]

with

\[
c^{(N)}_p=0\qquad(p<N).
\tag{4}
\]

Construct inductively a sequence `c^{(k)}\in\mathcal N_S`. Choose `N_1` large enough for the construction and let `q_1` be the least prime with `c^{(1)}_{q_1}\ne0`. Having chosen `c^{(1)},\ldots,c^{(k)}` with least nonzero support primes `q_1<\cdots<q_k`, choose

\[
N_{k+1}>q_k
\]

large enough for the tail construction and take a nonzero `c^{(k+1)}` supported on `p\ge N_{k+1}`. Its least nonzero prime `q_{k+1}` then satisfies `q_{k+1}>q_k`.

The resulting vectors are linearly independent. In a finite relation

\[
\sum_{k=1}^r a_kc^{(k)}=0,
\tag{5}
\]

the `q_1` coordinate receives no contribution from `c^{(k)}` for `k>1`, so `a_1=0`. Repeating at `q_2,q_3,\ldots` forces every `a_k=0`. Hence

\[
\boxed{\dim\mathcal N_S=\infty.}
\tag{6}
\]

This uses no asymptotic estimate and no analytic continuation of an Euler product. The analytic input is exactly the tail-supported zero-set theorem already imported in `PL-355`; the infinite-dimensional conclusion is elementary linear algebra plus the well ordering of the prime support.

## 2. Finite homogeneous linear repairs cannot restore rigidity

Let

\[
L=(L_1,\ldots,L_m):\mathcal N_S\to\mathbb C^m.
\tag{7}
\]

Since the range is finite-dimensional while `\mathcal N_S` is infinite-dimensional,

\[
\ker L
=
\mathcal N_S\cap\bigcap_{r=1}^m\ker L_r
\]

has finite codimension at most `m` inside `\mathcal N_S` and is therefore infinite-dimensional. This proves (3).

Continuity is not needed for the algebraic dimension argument once the functionals are defined on all of `\mathcal N_S`; boundedness is stated in the main claim because it covers the natural coefficient constraints native to the Hilbert completion and avoids pathologies of discontinuous everywhere-defined functionals. In particular, any finite set of constraints of the form

\[
\langle c,w_r\rangle_{\ell^2}=0,
\qquad w_r\in\ell^2(\mathcal P),
\tag{8}
\]

still leaves infinitely many nonzero prime-supported series vanishing on the same stack `S`.

Finite coordinate constraints are even more transparent. Given finitely many primes `P_0`, choose the Seip tail cutoff above `\max P_0`; then one obtains a nonzero zero-stack function satisfying

\[
c_p=0\qquad(p\in P_0).
\tag{9}
\]

So no finite collection of low-prime exclusions, finite orthogonality conditions, or other homogeneous bounded coefficient laws can recover the finite-support collapse of `PL-354`.

## 3. Relation to the live Prime-Lattice frontier

`PL-354` and `PL-355` isolate a sharp topology change:

\[
\text{finite prime support}
\quad\Longrightarrow\quad
\text{every infinite distinct real evaluation stack is fatal},
\]

whereas

\[
\ell^2(\mathcal P)\text{ completion}
\quad\Longrightarrow\quad
\text{Blaschke stacks at the }1/2\text{ boundary have a large nullspace}.
\]

The present finding shows that this is not a one-vector accident. The nullspace is sufficiently large to absorb every finite homogeneous continuous coefficient repair. Therefore a source-selected family cannot escape the flexibility exposed by `PL-355` merely by adding finitely many Hilbert-visible arithmetic moments or orthogonality conditions.

For the RH-directed program, a surviving coupling must be essentially stronger: an infinite closed relation with genuinely nontrivial range, a nonlinear or positivity constraint, cross-degree/Euler-product compatibility, target-relative Nyman/Weil structure, cross-aperture coupling, or another source-forced condition not reducible to finite scalar coefficient equations. This narrows the `PL-353`--`PL-355` frontier without turning the zero-set construction itself into an RH mechanism.

## 4. Prior-art and novelty audit

The analytic input is classical prior art: Kristian Seip, *Zeros of functions in Hilbert spaces of Dirichlet series*, Math. Z. **274** (2013), 1327--1339, arXiv:1206.2815. Seip proves the relevant zero-set theorem for `\mathscr D_\infty`; the proof uses arbitrarily far tail approximants, and `PL-355` already audited the `\alpha=\infty`, no-constant, prime-supported specialization needed here. Seip also explicitly emphasizes the local zero-set flexibility of Hilbert spaces of Dirichlet series near `Re s=1/2`.

A targeted literature audit on 18 September 2026 searched Seip's zero-set theorem together with tail support, vanishing subspaces, infinite-dimensional kernels, finite-codimension constraints, and prime-supported Dirichlet series. It found the classical Seip theorem and later extensions of its zero-set framework, but no reason to treat the elementary infinite-dimensional corollary (6) or the finite-codimension consequence (3) as a new theorem of independent priority. **No novelty claim is made.** The durable content is the route restriction relative to the current Prime-Lattice program: finite homogeneous coefficient repair cannot undo the completed boundary-zero flexibility.

The result is also deliberately narrower than an interpolation theorem. It does not assert arbitrary prescribed coefficient data simultaneously with the zeros; it only uses the existence of arbitrarily far tail-supported nonzero solutions to create an infinite-dimensional common vanishing subspace.

## 5. Adversarial boundaries

1. **Only finite homogeneous linear constraints are ruled out.** An infinite family of bounded linear constraints can have trivial intersection with `\mathcal N_S`; affine normalization constraints need a separate solvability argument; nonlinear constraints and positivity cones are outside (3).

2. **The tail theorem is the crucial analytic input.** Mere existence of one zero-set function would not imply (6). The argument depends on the stronger fact, audited in `PL-355`, that the same zero stack can be realized with support beginning beyond arbitrarily large cutoffs.

3. **No norm-uniform family is produced.** The construction gives linear independence, not frame bounds, Riesz bounds, stable interpolation constants, or uniform control of `\|c^{(k)}\|_2` as the tail moves outward.

4. **The allowed zero stacks remain boundary Blaschke stacks.** The least-prime argument in `PL-355` still forbids zeros escaping to `+\infty`, and holomorphy forbids interior accumulation. Nothing here transports a formal Euler-product identity through `Re s=1` or constrains the actual Riemann zero divisor.

5. **Changing the ambient topology can change the conclusion.** A coefficient condition that is not a finite bounded functional on native `\ell^2(\mathcal P)` may become decisive in a Mellin, Nyman, de Branges, graph, or other target-relative topology. The finding rules out a specific repair of the `PL-355` completion, not those geometries.

## Audit / falsification test

The claim would fail if the tail-supported specialization used in `PL-355` were false: specifically, if Seip's `\alpha=\infty` theorem produced a prime-supported zero-set function only for one fixed low-frequency support and did not permit the same `S` to be realized beyond arbitrarily large cutoffs. Subject to that already-audited tail statement, the remaining proof reduces to the triangular support construction and finite-dimensional rank-nullity and is exact.