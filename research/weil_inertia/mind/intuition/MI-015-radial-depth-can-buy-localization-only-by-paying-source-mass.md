# MI-015 — Same-window bow screening is limited by a joint amplitude-and-spacing ledger

**Evidence level:** exact count--depth and selected-amplitude tariffs, local Riemann--von Mangoldt density, published near-edge zero-density control, and spacing-surplus tariff through WI-235

## Core intuition

Density matching turns local bow screening into a first-harmonic amplitude budget: the selected population contributes `m A_T`, while the complementary population has limited count and near-edge radial capacity. A spacing surplus is a genuine way to enlarge that reservoir, but it is not a soft perturbation once the selected amplitude exceeds the near-edge capacity.

The same-window variables therefore form one coupled ledger. Count, radial depth, selected amplitude, and spacing surplus cannot be optimized independently.

## Strongest justified principle

WI-227--WI-234 establish the count--depth and amplitude tariffs. At the local Riemann--von Mangoldt spacing, a bow of size `m=T^(theta+o(1))`, `theta<1/2`, leaves only `O(log T)` complementary labels. Retaining the selected radial factor `A_T` requires cancellation amplitude of order `m A_T`, and Bellotti's near-edge zero-density theorem bounds how much first-harmonic mass the local complement can provide, closing the calibrated quarter boundary.

WI-235 keeps a relative spacing surplus `epsilon_T`. The local count reservoir becomes `O(epsilon_T m+log T)`, but Bellotti's estimate still caps the radial amplitude per shallow label. If `m A_T` is above the bounded near-edge capacity, the resulting inequality forces the normalized spacing surplus to exceed **every fixed Korobov--Vinogradov subexponential correction** to its power threshold. For a positive-density selected population at fixed depth `delta_0`, bow exponent `theta>1/4-delta_0/2` forces this super-KV tariff. At depth `delta_0=1/4`, any `theta>1/8` screen needs a spacing surplus asymptotically larger than `T^-1/8 exp(C S(T))` for every fixed `C` in the stated normalization.

## Program consequence

Treat small spacing surplus as closed in the same-window regime once the amplitude threshold is crossed. A surviving cancellation mechanism must use a genuinely larger power-scale/fixed surplus, remote ordinate mass, prime/source cancellation, or a theorem preventing the selected deep population. For any proposed escape, translate its available population and radial weight back into first-harmonic capacity before judging it viable.

A useful bootstrap must create population/coherence, not merely one exceptional deep zero, so that the new structure can be charged again by the same ledger.

## Counterevidence / boundary

WI-235 does not rule out a fixed or sufficiently large power-scale spacing surplus, nonlocal vertical screening, or source-side cancellation. Its sharp asymptotics are tied to the near-density-matched regime and Bellotti's near-edge theorem. The argument still does not manufacture a second forced population from the existence of one deep screen label.

The amplitude bound is a necessary screening condition, not a proof that admissible zeros can realize the optimally aligned complement allowed by the triangle inequality.

## Epistemic status

**Exact same-window capacity obstruction strengthened by spacing: once selected radial amplitude outruns the near-edge reservoir, any local spacing escape must pay a super-Korobov--Vinogradov tariff at the natural power scale; surviving cancellation must become genuinely larger-scale, nonlocal, source-side, or population-changing.**

## Falsification criterion

Construct a same-window screen satisfying the WI-235 hypotheses whose selected amplitude crosses the stated threshold while its spacing surplus remains within one fixed KV-corrected power bound, or show that the Bellotti/Riemann--von Mangoldt conversion does not control the multiplicity-sensitive first-harmonic capacity used in the tariff.
