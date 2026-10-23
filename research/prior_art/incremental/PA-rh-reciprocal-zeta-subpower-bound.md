---
id: PA-rh-reciprocal-zeta-subpower-bound
type: prior-art
canonical_name: RH reciprocal-zeta subpower bound
aliases:
  - Littlewood–Titchmarsh reciprocal-zeta estimate
kind: conditional-bound
topics:
  - riemann-hypothesis
  - reciprocal-zeta
  - mellin-transform
---

# RH reciprocal-zeta subpower bound

## What it is

Assuming RH, for each fixed \(\sigma>1/2\) and \(a>0\),
\[
|1/\zeta(\sigma+it)|\ll_{\sigma,a}(1+|t|)^a.
\]
Flajolet–Vepstas display this classical estimate as equation (52), citing Titchmarsh, equation (14.2.6).

## Relation to RH / Mathia research

[[research/mobius_cancellation/findings/MC-520-rh-mellin-variance-closes-conditional-farey-window-target|MC-520]], equations (5)–(9), uses it to control the Mellin frequencies of a Möbius difference. The physical transform also needs the [[research/prior_art/mobius-summatory-criterion|RH Möbius-summatory bound]]. The ensuing variance estimate and Farey application are derived in MC-520, not asserted by the cited equation alone.

## Known scope and limits

RH is a hypothesis. Constants depend on the fixed distance from the critical line and on the positive exponent. This statement supplies neither a uniform limit at \(\sigma=1/2\) nor a logarithmic-loss short-interval variance theorem. It is distinct from the physical summatory criterion.

## Related prior art

[[research/prior_art/incremental/PA-saffari-vaughan-averaging|Saffari–Vaughan averaging]] is the separate window-conversion input used by MC-520.

## Evidence and provenance

- Philippe Flajolet and Linas Vepstas, *On differences of zeta values*, [author-hosted paper, equation (52), p. 15](https://algo.inria.fr/flajolet/Publications/FlVe06.pdf), arXiv:math/0611332v1.
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, second edition, revised by D. R. Heath-Brown (1986), equation (14.2.6), p. 337; attribution verified through the displayed reference above.
- Persisted lookup trigger: `research/mobius_cancellation/findings/MC-520-rh-mellin-variance-closes-conditional-farey-window-target.md`, analytic input and prior-art sections.
