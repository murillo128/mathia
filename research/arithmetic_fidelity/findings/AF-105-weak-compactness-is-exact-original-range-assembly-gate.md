# AF-105 — Weak compactness is the exact original-range assembly gate

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-WEAK-COMPACTNESS-MECHANISM`, `CATEGORY-EXPLICIT-FIDELITY`, `NO-NOVELTY-CLAIM`

## Claim

Let `X` and `K` be Banach spaces and let

\[
J_K:K\longrightarrow K^{**}
\]

be the canonical embedding. AF-100 studies bounded pointwise weak-star accessibility of

\[
U\in\mathcal L(X,K^{**})
\]

through nets `S_i\in\mathcal L(X,K)` satisfying

\[
\sup_i\|S_i\|<\infty,
\qquad
J_KS_i x\longrightarrow Ux
\quad\text{weak-star in }K^{**}
\quad(x\in X).
\tag{1}
\]

Bounded accessibility alone does not force `U` to take values in the original target `J_K(K)`: AF-102 already gives accessible bidual-valued maps with no genuine preadjoint. The missing assembly condition has an exact compactness form.

### 1. Pointwise weakly compact repair orbits force exact original-range recovery

Assume a net `(S_i)` satisfies (1) and, in addition, for every `x\in X` the repair orbit

\[
\{S_i x:i\}
\tag{2}
\]

is relatively weakly compact in `K`. Then there exists a unique

\[
S\in\mathcal L(X,K)
\]

such that

\[
\boxed{U=J_KS.}
\tag{3}
\]

Moreover

\[
S_i x\longrightarrow Sx
\quad\text{weakly in }K
\qquad(x\in X),
\tag{4}
\]

and

\[
\|S\|=\|U\|\le\sup_i\|S_i\|.
\tag{5}
\]

Thus the extra requirement is not merely another sufficient approximation estimate. It removes the bidual relaxation completely.

### 2. The induced orbit-compact accessibility gauge is exactly the original target category

Define

\[
a_K^{\rm orb}(U)
:=
\inf C,
\tag{6}
\]

where the infimum runs over all nets `(S_i)\subset\mathcal L(X,K)` such that

\[
\|S_i\|\le C,
\qquad
J_KS_i\to U\text{ pointwise weak-star},
\tag{7}
\]

and every orbit (2) is relatively weakly compact. As usual `\inf\varnothing=+\infty`.

Then

\[
\boxed{
a_K^{\rm orb}(U)=
\begin{cases}
\|S\|,&U=J_KS\text{ for some }S\in\mathcal L(X,K),\\
+\infty,&U(X)\not\subseteq J_K(K).
\end{cases}}
\tag{8}
\]

Consequently every bounded-accessible but genuinely bidual-valued `U` has the following unavoidable escape property:

\[
\boxed{
\text{for every bounded approximating net in (1), some source vector }x
\text{ has a repair orbit that is not relatively weakly compact.}
}
\tag{9}
\]

The distinction between `K` and `K^{**}` therefore cannot be hidden entirely in an abstract limiting operation. If the limit lies outside the original target, some pointwise family of local repairs must escape weak compactness.

### 3. Collective weak compactness recovers exactly the weakly compact operator ideal

Strengthen the requirement further by asking the entire family of repaired unit balls to be relatively weakly compact:

\[
\mathcal R:=\bigcup_i S_i(B_X)
\subset K.
\tag{10}
\]

Define `a_K^{\rm coll}(U)` by the same infimum as (6)--(7), now requiring `\mathcal R` to be relatively weakly compact. Then

\[
\boxed{
a_K^{\rm coll}(U)=
\begin{cases}
\|S\|,&U=J_KS\text{ with }S:X\to K\text{ weakly compact},\\
+\infty,&\text{otherwise}.
\end{cases}}
\tag{11}
\]

Thus the two compactness levels recover two exact categorical endpoints:

\[
\boxed{
\begin{array}{c}
\text{pointwise weak compactness of repair orbits}
\iff \text{assembly in the original target},\\[2mm]
\text{collective weak compactness of repaired unit balls}
\iff \text{assembly as a weakly compact operator}.
\end{array}}
\tag{12}
\]

For Arithmetic Fidelity this gives a clean refinement of AF-100--AF-104. Finite observability may be spoofed without any budget; bounded accessibility adds a uniform resource law; weak compactness of the repair family is a separate coherence gate that prevents the bounded approximants from escaping through the bidual boundary.

## Derivation

### 1. A relatively weakly compact orbit cannot acquire a new bidual limit

Fix `x\in X` and let

\[
W_x:=\overline{\{S_i x:i\}}^{\,w}\subset K.
\tag{13}
\]

By hypothesis `W_x` is weakly compact. The canonical embedding

\[
J_K:(K,w)\longrightarrow (J_KK,w^*)
\tag{14}
\]

is a homeomorphism onto its image. Hence `J_K(W_x)` is weak-star compact in the Hausdorff space `K^{**}`, and therefore weak-star closed.

Every term `J_KS_i x` lies in `J_K(W_x)`, while (1) says that this same net converges weak-star to `Ux`. Closedness gives

\[
Ux\in J_K(W_x)\subseteq J_K(K).
\tag{15}
\]

This holds for every `x`, so `U(X)\subseteq J_K(K)`. Define

\[
S:=J_K^{-1}U:X\to K.
\tag{16}
\]

Because `J_K` is an isometric linear embedding and `U` is bounded linear, `S` is bounded linear and

\[
\|S\|=\|U\|.
\tag{17}
\]

The uniform bound in (1) gives `\|U\|\le\sup_i\|S_i\|` by passing to the weak-star limit in each scalar pairing, proving (5).

Finally, after (3), equation (1) becomes

\[
J_KS_i x\to J_KSx
\quad\text{weak-star}.
\tag{18}
\]

On `J_K(K)`, the inherited weak-star topology is exactly the weak topology of `K`. Therefore (18) is precisely (4).

### 2. The orbit-compact gauge has no intermediate regime

If `U=J_KS`, the constant net

\[
S_i=S
\tag{19}
\]

satisfies (7), and every orbit is the singleton `{Sx}`. Hence

\[
a_K^{\rm orb}(J_KS)\le\|S\|.
\tag{20}
\]

Conversely any admissible net of radius `C` satisfies (5), so `\|S\|\le C`. Taking the infimum gives equality.

If `U` is not original-range valued, part 1 says that no admissible orbit-compact net exists at any finite radius. This proves (8) and the contrapositive escape statement (9).

### 3. Collective weak compactness identifies weakly compact assembled maps

Suppose (10) is relatively weakly compact and let

\[
W:=\overline{\mathcal R}^{\,w}.
\tag{21}
\]

Then `W` is weakly compact. Part 1 gives `U=J_KS` and pointwise weak convergence `S_i x\to Sx`. For every `x\in B_X`, all `S_i x` lie in `\mathcal R`, hence the weak limit `Sx` lies in `W`. Therefore

\[
S(B_X)\subseteq W,
\tag{22}
\]

so `S` is weakly compact.

Conversely, if `S:X\to K` is weakly compact, the constant net (19) has

\[
\bigcup_iS_i(B_X)=S(B_X),
\tag{23}
\]

which is relatively weakly compact. The same norm lower bound as above then gives (11).

## Exact controls and failure modes

### Reflexive target

If `K` is reflexive, every bounded subset of `K` is relatively weakly compact. Therefore every bounded AF-100 accessibility net automatically satisfies the pointwise orbit condition, and (8) collapses to the expected fact

\[
K^{**}=J_K(K).
\tag{24}
\]

The new gate is only informative when the target is genuinely nonreflexive.

### Goldstine control: boundedness alone is deliberately insufficient

Goldstine's theorem says that `J_K(B_K)` is weak-star dense in `B_{K^{**}}`. Thus for every

\[
z\in K^{**}\setminus J_K(K)
\tag{25}
\]

there is a norm-bounded net `(k_i)\subset K` with

\[
J_Kk_i\to z\quad\text{weak-star}.
\tag{26}
\]

Equation (8) forces every such approximating net to fail relative weak compactness. This is exactly where weak-star compactness and weak compactness diverge in a nonreflexive space.

### AF-102's finite-source non-preadjoint control

AF-102 takes a nonreflexive `L`, a point

\[
z\in L^{**}\setminus J_L(L),
\]

and `K=\mathbb F`, producing a dual-side operator whose transposed realization is

\[
U(\lambda)=\lambda z
\]

with finite accessibility cost equal to `\|z\|`. AF-105 shows what every such bounded realization must pay beyond that scalar norm budget: already at the single source vector `1`, any `L`-valued approximation of `z` has a non-relatively-weakly-compact orbit. Thus finite `\beta` does not solve original-range provenance; the missing information is visible as compactness escape.

### Reinov's AF-104 example lies one level earlier

AF-104 supplies an operator for which no bounded accessibility net exists at all. AF-105 addresses a different boundary. Even when a bounded net does exist, it cannot assemble to a genuinely bidual-valued limit while remaining pointwise weakly compact. The two obstructions should not be conflated:

\[
\text{uniform norm blow-up}
\quad\text{and}\quad
\text{weak-compactness escape}
\tag{27}
\]

are distinct ways a family of finite repairs can fail to become an original-category recovery.

### No canonicity or arithmetic specificity follows

Weak compactness is a categorical closure condition, not an arithmetic discriminator. Equation (8) says when a particular bidual relaxation returns to `K`; it does not explain why an RH construction should supply weakly compact repair orbits, nor does it distinguish rational primes from matched controls.

Accordingly an arithmetic application may use this theorem only after deriving the relevant compactness from intrinsic structure. Imposing weak compactness by hand after observing a bidual escape would merely encode the desired target category into the admissibility rule.

## Prior art and novelty assessment

The mathematical mechanism is classical Banach-space weak compactness. **No theorem-level novelty is claimed.** The key fact used above is the standard bidual characterization of relative weak compactness: a bounded subset of `K` is relatively weakly compact exactly when its weak-star closure in `K^{**}` stays inside the canonical copy of `K`. The operator-level analogue is Gantmacher's classical characterization of weakly compact operators by their bidual/adjoint behavior.

- Robert E. Megginson, ***An Introduction to Banach Space Theory***, Graduate Texts in Mathematics 183, Springer (1998), ISBN `0-387-98431-3`. Role: standard Banach-space source for weak compactness, canonical bidual embeddings, Goldstine's theorem, and Gantmacher's theorem.
- Oleg I. Reinov, **“Approximation of operators in dual spaces by adjoint operators,”** *Journal of Mathematical Sciences* 173(5), 632–642 (2011), DOI `10.1007/s10958-011-0263-4`. Role: direct prior art for the surrounding bounded-adjoint-approximation problem and the infinite-cost example translated in AF-104.
- E. Serrano, C. Piñeiro, and J. M. Delgado, **“Weakly equicompact sets of operators defined on Banach spaces,”** *Archiv der Mathematik* 86(3), 231–240 (2006), DOI `10.1007/s00013-005-1468-x`. Role: neighboring established literature on collectively weakly compact and weakly equicompact operator families; it confirms that compactness properties of whole operator families are a developed operator-theoretic subject rather than a new Arithmetic Fidelity notion.

A targeted prior-art search across weak compactness, bidual range criteria, collectively weakly compact operator families, adjoint approximation, local reflexivity, and tensor-norm accessibility did not reveal a need for a new Banach-space theorem here. The durable contribution is the exact translation into the line's compression language and the two-level classification (8)/(11), which closes a specific assembly question left open by AF-100--AF-104 without presenting the classical compactness mechanism as new mathematics.

## Consequences for Arithmetic Fidelity

The current Banach-space sequence now has a sharper stopping rule. A proposed repair should not be credited with original-category fidelity merely because every finite observation is reproducible or because one uniform operator-norm budget exists. If the relaxed target is a bidual, exact assembly back into the intended target requires a compactness/coherence mechanism that prevents the repair family from escaping through weak-star boundary points.

This produces the hierarchy

\[
\boxed{
\text{finite observational reproducibility}
\;<\;
\text{bounded accessibility}
\;<\;
\text{orbit-compact original-range assembly}
\;<\;
\text{collectively weakly compact operator assembly},
}
\tag{28}
\]

where the last two levels have the exact categorical meanings in (8) and (11). The inequalities are logical strengthening, not numerical inequalities between one common scalar gauge.

For later prime-specific applications, the useful question is therefore not simply whether a sequence of finite repairs converges. It is whether the arithmetic construction itself supplies a natural compactness principle for those repairs. If no such principle exists, a bidual or completion limit may preserve every declared finite observation while still leaving the intended arithmetic category.