# VIS-280 — Wang's `D_x`–`B_x` cross is power-small on a fixed-source packet

## Claim

Keep the short-interval notation and fixed-source packet regime of `VIS-274`–`VIS-279`: `H=T^theta` with fixed `0<theta<1`, `I=(T,T+H]`, `L=log T`,

`A(x,t)=-D_x(t)+B_x(t)+E_x(t)`,

and

`x=e^(2*pi*q)`

with `q` restricted to a fixed compact set. Then the `D_x`–`B_x` cross term contributes only

`O_K(1/(H L))`

to the normalized fixed-`q` packet, hence is smaller than every fixed negative power of `L` when `H=T^theta`.

The input is already present explicitly in Biao Wang's proof of Proposition 2.6. With

`D_x(t)=sum_(n>=2) a_n n^(-it)`, `a_n=(Lambda(n)/sqrt(n)) min(n/x,x/n)`,

and

`B_x(t)=log(t+2)/x`,

Wang obtains by integration by parts

`| integral_I D_x(t) overline(B_x(t)) dt | << (L/x) sum_(n>=2) a_n/log n << L/sqrt(x)`.

For `x` in a fixed compact set this is `O_K(L)`. The fixed-source change of variables contributes `d alpha=(2*pi/L)dq`, and the pair-statistic normalization contributes a factor proportional to `1/(H L)`. Therefore the whole `D_x`–`B_x` packet is

`O_K(L) * O(L^-1) * O((H L)^-1) = O_K(1/(H L))`.

Thus Wang's deterministic `B_x` source does not generate either an intrinsic `L^(-3/2)` term or an intrinsic `L^(-2)` term through its cross interaction with `D_x` on a compact fixed-source packet. Together with `VIS-279`, which moves the `D_x`–`E_x` cross to at most `L^-2`, this removes the entire `D_x`–`(B_x+E_x)` interaction as a compulsory source of the theorem-level `L^-3/2` remainder.

**Evidence/status:** `LITERATURE+DERIVED + EXACT REGIME SPECIALIZATION + NEGATIVE/CONTROL + BOTTLENECK LOCALIZATION + NO-NOVELTY-CLAIM`.

No improvement of Wang's uniform theorem, no asymptotic coefficient for the full fixed-source statistic, no statement for growing `q`, and no RH implication is claimed.

## 1. The source estimate is already sharper than the theorem-level packet scale

Wang's explicit-formula decomposition is

`A(x,t)=-D_x(t)+B_x(t)+E_x(t)`.

In the proof of Proposition 2.6, after evaluating the `D_x` and `B_x` diagonal terms, Wang handles their cross term directly rather than by Cauchy–Schwarz. His equation (2.21) gives

`| integral_I D_x(t) overline(B_x(t)) dt | << (L/x) sum_(n>=2) a_n/log n << L/sqrt(x)`.

The last estimate uses `Lambda(n)/log n <= 1` together with the explicit shape of `a_n`. This is a theorem-level bound valid uniformly over Wang's source range; no new exponential-sum estimate is needed here.

If `q` is restricted to a fixed compact set and `x=e^(2*pi*q)`, then `x` and `1/sqrt(x)` are bounded by constants depending only on that compact set. Hence

`|<D_x,B_x>| = O_K(L)`.

This is much smaller than the `O_K(H)` scale that survives from the compact-source `D_x`–`E_x` Cauchy–Schwarz bound in `VIS-279`.

## 2. Fixed-source normalization makes the `D_x`–`B_x` packet power-small

The fixed-source coordinate used by this branch is

`alpha = 2*pi*q/L`,

so

`d alpha = (2*pi/L)dq`.

The normalized pair statistic has the additional factor proportional to `1/(H L)`. Therefore, after integrating over any fixed compact `q` support,

`D-B packet <<_K L * L^-1 * (H L)^-1 = 1/(H L)`.

Since `H=T^theta` with fixed `theta>0`, one has

`1/(H L) = o(L^-m)`

for every fixed `m>0`. In particular this sector is negligible relative to both `L^-3/2` and `L^-2` logarithmic scales.

This conclusion does not depend on extracting cancellation from the sign of the cross term. The signed contribution in the expansion of `|A|^2` is

`-2 Re integral_I D_x(t) overline(B_x(t)) dt`,

but Wang's absolute bound alone is already sufficient to make the packet power-small.

## 3. Consequence for the fixed-source `L^-3/2` search

`VIS-278` showed that the standalone gamma-normalized source energy `|B_x+E_x|^2` has its first unresolved scale at `L^-2`, not `L^-3/2`. `VIS-279` then restored Wang's exact compact-source mean square for `D_x` and showed that the `D_x`–`E_x` cross is at most `L^-2`; the apparent `L^-3/2` size there came from replacing the exact fixed-`x` identity by a coarser bound uniform for growing `x`.

The present finding handles the other part of the prime/source interaction. The `D_x`–`B_x` cross is not merely below `L^-3/2`; it is power-small in `T` after fixed-source packet normalization. Consequently the full cross

`D_x` against `B_x+E_x`

cannot force a fixed-source `L^-3/2` term: its `D-B` part is power-small and its `D-E` part is at most `L^-2`.

This does not prove that the complete fixed-source statistic has no `L^-3/2` contribution. It localizes the remaining search away from the direct `D_x`–source cross. Other theorem-level losses, localization steps, boundary replacements, or sectors not yet sharpened may still carry an `L^-3/2` envelope.

That next audit is a separate research thread and is intentionally not opened here.

## 4. Prior art and novelty boundary

The primary source is Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918 (2026), equations (2.7)–(2.9), Proposition 2.6, and especially equation (2.21). Wang already proves the `D_x`–`B_x` estimate used above. The only Mathia-specific step is to transport that published bound through the narrower fixed-source coordinate and normalization used in `VIS-274`–`VIS-279`.

Accordingly, no novelty is claimed for the cross-term estimate itself. The durable value is negative/control information for the current visual branch: a theorem-level term that could look like part of the fixed-source remainder is shown, under the exact representation being studied, to vanish far below the logarithmic frontier.

## Dependencies

- `VIS-274`: fixed-source Wang scaling and packet normalization.
- `VIS-278`: gamma-normalized standalone source energy reaches only the `L^-2` scale.
- `VIS-279`: the compact-source `D_x`–`E_x` cross reaches at most `L^-2`, removing its apparent theorem-level `L^-3/2` floor.

## Research consequence

The entire direct prime/source cross is now excluded as a compulsory fixed-source `L^-3/2` mechanism: `D_x`–`B_x` is power-small and `D_x`–`E_x` is at most `L^-2`. The next visual invocation should inspect a different proof-loss or localization boundary rather than further refine this cross sector.
