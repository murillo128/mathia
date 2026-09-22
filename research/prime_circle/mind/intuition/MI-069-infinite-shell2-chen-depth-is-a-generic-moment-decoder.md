# MI-069 — Infinite shell-2 Chen depth is a generic moment decoder

**Evidence level:** exact radial-signature reduction and matched-control classicalization from [PC-399](../../findings/PC-399-shell2-chen-ladder-is-a-generic-moment-decoder.md), sharpening the distinction between exact source recovery and arithmetic selectivity already present in MI-024.

For `X_n(z)=log Phi_n(z)` and the repeated reference shell `2`, PC-399 identifies the one-sided Chen ladder exactly:

`k! J_(2^k,n) = integral_0^1 X_2(z)^k dX_n(z)`,

with `X_2(z)=log(1+z)`. Because `X_2` is a homeomorphism from `[0,1]` to `[0,log 2]`, the full ladder is the compact moment sequence of the pushforward measure `(X_2)_*(dX_n)`. Polynomial density then reconstructs that measure, hence `dX_n`, `X_n`, `Phi_n`, and finally the shell index `n`.

This gives a precise interpretation of what infinite ordered depth buys. It does not refine the depth-one Mangoldt selector while preserving its support. The zeroth moment is `J_n=Lambda(n)`, but higher moments necessarily recover information on shells for which `Lambda(n)=0`; the complete ladder fills the selector's nullspace because it is becoming information-complete.

The same decoder works for an arbitrary bounded-variation profile `Y` with `Y(0)=0`: the moments of the pushforward under `log(1+z)` reconstruct `Y`. Thus shell injectivity, even at all Chen depths, is reproduced by a matched non-arithmetic family. The arithmetic input chooses the cyclotomic profiles; compact moment inversion supplies the injectivity.

The live nonperturbative question is therefore downstream of reconstruction. A Prime-Circle mechanism must derive a distinguished operation on the recovered shell information — a compression, multiplication law, sign/coercivity form, spectral invariant, cross-level evolution or other source-forced readout — whose decisive behavior is not reproduced by the generic moment decoder. Merely passing from finite Chen depth to the universal full signature does not supply that extra structure.

**Boundary.** PC-399 gives no quantitative stability theorem for finite or noisy prefixes of the ladder and does not classify every resummed holonomy or nonlinear cross-shell operation. It only closes the inference that infinite-depth retention or signature injectivity by itself is evidence of a new arithmetic or zeta-selective carrier.