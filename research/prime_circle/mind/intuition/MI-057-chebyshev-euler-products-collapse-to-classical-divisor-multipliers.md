# MI-057 — Chebyshev Euler products collapse to classical divisor multipliers

**Evidence level:** exact operator-theoretic synthesis from [PC-376](../../findings/PC-376-finite-coprime-chebyshev-transfer-families-are-universal-polydisk-shifts.md), [PC-377](../../findings/PC-377-infinite-prime-chebyshev-aggregates-have-sharp-l2-l1-domain-thresholds.md), and [PC-378](../../findings/PC-378-chebyshev-euler-product-collapses-to-classical-zeta-divisor-multiplier.md). The conclusion closes the canonical commuting Euler-product assembly of the Chebyshev quotient; it does not classify noncommuting, matrix-valued or pre-quotient couplings.

After the Chebyshev reduction, the prime refinement operators are commuting backward shifts `P_p`. A natural attempt to repair the nonclosable direct prime sum of PC-377 is to assemble every prime depth multiplicatively:

`Z_s = prod_p^(alg) (I-p^(1-s)P_p)^(-1)`

on the finite-mode core. This product is algebraically well-defined there because only finitely many primes divide a basis index and every local inverse truncates. Unique factorization immediately gives

`Z_s e_n = sum_(d|n) d^(1-s)e_(n/d)`.

Thus the full prime Euler product has already become a classical weighted divisor transform before any analytic completion is chosen.

The operator gate is unchanged. The adjoint basis column has squared norm `sum_d d^(2-2 Re(s))`, so the operator is closable exactly for `Re(s)>3/2`. A prime-column graph witness proves nonclosability at and left of that boundary. Under the Bohr lift, the adjoint is multiplication by

`prod_p (1-p^(1-conj(s))z_p)^(-1)`,

whose Dirichlet-series representative is exactly `zeta(w+conj(s)-1)`. Boundedness is therefore equivalent to `Re(s)>2`, with norm `zeta(Re(s)-1)`.

The explicit appearance of zeta is not new spectral information. It is the ordinary zeta Euler product acting as a Hardy/Dirichlet multiplier, the same weighted divisor mechanism already classified earlier in the line. In particular the source-derived half-density regime remains nonclosable. Replacing prime degrees by matched prime powers moves both thresholds to `1+1/(2r)` and `1+1/r`, so the vertical boundaries are controlled by degree growth and summability, not by an invariant critical line.

This closes a common representation trap: **multiplying universal prime shifts can write zeta explicitly without producing a new zeta-zero mechanism**. Once the finite Chebyshev channels have factorized into independent commuting coordinates, their canonical scalar Euler product reconstructs the classical divisor object rather than restoring source information lost in the quotient.

A surviving Prime-Circle route must therefore break that factorization before or during assembly: noncommuting/matrix cross-shell coupling, nonlinear pre-Chebyshev interaction, or a source-forced domain/topology not equal to the graph closure of the algebraic core. A different scalar packaging of the same commuting shifts -- finite sum, infinite sum or full geometric-series product -- does not escape the matched control.

**Boundary.** PC-378 concerns the canonical commuting Euler product with Jacobian weights inherited from the current Chebyshev model. It does not rule out independently justified nonstandard domains, matrix-valued coefficients, nonlinear operations or cross-shell data destroyed by the Bohr/divisor reduction. The zeta multiplier identity is classical structure; no RH consequence or novelty claim follows from its reappearance.