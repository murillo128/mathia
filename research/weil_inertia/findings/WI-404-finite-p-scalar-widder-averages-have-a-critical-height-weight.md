# WI-404 — finite-p scalar Widder averages have a critical height weight

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + DECISIVE-NEGATIVE + SHARP-STRUCTURAL-BARRIER + PRIOR-ART-AUDITED`.

**Parent findings:** [WI-399](./WI-399-widder-root-growth-gives-effective-shift-bootstrap.md), [WI-401](./WI-401-widder-sampling-mesh-has-exact-horizontal-resolution.md), [WI-403](./WI-403-scalar-widder-envelope-feedback-is-a-closure-operator.md).

## Claim

Conditional on the fixed-height prime/zero root-rate interface imported and independently audited in WI-399--WI-403, replacing pointwise scalar Widder control by a finite-`p` nonnegative average does **not** restore coercivity against sparse high off-critical defects unless the averaging weight grows at a precise critical rate.

For one off-critical zero

\[
\rho=\frac12+\delta+i\gamma,
\qquad d:=|\delta|>0,
\]

write

\[
r_{\gamma,d}(T)
:=
\frac{4T^2(\gamma^2+d^2)}
{(T^2+\gamma^2-d^2)^2+4\gamma^2d^2}.
\tag{1}
\]

For fixed `p>0` and real `a`, define its weighted positive-excess moment

\[
I_{p,a}(\gamma,d)
:=
\int_0^\infty T^a\,(r_{\gamma,d}(T)-1)_+^p\,dT.
\tag{2}
\]

Then for every fixed `d>0`, as `gamma -> infinity`,

\[
\boxed{
I_{p,a}(\gamma,d)
\sim
C_p\,d^{2p+1}\gamma^{a-2p},
}
\qquad
C_p
=
\int_{-1}^{1}(1-u^2)^p\,du
=
\frac{\sqrt\pi\,\Gamma(p+1)}{\Gamma(p+3/2)}.
\tag{3}
\]

Thus `a=2p` is the exact polynomial height-weight threshold for a fixed-depth defect at this scalar interface:

- if `a<2p`, the averaged cost of a fixed off-line defect tends to zero with height;
- if `a=2p`, it tends to the finite positive value `C_p d^(2p+1)`;
- if `a>2p`, it grows polynomially with height.

In particular, for the ordinary unweighted average,

\[
\boxed{
\int_0^\infty (r_{\gamma,d}(T)-1)_+^p\,dT
\sim
C_p\frac{d^{2p+1}}{\gamma^{2p}},
}
\tag{4}
\]

and there is already the exact elementary upper bound

\[
\boxed{
\int_0^\infty (r_{\gamma,d}(T)-1)_+^p\,dT
\le
2\frac{d^{2p+1}}{\gamma^{2p}}.
}
\tag{5}
\]

For logarithmic height measure,

\[
\boxed{
\int_0^\infty (r_{\gamma,d}(T)-1)_+^p\,\frac{dT}{T}
\sim
C_p\frac{d^{2p+1}}{\gamma^{2p+1}}.
}
\tag{6}
\]

Consequently no theorem that controls only an unweighted, logarithmically weighted, or more generally `T^a`-weighted finite-`p` **nonnegative scalar excess** with `a<2p` can obtain a height-uniform positive tariff for the presence of an isolated fixed-depth off-critical block. An abstract functional-equation/conjugation-symmetric family with fixed depth `d_0>0` and exponentially sparse ordinates `gamma_n=2^n` has summable scalar excess for every fixed finite `p` in the unweighted case. This is an interface obstruction, not an assertion that such a family is the zero set of zeta.

The result closes a natural attempted escape from WI-403. Cross-height information can matter, but simply integrating a nonnegative power of the same scalar fixed-height envelope below the critical height weight does not create the missing defect-to-zero coercivity. A useful cross-height observable must retain additional structure: for example signed/phase information, coupling between heights, a genuinely stronger prime-side estimate, or a height weight at or above the critical exponent together with arithmetic control strong enough to use it.

No improved simple-critical-zero proportion and no proof of RH is claimed.

## 1. Source interface and exact one-zero geometry

The load-bearing external source is Zeraoulia Rafik, *Uniform Beta Smoothing of Widder Sums for the Riemann xi-Function and a Schur--Triple Application to Simple Critical Zeros*, Preprints.org manuscript `202609.1018`, version 2, posted 17 September 2026. It is explicitly non-peer-reviewed. Proposition A1 and Lemma A1 provide the fixed-height zero-side root radius and prime-side transport reconstructed in WI-399--WI-400.

The present argument uses only the already-audited one-zero factor (1). WI-401 proved the exact threshold-`1` visibility interval

\[
r_{\gamma,d}(T)>1
\iff
T\in
\left(
\sqrt{\gamma^2+2d^2}-d,
\sqrt{\gamma^2+2d^2}+d
\right),
\tag{7}
\]

whose width is exactly `2d`, and the exact peak

\[
\max_T r_{\gamma,d}(T)
=
1+\frac{d^2}{\gamma^2}.
\tag{8}
\]

Equations (7)--(8) immediately imply (5): the positive part is supported on a set of length `2d`, and everywhere on that set

\[
0<(r_{\gamma,d}(T)-1)^p
\le
\left(\frac{d^2}{\gamma^2}\right)^p.
\]

This already proves the decisive noncoercivity statement for every finite `p>0` in unweighted height.

## 2. Sharp asymptotic and the critical weight exponent

The exact asymptotic (3) identifies the threshold rather than merely giving an upper bound. Put

\[
\varepsilon:=\frac d\gamma,
\qquad
c_\varepsilon:=\sqrt{1+2\varepsilon^2},
\qquad
T=\gamma(c_\varepsilon+\varepsilon u).
\tag{9}
\]

By (7), the positive-excess support is now exactly `-1<u<1`, and `dT=d\,du`. Direct algebra gives the factorization

\[
\frac{r_{\gamma,d}(T)-1}{\varepsilon^2}
=
(1-u^2)
\frac{(2c_\varepsilon+\varepsilon u)^2-\varepsilon^2}
{(c_\varepsilon+\varepsilon u)^4
 +2(1-\varepsilon^2)(c_\varepsilon+\varepsilon u)^2
 +(1+\varepsilon^2)^2}.
\tag{10}
\]

The quotient after `1-u^2` converges uniformly to `1` on `[-1,1]` as `epsilon -> 0`. Its denominator stays uniformly positive there for sufficiently small `epsilon`. Hence, for fixed `p>0` and real `a`, dominated convergence in (2) yields

\[
\begin{aligned}
I_{p,a}(\gamma,d)
&=
\gamma^a d\,\varepsilon^{2p}
\int_{-1}^{1}
(c_\varepsilon+\varepsilon u)^a
\left(
\frac{r_{\gamma,d}(\gamma(c_\varepsilon+\varepsilon u))-1}
{\varepsilon^2}
\right)^p du
\\
&\sim
\gamma^a d\,\varepsilon^{2p}
\int_{-1}^{1}(1-u^2)^pdu,
\end{aligned}
\]

which is exactly (3). The beta-integral evaluation of `C_p` is standard.

Taking `a=0` gives (4). Replacing `dT` by `dT/T` inserts the factor

\[
\frac{\varepsilon\,du}{c_\varepsilon+\varepsilon u},
\]

and gives (6).

For `p=1`, the leading constants are especially simple:

\[
\int_0^\infty (r_{\gamma,d}(T)-1)_+\,dT
\sim
\frac43\frac{d^3}{\gamma^2},
\qquad
\int_0^\infty (r_{\gamma,d}(T)-1)_+\frac{dT}{T}
\sim
\frac43\frac{d^3}{\gamma^3}.
\tag{11}
\]

Thus the suppression with ordinate is not an artifact of a loose norm estimate. It is the sharp one-zero asymptotic.

## 3. Sparse-block obstruction

Fix `d_0>0` and consider an abstract sequence of off-line blocks at ordinates

\[
\gamma_n=2^n,
\qquad d_n=d_0.
\tag{12}
\]

For the scalar envelope

\[
R(T):=\sup_n r_{\gamma_n,d_0}(T),
\]

pointwise

\[
(R(T)-1)_+^p
\le
\sum_n(r_{\gamma_n,d_0}(T)-1)_+^p.
\tag{13}
\]

Tonelli and (5) therefore give

\[
\int_0^\infty(R(T)-1)_+^p\,dT
\le
2d_0^{2p+1}\sum_n2^{-2pn}
<\infty.
\tag{14}
\]

Adding the reflected/conjugate companions changes only a finite multiplicity and does not affect summability. Therefore mere finiteness, boundedness, or another global finite budget for this unweighted positive scalar excess cannot distinguish zero defect from an infinite but sufficiently sparse family of fixed-depth defects.

This stress test is deliberately geometric. It does not claim that (12) satisfies the zeta explicit formula, zero counts, or any arithmetic correlation theorem. Its role is to falsify an implication that would be asserted solely from the scalar Widder-average interface. Any theorem using additional zeta-specific information lies outside the countermodel and may evade the barrier.

## 4. What the barrier does and does not close

WI-403 proved that pointwise feedback through the sharp scalar Widder envelope is a closure operator: geometry cannot improve itself by passing through its own pointwise supremum. A natural response is to retain several heights at once by averaging the positive excess. Equations (3)--(6) show exactly when this helps at the one-zero level.

The barrier closes finite-`p` nonnegative scalar averaging with subcritical polynomial height weight `T^a`, `a<2p`, as a source of a height-uniform per-defect tariff. It includes ordinary Lebesgue height, logarithmic height, bounded weights, and polylogarithmic perturbations of such subcritical weights.

It does **not** close:

- pointwise or supremum estimates that certify every required height;
- a critical/supercritical weight of order at least `T^(2p)` if the prime side can actually control it;
- signed averages, where cancellation and phase are retained rather than discarded by the positive part;
- cross-height correlations or matrix/vector observables that do not reduce to a scalar power of the one-height maximum;
- zero-population, pair/higher-correlation, or explicit-formula information added independently;
- a prime-side theorem strictly below the geometry-implied scalar envelope.

Even at the critical weight `a=2p`, the one-zero cost is proportional to `d^(2p+1)` and therefore degenerates for arbitrarily shallow defects. The critical weight removes loss with **height** for fixed depth; it does not by itself yield a uniform positive cost over all `d>0`.

## 5. Prior art and novelty audit

The primary Rafik manuscript was checked again on 22 September 2026 and remains version 2, posted 17 September 2026 and marked as not peer-reviewed. It contains the fixed-height root-radius/prime transport and the beta-smoothed integrated Widder quantities, but the present `T`-averaged positive-excess moment is a different construction: its integration variable is the fixed-height parameter of the Appendix A root profile, not the beta smoothing variable/order used in the main theorem.

A targeted search for Widder/Riemann-xi `L^p` averaging, averaged root-growth excess, and integrated scalar root-profile coercivity found the Rafik preprint and neighboring Widder-transform `L^p` inversion literature, but no theorem matching (3) or the critical exponent `a=2p`. The classical beta-integral evaluation of `C_p` is not novel. This audit is recorded only to delimit provenance; no priority claim is made.

## 6. Consequences for the research line

The scalar Widder route is now constrained in two complementary ways. WI-403 rules out self-improvement by pointwise envelope feedback, while the present finding rules out recovering a height-uniform defect charge merely by taking finite-`p` nonnegative cross-height averages with subcritical weights.

Accordingly, the live Widder target should not be another scalar norm of the same root profile. A materially different route must expose information discarded by the positive scalar envelope: signed prime/root data, phase, a coupled statistic at several heights, or an arithmetic estimate whose strength scales at least at the critical `gamma^(2p)` level for the chosen moment. The exact law (3) supplies a falsification test for future proposals: if their effective one-defect weight is `o(gamma^(2p))`, they cannot have height-uniform scalar coercivity at this interface.
