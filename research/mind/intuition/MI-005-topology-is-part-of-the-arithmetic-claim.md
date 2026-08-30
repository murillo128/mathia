# MI-005 — The topology of the limit is part of the arithmetic claim

**Evidence level:** supported by exact topology-sensitive obstructions in several branches

## Core intuition

Several Mathia constructions now carry the same underlying arithmetic/geometric perturbation into sharply different conclusions depending on the operator topology or completion. Strong limits can erase moving boundary states; norm and Calkin limits can preserve only essential recurrence; trace-class demands can fail for purely local microlocal reasons; ordinary Hilbert completions can be nonclosable; regular compact-resolvent completions can be structurally impossible. These are not technical afterthoughts. **Choosing the topology determines which information channel is even visible.**

## Strongest justified principle

Three branches give exact versions of the phenomenon.

- **Prime Lattice:** PL-050 has strong convergence to zero on every fixed window while moving boundary states retain order-one edges. PL-051 gives a universal PNT rank-one fixed-depth blow-up, whereas PL-052--PL-054 show an order-one norm/essential-norm obstruction and infinite-multiplicity partial reflections at prime-power thresholds. The same family is therefore trivial/universal strongly and nontrivial but non-Fredholm in the Calkin algebra.
- **Prime Flute:** increasingly strong pant/collar/gluing agreement with the composite clone coexists with a local theorem that the first relative resolvent cannot be trace class for any nonisometric smooth comparison (PF-112). Raw generator right limits are moreover gauge-dependent (PF-113). The unresolved tail question belongs specifically to compactness, `S_p` with `p>1`, higher resolvent powers, heat/wave, or scattering categories after a synchronized global identification.
- **Prime Circle / Weil Positivity:** the compatible solenoid carries exact-order labels, but regular commuting leaf/fiber operators have noncompact resolvent, while PC-069--PC-070 rule out ordinary compact-resolvent Hamiltonians under exact scalar affine dilation covariance. On the positivity side, the critical finite Gram selector becomes a nonclosable form on the natural Hilbert completion, while the Prime-Circle Weil birth term lives as a singular Haar tangent and disappears under ordinary positive radial/Schur completion (WP-032--WP-045).

The conclusion is not that weaker or singular topologies are better. It is that an RH claim must specify **why its topology is canonical for the arithmetic mechanism** and audit what universal or essential information survives there.

## Consequence for synthesis

A useful limit should occupy a narrow middle ground:

\[
\text{not so weak that the arithmetic escapes to moving states,}
\qquad
\text{not so strong that only essential/non-Fredholm spikes remain.}
\]

Relative determinants, spectral shift, mesoscopic smoothing, distributional boundary forms, or higher Schatten classes are legitimate candidates only when their category is forced independently of the desired zero signal. Moving to another topology solely because it reveals a preferred singularity is not evidence.

This intuition complements MI-001. MI-001 asks whether a transformation identifies the target variable; MI-005 asks **which completion/topology makes that identification continuous, compact, singular, or invisible**.

## Evidence against overgeneralization

Topology dependence is common in analysis and is not Mathia-specific novelty. The synthesis does not claim a universal “correct topology” for RH. It records that current exact controls invalidate arguments that silently move among strong, norm, Calkin, trace-class, Hilbert-form, and compact-resolvent categories as though they carried the same arithmetic content.

A noncompact or distributional construction may still be decisive if it comes with an independently justified spectral/sign theorem.

## Status / novelty

All topology separations cited above are persisted findings. Their cross-branch interpretation as a mandatory topology gate is a supported synthesis rather than a new operator theorem.

## Falsification criterion

Exhibit an audited family for which the claimed arithmetic invariant is provably topology-independent across the relevant strong/norm/essential/Schatten/completion categories, or derive a canonical topology from the geometry and prove that it retains a zero-selecting invariant while the matched controls vanish there. Either would sharpen or replace this principle.

## Lean-formalizable core

- Strong convergence with persistent norm/essential-norm lower bounds.
- Schatten-class separations for pseudodifferential resolvent differences.
- Nonclosability of rank-one critical forms.
- Compact-resolvent obstruction under dense rational-frequency and affine dilation covariance.
