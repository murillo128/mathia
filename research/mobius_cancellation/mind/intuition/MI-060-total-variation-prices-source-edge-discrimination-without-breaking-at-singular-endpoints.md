# MI-060 — Total variation prices source-edge discrimination without breaking at singular endpoints

**Evidence level:** exact synthesis from [MC-350](../../findings/MC-350-exact-source-quotient-needs-extensive-boundary.md), [MC-353](../../findings/MC-353-edge-jeffreys-is-the-exact-local-dephasing-currency.md), and [MC-359](../../findings/MC-359-total-variation-source-edge-tariff.md). The Jensen--Shannon/total-variation inequality and coupling bound are classical; the Mathia content is their composition with the reciprocal-endpoint information lower bound and source-edge geometry.

For neighboring source states `e={x,x'}` let

`t_e=TV(P_x,P_x')`

for their complete admitted transcript laws, and normalize the edge budget by

`T_1=(2/m) sum_e t_e`.

MC-359 proves

`I(X;Y) <= (log 2) T_1 + 2(R-1)log 2/m`.

Combining this with the independent endpoint transcript-information floor gives a bounded source-edge tariff. Under coefficient energy at most `C` and fixed nontrivial dephasing `eta`,

`liminf T_1/R >= eta^2/(2C log 2)`

along the even-rank endpoint regime. At matched-filter energy and vanishing dephasing error the normalized TV budget tends to its maximal value, and at the exact unit-energy endpoint every surviving source edge has mutually singular transcript laws and hence `t_e=1`.

This fills the gap between the exact row-cut and KL/Jeffreys descriptions. Exact quotient separation only records whether neighboring rows differ. Jeffreys divergence gives a sharp smooth local currency but becomes infinite when rows become singular. Total variation remains in `[0,1]` and therefore continues to measure how much of the source graph must be separated as the endpoint moves all the way to singularity.

The useful architectural form comes from genuine shared randomness. If

`Y=F(x,U_0)` with `U_0` independent of the source,

then the common-seed coupling gives

`TV(P_x,P_x') <= P(F(x,U_0) != F(x',U_0))`.

Thus a proposed mechanism cannot hide the compulsory source tariff merely by making its output laws singular or by using randomization. If flipping one source coordinate changes the complete transcript for only a vanishing fraction of shared seeds on average, its TV edge budget is too small for fixed nontrivial bounded-energy dephasing. Random seeds, adaptive branches and hidden state must be counted in the actual transcript architecture before applying the bound.

The reusable distinction is between **divergence geometry and bounded edge distinguishability**. Smooth channels may be priced efficiently by Fisher/Jeffreys action; singular or nearly deterministic channels can instead be audited by TV or a common-seed change probability. These are not interchangeable numerical currencies, but both must pay the same destination-imposed requirement that a positive fraction of source directions become observably different.

**Boundary.** MC-359 supplies no arithmetic upper bound for a Möbius-derived channel and no direct estimate for `M(x)`. A large TV edge budget is necessary, not sufficient, for the desired dephasing. The common-seed inequality is useful only when the shared-randomness representation is genuine rather than a post-hoc coupling. The next productive step remains architecture-specific: expose the actual Möbius endpoint transcript and prove that one-source flips affect too few shared seeds/output mass, or identify the real source-dependent mechanism that pays the required TV separation.
