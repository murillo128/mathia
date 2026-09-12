# MI-026 — Zero-count fidelity is controlled by distance to the boundary-zero discriminant

**Evidence level:** proved for finite Dirichlet polynomials on a fixed compact Jordan contour by AF-290; transfer from the AF-289 timing channel remains conditional on the stated coefficient-orbit error bound.

For

\[
P_b(s)=\sum_{n=1}^N b_n n^{-s},
\]

let `Delta_Gamma` be the coefficient vectors whose Dirichlet polynomial has a zero on a compact Jordan boundary `Gamma`. AF-290 identifies the exact Euclidean robustness radius

\[
\operatorname{dist}_2(b,\Delta_\Gamma)
=
\min_{z\in\Gamma}
\frac{|P_b(z)|}{\left(\sum_{n\le N}n^{-2\operatorname{Re}z}\right)^{1/2}}.
\]

Below this radius the zero count inside the contour is constant by Rouché, and at the radius a boundary collision is already reachable. The relevant conditioning is therefore not merely a norm bound on recovered coefficients; it is **distance of the requested analytic target to its own ill-posed locus**.

This distance is compatible with the common-clock quotient from AF-289. The action `b_n -> b_n n^{-i sigma}` translates `P_b(s)` vertically, and the discriminant margin is unchanged when the contour is translated with it. Hence a common timing center is free for a vertically tracked zero-count target, while residual differential jitter matters only through the coefficient-orbit error it produces.

The composition rule is explicit. If the coefficient decoder gives relative orbit error

\[
\eta
\le K\left(e^{r(\tau)\log N}-1\right),
\]

then zero-count fidelity follows only when

\[
\eta
<
\delta_\Gamma(b)
:=
\frac{\operatorname{dist}_2(b,\Delta_\Gamma)}{\|b\|_2}.
\]

The two factors are independent resources: a perfectly conditioned acquisition channel can still sit arbitrarily close to a target discontinuity. AF-290 gives fixed-`N` examples with `delta_Gamma -> 0`, so no uniform target theorem exists without an additional separation hypothesis.

**Boundary.** This is a finite-Dirichlet, fixed-contour zero-count statement. It does not control infinite Dirichlet series, global zero matching, exact zero ordinates, analytic continuation, or RH. Fixed-height windows retain absolute clock provenance and do not inherit the same quotient invariance. The live arithmetic question is whether a natural RH-relevant family supplies a nonvanishing normalized discriminant margin, or whether that margin necessarily collapses as the source breadth grows.
