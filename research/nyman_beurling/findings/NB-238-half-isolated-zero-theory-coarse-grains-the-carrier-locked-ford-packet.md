# NB-238 — Half-isolated-zero theory coarse-grains the carrier-locked Ford packet into one clump

**Date:** 2026-09-20  
**Status:** `METHOD-BOUNDARY + SOURCE-SPECIFIC + CARRIER-RESOLUTION-AUDIT + NB-231/NB-237-REFINEMENT + PRIOR-ART-AUDITED`.

`NB-237` isolates the unresolved source observable as a microlocal signed average of

\[
R^{-1}\frac{\zeta'}{\zeta}(s),
\]

and identifies the dangerous geometry: a Ford-critical packet whose poles are separated by `Theta(1/R)` and whose carrier phases are locked. A natural source-specific candidate for excluding such packets is the zero-detecting theory of Maynard--Pratt, because it is explicitly sensitive to the vertical distribution of zeta zeros rather than only to their total density.

The scale audit below shows that the published half-isolated-zero mechanism does **not** resolve the obstruction. In the conservative matched-packet regime already proved admissible in `NB-231`, the entire carrier-locked packet lies inside a single Maynard--Pratt zero clump. Their half-isolated statistic can therefore see only the bottom of the packet while the Ford residual sees all `Theta(J)` poles coherently.

This is a method boundary, not a negative theorem about possible refinements of their detector. It identifies the missing resolution quantitatively: the Ford current requires vertical information at scale `1/R`, whereas the published half-isolated clustering is organized at scale `(log t)^3`.

## 1. The matched Ford packet lives at microscopic spacing `1/R`

Retain the Ford notation used in `NB-231`--`NB-237`:

\[
Q=\log(10+|t|),
\qquad
R=Q^{2/3}(\log Q)^{1/3},
\qquad
X\asymp R,
\]

and

\[
J=\frac RH\to\infty.
\]

The conservative matched-packet construction of `NB-231` works in the regime

\[
1\ll J\le \log Q.
\tag{1}
\]

It places

\[
M\asymp \delta J
\tag{2}
\]

points at one fixed Ford depth, hence on one vertical line, with ordinates of the form

\[
\gamma_j
=
t+\frac{2\pi qj}{X},
\qquad 1\le j\le M,
\tag{3}
\]

for a fixed nonzero integer `q`. Consequently

\[
\gamma_{j+1}-\gamma_j
=\Theta\!\left(\frac1R\right),
\tag{4}
\]

and the full packet has vertical diameter

\[
\operatorname{diam}_\gamma \mathcal P
\ll \frac JR
\le
\frac{\log Q}{Q^{2/3}(\log Q)^{1/3}}
=
Q^{-2/3}(\log Q)^{2/3}
=o(1).
\tag{5}
\]

The carrier phase is locked because

\[
e^{iX(\gamma_j-t)}=1.
\tag{6}
\]

At the critical Ford depth, the damping of each point is `asymp 1/J`; multiplying by `M asymp J` leaves an order-one coherent residual. This is precisely the pole geometry that survives the `O(1/R)` current normalization of `NB-237`.

## 2. Half-isolated-zero theory sees the whole packet as one clump

Maynard and Pratt introduce a zero-detecting method sensitive to vertical zero structure and define half-isolated zeros on a fixed vertical line. In their clustering formulation, consecutive zeros on the same line belong to one cluster when their ordinate gaps are at most

\[
(\log T)^3.
\tag{7}
\]

For the present packet, `T asymp t`, so `log T = Q+O(1)`. Combining (4) with (7),

\[
\frac{(\log T)^3}{\gamma_{j+1}-\gamma_j}
\asymp
Q^3R
=
Q^{11/3}(\log Q)^{1/3}\to\infty.
\tag{8}
\]

Thus the detector's clustering scale is larger than the carrier-locking spacing by a factor tending to infinity extremely rapidly.

More strongly, by (5),

\[
\operatorname{diam}_\gamma \mathcal P=o(1)\ll Q^3.
\tag{9}
\]

Hence all `M=Theta(J)` points of the adversarial packet form **one** Maynard--Pratt cluster. Within that packet, at most the bottom point can be half-isolated in the relevant downward sense; every later point has a lower zero on the same line at distance `O(1/R)`, far inside the `(log T)^3` isolation radius.

The resulting information compression is therefore

\[
\Theta(J)\ \text{carrier-relevant poles}
\quad\longmapsto\quad
O(1)\ \text{half-isolated representatives}.
\tag{10}
\]

But the Ford residual is proportional to the coherent sum over all `Theta(J)` poles, not to the number of clusters. The very geometry that makes the packet dangerous makes it maximally non-isolated.

## 3. A global bound on half-isolated zeros cannot exclude one resonant Ford cell

The main strength of the Maynard--Pratt method is that it can detect and bound zeros with suitable one-sided isolation, and thereby extract improved zero-density information under additional horizontal rigidity hypotheses. That is genuine vertical information beyond a population-only zero-density estimate.

For the present problem, however, two mismatches remain.

First, the Ford obstruction is **intra-cluster occupancy**. Even a hypothetical very strong statement saying that half-isolated zeros are globally sparse would permit one cluster containing `Theta(J)` zeros in the particular microscopic window selected by the carrier. The residual of that single cluster can still be order one.

Second, the unresolved coefficient in `NB-237` is deterministic at the chosen height `t`. An averaged or global count of exceptional cluster bottoms does not imply that the specific Ford window around `t` is empty or incoherent. To kill the matched packet one needs information on the internal configuration of a cluster at spacing `Theta(1/R)`, including its Ford depth and carrier phase.

So the published half-isolated-zero theorem is not a replacement for the missing microlocal cancellation estimate. It coarse-grains exactly the configuration that has to remain resolved.

## 4. Representation audit: the missing observable is cluster-internal phase, not cluster count

This scale comparison suggests a more precise way to formulate the next source theorem. A statistic adequate for the Ford current must distinguish configurations inside a single same-line clump. Schematically, it must control something comparable to

\[
\frac1J
\sum_{\rho\in\mathcal W(t)}
 e^{-d_\rho}
 e^{iX(\gamma-t)}
 \Psi_\rho,
\tag{11}
\]

where `mathcal W(t)` is one Ford-critical window, `d_rho=O(1)` is the critical depth coordinate, and `Psi_rho` denotes the smooth profile factor inherited from the shell.

A cluster count discards all three pieces that matter in (11): multiplicity/occupancy inside the cluster, microscopic ordinate modulo the carrier period, and depth--phase coupling. `NB-231`--`NB-233` already show abstractly that those data can support an order-one matched packet. The present audit shows that a concrete modern zeta theorem designed to exploit vertical structure still does not retain them at the required resolution.

The generic part of this observation is only a scale-separation principle: a detector organized at scale `Delta_big` cannot determine a coherent Fourier statistic whose phase changes at scale `Delta_small << Delta_big` unless it retains additional intra-cell data. The zeta-specific content is the quantitative substitution

\[
\Delta_{\rm Ford}\asymp R^{-1},
\qquad
\Delta_{\rm MP}=Q^3,
\tag{12}
\]

plus the fact that the `NB-231` packet lies on one vertical line and is already compatible with the previously audited Ford zero-density constraints.

## 5. Prior-art audit and limitation

The source checked in this pass is:

- James Maynard and Kyle Pratt, *Half-Isolated Zeros and Zero-Density Estimates*, International Mathematics Research Notices 2024 (19), 12978--13014, published 6 September 2024, DOI `10.1093/imrn/rnae191`, [arXiv:2206.11729](https://arxiv.org/abs/2206.11729).

Their paper explicitly introduces a zero detector sensitive to vertical distribution and organizes same-line zeros into clusters with `(log T)^3` spacing. That makes it unusually close prior art for the current Ford-resonance frontier. The calculation above does not use their theorem as a load-bearing estimate; it audits the resolution of the published observable against the already-derived matched packet, so no new theorem dependency is added to `SOURCES.md`.

The conclusion must not be overstated. It does **not** show that the Maynard--Pratt zero-detection machinery cannot be retuned to a microscopic Ford scale, nor that some intermediate lemma in their method cannot provide stronger local information after new work. It shows only that the published half-isolated/clump output, as stated, cannot exclude the carrier-locked packet that saturates `NB-231` and resonates with the `NB-237` current.

It also does not prove that actual zeta zeros realize such a packet. As throughout `NB-231`--`NB-237`, the packet is an adversarial configuration compatible with the currently audited constraints. The target remains to find a zeta-specific theorem that rules it out or forces cancellation inside it.

## 6. Consequence for the next perturbation

The Ford frontier should not be phrased merely as "find a zero theorem sensitive to vertical distribution." Half-isolated-zero theory already has that property and is still too coarse. The required theorem must preserve vertical information at approximately the carrier period

\[
\boxed{\Delta\gamma\asymp R^{-1}}
\]

inside the critical depth layer, or provide an equivalent cancellation statement for the `R^{-1} zeta'/zeta` current.

In particular, a promising refinement would have to control **cluster-internal** zero geometry: occupancy and Fourier phase at `1/R` resolution, jointly with Ford depth. Bounds whose terminal observable is only the number of clusters, the number of isolated representatives, or a global density remain compatible with an order-one resonant packet.

This narrows the source-side search without changing the destination-side caveat: no bridge from this Ford observable to the optimal Nyman--Beurling distance is proved here.