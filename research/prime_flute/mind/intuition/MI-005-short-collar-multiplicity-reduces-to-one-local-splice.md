# MI-005 — Short-collar assembly reaches endpoint energy; the remaining gate is the conservative splice

**Evidence level:** exact geometric accounting, rigidity, weak-endpoint, and endpoint transport results through PF-191

## Core intuition

The Prime-Flute comparison has moved beyond the question of whether infinitely many thin pieces or the Lambert bodies have enough integrability. Above the endpoint, PF-183--PF-188 reduce short-collar multiplicity to one fixed-germ Sobolev localization problem and show why generic `C^1` branch selection is false. At the endpoint, PF-189--PF-191 now show that the central thin sector and the exact-area body transport both have substantially better budgets than the coarse global estimates suggest.

The unresolved object is therefore the **uncut conservative reassembly**: turn the endpoint body/collar energy into a fixed-germ exact-area splice with a linear cost, and then decide whether the critical gradient factors yield true weak trace class or a genuine logarithmic loss.

## Strongest justified principle

PF-183 makes infinitely many true short collars harmless once one uniform local splice estimate is charged to the body energy. PF-184--PF-185 remove annular flux and linearized Killing obstructions and provide an energy-local exact-area cutoff inside a fixed `C^1` chart. PF-186 proves that such a chart cannot be obtained from small strain alone: Hamiltonian microtwists can have vanishing metric defect and displacement while retaining order-one microscopic derivative rotation.

PF-187--PF-188 identify the correct weaker entry mechanism. On one fixed larger marked collar, vanishing strain and collar mismatch force `W^{1,r}` convergence to the canonical inclusion for every `r>1`; boundary normalization is not intrinsically needed, but fixed-germ confinement remains load-bearing.

PF-189 then proves that the complete decoupled central short-collar first-resolvent sector is already `S_{1,infinity}` with a summable weak-endpoint tail. PF-190 shows that a **global** two-sided weighted `L^1` metric budget would imply `S_r` norms growing like `(r-1)^{-2}` and hence the conditional singular-value envelope `O(log^2 n/n)`. The square logarithm comes from two critical gradient-resolvent half-factors and is not known sharp.

PF-191 closes a previously coarse geometric input at exactly this endpoint. The explicit PF-179 exact-area Lambert map has pointwise defect decaying across the body; integrating the actual cross-section yields `d/cosh(a)` at `r=1`, and the corner Moser correction is even smaller when measured relative to the outer isometry. For the prime/shift sequence these costs are summable, and the assembled-body `L^1` budget plus weighted thick-transition budget follows.

Thus the body transport does not explain a possible endpoint failure. **Any remaining loss must be created by fixed-germ collar localization or by the operator reassembly itself.**

## What remains possible

The low-regularity route is now sharply stated: prove endpoint fixed-germ confinement and an energy-linear exact-area splice on the actual canonical collar/body germ. If that yields weak-`S_2` control for each critical gradient half-factor, the full relative resolvent may reach weak `S_1`; if not, a source-faithful counterexample may show that the logarithmic envelope reflects a genuine assembly effect.

A source-specific `C^1` entry theorem derived from the explicit exact-area construction remains a distinct route. Either way, no arithmetic significance follows until a marked spectral observable separates the prime flute from its all-composite shift clone.

## Status / novelty

The collar geometry, exact-area transports, Sobolev rigidity, weak-Schatten estimates, and endpoint bookkeeping are persisted line evidence; the analytic tools behind them are classical or previously audited. The durable synthesis is the boundary relocation: **short-collar multiplicity and Lambert-body endpoint energy are controlled; the live geometric/operator gate is the endpoint conservative splice and its critical reassembly.**

## Falsification criterion

Show that PF-191's exact-area endpoint estimate fails on the prime/shift Lambert bodies; produce a contribution from the complete decoupled central family worse than PF-189's weak `S_1` bound; or prove that the actual canonical collar germ cannot satisfy any fixed-germ endpoint localization compatible with the existing body energy. Any such result would reopen an earlier boundary.