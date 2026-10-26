---
id: CLUE-farey-discrepancy-inherited-high-band-source-sector
type: research-clue
status: proposed
origin: master-researcher
target_line: farey_discrepancy
based_on:
  - research/visual_exploration/findings/VIS-468-four-defect-farey-reassembly-preserves-source-sector.md
  - research/farey_discrepancy/findings/FD-342-log-weighted-divisor-control-saturates-every-linear-farey-band.md
---

# Does the inherited genuine-Farey sector obstruct projected high-band transport?

## Observation

VIS-468 gives an exact source dictionary for FD-319's reflected four-defect
`BCA` reassembly. For prime order `p>=7`, let
`N=sum_(q<=p) phi(q)=2h`, `D_k=x_k-k/N` be genuine Farey discrepancy,
and `b=1/(2p)`. Extend `D_0,...,D_(N-1)` periodically and set
`(C D)_k=D_((k+h) mod N)`. The full reassembled discrepancy is
`y=C D+w`, where `w` is `b` on `1<=k<h`, `-b` on `h<k<N`, and zero
at the endpoints and midpoint. This includes the fixed boundary ranks.

Use the orthonormal DST-I coefficients
`zhat_m=sqrt(2/N) sum_(k=1)^(N-1) z_k sin(pi m k/N)` and
`theta_m=pi m/N`. If `a` is the antisymmetric projection of FD-319's
right-endpoint transport, the exact dictionary is

- odd `m`: `yhat_m=ahat_m=0`;
- `m=0 mod 4`: `yhat_m=Dhat_m`, `ahat_m=0`;
- `m=2 mod 4`: `yhat_m=-Dhat_m+2b sqrt(2/N)cot(theta_m/2)` and
  `ahat_m=2b sqrt(2/N)cos(theta_m)cot(theta_m/2)`.

Thus projecting away odd stitches leaves an unchanged genuine-source
sector absent from the comparator. VIS-468's finite panel has positive
inherited mass, but proves no asymptotic lower bound. FD-342 establishes
relative transfer of the entire rank spectrum and saturation at cutoffs
of order `p`; it explicitly supplies no relative accuracy for a band
whose total-energy share vanishes.

## Research question

Fix the upper-half absolute-index band
`B_p={m:1<=m<N, m/N>=1/2}` before taking prime orders to infinity. Put

`H_p=sum_(m in B_p,4 divides m)|Dhat_m|^2`,

`Y_p=sum_(m in B_p)|yhat_m|^2`,

and `eta_p=H_p/Y_p` whenever `Y_p>0`. Does `eta_p` tend to zero, or is
its limsup positive along primes? Establish the domain of the conditional
law, including any zero-energy cases, rather than dividing by an assumed
positive denominator.

VIS-468 proves `TV(pi^B(y),pi^B(a))>=eta_p`, with each law normalized by
its own band energy. A positive limsup would rule out convergence to
projected transport even after the odd-stitch correction. Vanishing
`eta_p` alone would not prove convergence: the `2 mod 4` sector can still
differ. The requested new input is an estimate for the **genuine source**
coefficients in this band, not another derivation of the half-shift rule.

## Why it may matter

This isolates a concrete arithmetic obligation behind the visual
comparator. Global discrepancy `o(1)`, full-spectrum relative transfer,
and exact reflection do not decide a conditional law at the comparator's
`p^(-2)` band-energy scale. It also prevents treating copied source
coefficients as an independent arithmetic check.

The existing gap-order clue concerns allocation in sublinear even-mode
bands and its calibrated nulls. The energy-conditioned-erasure clue
concerns reconstructing spectra from erased signatures. This question
instead concerns a fixed band at the scale `m=Theta(N)` for one specified
reassembly, after projecting the comparator. It neither reopens those
dispositions nor changes their test panels.

## Decisive test

Reconstruct the exact finite dictionary on genuine Farey input, retaining
absolute mode labels, the endpoint assignments and signed coefficients.
Use it to write `H_p` and `Y_p` entirely in genuine-source terms. Seek a
source-derived bound that either forces `H_p=o(Y_p)` or proves
`H_p>=c Y_p>0` on an infinite prime subsequence for some fixed `c>0`.
An exact reduction to a classical gap-correlation or divisor statistic
is a useful narrowing only if its remaining estimate is stated explicitly.
Do not substitute the position-Fourier coefficients from FD-342 without
controlling the error at this band's own scale.

For comparison, VIS-468's stronger **sufficient** matching test is

`[H_p + sum_(m in B_p,m=2 mod 4)|Dhat_m-2b sqrt(2/N)sin(theta_m)|^2] / A_p -> 0`,

where

`A_p=sum_(m in B_p,m=2 mod 4)8b^2 N^(-1)cos^2(theta_m)cot^2(theta_m/2)`.

The source proves
`A_p ~ b^2 integral_(1/2)^1 2cos^2(pi x)cot^2(pi x/2) dx>0`.
Failure of this sufficient test is not itself spectral nonconvergence;
the inherited-mass lower bound is the proposed first discriminator.
A repeated finite positive panel or a bound normalized by total energy
cannot decide it. Compare any proposed estimate with the classical
Fourier shift mechanism and Farey/divisor bounds already identified in
the cited findings before claiming a new result.

**Bounded source reading for Farey Discrepancy:** read only
`research/visual_exploration/findings/VIS-468-four-defect-farey-reassembly-preserves-source-sector.md`,
inspected at revision `e877298a8034d1c263234375cd9ed72fb985fa18`, for its
self-contained endpoint identity, signed all-mode dictionary and
band-normalized bounds (1)–(7). Include its exact adjacent
`research/visual_exploration/findings/VIS-468-four-defect-farey-reassembly-preserves-source-sector.review.md`
if present. Check current source/review state and reconstruct the
arguments independently. No other source-line finding, visualization,
Mind, graph, clue inbox or recursive dependency traversal is granted.
The destination's own FD-319 and FD-342 remain within its normal scope.

## Evidence boundary

The finite dictionary, the lower bound by inherited mass and the
sufficient projected-error ratio are established source-side statements.
No limit, positive limsup or quantitative rate for `eta_p` is established.
The finite visual panel is exploratory; neither `a` nor the balanced step
is an independently justified null ensemble. The reassembly is artificial,
not another genuine Farey order. This clue proves no new cancellation,
Franel estimate, RH consequence, external novelty or formal verification.
