# AF-170 — Full Blaschke inner factors lose uniform divisor fidelity in growing degree

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `QUANTITATIVE-RECOVERY`, `PHASE/ORIENTATION`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-167 shows that a degree-`n` finite Blaschke zero divisor is exactly recoverable from a finite phase-gradient moment lift, while AF-168 and AF-169 show that this exact inverse can become badly conditioned as multiplicity, degree, and radial moment attenuation grow. A natural escape is to retain more phase-sensitive information, perhaps even the entire Blaschke inner factor rather than its first `n` moments.

That escape still fails uniformly in the ordinary bounded-analytic norm on a simple matched family. For fixed

\[
0<r<s<1,
\qquad
\omega_n=e^{2\pi i/n},
\]

let

\[
A_{n,r}=\{r\omega_n^j:0\le j<n\},
\qquad
A_{n,s}=\{s\omega_n^j:0\le j<n\}.
\tag{1}
\]

The corresponding finite Blaschke products may be normalized as

\[
B_{n,r}(z)
=\prod_{j=0}^{n-1}
\frac{z-r\omega_n^j}{1-r\omega_n^{-j}z}
=\boxed{\frac{z^n-r^n}{1-r^n z^n}},
\tag{2}
\]

and similarly for `s`. Both have degree `n`, and their full zero divisors remain a fixed positive distance apart:

\[
\boxed{
d(A_{n,r},A_{n,s})=s-r
}
\tag{3}
\]

in bottleneck matching distance.

Nevertheless the **entire inner functions** become uniformly indistinguishable on the closed disk. If `a=r^n` and `b=s^n`, then for

\[
f_a(w)=\frac{w-a}{1-aw}
\]

one has `B_{n,r}(z)=f_a(z^n)` and the exact difference identity

\[
f_b(w)-f_a(w)
=\frac{(b-a)(w^2-1)}{(1-bw)(1-aw)}.
\tag{4}
\]

Hence

\[
\boxed{
\|B_{n,s}-B_{n,r}\|_{H^\infty}
\le
\frac{2(s^n-r^n)}{(1-s^n)(1-r^n)}
\longrightarrow0.
}
\tag{5}
\]

Thus there is no degree-uniform recovery modulus `\Omega(\varepsilon)\to0` for the full divisor endpoint from `(degree, B)` when `B` is measured in the ordinary `H^\infty` norm. The degree coordinate agrees exactly for the matched pair, the complete analytic inner factors converge to one another, yet the target divisors stay distance `s-r` apart.

The failure is not confined to function values or to truncating the phase-gradient Fourier series. Write

\[
B_{n,r}(e^{it})=e^{i\beta_{n,r}(t)}
\]

for a lifted boundary phase. The classical phase-derivative identity gives

\[
\boxed{
\beta_{n,r}'(t)
=nP_{r^n}(e^{int}),
}
\tag{6}
\]

where

\[
P_a(e^{i\theta})
=1+2\sum_{m\ge1}a^m\cos(m\theta)
=\frac{1-a^2}{|e^{i\theta}-a|^2}
\tag{7}
\]

is the Poisson kernel for real `0\le a<1`. Since the Fourier coefficients of `P_b-P_a` are nonnegative when `0\le a<b<1`, the triangle bound is attained at `\theta=0`, yielding

\[
\boxed{
\|\beta_{n,s}'-\beta_{n,r}'\|_{L^\infty(\mathbb T)}
=
\frac{2n(s^n-r^n)}{(1-s^n)(1-r^n)}
\longrightarrow0.
}
\tag{8}
\]

Consequently the complete boundary phase derivative, and therefore every normalized `L^p` discrepancy controlled by its sup norm, can collapse while the full divisor endpoint remains separated. The obstruction in AF-169 is therefore not merely an artifact of retaining only the first `n` monomial moments: **even restoring the complete finite Blaschke inner factor or complete phase derivative does not give growing-degree divisor fidelity unless the chosen data geometry resolves exponentially attenuated interior structure.**

## Derivation

### The regular zero divisor collapses to one disk automorphism after `z^n`

The numerator in `(2)` is the cyclotomic factorization

\[
\prod_{j=0}^{n-1}(z-r\omega_n^j)=z^n-r^n.
\tag{9}
\]

For the denominator, the conjugates of the zeros are `r\omega_n^{-j}`, so

\[
\prod_{j=0}^{n-1}(1-r\omega_n^{-j}z)
=1-r^n z^n.
\tag{10}
\]

This proves `(2)` without any hidden approximation. Each factor `(z-a)/(1-\bar a z)` is inner, so `(2)` is a degree-`n` finite Blaschke product with zero multiset exactly `A_{n,r}`. An alternative standard Blaschke-factor convention changes only a unimodular scalar; `(2)` fixes a common normalization for the matched family.

The radial matching `r\omega_n^j\mapsto s\omega_n^j` has cost `s-r`, proving `d\le s-r`. Conversely the reverse triangle inequality gives

\[
|s\omega_n^k-r\omega_n^j|\ge s-r
\]

for every pair of points, so no permutation can improve the bottleneck cost. This proves `(3)`.

### Full `H^\infty` data collapse exponentially

For `0\le a<b<1`, direct subtraction gives

\[
\frac{w-b}{1-bw}-\frac{w-a}{1-aw}
=
\frac{(b-a)(w^2-1)}{(1-bw)(1-aw)}.
\tag{11}
\]

When `|w|\le1`,

\[
|w^2-1|\le2,
\qquad
|1-aw|\ge1-a,
\qquad
|1-bw|\ge1-b.
\tag{12}
\]

Using `w=z^n`, `a=r^n`, and `b=s^n` gives `(5)`. Because `s<1` is fixed,

\[
\frac{2(s^n-r^n)}{(1-s^n)(1-r^n)}
=O(s^n).
\tag{13}
\]

The forward representation therefore contracts this fixed endpoint separation at an exponential rate.

Suppose there were a degree-independent recovery modulus `\Omega` with `\Omega(t)\to0` as `t\to0` such that, for all equal-degree finite Blaschke products in the family,

\[
d(Z(B),Z(C))
\le
\Omega(\|B-C\|_{H^\infty}).
\tag{14}
\]

Applying `(14)` to `B_{n,r}` and `B_{n,s}` would force

\[
s-r
\le
\Omega\!\left(
\frac{2(s^n-r^n)}{(1-s^n)(1-r^n)}
\right)
\longrightarrow0,
\tag{15}
\]

which is impossible. Including the exact degree in the retained representation does not change the argument because both members have degree `n`.

This is stronger than the raw-moment failure in AF-169. There the representation could plausibly be blamed on a poorly scaled truncated coordinate system. Here the complete bounded analytic function is retained; the instability belongs to the inverse geometry of the growing family under the declared `H^\infty` metric.

### The complete phase derivative collapses as well

For one real disk automorphism

\[
f_a(w)=\frac{w-a}{1-aw},
\]

the boundary phase derivative is the Poisson kernel `P_a`. Equation `(2)` is the composition `f_{r^n}(z^n)`, so the chain rule around the unit circle gives `(6)`.

For `0\le a<b<1`, the Fourier expansion `(7)` yields

\[
P_b(e^{i\theta})-P_a(e^{i\theta})
=2\sum_{m\ge1}(b^m-a^m)\cos(m\theta).
\tag{16}
\]

Therefore

\[
\|P_b-P_a\|_\infty
\le
2\sum_{m\ge1}(b^m-a^m)
=
\frac{2(b-a)}{(1-a)(1-b)}.
\tag{17}
\]

At `\theta=0`, every cosine equals one, so equality holds in `(17)`. Multiplication by the chain-rule factor `n` gives `(8)` exactly.

Since `n s^n\to0` for every fixed `s<1`, even the full phase-gradient profile converges uniformly between the matched families. In particular, for normalized Haar measure on `\mathbb T`,

\[
\|\beta_{n,s}'-\beta_{n,r}'\|_{L^p}
\le
\|\beta_{n,s}'-\beta_{n,r}'\|_\infty
\longrightarrow0
\qquad(1\le p\le\infty).
\tag{18}
\]

Thus retaining all Fourier modes without changing the measurement norm does not repair the asymptotic loss. The missing scale is not hidden in a mode omitted by AF-167; it is exponentially small throughout the ordinary unweighted function geometry for this symmetric family.

### Fixed-degree stability does not contradict the growing-degree obstruction

Finite Blaschke products of fixed degree form a finite-dimensional rigid class, and standard convergence results are correspondingly stronger when the degree is held fixed. For example, Evdoridou--Rempe--Sixsmith prove that if finite Blaschke products of one fixed degree converge locally uniformly to a finite Blaschke product of the same degree, then convergence is uniform on the disk.

The present matched family deliberately leaves that regime: the degree tends to infinity. Indeed, for every fixed interior `z`, both `z^n` and `r^n` tend to zero, so

\[
B_{n,r}(z)\longrightarrow0
\tag{19}
\]

locally uniformly in the open disk. The limit is no longer an inner function of the same degree; it carries none of the growing zero divisor. This is exactly the asymptotic compression that a fixed-degree inverse theorem cannot control.

## Prior art and novelty assessment

All analytic ingredients used above are classical, and no novelty is claimed for finite Blaschke products, the regular-polygon product identity, Poisson kernels, boundary phase derivatives, or fixed-degree convergence theory.

- Stephan Ramon Garcia, Javad Mashreghi, and William T. Ross, ***Finite Blaschke Products and Their Connections***, Springer (2018), DOI `10.1007/978-3-319-78247-8`, is a modern monograph on finite Blaschke products, including their zeros, mapping properties, and analytic/operator structure.
- Tao Qian, **“Boundary derivatives of the phases of inner and outer functions and applications,”** *Mathematical Methods in the Applied Sciences* 32(3), 253--263 (2009), DOI `10.1002/mma.1032`, gives the classical phase-derivative framework for inner functions used in AF-167 and in `(6)--(8)`.
- Vasiliki Evdoridou, Lasse Rempe, and David J. Sixsmith, **“Fatou's Associates,”** *Arnold Mathematical Journal* 6, 459--493 (2020), DOI `10.1007/s40598-020-00148-6`, Proposition 9.1, records the complementary fixed-degree statement that local uniform convergence of finite Blaschke products to a finite Blaschke product of the same degree upgrades to uniform convergence on the disk.

A targeted literature check found established work on finite-Blaschke structure, phase derivatives, convergence, and zero geometry, but no novelty claim is made for the particular closed-form estimates here. The Arithmetic Fidelity contribution is the endpoint-specific **growing-degree matched-control audit**: the exact zero-encoding inner factor itself can become arbitrarily close in a standard analytic norm while its full divisor endpoint remains a fixed distance apart. This closes the most immediate “retain all phase information” escape left open after AF-169 and makes the data norm/noise geometry an explicit part of any scalable recovery claim.

## Boundary conditions and falsification checks

- The conclusion is metric-relative. It rules out a degree-uniform inverse modulus from the ordinary `H^\infty` distance, and from phase-derivative `L^p` distances controlled as in `(18)`, on the declared growing family. It does not say that every possible topology, weighted norm, logarithmic coordinate, or nonlinear representation of a Blaschke product has the same instability.
- The degree is not being forgotten. Both matched objects have the same known degree `n`, so appending exact degree metadata does not separate them.
- The endpoint is the full unordered divisor with bottleneck metric. A coarser endpoint that intentionally identifies the two radii would make this matched pair endpoint-null, exactly as required by AF-165.
- Every zero in `(1)` is simple. Their angular spacing is `Theta(1/n)`, but the forward collapse in `(5)` and `(8)` is exponential in `n`; this remains distinct from the fixed-degree multiplicity singularity of AF-168.
- The family stays uniformly inside the disk at fixed radii `r<s<1`. If an application forces the relevant zeros to approach the boundary with `r_n^n` bounded away from zero, the present attenuation mechanism may disappear. The scale `r_n^n` must then be audited directly.
- A degree-dependent renormalization can magnify the exponentially small difference. Such a renormalization also changes the data/noise geometry and may amplify measurement error by the same factor; it is a new representation requiring an independent stability theorem, not a free consequence of exact recoverability.
- Uniform closeness of two inner functions does not imply closeness of their zero divisors when degree is unbounded; `(1)--(5)` are an explicit witness. This does not contradict Rouché-type root stability when a nonvanishing boundary margin and a fixed finite zero count are controlled.
- Equation `(8)` concerns a continuously lifted phase derivative. Additive phase constants are irrelevant because differentiation removes them; both products have the same winding degree.
- No statement about Riemann-zeta zeros follows directly. An RH-facing transfer must first justify an intrinsic finite-divisor/inner-factor model, the relevant growth of degree and radial scale, and the natural norm or noise model in which retained data are actually available.

## Consequences for the research line

AF-167 identified a sharply finite exact phase lift. AF-168 showed that exact inversion can be Hölder-singular at multiplicity. AF-169 then showed that simple regular divisors can defeat every degree-uniform inverse modulus in the first-`n` raw phase moments through radial attenuation. AF-170 strengthens that frontier: **the same matched family defeats uniform recovery even when the complete inner analytic factor and complete phase derivative are retained in their ordinary norms.**

The scalable-fidelity question must therefore be posed as more than “how much information is retained?” A representation can be exactly complete at every finite stage and still be asymptotically useless because the destination metric compresses a target-relevant direction faster than the endpoint geometry contracts. For a growing arithmetic application, the mandatory data are now: the endpoint quotient, the family geometry, the complete retained representation, and a quantitatively justified norm/noise scale under which its inverse remains useful.

The next escape is correspondingly narrower. A proposed repair must either prove that the admissible arithmetic family avoids this attenuation regime, identify an independently natural representation whose metric does not collapse the relevant direction, or weaken the endpoint so that the collapsed direction is genuinely irrelevant. Merely restoring more Fourier modes, the full phase gradient, or the full finite inner factor is not by itself a scalable recovery theorem.