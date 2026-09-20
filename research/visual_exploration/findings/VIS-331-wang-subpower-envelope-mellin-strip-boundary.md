# VIS-331 — subpower Wang source envelopes do not buy a fixed Mellin half-plane by decay alone

## Claim

Let Wang's symmetric squared-von-Mangoldt source remainder be

`R(x)=S(x)-log x`

with `S` as in `VIS-292` and `VIS-330`, and write its logarithmic-time profile as

`r(t)=R(e^t)` for `t>=0`.

Assume that for some eventually nonnegative function `phi(t)` and constant `C>0`,

`|r(t)| <= C exp(-phi(t))`

for all sufficiently large `t`. Define the lower linear decay rate

`a = liminf_(t->infinity) phi(t)/t`,

allowing `a=+infinity`.

Then the pointwise envelope alone certifies absolute, locally uniform convergence of Wang's tail Mellin transform

`F(w)=integral_1^infinity R(x)x^(-w-1) dx`

throughout

`Re(w)>-a`,

with the convention that `a=+infinity` gives all finite `w`.

Combining this with the pole divisor in `VIS-293`, every finite `a>0` forces the zero-free region

`Re(rho)>max(1/2,1-a)`

for nontrivial zeta zeros `rho`; if `a>=1/2`, this reaches RH exactly as in `VIS-330`.

By contrast, when `phi(t)=o(t)` — the genuine subpower regime in `x` — one has `a=0`. The pointwise decay envelope may still make `F(0)` or all right-side moments finite, but **the elementary absolute-convergence/fundamental-strip argument certifies no open half-plane with `Re(w)<0`**. In particular, the Korobov--Vinogradov envelope from `VIS-291`,

`phi_KV(t)=c t^(3/5)(log t)^(-1/5)`,

has zero linear rate and therefore carries no fixed zero-free-strip burden by this direct Mellin pricing mechanism.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-MELLIN/LAPLACE FUNDAMENTAL-STRIP SPECIALIZATION + NEGATIVE/BOUNDARY CONTROL + NO-NOVELTY-CLAIM`.

This is a statement about what the **pointwise majorant itself guarantees**. It does not prove that a subpower remainder cannot have additional cancellation, analytic continuation, or zero-free consequences by another argument.

## 1. Logarithmic time turns the tail Mellin transform into a Laplace transform

With `x=e^t` and `dx=e^t dt`, one has exactly

`F(w)=integral_0^infinity r(t) exp(-w t) dt`.

Thus the left edge obtained directly from pointwise decay is controlled by the exponential rate of `r(t)` in the logarithmic variable `t=log x`.

Fix a compact set `K` inside `Re(w)>-a`, and write

`sigma_K=min_(w in K) Re(w)`.

Because `sigma_K>-a`, choose a real number `eta` with

`-sigma_K < eta < a`.

By the definition of `liminf`, for all sufficiently large `t`,

`phi(t)>=eta t`.

Therefore uniformly for `w in K`,

`|r(t) exp(-w t)|`
` <= C exp(-(eta+sigma_K)t)`

for large `t`, and the right-hand side is integrable. The finite initial interval is harmless. Hence the defining integral converges absolutely and locally uniformly on every compact subset of `Re(w)>-a`, so `F` is holomorphic there.

If `a=+infinity`, the same argument works for every compact subset of the plane.

## 2. Positive linear rate reproduces the zero-free-strip price

`VIS-330` gives, initially for `0<Re(w)<2`,

`F(w) = [4/(4-w^2)]D(1+w) - C_0/(2-w) - 1/w^2`,

where `C_0=D(3)`, while `VIS-293` gives

`D(s)=(log zeta)''(s)+A(s)`

with `A` holomorphic for `Re(s)>1/2`.

Hence every nontrivial zero `rho` with `Re(rho)>1/2` produces an uncancelled double pole of the meromorphic right-hand side at

`w_rho=rho-1`.

If `a>0` and

`Re(rho)>1-a`,

then `Re(w_rho)>-a`, where the defining integral has just been shown holomorphic. The pole is impossible. Thus

`Re(rho)>max(1/2,1-a)`

is zero-free.

This recovers `VIS-330` when `phi(t)=delta t+O(1)`, for which `a=delta`. More generally, only the lower asymptotic **linear** component of `phi` is priced into a fixed Mellin half-plane by this argument.

## 3. Sublinear logarithmic decay sits exactly below the fixed-strip threshold

Suppose now that

`phi(t)=o(t)`.

Then `a=0`. For every fixed `epsilon>0`, the candidate left-half-plane weight at `w=-epsilon` is

`exp(epsilon t-phi(t))`.

The available pointwise comparison

`|r(t) exp(epsilon t)| <= C exp(epsilon t-phi(t))`

therefore does not provide an integrable majorant at infinity: the exponent on the right is eventually positive and asymptotic to `epsilon t`.

This does **not** prove divergence of the actual integral at `w=-epsilon`; an upper bound by a nonintegrable function cannot do that. It proves the narrower and useful statement that the subpower pointwise envelope, by itself, cannot certify absolute convergence on any fixed open strip to the left of `Re(w)=0`.

The distinction matters because many subpower envelopes are still strongly integrable on the boundary. For example `exp(-c t^alpha)` with `0<alpha<1` is integrable over `t>=0`, so it can control `F(0)`. But no fixed `epsilon>0` is absorbed by such a sublinear exponent, so this boundary control does not become an open negative half-plane without extra information.

## 4. The current Korobov--Vinogradov scale is in the analytically cheap class

`VIS-291` proves on every fixed source-exponent panel that Wang's complete fixed-power statistic inherits the unconditional source envelope

`exp(-c V(L))`,

where

`V(L)=L^(3/5)(log L)^(-1/5)`.

At source scale `x=e^t`, the corresponding exponent is

`phi_KV(t)=c t^(3/5)(log t)^(-1/5)=o(t)`.

Therefore its lower linear rate is zero. The same is true for any stretched-exponential or logarithmic improvement whose exponent remains `o(log x)`.

This identifies a clean boundary for the accepted Wang clue. A source-specific improvement can be **asymptotically stronger than the current Korobov--Vinogradov envelope while still remaining below every fixed power of `x`**. Such a gain is not automatically charged a fixed zero-free half-plane by the direct Mellin fundamental-strip argument. Its value must instead be decided quantitatively by whether it survives Wang's complete source, gamma, localization, cross-term, and moving-upper error budget.

Conversely, as soon as the lower logarithmic decay rate becomes positive, even if the envelope is not written as a pure power, the fixed-strip price reappears with width `a`.

## 5. Prior art and evidence boundary

The transform input is classical. Philippe Flajolet, Xavier Gourdon, and Philippe Dumas, **Mellin Transforms and Asymptotics: Harmonic Sums**, *Theoretical Computer Science* 144 (1995), 3--58, DOI `10.1016/0304-3975(95)00002-E`, develops Mellin fundamental strips and their relation to endpoint growth/decay; after `x=e^t`, the present tail transform is simply a Laplace transform. `VIS-330` already uses this source for the fixed-power case.

No novelty is claimed for Mellin/Laplace abscissae, comparison tests, or the distinction between exponential and subexponential decay in logarithmic time. The Mathia-specific content is the exact placement of the **remaining Wang source search space** relative to the pole divisor established in `VIS-293` and the Korobov--Vinogradov envelope propagated in `VIS-291`.

The result gives only a sufficient holomorphy domain from a pointwise envelope. It does not give a converse abscissa theorem for the actual signed remainder, does not exclude cancellation-based continuation, does not prove a new zero-free region, and does not show that any subpower improvement is quantitatively sufficient for Wang's final statistic.

## Dependencies

- `VIS-291`: current unconditional Korobov--Vinogradov-scale complete fixed-power envelope.
- `VIS-292`: exact Wang Green/Mellin identity.
- `VIS-293`: exact first-half-plane pole divisor of the squared-von-Mangoldt source transform.
- `VIS-330`: fixed-power real-axis decay implies a fixed zero-free half-plane.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose remaining source route is narrowed here.

## Research consequence

The live fixed-source question should no longer ask merely whether a candidate estimate is "subpower" or "weaker than RH." The relevant first classification is its logarithmic linear rate

`a=liminf phi(t)/t`.

If `a>0`, the candidate already carries the fixed zero-free-strip price above. If `a=0`, the direct pointwise Mellin argument does not impose such a strip, so the next meaningful test is quantitative rather than analytic-continuation bookkeeping: derive a **source-specific sublinear exponent or secondary expansion that genuinely improves the current Korobov--Vinogradov envelope**, prove the needed fixed-panel uniformity, and propagate that gain through Wang's complete error budget.
