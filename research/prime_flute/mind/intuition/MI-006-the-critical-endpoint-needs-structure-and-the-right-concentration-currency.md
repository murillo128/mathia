# MI-006 — The critical endpoint needs both structural coercivity and the right concentration currency

**Evidence level:** supported by exact geometric controls and literature-backed endpoint estimates through PF-196

## Core intuition

The Prime-Flute endpoint problem is not captured by a single statement such as “prove strong `L^1` rigidity.” Three different critical phenomena are now separated. Generic strong `L^1` geometric/Korn rigidity fails even after determinant-one Hamiltonian/reflection marking; one-sided weak-`S_2` localization can charge concentration much more strongly than the endpoint mass; but the symmetrized critical `L log L` currency charges the actual Lambert concentration by only one local depth logarithm, which the prime/shift tail still sums.

The useful endpoint theorem therefore has to match both **structure** and **concentration geometry**. A norm that is formally critical but charges the wrong localization profile can fail even when the total mass is summable, while a non-mass-linear Orlicz loss can still be harmless when its geometric logarithm is source-summable.

## Strongest justified principle

PF-192--PF-194 rule out deriving the desired strong endpoint from generic `r>1` rigidity by sending `r` to one, and show that exact determinant one plus Hamiltonian/reflection-compatible matrix structure does not by itself remove the Ornstein/laminate obstruction.

PF-195 shows that a generic one-sided critical Cwikel route is mismatched to the PF-191 endpoint currency: concentrated coefficients can have small `L^1` mass while the local-sup weak-`S_2` control remains too large, and the actual Lambert bodies are charged at a non-summable scale.

PF-196 gives the first positive critical accounting. The relevant symmetrized Cwikel--Solomyak theorem uses the Luxemburg norm of `Phi(t)=t log(e+t)`. For the exact-area Lambert profile that norm has scale `d(1+a)/cosh(a)`, and the exact prime/shift sequence sums this cost. More generally every fixed power of the local Lambert depth remains summable against the same geometric factor.

## Counterevidence / boundary

PF-196 does not transfer the torus/Euclidean scalar multiplication theorem to the noncompact hyperbolic vector-gradient operator, does not construct the endpoint conservative splice, and does not prove lossless global reassembly. A logarithm in local Lambert depth is not interchangeable with a logarithm in block count or singular-value index.

A PF-specific structural theorem stronger than the generic endpoint controls could still bypass the Orlicz route, but it must identify the source property that forbids the known determinant-one laminate mechanism.

## Epistemic status

**Supported endpoint synthesis with exact local accounting; global operator theorem open.**

## Falsification criterion

Either prove that the existing generic Hamiltonian/reflection/incompressibility structure yields the required strong `L^1` splice despite PF-192--PF-194, or show that every valid symmetrized estimate for the actual PF vector-gradient form necessarily incurs a loss larger than any fixed prime-summable polynomial in Lambert depth. Either result would relocate the endpoint frontier.