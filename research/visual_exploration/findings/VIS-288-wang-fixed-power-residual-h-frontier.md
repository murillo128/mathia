# VIS-288 — Wang's fixed-power residual frontier is the `H` scale

## Claim

Let `H=T^theta`, `L=log T`, with fixed `0<theta<1`. Fix a compact source-exponent panel

`0 < beta_0 <= beta <= beta_1 < theta`,

and put `x=T^beta`. Define the complete-statistic residual after Wang's two explicit main terms by

`R_beta(T)=F_I(T^beta)-(H/(2*pi))(L^2 T^(-2 beta)+beta L)`.

Then Biao Wang's Proposition 2.6 implies, uniformly for `beta in [beta_0,beta_1]`,

`R_beta(T)=O(H)`.

In fact every source-dependent error term displayed in Proposition 2.6 is `o(H)` on this panel; the only unresolved contribution at this level is the theorem's bare `O(H)` remainder. Since also

`H L^2 T^(-2 beta)=o(H)`

uniformly on the panel, the same frontier holds after subtracting only the linear source baseline:

`F_I(T^beta)-(H beta L)/(2*pi)=O(H)`.

Consequently, for every positive function `a(T)->infinity`,

`sup_(beta_0<=beta<=beta_1) |F_I(T^beta)-(H beta L)/(2*pi)| / (H a(T)) -> 0`.

Thus **no fixed-power source residual can live on a scale strictly larger than `H` and smaller than the leading `HL` scale while remaining compatible with Wang's stated estimate**. Any unresolved fixed-power effect is confined to the `H` scale or below. To identify an `H`-scale profile one needs a refinement of the `O(H)` term; Proposition 2.6 alone cannot distinguish such a profile from its own remainder.

**Evidence/status:** `LITERATURE-SPECIALIZATION + UNIFORM REMAINDER EXTRACTION + NEGATIVE SCALE CONTROL + NO-NOVELTY-CLAIM`.

No new pair-correlation estimate, `o(H)` remainder, `H`-scale asymptotic, moving-boundary theorem, or RH implication is claimed.

## 1. Start from the complete Wang estimate

For fixed `0<lambda<theta`, Wang's Proposition 2.6 states uniformly for `1<=x<=T^lambda` that

`F_I(x)`
` = (H/(2*pi))(L^2/x^2 + log x)`
`   + O(H + HL/x^2 + H sqrt(L)/x + x L^3 + L/sqrt(x))`.

Choose once and for all `lambda` with

`beta_1 < lambda < theta`.

Then the complete exponent panel `x=T^beta`, `beta in [beta_0,beta_1]`, lies in the same fixed theorem range, so the implied constant is uniform across the panel. Substitution gives

`R_beta(T)`
` = O(H + H L T^(-2 beta) + H sqrt(L) T^(-beta)`
`       + T^beta L^3 + L T^(-beta/2))`.

This is the complete pair statistic, not an isolated diagonal model. The remainder already includes the localization and the `D_x`, `B_x`, `E_x` recombination controlled in Wang's proof.

## 2. Every explicit source-dependent remainder is below `H`

Divide each displayed source-dependent error by `H=T^theta`. Uniformly for `beta in [beta_0,beta_1]`,

`(H L T^(-2 beta))/H <= L T^(-2 beta_0) -> 0`,

`(H sqrt(L) T^(-beta))/H <= sqrt(L) T^(-beta_0) -> 0`,

`(T^beta L^3)/H <= T^(beta_1-theta) L^3 -> 0`,

and

`(L T^(-beta/2))/H <= L T^(-theta-beta_0/2) -> 0`.

Therefore

`sup_(beta_0<=beta<=beta_1) |R_beta(T)| = O(H)`.

The fixed-power source coordinate has now been pushed one full logarithmic order below the leading `HL` profile without introducing any new estimate. The obstruction is no longer one of the explicit source-dependent terms: it is the source-unresolved `O(H)` remainder already present in Proposition 2.6.

## 3. The explicit `L^2/x^2` main term is also below the frontier

`VIS-287` kept both of Wang's displayed main terms because it was proving the normalized `HL` asymptotic. For the present residual-scale question, the first main term is smaller still. Uniformly for `beta>=beta_0>0`,

`(H/(2*pi)) L^2 T^(-2 beta) = o(H)`.

Hence

`F_I(T^beta) = (H beta L)/(2*pi) + O(H)`

uniformly on every fixed compact exponent panel inside `(0,theta)`.

This matters for the packet-localization clue: after the universal linear source law is subtracted, there is no remaining fixed-power signal at any scale `H a(T)` with `a(T)->infinity`. In particular, every intermediate scale satisfying

`H << H a(T) << H L`

is excluded by the existing theorem.

## 4. What the `O(H)` frontier does and does not say

The estimate does **not** imply

`R_beta(T)/H -> 0`,

nor does it identify a limiting function of `beta`. A bounded nontrivial `H`-scale profile, oscillation, or source-dependent term could still be hidden inside Wang's `O(H)` remainder. Likewise, an effect below `H` is not constrained by this argument.

The correct fixed-power frontier is therefore sharp only relative to the available theorem:

- leading source profile: `(H beta L)/(2*pi)`;
- every explicit source-dependent correction in Proposition 2.6: `o(H)` on compact exponent panels;
- unresolved theorem floor: `O(H)`.

A claimed fixed-power residual larger than `H` is already ruled out. A claimed `H`-scale residual requires a genuine refinement of the load-bearing `O(H)` estimate rather than a new normalization, visualization, or packet reweighting.

## 5. Prior art and novelty boundary

The source is Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026), Proposition 2.6. That proposition gives exactly the uniform formula used above for `1<=x<=T^lambda`, with fixed `lambda<theta`.

The present statement is a direct scale extraction from Wang's published error budget. It is not claimed as a new analytic-number-theory theorem. Its durable value inside Mathia is negative and organizational: it identifies `H`, not some intermediate `H log^c T` scale, as the first unresolved fixed-power residual frontier after the linear source term has been removed.

## Dependencies

- `VIS-283`: fixed-source signed-cross separation and coefficient-scale diagonal recombination.
- `VIS-284`: compact-source packet projection and inverse-width conditioning cost.
- `VIS-285`: regularity of the isolated profile at the left source endpoint.
- `VIS-286`: large-source linearization of the isolated diagonal profile.
- `VIS-287`: complete-statistic fixed-power linearization at the `HL` scale.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose second-order fixed-power branch is narrowed here.

## Research consequence

The fixed-power branch no longer has an unidentified mesoscopic residual scale. After subtracting the linear source law, Wang's existing theorem confines every remaining effect to `O(H)`. Further work on this branch is justified only by an attempt to sharpen the bare `O(H)` term itself. Otherwise the useful unexplored territory is a genuine moving boundary — for example `beta(T)->0` or approach to the source ceiling — where the fixed compact exponent panel no longer supplies one uniform theorem regime.