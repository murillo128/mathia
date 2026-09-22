# AF-492 — Closed convex nuisance differences factor into a recession quotient and bounded residual body

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `CONVEX-NUISANCE`, `RECESSION-QUOTIENT`, `MINIMAX-RESOLUTION`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-490 treats an unrestricted linear nuisance: directions lying in the nuisance subspace are permanently quotiented out. AF-491 treats a compact nuisance set: every nonzero discriminator ray eventually escapes the bounded nuisance difference set. A closed convex symmetric nuisance difference has an exact decomposition interpolating between those regimes.

Let `Y` be a finite-dimensional normed real vector space and let

\[
C\subset Y
\]

be nonempty, closed, convex, symmetric, and contain `0`. Interpret `C` as the admissible pairwise nuisance-difference set; when an underlying nuisance family `K` satisfies `K-K=C`, two target states separated by `delta` are confusable up to radius-`rho` noise exactly when

\[
\operatorname{dist}(\delta s,C)\le 2\rho.
\]

Let

\[
V:=\operatorname{rec}(C)
\]

be the recession cone. Symmetry forces `V` to be a linear subspace. Let

\[
q:Y\to Y/V
\]

be the quotient map with quotient norm, and put

\[
B:=q(C).
\]

Then

1. `C+V=C` and therefore `C=q^{-1}(B)`;
2. `B` is closed, convex, symmetric, and bounded, hence compact;
3. for every `x in Y`,

\[
\boxed{
\operatorname{dist}_Y(x,C)
=
\operatorname{dist}_{Y/V}(q(x),B).}
\]

Thus a closed convex symmetric nuisance difference is exactly a **cylinder over a compact residual body in the quotient by its recession subspace**. The unbounded part is not an additional finite-scale complication: it is removed once and for all by quotienting `V`; all remaining nuisance geometry is bounded.

For a discriminator direction `s`, define

\[
d_C(\delta;s):=\operatorname{dist}(\delta s,C),
\qquad \delta\ge0,
\]

and write

\[
a:=\|q(s)\|_{Y/V}=\operatorname{dist}(s,V),
\qquad
R_B:=\max_{b\in B}\|b\|_{Y/V}.
\]

Then

\[
\boxed{
\delta a-R_B
\le d_C(\delta;s)
\le \delta a.}
\]

Consequently:

- if `s in V`, then `d_C(delta;s)=0` for every `delta>=0`: the nuisance can absorb arbitrarily large displacement in that discriminator direction;
- if `s notin V`, then

\[
\boxed{
\lim_{\delta\to\infty}
\frac{d_C(\delta;s)}{\delta}
=
\operatorname{dist}(s,V).}
\]

So the asymptotic recovery slope is determined **only** by the quotient of the discriminator modulo the recession directions. The compact body `B` controls finite-scale offsets and crossover, but cannot change the linear escape rate.

## Recession subspace and compact quotient body

For a closed convex set, use the recession cone

\[
\operatorname{rec}(C)
=
\{v:c+t v\in C\text{ for every }c\in C,\ t\ge0\}.
\]

Because `C=-C`, if `v in rec(C)` then `-v in rec(C)`. A recession cone is a convex cone, so symmetry makes `V=rec(C)` a linear subspace.

For every `v in V`, recession gives `C+v subset C`; applying the same statement to `-v` gives the reverse inclusion. Hence

\[
C+V=C.
\]

Therefore `C` is saturated along quotient fibers and

\[
C=q^{-1}(q(C))=q^{-1}(B).
\]

This immediately makes `B` convex and symmetric. It is also closed: the quotient topology satisfies that a set `A subset Y/V` is closed exactly when `q^{-1}(A)` is closed, and here `q^{-1}(B)=C`.

It remains to prove boundedness. Suppose `B` were unbounded. In finite dimension, a nonempty closed convex unbounded set has a nonzero recession direction; choose

\[
0\ne \bar d\in\operatorname{rec}(B)
\]

and a lift `d in Y` with `q(d)=bar d`. For every `c in C` and `t>=0`,

\[
q(c)+t\bar d\in B.
\]

Thus there exists `c_t in C` with

\[
q(c_t)=q(c+t d).
\]

The difference `c+t d-c_t` lies in `V`. Since `C+V=C`, this implies `c+t d in C`. Therefore `d in rec(C)=V`, contradicting `q(d)=bar d !=0`. Hence `B` is bounded; finite-dimensional closedness then makes it compact.

This proves the exact geometric decomposition

\[
\boxed{C=q^{-1}(B),\qquad B\subset Y/V\text{ compact, convex, symmetric}.}
\]

## Exact distance reduction

The quotient norm is

\[
\|q(y)\|_{Y/V}
=
\operatorname{dist}(y,V).
\]

Using the `V`-saturation of `C`,

\[
\begin{aligned}
\operatorname{dist}_{Y/V}(q(x),B)
&=
\inf_{c\in C}\|q(x-c)\|_{Y/V}\\
&=
\inf_{c\in C}\inf_{v\in V}\|x-c-v\|\\
&=
\operatorname{dist}_Y(x,C+V)\\
&=
\operatorname{dist}_Y(x,C).
\end{aligned}
\]

Applying this to `x=delta s` gives the exact reduction

\[
\boxed{
d_C(\delta;s)
=
\operatorname{dist}_{Y/V}(\delta q(s),B).}
\]

This is stronger than merely knowing the recession cone. It says every finite-noise ambiguity calculation for this convex nuisance class can be performed entirely in the quotient, where the residual nuisance is compact.

## Asymptotic escape law

Because `0 in B`,

\[
d_C(\delta;s)
\le
\|\delta q(s)\|
=
\delta a.
\]

For every `b in B`, the reverse triangle inequality gives

\[
\|\delta q(s)-b\|
\ge
\delta a-\|b\|
\ge
\delta a-R_B.
\]

Taking the infimum over `b` yields

\[
\delta a-R_B
\le
 d_C(\delta;s)
\le
\delta a.
\]

If `a>0`, division by `delta` and `delta->infinity` gives

\[
\frac{d_C(\delta;s)}{\delta}\to a.
\]

If `a=0`, then `s in V`. Since `0 in C` and `s` is a recession direction,

\[
\delta s\in C
\qquad(\delta\ge0),
\]

so `d_C(delta;s)=0` identically.

The correct asymptotic dichotomy is therefore not **bounded nuisance versus unbounded nuisance**. It is:

- recession component: permanently invisible after quotienting;
- transverse component: eventually escapes at linear speed `dist(s,V)`;
- compact quotient body: controls only the finite-scale delay before that asymptotic regime dominates.

## Consequence for deterministic ambiguity

Define the largest displacement hidden by radius-`rho` pairwise noise as

\[
\Delta_C(\rho;s)
:=
\sup\{\delta\ge0:d_C(\delta;s)\le2\rho\}.
\]

When `a>0`, the previous bounds imply

\[
\boxed{
\frac{2\rho}{a}
\le
\Delta_C(\rho;s)
\le
\frac{R_B+2\rho}{a}.}
\]

Indeed, `d_C(delta;s)<=delta a` makes `delta=2rho/a` admissible, while `d_C(delta;s)>=delta a-R_B` prevents any admissible `delta` from exceeding `(R_B+2rho)/a`.

Whenever `C=K-K` for the actual nuisance family and the AF-491 two-point ambiguity argument applies, the deterministic minimax radius is

\[
R^*=\frac12\Delta_C(\rho;s),
\]

hence

\[
\boxed{
\frac{\rho}{\operatorname{dist}(s,V)}
\le
R^*
\le
\frac{R_B+2\rho}
{2\operatorname{dist}(s,V)}.}
\]

Two previous regimes become exact endpoints of the same decomposition.

If `C=V` is a linear subspace, then `B={0}` and the bounds collapse to

\[
R^*=\frac{\rho}{\operatorname{dist}(s,V)},
\]

which is AF-490.

If `C` is bounded, then `V={0}` and no direction is permanently quotiented out. The exact finite-scale law is the AF-491 difference-set profile itself; the present result only adds that every nonzero ray must eventually escape linearly.

Thus the structured convex interpolation is

\[
\text{nuisance difference }C
\quad\longrightarrow\quad
\text{quotient by }\operatorname{rec}(C)
\quad\longrightarrow\quad
\text{compact residual body }B.
\]

The first step determines what is lost forever. The second determines how much finite excursion can still be hidden.

## Compression interpretation

A useful fidelity audit for convex nuisance is therefore two-stage.

First remove all directions along which the nuisance can move without bound. Those directions define a genuine quotient and no increase in observation depth can recover discriminator components lying inside them.

Then analyze the bounded residual body in the quotient. That body can delay separation, alter finite-noise constants, and create crossover behavior like AF-491's capped-amplitude example, but it cannot erase a transverse discriminator indefinitely.

This prevents a common modeling mistake. Replacing a structured unbounded nuisance family by its full linear span can enlarge the recession geometry and falsely erase directions that the true nuisance can traverse only finitely. Conversely, treating an unbounded nuisance as merely a large bounded error can miss an exact quotient direction that remains invisible at every scale.

The invariant object is the pair

\[
\bigl(\operatorname{rec}(C),\ q(C)\bigr),
\]

not the coarse label “bounded” or “unbounded.”

## Falsification and boundary audit

- The theorem is finite-dimensional. The compactness conclusion for `B` and the use of nonzero recession directions for unbounded closed convex sets are not asserted here in arbitrary infinite-dimensional normed spaces.
- Closedness, convexity, and symmetry of `C` are substantive. For a nonconvex unbounded difference set, sparse arms or disconnected escape channels need not reduce to a recession subspace plus compact quotient body; the raw profile `dist(delta s,C)` remains the safe object.
- For an underlying nuisance set `K`, the algebraic difference `K-K` need not be closed even when `K` itself is closed and convex. Replacing it by `cl(K-K)` preserves positive-noise distance calculations but may turn an unattained zero-noise limit into an exact-looking collision. Exact zero-noise identifiability must therefore use the actual difference set or prove it closed.
- `R_B` gives only coarse finite-scale bounds. The exact ambiguity radius depends on the full shape of the compact quotient body `B`, not only on its radius.
- If the nuisance geometry changes with the observation scale, one must track the family `C_t`, its recession spaces, and its quotient bodies. This theorem is pointwise in the declared nuisance geometry and does not supply uniformity automatically.
- The result concerns target recovery under structured nuisance. It does not establish arithmetic provenance, distinguish rational primes from generalized-prime controls, or provide evidence for RH by itself.

## Prior-art and novelty audit

The convex-analysis backbone is classical. No broad novelty is claimed for recession cones, lineality, quotient norms, or the fact that unboundedness of finite-dimensional closed convex sets is detected by recession directions.

- R. Tyrrell Rockafellar, ***Convex Analysis***, Princeton University Press (1970), especially the classical treatment of recession cones and unboundedness in Chapter 8. Role: foundational convex-analysis language for recession directions and lineality.
- R. Tyrrell Rockafellar and Roger J.-B. Wets, ***Variational Analysis***, Grundlehren der mathematischen Wissenschaften 317, Springer (1998), DOI `10.1007/978-3-642-02431-3`. Role: authoritative variational-geometry treatment of cones, horizon/recession behavior, quotients, and asymptotic set structure.
- Alfred Auslender and Marc Teboulle, ***Asymptotic Cones and Functions in Optimization and Variational Inequalities***, Springer Monographs in Mathematics, Springer (2003), DOI `10.1007/b97594`. Role: systematic finite-dimensional treatment of asymptotic sets/cones and unbounded convex behavior.

The durable Arithmetic Fidelity contribution is the specialization and composition with AF-490/AF-491: **first quotient by the nuisance recession subspace, then apply bounded difference-set fidelity in the quotient**. This identifies the exact object that survives between the two earlier endpoint theorems and prevents an unbounded structured nuisance from being conflated either with its full linear span or with a merely large bounded perturbation.

## Relationship to AF-490 and AF-491

AF-490 gives the homogeneous endpoint: an unrestricted nuisance subspace erases its directions exactly and permanently. AF-491 gives the bounded endpoint: a compact difference set can hide only finite excursion, after which raw depth reappears.

AF-492 shows that every **closed convex symmetric** nuisance difference decomposes into those two mechanisms. Its recession subspace is the permanent quotient; after passing to that quotient, the remaining nuisance body is compact and therefore behaves by AF-491-type finite-scale escape.

The resulting hierarchy is now explicit:

\[
\text{raw discriminator}
\longrightarrow
\text{quotient by recession directions}
\longrightarrow
\text{bounded residual escape profile}
\longrightarrow
\text{recoverable target resolution}.
\]

The unresolved Arithmetic Fidelity question is no longer whether generic convex nuisance is bounded or linear. It is which nuisance recession directions and compact residual geometry arise from the actual arithmetic source class, and whether the rational-prime discriminator has a quantitatively useful component transverse to them.