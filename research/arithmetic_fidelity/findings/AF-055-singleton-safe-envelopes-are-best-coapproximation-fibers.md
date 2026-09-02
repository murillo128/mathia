# AF-055 — Singleton safe envelopes are exactly best-coapproximation fibers

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-MECHANISM`, `PRIOR-ART-REDIRECT`, `STRUCTURAL-CLASSIFICATION`

## Claim

Let `Y` be a real or complex normed linear space, let `M\subseteq Y` be a linear subspace, and let

\[
C:M\hookrightarrow Y
\]

be the inclusion. For `m_0\in M`, AF-054's safe envelope of the singleton target `\{m_0\}` is

\[
\mathcal E_C(\{m_0\})
=
\left\{
y\in Y:
\|x-y\|\ge \|x-m_0\|
\text{ for every }x\in M
\right\}.
\tag{1}
\]

Classical best-coapproximation theory uses the set-valued map

\[
R_M(y)
=
\left\{
m_0\in M:
\|m_0-x\|\le \|y-x\|
\text{ for every }x\in M
\right\}.
\tag{2}
\]

Then:

1. **The singleton safe-envelope relation is exactly the classical best-coapproximation relation.**
   \[
   \boxed{
   y\in\mathcal E_C(\{m_0\})
   \iff
   m_0\in R_M(y).
   }
   \tag{3}
   \]
   Hence the sets `\mathcal E_C(\{m_0\})` are precisely the inverse fibers of the set-valued best-coapproximation relation.

2. **Linearity makes all singleton envelopes translates of one kernel envelope.**
   \[
   \boxed{
   \mathcal E_C(\{m_0\})
   =m_0+\mathcal E_C(\{0\}).
   }
   \tag{4}
   \]
   Therefore the existence and uniqueness theory of singleton safe repairs is exactly the classical coproximinal/co-Chebyshev theory:
   \[
   \boxed{
   M\text{ coproximinal in }Y
   \iff
   Y=\bigcup_{m\in M}\mathcal E_C(\{m\}),
   }
   \tag{5}
   \]
   and
   \[
   \boxed{
   M\text{ co-Chebyshev in }Y
   \iff
   \{\mathcal E_C(\{m\}):m\in M\}
   \text{ partitions }Y.
   }
   \tag{6}
   \]

3. **In a Hilbert space, singleton safe envelopes reduce exactly to orthogonal fibers.** If `Y` is a Hilbert space, then
   \[
   \boxed{
   \mathcal E_C(\{0\})=M^\perp,
   \qquad
   \mathcal E_C(\{m_0\})=m_0+M^\perp.
   }
   \tag{7}
   \]
   If `M` is closed, these affine orthogonal fibers form a partition of `Y`, so every point has the unique coapproximant given by the orthogonal projection onto `M`.

4. **AF-054's `\ell^1` cone is therefore not a new singleton-envelope phenomenon.** For
   \[
   Y=(\mathbb R^2,\|\cdot\|_1),
   \qquad
   M=\mathbb R\times\{0\},
   \tag{8}
   \]
   one has
   \[
   \boxed{
   \mathcal E_C(\{(a,0)\})
   =
   \{(u,v):|v|\ge |u-a|\}.
   }
   \tag{9}
   \]
   Thus the cone computed in AF-054 is the inverse fiber of the classical best-coapproximation relation for the horizontal subspace. The subspace is coproximinal but not co-Chebyshev: for `(u,v)` with `v\ne0`, the complete coapproximation set is
   \[
   \boxed{
   R_M((u,v))
   =
   \{(a,0):|u-a|\le |v|\}.
   }
   \tag{10}
   \]

5. **The general set-target safe envelope is not exhausted by singleton coapproximation fibers.** For every nonempty `S\subseteq M`,
   \[
   \boxed{
   \bigcup_{s\in S}\mathcal E_C(\{s\})
   \subseteq
   \mathcal E_C(S),
   }
   \tag{11}
   \]
   but the inclusion can be strict even in the Euclidean plane. Take
   \[
   Y=\mathbb R^2,
   \qquad
   M=\mathbb R\times\{0\},
   \qquad
   S=\{(-1,0),(1,0)\}.
   \tag{12}
   \]
   Then
   \[
   \boxed{
   (0,1)\in\mathcal E_C(S)
   \setminus
   \left(
   \mathcal E_C(\{(-1,0)\})
   \cup
   \mathcal E_C(\{(1,0)\})
   \right).
   }
   \tag{13}
   \]

The reusable Arithmetic Fidelity conclusion is therefore a **prior-art boundary**:

\[
\boxed{
\text{singleton safe envelopes for linear inclusions}
=
\text{classical best coapproximation};
}
\tag{14}
\]

while

\[
\boxed{
\text{distance preservation to a non-singleton structural target}
\text{ can have genuinely collective safe points.}
}
\tag{15}
\]

Consequently future Arithmetic Fidelity work must search best-coapproximation, coproximinality, co-Chebyshev, and simultaneous-coapproximation literature before treating a linear target-envelope result as new. The residual AF-054 question is not the singleton linear case; it lies in genuinely set-valued targets, nonlinear/refined metric representations, target transport under equivalence, or category-specific admissibility constraints not already captured by coapproximation theory.

## Derivation

### Exact identification with best coapproximation

The standard coapproximation condition for `m_0\in M` to coapproximate `y\in Y` is

\[
\|m_0-x\|\le\|y-x\|
\qquad\forall x\in M.
\tag{16}
\]

Because norms are symmetric,

\[
\|m_0-x\|=\|x-m_0\|,
\qquad
\|y-x\|=\|x-y\|.
\tag{17}
\]

Thus (16) is literally the defining inequality (1) for

\[
y\in\mathcal E_C(\{m_0\}).
\]

No additional argument or regularity hypothesis is needed. This proves (3).

This exact dictionary materially narrows AF-054. Its singleton specialization for normed-linear inclusions is not merely analogous to a known approximation concept; it is the same relation with the two variables read in the opposite direction.

### Translation law

Let `m_0\in M` and write

\[
y=m_0+z,
\qquad
x=m_0+h,
\qquad h\in M.
\tag{18}
\]

Then

\[
\|x-y\|=\|h-z\|,
\qquad
\|x-m_0\|=\|h\|.
\tag{19}
\]

Therefore

\[
y\in\mathcal E_C(\{m_0\})
\iff
z\in\mathcal E_C(\{0\}),
\tag{20}
\]

which proves (4).

The standard existence/uniqueness terminology now reads directly in safe-envelope language. `M` is coproximinal precisely when every `y\in Y` admits at least one `m_0\in M` with `m_0\in R_M(y)`, which by (3) is precisely the covering property (5). It is co-Chebyshev precisely when every `R_M(y)` is a singleton, which is exactly the statement that every `y` lies in one and only one translated singleton envelope, proving (6).

### Hilbert specialization

Assume `Y` is a Hilbert space. If `y\in M^\perp`, then for every `x\in M`, Pythagoras gives

\[
\|x-y\|^2
=
\|x\|^2+\|y\|^2
\ge
\|x\|^2.
\tag{21}
\]

Hence `y\in\mathcal E_C(\{0\})`.

Conversely suppose

\[
\|x-y\|\ge\|x\|
\qquad\forall x\in M.
\tag{22}
\]

For any `m\in M` and scalar `t`, applying (22) to `x=tm` yields

\[
\|tm-y\|^2-\|tm\|^2
=
\|y\|^2-2\operatorname{Re}\langle tm,y\rangle
\ge0.
\tag{23}
\]

If `\langle m,y\rangle\ne0`, choose the phase of `t` so that

\[
\operatorname{Re}\langle tm,y\rangle>0
\]

and then increase `|t|`. The right-hand side of (23) eventually becomes negative, a contradiction. Thus

\[
\langle m,y\rangle=0
\qquad\forall m\in M,
\tag{24}
\]

so `y\in M^\perp`. This proves

\[
\mathcal E_C(\{0\})=M^\perp,
\]

and (4) gives the affine formula in (7).

When `M` is closed, the orthogonal decomposition

\[
Y=M\oplus M^\perp
\tag{25}
\]

makes the fibers `m+M^\perp` a partition, recovering the classical unique Hilbert-space coproximity map.

## Exact controls

### AF-054's `\ell^1` cone is a coapproximation fiber

Let `Y`, `M` be as in (8), let `y=(u,v)`, and ask when `0\in R_M(y)`. The condition is

\[
|t|
\le
|t-u|+|v|
\qquad\forall t\in\mathbb R.
\tag{26}
\]

The triangle inequality gives

\[
|t|
\le
|t-u|+|u|.
\tag{27}
\]

Hence `|v|\ge|u|` is sufficient. Taking `t=u` in (26) shows it is necessary. Therefore

\[
\mathcal E_C(\{0\})
=
\{(u,v):|v|\ge|u|\},
\tag{28}
\]

exactly the cone of AF-054. Translation gives (9).

For a fixed point `(u,v)`, equation (9) says

\[
(a,0)\in R_M((u,v))
\iff
|u-a|\le|v|,
\tag{29}
\]

which proves (10). Taking `a=u` proves existence for every point, while every `v\ne0` yields a nontrivial interval of coapproximants. The example therefore records classical non-Hilbert coapproximation geometry rather than an intrinsically new repair phenomenon.

### Non-singleton targets can have collective safe points

Now use the Euclidean norm with `M,S` as in (12), and put

\[
y=(0,1).
\]

For `x=(t,0)`,

\[
\|x-y\|^2=t^2+1.
\tag{30}
\]

The target distance is

\[
\operatorname{dist}(x,S)
=
\min\{|t-1|,|t+1|\}
=
\bigl||t|-1\bigr|,
\tag{31}
\]

so

\[
\|x-y\|^2-\operatorname{dist}(x,S)^2
=
t^2+1-(|t|-1)^2
=2|t|
\ge0.
\tag{32}
\]

Thus

\[
y\in\mathcal E_C(S).
\tag{33}
\]

But the Hilbert calculation gives

\[
\mathcal E_C(\{(-1,0)\})
=
\{-1\}\times\mathbb R,
\qquad
\mathcal E_C(\{(1,0)\})
=
\{1\}\times\mathbb R.
\tag{34}
\]

The point `(0,1)` belongs to neither. Hence the inclusion (11) is strict.

The mechanism is important. A singleton coapproximation requires one fixed target point `s` to beat `y` against **every** comparison point `x`. A set-target envelope only asks `y` to stay at least as far away as the distance to `S`, allowing the target point realizing or approximating `\operatorname{dist}(x,S)` to vary with `x`. That quantifier change creates collective safe points not attributable to any one singleton coapproximation fiber.

## Prior art and novelty assessment

The singleton linear theory is classical and must not be claimed as new.

- C. Franchetti and M. Furi, **“Some characteristic properties of real Hilbert spaces,”** *Revue Roumaine de Mathématiques Pures et Appliquées* 17 (1972), 1045–1048. Later coapproximation literature identifies this paper as the introduction of the best-coapproximation concept in normed spaces.
- Ivan Singer and Pier L. Papini, **“Best Coapproximation in Normed Linear Spaces,”** *Monatshefte für Mathematik* 88 (1979), 27–44, DOI `10.1007/BF01305855`. This is direct classical prior art on existence, characterization, and the set-valued best-coapproximation operator in normed linear spaces.
- H. Berens and U. Westphal, **“On the best coapproximation in a Hilbert space,”** in *Quantitative Approximation* (R. A. DeVore and K. Scherer, eds.), Academic Press (1980), 7–10. Role: direct Hilbert-space coapproximation prior art.
- T. D. Narang, **“On best coapproximation in normed linear spaces,”** *Rocky Mountain Journal of Mathematics* 22(1) (1992), 265–287, DOI `10.1216/rmjm/1181072810`. Role: survey and development of existence, uniqueness, coproximinality, co-Chebyshev behavior, and coapproximation operators.
- Eyad Abu-Sirhan and Zuhier Altawallbeh, **“Coproximinality in the Space of Bounded Functions,”** *International Journal of Mathematics and Mathematical Sciences* (2014), Article 196391, DOI `10.1155/2014/196391`. Its introduction states the standard definition used in (2), the set-valued notation `R_M`, and the coproximinal/co-Chebyshev existence/uniqueness terminology.

There is also an established literature under **best simultaneous coapproximation** (for example Geetha S. Rao and R. Saravanan, *Best simultaneous coapproximation*, *Indian Journal of Mathematics* 40(3) (1998), 353–362, as cited in later surveys). Therefore the non-singleton residual above should not be promoted as a novelty claim merely because it is not ordinary singleton coapproximation. The strict example (13) proves only a precise internal boundary: AF-054's general set-distance envelope is not the union of its singleton coapproximation fibers. A serious comparison with simultaneous-coapproximation definitions is still required before claiming that a broader set-target theorem is new.

The Arithmetic Fidelity contribution of this finding is thus **classification and redirection**, not a new theorem in approximation theory: it identifies exactly where AF-054 collapses to mature coapproximation language and isolates the quantifier-level residual that remains to be audited.

## Boundaries and failure modes

- The equivalence (3) uses the inclusion of a linear subspace into the ambient normed space. For a general isometric embedding `C:X\to Y` without linear structure, classical linear coapproximation need not apply.
- The translation law (4) depends on `M` being a linear subspace and the ambient metric being induced by a norm. It is not a generic metric-space identity.
- In a Hilbert space, `\mathcal E_C(\{m_0\})=m_0+M^\perp` holds whether or not `M` is closed. Closedness is needed for those fibers to cover all of `Y` and hence for global coproximinality/co-Chebyshev behavior.
- The `\ell^1` example should not be interpreted as saying every non-Hilbert subspace has many coapproximants. Coproximinality and uniqueness are genuine geometric properties and are extensively studied in the classical literature.
- Equation (11) is one-sided only. A safe point for a set target need not coapproximate any particular member of the target, as (13) proves.
- The existence of simultaneous-coapproximation literature means that the set-target residual needs its own exact dictionary before any novelty claim. Similar terminology is not enough; the quantifiers and objective functional must be compared explicitly.
- This finding does not alter AF-054's general metric theorem. It narrows the novelty interpretation of one important specialization and supplies a stronger prior-art audit rule for future target-envelope work.

## Consequences for Arithmetic Fidelity

AF-054 introduced a general maximal safe envelope for preserving distance to a structural target under isometric refinement. The present audit splits that object into two regimes.

For singleton targets inside normed-linear inclusions, the theory should import established coapproximation concepts rather than rediscover them under new names:

\[
\text{safe-envelope coverage}
\leftrightarrow
\text{coproximinality},
\qquad
\text{unique safe-envelope membership}
\leftrightarrow
\text{co-Chebyshev behavior}.
\tag{35}
\]

For non-singleton structural targets, the collective inequality can preserve a repair radius even when no individual target point is a best coapproximant. This is the more relevant residual for Arithmetic Fidelity because its structural targets are typically sets of admissible faithful representations, channels, spectra, or repairs rather than single points.

The next useful theorem should therefore not generalize singleton cones. It should ask whether the collective set-target envelope can be characterized by established simultaneous/coapproximation constructions, or whether additional hypotheses such as convexity, projection structure, equivalence-compatible target transport, or nonlinear category constraints produce a genuinely different invariant. Until that audit is done, singleton linear examples are prior art, not evidence of a new mathematical theory.