# MI-018 — Signed source complexity helps only through observation kernels that preserve sign regularity

**Evidence level:** supported by exact prime Prouhet controls, ordered sign-variation lower bounds, and the Euler total-positivity obstruction through AF-217

## Core intuition

Arithmetic provenance and oscillation complexity are different resources. Restricting support to distinct rational primes does not prevent arbitrarily high exact cancellation order: prime arithmetic progressions can carry Prouhet partitions of every prescribed order. A useful signed-source restriction must therefore control the **ordered variation of the coefficients**, not merely the arithmetic nature of the support.

AF-216 supplies an exact source-side complexity currency. An atomic signed source that annihilates `m` polynomial moments must have at least `m` ordered sign changes, and the same lower bound holds for a Dirichlet sum with `m` equally spaced real zeros. Bounded sign variation can therefore exclude arbitrarily high exact first-harmonic cancellation.

That source resource transfers only through an observation map that respects it. AF-217 shows that the full Euler-log kernel is not totally nonnegative of all orders: its bilateral transform contains the nontrivial zeta zeros, so the Schoenberg/Pólya-frequency criterion rules out all-order variation diminution. The stable-recovery problem must therefore match a **finite sign-complexity budget** to a finite-order/band sign-regularity theorem for the actual observation kernel.

## Strongest justified principle

AF-214 showed that integrality, simplicity, and unit multiplicity do not prevent arbitrary-order moment-flat controls. AF-215 strengthens the provenance test by placing the same Prouhet mechanism on genuine rational-prime support via prime arithmetic progressions. Primality alone is not an oscillation budget.

AF-216 proves the sharp qualitative converse: `m` exact moment cancellations force at least `m` sign changes. In Dirichlet form, exact zeros at `m` equally spaced real samples force the same ordered complexity. This gives a source-side obstruction to arbitrary exact cancellation whenever a separate theorem bounds sign variation.

AF-217 prevents silently promoting that obstruction to an all-order Euler transfer theorem. The Euler-log kernel cannot be a Pólya-frequency kernel of infinite order because its bilateral transform has zeros inherited from zeta. Thus a source sign budget and an observation sign-regularity order are separate parameters that must be proved to overlap quantitatively.

## Counterevidence / boundary

AF-216 is an exact-zero theorem. It does not by itself give a lower modulus for near-cancellation, and it does not prove that the actual prime-derived signed source has bounded sign variation at the scales needed by the application.

AF-217 is an all-order obstruction. It does not identify the first failing minor or rule out useful total positivity of some finite order on a declared scale, restricted mesh, or bandwidth. A finite-order variation-diminishing theorem could still combine with a source-forced finite sign budget to give quantitative recovery.

## Epistemic status

**Exact separation of arithmetic provenance, ordered source complexity, and observation-kernel sign regularity; no intrinsic prime sign-complexity bound or quantitative finite-order Euler modulus is yet established.**

## Falsification criterion

Produce a rational-prime support restriction that prevents the AF-215 arbitrary-order Prouhet controls, an `m`-moment signed source with fewer than `m` ordered sign changes, or an all-order totally nonnegative Euler-log kernel contradicting AF-217. A positive continuation should instead prove both a source-natural sign-complexity bound and a matching finite-order quantitative sign-regularity theorem for the declared observation regime.
