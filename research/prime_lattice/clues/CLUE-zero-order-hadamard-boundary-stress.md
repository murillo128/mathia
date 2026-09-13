---
id: CLUE-prime-lattice-zero-order-hadamard-boundary-stress
type: research-clue
status: accepted
origin: research-watch
target_line: prime_lattice
based_on:
  - research/prime_lattice/findings/PL-284-compact-window-0-8-simple-even-ground-gap.md
  - research/prime_lattice/findings/PL-289-one-dimensional-weil-graph-domain-squared-log-moment.md
  - research/prime_lattice/findings/PL-293-optimal-log-boundary-hhalf-obstruction.md
  - research/prime_lattice/findings/PL-294-exact-preprime-beurling-deny-threshold.md
  - research/prime_lattice/findings/PL-295-hlog-hhalf-sign-cone-eventual-positivity-obstruction.md
  - research/prime_lattice/findings/PL-297-renormalized-hadamard-stress-hhalf-decoupling.md
  - research/prime_lattice/findings/PL-298-fixed-order-fractional-shift-autocorrelation-c1.md
  - research/prime_lattice/findings/PL-299-uniform-bv-principal-shift-derivative-limit.md
---

# Can a zero-order Hadamard boundary stress differentiate the localized Weil ground branch without `H^{1/2}`?

## Observation

`PL-293` shows that the canonical zero-exterior logarithmic-Laplacian boundary channel is of order

\[
\ell(\delta)^{1/2},\qquad \ell(\delta)=\frac1{|\log\delta|},
\]

and that a nonzero channel of this size excludes zero-extension `H^{1/2}`. This blocks the routine absolute-first-frequency-moment differentiation of moving translation autocorrelations. `PL-289` gives all finite logarithmic Fourier moments for localized-Weil eigenstates, but no positive Sobolev power; `PL-294`--`PL-295` also remove generic semigroup-positivity and topological sign-continuation shortcuts.

There is, however, a nearby shape-calculus mechanism that does not start by differentiating translation correlations. Djitte--Fall--Weth's fractional Hadamard formula says that for the positive normalized principal Dirichlet eigenfunction `u_s` of `(-Delta)^s`, a smooth domain deformation with velocity `X` satisfies

\[
\lambda_s'(0)=\Gamma(1+s)^2
\int_{\partial\Omega}
\left(\frac{u_s}{\delta^s}\right)^2 X\!\cdot\nu\,d\sigma,
\]

where `nu` is their interior normal. On the symmetric interval `Omega=(-1,1)`, dilation by `1+epsilon` also gives exactly

\[
\lambda_s((1+\varepsilon)\Omega)
=(1+\varepsilon)^{-2s}\lambda_s(\Omega).
\]

Evenness of the principal state therefore forces the exact endpoint identity

\[
\boxed{
\Gamma(1+s)^2
\left(\frac{u_s}{\delta^s}\Big|_{x=\pm1}\right)^2
=s\lambda_s(\Omega).
}
\]

Feulefack--Jarohs--Weth prove `lambda_s=1+s lambda_L+o(s)` and convergence of the normalized fractional principal eigenfunction to the logarithmic-Laplacian principal eigenfunction as `s->0+`. Hence the fractional normal trace has the forced scale

\[
\frac1{\sqrt s}
\frac{u_s}{\delta^s}\Big|_{x=\pm1}
\longrightarrow1
\]

for the pure normalized interval problem. This is a precise indication that a **renormalized zero-order boundary stress** exists in the fractional approximation, even though the limiting logarithmic eigenfunction is not expected to have an ordinary normal derivative.

The observation is not yet a logarithmic Hadamard theorem. The limits `delta->0` and `s->0` are singular and need not commute: the fractional trace describes the `delta^s` boundary layer for each fixed `s`, whereas the limiting logarithmic profile lives on the `ell(delta)^{1/2}` scale. A targeted literature audit located the fractional Hadamard theorem and the small-order spectral/eigenfunction convergence, but not a theorem identifying the renormalized fractional trace with a boundary trace of the logarithmic Laplacian, nor a corresponding shape formula for Suzuki's bounded prime-shift perturbation.

## Research question

Can the domain dependence of the **actual localized completed-Weil simple ground branch** be differentiated through a zero-order Hadamard formula whose boundary observable is the `s->0` renormalization of the fractional Dirichlet trace, rather than through an `H^{1/2}` Fourier moment?

More concretely, construct a fractional regularization of the moving-domain localized Weil form that converges to Suzuki's canonical operator and ask whether, for a simple eigenbranch, the shape derivative has a limit of the form

\[
\lambda_a'
=\mathcal B_a(\tau_{a,-},\tau_{a,+})
+\mathcal A_a,
\]

where `tau_{a,+/-}` are well-defined logarithmic boundary stresses obtained from a renormalized fractional trace and `mathcal A_a` is an explicitly controlled contribution of the completed arithmetic/archimedean remainder. The crucial requirement is that this identity be proved directly in the moving-domain representation, so it genuinely bypasses the absolute differentiation mechanism ruled out by `PL-293` rather than hiding the same `H^{1/2}` assumption after pullback to a fixed interval.

## Why it may matter

At `a=0.8`, `PL-284` gives a certified simple even ground state and a spectral gap, but the available transport estimates are far too weak to propagate its tiny positive margin. A genuine shape derivative would replace worst-case translation moduli by a state-specific scalar observable. If the derivative can be expressed through two endpoint stresses plus an explicit arithmetic term, the first-crossing problem becomes a boundary-control problem rather than a high-frequency norm-continuity problem.

The fractional calculation also supplies a normalization that is not chosen to fit zeta: the `sqrt(s)` factor is forced by exact scaling and the Hadamard identity before any prime data are inserted. That makes the route falsifiable. Any RH relevance would still have to come from how the completed rational-prime eigen-equation constrains the limiting stress or the remainder term; the pure logarithmic operator provides only the universal boundary calculus.

## Decisive test

Work in the original moving support interval, not only in the fixed-domain rescaling. First define a family whose principal part is `(((-Delta)^s)-I)/s` (with the normalization chosen to converge to the logarithmic principal operator) and whose lower-order part converges to the same completed Weil prime/archimedean remainder. Prove form or norm-resolvent convergence strong enough to track the isolated simple branch near `a=0.8`.

Then establish all of the following, or kill the route at the first failure:

1. a Hadamard formula for the regularized simple eigenvalue in which every lower-order prime-shift/completion contribution is explicit and uniformly controlled as `s->0+`;
2. compactness and uniqueness for the renormalized boundary traces `s^{-1/2}(u_{s,a}/delta^s)|_{partial I_a}` (or an honestly weaker boundary measure), with a limit intrinsic to the logarithmic eigenstate rather than to the chosen regularization;
3. a proof that the limiting identity exists without assuming zero-extension `H^{1/2}` or absolute first-frequency-moment integrability;
4. a matched-control calculation for the pure logarithmic operator and for perturbed prime weights. The universal boundary-stress term must not be mistaken for arithmetic rigidity; a useful Weil conclusion must depend on a rational-prime-specific constraint on the limiting stress or on the explicit remainder;
5. compatibility across a prime-power source activation. A formula valid only on one source-static interval is still useful locally, but any first-crossing argument must state what happens when a new fixed translation enters.

A decisive negative outcome is any of: renormalized traces have no regularization-independent limit; the lower-order compressed shifts contribute an uncontrolled term of the same order; the putative formula requires precisely the `H^{1/2}` hypothesis it was meant to avoid; or the resulting derivative is universal under matched nonarithmetic weight replacements and supplies no source-specific control of the sign.

## Evidence boundary

The fractional Hadamard formula is prior art: Sidy Moctar Djitte, Mouhamed Moustapha Fall and Tobias Weth, *A fractional Hadamard formula and applications*, Calc. Var. PDE **60** (2021), 231, DOI `10.1007/s00526-021-02094-3`. The small-order spectral and eigenfunction convergence is prior art: Pierre Aime Feulefack, Sven Jarohs and Tobias Weth, *Small Order Asymptotics of the Dirichlet Eigenvalue Problem for the Fractional Laplacian*, J. Fourier Anal. Appl. **28** (2022), 18, DOI `10.1007/s00041-022-09908-8`.

The displayed `sqrt(s)` endpoint normalization on `(-1,1)` is an immediate exact consequence of those established formulas and scaling; it is a control calculation, not a new zeta mechanism. No theorem has been established here that the renormalized fractional trace converges to the coefficient of the logarithmic `ell(delta)^{1/2}` boundary law, that Suzuki's completed-Weil perturbation admits the same Hadamard formula, or that any resulting stress has the sign needed for RH. Those are precisely the missing statements that keep this as a clue rather than a finding.

## Research disposition

Outcome: accepted as a narrow technical route; no logarithmic Hadamard theorem or arithmetic sign mechanism is established.

A structure-based prior-art audit strengthens the fixed-order side of the proposal but leaves its decisive small-order step open. Djitte--Sueur, *Pointwise Hadamard variational formula for the fractional Laplacian* (arXiv:`2602.07214`, 2026), prove shape differentiability for fixed `s in (0,1)` and express the derivative through fractional boundary traces. Feulefack--Jarohs--Weth prove more small-order compactness than the original observation used: on regular bounded domains the relevant fractional eigenfunctions are relatively compact in `C_0` and converge uniformly on the closure, with an `s`-uniform bound of the form `|u_s(x)| <= C delta(x)^s` for small `s`. None of these results gives convergence of the quotient trace `u_s/delta^s`, however, and uniform convergence of `u_s` itself cannot control that singular boundary quotient. The required `s^{-1/2}` trace limit therefore remains a genuine analytic gate rather than a consequence already present in the literature audited here.

`PL-297` sharpens the distinction further: for the pure fractional/logarithmic interval branch, the renormalized Hadamard trace has a finite nonzero limit while the zero-extension `H^{1/2}` norms necessarily diverge. Thus boundary stress cannot be used as a proxy for the critical first-frequency moment. The route remains viable only if the lower-order moving shifts and completed remainder admit their own direct fixed-order shape contribution with an independently controlled `s->0` limit.

`PL-298` now removes one fixed-order obstruction from that remaining task. If a compactly supported state belongs to `W^{1,1} cap L^infty`, its translation autocorrelation is `C^1`; the standard fractional Dirichlet boundary estimates put the pure fixed-`s` principal state in exactly this class. The discrete prime-power term can therefore be differentiated in physical space without invoking a uniform `H^{1/2}` moment, and because both the autocorrelation and its first derivative vanish at the support edge, a new prime-power channel activates `C^1` rather than with a cusp. This advances decisive tests 1 and 5 at fixed `s`, but it does **not** supply the missing theorem for the actual boundedly perturbed completed-Weil eigenstate or the uniform `s->0` passage.

`PL-299` closes that uniform passage for the **pure principal fractional/logarithmic interval branch**. Uniform convergence of the positive principal eigenfunctions, their symmetric-decreasing shape, and the uniform `L^infty` bound imply a uniform BV bound `TV(u_s)=2u_s(0)`. Weak-star compactness of the derivative measures then upgrades the autocorrelations to `C_s -> C_0` in `C^1(R)`. Thus the pure prime-shift derivatives converge uniformly through `s->0+` despite the divergent `H^{1/2}` norms. The unresolved shift gate is now specifically a **perturbed-branch BV/finite-measure compactness problem**: establish uniform BV (or an equivalent derivative-measure compactness) plus uniform `C_0` convergence for the actual regularized completed-Weil eigenstate. This does not resolve the renormalized Hadamard trace, completion term, or arithmetic sign mechanism.

There is also a sharp matched control on what such a limit could mean. For the pure logarithmic principal operator, spatial dilation shifts the Dirichlet spectrum by the universal logarithmic scale term (equivalently, the multiplier `log|xi|` acquires `-log R` under dilation). Thus the principal-part shape response is universal and cannot itself be rational-prime rigidity. Any useful Weil derivative must obtain its non-universal content from the completed arithmetic/archimedean remainder or from a state-dependent boundary stress whose limiting law changes under a matched nonarithmetic replacement of the prime weights.

The exact unresolved question is therefore narrower than the proposal: can the small-`s` regularization of the actual isolated completed-Weil branch produce a regularization-independent limit of `s^{-1/2}(u_{s,a}/delta^s)|_{partial I_a}` (or an intrinsic boundary measure), **and** uniform BV/derivative-measure compactness strong enough to transport `C'_{u_{s,a}}(log n/a)` for the active prime-power shifts, together with a Hadamard identity whose remaining completion term is uniformly controlled by the rational-prime source, without importing `H^{1/2}` or absolute first-frequency-moment differentiability? Failure of trace compactness/uniqueness, loss of BV/shift-derivative compactness or bounded-remainder control, or persistence of the same limiting derivative under matched nonarithmetic source weights rejects the route.