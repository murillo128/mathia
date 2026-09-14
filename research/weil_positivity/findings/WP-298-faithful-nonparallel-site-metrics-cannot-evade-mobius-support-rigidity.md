---
id: WP-298
title: Faithful nonparallel site metrics cannot evade Möbius support rigidity
branch: weil_positivity
status: supported
kind: site-dependent-positive-metric-support-no-go
claim_strength: exact classification of the faithful pointwise-metric escape inside the flat source-covariant linear class, with a nonfaithful programmable control
created: 2026-09-14
related: [WP-230, WP-293, WP-295, WP-296, WP-297]
prior_art:
  - classical identity mu * log = Lambda and Dirichlet-convolution algebra
  - E. D. Cashwell and C. J. Everett, The ring of number-theoretic functions, Pacific J. Math. 9 (1959), 975-985
  - Jean-Pierre Antoine and Camillo Trapani, Partial inner product spaces, metric operators and generalized hermiticity, J. Phys. A 46 (2013), 025204
---

# WP-298 — Faithful nonparallel site metrics cannot evade Möbius support rigidity

## Claim

`WP-297` proves that flat multiplicative boundary transport is gauge-trivial. It deliberately leaves one apparently broader escape open: even after the transport is gauged flat, perhaps the positive metric itself can vary with the arithmetic site in a **nonparallel** way and use that variation to erase mixed composites without exposing Möbius inversion.

For pointwise positive readout of the flat source-covariant linear response, nonparallelity alone does not help. The only way a varying positive metric can change exact support is through its **nullspace**.

Let `H` be a complex Hilbert space, let

\[
L(n)=\log n,
\qquad
A:\mathbb N\to H,
\qquad
B:=A*L.
\tag{1}
\]

After the flat gauge reduction of `WP-297`, allow an arbitrary invertible site map

\[
G(N)\in GL(H)
\tag{2}
\]

and write the transported response as

\[
F(N)=G(N)B(N).
\tag{3}
\]

At every site let `Q_N` be an arbitrary bounded positive-semidefinite operator on `H`. No parallelity, common basis, uniform coercivity, continuity in `N`, commutation relation, or bounded inverse is assumed. Define the positive scalar readout

\[
r_Q(N)
:=
\langle F(N),Q_NF(N)\rangle^{1/2}
=
\|Q_N^{1/2}F(N)\|.
\tag{4}
\]

Suppose the exact finite Weil coefficient is required:

\[
r_Q(N)=\Lambda(N)
\qquad(N\ge2).
\tag{5}
\]

If `Q_N` is **faithful at every mixed-composite site**, meaning

\[
\ker Q_N=\{0\}
\qquad
\text{whenever }N\ge2\text{ is not a prime power},
\tag{6}
\]

then there is one nonzero vector `u in H` such that

\[
\boxed{
B(N)=u\Lambda(N),
\qquad
A(N)=u\mu_{\rm Mob}(N)
\quad\text{for every }N.
}
\tag{7}
\]

At prime powers the site metrics can only normalize that already-forced direction:

\[
\boxed{
\langle G(p^k)u,
Q_{p^k}G(p^k)u\rangle=1
\qquad(p\text{ prime},\ k\ge1).
}
\tag{8}
\]

Thus arbitrary faithful nonparallel metrics do **not** provide a new arithmetic localization mechanism. Within this architecture they can reweight or rotate the surviving Möbius direction, but they cannot create the prime-power support.

More generally, for arbitrary possibly nonfaithful `Q_N`, define the transported nullspace

\[
K_N:=G(N)^{-1}\ker Q_N.
\tag{9}
\]

Then exact vanishing at a mixed composite is equivalent to

\[
\boxed{B(N)\in K_N.}
\tag{10}
\]

Consequently, if `A` is not of the form `u mu_Mob`, then exact finite Weil support forces at least one mixed-composite `K_N` to be nontrivial and to contain a nonzero unwanted response `B(N)`. In the pointwise metric class, **all support-selecting power beyond Möbius therefore resides in source-forced moving kernels/support projections, not in positive metric values on a faithful support**.

**Classification:** `EXACT-DERIVED + FLAT-GAUGE-REDUCED + SITE-DEPENDENT-PSD-METRIC + NO-PARALLELITY-ASSUMPTION + FAITHFUL-MIXED-SITE-RIGIDITY + PRIME-POWER-SUPPORT + UNIQUE-VISIBLE-MOBIUS-KERNEL + NONFAITHFUL-NULLSPACE-CLASSIFICATION + PROGRAMMABLE-DEGENERATE-CONTROL + GENERALIZED-PRIME-GENERIC + ROUTE-NARROWING + NOT-A-GLOBAL-WEIL-POSITIVITY-PROOF`.

## 1. Faithfulness turns zero positive energy back into vector support

For a positive operator,

\[
\langle v,Q_Nv\rangle
=
\|Q_N^{1/2}v\|^2,
\tag{11}
\]

so

\[
\langle v,Q_Nv\rangle=0
\quad\Longleftrightarrow\quad
v\in\ker Q_N.
\tag{12}
\]

If `N` is not a prime power, then `Lambda(N)=0`. Equations (5) and (12) give

\[
F(N)\in\ker Q_N.
\tag{13}
\]

Under (6), this means `F(N)=0`. Since `G(N)` is invertible,

\[
B(N)=0
\qquad
(N\text{ not a prime power}).
\tag{14}
\]

This step uses no comparison between different sites. In particular, the metrics may vary arbitrarily rapidly and need not be parallel under the transport. The argument depends only on the elementary fact that a faithful positive quadratic form has no nonzero zero-energy vector.

The boundedness of `Q_N` is merely a clean Hilbert-space formulation. The same support implication holds for a closed nonnegative quadratic form whenever the evaluated vector lies in its form domain and the form has trivial nullspace at the relevant mixed site.

## 2. Three-prime support rigidity then forces Möbius exactly

Equation (14) is precisely the hypothesis of `WP-295` for the Hilbert-valued Dirichlet convolution

\[
B=A*L.
\tag{15}
\]

That theorem needs no information about the prime-power magnitudes: on a free multiplicative monoid with at least three independent prime generators, vanishing of `A*L` at every mixed composite already forces

\[
B=u\Lambda,
\qquad
A=u\mu_{\rm Mob}
\tag{16}
\]

for one fixed vector `u`. This proves (7).

Now let `N=p^k`. By (3) and (16),

\[
F(p^k)
=(\log p)G(p^k)u.
\tag{17}
\]

Substituting in the exact readout (5), and using `Lambda(p^k)=log p>0`, gives

\[
(\log p)
\langle G(p^k)u,Q_{p^k}G(p^k)u\rangle^{1/2}
=
\log p,
\tag{18}
\]

which is exactly (8). Hence the site dependence that survives after support rigidity is only a unit normalization along one common arithmetic direction. It does not supply new prime-power amplitudes, mixed-prime cancellation, or a new sign theorem.

The same argument applies to the critical half-density normalization. If the readout is instead

\[
\frac{r_Q(N)}{\sqrt N}
=
\frac{\Lambda(N)}{\sqrt N},
\tag{19}
\]

then multiplication by `sqrt(N)` returns (5), so no extra freedom is hidden in the Weil half-density factor.

## 3. The exact nonfaithful escape is a moving nullspace

Dropping faithfulness does not invalidate the pointwise classification. From (12)--(13), at every mixed site

\[
B(N)\in G(N)^{-1}\ker Q_N=K_N,
\tag{20}
\]

and conversely (20) is sufficient for the positive readout to vanish there. Thus the metric eigenvalues away from zero are irrelevant to exact support deletion. Only the kernel matters.

This gives a useful contrapositive of `WP-295`. Suppose exact Weil support holds but `A` is not a single Möbius direction. If `B(N)` vanished at every mixed composite, `WP-295` would force `A=u mu_Mob`, contrary to hypothesis. Therefore there exists a mixed composite `N` with

\[
B(N)\ne0,
\qquad
B(N)\in K_N,
\tag{21}
\]

so `K_N` is nontrivial. Any genuine non-Möbius escape in this class must therefore explain **why the source geometry canonically creates the required null directions at exactly the sites where unwanted mixed-prime response occurs**.

This is stronger than saying that a varying metric must be nonparallel. A metric can be arbitrarily nonparallel while remaining faithful, and then (14)--(16) still apply. The first pointwise metric datum capable of changing arithmetic support is degeneracy.

## 4. Degenerate metrics can program the answer even in one dimension

The nullspace escape is mathematically real but, without an independent source law, completely programmable. A scalar matched control makes this explicit.

Take

\[
H=\mathbb C,
\qquad
G(N)=1,
\qquad
A=\delta_1.
\tag{22}
\]

Then

\[
B(N)=(A*L)(N)=\log N.
\tag{23}
\]

For `N>=2`, define the scalar positive metric

\[
Q_N
=
\left(\frac{\Lambda(N)}{\log N}\right)^2.
\tag{24}
\]

This satisfies `0<=Q_N<=1`; it is zero at every mixed composite and equals `1/k^2` at `N=p^k`. Nevertheless

\[
\sqrt{Q_N}\,|B(N)|
=
\Lambda(N)
\tag{25}
\]

exactly.

So allowing arbitrary sitewise kernels makes exact Mangoldt support trivial to manufacture without Möbius inversion. The arithmetic content has simply been moved into the zero set of `Q_N`. Such a construction cannot count as an intrinsic positivity mechanism unless the kernel pattern is derived independently from Mathia geometry and survives the mandate's matched controls.

This control also prevents a misleading interpretation of (10): a moving nullspace is a **necessary escape from the faithful no-go**, not positive evidence for a Weil bridge.

## 5. Relation to `WP-230`: support rigidity rather than inertia rigidity

`WP-230` proves a related but distinct faithful-metric theorem for the already-formed Bost--Connes finite Weil defect. There the issue is sign: a faithful positive congruence has dense range and cannot remove the strict positive and negative directions of an indefinite operator; a nonfaithful metric repairs sign only by support compression.

The present result acts one stage earlier and answers a different question. Here the target is exact **arithmetic support** before the global Weil lift. A faithful pointwise metric cannot turn a nonzero mixed-composite vector into zero energy, so the response itself must be prime-power supported; `WP-295` then forces the signed Möbius inverse. Nonfaithfulness again becomes support selection, but now its support must track arithmetic sites and unwanted response directions.

The recurrence of the same faithful-versus-support boundary in two different categories is informative, but no abstract novelty is claimed for the operator fact behind it. Positivity identities such as (11), positive metric operators, and Dirichlet-convolution algebra are classical. Antoine--Trapani is a standard metric-operator reference, and Cashwell--Everett is a classical arithmetic-convolution reference. A bounded literature audit around positive metric operators, site-dependent quadratic forms, Dirichlet convolution, Möbius inversion, and von Mangoldt support did not reveal a published theorem in this exact arithmetic formulation. The Mathia-specific delta is the composition of the flat-gauge reduction of `WP-297` with the three-prime support theorem of `WP-295` to close a route that those findings explicitly left open.

## 6. Generalized-prime control and the Riemann-specific burden

Nothing in the faithful-support argument distinguishes ordinary primes. `WP-295` already proves the support theorem on every free generalized-prime monoid with at least three generators and nonzero logarithmic weights. The positive identity (11) is completely arithmetic-blind. Therefore the same conclusion holds in those matched clones:

\[
\text{faithful pointwise site metrics}
\Longrightarrow
\text{prime-power support of the vector response}
\Longrightarrow
\text{one Möbius direction}.
\tag{26}
\]

A surviving degenerate-metric construction must consequently do more than exhibit a clever kernel. It must derive a moving kernel from structure that is specific to the Riemann system, explain why the analogous kernel is absent or ineffective in generalized-prime controls, and do so before the desired Mangoldt support is read off.

## 7. Aggressive falsification and exact boundary

The theorem is intentionally narrow enough not to hide genuine category changes.

It does **not** cover non-flat transport with nontrivial prime-diamond holonomy, because then the reduction to one fixed convolutional response `A*L` can fail. It does not cover extra boundary vertices or orbits not generated from the rooted multiplicative action. It does not cover a source-forced moving kernel whose degeneracy is itself new arithmetic geometry. It also does not cover a genuinely nonlocal positive form coupling different arithmetic sites before scalarization, nonlinear support-sensitive geometry formed upstream, or a nonseparable finite--archimedean construction that changes the object before any pointwise local readout.

Conversely, merely allowing poor conditioning, eigenvalues tending to zero, arbitrary basis rotation, noncommutation between `Q_N` and transport, or complete failure of metric parallelity does **not** leave the theorem as long as the mixed-site forms remain faithful. Exact zero support is insensitive to how small a positive eigenvalue is; it changes only when an actual null direction appears.

Finally, even a source-forced degenerate kernel would solve only the localization gate. The research mandate still requires one intrinsic global structure that also produces the archimedean and polar terms under checked normalization and whose final nonnegativity follows from an independent geometric theorem rather than from RH or inserted zero data. Nothing here supplies that global sign.

## Consequence for `weil_positivity`

The post-`WP-297` boundary can be sharpened from

\[
\text{“use a source-forced nonparallel site metric”}
\]

to

\[
\boxed{
\text{faithful nonparallel metric}
\Longrightarrow
\text{no new support selection};
\qquad
\text{non-Möbius pointwise escape}
\Longrightarrow
\text{source-forced moving nullspace}.
}
\tag{27}
\]

So nonparallelity by itself is not the missing mixed-prime geometry. In the flat source-covariant linear class, the next pointwise metric candidate must expose a canonical, gauge-invariant degeneracy pattern before positivity is scalarized. Otherwise the search must move to the genuinely non-flat, topological, nonlinear, nonlocal, or finite--archimedean categories already isolated by `WP-297`.

This is a route narrowing, not a proof of Weil positivity or RH.