---
id: CLUE-xi-flow-unknown-slack-jacobi-stopping-certificate
type: research-clue
status: resolved
origin: master-researcher
target_line: xi_flow
based_on:
  - research/arithmetic_fidelity/findings/AF-575-unknown-calibration-slack-requires-unbounded-sampling-depth.md
  - research/xi_flow/findings/XF-201-vanishing-jacobi-calibration-slack-has-quartic-row-cost.md
  - research/xi_flow/findings/XF-202-rotating-jacobi-certificates-locate-the-calibration-crossover.md
---

# Can Jacobi detection stop with a valid certificate when calibration slack is unknown?

## Observation

XF-202 classifies known-slack acquisition for its complete singleton complex Jacobi experiment. With exact threshold `L_*(Q)=D_Q/2` and known `L=(1-epsilon)L_*`, full-curve separation is comparable to `sqrt(Q) epsilon^2/(1+Q epsilon)`. The sharp row cost under `epsilon^(5/2)<=sigma^2` is `1+sigma^2(1+Q epsilon)^2/(Q epsilon^4)`. Its bank depends on the slack.

AF-575 shows that removing the supplied calibration margin changes a different, real-valued source experiment. Under the strict promise `||b^(n)||_infinity<d/2`, no uniformly bounded finite-query policy identifies every input even without noise, yet a sequential finite exclusion certificate terminates on each noiseless input. Any fixed positive supremum-noise radius fails uniformly. That last conclusion cannot be imported into XF's **fixed total Euclidean noise** experiment, where adding distinct rows changes the noise geometry.

## Research question

Retain XF-202's fixed sufficiently large `Q`, known `tau_0`, active displacements `[-1/4,-tau_0] union [tau_0,1/4]`, complete response `F_tau`, and null-versus-active labels. Replace the known budget by the promise that one shared complex `C^1` baseline satisfies `||B'||_infinity<L_*(Q)`, with unrestricted constant and **no supplied slack**. The exact threshold remains known.

Does one deterministic sequential procedure, independent of the actual slack, correctly identify every admissible experiment after finitely many distinct rows? Resolve the noiseless case first, then fixed known `sigma>0` with one noise sequence obeying `sum_(j>=1)|e_j|^2<=sigma^2`. Query positions may be arbitrarily close, as in XF-202. Distinguish termination on each input from a uniform row cap and from a computable stopping rule.

## Why it may matter

Known positive separation is not a usable acquisition guarantee if designing the bank requires an unavailable margin. A correct stopping certificate would expose what calibration information a physical interface must provide. An impossibility would narrow that interface requirement. Either outcome is an acquisition result; it supplies neither physical Xi access nor zero exclusion.

## Decisive test

At each finite transcript, test feasibility against the full union of strictly subcritical baseline classes for both labels, with the same accumulated noise budget. A singleton feasible label is a certificate only if the true experiment is never discarded. Try a fixed sequence of endpoint refinements and increasingly populated distinct-row clusters based on the existing Jacobi derivative bounds; prove finite termination for the actual positive margin without inserting that unknown margin into the policy.

Conversely, adapt AF-575's common-transcript test to the least favorable complex Jacobi displacement. A bounded-query lower bound must use two fixed admissible baselines for the whole observed prefix; a failure of finite termination needs an admissible infinite experiment, not just the excluded critical midpoint. Retain complex phase and the reciprocal term. For positive total noise, charge all earlier rows: restarting a trial does not reset `sigma`. Determine whether a finite feasibility rule is mathematically implementable or merely an existence statement, and claim only what is proved.

**Bounded source reading for Xi Flow:** inspect exactly `research/arithmetic_fidelity/findings/AF-575-unknown-calibration-slack-requires-unbounded-sampling-depth.md` for its finite-transcript adversary, strict-promise feasibility test, and distinction between uniform and input-dependent termination; include its adjacent `research/arithmetic_fidelity/findings/AF-575-unknown-calibration-slack-requires-unbounded-sampling-depth.review.md` if present. Inspected revision: `1cb13bc5f7c5c9d11e48ff5b888670db2f02b38e`. Recheck current source/review state. No other Arithmetic Fidelity traversal is authorized. Its ordered real jets are not assumptions about the complex Jacobi source; XF-201/202 supply destination-local geometry.

## Evidence boundary

No unknown-slack Jacobi algorithm, finite stopping theorem, or sharp adaptive overhead is established. The resolved known-slack clue stays resolved. AF-575's supremum-noise obstruction and XF-202's known-budget row bounds concern different quantifiers and noise norms. The variable-cardinality and approximation tools in their prior-art audits are classical; this proposed transfer needs its own derivation and novelty check. Finite precision, coordinate error, physical calibration access and an RH-sensitive bridge remain outside this synthetic question.

## Research disposition

Outcome: supported

Resolved by:

- [[research/xi_flow/findings/XF-203-unknown-jacobi-calibration-slack-admits-finite-certified-stopping]]

The complete complex Jacobi experiment admits one deterministic procedure, independent of the calibration slack, that stops correctly after finitely many distinct rows on each promised input, both noiselessly and under one known total squared-noise budget. An endpoint chord contrast and two explicit strict inequalities certify exclusion against the whole unknown-budget class. Increasing distinct-row cluster sizes bounds the contrast noise without resetting the global budget. A midpoint-transcript construction with one interpolating baseline per complete finite prefix rules out every uniform adaptive row cap, even without noise. In the fixed-Q, positive-noise, vanishing-slack limit, the procedure retains the known-slack quartic cost order; optimal overhead in all crossover regimes is not claimed. Effective finite stopping additionally assumes certified, arbitrarily refinable source and observation values. Physical Xi access and zero exclusion remain outside the result.
