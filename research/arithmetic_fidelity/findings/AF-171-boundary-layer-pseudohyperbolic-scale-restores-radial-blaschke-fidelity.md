# AF-171 — Boundary-layer pseudohyperbolic scale restores radial Blaschke fidelity

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `QUANTITATIVE-RECOVERY`, `PHASE/ORIENTATION`, `SCALE-CLASSIFICATION`, `POSITIVE-RECOVERY`, `NO-NOVELTY-CLAIM`

## Claim

AF-170 shows that the complete finite Blaschke inner factor can lose every degree-uniform recovery modulus for a fixed-interior regular radial family. The same family admits an exact complementary classification: the loss is governed not merely by degree, but by the pseudohyperbolic separation of the compressed radial parameters `r^n` and `s^n`. This identifies a critical `1/n` boundary layer in which the full inner factor again has a degree-uniform quantitative relation to the appropriately rescaled divisor endpoint.

For

\[
A_{n,r}=\{r\omega_n^j:0\le j<n\},
\qquad
\omega_n=e^{2\pi i/n},
\qquad 0<r<s<1,
\]

use the fixed normalization from AF-170

\[
B_{n,r}(z)=\frac{z^n-r^n}{1-r^n z^n}.
\tag{1}
\]

Let

\[
\rho(a,b)=\frac{|a-b|}{|1-ab|}
\qquad (a,b\in(0,1))
\tag{2}
\]

be the real-diameter specialization of the pseudohyperbolic distance in the disk. Then the ordinary bounded-analytic distance of the complete inner factors is **exactly**

\[
\boxed{
\|B_{n,s}-B_{n,r}\|_{H^\infty}
=2\rho(r^n,s^n)
=\frac{2(s^n-r^n)}{1-r^n s^n}.
}
\tag{3}
\]

Thus AF-170's fixed-interior collapse has an exact criterion: for any radial sequences `r_n<s_n`, the retained full-inner-factor discrepancy tends to zero exactly when

\[
\rho(r_n^n,s_n^n)\longrightarrow0.
\tag{4}
\]

Now introduce the degree-adapted radial coordinates

\[
u_n=-n\log r_n,
\qquad
v_n=-n\log s_n,
\qquad u_n>v_n>0.
\tag{5}
\]

Since `r_n^n=e^{-u_n}` and `s_n^n=e^{-v_n}`, `(3)` becomes

\[
\boxed{
\|B_{n,s_n}-B_{n,r_n}\|_{H^\infty}
=
2\frac{\sinh((u_n-v_n)/2)}{\sinh((u_n+v_n)/2)}.
}
\tag{6}
\]

In particular, on every fixed compact boundary-layer window

\[
0<\alpha\le u,v\le\beta<\infty,
\tag{7}
\]

the full inner-factor metric is uniformly bi-Lipschitz equivalent to the rescaled radial coordinate difference:

\[
\boxed{
\frac{|u-v|}{\sinh\beta}
\le
\|B_{n,e^{-v/n}}-B_{n,e^{-u/n}}\|_{H^\infty}
\le
\frac{\cosh((\beta-\alpha)/2)}{\sinh\alpha}|u-v|.
}
\tag{8}
\]

Meanwhile the divisor bottleneck distance is exactly `|e^{-v/n}-e^{-u/n}|`, so

\[
\boxed{
n\,d(A_{n,e^{-u/n}},A_{n,e^{-v/n}})
\longrightarrow |u-v|
}
\tag{9}
\]

uniformly for `u,v` in a compact window. Therefore the same complete inner-factor representation that is asymptotically non-faithful for a fixed unscaled interior endpoint is quantitatively faithful, with degree-independent constants, to the **boundary-layer-scaled radial endpoint**.

The structural conclusion is not that one should always renormalize by degree. It is that an asymptotic fidelity statement has a genuine scale phase diagram. On this exact family, `r^n` is the forward radial coordinate selected intrinsically by the Blaschke factorization, `u=-n\log r` is its logarithmic boundary-layer coordinate, and the ordinary `H^\infty` metric sees pseudohyperbolic rather than Euclidean separation after compression. A recovery theorem must match its endpoint geometry to that actual retained scale.

## Derivation

### The `H^\infty` distance is exactly pseudohyperbolic

Write

\[
f_a(w)=\frac{w-a}{1-aw},
\qquad 0\le a<1,
\tag{10}
\]

so that `B_{n,r}(z)=f_{r^n}(z^n)`. The map `z\mapsto z^n` is onto the unit circle, and the difference of two finite Blaschke products is continuous on the closed disk. By the maximum-modulus principle,

\[
\|B_{n,s}-B_{n,r}\|_{H^\infty}
=
\|f_b-f_a\|_{H^\infty},
\qquad a=r^n,\ b=s^n.
\tag{11}
\]

The inverse of `f_a` is

\[
f_a^{-1}(\xi)=\frac{\xi+a}{1+a\xi}.
\tag{12}
\]

For

\[
c=\frac{b-a}{1-ab}=\rho(a,b),
\tag{13}
\]

a direct substitution gives

\[
f_b(f_a^{-1}(\xi))=\frac{\xi-c}{1-c\xi}.
\tag{14}
\]

Because `f_a` maps the unit circle bijectively to itself, the desired boundary supremum is the supremum of

\[
\left|\frac{\xi-c}{1-c\xi}-\xi\right|
=
c\frac{|\xi^2-1|}{|1-c\xi|}
\tag{15}
\]

over `|\xi|=1`. Put `x=\operatorname{Re}\xi`. Then

\[
\left|\frac{\xi-c}{1-c\xi}-\xi\right|^2
=
4c^2\frac{1-x^2}{1+c^2-2cx}.
\tag{16}
\]

The quotient in `(16)` is at most one because

\[
1-x^2\le1+c^2-2cx
\iff
(x-c)^2\ge0,
\tag{17}
\]

and equality is attained whenever `\operatorname{Re}\xi=c`. Hence the supremum equals `2c`, proving `(3)`.

This improves the upper estimate in AF-170 to an exact identity. In particular, no hidden boundary point or denominator estimate changes the asymptotic threshold: the whole collapse is precisely the pseudohyperbolic contraction of the pair `(r^n,s^n)`.

### Logarithmic boundary-layer coordinates expose the critical scale

Set

\[
a=e^{-u},\qquad b=e^{-v},\qquad u>v>0.
\]

Multiplying numerator and denominator of `(13)` by `e^{(u+v)/2}` gives

\[
\rho(e^{-u},e^{-v})
=
\frac{\sinh((u-v)/2)}{\sinh((u+v)/2)},
\tag{18}
\]

which proves `(6)`.

For `u,v\in[\alpha,\beta]`, let `h=|u-v|`. Since

\[
2\sinh(h/2)\ge h,
\qquad
\sinh((u+v)/2)\le\sinh\beta,
\]

we obtain the lower bound in `(8)`. Also

\[
2\sinh(h/2)
\le h\cosh((\beta-\alpha)/2),
\qquad
\sinh((u+v)/2)\ge\sinh\alpha,
\]

which gives the upper bound. The constants depend only on the declared boundary-layer window, not on degree.

The corresponding divisor bottleneck distance remains the exact radial difference

\[
d(A_{n,r},A_{n,s})=s-r.
\tag{19}
\]

For `r=e^{-u/n}`, `s=e^{-v/n}`, the mean-value theorem gives, for some `\theta` between `u` and `v`,

\[
n(s-r)=|u-v|e^{-\theta/n}.
\tag{20}
\]

On every fixed compact `u,v` window this converges uniformly to `|u-v|`, proving `(9)`. Equations `(8)--(9)` therefore give a degree-uniform two-sided comparison between retained `H^\infty` data and the scaled radial divisor endpoint in the `1/n` boundary layer.

### Fixed-interior and boundary-layer regimes are two sides of one formula

If `r<1` is fixed, then `u_n=-n\log r\to\infty`; similarly for fixed `s<1`. The lower constant in `(8)` is not available on such an escaping window, and `(3)` reduces to the exponential collapse already exhibited by AF-170.

If instead

\[
r_n=e^{-u/n},\qquad s_n=e^{-v/n}
\]

with fixed positive `u>v`, then `r_n,s_n\to1`, while `r_n^n=e^{-u}` and `s_n^n=e^{-v}` remain separated in the intrinsic compressed coordinate. The complete inner factors therefore stay a fixed positive `H^\infty` distance apart even though their ordinary Euclidean divisor distance is only `Theta(1/n)`.

This is why appending an arbitrary degree-dependent amplification would be the wrong interpretation. The degree enters before any external reweighting: the regular divisor itself factors through `z^n` and sends the radius to `r^n`. The boundary-layer variable `u=-\log(r^n)` is simply a coordinate on that exact retained parameter.

## Prior art and novelty assessment

The ingredients are classical and no novelty is claimed for disk automorphisms, pseudohyperbolic distance, finite Blaschke products, or the hyperbolic geometry of the unit disk.

- Stephan Ramon Garcia, Javad Mashreghi, and William T. Ross, ***Finite Blaschke Products and Their Connections***, Springer (2018), DOI `10.1007/978-3-319-78247-8`, is a modern monograph covering finite Blaschke products, Möbius transformations, zeros, mapping properties, and their connections with hyperbolic geometry.
- The standard disk pseudohyperbolic metric is `\rho(z,w)=|(z-w)/(1-\overline z w)|`; modern analytic-function-space treatments use its automorphism invariance as basic background. For example, Alejandro Miralles, **“Lipschitz continuity of the dilation of Bloch functions on the unit ball of a Hilbert space and applications,”** *Annals of Functional Analysis* 15, 17 (2024), DOI `10.1007/s43034-024-00317-0`, records the disk formula and its automorphism interpretation before extending related estimates to Hilbert balls.

A targeted literature search found extensive classical and modern use of pseudohyperbolic geometry for Blaschke products and disk automorphisms, but no novelty claim is needed for the elementary exact identity `(3)` or the change of variables `(5)`. The Arithmetic Fidelity contribution is the **scale audit of AF-170's matched family**: the negative fixed-interior example has an exact pseudohyperbolic control parameter, and that formula identifies a positive `1/n` boundary-layer regime where full-inner-factor data and the appropriately scaled divisor endpoint are uniformly comparable.

## Boundary conditions and falsification checks

- The theorem is restricted to the regular radial divisors `A_{n,r}` with the fixed common normalization `(1)`. It does not classify arbitrary degree-`n` Blaschke zero sets.
- The exact `H^\infty` formula depends on comparing the normalized products themselves. Allowing independent arbitrary unimodular factors changes the metric and requires minimizing over that gauge before claiming the same constant.
- The positive recovery statement concerns the scaled radial endpoint, equivalently the compact `u=-n\log r` profile. It does **not** contradict AF-170: for the ordinary unscaled divisor metric, boundary-layer endpoint separations themselves shrink like `1/n`.
- Compactness away from both `u=0` and `u=\infty` is material to the uniform bi-Lipschitz constants in `(8)`. As `u\downarrow0`, the compressed radius `e^{-u}` approaches the boundary and the hyperbolic geometry becomes strongly nonlinear; as `u\to\infty`, the lower recovery constant collapses, reproducing the fixed-interior attenuation regime.
- Equation `(4)` is exact for this family and metric. It says nothing about a different norm on inner functions, a phase-derivative norm, or a noise model that does not control `H^\infty` discrepancy.
- The coordinate `u=-n\log r` is intrinsic to this symmetric factorization but is not asserted to be a universal coordinate for an arbitrary divisor. A general application must derive its own retained scale from its exact compression rather than import `1/n` by analogy.
- No RH consequence follows directly. A transfer would need an independently justified arithmetic family whose natural analytic compression has an analogous boundary-layer regime and whose destination theorem consumes the corresponding scaled endpoint.

## Consequences for the research line

AF-170 left one precise escape: perhaps an admissible arithmetic family lives outside the fixed-interior attenuation regime. AF-171 resolves that escape on the same regular test family. The complete inner factor has an exact scale coordinate, and the transition is not binary: fixed-interior radial distinctions become exponentially invisible, while `1/n` boundary-layer distinctions remain visible in pseudohyperbolic `r^n` geometry and are uniformly comparable to the degree-rescaled divisor endpoint.

This sharpens the line-wide quantitative rule. It is not enough to ask whether a representation is complete, or even whether its inverse is stable for each finite size. One must identify the **asymptotic target scale actually consumed downstream** and compare it with the geometry induced by the retained representation. A direction that collapses in one endpoint metric can remain faithfully encoded after a justified change of endpoint scale; conversely, an arbitrary renormalization has no force unless the compression itself supplies that scale.

For future arithmetic instantiations, the useful audit is therefore three-part: derive the exact compressed coordinate, identify the scaling window in which it has a nondegenerate metric, and prove that the downstream arithmetic endpoint is naturally measured on the same scale. The present regular Blaschke family provides an exact positive/negative control pair for that test.