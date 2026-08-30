# PC-064 — compatible circle refinement is the classical adelic solenoid

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `PRIOR-ART-REDIRECTION` + `DECISIVE-NEGATIVE` for treating the canonical all-level compatible-circle completion itself as a new RH mechanism.

## Claim

PC-010 classifies the abstract roots-of-unity refinement tower as the classical cyclotomic/Bost–Connes object, while PC-059 identifies the finite-adic completion selected by the radial divisor-Haar basis with Haar measure on `\widehat{\mathbb Z}`. A natural remaining question is whether retaining the **ambient circle itself at every refinement level**, rather than only its torsion vertices, produces an intrinsic archimedean/finite-adic object not already present in classical arithmetic geometry.

Take one copy of `S^1` at each positive integer level and, for `m\mid n`, use the covering map already supplied by the roots-of-unity refinement geometry,

\[
p_{n,m}:S^1\to S^1,
\qquad
p_{n,m}(z)=z^{n/m}.
\]

The space of compatible lifts through all levels is

\[
\boxed{
\Sigma_{\mathbb Q}
=\varprojlim_{m\mid n}(S^1,p_{n,m}).
}
\]

This compact group is not a new prime-circle completion. It is exactly the **universal one-dimensional arithmetic solenoid**:

\[
\boxed{
\Sigma_{\mathbb Q}
\cong \widehat{\mathbb Q}
\cong (\mathbb R\times\widehat{\mathbb Z})/\mathbb Z
\cong \mathbb A_{\mathbb Q}/\mathbb Q,
}
\]

where `\widehat{\mathbb Q}` denotes the Pontryagin dual of the discrete additive rationals and `\mathbb A_{\mathbb Q}` is the additive adele group.

Moreover the projection to the level-one circle gives the exact compact-group extension

\[
\boxed{
0\longrightarrow\widehat{\mathbb Z}
\longrightarrow\Sigma_{\mathbb Q}
\longrightarrow S^1
\longrightarrow0.
}
\]

Thus the profinite space that appears in PC-059 has a direct geometric interpretation: it is the **transverse fiber over the common anchor** in the universal compatible refinement of the original circle. The ambient circle and the finite-adic fiber are indeed coupled nontrivially, but the coupling is the classical adelic solenoid, whose Fourier spectrum is the discrete group `\mathbb Q`.

This closes one specific escape left by PC-059: the canonical compatible refinement completion does not independently generate a new functional-equation or Hilbert–Pólya mechanism. Passing from it to Tate's functional equation requires the standard additional adelic data—analysis on the full self-dual additive adele group, the rational lattice and Poisson summation, together with multiplicative idele/Mellin structure. Those structures are classical and are not selected by the compact inverse limit alone.

## 1. Pontryagin duality gives the rational frequency group exactly

For one circle,

\[
\widehat{S^1}\cong\mathbb Z.
\]

Duality reverses the bonding arrows. If `m\mid n`, the dual of

\[
z\mapsto z^{n/m}
\]

is

\[
\mathbb Z\longrightarrow\mathbb Z,
\qquad
k\longmapsto\frac nm k.
\]

Therefore

\[
\widehat{\Sigma_{\mathbb Q}}
\cong
\varinjlim_{m\mid n}
\left(\mathbb Z,\ k\mapsto\frac nm k\right).
\]

At level `m`, send the integer `k` to `k/m\in\mathbb Q`. This is compatible with every transition because at level `n`

\[
\frac{(n/m)k}{n}=\frac km.
\]

Every rational `a/b` occurs from the integer `a` at level `b`, so

\[
\boxed{
\widehat{\Sigma_{\mathbb Q}}\cong\mathbb Q.
}
\]

Pontryagin duality for locally compact abelian groups then gives

\[
\boxed{
\Sigma_{\mathbb Q}\cong\widehat{\mathbb Q}.
}
\]

This has an immediate spectral consequence. Ordinary harmonic analysis on the canonical refinement completion is indexed by rational characters:

\[
\boxed{
L^2(\Sigma_{\mathbb Q})
\cong \ell^2(\mathbb Q)
}
\]

at the Fourier-basis level. The inverse limit has genuinely richer topology than one circle, but its linear translation-invariant spectrum is the classical rational character group, not a newly generated zeta-zero set.

## 2. The profinite completion is exactly the anchor fiber

There is an explicit standard model for the solenoid. Let `a\in\widehat{\mathbb Z}` and write `a_n` for its residue modulo `n`. Define

\[
z_n(t,a)
=\exp\!\left(2\pi i\frac{t-a_n}{n}\right).
\]

If `m\mid n`, then `a_n\equiv a_m\pmod m`, so

\[
z_n(t,a)^{n/m}=z_m(t,a).
\]

Thus `(t,a)` determines a compatible point of `\Sigma_{\mathbb Q}`. The kernel consists exactly of diagonal integers `(k,k)`, giving

\[
\boxed{
\Sigma_{\mathbb Q}\cong
(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z_{\rm diag}.
}
\]

Projection to level `1` is simply

\[
(t,a)\longmapsto e^{2\pi i t}.
\]

Its fiber over the common vertex `1` can be represented uniquely with `t=0`, and is therefore canonically

\[
\boxed{
\pi_1^{-1}(1)\cong\widehat{\mathbb Z}.
}
\]

This is the precise bridge to PC-059. There, normalized Haar measure on `\widehat{\mathbb Z}` and its prime-valuation pushforward arose from the infinite divisor-Haar spectral limit. Here the same `\widehat{\mathbb Z}` is the transverse compact fiber over the original common anchor in the all-level circle refinement.

Because `\Sigma_{\mathbb Q}` is a compact-group extension, Haar measure projects to circle Haar measure and has Haar conditional measure on the compact fiber. Hence the PC-059 finite-adic Haar law is not an unrelated completion imported after the fact: it is exactly the natural transverse Haar law of this classical solenoidal refinement geometry.

## 3. The same object is the additive adelic quotient

The standard strong-approximation description of the rational adeles gives

\[
\boxed{
\mathbb A_{\mathbb Q}/\mathbb Q
\cong
(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z_{\rm diag}.
}
\]

Consequently

\[
\boxed{
\Sigma_{\mathbb Q}\cong\mathbb A_{\mathbb Q}/\mathbb Q.
}
\]

This identification is well established in the literature on arithmetic solenoids. Burgos and Verjovsky explicitly describe the universal arithmetic one-dimensional solenoid as all three of:

- the Pontryagin dual of `\mathbb Q`;
- the inverse limit of the tower of finite coverings of `S^1`;
- the additive adele quotient `\mathbb A_{\mathbb Q}/\mathbb Q`.

Thus the most direct attempt to combine the original circle with all divisibility refinements lands exactly on a classical adelic object. The project-specific contribution here is the identification of that classical object as the canonical ambient completion sitting between the prime-circle circle geometry and the `\widehat{\mathbb Z}` limit already found independently in PC-059.

## 4. Why the solenoid alone does not supply a new zeta functional equation

The appearance of `\mathbb A_{\mathbb Q}/\mathbb Q` is structurally suggestive because Tate's thesis derives the completed zeta functional equation adelically. But the distinction between the **compact quotient** and the full Tate apparatus is decisive.

Tate works with Schwartz–Bruhat functions on the full additive adele group `\mathbb A_{\mathbb Q}`, uses its self-dual Fourier transform and Poisson summation over the discrete lattice `\mathbb Q`, and then introduces multiplicative scaling through ideles / Mellin-type zeta integrals. The archimedean local factor supplies the gamma factor, while the finite places supply the Euler factors. Fourier duality produces the `s\leftrightarrow1-s` functional equation.

The inverse-limit construction above determines only

\[
\boxed{
\Sigma_{\mathbb Q}=\mathbb A_{\mathbb Q}/\mathbb Q
\quad\text{with}\quad
\widehat{\Sigma_{\mathbb Q}}=\mathbb Q.
}
\]

It does not by itself select a Schwartz–Bruhat test space on `\mathbb A_{\mathbb Q}`, a lift from the quotient to the full adele group, a multiplicative idele action with a geometrically fixed normalization, or a Mellin parameter `s`. If those ingredients are appended in their standard forms, the result is Tate's classical reformulation of zeta rather than a new prime-circle derivation.

The novelty boundary is stronger still: Connes and collaborators have already developed spectral and trace-formula interpretations of zeta zeros using adele-class / Bost–Connes structures. Therefore the mere fact that prime-circle refinement reaches an adelic solenoid cannot count as a new spectral route to RH.

## 5. Relation to PC-010 and the exact extension duality

PC-010 observes that the union of all birth-labelled roots is

\[
\mu_\infty\cong\mathbb Q/\mathbb Z
\]

with the classical power-map semigroup. PC-064 keeps the entire ambient circle at every level and remembers compatible lifts. The two constructions fit the dual exact sequences

\[
0\to\widehat{\mathbb Z}
\to\Sigma_{\mathbb Q}
\to\mathbb R/\mathbb Z
\to0
\]

and

\[
0\to\mathbb Z
\to\mathbb Q
\to\mathbb Q/\mathbb Z
\to0.
\]

This makes the information boundary explicit:

- `\mathbb Q/\mathbb Z` is the torsion/birth tower already classicalized by PC-010;
- `\widehat{\mathbb Z}` is the finite-adic transverse fiber appearing in PC-059;
- `\Sigma_{\mathbb Q}` is the canonical compact object coupling that fiber to the archimedean circle;
- its full Fourier character group is still the classical `\mathbb Q`.

The coupling is therefore real and geometrically natural, but it is not an unrecognized arithmetic structure.

## 6. Prior-art and novelty audit

No historical novelty is claimed for the solenoid, Pontryagin duality, or the adelic quotient.

- Juan M. Burgos and Alberto Verjovsky, **Adelic Ahlfors–Bers theory**, arXiv:1603.05676 (2016), explicitly identify the universal arithmetic one-dimensional solenoid as the Pontryagin dual of `\mathbb Q`, as `\mathbb A_{\mathbb Q}/\mathbb Q`, and as the inverse limit of all finite coverings of the circle.
- John Tate, **Fourier Analysis in Number Fields and Hecke's Zeta-Functions**, in J. W. S. Cassels and A. Fröhlich (eds.), *Algebraic Number Theory*, Academic Press (1967), 305–347. Role: the classical full-adele Fourier/Poisson and idele-zeta-integral mechanism behind analytic continuation and functional equations.
- Alain Connes, **Trace formula in noncommutative geometry and the zeros of the Riemann zeta function**, *Selecta Mathematica* 5 (1999), 29–106; arXiv:math/9811068. Role: spectral realization of zeta zeros and explicit formulas on an adele-class noncommutative space.
- Alain Connes, Caterina Consani and Matilde Marcolli, **The Weil proof and the geometry of the adèles class space**, arXiv:math/0703392 (2007). Role: Weil-style trace/positivity formulation in the adele-class setting and a direct prior-art boundary for interpreting an adelic refinement space as a new RH geometry.

The durable Mathia result is the project-specific bridge

\[
\boxed{
\text{ambient prime-circle refinement}
\longrightarrow
\Sigma_{\mathbb Q}
\longleftarrow
\widehat{\mathbb Z}\text{ anchor fiber from PC-059},
}
\]

plus the negative conclusion that this canonical bridge is already the classical adelic solenoid.

## 7. Boundaries and exact audit tests

This result does **not** rule out:

- a nonlinear or non-translation-invariant operator on the solenoidal refinement that is forced by additional Euclidean/spherical prime-circle geometry;
- a genuinely geometric lamination metric or uniformization that is not determined by the compact-group structure alone;
- a cross-level operator formed before passage to the inverse limit;
- an independently derived mechanism that lifts the compact quotient to full adelic test-function data rather than choosing Tate's machinery by hand;
- or the global primitive-root uniformization/accessory branch of PC-017.

It does rule out treating the canonical compatible inverse limit itself, its rational Fourier characters, or the bare identification with `\mathbb A_{\mathbb Q}/\mathbb Q` as a new bridge to the zeta functional equation or critical line.

The exact part has simple falsifiers:

1. dualize `z\mapsto z^{n/m}` and verify the direct-limit map `k@m\mapsto k/m\in\mathbb Q`;
2. verify the explicit compatible coordinates `z_n(t,a)` and kernel `\mathbb Z_{\rm diag}`;
3. verify that the level-one anchor fiber is `\widehat{\mathbb Z}`;
4. verify the dual short exact sequence `0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0`;
5. compare the resulting compact group with the classical `\mathbb A_{\mathbb Q}/\mathbb Q` description.

Failure of any of the first four would invalidate the claimed intrinsic bridge. A future RH mechanism can evade the negative conclusion only by using additional structure not already determined by this classical compact refinement object.
