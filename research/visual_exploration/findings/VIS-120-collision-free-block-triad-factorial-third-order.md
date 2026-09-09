# VIS-120 — collision-free wrapped triads isolate the third factorial channel

## Claim

Let `theta_1,...,theta_M` be any finite circular point configuration and define

`p_m = sum_(j=1)^M exp(i m theta_j)`

for positive integers `m`. For positive `a,b`, let

`B_(a,b)=p_a p_b overline(p_(a+b))`

be the raw frequency-conserving triad used in `VIS-118`--`VIS-119`, and define its pairwise-distinct version

`F_(a,b)=sum_(i,j,k pairwise distinct) exp(i[a theta_i+b theta_j-(a+b)theta_k])`.

Then the following identity holds for every configuration, with no probabilistic assumptions:

`F_(a,b)`
` = B_(a,b) - |p_a|^2 - |p_b|^2 - |p_(a+b)|^2 + 2M`.

Thus a wrapped finite block has an exactly computable **collision-free third-order Fourier triad**. The correction removes every contribution in which two or three factors come from the same point. In particular, the resulting statistic depends only on ordered triples of distinct selected points and therefore has an expectation determined by the source's third factorial moment/correlation law under a deterministic windowing map.

This separation changes the source-dictionary boundary from `VIS-119` in two useful ways.

First, for `M` independent uniform phases,

`E[F_(a,b) | M]=0`.

The nonzero raw mean `E[B_(a,b)|M]=M` from `VIS-119` is therefore entirely a repeated-index self-collision effect.

Second, for Haar `CUE_N` on the full circle, whenever `a+b<=N`,

`E_CUE[F_(a,b)] = 2(N-a-b)`.

So collision removal does **not** make CUE centered. Instead it exposes a genuine three-distinct-point CUE contribution that exactly cancels the lower-order collision terms in the raw Haar trace identity `E_CUE[B_(a,b)]=0` from `VIS-118`.

Consequently, a finite zero-window versus CUE comparison can avoid one false transfer by using the same collision-free statistic on both sources. But it must still calibrate the third-order CUE window law itself; removing repeated indices is not a substitute for a matched finite-window CUE null.

**Evidence/status:** `EXACT-DERIVED + THIRD-FACTORIAL-CHANNEL DECOMPOSITION + SOURCE-DICTIONARY CONTROL + NO-NOVELTY-CLAIM`.

No zeta anomaly, asymptotic CUE block law, Gaussian limit, arithmetic excess, or RH implication is established.

## 1. Exact decomposition by index collisions

Expand

`B_(a,b)=sum_(i,j,k) exp(i[a theta_i+b theta_j-(a+b)theta_k])`.

Partition the ordered triples `(i,j,k)` into the five disjoint equality patterns: all distinct; `i=j!=k`; `i=k!=j`; `j=k!=i`; and `i=j=k`.

The all-distinct part is `F_(a,b)`. The three two-equal contributions are respectively

`sum_(i!=k) exp(i(a+b)(theta_i-theta_k)) = |p_(a+b)|^2-M`,

`sum_(i!=j) exp(i b(theta_j-theta_i)) = |p_b|^2-M`,

and

`sum_(j!=i) exp(i a(theta_i-theta_j)) = |p_a|^2-M`.

The all-equal contribution is exactly `M`. Therefore

`B_(a,b)`
` = F_(a,b) + |p_a|^2 + |p_b|^2 + |p_(a+b)|^2 - 2M`,

which rearranges to the claimed identity.

The formula remains valid when `a=b`; in that case the two `|p_a|^2` collision channels are genuinely distinct equality patterns and must both be subtracted.

Because the total frequency is zero, `F_(a,b)` is invariant under a common angular shift `theta_j -> theta_j+delta`, just like the raw triad. The correction therefore removes index collisions without reintroducing an arbitrary circular-origin dependence.

## 2. Independent uniform phases become exactly centered

Condition on a fixed count `M` and take the phases independently uniform on `[0,2 pi)`.

For pairwise distinct `i,j,k`, independence gives

`E exp(i[a theta_i+b theta_j-(a+b)theta_k])`
` = E exp(i a theta_i) E exp(i b theta_j) E exp(-i(a+b)theta_k)`
` = 0`.

Summing over distinct ordered triples yields

`E[F_(a,b)|M]=0`.

This identifies precisely where the `M` in `VIS-119` came from. In the raw product, the terms `i=j=k` survive even for a completely independent uniform source. After the exact collision correction, that self-interaction disappears rather than being mistaken for a third-order source signal.

This is a control statement only. Independent uniform phases remain an intentionally weak counter-model for CUE or zeta zeros.

## 3. Full-circle CUE has a nonzero genuine three-point mean

Now let the `theta_j` be the eigenangles of Haar `U(N)`. Inside `a+b<=N`, `VIS-118` records the classical exact trace moment

`E_CUE[B_(a,b)]=0`.

The same Diaconis--Shahshahani/Diaconis--Evans low-degree formula gives

`E_CUE[|p_q|^2]=q`

for every positive `q<=N`. Since `a`, `b`, and `a+b` all lie in this range,

`E_CUE[F_(a,b)]`
` = 0 - a - b - (a+b) + 2N`
` = 2(N-a-b)`.

Equivalently, the exact Haar centering of the raw trace triad is a cancellation among different information orders. The diagonal and two-point collision pieces do not vanish separately, and the genuine distinct-triple term does not vanish separately. Their sum does.

This makes the caution in `VIS-119` sharper: a visually natural operation such as deleting self-collisions may improve interpretation while simultaneously changing the exact null mean. A source-faithful statistic must be calibrated after the transformation actually used, not before it.

## 4. Deterministic hard windows reduce the null to a third factorial correlation

Let a deterministic source window select a finite set of points and let a deterministic map send every selected point `x` to a circular coordinate `theta=phi(x)`. Apply the exact configuration identity to the selected block and its random count `M_W`.

For a simple random point process with third factorial correlation density `rho_3(x,y,z)`, the expectation of the collision-free triad is, whenever the integrals exist,

`E[F_(a,b)^W]`
` = integral_(W^3) exp(i[a phi(x)+b phi(y)-(a+b)phi(z)])`
`   rho_3(x,y,z) dx dy dz`.

The integral is over distinct points in the factorial sense; the diagonals have already been removed by construction. This is the standard factorial-moment interpretation of a distinct-index point-process statistic.

For CUE, the finite-`N` eigenangle process is determinantal, so the relevant `rho_3` is determined by the finite CUE kernel. A matched CUE block baseline can therefore be obtained in either of the two source-faithful ways left open by `VIS-119`: apply the identical window/map/statistic to finite CUE samples, or evaluate the corresponding finite-window third-correlation integral analytically.

The present finding does not carry out that remaining CUE window integral. Its contribution is to remove the lower-order collision ambiguity before that calculation begins.

If the block is selected by a data-dependent fixed-count rule rather than by a deterministic region, the configuration identity still holds exactly, but the simple restricted-`rho_3` formula above need not describe the induced selection law without additional conditioning. The matched control must reproduce the same selection rule.

## 5. Why the collision-free form is the cleaner visual coordinate

A raw heatmap of `B_(a,b)` mixes three qualitatively different ingredients: one-point self-collisions, two-point Fourier power, and genuine three-distinct-point interaction. Two sources can therefore differ in the raw triad because of lower-order structure even when their distinct-triple channel is similar.

The corrected coordinate

`F_(a,b)=B_(a,b)-|p_a|^2-|p_b|^2-|p_(a+b)|^2+2M`

is still directly computable from the same wrapped point cloud, but its interpretation is narrower. It asks only about the ordered third factorial channel of the selected configuration.

This does not make a visual panel self-validating. A ridge or phase pattern in `F_(a,b)` can still come from the finite CUE three-point law, the window, compactification, edge effects, or a post-hoc frequency choice. It merely prevents the most elementary lower-order collision terms from being displayed as though they were irreducible three-point structure.

No canonical PNG is retained because the mathematical result is an algebraic information decomposition rather than an empirical visual pattern.

## 6. Prior art and novelty assessment

The inclusion--exclusion from ordinary products to pairwise-distinct sums is standard factorial-moment/U-statistic bookkeeping for point processes. Third-order point-process spectra and bispectra are classical; David R. Brillinger's 1994 survey **Comparative Aspects of the Analysis of Stationary Time Series, Point Processes and Hybrids** explicitly treats second- and third-order moments and spectra for point processes. General factorial moment measures and product densities are standard point-process machinery, for example in D. J. Daley and D. Vere-Jones, **An Introduction to the Theory of Point Processes, Volume I**, 2nd ed. (Springer, 2003).

The CUE side is also classical. `VIS-118` already records the exact Diaconis--Shahshahani/Diaconis--Evans Haar trace moments used above. Determinantal point-process correlation functions are standard; J. Ben Hough, Manjunath Krishnapur, Yuval Peres, and Balint Virag, **Determinantal Processes and Independence**, *Probability Surveys* 3 (2006), 206--229, DOI `10.1214/154957806000000078`, is an explicit modern reference.

No general factorial-spectrum, determinantal-process, or random-matrix theorem is claimed as new. The Mathia-specific delta is the exact audit of the currently proposed wrapped trace-bispectrum coordinate: it identifies and removes its repeated-index contamination, then shows that the resulting third-factorial coordinate has a different exact CUE mean and therefore still requires a matched source/window calibration.

## Boundary and falsification

The algebraic identity assumes unit weights on the selected points. A taper or other non-binary weighting changes the collision terms because repeated indices carry powers of the weight; the displayed correction must not be reused unchanged in that setting.

The independent-uniform centering assumes distinct phases are independent and uniform conditional on `M`. It is used only to identify the raw self-collision term.

The full-circle CUE mean `2(N-a-b)` assumes Haar `U(N)` and `a+b<=N`. It is not a finite-window formula and must not be transferred to a selected CUE block.

The deterministic-window factorial integral assumes a simple point process and a deterministic selection/map. Data-dependent fixed-count extraction requires the same conditional selection law on the control source.

The finding is falsified by any finite configuration violating the displayed algebraic identity, or by a Haar CUE moment inside the stated corridor for which `E|p_q|^2=q` or `E[B_(a,b)]=0` fails.

## Research consequence

`VIS-119` showed that naive circularization does not justify importing the full Haar trace null. The present result supplies the next exact source-dictionary refinement: **use a collision-free triad when the intended question is genuinely third-order, then calibrate that transformed statistic under the exact same source window and selection rule**.

This removes one avoidable ambiguity without pretending the source problem is solved. The next separate thread is now sharply defined: for a predeclared deterministic window/compactification and frequency panel, derive or simulate the finite-CUE mean/covariance of `F_(a,b)` itself, and only after that freeze a zeta-side confirmation protocol. That remaining matched-window calculation is intentionally left for a later invocation.
