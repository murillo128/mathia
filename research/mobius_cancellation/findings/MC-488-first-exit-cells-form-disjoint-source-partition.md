# MC-488 — First-exit cells form a disjoint source partition; common transforms cannot create cross-q dispersion

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-484` replaces the hard pair-sieve mask by an exact Buchstab first-exit sum, while `MC-487` removes the apparent inverse-shift motion by returning each root branch to an intrinsic integer coordinate. The normalized clue then leaves three possible sources of useful `q`-dependence: progression incidence, the nested cutoff `P(q)`, and the exact outer coefficients.

The first two, taken together as the **exact first-exit support**, do not supply an independent source dimension. They form a disjoint partition of the original sieve shell.

Keep the notation

\[
F_h(n)=n(n+h),
\qquad
A_t(n)=\mathbf 1_{(F_h(n),P(t))=1}
\]

from `MC-484`, and for active primes `w\le q<z` define the exact first-exit cell on a source interval `I` by

\[
E_q(I)
:=
\{n\in I:q\mid F_h(n),\ A_q(n)=1\}.
\tag{1}
\]

Then

\[
\boxed{E_q(I)\cap E_r(I)=\varnothing\quad(q\ne r),}
\tag{2}
\]

and pointwise

\[
\boxed{
\mathbf 1_I(n)\bigl(A_w(n)-A_z(n)\bigr)
=
\sum_{w\le q<z}\mathbf 1_{E_q(I)}(n).
}
\tag{3}
\]

Thus on the shell

\[
E(I):=\{n\in I:A_w(n)=1,\ A_z(n)=0\}
\tag{4}
\]

the first-exit prime is the deterministic function

\[
q_*(n)
:=
\min\{q\in[w,z):q\text{ active prime and }q\mid F_h(n)\}.
\tag{5}
\]

There is no independent `(q,n)` source state on the exact Buchstab support: the map

\[
(q,n)\longmapsto n,
\qquad n\in E_q(I),
\tag{6}
\]

is a bijection from the disjoint union of first-exit cells onto `E(I)`.

This has an immediate Hilbert-space consequence. Let

\[
f_q(n)=c_q(n)K_h(n)\mathbf 1_{E_q(I)}(n),
\qquad
K_h(n)=\chi(n+h)\overline{\chi(n)},
\tag{7}
\]

for arbitrary coefficients `c_q(n)`. Then

\[
\boxed{\langle f_q,f_r\rangle_{\ell^2(I)}=0\quad(q\ne r).}
\tag{8}
\]

Hence every **common** isometry or unitary transform `U` on the source coordinate preserves the diagonal row Gram matrix:

\[
\boxed{
\langle Uf_q,Uf_r\rangle
=
\delta_{q,r}\|f_q\|_2^2.
}
\tag{9}
\]

In particular, a common complete Fourier/Parseval transform cannot manufacture an off-diagonal `q`-dispersion term from the normalized exact progression-plus-cutoff supports. If the coefficients are also common, `c_q(n)=c(n)`, then first exit refolds exactly:

\[
\boxed{
\sum_{w\le q<z}\sum_{n\in E_q(I)}c(n)K_h(n)
=
\sum_{n\in I}c(n)K_h(n)\bigl(A_w(n)-A_z(n)\bigr).
}
\tag{10}
\]

With genuinely `q`-dependent coefficients the same statement becomes

\[
\sum_q\sum_{n\in E_q(I)}c_q(n)K_h(n)
=
\sum_{n\in E(I)}c_{q_*(n)}(n)K_h(n).
\tag{11}
\]

So the first-exit label can still matter through the **value of the coefficient attached to the least prime factor**, but it does not add a second independent source coordinate merely by being written as an outer sum.

This closes a specific part of the accepted first-exit clue. The exact normalized progression/cutoff incidence cannot by itself support a new cross-`q` dispersion mechanism under one common source transform. A surviving route must make the first-exit prime enter a genuinely `q`-dependent operator, modulus, completion, reciprocal phase, or outer arithmetic coefficient **before** positive closure. That is precisely the kind of quotient-breaking asymmetry exhibited by the neighboring Pascadi/Yang dispersion template in `MC-456`; it is not supplied by the Buchstab partition itself.

No conductor-power saving, improved bound for `M(x)`, zero-free region, or RH consequence follows.

## 1. Exact disjointness and refolding

Take distinct active primes `q<r` in `[w,z)`. If `n\in E_r(I)`, then `A_r(n)=1`, so no active prime below `r` divides `F_h(n)`. In particular `q\nmid F_h(n)`. Therefore `n\notin E_q(I)`, proving `(2)`.

Now suppose `A_w(n)=1`. If `A_z(n)=1`, no active prime in `[w,z)` divides `F_h(n)`, so the right side of `(3)` vanishes. If `A_z(n)=0`, there is at least one such divisor and its least value `q_*(n)` satisfies `A_{q_*(n)}(n)=1`. Thus exactly the `q=q_*(n)` term on the right side is one. This is the pointwise first-exit proof already underlying Buchstab's identity in `MC-484`; equations `(2)`--`(6)` isolate the additional source-space consequence.

The two roots of

\[
q\mid n(n+h)
\]

cause no ambiguity. When `q\nmid h`, the residue classes `n\equiv0,-h\pmod q` are disjoint branches inside the same cell `E_q`. When `q\mid h`, they coincide and there is only one branch. Across distinct `q`, uniqueness of the least active prime divisor remains unchanged.

Therefore the apparently two-index source family is a partitioned presentation of a one-index source shell. Equation `(10)` is just `(3)` multiplied by the fixed kernel `c(n)K_h(n)` and summed.

## 2. The exact incidence Gram matrix is diagonal

Let

\[
B_{q,n}:=\mathbf 1_{E_q(I)}(n).
\tag{12}
\]

Then disjointness gives the row Gram matrix

\[
\boxed{
BB^*=\operatorname{diag}\bigl(|E_q(I)|\bigr)_q.
}
\tag{13}
\]

The column Gram matrix is equally simple:

\[
B^*B=\operatorname{diag}\bigl(\mathbf 1_{E(I)}(n)\bigr)_n,
\tag{14}
\]

because every `n` belongs to at most one first-exit cell. After normalizing nonempty rows by `|E_q|^{-1/2}`, the source-incidence rows are exactly orthonormal.

Multiplication by the fixed translated-ratio kernel `K_h(n)` does not change support. Nor do arbitrary row-dependent coefficients `c_q(n)` create overlap between different `q` cells. This proves `(8)`.

If `U` is a common unitary transform on the ambient source space, then

\[
\langle Uf_q,Uf_r\rangle
=\langle f_q,f_r\rangle,
\]

which gives `(9)`. Taking `U` to be a complete discrete Fourier transform shows that a full-frequency Parseval calculation retains a diagonal `q` Gram matrix even though the individual Fourier transforms overlap pointwise in frequency. Any apparent off-diagonal frequency interaction cancels exactly when the complete dual space is recombined.

This is the precise sense in which **common completion does not create first-exit dispersion**. It may change coordinates, but it cannot turn the deterministic first-exit partition into an independent averaging variable.

## 3. Why progression-only overlap is not an escape

The arithmetic progressions

\[
q\mid n
\quad\text{or}\quad
q\mid n+h
\tag{15}
\]

certainly overlap for different primes. But the live first-exit rows are not those bare progressions. They also contain the nested residual condition

\[
A_q(n)=1,
\tag{16}
\]

which says that no earlier active prime divides `F_h(n)`. It is exactly `(16)` that converts the overlapping divisibility progressions into the disjoint cells `(1)`.

Therefore dropping the cutoff to manufacture overlapping `q`-progressions is not a harmless relaxation of the exact source family. It removes the least-prime selector that makes Buchstab first exit exact. Any majorization, envelope, or bracket used to replace `(16)` must independently pass the transfer barriers already recorded in `MC-479`--`MC-483`.

Conversely, keeping `(16)` while applying a common source transform leaves the Gram diagonal by `(9)`. Thus the clue's phrase "joint q-dependence of progression incidence and nested cutoff" has a sharper interpretation: their **exact joint effect at source level is a partition**, not an overlapping two-dimensional incidence geometry.

## 4. What can still create a genuine q-coupling

The result does not say that the first-exit prime is useless. It says that writing the deterministic least-prime label as an outer summation variable is not itself a new source dimension.

There are three structurally different ways a live continuation could still use `q`.

First, a transform may itself depend on `q`. If row `q` is completed modulo a `q`-dependent modulus or sent through a `q`-dependent reciprocity/Poisson map `U_q`, then

\[
\langle U_qf_q,U_rf_r\rangle
\]

need not vanish for `q\ne r`, because the common-unitary identity `(9)` no longer applies. Such a construction must be derived from the arithmetic problem rather than chosen merely to force overlap.

Second, the actual source coefficient can depend arithmetically on the first-exit prime. Equation `(11)` shows exactly what survives: not a free extra variable, but the weight `c_{q_*(n)}(n)` attached to each source integer through its least active prime divisor. A successful estimate must use a proved property of those actual coefficients.

Third, one may duplicate another source variable before first-exit labels are positively closed and derive a transformed kernel in which distinct factor labels occupy genuinely different modulus or phase roles. This is the structural pattern isolated in `MC-456`: the factor labels become observable because dispersion/completion is factor-dependent before the multiplication quotient forms.

All three routes require information absent from the bare partition `(1)`--`(6)`.

## 5. Prior art and novelty boundary

The underlying first-exit decomposition is classical Buchstab identity. Standard sieve references formulate it as

\[
S(\mathcal A,\mathcal P,z)
=
S(\mathcal A,\mathcal P,w)
-
\sum_{w\le q<z}S(\mathcal A_q,\mathcal P,q),
\]

with the proof assigning a sifted-out element to its least prime factor in the active range. Halberstam--Richert, *Sieve Methods* (Academic Press, 1974), is a classical reference; the Encyclopedia of Mathematics entry on Buchstab's identity records the same standard formula and reference. `MC-484` already audited this identity and its higher-dimensional use in the present pair-sieve setting.

Orthogonality of disjointly supported vectors and preservation of inner products by a common unitary transform are elementary Hilbert-space facts. No novelty is claimed for `(8)`--`(9)` or for Parseval.

The Mathia-specific delta is the **frontier classification** obtained by applying those classical facts after the affine normalization of `MC-487`: the exact progression-plus-cutoff rows proposed by the accepted clue are not an overlapping source family at all, but the disjoint first-exit partition `(1)`. This removes common source completion/Parseval as a possible way to turn that incidence geometry into new cross-`q` information.

The neighboring positive prior art in `MC-456` is consistent with the distinction. Pascadi's triply-well-factorable dispersion works because factor variables enter different arithmetic modulus roles before completion, so the transforms seen by the factor blocks are not one common relabeling of a disjoint source partition. No theorem from that literature is transferred here.

## Boundaries and falsification tests

- **The exact cutoff is essential.** Bare progressions for different `q` overlap; the complete first-exit cells including `A_q` do not. A proposed overlap gain must state explicitly which exact condition was removed or replaced and pay for that transfer.
- **Common transforms only.** Equation `(9)` applies to the same isometry/unitary `U` acting on every row. A genuinely `q`-dependent completion or reciprocity map is outside this obstruction and is now the primary live analytic possibility.
- **No claim against scalar cancellation.** The scalar row sums `\sum_{n\in E_q}f_q(n)` may cancel when summed over `q`. The finding says only that such cancellation is not forced by an independent support-overlap dimension or by a common unitary/Parseval transform.
- **Actual coefficients remain load-bearing.** A special arithmetic pattern in `c_{q_*(n)}(n)` can still matter. Coefficient-blind conclusions must not be upgraded to a no-go for the exact source weights.
- **Root collisions are already absorbed.** Primes dividing `h` merge the two local roots but do not violate the uniqueness of the first-exit prime.
- **No envelope shortcut.** Replacing `A_q` by a positive or bracketed approximation reopens the selector/leakage questions of `MC-479`--`MC-483`; it is not covered by the exact partition proof.
- **No global Möbius consequence.** The result is a representation and operator obstruction inside one first-exit continuation.

## Consequence for the research line

The normalized empty-vector first-exit frontier is narrower again. `MC-487` removes the moving inverse shift as affine gauge; the present finding shows that the remaining exact progression-plus-cutoff supports are a deterministic least-prime partition and stay orthogonal under every common source transform.

Therefore a new estimate should no longer seek generic "cross-q dispersion" from overlap of the exact normalized rows. The first admissible positive step must exhibit an operation whose arithmetic depends on `q` before positive closure — for example a `q`-dependent completion/modulus/reciprocity map, or an exact outer coefficient whose least-prime dependence survives refolding and yields a quantitative gain. If every legal continuation uses only a common transform of the partitioned rows, the first-exit variable is only lossless bookkeeping and the route refolds to the original hard-mask shell.