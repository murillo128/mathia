# PF-059 — zero-twist reflection kills Goldman/WP brackets of all reflection-invariant multi-gap lengths

**Status:** `DECISIVE-NEGATIVE` for the first-order noncommutative/Goldman branch suggested after PF-058.

## 1. Setup

Let a finite truncation of the zero-twist prime flute contain all curves under discussion. Use the distinguished cuffs

\[
\alpha_1,\ldots,\alpha_m
\]

as part of a Fenchel–Nielsen pants decomposition, with coordinates

\[
(\ell_i,\tau_i).
\]

The intrinsic zero-twist reflection \(\mathcal R\) preserves every cuff and every cusp and acts in these coordinates by

\[
\boxed{
\mathcal R:(\ell_i,\tau_i)\mapsto(\ell_i,-\tau_i).
}
\]

Wolpert's Fenchel–Nielsen formula gives, up to the standard global normalization convention,

\[
\omega_{WP}=\sum_i d\ell_i\wedge d\tau_i.
\]

Therefore

\[
\boxed{\mathcal R^*\omega_{WP}=-\omega_{WP}.}
\]

The zero-twist locus \(\tau_i=0\) is the fixed locus of this anti-symplectic involution and is Lagrangian.

This finite-truncation argument is sufficient for the infinite flute: every finite family of compact geodesics is contained in some finite-type subsurface, so no global Weil–Petersson structure on the full infinite-type Teichmüller space is needed.

## 2. General anti-symplectic lemma

Let \((M,\omega)\) be symplectic and \(\mathcal R\) an anti-symplectic involution. If two functions \(f,g\) are \(\mathcal R\)-invariant,

\[
f\circ\mathcal R=f,\qquad g\circ\mathcal R=g,
\]

then their Poisson bracket is \(\mathcal R\)-anti-invariant:

\[
\boxed{
\{f,g\}\circ\mathcal R=-\{f,g\}.
}
\]

Hence on the fixed locus,

\[
\boxed{
\{f,g\}=0.
}
\]

This is the standard fact that the fixed locus of an anti-symplectic involution is Lagrangian.

## 3. Application to the multi-gap curves

Let \(\beta_{a,b}\) be any of the simple separating geodesics enclosing a consecutive block of cusps, including the PF-004/PF-007/PF-034 multi-gap curves whose lengths are determined by prime-derived cross-ratios.

Because the zero-twist reflection fixes the cusp set and preserves each consecutive block, it preserves the isotopy class of \(\beta_{a,b}\). Uniqueness of the geodesic representative then gives

\[
\mathcal R(\beta_{a,b})=\beta_{a,b}.
\]

Therefore its geodesic-length function is reflection invariant:

\[
\ell_{\beta_{a,b}}\circ\mathcal R=\ell_{\beta_{a,b}}.
\]

The same is true of every cuff length \(\ell_{\alpha_i}\), and of every other reflection-invariant block-separating length.

Consequently, at the actual zero-twist prime surface,

\[
\boxed{
\{\ell_{\alpha_i},\ell_{\beta_{a,b}}\}_{WP}=0
}
\]

for all \(i,a,b\), even when the two curves intersect topologically.

More strongly, for any two reflection-invariant multi-gap curves \(\beta,\gamma\),

\[
\boxed{
\{\ell_\beta,\ell_\gamma\}_{WP}=0
}
\]

at the prime surface.

Since the PSL(2,R) trace of a hyperbolic geodesic is

\[
T_\gamma=2\cosh(\ell_\gamma/2),
\]

the same conclusion holds for the corresponding Goldman trace functions:

\[
\boxed{
\{T_\beta,T_\gamma\}_{Goldman}=0
}
\]

at the zero-twist Fuchsian representation whenever both curve classes are reflection invariant.

## 4. Exact angle cancellation

Wolpert's cosine formula states

\[
\frac{\partial\ell_\beta}{\partial\tau_\alpha}
=
\sum_{x\in\alpha\cap\beta}\cos\theta_x.
\]

The anti-symplectic argument therefore forces

\[
\boxed{
\sum_{x\in\alpha\cap\beta}\cos\theta_x=0
}
\]

at zero twist for every reflection-invariant \(\beta\).

For the genus-zero block curves relevant here, a cuff crossed by a block separator is crossed twice. The reflection pairs the two crossings, with supplementary angles \(\theta\) and \(\pi-\theta\), so

\[
\cos\theta+\cos(\pi-\theta)=0.
\]

Thus the vanishing is visible directly in the exact orthogonal/reflection geometry; it is not an abstract cancellation detached from the prime construction.

## 5. Consequence for PF-058

PF-058 left open the possibility that adding intersecting multi-gap geodesics to the commuting cuff traces could generate a non-abelian Goldman algebra whose first-order Poisson structure carried prime-gap information.

That route fails at the actual prime surface:

\[
\boxed{
\text{all reflection-invariant length/trace observables have zero mutual Poisson brackets on the zero-twist locus.}
}
\]

Hence the chain

\[
\text{cuffs + multi-gap separators}
\to
\text{nonzero Goldman brackets at the prime point}
\to
\text{canonical noncommutative/quantized prime dynamics}
\]

is ruled out.

The fact that some of these curves intersect does not rescue the construction; their Wolpert cosine contributions cancel pairwise because of reflection.

## 6. What is not ruled out

This is a first-order statement at the reflection-symmetric locus. It does **not** imply that the relevant length functions are globally Poisson commuting on Teichmüller space, and it does not kill second-order twist data.

Indeed, for a reflection-invariant length function \(\ell_\beta\),

\[
\ell_\beta(\tau)=\ell_\beta(-\tau)
\]

along any reflection-odd twist direction, so the first derivative vanishes but the Hessian

\[
\frac{\partial^2\ell_\beta}{\partial\tau_i\partial\tau_j}\Big|_{\tau=0}
\]

can be nonzero. Wolpert's positivity/convexity theory makes such second variations classical objects.

Therefore any surviving symplectic/character-variety direction would have to use second-order geometry, move away from the zero-twist fixed locus, or involve observables not preserved by the intrinsic reflection. None of these should be promoted unless the extra structure is forced by the original prime-circle geometry rather than introduced to manufacture noncommutativity.

## 7. Novelty check

The ingredients are classical:

- Wolpert's formula \(\omega_{WP}=\sum d\ell_i\wedge d\tau_i\);
- Wolpert's twist derivative / cosine formula;
- the general fact that fixed loci of anti-symplectic involutions are Lagrangian;
- Goldman's Poisson structure on trace functions.

No novelty is claimed for that symplectic principle. The substantive point for the prime-flute program is negative: the exact zero-twist reflection applies not only to the distinguished cuffs but also to the prime-derived block separators that survived the earlier spectral tests, so the proposed first-order non-abelian Goldman channel collapses at the prime surface itself.
