# WP-195 — Positive-definite background spectra preserve `4k` Weil-cone positivity away from zero

**Status:** `DERIVED + EXACT + HIGHER-ORDER-SPECTRAL-SHIFT + COMMUTING-FINITE-DIMENSIONAL + FULL-WEIL-AUTOCORRELATION-CONE + OFF-CENTER-POSITIVITY + SPECTRAL-AUTOCORRELATION-CLASS + MATCHED-NONARITHMETIC-CONTROL + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-194` proves a sharp scalar statement: for a nonzero scalar perturbation, full order-`4k` positivity on every real compactly supported smooth autocorrelation holds exactly when the scalar background is centered at zero. It explicitly leaves operator-level centering open.

That scalar rigidity does **not** globalize. A finite commuting direct sum can restore full Weil-autocorrelation positivity while its background has genuinely nonzero spectrum. The mechanism is exact and elementary: translated scalar spectral-shift densities add, and a positive-definite spectral multiplicity pattern turns their translation phases into a nonnegative Fourier multiplier.

In particular, for every `a!=0`, every `v>0`, and every `k>=1`,

\[
H_a=\operatorname{diag}(0,0,a,-a),
\qquad
V=vI_4
\tag{1}
\]

satisfy

\[
\boxed{
\mathcal R_{4k}(g*\widetilde g;H_a,V)>0
\quad\text{for every }0\ne g\in C_c^\infty(\mathbb R),\ g\text{ real},
}
\tag{2}
\]

even though `H_a!=0` and its spectrum is not concentrated at the origin.

More generally, every finite **difference-spectrum** background obtained from an atomic measure `nu` by the autocorrelation `mu=nu*\widetilde nu` has the same property for the scalar perturbation `V=vI`. Thus the extra positive-definiteness required by `WP-193` can be manufactured by ordinary spectral multiplicity interference, not only by source-centering.

This materially strengthens the matched-control warning around higher-order spectral shift. A viable Mathia bridge cannot count either zero centering or `4k` Weil-cone positivity as arithmetic evidence. It must explain why the source geometry forces the actual finite-prime, Gamma, and polar/global terms inside the same ordered object.

## 1. Direct sums turn background locations into a Fourier multiplier

Fix an order

\[
n=4k,\qquad r=n-1,
\tag{3}
\]

and a scalar perturbation size `v>0`. For a one-dimensional background `c`, the scalar Taylor-remainder density from `WP-194` is

\[
q_{n,v}(x-c),
\qquad
q_{n,v}(x)
=\frac{(v-x)^r}{r!}\,\mathbf 1_{[0,v]}(x).
\tag{4}
\]

Now let

\[
H=\operatorname{diag}(c_1,\ldots,c_N),
\qquad
V=vI_N.
\tag{5}
\]

Because `H` and `V` are simultaneously diagonal, the Taylor remainder is the sum of the scalar channel remainders. Therefore its higher-order spectral-shift density is exactly

\[
\eta_{n,H,V}(x)
=\sum_{j=1}^N q_{n,v}(x-c_j).
\tag{6}
\]

Introduce the finite background counting measure

\[
\mu_H=\sum_{j=1}^N\delta_{c_j}.
\tag{7}
\]

Then

\[
\boxed{
\eta_{n,H,V}=q_{n,v}*\mu_H,
\qquad
\widehat\eta_{n,H,V}(\xi)
=\widehat q_{n,v}(\xi)\widehat\mu_H(\xi).
}
\tag{8}
\]

No operator-theoretic approximation is being used here; this is simply the exact direct-sum trace formula.

## 2. Symmetric positive-definite background spectra give the exact `4k` sign theorem

Assume the background spectrum is symmetric as a multiset, so that

\[
\mu_H(E)=\mu_H(-E).
\tag{9}
\]

Then its Fourier transform is real and even:

\[
\widehat\mu_H(\xi)=\sum_j e^{-ic_j\xi}\in\mathbb R.
\tag{10}
\]

For a real integrable function, Fourier transformation of the even part takes the real part. Hence (8) gives

\[
\widehat{\eta_{n,H,V}^{\rm ev}}(\xi)
=\widehat\mu_H(\xi)\,
\operatorname{Re}\widehat q_{n,v}(\xi).
\tag{11}
\]

The second factor is exactly the centered scalar even density from `WP-194`. Writing

\[
\phi_{n,v}(x)
=\frac{(v-|x|)_+^r}{2r!},
\tag{12}
\]

we have

\[
\operatorname{Re}\widehat q_{n,v}(\xi)
=\widehat\phi_{n,v}(\xi)>0
\qquad\text{for every }\xi\in\mathbb R.
\tag{13}
\]

Therefore the exact `WP-193` autocorrelation criterion reduces in this commuting family to

\[
\boxed{
\mathcal R_{4k}(g*\widetilde g;H,vI)\ge0
\text{ for every real }g\in C_c^\infty
\iff
\widehat\mu_H(\xi)\ge0
\text{ for every }\xi.
}
\tag{14}
\]

Indeed, substituting (11) into the Fourier formula of `WP-193` yields

\[
\boxed{
\mathcal R_{4k}(g*\widetilde g;H,vI)
=\frac1{2\pi}\int_{\mathbb R}
\xi^{4k}|\widehat g(\xi)|^2
\widehat\mu_H(\xi)
\widehat\phi_{4k,v}(\xi)\,d\xi.
}
\tag{15}
\]

Since `\widehat\phi_{4k,v}` is strictly positive, the background multiplicity function `\widehat\mu_H` is the only remaining sign factor.

For a nonzero finite positive counting measure with `\widehat\mu_H>=0`, the inequality in (15) is strict for every nonzero `g`. The multiplier is positive on a neighborhood of the origin because `\widehat\mu_H(0)=N>0`, while the Fourier transform of a nonzero compactly supported smooth function cannot vanish on an interval.

Thus scalar centering rigidity is replaced at operator level by an ordinary positive-definiteness condition on the **background spectrum itself**.

## 3. A four-dimensional off-center counterexample to operator centering rigidity

Take `a!=0` and the background in (1). Its counting measure is

\[
\mu_a=2\delta_0+\delta_a+\delta_{-a}.
\tag{16}
\]

Its Fourier transform factors exactly:

\[
\boxed{
\widehat\mu_a(\xi)
=2+2\cos(a\xi)
=4\cos^2\!\left(\frac{a\xi}{2}\right)
\ge0.
}
\tag{17}
\]

Equations (14)--(17) prove (2).

This is a deliberately strong falsification control for the interpretation left after `WP-194`. Every off-center scalar channel at `c=a` or `c=-a` fails the full autocorrelation sign test on its own. The direct sum repairs the sign not by moving those channels back to zero, but by adding the translation phases with the multiplicity pattern `2,1,1`, whose Fourier symbol is a perfect square.

The zero eigenvalue is present with multiplicity two, but the conclusion is not a disguised copy of the `H=0` theorem. The translated densities at `\pm a` contribute nontrivially to the remainder, and deleting either their pair or one of the two zero channels changes the background Fourier multiplier and can restore sign changes. The sign is a property of the assembled multiplicity pattern.

## 4. Difference spectra give a large universal family

The example (16) is the smallest two-point autocorrelation construction. Let

\[
\nu=\sum_{j=1}^M m_j\delta_{a_j},
\qquad m_j\in\mathbb N,
\tag{18}
\]

and reflect it by `\widetilde\nu(E)=\nu(-E)`. Define

\[
\mu=\nu*\widetilde\nu.
\tag{19}
\]

This is again a finite positive atomic measure, with atoms at all differences `a_i-a_j` and integer multiplicities `m_i m_j`. It can therefore be realized exactly as the spectral counting measure of a finite diagonal self-adjoint background `H_\nu`.

Its Fourier transform is the elementary autocorrelation square

\[
\boxed{
\widehat\mu(\xi)
=\widehat\nu(\xi)\overline{\widehat\nu(\xi)}
=|\widehat\nu(\xi)|^2
\ge0.
}
\tag{20}
\]

Consequently, for every `v>0` and `k>=1`,

\[
\boxed{
\mathcal R_{4k}(g*\widetilde g;H_\nu,vI)>0
\quad
\text{for every nonzero real }g\in C_c^\infty(\mathbb R).
}
\tag{21}
\]

The construction is entirely arithmetic-free. The points `a_j` may be deterministic, generic real numbers, or chosen from an unrelated physical spectrum. Nothing singles out prime logarithms, the Riemann Gamma factor, or a zeta completion.

This family is already broad enough to kill a stronger possible reading of the `WP-194` survivor: **full `4k` Weil-cone positivity does not force a canonical spectral origin even among finite commuting pairs**. Off-center backgrounds can satisfy the exact same sign criterion through a classical autocorrelation factorization of their multiplicities.

## 5. Aggressive falsification and exact scope

**This does not contradict the scalar iff theorem of `WP-194`.** Each scalar translated density still has the high-frequency sign oscillation proved there. What changes is that direct-sum spectral multiplicities multiply the common centered Fourier factor by `\widehat\mu_H`; a positive-definite multiplicity pattern cancels those translation-sign oscillations in the assembled even density.

**The common perturbation size matters to the exact factorization.** Equations (8)--(15) use `V=vI`, so every scalar channel has the same base density `q_{n,v}`. Different perturbation sizes lead to a sum of different Fourier factors and are not classified here. The result is a sufficient matched-control family, not a classification of all commuting pairs.

**Symmetry is part of the clean iff statement.** For a nonsymmetric background, the exact condition is `Re(\widehat q_{n,v}\widehat\mu_H)>=0`, not simply `\widehat\mu_H>=0`. The explicit counterexample and the difference-spectrum family are symmetric, so no extra phase issue occurs.

**No noncommuting claim is made.** A noncommuting pair may admit additional positive-definite higher-order spectral-shift densities, or may fail for reasons absent from the direct-sum model. This finding only closes the inference that operator-level positivity should force `H=0`.

**No Weil coefficient is generated.** The construction proves positivity on the same abstract autocorrelation cone used in the Weil criterion, but it has no Mangoldt selector, no Gamma term, and no polar/global counterterm. Fitting the `a_j` or multiplicities to arithmetic data after the fact would be exactly the hand-picked spectral engineering excluded by the research mandate.

**The matched control is stronger than simple translation.** `WP-194` already shows that translating one scalar pair destroys positivity. Here several translated channels recover positivity by spectral interference. Therefore rejecting a proposed `4k` mechanism merely because its background is not centered is invalid; the real question is what source forces the positive-definite assembled density and whether that same source also carries the arithmetic completion.

## 6. Prior-art and novelty boundary

The analytic ingredients are classical or already audited in this branch. Potapov--Skripka--Sukochev higher-order spectral-shift theory supplies the trace-density framework used in `WP-193`; the scalar Taylor integral remainder and the centered truncated-power Fourier positivity are recorded in `WP-194`. Direct sums, translation phases under Fourier transform, and the autocorrelation identity

\[
\widehat{\nu*\widetilde\nu}=|\widehat\nu|^2
\tag{22}
\]

are standard harmonic analysis.

A targeted literature search across higher-order spectral shift, commuting/diagonal perturbations, positive-definite truncated powers, Fourier positivity, and spectral/autocorrelation factorization found the expected classical ingredients but no reason to treat the assembled construction as a new operator-theory theorem. No novelty is claimed for those ingredients. The durable Mathia result is the **branch-specific matched-control consequence**: the scalar centering rigidity of `WP-194` provably fails at the first nontrivial operator-multiplicity level, and there is a large explicit nonarithmetic class satisfying the exact `WP-193` Weil-cone gate off center.

## 7. Consequence for `weil_positivity`

The higher-order spectral-shift frontier has narrowed again. `WP-193` required positive definiteness of the even `4k` density; `WP-194` showed that zero background supplies it universally and that scalar translations destroy it. The present finding shows that **zero background is not the operator-level source of the order theorem**. Positive-definite spectral multiplicity can restore the same order far from scalar centering.

Hence the live obligation cannot be phrased as merely finding a canonical `H=0` realization. A credible bridge must force substantially more structure before arithmetic matching:

\[
\boxed{
\text{source-native finite--archimedean object}
\Longrightarrow
\text{positive-definite completed `4k` density}
\Longrightarrow
\text{exact finite-prime + Gamma + polar Weil functional},
}
\tag{23}
\]

where the first implication has an independent theorem and the construction survives the nonarithmetic difference-spectrum controls above.

The sign gate by itself is now known to have at least two broad universal realizations: zero-background direct sums and off-center positive-definite background spectra. Neither explains the arithmetic. Any future `4k` candidate must therefore demonstrate that its positive-definite density is **source-selective**, not merely another harmonic autocorrelation square hidden in spectral multiplicities.

## Dependencies

- `research/weil_positivity/findings/WP-193-higher-order-spectral-shift-positivity-has-a-mod-four-weil-autocorrelation-gate.md`
- `research/weil_positivity/findings/WP-194-source-centered-4k-taylor-remainders-are-weil-cone-positive-and-scalar-centering-is-rigid.md`

## Bottom line

The scalar centering rigidity in `WP-194` is real but not an operator rigidity theorem. At every order `4k`, a finite commuting background with spectral counting measure `mu` inherits full Weil-autocorrelation positivity whenever `mu` is positive definite; the explicit off-center background `diag(0,0,a,-a)` works because its Fourier multiplicity is `4 cos^2(a xi/2)`. More generally, every finite difference spectrum `nu*tilde nu` works.

Therefore higher-order Weil-cone positivity is even less arithmetically selective than the zero-background control suggested. The remaining research burden is not to find a spectral origin that makes the sign work, but to derive from Mathia a single source-native finite--archimedean structure whose independently forced order survives these universal controls and whose same geometry produces the actual global Weil terms.