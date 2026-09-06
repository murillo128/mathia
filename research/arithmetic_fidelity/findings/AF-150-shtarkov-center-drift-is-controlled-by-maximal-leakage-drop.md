# AF-150 — Shtarkov center drift is controlled by maximal-leakage drop

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `QUANTITATIVE-FIDELITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-149 introduced the finite Shtarkov/NML envelope as a source-natural common reference and observed that its mass contracts under stochastic compression, while warning that the recomputed output NML law need not equal the pushed-forward source NML law. A closer prior-art audit identifies the classical information-theoretic object exactly and makes the nonfunctoriality quantitative.

Let

\[
\mathcal E=(P_i)_{i=1}^m
\]

be a finite experiment on a finite sample space `X`. Define

\[
s(x)=\max_i P_i(x),
\qquad
C_X:=C(\mathcal E)=\sum_x s(x),
\qquad
M_X^*(x)=\frac{s(x)}{C_X}.
\tag{1}
\]

Regard the family as a channel from a model/control label `I` to the observation `X`, with

\[
W(x\mid i)=P_i(x).
\tag{2}
\]

For any full-support prior on `I`, the following quantity is classical:

\[
\boxed{
I_\infty(I;X)
=\log\sum_x\max_iP_i(x)
=\log C_X.
}
\tag{3}
\]

It is simultaneously Sibson mutual information of order infinity and **maximal leakage** from the label to the observation. Moreover,

\[
\boxed{
M_X^*
=\arg\min_Q\max_i D_\infty(P_i\|Q),
}
\tag{4}
\]

so AF-149's normalized Shtarkov envelope is exactly the order-infinity Rényi/Sibson information-radius center of the experiment. Thus AF-149's monotonicity

\[
C(\mathcal EK)\le C(\mathcal E)
\tag{5}
\]

is not merely analogous to data processing: after taking logarithms it **is the classical data-processing inequality for maximal leakage / Sibson order-infinity information**.

Now let `K:X->Y` be any stochastic channel and write

\[
Q_i=P_iK,
\qquad
t(y)=\max_i Q_i(y),
\qquad
C_Y:=C(\mathcal EK)=\sum_y t(y).
\tag{6}
\]

There are two canonical-looking output references:

- the **propagated source center**
  \[
  q:=M_X^*K,
  \tag{7}
  \]
- the **recomputed output center**
  \[
  r:=M_Y^*,
  \qquad
  r(y)=\frac{t(y)}{C_Y}.
  \tag{8}
  \]

Define the pushed source envelope

\[
\widetilde t(y):=\sum_x s(x)K(y\mid x).
\tag{9}
\]

Since

\[
t(y)=\max_i\sum_xP_i(x)K(y\mid x)
\le
\sum_x\max_iP_i(x)K(y\mid x)
=\widetilde t(y),
\tag{10}
\]

we have `C_Y<=C_X`. Put

\[
\alpha:=\frac{C_Y}{C_X}\in(0,1].
\tag{11}
\]

Then the propagated and recomputed centers satisfy the exact pointwise domination

\[
\boxed{
q(y)\ge \alpha r(y)
\quad\text{for every }y.
}
\tag{12}
\]

If `C_Y<C_X`, define

\[
u(y):=\frac{\widetilde t(y)-t(y)}{C_X-C_Y}.
\tag{13}
\]

The numerator is nonnegative and sums to `C_X-C_Y`, so `u` is a probability law and

\[
\boxed{
q=\alpha r+(1-\alpha)u.
}
\tag{14}
\]

Thus the failure of the Shtarkov center to commute with compression has an exact mixture decomposition. In particular,

\[
\boxed{
\|q-r\|_{\rm TV}
=(1-\alpha)\|u-r\|_{\rm TV}
\le 1-\frac{C_Y}{C_X},
}
\tag{15}
\]

and the directional information divergences obey

\[
\boxed{
D_\infty(r\|q)
\le
\log\frac{C_X}{C_Y},
}
\tag{16}
\]

\[
\boxed{
D_{\rm KL}(r\|q)
\le
\log\frac{C_X}{C_Y},
}
\tag{17}
\]

and

\[
\boxed{
\chi^2(r\|q)
\le
\frac{C_X}{C_Y}-1.
}
\tag{18}
\]

The logarithmic budget in `(16)--(17)` is exactly the **maximal-leakage drop**

\[
\Delta_\infty
:=I_\infty(I;X)-I_\infty(I;Y)
=\log\frac{C_X}{C_Y}.
\tag{19}
\]

For a chain

\[
\mathcal E_0\xrightarrow{K_1}\mathcal E_1
\xrightarrow{K_2}\cdots
\xrightarrow{K_n}\mathcal E_n,
\]

with `C_j=C(E_j)`, the scalar reset budgets telescope exactly:

\[
\sum_{j=1}^n\log\frac{C_{j-1}}{C_j}
=\log\frac{C_0}{C_n}.
\tag{20}
\]

Applying `(12)` to the composite channel also gives the path-independent endpoint domination

\[
\boxed{
M_n^*
\le
\frac{C_0}{C_n}
\,M_0^*K_1\cdots K_n
}
\tag{21}
\]

pointwise. Hence the same order-infinity information loss that contracts under the forward channel controls how far the newly canonicalized center can move *in the reverse-likelihood direction* from the source center propagated with its provenance.

However, this does **not** rescue stagewise recanonicalization for AF-145's compositional recovery architecture. In the private-label family of AF-146, the actual experiment recovery deficiency tends to zero while the propagated-versus-recomputed Shtarkov centers remain order-one apart and asymptotically saturate the bounds above. Therefore approximate recoverability of the declared family does not imply approximate functoriality of its Shtarkov/Rényi center.

## Derivation

### Shtarkov mass is maximal leakage and its law is the order-infinity center

Let `I` have any prior `pi_i>0` on all model labels and let `X|I=i` have law `P_i`. The order-infinity Sibson mutual information admits the variational form

\[
I_\infty(I;X)
=\inf_Q D_\infty(P_{IX}\|P_I\otimes Q).
\tag{22}
\]

Because the prior factors cancel inside the likelihood ratio,

\[
D_\infty(P_{IX}\|P_I\otimes Q)
=\log\max_{i,x: P_i(x)>0}\frac{P_i(x)}{Q(x)}.
\tag{23}
\]

Therefore

\[
I_\infty(I;X)
=\log\inf_Q\max_i\left\|\frac{dP_i}{dQ}\right\|_\infty.
\tag{24}
\]

AF-149 already proved directly that the infimum in `(24)` is `C_X` and that the unique minimizer is `M_X^*=s/C_X`. This proves `(3)--(4)` without importing any new algebra.

The same discrete quantity is the closed-form expression for maximal leakage. Consequently the operational interpretation of `log C_X` is stronger than the generic word "complexity": it is the largest multiplicative gain, after observing `X`, in optimally guessing an arbitrary randomized function of the experiment label `I`.

Under post-processing `Y` generated by `K`, maximal leakage satisfies data processing,

\[
I_\infty(I;Y)\le I_\infty(I;X),
\]

which is exactly `(5)` after exponentiating. AF-149's elementary envelope proof is therefore a finite direct proof of this classical order-infinity DPI for the channel family at hand.

### Exact propagated-versus-recomputed center decomposition

From `(1)` and `(9)`,

\[
q(y)
=(M_X^*K)(y)
=\frac{\widetilde t(y)}{C_X}.
\tag{25}
\]

Meanwhile

\[
\alpha r(y)
=\frac{C_Y}{C_X}\frac{t(y)}{C_Y}
=\frac{t(y)}{C_X}.
\tag{26}
\]

Subtracting `(26)` from `(25)` gives

\[
q(y)-\alpha r(y)
=\frac{\widetilde t(y)-t(y)}{C_X}
\ge0.
\tag{27}
\]

The total mass of the right-hand side is

\[
\frac{C_X-C_Y}{C_X}=1-\alpha.
\]

Normalizing the difference yields `u` from `(13)` and proves `(14)`. If `C_X=C_Y`, equation `(27)` is a nonnegative vector of total mass zero, so `q=r`; thus zero maximal-leakage drop is sufficient for exact center commutation. The converse is false: a channel can reduce `C` while moving the pushed and recomputed centers by zero if the lost envelope mass is proportional to the surviving output envelope.

Equation `(15)` follows immediately from

\[
q-r=(1-\alpha)(u-r).
\]

For `(16)`, `(12)` implies on the support of `r`

\[
\frac{r(y)}{q(y)}\le\frac1\alpha,
\]

so

\[
D_\infty(r\|q)
\le -\log\alpha.
\]

The same pointwise bound gives

\[
D_{\rm KL}(r\|q)
=\sum_y r(y)\log\frac{r(y)}{q(y)}
\le -\log\alpha,
\]

proving `(17)`. Finally,

\[
\begin{aligned}
\chi^2(r\|q)
&=\sum_y\frac{r(y)^2}{q(y)}-1\\
&\le\frac1\alpha\sum_y r(y)-1\\
&=\frac1\alpha-1,
\end{aligned}
\]

which is `(18)`.

These estimates are deliberately directional. The pushed source center `q` contains envelope mass inherited from distinctions that the output family may no longer need; the scalar ratio `C_X/C_Y` alone does not give a comparable universal bound on `D_\infty(q\|r)`.

### Private-label family makes center drift order one while recovery becomes exact

Return to AF-146's family

\[
P_i=(1-\rho)\delta_0+\rho\delta_i,
\qquad i=1,\ldots,m,
\tag{28}
\]

and the channel `K_m` that fixes `0` and maps every private symbol `1,...,m` to one output symbol `*`. AF-149 computed

\[
C_X=1+(m-1)\rho.
\tag{29}
\]

All compressed laws are identical,

\[
Q_i=(1-\rho)\delta_0+\rho\delta_*,
\]

so

\[
C_Y=1,
\qquad
r=(1-\rho)\delta_0+\rho\delta_*.
\tag{30}
\]

The propagated source center is

\[
q
=\frac{1-\rho}{C_X}\delta_0
+\frac{m\rho}{C_X}\delta_*.
\tag{31}
\]

Here `alpha=1/C_X` and `(14)` is exact with

\[
u=\delta_*.
\tag{32}
\]

Therefore

\[
\boxed{
\|q-r\|_{\rm TV}
=\left(1-\frac1{C_X}\right)(1-\rho).
}
\tag{33}
\]

Moreover, at the shared symbol `0`,

\[
\frac{r(0)}{q(0)}=C_X,
\]

so the order-infinity bound is attained exactly:

\[
\boxed{
D_\infty(r\|q)=\log C_X=\Delta_\infty.
}
\tag{34}
\]

The other divergences are also explicit:

\[
D_{\rm KL}(r\|q)
=\log C_X-\rho\log m,
\tag{35}
\]

and

\[
\chi^2(r\|q)
=C_X\left(1-\rho+\frac\rho m\right)-1.
\tag{36}
\]

At AF-146's separating scale `rho=1/m`,

\[
C_X=2-\frac1m,
\]

while the minimax experiment-recovery deficiency is

\[
\delta_{\rm rec}
=\frac1m\left(1-\frac1m\right)
\longrightarrow0.
\tag{37}
\]

Nevertheless,

\[
\|q-r\|_{\rm TV}
=\frac{(m-1)^2}{m(2m-1)}
\longrightarrow\frac12,
\tag{38}
\]

\[
D_\infty(r\|q)
\longrightarrow\log2,
\qquad
D_{\rm KL}(r\|q)
\longrightarrow\log2,
\tag{39}
\]

and

\[
\chi^2(r\|q)\longrightarrow1.
\tag{40}
\]

Thus the family becomes arbitrarily well recoverable in Le Cam/TV terms while source-propagated and output-recanonicalized Shtarkov centers stay macroscopically different. This decisively rules out the hope that **approximate experiment sufficiency by itself** makes the NML/Rényi center approximately functorial.

## Prior art and novelty assessment

The main identification is classical and materially sharpens the prior-art classification of AF-149.

- Robin Sibson, **“Information Radius,”** *Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete* 14, 149–160 (1969), DOI `10.1007/BF00537520`. Sibson introduced the information-radius family underlying the order-`alpha` mutual information used here.
- Yuri M. Shtarkov, **“Universal Sequential Coding of Single Messages,”** *Problems of Information Transmission* 23(3), 175–186 (1987). The normalized maximized-likelihood/Shtarkov law and minimax pointwise regret are classical.
- Ibrahim Issa, Aaron B. Wagner, and Sudeep Kamath, **“An Operational Approach to Information Leakage,”** *IEEE Transactions on Information Theory* 66(3), 1625–1657 (2020), DOI `10.1109/TIT.2019.2962804`, arXiv:`1807.07878`. They identify maximal leakage with Sibson mutual information of order infinity, give the discrete closed form `log sum_y max_x P(y|x)`, establish data processing, and explicitly connect this order-infinity quantity to the Shtarkov sum from universal compression.
- Barış Nakiboğlu, **“The Rényi Capacity and Center,”** *IEEE Transactions on Information Theory* 65(2), 841–860 (2019), DOI `10.1109/TIT.2018.2861002`. This develops general Rényi capacity/radius/center theory and provides the appropriate classical context for calling `M_X^*` an order-infinity information center.

Accordingly, **no novelty is claimed** for `(3)--(5)`, for the minimax center interpretation `(4)`, or for maximal-leakage data processing. Those are prior art that AF-149 had not named explicitly.

The Arithmetic Fidelity contribution is the exact specialization to the line's propagate-versus-recanonicalize question: the elementary decomposition `(14)`, its directional drift bounds `(15)--(18)`, and the AF-146 private-label separation `(37)--(40)` showing that center drift can remain order one while whole-experiment recovery deficiency vanishes. The literature search covered Shtarkov/NML, maximal leakage/Sibson information, Rényi centers, data processing, and post-processing/center terminology. I did not locate this exact finite decomposition or this private-label comparison in the inspected sources, but the derivation is elementary and **is not presented as a novelty claim**.

## Boundary conditions and falsification tests

1. **The new classical identification changes interpretation, not the formulas.** AF-149's `C(E)` and `M_*` were correct. They should now be read specifically as exponentiated maximal leakage / order-infinity information radius and its center, rather than as an isolated NML complexity construction.

2. **Leakage drop controls reset drift only in one direction.** Equations `(16)--(18)` bound divergence of the recomputed center `r` relative to the propagated source center `q`. They do not provide a symmetric metric equivalence or a bound on `D_\infty(q\|r)` from `C_X/C_Y` alone.

3. **The bounds are upper bounds, not an exact metric identity.** A large maximal-leakage drop can coexist with `q=r`; for example, distinct source labels can be sent through a channel with identical output rows. The private-label family shows that the same bounds can also be asymptotically tight. The scalar drop therefore budgets possible recanonicalization motion but does not determine it.

4. **Center stability is not recovery stability.** Equations `(37)--(40)` are the decisive control. Vanishing experiment-recovery deficiency does not force the source and output order-infinity centers to approach each other. Any theorem asserting such continuity needs additional structural hypotheses beyond approximate sufficiency.

5. **Reset budgets do not restore AF-145's exact Bayes composition.** AF-145 composes because one reference is physically propagated through every forward channel. Replacing that reference by a newly optimized center changes the reference joint law. A small bound on center drift may support a later perturbative theorem under extra regularity, but no such reverse-kernel stability theorem is claimed here.

6. **The control label is auxiliary but exact.** The maximal-leakage interpretation treats the experiment index `i` as the input alphabet of a channel. It does not require a meaningful Bayesian prior: order infinity depends only on which labels have positive support. That is precisely why it matches AF-149's prior-free envelope.

7. **Finite-space scope remains load-bearing.** The normalized Shtarkov envelope is automatic here. Continuous or noncompact model classes can have infinite Shtarkov integral, and their Rényi-center theory requires separate existence hypotheses.

8. **None of this is yet arithmetic.** Maximal leakage supplies a mature information-theoretic language for one abstract fidelity mechanism. An arithmetic application must still identify a mathematically forced control family and compression for which preserving label-discrimination geometry is relevant to the arithmetic property under study.

## Arithmetic Fidelity consequence

AF-149's source-natural reference is no longer an isolated candidate: it sits at the intersection of **universal coding, Rényi information radius, and operational guessing leakage**. This is useful because the line now inherits a substantial established theory instead of rebuilding the scalar `C(E)` and its data-processing behavior from scratch.

The more important negative result is structural. There are now three distinct notions that must not be conflated:

\[
\text{recoverability of the experiment},
\qquad
\text{loss of order-}\infty\text{ label information},
\qquad
\text{stability of the canonical information center}.
\]

They can separate sharply. In particular, the private-label family has vanishing recovery deficiency but order-one maximal-leakage drop and order-one center reset drift. Therefore a source-natural canonicalization rule cannot be made compositional merely by recomputing it after each compression, even when the compression is almost reversible on the declared family.

The productive frontier is consequently narrower than AF-149's final question. One should now ask for **additional hypotheses under which information-center recanonicalization is stable enough to perturb AF-145's propagated-reference reverse**, or else prove that any source-natural center with comparable minimax domination must face a similar discontinuity. The first useful conditions to test are lower-density/overlap assumptions, bounded likelihood-ratio geometry, and restrictions preventing the channel from merging many model-specific envelope maximizers into the same output point.