# MC-366 — Adaptive coordinate queries pay a sharp own-phase revealment tariff

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-338` replaces syntactic source-degree restrictions by the invariant predictability

\[
\rho_i^2
=\mathbf E\left|
\mathbf E[X_i\mid Y_i]
\right|^2,
\]

where `Y_i` is the information available to coefficients attached to source cell `i`. `MC-344`–`MC-365` then show that generic noisy channels do not close the endpoint: an extensive coordinatewise BSC can still carry enough information to asymptotically saturate the generic transcript tariffs.

For the **even-rank reciprocal endpoint**, there is nevertheless an exact source-specific tariff for a natural intermediate class: adaptive algorithms that may inspect source coordinates but do not receive arbitrary joint side information.

Let

\[
X=(X_1,\ldots,X_R)
\]

have the even-rank reciprocal source law from `MC-340`: `X` is uniform on

\[
\{-1,+1\}^R\setminus\{(+1,\ldots,+1)\},
\qquad
m:=2^R-1.
\tag{1}
\]

Fix a source cell `i`. Let `Y_i` be the complete transcript of a randomized, adaptive, noiseless coordinate-query algorithm with source-independent internal randomness. The algorithm may choose the next coordinate from all previous queried indices and observed values, and may stop adaptively. It has no other source side channel. Let

\[
Q_i=\{\text{coordinate }i\text{ is ever queried}\},
\qquad
p_i:=\mathbf P(Q_i).
\tag{2}
\]

Then

\[
\boxed{
\rho_i^2
:=\mathbf E\left|
\mathbf E[X_i\mid Y_i]
\right|^2
\le p_i+\frac1m.
}
\tag{3}
\]

The additive `1/m` is exactly the puncture leakage already visible in `MC-338`: if `X_i` is not queried, the other coordinates determine it only on the unique state

\[
X_{-i}=(+1,\ldots,+1),
\tag{4}
\]

whose probability is `1/m`.

Now attach such a transcript to every source cell and put

\[
\bar p:=\frac1R\sum_{i=1}^R p_i,
\qquad
\rho^2:=\frac1R\sum_{i=1}^R\rho_i^2.
\tag{5}
\]

Then

\[
\boxed{
\rho^2\le \min\left\{1,\bar p+\frac1m\right\}.
}
\tag{6}
\]

Combining `(6)` with the exact information-energy obstruction of `MC-338`, any admissible endpoint coefficient family with normalized coefficient energy

\[
\mathcal E(W)\le C
\]

and all-mode RMS dephasing error `\delta(W)` satisfies

\[
\boxed{
\delta(W)
\ge
\left(
1-\sqrt C\sqrt{\bar p+\frac1m}
\right)_+.
}
\tag{7}
\]

Equivalently, if `\delta(W)\le1-\eta` for some `\eta>0`, then necessarily

\[
\boxed{
\bar p
\ge
\frac{\eta^2}{C}-\frac1m.
}
\tag{8}
\]

At the matched-filter energy floor `C=1`, **exact dephasing** therefore requires

\[
\boxed{
\bar p\ge1-\frac1{2^R-1}.
}
\tag{9}
\]

This endpoint is sharp inside the coordinate-query model. For each `i`, query all coordinates except `i`; if they are all `+1`, infer `X_i=-1` from the puncture, and otherwise query `i`. This reconstructs `X_i` exactly while

\[
p_i=1-\frac1m.
\tag{10}
\]

Hence the BSC equality family of `MC-365` is not a mysterious counterexample to source-specific control. It sits on the **full-own-source-access side** of the boundary: a BSC readout first exposes the relevant source coordinate and then corrupts it. By contrast, an architecture with `\bar p=o(1)` cannot obtain any fixed amount of bounded-energy endpoint dephasing in the even-rank reciprocal model.

No estimate for `M(x)` follows. The result is an exact finite endpoint admission theorem: a proposed source-natural transcript built from adaptive source-coordinate inspection must either reveal the very phase it cancels at positive density, pay growing coefficient energy, or fail to dephase.

## 1. The punctured cube leaves exactly one no-query decoder atom

Let

\[
h_i(X_{-i})
:=\mathbf E[X_i\mid X_{-i}].
\tag{11}
\]

Under `(1)`, if `X_{-i}` contains at least one `-1`, both completions `X_i=+1` and `X_i=-1` remain present in the support with equal probability. Therefore

\[
h_i(X_{-i})=0.
\tag{12}
\]

If instead all other coordinates equal `+1`, the completion `X_i=+1` is precisely the deleted all-plus point, so only `X_i=-1` remains and

\[
h_i(+1,\ldots,+1)=-1.
\tag{13}
\]

There is exactly one source word with `(13)`, so

\[
\boxed{
\mathbf E\,h_i(X_{-i})^2=\frac1m.
}
\tag{14}
\]

This is the same `m^{-1}` leakage computed in `MC-338` for the observation consisting of all source phases except the own phase. Here it is written directly as the optimal mean-square predictor from the other coordinates.

## 2. Adaptive inspection cannot create additional no-query predictability

Let `U` denote all source-independent internal randomness of the query algorithm. Because the algorithm is nonanticipating, the event `Q_i^c` that coordinate `i` is never queried, together with the transcript produced on that event, is a measurable function of `(X_{-i},U)` alone.

Write

\[
g_i(Y_i):=\mathbf E[X_i\mid Y_i].
\tag{15}
\]

The complete transcript records which coordinates were queried, so `Q_i` is `Y_i`-measurable. On `Q_i`, the noiseless response reveals `X_i`, and hence

\[
\mathbf E[\mathbf1_{Q_i}g_i(Y_i)^2]=p_i.
\tag{16}
\]

On `Q_i^c`, the transcript is a coarsening of `(X_{-i},U)`. Since `U` is independent of the source,

\[
\mathbf E[X_i\mid X_{-i},U]
=h_i(X_{-i}).
\tag{17}
\]

Conditional expectation is the orthogonal projection in `L^2`, so coarsening cannot increase the squared norm of the predictor. Restricting to the `Y_i`-measurable event `Q_i^c` gives

\[
\begin{aligned}
\mathbf E[\mathbf1_{Q_i^c}g_i(Y_i)^2]
&\le
\mathbf E[\mathbf1_{Q_i^c}h_i(X_{-i})^2]\\
&\le
\mathbf E h_i(X_{-i})^2\\
&=\frac1m.
\end{aligned}
\tag{18}
\]

Equations `(16)` and `(18)` prove `(3)`. Averaging over source cells proves `(6)`.

The argument allows arbitrary adaptivity, arbitrary stopping, repeated queries, and arbitrary randomized postprocessing of the transcript. What it forbids is exactly the hidden resource that would make the theorem false: a side channel carrying information about `X_i` before `i` has been queried.

## 3. Revealment converts directly into endpoint dephasing cost

For each source cell let the admissible coefficient functions be arbitrary square-integrable functions of its transcript:

\[
\mathcal H_i=L^2(\sigma(Y_i)).
\tag{19}
\]

Then `MC-338` identifies its own-phase leakage with

\[
\rho_i
=\left\|
\mathbf E[X_i\mid Y_i]
\right\|_2.
\tag{20}
\]

The same finding proves, for normalized coefficient energy `\mathcal E(W)`,

\[
\delta(W)
\ge
\bigl(1-\rho\sqrt{\mathcal E(W)}\bigr)_+.
\tag{21}
\]

Insert `\mathcal E(W)\le C` and `(6)` into `(21)` to obtain `(7)`. If `\delta(W)\le1-\eta`, equation `(21)` forces

\[
\rho\sqrt C\ge\eta,
\]

and `(8)` follows.

Several regimes are immediate:

- if `\bar p=0`, then `\rho^2\le1/m`, recovering the exponential energy obstruction of the self-phase-excluded even-rank endpoint in `MC-338`;
- if `\bar p=o(1)` and `C=O(1)`, then `\delta(W)\to1`, so asymptotically no constant dephasing survives;
- fixed constant-factor dephasing at bounded energy requires `\bar p=\Omega(1)`;
- exact dephasing at unit energy forces the near-total self-revealment `(9)`.

Thus coordinate-query complexity enters the endpoint through a quantity more specific than mutual information: **direct revealment of the coordinate whose phase is being cancelled**.

## 4. The exact unit-energy tariff is attained

Fix `i`. Consider the deterministic algorithm that queries every coordinate in `[R]\setminus\{i\}` first. If all observed values are `+1`, equation `(13)` determines `X_i=-1` and the algorithm stops without querying `i`. Otherwise it queries `i` directly.

The no-query event occurs exactly on the unique source word with

\[
X_{-i}=(+1,\ldots,+1),
\]

so it has probability `1/m`. Therefore `(10)` holds. The resulting transcript determines `X_i` with zero error, hence

\[
\rho_i=1.
\tag{22}
\]

Using the reconstructed phase as the ordinary matched-filter coefficient attains exact endpoint dephasing with normalized energy one. Therefore `(9)` is not merely an order-of-magnitude converse: **its self-query probability is exact for this unrestricted adaptive coordinate-query model**.

The sharpness construction also clarifies what the theorem does and does not buy. It does not rule out a sophisticated algorithm that spends nearly all source coordinates to reconstruct each target phase. It says that the punctured source law offers no cheaper own-phase shortcut: apart from the single deleted atom, exact unit-energy cancellation must directly expose the target coordinate.

## 5. Relation to the BSC frontier

`MC-344` and `MC-365` deliberately allow a readout that takes each source coordinate as input and then passes it through a binary symmetric channel. Such a channel has `p_i=1` in the present revealment accounting: the own source coordinate is an explicit input to the readout before noise is added.

Consequently `(7)` does **not** contradict the BSC sharpness examples, and it should not. Instead it identifies their hidden structural resource. Generic information, Hellinger, JS, and product-affinity tariffs cannot distinguish a source-natural arithmetic transcript from an engineered noisy matched source because both may carry comparable aggregate information. Revealment can distinguish them when the arithmetic construction can be proved not to inspect the relevant own source coordinate directly.

This moves the next burden to the arithmetic side. A useful transcript proposal must now specify its provenance well enough to answer a concrete question:

> For coefficients attached to source cell `i`, what fraction of the endpoint source states can make the construction depend directly on the own phase `X_i`, rather than only on other source coordinates or source-independent data?

If that revealment fraction is `o(1)`, `(7)` kills bounded-energy constant dephasing in the even-rank endpoint. If it is positive or near one, the construction must justify why that own-phase access is not simply a disguised matched filter.

## Prior art and novelty boundary

The language of **revealment** for adaptive randomized coordinate algorithms is classical. O'Donnell, Saks, Schramm and Servedio, *Every decision tree has an influential variable*, 46th IEEE FOCS (2005), pp. 31–39, DOI `10.1109/SFCS.2005.34`, arXiv `cs/0508071`, prove the OSSS inequality

\[
\operatorname{Var}(f)
\le
\sum_i \delta_i\operatorname{Inf}_i(f)
\]

for product measures, where `\delta_i` is the probability that the decision tree reads coordinate `i`, and develop randomized/general-output variants. Schramm and Steif, *Quantitative noise sensitivity and exceptional times for percolation*, Annals of Mathematics **171** (2010), 619–672, DOI `10.4007/annals.2010.171.619`, use randomized-algorithm revealment to control Fourier levels. Extensions of OSSS-type ideas beyond product measures also exist; for example van den Berg and Don, *An OSSS-type inequality for uniformly drawn subsets of fixed size*, arXiv `2210.16100`, treat fixed-size subset measures.

No novelty is claimed for decision-tree revealment, influences, OSSS inequalities, or randomized query complexity. The proof of `(3)` does not invoke OSSS. Its durable Mathia-specific content is the exact composition of two already isolated endpoint facts: the reciprocal source is the uniform cube with one atom removed, which leaves precisely `1/m` no-own-query predictability, and `MC-338` converts that predictability into a normalized dephasing-energy obstruction. The sharp equality construction `(10)` pins down the resulting own-phase revealment tariff exactly.

A targeted prior-art audit on 18 September 2026 found the classical product-measure revealment theory and nonproduct extensions above, but no external theorem is needed for `(3)`–`(10)` and no standalone novelty claim is made.

## Boundaries and falsification tests

- **Even rank is load-bearing.** For odd `R`, `MC-338` gives `X_i=\prod_{j\ne i}X_j`; all other source phases determine the own phase exactly, so a zero-self-query theorem of this form is false.
- **The transcript is a coordinate-query transcript.** Arbitrary linear measurements, parity queries, group characters, or other joint functions of `X` are not covered and require their own provenance tariff.
- **No hidden side channel is allowed.** The next-query rule and stopping decision may use source-independent randomness and previously queried values only. If they may depend on `X_i` before querying `i`, that dependence is already own-phase access and must be charged separately.
- **Queries are noiseless in the theorem.** Noisy direct queries can only require a separate reliability analysis; `MC-344`–`MC-365` already show that noise by itself is not a universal obstruction.
- **Other-coordinate query count is unrestricted.** The sharp construction may inspect all `R-1` other coordinates. The theorem prices own-phase revealment, not total query complexity.
- **The additive puncture term is necessary.** Removing `1/m` would be false because the all-other-plus state determines `X_i` without querying it.
- **The result is an endpoint admission theorem, not an arithmetic estimate.** To affect `M(x)`, a future argument must prove that a concrete Möbius-derived transcript fits this coordinate-query model with a sufficiently small `\bar p` and then connect the endpoint obstruction to a global cancellation mechanism.

## Consequence for the research line

The generic information-tariff program ended at `MC-365` because a coordinatewise BSC realizes the endpoint at the expected generic information cost. `MC-366` identifies a stricter source-specific resource that the BSC spends explicitly: **own-phase revealment**.

For the even-rank reciprocal endpoint, bounded-energy dephasing cannot be manufactured from adaptive access to the *other* source coordinates plus source-independent randomness. Constant dephasing requires direct target-coordinate revealment at positive density, and exact unit-energy dephasing requires the sharp rate `1-1/(2^R-1)`. The next productive question is therefore no longer another generic divergence tariff. It is whether a concrete arithmetic transcript relevant to Möbius cancellation can be shown to have subconstant own-phase revealment—or whether every apparently natural construction that reaches the endpoint can be reduced to near-total direct phase access.