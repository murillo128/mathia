# MI-015 — Nonlinear post-processing after scalarization cannot create a new linear distribution

**Evidence level:** exact algebraic factorization for the Arthur/Maaß--Selberg height-profile setting through [WP-287](../../findings/WP-287-nonlinear-arthur-height-scalarizations-that-remain-distributions-collapse-to-linear-filters.md), building on the linear-height obstruction of WP-237. No claim is made about operator-level nonlinear constructions before scalarization or cone-only functionals lacking a linear extension.

Let `V` be the admissible test-function space and let

`Q: V -> P`, `Qg = (T -> Q_T(g))`

be the attainable scalar height-profile map. Every `Q_T` is a distribution, so `Q` is linear. Now allow an arbitrary rule `Phi:P->C`: it may be discontinuous, nonsmooth, nonlinear, defined by minimization, maximization, ratios, thresholds or any other post-processing.

If the resulting output

`R(g)=Phi(Qg)`

is required to be a **linear distribution in `g`**, then the apparent nonlinearity disappears on the only profiles the rule ever sees. For `u=Qg` and `v=Qh`, linearity of `R` gives `Phi(u+v)=Phi(u)+Phi(v)` and `Phi(lambda u)=lambda Phi(u)`. Hence `Phi` is linear on `im(Q)`.

For finitely many heights this is especially concrete. Any rule

`F(Q_(T1)(g),...,Q_(TN)(g))`

that is linear in `g` equals a fixed linear combination `sum_j a_j Q_(Tj)(g)` on the admissible test space. It therefore returns to the same linear-height class already audited: post hoc nonlinear processing has not recovered the internal decomposition of the common explicit-formula block into zero, finite-prime, archimedean and polar terms.

The reusable principle is an information-order gate: **nonlinearity applied after a linear compression cannot manufacture a new linear target that did not already factor through that compression linearly.** If the downstream theorem requires a linear functional, any genuine new mechanism must alter the information available before the scalar bottleneck, or add a new source variable rather than merely changing the combiner.

This also prevents a common category error around positivity. A quantity such as `min_T Q_T(g)`, `log Q_T(g)` or a nonlinear learned readout may be nonnegative on positive-type tests and still fail to be the Weil distribution. Positivity of a nonlinear statistic is not automatically Weil positivity. Either the statistic has an independently proved polarization/extension identifying it with the canonical form, or it belongs to a different problem.

The surviving space is therefore upstream. Operator-valued nonlinear constructions before taking the scalar trace, genuinely coupled automorphic channels, finite--archimedean interactions formed before the height profile is compressed, or cone-only constructions with a separate equivalence theorem are not covered by the factorization gate.

**Boundary.** The result is purely algebraic and says nothing about whether a nonlinear scalar statistic can prove useful inequalities. It rules out only the claim that arbitrary nonlinear post-processing of the same scalar profile yields a genuinely new Weil-type **linear distribution**. A successful construction that changes the source object before scalarization, or proves a separate cone-to-Weil equivalence, lies outside it.