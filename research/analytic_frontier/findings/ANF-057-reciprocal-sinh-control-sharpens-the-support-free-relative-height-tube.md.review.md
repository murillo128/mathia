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