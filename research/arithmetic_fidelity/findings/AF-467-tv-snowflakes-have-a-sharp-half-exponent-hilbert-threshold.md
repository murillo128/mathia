# AF-467 — TV snowflakes have a sharp half-exponent Hilbert threshold

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `SOURCE-METRIC-PHASE-BOUNDARY`, `QUANTITATIVE-FIDELITY`, `NONLINEAR-TARGET`, `NO-NOVELTY-CLAIM`

## Claim

AF-466 shows that the full probability simplex becomes exactly Hilbertian after the square-root deformation `d_TV -> d_TV^{1/2}`. AF-464 shows that the undeformed TV metric cannot admit complexity-independent bi-Lipschitz Hilbert fidelity on sparse-mixture cubes. These two endpoints extend to a sharp phase boundary for the whole power family.

Let `A` be an alphabet containing arbitrarily many atoms, let

\[
\Delta(A)=\left\{\mu\in\ell^1(A):\mu(a)\ge0,\ \sum_a\mu(a)=1\right\},
\qquad
d(\mu,\nu)=\|\mu-\nu\|_1,
\]

and for `0<alpha<=1` define the snowflaked source metric

\[
d_\alpha(\mu,\nu)=d(\mu,\nu)^\alpha.
\tag{1}
\]

Then the Hilbert-fidelity threshold is exactly

\[
\boxed{\alpha_*=\frac12.}
\tag{2}
\]

More precisely:

1. **Positive side.** For every `0<alpha<=1/2`, `(Delta(A),d_alpha)` admits an isometric embedding into a Hilbert space.

2. **Negative side.** Fix `alpha>1/2`. Let `A` contain at least `2k` atoms and let `Delta_k(A)` denote laws supported on at most `k` atoms. If an arbitrary map `F:Delta_k(A)->H` into Hilbert space satisfies
   \[
   \kappa d_\alpha(\mu,\nu)
   \le
   \|F(\mu)-F(\nu)\|_H
   \le
   L d_\alpha(\mu,\nu)
   \tag{3}
   \]
   for all source pairs, then
   \[
   \boxed{
   \kappa\le L\,k^{1/2-\alpha},
   \qquad
   \operatorname{dist}(F)=\frac{L}{\kappa}\ge k^{\alpha-1/2}.
   }
   \tag{4}
   \]
   Consequently the full infinite simplex `(Delta(A),d_alpha)` has no bi-Lipschitz embedding into Hilbert space with finite global distortion when `alpha>1/2`.

3. **Sharpness.** At `alpha=1/2`, the lower bound in `(4)` becomes the trivial distortion bound `>=1`, while AF-466 supplies distortion exactly `1`. Thus the transition occurs at the endpoint, not merely somewhere between square-root TV and TV.

The reusable Arithmetic Fidelity statement is therefore:

\[
\boxed{
\text{among power deformations }d_{TV}^\alpha,\ \sqrt{d_{TV}}
\text{ is the least severe snowflake that makes the full TV simplex Hilbertian.}
}
\tag{5}
\]

This classifies a metric-repair degree of freedom left open by AF-464. Changing the source metric can indeed remove the Hilbert obstruction, but within the natural power family one must cross all the way to exponent `1/2` or below.

## Exact derivation

### Positive half: `0<alpha<=1/2`

The TV simplex is a subset of `ell^1(A)` with its ordinary `L^1` metric. Schoenberg's negative-type theorem gives that, for an `L^1` metric `d`, every power `d^alpha` with

\[
0<\alpha\le\frac12
\]

is a Hilbert metric. Equivalently, `d^{2alpha}` is of negative type for `2alpha<=1`, so there is a map `Psi_alpha` into a Hilbert space satisfying

\[
\|\Psi_\alpha(\mu)-\Psi_\alpha(\nu)\|=d(\mu,\nu)^\alpha.
\tag{6}
\]

At the endpoint `alpha=1/2`, AF-466 gives the explicit subgraph realization

\[
\Phi(\mu)(a,t)=\mathbf1_{[0,\mu(a)]}(t)
\]

with

\[
\|\Phi(\mu)-\Phi(\nu)\|^2=d(\mu,\nu).
\tag{7}
\]

Thus the entire interval `0<alpha<=1/2` is positively classified, with no restriction on support complexity or arithmetic structure.

### Negative half: `alpha>1/2`

Choose `2k` distinct atoms

\[
a_1,b_1,\ldots,a_k,b_k
\]

and for each `epsilon in {-1,+1}^k` define the paired-mixture law from AF-464,

\[
\mu_\varepsilon
=\frac1k\sum_{j=1}^k
\begin{cases}
\delta_{a_j},&\varepsilon_j=+1,\\
\delta_{b_j},&\varepsilon_j=-1.
\end{cases}
\tag{8}
\]

If `epsilon` and `eta` differ in `r` coordinates, then

\[
d(\mu_\varepsilon,\mu_\eta)=\frac{2r}{k}.
\tag{9}
\]

Hence a cube edge has `d_alpha`-length

\[
\left(\frac2k\right)^\alpha,
\tag{10}
\]

while every antipodal pair has `d_alpha`-length

\[
2^\alpha.
\tag{11}
\]

Set `f(epsilon)=F(mu_epsilon)`. Hilbert space has Enflo type `2` with constant `1`, so

\[
\mathbb E_\varepsilon
\|f(\varepsilon)-f(-\varepsilon)\|^2
\le
\sum_{j=1}^k
\mathbb E_\varepsilon
\|f(\varepsilon)-f(\varepsilon^{(j)})\|^2.
\tag{12}
\]

The lower inequality in `(3)` and the antipodal distance `(11)` give

\[
\mathbb E_\varepsilon
\|f(\varepsilon)-f(-\varepsilon)\|^2
\ge
\kappa^2 2^{2\alpha}.
\tag{13}
\]

The upper inequality in `(3)` and the edge distance `(10)` give

\[
\sum_{j=1}^k
\mathbb E_\varepsilon
\|f(\varepsilon)-f(\varepsilon^{(j)})\|^2
\le
kL^2\left(\frac2k\right)^{2\alpha}
=L^2 2^{2\alpha}k^{1-2\alpha}.
\tag{14}
\]

Combining `(12)`--`(14)` and cancelling `2^{2alpha}` yields

\[
\kappa^2\le L^2k^{1-2\alpha},
\]

which is exactly `(4)`.

If `A` is infinite, the full simplex contains these cubes for every `k`. For `alpha>1/2`, the required distortion therefore diverges as `k^{alpha-1/2}`, excluding any finite-distortion Hilbert embedding of the full space.

## Why this is a distinct representation result

AF-464 fixes the original TV metric and proves a nonlinear metric-type obstruction. AF-466 changes the metric at one endpoint and gives an exact positive embedding. AF-467 varies the **source metric itself as a one-parameter representation family** and identifies the exact transition between those regimes.

The negative proof deliberately reuses the paired source cube from AF-464; the new mathematical content is not a new obstruction mechanism but the exponent accounting that converts it into a sharp source-metric phase law. The positive half uses Schoenberg's classical power theorem. This is therefore a classification result assembling two established mechanisms across a genuinely different source-geometry parameter, not a novelty claim for either mechanism separately.

## Prior art and novelty audit

The underlying mathematics is classical. **No novelty is claimed for the Hilbert snowflake theorem, negative type, Enflo type, or Hamming-cube distortion.**

- I. J. Schoenberg, **“Metric Spaces and Positive Definite Functions,”** *Transactions of the American Mathematical Society* 44(3), 522–536 (1938), DOI `10.1090/S0002-9947-1938-1501980-0`. The Hilbert-embedding criterion and the `L^p` power theorem imply the entire positive range `0<alpha<=1/2` for `L^1` metrics.
- Jean Bretagnolle, Didier Dacunha-Castelle, and Jean-Louis Krivine, **“Lois stables et espaces L^p,”** *Annales de l'Institut Henri Poincaré, Section B* 2(3), 231–259 (1966). Their negative-type formulation gives the classical `L^p`, `1<=p<=2`, Hilbertian power relation in stable-law language.
- Per Enflo, **“On the nonexistence of uniform homeomorphisms between `L_p`-spaces,”** *Arkiv för Matematik* 8 (1969), 103–105, DOI `10.1007/BF02589549`. This is foundational prior art for the metric-cube obstruction used on the negative side.
- Paata Ivanisvili, Ramon van Handel, and Alexander Volberg, **“Rademacher type and Enflo type coincide,”** *Annals of Mathematics* 192(2), 665–678 (2020), DOI `10.4007/annals.2020.192.2.8`. This supplies the modern metric-type framework already used in AF-464.

All of these source domains were already part of the AF-464/AF-466 audit. AF-467's line-specific value is the exact threshold statement `(2)`--`(5)` for total-variation probability laws and its interpretation as the minimum power deformation compatible with dimension-free Hilbert fidelity.

## Boundary and falsification audit

- **The threshold is for the full TV simplex / growing paired-mixture cubes.** A restricted source family can embed for `alpha>1/2` if it excludes the obstructing geometry strongly enough; AF-465 warns that simple cube exclusion or bounded doubling alone is not a general positive certificate.
- **The threshold is Hilbert-specific.** Other target categories have different metric type and may move the obstruction exponent. Equation `(4)` uses Hilbert Enflo type `2` exactly.
- **This classifies power snowflakes, not arbitrary metric transforms.** A non-power transform may preserve more local scale in some ranges while altering others. It requires its own audit.
- **Isometric Hilbertianity is not compression.** On the positive side the representation may remain infinite-dimensional and fully informative. Subsequent finite-rank, compact, quotient, spectral, Gram, or asymptotic operations can still destroy the discriminator.
- **Every `alpha<1` is singular relative to original-TV forward sensitivity near zero.** Since `d^alpha/d=d^{alpha-1}->infinity` as `d->0`, crossing the Hilbert threshold necessarily abandons a finite upper Lipschitz modulus in the original TV scale.
- **Bounded source diameter still gives inverse linear control in TV.** On probability laws `d<=2`, so `d^alpha >= 2^{alpha-1}d` for every `alpha<=1`. Thus the snowflake can retain a uniform inverse-TV margin while making forward sensitivity singular; the two notions must not be conflated.
- **Finite alphabets have a finite-dimensional lower bound, not an impossibility theorem.** If `|A|=n`, `(4)` applies for every `k<=floor(n/2)` and yields distortion at least `floor(n/2)^{alpha-1/2}` up to choosing the largest paired cube.

## Arithmetic specialization

Take the alphabet to be the rational primes. For unrestricted prime-weight laws, the exponent `1/2` is therefore the exact boundary for dimension-free Hilbert fidelity within the family `d_TV^alpha`.

This does **not** distinguish rational primes from matched non-prime alphabets: both sides of the theorem are universal. Its use is instead diagnostic. If a prime-facing spectral or positivity mechanism proposes a Hilbert carrier after a metric deformation, then:

- `alpha>1/2` cannot uniformly carry arbitrary growing sparse prime mixtures with bounded distortion;
- `alpha<=1/2` removes that Hilbert obstruction, so the remaining question is whether the later arithmetic operation is semantically compatible with the snowflaked scale and whether it preserves the labeled information rather than collapsing it again.

Thus the arithmetic burden moves cleanly downstream once the exponent reaches `1/2`: Hilbert geometry is no longer the blocker, but prime selectivity still has to survive the subsequent compression.

## Consequence for the line

AF-467 closes the simplest ambiguity left by AF-466. The square-root repair is not one arbitrary convenient deformation among nearby powers; it is the **maximal power exponent** compatible with uniform Hilbert geometry on the full TV simplex. Any attempt to stay closer to the original linear TV scale by taking `alpha>1/2` reactivates a quantitative cube obstruction whose distortion diverges with source-mixture complexity.

The live metric-compatible frontier is therefore no longer “which TV power should we use?” It is whether a concrete downstream discriminator can consume the `alpha<=1/2` geometry without reintroducing a forbidden bounded-original-TV sensitivity requirement or discarding the provenance retained by the Hilbert representation.