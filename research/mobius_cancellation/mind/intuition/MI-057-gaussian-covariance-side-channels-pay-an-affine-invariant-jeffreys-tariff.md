# MI-057 — Gaussian covariance side channels pay an affine-invariant Jeffreys tariff

**Evidence level:** exact finite-channel synthesis from [MC-351](../../findings/MC-351-exact-dephasing-forces-singular-neighbor-transcripts.md), [MC-353](../../findings/MC-353-edge-jeffreys-is-the-exact-local-dephasing-currency.md), and [MC-355](../../findings/MC-355-gaussian-location-scale-covariance-side-channel-tariff.md). The result applies to a finite-dimensional nondegenerate Gaussian location-scale intermediate readout followed by a common source-independent kernel; it is not a theorem about arbitrary endpoint channels.

Allowing the noise covariance to depend on the source state is a genuine side channel, but in a Gaussian readout it is not free. For neighboring source states with

`Z|X=x ~ N(mu_x,Sigma_x)`

and complete transcript downstream of `Z`, half-Jeffreys divergence is bounded by the exact Gaussian row cost

`M_e + C_e`,

where `M_e` is the symmetric covariance-whitened mean displacement and

`C_e = (1/4) tr(A_e + A_e^(-1) - 2I)`,  `A_e=Sigma_x^(-1/2) Sigma_x' Sigma_x^(-1/2)`.

If the generalized covariance eigenvalues are `exp(t_j)`, then

`C_e = (1/2) sum_j (cosh(t_j)-1)`.

Thus source information can migrate from mean motion into variance or correlation modulation, but both motions are charged in the same reverse-discrimination currency. Combining this exact upper decomposition with the MC-353 endpoint lower bound forces a nonvanishing average budget in `M_e+C_e` whenever bounded coefficient energy still produces nontrivial dephasing.

With a covariance floor `Sigma_x >= sigma_R^2 I`, the same statement becomes geometric: the mean term is controlled by `||Delta_e||^2/sigma_R^2` and the covariance term by squared affine-invariant log-covariance motion. When relative covariance changes stay bounded, both normalized mean motion and covariance motion cannot vanish simultaneously while a fixed dephasing level survives.

There is also an exact endpoint exclusion. Any two finite nondegenerate Gaussian rows have finite KL in both directions. Exact unit-energy dephasing, however, forces singular neighboring transcript laws and infinite edge KL by MC-351. A Gaussian location-scale architecture can therefore reach that endpoint only by leaving the finite nondegenerate class: singular covariance, diverging resources, a side channel outside `Z`, or a non-Gaussian transcript.

The reusable lesson is that **a side channel should be priced in the inverse likelihood geometry it actually changes**. Common additive noise turns mean displacement into Jeffreys cost; source-dependent Gaussian noise adds a covariance-deformation term rather than invalidating the accounting. The next escape classes are those where this finite Gaussian likelihood geometry genuinely breaks—singular, non-Gaussian, adaptive or metadata-rich channels—not merely those with state-dependent variance.

**Boundary.** The Gaussian KL and affine-invariant SPD geometry are classical. The Mathia-specific statement is their composition with the independently derived endpoint discrimination tariff. No bound on `M(x)` follows, and no claim is made that a concrete Möbius endpoint observation admits this Gaussian factorization.