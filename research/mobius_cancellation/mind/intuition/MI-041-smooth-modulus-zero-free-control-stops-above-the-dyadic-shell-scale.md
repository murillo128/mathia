# MI-041 — Prime-shell family energy, not primitive provenance, closes the natural reciprocal endpoint

**Evidence level:** literature-assisted source-specific resolution from [MC-319](../../findings/MC-319-smooth-modulus-zero-free-dyadic-resolution-barrier.md), the exact matched observation-category obstruction [MC-320](../../findings/MC-320-smooth-modulus-interval-cancellation-prime-shell-conductor-inflation.md), the decisive prime-family estimate in [MC-321](../../findings/MC-321-prime-halasz-montgomery-closes-natural-endpoint-family.md), and the energy/horizon sharpening [MC-322](../../findings/MC-322-prime-shell-bias-energy-cap-extends-modulus-horizon.md).

MC-319 shows that the natural endpoint source forces a smooth common modulus with strong collective zero-free control, but the known Rodosskii conversion operates on intervals much broader than the one-dyadic-shell signal consumed by the endpoint. MC-320 then proves that stronger **ordinary integer-interval cancellation** still targets the wrong observable: an imprimitive conductor-`4` character can have tiny interval sums while remaining maximally biased on the selected prime shell.

MC-321 identifies the missing theorem more directly than the primitive-conductor route suggested by that control. In the exact reciprocal endpoint there are distinct characters, all viewed modulo one controlled common modulus, and each is biased on the same dyadic prime shell. The prime Halász--Montgomery estimate of Puchta, in the form used by Klurman--Mangerel--Teräväinen, bounds the total squared correlation of a family of distinct characters against arbitrary coefficients supported on primes. Choosing those coefficients to be the exact endpoint shell turns simultaneous biases into an energy lower bound that contradicts the mean-square estimate.

MC-322 makes the reusable statement quantitative. For a dense dyadic prime shell, one common modulus `q<=y^(3-delta)`, and any family `Xi` of distinct characters,

`E(Xi)=sum_(chi in Xi) beta_chi^2 <<_delta 1 + |Xi| y^(-delta/24) log y`.

Thus every subpolynomial family has bounded total shell-bias energy. More locally, once `tau^2` dominates `y^(-delta/24)log y`, the number of characters with `|beta_chi|>=tau` is `O_delta(tau^-2)`. MC-321's fixed-bias growing-family contradiction is one consequence; MC-322 shows that redistributing the same endpoint demand into many weaker biases is also constrained by a conservation-like `ell^2` budget.

The modulus threshold is likewise sharper. The earlier `q<=y^(8/3-delta)` range came from a lower moment choice; the `k=3` form of the same classical prime Halász--Montgomery machinery reaches every fixed power below `y^3`. The exact endpoint with `q<=4y^2` lies far inside this range.

So the missing resource was not generic “more cancellation” and not primitive conductor provenance by itself. It was **cancellation in the exact observation category, aggregated as family energy across the whole source-forced set**. Common-modulus smoothness and unweighted interval pseudorandomness can miss the endpoint, while a prime-supported family theorem sees it directly.

The reusable audit is: when a construction needs many source modes to be simultaneously exceptional on one thin population, do not test the modes only one at a time or on a broader ambient population. Write the demanded correlation vector, compute its `ell^2` energy, and look for a family-energy inequality whose coefficients localize to the exact destination set. Family multiplicity matters through the energy it forces, not merely through a count of exceptional characters.

**Boundary.** MC-321--MC-322 close the exact natural-scale reciprocal one-defect endpoint under their common-modulus, dense-prime-shell and family hypotheses up to every fixed cubic-minus-power modulus range. They do not prove Möbius cancellation and do not rule out variants beyond the cubic scale, without a controlled common modulus, with collectively tiny bias energy, or with materially different defect/observation geometry.
