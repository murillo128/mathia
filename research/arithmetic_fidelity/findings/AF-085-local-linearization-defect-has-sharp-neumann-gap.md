# AF-085 — Local linearization defect has a sharp Neumann gap for quotient repair

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-BOUNDARY`

## Claim

Let `E` and `F` be real or complex Banach spaces with `F != {0}`, let

\[
q:E\to F
\tag{1}
\]

be a bounded linear surjection, let `U\subset F` be open, and let

\[
s:U\to E,
\qquad
qs(y)=y
\quad(y\in U)
\tag{2}
\]

be an arbitrary local right inverse. No continuity, homogeneity, or differentiability of `s` is assumed. Fix `y_0\in U`. For a bounded linear candidate tangent `A\in\mathcal L(F,E)`, define its local relative linearization defect by

\[
\Lambda_{s,y_0}(A)
:=
\limsup_{\substack{h\to0\\ h\ne0\\ y_0+h\in U}}
\frac{\|s(y_0+h)-s(y_0)-Ah\|}{\|h\|}
\in[0,+\infty].
\tag{3}
\]

Then quotient repair has an exact first-order threshold.

1. **Every local tangent defect controls the operator right-inverse defect.** For every `A\in\mathcal L(F,E)`,

   \[
   \boxed{
   \|I_F-qA\|
   \le
   \|q\|\,\Lambda_{s,y_0}(A).
   }
   \tag{4}
   \]

   Thus an approximately correct first-order lift cannot hide a large failure of `A` to be an approximate linear right inverse.

2. **Sub-threshold local linearization forces an exact global linear split.** If

   \[
   \Lambda_{s,y_0}(A)<\frac1{\|q\|},
   \tag{5}
   \]

   then `qA` is invertible by the Neumann lemma and

   \[
   \boxed{
   V:=A(qA)^{-1}:F\to E
   }
   \tag{6}
   \]

   is a bounded linear right inverse of `q`. More quantitatively, with

   \[
   r:=\|I_F-qA\|<1,
   \tag{7}
   \]

   one has

   \[
   \boxed{
   \|V\|
   \le
   \frac{\|A\|}{1-r}
   \le
   \frac{\|A\|}{1-\|q\|\Lambda_{s,y_0}(A)}.
   }
   \tag{8}
   \]

3. **A nonsplitting quotient has a uniform first-order defect gap at every point of every section.** If `q` has no bounded linear right inverse, then for every local section `s`, every `y_0\in U`, and every bounded linear `A:F\to E`,

   \[
   \boxed{
   \Lambda_{s,y_0}(A)
   \ge
   \frac1{\|q\|}.
   }
   \tag{9}
   \]

   In particular, for a normalized nonzero quotient map `q:E\to E/K`, where `\|q\|=1`, no local section can have relative bounded-linear tangent defect strictly below `1` at any point.

4. **The underlying unconstrained approximate-right-inverse problem is exactly `0/1` valued.** Define

   \[
   \beta(q)
   :=
   \inf_{A\in\mathcal L(F,E)}\|I_F-qA\|.
   \tag{10}
   \]

   Then

   \[
   \boxed{
   \beta(q)=
   \begin{cases}
   0,&q\text{ has a bounded linear right inverse},\\
   1,&q\text{ has no bounded linear right inverse}.
   \end{cases}}
   \tag{11}
   \]

   Indeed `A=0` always gives defect `1`, while any defect strictly below `1` is corrected to an exact right inverse by Neumann inversion. Therefore unrestricted operator-norm "approximate splitting" has no nontrivial intermediate regime below the unit threshold.

5. **One Fréchet-smooth local section point is already an existence certificate for global linear splitting.** The following are equivalent:

   \[
   \boxed{
   \begin{array}{c}
   q\text{ has a bounded linear right inverse};\\
   \text{some local right inverse of }q\text{ is Fréchet differentiable at one point};\\
   \text{some }C^1\text{ local right inverse exists}.
   \end{array}}
   \tag{12}
   \]

   The forward direction uses a global bounded linear section. For the reverse direction, differentiability gives `\Lambda_{s,y_0}(Ds(y_0))=0`, so (4) yields `qDs(y_0)=I_F`. This is the classical split-submersion boundary in Banach differential geometry.

6. **The unit gap is sharp for the canonical nonsplitting metric control.** Take the AF-081 example of a normalized quotient

   \[
   q:\ell^p\to\ell^p/K,
   \qquad
   1<p<\infty,
   \quad p\ne2,
   \tag{13}
   \]

   with `K` closed and uncomplemented, and let `s_K` be the unique minimum-norm homogeneous section. AF-081 gives

   \[
   \|s_K(h)\|=\|h\|,
   \qquad
   s_K(0)=0.
   \tag{14}
   \]

   Hence for `A=0`,

   \[
   \Lambda_{s_K,0}(0)=1.
   \tag{15}
   \]

   Equation (9) gives the reverse inequality for every `A`, so

   \[
   \boxed{
   \inf_A\Lambda_{s_K,0}(A)=1.
   }
   \tag{16}
   \]

   The obstruction is therefore not merely qualitative non-differentiability: the natural canonical nonlinear repair sits exactly at the sharp normalized first-order barrier.

7. **This strictly broadens the existence obstruction of AF-084 but not its rigidity conclusion.** AF-084 uses positive homogeneity at the distinguished apex to show that a linear tangent to that same section forces the section itself to equal the tangent globally. Here no homogeneity is required and the test applies at any interior point of any local right inverse. The price is that (5) produces an exact linear section `V`, but does **not** imply that the original nonlinear `s` equals `V`.

The reusable Arithmetic Fidelity conclusion is that, in the unconstrained Banach-linear category, **first-order approximate quotient repair has a hard Neumann phase transition**. Below normalized relative defect `1`, approximation automatically upgrades to exact global linear recovery. If linear splitting is forbidden, every local section must remain at least one full normalized unit away from every bounded-linear tangent model. Any genuinely graded notion of approximate repair must therefore constrain the admissible tangent category, weaken the topology/norm, or retain additional structure rather than merely allow arbitrary bounded-linear near-sections.

## Derivation

### The section identity pushes every tangent error through the quotient

For sufficiently small `h` with `y_0+h\in U`, define

\[
e_A(h):=s(y_0+h)-s(y_0)-Ah.
\tag{17}
\]

Using (2),

\[
q e_A(h)
=
(y_0+h)-y_0-qAh
=
(I_F-qA)h.
\tag{18}
\]

Fix a unit vector `u\in F`. Since `U` is open, `y_0+tu\in U` for all sufficiently small `t`. For `t\ne0`, (18) gives

\[
\|(I_F-qA)u\|
=
\frac{\|q e_A(tu)\|}{|t|}
\le
\|q\|\frac{\|e_A(tu)\|}{|t|}.
\tag{19}
\]

Taking `\limsup_{t\to0}` and then the supremum over `\|u\|=1` proves (4). This argument is purely local and does not use regularity of `s` beyond the value of the declared defect.

### Neumann correction turns sufficiently good approximation into exact repair

Assume (5). By (4),

\[
r:=\|I_F-qA\|<1.
\tag{20}
\]

The standard Neumann series in the Banach algebra `\mathcal L(F)` gives

\[
(qA)^{-1}
=
\sum_{n=0}^{\infty}(I_F-qA)^n,
\qquad
\|(qA)^{-1}\|\le\frac1{1-r}.
\tag{21}
\]

Therefore `V=A(qA)^{-1}` is bounded linear and

\[
qV
=qA(qA)^{-1}
=I_F,
\tag{22}
\]

with the bound (8). The local section `s` is used only to force the approximate right-inverse estimate; once `qA` lies inside the Neumann ball of the identity, exact global repair is algebraic.

If `q` does not split, (20) is impossible for every `A`, so

\[
\|I_F-qA\|\ge1.
\tag{23}
\]

Combining (23) with (4) yields (9). Since `A=0` gives `\|I_F-qA\|=1`, (11) follows immediately.

### Differentiability is the zero-defect endpoint

If `s` is Fréchet differentiable at `y_0` with derivative `A=Ds(y_0)`, then by definition

\[
\|s(y_0+h)-s(y_0)-Ah\|
=o(\|h\|),
\tag{24}
\]

so `\Lambda_{s,y_0}(A)=0`. Equation (4) then gives `qA=I_F` directly. Equivalently, differentiating the identity `q\circ s=I` gives the same statement by the Banach-space chain rule.

This is the linear model of the standard Banach-manifold fact that a smooth local section through a point supplies a bounded linear splitting of the tangent map there. Conversely, if `q` already has a bounded linear right inverse `V`, then `s=V` is a global smooth section. Thus (12) is an existence classification, not a claim that every section of a split quotient is smooth.

## Exact controls

### Split Hilbert control: zero defect

If `E` is Hilbert and `K=\ker q` is closed, the orthogonal minimum-norm section

\[
V:E/K\to K^\perp\subset E
\tag{25}
\]

is bounded linear. Taking `s=V` and `A=V` gives `\Lambda_{s,y_0}(A)=0` at every point, the zero endpoint of the phase diagram.

### Nonsplit uniformly convex control: exact unit defect

For AF-081's uncomplemented `K\subset\ell^p`, the minimum-norm section is continuous, canonical relative to the norm, and positive homogeneous but the quotient does not split. Equation (16) shows that its apex is exactly one unit away, in relative first-order defect, from the entire bounded-linear tangent class. This supplies sharpness rather than merely an example with positive defect.

### Smooth nonlinear split control: differentiability does not linearize the section

Suppose `q` splits and fix one bounded linear section `V`. For any Fréchet-smooth map

\[
k:U\to\ker q,
\tag{26}
\]

the map

\[
s(y)=Vy+k(y)
\tag{27}
\]

is again a local right inverse. Choosing nonlinear `k` gives a nonlinear smooth section. At `y_0`,

\[
Ds(y_0)=V+Dk(y_0)
\tag{28}
\]

is still an exact linear right inverse because `qDk(y_0)=0`. Hence AF-085 cannot be strengthened to say that a differentiable section must itself be linear. That stronger conclusion in AF-084 depends essentially on positive homogeneity at the apex.

### Directional regularity control

A nonlinear directional derivative need not trigger this theorem. AF-084 already shows that a continuous positive-homogeneous nonlinear section can have all one-sided and Hadamard directional derivatives at the apex, with derivative map equal to the nonlinear section itself. The split conclusion requires a bounded **linear** first-order model whose relative defect crosses the threshold in (5).

## Prior art and novelty assessment

The ingredients behind the classification are classical, and no novelty is claimed for the Neumann lemma, differentiating a right-inverse identity, Banach split-submersion theory, or nonlinear continuous selections.

- Walter Rudin, ***Functional Analysis***, 2nd ed., McGraw-Hill (1991). Role: standard Banach-algebra/functional-analysis source for the Neumann-series principle that `I-R` is invertible whenever `\|R\|<1`, which is the exact algebraic threshold used in (20)--(22).
- André Henriques, **“Integrating L-infinity algebras,”** *Compositio Mathematica* 144 (2008), 1017--1045, DOI `10.1112/S0010437X07003405`. Section 4 recalls the standard Banach-manifold convention that a submersion has split-surjective tangent maps and is locally equivalent to a projection, and uses local sections as an equivalent working definition, citing Lang and Abraham--Marsden--Ratiu. This is direct prior-art context for the zero-defect differentiability endpoint in (12).
- Robert G. Bartle and Lawrence M. Graves, **“Mappings between function spaces,”** *Transactions of the American Mathematical Society* 72 (1952), 400--413, DOI `10.1090/S0002-9947-1952-0047910-X`. Role: classical continuous-selection background showing that nonlinear continuous right inverses exist far beyond the linearly split category.
- Miek Messerschmidt, **“A Pointwise Lipschitz Selection Theorem,”** *Set-Valued and Variational Analysis* 27 (2019), 223--240, DOI `10.1007/s11228-017-0455-2`. Role: refined selection boundary; positively homogeneous continuous right inverses of Banach surjections can have pointwise Lipschitz regularity on a dense set without yielding a global linear split, so pointwise Lipschitz behavior must not be confused with the bounded-linear first-order approximation tested here.
- AF-078 and AF-081--AF-084 supply the persisted Mathia quotient-repair hierarchy: linear splitting and canonicity gates, canonical nonlinear metric repair beyond splitting, global Lipschitz linearization for separable quotients, bounded-scale uniform repair, and homogeneity-apex tangent rigidity.

The elementary inequality (4) and its sharp-gap packaging are derived here from the exact right-inverse identity plus the classical Neumann threshold. A bounded literature search found the expected split-submersion, continuous-selection, and approximate-inverse mechanisms but did not justify a novelty claim for this particular formulation. The durable Arithmetic Fidelity contribution is therefore the **category-level quantitative synthesis**: arbitrary bounded-linear approximate tangent repair is not a gradual escape from nonsplitting; it has a sharp subunit threshold at which exact splitting is forced.

## Boundaries and failure modes

- The openness of `U` is load-bearing for the full operator-norm estimate (4): every direction must be available for sufficiently small perturbations. A section defined only on a cone, boundary stratum, or restricted subset would require a tangent-cone version and can have a weaker directional obstruction.
- The normalized threshold `1` refers to quotient maps with `\|q\|=1`. For a general bounded surjection the local defect threshold is `1/\|q\|`; the operator defect `\|I-qA\|` still has the universal Neumann threshold `1`.
- Equation (9) is a lower bound for approximation by bounded **linear** models. It says nothing against useful nonlinear first-order models, Hölder models, bounded-scale uniform repair, or category-constrained lifts such as those studied in AF-079--AF-083.
- Splitting is an existence conclusion. If `q` splits, a particular badly behaved or nonlinear section may still have large or infinite `\Lambda`; only some exact linear section has zero defect.
- The result does not make `\Lambda` intrinsic under arbitrary renorming. As with other quantitative Banach-space constants, its numerical value depends on the declared norms; the normalized quotient convention fixes the natural scale used in (9) and (16).
- No claim is made that the threshold alone captures canonicity, equivariance, positivity, locality, arithmetic provenance, or another constrained repair category. In fact (11) shows why such additional constraints are necessary if one wants a nontrivial graded theory of approximate linear recovery.