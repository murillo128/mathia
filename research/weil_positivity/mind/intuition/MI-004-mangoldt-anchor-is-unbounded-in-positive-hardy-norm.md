# MI-004 — Pointed topology repairs the Mangoldt anchor, but positive finite and archimedean pieces still fail to couple with the Weil sign

**Evidence level:** supported by exact positive constructions and exact compatibility obstructions

## Core intuition

The Mangoldt selector is not intrinsically incompatible with positive Hilbert geometry. It is incompatible with the original rotation-invariant Hardy topology. Once the canonical base point is built into the metric, the selector becomes continuous and the intrinsic power maps force both the critical half-weight and a positive logarithmic scale defect. The remaining failure is more informative: the positive finite-place package still does not assemble with the signed Weil multiplier and the archimedean shift without an indefinite subtraction or coefficient contamination.

## Strongest justified principle

WP-067--WP-069 establish the original topology obstruction. The Hardy shell form recovers `Lambda(n)` algebraically, but the full-root controls give a null sequence on which the anchor stays equal to one. No finite scalar counterterm or regular positive auxiliary extension preserving that finite Hardy energy can represent the anchor by a finite-energy vector.

WP-070--WP-071 show that obvious symmetric repairs do not help. The canonical antipodal `q=2` positive correction remains blind to the normalized odd full-root controls, and in fact **every** positive rotation-invariant Hilbert completion with bounded evaluation at `1` excludes every nontrivial cyclotomic logarithm. The obstruction is therefore to rotation-invariant topology, not to positive realization as such.

WP-072 supplies the positive survivor. The canonical base-point local Dirichlet energy
`D_1(F)=||(F-F(1))/(z-1)||_{H^2}^2`
contains every cyclotomic shell, makes `F(1)=Lambda(n)` bounded, and is positive definite on the shell span. This is not a fitted point: `1` is already the distinguished base-shell point.

WP-073 then derives the critical attenuation internally. Composition by the intrinsic degree-`n` power map multiplies `D_1` by `n`, so `n^{-1/2}C_n` is the unique positive isometric normalization. The boundary representer is an adjoint eigenvector with eigenvalue `n^{-1/2}`, giving the exact `Lambda(n)/sqrt(n)` scale. This is a canonical **critical half-weight**, but still not zero selection.

WP-074 adds a second positive structure from the same cover geometry. The uniquely covariant half-integer number operator produces a positive trace-class inverse-scale defect with trace `log n`; on a primitive prime ray its Gram kernel has first row `(log p)p^{-k/2}`. Thus both factors in the finite Weil prime-power weight can be forced positively before analytic continuation. But converting the positive Poisson kernel into the actual finite Weil multiplier requires the sign-changing subtraction `1-P_r`.

WP-075 makes the finite/archimedean incompatibility exact. Positive shifted-resolvent defects mix `log n` with a digamma difference, but the exact finite coefficient remains `log n` for every degree only at zero shift, precisely where the digamma contribution disappears. Inside this canonical positive family, turning on the archimedean spectral shift necessarily contaminates the finite prime coefficient.

The present boundary is therefore not “find a positive norm containing the selector.” That has been done. It is **derive one global positive/sign-producing operation that couples the pointed finite package to the archimedean/polar terms without performing the known indefinite subtraction and without altering the exact finite coefficients**.

## What remains possible

A nonseparable finite--archimedean construction could couple the two sectors before either is reduced to a Poisson kernel or shifted resolvent trace. A singular boundary/intersection/cohomological form may also lie outside the scalar positive families classified so far. Any such mechanism must keep the `D_1`-level selector continuous, retain the forced half-density/log-degree data, and supply its own sign theorem.

Choosing a different shift because it resembles the Gamma factor, or subtracting the positive Poisson kernel from the identity after the fact, does not qualify.

## Status / novelty

Local Dirichlet positivity, composition-operator scaling, Jensen/resolvent positivity, and digamma trace formulas use classical functional analysis. Their exact specialization to the Mathia shell/cover data is persisted evidence. The synthesis is a supported finite-versus-global compatibility gate, not a Weil-positivity proof.

## Falsification criterion

Construct within the audited pointed-cover positive family a nonzero archimedean shift that preserves the exact finite `log p` weights, contradicting WP-075, or show that the pointed Dirichlet anchor is unbounded despite WP-072. A positive advance should instead derive a new global coupling outside the separated positive Poisson/resolvent architecture and prove its sign independently.

## Lean-formalizable core

- Boundedness of boundary evaluation in the pointed Dirichlet norm.
- Exact degree scaling and unique `n^{-1/2}` isometric normalization.
- Positivity/trace of the inverse-scale defect.
- Uniqueness of zero shift for exact finite log-degree coefficients.
