# AF-066 — Dual-face coherence classifies polyhedral first-order fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `(V,\|\cdot\|)` be a finite-dimensional real normed space, let `S\subset V` be nonempty and compact, fix `m\in V`, and put

\[
Q=S-m.
\tag{1}
\]

For a unit vector `u`, let

\[
J(u)=\{\varphi\in V^*: \|\varphi\|_*=1,\ \varphi(u)=1\}
=\partial\|\cdot\|(u)
\tag{2}
\]

be the exposed face of norming functionals at `u`. Define the **dual-face directional gap**

\[
\gamma_{S,m}(u)
=
\min_{v\in Q}\max_{\varphi\in J(u)}[-\varphi(v)].
\tag{3}
\]

Then:

1. **The exact first-order ray gap in an arbitrary norm is a min-max over the full norming face.** For every unit `u`,
   \[
   \boxed{
   \lim_{t\to\infty}
   \bigl(d(m+t u,S)-t\bigr)
   =\gamma_{S,m}(u).
   }
   \tag{4}
   \]
   Thus the nonsmooth analogue of AF-063 is not obtained by choosing one convenient norming functional. Every active functional in `J(u)` participates through the directional derivative of the norm.

2. **Nonpositive first-order gap is exactly a simultaneous-witness condition.** One has
   \[
   \boxed{
   \gamma_{S,m}(u)\le0
   \iff
   \exists s\in S\ \text{such that}\
   \varphi(s-m)\ge0
   \quad\forall\varphi\in J(u).
   }
   \tag{5}
   \]
   Call such an `s` a **dual-face coherent witness** for `(m,u)`. When `J(u)` is a singleton this reduces to the smooth support-functional test used in AF-063. When `J(u)` has positive dimension, different active functionals must be satisfied by one and the same target point; satisfying them only after taking different convex combinations is insufficient.

3. **Convex-hull membership need not imply first-order fidelity in a nonsmooth norm.** If `m\in\operatorname{conv}(S)`, then for every individual `\varphi\in J(u)` there exists some `s_\varphi\in S` with `\varphi(s_\varphi-m)\ge0`. But this point may depend on `\varphi`, while (5) requires one common witness for the entire face. Consequently
   \[
   m\in\operatorname{conv}(S)
   \not\Longrightarrow
   \gamma_{S,m}(u)\le0
   \tag{6}
   \]
   for nonsmooth norms. The gap is a genuine minimax/nonconvex-provenance obstruction: convexification can mix different target points to satisfy the face constraints, while point-to-set distance must choose one actual target point.

4. **A positive dual-face gap destroys every nonlinear powered safe lift.** For
   \[
   \Delta_{p,S}(m)
   =
   \sup_{x\in V}
   \left(d(x,S)^p-\|x-m\|^p\right),
   \qquad p>1,
   \tag{7}
   \]
   if `\gamma_{S,m}(u)>0` for some unit `u`, then
   \[
   \boxed{
   \Delta_{p,S}(m)=+\infty
   \qquad\forall p>1.
   }
   \tag{8}
   \]
   If `\gamma_{S,m}(u)<0`, that ray eventually contributes no positive distance excess. If `\gamma_{S,m}(u)=0`, first-order data tie and a finer contact analysis such as AF-065 may still be necessary.

5. **For polyhedral norms, dual-face coherence is the complete powered-fidelity classification.** Suppose the dual unit ball is a polytope and write its finite extreme set as
   \[
   A=\operatorname{ext}(B_*),
   \qquad
   \|x\|=\max_{a\in A}a(x).
   \tag{9}
   \]
   For a unit `u` put
   \[
   A(u)=\{a\in A:a(u)=1\}.
   \tag{10}
   \]
   Define the **dual-face coherence kernel**
   \[
   \mathcal C_S
   =
   \left\{
   m\in V:
   \forall\,\|u\|=1\ \exists s\in S\
   \text{with }a(s-m)\ge0\ \forall a\in A(u)
   \right\}.
   \tag{11}
   \]
   Then for every finite `p>1`,
   \[
   \boxed{
   \{m\in V:\Delta_{p,S}(m)<\infty\}
   =\mathcal C_S.
   }
   \tag{12}
   \]
   Moreover
   \[
   S\subseteq\mathcal C_S\subseteq\operatorname{conv}(S).
   \tag{13}
   \]
   Hence polyhedral source geometry admits no nontrivial finite critical exponent at infinity: once dual-face coherence passes, every finite power is bounded; once it fails, every power `p>1` diverges.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\begin{array}{c}
\text{smooth first-order fidelity sees one support functional and therefore convexifies the target;}\\
\text{nonsmooth first-order fidelity sees an entire dual face and can retain one-point provenance;}\\
\text{for polyhedral norms this face-coherence test already decides all finite powered lifts.}
\end{array}
}
\tag{14}
\]

This supplies the nonsmooth counterpart to AF-063--AF-065. Curved smooth norms can hide a hierarchy of higher-order contact exponents after the first-order gap vanishes. Polyhedral norms instead have finitely many linear support pieces, so the hierarchy terminates at a simultaneous first-order face constraint.

## Derivation

### Directional derivatives force the full norming face

For `\varepsilon>0` and `v\in V`, define

\[
g_\varepsilon(v)
=
\frac{\|u-\varepsilon v\|-1}{\varepsilon}.
\tag{15}
\]

The norm is a finite continuous convex function. Its directional derivative at `u` is the support function of its subdifferential:

\[
\lim_{\varepsilon\downarrow0}g_\varepsilon(v)
=
\max_{\varphi\in J(u)}[-\varphi(v)]
=:g(v).
\tag{16}
\]

For the present compact-target use, the convergence is uniform on `Q`. One can see this directly from duality. Let `B_*` be the dual unit ball. Then

\[
g_\varepsilon(v)
=
\max_{\psi\in B_*}
\left[
\frac{\psi(u)-1}{\varepsilon}-\psi(v)
\right].
\tag{17}
\]

The lower bound `g_\varepsilon(v)\ge g(v)` follows by restricting the maximum to `J(u)`. If uniform convergence failed on compact `Q`, choose `\varepsilon_n\downarrow0`, `v_n\to v\in Q`, and maximizing `\psi_n\in B_*` witnessing a fixed positive excess. Compactness gives a subsequence `\psi_n\to\psi`. Since `\psi_n(u)\le1`, any limit with `\psi(u)<1` would force the first term in (17) to `-\infty`, contradicting the bounded lower value supplied by `J(u)`. Hence `\psi\in J(u)`, and then

\[
\limsup_n g_{\varepsilon_n}(v_n)
\le-\psi(v)
\le g(v),
\tag{18}
\]

contradiction. Thus

\[
g_\varepsilon\to g
\quad\text{uniformly on }Q.
\tag{19}
\]

Now put `\varepsilon=1/t`. Positive homogeneity gives

\[
\begin{aligned}
d(m+t u,S)-t
&=
\min_{v\in Q}\bigl(\|t u-v\|-t\bigr)\\
&=
\min_{v\in Q}g_{1/t}(v).
\end{aligned}
\tag{20}
\]

Uniform convergence allows the minimum to pass to the limit, proving (4).

### The simultaneous-witness criterion

Because `Q` and `J(u)` are compact and the pairing is continuous, the minimum and maximum in (3) are attained. Therefore

\[
\gamma_{S,m}(u)\le0
\]

holds exactly when there exists `v=s-m\in Q` such that

\[
\max_{\varphi\in J(u)}[-\varphi(v)]\le0.
\tag{21}
\]

This is equivalent to

\[
\varphi(s-m)\ge0
\qquad\forall\varphi\in J(u),
\tag{22}
\]

which proves (5).

If `m\in\operatorname{conv}(S)`, then `0\in\operatorname{conv}(Q)`. For each fixed `\varphi`, linearity implies

\[
\max_{v\in Q}\varphi(v)\ge0.
\tag{23}
\]

But (23) allows its maximizing nonnegative witness to vary with `\varphi`. The order of quantifiers in (5) is stronger:

\[
\exists v\in Q\ \forall\varphi\in J(u).
\tag{24}
\]

This is precisely the information that convexification may erase. If the target itself is replaced by `K=\operatorname{conv}(S)` and `m\in K`, then the literal point `v=0\in K-m` is a simultaneous witness for every face. Thus the obstruction disappears under target convexification.

When the norm is smooth at `u`, `J(u)=\{\varphi_u\}` and (23) immediately supplies the required single witness. This recovers AF-063's fact that smooth first-order horofunction data depend only on the convex hull.

### Positive first-order gap amplifies every nonlinear power

If `\gamma_{S,m}(u)=c>0`, equation (4) yields, for large `t`,

\[
d(m+t u,S)-t\ge c/2.
\tag{25}
\]

Since `\|m+t u-m\|=t`, the positive distance excess stays bounded below along an escaping ray. AF-062 then gives (8). Equivalently, directly,

\[
(t+c/2)^p-t^p\to+\infty
\qquad(p>1).
\tag{26}
\]

If the gap is negative, equation (4) gives `d(m+t u,S)<t` eventually on that ray. Zero is the only first-order value at which a higher-order tail can remain relevant.

## Polyhedral classification

Assume now that `B_*` is a polytope with finite extreme set `A`. Classical polar duality gives the finite max representation (9). For a unit `u`, the extreme points of the norming face are precisely the active elements `A(u)`, and condition (5) is equivalent to the finite family in (11).

### Failure of coherence implies divergence for every `p>1`

If `m\notin\mathcal C_S`, choose a unit `u` for which no target point is a simultaneous witness. The continuous function

\[
s\mapsto
\max_{a\in A(u)}[-a(s-m)]
\tag{27}
\]

is then strictly positive on compact `S`; hence its minimum is some `c>0`. Since the convex hull of `A(u)` is `J(u)`, this minimum is exactly `\gamma_{S,m}(u)`. Equation (8) gives

\[
\Delta_{p,S}(m)=+\infty
\qquad\forall p>1.
\tag{28}
\]

### Coherence implies eventual domination outside a compact ball

Suppose `m\in\mathcal C_S`. We claim that there is `R<\infty` such that

\[
d(x,S)\le\|x-m\|
\qquad\text{whenever }\|x-m\|\ge R.
\tag{29}
\]

If not, choose `x_n=m+t_n u_n` with `t_n\to\infty`, `\|u_n\|=1`, and

\[
d(x_n,S)>t_n.
\tag{30}
\]

After a subsequence, compactness of the unit sphere gives `u_n\to u`, with `\|u\|=1`. By coherence choose `s\in S`, put `v=s-m`, and require

\[
a(v)\ge0
\qquad\forall a\in A(u).
\tag{31}
\]

For every `a\in A`, the finite-max formula gives

\[
\|t_nu_n-v\|-t_n
=
\max_{a\in A}
\left[t_n(a(u_n)-1)-a(v)\right].
\tag{32}
\]

If `a\in A(u)`, then `a(u_n)\le\|u_n\|=1` and (31) makes the bracket nonpositive. If `a\notin A(u)`, then `a(u)<1`; because `A` is finite, continuity gives a fixed negative gap from `1` for all sufficiently large `n`, and the term `t_n(a(u_n)-1)` dominates the bounded `-a(v)`. Thus every bracket in (32) is nonpositive for all sufficiently large `n`, so

\[
\|x_n-s\|\le t_n.
\tag{33}
\]

This contradicts (30), proving (29).

For every finite `p>1`, the powered defect is therefore nonpositive outside the compact ball `\overline B(m,R)`. On that ball the defect is continuous and bounded above, so

\[
\Delta_{p,S}(m)<\infty.
\tag{34}
\]

Together with the failure direction this proves (12).

### The coherence kernel lies between the target and its convex hull

If `m\in S`, choose `s=m` in (11), giving `a(s-m)=0` for every active functional. Thus

\[
S\subseteq\mathcal C_S.
\tag{35}
\]

If `m\notin K=\operatorname{conv}(S)`, strict separation gives a nonzero functional `\varphi` with

\[
\varphi(s-m)<0
\qquad\forall s\in S.
\tag{36}
\]

Normalize `\|\varphi\|_*=1` and choose a unit `u` with `\varphi(u)=1`. Then `\varphi\in J(u)`, so no target point can satisfy the simultaneous-witness condition (5). Hence `m\notin\mathcal C_S`, proving

\[
\mathcal C_S\subseteq K.
\tag{37}
\]

This also shows exactly where the polyhedral classification can differ from the smooth convex-hull classification: only inside `K`, where nonsmooth face coherence may still remember that `S` is not its convexification.

## Exact controls

### `\ell^\infty` keeps nonconvex provenance at first order

Take

\[
V=\mathbb R^2,
\qquad
\|(x,y)\|_\infty=\max(|x|,|y|),
\tag{38}
\]

with

\[
S=\{(1,-1),(-1,1)\},
\qquad
m=(0,0).
\tag{39}
\]

Then `m\in\operatorname{conv}(S)`. Along the unit direction

\[
u=(1,1),
\tag{40}
\]

one has

\[
J(u)=\operatorname{conv}\{e_1^*,e_2^*\}.
\tag{41}
\]

For `s=(1,-1)`, the second active functional is negative on `s-m`; for `s=(-1,1)`, the first is negative. Thus there is no simultaneous witness and

\[
\gamma_{S,0}(u)=1.
\tag{42}
\]

Indeed the geometry is exact for every `t\ge1`:

\[
d((t,t),S)=t+1,
\qquad
\|(t,t)\|_\infty=t.
\tag{43}
\]

Therefore every `p>1` diverges even though the base point belongs to the convex hull. If `S` is replaced by its segment `K=\operatorname{conv}(S)`, the point `m` itself belongs to the target, so the powered defect is identically zero. The first-order distinction is exactly one-point provenance versus a convex mixture.

### Smooth norms remove the face-coherence obstruction

If the norm is smooth, every `J(u)` is a singleton. For `m\in K`, equation (23) supplies a target point satisfying that one functional, so `\gamma(u)\le0` in every direction. AF-063 then refines this to signed convex-hull distance under its smooth/strictly-convex hypotheses. The new obstruction therefore comes from a nonsingleton dual face, not merely from replacing one coordinate formula by another.

### Polyhedral flatness terminates the critical-exponent hierarchy

AF-065 exhibits smooth/curved zero-gap rays where a local support-contact profile can decay as `\varepsilon^r`, producing a finite critical exponent `r`. In a polyhedral norm, by contrast, the norm is a maximum of finitely many linear forms. The compactness argument above shows that once all active face constraints have a common target witness, distance is eventually no larger than the base distance in every escaping direction. There is no residual polynomial positive tail left to amplify. Thus any claimed finite `r>1` phase transition in this exact polyhedral setting must come from changing the observable, the source/target model, or another assumption rather than from the AF-057 far-field mechanism itself.

## Prior art and novelty assessment

All convex-analytic and polyhedral ingredients used here are classical.

- R. Tyrrell Rockafellar, ***Convex Analysis***, Princeton University Press (1970). Role: standard convex directional-derivative/subdifferential theory; for a finite continuous convex function the directional derivative is the support function of the subdifferential, giving the classical mechanism behind (16).
- Cormac Walsh, **“The horofunction boundary of finite-dimensional normed spaces,”** *Mathematical Proceedings of the Cambridge Philosophical Society* 142(3), 497–507 (2007). DOI `10.1017/S0305004107000096`. Role: primary finite-dimensional normed-space horofunction prior art; the general boundary is controlled by extreme sets/faces of the dual unit ball rather than only the singleton functionals present in smooth norms.
- Corina Ciobotaru, Linus Kramer, and Petra Schwer, **“Polyhedral compactifications, I,”** *Advances in Geometry* 23(3), 413–436 (2023). DOI `10.1515/advgeom-2023-0018`, arXiv:`2002.12422`. Role: explicit polyhedral horofunction compactifications with strata indexed by dual faces, confirming that face-valued first-order data are intrinsic to polyhedral geometry.
- Derek Kitson, **“Finite and Infinitesimal Rigidity with Polyhedral Norms,”** *Discrete & Computational Geometry* 54, 390–411 (2015). DOI `10.1007/s00454-015-9706-x`. Role: clean published formulation of polar duality for a polyhedral unit ball and the finite extreme-functional representation `\|x\|=\max_{a\in\operatorname{ext}(B_*)}a(x)` used in (9) and the global sufficiency proof.

No novelty is claimed for subdifferentials, directional derivatives, dual faces, polyhedral norm formulas, or horofunction compactifications. A targeted literature audit found mature theories for each of those ingredients. It did not supply a basis for claiming the target-dependent quantity (3), the simultaneous-target witness criterion (5), or the exact powered-safe-lift kernel (12) as an established named theory; accordingly no broad novelty claim is made. The durable Arithmetic Fidelity contribution is the exact synthesis and falsification rule: nonsmoothness changes the first-order quantifiers from one support functional to a whole dual face, and in the polyhedral category that one-point coherence condition is already equivalent to finiteness of every powered AF-057 lift.

## Boundaries and failure modes

- Finite dimensionality and compactness of `S` are used essentially for attainment, compactness of the unit sphere/dual ball, and uniform passage from directional derivatives to the target minimum. No infinite-dimensional analogue is claimed.
- Equation (4) is a **fixed-ray first-order statement** for an arbitrary norm. It does not assert that every horofunction boundary point is a radial Busemann point, nor does it classify arbitrary nonradial escaping sequences outside the polyhedral argument.
- The complete equivalence (12) uses the finite extreme-functional representation of a polyhedral norm. It must not be extrapolated to smooth or general nonpolyhedral norms; AF-061, AF-064, and AF-065 explicitly show higher-order zero-gap behavior in those categories.
- `\gamma=0` is not full fidelity in a general norm. It only says that the declared ray has no positive first-order gap. Higher-order support contact, moving directions, or other retained structure may still decide the downstream observable.
- `\mathcal C_S` depends on the chosen norm/representation as well as on `S`. Smoothing a polyhedral unit ball can collapse a dual face to a single norming functional and thereby change the first-order fidelity kernel. This representation dependence is evidence about the compression, not an intrinsic property of the bare target.
- Convexifying `S` removes the face-coherence obstruction whenever `m` lies in the convexified target. Therefore the result must not be misread as a new convex-hull theorem; it identifies exactly why an actual nonconvex target can retain provenance that its convexification loses.
- Nothing in this result distinguishes rational primes or implies a statement about RH. It is an abstract compression theorem in the sense required by the Arithmetic Fidelity mandate.

## Consequence for the Arithmetic Fidelity frontier

AF-063 showed that in smooth normed geometry the first-order horofunction layer collapses a compact target to its convex hull. AF-065 then showed that zero first-order gaps can retain higher-order local support contact. The present finding identifies the missing nonsmooth branch: a nonsingleton norming face can already retain nonconvex one-point provenance **at first order**, because all active support constraints must be witnessed by the same target point.

This separates two distinct escape mechanisms that should not be conflated in later compression audits. Curved representations can lose provenance at first order and recover distinctions only through higher-order contact; polyhedral representations can retain provenance through dual-face coherence before any higher-order scale is reached. Any representation-invariance claim about structural fidelity therefore has to control not only contact exponents but also the dimension and combinatorics of the relevant norming faces.