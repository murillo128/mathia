# MI-046 — Euler frequency support is not source fidelity when amplitudes or acquisition cost can be normalized away

**Evidence level:** exact matched-control synthesis from [NB-176](../../findings/NB-176-euler-weighted-fourier-fingerprints-certify-source-complexity.md), [NB-177](../../findings/NB-177-square-summable-euler-spectrum-caps-canonical-complexity-certificate.md), [NB-178](../../findings/NB-178-coordinatewise-phase-codes-recover-linear-source-complexity-certificates.md), [NB-179](../../findings/NB-179-poisson-separated-dipoles-realize-maximal-coordinatewise-phase-codes-without-arithmetic.md), [NB-180](../../findings/NB-180-prime-power-euler-frequency-support-still-admits-geometric-fourier-codes.md), and [NB-181](../../findings/NB-181-bounded-hilbert-acquisition-cannot-recover-hadamard-scale-euler-codes.md).

NB-179 shows that unrestricted coordinatewise capped-Poisson probes can manufacture a maximal Hadamard-scale response on generic separated dipoles without arithmetic. A natural attempted repair is to allow only frequencies that genuinely occur in the Euler source. NB-180 shows that **frequency membership alone is still too weak** if each admitted coordinate may be independently normalized to the metric unit ball.

One fixed prime already supplies the exact progression

`log(p^m)=m log p`.

At the explicit widths `a_N=pi/(N log p)`, a block of `N` consecutive prime-power frequencies forms an exact DFT grid on the same generic packed dipoles used by the matched control. After independent capped-Poisson normalization, every response singular value stays on the `sqrt(N)` scale, so the coordinatewise dual again certifies linear approximate complexity. No prime-gap input or subtle arithmetic correlation is needed: the harmonic progression inside one prime-power tower is enough.

The actual logarithmic-derivative source behaves completely differently because its frequency coordinates do not have equal strength. The channel at `p^m` carries amplitude

`(log p) p^(-m(1+a))`.

Retaining those Euler amplitudes on exactly the same frequency block makes the nuclear response exponentially small in `N`. Recovering the normalized Fourier code requires multiplying the weak channels by factors growing like `p^(m(1+a))`. The apparent arithmetic phase code is therefore purchased by an exponentially expensive inverse renormalization.

NB-181 shows that this is not merely an artifact of the particular coordinatewise normalization. Put the true Euler amplitudes into the canonical feature Hilbert space and let `K` acquisition vectors have RMS Hilbert norm `G`. The response obeys a nuclear bound of the form

`||A||_* <= X sqrt(NK) G`.

Consequently, an `N x N` response with all singular values on the `sqrt N` scale forces `G` itself to grow on the `sqrt N` scale. Bounded Hilbert acquisition cannot recover the Hadamard code for free once the true source amplitudes are retained.

The genuine Euler scalar readout is not a contradiction. Its phase vector has coordinates `e^(-it log n)` and is not in `ell^2`; the scalar Dirichlet series is defined because the Euler amplitudes provide stronger weighted summability. The natural arithmetic channel therefore lives outside the bounded Hilbert dual used by the nuclear certificate. This identifies a precise next resource: a source-natural weighted/Dirichlet acquisition geometry whose finite conditioning budget includes the actual amplitudes and phases without independently amplifying weak coordinates.

The source-fidelity lesson is sharper than “use arithmetic frequencies.” A source-native probe family must retain, or explicitly charge for removing, the **coupling between frequency location, source amplitude and acquisition topology**. Support-only restrictions preserve labels while discarding conditioning; bounded Hilbert probes retain amplitudes but exclude the unbounded phase functional through which the actual scalar Euler readout is formed.

The matched-control audit for a future arithmetic dual should therefore ask whether its large spectral spread survives after the same source amplitudes, normalization budget, acquisition topology and conditioning are imposed on the control. A certificate that needs exponentially amplified prime-power channels or `sqrt N`-growing Hilbert acquisition has not established logarithmic Euler rescue at bounded source cost.

**Boundary.** NB-180 gives an exact DFT construction only along a sequence of Poisson widths and uses proper prime powers essentially. NB-181 is a bounded-Hilbert acquisition theorem, not a no-go result for weighted `ell^1`, Dirichlet, nonlinear or other source-natural duals. Neither shows that the natural Nyman template range equals the synthetic dipole packing or rules out a genuinely arithmetic non-Hilbert certificate.