# MI-066 — Rational operator orientation amplification pays inverse conditioning

**Evidence level:** exact finite-dimensional derivation from [VIS-377](../../findings/VIS-377-bounded-rational-operator-calculus-inherits-gram-noncommutativity.md), extending the polynomial/operator-calculus closure of MI-065 through inversion.

For the Wang Gram `G`, the commutator map `delta_G(X)=[G,X]` is a derivation. Addition and multiplication propagate generator-level orientation as in MI-065, while an inverse satisfies the exact identity

`[G,X^(-1)] = -X^(-1)[G,X]X^(-1)`.

Hence

`||[G,X^(-1)]||_F <= ||X^(-1)||_op^2 ||[G,X]||_F`.

By structural induction, every fixed finite noncommutative `*`-rational expression has an explicit orientation budget built from generator commutators, intermediate operator norms and squared inverse norms. If the expression tree is fixed and all those norms remain uniformly bounded, vanishing generator commutators still force the rational output commutator to vanish. Rational notation does not create a new Gram-orientation scale.

The genuine new possibility is therefore a paid singular limit. A denominator with smallest singular value `rho` can amplify inherited orientation only at a cost bounded by `rho^(-2)` at that inverse node. For a resolvent `(zI-H)^(-1)`, the same tax is `dist(z,spec(H))^(-2)`. Near-pole amplification is real, but its condition number is the resource; staying uniformly away from singularity remains in the same orientation class as the generators.

When the rational output is a bounded positive metric, VIS-374 then converts the resulting commutator budget into the existing resolved-gap/cluster spectral error. Thus a finite rational Wang construction escapes the commuting-preconditioning class only by substantial source-native generator orientation, growing expression complexity, diverging intermediate norms, near-singular inversion, or by leaving the bounded finite-dimensional positive-Hilbert category.

**Boundary.** VIS-377 does not classify unbounded operators, genuinely infinite-dimensional limits, growing rational complexity, singular limits whose domains are controlled, indefinite forms or nonlinear source-dependent geometry. It also does not make a near-pole construction arithmetic: provenance and the destination-level conditioning cost remain separate gates.