# MI-042 — Faithful exact-law UCP readouts are rigid, but scalar convergence does not control a thin moving tail

**Evidence level:** exact/classical-mechanism synthesis from [WP-329](../../findings/WP-329-deterministic-amalgamated-lifts-make-operator-valued-free-divisibility-universal-before-scalarization.md) through [WP-333](../../findings/WP-333-approximate-faithful-ucp-rigidity-is-nonuniform-at-mangoldt-cutoffs.md). Kadison--Schwarz, Stinespring dilation and multiplicative-domain theory are classical; the Mathia content is their source-readout boundary at expanding Mangoldt cutoffs.

The operator-valued route has two opposite failure modes. WP-329--WP-330 show that enriched variables can be universally positive/divisible while all source specificity sits only in an external scalar state or in a fluctuation sector annihilated by that state. WP-331--WP-332 show the opposite: if a faithful UCP readout preserves the exact second moment of the same self-adjoint source observable, the positive Kadison defect must vanish. The observable lies in the multiplicative domain, and the off-diagonal Stinespring block that could have carried hidden coupling of that observable is zero.

At a finite atomic cutoff the exact stability modulus is

`||D_R|| <= tau_R(D_R)/m_R`,

where `m_R` is the least output-state atom. Hence approximate scalar second-moment preservation implies approximate multiplicative-domain rigidity only at the **relative** scale `tau_R(D_R)=o(m_R)`. A sequence of faithful states need not be uniformly faithful, and the finite Mangoldt least mass decays at least exponentially along a fixed prime-power ray.

WP-333 makes this nonuniformity sharp in two stages. A least-atom split concentrates an order-one positive defect on a vanishing-mass atom, so scalar error tends to zero while operator defect does not. More importantly, the same phenomenon already exists **inside the exact Mangoldt support**. On three consecutive dyadic log points `y_R-h,y_R,y_R+h`, `h=log2`, define a Markov/UCP self-map that leaves every point fixed except that evaluation at `y_R` is replaced by the average of its two neighbors. For the coordinate observable `X_R`, barycentric symmetry gives `Psi_R(X_R)=X_R` pointwise, yet

`||Psi_R(X_R^2)-X_R^2|| = (log 2)^2`

and the associated Stinespring off-diagonal coupling has norm `log2` for every cutoff.

The modified atom has exponentially small weight `r_R`. Consequently the source law before and after the channel differs by total variation `r_R`, every fixed polynomial moment discrepancy tends to zero, and for every fixed `p>=1` the Wasserstein distance is at most `(log2) r_R^(1/p)`. Both scalar laws converge to the same full tilted Mangoldt source. Nevertheless `||Psi_R-id||=2`: weak scalarized convergence coexists with maximal map-level separation.

This strengthens the readout principle. **Exact faithful same-observable recovery is rigid at each fixed cutoff; asymptotic scalar-law recovery is not a substitute for uniform map control, even when the exact arithmetic support and nearest-neighbor prime-power geometry are preserved.** The moving thin tail can carry an order-one operator defect while becoming invisible to total variation, any fixed moment list and every fixed Wasserstein metric.

The support-preserving construction is still not arithmetic leverage. It is a martingale/barycentric move available on any suitable thin equally spaced tail. Arithmetic supplies a convenient intrinsic ray, but matched controls can reproduce the mechanism. A positive Weil route therefore cannot claim source selectivity merely because the hidden coupling sits on prime-power support.

A surviving enriched route has to change one of the load-bearing conditions: prove error relative to the vanishing faithfulness modulus, obtain a stronger map/operator topology, use a different observable whose relevant mixed data are not forced into the same multiplicative-domain theorem, or make the moving coupling source-forced and show that the finite-plus-archimedean destination assigns it a sign unavailable to matched controls.

**Boundary.** The exact rigidity concerns the same self-adjoint observable whose compressed image preserves its second moment under a faithful output state. The quantitative modulus is exact for finite atomic states. WP-333 does not trivialize the whole dilation algebra, rule out couplings through other operators, or establish Weil positivity. It shows that support fidelity and scalar-law convergence alone are far too weak to globalize the finite-cutoff no-go.
