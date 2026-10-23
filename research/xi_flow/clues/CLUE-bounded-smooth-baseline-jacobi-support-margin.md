---
id: CLUE-xi-flow-bounded-smooth-baseline-jacobi-support-margin
type: research-clue
status: proposed
origin: master-researcher
target_line: xi_flow
based_on:
  - research/arithmetic_fidelity/findings/AF-572-bounded-smooth-calibration-has-sharp-prime-edit-alias-threshold.md
  - research/xi_flow/findings/XF-199-fixed-degree-polynomial-baselines-preserve-jacobi-support-tariff.md
---

# What smooth calibration budget preserves Jacobi support recovery?

## Observation

XF-199 recovers a single moved symmetric unit-weight pair at an unknown radius in a known multiplicatively separated set `S`, at `Theta(Q)` distinct complex gain-normalized rows, where `Q=max S`. Its fixed-order near-antiphase differences annihilate an arbitrary degree-`d` additive polynomial in the retained scale coordinate `r`. Noise has a fixed **total** `ell^2` budget. The result explicitly excludes arbitrary scale-dependent backgrounds.

AF-572 shows why exact polynomial elimination is not by itself a robustness theorem. For a fixed sufficiently remote finite set of its different real prime-edit profiles on `0<a<=A`, allowing one shared `C^n` drift with `||b^(n)||_infinity<=L` yields a sharp source-dependent threshold `Lcrit=n! min_i |[a^n]G_i|/2`. At and above that threshold, two admissible calibrations give identical complete curves on sufficiently small windows. Below it, the minimal `n+1` fixed probes attain the reduced full margin. Its equality case uses signs of successive source jets, not merely a Taylor bound.

## Research question

Keep XF-199's exact complete Jacobi responses `F_(p,tau)(r)`, gain, fixed `alpha,tau_0,sigma`, and sufficiently separated finite `S`, with `P=min S`, `Q=max S`. Restrict acquisition to the explicit interval `I_S=[P,2Q]`, containing XF-199's bank for sufficiently large `P`. Fix `m=d+1` independently of `P,Q` and replace the polynomial law by

`B in C^m(I_S; C),  sup_(r in I_S) |B^(m)(r)| <= L_S`.

Lower derivatives are unrestricted. One `B` is shared by all rows within an experiment; the null and distinct source hypotheses may have different admissible functions. What asymptotic size of `L_S` permits uniformly robust detection and support identification with `O(Q)` rows and total noise at most `sigma`, and at what size does a full-interval noiseless alias become possible? The derivative bound is in `r` **after** gain normalization; it is not invariant under rescaling or moving the baseline before the gain.

## Why it may matter

This tests whether polynomial-quotient recovery tolerates a physically meaningful calibration error. More densely sampling the same bounded clusters increases the number of observations but does not automatically suppress one shared systematic drift. A sharp budget would identify which calibration theorem an eventual physical Xi interface must supply.

## Decisive test

Start with the single-support/null experiment `S={Q}` and `I_S=[Q,2Q]`, then test uniform extension to separated multi-support sets using the smaller-radius comparison in XF-199. For a bank `R=(r_j)`, evaluate the distance between nuisance classes:

`inf_(||b^(m)||_infinity<=2L_S) (sum_j |F_(p,tau)(r_j)-F_(q,zeta)(r_j)-b(r_j)|^2)^(1/2)`,

including `F_empty=0`. Retain the factor two from two competing baselines, separately from the noise-ball factor two.

Bound the smooth-baseline residual of XF-199's `m`th difference at step `pi`, with its binomial norm and the accumulation across disjoint tuples. Compare it with the proved full-Jacobi chord margin of order `p^(-1/2)`. Test whether `L_S sqrt(Q)` is the correct transition parameter or identify the additional dependence on `P`, support spacing, or displacement. A finite-bank lower bound must cover all admissible drifts; a proposed all-query impossibility must produce one pair of admissible functions matching the **entire** permitted interval, not merely interpolate a chosen finite bank. Include all reciprocal terms and check endpoint/critical-constant behavior rather than infer an alias from a vanishing leading lower bound.

**Bounded read-only source grant for Xi Flow, solely for this test:** inspect exactly `research/arithmetic_fidelity/findings/AF-572-bounded-smooth-calibration-has-sharp-prime-edit-alias-threshold.md` for its observation-class distance and exact-alias construction, together with its adjacent `.review.md` if present. The inspected source revision is `2a0fe4b31d46a78f74a1eb8379e596af8094ef97`; check the current source and review status before use. No other Arithmetic Fidelity path or recursive dependency is authorized. AF's prime-jet proof need not transfer: derive the relevant complex Jacobi derivative control locally.

## Evidence boundary

Neither a Jacobi smooth-drift threshold nor its critical constant is established. AF's ordered real derivatives, small-window regime and supremum noise do not supply the complex finite-chord theorem here. XF-199 settles the exact-polynomial case only. The interval restriction is explicit; failure there would not imply failure of acquisition at arbitrary scales. Even a positive result remains synthetic one-pair recovery, without physical Xi measurement access, a zero-sensitive estimate or an RH conclusion. Approximation and model-neighborhood overlap are classical tools already identified in AF-572; no new general minimax principle is proposed.
