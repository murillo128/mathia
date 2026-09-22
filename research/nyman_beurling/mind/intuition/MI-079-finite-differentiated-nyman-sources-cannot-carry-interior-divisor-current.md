# MI-079 — Finite differentiated Nyman sources cannot carry an interior divisor current

**Evidence level:** exact complex-analytic obstruction from [NB-278](../../findings/NB-278-finite-differentiated-nyman-sources-have-identically-zero-interior-divisor-current.md), sharpening the legal-realization boundary of MI-078.

For every finite Dirichlet polynomial `P`, the canonical differentiated Nyman current

`C_P(s)=-zeta(s)(P'(s)-P'(1))`

is entire. The subtraction at `s=1` cancels the Euler pole, and finite differentiation introduces no poles elsewhere. Consequently its interior divisor current vanishes identically: `bar-partial C_P=0` in every compact region away from the boundary representation.

The limiting source-native Ford current is categorically different. For `P_*=1/zeta`, meromorphic continuation gives

`C_0=zeta'/zeta+zeta`,

whose residues at the nontrivial zeros produce a nonzero interior divisor current. Since distributional `bar-partial` is continuous, no sequence of finite currents of the form `C_P` can converge distributionally across a neighborhood containing a zeta zero to `C_0`. Coefficient growth, Hardy-norm blowup or signed Möbius cancellation inside the finite polynomials cannot change this topological mismatch.

This closes the direct finite linear-truncation route left by MI-078. The obstruction is stronger than bad conditioning of the logarithmic derivative: finite legal differentiated sources live in the zero-divisor-current class, while the desired continued object does not. A successful realization must change how the singular information enters rather than merely choose better finite coefficients.

The surviving mechanisms are therefore architectural: a boundary/contour identity whose boundary term survives the finite stage, a moving or pinching contour, a nonlinear operation capable of creating poles, or another limit in which singularity formation is explicit and its Hardy/Nyman cost can be controlled. The next useful calculation is the exact finite boundary representation before meromorphic continuation, not another interior finite-polynomial approximation to the continued current.

**Boundary.** NB-278 rules out distributional convergence on neighborhoods containing zeta zeros for this finite differentiated linear Nyman architecture. It does not rule out boundary-only convergence, contour limits, nonlinear regularizations, singular limits outside compact neighborhoods of zeros, or other source classes. It proves no Hardy lower bound and does not promote the separate proposed NB-273--NB-275 chain.