# MI-058 — Regular exponential-family channels pay integrated Fisher edge action

**Evidence level:** exact finite-channel synthesis from [MC-351](../../findings/MC-351-exact-dephasing-forces-singular-neighbor-transcripts.md), [MC-353](../../findings/MC-353-edge-jeffreys-is-the-exact-local-dephasing-currency.md), and [MC-356](../../findings/MC-356-regular-exponential-family-fisher-edge-tariff.md). The exponential-family information geometry is classical; the Mathia-specific statement is its composition with the independently derived reciprocal-endpoint discrimination tariff.

Suppose an intermediate readout belongs to a finite-dimensional regular exponential family with natural parameter `theta_x`, source-independent carrier/support, and complete transcript obtained by one source-independent downstream kernel. For a neighboring source edge `e={x,x'}`, let `Delta_e=theta_x'-theta_x` and

`F_e = int_0^1 Delta_e^T I(theta_x+t Delta_e) Delta_e dt`,

where `I` is the Fisher information matrix in natural coordinates.

The row-level half-Jeffreys divergence is exactly `F_e/2`; after downstream processing it can only decrease. Thus Fisher action is not a local quadratic approximation here but the exact symmetrized reverse-discrimination cost integrated along the natural-parameter edge.

Combining this identity with MC-353 gives a compulsory endpoint budget. If coefficient energy is at most `C` and a fixed nontrivial dephasing level `eta` survives, then

`E_e F_e >= 2 eta^2/C - o(1)`.

Hence an admitted regular exponential-family architecture cannot simultaneously make its average Fisher edge action vanish and preserve bounded-energy dephasing. Bernoulli, Poisson, categorical and Gaussian sufficient-statistic modulation are all instances of the same tariff; changing higher moments through a regular sufficient-statistic law is not an unpriced escape.

The exact endpoint is even more rigid. Two finite regular interior rows share support and have finite directed KL. Exact unit-energy dephasing requires neighboring transcript laws to be singular, so an exact endpoint factorization cannot remain entirely inside the regular interior. Some parameter must approach a singular boundary, support must change, an unpriced side channel must enter, or the readout must leave the regular exponential-family model.

The reusable point is that **smooth source modulation should be priced in the intrinsic likelihood geometry of the channel, not by Euclidean parameter motion or by the label “Gaussian/non-Gaussian.”** Gaussian covariance deformation is one coordinate realization; integrated Fisher action is the broader invariant row cost for regular exponential families.

**Boundary.** The theorem does not cover source-dependent support, singular boundary limits, nonparametric families, general mixtures, infinite-dimensional models or transcript information outside the stated Markov factorization. It also does not show that any concrete Möbius endpoint architecture has small Fisher action. The next useful contradiction must pair the compulsory lower budget with an arithmetic upper bound for the actual channel class.