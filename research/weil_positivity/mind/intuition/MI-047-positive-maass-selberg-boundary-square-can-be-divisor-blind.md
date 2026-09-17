# MI-047 — A positive Maaß--Selberg boundary square can be divisor-blind

**Evidence level:** exact/literature-backed synthesis from [WP-237](../../findings/WP-237-arthur-height-operations-cannot-isolate-the-zeta-zero-block.md), [WP-287](../../findings/WP-287-nonlinear-height-postprocessing-does-not-escape-linear-weil-distribution.md), and [WP-345](../../findings/WP-345-maass-selberg-height-derivative-is-a-positive-boundary-square-but-does-not-constrain-the-scattering-divisor.md).

The rank-one Maaß--Selberg relation supplies a genuine source-defined positive object. If `N_T(r)` is the truncated Eisenstein norm and `tau=log T`, then on the unitary axis

`partial_tau N_(e^tau)(r) = |1+S(r)e^(-ir tau)|^2 >= 0`.

This is stronger than a formal positivity rewrite: it is the actual logarithmic-height derivative of a geometric Hilbert norm. But the same operation deletes the `T`-independent logarithmic-derivative term `m'/m` whose explicit-formula decomposition carries the zero divisor together with prime and archimedean contributions. The sign-visible boundary response and the divisor-sensitive carrier live in different pieces of the Maaß--Selberg formula.

WP-345 gives a decisive matched control. Multiply a scalar meromorphic scattering function by an inner/CDD factor that preserves reciprocal symmetry and unitary-axis modulus while inserting an off-axis zero/pole pair. Every boundary-square inequality remains true because it depends only on the unitary boundary phase, while the logarithmic derivative changes by the added divisor term. Thus **positivity of the direct height boundary square is insensitive to exactly the divisor motion a Weil mechanism must constrain**.

The control does not say that an arbitrary CDD-modified scalar is automorphically realizable. That is the surviving place for genuine source structure. A successful Maaß--Selberg route must use a theorem about the full finite part, automorphic realizability, Euler--Gamma coupling, or operator-level truncation that excludes the divisor-changing control before scalar boundary positivity is taken.

This sharpens the scalarization audit. A source-derived positive square is not automatically selective merely because it comes from the correct global geometric object. One must test whether the sign theorem survives deformations that preserve the hypotheses used by the positivity argument while changing the target divisor. If it does, the positive object is a matched control rather than a zero-selection mechanism.

The lesson is complementary to the fixed-boundary-state obstruction of MI-046. There the desired quadratic form was already encoded in a common scalar boundary readout. Here the positive boundary response is genuinely source-derived, but its sign is **too universal**: inner-factor freedom can move the meromorphic divisor without changing the square theorem.

**Boundary.** The CDD factor is a meromorphic matched control, not a proof that the modified function occurs as an automorphic scattering matrix or that the full modified Maaß--Selberg norm is positive for every truncation. WP-345 therefore leaves open a source-realizability theorem using the complete finite part, and operator-level finite--archimedean couplings before scalarization. It rules out only the direct inference from height-boundary positivity itself to Weil positivity.