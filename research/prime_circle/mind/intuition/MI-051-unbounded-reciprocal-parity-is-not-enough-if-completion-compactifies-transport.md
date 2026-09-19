# MI-051 — Breaking bounded reciprocal parity is not enough: scalar completions either compactify transport or reduce to radial Fock geometry

**Evidence level:** exact synthesis from `PC-358`--`PC-360` plus classical compact-operator and weighted-shift theory.

PC-358 isolates the first infinite-dimensional requirement. If the algebraic reciprocal-parity intertwiner remains bounded on the chosen completion, source and control remain similar and ordinary spectral data cannot distinguish them.

PC-359 shows that violating this boundedness condition is only one gate. In a scalar grade-weighted word completion, reciprocal parity can become genuinely unbounded while a positive-degree creation block of lag `k` has size governed by `sqrt(w_(m+k)/w_m)`. If every fixed-lag ratio tends to zero, those blocks are compact. A norm-convergent strictly grade-raising multiplier is then compact and quasinilpotent, so the desired ordinary spectrum disappears before any arithmetic comparison is made.

PC-360 closes the natural scalar borderline in the opposite direction. If

`w_(m+1)/w_m -> r`, with `0<r<infinity`,

then for every fixed lag `k` the weighted left creation operator is, after canonical unitary reweighting, a compact perturbation of ordinary free-Fock creation scaled by `r^(k/2)`. Every finite positive-degree polynomial therefore has the same high-grade/Calkin geometry as the standard free-Fock multiplier after a radial degree dilation. Noncompact transport survives, but no new asymptotic operator geometry is created by the scalar weights.

The most immediate source/control discriminator in that regime also fails the arithmetic matched-control test. A fixed two-dimensional nonarithmetic involution and a variable positive one-particle metric can make the ratio between reciprocal-control and source homogeneous spectral radii arbitrarily large. Thus passing both necessary gates from PC-359—unbounded reciprocal parity and noncompact high-grade transport—is still not sufficient. A spectral gap produced only by the completion metric is not arithmetic information.

The reusable audit now has three stages. **First test bounded similarity. Second test whether the actual source operator retains noncompact transport. Third test whether the surviving spectral distinction is invariant under matched nonarithmetic choices of metric/completion.** Scalar grade weights fail one of the latter two tests in both natural asymptotic regimes: decay compactifies the multiplier, while positive finite ratio leaves radial standard-Fock transport modulo compacts.

A genuinely new route must therefore use structure that the scalar grade sequence cannot encode: non-scalar inter-grade coupling, uncontrolled infinite mixed-degree tails outside the finite-polynomial/norm-summable compact-error regime, unbounded or closed operators with informative domains, same-grade/backward/two-sided interactions, or a source-forced observable whose distinction survives nonarithmetic metric controls.

**Boundary.** PC-360 does not classify arbitrary infinite series without additional convergence control, non-scalar grade weights, unbounded operators or different observables. Its nonarithmetic metric family refutes only the claim that a homogeneous radius gap is intrinsically arithmetic. Nothing here selects zeta zeros or implies RH.