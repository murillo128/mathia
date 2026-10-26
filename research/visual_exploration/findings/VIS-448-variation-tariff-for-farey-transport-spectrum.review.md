---
type: adversarial-review
target: research/visual_exploration/findings/VIS-448-variation-tariff-for-farey-transport-spectrum.md
---

# Adversarial review

## Adversary

**Target.** The second inequality in the boxed universal chain (1). Write
\[
B_q(v)=\frac{V(v)^2}{2NT(v)}
\sum_{m=q+1}^{N-1}\csc^2\!\left(\frac{\pi m}{2N}\right).
\]
The displayed statement asserts that this untruncated Abel-summation
majorant itself satisfies \(B_q(v)\le\min\{1,\mathcal R_N(v)/(2q)\}\).
The spectral fraction's upper bound one does not imply that bound for
\(B_q(v)\).

**Exact counterexample.** Take \(N=3\), \(v=(1,-1)\), and \(q=1\).
With the prescribed zero endpoints,
\[
V(v)=4,\qquad T(v)=2,\qquad\mathcal R_3(v)=24.
\]
The orthonormal sine coefficients are \(\widehat v_1=0\) and
\(\widehat v_2=\sqrt2\), so \(1-F_{\le1}(v)=1\). But
\[
B_1(v)=\frac{16}{12}\csc^2(\pi/3)=\frac{16}{9}>1,
\qquad
\min\{1,\mathcal R_3(v)/2\}=1.
\]
Thus (1) includes the false comparison \(16/9\le1\), on an admissible
nonzero real vector with an admissible cutoff. No numerical approximation,
asymptotic issue, or source hypothesis is involved.

**Scope and resolution.** This refutes the stated bound on the intermediate
majorant, not the useful roughness estimate for the spectral tail.
The existing Abel calculation and Parseval establish
\[
1-F_{\le q}(v)
\le\min\{1,B_q(v)\}
\le\min\{1,\mathcal R_N(v)/(2q)\}.
\]
Equivalently, the two legitimate bounds on the tail can be stated
separately. Please resolve the extra universal inequality in the canonical
claim. The capped tail bound, the Farey transfer (2), and the necessary
roughness condition (3) still follow from the stored proof; this objection
does not refute those conclusions or demand a new analytic lemma.
