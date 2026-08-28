# Weil-inertia critical-line research

This directory preserves high-signal evidence from the **Mathia Weil-inertia** research line.

The line starts from the recent Montgomery/Weil-form, matrix-inertia route to an unconditional lower bound for zeros that are both **simple and on the critical line**. Its purpose is not to repackage that bound, but to attack the structural gap that remains after it.

The central question is:

> **Can the inertia/rank-trace mechanism be strengthened beyond the current two-thirds barrier, or can the exceptional mass not certified by the argument be characterized so rigidly that the remaining off-line or multiple-zero configurations can be ruled out?**

## Important interpretation of the exceptional fraction

The complement of a lower bound such as `2/3` is **not** a known set of zeros sitting off the critical line, and the bound does not assert that exactly `1/3` of the zeros are exceptional.

The uncertified mass may contain different phenomena, including:

- zeros on the critical line that are not proved simple by the argument;
- zeros away from the critical line, with the functional-equation/conjugation symmetries they must satisfy;
- slack introduced by inequalities, test-function restrictions, moment truncation, or other proof losses.

A core goal of this line is therefore to separate these sources of slack rather than treating the complement as one homogeneous population.

## Research stance

The first substantive pass must reconstruct and verify the exact theorem, hypotheses, normalization, and primary sources behind the recent result before treating any informal description of it as evidence.

After that, the line should prioritize mechanisms that can materially change the certified proportion or constrain the exceptional contribution:

1. **Locate every source of loss.** Rewrite the proof as a chain of exact identities and inequalities; identify equality and near-equality cases for the rank/trace/inertia step, moment estimates, kernel restrictions, and any zero-counting reductions.
2. **Exploit block structure, not only aggregate positivity.** Track separately the positive semidefinite contribution from critical-line zeros and the paired/quadrupled indefinite structure forced by off-line zeros, including multiplicities and all zeta symmetries.
3. **Study extremizers.** If the present constant were close to sharp, determine what the zero configuration and the associated Hermitian form would have to look like. Then test whether the explicit formula, arithmetic side, known density estimates, or additional spectral invariants forbid such near-extremizers.
4. **Add information beyond two global moments.** Investigate higher trace moments, mixed moments, principal minors, determinant/interlacing constraints, local spectral statistics, or other invariants only when they are actually accessible from the explicit formula or established zero statistics.
5. **Optimize the test-function/kernel problem.** Determine the true variational barrier imposed by Fourier support, explicit-formula control, or positivity assumptions. Distinguish a sharp barrier of the method from a merely nonoptimal kernel choice.
6. **Separate multiplicity from off-line mass.** Seek inequalities or auxiliary observables that penalize multiple critical-line zeros differently from off-line hyperbolic blocks, rather than paying for both with one undifferentiated error term.
7. **Combine independent unconditional information carefully.** Zero-density theorems, simple-zero results, pair-correlation information, mollifier methods, or wider-support results are useful only when the hypotheses and overlap with the inertia framework are explicit and non-circular.
8. **Look for a defect-to-zero mechanism.** A particularly valuable outcome would be a monotone or bootstrapping principle that turns a quantitative bound on negative inertia/off-line mass into a stronger bound, potentially iterating toward zero.

Negative results are first-class. A rigorous proof that a proposed higher-moment, kernel, interlacing, or bootstrapping improvement cannot beat a specific barrier is a substantive result because it identifies what genuinely new arithmetic information would be required.

## Relation to `weil_positivity`

`research/weil_positivity/` asks whether an independent Mathia-native geometry can force a global Weil-type positivity statement.

This line is deliberately complementary. It does **not** begin by demanding full positivity. Instead it studies the **defect from positivity**: inertia, rank, block signature, exceptional mass, and the amount of arithmetic information needed to squeeze that defect.

A mechanism that actually forces the negative inertia to vanish may become a bridge to `weil_positivity`, but the two lines should remain distinct unless persisted evidence establishes such a bridge.

## Prior-art audit surface

Novelty checks should search by mechanism, not by wording, especially around:

- Montgomery pair correlation and simple-zero density arguments;
- Weil's explicit formula and Hermitian/positivity formulations;
- inertia and signature of Hermitian forms, Sylvester law of inertia, rank/trace/Frobenius inequalities, interlacing, and extremal matrix inequalities;
- Levinson/Conrey-style critical-line proportions and mollifier methods;
- zero-density theorems, multiplicity bounds, pair correlation, and higher zero correlations;
- test-function optimization and Fourier-support barriers in explicit-formula arguments;
- recent work that supplies unconditional arithmetic-side estimates used by the two-thirds argument.

Do not claim novelty merely because the matrix language, kernel, or decomposition is phrased differently.

## Evidence labels

Use the shared `mathia-research-watch` vocabulary, including:

- **EXACT-DERIVED**;
- **LITERATURE+DERIVED**;
- **CLASSICAL-IDENTITY**;
- **CANDIDATE-NEW-STRUCTURE**;
- **NEGATIVE/OBSTRUCTION** / **DECISIVE-NEGATIVE**;
- **CONJECTURAL** / **NEEDS-AUDIT**.

These labels record evidence and uncertainty, not importance.

## Persistence boundary

This line is maintained by `.agents/skills/mathia-research-watch/SKILL.md` with stable finding prefix **`WI`**.

When substantive results appear, persist them under the standard evidence contract:

```text
research/weil_inertia/SOURCES.md
research/weil_inertia/findings/WI-NNN-<slug>.md
```

The individual files under `findings/` are the canonical research evidence. Do not create a parallel hand-maintained finding index. Derived graph navigation is owned by the graph curator.

Do not create chronological run notes or write into any `mind/` directory. Missing evidence artifacts should be initialized only when the first substantive finding requires them.
