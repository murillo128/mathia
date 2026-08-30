# Weil Inertia

## Research mandate

### Identity

Research line: `weil_inertia`.

### Primary object

The line starts from the recent Montgomery/Weil-form matrix-inertia approach giving an unconditional lower bound of roughly two thirds for zeta zeros that are both simple and on the critical line.

Before using the result as evidence, reconstruct and verify its exact theorem statement, constant, hypotheses, normalization, proof provenance, and primary sources. The central mathematical object is the associated Hermitian/Weil form together with the rank, trace, inertia, block-signature, moment, and test-function information that can be extracted from it.

The uncertified complement is not a known population of off-critical zeros and is not known to equal one third. It may contain multiple zeros on the critical line, off-line zeros constrained by functional-equation/conjugation symmetries, and pure slack from the proof.

### Objective

Pursue two coupled goals:

1. strengthen the certified critical-line/simple-zero proportion beyond the current result; and
2. characterize the uncertified complement so rigidly that the remaining off-line, multiple-zero, or proof-slack configurations can be reduced or ruled out.

A particularly valuable outcome would be a defect-to-zero or bootstrapping mechanism that converts a quantitative bound on negative inertia/off-line mass into a strictly stronger bound and can potentially iterate.

### Priority questions

- Reconstruct the proof as exact identities and inequalities and locate every source of slack.
- Determine equality and near-equality cases for the rank/trace/inertia estimates and associated moment or zero-counting steps.
- Separate positive-semidefinite critical-line contributions from the paired or quadrupled indefinite blocks forced by off-line zeros, keeping multiplicity explicit.
- Characterize extremal or near-extremal zero/matrix configurations required for the current constant to be sharp.
- Test whether arithmetic constraints, explicit-formula identities, zero-density information, or spectral invariants forbid those extremizers.
- Investigate higher trace moments, mixed moments, principal minors, determinant constraints, interlacing, local spectral statistics, or other invariants only when they are genuinely accessible.
- Optimize admissible test functions and kernels and identify the true barrier imposed by Fourier support and available arithmetic information.
- Seek observables that distinguish multiple critical-line zeros from off-line blocks instead of paying for both through one error term.
- Combine independent unconditional information from simple-zero results, pair/higher correlations, mollifier methods, or zero-density estimates only when hypotheses and overlap with the inertia framework are explicit.
- Search for monotone defect estimates or bootstrap inequalities that can feed improved bounds back into the argument.

### Scope and exclusions

Do not interpret the uncertified complement as exactly `1/3`, as entirely off the critical line, or as a homogeneous exceptional population.

Do not assume full Weil positivity at the outset; this line studies quantitative defect from positivity. Do not import conjectural pair-correlation, density, or support information into an unconditional bound without labeling the dependency explicitly.

A wider Fourier support, stronger moment estimate, or additional spectral invariant is admissible only when the arithmetic side required to control it is actually available.

### Falsification and novelty standard

Treat barriers and negative results as first-class outcomes. For each proposed improvement:

- identify the exact inequality or information bottleneck it changes;
- compute or characterize extremizers and near-extremizers;
- test whether the new invariant is independent of the moments already used;
- distinguish a nonoptimal choice of kernel from a sharp barrier of the method;
- determine what genuinely new arithmetic information would be required if the route cannot improve the constant;
- check all functional-equation, conjugation, multiplicity, normalization, and block-signature constraints;
- reject matrix reformulations that merely restate the same bound without adding information.

Novelty must be assessed by mathematical mechanism, not by different matrix notation or decomposition language.

### Prior-art audit surface

Search by mechanism and equivalent formulation across:

- Montgomery pair correlation and simple-zero density arguments;
- Weil's explicit formula and Hermitian/positivity formulations;
- inertia and signature of Hermitian forms, Sylvester law of inertia, rank/trace/Frobenius inequalities, interlacing, determinants, principal minors, and extremal matrix inequalities;
- Levinson/Conrey-style critical-line proportions and mollifier methods;
- zero-density theorems and multiplicity estimates;
- pair and higher zero correlations;
- test-function optimization and Fourier-support barriers in explicit-formula arguments;
- recent arithmetic estimates used by the two-thirds argument.

### Relationship to other lines

`weil_positivity` asks whether an independent Mathia-native structure can force global Weil positivity. This line is complementary: it studies inertia, rank, block signature, exceptional mass, and quantitative defect without assuming full positivity.

Prime Circle, Prime Flute, and Prime Lattice may contribute explicit auxiliary structures or constraints only when a precise evidence-backed bridge exists. They are otherwise separate research objects.
