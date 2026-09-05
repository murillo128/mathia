# AF-126 — Le Cam recovery deficiency quantifies approximate statistical fidelity

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `QUANTITATIVE-FIDELITY`, `APPROXIMATE-SUFFICIENCY`, `NO-NOVELTY-CLAIM`

## Claim

AF-012 and AF-013 identify the exact statistical-fidelity boundary: a stochastic compression preserves a binary or finite experiment exactly when one reverse channel reconstructs every member of the experiment. The natural quantitative relaxation is not another selected divergence. It is the **best uniform reverse simulation error** of the whole experiment.

Let

\[
\mathcal E=(P_\theta)_{\theta\in\Theta}
\]

be a finite statistical experiment on a finite sample space `X`, with finite parameter set `Theta`, and let

\[
K:X\rightsquigarrow Y
\]

be a stochastic compression. Write

\[
\mathcal F=\mathcal E K=(P_\theta K)_{\theta\in\Theta}.
\]

Using normalized total variation

\[
\|P-Q\|_{\mathrm{TV}}
:=\frac12\sum_x|P(x)-Q(x)|,
\tag{1}
\]

define the **recovery deficiency** of the compression by

\[
\boxed{
\delta_{\rm rec}(K;\mathcal E)
:=
\inf_{R:Y\rightsquigarrow X}
\sup_{\theta\in\Theta}
\bigl\|P_\theta-(P_\theta K)R\bigr\|_{\mathrm{TV}}.
}
\tag{2}
\]

This is the one-sided Le Cam deficiency measuring how well the compressed experiment can simulate the original one; conventions in the literature reverse the argument order, so `(2)` fixes the orientation explicitly.

For finite spaces and finite `Theta`:

1. the infimum in `(2)` is attained;
2. \(\delta_{\rm rec}(K;\mathcal E)=0\) if and only if there exists one reverse channel `R` with
   \[
   (P_\theta K)R=P_\theta
   \qquad\forall\theta,
   \tag{3}
   \]
   so zero recovery deficiency is exactly the Blackwell/statistical-sufficiency boundary of AF-013;
3. if a second garbling
   \[
   L:Y\rightsquigarrow Z
   \]
   is applied, then
   \[
   \boxed{
   \delta_{\rm rec}(L\circ K;\mathcal E)
   \ge
   \delta_{\rm rec}(K;\mathcal E).
   }
   \tag{4}
   \]
   Approximate recoverability cannot improve under downstream processing that receives only the already-compressed observation;
4. more generally, for experiments `A,B,C` with the same parameter set, define
   \[
   \delta(A\mid B)
   :=
   \inf_{R:B\rightsquigarrow A}
   \sup_\theta\|A_\theta-B_\theta R\|_{\rm TV}.
   \tag{5}
   \]
   Then
   \[
   \boxed{
   \delta(A\mid C)
   \le
   \delta(A\mid B)+\delta(B\mid C).
   }
   \tag{6}
   \]
   Thus recovery errors compose subadditively rather than disappearing after another compression;
5. because `F=EK` is already an exact garbling of `E`,
   \[
   \delta(\mathcal F\mid\mathcal E)=0.
   \tag{7}
   \]
   Hence the symmetric Le Cam distance
   \[
   \Delta(\mathcal E,\mathcal F)
   :=
   \max\{\delta(\mathcal E\mid\mathcal F),
          \delta(\mathcal F\mid\mathcal E)\}
   \tag{8}
   \]
   collapses on a genuine compression chain to
   \[
   \boxed{
   \Delta(\mathcal E,\mathcal E K)
   =
   \delta_{\rm rec}(K;\mathcal E).
   }
   \tag{9}
   \]
6. if `0<=ell(theta,a)<=1` is any bounded loss and `D:X\rightsquigarrow A` any decision rule for the original experiment, then every reverse channel `R` with error at most `epsilon` produces a compressed-data rule `R D` satisfying
   \[
   \boxed{
   \bigl|
   \mathcal R_\theta(D;\mathcal E)
   -
   \mathcal R_\theta(RD;\mathcal F)
   \bigr|
   \le\varepsilon
   \qquad\forall\theta.
   }
   \tag{10}
   \]
   Recovery deficiency is therefore a uniform decision-simulation defect, not merely a distance between probability vectors;
7. every pair of hypotheses gives the computable lower bound
   \[
   \boxed{
   \delta_{\rm rec}(K;\mathcal E)
   \ge
   \frac12
   \left[
   \|P_\theta-P_{\theta'}\|_{\rm TV}
   -
   \|P_\theta K-P_{\theta'}K\|_{\rm TV}
   \right]
   }
   \tag{11}
   \]
   whenever the bracket is positive. Thus loss of pairwise total-variation distinguishability certifies a minimum amount of irrecoverable experiment-level information;
8. the pairwise bound is **not complete**. AF-012 already supplies a binary compression that preserves total variation exactly while failing statistical sufficiency. For that example the right side of `(11)` is zero, yet compactness plus failure of exact sufficiency force
   \[
   \delta_{\rm rec}>0.
   \tag{12}
   \]
   Preserving one pairwise scalar discrimination score can therefore miss a genuine positive whole-experiment recovery defect.

The deficiency framework is classical Le Cam/Blackwell comparison-of-experiments theory. The Arithmetic Fidelity consequence is the placement of the correct approximate boundary after AF-012/AF-013: **exact fidelity is zero reverse-simulation deficiency, while approximate fidelity of the whole declared control family is the distance to a common reverse channel.** Individual divergence losses may lower-bound or diagnose that defect, but they need not determine it.

## Derivation

### Finite recovery deficiency attains its optimum

A reverse channel `R:Y\rightsquigarrow X` is a row-stochastic matrix. The set of all such matrices is a finite product of probability simplices and hence compact.

For each `theta`,

\[
R\mapsto
\|P_\theta-(P_\theta K)R\|_{\rm TV}
\tag{13}
\]

is continuous, and the maximum over finite `Theta` is continuous. Therefore the infimum in `(2)` is achieved by at least one reverse channel.

It follows immediately that

\[
\delta_{\rm rec}(K;\mathcal E)=0
\]

if and only if the minimizing channel has zero error for every parameter value, which is exactly `(3)`. In the finite dominated setting of AF-013 this is the same common-reverse-channel criterion obtained from vector likelihood-ratio sufficiency.

Thus deficiency does not introduce a different exact notion of fidelity. It extends the existing exact boundary continuously into a quantitative regime.

### Downstream garbling restricts the available recovery channels

Let

\[
L:Y\rightsquigarrow Z
\]

be a further compression and let

\[
S:Z\rightsquigarrow X
\]

be any attempted recovery from the final output. Then

\[
R:=LS:Y\rightsquigarrow X
\tag{14}
\]

is a legitimate recovery channel from the earlier output and

\[
(P_\theta K L)S
=(P_\theta K)R.
\tag{15}
\]

Therefore every recovery strategy available after `L` belongs to a restricted subclass of the recovery strategies already available after `K`. Taking infima gives `(4)`.

This is stronger than the binary statement that a selected divergence loss cannot decrease. It says that the **best simultaneous reconstruction of the entire declared experiment** cannot improve without a new side channel.

### Deficiency satisfies the directed triangle inequality

Let `R:B -> A` and `S:C -> B` be arbitrary randomizations. For every `theta`, total variation and its contraction under stochastic maps give

\[
\begin{aligned}
\|A_\theta-C_\theta S R\|_{\rm TV}
&\le
\|A_\theta-B_\theta R\|_{\rm TV}
+
\|B_\theta R-C_\theta S R\|_{\rm TV}\\
&\le
\|A_\theta-B_\theta R\|_{\rm TV}
+
\|B_\theta-C_\theta S\|_{\rm TV}.
\end{aligned}
\tag{16}
\]

Take the supremum over `theta`, then choose `R` and `S` arbitrarily close to their respective infima. This proves `(6)`.

For `F=EK`, the forward randomization `K` itself gives exact simulation of `F` from `E`, hence `(7)`. Equations `(8)` and `(9)` then follow.

This is an exact formal version of a recurring Arithmetic Fidelity intuition: when one representation is literally obtained by compressing another, the only nonzero direction in experiment distance is the information needed to go back.

### A reverse simulation transfers every bounded decision rule

Fix a reverse channel `R` and suppose

\[
\sup_\theta
\|P_\theta-(P_\theta K)R\|_{\rm TV}
\le\varepsilon.
\tag{17}
\]

A decision rule `D:X\rightsquigarrow A` maps the original observation to an action distribution. The corresponding rule on compressed data is the composition

\[
Y\xrightarrow{R}X\xrightarrow{D}A.
\tag{18}
\]

Total variation contracts under `D`, so

\[
\|P_\theta D-(P_\theta K)R D\|_{\rm TV}
\le\varepsilon.
\tag{19}
\]

For any loss bounded in `[0,1]`, the difference of its expectations under two action distributions is at most their total variation. Hence `(10)` follows.

Classical randomization/deficiency theory supplies the converse decision-theoretic characterizations under the corresponding conventions and normalizations. For the present line the forward implication is the useful audit statement: a single reverse channel simultaneously transfers **every** bounded downstream decision rule, so deficiency measures loss at the experiment level rather than for one chosen statistic.

### Pairwise distinguishability gives a universal lower bound

Fix `theta,theta'` and any reverse channel `R`. Put

\[
\varepsilon_R
:=
\sup_\eta
\|P_\eta-(P_\eta K)R\|_{\rm TV}.
\tag{20}
\]

The triangle inequality gives

\[
\begin{aligned}
\|P_\theta-P_{\theta'}\|_{\rm TV}
&\le
\|P_\theta-(P_\theta K)R\|_{\rm TV}\\
&\quad+
\|(P_\theta K)R-(P_{\theta'}K)R\|_{\rm TV}\\
&\quad+
\|(P_{\theta'}K)R-P_{\theta'}\|_{\rm TV}.
\end{aligned}
\tag{21}
\]

By contraction of total variation under `R`,

\[
\|(P_\theta K)R-(P_{\theta'}K)R\|_{\rm TV}
\le
\|P_\theta K-P_{\theta'}K\|_{\rm TV}.
\tag{22}
\]

Therefore

\[
\|P_\theta-P_{\theta'}\|_{\rm TV}
-
\|P_\theta K-P_{\theta'}K\|_{\rm TV}
\le2\varepsilon_R.
\tag{23}
\]

Taking the infimum over `R` proves `(11)`.

The factor `1/2` is unavoidable in this direct two-endpoint argument because the reverse simulation may spend error on both hypotheses.

## A scalar divergence can miss positive recovery deficiency

AF-012 gives an exact matched control against overinterpreting `(11)`. There

\[
X=\{a,b,c\},
\qquad
Q=(1/3,1/3,1/3),
\]

with likelihood ratios

\[
L(a)=1/2,
\qquad
L(b)=4/5,
\qquad
L(c)=17/10,
\tag{24}
\]

and a deterministic compression merges `a` and `b` while retaining `c` separately.

The merged likelihood ratios `1/2` and `4/5` lie on the same affine branch of

\[
f(t)=\frac12|t-1|,
\tag{25}
\]

so total variation between the two hypotheses is preserved exactly by the compression. Consequently the lower bound `(11)` gives zero.

But the compression is not sufficient because

\[
L(a)\ne L(b).
\tag{26}
\]

By the attainment result above, zero recovery deficiency would require an exact reverse channel, contradicting AF-012. Hence

\[
\boxed{
\text{pairwise TV loss}=0
\quad\text{while}\quad
\delta_{\rm rec}>0.
}
\tag{27}
\]

This is the decisive separation from an arbitrary scalar fidelity score. The whole-experiment defect detects the absence of a common reconstruction even when a particular non-strict divergence happens to sit on an equality face.

The same warning applies to larger control families. Pairwise diagnostics are useful obstructions, but a collection of scalar equalities should not be promoted to approximate family fidelity unless a theorem connects them to a single common reverse randomization.

## Relationship to AF-009, AF-012, AF-013, and downstream compression

AF-009 measures the mean squared recovery defect of one declared random discriminator under one probability law. It is a useful task-relative average defect.

AF-012 and AF-013 identify the exact likelihood-ratio structure whose preservation is equivalent to binary or finite-experiment sufficiency. They answer the zero-loss question exactly.

AF-126 adds the quantitative **whole-experiment** layer. Instead of choosing a discriminator or divergence and asking how much that quantity changes, it asks how closely the compressed experiment can regenerate all upstream distributions using one admissible stochastic recovery map.

This produces a hierarchy of claims that should not be conflated:

\[
\text{small selected-discriminator loss}
\not\Rightarrow
\text{small whole-experiment deficiency},
\tag{28}
\]

while

\[
\text{small whole-experiment deficiency}
\Rightarrow
\text{uniformly small loss for every bounded decision rule}
\tag{29}
\]

through the same reverse channel.

In a chain

\[
\mathcal E
\to\mathcal E K
\to\mathcal E K L,
\tag{30}
\]

`(4)` supplies a monotone quantitative obstruction. Once the family is a positive deficiency away from the original experiment, later processing of the retained state cannot reduce that distance. Any claimed repair must identify genuinely new side information, a changed admissible category, or a weaker discriminator family.

## Prior art and novelty assessment

The central framework is classical.

Lucien Le Cam's 1964 paper **“Sufficiency and Approximate Sufficiency,”** *The Annals of Mathematical Statistics* 35(4), 1419–1455, DOI `10.1214/AOMS/1177700372`, is primary prior art for approximate sufficiency and distance/deficiency between statistical experiments.

David Blackwell's **“Equivalent Comparisons of Experiments,”** *The Annals of Mathematical Statistics* 24(2), 265–272 (1953), DOI `10.1214/aoms/1177729032`, supplies the exact comparison/randomization boundary underlying zero deficiency.

Erik Torgersen's ***Comparison of Statistical Experiments***, Cambridge University Press (1991), especially Chapter 6, **“Deficiencies,”** DOI `10.1017/CBO9780511666353.007`, is an authoritative systematic treatment of deficiency, randomization, risk comparison, distance, and the question of worst-case information loss between experiments.

Friedrich Liese's **“φ-divergences, sufficiency, Bayes sufficiency, and deficiency,”** *Kybernetika* 48(4), 690–713 (2012), places deficiency explicitly next to the `phi`-divergence and sufficiency language already used in AF-012.

Accordingly, **no novelty is claimed** for Le Cam deficiency, Blackwell comparison, the randomization theorem, the Le Cam distance, total-variation contraction, or their standard decision-theoretic interpretation. Equations `(2)`–`(10)` are a finite compression-specialized organization of that classical theory; `(11)` is the elementary pairwise consequence derived here.

The line-specific value is the taxonomy boundary: AF-012/AF-013 should not be extended approximately by selecting one convenient divergence and treating its small loss as generic structural fidelity. When the declared upstream discriminator is an entire finite matched-control experiment, the canonical approximate target is a **common reverse-simulation defect**. Scalar divergences are probes of that defect, not substitutes for it without a completeness theorem.

## Boundaries and falsification controls

- The concrete derivations above assume finite sample spaces and finite `Theta`. General Le Cam theory is substantially broader; this finding deliberately uses the finite setting where compactness and randomization are transparent.
- The normalization `(1)` matters. Other conventions use the full `L^1` norm and therefore differ by a factor of two.
- Literature reverses the order of the arguments in one-sided deficiency in different notational conventions. The operational direction in `(2)` is authoritative here: the available compressed experiment tries to simulate the original experiment.
- Recovery channels are arbitrary stochastic kernels. A Mathia application with locality, equivariance, bounded complexity, continuity, operator, or geometric constraints needs a **restricted deficiency** with the admissible recovery class declared independently. Unrestricted Le Cam recovery can otherwise certify an abstract simulation that is unavailable in the intended mathematical category.
- `delta_rec` is relative to the declared family `(P_theta)`. A small defect for a weak control family says nothing about a stronger family omitted from `Theta`.
- Pairwise total-variation loss gives only a lower bound. Equation `(27)` proves that even for a binary experiment this bound can vanish while the true recovery deficiency is positive.
- Conversely, a positive selected divergence loss establishes information loss for that selected experiment but should not be assigned an exact numerical deficiency without a theorem relating the divergence to reverse-simulation error.
- The bounded-decision transfer `(10)` is one direction of the classical randomization principle; do not silently replace its stated finite normalized form by a stronger minimax equality without auditing the exact theorem and convention.
- No claim is made that a probabilistic statistical experiment is the correct model for every RH compression. The framework applies when a control family, randomized observation, sampling law, noisy measurement, or probability-weighted discriminator is genuinely part of the construction.

## Decisive audit test for approximate statistical compression

When a proposed compression is claimed to preserve an entire finite matched-control family approximately:

1. declare the experiment `(P_theta)` before examining the compressed output;
2. compute or bound the best **single** reverse channel in `(2)`, rather than optimizing a different reconstruction separately for each control;
3. use pairwise total-variation or divergence losses only as lower bounds/diagnostics unless a completeness theorem is available;
4. verify that the admissible reverse channel belongs to the mathematical category of the claimed mechanism rather than using target-leaking or externally supplied reconstruction;
5. under further compression, require any claimed improvement in fidelity to identify new side information, because `(4)` forbids improvement from downstream garbling alone;
6. for exact claims, set the defect to zero and recover AF-013's common-reverse-channel / vector-likelihood-ratio sufficiency criterion.

## Consequence for the line

Add **recovery deficiency** as the canonical quantitative notion for finite statistical-control families. The resulting statistical part of the Arithmetic Fidelity taxonomy now has three genuinely different levels:

\[
\text{supportwise zero-error fidelity}
\quad\text{(AF-011)},
\]

\[
\text{selected average/divergence fidelity}
\quad\text{(AF-009/AF-012)},
\]

and

\[
\text{whole-experiment approximate fidelity}
\quad\text{(AF-126)}.
\]

AF-013 is their exact family-level boundary: `delta_rec=0` exactly when the full vector likelihood-ratio experiment survives. Future arithmetic uses should state which level their claim actually requires before interpreting a small loss as preservation of rational-prime-specific information.