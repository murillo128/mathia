# NB-277 — Abel damping that preserves Ford depth cannot soften the differentiated Möbius source

**Date:** 2026-09-22  
**Status:** `EXACT-DERIVED + FORD-SCALE-REGULARIZATION-BOUNDARY + DIFFERENTIATED-MOBIUS-SOURCE + MATCHED-CURRENT-AUDIT + SOURCE-SIDE + PRIOR-ART-AUDITED`.

`NB-276` identifies an exact but singular source bridge from the canonical reciprocal-zeta source to the Ford divisor current. Its finite legal ancestry uses

\[
P_{\epsilon,M}'(s)
=-\sum_{k\le M}
\mu(k)\log k\,k^{-\epsilon}k^{-s},
\]

and leaves two regularization parameters to understand quantitatively: the Abel shift `epsilon` and the truncation length `M`.

The Abel parameter cannot provide the missing Ford-scale regularization gain by itself. The closed infinite source

\[
P_\epsilon(s)=\frac1{\zeta(s+\epsilon)}
\]

moves the singular zero geometry horizontally by exactly `epsilon`. In the Ford depth coordinate `X(1-Re s)`, this is a translation by `X epsilon`. Hence preserving the divisor current at fixed Ford resolution forces

\[
X\epsilon\longrightarrow0.
\]

But in precisely that regime the coefficient damping is asymptotically invisible on the logarithmic shell `log k asymp X`:

\[
k^{-\epsilon}=e^{-\epsilon\log k}=1+o(1).
\]

So the Mellin-derivative tariff `log k asymp X` from `NB-276` survives unchanged. The same conclusion appears in the crude absolute truncation audit: once `X epsilon=o(1)`, the Abel weight does not improve the tail exponent at Ford scale.

This does **not** prove a lower bound for the actual Nyman `H^2` norm and does not rule out Möbius cancellation in the finite truncation. It removes one apparent escape route from the finite-regularization problem: within the canonical Abel family, one cannot simultaneously damp the differentiated source at carrier scale and preserve the Ford-depth location of the divisor current.

## 1. The epsilon-regularized current is exact and its Euler pole still cancels

Retain the canonical synthesis from `NB-276`,

\[
\mathcal N[P](s)
:=
\frac{\zeta(s)}s\bigl(P(s)-P(1)\bigr).
\tag{1}
\]

For `epsilon>0`, put

\[
P_\epsilon(s)
:=
\frac1{\zeta(s+\epsilon)}.
\tag{2}
\]

Then

\[
P_\epsilon'(s)
=-\frac{\zeta'(s+\epsilon)}{\zeta(s+\epsilon)^2},
\tag{3}
\]

and define the pole-cancelled synthesized current

\[
\mathcal C_\epsilon(s)
:=-s\,\mathcal N[P_\epsilon'](s).
\tag{4}
\]

Substitution into `(1)` gives the exact closed form

\[
\boxed{
\mathcal C_\epsilon(s)
=
\zeta(s)
\frac{\zeta'(s+\epsilon)}{\zeta(s+\epsilon)^2}
-
\zeta(s)
\frac{\zeta'(1+\epsilon)}{\zeta(1+\epsilon)^2}.
}
\tag{5}
\]

The second term is the canonical Euler-anchor correction. The bracket multiplying `zeta(s)` in `(5)` vanishes at `s=1`, so the pole of `zeta` at `1` is cancelled for every fixed `epsilon>0`, not only in the limit.

Using

\[
\frac1{\zeta(1+\epsilon)}
=\epsilon+O(\epsilon^2),
\qquad
\frac{\zeta'(1+\epsilon)}{\zeta(1+\epsilon)^2}
=-1+O(\epsilon),
\tag{6}
\]

and Taylor expansion away from zeta zeros, one obtains locally uniformly on compact zero-free sets,

\[
\mathcal C_\epsilon(s)
\longrightarrow
\frac{\zeta'}{\zeta}(s)+\zeta(s)
=:
\mathcal C_0(s).
\tag{7}
\]

Thus `(5)` is a genuine regularization of the `NB-276` current away from its divisor. The issue is what happens **at the Ford spatial resolution of that divisor**.

## 2. The Abel shift translates the singular geometry by `X epsilon`

Let `rho` be a zeta zero. The singular denominator in the first term of `(5)` is

\[
\zeta(s+\epsilon)^2.
\]

Hence its zero-generated singularity occurs at

\[
s=\rho-\epsilon,
\tag{8}
\]

rather than at `s=rho`. At the original zero, provided no exceptional shifted-zero collision occurs, the factor `zeta(s)` instead vanishes. Finite positive `epsilon` therefore does not preserve the pointwise meromorphic divisor of `mathcal C_0`; the correct current is recovered only in the singular limit `epsilon downarrow0`.

Now use the Ford depth coordinate from `NB-237`,

\[
d_X(s)
:=
X(1-\Re s)-\log J.
\tag{9}
\]

The displacement `(8)` is exactly

\[
\boxed{
 d_X(\rho-\epsilon)
 =d_X(\rho)+X\epsilon.
}
\tag{10}
\]

Thus the natural dimensionless regularization parameter is not `epsilon` itself but

\[
c_X:=X\epsilon.
\tag{11}
\]

A Ford test keeps its depth cutoff fixed while `X` grows. If `c_X` tends to a positive constant, the regularized singular geometry is displaced by an order-one amount in that fixed coordinate. If `c_X` diverges, it is displaced by a diverging Ford depth.

This immediately gives a representation-fidelity necessity. Translation by `c_X` converges to the identity on **every** smooth compactly supported depth test only if

\[
\boxed{
X\epsilon\to0.
}
\tag{12}
\]

The statement is deliberately about fidelity to the Ford current, not about an average over a specially chosen cutoff that might happen to be translation-insensitive. A single fixed cutoff can have accidental cancellations; a bridge that is meant to reproduce the divisor current at Ford resolution has to work for the local test class used by the first-order representation.

### Local zero calibration

The same scale can be seen without any distributional shorthand. Suppose locally

\[
\zeta(\rho+z)=z^m a(z),
\qquad
a(0)\ne0,
\tag{13}
\]

where `m=m(rho)`. Ignore only terms that are holomorphic at the zero and set

\[
s=\rho+\frac wX,
\qquad
\epsilon=\frac cX.
\tag{14}
\]

The singular first term in `(5)`, divided by the natural local size `X`, has the universal leading profile

\[
\boxed{
\frac1X
\zeta(s)
\frac{\zeta'(s+\epsilon)}{\zeta(s+\epsilon)^2}
\longrightarrow
m\frac{w^m}{(w+c)^{m+1}}.
}
\tag{15}
\]

At `c=0`, this is exactly

\[
\frac m w,
\tag{16}
\]

the local profile of `zeta'/zeta`. For every fixed `c ne 0`, `(15)` is a different function. In particular, finite Ford-scale displacement does not merely multiply the correct pole by a harmless scalar; it changes its local shape. For multiple zeros the finite-`epsilon` object can even have a higher-order pole at the shifted location before the singular limit collapses it back to the logarithmic derivative.

Equation `(15)` is a local calibration, not a uniform assertion about spacing or regular factors for all high zeta zeros. The exact depth displacement `(10)` does not require such a uniformity assumption.

## 3. Ford-depth fidelity makes the Abel weight invisible on the differentiated source shell

On the Euler half-plane the differentiated regularized source has the absolutely convergent Dirichlet series

\[
P_\epsilon'(s)
=-\sum_{k\ge2}
\mu(k)\log k\,k^{-\epsilon}k^{-s}.
\tag{17}
\]

The only coefficient-level gain supplied by `epsilon` is therefore

\[
k^{-\epsilon}
=e^{-\epsilon\log k}.
\tag{18}
\]

Consider any fixed logarithmic carrier annulus

\[
aX\le\log k\le bX,
\qquad
0<a<b<\infty.
\tag{19}
\]

Under the Ford-fidelity condition `(12)`,

\[
\sup_{aX\le\log k\le bX}
\left|k^{-\epsilon}-1\right|
\le
1-e^{-bX\epsilon}
\longrightarrow0.
\tag{20}
\]

Consequently, uniformly on `(19)`,

\[
\boxed{
-\mu(k)\log k\,k^{-\epsilon}
=
-(1+o(1))\mu(k)\log k.
}
\tag{21}
\]

The source differentiation tariff from `NB-276` therefore remains

\[
|\log k|\asymp X.
\tag{22}
\]

There are three clean regimes:

- If `X epsilon -> 0`, Ford depth is preserved but the shell damping tends to one.
- If `X epsilon -> c in (0,infinity)`, the shell receives only constant-factor damping (`e^{-c}` on `log k=X+o(X)`) while the divisor is biased by an order-one Ford depth.
- If `X epsilon -> infinity`, the Abel factor can strongly suppress the shell, but the regularized singular geometry is translated by a diverging Ford depth.

Thus no choice of `epsilon(X)` inside this family gives both asymptotically faithful Ford localization and asymptotically nontrivial suppression of the Mellin-derivative multiplier on the carrier shell.

This is a coefficient statement. It does **not** say that the `H^2` norm of a signed Möbius combination is the unsigned coefficient norm; cancellation can still lower the physical cost.

## 4. The crude truncation boundary from NB-276 is unchanged in the faithful regime

The same incompatibility appears in the absolute tail estimate. On

\[
\sigma_X
=1+\frac rX,
\qquad r>0,
\tag{23}
\]

the unsigned tail after Abel damping satisfies, with

\[
a_X:=\frac rX+\epsilon,
\tag{24}
\]

\[
\begin{aligned}
\sum_{k>M}
\frac{\log k}{k^{1+r/X+\epsilon}}
&\ll
\int_M^\infty
\frac{\log x}{x^{1+a_X}}\,dx\\
&=
M^{-a_X}
\left(
\frac{\log M}{a_X}
+
\frac1{a_X^2}
\right).
\end{aligned}
\tag{25}
\]

If the regularization preserves Ford depth, `X epsilon=o(1)`, then

\[
a_X
=
\frac{r+o(1)}X,
\tag{26}
\]

and `(25)` becomes

\[
\boxed{
M^{-(r+o(1))/X}
\left(
\frac{X\log M}{r+o(1)}
+
\frac{X^2}{(r+o(1))^2}
\right).
}
\tag{27}
\]

This is the same black-box scale as equation `(36)` of `NB-276`. In other words, the parameter `epsilon` does not improve the absolute truncation method in the regime where it remains a faithful Ford-current regularizer.

As in `NB-276`, `(27)` is **not** a necessity theorem for the true Möbius tail. It discards every sign of `mu(k)`. Its value is narrower: it shows that any improvement over the existing absolute boundary must come from arithmetic cancellation, not from tuning the Abel factor while keeping the Ford current fixed.

## 5. Re-centering the shifted current is not a free repair

One possible objection is to take `epsilon asymp 1/X`, accept the translation `(10)`, and move the Ford test back by the same amount. This changes the quantity being represented. The exact first-order Ford identity pairs a prescribed depth cutoff with the zero divisor of `zeta`; replacing it by a translated cutoff pairs a different depth layer.

To return from the translated layer to the original one, one must account for the divisor crossed between the two contours/depth slices. Those residues are precisely the object that the source bridge is supposed to reconstruct. Thus re-centering does not remove the cost; it moves it into an explicit current-difference term.

The same point appears algebraically in `(15)`: for `c ne 0`, one cannot turn

\[
m\frac{w^m}{(w+c)^{m+1}}
\]

into `m/w` merely by multiplying by a bounded scalar. A horizontal translation of the destination variable is an additional operator, not part of the legal canonical synthesis `(1)`, and its discrepancy at the zero divisor has to be paid separately.

This finding therefore closes only the **canonical Abel-shift** regularization route. It does not rule out a different source regularizer that preserves zero locations while controlling the derivative graph norm, nor does it rule out a representation that exploits additional arithmetic cancellation before continuation.

## 6. Prior-art boundary

Shifted zeta ratios are classical in the Nyman--Báez-Duarte literature. In particular, Jean-François Burnol, *On an analytic estimate in the theory of the Riemann Zeta function and a Theorem of Baez-Duarte* (Acta Cientifica Venezolana 54 (2003), 210--215; arXiv:math/0202166), proves under RH a uniform estimate for

\[
\frac{\zeta(s)}{\zeta(s+A)},
\qquad A\ge0,
\]

on the critical line and uses it in a complex-analytic proof of Báez-Duarte's strengthened criterion. Thus neither the use of a positive horizontal shift nor shifted reciprocal-zeta geometry is new here.

A fresh search also recovered the standard Báez-Duarte work on Möbius-based Nyman approximants and later expositions of those constructions. None of the located sources gives the specific scale-coupled statement proved above: after differentiating the canonical reciprocal-zeta source, the same shift that supplies coefficient damping translates the Ford divisor by `X epsilon`, and Ford-depth fidelity forces that damping to disappear on `log k asymp X`.

No external theorem is load-bearing in `(5)`--`(27)`; they follow from the canonical synthesis, the reciprocal-zeta identity, Taylor expansion, and an elementary integral. Burnol's paper is therefore a prior-art boundary rather than a dependency, so `SOURCES.md` does not need a new durable source entry for this finding.

## 7. Adversarial audit and next target

Several stronger readings would be incorrect.

First, `(12)` is a necessity for **uniform Ford-depth fidelity of this Abel family**, not a theorem that every useful approximation to the Nyman target must have `epsilon=o(1/X)`. A proof that deliberately changes the depth test and controls the resulting divisor correction could use another regime, but that correction is then part of the theorem and cannot be declared free.

Second, `(21)` is not an `H^2` lower bound. The signed Möbius vector can have cancellations that are invisible to coefficientwise magnitude. The finding only shows that the Abel factor does not itself reduce the differentiated coefficients on the live shell once the current is kept at the correct Ford depth.

Third, `(27)` is an upper bound obtained after discarding Möbius signs. It cannot be inverted into a lower bound on the necessary truncation length `M`.

Fourth, the local model `(15)` does not assume simplicity of zeta zeros; multiplicity `m` is retained. It is used only to expose the universal scaled distortion from a nonvanishing `X epsilon`, not to assert a uniform local factorization radius for all high zeros.

Subject to those limits, `NB-276`'s two-parameter finite-regularization problem has been reduced by one degree of freedom. For a Ford-faithful approximation one may now take

\[
\epsilon=o(1/X)
\tag{28}
\]

without expecting this parameter to pay any meaningful part of the source cost. The discriminating question is the **signed finite truncation**:

> With `epsilon=o(1/X)` fixed only as a convergence device, can the truncated differentiated Möbius source `P_{epsilon,M}'` reproduce the first-order Ford current in its carrier test with controlled Nyman `H^2` cost, using Möbius cancellation rather than absolute tail decay?

That is the remaining mechanism inside the canonical finite ancestry of `NB-276`. If the signed truncation can be controlled, it gives a genuine finite source-to-current bridge. If not, the singular derivative identity remains a diagnostic representation whose regularization cost cannot be hidden in Abel damping.

## Conclusion

`NB-276` showed that the Ford divisor current is already encoded in the canonical Nyman source, but through source differentiation and a singular continuation. The most immediate regularization, multiplying the differentiated Möbius coefficients by `k^{-epsilon}`, has an exact geometric price: it moves the zero-generated singular structure by `epsilon`, which is `X epsilon` at Ford depth scale.

Therefore **Ford fidelity and useful Abel damping are incompatible at the live carrier shell**. Requiring the depth error to vanish forces `X epsilon->0`, and then `k^{-epsilon}=1+o(1)` precisely where `log k asymp X`. The next calculation should no longer try to optimize `epsilon`; it should keep the Möbius signs and quantify the finite-`M` truncation directly in the Ford edge pairing and in the actual Nyman Hardy norm.