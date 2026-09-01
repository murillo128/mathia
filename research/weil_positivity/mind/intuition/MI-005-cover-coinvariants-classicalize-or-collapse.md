# MI-005 — Zeroth cover coinvariants classicalize on the diagonal and collapse on full operator ideals

**Evidence level:** supported by exact Banach-quotient classifications

## Core intuition

Quotienting by the canonical root-cover transport does not provide a hidden positive home for the mixed-prime cancellation left by the Möbius primitive. At zeroth Hausdorff coinvariant level, the diagonal trace ideal remembers only ordinary trace; enlarging to the full trace/Schatten/compact operator ideals destroys even that scalar class. A viable cohomological or quotient repair must therefore add genuinely new module/action structure rather than merely identify canonical cover transports.

## Strongest justified principle

WP-079 considers the self-adjoint diagonal trace ideal with cover block-sum action `rho_n`. The closed span of all transport differences is exactly `ker Tr`; degree two already generates a dense subspace of that kernel. Hence the Hausdorff coinvariant quotient is canonically one-dimensional and every bounded transport-invariant readout factors through ordinary trace.

Applied to the positive defects and their Möbius primitives, this quotient gives `[Q_n]=(log n)[E_0]` and `[M_n]=Lambda(n)[E_0]`. Mixed-prime primitives disappear and prime-power classes remain positive, but only because **all** trace-zero operator geometry has been discarded. The apparent repair is therefore the classical scalar identity `Lambda=mu*log`, not a new cross-prime positive mechanism.

WP-080 shows that adding off-diagonal coherence does not enrich this quotient. For the canonical transfer `rho_n(X)=n W_n^* X W_n`, the norm-closed range of `I-rho_n` is the whole trace class for every `n>1`. By Schatten duality the same zeroth Hausdorff coinvariant collapse holds throughout the standard `S_p`/compact-operator scale. Every bounded invariant readout is zero; off-diagonal matrix units can feed trace-zero coherence into diagonal mass, so the trace class that survived on the diagonal cannot extend invariantly.

This gives a precise category boundary. Diagonal zeroth coinvariants **classicalize to trace**; full standard operator-ideal zeroth coinvariants **collapse to zero**. Neither can carry the missing finite--archimedean sign.

## What remains possible

Higher semigroup homology/cohomology, a nontrivial coefficient module, a different geometrically forced action, a selective quotient with an independently derived nullspace, or an unbounded/non-Hausdorff invariant could lie outside WP-079--WP-080. So could a nonseparable finite--archimedean construction formed before quotienting. Any such route must demonstrate which new information survives that is absent from the zeroth canonical coinvariants.

## Status / novelty

The quotient/annihilator identities and Schatten duality are standard functional analysis; the exact cover action and resulting diagonal-versus-full collapse are persisted Mathia findings. The synthesis is a no-go for the canonical zeroth coinvariant route, not for all cohomological constructions.

## Falsification criterion

Exhibit a non-trace bounded transport-invariant functional on the diagonal trace ideal, contradicting WP-079, or any nonzero bounded transport-invariant functional on the full trace class under the canonical action, contradicting WP-080. A positive advance must explicitly change the homological degree, coefficient module, action, or regularity category.

## Lean-formalizable core

- Density of `ran(I-rho_2)` in the diagonal trace-zero subspace.
- Duality proof that `ran(I-rho_n)` is dense in full `S_1`.
- Factorization of bounded invariant readouts through the coinvariant quotient.
