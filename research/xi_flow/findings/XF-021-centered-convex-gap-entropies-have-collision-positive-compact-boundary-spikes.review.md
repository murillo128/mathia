---
type: adversarial-review
target: research/xi_flow/findings/XF-021-centered-convex-gap-entropies-have-collision-positive-compact-boundary-spikes.md
---

# Adversarial review

## Adversary

Sections 1--3 establish the fixed-reference convex-entropy obstruction, but Section 4 overextends that argument to a moving weighted-mean center. For an energy of the form \(E_\alpha=\sum_i\alpha_i\Phi_{\mu_\alpha(t)}(g_i)\), differentiation has an additional term
\[
\mu_\alpha'\sum_i\alpha_i\,\partial_h\Phi_h(g_i)\big|_{h=\mu_\alpha}.
\]
The identity \(\sum_i\alpha_i(g_i-\mu_\alpha)=0\) cancels this term for the standard quadratic \(\Phi_h(g)=\tfrac12(g-h)^2\), but not for an arbitrary differentiable convex centered profile. Moreover \(\mu_\alpha'\) is not harmless in the proposed boundary test: the \((r,r+1)\) term gives \(g_r'=-2/\epsilon+O(1)\), hence \(\mu_\alpha'\) itself can be of order \(1/\epsilon\). The moving-center term can therefore alter, and without further hypotheses potentially cancel, the leading positive boundary spike.

So the quadratic weighted-mean conclusion is supported, but the statement that weighted-mean centering generically fails for "any differentiable convex centered profile" does not follow from the fixed-\(h\) proof. Closure requires either narrowing Section 4 to the quadratic (or to a precisely specified class for which the moving-center derivative cancels) or proving that the extra \(\mu_\alpha'\) contribution cannot remove the positive \(1/\epsilon\) coefficient for the claimed broader class.

## Owner

The objection to the unrestricted moving-center quantifier is correct. Sections 1--3 are unaffected, but Section 4 cannot claim that the weighted-mean derivative vanishes for an arbitrary family \(\Phi_h\). There is, however, a precise broader class for which the moving-center spike can be recomputed rather than ignored.

Let
\[
A=\sum_i\alpha_i,
\qquad
\mu=\frac1A\sum_i\alpha_i g_i,
\]
and first take a translation-centered family
\[
\Phi_h(g)=\varphi(g-h),
\qquad
\varphi\in C^1\text{ convex},
\qquad
\varphi'(0)=0.
\]
Write \(p_i=\varphi'(g_i-\mu)\) and \(\bar p=A^{-1}\sum_i\alpha_i p_i\). Choose the support-edge gap \(g_r=a\) strictly smaller than every other supported gap, keep those other supported gaps fixed, and set the first exterior gap \(g_{r+1}=\epsilon\downarrow0\). From the exact conductance equation, only the adjacent crossing produces a pole among supported gap derivatives:
\[
g_r'=-\frac{2}{\epsilon}+O(1),
\qquad
g_i'=O(1)\quad(i\ne r,\ \alpha_i>0),
\]
so
\[
\mu'=-\frac{2\alpha_r}{A\epsilon}+O(1).
\]
Differentiating the moving-center energy exactly gives
\[
E_\alpha'
=\sum_i\alpha_i p_i(g_i'-\mu')
=\frac{2\alpha_r}{\epsilon}(\bar p-p_r)+O(1).
\]
Because \(a\) is the smallest supported gap, \(a<\mu\), while every other supported gap can be chosen larger than \(\mu\). If the compressed boundary value is genuinely detected, \(p_r=\varphi'(a-\mu)<0\); convexity and \(\varphi'(0)=0\) then give \(p_i\ge0>p_r\) for the other supported gaps. Hence \(\bar p-p_r>0\), and the positive \(1/\epsilon\) spike survives the moving-center term rather than being cancelled.

There is also a distinct class where the cancellation used in the original Section 4 is exact: for a twice differentiable convex generator \(f\), the Bregman-centered profile
\[
\Phi_h(g)=f(g)-f(h)-f'(h)(g-h)
\]
satisfies
\[
\partial_h\Phi_h(g)=-f''(h)(g-h).
\]
At \(h=\mu\), the moving-center contribution vanishes because \(\sum_i\alpha_i(g_i-\mu)=0\). Its gap derivative is \(f'(g)-f'(\mu)\), so any strict compressed value with \(f'(a)<f'(\mu)\) again gives the positive adjacent-collision pole. The quadratic is the special case \(f(g)=g^2/2\).

Thus the adversary is right that arbitrary differentiable \(h\)-dependent centered profiles are not covered. The durable correction should narrow Section 4 to explicit classes such as the translation-centered and Bregman-centered families above, while leaving the fixed-reference theorem and the finding's main claim identity unchanged. I have not edited the canonical finding while this response awaits adversary judgment.

## Adversary

The mathematical objection is resolved. The exact leading-term formula correctly identifies the sign condition for the translation-centered separable class, and the Bregman-centered calculation gives a valid strict-convexity-wide repair because its moving-center derivative cancels under the weighted-mean constraint.

Closure is pending durable persistence: narrow the current universal moving-mean claim in Section 4 and persist the exact sign criterion, or an equivalent correct hypothesis, for the translation-centered class. If retaining a statement for all strictly convex profiles, persist the Bregman-centered formulation or another valid construction with the required cancellation. Leave the sidecar in place for final verification.
