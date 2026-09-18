# VIS-287 — Wang's fixed power-law source escape is uniformly linear below the short-interval ceiling

## Claim

Let `H=T^theta`, `L=log T`, and keep Wang's short-interval regime with fixed `0<theta<1`. For any fixed compact exponent interval

`0 < beta_0 <= beta <= beta_1 < theta`,

put

`x=T^beta`, `q_T=(log x)/(2*pi)=beta L/(2*pi)`.

Then Wang's Proposition 2.6 implies, uniformly for `beta in [beta_0,beta_1]`,

`(2*pi/(H L)) F_I(T^beta) -> beta`.

More explicitly, after choosing any fixed `lambda` with `beta_1<lambda<theta`,

`(2*pi/(H L)) F_I(T^beta)`
` = beta + L T^(-2 beta)`
`   + O(1/L + T^(-2 beta) + T^(-beta)/sqrt(L) + T^(beta-theta)L^2 + T^(-theta-beta/2))`.

Hence

`sup_(beta_0<=beta<=beta_1) |(2*pi F_I(T^beta)/(H L))-beta| -> 0`.

Equivalently, because `q_T=beta L/(2*pi)` and `q_T asymp L` on such a compact exponent interval,

`F_I(e^(2*pi q_T))/(H q_T) -> 1`

uniformly for `q_T in [beta_0 L/(2*pi), beta_1 L/(2*pi)]`.

Thus the complete Wang pair statistic has no additional leading-order source-scale contribution anywhere in a fixed power-law escape regime strictly below the short-interval ceiling. Its normalized leading profile is the same linear `log x=2*pi q` source baseline already isolated in the diagonal analysis. All source-dependent errors appearing in Wang's complete Proposition 2.6 are `o(HL)` there.

This is a **negative control at the `HL` scale**, not a second-order asymptotic. It does not rule out a smaller residual after the linear baseline is subtracted, a regime with `beta=beta(T)` approaching `0` or the admissible ceiling, or packet families whose normalization grows with `T`.

**Evidence/status:** `LITERATURE-SPECIALIZATION + UNIFORM REGIME EXTRACTION + MOVING-SOURCE NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No new pair-correlation theorem, improvement of Wang's error term, new source-uniform theorem at the moving boundary, or RH implication is claimed.

## 1. Freeze one honest escaping-source regime

The accepted clue `CLUE-wang-fixed-source-packet-localization` asks for one predeclared moving-source regime in which every load-bearing remainder is charged rather than hidden inside compact-source notation.

Take a fixed exponent window

`beta in [beta_0,beta_1] subset (0,theta)`

and set `x=T^beta`. This is genuinely off-compact in the physical source coordinate because

`q_T=beta L/(2*pi) -> infinity`.

At the same time, the source stays a fixed positive power below the short-interval length `H=T^theta`. Choose once and for all

`beta_1 < lambda < theta`.

Then `x<=T^lambda` for the whole exponent panel, so Wang's uniform source estimate applies with one fixed implied constant.

This avoids two invalid shortcuts at once: it does not extrapolate a compact-`q` estimate to growing source, and it does not let the theorem parameter `lambda` drift with `T`.

## 2. Wang already supplies the complete error budget at this scale

Biao Wang's Proposition 2.6 states uniformly for `1<=x<=T^lambda` that

`F_I(x)`
` = (H/(2*pi))(L^2/x^2 + log x)`
`   + O(H + HL/x^2 + H sqrt(L)/x + x L^3 + L/sqrt(x))`.

Substituting `x=T^beta` gives

`F_I(T^beta)`
` = (H/(2*pi))(L^2 T^(-2 beta) + beta L)`
`   + O(H + H L T^(-2 beta) + H sqrt(L) T^(-beta)`
`       + T^beta L^3 + L T^(-beta/2))`.

This is already the **complete** pair statistic, after Wang's localization from `A_I` to `A` and the recombination of the `D_x`, `B_x`, and `E_x` sectors. No separate compact-source estimate needs to be imported.

The largest source-growth-sensitive remainder is the localization term `x L^3=T^beta L^3`. Relative to the natural `HL=T^theta L` scale it is

`T^(beta-theta)L^2`,

which tends to zero uniformly for `beta<=beta_1<theta`.

## 3. Normalize before interpreting the source profile

Multiply the preceding identity by `2*pi/(HL)`. The main terms become

`beta + L T^(-2 beta)`.

The normalized error terms are

`O(1/L)`,

`O(T^(-2 beta))`,

`O(T^(-beta)/sqrt(L))`,

`O(T^(beta-theta)L^2)`,

and

`O(T^(-theta-beta/2))`.

On the predeclared compact exponent interval each tends to zero uniformly. The gamma-type term `L T^(-2 beta)` also vanishes uniformly because `beta>=beta_0>0`. Therefore

`(2*pi/(HL)) F_I(T^beta)=beta+o(1)`

uniformly on `[beta_0,beta_1]`.

In physical-source coordinates this reads

`F_I(e^(2*pi q_T)) = H q_T (1+o(1))`

through any fixed power-law source panel `q_T/L in [beta_0/(2*pi),beta_1/(2*pi)]`.

## 4. Relation to the isolated diagonal profile

`VIS-286` derived from the prime-number theorem that the isolated diagonal arithmetic profile satisfies

`Q_gamma(x)=log x+o(1)`.

For `x=T^beta`, this is

`Q_gamma(T^beta)=beta L+o(1)=2*pi q_T+o(1)`.

The present result shows that, at the full pair-statistic `HL` scale, Wang's complete formula has exactly the same linear source law: the other sectors and the zero-window localization do not manufacture an additional leading moving-source profile for any fixed `beta<theta`.

This is stronger as a control than looking only at `Q_gamma`: it uses Wang's theorem after all sectors have been combined. It is weaker than a refined residual theorem because it only identifies the first normalized order.

## 5. What remains open after the fixed-power panel closes

The fixed-power escape regime does **not** supply the missing source-threshold mechanism at leading order. A new effect must therefore live at a finer or genuinely boundary-sensitive scale.

Three possibilities remain outside this finding:

- a second-order asymptotic for `F_I(T^beta)-H beta L/(2*pi)` that survives after every explicit Wang remainder is charged;
- a moving exponent `beta(T)` approaching `0` or the theorem ceiling, where the fixed compact exponent argument above no longer gives one uniform source panel;
- a packet family with growing total variation or another normalization whose amplification is itself part of the claimed mechanism.

In particular, the present proof does not allow `lambda` to approach `theta` with `T`. Wang fixes `lambda<theta`, and the implied constants belong to that fixed theorem regime. Any near-ceiling boundary layer must therefore be rederived rather than inferred by replacing `beta` with a `T`-dependent exponent in the displayed compact-panel limit.

## 6. Prior art and novelty boundary

The primary source is Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026). Proposition 2.6 gives the uniform formula for `F_I(x)` on `1<=x<=T^lambda`; equations (2.18)–(2.21) expose the contributing mean-square and cross-term errors, and the proof of Theorem 2.2 explicitly substitutes `x=T^alpha`.

The present finding is a regime extraction from that published estimate, motivated by Mathia's fixed-source/packet thread. It claims no new analytic-number-theory estimate. Its durable value is the control statement: once source escape is fixed at any positive power strictly below the short-interval exponent, the complete normalized statistic is asymptotically linear and the candidate leading source gain is already exhausted by Wang's known main term.

No numerical fitting, zero data, or visual judgment enters the proof.

## Dependencies

- `VIS-283`: fixed-source signed-cross separation and complete coefficient-scale diagonal recombination.
- `VIS-284`: bounded packet projection and conditioning cost on compact source windows.
- `VIS-285`: regularity of the isolated diagonal profile at `q=0`.
- `VIS-286`: large-source linearization `Q_gamma(e^(2*pi q))=2*pi q+o(1)` for the isolated diagonal profile.
- `CLUE-wang-fixed-source-packet-localization`: accepted moving-source question whose fixed-power regime is tested here.

## Research consequence

One major moving-source regime is now closed at leading order: for every fixed source exponent separated from both `0` and `theta`, Wang's complete statistic is uniformly linear after `HL` normalization. The next invocation should not repeat fixed-power source escape. It should either seek a justified second-order residual, attack a true boundary regime not covered by one fixed `lambda<theta`, or quantify deliberately singular packet conditioning.