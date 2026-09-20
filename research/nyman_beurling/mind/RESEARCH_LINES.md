# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the source-only full-band obstruction through the legal Hardy/Nyman destination

**Linked intuitions:** `MI-062-the-critical-ford-mark-is-a-growing-moment-observable`, `MI-063-demodulated-ford-energy-is-bandlimited-at-the-window-scale`, `MI-064-signed-scalar-coherence-shrinks-only-by-paying-total-variation`, `MI-065-signed-carrier-cost-must-be-measured-after-quotienting-unresolved-microscopic-dipoles`, `MI-066-resolved-carrier-channels-can-amortize-hilbert-cancellation-at-j-two-thirds`.

NB-245--NB-250 fix the representation and order of operations: the Ford-scaled Cauchy pole must be Hardy-projected through positive Mellin frequencies before Hilbert-space squaring, and the surviving second moment is a positive carrier-band form factor at natural width `Theta(H)=Theta(X/J)`.

NB-251--NB-256 separate coherence cost from representation artifacts. Positive or bounded-variation scalar mixtures retain compulsory coherent windows, but unresolved opposite dipoles show that raw total variation is not a physical source norm. NB-257 repairs that defect with an `H`-separated dictionary: translated shells are disjoint, so shell-scaled source `L^2` is coefficient `ell^2`. One Ford-scale notch can nevertheless be amortized at bounded cost once `K~J^(2/3)` resolved channels are available.

NB-258 now closes the corresponding **full fixed Ford-band** loophole throughout every fixed-power mesoscopic regime. If the shell-Hilbert cost stays bounded and

`K <= J^(1-delta)`

for some fixed `delta>0`, then after Ford rescaling `C_J(x)=B_lambda(x/R)` has a derivative order `q=q(delta)` with `||C_J^(q)||_infty=o(1)`. On every fixed bounded Ford interval it is therefore `o(1)`-close to a polynomial of fixed degree with `C_J(0)=1`. Finite-dimensional polynomial coercivity gives a strictly positive `L^2` floor on every interval of positive length. At the NB-257 crossover `K~J^(2/3)`, the bounded-cost carrier is asymptotically affine: it can hit one notch but cannot suppress a whole band.

Hence any bounded-source-cost scalar family that truly erases a fixed Ford band must satisfy

`K = J^(1-o(1))`,

or equivalently for a filled resolved span `W~KH`, `W/R=J^(-o(1))`. This is much stronger than the one-notch `J^(2/3)` crossover, but it remains source-only. The live question is whether the legally Hardy-projected Nyman destination inherits a comparable full-band lower bound, or whether projection/cancellation can still discard the source-side energy that NB-258 forces to remain.

## Keep source-band coercivity and final Hardy/Nyman energy distinct

NB-258 is a method boundary for resolved scalar dictionaries, not an RH estimate. It proves that fixed-power mesoscopic spans cannot suppress a full unprojected Ford band at bounded shell-Hilbert cost, but NB-250's full-line carrier-energy route is sufficient rather than known to be equivalent to the final Nyman distance.

A surviving scalar mechanism must therefore either operate at near-Ford channel count `J^(1-o(1))`, exploit a destination projection that invalidates the source-band lower bound, or introduce structure outside the resolved scalar dictionary. The next theorem must keep Euler normalization, source Hilbert cost, channel resolution, Ford rescaling and the actual positive-frequency Hardy projection in the same argument; a source-only band floor cannot simply be declared to survive the destination map.