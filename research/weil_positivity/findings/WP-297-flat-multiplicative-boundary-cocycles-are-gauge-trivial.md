---
id: WP-297
title: Flat multiplicative boundary cocycles are gauge-trivial and cannot evade Möbius rigidity
branch: weil_positivity
status: supported
kind: cocycle-gauge-no-go
claim_strength: exact classification showing that source-covariant site-dependent flat transport and parallel positive metrics gauge back to the multiplicative-shift-equivariant convolution class, so exact Weil localization still forces Möbius on every visible channel
created: 2026-09-14
related: [WP-293, WP-295, WP-296]
prior_art:
  - Mati Kilp, Ulrich Knauer, Alexander V. Mikhalev, Monoids, Acts and Categories (2000)
  - Jean Renault and S. Sundar, Groupoids associated to semigroup actions, arXiv:1402.2762
  - standard fact that a category with an initial object has contractible nerve
---

# WP-297 — Flat multiplicative boundary cocycles are gauge-trivial and cannot evade Möbius rigidity

## Claim

`WP-296` closes the linear nonlocal escape when a coupling commutes with the multiplicative shifts. It deliberately leaves open a natural weakening: perhaps the output fiber or boundary state can depend on the integer site, with multiplicative translation transporting vectors by a site-dependent unitary or invertible map. Such a construction no longer commutes literally with the untwisted shifts and could appear to supply the source-forced symmetry breaking that `WP-296` says is necessary.

For **flat multiplicative transport**, it does not. The site dependence is pure gauge.

Let `H` be a complex Hilbert space and let

\[
C(m,n)\in GL(H),\qquad m,n\ge 1,
\]

satisfy the normalized multiplicative cocycle law

\[
C(ab,n)=C(a,bn)C(b,n),
\qquad C(1,n)=I.
\tag{1}
\]

Define the twisted multiplicative shifts on `H`-valued arithmetic sequences by

\[
(S_m^C h)(N)
=
\begin{cases}
C(m,N/m)h(N/m),&m\mid N,\\
0,&m\nmid N.
\end{cases}
\tag{2}
\]

Then there is a pointwise gauge `G(n) in GL(H)` for which

\[
\boxed{C(m,n)=G(mn)G(n)^{-1}}
\tag{3}
\]

for every `m,n`. Consequently the twisted shifts are exactly conjugate to the ordinary multiplicative shifts.

If a coefficientwise-continuous linear map `T` intertwines ordinary source shifts with this twisted output action,

\[
T S_m=S_m^C T,
\tag{4}
\]

then after the gauge change it lies in the commutant classified by `WP-296`. Hence there is an `H`-valued arithmetic kernel `A` such that, on a scalar arithmetic sequence `f`,

\[
\boxed{
(Tf)(N)=G(N)\sum_{d\mid N}A(d)f(N/d).
}
\tag{5}
\]

In particular, on the logarithmic source `L(N)=log N`,

\[
(TL)(N)=G(N)(A*L)(N).
\tag{6}
\]

Two positive-readout consequences are exact.

First, if every `C(m,n)` is unitary and the readout is the ordinary Hilbert norm, then the gauge is unitary and

\[
\|(TL)(N)\|=\|(A*L)(N)\|.
\tag{7}
\]

Therefore exact finite-Weil localization

\[
\|(TL)(N)\|=\Lambda(N)
\tag{8}
\]

forces, by `WP-295`,

\[
\boxed{A(N)=u\,\mu_{\rm Mob}(N)}
\tag{9}
\]

for one fixed unit vector `u`. The apparent site-dependent boundary transport has only rotated the same Möbius direction.

Second, suppose the output carries bounded positive-semidefinite forms `Q_N` that are parallel under the transport,

\[
C(m,n)^*Q_{mn}C(m,n)=Q_n.
\tag{10}
\]

Then the same gauge makes the metric site-independent:

\[
\boxed{G(N)^*Q_NG(N)=Q_1.}
\tag{11}
\]

If

\[
\sqrt{\langle (TL)(N),Q_N(TL)(N)\rangle}=\Lambda(N),
\tag{12}
\]

then every channel visible to the positive form again collapses to Möbius:

\[
\boxed{Q_1^{1/2}A(N)=u\,\mu_{\rm Mob}(N)}
\tag{13}
\]

for one fixed unit vector `u` in the visible Hilbert quotient. Components in `ker Q_1` remain arbitrary but are invisible to the claimed positive readout.

Thus **flat source-covariant site dependence is not genuine multiplicative symmetry breaking**. To escape the convolution/Möbius rigidity of `WP-295`--`WP-296`, a boundary construction must introduce non-flat mixed-prime curvature, additional boundary topology/orbits, a metric not parallel under the source action, a nonlinear operation before scalarization, or a genuinely global finite--archimedean coupling.

**Classification:** `EXACT-DERIVED + FLAT-MULTIPLICATIVE-COCYCLE + PURE-GAUGE + SITE-DEPENDENT-PARALLEL-METRIC + WP-296-COMMUTANT + WP-295-MOBIUS-RIGIDITY + CURVATURE-REQUIRED + GENERALIZED-PRIME-GENERIC + ROUTE-CLOSURE + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. The rooted multiplicative action trivializes every flat cocycle

Set

\[
G(n):=C(n,1).
\tag{14}
\]

Apply (1) with `a=m`, `b=n`, and base point `1`:

\[
G(mn)=C(m,n)G(n).
\tag{15}
\]

Since `G(n)` is invertible,

\[
C(m,n)=G(mn)G(n)^{-1},
\tag{16}
\]

which is (3). No analytic assumption, commutativity of the operators `C(m,n)`, or information about primes is used.

Categorically, the objects are positive integers and a multiplicative morphism `m` sends `n` to `mn`. The object `1` is initial: there is exactly one such morphism from `1` to every `n`, namely multiplication by `n`. A flat local system on this rooted action category therefore has a canonical transport from the root to each fiber, and those root transports trivialize all other transports. This is the concrete cocycle version of the standard fact that a category with an initial object has contractible nerve.

Define the pointwise gauge

\[
(Jh)(N):=G(N)^{-1}h(N).
\tag{17}
\]

For `m|N`, (16) gives

\[
\begin{aligned}
(JS_m^C h)(N)
&=G(N)^{-1}C(m,N/m)h(N/m)\\
&=G(N/m)^{-1}h(N/m)\\
&=(S_mJh)(N).
\end{aligned}
\tag{18}
\]

Thus

\[
\boxed{J S_m^C=S_mJ.}
\tag{19}
\]

The twisted representation is not merely similar in some asymptotic sense; it is exactly gauge-equivalent, coefficient by coefficient, to the ordinary one.

## 2. Every flat-covariant linear boundary map reduces to the `WP-296` commutant

Assume `T` is continuous for the product topology on arithmetic sequence spaces and satisfies (4). Combining (4) with (19),

\[
(JT)S_m
=J S_m^C T
=S_m(JT).
\tag{20}
\]

Therefore `JT` commutes with every ordinary multiplicative shift. The commutant theorem of `WP-296` supplies a unique operator-valued Dirichlet kernel. For scalar input, absorb the action of that kernel on `1` into an `H`-valued arithmetic function `A`; then

\[
(JTf)(N)=\sum_{d\mid N}A(d)f(N/d)=(A*f)(N).
\tag{21}
\]

Undoing the gauge proves (5).

This classification is stronger than saying that a particular twisted example can be untwisted. **Every** continuous linear intertwiner into a flat multiplicative boundary bundle has only two ingredients: a global pointwise gauge `G(N)` and one ordinary Dirichlet-convolution kernel `A`. Any finite stack of such flat-covariant linear layers can likewise be gauged layer by layer and collapsed to the single effective convolution already treated in `WP-296`.

The site dependence therefore carries no additional arithmetic invariant unless a later readout is deliberately made gauge-sensitive. Such a readout is not automatically forbidden, but its gauge dependence must then be justified by extra source geometry; the flat transport itself does not provide it.

## 3. Unitary transport leaves positive norm selection exactly unchanged

Assume now

\[
C(m,n)^*C(m,n)=I.
\tag{22}
\]

Then every root transport `G(N)=C(N,1)` is unitary. For the logarithmic source,

\[
F(N):=(TL)(N)=G(N)(A*L)(N),
\tag{23}
\]

so

\[
\|F(N)\|=\|(A*L)(N)\|.
\tag{24}
\]

Suppose the norm is intended to recover exactly the finite arithmetic selector:

\[
\|F(N)\|=\Lambda(N)
\qquad(N\ge2).
\tag{25}
\]

Then `(A*L)(N)=0` at every non-prime-power integer. `WP-295` shows that prime-power support alone, once three independent prime generators are present, already forces

\[
A*L=u\Lambda,
\qquad
A=u\mu_{\rm Mob}
\tag{26}
\]

for one fixed vector `u`; (25) normalizes `||u||=1`.

So a unitary boundary bundle can make the visible direction vary as `G(N)u`, but it cannot change the arithmetic inverse that created the support. The sign of Möbius has not disappeared; it has been hidden upstream of a norm in exactly the sense classified by `WP-295`.

## 4. Parallel site-dependent positive metrics are also gauge-trivial

A natural attempt to escape (24) is to let the positive form itself vary with the site. Arbitrary variation is too programmable to be informative: one can simply choose `Q_N` to vanish or amplify on a prescribed arithmetic set. The source-covariant version is the parallelity condition (10).

Taking `m=N`, `n=1` in (10) and using `G(N)=C(N,1)` yields

\[
G(N)^*Q_NG(N)=Q_1,
\tag{27}
\]

which is (11). Hence, writing

\[
B(N):=(A*L)(N),
\]

we obtain

\[
\begin{aligned}
\langle F(N),Q_NF(N)\rangle
&=\langle G(N)B(N),Q_NG(N)B(N)\rangle\\
&=\langle B(N),Q_1B(N)\rangle\\
&=\|Q_1^{1/2}B(N)\|^2.
\end{aligned}
\tag{28}
\]

Define the visible Hilbert-valued kernel

\[
A_{\rm vis}(d):=Q_1^{1/2}A(d).
\tag{29}
\]

Because `Q_1^{1/2}` is fixed and bounded,

\[
Q_1^{1/2}(A*L)=A_{\rm vis}*L.
\tag{30}
\]

Exact equality (12) therefore reduces to the fixed-norm hypothesis of `WP-295`. Thus

\[
A_{\rm vis}(d)=u\mu_{\rm Mob}(d),
\tag{31}
\]

which proves (13).

This is the appropriate anti-programming statement for a site-dependent positive form. **Variation that is only parallel transport contains no new positive geometry.** To matter, a varying metric must fail parallelity in a source-forced way, and that failure itself becomes the new structure whose arithmetic content and sign theorem must be justified.

## 5. Prime-diamond curvature is the exact boundary between flat gauge and genuine mixed incidence

For distinct primes `p,q`, there are two elementary multiplicative paths from `n` to `pqn`. Their transports are

\[
C(p,qn)C(q,n)
\quad\text{and}\quad
C(q,pn)C(p,n).
\tag{32}
\]

The cocycle law and commutativity of integer multiplication force

\[
C(p,qn)C(q,n)
=C(pq,n)
=C(q,pn)C(p,n).
\tag{33}
\]

Thus every prime diamond has trivial holonomy. Equivalently, the curvature operator

\[
\mathcal K_{p,q}(n)
:=
\bigl[C(q,pn)C(p,n)\bigr]^{-1}
C(p,qn)C(q,n)
\tag{34}
\]

is identically `I`.

This identifies a sharper surviving question than the broad phrase “site-dependent boundary condition.” A boundary transport can evade the theorem only if the full source geometry supplies something not representable by the flat action cocycle (1). The smallest finite certificate is a nontrivial prime-diamond response, or an obstruction to even defining a single transport `C(m,n)` independent of path. Such curvature would be genuine cross-prime incidence **before positivity is formed**, precisely the type of missing structure isolated by the accepted non-character-incidence clue.

Nontrivial curvature is only a necessary escape from this no-go, not sufficient evidence for Weil positivity. It would still have to be canonical, survive generalized-prime controls in a Riemann-specific way, couple correctly to the real place, and support an independent global sign theorem.

## 6. Matched controls and generalized-prime boundary

The proof uses only the rooted free multiplicative action and the three-generator support rigidity imported from `WP-295`. It does not use numerical properties of ordinary primes, the zeta functional equation, Gamma factors, or zero data.

Accordingly, the same gauge-triviality holds for any free generalized-prime monoid: the identity is again an initial object, so every flat invertible transport cocycle is a coboundary. With at least three independent generators and nonzero logarithmic axis weights, `WP-295` then gives the same visible Möbius-type inverse in the generalized arithmetic convolution ring.

This clone invariance is decisive for interpretation. The theorem removes a false architecture; it does **not** produce the arithmetic distinction required by the research mandate. A successful non-flat boundary geometry would have to explain why its curvature or topology is forced for the Riemann system and not merely available in every free-prime clone.

The two-generator exception of `WP-295` also remains intact. Gauge triviality itself does not need three primes, but the final implication from exact prime-power support to one Möbius direction does. Thus the cocycle theorem and the support theorem have distinct hypotheses and should not be conflated.

## 7. Prior-art and novelty audit

The abstract ingredients are classical. Monoid actions, acts, and their categorical organization are standard; Kilp--Knauer--Mikhalev give a broad reference. Renault--Sundar provide a modern groupoid treatment of semigroup actions. The topological statement behind the gauge calculation is also standard: a category with an initial object has contractible nerve because the identity functor is naturally homotopic to the constant functor at the initial object.

No novelty is claimed for those facts, and (15)--(16) are elementary enough that the present argument does not depend on a sophisticated cohomology theorem. In particular, the phrase “flat cocycle is pure gauge” is not being presented as a new result in category theory, semigroup cohomology, or gauge theory.

The Mathia-specific delta is the composition of that elementary trivialization with the exact commutant classification of `WP-296` and the three-prime support theorem of `WP-295`. `WP-296` explicitly left boundary-/site-dependent maps outside its theorem. The present result shows that a large and natural subclass of such maps—flat source-covariant transport, even with parallel site-dependent positive metrics—does **not** escape. It also converts the remaining boundary into a precise falsifiable object: nontrivial prime-diamond curvature or genuinely additional boundary topology must appear before the positivity mechanism can be new.

## 8. Aggressive falsification and exact boundary

Several apparent counterexamples were separated from the theorem rather than hidden in its hypotheses.

A general invertible, nonunitary cocycle is still algebraically a coboundary by (16). What can fail is norm invariance: if one keeps an arbitrary fixed norm while applying a nonunitary gauge, magnitudes may change with `N`. That does not contradict the theorem. To retain a geometrically meaningful positive form, one needs either unitarity or the parallel-metric condition (10); otherwise the varying metric/gauge can itself encode the target coefficients.

Arbitrary site-dependent `Q_N` are therefore intentionally outside the positive corollary. So are unbounded quadratic forms whose domains vary with `N`, unless a common domain and a valid gauge/parallelity theorem are proved. A singular domain change could carry genuine information and must be audited separately.

Projective cocycles, non-flat connections, path-dependent transports, extra boundary vertices or orbits not generated from the root `1`, nonlinear rank/determinant/exterior-power operations, and finite--archimedean couplings that modify the action before scalarization are also outside the result. These are not technical loopholes: they are exactly the structures capable of carrying curvature or topology that the rooted flat category lacks.

Finally, the theorem concerns exact finite-Weil localization when `WP-295` is invoked. Restricted test panels, approximate localization, or approximate parallelity require quantitative stability estimates not supplied here. `WP-294` still says that an exact final Weil quadratic form on the full autocorrelation cone cannot hide an exact scalar finite-place error behind a finite-place-clean remainder, but approximate versions remain a separate problem.

## Consequence for `weil_positivity`

The post-`WP-296` frontier can be narrowed from “break multiplicative-shift equivariance by making the boundary site-dependent” to a sharper statement:

\[
\boxed{
\text{flat source-covariant site dependence}
\Longrightarrow
\text{pure gauge}
\Longrightarrow
\text{ordinary equivariant convolution}
\Longrightarrow
\text{Möbius on every exact visible Weil channel}.
}
\tag{35}
\]

So a viable boundary route cannot obtain new arithmetic content merely by transporting a fixed positive fiber along the multiplicative lattice. It needs **curvature, extra topology, nonlinear geometry, or a genuinely global finite--archimedean relation before positivity is read out**. The prime-diamond test (34) is the smallest exact diagnostic for whether a proposed site-dependent construction has actually left the flat class.

No such non-flat Mathia-native boundary geometry, Gamma/polar completion, or independent Weil sign theorem is established here. The result is a route closure and a sharper search boundary, not a proof of Weil positivity or RH.
