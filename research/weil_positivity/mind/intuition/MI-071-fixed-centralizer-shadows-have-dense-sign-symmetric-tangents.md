# MI-071 — Fixed centralizer shadows have dense sign-symmetric tangents

**Evidence level:** exact operator-algebraic tangent-density synthesis from [WP-399](../../findings/WP-399-fixed-critical-centralizer-shadows-have-strongly-dense-sign-symmetric-tangents.md), extending the unit-shadow local symmetry of [WP-398](../../findings/WP-398-critical-centralizer-quotient-positivity-is-order-trivial.md).

Let `M` be the critical factor, `N` its fixed-point centralizer, `E:M->N` the faithful expectation, and fix a bounded positive shadow `d in N_+` with support `p=s(d)`. The centered supported self-adjoint directions are

`K_d={k=k^*: E(k)=0, k=pkp}`.

A direction is an actual two-sided fixed-shadow tangent whenever it is order-bounded by the shadow: for some `C<infinity`,

`-C d <= k <= C d`.

Then `d+/-epsilon k` stays positive for sufficiently small `epsilon` and has the same expectation `d`. This already gives both signs on every order-bounded centered direction.

The crucial point is that lack of a uniform lower bound on `d` does not leave a normal first-order sign carrier. Let

`e_n=1_[1/n,infinity)(d)`

be the spectral cutoffs of the shadow. For every `k in K_d`, the compressions `k_n=e_n k e_n` are order-bounded by `d`, remain centered and supported, and converge strongly, hence ultraweakly, to `k`. Thus genuine two-sided positive fixed-shadow tangents are strongly and ultraweakly dense in the full centered supported direction space.

Consequently any normal real linear functional that is nonnegative on every positive fixed-shadow displacement must vanish on `K_d`. Replacing the scalar unit shadow of WP-398 by a nonconstant, source-forced bounded shadow does not by itself create a first-order Weil orientation. The support can be source-specific while the normal tangent geometry remains sign-symmetric.

The durable escape condition is therefore stronger than “keep the shadow instead of quotienting it.” A successful bounded construction needs an additional source-forced **joint relation** between the shadow and noncentral correlations that removes a proper set of tangent directions and survives spectral cutoff. Otherwise normal first-order positivity sees both signs densely.

**Boundary.** WP-399 concerns bounded positive fixed-shadow slices and normal linear readouts. It does not rule out extra correlation equations that define a genuinely smaller admissible tangent set, nonlinear/global invariants, singular or non-normal functionals, unbounded/domain-sensitive constructions, or finite--archimedean coupling. The conclusion is only that the fixed positive shadow and its support, by themselves, do not supply the missing first-order sign orientation.
