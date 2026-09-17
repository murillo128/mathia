# MI-043 — Diagonal cubes close density-one ordinary Gowers escape at the critical threshold

**Evidence level:** exact synthesis from [WI-332](../../findings/WI-332-u2-smallness-cannot-control-bow-sliding-variance.md)--[WI-337](../../findings/WI-337-almost-all-gowers-countermodels-reach-diagonal-threshold.md). The Gowers norms and Rademacher comparison mechanism are classical; the Mathia content is the matched-energy two-sided squeeze at the bow scale and the distinction between all-start and density-one quantifiers.

Earlier countermodels showed that local `U^2`, square-root cancellation against fixed-degree phases, and every fixed finite hierarchy of small local Gowers norms can coexist with full diagonal-scale sliding variance. WI-335 extended that obstruction to slowly growing order. WI-336 identified the complementary high-order barrier from the same matched energy.

For an interval of length `L` and a sequence with energy `E` comparable to `L log N`, the zero-increment cubes alone force

`||f||_(U^s(I)) >= sqrt(E/(2L)) L^(-1/2^s)`.

At the bow scale define

`R_s(L,N)=2^s loglog N/log L`.

WI-336 shows that any comparable-energy source cannot have ordinary normalized `U^s=o(1)` once `R_s>=2+eta`. Its all-interval Rademacher construction gives simultaneous smallness only below `R_s<=1-eta`, leaving at most one binary-order transition window for an **all-start** theorem.

WI-337 shows that this apparent gap disappears for the **density-one/almost-all** interface. A matched-energy Rademacher realization can be chosen so that, on `N-o(N)` prescribed bow-scale intervals and simultaneously for every retained order with

`R_s<=2-eta`,

all normalized `U^s` norms tend to zero, while those same good intervals still carry asymptotically the entire diagonal sliding variance. Thus deleting the exceptional starts does not remove the missing covariance: below every fixed margin from the deterministic diagonal threshold, almost-all ordinary Gowers smallness can coexist with full variance on the good set itself.

The density-one black-box transition is therefore pinned to `R_s=2` up to arbitrary fixed margins. Below it, ordinary Gowers smallness is too weak even when allowed to hold through growing order on almost every interval. Above it, the source's own diagonal energy makes ordinary smallness impossible. There is no remaining open interval of ordinary Gowers orders for an almost-all theorem to exploit.

This sharpens rather than eliminates the quantifier distinction. In the low-bow regime `theta<3/16`, the available arithmetic input is all-start, so the narrower all-interval transition window left by WI-336 remains logically different and may still support a source-specific critical statistic. In the higher regime, where current arithmetic uniformity is only almost-all, WI-337 says that simply strengthening the theorem to higher and higher **ordinary** Gowers order would not close the bow gate.

The reusable lesson is that **a norm hierarchy can saturate from both sides, and the source-start quantifier determines where the generic obstruction reaches the diagonal wall**. For density-one information, the random-sign obstruction reaches every fixed margin below the same threshold at which diagonal cubes make smallness impossible. A successful route must therefore leave the ordinary-smallness interface: preserve source-specific signed covariance, use genuinely all-start information where available, or define a renormalized/diagonal-free statistic whose large diagonal contribution has been removed before asking for higher-order uniformity.

For Weil inertia the destination remains the distinguished bow twist. The exact variance needs a macroscopic negative off-diagonal term to beat its positive diagonal contribution. WI-337 does not supply that sign; it shows that almost-all ordinary Gowers smallness, even hypothetically extended to growing order, cannot supply it as a black-box consequence.

**Boundary.** WI-337 makes no assertion exactly at `R_s=2`, does not construct an arithmetic counterexample with the prime singular series, and does not close the all-start critical window. It does not describe the actual `Lambda-Lambda^sharp` covariance or rule out a diagonally renormalized higher-order statistic. The result closes the density-one ordinary-Gowers escape, not the source-specific arithmetic covariance problem.
