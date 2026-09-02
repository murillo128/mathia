# AF-058 — Near-isometric renorming can destroy safe-lift existence

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `(X,d)` be a metric space, let `S\subseteq X` be nonempty, and let

\[
C:(X,d)\longrightarrow (Y,D)
\]

be an isometric embedding. Write

\[
r_S(x)=d(x,S)
\]

and define the **multiplicative safety modulus** of a refined point `y\in Y` by

\[
\mu_D(y;C,S)
=
\inf_{\{x:r_S(x)>0\}}
\frac{D(Cx,y)}{r_S(x)},
\tag{1}
\]

with the convention `\mu_D=+\infty` when `r_S\equiv0`.

Then:

1. **The modulus is the exact pointwise safe-envelope criterion.** For the AF-054 safe envelope
   \[
   \mathcal E_C^D(S)
   =
   \{y\in Y:D(Cx,y)\ge r_S(x)\ \forall x\in X\},
   \]
   one has
   \[
   \boxed{
   y\in\mathcal E_C^D(S)
   \iff
   \mu_D(y;C,S)\ge1.
   }
   \tag{2}
   \]

2. **Global bi-Lipschitz distortion transports the safety modulus multiplicatively.** Suppose `\widetilde D` is another metric on the same set `Y`, the same map `C` is also an isometric embedding into `(Y,\widetilde D)`, and for some `K\ge1`,
   \[
   K^{-1}D(u,v)
   \le
   \widetilde D(u,v)
   \le
   K D(u,v)
   \qquad\forall u,v\in Y.
   \tag{3}
   \]
   Then
   \[
   \boxed{
   K^{-1}\mu_D(y;C,S)
   \le
   \mu_{\widetilde D}(y;C,S)
   \le
   K\mu_D(y;C,S).
   }
   \tag{4}
   \]
   Consequently `\mu_D(y)\ge K` certifies that `y` remains safe under every such `K`-distortion representation, while `\mu_D(y)<K^{-1}` certifies that it remains unsafe. Exact safety without a strict multiplicative margin need not be representation-stable.

3. **AF-057's Hilbert safe lifts have zero multiplicative robustness margin even when the finite-point inequalities are strict.** Let
   \[
   X=\mathbb R^2,
   \qquad
   S_a=\{(-a,0),(a,0)\},
   \qquad a>0,
   \]
   and put
   \[
   Y=\mathbb R^2\times\mathbb R,
   \qquad
   C(x)=(x,0).
   \]
   Equip `Y` first with
   \[
   D_2((x,h),(x',h'))
   =
   \left(\|x-x'\|_2^2+|h-h'|^2\right)^{1/2}.
   \tag{5}
   \]
   For every finite `h` with `|h|\ge a`, AF-057 gives `(0,h)\in\mathcal E_C^{D_2}(S_a)`, but in fact
   \[
   \boxed{
   \mu_{D_2}((0,h);C,S_a)=1.
   }
   \tag{6}
   \]
   Thus every finite Hilbert safe lift above the midpoint lies exactly at zero multiplicative safety margin. When `|h|>a`, each fixed source point satisfies a strict safety inequality, yet the uniform margin still vanishes at infinity.

4. **Arbitrarily small global norm distortion can remove every finite safe lift above the same midpoint.** For `q>2`, equip the same vector space `Y` with
   \[
   D_q((x,h),(x',h'))
   =
   \left(\|x-x'\|_2^q+|h-h'|^q\right)^{1/q}.
   \tag{7}
   \]
   The source embedding remains exactly isometric for every `q`. Standard two-coordinate norm comparison gives
   \[
   \boxed{
   D_q\le D_2\le K_q D_q,
   \qquad
   K_q=2^{\frac12-\frac1q}.
   }
   \tag{8}
   \]
   Hence
   \[
   K_q\downarrow1
   \qquad(q\downarrow2),
   \tag{9}
   \]
   and the identity map between the two ambient normed spaces has distortion at most `K_q`. In particular their multiplicative Banach--Mazur distance is at most `K_q`.

   Nevertheless AF-057 proves that for every `q>2`,
   \[
   \boxed{
   \mathcal E_C^{D_q}(S_a)
   \cap
   \bigl(\{0\}\times\mathbb R\bigr)
   =\varnothing.
   }
   \tag{10}
   \]
   No finite vertical height above the midpoint is safe.

5. **Therefore finite safe-lift existence is not stable under arbitrarily near-isometric renorming.** For every `\varepsilon>0`, choose `q>2` sufficiently close to `2` that
   \[
   K_q<1+\varepsilon.
   \]
   The source metric, target `S_a`, embedding `C`, and underlying vector space are unchanged, and the two ambient norms are globally `(1+\varepsilon)`-bi-Lipschitz close under the identity. Yet
   \[
   \boxed{
   \exists h\in\mathbb R:\ (0,h)\in\mathcal E_C^{D_2}(S_a),
   \qquad
   \nexists h\in\mathbb R:\ (0,h)\in\mathcal E_C^{D_q}(S_a).
   }
   \tag{11}
   \]

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{metric equivalence, even with distortion arbitrarily close to }1,
\text{ does not preserve exact safe-lift existence without a uniform safety margin.}
}
\tag{12}
\]

This sharpens AF-057. That finding showed that equivalent norms can disagree on safe-lift existence; the present result shows that the disagreement occurs **arbitrarily close to the Hilbert representation in global multiplicative distortion**. A topology or an unspecified equivalence class of norms is therefore too weak a declaration of the admissible representation category for exact repair questions.

## Derivation

### Exact safety is a ratio condition

If `r_S(x)=0`, the safe inequality

\[
D(Cx,y)\ge r_S(x)
\]

is automatic. Therefore only points with positive target distance matter. On that set, requiring the inequality for every `x` is exactly the condition

\[
\frac{D(Cx,y)}{r_S(x)}\ge1
\qquad\forall x:r_S(x)>0.
\]

Taking the infimum proves (2). The convention in the degenerate case `r_S\equiv0` is consistent: then every `y\in Y` is safe because all right-hand sides vanish.

### Distortion covariance

From (3), for each `x` with `r_S(x)>0`,

\[
K^{-1}
\frac{D(Cx,y)}{r_S(x)}
\le
\frac{\widetilde D(Cx,y)}{r_S(x)}
\le
K
\frac{D(Cx,y)}{r_S(x)}.
\]

Taking infima gives (4). Thus the relevant robustness quantity is not merely Boolean membership in a safe envelope but the distance ratio separating that membership from the threshold `1`.

This is the representation-side analogue of the distance-to-failure moduli already encountered in AF-044 and AF-045 for perturbations of compression maps. The perturbation variable is different here: the source, target, and embedding are held fixed while the **ambient metric itself** changes.

### The Hilbert lift has no uniform multiplicative slack

Take `x_t=(0,t)\in\mathbb R^2`. Then

\[
r_{S_a}(x_t)
=
\sqrt{t^2+a^2},
\tag{13}
\]

while for `y_h=(0,h)\in Y`,

\[
D_2(Cx_t,y_h)
=
\sqrt{t^2+h^2}.
\tag{14}
\]

If `|h|\ge a`, AF-057 proves `y_h` is safe, hence `\mu_{D_2}(y_h)\ge1`. But along the perpendicular ray,

\[
\frac{D_2(Cx_t,y_h)}{r_{S_a}(x_t)}
=
\sqrt{\frac{t^2+h^2}{t^2+a^2}}
\longrightarrow1
\qquad(t\to\infty).
\tag{15}
\]

Therefore the infimum cannot exceed `1`, proving (6).

For `|h|>a`, the ratio in (15) is strictly larger than `1` for every finite `t`. More generally, the exact AF-057 inequality is strict at every fixed source point. The loss of margin is therefore a **far-field phenomenon**, not a finite collision.

### Arbitrarily close product norms cross the safe-lift boundary

For nonnegative scalars `A,B` and `q>2`, the standard finite-dimensional `\ell^q`/`\ell^2` comparison is

\[
(A^q+B^q)^{1/q}
\le
(A^2+B^2)^{1/2}
\le
2^{\frac12-\frac1q}(A^q+B^q)^{1/q}.
\tag{16}
\]

Apply this with

\[
A=\|x-x'\|_2,
\qquad
B=|h-h'|.
\]

This proves (8). The same inequality shows that the identity linear isomorphism has norm-product distortion at most `K_q`, which tends to `1` as `q\downarrow2`.

But AF-057 computes the powered far-field defect for the midpoint. For every `q>2`,

\[
\sup_{x\in X}
\left(
 d(x,S_a)^q-d(x,0)^q
\right)
=+\infty.
\tag{17}
\]

Hence no finite vertical coordinate can satisfy the safe-envelope inequalities. Combining (8)--(17) proves (11).

## Exact controls

### The threshold is not caused by source distortion

For every `q\ge1`,

\[
D_q(Cx,Cx')
=
\|x-x'\|_2.
\]

Thus the source metric is not approximately preserved; it is **exactly** preserved throughout the perturbation family. The instability comes from how the refined direction combines with large horizontal distances.

### The phenomenon survives arbitrarily small prescribed distortion

Given any `\varepsilon>0`, continuity of

\[
q\mapsto2^{\frac12-\frac1q}
\]

at `q=2` gives a whole interval `(2,2+\delta)` in which the identity distortion is below `1+\varepsilon`. Every member of that interval still has the AF-057 `q>2` far-field obstruction. This is not a comparison between one especially non-Euclidean norm and the Hilbert norm; the failure accumulates at the Hilbert norm itself.

### Compact truncation hides the obstruction

For any fixed radius `R`, the source set

\[
\{x\in\mathbb R^2:\|x\|_2\le R\}
\]

is compact. The powered defect in AF-057 is continuous there, so every `q>2` admits a finite vertical height that is safe on that truncation. The impossibility appears only after the full unbounded source is restored.

Therefore finite experiments on growing compact regions can repeatedly suggest a stable lift while the exact global lift does not exist. Any computational or local audit of this phenomenon needs an explicit far-field bound rather than only larger cutoffs.

## Prior art and novelty assessment

The surrounding concepts are classical, and no novelty is claimed for Banach--Mazur distance, equivalent-norm comparison, best coapproximation, or the general idea that robustness should be measured by distance from an ill-posed boundary.

- Nicole Tomczak-Jaegermann, ***Banach-Mazur Distances and Finite-Dimensional Operator Ideals***, Pitman Monographs and Surveys in Pure and Applied Mathematics 38, Longman Scientific & Technical / Wiley (1989). Role: standard finite-dimensional Banach--Mazur and norm-distortion framework used to interpret (8)--(9).
- T. D. Narang and S. P. Singh, **“Best Coapproximation in Metric Linear Spaces,”** *Tamkang Journal of Mathematics* 30(4), 241–252 (1999), DOI `10.5556/j.tkjm.30.1999.4198`. Role: direct prior art that coapproximation is intrinsically metric-dependent beyond the normed/Hilbert setting; AF-055 already identifies singleton safe envelopes with classical coapproximation fibers.
- J. Villada Bedoya, **“The almost fixed point property is not invariant under isometric renormings,”** *Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A. Matemáticas* 115, article 80 (2021), DOI `10.1007/s13398-021-01016-4`. Role: strong neighboring renorming-stability precedent. Its introduction records Banach--Mazur stability questions and a theorem giving, for a different fixed-point property, equivalent norms at distance `<1+\delta` whose admissible-set collections differ. Thus arbitrarily-close-renorming instability is not itself a new paradigm.
- James W. Demmel, **“On Condition Numbers and the Distance to the Nearest Ill-posed Problem,”** *Numerische Mathematik* 51 (1987), 251–290, DOI `10.1007/BF01400115`. Role: classical conditioning precedent for measuring robustness through quantitative distance to failure rather than a Boolean well-posed/ill-posed label.

A targeted search across coapproximation, coproximinality, renorming stability, Banach--Mazur stability, and distance-to-ill-posedness literature found mature theories for each surrounding mechanism. It did not establish the exact safe-envelope ratio (1)--(4) or the AF-057 specialization (6)--(11) as a named theorem, but that absence is **not** used as a novelty claim. The durable contribution is an Arithmetic Fidelity classification: it identifies the precise missing hypothesis in the proposed “equivalent presentation” idea and gives an exact counterexample showing that even globally near-isometric presentation changes can cross the repair-existence boundary.

## Boundaries and failure modes

- The covariance bound (4) is elementary and does not claim a new theorem in metric geometry or perturbation theory.
- `\mu_D(y)>1` is a strict pointwise robustness margin for multiplicative metric perturbations; it is not asserted to be necessary for stability under every narrower transformation class.
- Banach--Mazur distance alone forgets distinguished embeddings and target subsets. The rigorous instability statement here uses the stronger fact that the **identity** on the same ambient vector space has distortion tending to `1` while `C` and `S_a` are held fixed. The Banach--Mazur bound is a corollary, not the definition of the structured perturbation.
- The example is noncompact. Compactness can turn pointwise strict safety into a positive uniform additive margin, so the far-field mechanism cannot be transferred unchanged to compact sources.
- The result concerns exact safe-lift existence above a fixed base point. It does not say that all approximate repair notions, all coapproximation properties, or every target geometry are unstable near Hilbert space.
- Nothing here singles out the rational primes or yields an RH mechanism. It is a structural obstruction required before calling a metric/lift construction “intrinsic” under a declared presentation equivalence.

## Consequence for the Arithmetic Fidelity frontier

AF-054 showed that target transport must be specified in addition to representation geometry. AF-055 and AF-056 placed large linear/Hilbert parts of that geometry inside classical coapproximation and convex-roof theory. AF-057 then showed qualitative dependence on the product norm.

The present result closes one tempting escape: replacing “same metric” by “equivalent” or even “arbitrarily close bi-Lipschitz” metrics does **not** make exact safe-lift existence intrinsic on an unbounded source. The correct next gate is quantitative.

A future compression/lift category should therefore declare both:

\[
\text{admissible representation distortion}
\quad\text{and}\quad
\text{a safety/conditioning modulus that stays uniformly away from failure}.
\]

For an arithmetic application, a claimed relational or transverse lift should not merely exist in one convenient metric presentation. It should either be forced by an exact canonical geometry, or carry a positive robustness certificate against the full independently justified class of representation changes. Otherwise an arbitrarily small admissible change may erase the very repair the construction was meant to preserve.
