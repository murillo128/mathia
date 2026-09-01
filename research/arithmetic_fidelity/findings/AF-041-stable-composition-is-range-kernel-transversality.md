# AF-041 — Stable composition fidelity is range–kernel transversality

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `STRUCTURAL-CLASSIFICATION`, `NEGATIVE/OBSTRUCTION`

## Claim

Let `H,K,L` be real or complex Hilbert spaces. Let

\[
A:H\to K,
\qquad
B:K\to L
\]

be bounded linear maps. Assume that `A` is injective with closed range and that `B` has closed range. Write

\[
M=\operatorname{Ran}A,
\qquad
N=\ker B.
\]

Define the lower modulus of the upstream carrier

\[
a(A)=\inf_{\|x\|=1}\|Ax\|>0,
\]

and the reduced minimum modulus of the downstream map

\[
\gamma(B)
=
\inf_{\substack{y\in N^\perp\\\|y\|=1}}
\|By\|>0.
\]

The range–kernel transversality modulus is

\[
\tau(M,N)
=
\inf_{\substack{m\in M\\\|m\|=1}}
\operatorname{dist}(m,N).
\]

Then:

1. **Exact fidelity through the chain is exactly a range–kernel intersection test.**
   \[
   \boxed{
   \ker(BA)=\{0\}
   \iff
   M\cap N=\{0\}.
   }
   \]
   More precisely,
   \[
   A(\ker BA)=M\cap N.
   \]

2. **Stable fidelity requires strictly more than exact fidelity.** The composite `BA` is bounded below if and only if
   \[
   \boxed{
   \tau(M,N)>0.
   }
   \]
   Because `M` and `N` are closed, this is equivalent to
   \[
   \boxed{
   M\cap N=\{0\}
   \quad\text{and}\quad
   M+N\text{ is closed}.
   }
   \]
   Thus two individually closed-range stages can compose to an exact but unstable map.

3. **The loss of conditioning is quantitatively controlled by transversality.** If
   \[
   \gamma(BA)=\inf_{\|x\|=1}\|BAx\|,
   \]
   then
   \[
   \boxed{
   \gamma(B)\,a(A)\,\tau(M,N)
   \le
   \gamma(BA)
   \le
   \|B\|\,\|A\|\,\tau(M,N).
   }
   \]
   Hence a uniform stability theorem for a family of compression chains needs uniform lower bounds not only for the individual stages but also for the angle at which the surviving upstream range meets the downstream kernel.

4. **When exact fidelity holds, the transversality modulus is the sine of the range–kernel angle.** If `M\cap N=\{0\}` and `c(M,N)` denotes the Friedrichs cosine, then
   \[
   \boxed{
   \tau(M,N)=\sqrt{1-c(M,N)^2}.
   }
   \]
   Consequently
   \[
   \boxed{
   BA\text{ is stably faithful}
   \iff
   c(M,N)<1.
   }
   \]

5. **Orthogonal quotienting is the sharp model case.** If the downstream compression is
   \[
   Q_N=P_{N^\perp}:K\to N^\perp,
   \]
   then
   \[
   \boxed{
   a(A)\tau(M,N)
   \le
   \gamma(Q_NA)
   \le
   \|A\|\tau(M,N).
   }
   \]
   If `A` is a scaled isometry, `\|Ax\|=c\|x\|`, the bounds coincide:
   \[
   \boxed{
   \gamma(Q_NA)=c\,\tau(M,N).
   }
   \]
   Thus, for an isometric carrier followed by a Hilbert quotient, the angle to the forgotten subspace is exactly the stability cost of the compression.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{stagewise stable fidelity does not compose unless the upstream retained range stays uniformly transverse to the next kernel.}
}
\]

This is the stable analogue of AF-001's deterministic composition obstruction. Exact information lost by an earlier map cannot be recreated downstream; even when no exact collision occurs, information can approach the downstream kernel arbitrarily closely and make the inverse discontinuous.

## Derivation

### Exact collisions are precisely range–kernel intersections

Since `A` is injective,

\[
BAx=0
\iff
Ax\in\ker B=N.
\]

But `Ax\in M`, so

\[
A(\ker BA)=M\cap N.
\]

Injectivity of `A` immediately gives

\[
\ker BA=\{0\}
\iff
M\cap N=\{0\}.
\]

This is the exact composition law in geometric form: a downstream compression destroys an upstream discriminator direction exactly when the upstream carrier lands in the downstream nullspace.

### Closed range gives a distance-to-kernel estimate

Because `B` has closed range, its restriction

\[
B|_{N^\perp}:N^\perp\to\operatorname{Ran}B
\]

is a bounded bijection with bounded inverse. Hence `\gamma(B)>0` and, for every `y\in K`,

\[
By=B P_{N^\perp}y.
\]

Therefore

\[
\gamma(B)\operatorname{dist}(y,N)
\le
\|By\|
\le
\|B\|\operatorname{dist}(y,N).
\]

Applying this to `y=Ax\in M` yields

\[
\|BAx\|
\ge
\gamma(B)\operatorname{dist}(Ax,N).
\]

By the definition of `\tau(M,N)`,

\[
\operatorname{dist}(Ax,N)
\ge
\tau(M,N)\|Ax\|
\ge
\tau(M,N)a(A)\|x\|.
\]

Thus

\[
\gamma(BA)
\ge
\gamma(B)a(A)\tau(M,N).
\]

For the reverse estimate, choose unit vectors `m_j\in M` with

\[
\operatorname{dist}(m_j,N)\to\tau(M,N).
\]

Write `m_j=Ax_j`. Since `\|m_j\|=1`,

\[
\|x_j\|\ge\frac1{\|A\|}.
\]

After normalizing `u_j=x_j/\|x_j\|`,

\[
\begin{aligned}
\|BAu_j\|
&=
\frac{\|Bm_j\|}{\|x_j\|}\\
&\le
\frac{\|B\|\operatorname{dist}(m_j,N)}{\|x_j\|}\\
&\le
\|B\|\,\|A\|\operatorname{dist}(m_j,N).
\end{aligned}
\]

Taking the infimum and then the limit gives

\[
\gamma(BA)
\le
\|B\|\|A\|\tau(M,N).
\]

The two estimates show that, once the individual stage constants are controlled, **all remaining collapse in the composition is concentrated in one geometric number: the range–kernel transversality modulus**.

### Positive transversality is the closed-sum condition

For closed subspaces `M,N`, the quantity

\[
\tau(M,N)
=
\inf_{\|m\|=1,m\in M}\|P_{N^\perp}m\|
\]

is positive exactly when `P_{N^\perp}|_M` is bounded below. Its kernel is `M\cap N`. Its range is naturally isomorphic to the image of `M` in the Hilbert quotient `K/N`.

If `M\cap N=\{0\}`, the classical closed-subspace angle criterion gives

\[
P_{N^\perp}|_M\text{ bounded below}
\iff
M+N\text{ closed}
\iff
c(M,N)<1.
\]

Moreover

\[
\begin{aligned}
\tau(M,N)^2
&=
\inf_{\|m\|=1,m\in M}
\left(1-\|P_Nm\|^2\right)\\
&=
1-
\sup_{\|m\|=1,m\in M}\|P_Nm\|^2\\
&=
1-c(M,N)^2,
\end{aligned}
\]

where the last equality uses the zero-intersection hypothesis. If the intersection is nonzero, exact fidelity has already failed and `\tau(M,N)=0`.

Combining this with the quantitative bounds proves the stable-composition criterion.

### Quotient specialization

For `Q_N=P_{N^\perp}`, the downstream kernel is exactly `N` and

\[
\gamma(Q_N)=\|Q_N\|=1
\]

unless the quotient is trivial. The general bounds reduce to

\[
a(A)\tau(M,N)
\le
\gamma(Q_NA)
\le
\|A\|\tau(M,N).
\]

If `A=cU` for an isometry `U`, then `a(A)=\|A\|=c`, so equality is forced. In that case the abstract stability defect is literally the sine of the angle between the encoded carrier and the subspace discarded by the quotient.

This supplies a precise replacement for the vague statement that a downstream quotient is harmless because it is itself well conditioned. A quotient is perfectly conditioned on `N^\perp`, but it can still be arbitrarily ill conditioned on a particular incoming carrier `M` if that carrier approaches `N`.

## Explicit exact-but-unstable composition control

Let

\[
H_0=\ell^2(\mathbb N)
\]

and define the bounded injective diagonal operator

\[
De_k=\frac1k e_k.
\]

Its range is dense but not closed. Set

\[
H=H_0,
\qquad
K=H_0\oplus H_0,
\qquad
L=H_0.
\]

Define

\[
A:H_0\to H_0\oplus H_0,
\qquad
Ax=(x,Dx),
\]

and

\[
B:H_0\oplus H_0\to H_0,
\qquad
B(u,v)=v.
\]

Then `A` is bounded below because

\[
\|Ax\|^2=\|x\|^2+\|Dx\|^2\ge\|x\|^2,
\]

and its range

\[
M=\operatorname{graph}(D)
\]

is closed. The map `B` is a surjective orthogonal coordinate quotient with

\[
N=\ker B=H_0\oplus\{0\},
\qquad
\gamma(B)=1.
\]

Thus both stages individually have closed range and stable inverses on their natural supports.

Their exact interaction is also collision-free:

\[
M\cap N=\{0\},
\]

because `(x,Dx)\in N` implies `Dx=0`, hence `x=0`.

Nevertheless

\[
M+N
=
H_0\oplus\operatorname{Ran}D,
\]

which is dense and nonclosed. Hence

\[
\tau(M,N)=0,
\qquad
c(M,N)=1,
\]

and the composite is exact but not bounded below. Indeed,

\[
BA=D,
\]

so

\[
\|BAe_k\|=\frac1k\longrightarrow0.
\]

This is a particularly sharp control because the downstream operation is not itself pathological: it is merely deletion of one orthogonal coordinate. The instability arises entirely from the **relative position** of the retained upstream graph and the downstream forgotten subspace.

## Finite-scale consequence

Let

\[
H_0^{(n)}=\operatorname{span}\{e_1,\ldots,e_n\}
\]

and restrict `D,A,B` to the first `n` coordinates. Every finite composite is stably invertible, with

\[
\gamma(B_nA_n)
=
\gamma(D_n)
=
\frac1n.
\]

For the graph carrier,

\[
a(A_n)=\sqrt{1+\frac1{n^2}},
\]

while its transversality to the horizontal kernel is

\[
\tau(M_n,N_n)
=
\frac1{\sqrt{n^2+1}}.
\]

Therefore the lower composition bound is sharp at every finite stage:

\[
\gamma(B_n)a(A_n)\tau(M_n,N_n)
=
1\cdot
\sqrt{1+\frac1{n^2}}
\cdot
\frac1{\sqrt{n^2+1}}
=
\frac1n.
\]

Yet

\[
\gamma(B_nA_n)\to0.
\]

So even a chain in which **every finite stage has two individually stable maps and an injective stable composite** can lose all uniform stability in the limit. The missing hypothesis is not another stagewise bound; it is a uniform range–kernel angle.

## Prior art and novelty assessment

The closed-range/product-angle mathematics is classical, and no novelty is claimed for the operator-theoretic criterion itself.

- Richard Bouldin, **“The Product of Operators with Closed Range,”** *Tohoku Mathematical Journal, Second Series* 25(3) (1973), 359–363, DOI `10.2748/tmj/1178241337`. Bouldin proves a closed-range criterion for a product of two closed-range Hilbert-space operators in terms of a positive angle between the incoming range and the relevant part of the next kernel. This directly classicalizes the core range–kernel transversality boundary used here.
- Richard Bouldin, **“The Pseudo-Inverse of a Product,”** *SIAM Journal on Applied Mathematics* 24(4) (1973), 489–495, DOI `10.1137/0124051`. Role: classical conditions for product Moore–Penrose inverses and stable reconstruction through operator products.
- Saichi Izumino, **“The Product of Operators with Closed Range and an Extension of the Reverse Order Law,”** *Tohoku Mathematical Journal, Second Series* 34(1) (1982), 43–52, DOI `10.2748/tmj/1178229307`. Role: later closed-range product and reverse-order-law development.
- The Friedrichs-angle and closed-sum literature already audited in AF-039 supplies the two-subspace equivalences used to rewrite the product criterion as `\tau(M,N)>0` and `c(M,N)<1` in the exact-fidelity case.

The Arithmetic Fidelity contribution is therefore not a new theorem about products of Hilbert-space operators. It is the **composition audit** obtained by placing this classical geometry after AF-001 and AF-039/040: exact survival composes by a range–kernel intersection test, while stable survival composes only with a quantitative transversality margin. The explicit graph/quotient control isolates a failure mode especially relevant to asymptotic compression arguments: each stage can be stable in isolation while their relative geometry makes the chain arbitrarily unstable.

## Boundaries and failure modes

- The stable equivalence above assumes `A` is bounded below and `B` has closed range. If `A` already has nonclosed range or `B` has zero reduced minimum modulus, instability may be intrinsic to one stage before relative transversality is considered.
- Exact fidelity needs only `M\cap N=\{0\}`. Closedness of `M+N` is a quantitative/topological condition and must not be smuggled into an exact collision claim.
- The identity `\tau=\sqrt{1-c^2}` is stated after exact intersection has been removed. With nontrivial intersection, the Friedrichs angle uses reduced subspaces while the un-reduced transversality modulus is already zero because exact fidelity fails.
- Stability depends on the norms/topologies used at the source and destination. Renorming a space can change the quantitative modulus even when the exact fiber relation is unchanged.
- The quotient specialization assumes the actual destination retains the Hilbert quotient, equivalently the orthogonal `N^\perp` representative. A scalar norm, trace, spectrum, determinant, or other summary of that quotient is a further compression requiring its own audit.
- A later stage can restore stability only by receiving genuinely additional information or by restricting the admissible source class so that the bad near-kernel sequence is excluded by an independent theorem. A deterministic post-processing of the same unstable destination cannot create a bounded inverse for the lost metric separation.
- The theorem is linear/Hilbertian. Nonlinear maps may need tangent, metric-regularity, inverse-function, or other category-specific notions of transversality.
- The graph example is a structural control, not an arithmetic model and not evidence for RH. An arithmetic application must identify the actual carrier range, downstream null directions, and natural norms before invoking the criterion.

## Decisive audit test

For any proposed multi-stage compression

\[
X\xrightarrow{A}Y\xrightarrow{B}Z
\]

whose relevant retained structure has a Hilbert-linear realization:

1. identify the exact subspace `M=Ran A` carrying the discriminator at the intermediate layer;
2. identify the exact downstream kernel `N=ker B` rather than only the behavior of `B` on its preferred support;
3. test `M\cap N` first; a nonzero intersection is an exact fidelity failure;
4. if the intersection is zero, compute or bound `\tau(M,N)` or the corresponding Friedrichs angle;
5. under truncation, continuation, thermodynamic limits, or asymptotic passage, require a **uniform** positive transversality bound;
6. reject an argument that cites only separate conditioning of `A` and `B` while leaving the range–kernel geometry uncontrolled.

For Arithmetic Fidelity, this supplies a genuine composition law: exact losses are governed by fibers/intersections, while stable losses are governed by how closely the surviving intermediate representation approaches the next stage's forgotten directions.