---
id: CLUE-mobius-cancellation-explicit-cubefree-burgess-moving-order-prime-hm
type: research-clue
status: proposed
origin: research-watch
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-323-varying-modulus-prime-halasz-montgomery-forces-quadratic-source-saturation.md
  - research/mobius_cancellation/findings/MC-329-fixed-common-modulus-bias-energy-has-a-quartic-horizon.md
---

# Can explicit cubefree Burgess constants make the prime Halász–Montgomery boundary quantitative?

## Observation

`MC-323` and `MC-329` use Schlage-Puchta's prime Halász–Montgomery inequality with an arbitrary fixed Burgess order when the relevant modulus is cubefree. They deliberately keep the approach to the quadratic varying-modulus boundary and quartic common-modulus boundary non-uniform: Schlage-Puchta writes the character-sum input with an unspecified constant `c_{k,epsilon}`, so those findings can take any fixed deficit from the endpoint but cannot let `k` grow with the prime-shell scale.

A later primary manuscript removes part of that opacity. Hasanalizade, Lin, Martin, Luna Martínez and Treviño, *Explicit Burgess inequalities for cubefree moduli*, arXiv:2511.17778v1 (21 November 2025), Theorem 1.1, gives for primitive characters modulo cubefree `q` and every integer `r>=3` an explicit Burgess inequality of the form

\[
|S_\chi(M,N)|
\le C(r)N^{1-1/r}q^{(r+1)/(4r^2)}(\log q)^{1/(2r)}
\left((4r)^{\omega(q)}m_r(q)\right)^{1/(2r)-1/(2r^2)}
\left(\frac q{\phi(q)}\right)^{1/r},
\]

provided

\[
q\ge \max\{10^{1145},\exp(\exp(a(r)))\},
\]

where `a(r)` is explicit, `C(r)` is tabulated (and bounded by `1.869` for `r>=10` in the stated table), and

\[
m_r(q)=\min\left\{\tau_{2r}(q),\left(\frac{\tau(q)}2\right)^{2r-1},\frac q{2r}\right\}.
\]

Thus the raw Burgess constant is no longer the only reason that `k` had to remain fixed. The theorem itself permits `r=r(q)` as long as its explicit lower bound on `q` is met. Since `a(r)` grows linearly in `r` up to a logarithmic correction, this admits at least the possibility of orders on the scale `r=O(\log\log q)`.

This does **not** immediately upgrade `MC-323` or `MC-329`. Schlage-Puchta's Proposition 9 inserts Burgess into a Selberg-sieve convolution, and Theorem 3 then feeds those bounds through a Hilbert-space/large-value step. The endpoint characters used by Mathia can also be induced from proper primitive conductors. The new explicit Burgess theorem carries modulus-complexity factors through `omega(q)`, `m_r(q)` and `q/phi(q)`. Those factors, the imprimitive-character reduction, and the constants in the sieve convolution must all be propagated before any moving-order prime-character estimate is legitimate.

## Research question

Redo exactly the Burgess-dependent part of Schlage-Puchta Proposition 9 and Theorem 3 using the explicit cubefree inequality, with all dependence on `r`, `omega(q)`, `tau_j(q)` and induction from primitive conductors retained. Determine whether this produces a **uniform moving-order prime Halász–Montgomery estimate** in either of the two regimes already owned by the line:

- fixed common modulus `q`, approaching `q=y^4` from below as `q<=y^{4-delta(y)}`;
- varying primitive moduli `q_chi<=Q`, approaching `Q=y^2` from below as `Q<=y^{2-delta(y)}`.

The target is not to cross the exponents `4` or `2`: `MC-329` already proves from the Burgess exponent itself that moving the order cannot yield a fixed-power gain beyond the quartic common-modulus horizon. The target is to determine the strongest **effective shrinking deficit** `delta(y)->0` that survives all explicit factors, especially for the squarefree lower-prime source moduli actually arising in the endpoint construction.

## Why it may matter

The current findings know that every fixed subquadratic primitive-conductor range and every fixed subquartic common-modulus range are controlled, but they intentionally leave the rate of approach unresolved. The 2025 explicit Burgess theorem changes the prior-art boundary: the missing ingredient is no longer simply "explicit Burgess constants". It is now the more precise question of whether those constants and arithmetic factors survive Schlage-Puchta's prime-sieve transfer at a useful moving order.

A positive answer would not prove a Mertens bound, but it could turn qualitative `y^{2-o(1)}` / `y^{4-o(1)}` source boundaries into quantitative ones and test whether near-boundary alternative source representations remain genuinely available. A negative answer would be equally useful if it identifies the exact modulus-complexity or sieve factor that forces `delta` to remain fixed.

## Decisive test

Start from Schlage-Puchta Proposition 9, not from Theorem 3 as a black box. Replace each incomplete character-sum invocation by the explicit theorem and bound the Selberg-sieve convolution explicitly. For the elementary lcm sum that appears after expanding the sieve weight, retain its `r` dependence rather than hiding it in `O_r(1)`. Then handle induced characters explicitly and propagate the resulting off-diagonal bound through Bombieri's Hilbert-space lemma.

After obtaining a candidate formula, optimize `r=r(y)` jointly with the source-modulus complexity. Test at least the worst squarefree-modulus bound and the structurally relevant lower-prime source packages. Keep the direction only if one obtains a rigorously shrinking `delta(y)` with a nontrivial normalized bias-energy saving. Kill or narrow it if `(4r)^{omega(q)}m_r(q)`, imprimitive induction, the sieve convolution, or the theorem's condition `q>=exp(exp(a(r)))` consumes the putative gain.

## Evidence boundary

The explicit Burgess inequality is a primary-source theorem statement in an arXiv v1 manuscript; it is not being treated here as a peer-reviewed result. Its displayed theorem is for primitive characters. No uniform prime Halász–Montgomery estimate with growing order has been derived here, and no claim is made that Schlage-Puchta's full constant dependence is already controlled.

In particular, the existence of explicit Burgess constants does not alter the fixed-power horizon proved in `MC-329`, does not supply a cheaper-to-minimum-conductor bridge for `MC-372`, and does not imply any new bound for `M(x)`. The clue is only a now-concrete audit path for the previously qualitative moving-order boundary.
