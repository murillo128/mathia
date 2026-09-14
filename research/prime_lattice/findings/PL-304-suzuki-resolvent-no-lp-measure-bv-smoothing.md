# PL-304 — The localized-Weil resolvent has no unstructured `L^p` or finite-measure route into `BV`

**Evidence:** `EXACT-DERIVED + DECISIVE-REGULARITY-OBSTRUCTION`

**Status:** `ALL-LP-BV-SMOOTHING-CLOSED + GENERAL-MEASURE-BV-EXTENSION-CLOSED + SOURCE-STRUCTURED-RANGE-STILL-OPEN`

## Claim

`PL-303` shows that the certified odd-sector gap at aperture `a=0.8` does not make the exact localized-Weil resolvent a bounded map from ordinary `L^2` forcing into `BV_0`. The same canonical high-frequency packets in fact rule out every unstructured `L^p` forcing norm and every bounded finite-measure extension.

Let `I=(-1,1)`, let `\widetilde A_a` denote Suzuki's fixed-domain localized completed-Weil operator, and let `\widetilde A_a^-` be its odd restriction. For fixed `a>0` and `z\in\rho(\widetilde A_a^-)`, write

\[
R^-_{a,z}=(\widetilde A_a^- -z)^{-1}.
\]

Then for every `2<=p<=infinity`, the restriction of the Hilbert resolvent to odd `L^p(I)` is not bounded into

\[
BV_0(I)=\{u\in L^1(I):Eu\in BV(\mathbb R)\}.
\]

For every `1<=p<2`, there is no bounded extension

\[
\mathcal R_p:L^p_{\rm odd}(I)\longrightarrow BV_0(I)
\]

that agrees with `R^-_{a,z}` on the common `L^2\cap L^p` forcing domain. Equivalently, no ordinary `L^p` right-hand-side estimate can turn the odd inverse into a `BV` estimate, for any `p`.

The obstruction also reaches the natural finite-measure forcing space. There is no bounded operator

\[
\mathcal R_{\mathcal M}:\mathcal M_{\rm odd}(I)\longrightarrow BV_0(I)
\]

from finite complex Radon measures that agrees with the Hilbert resolvent on absolutely continuous odd `L^2` data.

At the certified `a=0.8` ground parameter `z=\lambda_1`, this applies in particular to the actual odd inverse used by the simple-even ground-branch program. Thus the option left open in `PL-303` cannot be interpreted as a **general** stronger Banach or finite-measure coercivity theorem. Any surviving estimate must be restricted to a genuinely source-structured forcing class, exploit cancellation in the exact differentiated equation, or use a graph norm that already prices linear spatial frequency.

## 1. The exact canonical graph cost is `O(log K)` even in `L^infinity`

Choose a nonzero real even cutoff

\[
\chi\in C_c^\infty(I)
\]

and set

\[
v_K(x)=\chi(x)\sin(Kx).
\]

As in `PL-303`, `v_K` is odd, belongs to the operator core, has `L^2` norm bounded above and below for large `K`, and its zero extension is smooth with compact support strictly inside `I`.

Write the exact fixed-domain operator as

\[
\widetilde A_a=T+K_a,
\]

where `T` is the compressed one-dimensional logarithmic principal operator and `K_a` is the bounded exact remainder: a scalar term, finitely many symmetric compressed prime-power translations, and the continuous completion kernel. On interior core vectors,

\[
T v_K
=1_I\,\mathcal F^{-1}\!\left[m(\xi)\widehat{Ev_K}(\xi)\right],
\qquad
m(\xi)=\log|\xi|+\gamma,
\]

with

\[
\widehat{Ev_K}(\xi)
=\frac1{2i}\bigl(\widehat\chi(\xi-K)-\widehat\chi(\xi+K)\bigr).
\]

Fourier inversion therefore gives

\[
\|Tv_K\|_\infty
\le C\int_{\mathbb R}|m(\xi)|\,|\widehat{Ev_K}(\xi)|\,d\xi.
\]

For one translated packet, after `eta=xi-K`, the relevant integral is

\[
\int_{\mathbb R}
|\log|K+\eta|+\gamma|\,|\widehat\chi(\eta)|\,d\eta.
\]

On `|eta|<=K/2`, the logarithmic factor is `O(log K)`. On `|eta|>K/2`, Schwartz decay of `widehat chi` makes the tail negligible; the possible logarithmic singularity near `eta=-K` is locally integrable and is multiplied there by `O_N(K^{-N})` for every `N`. The packet centered at `-K` is identical. Hence

\[
\boxed{\|Tv_K\|_\infty=O(\log K).}
\]

The exact remainder does not change this scale. Each compressed translation is an `L^infinity` contraction. The scalar term is trivial. For fixed `a`, the completion

\[
R_a u(x)=-a\int_I r''(a(x-y))u(y)\,dy
\]

has a bounded kernel on the compact difference interval `[-2a,2a]` by the regularity already audited in `PL-291` and `PL-301`, so

\[
\|R_a u\|_\infty\le C_a\|u\|_\infty.
\]

Since `\|v_K\|_\infty<=\|\chi\|_\infty`, it follows that for every fixed `a` and fixed spectral parameter `z`,

\[
\boxed{
\|f_K\|_\infty=O(\log K),
\qquad
f_K:=(\widetilde A_a^- -z)v_K.
}
\]

The operator preserves parity, so every `f_K` is odd. Because `I` has finite measure, the same estimate immediately gives

\[
\boxed{
\|f_K\|_{L^p(I)}=O(\log K)
\qquad(1\le p\le\infty).
}
\]

This strengthens the `L^2` graph-cost estimate in `PL-303`; it uses the exact Suzuki remainder rather than an engineered perturbation.

## 2. The output variation still costs order `K`

The variation calculation from `PL-303` is unchanged. Since `v_K` vanishes near the endpoints,

\[
\operatorname{TV}(Ev_K)
=
\int_I
|\chi'(x)\sin(Kx)+K\chi(x)\cos(Kx)|\,dx.
\]

Periodic averaging gives

\[
\int_I|\chi(x)\cos(Kx)|\,dx
\longrightarrow
\frac2\pi\int_I|\chi(x)|\,dx>0,
\]

so for some `c_chi>0`,

\[
\boxed{
\|v_K\|_{BV_0}
\ge
\operatorname{TV}(Ev_K)
\ge c_\chi K-O(1).
}
\]

Thus the exact operator sees the packet at only logarithmic cost in every ordinary `L^p` forcing norm, while `BV` sees its linear spatial frequency.

## 3. No `L^p` forcing norm can close the BV gate

First let `2<=p<=infinity`. On the finite interval, `L^p(I)\subset L^2(I)`, so the Hilbert resolvent is already defined on every odd `L^p` input. If its restriction were bounded into `BV_0`, then for the exact forcings above,

\[
\|v_K\|_{BV_0}
=
\|R^-_{a,z}f_K\|_{BV_0}
\le C_p\|f_K\|_p
=O(\log K),
\]

contradicting `\|v_K\|_{BV_0}\gtrsim K`.

Now let `1<=p<2`. Here the Hilbert resolvent need not be defined on all of `L^p`, so the correct statement is about extension rather than restriction. Every `f_K` belongs to `L^2\cap L^p`. Any bounded extension `\mathcal R_p:L^p_{odd}->BV_0` agreeing with the Hilbert resolvent on this common domain would again satisfy

\[
\|v_K\|_{BV_0}
=
\|\mathcal R_p f_K\|_{BV_0}
\le C_p\|f_K\|_p
=O(\log K),
\]

which is impossible.

Therefore

\[
\boxed{
\text{ordinary }L^p\text{ forcing }\not\Rightarrow BV
\quad\text{for every }1\le p\le\infty.
}
\]

This is not a consequence of the small numerical value of the `a=0.8` gap and does not disappear at another resolvent point. It is the scale mismatch of a zero-order logarithmic principal symbol with first-order variation.

## 4. A general finite-measure-to-BV resolvent extension is impossible

Let `\mathcal M(I)` be the finite complex Radon measures with total-variation norm. Regard `f_K` as the absolutely continuous measure

\[
\mu_K=f_K(x)\,dx.
\]

Then

\[
\|\mu_K\|_{\mathcal M}
=\|f_K\|_1
=O(\log K).
\]

Suppose there were a bounded extension

\[
\mathcal R_{\mathcal M}:\mathcal M_{\rm odd}(I)\to BV_0(I)
\]

that agreed with the Hilbert resolvent on absolutely continuous odd `L^2` data. Since every `f_K` is bounded and hence lies in `L^2`, compatibility would give

\[
\mathcal R_{\mathcal M}\mu_K=v_K.
\]

Boundedness would force

\[
c_\chi K-O(1)
\le\|v_K\|_{BV_0}
\le C\|\mu_K\|_{\mathcal M}
=O(\log K),
\]

again a contradiction. Therefore no such global measure-to-BV resolvent extension exists.

The statement is deliberately about an **unstructured** measure space. It does not exclude a bounded inverse on a narrow source-generated subspace of measures whose Fourier content is constrained, nor a cancellation identity that makes the actual aperture-derivative forcing much smaller than an arbitrary measure of the same total variation.

## 5. Why this is a genuine strengthening of `PL-303`

`PL-303` closed the tempting argument

\[
\text{odd spectral gap}+\text{ordinary }L^2\text{ forcing}
\Longrightarrow
\text{BV control}.
\]

It explicitly left open a stronger Banach or finite-measure coercivity estimate tailored to the differentiated equation. The present result separates the two meanings of that escape.

A **generic** strengthening of the forcing norm from `L^2` to `L^1`, any intermediate `L^p`, `L^infinity`, or the full finite-measure space does not help: the same actual canonical packets have only `O(log K)` cost in all those input norms. Merely changing the ambient forcing space therefore cannot overcome the zero-order symbol.

What remains open is the genuinely narrower alternative already suggested by the accepted zero-order Hadamard clue: the actual differentiated ground-branch forcing may lie in a source-structured range on which the high-frequency packets above are forbidden or cancel. Such a theorem would have to identify and use that range explicitly. Calling the input a measure is not enough.

## 6. Adversarial and novelty audit

The Fourier estimate is elementary zero-order pseudodifferential analysis. No novelty is claimed for the general principle that a logarithmic multiplier cannot control first-order variation on arbitrary oscillatory packets. Chen--Weth's logarithmic-Laplacian theory, stored as source 96, fixes the exact `2 log|xi|` principal symbol; Suzuki's source 56 fixes the bounded prime/completion remainder. Existing logarithmic-Laplacian regularity works in logarithmic or log-Hölder scales and does not supply a generic positive-order smoothing theorem that would conflict with the packet calculation.

The line-local contribution is the exact closure of a live route for Suzuki's **full canonical localized operator**: after `PL-301` showed that its actual remainder is BV-stable and `PL-303` ruled out `L^2` gap smoothing, one might still hope that the differentiated equation can be estimated merely by moving to a stronger-looking `L^p` or finite-measure forcing norm. The `L^infinity` packet estimate proves that this is impossible without additional source restrictions.

The proof does not use analytic continuation, an Euler product, a matched nonarithmetic replacement, or an engineered perturbation. It is a direct estimate on the already-established self-adjoint localized completed-Weil operator.

No new literature entry is required. Sources 56 and 96 are already recorded in `research/prime_lattice/SOURCES.md`, and the dependencies `PL-291`, `PL-301`, and `PL-303` contain the exact operator and remainder facts used above.

## 7. Boundaries and failure modes

**No statement about the actual branch variation.** The finding does not prove that the localized-Weil ground state, its fractional regularizations, or its aperture derivative fail to have bounded variation. It only rules out obtaining that conclusion from an inverse estimate valid on an ambient `L^p` or measure space.

**No source-specific range is ruled out.** A differentiated source may satisfy moment cancellation, boundary compatibility, parity, a commutator identity, or a finite-dimensional relation not shared by the packet forcings `f_K`. A bounded inverse on such a proper range remains possible.

**No contradiction with all-log eigenstate regularity.** `PL-291` concerns actual eigenstates and every fixed logarithmic Fourier moment. The witnesses here are graph-domain packets used to test an ambient inverse estimate; they need not resemble the ground branch.

**No positive-order graph norm has been tested.** If the forcing norm itself contains a multiplier comparable to `|xi|`, or an equivalent variation derivative, the packet cost is no longer `O(log K)`. Such an estimate would be genuinely stronger and cannot be dismissed by this argument, but it must arise from the exact differentiated equation rather than the ordinary resolvent gap.

**No arithmetic sign theorem.** Even perfect derivative-measure control would leave the independent source-specific first-crossing/sign problem from `PL-294`--`PL-295` unresolved.

**No small-order boundary-stress limit.** The accepted Hadamard clue separately asks whether the renormalized fractional boundary trace has an intrinsic `s->0+` limit. The present obstruction concerns the BV/forcing side only.

## Consequence for `prime_lattice`

The regularity fork after `PL-303` is now sharper. There is no ambient forcing space among the standard `L^p` scale or finite measures on which the canonical odd resolvent gains the one full spatial order needed for `BV`. In particular,

\[
\boxed{
\text{change }L^2\text{ to }L^p\text{ or }\mathcal M
\quad\text{does not close the BV gate.}
}
\]

A viable continuation must expose structure that the packet family cannot satisfy: an exact commutator/source range with high-frequency cancellation, a derivative-measure equation whose right-hand side has additional algebraic constraints, an order/variation principle for the actual isolated ground branch, or a forcing graph norm that already charges linear frequency. The distinction is now precise: **unstructured Banach strengthening is closed; source-structured coercivity remains open.**

## Dependencies

- `PL-291`: exact logarithmic principal symbol and structured bounded remainder on the fixed interval.
- `PL-301`: compressed prime shifts are BV-stable and the archimedean completion is regular; in particular the exact remainder is bounded on the relevant standard spaces at fixed aperture.
- `PL-303`: canonical high-frequency odd packet, `O(log K)` `L^2` graph cost, and `Omega(K)` variation obstruction.
- Source 56 in `research/prime_lattice/SOURCES.md`: Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:`2606.09096v2`.
- Source 96 in `research/prime_lattice/SOURCES.md`: Huyuan Chen and Tobias Weth, *The Dirichlet problem for the logarithmic Laplacian*, *Communications in Partial Differential Equations* **44** (2019), 1100–1139.
