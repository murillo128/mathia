# AF-107 — Collective compactness is the exact compact-operator assembly gate

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-COLLECTIVE-COMPACTNESS-MECHANISM`, `CATEGORY-EXPLICIT-FIDELITY`, `NO-NOVELTY-CLAIM`

## Claim

Let `X` and `K` be Banach spaces, let

\[
J_K:K\to K^{**}
\]

be the canonical embedding, and suppose a net

\[
S_i\in\mathcal L(X,K)
\]

satisfies

\[
J_KS_i x\longrightarrow Ux
\quad\text{weak-star in }K^{**}
\qquad(x\in X)
\tag{1}
\]

for some bounded linear

\[
U:X\to K^{**}.
\]

AF-105 showed that weak compactness of the repair orbits is the exact gate forcing the bidual-valued assembly back into the original target. AF-106 then separated WOT-closed stagewise constraints from stronger family-level coherence constraints. The compact-operator category has an exact version of that second phenomenon.

Write

\[
\mathcal R
:=
\bigcup_i S_i(B_X)
\subseteq K.
\tag{2}
\]

Then:

### 1. Collective norm compactness forces original-range, strong, compact assembly

If `\mathcal R` is relatively norm compact, then there is a unique

\[
S\in\mathcal L(X,K)
\]

such that

\[
\boxed{U=J_KS,}
\tag{3}
\]

and in fact

\[
\boxed{S_i x\to Sx\text{ in norm for every }x\in X.}
\tag{4}
\]

Moreover `S` is compact and

\[
\boxed{
\{S_i:i\}\cup\{S\}
\text{ is collectively compact.}
}
\tag{5}
\]

Thus a family-level norm-compactness condition does two things simultaneously: it upgrades the AF-105 weak assembly to strong-operator convergence and prevents the limit from leaving the compact-operator category.

### 2. Collective compactness is the exact compact-operator gate

Define the collective-compact accessibility cost

\[
a_K^{\rm cc}(U)
:=
\inf\Bigl\{
\sup_i\|S_i\|:
J_KS_i\to U\text{ pointwise weak-star and }
\bigcup_iS_i(B_X)\text{ is relatively norm compact}
\Bigr\},
\tag{6}
\]

with `\inf\varnothing=+\infty`.

Then

\[
\boxed{
a_K^{\rm cc}(U)=
\begin{cases}
\|S\|,
&U=J_KS\text{ for a compact }S:X\to K,\\[1mm]
+\infty,
&\text{otherwise}.
\end{cases}}
\tag{7}
\]

In particular, the finite value set of `a_K^{\rm cc}` is exactly the canonical copy of the compact-operator ideal inside `\mathcal L(X,K^{**})`.

Collective compactness already implies a uniform norm bound, so the explicit budget in (6) records the exact cost but is not an additional existence hypothesis.

### 3. Pointwise norm compactness is strictly weaker than collective compactness

If every individual orbit

\[
\{S_i x:i\}
\tag{8}
\]

is relatively norm compact, then (1) still forces (3) and upgrades the convergence to (4). But this does **not** force `S` to be compact.

Take

\[
X=K=\ell^2
\]

and let `P_n` be the coordinate truncations

\[
P_n(x_1,x_2,\ldots)
=(x_1,\ldots,x_n,0,0,\ldots).
\tag{9}
\]

Then every `P_n` has finite rank, hence is compact, and

\[
P_nx\to x
\quad\text{in norm for every }x\in\ell^2.
\tag{10}
\]

So every pointwise orbit is norm relatively compact and the assembled limit is

\[
S=I_{\ell^2}.
\tag{11}
\]

But `I_{\ell^2}` is not compact. Correspondingly,

\[
\bigcup_nP_n(B_{\ell^2})
\tag{12}
\]

is not relatively norm compact because it contains the orthonormal sequence `(e_n)`.

Therefore

\[
\boxed{
\text{compact at every stage}
+\text{ pointwise norm convergence}
\not\Rightarrow
\text{compact assembled operator}.
}
\tag{13}
\]

The missing datum is genuinely **collective** compactness across the whole repaired unit ball.

## Derivation

### 1. Collective compactness automatically supplies the boundedness required by AF-105

Assume `\mathcal R` in (2) is relatively norm compact. Its norm closure

\[
C:=\overline{\mathcal R}^{\|\cdot\|}
\tag{14}
\]

is compact, hence bounded. Therefore

\[
M:=\sup_{y\in\mathcal R}\|y\|<\infty.
\tag{15}
\]

For every `i`,

\[
\|S_i\|
=
\sup_{x\in B_X}\|S_ix\|
\le M,
\tag{16}
\]

so the family is uniformly bounded without an extra assumption.

For a fixed `x\ne0`,

\[
S_ix
=\|x\|S_i\!\left(\frac{x}{\|x\|}\right),
\tag{17}
\]

hence the orbit `(8)` lies in the relatively norm compact set `\|x\|\mathcal R`. It is therefore relatively weakly compact. AF-105 applies and yields the unique operator `S` satisfying (3), together with

\[
S_ix\to Sx
\quad\text{weakly in }K.
\tag{18}
\]

### 2. Compact range coherence upgrades weak convergence to norm convergence

For `x\in B_X`, every `S_ix` lies in the compact set `C`. Equation (18) shows that the same net converges weakly to `Sx`.

The norm topology on `C` is compact, while the weak topology restricted to `C` is Hausdorff and weaker. The identity map

\[
(C,\|\cdot\|)\to(C,w)
\tag{19}
\]

is therefore a continuous bijection from a compact space to a Hausdorff space, hence a homeomorphism. Consequently weak and norm convergence coincide for nets that remain in `C`.

First, weak closedness of the compact set `C` gives

\[
Sx\in C.
\tag{20}
\]

Then (18)--(19) give

\[
\|S_ix-Sx\|\to0
\qquad(x\in B_X).
\tag{21}
\]

Scaling proves (4) for arbitrary `x\in X`.

### 3. The assembled operator is compact and joins the same collectively compact family

Equation (20) holds for every `x\in B_X`, so

\[
S(B_X)\subseteq C.
\tag{22}
\]

Since `C` is norm compact, `S(B_X)` is relatively norm compact. Thus `S` is compact.

Moreover

\[
\left(\bigcup_iS_i(B_X)\right)\cup S(B_X)
\subseteq C,
\tag{23}
\]

so adjoining the limit preserves collective compactness, proving (5).

This is also exactly the classical strong-closure theorem for collectively compact families: Anselone--Palmer prove that the strong-operator closure of a collectively compact set of linear operators is collectively compact. Here the AF-105 assembly plus (14)--(21) shows why the weak-star/bidual formulation is forced into that classical strong-closure regime.

### 4. Exactness of the gauge

If `U=J_KS` for a compact operator `S`, take the constant net

\[
S_i=S.
\tag{24}
\]

Then

\[
\bigcup_iS_i(B_X)=S(B_X)
\tag{25}
\]

is relatively norm compact and the cost is `\|S\|`. Hence

\[
a_K^{\rm cc}(J_KS)\le\|S\|.
\tag{26}
\]

Conversely, every admissible family in (6) assembles by parts 1--3 to a compact `S` with `U=J_KS`, and pointwise weak-star lower semicontinuity of the norm gives

\[
\|S\|=\|U\|\le\sup_i\|S_i\|.
\tag{27}
\]

Taking the infimum proves (7).

### 5. The `\ell^2` projection control isolates the collective requirement

For (9),

\[
\|P_nx-x\|_2^2
=
\sum_{j>n}|x_j|^2\to0,
\tag{28}
\]

so the convergence is already strong. Each `P_n` is finite rank, and for each fixed `x`, the orbit is a norm-convergent sequence plus its limit.

Nevertheless `e_n\in P_n(B_{\ell^2})`, so (12) contains a sequence with pairwise distances

\[
\|e_n-e_m\|_2=\sqrt2
\qquad(n\ne m).
\tag{29}
\]

Hence (12) is not totally bounded and cannot have compact norm closure. The limit identity is correspondingly noncompact.

This example is especially useful because `\ell^2` is reflexive. The AF-105 weak-compactness gate is automatic for bounded families in this target, and `I_{\ell^2}` is weakly compact. The failure therefore occurs strictly one categorical level later: weak/original-range coherence survives, while norm-compact/compact-operator coherence does not.

## Exact controls and failure modes

### Per-operator compactness is not a closure constraint at the supplied topology

The class of compact operators is neither WOT-closed nor SOT-closed in general. The sequence `(P_n)` already converges SOT to a noncompact operator.

Thus AF-106's stagewise closure rule cannot rescue compactness by merely upgrading WOT assembly to SOT. What survives is the stronger **family property** of collective compactness. This is a coherence condition, not membership of each approximant in an operator ideal.

### Pointwise compactness and collective compactness carry different information

Requiring every orbit `(8)` to be norm precompact controls one source vector at a time and is enough to turn the weak assembly into strong convergence. It does not control the simultaneous image of the whole unit ball.

Collective compactness requires one common compact envelope for

\[
\{S_ix:\ i\text{ arbitrary},\ \|x\|\le1\},
\tag{30}
\]

which is exactly the missing cross-vector/cross-index coherence in the `\ell^2` control.

### Finite rank does not help unless ranks or ranges are coherently controlled

Every `P_n` is finite rank, but the available ranges exhaust larger and larger coordinate subspaces. No fixed compact set contains all repaired unit balls.

Therefore "every finite repair has finite rank" is not a meaningful compactness certificate for an infinite assembly unless some additional structure controls the union of those ranges, approximation numbers, or another equivalent compactness modulus.

### Compactness does not imply canonicity or arithmetic specificity

A compact assembled repair may still be nonunique, gauge-dependent, or reproducible by matched controls. AF-107 certifies only membership in the compact-operator category.

A prime-specific application must derive collective compactness from the arithmetic construction itself and still prove that the surviving compact operator carries a rational-prime discriminator. Imposing a compactness envelope by hand would merely bake the desired destination category into the admissibility rule.

## Prior art and novelty assessment

The mathematical mechanism is classical collectively compact operator theory. **No theorem-level novelty is claimed.**

- P. M. Anselone and T. W. Palmer, **“Collectively compact sets of linear operators,”** *Pacific Journal of Mathematics* 25(3), 417–422 (1968), DOI `10.2140/pjm.1968.25.417`. Role: direct primary prior art. Their Proposition 2.1(c) states that the strong-operator closure of a collectively compact family is collectively compact; the paper defines collective compactness exactly by relative compactness of the union of unit-ball images.
- Philip M. Anselone, ***Collectively Compact Operator Approximation Theory and Applications to Integral Equations***, Prentice-Hall, Englewood Cliffs, NJ (1971), ISBN `0-13-140673-6`. Role: classical monograph developing collectively compact approximation as a systematic framework for strong operator approximation and compact spectral problems.
- P. M. Anselone and R. H. Moore, **“Approximate solutions of integral and operator equations,”** *Journal of Mathematical Analysis and Applications* 9(2), 268–277 (1964), DOI `10.1016/0022-247X(64)90042-3`. Role: early collectively compact approximation context preceding the later abstract closure theory.

A targeted prior-art audit found that the operator-theoretic theorem needed here is already classical and stronger than any novelty claim based merely on "compact approximants remain compact under coherent convergence." The durable Arithmetic Fidelity result is the exact placement of that theorem in the AF-105/AF-106 assembly hierarchy: collective norm compactness is not just a convenient sufficient condition but precisely characterizes which bidual accessibility targets can be assembled as compact original-category operators at finite cost.

## Consequences for Arithmetic Fidelity

AF-105 and AF-107 now separate three distinct coherence levels for a weak-star assembly of finite repairs:

\[
\boxed{
\begin{array}{c}
\text{pointwise weakly compact orbits}
\Rightarrow
\text{original-range WOT assembly},\\[1mm]
\text{pointwise norm-compact orbits}
\Rightarrow
\text{original-range SOT assembly},\\[1mm]
\text{collectively norm-compact unit-ball images}
\Rightarrow
\text{compact SOT assembly}.
\end{array}}
\tag{31}
\]

The `\ell^2` projection control shows that the second implication cannot be strengthened to compactness of the assembled operator. Compactness requires coherence simultaneously over the approximation index and the source unit ball.

For later RH-facing constructions this gives a concrete audit rule. If a proposed spectral, resolvent, boundary-response, or smoothing mechanism is built from finite-rank or compact local repairs, **stagewise compactness is not evidence that the global object remains compact**. One must derive a collective compactness principle, or an equivalent quantitative compactness bound, from the intrinsic arithmetic/geometric structure before compactness of the assembled carrier can be credited.

This closes the first natural non-WOT-closed operator property singled out by AF-106 and sharpens the line's distinction between closure constraints and coherence constraints.