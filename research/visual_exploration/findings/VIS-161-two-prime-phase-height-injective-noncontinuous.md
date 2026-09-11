# VIS-161 — two exact prime phases encode height only through a discontinuous inverse

## Claim

Let `p != q` be two distinct rational primes and define the two-prime phase map

`Phi_(p,q)(t) = (p^(-it), q^(-it)) in T^2`.

Then three facts hold simultaneously.

First, `Phi_(p,q)` is injective. If `Phi_(p,q)(t)=Phi_(p,q)(u)`, then for `Delta=t-u`

`Delta log p in 2 pi Z`,
`Delta log q in 2 pi Z`.

If `Delta != 0`, their ratio would force `log p/log q in Q`, hence `p^a=q^b` for nonzero integers `a,b`, contradicting unique factorization. Therefore `t=u`.

Second, the image is dense in `T^2`, but the inverse

`Phi_(p,q)^(-1) : Phi_(p,q)(R) -> R`

is nowhere continuous. Indeed, irrationality of `log q/log p` gives integers `n_j -> infinity` with

`|| n_j log q/log p ||_(R/Z) -> 0`.

Putting `t_j=2 pi n_j/log p` gives

`Phi_(p,q)(t_j) -> (1,1)=Phi_(p,q)(0)`

while `t_j -> infinity`. Translation by any fixed height gives the same failure at every point of the orbit.

Third, every same-height observable `A(t)` factors **set-theoretically** through this two-phase orbit:

`A(t) = A_tilde(Phi_(p,q)(t))`

with a unique `A_tilde` defined on `Phi_(p,q)(R)`. This factorization is therefore information-theoretically vacuous unless a regularity or complexity class is imposed on the decoder. In particular, if a complex-valued decoder extends continuously to all of `T^2`, then its pullback along `Phi_(p,q)` is bounded and Bohr almost periodic: uniform trigonometric approximation on the torus pulls back to finite sums with frequencies `m log p+n log q`.

Thus an added same-height analytic coordinate cannot be called an "independent information source" merely because it is not an obvious finite prime-phase formula. With exact infinite-precision phases, two primes already identify the height. The meaningful question is whether the coordinate is recoverable **stably and within a predeclared regular/complexity-bounded representation class**.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL KRONECKER/QUASIPERIODIC SPECIALIZATION + REPRESENTATION-OBSTRUCTION + NO-NOVELTY-CLAIM`.

No new theorem about Kronecker flows, almost-periodic functions, zeta values, Hardy `Z`, zero statistics, or RH is claimed.

## 1. Two primes already separate real heights

Equality of the first phase gives

`Delta log p = 2 pi m`

for some integer `m`, and equality of the second gives

`Delta log q = 2 pi n`.

If either `m` or `n` is zero, then `Delta=0` immediately. Otherwise

`log p/log q = m/n`,

so after clearing signs and denominators one obtains an equality of positive integer powers of two distinct primes. Unique factorization forbids this. Hence the two-phase coordinate is injective on the entire real height axis.

This is much stronger than saying that finitely many prime phases distinguish generic heights or almost every height. At exact precision the pair distinguishes **every** real height.

## 2. Exact identifiability is maximally ill-conditioned

Injectivity does not make `Phi_(p,q)` a topological embedding. Let

`alpha = log q/log p`,

which is irrational. Classical irrational-rotation recurrence supplies positive integers `n_j -> infinity` with fractional parts of `n_j alpha` tending to zero. At

`t_j = 2 pi n_j/log p`,

the `p` phase is exactly one and the `q` phase tends to one. Thus arbitrarily large heights return arbitrarily close to the phase pair at height zero.

For an arbitrary `t_0`,

`Phi_(p,q)(t_0+t_j) = Phi_(p,q)(t_0) Phi_(p,q)(t_j) -> Phi_(p,q)(t_0)`,

while `|t_j| -> infinity`. Therefore the inverse is discontinuous at every orbit point.

This gives the representation-level boundary that raw information counting misses. An exact phase pair contains the height, but no uniformly stable local inverse exists. Any finite-resolution picture necessarily aliases sufficiently distant heights.

## 3. Continuous torus decoders form a much smaller information class

Suppose `F:T^2->C` is continuous and set

`A(t)=F(Phi_(p,q)(t))`.

Compactness makes `F` bounded, so `A` is bounded. More structurally, trigonometric polynomials are uniformly dense in `C(T^2)`. A torus monomial

`z_1^m z_2^n`

pulls back to

`exp(-it(m log p+n log q))`.

Hence `A` is a uniform limit of finite trigonometric sums in `t`, i.e. a Bohr almost-periodic function. Continuous phase decoders therefore occupy a strict regularity class even though arbitrary functions on the dense orbit can encode anything about height.

The same distinction persists for stronger practical decoder classes such as Lipschitz maps, bounded Fourier degree, bounded character complexity, finite partitions, or finite numerical resolution. Each imposes structure that the bare injective map does not provide.

## 4. Why this does not contradict Haar and joining controls

`VIS-071` proves that fixed finite prime-phase fields have the shared-phase Haar law under long vertical averaging. `VIS-083` and the later Gram findings push that control through increasingly elaborate deterministic sampling geometries. None of those statements requires the orbit map to be noninjective.

Likewise, `research/prime_lattice/findings/PL-070-prime-zero-kronecker-joining-intersection.md` classifies **continuous compact-dynamical** same-time couplings by common eigenfrequencies. The present result does not create a hidden continuous coupling. Its inverse is precisely noncontinuous, so set-theoretic recovery of height lies outside the compact-character observable class used by that joining theorem.

This distinction is essential: a dense one-parameter orbit can be injective as a parameterization while its invariant population law is still Haar and while continuous observables forget stable pointwise height recovery.

## 5. Prior art and novelty boundary

The density/recurrence input is classical Kronecker theory. The *Encyclopedia of Mathematics*, **Kronecker theorem**, records the rational-independence criterion for dense and uniformly distributed torus rotations. Rational independence here reduces elementarily to unique factorization of distinct primes.

The regular-decoder boundary is classical quasiperiodic/almost-periodic analysis. The *Encyclopedia of Mathematics* entries **Quasi-periodic function** and **Bohr almost-periodic functions** describe continuous torus-type quasiperiodic pullbacks and their almost-periodic closure. `VIS-071` already uses the same Kronecker/Bohr background for finite prime vertical flow.

The Mathia-specific contribution is only the representation audit: the accepted visual clue had treated an analytic coordinate as potentially carrying information "absent from" the exact prime-phase state. The two-prime injectivity calculation shows that absence of raw information is the wrong discriminator. The unresolved and scientifically meaningful discriminator is regular, stable, complexity-controlled recoverability.

## 6. Boundaries and falsification

The result assumes exact phases with infinite precision. It does not provide a numerically stable height decoder; in fact the recurrence argument proves the opposite. It does not say that a finite-support Euler product determines zeta values, Hardy `Z`, derivatives, or zero geometry by a continuous, smooth, low-complexity, or computationally usable formula.

The set-theoretic factorization `A=A_tilde o Phi` places no useful regularity on `A_tilde`. A difficult analytic coordinate may correspond to a violently discontinuous function on the dense two-phase orbit and may fail to extend continuously to the torus. Establishing such a regularity separation for a specific zeta-facing observable remains a genuine research question.

The finding also does not rule out sampling-based escapes from `VIS-160`, where test complexity grows jointly with height. It only corrects the alternative "independent analytic coordinate" branch by identifying the decoder class as load-bearing.

Falsify injectivity by producing `t != u` with both `p^(-it)=p^(-iu)` and `q^(-it)=q^(-iu)` for distinct primes. Falsify the noncontinuity statement by giving a neighborhood of any orbit point whose phase preimage excludes all sufficiently distant heights; the irrational-return sequence above rules this out. Falsify the continuous-decoder claim by exhibiting a continuous `F` on `T^2` whose pullback is not a uniform limit of trigonometric polynomials.

## Research consequence

The accepted prime-phase recursive-geometry clue should no longer ask whether a same-height analytic coordinate is merely "measurable from" or contains raw information absent from the exact phase state. At infinite precision that test is too weak: two prime phases already encode height set-theoretically.

A meaningful positive route must instead freeze a decoder/representation class and prove separation there. Examples include a quantitative lower bound against bounded Fourier/character complexity, a modulus-of-continuity or Lipschitz obstruction, a finite-resolution reconstruction lower bound, or another predeclared stable class under which Hardy `Z`, zero occupancy, derivatives, or nearby-zero geometry cannot be reproduced from the admitted prime-phase/clock state. Such a theorem would identify genuinely usable analytic structure rather than exploit the pathological exact inverse of a dense Kronecker orbit.
