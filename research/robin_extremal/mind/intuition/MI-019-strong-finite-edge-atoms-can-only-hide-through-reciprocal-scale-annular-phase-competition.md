# MI-019 — Strong finite-edge atoms can only hide through reciprocal-scale annular phase competition

**Evidence level:** exact consequence of [RE-125](../../findings/RE-125-invisible-algebraic-subedge-atoms-require-a-reciprocal-scale-ordinate-annulus.md) and [RE-126](../../findings/RE-126-hiding-a-strong-subedge-atom-forces-a-logarithmically-comparable-vanishing-spacing-companion.md), building on the full-packet phase transfer of RE-123 and matched-filter localization of RE-124. No theorem excluding the required zeta-zero pairs, controlling diffuse packets, the nonattained edge or the `Theta=1` branch is claimed.

RE-124 shows that an algebraically strong subedge atom can remain invisible only if comparable coefficient mass is spectrally localized within `U^(-1+eta)` of its ordinate. RE-125 identifies a source-specific lower edge for that cancellation window.

For positive-ordinate finite-edge zeros with `sigma_0<=beta<Theta<1`, the leading Robin/CA coefficient `1/[rho(1-rho)]` lies in a fixed angular sector strictly inside the open right half-plane. Fixed-order `1/U` corrections preserve that sector. After demodulating at a target ordinate `gamma_0`, every neighboring atom with

`|gamma-gamma_0| <= c_*/U`

has a uniformly positive real projection. Exact multiplicity and tighter `o(1/U)` micro-clusters therefore reinforce the target; they cannot cancel it. The only strong-atom cancellation region is the annulus

`c_*/U < |gamma-gamma_0| <= U^(-1+eta)`.

RE-126 adds the local zero-count budget. An algebraically visible target lies at polynomial height, so a unit ordinate interval around it contains only `O(log U)` zeros by the Riemann--von Mangoldt count. If the target remains hidden, the comparable annular mass forced by RE-125 cannot be spread across arbitrarily many individually negligible atoms. At least one distinct-ordinate companion must satisfy

`|a_(rho_1,K)(U)| >= c |a_(rho_0,K)(U)|/log U`.

The companion is therefore algebraically strong up to a logarithm, lies in the same `O(log U/U)` horizontal edge layer at polynomial height, and obeys

`c_*/U < |gamma_1-gamma_0| <= U^(-1+eta)`

for every fixed `eta>0`. Along any unbounded sequence of hidden strong targets,

`|gamma_1-gamma_0| log(2+gamma_0) -> 0`.

So the strong-atom escape has become a **pairwise zero-geometry requirement**: an attained off-critical edge must support algebraically strong near-edge pairs whose ordinate gaps are vanishing relative to the conventional `1/log gamma` spacing scale. The pair need not be consecutive, and the theorem does not say the companion alone supplies the needed phase cancellation.

This is stronger than saying “nearby mass is needed.” The local zero count converts mass into an individual companion; the coefficient sector excludes sub-reciprocal same-direction clustering; and the CA phase mesh already resolves any surviving continuum excursion. A strong atom can hide only if an actual second near-edge zero appears in the narrow phase-rotation window with almost comparable coefficient size.

The next strong-atom theorem should therefore attack the existence or signed geometry of infinitely many such pairs. A spacing result is relevant only if it applies to the potentially off-line, nonconsecutive near-edge zeros forced here and at the required horizontal depth. The other live escape is qualitatively different: a diffuse boundary packet in which no individual atom reaches the algebraic threshold.

**Boundary.** RE-126 gives a necessary companion, not a sufficient cancellation mechanism and not a lower-gap theorem for zeta zeros. It does not rule out vanishing normalized gaps, control the companion's cancelling phase, or address diffuse many-mode mass. The durable refinement is that reciprocal-scale annular mass can no longer be treated as an arbitrary cloud: in the strong-atom branch it forces at least one logarithmically comparable near-edge zero companion.