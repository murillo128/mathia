# PC-405 — shell-2 cross-level cyclotomic refinement is one-measure dilation data

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for finite shell-2-interleaved Chen packets whose cross-level targets lie in one multiplicative descendant tree and are generated only by the canonical cyclotomic prime-child refinement law. This does not classify source-derived interactions that change the product law, angular/chord/old-new data coupled to radial refinement, nonlinear functionals that use special arithmetic properties of the cyclotomic base measure, or genuinely new infinite-level analytic limits.

PC-186 classified the **linear radial** prime-refinement directions and showed that they commute, while PC-404 classified arbitrary finite shell-2-interleaved multishell Chen packets once the target-shell measures are supplied separately. The natural gap between them is therefore precise: can one first use the actual cyclotomic child relation to create cross-level target shells and then feed those descendants into the nonlinear ordered Chen construction, thereby obtaining a carrier that is not already present in the parent shell?

The answer is no for this canonical construction. In the shell-2 coordinate the exact prime-child law acts on the parent measure by a universal pushforward semigroup. That semigroup is conjugate to ordinary dilation of logarithmic radius. Every multiplicative descendant measure is therefore a finite integral-linear combination of dilated copies of one base measure, and substituting those descendants into PC-404 turns every finite cross-level Chen packet into a universal ordered kernel integrated against tensor powers of that same one-shell measure. The construction retains the cyclotomic base profile, but it creates no additional source-derived interaction measure.

## 1. Shell-2 coordinates turn cyclotomic child refinement into a measure pushforward

For `n>1`, put

\[
X_n(r)=\log\Phi_n(r),\qquad
\tau(r)=X_2(r)=\log(1+r),\qquad
L=\log2,
\]

for `0<=r<=1`, and use the shell-2 flux measure from PC-399,

\[
\mu_n:=\tau_*(dX_n)
\quad\text{on }[0,L].
\tag{1}
\]

For every integer `a>=1`, define the increasing map

\[
h_a(t)
:=
\tau\!\left((\tau^{-1}(t))^{1/a}\right)
=
\log\!\left(1+(e^t-1)^{1/a}\right),
\tag{2}
\]

and let

\[
T_a\nu:=(h_a)_*\nu
\tag{3}
\]

for any finite signed measure `nu` on `[0,L]`.

The classical prime-child cyclotomic identities are

\[
\Phi_{pn}(r)=
\begin{cases}
\Phi_n(r^p)/\Phi_n(r),&p\nmid n,\\[2mm]
\Phi_n(r^p),&p\mid n.
\end{cases}
\tag{4}
\]

Taking logarithms and Stieltjes differentials gives

\[
dX_{pn}(r)=
\begin{cases}
dX_n(r^p)-dX_n(r),&p\nmid n,\\
dX_n(r^p),&p\mid n.
\end{cases}
\tag{5}
\]

The first term has an exact pushforward description. For every continuous test function `f`, set `y=r^p`. Then

\[
\begin{aligned}
\int_0^L f(t)\,d\bigl[\tau_*dX_n(r^p)\bigr](t)
&=\int_0^1 f(\tau(r))\,dX_n(r^p)\\
&=\int_0^1 f\!\left(\tau(y^{1/p})\right)dX_n(y)\\
&=\int_0^L f(h_p(t))\,d\mu_n(t)\\
&=\int_0^L f(t)\,d(T_p\mu_n)(t).
\end{aligned}
\tag{6}
\]

Hence the shell-2 measures themselves obey the exact child law

\[
\boxed{
\mu_{pn}=
\begin{cases}
(T_p-I)\mu_n,&p\nmid n,\\[1mm]
T_p\mu_n,&p\mid n.
\end{cases}}
\tag{7}
\]

This is stronger than merely comparing moments: the entire signed flux measure of the child is determined functorially by the parent.

As a consistency check, `T_p` preserves total mass. Equation (7) therefore reproduces the common-vertex identity `mu_n([0,L])=log Phi_n(1)=Lambda(n)`: adjoining a fresh prime gives zero mass, while repeating the existing prime of a prime power preserves `log p`.

## 2. The refinement semigroup is just logarithmic-radius dilation in disguise

The maps (2) satisfy

\[
h_a\circ h_b=h_{ab},
\qquad
T_aT_b=T_{ab}=T_bT_a.
\tag{8}
\]

There is an explicit conjugacy making this action elementary. On `(0,L]`, define

\[
\chi(t):=-\log(e^t-1).
\tag{9}
\]

Since `e^t-1` is the original radius, `chi` is simply logarithmic radius `-log r`. Directly from (2),

\[
\boxed{\chi(h_a(t))=\frac{\chi(t)}{a}.}
\tag{10}
\]

Thus the apparently nonlinear shell-2 refinement map is conjugate to the ordinary dilation `x -> x/a` on `[0,infinity)`; the endpoint `t=0` corresponds to `x=infinity`. The commutativity found for linear radial refinement in PC-186 therefore survives after changing to the shell-2 moment coordinate. No curvature or noncommutative ordering is created by this coordinate change.

This also places the abstract semigroup aspect squarely inside the cyclotomic refinement territory already classicalized in PC-010: the roots-of-unity multiplication/refinement action is not a new dynamical system. The project-specific point here is the exact intertwining with the shell-2 flux measures used by PC-399--PC-404.

## 3. Every multiplicative descendant is generated from one base measure

Let

\[
m=\prod_p p^{k_p}.
\]

Iterating (7) and using (8) gives an explicit operator `A_{n,m}` with

\[
\boxed{\mu_{nm}=A_{n,m}\mu_n,}
\tag{11}
\]

where

\[
A_{n,m}
=
\left(\prod_{\substack{p\mid n\\k_p>0}}T_{p^{k_p}}\right)
\left(\prod_{\substack{p\nmid n\\k_p>0}}
\bigl(T_{p^{k_p}}-T_{p^{k_p-1}}\bigr)\right).
\tag{12}
\]

Indeed, if `p|n` from the start, every multiplication by `p` contributes another `T_p`. If `p` is fresh, the first step contributes `T_p-I`, while each subsequent repetition contributes `T_p`, giving

\[
T_p^{k_p-1}(T_p-I)
=T_{p^{k_p}}-T_{p^{k_p-1}}.
\tag{13}
\]

All prime factors commute by (8), so no choice of refinement order remains.

In particular, every `A_{n,m}` is a finite integral-linear combination of universal pushforwards,

\[
A_{n,m}=\sum_{d\mid m} c_{n,m}(d)\,T_d,
\qquad c_{n,m}(d)\in\mathbb Z,
\tag{14}
\]

with the coefficients fixed entirely by the elementary fresh-prime/repeated-prime pattern. The child tree therefore contains no measure-valued datum independent of `mu_n`.

## 4. Substitution into PC-404 removes the apparent cross-level carrier

PC-404 gives, for an ordered target list `n_1,...,n_r` and nonnegative shell-2 gap multiplicities `k_0,...,k_r`,

\[
\left(\prod_{j=0}^{r}k_j!\right)
J_{2^{k_0},n_1,2^{k_1},\ldots,n_r,2^{k_r}}
=
\int_{0<t_1<\cdots<t_r<L}
P_{\mathbf k}(t_1,\ldots,t_r)
\prod_{j=1}^{r}d\mu_{n_j}(t_j),
\tag{15}
\]

where

\[
P_{\mathbf k}(\mathbf t)
=t_1^{k_0}
\prod_{j=1}^{r-1}(t_{j+1}-t_j)^{k_j}
(L-t_r)^{k_r}.
\tag{16}
\]

Now restrict the targets to descendants of one shell,

\[
n_j=nm_j.
\]

Write from (14)

\[
A_{n,m_j}=\sum_d c_{j,d}T_d.
\tag{17}
\]

Substituting `mu_nmj=A_{n,m_j}mu_n` into (15), expanding multilinearly, and pulling every pushforward back to the parent variable gives

\[
\boxed{
\begin{aligned}
&\left(\prod_{j=0}^{r}k_j!\right)
J_{2^{k_0},nm_1,2^{k_1},\ldots,nm_r,2^{k_r}}\\
&=\sum_{d_1,\ldots,d_r}
\left(\prod_{j=1}^{r}c_{j,d_j}\right)
\int_{[0,L]^r}
\mathbf 1_{\{h_{d_1}(s_1)<\cdots<h_{d_r}(s_r)\}}
P_{\mathbf k}\!\left(h_{d_1}(s_1),\ldots,h_{d_r}(s_r)\right)
\prod_{j=1}^{r}d\mu_n(s_j).
\end{aligned}}
\tag{18}
\]

Everything outside `mu_n^{\otimes r}` in (18) is universal: the maps `h_d`, the order indicator, the gap polynomial, and the integer coefficients forced by the multiplicative labels. Thus the canonical operation “refine cyclotomically to several levels, then form an arbitrary finite shell-2-interleaved Chen packet” is not a new interacting measure. It is a family of universal kernels evaluated against tensor powers of **one already-known base measure**.

For two targets, the same statement can be seen directly in the antisymmetric sector. If `p` is fresh, `mu_pn=(T_p-I)mu_n`; antisymmetrizing a two-measure ordered integral kills the self-term involving `mu_n otimes mu_n`, leaving only the universal relative-order comparison between `mu_n` and `T_p mu_n`. In the coordinate (9), that comparison is merely order against the dilation `x -> x/p`.

## 5. Matched arbitrary-measure control shows the architecture is not source-specific

The decisive control does not require a second arithmetic source. Let `nu` be an arbitrary finite signed measure on `[0,L]` and declare synthetic descendants by exactly the same rule

\[
\nu_{nm}:=A_{n,m}\nu.
\tag{19}
\]

Because the proof of (11)--(18) uses only pushforwards, linear combinations, tensor products, and ordering, every semigroup identity and every finite cross-level Chen formula remains valid with `mu_n` replaced by `nu`.

Therefore the **architecture** of the proposed cross-level mechanism is source-independent. The cyclotomic source still supplies the special base profile `mu_n`, and the integer labels still specify which universal dilation/difference operators are applied, but no additional cyclotomic interaction law is created when child refinement is composed with finite shell-2 Chen ordering.

This is exactly the source-specificity test required by the research mandate: any RH relevance would have to come from a special arithmetic property of the base measure, or from extra geometric data not represented by (7), rather than from the refinement-plus-Chen construction itself.

## 6. RH relevance and novelty audit

This result closes a genuine gap between two previously independent exact reductions. PC-186 showed that prime radial refinement is a flat commuting dilation/difference calculus, but explicitly left nonlinear ordered multishell combinations open. PC-404 showed that finite multishell Chen packets are ordered product-measure data, but explicitly left cross-level/refinement operations that change the supplied target measures open. Equations (7)--(18) show that the **canonical cyclotomic** operation connecting those two constructions still does not change the information law.

The ingredients themselves are not historically novel. Equation (4) is standard cyclotomic polynomial theory; the multiplicative refinement semigroup belongs to the Bost--Connes/cyclotomic territory already recorded in PC-010; PC-186 already identifies its ordinary radial dilation form; and PC-399--PC-404 already identify shell 2 with a compact moment coordinate and finite Chen packets with ordered product measures. No historical novelty is claimed for any of those components. The durable project-level contribution is the exact intertwining (7), its conjugacy (10), and the resulting closure (18) of the previously open intersection of the refinement and Chen branches.

Nothing in this architecture supplies an independent spectral variable, the archimedean gamma factor, an `s <-> 1-s` functional equation, or a selector for `Re(s)=1/2`. Feeding (18) into a spectral wrapper would therefore inherit the same objection as earlier arbitrary spectralizations: the wrapper would be adding the desired analytic structure rather than deriving it from a new prime-circle carrier.

## 7. Boundary of the negative result

The theorem is deliberately narrower than “cross-level coupling contains no new information.” It rules out the canonical finite construction in which all descendants are produced solely by the cyclotomic prime-child law and all nonlinear combination is the shell-2 ordered Chen product of PC-404.

It does **not** rule out:

- a nonlinear functional that exploits a special arithmetic property of the actual cyclotomic `mu_n` not shared by an arbitrary control measure;
- a source-derived interaction kernel that couples two levels before they reduce to separate pushforwards of one measure;
- angular, chord, old/new, or other genuinely two-dimensional data coupled to radial refinement;
- a non-functorial cross-level operation that changes the state space or product law rather than applying `T_a` to existing data;
- an infinite-level or renormalized analytic limit that can be proved to create genuinely new analytic structure rather than merely taking a limit of the finite universal kernels above.

These are now the relevant escape routes. Merely increasing Chen depth, adding more multiplicative descendants, or changing the order in which prime children are generated cannot evade (18).

## 8. Audit and falsification tests

The core claim is exact and can be attacked at three independent points.

First, (7) is equivalent to the test-function identity (6); any `n,p` and continuous `f` for which direct evaluation of `Phi_pn` disagrees with that pushforward falsifies the result. Second, (8) and (10) are pointwise identities, so failure of the semigroup or dilation conjugacy at one interior `t` would invalidate the descendant formula (12). Third, for any finite descendant list, direct numerical or symbolic evaluation of the Chen coefficient can be compared with the right-hand side of (18); disagreement would isolate either the PC-404 simplex formula or the refinement substitution.

No asymptotic estimate, unproved interchange, or numerical pattern is used in the derivation. All measures live on the compact shell-2 interval before the optional logarithmic-radius conjugacy, and (18) is a finite multilinear expansion.

## Consequence

The most natural remaining cross-level continuation of the shell-2 program is now exhausted: **canonical cyclotomic refinement followed by arbitrary finite shell-2 Chen ordering is one-base-measure dilation data**. A substantive next mechanism must change the information law itself rather than merely traverse the multiplicative descendant tree and then apply the already-classified moment/Chen machinery.