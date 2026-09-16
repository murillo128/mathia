# MI-041 — Prime-shell family energy, not primitive provenance, closes the natural reciprocal endpoint

**Evidence level:** literature-assisted source-specific resolution from [MC-319](../../findings/MC-319-smooth-modulus-zero-free-dyadic-resolution-barrier.md), the exact matched observation-category obstruction [MC-320](../../findings/MC-320-smooth-modulus-interval-cancellation-prime-shell-conductor-inflation.md), the decisive prime-family estimate in [MC-321](../../findings/MC-321-prime-halasz-montgomery-closes-natural-endpoint-family.md), the fixed-common-modulus energy/horizon sharpening [MC-322](../../findings/MC-322-prime-shell-bias-energy-cap-extends-modulus-horizon.md), and the varying-modulus quadratic-source saturation theorem [MC-323](../../findings/MC-323-varying-modulus-prime-halasz-montgomery-forces-quadratic-source-saturation.md).

MC-319 shows that the natural endpoint source forces a smooth common modulus with strong collective zero-free control, but the known Rodosskii conversion operates on intervals much broader than the one-dyadic-shell signal consumed by the endpoint. MC-320 then proves that stronger **ordinary integer-interval cancellation** still targets the wrong observable: an imprimitive conductor-`4` character can have tiny interval sums while remaining maximally biased on the selected prime shell.

MC-321 identifies the missing theorem more directly than the primitive-conductor route suggested by that control. In the exact reciprocal endpoint there are distinct characters, all viewed modulo one controlled common modulus, and each is biased on the same dyadic prime shell. The prime Halász--Montgomery estimate bounds the total squared correlation of a family of distinct characters against arbitrary coefficients supported on primes. Choosing those coefficients to be the exact endpoint shell turns simultaneous biases into an energy lower bound that contradicts the mean-square estimate.

MC-322 makes the fixed-common-modulus statement quantitative. For a dense dyadic prime shell, one common modulus `q<=y^(3-delta)`, and any family `Xi` of distinct characters,

`E(Xi)=sum_(chi in Xi) beta_chi^2 <<_delta 1 + |Xi| y^(-delta/24) log y`.

Thus every subpolynomial family has bounded total shell-bias energy. More locally, once `tau^2` dominates the error scale, the number of characters with `|beta_chi|>=tau` is `O_delta(tau^-2)`. The common-modulus theorem therefore reaches every fixed power below the cubic boundary.

MC-323 removes the most obvious remaining provenance escape. Schlage-Puchta's varying-modulus clause replaces the single modulus by `Q^2`; with cubefree individual moduli one may choose the Burgess parameter arbitrarily. Consequently, for every fixed `delta in (0,2)` and distinct characters with cubefree individual moduli `q_chi<=y^(2-delta)`, the same shell-energy shape holds:

`sum_(chi in Xi) |beta_chi|^2 <= C_delta(1+|Xi| y^(-c_delta) log y)`.

In particular a fixed nonzero shell bias can occur for only `O_delta(1)` such characters. The obstruction therefore does **not** require embedding the family into one common modulus throughout the whole fixed-subquadratic individual-conductor range.

For the reciprocal endpoint generators this has a source-cost consequence stronger than a family-count contradiction: all but `O_delta(1)` generator directions require primitive conductor above `y^(2-delta)`. In the natural `2R`-coordinate common source package, where every source prime is at most `y^(1/R)`, the common squarefree radical has the a priori ceiling `P<=y^2`; MC-323 forces

`P=y^(2-o(1))`,

and, for every fixed `eta>0`, all but `o(R)` source primes must lie above `y^((1-eta)/R)`. The package survives only by saturating essentially its entire quadratic logarithmic source budget.

So the reusable resource is more precise than “many characters” or “one common modulus.” It is **prime-supported family energy in the exact observation category, together with the conductor/source budget needed to sustain exceptional coordinates**. Common-modulus energy controls reach below the cubic scale; varying-modulus energy already forces near-quadratic individual conductors and quadratic package saturation. Losing a common embedding is therefore not by itself an escape.

The reusable audit is: when a construction needs many source modes to be simultaneously exceptional on one thin population, write the demanded correlation vector, compute its `ell^2` energy, and identify which conductor parameter the family theorem actually prices. Then compare the required exceptional conductors with the source package's total logarithmic capacity. A family can evade a common-modulus theorem only if the replacement provenance genuinely leaves the varying-modulus range or changes another load-bearing hypothesis.

**Boundary.** MC-321--MC-322 close the exact natural-scale reciprocal endpoint under a controlled common modulus through every fixed cubic-minus-power range. MC-323 removes the common-modulus hypothesis only for cubefree individual conductors through every fixed subquadratic range and converts the natural package to the saturation law `P=y^(2-o(1))`. These results do not prove Möbius cancellation and do not classify super/subtle quadratic-boundary conductors, noncubefree families without the same Burgess flexibility, collectively tiny shell-bias energy, sparse/non-dyadic populations, or materially different defect geometry.
