# MC-347 — Variable-fidelity raw source queries pay in discrimination divergence

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-346` proves an `R log(1/error)` access lower bound when every raw source query passes through the same binary symmetric channel. Query count, however, is not an invariant resource once a protocol may choose measurements of different quality. A single almost-noiseless query can be much more informative than a noisy one.

The invariant reliability currency is the **binary discrimination divergence paid by the chosen raw-coordinate experiments**.

Keep the reciprocal source vector

\[
X=(X_1,\ldots,X_R)\in\{-1,+1\}^R
\]

from `MC-340`. At query time `t`, after the current transcript history `H_t`, an adaptive controller chooses a coordinate `J_t` and an observation kernel

\[
K_t^{H_t}(\,\cdot\mid s),\qquad s\in\{-1,+1\},
\tag{1}
\]

using only admitted history and controller randomness, then observes

\[
Z_t\sim K_t^{H_t}(\,\cdot\mid X_{J_t}).
\tag{2}
\]

The output alphabet may vary with `t` and the history. Repeated queries, adaptive measurement quality, randomized kernels, and an adapted stopping time `\tau` are all allowed. Assume the opposite-sign kernels are mutually absolutely continuous whenever queried; if a required divergence is infinite, the lower bounds below are automatically satisfied.

For history `h` and sign `s`, define the one-query directional discrimination cost

\[
d_t(h,s)
:=D\!\left(
K_t^h(\cdot\mid s)
\middle\|
K_t^h(\cdot\mid -s)
\right).
\tag{3}
\]

Define the source-averaged total reliability expenditure

\[
\mathfrak D
:=
\mathbf E\!\left[
\sum_{t\le\tau} d_t(H_t,X_{J_t})
\right].
\tag{4}
\]

Let `\widehat X` be any estimator from the complete transcript and

\[
\bar p
:=\frac1R\mathbf E\,d_H(\widehat X,X).
\tag{5}
\]

As in `MC-346`, put

\[
\Lambda_k:=\frac{2^k-2}{2^k-1}.
\tag{6}
\]

For even `R>=2`, every such adaptive variable-fidelity protocol satisfies

\[
\boxed{
\bar p
\ge
\frac{\Lambda_R}{4}
\exp\!\left(-\frac{\mathfrak D}{\Lambda_R R}\right),
}
\tag{7}
\]

or equivalently

\[
\boxed{
\mathfrak D
\ge
\Lambda_R R
\left[
\log\frac{\Lambda_R}{4\bar p}
\right]_+.
}
\tag{8}
\]

For odd `R>=3`,

\[
\boxed{
\bar p
\ge
\frac{\Lambda_R\Lambda_{R-1}}{4}
\exp\!\left(
-\frac{2\mathfrak D}{\Lambda_R\Lambda_{R-1}R}
\right),
}
\tag{9}
\]

and therefore

\[
\boxed{
\mathfrak D
\ge
\frac{\Lambda_R\Lambda_{R-1}R}{2}
\left[
\log\frac{\Lambda_R\Lambda_{R-1}}{4\bar p}
\right]_+.
}
\tag{10}
\]

Thus the logarithmic reliability overhead from `MC-346` is not a peculiarity of fixed BSC noise. In the raw-coordinate model, vanishing Hamming risk requires

\[
\boxed{
\mathfrak D=\Omega\!\left(R\log\frac1{\bar p}\right).
}
\tag{11}
\]

A protocol may trade many weak measurements for a few strong measurements, but it cannot make the total pairwise discrimination evidence disappear.

At the matched-filter endpoint of `MC-340`, energy `\mathcal E(W)\le1` and dephasing error `\delta(W)\le\varepsilon` force average source-coordinate Bayes error at most

\[
\alpha_\varepsilon
:=\varepsilon-\frac{\varepsilon^2}{2}.
\tag{12}
\]

Whenever the admitted endpoint observation is downstream of the raw-query transcript above, `(8)` and `(10)` apply with `\bar p=\alpha_\varepsilon`. Hence any variable-fidelity raw-source realization with `\varepsilon_R\to0` must satisfy

\[
\boxed{
\mathfrak D
=\Omega\!\left(R\log\frac1{\varepsilon_R}\right).
}
\tag{13}
\]

This is the representation-invariant repair of the fixed-noise statement: **query count can be reparameterized by changing measurement quality, while accumulated discrimination KL cannot.**

For the fixed BSC of `MC-346`, every active query has

\[
d_t=D_q
=(1-2q)\log\frac{1-q}{q},
\]

so

\[
\mathfrak D=D_q\,\mathbf E\tau.
\tag{14}
\]

Equations `(8)` and `(10)` then reduce exactly to the even- and odd-rank bounds of `MC-346`.

No estimate for `M(x)` follows. The result only strengthens the finite reciprocal-endpoint admission test: a future Möbius-derived source-access architecture must expose enough **total discrimination divergence**, not merely enough nominal query events.

## 1. Adaptive change of measure gives an exact edge cost

Fix two admissible source states `x,x'` and run the same controller under each. Let `P_x^T` and `P_{x'}^T` be the complete stopped-transcript laws. Because the controller chooses `J_t` and the kernel `K_t^{H_t}` from admitted history alone, their conditional laws agree under the two source hypotheses once the realized history is fixed. The only likelihood-ratio contribution comes from queries to coordinates on which `x` and `x'` differ.

The standard stopped adaptive chain rule therefore gives

\[
D(P_x^T\|P_{x'}^T)
=
\mathbf E_x
\sum_{t\le\tau:\,x_{J_t}\ne x'_{J_t}}
 d_t(H_t,x_{J_t}).
\tag{15}
\]

The reverse divergence is the analogous expectation under `x'`. Define the symmetrized edge expenditure

\[
b(x,x')
:=\frac12\left(
D(P_x^T\|P_{x'}^T)
+
D(P_{x'}^T\|P_x^T)
\right).
\tag{16}
\]

If coordinate `j` differs between the two source states, applying Bretagnolle--Huber to the event selected by the coordinate decoder in both directions gives

\[
e_j(x)+e_j(x')
\ge
\frac12 e^{-b(x,x')},
\tag{17}
\]

where `e_j(x)=P_x(\widehat X_j\ne x_j)`. This is the same testing step as `MC-346`, but the edge weight is now the actual accumulated KL of the adaptive experiments rather than `D_q` times a query count.

## 2. Even rank: summing cube-edge divergence gives the global budget

For even `R`, the reciprocal source law is uniform on

\[
S=\{-1,+1\}^R\setminus\{\mathbf1\},
\qquad m=2^R-1.
\]

Join surviving states that differ in one coordinate. As in `MC-346`,

\[
|E|=\frac{mR\Lambda_R}{2}.
\tag{18}
\]

Summing `(17)` over all surviving edges gives

\[
mR\bar p
\ge
\frac12\sum_{e\in E}e^{-b_e}.
\tag{19}
\]

For a fixed source state `x`, each realized query contributes its directional KL cost to at most one surviving cube edge: the edge obtained by flipping the queried coordinate, if that neighboring state has not been punctured. Hence

\[
\sum_{e\in E}b_e
\le
\frac12\sum_{x\in S}
\mathbf E_x\sum_{t\le\tau}d_t(H_t,x_{J_t})
=
\frac m2\,\mathfrak D.
\tag{20}
\]

Jensen applied to `(19)`, followed by `(18)` and `(20)`, yields

\[
\bar p
\ge
\frac{\Lambda_R}{4}
\exp\!\left(-\frac{\mathfrak D}{\Lambda_RR}\right),
\]

which is `(7)`.

The proof never counts queries and never assumes a common noise law. A weak measurement has small edge KL and a high-fidelity measurement has large edge KL automatically.

## 3. Odd rank: parity-preserving pair flips retain the same invariant

For odd `R`, condition on the event `E_0` that the source is not the all-`+1` word. As in `MC-346`, `P(E_0)=\Lambda_R`, and conditioned on `E_0` the source is uniform on the even-parity cube with one vertex deleted.

Join states differing in two coordinates. Let `M=2^{R-1}-1`; the pair-flip graph has

\[
|E_2|
=
\frac{M\Lambda_{R-1}}2\binom R2.
\tag{21}
\]

If an edge differs in coordinates `i,j`, `(17)` for `i` and `j` gives

\[
e_i(x)+e_i(x')+e_j(x)+e_j(x')
\ge e^{-b_e}.
\tag{22}
\]

Each coordinate error participates in at most `R-1` pair-flip edges, so for conditional average Hamming risk `\bar p_0`,

\[
(R-1)MR\bar p_0
\ge
\sum_{e\in E_2}e^{-b_e}.
\tag{23}
\]

Similarly, each directional KL contribution from a query to one source coordinate participates in at most `R-1` pair-flip edges. If `\mathfrak D_0` is the conditional average of `(4)` given `E_0`, then

\[
\sum_{e\in E_2}b_e
\le
\frac{M(R-1)}2\,\mathfrak D_0.
\tag{24}
\]

Jensen and `(21)` give

\[
\bar p_0
\ge
\frac{\Lambda_{R-1}}4
\exp\!\left(
-\frac{2\mathfrak D_0}{\Lambda_{R-1}R}
\right).
\tag{25}
\]

Unconditionally,

\[
\bar p\ge\Lambda_R\bar p_0,
\qquad
\mathfrak D\ge\Lambda_R\mathfrak D_0.
\tag{26}
\]

Substituting these inequalities into `(25)` proves `(9)` and `(10)`.

As in `MC-346`, the factor `1/2` in the odd-rank exponent is not claimed sharp. It is the cost of using parity-preserving two-coordinate neighbors. The durable point is the logarithmic dependence on target error in the invariant divergence currency.

## 4. Variable BSC quality illustrates why query count is the wrong currency

Suppose the controller may choose a crossover probability `q_t(H_t)\in(0,1/2)` before each raw-coordinate observation. Then

\[
d_t(H_t,X_{J_t})
=
D_{q_t}
=(1-2q_t)\log\frac{1-q_t}{q_t},
\tag{27}
\]

independent of the hidden sign. Therefore

\[
\mathfrak D
=
\mathbf E\sum_{t\le\tau}D_{q_t}.
\tag{28}
\]

The protocol can reduce the number of accesses by choosing smaller `q_t`, but `(8)` and `(10)` force the missing cost to reappear through the larger `D_{q_t}`. In particular, letting `q_t` tend to zero is not a loophole: `D_q\sim\log(1/q)` as `q\downarrow0`, exactly the scale needed for exponentially reliable binary discrimination.

Conversely, if every admitted raw query satisfies the uniform reliability ceiling

\[
d_t(H_t,s)\le D_*
\qquad\text{for both signs},
\tag{29}
\]

then `\mathfrak D\le D_*\mathbf E\tau`, and `(8)`--`(10)` recover an access lower bound with `D_*` in place of the fixed-BSC `D_q`. The theorem therefore applies to arbitrary bounded-fidelity raw-coordinate channels, not only bit flips.

## Prior art and novelty boundary

The statistical machinery is classical and no novelty is claimed for it.

Kaufmann, Cappé and Garivier, *On the Complexity of Best-Arm Identification in Multi-Armed Bandit Models*, JMLR **17** (2016), 1--42, develop an adaptive change-of-measure inequality in which expected numbers of adaptively selected observations multiply KL divergences between alternative models. Their Lemma 1 is a standard modern anchor for the stopped adaptive KL accounting used in `(15)`.

Bretagnolle and Huber's testing inequality supplies the exponential conversion from transcript KL to binary testing error used in `(17)`. The cube-edge summation is an Assouad-style reduction from Hamming estimation to neighboring binary tests. Recent work such as Chen, Foster, Han, Qian, Rakhlin and Xu, *Assouad, Fano, and Le Cam with Interaction: A Unifying Lower Bound Framework and Characterization for Bandit Learnability*, arXiv:2410.05117, explicitly develops interactive analogues of classical Assouad/Fano/Le Cam lower-bound methods.

Feige, Raghavan, Peleg and Upfal, *Computing with Noisy Information*, SIAM Journal on Computing **23** (1994), 1001--1018, and Evans and Pippenger, *Average-Case Lower Bounds for Noisy Boolean Decision Trees*, SIAM Journal on Computing **28** (1999), 433--446, are direct noisy-query antecedents for logarithmic reliability overheads in Boolean decision trees.

A targeted literature audit on 17 September 2026 therefore makes **no novelty claim** for adaptive KL accounting, Assouad hypercube reductions, noisy-decision-tree reliability, or variable-quality statistical experiments. The Mathia delta is the exact specialization to the reciprocal endpoint source law and the conversion of `MC-346` from a fixed-channel query-count statement into the source-natural divergence budget `(8)`--`(13)`.

## Boundaries and falsification tests

- **The selector and measurement kernel may use admitted history, not hidden source side information.** If `J_t` or `K_t` can inspect `X` outside the transcript, their choices themselves carry source information and must be included as an observation channel.
- **Opposite-sign kernels must be compared at the same realized history.** The theorem allows history-dependent experiments, but the controller cannot silently choose a source-dependent kernel before that source information has appeared in admitted history.
- **Infinite KL is not forbidden; it is expensive.** A noiseless observation can make opposite source signs mutually singular, giving infinite directional discrimination cost. The theorem then becomes vacuous rather than incorrectly declaring a cheap perfect measurement.
- **This is a raw-coordinate theorem.** A coded observation depending jointly on many source bits is not charged by `(3)` and requires a different experiment graph and its own information/reliability audit.
- **The divergence budget is necessary, not sufficient.** Paying `Theta(R log(1/epsilon))` discrimination KL does not construct the coherent Möbius coefficient family required by endpoint dephasing.
- **The odd-rank constant is not optimized.** The parity relation is handled by pair-flip edges; a sharper graph inequality may improve constants without changing the reliability scale.
- **No arithmetic source-access representation is proved.** The live arithmetic task remains to show that a natural Möbius-derived transcript actually factors through controlled raw-source experiments and to bound the resulting `\mathfrak D` from the arithmetic side.
- **No RH or Mertens estimate follows.** This is an admission obstruction inside the finite reciprocal endpoint model.

## Consequence for the research line

`MC-345` made Shannon capacity the invariant currency for fixed-error source acquisition. `MC-346` showed that raw-coordinate recovery has an additional logarithmic reliability overhead, but expressed that overhead in fixed-BSC query count. The present result removes that coordinate choice: **the reliable-acquisition resource is accumulated discrimination KL**.

This sharpens the next arithmetic question. For any proposed Möbius-derived source transcript, one should now identify the actual raw-coordinate experiment kernel and bound

\[
\mathbf E\sum_{t\le\tau}
D\!\left(
K_t^{H_t}(\cdot\mid X_{J_t})
\middle\|
K_t^{H_t}(\cdot\mid -X_{J_t})
\right)
\]

at the source scale consumed downstream. Bounding only the number of observations, their nominal noise variance, or their forward sensitivity is not enough: those quantities can be traded against measurement fidelity, while the discrimination divergence cannot.