# AF-443 — Finite moment families cannot protect remote marks against equal latent support dimension

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `FINITE-MOMENT-NONIDENTIFIABILITY`, `MINIMAL-LIFT-OBSTRUCTION`, `CLASSICAL-GENERALIZED-VANDERMONDE/IFT`, `NO-NOVELTY-CLAIM`

## Claim

AF-442 shows that one high reciprocal-square moment cannot protect a later binary shell mark when one earlier support coordinate is latent inside its retained shell/cell. Adding finitely many independent moments removes that particular one-coordinate compensation only if the admissible latent support freedom is correspondingly smaller.

Fix

\[
0<\rho<\frac12,
\]

and distinct positive moment orders

\[
1\le n_1<n_2<\cdots<n_K.
\]

Choose fixed earlier shells

\[
1\le j_1<j_2<\cdots<j_K
\]

and let

\[
I_j=[j-\rho,j+\rho].
\]

For a support sequence `r=(r_j)` with `r_j\in I_j` and binary marks `a_j\in\{0,1\}`, observe only the shell labels together with the `K` moments

\[
M_{n_\ell}(r,a)
=\sum_{j\ge1}a_j r_j^{-2n_\ell},
\qquad \ell=1,\ldots,K.
\tag{1}
\]

Then there exists `m_0>j_K` such that for every target shell `m\ge m_0` one can find two admissible configurations `(r,a)` and `(\widetilde r,b)` satisfying:

- `a_{j_i}=b_{j_i}=1` for `i=1,\ldots,K`;
- `a_m=0` and `b_m=1`;
- all other marks agree;
- all support coordinates agree except possibly the `K` earlier coordinates `j_1,\ldots,j_K`;
- both realized supports remain inside the same retained shell cells, so the shell/cell provenance is identical;
- nevertheless

\[
\boxed{
M_{n_\ell}(r,a)=M_{n_\ell}(\widetilde r,b)
\qquad(\ell=1,\ldots,K).
}
\tag{2}
\]

Moreover the required earlier support displacements tend to zero as `m\to\infty`. If the first moment order is `n_1`, then

\[
\boxed{
\max_i|\widetilde r_{j_i}-j_i|=O(m^{-2n_1}).
}
\tag{3}
\]

Thus **no fixed finite family of reciprocal-power moments can uniformly protect arbitrarily remote discrete marks on a source class that retains equally many independently movable earlier support coordinates only up to cell identity**.

This is a source-dimension obstruction, not a claim that several moments never help. If the admissible support deformation is lower-dimensional than the retained moment family, or if relational data ties the latent coordinates together, the compensation mechanism below can disappear. Likewise, the theorem does not address a number of moments that grows with the target depth.

## Local moment-map derivation

Write

\[
x_i=r_{j_i}^{-2},
\qquad
x_i^0=j_i^{-2},
\qquad
1\le i\le K,
\]

and define the local moment map

\[
\Phi:(0,\infty)^K\to\mathbb R^K,
\qquad
\Phi_\ell(x_1,\ldots,x_K)
=\sum_{i=1}^K x_i^{n_\ell}.
\tag{4}
\]

Its Jacobian at the nominal reciprocal-square skeleton is

\[
J_{\ell i}
=n_\ell(x_i^0)^{n_\ell-1}.
\tag{5}
\]

Factor the positive row scalars `n_\ell`. The remaining matrix is the generalized Vandermonde matrix

\[
V_{\ell i}=(x_i^0)^{e_\ell},
\qquad
 e_\ell=n_\ell-1,
\tag{6}
\]

with strictly increasing nonnegative integer exponents

\[
0\le e_1<e_2<\cdots<e_K
\]

and distinct positive nodes `x_i^0`.

After ordering the nodes increasingly, `V` is strictly totally positive; equivalently its determinant is a classical Vandermonde determinant times a positive Schur polynomial. Hence

\[
\det J\ne0.
\tag{7}
\]

By the inverse-function theorem there are neighborhoods `U` of `x^0=(x_i^0)` and `W` of `\Phi(x^0)` for which

\[
\Phi:U\to W
\]

is a diffeomorphism.

Choose `U` small enough that every `x\in U`, after returning to support coordinates

\[
r_{j_i}=x_i^{-1/2},
\]

lies inside the same shell interval `I_{j_i}`. This is possible because each nominal point `j_i` lies in the interior of its cell and `x\mapsto x^{-1/2}` is continuous on the positive axis.

Thus the `K` earlier latent support coordinates provide exactly `K` independent local directions whose effect on the retained `K` moments is nonsingular.

## Exact compensation of a remote mark

Take the first configuration at the nominal support `r_j=j`. Give the selected earlier shells mark `1`, give target shell `m` mark `0`, and fix arbitrary common marks and support coordinates elsewhere.

In the second configuration change only the target mark to `1` and allow only the selected earlier support coordinates to move. Put

\[
y=m^{-2}
\]

and

\[
v_m=(y^{n_1},y^{n_2},\ldots,y^{n_K}).
\tag{8}
\]

To keep every retained moment unchanged, the earlier reciprocal-square coordinates must satisfy

\[
\boxed{
\Phi(\widetilde x)=\Phi(x^0)-v_m.
}
\tag{9}
\]

Because `n_1\ge1`, one has

\[
v_m\longrightarrow0
\qquad(m\to\infty).
\]

Therefore `\Phi(x^0)-v_m\in W` for every sufficiently large `m`. The local inverse gives a unique

\[
\widetilde x(m)\in U
\]

satisfying `(9)`. Set

\[
\widetilde r_{j_i}=\widetilde x_i(m)^{-1/2}
\]

and leave all other support coordinates unchanged.

Since `\widetilde x(m)\in U`, all moved support points remain inside their original cells. Equation `(9)` says that their joint decrease in each of the `K` observed moments exactly cancels the contribution of the newly occupied target shell. Every unselected term is identical in the two sources and cancels term by term. This proves `(2)`.

The construction is exact, not asymptotic: largeness of `m` is used only to place the required moment vector inside the local image `W` while keeping the compensating support points inside their prescribed cells.

## Quantitative displacement scale

The local inverse is differentiable at `\Phi(x^0)`. Therefore

\[
\widetilde x(m)-x^0
=-J^{-1}v_m+O(\|v_m\|^2).
\tag{10}
\]

Since `n_1<n_2<\cdots<n_K` and `0<y<1`,

\[
\|v_m\|=O(y^{n_1})=O(m^{-2n_1}).
\tag{11}
\]

Consequently

\[
\max_i|\widetilde x_i(m)-x_i^0|
=O(m^{-2n_1}).
\tag{12}
\]

The derivative of `x\mapsto x^{-1/2}` is finite at each fixed positive `x_i^0`, so `(12)` transfers directly to the support coordinates and proves `(3)`.

The important scale is therefore set by the **lowest retained moment order**, not the highest. Higher moments add independent equations and make the Jacobian square, but a sufficiently remote target contributes a moment vector whose entire norm is already controlled by its lowest-order component. Once the nuisance support dimension matches the number of equations, that small target vector lies inside the locally programmable image of the earlier coordinates.

## Relation to AF-439 through AF-442

AF-439 proves that the first `N` Euler moments have local pole-moving fibers when `N+1` support locations are continuously free. That is a support-identifiability obstruction and does not itself encode a discrete mark change.

AF-440 gives the complementary positive result: on the exact fixed reciprocal-square skeleton, one sufficiently high moment can separate a linearly growing prefix of marks because the reciprocal weights become superincreasing.

AF-441 shows that the positive result survives support jitter when the **realized** support skeleton is retained, while finite moment prefixes become nonidentified when support locations are latent. AF-442 then gives the first mixed support/mark collision: one latent earlier coordinate exactly hides one later mark from one high moment even though shell identity is retained.

The present theorem closes the obvious fixed-finite-dimensional escape from AF-442. Replacing the single scalar moment by `K` independent reciprocal-power moments does not restore uniform remote-mark fidelity when the source class permits `K` independent earlier latent support coordinates. The relevant local accounting is therefore not simply

\[
\text{more moments} \Rightarrow \text{more fidelity},
\]

but rather

\[
\boxed{
\text{measurement rank versus admissible latent-support dimension}.
}
\tag{13}
\]

This is compatible with AF-007's general vertical-rank principle, but it is stronger for the present source because it integrates the local full-rank compensation into an **exact collision between two different discrete target marks** while preserving shell provenance.

## Prior-art and novelty audit

The mathematical ingredients are classical, and no novelty is claimed for them.

Generalized Vandermonde matrices on ordered positive nodes and ordered monomial exponents are a standard totally positive family. James Demmel and Plamen Koev, **“The Accurate and Efficient Solution of a Totally Positive Generalized Vandermonde Linear System,”** *SIAM Journal on Matrix Analysis and Applications* 27(1), 142–152 (2005), DOI `10.1137/S0895479804440335`, develops the total-positivity and Schur-function structure of these systems. The nonsingularity used in `(7)` is a classical consequence of that theory.

The inverse-function theorem and the principle that a nonsingular moment Jacobian permits local programming of nearby moment vectors are standard differential topology. In finite atomic moment inversion this sits inside classical Prony geometry. Dmitry Batenkov, Gil Goldman, Yehonatan Salman, and Yosef Yomdin, **“Algebraic Geometry of Error Amplification: the Prony leaves,”** arXiv:`1702.05338` (2017), studies equi-moment surfaces and Prony foliations in the node/amplitude parameter space.

AF-439 and AF-442 already place the neighboring underdetermined and one-moment compensation mechanisms inside that classical moment/Prony prior art. The Arithmetic Fidelity contribution recorded here is the exact boundary needed by the current minimal-lift question: for the reciprocal-square shell model with retained cell provenance and a discrete occupancy discriminator, **every fixed `K`-moment observation can still be made target-impure by `K` independently latent earlier support coordinates**, with an exact remote-mark collision whose required support movement tends to zero polynomially in the target shell.

No novelty is claimed for generalized Vandermonde nonsingularity, total positivity, the inverse-function theorem, finite-dimensional local identifiability, or Prony systems.

## Boundaries and falsification checks

- The theorem requires `K` independently movable earlier support coordinates for `K` retained moments. It does not show failure when the admissible support deformation has smaller effective dimension or is constrained by a source-derived law.
- The result uses a **fixed finite** moment family. It does not rule out a number of observations that increases with target depth, nor an infinite exact moment sequence.
- The target shell must be sufficiently remote. For a fixed nearby target, the required moment perturbation need not lie inside the chosen local image while respecting the prescribed cell radius.
- The cells contain two-sided neighborhoods of the nominal support points. One-sided admissibility constraints require an additional cone/sign analysis because the local inverse may point outside the allowed tangent cone.
- The selected earlier marks are nonzero; the binary construction uses mark `1`. If fewer than `K` earlier occupied coordinates are allowed to move, the square compensation map above is unavailable.
- The theorem concerns the declared reciprocal-power moments and cell labels. A richer observation carrying relational support data, realized coordinates, a recurrence, or another independent constraint can remove the collision.
- The generalized Vandermonde determinant is nonzero only because the moment orders are distinct and the selected support nodes are distinct and positive. Repeated measurements do not increase the local rank.
- The result is exact identifiability failure, not merely poor numerical conditioning. The displacement estimate only quantifies how deeply inside an arbitrarily narrow cell the exact collision can eventually fit.
- Nothing here distinguishes rational primes, constrains the Riemann zero divisor, or implies RH. It isolates the amount of source-side provenance required before finite Euler-style moment compression can be credited with preserving a remote discrete discriminator.

A direct falsification would require fixed admissible data satisfying the hypotheses and arbitrarily large `m` for which `(9)` has no solution inside the selected cells. The generalized Vandermonde Jacobian is nonsingular, so the inverse-function theorem supplies an open neighborhood of exactly reachable moment vectors around `\Phi(x^0)`; `v_m\to0` places `(9)` in that neighborhood for all sufficiently large `m`.

## Consequence for the research line

The minimal-lift frontier after AF-442 should no longer ask merely whether **several** moments repair one latent support coordinate. They can, but that does not scale to a source class whose independent latent dimension grows with the amount of retained data.

A constructive lift must instead control the ratio between observation rank and admissible nuisance dimension. Three genuinely different escape routes remain:

- retain enough realized support/provenance to remove nuisance coordinates from the fiber;
- impose a canonical low-dimensional deformation law so that additional moments eventually overdetermine the latent motion;
- retain relational support information from which the realized skeleton is itself recoverable.

For any proposed finite-dimensional lift, the first decisive test should be whether its retained observations have a **target-pure fiber** after all source-side latent degrees of freedom are counted. Conditioning and reconstruction algorithms become relevant only after that identifiability gate passes.