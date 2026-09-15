# MI-004 — Rational-prime specificity depends on the retained analytic layer and admissible global class

**Evidence level:** supported by exact analytic fiber classifications, matched controls, and the Riesz/Mellin singularity gate in [AF-350](../../findings/AF-350-riesz-error-exponent-is-a-dirichlet-singularity-gate.md)

## Core intuition

“Contains primes” is not a stable fidelity statement, and neither is “contains the zero set.” The bare multiplicative source, the exact Euler product, the exact logarithmic derivative, meromorphic principal parts in a specified half-plane, and the zero/pole divisor are different information layers. A later global analytic restriction can also shrink a broad same-divisor fiber, but only when that restriction is independently part of the admitted object rather than imposed after the desired target is known.

## Strongest justified principle

AF-015 computes the symmetry boundary of the bare multiplicative monoid: it remembers atomhood and factorization shape while forgetting the ordinary assignments `p`, `log p`, and prime order. AF-017 then shows that, in an absolute-convergence half-plane, the exact Euler-product function determines the unordered generator-norm multiset, whereas the meromorphic divisor can lose it through a zero-free factor.

AF-019 inserts the exact logarithmic derivative between those layers. Equality of `f'/f` determines a meromorphic function up to one nonzero scalar, and normalized Euler products remove that scalar intrinsically; by contrast, retaining only the polar principal parts of `f'/f` is exactly divisor data and discards the regular contribution of the zero-free factor. Thus the regular part of the logarithmic derivative is a genuine fidelity carrier rather than disposable analytic background.

AF-350 gives a quantitative version of the same hierarchy for the weak Riesz endpoint. For fixed integer order `r`, if two coefficient sources have Riesz profiles differing by `O(X^theta)`, then the Mellin identity forces the difference of their Dirichlet transforms to extend holomorphically to `Re s>theta`. Therefore the quotient by `O(X^theta)` may erase coefficients, support geometry, signs and local provenance, but it preserves every meromorphic principal part strictly to the right of the error line. For `c_n=Lambda(n)-1`, the transform is `-zeta'/zeta-zeta`; its pole at `s=1` cancels, while every nontrivial zeta zero remains a pole. Hence an `O(X^theta)` Riesz bound excludes zeros with `Re rho>theta`, and `O_epsilon(X^(1/2+epsilon))` for every `epsilon>0` implies RH. The weighted perfect-power controls do not contradict this: their Dirichlet-transform difference from unit mass is entire, so they already agree in the singularity class retained by the weak quotient.

AF-018 supplies the complementary rigidity direction. Inside the class of entire functions of order at most one, a common zero divisor leaves only an `e^{as+b}` ambiguity. A common reflection equation kills the linear slope and one nonzero normalization kills the remaining scale. For Riemann `xi`, the nontrivial zero divisor together with the independently admitted order-one class, reflection law, normalization, and completion convention therefore recovers the exact completed function. This is constraint-assisted recovery, not faithfulness of the raw divisor in an unrestricted category.

## What remains possible

A rational-prime-specific mechanism can survive at a compressed analytic layer when the retained layer still carries the discriminator actually needed. AF-350 makes this explicit: a weak amplitude quotient can be drastically nonfaithful to the source yet exactly faithful to singularities above a moving half-plane threshold. Conversely, a route that uses only residues or a zero divisor must not silently inherit the regular/zero-free information of the exact logarithmic derivative, and a route that needs a boundary singularity cannot infer it from control only in the open half-plane.

The audit is therefore category- and threshold-indexed:

`source -> exact analytic object -> exact log derivative -> half-plane principal-part class -> divisor`,

with any claimed reverse implication justified by an explicit fiber-rigidity theorem or a quantitative transform bound rather than provenance or symmetry alone.

## Status / novelty

Hadamard factorization, logarithmic-derivative recovery, the Riemann `xi` functional equation, Möbius inversion, the Mellin/Riesz continuation principle, and the Grosswald--Schnitzer controls are classical or persisted exact findings. The durable Arithmetic Fidelity contribution is the placement of these results into one explicit hierarchy of adjacent information layers and admissible-category fibers, with AF-350 calibrating the error exponent as a half-plane singularity-fidelity threshold.

## Falsification criterion

Exhibit two different normed prime systems or completed analytic objects with the same destination inside a category claimed to be faithful, or prove that an independently forced analytic class and normalization classify the full destination fiber and reconstruct the exact normalized Euler product. For the Riesz threshold statement, a counterexample would require `R_r[a-b](X)=O(X^theta)` while `A-B` retains a genuine meromorphic singularity in `Re s>theta`.

## Lean-formalizable core

- Equality of logarithmic derivatives implies equality modulo scale on a connected domain.
- Principal parts of `f'/f` equal divisor data.
- Order-one same-zero fiber `e^{as+b}` and its reduction by reflection and normalization.
- Möbius inversion from an exact normalized Euler product to the generator-norm multiset.
