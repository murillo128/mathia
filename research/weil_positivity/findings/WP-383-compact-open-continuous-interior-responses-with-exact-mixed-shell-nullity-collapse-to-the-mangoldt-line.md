---
id: WP-383
title: Compact-open-continuous interior responses with exact mixed-shell nullity collapse to the Mangoldt line
branch: weil_positivity
status: supported
kind: pointed-cyclotomic-compact-open-response-rigidity
claim_strength: exact RH-independent Banach/Hilbert-valued extension of WP-382 showing that every fixed compact-open-continuous linear response of the pointed cyclotomic source which annihilates mixed-prime shells has response Lambda(n) times one fixed vector on every shell; therefore arbitrary infinite interior packets that remain uniformly controlled on a fixed compact subdisk still give only a rank-one Mangoldt Gram, and any surviving infinite escape must genuinely reach the boundary or otherwise break compact-open continuity
created: 2026-09-20
related: [WP-168, WP-374, WP-378, WP-379, WP-380, WP-381, WP-382]
clues: [CLUE-weil-positivity-noncharacter-finite-archimedean-incidence]
prior_art:
  - classical compact-open Frechet topology on spaces of holomorphic functions
  - classical cyclotomic index-raising identity Phi_m(z^q)=Phi_mq(z) Phi_m(z) for fresh primes q
  - Hardy/local-Dirichlet formulations of the Nyman--Baez-Duarte criterion
---

# WP-383 — Compact-open-continuous interior responses with exact mixed-shell nullity collapse to the Mangoldt line

## Claim

`WP-382` proved that every fixed **finite** packet of interior Hardy evaluations and jets that annihilates all mixed-prime pointed cyclotomic shells collapses to the Mangoldt line. The obvious remaining loophole was that an infinite interior packet might retain independent arithmetic information even when every finite packet fails.

That loophole is smaller than it first appears. Finiteness is not the relevant boundary. The relevant boundary is **compact-open continuity**.

Let

\[
F_n(z):=\log\Phi_n(z),
\qquad
B_n(z):=\frac{\Lambda(n)-F_n(z)}{1-z},
\tag{1}
\]

with the analytic logarithm on the unit disk normalized by `F_n(0)=0`. Let `H(D)` denote the Frechet space of holomorphic functions on the open unit disk with the topology of uniform convergence on compact subsets. Let `K` be a Banach space and let

\[
T:H(\mathbb D)\longrightarrow K
\tag{2}
\]

be a continuous linear response. Assume

\[
T(B_n)=0
\qquad
\text{whenever }n\text{ has at least two distinct prime divisors}.
\tag{3}
\]

Then one vector

\[
v:=T\!\left(\frac1{1-z}\right)\in K
\tag{4}
\]

controls the response of **every** shell:

\[
\boxed{
T(B_m)=\Lambda(m)v
\qquad(m>1).
}
\tag{5}
\]

Thus an arbitrary finite- or infinite-dimensional interior response packet does not escape `WP-382` merely by having infinitely many coordinates. If the whole packet is a single continuous linear map for the compact-open topology, exact mixed-shell nullity again leaves only one arithmetic degree of freedom.

For the critical shells `W_m=m^{-1/2}F_m`, linearity gives

\[
T(T_1W_m)=\frac{\Lambda(m)}{\sqrt m}\,v.
\tag{6}
\]

If `K` is Hilbert and positivity is supplied by its norm or Gram form, then

\[
\langle T(B_m),T(B_n)\rangle
=\Lambda(m)\Lambda(n)\|v\|^2,
\tag{7}
\]

so the shell Gram has rank at most one. The missing independent test-function and archimedean/global channel still does not appear.

The genuine remaining escape is therefore sharper than the one left by `WP-382`: a useful infinite packet must be **boundary-accumulating, scale-dependent, or otherwise non-continuous for the compact-open topology**, unless it deliberately keeps mixed shells active until a later finite--archimedean coupling.

## 1. Fresh-prime dilation gives a compact-open limit

Fix `m>1` and let `q` run through primes with `q` not dividing `m`. The standard cyclotomic relation

\[
\Phi_{mq}(z)=\frac{\Phi_m(z^q)}{\Phi_m(z)}
\tag{8}
\]

holds for fresh `q`. Since every cyclotomic polynomial has no zero in the open unit disk and has value `1` at zero, the normalized analytic logarithms satisfy exactly

\[
F_{mq}(z)=F_m(z^q)-F_m(z).
\tag{9}
\]

Because `mq` has at least two distinct prime divisors,

\[
\Lambda(mq)=0,
\tag{10}
\]

and hence

\[
B_{mq}(z)
=\frac{F_m(z)-F_m(z^q)}{1-z}.
\tag{11}
\]

For every fixed `0<r<1`, `F_m(u)=O_m(u)` near zero, so

\[
\sup_{|z|\le r}|F_m(z^q)|=O_m(r^q).
\tag{12}
\]

Since `1/(1-z)` is bounded on every such disk,

\[
\frac{F_m(z^q)}{1-z}\longrightarrow0
\tag{13}
\]

in the compact-open topology. Therefore

\[
B_{mq}
\longrightarrow
\frac{F_m}{1-z}
=\frac{\Lambda(m)}{1-z}-B_m
\tag{14}
\]

in `H(D)`.

Continuity of `T` now gives

\[
T(B_{mq})
\longrightarrow
\Lambda(m)T\!\left(\frac1{1-z}\right)-T(B_m).
\tag{15}
\]

The left side is exactly zero for every fresh prime `q` by (3). Taking the limit proves (5).

No prime-distribution estimate, zero data, RH assumption, spectral insertion, or regularization enters the argument. The auxiliary prime tends to infinity only to remove the spectator dilation `z -> z^q` on compact subsets of the disk.

## 2. Compact-open continuity means one fixed interior radius controls the whole packet

The extension beyond `WP-382` is not a formal replacement of a finite vector by an infinite one. Continuity of a linear map from `H(D)` into a normed space has a concrete consequence.

The compact-open topology can be generated by seminorms

\[
p_r(f):=\sup_{|z|\le r}|f(z)|,
\qquad 0<r<1.
\tag{16}
\]

Because `T` is continuous at zero, finitely many such seminorms control its norm. Taking their largest radius gives some `r<1` and `C>0` with

\[
\boxed{
\|Tf\|_K\le C p_r(f)
\qquad(f\in H(\mathbb D)).
}
\tag{17}
\]

Thus even if `K` has infinitely many coordinates, the entire response is uniformly controlled by analytic data inside one fixed compact subdisk.

Combining (12) and (17) yields the quantitative spectator estimate

\[
\left\|
T\!\left(\frac{F_m(z^q)}{1-z}\right)
\right\|_K
\le
\frac{C}{1-r}
\sup_{|z|\le r}|F_m(z^q)|
=O_{m,T}(r^q).
\tag{18}
\]

Hence the fresh-prime part dies exponentially for every compact-open-continuous packet, not merely coordinatewise for a finite list of jets.

The theorem also has a stable approximate form. From (11)--(15),

\[
\|T(B_m)-\Lambda(m)v\|_K
\le
\|T(B_{mq})\|_K+O_{m,T}(r^q).
\tag{19}
\]

Therefore it is already enough that `T(B_mq) -> 0` along fresh primes for each fixed `m`; exact nullity is stronger than necessary. Approximate mixed-shell suppression that genuinely tends to zero cannot hide an additional interior channel.

## 3. Dual/moment form identifies the actual escape boundary

For a scalar compact-open-continuous functional `ell`, (17) implies

\[
|\ell(z^k)|\le Cr^k.
\tag{20}
\]

So the moments of every such interior functional decay geometrically. Finite evaluation/jet packets from `WP-382` are a strict subclass of this dual: the present theorem also covers infinite linear combinations and vector-valued packets whenever their total response remains controlled at one interior radius.

This immediately explains what the proof does **not** cover. A bounded Hardy `H^2` functional can have a Riesz vector whose Taylor coefficients lie in `ell^2` but do not decay geometrically. For example coefficients comparable to `1/(k+1)` define an `ell^2` vector, yet they cannot satisfy (20) for any `r<1`. Such a functional is bounded for the `H^2` norm but is not continuous for the compact-open topology on all of `H(D)`.

That distinction is the matched control. An infinite boundary-sensitive Hardy packet is not being ruled out by a hidden assumption: it lies precisely outside the topology in which the spectator-prime dilation disappears uniformly. Conversely, any proposed "infinite interior" repair whose energy bounds imply (17) has already fallen back inside the no-go theorem.

The canonical anchor from `WP-381` is the positive control. Evaluation at zero is compact-open continuous and satisfies

\[
B_n(0)=\Lambda(n),
\tag{21}
\]

so (5) recovers its exact response rather than incorrectly killing all selectors.

## 4. Representation audit

The conclusion survives several representations of the same construction, but the continuity hypothesis is architecture-sensitive.

**Intrinsic/native lens.** The objects are the source-forced pointed cyclotomic shells `B_n`. The fresh-prime relation is an identity internal to their cyclotomic incidence, and the anchor `1/(1-z)` is forced by the same pointed transform. This preserves exact shell incidence and forgets how a candidate implementation stores its response coordinates.

**Operator lens (primary).** The candidate geometry is summarized by one response operator `T:H(D)->K`; if `K` is Hilbert, positivity is the ordinary norm/Gram positivity of its image. Under mixed-shell nullity the source family has one-dimensional image, so positive completion inside this response space cannot create an independent finite or real-place degree of freedom.

**Invariant/symmetry lens (secondary).** Adjoining a fresh prime acts by the dilation `z -> z^q` in (9). On every fixed compact subdisk this spectator component contracts exponentially to the zero germ. Any response continuous for that topology must respect the contraction, which is the invariant mechanism behind (5).

**Representation-change/dual lens.** Passing to dual moments turns compact-open continuity into geometric decay as in (20). This makes the escape boundary explicit: boundary-accumulating Hardy data can remain bounded in an `H^2` representation while ceasing to be compact-open continuous.

The **representation-invariant** content is the rank-one shell collapse for every response that is continuous under locally uniform convergence. What remains **architecture-sensitive** is whether a proposed Mathia-native boundary/cusp construction really has that continuity. A singular boundary response may escape, but it must then justify its energy and finite--archimedean coupling independently rather than being described as merely a larger interior packet.

## 5. Adversarial scope and controls

The theorem does not say that every infinite positive completion of the pointed geometry is rank one. It says this only when exact mixed-shell selection is imposed before positivity and the resulting response is compact-open continuous. Keeping mixed shells alive until after an indefinite or finite--archimedean interaction avoids hypothesis (3).

It also does not rule out a sequence of probes whose radii approach one with arithmetic scale, a boundary distribution, an unbounded operator subsequently closed in another topology, or a source-derived cusp sector. Those mechanisms can fail (17). They remain live only if their scale dependence or singularity is generated by the source geometry and if their positivity does not amount to a hand-picked regularization.

Nor is a density or completeness statement about the cyclotomic shells assumed. The operator can behave arbitrarily on other holomorphic functions. Equation (5) classifies only its values on the source shell family under the mixed-shell condition, so it does not import an RH-equivalent Nyman--Beurling totality criterion.

Finally, (7) is not asserted to be Weil's finite term. It is exactly the obstruction: norm positivity applied after the collapse produces a rank-one square of Mangoldt data, whereas a global Weil criterion requires test-function-dependent finite-prime coefficients together with a separately matched Gamma/polar completion.

## 6. Prior-art and novelty audit

All analytic ingredients are standard. The space `H(D)` of holomorphic functions with uniform convergence on compact subsets is a Frechet space whose topology is generated by compact sup-seminorms; this standard setup is stated, for example, in the holomorphic-function-space literature:

https://link.springer.com/article/10.1007/s13398-022-01380-9

The fresh-prime identity (8) is the classical cyclotomic recursion. De Carli and Laporta, *Divisibility criteria and coefficient formulas for cyclotomic polynomials*, Ramanujan Journal 70 (2026), discuss the corresponding prime-index recursion:

https://link.springer.com/article/10.1007/s11139-026-01421-6

Hardy and local-Dirichlet Hilbert-space formulations around RH are also prior art. Noor, *A Hardy space analysis of the Baez-Duarte criterion for the RH*, develops those spaces in an explicitly RH-equivalent setting:

https://arxiv.org/abs/1809.09577

`WP-168` already records that overlap. Nothing here claims novelty for the Frechet topology, analytic functionals, Hardy Riesz representation, cyclotomic recursion, or Mangoldt endpoint identity.

A bounded literature search did not locate the specific route-level theorem used here: the fresh-prime cyclotomic dilation combined with compact-open continuity to classify arbitrary Banach/Hilbert-valued exact mixed-shell responses as one fixed vector times `Lambda(n)`. No broad mathematical novelty claim is made. The durable delta is relative to `WP-382`: **finite dimensionality is not the obstruction; fixed-interior continuity is**.

## Consequence for the research line

`WP-382` left "infinite packet" as a broad possible escape. This result separates two very different meanings of infinite. Merely adding infinitely many interior coordinates does nothing if their joint response is uniformly controlled on a fixed compact subdisk: exact mixed-shell nullity still collapses the entire source family to one Mangoldt vector.

The next boundary-sector experiment should therefore test a genuinely boundary-accumulating or scale-varying response, not another fixed-radius infinite enrichment. Its first adversarial question is now concrete: **does the proposed source-derived energy force compact-open continuity anyway?** If yes, (5) kills the route immediately. If no, the construction must show that the resulting boundary singularity remains geometrically canonical, positive independently of RH, and capable of coupling the finite Mangoldt channel to the required archimedean/global counterterm.