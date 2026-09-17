# MC-352 — Source-edge likelihood-ratio stability cannot coexist with bounded-energy dephasing

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-351` closes the lower-bound side of the transcript problem: bounded-energy reciprocal dephasing forces an extensive aggregate Jeffreys/KL budget across the natural source graph. The remaining upper-bound question is which analytic regularity currencies can actually price that budget.

A source-local **likelihood-ratio stability** condition does so directly, without assuming a raw-query model, a finite transcript alphabet, Gaussian noise, or a Euclidean realization.

For every admissible source state `x`, let

\[
P_x:=\operatorname{Law}(Y\mid X=x)
\]

be the complete transcript law. For a natural source edge `e={x,x'}`, define the edge log-likelihood radius

\[
\varepsilon_e
:=
\operatorname*{ess\,sup}_{P_x+P_{x'}}
\left|\log\frac{dP_x}{dP_{x'}}\right|,
\tag{1}
\]

with `epsilon_e=+infinity` when the two laws are not mutually absolutely continuous. Put

\[
\psi(u):=u\tanh(u/2),
\qquad u\ge0.
\tag{2}
\]

For the symmetrized edge divergence used in `MC-348`--`MC-351`,

\[
b_e
:=\frac12\left(D(P_x\|P_{x'})+D(P_{x'}\|P_x)\right),
\]

one has the sharp two-row bound

\[
\boxed{b_e\le \psi(\varepsilon_e).}
\tag{3}
\]

The small-stability regime is quadratic:

\[
\psi(u)=\frac{u^2}{2}+O(u^4),
\qquad
\psi(u)\le\frac{u^2}{2}.
\tag{4}
\]

Thus the `MC-351` lower bound immediately becomes a likelihood-ratio resource theorem.

### Even rank

Let

\[
S=\{-1,+1\}^R\setminus\{\mathbf1\},
\qquad
m=2^R-1,
\]

and let `E_1` be the surviving Hamming-one edges. Define

\[
\mathfrak L_1
:=\frac2m\sum_{e\in E_1}\psi(\varepsilon_e).
\tag{5}
\]

Then

\[
\boxed{
I(X;Y)\le\frac12\mathfrak L_1+\Gamma_R,
}
\tag{6}
\]

where `Gamma_R<2 log 2` is the puncture defect of `MC-351`. Consequently, using the global dephasing inequality of `MC-340`,

\[
\boxed{
\delta(W)
\ge
\left(
1-\sqrt{\mathcal E(W)}
\sqrt{
\frac1{m^2}
+\frac{\mathfrak L_1}{R}
+\frac{2(\Gamma_R+\operatorname{TC}(X))}{R}
}
\right)_+.
}
\tag{7}
\]

If every surviving edge satisfies the common likelihood-ratio ceiling

\[
\varepsilon_e\le\varepsilon_R,
\]

then, writing

\[
\Lambda_R:=\frac{2^R-2}{2^R-1},
\]

one has

\[
\frac{\mathfrak L_1}{R}
\le
\Lambda_R\psi(\varepsilon_R),
\tag{8}
\]

because `|E_1|=mR Lambda_R/2`. Hence bounded coefficient energy together with `epsilon_R -> 0` forces

\[
\boxed{\delta(W)\to1.}
\tag{9}
\]

More quantitatively, if

\[
\mathcal E(W)\le C,
\qquad
\delta(W)\le1-\eta,
\qquad \eta>0,
\]

then

\[
\boxed{
\Lambda_R\psi(\varepsilon_R)
\ge
\frac{\eta^2}{C}
-\frac1{m^2}
-\frac{2(\Gamma_R+\operatorname{TC}(X))}{R}.
}
\tag{10}
\]

Since `Lambda_R -> 1`, `Gamma_R=O(1)` and `TC(X)=o(1)` for even rank,

\[
\liminf_{R\to\infty}\psi(\varepsilon_R)
\ge\frac{\eta^2}{C}.
\tag{11}
\]

Using `(4)`, a simpler but nonsharp consequence is

\[
\boxed{
\liminf_{R\to\infty}\varepsilon_R
\ge\frac{\sqrt2\,\eta}{\sqrt C}.
}
\tag{12}
\]

So fixed nontrivial bounded-energy dephasing requires a **constant source-edge log-likelihood contrast**. An asymptotically source-edge-indistinguishable transcript cannot do it.

### Odd rank

For odd `R>=3`, condition on the nonexceptional parity source as in `MC-351`. Let

\[
M=2^{R-1}-1
\]

and let `E_2` be the surviving pair-flip edges. Define

\[
\mathfrak L_2
:=
\frac{2\Lambda_R}{M(R-1)}
\sum_{e\in E_2}\psi(\varepsilon_e).
\tag{13}
\]

Then `MC-351` and `(3)` give

\[
I(X;Y)
\le
\frac{R-1}{R}\mathfrak L_2
+h(\Lambda_R)
+\Lambda_R\Gamma_{R-1}.
\tag{14}
\]

Therefore

\[
\boxed{
\delta(W)
\ge
\left(
1-\sqrt{\mathcal E(W)}
\sqrt{
\frac1{m^2}
+\frac{2(R-1)}{R^2}\mathfrak L_2
+\frac{2[h(\Lambda_R)+\Lambda_R\Gamma_{R-1}+\operatorname{TC}(X)]}{R}
}
\right)_+.
}
\tag{15}
\]

If every pair-flip edge has `epsilon_e<=epsilon_R`, then the exact pair-edge count from `MC-351` gives

\[
\mathfrak L_2
\le
\frac R2\Lambda_R\Lambda_{R-1}\psi(\varepsilon_R),
\tag{16}
\]

and hence the coefficient of `psi(epsilon_R)` inside `(15)` is

\[
\frac{R-1}{R}\Lambda_R\Lambda_{R-1}\to1.
\tag{17}
\]

Thus `(9)` holds for odd rank as well, and the fixed-dephasing consequence has the same asymptotic form `(11)`--`(12)`.

At exact unit-energy dephasing, `MC-340` forces exact source recovery and `MC-351` gives infinite edge KL. In particular no finite likelihood-ratio ceiling can survive: neighboring source states must become statistically singular at the exact endpoint.

No estimate for `M(x)` follows. The advance is a channel-free upper-price theorem for the exact KL currency exposed by `MC-351`: the missing analytic ingredient can now be stated as a bound on how strongly neighboring reciprocal source states can change the **entire transcript likelihood**, not merely its forward metric position.

## 1. Bounded likelihood ratio sharply bounds Jeffreys divergence

Fix two probability laws `P,Q` with

\[
e^{-u}
\le
r:=\frac{dP}{dQ}
\le
e^u
\qquad Q\text{-a.s.}
\tag{18}
\]

Then `E_Q r=1`, and

\[
D(P\|Q)+D(Q\|P)
=
\mathbf E_Q[(r-1)\log r].
\tag{19}
\]

The function

\[
\phi(r):=(r-1)\log r
\]

is convex on `(0,infinity)` because

\[
\phi''(r)=\frac1r+\frac1{r^2}>0.
\tag{20}
\]

Among probability laws for `r` supported on `[e^{-u},e^u]` with mean one, the expectation of a convex function is maximized by placing all mass at the two endpoints. The mean-one weights are

\[
q=\frac{e^u-1}{e^u-e^{-u}},
\qquad
1-q=\frac{1-e^{-u}}{e^u-e^{-u}}.
\tag{21}
\]

Substitution gives

\[
\mathbf E_Q\phi(r)
\le
2u\tanh(u/2).
\tag{22}
\]

Dividing by two proves `(3)`. Equality is attained by the corresponding binary two-row channel, equivalently the symmetric randomized-response extremizer after relabeling outputs.

The elementary inequality `tanh(v)<=v` proves the second part of `(4)`; the Taylor expansion gives the first.

This is exactly the regularity direction that total variation, bounded range, or one-sided forward Lipschitz control could not provide in `MC-342`: a two-sided likelihood-ratio bound prevents information from being hidden in arbitrarily rare, arbitrarily decisive transcript events.

## 2. Even rank: MC-351 turns local likelihood stability into a global capacity ceiling

Equation `(3)` implies

\[
\mathfrak J_1
:=\frac2m\sum_{e\in E_1}b_e
\le\mathfrak L_1.
\tag{23}
\]

But `MC-351` proves

\[
I(X;Y)
\le\frac12\mathfrak J_1+\Gamma_R.
\tag{24}
\]

Combining `(23)`--`(24)` gives `(6)`. Substitution into equation (1) of `MC-340`,

\[
\rho^2
\le
\frac1{m^2}
+\frac2R\bigl(I(X;Y)+\operatorname{TC}(X)\bigr),
\tag{25}
\]

then yields

\[
\rho^2
\le
\frac1{m^2}
+\frac{\mathfrak L_1}{R}
+\frac{2(\Gamma_R+\operatorname{TC}(X))}{R}.
\tag{26}
\]

The dephasing inequality of `MC-338`,

\[
\delta(W)\ge(1-\rho\sqrt{\mathcal E(W)})_+,
\tag{27}
\]

proves `(7)`.

Under the common ceiling `epsilon_R`, equation `(8)` follows from the surviving-edge count. If `E(W)<=C` and `delta(W)<=1-eta`, equations `(7)`--`(8)` force `(10)`. This proves the asymptotic statements.

The nonuniform form `(5)` is useful: a candidate architecture need not have one global stability constant. What matters is the source-edge average of `psi(epsilon_e)`. Large likelihood contrast may be concentrated on selected directions, but the total weighted budget must still be extensive if bounded-energy dephasing is to survive.

## 3. Odd rank: pair-flip likelihood stability pays the same asymptotic tariff

For odd rank, `MC-351` proves

\[
\mathfrak J_2
\ge
\frac{R}{R-1}
\left[
I(X;Y)-h(\Lambda_R)-\Lambda_R\Gamma_{R-1}
\right]_+.
\tag{28}
\]

Since `mathfrak J_2<=mathfrak L_2`, equation `(28)` rearranges to `(14)`. Inserting `(14)` into `(25)` and then `(27)` gives `(15)`.

The conditioned parity source has

\[
|E_2|
=
\frac{M\Lambda_{R-1}}2\binom R2.
\tag{29}
\]

Applying the common edge ceiling in `(13)` therefore gives `(16)`, and `(17)` follows. The odd-rank parity constraint changes only bounded defects and finite-rank constants; it does not create an asymptotic likelihood-stability loophole.

## 4. Pure edge indistinguishability is the load-bearing notion

The likelihood-ratio condition `(1)` is mathematically the same two-row constraint used by **pure local differential privacy** when the neighboring inputs are the source-edge endpoints. Privacy semantics are not being asserted here; the language is useful because that literature has studied exactly the utility/divergence capacity of channels under bounded likelihood ratios.

The distinction between a pure likelihood-ratio ceiling and weaker forward metrics is essential. A small total-variation, Hellinger, Wasserstein, or Euclidean displacement does not upper-bound KL without additional reverse regularity. This is the statistical analogue of the dyadic inverse-conditioning obstruction in `MC-342`.

Likewise, replacing `(1)` by an approximate `(epsilon,delta)` likelihood condition with any positive exceptional mass does **not** by itself bound Jeffreys divergence: an arbitrarily rare transcript event may be singular under the neighboring row and make KL infinite. Any arithmetic use of an approximate condition must separately control those exceptional likelihood tails.

Thus the new resource is not “smoothness” in a generic sense. It is exclusion of rare transcript events whose probability ratio changes without bound under a single natural source move.

## Prior art and novelty boundary

The likelihood-ratio mechanism is classical and no novelty is claimed for it.

Dwork, McSherry, Nissim and Smith, *Calibrating Noise to Sensitivity in Private Data Analysis*, TCC 2006, introduced the now-standard pure differential-privacy likelihood-ratio control for neighboring inputs. The original paper is available at `https://www.iacr.org/archive/tcc2006/38760266/38760266.pdf`.

Kairouz, Oh and Viswanath, *Extremal Mechanisms for Local Differential Privacy*, JMLR **17** (2016), 1--51, arXiv `1407.1338`, studies utility maximization under local differential-privacy likelihood-ratio constraints and proves staircase extremality for broad classes of information-theoretic utilities including `f`-divergences. Binary/randomized-response mechanisms appear as extremal mechanisms in the corresponding regimes. The elementary two-row calculation `(18)`--`(22)` is included here so that the exact normalization needed by the Mathia edge budget is independently checkable.

A targeted prior-art audit on 17 September 2026 found no basis for claiming novelty for pure likelihood-ratio indistinguishability, its relation to local differential privacy, binary extremizers, or divergence control under a bounded likelihood ratio. The durable Mathia delta is the exact composition with the punctured reciprocal source laws and `MC-340`/`MC-351`: a source-edge likelihood-stability budget now upper-prices the same aggregate KL quantity that bounded-energy dephasing lower-prices.

## Boundaries and falsification tests

- **The condition is on the complete transcript law.** Bounding likelihood ratios for one intermediate statistic is insufficient unless the entire admitted transcript factors through that statistic.
- **Even and odd rank use different natural edges.** Hamming-one edges are used for the even punctured cube; parity-preserving pair flips are used for odd rank. Treating nonexistent odd-rank one-bit neighbors as admissible would be a source-model error.
- **Pure two-sided absolute continuity is load-bearing.** Positive exceptional mass can hide infinite KL, so approximate likelihood control needs an additional tail-divergence estimate.
- **The theorem is an admission test, not an arithmetic regularity theorem.** Nothing here proves that a natural Möbius/endpoint transcript has `epsilon_e=o(1)` or any other favorable likelihood ceiling.
- **Large likelihood ratio is necessary, not sufficient.** A transcript may spend the required source-edge discrimination budget and still fail to produce useful coefficient cancellation.
- **Re-encoding cannot evade the statement.** `epsilon_e` depends only on the probability laws `P_x,P_x'`, not on coordinates assigned to transcript outcomes. Any measurable bijective reparameterization leaves the likelihood ratios and KL unchanged.
- **Deterministic injective transcripts sit at the singular endpoint.** They have infinite edge likelihood radius rather than contradicting the theorem; this is exactly the inverse-precision phenomenon exposed by `MC-342` before noise or regularity is imposed.
- **No RH input is used.** The conclusion is finite and information-theoretic; it proves no global Möbius cancellation, zero-free region, or estimate for `M(x)`.

## Consequence for the research line

The `MC-351` frontier is now two-sided at the abstract channel level. Bounded-energy dephasing forces an extensive source-edge KL budget; `MC-352` shows that a pure source-edge likelihood-ratio stability theorem would upper-bound that budget in the exact same currency. In particular, any canonical arithmetic architecture whose neighboring reciprocal source states become asymptotically indistinguishable in log-likelihood ratio is automatically too stable to support fixed nontrivial bounded-energy dephasing.

The remaining arithmetic question is correspondingly sharper: **can the actual Möbius/endpoint observation law be shown, from coefficient size, analytic bandwidth, precision, or another natural resource, to have small source-edge likelihood ratios or controlled exceptional likelihood tails?** Forward metric regularity is insufficient; the needed estimate is genuinely about statistical reverse sensitivity of the full transcript law.