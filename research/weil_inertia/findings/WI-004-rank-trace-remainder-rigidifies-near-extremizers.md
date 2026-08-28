# WI-004 — the rank--trace remainder rigidifies every near-extremizer

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED`. The finite-dimensional identity below is an exact remainder extraction from the proof of Alpöge--Furman Lemma 3.2. No novelty claim is made for the underlying von Neumann trace inequality or scalar square identities. The new research consequence recorded here is that asymptotic saturation of the simple-critical-zero certificate forces several distinct exceptional mechanisms to vanish separately at density scale.

## 1. Why the equality example is not the whole story

WI-001 records that the first-two-moment certificate is sharp: `2N/3` orthogonal simple critical zeros plus `N/6` double critical-line points attain the flat-window bound, and replacing the doubles by off-line pairs whose horizontal depth tends to zero is spectrally limiting-equivalent.

That shows the constant cannot be improved from the same aggregate inputs alone, but it leaves a more refined question:

> If an actual zeta-zero configuration comes close to saturating the rank--trace bound, what must the residual matrix look like?

Alpöge--Furman's proof contains more information than the final inequality because every discarded term is nonnegative. Keeping those terms gives an exact stability decomposition.

## 2. Exact remainder identity for the rank--trace lemma

Let `P,Q` be Hermitian matrices with

\[
P\succeq0,\qquad \operatorname{rank}P\le r,\qquad n_+(Q)=k\le b.
\]

Pad by zero dimensions if necessary so that `r` and `b` can be used as indexing bounds. Write

\[
Q=Q_+-Q_-,\qquad Q_\pm\succeq0,\qquad Q_+Q_-=0.
\]

Let

\[
p_1\ge p_2\ge\cdots\ge0,
\qquad
n_1\ge n_2\ge\cdots\ge0
\]

be the eigenvalues of `P` and `Q_-`, padded with zeros, and let

\[
q_1,\ldots,q_k>0
\]

be the positive eigenvalues of `Q`. Define the von-Neumann alignment defect

\[
V(P,Q_-):=\sum_i p_i n_i-\operatorname{tr}(PQ_-)\ge0.
\]

For the slack in Alpöge--Furman's rank--trace inequality,

\[
\Delta:=r-2\operatorname{tr}P-4\operatorname{tr}Q+4b+\|P+Q\|_{\mathrm{HS}}^2,
\]

one has the exact identity

\[
\boxed{
\begin{aligned}
\Delta={}&2\operatorname{tr}(PQ_+)+2V(P,Q_-)\\
&+\sum_{i\le r}\left((p_i-n_i-1)^2+2n_i\right)\\
&+\sum_{i>r}\left(n_i^2+4n_i\right)\\
&+\sum_{j=1}^{k}(q_j-2)^2+4(b-k).
\end{aligned}
}
\]

Every term on the right is nonnegative.

### Derivation

Expand exactly:

\[
\begin{aligned}
\|P+Q\|_{\mathrm{HS}}^2
={}&\|P\|_{\mathrm{HS}}^2+\|Q_+\|_{\mathrm{HS}}^2+\|Q_-\|_{\mathrm{HS}}^2\\
&+2\operatorname{tr}(PQ_+)-2\operatorname{tr}(PQ_-).
\end{aligned}
\]

Since

\[
\operatorname{tr}(PQ_-)=\sum_i p_i n_i-V(P,Q_-),
\]

the part involving `P,Q_-` becomes

\[
r-2\sum_i p_i+4\sum_i n_i+\sum_i(p_i-n_i)^2+2V(P,Q_-).
\]

Because `p_i=0` for `i>r`, this is exactly

\[
2V(P,Q_-)
+\sum_{i\le r}\left((p_i-n_i-1)^2+2n_i\right)
+\sum_{i>r}\left(n_i^2+4n_i\right).
\]

Similarly,

\[
4b-4\operatorname{tr}Q_++\|Q_+\|_{\mathrm{HS}}^2
=\sum_{j=1}^{k}(q_j-2)^2+4(b-k).
\]

Adding the retained cross term `2 tr(PQ_+)` gives the displayed identity. This is the equality bookkeeping behind the scalar squares already noted in Alpöge--Furman Remark 3.3, but without discarding their remainders.

## 3. A strictly stronger inequality if negative spectral mass is known

The identity immediately gives

\[
\boxed{
\Delta\ge2\operatorname{tr}Q_-+4\bigl(b-n_+(Q)\bigr).
}
\]

Equivalently,

\[
\boxed{
r\ge
2\operatorname{tr}P+4\operatorname{tr}Q-4b-\|P+Q\|_{\mathrm{HS}}^2
+2\operatorname{tr}Q_-
+4\bigl(b-n_+(Q)\bigr).
}
\]

Thus negative **spectral mass**, not merely negative index, is useful information: if one can lower-bound `tr Q_-`, the same first two global moments certify more positive rank.

This does not contradict WI-001. The existing unconditional argument controls only an upper bound for the positive index of the residual, not a positive lower bound for the magnitude of its negative spectrum. The extremal models make precisely this extra information vanish.

## 4. Apply the remainder to the simple-critical-zero decomposition

Use Alpöge--Furman's notation on the enlarged interval `I'`:

- `s_1` = number of simple critical-line zeros;
- `s_2` = number of distinct multiple critical-line points;
- `p` = number of off-line functional-equation pairs;
- `P_1` = compressed contribution of the simple critical-line zeros;
- `Q'=\widetilde G-P_1`;
- `b:=s_2+p`.

Their block argument gives

\[
P_1\succeq0,
\qquad
\operatorname{rank}P_1\le s_1,
\qquad
n_+(Q')\le b.
\]

Applying the strengthened inequality with `r=s_1` and then using the exact counting budget yields

\[
\boxed{
\begin{aligned}
s_1\ge{}&4\operatorname{tr}\widetilde G-2N(I')-\|\widetilde G\|_{\mathrm{HS}}^2\\
&+2A
+2\operatorname{tr}(Q'_-)
+4\bigl(b-n_+(Q')\bigr),
\end{aligned}
}
\]

where

\[
A:=N(I')-\operatorname{tr}P_1-2(s_2+p)\ge0.
\]

The quantity `A` itself has an exact zero-side interpretation. If `m_\rho` denotes multiplicity and one representative is chosen from each off-line pair, then

\[
\boxed{
A=(s_1-\operatorname{tr}P_1)
+\sum_{\rho\in\mathrm{on}_{\ge2}}(m_\rho-2)
+2\sum_{\text{off-line pairs}}(m_\rho-1).
}
\]

So the ordinary `2-R(\psi)` certificate is what remains after discarding three separately nonnegative charges:

1. excess multiplicity / simple-vector trace deficit `A`;
2. aggregate negative spectral mass `tr(Q'_-)`;
3. collapse of the available positive-index budget `b-n_+(Q')`.

## 5. Rigidity of an asymptotically sharp configuration

Let

\[
C_T:=4\operatorname{tr}\widetilde G-2N(I')-\|\widetilde G\|_{\mathrm{HS}}^2.
\]

The prime-side evaluation gives

\[
C_T=(2-R(\psi)+o(1))N(T,2T).
\]

Suppose along some sequence of heights the actual simple-critical count asymptotically saturates this certificate:

\[
s_1=C_T+o(N).
\]

Then the displayed inequality forces, separately,

\[
\boxed{
A=o(N),
\qquad
\operatorname{tr}(Q'_-)=o(N),
\qquad
b-n_+(Q')=o(N).
}
\]

In particular, from the exact expansion of `A`, a saturating exceptional population cannot contain a positive density of either

\[
\boxed{\text{critical-line points of multiplicity }\ge3}
\]

or

\[
\boxed{\text{off-line pairs of multiplicity }\ge2.}
\]

Up to `o(N)` charge, the only multiplicity types compatible with saturation are exactly the ones seen in WI-001's extremizers: double points on the line and simple off-line pairs.

The full remainder identity gives additional rigidity. Near saturation also forces, in aggregate,

\[
\sum_j(q_j-2)^2=o(N),
\qquad
\operatorname{tr}(P_1Q'_+)=o(N),
\qquad
V(P_1,Q'_-)=o(N),
\]

and the corresponding `P_1`/`Q'_-` eigenvalue-square remainders are `o(N)`. Thus the residual positive spectrum must cluster near eigenvalue `2`, its positive subspace must become nearly orthogonal to the simple-zero contribution in Hilbert--Schmidt pairing, and the total magnitude of the aggregate negative spectrum must vanish at density scale.

This is substantially more rigid than merely saying that `Q'` has at most `s_2+p` positive directions.

## 6. What this says about the unresolved complement

The first-two-moment barrier does not leave an arbitrary `1/3`-sized exceptional set. If the theorem's constant were genuinely close to the truth, the exceptional part would have to organize itself into a very special near-equality regime:

\[
\boxed{
\text{mostly on-line doubles and/or simple off-line pairs}
}
\]

with

\[
\boxed{
\operatorname{tr}(Q'_-)=o(N)
}
\]

and essentially full positive-index realization.

This sharpens the multiplicity/depth degeneracy of WI-001. The hard off-line configurations are not just any off-line zeros; they must be **spectrally almost nonnegative after aggregation**. A positive-density family producing a fixed amount of uncancelled negative spectral mass per pair would automatically push the simple-critical lower bound strictly above `2-R(\psi)`.

The remaining escape is real: individual hyperbolic pair blocks can be shallow, and negative directions from different blocks may be masked after pull-back and summation. Therefore `tr(Q'_-)` cannot be replaced by a pair count without a new argument. The finding does not prove a better numerical constant.

## 7. The next discriminating target

The exact remainder identifies a more specific route than "use more moments":

> Prove an unconditional lower bound on the aggregate negative spectral mass of `Q'` for off-line pairs that are not extremely shallow, or prove that cancellation capable of making `tr(Q'_-)=o(N)` itself forces a rigid zero configuration incompatible with another known observable.

The natural scale to test is horizontal depth `|\beta-1/2|\,L`, because the compressed vectors are sampled at bandwidth `L\asymp\log T` and Alpöge--Furman's sharpness example uses depth tending to zero on that scale. A useful next lemma would quantify the negative eigenvalue of one off-line Gabor block as a function of this normalized depth and then determine exactly how much of that blockwise defect can disappear under aggregation.

A theorem of the form

\[
\operatorname{tr}(Q'_-)
\ge c(\eta)\,\#\{\rho:\ |\beta-1/2|\log T\ge\eta\}-o(N)
\]

for any fixed `eta>0`, with `c(eta)>0`, would immediately convert the present identity into a stronger simple-critical-zero proportion unless almost all exceptional off-line zeros lie inside an `o(1/\log T)` horizontal box. This inequality is **not proved here**; it is the precise falsifiable bridge exposed by the remainder calculation.

## 8. Prior art and novelty audit

The ingredients of the matrix identity are classical: spectral positive/negative parts, von Neumann's trace inequality, and completion of the scalar squares used explicitly in Alpöge--Furman Lemma 3.2 and Remark 3.3. Alpöge--Furman already give the exact projection equality model `P=Pi_1`, `Q=2Pi_2`, and Bombieri's earlier work studies the **negative index** of Weil-form truncations when RH fails.

No novelty is claimed for those ingredients, nor for the observation that exact equality requires the projection model. The durable addition for this research line is the retained nonnegative remainder and its zero-counting interpretation: asymptotic sharpness separately kills higher multiplicity charge, aggregate negative spectral mass, and positive-index collapse.

This distinction matters because the prior literature sources currently in `SOURCES.md` control inertia/index, first two moments, or narrow-box hypotheses, but do not supply the missing unconditional lower bound on `tr(Q'_-)`. The remainder therefore converts the vague instruction "characterize the remaining third" into a concrete spectral-mass problem without pretending that the new observable is already arithmetically available.

## 9. Consequence for `weil_inertia`

WI-001 showed that the first-two-moment theorem has explicit extremizers; WI-004 now describes the **stability class** of those extremizers.

A route that hopes to improve the constant while staying close to the same compressed Weil matrix should be tested against the following question first:

\[
\boxed{
\text{Can it force a positive density-scale contribution to }
A,
\ \operatorname{tr}(Q'_-),
\ \text{or }b-n_+(Q')?
}
\]

If not, it still cannot distinguish the near-extremal double/shallow-pair configurations. If yes, the rank--trace machinery itself already converts that extra information into quantitative improvement, with no need to replace the linear-algebra lemma.