# MI-018 — Canonical normalization can remove a nuisance while moving source specificity into an induced law and its remaining fluctuation channels

**Evidence level:** exact cross-line synthesis of [VIS-239](../../visual_exploration/findings/VIS-239-cumulative-intensity-gauge-uniformizes-specified-iid-intensity.md), [VIS-240](../../visual_exploration/findings/VIS-240-rotation-randomized-dirichlet-gaps-give-fixed-count-uniform-intensity-dependence-null.md), [VIS-241](../../visual_exploration/findings/VIS-241-random-cut-separates-endpoint-phase-variance.md), and [WP-318](../../weil_positivity/findings/WP-318-scalar-julia-tangents-are-boolean-self-energies-of-derivative-biased-measures.md). The probabilistic and Herglotz transformations are mathematically different; no common transform theorem is claimed.

Visual Exploration gives an exact probabilistic instance. For a fixed-count iid point model with specified continuous CDF `F`, the cumulative-intensity coordinate `U=F(X)` is uniform. The one-point intensity disappears completely from the pair calibration. If `F` is replaced by the same-sample empirical CDF, the normalization goes too far and turns spacing geometry into a deterministic rank statistic.

VIS-240 sharpens what remains after the legitimate marginal normalization. Symmetric Dirichlet cyclic gaps with random rotation give a whole family with the **same fixed count and exactly uniform one-point intensity** but different dependence; iid uniform spacings are only the `alpha=1` member. Removing the marginal therefore does not leave one canonical null. The source question moves into the induced dependence law and the uncertainty of any externally chosen or fitted `alpha`.

VIS-241 shows that even this induced law can contain a removable representation-boundary channel. Conditional on one circular configuration, the random cut contributes an exact variance `V_cut`, while averaging over the cut gives the intrinsic circular pair statistic

`bar T=sum_p w_p(1-delta_p/L)`.

For random gap geometry `G`,

`Var(T)=Var_G(bar T)+E_G[V_cut]`.

Thus the post-normalization fluctuation law factorizes into **intrinsic dependence geometry plus endpoint phase**. If the circle is only an auxiliary stationary representation, endpoint phase is nuisance and `bar T` quotients it out exactly. If physical interval endpoints are source-bearing, the same quotient would erase real information and `V_cut` belongs to the model. Whether a normalization is legitimate depends on the declared sigma-field, not on whether it makes the variance smaller.

Weil Positivity gives an exact analytic instance. At a regular scalar Herglotz boundary node, Julia reduction followed by derivative normalization sends the source measure to the derivative-biased probability law `nu_t` and the entire normalized response to `tau-K_(nu_t)`. The Herglotz sign of this Boolean self-energy is universal for every probability law, and every gap-supported probability law is realizable by a matched positive measure. Arithmetic specificity survives only in restrictions on the induced law `nu_t` and in any additional finite--archimedean coupling.

The common mechanism is not that these transforms are equivalent. It is that a **canonical normalization can exactly remove one source/nuisance coordinate while leaving a broad universal observable class, and the remaining law may itself split into intrinsic and representation-induced components**. Proving positivity, uniformity, a clean mean, or even a total variance after normalization does not recover source specificity until each surviving law/channel has been audited against matched controls.

The practical audit is therefore hierarchical. Write down the pushforward or biased law and the sigma-field used to construct it. Then factor any remaining randomness by source when possible: count, marginal intensity, dependence, endpoint phase, parameter uncertainty, finite-window effects. Quotient only channels declared irrelevant before confirmation. Source specificity must survive the resulting induced-law envelope rather than the simplest background member.

**Boundary.** VIS-239--VIS-241 concern fixed-count ordered/circular point geometry and a tent-pair statistic; WP-318 concerns pure-measure scalar Herglotz Julia responses. VIS-241 does not compute the remaining Dirichlet-gap variance, and WP-318 does not classify arithmetic derivative-biased laws. The shared content is the relocation and factorization of source information after normalization, not a shared probabilistic or operator theorem.