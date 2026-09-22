# MI-067 — Rational orientation is priced by intrinsic derivative, not syntax conditioning

**Evidence level:** exact function-level refinement from [VIS-374](../../findings/VIS-374-near-degenerate-gram-clusters-have-small-bounded-metric-spectral-leverage.md), [VIS-377](../../findings/VIS-377-bounded-rational-operator-calculus-inherits-gram-noncommutativity.md), and [VIS-378](../../findings/VIS-378-rational-orientation-is-controlled-by-intrinsic-free-derivative.md), refining the expression-level budget of MI-066.

VIS-377 correctly shows how Gram orientation propagates through one chosen finite rational expression: inverse nodes can amplify commutators by squared inverse norms. VIS-378 identifies the representation-independent quotient of that bookkeeping. For a noncommutative rational function `R` evaluated at an external operator tuple `H=(H_1,...,H_r)`, simultaneous-similarity covariance gives the exact tangent identity

`D R_H([G,H_1],...,[G,H_r]) = [G,R(H)]`.

If `L_R(H)` is the operator norm of this Fréchet derivative from tuple Frobenius norm to Frobenius norm, then

`||[G,R(H)]||_F <= L_R(H) (sum_j ||[G,H_j]||_F^2)^(1/2)`.

The intrinsic amplification resource is therefore the local sensitivity of the represented rational map, not the condition number of an arbitrary syntax tree. Intermediate inverse norms remain useful sufficient bounds, but removable poles are automatically discarded: an expression such as `X^(-1)X` can contain an arbitrarily ill-conditioned inverse while representing the constant map `I`, whose derivative and output commutator vanish exactly.

Genuine poles survive this quotient because they make the function itself sensitive. For a resolvent `(zI-H)^(-1)`, the derivative recovers the familiar squared resolvent tax. More generally, if generator orientation tends to zero while the output retains order-one Gram orientation, then the intrinsic derivative norm must diverge along a subsequence. That divergence may come from a genuine singular boundary, growing rational family, changing dimension, or another controlled degeneration; it cannot be credited merely because one formula uses a badly conditioned inverse.

Composed with VIS-374, the destination ledger becomes fully intrinsic: generator commutators supply the orientation input, `L_R(H)` supplies function-level amplification, and Gram gaps, cluster widths and positive-metric bounds determine how much of that orientation changes the Wang singular spectrum. Rational identities and implementation conditioning that disappear before this ledger are representation artifacts.

**Boundary.** The derivative control is finite-dimensional and local. It does not classify unbounded operators, singular limits with changing domains, infinite-dimensional limits, growing rational complexity, indefinite forms or nonlinear source-dependent geometry. A diverging derivative is only a paid orientation resource; provenance and destination usefulness remain separate gates.