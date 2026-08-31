# AF-008 — Formal jet fidelity has a quasianalyticity boundary

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `NEGATIVE/OBSTRUCTION`

## Claim

Let

\[
\pi:\mathbb R^{m+n}\to\mathbb R^m,
\qquad
\pi(u,v)=u,
\]

and let

\[
D:(\mathbb R^{m+n},0)\to\mathbb R^q
\]

be a germ. Call `D` **formally basic for `\pi` at `0`** when every Taylor coefficient involving at least one vertical variable vanishes, equivalently

\[
\partial_u^\alpha\partial_v^\beta D(0,0)=0
\qquad
\text{for every }\alpha\in\mathbb N^m,
\ \beta\in\mathbb N^n\setminus\{0\},
\]

componentwise. This means that the formal Taylor series of `D` belongs to

\[
\mathbb R[[u]]^q\subset \mathbb R[[u,v]]^q.
\]

Then:

1. if `D` actually factors locally through `\pi`, so that
   \[
   D=R\circ\pi,
   \]
   then `D` is formally basic;
2. **no finite jet order is sufficient** for the converse, even for polynomials: for every `k`,
   \[
   D_k(u,v)=v_1^{k+1}
   \]
   passes every vertical/mixed derivative test of total order at most `k` at the origin but does not factor through `\pi` on any neighborhood;
3. for a real-analytic germ `D`, formal basicness is sufficient: there is a real-analytic germ `R` with
   \[
   D=R\circ\pi;
   \]
4. more generally, in any quasianalytic germ class closed under coordinate restriction and subtraction, formal basicness is sufficient in the projection model;
5. in any smooth germ class containing a nonzero flat germ, full infinite-jet basicness is **not** sufficient. In particular, for `C^\infty`,
   \[
   D(u,v)=
   \begin{cases}
   e^{-1/v_1^2},&v_1\ne0,\\
   0,&v_1=0
   \end{cases}
   \]
   has every derivative involving `v` equal to zero at the origin, yet varies along every sufficiently small vertical fiber;
6. therefore, in the projection model, the principle
   
   > “a single full infinite jet decides whether a discriminator locally descends through the compression”
   
   is precisely a **quasianalyticity phenomenon**: it holds when the Borel/Taylor map is injective on germs and fails whenever nonzero flat germs are admitted;
7. for a real-analytic submersion `T:M\to N`, the analytic submersion theorem transfers this criterion to analytic local coordinates. Thus local analytic factorization through `T` is equivalent to formal factorization of the infinite jet through the jet of `T` at one point;
8. for ordinary smooth submersions, neither a finite jet nor the complete infinite jet at one point can replace AF-007's neighborhood vertical audit or AF-001's full fiber criterion.

The main consequence for Arithmetic Fidelity is a sharp **regularity-category boundary**. Higher-order local data do not monotonically converge to a complete pointwise certificate in the smooth category. The entire infinite Taylor tower can still miss genuine structural variation. Pointwise formal data become complete only in classes with a uniqueness principle strong enough to rule out flat germs.

## Derivation

### Exact factorization forces formal basicness

If

\[
D(u,v)=R(u),
\]

then every derivative containing at least one differentiation with respect to a vertical coordinate `v_j` vanishes identically. Hence all mixed/vertical Taylor coefficients vanish at the origin.

Equivalently, the Taylor series of `D` is the pullback of the Taylor series of `R` under the formal projection

\[
\widehat\pi:(u,v)\mapsto u.
\]

This implication is purely formal and does not depend on analyticity.

## Finite-order jets can never certify local descent

Fix any finite order `k`. Let

\[
D_k(u,v)=v_1^{k+1}.
\]

Every derivative of total order at most `k` containing a vertical differentiation vanishes at the origin. Thus any test inspecting only the `k`-jet concludes exactly what it would conclude for the identically zero discriminator.

But `D_k` is not constant on any vertical fiber neighborhood:

\[
D_k(u,t e_1)=t^{k+1}.
\]

Therefore `D_k` cannot factor through `\pi` locally.

This counterexample is polynomial, so the obstruction is not caused by pathological smoothness. Even inside the real-analytic category, **every fixed finite jet order is incomplete**.

Consequently, AF-007's first-order defect cannot be repaired by selecting some universal finite derivative order. Any finite-order point audit has an exact analytic counterexample one order higher.

## Full jets are complete for real-analytic germs

Assume now that `D` is real analytic near `(0,0)`. Write its convergent multivariable Taylor expansion componentwise as

\[
D(u,v)
=
\sum_{\alpha,\beta}
 c_{\alpha,\beta}
 u^\alpha v^\beta.
\]

Formal basicness says

\[
c_{\alpha,\beta}=0
\qquad\text{whenever }\beta\ne0.
\]

Hence the convergent series reduces to

\[
D(u,v)
=
\sum_\alpha c_{\alpha,0}u^\alpha.
\]

Define

\[
R(u)=D(u,0)
=
\sum_\alpha c_{\alpha,0}u^\alpha.
\]

Then, on a sufficiently small neighborhood,

\[
D(u,v)=R(u)=R(\pi(u,v)).
\]

Thus

\[
\boxed{
D\text{ analytic and formally basic at one point}
\iff
D\text{ locally factors through }\pi.
}
\]

The important distinction from AF-007 is that the hypothesis is concentrated at a **single point**, but uses the entire infinite analytic jet rather than first-order data on a neighborhood.

## Quasianalytic generalization

The same argument does not fundamentally require convergence of the Taylor series; it requires that the Taylor series uniquely determine the germ.

Let `\mathcal Q` be a class of smooth germs satisfying the quasianalytic uniqueness property at the origin:

\[
j_0^\infty f=0
\Longrightarrow
f=0\text{ as a germ},
\]

and assume the class is closed under restriction to the coordinate slice `v=0` and subtraction.

For a formally basic `D`, define

\[
G(u,v)=D(u,v)-D(u,0).
\]

Every pure `u` derivative of `G` at the origin vanishes because the two terms have identical restriction to `v=0`. Every derivative containing a vertical factor vanishes by formal basicness of `D`. Therefore

\[
j_0^\infty G=0.
\]

Quasianalyticity forces

\[
G=0
\]

as a germ, so

\[
D(u,v)=D(u,0)
\]

locally. Taking

\[
R(u)=D(u,0)
\]

gives the desired factorization.

Thus the actual engine is injectivity of the Borel/Taylor map, not analyticity specifically.

## Nonquasianalytic classes admit invisible vertical variation

Suppose instead that the function class contains a nonzero flat one-variable germ `\phi`:

\[
\phi^{(j)}(0)=0
\qquad\text{for every }j\ge0,
\]

but `\phi` is not identically zero near `0`.

Set

\[
D(u,v)=\phi(v_1).
\]

Then every mixed/vertical derivative of `D` at the origin vanishes, so the complete formal Taylor series is identical to that of the zero discriminator. Nevertheless `D` varies with `v_1` and therefore does not factor through `\pi`.

For ordinary smooth functions one may take

\[
\phi(t)=
\begin{cases}
 e^{-1/t^2},&t\ne0,\\
 0,&t=0.
\end{cases}
\]

which is smooth, nonzero away from the origin, and flat at the origin.

So in `C^\infty`:

\[
\boxed{
\text{identical infinite jets at one point}
\not\Rightarrow
\text{identical local structural behavior}.
}
\]

This is stronger than AF-007's example `D=y^2`, which only defeated first-order inspection at a point. A flat germ defeats **every derivative order simultaneously**.

## Quasianalyticity is the exact projection-model boundary

The previous two arguments give a converse characterization.

Assume a germ class has the following projection-fidelity property:

> For the scalar projection `\pi(u,v)=u`, every germ whose full Taylor series contains no `v`-dependent term actually factors locally through `\pi`.

Take any one-variable flat germ `f(v)` in the class and regard it as

\[
D(u,v)=f(v).
\]

Its Taylor series is zero and is therefore formally basic. By the assumed projection-fidelity property, `D` must be independent of `v` near the origin. Since `f(0)=0`, this forces

\[
f=0
\]

as a germ.

Hence the projection-fidelity property excludes every nonzero flat germ, i.e. the Taylor/Borel map is injective. Conversely, injectivity gave the factorization theorem above.

Therefore, under the mild closure assumptions used above,

\[
\boxed{
\text{single-point full-jet fidelity for a projection}
\iff
\text{quasianalyticity}.
}
\]

This identifies a precise established mathematical property controlling whether formal local information is enough to certify structural survival.

## Analytic-submersion corollary

Let

\[
T:M\to N
\]

be a real-analytic submersion and let `D:M\to\mathbb R^q` be real analytic. Around any point `x\in M`, analytic submersion coordinates identify `T` with a projection

\[
(u,v)\mapsto u.
\]

In those coordinates, local factorization of `D` through `T` is equivalent to formal basicness as above. Coordinate-invariantly, this says that the infinite formal germ of `D` lies in the image of formal pullback by the infinite germ of `T`.

Thus

\[
\boxed{
\widehat D_x
=
\widehat R_{T(x)}\circ\widehat T_x
\quad\Longrightarrow\quad
D=R\circ T
\text{ locally}
}
\]

for real-analytic submersions.

The regular-submersion case is deliberately simpler than singular formal-composition problems. At singular or merely generically submersive maps, formal compositeness can be substantially subtler and may involve regularity loss.

## Relationship to AF-007 and AF-001

AF-007 established that for a smooth submersion with connected fibers, the neighborhood condition

\[
dD(\ker dT)=0
\]

is equivalent to smooth descent. It also showed that vanishing at a single point is insufficient.

AF-008 sharpens the pointwise boundary:

- first-order data at one point are insufficient;
- every finite-order jet at one point is insufficient, even analytically;
- the entire infinite jet at one point is sufficient in quasianalytic categories;
- the entire infinite jet at one point is still insufficient in `C^\infty`;
- the exact global fiber criterion of AF-001 remains category-independent.

So there are now three distinct audit scales:

1. **fiber audit** — exact and set-theoretic, but potentially global;
2. **neighborhood vertical audit** — first-order and complete for regular smooth connected-fiber submersions;
3. **single-point formal audit** — complete only under quasianalytic uniqueness.

These must not be conflated.

## Prior art and novelty assessment

The ingredients are classical and the strongest nearby theorem is substantially deeper than this regular projection calculation.

Krantz and Parks give standard real-analytic background: multivariable analytic germs are represented by convergent Taylor series and analytic inverse/implicit-function machinery supplies the local coordinate changes used in the analytic submersion corollary. The analytic full-jet proof above is therefore elementary classical analysis.

Thilliez's survey of quasianalytic local rings explicitly identifies quasianalyticity with injectivity of the Borel/Taylor map and recalls the Denjoy-Carleman characterization. Accordingly, the equivalence between full-jet uniqueness and absence of flat germs is established theory and is not a new Arithmetic Fidelity theorem.

Most decisively, Belotto da Silva, Bierstone, and Chow prove a **composite quasianalytic function theorem**: for suitable quasianalytic Denjoy-Carleman classes, a function that is formally composite at a single point with a generically submersive map is locally composite, with a possible shift/loss in Denjoy-Carleman regularity. Their result contains a much harder singular/generically-submersive version of the formal-to-actual mechanism considered here. Therefore Arithmetic Fidelity must not claim novelty for “formal compositeness at one point implies local composition” in the quasianalytic setting.

Bierstone and Milman's earlier work on composite differentiable functions likewise places smooth factorization/composition questions in an established literature.

The useful contribution here is the **fidelity classification** of local audit strength:

\[
\text{finite jet}
\;<\;
\text{full formal jet}
\;<\;?\;
\text{actual germ},
\]

where the second gap closes exactly in quasianalytic classes but remains open in `C^\infty`. This converts AF-007's vague “higher-order jets may matter” boundary into a precise no-go theorem and routes future work toward formal-composition/quasianalytic theory rather than inventing an ad hoc hierarchy of ever-higher derivatives.

## Boundaries and failure modes

- The finite-order counterexample is pointwise. AF-007 already shows that first-order vertical vanishing on a whole neighborhood is sufficient for regular connected-fiber submersions.
- The quasianalytic proof is stated first for the projection model with closure under coordinate restriction and subtraction. Transfer to general Denjoy-Carleman manifolds requires the appropriate class to support the needed coordinate/inverse-function operations.
- At singular or generically submersive maps, formal composition is not exhausted by the elementary projection argument; the Belotto da Silva-Bierstone-Chow theorem is the relevant deeper prior art and can involve a shifted regularity class.
- Formal basicness at one point says nothing about disconnected global fibers, monodromy, covering sheets, or other nonlocal identifications. AF-001 remains the exact global criterion.
- Quasianalyticity supplies uniqueness, not numerical stability. A discriminator may be uniquely determined by its infinite jet while reconstruction is catastrophically ill-conditioned or require inaccessible derivative information.
- No claim is made that prime-sensitive data are analytic or quasianalytic in any useful representation. The result is a category gate: if a proposed RH mechanism relies on recovering lost structure from formal local data, its regularity class becomes part of the mathematical hypothesis.

## Consequence for the line

Do not pursue a generic “higher jets eventually recover the discriminator” program. There is no universal finite derivative order, and in ordinary smooth categories even the complete infinite jet at one point can miss real fiber variation.

Instead, when a candidate compression is local/differential, first classify the **function category** and ask whether it is quasianalytic. If it is, formal compositeness can be a meaningful recovery certificate and established composite-function theory should be consulted. If it is not, pointwise Taylor data are fundamentally incomplete and the audit must use neighborhood, fiber, relational, boundary, or other nonlocal structure.