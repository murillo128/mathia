---
type: adversarial-review
target: research/weil_inertia/findings/WI-188-count-saturating-bows-force-self-dual-twisted-prime-covariance.md
---

# Adversarial review

## Adversary

The passage from count saturation `c=4π+o(1)` to the square-root scale used in Section 4 needs a stronger rate. From `α_*=2π/c=1/2+o(1)` one gets only `x_*=T^{1/2+o(1)}=√T·T^{o(1)}`, not `x_*=√T(1+o(1))`. Consequently

\[
\frac{U}{x_*^2}=\frac{\theta T}{T^{2\alpha_*}}=\theta T^{1-2\alpha_*}
\]

need not stay bounded above and below by positive constants. For example, `α_*=1/2+1/√log T` still satisfies `α_*=1/2+o(1)` but makes `U/x_*^2→0`, while the opposite sign makes it diverge. Thus (23)--(24), and hence the claim of `Θ(h)` lattice aliases per shift at the count-saturating scale, do not follow from WI-184's stated `c=4π+o(1)` asymptotic alone.

Resolve the objection either by proving quantitative saturation strong enough that `(α_*-1/2)log T→0` (for example a sufficient rate `c-4π=o(1/log T)`), or by retaining the factor `U/x_*^2` throughout the derivative/alias analysis and weakening the self-dual stationary-lattice conclusion to the regime actually justified by its asymptotics. The earlier polynomial resolution-barrier calculation using `x_*=T^{1/2+o(1)}` is not the issue; the objection is specifically to upgrading that exponent-level statement to the multiplicative square-root normalization required by Section 4.

## Owner

The objection to the `Θ(h)` statement is correct; no stronger saturation rate is available from WI-184. The main obstruction in WI-188 nevertheless survives after retaining the missing scale factor, without assuming `x_*=√T(1+o(1))`.

Write

\[
\rho_T:=\frac{U}{x_*^2},
\qquad
x_*=T^{\alpha_*},
\qquad
\alpha_*=\frac12+o(1).
\]

Since `U=θT` with `θ` bounded above and below, `\rho_T=T^{1-2\alpha_*}` up to such a bounded factor, hence `\rho_T=T^{o(1)}` but it need not tend to a nonzero constant. For every relevant `h=o(x_*)`, the exact derivative

\[
f_h'(m)=-\frac{Uh}{2\pi m(m+h)}
\]

therefore gives, uniformly on `m\in[x_*,2x_*]`,

\[
|f_h'(x_*)|=\frac{\rho_T h}{2\pi}(1+o(1)),
\qquad
|f_h'(2x_*)|=\frac{\rho_T h}{8\pi}(1+o(1)),
\]

so the derivative sweep has length

\[
\left(\frac{3}{8\pi}+o(1)\right)\rho_T h.
\]

Thus the justified alias count is `O(1+\rho_T h)` in general and is asymptotic to a constant multiple of `\rho_T h` once `\rho_T h\to\infty`; `Θ(h)` is not justified without the stronger rate identified in the objection.

What matters for the no-free-cancellation conclusion is that the *relevant shift range itself* is long enough that `\rho_T h` becomes large. With `H\asymp T^\epsilon/\log T` and

\[
K:=\frac{x_*}{H},
\]

we have

\[
\rho_T K
=\frac{U}{H x_*}
=T^{1-\epsilon-\alpha_*+o(1)}\log T
=T^{1/2-\epsilon+o(1)}\log T\to\infty
\]

for every fixed `0<\epsilon<1/2`. Hence for shifts `h\asymp K` the derivative interval crosses

\[
T^{1/2-\epsilon+o(1)}
\]

integer levels. In particular, even when `\rho_T\to0`, the top part of the required growing-shift range contains arbitrarily many lattice resonances. A uniform first-derivative/Kusmin--Landau dismissal of the entire off-diagonal therefore remains unavailable. If the adversary accepts this repair, the canonical finding should replace the multiplicative `x_*=√T(1+o(1))` and `Θ(h)` assertions by this rate-free `\rho_T` formulation while keeping the finding's central conclusion: the remaining escape is still a genuinely oscillatory shifted-prime covariance problem rather than automatic height-chirp cancellation.

## Adversary

The objection is mathematically resolved. Retaining `ρ_T=U/x_*^2` gives a derivative sweep of order `ρ_T h`, and at the top of the required shift range `K=x_*/H` one has `ρ_T K=U/(H x_*)=T^{1/2-ε+o(1)} log T→∞` for every fixed `0<ε<1/2`. Thus the uniform first-derivative/Kusmin--Landau dismissal still fails even without the unjustified multiplicative square-root normalization.

Closure is pending durable persistence: the current finding still states `x=√T(1+o(1))` in Section 4 and derives `Θ(h)` aliases. Please replace those statements by the rate-free `ρ_T` sweep/alias calculation (or an equivalent valid formulation) while preserving only the central conclusion that the remaining escape is a genuinely oscillatory shifted-prime covariance problem.