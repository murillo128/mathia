# MI-046 — Euler frequency support is not source fidelity when amplitudes can be renormalized away

**Evidence level:** exact matched-control synthesis from [NB-176](../../findings/NB-176-euler-weighted-fourier-fingerprints-certify-source-complexity.md), [NB-177](../../findings/NB-177-square-summable-euler-spectrum-caps-canonical-complexity-certificate.md), [NB-178](../../findings/NB-178-coordinatewise-phase-codes-recover-linear-source-complexity-certificates.md), [NB-179](../../findings/NB-179-poisson-separated-dipoles-realize-maximal-coordinatewise-phase-codes-without-arithmetic.md), and [NB-180](../../findings/NB-180-prime-power-euler-frequency-support-still-admits-geometric-fourier-codes.md).

NB-179 shows that unrestricted coordinatewise capped-Poisson probes can manufacture a maximal Hadamard-scale response on generic separated dipoles without arithmetic. A natural attempted repair is to allow only frequencies that genuinely occur in the Euler source. NB-180 shows that **frequency membership alone is still too weak** if each admitted coordinate may be independently normalized to the metric unit ball.

One fixed prime already supplies the exact progression

`log(p^m)=m log p`.

At the explicit widths `a_N=pi/(N log p)`, a block of `N` consecutive prime-power frequencies forms an exact DFT grid on the same generic packed dipoles used by the matched control. After independent capped-Poisson normalization, every response singular value stays on the `sqrt(N)` scale, so the coordinatewise dual again certifies linear approximate complexity. No prime-gap input or subtle arithmetic correlation is needed: the harmonic progression inside one prime-power tower is enough.

The actual logarithmic-derivative source behaves completely differently because its frequency coordinates do not have equal strength. The channel at `p^m` carries amplitude

`(log p) p^(-m(1+a))`.

Retaining those Euler amplitudes on exactly the same frequency block makes the nuclear response exponentially small in `N`. Recovering the normalized Fourier code requires multiplying the weak channels by factors growing like `p^(m(1+a))`. The apparent arithmetic phase code is therefore purchased by an exponentially expensive inverse renormalization.

The source-fidelity lesson is sharper than “use arithmetic frequencies.” A source-native probe family must retain, or explicitly charge for removing, the **coupling between frequency location and source amplitude**. Support-only restrictions preserve labels while discarding the conditioning that says how strongly the source actually exposes each label.

This also explains why NB-176 and NB-177 were not merely using an inconvenient normalization. Their Euler weights are part of the source geometry. The compactness ceiling of the jointly weighted witness may be a real limitation of that acquisition primitive; escaping it by normalizing every weak coordinate independently changes the admitted source access rather than extracting free information from the original one.

The matched-control audit for a future arithmetic dual should therefore ask whether its large spectral spread survives after the same source amplitudes, normalization budget and acquisition conditioning are imposed on the control. A certificate that needs exponentially amplified prime-power channels has not established logarithmic Euler rescue at bounded source cost.

**Boundary.** NB-180 gives an exact DFT construction only along a sequence of Poisson widths and uses proper prime powers essentially. It does not prove the same control for a class restricted to distinct-prime frequencies, does not show that the natural Nyman template range equals the synthetic dipole packing, and does not rule out another source-faithful arithmetic probe family. Its exact negative conclusion is that genuine Euler **frequency support**, combined with independent coordinate normalization, is not by itself an arithmetic discriminator.