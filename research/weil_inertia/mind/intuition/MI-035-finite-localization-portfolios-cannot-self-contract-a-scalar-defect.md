# MI-035 — Scalar localization self-bootstrap has a sharp recurrence-complexity threshold

**Evidence level:** exact synthesis from [WI-315](../../findings/WI-315-nested-weil-windows-make-vanishing-cap-diagonals-inertia-complete.md), [WI-316](../../findings/WI-316-capped-comparison-bottoms-converge-to-global-weil-floor.md), [WI-317](../../findings/WI-317-finite-localization-portfolios-cannot-contract-scalar-defect.md), [WI-318](../../findings/WI-318-bounded-h1-adaptive-localizers-cannot-contract-scalar-defect.md), and [WI-319](../../findings/WI-319-recurrence-obstruction-has-a-sharp-t2-over-logt-complexity-threshold.md).

Once the capped comparison is reduced to a fixed nonzero scalar defect, source-exact localization does not automatically provide a bootstrap. Suppose an exact localization identity writes the global form as localized source terms plus an explicit error, and the only estimate supplied for every localized term is the same scalar lower bound `Q(h)>=-c||h||^2`. To improve the defect uniformly to `c-kappa`, the localization error would have to contribute a uniformly negative amount on every test vector after choosing a member of the portfolio.

WI-317 rules this out for every fixed finite portfolio of admissible smooth localizers at fixed aperture. High-frequency modulations preserve the scalar Rayleigh geometry while making the finitely many active prime-power phases simultaneously recurrent. Along a common weakly-null sequence, every active source error can be made nonnegative; in the prime-free regime the defects vanish instead. Thus even a best-after-seeing-`f` finite portfolio cannot force the negative correction needed for a uniform scalar contraction.

WI-318 shows that finiteness was not the essential resource limit for the unit-window architecture. Let an arbitrary finite or infinite family of normalized smooth multiwindow localizers have uniformly bounded total derivative energy. The `H^1` budget gives uniform Riemann--Lebesgue decay for the continuous localization error on high-frequency modulations. Independently, unit support makes translation by `log 2` square-zero, so the Haagerup--de la Harpe numerical-radius bound gives a family-independent autocorrelation ceiling `R(log 2)<=1/2`. A single Kronecker recurrence sequence then makes the active prime-power phases simultaneously favorable and defeats the infimum over the entire adaptive family.

WI-319 identifies the actual complexity scale hidden by that qualitative statement. If

`M_t=sum_nu ||g'_(nu,t)||_2^2`

is the total derivative energy of the localizer chosen against carrier `t`, then the continuous defect obeys

`|C_t| <= C[(1+sqrt(M_t))/|t| + M_t log(2+|t|)/t^2]`.

Consequently `M_t=o(t^2/log|t|)` still makes the continuous error vanish on the common recurrence sequence. When `log 2<2L`, the arithmetic part retains a family-independent positive first-prime floor there, so any selector claiming a fixed contraction must satisfy

`M_(t_k) >= c t_k^2/log t_k`

along all sufficiently large recurrence carriers. The prime-free regime gives the same scale when a fixed contraction is demanded from the continuous term alone.

This lower scale is sharp **for the recurrence obstruction**. WI-319 constructs three real unit-window components consisting of one base window plus sine/cosine resonant copies with total resonant mass `c/log t`. Their derivative energy is `M_0+c t^2/log t`, while the singular archimedean kernel turns that vanishing resonant mass into a logarithmic amplification and hence an order-one limit `C_t->-c/2`. Along the same prime-phase recurrence sequence the arithmetic defect returns to a fixed base-profile value, so sufficiently large `c` makes the very witness that defeated every subcritical family acquire negative total source defect.

The correct conclusion is therefore stronger and narrower than “spectral noncompactness is necessary.” **Below `t^2/log t`, the common recurrence witness still forbids scalar self-contraction; at the `t^2/log t` scale, that witness is quantitatively exhausted.** Crossing the threshold does not prove a successful bootstrap. It only shows that a new obstruction—or a positive contraction theorem—must now control the resonances created by an almost-quadratic frequency-second-moment budget on all test vectors.

This clarifies the information accounting. Portfolio cardinality, adaptivity, localization frequency budget and information content of the estimate fed into each piece are distinct resources. A countably infinite family with subcritical `M_t` remains one ineffective scalar channel for this purpose. A critical-scale resonant family changes the analytic resource class enough to evade the old falsifier, but it still imports no new arithmetic information: its new leverage comes from resonating with the singular continuous kernel.

The clean alternatives remain those not reducible to recycling the same scalar premise: a stronger localized arithmetic theorem, prime/mode-dependent data, vector- or matrix-valued state retained between pieces, different support geometry, or a direct sign/coercivity mechanism for the exact comparison form.

**Boundary.** The obstruction and the `t^2/log t` threshold are exact for the source-exact **unit-window** scalar-feedback architecture at fixed aperture and for the high-carrier recurrence witness constructed in WI-317--WI-319. The threshold is necessary to defeat that witness, not a lower bound on every possible proof and not a sufficient condition for contraction. Non-unit support geometries, stronger local arithmetic inputs, non-scalar information, or a different explicit-formula decomposition remain outside the result.