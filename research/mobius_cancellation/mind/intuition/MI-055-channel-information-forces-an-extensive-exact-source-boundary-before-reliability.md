# MI-055 — Channel information forces an extensive exact source boundary and a nonvanishing privacy-loss budget

**Evidence level:** exact synthesis of MC-340 and [MC-349](../../findings/MC-349-destination-relative-edge-kl-reliability.md) through [MC-353](../../findings/MC-353-privacy-loss-tail-budget.md). The finite-source information/KL/privacy-loss implications are exact for the declared reciprocal source; the analytic upper bound for a concrete Möbius architecture remains open.

The transcript channel defines a canonical source quotient: two source states are equivalent exactly when they induce the same transcript law. MC-350--MC-351 show that the information required by bounded-energy nontrivial dephasing forces this quotient to have an extensive source-graph boundary and forces an `Omega(R)` aggregate symmetrized KL budget on that exact cut.

MC-352 converts reverse likelihood stability into an upper currency. For a neighboring source edge `e={x,x'}`, let `L_e=log(dP_x/dP_x')` and put `psi(u)=u tanh(u/2)`. The symmetrized edge divergence is bounded by the edge likelihood-ratio radius and hence cannot stay extensive if all neighboring transcript laws become uniformly likelihood-close.

MC-353 sharpens this from a worst-case radius to the **distribution of privacy loss itself**. Under the edge mixture law `M_e=(P_x+P_x')/2`,

`b_e = E_(M_e) psi(|L_e|)`

for the corresponding half-Jeffreys divergence. Averaging over the natural source graph therefore turns the compulsory KL tariff into a compulsory privacy-loss tariff. If bounded-energy nontrivial dephasing requires a positive asymptotic average of `b_e`, then for every cutoff `u` the mass of `psi(|L_e|)` above `u` must pay the part not already supplied below `u`.

Consequently, convergence of source-edge privacy loss to zero in probability is incompatible with the required dephasing whenever the family is uniformly integrable in this `psi` currency. A uniform `p>1` moment bound gives an explicit version: rare large-privacy-loss edges cannot carry the whole extensive Jeffreys budget once their probability tends to zero fast enough. The remaining escapes are now concrete—nonvanishing typical reverse contrast, loss of uniform integrability/moment control, or a rare tail whose magnitude is large enough to carry constant aggregate divergence.

The reusable lesson is that **information must be paid by reverse statistical distinguishability in the actual transcript law, not by forward smoothness of the encoding**. Exact quotient geometry identifies which neighboring source directions matter; aggregate KL says how much discrimination is compulsory; MC-353 says that this discrimination must appear either typically or in a quantitatively visible privacy-loss tail.

**Boundary.** No theorem yet bounds the privacy-loss distribution of a concrete Möbius/endpoint architecture from coefficient energy, analytic bandwidth, precision or regularity. MC-353 is a finite-source endpoint theorem and does not estimate `M(x)` or prove RH. The live bridge is now an analytic uniform-integrability/tail theorem for the induced source-edge transcript laws, or an honest demonstration that the architecture really can sustain the required heavy reverse-discrimination tail.