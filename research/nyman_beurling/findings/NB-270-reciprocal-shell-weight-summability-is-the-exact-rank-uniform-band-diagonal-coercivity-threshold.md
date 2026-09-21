# NB-270 — Reciprocal shell-weight summability is the exact rank-uniform band-diagonal coercivity threshold

**Date:** 2026-09-21  
**Status:** `EXACT-DERIVED + SHARP-BAND-DIAGONAL-COERCIVITY-CRITERION + RESOLVED-MULTI-SHELL-HARDY-PROJECTION + SHARP-SOBOLEV-THRESHOLD + CRITICAL-ENDPOINT-COUNTERCONTROL + LOG-REFINED-ENDPOINT + NB-269-DESTINATION-INVARIANT-AUDIT + METHOD-BOUNDARY + FRESH-PRIOR-ART-AUDIT`.

`NB-269` shows that the resolved multi-shell matched Ford packet can keep an order-one center residue while the ordinary full-line Hardy quadratic energy is only `Theta(1/K)`. The open destination-side question is therefore not whether the unweighted norm can see the spike—it cannot—but **what extra positive quadratic weight would be sufficient to charge it uniformly in the number of resolved shells**.

For the entire class of full-line quadratic forms that remain diagonal on the resolved shell bands, there is an exact answer. If shell `j` is charged by a positive weight `q_j`, then the Euler anchor `sum_j c_j=1` has a rank-uniform quadratic lower bound if and only if

\[
\boxed{
\sup_K\sum_{j=0}^{K-1}\frac1{q_j}<\infty.
}
\]

Applied to Sobolev weights on the center variable, `q_j asymp (1+j)^(2s)`, this gives the sharp trichotomy

\[
\inf \mathcal E_s
\asymp
\begin{cases}
K^{-(1-2s)}, & 0\le s<1/2,\\[3pt]
1/\log K, & s=1/2,\\[3pt]
1, & s>1/2.
\end{cases}
\]

Thus a positive amount **strictly more than half a center derivative** would charge the `NB-269` spike uniformly, but the critical `H^{1/2}` endpoint still leaks. More sharply, at the endpoint a logarithmic band weight `q_j asymp (j+1)(log(e+j))^alpha` is rank-uniform exactly when `alpha>1`.

This is a destination-interface classification, not a claim that the exact Nyman–Beurling norm supplies any such weight. The standard Hardy boundary norm corresponds to the leaking unweighted case `s=0`.

---

## 1. Setup inherited from `NB-269`

Use the resolved `H`-separated multi-shell dictionary of `NB-269`:

\[
J=mK,
\qquad
m\to\infty,
\qquad
K\to\infty,
\]

with shell-frequency intervals

\[
j+\operatorname{supp}\phi,
\qquad
0\le j<K,
\]

pairwise disjoint because `diam(supp phi)<1`. For a coefficient vector `c=(c_0,...,c_{K-1})`, the projected packet has Fourier representation

\[
\widehat G^{(c)}_J(j+u)
=
c_j\phi(u)A_{j,J}(u),
\qquad
u\in[a,b]\subset(0,1),
\]

where, on the shallow matched packet of `NB-269`, the channel amplitudes obey uniform two-sided bounds

\[
0<a_*\le |A_{j,J}(u)|\le A_*<\infty
\]

for every resolved shell and every `u in [a,b]`, after fixing the packet density sufficiently small. The same construction places all center contributions in a common sector.

The Euler normalization used throughout the multi-shell route is

\[
\boxed{
\sum_{j=0}^{K-1}c_j=1.
}
\]

The small physical renormalization that appeared earlier in the line does not alter the present rank asymptotics because `K/J=1/m -> 0`; the shell-dependent exponential factor is uniformly `1+o(1)` over the resolved family.

The only new ingredient below is to ask what happens if the destination quadratic form charges different resolved bands by different positive amounts.

---

## 2. Exact abstract theorem for every band-diagonal quadratic form

Let

\[
q_j>0,
\qquad
\mathcal E_q(c):=\sum_{j=0}^{K-1}q_j|c_j|^2.
\]

Under the single affine constraint `sum_j c_j=1`, weighted Cauchy–Schwarz gives

\[
1
=
\left|\sum_j c_j\right|^2
=
\left|\sum_j (q_j^{1/2}c_j)q_j^{-1/2}\right|^2
\le
\left(\sum_j q_j|c_j|^2\right)
\left(\sum_j q_j^{-1}\right).
\]

Hence

\[
\mathcal E_q(c)
\ge
\left(\sum_{j=0}^{K-1}q_j^{-1}\right)^{-1}.
\]

This lower bound is exact. Equality is attained by the positive vector

\[
\boxed{
c_j
=
\frac{q_j^{-1}}{\sum_{\ell=0}^{K-1}q_\ell^{-1}}.
}
\]

Therefore

\[
\boxed{
\inf_{\sum c_j=1}\mathcal E_q(c)
=
\left(\sum_{j=0}^{K-1}q_j^{-1}\right)^{-1}.
}
\]

No asymptotic argument, sign assumption, or probabilistic input is involved. This is also the squared inverse norm of the Euler-anchor functional on the weighted shell Hilbert space. Consequently a family of such quadratic forms has a positive lower bound independent of `K` **if and only if**

\[
\boxed{
\sup_K\sum_{j<K}q_j^{-1}<\infty.
}
\]

This reciprocal-summability condition is the exact coercivity threshold for the full band-diagonal class.

The result already explains the `NB-269` loss. In the ordinary full-line Hardy norm the matched packet gives `q_j asymp 1`, so `sum q_j^(-1) asymp K` and the best possible energy is `Theta(1/K)`.

---

## 3. Sobolev weights give a sharp half-derivative transition

To test a natural destination invariant, put a Sobolev weight on the center coordinate `z=H(t-t_0)`. With the same Fourier convention as `NB-269`, define

\[
\mathcal E_s(G)
:=
\frac1{2\pi}
\int_{\mathbb R}
\langle\xi\rangle^{2s}
|\widehat G(\xi)|^2\,d\xi,
\qquad
s\ge0,
\]

where `langle xi rangle=(1+xi^2)^(1/2)`. Disjoint shell bands still diagonalize the form exactly:

\[
\mathcal E_s(G_J^{(c)})
=
\sum_{j=0}^{K-1}q_{j,s}|c_j|^2,
\]

with

\[
q_{j,s}
:=
\int_a^b
\langle j+u\rangle^{2s}
|\phi(u)|^2
|A_{j,J}(u)|^2\,du.
\]

On the matched packet, the uniform bounds on `A_{j,J}` and the fixed compact interval `[a,b]` give

\[
\boxed{
q_{j,s}\asymp_s(1+j)^{2s}
}
\]

uniformly in `j`, `K`, and `J` along the admissible regime. The exact theorem therefore reduces the rank behavior to the elementary reciprocal sum

\[
\sum_{j<K}(1+j)^{-2s}.
\]

Hence

\[
\boxed{
\inf_{\sum c_j=1}\mathcal E_s(G_J^{(c)})
\asymp_s
\begin{cases}
K^{-(1-2s)}, & 0\le s<1/2,\\[3pt]
(\log K)^{-1}, & s=1/2,\\[3pt]
1, & s>1/2.
\end{cases}
}
\]

The `s=0` row recovers the `Theta(1/K)` scaling found directly in `NB-269`. The transition at `s=1/2` is also consistent with the classical one-dimensional Sobolev point-evaluation threshold, but that generic theorem is not used here: the resolved-shell calculation gives the exact line-local rank law directly.

The important distinction is the endpoint. Merely charging one half derivative does **not** give rank-uniform coercivity; it improves `1/K` only to `1/log K`.

---

## 4. A positive critical-endpoint control keeps the center residue but loses `H^{1/2}` energy

The failure at `s=1/2` is not an artifact of an inequality. Take, for the model weights `q_j asymp j+1`, the positive normalized coefficients

\[
c_j
=
\frac{(j+1)^{-1}}{H_K},
\qquad
H_K:=\sum_{\ell=0}^{K-1}(\ell+1)^{-1}
\asymp\log K.
\]

They satisfy

\[
\sum_jc_j=1,
\qquad
c_j\ge0.
\]

Because the matched shell contributions at the center remain in one fixed sector and have amplitudes uniformly bounded below, positivity prevents cancellation. The center residue therefore remains of order one, exactly as in the uniform positive carrier of `NB-269`.

At the same time,

\[
\sum_{j<K}(j+1)|c_j|^2
=
\frac1{H_K^2}
\sum_{j<K}\frac1{j+1}
\asymp
\frac1{\log K}
\longrightarrow0.
\]

Even its unweighted coefficient cost is benign:

\[
\sum_j|c_j|^2
\ll
\frac1{(\log K)^2}.
\]

Thus a legal positive carrier can retain the order-one matched center obstruction while its critical half-derivative quadratic energy vanishes. No signed cancellation or large coefficient conditioning is needed.

This is the direct endpoint analogue of the `NB-269` center-spike counterexample.

---

## 5. The endpoint can be classified more finely by logarithmic weights

The reciprocal-summability criterion gives a sharper boundary than the slogan “more than half a derivative.” Suppose the band energy at the critical polynomial power is refined to

\[
q_j
\asymp
(j+1)\,[\log(e+j)]^\alpha.
\]

Then

\[
\sum_{j<K}q_j^{-1}
\asymp
\sum_{j<K}
\frac1{(j+1)[\log(e+j)]^\alpha}.
\]

The integral test gives three regimes:

\[
\sum_{j<K}q_j^{-1}
\asymp
\begin{cases}
(\log K)^{1-\alpha}, & \alpha<1,\\[3pt]
\log\log K, & \alpha=1,\\[3pt]
1, & \alpha>1.
\end{cases}
\]

Consequently the corresponding optimal anchored energy behaves as

\[
\boxed{
\inf \mathcal E_q
\asymp
\begin{cases}
(\log K)^{-(1-\alpha)}, & \alpha<1,\\[3pt]
(\log\log K)^{-1}, & \alpha=1,\\[3pt]
1, & \alpha>1.
\end{cases}
}
\]

So a logarithmic correction **strictly stronger than one power in the squared band weight** is already enough for rank-uniform coercivity, whereas the exact `alpha=1` endpoint still leaks, now only as `1/log log K`.

This formulation is useful because it identifies the property that matters independently of any particular Sobolev notation: the shell weights must have summable reciprocals.

---

## 6. What this does—and does not—supply for Nyman–Beurling

`NB-269` left two qualitatively different possibilities for recovering a destination-side obstruction: an additional invariant that charges concentration, or genuinely off-diagonal Hardy/Nyman structure. The present calculation completely classifies the first possibility **within the resolved full-line band-diagonal class**.

If the exact destination theory can furnish a positive quadratic quantity whose resolved-shell weights satisfy

\[
\sum_jq_j^{-1}<\infty,
\]

then the Euler anchor alone forces an order-one cost, regardless of how the coefficients are distributed across arbitrarily many resolved carriers. A Sobolev control with any fixed `s>1/2`, or the logarithmically refined critical weight above with `alpha>1`, would be sufficient.

Conversely, any proposed diagonal bridge with nonsummable reciprocal weights is defeated by the explicit optimizer

\[
c_j\propto q_j^{-1}.
\]

This is stronger than producing one counterexample for one norm: it gives the exact adversarial coefficient vector for every leaking diagonal weight.

What the finding does **not** prove is that the Nyman–Beurling approximation problem controls such a stronger norm. The canonical Hardy boundary norm is the unweighted case `s=0`, precisely the regime already shown by `NB-269` to leak. Introducing `H^s`, a logarithmic multiplier, or any other shell weight would require an independent theorem tying that quantity to the actual Nyman distance or to an exact invariant of the admissible approximants.

Nor does the theorem classify quadratic forms that are genuinely off-diagonal in the resolved shell basis. Such a form may restore coercivity even when every diagonal weight separately lies below the reciprocal-summability threshold. That remains a distinct route.

---

## 7. Adversarial audit

Several apparent upgrades are deliberately excluded from the conclusion.

First, the two-sided estimate `q_{j,s} asymp (1+j)^(2s)` uses the **matched packet model** from `NB-269`, where every resolved shell amplitude is uniformly bounded above and below. It is not asserted for the actual zeta-zero configuration, where channel cancellation could make an individual packet amplitude small. The abstract reciprocal-weight theorem itself, however, is exact for any prescribed positive `q_j`.

Second, all norms here are full-line in the normalized center variable. A hard observation window multiplies in physical space and hence convolves neighboring frequency bands; the resulting finite-window Gram need not remain shell-diagonal. The criterion therefore cannot be transferred unchanged to a local window.

Third, the endpoint counter-control is positive. Its failure is not caused by oscillating signs, superoscillation, or coefficient blowup. This matters because it rules out repairing the critical endpoint merely by prohibiting signed carrier cancellation.

Fourth, the result is a method boundary, not a zero theorem. The shallow packet remains the same matched compatibility control used in the preceding findings; no claim is made that the zeros of `zeta` realize that packet, and no RH implication is inferred.

Finally, the `s>1/2` transition itself is compatible with standard one-dimensional Sobolev theory and is not claimed as a new functional-analytic threshold. The line-specific content is the exact reduction of the resolved `NB-269` Hardy-projected packet to reciprocal shell-weight summability, including the sharp `1/K`, `1/log K`, and logarithmically refined rank laws.

---

## 8. Prior-art and source ledger

**Load-bearing internal input:** `NB-269` supplies the exact disjoint-band Hardy projection, the resolved shell representation, and the uniform matched-packet channel bounds used to identify `q_{j,s}`.

**Existing Nyman boundary:** `SOURCES.md` already records Gallardo-Gutiérrez and Seco (2025) on Nyman–Beurling approximation in weighted Dirichlet spaces. That literature confirms that stronger weighted function spaces are meaningful in neighboring Nyman questions, but it does not provide the resolved-shell reciprocal-summability criterion proved here and is not used in the derivation.

**Fresh search boundary:** generic Sobolev/Hardy-Sobolev literature recovers the familiar fact that one-dimensional point evaluation becomes bounded above the half-derivative threshold. This is background consistency only. No external theorem is load-bearing: the exact criterion and all rank asymptotics follow from the `NB-269` band decomposition plus weighted Cauchy–Schwarz and elementary series estimates. Therefore no new durable source dependency is added to `SOURCES.md`.

---

## 9. Next discriminating question

The diagonal destination route is now sharp enough that another arbitrary weight experiment would mostly restate the same theorem. The useful next question is structural:

> **Does the exact Nyman/Hardy problem control any resolved-shell quadratic quantity with reciprocal-summable weights, or must all missing coercivity come from genuinely off-diagonal structure?**

A concrete first test is to derive the exact destination Gram form for the admissible Nyman object after the `NB-269` projection and ask whether its high-shell part dominates either

\[
\sum_j (j+1)^{1+\varepsilon}|c_j|^2
\]

for some fixed `epsilon>0`, or a critical logarithmic weight

\[
\sum_j (j+1)[\log(e+j)]^{1+\varepsilon}|c_j|^2.
\]

If no such domination can hold, then the present theorem rules out the entire diagonal-weight repair and focuses the line on off-diagonal arithmetic/Hardy coupling. If one does hold for an exact Nyman invariant, it supplies precisely the rank-uniform bridge that `NB-269` showed the ordinary Hardy norm lacks.

---

## Conclusion

The narrow `NB-269` center spike is not merely invisible to ordinary `L^2`; there is an exact quantitative threshold for every resolved-shell **diagonal** quadratic attempt to see it. Under the Euler anchor, the minimum energy is the reciprocal of `sum_j 1/q_j`. Rank-uniform coercivity is therefore equivalent to reciprocal summability of the shell weights.

For Sobolev weights this puts the sharp boundary at one half derivative: `s<1/2` leaks polynomially, `s=1/2` still leaks as `1/log K`, and `s>1/2` is uniformly coercive. The critical endpoint itself can be sharpened to an exact logarithmic threshold `alpha>1`.

This does not solve the Nyman–Beurling problem; it identifies exactly what a **diagonal destination invariant would have to provide**. If the real Nyman geometry does not supply that much shell growth, then the only remaining way for the projected Ford obstruction to survive is genuinely non-diagonal.