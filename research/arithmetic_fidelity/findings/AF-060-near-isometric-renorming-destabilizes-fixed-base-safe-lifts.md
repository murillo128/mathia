# AF-060 — Near-isometric renorming destabilizes fixed-base safe lifts, not global safe envelopes

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

and define AF-054's safe envelope

\[
\mathcal E_C^D(S)
=
\{y\in Y:D(Cx,y)\ge r_S(x)\ \forall x\in X\}.
\tag{1}
\]

Then the following distinction is exact.

1. **Global safe-envelope nonemptiness is automatic and cannot be destroyed by any ambient renorming that keeps `C` isometric.** One always has
   \[
   \boxed{C(\overline S)\subseteq \mathcal E_C^D(S).}
   \tag{2}
   \]
   In particular
   \[
   \boxed{\mathcal E_C^D(S)\neq\varnothing.}
   \tag{3}
   \]
   Thus no change of the ambient metric can erase global safe-envelope existence while `S` remains nonempty and the same source embedding remains isometric.

2. **Pointwise safety has an exact multiplicative robustness modulus.** For `y\in Y` define
   \[
   \mu_D(y;C,S)
   =
   \inf_{\{x:r_S(x)>0\}}
   \frac{D(Cx,y)}{r_S(x)},
   \tag{4}
   \]
   with `\mu_D=+\infty` when `r_S\equiv0`. Then
   \[
   \boxed{
   y\in\mathcal E_C^D(S)
   \iff
   \mu_D(y;C,S)\ge1.
   }
   \tag{5}
   \]
   If `\widetilde D` is another metric on the same `Y`, the same `C` is also isometric for `\widetilde D`, and
   \[
   K^{-1}D(u,v)\le \widetilde D(u,v)\le K D(u,v)
   \qquad\forall u,v\in Y,
   \tag{6}
   \]
   then
   \[
   \boxed{
   K^{-1}\mu_D(y;C,S)
   \le
   \mu_{\widetilde D}(y;C,S)
   \le
   K\mu_D(y;C,S).
   }
   \tag{7}
   \]

3. **Fixed-base safe-lift existence can nevertheless be destroyed by arbitrarily small global multiplicative distortion.** Let
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
   \tag{8}
   \]
   For `q\ge2` equip `Y` with
   \[
   D_q((x,h),(x',h'))
   =
   \left(\|x-x'\|_2^q+|h-h'|^q\right)^{1/q}.
   \tag{9}
   \]
   The embedding `C` is exactly isometric for every `q`. For the vertical fiber over the midpoint
   \[
   F_0=\{(0,h):h\in\mathbb R\}\subset Y,
   \tag{10}
   \]
   AF-057 gives
   \[
   \boxed{
   \mathcal E_C^{D_2}(S_a)\cap F_0
   =\{(0,h):|h|\ge a\},
   }
   \tag{11}
   \]
   whereas for every `q>2`,
   \[
   \boxed{
   \mathcal E_C^{D_q}(S_a)\cap F_0
   =\varnothing.
   }
   \tag{12}
   \]

4. **The instability accumulates at the Hilbert norm.** Standard two-coordinate norm comparison gives, for every `q>2`,
   \[
   \boxed{
   D_q\le D_2\le K_qD_q,
   \qquad
   K_q=2^{\frac12-\frac1q}.
   }
   \tag{13}
   \]
   Since `K_q\downarrow1` as `q\downarrow2`, for every `\varepsilon>0` there is a `q>2` such that the identity on the common ambient vector space has distortion `<1+\varepsilon`, while the fixed-base existence statement changes from (11) to (12).

5. **The Hilbert midpoint lifts sit exactly on the zero-margin boundary.** For `|h|\ge a`, let `y_h=(0,h)\in F_0`. Then
   \[
   \boxed{
   \mu_{D_2}(y_h;C,S_a)=1.
   }
   \tag{14}
   \]
   Hence those safe points possess no strict multiplicative safety margin, even when `|h|>a` makes every fixed source-point inequality strict. The loss of margin occurs at infinity.

The reusable Arithmetic Fidelity conclusion is therefore

\[
\boxed{
\begin{array}{c}
\text{near-isometric ambient changes can destroy safe-lift existence}\
\text{inside a prescribed fiber, but cannot destroy global safe-envelope}\
\text{nonemptiness while the source embedding remains isometric.}
\end{array}
}
\tag{15}
\]

The admissible notion of "lift existence" must therefore specify whether the base point, fiber, projection, or another provenance constraint is part of the observable. Dropping that constraint changes the mathematical question: globally, transported target points are always safe.

## Derivation

### Global safe points are forced by the transported target

Take `s\in\overline S`. Since `C` is an isometry,

\[
D(Cx,Cs)=d(x,s)
\qquad\forall x\in X.
\tag{16}
\]

By the definition of distance to a set,

\[
d(x,s)\ge d(x,S)=r_S(x).
\tag{17}
\]

Therefore `Cs\in\mathcal E_C^D(S)`. This proves (2), hence (3). The argument uses no linear structure, convexity, completeness, or special form of `D`; it requires only nonempty `S` and an isometric source embedding.

This is the exact reason a fixed-base statement cannot be promoted to a global existence statement. The points `C(S)` remain available even when an entire off-image fiber loses all safe points.

### The safety modulus is exactly the membership threshold

When `r_S(x)=0`, the safe inequality is automatic. On the set where `r_S(x)>0`, the condition

\[
D(Cx,y)\ge r_S(x)
\]

is equivalent to

\[
\frac{D(Cx,y)}{r_S(x)}\ge1.
\]

Requiring this for every such `x` is exactly `\mu_D(y;C,S)\ge1`, which proves (5).

Under (6), each ratio satisfies

\[
K^{-1}\frac{D(Cx,y)}{r_S(x)}
\le
\frac{\widetilde D(Cx,y)}{r_S(x)}
\le
K\frac{D(Cx,y)}{r_S(x)}.
\]

Taking infima gives (7). Thus a point with `\mu_D(y)>1` has an explicit multiplicative buffer against sufficiently small metric distortion, whereas a point with `\mu_D(y)=1` is located exactly on the threshold and requires a more detailed perturbation analysis.

### Hilbert midpoint lifts have no uniform margin

Let

\[
x_t=(0,t)\in\mathbb R^2,
\qquad t>0.
\]

Then

\[
r_{S_a}(x_t)=\sqrt{t^2+a^2},
\tag{18}
\]

while for `y_h=(0,h)` in the midpoint fiber,

\[
D_2(Cx_t,y_h)=\sqrt{t^2+h^2}.
\tag{19}
\]

For `|h|\ge a`, AF-057 gives safety, so `\mu_{D_2}(y_h)\ge1`. But

\[
\frac{D_2(Cx_t,y_h)}{r_{S_a}(x_t)}
=
\sqrt{\frac{t^2+h^2}{t^2+a^2}}
\longrightarrow1
\qquad(t\to\infty).
\tag{20}
\]

Therefore the infimum is exactly `1`, proving (14). For `|h|>a`, the ratio is strictly larger than `1` for every finite point on this perpendicular ray; the missing uniform margin is genuinely a far-field effect.

### Arbitrarily close product norms cross the fixed-base boundary

For nonnegative `A,B` and `q>2`,

\[
(A^q+B^q)^{1/q}
\le
(A^2+B^2)^{1/2}
\le
2^{\frac12-\frac1q}(A^q+B^q)^{1/q}.
\tag{21}
\]

Substituting

\[
A=\|x-x'\|_2,
\qquad
B=|h-h'|
\]

proves (13). The same estimate shows that the identity linear map between these two normed realizations has multiplicative distortion at most `K_q`, tending to `1` as `q\downarrow2`.

For `q=2`, AF-057 computes the powered far-field defect above the midpoint as `a^2`, giving (11). For every `q>2`, along the same ray `x_t=(0,t)`,

\[
\operatorname{dist}(x_t,S_a)^q-\|x_t\|_2^q
=
(t^2+a^2)^{q/2}-t^q
\longrightarrow+\infty.
\tag{22}
\]

Hence no finite vertical coordinate can satisfy the safe inequalities, proving (12). Combining this with (13) yields the arbitrarily-near-isometric instability of the **fiber-constrained** existence statement.

## Exact controls

### The global envelope survives in both metrics

For every `q\ge2`, the source embedding remains isometric and therefore

\[
C(S_a)\subseteq\mathcal E_C^{D_q}(S_a).
\tag{23}
\]

So the global envelope is nonempty on both sides of the phase change. The only disappearing set in the example is its intersection with the chosen midpoint fiber `F_0`.

This is not a semantic qualification; it is a different quantifier:

\[
\exists y\in\mathcal E_C^D(S)
\]

is always true here, whereas

\[
\exists y\in\mathcal E_C^D(S)\cap F_0
\]

changes truth value under arbitrarily small distortion.

### The source geometry is preserved exactly

For every `q\ge2`,

\[
D_q(Cx,Cx')=\|x-x'\|_2.
\tag{24}
\]

The effect is not caused by approximate source preservation. It comes from the interaction between the distinguished vertical fiber and far-field horizontal geometry.

### Compact truncation hides the instability

For any fixed compact source truncation, the powered defect in (22) is bounded. A sufficiently large vertical height therefore passes every truncated audit for every finite `q`. The obstruction appears only when the full unbounded source is restored.

Thus finite numerical searches cannot certify the global fixed-base failure unless accompanied by an analytic far-field argument.

### Zero margin is a warning, not a universal converse theorem

Equation (7) shows that strict margin gives a sufficient robustness certificate against bounded multiplicative perturbations. The converse is not claimed: `\mu_D(y)=1` does not imply that every arbitrarily small perturbation destroys safety. The explicit `D_q` family is what proves instability in this example.

## Prior art and novelty assessment

The component mechanisms are classical and no novelty is claimed for norm comparison, Banach--Mazur stability language, metric coapproximation, or condition-number ideas.

- T. D. Narang and S. P. Singh, **“Best Coapproximation in Metric Linear Spaces,”** *Tamkang Journal of Mathematics* 30(4), 241–252 (1999), DOI `10.5556/j.tkjm.30.1999.4198`. Role: established metric-dependent coapproximation framework neighboring AF-054--AF-057.
- J. Villada Bedoya, **“The almost fixed point property is not invariant under isometric renormings,”** *Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A. Matemáticas* 115, article 80 (2021), DOI `10.1007/s13398-021-01016-4`. Role: direct precedent that collections of geometrically defined admissible sets can fail stability under renormings, including perturbations with Banach--Mazur distance arbitrarily close to `1` in the preceding stability theorem discussed there. It is neighboring stability theory, not the present safe-envelope theorem.
- James W. Demmel, **“On Condition Numbers and the Distance to the Nearest Ill-posed Problem,”** *Numerische Mathematik* 51 (1987), 251–289, DOI `10.1007/BF01400115`. Role: classical precedent for replacing a Boolean well-posed/ill-posed label by a quantitative margin to failure.

AF-054 already proves the global inclusion (2), and AF-057 proves the exact product threshold used in (11)--(12). The present finding does not rebrand those statements as new. Its durable role is corrective and structural: it separates the always-nonempty global safe envelope from a genuinely unstable **fiber-constrained** existence observable, and it identifies the pointwise multiplicative modulus that explains why the Hilbert midpoint lifts are vulnerable to the explicit near-isometric renorming family.

A targeted literature check confirms that near-Banach--Mazur renorming instability is an established phenomenon in neighboring Banach-space geometry. No claim is made that (15) defines a new general theory of renorming stability.

## Boundaries and failure modes

- The global nonemptiness theorem assumes `S` is nonempty and `C` is isometric for the metric being considered. If either condition is removed, (2) need not apply.
- The instability theorem is about the distinguished midpoint fiber `F_0`. It does not assert loss of all safe points, loss of the global safe envelope, or instability of every possible fiber.
- The explicit perturbation family is the product `\ell^q` family on `\mathbb R^2\times\mathbb R`; no classification of arbitrary near-isometric renormings is claimed.
- The multiplicative safety modulus is pointwise. It does not by itself encode naturality, minimality of a lift, or admissibility of the chosen fiber in an arithmetic application.
- The example is noncompact and the mechanism is far-field. Compact sources require a separate analysis.
- Nothing here distinguishes rational primes or implies RH. The result is an abstract fidelity control about how a provenance constraint changes the meaning of existence under compression/refinement.

## Consequence for the Arithmetic Fidelity frontier

AF-054 already guarantees that transported target points make every global safe envelope nonempty. AF-057 and AF-059 show that product-lift geometry can nevertheless have sharp exponent-dependent constraints on which **base points** admit finite vertical repairs.

The corrected frontier is therefore not to ask whether a refinement admits any safe point. That question is trivial under an isometric source embedding and nonempty target. The nontrivial observable must include additional provenance: a prescribed base point, fiber, projection, boundary component, marking, or other relational constraint whose survival can actually fail.

This strengthens the line's general warning about compression: **existence after forgetting provenance can be vacuous even when existence with provenance is highly rigid and representation-sensitive.** Future minimal-lift claims should state the retained provenance explicitly before treating existence or nonexistence as an intrinsic discriminator.