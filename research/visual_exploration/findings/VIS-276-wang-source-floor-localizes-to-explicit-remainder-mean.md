# VIS-276 — the fixed-source `1/log T` floor localizes to the mean explicit-formula remainder

## Claim

Keep the fixed-source setting of `VIS-274`–`VIS-275`. Let

`L=log T`, `H=T^theta`, `0<lambda<theta<1`,

and use Wang's explicit-formula decomposition

`A(x,t)=-D_x(t)+B_x(t)+E_x(t)`,

with

`B_x(t)=log(t+2)/x`, `E_x(t)=O(1/x)`

uniformly for `t in I=(T,T+H]` and `1<=x<=T^lambda`.

The `O(HL/x^2)` term in Wang's Proposition 2.6, which becomes the unique certified `O(1/L)` floor in the fixed-source rescaling of `VIS-275`, is not an indivisible source error. At the fixed-source scale it separates into:

1. the variation error in `integral_I |B_x(t)|^2 dt`, which can be sharpened using `H=o(T)` to

`O(L H^2/(T x^2) + H^3/(T^2 x^2)) = o(HL/x^2)`;

2. the `B_x,E_x` cross term, whose leading unresolved part is

`(2L/x) Re integral_I overline(E_x(t)) dt`.

More precisely,

`integral_I |B_x(t)|^2 dt`
` = H L^2/x^2`
`   + O(L H^2/(T x^2) + H^3/(T^2 x^2))`,

and

`2 Re integral_I B_x(t) overline(E_x(t)) dt`
` = (2L/x) Re integral_I overline(E_x(t)) dt`
`   + O(H^2/(T x^2)).`

Thus the present fixed-source `1/L` obstruction localizes to one signed quantity:

`M_T(x) := (x/H) Re integral_I E_x(t) dt.`

The pointwise bound `E_x(t)=O(1/x)` gives only `M_T(x)=O(1)`, which reproduces the `O(1/L)` certificate. If instead one can prove

`M_T(e^(2*pi*q)) = o(1)`

uniformly for `q` in each fixed compact subset of `(0,infinity)`, then the `B,E` contribution becomes `o(1/L)` for every fixed smooth source packet. No additional signed moment conditions on the packet are required to cross the present floor.

If the stronger bound `M_T(e^(2*pi*q))=O(L^(-1/2))` holds uniformly on the packet support, the remaining source terms already present in `VIS-275` are at most `O(L^(-3/2))` after fixed-source normalization, apart from smaller powers and `H/T` corrections.

**Evidence/status:** `LITERATURE+DERIVED + EXACT SOURCE-TERM REFINEMENT + BOTTLENECK LOCALIZATION + NO-NOVELTY-CLAIM`.

No estimate for `M_T`, secondary pair-correlation coefficient, prime-power transfer theorem, or RH implication is claimed.

## 1. The `B_x^2` remainder is much smaller on a power-short interval

Wang writes

`B_x(t)=log(t+2)/x`.

His proof of Proposition 2.6 records

`integral_I |B_x(t)|^2 dt = H L^2/x^2 + O(HL/x^2)`

from the coarse observation `log(t+2)=L+O(1)` on `I`.

For `t=T+u`, `0<u<=H`, the short-interval geometry gives more. Since `H=T^theta=o(T)`,

`log(t+2)-L = log(1+(u+2)/T) = O((u+2)/T)`

uniformly on `I`. Hence

`log(t+2)^2-L^2`
` = O(L(u+2)/T + (u+2)^2/T^2)`.

Integrating from `u=0` to `H` yields

`integral_I [log(t+2)^2-L^2] dt`
` = O(L H^2/T + H^3/T^2)`,

with lower-order `H/T` terms absorbed because `H>=1`. Dividing by `x^2` proves

`integral_I |B_x(t)|^2 dt`
` = H L^2/x^2`
`   + O(L H^2/(T x^2) + H^3/(T^2 x^2)).`

Since `H/T=T^(theta-1)->0`, this is `o(HL/x^2)`. The deterministic variation of `B_x` therefore does not create the fixed-source `1/L` boundary.

## 2. The surviving term is the signed mean of `E_x`

The expansion of `|A|^2` contains the cross term

`2 Re integral_I B_x(t) overline(E_x(t)) dt.`

On the same interval,

`B_x(t)=L/x + O(H/(T x))`.

Using Wang's uniform `E_x(t)=O(1/x)` gives

`2 Re integral_I B_x(t) overline(E_x(t)) dt`
` = (2L/x) Re integral_I overline(E_x(t)) dt`
`   + O(H^2/(T x^2)).`

Define

`M_T(x)=(x/H) Re integral_I E_x(t) dt.`

Then the leading cross term is exactly

`2 H L M_T(x)/x^2`

up to the `H/T` correction above. The current pointwise estimate supplies only `M_T(x)=O(1)`. This recovers the same `HL/x^2` scale as Wang's aggregate Proposition 2.6 error, but now identifies the single signed average responsible for that scale after the `B_x^2` refinement.

This distinction matters because `M_T` is not an absolute norm. Unlike the weighted `L^1` majorant in `VIS-275`, it can in principle exhibit cancellation in `t` before any source packet is applied.

## 3. Fixed-source rescaling turns `M_T` into the unique `1/L` channel

Let `h in C_c^infinity((0,infinity))` be fixed and set

`g_T(alpha)=h(L|alpha|/(2*pi))`,

as in `VIS-274`. On the positive half-line put

`q=L alpha/(2*pi)`, `x=T^alpha=e^(2*pi*q)`.

The normalization is

`(2*pi/(H L)) W_I(g_T)`.

The refined `B_x^2` variation contributes only

`O_h(H/(T L))`,

up to still smaller `H^2/T^2` terms. The error from replacing `B_x(t)` by `L/x` inside the `B,E` cross term is smaller again, of order `O_h(H/(T L^2))` after normalization.

By contrast, the leading `B,E` term contributes at scale

`(1/L) integral h(q) e^(-4*pi*q) M_T(e^(2*pi*q)) dq`,

up to a harmless fixed numerical factor determined by the normalization convention. Wang's bound `M_T=O(1)` is therefore precisely the surviving `O(1/L)` channel.

All other source errors listed in `VIS-275` are already below this scale for fixed `q` support:

- the `H sqrt(L)/x` term gives `O(L^(-3/2))`;
- the bare `H` term gives `O(L^(-2))`;
- the `xL^3` term gives `O(L/H)`;
- the `L/sqrt(x)` term gives `O(1/(HL))`.

Consequently, `M_T=o(1)` on compact fixed-source windows is enough to make the current `1/L` barrier disappear. To reach the next already-exposed scale `O(L^(-3/2))`, it is sufficient at this stage to obtain `M_T=O(L^(-1/2))` there.

## 4. This changes the next theorem question

`VIS-275` correctly showed that packet-side Laplace moment cancellation cannot improve an absolute source majorant. The present refinement shows where a source-side improvement must enter.

The next question is not the broad request to sharpen every term in Proposition 2.6. It is the narrower signed-average problem:

> Can the explicit-formula remainder `E_x(t)` be represented or estimated strongly enough to prove cancellation in `integral_T^(T+H) E_x(t) dt` for fixed `x=e^(2*pi*q)` (or uniformly for `q` in a compact source window)?

A direct bound `o(H/x)` already beats the fixed-source `1/L` floor. An asymptotic expansion for this mean would be stronger: it would expose the actual first correction kernel against which Laplace-null packets should be tested.

This also rules out a less useful direction. Further sharpening the elementary variation of `log(t+2)` cannot solve the current boundary; that component is already power-smaller because the interval length is `o(T)`.

## 5. Stress tests and boundaries

The localization is about Wang's current decomposition and does not prove that `M_T` is nonzero, large, arithmetic, or difficult to estimate. It identifies the quantity left uncontrolled at the relevant scale.

The argument uses fixed `0<theta<1` essentially through `H/T->0`. It does not apply unchanged to intervals with `H` comparable to `T`.

The source coordinate is fixed: `q` remains in a compact subset of `(0,infinity)`, so `x=e^(2*pi*q)` is bounded above and below independently of `T`. Moving source windows can change the relative sizes of the terms and require a separate audit.

The conclusion also depends on retaining Wang's exact explicit-formula decomposition rather than treating `E_x` only through its pointwise envelope. If `E_x` is later replaced by a different remainder convention, the signed mean must be translated before reusing this bottleneck statement.

Finally, an estimate for `M_T` must come from the actual explicit-formula remainder, not from assuming cancellation in the packet `h`; packet orthogonality and `t`-average cancellation are mathematically distinct mechanisms.

## 6. Prior-art and novelty boundary

The external inputs are Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918 (2026), especially equations (2.7)–(2.9) and the proof of Proposition 2.6, together with the explicit-formula framework inherited there from Baluyot, Goldston, Suriajaya, and Turnage-Butterbaugh, **An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function**, *Acta Arithmetica* 214 (2024), 357–376.

Wang explicitly bounds the `B_x^2` contribution by `O(HL/x^2)` and the `B_x,E_x` cross term by the same order inside the aggregate proposition. The refinement here uses only the additional short-interval fact `H=o(T)` to sharpen the former and then preserves the signed integral of `E_x` instead of taking its absolute pointwise bound immediately.

No novelty is claimed for Taylor expansion of `log`, short-interval averaging, or separating cross terms in a square. The durable Mathia content is the exact specialization to the active fixed-source channel: the previously opaque `1/L` floor is reduced to a single signed mean of the explicit-formula remainder, giving a concrete falsifiable target for the next source-side step.

## Research consequence

The fixed-source branch should now stop spending effort on the deterministic `B_x^2` variation or on extra packet moments. The first unresolved source quantity at the current asymptotic frontier is

`M_T(x)=(x/H) Re integral_I E_x(t) dt.`

A proof that `M_T=o(1)` on fixed source windows would cross the present `1/L` barrier; a proof of `M_T=O(L^(-1/2))` would expose the next `L^(-3/2)` source scale already visible in Wang's remainder decomposition. The natural next investigation is therefore the exact structure and short-interval mean of `E_x(t)` itself.

No untouched confirmation-zero data are used.
