# AF-172 — Cyclic Blaschke quotient has cylindrical boundary-layer fidelity

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `QUANTITATIVE-RECOVERY`, `PHASE/ORIENTATION`, `QUOTIENT-GEOMETRY`, `SCALE-CLASSIFICATION`, `POSITIVE-RECOVERY`, `NO-NOVELTY-CLAIM`

## Claim

AF-171 identifies the exact radial boundary-layer scale for regular finite Blaschke divisors. The same symmetric family has a two-dimensional completion in which radius and orientation are not independent ad hoc marks: after quotienting by permutation of the roots they combine into one exact complex coefficient.

For `n>=1` and `alpha` in the punctured unit disk, define the unordered cyclic divisor

\[
Z_n(\alpha)=\{z\in\mathbb D:z^n=\alpha\}
\tag{1}
\]

and the normalized finite Blaschke product

\[
B_{n,\alpha}(z)
=\frac{z^n-\alpha}{1-\overline\alpha z^n}.
\tag{2}
\]

The parameter `alpha` is intrinsic to the unordered divisor: it is, up to the fixed Vieta sign, the product of the roots, and it is also read directly from the retained analytic representation through

\[
B_{n,\alpha}(0)=-\alpha.
\tag{3}
\]

Write

\[
\alpha=e^{-u+i\theta},\qquad
\beta=e^{-v+i\psi},
\tag{4}
\]

and let

\[
\delta=d_{\mathbb T}(\theta,\psi)\in[0,\pi]
\tag{5}
\]

be the shortest angular distance modulo `2pi`. Define the logarithmic-polar quotient metric

\[
D_{\mathrm{cyl}}(\alpha,\beta)
=\sqrt{(u-v)^2+\delta^2}.
\tag{6}
\]

Then the bottleneck matching distance `d_n` between the two unordered root divisors is exactly

\[
\boxed{
 d_n(Z_n(\alpha),Z_n(\beta))^2
 =
 (e^{-u/n}-e^{-v/n})^2
 +4e^{-(u+v)/n}\sin^2\!\left(\frac{\delta}{2n}\right).
}
\tag{7}
\]

Consequently, on every fixed compact logarithmic annulus

\[
0<a\le u,v\le b<\infty,
\tag{8}
\]

one has for every `n`

\[
\boxed{
\frac{2}{\pi}e^{-b/n}D_{\mathrm{cyl}}(\alpha,\beta)
\le
n\,d_n(Z_n(\alpha),Z_n(\beta))
\le
D_{\mathrm{cyl}}(\alpha,\beta),
}
\tag{9}
\]

and, uniformly on `(8)`,

\[
\boxed{
n\,d_n(Z_n(\alpha),Z_n(\beta))
\longrightarrow
D_{\mathrm{cyl}}(\alpha,\beta).
}
\tag{10}
\]

The full Blaschke representation sees the same two-dimensional quotient scale. Put `R=e^{-a}<1`. Since `(3)` gives a point evaluation lower bound and direct subtraction in `(2)` gives a uniform parameter Lipschitz bound,

\[
\boxed{
|\alpha-\beta|
\le
\|B_{n,\alpha}-B_{n,\beta}\|_{H^\infty}
\le
\frac{2(1+R)}{(1-R)^2}|\alpha-\beta|.
}
\tag{11}
\]

Meanwhile

\[
|\alpha-\beta|^2
=(e^{-u}-e^{-v})^2
+4e^{-(u+v)}\sin^2(\delta/2),
\tag{12}
\]

so on `(8)`

\[
\boxed{
\frac{2}{\pi}e^{-b}D_{\mathrm{cyl}}(\alpha,\beta)
\le
|\alpha-\beta|
\le
e^{-a}D_{\mathrm{cyl}}(\alpha,\beta).
}
\tag{13}
\]

Thus the complete normalized inner factor is uniformly bi-Lipschitz to the same compact cylindrical quotient geometry that appears as the `n`-rescaled source bottleneck limit. AF-171's radial coordinate `u=-n\log r` is therefore one axis of a source-forced two-dimensional boundary layer; the second is the quotient orientation `theta=arg alpha`, whose physical root rotation is `theta/n` modulo the cyclic symmetry.

The structural conclusion is stronger than a radial rescaling rule. On this cyclic stratum, permutation quotient, endpoint metric, orientation provenance, and asymptotic normalization are all forced by one exact retained coefficient `alpha`. A phase/orientation mark need not be appended separately when the compression already transports the symmetric complex coefficient that carries it.

## Derivation

### The unordered divisor collapses exactly to one complex coefficient

The roots of `z^n-alpha` form one regular `n`-gon. If `alpha=e^{-u+i theta}`, they can be written

\[
a_j=e^{-u/n}e^{i(\theta+2\pi j)/n},
\qquad 0\le j<n.
\tag{14}
\]

By Vieta,

\[
\prod_{j=0}^{n-1}a_j=(-1)^{n+1}\alpha.
\tag{15}
\]

Thus `alpha` is a symmetric function of the unordered divisor rather than a labeling choice. The numerator and denominator factor as

\[
\prod_j(z-a_j)=z^n-\alpha,
\qquad
\prod_j(1-\overline{a_j}z)=1-\overline\alpha z^n,
\tag{16}
\]

which gives `(2)` and `(3)`.

A rigid rotation of the root set by angle `phi` sends `alpha` to `e^{in phi}alpha`. Rotations differing by `2pi/n` produce the same unordered set, so `arg alpha` is exactly the angular coordinate left after the cyclic/permutation quotient. This is why the relevant root-level angular displacement is `delta/n`, not `delta`.

### Bottleneck matching has an exact cyclic formula

Let

\[
r=e^{-u/n},\qquad s=e^{-v/n}.
\]

Every root of `Z_n(alpha)` sees the same set of angular offsets to `Z_n(beta)`. The nearest target root differs in angle by exactly `delta/n`; choosing that nearest cyclic shift for every root gives a bijection. No other matching can improve the maximum distance because no root has any target point at a smaller angular separation.

The Euclidean distance of one optimally matched pair is therefore

\[
|re^{it}-se^{i(t+\delta/n)}|^2
=r^2+s^2-2rs\cos(\delta/n),
\tag{17}
\]

which is `(7)` after using `1-cos x=2sin^2(x/2)`.

Multiplying `(7)` by `n^2` separates radial and angular terms:

\[
n^2d_n^2
=\bigl[n(e^{-u/n}-e^{-v/n})\bigr]^2
+\biggl[2n e^{-(u+v)/(2n)}
\sin\!\left(\frac{\delta}{2n}\right)\biggr]^2.
\tag{18}
\]

The mean-value theorem gives

\[
e^{-b/n}|u-v|
\le
n|e^{-u/n}-e^{-v/n}|
\le
|u-v|.
\tag{19}
\]

For `0<=x<=pi/2`,

\[
\frac{2}{\pi}x\le\sin x\le x.
\tag{20}
\]

Since `0<=delta/(2n)<=pi/2`, the angular term in `(18)` lies between

\[
\frac{2}{\pi}e^{-b/n}\delta
\quad\text{and}\quad
\delta.
\tag{21}
\]

Combining `(19)` and `(21)` proves `(9)`. Each component in `(18)` converges uniformly on the compact parameter set to the corresponding component of `(6)`, proving `(10)`.

### The analytic representation carries the same quotient coordinate stably

Write for `w` in the closed unit disk

\[
F_\alpha(w)=\frac{w-\alpha}{1-\overline\alpha w}.
\tag{22}
\]

Because `z->z^n` maps the unit disk onto itself,

\[
\|B_{n,\alpha}-B_{n,\beta}\|_{H^\infty}
=\|F_\alpha-F_\beta\|_{H^\infty}.
\tag{23}
\]

At `w=0`, `F_alpha(0)=-alpha`, giving the lower bound in `(11)`. Direct subtraction gives

\[
F_\alpha(w)-F_\beta(w)
=
\frac{(\beta-\alpha)+(\overline\alpha-\overline\beta)w^2
+(\alpha\overline\beta-\beta\overline\alpha)w}
{(1-\overline\alpha w)(1-\overline\beta w)}.
\tag{24}
\]

On `(8)`, `|alpha|,|beta|<=R`. The numerator in `(24)` is at most

\[
2(1+R)|\alpha-\beta|,
\tag{25}
\]

while the denominator has modulus at least `(1-R)^2`. This proves the upper bound in `(11)`.

Finally, `(12)` is the polar chord identity. On `[a,b]`, the radial mean-value estimate gives

\[
e^{-b}|u-v|
\le
|e^{-u}-e^{-v}|
\le
e^{-a}|u-v|,
\tag{26}
\]

and `(20)` gives

\[
\frac{2}{\pi}e^{-b}\delta
\le
2e^{-(u+v)/2}\sin(\delta/2)
\le
e^{-a}\delta.
\tag{27}
\]

Equations `(26)--(27)` imply `(13)`. Together with `(9)--(11)`, this gives a common, degree-uniform metric model for the retained analytic data and the rescaled unordered source divisor.

## Prior art and novelty assessment

The ingredients are classical and no novelty is claimed for symmetric products/effective divisors, Vieta coordinates, finite Blaschke products, disk automorphisms, or the elementary geometry of regular polygons.

- I. G. Macdonald, **“Symmetric products of an algebraic curve,”** *Topology* 1(4), 319–343 (1962), DOI `10.1016/0040-9383(62)90019-8`, is classical background for treating unordered degree-`n` point configurations as symmetric products/effective divisors rather than labeled tuples.
- Stephan Ramon Garcia, Javad Mashreghi, and William T. Ross, ***Finite Blaschke Products and Their Connections***, Springer (2018), DOI `10.1007/978-3-319-78247-8`, is a modern reference for finite Blaschke products, their zero sets, disk automorphisms, and hyperbolic geometry.
- Garcia, Mashreghi, and Ross, **“Finite Blaschke products: a survey,”** in *Harmonic Analysis, Function Theory, Operator Theory, and Their Applications*, 133–158, Contemporary Mathematics 22 (2018), also surveys the zero geometry and mapping structure of finite Blaschke products; an earlier version is arXiv:`1512.05444`.

A targeted literature search found the expected mature theories of symmetric products, symmetrized domains, finite Blaschke products, and hyperbolic/pseudohyperbolic disk geometry. No claim is made that `(7)--(13)` constitute a new theorem in complex analysis or configuration-space geometry; on this highly symmetric one-complex-parameter stratum they are elementary consequences of those structures.

The Arithmetic Fidelity contribution is the **combined quotient-and-scale audit** following AF-169--AF-171. The radial positive regime is not an isolated one-dimensional trick: the full cyclic divisor quotient has a natural logarithmic-polar cylinder, the source bottleneck metric converges to that cylinder after exactly the forced `n` scaling, and the complete normalized Blaschke factor retains the same complex coefficient with degree-independent conditioning on compact logarithmic annuli.

## Boundary conditions and falsification checks

- The result concerns the cyclic regular stratum `Z_n(alpha)`, not arbitrary degree-`n` divisors. Generic divisors require more than one symmetric coefficient and can have collision/conditioning phenomena absent here.
- The parameter excludes `alpha=0`; the angular coordinate is undefined there and the cyclic divisor collapses to a multiple zero, returning to the multiplicity singularity of AF-168.
- Compactness `a<=u,v<=b` is material. As `a` tends to zero, `|alpha|` approaches the unit circle and the upper constant in `(11)` blows up. As `b` tends to infinity, `alpha` approaches zero and angular provenance becomes metrically cheap before disappearing at the multiple-zero apex.
- The orientation coordinate is quotient orientation, not a labeling of individual roots. Only `arg alpha` modulo `2pi` is retained; a physical rotation by `2pi/n` is already invisible because it permutes the divisor.
- The `n` scaling is not appended after seeing a bad example. It is forced twice: taking `n`-th roots turns the retained logarithmic radius `u=-log|alpha|` into the source radius `e^{-u/n}`, and the quotient phase `arg alpha` into root orientation `arg alpha/n`.
- The H-infinity comparison uses the common normalization `(2)`. Independent arbitrary unimodular factors would introduce an extra gauge and require quotienting or marking that gauge before the same metric statement can be used.
- Equation `(11)` is a compact-annulus bi-Lipschitz estimate, not an exact formula for arbitrary complex `alpha,beta`. AF-171's exact `2 rho` identity is the special real-diameter case; no unsupported complex-parameter extension of that identity is claimed here.
- No RH consequence follows directly. A transfer requires an arithmetic compression with an independently forced complex or relational retained coordinate, a source quotient whose metric scales compatibly, and a downstream theorem that consumes that same endpoint geometry.

## Consequences for the research line

AF-169--AF-171 establish that exact finite completeness, growing-degree stability, and endpoint scale are separate questions. AF-172 adds the missing quotient-orientation dimension on the cleanest symmetric test family. **The correct asymptotic endpoint is not merely a rescaled radius; it is a quotient geometry whose coordinates are exactly the symmetric data transported by the compression.**

This sharpens the line's current provenance rule. Before adding an explicit phase, sign, orientation, or label as a repair, first ask whether an existing symmetric coefficient already transports that provenance through the compression. If it does, derive the metric and scaling induced by that coefficient and compare them with the downstream endpoint. If it does not, only then is an additional mark a genuine candidate lift.

For arithmetic instantiations the next useful audit is therefore: identify the exact retained symmetric/relational coordinate, compute the source quotient it parameterizes, derive the endpoint metric at the asymptotic scale forced by that coordinate, and test whether the destination norm is uniformly comparable. A proposed provenance lift is useful only when it supplies structure not already present in that quotient and remains stable in the metric actually consumed downstream.