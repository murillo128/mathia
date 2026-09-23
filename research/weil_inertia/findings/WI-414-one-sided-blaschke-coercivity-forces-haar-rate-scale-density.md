# WI-414 — One-sided Blaschke coercivity forces Haar-rate lower scale density

**Status:** `CLASSICAL-THEOREM + LITERATURE+DERIVED + EXACT-DERIVED + DECISIVE-NEGATIVE`.

**Parents:** [WI-412](./WI-412-haar-scale-blaschke-mixing-buys-a-count-quantum-only-at-infinite-budget.md), [WI-413](./WI-413-centered-blaschke-scale-convolution-is-invertible.md).

## Claim

WI-413 closed the exact-constant tempered-distribution loophole for centered Burnol--Kunik scale mixing, but explicitly left open a weaker target: perhaps a non-Haar scale mixture could keep the centered response merely bounded below by a fixed positive quantum at every depth, without paying the Haar density of scale mass.

For linear **measure** mixtures with controlled local source budget, classical Beurling-density theory closes that loophole sharply.

Keep the centered log-scale kernel from WI-412--WI-413,

\[
K(t)=\log\coth\frac{|t|}{2},
\qquad K\ge0,
\qquad \int_{\mathbb R}K(t)\,dt=\frac{\pi^2}{2}.
\tag{1}
\]

Let `nu` be a signed or complex locally finite Borel measure on logarithmic scale and assume its total-variation measure `|nu|` is translation-bounded. Define

\[
F_\nu(u)=\int_{\mathbb R}K(s-u)\,d\nu(s)
\tag{2}
\]

wherever the integral is finite; translation-boundedness and `K in L^1` make this an a.e. statement, which is all that is needed below. If for some `q>0`

\[
|F_\nu(u)|\ge q
\qquad\text{for a.e. }u\in\mathbb R,
\tag{3}
\]

then the lower Beurling density of the coefficient total variation obeys the sharp bound

\[
\boxed{
D^-(|\nu|)\ge \frac{2q}{\pi^2}.
}
\tag{4}
\]

Here

\[
D^-(\mu)
:=\liminf_{L\to\infty}\inf_{x\in\mathbb R}
\frac{\mu([x-L/2,x+L/2])}{L}.
\tag{5}
\]

Consequently, a merely one-sided/count-coercive centered response still forces asymptotically Haar-rate mass in **every sufficiently long logarithmic-scale interval**. It is not enough for the scale measure to have infinite total variation: any finite measure, or any infinite measure with `D^-=0`, is excluded. In particular, sparse infinite scale mixtures that leave arbitrarily long logarithmic-scale intervals underpopulated cannot provide an all-depth count quantum.

The constant is optimal. The Haar measure already isolated in WI-412--WI-413,

\[
d\nu(s)=\frac{2q}{\pi^2}\,ds,
\tag{6}
\]

has lower Beurling density exactly `2q/pi^2` and gives

\[
K*\nu\equiv q.
\tag{7}
\]

Thus relaxing **exact flatness** to **one-sided coercivity** does not lower the asymptotic scale-budget density within the translation-bounded measure class. What exact flatness adds, by WI-413, is uniqueness: equality in the budget statement alone is not claimed to force Haar, but exact constant response in the tempered class does.

No improved simple-critical-zero proportion and no RH conclusion are claimed.

## 1. The load-bearing theorem is classical

Jean-Pierre Gabardo's convolution/Beurling-density theorem states, in the one-measure case, that if `mu` is a positive translation-bounded Borel measure on `R`, `h>=0` lies in `L^1(R)`, and

\[
\mu*h\ge A
\qquad\text{a.e. on }\mathbb R,
\tag{8}
\]

then

\[
\boxed{
A\le D^-(\mu)\int_{\mathbb R}h(x)\,dx.
}
\tag{9}
\]

The 2013 source further identifies the lower Beurling density as the best possible constant in the corresponding normalized lower-convolution problem. Gabardo--Lai restate the result as their convolution theorem for positive Borel measures and explicitly retain translation-boundedness in the lower-bound direction.

This is not a new harmonic-analysis theorem of Mathia. The new line-specific content is recognizing that the exact centered Blaschke kernel of WI-412 lies directly in the theorem's scope and that its known `L^1` mass makes the surviving one-sided coercivity loophole quantitatively identical to the Haar budget.

## 2. Application to signed or complex scale mixtures

Because `K>=0`, total variation gives pointwise wherever (2) is defined

\[
|F_\nu(u)|
\le
\int K(s-u)\,d|\nu|(s)
=(|\nu|*K)(u).
\tag{10}
\]

Hence (3) implies

\[
|\nu|*K\ge q
\qquad\text{a.e.}
\tag{11}
\]

Apply (9) with

\[
\mu=|\nu|,
\qquad h=K,
\qquad A=q.
\]

Using (1),

\[
q
\le
D^-(|\nu|)\frac{\pi^2}{2},
\]

which is exactly (4).

The same conclusion applies if the desired detector is phrased as a real one-sided inequality such as `Re F_nu>=q`, since that implies `|F_nu|>=q`. Thus allowing signed or complex coefficients does not reduce the **total-variation** density price for a globally coercive response.

Equation (4) is stronger than the finite-total-variation obstruction of WI-412. It says that an admissible infinite measure cannot buy coercivity by placing ever larger but increasingly sparse packets of scale mass. For every `epsilon>0`, all sufficiently long intervals `I` satisfy

\[
|\nu|(I)
\ge
\left(\frac{2q}{\pi^2}-\epsilon\right)|I|.
\tag{12}
\]

So the budget must be extensive in log scale, uniformly with respect to where the interval is placed.

## 3. Sharpness and relation to WI-412--WI-413

WI-412 computed

\[
\int_{\mathbb R}K(t)\,dt=\frac{\pi^2}{2}
\]

and observed that Lebesgue/Haar scale measure `ds` produces the constant response `pi^2/2`. Rescaling by `2q/pi^2` proves sharpness of (4).

There is therefore a clean three-level closure for the centered linear Blaschke scale architecture:

1. **finite total variation:** WI-412 shows that uniform coercivity across a log-depth interval of length `L` costs at least `(2q/pi^2)L`, so a fixed finite budget cannot cover all depths;
2. **infinite but translation-bounded measure budget:** the present finding shows that all-depth one-sided coercivity forces lower Beurling density at least `2q/pi^2`, so sparse infinite scale mass does not evade the cost;
3. **tempered generalized scale distributions with exact constant response:** WI-413 shows Fourier-multiplier injectivity and forces the unique preimage `(2q/pi^2)ds`.

The second point is the durable delta here. The phrase `one-sided coercive profile` in WI-413 is not an unconstrained remaining degree of freedom inside the natural locally finite measure class: classical density theory already forces the same asymptotic local scale budget as Haar.

## 4. What remains open

This does **not** close every alternative listed in WI-413. The theorem uses a scale **measure** whose total variation is translation-bounded. It does not price a genuinely distributional, non-measure source object under only a one-sided response condition; such an object would first need a meaningful source-side budget notion. It also does not justify a non-translation-bounded or renormalized infinite source identity.

Nor does it address finite depth windows, ordinate-dependent coupling between scale and vertical center, nonlinear observables, or arithmetic/spectral information that independently prevents arbitrarily shallow off-line displacement. Most importantly, as in WI-411, a source-independent continuum coverage theorem does not by itself control an oracle-like construction singularly adapted to the discrete ordinates and depths of hypothetical exceptional zeros. Such targeting would require a non-circular zeta-side construction.

So the remaining centered-scale escape is narrower than after WI-413: replacing exact constancy by a positive lower envelope does not help for translation-bounded measure mixtures. To avoid Haar-rate local budget one must leave this measure class, restrict the depth range, couple to additional zero/source data, or introduce genuinely new arithmetic/spectral information.

## 5. Prior-art and novelty audit

The decisive external input is established harmonic-analysis prior art:

- Jean-Pierre Gabardo, **Convolution Inequalities for Positive Borel Measures on R^d and Beurling Density**, in *Excursions in Harmonic Analysis, Volume 2*, Applied and Numerical Harmonic Analysis, Birkhäuser/Springer (2013), pp. 23--47, DOI `10.1007/978-0-8176-8379-5_3`. The chapter states the lower-convolution/lower-Beurling-density implication under translation-boundedness and identifies the density constant as optimal.
- Jean-Pierre Gabardo and Chun-Kit Lai, **Frames of multi-windowed exponentials on subsets of R^d**, *Applied and Computational Harmonic Analysis* 36:3 (2014), 461--472, DOI `10.1016/j.acha.2013.08.004`. Their Theorem 2.3 restates the convolution inequalities used here, including the lower-bound direction for translation-bounded positive measures.

The Blaschke-side inputs are internal established findings: WI-412 derives the exact centered kernel `K` and its mass `pi^2/2`; WI-413 derives its nonvanishing Fourier multiplier and exact-Haar uniqueness for constant tempered response.

A targeted literature search around positive convolution inequalities, lower Beurling density, translation-bounded measures, Wiener--Tauberian convolution, and Blaschke/Mellin scale mixtures found Gabardo's theorem as direct prior art for the abstract analytic implication. Accordingly, no novelty is claimed for (9), and the present result is classified as a **literature-backed consequence** at the Mathia defect-to-zero frontier rather than a new convolution theorem.

## Consequence

The `approximate / one-sided coercive profile` escape listed after WI-413 splits cleanly. Approximation on finite windows remains open, but **global positive coercivity at every depth cannot be obtained with sub-Haar lower scale density** in any translation-bounded signed/complex measure architecture when budget is measured by total variation.

This materially narrows the Blaschke amplification program. A viable route toward zero defect can no longer hope that an irregular or sparse infinite scale measure supplies a fixed count quantum more cheaply than Haar. It must instead produce a controlled renormalized object outside this budget class, exploit finite-window information that itself shrinks the admissible defect depths, couple scale to independently available zeta data, or find a different invariant whose per-zero response does not require extensive logarithmic-scale mass.