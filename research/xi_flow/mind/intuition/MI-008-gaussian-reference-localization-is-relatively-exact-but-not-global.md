# MI-008 — The Xi dictionary is nonidentifiable generically but stable inside the real-divisor logarithmic class

**Evidence level:** exact center-local nullspace and heat-compatibility controls through XF-082, with exact positive real-divisor stability through XF-083

## Core intuition

The Xi source-to-Vieta interface now has a sharp admissible-class boundary. Generic center-local function approximation is too weak: exponentially invisible changes can alter the entire guarded Vieta prefix, and exact periodic heat compatibility does not remove that ambiguity. But the ambiguity disappears when the candidate carrier has a **real periodic divisor** and the source is compared through its logarithmic derivative.

The live problem is therefore no longer generic inverse conditioning. It is an **existence/root-faithfulness problem**: can the actual transported Xi source be placed in the real-divisor class at the available exponential accuracy on the relevant slice?

## Strongest justified principle

XF-078--XF-080 show that local mode count and local function accuracy do not control normalized Vieta coordinates. XF-081 makes the failure structural: a Chebyshev nullspace is exponentially small on the actual center high-line geometry while allowing an arbitrarily long growing edge/Vieta prefix to be prescribed. XF-082 evolves both the original and repaired carriers by the exact same periodic backward heat equation and proves that they remain exponentially indistinguishable on every Xi-relevant fixed heat interval while their low Vieta states stay macroscopically different.

Thus neither static accuracy nor free-heat compatibility identifies the source state in the unrestricted polynomial class.

XF-083 supplies the positive constraint. If the periodic roots all lie on the unit circle, the centered logarithmic derivative is a one-sided Hardy generating function for the root power sums. A two-constants/harmonic-measure argument turns exponential agreement on only the center half-arc into coefficient bounds with loss `(2/r)^m`. At Xi scale the available error is `exp(-Theta(D))` or better, while every source-visible guarded mode has `m=o(D)`, so the whole low power-sum range and exact XF-079 selector are exponentially stable.

The Chebyshev controls therefore fail precisely because they leave the real-divisor class. Inside that class, one-center logarithmic data is quantitatively sufficient without root matching, simplicity, or a gap lower bound.

## Counterevidence / boundary

XF-083 is conditional on two same-degree real-divisor periodic carriers. It does not construct one from Xi and does not apply through a genuinely complex-root interval. The positive-time/reference transport may fail to enter the class or may consume the source margin before the real-rooted slice is reached.

The remote guarded-mass control remains valid for weaker interfaces based only on local root agreement. The strength of XF-083 is exactly that it controls the power sums through the logarithmic field rather than through local root matching.

## Epistemic status

**Proved nonidentifiability outside the class and proved stability inside the class; open source realization.** The current Xi clue `CLUE-relative-xi-source-to-guarded-selector-stability` owns the unproved source-to-class handoff.

## Falsification criterion

Construct two same-degree real-divisor carriers satisfying XF-083's exponentially close center-half-line logarithmic data but with macroscopically different guarded power sums, or construct the required real-rooted Xi carrier with the stated accuracy and track it into the guarded selector. The first would invalidate the positive interface; the second would close the present dictionary gate.