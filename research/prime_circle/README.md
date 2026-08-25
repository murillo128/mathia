# Prime-circle geometry

This directory records research that starts from the **original regular-polygon / roots-of-unity construction**, before imposing the hyperbolic prime-flute model.

## Primary object

Let

\[
P_n=\mu_n=\{z\in\mathbb C:z^n=1\}
\]

be the vertices of the regular \(n\)-gon on a fixed circle, with the common vertex \(1\). The vertices that appear for the first time at level \(n\) are the primitive \(n\)-th roots

\[
P_n^*=\{\zeta:\operatorname{ord}(\zeta)=n\}.
\]

Thus

\[
P_n=\bigsqcup_{d\mid n}P_d^*,
\qquad |P_n^*|=\varphi(n).
\]

A prime \(p\) is characterized geometrically by

\[
P_p=P_1\sqcup P_p^*,
\]

so every non-common vertex of the \(p\)-gon is new.

## Research stance

The primary aim is to discover structures forced by this geometry itself: vertex collisions, chord distances, primitive/birth layers, logarithmic potentials, interior/exterior reciprocity, Fourier modes, scale renormalization, and interactions between layers.

Classical analytic-number-theory or spectral machinery is used mainly as a falsifier/novelty check after a candidate structure has been derived.

The hyperbolic prime-flute under `research/prime_flute/` is now treated as a secondary derived model rather than the central object.

## Evidence labels

- `EXACT-DERIVED`: exact consequence of the roots-of-unity geometry / elementary algebra.
- `CLASSICAL-IDENTITY`: exact but already standard in the literature.
- `CANDIDATE-NEW-STRUCTURE`: a new organization or operator suggested by the geometry; novelty not established.
- `NEGATIVE`: a proposed interpretation ruled out.
- `NEEDS-AUDIT`: requires source or proof verification.

## Current high-priority direction

Treat each primitive layer \(P_n^*\) as a boundary charge distribution and study its logarithmic potential

\[
U_n(z)=\sum_{\zeta\in P_n^*}\log|z-\zeta|=\log|\Phi_n(z)|.
\]

This construction simultaneously preserves the original circle geometry, the primitive/new-vertex decomposition, and an exact interior/exterior reciprocity. See `FINDINGS.md`.
