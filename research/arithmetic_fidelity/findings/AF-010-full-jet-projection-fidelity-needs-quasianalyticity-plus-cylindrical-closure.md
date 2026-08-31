# AF-010 — Full-jet projection fidelity needs quasianalyticity plus cylindrical closure

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

componentwise. Thus the formal Taylor series of `D` lies in

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
3. for a real-analytic germ `D`, formal basicness is sufficient and yields a real-analytic germ `R` with `D=R\circ\pi`;
4. more generally, let `(\mathcal Q_d)_{d\ge 1}` be a dimension-stable family of scalar smooth germ classes that is closed under subtraction, coordinate restriction, and pullback by coordinate projections (cylindrical extension). If every `\mathcal Q_d` is quasianalytic, then formal basicness is sufficient for every projection model;
5. the cylindrical-extension hypothesis in (4) is genuinely part of the proof: quasianalyticity and coordinate restriction alone do not guarantee that the comparison germ
   \[
   (u,v)\mapsto D(u,0)
   \]
   belongs to the same `(m+n)`-variable class, so they do not by themselves imply the factorization theorem;
6. within such a dimension-stable family, projection-model single-point full-jet fidelity for all coordinate projections is equivalent to quasianalyticity: nonzero flat germs give exact counterexamples after cylindrical pullback, while quasianalyticity plus the closure package gives recovery;
7. in any smooth germ class containing a nonzero flat germ, full infinite-jet basicness is **not** sufficient. In particular, in `C^\infty`,
   \[
   D(u,v)=
   \begin{cases}
   e^{-1/v_1^2},&v_1\ne0,\\
   0,&v_1=0
   \end{cases}
   \]
   has every vertical/mixed derivative equal to zero at the origin yet varies along vertical fibers;
8. for a real-analytic submersion `T:M\to N`, the analytic submersion theorem transfers the projection criterion to analytic local coordinates: local analytic factorization through `T` is equivalent to formal factorization of the infinite jet through the jet of `T` at one point;
9. for ordinary smooth submersions, neither a finite jet nor the complete infinite jet at one point can replace AF-007's neighborhood vertical audit or AF-001's exact fiber criterion.

The main consequence is a sharper category gate than “quasianalytic versus smooth.” A uniqueness principle can turn formal equality into actual equality only after the candidate comparison object is known to remain **inside the admissible function class**. Full-jet recovery therefore requires both uniqueness and closure under the structural operations used to reconstruct the putative factor.

## Derivation

### Exact factorization forces formal basicness

If

\[
D(u,v)=R(u),
\]

then every derivative containing at least one differentiation with respect to a vertical coordinate vanishes identically. Hence all mixed/vertical Taylor coefficients vanish at the origin.

Equivalently, the Taylor series of `D` is the pullback of the Taylor series of `R` under the formal projection

\[
\widehat\pi:(u,v)\mapsto u.
\]

This implication is purely formal and does not depend on analyticity.

## Finite-order jets can never certify local descent

Fix any finite order `k` and set

\[
D_k(u,v)=v_1^{k+1}.
\]

Every derivative of total order at most `k` containing a vertical differentiation vanishes at the origin. Thus any test inspecting only the `k`-jet sees the same vertical data as for the identically zero discriminator.

But

\[
D_k(u,t e_1)=t^{k+1},
\]

so `D_k` is not constant on any vertical fiber neighborhood and cannot factor through `\pi` locally.

The counterexample is polynomial. Therefore even in the real-analytic category **no universal finite derivative order** certifies local descent from one point.

## Full jets are complete for real-analytic germs

Assume `D` is real analytic near `(0,0)`. Componentwise,

\[
D(u,v)=\sum_{\alpha,\beta}c_{\alpha,\beta}u^\alpha v^\beta
\]

with a convergent multivariable Taylor series. Formal basicness gives

\[
c_{\alpha,\beta}=0
\qquad\text{whenever }\beta\ne0.
\]

Hence

\[
D(u,v)=\sum_\alpha c_{\alpha,0}u^\alpha.
\]

Defining

\[
R(u)=D(u,0)=\sum_\alpha c_{\alpha,0}u^\alpha
\]

gives, on a sufficiently small neighborhood,

\[
D=R\circ\pi.
\]

Thus

\[
\boxed{
D\text{ analytic and formally basic at one point}
\iff
D\text{ locally factors through }\pi.
}
\]

## The correct quasianalytic projection theorem

A bare quasianalytic uniqueness axiom is not enough to run the usual comparison argument. The theorem needs a family of germ classes stable under the operations that construct the comparison germ.

Let `\mathcal Q_d` be a scalar class of smooth germs at the origin of `\mathbb R^d`. Assume, for every relevant pair of dimensions:

1. **quasianalyticity**:
   \[
   j_0^\infty f=0\Longrightarrow f=0\text{ as a germ};
   \]
2. **subtraction closure** inside each `\mathcal Q_d`;
3. **coordinate restriction**: if `F\in\mathcal Q_{m+n}`, then
   \[
   u\mapsto F(u,0)
   \]
   lies in `\mathcal Q_m`;
4. **coordinate-projection pullback / cylindrical extension**: if `R\in\mathcal Q_m`, then
   \[
   (u,v)\mapsto R(u)=R\circ\pi(u,v)
   \]
   lies in `\mathcal Q_{m+n}`.

For a vector-valued germ, apply these assumptions componentwise.

Now let `D\in\mathcal Q_{m+n}^q` be formally basic and define

\[
R(u)=D(u,0).
\]

Restriction gives `R\in\mathcal Q_m^q`; cylindrical extension gives `R\circ\pi\in\mathcal Q_{m+n}^q`; subtraction therefore gives

\[
G=D-R\circ\pi\in\mathcal Q_{m+n}^q.
\]

Every pure `u` derivative of `G` at the origin vanishes because `D` and `R\circ\pi` have the same restriction to `v=0`. Every derivative containing a vertical factor vanishes by formal basicness of `D`. Hence

\[
j_0^\infty G=0.
\]

Quasianalyticity forces `G=0` as a germ, so

\[
D=R\circ\pi.
\]

Therefore

\[
\boxed{
\text{quasianalyticity + admissible cylindrical comparison}
\Longrightarrow
\text{single-point full-jet projection fidelity}.
}
\]

The closure under cylindrical extension cannot be deleted from this proof. Coordinate restriction only constructs the lower-dimensional germ `R`; it does not imply that its pullback `R\circ\pi` belongs to the original higher-dimensional class. Without that admissibility, the flat comparison germ `G` may not lie in a class on which quasianalytic uniqueness is available.

## Converse: flat germs obstruct full-jet projection fidelity

Assume the same dimension-stable pullback closure and suppose `\mathcal Q_n` contains a nonzero flat germ `f`:

\[
j_0^\infty f=0,
\qquad
f\ne0\text{ as a germ}.
\]

Pull `f` back to `\mathbb R^{m+n}` by the coordinate projection onto the vertical block:

\[
D(u,v)=f(v).
\]

By closure, `D` lies in the admissible higher-dimensional class. Since `f` is flat, every Taylor coefficient of `D` involving `v` vanishes, and the pure `u` coefficients vanish as well; in particular `D` is formally basic for the projection onto `u`.

If single-point full-jet projection fidelity held, `D` would equal `R(u)` locally. Evaluating at `v=0` gives `R(u)=f(0)=0`, hence `f(v)=0` locally, a contradiction.

Thus any nonzero flat germ destroys full-jet projection fidelity. Conversely, the previous section proves fidelity when the family is quasianalytic and closed under the required operations. Under this common dimensional closure package,

\[
\boxed{
\text{projection-model single-point full-jet fidelity}
\iff
\text{quasianalyticity}.
}
\]

The equivalence is therefore a statement about an **admissible family of function classes**, not about the uniqueness axiom in isolation.

## Ordinary smooth functions retain invisible vertical variation

In `C^\infty`, take

\[
\phi(t)=
\begin{cases}
 e^{-1/t^2},&t\ne0,\\
 0,&t=0.
\end{cases}
\]

and set

\[
D(u,v)=\phi(v_1).
\]

Every derivative of `D` at the origin is zero, so its complete formal Taylor series is identical to that of the zero discriminator. Nevertheless `D` varies with `v_1` and cannot factor through `\pi` locally.

Hence

\[
\boxed{
\text{identical infinite jets at one point}
\not\Rightarrow
\text{identical local structural behavior in }C^\infty.
}
\]

The failure survives every finite or infinite pointwise derivative audit simultaneously.

## Analytic-submersion corollary

Let

\[
T:M\to N
\]

be a real-analytic submersion and `D:M\to\mathbb R^q` real analytic. Around any `x\in M`, analytic submersion coordinates identify `T` with a coordinate projection. The analytic projection theorem therefore implies that local factorization of `D` through `T` is equivalent to formal basicness in those coordinates.

Coordinate-invariantly, if the infinite formal germ of `D` lies in the image of formal pullback by the infinite germ of `T`, then there is a real-analytic germ `R` at `T(x)` such that

\[
D=R\circ T
\]

locally.

For general Denjoy--Carleman or other quasianalytic categories, transferring the projection statement through arbitrary coordinate changes requires the corresponding composition, inverse-function, and regularity hypotheses. Those are not supplied by quasianalyticity alone.

## Relationship to AF-007 and AF-001

AF-007 established that for a smooth submersion with connected fibers, the neighborhood condition

\[
dD(\ker dT)=0
\]

is equivalent to smooth descent. It also showed that vanishing at a single point is insufficient.

The present result sharpens the pointwise boundary:

- first-order data at one point are insufficient;
- every finite-order jet at one point is insufficient, even analytically;
- the entire infinite jet at one point is sufficient in real-analytic classes;
- in more general quasianalytic classes, full-jet recovery additionally requires that the comparison germ produced by restriction and cylindrical extension remain admissible;
- the entire infinite jet at one point is insufficient in `C^\infty` because flat germs are admitted;
- the exact global fiber criterion of AF-001 remains category-independent.

This leaves three distinct audit scales:

1. **fiber audit** — exact and set-theoretic, but potentially global;
2. **neighborhood vertical audit** — first-order and complete for regular smooth connected-fiber submersions;
3. **single-point formal audit** — complete only when uniqueness and admissible reconstruction operations coexist.

## Prior art and novelty assessment

The ingredients are classical and the strongest nearby theorem is substantially deeper than this regular projection calculation.

Krantz and Parks give standard real-analytic background: multivariable analytic germs are represented by convergent Taylor series and analytic inverse/implicit-function machinery supplies the local coordinate changes used in the analytic submersion corollary. The analytic full-jet proof above is elementary classical analysis.

Thilliez's survey of quasianalytic local rings identifies quasianalyticity with injectivity of the Borel/Taylor map and recalls the Denjoy--Carleman characterization. Standard Denjoy--Carleman classes used in this literature carry considerably more algebraic/composition structure than the bare uniqueness axiom.

Belotto da Silva, Bierstone, and Chow prove a **composite quasianalytic function theorem**: for suitable quasianalytic Denjoy--Carleman classes, a function that is formally composite at a single point with a generically submersive map is locally composite, with a possible shift/loss in Denjoy--Carleman regularity. Their result contains a much harder singular/generically-submersive version of the formal-to-actual mechanism considered here. Arithmetic Fidelity therefore makes no novelty claim for formal compositeness from quasianalytic data.

Bierstone and Milman's earlier work on composite differentiable functions likewise places smooth factorization/composition questions in an established literature.

The Arithmetic Fidelity contribution is the **audit decomposition** exposed by the projection proof:

\[
\text{formal recovery}
=
\text{uniqueness of germs}
+
\text{admissibility of the reconstruction operations}.
\]

This prevents a uniqueness theorem from being used outside the category in which its comparison germ lives, and it gives a reusable checklist for other compression/recovery problems.

## Boundaries and failure modes

- The finite-order counterexample is pointwise. AF-007 already shows that first-order vertical vanishing on a whole neighborhood is sufficient for regular connected-fiber submersions.
- The quasianalytic theorem is only a projection-model theorem under the stated dimension-stable closure assumptions. Quasianalyticity alone is not asserted to imply those operations.
- Standard real-analytic and standard Denjoy--Carleman settings have stronger closure properties, but the exact hypotheses needed for a general coordinate-change or composite-function theorem must be checked in that class rather than inferred from the word “quasianalytic.”
- At singular or generically submersive maps, formal composition is not exhausted by the elementary projection argument; the Belotto da Silva--Bierstone--Chow theorem is relevant deeper prior art and may involve shifted regularity.
- Formal basicness at one point says nothing about disconnected global fibers, monodromy, covering sheets, or other nonlocal identifications. AF-001 remains the exact global criterion.
- Quasianalyticity supplies uniqueness, not numerical stability. A discriminator may be uniquely determined by its infinite jet while reconstruction is catastrophically ill-conditioned or require inaccessible derivative information.
- No claim is made that prime-sensitive data are analytic or quasianalytic in any useful representation.

## Consequence for the line

Do not pursue a generic “higher jets eventually recover the discriminator” program. There is no universal finite derivative order, and in ordinary smooth categories even the complete infinite jet at one point can miss real fiber variation.

For pointwise formal recovery, audit two independent gates:

1. **uniqueness:** does the function category exclude nonzero flat germs or otherwise make the formal data determining?;
2. **admissibility:** are restriction, pullback/cylindrical extension, subtraction, coordinate changes, and any other reconstruction operations actually closed inside the category where uniqueness is invoked?

Only after both gates pass should a full-jet certificate be treated as a valid recovery mechanism. Otherwise the audit must use neighborhood, fiber, relational, boundary, or other nonlocal structure.