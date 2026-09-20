# MI-063 — Ford-scale observability is one hard box, and the pole must be Hardy-projected before squaring

**Evidence level:** exact harmonic/source-specific synthesis from [NB-246](../../findings/NB-246-demodulation-bandlimits-ford-pair-energy-to-the-window-scale.md), [NB-247](../../findings/NB-247-bellotti-population-turns-hard-ford-window-energy-into-pointwise-control.md), the method boundary [NB-248](../../findings/NB-248-squaring-the-ford-edge-logarithmic-derivative-hits-the-pole-critical-l2-endpoint.md), and the exact projection identity [NB-249](../../findings/NB-249-positive-ford-frequencies-collapse-first-order-depth-localization-to-a-one-sided-cauchy-projection.md), interpreted against NB-230, NB-237, NB-243 and NB-245. The required local second moment is sufficient, not known for zeta zeros.

Freeze the Ford parameters at a selected center and demodulate the common carrier. NB-246 shows that the moving-center current has bandwidth `O(H)` while its zero-pair expansion retains the fine phase `e^{iX(gamma_j-gamma_k)}` and horizontal depth marks. NB-247 adds enough population regularity that one literal hard-window energy
`I_A(t_0)=H int_{t_0-A/H}^{t_0+A/H}|R_{t_0}(s)|^2 ds`
is sufficient: a uniform `o(1)` bound implies uniform pointwise `o(1)` control, and the matched coherent packet still has nonvanishing hard-box energy.

NB-248 identifies the forbidden order of operations. In Ford-scaled two-dimensional edge coordinates, each zero contributes a Cauchy pole to `R^{-1} zeta'/zeta`; the pole is locally `L^p` only for `p<2` and logarithmically divergent at `p=2`. Squaring or taking absolute values of that area field before the signed divisor pairing therefore destroys the cancellation interface.

NB-249 identifies the corresponding allowed operation exactly. For every shell frequency the scaled frequency is positive, `lambda=Y+u/J>0`, so the Cauchy identity
`int_R e^(i lambda y)/(-x+i y) dy = 2 pi e^(lambda x) 1_{x<0}`
Hardy-projects the pole onto the shallower depth edge. With `x=(d-d_rho)/Y`, only `d<d_rho` survives. The exponential produced by the projection cancels the remaining Ford depth factors, and
`int_{-infinity}^{d_rho} chi'(d) dd = chi(d_rho)`
recovers the original marked zero coefficient. Thus the singular first-order field is not itself the Hilbert-space object: **project/pair first, obtaining the finite marked zero current, then square**.

This fixes the representation-level obstruction without solving the analytic one. The projection preserves the carrier phase, the depth mark and the matched coherent packets, so it does not manufacture Ford decay. The surviving problem is exactly the hard-window second moment of that projected finite current, or equivalently its two-copy depth-marked pair energy.

**Boundary.** NB-249 is an exact Cauchy/Hardy projection identity, not a zero-density estimate or a new local second-moment theorem. It removes the pole-critical planar `L^2` interface only because the actual Mellin shell has positive Fourier support; any argument that replaces the projected current by absolute local control of `zeta'/zeta` reintroduces the obstruction of NB-248.
