---
id: CLUE-weil-inertia-wang-endpoint-localization-cancellation
type: research-clue
status: resolved
origin: mind
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-354-short-interval-pair-correlation-has-a-support-localization-barrier.md
---

# Can a signed or smoothed zero-window localization beat Wang's endpoint support loss?

## Observation

Wang's current zero-window comparison contains an \(O(xL^3)\) localization error before the prime-polynomial mean-square step. The earlier coarse audit treated its support integral by replacing the fixed test with a uniform sup norm and therefore inferred an \(O(T^\lambda L^2)\) obstruction at the equality \(\lambda=\theta\).

WI-440 reconstructs the displayed proof without that loss. For the exact interval \(H=T^\theta\), a fixed \(g\in C_c^\infty\) supported in \([-\theta,\theta]\) satisfies \(g(\theta)=g'(\theta)=0\). Keeping this flatness inside the support integral turns the critical \(xL^3\) contribution into \(O_g(H)\). The other place where the source proof uses the strict gap can be handled with the unsimplified Montgomery--Vaughan bound, yielding an integrable \(HL/x\) cross term.

## Research question

The original decisive question had two levels: can the proof reach the boundary \(\lambda=\theta\), or can it go genuinely beyond it?

The first level is now settled positively without introducing a new localization scheme. The second remains genuinely stronger: for support extending into \(\alpha>\theta\), the current proof must control prime/localization scales \(x=T^\alpha>H\), where the displayed \(xL^3\) and \(x\log^2(2x)\) terms are no longer absorbed by the interval scale.

## Evidence boundary

The endpoint result is only for fixed smooth tests and exact \(H=T^\theta\). It does not prove a support-crossing theorem, does not cover uncontrolled \(T\)-dependent test families, and does not automatically extend the endpoint to every \(H=T^{\theta+o(1)}\).

## Research disposition

Outcome: narrowed

Resolved by:
- [[research/weil_inertia/findings/WI-440-smooth-test-flatness-reaches-wang-short-interval-endpoint]]

The strict endpoint obstruction was an artifact of the coarse final integration. The surviving research target is support genuinely beyond the interval exponent, where new cancellation/localization or stronger short-interval arithmetic is still required.