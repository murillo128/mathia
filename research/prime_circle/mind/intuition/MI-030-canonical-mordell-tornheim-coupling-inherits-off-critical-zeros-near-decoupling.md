# MI-030 — Canonical Mordell--Tornheim coupling inherits off-critical zeros near decoupling

**Evidence level:** proved for the smallest canonical Prime-Circle pair by [PC-319](../../findings/PC-319-small-mordell-tornheim-coupling-preserves-off-critical-zeros.md), using the classical Saias--Weingartner zero theorem for periodic Dirichlet series and Rouché stability.

The genuinely two-index carrier of PC-316 is not rescued merely by using the exact Prime-Circle coefficient vector. For the canonical `(q,r)=(5,7)` source, the one-level factor `A_5(s)` is provably outside the exceptional `P(s)L(s,chi)` class: its exact residue values violate the multiplicative relation that such a factorization would force.

Saias--Weingartner therefore supplies zeros of `A_5` already in `Re s>1`, inside absolute convergence. Fixing a real `T>1` with nonzero second factor gives the exact decoupled identity

`Z_(5,7)(s,T,0)=A_5(s)B_7(T)`.

Uniform convergence on compact sets as the Mordell--Tornheim coupling `u->0+`, followed by Rouché's theorem, preserves those zeros for **every sufficiently small positive `u`**. The coupled source-specific packet itself therefore has zeros in a fixed disk contained in `Re s>1`; this is not a meromorphic-continuation artifact or a generic-coefficient counterexample.

The lesson is sharper than “multiple zeta functions have complicated zeros.” **Source fidelity and genuine nonseparability still do not imply coordinatewise zero selection.** Near the natural decoupling face, the exact canonical coefficients retain the off-critical zero geometry of their periodic factor.

The live multivariable route must therefore use a destination theorem that is not uniform coordinatewise critical-line confinement near `u=0`: for example a distinguished positive-coupling locus bounded away from the decoupled face, a completion or diagonal mixing several variables, or another invariant of the full zero locus. Merely pointing to the exact coefficient vector or to positive Mordell--Tornheim coupling is no longer evidence for Riemann-like coordinatewise zeros.

**Boundary.** PC-319 does not rule out special diagonals, completions, multivariable divisors, or couplings separated from `u=0`. It rules out only the natural source-specific coordinatewise confinement hope in an open genuinely coupled neighborhood of the decoupled face.
