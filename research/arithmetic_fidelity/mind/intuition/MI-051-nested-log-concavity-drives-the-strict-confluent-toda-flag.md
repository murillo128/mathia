# MI-051 — Nested log-concavity drives the strict confluent Toda flag

**Evidence level:** exact/classical synthesis from [AF-403](../../findings/AF-403-complete-confluent-flags-globalize-strict-translation-total-positivity.md), [AF-404](../../findings/AF-404-confluent-hankel-toda-recursion-reduces-strict-flags-to-nested-log-concavity.md), [AF-405](../../findings/AF-405-full-euler-log-is-strictly-sign-regular-through-order-four.md), and [AF-408](../../findings/AF-408-order-five-euler-failure-is-confined-to-compact-log-scale.md). The determinant identity and ECT globalization are classical; the Mathia content is the reduction and exact placement of the current finite-order Euler-fidelity frontier.

For a smooth positive translation profile `f`, write

`H_m(t)=(-1)^(m(m-1)/2) det(f^(i+j)(t))_(i,j=0)^(m-1)`.

AF-403 shows that positivity of the complete flag `H_1,...,H_r` globalizes to strict total positivity through order `r`. AF-404 identifies the internal recursion of that flag:

`H_(m+1) H_(m-1) = -H_m^2 (log H_m)''`.

Consequently, once `H_(m-1)>0` and `H_m>0`, the next certificate is positive exactly when `H_m` is strictly log-concave. The strict flag is therefore a nested curvature hierarchy rather than an unrelated list of higher derivative determinants.

The normalization makes the recursion easier to compare across profiles. Put `q=-(log f)''` and `R_m=H_m/f^m`. Then

`R_(m+1)R_(m-1)=R_m^2(mq-(log R_m)'')`.

AF-405 closes the order-four gate for the full Euler-log profile `f(t)=-log(1-exp(-e^t))`: `H_1,H_2,H_3,H_4` are strictly positive on the whole real line. Hence the associated translation kernel is strictly totally positive through order four, and a nonzero finite signed source with at most three ordered sign changes cannot annihilate four distinct positive real Euler samples. Since AF-217 already rules out total nonnegativity at all orders, the first possible failure is `m>=5`.

Because `R_3,R_4>0`, order five is equivalent to the single scalar curvature gate

`A_4(t)=4q(t)-(log R_4(t))'' > 0`.

AF-408 now localizes that gate sharply. For the same Euler-log profile,

`A_4(t)=(24/5)e^(2t)(1+o(1))` as `t->-infinity`,

and

`A_4(t)=4e^t(1+o(1))` as `t->+infinity`.

Thus `H_5` is automatically positive in both logarithmic tails. Any order-five failure must lie in one compact interior interval where several Euler harmonics interact at comparable size. The next exact task is therefore no longer an all-line asymptotic problem: decide `A_4>0` on that bounded remainder. If it holds there, strict total positivity globalizes through order five and the first possible bad order moves to at least six.

The reusable fidelity lesson is that **source-class structure can make a nominally new coordinate recursively determined by the geometry of the retained certificate, while asymptotic regimes can remove most of the remaining sign problem before any global search is attempted**. Here each omitted next determinant is recovered from the current determinant, the previous one and one local curvature, and AF-408 shows that the only unresolved order-five information is compact-scale interaction rather than tail behavior.

**Boundary.** Strict positivity supplies no uniform determinant margin or conditioning estimate. AF-408 does not prove `A_4>0` on the compact interior, so the exact first bad order remains unsettled. The order-four/five analysis is source-agnostic and creates no rational-prime discriminator; arbitrary positive generator norms can obey the same finite-order theorem. AF-217 still forces eventual failure. Any RH-facing use must separately show that the arithmetic source belongs to the bounded-sign class needed by the finite-order certificate and that this structure is destination-selective.