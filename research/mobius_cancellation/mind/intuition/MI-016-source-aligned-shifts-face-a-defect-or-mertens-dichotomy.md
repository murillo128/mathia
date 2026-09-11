# MI-016 — Möbius cancellation must be a moving-degree parity-balance law

**Evidence level:** supported by exact shell decompositions and asymptotic calibrations

## Core intuition

Residue phase is no longer a viable carrier: the selected congruence classes form one coherent inverse-limit gauge point. Nor can the missing cancellation be assigned to any fixed finite collection of square-free Hamming degrees. On the first active square-defect shell, each fixed degree is larger than the previous one by an asymptotic factor of order `loglog X/k`, so every fixed truncation is dominated by its last retained degree.

The surviving source information is therefore a **moving-degree parity-balance relation** inside the lifted constraint `n+q=d^2m`, strong enough to cancel an unsigned square-free population of almost quadratic energy down to the diagonal target scale.

## Strongest justified claim

MC-215--MC-216 show that selected-character phases, even across square moduli, are removable by one coherent unit translation. MC-217 gives a matched random-multiplicative source with identical square-free support and incidences whose shell energy already sits at the diagonal scale, showing that the power target is combinatorially possible.

MC-218 exposes why actual Möbius is different: its coherent degree-one prime layer has weighted energy polynomially above the target. MC-219 shows degree two does not cancel it; the semiprime layer overcompensates by a factor `L_X ~ loglog X`.

MC-220 extends this cascade to every fixed degree. For fixed `k`, the degree-`k` population is asymptotic to a Poisson-like factor `L_X^(k-1)/(k-1)!` times the prime population, so `B_(k+1)/B_k ~ L_X/k`. Any fixed signed truncation alternates sign and is dominated by its final term. Required cancellation must therefore involve degrees growing with `X`.

MC-221 identifies the full scale of the burden. The selected residue classes have unsigned square-free energy `X^(2-o(1))`, while the desired signed Möbius energy is at most `X^(1+o(1))`. Writing `A_d=E_d-O_d` and `N_d=E_d+O_d`, the target is an extremely small parity bias across the complete square-free population, not cancellation of one or two low-degree layers.

## Synthesis of evidence

The natural live variable is the distribution of `omega(n)` conditioned simultaneously on `(n,q)=1` and `n ≡ -q (mod d^2)`, with its alternating parity evaluated across the moving degree window where most mass lies. A useful theorem must prove square-root-scale parity cancellation **uniformly enough across the first shell** while retaining the lift and interval order erased by character gauge.

Generic multiplicative randomness remains only a matched scale control. The deterministic theorem must explain why the actual all-prime sign pattern produces the required moving-degree anti-alignment.

## Counterevidence / boundary cases

MC-219--MC-221 do not prove that the needed moving-degree cancellation fails. Fixed-degree asymptotics cannot be extrapolated automatically through the central `omega(n)` range, and that is precisely where a new uniform Sathe--Selberg/sieve-level statement would have to operate.

The gauge no-go still leaves observables that retain integer representatives, endpoints, and the lift relation.

## Epistemic status

**Supported moving-degree boundary:** every fixed Hamming-degree truncation misses the deterministic cancellation, and the full target is equivalent to a square-root-scale parity-balance theorem on a large unsigned population.

## Novelty/prior-art status

The inverse-limit gauge, random-multiplicative orthogonality, sieve/Sathe--Selberg mechanisms, and shell asymptotics retain their finding-level audits.

## Falsification criterion

Invalidate the fixed-degree cascade or the unsigned-energy/parity decomposition. Strategically, prove a uniform moving-degree parity theorem on the selected square-defect shell strong enough to reduce `E_d-O_d` to the target scale.
