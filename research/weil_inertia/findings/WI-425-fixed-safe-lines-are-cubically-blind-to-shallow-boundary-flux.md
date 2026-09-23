# WI-425 — Fixed safe lines are cubically blind to shallow Kunik boundary flux

**Status:** `CLASSICAL-IDENTITY + EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`.

**Parents:** [WI-410](./WI-410-carleman-summation-removes-bsy-height-decay-only-by-giving-up-finite-source-budget.md), [WI-422](./WI-422-translated-blaschke-source-regularity-has-sharp-lp-threshold.md), [WI-424](./WI-424-kunik-boundary-flux-is-a-poisson-defect-counter.md).

## Claim

WI-424 isolates the canonical Kunik boundary flux

\[
h_B(t)=-\frac{B'}{B}\!\left(\frac12+it\right),
\]

whose finite-subproduct contribution from an off-critical zero

\[
\rho=\frac12+d+i\gamma,
\qquad 0<d<\frac12,
\]

is the positive Poisson profile

\[
h_{d,\gamma}(t)=\frac{2d}{(t-\gamma)^2+d^2},
\qquad
\|h_{d,\gamma}\|_2^2=\frac{2\pi}{d}.
\tag{1}
\]

A natural attempt is to estimate the Blaschke logarithmic derivative where the Euler product is directly available, for example on a fixed line `Re(s)=1/2+a>1`, and then transfer that control to the boundary. There is an exact obstruction: for every fixed `a>d`, the same single Blaschke zero contributes on that interior line

\[
g_{a;d,\gamma}(t)
:=\frac{B_\rho'}{B_\rho}\!\left(\frac12+a+it\right)
=
\frac{1}{a-d+i(t-\gamma)}
-
\frac{1}{a+d+i(t-\gamma)}
=
\frac{2d}{(a+i(t-\gamma))^2-d^2},
\tag{2}
\]

and exactly

\[
\boxed{
\|g_{a;d,\gamma}\|_2^2
=
\frac{2\pi d^2}{a(a^2-d^2)}.
}
\tag{3}
\]

Consequently

\[
\boxed{
\frac{\|h_{d,\gamma}\|_2^2}
     {\|g_{a;d,\gamma}\|_2^2}
=
\frac{a(a^2-d^2)}{d^3}.
}
\tag{4}
\]

For every fixed `a>0`, this ratio is asymptotic to `a^3/d^3` as `d -> 0`; in norm rather than squared norm, the condition number diverges like `(a/d)^(3/2)`. Hence there is no constant `C_a` such that

\[
\|h_B\|_2\le C_a
\left\|\frac{B'}B\left(\frac12+a+i\cdot\right)\right\|_2
\tag{5}
\]

holds uniformly even for one-zero finite half-plane Blaschke products. The same conclusion holds for every finite collection of fixed interior lines: each interior `L^2` energy is `O(d^2)` while the boundary tariff is `2\pi/d`.

This is a **stability/coercivity barrier, not an information-theoretic nonuniqueness statement**. Exact noiseless values of an analytic function on an interior line determine its continuation. What fails is any depth-uniform bounded `L^2` transfer from a fixed line to the Kunik boundary flux. The obstruction disappears only if the interior displacement is itself on the defect scale: putting `a=c d`, `c>1`, makes the squared ratio in (4) equal to the finite constant `c(c^2-1)`.

There is a second, classical blindness at the other term in Kunik's factorization. On the critical boundary a Blaschke inner factor has modulus one,

\[
|B_\rho(1/2+it)|=1.
\tag{6}
\]

Thus multiplying an outer factor by `B_\rho` changes the boundary flux by (1) while leaving the boundary modulus, and hence `log|f|`, unchanged. Therefore the critical-line modulus data in the Poisson--Schwarz outer factor cannot by itself upper-bound the canonical defect flux in the ambient Hardy/Blaschke class.

Taken together, (4) and (6) close the naive black-box route

\[
\text{critical-line modulus}
+\text{fixed safe-line log-derivative norm}
\Longrightarrow
\text{reciprocal-depth boundary-flux control}.
\]

Any successful Kunik-based defect-to-zero mechanism must use genuinely stronger information: boundary-approaching control on scales comparable with the unknown depth, a continuum/multiscale norm that survives this conditioning, or a zeta-specific arithmetic coupling that is not present in generic inner--outer factorization.

## 1. Exact one-zero calculation

Center the half-plane at the critical line by writing `z=s-1/2` and `u=t-\gamma`. Up to an irrelevant unimodular normalization, the Blaschke factor attached to the right-half zero `d+i\gamma` is

\[
b_{d,\gamma}(z)
=
\frac{z-d-i\gamma}{z+d-i\gamma}.
\tag{7}
\]

On the boundary `z=it`, numerator and denominator have equal modulus, proving (6). Its logarithmic derivative is

\[
\frac{b_{d,\gamma}'}{b_{d,\gamma}}(z)
=
\frac1{z-d-i\gamma}-\frac1{z+d-i\gamma}.
\tag{8}
\]

At `z=it`, (8) equals `-2d/(u^2+d^2)`, giving (1). At `z=a+it`, it gives (2).

For `a>d`, set `A=a-d` and `C=a+d`. Then

\[
|g_{a;d,\gamma}(t)|^2
=
\frac{4d^2}
{(u^2+A^2)(u^2+C^2)}.
\tag{9}
\]

The elementary partial-fraction integral

\[
\int_{-\infty}^{\infty}
\frac{du}{(u^2+A^2)(u^2+C^2)}
=
\frac{\pi}{AC(A+C)}
\tag{10}
\]

gives

\[
\int_{\mathbb R}|g_{a;d,\gamma}(t)|^2dt
=
4d^2\frac{\pi}{(a-d)(a+d)(2a)}
=
\frac{2\pi d^2}{a(a^2-d^2)},
\]

which proves (3). The standard integral

\[
\int_{\mathbb R}\frac{du}{(u^2+d^2)^2}
=\frac{\pi}{2d^3}
\]

gives (1), and division yields (4).

For fixed lines `a_1,...,a_J>0`, choose `d<\frac12\min_j a_j`. Then for each `j`

\[
\|g_{a_j;d,\gamma}\|_2^2
=\frac{2\pi}{a_j^3}d^2(1+O(d^2)),
\tag{11}
\]

whereas `\|h_{d,\gamma}\|_2^2=2\pi/d`. Therefore no finite weighted sum of these fixed-line energies, with weights independent of `d`, can dominate the boundary energy uniformly as `d\downarrow0`.

Multiplicity does not change the obstruction: both `h` and `g` scale linearly with multiplicity, so their squared-norm ratio is unchanged.

## 2. Relation to Kunik's zeta factorization

Kunik's half-plane factorization writes, for `Re(s)>1/2`,

\[
\frac{s-1}{s}\zeta(s)=\zeta_B(s)B(s),
\tag{12}
\]

where `\zeta_B` is the Poisson--Schwarz outer factor determined by `log|\zeta(1/2+it)|` and `B` is the Blaschke product over zeta zeros with `Re(\rho)>1/2`. This is the primary-source analytic setting used in WI-409--WI-424. Kunik explicitly records the factorization and the boundary-logarithm representation; the generic inner-factor modulus identity (6) is the standard Hardy-space mechanism behind the separation.

Differentiating the factorization in the open half-plane expresses `B'/B` through `\zeta'/\zeta` and the derivative of the Poisson--Schwarz outer factor. On a safe Euler-product line `\sigma>1`, both zeta-side terms invite direct arithmetic estimates. Equations (3)--(4) show, however, that **a fixed-line norm bound on the resulting `B'/B` cannot be transferred with a depth-independent constant to the boundary `L^2` flux**. For a zero at depth `d`, the interior signal loses three powers of `d` relative to the boundary energy.

This does not rule out a zeta-specific theorem coupling the safe-line data to additional information, nor does it rule out exact analytic continuation using the complete function rather than norm budgets. It rules out the particular coercive interface in which a fixed safe-line `L^2` estimate is treated as a uniform budget for WI-424's reciprocal-depth boundary charge.

## 3. Prior-art and novelty audit

The analytic ingredients are classical. Kunik, *Logarithmic Fourier integrals for the Riemann Zeta Function*, arXiv:0804.4829, gives the zeta half-plane Poisson--Schwarz/Blaschke factorization; equations (1.2)--(1.6) of the paper explicitly separate the outer critical-line-modulus factor from the Blaschke product over right-half zeros. The paper points to the standard Hardy-space literature for that factorization.

The neighboring classical theory of inner-function derivatives is extensive; in particular P. R. Ahern and D. N. Clark, *On inner functions with H^p derivative*, Michigan Math. J. 21 (1974), 115--127, DOI `10.1307/mmj/1029001255`, and P. R. Ahern, *The mean modulus and the derivative of an inner function*, Indiana Univ. Math. J. 28 (1979), 311--347, DOI `10.1512/iumj.1979.28.28022`, study Hardy-norm regularity of derivatives of inner functions. These sources are prior art for treating derivative norms of Blaschke products, not a novelty claim for the elementary one-zero integral above.

Repository-local comparison was made against WI-408, WI-410, WI-422 and WI-424. WI-410 proves a different height-loss statement for finite-TV mixtures of **real Poisson scales**; WI-422 classifies source-plane `L^p` regularity of translated Blaschke probes; WI-424 identifies the canonical boundary flux and its reciprocal-depth `L^p` tariff. None of those stored results gives the exact fixed-interior-line versus boundary norm ratio (4), nor the consequent no-go for a fixed safe-line Euler-product budget. The mathematical delta here is precisely that conditioning barrier. No priority claim is made for the elementary complex-analysis identity itself.

## 4. Stress tests and boundaries

1. **Depth-scale approach is not excluded.** If `a=c d`, equation (4) has bounded ratio `c(c^2-1)`. The obstruction concerns a line whose displacement from the critical line stays fixed while `d->0`, including every fixed Euler-product-safe line `sigma>1`.

2. **Exact continuation is not excluded.** A complete analytic function on one interior vertical line has uniqueness information far beyond its `L^2` norm. The finding is about bounded coercive transfer, not uniqueness.

3. **Zeta-specific coupling is not excluded.** A generic Blaschke factor may be inserted without changing boundary modulus. Zeta zeros are not arbitrary inner factors: the Euler product, functional equation and zero symmetries may impose additional relations. Any successful use of such relations is genuinely new arithmetic input relative to this no-go.

4. **The one-zero test is sufficient for the universal inequality.** Any proposed norm inequality intended to hold for all admissible finite Blaschke subproducts must hold for a one-zero factor. Positive superposition on the boundary cannot repair failure already present in that subfamily.

5. **No claim about the number of off-line zeta zeros follows.** This is an obstruction to a proof interface. It neither constructs a zeta zero nor weakens WI-424's positive boundary defect counter.

## Consequence for the research line

WI-424 leaves open whether arithmetic data can control the canonical boundary flux strongly enough to force it to vanish. This finding removes the most direct version of that bridge: estimating `B'/B` by Euler-product methods on one or finitely many fixed safe vertical lines and transferring an `L^2` budget to the critical boundary cannot control shallow defects uniformly.

The next viable Kunik route must therefore preserve **scale information**. A useful target would be an arithmetic estimate integrated over `a` down toward zero with a weight strong enough to dominate the reciprocal-depth boundary tariff, or a zeta-specific identity that couples the outer factor and inner zeros in a way generic Hardy factorization does not. Any such proposal should be tested against the exact one-zero conditioning law (4) before further development.
