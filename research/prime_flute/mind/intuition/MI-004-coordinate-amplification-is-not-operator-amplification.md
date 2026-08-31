# MI-004 — The all-composite shift clone is compact-resolvent equivalent, and the remaining gap is two-dimensional rather than a hidden boundary mode

**Evidence level:** supported; compact relative resolvent and one-dimensional trace controls are exact, stronger global relative classes remain open

## Core intuition

Large Fenchel--Nielsen coordinates and collapsing collars are poor proxies for operator distance in the prime flute. The exact all-composite shift control `q_n=p_n+1` is compact-resolvent equivalent to the exact prime flute, so essential-spectrum data cannot carry prime specificity. The newer Lambert analysis further shows that the apparent gluing/cusp boundary defects do not conceal a nonsummable scalar mode. What remains is a global two-dimensional operator-comparison problem.

## Strongest justified principle

PF-121--PF-125 construct the canonical marked asymptotically bilipschitz identification and invoke the appropriate asymptotic metric comparison to obtain compact first relative resolvent and equality of essential spectra. Since every label `p_n+1` is composite, every invariant determined solely by this compact-resolvent class is closed as a rational-prime discriminator.

First-resolvent trace class is separately the wrong endpoint: PF-112 rules it out locally for a nonisometric smooth metric comparison. PF-126--PF-130 nevertheless show that the actual clone defect is far better behaved than coarse coordinates suggest: metric defect is `L^r` for every `r>1`, collapsing collars are locally `S_r`-benign for `r>1`, collar wave weights are controlled, cusp synchronization is summable, and the Lambert body has strong `L1` defect.

PF-131--PF-134 close a further family of possible assembly obstructions. The independently built Lambert pieces induce left/right traces on the same artificial split ray whose mismatch is summable on bounded height and then on the entire ray in `L-infinity + homogeneous W^{1,1}`. The tail approaches one scalar offset `c_n`; those offsets have `ell^1` variation, the centered tail is an `ell^1` family in strong `W^{1,1}`, and even `sum log(p_n)|c_n|` is finite. Thus neither deep cusp height nor the growing pre-cusp Busemann length resurrects the reciprocal-prime common mode.

## What remains possible

These trace estimates do not themselves construct a two-dimensional boundary-coherent extension, prove the Güneysu--Thalmaier-type weighted metric criterion, or establish a global `S_r`, wave/scattering, resonance, or determinant comparison. Prime specificity can survive only if such a stronger relative invariant is well defined and distinguishes the prime flute from the composite clone.

## Status / novelty

The compact-resolvent equivalence and the Lambert trace summability statements are persisted exact findings with classical analytic inputs. The conclusion is a no-go for essential-spectrum/one-dimensional-boundary discrimination, not an isospectrality or scattering-equivalence theorem.

## Falsification criterion

An essential-spectrum invariant that differs under the PF-125 identification would contradict compact-resolvent equivalence. A nonsummable canonical split-ray mode would contradict PF-131--PF-134. A genuine advance must prove or refute the remaining two-dimensional global comparison and then test the resulting stronger invariant against the clone.

## Lean-formalizable core

- Bilipschitz and trace bounds for ideal Lambert pieces.
- Summability of full split-ray mismatch and centered tail.
- Log-weighted scalar-offset summation.