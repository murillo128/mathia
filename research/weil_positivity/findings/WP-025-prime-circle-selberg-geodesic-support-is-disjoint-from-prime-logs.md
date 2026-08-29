# WP-025 — Prime-Circle Selberg geodesic support is disjoint from Riemann prime logs

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` + `PRIOR-ART-REDIRECTION` for the ordinary hyperbolic-orbit route

```text
Prime-Circle base B = Gamma(2)\H
  -> ordinary Selberg test-function trace
  -> primitive closed-geodesic / hyperbolic orbital terms
  -> identify those orbit atoms with Riemann prime-power atoms
  -> finite Weil distribution.
```

`WP-024` left open a test-function-level trace construction because its scalar scattering calculation only tested the logarithmic derivative of the modular scattering coefficient. The most direct remaining possibility is that the *hyperbolic orbital side* of the ordinary Selberg trace formula on the same Prime-Circle base might supply the finite Weil distribution more exactly than scalar scattering does.

It cannot. On `Gamma(2)\H`, every hyperbolic closed-geodesic length is the logarithm of a real quadratic unit, while the Riemann finite explicit formula is supported on logarithms of rational prime powers. These two atomic supports are exactly disjoint, even after any positive rational rescaling of the length variable. The obstruction is algebraic and does not depend on zero data, asymptotics, numerics, or positivity assumptions.

No novelty is claimed for the Selberg trace formula, the trace/length relation, real-quadratic-unit descriptions of modular geodesics, or the analogy between prime geodesics and rational primes. The durable Mathia result is the exact support obstruction for the canonical Prime-Circle modular base, together with the resulting redirection: if a trace-formula route survives, the Riemann prime terms cannot come from the ordinary `Gamma(2)` hyperbolic closed-orbit sum without adding genuinely new arithmetic correspondences or a different geometric channel.

## 1. The ordinary Selberg hyperbolic term lives on iterated geodesic lengths

By `WP-024`, the universal Prime-Circle base is

\[
B\simeq \Gamma(2)\backslash\mathbb H,
\qquad
\Gamma(2)\subset \operatorname{PSL}_2(\mathbb Z).
\]

For a finite-area hyperbolic quotient, the hyperbolic part of the Selberg trace formula has the standard shape

\[
\boxed{
H_\Gamma(g)
=
\sum_{P\ \mathrm{primitive}}
\sum_{k\ge 1}
\frac{\ell(P)}{2\sinh(k\ell(P)/2)}
\,g(k\ell(P)),
}
\]

up to the conventional normalization of the Fourier transform/test function. Here `P` ranges over primitive hyperbolic conjugacy classes, equivalently primitive closed geodesics, and `ell(P)>0` is the primitive geodesic length. Thus the atomic support of the ordinary hyperbolic orbital distribution is

\[
\boxed{
\mathcal L_{\Gamma(2)}
=
\{k\ell(P): P\text{ primitive closed geodesic},\ k\ge1\}.
}
\]

The noncompact trace formula also has identity, parabolic, elliptic when present, and continuous/scattering terms. The claim below concerns only the ordinary **hyperbolic closed-orbit term**. Those additional terms are not being discarded; in fact `WP-024` already shows that the continuous scattering channel is precisely where completed zeta data can enter.

Dennis Hejhal's classical treatment of the Selberg trace formula and the Riemann zeta function is a standard reference for this prime/geodesic analogy and trace-formula normalization: D. A. Hejhal, *The Selberg trace formula and the Riemann zeta function*, Duke Math. J. 43 (1976), 441–482, DOI `10.1215/S0012-7094-76-04338-6`.

## 2. Closed geodesics on the modular base are logarithms of quadratic units

Let `gamma` be a hyperbolic element of `Gamma(2)`. Choose an `SL_2(Z)` representative and write

\[
T=|\operatorname{tr}\gamma|\in\mathbb Z,
\qquad T>2.
\]

The standard trace-length relation is

\[
\boxed{
2\cosh\frac{\ell(\gamma)}2=T.
}
\]

Equivalently, define

\[
\alpha_\gamma=e^{\ell(\gamma)/2}>1.
\]

Then

\[
\alpha_\gamma+\alpha_\gamma^{-1}=T,
\]

so `alpha_gamma` is a root of

\[
\boxed{
x^2-Tx+1=0.}
\]

For integer `T>2`, the discriminant `T^2-4` is not a square: if `T^2-r^2=4`, then `(T-r)(T+r)=4`, whose only nonnegative same-parity solution gives `T=2`. Hence `Q(alpha_gamma)` is a real quadratic field and the nontrivial Galois automorphism sends

\[
\boxed{
\alpha_\gamma\longmapsto\alpha_\gamma^{-1}.
}
\]

Thus

\[
\ell(\gamma)=2\log\alpha_\gamma
\]

is the logarithm of a nontrivial norm-one real quadratic unit, not the logarithm of a rational integer.

The classical trace/length relation and its arithmetic interpretation for arithmetic Fuchsian groups are reviewed, for example, in Slavyana Geninska, *On arithmetic Fuchsian groups and their characterizations*, Ann. Fac. Sci. Toulouse Math. 23 (2014), 1093–1102, DOI `10.5802/afst.1437`. The broader real-quadratic-field/closed-geodesic correspondence is also standard; see W. Duke, Ö. Imamoglu, and Á. Tóth, *Geometric invariants for real quadratic fields*, Ann. of Math. 184 (2016), 949–990, DOI `10.4007/annals.2016.184.3.8`.

## 3. Exact support-disjointness lemma

The finite Riemann/Weil prime distribution is supported on

\[
\boxed{
\mathcal P
=
\{m\log p: p\text{ a rational prime},\ m\ge1\},
}
\]

with the familiar weights `log(p)/p^{m/2}` after centering at `1/2` (and with the reflected negative support according to test-function convention).

We now compare supports exactly.

### Lemma

For every hyperbolic closed geodesic `P` on `Gamma(2)\H`, every integers `k,m>=1`, every rational prime `p`, and every positive rational number `q`,

\[
\boxed{
qk\ell(P)\ne m\log p.
}
\]

### Proof

Write `q=a/b` in positive coprime integers and suppose, for contradiction, that

\[
\frac{a}{b}k\ell(P)=m\log p.
\]

Multiplying by `b` and exponentiating gives

\[
e^{ak\ell(P)}=p^{bm}.
\]

Since `alpha_P=e^{ell(P)/2}`,

\[
\boxed{
\alpha_P^{2ak}=p^{bm}\in\mathbb Q.
}
\]

Apply the nontrivial Galois automorphism of the real quadratic field `Q(alpha_P)`. The rational number on the right is fixed, while `alpha_P` is sent to `alpha_P^{-1}`. Hence

\[
\alpha_P^{-2ak}=p^{bm}=\alpha_P^{2ak}.
\]

Therefore

\[
\alpha_P^{4ak}=1,
\]

contradicting `alpha_P>1`. This proves the lemma. `QED`

In particular, with `q=1`,

\[
\boxed{
\mathcal L_{\Gamma(2)}\cap\mathcal P=\varnothing.
}
\]

The rational-rescaling strengthening matters because harmless trace-formula convention changes can introduce factors such as `2`; no such normalization can repair the mismatch.

## 4. Consequence: the prime-geodesic analogy is not an exact atom identification here

The Selberg and Riemann explicit formulas are famously parallel:

\[
\text{primitive closed geodesics}
\leftrightarrow
\text{primes},
\qquad
\ell(P)
\leftrightarrow
\log p.
\]

For the canonical Prime-Circle base, however, this correspondence is **structural/asymptotic rather than an equality of atomic supports**. The two supports do not merely have different weights; no ordinary hyperbolic orbit atom lies at any Riemann prime-power location.

Therefore an identity of the form

\[
\sum_{P,k} a_{P,k}\,g(k\ell(P))
=
\sum_{p,m}\frac{\log p}{p^{m/2}}\,g(m\log p)
\]

for all admissible test functions `g` cannot arise by simply choosing or reweighting the standard hyperbolic orbit coefficients while leaving their locations fixed. For discrete distributions, equality against a sufficiently rich test class forces equality of supports and atomic masses; the support lemma already fails before the weights are compared.

This also rules out a tempting positivity shortcut: the hyperbolic orbital side cannot be given positive geometric weights and then declared to be the finite Weil prime distribution. Even if one found a sign theorem for those orbit weights, it would be positivity of the wrong atomic measure.

The statement is deliberately narrower than “no trace formula can produce Weil.” It rules out the **ordinary scalar Laplacian Selberg hyperbolic closed-orbit term on the Prime-Circle modular base** as the exact finite-prime sector.

## 5. Matched controls and failed repairs

The obstruction survives several natural attempts to rescue the route.

First, it is not specific to the index-six subgroup `Gamma(2)`. Any congruence subgroup of `PSL_2(Z)` still has integral matrix traces, so the same quadratic-unit/Galois proof applies to every ordinary hyperbolic conjugacy class. Passing to a finite modular cover can change multiplicities and which geodesics occur, but not turn those geodesic norms into rational prime powers.

Second, iteration does not help. The trace formula already includes all repetitions `k ell(P)`, and the proof uses arbitrary `k>=1`. Nor do the conventional rational rescalings of the spectral or length variable help, by the strengthened lemma above.

Third, positive reweighting, bounded compression, or deletion of orbit classes cannot help as long as the operation leaves the orbital locations `k ell(P)` fixed. Such operations alter masses, not support.

A genuinely nonlinear, orbit-dependent relabeling `ell(P) -> log p` could of course be imposed by hand, but that would be precisely the sort of arithmetic insertion this research line excludes: it is not forced by the intrinsic hyperbolic geometry and it gives no independent positivity theorem.

## 6. Prior-art audit redirects the trace-formula route toward continuous/arithmetic channels

The resemblance between the Selberg trace formula and the Weil/Riemann explicit formula is classical, so it would be incorrect to claim novelty from placing the two formulas side by side. Hejhal's 1976 paper already develops that comparison in detail.

More strongly, Tian An Wong's 2016 dissertation *Explicit Formulae and Trace Formulae* proves, in number-field trace-formula settings, that Weil explicit formulas for Hecke `L`-functions occur through **continuous spectral terms via the Maass-Selberg relation**. See CUNY Graduate Center dissertation 1542, `https://academicworks.cuny.edu/gc_etds/1542/`. This is a direct prior-art warning against expecting the rational-prime Weil distribution to emerge by literally equating modular closed geodesics with rational primes.

That prior art is consistent with `WP-024`: on the Prime-Circle modular base the completed Riemann zeta function appears in the Eisenstein/scattering coefficient, i.e. the continuous channel, while the ordinary hyperbolic orbit channel carries the modular length spectrum instead.

The exact support-disjointness lemma above is therefore not presented as a new theorem about Selberg theory. Its Mathia-specific role is to close a concrete escape left by `WP-024`: **moving from the scalar logarithmic derivative to the ordinary test-function Selberg trace does not cause the Prime-Circle closed orbits to become the Riemann prime-power comb.**

## 7. What is ruled out and what remains open

This finding rules out the direct chain

\[
\boxed{
\text{Prime-Circle }\Gamma(2)\text{ geodesic flow}
\to
\text{ordinary hyperbolic Selberg orbit sum}
\to
\text{exact finite Weil prime distribution}
\to
\text{global geometric positivity}.
}
\]

The obstruction is stronger than a coefficient mismatch: the finite atomic supports are disjoint.

This does **not** rule out:

- the continuous/scattering contribution, already isolated in `WP-024`, though its direct positivity route failed there;
- Hecke-inserted or correspondence trace formulas, where the arithmetic operator changes the geometric fixed-point data rather than merely reweighting ordinary geodesic orbits;
- nontrivial local-system or marking-sensitive Prime-Circle channels whose trace formula has additional arithmetic orbital data;
- a relative/compressed/cohomological trace construction with a new independent sign theorem;
- coupling a Prime-Circle global/archimedean channel to the exact finite Prime-Lattice selector of `WP-018`;
- a different Mathia-native geometry whose primitive orbit lengths are intrinsically `log p` rather than modular quadratic-unit lengths.

Any surviving test-function trace route must therefore explain **where the rational-prime support enters as intrinsic geometry or correspondence data**. The ordinary closed-geodesic spectrum of the canonical Prime-Circle modular base cannot supply it.