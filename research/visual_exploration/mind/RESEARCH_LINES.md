# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Treat the moving lower-source branch as closed after exact gamma recentering

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-039-wang-lower-source-crossover-is-resolution-dependent`.

VIS-282--VIS-298 separate the coefficient profile, Wang's complete pair statistic, deterministic gamma structure and the source transform. After exact gamma recentering, the apparent `sqrt(log T)` and related lower-source thresholds disappear: they were proof-packaging artifacts rather than arithmetic transitions.

## Reduce the natural-window problem to taper-weighted prime-ratio crowding without projecting away sieve dimension

**Linked intuitions:** `MI-040-wang-pointwise-upper-ceiling-is-a-localization-coherence-budget` and `MI-041-wang-natural-window-is-a-taper-weighted-prime-ratio-occupancy-problem`.

VIS-299--VIS-312 move the generic upper wall from localization leakage to coefficient-specific spacing, then show that randomized phases, completely multiplicative same-base controls and the true long-time prime-log orbit do not make the absolute candidate scale an intrinsic obstruction. Pointwise nearest-neighbour isolation itself has no cutoff-free limit because the full cross-base ratio spectrum is dense.

VIS-313 resolves that representation problem by grouping the strict near band by dyadic arithmetic height. VIS-314 retains two-prime sparsity and removes one logarithm from the shell energy. VIS-315 identifies the correct shell-local object: if `kappa_M(V)` is the maximal number of ordinary-prime ratio frequencies in a log-frequency cell of width `O(1/V)`, the separated-frequency large sieve plus coloring gives

`V^(-1) integral |F_M^pp(T)|^2 dT << kappa_M(V) E_M^pp`.

A nonempty frequency cell is, up to constants, a thin determinant strip `|qv-ur| << M^2/V` around a represented prime-ratio direction `u/v`. VIS-316 then removes unnecessary uniformity across shells. If

`kappa_M(V) << 1 + A_M M^2/(V log^2 M)`,

the Wang taper sees only `B(x,V)=sum_M w(M/x) sqrt(A_M)`, and at `H~V~x log log x` the natural-window mean square follows from `B=o((log log x)^(3/2))`.

VIS-317 adds a representation-level obstruction that is easy to miss if the determinant coordinate is treated as the arithmetic variable rather than the geometric label. For fixed coprime odd `u,v` and `h=qv-ur`, every odd prime `ell` away from `uv` admits **every** residue class of `h` with `q,r` both nonzero modulo `ell`: the exact local multiplicity is `ell-1` when `h=0` and `ell-2` otherwise. Thus `(q,r)->h` preserves the ratio-cell geometry but erases the two coordinatewise forbidden residues that carry the prime-pair sieve dimension. A determinant-only residue sieve cannot by itself generate the desired `log^(-2) M` density factor.

The live arithmetic question is therefore a taper-weighted determinant-strip estimate in a representation that retains the two prime coordinates: a pair-coordinate Selberg sieve, a fixed-`h` parametrization by two affine linear forms, or a weighted/additive-energy argument with equivalent information. A spectacular remote-shell cluster is not automatically relevant after tapering, but neither can the central-shell problem be solved by scalar determinant residue sifting after its prime-coordinate exclusions have already been projected away.

## Recombine exact deterministic structure before interpreting a proof wall

The current ledger separates coefficient weights, support-sensitive spacing, random versus completely multiplicative phases, the actual prime-log orbit, dense full-spectrum geometry, dyadic aggregate density, prime-pair sieve sparsity, Fourier-cell occupancy, shell taper, determinant projection, finite-window length and the moving-frequency/joint-limit quantifier.

VIS-313--VIS-317 give a reusable audit pattern: when dense spectrum makes pointwise gaps meaningless, aggregate by arithmetic scale; when a logarithmic loss remains, preserve the actual prime-pair sparsity; before demanding a uniform shell theorem, recombine shell excess through the destination taper; and when introducing a scalar geometric coordinate, check whether the projection has discarded the local residue exclusions that the intended sieve still needs. A structural transition is credible only after the remaining finite-height mechanism defeats a control that preserves these same weighted variables and arithmetic coordinates at the same scale.
