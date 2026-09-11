# Prime-flute research lines

This file holds the current mathematical questions suggested by the durable prime-flute intuitions. It is not a roadmap, task queue, status page, or history.

## Stop using the fixed-axis Robin normalization as a supercritical low-output escape

**Linked intuition:** `MI-007-square-root-functional-calculus-closes-the-finite-seam-mass-gap`.

PF-271--PF-278 show why separated propagation initially looked promising and why the fixed-axis route nevertheless closes at the critical continuum threshold. The fully Robin-normalized fixed-row shell leakage is `asymp N^(-1)(log N)^(-3/2)`: logarithmically improved, but not supercritical by any fixed power. The fixed-axis Robin-homotopy route is closed rather than merely unresolved.

## Prove angular decay on genuinely infinite heavy sectors

**Linked intuition:** `MI-008-complete-cut-transmission-needs-extension-mass-not-only-boundary-impedance`.

PF-228--PF-283 reduce the physical low/high leakage to the bounded energy-normalized factorization `T=F_P Gamma F_H`. On heavy extension sectors the outer strengths saturate, so relative extension angle is the mixed-channel currency. PF-283 gives a sufficient weak-trace criterion through thresholded angle counting.

PF-284 makes the endpoint budget two-sided. For symmetric threshold `tau`,

`N_T(4 tau) <= N_(Gamma_tau)(2 tau) <= N_T(2 tau^3)`.

Thus `O(tau^(-1))` is a sufficient heavy-angle count, whereas weak trace class itself forces only the much weaker `O(tau^(-3))` necessary envelope. Failure of the original sufficient count is not yet an endpoint obstruction; divergence of the corresponding `tau^3` statistic is.

PF-285 identifies an abstract cheaper route: complementary weak-Schatten decay of the two extension-strength factors would close the endpoint even with no angular decay. PF-286 rules that route out for the canonical physical split. The low strength factor has infinite rank above every positive threshold, and the high strength factor is noncompact with an infinite heavy population below a fixed threshold. No finite population exponents exist.

The live theorem is therefore genuinely angular: compactness/weak-trace decay must come from the **relative low/high extension geometry on infinite-dimensional heavy sectors**, or from an equivalent threshold-dependent strength-angle relation. Raw reservoir size, population decay of the outer factors, and the original `tau^(-1)` sufficient statistic are now matched controls.

## Treat sufficient angle counts, necessary endpoint counts, strength populations, and physical angle geometry as separate gates

The energy-normalized factorization isolates the right channel, but several endpoint criteria have different logical strength. Future work should first test the genuine obstruction statistic supplied by PF-284 and then exploit the complete physical extension geometry; it should not infer endpoint failure from a missed sufficient count or hope that outer-factor compactness will supply the missing decay.