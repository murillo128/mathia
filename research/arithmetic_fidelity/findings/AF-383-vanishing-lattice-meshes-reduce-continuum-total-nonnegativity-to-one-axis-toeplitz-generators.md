# AF-383 — Vanishing lattice meshes reduce continuum total nonnegativity to one-axis Toeplitz generators

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `POLYA-FREQUENCY` · `TOEPLITZ` · `LOCAL-TO-GLOBAL` · `CERTIFICATE-COMPRESSION` · `NO-NOVELTY-CLAIM`

## Claim

AF-381 shows that a continuous translation kernel is determined, for total-nonnegativity purposes, by all minors on any two-sided sampling set with sufficiently dense finite patterns. AF-382 then compresses the order-two prime-log certificate all the way to adjacent rectangles. At arbitrary determinant order there is a different exact spatial compression: **on shrinking uniform lattices, one may fix one entire row tuple to a single consecutive stencil and retain only arbitrary column tuples.**

Let

\[
K_f(u,x)=f(u-x),\qquad f:\mathbb R\to\mathbb R
\]

with `f` continuous, and let `h_m>0` satisfy

\[
h_m\longrightarrow0.
\tag{1}
\]

Fix `r\in\mathbb N`. Then the following are equivalent:

1. `K_f` is totally nonnegative through order `r` on `\mathbb R\times\mathbb R`;
2. for every `m`, every `1\le k\le r`, and every increasing integer tuple
   \[
   n_1<\cdots<n_k,
   \]
   the single-row-stencil determinant
   \[
   G_{k,h_m}(n_1,\ldots,n_k)
   :=
   \det\!\left(
   f\!\left((a-n_b)h_m\right)
   \right)_{\substack{a=0,\ldots,k-1\\ b=1,\ldots,k}}
   \ge0.
   \tag{2}
   \]

Consequently `K_f` is Pólya-frequency / totally nonnegative of all orders if and only if `(2)` holds for every finite `k` and every mesh in any one vanishing sequence `(h_m)`.

The compression is exact but asymmetric. At each fixed order and mesh, arbitrary row placements are dispensable: the canonical stencil

\[
0,h_m,2h_m,\ldots,(k-1)h_m
\tag{3}
\]

suffices. **Arbitrary column patterns remain load-bearing in this theorem.** Thus the huge two-tuple family of translation minors factors into three resources with different status:

- determinant order must remain unbounded on the unrestricted Pólya-frequency class, by AF-372;
- row-placement complexity can be collapsed to one consecutive `k`-row stencil, by the Toeplitz minor decomposition used here;
- continuum placement is recovered from a one-parameter family of lattice scales tending to zero.

This is a stronger higher-order spatial reduction than AF-381, but unlike AF-382 it does not reduce both row and column locations to nearest-neighbor data.

## Fixed-mesh Toeplitz reduction

Fix a mesh `h>0` and form the bi-infinite Toeplitz array

\[
A^{(h)}_{ij}=f((i-j)h),\qquad i,j\in\mathbb Z.
\tag{4}
\]

Grussler and Damm prove a row-consecutive minor decomposition for Hankel matrices: every order-`k` minor is a nonnegative integer linear combination of order-`k` minors with one consecutive row block and arbitrary columns. Their Theorem 2 gives the explicit coefficients as Littlewood--Richardson coefficients. Reversing column order converts Hankel matrices to Toeplitz matrices; the same reversal sign `(-1)^{k(k-1)/2}` occurs on both the target minor and every generator minor, so it cancels. Their Toeplitz Corollary 5 records the resulting fixed-order sign-consistency reduction.

Therefore every finite order-`k` minor of a Toeplitz matrix can be written in the form

\[
\Delta_{I,J}
=
\sum_\nu c_\nu\,\Delta^{\mathrm{consec}}_\nu,
\qquad c_\nu\in\mathbb Z_{\ge0},
\tag{5}
\]

where each generator on the right has `k` consecutive rows and an arbitrary increasing `k`-tuple of columns in a suitable reshaped Toeplitz block.

For `(4)`, translation invariance removes even the starting location of the consecutive row block. Indeed a generator with rows

\[
s,s+1,\ldots,s+k-1
\]

and columns `j_1<\cdots<j_k` has entries

\[
f((s+a-j_b)h)
=
f((a-(j_b-s))h),
\tag{6}
\]

so it is exactly a determinant of the form `(2)` after shifting all column indices by `s`.

Assume `(2)` at this fixed mesh. Then every generator in `(5)` is nonnegative, hence every finite Toeplitz order-`k` minor is nonnegative. The argument applies to the bi-infinite array because any finite row/column configuration can be translated by a common integer until all indices lie in the one-sided finite/operator setting of the cited theorem, without changing any entry difference.

Thus for each fixed `h_m`, condition `(2)` implies

\[
\det\bigl(f((i_a-j_b)h_m)\bigr)_{a,b=1}^k\ge0
\tag{7}
\]

for **all** increasing integer row and column tuples and every `k\le r`.

The reverse fixed-mesh implication is immediate, since the stencil minors are members of the full sampled family.

## Vanishing mesh closes the continuum

Now assume `(2)` for every `h_m` in `(1)`. Fix arbitrary increasing real tuples

\[
u_1<\cdots<u_k,
\qquad
x_1<\cdots<x_k,
\qquad k\le r.
\tag{8}
\]

For each sufficiently large `m`, choose increasing integer tuples

\[
i_1^{(m)}<\cdots<i_k^{(m)},
\qquad
j_1^{(m)}<\cdots<j_k^{(m)}
\]

such that

\[
i_a^{(m)}h_m\to u_a,
\qquad
j_b^{(m)}h_m\to x_b.
\tag{9}
\]

This is possible because `h_m\to0`; once the mesh is smaller than half the minimum gap in each target tuple, ordinary rounding can be chosen without changing order.

By the fixed-mesh result, each sampled determinant

\[
D_m=
\det\!\left(
 f\!\left((i_a^{(m)}-j_b^{(m)})h_m\right)
\right)_{a,b=1}^k
\tag{10}
\]

is nonnegative. Continuity of `f` gives entrywise convergence to

\[
\bigl(f(u_a-x_b)\bigr)_{a,b=1}^k,
\]

and continuity of the determinant therefore gives

\[
\det\bigl(f(u_a-x_b)\bigr)_{a,b=1}^k
=
\lim_{m\to\infty}D_m
\ge0.
\tag{11}
\]

The tuples in `(8)` were arbitrary, so `K_f\in TN_r`. Conversely, global `TN_r` trivially implies every stencil inequality `(2)`. This proves the equivalence.

Notice that the closure step needs no positivity of the entries, logarithm, differentiability, analyticity, or control of zero patterns. Those were relevant to AF-382's stronger two-axis nearest-neighbor reduction; here the algebraic Toeplitz decomposition carries the higher-order spatial reduction, while continuity is used only to pass from shrinking grids to the continuum.

## Compression accounting

The result separates **placement complexity** from **relational arity** more sharply than the previous prime-sampling findings.

At order `k`, a generic translation-minor test appears to require two arbitrary ordered `k`-tuples, hence roughly `2k-1` continuous relative coordinates after quotienting common translation. On each lattice scale, `(2)` fixes the row tuple completely. The surviving generator has only the arbitrary column pattern. The row geometry has not been approximated or statistically summarized; it has been eliminated exactly by a positive linear generation theorem in the Toeplitz category.

That exactness is important for Arithmetic Fidelity. A family of tests can be much smaller than the full target family without losing target information when the omitted relations lie in the **positive cone generated by retained relations**. Equation `(5)` is such a certificate factorization: a negative omitted minor cannot hide behind nonnegative retained generator minors because all combination coefficients are nonnegative.

AF-372 shows why this should not be confused with finite-order sufficiency. Even after the spatial reduction, every finite cutoff `r` still admits kernels in `TN_r\setminus TN_{r+1}`. The load-bearing information is therefore not the combinatorial abundance of row placements. On the unrestricted class it is the need to retain arbitrarily high determinant order.

The vanishing mesh is a separate resource. A single fixed lattice generally does not determine an arbitrary continuous translation profile between lattice points. The family `h_m\to0` repairs exactly that geometric loss. Thus the certificate has a clean three-stage structure:

\[
\text{one-axis Toeplitz generators at each mesh}
\Longrightarrow
\text{all lattice minors}
\Longrightarrow
\text{all continuum minors}.
\tag{12}
\]

The first arrow is algebraic and order-by-order; the second is topological and uses shrinking mesh.

## Why fully consecutive higher-order minors are a different claim

The retained family in `(2)` must not be confused with ordinary **fully consecutive** Toeplitz minors, where both the rows and columns form consecutive blocks. Grussler--Damm explicitly show that fixed-order sign consistency cannot in general be reduced further to consecutive `k`-minors alone: their Example 3 already gives a `k=2` Hankel witness in which consecutive minors have the required strict sign while nonconsecutive minors do not. Column reversal transports the same warning to Toeplitz sign-consistency questions.

Additional hypotheses can change this boundary. Their Proposition 2, building on classical total-positivity recognition, shows that strict positivity of the lower-order initial minors plus nonnegativity of all consecutive order-`k` minors suffices for `k`-positivity of a finite matrix. But that is a **conditional strict-interior certificate**. The Pólya-frequency target is total nonnegativity, allows vanishing minors and support boundaries, and cannot silently assume those lower-order strictness hypotheses.

So AF-382's two-axis adjacency collapse at order two is genuinely special: positivity of the entries permits a logarithmic Monge telescoping identity. AF-383 gives the robust higher-order replacement currently justified by the literature: one consecutive row stencil, but arbitrary columns.

## Riemann-facing consequence

For the Schoenberg/Gröchenig Pólya-frequency formulation reviewed in AF-371, AF-383 gives a target-equivalent continuum certificate that is much smaller in spatial placement than the definition. In principle one may choose, for example, `h_m=1/m` and ask only for the determinants `(2)` at every finite order. If they all hold, the full translation kernel is Pólya-frequency; if the full kernel is Pólya-frequency, they all hold.

This is **not** an arithmetic mechanism for proving the inequalities. The mesh can be completely nonarithmetic, so the reduction carries no rational-prime discrimination by itself. Its value is diagnostic: a source-specific argument does not need to prove every possible row placement independently. It may target a canonical shrinking row stencil while preserving arbitrary column relations and unbounded determinant order.

A recent Riemann-adjacent result illustrates why the distinction between generator families matters. Michalowski proves eventual positivity of a family of **consecutive** Toeplitz minors of the normalized Riemann `xi` coefficient sequence for `k` beyond an explicit cubic scale in the determinant order. That result is in a different discrete coefficient model and explicitly does not prove RH. AF-383 explains a structural reason not to overread such consecutive-minor positivity: even in Toeplitz settings, a target-complete fixed-order generator generally retains arbitrary column selections, not merely consecutive square blocks, unless extra strictness or source rigidity is proved.

The live source-side question is therefore sharper. Instead of asking whether prime arithmetic can somehow force the full continuum determinant family directly, ask whether the RH-facing source structure can force a **target-complete generator family** such as `(2)`, or can justify additional hypotheses that compress the arbitrary-column requirement further. Any such reduction must still confront AF-372's unbounded-order barrier unless the arithmetic source class itself supplies a theorem collapsing determinant order.

## Prior-art and novelty audit

- Christian Grussler and Tobias Damm, **“Efficient `k`-Sign Consistency Verification of Hankel Matrices via Schur Polynomials,”** arXiv:`2602.08122` (8 February 2026). Role: primary source for the nonnegative Littlewood--Richardson decomposition of arbitrary fixed-order Hankel minors into row-consecutive generators, its Toeplitz extension by column reversal, the infinite-operator equivalence, and the warning that ordinary consecutive minors alone do not certify fixed-order sign consistency in general.
- Shaun M. Fallat and Charles R. Johnson, ***Totally Nonnegative Matrices***, Princeton University Press (2011). Role: classical modern reference for total-positive/nonnegative matrix recognition and the initial/consecutive-minor criteria underlying the strict lower-order hypotheses used in Grussler--Damm's Proposition 2.
- I. J. Schoenberg and A. M. Whitney, **“On Pólya Frequency Functions. III. The Positivity of Translation Determinants With an Application to the Interpolation Problem by Spline Curves,”** *Transactions of the American Mathematical Society* **74** (1953), 246--259, DOI `10.2307/1990881`. Role: classical translation-determinant target class.
- Wojciech Michalowski, **“An explicit uniform cubic wedge for consecutive Toeplitz minors of the Riemann xi coefficients,”** arXiv:`2607.16795` (18 July 2026). Role: recent Riemann-facing consecutive-minor result illustrating the practical importance of distinguishing fully consecutive minors from a target-complete Toeplitz generator family; the paper explicitly limits its result to a tail regime and makes no RH claim.

The fixed-mesh row-consecutive decomposition is Grussler--Damm prior art, and the continuum passage through `h_m\to0` is an elementary closure argument. A focused search did not identify this exact shrinking-lattice formulation as a named theorem, but **no novelty is claimed**. The durable Arithmetic Fidelity contribution is the resource accounting: higher-order translation total positivity admits a large exact compression in spatial placement while retaining arbitrary-column relations, shrinking scale, and unbounded determinant order.

## Boundaries and falsification checks

Continuity of `f` is load-bearing only for the continuum closure. Without regularity between lattice points, even total nonnegativity on every member of a sparse family of grids need not determine unsampled values unless the union of tested configurations is itself determining in the relevant topology.

The theorem requires a sequence of meshes tending to zero. No claim is made that one fixed lattice is target-faithful for an unrestricted continuous profile.

The generator condition retains **all arbitrary integer column tuples** at each order and mesh. Replacing them by consecutive columns is a strictly stronger compression and is not justified by the argument. The recent row-consecutive decomposition should therefore not be summarized as “consecutive minors suffice.”

The theorem is source-independent. It applies equally to arithmetic and nonarithmetic continuous translation profiles and therefore supplies target compression, not arithmetic discrimination.

Finally, the all-order Pólya-frequency consequence still requires every finite determinant order. AF-372 gives exact finite-order false positives, so neither shrinking mesh nor row-stencil compression removes the unbounded-arity obstruction on the unrestricted class.