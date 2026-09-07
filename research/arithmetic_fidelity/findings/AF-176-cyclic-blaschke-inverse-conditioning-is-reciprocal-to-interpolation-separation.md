# AF-176 — Cyclic Blaschke inverse conditioning is reciprocal to interpolation separation

**Status:** `EXACT-DERIVED`, `QUANTITATIVE-OBSTRUCTION`, `CONDITIONING-LOWER-BOUND`, `GAUGE-QUOTIENT`, `NO-NOVELTY-CLAIM`

## Claim

AF-175 shows that a degree-independent lower bound on the Blaschke interpolation constant is sufficient for degree-uniform local Lipschitz recovery of the zero divisor from the complete inner factor modulo unimodular output gauge. On the regular cyclic family, the same interpolation constant is also quantitatively necessary: the radial inverse condition number is **exactly one half of its reciprocal**.

For `n>=2` and `0<r<1`, define

\[
B_{n,r}(z)
=
\frac{z^n-r^n}{1-r^n z^n}.
\tag{1}
\]

Its zero divisor is

\[
Z_{n,r}
=
\{r\omega_k:0\le k<n\},
\qquad
\omega_k=e^{2\pi i k/n}.
\tag{2}
\]

For `0<s<1`, put

\[
\Delta_n(r,s)
=
\inf_{|\lambda|=1}
\|B_{n,r}-\lambda B_{n,s}\|_{H^\infty}
\tag{3}
\]

and let `d_n(r,s)` be the multiplicity-aware pseudohyperbolic bottleneck distance between `Z_{n,r}` and `Z_{n,s}`. Then

\[
\boxed{
\Delta_n(r,s)=2\rho(r^n,s^n),
\qquad
 d_n(r,s)=\rho(r,s),
}
\tag{4}
\]

where

\[
\rho(x,y)=\frac{|x-y|}{|1-xy|}
\qquad (x,y\in(0,1)).
\tag{5}
\]

Consequently

\[
\frac{d_n(r,s)}{\Delta_n(r,s)}
=
\frac{1-r^n s^n}
{2(1-rs)\displaystyle\sum_{j=0}^{n-1}r^{n-1-j}s^j},
\tag{6}
\]

and therefore

\[
\boxed{
\lim_{s\to r}
\frac{d_n(r,s)}{\Delta_n(r,s)}
=
\frac{1-r^{2n}}
{2n r^{n-1}(1-r^2)}
=
\frac{1}{2\,\delta(B_{n,r})},
}
\tag{7}
\]

with the interpolation/separation constant

\[
\delta(B_{n,r})
=
\min_k\prod_{j\ne k}\rho(r\omega_k,r\omega_j)
=
\frac{n r^{n-1}(1-r^2)}{1-r^{2n}}.
\tag{8}
\]

Thus any local inverse Lipschitz estimate on a class containing this cyclic radial direction,

\[
d_{\mathrm{div}}(B,C)
\le L\,\Delta(B,C),
\tag{9}
\]

must satisfy

\[
\boxed{
L\ge \frac{1}{2\,\delta(B_{n,r})}
}
\tag{10}
\]

at `B=B_{n,r}`. In particular, no local Lipschitz theorem can have a uniform constant over the full class of simple degree-`n` Blaschke divisors for `n>=2`: as `r\downarrow0`, all zeros remain simple for every `r>0` but `\delta(B_{n,r})\to0`, and the required inverse constant diverges.

This makes AF-175 quantitatively near-sharp in its conditioning parameter. Its sufficient modulus has tangent slope `1/\delta` at zero, while the cyclic family forces every general local inverse theorem to pay at least `1/(2\delta)`. The dependence on the interpolation constant therefore cannot be removed or replaced by degree alone; it has the correct order already on an exactly solvable one-parameter stratum.

## Derivation

### The quotient output metric is the coefficient pseudohyperbolic metric

Write

\[
B_{n,r}(z)=B_{n,a}(z),
\qquad a=r^n,
\tag{11}
\]

in the cyclic notation of AF-173. That finding proves the exact gauge-quotient identity

\[
\inf_{|\lambda|=1}
\|B_{n,a}-\lambda B_{n,b}\|_{H^\infty}
=2\rho(a,b).
\tag{12}
\]

Taking `a=r^n` and `b=s^n` gives the first equality in `(4)`.

### Radial matching is the exact divisor bottleneck

For two points of moduli `r,s` and angular difference `\theta`, pseudohyperbolic distance satisfies

\[
\rho(re^{i\alpha},se^{i\beta})^2
=
\frac{r^2+s^2-2rs\cos\theta}
{1+r^2s^2-2rs\cos\theta},
\qquad
\theta=\alpha-\beta.
\tag{13}
\]

As a function of `x=\cos\theta`, the derivative of the squared distance is

\[
-\frac{2rs(1-r^2)(1-s^2)}
{(1+r^2s^2-2rsx)^2}<0.
\tag{14}
\]

Hence, among the target points `s\omega_j`, the unique nearest point to `r\omega_k` is `s\omega_k`, with distance `\rho(r,s)`. Matching equal angular labels therefore achieves bottleneck `\rho(r,s)`, and no permutation can do better because every source point has no target point closer than its radial partner. This proves the second equality in `(4)`.

### The interpolation constant is the exact local condition parameter

Combining `(4)` gives

\[
\frac{d_n(r,s)}{\Delta_n(r,s)}
=
\frac{|r-s|}{1-rs}
\frac{1-r^ns^n}{2|r^n-s^n|}.
\tag{15}
\]

Using

\[
|r^n-s^n|
=|r-s|\sum_{j=0}^{n-1}r^{n-1-j}s^j
\tag{16}
\]

produces `(6)`. Letting `s\to r` yields

\[
\lim_{s\to r}\frac{d_n(r,s)}{\Delta_n(r,s)}
=
\frac{1-r^{2n}}{2n r^{n-1}(1-r^2)}.
\tag{17}
\]

AF-175 derived directly for this same cyclic divisor

\[
\delta(B_{n,r})
=
\frac{n r^{n-1}(1-r^2)}{1-r^{2n}},
\tag{18}
\]

so `(17)` is exactly `(7)`.

Now suppose `(9)` holds in a neighborhood of `B_{n,r}` for a class containing the radial perturbations `B_{n,s}`. Dividing `(9)` by `\Delta_n(r,s)` and letting `s\to r` gives `(10)`. The obstruction uses only simple divisors: for every positive `r`, the `n` zeros in `(2)` are distinct. The loss of a uniform local inverse constant arises as those simple divisors approach the collision stratum `r=0` and their interpolation constant tends to zero.

### The same identity separates the two asymptotic regimes

For fixed `0<r<1` and growing degree,

\[
\delta(B_{n,r})
=
\frac{n r^{n-1}(1-r^2)}{1-r^{2n}}
\longrightarrow0,
\tag{19}
\]

so the forced radial inverse slope

\[
\frac{1}{2\delta(B_{n,r})}
\tag{20}
\]

diverges exponentially up to the polynomial factor `n`. This is the infinitesimal form of AF-170's fixed-radius growing-degree collapse.

In contrast, use the boundary-layer radius

\[
r_n=e^{-u/n},
\qquad u>0.
\tag{21}
\]

AF-175 gives

\[
\delta(B_{n,r_n})
\longrightarrow
\frac{u}{\sinh u}.
\tag{22}
\]

Therefore the exact radial inverse slope converges to

\[
\boxed{
\frac{1}{2\delta(B_{n,r_n})}
\longrightarrow
\frac{\sinh u}{2u}.
}
\tag{23}
\]

On compact positive `u`-windows this remains bounded. Thus the interpolation constant does not merely correlate with the positive and negative regimes found in AF-170--AF-175: on the cyclic radial direction its reciprocal is exactly the local metric conditioning, up to the fixed factor `2` coming from the quotient `H^\infty` normalization.

## Prior art and novelty assessment

No theorem-level novelty is claimed. Finite and interpolating Blaschke products, pseudohyperbolic zero separation, Carleson interpolation constants, and perturbative zero localization are classical subjects.

- John B. Garnett, ***Bounded Analytic Functions***, Graduate Texts in Mathematics 236, Springer (2007), is a standard reference for interpolating sequences, Blaschke products, pseudohyperbolic geometry, and Carleson separation.
- Artur Nicolau, **“Finite Products of Interpolating Blaschke Products,”** *Journal of the London Mathematical Society* 50(3), 520--531 (1994), DOI `10.1112/jlms/50.3.520`, gives classical neighboring theory relating finite products and interpolating-Blaschke separation geometry.
- Kenneth Hoffman, **“Bounded Analytic Functions and Gleason Parts,”** *Annals of Mathematics* 86(1), 74--111 (1967), DOI `10.2307/1970361`, is foundational background for the `H^\infty` and interpolating-Blaschke geometry used in AF-175.
- Stephan Ramon Garcia, Javad Mashreghi, and William T. Ross, ***Finite Blaschke Products and Their Connections***, Springer (2018), DOI `10.1007/978-3-319-78247-8`, gives modern finite-Blaschke and disk-automorphism background.

A targeted search of finite/interpolating Blaschke perturbation and zero-separation literature found the expected mature theory and did not justify a novelty claim for `(7)`. The identity is an elementary specialization of the exact cyclic quotient metric from AF-173 and the classical interpolation constant computed in AF-175. Its Arithmetic Fidelity value is diagnostic: it converts the previously sufficient source-regularity modulus into a necessary quantitative conditioning scale on an explicit family.

## Boundary conditions and falsification checks

- Equation `(7)` is a **directional local lower bound** along the cyclic radial stratum. It does not claim that `1/(2\delta)` is the exact condition number for every perturbation of an arbitrary finite Blaschke product.
- The obstruction applies to any proposed local theorem whose source class contains these radial perturbations and whose endpoint metric is the multiplicity-aware pseudohyperbolic bottleneck metric. A narrower source class may legitimately exclude the degenerating directions.
- The output metric is the quotient `H^\infty` distance removing one unimodular scalar. A raw fixed-normalization norm has the additional gauge effect classified in AF-173 and cannot be substituted silently.
- The divergence as `r\downarrow0` occurs while every `r>0` divisor is simple. Simplicity alone therefore does not provide uniform conditioning; a quantitative separation/interpolation lower bound is essential.
- For fixed `n`, the limit `r\downarrow0` approaches the multiple zero at the boundary of the simple-divisor stratum. The claim is not that a single fixed well-separated divisor is ill-conditioned.
- The factor `2` in `(7)` comes from the exact quotient identity `\Delta=2\rho(r^n,s^n)`. Changing the output normalization or metric changes that numerical factor, though not the reciprocal-separation mechanism.
- Pairwise angular separation of this regular polygon happens to determine the full interpolation constant through symmetry. For arbitrary growing divisors, AF-175's warning remains: nearest-neighbor separation is not interchangeable with a uniform Carleson interpolation constant.
- No RH consequence follows directly. An arithmetic transfer must show that its source family carries an analogous regularity modulus and that the downstream theorem consumes the same quotient and metric in which the inverse conditioning is controlled.

## Consequences for the research line

AF-174 and AF-175 separated two different sources of bad inversion: unrestricted multiplicity/cluster splitting produces the global `1/n` Hölder law, while a uniform interpolation constant restores a degree-independent local Lipschitz inverse. AF-176 closes the remaining ambiguity about whether that interpolation hypothesis was merely a convenient sufficient condition. On the cyclic family it is the actual local conditioning parameter: every inverse estimate must pay at least `1/(2\delta)`.

The practical fidelity audit is therefore sharper. A claim of stable recovery from a compressed analytic representation should identify a **source regularity modulus** and prove that it stays nondegenerate in the asymptotic regime of interest. Declaring degree, simplicity, or exact injectivity is insufficient. If the relevant interpolation/separation modulus collapses, the inverse can become arbitrarily ill-conditioned even before an exact collision occurs.

The cyclic model also supplies a positive calibration rather than only a no-go. Fixed-radius growing degree sends the reciprocal-separation condition number to infinity, while the boundary-layer normalization keeps it finite and converges to `sinh(u)/(2u)`. This is exactly the kind of source-forced scale test the line needs before deciding that a downstream compression has preserved useful structure rather than merely exact information.