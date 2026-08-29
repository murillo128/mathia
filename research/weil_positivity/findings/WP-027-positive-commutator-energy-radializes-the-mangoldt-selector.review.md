---
type: adversarial-review
target: research/weil_positivity/findings/WP-027-positive-commutator-energy-radializes-the-mangoldt-selector.md
---

# Adversarial review

## Adversary

The Clifford calculation itself is convincing: equations (8), (10), and (12) show exactly that `C_alpha^2` and `|C_alpha|` collapse to the scalar radius `A(n)`, and equations (13)--(14) correctly classify scalar spectral functions of `C_alpha` and their full Boolean supertrace. The finding, however, appears to overextend those facts to **positive spectral functional calculus of the single commutator in general**.

A direct counterexample is the fixed nonnegative scalar function

\[
f(t)=t_+:=\max(t,0).
\]

Since `spec(C_alpha)={-A(n),+A(n)}`, functional calculus gives

\[
\boxed{
(C_\alpha)_+
=\frac{A(n)I+C_\alpha}{2}\succeq0.
}
\]

For `|S|\ge2` this operator is not radial/scalar: its off-diagonal part is exactly `C_alpha/2`, so it still carries the weighted oriented Boolean edge differential and the individual coefficients `log p`. Thus positivity obtained by spectral functional calculus does **not** by itself erase the directional/incidence information. What radializes automatically is the even functional calculus (equivalently functions of `C_alpha^2`), including the square and modulus.

The subsequent trace statements do not close this gap. The ordinary full trace of `(C_alpha)_+` depends only on `A(n)`, and its Boolean supertrace vanishes, exactly as Section 4 says; but those are two particular readouts. They do not prove that every positive pairing, compression, boundary functional, or other canonical use of a positive `f(C_alpha)` must factor only through `A(n)`. Indeed the finding's own boundary section leaves incidence-sensitive compressions open, and `(C_alpha)_+` shows that such information is still present after a positive spectral operation.

This is material because the status paragraph and Section 4 currently say that applying positive spectral functional calculus to the single commutator destroys the Boolean information and that "spectral positivity of the single commutator cannot recover the Boolean cancellation." The stored derivation establishes the stronger no-go only for `C^2`, `|C|`, other even/radial functions, and for the specific ordinary-trace / Boolean-supertrace readouts analyzed there.

Resolve the objection either by narrowing the durable claim to those operations/readouts, or by supplying an additional theorem showing that every admissible **canonical positive readout** of a general positive `f(C_alpha)` necessarily loses the oriented Boolean information or cannot reproduce Mangoldt support. The counterexample above does not claim that `(C_alpha)_+` already yields such a readout; it shows that positivity alone has not yet proved the asserted radialization/no-go.