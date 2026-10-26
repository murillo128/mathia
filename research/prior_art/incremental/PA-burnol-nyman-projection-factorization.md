---
id: PA-burnol-nyman-projection-factorization
type: prior-art
canonical_name: Burnol's Nyman projection and inner factorization
aliases:
  - Burnol projection theorem
  - Quantitative Nyman projection formula
kind: projection theorem
topics:
  - riemann-hypothesis
  - hardy-spaces
  - approximation
---

# Burnol's Nyman projection and inner factorization

## What it is

For the continuous Nyman space \(\mathcal N\subset L^2(0,1)\), the unitary Mellin transform identifies \(\mathcal N\) with \(BH^2(\Re s>1/2)\). Here \(B\) is the Blaschke product of zeta zeros strictly right of the critical line, with multiplicities, normalized by \(b=B(1)>0\). Burnol proves

\[
\mathcal M(P_{\mathcal N}1)(s)=bB(s)/s,\qquad
\|P_{\mathcal N}1\|=b=\prod_{\Re\rho>1/2}|(1-\rho)/\rho|^{m_\rho}.
\]

The inner factor of \((s-1)\zeta(s)/s^2\) is exactly \(B\), without a singular or exponential factor.

## Relation to RH / Mathia research

[[research/nyman_beurling/findings/NB-354-finite-seed-real-dilation-spaces-have-an-exact-target-loss-classification|NB-354]] uses this unconditional projection. [[research/nyman_beurling/findings/NB-371-critical-line-zeros-force-unbounded-finite-dilation-synthesis-cost|NB-371]] retains it when pricing generator coefficients.

## Known scope and limits

The squared target distance is \(1-b^2\); its vanishing is equivalent to RH. This gives neither finite-generator rates nor coefficient bounds. Critical-line zeros are not additional inner factors. Burnol's separate [cutoff theorem, Theorem 1.3](https://arxiv.org/pdf/math/0103058), prices restricted dilation range, not NB-371's absolute coefficient budget.

## Related prior art

- [[research/prior_art/nyman-beurling-criterion|Nyman–Beurling criterion]] — quantitatively refined by this projection formula; the closure criterion and unconditional projection are distinct objects.

## Evidence and provenance

- Jean-François Burnol, *A note on Nyman's equivalent formulation of the Riemann Hypothesis*, [arXiv:math/9910055v3](https://arxiv.org/pdf/math/9910055v3), Theorem 1.2, §2, equation (2.3), and Lemma 2.4.
- Trigger: `research/nyman_beurling/findings/NB-371-critical-line-zeros-force-unbounded-finite-dilation-synthesis-cost.md`, §1 and prior-art comparison; projection normalization checked against NB-354 above.
