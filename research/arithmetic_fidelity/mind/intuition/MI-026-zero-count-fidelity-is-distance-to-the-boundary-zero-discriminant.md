# MI-026 — Zero-count fidelity is distance to the boundary-zero discriminant, and that distance can collapse with breadth

**Evidence level:** proved for finite Dirichlet polynomials on a fixed compact Jordan contour by AF-290, with the increasing-breadth eta specialization proved in AF-291; transfer from acquisition remains conditional on the actual coefficient-orbit error.

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

Below this radius the zero count inside the contour is constant by Rouché, and at the radius a boundary collision is reachable. The relevant conditioning is therefore not merely a norm bound on recovered coefficients; it is **distance of the requested analytic target to its own ill-posed locus**.

This distance is compatible with the common-clock quotient from AF-289. The action `b_n -> b_n n^{-i sigma}` translates `P_b(s)` vertically, and the discriminant margin is unchanged when the contour is translated with it. Hence a common timing center is free for a vertically tracked zero-count target, while residual differential jitter matters only through the coefficient-orbit error it produces.

AF-291 shows that the normalized target radius can deteriorate even when the analytic approximation itself behaves perfectly well. For the raw eta truncations

\[
\eta_N(s)=\sum_{n\le N}(-1)^{n-1}n^{-s},
\]

fix a zero-free compact Jordan boundary in `Re(s)>0` and put `alpha=min_Gamma Re(s)`. Local uniform convergence gives a boundary modulus bounded above and below independently of large `N`, but

\[
\delta_{\Gamma,N}
:=
\frac{\operatorname{dist}_2(b^{(N)},\Delta_{\Gamma,N})}{\|b^{(N)}\|_2}
\asymp
\frac1{\sqrt N\,H_N(\alpha)}
\]

and therefore

\[
\delta_{\Gamma,N}\asymp
\begin{cases}
N^{-1/2}, & \alpha>1/2,\\
(N\log N)^{-1/2}, & \alpha=1/2,\\
N^{\alpha-1}, & 0<\alpha<1/2.
\end{cases}
\]

The collapse comes from the growth of the dual boundary-evaluation norm relative to coefficient size, not from the contour approaching a zero. In particular, eventual correctness of the zero count under analytic convergence does not imply robustness to a breadth-independent relative coefficient error.

The composition rule is consequently breadth-sensitive. If a decoder gives relative coefficient-orbit error `eta_N`, the AF-290 gate protects the zero count only while

\[
\eta_N<\delta_{\Gamma,N}.
\]

For raw eta truncations this means the recovery accuracy must tighten with `N`; a fixed relative recovery guarantee cannot be promoted to a uniform zero-count theorem through this geometry alone.

The reusable lesson is that **source completeness, analytic convergence, and target-conditioned robustness can move in opposite directions as breadth increases**. Adding coordinates may improve approximation while simultaneously shrinking the perturbation ball in the upstream norm that preserves the final discrete target.

**Boundary.** AF-291 is a statement about the raw eta coefficient geometry on fixed compact contours. It does not prove that every RH-relevant representation has a collapsing margin, nor does it rule out a preconditioned norm, nonlinear representation, quotient, or target geometry with a better breadth law. It controls finite zero count, not global zero matching, exact ordinates, or RH.
