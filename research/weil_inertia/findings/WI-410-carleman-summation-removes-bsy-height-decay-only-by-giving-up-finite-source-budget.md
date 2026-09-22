# WI-410 — Carleman summation removes BSY height decay only by giving up a finite source budget

**Status:** `CLASSICAL-IDENTITY + LITERATURE+DERIVED + EXACT-DERIVED + PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE`.

**Parent:** WI-409.

## Claim

The positive horizontal-defect functional isolated in WI-409 is not the strongest classical zero-side sensitivity available. Kondratyuk's Carleman--Nevanlinna summation formula gives a height-unweighted positive defect,

\[
\frac{\pi}{2}\sum_j\left|\Re\rho_j-\frac12\right|
= I(+0)+\frac{\pi}{2},
\qquad
I(\varepsilon)=\int_0^\infty e^{-\varepsilon t}
\log\left|\zeta\left(\frac12+it\right)\right|\,dt,
\]

with \(I(+0)=\lim_{\varepsilon\downarrow0}I(\varepsilon)\) in the sense of the cited theorem. Thus the lack of a positive charge without the BSY \(\gamma^{-2}\) decay is not itself the missing ingredient.

What is missing is the conjunction of **height sensitivity and a controlled finite source budget**. This tradeoff can be made exact inside the classical Burnol--Kunik half-plane factorization: for a zero

\[
\rho=\frac12+d+i\gamma,\qquad d>0,
\]

a real Poisson-scale probe at \(s=\frac12+a\), \(a>0\), assigns the Blaschke charge

\[
q_a(\gamma,d)
=\frac12\log\frac{\gamma^2+(a+d)^2}{\gamma^2+(a-d)^2}
=\operatorname{artanh}\!\left(
\frac{2ad}{\gamma^2+a^2+d^2}
\right).
\]

Optimizing over all real scales gives exactly

\[
\sup_{a>0}q_a(\gamma,d)
=\operatorname{arsinh}\frac d\gamma
\le \frac d\gamma.
\]

Consequently every finite signed mixture \(\nu\) of these scales, with total variation \(M=\|\nu\|_{\mathrm{TV}}<\infty\), obeys

\[
\left|\int q_a(\gamma,d)\,d\nu(a)\right|
\le M\operatorname{arsinh}\frac d\gamma
\le M\frac d\gamma.
\]

So finite-total-variation mixtures of the real-axis Poisson-scale family cannot produce a height-uniform \(O(d)\) defect response. To retain such a response at height \(\gamma\), the scale weight must have total variation growing at least on the order of \(\gamma\), or one must leave this probe family. Kondratyuk's Carleman endpoint does leave the finite-budget regime: its zero-side tariff is proportional to \(d\), but the identity itself does not give an unconditional finite upper bound for \(I(+0)\) or for the positive defect sum off RH.

## 1. Classical Carleman endpoint

Kondratyuk proves a Carleman--Nevanlinna theorem for a rectangle and applies it to the zeta function. The published abstract states that for the nontrivial zeros \(\rho_j\), counted with multiplicity,

\[
\frac{\pi}{2}\sum_j\left|\Re\rho_j-\frac12\right|
=I(+0)+\frac\pi2,
\]

where

\[
I(\varepsilon)=\int_0^\infty e^{-\varepsilon t}
\log\left|\zeta\left(\frac12+it\right)\right|dt,
\qquad \varepsilon>0.
\]

It follows immediately that RH is equivalent to \(I(+0)=-\pi/2\). More importantly for this research line, each off-line zero is charged by horizontal displacement alone; there is no \(\gamma^{-1}\) or \(\gamma^{-2}\) attenuation in the zero-side summand.

This is **not** an unconditional finite defect budget. If the displacement sum diverges, the formula does not turn it into a finite quantity merely by writing the source side as an Abel limit. The useful distinction is therefore not "summable positive charge versus non-summable positive charge" in isolation, but whether the source representation comes with an independently bounded budget strong enough to force the charge to vanish.

Primary source:

- A. A. Kondratyuk, *A Carleman-Nevanlinna Theorem and Summation of the Riemann Zeta-Function Logarithm*, Computational Methods and Function Theory **4**(2), 391--403, DOI: `10.1007/BF03321076`. The theorem and displayed zeta identity are stated in the published abstract.

## 2. The Burnol--Kunik real Poisson-scale family

Kunik's half-plane factorization writes the normalized zeta function in \(\Re s>1/2\) as an outer/Poisson--Schwarz factor times a Blaschke product over zeros with \(\Re\rho>1/2\). This factorization is explicitly presented as a variant of the Balazard--Saias--Yor theorem and traces the underlying Blaschke/Nyman product to Burnol.

For one right-half zero \(\rho=1/2+d+i\gamma\), its reflected point across the boundary is \(1-\bar\rho=1/2-d+i\gamma\). At a positive real half-plane displacement \(s=1/2+a\), normalization factors in the Blaschke factor have modulus one, so

\[
|b_\rho(1/2+a)|^2
=\frac{\gamma^2+(a-d)^2}{\gamma^2+(a+d)^2}.
\]

Therefore

\[
-\log|b_\rho(1/2+a)|
=\frac12\log\frac{\gamma^2+(a+d)^2}{\gamma^2+(a-d)^2}
=q_a(\gamma,d).
\]

At \(a=1/2\), this is precisely the BSY charge used in WI-409:

\[
q_{1/2}(\gamma,d)
=\operatorname{artanh}\!\left(
\frac{d}{\gamma^2+1/4+d^2}
\right),
\]

which is asymptotic to \(d/\gamma^2\) at large height.

Primary sources:

- M. Kunik, *Logarithmic Fourier integrals for the Riemann Zeta Function*, arXiv:`0804.4829v2` (2009). The paper derives half-plane Poisson--Schwarz factorizations of zeta and a BSY variant using Blaschke zeros.
- J.-F. Burnol, *A note on Nyman's equivalent formulation of the Riemann hypothesis*, Contemp. Math. **287** (2001), 23--26; arXiv:`math/9910055`. Burnol identifies the product over zeros with \(\Re\rho>1/2\) with a Nyman-space projection norm, giving a quantitative RH equivalence.

## 3. Sharp scale optimization

Because \(\operatorname{artanh}\) is strictly increasing on \((0,1)\), it is enough to maximize

\[
z(a)=\frac{2ad}{\gamma^2+a^2+d^2}.
\]

Differentiation gives

\[
z'(a)=
\frac{2d(\gamma^2+d^2-a^2)}
{(\gamma^2+a^2+d^2)^2}.
\]

Hence the unique maximizer is

\[
a_*=\sqrt{\gamma^2+d^2}.
\]

At that scale,

\[
z(a_*)=\frac d{\sqrt{\gamma^2+d^2}},
\]

and the elementary identity

\[
\operatorname{artanh}\frac{x}{\sqrt{1+x^2}}
=\operatorname{arsinh}x
\]

yields

\[
\boxed{
\sup_{a>0}q_a(\gamma,d)
=\operatorname{arsinh}\frac d\gamma
\le\frac d\gamma.}
\]

Thus even an oracle choosing the best real Poisson scale separately for each defect cannot remove all height decay from this family. It improves the fixed BSY scale from \(d/\gamma^2\) to at best \(d/\gamma\).

The same point survives arbitrary finite signed combinations. If \(\nu\) has finite total variation \(M\), then

\[
\left|\int q_a\,d\nu(a)\right|
\le \int q_a\,d|\nu|(a)
\le M\sup_a q_a
\le M\frac d\gamma.
\]

This is an exact no-go for a natural attempted repair of WI-409: taking finitely many or finite-total-variation many Burnol--Kunik real scales cannot turn the summable BSY-type charge into a height-uniform displacement charge while retaining a fixed source budget.

## 4. What the barrier does and does not close

The result closes only the **real-axis Poisson-scale / finite-total-variation mixture** route. It does not cover probes translated vertically to \(1/2+a+it_0\), especially a family whose center tracks an unknown zero height. It also does not cover infinite-total-variation or distributional scale combinations, Abel/Carleman limiting kernels, or a genuinely different explicit-formula observable.

Kondratyuk shows that a Carleman limit can reach an \(O(d)\) zero-side tariff. The price visible from the present comparison is precisely that this endpoint is no longer accompanied by the finite source budget that makes BSY useful as an absolutely summable defect identity. This does not prove that every conceivable route to a nondecaying finite-budget functional is impossible; it sharply identifies where the classical interpolation from BSY to Carleman loses the property needed for defect elimination.

There is a second independent limitation: even Kondratyuk's charge is proportional to \(d\). A sequence of off-line zeros could in principle have horizontal displacements tending rapidly to zero. Therefore a height-independent \(O(d)\) tariff would still not supply a fixed positive quantum per off-line zero unless one also proves a displacement lower bound/quantization law or obtains a stronger nonlinear coercivity mechanism.

## 5. Prior-art and novelty audit

The constituent analytic identities are classical. Kondratyuk already supplies the height-unweighted Carleman defect formula; Kunik supplies the symmetric Poisson--Schwarz/Blaschke factorization; Burnol supplies the earlier quantitative Blaschke/Nyman product. No priority claim is made for any of those ingredients.

The contribution recorded here is the **comparison and exact optimization relevant to the current Mathia frontier**: the same Blaschke geometry that gives WI-409 has a one-parameter real-scale family whose sharp single-zero sensitivity is \(\operatorname{arsinh}(d/\gamma)\), and finite-total-variation mixing cannot beat that height order. This turns "find a stronger positive defect functional" into a materially narrower target.

The prior-art audit also found neighboring Carleman/log-zeta integral criteria (including later variants by Yatsulka and by Brydun--Yatsulka). They reinforce that unweighted or differently weighted zero-side sums are not new. None of the material inspected supplies the missing conjunction of an independently finite source budget with a height-uniform defect tariff.

## Consequences for `weil_inertia`

WI-409 should no longer be read as saying that the main missing object is merely a positive horizontal-defect functional stronger than BSY. Such a functional already exists at the Carleman endpoint. The viable target is stricter:

1. a source-side identity or inequality with a **controlled finite budget or an exact annihilation mechanism**;
2. zero-side sensitivity that does not decay too rapidly with height, or an amplification/aggregation argument that compensates for that decay; and
3. enough coercivity in the displacement variable to exclude defects that approach the critical line arbitrarily fast, unless an independent displacement-quantization theorem is available.

Within the classical Burnol--Kunik real-scale family, condition 2 cannot be achieved uniformly from any fixed finite-total-variation combination: its sharp per-zero response is at most \(M d/\gamma\). Therefore further work should not spend effort optimizing finite mixtures of those scales unless an additional arithmetic/spectral constraint couples the available source budget to zero height.