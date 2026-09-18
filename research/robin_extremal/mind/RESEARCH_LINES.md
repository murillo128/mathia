# Robin-extremal research lines

This file holds the current mathematical questions suggested by the durable Robin-extremal intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve the scalar Euler frontier between exact identification and selector-scale stable rigidity

**Linked intuitions:** `MI-001-robin-failure-requires-self-tangent-half-mass-event-gaps` through `MI-053-positive-real-euler-is-laplace-compressive-vertical-phase-is-fourier-resolving`.

The matched-control program has progressively removed apparent scalar rigidity thresholds. Ordinary-prime `{0,1,2}` controls can preserve every fixed KV source envelope and an order-one transient Robin excursion while matching exact Mertens/Euler data at fixed depth, growing depth and separated temperatures. RE-188 optimizes the deep Euler-jet repair to a linear-width Chebyshev window and keeps exact source-side non-rigidity throughout

`K=o((log p)^(5/3)(loglog p)^(1/3))`.

RE-189 supplies a qualitatively different upper-scale obstruction. For a prime factor with `L=log q`, factorial-normalized high boundary derivatives become essentially a net-multiplicity channel near the log-squared scale. RE-190--RE-193 show, from the complementary spectral side, that shrinking Euler windows collapse to reciprocal-mass rank one and fixed windows have factorially compressible finite-Laplace rank controlled by `R=U log(Q_+/Q_-)`, with only logarithmic stable-rank growth in transform rectangle and requested precision.

RE-194--RE-195 show why unsigned reciprocal variation is not a coercive source resource. The Robin debt scale `d_p~1/(sqrt(p)log p)` determines the relevant relative tolerance, but arbitrary reciprocal variation can be hidden in remote Chebyshev-balanced ordinary-prime packets whose fixed Euler profile is `O(p^-2)` while exact jet repair, KV fidelity and the order-one Robin transient survive.

RE-196 moves from finite panels to the entire positive real Euler ray. Exact matching of the first `K` boundary jets makes the selector-centered transform vanish to order `K+1`, and selector damping turns the first omitted centered moment into a global inverse-modulus bound. For every fixed `K`, the complete real ray can therefore be `o(d_p/(log p)^A)` for arbitrary fixed `A` while the Robin destination changes by order one.

RE-197 makes that collapse uniform at growing depth for the fixed-width repair. If `K loglog p=o(log p)`, then

`sup_(s>=1)|D_Q(s)| <= d_p exp(-(1-o(1))K loglog p)`.

RE-198 replaces the fixed-width repair by the linear-window RE-188 geometry. Writing `L=log p`, every growing `K=o(L)` satisfies

`sup_(s>=1)|D_Q(s)| <= d_p exp(-(1-o(1))K log(L/K))`.

Thus the complete positive real Euler ray remains stably noncoercive through every sublinear jet depth.

RE-199 shows that `K~L` is **not itself** the onset of scalar rigidity. Keeping the exact RE-188 window width `W=4K` inside the first omitted moment gives, for every fixed `eta<1/4` and every `K<=eta L`,

`sup_(s>=1)|D_Q(s)| << d_p e^(C sqrt(K)) K ((4K+O(1))/L)^(K+1) + d_p p^(-1+o(1))`.

Hence whenever `K->infinity` and `K<=eta log p`,

`sup_(s>=1)|D_Q(s)| <= d_p e^(-c_eta K)`.

More precisely, if `K/L->kappa<1/4`, the relative suppression is

`exp(-(1-o(1))K log(1/(4 kappa)))`.

The prime-power modes remain cheaper by a full additional factor `p^-1`; the obstruction is the first-harmonic centered radius, not hidden growth from higher Euler harmonics. The ordinary-prime realization, exact jet matching, `{0,1,2}` multiplicities, KV fidelity and pre-repair order-one Robin excursion are unchanged.

The number `1/4` is a **representation threshold of the present `W=4K` absolute-moment estimate**, not a universal rigidity constant. It is where the factor `(4K/L)^(K+1)` stops decaying. A different repair frame with smaller effective centered radius, or signed cancellation in the first omitted moment, could cross it. Conversely, RE-199 proves that merely reaching linear depth is not enough: a genuine positive fraction of the `log p` scale is still continuum-near-null.

RE-200 separates that positive-real failure from complex spectral geometry. On any fixed multiplicative prime shell, actual ordinary primes can be placed on an almost uniform logarithmic grid using the same KV PNT input. Sampling the exact Euler factors at dual imaginary frequencies produces a diagonally weighted DFT plus a vanishing prime-placement/prime-power perturbation. For every `K` with `log K=o(V(Q))`, the resulting `K x K` response matrix has all normalized singular values bounded away from zero while the largest imaginary height is only `O(K)`.

Thus the strong compression in RE-190--RE-199 is not a generic property of scalar Euler data: it is specifically tied to **positive-real Laplace damping**. On the same fixed shell and comparable span, RE-193 gives polylogarithmic approximate rank for positive-real samples, whereas RE-200 gives linear Euclidean dimension for vertical complex samples. For `K~c log Q`, a height `O(log Q)` complex window already has raw representation capacity for `Theta(log Q)` honest prime directions.

RE-201 shows why that within-shell conditioning is still not a global inverse estimate. The commensurate heights `t_k=2pi k/W` identify logarithmic prime position only modulo `W`: a shell shifted by `mW` in `log q` has exactly the same first-harmonic phases. Using `Lambda=e^(mW)=Q^o(1)` and about `Lambda` ordinary remote primes per unit local reciprocal mass realizes that alias with honest `{0,1,2}` multiplicities. At total local population `B~sqrt(Q)/log Q`, the packet carries selector-scale debt `d_Q~1/(sqrt(Q)log Q)` between the local and remote shells, yet all `K` sampled exact Euler values are `o(d_Q)` after repair. The entire construction remains inside every fixed KV envelope.

RE-202 removes exact commensurability as the essential escape hatch. Let

`L_KV(Q)=(log Q)^(5/3)(loglog Q)^(1/3)`.

If a finite height family lies in a rank-`r` integer frequency module with coefficient radius `K`, simultaneous Diophantine approximation gives a common approximate logarithmic period whose cost is polynomial in `K` with exponent `r`. Pulling that recurrence back to exact ordinary-prime Euler atoms yields the same selector-scale `{0,1,2}` remote alias whenever

`K^r=o(L_KV(Q))`.

The displacement can be chosen with `log Lambda=o(L_KV(Q))`, which is still cheap enough that the remote prime population exists and every fixed KV source envelope survives. In particular, **two irrationally related arithmetic panels remain noncoercive throughout**

`K=o((log Q)^(5/6)(loglog Q)^(1/6))`.

At the opposite extreme, treating every sampled height as an independent frequency shows that any fully jittered panel of `M=o(loglog Q)` heights of size `O(M)` still has a common recurrence early enough to realize the same selector-scale ordinary-prime alias. Thus merely replacing the DFT grid by one or two incommensurate panels does not solve shell-index recovery; the relevant resource is spectral Diophantine rank relative to the source-fidelity displacement budget.

Exact continuum identification and selector-scale stable discrimination are therefore more sharply separated. RE-174 remains valid at infinite precision: exact values on an unbounded temperature set identify the source. RE-196--RE-199 show that the inverse has no Robin-scale modulus along increasingly deep ordinary-prime matched directions throughout every fixed linear wedge `K/log p<1/4` covered by the existing positive-real representation. RE-200 shows that vertical phase can restore linear dimension inside one shell, RE-201 shows that a commensurate panel can lose that information globally through multiplicative aliasing, and RE-202 shows that low-Diophantine-rank incommensurability still admits cheap approximate shell recurrences.

The scalar frontier now has two genuinely different representation questions. On the real ray, a future rigidity argument must control the first omitted centered moment beyond the `W=4K` absolute bound, prove an unavoidable lower bound on effective repair radius, or exploit signed/source complexity that the present estimate discards. In the complex direction, the next positive target must go beyond nominal incommensurability: construct a height family whose common almost-periods are excluded throughout the KV-affordable logarithmic displacement range, and then test whether several remote shells with integer prime populations can nevertheless synthesize the same observation vector. For low-rank spectral modules RE-202 already prices the recurrence explicitly; for fully irregular panels the first universal escape from that argument is around the `log log Q` sample scale. RE-189's separate log-squared common-mode collapse remains a further warning that deeper scalar coordinates need not improve monotonically.

## Control one-sided reciprocal escape independently

The zero-side packet obstruction remains separate. One-sided vertical phase geometry can hide a scale-maximal target along lacunary stages while fixed-order typical local-correlation statistics remain unchanged. Closing that branch still needs target-conditioned exceptional geometry rather than average-center statistics.

## Keep exact identification, stable information and destination leverage distinct

Finite ordinary-prime rigidity, full exact Euler-germ identification, fixed/growing jet matching, KV fidelity, weighted reset complexity, repair width, high-order jet saturation, shrinking-window rank-one collapse, fixed-window factorial compression, spectral-logwidth compression, full-real-ray suppression, Robin-scale precision conversion, reciprocal total variation, Chebyshev-balanced signed response, vertical Fourier capacity, multiplicative shell aliasing, Diophantine recurrence rank, transient Robin displacement and destination leverage answer different questions.

RE-199 makes the positive-real separation especially concrete: an analytically injective full real continuum can remain exponentially almost blind at selector scale even after the number of exactly matched boundary jets grows like a fixed positive fraction of `log p`. RE-200 adds the complementary warning that low stable dimension is representation-dependent: complex phase can restore linear Euclidean capacity. RE-201 adds that stable dimension measured on one support shell does not imply global source coercivity when the sampling grid aliases shell index. RE-202 adds that breaking exact periodicity is still insufficient when the height family has low Diophantine rank: approximate common periods can remain cheaper than the source-fidelity budget. Future proposals should therefore state the surviving source ambiguity, exact invariant family, optimized repair width, source-fidelity cost, integer-multiplicity constraints, normalization, inverse conditioning, spectral/source diameter, alias period or quantitative anti-recurrence, **source-visible signed complexity rather than only unsigned reciprocal variation**, precision scale and selector-normalized destination effect. A scalar family should be credited as Robin leverage only after the present matched near-kernels are ruled out at the actual physical parameters.