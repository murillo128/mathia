# PC-019 — unanchored single-shell geometry cannot distinguish an odd level n from the composite level 2n

**Status:** `DECISIVE-NEGATIVE` for any proposed RH/primality mechanism built only from the intrinsic, unanchored geometry or spectrum of one primitive/birth shell. The obstruction is exact and survives spherical projection, hyperbolic uniformization, flat cone metrics, canonical cyclic covers, and the original interior/exterior involution.

## 1. Exact cyclotomic half-turn degeneracy

For every odd integer `n > 1`, the classical cyclotomic identity is

\[
\boxed{\Phi_{2n}(z)=\Phi_n(-z).}
\]

Equivalently, the primitive root sets satisfy

\[
\boxed{\mu_{2n}^*=-\mu_n^*.}
\]

Thus the shell born at level `2n` is exactly the shell born at level `n`, rotated by `pi` in the original circle.

This is already fatal to any invariant that forgets the distinguished common vertex `1` and depends only on the intrinsic Euclidean/spherical configuration of one birth shell.

In particular, if `p` is any odd prime, then the prime level `p` and the composite level `2p` have congruent primitive shells.

## 2. The degeneracy preserves the original inside/outside duality

Let

\[
R(z)=-z,
\qquad
I(z)=\frac1{\bar z}.
\]

Then

\[
R\circ I=I\circ R.
\]

Under the spherical compactification of PC-015, `R` is the half-turn around the north-south axis, while `I` is reflection across the equator. Hence the isomorphism between the `n` and `2n` shells preserves the full two-sided spherical structure:

- the equator;
- northern/southern hemispheres;
- the interior/exterior involution;
- all chord lengths and angles;
- all orthogonal circles and their spherical-cap images, up to the same half-turn.

Therefore merely retaining the spherical projection or the exact orthogonal-circle geometry does not remove this degeneracy if the common vertex / absolute phase is forgotten.

## 3. Hyperbolic spectral consequence

Recall the unanchored primitive-shell surface from PC-016,

\[
S_n:=\widehat{\mathbb C}\setminus
\bigl(\{0,\infty\}\cup\mu_n^*\bigr).
\]

For odd `n > 1`, the rotation `R(z)=-z` gives an exact biholomorphism

\[
\boxed{R:S_n\overset\sim\longrightarrow S_{2n}.}
\]

Both surfaces are hyperbolic punctured spheres of finite area. By uniqueness of the complete Poincare metric in a conformal class, `R` is an isometry for their canonical hyperbolic metrics:

\[
\boxed{R^*g_{S_{2n}}=g_{S_n}.}
\]

Consequently every **unmarked intrinsic spectral invariant** agrees exactly:

\[
\boxed{
\operatorname{Spec}\Delta_{S_n}
=
\operatorname{Spec}\Delta_{S_{2n}}.
}
\]

Likewise, after the obvious cusp relabeling, the two surfaces have the same

- length spectrum;
- Selberg zeta function;
- resonances;
- scattering matrix up to permutation/conjugation of cusp channels;
- scattering determinant;
- regularized determinants and heat invariants whenever defined intrinsically.

Thus, for every odd prime `p`,

\[
\boxed{
\text{all unanchored hyperbolic spectral data of }S_p
=
\text{those of the composite }S_{2p}.
}
\]

This rules out the entire branch

\[
\text{one primitive shell}
\to
\text{canonical punctured-sphere hyperbolic spectrum}
\to
\text{prime-specific/RH mechanism},
\]

unless some datum from the original construction that is not preserved by the half-turn is retained.

## 4. The same obstruction kills a natural new flat/spherical spectral candidate

A natural attempt suggested by PC-003 and PC-015 is to turn the primitive-shell potential itself into a metric. Let

\[
\phi=\varphi(n),
\qquad
U_n(z)=\log|\Phi_n(z)|.
\]

Among the power-law conformal metrics

\[
g_{n,c}=e^{-cU_n(z)}|dz|^2,
\]

the original inversion `I(z)=1/bar(z)` is an isometry if and only if

\[
c\phi=4.
\]

Hence the geometry itself singles out

\[
\boxed{
g_n=|\Phi_n(z)|^{-4/\varphi(n)}|dz|^2.}
\]

For `phi > 2` this is a compact flat cone metric on the sphere: every primitive root has cone angle

\[
\boxed{2\pi\left(1-\frac{2}{\phi}\right),}
\]

and the total cone deficit is exactly `4 pi`, as required by Gauss-Bonnet. The point at infinity is regular. For `phi=2` the cone points degenerate to cylindrical ends.

Equivalently, with

\[
m=\frac{\varphi(n)}2,
\]

the metric is induced by the canonical meromorphic `m`-differential

\[
\boxed{\eta_n=\frac{(dz)^m}{\Phi_n(z)},}
\]

whose canonical cyclic orientation cover is the superelliptic translation surface

\[
\boxed{C_n:\ y^m=\Phi_n(z),\qquad \omega=\frac{dz}{y}.}
\]

A Riemann-Hurwitz calculation gives

\[
\boxed{g(C_n)=(m-1)^2.}
\]

The general theory of flat metrics from `k`-differentials and their canonical cyclic covers is standard. This specialization looked initially attractive because it is two-dimensional, canonical, inversion-invariant, and produces a genuine discrete Laplace/translation-surface spectral package without inserting a generating function.

However the same cyclotomic identity kills it as an unanchored prime detector. For odd `n`, `phi(2n)=phi(n)` and

\[
\Phi_{2n}(z)=\Phi_n(-z),
\]

so

\[
\boxed{R^*g_{2n}=g_n.}
\]

The canonical cyclic covers are likewise isomorphic under the induced half-turn (up to the harmless constant phase of the `m`-differential). Therefore their Laplace spectra, period data, Hodge data, and translation-surface dynamics cannot distinguish an odd prime `p` from `2p` either.

This closes the **unmarked** version of that flat-cone / canonical-cover branch before it is mistaken for an RH mechanism.

## 5. What survives: the anchor is mathematically indispensable

The original construction does have extra structure that the half-turn does not preserve: every polygon shares the distinguished vertex

\[
\boxed{1.}
\]

The half-turn sends it to `-1`. Therefore the **anchored** birth surface

\[
X_n^{\rm birth}
=
\widehat{\mathbb C}\setminus
\bigl(\{0,1,\infty\}\cup\mu_n^*\bigr)
\]

is not identified with `X_{2n}^{birth}` by this argument. This is exactly why the prime characterization of PC-016 survives:

\[
n\text{ prime}
\iff
z^n:X_n^{\rm birth}\to
\widehat{\mathbb C}\setminus\{0,1,\infty\}
\text{ is the complete cyclic cover}.
\]

The same is true for pointed/anchored fields. At the common vertex,

\[
U_n(1)=\Lambda(n),
\]

so the anchor immediately breaks the `n <-> 2n` degeneracy (for an odd prime `p`, `U_p(1)=log p` while `U_{2p}(1)=0`). That scalar fact is classical and is **not** itself progress toward RH, but it proves that the absolute phase relative to the common vertex is essential information, not cosmetic decoration.

A future spectral construction based on one shell must therefore be **pointed/anchored** in a geometrically forced way, or else use interactions between different birth levels. Purely intrinsic single-shell spectra are provably too coarse.

## 6. Literature / novelty check

The obstruction uses a classical identity, not a new theorem:

- for odd `n`, `Phi_{2n}(x)=Phi_n(-x)` is a standard elementary property of cyclotomic polynomials;
- complete hyperbolic metrics on punctured Riemann surfaces are conformally canonical;
- meromorphic `k`-differentials induce flat cone metrics and possess canonical cyclic covers on which their pullbacks become powers of abelian differentials (standard strata-of-`k`-differentials theory).

No novelty is claimed for those ingredients. The useful research conclusion is the exact scope of the resulting no-go theorem for the prime-circle program: **any unanchored, rotation-equivariant geometry of a single primitive shell necessarily identifies every odd `n` with `2n`, including every odd prime with an explicit composite.**

## 7. Research gate

From now on, reject any purported prime-specific invariant that depends only on an unmarked primitive shell `mu_n^*`, even if it is dressed as

- a spherical geometry;
- an orthogonal-circle/cap arrangement;
- a hyperbolic punctured surface;
- a Laplace/scattering/Selberg spectrum;
- a flat cone metric;
- a translation surface or canonical cyclic cover.

The candidate must retain at least one piece of genuinely original anchored/multi-level structure: the common vertex `1`, absolute phase, labeled birth level, cross-level interaction, or a nonlinear operation coupling several shells.
