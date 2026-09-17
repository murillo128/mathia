# MI-059 — Fixed-component mixtures pay their source tariff in the mixing law

**Evidence level:** exact synthesis from [MC-353](../../findings/MC-353-edge-jeffreys-is-the-exact-local-dephasing-currency.md) and [MC-357](../../findings/MC-357-fixed-component-mixture-edge-tariff.md). Relative-entropy and total-variation data processing are classical; the Mathia content is their composition with the reciprocal endpoint discrimination lower bound.

Suppose a source-dependent mixture factors as

`X=x -> Theta~nu_x -> Y~K(.|Theta)`

with a component kernel `K` that is independent of the source. For a natural neighboring source edge `e={x,x'}`, half-Jeffreys divergence contracts through the fixed kernel:

`b_e(Y) <= b_e(Theta)`.

MC-353 independently forces `E_e b_e(Y) >= eta^2/C-o(1)` under bounded coefficient energy `C` and fixed nontrivial dephasing `eta`. Therefore every fixed-component mixture that carries the endpoint must pay

`E_e b_e(Theta) >= eta^2/C-o(1)`.

The output density may be highly non-Gaussian, multimodal, singular-looking or outside a finite-dimensional exponential family; none of that creates free discrimination when all source dependence enters through the mixing law. The latent law is the bottleneck.

For a finite component bank with categorical weights `w_x`, the latent tariff is explicit:

`b_e(Theta) = (1/2) sum_j (w_(x,j)-w_(x',j)) log(w_(x,j)/w_(x',j))`.

Inside the simplex this prices weighted squared motion of the weights. At the exact endpoint, total-variation contraction is sharper: mutually singular neighboring transcript laws force mutually singular mixing laws, so finite categorical mixtures need disjoint neighboring supports. An all-interior weight path cannot realize exact dephasing.

The reusable point is that **mixture complexity and source complexity are different resources**. A fixed library of arbitrarily complicated components cannot manufacture source information absent from the latent selector. To escape the tariff, the architecture must change the component kernel with the source, approach a singular/support-changing latent law, or expose another source-dependent transcript path.

**Boundary.** MC-357 gives no arithmetic upper bound on the latent Jeffreys budget and does not price genuinely source-dependent component kernels. Growing component count can also destroy simple Euclidean interior-floor corollaries even though the exact data-processing inequality remains valid. The next contradiction still needs a theorem showing that the actual Möbius architecture cannot afford the required latent/component discrimination.