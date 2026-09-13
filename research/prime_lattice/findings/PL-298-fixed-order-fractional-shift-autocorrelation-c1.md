# PL-298 — Fixed-order fractional boundary regularity makes prime-shift autocorrelations `C^1` without a uniform `H^{1/2}` moment

**Evidence:** `LITERATURE+EXACT-DERIVED + POSITIVE-ROUTE-REFINEMENT + SMALL-ORDER-GATE`

**Status:** `FIXED-S-C1-ARITHMETIC + ACTIVATION-SMOOTH + S-TO-ZERO-UNRESOLVED`

## Claim

The `H^{1/2}` obstruction in `PL-293` and the stress/moment decoupling in `PL-297` do **not** obstruct differentiability of the discrete prime-shift terms at a fixed positive fractional order. There is a simpler physical-space route.

If `u` is compactly supported and

\[
u\in W^{1,1}(\mathbb R)\cap L^\infty(\mathbb R),
\]

then its translation autocorrelation

\[
C_u(h):=\int_{\mathbb R}u(x)\overline{u(x+h)}\,dx
\]

belongs to `C^1(R)` and

\[
\boxed{
C_u'(h)=\int_{\mathbb R}u(x)\overline{u'(x+h)}\,dx,
\qquad
\|C_u'\|_\infty\le \|u\|_\infty\|u'\|_1.
}
\]

If `supp(u) subset [-1,1]`, then `C_u(h)=0` for `|h|>=2`; hence continuity of the derivative forces

\[
\boxed{C_u(\pm2)=C_u'(\pm2)=0.}
\]

For every fixed `s in (0,1)`, the positive zero-exterior Dirichlet principal eigenfunction of `(-Delta)^s` on a smooth interval satisfies exactly the regularity needed for this lemma. Djitte--Fall--Weth recall that `u/delta^s` extends Hölder continuously to the boundary and that `delta^(1-s) grad u` has a Hölder extension. In one dimension this gives `|u'(x)| <= C delta(x)^(s-1)` near the endpoints, which is integrable for every fixed `s>0`; since the boundary trace of `u` itself is zero, its zero extension belongs to `W^{1,1}(R) cap L^infty(R)`.

Consequently the discrete prime-power part of a fixed-order fractional regularization of the localized-Weil problem has an ordinary `C^1` quadratic-form derivative with respect to the shift parameter whenever its state has this standard fractional boundary regularity. Moreover, when a new prime-power shift first enters through the support edge, the value and first derivative of that term both vanish. **Prime-source activation therefore creates no `C^1` cusp at fixed fractional order.**

This is not yet a zero-order Hadamard theorem. The unresolved issue is now sharper: one must prove the corresponding regularity for the actual regularized completed-Weil eigenbranch and control the `s->0+` limit of these physical-space shift derivatives. `PL-297` shows that this limit cannot be justified by replacing it with a uniform `H^{1/2}` estimate.

## 1. A physical-space autocorrelation lemma

Let `u in W^{1,1}(R) cap L^infty(R)` have compact support. The translation map

\[
h\longmapsto T_hu,\qquad (T_hu)(x)=u(x+h),
\]

is continuously differentiable as an `L^1(R)`-valued map, with derivative `T_hu'`. Pairing this map against the fixed bounded function `u` gives

\[
C_u'(h)=\int u(x)\overline{u'(x+h)}\,dx.
\]

Translation continuity of `u'` in `L^1` makes `C_u'` continuous, while Hölder's inequality in `L^infty x L^1` gives

\[
|C_u'(h)|\le \|u\|_\infty\|u'\|_1.
\]

No Fourier first moment occurs in this proof. In particular, the sufficient condition

\[
\int_{\mathbb R}|\xi|\,|\widehat u(\xi)|^2\,d\xi<\infty
\]

used for absolute dominated-convergence differentiation in `PL-293` is not logically necessary for differentiability of `C_u`.

If `supp(u) subset [-1,1]`, the two translates have disjoint interiors once `|h|>=2`, so `C_u` is identically zero on each exterior half-line. Since `C_u in C^1(R)`, its derivative must match the exterior derivative at the support edge and therefore `C_u'(2)=C_u'(-2)=0`.

This endpoint fact is the key source-activation observation: a shift term whose lag crosses `2` turns on to first order with zero value and zero slope.

## 2. Fixed-order fractional Dirichlet states satisfy the lemma

For a positive normalized principal minimizer of the fractional Dirichlet problem, Djitte--Fall--Weth use the standard boundary regularity

\[
\frac{u}{\delta^s}\in C^\alpha(\overline\Omega),
\qquad
\delta^{1-s}\nabla u\in C^\alpha(\overline\Omega),
\]

and on the boundary

\[
\delta^{1-s}\nabla u\cdot\nu
=s\frac{u}{\delta^s}.
\]

On an interval the second statement implies, in a boundary collar,

\[
|u'(x)|\le C\delta(x)^{s-1}.
\]

Because

\[
\int_0^\varepsilon t^{s-1}\,dt=\frac{\varepsilon^s}{s}<\infty
\]

for every fixed `s>0`, and the solution is `C^1` in the interior, `u' in L^1`. The first boundary estimate gives boundedness and `u->0` at each endpoint. Thus zero extension introduces no endpoint Dirac mass in the distributional derivative, and

\[
Eu\in W^{1,1}(\mathbb R)\cap L^\infty(\mathbb R).
\]

Therefore the preceding autocorrelation lemma applies to the canonical fixed-order fractional principal state.

The constants here are allowed to depend on `s`. That qualification is essential. The estimate proves existence of the derivative for every positive order; it does not establish the uniform compactness needed to pass that derivative to `s=0`.

## 3. Prime-power shifts are differentiable through activation

On a source-static aperture interval, after the fixed-domain rescaling used in the localized-Weil analysis, each discrete arithmetic contribution has the form

\[
q_n(a;u)=b_n(a)\,C_u(h_n(a)),
\qquad
h_n(a)=\frac{\log n}{a},
\]

with a smooth explicit coefficient `b_n(a)` and `Lambda(n)>0`. When differentiating the operator/form at a fixed normalized state, the physical-space lemma gives

\[
\frac d{da}q_n(a;u)
=b_n'(a)C_u(h_n(a))
-b_n(a)\frac{\log n}{a^2}C_u'(h_n(a)).
\]

At the activation aperture

\[
a_n=\frac{\log n}{2},
\qquad h_n(a_n)=2,
\]

both factors from the correlation vanish:

\[
C_u(2)=C_u'(2)=0.
\]

Hence the term obtained by setting it equal to zero before activation and using the displayed expression after activation is `C^1` across `a=a_n`. Locally only finitely many prime powers can overlap a compactly supported state, so the entire discrete von-Mangoldt sum is `C^1` at fixed order under the same regularity hypothesis.

This removes one specific failure mode from the accepted Hadamard clue: a new prime-power source does not by itself create a first-derivative singularity. Any singularity in a full aperture derivative must instead come from loss of state regularity, the continuous/completion term, branch behavior, or failure of uniform control as `s->0`.

## 4. Why this does not contradict the `H^{1/2}` obstruction

`PL-293` proved that the sharp logarithmic boundary scale `ell(delta)^(1/2)` can force the zero extension outside `H^{1/2}`. `PL-297` then showed that the fractional boundary stress can have a finite nonzero `sqrt(s)` renormalization while the `H^{1/2}` norms diverge as `s->0+`.

The present mechanism uses a different Banach-space pairing. Fourier absolute differentiation controls

\[
\int |\xi|\,|\widehat u(\xi)|^2d\xi,
\]

whereas physical-space differentiation controls

\[
\|u\|_\infty\|u'\|_1.
\]

Neither quantity is a surrogate for the other in the singular small-order limit. For fixed `s`, fractional boundary behavior `u~delta^s` makes the spatial derivative integrable even though the family can lose every uniform critical half-Sobolev bound as `s->0`.

Thus `PL-293` should be read exactly as stated there: it blocks the routine **absolute Fourier-moment** route, not every possible derivative of a nonzero-lag autocorrelation. The present lemma realizes one of the conditional/physical-space escapes that `PL-293` explicitly left open.

## 5. What remains for the actual completed-Weil branch

The result settles only the kinematic regularity of the discrete shift channel at fixed positive order. The accepted clue still requires a theorem for the **actual regularized completed-Weil simple eigenbranch**. In particular one must establish that the chosen regularization gives eigenstates to which the bounded-RHS fractional boundary estimates apply uniformly enough to justify the full form derivative.

Even after fixed-`s` differentiability is established, the hard limit remains

\[
s\to0^+.
\]

The bound `||C_u'||_infty <= ||u||_infty ||u'||_1` is useful only if the relevant norms, or the particular correlation derivatives at the active prime lags, are compact enough in `s`. The boundary estimate `|u_s'| <= C_s delta^(s-1)` by itself gives no uniform information because its constant may depend singularly on `s`. `PL-297` prevents recovering that missing compactness from a uniform `H^{1/2}` estimate.

The continuous archimedean/completion remainder also has to be differentiated and passed to the limit independently. Nothing here gives its sign, nor any rational-prime-specific constraint on the resulting derivative.

## 6. Prior art and novelty audit

The fractional boundary regularity and Hadamard framework are prior art. Djitte--Fall--Weth prove the fractional Hadamard formula and explicitly record the Hölder extension of `u/delta^s` and `delta^(1-s) grad u`, including the boundary relation used above. Recent work of Djitte--Sueur gives a pointwise fixed-order Hadamard theory for fractional Dirichlet problems, further confirming that fixed-`s` shape differentiation is established PDE structure rather than a new arithmetic mechanism.

The fact that translations are `C^1` in `L^1` on `W^{1,1}`, and hence that convolution/autocorrelation inherits the displayed derivative, is elementary classical analysis. No novelty is claimed for that lemma in isolation.

A targeted search of fractional-Hadamard, fractional-boundary-regularity, autocorrelation differentiability, and localized-Weil/prime-shift literature did not locate the exact line-local consequence used here: the fixed-order fractional boundary law places the compactly supported state in `W^{1,1}`, which makes every discrete prime-shift quadratic term `C^1` and forces both value and slope to vanish at prime-power activation. This is recorded as `EXACT-DERIVED`, not as a broad originality claim.

The mathematical delta relative to `PL-293`--`PL-297` is the separation of two proof obligations: **fixed-order existence of the arithmetic shift derivative is cheap once `W^{1,1}` boundary regularity is available; the difficult part is uniform small-order transport of that derivative and the completed remainder.**

## 7. Boundaries and falsification tests

1. **No full-Weil fractional regularity theorem is claimed.** The direct application above is rigorous for the canonical fractional Dirichlet principal state. Applying it to a bounded perturbation requires verifying the regularized completed-Weil eigen-equation lies in the hypotheses of the relevant boundary/gradient estimates.
2. **No uniform `s->0` estimate is claimed.** Fixed-order `W^{1,1}` can coexist with divergence of stronger norms or of its own constants as `s->0`.
3. **No replacement of Hadamard stress by `W^{1,1}`.** The boundary-stress term and the translation derivative are different contributions. The point is only that the latter can be differentiated without importing the forbidden half-Sobolev shortcut.
4. **No arithmetic sign theorem.** Smooth activation is kinematic and survives matched nonarithmetic weights. Rational-prime rigidity, if any, must arise from the values/coupling of the active shifts or the completion term.
5. **Decisive next test.** For the actual fractionalized operator near the certified `a=0.8` branch, prove bounded-RHS boundary/gradient regularity and obtain a uniform or convergent formula for `C'_{u_{s,a}}(log n/a)` at the active prime powers. Failure of such compactness leaves the Hadamard route open but blocks this physical-space passage to `s=0`.

## Consequence for `prime_lattice`

The accepted zero-order Hadamard route no longer needs to treat differentiability of the finite prime-shift comb at **fixed** fractional order as an `H^{1/2}` problem. The source activation itself is also first-order smooth. The live analytic bottleneck moves to the actual perturbed eigenbranch and the singular `s->0` passage:

\[
\boxed{
\text{fixed }s>0:\ \text{prime shifts are }C^1\text{ under standard fractional boundary regularity};
\qquad
s\to0^+:\ \text{uniform derivative transport remains open}.
}
\]

That is a narrower and falsifiable gate than asking for a generic positive Sobolev exponent.

## Literature anchors

- Sidy Moctar Djitte, Mouhamed Moustapha Fall, Tobias Weth, “A fractional Hadamard formula and applications,” *Calculus of Variations and Partial Differential Equations* **60** (2021), Article 231. DOI: `10.1007/s00526-021-02094-3`.
- Sidy M. Djitte, Franck Sueur, “Pointwise Hadamard variational formula for the fractional Laplacian,” *Annales de la Faculté des Sciences de Toulouse* (2026); arXiv:`2602.07214`.
