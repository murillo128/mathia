# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Beat the exact-endpoint source horizon only with analytic input whose admission, conductor and exceptional geometry all scale differently

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-071-exceptional-sets-must-be-measured-on-the-source-difference-frame`.

MC-366--MC-381 separate exact-real source leakage, finite-resolution quotienting, shell stability and the geometry of a hypothetical exact endpoint. After removing avoidable combinatorial losses, the current common-source obstruction is already linear in rank until an analytic ceiling intervenes:

`log P/log y >= c min{R, log log y}`.

MC-382--MC-384 identify three distinct reasons why a stronger-looking character estimate need not move that horizon. MC-382 isolates an exponential q-van der Corput depth tax. MC-383 shows that exponential family breadth cannot defeat a fixed positive power of one full modulus. MC-384 shows that Chang's factorization-sensitive theorem has excellent terminal saving once admitted, but its own applicability condition already forces `q=y^(O(log log y))` in the source regime.

MC-385 adds the source-family exceptional-geometry gate: ambient exceptional-set counts must be measured on the structured source-difference family actually used by the endpoint frame. Its row-sum argument shows that source-conditioned incidence, not ambient exceptional volume, is the relevant quantity.

MC-386 sharpens that gate to the natural quadratic threshold and shows it is generically sharp. If `W` is a surviving endpoint subspace, `H=|W|`, and the normalized source rows lie in rank at most `R`, the Welch/frame-potential identity forces total off-diagonal squared correlation at least `H/R-1`. If `E` difference modes are exceptional with trivial bound one and all remaining correlations have magnitude at most `epsilon`, then

`H/R-1 <= E+(H-1-E)epsilon^2`.

Thus good modes only need `epsilon=o(R^(-1/2))`, while the exceptional budget remains `E=o(H/R)`. An annihilator-subgroup Cayley frame attains the `H/R` exceptional scale, so generic PSD/rank geometry cannot improve it.

MC-387 closes the corresponding abstract near-extremizer question. For a PSD Cayley kernel whose Welch energy is `(1+o(1))H/R` and whose physical `L^2` mass is concentrated on `(1+o(1))H/R` points, finite Bochner theory turns the kernel into a probability measure `p` on the dual group. Near-Welch equality makes `p` almost uniform on its support; minimal physical concentration forces near equality in Young's inequality and hence asymptotically maximal additive energy of that support. Additive-combinatorial stability then forces the dual support to be `o(R)`-close to a subgroup coset and the physical concentration set to be `o(H/R)`-close to the corresponding annihilator subgroup.

The live frontier is therefore fully source-specific. Abstract frame geometry no longer leaves an arbitrary family of possible sharp escapes: any near-sharp endpoint frame must approximate the coset/annihilator model. The decisive question is whether the **actual quadratic-character source map** can realize or approach that geometry once primitive-character multiplication, conductor reduction, reused source primes and endpoint rank constraints are imposed. If those arithmetic rules exclude near-coset Fourier support, the generic sharpness example becomes inadmissible; if they permit it, the `H/R` barrier is structurally reachable.

## Keep resolution, source incidence, conductor, theorem admission, exceptional geometry and terminal saving distinct

The current resource ledger separates exact-real subset-sum conditioning, finite-resolution quotienting, source-incidence balance, package conductor, common-radical size, q-vdC factor depth, collective family size, global-modulus exponent, theorem-admission range, terminal saving exponent, ambient exceptional volume, bad-neighbor degree on the source Cayley frame, source-frame correlation energy and now **distance to the coset/annihilator near-extremizer class**.

These currencies are not interchangeable. A theorem can have a strong terminal estimate but fail admission; it can apply to exponentially many objects but pay one global conductor power; or it can control almost all ambient moduli while giving no certificate on the specific exponentially structured source family. MC-386--MC-387 show that pointwise correlation demands should not be set below the Welch scale and that near equality at that scale has a rigid additive-combinatorial form. Further generic Gram or uncertainty inequalities are unlikely to help unless they use arithmetic information that forbids that form.

## Repair probabilistic comparators only after exact-stratum and algebraic-collapse gates

Probabilistic proxies remain secondary until their conditioning is arithmetically consistent and their observables survive exact multiplicative simplification. A model that becomes degenerate after conditioning on an exact arithmetic stratum, or whose auxiliary statistic collapses algebraically to `M(x)`, has not created an independent cancellation mechanism.

The source-cost results add the same control at the theorem interface: a plausible endpoint comparator must not hide the exact architecture inside an ambient modulus class whose admission, conductor or exceptional-set geometry is misaligned with the structured source family. MC-386 supplies the sharp generic energy scale; MC-387 identifies the only asymptotic geometry that can nearly attain it under minimal physical concentration. Any improvement must now exploit arithmetic structure absent from the coset/annihilator control rather than refine the generic endpoint model again.