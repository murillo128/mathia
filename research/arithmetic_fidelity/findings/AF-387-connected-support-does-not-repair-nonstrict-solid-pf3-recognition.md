# AF-387 — Connected support does not repair nonstrict solid PF3 recognition on one lattice

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `PF3` · `TOEPLITZ` · `CERTIFICATE-COMPRESSION` · `LOWER-ORDER-DEGENERACY` · `NEGATIVE/OBSTRUCTION` · `NO-NOVELTY-CLAIM`

## Claim

AF-386 shows that at order two, the failure of nonstrict solid-minor recognition is repaired exactly by one qualitative resource: no internal zeros. That repair does **not** extend unchanged to order three, even in the discrete Toeplitz setting.

For any parameter

\[
0<t<1,
\]

define a bi-infinite nonnegative sequence by

\[
a_0=a_1=a_2=a_3=1,\qquad a_4=t,
\qquad a_n=0\quad(n\notin\{0,1,2,3,4\}).
\tag{1}
\]

Let

\[
A_{rs}=a_{r-s},\qquad r,s\in\mathbb Z,
\tag{2}
\]

be its Toeplitz matrix. Then all of the following hold simultaneously:

1. the positive support of `a` is the interval of integers `\{0,1,2,3,4\}`, so there are no internal zeros;
2. `a` is `PF_2`, hence **every** Toeplitz minor of orders one and two is nonnegative;
3. every solid/consecutive order-three Toeplitz minor is nonnegative;
4. `A` nevertheless has a strictly negative order-three minor, so `a` is not `PF_3`.

Therefore, already at `k=3`, **full lower-order total nonnegativity + connected support + nonnegative solid top-order minors do not imply total nonnegativity through order three on a fixed lattice**.

This sharply separates the two resources that AF-385 had bundled into strict lower-order positivity. At order two, zero-pattern topology is enough to replace strictness. At order three, support connectivity does not control lower-order degeneracy inside the positive support.

## Exact lower-order verification

The sequence in `(1)` has no internal zeros. Its adjacent order-two determinants are

\[
C_2(d):=a_d^2-a_{d-1}a_{d+1}.
\tag{3}
\]

The only nonzero values are

\[
C_2(0)=1,\qquad
C_2(3)=1-t,\qquad
C_2(4)=t^2,
\tag{4}
\]

while

\[
C_2(1)=C_2(2)=0.
\tag{5}
\]

Thus `a` is nonnegative, log-concave, and has no internal zeros. By the classical `PF_2` characterization, the full Toeplitz matrix `(2)` is totally nonnegative through order two, not merely on adjacent minors.

The equalities in `(5)` are important: they occur **inside** the positive support. The source is therefore topologically connected but lies on a lower-order boundary of the totally-nonnegative cone rather than in its strict interior.

## Every solid order-three minor passes

Define the solid order-three determinants

\[
C_3(d)
:=
\det\!\left(a_{d+i-j}\right)_{i,j=0}^{2}.
\tag{6}
\]

Direct evaluation gives

\[
C_3(0)=1,
\qquad
C_3(3)=(1-t)^2,
\qquad
C_3(4)=t^3,
\tag{7}
\]

and

\[
C_3(d)=0
\qquad
\text{for every other }d\in\mathbb Z.
\tag{8}
\]

Hence every fully consecutive order-three Toeplitz minor is nonnegative. Together with `PF_2`, this supplies strictly more side information than the naive nonstrict version of AF-385 would require: **all** lower-order minors are already known nonnegative, the support has no holes, and every solid top-order generator passes.

## A hidden nonlocal order-three minor

Take rows

\[
I=(1,2,4)
\]

and columns

\[
J=(0,1,2).
\]

The corresponding Toeplitz submatrix is

\[
A[I\mid J]
=
\begin{pmatrix}
1&1&0\\
1&1&1\\
t&1&1
\end{pmatrix}.
\tag{9}
\]

Its determinant is

\[
\det A[I\mid J]=t-1<0.
\tag{10}
\]

Thus `A` is not totally nonnegative through order three and the sequence is not `PF_3`.

The failure is purely a placement alias. The solid family never sees the gapped row pattern `(1,2,4)`, and the lower-order data do not propagate its sign because the order-two interior has collapsed along `(5)`.

## What replaces the PF2 support-topology story

AF-386 identified an exact order-two dichotomy. Adjacent log-concavity controls local shape, while connected positive support prevents those inequalities from becoming vacuous across a zero gap. Once both are retained, the full `PF_2` target is recovered.

AF-387 shows that order three has an additional failure mode. The support can be perfectly connected and the entire lower-order `PF_2` target can hold, yet zero lower-order minors **inside** that support can block propagation from solid order-three generators to nonlocal order-three placements.

So the resource split is at least three-way:

- support topology controls whether positive regions are disconnected;
- lower-order nonnegativity controls the sign but permits flat/degenerate strata;
- lower-order interiority controls whether local determinant information can propagate through those strata without losing placement information.

At `k=2`, the third resource is unnecessary once support connectivity is known. At `k=3`, the example proves that it cannot simply be discarded in favor of support connectivity.

This does not prove that full strictness is minimal. A weaker zero-minor pattern condition, almost-strict total positivity condition, rank condition, or another structural rule may still be enough. What is ruled out is the specific extrapolation

\[
\text{lower-order TN + no internal zeros + solid }C_3\ge0
\Longrightarrow PF_3.
\tag{11}
\]

## Relation to AF-384--AF-386

AF-384 and AF-385 use strict positivity of the required lower-order initial/solid minors to invoke a finite recognition theorem. AF-386 shows that for `k=2` this strictness overpays: connected positive support is the exact missing qualitative resource.

The family `(1)` explains why that simplification is exceptional at the first nontrivial order. It satisfies the strongest natural nonstrict replacement one could infer from AF-386—full `PF_2` plus no internal zeros—yet the solid order-three test is not target-complete.

AF-387 therefore does not weaken AF-385. It validates the role of its strict-interior hypothesis at `k=3` by exhibiting what can go wrong when strictness is removed. The example also refines the open question: the next useful target is **not** merely a higher-order notion of connected support, but a characterization of which lower-order zero-minor patterns permit solid order-`k` recognition.

## Fixed-lattice versus shrinking-mesh boundary

The obstruction above is exact on one discrete lattice. It does **not** by itself settle the continuum shrinking-mesh question left by AF-385.

A fixed continuous profile tested on a sequence `h_m\to0` must satisfy compatible solid-minor inequalities at arbitrarily fine resolutions. Such multiscale consistency could rule out discrete aliases like `(1)`, or it could admit a continuous analogue with persistent lower-order degeneracy. AF-387 establishes neither outcome.

The sharpened continuum question is therefore:

> Can a continuous nonnegative profile with connected positive support pass the nonstrict solid hierarchy through order three on a vanishing mesh sequence and still fail continuum `TN_3`, or does multiscale consistency supply a weaker replacement for strict lower-order interiority?

That is a genuinely stronger question than the fixed-lattice recognition problem and should not be answered by importing `(1)` unchanged.

## Prior-art and novelty audit

The surrounding mathematics is classical, and no novelty is claimed for the general phenomenon that nonstrict total-nonnegativity recognition requires more care than strict total positivity.

- Samuel Karlin, ***Total Positivity, Vol. I***, Stanford University Press (1968). Role: classical Pólya-frequency and total-positivity background, including the `PF_2` / log-concavity boundary used above.
- Francesco Brenti, ***Unimodal, Log-Concave and Pólya Frequency Sequences in Combinatorics***, Memoirs of the AMS **81**(413) (1989), DOI `10.1090/memo/0413`. Role: standard discrete `PF_2`, log-concavity, and no-internal-zero background.
- H. F. Weinberger, **“A Characterization of the Polya Frequency Functions of Order 3,”** *Applicable Analysis* **15**(1--4) (1983), 53--69, DOI `10.1080/00036818308839439`. Role: direct prior-art boundary showing that order-three Pólya-frequency structure has its own classical characterization theory; AF-387 is not a claim to characterize `PF_3`.
- M. Gasca and J. M. Peña, **“Characterizations and Decompositions of Almost Strictly Positive Matrices,”** *SIAM Journal on Matrix Analysis and Applications* **28**(1) (2006), 1--8, DOI `10.1137/050631203`. Role: established theory in which zero patterns and boundary minors provide reduced recognition for structured nonstrict total positivity; this is the natural prior-art region for any attempt to replace AF-385 strictness by a weaker zero-minor condition.
- Christian Grussler and Tobias Damm, **“Efficient `k`-Sign Consistency Verification of Hankel Matrices via Schur Polynomials,”** arXiv:`2602.08122` (8 February 2026), especially Proposition 2. Role: the strict-lower-order finite recognition criterion used by AF-384/AF-385 and the immediate source of the resource question answered negatively here in the nonstrict `k=3` case.

The one-parameter witness `(1)` is an elementary exact counterexample organized for Mathia's certificate-resource question. The durable contribution is the **resource separation**, not a new theorem about the classical `PF_3` class: support connectivity and lower-order interiority are different retained structures, and the first cannot replace the second once order-three placement must be reconstructed.

## Riemann-facing boundary

This finding has no direct RH consequence. It concerns the certificate geometry of Pólya-frequency targets before any arithmetic source has supplied the required determinant signs.

Its practical warning is narrower. If an RH-facing route tries to replace arbitrary translation minors by a solid/consecutive family, proving connected support and lower-order nonnegativity is not enough at order three. One must either retain a stronger lower-order zero-pattern/interiority certificate or prove a separate multiscale theorem showing that the continuous source cannot realize the fixed-lattice alias.

The example is also in a discrete Toeplitz sequence model, not automatically the same model as a Riemann-associated translation kernel or a coefficient Toeplitz matrix. Any transfer must identify the exact matrix/kernel and source assumptions rather than importing the sign failure by analogy.

## Boundaries and falsification checks

The parameter restriction `0<t<1` is load-bearing for the displayed witness: it makes `(4)` nonnegative and `(10)` strictly negative.

The example has no internal zeros in its positive integer support, but it does have zeros outside that finite support. That is compatible with the standard discrete `PF_2` notion and is not the internal-gap mechanism of AF-386.

The obstruction remains even though the **full** order-two Toeplitz family is nonnegative; it is not an artifact of checking only adjacent `2x2` minors. What fails is strict lower-order interiority, witnessed by the zero minors in `(5)`.

No claim is made that strict lower-order positivity is necessary for every `PF_3` recognition theorem. Classical almost-strict and zero-pattern theories show that weaker structured hypotheses can suffice in special classes. AF-387 only proves that support connectivity plus nonstrict lower-order total nonnegativity is not enough by itself.

Finally, the fixed-lattice example does not answer whether a shrinking family of meshes for one continuous profile removes the degeneracy. That multiscale question remains open after this finding.