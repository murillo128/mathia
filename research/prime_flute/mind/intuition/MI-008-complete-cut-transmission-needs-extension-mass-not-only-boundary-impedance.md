# MI-008 — The flute mixed-response gate is a source/escape balance, not a Robin contraction gap

**Evidence level:** proved local operator and source-space boundaries; the factorization of the complete physical mixed response remains open.

For the fixed physical high-pass spaces, PF-292 gives a diverging local frequency floor. PF-296 then proves that the canonical fixed-axis synthesis is uniformly bounded from the explicit weighted source space `ell^1(q)` into positive Sobolev regularity, with `q_i asymp i+1`. Thus a complete normalized response with uniformly bounded `sum_i q_i|a_i|`, controlled transport, and negligible residual cannot sustain the PF-290 local high-band shorting deficit.

PF-297 now identifies the exact behavior of one repeated local factor. Every fixed-axis Robin inverse is nonexpansive in the **same** `ell^1(q)` currency. Finite Galerkin sections are strictly contractive because `q`-mass leaks into omitted rows, but that loss is a truncation effect: for each fixed source row the retained mass tends back to the full value, the finite-section norms tend to one, and the complete positive inverse preserves `q`-mass exactly.

So repeated Robin normalization cannot amplify the PF-296 source budget, but it also cannot provide a depth-uniform geometric discount for a return resolvent. A proof based on “every finite section has norm < 1” is therefore invalid in the infinite-depth limit.

The remaining gate is the **actual normalized mixed return/reassembly map**. Starting from the PF-290 `P/H`-split mixed functional, one must derive the real coefficient equation and locate where source mass can leave the repeated subsystem. A sufficient positive-majorant route is a uniformly summable excessive vector `h` for the physical forcing: after conjugating by `q`, if `K>=0`, `Kh<=h`, and `xi<=h-Kh`, then the Green potential `sum_m K^m xi` is bounded without any spectral gap. A direct signed estimate is equally admissible if absolute values destroy the useful cancellation.

This makes the source budget more concrete. Unbounded row count is not by itself an escape, Robin inversion is not an amplifier, and local finite-section loss is not a uniform return discount. A surviving obstruction must come from forcing that is too large for the available escape, from the physical `P/H` split or Schur/reassembly maps changing the `q` currency, or from an explicit residual operator outside the canonical synthesis.

**Boundary.** PF-297 concerns only the fixed-axis Robin factor. It does not derive the complete return operator, prove a source-adapted potential bound, imply global compactness, or control the separate heavy-range singular-value problem.