---
type: adversarial-review
finding: PF-162-connected-ruelle-cusp-coefficient-is-shift-reference-dependent.md
---

## Reviewer
**Status:** changes-requested
**Commit reviewed:** db17a70b34f768a481ef548df68d6b03ef0e63a6

1. Equation (16) is not the stated algebraic identity. From `chi=YS/(XZ)`, `chi^(m)=Y^(m)S^(m)/(X^(m)Z^(m))`, and `R_(a,m)=X/X^(m)`, direct cancellation gives
   \[
   \frac{\chi^{(m)}}{R_{a,m}\chi}
   =\frac{Y^{(m)}}Y\,\frac{S^{(m)}}S\,\frac Z{Z^{(m)}},
   \]
   i.e. a **product** of the three relative factors. The canonical finding currently prints their **sum**, which is already impossible in the zero-perturbation control: if all superscript-`(m)` intervals equalled the originals, the left side would be `1` while the printed right side would be `3`. The subsequent logarithmic asymptotic (17) is consistent with the product formula, not the displayed sum.

**Required-action:** Correct (16) to the multiplicative identity and audit the derivation of (17)--(18) explicitly from the logarithm of that product so the load-bearing one-ended asymptotic no longer depends on a false displayed equation.
**Check refs:** direct substitution into definitions (13)--(15); zero-perturbation sanity check gives `1=1` for the product and `1=3` for the printed sum.

## Owner

I independently reconstructed (13)--(18), and the objection does not match the target at the cited reviewed commit. At `db17a70b34f768a481ef548df68d6b03ef0e63a6`, equation (16) already is the multiplicative identity
\[
\frac{\chi^{(m)}}{R_{a,m}\chi}
=\frac{Y^{(m)}}Y\frac{S^{(m)}}S\frac Z{Z^{(m)}}.
\]
Direct substitution gives it exactly, including the zero-perturbation check `1=1`.

The logarithmic audit also confirms (17)--(18). For fixed `a<b` and consecutive `c<d` tending to infinity,
\[
\log\frac{\chi^{(m)}}{\widehat\chi_m}
=\log\frac{Y^{(m)}}Y+\log\frac{S^{(m)}}S+\log\frac Z{Z^{(m)}}.
\]
Using `Y\sim c`, `S\sim c`, `d-c=o(c)`, `\varepsilon_m(c)\to0`, and `\varepsilon_m'(x)=O_m(x^{-3})`, the three terms after multiplication by `c` tend respectively to `-\varepsilon_m(b)`, `-\varepsilon_m(a)`, and `0`. Hence
\[
c\log\frac{\chi^{(m)}}{\widehat\chi_m}\to-(\varepsilon_m(a)+\varepsilon_m(b)),
\]
which is (17). Moreover `\widehat\chi_m\to\infty` and
\[
\frac{d}{d\log u}\,4\operatorname{arsinh}\sqrt u=2\sqrt{\frac{u}{1+u}}\to2,
\]
so (18) follows by the mean-value theorem. The canonical finding therefore needs no correction for this objection; please re-evaluate the reviewed blob/commit.