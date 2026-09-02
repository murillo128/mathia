# AF-057 — Product-norm exponent sets a sharp collective safe-lift threshold

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `(X,d)` be a metric space, let `(N,\|\cdot\|)` be a normed linear space, let `S\subseteq X` be nonempty, and for `1\le p<\infty` equip

\[
Y_p=X\times N
\]

with the product metric

\[
D_p((x,u),(x',u'))
=
\left(d(x,x')^p+\|u-u'\|^p\right)^{1/p}.
\tag{1}
\]

Embed the source isometrically by

\[
C_p(x)=(x,0).
\tag{2}
\]

For `m\in X` define the extended **powered far-field defect**

\[
\Delta_{p,S}(m)
=
\sup_{x\in X}
\left(
 d(x,S)^p-d(x,m)^p
\right)
\in[0,+\infty].
\tag{3}
\]

Then:

1. **Product safe lifts are classified exactly by the powered far-field defect.** For every `(m,v)\in Y_p`, AF-054's safe-envelope condition is
   \[
   \boxed{
   (m,v)\in\mathcal E_{C_p}(S)
   \iff
   \|v\|^p\ge \Delta_{p,S}(m).
   }
   \tag{4}
   \]
   In particular a finite vertical safe lift above `m` exists exactly when `\Delta_{p,S}(m)<\infty` and the vertical factor contains a vector of sufficiently large norm.

2. **For the `\ell^1` product, the threshold collapses to the ordinary distance function for every metric source.** One has
   \[
   \boxed{
   \Delta_{1,S}(m)=d(m,S),
   }
   \tag{5}
   \]
   hence
   \[
   \boxed{
   \mathcal E_{C_1}(S)
   =
   \{(m,v):\|v\|\ge d(m,S)\}.
   }
   \tag{6}
   \]
   Thus `\ell^1` refinement admits a finite safe vertical lift over **every** base point, even far outside any convex hull when the source happens to be linear.

3. **A two-point Euclidean target has a sharp critical exponent at `p=2`.** Let
   \[
   X=\mathbb R^2,
   \qquad
   S_a=\{(-a,0),(a,0)\},
   \qquad a>0,
   \tag{7}
   \]
   with the Euclidean metric, take `N=\mathbb R`, and consider the midpoint `m=0`. Then
   \[
   \boxed{
   \Delta_{p,S_a}(0)=a^p
   \qquad(1\le p\le2),
   }
   \tag{8}
   \]
   whereas
   \[
   \boxed{
   \Delta_{p,S_a}(0)=+\infty
   \qquad(p>2).
   }
   \tag{9}
   \]
   Consequently
   \[
   \boxed{
   (0,h)\in\mathcal E_{C_p}(S_a)
   \iff |h|\ge a
   \qquad(1\le p\le2),
   }
   \tag{10}
   \]
   while for every `p>2` **no finite vertical coordinate is safe above the midpoint**.

4. **The same impossibility holds for the `\ell^\infty` product metric.** With
   \[
   D_\infty((x,u),(x',u'))
   =\max\{d(x,x'),\|u-u'\|\},
   \tag{11}
   \]
   the midpoint of the same two-point Euclidean target has no finite safe vertical lift.

5. **Safe-lift existence is therefore not determined by the underlying finite-dimensional linear topology or by norm equivalence.** On the common vector space `\mathbb R^3`, the norms
   \[
   \|(x,h)\|_{(p)}
   =
   \left(\|x\|_2^p+|h|^p\right)^{1/p},
   \qquad 1\le p<\infty,
   \tag{12}
   \]
   together with the corresponding max norm are all equivalent and induce the same finite-dimensional topology. Nevertheless the exact same embedded source `\mathbb R^2\times\{0\}` and the same two-point target have a finite midpoint safe lift for `p\le2` and none for `p>2`.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{safe-lift existence can be controlled by global quantitative metric geometry, not by topology or linear presentation alone.}
}
\tag{13}
\]

In particular, a proposed "minimal lift" or repair radius is not an intrinsic object until the admissible metric category has been fixed strongly enough. Equivalent norms are not harmless reparameterizations for this question.

## Derivation

### Exact product threshold

By AF-054, `(m,v)` is safe precisely when

\[
D_p(C_p(x),(m,v))
\ge d(x,S)
\qquad\forall x\in X.
\tag{14}
\]

Using (1)--(2) and raising both sides to the `p`th power gives

\[
d(x,m)^p+\|v\|^p
\ge d(x,S)^p
\qquad\forall x\in X.
\tag{15}
\]

Equivalently,

\[
\|v\|^p
\ge
\sup_{x\in X}
\left(d(x,S)^p-d(x,m)^p\right),
\tag{16}
\]

which is exactly (4). Evaluating the expression at `x=m` shows

\[
\Delta_{p,S}(m)\ge d(m,S)^p\ge0,
\tag{17}
\]

so no positive-part convention is required in (3).

This formula separates a local-looking vertical repair from a genuinely global condition: the required height is controlled by the worst comparison point anywhere in the source, and the supremum may be infinite even when `S` is finite and the embedding is linear and isometric.

### The universal `p=1` formula

The distance-to-set map is `1`-Lipschitz. For every `x,m\in X`,

\[
d(x,S)
\le d(x,m)+d(m,S),
\tag{18}
\]

so

\[
d(x,S)-d(x,m)
\le d(m,S).
\tag{19}
\]

Taking the supremum gives

\[
\Delta_{1,S}(m)\le d(m,S).
\tag{20}
\]

At `x=m`, equality holds:

\[
d(m,S)-d(m,m)=d(m,S).
\tag{21}
\]

Thus (5) follows. Substitution into (4) gives (6).

The result is worth separating from Hilbert geometry. In AF-056, quadratic orthogonal refinement forced the horizontal component of any safe point into `\operatorname{conv}(S)`. Under the `\ell^1` product, no analogous convex-hull restriction exists: arbitrary `m` is repaired exactly by paying its ordinary distance to `S` in the new coordinate.

### The two-point threshold for `1\le p\le2`

Let `x=(u,w)\in\mathbb R^2` and write

\[
r=\|x\|_2.
\tag{22}
\]

For the symmetric target `S_a`,

\[
d(x,S_a)^2
=r^2+a^2-2a|u|
\le r^2+a^2.
\tag{23}
\]

When `1\le p\le2`, the exponent `q=p/2` lies in `(0,1]`, so subadditivity of `t\mapsto t^q` on `\mathbb R_+` gives

\[
(r^2+a^2)^{p/2}
\le r^p+a^p.
\tag{24}
\]

Combining (23)--(24),

\[
d(x,S_a)^p-r^p
\le a^p.
\tag{25}
\]

At `x=0`,

\[
d(0,S_a)^p-0=a^p,
\tag{26}
\]

so the supremum is exactly `a^p`, proving (8). Equation (10) follows immediately from (4).

For `p=2`, this agrees with AF-056's Delaunay-radius description: the midpoint of the chord between the two sites lies one radius `a` below the safe boundary in the orthogonal direction.

### Superquadratic exponents fail at infinity

Now let `p>2` and inspect only the perpendicular ray

\[
x_t=(0,t),
\qquad t>0.
\tag{27}
\]

Then

\[
d(x_t,S_a)=\sqrt{t^2+a^2},
\qquad
\|x_t\|_2=t,
\tag{28}
\]

so the defect along this ray is

\[
\left(t^2+a^2\right)^{p/2}-t^p.
\tag{29}
\]

By the mean-value theorem applied to `s\mapsto s^{p/2}`, for some `\xi_t\in(t^2,t^2+a^2)`,

\[
\left(t^2+a^2\right)^{p/2}-t^p
=
\frac p2 a^2\xi_t^{p/2-1}.
\tag{30}
\]

Since `p/2-1>0`, the right-hand side tends to `+\infty` as `t\to\infty`. Hence `\Delta_{p,S_a}(0)=+\infty`, proving (9).

This failure is invisible on every fixed compact subset of the source. It is a pure far-field obstruction: increasingly remote comparison points accumulate an unbounded powered-distance advantage for the target over the midpoint.

### The max-product endpoint

For `D_\infty`, suppose a finite vertical height `h` were safe above the midpoint. Choose `t>|h|`. Then for `x_t=(0,t)`,

\[
D_\infty(C_\infty(x_t),(0,h))
=
\max\{t,|h|\}=t,
\tag{31}
\]

while

\[
d(x_t,S_a)=\sqrt{t^2+a^2}>t.
\tag{32}
\]

Thus the safe inequality fails, proving the `p=\infty` claim.

## Exact controls

### Same target, same embedding, opposite existence answer

Fix `a=1`. In the `p=2` product, the point

\[
y_2=(0,0,1)
\tag{33}
\]

is safe and lies exactly on the boundary. Indeed for every `(u,w)`,

\[
\|(u,w,0)-y_2\|_{(2)}^2
=u^2+w^2+1
\ge
u^2+w^2+1-2|u|
=d((u,w),S_1)^2.
\tag{34}
\]

In the `p=4` product, no point `(0,0,h)` with finite `h` is safe, because along `(0,t)` the required fourth-power correction is

\[
(t^2+1)^2-t^4
=2t^2+1
\to\infty.
\tag{35}
\]

Thus the existence change is exact, not an artifact of a limiting estimate.

### `\ell^1` permits safe lifts outside the Euclidean convex hull

Still with `S_1=\{(-1,0),(1,0)\}`, choose `m=(3,0)`. Then

\[
d(m,S_1)=2.
\tag{36}
\]

Formula (6) says

\[
((3,0),2)\in\mathcal E_{C_1}(S_1).
\tag{37}
\]

But `m\notin\operatorname{conv}(S_1)`. By AF-056, no finite orthogonal height above this same horizontal point belongs to the Hilbert (`p=2`) safe envelope. Therefore the norm exponent changes not merely the numerical repair cost but the projection of the entire safe region onto the source.

## Prior art and novelty assessment

The surrounding coapproximation and norm-geometry mechanisms are classical, and this finding does not claim a new theorem of Banach-space approximation theory.

- T. W. Narang and Sahil Gupta, **“Proximinality and co-proximinality in metric linear spaces,”** *Annales Universitatis Mariae Curie-Skłodowska, Sectio A* 69(1), 83--90 (2015), DOI `10.17951/a.2015.69.1.83`. Role: direct evidence that best coapproximation is studied beyond a fixed normed setting in metric linear spaces; existence and uniqueness depend on the declared metric geometry.
- Maciej Ciesielski and Grzegorz Lewicki, **“Some remarks on contractive and existence sets,”** *Monatshefte für Mathematik* 200, 1--21 (2023), DOI `10.1007/s00605-022-01777-z`. Role: modern coapproximation/existence-set framework tied to nonexpansive maps and norm-one projections; it also documents the established geometry-sensitive coapproximation literature in finite-dimensional `\ell^p` spaces.
- U. Westphal, **“Cosuns in `l_p(n)`, `1\le p<\infty`,”** *Journal of Approximation Theory* 54 (1988), 287--305. Role: direct classical prior art that coapproximation/cosun structure changes with `p` in finite-dimensional `\ell^p` geometry.
- Dmitri Burago, Yuri Burago, and Sergei Ivanov, ***A Course in Metric Geometry***, Graduate Studies in Mathematics 33, American Mathematical Society (2001). Role: standard metric-space background for distance-to-set functions and their `1`-Lipschitz property underlying the exact `p=1` formula.

A bounded search across coapproximation, simultaneous coapproximation, metric-linear-space, and `\ell^p` cosun literature found substantial prior art for norm-dependent coapproximation geometry. It did not establish that the exact product formula (4) or the symmetric two-point `p=2` threshold (8)--(9) is a named theorem, but that absence is not used as a novelty claim. The durable contribution here is an **Arithmetic Fidelity classification and falsification control**: the abstract safe-envelope construction can change qualitatively under equivalent finite-dimensional norms, and a compact/local audit can miss a global obstruction that appears only at infinity.

## Boundaries and failure modes

- Formula (4) is specific to the exact `\ell^p` product metric. It does not claim a classification for arbitrary Banach-space extensions or nonlinear refinements.
- The critical value `p=2` in (8)--(9) belongs to the declared Euclidean two-point source geometry. Other targets or source metrics can have different far-field decay and therefore different powered-defect behavior.
- Norm equivalence preserves topology and coarse finite-dimensional linear structure, but not metric inequalities with constant `1`. Therefore the phase transition is not a contradiction: it is evidence that safe-envelope fidelity is a quantitative metric notion.
- The `p>2` obstruction uses the unbounded source. On a compact source every continuous powered defect is bounded, so a sufficiently large vertical lift always exists in this product model.
- Existence of a safe lift does not make that lift natural, minimal in a categorical sense, or admissible for an arithmetic application. It only passes the AF-054 metric target-preservation gate.
- Nothing here distinguishes rational primes or yields an RH mechanism. This is an abstract structural result required by the line mandate before arithmetic specialization.

## Consequence for the Arithmetic Fidelity frontier

AF-054 isolated target transport as an independent source of repair-radius failure. AF-055 showed that singleton linear safe envelopes are classical best-coapproximation fibers, and AF-056 reduced compact Hilbert set-target envelopes to convex-roof/Delaunay geometry.

The first non-Hilbert audit now shows that there is **no presentation-free safe-envelope geometry at the level of topology or bare linear structure**. Even a one-parameter family of equivalent product norms can cross from finite to infinite repair cost while leaving the source embedding and target set unchanged.

The useful next question is therefore not to catalogue more norm examples. It is to identify which quantitative structures make a compression/lift category legitimate: isometry, nonexpansive equivalence, a fixed uniform structure with distortion bounds, an operator norm dictated by the construction, or another independently forced geometry. For eventual arithmetic use, any claimed minimal lift should be tested against exactly that declared category rather than against an unspecified notion of equivalent presentation.