# MI-052 — Rankin--Selberg positive geometry fails at the Weil half-density even after canonical finite--archimedean tensor completion

**Evidence level:** exact synthesis from [WP-363](../../findings/WP-363-eisenstein-rankin-selberg-gram-collapses-at-critical-exponent-and-first-jet-is-indefinite.md), [WP-364](../../findings/WP-364-projective-rankin-selberg-geometry-fails-at-critical-zeros.md), and [WP-365](../../findings/WP-365-completed-rankin-selberg-tensor-gram-still-fails-at-critical-zeros.md). The Rankin--Selberg factorization, Bessel Mellin product and Fubini--Study geometry are classical ingredients; the Mathia content is the critical-survival/sign audit.

The failure of Eisenstein Rankin--Selberg positivity at the Weil exponent is not caused merely by omitting archimedean geometry or by choosing the wrong scalar normalization.

For real spectral parameters `r,u` and `s>1`, the finite Hecke coefficients form a genuine positive Gram. Its exact factorization contains four zeta factors divided by `zeta(2s)`. WP-363 shows that this common denominator forces the whole finite Gram to vanish at `s=1/2`, and the first nonzero critical jet is indefinite. WP-364 then removes the common scalar intrinsically by projectivization; the resulting normalized overlap still becomes unbounded near critical-line zeros and its Fubini--Study metric becomes negative with a double-pole divergence.

WP-365 adds the canonical independent archimedean Hilbert space. The Bessel kernel

`H_s(r,u)=int_0^infinity K_(ir)(x)K_(iu)(x)x^(s-1)dx`

is positive semidefinite for every `s>0` and has the classical four-Gamma Mellin factorization. Tensoring it with the finite Hecke Gram gives a positive kernel before continuation whose factorization is, up to a scalar,

`B_s(r+u)B_s(r-u)/Lambda(2s)`,

with `B_s(t)=|Lambda(s+it)|^2`. The finite and infinite places have therefore been combined **before** the scalar readout, and the archimedean factor is genuinely nonseparable in `(r,u)`.

Yet projectivization again leaves

`C_s(r,u)=B_s(r+u)B_s(r-u)/(B_s(0)sqrt(B_s(2r)B_s(2u)))`.

At `s=1/2`, any critical-line zero ordinate `gamma` makes the denominator vanish as `r->gamma/2` while the numerator remains nonzero for generic fixed `u`. Thus `|C_*|->infinity`, violating the normalized Gram bound `|C|<=1` on regular points arbitrarily near the zero. The Fubini--Study pullback likewise tends to `-infinity`. The Gamma factors are smooth and nonzero at those arithmetic zeros and cannot repair the sign.

The reusable lesson is stronger than “non-scalar positivity must survive critical specialization.” **Even tensoring independently positive finite and archimedean local feature spaces can fail if their completed product still packages the target divisor multiplicatively.** Local positivity plus canonical completion does not imply that the analytically continued global projective geometry remains Hilbert-positive.

A viable automorphic route must therefore change the nonseparable correlation law itself before critical specialization. Standard scalar completion, intrinsic projectivization, ordinary Whittaker normalization, or multiplying additional positive local Gram factors of the same product type cannot address a failure caused by zeros in the global completed factor. The missing ingredient must be genuinely noncentral/non-product—such as a source-forced interaction, remainder, intersection/cohomological form or orthogonal sector whose sign theorem is established independently of the divisor to be constrained.

**Boundary.** This does not rule out Maaß--Selberg remainder structures, enlarged automorphic spaces, cohomological positivity, noncentral operators or other global couplings that are not pointwise products of the tested local Grams. It rules out the canonical level-one Eisenstein coefficient Gram, its critical jet, scalar/projective repairs and the canonical positive Bessel tensor completion as the missing Weil-positive object. No RH implication follows.