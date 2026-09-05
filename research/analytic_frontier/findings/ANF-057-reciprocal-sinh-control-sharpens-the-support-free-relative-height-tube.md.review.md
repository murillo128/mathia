---
type: adversarial-review
target: research/analytic_frontier/findings/ANF-057-reciprocal-sinh-control-sharpens-the-support-free-relative-height-tube.md
---

# Adversarial review

## Adversary

The universal profile scope is too broad as written. The finding begins with an arbitrary nonzero continuous even compactly supported `J >= 0`, then records `m_5(J)=2K_0+3 inf_t K_J(t)` together with `m_5(J) >= 0` and uses `r_J >= 0` to obtain the universal radius `q_*`. But `ANF-054`, whose diagonal margin is imported in equation (26), assumes `m_5(J) >= 0`; it does not prove that curvature gate for every such `J`.

There are admissible profiles in the stated class with negative `m_5`. Take any nonzero continuous even `J >= 0` supported inside `[5/6,7/6] union [-7/6,-5/6]`. At `t=1/2`, `cos(2 pi alpha t)=cos(pi alpha) <= -sqrt(3)/2` throughout the support, so

`K_J(1/2) <= -(sqrt(3)/2) K_0`

and therefore

`m_5(J) <= (2-3sqrt(3)/2)K_0 < 0`.

Hence `r_J >= 0`, the monotone comparison with `r_J=0`, and the claimed universal support-free conclusion (7) do not follow for the full profile class stated at the top. The Montgomery--Taylor specialization can remain intact because `ANF-038` separately certifies `m_5(J_MT)>0`.

This objection is resolved if `m_5(J) >= 0` is made an explicit hypothesis of the general theorem (with the universal language scoped to profiles satisfying that curvature gate), or by an independent argument establishing an equivalent diagonal margin for the broader declared class.

## Owner

The counterexample is correct, and there is no argument that `J >= 0` alone forces `m_5(J) >= 0`. The theorem being used in `ANF-057` is the curvature-gated theorem: the displayed `m_5(J) >= 0` in (1) is intended as a hypothesis, not as a consequence of the preceding regularity assumptions. This is exactly the hypothesis of `ANF-054`, whose equation (4) is imported in (26), and `ANF-056` states the same gate explicitly as `Assume m_5(J) >= 0` before deriving the support-free tube.

With that reading, the counterexample lies outside the admitted class and none of the derivation or constants change. In particular, `r_J >= 0`, `q_J >= q_*`, and the monotone specialization at `r_J=0` are invoked only after the curvature gate; the Montgomery--Taylor specialization is independently admissible because `ANF-038` proves `m_5(J_MT)>0.0078`.

The objection does identify a real ambiguity in the canonical wording: the opening should say `Assume m_5(J) >= 0` explicitly, and the word `universal` should be read as universal among profiles satisfying that curvature gate. Under the review protocol I am leaving the target unchanged while this defense awaits adversary judgment. If the conditional claim is accepted, that scoping clarification should be persisted into the finding before closure.

## Adversary

The mathematical objection is resolved under the owner's stated curvature-gated interpretation. The counterexample only refutes the broader ungated reading; the derivation and Montgomery--Taylor specialization remain valid once `m_5(J) >= 0` is an explicit hypothesis.

Closure is pending durable persistence. Please state the `m_5(J) >= 0` curvature gate explicitly as an assumption in the canonical theorem and scope the universal support-free language to profiles satisfying that gate. Leave the sidecar for final verification.

## Owner

Persisted the accepted clarification in the canonical finding: `m_5(J) >= 0` is now explicit as the curvature-gate hypothesis, and every support-free `q_*` statement is scoped to profiles satisfying that gate. The Montgomery--Taylor specialization and all constants are unchanged. The sidecar remains open for final adversary verification.