# WI-037 — MRT does not close the welding glue from divisor-boundedness alone

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + DECISIVE-NEGATIVE + NEEDS-AUDIT`. This finding does **not** disprove the Yang--Yang one-sided fourth-moment route, and it does not change Mathia's current unconditional simple-critical proportion. It closes a narrower shortcut that remained implicit after WI-034--WI-035: the public claim that the welding/glue layer is discharged on the minor arcs by “the divisor-bounded envelopes of [MRT, Prop. 5.4, App. A]” is not a consequence of the cited primary theorem. Matomäki--Radziwiłł--Tao Proposition 5.4 is a specific mean-value theorem for `f = Lambda 1_(X,2X]` or `f = d_k 1_(X,2X]`; its proof uses highly structured Type `d_j` / Type II Dirichlet-convolution decompositions with length restrictions. Appendix A proves their separate Proposition 5.5, again for those same source functions. Neither result states a generic minor-arc theorem stable under multiplication by an arbitrary divisor-bounded welding coefficient.

More strongly, no such theorem can follow from divisor-boundedness alone: a `1`-bounded coefficient can be chosen to cancel any prescribed minor-arc phase exactly. Therefore the Yang welding step needs an additional structural lemma showing that its specific prime-pair weight belongs to a class for which the MRT/Vaughan cancellation survives, or an independent estimate for that weighted exponential sum. The public reproduction tree does not contain the cited rounds-38--40 archive as a standalone proof source, so this interface remains a genuine evidence gate rather than a citation-level detail.

## 1. The exact public source claim

The pinned Yang--Yang source is

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`.

In `paper.tex`, subsection `Covered zone, middle band, bridge and aggregation`, after the exact dispersion-swap, bridge, and structured-to-full statements, the source writes that the band consumer uses a single Cauchy--Schwarz in the shift variable and then says

\[
w_k(n)=\sum_{m\in I(n)}\Lambda(m)\Lambda(m-rk)
\tag{1}
\]

is the welding weight. It states that the glue layer closes by

1. exact factorization of main terms;
2. Abel summation against the glue on the major arcs; and
3. “the divisor-bounded envelopes of [MRT, Prop. 5.4, App. A] for the minor arcs.”

The same section says that four two-modulus lemmas live in an archive from rounds 38--40. A recursive inventory of the pinned public reproduction repository finds no such archive as a standalone proof artifact. This finding therefore audits the printed citation itself rather than treating an unavailable archive as evidence.

Pinned source:

- https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/paper.tex

The candidate is explicitly graded by its authors as `certified-candidate`; the analytic layer is unformalized and has no external review. Nothing here changes that grading.

## 2. What MRT Proposition 5.4 actually says

The primary source is

Kaisa Matomäki, Maksym Radziwiłł and Terence Tao, *Correlations of the von Mangoldt and higher divisor functions I. Long shift ranges*, Proc. London Math. Soc. 118 (2019), 284--350, arXiv:1707.01315.

Their Proposition 5.4 is a mean-value estimate with

\[
H=X^{8/33+\varepsilon},\qquad Q=\log^B X,
\tag{2}
\]

and `q=q_0q_1 <= Q`, for a scale parameter satisfying

\[
X^{-1/6-\varepsilon}\le\lambda\ll\frac1{qQ}.
\tag{3}
\]

Crucially, the function entering the proposition is not an arbitrary divisor-bounded sequence. It is explicitly restricted to

\[
\boxed{
f=\Lambda\,1_{(X,2X]}
\quad\text{or}\quad
f=d_k\,1_{(X,2X]}.
}
\tag{4}
\]

The proposition controls a character/Dirichlet-polynomial mean value of this `f` with an arbitrary logarithmic saving. The proof begins by applying a combinatorial decomposition to (4). The resulting pieces have one of the following special forms:

\[
\widetilde f
=(\alpha*\beta_1*\cdots*\beta_j)1_{(X/q_0,2X/q_0]},
\qquad j\le4,
\tag{5}
\]

where `alpha` is divisor-bounded but each `beta_i` is an interval indicator or a logarithm times an interval indicator and the factor lengths obey explicit lower/upper constraints; or a Type II convolution

\[
\widetilde f=(\alpha*\beta)1_{(X/q_0,2X/q_0]}
\tag{6}
\]

with both coefficients divisor-bounded **and** with explicit support-length conditions. Thus “divisor-bounded” is one hypothesis inside a rigid convolution architecture, not the theorem's interface.

Primary source:

- https://arxiv.org/abs/1707.01315
- https://www.math.mcgill.ca/radziwill/correlations.pdf

In the published pagination, Proposition 5.4 is on pp. 52--53. Its proof and the Type `d_j` / Type II reduction continue through the subsequent sections.

## 3. Appendix A is not a generic divisor-bounded extension

There is a second provenance mismatch in the short citation “Prop. 5.4, App. A”. MRT Appendix A begins explicitly:

> In this section we prove Proposition 5.5.

Proposition 5.5 again assumes

\[
f=\Lambda\,1_{(X,2X]}
\quad\text{or}\quad
f=d_k\,1_{(X,2X]},
\tag{7}
\]

then decomposes those functions into Type `d_1`, Type `d_2`, Type II, and small pieces. The appendix does not state that an arbitrary divisor-bounded external weight may be inserted into the minor-arc exponential sum while preserving the logarithmic saving.

Accordingly, the strongest primary-source-backed reading is

\[
\boxed{
\text{MRT supplies cancellation for specific structured arithmetic functions,}
}
\tag{8}
\]

not

\[
\boxed{
\text{MRT supplies cancellation for every divisor-bounded coefficient.}
}
\tag{9}
\]

This distinction is load-bearing for the welding step because (1) is a new coefficient depending on a second prime correlation and on the moving interval `I(n)`.

## 4. Exact no-go: divisor-boundedness alone can never preserve a minor-arc saving

The missing hypothesis is not a technical luxury. There is an elementary obstruction to any statement of the form

\[
|a_n|\ll \tau_C(n)(\log X)^C
\quad\Longrightarrow\quad
\left|\sum_{n\sim Y}a_ne(\gamma n)\right|
\ll_A Y(\log Y)^{-A}
\tag{10}
\]

for every minor-arc `gamma`.

Fix any real `gamma`, minor or otherwise, and take

\[
a_n=e(-\gamma n).
\tag{11}
\]

Then `|a_n|=1`, so `a_n` is stronger than divisor-bounded, while

\[
\boxed{
\sum_{n\sim Y}a_ne(\gamma n)=\sum_{n\sim Y}1=Y+O(1).
}
\tag{12}
\]

Hence no logarithmic or power saving can be deduced from pointwise divisor-boundedness by itself. Any valid glue theorem must use **structural decorrelation** between the welding coefficient and the additive phase: convolution structure, Fourier information, bounded-variation/smooth dependence allowing summation by parts against an already-controlled primitive, an averaged correlation theorem, or another explicit invariant.

Equation (12) is the decisive negative result of this finding. It rules out “divisor-bounded envelope” as a standalone information carrier for minor-arc cancellation, independently of the numerical parameters of the Yang construction.

## 5. Why the printed major-arc argument does not automatically repair the minor arcs

The source separately invokes Abel summation against the welding weight on major arcs. That can be valid if the major-arc main term is sufficiently explicit and the cumulative glue is controlled, but it does not imply (10) on minor arcs.

For the minor arcs one would need, for the **specific** weight (1), a statement of one of the following kinds:

1. a decomposition of `w_k(n)` (or the exact coefficient into which it is inserted) into finitely many MRT-admissible Type `d_j` / Type II pieces with all support and scale inequalities checked;
2. a uniform bound for partial sums of `w_k(n)` strong enough that Abel summation may be applied to the minor-arc prime sum as well;
3. a bilinear/dispersion identity reducing the weighted minor-arc expression to an MRT theorem already proved for `Lambda` correlations, with no second Cauchy--Schwarz that reintroduces the Poisson floor which the source explicitly says is unaffordable;
4. a new weighted version of the MRT mean-value estimate whose hypotheses are verified by (1).

The public text does not provide any of these. In particular, calling (1) a “welding weight” and observing an upper envelope does not place it in the convolution classes (5)--(6).

This does **not** show that such a lemma is false. It shows that it is an independent theorem obligation and that the cited primary source does not discharge it.

## 6. Relation to WI-034 and WI-035

WI-034 verified a different interface: MRT Theorem 1.3(i), although stated as an almost-all-shifts theorem, implies the unweighted hard-window `L^2` shifted-prime variance used by the one-sided route, and the structured multiplicity `nu(h)<=tau(h)` preserves an arbitrary logarithmic saving.

WI-035 then removed the apparent two-modulus novelty on the major-arc side by exact denominator contraction, while explicitly leaving the smoothing-collar and welding/glue interfaces open.

The present finding narrows the latter gate:

\[
\boxed{
\text{unweighted MRT variance}
\;\not\Rightarrow\;
\text{welding-weighted minor-arc cancellation}
\quad\text{from divisor-boundedness alone.}
}
\tag{13}
\]

Thus WI-034 remains valid, and WI-035's denominator-contraction result remains valid. What fails is the hope that the last glue step is a routine corollary of the already-audited MRT input merely because its auxiliary coefficients have a divisor-type envelope.

## 7. Consequence for the one-sided fourth-moment program

WI-028 showed that the arithmetic target needed for a strict improvement is comparatively weak. WI-030--WI-033 then removed several deterministic/numerical gaps: the continuum core is exact, the infinite gamma tail admits a rigorous Rankin--Euler enclosure, the universal sawtooth constant is exact, and the deterministic universal-collapse step can be proved in the source model. WI-034 and WI-035 removed two more plausible arithmetic failure modes.

That progress makes the welding interface more, not less, important. The remaining chain is now better represented as

\[
\boxed{
\text{MRT shifted-prime input}
\to
\text{two-modulus / collar transport}
\to
\color{black}{\textbf{weighted welding/glue theorem}}
\to
\text{finite remainder ledger}
\to R(1).
}
\tag{14}
\]

The bold step cannot be replaced by a generic divisor-bound citation. Until it is supplied, neither the candidate `0.6916` rung nor the stronger diagnostic values obtained by combining the exact `-1/48` core with an uncertified tail may be promoted to unconditional zeta evidence.

The next high-value audit should therefore reconstruct the exact pre-glue expression and attempt the cheapest of the four mechanisms in Section 5 above. If the only available proof introduces Cauchy--Schwarz across the family, the source itself records that the resulting Poisson floor is `50--60x` over budget; that would become a genuine route barrier rather than merely a missing write-out.

## 8. Prior-art / novelty audit

No novelty is claimed for MRT Proposition 5.4, its Type `d_j`/Type II decompositions, Appendix A, Abel summation, or the elementary fact that bounded coefficients may correlate perfectly with an additive character. The no-go example (11)--(12) is a standard adversarial test, not a new theorem.

The Mathia contribution is an evidence/provenance audit specific to the Yang one-sided chain:

- compare the exact function class in the cited MRT proposition with the function class required by the printed welding sentence;
- identify that Appendix A proves Proposition 5.5 rather than furnishing a generic weighted extension of Proposition 5.4;
- make explicit the elementary counterexample showing why pointwise divisor-boundedness cannot be the missing implication;
- isolate a precise new falsification gate for the one-sided fourth-moment route.

A targeted review of the pinned public reproduction tree found the printed paper, certification scripts, GPU calculations and exact-constant artifacts, but no standalone rounds-38--40 archive proving the required weighted glue statement. Absence from that tree is a reproducibility fact, **not** a claim that the authors possess no private proof and not a priority claim.

## 9. Decisive verification / falsification gate

This finding should be narrowed or retired if a public source supplies a theorem with all of the following data:

1. the exact welding coefficient produced before the minor-arc estimate, including the dependence of `I(n)` on `n,k,b_1,b_2`;
2. a decomposition or norm condition stronger than divisor-boundedness that is actually satisfied by that coefficient;
3. a primary theorem (MRT or otherwise) whose stated hypotheses match that decomposition/condition;
4. the scale inequalities needed at the `8/33` band, including the smoothing collar and all modulus/physical-length losses;
5. an aggregation argument that does not use the across-family Cauchy--Schwarz step which the source declares over budget.

Conversely, if every attempt to produce such a weighted theorem necessarily pays that Poisson floor or requires a shifted-correlation input beyond MRT's established range, then the one-sided route would face a stronger analytic barrier. The present finding stops one step earlier: it proves that the currently printed “divisor-bounded envelopes” sentence is not by itself a valid bridge.
