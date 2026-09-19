# MI-057 — Exact mixed-shell nullity collapses every closable radial positive form with absolutely-continuous translation spectrum

**Evidence level:** exact synthesis from [WP-374](../../findings/WP-374-positive-composite-nullity-collapses-stationary-radial-flux-to-zero-frequency.md), [WP-375](../../findings/WP-375-exact-mixed-shell-nullity-collapses-every-closable-log-radial-positive-form.md), and [WP-376](../../findings/WP-376-sobolev-radial-topologies-do-not-escape-exact-mixed-shell-nullity.md).

WP-374 first showed that translation-invariant positive radial forms are too rigid: mixed-prime shell nullity plus source coboundary identities force prime-power shell profiles into the translation-fixed zero-Mellin sector. WP-375 removes stationarity. In the canonical logarithmic-radial `L^2` topology, positivity makes every zero-energy mixed shell radical; spectator-prime identities

`h_(p^a q)=tau_(log q) h_(p^a)-h_(p^a)`

and weak escape of far translations let Mazur convexification approximate `-h_(p^a)` strongly by radical mixed shells. Closability then forces the prime-power shell itself into the radical.

WP-376 identifies the actual topological hypothesis more precisely. Every cyclotomic shell profile `h_n` is Schwartz, so it lies in every finite-order Sobolev `H^r`. In `H^r`, and more generally in any translation-invariant Fourier-weight Hilbert space

`||f||_(H_w)^2 = integral w(xi)|hat f(xi)|^2 dxi`

with positive measurable absolutely-continuous weight and the relevant `h_n` in the space, translations are unitary and `tau_t f -> 0` weakly as `|t|->infinity`. The proof is again Riemann--Lebesgue after the weighted Fourier product is placed in `L^1`. Therefore the WP-375 radical argument survives every such reweighting.

So the escape is not “choose a stronger or weaker Sobolev norm.” A successful topology must change the **spectral type seen by translations** or another load-bearing assumption. WP-376 supplies an exact control: adjoining the zero-frequency trace

`||f||_*^2 = ||f||_(H^r)^2 + c|hat f(0)|^2`

prevents far translates from disappearing in that coordinate. The bounded positive form `Q_*(f)=c|hat f(0)|^2` annihilates every mixed shell while retaining prime powers, because `hat h_n(0)=Lambda(n)`. But the retained value is exactly `c Lambda(n)^2`, the zero-Mellin survivor already isolated in WP-374, not the linear Weil coefficient.

Within the simplest atomic class, zero frequency is forced. If one Fourier atom `xi_0` retains a prime-power profile while annihilating all spectator-prime mixed shells, the identity

`hat h_(nq)(xi_0)=(e^(i xi_0 log q)-1)hat h_n(xi_0)`

forces `e^(i xi_0 log q)=1` for all spectator primes, hence `xi_0=0`. Thus moving to a single nonzero spectral atom does not create a new selector either.

The reusable audit is: before treating a topology change as new arithmetic structure, compute how remote source-forced translations behave in that topology. If they still escape weakly, exact positive nullity plus closability propagates through the same closure. If a singular spectral component blocks escape, identify what coefficient it actually retains; the simplest canonical component retains only the already-known `Lambda^2` zero mode.

**Boundary.** WP-376 does not classify arbitrary singular-continuous or multi-atomic spectral completions, approximate mixed-shell nullity, indefinite intermediate pairings, nonclosable forms, or genuinely nonradial/global geometry. It does not construct the linear finite Weil form or prove global Weil positivity/RH.