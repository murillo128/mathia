# AF-046 — Zero-error stochastic fidelity has zero total-variation robustness

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `STRUCTURAL-CLASSIFICATION`, `NEGATIVE/OBSTRUCTION`

## Claim

Let `X` and `Y` be finite nonempty sets, let

\[
d:X\to D
\]

be a nonconstant discriminator, and let a stochastic channel `K:X\rightsquigarrow Y` be written rowwise as

\[
K_x(\cdot)=K(\cdot\mid x)\in\Delta(Y).
\]

Equip the channel space with the row-sup total-variation metric

\[
\rho_\infty(K,L)
=
\max_{x\in X}\operatorname{TV}(K_x,L_x),
\qquad
\operatorname{TV}(P,Q)
=
\frac12\sum_{y\in Y}|P(y)-Q(y)|.
\]

There are two sharply different fidelity boundaries.

Define the **distribution-law collision set**

\[
\mathcal C_d
=
\left\{
L:\exists x\ne x',\ d(x)\ne d(x'),\ L_x=L_{x'}
\right\}
\]

and the row-separation modulus

\[
\gamma_{\mathrm{TV}}(K,d)
=
\min_{d(x)\ne d(x')}
\operatorname{TV}(K_x,K_{x'}).
\]

Also define the **zero-error failure set** from AF-011,

\[
\mathcal F_d^{(0)}
=
\left\{
L:\exists x,x',y,\ d(x)\ne d(x'),\
L(y\mid x)>0,\ L(y\mid x')>0
\right\},
\]

whose complement `\mathcal Z_d^{(0)}` consists of channels whose distinct discriminator classes have disjoint output supports.

Then:

1. **Distribution-law collision has an exact positive margin.**
   \[
   \boxed{
   \operatorname{dist}_{\rho_\infty}(K,\mathcal C_d)
   =
   \frac12\gamma_{\mathrm{TV}}(K,d).
   }
   \]
   For a fixed conflicting pair `x,x'`, the nearest row-equality collision is obtained by replacing both rows by their midpoint
   \[
   M=\frac{K_x+K_{x'}}2.
   \]

2. **The law-separation margin is stable.** The function
   \[
   K\mapsto \gamma_{\mathrm{TV}}(K,d)
   \]
   is `2`-Lipschitz with respect to `\rho_\infty`, so its half is exactly the `1`-Lipschitz distance to the closed collision set `\mathcal C_d`.

3. **Zero-error failure is open and dense.** In the finite channel simplex,
   \[
   \boxed{
   \mathcal F_d^{(0)}\text{ is relatively open and dense},
   }
   \]
   while
   \[
   \boxed{
   \mathcal Z_d^{(0)}\text{ is closed and nowhere dense}.
   }
   \]

4. **Zero-error support fidelity has no positive TV radius at all.** For every channel `K`, including every zero-error faithful channel,
   \[
   \boxed{
   \operatorname{dist}_{\rho_\infty}
   (K,\mathcal F_d^{(0)})=0.
   }
   \]
   Thus an arbitrarily small total-variation perturbation can activate a previously zero transition probability and create a fatal AF-011 confusability edge.

5. **The two robustness notions can be maximally separated.** If `K\in\mathcal Z_d^{(0)}`, then every pair of rows from different discriminator classes has disjoint support, hence
   \[
   \operatorname{TV}(K_x,K_{x'})=1.
   \]
   Therefore
   \[
   \boxed{
   \gamma_{\mathrm{TV}}(K,d)=1,
   \qquad
   \operatorname{dist}(K,\mathcal C_d)=\frac12,
   \qquad
   \operatorname{dist}(K,\mathcal F_d^{(0)})=0.
   }
   \]
   A zero-error faithful channel is consequently at the **maximum possible distance from equality of conflicting output laws** while simultaneously lying on the boundary of **supportwise zero-error failure**.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{robust fidelity is topology- and criterion-dependent: total variation gives a sharp positive margin for equality-of-law collisions, but zero margin for support-confusability loss.}
}
\]

This strengthens AF-011's small-crossover example into a complete topological classification for finite channels under row-sup total variation.

## Derivation

### Exact distance to one conflicting row equality

Fix `x,x'` with `d(x)\ne d(x')`. Let

\[
\mathcal C_{x,x'}
=
\{L:L_x=L_{x'}\}.
\]

If `L\in\mathcal C_{x,x'}` and `R=L_x=L_{x'}`, the triangle inequality gives

\[
\operatorname{TV}(K_x,K_{x'})
\le
\operatorname{TV}(K_x,R)
+
\operatorname{TV}(R,K_{x'}).
\]

Both terms are at most `\rho_\infty(K,L)`, so

\[
\rho_\infty(K,L)
\ge
\frac12\operatorname{TV}(K_x,K_{x'}).
\]

For the reverse inequality, set

\[
M=\frac{K_x+K_{x'}}2
\]

and define `L` by replacing only rows `x,x'` with `M`. Since total variation is half the `\ell^1` norm,

\[
\operatorname{TV}(K_x,M)
=
\operatorname{TV}(K_{x'},M)
=
\frac12\operatorname{TV}(K_x,K_{x'}).
\]

Hence

\[
\boxed{
\operatorname{dist}_{\rho_\infty}(K,\mathcal C_{x,x'})
=
\frac12\operatorname{TV}(K_x,K_{x'}).
}
\]

Because `X` is finite,

\[
\mathcal C_d
=
\bigcup_{d(x)\ne d(x')}\mathcal C_{x,x'}
\]

is a finite union, and taking the minimum over conflicting pairs yields

\[
\boxed{
\operatorname{dist}_{\rho_\infty}(K,\mathcal C_d)
=
\frac12\min_{d(x)\ne d(x')}\operatorname{TV}(K_x,K_{x'}).
}
\]

Unlike AF-011's one-sample decoder problem, this criterion treats the row distribution itself as the retained representation. It therefore measures when two discriminator classes become identical as probability laws, not when one observed output can be shared with positive probability.

### Lipschitz stability of the law-separation modulus

For any two channels `K,L` and any fixed pair `x,x'`,

\[
\begin{aligned}
&\left|
\operatorname{TV}(K_x,K_{x'})
-
\operatorname{TV}(L_x,L_{x'})
\right|\\
&\qquad\le
\operatorname{TV}(K_x,L_x)
+
\operatorname{TV}(K_{x'},L_{x'})\\
&\qquad\le
2\rho_\infty(K,L).
\end{aligned}
\]

Taking minima over the same finite set of conflicting pairs gives

\[
\boxed{
|\gamma_{\mathrm{TV}}(K,d)-\gamma_{\mathrm{TV}}(L,d)|
\le
2\rho_\infty(K,L).
}
\]

Thus `\gamma_{\mathrm{TV}}/2` is a genuine stable-fidelity margin. This is the stochastic probability-simplex analogue of AF-044/AF-045's distance-to-collision formulas.

### Zero-error failure is relatively open

For each triple `(x,x',y)` with `d(x)\ne d(x')`, consider

\[
U_{x,x',y}
=
\{K:K(y\mid x)>0,\ K(y\mid x')>0\}.
\]

Coordinate evaluation is continuous on the finite product of simplices, and strict positivity is relatively open. Therefore every `U_{x,x',y}` is relatively open, and

\[
\mathcal F_d^{(0)}
=
\bigcup_{d(x)\ne d(x')}
\bigcup_{y\in Y}
U_{x,x',y}
\]

is relatively open.

Its complement is exactly the AF-011 zero-error faithful set, so `\mathcal Z_d^{(0)}` is closed.

### Zero-error failure is dense

Take an arbitrary channel `K`. If `K\in\mathcal F_d^{(0)}`, there is nothing to prove. Otherwise `K` is zero-error faithful.

Choose any pair `x,x'` with `d(x)\ne d(x')`. Because `K_x` is a probability distribution, choose `y\in Y` with

\[
K(y\mid x)>0.
\]

Zero-error faithfulness forces

\[
K(y\mid x')=0.
\]

For `0<\varepsilon<1`, modify only row `x'` by

\[
L_{x'}
=
(1-\varepsilon)K_{x'}
+\varepsilon\delta_y,
\]

leaving all other rows unchanged. Then

\[
L(y\mid x')=\varepsilon>0,
\]

so `x` and `x'` now share output `y` and

\[
L\in\mathcal F_d^{(0)}.
\]

Since `K_{x'}(y)=0`, the two measures `K_{x'}` and `\delta_y` are mutually singular, hence

\[
\operatorname{TV}(K_{x'},L_{x'})
=
\varepsilon.
\]

Therefore

\[
\rho_\infty(K,L)=\varepsilon.
\]

As `\varepsilon` is arbitrary,

\[
\boxed{
\operatorname{dist}_{\rho_\infty}(K,\mathcal F_d^{(0)})=0.
}
\]

Thus `\mathcal F_d^{(0)}` is dense. Because it is open, its complement `\mathcal Z_d^{(0)}` is closed with empty interior, hence nowhere dense.

This is stronger than AF-011's particular `K_\varepsilon` example: every zero-error faithful finite channel has the same topological instability under any perturbation model that permits arbitrarily small activation of a zero transition probability in total variation.

### Zero-error fidelity is maximally separated at the law level

If `K` is zero-error faithful and `d(x)\ne d(x')`, AF-011 says the two row supports are disjoint. For probability measures on a finite set,

\[
\operatorname{supp}(K_x)\cap\operatorname{supp}(K_{x'})=\varnothing
\]

implies

\[
\operatorname{TV}(K_x,K_{x'})=1.
\]

Since total variation never exceeds `1`, every conflicting pair is maximally separated and

\[
\gamma_{\mathrm{TV}}(K,d)=1.
\]

The exact law-collision formula then gives

\[
\operatorname{dist}(K,\mathcal C_d)=\frac12.
\]

But the density argument simultaneously gives

\[
\operatorname{dist}(K,\mathcal F_d^{(0)})=0.
\]

So the discrepancy is not a matter of a poorly conditioned example. It is maximal:

\[
\boxed{
\text{maximal probability-law separation}
\quad\text{coexists with}\quad
\text{zero supportwise robustness}.
}
\]

The two loss sets encode different mathematical questions.

## Exact two-state control

Let

\[
X=D=\{0,1\},
\qquad
Y=\{a,b\},
\qquad
d(x)=x,
\]

and take the noiseless channel

\[
K_0=\delta_a,
\qquad
K_1=\delta_b.
\]

The rows are disjoint, so one sample determines the discriminator with zero error. Also

\[
\operatorname{TV}(K_0,K_1)=1,
\]

hence

\[
\operatorname{dist}(K,\mathcal C_d)=\frac12.
\]

Now for any `\varepsilon>0`, replace

\[
K_1
\quad\text{by}\quad
K_1^{(\varepsilon)}
=
(1-\varepsilon)\delta_b
+\varepsilon\delta_a.
\]

Then

\[
\rho_\infty(K,K^{(\varepsilon)})=\varepsilon,
\]

but output `a` is possible under both discriminator values. Thus zero-error recovery fails for every positive `\varepsilon`.

At the same time,

\[
\operatorname{TV}(K_0,K_1^{(\varepsilon)})
=1-\varepsilon,
\]

so the two conditional laws remain very far from equality. This isolates the distinction cleanly:

\[
\text{supportwise exactness can fail immediately while distributional distinguishability degrades continuously.}
\]

## Relationship to AF-009, AF-011, and AF-045

AF-009 gives a probability-weighted `L^2`/Bayes defect. Small rare-event mass creates only a small average penalty.

AF-011 gives the support-confusability graph. It already showed by one family that a tiny crossover probability can destroy zero-error recovery discontinuously.

The present result identifies the complete perturbation geometry behind that example. In row-sup total variation, support-confusability failure is not merely discontinuous at a special boundary: it is **dense**, and every zero-error faithful point has distance zero to failure.

AF-045 gives the opposite pattern for deterministic metric representations: the lower Lipschitz modulus is exactly the distance to collision. The distribution-law part above shows the same distance-to-collision principle inside the probability simplex. The zero-error part shows why that principle cannot be transferred across fidelity categories without preserving the exact definition of failure.

In particular,

\[
\text{row equality}
\neq
\text{support overlap}.
\]

The first is a closed metric collision event with a positive separation modulus. The second is triggered by any newly positive common coordinate and therefore has no positive TV safety radius.

## Prior art and novelty assessment

The zero-error support criterion is classical. Shannon's 1956 zero-error theory depends on the confusability relation determined by which transition probabilities are positive, not by their positive magnitudes. Witsenhausen's zero-error side-information formulation and Orlitsky--Roche characteristic-graph theory, already audited in AF-011 and recorded in `SOURCES.md`, place the same supportwise mechanism in graph-theoretic language.

Accordingly, no novelty is claimed for the confusability graph, for the fact that a tiny positive crossover can create an edge, or for total variation as a probability metric.

The exact midpoint distance to conflicting row equality, the open-dense / closed-nowhere-dense classification of the AF-011 success and failure sets under `\rho_\infty`, and their juxtaposition are derived directly here from elementary finite-simplex geometry. They should be treated as a structural classification inside Arithmetic Fidelity rather than as a claim that zero-error information theory lacked continuity/discontinuity phenomena.

The novelty audit therefore cuts in the conservative direction: the result is useful because it makes the **perturbation topology** explicit and produces an exact contrast between two loss sets, not because support sensitivity itself is new.

## Boundaries and failure modes

- The theorem uses finite `X,Y`. For countable or continuous alphabets, support, essential support, absolute continuity, and topology require a separate formulation.
- The discriminator is assumed nonconstant. If no conflicting discriminator pair exists, zero-error recovery is vacuous and the declared collision/failure sets should be redefined rather than assigning artificial infinities.
- `\rho_\infty` is the maximum rowwise total-variation distance on a fixed channel alphabet. It is not the quotient topology of Blackwell-equivalent experiments, deficiency distance, weak convergence, Wasserstein distance, or an operator norm. The distance-to-loss result must not be transported to those categories without proof.
- `\mathcal C_d` treats the full conditional law `K_x` as retained data. A decoder receiving one random sample from `K_x` does not observe that law exactly. The positive `\gamma_{\mathrm{TV}}` margin is therefore a representation-level law-separation statement, not a one-shot zero-error decoding theorem.
- The dense-failure theorem relies on perturbations being allowed to turn a zero probability into an arbitrarily small positive probability. If the admissible perturbation class fixes the support pattern, imposes a minimum positive mass, or otherwise forbids support activation, zero-error fidelity can become locally constant inside that restricted stratum.
- No statement is made here about Shannon's asymptotic zero-error capacity or graph capacity under repeated channel uses. The finding concerns AF-011's one-shot discriminator fidelity relation.
- Positive TV separation of every conflicting row is weaker than zero-error fidelity: overlapping distributions can have large TV distance. Conversely, zero-error fidelity forces maximal TV separation `1` but, paradoxically, no positive radius against support activation.
- The theorem does not say total variation is the "wrong" topology. It says that robustness claims must be indexed jointly by the perturbation topology and the mathematical failure criterion.

## Decisive audit rule

For a stochastic compression whose downstream theorem needs exact discriminator survival, state which object is supposed to remain faithful before assigning a robustness margin:

1. if the retained object is the **full output law**, compute
   \[
   \gamma_{\mathrm{TV}}(K,d)
   =
   \min_{d(x)\ne d(x')}\operatorname{TV}(K_x,K_{x'}),
   \]
   and use `\gamma_{\mathrm{TV}}/2` as the exact row-sup-TV distance to law collision;
2. if the requirement is **one-sample zero-error recovery**, use AF-011's support-confusability graph instead, and under ordinary TV perturbations do not claim any positive distance-to-failure merely because the current supports are disjoint;
3. if a positive supportwise margin is essential, justify a stricter admissible perturbation class that prevents arbitrarily small support activation, and prove the margin in that declared category.

This prevents a common category mistake: using continuous probability-law separation to certify a support property whose failure set is dense in the same metric topology.

## Consequence for the line

The distance-to-collision program from AF-041--AF-045 does extend to stochastic channels, but only after the failure event is fixed precisely.

For equality of conflicting output laws, the exact distance principle survives with a simple total-variation formula. For AF-011 zero-error support fidelity, the same topology yields an identically zero distance to failure.

Future robust-fidelity claims should therefore be written as a triple

\[
\boxed{
(\text{retained representation},\ \text{failure relation},\ \text{perturbation topology})
}
\]

rather than assigning a stability number to a compression in isolation. Two mathematically natural failure relations on the same finite stochastic channel can have maximally different robustness at the same point.