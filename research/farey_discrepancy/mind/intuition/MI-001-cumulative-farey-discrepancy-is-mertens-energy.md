# MI-001 — Linear Möbius ancestry creates a projective multiscale gap, not an absolute-energy gap

**Evidence level:** exact sparse-horizon saturation, linear-prefix Schur geometry, critical-line energy growth, and four-adic projective obstruction through FD-034

## Core intuition

The GCD-duality/Farey route has crossed from a free-model classification to its first unconditional normalized rigidity. Every sublinear prime-ancestry prefix remains compatible with square-root saturation, while linear breadth exposes a Schur-projective defect of the physical Mertens tail. Absolute transverse distance is not enough because the physical tail energy grows superlinearly, but square-divisor modes prevent the normalized defect from collapsing on every scale of a `4`-adic chain.

The surviving question is therefore not whether the physical tail differs from the equality ray, but whether its **projective alignment can persist on a cofinal set of horizons** despite the exact multiplicative renormalization obstruction.

## Strongest justified principle

FD-024--FD-030 establish the free boundary: exact squarefree/ternary source data and every `Y_H=o(H)` ancestry prefix can still saturate the sharp GCD-duality constant. FD-031 reduces linear-prefix saturation to alignment with one distinguished Schur direction.

FD-032 proves a macroscopic absolute mismatch because the equality direction vanishes on nonsquarefree coordinates while the physical Mertens tail is fixed on the terminal shell. FD-033 then shows that this does not imply a uniform angle: the Schur-tail energy has an exact quotient-shell representation, and Hardy's critical-line zeros force `E_{H,D}/H -> infinity` for every fixed head dimension. Thus the proposed absolute-energy bound `E=O(H)` is impossible and the normalized defect is the correct currency.

FD-034 extracts exactly such a normalized obstruction. Rows divisible by `4` carry a scaled copy of the same physical energy at `floor(H/4)`, forcing `epsilon_{H,D} >= (3/4) E_{floor(H/4),D}/E_{H,D}`. Iteration plus the elementary upper energy bound yields a positive geometric and Cesaro lower bound for `epsilon` along every `4`-adic chain. For half-linear ancestry this becomes an explicit strict average gap below `zeta(2)`.

## Program consequence

Exploit the multiplicative self-similarity rather than seek another absolute norm bound. Extend the square-divisor argument across several prime-square scales, prove that the forced defects have enough overlap to yield a pointwise or positive-density lower bound, or combine projective defect with the independent endpoint-reachability condition from FD-031. The target is a cofinal obstruction to saturation, not merely an average gap on one geometric subsequence.

## Counterevidence / boundary

FD-034 does not give a pointwise gap at every horizon and does not reach an RH-critical cancellation exponent. A sparse subsequence could still carry unusually small projective defect while compensating elsewhere on each `4`-adic chain. The argument also uses fixed bounded Schur-head dimension corresponding to fixed positive linear ancestry fraction; uniform behavior when that geometry changes requires separate control.

The superlinear energy in FD-033 is unconditional and must not be treated as evidence against the route; it only invalidates absolute-energy coercivity.

## Epistemic status

**Exact free boundary through all sublinear ancestry, exact linear Schur discriminator, and unconditional four-adic average projective gap; the remaining problem is to prevent sparse/cofinal projective saturation strongly enough to improve the Farey/Mertens target.**

## Falsification criterion

Construct a complete `4`-adic chain satisfying the FD-031 physical-tail geometry whose normalized Schur defects Cesaro-collapse to zero, or prove that the FD-034 renormalization cannot be extended into any cofinal/pointwise obstruction because a compatible sparse saturation mechanism exists.
