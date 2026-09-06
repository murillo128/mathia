# AF-147 — Common-reference KL loss gives recovery with logarithmic family dilution

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-INFORMATION-THEORETIC-SPECIALIZATION`, `QUANTITATIVE-FIDELITY`, `RECOVERY-UPPER-BOUND`, `NEGATIVE/OBSTRUCTION`, `FAMILY-COMPLEXITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-144 shows that one common reference mixture turns Pearson chi-square data-processing loss into a simultaneous recovery certificate for an entire finite experiment, while AF-146 shows that the optimized Pearson profile is not quantitatively calibrated to Le Cam recovery when the control family grows: its family-size penalty can be linear in the number of alternatives.

Relative entropy gives a strictly better calibrated version of the same common-reference mechanism, but it does not remove the family-complexity obstruction entirely.

Let

\[
\mathcal E=(P_\theta)_{\theta\in\Theta}
\]

be a finite statistical experiment on a finite space `X`, let

\[
K:X\rightsquigarrow Y,
\qquad
Q_\theta=P_\theta K,
\]

and choose a full-support prior

\[
\lambda\in\Delta^\circ(\Theta).
\]

Define the common mixtures

\[
M_\lambda=\sum_\theta\lambda_\theta P_\theta,
\qquad
N_\lambda=M_\lambda K
=\sum_\theta\lambda_\theta Q_\theta,
\tag{1}
\]

and the same Bayes reverse used in AF-144,

\[
R_\lambda(x\mid y)
=
\frac{M_\lambda(x)K(y\mid x)}{N_\lambda(y)}
\qquad(N_\lambda(y)>0).
\tag{2}
\]

Using natural logarithms, define the memberwise common-reference KL loss

\[
\eta_\theta(\lambda)
:=
D(P_\theta\|M_\lambda)
-
D(Q_\theta\|N_\lambda)
\ge0.
\tag{3}
\]

Then the following hold.

1. If
   \[
   J_\theta(x,y)=P_\theta(x)K(y\mid x)
   \]
   is the true source/output joint law and
   \[
   \widetilde J_{\theta,\lambda}(x,y)
   =Q_\theta(y)R_\lambda(x\mid y),
   \]
   is the joint law obtained by retaining the correct output law and replacing the source conditional by the common Bayes reverse, then
   \[
   \boxed{
   \eta_\theta(\lambda)
   =D(J_\theta\|\widetilde J_{\theta,\lambda}).
   }
   \tag{4}
   \]

2. Marginalizing `(4)` back to `X` and applying Pinsker gives the simultaneous one-kernel recovery bound
   \[
   \boxed{
   2\,
   \|P_\theta-Q_\theta R_\lambda\|_{\rm TV}^2
   \le
   \eta_\theta(\lambda)
   }
   \tag{5}
   \]
   for every `theta`.

3. Therefore the one-sided recovery deficiency from AF-126 satisfies
   \[
   \boxed{
   \delta_{\rm rec}(K;\mathcal E)
   \le
   \sqrt{\frac12\max_\theta\eta_\theta(\lambda)}.
   }
   \tag{6}
   \]
   Defining
   \[
   \Gamma_{\rm KL}(K;\mathcal E)
   :=
   \inf_{\lambda\in\Delta^\circ(\Theta)}
   \max_\theta\eta_\theta(\lambda),
   \tag{7}
   \]
   gives
   \[
   \boxed{
   2\,\delta_{\rm rec}(K;\mathcal E)^2
   \le
   \Gamma_{\rm KL}(K;\mathcal E).
   }
   \tag{8}
   \]

4. The zero boundary is exact:
   \[
   \boxed{
   \Gamma_{\rm KL}(K;\mathcal E)=0
   \iff
   \delta_{\rm rec}(K;\mathcal E)=0
   \iff
   K\text{ is sufficient for }\mathcal E.
   }
   \tag{9}
   \]

5. If `\Theta` is itself sampled from `\lambda` and the joint model is
   \[
   \Theta\longrightarrow X\longrightarrow Y,
   \]
   then the prior-weighted KL loss is exactly the conditional mutual information:
   \[
   \boxed{
   \sum_\theta\lambda_\theta\eta_\theta(\lambda)
   =I_\lambda(\Theta;X\mid Y)
   =I_\lambda(\Theta;X)-I_\lambda(\Theta;Y).
   }
   \tag{10}
   \]
   Thus the common Bayes reconstruction is the classical conditional-independence projection that replaces the true `Theta-X-Y` joint by one satisfying `Theta-Y-X` while preserving the `(Theta,Y)` marginal and the reference conditional `X|Y`.

This positive certificate is dimension-free in the forward direction: neither `(5)` nor `(8)` contains an explicit factor depending on `|Theta|`.

However, AF-146's private-label family gives an exact converse obstruction. For

\[
P_i=(1-\rho)\delta_0+\rho\delta_i,
\qquad i=1,\ldots,m,
\tag{11}
\]

and the deterministic compression that sends every private label `i>=1` to one symbol `*`, AF-146 already proves

\[
\delta_{\rm rec}
=
\rho\left(1-\frac1m\right).
\tag{12}
\]

For the KL profile one has exactly

\[
\boxed{
\Gamma_{\rm KL}
=
\rho\log m.
}
\tag{13}
\]

The optimizer is again the uniform prior, and its Bayes reverse is the same minimax-optimal recovery kernel identified in AF-146. Consequently

\[
\boxed{
\Gamma_{\rm KL}
=
\frac{\log m}{1-1/m}\,
\delta_{\rm rec}.
}
\tag{14}
\]

This sharply separates KL from Pearson chi-square. Under the AF-146 scaling `rho_m=1/m`,

\[
\Gamma_{\rm KL}
=\frac{\log m}{m}\to0,
\]

so KL removes the specific order-one Pearson obstruction from that scaling. But taking instead

\[
\rho_m=\frac1{\log m}
\qquad(m\ge3)
\tag{15}
\]

gives

\[
\delta_{\rm rec}
=
\frac{1-1/m}{\log m}
\longrightarrow0,
\qquad
\Gamma_{\rm KL}=1.
\tag{16}
\]

Hence there is still no family-size-independent modulus `omega(t)->0` as `t->0` such that every finite experiment and stochastic compression obey

\[
\Gamma_{\rm KL}(K;\mathcal E)
\le
\omega\!\left(\delta_{\rm rec}(K;\mathcal E)\right).
\tag{17}
\]

The family-size penalty has improved from the Pearson factor `m` in AF-146 to the KL factor `log m`, but it has not disappeared.

## Derivation

### KL loss is exactly divergence from the Bayes-recovered joint

Fix `lambda` and abbreviate `M=M_lambda`, `N=N_lambda`, and `R=R_lambda`. Full support of `lambda` makes `M` dominate every `P_theta` and `N` dominate every `Q_theta`.

For every `(x,y)` in the support of `J_theta`,

\[
\frac{J_\theta(x,y)}{\widetilde J_{\theta,\lambda}(x,y)}
=
\frac{P_\theta(x)K(y\mid x)}
{Q_\theta(y)M(x)K(y\mid x)/N(y)}
=
\frac{P_\theta(x)}{M(x)}
\frac{N(y)}{Q_\theta(y)}.
\tag{18}
\]

Taking `J_theta` expectation of the logarithm gives

\[
\begin{aligned}
D(J_\theta\|\widetilde J_{\theta,\lambda})
&=
\sum_xP_\theta(x)
\log\frac{P_\theta(x)}{M(x)}
+
\sum_yQ_\theta(y)
\log\frac{N(y)}{Q_\theta(y)}\\
&=
D(P_\theta\|M)-D(Q_\theta\|N)\\
&=
\eta_\theta(\lambda),
\end{aligned}
\tag{19}
\]

which proves `(4)`. Equivalently, the relative-entropy chain rule gives

\[
\eta_\theta(\lambda)
=
\sum_yQ_\theta(y)
D\!\left(
P_\theta(\cdot\mid y)
\middle\|
R_\lambda(\cdot\mid y)
\right).
\tag{20}
\]

This is stronger structural information than data processing alone: the scalar loss is exactly the conditional mismatch between the member-specific posterior source law and the one common posterior generated by the reference mixture.

### Marginalization plus Pinsker gives one common reverse channel

The `X` marginal of `J_theta` is `P_theta`; the `X` marginal of `widetilde J` is `Q_theta R_lambda`. Relative entropy contracts under marginalization, so `(4)` yields

\[
D(P_\theta\|Q_\theta R_\lambda)
\le
\eta_\theta(\lambda).
\tag{21}
\]

Pinsker's inequality in the convention

\[
\|P-S\|_{\rm TV}
=\frac12\|P-S\|_1
\]

states

\[
\|P-S\|_{\rm TV}^2
\le
\frac12D(P\|S).
\tag{22}
\]

Combining `(21)--(22)` proves `(5)`, and then `(6)--(8)` follow by taking the worst member, allowing the best reverse channel in the definition of deficiency, and finally optimizing the reference prior.

The exact-zero claim `(9)` follows in both directions. If `Gamma_KL=0`, `(8)` gives zero deficiency. Conversely, if one reverse channel `S` recovers every member exactly, then it also recovers every mixture `M_lambda` from `N_lambda`; applying KL data processing through `K` and then through `S` forces

\[
D(P_\theta\|M_\lambda)
=
D(Q_\theta\|N_\lambda)
\]

for every `theta` and every full-support `lambda`. Hence `Gamma_KL=0`. More directly, if one full-support `lambda` has `eta_theta(lambda)=0` for all members, `(4)` forces `J_theta=widetilde J_theta`, so that same Bayes reverse recovers every `P_theta` exactly.

### The average loss is conditional mutual information

Under the prior `lambda`, let

\[
\mathbb P(\Theta=\theta,X=x,Y=y)
=
\lambda_\theta P_\theta(x)K(y\mid x).
\tag{23}
\]

The standard mixture identities give

\[
I_\lambda(\Theta;X)
=
\sum_\theta\lambda_\theta
D(P_\theta\|M_\lambda),
\tag{24}
\]

and

\[
I_\lambda(\Theta;Y)
=
\sum_\theta\lambda_\theta
D(Q_\theta\|N_\lambda).
\tag{25}
\]

Since `Theta-X-Y` is a Markov chain, the mutual-information chain rule gives

\[
I_\lambda(\Theta;X)
-I_\lambda(\Theta;Y)
=
I_\lambda(\Theta;X\mid Y),
\tag{26}
\]

which proves `(10)`.

There is an equivalent KL-projection statement. The joint law

\[
\widetilde{\mathbb P}(\theta,x,y)
=
\lambda_\theta Q_\theta(y)R_\lambda(x\mid y)
\tag{27}
\]

preserves the true `(Theta,Y)` marginal, uses the mixture conditional `P(X|Y)=R_lambda`, and satisfies

\[
\Theta\perp X\mid Y.
\]

Then

\[
D(\mathbb P\|\widetilde{\mathbb P})
=
I_\lambda(\Theta;X\mid Y)
=
\sum_\theta\lambda_\theta\eta_\theta(\lambda).
\tag{28}
\]

Thus the weighted-average version is exactly classical conditional mutual information; `Gamma_KL` is a worst-member, prior-optimized strengthening adapted to the whole-experiment recovery target.

### The private-label family has logarithmic prior dilution

For the family `(11)`, the common mixture for prior `lambda=(lambda_1,...,lambda_m)` is

\[
M_\lambda
=(1-\rho)\delta_0
+\rho\sum_{j=1}^m\lambda_j\delta_j.
\tag{29}
\]

Every output law equals

\[
Q_i=N_\lambda
=(1-\rho)\delta_0+\rho\delta_*.
\tag{30}
\]

Therefore the output divergence in `(3)` vanishes and

\[
\eta_i(\lambda)
=D(P_i\|M_\lambda)
=\rho\log\frac1{\lambda_i}.
\tag{31}
\]

Hence

\[
\max_i\eta_i(\lambda)
=
\rho\log\frac1{\min_i\lambda_i}.
\tag{32}
\]

Every probability vector on `m` points has `min_i lambda_i<=1/m`, with equality at the uniform prior. This proves `(13)`.

At that prior, `R_lambda` retains `0` exactly and maps `*` uniformly onto the `m` private labels, exactly as in AF-146. AF-146 already proves that this reverse is minimax optimal and that its recovery error is `(12)`. Equation `(14)` follows immediately.

The mechanism is now transparent. Losing a private label of total probability `rho` costs only order `rho` in total variation recovery, but the label itself carries `log m` nats when it occurs. KL measures that information-weighted loss, producing `rho log m`. Pearson chi-square weights the same rare event by the inverse reference probability and pays order `rho m`. Thus the two divergences induce genuinely different quantitative notions of approximate fidelity even though both vanish exactly at sufficiency.

### Coherent composition is inherited without a new compatibility layer

AF-145 proves that the Bayes reverses generated by one propagated reference compose exactly along a finite Markov pipeline. The same reference chain also makes KL losses telescope algebraically.

For

\[
X_0\xrightarrow{K_1}\cdots\xrightarrow{K_n}X_n,
\]

put `P_{theta,j}=P_{theta,j-1}K_j` and `M_j=sum_theta lambda_theta P_{theta,j}`. Define

\[
\eta_{\theta,j}
=
D(P_{\theta,j-1}\|M_{j-1})
-D(P_{\theta,j}\|M_j).
\tag{33}
\]

Then

\[
\sum_{j=1}^n\eta_{\theta,j}
=
D(P_{\theta,0}\|M_0)
-D(P_{\theta,n}\|M_n),
\tag{34}
\]

while AF-145's Bayes reverse factorization identifies `R_n...R_1` with the Bayes reverse of the composite channel. Applying `(5)` once at the endpoint gives

\[
2\left\|
P_{\theta,0}-P_{\theta,n}R_n\cdots R_1
\right\|_{\rm TV}^2
\le
\sum_{j=1}^n\eta_{\theta,j}.
\tag{35}
\]

So the KL replacement preserves the favorable compositional structure of AF-145. The new boundary is calibration against growing families, not a reappearance of the generic composition obstruction from AF-133--AF-134.

## Prior art and novelty assessment

No theorem-level novelty is claimed for the information-theoretic ingredients.

- Thomas M. Cover and Joy A. Thomas, ***Elements of Information Theory***, 2nd ed., Wiley (2006). Role: standard source for relative entropy, the KL chain rule, mutual-information mixture identities, conditional mutual information, data processing, and Pinsker-type control. Equations `(4)`, `(10)`, `(19)--(28)` are finite classical specializations of this established calculus.
- Friedrich Liese, **“φ-divergences, sufficiency, Bayes sufficiency, and deficiency,”** *Kybernetika* 48(4), 690--713 (2012). Role: direct decision-theoretic prior art relating classes of `phi`-divergences to sufficiency, Bayes sufficiency, and Le Cam deficiency. In particular, this is strong prior art against treating a single divergence profile as a complete new theory of statistical deficiency.
- Igal Sason, **“On Reverse Pinsker Inequalities,”** arXiv:`1503.07118` (2015), together with Igal Sason and Sergio Verdú, **“f-Divergence Inequalities,”** *IEEE Transactions on Information Theory* 62(11), 5973--6006 (2016), DOI `10.1109/TIT.2016.2603151`, arXiv:`1508.00335`. Role: established boundaries for upper-bounding relative entropy from total variation; reverse inequalities require additional support/relative-information control in general. AF-147's growing-family example is a whole-experiment specialization of that broader non-equivalence phenomenon.
- Omar Fawzi and Renato Renner, **“Quantum Conditional Mutual Information and Approximate Markov Chains,”** *Communications in Mathematical Physics* 340, 575--611 (2015), DOI `10.1007/s00220-015-2466-x`, arXiv:`1410.0664`. Role: stronger neighboring noncommutative recovery literature showing that conditional mutual information controls approximate reconstruction. The finite classical identity here is much simpler: the conditional-independence projection is explicit and Pinsker turns its exact KL gap into total-variation recovery.
- AF-126 provides the exact whole-experiment recovery target, AF-144 supplies the common Bayes reverse in the Pearson setting, AF-145 supplies its coherent composition law, and AF-146 supplies the symmetric family on which the quantitative calibration can be compared exactly.

The durable Arithmetic Fidelity delta is therefore not a new KL, Pinsker, conditional-mutual-information, or recovery theorem. It is the exact comparison needed by the current line frontier: **changing the common-reference loss from Pearson chi-square to KL removes the linear family-size dilution but only replaces it by logarithmic dilution.** The same canonical reverse remains optimal in the diagnostic family, so this hierarchy measures the certificate rather than the inverse-selection quality.

## Boundary conditions and falsification tests

1. **Natural logarithms are load-bearing for the constants.** With logarithms base two, `(5)` and `(8)` acquire the corresponding `ln 2` conversion. The family-complexity conclusion remains logarithmic.

2. **The common reference remains essential.** The same `M_lambda` must generate both the source/output KL losses and the reverse kernel. Independently selected pairwise references do not produce one experiment-wide inverse.

3. **The positive bound is one-way.** Equation `(8)` says small `Gamma_KL` certifies small recovery deficiency. Equation `(17)` rules out the converse without family-complexity or likelihood-ratio control.

4. **KL fixes the AF-146 scaling but not the general problem.** At `rho=1/m`, both `Gamma_KL` and deficiency vanish. A conclusion that KL is therefore dimension-free in both directions is falsified by `rho=1/log m`.

5. **The reverse kernel is not responsible for the gap.** In the symmetric family the optimizing uniform-prior Bayes reverse is already minimax optimal. The logarithmic factor belongs to the KL notion of lost information.

6. **The average and worst-member profiles are different objects.** Equation `(10)` identifies the prior average with conditional mutual information. The recovery target in `(6)--(8)` requires the worst member. A small average loss can hide a bad rare control unless the prior or control geometry supplies a lower-weight bound or another uniformity argument.

7. **No arithmetic conclusion follows yet.** The counterexample is deliberately non-arithmetic. A concrete prime application must still define the relevant growing control family and prove whether its effective label entropy, likelihood ratios, or a smaller sufficient control skeleton remain bounded with scale.

8. **Restricted converses remain open.** Uniform likelihood-ratio bounds, lower reference weights, bounded effective entropy/cardinality, or another source-natural complexity constraint can yield reverse-Pinsker-type control. AF-147 rules out only an unrestricted family-size-independent converse.

9. **No claim is made that KL is the optimal fidelity gauge.** Liese's deficiency results already point to classes of divergences rather than one universal scalar. The present result instead gives an exact calibration datum for choosing among candidate gauges.

## Consequence for the current frontier

AF-143 showed that local Fisher geometry and pairwise distinguishability do not guarantee one common reverse experiment. AF-144 supplied such a reverse from one common reference, AF-145 showed that it composes coherently, and AF-146 exposed a linear family-size calibration failure of the Pearson certificate.

AF-147 now separates the **recovery mechanism** from the **loss gauge**. The Bayes reverse and its compositional behavior survive unchanged when Pearson loss is replaced by KL. What changes is how a growing family prices rare discarded distinctions: linear `m` amplification becomes logarithmic `log m`, but a dimension-free converse still fails.

For an eventual arithmetic application, this makes family complexity a first-class fidelity datum. It is not enough to find a divergence whose data-processing loss vanishes exactly at sufficiency. One must also prove that the chosen loss remains quantitatively calibrated to the actual recovery target for the scale-dependent control family. A promising route is therefore to identify a source-natural bound on **effective control entropy or reference likelihood geometry**, rather than merely switching from one divergence to another.