# MI-071 — Critical observation survival yields only inverse-depth raw generator resolution

**Evidence level:** exact local minimax synthesis from [AF-486](../../findings/AF-486-moving-hankel-determinants-recover-finite-dirichlet-depth-at-sharp-exponential-precision.md) and [AF-487](../../findings/AF-487-critical-moving-window-noise-has-sharp-inverse-depth-log-generator-resolution.md), refining the finite-window resource split in MI-070.

For a positive ordered Dirichlet source

`F(s)=sum_n a_n q_n^(-s)`, `a_n>0`, `q_1<q_2<...`,

fix the depth `J`, the step `h`, and a compact neighborhood `I` of `q_J` that stays inside the adjacent-node gap. From the `2J-1` moving samples `F_q(t+kh)`, `0<=k<=2J-2`, AF-486 identifies the sharp absolute scale at which the `J`th atom remains visible: samplewise errors of order `epsilon q^(-t)` are admissible below a source-dependent Vandermonde/weight conditioning threshold, while an order-one perturbation at the same exponential scale can erase that atom.

AF-487 shows that **survival at this critical observation scale does not imply comparably sharp parameter localization**. The noisy Hankel determinant ratio has only bounded multiplicative uncertainty relative to `q^(-t)`. Taking the `(-1/t)` root converts any such bounded factor into additive logarithmic uncertainty `O(1/t)`. Conversely, the two nearby generators

`q_1(t)=q_0 exp(gamma/t)`

have `|log q_1(t)-log q_0|=gamma/t`, while their whole fixed-width sample vectors differ by only `O(gamma q_0^(-t))`; for sufficiently small fixed `gamma`, one datum is admissible under both critical-noise models. Therefore

`inf_qhat sup_(q in I, ||eta||_inf<=epsilon q^(-t)) |log qhat-log q| = Theta(1/t)`.

The reusable distinction is between an **observation survival threshold** and the **inverse parameter-resolution modulus** at that threshold. Here exponentially fine absolute measurements are needed merely to retain the deepest atom, yet the surviving raw generator coordinate is localized only to inverse depth in `log q`. Treating “the atom survives” as a binary fidelity statement hides this second loss.

A discrete source mark changes the inverse problem rather than improving the same raw modulus. If side information restricts the unknown generator to `Lambda subset I` with fixed positive logarithmic spacing `delta_Lambda`, the `O(1/t)` estimate becomes exact nearest-neighbor identification once `C/t<delta_Lambda/2`. For rational primes in a fixed finite region this is available only after supplying rational-prime membership as side information. It therefore cannot be used as evidence that the unmarked Dirichlet-sampling channel intrinsically recognizes rational primality.

**Boundary.** The `Theta(1/t)` law is proved for fixed `J`, fixed `h`, one finite moving window at each `t`, positive ordered coefficients/nodes, a compact neighbor gap with uniform Vandermonde conditioning, and samplewise `l_infinity` noise at a fixed nonzero multiple of `q^(-t)`. It does not give a growing-depth modulus, signed/complex stability, a rate for a decoder accumulating an expanding history of earlier windows, or rational-prime provenance. Those are different observation/source classes and require separate evidence.