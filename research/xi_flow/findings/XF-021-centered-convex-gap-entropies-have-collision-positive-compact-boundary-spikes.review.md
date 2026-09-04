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
