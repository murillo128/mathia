# MI-056 — Infinite Chebyshev prime sums need ℓ² coefficients before closure

**Evidence level:** exact operator-theoretic synthesis from [PC-374](../../findings/PC-374-half-density-chebyshev-transfer-is-universal-weighted-shift.md), [PC-376](../../findings/PC-376-finite-coprime-chebyshev-transfer-families-are-universal-polydisk-shifts.md), and [PC-377](../../findings/PC-377-infinite-prime-chebyshev-aggregates-have-sharp-l2-l1-domain-thresholds.md). The result concerns the direct scalar all-prime sum on the canonical finite-mode core and its graph closure; it does not classify different topologies or genuinely coupled infinite operators.

On the positive Chebyshev sector, let `P_p=V_p^*` be the prime-degree backward shifts and define algebraically on finite-support modes

`A_a=sum_p a_p P_p`.

This sum is pointwise finite on the core because only prime divisors of a basis index contribute. PC-377 gives the exact first functional-analytic gate:

`A_a is closable iff (a_p) in ell^2`.

The obstruction below `ell^2` is stronger than norm divergence. If finite prime sets have `S_N=sum |a_p|^2 -> infinity`, then normalized vectors built from the prime basis satisfy `x_N->0` while `A_a x_N=e_1`; the graph closure contains `(0,e_1)` and therefore is not the graph of an operator. Conversely, square summability makes the adjoint densely defined on the finite-mode core.

Boundedness has the sharper exact threshold

`A_a bounded iff (a_p) in ell^1`,

with `||A_a||=sum_p |a_p|`. Under the Bohr/infinite-polydisk lift this is the ordinary multiplier norm of a linear coordinate symbol. Infinite channel count therefore creates no new canonical operator merely by formal summation; the coefficient geometry has to enter a valid operator category first.

For the source-derived Jacobian coefficients `a_p(s)=p^(1-s)`, the thresholds become `Re(s)>3/2` for closability and `Re(s)>2` for boundedness. Hence the half-density line `Re(s)=1/2`, where each individual transfer is unitarily gauged to a Chebyshev shift, lies far inside the nonclosable region for the literal all-prime sum. Replacing prime degrees by matched prime powers `p^r` moves the thresholds to `1+1/(2r)` and `1+1/r`, confirming that these vertical boundaries come from degree growth and sequence summability rather than an invariant arithmetic critical line.

The surviving infinite-family question is therefore structural, not cardinal. A viable construction needs coefficients whose `ell^2` admissibility is itself source-forced and arithmetically meaningful, a matrix/nonlinear cross-prime interaction before scalar aggregation, or a different source-forced domain/topology whose operator is not the graph closure of this finite-mode sum. Simply adding infinitely many canonical directions does not escape the finite polydisk universality unless the mode of assembly changes.

**Boundary.** The `ell^2`/`ell^1` classification applies to the scalar sum `sum_p a_p P_p` on the canonical finite-mode core. It does not exclude matrix-valued couplings, nonlinear operations, pre-Chebyshev interactions, independently justified nonstandard domains or other global topologies. The moving prime-power thresholds are controls for the functional-analytic mechanism; no RH implication is inferred.