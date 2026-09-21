# MI-058 — One inner scale reprices weighted Gram collapse by balanced Hermite depth

**Evidence level:** exact fixed-depth multiscale synthesis from [VIS-362](../../findings/VIS-362-one-inner-scale-weighted-support-exponent.md), continuing the weighted-Gram boundary in VIS-361.

Suppose a fixed-depth Wang bank has already collapsed at its outer normalized scale onto `L<q` separated weighted support points, but every outer point retains a positive fraction of the total mass and resolves a uniformly nondegenerate local polynomial cloud after one finer rescaling by `epsilon`. Then the outer Gram degeneracy is not an unpriced cancellation resource.

Writing `M` for the total weight, `rho` for the outer width and

`h=floor((q-1)/L)`,

VIS-362 proves the sharp law

`s_q(A_w) asymp sqrt(M) rho^(q-1) epsilon^h`.

Equivalently, the smallest eigenvalue of the normalized weighted polynomial-sampling Gram is `asymp epsilon^(2h)`. The exponent is the balanced Hermite depth needed to recover the polynomial modes lost when only `L` outer values remain visible.

The mechanism is explicit. Taylor expansion converts each inner cloud into value and derivative jets at its outer center; value data cost order one, first derivatives cost `epsilon`, and successive jets cost higher powers. Distributing the `q` interpolation conditions across the `L` separated centers makes the deepest necessary derivative order exactly `h`. A polynomial whose zeros are balanced across the same centers gives the matching upper bound, so the exponent is not an artifact of the proof.

Thus the first positive weighted hierarchical degeneration is fully priced. A further compact escape must make some outer mass fraction vanish, let a local weighted Gram degenerate again, introduce a deeper nested scale in deficient modes, change the asymptotic depth or compactness regime, or leave the positive diagonal Hilbert geometry. Merely observing an outer Gram eigenvalue tending to zero is no longer enough.

**Boundary.** VIS-362 treats one common finer scale with separated outer centers, nonvanishing cluster masses and uniformly healthy local weighted Grams. It does not classify arbitrary recursive cluster trees, vanishing-mass hierarchies, growing `q`, noncompact scales, non-diagonal/indefinite coefficient metrics or signed arithmetic source gains.