# MI-051 — Nested log-concavity drives the strict confluent Toda flag

**Evidence level:** exact/classical synthesis from [AF-403](../../findings/AF-403-complete-confluent-flags-globalize-strict-translation-total-positivity.md) and [AF-404](../../findings/AF-404-confluent-hankel-toda-recursion-reduces-strict-flags-to-nested-log-concavity.md). The determinant identity is classical Toda/Hankel mathematics; the Mathia content is the reduction of the active finite-order fidelity certificate.

For a smooth positive translation profile `f`, write

`H_m(t)=(-1)^(m(m-1)/2) det(f^(i+j)(t))_(i,j=0)^(m-1)`.

AF-403 shows that positivity of the complete flag `H_1,...,H_r` globalizes to strict total positivity through order `r`. AF-404 identifies the internal recursion of that flag:

`H_(m+1) H_(m-1) = -H_m^2 (log H_m)''`.

Consequently, once `H_(m-1)>0` and `H_m>0`, the next certificate is positive exactly when `H_m` is strictly log-concave. The strict flag is therefore a nested curvature hierarchy rather than an unrelated list of higher derivative determinants.

The normalization makes the recursion easier to compare across profiles. Put `q=-(log f)''` and `R_m=H_m/f^m`. Then

`R_(m+1)R_(m-1)=R_m^2(mq-(log R_m)'')`.

Thus every next-order test asks whether the current normalized certificate has curvature below the explicit background `mq`. For the full Euler-log profile, the known positivity of `q=R_2` and `R_3` reduces strict order four exactly to

`(log R_3)'' < 3q`.

This supplies a concrete failure locator. If the strict hierarchy breaks at finite order, the first breakdown occurs when one current Toda certificate loses the required log-concavity; arbitrary-node searches or independent determinant expansions are unnecessary at that stage. Conversely, proving one gate says nothing automatically about all later gates.

The reusable fidelity lesson is that **source-class structure can make a nominally new coordinate recursively determined by the geometry of the retained certificate**. Here the omitted next determinant is recovered from the current determinant, the previous one and one local curvature. That is a genuine reduction in the certificate representation, not a new arithmetic discriminator.

**Boundary.** The logarithmic formulation requires strict positivity and does not classify zero strata. The recursion supplies no uniform margin or conditioning estimate, no finite cutoff for all-order positivity, and no proof that the Euler-log order-four inequality holds. AF-217 still forces eventual failure of the all-order Euler-log hierarchy. Any RH-facing use must separately show that the arithmetic profile satisfies the needed finite Toda gate on the physically accessible source scale and that this positivity is destination-selective.