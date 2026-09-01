# AF-050 — f-divergence zero-error repair reduces to binary retained-mass penalties

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

and assume `|Y|\ge m`. Let `K:X\rightsquigarrow Y` be a stochastic channel and fix a strictly positive prior

\[
\pi_x>0,
\qquad
\sum_x\pi_x=1.
\]

Let `\mathcal Z_d^{(0)}` be AF-011's zero-error faithful set: rows belonging to distinct discriminator classes have disjoint output supports.

Let `f:[0,\infty)\to(-\infty,+\infty]` be convex and lower semicontinuous, finite on `(0,\infty)`, and normalized by `f(1)=0`. Write

\[
f_0:=f(0)=\lim_{t\downarrow0}f(t),
\qquad
f_\infty:=\lim_{t\to\infty}\frac{f(t)}{t},
\]

with either endpoint allowed to be `+\infty`. On a finite alphabet use the standard extended Csiszár divergence

\[
D_f(P\|Q)
=
\sum_{y:Q(y)>0}Q(y)
 f\!\left(\frac{P(y)}{Q(y)}\right)
+
f_\infty\sum_{y:Q(y)=0}P(y).
\]

For `p\in[0,1]` define the two binary support-penalty functions

\[
\Psi_f(p)
:=
\begin{cases}
f(p)+(1-p)f_\infty,&p>0,\\
f_0+f_\infty,&p=0,
\end{cases}
\]

and

\[
\Phi_f(p)
:=
\begin{cases}
p f(1/p)+(1-p)f_0,&p>0,\\
f_\infty+f_0,&p=0.
\end{cases}
\]

Then:

1. **Projection onto one prescribed support cell is exactly binary.** For every probability distribution `P` on `Y` and every nonempty `S\subseteq Y`, with `p=P(S)`,
   \[
   \boxed{
   \inf_{Q:\operatorname{supp}(Q)\subseteq S}
   D_f(P\|Q)
   =\Psi_f(p),
   }
   \]
   and
   \[
   \boxed{
   \inf_{Q:\operatorname{supp}(Q)\subseteq S}
   D_f(Q\|P)
   =\Phi_f(p).
   }
   \]
   If `p>0`, the conditional law
   \[
   Q=P(\,\cdot\mid S)
   \]
   attains both infima. Strict convexity is not needed for attainment; without it the minimizer need not be unique.

2. **Every prior-weighted row-separable f-divergence repair of zero-error fidelity has the same partition geometry.** For a partition into nonempty class cells
   \[
   Y=\bigsqcup_{a\in A}Y_a,
   \]
   set
   \[
   p_x(Y_\bullet)=K_x(Y_{d(x)}).
   \]
   Then
   \[
   \boxed{
   \inf_{L\in\mathcal Z_d^{(0)}}
   \sum_x\pi_xD_f(K_x\|L_x)
   =
   \min_{Y=\bigsqcup_aY_a}
   \sum_x\pi_x\Psi_f(p_x(Y_\bullet)),
   }
   \]
   and
   \[
   \boxed{
   \inf_{L\in\mathcal Z_d^{(0)}}
   \sum_x\pi_xD_f(L_x\|K_x)
   =
   \min_{Y=\bigsqcup_aY_a}
   \sum_x\pi_x\Phi_f(p_x(Y_\bullet)).
   }
   \]
   Thus changing the f-divergence does not create a new zero-error support combinatorics: the discrete variable is always the same nonempty class partition of `Y`; only the scalar cost assigned to each retained row mass changes.

3. **The two endpoint constants classify which support surgery is finite.** For every nontrivial retained mass `0<p<1`,
   \[
   \Psi_f(p)<\infty
   \iff
   f_\infty<\infty,
   \]
   while
   \[
   \Phi_f(p)<\infty
   \iff
   f_0<\infty.
   \]
   Therefore forward repair `D_f(K\|L)` can delete positive original mass at finite cost exactly when the recession slope is finite, whereas reverse repair `D_f(L\|K)` can do so exactly when the zero endpoint is finite. If `p=0`, a repair cell must create all of its row mass on outputs absent from the original row, and either direction has finite cost exactly when both endpoint quantities are finite.

4. **The classification is intrinsic to the divergence, not to a chosen generator normalization.** Replacing
   \[
   f(t)\mapsto f(t)+c(t-1)
   \]
   leaves `D_f` unchanged. It sends
   \[
   f_0\mapsto f_0-c,
   \qquad
   f_\infty\mapsto f_\infty+c,
   \]
   but the affine terms cancel exactly in both `\Psi_f` and `\Phi_f`. Hence the retained-mass penalties and their finiteness barriers are invariant under the standard affine ambiguity of f-divergence generators.

5. **AF-047 and AF-049 are special cases of one endpoint taxonomy.** With the normalizations below:

   - total variation, `f(t)=|t-1|/2`, has `f_0=f_\infty=1/2` and
     \[
     \Psi_f(p)=\Phi_f(p)=1-p;
     \]
   - Kullback--Leibler, `f(t)=t\log t`, has `f_0=0`, `f_\infty=+\infty`, so
     \[
     \Psi_f(p)=+\infty\quad(0\le p<1),
     \qquad
     \Phi_f(p)=-\log p\quad(p>0);
     \]
   - squared Hellinger, `f(t)=(\sqrt t-1)^2`, has `f_0=f_\infty=1` and
     \[
     \Psi_f(p)=\Phi_f(p)=2(1-\sqrt p);
     \]
   - Pearson chi-square, `f(t)=(t-1)^2`, has `f_0=1`, `f_\infty=+\infty`, so forward nontrivial support deletion is infinite while
     \[
     \Phi_f(p)=\frac{1-p}{p}
     \qquad(p>0).
     \]

6. **Metric-by-metric exploration inside this class is structurally bounded.** Once the target is AF-011 zero-error fidelity and the discrepancy is a prior-weighted sum of rowwise Csiszár f-divergences, every new choice of `f` can change the retained-mass welfare/penalty landscape and computational optimization, but it cannot alter the underlying class-partition constraint. A qualitatively different repair geometry must therefore change at least one of: the target fidelity notion, the row aggregation, the admissible coupling between repaired rows, or the divergence family itself.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{for zero-error support fidelity, row-separable f-divergence repair}
=
\text{one universal partition problem plus a direction-dependent binary penalty.}
}
\]

The endpoint pair `(f_0,f_\infty)` decides whether deleting or creating support is even visible at finite cost; the interior shape of `f` decides how the surviving mass is graded once that surgery is permitted.

## Derivation

### The extended finite f-divergence and binary coarse graining

For finite measures, the extended definition above is the usual perspective extension of `q f(p/q)` to `q=0`: positive `P`-mass singular to `Q` is charged at recession rate `f_\infty`. Convexity and `f(1)=0` give the data-processing inequality for every deterministic or stochastic coarse graining.

Fix a nonempty cell `S\subseteq Y`, put `p=P(S)`, and let

\[
C:Y\to\{0,1\}
\]

record membership in `S`. If `Q` is supported on `S`, then

\[
PC=(p,1-p),
\qquad
QC=(1,0).
\]

Data processing therefore gives

\[
D_f(P\|Q)
\ge
D_f((p,1-p)\|(1,0)).
\]

For `p>0` the right-hand side is exactly

\[
f(p)+(1-p)f_\infty
=\Psi_f(p).
\]

For `p=0` it is `f_0+f_\infty` in the extended sense.

Now assume `p>0` and choose

\[
Q=P(\,\cdot\mid S).
\]

For `y\in S` with `Q(y)>0`,

\[
\frac{P(y)}{Q(y)}=p,
\]

so the contribution from `S` is `f(p)`. Outside `S`, `Q=0` and the total singular `P`-mass is `1-p`, contributing `(1-p)f_\infty`. Hence

\[
D_f(P\|P(\cdot\mid S))
=\Psi_f(p),
\]

which attains the data-processing lower bound.

If `p=0`, every probability `Q` supported on `S` has `P=0` on its support and `Q=0` on the full `P`-support outside `S`. The two singular endpoint contributions are exactly `f_0` and `f_\infty`, so the same formula remains exact.

### Reverse direction swaps the two endpoint roles

Apply the same coarse graining with the arguments reversed:

\[
QC=(1,0),
\qquad
PC=(p,1-p).
\]

Therefore

\[
D_f(Q\|P)
\ge
D_f((1,0)\|(p,1-p)).
\]

For `p>0` this binary divergence equals

\[
p f(1/p)+(1-p)f_0
=\Phi_f(p).
\]

Conditioning again attains equality because inside `S`

\[
\frac{Q(y)}{P(y)}=\frac1p,
\]

while outside `S` the repaired law is zero and contributes `(1-p)f_0`. If `p=0`, unit repaired mass is singular to `P` on `S` and all original mass lies outside the repair support, giving `f_\infty+f_0`.

Thus the direction asymmetry of AF-049 is not peculiar to logarithms. Forward and reverse support surgery exchange the generator's zero endpoint and recession endpoint. Equivalently, under the standard reversed generator

\[
f^\diamond(t)=t f(1/t),
\]

one has the endpoint swap

\[
f^\diamond_0=f_\infty,
\qquad
f^\diamond_\infty=f_0,
\]

and correspondingly

\[
\Phi_f=\Psi_{f^\diamond}.
\]

### The penalty functions are monotone without a calculus argument

If `S\subseteq S'`, then the family of probability distributions supported on `S` is contained in the family supported on `S'`. Hence either directional projection cost cannot increase when the permitted support grows.

Because the one-cell projection depends on `S` only through `P(S)`, this proves directly that

\[
\Psi_f(p),\qquad\Phi_f(p)
\]

are nonincreasing on the attainable retained-mass values. This variational monotonicity is what permits the zero-error support unions below to be enlarged to a full partition without weakening the lower bound incorrectly.

### Every zero-error channel reduces to a class partition

Take any

\[
L\in\mathcal Z_d^{(0)}.
\]

For each discriminator class `a\in A`, define its used output support

\[
S_a
=
\bigcup_{x:d(x)=a}\operatorname{supp}(L_x).
\]

Every `S_a` is nonempty, and AF-011 gives

\[
S_a\cap S_b=\varnothing
\qquad(a\ne b).
\]

Assign every unused output symbol to an arbitrary class, obtaining a partition

\[
Y=\bigsqcup_{a\in A}Y_a,
\qquad
S_a\subseteq Y_a.
\]

For every row `x` of class `a`, the one-cell theorem and monotonicity give

\[
D_f(K_x\|L_x)
\ge
\Psi_f(K_x(S_a))
\ge
\Psi_f(K_x(Y_a)),
\]

and similarly

\[
D_f(L_x\|K_x)
\ge
\Phi_f(K_x(S_a))
\ge
\Phi_f(K_x(Y_a)).
\]

Summing with the positive prior yields the two partition lower bounds.

Conversely, choose any partition `Y=\bigsqcup_aY_a`. For every row with positive retained mass

\[
p_x=K_x(Y_{d(x)})>0,
\]

set

\[
L_x=K_x(\,\cdot\mid Y_{d(x)}).
\]

For a row with `p_x=0`, choose any probability distribution supported inside its nonempty class cell. All repaired rows of class `a` then live inside `Y_a`, so `L\in\mathcal Z_d^{(0)}`. The one-cell formulas attain the corresponding `\Psi_f(p_x)` or `\Phi_f(p_x)` row by row, including the extended `p_x=0` case. Since there are finitely many partitions of finite `Y`, a minimizing partition exists in the extended-valued sense.

This proves both exact zero-error repair formulas.

## Endpoint taxonomy and examples

The assumption that `f` is finite on `(0,\infty)` isolates all support singularities at the two endpoints.

For `0<p<1`, `f(p)` and `f(1/p)` are finite. Therefore

\[
\Psi_f(p)<\infty
\iff
f_\infty<\infty,
\]

and

\[
\Phi_f(p)<\infty
\iff
f_0<\infty.
\]

This produces three qualitatively different regimes before any global partition optimization is solved:

- **both endpoints finite:** support mass may be deleted in either direction at finite cost; TV and squared Hellinger lie here;
- **only `f_0` finite:** reverse repair can delete original support mass but forward repair cannot; ordinary KL and Pearson chi-square lie here;
- **only `f_\infty` finite:** the directional mirror image; forward deletion can be finite while reverse deletion is singular.

At `p=0`, deletion alone is no longer the whole operation. The repaired row must place probability one on a cell that the original row never visits. Both the zero endpoint and recession endpoint occur, so finite repair requires both to be finite.

The standard generator ambiguity does not disturb this taxonomy. If

\[
g(t)=f(t)+c(t-1),
\]

then

\[
g_0=f_0-c,
\qquad
g_\infty=f_\infty+c.
\]

For `p>0`,

\[
\begin{aligned}
\Psi_g(p)
&=f(p)+c(p-1)+(1-p)(f_\infty+c)\\
&=\Psi_f(p),
\end{aligned}
\]

and

\[
\begin{aligned}
\Phi_g(p)
&=p\left[f(1/p)+c(1/p-1)\right]
 +(1-p)(f_0-c)\\
&=\Phi_f(p).
\end{aligned}
\]

So the classification depends on the divergence itself rather than on a cosmetic generator choice.

## Relationship to AF-012, AF-047, AF-048, and AF-049

AF-012 studies a different use of the same divergence family: equality in data processing for a **fixed statistical experiment**. There, strict convexity makes zero f-divergence loss equivalent to likelihood-ratio sufficiency. The present result instead fixes AF-011's **zero-error support target** and asks for the nearest repaired channel. Strict convexity is not required because the key projection lower bound is attained by conditioning even when other minimizers may coexist.

AF-047 is recovered by total variation. Its rowwise cost `1-p_x` is exactly `\Psi_f=\Phi_f`, after which prior-weighted summation turns the partition problem into retained class mass and exposes the extra Hall coverage term relative to unconstrained Bayes classification.

AF-049 is recovered by KL. Its infinite forward barrier is exactly `f_\infty=+\infty`; its reverse penalty `-\log p_x` is exactly `\Phi_f`, and the resulting weighted product is the exponentiated sum of those binary row penalties.

AF-048 remains genuinely distinct. It changes the **row aggregation** from a prior-weighted sum to a row-sup total-variation objective, producing max-min allocation rather than merely substituting another f-divergence inside the same additive aggregation.

This separation is useful for future work. If a proposed new metric produces a different global geometry, one should first ask which structural ingredient actually changed: the row penalty, the aggregation across rows, the coupling constraints, or the target notion of fidelity.

## Prior art and novelty audit

The f-divergence mechanism is classical and is not claimed as a new theorem of information theory.

- S. M. Ali and S. D. Silvey, **“A General Class of Coefficients of Divergence of One Distribution from Another,”** *Journal of the Royal Statistical Society, Series B* 28(1), 131--142 (1966), DOI `10.1111/j.2517-6161.1966.tb00626.x`, is foundational prior art for convex likelihood-ratio divergences encompassing many of the examples used here.
- Imre Csiszár, **“Information-type measures of difference of probability distributions and indirect observations,”** *Studia Scientiarum Mathematicarum Hungarica* 2, 299--318 (1967), is foundational prior art for f-divergence under indirect observation and the partition/data-processing inequality. The one-support-cell projection above is an elementary finite binary specialization of that mechanism.
- Friedrich Liese and Igor Vajda, **“On Divergences and Informations in Statistics and Information Theory,”** *IEEE Transactions on Information Theory* 52(10), 4394--4412 (2006), DOI `10.1109/TIT.2006.881731`, surveys and develops the basic f-divergence, information, sufficiency, and deficiency framework and confirms that KL, total variation, Hellinger, Pearson and related measures belong to one mature class.
- A. A. Gushchin, **“On an Extension of the Notion of f-Divergence,”** *Theory of Probability and Its Applications* 52(3), 439--455 (2008), DOI `10.1137/S0040585X97983134`, gives an extended lower-semicontinuous convex formulation equivalent to classical Csiszár divergence for probability measures and studies f-divergence minimization. It is the closest authoritative boundary for the singular endpoint convention used here.

No novelty is claimed for f-divergence data processing, the partition inequality, the perspective/recession extension, conditional f-projections, or the individual TV/KL/Hellinger/Pearson formulas.

The durable Arithmetic Fidelity result is the **cross-metric structural closure** obtained by applying those classical ingredients to the same AF-011 target. The exact zero-error repair problem for the whole prior-weighted row-separable Csiszár class has one universal partition skeleton; divergence direction and generator enter only through the binary functions `\Psi_f` and `\Phi_f`. Consequently, replacing one rowwise f-divergence by another cannot by itself escape the class-partition compression geometry. The endpoint taxonomy also explains, without metric-specific rederivation, when support deletion or support creation becomes infinitely expensive.

## Boundaries and falsification checks

- The theorem is finite-alphabet. Measure-theoretic extensions require measurable partitions, existence/attainment checks, and care with singular components; none is inferred here automatically.
- `|Y|\ge|A|` is the exact nonemptiness condition for AF-011's zero-error target. If it fails, there is no faithful repair channel to optimize over.
- The prior is assumed strictly positive so an infinite or positive repair cost on any upstream row cannot be hidden by zero weight. The rowwise projection formulas themselves do not require this assumption.
- Convexity and the standard extended f-divergence convention are essential. A generic Bregman, Wasserstein, integral-probability, or non-row-separable discrepancy need not reduce to the binary penalties above.
- The result classifies **support repair**, not full reconstruction of `X`. Rows inside one discriminator class may still collapse arbitrarily because AF-011 asks only for exact recovery of `d(X)`.
- Strict convexity would sharpen uniqueness/equality statements for the projection but is intentionally not assumed; the classification concerns the optimal value and an attaining conditional repair.
- Endpoint finiteness is an admissibility boundary, not a statement that two finite penalties are quantitatively equivalent. Different finite `\Psi_f` or `\Phi_f` can still produce different optimal partitions and different computational hardness.
- The theorem does not subsume AF-048's row-sup geometry or any repair that couples rows through additional constraints. Those are explicit matched controls showing where the classification stops.

A decisive falsification would be a finite zero-error instance with a standard Csiszár f-divergence and prior-weighted row-sum aggregation whose exact optimum cannot be represented by the declared nonempty class partition and the corresponding binary retained-mass penalties. The proof above reduces every admissible repair to such a partition and constructs an attaining repair for every partition, so within the stated hypotheses no such counterexample remains.