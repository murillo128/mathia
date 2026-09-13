# MI-021 — Endpoint-optimal detection needs flat-vector cancellation; uniform operator norms hit the blind threshold

**Evidence level:** exact for the support threshold and basis reductions through [MC-264](../../findings/MC-264-support-matched-high-moment-blind-threshold.md)--[MC-267](../../findings/MC-267-krawtchouk-source-hierarchy-amplitude-duality.md), for the endpoint-optimal detector through [MC-268](../../findings/MC-268-christoffel-endpoint-detector.md), for its exact sparse second-moment form through [MC-269](../../findings/MC-269-christoffel-flat-sparse-quadratic-large-sieve-energy.md), and for the coefficient-uniform obstruction through [MC-270](../../findings/MC-270-uniform-large-sieve-blind-atom-threshold.md). The required flat-vector arithmetic cancellation remains open.

Let `B_m` be the lower-prime subsets of size at most `m`, `Z=|B_m|`, and let the rows `T` be fixed-weight products of shell primes, with `C` rows. The Christoffel endpoint detector turns blind-relation exclusion into the exact flat energy

`F=||A 1_Z||_2^2`, where `A_(T,S)=chi_T(q_S)`.

Its natural diagonal is `CZ`. A blind row has every entry equal to one and contributes exactly `Z^2`, so any upper bound `F<=L_y CZ` excludes blindness only when

`L_y < Z/C`.

At the live choice `m=t+1`, `Z/C~k_y/(t+1)`, which is precisely the previously identified loss budget.

MC-270 shows that the usual coefficient-uniform large-sieve relaxation destroys exactly this budget. Every row of `A` has Euclidean norm `sqrt(Z)`, hence

`||A||_op^2 >= Z`.

Therefore any valid inequality `||Aa||_2^2<=D_y||a||_2^2` for every coefficient vector has `D_y>=Z`. Applying it to `1_Z` yields a certified right-hand side at least `Z^2`, already as large as one blind atom. In the normalized language `D_y<=L_y C`, uniformity forces `L_y>=Z/C`, exactly opposite to the strict inequality needed for exclusion.

This obstruction survives even an ideal arithmetic row geometry. Orthogonal rows already have operator norm squared `Z`. Passing to the adjoint, Hilbert-space duality or Cauchy--Schwarz cannot repair it because these preserve the same unrestricted operator norm. The missing gain is not hidden in a better estimate of the full coefficient space.

The residual is a **flat-source discrepancy theorem**. One must use that every source coefficient is exactly one before uniformization, for example by controlling

`<1_Z,A^*A1_Z>-CZ`

directly through signed off-diagonal cancellation. A genuinely narrower structured coefficient class could also work, but only if its own worst direction stays strictly below the blind-row scale while still containing the flat source vector.

The durable lesson is that detector optimization and family sparsity do not justify coefficient uniformization. **When one exceptional atom sits exactly at the operator-norm floor, preserving the distinguished source vector is part of the arithmetic information.**

**Boundary.** MC-270 does not show that the desired flat energy is large, construct a blind row, or disprove diagonal-scale cancellation. It rules out proof architectures whose decisive arithmetic estimate first replaces the flat source vector by arbitrary coefficients. Weighted/preconditioned variants remain possible only after translating their gain back to the original blind-row atom.