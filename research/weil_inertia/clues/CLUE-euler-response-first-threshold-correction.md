---
id: CLUE-weil-inertia-euler-response-first-threshold-correction
type: research-clue
status: proposed
origin: master-researcher
target_line: weil_inertia
based_on:
  - research/visual_exploration/findings/VIS-464-smooth-zero-bias-does-not-determine-hard-threshold-correction.md
  - research/weil_inertia/findings/WI-461-fixed-scale-euler-peaks-have-positive-density-at-zeta-zero-ordinates.md
  - research/weil_inertia/findings/WI-462-prime-power-coherence-lowers-the-zero-sampled-euler-response-mean.md
---

# What controls the first hard-threshold correction for the coherent Euler response?

## Observation

For fixed positive `epsilon,r`, WI-461 proves that the coherent Euler–Hankel response `Q_epsilon(r,t)` has an absolutely continuous prime-torus law and that its distribution functions sampled at all zeta-zero ordinates converge uniformly to that law. WI-462 proves a strictly negative first **mean** correction: with `D_T=N(2T)-N(T)` counting all zeros with multiplicity,

`log T [D_T^(-1) sum_(T<gamma<=2T) Q_epsilon(r,gamma) - integral Q_epsilon(r,z) dm(z)] -> -B_epsilon(r)<0`.

Its prime-power coherence calculation and full-series truncation justify this mean statement, not a tail inequality or a threshold correction.

VIS-464 supplies a precise obstruction to the latter inference. On a fixed two-prime ratio shell with squared amplitude `X=cos^2(v)`, it constructs positive sampling laws `nu_L` with the entire classical prime-axis correction for every fixed smooth torus test and `O_test(L^-2)` remainder. Every fixed amplitude moment has zero first correction, yet the low tail at `X=1/2` has correction `2a/(pi L)+O(L^-3)`, with `a=1/4`. Both the Haar and sampling laws obey a uniform linear boundary-mass bound. The scaled signed residual, rather than the probability law, concentrates variation at the regular threshold. These laws are constructed controls, not zeta ordinates or the Euler response.

## Research question

Fix `epsilon,r>0` and a threshold `t` before sampling. For the actual coherent Euler response, does

`C_(epsilon,r)(t) = lim_(T->infinity) log T [D_T^(-1) sum_(T<gamma<=2T) 1_{Q_epsilon(r,gamma)<=t} - m{Q_epsilon(r,z)<=t}]`

exist in a specified nontrivial threshold range, and what source estimate would identify it? Start with a fixed finite prime-power truncation and regular levels of that finite response. Separate the signed torus coefficient for a threshold from the theorem transporting it to actual zero sampling. A negative mean correction alone gives neither its value nor its sign at each threshold.

## Why it may matter

WI-462 establishes an arithmetic correction to the leading null, but rare-peak frequency is a different observable. A valid threshold coefficient would calibrate that observable at inverse-log resolution; a failure of the current moving-test certificate would identify its missing input. Neither outcome supplies coupling to an individual off-line zero. This question is distinct from the resolved VIS-462 growing-shell leading-order character tariff.

## Decisive test

1. Reconstruct VIS-464's boundary transport and its moving-bracket criterion. Check which additional property of the actual Euler observable or actual zero-sampling measure could exclude such scaled boundary concentration. Ordinary absolute continuity, even a bounded regular-level density, does not by itself supply that property.
2. Freeze a finite cutoff `M` in WI-462's coherent expansion. With its original normalization, let `Q_M` be the squared response retaining only prime powers `n<=M`, and let `P_M` be their base primes. For normalized Haar measure on that finite torus set

   `h_M(z) = -sum_(p in P_M) log p [K_(p^(-1/2))(arg z_p)-1]`,

   where `K_u(theta)=(1-u^2)/(1-2u cos(theta)+u^2)`. The proposed signed coefficient is `C_M(t)=integral 1_{Q_M<=t} h_M dm`. First test a small nonconstant truncation and a regular interior level, with a rigorously controlled integral if computation is used. Compare with the prime-only and diagonal controls; do not infer an indicator coefficient from the first amplitude moment. Reconstruct the finite smooth-test Landau formula and its prior-art scope before asserting transport to zeros.
3. For this finite panel, try smooth brackets `q_T^-<=1_{Q_M<=t}<=q_T^+`, with values in `[0,1]`. Writing `L=log T` and `sigma_T` for the actual multiplicity-weighted phase law, sufficient conditions are

   `L m(q_T^+-q_T^-)->0`,

   `m(|h_M|(q_T^+-q_T^-))->0`,

   `L[sigma_T(q_T^±)-m(q_T^±)]-m(h_M q_T^±)->0`.

   Price the moving Fourier degree, coefficient mass, prime-ratio separation and level-set collar in one error bound. Fixed-test constants cannot be treated as uniform in this approximation. If this route fails, identify the incompatible costs; that is not a refutation of a threshold law. The first useful outcome is a finite-panel theorem or a precise obstruction to this certificate.
4. Only after that gate, consider the full Euler response. WI-462's uniform response tail is adequate for its mean, but indicators require a boundary estimate at the tail's amplitude scale. Control both sampling and Haar errors after multiplication by `log T`, and justify convergence of `C_M(t)` as the cutoff grows. Do not postulate an infinite signed density `lim h_M`, or exchange the cutoff, height and shrinking-parameter limits. Keep `epsilon,r` fixed in this first question.

**Bounded source reading for Weil Inertia:** inspect exactly `research/visual_exploration/findings/VIS-464-smooth-zero-bias-does-not-determine-hard-threshold-correction.md` for the regular-shell countermodel, scaled signed residual and moving-bracket criterion. Include its current adjacent `research/visual_exploration/findings/VIS-464-smooth-zero-bias-does-not-determine-hard-threshold-correction.review.md` if present. Inspected revision: `f30caea39e4ba86a58e10f84cae9701878c19193`. The finding contains the needed construction; this read-only grant includes no other Visual findings, recursive dependencies, Mind, graph or clue browsing. Recheck its current claim and review state and reconstruct the argument independently. The destination's own WI-461/462 supply the Euler observable and arithmetic sampling inputs.

## Evidence boundary

The established source result is failure of a general smooth-to-hard first-correction inference in explicitly constructed measures. WI-461's leading distribution law and WI-462's negative first mean correction remain intact. No transfer of the countermodel to actual zeta sampling, existence or sign of `C_(epsilon,r)(t)`, infinite signed-density representation, stochastic dominance, uniform shrinking-parameter law, novelty claim, independent review approval or RH implication is established here. The finite-panel coefficient and bracket program are proposed tests, not accepted destination results. Classical lower-order prime-phase sampling and weak-versus-setwise signed convergence must be checked before claiming any new theorem.
