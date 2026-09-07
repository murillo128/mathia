# MI-010 — Source-fixed endpoint renormalization closes the current Xi source-to-periodic bridge

**Evidence level:** exact singular/reference analysis, Xi-specific endpoint regularity, exact moment realization, and guarded Volterra shadowing through XF-097

## Core intuition

The Xi continuum-to-periodic interface contains real singular structure, but that structure is deterministic source data rather than an open arithmetic error. The endpoint pole fixes the logarithmic lattice counterterm, positive heat time forces a universal lower-order `xi log^2 xi` correction, and the corrected Xi residual has enough endpoint regularity to be sampled on the actual Volterra mesh.

With those source-fixed sectors removed in the canonical normalization, the remaining source trajectory can be realized by an exact finite real periodic carrier and transported for fixed heat time with `o(1)` error in the same guarded resource used downstream. The current bottleneck has therefore moved from source discretization to destination coercivity.

## Strongest justified principle

XF-088 proves that the pole `-1/(4 xi)` requires the mesh counterterm `(1/4) log Delta delta_0`; omitting it leaves a logarithmically growing vector-field defect. XF-089 shows that the pole residue remains `-1/4` throughout the positive-time reference regime, so the leading renormalization is source-fixed rather than time-refitted.

XF-094 identifies and removes the deterministic linear endpoint floor at `t=0`. XF-095 then propagates the endpoint correction dynamically: the reference forcing integrates into the universal term `-(t^2/32) xi(log xi+C_0)^2 + beta(t)xi`, after which the corrected residual is `O(xi^2 log^3 xi)` and the corrected reference defect is guarded-small. This non-`C^1` reference cusp is forced by the heat evolution rather than introduced to fit the mesh.

XF-096 uses the Xi-specific endpoint derivative bound together with the exact cellwise `H^1` sampling inequality to close the anti-concentration gap exposed by XF-093. XF-097 completes the interface: the full endpoint prefix has normalized `ell^1=o(1)`, so it has an exact equal-weight unit-circle realization, and the resulting periodic heat trajectory shadows the canonical Xi positive-frequency trajectory for fixed time in the declared guarded resource.

## Counterevidence / boundary

The closure is scale-, topology-, and observable-specific. A later theorem using a different frequency band, stronger norm, or longer heat interval may require a new transport estimate. The source-fixed corrections also do not prove anything about the sign of the de Bruijn--Newman constant.

Most importantly, transport closure is not transition coercivity. XF-098 constructs a genuine isolated periodic collision threshold whose low-frequency guarded resource stays `o(1)` under full heat. The remaining theorem must therefore force a collective Xi-specific destination signal rather than infer it from collision existence alone.

## Epistemic status

**Exact source-side renormalization and source-to-periodic transport closure at the current guarded scales; positive-transition destination coercivity remains open.**

## Falsification criterion

Break any load-bearing source statement: the fixed pole residue/counterterm, the dynamic `xi log^2 xi` correction, the corrected endpoint `C^1` bound, exact full-prefix realization, or fixed-time guarded shadowing. A positive continuation should instead prove that a hypothetical `Lambda>0` Xi transition creates nonvanishing destination resource despite the sparse-collision controls.