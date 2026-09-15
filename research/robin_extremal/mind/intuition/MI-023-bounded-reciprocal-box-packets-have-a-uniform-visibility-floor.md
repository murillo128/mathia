# MI-023 — Fixed reciprocal-box packets have a cardinality-free visibility floor

**Evidence level:** exact reciprocal-box visibility theorem from [RE-135](../../findings/RE-135-fixed-reciprocal-box-packets-have-a-cardinality-free-visibility-floor.md), strengthening the bounded-cardinality compactness theorem [RE-134](../../findings/RE-134-bounded-reciprocal-box-packets-have-a-fixed-relative-visibility-floor.md)

For the attained finite-edge Robin/CA packet, fix a relative observation window and a fixed scaled reciprocal box around a target strict-subedge zero. RE-135 removes the cardinality hypothesis from RE-134: for **any finite nonempty multiset** `C_U` inside that box,

`sup_((1-kappa)U<=u<=U) |S_(C_U,K)(u)| >= c_0 #C_U |a_(rho_0,K)(U)|`,

with `c_0>0` depending only on the fixed box/window/strip parameters, not on `#C_U`.

The reason is stronger than bounded-term exponential-polynomial compactness. Inside a fixed `R/U` box the Robin coefficient ratios have one common orientation up to `O(U^-1)`. After dividing by `#C_U`, the local packet is the Fourier--Laplace transform

`F_mu(x)=int exp(lambda x) dmu(lambda)`

of an empirical **probability measure** on one fixed compact set, plus a uniform `O(U^-1)` error. Probability measures on that compact set are weakly compact, while `F_mu(0)=1`; no limiting transform can vanish on a real interval. A uniform complex `L^2` floor follows, and the fast target carrier transfers it to the real Robin packet.

This collapses the earlier concentration--compactness alternative. Growing occupancy inside a fixed scaled reciprocal box is not an escape mechanism. If the full packet hides at `o(M_K(U))` on a fixed-relative window, then for every fixed scaled radius `R` the complement of that box must supply order-`M_K(U)` cancellation. **Macroscopic hiding forces failure of reciprocal-scale tightness; scaled diameter, not local cardinality, is the unavoidable noncompact direction.**

The accepted growing-cluster control RE-133 is consistent with this sharpening. Its hiding packet has many atoms but also scaled vertical diameter tending to infinity, so no fixed reciprocal box contains the full cancelling cluster. RE-135 identifies that growing diameter as load-bearing and removes the need for a source-side bounded-occupancy theorem.

The next source theorem is therefore an exterior-tightness statement or a quantitative cost for escape as the scaled radius grows. If, along a hypothetical hiding sequence, the contribution outside some fixed `R/U` box were `o(M_K(U))`, the cardinality-free local floor would already give a contradiction.

**Boundary.** The result is local to a fixed scaled radius. The visibility constant may deteriorate as `R->infinity`, and no rate is proved for `R=R(U)->infinity`. It does not show that actual off-critical zeta zeros satisfy reciprocal-scale tightness, that such zeros exist, or that the nonattained edge and `Theta=1` branches behave the same way.