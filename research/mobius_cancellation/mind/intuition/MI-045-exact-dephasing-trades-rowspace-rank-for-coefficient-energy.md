# MI-045 — Exact dephasing trades rowspace rank for coefficient energy

**Evidence level:** exact finite endpoint synthesis from [MC-332](../../findings/MC-332-unrestricted-mode-dependent-weights-erase-character-oscillation.md) and [MC-333](../../findings/MC-333-energy-efficient-all-mode-dephasing-needs-linear-rank.md).

MC-332 shows why unrestricted mode-dependent coefficients are not a cancellation theorem. If every character mode receives its own row, the choice `w_(chi,r)=c_chi conjugate(chi(r))` removes the character phase pointwise. At the reciprocal endpoint this matched filter is especially deceptive: the entire character-evaluation matrix has rank only `R`, even though it acts on `2^R-1` nonprincipal modes. “Low rank compared with family size” therefore does not exclude exact dephasing.

MC-333 identifies the quantitative resource that rank alone misses. Let `A` shell primes be evenly distributed across the `R` one-defect sign cells, and require a coefficient matrix `W` of rank at most `d` to realize exact amplitudes `T_W(a)=A c_a` on every nonprincipal mode. Then

`||W||_F^2 >= (A R/(d 2^R)) ||c||_1^2`.

For the spread target `c_a=1`, the optimal energy is `Theta((R/d) A(2^R-1))`; the full endpoint evaluation rowspace at `d=R` achieves energy `A(2^R-1)`. Thus shrinking the common rowspace by a factor `R/d` forces the same-order inflation in quadratic coefficient energy. Constant-factor-energy exact dephasing of a spread all-mode target needs `d=Omega(R)`.

The mechanism is geometric. All rows must lie in one `d`-dimensional prime-coordinate subspace. Exact dephasing asks that this subspace correlate strongly with many character-evaluation vectors at once. The exact endpoint Gram spectrum and a Ky Fan projection bound limit how much total squared projection a `d`-plane can capture. The lower bound is therefore not “rank is good” or “energy is good”; it is a **joint rank--energy capacity law** for a family whose dangerous matched filter already has unexpectedly small rank.

This changes how candidate joint coefficient classes should be judged. A class may exclude the full evaluation matrix by rank while still contain a cheaper partial dephaser, or it may permit rank `Theta(R)` but penalize the evaluation geometry strongly in the norm appearing in the analytic theorem. What matters is the cheapest admissible approximation to the phase-matched filter under the exact theorem cost, not nominal matrix complexity.

The natural audit is consequently three-dimensional: latent rowspace dimension, coefficient energy/conditioning, and target amplitude distribution. Spread amplitudes force the `R/d` bill; sparse or highly concentrated amplitudes can evade an `ell^1`-driven lower bound and need separate analysis. Likewise a different analytic norm or approximate rather than exact dephasing could shift the capacity law.

For the Möbius endpoint, the next useful linear theorem should therefore specify the admissible prime--mode coupling *before* estimating it, prove that the class cannot realize the conjugate-character geometry cheaply, and charge the same norm in both the dephasing lower bound and the analytic family estimate. Otherwise the proposal falls back to one of the two closed extremes: a common vector whose norm cancels from the quartic balance, or a programmable joint matrix that erases oscillation itself.

**Boundary.** The MC-333 tradeoff is exact for the finite reciprocal endpoint, equal one-defect cell multiplicities, Frobenius cost and exact all-mode interpolation. It is not a theorem about every low-rank character model, sparse target vectors, approximate dephasing, unequal endpoint cells, nonlinear statistics or alternative analytic norms. Its durable content is the resource principle: when the dangerous matched filter is itself low-rank, rank must be priced together with the norm cost of realizing it.
