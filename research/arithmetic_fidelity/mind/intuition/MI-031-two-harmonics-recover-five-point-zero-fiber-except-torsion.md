# MI-031 — One complex invariant recovers the five-point zero shape, but not stably

**Evidence level:** exact for five unit-modulus points on the first-harmonic zero fiber through AF-314. The distinct-prime specialization is conditional on a hypothetical nonzero five-prime hit. No first-incidence theorem or uniform conditioning bound follows.

**Representation.** The source is one exact unordered phase multiset `Z={z_1,...,z_5}` on `S^1`, with multiplicity allowed and `s_1=sum_j z_j=0`. Shape means the quotient by permutation and one common `S^1` rotation; prime labels, absolute phase and the original time parameter are deliberately outside this quotient. The exact observations are the power sums `s_m=sum_j z_j^m`.

AF-313 gives the self-inversive/Newton relation

`s_3 = -(3/2) E conjugate(s_2)`, with `E=prod_j z_j in S^1`,

so `|s_3|=(3/2)|s_2|`, and `(s_2,s_3)` reconstructs the whole unordered multiset away from the common zero `s_2=s_3=0`; that exceptional fiber is exactly one rotated-regular-pentagon orbit. AF-314 removes the remaining common-phase gauge. Under `Z -> rho Z`, the pair transforms with weights `(2,3)`, hence the primitive Laurent invariant

`kappa(Z)=s_2(Z)^3/s_3(Z)^2`

is rotation-invariant whenever the pair is nonzero. The zero-fiber radial relation supplies the information that a generic weighted pair would lose: `|kappa|=(4/9)|s_2|`. Extending `kappa=0` on the regular-pentagon orbit is therefore continuous, and AF-314 proves that `kappa` is a complete invariant of the entire unordered rotation quotient.

Thus the two complex harmonics used by AF-313 are not the intrinsic post-incidence information cost. After quotienting the physically irrelevant common phase, **one complex coordinate is enough to recover the complete five-point shape**. The generic quotient is real two-dimensional, so this is dimension-tight among continuous Euclidean summaries, although it does not make `kappa` uniquely canonical or minimal for every algebraic/computational notion of cost.

For phases `z_j=p_j^(-it)` from five distinct rational primes, a hypothetical nonzero hit `F_P(t)=0` satisfies `F_P(2t),F_P(3t) != 0` by AF-312. Therefore

`kappa_P(t)=F_P(2t)^3/F_P(3t)^2`

is well-defined and recovers the complete unordered phase shape modulo common phase. It still does **not** recover prime labels, absolute phase, `t`, or the existence of the first exact hit.

The incidence/stability distinction remains load-bearing. Prime phases exclude the exact regular-pentagon orbit at nonzero time, but current evidence gives no positive lower bound on `|s_2|` at hypothetical prime hits. Reconstruction becomes singular as `kappa -> 0`, so exact quotient fidelity can coexist with arbitrarily bad conditioning. AF-314 therefore removes a post-incidence information-loss obstruction more sharply than AF-313 without touching the live first nontorsion-incidence problem.

**Research consequence.** Raw harmonic count can overstate representation complexity when observations carry a gauge action plus source-specific algebraic relations. For this five-point fiber the relevant information count is the dimension and separating power of the invariant quotient, not the number of observed harmonics. The next informative comparison is whether larger exact-zero fibers still admit one complex complete quotient invariant, or whether an additional independent invariant first appears before any arithmetic-lift information is used.