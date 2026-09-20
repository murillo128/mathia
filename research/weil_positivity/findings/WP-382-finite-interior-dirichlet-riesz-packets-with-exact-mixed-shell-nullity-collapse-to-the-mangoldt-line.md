---
id: WP-382
title: Finite interior Dirichlet Riesz packets with exact mixed-shell nullity collapse to the Mangoldt line
branch: weil_positivity
status: supported
kind: pointed-dirichlet-finite-interior-jet-selector-rigidity
claim_strength: exact RH-independent classification showing that every fixed finite linear combination of interior Hardy reproducing-kernel jets of the pointed cyclotomic transform which annihilates all mixed-prime shells has response C Lambda(n) on every primitive shell; consequently every finite vector packet of such exact-support channels is rank one on the shell family and at critical half-density gives only C Lambda(n)/sqrt(n), so finite bounded interior Riesz enrichment cannot create an independent test-function or archimedean selector beyond WP-381
created: 2026-09-20
related: [WP-161, WP-162, WP-168, WP-374, WP-375, WP-378, WP-379, WP-380, WP-381]
clues: [CLUE-weil-positivity-noncharacter-finite-archimedean-incidence]
prior_art:
  - classical local Dirichlet spaces at a boundary point and Hardy H2 reproducing kernels
  - classical cyclotomic index-raising identity Phi_m(z^q)=Phi_mq(z) Phi_m(z) for fresh primes q
  - Hardy/local-Dirichlet formulations of the Nyman--Baez-Duarte criterion
---

# WP-382 — Finite interior Dirichlet Riesz packets with exact mixed-shell nullity collapse to the Mangoldt line

## Claim

`WP-381` found a canonical bounded coordinate inside the pointed local-Dirichlet geometry,

\[
D_1(F,e)=F(1)-F(0),
\qquad e(z)=z-1,
\]

which gives the exact critical finite coefficient

\[
D_1(n^{-1/2}\log\Phi_n,e)=\frac{\Lambda(n)}{\sqrt n}.
\]

A natural escape from its one-dimensional character is to replace the single Hardy coordinate at zero by a finite packet of interior reproducing kernels and their confluent derivatives. Such packets are still canonical bounded Riesz data in `H^2`, can resolve much more analytic information than one scalar endpoint coordinate, and remain inside the source-forced pointed geometry.

That escape is rigid once the exact arithmetic support requirement is imposed.

Let

\[
F_n(z):=\log\Phi_n(z),
\qquad
B_n(z):=T_1F_n(z)
=\frac{F_n(z)-F_n(1)}{z-1}
=\frac{\Lambda(n)-F_n(z)}{1-z},
\tag{1}
\]

where the analytic logarithm is normalized by `F_n(0)=0`. Fix finitely many points `w_i` in the open unit disk, finitely many derivative orders `0<=r<=R_i`, and coefficients `a_{i,r}`. Define the bounded finite interior-jet functional

\[
L(B):=
\sum_{i=1}^s\sum_{r=0}^{R_i}
 a_{i,r} B^{(r)}(w_i).
\tag{2}
\]

Assume only the exact selector condition

\[
L(B_n)=0
\qquad
\text{whenever }n\text{ has at least two distinct prime divisors}.
\tag{3}
\]

Then there is one scalar, determined solely by the chosen jet packet,

\[
C_L:=L\!\left(\frac1{1-z}\right),
\tag{4}
\]

such that for **every** `m>1`,

\[
\boxed{
L(B_m)=C_L\Lambda(m).
}
\tag{5}
\]

Thus finite interior Hardy jets do not enlarge the exact mixed-shell-null selector space on the primitive cyclotomic family. They may look multidimensional as analytic probes, but after imposing exact composite-shell nullity their shell response collapses to the same one-dimensional Mangoldt line already represented by the unit anchor of `WP-381`.

For the critical shells

\[
W_m=m^{-1/2}F_m,
\]

one therefore has

\[
\boxed{
L(T_1W_m)
=C_L\frac{\Lambda(m)}{\sqrt m}.
}
\tag{6}
\]

More generally, if a finite vector of such functionals is required componentwise to vanish on all mixed-prime shells, then its values on all primitive shells have the form

\[
\mathbf L(B_m)=\Lambda(m)v
\tag{7}
\]

for one fixed vector `v`. Every positive Gram form made only from those exact-support selector channels is consequently rank one on the shell family:

\[
\langle \mathbf L(B_m),\mathbf L(B_n)\rangle
=\|v\|^2\Lambda(m)\Lambda(n).
\tag{8}
\]

At critical scale the corresponding diagonal is proportional to `Lambda(n)^2/n`, not to a new linear Weil coefficient or an independent real-place term.

This closes the fixed **finite interior Riesz-packet** enrichment of `WP-381`. A surviving pointed construction must either keep mixed shells active until a later global sign theorem, use an infinite or boundary-accumulating packet, vary the analytic probes with scale for a source-derived reason, or introduce genuinely new finite--archimedean geometry before exact selection.

## 1. The fresh-prime identity supplies the rigidity

For a prime `q` not dividing `m`, the classical cyclotomic identity is

\[
\Phi_{mq}(z)
=\frac{\Phi_m(z^q)}{\Phi_m(z)}.
\tag{9}
\]

With the logarithm branches normalized to vanish at zero, this becomes exactly

\[
F_{mq}(z)=F_m(z^q)-F_m(z)
\qquad (|z|<1).
\tag{10}
\]

Because `m>1` and `q` is a fresh prime, `mq` has at least two distinct prime divisors and therefore

\[
\Lambda(mq)=0.
\tag{11}
\]

Substituting (10)--(11) into (1) gives

\[
\boxed{
B_{mq}(z)
=\frac{F_m(z)-F_m(z^q)}{1-z}.
}
\tag{12}
\]

Now fix `m` and let `q` tend to infinity through primes not dividing `m`. On every compact subset of the unit disk,

\[
F_m(z^q)\longrightarrow0
\tag{13}
\]

locally uniformly, together with every fixed derivative. Indeed `F_m(u)=O(u)` near `u=0`, while derivatives of `z^q` contribute only polynomial factors in `q` against exponential decay `|z|^{q-r}` on `|z|<=rho<1`.

Hence for every fixed finite jet packet in (2),

\[
L(B_{mq})
\longrightarrow
L\!\left(\frac{F_m(z)}{1-z}\right).
\tag{14}
\]

But (1) rearranges to

\[
\frac{F_m(z)}{1-z}
=\frac{\Lambda(m)}{1-z}-B_m(z).
\tag{15}
\]

The left side of (14) is identically zero for every fresh prime `q` by (3). Taking the limit and using (15) yields

\[
0
=\Lambda(m)L\!\left(\frac1{1-z}\right)-L(B_m)
=C_L\Lambda(m)-L(B_m),
\tag{16}
\]

which proves (5).

The argument is exact and uses no zero data, no RH assumption, no prime-distribution theorem, and no asymptotic statement about the size of `Lambda(m)`. The only limiting variable is an auxiliary fresh prime in a classical source identity.

## 2. Why this is a bounded Riesz-packet statement

For `|w|<1`, point evaluation

\[
f\mapsto f(w)
\]

and every fixed derivative evaluation

\[
f\mapsto f^{(r)}(w)
\]

are bounded linear functionals on Hardy `H^2`. Each is represented by the corresponding reproducing kernel or confluent kernel derivative. Therefore every `L` in (2) is a bounded Riesz functional on the Hardy image of the pointed Dirichlet transform `T_1`.

The function `(1-z)^{-1}` appearing in (4) is not itself in `H^2`, but no unbounded Hilbert-space operation is being smuggled into the theorem: `C_L` uses only finitely many interior values and derivatives of that analytic function, all of which are finite. Equation (4) is merely the scalar produced by the compact-open limit (14).

The conclusion is therefore specifically about the most natural finite bounded enlargement of the `WP-381` anchor: finitely many fixed interior Hardy kernels and jets. It does **not** assume that the raw packet is one-dimensional. The one-dimensionality appears only after exact mixed-shell nullity is demanded.

## 3. The WP-381 anchor is unique among single interior evaluation anchors

Take the smallest packet,

\[
L_w(B):=B(w),
\qquad |w|<1.
\tag{17}
\]

If `L_w(B_n)=0` on every mixed-prime shell, (5) gives

\[
B_m(w)=\frac{\Lambda(m)}{1-w}
\qquad(m>1).
\tag{18}
\]

Comparing with (1) forces

\[
F_m(w)=0
\qquad(m>1).
\tag{19}
\]

Already `m=2` is decisive because

\[
F_2(z)=\log\Phi_2(z)=\log(1+z).
\tag{20}
\]

On the open unit disk, with the analytic branch normalized at zero,

\[
\log(1+w)=0
\quad\Longrightarrow\quad
w=0.
\tag{21}
\]

Thus the only nonzero single interior evaluation channel with exact mixed-shell nullity is the zero-coordinate evaluation

\[
B_n(0)=\Lambda(n),
\tag{22}
\]

which is precisely the Riesz anchor isolated in `WP-381`.

This is a useful matched control against the idea that the anchor at zero was an arbitrary choice. Moving the reproducing kernel to any fixed nonzero interior point immediately restores mixed-shell response. In fact, for `m=2` and fresh primes `q`, (12) gives

\[
B_{2q}(w)
\longrightarrow
\frac{\log(1+w)}{1-w}\ne0
\qquad(w\ne0),
\tag{23}
\]

so exact nullity cannot survive.

## 4. Finite vector packets cannot manufacture an independent selector family

Suppose a proposed positive completion uses a fixed finite vector of bounded interior jet coordinates

\[
\mathbf L(B)
=(L_1(B),\ldots,L_d(B)),
\tag{24}
\]

and requires every coordinate to vanish on mixed-prime shells before positivity is imposed. Applying (5) componentwise gives

\[
\mathbf L(B_m)
=\Lambda(m)(C_{L_1},\ldots,C_{L_d}).
\tag{25}
\]

Therefore the image of the entire primitive-shell family lies on one line. Any positive matrix weighting `M>=0` on this finite packet gives

\[
\mathbf L(B_m)^*M\mathbf L(B_n)
=c_M\Lambda(m)\Lambda(n),
\qquad c_M\ge0,
\tag{26}
\]

and after critical normalization,

\[
\frac{c_M\Lambda(m)\Lambda(n)}{\sqrt{mn}}.
\tag{27}
\]

No choice of a fixed positive matrix creates a second shell-dependent degree of freedom. In particular it cannot produce an exact family

\[
\frac{\Lambda(n)}{\sqrt n}\,g(\log n)
\tag{28}
\]

for arbitrary nonconstant test data `g` while simultaneously maintaining exact mixed-shell nullity through these channels. The only allowed dependence on `n` is the Mangoldt factor already present in `WP-381`; all packet-specific information is absorbed into one constant vector.

This does not say that (8) or (26) is itself the finite side of Weil positivity. A rank-one positive selector energy gives a square of a Mangoldt sum. The classical explicit formula requires a much richer test-function-dependent finite--archimedean assembly. `WP-381` already showed that the linear finite term can occur as a cross term with the unit anchor; the present result says that adding finitely many fixed interior Riesz probes does not create the missing independent selector geometry.

## 5. Adversarial controls and exact scope

Several stronger conclusions would be unjustified.

First, the theorem uses **exact** mixed-shell nullity. If mixed-prime channels are deliberately retained until after finite and archimedean pieces interact, the hypothesis (3) fails and the packet can carry additional analytic information. That is a live escape, not a defect in the proof.

Second, the packet is fixed and finite. An infinite collection of kernels, a sequence of points approaching the unit circle, derivative order tending to infinity, or probes that vary with the shell scale need not commute with the compact-open spectator-prime limit used in (14). Such a construction would have to derive its growth or boundary accumulation from the source geometry and control its energy; it is not ruled out here.

Third, the theorem classifies the **response on the cyclotomic shell family**, not the ambient Hardy functional itself. Distinct finite jet combinations may differ on general `H^2` vectors while inducing the same scalar multiple of `Lambda` on every `F_n`. No density statement about the shell span is assumed, so the result does not smuggle in a Nyman--Beurling or RH-equivalent completeness claim.

Fourth, the result does not rule out a singular boundary functional. Indeed the mechanism explains why such a possibility remains structurally different: the fresh-prime limit `F_m(z^q)->0` is uniform only on compact subsets strictly inside the disk. Boundary accumulation is exactly where the finite-interior proof ceases to apply.

Finally, the conclusion is not a new proof of any classical Weil criterion. It is a route-specific rigidity statement: if exact prime-power selection is demanded *before* a fixed finite bounded interior Riesz packet enters a positive Gram construction, that packet has only the Mangoldt line available.

## 6. Prior-art and novelty audit

The ingredients are classical. The identity (9) is the standard prime-index cyclotomic relation. For example, De Carli and Laporta, *Divisibility criteria and coefficient formulas for cyclotomic polynomials*, Ramanujan Journal 70 (2026), explicitly note that the Arnold--Monagan recursion starts from

`Phi_m(z^p)=Phi_mp(z) Phi_m(z)`

for a fresh prime `p`:

https://link.springer.com/article/10.1007/s11139-026-01421-6

The use of Hardy and local Dirichlet spaces in RH-equivalent Hilbert-space formulations is also established prior art. S. Waleed Noor, *A Hardy space analysis of the Baez-Duarte criterion for the RH* (2018), develops precisely such `H^2`, local-Dirichlet, and Nyman--Baez-Duarte machinery:

https://arxiv.org/abs/1809.09577

`WP-168` already treats that Nyman/Mellin overlap as prior art for Mathia's full-root pointed geometry. Nothing here claims novelty for local Dirichlet spaces, Hardy reproducing kernels, cyclotomic index raising, or the Mangoldt identity `log Phi_n(1)=Lambda(n)`.

A bounded literature search did not locate the specific combination proved here: using the fresh-prime cyclotomic identity to classify fixed finite interior Hardy-jet selectors on primitive cyclotomic shells under exact mixed-prime nullity, and then reading the result as a rigidity theorem for a candidate Weil-positive finite--global incidence. No broad literature novelty is claimed; the durable delta is the exact Mathia route boundary relative to `WP-381`.

## Consequence for the research line

The positive result of `WP-381` cannot be turned into a multi-coordinate exact finite selector merely by taking finitely many more bounded interior Riesz probes of the same pointed analytic geometry. The single endpoint coordinate is not just the first member of a larger finite family carrying independent prime-power data. Under exact mixed-shell nullity, **every fixed finite interior kernel/jet packet collapses back to the same Mangoldt line**.

This sharpens the remaining search. A candidate should not spend effort on another fixed finite packet of interior evaluations, derivatives, or positive matrix completions unless it intentionally keeps mixed shells alive. The viable escapes are now structurally different: an infinite or boundary-singular Riesz sector with source-forced energy control; a scale-varying family justified before seeing the target coefficient; or a genuinely global finite--archimedean coupling in which mixed-shell information is retained through an indefinite/nonlocal stage and only the assembled object is subjected to an independent sign theorem.
