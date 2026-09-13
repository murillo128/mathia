# PL-297 — Renormalized fractional Hadamard stress can stay finite while the critical `H^{1/2}` channel diverges

**Evidence:** `LITERATURE+EXACT-DERIVED + NEGATIVE/ROUTE-RESTRICTION + MATCHED-CONTROL`

**Status:** `TRACE-MOMENT-DECOUPLING + H-HALF-BLOWUP + HADAMARD-ROUTE-NARROWED`

## Claim

The zero-order fractional Hadamard boundary trace and the critical half-Sobolev frequency moment are genuinely different singular observables in the small-order limit.

Let `I_R=(-R,R)` be an interval chosen small enough that the principal Dirichlet eigenvalue `lambda_{1,L}(I_R)` of the logarithmic Laplacian is positive. For `s>0`, let `u_s` be the positive `L^2(I_R)`-normalized principal zero-exterior Dirichlet eigenfunction of `(-Delta)^s`, and let

\[
\tau_s
:=\left.\frac{u_s}{\delta^s}\right|_{x=R}
=\left.\frac{u_s}{\delta^s}\right|_{x=-R},
\]

where equality follows from interval symmetry. Then:

\[
\boxed{
\Gamma(1+s)^2\tau_s^2
=\frac{s}{R}\lambda_{1,s}(I_R),
\qquad
\frac{\tau_s}{\sqrt s}\longrightarrow R^{-1/2}.
}
\]

At the same time, if every `H^{1/2}` norm below is understood in the extended sense with value `+infinity` when the zero extension does not belong to `H^{1/2}(R)`, then

\[
\boxed{
\|E u_s\|_{H^{1/2}(\mathbb R)}\longrightarrow+\infty
\qquad(s\to0^+).
}
\]

Thus a perfectly finite, nonzero renormalized Hadamard stress can coexist with divergence of the exact critical frequency moment that routine absolute differentiation of translated autocorrelations would require. In particular, convergence of `s^{-1/2}(u_s/delta^s)|_{partial I_R}` cannot by itself provide the missing uniform `H^{1/2}` control in the accepted zero-order Hadamard clue.

This does **not** reject that clue. It sharpens its proof obligation: a successful fractional regularization of the completed localized-Weil branch must derive and pass to the limit in the lower-order prime-shift/remainder shape contribution directly. It cannot use convergence of the boundary stress as a surrogate for the `H^{1/2}` route already blocked by `PL-293`.

## 1. Exact fractional stress from scaling and Hadamard variation

Djitte--Fall--Weth prove that for the positive normalized principal Dirichlet eigenfunction of `(-Delta)^s`, a smooth domain deformation has shape derivative

\[
\lambda_s'(0)
=\Gamma(1+s)^2
\int_{\partial\Omega}
\left(\frac{u_s}{\delta^s}\right)^2
X\!\cdot\nu\,d\sigma,
\]

with their normal convention. For the dilation `Phi_epsilon(x)=(1+epsilon)x` of `I_R`, fractional scaling gives independently

\[
\lambda_{1,s}((1+\varepsilon)I_R)
=(1+\varepsilon)^{-2s}\lambda_{1,s}(I_R),
\]

hence

\[
\frac d{d\varepsilon}\Big|_{0}
\lambda_{1,s}((1+\varepsilon)I_R)
=-2s\lambda_{1,s}(I_R).
\]

At the two endpoints the boundary trace has the same magnitude and `|X dot nu|=R`; matching the sign convention to the expanding-domain derivative therefore gives

\[
2R\,\Gamma(1+s)^2\tau_s^2
=2s\lambda_{1,s}(I_R),
\]

which is the first boxed identity.

Feulefack--Jarohs--Weth prove the small-order expansion

\[
\lambda_{1,s}(I_R)
=1+s\lambda_{1,L}(I_R)+o(s),
\]

and convergence of the normalized positive principal eigenfunction to the unique positive logarithmic-Laplacian principal eigenfunction. Since `Gamma(1+s)->1`, the exact stress identity immediately yields

\[
\frac{\tau_s}{\sqrt s}
\longrightarrow R^{-1/2}.
\]

No boundary-layer interchange is used in this limit: it comes entirely from the fixed-`s` Hadamard formula and exact spatial scaling.

## 2. The logarithmic limit is not in zero-extension `H^{1/2}`

The same fractional scaling and first-order expansion give the logarithmic eigenvalue scaling law

\[
\lambda_{1,L}(I_R)
=\lambda_{1,L}(I_1)-2\log R.
\]

Hence `R` can be chosen small enough that `lambda_{1,L}(I_R)>0`. Let `u_0` denote the positive normalized principal logarithmic-Laplacian eigenfunction on this interval. Feulefack--Jarohs--Weth give `u_0 in C_0(I_R)` and

\[
L_\Delta u_0=\lambda_{1,L}(I_R)u_0\ge0.
\]

The Hopf theorem of Hernández-Santamaría--López Ríos--Saldaña therefore applies at each endpoint. Writing `t=R-x`, for sufficiently small positive `t` there is `c>0` such that

\[
u_0(R-t)\ge
c\,\ell(t)^{1/2},
\qquad
\ell(t)=\frac1{|\log t|}.
\]

For the zero extension, the one-dimensional `H^{1/2}` Gagliardo seminorm contains the cross-boundary term

\[
[E u_0]_{H^{1/2}}^2
\ge C
\int_0^\varepsilon
\frac{|u_0(R-t)|^2}{t}\,dt.
\]

The Hopf lower law gives

\[
\int_0^\varepsilon
\frac{|u_0(R-t)|^2}{t}\,dt
\ge c^2
\int_0^\varepsilon
\frac{dt}{t|\log t|}
=+\infty.
\]

Thus

\[
\boxed{E u_0\notin H^{1/2}(\mathbb R).}
\]

This is exactly the endpoint obstruction isolated abstractly in `PL-293`, now applied to the principal logarithmic eigenbranch used as the small-order fractional control.

## 3. Weak compactness forces the `H^{1/2}` norms to diverge

Feulefack--Jarohs--Weth prove

\[
E u_s\longrightarrow E u_0
\quad\text{strongly in }L^2(\mathbb R)
\]

as `s->0+` (indeed they prove stronger compactness on regular domains). Suppose the extended `H^{1/2}` norms did **not** tend to infinity. Then there would be a sequence `s_j->0` and a finite `C` such that

\[
\|E u_{s_j}\|_{H^{1/2}}\le C.
\]

By weak compactness of the Hilbert space `H^{1/2}(R)`, a subsequence would converge weakly in `H^{1/2}` to some `v in H^{1/2}`. The continuous embedding into `L^2` gives weak `L^2` convergence to the same `v`, while the established strong `L^2` convergence identifies `v=E u_0`. This contradicts `E u_0 notin H^{1/2}`.

Therefore

\[
\boxed{
\|E u_s\|_{H^{1/2}(\mathbb R)}\to+\infty.
}
\]

The argument deliberately does not require a separate fixed-`s` global regularity theorem saying that every `u_s` belongs to `H^{1/2}`. If a particular small `s` has infinite half-Sobolev norm, the extended-norm statement already holds; if all are finite, their norms must nevertheless diverge.

## 4. What this says about the live Hadamard route

The two limits measure different parts of the singular boundary crossover. For each fixed `s>0`, `u_s/delta^s` measures the ultimate fractional `delta^s` layer right at the boundary. The `s->0` logarithmic profile spreads over a much wider scale and saturates the critical `ell(delta)^{1/2}` law. The latter is what makes the half-Sobolev/absolute-first-frequency channel diverge.

Consequently, even an ideal proof of compactness and uniqueness for

\[
s^{-1/2}\left.\frac{u_{s,a}}{\delta^s}\right|_{\partial I_a}
\]

for a fractional regularization of the actual localized-Weil eigenbranch would **not** automatically justify differentiating every translated prime term by an `H^{1/2}` estimate. The lower-order moving shifts must have their own direct shape derivative or a source-specific conditional/cancellation argument whose `s->0` limit is controlled independently.

This separation is useful rather than fatal to the clue. A genuine Hadamard formula could still bypass `H^{1/2}` precisely because fixed-order shape calculus can exist without uniform critical Sobolev control. What is ruled out is the shortcut

\[
\text{finite renormalized boundary stress}
\Longrightarrow
\text{uniform }H^{1/2}
\Longrightarrow
\text{routine absolute shift differentiation}.
\]

## 5. Matched control and arithmetic boundary

Everything proved above holds for the pure interval fractional/logarithmic principal branch and contains no prime data. It is therefore a matched nonarithmetic control, not rational-prime rigidity. The finite stress and divergent `H^{1/2}` channel are consequences of universal nonlocal boundary scaling.

For the prime-lattice program, arithmetic relevance can only enter after the universal principal part is coupled to the completed Weil remainder. A successful continuation argument must show that the rational-prime lower-order term has a well-defined shape contribution and imposes a sign, cancellation, or boundary relation that fails for admissible nonarithmetic weight replacements. The present result supplies no such sign theorem.

It also does not show that the certified `a=0.8` localized-Weil ground state has a nonzero logarithmic Hopf coefficient. `PL-293` kept that source-specific possibility open. The small-interval pure operator is used only as a decisive control showing that boundary-trace convergence and critical Sobolev control are logically independent.

## 6. Prior-art and novelty audit

The three load-bearing external ingredients are established literature:

- Djitte--Fall--Weth (2021): the fractional Hadamard formula with the boundary quotient `u_s/delta^s`;
- Feulefack--Jarohs--Weth (2022): `lambda_{1,s}=1+s lambda_{1,L}+o(s)` and convergence/positivity of the principal eigenfunctions in the small-order limit;
- Hernández-Santamaría--López Ríos--Saldaña (2025): the sharp `ell(delta)^(1/2)` logarithmic boundary law and Hopf lower estimate for nontrivial nonnegative supersolutions.

A targeted search through current small-order fractional-Laplacian, fractional shape-calculus, boundary-trace, and Sobolev-regularity literature found these ingredients and recent fixed-order Hadamard refinements, but did not surface the exact combined statement that the renormalized principal fractional boundary trace stays finite while the zero-extension `H^{1/2}` norm necessarily diverges as `s->0+`. No broad originality claim is made: the mathematical delta is the exact weak-compactness consequence and its use as a guardrail for the accepted localized-Weil Hadamard route.

The result is not RH evidence and does not identify a new zeta invariant. It is a source-independent route restriction that prevents one singular observable from being substituted for another.

## 7. Decisive boundaries

1. **No claim about the actual Weil boundary coefficient.** The Hopf lower law is invoked on a deliberately small pure logarithmic interval where the principal eigenvalue is positive. The rational-prime localized-Weil branch may suppress that channel.
2. **No interchange of `s->0` and `delta->0`.** Their noncommutation is the point. The fractional trace is taken at fixed `s`; the logarithmic lower law belongs to the limiting operator.
3. **No fixed-`s` `H^{1/2}` regularity assumption.** The divergence proof uses only the impossibility of a bounded half-Sobolev subsequence.
4. **No arithmetic conclusion from a universal control.** The matched pure operator has no prime weights. Any RH-facing use must come from the explicit completed-Weil remainder.
5. **The Hadamard clue remains live.** The route is rejected only if the lower-order shape contribution cannot be defined or controlled without re-importing the forbidden absolute first-frequency moment. A direct shape-calculus identity would evade this obstruction rather than contradict it.

## 8. Consequence for `prime_lattice`

The current transport frontier should keep the two singular resources separate:

\[
\boxed{
\text{boundary stress is a shape-calculus observable,}
\qquad
H^{1/2}\text{ is a translation-moment observable.}
}
\]

The first can remain finite after the natural `sqrt(s)` renormalization while the second diverges. Therefore the next meaningful test of the zero-order Hadamard route is not another attempt to infer positive-order regularity from the boundary trace. It is a direct fixed-`s` shape derivative for the **full regularized completed-Weil operator**, followed by an independent `s->0` limit of its arithmetic remainder.

## Literature anchors

- Sidy Moctar Djitte, Mouhamed Moustapha Fall, Tobias Weth, “A fractional Hadamard formula and applications,” *Calculus of Variations and Partial Differential Equations* **60** (2021), Article 231. DOI: `10.1007/s00526-021-02094-3`.
- Pierre Aime Feulefack, Sven Jarohs, Tobias Weth, “Small Order Asymptotics of the Dirichlet Eigenvalue Problem for the Fractional Laplacian,” *Journal of Fourier Analysis and Applications* **28** (2022), Article 18. DOI: `10.1007/s00041-022-09908-8`.
- Víctor Hernández-Santamaría, Luis Fernando López Ríos, Alberto Saldaña, “Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian,” *Discrete and Continuous Dynamical Systems* **45**(1) (2025), 1–36. DOI: `10.3934/dcds.2024084`.
