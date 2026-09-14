---
id: WP-299
title: Source-equivariant linear response lives in the holonomy-fixed sector
branch: weil_positivity
status: supported
kind: curved-transport-intertwiner-no-go
claim_strength: exact selection rule showing that commuting multiplicative source shifts force every linearly equivariant response into the common fixed sector of prime-diamond holonomy; scalar projective curvature is therefore trivial on any nonzero exact Mangoldt channel
created: 2026-09-14
related: [WP-004, WP-295, WP-296, WP-297, WP-298]
prior_art:
  - standard intertwiner principle for commuting representations and projective representations
  - A. Kleppner, Multipliers on Abelian Groups, Math. Ann. 158 (1965), 11-34, DOI 10.1007/BF01370393
  - K. G. Wilson, Confinement of quarks, Phys. Rev. D 10 (1974), 2445-2459, DOI 10.1103/PhysRevD.10.2445
---

# WP-299 — Source-equivariant linear response lives in the holonomy-fixed sector

## Claim

`WP-297` shows that a flat multiplicative boundary connection is pure gauge, and `WP-298` shows that arbitrary faithful site metrics on that flat response cannot change exact prime-power support. The cleanest linear escape left by those results is to make the boundary connection genuinely non-flat, so that distinct prime directions have nontrivial diamond holonomy before positivity is formed.

For an exactly source-equivariant **linear** response, curvature in the output connection cannot act on the source-generated sector.

Let `H_n` be complex vector spaces indexed by positive integers. For every prime `p`, let

\[
C_p(n):H_n\longrightarrow H_{pn}
\tag{1}
\]

be invertible linear transport. No cocycle or flatness relation is assumed. On sections `h=(h(n))_n`, define the prime shift

\[
(U_p h)(N)
=
\begin{cases}
C_p(N/p)h(N/p),&p\mid N,\\
0,&p\nmid N.
\end{cases}
\tag{2}
\]

Let the scalar source carry the ordinary multiplicative shifts `S_p` of `WP-296`, and let

\[
T:\mathscr A(\mathbb C)\longrightarrow \prod_{n\ge1}H_n
\tag{3}
\]

be linear and exactly equivariant prime by prime,

\[
\boxed{T S_p=U_pT\qquad\text{for every prime }p.}
\tag{4}
\]

Since the source shifts commute, every pair of output shifts commutes **on the image of `T`**:

\[
\boxed{[U_p,U_q]\,T=0\qquad(p\ne q).}
\tag{5}
\]

Equivalently, at every base site `n`, every source-generated vector

\[
v=(Tf)(n)\in H_n
\tag{6}
\]

lies in the equalizer of the two prime-diamond transports,

\[
C_p(qn)C_q(n)v
=
C_q(pn)C_p(n)v.
\tag{7}
\]

Writing the plaquette holonomy based at `n` as

\[
\mathcal K_{p,q}(n)
:=
\bigl[C_q(pn)C_p(n)\bigr]^{-1}
C_p(qn)C_q(n),
\tag{8}
\]

one has the exact selection rule

\[
\boxed{
(Tf)(n)\in
\bigcap_{p\ne q}\operatorname{Fix}\mathcal K_{p,q}(n)
\qquad\text{for every }f,n.
}
\tag{9}
\]

Thus non-flat curvature may exist in the ambient fibers, but it can only live on directions not reached by the commuting source representation. The source-generated subrepresentation is flat in the only sense relevant to a linear intertwiner: the `U_p` commute on it.

There is a sharp scalar/projective corollary. If at some site

\[
\mathcal K_{p,q}(n)=\omega_{p,q}(n)I
\tag{10}
\]

with `omega != 1`, then

\[
(Tf)(n)=0
\qquad\text{for every }f.
\tag{11}
\]

If `T` is coefficientwise continuous and its response to the logarithmic source satisfies the required nonzero prime values

\[
(TL)(p)\ne0
\qquad\text{for every prime }p,
\tag{12}
\]

then the root channel is nonzero and invertible transport propagates a nonzero source-generated vector to every site. Consequently **every scalar prime-diamond holonomy is forced to be trivial at every base site**. A `U(1)`/scalar magnetic curvature therefore cannot be the missing linear mixed-prime mechanism for exact Mangoldt recovery.

For unitary transports there is a second useful corollary. Any positive operator constructed only from the local plaquette holonomies by a fixed unital `*`-polynomial or norm-limit thereof restricts on the source-generated sector to its value at the trivial holonomy. Standard positive curvature energies such as

\[
(I-\mathcal K)^*(I-\mathcal K)
\tag{13}
\]

vanish there. Nontrivial holonomy eigenvalues can contribute only through an ambient sector that the exact linear source map does not reach.

**Classification:** `EXACT-DERIVED + NONFLAT-OUTPUT-CONNECTION + COMMUTING-SOURCE-INTERTWINER + HOLONOMY-FIXED-SECTOR + PROJECTIVE-SCALAR-CURVATURE-EXCLUSION + HOLONOMY-ENERGY-INVISIBLE-ON-SOURCE + SHARP-CURVED-AMBIENT-CONTROL + GENERALIZED-PRIME-GENERIC + LINEAR-CURVATURE-ROUTE-NARROWING + NOT-A-GLOBAL-WEIL-POSITIVITY-PROOF`.

## 1. Commuting source shifts impose a curvature selection rule

For distinct primes `p,q`, the ordinary multiplicative source shifts satisfy

\[
S_pS_q=S_qS_p.
\tag{14}
\]

Using (4),

\[
U_pU_qT
=
TS_pS_q
=
TS_qS_p
=
U_qU_pT,
\tag{15}
\]

which is exactly (5). No topology, norm, positivity, arithmetic coefficient, or RH input is used.

Evaluate (15) at the coordinate `pqn`. From (2),

\[
(U_pU_qTf)(pqn)
=
C_p(qn)C_q(n)(Tf)(n),
\tag{16}
\]

whereas

\[
(U_qU_pTf)(pqn)
=
C_q(pn)C_p(n)(Tf)(n).
\tag{17}
\]

Equality gives (7). Invertibility of the second path gives (9).

This is the precise obstruction to using ordinary output curvature as the new information while retaining exact linear source covariance. The source is a representation of a commutative monoid. An intertwiner from it cannot populate a sector on which the corresponding output generators fail to commute.

Define the source-reachable section space

\[
\mathcal R:=\operatorname{im}T.
\tag{18}
\]

Equation (4) makes `R` invariant under every `U_p`, and (5) gives

\[
U_pU_q|_{\mathcal R}
=
U_qU_p|_{\mathcal R}.
\tag{19}
\]

So the ambient connection may be curved, but its restriction to the actual linear response representation is flat. The curvature is not forbidden; it is **representation-theoretically decoupled from the source image**.

## 2. Scalar/projective curvature is incompatible with a nonzero reachable fiber

Suppose (10) holds. Combining it with (9),

\[
\omega_{p,q}(n)(Tf)(n)=(Tf)(n)
\tag{20}
\]

for every `f`. If `omega != 1`, (11) follows.

This local statement becomes global for the exact arithmetic channel. Assume now that `T` is continuous for the product topology, as in `WP-296`, and put

\[
a(n):=[T e_1](n).
\tag{21}
\]

For a prime `p`, equivariance gives

\[
T e_p
=
T S_p e_1
=
U_p T e_1.
\tag{22}
\]

At coordinate `p`,

\[
[T e_p](p)=C_p(1)a(1).
\tag{23}
\]

The coordinate map `f -> (Tf)(p)` is continuous, so it is determined by finitely many input coordinates. Equivariance also implies `T e_m` has no coordinate below the multiplicative shift `m`; in particular, at a prime coordinate only `e_1` and `e_p` can contribute. Since `L(1)=0`,

\[
(TL)(p)
=
(\log p)C_p(1)a(1).
\tag{24}
\]

Hence any required nonzero prime response forces

\[
a(1)\ne0.
\tag{25}
\]

Now choose any integer `n` and any prime factorization path from `1` to `n`. Repeatedly applying (4) to `e_1` transports `a(1)` along that path to the `n`-coordinate of `T e_n`. Every link is invertible, so this vector is nonzero. Thus the reachable fiber

\[
\mathcal R_n
:=
\{(Tf)(n):f\in\mathscr A(\mathbb C)\}
\tag{26}
\]

is nonzero for every `n`.

If every plaquette holonomy is scalar as in (10), (9) then forces

\[
\boxed{\omega_{p,q}(n)=1
\qquad\text{for every }n,\ p\ne q.}
\tag{27}
\]

The conclusion does not depend on the mixed-composite zeros of `Lambda`; the nonzero prime coefficients already activate the root channel, and exact source covariance propagates a nonzero reachable direction everywhere. Scalar curvature therefore cannot be placed only on the unwanted mixed sites without contradicting equivariance.

The same argument applies to a projective output representation with a scalar multiplier. If

\[
U_pU_q=\omega_{p,q}U_qU_p
\tag{28}
\]

and `omega_{p,q} != 1`, then (5) and injectivity of the twisted shifts imply `T=0`. This is the standard projective-representation obstruction in its simplest form.

## 3. Nonabelian curvature survives only on source-unreachable directions

For operator-valued holonomy, (9) does not force `K=I` on the entire ambient fiber. It forces only

\[
\mathcal R_n
\subseteq
\operatorname{Fix}\mathcal K_{p,q}(n).
\tag{29}
\]

This distinction is essential. A connection can have genuine nontrivial curvature on a complementary sector while carrying an ordinary flat source representation on its fixed sector.

If the reachable fiber is all of `H_n`, then (29) immediately gives

\[
\mathcal K_{p,q}(n)=I.
\tag{30}
\]

More generally, every source-generated local vector sees identity holonomy. Therefore a proposed nonabelian curvature mechanism must answer a sharper question than “is the ambient plaquette holonomy nontrivial?” It must explain how the arithmetic response reaches a curvature-sensitive sector without violating the commuting source action that defined the equivariant linear map.

This is exactly where a genuinely new source incidence would have to enter. If the source itself carried a compatible projective/curved action, then the two sides of the intertwining relation could share the same multiplier. But that would be new upstream geometry, not curvature manufactured only in the output bundle.

## 4. Ordinary positive holonomy energies vanish or become scalar on the reachable sector

Assume the transports are unitary, so every `K_{p,q}(n)` is unitary. Let `v in R_n`. By (9),

\[
\mathcal K_{p,q}(n)v=v
\tag{31}
\]

for every prime pair. Unitarity also gives

\[
\mathcal K_{p,q}(n)^*v=v.
\tag{32}
\]

Therefore every word in the local holonomies and their adjoints acts as the identity on `v`. For any fixed `*`-polynomial `P`,

\[
P(\mathcal K_1,\mathcal K_1^*,\ldots,\mathcal K_r,\mathcal K_r^*)v
=
P(1,1,\ldots,1)v.
\tag{33}
\]

The same statement extends by norm closure to the unital `C^*`-algebra generated by a finite family of such holonomies.

In particular, the standard nonnegative plaquette defect

\[
Q_{\mathcal K}:=(I-\mathcal K)^*(I-\mathcal K)\succeq0
\tag{34}
\]

satisfies

\[
Q_{\mathcal K}v=0
\qquad(v\in\mathcal R_n).
\tag{35}
\]

Likewise a fixed positive class function of unitary holonomy restricts to its value at `1`; the nontrivial spectrum of the curvature is invisible on the source-generated channel.

This does not exclude a separately supplied site metric whose coefficients depend on `n`, on a boundary variable, or on extra finite--archimedean data. But then the sign/support mechanism resides in that extra metric or degeneracy, not in the ordinary holonomy energy itself. `WP-298` already shows how quickly arbitrary moving kernels become programmable if their source law is not independently derived.

## 5. Sharp control: exact Mangoldt response can coexist with ambient curvature, but only in a flat sector

The theorem must not be misread as saying that a curved ambient connection is impossible.

Take every fiber to be

\[
H_n=\mathbb C^3
=
\mathbb C e_0\oplus\mathbb C^2.
\tag{36}
\]

For two distinguished primes `p,q`, let the link transports be site-independent unitaries

\[
C_p=1\oplus X,
\qquad
C_q=1\oplus Z,
\tag{37}
\]

where

\[
X=
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
Z=
\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\tag{38}
\]

Take all other prime transports to act as identity on the complementary two-dimensional sector. Since `XZ=-ZX`, the `p,q` plaquette holonomy is

\[
\boxed{\mathcal K_{p,q}=1\oplus(-I_2).}
\tag{39}
\]

The ambient bundle is genuinely non-flat, with fixed space exactly `C e_0`.

Now define the coefficientwise-continuous linear map

\[
(Tf)(N)
=
e_0\,(\mu_{\rm Mob}*f)(N).
\tag{40}
\]

Because every link transport fixes `e_0` and Dirichlet convolution commutes with the ordinary multiplicative shifts,

\[
TS_r=U_rT
\tag{41}
\]

for every prime `r`. On the logarithmic source,

\[
\boxed{(TL)(N)=e_0\Lambda(N).}
\tag{42}
\]

So exact Mangoldt localization and nontrivial ambient curvature can coexist. But the curvature has contributed nothing: the entire arithmetic response lives in the flat fixed line, and the visible transfer is still the Möbius kernel of `WP-295`--`WP-296`.

This matched control makes the boundary exact. The theorem does not rule out ambient curvature; it rules out counting that curvature as the source of a linearly equivariant arithmetic response when the response never leaves its fixed sector.

## 6. Relation to `WP-297` and `WP-298`

`WP-297` assumed the full output connection was flat and then gauged it globally to ordinary Dirichlet convolution. The present result removes that flatness assumption at the first representation-theoretic gate. Even when the ambient connection is non-flat, an exact intertwiner from the commuting multiplicative source automatically factors through a subrepresentation on which the prime shifts commute.

This does not literally reduce every curved bundle to the fixed-fiber hypotheses of `WP-297`: reachable fiber dimensions can vary, and the embedding of the commuting subrepresentation into the ambient bundle can carry additional boundary data. What is closed is narrower and cleaner:

\[
\boxed{
\text{ambient non-flat transport alone}
+
\text{exact linear source equivariance}
\not\Rightarrow
\text{curvature-sensitive arithmetic response}.
}
\tag{43}
\]

Any remaining support-selection power must come from something beyond the nontrivial holonomy eigenvalues themselves: a source-forced moving reachable subspace, a source-forced degenerate metric/nullspace, explicit covariance breaking, nonlinear upstream geometry, extra boundary orbits, or a finite--archimedean construction that changes the source action before the linear intertwiner is applied.

That boundary aligns with `WP-298`. There, after a flat gauge reduction, exact support could differ from Möbius only through a moving nullspace. Here, before any flat gauge reduction, nontrivial curvature can survive only outside the source-generated sector. Turning the **location of that sector** or a curvature-derived degeneracy into the selector is a new moving-subspace mechanism and must be justified independently; curvature as a bare plaquette defect does not supply it.

## 7. Generalized-prime control and prior-art audit

Nothing in (14)--(19) uses ordinary prime values. The proof uses only that the source action is a free commutative multiplicative action and that `T` intertwines it with the output prime shifts. The same fixed-sector theorem therefore holds for every free generalized-prime monoid.

This clone invariance is decisive for interpretation. The selection rule is a representation constraint, not Riemann-specific arithmetic. A surviving curved construction must introduce source data that distinguish the ordinary-prime system from generalized-prime controls before claiming relevance to global Weil positivity.

The abstract ingredients are classical. Intertwiners preserve algebraic relations of the source representation. Projective representations of abelian groups and their multipliers are classical; Kleppner's 1965 treatment is a standard anchor for the multiplier side. Plaquette holonomy as discrete curvature is classical lattice gauge theory, with Wilson's 1974 construction the canonical reference. No novelty is claimed for either fact.

The Mathia-specific content is their exact composition with the current route boundary. `WP-296` closed commuting nonlocal linear couplings, `WP-297` left non-flat prime-diamond transport as the cleanest linear escape, and `WP-298` showed that faithful metric variation alone cannot select the support. The present result shows that **merely putting curvature into the output connection still does not expose new arithmetic information to an exact linear source intertwiner**: the source image is automatically confined to the holonomy-fixed sector.

A bounded prior-art audit around projective representations of abelian groups, multiplier commutators, and lattice plaquette holonomy found the underlying algebraic mechanisms to be standard, not a published Riemann-specific positivity theorem. Accordingly this finding is a route closure, not a claim of a new general representation theorem.

## Consequence for `weil_positivity`

The current linear frontier can be narrowed again. After `WP-296`--`WP-298`, it is not enough to demand a nontrivial prime-diamond holonomy in an ambient boundary bundle. If the arithmetic source still carries the ordinary commuting multiplicative shifts and the response map is exactly linear and equivariant, then the source-generated sector is automatically holonomy-flat. Scalar/projective curvature is excluded outright from every nonzero exact Mangoldt channel, and ordinary positive holonomy energies see only the trivial holonomy on the reachable sector.

A viable curvature route must therefore make the **source action itself** genuinely relational before the intertwiner: for example a source-forced projective/curved incidence with a matching multiplier, a canonical violation of multiplicative shift covariance, a nonlinear operation before scalarization, or a nonseparable finite--archimedean construction whose global geometry changes the representation class. It must still recover the exact finite and archimedean Weil normalization, survive generalized-prime controls, and obtain final nonnegativity from an independent geometric theorem.

This is a substantive closure of the simplest non-flat linear escape, not a proof of global Weil positivity or RH.
