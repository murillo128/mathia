# MI-049 — Shrinking Euler spectral windows collapse to reciprocal-mass rank one

**Evidence level:** exact synthesis from [RE-190](../../findings/RE-190-shrinking-euler-sampling-windows-collapse-to-reciprocal-mass-rank-one.md). The statement concerns finite ordinary-prime multiplicity packets inside a fixed multiplicative selector shell and the natural weighted `ell^1(q^-1)` source norm; it is not a global uniqueness theorem for Euler products.

Let a signed prime packet be supported on `Ap<=q<=Bp` and sample its exact Euler discrepancy at

`s=1+tau/log p`,  `|tau|<=T_p`,  `T_p=o(log p)`.

After removing the common first-harmonic factor by multiplying by `e^tau`, RE-190 proves that the entire continuum of sampled values is operator-norm close to the single reciprocal-mass functional

`A_p = sum_q c_q/q`.

More precisely, with `V_p=sum_q |c_q|/q`,

`sup_|tau|<=T_p |G_p(tau)-A_p| <= C_(A,B) (T_p/log p + p^(-1+o(1))) V_p`.

Hence any arbitrarily dense sampling grid inside an `o(1)` spectral neighborhood of `s=1` has asymptotic rank one on a fixed multiplicative selector shell. Adding more nearby exact values creates more rows, but those rows become parallel at the natural source scale.

The mechanism is geometric rather than a Taylor-truncation artifact. Write `q=pe^alpha` with `alpha=O(1)`. The first harmonic distinguishes shell location only through `e^(-(s-1)alpha)`. An order-one distinction across the shell therefore requires `|s-1|=Theta(1)`. If the spectral window shrinks, relative shell weights differ only by `1+o(1)`; higher prime powers are smaller at the same source norm.

This complements the high-jet collapse of MI-048 without duplicating it. Very high normalized derivatives at the single boundary point converge toward **net multiplicity**; exact values throughout a shrinking neighborhood converge toward **reciprocal mass**. The two common modes coexist because extracting growing-order derivatives from nearly parallel nearby values is itself badly conditioned.

The reusable lesson is that **sampling density does not determine effective source rank; dual-window width relative to logarithmic source diameter does**. A continuum of exact observations can be asymptotically one-dimensional when the physical spectral window is too narrow to separate locations inside the source shell.

**Boundary.** Constant-distance spectral probes are outside the collapse, as are packets spanning logarithmically different prime scales. Exact equality on an interval still determines an analytic function; RE-190 is a conditioning statement saying that selector-scale source differences live in an `o(V_p)` residue. No Robin impossibility result follows without pricing the inverse conditioning or showing that the destination requires source information unavailable from the surviving common mode.