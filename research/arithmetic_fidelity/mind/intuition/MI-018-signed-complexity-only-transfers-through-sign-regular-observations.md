# MI-018 — Signed complexity transfers only through a quantitatively sign-regular observation window

**Evidence level:** exact source sign-complexity and Euler-log sign-regularity results through AF-220

## Core intuition

A source sign budget is useful only when the observation kernel has a matching finite-order variation-diminishing modulus at the scale actually occupied by the source. Global all-order positivity is unnecessary, but qualitative finite-order positivity without a separation modulus is also insufficient.

## Strongest justified principle

AF-216 gives the sharp source currency: exact cancellation of `m` ordered moments/Dirichlet samples forces at least `m` sign changes. AF-217 rules out total nonnegativity of the full Euler-log kernel as a universal rescue. AF-218 and AF-219 establish global strict sign regularity through orders two and three. AF-220 then shows that for every prescribed finite order, positive curvature together with sufficient coordinate separation yields strict sign regularity on compact interaction windows.

Thus the next bridge is not “prove the kernel totally positive.” It is to match a source-forced finite sign budget to a scale where the Euler kernel has a quantitative finite-order determinant margin that survives tail refinement and inversion.

## Counterevidence / boundary

AF-220 does not give global order-four positivity and its separation condition can fail as prime differences become dense. Arbitrary-order Prouhet constructions remain available on genuine prime support, so a fixed observation order cannot control an unbounded source sign budget.

## Epistemic status

**Supported finite-order synthesis; the tail-uniform quantitative modulus needed for an RH-facing recovery theorem remains open.**

## Falsification criterion

Show that every source-relevant tail window necessarily violates the separation/curvature condition before reaching the required sign order, or construct a bounded-sign-complexity source theorem whose required determinant margin cannot be obtained from AF-220. A positive result should prove the matched source-budget/observation-modulus estimate with explicit scale dependence.