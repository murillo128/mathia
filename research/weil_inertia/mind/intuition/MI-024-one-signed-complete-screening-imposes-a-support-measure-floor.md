# MI-024 — One-signed complete screening imposes a positive support-measure floor

**Evidence level:** exact line-local consequence of WI-240, WI-284, WI-287 and [WI-294](../../findings/WI-294-one-signed-pole-sign-kills-large-two-island-complete-screening.md). The large symmetric two-island exclusion uses only the classical PNT after the support floor is established.

Complete screening of the actual first-crossing mode is stronger than saying that the prime-deleted form has zero spectral bottom on its support. WI-284 gives a specific null vector `v>=0` with `q_arch(v)=0`.

For that vector, the pole form factors as `2 L_-(v)L_+(v)` and is **strictly positive**, because both exponential moments are positive for nonzero `v>=0`. Hence the gamma term must be negative. But the support-measure Fourier cap and bathtub bound give

`G(v)/||v||_2^2 >= log(1/mu)-C_0`, `mu=|{v>0}|`.

Negative gamma energy therefore forces `mu>exp(-C_0)=mu_0>0`. A one-signed completely screened null mode cannot concentrate on supports of arbitrarily small total measure.

This reveals why the earlier unrestricted spectral-bottom relaxation was too pessimistic. Signed test vectors can exploit the negative eigen-direction of the rank-two pole form; the actual nonnegative null vector cannot. Preserving a source-side sign constraint changes the coercive geometry before any detailed prime-gap estimate is used.

For a symmetric two-island support, complete screening plus the PNT places primes in every fixed multiplicative interval at sufficiently large scale, forcing each island width to zero. The support-measure floor then rules out the entire large-aperture branch.

**Boundary.** The floor does not exclude sign-changing modes, incomplete screening, bounded-aperture configurations, or many-component supports with positive total measure. Its reusable content is the constrained-variational principle: before optimizing over a larger function class, retain sign information carried by the actual null vector, because the relaxation can create false escape directions.
