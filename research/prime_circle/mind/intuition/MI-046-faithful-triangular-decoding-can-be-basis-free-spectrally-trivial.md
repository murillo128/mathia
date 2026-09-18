# MI-046 — Faithful triangular decoding can be basis-free spectrally trivial

**Evidence level:** exact synthesis from [PC-350](../../findings/PC-350-all-depth-reciprocal-defect-faithfully-recovers-centered-shell-profile.md) and [PC-351](../../findings/PC-351-triangular-inversion-defect-readouts-are-spectrally-trivial.md).

A representation can recover the complete source and still lose every useful discriminator when one passes to its natural basis-free operator invariants.

PC-350 gives an explicit `2x2` solvable decoder for the reciprocal shell defect. Its off-diagonal coefficient

`V_n(lambda)=int_0^infinity (1+r)^lambda dW_n(r)`

is faithful to the complete centered radial profile: on the imaginary axis Fourier uniqueness recovers `dW_n`. Thus the decoder is not information-poor.

PC-351 shows where that information lives. Every simultaneously upper-triangular regularized development has limiting diagonal equal to one, so its ordinary spectrum, determinant and trace powers are source-blind. In the canonical `2x2` family

`T_n(lambda)=[[1,V_n(lambda)],[0,1]]`,

all nonzero coefficients have the same nontrivial Jordan class. The faithful information is an **oriented nilpotent coordinate**, not an eigenvalue.

The obstruction survives richer basis-free geometry. In the matched reciprocal control class, replacing the centered profile by its sign flip `W->-W` preserves residue and reciprocity. One fixed unitary `S=diag(1,-1)` conjugates `T(V)` to `T(-V)` for every shell and every parameter. Consequently singular values, pseudospectra, numerical ranges and every invariant that factors through simultaneous unitary equivalence are identical for the source and its matched control.

The reusable lesson is: **source fidelity and invariant fidelity are different resources**. Before crediting a faithful matrix or noncommutative encoding, identify where its information sits and then apply the exact gauge/basis quotient used by the proposed destination. Information confined to oriented off-diagonal coordinates may disappear completely under the very invariance that makes an operator construction canonical.

This also explains why “spectralize the faithful decoder” is not a free next step. Keeping the orientation retains the source but merely continues reconstruction. Forgetting orientation through the triangular basis-free spectrum loses the source distinction. A useful intermediate object needs a source-forced quotient that is both genuinely information-reducing and still selective against matched controls.

**Boundary.** The no-go covers simultaneously triangularizable finite-dimensional developments and the unitary-equivalence class of the canonical decoder. It does not rule out genuinely non-triangular/non-solvable source-forced representations or other quotients whose invariants are not captured by this control conjugacy. No zero-selection theorem follows from fidelity alone.