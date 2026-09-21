---
id: WP-397
title: Multi-frequency positivity is support-dominated by the critical centralizer shadow
branch: weil_positivity
status: supported
kind: bost-connes-critical-kms-positive-fourier-coefficient-centralizer-support-domination
claim_strength: exact RH-independent obstruction showing that every bounded positive element of the critical Bost--Connes factor has a faithful nonzero centralizer average and that every modular/gauge Fourier coefficient is two-sided support-dominated by that average; consequently cross-frequency interference cannot cancel the centralizer floor or produce a nonzero positive element whose canonical diagonal support is confined to the Haar-null prime-power orbit
created: 2026-09-21
related: [WP-226, WP-331, WP-395, WP-396]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - J.-B. Bost and A. Connes, Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory, Selecta Math. (N.S.) 1 (1995), 411--457, DOI 10.1007/BF01589495
  - M. Takesaki, Conditional expectations in von Neumann algebras, Journal of Functional Analysis 9 (1972), 306--321, DOI 10.1016/0022-1236(72)90004-3
  - L. Zsido, On spectral subspaces associated to locally compact Abelian groups of operators, Advances in Mathematics 36 (1980), 213--276, DOI 10.1016/0001-8708(80)90016-X
  - standard positivity of operator-valued Fourier/Toeplitz coefficient matrices and the block-matrix support factorization for positive operators
---

# WP-397 — Multi-frequency positivity is support-dominated by the critical centralizer shadow

## Claim

`WP-396` leaves one immediate critical-factor escape open: combine several nonzero modular/gauge frequencies before taking positivity. If

\[
y=\sum_{r\in F}x_r,
\qquad x_r\in M_r,
\]

then `y^*y` contains cross-frequency terms `x_r^*x_s` that need not lie in the centralizer. So the one-mode argument alone does not show that a genuinely multi-frequency positive element loses all noncentral information.

There is nevertheless an exact obstruction to using those cross terms to cancel the zero-frequency part.

Let

\[
M=\pi_{\phi_1}(A_{BC})'',
\qquad
K=\widehat{\mathbf Q_+^\times},
\]

with the normal compact gauge action `theta` from `WP-395`, and let

\[
E(a)=\int_K\theta_\chi(a)\,d\chi
\]

be the canonical normal conditional expectation onto

\[
N=M^K=M_{\phi_1}
\cong L^\infty(\widehat{\mathbf Z},m_{\rm Haar}).
\]

For `r in Q_+^*`, write

\[
a_r=E_r(a)
:=\int_K\overline{\chi(r)}\,\theta_\chi(a)\,d\chi
\in M_r.
\]

Then every bounded `a>=0` satisfies:

1. `E(a)=0` if and only if `a=0`;
2. if `d=E(a)` and `p=s(d)` is its support projection in `N`, then for every gauge frequency `r`,

\[
\boxed{a_r=p\,a_r\,p;}
\]

3. equivalently, both source and range supports of every Fourier coefficient obey

\[
s(a_r^*a_r)\le p,
\qquad
s(a_ra_r^*)\le p.
\]

Thus a positive multi-frequency element cannot hide nonzero off-diagonal frequency data over a region where its centralizer shadow vanishes. The zero-frequency component is an **uncancellable support floor** for all of its gauge Fourier coefficients.

For a finite spectral sum `y=sum_r x_r`, this specializes to the explicit identity

\[
\boxed{
E(y^*y)=\sum_r x_r^*x_r.
}
\]

All cross-frequency terms disappear under the canonical source gauge average, while the surviving self-pairings are positive and cannot cancel one another.

Combining this with `WP-395` gives the arithmetic consequence. If the canonical diagonal support of a positive multi-frequency construction is required to lie in the standard prime-power orbit

\[
\mathcal P_\alpha=\{p^j\alpha:p\text{ prime},\ j\ge1\}
\subset\widehat{\mathbf Z},
\]

then that support projection is zero because `P_alpha` is Haar-null. Hence `E(a)=0`, and faithfulness forces `a=0`. If instead one prescribes only point values on the countable arithmetic orbit, `WP-395` already shows that those values are not operator invariants in the `L^infty` centralizer.

Therefore **multi-frequency interference does not rescue exact prime-power selection by cancelling the diffuse critical centralizer component**. A surviving bounded critical-factor route must keep a nonzero diffuse centralizer shadow and use genuinely off-diagonal/nonzero-frequency information in an essential way, or it must change the ambient category/readout.

This does not say that every noncentral positive element is central, nor that off-diagonal modular correlations are arithmetically useless. It closes the narrower escape in which cross-frequency interference was expected to erase the zero-frequency obstruction while leaving a positive exact selector.

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + CRITICAL-KMS-GNS + COMPACT-GAUGE-EXPECTATION + FAITHFUL-CONDITIONAL-EXPECTATION + OPERATOR-VALUED-FOURIER-POSITIVITY + MULTI-FREQUENCY + CENTRALIZER-SUPPORT-DOMINATION + UNCANCELLABLE-ZERO-FREQUENCY-FLOOR + PRIME-POWER-ORBIT-NULL + BOUNDED-POSITIVE-NO-GO + MATCHED-CONTROL-UNIVERSAL + CATEGORY-BOUNDARY + NOT-A-WEIL-BRIDGE`.

## 1. The critical gauge expectation is faithful on positive elements

`WP-395` constructs the compact gauge action by extending the source Bost--Connes energy grading. The critical state `phi_1` is invariant under this action, so

\[
\phi_1(E(a))=\phi_1(a)
\qquad(a\in M_+).
\]

The GNS state is faithful normal on `M`. Therefore, if `a>=0` and `E(a)=0`, then

\[
0=\phi_1(E(a))=\phi_1(a),
\]

and faithfulness gives `a=0`.

This is the first obstruction to cross-frequency cancellation: no nonzero positive element can have zero gauge-invariant component. The result is standard conditional-expectation theory; the line-specific content comes from the identification of the fixed algebra with the diffuse critical centralizer in `WP-395`.

## 2. Positivity makes the Fourier coefficients an operator-valued positive-definite family

Let `a>=0`. For any finite frequencies `r_1,...,r_n in Q_+^*`, the matrix

\[
\Big[a_{r_i^{-1}r_j}\Big]_{i,j=1}^n
\]

is positive in `M_n(M)`.

Indeed, for arbitrary `c_1,...,c_n in M`, set

\[
b_\chi=\sum_i\overline{\chi(r_i)}c_i.
\]

Then

\[
\begin{aligned}
\sum_{i,j}c_i^*a_{r_i^{-1}r_j}c_j
&=\int_K b_\chi^*\,\theta_\chi(a)\,b_\chi\,d\chi\\
&\ge0.
\end{aligned}
\]

Taking just the frequencies `1` and `r` gives

\[
\boxed{
\begin{pmatrix}
d&a_r\\
a_r^*&d
\end{pmatrix}\ge0,
\qquad d=E(a).
}
\]

So the nonzero-frequency coefficient is not an independent degree of freedom: positivity couples it to the centralizer coefficient through an ordinary positive `2 x 2` operator matrix.

## 3. The centralizer support dominates every nonzero frequency

Let `p=s(d)` and `q=1-p`. Since `qd=dq=0`, compress the positive block matrix above against vectors supported in the `q` corner. The diagonal quadratic term there is zero. Positivity for arbitrary complex scalar multiples of a second vector then forces the corresponding cross term to vanish. Thus

\[
q a_r=0,
\qquad
a_r q=0,
\]

for every `r`. Equivalently,

\[
a_r=p a_r p.
\]

This is also the support content of the standard block-factorization theorem: a positive block matrix `[[d,x],[x^*,d]]` factors its off-diagonal entry through the support of `d`.

Hence the source and range support projections of `a_r` satisfy

\[
s(a_r^*a_r)\le p,
\qquad
s(a_ra_r^*)\le p.
\]

The conclusion is stronger than the scalar statement `E(a) != 0`. It says that **every modular frequency of a positive element lives over the measurable support already occupied by the centralizer shadow**. Cross-frequency information may change phase, transport, or correlation inside that support, but it cannot create positive arithmetic mass on a centralizer-null set.

## 4. Finite multi-frequency squares have an explicit noncancellable floor

The open boundary in `WP-396` can now be written exactly. Let

\[
y=\sum_{r\in F}x_r,
\qquad x_r\in M_r,
\]

with distinct frequencies. Then

\[
y^*y
=\sum_r x_r^*x_r
+\sum_{r\ne s}x_r^*x_s.
\]

Because `x_r^*x_s` has frequency `r^{-1}s`, the gauge expectation removes every cross term with `r != s` and gives

\[
E(y^*y)=\sum_r x_r^*x_r.
\]

Each summand is positive. If `y != 0`, uniqueness of Fourier coefficients implies at least one `x_r != 0`, hence the right-hand side is nonzero. There is no destructive interference available at zero frequency.

This extends the finite-cylinder self-pairing calculation of `WP-226` in a different category and at a different level of generality. `WP-226` computed the zero-mode square of one specific finite Bost--Connes Weil defect and found squared half-density plus absence of cross-prime resonance. Here no special defect or coefficient formula is assumed: positivity itself forces the zero-frequency floor for every bounded multi-frequency element of the critical KMS factor.

## 5. Exact prime-power diagonal support still collapses

Under `WP-395`, the centralizer support projection `p` is a measurable projection in

\[
L^\infty(\widehat{\mathbf Z},m_{\rm Haar}).
\]

For a standard arithmetic unit `alpha`, both the full orbit `O_alpha={n alpha:n>=1}` and the prime-power subset `P_alpha` are countable and Haar-null.

Suppose one asks a bounded positive multi-frequency element to retain exact prime-power support in its canonical gauge-invariant diagonal, meaning

\[
p\le 1_{\mathcal P_\alpha}
\]

in the measurable centralizer. The right-hand side is the zero projection, so `p=0`, hence `d=E(a)=0`, and Section 1 gives `a=0`.

Moreover Section 3 prevents an attempted repair in which the diagonal vanishes there but a nonzero off-diagonal Fourier coefficient survives over that null support: every `a_r` is already supported by `p` on both sides.

The alternative pointwise formulation is no better. Changing representatives of an `L^infty` function on the countable orbit changes no operator, so statements such as "zero on mixed-prime orbit points but nonzero on prime powers" are not well-defined properties of the centralizer shadow.

Thus the critical factor can retain noncentral frequency information, but a positive element cannot use that information to restore the **atomic orbit support semantics** of the standard positive-energy representation while keeping the canonical critical measure class.

## 6. Stress tests and exact boundary

A noncentral positive element is perfectly possible. For example, if `x in M_r`, then

\[
a=(1+x)^*(1+x)
\]

is positive and generally has frequencies `1`, `r`, and `r^{-1}`. The theorem does not remove those cross terms. It says only that their source/range support is dominated by the nonzero centralizer coefficient

\[
E(a)=1+x^*x.
\]

So this is not a hidden claim that positivity forces gauge invariance.

The theorem also does not prove that a diffuse-support off-diagonal coefficient cannot encode arithmetic information through some other invariant. A source-forced correlation, correspondence, or finite--archimedean coupling may use nonzero frequencies essentially while accepting a nonzero diffuse centralizer floor. Such a construction would be a genuinely different hypothesis and must be tested on its own normalization and sign mechanism.

The bounded hypothesis matters. Conditional expectation extends to the extended positive cone, but arbitrary multi-frequency affiliated operators require domain and Fourier-decomposition control not supplied here. Continuous-core/crossed-product constructions, genuinely unbounded nonhomogeneous forms, one-sided correspondences, and nonunital boundary categories remain outside the result.

Finally, the operator-algebraic mechanism is universal. Any compact group action preserving a faithful normal state has the same faithful fixed-point expectation and positive-definite Fourier coefficient matrices. Therefore the positivity theorem by itself is not Riemann-specific. Its research value here is negative and structural: after the source-forced Bost--Connes identifications of `WP-395`, it shows that the most immediate multi-frequency cancellation escape cannot restore a nonzero atomic prime-power selector.

## 7. Prior-art and novelty audit

Compact-group averaging onto a fixed-point von Neumann algebra and faithful state-preserving conditional expectations are classical operator-algebra machinery; Takesaki's 1972 theorem is the standard conditional-expectation anchor. Spectral subspaces for abelian automorphism groups are likewise classical, with Zsido providing a standard reference. Positivity of the Fourier/Toeplitz coefficient matrices above is the usual positive-definite consequence of integrating positive conjugate-frequency combinations.

No novelty is claimed for those general facts. The durable delta is their application to the exact frontier left by `WP-395`--`WP-396`: the fixed algebra is the Haar-measurable critical Bost--Connes centralizer, the standard arithmetic orbit is null there, and positivity forces every multi-frequency coefficient to be supported by the centralizer shadow. This turns the previously open "cross-frequency interference" escape into a sharper boundary: interference may carry information, but it cannot cancel the centralizer support floor and leave a nonzero positive exact orbit selector.

The closest internal predecessor is `WP-226`, which studies one specific finite-prime defect under a time-zero self-pairing. `WP-331` gives a different faithful-conditional-expectation obstruction for source-preserving centered enrichments. Neither proves the critical-factor Fourier support domination above. `WP-396` handles only one homogeneous mode and explicitly leaves multi-frequency cross terms open.

A bounded literature check found the classical conditional-expectation and spectral-subspace ingredients, but no source claiming the Mathia-specific Bost--Connes/prime-power consequence. The claim should therefore be read as an exact derived narrowing of this research line, not as a new general theorem in operator algebras.

## Research consequence

The critical Bost--Connes factor remains a possible source of noncentral arithmetic structure, but the route is now narrower. A viable bounded positive construction cannot rely on multi-frequency destructive interference to remove the diffuse centralizer component while preserving an atomic prime-power selector. It must instead **use the surviving nonzero-frequency correlations themselves as the arithmetic datum while tolerating their nonzero diffuse centralizer support**, or move to a genuinely different category such as a continuous core, correspondence, unbounded nonhomogeneous form, or finite--archimedean global assembly.

That is the next live boundary; no Weil sign theorem follows from the present obstruction.