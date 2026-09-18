---
id: CLUE-visual-wang-fixed-source-packet-localization
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-283-wang-fixed-source-cross-frequency-separation.md
  - research/visual_exploration/findings/VIS-284-wang-fixed-source-packet-projection-bound.md
  - research/visual_exploration/findings/VIS-285-wang-q-zero-source-observable-analytic.md
  - research/visual_exploration/findings/VIS-286-wang-large-source-diagonal-linearizes.md
  - research/visual_exploration/findings/VIS-287-wang-fixed-power-source-escape-linear.md
  - research/visual_exploration/findings/VIS-288-wang-fixed-power-residual-h-frontier.md
  - research/visual_exploration/findings/VIS-289-wang-fixed-power-residual-o-h.md
  - research/visual_exploration/findings/VIS-290-wang-fixed-power-classical-pnt-envelope.md
  - research/visual_exploration/findings/VIS-291-wang-fixed-power-korobov-vinogradov-envelope.md
  - research/visual_exploration/findings/VIS-292-wang-symmetric-smoothing-green-resolvent.md
  - research/visual_exploration/findings/VIS-293-wang-source-dirichlet-rh-half-plane.md
  - research/visual_exploration/findings/VIS-294-wang-lower-moving-source-sqrtlog-crossover.md
  - research/visual_exploration/findings/VIS-295-wang-gamma-subtracted-residual-relative-crossover.md
  - research/visual_exploration/findings/VIS-296-wang-relative-boundary-reduces-to-explicit-formula-remainder-mean.md
  - research/visual_exploration/findings/VIS-297-wang-boundary-remainder-mean-is-gamma-normalization.md
  - research/visual_exploration/findings/VIS-298-wang-gamma-recentering-removes-moving-h-barrier.md
  - research/visual_exploration/findings/VIS-299-wang-pointwise-moving-ceiling-h-over-log-cubed.md
  - research/visual_exploration/findings/VIS-300-wang-localization-cross-coherence.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

`VIS-283`--`VIS-291` isolate Wang's source channel and show that fixed-interior packet localization does not create new information: the complete statistic on compact power panels reduces to the linear source law plus the classical Korobov--Vinogradov arithmetic envelope. `VIS-292` and `VIS-293` then rule out two cheap escapes: the symmetric smoother has no exact blind frequency, while excluding all poles of the squared-von-Mangoldt source transform in `Re(s)>1/2` is already RH-equivalent.

`VIS-294`--`VIS-298` close the apparent moving lower-source boundary. Exact gamma recentering removes the square-root-log `H` barrier and yields

`F_I(x) = (H/(2*pi))[log x + (L-log(2*pi))^2/x^2] + o(H)`

for every moving `x->infinity` below one fixed exponent ceiling.

`VIS-299` removes that fixed exponent gap as a **pointwise** obstruction. Re-running Wang's localization proof rather than substituting a moving theorem parameter shows that the same asymptotic holds whenever

`x L^3 / H -> 0`.

Equivalently, for `x=T^beta(T)`,

`(theta-beta(T))L - 3 log L -> +infinity`.

Thus `beta(T)` may approach `theta`; the first unresolved upper layer in the current proof is where the explicit localization remainder `O(xL^3)` reaches `H` scale, around `x asymp H/L^3`.

`VIS-300` now isolates that layer exactly. With `R_I=A-A_I`, Wang's Lemma 2.3 gives

`2*pi F_I - integral_I |A|^2`
` = integral_(R\I)|A_I|^2 - 2 Re integral_I A_I overline(R_I) - integral_I|R_I|^2`.

Both pure leakage energies are only `O(xL^2)`. Therefore for every `x=O(H/L^3)` they are already `o(H)`, and after inserting the interior expansion the complete `H`-scale ambiguity is

`C_I(x)=Re integral_I A_I(x,t) overline(A(x,t)-A_I(x,t)) dt`.

The extra factor `log H` in Wang's `O(xL^3)` estimate enters only when this bilinear term is bounded by absolute values. The upper source problem is consequently an inside--outside coherence problem, not a tail-mass problem.

## Research question

Two genuinely distinct source routes remain.

For the **fixed-power real-axis source**, is there a property of

`mu=sum Lambda(n)^2/n delta_(log n)`,

strictly weaker than the RH-equivalent half-plane pole exclusion of `VIS-293`, that improves the generic Korobov--Vinogradov envelope and survives Wang's complete error budget?

For the **upper localization layer**, does the bilinear coherence

`C_I(x)=Re integral_I A_I(x,t) overline(A(x,t)-A_I(x,t)) dt`

satisfy `C_I(x)=o(H)` when `x asymp H/L^3`, or does it have a deterministic or oscillatory `H`-scale correction? If it is small, what zero-phase or endpoint structure forces that cancellation? If it is not small, can its leading term be identified and separated from genuinely arithmetic source information?

A genuinely bounded source `x=O(1)` remains separate. A moving-support version of Wang's integrated Theorem 2.2 is also separate: `VIS-299` controls the pointwise source statistic and does not establish uniformity for a test function whose support changes with `T`.

## Why it may matter

The source-scale search space has been compressed substantially. Neither the moving lower boundary nor a fixed exponent gap below `theta` is a live pointwise obstruction, and `VIS-300` rules out pure localization leakage as the explanation for the first remaining boundary. Any upper-source signal within Wang's present framework must now enter through one explicit bilinear coherence or through arithmetic information stronger than the generic PNT envelope.

This gives a much sharper target than improving a global `O(xL^3)` remainder. A proof that `C_I=o(H)` at the boundary would extend the `VIS-299` asymptotic without needing smaller tail energy; a nonzero `H`-scale limit would instead identify the actual endpoint-localization correction that the present absolute-value proof hides.

## Decisive test

For the fixed-power branch, state a concrete real-axis estimate or secondary expansion for `S(x)-log x`, derive it from arithmetic information strictly weaker than the pole exclusion of `VIS-293`, and propagate it through all `D_x`, gamma/zeta, localization, and cross-term errors. Kill the route if the gain is only a generic PNT substitution, smoothing attenuation, an RH-equivalent continuation assumption, or a term swallowed by another Wang remainder.

For the upper branch, analyze `C_I(x)` directly in the moving range `x asymp H/L^3`. Keep the interval/exterior split explicit and preserve the oscillatory factor carried by the zero kernel rather than replacing it immediately by absolute values. A decisive outcome is one of:

- prove `Re C_I=o(H)` from unconditional zero information already available;
- derive a stable deterministic `H`-scale correction and show how it modifies the pointwise asymptotic;
- construct a mathematically admissible matched zero model with the same relevant local density/correlation constraints in which an `H`-scale cross term survives, showing that additional arithmetic input is necessary.

Do not count a smaller `L^2` bound for `A-A_I` or exterior `A_I` as progress by itself; `VIS-300` already shows those masses are `o(H)` at the boundary. Kill the upper route if every proposed improvement implicitly assumes the desired pair-correlation/zero-distribution conclusion, or if the coherence term is reproduced generically by an admissible non-arithmetic control.

Do not reopen a moving lower-source branch unless a new hypothesis invalidates the exact recombination of `VIS-298`; changing only the rate at which `x->infinity` is not such a hypothesis.

## Evidence boundary

`VIS-283`--`VIS-299` establish reductions, negative controls, exact decomposition identities, normalization corrections, closure of the moving lower-source branch, and extension of the **pointwise** source asymptotic through every `x=o(H/L^3)`. `VIS-300` further establishes that at `x=O(H/L^3)` both pure leakage energies are `o(H)` and the only remaining `H`-scale localization term is the inside--outside bilinear coherence `C_I(x)`.

None of these findings determines the sign, size, or asymptotic law of `C_I` at the boundary. They also do **not** improve the Korobov--Vinogradov arithmetic input, control a genuinely bounded source by the same formula, or prove a moving-support version of Wang's integrated pair-correlation theorem.

In particular, `H/L^3` remains a proof boundary, not an established transition of `F_I`.

## Research disposition

Outcome so far: **narrowed to one bilinear localization observable**.

The moving lower-source branch remains closed. The pointwise upper-ceiling branch no longer asks for a generic improvement of Wang's tail bounds: it asks whether the inside field and the outside-zero tail are asymptotically orthogonal at absolute `H` resolution, or what correction replaces orthogonality. The separate fixed-power source-specific arithmetic question remains live.