# AF-052 — Reversible output cloning removes the Hall part of TV zero-error repair

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `NEGATIVE/OBSTRUCTION`

## Claim

Let `X` and `Y` be finite nonempty sets, let

\[
d:X\to D,
\qquad
A=d(X),
\qquad
m=|A|,
\]

assume `|Y|\ge m`, and fix a strictly positive prior `\pi` on `X`. Let `K:X\rightsquigarrow Y` be a stochastic channel. As in AF-047, define

\[
q_a(y)=\sum_{x:d(x)=a}\pi_xK(y\mid x),
\qquad
m(y)=\max_{a\in A}q_a(y),
\]

\[
c(a,y)=m(y)-q_a(y)\ge0,
\]

and let

\[
R_B(K)=1-\sum_{y\in Y}m(y)
\]

be the Bayes error for predicting the discriminator `d(X)` from `Y`.

For an integer `k\ge1`, define the uniform output-cloning map

\[
C_k:\Delta(Y)\to\Delta(Y\times[k]),
\qquad
(C_kP)(y,j)=\frac{P(y)}{k}.
\]

Write `K^{(k)}=C_kK`, and let `\mathcal Z_{d,k}^{(0)}` be AF-011's zero-error faithful set on the cloned output alphabet `Y\times[k]`. Then:

1. **Cloning does not change the statistical experiment or total-variation geometry.** If `M_k(y\mid(y',j))=1_{\{y=y'\}}`, then
   \[
   M_kC_k=\operatorname{id}_{Y}.
   \]
   Hence `K` and `K^{(k)}` are Blackwell-equivalent. Moreover, for every pair of probability vectors `P,Q` on `Y`,
   \[
   \boxed{
   \operatorname{TV}(C_kP,C_kQ)=\operatorname{TV}(P,Q).
   }
   \]
   Consequently the prior-weighted row metric `\rho_\pi` from AF-047 is also preserved exactly by `C_k`.

2. **The unrestricted zero-error repair distance nevertheless changes under this reversible refinement.** Define the capacitated coverage cost
   \[
   \tau_k^{\mathrm{cap}}
   :=
   \min_{g:A\to Y\,:\,|g^{-1}(y)|\le k\ \forall y}
   \sum_{a\in A}c(a,g(a)).
   \]
   Then
   \[
   \boxed{
   \operatorname{dist}_{\rho_\pi}
   \bigl(K^{(k)},\mathcal Z_{d,k}^{(0)}\bigr)
   =
   R_B(K)+\frac1k\tau_k^{\mathrm{cap}}.
   }
   \]
   For `k=1`, `\tau_1^{\mathrm{cap}}` is exactly AF-047's injective Hall/assignment penalty `\tau`.

3. **After enough cloning, the Hall distinct-output obstruction disappears and only one per-class local penalty remains.** Put
   \[
   \eta(K,d,\pi)
   :=
   \sum_{a\in A}\min_{y\in Y}c(a,y).
   \]
   For every `k\ge m`, the capacity constraints are vacuous, so
   \[
   \boxed{
   \operatorname{dist}_{\rho_\pi}
   \bigl(K^{(k)},\mathcal Z_{d,k}^{(0)}\bigr)
   =
   R_B(K)+\frac{\eta(K,d,\pi)}{k}.
   }
   \]
   In particular,
   \[
   \boxed{
   \lim_{k\to\infty}
   \operatorname{dist}_{\rho_\pi}
   \bigl(K^{(k)},\mathcal Z_{d,k}^{(0)}\bigr)
   =R_B(K).
   }
   \]
   Thus the global Hall coverage penalty in AF-047 is not an invariant of the Blackwell experiment. It is partly an invariant of how many output atoms the chosen presentation makes available to a repair.

4. **The effect is target-induced, not metric-induced.** Let the clone-compatible zero-error target be
   \[
   \mathcal Z_{d,k}^{\mathrm{desc}}
   :=
   \{C_kL:L\in\mathcal Z_d^{(0)}\}.
   \]
   Since `C_k` is a `\rho_\pi`-isometry,
   \[
   \boxed{
   \operatorname{dist}_{\rho_\pi}
   \bigl(C_kK,\mathcal Z_{d,k}^{\mathrm{desc}}\bigr)
   =
   \operatorname{dist}_{\rho_\pi}
   \bigl(K,\mathcal Z_d^{(0)}\bigr).
   }
   \]
   The drop occurs only because the unrestricted target `\mathcal Z_{d,k}^{(0)}` contains zero-error repaired channels that use different clone labels for different discriminator classes and therefore do not descend to a channel on the original alphabet.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{presentation-invariant discrepancy}
\not\Rightarrow
\text{presentation-invariant distance to a structural target}.}
\]

A structural repair radius can be intrinsic on equivalence classes only if the **target class is itself compatible with the declared equivalence**, or if repairs are required to descend through the equivalence map. AF-051 showed one failure mode in which Euclidean geometry itself contracts under cloning. AF-052 isolates a different and stronger failure mode: even total variation, which is exactly invariant under uniform cloning, gives a clone-dependent repair radius because the zero-error target acquires new non-descending support partitions.

## Derivation

### Cloning is both Blackwell-reversible and TV-isometric

For each original output `y`, `C_k` replaces it by a uniformly random clone `(y,j)`. The deterministic merge `M_k` forgets `j`, hence `M_kC_k=id`. Applying `C_k` after `K` is a garbling of `K`, while applying `M_k` after `C_kK` recovers `K`; the two experiments are therefore Blackwell-equivalent.

For any `P,Q\in\Delta(Y)`,

\[
\begin{aligned}
\operatorname{TV}(C_kP,C_kQ)
&=\frac12\sum_{y\in Y}\sum_{j=1}^k
\left|\frac{P(y)-Q(y)}{k}\right|\\
&=\frac12\sum_y|P(y)-Q(y)|\\
&=\operatorname{TV}(P,Q).
\end{aligned}
\]

Averaging over the fixed upstream prior gives the same identity for `\rho_\pi` on channels.

This is the crucial control against the AF-051 mechanism: here the ambient metric does **not** shrink when outputs are refined.

### AF-047 on the cloned alphabet becomes a capacitated assignment

The class-output masses of the cloned experiment are

\[
q_a^{(k)}(y,j)=\frac{q_a(y)}{k},
\]

so

\[
m^{(k)}(y,j)=\frac{m(y)}{k}
\]

and the Bayes accuracy is unchanged:

\[
\sum_{y,j}m^{(k)}(y,j)
=\sum_y m(y).
\]

Therefore

\[
R_B(K^{(k)})=R_B(K).
\]

AF-047 writes the excess zero-error repair cost above Bayes error as a minimum-cost injection from discriminator classes into output symbols. An injection

\[
\iota:A\hookrightarrow Y\times[k]
\]

chooses, for every class `a`, a representative clone `\iota(a)=(g(a),j_a)`. Distinctness of the clones means precisely that no original output `y` can receive more than `k` class representatives:

\[
|g^{-1}(y)|\le k.
\]

The cost of assigning class `a` to clone `(y,j)` is

\[
m^{(k)}(y,j)-q_a^{(k)}(y,j)
=\frac{c(a,y)}{k}.
\]

Hence the cloned Hall/assignment penalty is exactly

\[
\tau(K^{(k)},d,\pi)
=\frac1k\tau_k^{\mathrm{cap}}.
\]

Substituting into AF-047 gives

\[
\operatorname{dist}_{\rho_\pi}
(K^{(k)},\mathcal Z_{d,k}^{(0)})
=R_B(K)+\frac1k\tau_k^{\mathrm{cap}}.
\]

No approximation is involved.

### The large-clone regime

If `k\ge m=|A|`, then every map `g:A\to Y` automatically obeys

\[
|g^{-1}(y)|\le m\le k.
\]

The minimization therefore separates class by class:

\[
\tau_k^{\mathrm{cap}}
=\min_{g:A\to Y}\sum_ac(a,g(a))
=\sum_a\min_yc(a,y)
=\eta.
\]

This proves the exact tail formula

\[
\operatorname{dist}_{\rho_\pi}
(K^{(k)},\mathcal Z_{d,k}^{(0)})
=R_B(K)+\frac{\eta}{k}
\qquad(k\ge m)
\]

and therefore convergence to Bayes error.

The interpretation is sharp. AF-047's `\tau` measures the cost of choosing **distinct original output atoms** to witness all classes. Cloning gives each original atom `k` statistically redundant copies. Those copies are useless for inference in `K^{(k)}`, but the unrestricted repair set is free to repurpose them as distinct class-support atoms. The original Hall bottleneck is therefore diluted by the presentation refinement.

## Exact controls

### A fixed experiment can lose a large structural penalty without gaining information

Take two discriminator classes with prior

\[
\pi_1=0.9,
\qquad
\pi_2=0.1,
\]

and identical rows

\[
K_1=K_2=\left(\frac12,\frac12\right).
\]

As in AF-047,

\[
R_B=0.1,
\qquad
\operatorname{dist}_{\rho_\pi}(K,\mathcal Z_d^{(0)})=0.5.
\]

For both outputs, the majority class has mass `0.45` and the minority class `0.05`, so

\[
\eta=0+0.40=0.40.
\]

Thus for every `k\ge2`,

\[
\boxed{
\operatorname{dist}_{\rho_\pi}
(K^{(k)},\mathcal Z_{d,k}^{(0)})
=0.1+\frac{0.4}{k}
\longrightarrow0.1.
}
\]

The experiment is Blackwell-equivalent for every `k`; only the number of redundant output atoms changed.

### Cloning can remove the Hall penalty completely at finite `k`

Let `A=\{1,2,3\}` and `Y=\{u,v,w\}`. It is enough to specify the class-output joint masses:

\[
\begin{array}{c|ccc}
 & u & v & w\\\hline
1 & 1/9 & 2/9 & 2/9\\
2 & 1/9 & 1/18 & 1/18\\
3 & 1/9 & 1/18 & 1/18
\end{array}
\]

which sum to one and therefore arise from a valid positive prior and one channel row per class. At `u` all three classes are Bayes-optimal; at `v,w` only class `1` is Bayes-optimal. Hence classes `2` and `3` have the same unique Bayes-optimal original output, so AF-047's Hall condition fails for the original alphabet.

The Bayes error is

\[
R_B
=1-\left(\frac19+\frac29+\frac29\right)
=\frac49.
\]

On the original alphabet, one of classes `2,3` must use `v` or `w` as its representative, at cost

\[
\frac29-\frac1{18}=\frac16,
\]

so

\[
\operatorname{dist}_{\rho_\pi}(K,\mathcal Z_d^{(0)})
=\frac49+\frac16
=\frac{11}{18}.
\]

After `k=2` cloning, classes `2` and `3` may use the two distinct clones of `u`, while class `1` uses a clone of `v` or `w`. Every representative is then Bayes-optimal, so the cloned Hall penalty is exactly zero:

\[
\boxed{
\operatorname{dist}_{\rho_\pi}(K^{(2)},\mathcal Z_{d,2}^{(0)})
=R_B
=\frac49.
}
\]

Nothing about the experiment became more informative. A redundant random label merely enlarged the set of support partitions available to the repair optimization.

## Descending repairs restore presentation invariance

The preceding defect disappears if the target is transported together with the representation. Define

\[
\mathcal Z_{d,k}^{\mathrm{desc}}
= C_k(\mathcal Z_d^{(0)}).
\]

Every element of this set is clone-symmetric and descends through `M_k` to an original-alphabet zero-error channel. Conversely every original zero-error channel has exactly one uniform cloned image.

Using the TV isometry row by row,

\[
\begin{aligned}
\operatorname{dist}_{\rho_\pi}
(C_kK,\mathcal Z_{d,k}^{\mathrm{desc}})
&=\inf_{L\in\mathcal Z_d^{(0)}}
\rho_\pi(C_kK,C_kL)\\
&=\inf_{L\in\mathcal Z_d^{(0)}}
\rho_\pi(K,L)\\
&=\operatorname{dist}_{\rho_\pi}(K,\mathcal Z_d^{(0)}).
\end{aligned}
\]

Thus the issue is not that zero-error support separation is meaningless. The issue is that a distance to it is **representation-relative unless the admissible repair class transforms functorially with the representation**.

For Arithmetic Fidelity this gives a practical audit rule:

> When a retained representation is defined only up to a declared equivalence, test both the discrepancy and the repair target under reversible refinements. If the metric is invariant but the target gains non-descending repairs, the resulting radius measures presentation freedom rather than intrinsic structural robustness.

## Prior art and novelty assessment

The surrounding mathematics is classical.

- David Blackwell, **“Equivalent Comparisons of Experiments,”** *The Annals of Mathematical Statistics* 24(2), 265–272 (1953), DOI `10.1214/aoms/1177729032`, is the foundational comparison-of-experiments source. Uniform output cloning followed by deterministic merging is an elementary pair of mutually recovering garblings, so no novelty is claimed for their statistical equivalence.
- Lucien Le Cam, **“Sufficiency and Approximate Sufficiency,”** *The Annals of Mathematical Statistics* 35(4), 1419–1455 (1964), DOI `10.1214/aoms/1177700372`, supplies the classical equivalence/deficiency viewpoint in which experiment comparison is performed modulo Markov simulation rather than raw output presentation.
- Claude E. Shannon, **“The Zero Error Capacity of a Noisy Channel,”** *IRE Transactions on Information Theory* 2(3), 8–19 (1956), DOI `10.1109/TIT.1956.1056798`, is the foundational source for exact support-confusability as a zero-error notion.
- AF-047 already derives the exact TV projection onto the zero-error target as Bayes error plus a minimum-cost Hall coverage penalty. The capacitated clone formula above is an exact specialization of that theorem after a reversible output refinement.

A targeted search of comparison-of-experiments, Le Cam deficiency, and zero-error-channel literature confirms that the ingredients and the equivalence language are classical. No historical novelty is claimed for Blackwell equivalence, TV invariance under symbol splitting, Hall matching, or zero-error supports. The durable result here is the explicit **mismatch theorem** between those classical structures: AF-047's raw distance-to-zero-error target does not descend to Blackwell equivalence classes even when the discrepancy itself does, and the lost invariance is measured exactly by a capacitated Hall penalty.

## Boundary conditions and falsification checks

1. **Uniform cloning is deliberately information-free.** The clone index is independent of `X` conditional on the original output. A refinement that adds genuine state-dependent side information is not a control for presentation invariance.
2. **The result concerns the repair radius, not zero-error status of the original experiment.** `K` is zero-error faithful if and only if `C_kK` is; cloning does not repair the actual channel. What changes is the distance to the ambient set of all zero-error channels on the chosen alphabet.
3. **The TV metric is essential to the clean target-only diagnosis.** AF-051 shows that quadratic distance already changes under `C_k` before target enlargement is considered. Here TV removes that confound exactly.
4. **The prior is fixed.** `R_B`, `q_a`, `c(a,y)`, and the repair metric all use the same strictly positive prior. This is the same decision-relative setting as AF-047.
5. **The exact tail threshold `k\ge m` is sufficient, not necessary.** Smaller `k` may already make the capacity constraints inactive for the cost-minimizing assignment, as the three-class example with `k=2` shows.
6. **Clone-compatible repair is one natural remedy, not the only possible intrinsic target.** One may instead quotient the entire construction by Blackwell equivalence or use a deficiency-style distance between experiment classes. Any such replacement must state its own target semantics and cannot be inferred from this theorem alone.
7. **No claim is made that every structural target must be Blackwell-invariant.** In applications where output atoms have intrinsic physical, geometric, arithmetic, or operator meaning, clone splitting may be forbidden. The theorem is a falsification control precisely for settings that treat statistically sufficient presentation changes as inessential.

## Consequence for the line

AF-051 separated three ingredients: target geometry, discrepancy geometry, and presentation invariance. AF-052 makes that separation exact even inside an information-monotone metric. There are now two independent presentation-failure modes:

\[
\boxed{
\begin{array}{ll}
\text{AF-051:} & \text{the discrepancy itself changes under reversible refinement},\\
\text{AF-052:} & \text{the discrepancy is invariant but the target class enlarges non-descendingly}.
\end{array}
}
\]

Therefore future Arithmetic Fidelity repair margins should not be treated as structural invariants merely because their divergence obeys data processing or because the retained experiments are Blackwell-equivalent. The admissible **target/repair class must pass the same equivalence audit**. In a prime/RH application, this translates to a sharper gate: if a representation is only canonical up to refinement, relabeling, basis splitting, or another reversible change, then any proposed distance-to-faithfulness or positivity margin must either descend to that quotient or justify why the finer presentation is mathematically intrinsic.