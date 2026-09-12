# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Prevent the first forbidden localized Weil crossing in the correct form topology

**Linked intuition:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`.

PL-280--PL-282 give the one-sided aperture ledger, global exhaustion, and a terminating finite positivity certificate at each fixed aperture. PL-283--PL-284 add a conditional computer-assisted positive endpoint at `a=0.8` with a simple isolated ground state and a tiny but explicit positive margin.

PL-285 closes the naive perturbative bridge from that endpoint. After scaling to a fixed interval, each already-active prime-power term contains a compressed translation with shift `log(n)/a`. These translations are strongly continuous but maximally discontinuous in ambient `L^2` operator norm: an arbitrarily small nonzero shift change can have norm difference approaching two. Therefore “no new prime atom enters” does not imply a small bounded-operator perturbation, even inside the source-static interval before `log(5)/2`.

The canonical logarithmic form domain restores continuity. On an `H^log` energy ball, the moving translations admit only a logarithmic generic modulus, of order roughly `1/sqrt(log(1/|delta|))`. This identifies the correct topology behind Suzuki's continuity theorem, but compared with the `8.9e-18` endpoint margin it is far too weak, without much stronger constants or regularity, to bridge the visible interval quantitatively.

The live theorem is therefore a **form-level source-specific transport law**. It must exploit uniform low-energy `H^log` bounds, stronger regularity of the ground branch, cancellation among the moving arithmetic channels, or another variational/Schur identity. Termwise `L^2` operator-norm perturbation is a closed route.

## Separate endpoint isolation, qualitative continuity, and aperture-uniform coercivity

A simple positive ground state makes local spectral tracking meaningful, but PL-285 shows that the topology and modulus of that tracking are themselves part of the arithmetic problem. Qualitative continuity, a fixed-window gap, source-static support, and a usable quantitative positivity radius are different resources. A future endpoint certificate matters globally only if it composes with a transport estimate in the canonical form geometry.