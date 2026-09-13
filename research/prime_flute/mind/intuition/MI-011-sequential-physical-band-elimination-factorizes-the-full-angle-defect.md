# MI-011 — Sequential elimination leaves two visible angle channels, and the direct one is locally banded

**Evidence level:** exact on every finite strictly positive canonical section through PF-317. Compatible infinite-section realization and the required local mixed-frequency estimate remain open.

PF-315--PF-316 reduce the physical low/high angle to the pair `(T_H,Z_LH)`. The residual map `V_H` is not a third endpoint regularizer: if it attenuates a conditional direction, the defect is quadratically controlled by the direct angle, and weak trace of the full angle is equivalent to weak trace of both channels.

PF-317 adds a second exact simplification for `Z_LH`. In simultaneous seam-energy coordinates the positive precision is `I+K` with `K>=0`. The diagonal completion factors around `K_LH` are contractions, so `s_j(Z_LH)<=s_j(K_LH)`. Moreover `K` is nearest-neighbor in cuff-module index, making the direct cross block a sum of only the three offsets `r=-1,0,1`, each an orthogonal direct sum of local pant blocks.

Because the retained nonconstant low band on module `n` has only `O(1+log P_n)` dimensions, a local normalized pant estimate `||L_(n+r) K H_n|| <= C/P_n` is already sufficient for the global weak-`S_1` count. The collapsing seam normalizer is not the remaining obstacle: PF-317 compares the true strip energy to the explicit flat shifted-strip DtN matrix at relative error `1+O(P_n^-2)`.

The load-bearing obstruction is frequency-selective. PF-215 shows that the complete adjacent normalized pant transfer can diverge on constant-to-constant data, so no proof may bound the whole pant block and infer the desired corner. The unresolved theorem must use the physical high/nonconstant-low split to show reciprocal-prime decay, or produce an equally strong local singular-value envelope.

**Boundary.** This localization closes the organizational and reassembly burden only for the direct channel. It does not estimate `T_H`, prove the local `C/P_n` bound, construct the infinite operator, or close the signed target composition.