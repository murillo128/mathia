# Weil-inertia research lines

This file records the current mathematical questions that survive the Weil-Inertia evidence. It is not a roadmap, task queue, status page, or history.

## Separate collective RH reserve from defect-sensitive arithmetic information

WI-387--WI-393 locate the compactness and square-root-prime boundaries for fixed-width Weil trials. Escaping logarithmic spectral tightness can create a source-exact positive RH floor, but the same dilute carrier may remain blind to sparse off-line defects. The crossover occurs when the shifted prime polynomial has absolute size comparable with the local zero-density reserve, near `e^(A/2)~log R`. Beyond that scale a useful converse needs signed prime cancellation, stronger per-defect amplification, or collective defect aggregation rather than only an RH-side density floor.

WI-397--WI-398 show that passing from a scalar Fourier observable to a matrix-valued one does not remove this cost by dimension alone. Jutila-type horizontal Fourier control leaves a `log^2 T` source-budget barrier: a positive-density scalar separation requires that budget, and a matrix inertia change requires either the same order of operator total variation or a reference spectral margin collapsing at the corresponding rate. Nominal matrix rank is not a free amplification resource.

## Use the Widder/superzeta hierarchy only with a defect-determining global identity

WI-399--WI-405 depend on a recent non-peer-reviewed Rafik preprint and should be read with that evidence boundary explicit. Conditional on the fixed-height prime/zero root-rate interface audited there, WI-401--WI-404 price endpoint mesh, root-rate slack and cross-height averaging exactly. The scalar law `d^2 <= epsilon gamma^2 + (1+epsilon)h^2` shows that fixed positive slack becomes vacuous at high ordinate, and the one-defect positive moment has scale `C_p d^(2p+1) gamma^(a-2p)`, so `a=2p` is the exact polynomial height-weight threshold for finite-`p` nonnegative averaging.

WI-405 identifies the signed Mellin family with Voros's second-kind superzeta. The locally attractive critical Widder weight corresponds to superzeta exponent `sigma=-1`: at finite height it carries a clean horizontal-defect charge, but the zero sum is outside absolute convergence and therefore needs a renormalization theorem rather than termwise summation.

WI-406 closes the naive continuation version of that theorem. Voros's canonical meromorphic continuation gives the exact actual-spectrum value `Z(-1|0)=-9/32`. This fixed scalar is not a nonnegative global sum of off-line horizontal defects. The finite-cutoff identity survives only as a difference between the actual zero sequence and a fictitious same-ordinate criticalized baseline, and the continuation of the actual superzeta does not automatically provide a matched finite part for that second sequence.

WI-407 shows that differentiating in the superzeta exponent creates a stronger local carrier but not yet a defect-to-zero principle. For a same-ordinate off-line pair of depth `d` at height `gamma`, the actual-minus-criticalized derivative defect is strictly positive and asymptotic to `4 d^2 log gamma` at fixed `d`. A hypothetical matched finite part would therefore imply a log-weighted square-depth budget such as `sum d_rho^2 log gamma_rho < infinity`. Mere finiteness is insufficient for RH.

WI-408 closes the whole **finite exponent-jet finiteness** escape. At derivative order `k`, the same pair contributes

`Q_k(gamma,d)=2^(k+1) d^2 (log gamma)^k [1+O_k(1/log gamma+d^2/gamma^2)]`.

Thus any fixed finite jet controls only finitely many logarithmic moments of the horizontal-defect measure. Even requiring every fixed-order logarithmic moment to be finite separately does not force the measure to vanish: a sparse hypothetical family such as `gamma_n=e^n`, `d_n=e^(-n)` makes all of those moments summable while retaining infinitely many off-line defects. Nor does a generic tail bound merely tending to zero become coercive; a finite off-line set disappears from every sufficiently high tail, and sparse infinite defects can decay faster than the prescribed envelope.

WI-409--WI-410 expose a different but complementary obstruction in the classical half-plane factorization. The fixed Balazard--Saias--Yor/Blaschke probe gives a positive horizontal-defect charge that decays like `d/gamma^2`. Allowing the whole real Poisson-scale family improves the best single-zero response only to

`sup_(a>0) q_a(gamma,d)=arsinh(d/gamma) <= d/gamma`.

Consequently any finite signed mixture of these scales with total variation `M` has response at most `M d/gamma`. A fixed finite source budget cannot therefore produce a height-uniform `O(d)` tariff inside this family. Kondratyuk's Carleman--Nevanlinna endpoint shows that a height-unweighted positive defect `sum |Re rho-1/2|` does exist classically, but precisely without an independently controlled finite source budget strong enough to force that sum to vanish. Removing height decay and retaining a finite budget are separate requirements.

WI-411 closes the simplest vertical-translation escape from that real-axis barrier inside the same finite-total-variation mixture model. For a translated half-plane probe `s=1/2+a+ib`, the one-zero Blaschke charge satisfies the exact height-area identity

`int_R q_(a,b)(gamma,d) dgamma = 2 pi min(a,d) <= 2 pi d`,

independent of the center `b`. Hence a mixture with coefficient total variation `M` has integrated response at most `2 pi d M`; obtaining `Omega(d)` sensitivity on an interval of length `L` forces `M=Omega(L)`. The order is sharp: uniform linear-depth response on `[T,2T]` costs `Theta(T)` coefficient mass. Translation can move local sensitivity to the target height, but it cannot convert localization into a fixed finite-budget detector over an expanding height range.

WI-412 closes the canonical scale-mixing escape left by that area law. Mixing the centered Blaschke probes over horizontal scale with Haar measure `da/a` gives the exact one-zero kernel

`H_b(gamma,d)=pi arctan(d/|gamma-b|)`

and, at exact ordinate matching, the depth-independent quantum `pi^2/2` for every `d>0`. But this fixed quantum is bought only outside the finite-budget regime. In logarithmic scale the centered kernel is `K(t)=log coth(|t|/2)` with `||K||_1=pi^2/2`; any finite signed/complex scale measure of TV mass `M` can therefore sustain response at least `c` across only `O(M/c)` logarithmic depth length. Covering `d_min<=d<=d_max` costs at least a constant times `log(d_max/d_min)`. The Haar escape has infinite total variation, and its mixed height profile has a nonintegrable `1/|gamma-b|` tail with logarithmically divergent mass.

WI-413 removes the remaining exact tempered-distribution loophole for that centered scale architecture. The log-scale convolution kernel has Fourier multiplier

`Khat(xi)=pi/xi tanh(pi xi/2)`, with `Khat(0)=pi^2/2`,

which is smooth, strictly positive on the real axis, and has a slowly increasing reciprocal. Convolution by `K` is therefore an automorphism of tempered distributions. If a tempered log-scale distribution produces an **exact constant** response `q` at every depth, its unique preimage is

`mu(ds)=(2q/pi^2) ds`, equivalently `mu(da)=(2q/pi^2) da/a`.

So normalized Haar mixing is not merely one way to obtain the exact all-depth count quantum: it is the unique tempered linear realization. Combined with WI-412, exact all-depth flatness uniquely forces the same infinite scale budget and nonintegrable height tail. Oscillatory signed derivatives or other tempered generalized functions cannot cancel around that cost.

WI-414 strengthens the scale-side closure from exact flat response to one-sided coercivity. For a translation-bounded signed or complex scale measure, a global lower response `|nu*K|>=q` forces the total-variation measure to have lower Beurling density at least `2q/pi^2`. Sparse infinite packets therefore cannot beat Haar-rate local scale budget. Finite depth windows remain different, but global positive coercivity in the natural measure class is already extensive in logarithmic scale.

WI-415 couples scale and height directly. For finite-TV mixtures of translated Blaschke probes required to deliver a fixed count quantum `q` throughout `[T,2T] x [delta,d_0]`, the exact vertical area law forces TV cost asymptotic to `qT/(2pi delta)`. The reciprocal shallow-depth tariff is sharp: arbitrary coupling between horizontal scale and vertical center cannot beat it for continuum coverage.

WI-416 shows why that continuum theorem cannot simply be transferred to the actual discrete exceptional set by zero counts or spacing. If the probe locations may be adapted to a finite target set of hypothetical zeros, logarithmic concentration near each target drives the infimum TV cost all the way to zero. The missing resource is therefore **non-oracular regularity of probe placement**, not more accurate counting of exceptional ordinates.

WI-417 now computes the corresponding one-target bounded-density problem exactly rather than only up to exponent. If the translated-probe coefficient measure is absolutely continuous in `(a,b)` with density bounded by `B`, then the optimal TV mass `M_B(d,Q)` for producing response `Q` at a defect of depth `d` is determined by the exact superlevel-disk geometry of the Blaschke kernel. Writing `x=sqrt(M/(pi B d^2))`, the capacity relation is

`Q/(pi B d^2)=x^2 arsinh(1/x)+sqrt(1+x^2)-1`.

Equivalently the extremizer is positive density `B` on one kernel superlevel disk. In particular

`Q^2/(4 pi B d^2) <= M_B(d,Q) <= (Q+pi B d^2)^2/(4 pi B d^2)`,

so for fixed `B,Q`, `M_B(d,Q) ~ Q^2/(4 pi B)d^(-2)` as `d->0`. Signed or complex coefficients cannot improve the optimum. Thus the earlier `1/(B d^2)` tariff is not merely order-sharp: its leading shallow-depth constant and full one-target capacity are fixed by the half-plane Green geometry.

WI-418 shows that this one-target cost is **not additive in raw shallow-factor multiplicity**. Several shallow Blaschke factors aimed at the same target angular pocket can share the same source harmonic support, and the cluster is controlled by a single target attenuation cost rather than the sum of the individual one-zero costs. Consequently a bounded source budget does not by itself bound the number of shallow factors. Any multiplicity theorem must first force enough target-pocket or source-resolution separation that the relevant costs become additive or near-additive, or use a different invariant that is intrinsically sensitive to clustered multiplicity.

The live Blaschke route is therefore a **source-regularity, separation and budget-reuse problem**. Continuum-uniform count coercivity costs `T/delta`; unconstrained discrete oracle targeting costs zero; a non-oracular `L^infinity` density cap gives an exact one-target capacity with quadratic shallow-depth growth; but WI-418 shows that even this local tariff can be reused by a same-target cluster. A viable defect-to-zero bootstrap must derive admissible non-oracular regularity from independent arithmetic/source data and then prove a quantitative separation/packing theorem that limits such reuse across the actual defect configuration, or leave the linear translated-Blaschke architecture entirely.

## Keep budget, margin, defect response and representation dimension distinct

A candidate inertia mechanism must state whether it changes the source budget, reference spectral margin, individual defect response, collective zero density, height-sampling resolution, horizontal-depth coverage, endpoint-amplitude precision, cross-height weight, summability/renormalization law, moment determinacy, probe-placement regularity, cluster separation or genuinely adds independent information. Matrix enlargement, finer sampling, scalar-profile inversion, critical height weighting, analytic continuation, exponent differentiation, vertical translation, scale mixing and source-density regularization affect different entries in that ledger. WI-414--WI-418 sharpen the last distinction: global one-sided scale coercivity still pays Haar-rate local density; finite-window count coercivity pays `T/delta`; passing to a discrete set without non-oracular regularity destroys every TV lower bound; bounded two-dimensional probe density restores an exact one-target capacity asymptotic to `Q^2/(4 pi B d^2)`; and same-target clusters can still reuse that cost. None of these by itself supplies the arithmetic theorem that makes regularity and separation source-forced or turns individual coercivity into a global RH exclusion.