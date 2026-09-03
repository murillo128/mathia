# AF-086 — Tangent-cone norming modulus controls restricted-domain quotient fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-BOUNDARY`

## Claim

Let `E` and `F` be real or complex Banach spaces, let

\[
q:E\to F
\tag{1}
\]

be a bounded linear surjection, let `S\subseteq F`, and let `y_0\in S` be an accumulation point of `S`. Suppose

\[
s:S\to E,
\qquad
qs(y)=y
\quad(y\in S)
\tag{2}
\]

is an arbitrary right inverse on the restricted domain `S`. For a bounded linear candidate first-order lift `A\in\mathcal L(F,E)`, define

\[
\Lambda_{S,s,y_0}(A)
:=
\limsup_{\substack{y\to y_0\\y\in S,\ y\ne y_0}}
\frac{\|s(y)-s(y_0)-A(y-y_0)\|}{\|y-y_0\|}.
\tag{3}
\]

Let `C=T_S(y_0)` be the Bouligand/contingent tangent cone:

\[
C
:=
\left\{v\in F:
\begin{array}{l}
\text{there exist }t_n\downarrow0\text{ and }v_n\to v\\
\text{with }y_0+t_nv_n\in S
\end{array}
\right\}.
\tag{4}
\]

Write `B_F` for the closed unit ball and define the **tangent norming modulus**

\[
\nu(C)
:=
\sup\left\{
\nu\ge0:
\nu B_F\subseteq
\overline{\operatorname{aco}}(C\cap B_F)
\right\}
\in[0,1],
\tag{5}
\]

where `aco` denotes the absolutely convex hull over the base field. Equivalently, by Hahn--Banach separation,

\[
\boxed{
\nu(C)
=
\inf_{\|\phi\|=1}
\sup_{v\in C\cap B_F}|\phi(v)|.
}
\tag{6}
\]

Thus `\nu(C)>0` exactly when the available first-order directions form a quantitatively norming set for the ambient space.

Then restricted-domain quotient repair has two distinct fidelity gates.

1. **The section identity controls every available tangent direction.** For every `v\in C`,

   \[
   \boxed{
   \|(I_F-qA)v\|
   \le
   \|q\|\,\Lambda_{S,s,y_0}(A)\,\|v\|.
   }
   \tag{7}
   \]

2. **Norming tangent coverage upgrades directional control to ambient operator control.** If `\nu(C)>0`, then

   \[
   \boxed{
   \|I_F-qA\|
   \le
   \frac{\|q\|}{\nu(C)}
   \Lambda_{S,s,y_0}(A).
   }
   \tag{8}
   \]

   Consequently, if

   \[
   \boxed{
   \Lambda_{S,s,y_0}(A)
   <
   \frac{\nu(C)}{\|q\|},
   }
   \tag{9}
   \]

   then `qA` lies in the Neumann ball of `I_F`, hence is invertible, and

   \[
   V:=A(qA)^{-1}:F\to E
   \tag{10}
   \]

   is a bounded linear global right inverse of `q`.

3. **Nonsplitting imposes a tangent-coverage-weighted first-order gap.** If `q` has no bounded linear right inverse and `\nu(C)>0`, then every restricted section `s` and every bounded linear `A:F\to E` satisfy

   \[
   \boxed{
   \Lambda_{S,s,y_0}(A)
   \ge
   \frac{\nu(C)}{\|q\|}.
   }
   \tag{11}
   \]

   Thus the sharp unit Neumann barrier of AF-085 is attenuated exactly by how completely the restricted domain exposes ambient directions.

4. **Exact zero-defect fidelity needs only total tangent directions, not positive norming modulus.** If

   \[
   \overline{\operatorname{span}}\,C=F
   \tag{12}
   \]

   and

   \[
   \Lambda_{S,s,y_0}(A)=0,
   \tag{13}
   \]

   then (7) gives `(I_F-qA)v=0` on `C`, hence by linearity and continuity

   \[
   qA=I_F.
   \tag{14}
   \]

   Therefore one can have qualitative exact fidelity with `\nu(C)=0`: dense linear directional coverage is enough to propagate an **exact** first-order identity, while a positive `\nu(C)` is what supplies a **robust quantitative margin**.

5. **The norming modulus is the optimal universal directional-to-operator conversion constant.** For every Banach space `G` and every bounded linear `R:F\to G`,

   \[
   \boxed{
   \nu(C)\,\|R\|
   \le
   \sup_{v\in C\cap B_F}\|Rv\|.
   }
   \tag{15}
   \]

   No larger constant than `\nu(C)` works uniformly for all scalar-valued `R=\phi\in F^*`, by (6). Hence the loss factor in passing from tangent-direction information to an arbitrary ambient operator is not a proof artifact: it is exactly the norming strength of the available direction set. This optimality concerns the universal operator-conversion step; it does not assert that every quotient/section pair attains equality in (11).

The reusable Arithmetic Fidelity conclusion is that **restricted-domain first-order fidelity is governed by directional coverage, not by interiority itself**. The closed linear span of the tangent cone decides whether exact zero error propagates globally; the norming modulus decides whether small error has a positive stability threshold. A boundary can therefore be as informative as an open neighborhood, while a large-looking but nonnorming family of directions can retain exact information with arbitrarily poor robustness.

## Derivation

### The right-inverse identity propagates the local error through the quotient

Put

\[
e_A(y)
:=
s(y)-s(y_0)-A(y-y_0).
\tag{16}
\]

Because `qs(y)=y` on `S`,

\[
q e_A(y)
=
(I_F-qA)(y-y_0).
\tag{17}
\]

Fix `v\in C`. By (4), choose `t_n\downarrow0` and `v_n\to v` with

\[
y_n:=y_0+t_nv_n\in S.
\tag{18}
\]

For nonzero `v` the points `y_n` are eventually distinct from `y_0`; the case `v=0` is trivial. From (17),

\[
(I_F-qA)v_n
=
\frac{q e_A(y_n)}{t_n}.
\tag{19}
\]

Therefore

\[
\|(I_F-qA)v_n\|
\le
\|q\|
\frac{\|e_A(y_n)\|}{\|y_n-y_0\|}
\|v_n\|.
\tag{20}
\]

Taking `\limsup` and using continuity of `I_F-qA` proves (7).

### Absolute convex coverage is exactly what a linear operator can see

Let

\[
D:=C\cap B_F,
\qquad
M_R:=\sup_{v\in D}\|Rv\|.
\tag{21}
\]

If `0\le\nu<\nu(C)`, then by definition every `x\in\nu B_F` lies in the closed absolutely convex hull of `D`. A bounded linear map sends an absolutely convex combination of points of `D` into the ball of radius `M_R`; passing to the closure gives

\[
\|Rx\|\le M_R
\qquad(x\in\nu B_F).
\tag{22}
\]

Hence

\[
\nu\|R\|\le M_R.
\tag{23}
\]

Letting `\nu\uparrow\nu(C)` proves (15). Taking `R=I_F-qA` and applying (7) on `D` gives

\[
\nu(C)\|I_F-qA\|
\le
\|q\|\Lambda_{S,s,y_0}(A),
\tag{24}
\]

which is (8).

For the dual expression, set

\[
K:=\overline{\operatorname{aco}}D.
\tag{25}
\]

Since `K` is closed, convex, balanced, and contained in `B_F`, Hahn--Banach separation gives

\[
\sup\{\nu:\nu B_F\subseteq K\}
=
\inf_{\|\phi\|=1}\sup_{x\in K}|\phi(x)|.
\tag{26}
\]

Absolute convexification does not change the last supremum, yielding (6). It also shows directly that no constant larger than `\nu(C)` can satisfy (15) for every scalar functional.

### Neumann inversion supplies the global split

Under (9), equation (8) gives

\[
\|I_F-qA\|<1.
\tag{27}
\]

Therefore the classical Neumann series makes `qA` invertible and (10) satisfies

\[
qV=qA(qA)^{-1}=I_F.
\tag{28}
\]

Conversely, if `q` does not split, AF-085's elementary approximate-right-inverse dichotomy gives

\[
\|I_F-qA\|\ge1
\qquad
\text{for every }A\in\mathcal L(F,E),
\tag{29}
\]

because any strict subunit defect would already be Neumann-correctable. Combining (24) and (29) proves (11).

### Totality and norming are genuinely different

If (12) holds and the local defect is zero, (7) says that the bounded linear operator

\[
R:=I_F-qA
\tag{30}
\]

vanishes on `C`. It therefore vanishes on the algebraic span of `C` and, by continuity, on its closed span `F`. This proves (14) without requiring `\nu(C)>0`.

By contrast, `\nu(C)>0` says much more than totality: the balanced convex hull of the unit tangent directions contains a whole ambient ball. It is precisely this uniform geometric coverage that converts a small directional residual into a small operator norm.

## Exact controls

### Open-domain control: AF-085 is recovered exactly

If `S` contains an open neighborhood of `y_0`, then every `v\in F` is a contingent direction and

\[
C=F.
\tag{31}
\]

Thus

\[
\overline{\operatorname{aco}}(C\cap B_F)=B_F,
\qquad
\nu(C)=1.
\tag{32}
\]

Equations (8)--(11) reduce exactly to AF-085's threshold `1/\|q\|`. The open-domain theorem is therefore the maximal-direction endpoint of the present classification.

### One-sided half-space boundary: losing one sign of a direction loses nothing linearly

Let `0\ne\phi\in F^*` and suppose locally at `y_0` the admissible set has tangent cone

\[
C=\{v\in F:\operatorname{Re}\phi(v)\ge0\}
\tag{33}
\]

(with `\phi(v)\ge0` in the real case). For every `x\in B_F`, either `x\in C` or `-x\in C`. Since the hull in (5) is balanced,

\[
\overline{\operatorname{aco}}(C\cap B_F)=B_F,
\qquad
\nu(C)=1.
\tag{34}
\]

Hence the full AF-085 first-order splitting threshold survives at a smooth one-sided boundary. **Interiority is not the invariant:** because the tested model is linear, access to either sign of each ambient direction is enough after absolute convexification.

### Thin finite-dimensional slice: perfect local fidelity can coexist with global nonsplitting

Let `W\subsetneq F` be finite-dimensional and let

\[
S=y_0+W.
\tag{35}
\]

Then

\[
C=W,
\qquad
\nu(C)=0.
\tag{36}
\]

This is not merely a failure of the proof. Even if `q` is globally nonsplitting, choose `e_0\in E` with `qe_0=y_0`. A linear lift

\[
L:W\to E,
\qquad
qL=I_W,
\tag{37}
\]

exists by choosing preimages of a basis of `W`. Since every finite-dimensional subspace of a Banach space is complemented, choose a bounded projection `P:F\to W` and define

\[
A:=LP\in\mathcal L(F,E),
\qquad
s(y_0+w):=e_0+Lw.
\tag{38}
\]

Then `s` is a section on `S` and

\[
\Lambda_{S,s,y_0}(A)=0,
\tag{39}
\]

although `q` has no global bounded linear right inverse. A restricted domain that fails even the totality gate can therefore make a nonsplitting quotient look perfectly linearly repairable.

### Total but nonnorming directions: exact fidelity without robust margin

Take

\[
F=\ell^2
\tag{40}
\]

and let `C` be the union of the nonnegative rays through the standard basis vectors:

\[
C=\bigcup_{n\ge1}\{t e_n:t\ge0\}.
\tag{41}
\]

For example, `C` is the contingent tangent cone at `0` of the set on the right-hand side itself. Its closed linear span is all of `\ell^2`, so zero defect against a bounded linear `A` still forces `qA=I` by (12)--(14).

However `\nu(C)=0`. For each `N`, let

\[
\phi_N(x)
=
\frac1{\sqrt N}\sum_{n=1}^N x_n.
\tag{42}
\]

Then `\|\phi_N\|=1` while

\[
\sup_{v\in C\cap B_{\ell^2}}|\phi_N(v)|
=
\frac1{\sqrt N}
\longrightarrow0.
\tag{43}
\]

By (6), the norming modulus vanishes. Thus a direction family can be algebraically complete enough to certify an exact identity yet become arbitrarily insensitive to norm-one ambient functionals. This is the clean separation between **exact structural fidelity** and **stable structural fidelity** promised by the mandate.

## Prior art and novelty assessment

All mathematical ingredients behind the theorem are classical, and no novelty is claimed for contingent tangent cones, norming sets, Hahn--Banach separation, absolutely convex hulls, or Neumann inversion.

- Jean-Pierre Aubin and Hélène Frankowska, ***Set-Valued Analysis***, Modern Birkhäuser Classics, Birkhäuser (2009 reprint), DOI `10.1007/978-0-8176-4848-0`. Role: standard set-valued/variational-analysis source with a dedicated tangent-cone theory and derivative framework; this is the primary language for (4).
- J. M. Borwein, **“Weak Tangent Cones and Optimization in a Banach Space,”** *SIAM Journal on Control and Optimization* 16(3), 512--522 (1978), DOI `10.1137/0316034`. Role: direct Banach-space prior art for tangent-cone notions and their use in first-order analysis.
- R. Tyrrell Rockafellar and Roger J.-B. Wets, ***Variational Analysis***, Grundlehren der mathematischen Wissenschaften 317, Springer (1998), DOI `10.1007/978-3-642-02431-3`. Role: authoritative neighboring framework for variational geometry, set convergence, and first-order tangent constructions.
- Robert E. Megginson, ***An Introduction to Banach Space Theory***, Graduate Texts in Mathematics 183, Springer (1998), DOI `10.1007/978-1-4612-0603-3`. Role: standard Banach-space duality and Hahn--Banach background for the norming/absolutely-convex-hull equivalence used in (5)--(6).
- AF-085 supplies the immediately preceding open-domain quotient-repair theorem and its classical Neumann-series boundary.

A bounded literature audit found the expected mature tangent-cone, variational, Banach-duality, and approximate-inverse machinery, but did not justify treating the particular packaging (5)--(15) as a new literature theorem. The durable Arithmetic Fidelity contribution is therefore a **category-level synthesis and stopping rule**: once the domain of a proposed recovery mechanism is restricted by positivity, boundary conditions, feasible states, sampling, or another admissibility constraint, the relevant first-order question is whether its tangent directions are merely total or quantitatively norming. Those two levels determine respectively exact and robust propagation of the retained identity.

## Boundaries and failure modes

- `C` is the Bouligand/contingent cone for the norm topology. Replacing it by Clarke, weak, proximal, algebraic, or another tangent notion changes the available direction set and must be justified independently.
- The theorem tests approximation by a bounded **linear** ambient model `A:F\to E`. Nonlinear, Hölder, set-valued, order-constrained, or category-specific first-order models can behave differently.
- The modulus `\nu(C)` is intrinsic to the chosen norm on `F` and the declared tangent cone, not to the abstract set `S` under arbitrary renorming. Renorming can change quantitative robustness even when totality is preserved.
- Equation (15) is sharp as a universal operator estimate, but (11) need not be attained by a particular quotient or section. Do not call `\nu(C)/\|q\|` an attained sharp quotient defect without a separate extremizer.
- `\nu(C)=0` does not imply that every restricted-domain problem is uninformative. The total-but-nonnorming control shows the opposite: exact zero error can remain decisive. What disappears is a positive robustness margin derivable from tangent coverage alone.
- Conversely, `\nu(C)>0` concerns directional coverage only. It does not make a particular section canonical or prove that the retained directions are semantically relevant to an arithmetic discriminator.
- A one-sided boundary retains full linear directional coverage only because absolute convexification is legitimate for a linear residual. For positivity-preserving, cone-linear, monotone, or other asymmetric downstream categories, replacing the cone by its balanced hull may erase precisely the structure under study; such categories require their own fidelity modulus.
- No rational-prime or RH-specific conclusion follows from this Banach-space classification alone.

## Consequences for Arithmetic Fidelity

AF-085 identified openness as the condition allowing its local error estimate to test every ambient direction. AF-086 replaces that sufficient condition by the exact structural quantity that the proof actually needs. **A full neighborhood is only one way to obtain norming tangent coverage.** Smooth one-sided boundaries can retain the same first-order fidelity, while thin domains can hide a global nonsplitting obstruction completely.

More importantly, the result separates two notions that earlier compression arguments can easily conflate. The condition

\[
\overline{\operatorname{span}}C=F
\tag{44}
\]

is an exact-identifiability gate: zero residual on the admissible infinitesimal states determines the ambient linear identity. The stronger condition

\[
\nu(C)>0
\tag{45}
\]

is a stability gate: approximate agreement on admissible infinitesimal states controls approximate agreement everywhere and therefore crosses the Neumann splitting threshold once the error is small enough.

This supplies a reusable audit for later arithmetic compressions with constrained test families or admissible perturbations. Before concluding that a discriminator survives because all allowed local variations look correct, determine whether those variations are total and whether they are norming in the topology needed downstream. If they are neither, the test can be perfectly satisfied while the missing global structure remains invisible; if they are total but nonnorming, exact identities may transfer while quantitative estimates remain unstable; if they are norming, first-order approximation has a genuine ambient robustness margin.