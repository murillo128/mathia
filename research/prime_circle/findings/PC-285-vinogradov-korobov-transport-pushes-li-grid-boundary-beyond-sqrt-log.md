# PC-285 — Vinogradov–Korobov transport pushes the Li-grid boundary beyond sqrt-log

**Status:** `LITERATURE-TRANSFER` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the one-profile source-transport frontier in PC-277/PC-281/PC-284.

PC-277, PC-281, and PC-284 deliberately use the classical de la Vallée-Poussin-scale prime-number-theorem remainder

\[
\pi(x)-\operatorname{Li}(x)
\ll x\exp(-c\sqrt{\log x}),
\]

and consequently record `sqrt(log q)` as the exponent scale up to which the Prime-Circle source can be transported to the denominator-`q` Li-grid control. That scale is **not intrinsic to the Prime-Circle geometry**. The stronger unconditional Korobov–Vinogradov prime-number-theorem estimate is

\[
\boxed{
\pi(x)-\operatorname{Li}(x)
\ll
x\exp\!\left(
-c\,V(x)
\right),
\qquad
V(x):=
\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}},
}
\tag{1}
\]

for some absolute `c>0`. Re-running the already-persisted transport arguments with (1) moves all three Li-grid no-go boundaries from `sqrt(log q)` to the strictly larger scale `V(q)`.

In particular, for the normalized prime source `nu_q` and the denominator-`q` Li-grid control `\widetilde\lambda_q` of PC-277,

\[
\boxed{
W_1(\nu_q,\widetilde\lambda_q)
\ll
(\log q)e^{-cV(q)}+\frac{\log q}{q}.
}
\tag{2}
\]

After this substitution:

- the normalized scalar near-resonance law of PC-277 is Li-grid reproducible whenever `log B=o(V(q))`;
- the complete normalized singular spectrum of every regular PC-281 profile is Li-grid reproducible whenever `log(BL_q)=o(V(q))` (with the same amplitude condition already present there); and
- the **exact selector-subtracted boundary logarithm** of PC-284 has Li-grid-reproducible normalized singular-spectrum law whenever

\[
\boxed{
\log B=o\!\left(
\frac{(\log q)^{3/5}}{(\log\log q)^{1/5}}
\right).
}
\tag{3}
\]

Thus the currently recorded `log B\asymp\sqrt{\log q}` window is not yet a genuine rational-microscopic frontier. It lies inside a larger classical source-transport regime. Any one-profile order-one discrepancy appearing there can still be reproduced or excluded using unconditional classical prime-distribution information alone.

## 1. The stronger source transport is a black-box replacement

PC-277 derives its source estimate by Stieltjes partial summation against `\pi(x)-\operatorname{Li}(x)`, splitting away the small initial interval and normalizing by `\pi(q)\asymp q/\log q`. Nothing in that proof uses the special square-root shape of the de la Vallée-Poussin exponent.

Using (1), the same argument gives, for every bounded Lipschitz test `g`, after decreasing `c` harmlessly to make the estimate uniform on `[q^{1/2},q]`,

\[
\left|
\int g\,d\nu_q-
\int g\,d\lambda_q
\right|
\ll
(\|g\|_\infty+\operatorname{Lip}(g))
(\log q)e^{-cV(q)}
+
\|g\|_\infty\frac{\log q}{q}.
\tag{4}
\]

The nearest denominator-`q` grid projection still contributes only `O(1/q)`. Kantorovich duality therefore gives (2). No new Prime-Circle estimate enters: this is exactly the PC-277 source argument with the stronger standard PNT remainder inserted at its sole analytic-number-theory input.

Because

\[
\frac{V(q)}{\sqrt{\log q}}
=
\frac{(\log q)^{1/10}}{(\log\log q)^{1/5}}
\longrightarrow\infty,
\tag{5}
\]

this is an asymptotically strict enlargement of the transport regime, not a change of constants inside the old one.

## 2. Consequence for the scalar moving-bandwidth law

The deterministic part of PC-277 is unchanged. Its normalized scalar observable

\[
X_B=(B+1)^2D_B
\]

has source Lipschitz constant at most `B(B+1)^2`. Combining that bound with (2) gives

\[
\boxed{
W_1(\rho^{prime}_{q,B},\rho^{Li-grid}_{q,B})
\ll
B(B+1)^2
\left(
(\log q)e^{-cV(q)}+\frac{\log q}{q}
\right)
+
\frac{\log q}{q}.
}
\tag{6}
\]

Hence (6) tends to zero for every `log B=o(V(q))`. More quantitatively, because the polynomial logarithmic factors are negligible compared with `e^{cV(q)}`, there exists a fixed `kappa>0` such that the same conclusion holds for `B<=exp(kappa V(q))`; one may take any sufficiently small `kappa<c/3` after the harmless constant reductions in (4).

The exact denominator resonance from PC-277 remains unchanged:

\[
(B+1)^2>q
\quad\Longrightarrow\quad
D_B=0
\]

for every denominator-`q` source pair. PC-285 does not bridge the remaining gap to that `B\asymp q^{1/2}` scale. It only shows that the lower endpoint of the unresolved window was previously set by a deliberately nonoptimal classical PNT input.

## 3. Consequence for regular whole-spectrum finite sections

PC-281 proves the deterministic whole-spectrum bound

\[
\|\Sigma_{q,B}^{F_q}(x,y)-\Sigma_{q,B}^{F_q}(x',y')\|_\infty
\le
B L_q\bigl(d(x,x')+d(y,y')\bigr).
\]

Using (2) in place of the older source estimate gives

\[
\boxed{
W_1^{(\ell^\infty)}
(\rho^{prime,spec}_{q,B,F_q},
 \rho^{Li,spec}_{q,B,F_q})
\ll
B L_q
\left(
(\log q)e^{-cV(q)}+\frac{\log q}{q}
\right)
+
A_q\frac{\log q}{q}.
}
\tag{7}
\]

Therefore every bounded-amplitude family with

\[
\log(BL_q)=o(V(q))
\tag{8}
\]

still has its **entire ordered normalized singular spectrum** reproduced by the non-prime Li-grid control. As in PC-281, this includes all corresponding uniformly regular anchored chord profiles; the improvement concerns only how quickly their finite window and regularity scale may grow.

## 4. Consequence for the exact boundary logarithm

The singular boundary profile of PC-284 is the more important test because its microscopic anchor singularity prevents a direct application of PC-281. PC-284 proves, for every `1/q<=epsilon<=1/4`,

\[
\begin{aligned}
W_1^{(\ell^\infty)}
(\rho^{prime,log}_{q,B},\rho^{Li,log}_{q,B})
\ll{}&
\sqrt\varepsilon\,(\log q)^{3/2}\\
&+\frac{B\log q}{\varepsilon}
W_1(\nu_q,\widetilde\lambda_q)
+\frac{(\log q)^2}{q}.
\end{aligned}
\tag{9}
\]

Substituting (2) gives the sharpened bound

\[
\boxed{
\begin{aligned}
W_1^{(\ell^\infty)}
(\rho^{prime,log}_{q,B},\rho^{Li,log}_{q,B})
\ll{}&
\sqrt\varepsilon\,(\log q)^{3/2}\\
&+\frac{B\log q}{\varepsilon}
\left(
(\log q)e^{-cV(q)}+\frac{\log q}{q}
\right)
+\frac{(\log q)^2}{q}.
\end{aligned}
}
\tag{10}
\]

Choose, for example,

\[
\varepsilon_q=\exp\!\left(-\frac c4 V(q)\right).
\tag{11}
\]

Then the clipping term tends to zero exponentially on the `V(q)` scale. The PNT part of the transport term is

\[
B(\log q)^2
\exp\!\left(-\frac{3c}{4}V(q)\right),
\]

while the denominator-mesh part is

\[
\frac{B(\log q)^2}{q}
\exp\!\left(\frac c4V(q)\right).
\]

Both vanish under (3), since `V(q)=o(\log q)`. This proves the boundary-log statement. Again one can replace the little-`o` condition by `B<=exp(kappa V(q))` for some fixed sufficiently small `kappa>0` depending only on the PNT constant.

This matters for the research frontier because PC-284 was the first finding to retain the exact boundary logarithmic singularity while controlling the **complete normalized singular-spectrum law**. The improved range therefore cannot be dismissed as a statement only about a smooth scalar statistic.

## 5. Prior-art and novelty audit

There is no new analytic-number-theory theorem here. The Korobov–Vinogradov estimate (1) is classical. A convenient modern exposition is Robert C. Vaughan, *The Prime Number Theorem*, Math 571 notes, Chapter 3 (2025), which states

\[
\pi(x)-\operatorname{li}(x)
\ll x\exp\!\left(-c(\log x)^{3/5}(\log\log x)^{-1/5}\right).
\]

The current literature goes further on the relation between zero-free regions and PNT error constants: Chiara Bellotti, **A new zero-density estimate for `zeta(s)` and the error term in the prime number theorem**, *Bulletin of the London Mathematical Society* 58 (2026), e70442, DOI `10.1112/blms.70442`, proves an essentially optimal PNT error transfer for the Korobov–Vinogradov zero-free-region profile. This strengthens the literature boundary but does not change the `V(x)` scale used above.

Targeted checks against current PNT-error literature therefore make the novelty classification unambiguous. Equation (1) is established classical theory; equations (2), (6), (7), and (10) are transfers through deterministic bounds already proved in PC-277/281/284. **No new zeta mechanism is being claimed.** The project-local mathematical delta is a frontier correction: the square-root-log threshold recorded by those findings is not the strongest unconditional classical control and must not be treated as the beginning of an intrinsically Prime-Circle regime.

## 6. What remains open

PC-285 does not make the one-profile branch interesting by itself; it makes its surviving region smaller. After this correction, a one-profile candidate must lie beyond the unconditional `V(q)` transport range, survive the exact denominator-`q` Li-grid control, and still avoid the universal exact-resonance collapse near `B\asymp q^{1/2}`.

The finding also does not address a **magnified prime-minus-Li residual**. Such a residual is exactly where explicit-formula/zero information may re-enter, but then the burden is to show that the Prime-Circle geometry supplies the magnification and topology rather than merely re-encoding a classical PNT error. Cross-level, cross-source, directional, or genuinely richer observables remain outside the theorem as already recorded by PC-277/281/284.

The corrected live boundary is therefore:

\[
\boxed{
\text{one-profile Li-grid reproducibility at least through }
\log B=o\!\left((\log q)^{3/5}(\log\log q)^{-1/5}\right),
}
\]

not merely through `log B=o(sqrt(log q))`. Any claimed order-one prime-specific effect below this stronger scale is a classical-source false positive unless it uses information not covered by the persisted transport hypotheses.