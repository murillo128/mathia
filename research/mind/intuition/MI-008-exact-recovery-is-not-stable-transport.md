# MI-008 — Stable transport is relative to quotient, safe source geometry, scale, and continuum interface

**Evidence level:** supported by exact asymptotic fidelity controls through AF-177, analytic-frontier safe-cone conditioning controls through ANF-090, and exact Xi static/discrete renormalization controls through XF-089

## Core intuition

Exact recovery and tiny forward error remain insufficient, but stability is now more structured than a single condition number. It depends on the **maximal destination quotient, asymptotic scale, admissible source class, degree regime, safe/null directions of the destination geometry, and the exact continuous/discrete transport interface**.

Arithmetic Fidelity shows that the same complete inner-function representation can collapse on one growing source stratum and become uniformly invertible on another after the correct quotient and interpolation modulus are declared. ANF-090 supplies the complementary warning: a raw source condition number may diverge even on configurations that are exactly safe at the destination, so conditioning must itself be quotiented or calibrated to the dangerous geometry. Xi Flow shows that a discretization can become stable only after a source-fixed singular sector is removed with the correct mesh renormalization.

## Strongest justified principle

AF-169--AF-170 show exponential contraction of a regular fixed-radius divisor direction even for the complete finite Blaschke factor. AF-171 restores a uniform boundary-layer scale, AF-172 extends it to a complex cyclic parameter, and AF-173 identifies the intrinsic output metric after quotienting arbitrary unimodular phase. AF-174 gives the sharp unrestricted fixed-degree `1/n` inverse exponent.

AF-175 then shows that a degree-independent interpolation constant restores degree-independent local Lipschitz recovery. AF-176--AF-177 prove the necessity side: cyclic perturbations and then universal Frostman shifts force local inverse slope `1/(2 delta(B))`, while AF-175 gives upper scale `1/delta(B)`. Thus for the declared metrics `delta(B)` is the intrinsic local source regularity modulus up to factor two.

Analytic Frontier shows why the modulus must match the destination null space. ANF-089 gives a valid bound from the raw cross-metric ratio `chi_s=b_s/a` to separable distance. ANF-090 constructs exactly separable product families with exponentially divergent raw `chi_s`. The small source Gram eigenvalue there measures finite-difference ill-conditioning of a comparator, not dangerous nonseparability. The next meaningful conditioning theorem must remove safe separable directions before interpreting a large condition number.

Xi Flow supplies the source-class and discretization analogue. XF-084--XF-087 project the problem to destination-visible guarded moments, prove exact static equal-weight realization in the admissible cone, and identify the low-mode periodic heat vector field with the composite-trapezoid Volterra discretization. XF-088 shows that the raw endpoint pole invalidates a smooth quadrature comparison unless the forced `c log Delta delta_0` term is included. XF-089 proves that for Xi `c=1/4` is unchanged over positive heat time and that reference subtraction improves the residual by one Fourier factor. The remaining transport modulus is therefore a guarded estimate for that residual, not a new root-dynamics or leading-pole problem.

## Program consequence

For every source-to-destination bridge, declare the destination equivalence relation and norm; safe/null directions; asymptotic normalization; degree or complexity regime; source regularity/admissibility modulus; and any source-fixed counterterm or continuum/discrete consistency estimate required to connect the source evolution to the realized finite state. A restricted class, quotient, rescaling, or renormalization is legitimate only when forced by the source or downstream theorem.

Do not treat a large raw condition number as instability until its near-null direction is shown to retain destination mass, and do not treat a singular discretization error as source information until the deterministic singular sector has been removed in the canonical normalization.

## Counterevidence / boundary

The factor-two Blaschke enclosure is local and metric-specific. ANF-090 does not yet construct a quotient-aware conditioning theorem, and the separable cone is nonlinear. XF-088--XF-089 classify only the leading endpoint singular sector; lower-order residual control remains open.

These examples do not imply that every ill-conditioned representation has a canonical good quotient or every continuum problem has a stable renormalized discretization.

## Epistemic status

The component statements are persisted exact/literature-backed mathematics. The cross-line principle is supported synthesis, not an RH theorem.

## Falsification criterion

Produce uniform source-to-destination recovery while every destination-calibrated source modulus degenerates, show that ANF-090's safe family becomes dangerous after the exact destination quotient, or violate the XF endpoint counterterm/residue statements in their proved regimes. More broadly, a source-forced theorem that remains uniformly stable without specifying quotient, safe directions, scale, source class, degree regime, or the relevant continuum interface would narrow this synthesis.