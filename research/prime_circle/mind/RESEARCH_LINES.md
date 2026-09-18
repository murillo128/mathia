# Prime-circle research lines

This file holds the current mathematical questions suggested by the durable prime-circle intuitions. It is not a roadmap, task queue, status page, or history.

## Demand a destination theorem after scalar Mellin closure

**Linked intuitions:** `MI-040-endpoint-mellin-singularities-form-a-classical-von-mangoldt-jet` through `MI-044-full-shell-finite-measure-nullspace-is-only-the-universal-zeta-factor`.

PC-335--PC-343 classify the scalar finite-measure Mellin route. Prime-log interpolation depends on strip width and growth class; full-plane analyticity alone permits infinite-order survivors; but the full shell observation family is much stronger. Divisor inversion promotes the interpolation set to all integer logarithms, whose density is incompatible with the Gamma-controlled boundary growth of a finite Mellin measure. The resulting nullspace is exactly the already-explicit common zeta-zero support. Complete scalar observation therefore closes the interpolation escape by reconstructing classical zeta structure rather than by selecting its zeros.

PC-344--PC-346 sharpen that closure distributionally. The full-shell tempered Mellin kernel is a finite collection of zeta-zero jets, with a sharp Gamma-strip threshold deciding which jets act continuously on the chosen test space. Finite linear Hilbert/matrix lifts inherit the same threshold. Enlarging the scalar channel by a finite linear package therefore does not escape the analytic boundary; it only repackages the same zeta-divisor data.

## Find a strict arithmetic quotient of the faithful all-depth inversion defect

**Linked intuition:** `MI-045-reciprocity-closed-signature-is-abelian-trivial-and-rank-two-at-first-lie-level`.

PC-347--PC-348 move outside the finite linear class. Finite radial-flux Chen truncations remain cyclotomic/finite-level objects, while the full radial Chen signature is faithful to the shell path and its abelianization recovers the Mangoldt shell data.

PC-349 tests reciprocity closure. The closed signature has trivial abelianization, so every commutative character and finite-dimensional determinant sees the identity. Its first nonzero Lie term is a decomposable antisymmetric area matrix of rank at most two,

`A_mn = zeta(2) phi(m) phi(n) (g_n-g_m)`,

with `g_n=mu(rad n) rad(n)/n^2`. That low-rank collapse is kinematic for any reciprocal path with one asymptotic direction.

PC-350 resolves the remaining raw-depth ambiguity. Center each shell against the canonical shell `2`, `W_n=X_n-phi(n)X_2`, and evaluate the regularized defect in a `2x2` solvable family with parameter `lambda`. The upper-right entry is

`V_n(lambda)=int_0^infinity (1+r)^lambda dW_n(r)`.

On the imaginary axis reciprocity turns this into a Fourier--Stieltjes transform whose two pushforward pieces have disjoint supports on either side of `log 2`. Fourier uniqueness therefore recovers `dW_n`, hence the complete centered radial profile. The repeated-shell-`2`/one-transverse word sector already suffices: the first Lie area `A_(2n)` is just `V_n'(0)`, while all depths reconstruct the source lost at first order.

This is a decisive negative for **raw unbounded depth as a selector**. The same decoder works for broad non-arithmetic reciprocal paths with one calibration coordinate. Full noncommutative depth is therefore another lossless source encoding, not an RH discriminator.

The surviving question is now stricter: identify a **proper geometry-forced quotient or invariant** of the faithful defect, or a growing-conductor law on its coefficients, whose destination theorem is independently zero-sensitive and whose value cannot be reproduced by the reciprocal matched-control class. Merely keeping more words, taking unbounded degree, or demonstrating faithfulness is already classified.

## Keep source recovery, nonlinear completeness and zero selection separate

Prime Circle now exhibits linear completeness, nonlinear completeness and two complementary reciprocity facts. Full-shell finite-measure Mellin data collapses to the universal zeta factor; the full Chen signature reconstructs the radial path; reciprocity closure kills the abelian channel and makes the first Lie correction rank two; yet PC-350 shows that the complete closed defect is again faithful at all depths.

These are not contradictory. Low-order quotienting can erase most source information while the full tower restores it. The relevant audit is therefore not the rank of one graded layer or the faithfulness of the whole signature, but whether a **strict intermediate quotient** survives that is both source-forced and destination-selective.

The next route should state the zero-sensitive destination first, identify exactly which quotient of source/path information it needs, and prove that the proposed observation retains that quotient while matched reciprocal controls do not. Larger matrices, higher fixed Chen degree, unbounded raw depth or exact source reconstruction count only when the surviving invariant is independently coupled to the Riemann zero restriction.