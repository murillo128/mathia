# NB-168 — Block-stationary templates make logarithmic Euler rescue sparse

**Date:** 2026-09-16  
**Status:** `DERIVED + SOURCE-SPECIFIC + MEAN-SQUARE + CAPPED-TRANSPORT + HEIGHT-STATIONARY + NB-167-REFINEMENT`.

`NB-167` leaves one compact-support escape that generic bounded-Lipschitz geometry cannot rule out: the actual values of `zeta'/zeta` might line up arithmetically with a signed sampler and create a conservation defect much larger than the generic capped-transport scale. The pointwise bound does not distinguish a persistent mechanism from a rare phase resonance.

For a sampler obtained by translating one fixed offset template through a dyadic height block, that distinction can be made. Montgomery--Vaughan mean-value theory shows that a source defect of the `q log T` size needed to cancel a logarithmic target packet occupies only a quantitatively small set of heights unless the capped transport itself is almost logarithmic. Thus a fixed local shape cannot use the arithmetic phases as a persistent rescue mechanism; any remaining rescue must be height-adaptive, confined to a sparse sequence of centers, or live in an ultra-thin exterior layer where the elementary mean-square error is no longer negligible.

## Claim

Fix `B>0`. Let `T -> infinity`, let `0<a_T<=1`, and let `nu_T` be a finite real signed Borel measure supported on `[-B,B]` with zero total mass. Write

\[
\nu_T=\nu_T^+-\nu_T^-,
\qquad
\nu_T^+(\mathbf R)=\nu_T^-(\mathbf R).
\]

The template may depend on `T`, but it is fixed as the center `t` varies across `[T,2T]`. Define its capped Jordan transport at the exterior Poisson width `a_T` by

\[
\mathsf T_T
:=
\inf_{\pi\in\Pi(\nu_T^+,\nu_T^-)}
\iint
\min\left\{1,\frac{|u-v|}{a_T}\right\}
\,d\pi(u,v).
\]

For a positive reference charge `q_T`, put

\[
\Xi_T:=\frac{\mathsf T_T}{q_T}.
\]

Translate the template to height `t` and define its arithmetic source defect

\[
\mathcal E_T(t)
:=
\int
\frac{\zeta'}{\zeta}(1+a_T+i(t+u))
\,d\nu_T(u).
\]

Then uniformly in the template,

\[
\boxed{
\int_T^{2T}|\mathcal E_T(t)|^2\,dt
\ll_B
\mathsf T_T^2\left(T+a_T^{-2}\right).
}
\]

Consequently, for every fixed `eta>0`,

\[
\boxed{
\frac1T
\left|
\left\{t\in[T,2T]:
|\mathcal E_T(t)|\ge \eta q_T\log T
\right\}
\right|
\ll_B
\frac{\Xi_T^2}{\eta^2(\log T)^2}
\left(1+\frac1{Ta_T^2}\right).
}
\]

In particular,

\[
\boxed{
\Xi_T
\sqrt{1+\frac1{Ta_T^2}}
=o(\log T)
}
\]

forces `q_T log T`-scale arithmetic rescue onto a set of relative Lebesgue measure `o(1)`. In the natural regime `Ta_T^2 -> infinity`, this reduces simply to

\[
\boxed{\Xi_T=o(\log T).}
\]

This is much weaker than the pointwise conservation condition of `NB-167` in the high-ordinate boundary layer. There `NB-167` needs roughly `Xi_T=o(log log T)` to make its worst-case bounded-Lipschitz remainder negligible; a block-stationary template can have `Xi_T` almost as large as `log T` and still fail to generate a logarithmic arithmetic remainder at almost every height.

## Derivation

### Capped transport controls every prime phase coefficient

For

\[
\widehat\nu_T(\xi)
:=
\int e^{-iu\xi}\,d\nu_T(u),
\]

let `pi` be any coupling of the two Jordan parts. Since the marginals of `pi` are `nu_T^+` and `nu_T^-`,

\[
\widehat\nu_T(\xi)
=
\iint
\left(e^{-iu\xi}-e^{-iv\xi}\right)
\,d\pi(u,v).
\]

For `d=|u-v|`,

\[
|e^{-iu\xi}-e^{-iv\xi}|
\le \min\{2,|\xi|d\}.
\]

If `d>=a_T`, the right side is at most `2`; if `d<a_T`, it is at most `|xi|d`. Hence in both cases

\[
\min\{2,|\xi|d\}
\le
2(1+a_T|\xi|)
\min\left\{1,\frac d{a_T}\right\}.
\]

Minimizing over couplings gives the Fourier estimate

\[
\boxed{
|\widehat\nu_T(\xi)|
\le
2\mathsf T_T(1+a_T|\xi|).
}
\]

This is the key improvement over using total variation. Prime phases whose positive and negative masses nearly coincide are charged only by their unresolved transport at one Poisson width.

### The Euler series turns the translated sampler into one Dirichlet series

Because `1+a_T>1`, the logarithmic derivative has the absolutely convergent expansion

\[
\frac{\zeta'}{\zeta}(1+a_T+it)
=
-\sum_{n\ge2}
\frac{\Lambda(n)}{n^{1+a_T+it}}.
\]

Therefore

\[
\mathcal E_T(t)
=
-\sum_{n\ge2}b_{n,T}n^{-it},
\qquad
b_{n,T}
:=
\frac{\Lambda(n)}{n^{1+a_T}}
\widehat\nu_T(\log n).
\]

The already anchored Montgomery--Vaughan Hilbert inequality gives its standard Dirichlet-polynomial mean-value consequence

\[
\int_T^{2T}
\left|\sum_{n\le N}b_{n,T}n^{-it}\right|^2dt
\ll
T\sum_{n\le N}|b_{n,T}|^2
+
\sum_{n\le N}n|b_{n,T}|^2.
\]

The capped Fourier estimate implies

\[
\sum_{n\ge2}|b_{n,T}|^2
\ll
\mathsf T_T^2
\sum_{n\ge2}
\frac{\Lambda(n)^2}{n^{2+2a_T}}
(1+a_T\log n)^2
\ll
\mathsf T_T^2,
\]

uniformly for `0<a_T<=1`.

For the weighted error, use `Lambda(n)^2<=Lambda(n) log n` and expand the square:

\[
\sum_{n\ge2}n|b_{n,T}|^2
\ll
\mathsf T_T^2
\sum_{n\ge2}
\frac{\Lambda(n)\log n}{n^{1+2a_T}}
(1+a_T\log n)^2.
\]

The three resulting sums are derivatives of `-zeta'/zeta` at `1+2a_T`. Its simple pole at `1` gives, for `m=1,2,3`,

\[
\sum_{n\ge2}
\frac{\Lambda(n)(\log n)^m}{n^{1+2a_T}}
\ll_m a_T^{-(m+1)}.
\]

After the coefficients `1`, `a_T`, and `a_T^2` from the expanded square are inserted, all three contributions are `O(a_T^{-2})`. Thus

\[
\sum_{n\ge2}n|b_{n,T}|^2
\ll
\mathsf T_T^2a_T^{-2}.
\]

Letting `N -> infinity` by the resulting `L^2` control proves

\[
\int_T^{2T}|\mathcal E_T(t)|^2dt
\ll
\mathsf T_T^2(T+a_T^{-2}).
\]

Chebyshev's inequality then gives the exceptional-height estimate in the claim.

## Relation to `NB-167` conservation

For the translated template, define

\[
Q_{T,t}(\rho)
:=
\Re\int
\frac{d\nu_T(u)}{1+a_T+i(t+u)-\rho}.
\]

The completed explicit-formula bookkeeping used in `NB-165`--`NB-167` expresses the zero-side conservation defect through `Re E_T(t)` plus Gamma, pole, and reference terms. Zero total mass removes the constant pieces. On `t in [T,2T]` the remaining elementary factors have derivative `O_B(1/T)` across the fixed offset interval.

Moreover, because `|u-v|<=2B` and `a_T<=1`, every Jordan coupling satisfies

\[
|u-v|
\ll_B
\min\left\{1,\frac{|u-v|}{a_T}\right\}.
\]

Hence those elementary completed terms are `O_B(mathsf T_T/T)`, negligible compared with `q_T log T` whenever `Xi_T=o(T log T)`. Thus the same mean-square estimate applies, at the scale relevant here, to the completed conservation remainder rather than merely to the bare Euler term.

Suppose an architecture translates this same offset template through the block and, at some center `t`, produces a target packet of at least `kappa log T` zeros, each carrying charge at least `q_T`. To defeat the logarithmic adverse-debt conclusion by the **arithmetic-source escape left open in `NB-167`**, it must create a completed remainder of order `q_T log T`, hence an Euler defect of that order up to the negligible elementary terms. The claim shows that, under

\[
\Xi_T
\sqrt{1+(Ta_T^2)^{-1}}
=o(\log T),
\]

such centers occupy relative measure `o(1)` in every dyadic block.

This does **not** say that a sparse sequence of specially selected target heights cannot all lie in the exceptional set. It says that arithmetic phase alignment cannot be a persistent mechanism for one translated compact shape.

## Adversarial checks and exact boundary

The result deliberately does not freeze the template across different dyadic blocks: `nu_T` may depend arbitrarily on `T`. What is forbidden is adapting the coefficients or offsets to the center `t` *inside the same block*. A family `nu_{T,t}` chosen after observing the local values of `zeta'/zeta` is outside the theorem; that is now the cleanest compact source-specific escape.

The factor `1+(Ta_T^2)^{-1}` is also real, not bookkeeping noise. It comes from the weighted off-diagonal term in the Montgomery--Vaughan theorem. If `a_T` is at or below the ultra-thin scale `T^{-1/2}`, this argument alone no longer proves density-zero rescue for `Xi_T=o(log T)`. At the Vinogradov--Korobov/logarithmic boundary scales relevant to `NB-165`--`NB-167`, however, `Ta_T^2 -> infinity` by an enormous margin.

Finally, the conclusion is a Lebesgue-density statement in height. Without an independent robustness interval around each target packet, it cannot be converted into a theorem excluding a discrete exceptional sequence of target centers. Any later use against a sparse zero-selected architecture must supply that extra bridge rather than silently replacing density by pointwise control.

## Representation audit

The mean-value step is not special to zeta. Any Dirichlet series whose translated-template coefficients satisfy analogous unweighted and `n`-weighted `ell^2` estimates obeys the same stationary-template suppression. The zeta-specific content is the von Mangoldt coefficient structure, which makes the two coefficient budgets respectively `O(1)` and `O(a_T^{-2})`, and the explicit-formula transfer identifying a `q_T log T` Euler defect as the arithmetic currency capable of offsetting a logarithmic zero packet.

Thus this finding does not claim a new Montgomery--Vaughan theorem or a new generic mean-square principle. Its line-local contribution is the capped-transport Fourier reduction and the resulting separation between persistent compact sampling and height-adaptive arithmetic resonance in the `NB-167` transfer framework.

## Prior-art audit

The load-bearing external input is the Montgomery--Vaughan generalized Hilbert inequality and its standard mean-value corollary for Dirichlet polynomials. That source is already anchored in `research/nyman_beurling/SOURCES.md` as H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*, J. London Math. Soc. (2) 8 (1974), 73--82, DOI `10.1112/jlms/s2-8.1.73`; no new source anchor is required.

There is extensive literature on moments of `zeta'/zeta`, including work near the critical line. The present statement stays entirely in `Re s>1` and does not claim novelty for mean values of the logarithmic derivative themselves. What is new to this line is the use of one-Poisson-width capped Jordan transport to bound the translated Dirichlet coefficients and then to show that the particular `q_T log T` source rescue left open by `NB-167` is non-persistent for a block-stationary compact template.

## Research consequence

The compact frontier is narrower after this step. Generic pointwise geometry leaves open the possibility that the real arithmetic source happens to cancel the target debt. For a fixed translated shape, that possibility is now confined to a vanishing fraction of heights throughout the broad regime `Xi_T=o(log T)` and `Ta_T^2 -> infinity`.

The surviving routes are therefore sharply separated: a sampler may adapt its signed shape to height and exploit the actual prime phases; it may target a genuinely sparse exceptional sequence of centers; it may raise capped transport to logarithmic scale; or it may enter the ultra-thin layer `a_T \lesssim T^{-1/2}` where the present mean-square estimate loses force. The first two are genuinely arithmetic/selective mechanisms rather than consequences of generic Poisson geometry.