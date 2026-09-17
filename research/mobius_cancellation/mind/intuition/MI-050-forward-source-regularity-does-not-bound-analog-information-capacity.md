# MI-050 — Forward source regularity does not bound analog information capacity

**Evidence level:** exact finite-source synthesis from [MC-340](../../findings/MC-340-global-transcript-information-capacity.md), [MC-341](../../findings/MC-341-analog-transcript-spread-capacity.md), and [MC-342](../../findings/MC-342-forward-source-regularity-does-not-price-analog-capacity.md).

MC-340 forces `Omega(R)` joint source information into any bounded-energy transcript that achieves nontrivial reciprocal-endpoint dephasing. MC-341 shows that, once a source-natural Euclidean resolution is declared, low-dimensional realization of that information costs large metric spread. MC-342 closes a tempting replacement for that resolution hypothesis: bounded **forward** source smoothness does not control how much exact information an analog transcript can hide.

On the even-rank punctured source cube, the scalar positional code

`T_R(B)=sum_(i=1)^R 2^(-i) B_i`

is injective, so it carries `log(2^R-1)=Theta(R)` nats. Nevertheless its diameter is below one, its Hamming-to-Euclidean Lipschitz constant is exactly `1/2`, and every fixed positive-moment edge energy `D_p(T_R)` remains bounded uniformly in `R`. Successive source coordinates are simply stored at geometrically decreasing amplitudes.

The hidden cost appears only in the inverse direction. Distinct transcript values can be separated by `2^(-R)`, the scalar spread is `2^R-2`, and any inverse-Lipschitz constant is at least exponential. If the transcript is quantized to `k` binary digits, its information is at most `k log 2`; composing this with MC-340 forces `k=Theta(R)` for fixed nontrivial dephasing at bounded coefficient energy.

The reusable distinction is therefore **forward regularity versus inverse distinguishability**. A source-to-transcript map can have bounded range, bounded Lipschitz constant and bounded fixed-`p` gradient energy while being an exact high-capacity encoder. Those quantities only upper-bound how far source perturbations move the transcript; they do not lower-bound how far distinct relevant source states remain separated under the observation/noise model.

For a genuine arithmetic transcript, a useful conditioning theorem must therefore identify an intrinsic observation norm or noise/precision scale and prove a lower separation, inverse modulus, co-Lipschitz estimate, finite-precision capacity bound, or arithmetic prohibition on hierarchical sub-resolution coding. Without such an inverse statement, low dimension and benign forward sensitivity are coordinate-dependent descriptions rather than endpoint obstructions.

**Boundary.** The dyadic encoder is an adversarial control, not a claim about the actual Möbius transcript. It proves that a generic theorem based only on forward regularity cannot supply the missing capacity bound. The open arithmetic task is to derive an inverse-resolution resource from the real construction rather than impose one by an arbitrary coordinate choice.