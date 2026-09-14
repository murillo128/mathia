---
id: WP-296
title: Multiplicative-shift equivariance turns every linear nonlocal coupling back into Dirichlet convolution
branch: weil_positivity
status: supported
kind: equivariant-nonlocal-relocalization-no-go
claim_strength: exact commutant classification on coefficientwise arithmetic sequence spaces, combined with WP-295 to force Möbius on every visible exact Weil-relocalizing channel
created: 2026-09-14
related: [WP-004, WP-030, WP-293, WP-294, WP-295]
prior_art:
  - classical regular-representation/semigroup-algebra commutant principle for a commutative free multiplicative monoid
  - Hedenmalm, Lindqvist, and Seip (1997), Hardy-Hilbert/Bohr realization of Dirichlet series
---

# WP-296 — Multiplicative-shift equivariance turns every linear nonlocal coupling back into Dirichlet convolution

## Claim

`WP-295` closes fixed positive **pointwise** multi-channel recovery: if a Hilbert-valued divisor convolution of the all-integer logarithmic carrier vanishes away from prime powers, then its visible kernel is one Möbius direction. One explicit boundary remained: perhaps a linear positive construction could mix different integer/log sites before scalarization and thereby escape the divisor-convolution classification.

For multiplicative-translation-equivariant linear couplings, it cannot.

Let `V,W` be complex Banach spaces and let

\[
\mathscr A(V):=V^{\mathbb N}
\]

carry the product topology. For `m>=1`, define the multiplicative shift

\[
(S_m f)(N)
:=
\begin{cases}
f(N/m),&m\mid N,\\
0,&m\nmid N.
\end{cases}
\tag{1}
\]

Let

\[
T:\mathscr A(V)\to\mathscr A(W)
\]

be continuous and linear and suppose

\[
T S_m=S_m T
\qquad(m\ge1).
\tag{2}
\]

Then there is a unique operator-valued arithmetic kernel

\[
K(d)\in\mathcal L(V,W)
\]

such that

\[
\boxed{
(Tf)(N)=\sum_{d\mid N}K(d)f(N/d).
}
\tag{3}
\]

Thus every coefficientwise-continuous linear coupling that is intrinsic under multiplicative translation is already an operator-valued Dirichlet convolution. It may be highly nonlocal in the integer/log coordinate, but its nonlocality has exactly the convolution form already exposed by the arithmetic source.

Finite cascades do not enlarge the class. If `T_1,...,T_r` are equivariant linear channel maps, their composition has the single effective kernel

\[
K_{\rm eff}=K_r*\cdots*K_1,
\tag{4}
\]

where convolution uses composition of the channel operators. Hence any finite linear equivariant network applied to the scalar logarithmic carrier

\[
L(N)=\log N
\tag{5}
\]

reduces to one Hilbert-valued convolution

\[
F=A*L.
\tag{6}
\]

If a fixed faithful Hilbert norm, or a fixed positive-semidefinite channel form after quotienting its nullspace, is then required to produce exactly the finite Weil selector

\[
\frac{\Lambda(N)}{\sqrt N},
\tag{7}
\]

`WP-295` applies to the effective visible kernel and forces

\[
\boxed{
F(N)=u\Lambda(N),
\qquad
A(N)=u\mu_{\rm Mob}(N)
}
\tag{8}
\]

for one fixed visible channel vector `u` (unit when (7) is normalized exactly). On the Dirichlet-series side the visible transfer therefore contains the reciprocal-zeta factor `1/zeta(s)` again. Linear nonlocal mixing has not removed the signed inverse or its zero screen; equivariance has merely hidden the same Möbius kernel inside an operator network.

**Classification:** `EXACT-DERIVED + MULTIPLICATIVE-SHIFT-COMMUTANT + OPERATOR-VALUED-DIRICHLET-CONVOLUTION + FINITE-DEPTH-COLLAPSE + WP-295-MOBIUS-RIGIDITY + NONLOCAL-EQUIVARIANT-ROUTE-CLOSURE + GENERALIZED-PRIME-GENERIC + NOT-A-GLOBAL-WEIL-POSITIVITY-PROOF`.

## 1. The commutant calculation is exact

For `n>=1` and `v in V`, let `e_n v` denote the sequence supported only at `n`, with value `v` there. Since

\[
e_n v=S_n(e_1 v),
\tag{9}
\]

equivariance gives

\[
T(e_n v)=S_nT(e_1 v).
\tag{10}
\]

Define

\[
K(d)v:=[T(e_1v)](d).
\tag{11}
\]

Linearity gives a linear operator `K(d):V->W`; continuity of `T` in the product topology makes each coordinate map continuous, hence `K(d) in L(V,W)`.

For a finitely supported sequence

\[
f=\sum_n e_n f(n),
\]

(10) yields, at coordinate `N`,

\[
\begin{aligned}
(Tf)(N)
&=\sum_n [S_nT(e_1f(n))](N)\\
&=\sum_{n\mid N}K(N/n)f(n)\\
&=\sum_{d\mid N}K(d)f(N/d).
\end{aligned}
\tag{12}
\]

Finitely supported sequences are dense in the product topology. Both sides of (12) are continuous coefficientwise, and for each fixed `N` the divisor sum is finite. Therefore (12) extends to every `f in A(V)`, proving (3).

Uniqueness is immediate from (11). Conversely every map of the form (3) commutes with every `S_m`, because multiplication of positive integers is commutative and both iterated divisor sums enumerate the same factorizations. Thus (3) is not merely a representation of examples: it is the full continuous linear commutant of the multiplicative shifts.

The continuity hypothesis is the exact category gate. Without any regularity at all, pathological linear maps on the full infinite product can depend on non-coordinatewise Hamel data. Such maps are not source-native coefficientwise operators and provide no canonical geometric mechanism. Bounded operators on the usual Hardy/Dirichlet-series Hilbert realizations lie on the regular side of this gate; boundedness further restricts which kernels are admissible but does not create a different equivariant algebra.

## 2. Multi-channel and finite-depth nonlocality collapses before positivity

The same argument works when the input and output already have channels. Suppose

\[
T_j:\mathscr A(V_{j-1})\to\mathscr A(V_j)
\]

has kernel `K_j(d) in L(V_{j-1},V_j)`. For two layers,

\[
\begin{aligned}
(T_2T_1f)(N)
&=\sum_{a\mid N}K_2(a)(T_1f)(N/a)\\
&=\sum_{ab\mid N}K_2(a)K_1(b)f(N/(ab)).
\end{aligned}
\tag{13}
\]

Grouping by `d=ab` gives another kernel

\[
(K_2*K_1)(d)
=\sum_{ab=d}K_2(a)\circ K_1(b).
\tag{14}
\]

Iteration proves (4). The architecture may therefore have arbitrarily many finite linear channels and mix values from many multiplicatively related sites, but as long as each layer respects the same source translation symmetry, the whole network has one effective arithmetic kernel.

For a scalar source, choose a fixed input vector if necessary and define

\[
A(d):=K_{\rm eff}(d)(1).
\tag{15}
\]

Then the output on the logarithmic carrier is exactly (6). At this point there is no remaining architectural distinction for the support problem: `WP-295` sees only the effective Hilbert-valued kernel `A` and already classifies it.

This also rules out an apparent operator-valued escape from `WP-293`. Operator-valued intermediate states matter only if some later operation uses information that is not reducible to the fixed visible Hilbert channel. If the endpoint is a fixed positive quadratic channel form at each `N`, factor that form through its Hilbert quotient first; the visible composite remains of the form (6), and (8) follows.

## 3. Exact finite Weil support therefore restores the signed inverse

Assume the visible output is measured by a fixed Hilbert norm and satisfies

\[
\|F(N)\|
=
\Lambda(N)
\qquad(N\ge2).
\tag{16}
\]

Then `F(N)=0` at every mixed-prime integer. `WP-295` needs only this support vanishing to force

\[
F=u\Lambda,
\qquad
A=u\mu_{\rm Mob}.
\tag{17}
\]

The norm values in (16) merely normalize `||u||=1`.

Equivalently, if one works with Dirichlet transforms in a half-plane where the relevant series converge, (17) reads formally

\[
\mathcal D A(s)=\frac{u}{\zeta(s)}.
\tag{18}
\]

Thus the nontrivial-zero divisor has not been removed by nonlocal channel transport. It has reappeared as the transfer function forced by exact prime-power localization. This is precisely the source-side obstruction the line is trying not to import by hand: positivity of the final channel norm does not make the inverse kernel positive or geometrically independent of the zeta zero screen.

Combining this with `WP-294` gives the same conclusion when exact coefficient recovery is not postulated directly but the resulting scalar atomic finite-place distribution is required to agree with the canonical finite Weil term on the full autocorrelation-square test class. Exact square equality first forces equality of the underlying finite distribution; the present commutant reduction then forces that any linear multiplicative-equivariant nonlocal recovery realizing it is Möbius on its visible subspace.

## 4. Matched escape: the canonical axis selector breaks equivariance

The obstruction is not a disguised claim that no non-convolutional linear selector can recover `Lambda`. `WP-004` supplies an exact intrinsic counter-control.

There the Prime-Lattice projection

\[
Q=\mathbf 1_{\{1\}}(R)
\tag{19}
\]

keeps precisely the one-prime-coordinate axes, and

\[
QAN^{-1}Q
\]

acts by `Lambda(n)`. But `Q` is not multiplicative-shift equivariant. For distinct primes `p` and `q`,

\[
Q S_q e_p=Qe_{pq}=0,
\qquad
S_qQe_p=S_qe_p=e_{pq}.
\tag{20}
\]

So

\[
[Q,S_q]\ne0.
\tag{21}
\]

This is a useful matched control: breaking the multiplicative translation symmetry can genuinely select prime-power support without Möbius inversion. The price is exactly the one already identified in `WP-004`: the axis projection is generic free-prime geometry and has no intrinsic archimedean/global sign completion; Beurling-prime systems possess the same selector while violating the Riemann zero geometry.

Therefore the surviving distinction is sharper than “local versus nonlocal.” The load-bearing question is whether the operation breaks source translation symmetry in a canonical way that also carries genuinely global arithmetic information.

## 5. Generalized-prime control

The commutant proof uses only the free commutative multiplicative-semigroup law and coefficientwise regularity. Replace the ordinary primes by any free generalized-prime set and the same argument identifies equivariant linear maps with convolution by a kernel on that monoid. If there are at least three independent generators, the support-rigidity argument of `WP-295` then applies verbatim after replacing the logarithmic axis weights by any nonzero generator weights.

Hence the combined no-go survives the line's strongest clone control:

\[
\boxed{
\text{linear multiplicative-equivariant nonlocality}
+\text{ exact prime-power support}
\Longrightarrow
\text{the same signed inverse architecture}
}
\tag{22}
\]

on ordinary and generalized-prime systems alike. The result closes a representation class; it supplies no arithmetic distinction capable of implying RH.

## 6. Prior-art and novelty audit

The operator-algebra statement by itself is classical in mechanism. Equation (3) is the commutant calculation for the regular representation of a commutative semigroup: an equivariant linear operator is convolution by its response to the identity basis vector. In the analytic Dirichlet-series setting, the Bohr/Hardy realization and multiplication by Dirichlet-series symbols are standard; the Hedenmalm--Lindqvist--Seip framework already anchors that representation in this research line. A bounded literature audit of modern Hardy-space multiplier work found refinements of the admissible multiplier classes, norms and spectra, not a distinct source-equivariant linear operation that evades convolution.

Accordingly, no novelty is claimed for the commutant theorem itself. The Mathia-specific delta is the **composition with `WP-295`**: the nonlocal linear escape explicitly left open there collapses whenever “source-native” is made precise as multiplicative-shift equivariance. Exact finite Weil localization then forces the same Möbius transfer even after arbitrary finite channel depth.

This is stronger than merely saying that a proposed kernel happened to be convolutional. It identifies the structural hypothesis that forces convolution and shows exactly which symmetry a genuinely different construction must violate.

## 7. Boundary of the no-go

The result does **not** close arbitrary nonlocal geometry.

**Boundary-conditioned or site-dependent maps.** Operators whose rule changes with `N`, with a boundary state, with occupied-prime rank, or with global geometry need not commute with `S_m`. `WP-004` is the concrete example. Such symmetry breaking must still be intrinsic rather than a mask chosen to encode `Lambda`.

**Nonlinear upstream geometry.** Rank, determinant, exterior-power, minimization or other nonlinear operations formed before scalarization are outside the linear commutant theorem. `WP-030` remains a representative support-sensitive nonlinear mechanism. Exact final Weil equality still faces the target-side linearization gates of `WP-288`/`WP-294`.

**Infinite or singular limits.** A limit of equivariant bounded layers remains equivariant when it converges in a topology in which the shifts and limit are compatible, but singular domain changes can evade that passage. Any such proposal must state its domain and show that the singular limit is canonical rather than a zero-coded regularization.

**Archimedean/global coupling.** Nothing here manufactures the Gamma term, pole counterterms, or an independent global sign theorem. A finite-place map may deliberately break multiplicative shift symmetry because an archimedean boundary couples to it; that is outside the theorem and is exactly the kind of extra structure the line seeks.

## Consequence for the search

The open frontier after `WP-295` can now be narrowed. Merely replacing pointwise divisor convolution by a **linear nonlocal network across multiplicatively related log sites** is not a new architecture if the network remains source-translation equivariant. Its full visible action is one Dirichlet convolution and exact Weil localization forces Möbius again.

A viable nonlocal route must therefore obtain its arithmetic information from a source-forced violation of that equivariance, from nonlinear support-sensitive geometry before scalarization, or from a genuinely finite--archimedean/global coupling whose boundary structure changes the operator class. It must then still explain the final Weil sign independently and survive generalized-prime controls.