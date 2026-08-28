# WI-001 — the first-two-moment bandwidth-one data have explicit extremizers

**Status:** `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for attempts that try to close the exceptional mass using only the existing first two trace moments, the on/off-line block partition, or a re-optimization of one admissible bandwidth-one window.

## 1. Verified baseline

Alpöge--Furman, arXiv:2608.13637v2, proves unconditionally that, as `T -> infinity`,

\[
N_0^s(T,2T)\ge \left(\frac23-o(1)\right)N(T,2T),
\qquad
N_d(T,2T)\ge \left(\frac56-o(1)\right)N(T,2T),
\]

where `N` counts nontrivial zeros with multiplicity, `N_0^s` counts simple zeros on `Re s=1/2`, and `N_d` counts distinct zeros. With the Montgomery--Taylor window,

\[
c_{\rm MT}^{-1}=\frac12+\frac1{\sqrt2}\cot\frac1{\sqrt2},
\]

the simple-on-line constant becomes

\[
2-c_{\rm MT}^{-1}=0.672500703679\ldots
\]

and the distinct-zero constant becomes

\[
\frac12(3-c_{\rm MT}^{-1})=0.836250351839\ldots .
\]

The theorem is explicitly unconditional: no mollifier, zero-density estimate, zero-free region, or RH assumption is used. The paper states the same theorem for every fixed primitive Dirichlet `L`-function. Anthropic's public `formal-math/zeta23` project contains a Lean 4 formalization of the headline statements.

The proof compresses Weil's Hermitian form to a real symmetric matrix `G` of dimension asymptotic to `N=N(T,2T)`. Up to a negligible tail,

\[
G=P+Q,
\]

where critical-line zeros contribute positive rank-one forms to `P`, while a functional-equation pair `\{\rho,1-\bar\rho\}` off the line contributes a pullback of a signature `(1,1)` block to `Q`. Thus the number of positive directions of `Q` is controlled by the number of off-line pairs.

The prime side supplies

\[
\operatorname{tr}G=(1+o(1))N,
\qquad
\|G\|_{\rm HS}^{2}=(R(\psi)+o(1))N.
\]

For the flat window `R=4/3`; for Montgomery--Taylor, `R=c_MT^{-1}`. The linear-algebra input is the rank--trace inequality

\[
\operatorname{rank}P_1
\ge
2\operatorname{tr}P_1+4\operatorname{tr}Q'-4b-\|P_1+Q'\|_{\rm HS}^{2},
\]

for `P_1 >= 0` and `n_+(Q') <= b`. After regrouping the simple on-line contribution onto the rank side, this yields

\[
N_0^s+o(N)
\ge
4\operatorname{tr}G-2N-\|G\|_{\rm HS}^{2}
=
(2-R(\psi)-o(1))N.
\]

This reconstruction matters because it identifies exactly which information is being consumed: the first trace moment, the Hilbert--Schmidt/second trace moment, the rank of the simple positive part, and the positive index budget of the rest.

## 2. The rank--trace step itself is sharp

The matrix inequality is not leaving an unexploited universal algebraic gap. Alpöge--Furman give the equality model

\[
P=\Pi_1,\qquad Q=2\Pi_2,
\]

for orthogonal projections `Pi_1`, `Pi_2` of the allowed ranks. Their proof reduces, after the optimal alignment step, to scalar inequalities with exact equality cases corresponding to `(x-1)^2`, `x^2`, and `(x-2)^2`.

More importantly, Section 7.2 proves sharpness at the zero-counting level. With only

- `tr G`,
- `||G||_HS^2`,
- the critical/off-critical block structure, and
- the bound of the simple critical contribution by its rank/trace,

the flat-window `2/3` simple-on-line and `5/6` distinct constants admit an explicit extremizer:

\[
\frac{2N}{3}\quad\text{mutually orthogonal simple critical-line zeros}
\]

together with

\[
\frac{N}{6}\quad\text{double critical-line points}.
\]

The latter account for `N/3` zeros when multiplicity is counted, so the total multiplicity is `N`. This configuration has

\[
\operatorname{tr}G=N,
\qquad
\|G\|_{\rm HS}^{2}=\frac43N,
\qquad
N_0^s=\frac23N,
\qquad
N_d=\frac56N.
\]

Therefore a stronger inequality using no information beyond these same aggregate quantities cannot improve the flat-window theorem: there is a genuine feasible equality configuration, not merely a loose proof estimate.

## 3. Multiple on-line zeros and shallow off-line pairs are degenerate at this resolution

The same section gives a more important obstruction for the second research direction. Replace the `N/6` double critical-line points above by `N/6` off-line functional-equation pairs whose horizontal depth tends to zero. Alpöge--Furman state that this is spectrally the same limiting extremal configuration for the simple-on-line certificate.

Hence, at the resolution of the current first-two-moment compression,

\[
\boxed{\text{on-line multiplicity} \quad\text{and}\quad \text{arbitrarily shallow off-line pairs}}
\]

can consume the same certificate budget.

This rules out an overly simple interpretation of the uncertified complement. Even if one found an argument excluding a positive density of genuinely off-line pairs, the present certificate could still be saturated by multiple zeros on the critical line. Conversely, a simplicity-only argument need not control shallow off-line pairs. The `1/3` complement is therefore not one defect variable.

A defect-to-zero mechanism must distinguish at least three effects:

1. multiplicity on the critical line;
2. horizontal displacement of off-line pairs;
3. slack/non-orthogonality introduced by the compression and certificate.

An observable that only counts negative or positive inertia does not by itself separate the first two.

## 4. Re-optimizing one bandwidth-one window is exhausted

For certificates of the exact form

\[
2-R(\psi),
\]

the Montgomery--Taylor window is already optimal; Alpöge--Furman cite the extremal Hilbert-space result of Carneiro--Chandee--Littmann--Milinovich for this optimization. Thus merely searching for a better single admissible window cannot improve `0.672500703679...` within that certificate class.

The paper also studies a substantially broader class: configuration-wise certificates that depend only on the first two trace moments against Fourier-support-`[-1,1]` test functions together with the on-line/off-line partition. It constructs an explicit finite periodic adversarial law and reports the ceiling

\[
p_0\le 0.6818287.
\]

For sufficiently regular band-limited windows the corresponding stability bound remains below `0.6819`. This numerical ceiling is a useful method barrier, but its epistemic status must be stated precisely: the finite-law analytic implication is formalized, while the `EnclOK` numerical enclosures are certified by interval arithmetic outside the Lean kernel. The main `2/3` and Montgomery--Taylor theorems do not depend on that numerical certification.

The conclusion is stronger than “the current kernel may be nonoptimal”: **all first-two-moment, bandwidth-one certificates in the stated class are separated from density one by a large gap.** Even perfect optimization of that information cannot prove RH or even certify `90%` simple critical zeros.

## 5. Higher moments expose the actual arithmetic wall

A natural response is to add `tr G^3`, `tr G^4`, and higher spectral moments. Alpöge--Furman identify why these are not free improvements. At the present bandwidth `X \asymp T`, the diagonal prime-side method lies at the edge of the Rudnick--Sarnak support range; moments beyond those already used require new additive correlations of prime powers. The paper summarizes this as: unconditionally, higher moments add no new usable information in the same regime.

This is not a linear-algebra obstruction. It is an arithmetic one. Their conditional model makes the distinction explicit. Under a Hardy--Littlewood-type hypothesis giving the first four limiting trace moments,

\[
1,\quad \frac43,\quad 2,\quad \frac{13}{4},
\]

the Christoffel-function certificate gives

\[
\liminf\frac{N_0^s(T,2T)}{N(T,2T)}\ge \frac{13}{18}\approx0.7222.
\]

If the required hierarchy of moments were available to all orders, the same moment method could drive the certified density to `1`. Separately, Goldston--Lee--Schettler--Suriajaya show that the full pair-correlation conjecture, without assuming RH, implies that asymptotically `100%` of the zeros are both simple and on the critical line.

So a conditional defect-to-zero mechanism is already known: sufficiently rich correlation information resolves both vertical multiplicity and horizontal displacement. What is missing is an unconditional route to comparable information.

## 6. Consequence for the Weil-inertia program

The first substantive search region can now be narrowed sharply.

The following routes are closed as stand-alone ways to remove the exceptional mass:

- replacing the rank--trace lemma by a universally stronger inequality while feeding it only the same trace, Hilbert--Schmidt norm, and block-count data;
- optimizing a single bandwidth-one window within `2-R(psi)`;
- treating the uncertified complement as if it were solely negative inertia/off-line zeros;
- asking higher spectral moments to improve the theorem without also supplying new prime-correlation information needed to evaluate them.

The surviving routes must add information not present in the extremal models above. Plausible categories are:

- unconditional arithmetic information beyond Fourier support `1` or beyond the current prime-pair diagonal control;
- a new observable accessible from the explicit formula that distinguishes horizontal depth from on-line multiplicity rather than collapsing both into one charge;
- a zeta-specific structural constraint, independent of the first two moments, that proves the explicit equality/near-equality configurations cannot occur;
- a combination of several admissible local certificates whose joint constraints contain information not reducible to one global first-two-moment pair.

The last category is especially concrete because a contemporaneous preprint directly claims such an improvement.

## 7. Current direct-improvement claim is a precise audit target, not yet evidence

Michael Devine's Zenodo preprint, version 1.0.3 dated 23 Aug 2026, claims

\[
\liminf_{T\to\infty}\frac{N_0^s(T,2T)}{N(T,2T)}\ge 0.673399
\]

unconditionally, using four admissible bandlimited profiles, several nonnegative pair-interaction rows, a rational piecewise-linear certificate, and interval-arithmetic verification. The claimed value is strictly above the single-window Montgomery--Taylor constant but comfortably below the broader `~0.6818` bandwidth-one ceiling, so the headline is not in logical conflict with Alpöge--Furman's barrier.

This pass verified only the public deposit metadata, not the mathematical proof or its computational certificate. The claim is therefore `NEEDS-AUDIT` and is **not** used as an established improvement in this finding. A decisive audit would have to verify, at minimum:

1. that every profile and pair-interaction observable has an unconditional prime-side evaluation at the asserted support;
2. that no positivity step silently assumes the zeros are on, or uniformly close to, the critical line;
3. that the finite-domain interval enclosures cover all transition, reset, endpoint, and tail cases without gaps;
4. that the joint multi-profile certificate is genuinely stronger than a single `2-R(psi)` certificate while remaining within the legal unconditional information budget;
5. that its public artifact reproduces the stated rational lower bound independently.

If it survives those checks, it would be a small but genuine example of the fourth surviving route above and would immediately supersede `0.672500703679...` as the unconditional constant. Until then, the verified Alpöge--Furman theorem remains the evidence baseline for this line.

## 8. Prior-art and novelty assessment

No novelty is claimed here for the Alpöge--Furman theorem, its sharpness examples, the Montgomery--Taylor optimization, the Rudnick--Sarnak support barrier, or the conditional pair-correlation implications. Those are literature results.

The Mathia-specific contribution of this finding is the research-scope classification obtained by putting them together:

\[
\boxed{\text{the main obstruction is not “prove negative inertia is zero”; it is “add an observable that breaks the multiplicity/depth extremal degeneracy”.}}
\]

That statement materially changes the search. The explicit extremizers prove that the first two moments cannot tell which kind of exceptional zero consumed the missing certificate mass, while the full-support pair-correlation result shows what sufficiently rich information would look like. Any proposed bootstrap should therefore be tested first against both extremal families: on-line doubles and shallow off-line pairs. A mechanism that does not separate them cannot, by itself, drive the simple-critical proportion to one.