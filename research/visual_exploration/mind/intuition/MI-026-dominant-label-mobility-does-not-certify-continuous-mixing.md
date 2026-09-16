# MI-026 — Dominant-label mobility does not certify mixing of the continuous conditioned geometry

**Evidence level:** proved local transition law from the VIS-249--VIS-251 exact Gibbs construction, with the label-switch calculation established in [VIS-251](../../findings/VIS-251-uniform-triple-gibbs-escapes-dominant-labels.md).

For the exact uniform random-scan three-coordinate heat-bath chain on a regular log-product level, suppose one coordinate `j` satisfies

`x_j > 3 max_(k!=j) x_k`.

Then the identity of the global maximizer changes after one update with exact probability

`2/m`,

independent of the conditioned log-product level `lambda`. Each specified alternative label becomes maximal with probability `2/[m(m-1)]`.

The mechanism is elementary but diagnostically important. A selected triple excluding `j` has total mass below `x_j`, so cannot replace it. A triple containing `j` necessarily contains the new global maximum, and exchangeability of the exact labeled conditional assigns its largest root uniformly among the three labels. The scan probability `3/m` times the conditional switch probability `2/3` gives `2/m`.

Therefore a visually vertex-like state space does not acquire a high-`|lambda|` metastable barrier merely through the **label** of its dominant coordinate. Label changes can remain frequent while the chain still mixes slowly in continuous degrees of freedom: sizes of the small coordinates, movement along narrow block fibres, another collective coordinate, or conductance outside the dominance cone.

The practical inference is one-way. Slow label switching can reveal a problem, but fast label switching is not evidence of global mixing. Quantitative calibration must monitor continuous observables relevant to the final statistic and compare separated admissible starts; the exact `2/m` law is a control that removes one false bottleneck explanation, not a spectral-gap theorem.
