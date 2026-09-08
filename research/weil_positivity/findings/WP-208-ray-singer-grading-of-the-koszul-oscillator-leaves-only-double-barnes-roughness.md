# WP-208 — Ray–Singer grading of the Koszul oscillator leaves only double-Barnes roughness

**Status:** `DERIVED + EXACT + KOSZUL-GRADING + ANALYTIC-TORSION-CONTROL + DOUBLE-BARNES + ROUGHNESS-BOUND + POLYNOMIAL-GRADING-CLASSIFICATION + POSITIVITY-FORK + PRIOR-ART-AUDITED + DECISIVE-NARROWING + MATCHED-CONTROL + NOT-A-WEIL-BRIDGE`.

`WP-207` leaves a deliberately important escape hatch. The ordinary Koszul cohomology that turns the Barnes finite difference into a positive Hilbert space collapses to one mode and loses the reciprocal Fourier floor, but a determinant line can retain spectral information from acyclic chain directions even when cohomology forgets them. Ray–Singer/Quillen torsion is the canonical classical example: it uses an alternating **degree-weighted** determinant rather than the unweighted Euler superdeterminant.

For the exact `WP-207` Koszul oscillator source, that escape can be calculated completely. The unweighted supertrace reduces the `d`-mode Barnes source to one Euler/Hurwitz mode, while the first degree-weighted supertrace used by analytic torsion reduces it only to a **two-mode Barnes source**:

\[
\operatorname{Str}\!\left(F e^{-tH_{d,a}}\right)
=
-(d-1)\frac{e^{-(a+1)t}}{(1-e^{-t})^2}.
\]

Thus determinant-line torsion really does remember acyclic transverse directions after cohomology has collapsed. But it remembers only a universal double-Barnes multiplicity, independent of how large `d` is. At every allowed Weil-cone order `n=4k>=4`, the corresponding positive double-Barnes magnitude is already in `S^{n-1}` and its centered multiplier satisfies

\[
|\xi|F_{\rm tors}(\xi)\longrightarrow0.
\]

So the standard Ray–Singer grading is still too smooth to provide the `WP-202` reciprocal floor.

More generally, the `k`th polynomial grading moment has an exact finite Barnes expansion whose largest possible Barnes order is `min(k,d-1)+1`. Recovering the original critical `d=n-1` roughness therefore requires

\[
k\ge d-1=n-2.
\]

That is not the Ray–Singer/Quillen determinant-line prescription; it reintroduces an order-dependent grading choice tied to the externally chosen spectral-shift order. Moreover the readout remains a signed supertrace. Taking absolute values can create a positive magnitude but no longer preserves the same graded determinant identity.

The resulting fork is sharper than `WP-207`:

\[
\boxed{
\begin{array}{ccl}
k=0\ \text{Euler supertrace} &:& \text{exact one-mode source, signed cancellation},\\[1mm]
k=1\ \text{Ray--Singer weight} &:& \text{double-Barnes memory, but subcritical roughness},\\[1mm]
k\ge n-2 &:& \text{critical Barnes order can return, but only through a higher signed grading moment}.
\end{array}}
\]

This closes the most canonical determinant-line/torsion repair of the `WP-207` roughness collapse. It does **not** rule out a genuinely global Quillen/intersection construction whose curvature or assembled pairing has an independent sign theorem, nor does it classify higher analytic torsion forms. It shows that ordinary determinant-line torsion of the present Koszul oscillator cannot simultaneously be the source of exact Euler-Gamma cancellation and the critical positive roughness needed by the current higher spectral-shift route.

## 1. The full graded heat trace has one exact generating function

Keep the `WP-207` polynomial/Fock space

\[
S_d=\mathbb C[z_1,\ldots,z_d]
\]

and the Koszul complex on the regular sequence `z_2,...,z_d`. Write

\[
r=d-1,
\qquad
F=\text{exterior/Koszul degree},
\qquad
H_{d,a}=N^{(d)}+F+a,
\qquad a>0.
\]

The differential preserves `N^{(d)}+F`, so `H_{d,a}` is a degree-preserving positive source on the complex. Introduce a bookkeeping variable `y` for exterior degree and put `q=e^{-t}`. Direct factorization of the bosonic and exterior Fock traces gives

\[
\boxed{
Z_d(y,t)
:=
\operatorname{Tr}\!\left(y^F e^{-tH_{d,a}}\right)
=
e^{-at}\frac{(1+yq)^r}{(1-q)^{r+1}}.
}
\tag{1}
\]

Setting `y=-1` recovers `WP-207`:

\[
Z_d(-1,t)
=
\frac{e^{-at}}{1-e^{-t}}.
\tag{2}
\]

Thus the ordinary supertrace is exactly one-mode, independently of `d`.

Equation (1) is also a matched control. It uses no primes, no Riemann shift beyond the freely chosen `a`, no pole term, and no zero data. Any grading effect derived below therefore belongs to the Koszul/Fock architecture itself rather than to arithmetic.

## 2. The Ray–Singer degree weight leaves a double-Barnes source

Let

\[
D_y:=y\frac{\partial}{\partial y}.
\]

Because `D_y y^F=F y^F` degreewise,

\[
\operatorname{Str}\!\left(F e^{-tH_{d,a}}\right)
=
\left.D_y Z_d(y,t)\right|_{y=-1}.
\tag{3}
\]

Differentiating (1) gives

\[
\begin{aligned}
\left.D_y Z_d(y,t)\right|_{y=-1}
&=
e^{-at}
\frac{-r q(1-q)^{r-1}}{(1-q)^{r+1}}\\
&=
\boxed{
-r\,\frac{e^{-(a+1)t}}{(1-e^{-t})^2}.
}
\end{aligned}
\tag{4}
\]

The equal-period Barnes zeta of order two has heat kernel

\[
\frac{e^{-bt}}{(1-e^{-t})^2}
=
\sum_{m\ge0}(m+1)e^{-(m+b)t}.
\tag{5}
\]

Therefore the degree-weighted zeta function associated with the same source is, initially in its convergence half-plane,

\[
\boxed{
\operatorname{Str}\!\left(F H_{d,a}^{-w}\right)
=
-r\,\zeta_2(w,a+1).
}
\tag{6}
\]

Up to the conventional overall sign and factor `1/2`, (6) is exactly the grading pattern entering Ray–Singer analytic torsion: analytic torsion weights the degree-`q` determinant by `(-1)^q q/2`. The key point here is not the convention but the spectral order. The torsion weighting converts the `d`-mode chain source into a **double-Barnes** virtual determinant, not back into the Euler/Hurwitz determinant and not into a `d`-mode positive determinant.

This is a real improvement over taking cohomology: acyclic directions leave determinant-line data. But their surviving multiplicity is only

\[
m+1,
\tag{7}
\]

up to the fixed factor `r=d-1`.

## 3. Double-Barnes memory is too smooth for every allowed Weil order

To give the torsion escape its strongest possible sign-compatible interpretation, discard the minus sign in (4) and ask whether the corresponding **positive** double-Barnes magnitude could supply the `WP-202` rough bath.

Use the positive inverse spectrum

\[
b_m=\frac{\pi}{m+a+1}
\]

with multiplicity `m+1`. Its Schatten sum is

\[
\sum_{m\ge0}(m+1)b_m^s,
\]

which converges exactly for

\[
\boxed{s>2.}
\tag{8}
\]

For every allowed higher spectral-shift order

\[
n=4k\ge4,
\tag{9}
\]

we have `n-1>=3`, hence the positive double-Barnes surrogate lies in

\[
\boxed{\mathcal S^{\,n-1}.}
\tag{10}
\]

The Fourier failure can also be seen directly. With the centered scalar multiplier `F_b(\xi)` of `WP-202`/`WP-206`, define

\[
F_{\rm dbl}(\xi)
=
\sum_{m\ge0}(m+1)
F_{\pi/(m+a+1)}(\xi).
\tag{11}
\]

The elementary bounds already used in `WP-207` are

\[
F_b(\xi)\le \frac{b^n}{n!},
\qquad
F_b(\xi)\le
\frac{2b^{n-2}}{(n-2)!\,\xi^2}.
\tag{12}
\]

Split (11) at `m+a+1=pi|\xi|`. On the tail, the first bound gives

\[
\sum_{m\gtrsim|\xi|}
(m+1)F_{\pi/(m+a+1)}(\xi)
=
O(|\xi|^{2-n}).
\tag{13}
\]

On the head, the second bound gives

\[
\frac{C}{\xi^2}
\sum_{m\lesssim|\xi|}
(m+1)(m+a+1)^{-(n-2)}.
\tag{14}
\]

For `n=4`, (14) is `O(\log|\xi|/\xi^2)`. For `n>=8`, it is `O(|\xi|^{-2})`. Thus in every allowed case

\[
\boxed{
|\xi|F_{\rm dbl}(\xi)\longrightarrow0.
}
\tag{15}
\]

By the exact `WP-202` criterion, even this sign-favorable positive magnitude cannot universally stabilize finite positive payloads. The actual Ray–Singer weighted source is less directly usable because it is a signed supertrace.

## 4. All polynomial grading moments admit an exact Barnes-order bound

The first moment is not an isolated accident. For an integer `k>=1`,

\[
\operatorname{Str}\!\left(F^k e^{-tH_{d,a}}\right)
=
\left.D_y^k Z_d(y,t)\right|_{y=-1}.
\tag{16}
\]

Using

\[
D_y^k
=
\sum_{j=1}^k
\left\{\!\!\begin{matrix}k\\j\end{matrix}\!\!\right\}
y^j\frac{\partial^j}{\partial y^j},
\tag{17}
\]

where braces are Stirling numbers of the second kind, and differentiating `(1+yq)^r`, one obtains the exact formula

\[
\boxed{
\operatorname{Str}\!\left(F^k e^{-tH_{d,a}}\right)
=
e^{-at}
\sum_{j=1}^{\min(k,r)}
\left\{\!\!\begin{matrix}k\\j\end{matrix}\!\!\right\}
(-1)^j r^{\underline j}
\frac{q^j}{(1-q)^{j+1}}.
}
\tag{18}
\]

Each summand is an equal-period Barnes heat kernel of order `j+1`, with a shift and a signed coefficient. Therefore

\[
\boxed{
\text{largest Barnes order in the }F^k\text{ supertrace}
=
\min(k,d-1)+1.
}
\tag{19}
\]

For `k=0`, equation (2) gives Barnes order one. For `k=1`, (19) gives order two, recovering (4). To retain the full original `d`-mode multiplicity one must have

\[
k\ge d-1.
\tag{20}
\]

The coefficient of the top `j=d-1` term is nonzero, so this is a sharp algebraic threshold.

## 5. Recovering critical roughness reintroduces the external order choice

The `WP-206` critical rough bath at spectral-shift order `n` requires

\[
d=n-1.
\tag{21}
\]

Combining (19)--(21), a polynomial grading supertrace can retain Barnes order `n-1` only if

\[
\boxed{k\ge n-2.}
\tag{22}
\]

Thus the canonical first degree moment `k=1` is insufficient for every allowed `n>=4`. One can algebraically rebuild the missing multiplicity by choosing a high enough grading moment, but the required moment now depends on the same externally selected order `n` that `WP-205` and `WP-206` were trying to source-force.

There is a second obstruction. Equation (18) is a **virtual** signed combination. The top Barnes term itself has sign `(-1)^{d-1}` and the lower Barnes orders carry their own coefficients. Replacing the virtual combination by its absolute spectral mass may restore an ordinary positive carrier, but then it is no longer the same determinant-line/supertrace functional. Conversely, keeping the exact graded identity does not inherit a quadratic sign theorem from positivity of the chain Hilbert norm.

So higher polynomial grading moments can trade cancellation against roughness, but within this family they do not identify a single object whose ordinary positivity supplies both.

## 6. Aggressive falsification and exact scope

**Does determinant-line torsion really retain more than cohomology?** Yes. Cohomology in `WP-207` has one state per level, whereas (4)--(7) leave multiplicity `m+1`. The statement that every acyclic direction is spectrally forgotten would therefore be false.

**Could the double-Barnes source still satisfy the reciprocal-floor criterion despite belonging to `S^{n-1}`?** No for this source. Equation (15) is a direct multiplier estimate and gives the stronger pointwise failure `|\xi|F_{\rm dbl}(\xi)->0`.

**Could `d` itself rescue Ray–Singer torsion?** No. The factor `d-1` in (4) changes only the amplitude. It never changes the double-Barnes order or the high-frequency decay class.

**Could one call the positive Quillen/Ray–Singer norm the required positivity theorem?** No. A Hermitian metric has nonnegative squared norm by definition, while the logarithmic torsion correction is built from alternating degree-weighted determinants. Positivity of the norm does not imply nonnegativity of an arbitrary quadratic functional formed from its logarithm, curvature, or variation. A special curvature/intersection positivity theorem could be genuinely useful, but it would be an additional geometric theorem and must be checked on the assembled finite--archimedean object.

**Could a higher grading moment `F^{n-2}` solve the problem?** It restores enough Barnes order algebraically, not a canonical Weil geometry. The choice depends on `n`; the readout remains graded/signed; no Mangoldt or pole term appears; and the same construction works for every `a>0`.

**Does this classify higher analytic torsion?** No. It classifies only polynomial degree moments of the specific commuting Koszul oscillator source (1). Classical higher analytic torsion forms are a broader geometric theory. A global superconnection, family index, anomaly formula, or nonlocal intersection pairing can leave this category and must be tested separately.

**Is `H_{d,a}` being claimed to be the Hodge Laplacian of the Koszul differential?** No. It is the positive degree-preserving spectral source already used in `WP-207`. The Ray–Singer comparison concerns the canonical `(-1)^q q` determinant-line grading applied to this source. A future geometry whose actual Hodge Laplacians have different spectra is outside this calculation.

## 7. Prior art and novelty boundary

No novelty is claimed for analytic torsion, Quillen metrics, Koszul complexes, harmonic oscillators, Barnes zeta functions, or graded heat traces.

D. B. Ray and I. M. Singer, *R-torsion and the Laplacian on Riemannian manifolds*, Advances in Mathematics **7** (1971), 145--210, introduced analytic torsion through zeta-regularized Laplacian determinants with the degree weight underlying (3)--(6). The standard formula uses the alternating first moment in form degree.

The determinant-line metric interpretation is classical Quillen/Ray–Singer theory. J.-M. Bismut, H. Gillet, and C. Soulé, *Analytic torsion and holomorphic determinant bundles III. Quillen metrics on holomorphic determinants*, Communications in Mathematical Physics **115** (1988), 301--351, develops Quillen metrics and their curvature/variation for determinant bundles.

Most importantly for novelty control, J.-M. Bismut, *Koszul complexes, harmonic oscillators, and the Todd class*, Journal of the American Mathematical Society **3** (1990), 159--256, already combines Koszul complexes, harmonic oscillators, and generalized analytic-torsion/secondary characteristic-class machinery. The category “Koszul oscillator plus torsion” is therefore emphatically classical, not a Mathia discovery.

The line-specific contribution of this finding is the elementary exact compatibility test against the `WP-202`/`WP-206` reciprocal-floor resource: on the precise `WP-207` source, the canonical first degree moment has effective Barnes order two regardless of ambient oscillator dimension, while an `F^k` moment reaches Barnes order at most `k+1` until the full Koszul degree is reached. A targeted search found no prior statement connecting this grading-order collapse to the current Weil-cone stabilization criterion. Search absence is not a novelty claim.

## 8. Consequence for `weil_positivity`

The determinant-line escape from `WP-207` is real but narrower than hoped. Acyclic Koszul directions can survive in a metric/torsion invariant after cohomology has reduced to one mode. Standard analytic torsion, however, remembers them through only a double-Barnes virtual spectrum, which is too smooth for every surviving order `n=4k`.

Accordingly the live target cannot be merely “put the Koszul cancellation on a determinant line.” A successful construction must provide a more global mechanism in which the grading or intersection pairing that creates the exact archimedean normalization also carries a source-forced sign resource of critical strength **without** selecting a high polynomial degree moment from the desired spectral-shift order.

Even that remains only the real-place side. The research mandate still requires the same global object to produce the finite Mangoldt selector and pole/global counterterms, and its sign theorem must precede the identification with Weil positivity rather than follow from RH or inserted zero data.

## Dependencies

- `research/weil_positivity/findings/WP-202-universal-centered-bath-stabilization-is-equivalent-to-a-reciprocal-fourier-floor.md`
- `research/weil_positivity/findings/WP-206-geometric-oscillator-multiplicity-supplies-reciprocal-floor-but-euler-gamma-forces-dimension-one.md`
- `research/weil_positivity/findings/WP-207-koszul-cohomology-recovers-euler-gamma-only-by-collapsing-barnes-roughness.md`
- `research/weil_positivity/SOURCES.md`
