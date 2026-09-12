# MI-012 — Information content and destination sensitivity are separate mathematical resources

**Evidence level:** supported by the exact finite-Dirichlet discriminant radius AF-290, the first-layer Robin timing compression RE-069, and the sliding-aperture inversion/saturation theorem WI-254; the three operators and targets remain distinct.

Three current lines now isolate different ways in which a mathematically rich intermediate representation can fail to yield a useful final theorem.

AF-290 gives the clean conditioning case. Finite Dirichlet coefficients may be stably recovered modulo the common-clock gauge, but a zero-count target is protected only inside its own exact distance to the boundary-zero discriminant. Upstream error `eta` matters only relative to the target margin `delta_Gamma(b)`. Stable representation recovery and stable target transport are therefore different questions.

RE-069 gives the kernel-compression case. First-layer CA delays carry asymptotically half of a matched packet's logarithmic mass in raw transport coordinates, yet the exact Robin derivative kernel maps each delay to `1/p-log(1+1/p)=O(p^-2)`. The information is present and extensive before readout but becomes an absolutely summable tail in the requested scalar workload.

WI-254 gives the inequality-loss case. The exact sliding-aperture profile at a hypothetical first global Weil crossing determines the whole real autocorrelation through distributional differentiation. But firstness supplies only a pointwise lower envelope for that profile. The envelope cannot be differentiated into prime-threshold signs, and its small-radius leading term is asymptotically saturated. The representation is information-complete; the available theorem about it is not.

These are different mechanisms, but they impose one concrete diagnostic:

**after proving that a representation contains a desired source variable, identify the exact map from that variable to the final target and quantify the target's sensitivity before assigning mathematical value to the representation.**

The missing object may be a distance to an ill-posed locus, a non-summable kernel response, or a stronger relation on an information-complete profile. More source coordinates, more accurate upstream reconstruction, or more apertures do not help if the destination map collapses the added information.

**Boundary.** No discriminant formula, Robin kernel estimate, or aperture inversion transfers between these lines. The synthesis is the separation of resources: representation information, available control on that information, and destination sensitivity must each be established in the actual mathematical category of the target.
