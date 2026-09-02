# AF-054 — Maximal safe target envelopes classify repair-radius invariance under isometric refinement

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`

## Claim

Let `(X,d_X)` and `(Y,d_Y)` be metric spaces, let

\[
C:X\to Y
\]

be an isometric embedding, and let `S\subset X` be a nonempty structural target. Write

\[
r_S(x)=\operatorname{dist}_X(x,S).
\]

Define the **safe target envelope** of `S` under the refinement `C` by

\[
\mathcal E_C(S)
=
\left\{
 y\in Y:
 d_Y(Cx,y)\ge r_S(x)
 \text{ for every }x\in X
\right\}.
\]

Then:

1. **`\mathcal E_C(S)` is the unique maximal target enlargement that preserves every repair radius on the embedded source.** It is closed, contains `C(\overline S)`, and for every nonempty `R\subset Y` satisfying
   \[
   C(S)\subseteq R,
   \]
   one has
   \[
   \boxed{
   \operatorname{dist}_Y(Cx,R)=\operatorname{dist}_X(x,S)
   \ \forall x\in X
   \iff
   R\subseteq\mathcal E_C(S).
   }
   \]

2. **Every unsafe target point gives an explicit witness of presentation-induced contraction.** If `y\notin\mathcal E_C(S)`, then there exists `x\in X` such that
   \[
   d_Y(Cx,y)<r_S(x).
   \]
   Therefore every target `R` containing both `C(S)` and `y` satisfies
   \[
   \operatorname{dist}_Y(Cx,R)
   <
   \operatorname{dist}_X(x,S).
   \]
   A new degree of freedom can therefore reduce a repair radius even when the representation map itself is perfectly isometric.

3. **A nonexpansive retraction gives a simple sufficient descent rule.** Suppose in addition that there is a `1`-Lipschitz map
   \[
   M:Y\to X,
   \qquad
   M\circ C=\operatorname{id}_X.
   \]
   Then
   \[
   \boxed{
   M^{-1}(\overline S)
   \subseteq
   \mathcal E_C(S).
   }
   \]
   Hence every refined target `R` with
   \[
   C(S)\subseteq R
   \subseteq
   M^{-1}(\overline S)
   \]
   has exactly the same repair-radius function as the original target.

4. **Failure to descend controls the maximum possible contraction.** For such a split nonexpansive refinement define the one-sided descent defect
   \[
   \varepsilon_M(R,S)
   =
   \sup_{y\in R}
   \operatorname{dist}_X(My,S)
   \in[0,\infty].
   \]
   If `C(S)\subseteq R`, then for every `x\in X`,
   \[
   \boxed{
   r_S(x)-\varepsilon_M(R,S)
   \le
   \operatorname{dist}_Y(Cx,R)
   \le
   r_S(x).
   }
   \]
   Equivalently,
   \[
   \boxed{
   0
   \le
   r_S(x)-\operatorname{dist}_Y(Cx,R)
   \le
   \varepsilon_M(R,S).
   }
   \]
   In particular `\varepsilon_M(R,S)=0` forces exact invariance.

5. **The same defect is a directed Hausdorff excess on the descended target.** Because `M(C(S))=S`, the assumption `C(S)\subseteq R` gives
   \[
   S\subseteq M(R).
   \]
   Thus
   \[
   \varepsilon_M(R,S)
   =
   \sup_{u\in M(R)}\operatorname{dist}_X(u,S),
   \]
   the one-sided Hausdorff excess of `M(R)` beyond `S`. Moreover
   \[
   \boxed{
   \operatorname{dist}_X(x,M(R))
   \le
   \operatorname{dist}_Y(Cx,R)
   \le
   \operatorname{dist}_X(x,S).
   }
   \]

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{an isometric refinement preserves distance to structure exactly only for target enlargements contained in a precise safe envelope.}
}
\]

Thus metric compatibility of the representation is not enough. The admissible **target family** must also be compatible with the declared presentation equivalence. AF-052 and AF-053 exhibited this phenomenon in finite stochastic channels; the result here isolates the general metric mechanism and gives both an exact maximality criterion and a quantitative descent-defect bound.

## Derivation

### The safe envelope is closed and contains the transported target

For fixed `x\in X`, the function

\[
y\mapsto d_Y(Cx,y)
\]

is continuous. Hence

\[
\{y:d_Y(Cx,y)\ge r_S(x)\}
\]

is closed. Intersecting over all `x` gives that `\mathcal E_C(S)` is closed.

Now take `s\in\overline S`. Since `C` is an isometry,

\[
d_Y(Cx,Cs)=d_X(x,s).
\]

By definition of distance to a set,

\[
d_X(x,s)\ge\operatorname{dist}_X(x,S)=r_S(x).
\]

Thus `Cs\in\mathcal E_C(S)` for every `s\in\overline S`, so

\[
C(\overline S)\subseteq\mathcal E_C(S).
\]

### Exact maximality of the envelope

Let `R\subset Y` be nonempty with `C(S)\subseteq R`. Because `C` is an isometry,

\[
\begin{aligned}
\operatorname{dist}_Y(Cx,R)
&\le
\operatorname{dist}_Y(Cx,C(S))\\
&=
\operatorname{dist}_X(x,S)\\
&=r_S(x).
\end{aligned}
\]

So every target enlargement can only decrease the repair radius on the embedded source.

If `R\subseteq\mathcal E_C(S)`, then every `y\in R` satisfies

\[
d_Y(Cx,y)\ge r_S(x)
\]

for every `x`. Taking the infimum over `y\in R` gives

\[
\operatorname{dist}_Y(Cx,R)\ge r_S(x).
\]

Together with the previous upper bound this yields equality for all `x`.

Conversely, suppose

\[
\operatorname{dist}_Y(Cx,R)=r_S(x)
\qquad\forall x\in X.
\]

For any fixed `y\in R`,

\[
d_Y(Cx,y)
\ge
\operatorname{dist}_Y(Cx,R)
=
r_S(x)
\]

for every `x`. Hence `y\in\mathcal E_C(S)`. Since `y` was arbitrary,

\[
R\subseteq\mathcal E_C(S).
\]

This proves the equivalence and the set-inclusion maximality of `\mathcal E_C(S)`.

### Unsafe points force contraction

The negation of the defining condition is exact:

\[
y\notin\mathcal E_C(S)
\iff
\exists x\in X:\ d_Y(Cx,y)<r_S(x).
\]

If `y\in R`, then

\[
\operatorname{dist}_Y(Cx,R)
\le d_Y(Cx,y)
<r_S(x).
\]

Thus an unsafe added repair is not merely potentially problematic: it necessarily lowers the repair-radius function at an explicit source witness.

### Nonexpansive descent implies safety

Assume now that `M:Y\to X` is `1`-Lipschitz and `MC=id_X`. Take `y\in Y` with

\[
My\in\overline S.
\]

For every `x\in X`, nonexpansiveness gives

\[
\begin{aligned}
d_Y(Cx,y)
&\ge d_X(MCx,My)\\
&=d_X(x,My)\\
&\ge r_S(x).
\end{aligned}
\]

Hence `y\in\mathcal E_C(S)`. Therefore

\[
M^{-1}(\overline S)
\subseteq
\mathcal E_C(S).
\]

This is stronger than requiring the refined target to be exactly `C(S)`: arbitrary vertical or presentation-specific target points are harmless whenever they descend to a valid source target under the nonexpansive retraction.

### Quantitative descent defect

Let

\[
\varepsilon
=
\varepsilon_M(R,S)
=
\sup_{y\in R}r_S(My).
\]

For any `x\in X` and `y\in R`, the point-to-set triangle inequality gives

\[
r_S(x)
\le
 d_X(x,My)+r_S(My).
\]

Therefore

\[
d_X(x,My)
\ge
r_S(x)-r_S(My)
\ge
r_S(x)-\varepsilon.
\]

Nonexpansiveness of `M` yields

\[
d_Y(Cx,y)
\ge
 d_X(MCx,My)
=
d_X(x,My).
\]

Thus every `y\in R` satisfies

\[
d_Y(Cx,y)
\ge
r_S(x)-\varepsilon.
\]

Taking the infimum over `R` proves

\[
\operatorname{dist}_Y(Cx,R)
\ge
r_S(x)-\varepsilon.
\]

The opposite inequality was already proved from `C(S)\subseteq R`.

There is also a useful intermediate sandwich. Since `M` is nonexpansive,

\[
d_X(x,My)
\le
 d_Y(Cx,y).
\]

Infimizing over `y\in R` gives

\[
\operatorname{dist}_X(x,M(R))
\le
\operatorname{dist}_Y(Cx,R).
\]

Because `S\subseteq M(R)`,

\[
\operatorname{dist}_X(x,M(R))
\le
r_S(x).
\]

The descent defect is exactly the one-sided excess

\[
\sup_{u\in M(R)}\operatorname{dist}_X(u,S),
\]

so the quantitative theorem is the standard stability of distance-to-set functions under one-sided Hausdorff enlargement, transported through a nonexpansive retraction.

## Exact controls

### A nontrivial safe envelope in a split refinement

Take

\[
X=\mathbb R,
\qquad
Y=\mathbb R^2
\]

with

\[
d_X(x,x')=|x-x'|,
\qquad
 d_Y((u,v),(u',v'))=|u-u'|+|v-v'|.
\]

Let

\[
C(x)=(x,0),
\qquad
M(u,v)=u,
\qquad
S=\{0\}.
\]

Then `C` is isometric, `M` is `1`-Lipschitz, and `MC=id`.

Here

\[
r_S(x)=|x|.
\]

A point `(u,v)` is safe exactly when

\[
|x-u|+|v|\ge|x|
\qquad\forall x\in\mathbb R.
\]

The triangle inequality shows this holds whenever `|v|\ge|u|`, and choosing `x=u` shows that condition is necessary. Therefore

\[
\boxed{
\mathcal E_C(\{0\})
=
\{(u,v):|v|\ge|u|\}.
}
\]

The safe target envelope can therefore be strictly larger than the transported target `C(S)=\{(0,0)\}` while remaining much smaller than the whole refined ambient space.

### The descent-defect coefficient is sharp

In the same split refinement choose `a>0` and `0<h<a`, and let

\[
R=\{(0,0),(a,h)\}.
\]

Then

\[
\varepsilon_M(R,S)=a.
\]

At the source point `x=a`,

\[
r_S(a)=a,
\]

while

\[
\operatorname{dist}_Y(Ca,R)
=
\min\{a,h\}
=h.
\]

Thus the contraction is

\[
a-h.
\]

As `h\downarrow0`, the ratio

\[
\frac{a-h}{\varepsilon_M(R,S)}
\to1.
\]

Hence the constant `1` in the descent-defect bound cannot be uniformly improved even for genuine off-image target additions in a split isometric refinement.

## Relation to AF-052 and AF-053

AF-052 uses uniform output cloning. On the fixed-prior channel spaces, the cloning map `C_k` is a total-variation isometric embedding and deterministic clone merging is a total-variation contraction with

\[
M_kC_k=id.
\]

The clone-compatible target

\[
C_k(\mathcal Z_d^{(0)})
\]

is therefore safe automatically. More generally, any refined target channel whose merge lies in the original zero-error set is safe by the nonexpansive descent rule above.

The unrestricted cloned zero-error target is larger. It contains channels that use clone labels as new class-separating support atoms even though merging those labels can destroy zero-error fidelity. Such channels need not lie in the safe envelope, and AF-052 computes the resulting contraction exactly.

AF-053 makes the same mechanism decisive under null-symbol stabilization. Adjoining zero-probability symbols leaves the source experiment unchanged, but the unrestricted refined target may repurpose those null coordinates into class-private repair mass. The retracted repaired channel need not belong to the source zero-error target, so the target fails the descent gate. AF-053 then shows that enough such unsafe target freedom collapses the Blackwell-relaxed TV repair radius all the way to Bayes error.

Thus the three findings separate three logically distinct ingredients:

\[
\text{representation geometry}
\quad+
\text{target transport}
\quad+
\text{equivalence/retraction}.
\]

An intrinsic repair radius requires all three to be compatible.

## Prior art and novelty assessment

The mathematical ingredients are classical.

- Dmitri Burago, Yuri Burago, and Sergei Ivanov, ***A Course in Metric Geometry***, Graduate Studies in Mathematics 33, American Mathematical Society (2001), is a standard source for metric-space distance, isometric embeddings, Hausdorff distance, and related set-distance constructions.
- Gerald Beer, ***Topologies on Closed and Closed Convex Sets***, Mathematics and Its Applications 268, Kluwer/Springer (1993), DOI `10.1007/978-94-015-8149-3`, develops distance functionals, Hausdorff metric topologies, and gap/excess functionals on closed sets. The one-sided quantity `\sup_{u\in M(R)}d(u,S)` used here is exactly in that classical excess language.
- Juha Heinonen, ***Lectures on Analysis on Metric Spaces***, Universitext, Springer (2001), DOI `10.1007/978-1-4613-0131-8`, provides standard metric/Lipschitz background for nonexpansive maps and distance estimates.
- David Blackwell, **“Equivalent Comparisons of Experiments,”** *The Annals of Mathematical Statistics* 24(2), 265–272 (1953), DOI `10.1214/aoms/1177729032`, and Lucien Le Cam, **“Sufficiency and Approximate Sufficiency,”** *The Annals of Mathematical Statistics* 35(4), 1419–1455 (1964), DOI `10.1214/aoms/1177700372`, provide the statistical comparison/equivalence setting instantiated by AF-052 and AF-053.

No novelty is claimed for point-to-set distance, Hausdorff excess, Lipschitz contraction, retractions, or the elementary inequalities used in the proof. A targeted literature check did not identify a standard named theorem with exactly the `\mathcal E_C(S)` packaging, but the result is deliberately classified as a classical mechanism rather than as new metric geometry: the safe envelope is an exact organization of standard distance-function facts chosen to answer the Arithmetic Fidelity question created by AF-052/AF-053.

## Boundary conditions and falsification checks

1. **`C` must be isometric for the exact maximal-envelope statement as written.** If `C` merely contracts or distorts distances, even the transported target `C(S)` may change the repair-radius function.
2. **Target enlargement is one-sided.** The theorem assumes `C(S)\subseteq R`. If valid source repairs are removed in the refined presentation, the radius can increase instead.
3. **The retraction criterion is sufficient, not necessary.** A target point can fail to descend into `\overline S` yet still be safe because its vertical distance in `Y` keeps it outside every forbidden ball around `C(X)`.
4. **The safe envelope is decision/target relative.** Changing `S` changes `r_S` and therefore changes `\mathcal E_C(S)` even when the ambient refinement is fixed.
5. **Closures are unavoidable.** Distance to a target depends only on its closure. Accordingly the exact descent condition uses `\overline S`, and `\mathcal E_C(S)=\mathcal E_C(\overline S)`.
6. **The descent defect can be infinite.** The quantitative inequality remains formally true but is useful only when the one-sided excess of `M(R)` beyond `S` is finite.
7. **Zero contraction does not prove semantic equivalence of targets.** Two target families may induce the same distance function on `C(X)` while differing elsewhere in `Y`; the theorem classifies repair-radius fidelity, not equality of the full target objects.

## Consequence for the line

AF-052 showed that a presentation-invariant metric can still produce a presentation-dependent distance to structure. AF-053 showed that unrestricted target freedom can erase the entire excess zero-error repair penalty under information-free stabilization. AF-054 extracts the reusable gate:

\[
\boxed{
\text{before interpreting a repair radius as intrinsic, audit whether every newly admissible target point lies in }\mathcal E_C(S).
}
\]

When a nonexpansive retraction is available, the practical sufficient test is simpler:

\[
\boxed{
M(R)\subseteq\overline S
\Longrightarrow
\text{exact repair-radius invariance}.
}
\]

If the refined targets do not descend, their one-sided excess after retraction gives a quantitative upper bound on how much the apparent structural margin can shrink solely because the presentation admitted new repair states.

For later arithmetic applications this is a direct anti-artifact test. Adding a marking, boundary coordinate, auxiliary spectral sector, regularization variable, or null degree of freedom is not automatically a faithful enrichment merely because the original object embeds isometrically or reversibly. The allowed **successful targets** in the enlarged representation must also descend to genuinely successful targets in the original mathematical category, or else any reduced distance-to-success may be measuring extra presentation capacity rather than preservation of the rational-prime discriminator.