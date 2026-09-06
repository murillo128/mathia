# MI-013 — Exceptional populations have a finite spectral screening rank

**Evidence level:** exact finite Hilbert-space and matrix inequalities through WI-180, with literature-backed Lamzouri source

## Core intuition

The first useful joint constraint beyond the affine-vector barrier is not another additive coordinate. In Lamzouri's exact finite Hilbert tensor, exceptional zeros control the **rank of the operator that can screen supercritical simple-real Gram modes**. One distinct off-line conjugate pair can cancel at most one projected supercritical mode, and after restoring the full simple-real Gram each distinct exceptional element accounts for at most one screening slot.

This converts exceptional population from a scalar tax into a nonlinear feasibility constraint on spectral shape. It is precisely the kind of information that WI-177's affine/support-functional witness theorem does not erase.

## Strongest justified principle

WI-178 shows that the Lamzouri slack contains the entire clipped Gram defect of the simple-real sector while retaining off-line mass and multiplicity separately:

`Q-N >= O + 2M + tr Psi(G_s)`.

WI-179 keeps the source fact discarded by the unrestricted proximal relaxation: the odd exceptional correction has rank at most the number `k` of distinct off-line conjugate pairs. Rank-constrained low-rank approximation then leaves the unavoidable tail `T_k(S)` of quotient-Gram eigenvalues above `2` after the first `k` modes.

WI-180 transfers this tail to the directly observable full simple-real Gram. The projection component has rank at most `r+k`, so interlacing costs only those additional slots. The resulting exact screening cutoff is `D-n=r+2k`, the number of distinct exceptional elements:

`Q-N >= O + 2M + tr Psi(G_s) + T_{D-n}(G_s)`.

Thus **multiplicity can spend scalar budget but does not buy arbitrary spectral screening rank**. A source theorem forcing more than `D-n` substantial eigenvalues above `2`, or forcing the supercritical participation ratio beyond that count, would create a new coercive term automatically.

## What remains possible

No existing source theorem yet forces the required supercritical spectral shape. The Montgomery--Taylor periodic control in WI-180 has extensive Gram defect while all eigenvalues remain below `2`, proving that scalar defect or pair energy alone cannot activate the new tail. The missing input must preserve information about the positive spectral part above the clipping threshold, such as mode multiplicity, higher moments, or another zeta-specific constraint excluding subcritical controls.

Confluence remains live: a small number of exceptional pairs may still screen a correspondingly small number of supercritical modes. The new mechanism becomes useful only if source geometry forces spectral complexity faster than the exceptional count can track it.

## Status / novelty

Lamzouri's finite Hilbert-space source is literature; proximal PSD minimization, Eckart--Young approximation, rank interlacing, and moment/rank inequalities are classical. The durable synthesis is source-specific: **the exceptional block has a finite spectral screening capacity, creating a genuinely joint nonlinear constraint unavailable to additive affine bookkeeping.**

## Falsification criterion

Construct a Lamzouri-admissible configuration in which `D-n` distinct exceptional elements screen more than `D-n` full-Gram supercritical modes without paying the WI-180 tail, invalidate the rank/interlacing transfer, or show that the source class forces no observable capable of distinguishing the subcritical periodic control from the actual simple-real Gram. The first two would refute the mechanism; the third would leave it exact but unusable for further bootstrap.
