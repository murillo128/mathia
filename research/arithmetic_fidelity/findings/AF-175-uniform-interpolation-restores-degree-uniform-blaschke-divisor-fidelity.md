# AF-175 — Uniform interpolation restores degree-uniform Blaschke divisor fidelity

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `QUANTITATIVE-RECOVERY`, `CONDITIONING-CLASSIFICATION`, `POSITIVE-RECOVERY`, `NO-NOVELTY-CLAIM`

## Claim

AF-174 gives a global fixed-degree inverse modulus from the complete finite Blaschke inner factor modulo output phase to its zero divisor, but its worst-case exponent `1/n` cannot be uniform in degree. That loss is not forced by degree alone. On a class whose zero divisors remain uniformly interpolating, quotient `H^\infty` closeness gives a **degree-independent local recovery modulus** for the entire multiplicity-aware divisor.

Let

\[
B(z)=\eta\prod_{i=1}^n\phi_{a_i}(z),
\qquad
C(z)=\xi\prod_{j=1}^n\phi_{b_j}(z),
\qquad
\phi_a(z)=\frac{z-a}{1-\overline a z},
\tag{1}
\]

be finite Blaschke products of the same degree `n`, and define

\[
\Delta(B,C)
=
\inf_{|\lambda|=1}\|B-\lambda C\|_{H^\infty}.
\tag{2}
\]

For a finite Blaschke product with simple zeros define its interpolation/separation constant

\[
\delta(B)
=
\min_i (1-|a_i|^2)|B'(a_i)|
=
\min_i\prod_{k\ne i}\rho(a_i,a_k),
\qquad
\rho(z,w)=\left|\frac{z-w}{1-\overline w z}\right|.
\tag{3}
\]

Assume

\[
\delta(B)\ge \delta,
\qquad 0<\delta<1.
\tag{4}
\]

Put

\[
q_\delta
=
\frac{1-\sqrt{1-\delta^2}}{\delta}
=
\frac{\delta}{1+\sqrt{1-\delta^2}},
\tag{5}
\]

and for `0\le t<q_\delta^2` define

\[
\omega_\delta(t)
=
\frac{\delta(1+t)-\sqrt{\delta^2(1+t)^2-4t}}{2}.
\tag{6}
\]

Then whenever

\[
\Delta(B,C)<q_\delta^2,
\tag{7}
\]

the zero divisors, counted with multiplicity, satisfy

\[
\boxed{
 d_{\mathrm{div}}^\rho(B,C)
 \le \omega_\delta\!\left(\Delta(B,C)\right),
}
\tag{8}
\]

where

\[
d_{\mathrm{div}}^\rho(B,C)
=
\min_{\sigma\in S_n}\max_i\rho(a_i,b_{\sigma(i)}).
\tag{9}
\]

The modulus is locally Lipschitz:

\[
\omega_\delta(t)=\frac{t}{\delta}+O_\delta(t^2)
\qquad (t\downarrow0).
\tag{10}
\]

Thus a family with one degree-independent lower bound `\delta(B)\ge\delta>0` has a degree-independent local inverse modulus from the complete gauge-quotiented inner function to its divisor. No separation hypothesis on `C` is needed in advance: sufficiently small `\Delta` plus equal degree forces exactly one zero of `C` into each separated Hoffman disk around a zero of `B`.

This identifies the conditioning parameter that AF-170--AF-174 left implicit. The global `1/n` exponent in AF-174 pays for arbitrary multiplicity splitting and arbitrarily collapsing separation. Once a uniform interpolation constant excludes those degeneracies, the inverse is locally linear and the degree disappears from the recovery law.

## Derivation

### Hoffman sublevel geometry gives a uniform zero neighborhood

For fixed `0<\delta<1`, define

\[
h_\delta(r)
=
\frac{r(\delta-r)}{1-\delta r}.
\tag{11}
\]

Hoffman's lemma for interpolating Blaschke products states that if `\delta(B)\ge\delta` and

\[
0<r<q_\delta,
\qquad
0<\varepsilon<h_\delta(r),
\tag{12}
\]

then the pseudohyperbolic disks

\[
D_\rho(a_i,r)=\{z:\rho(z,a_i)<r\}
\tag{13}
\]

are pairwise disjoint and

\[
\{|B|<\varepsilon\}
\subset
\{z:\rho(z,Z(B))<r\}.
\tag{14}
\]

Equivalently, on the boundary of every disk in `(13)`,

\[
|B(z)|\ge \varepsilon.
\tag{15}
\]

The quantitative constants are classical. The endpoint `q_\delta` is exactly the critical point of `h_\delta`, because

\[
h_\delta'(r)
=
\frac{\delta r^2+\delta-2r}{(1-\delta r)^2},
\tag{16}
\]

so `h_\delta` is strictly increasing on `[0,q_\delta]`. Using

\[
\delta(1+q_\delta^2)=2q_\delta,
\tag{17}
\]

one also gets

\[
h_\delta(q_\delta)=q_\delta^2.
\tag{18}
\]

### Rouche counting turns the sublevel inclusion into divisor recovery

The infimum in `(2)` is attained because the unit circle is compact and the norm depends continuously on `\lambda`. Choose a minimizing phase `\lambda_*`.

Take any radius

\[
\omega_\delta(\Delta)<r<q_\delta.
\tag{19}
\]

By construction of `\omega_\delta`, equation `(6)` is the smaller solution of

\[
t=h_\delta(r),
\tag{20}
\]

or equivalently

\[
r^2-\delta(1+t)r+t=0.
\tag{21}
\]

Since `h_\delta` is increasing on the admissible interval,

\[
\Delta<h_\delta(r).
\tag{22}
\]

Choose `\varepsilon` with

\[
\Delta<\varepsilon<h_\delta(r).
\tag{23}
\]

Hoffman's lemma gives `(15)`. Hence on every boundary `\partial D_\rho(a_i,r)`,

\[
|B-\lambda_*C|
\le \Delta
<\varepsilon
\le |B|.
\tag{24}
\]

Each pseudohyperbolic disk is an ordinary Euclidean disk, so Rouche's theorem applies. The function `B` has exactly one zero in each disk because the disks are pairwise disjoint and `(4)` excludes multiple zeros. Therefore `\lambda_*C` also has exactly one zero, counted with multiplicity, in each disk.

There are `n` disks and `C` has degree `n`, so these are all zeros of `C`. Matching each `a_i` to the unique `C` zero in its disk yields

\[
d_{\mathrm{div}}^\rho(B,C)<r.
\tag{25}
\]

Let `r\downarrow\omega_\delta(\Delta)` to obtain `(8)`.

Expanding the smaller quadratic root `(6)` at `t=0` gives `(10)`. The local inverse constant is therefore controlled by the interpolation constant rather than by the number of zeros.

### The cyclic families expose exactly when the separation constant collapses

The regular cyclic family used in AF-170--AF-173 can be written

\[
B_{n,a}(z)
=
\frac{z^n-a}{1-\overline a z^n},
\qquad a\in\mathbb D.
\tag{26}
\]

Its zeros have common radius

\[
r=|a|^{1/n}.
\tag{27}
\]

At any zero `\alpha`, direct differentiation gives

\[
|B_{n,a}'(\alpha)|
=
\frac{n r^{n-1}}{1-r^{2n}},
\tag{28}
\]

and hence the exact interpolation constant is

\[
\boxed{
\delta(B_{n,a})
=
\frac{n r^{n-1}(1-r^2)}{1-r^{2n}}.
}
\tag{29}
\]

This single quantity separates the two asymptotic regimes already seen in the preceding findings.

If the zero radius is fixed, `0<r<1`, then

\[
\delta(B_{n,r^n})
=
\frac{n r^{n-1}(1-r^2)}{1-r^{2n}}
\longrightarrow0
\tag{30}
\]

exponentially up to the polynomial factor `n`. This is exactly the AF-170 regime in which complete inner factors can become arbitrarily close while the unscaled source divisors remain macroscopically distinct. The family exits every uniform-interpolation class, so `(8)` supplies no degree-uniform rescue.

In the boundary-layer scaling

\[
a=e^{-u+i\theta},
\qquad
r=e^{-u/n},
\tag{31}
\]

one instead has

\[
\delta_n(u)
=
\frac{n e^{-u(n-1)/n}(1-e^{-2u/n})}{1-e^{-2u}}
\longrightarrow
\frac{u}{\sinh u}.
\tag{32}
\]

The convergence is uniform for `u` in every compact interval `0<c\le u\le d<\infty`. Consequently such a boundary-layer family has

\[
\inf_{n\ge n_0,\ u\in[c,d]}\delta_n(u)>0
\tag{33}
\]

for sufficiently large `n_0`. It therefore lies in a degree-uniform Hoffman regime. Combined with AF-173's exact quotient identity on the cyclic stratum,

\[
\Delta(B_{n,a},B_{n,b})=2\rho(a,b),
\tag{34}
\]

this shows that the positive boundary-layer behavior is not an accidental coordinate effect: its zero configurations retain a nondegenerate interpolation constant while the fixed-radius configurations lose it.

## Prior art and novelty assessment

The mathematical engine is classical and no theorem-level novelty is claimed.

- Kenneth Hoffman, **“Bounded Analytic Functions and Gleason Parts,”** *Annals of Mathematics* 86(1), 74--111 (1967), DOI `10.2307/1970361`, is a foundational source for the `H^\infty` geometry underlying the interpolating-Blaschke sublevel estimates.
- A. Kerr-Lawson, **“Some Lemmas on Interpolating Blaschke Products and a Correction,”** *Canadian Journal of Mathematics* 21, 531--534 (1969), DOI `10.4153/CJM-1969-060-2`, explicitly records the classical fact that an interpolating Blaschke product is bounded away from zero outside fixed pseudohyperbolic neighborhoods of its zero set and attributes the corrected proof to Hoffman.
- Joseph Cima and Raymond Mortini, **“One-component inner functions,”** *Complex Analysis and its Synergies* 3, article 2 (2017), DOI `10.1186/s40627-016-0008-8`, states a quantitative Hoffman lemma in precisely the normalization used here: if `\delta(B)\ge\delta`, then for `r<q_\delta` and `\varepsilon<h_\delta(r)` the radius-`r` zero disks are disjoint and the `\varepsilon`-sublevel set lies inside them.
- John B. Garnett, ***Bounded Analytic Functions***, Graduate Texts in Mathematics 236, Springer (2007), is a standard modern reference for interpolating sequences, Blaschke products, pseudohyperbolic geometry, and Carleson separation.

The passage from the quantitative Hoffman sublevel estimate to `(8)` is the direct Rouche perturbation argument above. A targeted search found the expected mature theory of interpolating and Carleson--Newman Blaschke products, sublevel-set localization, and zero-set geometry. It did not justify treating the recovery theorem as new complex analysis.

The Arithmetic Fidelity contribution is its placement as the missing conditioning law behind AF-170--AF-174: **degree is not itself the destructive variable**. Global root-splitting gives the `1/n` worst case when multiplicities or clusters are admitted, while a uniform interpolation constant converts the same complete gauge-quotient representation into a degree-independent locally Lipschitz inverse. Formula `(29)` then diagnoses the earlier cyclic positive and negative examples with one intrinsic source parameter.

## Boundary conditions and falsification checks

- The theorem assumes equal known degree. If degree is itself forgotten, it must first be recovered from winding number or another retained datum.
- The reference product `B` must have simple zeros and `\delta(B)\ge\delta>0`. Multiple zeros force `\delta(B)=0`, exactly matching AF-174's `1/n` multiplicity-splitting obstruction.
- Pairwise nearest-neighbor separation alone is not the same as a uniform Carleson interpolation constant for arbitrary large families. The relevant hypothesis is the product/derivative quantity `(3)`.
- The conclusion uses the pseudohyperbolic bottleneck metric. Euclidean or degree-rescaled source metrics require an explicit comparison in the regime being studied; AF-171--AF-173 already show why the scale cannot be selected after the fact.
- The small-error threshold `q_\delta^2` is inherited from the explicit Hoffman constants and is not claimed optimal for finite products. The important point is that it depends on `\delta`, not on `n`.
- No separation assumption on `C` is needed only because the products have equal degree and Rouche counting places exactly one target zero in each of the `n` disjoint reference disks. Without equal degree, extra target zeros could remain outside those disks.
- Quotienting by one unimodular output scalar is harmless for zero-divisor recovery. A larger gauge group could identify different divisors and would need a new audit.
- Formula `(32)` addresses compact positive boundary-layer windows. Sending `u\to\infty` drives `u/\sinh u` to zero, so the uniform modulus can fail again even in boundary-layer coordinates if the source window itself degenerates.

## Research consequence

The next generic Blaschke-fidelity question should no longer be phrased as whether high degree necessarily destroys recovery. The sharper audit is whether the source class retains a quantitative interpolation constant in the metric consumed downstream. If it does, complete-inner-factor recovery is locally degree-uniform; if it does not, one must determine whether the collapse comes from multiplicity, clustering, radial attenuation, or another explicit conditioning defect before introducing additional marks.

For Arithmetic Fidelity more broadly, this supplies a concrete model of a reusable principle: an injective compressed representation can have radically different asymptotic fidelity on two source strata even when the destination map is unchanged. The decisive extra datum is not another side channel but a **source regularity modulus** controlling how close distinct fibers can approach after compression.