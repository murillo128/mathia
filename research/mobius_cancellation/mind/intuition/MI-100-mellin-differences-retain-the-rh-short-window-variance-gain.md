# MI-100 — Keeping the Mellin difference retains the RH short-window variance gain

**Evidence level:** supported conditional synthesis of the classical analytic inputs and explicit derivation in [MC-520](../../findings/MC-520-rh-mellin-variance-closes-conditional-farey-window-target.md). RH is assumed throughout; no new unconditional cancellation or novelty is claimed.

Let `M(x)=sum_(n<=x) mu(n)`. For fixed `1/2<sigma<1`, RH makes `f_sigma(u)=exp(-sigma u)M(exp u)` integrable and square integrable, with Fourier transform `1/((sigma+it)zeta(sigma+it))`. Keeping the two endpoints together gives the exact multiplier identity

`int_0^infty |M((1+delta)x)-M(x)|^2 x^(-2sigma-1) dx`
`= (1/(2pi)) int_R |((1+delta)^(sigma+it)-1)/((sigma+it)zeta(sigma+it))|^2 dt`.

For `0<delta<=3`, the difference factor is bounded by `C_sigma min(delta,(1+|t|)^(-1))`. RH also gives `1/zeta(sigma+it) <<_(sigma,a) (1+|t|)^a` for every fixed `a>0`. Splitting at `|t|=1/delta`, with `0<a<1/2`, bounds the weighted integral by `O_(sigma,a)(delta^(1-2a))`. The low-frequency factor `delta` is precisely what separate endpoint majorization discards.

Saffari–Vaughan averaging transfers multiplicative windows with `delta` comparable to `H/X` to the fixed additive window without a power loss:

`int_X^(2X) |M(x+H)-M(x)|^2 dx <<_(sigma,a) X^(2sigma+2a) H^(1-2a)`.

For `0<epsilon<1`, choose `sigma=1/2+epsilon/4`, `a=epsilon/4`. Uniformly in real `X>=2`, `1<=H<=X`, this yields `O_epsilon(X^(1+epsilon)H)`. For integer `X,H` the integral equals the discrete sliding moment exactly. There is no exceptional-start set or uncontrolled source-selected scale.

The fixed positive distances `sigma-1/2` and `a` are load-bearing. This does not give a logarithmic-loss bound, an asymptotic, or uniform control as `sigma` tends to `1/2`. The same conditional mechanism applies to Liouville via `zeta(2s)/zeta(s)`; the all-plus squarefree series `zeta(s)/zeta(2s)` has a pole at `1` and fails the analytic hypotheses. The gain is therefore conditional analytic structure, not a generic bounded-coefficient law or a Möbius-specific discriminator.

[MC-178](../../findings/MC-178-chinis-polynomial-window-smooth-number-ceiling.md) still proves that Chinis's particular large-prime-factor/block-extension bound gives only a subpower saving at fixed polynomial lengths. That limitation does not extend to every RH method: the `X^epsilon` loss above can be made smaller than any prescribed fixed power of `H=X^(beta+o(1))` when `beta>0` is fixed. MC-520's derivation does not depend on the independently unverified unpublished estimate attributed to Gao, and cannot be used as an unconditional input to an RH-directed bootstrap.
