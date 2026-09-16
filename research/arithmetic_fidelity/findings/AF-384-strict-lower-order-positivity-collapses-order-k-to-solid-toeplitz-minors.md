# AF-384 — Strict lower-order positivity collapses continuum order-k fidelity to solid Toeplitz minors

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `POLYA-FREQUENCY` · `TOEPLITZ` · `CERTIFICATE-COMPRESSION` · `STRICT-INTERIOR` · `NO-NOVELTY-CLAIM`

## Claim

AF-383 showed that, on shrinking uniform lattices, continuum total nonnegativity through fixed order can be certified by one consecutive row stencil together with **arbitrary** column tuples. Its main unresolved spatial cost was therefore the arbitrary-column family. Classical finite-matrix recognition shows exactly when that remaining geometry disappears.

Let

\[
K_f(u,x)=f(u-x),\qquad f:\mathbb R\to\mathbb R
\]

with `f` continuous. Fix `k\ge2`, and assume that `K_f` is **strictly totally positive through order `k-1`**:

\[
\det\bigl(f(u_a-x_b)\bigr)_{a,b=1}^j>0
\tag{1}
\]

for every `1\le j<k` and every strictly increasing real tuples

\[
u_1<\cdots<u_j,\qquad x_1<\cdots<x_j.
\]

Let `h_m>0` with `h_m\to0`. For `d\in\mathbb Z`, define the fully consecutive / solid Toeplitz determinant

\[
C_{k,h_m}(d)
:=
\det\!\left(f\!\left((d+a-b)h_m\right)\right)_{a,b=0}^{k-1}.
\tag{2}
\]

Then the following are equivalent:

1. `K_f` is totally nonnegative through order `k` on `\mathbb R\times\mathbb R`;
2. for every `m` and every `d\in\mathbb Z`,
   \[
   C_{k,h_m}(d)\ge0.
   \tag{3}
   \]

Thus, **conditional on strict positivity of all lower orders, the arbitrary-column generator family left by AF-383 collapses at order `k` to one integer offset per mesh.** At fixed `h_m`, both the row and column shapes are the single consecutive stencil

\[
0,h_m,\ldots,(k-1)h_m,
\]

and translation invariance leaves only their relative offset `d`.

This is an exact source-class/resource trade. The compression is unavailable on the unrestricted totally-nonnegative class: the lower-order strictness in `(1)` is the resource that removes the arbitrary-column degree of freedom.

## Fixed-mesh derivation

Fix one mesh `h>0` and form the bi-infinite Toeplitz array

\[
A^{(h)}_{ij}=f((i-j)h),\qquad i,j\in\mathbb Z.
\tag{4}
\]

Grussler and Damm's Proposition 2 gives the relevant finite-matrix recognition criterion. For a finite matrix `X` and fixed order `k`, if

- every row-initial and column-initial minor of orders `1,\ldots,k-1` is strictly positive; and
- every consecutive `k`-minor is nonnegative,

then `X` is `k`-positive: every minor of every order up to `k` is nonnegative, while the lower-order minors are positive. Their strict version replaces nonnegativity of the consecutive `k`-minors by positivity.

Now take an arbitrary order-`k` lattice minor of `(4)`, with increasing integer row tuple `I` and column tuple `J`. Choose a finite rectangular consecutive-index block `X` of `(4)` large enough to contain all rows in `I` and all columns in `J`.

The lower-order initial-minor hypotheses of Proposition 2 hold automatically for `X`: each such minor is a sampled minor of the continuum kernel `K_f`, hence is strictly positive by `(1)`.

Every consecutive `k`-minor of `X` uses consecutive lattice rows and consecutive lattice columns. If their starting indices are `s` and `t`, its entries are

\[
f\bigl((s+a-t-b)h\bigr)
=
f\bigl((d+a-b)h\bigr),
\qquad d=s-t,
\tag{5}
\]

so its determinant is exactly `C_{k,h}(d)`. Therefore `(3)` supplies the second hypothesis of Proposition 2 for every finite block `X`.

It follows that `X` is `k`-positive, hence the originally chosen arbitrary order-`k` lattice minor is nonnegative. Since `I,J` were arbitrary,

\[
\det\bigl(f((i_a-j_b)h)\bigr)_{a,b=1}^k\ge0
\tag{6}
\]

for all increasing integer tuples. In other words, at a fixed mesh, strict lower-order positivity turns the one-parameter solid-minor test `(3)` into **all** order-`k` lattice inequalities.

The converse fixed-mesh implication is immediate if the full lattice array is `k`-positive, because every `C_{k,h}(d)` is one of its minors.

## Vanishing mesh closes the continuum

Apply the fixed-mesh argument to every `h_m`. For arbitrary increasing real tuples

\[
u_1<\cdots<u_k,\qquad x_1<\cdots<x_k,
\tag{7}
\]

choose increasing integer tuples `i^{(m)}` and `j^{(m)}` such that

\[
i_a^{(m)}h_m\to u_a,
\qquad
j_b^{(m)}h_m\to x_b.
\tag{8}
\]

For sufficiently large `m` this can be done by ordinary rounding while preserving order. The corresponding lattice determinants are nonnegative by `(6)`. Continuity of `f` and of the determinant gives

\[
\det\bigl(f(u_a-x_b)\bigr)_{a,b=1}^k
=
\lim_{m\to\infty}
\det\!\left(
 f\!\left((i_a^{(m)}-j_b^{(m)})h_m\right)
\right)_{a,b=1}^k
\ge0.
\tag{9}
\]

All lower-order continuum minors are already strictly positive by `(1)`, so `(9)` proves total nonnegativity through order `k`. The reverse implication to `(3)` is trivial. This proves the equivalence.

Notice the asymmetry between strictness and closure. If every sampled `C_{k,h_m}(d)` is **strictly** positive, Proposition 2 makes every sampled lattice `k`-minor strictly positive, but the limit in `(9)` can still be zero. A vanishing-grid argument alone therefore yields continuum `TN_k`, not continuum `STP_k`, unless an additional quantitative lower-margin condition is supplied.

## Certificate-complexity consequence

AF-383 and AF-384 together give a clean two-regime classification of the spatial information required at fixed determinant order.

On the unrestricted continuous `TN` class, AF-383 removes arbitrary row placement but retains arbitrary column geometry. A target-complete sampled generator has the form

\[
\det\!\left(f((a-n_b)h_m)\right)_{a=0,\ldots,k-1;\,b=1,\ldots,k},
\tag{10}
\]

with arbitrary increasing `n_1<\cdots<n_k`.

On the strict lower-order interior `(1)`, the classical recognition criterion compresses `(10)` further to `(2)`: all column gaps disappear and only one relative offset `d` survives at each mesh.

So **extra source rigidity buys exact certificate compression**. This is not merely a smaller sufficient test chosen ad hoc; the omitted order-`k` placements are forced by a theorem once the retained lower-order strictness is available. In Arithmetic Fidelity terms, lower-order strict positivity is side information that shrinks the target-faithful observation family.

The result also identifies why AF-383's arbitrary-column warning was necessary. Grussler--Damm's counterexamples show that consecutive fixed-order minors alone do not control arbitrary minors without additional assumptions. Proposition 2 pinpoints a sufficient missing resource: strict positivity of the lower-order initial minors. Condition `(1)` supplies that resource uniformly to every finite lattice block.

## Pólya-frequency and Riemann-facing boundary

For a Pólya-frequency / translation-total-nonnegativity target, this theorem does **not** justify replacing the full determinant family by solid minors unconditionally. Total nonnegativity permits lower-order zero minors and support-boundary degeneracies; Proposition 2 deliberately assumes strict lower-order initial minors. The extra compression is therefore valid only after an independent argument places the source in the strict lower-order interior.

This matters for Riemann-facing uses of total positivity. AF-371 identifies translation total positivity as an exact classical target for the Laguerre--Pólya / real-zero discriminator, while AF-372 shows that no fixed determinant-order cutoff suffices on the unrestricted Pólya-frequency class. AF-384 changes only the **placement** cost at one fixed order under a strict source hypothesis; it does not remove the need for unbounded order, prove that the Riemann-associated kernel satisfies `(1)`, or supply an arithmetic reason for the solid minors `(3)` to be nonnegative.

It also prevents overreading recent consecutive-Toeplitz-minor results. Positivity of a consecutive-minor family becomes target-complete at the next determinant order only when the required lower-order strictness is independently available in the same matrix/kernel model. A tail theorem for consecutive minors in a different coefficient model does not acquire an RH consequence merely by invoking this criterion.

The resulting source-side question is now sharply conditional: **can an RH-facing arithmetic structure establish strict positivity of the lower-order translation minors and the one-parameter solid order-`k` family without already assuming the target?** If yes, AF-384 removes the arbitrary-column burden at that order. If not, AF-383's larger one-axis generator family remains the target-complete certificate.

## Prior-art and novelty audit

- Christian Grussler and Tobias Damm, **“Efficient `k`-Sign Consistency Verification of Hankel Matrices via Schur Polynomials,”** arXiv:`2602.08122` (8 February 2026), especially Proposition 2. Role: primary source for the finite-matrix criterion used here: positive lower-order row/column initial minors plus nonnegative consecutive order-`k` minors imply `k`-positivity. The paper explicitly presents this as following from established total-positivity recognition results, and extends related structured-minor reductions to Hankel/Toeplitz settings.
- Allan Pinkus, ***Totally Positive Matrices***, Cambridge University Press (2009; online 2010), Chapter 2. Role: classical source for initial/consecutive-minor criteria, Fekete-type recognition, and the crucial difference between strict total positivity and the more delicate totally-nonnegative boundary.
- I. J. Schoenberg and A. M. Whitney, **“On Pólya Frequency Functions. III. The Positivity of Translation Determinants With an Application to the Interpolation Problem by Spline Curves,”** *Transactions of the American Mathematical Society* **74** (1953), 246--259, DOI `10.2307/1990881`. Role: classical translation-determinant target class.
- Wojciech Michalowski, **“An explicit uniform cubic wedge for consecutive Toeplitz minors of the Riemann xi coefficients,”** arXiv:`2607.16795` (18 July 2026). Role: recent Riemann-facing example of a consecutive-minor family; its coefficient model and tail theorem do not establish the strict lower-order translation-kernel hypotheses required here and the paper explicitly makes no RH claim.

The finite recognition theorem is classical/current prior art, and the passage from finite lattice blocks to a continuous translation kernel through `h_m\to0` is an elementary corollary. A focused search did not locate this exact shrinking-lattice formulation as a named theorem, but **no novelty is claimed**. The durable Arithmetic Fidelity result is the resource boundary it exposes: arbitrary-column placement is genuinely necessary in the boundary/nonnegative regime covered by AF-383, yet becomes redundant once strict lower-order positivity is retained as source information.

## Boundaries and falsification checks

The strict lower-order assumption `(1)` is load-bearing. It cannot be replaced in this proof by mere lower-order nonnegativity. The finite recognition theorem itself distinguishes those regimes, and AF-383 records fixed-order consecutive-minor counterexamples without the strict hypothesis.

Condition `(3)` must hold on a sequence of meshes tending to zero to recover an unrestricted continuous profile. A single fixed lattice still leaves between-grid freedom unless additional regularity or a separate uniqueness theorem is supplied.

The theorem compresses **placement**, not determinant order. Even if `(1)` and `(3)` can be verified successively for each `k`, AF-372 remains the reason that an unrestricted all-order Pólya-frequency target cannot be replaced by any one fixed `k`.

No source-identification claim is made. Many different functions can share the same Boolean positivity verdicts. The statement is only target-faithful for the order-`k` total-nonnegativity property inside the declared strict lower-order source class.

Finally, no arithmetic discriminator is created by the theorem. Uniform lattices, the finite recognition criterion, and the closure argument are source-independent. Any Riemann use must still explain why the relevant arithmetic source lies in the strict lower-order class and why its solid minors have the required sign.