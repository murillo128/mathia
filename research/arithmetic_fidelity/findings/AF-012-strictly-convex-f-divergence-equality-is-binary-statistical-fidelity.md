# AF-012 — Strictly convex f-divergence equality is binary statistical fidelity

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `NEGATIVE/OBSTRUCTION`

## Claim

Let `X` and `Y` be finite sets. Let `P` and `Q` be strictly positive probability distributions on `X`, let

\[
K(y\mid x)\ge 0,
\qquad
\sum_{y\in Y}K(y\mid x)=1,
\]

be a stochastic compression channel, and write

\[
\bar P=PK,
\qquad
\bar Q=QK.
\]

Define the upstream likelihood ratio

\[
L(x)=\frac{P(x)}{Q(x)}
\]

and, for every `y` with `\bar Q(y)>0`, the retained likelihood ratio

\[
\bar L(y)=\frac{\bar P(y)}{\bar Q(y)}.
\]

Under the joint law `Q(x)K(y|x)`, one has the exact conditional-expectation identity

\[
\bar L(Y)=\mathbb E_Q[L(X)\mid Y].
\]

Let `f:(0,\infty)\to\mathbb R` be convex with `f(1)=0`, and define the finite `f`-divergence

\[
D_f(P\|Q)=\sum_x Q(x)f(L(x)).
\]

Then:

1. the loss of `f`-divergence under the channel is exactly the conditional Jensen gap
   \[
   \Delta_f(K;P,Q)
   :=D_f(P\|Q)-D_f(\bar P\|\bar Q)
   \]
   \[
   =\sum_y \bar Q(y)
   \left(
   \mathbb E_Q[f(L(X))\mid Y=y]
   -f(\mathbb E_Q[L(X)\mid Y=y])
   \right)
   \ge0;
   \]
2. if `f` is strictly convex on the convex hull of the likelihood-ratio values `L(X)`, then
   \[
   \Delta_f(K;P,Q)=0
   \]
   if and only if every retained output mixes only upstream states having the same likelihood ratio:
   \[
   K(y\mid x)>0,\ K(y\mid x')>0
   \Longrightarrow
   L(x)=L(x')
   \]
   for every `y` with `\bar Q(y)>0`;
3. that condition is equivalent to **binary statistical sufficiency** of the compression: there exists a reverse channel `R:X\leftarrow Y` such that
   \[
   \bar P R=P,
   \qquad
   \bar Q R=Q;
   \]
4. consequently, for a fixed binary experiment `(P,Q)`, equality for **one** strictly convex `f`-divergence already implies equality for **every** convex `f`-divergence and preserves the complete Blackwell decision content of the pair;
5. for a deterministic compression `T:X\to Y`, binary sufficiency holds exactly when the likelihood ratio factors through `T`. Therefore the likelihood-ratio partition
   \[
   x\sim x'
   \iff
   L(x)=L(x')
   \]
   is the coarsest deterministic representation that is lossless for the binary experiment;
6. for the Pearson generator
   \[
   f(t)=(t-1)^2,
   \]
   the divergence loss is precisely AF-009's conditional-variance fidelity defect applied to the likelihood ratio under `Q`:
   \[
   \Delta_{\chi^2}(K;P,Q)
   =\mathbb E_Q[\operatorname{Var}_Q(L(X)\mid Y)];
   \]
7. for the Kullback-Leibler generator
   \[
   f(t)=t\log t,
   \]
   the loss is the conditional relative entropy
   \[
   D(P\|Q)-D(\bar P\|\bar Q)
   =\sum_y \bar P(y)
   D(P_{X\mid y}\|Q_{X\mid y});
   \]
8. for a chain of garblings `X -> Y -> Z`, the loss composes additively:
   \[
   \Delta_f(X\to Z)
   =\Delta_f(X\to Y)+\Delta_f(Y\to Z),
   \]
   with both terms nonnegative. Hence once a strictly convex divergence has dropped at an intermediate stage, no later garbling can restore binary statistical fidelity without new side information.

The mathematics is classical `f`-divergence data processing, likelihood-ratio sufficiency, conditional Jensen equality, and Blackwell comparison of experiments. The Arithmetic Fidelity contribution is organizational: **all strictly convex `f`-divergences have the same exact zero-loss set for a fixed binary compression**, even though they assign different quantitative penalties away from that set. The surviving structural object is the likelihood-ratio partition, not the full upstream state.

## Derivation

### Retained likelihood ratio is a conditional expectation

Under the reference law `Q`, the joint distribution of `(X,Y)` is

\[
J_Q(x,y)=Q(x)K(y\mid x).
\]

For `\bar Q(y)>0`, the conditional law is

\[
Q(x\mid y)
=\frac{Q(x)K(y\mid x)}{\bar Q(y)}.
\]

Therefore

\[
\mathbb E_Q[L(X)\mid Y=y]
=\sum_x \frac{Q(x)K(y\mid x)}{\bar Q(y)}\frac{P(x)}{Q(x)}
\]

\[
=\frac{\sum_x P(x)K(y\mid x)}{\bar Q(y)}
=\frac{\bar P(y)}{\bar Q(y)}
=\bar L(y).
\]

Thus stochastic compression acts on the binary discriminator `L` by conditional expectation.

### Data processing is conditional Jensen

Using the previous identity,

\[
D_f(\bar P\|\bar Q)
=\sum_y \bar Q(y)f(\bar L(y))
\]

\[
=\mathbb E_Q\left[
 f\!\left(\mathbb E_Q[L(X)\mid Y]\right)
\right].
\]

Meanwhile

\[
D_f(P\|Q)=\mathbb E_Q[f(L(X))].
\]

Hence

\[
\boxed{
\Delta_f(K;P,Q)
=\mathbb E_Q\left[
 f(L)-f(\mathbb E_Q[L\mid Y])
\right]
}
\]

with the more explicit fiberwise form stated in the claim. Conditional Jensen gives nonnegativity immediately.

This identifies the precise object being averaged away: not arbitrary upstream information, but fluctuations of the likelihood ratio inside retained-output fibers/supports.

### Strict convexity makes zero divergence loss equivalent to likelihood-ratio constancy

Assume `f` is strictly convex on the convex hull of `L(X)`. Every term in the conditional Jensen gap is nonnegative. Equality of the total gap therefore requires equality in Jensen for every `y` with positive `\bar Q(y)`.

Strict convexity gives equality exactly when the random variable `L(X)` is constant under `Q(\cdot\mid y)`. Since `Q(x)>0`, this is equivalent to

\[
K(y\mid x)>0,\ K(y\mid x')>0
\Longrightarrow
L(x)=L(x').
\]

Conversely, if every output support is likelihood-ratio monochromatic, then

\[
L(X)=\bar L(Y)
\]

almost surely under the joint `Q` law, so every conditional Jensen gap vanishes.

Therefore, for any strictly convex generator in the declared range,

\[
\boxed{
D_f(P\|Q)=D_f(PK\|QK)
\iff
L(X)\text{ is recoverable from }Y.
}
\]

This is an exact structural criterion, not merely a scalar monotonicity statement.

### Likelihood-ratio constancy constructs an explicit reverse channel

Define the `Q`-posterior reverse channel

\[
R(x\mid y)
=\frac{Q(x)K(y\mid x)}{\bar Q(y)}
\]

for `\bar Q(y)>0`, with arbitrary values on never-observed outputs.

By construction,

\[
(\bar Q R)(x)
=\sum_y \bar Q(y)R(x\mid y)
=Q(x)\sum_y K(y\mid x)
=Q(x).
\]

Now assume likelihood-ratio constancy on every output support. Whenever `K(y|x)>0`, one has

\[
\bar L(y)=L(x).
\]

Therefore

\[
(\bar P R)(x)
=\sum_y \bar P(y)\frac{Q(x)K(y\mid x)}{\bar Q(y)}
\]

\[
=Q(x)\sum_y \bar L(y)K(y\mid x)
=Q(x)L(x)
=P(x).
\]

Thus the same reverse channel reconstructs both hypotheses:

\[
\boxed{
PKR=P,
\qquad
QKR=Q.
}
\]

This is the finite binary form of statistical sufficiency / Blackwell equivalence.

Conversely, if such an `R` exists, then applying the data-processing inequality first through `K` and then through `R` gives

\[
D_f(P\|Q)
\ge D_f(PK\|QK)
\ge D_f(PKR\|QKR)
=D_f(P\|Q).
\]

Hence equality holds for every convex `f`. Combining this with the strict-convexity argument proves the common zero-loss set:

\[
\boxed{
\text{equality for one strictly convex }f
\iff
\text{binary sufficiency}
\iff
\text{equality for every convex }f.
}
\]

### Deterministic compression has a canonical coarsest sufficient quotient

Let `K` be deterministic, induced by `T:X\to Y`. Then each output support is exactly a fiber of `T`, so the criterion becomes

\[
T(x)=T(x')
\Longrightarrow
L(x)=L(x').
\]

Equivalently, there exists `\ell:T(X)\to(0,\infty)` such that

\[
L=\ell\circ T.
\]

Therefore every deterministic sufficient statistic must refine the partition into equal-likelihood-ratio classes. Conversely, the map

\[
x\mapsto L(x)
\]

is itself sufficient, because its fibers are likelihood-ratio monochromatic. Thus the likelihood-ratio quotient is the coarsest deterministic sufficient representation for the binary pair, up to relabeling of its values.

This is materially different from AF-001's unrestricted lift problem. There, an arbitrary target-carrying mark makes recovery trivial. Here the binary model itself determines a canonical decision-equivalence relation: upstream states are interchangeable exactly when they carry the same evidence ratio between `P` and `Q`.

### Pearson chi-square loss is AF-009 on the likelihood ratio

For

\[
f(t)=(t-1)^2,
\]

one has

\[
D_{\chi^2}(P\|Q)
=\mathbb E_Q[(L-1)^2].
\]

Since

\[
\mathbb E_Q[L]=1,
\]

this is simply

\[
\operatorname{Var}_Q(L).
\]

The output likelihood ratio is

\[
\bar L(Y)=\mathbb E_Q[L\mid Y],
\]

so

\[
D_{\chi^2}(PK\|QK)
=\operatorname{Var}_Q(\mathbb E_Q[L\mid Y]).
\]

The law of total variance gives

\[
\boxed{
\Delta_{\chi^2}(K;P,Q)
=\mathbb E_Q[\operatorname{Var}_Q(L\mid Y)].
}
\]

This is exactly AF-009's scalar conditional-variance defect with discriminator `D=L(X)` and probability law `Q`.

Hence AF-009 is not merely adjacent to divergence data processing: for binary statistical discrimination, its quadratic defect is the Pearson `\chi^2` information lost by the compression.

### KL loss resolves into conditional hypothesis information

For

\[
f(t)=t\log t,
\]

write

\[
P(x\mid y)
=\frac{P(x)K(y\mid x)}{\bar P(y)},
\qquad
Q(x\mid y)
=\frac{Q(x)K(y\mid x)}{\bar Q(y)}.
\]

On their common support,

\[
\frac{P(x\mid y)}{Q(x\mid y)}
=\frac{L(x)}{\bar L(y)}.
\]

Therefore

\[
\sum_y \bar P(y)D(P_{X\mid y}\|Q_{X\mid y})
\]

\[
=\sum_{x,y}P(x)K(y\mid x)
\log\frac{L(x)}{\bar L(y)}
\]

\[
=D(P\|Q)-D(\bar P\|\bar Q).
\]

So KL loss has a direct interpretation: it is precisely the residual hypothesis-distinguishing information still present in `X` after `Y` is known.

It vanishes exactly when the conditional law of the upstream state given the retained output is the same under both hypotheses.

### Composition localizes irreversible loss

For a second channel `M: Y\rightsquigarrow Z`, define

\[
P_Z=PKM,
\qquad
Q_Z=QKM.
\]

Then algebraically

\[
D_f(P\|Q)-D_f(P_Z\|Q_Z)
\]

\[
=\left[D_f(P\|Q)-D_f(PK\|QK)\right]
+\left[D_f(PK\|QK)-D_f(P_Z\|Q_Z)\right].
\]

Each bracket is nonnegative by data processing. Hence

\[
\boxed{
\Delta_f(KM;P,Q)
=\Delta_f(K;P,Q)
+\Delta_f(M;PK,QK).
}
\]

If the first term is positive for a strictly convex `f`, the total loss remains positive under every downstream garbling. Statistical decision information destroyed by `K` cannot be manufactured later by processing `Y` alone.

This is the binary-experiment analogue of AF-001's deterministic factorization obstruction and AF-011's monotone growth of support-confusability.

## Strict convexity is essential

A non-strict generator may preserve its scalar divergence even though the channel is not sufficient.

Take

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
L(c)=17/10.
\]

Their `Q`-mean is `1`, so they define a valid positive distribution `P=QL`. Let a deterministic compression merge `a` and `b` while retaining `c` separately.

The merged fiber is not sufficient because

\[
L(a)\ne L(b).
\]

But for total variation,

\[
f(t)=\frac12|t-1|,
\]

`f` is affine on `(0,1)` and both merged ratios lie on that same affine branch. Therefore Jensen is an equality on the merged fiber, and total variation is unchanged by the compression despite the lost likelihood-ratio distinction.

Thus

\[
\boxed{
\text{equality of one arbitrary divergence}
\not\Rightarrow
\text{statistical fidelity}.
}
\]

The certification result requires a generator whose strict convexity covers the likelihood-ratio range actually mixed by the channel.

## Relationship to AF-001, AF-009, and AF-011

AF-001 asks whether a declared statewise discriminator `d(x)` factors through a deterministic compression. AF-012 instead treats a **binary statistical experiment**: the relevant retained object is the likelihood ratio `P/Q`, because that is the complete evidence coordinate for deciding between the two hypotheses.

AF-009 quantifies average squared recovery of an arbitrary random discriminator. AF-012 identifies one canonical discriminator induced by a binary experiment, `L=P/Q`, and shows that the AF-009 defect for that discriminator is exactly Pearson `\chi^2` divergence loss. Other strictly convex `f`-divergences change the geometry of the quantitative penalty while preserving the same exact zero-loss condition.

AF-011 uses support overlap to ask whether a statewise discriminator can be recovered with zero error for every possible channel outcome. AF-012 is weaker in a deliberate decision-theoretic sense: an output may mix many upstream states without loss as long as those states have identical likelihood ratio. Such states are different as upstream points but statistically interchangeable for the declared pair `(P,Q)`.

This gives three distinct stochastic notions that should not be conflated:

\[
\text{statewise zero-error fidelity}
\quad\leftrightarrow\quad
\text{support confusability},
\]

\[
\text{quadratic discriminator fidelity}
\quad\leftrightarrow\quad
\text{conditional variance},
\]

and

\[
\text{full binary decision fidelity}
\quad\leftrightarrow\quad
\text{likelihood-ratio sufficiency}.
\]

## Prior art and novelty assessment

The core theorem is classical statistical information theory.

Kullback and Leibler's 1951 paper *On Information and Sufficiency* directly connects information loss under a statistic with statistical sufficiency. Ali and Silvey's 1966 paper develops the general convex class of divergence coefficients generated from the Radon-Nikodym likelihood ratio. Csiszár's 1967 paper *Information-type measures of difference of probability distributions and indirect observations* is foundational prior art for `f`-divergence monotonicity under indirect observation. Liese's 2012 paper *φ-divergences, sufficiency, Bayes sufficiency, and deficiency* explicitly studies the relation between `φ`-divergences and sufficiency/decision-theoretic information.

Accordingly, no novelty is claimed for `f`-divergence data processing, likelihood-ratio sufficiency, equality characterization, or Blackwell recoverability. The finite proof above is included so that the exact structural criterion is auditable without importing a broad theorem as a black box.

The Arithmetic Fidelity contribution is the placement of these classical results inside the developing compression taxonomy:

- the **likelihood-ratio partition** is the canonical binary decision quotient;
- every strictly convex `f`-divergence has the same exact fidelity boundary for a fixed binary compression;
- AF-009's conditional variance becomes exactly the `\chi^2` member of this family when the discriminator is the likelihood ratio;
- a strict divergence drop is a reusable no-go certificate for every later garbling of that representation.

## Boundaries and failure modes

- The theorem is stated for finite `X,Y` and strictly positive `P,Q` to keep support and Radon-Nikodym issues explicit. Standard measure-theoretic extensions exist but require care with singular parts and almost-sure equivalence.
- Statistical sufficiency is relative to the declared pair `(P,Q)`. A channel may be perfectly sufficient for that pair while destroying information needed for a third hypothesis or another mathematical discriminator.
- The likelihood ratio is canonical only after the binary experiment has been independently specified. Choosing `P` and `Q` so that `P/Q` secretly encodes the desired answer would merely move target leakage into the model definition.
- Equality is an exact criterion. A small `f`-divergence loss need not, by itself, imply a small Blackwell deficiency or a uniformly small loss for all decision problems without additional quantitative assumptions.
- Non-strict generators can have flat/affine regions and may show equality despite genuine statistical loss, as the total-variation example demonstrates.
- Different strictly convex generators share the same zero-loss set but can rank **approximate** compressions differently. There is no universal scalar notion of near-fidelity supplied by this theorem.
- A reverse channel certifies recovery of the two probability laws, not pointwise reconstruction of the original upstream state. This is decision-equivalence, not injectivity.
- No claim is made that a natural probability pair `(P,Q)` has yet been identified for rational primes or for any existing Mathia RH construction.

## Decisive audit test for binary statistical compression

When a proposed representation is intended to preserve all information relevant to distinguishing two probabilistic models `P` and `Q`:

1. compute the upstream likelihood ratio `L=P/Q` on the declared support;
2. for each retained output, determine whether all upstream states that can produce it have the same likelihood ratio;
3. equivalently, evaluate one strictly convex `f`-divergence before and after compression; any strict drop proves that the channel is not sufficient;
4. if equality holds, construct or verify the reverse channel rather than inferring more than binary decision fidelity;
5. for deterministic compression, compare its fibers with the likelihood-ratio partition to determine whether the representation is finer than the coarsest sufficient quotient;
6. use the `\chi^2` generator when an AF-009 conditional-variance interpretation is useful, and KL when conditional hypothesis information is the useful decomposition;
7. do not use equality of a non-strict divergence as a sufficiency certificate without checking its Jensen equality set;
8. under composition, localize the first stage at which a strict divergence drop occurs: later garblings cannot repair it.

## Consequence for the line

Add **binary statistical sufficiency / likelihood-ratio fidelity** as a third canonical stochastic model beside AF-009's average discriminator defect and AF-011's supportwise zero-error criterion.

This is the first probabilistic setting in the line where a genuinely canonical minimal retained representation appears without an arbitrary lift library: once the binary experiment `(P,Q)` is fixed, the likelihood-ratio partition is the coarsest deterministic representation preserving all decision information for that pair.

For later arithmetic applications, this suggests a sharper question than asking whether a compression preserves a large amount of information. If rational primes and a matched control can be represented by an independently motivated statistical experiment, the relevant audit is whether the compression preserves their likelihood-ratio partition—or equivalently whether a strictly convex divergence is exactly conserved. Until such a natural pair is identified, this remains a general structural theorem rather than evidence about RH.