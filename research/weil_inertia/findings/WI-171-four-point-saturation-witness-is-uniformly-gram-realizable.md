# WI-171 — the WI-166 four-point saturation witness is uniformly Gram-realizable

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + BARRIER + STRUCTURAL-RIGIDITY`. WI-166 closes positive four-point cover improvements after relaxing the Montgomery--Taylor pair data to arbitrary nonnegative weights: its exact saturation witness puts weight `epsilon/2` only on third-neighbor pairs. The obvious surviving objection was that this sparse weight pattern might already be forbidden by positive-semidefinite/Gram consistency. It is not. For every block length `m>=4`, the WI-166 pair-weight witness is the entrywise-square pattern of a real unit-diagonal **positive-definite Toeplitz Gram matrix** whose spectrum stays uniformly bounded away from zero and infinity.

With

\[
\varepsilon=\frac{231}{100000},
\qquad
c:=\sqrt{\frac{\varepsilon}{2}}
=\sqrt{\frac{231}{200000}},
\]

there is a Gram matrix `G_m` satisfying

\[
(G_m)_{ii}=1,
\qquad
|(G_m)_{ij}|^2=
\begin{cases}
\varepsilon/2,&|i-j|=3,\\
0,&i\ne j,\ |i-j|\ne3,
\end{cases}
\tag{A}
\]

and, uniformly in `m`,

\[
\boxed{
\frac9{10}I_m\prec G_m\prec\frac{11}{10}I_m.
}
\tag{B}
\]

Hence PSD feasibility, full rank, principal-minor positivity, ordinary interlacing, generic determinant nonvanishing, bounded condition number, and even Toeplitz/stationary Gram structure do **not** exclude the sharp abstract pair-weight witness from WI-166. Any source-constrained escape from that barrier must use information that couples the pair weights to the actual Montgomery--Taylor translation kernel and ordered gap/pressure geometry, or use genuinely additional arithmetic information. No unconditional zeta-zero proportion changes here.

## 1. The exact WI-166 witness

For `m>=4`, put `q=m-3`. WI-166 studies the local four-point functionals

\[
C_s(w)
=\frac23\bigl(w_{s,s+1}+w_{s+1,s+2}+w_{s+2,s+3}\bigr)
 +\bigl(w_{s,s+2}+w_{s+1,s+3}\bigr)
 +2w_{s,s+3},
\tag{1}
\]

for `s=0,...,q-1`, with local constraints

\[
\varepsilon\le C_s(w)+P_s,
\qquad P_s\ge0.
\tag{2}
\]

Its primal saturation point is

\[
P_s=0,
\qquad
w_{s,s+3}=\frac\varepsilon2,
\qquad
w_{ij}=0\ \text{for every other pair}.
\tag{3}
\]

Then every local inequality is an equality,

\[
C_s(w)=2\frac\varepsilon2=\varepsilon,
\]

and the global pair resource is

\[
E=2\sum_{i<j}w_{ij}=q\varepsilon.
\tag{4}
\]

WI-166 deliberately did not assert that (3) came from a Gram matrix or from the Montgomery--Taylor kernel. The first of those two possible obstructions can be tested exactly.

## 2. A uniformly positive-definite Gram realization

Let `A_m^{(3)}` be the symmetric adjacency matrix on the vertices `0,...,m-1` with an edge precisely when

\[
|i-j|=3.
\tag{5}
\]

Equivalently, this graph is the disjoint union of the three path graphs obtained by restricting to the three residue classes modulo `3`. Define

\[
\boxed{G_m:=I_m+cA_m^{(3)}.}
\tag{6}
\]

Equation (A) is immediate from `c^2=epsilon/2`.

Every row of `A_m^{(3)}` contains at most two nonzero entries. Therefore Gershgorin's theorem, or simply the symmetric operator-norm bound `||A_m^{(3)}||<=2`, gives

\[
1-2c\le\lambda(G_m)\le1+2c.
\tag{7}
\]

Moreover

\[
c<\frac1{20},
\]

because

\[
\frac{231}{200000}<\frac1{400}
\quad\Longleftrightarrow\quad
92400<200000.
\tag{8}
\]

Thus

\[
1-2c>\frac9{10},
\qquad
1+2c<\frac{11}{10},
\]

which proves (B). In particular `G_m` is positive definite for every `m`, with condition number uniformly bounded by `11/9` using the coarse rational enclosure above.

Since `diag(G_m)=1`, positive definiteness makes `G_m` the Gram matrix of `m` linearly independent unit vectors. Consequently the exact WI-166 weights satisfy

\[
w_{ij}=|\langle v_i,v_j\rangle|^2
\tag{9}
\]

for a uniformly well-conditioned family of unit vectors.

## 3. Principal minors, rank, and determinant constraints do not rescue PSD alone

Every principal submatrix of `G_m` has the form `I+cA'`, where `A'` is an induced subgraph of the same degree-at-most-two graph. The argument above therefore applies verbatim:

\[
\frac9{10}I\prec G_m[J]\prec\frac{11}{10}I
\tag{10}
\]

for every nonempty coordinate set `J`. Hence all principal minors are strictly positive, all coordinate compressions have full rank, and ordinary Cauchy interlacing remains uniformly separated from zero.

For a principal submatrix of size `r`, (10) also gives

\[
\left(\frac9{10}\right)^r
<\det G_m[J]
<\left(\frac{11}{10}\right)^r.
\tag{11}
\]

Thus an attempted refinement that merely appends generic PSD feasibility, nonzero determinants, principal-minor positivity, or a fixed Riesz/conditioning lower bound to the arbitrary-weight relaxation still admits the saturation witness. Such constraints can become useful only when their **actual numerical values are tied to the Montgomery--Taylor kernel or another source invariant**, not when they are used as abstract Gram consistency checks.

## 4. The witness is even stationary Toeplitz

The construction is stronger than an arbitrary Gram realization: `G_m` depends only on `i-j`. The bi-infinite correlation sequence

\[
r_0=1,
\qquad r_{\pm3}=c,
\qquad r_n=0\quad(n\ne0,\pm3)
\tag{12}
\]

has spectral density

\[
\boxed{F(\theta)=1+2c\cos(3\theta).}
\tag{13}
\]

Because `c<1/20`,

\[
F(\theta)\ge1-2c>\frac9{10}>0.
\tag{14}
\]

The classical Herglotz/Toeplitz correspondence therefore gives the same positive-definite sequence on the whole integer lattice, and `G_m=(r_{i-j})` is its finite restriction. So stationarity or Toeplitz structure by itself is also too weak to reject (3).

This matters because the genuine Montgomery--Taylor Gram is likewise a translation Gram. The surviving distinction is not generic translation invariance; it is the **specific kernel-value relation** imposed by the Montgomery--Taylor optimizer together with the additive distance relation coming from ordered zero gaps.

## 5. Where the actual source coupling still bites

The realization above does **not** turn the whole WI-166 primal point into a Montgomery--Taylor zero configuration. In the relaxed saturation point, all local pressures were set to zero. For the actual four-point zeta geometry the pressure is tied to the three-gap span, while the pair weights are simultaneously tied to those same gaps through the fixed Montgomery--Taylor kernel.

In particular, forcing all gaps to zero would make all points coincide. A normalized translation Gram would then have every pair entry equal to the kernel value at zero, rather than the sparse lag-three pattern (A). Conversely, the Toeplitz realization (12) is only a generic stationary correlation sequence; it is not asserted to equal the Montgomery--Taylor kernel sampled at an admissible gap configuration with zero pressure.

Therefore WI-171 does **not** resolve the full source-constrained question left by WI-166. It isolates its load-bearing part:

\[
\boxed{
\text{PSD / Gram / Toeplitz consistency alone is insufficient;}
\quad
\text{kernel--placement--pressure coupling is essential.}
}
\tag{15}
\]

A future improvement must prove a source-specific incompatibility that survives the global assembly, rather than invoke PSD as an extra constraint in the abstract.

## 6. Relation to existing barriers

WI-026 already gives a stronger, source-realizable periodic obstruction for the single Montgomery--Taylor profile after the complete shifted-block assembly: even an oracle for the optimal universal local `D+P_m` constant cannot cross `0.673604` through that architecture. WI-171 acts at a different and earlier logical layer. It shows that the exact local saturation witness of WI-166 cannot be dismissed merely because WI-166 relaxed away Gram consistency.

This also clarifies what principal-minor or interlacing refinements from the line's broader mandate would have to retain. Generic matrix feasibility is exhausted by (6)--(11); a useful refinement must exploit identities of **the actual MT translation Gram**, a second independent profile, the exceptional indefinite block, or another source-accessible invariant.

## 7. Prior-art and novelty audit

No novelty is claimed for Gershgorin bounds, path-graph spectra, Gram realization of positive-semidefinite matrices, positive-definite Toeplitz sequences, or the Herglotz correspondence. A targeted literature search around banded Toeplitz correlation matrices and path-adjacency Gram constructions found these ingredients only as standard matrix/covariance machinery, as expected.

The repository-local novelty check is the substantive one here. WI-166 explicitly leaves `positive-semidefinite/Gram consistency` as a possible way to invalidate its arbitrary-weight witness; WI-026 instead constrains the fully source-realizable scalar block architecture by a different period-33 configuration. No existing `weil_inertia` finding located in the current corpus supplies the explicit uniformly conditioned Gram realization (6) for WI-166's own saturation point.

The durable deduction is therefore a **route closure**, not a new matrix theorem: the proposed PSD-only escape from WI-166 fails on an exact, uniformly well-conditioned Toeplitz Gram realization.

## 8. Consequence for the research line

The positive-cover frontier is narrower than it appeared. Adding PSD, full-rank, principal-minor, determinant, interlacing, or generic Toeplitz constraints to the arbitrary nonnegative pair-weight relaxation cannot create a strict surplus over the WI-166 saturation point. The next meaningful test is the smallest source-constrained class that keeps the actual Montgomery--Taylor relation

\[
w_{ij}=|K_{\rm MT}(y_j-y_i)|^2
\]

and the common ordered-gap ledger that also determines pressure.

If that coupled class forces a strict surplus, it must be quantified and propagated through the full assembly; if a source-realizable periodic configuration saturates or asymptotically saturates the same resource, the remaining kernel-constrained cover escape closes as well. Either outcome requires more structure than abstract Gram positivity.