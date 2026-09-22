# AF-493 — Nonconvex nuisance asymptotics are controlled by horizon scaling, not recession translation

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `NONCONVEX-NUISANCE`, `HORIZON-CONE`, `MINIMAX-RESOLUTION`, `NEGATIVE/OBSTRUCTION`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-492 gives an exact recession-quotient decomposition for closed convex symmetric nuisance differences. Convexity is doing essential work there. For a general closed nonconvex nuisance-difference set, the translation directions along which the whole set can move forever can be much smaller than the directions that recur asymptotically at large scale.

Let `Y` be a finite-dimensional normed real vector space, let `C subset Y` be nonempty and closed with `0 in C`, and let `s in Y`. Define

\[
d_C(t;s):=\operatorname{dist}(t s,C),
\qquad
q_C(t;s):=\frac{d_C(t;s)}{t}
=\operatorname{dist}(s,t^{-1}C),
\qquad t>0.
\]

Define the horizon/scaling cone

\[
C^\infty
:=
\left\{h:\exists\ t_n\to\infty,\ c_n\in C,
\ \frac{c_n}{t_n}\to h\right\}.
\]

Equivalently, `C^infty` is the Painlevé-Kuratowski outer limit of the rescaled sets `t^{-1}C` as `t->infinity`. Then

\[
\boxed{
\liminf_{t\to\infty}
\frac{\operatorname{dist}(t s,C)}{t}
=
\operatorname{dist}(s,C^\infty).}
\]

Thus the correct first-order asymptotic fidelity test for an arbitrary closed nuisance geometry is **horizon membership**, not the convex translation-recession test.

In particular, because `C^infty` is closed:

- if `s notin C^infty`, then `dist(s,C^infty)>0`, so the discriminator escapes `C` at a uniformly positive linear rate for all sufficiently large `t`; every fixed noise radius therefore hides only a bounded target displacement;
- if `s in C^infty`, then the normalized separation has liminf zero, but this alone does **not** imply bounded-distance aliases or infinite fixed-noise ambiguity. One must return to the full profile `d_C(t;s)`.

The second point is the nonconvex obstruction. Horizon scaling records asymptotic direction after normalization; it forgets the absolute radial gaps that determine whether a fixed noise budget can actually bridge the nuisance set.

## Exact liminf theorem

Put

\[
\alpha:=\liminf_{t\to\infty}q_C(t;s).
\]

For every `h in C^infty`, choose `t_n->infinity` and `c_n in C` with `c_n/t_n -> h`. Then

\[
q_C(t_n;s)
\le
\left\|s-\frac{c_n}{t_n}\right\|
\longrightarrow
\|s-h\|.
\]

Since the liminf over all `t` is no larger than the liminf along this subsequence,

\[
\alpha\le\|s-h\|.
\]

Taking the infimum over `h in C^infty` gives

\[
\alpha\le\operatorname{dist}(s,C^\infty).
\]

For the reverse inequality, choose `t_n->infinity` with

\[
q_C(t_n;s)\to\alpha.
\]

For each `n`, choose `c_n in C` satisfying

\[
\left\|s-\frac{c_n}{t_n}\right\|
\le q_C(t_n;s)+\frac1n.
\]

Because `0 in C`,

\[
q_C(t;s)\le\|s\|
\]

for every `t`; hence the sequence `c_n/t_n` is bounded. Finite-dimensional compactness gives a convergent subsequence

\[
\frac{c_{n_k}}{t_{n_k}}\to h.
\]

By definition `h in C^infty`, and along this subsequence

\[
\alpha
=
\lim_k q_C(t_{n_k};s)
\ge
\lim_k
\left(\left\|s-\frac{c_{n_k}}{t_{n_k}}\right\|-\frac1{n_k}\right)
=
\|s-h\|
\ge
\operatorname{dist}(s,C^\infty).
\]

Therefore

\[
\boxed{
\alpha=\operatorname{dist}(s,C^\infty).}
\]

The proof uses only finite-dimensional compactness and the definition of the outer scaling limit. Convexity and symmetry are not required for the identity itself.

## Consequence for fixed-noise ambiguity

As in AF-491 and AF-492, define

\[
\Delta_C(\rho;s)
:=
\sup\{t\ge0:d_C(t;s)\le2\rho\}.
\]

Suppose

\[
a:=\operatorname{dist}(s,C^\infty)>0.
\]

The liminf theorem implies that for every `0<eta<a` there is `T_eta` such that

\[
d_C(t;s)\ge \eta t
\qquad(t\ge T_\eta).
\]

Hence no `t` larger than both `T_eta` and `2rho/eta` is admissible in the definition of `Delta_C`. Therefore

\[
\boxed{
s\notin C^\infty
\quad\Longrightarrow\quad
\Delta_C(\rho;s)<\infty
\quad\text{for every finite }\rho.}
\]

So exclusion from the horizon cone is a robust sufficient condition for eventual recoverability under any fixed deterministic noise budget.

The converse is false. Membership `s in C^infty` says only that there are arbitrarily large scales at which the distance is `o(t)`; that distance may still tend to infinity and eventually exceed every fixed noise radius.

## Why translation recession is insufficient outside convexity

For an arbitrary set define the strong translation-recession directions

\[
R_{\mathrm{tr}}(C)
:=
\{v:C+t v\subset C\text{ for every }t\ge0\}.
\]

For a closed convex set this is the usual recession cone, and the horizon cone agrees with it. This is exactly the regular regime used by AF-492.

Without convexity, however, `R_tr(C)` asks for a direction that can be translated from **every point at every magnitude**, whereas `C^infty` asks only whether that direction occurs along some unbounded normalized sequence. The latter can be vastly larger.

This distinction is decisive for arithmetic-fidelity style nuisance classes, because sparse or recurrent aliases need not form a translation-invariant arm.

## Discrete alias counterexample: `Z`

Take

\[
K=\mathbb Z\subset\mathbb R,
\qquad
C=K-K=\mathbb Z,
\qquad
s=1.
\]

The strong translation-recession set is trivial:

\[
R_{\mathrm{tr}}(\mathbb Z)=\{0\},
\]

because no nonzero real direction can be added with every real magnitude while remaining in `Z`.

But the horizon cone is all of `R`. For any `h in R`, take `t_n=n` and integers `c_n` nearest to `hn`; then

\[
\frac{c_n}{t_n}\to h.
\]

Thus

\[
C^\infty=\mathbb R.
\]

The raw separation profile makes the failure even sharper:

\[
\operatorname{dist}(t,\mathbb Z)\le\frac12,
\qquad
\frac{\operatorname{dist}(t,\mathbb Z)}{t}\to0.
\]

At every integer displacement `m`, the alias is exact:

\[
d_C(m;1)=0.
\]

Consequently

\[
\boxed{
\Delta_C(\rho;1)=\infty
\qquad\text{for every }\rho\ge0.}
\]

This is not merely an abstract set example: `C` is the exact difference set of the nuisance family `K=Z`. An estimator of an unrestricted real target in the channel `y=v-theta+u`, `v in Z`, cannot recover the absolute target because arbitrarily large integer shifts are absorbed exactly by the nuisance.

A recession-only audit would completely miss this loss: the translation-recession set is `{0}`, yet global fidelity is destroyed.

## Horizon membership does not by itself imply fixed-noise aliasing

The opposite caution is also necessary. Let

\[
C
=
\{0\}
\cup
\{\pm(n,\sqrt n):n\in\mathbb N\}
\subset\mathbb R^2,
\qquad
s=e_1.
\]

This is closed and symmetric. Its horizon cone contains the whole first-coordinate axis, so in particular `s in C^infty`: choosing `t_n=n` gives

\[
\frac{(n,\sqrt n)}{n}
\to e_1.
\]

Nevertheless the absolute distance along the discriminator ray diverges. For `t>=2`, any positive point `(n,sqrt n)` either has `n<t/2`, in which case the horizontal error exceeds `t/2`, or has `n>=t/2`, in which case the vertical error is at least `sqrt(t/2)`. Negative points are farther away. Hence

\[
\operatorname{dist}(t e_1,C)
\ge
\sqrt{t/2}
\qquad(t\ge2),
\]

up to the harmless comparison with the origin, and therefore

\[
d_C(t;e_1)\to\infty
\quad\text{while}\quad
\frac{d_C(t;e_1)}t\to0.
\]

So every fixed noise radius has finite ambiguity even though the normalized asymptotic slope vanishes.

The horizon cone therefore answers a **first-order scaling question**, not the full fixed-noise recovery question.

## Set-convergence interpretation

The identity

\[
q_C(t;s)=\operatorname{dist}(s,t^{-1}C)
\]

shows that nuisance asymptotics are naturally a set-convergence problem. The horizon cone is the Painlevé-Kuratowski outer limit of the rescaled sets. The theorem above says that this outer limit determines the liminf of the distance functions in finite dimension.

A full limit

\[
q_C(t;s)\to\operatorname{dist}(s,C^\infty)
\]

requires more than the existence of the outer limit. One sufficient language is Wijsman convergence of the scaled closed sets `t^{-1}C`, because Wijsman convergence is precisely pointwise convergence of distance functions. Sparse radial gaps can prevent such convergence even when the horizon cone is simple.

This yields a useful hierarchy for nonconvex nuisance:

\[
\text{translation recession}
\subseteq
\text{horizon/scaling directions}
\quad\text{plus}\quad
\text{radial recurrence profile}.
\]

The horizon cone determines whether linear-rate escape is unavoidable. The raw distance profile determines whether sublinear recurrence is still close enough to create fixed-noise aliases.

## Falsification and boundary audit

- The liminf identity is stated in finite dimension. The compact-subsequence step can fail in a general infinite-dimensional normed space without an additional compactness hypothesis.
- Closedness of `C` is natural for the set-convergence statement. For an underlying nuisance family `K`, `K-K` need not be closed. Positive-noise distances are unchanged by closure, but at exactly zero noise an unattained limit point is not an actual collision; exact identifiability must distinguish `K-K` from its closure.
- Horizon membership is not a sufficient criterion for infinite minimax ambiguity at fixed noise. The curved sparse example above shows that absolute distance can diverge sublinearly.
- Conversely, `s notin C^infty` is stronger than merely having no exact aliases: it forces eventually linear separation and therefore finite ambiguity at every fixed noise radius.
- `R_tr(C)` is introduced only to expose the failure of the convex recession intuition. Terminology for recession/asymptotic cones varies outside convex analysis; the operative definitions here are explicit.
- The `Z` example demonstrates a genuine difference-set failure mode, but it is not an arithmetic-prime result. It does not show that rational-prime nuisance classes possess the same recurrent aliases.
- Nothing here proves RH or supplies prime provenance. The result classifies which large-scale information a nonconvex nuisance compression can erase before any arithmetic specialization.

## Prior-art and novelty audit

The set-convergence backbone is classical, and no broad novelty is claimed for horizon cones, Painlevé-Kuratowski outer limits, or Wijsman convergence.

- R. Tyrrell Rockafellar and Roger J.-B. Wets, ***Variational Analysis***, Grundlehren der mathematischen Wissenschaften 317, Springer (1998), DOI `10.1007/978-3-642-02431-3`. Role: authoritative language for horizon cones, outer limits, and asymptotic variational geometry; in the convex case the horizon/recession notions collapse to the familiar recession geometry used in AF-492.
- Gerald Beer, ***Topologies on Closed and Closed Convex Sets***, Mathematics and Its Applications 268, Kluwer/Springer (1993), DOI `10.1007/978-94-015-8149-3`. Role: systematic reference for Wijsman, Attouch-Wets, and Painlevé-Kuratowski convergence and their formulation through distance functionals.
- R. A. Wijsman, **“Convergence of Sequences of Convex Sets, Cones and Functions. II,”** *Transactions of the American Mathematical Society* 123 (1966), 32–45. Role: classical distance-functional convergence background underlying the Wijsman viewpoint.

The durable Arithmetic Fidelity contribution is the specialization to the AF-490–AF-492 nuisance-fidelity chain: **convex recession geometry does not survive as a complete asymptotic diagnostic once the nuisance difference set becomes nonconvex**. The exact liminf law identifies the horizon cone as the correct first-order replacement, while the `Z` and sparse-curved examples prove that one must still retain radial recurrence information to decide fixed-noise recoverability.

## Relationship to AF-490–AF-492

AF-490 handles an unrestricted nuisance subspace: the hidden directions are an exact quotient. AF-491 handles compact nuisance: every nonzero discriminator ray eventually escapes. AF-492 interpolates exactly across all closed convex symmetric nuisance differences by quotienting their recession subspace and leaving a compact residual body.

AF-493 identifies the boundary of that interpolation. For nonconvex nuisance, there need not be a recession quotient plus compact body. Sparse large-scale pieces can recur in directions that are invisible to translation recession. The hierarchy becomes

\[
\text{convex nuisance}
\Rightarrow
\text{recession quotient + compact residual},
\]

whereas in the general closed nonconvex case one must use

\[
\text{horizon/scaling cone}
\quad+\quad
\text{full radial distance profile}.
\]

The unresolved Arithmetic Fidelity question is therefore sharper: when arithmetic source classes generate nonconvex nuisance differences, determine whether the rational-prime discriminator lies outside their horizon cones, and when it does not, whether the residual radial recurrence is strong enough to create bounded-distance aliases rather than merely sublinear separation.