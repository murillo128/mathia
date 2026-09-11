# Prime-flute research lines

This file holds the current mathematical questions suggested by the durable prime-flute intuitions. It is not a roadmap, task queue, status page, or history.

## Stop using the fixed-axis Robin normalization as a supercritical low-output escape

**Linked intuition:** `MI-007-square-root-functional-calculus-closes-the-finite-seam-mass-gap`.

PF-271--PF-278 show why separated propagation initially looked promising and why the fixed-axis route nevertheless closes at the critical continuum threshold. The fully Robin-normalized fixed-row shell leakage is `asymp N^(-1)(log N)^(-3/2)`: logarithmically improved, but not supercritical by any fixed power. The fixed-axis Robin-homotopy route is closed rather than merely unresolved.

## Prove a heavy-angle counting law for the physical energy-normalized low/high cross form

**Linked intuition:** `MI-008-complete-cut-transmission-needs-extension-mass-not-only-boundary-impedance`.

PF-228--PF-281 separate unprojected reservoir transmission from the actual physical low/high leakage. Positivity canonically defines the bounded energy-normalized cross operator `T=A^(-1/2) B C^(-1/2)`, and membership of `T` in the required symmetric ideal passes to the mixed inverse block and reciprocal-prime commutator. Same-sector reservoir amplification is therefore not itself an obstruction to the projected route, while positivity alone does not force compactness.

PF-282 identifies the remaining invariant. After polar normalization,

`T = f(|R_P|) Gamma f(|R_H|)`

with `f(t)=t/sqrt(1+t^2)` and `Gamma` the relative low/high extension-angle operator. On sectors where extension mass is already large, the singular values of `T` are equivalent to those of `Gamma`; reservoir strength saturates and persistent angular overlap is the real obstruction.

PF-283 converts the weak-trace endpoint into a counting problem. Thresholding the heavy extension sectors gives `||T-T_tau||<=2 tau` and reduces singular-value control to the Weyl count of the compressed angle operator. In particular, a uniform bound of the form `sup_tau tau N_(Gamma_tau)(2 tau)<infinity` is sufficient for the required weak-trace class.

The live theorem is therefore concrete: prove a **heavy-angle counting estimate for the complete physical low/high extension geometry**, including finite-pant completion and neighboring-cell coupling. Unprojected cut norms and raw extension mass are matched controls; what matters after energy normalization is how many heavy directions retain a large low/high angle.

## Treat branch singularity, reservoir strength, and extension angle as distinct currencies

The fixed-axis source fails through a threshold branch. Variable same-sector reservoirs can erase an isolated unprojected seam gain. After energy normalization their magnitude saturates, leaving the relative extension angle as the mixed-channel currency. A new Prime-Flute argument must control the angle count at the endpoint ideal scale rather than transfer conclusions from either of the first two mechanisms.