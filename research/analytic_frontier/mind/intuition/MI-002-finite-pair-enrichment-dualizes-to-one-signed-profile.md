# MI-002 — Universal scalar pair certificates are governed by finite-cluster stability, not only thermodynamic periodization

**Evidence level:** supported by ANF-003--ANF-005 and ANF-010--ANF-018

## Core intuition

Finite enrichment does not create new pair information when all channels are finally compressed into one translation-invariant scalar affine counting functional. Universal validity already forces a nonnegative compact-band spectral profile. The newer evidence closes the remaining thermodynamic shortcut: long duplicated lattices are only bulk controls, and the decisive deterministic floor is the **finite-particle stability constant** of the associated positive-type pair potential.

The scalar branch is therefore a sharp many-body stability problem. Passing every lattice-periodization test is not enough, because a finite boundary-relaxed cluster can bind below the thermodynamic lattice energy.

## Strongest justified principle

ANF-003--ANF-005 reduce finite global pair enrichments to one scalar support-one witness plus explicit normalization slack. ANF-010--ANF-012 then force the admissible compact-band profile `J` to satisfy `J>=0`; favorable out-of-band or signed spectral mass cannot be used by this universal affine class.

ANF-013--ANF-014 identify the thermodynamic duplicated-lattice floor `p(J)` and the exact Mellin lower bound `C(J)/p(J)>=1+3/pi^2`. ANF-015 strengthens that lattice floor strictly by using Möbius oscillation in the multiplicative packing dual, but only qualitatively.

ANF-016 then shows that thermodynamic constraints still do not close Montgomery--Taylor: an explicit positive cubic spectral profile has `C(J)/p(J)=53/40<C_MT`. ANF-017 kills that survivor with a finite edge-detuned real configuration. ANF-018 identifies the correct invariant exactly. If `F` is the spatial positive-type kernel associated with `J`, then the universal finite-real floor satisfies

`q_real(J)=F(0)-2 B_stab(F)`,

where `B_stab(F)` is the optimal classical pair-potential stability constant. The Montgomery--Taylor obstruction is therefore equivalent to a sharp lower bound on finite-cluster binding, not to another periodization estimate.

## What remains possible

The universal scalar branch is not yet proved empty. A decisive result should prove the required stability inequality for every admissible positive-band `F`, or exhibit a genuine profile whose complete finite-configuration floor still beats Montgomery--Taylor. Thermodynamic lattice calculations alone cannot decide this.

Matrix/inertia order, source-specific inequalities, nonlinear configuration functionals, and genuine higher correlations remain outside this scalar-affine classification.

## Status / novelty

Fourier positivity, Mellin transforms, lattice periodization, Ruelle-type stability constants, and finite-particle binding are classical. The persisted synthesis is the sharpened boundary: **the complete universal scalar-pair gate is a finite-cluster stability problem, and bulk lattice saturation can miss the binding mode that controls the final certificate**.

## Falsification criterion

Construct an admissible positive-band profile for which the exact ANF-018 stability identity holds but the complete finite-real certificate is not governed by `B_stab(F)`, or prove a profile with `C(J)/q_real(J)<C_MT`. A non-scalar or non-affine carrier would evade rather than falsify this intuition.

## Lean-formalizable core

- Affine scalarization of finite pair channels.
- Conjugate-comb localization forcing `J>=0`.
- Duplicated-lattice periodization and Mellin floor.
- Finite-cluster counterexample to thermodynamic sufficiency.
- Identity `q_real(J)=F(0)-2B_stab(F)` and the resulting sharp stability inequality.
