---
id: CLUE-prime-flute-positive-width-transition-schur-complement
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-342-sharp-physical-cutoff-forces-order-one-direct-angle-correlation.md
  - research/prime_flute/findings/PF-343-uniformly-small-physical-hard-sector-gaps-force-order-one-direct-angle-correlation.md
  - research/prime_flute/findings/PF-344-positive-width-transition-shorting-removes-the-leading-corridor-cost.md
  - research/prime_flute/findings/PF-345-growing-exterior-edge-strips-have-exponentially-small-shorted-trace.md
  - research/prime_flute/findings/PF-346-corridor-gram-shorting-preserves-correlations-but-is-unstable-to-subleading-energy.md
  - research/prime_flute/findings/PF-347-natural-seam-energy-cannot-regularize-the-bounded-band-corridor-gram-model.md
  - research/prime_flute/findings/PF-348-narrow-transition-shorting-preserves-the-local-dirichlet-pant-angle.md
  - research/prime_flute/findings/PF-349-local-full-parity-transition-shorting-retains-the-narrow-band-angle.md
  - research/prime_flute/findings/PF-350-collective-antisymmetric-transition-relaxation-is-uniformly-form-small.md
  - research/prime_flute/findings/PF-351-mismatched-transition-nodes-can-erase-the-coupled-corridor-model-angle.md
  - research/prime_flute/findings/PF-354-prime-cuff-lengths-are-rationally-independent-and-have-no-common-nonzero-frequency.md
  - research/prime_flute/findings/PF-355-one-complete-constant-fibre-retains-corridor-correlation-on-unequal-lattices.md
  - research/prime_flute/findings/PF-356-degenerating-network-metrics-concentrate-the-constant-fibre-angle-in-one-direction.md
  - research/prime_flute/findings/PF-357-network-conditioning-bounds-every-constant-fibre-correlation-defect.md
  - research/prime_flute/findings/PF-358-nearest-neighbor-factorization-preserves-half-the-constant-fibre-correlations.md
  - research/prime_flute/findings/PF-359-infinite-corridor-transition-shorting-has-essential-angle-norm-one.md
  - research/prime_flute/findings/PF-360-removing-or-shorting-constants-does-not-compactify-the-corridor-angle.md
  - research/prime_flute/findings/PF-361-finite-corridor-windows-preserve-the-narrow-band-model-angle.md
  - research/prime_flute/findings/PF-362-normal-ray-transport-has-a-nonvanishing-corridor-end-cost.md
  - research/prime_flute/findings/PF-363-trace-preserving-corridor-charts-give-a-coupled-pant-energy-lower-bound.md
  - research/prime_flute/findings/PF-364-narrow-transition-shorting-has-essential-angle-one-in-the-actual-seam-energy.md
  - research/prime_flute/findings/PF-365-removing-or-shorting-constants-leaves-essential-angle-one-in-the-actual-seam-energy.md
  - research/prime_flute/findings/PF-366-shorting-a-small-positive-width-low-band-leaves-essential-angle-one.md
  - research/prime_flute/findings/PF-367-exact-cuff-lattice-packets-obstruct-broad-band-corridor-comparison.md
---

# Can a positive-width transition band absorb the collapsing-corridor mode after exact Schur elimination?

## Observation

PF-342 shows that the canonical sharp fixed physical \`L/H\` split has order-one low/high canonical correlation. PF-343 strengthens the mechanism: the direct hard-sector angle is still noncompact whenever opposite sectors contain bounded physical Fourier modes separated by at most one sufficiently small fixed physical distance.

Therefore moving the hard cutoff or inserting only a narrow direct gap does not address the obstruction. The first representation change not covered by the argument is a genuine three-sector decomposition

\[
\mathcal H=L\oplus T\oplus H
\]

in which the transition band \`T\` has a physical width bounded below independently of the cuff period and is **retained in the full positive boundary form** before being eliminated.

Schur-complement realizations of Dirichlet-to-Neumann operators are classical. PF-344 proves that exact positive shorting cancels the leading raw corridor-scale matrix element on bounded edge witnesses. Its strengthened binomial compensation (equation (27)) gives a relative (O(e^{-\gamma L_n})) edge rate, while individual arbitrary bounded-frequency cosine modes still have only the qualitative (o(D_n)) result. PF-345 extends the relative exponential upper bound to two positive-width exterior edge strips of dimension Θ(L_n), with a positive-compression trace estimate. The surviving issue is the **diagonally normalized** effective angle and its global singular-value scale.

## Research question

Let

\[
M_n=Q_n+\Lambda_{E,n}>0
\]

be the raw completed positive boundary form on one tail module. Choose bounded physical cutoffs

\[
0<\kappa_-<\kappa_+
\]

with fixed separation \`\eta=\kappa_+-\kappa_->0\`, and decompose Fourier modes into

\[
L_n=\{|\xi|\le\kappa_-\},
\qquad
T_n=\{\kappa_-<|\xi|<\kappa_+\},
\qquad
H_n=\{|\xi|\ge\kappa_+\}.
\]

Form the exact positive shorted/Schur-complement form on \`L_n\oplus H_n\`,

\[
M_n^{/T}
=
M_{LH,LH}
-
M_{LH,T}M_{TT}^{-1}M_{T,LH},
\]

with the appropriate quadratic-form interpretation if an inverse must be taken on the supported transition range.

After normalizing by the \`L\` and \`H\` diagonal blocks of \`M_n^{/T}\`, does the resulting effective low/high canonical-correlation operator become compact, Hilbert--Schmidt, or weak trace class at the scale needed by the Prime-Flute endpoint?

Equivalently: **does the fixed-width transition band absorb the leading collapsing-corridor response, or does an order-one canonical correlation survive the Schur complement?**

## Why it may matter

PF-343 removes cosmetic versions of cutoff smoothing. A positive answer here would be the first direct-angle representation in which low and high are genuinely separated at finite physical scale while all intermediate boundary degrees of freedom are still accounted for exactly.

A negative answer would close a much larger family of completed-angle architectures: not only hard binary cutoffs, but also the natural finite-width transition-band repair suggested by PF-342/PF-343.

The test is also structurally clean. It asks whether the leading thin-corridor response is carried by a transition subspace that can be shorted out, rather than asking for another absolute estimate on the same obstructed binary angle.

## Decisive test

PF-344 settles the first raw-corridor-scale obstruction, but not the completed endpoint. In strictly positive canonical finite sections, form the exact three-sector positive shorted precision

\[
\widehat M_{LH}
=M_{LH}-M_{LT}M_{TT}^{-1}M_{TH}
\]

with a fixed positive-width physical transition sector. PF-344 supplies the actual bound that its bounded-frequency *matrix entries* are \(o(D_n)\), and the strengthened edge rate \(O(D_n e^{-\gamma L_n})\) from growing binomial compensators, by explicit variational trials. Do not ask for the same raw leading-order cancellation again or reinterpret it as normalized angle decay.

Now determine the shorted diagonal energies \(\widehat M_{LL},\widehat M_{HH}\) on these witnesses and estimate

\[
\widehat Z_{LH}
=
\widehat M_{LL}^{-1/2}
\widehat M_{LH}
\widehat M_{HH}^{-1/2}
\]

in the actual finite-section spectral currency. A lower bound on the normalized correlation along infinitely many separated modules would refute this architecture. A positive endpoint requires quantitative decay after normalization, control of all high frequencies, and the PF-318/PF-320 weak-trace reassembly, not merely small unnormalized entries.

PF-346 supplies an exact control for this test. The weighted cosine Gram matrix in PF-344 is diagonally scaled Cauchy, and its transition Schur complement is another diagonal congruence of the retained Gram block. Hence **all its retained low/high canonical correlations survive shorting**, despite exponentially small raw residual energies. Yet a positive `o(D_n)` perturbation of that raw model can make the residual correlation vanish. This rules out deciding the actual angle from the weighted leading kernel and raw-scale error alone; it does not decide the flute operator.

The approximation-cost gate remains the tradeoff in PF-344's trial bound

\[
D_n\left\|f+\sum_j a_j\cos(\xi_j\cdot)\right\|_
{L^2(\operatorname{sech}t\,dt)}^2
+C\left(1+\sum_j|a_j|\right)^2.
\]

PF-344 controls the coefficient tradeoff at the two edges; PF-345's negative-binomial extrapolator controls a **positive physical-width strip** at each edge and obtains a relative exponential trace bound on its positive compressed shorted form. Arbitrary bounded exterior packets still lack a uniform coefficient-cost bound. Obtain two-sided bounds on the shorted diagonal energies and the normalized mixed response (including beyond-strip modes), then either prove a small completed angle or construct a surviving normalized witness. Keep the full growing transition block, not a fixed-rank surrogate.

In particular, quantify the nonsingular pant/seam terms and intermodule elimination **relative to the shorted diagonal energies**. PF-346 (18)–(19) gives a sufficient residual-scale comparison for transferring its model witness; that comparison is unproved. A positive compactness route must instead establish how the actual remainder changes the normalized model correlation, while retaining uniform global finite-section control.

PF-347 rules out the natural **symmetric seam term alone** as the regularizer of the bounded-band Gram model. Full-period Fourier coercivity and the exact cuff law give `0<=Q_J<=epsilon_n D_n G_n`, with `epsilon_n=O_K(P_n^(-19/40))`. The same relative sandwich survives elimination of the whole growing transition band, so the model's normalized edge correlation has the same positive limit after adding `Q_J`. The remaining comparison must use the other pant terms or global transition couplings; replacing them by this seam block is insufficient. The full-period Gram lower bound is not an actual pant lower bound.

PF-348 proves a two-sided comparison for the **actual local Dirichlet module** on a sufficiently narrow fixed positive-width band. A Cauchy inverse estimate gives a conditioning exponent tending to zero with the band width, so the finite-corridor truncation and nonsingular pant trial cost are controlled relative to the entire growing-band Gram form. Exact local shorting then leaves edge correlation at least `1/2` on the tail. This includes the actual pant remainder, but holds with all other cuff traces fixed at zero and relaxation restricted to the local symmetric cosine channel. The remaining test must quantify the additional parity and intermodule transition relaxation; the local Dirichlet lower bound does not survive that enlargement automatically.

PF-349 settles the local parity enlargement for sufficiently narrow fixed width: the actual antisymmetric seam penalty and whole-band pant trace bound give a relative sandwich with loss `b_n/(1+b_n)`, where `b_n<=C eta+o(1)`, even after symmetric transition elimination. Tangential reflection also decouples every sine transition mode. The full local transition shorting therefore retains correlation at least `1/4`. All other cuffs are still fixed to zero. The unresolved narrow-band test is now **intermodule** transition relaxation; a different global answer cannot be attributed just to restoring local parity variables.

PF-350 controls **collective** antisymmetric transition relaxation across any coupled tail finite section: positive pant assembly gives `C<=2 direct-sum C_nn`, and the actual seam penalty gives `C<=b Q_-`, with `b<=C_kappa eta+epsilon_m` and `epsilon_m -> 0` independently of section size. Hence `(1+b)^(-1) S_sym <= S_full <= S_sym` even after all symmetric transition modes are shorted. Both forms already allow neighboring symmetric transition data. The decisive narrow-band question can therefore be attacked in the global symmetric face sector; a normalized witness larger than `b/(1+b)` transfers to full parity. PF-349's local Dirichlet witness does not establish that global symmetric witness, and a fixed form comparison does not transfer compactness.

PF-351 shows that scalar Cauchy invariance does not settle this global symmetric test. A positive two-module difference-energy model using the exact cosine Gram kernel has zero shorted edge correlation at an explicit coupling-to-grounding ratio when neighboring transition sets differ by one node. Arbitrarily many common transition modes preserve that cancellation. The local Dirichlet correlation can approach one in arbitrarily narrow bands, but the required grounding ratios then shrink at fourth order in band width. This is a control with tunable nodes and conductances, not an actual flute realization. A global obstruction must use the actual lattice/grounding relationship or another geometric estimate that excludes this relaxation mechanism; a compactness argument must still control all retained modes.

## Evidence boundary

PF-344 proves a **partial positive** result: a fixed positive physical transition band removes the raw \(D_n\)-scale edge correlation after exact positive Schur shorting; all individual bounded-frequency cosine matrix entries are \(o(D_n)\). These are variational upper bounds on the unnormalized shorted form, not a claim about its normalized low/high canonical-correlation angle.

PF-345 strengthens the relative unnormalized control to a growing-rank edge-strip compression, but no spectral bound **after division by the shorted diagonal energies**, no uniform approximation-conditioning rate **for the whole exterior band**, no control of the unbounded high sector, and no compactness or weak-\(\mathcal S_1\) endpoint is established. General DtN/Schur theory and weighted-exponential completeness are classical; neither supplies these missing quantitative Prime-Flute estimates.

PF-346's exact correlation preservation and instability control concern the corridor **Gram model only**. PF-344's one-sided geometric trial estimate does not supply a two-sided comparison at the much smaller shorted scale. The model is therefore neither proof nor refutation of the actual transition-band architecture.

## Research disposition

Status: accepted. PF-344 removes the raw \(D_n\) term on bounded edge witnesses, and PF-345 extends relative exponential suppression to two physically positive-width edge strips of dimension \(\Theta(L_n)\) in the positive unnormalized shorted compression. The clue remains active for the materially different question of the **completed, diagonally normalized and globally reassembled** effective low/high angle. Its decisive test is now a **beyond-strip** approximation-cost/conditioning estimate **together with two-sided diagonal normalization**, or a normalized counter-witness. See [[research/prime_flute/findings/PF-344-positive-width-transition-shorting-removes-the-leading-corridor-cost.md]] and [[research/prime_flute/findings/PF-345-growing-exterior-edge-strips-have-exponentially-small-shorted-trace.md]].

[[research/prime_flute/findings/PF-346-corridor-gram-shorting-preserves-correlations-but-is-unstable-to-subleading-energy.md]] sharpens the required comparison: the leading corridor Gram model retains its normalized correlations, and `o(D_n)` raw error is insufficient to transfer that answer. The remaining actual-PDE question must control the remainder at the residual-energy scale or demonstrate its effect on the normalized angle directly. The clue stays accepted and unresolved.

[[research/prime_flute/findings/PF-347-natural-seam-energy-cannot-regularize-the-bounded-band-corridor-gram-model.md]] excludes one concrete repair of that model: the actual bounded-frequency symmetric seam energy is relatively form-small even before shorting and therefore cannot erase its normalized witness. This narrows the residual question to the remaining geometric and global terms; it does not resolve the actual-PDE clue.

[[research/prime_flute/findings/PF-348-narrow-transition-shorting-preserves-the-local-dirichlet-pant-angle.md]] rules out the sufficiently narrow **local Dirichlet, symmetric-cosine** transition repair using the actual two-pant form. It leaves the clue accepted and unresolved for full parity/global transition shorting: a positive local correlation is not monotone under further relaxation, as its explicit finite control shows.

[[research/prime_flute/findings/PF-349-local-full-parity-transition-shorting-retains-the-narrow-band-angle.md]] extends that local obstruction to both face parities and the full sine/cosine transition sector. The clue remains accepted and unresolved for intermodule relaxation, wider fixed bands, and the globally completed angle; the new relative bound does not cross that boundary.

[[research/prime_flute/findings/PF-350-collective-antisymmetric-transition-relaxation-is-uniformly-form-small.md]] narrows the intermodule test to symmetric transition propagation by controlling all antisymmetric transition freedoms uniformly over coupled tail sections. The clue remains accepted and unresolved: the global symmetric correlation, infinite-section passage and completed operator ideal are still unproved.

[[research/prime_flute/findings/PF-351-mismatched-transition-nodes-can-erase-the-coupled-corridor-model-angle.md]] supplies an exact coupled-corridor countercontrol to transferring the local scalar Cauchy invariant by positivity and adjacency alone. The clue remains accepted and unresolved for the actual geometry, its complete transition lattices and the normalized global operator.

[[research/prime_flute/findings/PF-354-prime-cuff-lengths-are-rationally-independent-and-have-no-common-nonzero-frequency.md]] proves that distinct actual prime cuffs have rationally independent lengths and share no nonzero physical Fourier frequency. Thus PF-353's exact complete common-frequency obstruction for the PF-352 model cannot be transplanted to those cuffs. Near-common modes remain possible at the lattice-spacing scale; they need a stability estimate after shorted diagonal normalization. The same exact independence holds for pairwise coprime odd composite labels, so it is not a primality selector. The clue remains accepted and unresolved for the actual global normalized angle.

[[research/prime_flute/findings/PF-355-one-complete-constant-fibre-retains-corridor-correlation-on-unequal-lattices.md]] removes the shared-nonzero-frequency requirement for the **whole retained-constant angle of the coupled corridor model**. After arbitrary mismatched transition shorting, all module constants together have correlation `2 sqrt(cosh(pi xi))/(1+cosh(pi xi))` with any single retained high mode of frequency `xi`. A residual determinant identity forces the model angle norm towards one when a bounded high strip contains a diverging number of modes per module. These witnesses use exact unequal lattices, including prime-cuff lattices, but can spread over all module constants. The clue remains accepted and unresolved for the actual pant/seam form, a mean-zero split, residual-scale comparison, localization and infinite-operator singular-value counting. Frequency mismatch alone no longer supplies a whole-model escape from the retained-constant witness.

[[research/prime_flute/findings/PF-356-degenerating-network-metrics-concentrate-the-constant-fibre-angle-in-one-direction.md]] makes the constant-fibre multiplicity limitation sharp for arbitrary positive network matrices. With globally distinct nonzero nodes and `K_tau=vv^T+tau I`, the first constant/high-strip correlation tends to the exact determinant-deficit limit while all later correlations are `O(sqrt(tau))`. Complete unequal bands and growing module counts allow the angle norm to approach one with only one singular value above any fixed threshold. The growing-dimensional coupling is dense, not the flute's nearest-neighbor matrix; the high strip is finite and the low witness retains only constants. Thus the clue remains accepted and unresolved: actual coupling locality, additional low modes, the unbounded high sector, and the residual-scale pant comparison can still change the answer.

[[research/prime_flute/findings/PF-357-network-conditioning-bounds-every-constant-fibre-correlation-defect.md]] quantifies the remaining finite-model multiplicity test. If `alpha D <= K <= beta D` for a positive diagonal spatial metric, each ordered squared correlation defect is within the factor `beta/alpha` of the corresponding ordered per-module high-node Cauchy product, uniformly in all transition sets. Complete high strips give products `exp(-gamma L_i+O(1))`; a grounded weighted path therefore retains all module-count many correlations tending to one when `(c_max/c_min)(d+1)^2 exp(-gamma L_min) -> 0`. Conversely, concentration to one direction requires exponential deterioration of every such comparison ratio. This narrows PF-356's freely degenerate control without excluding it. The clue remains accepted and unresolved for the actual pant/seam comparison, effective grounding and compatible infinite-section passage.

[[research/prime_flute/findings/PF-358-nearest-neighbor-factorization-preserves-half-the-constant-fibre-correlations.md]] removes the network-conditioning requirement for a sharp **half-module** count in the finite tridiagonal Cauchy model. Bidiagonal Cholesky factors pay only adjacent transition products; independent spatial parity directions and the high-mode residual then give `1-sigma_(ceil(d/2))^2 <= 2 max_i(Q_i P_i)/min_i(Q_i Q_(i+1))`, with the products defined in the finding. Complete bands force this bound to zero when `(delta+gamma)L_min-2 delta L_max -> +infinity`, independently of grounding, conductance contrast and section size. Nearly singular paired modules, with arbitrarily weak positive connecting links, show that the asymptotic fraction cannot be improved uniformly in this class. The clue remains accepted and unresolved: the actual pant/seam residual-scale comparison, additional low modes, reservoir attachments and compatible infinite-operator singular-value counting are not established.

[[research/prime_flute/findings/PF-359-infinite-corridor-transition-shorting-has-essential-angle-norm-one.md]] closes the compatible infinite-section question for the nearest-neighbor **Cauchy corridor model**. In the energy completion of finitely supported fields, edgewise scalar residual bounds survive elimination of the entire closed transition space. Constants on nonadjacent modules then force essential angle norm one whenever the per-module high product beats the neighboring transition products. Complete sufficiently narrow bands satisfy this criterion on the exact prime-cuff periods, for arbitrary positive corridor conductances. The clue remains accepted and unresolved for the actual surface: the globally shorted pant/seam comparison at residual scale and the identification of its completion remain unproved. The model result does not apply to a mean-zero split or establish an intrinsic spectral/RH consequence.

[[research/prime_flute/findings/PF-360-removing-or-shorting-constants-does-not-compactify-the-corridor-angle.md]] closes the **mean-zero and post-constant model escape**. The first nonzero cosine on each cuff replaces the shared constant fibre: independent spatial support permits an edgewise residual certificate with different low nodes, and the same narrow-band criterion gives essential angle norm one. Eliminating the entire constant sector is exactly angle-equivalent to excluding it, by the common scalar residual isometry in the completed network energy. Neither operation repairs the Cauchy model. The clue stays accepted and unresolved for the actual pant/seam form, its residual-scale comparison and completion, and wider bands outside the sufficient criterion; the new result does not identify a surface operator or establish an RH consequence.

[[research/prime_flute/findings/PF-361-finite-corridor-windows-preserve-the-narrow-band-model-angle.md]] removes **finite corridor truncation alone** as a model escape when the combined transition/high band is sufficiently narrow. Turán–Nazarov concentration gives a relative estimate on every combination from both unequal neighboring lattices, without frequency separation or coefficient conditioning; it survives the infinite transition infimum and preserves essential angle norm one for retained constants or first nonzero cosine carriers with constants absent. This concerns the straight-coordinate difference energy. The actual ray correspondence is nonlinear, and its transport, positive-shift mass and nonsingular pant/seam terms remain uncontrolled at the shorted scale. The clue stays accepted and unresolved for the actual surface; the result does not assert that shorting constants remains equivalent to excluding them after truncation.

[[research/prime_flute/findings/PF-362-normal-ray-transport-has-a-nonvanishing-corridor-end-cost.md]] rules out extending that comparison to normal-ray transport by a **universal relative bound using straight-coordinate difference energy alone**. Matching bounded-frequency waves have a positive limiting transverse transport cost at the growing corridor ends, even after small seam-offset trimming; distinct frequencies separated by `o(sqrt(s))` retain this cost while their straight difference energy vanishes. An additive derivative bound is available. These controls are not proved to occur on the actual prime Fourier lattices and do not determine the globally shorted angle. The clue stays accepted: the remaining comparison must retain the correspondence, pay its error with completed coercive energy, or supply an actual-lattice estimate excluding the control regime.

[[research/prime_flute/findings/PF-363-trace-preserving-corridor-charts-give-a-coupled-pant-energy-lower-bound.md]] supplies a **coupled actual-pant lower certificate** using a different foliation. Interpolating the two inverse hypercycle boundary maps across the logarithmic strip fixes both inherited cuff coordinates and costs only `O(s)` shear in the full energy metric. The chart fits inside a growing embedded corridor; narrow-band concentration then transfers the straight-coordinate Cauchy residual lower bound against every symmetric transition trial, including remote ones. This does not contradict PF-362: tangential and mass energy remain in the two-sided local comparison and can only be dropped for the lower bound. The clue stays accepted and unresolved for the matching actual upper trial at the shorted residual scale, other coupled freedoms, and the completed normalized angle.

[[research/prime_flute/findings/PF-364-narrow-transition-shorting-has-essential-angle-one-in-the-actual-seam-energy.md]] closes the **sufficiently narrow fixed-width, constant-retaining actual-angle repair**. A single-cuff least-squares compensator on a narrow transition-plus-high strip has coefficient exponent tending to zero with the combined width. The actual complete-pant trial then beats the coupled lower certificate when both `gamma>R delta` and `a+(1+R)delta<b_0`. The distance ratio tends to zero on infinite-dimensional sparse tail spans, survives all transition face parities, and survives restoring the finite head. Consequently the full transition-shorted angle has essential norm one in the actual seam-energy completion of finitely supported Fourier fields. This is no longer only a corridor-model conclusion.

[[research/prime_flute/findings/PF-365-removing-or-shorting-constants-leaves-essential-angle-one-in-the-actual-seam-energy.md]] also closes **constants fixed to zero and all module constants shorted** in that actual-energy setting. First nonzero cosines provide the retained low witnesses. Constant elimination costs `tanh^4(pi^2/L_i) ~ pi^8/L_i^4` in the lower residual; coefficient-controlled complete-pant trials and the extended collective antisymmetric estimate absorb that polynomial loss within the same strict margins. Both actual angles have essential norm one, without asserting the model's unitary equivalence for the surface. The clue remains accepted for **wider fixed bands outside these sufficient margins, elimination of a growing low sector, or a different observable**. Numerical optimal widths, other conditions at infinity, relative resolvent/scattering consequences and RH remain unproved. Retaining, excluding, or shorting constants does not reopen the sufficiently narrow-band test in these completions.

[[research/prime_flute/findings/PF-366-shorting-a-small-positive-width-low-band-leaves-essential-angle-one.md]] rules out a **small fixed positive-width low-band elimination** in addition to the sufficiently narrow transition band, in the actual energy completion. The extra low sector has linearly growing rank per cuff. Carriers near a fixed interior low frequency survive all remote low/transition relaxation; a two-cluster inverse-Gram estimate prices the quadratic cosine-node spacing at zero, and strict residual/coefficient margins again give essential angle norm one. Section 5a also rules out **every closed subspace of that band envelope**, including cuff-dependent subsets, individual face/parity selections and nonlocal mixtures, under the stronger first margin `gamma>(1+R)delta`. A high-only approximation and the full-envelope lower residual bound make the distance ratio uniform in the chosen eliminated subspace; normalized-angle monotonicity is not assumed. The clue remains accepted for wider eliminated bands outside these margins, materially different cutoffs/completions, or a different observable. Partial elimination inside the sufficiently small envelope does not repair compactness, but the stronger uniform conclusion is not asserted throughout the original larger margin range.

[[research/prime_flute/findings/PF-367-exact-cuff-lattice-packets-obstruct-broad-band-corridor-comparison.md]] restricts a possible wider-band extension of that proof. A binomial packet using consecutive exact cuff Fourier modes in a band of width `W` places its weighted mass at `|t|/L=arctan(W)/pi`. A shorter fixed-ratio window captures exponentially vanishing mass. Thus exact lattice membership does not justify the uniform full-line/window comparison for arbitrary broad bands; the conservative `19L/80` subwindow already fails when `W>tan(19pi/80)`. This does not establish failure on the larger actual embedded window or on the actual minimizing residual. The clue remains accepted: wider-band arguments must use the available window size, residual-specific structure or other completed energy terms rather than extrapolating the narrow-band scalar comparison.

For that same finding's actual embedded window, `T_i<=theta L_i` with fixed `theta<1/2` requires a neighboring prime-gap jump `b>=c P^(1-2theta) a^(2theta)` and has at most `O(X^(2theta))` occurrences below `P=X`. The actual ratio tends to `1/2` in prime-index density, so each fixed-width binomial packet has window mass tending to one in density. Pintz's unbounded gap-ratio theorem does not supply the needed power-scale subsequence. This narrows the packet's arithmetic realization test, while leaving rare subsequences, other band fields, minimizing residuals and the normalized angle unresolved; the clue remains accepted.
