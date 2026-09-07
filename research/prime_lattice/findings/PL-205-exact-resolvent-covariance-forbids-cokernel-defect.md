# PL-205 — Exact fiberwise resolvent covariance forbids prime-edge cokernel defects

**Status:** negative result / structural collapse  
**Evidence class:** `EXACT-DERIVED + CLASSICAL-OPERATOR-LEMMA + DECISIVE-NEGATIVE` for bounded fiberwise exact-resolvent transport  
**Research line:** `prime_lattice`

## Claim

The cokernel/range-defect escape left open by `PL-203` is unavailable inside the bounded **fiberwise exact self-adjoint resolvent-covariance** architecture.

Let

\[
\Gamma=\mathbb N_0^{(\mathcal P)}
\]

be the prime-exponent lattice, let \(\mathcal K\) be a Hilbert space, and let

\[
H_\alpha=H_\alpha^*
\]

be densely defined self-adjoint operators on \(\mathcal K\). Fix \(z\in\mathbb C\setminus\mathbb R\) and write

\[
R_\alpha=(H_\alpha-z)^{-1}.
\]

Suppose that for every prime \(p\) and every vertex \(\alpha\) there is a bounded edge operator

\[
A_p(\alpha)\in\mathcal B(\mathcal K)
\]

such that the exact fiber covariance relation holds:

\[
\boxed{
R_{\alpha+e_p}=A_p(\alpha)R_\alpha.
}
\]

Then every edge operator has dense range:

\[
\boxed{
\overline{\operatorname{Ran}A_p(\alpha)}=\mathcal K.
}
\]

Equivalently,

\[
\boxed{
\ker A_p(\alpha)^*=\{0\}.
}
\]

Consequently any proposed prime-edge singularity whose load-bearing datum is a nonzero Hilbert-space cokernel, a proper closed range, or a missing closed support sector is incompatible with exact bounded fiberwise self-adjoint resolvent covariance. In particular:

\[
\boxed{
\operatorname{Ran}A_p(\alpha)\text{ closed}
\Longrightarrow
A_p(\alpha)\text{ surjective},
}
\]

and if an edge operator is an isometry, then its range is closed, so it is automatically unitary. Thus a unilateral-shift-type **isometric one-sided defect** cannot be the missing prime-lattice rigidity while this exact covariance architecture is retained.

This sharpens `PL-203`. That finding showed that injective dense-range non-surjective edge weights remain fully programmable and therefore that noninvertibility alone is useless. The present result shows why its example had to use dense-range singularity: exact self-adjoint resolvent covariance itself forces density of every bounded edge range. A genuine cokernel or proper closed-range defect is not merely non-rigid here; it is impossible.

## 1. Self-adjoint resolvents have dense range

For a self-adjoint operator \(H_\alpha\) and nonreal \(z\), the resolvent

\[
R_\alpha=(H_\alpha-z)^{-1}
\]

is bounded on \(\mathcal K\), injective, and satisfies

\[
\operatorname{Ran}R_\alpha=\operatorname{Dom}H_\alpha.
\]

Because a self-adjoint operator is densely defined,

\[
\overline{\operatorname{Ran}R_\alpha}=\mathcal K.
\]

The same holds at the neighboring vertex:

\[
\overline{\operatorname{Ran}R_{\alpha+e_p}}=\mathcal K.
\]

No compactness, semiboundedness, spectral discreteness, or zeta-specific hypothesis is used.

## 2. Exact fiber covariance forces dense edge range

From

\[
R_{\alpha+e_p}=A_p(\alpha)R_\alpha
\]

we obtain

\[
\operatorname{Ran}R_{\alpha+e_p}
=A_p(\alpha)\operatorname{Ran}R_\alpha
\subseteq
\operatorname{Ran}A_p(\alpha).
\]

The left-hand side is dense in \(\mathcal K\). Hence the range of \(A_p(\alpha)\) contains a dense subset, and therefore

\[
\boxed{
\overline{\operatorname{Ran}A_p(\alpha)}=\mathcal K.
}
\]

Equivalently, by the standard Hilbert-space identity

\[
\overline{\operatorname{Ran}A}
=(\ker A^*)^\perp,
\]

we have

\[
\boxed{
\ker A_p(\alpha)^*=\{0\}.
}
\]

This is an edge-by-edge statement. It is stronger for the present weighted-fiber architecture than the global dense-range observation in `PL-198`: there the common resolvent intertwiner forces polynomial relations on the target prime tuple, whereas here the coordinatewise resolvent factorization forces the **individual fiber edge operators themselves** to have no cokernel mode.

## 3. Closed-range and isometric defects collapse

If \(A_p(\alpha)\) has closed range, then dense range gives

\[
\operatorname{Ran}A_p(\alpha)=\mathcal K.
\]

Thus every closed-range edge satisfying the exact covariance is surjective. In particular, a Fredholm edge can have no cokernel:

\[
\operatorname{coker}A_p(\alpha)=0.
\]

The same kills the most canonical one-sided-shift repair. An isometry \(V\) has closed range because

\[
\|Vx\|=\|x\|
\]

makes the range complete. Therefore an isometric edge satisfying the covariance is surjective and hence unitary:

\[
\boxed{
A_p(\alpha)^*A_p(\alpha)=I
\quad\Longrightarrow\quad
A_p(\alpha)A_p(\alpha)^*=I.
}
\]

If all prime edges are isometries, the hoped-for unilateral defect disappears before any zeta input enters. Combined with the exact-commutation/gauge results of `PL-197`--`PL-198`, this means that replacing the canonical prime shifts by bounded fiberwise isometries cannot create an RH-sensitive defect through a missing range sector while keeping one exact self-adjoint resolvent transport.

A general partial isometry is different: dense range forces its final space to be all of \(\mathcal K\), so it becomes a coisometry, but it may still have a kernel. The theorem therefore eliminates **cokernel-side** one-sidedness, not every possible kernel-side singularity.

## 4. Why PL-203's dense-range singular tail is the sharp control

`PL-203` constructs edge weights with a diagonal tail

\[
a_d(k)=\frac{k^{d+1}-i}{k^{d+2}-i}\sim\frac1k,
\]

which is injective, dense-range, non-surjective, and not bounded below. At first sight that example left both kernel and cokernel/range defects as possible stronger singular repairs.

The present lemma shows that the range behavior of that control is not accidental. Any bounded edge participating in the same exact fiberwise self-adjoint resolvent factorization must have dense range. Hence the next singular mechanism cannot be obtained by replacing the dense-range tail with an ordinary unilateral shift, a proper support projection, an isometric embedding into a proper closed subspace, or any other bounded closed-range operator with nonzero cokernel.

What remains possible is more specific:

- a bounded dense-range edge with a nontrivial kernel;
- a coisometric or otherwise kernel-bearing edge whose range is all of \(\mathcal K\);
- nonclosed dense-range singularity of the type already controlled by `PL-203`, but with additional arithmetically forced structure not supplied by the generic tail;
- an unbounded or genuinely domain-sensitive transport for which the bounded-continuity argument above no longer applies;
- approximate or ideal-valued covariance rather than exact equality;
- a target-relative architecture that does not decompose into the fiber identity \(R_{\alpha+e_p}=A_p(\alpha)R_\alpha\).

Dense range by itself does **not** imply injectivity of a bounded operator. The proof above therefore cannot be inverted to claim that exact covariance forces the edge weights to be one-to-one. That distinction is load-bearing: the surviving singular question, if pursued, must place real arithmetic content in a kernel/domain defect rather than merely in failure of bounded invertibility.

## 5. Prior art and novelty audit

The abstract functional-analysis ingredients are classical. The identities

\[
\operatorname{Ran}(H-z)^{-1}=\operatorname{Dom}H
\]

for a closed densely defined operator at a resolvent point and

\[
\overline{\operatorname{Ran}A}=(\ker A^*)^\perp
\]

for bounded Hilbert-space operators are standard. Classical operator-range theory, including Fillmore--Williams, *On Operator Ranges*, Advances in Mathematics **7** (1971), 254--281, DOI `10.1016/S0001-8708(71)80006-3`, and Douglas's range-inclusion/factorization theorem, provides the surrounding literature. No novelty is claimed for the abstract range lemma.

The durable delta is line-specific and exact. `PL-203` explicitly left an actual cokernel/range defect among the singular structures that might evade its programmability control. Once the same exact fiberwise self-adjoint resolvent equation is retained, that escape is impossible by a two-line range argument. The result therefore removes a live operator-design branch rather than introducing a new general theorem.

The literature audit found no reason to reinterpret this as an RH mechanism. Operator-range theory supplies abundant proper dense ranges; it does not impose rational-prime arithmetic or critical-line localization. The prime-lattice significance lies solely in narrowing which singular edge data can coexist with the already-used exact resolvent architecture.

## 6. Boundary conditions and adversarial checks

### Boundedness of the edge operator is load-bearing

The proof uses the bounded operator \(A_p(\alpha)\) as an everywhere-defined map on the fiber. With an unbounded or partially defined transport, the composition domain and closure of the image require separate analysis. The finding makes no claim about that regime.

### Exact fiberwise equality is stronger than an approximate relation

If

\[
R_{\alpha+e_p}-A_p(\alpha)R_\alpha
\]

is merely compact, Schatten, small in norm, or asymptotically small, the exact range inclusion used above disappears. No corresponding dense-range conclusion is asserted.

### A global intertwiner alone is not enough

The result is not the statement that every target prime operator in

\[
RV_p=T_pR
\]

must have dense range. The canonical source shift \(V_p\) itself has a proper closed range on the full lattice Hilbert space. The conclusion concerns the **fiber weight** \(A_p(\alpha)\) only when the global weighted-shift equation decomposes coordinatewise into the displayed resolvent identity.

### Dense range does not kill kernel defects

The implication

\[
\overline{\operatorname{Ran}A}=\mathcal K
\Longrightarrow
\ker A=\{0\}
\]

is false in general. The theorem only gives \(\ker A^*=0\). A kernel-bearing surjective/coisometric edge is therefore not excluded by this argument. Any later attempt to close that regime must use an additional hypothesis rather than silently treating dense range as invertibility.

### No analytic continuation or Euler product is involved

The result is pure operator theory applied to the prime-exponent indexing. It neither evaluates nor analytically continues a zeta Euler product, and it supplies no zero localization by itself.

## Falsification / audit test

The claim is falsified if one can exhibit a Hilbert space \(\mathcal K\), self-adjoint \(H_\alpha,H_{\alpha+e_p}\), a nonreal \(z\), and a bounded operator \(A_p(\alpha)\) with non-dense range such that

\[
(H_{\alpha+e_p}-z)^{-1}
=A_p(\alpha)(H_\alpha-z)^{-1}.
\]

Such an example would contradict the elementary range inclusion above. Apparent counterexamples must therefore be checked for one of the actual escape hypotheses: a non-self-adjoint or non-densely-defined target, an unbounded/partially defined edge map, approximate rather than exact covariance, or failure of the fiberwise factorization.

## Consequence for the research line

The singular prime-edge frontier after `PL-202`--`PL-204` is narrower than the current synthesis suggests. Within bounded fiberwise exact self-adjoint resolvent transport:

\[
\text{proper closed range / cokernel / isometric unilateral defect}
\quad\text{is impossible},
\]

while

\[
\text{proper dense range}
\]

is possible but already non-rigid by `PL-203`.

Thus the remaining singular operator route cannot obtain arithmetic rigidity merely by making a prime edge non-surjective. It must make a **kernel, domain, approximation defect, non-fiberwise target coupling, or other source-forced structure** mathematically load-bearing and then prove a target-specific sign, coercivity, trace, or localization statement that survives the programmability controls.