# MI-043 — Square-summable Euler spectrum caps the canonical complexity certificate

**Evidence level:** exact synthesis from [NB-174](../../findings/NB-174-capped-transport-approximate-complexity.md), [NB-175](../../findings/NB-175-joint-capped-transport-witnesses-certify-source-resolved-linear-complexity.md), [NB-176](../../findings/NB-176-euler-weighted-fourier-fingerprints-certify-source-complexity.md), and [NB-177](../../findings/NB-177-square-summable-euler-spectrum-caps-canonical-complexity-certificate.md).

NB-176 gives a source-native lower certificate for approximate Nyman template complexity by embedding the actual Euler frequencies of `zeta'/zeta` into one capped-Poisson-contracting Hilbert feature map. NB-177 shows that this canonicality does not make the witness asymptotically complete.

After the capped-transport Fourier estimate is applied, the squared normalized Euler amplitudes have a uniformly summable spectral tail. The exterior damping `n^(-a)` absorbs the apparent `1+a log n` growth, leaving a bound controlled by `Lambda(n)^2/n^2`. Consequently every bounded-transport fingerprint is uniformly approximable by finitely many Euler coordinates at each fixed positive resolution, even as `a->0`.

For `N` realized templates with normalized capped amplitude at most `X`, NB-177 derives

`tr sqrt(G^Eul) <= C X N^(3/4) sqrt(log(2N))`.

Thus the mean Euler singular value is at most `C X N^(-1/4)sqrt(log(2N))`. In particular the strong sufficient condition `G^Eul >= alpha^2 I_N` forces `alpha` to decay with `N`; bounded source amplitude cannot support arbitrarily many Euler-fingerprint directions at one fixed nonzero singular scale.

The same compactness bounds the complete NB-176 lower certificate. If `mathfrak C_T^Eul(epsilon)` denotes its supremum over finite template families, then

`mathfrak C_T^Eul(epsilon) << X_T^4 epsilon^(-2) log^2(2+X_T/epsilon)`

for `0<epsilon<X_T`, and it vanishes for `epsilon>=X_T`. At the high-ordinate tolerance `epsilon_T~log log T`, the regime `X_T=o(sqrt(log T))` therefore forces `mathfrak C_T^Eul(epsilon_T)=o((log T)^2)`, below the approximate-complexity scale that NB-174 says positive-density rescue would require.

This is a **certificate boundary, not a sampler impossibility theorem**. NB-175--NB-176 are one-sided: a small Euler Gram does not imply small `mathfrak L_T(epsilon)`. The actual template family may remain highly complex in capped-Poisson geometry while the square-summed Euler embedding compresses its distinctions below the declared source resolution.

The reusable lesson is that source-native coordinates and source-native resolution are not enough; the witness must also preserve the interaction consumed by the destination. Here the actual logarithmic derivative uses a coherent scalar phase sum, while the Euler Gram keeps squared-amplitude Hilbert geometry. A stronger certificate must retain more of that coherent prime-phase structure without violating the same jointly contractive source budget.

**Boundary.** The `N^(-1/4)` presentation is not claimed sharp, and NB-177 does not upper-bound `mathfrak L_T(epsilon)` itself. It rules out only the hope that arbitrarily many above-resolution directions can be certified by the static square-summed Euler Hilbert witness at bounded capped amplitude. Direct approximate-complexity bounds or different phase-sensitive contractive witnesses remain open.