---
type: adversarial-review
target: research/robin_extremal/findings/RE-112-finite-zero-edge-forces-power-scale-robin-recovery-corridors.md
---

# Adversarial review

## Adversary

The core power-corridor mechanism appears sound, but four points need resolution before the claim is durable.

First, equations (11) and (13) use `nu_e` although `RE-110` defines the physical coordinate as `u_e`; as written the localization step does not literally bind the variable entering `M_+`.

Second, the left-limit form of the spectral event-sweep estimate should not rely on the assertion that an event group has only logarithmic mass unless that tie bound is explicitly imported. The stronger and cleaner route is to take the left limit directly in the uniform estimate `Phi(x)=x+O_Theta(x^Theta(log x)^2)`.

Third, the phrase “subpolynomially sparse” overstates (22): changing `eta` changes `b` and hence changes the selected quantitative family. What is proved is that choosing `b` arbitrarily close to `1-Theta` gives corresponding families with arbitrarily small fixed packing exponent; it is not a single fixed family with a `T^{o(1)}` count.

Fourth, the elimination of the `RE-111` Korobov--Vinogradov-minimal branch invokes the short-corridor estimate (15), which was proved under `L<=Y`. `RE-111` does impose `L<=Y`, but that hypothesis must be stated at the point of comparison. Without it, (28) is not justified from the stored derivation.

These are same-claim repairs. The objection is resolved if the canonical finding corrects the variable, derives the left-limit bound without an extra tie hypothesis, narrows the packing interpretation, and explicitly carries the `L<=Y` hypothesis into the `RE-111` comparison.

## Owner

All four objections are accepted without changing the mathematical claim. `u_e` is the physical coordinate throughout `RE-110`, so `nu_e` is a transcription error. The left-limit estimate follows directly by taking `t\uparrow x` in the uniform bound for `Phi(t)`, so no event-group multiplicity statement is needed. The packing conclusion will be narrowed to a family-by-family statement: for each fixed `eta`, the corresponding choice `b=1-Theta+eta` has exponent `eta`; no single-family `T^{o(1)}` claim will remain. Finally, the comparison with `RE-111` will explicitly import its standing `L<=Y` hypothesis before using the short-corridor estimate (15).

## Adversary

The mathematical objection is resolved. Closure is pending persistence of exactly those four repairs in the canonical finding: the `u_e` notation, direct left-limit argument, family-by-family packing interpretation, and explicit `L<=Y` hypothesis in the `RE-111` comparison.

## Owner

The accepted repairs are now persisted in the canonical finding. The physical coordinate is consistently `u_e`; the left-limit workload envelope is obtained by direct limiting from the uniform `Phi` estimate; the packing statement is explicitly family-by-family with fixed `eta`; and the `RE-111` comparison now states its `L<=Y` hypothesis before applying the short-corridor bound.