# WI-412 — Haar-scale Blaschke mixing buys a count quantum only at infinite budget

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE`.

**Parents:** [WI-410](./WI-410-carleman-summation-removes-bsy-height-decay-only-by-giving-up-finite-source-budget.md), [WI-411](./WI-411-vertical-translations-obey-height-area-budget.md).

## Claim

WI-411 left open a measure-zero targeting loophole: its exact height-area law rules out a cheap response that is uniformly spread across a long ordinate interval, but does not prevent a vertically centered probe from becoming very large exactly at a hypothetical off-line zero. The remaining horizontal-scale question can also be priced exactly.

For the Burnol--Kunik half-plane Blaschke charge of one right-half zero

\[
\rho=\frac12+d+i\gamma,\qquad d>0,
\]

at the translated probe `1/2+a+ib`, write

\[
q_{a,b}(\gamma,d)
=\frac12\log
\frac{(\gamma-b)^2+(a+d)^2}
     {(\gamma-b)^2+(a-d)^2},
\qquad a>0.
\tag{1}
\]

The scale-invariant positive mixture with Haar measure `da/a` has the exact zero-side kernel

\[
\boxed{
\mathcal H_b(\gamma,d)
:=\int_0^\infty q_{a,b}(\gamma,d)\,\frac{da}{a}
=\pi\arctan\frac d{|\gamma-b|}
}
\tag{2}
\]

when `b != gamma`, with the continuous-in-height value

\[
\boxed{
\mathcal H_\gamma(\gamma,d)=\frac{\pi^2}{2}
\qquad(d>0).
}
\tag{3}
\]

Thus the canonical infinite-scale mixture really does turn an arbitrarily shallow off-line displacement into a **fixed count-like quantum** at its exact ordinate. But it does so only by leaving the finite-source-budget regime in two sharp ways.

First, in logarithmic scale `s=log a`, `u=log d`, the centered kernel is

\[
K(s-u)
=\log\frac{e^{s-u}+1}{|e^{s-u}-1|}
=\log\coth\frac{|s-u|}{2},
\tag{4}
\]

and

\[
\boxed{\|K\|_{L^1(\mathbb R)}=\frac{\pi^2}{2}.}
\tag{5}
\]

Therefore every finite signed or complex scale measure `mu` of total variation `M`, pushed to logarithmic scale, satisfies for every log-depth interval `I`

\[
\int_I
\left|\int K(s-u)\,d\mu(s)\right|du
\le \frac{\pi^2}{2}M.
\tag{6}
\]

If a source-independent scale mixture has centered response at least `c>0` for almost every depth in
`d_min <= d <= d_max`, then necessarily

\[
\boxed{
M\ge
\frac{2c}{\pi^2}
\log\frac{d_{\max}}{d_{\min}}.
}
\tag{7}
\]

So no fixed finite-total-variation scale combination can supply a positive count quantum uniformly down to arbitrarily shallow defects. The budget must diverge at least linearly in the number of logarithmic depth decades. Haar measure `da/a` is the order-sharp limiting escape: it has infinite total variation and produces the exact constant `pi^2/2` in (3).

Second, the same mixed kernel has the nonintegrable height tail

\[
\mathcal H_b(\gamma,d)
\sim \frac{\pi d}{|\gamma-b|}
\qquad(|\gamma-b|\to\infty),
\tag{8}
\]

and in fact

\[
\boxed{
\int_{\gamma-L}^{\gamma+L}\mathcal H_b(\gamma,d)\,db
=2\pi L\arctan\frac dL
+\pi d\log\left(1+\frac{L^2}{d^2}\right).
}
\tag{9}
\]

The right side is

\[
2\pi d\left(1+\log\frac Ld\right)+o(d)
\qquad(L/d\to\infty),
\tag{10}
\]

so the height mass diverges logarithmically. The scale-invariant escape from the finite-TV obstruction therefore trades depth attenuation for both infinite logarithmic-scale budget and a `1/|gamma-b|` height tail.

This closes the most canonical version of WI-411's `infinite-TV / sparse targeting` escape. It does **not** prove that every possible infinite-TV or renormalized Blaschke combination is useless, and it does not justify exchanging the Haar-scale integral with the full zeta source factorization. It shows exactly what the natural multiplicatively invariant choice buys and what source-budget property it necessarily loses.

## 1. Exact Haar-scale integral

Put

\[
x:=|\gamma-b|.
\]

For `x>0` define

\[
R_x(d):=\int_0^\infty
\frac12\log
\frac{x^2+(a+d)^2}{x^2+(a-d)^2}\,\frac{da}{a}.
\tag{11}
\]

The integral converges absolutely as an improper positive integral: near `a=0`, the logarithm is `O(a)`, while as `a -> infinity` it is `O(1/a)`; the extra factor `1/a` therefore gives integrable endpoints.

Differentiate in `d`. After cancellation of the apparent `1/a` terms,

\[
\frac{\partial}{\partial d}
\left(\frac{q_a(x,d)}a\right)
=\frac1{d^2+x^2}
\left[
\frac{-d(a+d)+x^2}{(a+d)^2+x^2}
+
\frac{d(a-d)+x^2}{(a-d)^2+x^2}
\right].
\tag{12}
\]

Integrating the two rational terms over `a in (0,infinity)`, the logarithmic endpoint contributions cancel and the two arctangent contributions sum to

\[
R_x'(d)=\frac{\pi x}{x^2+d^2}.
\tag{13}
\]

Since `R_x(0)=0`, integration in `d` yields

\[
R_x(d)=\pi\arctan\frac d x,
\]

which proves (2) away from the center.

At `x=0`, scale `a=du` gives directly

\[
R_0(d)
=\int_0^\infty
\log\frac{1+u}{|1-u|}\,\frac{du}{u}.
\tag{14}
\]

The logarithmic singularity at `u=1` is integrable. Splitting at `1` and sending `u -> 1/u` in the upper half gives twice the integral over `(0,1)`. There

\[
\log\frac{1+u}{1-u}
=2\sum_{n\ge0}\frac{u^{2n+1}}{2n+1},
\]

so

\[
R_0(d)
=4\sum_{n\ge0}\frac1{(2n+1)^2}
=\frac{\pi^2}{2}.
\tag{15}
\]

The striking feature is the discontinuity in the defect variable at the centered point: `R_0(0)=0` before mixing, but `R_0(d)=pi^2/2` for every `d>0` after the infinite Haar mixture. This non-uniform limit is exactly what finite source budget cannot reproduce uniformly over arbitrarily many depth scales.

## 2. Log-depth budget theorem

At exact vertical centering `b=gamma`, set

\[
a=e^s,\qquad d=e^u.
\]

Then (1) becomes the translation kernel (4). It is positive, even, locally integrable, and for `t>0`

\[
K(t)
=\log\frac{1+e^{-t}}{1-e^{-t}}
=2\sum_{n\ge0}\frac{e^{-(2n+1)t}}{2n+1}.
\tag{16}
\]

Hence

\[
\int_0^\infty K(t)\,dt
=2\sum_{n\ge0}\frac1{(2n+1)^2}
=\frac{\pi^2}{4},
\]

and evenness proves (5).

Let `mu` be any finite signed or complex Borel measure on logarithmic scale, with `||mu||_TV=M`, and let

\[
F_\mu(u):=\int_\mathbb R K(s-u)\,d\mu(s).
\tag{17}
\]

Atoms can make `F_mu` singular at isolated matching depths, but Tonelli applied to `|mu|` and `K` gives the integrated statement without any pointwise regularity assumption:

\[
\begin{aligned}
\int_I |F_\mu(u)|\,du
&\le
\int_\mathbb R
\int_I K(s-u)\,du\,d|\mu|(s)\\
&\le \|K\|_1\,\|\mu\|_{TV}
=\frac{\pi^2}{2}M.
\end{aligned}
\tag{18}
\]

If `|F_mu(u)| >= c` almost everywhere on an interval of length

\[
|I|=\log(d_{\max}/d_{\min}),
\]

then (7) follows. In particular, a fixed finite budget cannot be uniformly count-coercive as `d_min -> 0`.

Conversely, Haar measure `dmu(s)=ds`, equivalently `da/a`, has infinite total variation and translation invariance gives

\[
F_\mu(u)=\int_\mathbb R K(t)\,dt=\frac{\pi^2}{2}
\]

for every `u`. The lower bound (7) therefore has the correct logarithmic order: constant centered sensitivity over `L` logarithmic depth units costs at least order `L` scale mass, and the scale-invariant construction uses exactly that order locally while becoming infinite over all depth scales.

## 3. The price reappears in height

Equation (2) immediately gives

\[
\mathcal H_b(\gamma,d)
=\pi\arctan\frac d{|\gamma-b|}
=\frac{\pi d}{|\gamma-b|}
+O\left(\frac{d^3}{|\gamma-b|^3}\right),
\]

which is (8). Integrating the even profile in `x=gamma-b` and using

\[
\int \arctan\frac d x\,dx
=x\arctan\frac d x
+\frac d2\log(x^2+d^2)
\]

gives (9) exactly.

This is the complementary obstruction to WI-411. WI-411 showed that finite-TV translated probes have only finite height area proportional to the horizontal depth. The Haar-scale mixture evades the scale-side attenuation at one exact center, but its height profile ceases to be integrable. Thus the apparent fixed quantum is not a free defect counter: it is a narrowing spike with long logarithmic tails, produced by an infinite source coefficient budget.

## 4. What this does and does not close

The result is deliberately narrower than a universal no-go theorem.

It **does** close the following route: choose a source-independent finite signed/complex mixture of the Burnol--Kunik horizontal scales, vertically center it at a candidate ordinate, and hope for a fixed positive response to every off-line zero regardless of how close it lies to the critical line. Even granting oracle knowledge of the ordinate, the scale budget must grow at least like the logarithmic depth range. Since no unconditional lower bound on off-line displacement is known, a fixed finite budget cannot supply such a quantum.

The full Haar mixture demonstrates the only obvious scale-invariant escape and simultaneously exposes why it is outside the finite-budget regime. It also explains why the centered fixed quantum does not contradict WI-410: WI-410 assumes finite total variation in scale, whereas `da/a` has infinite total variation.

The result **does not** exclude a renormalized infinite-TV construction with source-side cancellations, a distributional scale combination, a nonlinear observable, or arithmetic/spectral information that independently quantizes horizontal displacement. It also does not establish that the infinite Haar zero-side integral may be interchanged with Kunik's full outer/Blaschke factorization; such a source-side renormalization would be a new theorem and is not assumed here.

## 5. Prior-art and novelty audit

The load-bearing analytic input is the classical half-plane Blaschke geometry already anchored in WI-410--WI-411:

- M. Kunik, *Logarithmic Fourier integrals for the Riemann Zeta Function*, arXiv:`0804.4829v2` (2009), for the half-plane Poisson--Schwarz/Blaschke factorization;
- J.-F. Burnol, *A note on Nyman's equivalent formulation of the Riemann hypothesis*, Contemp. Math. **287** (2001), 23--26; arXiv:`math/9910055`, for the quantitative half-plane Blaschke/Nyman connection.

Neighboring literature includes Mikayelyan--Hayrapetyan on integral logarithmic means of half-plane Blaschke products and Bruna--Melnikov on translates of the Poisson kernel. A targeted search also found general Mellin-transform literature for logarithms of rational/quadratic quotients. These sources establish that the analytic ingredients and scale/Mellin viewpoint are classical territory. No inspected source was used for the specific Mathia conclusion (7), and no priority claim is made for the elementary integral identity (2), the `log coth` kernel, or its `pi^2/2` norm.

The durable delta is the exact **budget statement at the current defect-to-zero frontier**: the multiplicatively invariant scale mixture is count-coercive at an exactly centered off-line zero, but finite-TV mixtures pay at least linearly in logarithmic depth range, while the Haar limit that attains depth-independent charge has infinite coefficient mass and a nonintegrable `1/height` tail.

## Consequence

The WI-410--WI-411 frontier can now be sharpened. There are two distinct ways to try to amplify a shallow off-line zero with the classical Blaschke family:

- spread sensitivity over height, which WI-411 prices by a height-area budget;
- concentrate at the exact ordinate and spread over horizontal scales, which the present finding prices by a logarithmic-depth budget.

The canonical Haar-scale escape reaches a genuine fixed zero-side quantum, but only by abandoning finite source budget and producing logarithmically divergent height mass. Therefore further work should not treat `infinite scale mixing` by itself as a defect-to-zero mechanism. A viable continuation must supply an independently controlled renormalized source identity, a non-circular way to target the unknown ordinates with acceptable budget, or genuinely new arithmetic/spectral information that prevents arbitrarily shallow defects.